"""
src/features/feature_pipeline.py
--------------------------------
Master Feature Engineering Pipeline.
Integrates REC-01, REC-02, REC-03, REC-04, REC-07, and REC-13 into a single
unified, reproducible transformer pipeline for the 9-airport experimental cohort.
"""

import pandas as pd
import numpy as np

from src.features.time_features import generate_temporal_features
from src.features.fleet_tiers import apply_fleet_tiering
from src.features.demand_deflat import compute_originating_demand
from src.features.cluster_adapt import convolve_cluster_adaptive_demand
from src.features.airside_flow import compute_airside_interactions
from src.features.checkpoint_map import compute_checkpoint_weights

def build_conformed_feature_matrix(
    df: pd.DataFrame,
    airport_col: str = "Airport",
    date_col: str = "Date",
    hour_col: str = "Hour",
    seats_col: str = "Scheduled_Seats",
    throughput_col: str = "TSA_Throughput"
) -> pd.DataFrame:
    """
    Executes the full physics-informed feature pipeline:
    1. Temporal terms: minute-of-day, diurnal and weekly sin/cos cycles (REC-01).
    2. Fleet tiering: Regional, Narrowbody, Widebody categorizations (REC-04).
    3. Demand deflation: BTS DB1B connecting ratio adjustments (REC-03).
    4. Cluster-adaptive convolution: Cluster 0-3 lognormal arrival kernels (REC-02).
    5. Airside surface queuing & taxi interactions (REC-07).
    6. Airline-to-checkpoint spatial scaling & confidence tiers (REC-13).
    """
    res = df.copy()
    
    # 1. Temporal cyclical features
    if hour_col in res.columns:
        res = generate_temporal_features(res, time_col=hour_col)
    elif "Time" in res.columns:
        res = generate_temporal_features(res, time_col="Time")
        
    # 2. Fleet gauge tiering
    res = apply_fleet_tiering(res, seat_col=seats_col)
    
    # 3. DB1B Connecting ratio deflation
    res = compute_originating_demand(res, airport_col=airport_col, seats_col=seats_col)
    
    # 4. Cluster-adaptive lognormal arrival convolution
    res = convolve_cluster_adaptive_demand(res, demand_col="net_originating_demand", airport_col=airport_col)
    
    # 5. Airside surface taxi-out & delay interactions
    res = compute_airside_interactions(res, lead1_col="convolved_lead1", cluster_col="cluster_id")
    
    # 6. Checkpoint spatial confidence weighting
    res = compute_checkpoint_weights(res)
    
    return res

if __name__ == "__main__":
    sample_df = pd.DataFrame({
        "Airport": ["DFW", "ORD", "BOS", "EWR"],
        "Hour": [7, 8, 14, 18],
        "Date": ["2023-05-01", "2023-05-01", "2023-05-01", "2023-05-01"],
        "Scheduled_Seats": [1500, 1800, 800, 1200],
        "Scheduled_Departures": [10, 12, 6, 8],
        "TSA_Throughput": [1250, 1500, 680, 1100],
        "avg_taxi_out": [18.5, 20.2, 17.0, 26.5]
    })
    
    feat_df = build_conformed_feature_matrix(sample_df)
    print("Conformed Feature Pipeline Matrix Generated successfully:")
    print("Columns:", feat_df.columns.tolist())
    print("Shape:", feat_df.shape)
