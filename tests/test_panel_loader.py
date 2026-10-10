"""
tests/test_panel_loader.py
--------------------------
Unit tests for centralized panel data loading and volatility metric preparation (REC-06).
"""

import os
import sys
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from data.panel_loader import load_and_prepare_panel_data, CURATED_HOURLY_AIRPORTS
from utils.paths import HOURLY_CURATED_PATH

class TestPanelLoader(unittest.TestCase):
    def test_load_and_prepare_panel_data(self):
        """Verify panel data loader returns valid, conformed dataframes."""
        df_panel, df_census = load_and_prepare_panel_data()
        
        self.assertIsInstance(df_panel, pd.DataFrame)
        self.assertIsInstance(df_census, pd.DataFrame)
        self.assertGreater(len(df_panel), 0, "Panel dataframe must not be empty")
        self.assertGreater(len(df_census), 0, "Census dataframe must not be empty")

        # Verify essential columns exist
        expected_cols = [
            "Date", "Airport", "tsa_hourly_std", "tsa_hourly_cv",
            "sched_hourly_std", "actual_hourly_std", "avg_dep_delay_minutes"
        ]
        for col in expected_cols:
            self.assertIn(col, df_panel.columns, f"Missing required column: {col}")

        # Verify cohort containment
        airports_found = set(df_panel["Airport"].unique())
        self.assertEqual(airports_found, CURATED_HOURLY_AIRPORTS)

        # Verify volatility metrics are non-negative
        self.assertTrue((df_panel["tsa_hourly_std"].dropna() >= 0).all())
        self.assertTrue((df_panel["tsa_hourly_cv"].dropna() >= 0).all())

if __name__ == "__main__":
    unittest.main()
