"""
tests/test_time_features.py
---------------------------
Unit tests for REC-01 Minute-of-Day & Diurnal/Weekly Cyclical Terms.
"""

import unittest
import numpy as np
import pandas as pd
from src.features.time_features import generate_temporal_features

class TestTimeFeatures(unittest.TestCase):
    def test_minute_of_day_bounds(self):
        times = ["2023-01-01 00:00:00", "2023-01-01 12:30:00", "2023-01-01 23:59:00"]
        df = pd.DataFrame({"Scheduled_Departure_Time": times})
        out = generate_temporal_features(df)
        self.assertEqual(out["minute_of_day"].iloc[0], 0)
        self.assertEqual(out["minute_of_day"].iloc[1], 750)
        self.assertEqual(out["minute_of_day"].iloc[2], 1439)
        self.assertTrue((out["minute_of_day"] >= 0).all() and (out["minute_of_day"] <= 1439).all())

    def test_trigonometric_pythagorean_identity(self):
        df = pd.DataFrame({
            "Scheduled_Departure_Time": pd.date_range("2023-05-01", periods=100, freq="15min")
        })
        out = generate_temporal_features(df)
        
        # sin^2 + cos^2 == 1.0 (within float32 precision)
        diurnal_sq = out["sin_diurnal"]**2 + out["cos_diurnal"]**2
        weekly_sq  = out["sin_weekly"]**2 + out["cos_weekly"]**2
        
        np.testing.assert_allclose(diurnal_sq, 1.0, atol=1e-5)
        np.testing.assert_allclose(weekly_sq, 1.0, atol=1e-5)

if __name__ == "__main__":
    unittest.main()
