"""
src/models/hybrid_sarima_tree.py
--------------------------------
Dynamic Two-Stage Hybrid Model (Model 3).

Two-Stage Estimation Architecture:
Stage 1: Linear seasonal diurnal baseline (capturing periodic diurnal schedule demand).
Stage 2: Non-parametric Tree Booster estimating residual errors (e_t = y_t - y_hat_base)
         augmented with dynamic 1-step residual error feedback:
         y_hat_t = y_hat_base_t + e_hat_tree(X_t | e_{t-1} = y_{t-1} - y_hat_{t-1})
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.ensemble import HistGradientBoostingRegressor
from typing import Optional

class SequentialSARIMATreeHybrid:
    """
    Model 3: Dynamic Two-Stage Hybrid Model with Dynamic Residual Error Feedback.
    """
    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.stage1_model = Ridge(alpha=100.0, solver="auto")
        self.stage2_model = HistGradientBoostingRegressor(
            loss="squared_error",
            max_iter=100,
            learning_rate=0.08,
            max_depth=5,
            random_state=self.random_state
        )
        self.fitted = False

    def _get_stage1_features(self, X: pd.DataFrame) -> np.ndarray:
        cols = [
            "sched_hourly_cv", "sched_hourly_std", "sched_rolling_7d_cv",
            "convolved_lead2", "convolved_lead1", "sin_diurnal", "cos_diurnal", "sin_weekly", "cos_weekly"
        ]
        avail = [c for c in cols if c in X.columns]
        if not avail:
            numeric_cols = X.select_dtypes(include=[np.number]).columns.tolist()[:4]
            return X[numeric_cols].fillna(0.0).values if numeric_cols else np.ones((len(X), 1))
        return X[avail].fillna(0.0).values

    def _get_stage2_features(self, X: pd.DataFrame, lag_residuals: np.ndarray) -> np.ndarray:
        cols = [
            "sched_hourly_std", "sched_hourly_cv", "sched_rolling_7d_std", "sched_rolling_7d_cv",
            "daily_cancel_rate", "daily_cancellations", "avg_dep_delay_minutes", "otp_departure_delay_volatility_cv",
            "avg_taxi_out_minutes", "aircraft_gauge_seats", "connecting_passenger_share_pct",
            "convolved_lead1", "convolved_lead2", "convolved_lead3",
            "minute_of_day", "sin_diurnal", "cos_diurnal",
            "is_regional", "is_narrowbody", "is_widebody",
            "originating_multiplier", "taxi_out_duration", "taxi_congestion_interaction"
        ]
        avail = [c for c in cols if c in X.columns]
        base_mat = X[avail].fillna(0.0).values if avail else np.zeros((len(X), 1))
        # Stack 1-step lagged residual feedback column
        lag_res_col = lag_residuals.reshape(-1, 1)
        return np.hstack([base_mat, lag_res_col])

    def fit(self, X: pd.DataFrame, y: pd.Series):
        y_vec = np.array(y, dtype=np.float64)
        
        # 1. Fit Stage 1: Linear seasonal schedule baseline
        X1 = self._get_stage1_features(X)
        self.stage1_model.fit(X1, y_vec)
        y_hat_stage1 = self.stage1_model.predict(X1)
        
        # 2. Compute residual error: e_t = y_t - y_hat_1
        residuals = y_vec - y_hat_stage1
        
        # 3. Create 1-step lagged residual: e_{t-1}
        lag_residuals = np.roll(residuals, 1)
        lag_residuals[0] = 0.0  # Zero initialization
        
        # 4. Fit Stage 2: Tree Booster on residuals with error feedback
        X2 = self._get_stage2_features(X, lag_residuals)
        self.stage2_model.fit(X2, residuals)
        
        # Calculate residual distribution for conformal/probabilistic intervals (REC-12)
        stage2_pred = self.stage2_model.predict(X2)
        self.final_residuals_ = residuals - stage2_pred
        self.residual_std_ = float(np.std(self.final_residuals_)) if len(self.final_residuals_) > 0 else 50.0
        
        self.fitted = True
        return self

    def predict(self, X: pd.DataFrame, y_true_for_feedback: Optional[pd.Series] = None) -> np.ndarray:
        if not self.fitted:
            return X.get("convolved_lead2", np.full(len(X), 800.0)).values
            
        # 1. Stage 1 baseline prediction
        X1 = self._get_stage1_features(X)
        y_hat_stage1 = self.stage1_model.predict(X1)
        
        # 2. Dynamic residual feedback
        if y_true_for_feedback is not None:
            # Exploit observed error from prior step
            y_arr = np.array(y_true_for_feedback, dtype=np.float64)
            res = y_arr - y_hat_stage1
            lag_residuals = np.roll(res, 1)
            lag_residuals[0] = 0.0
        else:
            # Self-propagated residual feedback
            lag_residuals = np.zeros(len(X))
            
        X2 = self._get_stage2_features(X, lag_residuals)
        residual_preds = self.stage2_model.predict(X2)
        
        final_preds = y_hat_stage1 + residual_preds
        return np.maximum(0.0, final_preds)

    def predict_quantiles(
        self,
        X: pd.DataFrame,
        y_true_for_feedback: Optional[pd.Series] = None,
        quantiles: tuple = (0.10, 0.50, 0.85, 0.90)
    ) -> dict:
        """
        Calculate quantile bounds for TSA staffing allocations and off-peak risk management (REC-12).
        Returns a dictionary mapping quantile level -> predicted array.
        """
        y_point = self.predict(X, y_true_for_feedback=y_true_for_feedback)
        out = {}
        for q in quantiles:
            if hasattr(self, "final_residuals_") and len(self.final_residuals_) > 0:
                q_offset = np.percentile(self.final_residuals_, q * 100)
            else:
                # Standard approximation for 85th percentile: +1.036 sigma
                q_offset = (1.036 if abs(q - 0.85) < 0.01 else 0.0) * getattr(self, "residual_std_", 50.0)
            out[q] = np.maximum(0.0, y_point + q_offset)
        return out

if __name__ == "__main__":
    n = 200
    df = pd.DataFrame({
        "convolved_lead2": np.random.uniform(500, 1500, size=n),
        "convolved_lead1": np.random.uniform(300, 1000, size=n),
        "sin_diurnal": np.sin(np.linspace(0, 2*np.pi, n)),
        "cos_diurnal": np.cos(np.linspace(0, 2*np.pi, n)),
        "taxi_out_duration": np.random.uniform(15, 25, size=n),
        "taxi_congestion_interaction": np.random.uniform(0, 20, size=n),
        "TSA_Throughput": np.random.uniform(400, 1600, size=n)
    })
    
    model3 = SequentialSARIMATreeHybrid()
    model3.fit(df, df["TSA_Throughput"])
    preds = model3.predict(df, y_true_for_feedback=df["TSA_Throughput"])
    corr = np.corrcoef(preds, df["TSA_Throughput"])[0, 1]
    print(f"Model 3 Dynamic Hybrid fitted successfully. Prediction-Target correlation: r = {corr:.4f}")
