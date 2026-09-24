import unittest
import numpy as np
import pandas as pd
from models.baselines import DiurnalSeasonalNaive, DeterministicFixedLeadBaseline

class TestBaselineModels(unittest.TestCase):
    def test_diurnal_seasonal_naive(self):
        """Verify DiurnalSeasonalNaive lags 24 time steps."""
        df = pd.DataFrame({"actual_tsa": np.arange(48, dtype=float)})
        model = DiurnalSeasonalNaive(lag=24)
        preds = model.predict(df)
        self.assertEqual(len(preds), 48)
        self.assertEqual(preds[0], 0.0)
        self.assertEqual(preds[24], 0.0)
        self.assertEqual(preds[25], 1.0)
        self.assertEqual(preds[47], 23.0)

    def test_deterministic_fixed_lead_baseline(self):
        """Verify DeterministicFixedLeadBaseline applies static 2-hour lead formula."""
        df = pd.DataFrame({"lead_seats_t2": [0.0, 150.0, 300.0]})
        model = DeterministicFixedLeadBaseline(beta_lead=75.0, intercept=10.0)
        preds = model.predict(df)
        self.assertEqual(len(preds), 3)
        self.assertEqual(preds[0], 10.0)
        self.assertAlmostEqual(preds[1], 85.0, places=4)
        self.assertAlmostEqual(preds[2], 160.0, places=4)

if __name__ == "__main__":
    unittest.main()
