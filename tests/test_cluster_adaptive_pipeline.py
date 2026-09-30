"""
tests/test_cluster_adaptive_pipeline.py
---------------------------------------
Unit tests for REC-02 (Cluster-Adaptive Kernels), REC-03 (Demand Deflation),
REC-07 (Airside Surface Queuing), and REC-13 (Checkpoint Confidence).
"""

import unittest
import numpy as np
import pandas as pd

from src.features.demand_deflat import (
    get_connecting_ratio,
    get_originating_multiplier,
    compute_originating_demand
)
from src.features.cluster_adapt import (
    compute_cluster_weights,
    convolve_cluster_adaptive_demand
)
from src.features.airside_flow import compute_airside_interactions
from src.features.checkpoint_map import (
    get_checkpoint_confidence,
    compute_checkpoint_weights
)
from src.features.feature_pipeline import build_conformed_feature_matrix

class TestClusterAdaptivePipeline(unittest.TestCase):
    def test_connecting_ratios(self):
        # DFW must have ~66.3% connecting ratio
        self.assertAlmostEqual(get_connecting_ratio("DFW"), 0.663, places=2)
        # LGA must have ~8.2% connecting ratio
        self.assertAlmostEqual(get_connecting_ratio("LGA"), 0.082, places=2)
        # Originating multiplier: DFW ~ 0.337, LGA ~ 0.918
        self.assertAlmostEqual(get_originating_multiplier("DFW"), 0.337, places=2)
        self.assertAlmostEqual(get_originating_multiplier("LGA"), 0.918, places=2)

    def test_demand_deflation_reduction(self):
        df = pd.DataFrame({
            "Airport": ["DFW", "LGA"],
            "Scheduled_Seats": [1000, 1000],
            "Load_Factor": [1.0, 1.0]
        })
        out = compute_originating_demand(df)
        dfw_dem = out[out["Airport"] == "DFW"]["net_originating_demand"].iloc[0]
        lga_dem = out[out["Airport"] == "LGA"]["net_originating_demand"].iloc[0]
        # DFW net demand must be much smaller than LGA for same seat count
        self.assertAlmostEqual(dfw_dem, 337.0, places=0)
        self.assertAlmostEqual(lga_dem, 918.0, places=0)

    def test_cluster_weights_normalization_and_peaks(self):
        # All cluster weights must normalize to 1.0
        for c in range(4):
            w = compute_cluster_weights(c)
            self.assertEqual(len(w), 3)
            self.assertAlmostEqual(w.sum(), 1.0, places=5)
            
        # Cluster 0 (Mega Hub) modal peak at 115m -> t+2 must be largest weight
        w0 = compute_cluster_weights(0)
        self.assertGreater(w0[1], w0[0])
        self.assertGreater(w0[1], w0[2])
        
        # Cluster 1 (O&D Focus) modal peak at 65m -> t+1 must be largest weight
        w1 = compute_cluster_weights(1)
        self.assertGreater(w1[0], w1[1])
        self.assertGreater(w1[0], w1[2])

    def test_airside_taxi_interaction_conditional(self):
        df = pd.DataFrame({
            "Airport": ["EWR", "DFW"],
            "cluster_id": [3, 0],
            "avg_taxi_out": [25.0, 18.0],
            "convolved_lead1": [500.0, 500.0]
        })
        out = compute_airside_interactions(df)
        # Cluster 3 (EWR) should have positive taxi interaction
        self.assertGreater(out[out["Airport"] == "EWR"]["taxi_congestion_interaction"].iloc[0], 0.0)
        # Cluster 0 (DFW) should have 0.0 taxi interaction
        self.assertEqual(out[out["Airport"] == "DFW"]["taxi_congestion_interaction"].iloc[0], 0.0)

    def test_checkpoint_confidence_tiers(self):
        # Tier 1 exclusive: 1.0
        self.assertEqual(get_checkpoint_confidence("DTW_McNamara_Red"), 1.0)
        self.assertEqual(get_checkpoint_confidence("EWR_TermC_CKPT1"), 1.0)
        # Tier 2 shared: 0.8
        self.assertEqual(get_checkpoint_confidence("ORD_Term3_CKPT7"), 0.80)
        # Tier 3 central: 0.5
        self.assertEqual(get_checkpoint_confidence("IAD_Main_East"), 0.50)

    def test_full_conformed_feature_pipeline(self):
        sample_df = pd.DataFrame({
            "Airport": ["DFW", "ORD", "BOS", "EWR"],
            "Hour": [6, 9, 14, 18],
            "Date": ["2023-06-01", "2023-06-01", "2023-06-01", "2023-06-01"],
            "Scheduled_Seats": [1200, 1500, 900, 1100],
            "Scheduled_Departures": [8, 10, 6, 7],
            "TSA_Throughput": [1100, 1400, 750, 980],
            "avg_taxi_out": [18.0, 21.0, 16.5, 27.0]
        })
        feat_df = build_conformed_feature_matrix(sample_df)
        # Check generated column presence
        expected_cols = [
            "minute_of_day", "sin_diurnal", "cos_diurnal",
            "gauge_tier", "is_narrowbody",
            "connecting_ratio", "net_originating_demand",
            "convolved_lead1", "convolved_lead2", "convolved_lead3",
            "taxi_congestion_interaction", "checkpoint_confidence_factor"
        ]
        for col in expected_cols:
            self.assertIn(col, feat_df.columns)

if __name__ == "__main__":
    unittest.main()
