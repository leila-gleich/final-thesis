"""
src/models/baselines.py
-----------------------
Deterministic Baseline Models:
- M0: Diurnal Seasonal Naive (y(t - 24))
- M1: Rebuilt Deterministic 2-Hour Static Lead Baseline (Static 1.5 - 2.5 hr arrival assumption)
"""

import numpy as np
import pandas as pd
from typing import Optional

class DiurnalSeasonalNaive:
    """
    M0: Diurnal Seasonal Naive Persistence Baseline (24-hour seasonal lag).
    Predicts checkpoint throughput at time t using the observed volume at t - 24 hours.
    """
    def __init__(self, lag_hours: int = 24):
        self.lag_hours = lag_hours

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        """Naive baseline requires no parameter estimation."""
        return self

    def predict(self, df: pd.DataFrame, target_col: str = "TSA_Throughput") -> np.ndarray:
        """
        Generates 24-hour lagged persistence forecast.
        If target column is not present or has NaNs, imputes with airport-hour mean.
        """
        if target_col in df.columns:
            preds = df[target_col].shift(self.lag_hours).bfill().fillna(df[target_col].mean()).values
        else:
            preds = np.full(len(df), 850.0)
        return np.maximum(0.0, preds)

class DeterministicFixedLeadBaseline:
    """
    M1: Rebuilt Deterministic 2-Hour Static Lead Baseline.
    
    Reflects standard airport master planning practice (e.g. FAA / ACRP Report 40 baseline):
    Applies a rigid, static 2-hour pre-departure arrival lead shift (t+2) to scheduled flight capacity.
    Assumes constant average load factor (84.7%) and connecting deflation without dynamic volatility.
    
    Equation:
        y_hat_t = beta_0 + beta_1 * (Seats_{t+2} * LF * (1 - CR))
    """
    def __init__(self, beta_0: float = 12.4, beta_1: float = 0.847):
        self.beta_0 = beta_0
        self.beta_1 = beta_1

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """Fits OLS linear scaling factor between 2-hour lead capacity and throughput."""
        lead_demand = self._extract_lead_demand(X)
        if len(y) > 10 and np.var(lead_demand) > 1e-4:
            # Simple 1D linear regression
            cov = np.cov(lead_demand, y)[0, 1]
            var = np.var(lead_demand)
            self.beta_1 = float(cov / var) if var > 0 else 0.847
            self.beta_0 = float(np.mean(y) - self.beta_1 * np.mean(lead_demand))
        return self

    def _extract_lead_demand(self, X: pd.DataFrame) -> np.ndarray:
        if "convolved_lead2" in X.columns:
            return X["convolved_lead2"].values
        elif "net_originating_demand" in X.columns:
            return X["net_originating_demand"].values
        elif "Scheduled_Departures" in X.columns:
            return X["Scheduled_Departures"].values * 140.0
        else:
            return np.full(len(X), 800.0)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        lead_demand = self._extract_lead_demand(X)
        preds = self.beta_0 + self.beta_1 * lead_demand
        return np.maximum(0.0, preds)

if __name__ == "__main__":
    df = pd.DataFrame({
        "TSA_Throughput": [500, 600, 800, 1200, 1500] * 10,
        "convolved_lead2": [450, 580, 750, 1100, 1400] * 10
    })
    m0 = DiurnalSeasonalNaive()
    m1 = DeterministicFixedLeadBaseline()
    m1.fit(df, df["TSA_Throughput"])
    
    p0 = m0.predict(df)
    p1 = m1.predict(df)
    print("M0 Naive predictions:", p0[:5])
    print(f"M1 Baseline fitted: beta_0={m1.beta_0:.2f}, beta_1={m1.beta_1:.4f}")
    print("M1 Baseline predictions:", p1[:5])
