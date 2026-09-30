import os
import sys
import unittest
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from etl.apply_4tier_filtering import apply_four_tier_filtering, get_unique_cohort_airports


class TestFourTierFiltering(unittest.TestCase):
    def test_four_tier_filtering_cohort(self):
        """Verify 4-tier filtering produces the balanced 4x4 factorial design across 9 airports."""
        cohort = apply_four_tier_filtering()
        self.assertIsInstance(cohort, pd.DataFrame)
        self.assertEqual(len(cohort), 12)  # 12 carrier-hub facilities
        
        # Check carrier symmetry (4 AA, 4 DL, 4 UA)
        carrier_counts = cohort["carrier"].value_counts().to_dict()
        self.assertEqual(carrier_counts, {"AA": 4, "DL": 4, "UA": 4})
        
        # Check 9 unique airports
        expected_airports = {"DFW", "PHL", "ORD", "DTW", "LGA", "BOS", "EWR", "IAH", "LAX"}
        self.assertEqual(set(cohort["airport"]), expected_airports)
        self.assertEqual(len(get_unique_cohort_airports()), 9)
        
        # Verify DFW includes Terminals A, B, C for AA
        dfw_row = cohort[(cohort["airport"] == "DFW") & (cohort["carrier"] == "AA")].iloc[0]
        self.assertIn("Terminals A, B, C", dfw_row["facility"])

if __name__ == "__main__":
    unittest.main()
