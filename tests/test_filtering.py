import unittest
import pandas as pd
from etl.apply_4tier_filtering import apply_four_tier_filtering

class TestFourTierFiltering(unittest.TestCase):
    def test_four_tier_filtering_cohort(self):
        """Verify 4-tier filtering produces the balanced 9-airport experimental cohort."""
        cohort = apply_four_tier_filtering()
        self.assertIsInstance(cohort, pd.DataFrame)
        self.assertEqual(len(cohort), 9)
        
        # Check carrier symmetry (3 AA, 3 DL, 3 UA)
        carrier_counts = cohort["carrier"].value_counts().to_dict()
        self.assertEqual(carrier_counts, {"AA": 3, "DL": 3, "UA": 3})
        
        # Check key airports
        expected_airports = {"DFW", "PHL", "ORD", "DTW", "LGA", "BOS", "EWR", "IAH", "LAX"}
        self.assertEqual(set(cohort["airport"]), expected_airports)

if __name__ == "__main__":
    unittest.main()
