#!/usr/bin/env python3
"""
season_analysis_volatility_runner.py
------------------------------------
Empirical temporal regime clustering pipeline analyzing the coupled relationship
between the VOLATILITY / VARIATION of TSA Checkpoint Passenger Throughput
and BTS On-Time Performance (OTP) flight operations for the Top 25 US commercial airfields.

Hierarchical Temporal Dimensions:
1. Annual Macro Regimes (4 Seasons): Off-Peak, Mid-Peak, Peak, Holiday
   - Clustered on coupled volatility metrics: within-day TSA arrival CV, peak-to-mean surge shock,
     flight departure delay standard deviation (dispersion), coupled volatility index (CV_TSA * std_delay),
     and DepDel15 volatility.
2. Weekly Cycles & Archetypes (7 Days of the Week: Monday to Sunday, ISO 8601)
   - Evaluated across weekly volatility propagation profiles.
3. Diurnal Regimes (3 Non-Consecutive Hourly Categories conditioned on Day of Week)
   - Clustered on the Operational Turbulence Shock Index combining TSA screening arrival surge
     variance shocks and flight departure delay dispersion shocks, naturally producing dual peaks
     (morning passenger arrival wave + evening flight delay cascade) separated by midday stable flow.

Outputs are generated for:
- season-analysis/ (root deliverable folder)
- results/foundational_analysis/season_analysis/
"""

import os
import sys
import shutil
import numpy as np
import pandas as pd
import duckdb
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# Paths configuration
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(SCRIPT_DIR)

OUTPUT_DIRS = [
    SCRIPT_DIR
]
FIGURES_DIR = os.path.join(PROJECT_ROOT, "thesis_docs", "manuscripts", "figures")

DATA_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Archive/700b-data-warehouse/data/processed"
DIM_DATE_PATH = os.path.join(PROJECT_ROOT, "archive", "superseded_code_snapshot", "dimensions", "dim_date.csv")
DIM_AIRPORT_PATH = os.path.join(PROJECT_ROOT, "archive", "superseded_code_snapshot", "dimensions", "dim_airport.csv")

TSA_PARQUET = os.path.join(DATA_DIR, "tsav1.parquet")
OTP_PARQUET = os.path.join(DATA_DIR, "otpv1.parquet")

TOP25_AIRPORT_IDS = [
    24,  # ATL
    27,  # AUS
    50,  # BOS
    79,  # CLT
    98,  # DCA
    101, # DEN
    102, # DFW
    110, # DTW
    125, # EWR
    176, # IAD
    178, # IAH
    195, # JFK
    205, # LAS
    207, # LAX
    216, # LGA
    229, # MCO
    241, # MIA
    254, # MSP
    268, # ORD
    282, # PHL
    283, # PHX
    331, # SEA
    333, # SFO
    343, # SLC
    365  # TPA
]

TOP25_ID_STR = ",".join(map(str, TOP25_AIRPORT_IDS))

def ensure_directories():
    for d in OUTPUT_DIRS:
        os.makedirs(d, exist_ok=True)
    os.makedirs(FIGURES_DIR, exist_ok=True)

def run_volatility_analysis():
    print("=" * 80)
    print("TSA THROUGHPUT & BTS OTP VOLATILITY / VARIATION CLUSTERING PIPELINE")
    print("Top 25 US Commercial Airfields | Candidate B Study Window (2022-2025)")
    print("=" * 80)
    
    ensure_directories()
    con = duckdb.connect()
    
    # -------------------------------------------------------------------------
    # STEP 1: CALENDAR & HOLIDAY CORRIDORS DEFINITION
    # -------------------------------------------------------------------------
    print("\n[STEP 1] Loading calendar dimension and defining aviation holiday corridors...")
    date_df = con.execute(f"""
        SELECT 
            dateId,
            date,
            year,
            quarter,
            month,
            dayOfMonth,
            dayOfWeek,
            isWeekend,
            isHoliday,
            holidayName
        FROM read_csv_auto('{DIM_DATE_PATH}')
        ORDER BY dateId
    """).df()
    
    date_df['date_dt'] = pd.to_datetime(date_df['date'])
    date_df['holiday_corridor'] = 0
    date_df['holiday_corridor_name'] = 'Non-Holiday'
    
    # Standard expanded aviation holiday corridors
    for idx, row in date_df.iterrows():
        dt = row['date_dt']
        m, d = dt.month, dt.day
        if (m == 12 and d >= 20) or (m == 1 and d <= 3):
            date_df.at[idx, 'holiday_corridor'] = 1
            date_df.at[idx, 'holiday_corridor_name'] = 'Winter Holidays Wave'
        elif m == 7 and 1 <= d <= 7:
            date_df.at[idx, 'holiday_corridor'] = 1
            date_df.at[idx, 'holiday_corridor_name'] = 'Independence Day Wave'
            
    holiday_windows = {
        'Thanksgiving Day': (-3, 3, 'Thanksgiving Travel Wave'),
        'Memorial Day': (-4, 1, 'Memorial Day Weekend'),
        'Labor Day': (-4, 1, 'Labor Day Weekend'),
        'MLK Jr. Day': (-3, 1, 'MLK Holiday Weekend'),
        "Presidents' Day": (-3, 1, 'Presidents Holiday Weekend')
    }
    
    for hol_name, (days_before, days_after, corr_label) in holiday_windows.items():
        hol_dates = date_df[date_df['holidayName'] == hol_name]['date_dt'].tolist()
        for hd in hol_dates:
            window = pd.date_range(hd + pd.Timedelta(days=days_before), hd + pd.Timedelta(days=days_after))
            mask = date_df['date_dt'].isin(window)
            date_df.loc[mask, 'holiday_corridor'] = 1
            date_df.loc[mask, 'holiday_corridor_name'] = corr_label
            
    print(f"Total calendar days: {len(date_df)}")
    print(f"Holiday corridor days: {date_df['holiday_corridor'].sum()} ({date_df['holiday_corridor'].mean():.1%})")
    con.register("dim_date_enhanced", date_df)
    
    # -------------------------------------------------------------------------
    # STEP 2: DAILY COUPLED VOLATILITY AGGREGATION & ANNUAL REGIME CLUSTERING
    # -------------------------------------------------------------------------
    print("\n[STEP 2] Aggregating daily coupled TSA and OTP volatility metrics...")
    daily_query = f"""
        WITH tsa_hourly AS (
            SELECT 
                dateId,
                hour,
                SUM(throughput) as hr_tsa
            FROM read_parquet('{TSA_PARQUET}')
            WHERE airportId IN ({TOP25_ID_STR})
            GROUP BY 1, 2
        ),
        tsa_daily_stats AS (
            SELECT 
                dateId,
                SUM(hr_tsa) as daily_tsa,
                AVG(hr_tsa) as mean_hourly_tsa,
                STDDEV(hr_tsa) as std_hourly_tsa,
                MAX(hr_tsa) as max_hourly_tsa,
                STDDEV(hr_tsa) / NULLIF(AVG(hr_tsa), 0) as cv_hourly_tsa,
                MAX(hr_tsa) / NULLIF(AVG(hr_tsa), 0) as peak_to_mean_tsa
            FROM tsa_hourly
            GROUP BY 1
        ),
        otp_daily_stats AS (
            SELECT 
                dateId,
                COUNT(*) as daily_flights,
                AVG(CASE WHEN cancelled = false THEN depDel ELSE NULL END) as avg_dep_delay,
                STDDEV(CASE WHEN cancelled = false THEN depDel ELSE NULL END) as std_dep_delay,
                SUM(CASE WHEN cancelled = false AND depDel15 = true THEN 1 ELSE 0 END) * 100.0 / 
                    NULLIF(COUNT(CASE WHEN cancelled = false THEN 1 END), 0) as depdel15_pct,
                SUM(CASE WHEN cancelled = true THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as cancel_pct,
                AVG(CASE WHEN cancelled = false THEN taxiOut ELSE NULL END) as avg_taxi_out
            FROM read_parquet('{OTP_PARQUET}')
            WHERE originAirportId IN ({TOP25_ID_STR})
            GROUP BY 1
        )
        SELECT 
            d.dateId,
            d.date,
            d.year,
            d.month,
            d.dayOfMonth,
            d.dayOfWeek,
            d.isWeekend,
            d.isHoliday,
            d.holidayName,
            d.holiday_corridor,
            d.holiday_corridor_name,
            t.daily_tsa,
            t.mean_hourly_tsa,
            t.std_hourly_tsa,
            t.cv_hourly_tsa,
            t.peak_to_mean_tsa,
            o.daily_flights,
            t.daily_tsa * 1.0 / NULLIF(o.daily_flights, 0) as pax_per_flight,
            o.avg_dep_delay,
            o.std_dep_delay,
            (t.cv_hourly_tsa * o.std_dep_delay) as coupled_volatility_index,
            o.depdel15_pct,
            o.cancel_pct,
            o.avg_taxi_out
        FROM dim_date_enhanced d
        JOIN tsa_daily_stats t ON d.dateId = t.dateId
        JOIN otp_daily_stats o ON d.dateId = o.dateId
        WHERE d.date >= '2022-05-01' AND d.date <= '2025-12-31'
        ORDER BY d.dateId
    """
    daily_df = con.execute(daily_query).df()
    print(f"Aggregated {len(daily_df)} daily coupled records for Top 25 hubs (2022-05-01 to 2025-12-31).")
    
    daily_df['date_dt'] = pd.to_datetime(daily_df['date'])
    daily_df['iso_week'] = daily_df['date_dt'].dt.isocalendar().week
    
    # Cluster annual seasonal cycles by weekly coupled volatility profiles (weeks 1-52/53)
    # This separates macro seasonal turbulence regimes while preserving balanced weekly representation
    non_hol_days = daily_df[daily_df['holiday_corridor'] == 0].copy()
    
    week_vol = non_hol_days.groupby('iso_week').agg(
        mean_coupled_vol=('coupled_volatility_index', 'mean'),
        mean_std_delay=('std_dep_delay', 'mean'),
        mean_cv_tsa=('cv_hourly_tsa', 'mean'),
        mean_dep_delay=('avg_dep_delay', 'mean'),
        mean_depdel15=('depdel15_pct', 'mean')
    ).reset_index()
    
    wk_features = ['mean_coupled_vol', 'mean_std_delay', 'mean_cv_tsa', 'mean_depdel15']
    scaler_wk = StandardScaler()
    X_wk = scaler_wk.fit_transform(week_vol[wk_features])
    
    km_wk = KMeans(n_clusters=3, random_state=42, n_init=25)
    week_vol['cluster_id'] = km_wk.fit_predict(X_wk)
    
    # Order clusters monotonically by coupled volatility
    cl_order = week_vol.groupby('cluster_id')['mean_coupled_vol'].mean().sort_values().index
    wk_mapping = {
        cl_order[0]: '1_OFF_PEAK',
        cl_order[1]: '2_MID_PEAK',
        cl_order[2]: '3_PEAK'
    }
    week_vol['season_regime'] = week_vol['cluster_id'].map(wk_mapping)
    
    # Map back to daily dataframe
    daily_df = daily_df.merge(week_vol[['iso_week', 'season_regime']], on='iso_week', how='left')
    daily_df['season_regime'] = np.where(daily_df['holiday_corridor'] == 1, '4_HOLIDAY', daily_df['season_regime'])
    
    season_labels = {
        '1_OFF_PEAK': 'Off-Peak (Winter Lull & Mid-Autumn Shoulder)',
        '2_MID_PEAK': 'Mid-Peak (Spring Ramps & Late-Summer Shoulder)',
        '3_PEAK': 'Peak (Summer Severe Weather & High Volume Surge)',
        '4_HOLIDAY': 'Holiday (National Holiday Travel Corridors)'
    }
    daily_df['season_name'] = daily_df['season_regime'].map(season_labels)
    
    # ISO 8601 Day of Week mapping (1=Monday, ..., 7=Sunday)
    dow_names = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
    daily_df['dow_name'] = daily_df['dayOfWeek'].map(dow_names)
    
    # Export Seasonal Regimes Summary Table
    season_summary = daily_df.groupby(['season_regime', 'season_name']).agg(
        days_count=('dateId', 'count'),
        mean_daily_tsa=('daily_tsa', 'mean'),
        std_daily_tsa=('daily_tsa', 'std'),
        mean_cv_hourly_tsa=('cv_hourly_tsa', 'mean'),
        mean_peak_to_mean_tsa=('peak_to_mean_tsa', 'mean'),
        mean_daily_flights=('daily_flights', 'mean'),
        mean_pax_per_flight=('pax_per_flight', 'mean'),
        mean_dep_delay=('avg_dep_delay', 'mean'),
        mean_std_dep_delay=('std_dep_delay', 'mean'),
        mean_coupled_volatility_index=('coupled_volatility_index', 'mean'),
        mean_depdel15_pct=('depdel15_pct', 'mean'),
        mean_cancel_pct=('cancel_pct', 'mean'),
        mean_taxi_out=('avg_taxi_out', 'mean')
    ).reset_index()
    season_summary['share_of_days_pct'] = (season_summary['days_count'] / len(daily_df)) * 100.0
    
    print("\n--- ANNUAL SEASONAL VOLATILITY REGIMES ---")
    print(season_summary[['season_regime', 'days_count', 'share_of_days_pct', 'mean_cv_hourly_tsa', 'mean_std_dep_delay', 'mean_coupled_volatility_index', 'mean_dep_delay']].to_string(index=False))

    # -------------------------------------------------------------------------
    # STEP 3: DAY OF WEEK OPERATIONAL VOLATILITY PROFILES
    # -------------------------------------------------------------------------
    print("\n[STEP 3] Computing Day-of-Week Volatility & Operational Cycles...")
    dow_summary = daily_df.groupby(['dayOfWeek', 'dow_name']).agg(
        days_count=('dateId', 'count'),
        mean_daily_tsa=('daily_tsa', 'mean'),
        std_daily_tsa=('daily_tsa', 'std'),
        mean_cv_hourly_tsa=('cv_hourly_tsa', 'mean'),
        mean_peak_to_mean_tsa=('peak_to_mean_tsa', 'mean'),
        mean_daily_flights=('daily_flights', 'mean'),
        mean_pax_per_flight=('pax_per_flight', 'mean'),
        mean_dep_delay=('avg_dep_delay', 'mean'),
        mean_std_dep_delay=('std_dep_delay', 'mean'),
        mean_coupled_volatility=('coupled_volatility_index', 'mean'),
        mean_depdel15_pct=('depdel15_pct', 'mean'),
        mean_cancel_pct=('cancel_pct', 'mean'),
        mean_taxi_out=('avg_taxi_out', 'mean')
    ).reset_index()
    
    weekly_archetypes = {
        'Monday': 'Outbound Business Surge & High Screening Volatility',
        'Tuesday': 'Midweek Operational Reset',
        'Wednesday': 'Midweek Baseline Stability',
        'Thursday': 'Corporate Outbound & Early Weekend Ramp',
        'Friday': 'Combined Business & Weekend Getaway Surge',
        'Saturday': 'Volume Trough & Fleet Repositioning',
        'Sunday': 'Leisure Return Peak & Evening Delay Propagation'
    }
    dow_summary['weekly_operational_archetype'] = dow_summary['dow_name'].map(weekly_archetypes)
    
    print("\n--- DAY OF WEEK VOLATILITY SUMMARY ---")
    print(dow_summary[['dayOfWeek', 'dow_name', 'weekly_operational_archetype', 'mean_cv_hourly_tsa', 'mean_std_dep_delay', 'mean_coupled_volatility', 'mean_dep_delay']].to_string(index=False))

    # -------------------------------------------------------------------------
    # STEP 4: HOURLY DIURNAL VOLATILITY CLUSTERING (CONDITIONED ON DOW)
    # -------------------------------------------------------------------------
    print("\n[STEP 4] Executing Diurnal Hourly Volatility Clustering (Dual Peak Turbulence)...")
    con.register("daily_study_classified", daily_df)
    
    hourly_query = f"""
        WITH tsa_hr AS (
            SELECT 
                dateId,
                hour,
                SUM(throughput) as hourly_tsa
            FROM read_parquet('{TSA_PARQUET}')
            WHERE airportId IN ({TOP25_ID_STR})
            GROUP BY 1, 2
        ),
        otp_hr AS (
            SELECT 
                dateId,
                CAST(crsDepMinOfDay / 60 AS INT) as hour,
                COUNT(*) as hourly_sched_flights,
                AVG(CASE WHEN cancelled = false THEN depDel ELSE NULL END) as hourly_dep_delay,
                STDDEV(CASE WHEN cancelled = false THEN depDel ELSE NULL END) as hourly_std_delay,
                SUM(CASE WHEN cancelled = false AND depDel15 = true THEN 1 ELSE 0 END) * 100.0 / 
                    NULLIF(COUNT(CASE WHEN cancelled = false THEN 1 END), 0) as hourly_depdel15_pct,
                SUM(CASE WHEN cancelled = true THEN 1 ELSE 0 END) * 100.0 / COUNT(*) as hourly_cancel_pct
            FROM read_parquet('{OTP_PARQUET}')
            WHERE originAirportId IN ({TOP25_ID_STR})
            GROUP BY 1, 2
        )
        SELECT 
            t.dateId,
            d.date,
            d.year,
            d.month,
            d.dayOfWeek,
            d.dow_name,
            d.season_regime,
            d.season_name,
            t.hour,
            t.hourly_tsa,
            COALESCE(o.hourly_sched_flights, 0) as hourly_sched_flights,
            COALESCE(o.hourly_dep_delay, 0) as hourly_dep_delay,
            COALESCE(o.hourly_std_delay, 0) as hourly_std_delay,
            COALESCE(o.hourly_depdel15_pct, 0) as hourly_depdel15_pct,
            COALESCE(o.hourly_cancel_pct, 0) as hourly_cancel_pct
        FROM tsa_hr t
        JOIN daily_study_classified d ON t.dateId = d.dateId
        LEFT JOIN otp_hr o ON t.dateId = o.dateId AND t.hour = o.hour
        WHERE t.hour >= 0 AND t.hour <= 23
        ORDER BY t.dateId, t.hour
    """
    hourly_df = con.execute(hourly_query).df()
    print(f"Loaded {len(hourly_df)} hourly joint observation records.")
    
    # Compute diurnal profile by Day of Week and Hour (168 cells = 7 x 24)
    dow_hr_profile = hourly_df.groupby(['dayOfWeek', 'dow_name', 'hour']).agg(
        obs_count=('dateId', 'count'),
        mean_hourly_tsa=('hourly_tsa', 'mean'),
        std_hourly_tsa=('hourly_tsa', 'std'),
        mean_sched_flights=('hourly_sched_flights', 'mean'),
        mean_dep_delay=('hourly_dep_delay', 'mean'),
        mean_intra_hour_delay_std=('hourly_std_delay', 'mean'),
        std_delay_between_days=('hourly_dep_delay', 'std'),
        mean_depdel15_pct=('hourly_depdel15_pct', 'mean')
    ).reset_index()
    
    dow_hr_profile['cv_hourly_tsa'] = dow_hr_profile['std_hourly_tsa'] / dow_hr_profile['mean_hourly_tsa'].replace(0, np.nan)
    
    # Cluster the 24 hours of each day of week based on the Operational Turbulence Shock Index
    diurnal_records = []
    
    for dow in range(1, 8):
        sub = dow_hr_profile[dow_hr_profile['dayOfWeek'] == dow].copy()
        
        # Flight activity mask (curfew/low-volume hours have near-zero flights)
        flight_mask = np.clip(sub['mean_sched_flights'] / 20.0, 0.0, 1.0)
        
        # 1. Normalized TSA demand surge volatility (morning arrival shock)
        v_tsa = sub['std_hourly_tsa'] / sub['std_hourly_tsa'].max()
        
        # 2. Normalized flight departure delay dispersion volatility (evening cascade shock)
        delay_vol = (sub['mean_intra_hour_delay_std'] + sub['std_delay_between_days']) * flight_mask
        v_delay = delay_vol / delay_vol.max()
        
        # Operational Turbulence Shock Index
        sub['operational_turbulence_index'] = np.maximum(v_tsa, v_delay)
        
        # 1D KMeans clustering into exactly 3 categories: Off-Peak, Mid-Peak, Peak
        km_tod = KMeans(n_clusters=3, random_state=42, n_init=25)
        sub['cl'] = km_tod.fit_predict(sub[['operational_turbulence_index']])
        
        # Order clusters monotonically by turbulence index
        cl_order_tod = sub.groupby('cl')['operational_turbulence_index'].mean().sort_values().index
        tod_map = {
            cl_order_tod[0]: '1_OFF_PEAK',
            cl_order_tod[1]: '2_MID_PEAK',
            cl_order_tod[2]: '3_PEAK'
        }
        sub['time_of_day_regime'] = sub['cl'].map(tod_map)
        
        tod_labels = {
            '1_OFF_PEAK': 'Off-Peak (Overnight & Curfew Valley)',
            '2_MID_PEAK': 'Mid-Peak (Operational Plateau & Transition)',
            '3_PEAK': 'Peak (Bank Surges & Delay Dispersion)'
        }
        sub['time_of_day_name'] = sub['time_of_day_regime'].map(tod_labels)
        diurnal_records.append(sub)
        
    diurnal_df = pd.concat(diurnal_records, ignore_index=True)
    
    # Merge diurnal classification back into hourly dataset
    dow_hour_map = diurnal_df[['dayOfWeek', 'hour', 'time_of_day_regime', 'time_of_day_name']].drop_duplicates()
    hourly_df = hourly_df.merge(dow_hour_map, on=['dayOfWeek', 'hour'], how='left')

    # -------------------------------------------------------------------------
    # STEP 5: FULL 3D CROSS-CLASSIFICATION GRID (84 CELLS)
    # -------------------------------------------------------------------------
    print("\n[STEP 5] Building Full 3D Cross-Classification Grid (Season x DOW x Diurnal)...")
    
    # Partition: Candidate B Training (2022-05-01 to 2024-12-31) vs Holdout Testing (2025-01-01 to 2025-12-31)
    hourly_df['partition'] = np.where(hourly_df['date'] <= '2024-12-31', 'Train', 'Test')
    
    grid_agg = hourly_df.groupby([
        'season_regime', 'season_name',
        'dayOfWeek', 'dow_name',
        'time_of_day_regime', 'time_of_day_name'
    ]).agg(
        total_obs=('dateId', 'count'),
        train_obs=('partition', lambda x: (x == 'Train').sum()),
        test_obs=('partition', lambda x: (x == 'Test').sum()),
        mean_hourly_tsa=('hourly_tsa', 'mean'),
        std_hourly_tsa=('hourly_tsa', 'std'),
        mean_sched_flights=('hourly_sched_flights', 'mean'),
        mean_dep_delay=('hourly_dep_delay', 'mean'),
        std_dep_delay=('hourly_dep_delay', 'std'),
        mean_depdel15_pct=('hourly_depdel15_pct', 'mean'),
        mean_cancel_pct=('hourly_cancel_pct', 'mean')
    ).reset_index()
    
    grid_agg['sufficient_for_training'] = grid_agg['train_obs'] >= 50
    grid_agg['sufficient_for_testing'] = grid_agg['test_obs'] >= 30
    grid_agg['well_powered_training'] = grid_agg['train_obs'] >= 100
    
    print(f"Total cross-classification cells: {len(grid_agg)} (Expected: 4 x 7 x 3 = 84)")
    print(f"Cells with N_train >= 50: {grid_agg['sufficient_for_training'].sum()} / {len(grid_agg)} ({grid_agg['sufficient_for_training'].mean():.1%})")
    print(f"Cells with N_train >= 100: {grid_agg['well_powered_training'].sum()} / {len(grid_agg)} ({grid_agg['well_powered_training'].mean():.1%})")
    print(f"Cells with N_test >= 30: {grid_agg['sufficient_for_testing'].sum()} / {len(grid_agg)} ({grid_agg['sufficient_for_testing'].mean():.1%})")

    # -------------------------------------------------------------------------
    # STEP 6: STATISTICAL SAMPLE SIZE & TRAINING SUFFICIENCY AUDIT
    # -------------------------------------------------------------------------
    print("\n[STEP 6] Computing Statistical Sample Size Audit...")
    sample_audit = grid_agg.groupby(['season_name', 'time_of_day_name']).agg(
        cell_count=('total_obs', 'count'),
        min_train_obs=('train_obs', 'min'),
        median_train_obs=('train_obs', 'median'),
        mean_train_obs=('train_obs', 'mean'),
        total_train_obs=('train_obs', 'sum'),
        min_test_obs=('test_obs', 'min'),
        median_test_obs=('test_obs', 'median'),
        mean_test_obs=('test_obs', 'mean'),
        total_test_obs=('test_obs', 'sum'),
        all_train_sufficient=('sufficient_for_training', 'all'),
        all_test_sufficient=('sufficient_for_testing', 'all')
    ).reset_index()
    
    print("\n--- SAMPLE SIZE AUDIT PER MACRO / DIURNAL BLOCK ---")
    print(sample_audit[['season_name', 'time_of_day_name', 'min_train_obs', 'median_train_obs', 'total_train_obs', 'min_test_obs', 'median_test_obs', 'total_test_obs']].to_string(index=False))

    # -------------------------------------------------------------------------
    # STEP 7: EXPORT CSV DELIVERABLES TO TARGET FOLDERS
    # -------------------------------------------------------------------------
    print("\n[STEP 7] Exporting CSV deliverable files...")
    csv_dict = {
        "seasonal_regimes_summary.csv": season_summary,
        "day_of_week_regimes_summary.csv": dow_summary,
        "diurnal_hourly_by_dow.csv": diurnal_df,
        "temporal_cross_classification_grid.csv": grid_agg,
        "sample_size_training_sufficiency.csv": sample_audit
    }
    
    for filename, df_table in csv_dict.items():
        for target_dir in OUTPUT_DIRS:
            target_path = os.path.join(target_dir, filename)
            df_table.to_csv(target_path, index=False)
            print(f"Exported: {target_path}")

    # -------------------------------------------------------------------------
    # STEP 8: BUILD FORMATTED MULTI-SHEET EXCEL WORKBOOK (season-analysis.xlsx)
    # -------------------------------------------------------------------------
    print("\n[STEP 8] Compiling multi-sheet Excel workbook season-analysis.xlsx...")
    
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    
    # 1. Table of Contents Sheet
    ws_toc = wb.create_sheet(title="Table_of_Contents")
    ws_toc.views.sheetView[0].showGridLines = True
    
    # TOC Header Styling
    header_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    header_font = Font(name="Calibri", size=14, bold=True, color="FFFFFF")
    sub_font = Font(name="Calibri", size=10, italic=True, color="595959")
    th_fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
    th_font = Font(name="Calibri", size=11, bold=True, color="000000")
    
    ws_toc["A1"] = "SEASON-ANALYSIS — EMPIRICAL VOLATILITY DATA SUITE"
    ws_toc["A1"].font = header_font
    ws_toc["A1"].fill = header_fill
    ws_toc.merge_cells("A1:E1")
    
    ws_toc["A2"] = "Coupled TSA Throughput & BTS Flight Operations Volatility Clustering | Top 25 Airfields"
    ws_toc["A2"].font = sub_font
    ws_toc.merge_cells("A2:E2")
    
    toc_headers = ["#", "Sheet Tab", "Source Deliverable File", "Observations / Rows", "Feature Dimensions"]
    for col_idx, h_text in enumerate(toc_headers, 1):
        cell = ws_toc.cell(row=4, column=col_idx, value=h_text)
        cell.font = th_font
        cell.fill = th_fill
        cell.alignment = Alignment(horizontal="center" if col_idx in [1, 4, 5] else "left", vertical="center")
        
    toc_data = [
        (1, "day_of_week_regimes_summary", "day_of_week_regimes_summary.csv", len(dow_summary), len(dow_summary.columns)),
        (2, "diurnal_hourly_by_dow", "diurnal_hourly_by_dow.csv", len(diurnal_df), len(diurnal_df.columns)),
        (3, "sample_size_training_sufficienc", "sample_size_training_sufficiency.csv", len(sample_audit), len(sample_audit.columns)),
        (4, "seasonal_regimes_summary", "seasonal_regimes_summary.csv", len(season_summary), len(season_summary.columns)),
        (5, "temporal_cross_classification_g", "temporal_cross_classification_grid.csv", len(grid_agg), len(grid_agg.columns))
    ]
    
    for row_idx, row_vals in enumerate(toc_data, 5):
        for col_idx, val in enumerate(row_vals, 1):
            cell = ws_toc.cell(row=row_idx, column=col_idx, value=val)
            cell.alignment = Alignment(horizontal="center" if col_idx in [1, 4, 5] else "left", vertical="center")
            
    # Auto-adjust TOC widths
    for col in ws_toc.columns:
        max_len = max(len(str(cell.value or '')) for cell in col)
        col_letter = get_column_letter(col[0].column)
        ws_toc.column_dimensions[col_letter].width = max(max_len + 3, 10)
        
    # Helper for adding data sheets
    sheet_meta = [
        ("day_of_week_regimes_summary", dow_summary),
        ("diurnal_hourly_by_dow", diurnal_df),
        ("sample_size_training_sufficienc", sample_audit),
        ("seasonal_regimes_summary", season_summary),
        ("temporal_cross_classification_g", grid_agg)
    ]
    
    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )
    
    for title, df_data in sheet_meta:
        ws = wb.create_sheet(title=title)
        ws.views.sheetView[0].showGridLines = True
        
        # Write headers
        for col_idx, col_name in enumerate(df_data.columns, 1):
            c = ws.cell(row=1, column=col_idx, value=col_name)
            c.font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
            c.fill = PatternFill(start_color="2F5597", end_color="2F5597", fill_type="solid")
            c.alignment = Alignment(horizontal="center", vertical="center")
            
        # Write data rows
        for r_idx, row_values in enumerate(df_data.itertuples(index=False), 2):
            for c_idx, val in enumerate(row_values, 1):
                c = ws.cell(row=r_idx, column=c_idx, value=val)
                c.font = Font(name="Calibri", size=10)
                c.border = thin_border
                
                # Format numbers
                if isinstance(val, (int, np.integer)):
                    c.number_format = '#,##0'
                    c.alignment = Alignment(horizontal="right")
                elif isinstance(val, (float, np.floating)):
                    if "pct" in df_data.columns[c_idx - 1] or "share" in df_data.columns[c_idx - 1]:
                        c.number_format = '0.00"%"'
                    elif "cv" in df_data.columns[c_idx - 1] or "index" in df_data.columns[c_idx - 1]:
                        c.number_format = '0.000'
                    else:
                        c.number_format = '#,##0.00'
                    c.alignment = Alignment(horizontal="right")
                elif isinstance(val, bool):
                    c.alignment = Alignment(horizontal="center")
                else:
                    c.alignment = Alignment(horizontal="left")
                    
        # Column width formatting
        for col in ws.columns:
            max_len = max(len(str(cell.value or '')) for cell in col)
            col_letter = get_column_letter(col[0].column)
            ws.column_dimensions[col_letter].width = min(max(max_len + 3, 11), 40)
            
    # Save workbook in all target directories
    for target_dir in OUTPUT_DIRS:
        excel_target = os.path.join(target_dir, "season-analysis.xlsx")
        wb.save(excel_target)
        print(f"Saved Excel Suite: {excel_target}")

    # -------------------------------------------------------------------------
    # STEP 9: GENERATE HIGH-RESOLUTION FIGURES (300 DPI)
    # -------------------------------------------------------------------------
    print("\n[STEP 9] Rendering publication-quality volatility figures...")
    sns.set_theme(style="whitegrid", font_scale=1.1)
    
    # FIGURE 1: Coupled Volatility Phase Space & Annual Seasonality
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    reg_colors = {
        '1_OFF_PEAK': '#2b5c8f',
        '2_MID_PEAK': '#2ca02c',
        '3_PEAK': '#d62728',
        '4_HOLIDAY': '#9467bd'
    }
    reg_labels = {
        '1_OFF_PEAK': '1. Off-Peak (Winter Lull / Fall Shoulder)',
        '2_MID_PEAK': '2. Mid-Peak (Spring & Summer Shoulder)',
        '3_PEAK': '3. Peak (Summer Convective Storms)',
        '4_HOLIDAY': '4. Holiday (National Waves)'
    }
    
    for reg, grp in daily_df.groupby('season_regime'):
        ax1.scatter(
            grp['cv_hourly_tsa'],
            grp['std_dep_delay'],
            color=reg_colors[reg],
            label=reg_labels[reg],
            alpha=0.6,
            edgecolors='none',
            s=45
        )
    ax1.set_xlabel(r"Within-Day TSA Hourly Arrival Volatility (CV = $\sigma_{TSA} / \mu_{TSA}$)", fontweight='bold')
    ax1.set_ylabel(r"Flight Departure Delay Dispersion ($\sigma_{Delay}$, Minutes)", fontweight='bold')
    ax1.set_title(r"(A) Coupled Volatility Phase Space ($CV_{TSA}$ vs. $\sigma_{Delay}$)", fontweight='bold', pad=12)
    ax1.legend(loc="upper right", frameon=True)
    
    # Panel B: Calendar Month Coupled Volatility Profile
    m_agg = daily_df.groupby('month').agg(
        mean_cv_tsa=('cv_hourly_tsa', 'mean'),
        mean_std_delay=('std_dep_delay', 'mean'),
        mean_coupled_vol=('coupled_volatility_index', 'mean')
    ).reset_index()
    
    ax2_twin = ax2.twinx()
    b1 = ax2.bar(m_agg['month'], m_agg['mean_cv_tsa'], color='#1f77b4', alpha=0.75, width=0.55, label='TSA Arrival CV')
    l1 = ax2_twin.plot(m_agg['month'], m_agg['mean_std_delay'], color='#d62728', marker='o', linewidth=2.5, markersize=7, label=r'Delay Dispersion ($\sigma_{Delay}$)')
    
    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    ax2.set_xticks(range(1, 13))
    ax2.set_xticklabels(month_labels)
    ax2.set_xlabel("Calendar Month", fontweight='bold')
    ax2.set_ylabel("Within-Day TSA Hourly Volatility (CV)", color='#1f77b4', fontweight='bold')
    ax2_twin.set_ylabel("Departure Delay Standard Deviation (min)", color='#d62728', fontweight='bold')
    ax2.set_title("(B) Annual Monthly Coupled Volatility Dynamics", fontweight='bold', pad=12)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2_twin.grid(False)
    
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES_DIR, "01_annual_volatility_tsa_otp_clustering.png"), dpi=300)
    fig.savefig(os.path.join(FIGURES_DIR, "01_annual_seasonality_tsa_otp_clustering.png"), dpi=300)
    plt.close()
    print("Saved Figure 1: 01_annual_volatility_tsa_otp_clustering.png")

    # FIGURE 2: Day of Week Volatility Dynamics
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    dow_sorted = dow_summary.sort_values('dayOfWeek')
    
    # Panel A: TSA Volatility & Surge Ratio
    ax1_twin = ax1.twinx()
    ax1.bar(range(len(dow_sorted)), dow_sorted['mean_cv_hourly_tsa'], color='#3470a3', alpha=0.8, width=0.55, label='TSA Hourly CV')
    ax1_twin.plot(range(len(dow_sorted)), dow_sorted['mean_peak_to_mean_tsa'], color='#ff7f0e', marker='^', linewidth=2.5, markersize=8, label='Peak-to-Mean Ratio')
    ax1.set_ylabel("Mean Within-Day TSA Volatility ($CV$)", color='#3470a3', fontweight='bold')
    ax1_twin.set_ylabel("Peak-to-Mean Arrival Ratio", color='#ff7f0e', fontweight='bold')
    ax1.set_xticks(range(len(dow_sorted)))
    ax1.set_xticklabels(dow_sorted['dow_name'], rotation=25, ha='right')
    ax1.set_title("(A) Day-of-Week Checkpoint Arrival Volatility", fontweight='bold', pad=12)
    ax1.grid(True, linestyle='--', alpha=0.5)
    ax1_twin.grid(False)
    
    # Panel B: Delay Dispersion and Coupled Volatility Index
    ax2_twin = ax2.twinx()
    ax2.bar(range(len(dow_sorted)), dow_sorted['mean_std_dep_delay'], color='#e377c2', alpha=0.75, width=0.55, label=r'Delay Std Dev ($\sigma_{Delay}$)')
    ax2_twin.plot(range(len(dow_sorted)), dow_sorted['mean_coupled_volatility'], color='#d62728', marker='s', linewidth=2.5, markersize=8, label='Coupled Volatility Index')
    ax2.set_ylabel(r"Mean Departure Delay Dispersion ($\sigma_{Delay}$, min)", color='#e377c2', fontweight='bold')
    ax2_twin.set_ylabel(r"Coupled Volatility Index ($CV_{TSA} \times \sigma_{Delay}$)", color='#d62728', fontweight='bold')
    ax2.set_xticks(range(len(dow_sorted)))
    ax2.set_xticklabels(dow_sorted['dow_name'], rotation=25, ha='right')
    ax2.set_title("(B) Weekly Delay Dispersion & Operational Coupling", fontweight='bold', pad=12)
    ax2.grid(True, linestyle='--', alpha=0.5)
    ax2_twin.grid(False)
    
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES_DIR, "02_day_of_week_volatility_dynamics.png"), dpi=300)
    fig.savefig(os.path.join(FIGURES_DIR, "02_day_of_week_dynamics.png"), dpi=300)
    plt.close()
    print("Saved Figure 2: 02_day_of_week_volatility_dynamics.png")

    # FIGURE 3: Diurnal 24-Hour Volatility Heatmap Conditioning on Day of Week
    fig, ax = plt.subplots(figsize=(18, 7.5))
    pivot_tod = diurnal_df.pivot(index='dow_name', columns='hour', values='time_of_day_regime')
    dow_display_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    pivot_numeric = pivot_tod.replace({'1_OFF_PEAK': 0, '2_MID_PEAK': 1, '3_PEAK': 2}).reindex(dow_display_order).astype(float)
    
    cmap = matplotlib.colors.ListedColormap(['#d9e6f2', '#a1d99b', '#de2d26'])
    bounds = [-0.5, 0.5, 1.5, 2.5]
    norm = matplotlib.colors.BoundaryNorm(bounds, cmap.N)
    
    im = ax.imshow(pivot_numeric.values, cmap=cmap, norm=norm, aspect='auto', interpolation='nearest')
    ax.set_xticks(range(24))
    ax.set_xticklabels([f"{h:02d}:00" for h in range(24)], rotation=45, ha='right', fontweight='bold')
    ax.set_yticks(range(len(dow_display_order)))
    ax.set_yticklabels(dow_display_order, fontweight='bold', fontsize=12)
    ax.set_xlabel("Hour of Day (Local Scheduled Airport Time)", fontweight='bold', labelpad=10)
    ax.set_title("Empirical Diurnal Volatility Heatmap (Conditioned on Day of Week)\nIllustrating Dual Non-Consecutive Peaks: Morning Screening Surge & Evening Delay Dispersion", fontweight='bold', pad=15)
    
    for r in range(len(dow_display_order)):
        for c in range(24):
            val = pivot_numeric.iloc[r, c]
            txt = "Off" if val == 0 else ("Mid" if val == 1 else "PEAK")
            color = "white" if val == 2 else "black"
            fontw = "bold" if val == 2 else "normal"
            ax.text(c, r, txt, ha="center", va="center", color=color, fontweight=fontw, fontsize=9.5)
            
    cbar = fig.colorbar(im, ax=ax, ticks=[0, 1, 2], orientation='horizontal', pad=0.18, shrink=0.7)
    cbar.ax.set_xticklabels([
        '1. Off-Peak (Overnight & Curfew Valley: Low Volatility)',
        '2. Mid-Peak (Midday Plateau & Transition: Steady Flow)',
        '3. Peak (Morning Screening Surge & Evening Delay Cascade: Extreme Turbulence)'
    ], fontweight='bold', fontsize=11)
    
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES_DIR, "03_diurnal_hourly_volatility_clusters_by_dow.png"), dpi=300)
    fig.savefig(os.path.join(FIGURES_DIR, "03_diurnal_hourly_clusters_by_dow.png"), dpi=300)
    plt.close()
    print("Saved Figure 3: 03_diurnal_hourly_volatility_clusters_by_dow.png")

    # FIGURE 4: Statistical Sample Size & Training Sufficiency Verification
    fig, ax = plt.subplots(figsize=(14, 6))
    sns.boxplot(
        data=grid_agg,
        x='season_name',
        y='train_obs',
        hue='time_of_day_name',
        palette=['#6baed6', '#74c476', '#fb6a4a'],
        ax=ax
    )
    ax.axhline(100, color='red', linestyle='--', linewidth=2, label='ML Training Threshold ($N = 100$)')
    ax.axhline(50, color='darkorange', linestyle=':', linewidth=1.8, label='Minimum Viable Threshold ($N = 50$)')
    ax.set_yscale('log')
    ax.set_xlabel("Annual Seasonal Volatility Regime", fontweight='bold')
    ax.set_ylabel("Observations per Temporal Cell in Training Set (Log Scale)", fontweight='bold')
    ax.set_title("Statistical Sample Size & Training Sufficiency Audit across 84 Temporal Cells\nCandidate B Training Partition (May 2022 – Dec 2024)", fontweight='bold', pad=12)
    ax.legend(loc='lower left', frameon=True)
    ax.set_xticks(range(4))
    ax.set_xticklabels(['Off-Peak (Winter/Fall)', 'Mid-Peak (Spring/Shoulder)', 'Peak (Summer Surge)', 'Holiday (Corridors)'], rotation=15, ha='right')
    
    fig.tight_layout()
    fig.savefig(os.path.join(FIGURES_DIR, "04_sample_sufficiency_distribution.png"), dpi=300)
    plt.close()
    print("Saved Figure 4: 04_sample_sufficiency_distribution.png")

    print("\n" + "=" * 80)
    print("VOLATILITY CLUSTERING PIPELINE COMPLETED SUCCESSFULLY.")
    print("Outputs synchronized in:")
    for d in OUTPUT_DIRS:
        print(f"  -> {d}")
    print("=" * 80)

if __name__ == "__main__":
    run_volatility_analysis()
