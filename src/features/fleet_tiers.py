"""
src/features/fleet_tiers.py
---------------------------
High-Cardinality Airframe Gauge Tiering (REC-04).

Segments flights into three structural airframe gauge tiers:
1. Regional Tier (<= 76 seats: CRJ-700/900, E170/175):
   - Modal lead: 55 min, Boarding cutoff: T-25 min
2. Narrowbody Mainline (77-210 seats: A320/321, B737-800/900/MAX, A220):
   - Modal lead: 95 min, Boarding cutoff: T-35 min
3. Widebody Transcontinental / International (> 210 seats: B777, B787, A350, A330):
   - Modal lead: 140 min, Boarding cutoff: T-50 min
"""

import pandas as pd
import numpy as np

GAUGE_TIER_PARAMS = {
    "Regional":   {"max_seats": 76,  "modal_lead_min": 55,  "gate_cutoff_min": 25},
    "Narrowbody": {"max_seats": 210, "modal_lead_min": 95,  "gate_cutoff_min": 35},
    "Widebody":   {"max_seats": 999, "modal_lead_min": 140, "gate_cutoff_min": 50}
}

def assign_fleet_gauge_tier(seats: int) -> str:
    """Classifies seating capacity into Regional, Narrowbody, or Widebody."""
    if pd.isna(seats):
        return "Narrowbody"
    s = float(seats)
    if s <= 76:
        return "Regional"
    elif s <= 210:
        return "Narrowbody"
    else:
        return "Widebody"

def apply_fleet_tiering(df: pd.DataFrame, seat_col: str = "Scheduled_Seats") -> pd.DataFrame:
    """
    Applies airframe gauge tiering and assigns structural capacity features.
    """
    res = df.copy()
    if seat_col not in res.columns:
        # Default placeholder if seat column absent
        res[seat_col] = 165
        
    res["gauge_tier"] = res[seat_col].apply(assign_fleet_gauge_tier)
    res["gauge_modal_lead_min"] = res["gauge_tier"].map(lambda t: GAUGE_TIER_PARAMS[t]["modal_lead_min"])
    res["gauge_gate_cutoff_min"] = res["gauge_tier"].map(lambda t: GAUGE_TIER_PARAMS[t]["gate_cutoff_min"])
    
    # One-hot encoding for machine learning inputs
    res["is_regional"] = (res["gauge_tier"] == "Regional").astype(np.int8)
    res["is_narrowbody"] = (res["gauge_tier"] == "Narrowbody").astype(np.int8)
    res["is_widebody"] = (res["gauge_tier"] == "Widebody").astype(np.int8)
    
    return res

if __name__ == "__main__":
    df = pd.DataFrame({"Scheduled_Seats": [70, 160, 220, 76, 210, 300]})
    out = apply_fleet_tiering(df)
    print(out[["Scheduled_Seats", "gauge_tier", "gauge_modal_lead_min", "is_widebody"]])
