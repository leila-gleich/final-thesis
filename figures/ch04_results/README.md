# Chapter IV: Results & Findings Figures & Datasets
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Publication-ready empirical visualizations, out-of-time benchmark results, and companion datasets for **Chapter IV (*Results & Findings*)**.

---

### Empirical Figures & Associated Conformed Data Tables

| Figure ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Manuscript Target Location | Operational Function & Empirical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 4.2** | `01_annual_volatility_tsa_otp_clustering.png` / `figure_4_2_annual_volatility_clusters.png` | `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv` | Following Table 4.3b | **Annual Volatility Dynamics & Coupled Volatility Clusters**: Network-level annual volatility regimes across the Top 25 airfields, showing the positive coupling between flight delay dispersion and checkpoint arrival volatility ($CVI = \sigma_{\text{TSA}} \cdot \sigma_{\text{Delay}}$). |
| **Figure 4.3** | `02_day_of_week_volatility_dynamics.png` / `figure_4_3_day_of_week_volatility_dynamics.png` | `table_4_4a_master_day_of_week_operational_volatility_regimes.csv` | Following Table 4.4a | **Day-of-Week Volatility Dynamics Across the National Network**: Illustrates day-of-week arrival burstiness ($CV_{\text{TSA}}$) across corporate-heavy (Mon/Thu/Fri peaks) vs. leisure-heavy (Sun/Fri peaks) commercial airfields. |
| **Figure 4.4** | `03_diurnal_hourly_volatility_clusters_by_dow.png` / `figure_4_4_diurnal_hourly_volatility_clusters.png` | `table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv` | Under Section `TSA and OTP Throughput Data` | **Intraday Diurnal Hourly Volatility Clusters (Bimodal Peaks by DOW)**: Resolves 24-hour diurnal passenger arrival profiles, highlighting morning (05:00–08:00) and afternoon/evening (16:00–19:00) peak shock windows. |
| **Figure 4.5** | `figure_4_5_lead_lag_convolution_curves.png` / `physical transfer lead lag time.png` | `table_4_9_empirical_lead_lag_transfer_dynamics.csv` | Directly following Table 4.9 | **Empirical Lead-Lag Passenger Show-Up Curve Convolution**: Depicts the temporal asynchrony between scheduled departure flight banks and landside checkpoint arrivals, highlighting modal 90–120 minute show-up ($t+1, t+2$). |
| **Figure 4.6** | `figure_4_6_master_model_benchmark_matrix.png` | `table_4_10_master_model_benchmark_matrix.csv` | Following Table 4.10 | **Master Model Benchmark Matrix for Throughput Volatility**: Multi-metric out-of-time benchmark (Test $R^2$, Test RMSE, Test MASE, Forecast Bias) comparing Baseline Control, Model 1 (Deterministic), Model 2 (Machine Learning), and Model 3 (Dynamic Hybrid) across 72,053 complex hours. |
| **Diagnostic** | `04_sample_sufficiency_distribution.png` / `figure_sample_sufficiency_distribution.png` | `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv` | Within Section `### Temporal Boundaries` | **Sample Sufficiency Distribution**: Validates statistical sample size and temporal coverage across the post-pandemic demarcation window (May 1, 2022 to December 31, 2025; $N = 3,222$ holdout complex-days). |
