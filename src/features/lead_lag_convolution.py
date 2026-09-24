"""
lead_lag_convolution.py
-----------------------
Implements continuous passenger arrival kernel deconvolution for TSA checkpoint demand.
Deconvolves rigid scheduled flight departure seats into pre-departure arrival time
buckets using an empirical lognormal arrival distribution:
    tau ~ Lognormal(mu=4.65, sigma=0.35) peaking at 90-120 min pre-departure.
"""

import numpy as np
import pandas as pd
from scipy.stats import lognorm


def compute_arrival_weights(peak_lead_minutes=105, scale=0.35):
    """
    Computes discrete hourly integration weights from a continuous lognormal arrival kernel.
    Returns normalized weights for lead horizons [t+1, t+2, t+3].
    
    t+1: 1 hour pre-departure  [30, 90) min  (~28.4%)
    t+2: 2 hours pre-departure [90, 150) min (~52.6% peak window)
    t+3: 3 hours pre-departure [150, 210) min (~19.0%)
    """
    s = scale
    scale_param = peak_lead_minutes / np.exp(-s**2)
    dist = lognorm(s=s, scale=scale_param)
    
    w1 = dist.cdf(90) - dist.cdf(30)
    w2 = dist.cdf(150) - dist.cdf(90)
    w3 = dist.cdf(210) - dist.cdf(150)
    
    weights = np.array([w1, w2, w3])
    return weights / weights.sum()


def convolve_scheduled_demand(flights_df, seats_col="seats", load_factor_col="load_factor", connecting_ratio_col="connecting_ratio"):
    """
    Applies empirical arrival kernel convolution to scheduled flights.
    Accounts for airside connecting ratios and carrier load factors:
        Demand_t = SUM [ Seats_k * LF_k * (1 - CR_k) * w_h ]
    """
    weights = compute_arrival_weights()
    df = flights_df.copy()
    
    # Net landside originating passenger demand
    lf = df[load_factor_col] if load_factor_col in df.columns else 0.85
    cr = df[connecting_ratio_col] if connecting_ratio_col in df.columns else 0.50
    net_originating_pax = df[seats_col] * lf * (1.0 - cr)
    
    df["convolved_demand_lead1"] = net_originating_pax * weights[0]
    df["convolved_demand_lead2"] = net_originating_pax * weights[1]
    df["convolved_demand_lead3"] = net_originating_pax * weights[2]
    df["convolved_total_demand"] = net_originating_pax
    
    return df
