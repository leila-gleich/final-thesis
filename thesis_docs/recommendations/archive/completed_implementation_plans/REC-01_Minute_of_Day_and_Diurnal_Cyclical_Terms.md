# STATUS: IMPLEMENTED

# Recommendation REC-01: High-Precision Minute-of-Day & Diurnal Cyclical Features

**Recommendation ID**: REC-01  
**Target Module**: `src/features/time_features.py`  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Standard hourly aggregations treat a flight departing at 07:05 and a flight departing at 07:55 identically (both assigned to Hour 7). However, physical passenger show-up distributions dictate that an 07:05 flight's passengers arrive at security checkpoints primarily during Hour 5 and Hour 6, whereas an 07:55 flight's passengers arrive during Hour 6 and Hour 7.

Lumping departures into coarse hourly buckets creates temporal phase error and artificial step discontinuities at midnight ($23:59 \to 00:00$). To capture smooth diurnal and weekly dynamics, high-precision minute-of-day encoding and continuous trigonometric cyclical terms must be engineered.

---

## 2. Technical Specification

### 2.1 Minute-of-Day Encoding
Calculate exact integer minute-of-day:
$$m = \text{hour} \times 60 + \text{minute} \quad \text{where } m \in [0, 1439]$$

### 2.2 Diurnal Trigonometric Transforms
To eliminate artificial boundary discontinuities between 23:59 and 00:00:
$$\sin_{\text{diurnal}} = \sin\left(\frac{2\pi \cdot m}{1440}\right), \quad \cos_{\text{diurnal}} = \cos\left(\frac{2\pi \cdot m}{1440}\right)$$

### 2.3 Weekly Trigonometric Transforms
Calculate weekly minute timestamp $w \in [0, 10079]$:
$$w = \text{dayofweek} \times 1440 + m$$
$$\sin_{\text{weekly}} = \sin\left(\frac{2\pi \cdot w}{10080}\right), \quad \cos_{\text{weekly}} = \cos\left(\frac{2\pi \cdot w}{10080}\right)$$

---

## 3. Implementation Code

```python
"""
src/etl/ingest_curated_data.py
Autonomous feature generation for high-precision minute-of-day and cyclical time.
"""

import numpy as np
import pandas as pd

def generate_temporal_features(df: pd.DataFrame, time_col: str = "Scheduled_Departure_Time") -> pd.DataFrame:
    """
    Computes integer minute-of-day and smooth cyclical diurnal/weekly trigonometric features.
    """
    res = df.copy()
    dt_series = pd.to_datetime(res[time_col])
    
    # Integer minute of day [0, 1439]
    minute_of_day = dt_series.dt.hour * 60 + dt_series.dt.minute
    res["minute_of_day"] = minute_of_day.astype(np.int16)
    
    # Diurnal Cyclical (Period = 1440 minutes)
    rad_diurnal = 2.0 * np.pi * minute_of_day / 1440.0
    res["sin_diurnal"] = np.sin(rad_diurnal).astype(np.float32)
    res["cos_diurnal"] = np.cos(rad_diurnal).astype(np.float32)
    
    # Weekly Cyclical (Period = 10080 minutes)
    minute_of_week = dt_series.dt.dayofweek * 1440 + minute_of_day
    rad_weekly = 2.0 * np.pi * minute_of_week / 10080.0
    res["sin_weekly"] = np.sin(rad_weekly).astype(np.float32)
    res["cos_weekly"] = np.cos(rad_weekly).astype(np.float32)
    
    return res
```

---

## 4. Verification & Acceptance Criteria

- [ ] `minute_of_day` values strictly lie in range $[0, 1439]$.
- [ ] $\sin^2(\text{diurnal}) + \cos^2(\text{diurnal}) = 1.0$ for all records.
- [ ] $\sin^2(\text{weekly}) + \cos^2(\text{weekly}) = 1.0$ for all records.
- [ ] Smooth transition across midnight boundary verified without NaNs or discontinuities.
