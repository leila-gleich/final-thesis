"""
src/data/panel_loader.py
------------------------
Authoritative Ingestion & Feature Consolidation Engine for TSA Checkpoint
Throughput Volatility and BTS On-Time Performance (OTP) Panel Construction.

Constructs conformed daily airport panel data:
1. Ingests curated hourly screening counts (data/curated/hourly_aggregated_data.csv).
2. Computes within-day diurnal volatility metrics (std, CV, p95, median, IQR).
3. Derives scheduled vs actual departure metrics and daily cancellation rates.
4. Generates multi-day rolling volatility statistics (7-day rolling std, mean, and CV).
5. Merges Top 25 airport census operational attributes from 01_top25_clustering.xlsx.
"""

import os
from pathlib import Path
import numpy as np
import pandas as pd

try:
    from src.utils.paths import (
        BASE_DIR,
        HOURLY_CURATED_PATH,
        DAILY_CURATED_PATH,
        TOP25_CLUSTERING_WB
    )
except ImportError:
    from utils.paths import (
        BASE_DIR,
        HOURLY_CURATED_PATH,
        DAILY_CURATED_PATH,
        TOP25_CLUSTERING_WB
    )


def load_and_prepare_panel_data(
    hourly_path=None,
    excel_top25_path=None
):
    """
    Ingests curated hourly and daily data to construct the conformed 
    airport-day volatility panel for candidate model estimation.
    
    Returns:
        tuple: (df_panel, df_census)
            - df_panel: DataFrame with within-day volatility, rolling metrics, and OTP features.
            - df_census: Master Top 25 airport operational census.
    """
    print("\n[Data Loader] Loading Curated Hourly and Daily Aggregates...")
    h_path = Path(hourly_path) if hourly_path else HOURLY_CURATED_PATH
    wb_path = Path(excel_top25_path) if excel_top25_path else TOP25_CLUSTERING_WB
    
    # 1. Load Hourly Data
    df_h = pd.read_csv(h_path)
    df_h['Date'] = pd.to_datetime(df_h['Date'])
    df_h = df_h.sort_values(by=['Airport', 'Date', 'Hour'])
    
    # 2. Compute Daily Within-Day Volatility and Metrics
    daily_within = df_h.groupby(['Date', 'Airport']).agg(
        tsa_daily_total=('TSA_Throughput', 'sum'),
        tsa_hourly_mean=('TSA_Throughput', 'mean'),
        tsa_hourly_std=('TSA_Throughput', 'std'),
        tsa_hourly_p95=('TSA_Throughput', lambda x: np.percentile(x, 95)),
        tsa_hourly_p50=('TSA_Throughput', 'median'),
        tsa_hourly_iqr=('TSA_Throughput', lambda x: np.percentile(x, 75) - np.percentile(x, 25)),
        sched_daily_total=('Scheduled_Departures', 'sum'),
        sched_hourly_mean=('Scheduled_Departures', 'mean'),
        sched_hourly_std=('Scheduled_Departures', 'std'),
        actual_daily_total=('Actual_Departures', 'sum'),
        actual_hourly_mean=('Actual_Departures', 'mean'),
        actual_hourly_std=('Actual_Departures', 'std')
    ).reset_index()
    
    # Target calculations
    daily_within['tsa_hourly_cv'] = daily_within['tsa_hourly_std'] / daily_within['tsa_hourly_mean'].replace(0, np.nan)
    daily_within['tsa_surge_ratio'] = daily_within['tsa_hourly_p95'] / daily_within['tsa_hourly_p50'].replace(0, np.nan)
    
    # OTP Features
    daily_within['daily_cancellations'] = daily_within['sched_daily_total'] - daily_within['actual_daily_total']
    daily_within['daily_cancel_rate'] = (daily_within['daily_cancellations'] / daily_within['sched_daily_total'].replace(0, np.nan)).clip(lower=0.0)
    daily_within['sched_hourly_cv'] = daily_within['sched_hourly_std'] / daily_within['sched_hourly_mean'].replace(0, np.nan)
    daily_within['actual_hourly_cv'] = daily_within['actual_hourly_std'] / daily_within['actual_hourly_mean'].replace(0, np.nan)
    
    # 3. Multi-day Rolling Metrics
    daily_within = daily_within.sort_values(by=['Airport', 'Date'])
    
    rolling_dfs = []
    for apt, grp in daily_within.groupby('Airport'):
        grp = grp.set_index('Date').sort_index()
        # Rolling 7-day TSA volatility
        grp['tsa_rolling_7d_std'] = grp['tsa_daily_total'].rolling('7D', min_periods=4).std()
        grp['tsa_rolling_7d_mean'] = grp['tsa_daily_total'].rolling('7D', min_periods=4).mean()
        grp['tsa_rolling_7d_cv'] = grp['tsa_rolling_7d_std'] / grp['tsa_rolling_7d_mean'].replace(0, np.nan)
        
        # Rolling 7-day OTP Feature Values
        grp['sched_rolling_7d_mean'] = grp['sched_daily_total'].rolling('7D', min_periods=4).mean()
        grp['actual_rolling_7d_mean'] = grp['actual_daily_total'].rolling('7D', min_periods=4).mean()
        grp['cancel_rolling_7d_mean'] = grp['daily_cancellations'].rolling('7D', min_periods=4).mean()
        grp['cancel_rate_rolling_7d_mean'] = grp['daily_cancel_rate'].rolling('7D', min_periods=4).mean()
        
        # Rolling 7-day OTP Feature Volatilities
        grp['sched_rolling_7d_std'] = grp['sched_daily_total'].rolling('7D', min_periods=4).std()
        grp['sched_rolling_7d_cv'] = grp['sched_rolling_7d_std'] / grp['sched_rolling_7d_mean'].replace(0, np.nan)
        grp['actual_rolling_7d_std'] = grp['actual_daily_total'].rolling('7D', min_periods=4).std()
        grp['actual_rolling_7d_cv'] = grp['actual_rolling_7d_std'] / grp['actual_rolling_7d_mean'].replace(0, np.nan)
        grp['cancel_rolling_7d_std'] = grp['daily_cancellations'].rolling('7D', min_periods=4).std()
        grp['cancel_rate_rolling_7d_std'] = grp['daily_cancel_rate'].rolling('7D', min_periods=4).std()
        
        rolling_dfs.append(grp.reset_index())
        
    df_panel = pd.concat(rolling_dfs, ignore_index=True)
    
    # 4. Merge Top 25 Airport Census Profile for baseline delay & network features
    df_top25 = pd.read_excel(wb_path, sheet_name='01_Executive_Top25_Airport_Coup')
    top25_cols = [
        'airport_code', 'avg_dep_delay_minutes', 'flights_delayed_15min_pct', 
        'avg_taxi_out_minutes', 'otp_departure_delay_volatility_cv', 
        'otp_cancellation_volatility_cv', 'connecting_passenger_share_pct',
        'aircraft_gauge_seats', 'route_load_factor_pct'
    ]
    df_census = df_top25[top25_cols].rename(columns={'airport_code': 'Airport'})
    
    df_merged = pd.merge(df_panel, df_census, on='Airport', how='left')
    df_merged['Year'] = df_merged['Date'].dt.year
    df_merged['Month'] = df_merged['Date'].dt.month
    df_merged['DayOfWeek'] = df_merged['Date'].dt.dayofweek
    
    print(f"Panel constructed: {df_merged.shape[0]} airport-days across {df_merged['Airport'].nunique()} airfields.")
    return df_merged, df_top25
