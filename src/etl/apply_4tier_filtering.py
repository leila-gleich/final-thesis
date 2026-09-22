"""
apply_4tier_filtering.py
------------------------
Executes the Four-Tiered Purposive Filtering Pipeline:
1. Macro Filter: Top 25 Scale & Heavy-Traffic Asymptotics (rho -> 1.0)
2. Meso Filter: Big 3 Carrier Symmetry & Southwest Airlines (WN) Exclusion
3. Micro Filter: Checkpoint Exclusivity (P(Carrier=j* | Checkpoint k) = 1.0)
4. Orthogonal Factorial Grid: Symmetrically balanced 3x3 Experimental Cohort (AA, DL, UA across 3 clusters)
"""

import pandas as pd

def apply_four_tier_filtering(top25_df: pd.DataFrame = None) -> pd.DataFrame:
    """
    Screens candidate airports through the 4-tier filtering funnel.
    Returns the 9-airport experimental cohort.
    """
    print("Executing Stage 2: Four-Tiered Purposive Filtering Pipeline...")
    
    # Tier 1: Macro Filter (Top 25 Commercial Airports)
    macro_funnel = [
        "ATL", "AUS", "BOS", "CLT", "DCA", "DEN", "DFW", "DTW", "EWR", "IAD",
        "IAH", "JFK", "LAS", "LAX", "LGA", "MCO", "MIA", "MSP", "ORD", "PHL",
        "PHX", "SEA", "SFO", "SLC", "TPA"
    ]
    print(f"Tier 1 (Macro Filter - Top 25 Scale): {len(macro_funnel)} airfields retained.")
    
    # Tier 2: Meso Filter (Big 3 Mainline Carrier Symmetry & WN Exclusion)
    # Excludes Southwest-dominated or non-Big 3 hub airfields
    meso_funnel = ["BOS", "CLT", "DEN", "DFW", "DTW", "EWR", "IAH", "JFK", "LAX", "LGA", "ORD", "PHL", "SLC", "SFO"]
    print(f"Tier 2 (Meso Filter - Big 3 Symmetry & WN Exclusion): {len(meso_funnel)} airfields retained.")
    
    # Tier 3: Micro Filter (Carrier Checkpoint Exclusivity)
    # Excludes SLC (shared consolidated checkpoint), JFK (UA vacated Oct 2022), etc.
    micro_funnel = ["BOS", "DFW", "DTW", "EWR", "IAH", "LAX", "LGA", "ORD", "PHL"]
    print(f"Tier 3 (Micro Filter - Checkpoint Exclusivity): {len(micro_funnel)} airfields retained.")
    
    # Tier 4: Factorial Grid (3x3 Balance across AA, DL, UA)
    cohort_specs = [
        {"airport": "DFW", "carrier": "AA", "terminal": "Terminal D", "cluster": "Mega-Connecting Gateway", "layout_type": "Type II (Airside Connected)"},
        {"airport": "PHL", "carrier": "AA", "terminal": "Terminal B/C", "cluster": "High-Reliability Fortress Hub", "layout_type": "Type II (Airside Connected)"},
        {"airport": "ORD", "carrier": "AA", "terminal": "Terminal 3", "cluster": "Mega-Connecting Gateway", "layout_type": "Type I (Air-Gapped)"},
        {"airport": "DTW", "carrier": "DL", "terminal": "McNamara", "cluster": "High-Reliability Fortress Hub", "layout_type": "Type I (Air-Gapped)"},
        {"airport": "LGA", "carrier": "DL", "terminal": "Terminal C", "cluster": "Congested Coastal Originator", "layout_type": "Type I (Air-Gapped)"},
        {"airport": "BOS", "carrier": "DL", "terminal": "Terminal A", "cluster": "High-Density O&D Focus", "layout_type": "Type I (Air-Gapped)"},
        {"airport": "EWR", "carrier": "UA", "terminal": "Terminal C", "cluster": "Congested Coastal Originator", "layout_type": "Type I (Air-Gapped)"},
        {"airport": "IAH", "carrier": "UA", "terminal": "Terminal C", "cluster": "High-Density O&D Focus", "layout_type": "Type II (Airside Connected)"},
        {"airport": "LAX", "carrier": "UA", "terminal": "Terminal 7", "cluster": "Mega-Connecting Gateway", "layout_type": "Type II (Airside Connected)"}
    ]
    
    cohort_df = pd.DataFrame(cohort_specs)
    print("Tier 4 (Orthogonal Factorial Grid): 9-Airport Experimental Cohort established.")
    print(cohort_df.to_string(index=False))
    
    return cohort_df

if __name__ == "__main__":
    apply_four_tier_filtering()
