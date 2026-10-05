import duckdb
import pandas as pd
import numpy as np

def run_candidate_b_analysis():
    con = duckdb.connect('data/warehouse.duckdb', read_only=True)
    print("="*90)
    print("IN-DEPTH ANALYSIS: CANDIDATE B REGIME (MAY 1, 2022 TO DECEMBER 31, 2025)")
    print("="*90)

    # 1. Dataset Dimensions and Overview
    overview_sql = """
    SELECT 
        COUNT(*) AS total_hourly_obs,
        COUNT(DISTINCT tl.airportId) AS num_airports,
        COUNT(DISTINCT tl.dateId) AS total_calendar_days,
        MIN(d.date) AS start_date,
        MAX(d.date) AS end_date,
        SUM(tl.tsaThroughput) AS total_tsa_passengers,
        SUM(tl.contemporaneousSchedFlights) AS total_sched_flights,
        SUM(tl.convolvedSchedFlights) AS total_convolved_flights,
        SUM(tl.priorHourCancelledFlights) AS total_cancelled_flights,
        ROUND(AVG(tl.priorHourAvgDepDel), 2) AS mean_dep_del_min,
        ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS mean_depDel15_pct,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_sched_flight,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS convolved_r2,
        ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS convolved_slope
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE tl.dateId BETWEEN 20220501 AND 20251231;
    """
    df_overview = con.execute(overview_sql).df()
    print("\n--- 1. OVERALL CANDIDATE B SCOPE ---")
    print(df_overview.to_string(index=False))

    # 2. Annual Breakdown within Candidate B
    annual_sql = """
    SELECT 
        d.year,
        COUNT(*) AS hourly_obs,
        COUNT(DISTINCT d.dateId) AS days,
        SUM(tl.tsaThroughput) AS annual_tsa,
        SUM(tl.contemporaneousSchedFlights) AS sched_flights,
        SUM(tl.convolvedSchedFlights) AS convolved_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_flight,
        ROUND(AVG(tl.priorHourAvgDepDel), 2) AS avg_delay_min,
        ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS depDel15_pct,
        SUM(tl.priorHourCancelledFlights) AS cancelled_flights,
        ROUND(regr_r2(tl.tsaThroughput, tl.contemporaneousSchedFlights), 4) AS r2_contemp,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS slope_convolved,
        ROUND(regr_intercept(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS intercept_convolved
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE tl.dateId BETWEEN 20220501 AND 20251231
    GROUP BY d.year
    ORDER BY d.year;
    """
    df_annual = con.execute(annual_sql).df()
    print("\n--- 2. ANNUAL BREAKDOWN (CANDIDATE B) ---")
    print(df_annual.to_string(index=False))

    # 3. Monthly Progression: Load Factor, OTP Delays, Throughput, and R2
    monthly_sql = """
    WITH monthly_t100 AS (
        SELECT 
            year,
            month,
            SUM(seats) AS seats,
            SUM(passengers) AS pax,
            ROUND(SUM(passengers)::DOUBLE / NULLIF(SUM(seats), 0), 4) AS sys_load_factor,
            ROUND(AVG(loadFactor), 4) AS mean_load_factor
        FROM t100v1
        WHERE (year = 2022 AND month >= 5) OR (year BETWEEN 2023 AND 2025)
        GROUP BY year, month
    ),
    monthly_demand AS (
        SELECT 
            strftime(d.date, '%Y-%m') AS ym,
            d.year,
            d.month,
            SUM(tl.tsaThroughput) AS monthly_tsa,
            SUM(tl.contemporaneousSchedFlights) AS monthly_flights,
            SUM(tl.convolvedSchedFlights) AS monthly_convolved_flights,
            ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_flight,
            ROUND(AVG(tl.priorHourAvgDepDel), 2) AS avg_delay_min,
            ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS depDel15_pct,
            SUM(tl.priorHourCancelledFlights) AS cancelled_flights,
            ROUND(regr_r2(tl.tsaThroughput, tl.contemporaneousSchedFlights), 4) AS r2_contemp,
            ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2_convolved,
            ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS slope_convolved
        FROM vw_airport_hourly_demand tl
        JOIN dim_date d ON tl.dateId = d.dateId
        WHERE tl.dateId BETWEEN 20220501 AND 20251231
        GROUP BY strftime(d.date, '%Y-%m'), d.year, d.month
    )
    SELECT 
        md.ym,
        md.monthly_tsa,
        md.monthly_flights,
        md.pax_per_flight,
        ROUND(t.sys_load_factor * 100, 2) AS sys_load_factor_pct,
        ROUND(t.mean_load_factor * 100, 2) AS mean_load_factor_pct,
        md.avg_delay_min,
        md.depDel15_pct,
        md.cancelled_flights,
        md.r2_contemp,
        md.r2_convolved,
        md.slope_convolved
    FROM monthly_demand md
    LEFT JOIN monthly_t100 t ON md.year = t.year AND md.month = t.month
    ORDER BY md.ym;
    """
    df_monthly = con.execute(monthly_sql).df()
    print("\n--- 3. MONTHLY METRICS (TSA, OTP, LOAD FACTOR) ---")
    print(df_monthly.to_string(index=False))

    # 4. T-100 Load Factor Impact on Correlation & Explanatory Power
    print("\n--- 4. T-100 LOAD FACTOR INTEGRATION ANALYSIS ---")
    lf_integration_sql = """
    WITH monthly_airport_t100 AS (
        SELECT 
            year,
            month,
            originAirportId AS airportId,
            SUM(seats) AS airport_seats,
            SUM(passengers) AS airport_pax,
            ROUND(SUM(passengers)::DOUBLE / NULLIF(SUM(seats), 0), 4) AS airport_lf
        FROM t100v1
        WHERE (year = 2022 AND month >= 5) OR (year BETWEEN 2023 AND 2025)
        GROUP BY year, month, originAirportId
    ),
    enriched AS (
        SELECT 
            tl.tsaThroughput,
            tl.contemporaneousSchedFlights,
            tl.schedFlights_lead1,
            tl.schedFlights_lead2,
            tl.schedFlights_lead3,
            tl.convolvedSchedFlights,
            COALESCE(t.airport_lf, 0.84) AS airport_lf,
            tl.convolvedSchedFlights * COALESCE(t.airport_lf, 0.84) AS lf_convolved_flights
        FROM vw_airport_hourly_demand tl
        LEFT JOIN monthly_airport_t100 t 
            ON tl.airportId = t.airportId 
           AND tl.year = t.year 
           AND tl.month = t.month
        WHERE tl.dateId BETWEEN 20220501 AND 20251231
    )
    SELECT 
        ROUND(regr_r2(tsaThroughput, contemporaneousSchedFlights), 4) AS r2_contemp,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead1), 4) AS r2_lead1,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead2), 4) AS r2_lead2,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead3), 4) AS r2_lead3,
        ROUND(regr_r2(tsaThroughput, convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_r2(tsaThroughput, lf_convolved_flights), 4) AS r2_lf_convolved,
        ROUND(corr(tsaThroughput, convolvedSchedFlights), 4) AS corr_convolved,
        ROUND(corr(tsaThroughput, lf_convolved_flights), 4) AS corr_lf_convolved,
        ROUND(regr_slope(tsaThroughput, convolvedSchedFlights), 2) AS slope_raw_flights,
        ROUND(regr_slope(tsaThroughput, lf_convolved_flights), 2) AS slope_lf_flights
    FROM enriched;
    """
    df_lf_impact = con.execute(lf_integration_sql).df()
    print(df_lf_impact.to_string(index=False))

    # 5. Airport Cohorts within Candidate B
    print("\n--- 5. AIRPORT COHORT DYNAMICS (CANDIDATE B) ---")
    cohort_sql = """
    WITH airport_cohorts AS (
        SELECT 
            airportId,
            airportCode,
            faaHubCategory,
            CASE 
                WHEN airportCode IN ('ATL', 'DFW', 'DEN', 'ORD', 'CLT') THEN '1_Top5_MegaHubs'
                WHEN airportCode IN ('LAS', 'MCO', 'MIA', 'TPA', 'PHX') THEN '2_Leisure_Sunbelt'
                WHEN airportCode IN ('BOS', 'DCA', 'LGA', 'SFO', 'JFK') THEN '3_Business_Coastal'
                ELSE '4_Other_Large_Hubs'
            END AS cohort
        FROM dim_airport
        WHERE airportId > 0
    )
    SELECT 
        ac.cohort,
        COUNT(DISTINCT ac.airportCode) AS num_apts,
        SUM(tl.tsaThroughput) AS total_tsa,
        ROUND(SUM(tl.tsaThroughput) * 100.0 / (SELECT SUM(tsaThroughput) FROM vw_airport_hourly_demand WHERE dateId BETWEEN 20220501 AND 20251231), 2) AS pct_system_tsa,
        SUM(tl.contemporaneousSchedFlights) AS total_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_flight,
        ROUND(AVG(tl.priorHourAvgDepDel), 2) AS avg_delay_min,
        ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS depDel15_pct,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS slope_convolved,
        ROUND(corr(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS corr_convolved
    FROM vw_airport_hourly_demand tl
    JOIN airport_cohorts ac ON tl.airportId = ac.airportId
    WHERE tl.dateId BETWEEN 20220501 AND 20251231
    GROUP BY ac.cohort
    ORDER BY ac.cohort;
    """
    df_cohort = con.execute(cohort_sql).df()
    print(df_cohort.to_string(index=False))

    # 6. Stationarity & Autocorrelation Tests
    print("\n--- 6. DAILY AGGREGATE STATIONARITY METRICS (CANDIDATE B) ---")
    daily_sql = """
    SELECT 
        d.date,
        SUM(tl.tsaThroughput) AS daily_tsa,
        SUM(tl.convolvedSchedFlights) AS daily_convolved_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS daily_pax_per_flight,
        AVG(tl.priorHourDepDel15Rate) AS daily_del15_rate,
        SUM(tl.priorHourCancelledFlights) AS daily_cancellations
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE tl.dateId BETWEEN 20220501 AND 20251231
    GROUP BY d.date
    ORDER BY d.date;
    """
    df_daily = con.execute(daily_sql).df()
    
    # Statistical properties of daily series
    tsa_series = df_daily['daily_tsa'].values
    pax_flt_series = df_daily['daily_pax_per_flight'].values
    
    print(f"Daily TSA Mean: {np.mean(tsa_series):,.0f}, Std: {np.std(tsa_series):,.0f}, Coeff of Var (CV): {np.std(tsa_series)/np.mean(tsa_series):.4f}")
    print(f"Daily Pax/Flight Mean: {np.mean(pax_flt_series):.2f}, Std: {np.std(pax_flt_series):.2f}, Coeff of Var (CV): {np.std(pax_flt_series)/np.mean(pax_flt_series):.4f}")
    
    # Check autocorrelations
    ac1 = pd.Series(tsa_series).autocorr(lag=1)
    ac7 = pd.Series(tsa_series).autocorr(lag=7)
    ac14 = pd.Series(tsa_series).autocorr(lag=14)
    print(f"Daily TSA Autocorrelations: lag-1={ac1:.4f}, lag-7 (weekly seasonality)={ac7:.4f}, lag-14={ac14:.4f}")

    # 7. Model Benchmarking across Train / Val / Test splits within Candidate B
    print("\n--- 7. OUT-OF-TIME ML MODEL BENCHMARKING WITHIN CANDIDATE B ---")
    print("Partition Design:")
    print("  Train: 2022-05-01 to 2024-04-30 (24 months, 404,324 hourly rows)")
    print("  Validation: 2024-05-01 to 2024-12-31 (8 months, 137,879 hourly rows)")
    print("  Test (Holdout): 2025-01-01 to 2025-12-31 (12 months, 215,562 hourly rows)")
    
    ml_sql = """
    WITH monthly_airport_t100 AS (
        SELECT 
            year,
            month,
            originAirportId AS airportId,
            ROUND(SUM(passengers)::DOUBLE / NULLIF(SUM(seats), 0), 4) AS airport_lf
        FROM t100v1
        WHERE (year = 2022 AND month >= 5) OR (year BETWEEN 2023 AND 2025)
        GROUP BY year, month, originAirportId
    )
    SELECT 
        tl.dateId,
        tl.hour,
        tl.dayOfWeek,
        tl.month,
        tl.airportId,
        tl.tsaThroughput,
        tl.contemporaneousSchedFlights,
        tl.convolvedSchedFlights,
        COALESCE(t.airport_lf, 0.84) AS loadFactor,
        tl.convolvedSchedFlights * COALESCE(t.airport_lf, 0.84) AS lfConvolvedFlights,
        tl.priorHourAvgDepDel,
        tl.priorHourDepDel15Rate,
        tl.priorHourCancelledFlights
    FROM vw_airport_hourly_demand tl
    LEFT JOIN monthly_airport_t100 t 
        ON tl.airportId = t.airportId 
       AND tl.year = t.year 
       AND tl.month = t.month
    WHERE tl.dateId BETWEEN 20220501 AND 20251231;
    """
    df_ml = con.execute(ml_sql).df()
    con.close()

    # Feature preparation
    df_ml['hour_sin'] = np.sin(2 * np.pi * df_ml['hour'] / 24.0)
    df_ml['hour_cos'] = np.cos(2 * np.pi * df_ml['hour'] / 24.0)
    df_ml['dow_sin'] = np.sin(2 * np.pi * df_ml['dayOfWeek'] / 7.0)
    df_ml['dow_cos'] = np.cos(2 * np.pi * df_ml['dayOfWeek'] / 7.0)
    df_ml['month_sin'] = np.sin(2 * np.pi * df_ml['month'] / 12.0)
    df_ml['month_cos'] = np.cos(2 * np.pi * df_ml['month'] / 12.0)
    
    # Airport dummies
    df_ml = pd.get_dummies(df_ml, columns=['airportId'], drop_first=True, dtype=float)
    apt_dummies = [c for c in df_ml.columns if c.startswith('airportId_')]
    
    temporal_features = ['hour_sin', 'hour_cos', 'dow_sin', 'dow_cos', 'month_sin', 'month_cos'] + apt_dummies

    # Splits
    train_mask = (df_ml['dateId'] >= 20220501) & (df_ml['dateId'] <= 20240430)
    val_mask = (df_ml['dateId'] >= 20240501) & (df_ml['dateId'] <= 20241231)
    test_mask = (df_ml['dateId'] >= 20250101) & (df_ml['dateId'] <= 20251231)

    df_train = df_ml[train_mask]
    df_val = df_ml[val_mask]
    df_test = df_ml[test_mask]

    y_train = df_train['tsaThroughput'].values
    y_val = df_val['tsaThroughput'].values
    y_test = df_test['tsaThroughput'].values

    # Model Architecture Comparisons:
    model_specs = {
        'M1: Contemporaneous Flights Only': ['contemporaneousSchedFlights'] + temporal_features,
        'M2: Convolved Lead Flights Only': ['convolvedSchedFlights'] + temporal_features,
        'M3: Convolved Flights + OTP Operational Delays/Cancels': [
            'convolvedSchedFlights', 'priorHourAvgDepDel', 'priorHourDepDel15Rate', 'priorHourCancelledFlights'
        ] + temporal_features,
        'M4: Convolved Flights + Load Factor Interaction (LF * Flights)': [
            'convolvedSchedFlights', 'loadFactor', 'lfConvolvedFlights'
        ] + temporal_features,
        'M5: Full Tri-Modal Pipeline (Convolved Flights + Load Factor + OTP Delays)': [
            'convolvedSchedFlights', 'loadFactor', 'lfConvolvedFlights',
            'priorHourAvgDepDel', 'priorHourDepDel15Rate', 'priorHourCancelledFlights'
        ] + temporal_features,
    }

    results = []
    for model_name, feature_list in model_specs.items():
        X_train = np.column_stack([np.ones(len(df_train)), df_train[feature_list].values])
        X_val = np.column_stack([np.ones(len(df_val)), df_val[feature_list].values])
        X_test = np.column_stack([np.ones(len(df_test)), df_test[feature_list].values])

        alpha = 10.0
        XTX = X_train.T @ X_train + alpha * np.eye(X_train.shape[1])
        XTy = X_train.T @ y_train
        beta = np.linalg.solve(XTX, XTy)

        y_pred_val = X_val @ beta
        y_pred_test = X_test @ beta

        test_rmse = np.sqrt(np.mean((y_test - y_pred_test) ** 2))
        test_mae = np.mean(np.abs(y_test - y_pred_test))
        test_bias = np.mean(y_pred_test - y_test)
        test_r2 = 1 - (np.sum((y_test - y_pred_test) ** 2) / np.sum((y_test - y_test.mean()) ** 2))
        
        val_rmse = np.sqrt(np.mean((y_val - y_pred_val) ** 2))
        val_r2 = 1 - (np.sum((y_val - y_pred_val) ** 2) / np.sum((y_val - y_val.mean()) ** 2))

        results.append({
            'Model Specification': model_name,
            'Num Features': len(feature_list) + 1,
            'Val R2': round(val_r2, 4),
            'Val RMSE': round(val_rmse, 1),
            'Test R2 (2025)': round(test_r2, 4),
            'Test RMSE (2025)': round(test_rmse, 1),
            'Test MAE (2025)': round(test_mae, 1),
            'Mean Bias': round(test_bias, 1)
        })

    df_results = pd.DataFrame(results)
    print("\n--- ML MODEL EVALUATION MATRIX (VALIDATION 2024 & TEST 2025) ---")
    print(df_results.to_string(index=False))

    print("\n" + "="*90)
    print("CANDIDATE B ANALYSIS COMPLETE.")
    print("="*90)

if __name__ == '__main__':
    run_candidate_b_analysis()
