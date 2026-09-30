"""
src/features/demand_deflat.py
-----------------------------
Mandatory DB1B/DB1C Connecting Ratio Capacity Deflation (REC-03).

Deflates scheduled departing flight capacity by empirical connecting ratios to derive
true landside originating passenger demand:
    NetOriginatingDemand = Scheduled_Seats * Load_Factor * (1.0 - Connecting_Ratio)
"""

import pandas as pd
import numpy as np

# Official empirical connecting ratios from BTS DB1B ticket survey for the 9-airport cohort
AIRPORT_CONNECTING_RATIOS = {
    "DFW": 0.663,  # Dallas/Fort Worth: 66.3% connecting -> 33.7% local
    "ORD": 0.600,  # Chicago O'Hare: 60.0% connecting -> 40.0% local
    "DTW": 0.528,  # Detroit: 52.8% connecting -> 47.2% local
    "IAH": 0.485,  # Houston Intercontinental: 48.5% connecting -> 51.5% local
    "PHL": 0.412,  # Philadelphia: 41.2% connecting -> 58.8% local
    "LAX": 0.320,  # Los Angeles: 32.0% connecting -> 68.0% local
    "EWR": 0.285,  # Newark: 28.5% connecting -> 71.5% local
    "BOS": 0.184,  # Boston: 18.4% connecting -> 81.6% local
    "LGA": 0.082   # LaGuardia: 8.2% connecting -> 91.8% local
}

# Default network average for other Top 25 airfields
DEFAULT_CONNECTING_RATIO = 0.450

def get_connecting_ratio(airport: str) -> float:
    """Returns empirical connecting fraction for an airport."""
    if not isinstance(airport, str):
        return DEFAULT_CONNECTING_RATIO
    return AIRPORT_CONNECTING_RATIOS.get(airport.strip().upper(), DEFAULT_CONNECTING_RATIO)

def get_originating_multiplier(airport: str) -> float:
    """Returns originating demand multiplier (1.0 - connecting_ratio)."""
    return 1.0 - get_connecting_ratio(airport)

def compute_originating_demand(
    df: pd.DataFrame,
    airport_col: str = "Airport",
    seats_col: str = "Scheduled_Seats",
    load_factor_col: str = "Load_Factor"
) -> pd.DataFrame:
    """
    Computes net originating passenger demand by deflating seats by connecting ratio
    and scaling by route/segment load factor.
    """
    res = df.copy()
    
    # Map connecting ratio and originating multiplier
    if airport_col in res.columns:
        res["connecting_ratio"] = res[airport_col].apply(get_connecting_ratio).astype(np.float32)
    else:
        res["connecting_ratio"] = DEFAULT_CONNECTING_RATIO
        
    res["originating_multiplier"] = (1.0 - res["connecting_ratio"]).astype(np.float32)
    
    # Load factor (default to national average 84.7% if missing)
    if load_factor_col in res.columns:
        lf = res[load_factor_col].fillna(0.847).astype(np.float32)
    else:
        lf = 0.847
    res["effective_load_factor"] = lf
    
    # Seats column
    if seats_col in res.columns:
        seats = res[seats_col].astype(float)
    elif "Scheduled_Departures" in res.columns:
        # Estimate average 165 seats per flight if only flight count available
        seats = res["Scheduled_Departures"].astype(float) * 165.0
    else:
        seats = 165.0
        
    res["gross_seat_capacity"] = seats
    res["net_originating_demand"] = (seats * lf * res["originating_multiplier"]).astype(np.float32)
    
    return res

if __name__ == "__main__":
    test_df = pd.DataFrame({
        "Airport": ["DFW", "ORD", "LGA", "BOS"],
        "Scheduled_Seats": [1000, 1000, 1000, 1000],
        "Load_Factor": [0.85, 0.85, 0.85, 0.85]
    })
    out = compute_originating_demand(test_df)
    print(out[["Airport", "connecting_ratio", "originating_multiplier", "net_originating_demand"]])
