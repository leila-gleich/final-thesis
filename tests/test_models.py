"""
tests/test_models.py
--------------------
Unit tests for candidate model estimators (Baseline Control, Model 1, Model 2, Model 3)
and evaluation frameworks (REC-05, REC-11, REC-12).
"""

import os
import sys
import unittest
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from models.baselines import DiurnalSeasonalNaive, DeterministicFixedLeadBaseline
from models.machine_learning import TweedieGradientBoostedRegressor
from models.hybrid_sarima_tree import SequentialSARIMATreeHybrid
from models.eval_pillars import MultiPillarEvaluator, compute_rmse, compute_mae, compute_mase
from models.dual_track_eval import run_dual_track_evaluation

class TestModelEstimators(unittest.TestCase):
    def setUp(self):
        n = 100
        self.df = pd.DataFrame({
            "TSA_Throughput": np.linspace(400, 1600, n),
            "convolved_lead1": np.linspace(300, 1000, n),
            "convolved_lead2": np.linspace(400, 1400, n),
            "convolved_lead3": np.linspace(200, 800, n),
            "minute_of_day": np.tile(np.arange(0, 1440, 1440/10), 10),
            "sin_diurnal": np.sin(np.linspace(0, 2*np.pi, n)),
            "cos_diurnal": np.cos(np.linspace(0, 2*np.pi, n)),
            "sin_weekly": np.sin(np.linspace(0, 2*np.pi, n)),
            "cos_weekly": np.cos(np.linspace(0, 2*np.pi, n)),
            "is_regional": 0, "is_narrowbody": 1, "is_widebody": 0,
            "originating_multiplier": 0.65,
            "taxi_out_duration": 18.0,
            "taxi_congestion_interaction": 0.0
        })

    def test_diurnal_seasonal_naive(self):
        baseline_ctrl = DiurnalSeasonalNaive(lag_hours=24)
        preds = baseline_ctrl.predict(self.df, target_col="TSA_Throughput")
        self.assertEqual(len(preds), len(self.df))
        self.assertTrue((preds >= 0).all())

    def test_deterministic_fixed_lead_baseline(self):
        model1 = DeterministicFixedLeadBaseline()
        model1.fit(self.df, self.df["TSA_Throughput"])
        preds = model1.predict(self.df)
        self.assertEqual(len(preds), len(self.df))
        self.assertTrue((preds >= 0).all())

    def test_tweedie_gbr_estimator(self):
        model2 = TweedieGradientBoostedRegressor(max_iter=30)
        model2.fit(self.df, self.df["TSA_Throughput"])
        preds = model2.predict(self.df)
        self.assertEqual(len(preds), len(self.df))
        self.assertTrue((preds >= 0).all())

    def test_sequential_sarima_tree_hybrid(self):
        model3 = SequentialSARIMATreeHybrid()
        model3.fit(self.df, self.df["TSA_Throughput"])
        preds = model3.predict(self.df, y_true_for_feedback=self.df["TSA_Throughput"])
        self.assertEqual(len(preds), len(self.df))
        self.assertTrue((preds >= 0).all())

    def test_probabilistic_quantiles(self):
        model3 = SequentialSARIMATreeHybrid()
        model3.fit(self.df, self.df["TSA_Throughput"])
        q_dict = model3.predict_quantiles(self.df, quantiles=(0.10, 0.50, 0.85, 0.90))
        self.assertIn(0.85, q_dict)
        self.assertEqual(len(q_dict[0.85]), len(self.df))
        # 85th percentile upper bound must be greater than or equal to 10th percentile bound
        self.assertTrue((q_dict[0.85] >= q_dict[0.10]).all())

    def test_multi_pillar_evaluator(self):
        y_true = np.array([500, 800, 1200, 1500, 600] * 10)
        y_pred = y_true + 20.0
        evaluator = MultiPillarEvaluator(y_true, y_pred)
        results = evaluator.full_evaluation()
        
        self.assertIn("routine_rmse", results)
        self.assertIn("routine_mae", results)
        self.assertIn("routine_mase", results)
        self.assertIn("max_ae", results)
        self.assertIn("rtr", results)
        self.assertAlmostEqual(results["routine_mae"], 20.0, places=1)

    def test_dual_track_framework_execution(self):
        df_a, df_b = run_dual_track_evaluation()
        self.assertIsInstance(df_a, pd.DataFrame)
        self.assertIsInstance(df_b, pd.DataFrame)
        self.assertEqual(len(df_a), 4)
        self.assertEqual(len(df_b), 4)

if __name__ == "__main__":
    unittest.main()
