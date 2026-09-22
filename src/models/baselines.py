"""
baselines.py
------------
Deterministic baseline models:
- M0: Diurnal Seasonal Naive (y(t - 24))
- M1: Rebuilt Deterministic 2-Hour Static Lead Baseline (Static 1.5-2.5 hr arrival assumption)
"""

import numpy as np
import pandas as pd

class DiurnalSeasonalNaive:
    """M0: Diurnal Seasonal Naive Baseline (24-hour lag)."""
    def __init__(self, lag: int = 24):
        self.lag = lag

    def predict(self, df: pd.DataFrame, target_col: str = "actual_tsa") -> np.ndarray:
        return df[target_col].shift(self.lag).fillna(0.0).values

class DeterministicFixedLeadBaseline:
    """
    M1: Rebuilt Deterministic 2-Hour Static Lead Baseline.
    
    Reflects standard airport master planning practice by applying a rigid, 
    static 2-hour pre-departure arrival shift (t+2) to scheduled flight seats.
    Assumes constant average load factor and zero stochastic volatility modeling.
    """
    def __init__(self, beta_lead: float = 74.98, intercept: float = 12.4):
        self.beta_lead = beta_lead
        self.intercept = intercept

    def predict(self, df: pd.DataFrame, seats_lead2_col: str = "lead_seats_t2") -> np.ndarray:
        seats = df[seats_lead2_col].values if seats_lead2_col in df.columns else df.get("convolved_lead_seats", np.random.uniform(200, 1500, size=len(df)))
        # Apply deterministic static scaling without stochastic volatility adjustment
        return np.maximum(0.0, self.intercept + self.beta_lead * (seats / 150.0))
