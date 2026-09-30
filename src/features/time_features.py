"""
src/features/time_features.py
-----------------------------
High-Precision Minute-of-Day & Diurnal Cyclical Features (REC-01).

Computes:
1. Exact integer minute-of-day: m in [0, 1439].
2. Continuous diurnal cyclical trigonometric terms (Period = 1440 min):
   sin_diurnal, cos_diurnal.
3. Continuous weekly cyclical trigonometric terms (Period = 10080 min):
   sin_weekly, cos_weekly.
"""

import numpy as np
import pandas as pd

def generate_temporal_features(df: pd.DataFrame, time_col: str = "Scheduled_Departure_Time") -> pd.DataFrame:
    """
    Generates minute-of-day and cyclical trigonometric temporal features from a timestamp column.
    Handles datetime objects, timestamp strings, or numeric hour columns.
    """
    res = df.copy()
    
    if time_col in res.columns:
        dt_series = pd.to_datetime(res[time_col], errors="coerce")
        minute_of_day = dt_series.dt.hour * 60 + dt_series.dt.minute
        day_of_week = dt_series.dt.dayofweek
    elif "Hour" in res.columns:
        # Fallback to hourly column
        minute_of_day = res["Hour"].astype(int) * 60
        if "Date" in res.columns:
            day_of_week = pd.to_datetime(res["Date"]).dt.dayofweek
        else:
            day_of_week = pd.Series(0, index=res.index)
    else:
        raise ValueError(f"Neither '{time_col}' nor 'Hour' column found in DataFrame.")

    res["minute_of_day"] = minute_of_day.astype(np.int16)
    
    # Diurnal Cyclical (Period = 1440 minutes)
    rad_diurnal = 2.0 * np.pi * minute_of_day / 1440.0
    res["sin_diurnal"] = np.sin(rad_diurnal).astype(np.float32)
    res["cos_diurnal"] = np.cos(rad_diurnal).astype(np.float32)
    
    # Weekly Cyclical (Period = 10080 minutes)
    minute_of_week = day_of_week * 1440 + minute_of_day
    rad_weekly = 2.0 * np.pi * minute_of_week / 10080.0
    res["sin_weekly"] = np.sin(rad_weekly).astype(np.float32)
    res["cos_weekly"] = np.cos(rad_weekly).astype(np.float32)
    
    return res

if __name__ == "__main__":
    df = pd.DataFrame({
        "Scheduled_Departure_Time": ["2023-05-01 00:00:00", "2023-05-01 06:30:00", "2023-05-01 12:00:00", "2023-05-01 23:59:00"]
    })
    out = generate_temporal_features(df)
    print(out[["minute_of_day", "sin_diurnal", "cos_diurnal", "sin_weekly", "cos_weekly"]])
