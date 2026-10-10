"""
tests/test_feature_pipeline.py
------------------------------
Unit tests for the integrated master feature engineering pipeline (REC-01 to REC-13).
"""

import os
import sys
import unittest
import pandas as pd
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from features.feature_pipeline import build_conformed_feature_matrix

class TestFeaturePipeline(unittest.TestCase):
    def setUp(self):
        self.sample_df = pd.DataFrame({
            "Airport": ["DFW", "ORD", "BOS", "EWR", "DTW", "LGA"],
            "Hour": [7, 8, 14, 18, 10, 16],
            "Date": ["2023-05-01", "2023-05-01", "2023-05-02", "2023-05-02", "2023-05-03", "2023-05-03"],
            "Scheduled_Seats": [1500, 1800, 800, 1200, 1400, 950],
            "Scheduled_Departures": [10, 12, 6, 8, 9, 7],
            "TSA_Throughput": [1250, 1500, 680, 1100, 1150, 890],
            "avg_taxi_out": [18.5, 20.2, 17.0, 26.5, 19.0, 22.1]
        })

    def test_build_conformed_feature_matrix(self):
        feat_df = build_conformed_feature_matrix(self.sample_df)

        self.assertIsInstance(feat_df, pd.DataFrame)
        self.assertEqual(len(feat_df), len(self.sample_df), "Feature pipeline must preserve row count")

        # Verify REC-01 temporal cyclical features
        for col in ["minute_of_day", "sin_diurnal", "cos_diurnal", "sin_weekly", "cos_weekly"]:
            self.assertIn(col, feat_df.columns, f"Missing REC-01 feature: {col}")

        # Verify REC-04 fleet tiering features
        for col in ["gauge_tier", "is_regional", "is_narrowbody", "is_widebody"]:
            self.assertIn(col, feat_df.columns, f"Missing REC-04 feature: {col}")

        # Verify REC-03 demand deflation features
        for col in ["connecting_ratio", "originating_multiplier", "net_originating_demand"]:
            self.assertIn(col, feat_df.columns, f"Missing REC-03 feature: {col}")

        # Verify REC-02 arrival convolution features
        for col in ["cluster_id", "convolved_lead1", "convolved_lead2", "convolved_lead3"]:
            self.assertIn(col, feat_df.columns, f"Missing REC-02 feature: {col}")

        # Verify REC-07 airside surface interaction features
        for col in ["taxi_out_duration", "taxi_congestion_interaction"]:
            self.assertIn(col, feat_df.columns, f"Missing REC-07 feature: {col}")

        # Verify REC-13 checkpoint confidence weighting features
        self.assertIn("checkpoint_confidence_factor", feat_df.columns, "Missing REC-13 feature: checkpoint_confidence_factor")
        self.assertTrue((feat_df["checkpoint_confidence_factor"] >= 0.50).all())

if __name__ == "__main__":
    unittest.main()
