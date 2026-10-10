"""
perform_top9_analysis.py
------------------------
Executes all descriptive, cluster-level, post-pandemic, and econometric OTP-TSA 
coupling analyses on the 9-Airport Experimental Cohort (BOS, DFW, DTW, EWR, IAH, 
LAX, LGA, ORD, PHL), matching the analytical methodology applied to the Top 25 airfields.

Saves compiled results to:
  results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx
"""

import os
import sys
import numpy as np
import pandas as pd
from scipy import stats

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RESULTS_DIR = os.path.join(BASE_DIR, "results", "02_4tier_filtering")
TOP25_EXCEL = os.path.join(BASE_DIR, "results", "01_top25_clustering", "01_top25_clustering.xlsx")
SEASON_EXCEL = os.path.join(BASE_DIR, "results", "01_top25_clustering", "seasonality_and_regimes", "top25_seasonality_regimes_and_events.xlsx")
DAILY_CSV = os.path.join(BASE_DIR, "data", "curated", "daily_aggregated_data.csv")
HOURLY_CSV = os.path.join(BASE_DIR, "data", "curated", "hourly_aggregated_data.csv")

OUTPUT_EXCEL = os.path.join(RESULTS_DIR, "02_top9_cohort_comprehensive_analysis.xlsx")

TOP9_AIRPORTS = ["BOS", "DFW", "DTW", "EWR", "IAH", "LAX", "LGA", "ORD", "PHL"]

CLUSTER_NAMES = {
    0: "Cluster 0: Mega-Connecting Gateways",
    1: "Cluster 1: High-Density O&D Focus",
    2: "Cluster 2: High-Reliability Fortress Hubs",
    3: "Cluster 3: Congested Coastal Originators"
}

def run_top9_comprehensive_analysis():
    print("=" * 80)
    print("PERFORMING COMPREHENSIVE ANALYSIS ON THE 9-AIRPORT EXPERIMENTAL COHORT")
    print("Airports: BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL")
    print("=" * 80)

    # 1. Load Top 25 Master Data and filter Top 9
    print("\n[Step 1] Loading Top 25 Census and filtering 9-Airport Cohort...")
    df_top25 = pd.read_excel(TOP25_EXCEL, sheet_name="01_Executive_Top25_Airport_Coup")
    df_top9 = df_top25[df_top25["airport_code"].isin(TOP9_AIRPORTS)].copy()
    
    # Map cluster ID
    cluster_mapping = {
        'Mega Connecting Hub (Very high passenger volumes with heavy connecting flight transfers)': 0,
        'High Local Demand Airport (Most passengers start locally and pass through TSA security)': 1,
        'High-Reliability Fortress Hub (Major airline fortress with smooth operations and low delays)': 2,
        'Congested Coastal Airport (Restricted airspace, smaller regional planes, and chronic flight delays)': 3
    }
    df_top25["cluster_id"] = df_top25["operational_archetype"].map(cluster_mapping)
    df_top9["cluster_id"] = df_top9["operational_archetype"].map(cluster_mapping)

    # 2. Cohort Macro Summary Descriptive Statistics
    print("\n[Step 2] Computing Macro Summary Descriptive Statistics (Top 9 vs Top 25)...")
    core_metrics = [
        ("scheduled_flights", "Scheduled Commercial Flights", "flights"),
        ("cancelled_flights", "Cancelled Flights", "flights"),
        ("cancellation_rate_pct", "Flight Cancellation Rate", "percent"),
        ("avg_dep_delay_minutes", "Average Departure Delay", "minutes"),
        ("flights_delayed_15min_pct", "Flights Delayed 15+ Minutes Rate", "percent"),
        ("avg_taxi_out_minutes", "Runway Taxi-Out Queue Time", "minutes"),
        ("total_tsa_passengers", "Total TSA Passenger Throughput", "passengers"),
        ("avg_daily_tsa_passengers", "Average Daily TSA Passenger Count", "passengers/day"),
        ("avg_hourly_tsa_passengers", "Average Hourly TSA Passenger Count", "pax/hour"),
        ("peak_single_hour_tsa_rush", "Peak Single-Hour TSA Rush", "pax/hour"),
        ("connecting_passenger_share_pct", "Connecting Passenger Share", "percent"),
        ("local_originating_share_pct", "Local Originating Passenger Share", "percent"),
        ("true_local_originating_tsa_demand", "True Local Originating TSA Demand", "passengers"),
        ("aircraft_gauge_seats", "Airplane Passenger Capacity (Gauge)", "seats/flight"),
        ("route_load_factor_pct", "Flight Fullness (Load Factor)", "percent"),
        ("otp_departure_delay_volatility_cv", "OTP Departure Delay Volatility (CV)", "ratio"),
        ("otp_cancellation_volatility_cv", "OTP Cancellation Volatility (CV)", "ratio"),
        ("tsa_daily_throughput_volatility_cv", "TSA Daily Throughput Volatility (CV)", "ratio"),
        ("tsa_hourly_throughput_volatility_cv", "TSA Hourly Throughput Volatility (CV)", "ratio"),
        ("tsa_peak_to_median_surge_ratio", "TSA Peak-to-Median Surge Ratio", "ratio")
    ]

    macro_rows = []
    for col, name, unit in core_metrics:
        s9 = df_top9[col]
        s25 = df_top25[col]
        macro_rows.append({
            "metric_name": name,
            "unit": unit,
            "top9_mean": s9.mean(),
            "top9_std": s9.std(),
            "top9_median": s9.median(),
            "top9_min": s9.min(),
            "top9_min_airport": df_top9.loc[s9.idxmin(), "airport_code"],
            "top9_max": s9.max(),
            "top9_max_airport": df_top9.loc[s9.idxmax(), "airport_code"],
            "top25_mean": s25.mean(),
            "top25_std": s25.std(),
            "top25_median": s25.median(),
            "mean_delta_pct": ((s9.mean() - s25.mean()) / s25.mean()) * 100.0
        })
    df_macro_summary = pd.DataFrame(macro_rows)

    # 3. Cluster-Level In-Depth Descriptive Statistics
    print("\n[Step 3] Computing Cluster-Level Descriptive Statistics for each Archetype...")
    cluster_metrics = [
        "scheduled_flights", "cancelled_flights", "cancellation_rate_pct",
        "avg_dep_delay_minutes", "flights_delayed_15min_pct", "avg_taxi_out_minutes",
        "total_tsa_passengers", "connecting_passenger_share_pct", "local_originating_share_pct",
        "true_local_originating_tsa_demand", "aircraft_gauge_seats", "route_load_factor_pct",
        "otp_departure_delay_volatility_cv", "otp_cancellation_volatility_cv",
        "tsa_daily_throughput_volatility_cv", "tsa_hourly_throughput_volatility_cv",
        "tsa_peak_to_median_surge_ratio"
    ]

    cluster_profiles = []
    for cid in range(4):
        sub9 = df_top9[df_top9["cluster_id"] == cid]
        sub25 = df_top25[df_top25["cluster_id"] == cid]
        members9 = ", ".join(sorted(sub9["airport_code"].tolist()))
        members25 = ", ".join(sorted(sub25["airport_code"].tolist()))
        
        prof = {
            "cluster_id": cid,
            "cluster_name": CLUSTER_NAMES[cid],
            "top9_airports_count": len(sub9),
            "top9_members": members9,
            "top25_airports_count": len(sub25),
            "top25_members": members25
        }
        for cm in cluster_metrics:
            prof[f"{cm}_top9_mean"] = sub9[cm].mean()
            prof[f"{cm}_top9_median"] = sub9[cm].median()
            prof[f"{cm}_top9_std"] = sub9[cm].std()
            prof[f"{cm}_top25_mean"] = sub25[cm].mean()
            prof[f"{cm}_delta_pct"] = ((sub9[cm].mean() - sub25[cm].mean()) / sub25[cm].mean()) * 100.0 if sub25[cm].mean() != 0 else 0
        cluster_profiles.append(prof)
    df_cluster_profiles = pd.DataFrame(cluster_profiles)

    # 4. Econometric & Cross-Dataset Correlation Matrix (Top 9 vs Top 25)
    print("\n[Step 4] Computing Econometric & Cross-Dataset Correlation Matrix...")
    rel_pairs = [
        ("scheduled_flights", "total_tsa_passengers", "Scheduled Flights vs Total TSA Passengers", "Raw Scheduled Volume Coupling"),
        ("scheduled_flights", "true_local_originating_tsa_demand", "Scheduled Flights vs True Local Demand", "Connecting-Adjusted Demand Coupling"),
        ("connecting_passenger_share_pct", "scheduled_flights", "Connecting Share (%) vs Scheduled Flights", "Hub Scale-Connecting Ratio Coupling"),
        ("avg_taxi_out_minutes", "total_tsa_passengers", "Taxi-Out Minutes vs Total TSA Passengers", "Surface Congestion Scale Coupling"),
        ("avg_dep_delay_minutes", "avg_taxi_out_minutes", "Departure Delay vs Taxi-Out Minutes", "Tarmac Queue Delay Feedback"),
        ("flights_delayed_15min_pct", "total_tsa_passengers", "DepDel15 (%) vs Total TSA Passengers", "Schedule Delay Rate vs Passenger Volume"),
        ("tsa_hourly_throughput_volatility_cv", "otp_departure_delay_volatility_cv", "Hourly TSA CV vs Dep Delay CV", "Hourly Throughput Volatility Transmission"),
        ("tsa_daily_throughput_volatility_cv", "otp_departure_delay_volatility_cv", "Daily TSA CV vs Dep Delay CV", "Daily Checkpoint Volatility Coupling"),
        ("tsa_peak_to_median_surge_ratio", "otp_departure_delay_volatility_cv", "Peak/Median Surge vs Dep Delay CV", "Surge Ratio vs Delay Volatility"),
        ("tsa_daily_throughput_volatility_cv", "cancellation_rate_pct", "Daily TSA CV vs Cancellation Rate (%)", "Passenger Volatility vs Cancellation Exposure"),
        ("avg_dep_delay_minutes", "cancellation_rate_pct", "Departure Delay vs Cancellation Rate (%)", "Delay-Cancellation Confounding Coupling")
    ]

    stat_rows = []
    for m1, m2, label, cat in rel_pairs:
        r9, p9 = stats.pearsonr(df_top9[m1], df_top9[m2])
        r25, p25 = stats.pearsonr(df_top25[m1], df_top25[m2])
        
        # Regression slope for top 9
        slope, intercept, _, _, _ = stats.linregress(df_top9[m1], df_top9[m2])
        
        stat_rows.append({
            "relationship_category": cat,
            "metric_1": m1,
            "metric_2": m2,
            "relationship_label": label,
            "top9_pearson_r": r9,
            "top9_r_squared_pct": (r9**2) * 100.0,
            "top9_p_value": p9,
            "top9_regression_slope": slope,
            "top9_regression_intercept": intercept,
            "top25_pearson_r": r25,
            "top25_r_squared_pct": (r25**2) * 100.0,
            "top25_p_value": p25
        })
    df_stat_relationships = pd.DataFrame(stat_rows)

    # 5. Post-Pandemic Behavioral Analysis (2019-2025)
    print("\n[Step 5] Analyzing 7-Year Post-Pandemic Progression and Regime Shifts...")
    df_daily = pd.read_csv(DAILY_CSV)
    df_daily["Date"] = pd.to_datetime(df_daily["Date"])
    df_daily["Year"] = df_daily["Date"].dt.year
    df_daily_9 = df_daily[df_daily["Airport"].isin(TOP9_AIRPORTS)].copy()

    annual_grouped = df_daily_9.groupby(["Airport", "Year"]).agg(
        tsa_throughput=("TSA_Throughput", "sum"),
        scheduled_departures=("Scheduled_Departures", "sum"),
        actual_departures=("Actual_Departures", "sum")
    ).reset_index()

    pivot_tsa = annual_grouped.pivot(index="Airport", columns="Year", values="tsa_throughput")
    pivot_sched = annual_grouped.pivot(index="Airport", columns="Year", values="scheduled_departures")

    tsa_recovery_pct = pivot_tsa.div(pivot_tsa[2019], axis=0) * 100.0
    sched_recovery_pct = pivot_sched.div(pivot_sched[2019], axis=0) * 100.0

    # Regime Correlation Analysis
    regimes = {
        "Pre-Pandemic (2019)": df_daily_9["Date"] < "2020-01-01",
        "Acute Pandemic (2020-2021)": (df_daily_9["Date"] >= "2020-01-01") & (df_daily_9["Date"] < "2022-01-01"),
        "Early Post-Mask Mandate (May 2022 - Dec 2025)": (df_daily_9["Date"] >= "2022-05-01") & (df_daily_9["Date"] <= "2025-12-31"),
        "Mature Post-Pandemic (2023 - 2025)": (df_daily_9["Date"] >= "2023-01-01") & (df_daily_9["Date"] <= "2025-12-31")
    }

    regime_results = []
    for rname, rmask in regimes.items():
        sub = df_daily_9[rmask].dropna(subset=["Scheduled_Departures", "TSA_Throughput"])
        r, p = stats.pearsonr(sub["Scheduled_Departures"], sub["TSA_Throughput"])
        regime_results.append({
            "temporal_regime": rname,
            "observations_days": len(sub),
            "pearson_r": r,
            "r_squared_pct": (r**2) * 100.0,
            "p_value": p,
            "mean_daily_tsa": sub["TSA_Throughput"].mean(),
            "mean_daily_sched": sub["Scheduled_Departures"].mean()
        })
    df_regime_coupling = pd.DataFrame(regime_results)

    # 6. Hourly Lead-Lag Arrival Deconvolution & Transfer Function
    print("\n[Step 6] Computing Hourly Lead-Lag Arrival Transfer Function...")
    df_hourly = pd.read_csv(HOURLY_CSV)
    df_hourly["DateTime"] = pd.to_datetime(df_hourly["Date"]) + pd.to_timedelta(df_hourly["Hour"], unit="h")
    df_hourly = df_hourly.sort_values(["Airport", "DateTime"]).reset_index(drop=True)
    df_hourly_post = df_hourly[(df_hourly["Airport"].isin(TOP9_AIRPORTS)) & (df_hourly["Date"] >= "2022-05-01")].copy()

    df_hourly_post["sched_lag1"] = df_hourly_post.groupby("Airport")["Scheduled_Departures"].shift(1)
    df_hourly_post["sched_t"] = df_hourly_post["Scheduled_Departures"]
    df_hourly_post["sched_lead1"] = df_hourly_post.groupby("Airport")["Scheduled_Departures"].shift(-1)
    df_hourly_post["sched_lead2"] = df_hourly_post.groupby("Airport")["Scheduled_Departures"].shift(-2)
    df_hourly_post["sched_lead3"] = df_hourly_post.groupby("Airport")["Scheduled_Departures"].shift(-3)

    lead_horizons = [
        ("sched_lag1", "Lag t-1 (1 Hr Post-Departure)"),
        ("sched_t", "Contemporaneous t (Flight Departure Hour)"),
        ("sched_lead1", "Lead t+1 (1 Hr Pre-Departure Horizon)"),
        ("sched_lead2", "Lead t+2 (2 Hr Pre-Departure Modal Horizon)"),
        ("sched_lead3", "Lead t+3 (3 Hr Pre-Departure Horizon)")
    ]

    lead_lag_rows = []
    for col, desc in lead_horizons:
        sub = df_hourly_post.dropna(subset=["TSA_Throughput", col])
        r, p = stats.pearsonr(sub[col], sub["TSA_Throughput"])
        slope, intercept, _, _, _ = stats.linregress(sub[col], sub["TSA_Throughput"])
        lead_lag_rows.append({
            "horizon": desc,
            "pearson_r": r,
            "r_squared_pct": (r**2) * 100.0,
            "p_value": p,
            "regression_slope_pax_per_flight": slope,
            "intercept": intercept
        })
    df_lead_lag = pd.DataFrame(lead_lag_rows)

    # 7. Write Comprehensive Excel Workbook
    print(f"\n[Step 7] Writing comprehensive results to {OUTPUT_EXCEL}...")
    with pd.ExcelWriter(OUTPUT_EXCEL, engine="openpyxl") as writer:
        df_top9.to_excel(writer, sheet_name="Top9_Master_Census", index=False)
        df_macro_summary.to_excel(writer, sheet_name="Top9_Macro_Summary_vs_Top25", index=False)
        df_cluster_profiles.to_excel(writer, sheet_name="Top9_Cluster_Archetypes", index=False)
        df_stat_relationships.to_excel(writer, sheet_name="Top9_Econometric_Relationships", index=False)
        pivot_tsa.to_excel(writer, sheet_name="TSA_Annual_Throughput")
        tsa_recovery_pct.to_excel(writer, sheet_name="TSA_Recovery_Pct_2019_Base")
        pivot_sched.to_excel(writer, sheet_name="Sched_Departures_Annual")
        sched_recovery_pct.to_excel(writer, sheet_name="Sched_Recovery_Pct_2019_Base")
        df_regime_coupling.to_excel(writer, sheet_name="Temporal_Regime_Coupling", index=False)
        df_lead_lag.to_excel(writer, sheet_name="Hourly_Lead_Lag_Transfer", index=False)

    print("\nSUCCESS: All analyses on Top 9 airports completed successfully!")
    print(f"Results saved in: {OUTPUT_EXCEL}")

if __name__ == "__main__":
    run_top9_comprehensive_analysis()
