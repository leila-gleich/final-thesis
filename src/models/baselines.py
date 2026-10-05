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
    M0: Diurnal Seasonal Naive Persistence Baseline for Throughput Volatility.
    Predicts checkpoint throughput volatility at time t using observed volatility at t - lag.
    Supports within-day hourly volatility (tsa_hourly_cv, tsa_hourly_std) and multi-day rolling volatility.
    """
    def __init__(self, lag_hours: int = 24):
        self.lag_hours = lag_hours

    def fit(self, X: pd.DataFrame, y: pd.Series = None):
        """Naive baseline requires no parameter estimation."""
        return self

    def predict(self, df: pd.DataFrame, target_col: str = "tsa_hourly_cv") -> np.ndarray:
        """
        Generates lagged persistence volatility forecast.
        Checks for target_col, falling back to tsa_hourly_std, tsa_hourly_cv, or TSA_Throughput.
        """
        if target_col in df.columns:
            preds = df[target_col].shift(self.lag_hours).bfill().fillna(df[target_col].mean()).values
        elif "tsa_hourly_cv" in df.columns:
            preds = df["tsa_hourly_cv"].shift(self.lag_hours).bfill().fillna(df["tsa_hourly_cv"].mean()).values
        elif "tsa_hourly_std" in df.columns:
            preds = df["tsa_hourly_std"].shift(self.lag_hours).bfill().fillna(df["tsa_hourly_std"].mean()).values
        elif "TSA_Throughput" in df.columns:
            preds = df["TSA_Throughput"].shift(self.lag_hours).bfill().fillna(df["TSA_Throughput"].mean()).values
        else:
            preds = np.full(len(df), 0.50)
        return np.maximum(0.0, preds)

class DeterministicFixedLeadBaseline:
    """
    M1: Rebuilt Deterministic Schedule Volatility Baseline.
    
    Reflects deterministic airport planning practice:
    Derives predicted passenger screening volatility directly from scheduled flight departure bank dispersion
    (standard deviation or CV of scheduled flight movements across hours).
    
    Equation:
        Vol_hat_t = beta_0 + beta_1 * Vol_sched_t
    """
    def __init__(self, beta_0: float = 0.15, beta_1: float = 0.85):
        self.beta_0 = beta_0
        self.beta_1 = beta_1

    def fit(self, X: pd.DataFrame, y: pd.Series):
        """Fits OLS linear scaling factor between schedule dispersion and throughput volatility."""
        sched_vol = self._extract_sched_volatility(X)
        if len(y) > 10 and np.var(sched_vol) > 1e-6:
            cov = np.cov(sched_vol, y)[0, 1]
            var = np.var(sched_vol)
            self.beta_1 = float(cov / var) if var > 0 else 0.85
            self.beta_0 = float(np.mean(y) - self.beta_1 * np.mean(sched_vol))
        return self

    def _extract_sched_volatility(self, X: pd.DataFrame) -> np.ndarray:
        if "sched_hourly_cv" in X.columns:
            return X["sched_hourly_cv"].fillna(X["sched_hourly_cv"].mean()).values
        elif "sched_hourly_std" in X.columns:
            return X["sched_hourly_std"].fillna(X["sched_hourly_std"].mean()).values
        elif "convolved_lead2" in X.columns:
            return X["convolved_lead2"].values
        elif "net_originating_demand" in X.columns:
            return X["net_originating_demand"].values
        elif "Scheduled_Departures" in X.columns:
            return X["Scheduled_Departures"].values * 140.0
        else:
            return np.full(len(X), 0.50)

    def predict(self, X: pd.DataFrame) -> np.ndarray:
        sched_vol = self._extract_sched_volatility(X)
        preds = self.beta_0 + self.beta_1 * sched_vol
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
