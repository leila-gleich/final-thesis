# Master Manuscript Tables Registry (Conformed CSV Suite)

This directory contains conformed, publication-grade CSV spreadsheets for **every empirical table in the thesis manuscripts** (`thesis_docs/manuscripts/chp4-results.md` and `thesis_docs/manuscripts/chp5-discussion.md`).

This registry ensures complete transparency, auditability, and mathematical reproducibility across the three thesis evaluation dimensions (**Robustness**, **Resilience**, and **Generalizability**).

---

## Automated Synchronization Procedure

> [!IMPORTANT]
> Every time the underlying analysis, ETL pipelines, or model parameters are updated, run:
> ```bash
> python src/analysis/sync_manuscript_tables.py
> ```
> or execute the master end-to-end pipeline:
> ```bash
> python run_pipeline.py
> ```
> This automatically extracts all tables from the manuscript Markdown drafts, sanitizes LaTeX symbols, generates conformed CSV files, and updates the companion multi-tab Excel workbooks in `results/`.

---

## Master Manuscript Table Catalog

| Table ID | Table Title / Scope | Canonical CSV File | Short Link | Dimensions | Manuscript Chapter | Companion Excel Workbook |
| :--- | :--- | :--- | :---: | :---: | :--- | :--- |
| **Table 4.1** | Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network) | [`table_4_1_master_post_etl_multi_source_data_foundation_census.csv`](table_4_1_master_post_etl_multi_source_data_foundation_census.csv) | [`table_4_1.csv`](table_4_1.csv) | 5 rows x 6 cols | `chp4-results.md` | [`01_top25_clustering.xlsx`](../01_top25_clustering/01_top25_clustering.xlsx) |
| **Table 4.2** | Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse) | [`table_4_2_post_etl_master_summary_descriptive_statistics.csv`](table_4_2_post_etl_master_summary_descriptive_statistics.csv) | [`table_4_2.csv`](table_4_2.csv) | 11 rows x 11 cols | `chp4-results.md` | [`01_top25_clustering.xlsx`](../01_top25_clustering/01_top25_clustering.xlsx) |
| **Table 4.3a** | Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network | [`table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv`](table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv) | [`table_4_3a.csv`](table_4_3a.csv) | 8 rows x 3 cols | `chp4-results.md` | [`top25_seasonality_regimes_and_events.xlsx`](../seasonality_and_regimes/top25_seasonality_regimes_and_events.xlsx) |
| **Table 4.3b** | Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields) | [`table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`](table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv) | [`table_4_3b.csv`](table_4_3b.csv) | 4 rows x 11 cols | `chp4-results.md` | [`season-analysis.xlsx`](../seasonality_and_regimes/season-analysis.xlsx) |
| **Table 4.4a** | Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields) | [`table_4_4a_day_of_week_volatility_dynamics_and_operational_archetypes.csv`](table_4_4a_day_of_week_volatility_dynamics_and_operational_archetypes.csv) | [`table_4_4a.csv`](table_4_4a.csv) | 7 rows x 10 cols | `chp4-results.md` | [`season-analysis.xlsx`](../seasonality_and_regimes/season-analysis.xlsx) |
| **Table 4.5** | Master Cross-Dataset Econometric Relationships (Top 25 Airfields) | [`table_4_5_master_cross_dataset_econometric_relationships.csv`](table_4_5_master_cross_dataset_econometric_relationships.csv) | [`table_4_5.csv`](table_4_5.csv) | 12 rows x 9 cols | `chp4-results.md` | [`01_top25_clustering.xlsx`](../01_top25_clustering/01_top25_clustering.xlsx) |
| **Table 4.6** | The Nine-Airport Experimental Cohort Factorial Specification | [`table_4_6_nine_airport_experimental_cohort_factorial_specification.csv`](table_4_6_nine_airport_experimental_cohort_factorial_specification.csv) | [`table_4_6.csv`](table_4_6.csv) | 9 rows x 7 cols | `chp4-results.md` | [`02_4tier_filtering.xlsx`](../02_4tier_filtering/02_4tier_filtering.xlsx) |
| **Table 4.7** | Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe | [`table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`](table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv) | [`table_4_7.csv`](table_4_7.csv) | 16 rows x 10 cols | `chp4-results.md` | [`02_4tier_filtering.xlsx`](../02_4tier_filtering/02_4tier_filtering.xlsx) |
| **Table 4.8** | Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports | [`table_4_8_day_of_week_mean_daily_passenger_throughput_nine_airports.csv`](table_4_8_day_of_week_mean_daily_passenger_throughput_nine_airports.csv) | [`table_4_8.csv`](table_4_8.csv) | 9 rows x 12 cols | `chp4-results.md` | [`02_top9_cohort_comprehensive_analysis.xlsx`](../02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx) |
| **Table 4.9** | Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand) | [`table_4_9_empirical_lead_lag_transfer_dynamics.csv`](table_4_9_empirical_lead_lag_transfer_dynamics.csv) | [`table_4_9.csv`](table_4_9.csv) | 7 rows x 5 cols | `chp4-results.md` | [`03_lead_lag_deconvolution.xlsx`](../03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx) |
| **Table 4.10** | Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout) | [`table_4_10_master_model_benchmark_matrix.csv`](table_4_10_master_model_benchmark_matrix.csv) | [`table_4_10.csv`](table_4_10.csv) | 4 rows x 10 cols | `chp4-results.md` | [`04_model_execution_2025_holdout.xlsx`](../04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx) |
| **Table 4.11** | Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Canonical Models (Throughput Volatility) | [`table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`](table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv) | [`table_4_11.csv`](table_4_11.csv) | 11 rows x 9 cols | `chp4-results.md` | [`05_robustness_resilience_generalizability.xlsx`](../05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx) |
| **Table 5.1** | Evaluation Dimension 1: Routine Operational Accuracy Across the Four Canonical Models | [`table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv`](table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv) | [`table_5_1.csv`](table_5_1.csv) | 4 rows x 7 cols | `chp5-discussion.md` | [`05_robustness_resilience_generalizability.xlsx`](../05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx) |
| **Table 5.2** | Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption | [`table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv`](table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv) | [`table_5_2.csv`](table_5_2.csv) | 4 rows x 8 cols | `chp5-discussion.md` | [`05_robustness_resilience_generalizability.xlsx`](../05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx) |
| **Table 5.3** | Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance | [`table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv`](table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv) | [`table_5_3.csv`](table_5_3.csv) | 4 rows x 8 cols | `chp5-discussion.md` | [`05_robustness_resilience_generalizability.xlsx`](../05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx) |
| **Table 5.4** | Master Asymmetric Trade-Off Matrix Across the Four Canonical Models | [`table_5_4_master_asymmetric_trade_off_matrix.csv`](table_5_4_master_asymmetric_trade_off_matrix.csv) | [`table_5_4.csv`](table_5_4.csv) | 3 rows x 7 cols | `chp5-discussion.md` | [`05_robustness_resilience_generalizability.xlsx`](../05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx) |

---

## Detailed Table Specifications

### Chapter 4: Findings and Results

1. **Table 4.1: Master Post-ETL Multi-Source Data Foundation Census** (`table_4_1_master_post_etl_multi_source_data_foundation_census.csv`)
   - *Scope*: Census of all 4 conformed federal feeds (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B) covering 42,062,039 conformed records.
   - *Companion Workbook*: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Section_1A_Data_Foundation_Cens`).

2. **Table 4.2: Post-ETL Master Summary Descriptive Statistics** (`table_4_2_post_etl_master_summary_descriptive_statistics.csv`)
   - *Scope*: Master descriptive moments (mean, std dev, median, IQR, skewness, kurtosis) across all operational variables.
   - *Companion Workbook*: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Section_1B_Post_ETL_Master_Desc`).

3. **Table 4.3a: Post-Pandemic Temporal Demarcation Evaluation** (`table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv`)
   - *Scope*: Comparison of Candidate A (Mature Post-Pandemic) and Candidate B (Early Post-Mask Regime; Selected, 44 months).
   - *Companion Workbook*: `results/01_top25_clustering/seasonality_and_regimes/top25_seasonality_regimes_and_events.xlsx`.

4. **Table 4.3b: Master Annual Seasonal Volatility Regimes Summary** (`table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`)
   - *Scope*: Annual seasonal volatility regimes (Off-Peak, Mid-Peak, Peak, Holiday) across 1,341 post-demarcation days.
   - *Companion Workbook*: `results/01_top25_clustering/seasonality_and_regimes/season-analysis.xlsx` (Sheet: `seasonal_regimes_summary`).

5. **Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes** (`table_4_4a_day_of_week_volatility_dynamics_and_operational_archetypes.csv`)
   - *Scope*: Weekly cyclical dynamics and operational archetypes across Monday through Sunday.
   - *Companion Workbook*: `results/01_top25_clustering/seasonality_and_regimes/season-analysis.xlsx` (Sheet: `day_of_week_regimes_summary`).

6. **Table 4.5: Master Cross-Dataset Econometric Relationships** (`table_4_5_master_cross_dataset_econometric_relationships.csv`)
   - *Scope*: Econometric coupling between TSA checkpoint volumes and BTS OTP delays/capacity across 12 operational dimensions.
   - *Companion Workbook*: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `02_Executive_Cross_Dataset_Stat`).

7. **Table 4.6: The Nine-Airport Experimental Cohort Factorial Specification** (`table_4_6_nine_airport_experimental_cohort_factorial_specification.csv`)
   - *Scope*: Balanced 4x4 factorial design across 12 carrier-exclusive complexes at 9 hubs (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL).
   - *Companion Workbook*: `results/02_4tier_filtering/02_4tier_filtering.xlsx` (Sheet: `Section_2B_Nine_Airport_Experim`).

8. **Table 4.7: Summary Descriptive Statistics: 9-Airport Experimental Cohort vs. Top 25 Universe** (`table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`)
   - *Scope*: Formal comparison proving sample representativeness of the 9-airport experimental cohort against the Top 25 universe.
   - *Companion Workbook*: `results/02_4tier_filtering/02_4tier_filtering.xlsx` (Sheet: `Table_C_Summary_Descriptive_Sta`).

9. **Table 4.8: Day-of-Week Mean Daily Passenger Throughput Across Nine Selected Airports** (`table_4_8_day_of_week_mean_daily_passenger_throughput_nine_airports.csv`)
   - *Scope*: Local airport DOW profiles, weekly peak/trough days, and Peak/Trough ratios (highlighting LGA corporate profile = 2.30).
   - *Companion Workbook*: `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx`.

10. **Table 4.9: Empirical Lead-Lag Transfer Dynamics** (`table_4_9_empirical_lead_lag_transfer_dynamics.csv`)
    - *Scope*: Asymmetric correlation and explanatory power across Lag $t-1$, Same-Hour $t$, Lead $t+1, t+2, t+3$, and convolved kernels.
    - *Companion Workbook*: `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx` (Sheet: `Section_4B_Lead_Lag_Arrival_Dec`).

11. **Table 4.10: Master Model Benchmark Matrix (2025 Holdout)** (`table_4_10_master_model_benchmark_matrix.csv`)
    - *Scope*: Master benchmark matrix across the Four Canonical Models ($M_0, M_1^*, M_3, M_5$) on 72,053 holdout observations.
    - *Companion Workbook*: `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx` (Sheet: `Section_5A_Master_Model_Executi`).

12. **Table 4.11: Master Multi-Pillar Hypothesis Evaluation Matrix** (`table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`)
    - *Scope*: Formal empirical hypothesis test matrix across Robustness, Resilience, and Generalizability with explicit academic targets benchmarking $M_0, M_1^*, M_3, M_5$.
    - *Companion Workbook*: `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` (Sheet: `master_model_evaluation_metrics`).

### Chapter 5: Analysis and Discussion

13. **Table 5.1: Routine Operational Accuracy Across the Four Canonical Models** (`table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv`)
    - *Scope*: Robustness evaluation under nominal flight conditions (RMSE, MASE, stated target $\text{MASE} < 0.70$, and Diebold-Mariano significance testing).
    - *Companion Workbook*: `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` (Sheet: `Summary`).

14. **Table 5.2: Resilience and Shock Performance Under Severe Operational Disruption** (`table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv`)
    - *Scope*: Resilience evaluation under severe weather ground stops and ground delay programs (RMSE, MASE, $R_{\text{MASE}} \approx 1.00$, $\text{TTR} < 4.0\text{h}$).
    - *Companion Workbook*: `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` (Sheet: `Summary`).

15. **Table 5.3: Generalizability and Cross-Airport Transfer Performance** (`table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv`)
    - *Scope*: Zero-shot spatial transfer evaluation from EWR to LGA without retraining (RMSE, RTR $= 1.00$, $\Delta\text{MASE} \le 10.0\%$).
    - *Companion Workbook*: `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` (Sheet: `Summary`).

16. **Table 5.4: Master Asymmetric Trade-Off Matrix Across the Four Canonical Models** (`table_5_4_master_asymmetric_trade_off_matrix.csv` / `master_asymmetric_trade_off_matrix.csv`)
    - *Scope*: Synthesis of architectural trade-offs demonstrating asymmetric performance strengths across the three modeling families and confirming Hypothesis 1.
    - *Companion Workbook*: `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` (Sheet: `Summary`).

### Companion Operational Decision Matrices

17. **Master Asymmetric Trade-Off Matrix** (`master_asymmetric_trade_off_matrix.csv`)
    - *Scope*: Standalone conformed export of the Master Asymmetric Trade-Off Matrix with explicit academic targets, canonical models, and dimension winners.

18. **Dual-Track Model Selection Policy** (`dual_track_model_selection_policy.csv`)
    - *Scope*: Gated operational deployment rules for Gate 1 (Routine Flow Track $\to M_3$) and Gate 2 (Tactical Shock Track $\to M_5$).

---

## Referential Integrity & Audit Rule

All table numbers, column names, and decimal precisions in these CSV files are guaranteed to match the thesis manuscript chapters and the master pipeline output with **zero drift**.
