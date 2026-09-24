import os
import sys
import unittest
import duckdb
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from features import compute_arrival_weights, convolve_scheduled_demand, AirportSelector

class TestFeatures(unittest.TestCase):
    def test_arrival_weights_normalization(self):
        """Verify empirical arrival kernel weights sum to 1.0."""
        weights = compute_arrival_weights()
        self.assertEqual(len(weights), 3)
        self.assertAlmostEqual(weights.sum(), 1.0, places=6)
        # Peak lead (t+2) should have largest weight
        self.assertGreater(weights[1], weights[0])
        self.assertGreater(weights[1], weights[2])

    def test_convolve_scheduled_demand(self):
        """Verify convolving scheduled flights computes lead horizons correctly."""
        df = pd.DataFrame({
            "seats": [150.0, 200.0],
            "load_factor": [0.85, 0.90],
            "connecting_ratio": [0.50, 0.40]
        })
        convolved = convolve_scheduled_demand(df)
        self.assertIn("convolved_demand_lead1", convolved.columns)
        self.assertIn("convolved_demand_lead2", convolved.columns)
        self.assertIn("convolved_demand_lead3", convolved.columns)
        self.assertIn("convolved_total_demand", convolved.columns)
        
        # Total demand should equal sum of lead demands
        lead_sum = convolved["convolved_demand_lead1"] + convolved["convolved_demand_lead2"] + convolved["convolved_demand_lead3"]
        for total, s in zip(convolved["convolved_total_demand"], lead_sum):
            self.assertAlmostEqual(total, s, places=5)

    def test_airport_selector_curated(self):
        """Verify AirportSelector can query curated hourly dataset."""
        con = duckdb.connect()
        top_airports = AirportSelector.get_top_airports(con, n=5, dataset="otp")
        self.assertEqual(len(top_airports), 5)
        for apt in ["DFW", "ORD"]:
            self.assertIn(apt, top_airports)

if __name__ == "__main__":
    unittest.main()
