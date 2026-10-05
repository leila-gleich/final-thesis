import duckdb
import pandas as pd
import numpy as np
import os

def run_in_depth_analysis():
    con = duckdb.connect('data/warehouse.duckdb', read_only=True)
    print("Connected to DuckDB database.")

    # 1. Macro Annual Overview (2019 - 2025)
    print("\n" + "="*80)
    print("1. MACRO ANNUAL METRICS (2019 - 2025)")
    print("="*80)
    annual_sql = """
    SELECT 
        d.year,
        SUM(tl.tsaThroughput) AS total_tsa_throughput,
        SUM(tl.contemporaneousSchedFlights) AS total_sched_flights,
        SUM(tl.convolvedSchedFlights) AS total_convolved_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_sched_flight,
        ROUND(AVG(tl.priorHourAvgDepDel), 2) AS avg_prior_dep_del,
        ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS depDel15_pct,
        SUM(tl.priorHourCancelledFlights) AS total_cancelled_flights,
        ROUND(regr_r2(tl.tsaThroughput, tl.contemporaneousSchedFlights), 4) AS r2_contemp,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS slope_convolved,
        ROUND(regr_intercept(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS intercept_convolved
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE d.year BETWEEN 2019 AND 2025
    GROUP BY d.year
    ORDER BY d.year;
    """
    df_annual = con.execute(annual_sql).df()
    print(df_annual.to_string(index=False))

    # 2. Lead-Lag Alignment Comparison (Pre vs Pandemic vs Post)
    print("\n" + "="*80)
    print("2. LEAD-LAG ARCHITECTURE COMPARISON ACROSS OPERATIONAL REGIMES")
    print("="*80)
    lead_lag_sql = """
    WITH periods AS (
        SELECT 
            *,
            CASE 
                WHEN dateId BETWEEN 20190101 AND 20200229 THEN '1_Pre_Pandemic (2019-01 to 2020-02)'
                WHEN dateId BETWEEN 20200301 AND 20200630 THEN '2_Acute_Lockdown (2020-03 to 2020-06)'
                WHEN dateId BETWEEN 20200701 AND 20210331 THEN '3_Depressed_Pandemic (2020-07 to 2021-03)'
                WHEN dateId BETWEEN 20210401 AND 20220430 THEN '4_Vaccine_Rebound (2021-04 to 2022-04)'
                WHEN dateId BETWEEN 20220501 AND 20221231 THEN '5_Early_Post_Pandemic (2022-05 to 2022-12)'
                WHEN dateId BETWEEN 20230101 AND 20251231 THEN '6_Mature_Post_Pandemic (2023-01 to 2025-12)'
                ELSE 'Other'
            END AS regime
        FROM vw_airport_hourly_demand
        WHERE dateId <= 20251231
    )
    SELECT 
        regime,
        COUNT(*) AS obs,
        ROUND(AVG(tsaThroughput), 1) AS avg_hourly_throughput,
        ROUND(AVG(convolvedSchedFlights), 2) AS avg_hourly_flights,
        ROUND(regr_r2(tsaThroughput, contemporaneousSchedFlights), 4) AS r2_contemp,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead1), 4) AS r2_lead1,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead2), 4) AS r2_lead2,
        ROUND(regr_r2(tsaThroughput, schedFlights_lead3), 4) AS r2_lead3,
        ROUND(regr_r2(tsaThroughput, convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_slope(tsaThroughput, convolvedSchedFlights), 2) AS slope_convolved,
        ROUND(corr(tsaThroughput, convolvedSchedFlights), 4) AS corr_convolved
    FROM periods
    WHERE regime != 'Other'
    GROUP BY regime
    ORDER BY regime;
    """
    df_lead_lag = con.execute(lead_lag_sql).df()
    print(df_lead_lag.to_string(index=False))

    # 3. Monthly Granular Breakdown: Finding the Exact Breakdown and Recovery
    print("\n" + "="*80)
    print("3. MONTHLY TRAJECTORY OF RELATIONSHIP: COUPLING & DECOUPLING")
    print("="*80)
    monthly_sql = """
    SELECT 
        strftime(d.date, '%Y-%m') AS ym,
        d.year,
        d.month,
        SUM(tl.tsaThroughput) AS monthly_tsa,
        SUM(tl.convolvedSchedFlights) AS monthly_convolved_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_flight,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2_convolved,
        ROUND(regr_slope(tl.tsaThroughput, tl.convolvedSchedFlights), 2) AS slope_convolved,
        ROUND(AVG(tl.priorHourAvgDepDel), 2) AS avg_dep_del,
        ROUND(AVG(tl.priorHourDepDel15Rate) * 100, 2) AS depDel15_pct,
        SUM(tl.priorHourCancelledFlights) AS total_cancelled
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE d.year BETWEEN 2019 AND 2025
    GROUP BY strftime(d.date, '%Y-%m'), d.year, d.month
    ORDER BY ym;
    """
    df_monthly = con.execute(monthly_sql).df()
    
    # Calculate recovery ratio relative to 2019 same-month baseline
    base_2019 = df_monthly[df_monthly['year'] == 2019].set_index('month')['monthly_tsa'].to_dict()
    df_monthly['tsa_pct_of_2019'] = df_monthly.apply(
        lambda r: round(r['monthly_tsa'] / base_2019[r['month']] * 100, 2) if r['month'] in base_2019 else np.nan, axis=1
    )
    print(df_monthly[['ym', 'monthly_tsa', 'tsa_pct_of_2019', 'pax_per_flight', 'r2_convolved', 'slope_convolved', 'depDel15_pct', 'total_cancelled']].to_string(index=False))

    # 4. March 2020 Shock Timeline (Daily Granularity)
    print("\n" + "="*80)
    print("4. MARCH 2020 COLLAPSE: DAILY BREAKPOINT ANALYSIS")
    print("="*80)
    shock_sql = """
    SELECT 
        d.date,
        d.dayOfWeek,
        SUM(tl.tsaThroughput) AS daily_tsa,
        SUM(tl.contemporaneousSchedFlights) AS daily_sched_flights,
        ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.contemporaneousSchedFlights), 0), 2) AS pax_per_flight,
        ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS daily_r2,
        SUM(tl.priorHourCancelledFlights) AS daily_cancelled_flights
    FROM vw_airport_hourly_demand tl
    JOIN dim_date d ON tl.dateId = d.dateId
    WHERE d.date BETWEEN '2020-03-01' AND '2020-04-15'
    GROUP BY d.date, d.dayOfWeek
    ORDER BY d.date;
    """
    df_shock = con.execute(shock_sql).df()
    print(df_shock.to_string(index=False))

    # 5. Diurnal and Day-of-Week Structural Profile Comparison
    print("\n" + "="*80)
    print("5. DIURNAL PROFILE STABILITY ACROSS REGIMES")
    print("="*80)
    diurnal_sql = """
    WITH hourly_regimes AS (
        SELECT 
            hour,
            CASE 
                WHEN dateId BETWEEN 20190101 AND 20191231 THEN '2019_Baseline'
                WHEN dateId BETWEEN 20200401 AND 20201231 THEN '2020_Lockdown'
                WHEN dateId BETWEEN 20210101 AND 20211231 THEN '2021_Rebound'
                WHEN dateId BETWEEN 20220501 AND 20221231 THEN '2022_PostMask'
                WHEN dateId BETWEEN 20230101 AND 20231231 THEN '2023_MaturePost'
                WHEN dateId BETWEEN 20240101 AND 20241231 THEN '2024_Post'
                WHEN dateId BETWEEN 20250101 AND 20251231 THEN '2025_Post'
            END AS period,
            SUM(tsaThroughput) AS total_throughput
        FROM vw_airport_hourly_demand
        WHERE dateId <= 20251231
        GROUP BY hour, 2
    ),
    totals AS (
        SELECT period, SUM(total_throughput) AS period_sum
        FROM hourly_regimes
        WHERE period IS NOT NULL
        GROUP BY period
    )
    SELECT 
        hr.hour,
        hr.period,
        ROUND(hr.total_throughput * 100.0 / t.period_sum, 3) AS pct_of_daily_volume
    FROM hourly_regimes hr
    JOIN totals t ON hr.period = t.period
    WHERE hr.period IS NOT NULL
    ORDER BY hr.hour, hr.period;
    """
    df_diurnal = con.execute(diurnal_sql).df()
    pivot_diurnal = df_diurnal.pivot(index='hour', columns='period', values='pct_of_daily_volume')
    print("Diurnal Hourly Proportions (% of daily volume):")
    print(pivot_diurnal.to_string())

    # Check correlation of hourly profiles with 2019 baseline
    print("\nCorrelation of Diurnal Hourly Distribution with 2019 Baseline:")
    diurnal_corr = pivot_diurnal.corr()['2019_Baseline']
    print(diurnal_corr)

    # 6. Day of Week Profile Comparison
    print("\n" + "="*80)
    print("6. DAY OF WEEK DISTRIBUTION (% of weekly volume)")
    print("="*80)
    dow_sql = """
    WITH dow_regimes AS (
        SELECT 
            dayOfWeek,
            CASE 
                WHEN dateId BETWEEN 20190101 AND 20191231 THEN '2019_Baseline'
                WHEN dateId BETWEEN 20200401 AND 20201231 THEN '2020_Lockdown'
                WHEN dateId BETWEEN 20210101 AND 20211231 THEN '2021_Rebound'
                WHEN dateId BETWEEN 20220501 AND 20221231 THEN '2022_PostMask'
                WHEN dateId BETWEEN 20230101 AND 20231231 THEN '2023_MaturePost'
                WHEN dateId BETWEEN 20240101 AND 20241231 THEN '2024_Post'
                WHEN dateId BETWEEN 20250101 AND 20251231 THEN '2025_Post'
            END AS period,
            SUM(tsaThroughput) AS total_throughput
        FROM vw_airport_hourly_demand
        WHERE dateId <= 20251231
        GROUP BY dayOfWeek, 2
    ),
    totals AS (
        SELECT period, SUM(total_throughput) AS period_sum
        FROM dow_regimes
        WHERE period IS NOT NULL
        GROUP BY period
    )
    SELECT 
        dr.dayOfWeek,
        dr.period,
        ROUND(dr.total_throughput * 100.0 / t.period_sum, 2) AS pct_of_week
    FROM dow_regimes dr
    JOIN totals t ON dr.period = t.period
    WHERE dr.period IS NOT NULL
    ORDER BY dr.dayOfWeek, dr.period;
    """
    df_dow = con.execute(dow_sql).df()
    pivot_dow = df_dow.pivot(index='dayOfWeek', columns='period', values='pct_of_week')
    print(pivot_dow.to_string())

    # 7. Airport Heterogeneity: When did different airport categories recover?
    print("\n" + "="*80)
    print("7. AIRPORT HETEROGENEITY: RECOVERY BY HUB CLASSIFICATION & ARCHETYPE")
    print("="*80)
    apt_sql = """
    WITH apt_annual AS (
        SELECT 
            apt.airportCode,
            apt.faaHubCategory,
            d.year,
            SUM(tl.tsaThroughput) AS total_tsa,
            SUM(tl.convolvedSchedFlights) AS total_flights,
            ROUND(SUM(tl.tsaThroughput) / NULLIF(SUM(tl.convolvedSchedFlights), 0), 2) AS pax_per_flight,
            ROUND(regr_r2(tl.tsaThroughput, tl.convolvedSchedFlights), 4) AS r2
        FROM vw_airport_hourly_demand tl
        JOIN dim_airport apt ON tl.airportId = apt.airportId
        JOIN dim_date d ON tl.dateId = d.dateId
        WHERE d.year IN (2019, 2020, 2021, 2022, 2023, 2024, 2025)
        GROUP BY apt.airportCode, apt.faaHubCategory, d.year
    )
    SELECT * FROM apt_annual
    ORDER BY airportCode, year;
    """
    df_apt = con.execute(apt_sql).df()
    # Compute recovery vs 2019 for each airport
    base_apt_2019 = df_apt[df_apt['year'] == 2019].set_index('airportCode')['total_tsa'].to_dict()
    df_apt['recovery_vs_2019'] = df_apt.apply(
        lambda r: round(r['total_tsa'] / base_apt_2019.get(r['airportCode'], 1) * 100, 2), axis=1
    )
    pivot_apt_rec = df_apt.pivot(index='airportCode', columns='year', values='recovery_vs_2019')
    print("Airport Volume Recovery vs 2019 (%):")
    print(pivot_apt_rec.to_string())

    # 8. Statistical Chow Test / Structural Break Test
    print("\n" + "="*80)
    print("8. ECONOMETRIC CHOW TEST FOR STRUCTURAL BREAK")
    print("="*80)
    # Let's run OLS regression TSA = b0 + b1 * convolved_flights
    # Compare:
    # 1) Pre-Pandemic (2019) vs Pandemic (2020-03 to 2022-04)
    # 2) Pre-Pandemic (2019) vs Post-Pandemic (2023 to 2025)
    # 3) Pre-Pandemic (2019) vs Post-Pandemic (2022-05 to 2022-12)
    chow_query = """
    SELECT 
        tsaThroughput,
        convolvedSchedFlights,
        CASE 
            WHEN dateId BETWEEN 20190101 AND 20191231 THEN 'pre_2019'
            WHEN dateId BETWEEN 20200315 AND 20220430 THEN 'pandemic'
            WHEN dateId BETWEEN 20220501 AND 20221231 THEN 'post_2022'
            WHEN dateId BETWEEN 20230101 AND 20251231 THEN 'post_2023_2025'
            ELSE 'other'
        END AS regime
    FROM vw_airport_hourly_demand
    WHERE dateId <= 20251231;
    """
    df_reg = con.execute(chow_query).df()
    
    def run_chow_test(df1, df2, name1, name2):
        # Combined
        df_c = pd.concat([df1, df2])
        
        # OLS on df1
        X1 = np.column_stack([np.ones(len(df1)), df1['convolvedSchedFlights']])
        y1 = df1['tsaThroughput'].values
        b1, rss1, _, _ = np.linalg.lstsq(X1, y1, rcond=None)
        residuals1 = y1 - X1 @ b1
        rss1 = np.sum(residuals1 ** 2)
        
        # OLS on df2
        X2 = np.column_stack([np.ones(len(df2)), df2['convolvedSchedFlights']])
        y2 = df2['tsaThroughput'].values
        b2, rss2, _, _ = np.linalg.lstsq(X2, y2, rcond=None)
        residuals2 = y2 - X2 @ b2
        rss2 = np.sum(residuals2 ** 2)
        
        # OLS on pooled
        Xc = np.column_stack([np.ones(len(df_c)), df_c['convolvedSchedFlights']])
        yc = df_c['tsaThroughput'].values
        bc, rssc, _, _ = np.linalg.lstsq(Xc, yc, rcond=None)
        residualsc = yc - Xc @ bc
        rssc = np.sum(residualsc ** 2)
        
        k = 2 # number of parameters (intercept + slope)
        N1 = len(df1)
        N2 = len(df2)
        
        f_stat = ((rssc - (rss1 + rss2)) / k) / ((rss1 + rss2) / (N1 + N2 - 2 * k))
        
        print(f"\nChow Test: [{name1}] vs [{name2}]")
        print(f"  {name1}: N={N1:,}, Intercept={b1[0]:.2f}, Slope={b1[1]:.2f}, RSS={rss1:,.0f}")
        print(f"  {name2}: N={N2:,}, Intercept={b2[0]:.2f}, Slope={b2[1]:.2f}, RSS={rss2:,.0f}")
        print(f"  Pooled:   N={len(df_c):,}, Intercept={bc[0]:.2f}, Slope={bc[1]:.2f}, RSS={rssc:,.0f}")
        print(f"  F-Statistic: {f_stat:.2f} (df1={k}, df2={N1+N2-2*k:,})")
        return f_stat, b1, b2

    df_pre = df_reg[df_reg['regime'] == 'pre_2019']
    df_pan = df_reg[df_reg['regime'] == 'pandemic']
    df_post22 = df_reg[df_reg['regime'] == 'post_2022']
    df_post23 = df_reg[df_reg['regime'] == 'post_2023_2025']
    
    run_chow_test(df_pre, df_pan, "Pre-Pandemic (2019)", "Pandemic Disruption (2020-03 to 2022-04)")
    run_chow_test(df_pre, df_post22, "Pre-Pandemic (2019)", "Post-Pandemic (May-Dec 2022)")
    run_chow_test(df_pre, df_post23, "Pre-Pandemic (2019)", "Post-Pandemic (2023-2025)")
    run_chow_test(df_post22, df_post23, "Post-Pandemic 2022", "Post-Pandemic 2023-2025")

    con.close()
    print("\n" + "="*80)
    print("ANALYSIS COMPLETE.")
    print("="*80)

if __name__ == '__main__':
    run_in_depth_analysis()
