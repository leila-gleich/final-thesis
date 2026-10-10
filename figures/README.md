# Thesis Figures, Exhibits, and Companion Data Directory
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Directory Purpose**: This directory provides the intuitive, canonical home for all visual graphics, conceptual frameworks, process diagrams, empirical figures, companion CSV datasets, and multi-tab Excel workbooks organized strictly by **Thesis Chapter**.
>
> All figures and tables strictly adhere to **APA Style (7th ed.)**, authentic commercial aviation operations nomenclature, and **Kingman's Heavy-Traffic Queuing Formula** ($W_q \\approx \\frac{\\rho}{1-\\rho} \\frac{C_a^2+C_s^2}{2} \\frac{1}{\\mu}$), targeting **passenger throughput volatility** ($\\sigma_{\\text{TSA}}$ and $CV_{\\text{TSA}}$) rather than raw volume.

---

## 1. Chapter-by-Chapter Master Directory Architecture

```
figures/
├── ch01_intro/                 <-- Chapter I: Introduction (3 figures, 3 CSVs)
├── ch02_lit_review/            <-- Chapter II: Literature Review (6 figures, 6 CSVs)
├── ch03_methodology/           <-- Chapter III: Methodology (15 figures, 15 CSVs, 3 workbooks)
│   └── workbooks/              <-- APA 7 Multi-Tab Companion Excel Workbooks
├── ch04_results/               <-- Chapter IV: Results & Findings (5 figure pairs, 7 CSVs)
├── ch05_discussion/            <-- Chapter V: Discussion & Conclusions (1 figure, 5 CSVs)
├── appendix/                   <-- Thesis Appendix & Reference (7 figures, 7 CSVs, 1 workbook)
├── 04_Appendix_and_Reference/  <-- Legacy Appendix Folder (Preserved for backward compatibility)
└── TABLE_AND_FIGURE_RECOMMENDATIONS.md <-- Authoritative Manuscript Integration Guide
```

---

## 2. Summary of Visual Assets and Datasets by Chapter

### Chapter I: Introduction (`ch01_intro/`)
* **Figure 1.1**: `models and tests.png` + `models_and_tests.csv` — *Asymmetric Trade-Off Evaluation Triangle ($H_1$)*
* **Table 1.1**: Derived from `models_and_tests.csv` — *3-Model Candidate Evaluation Suite & Baseline Control*
* **Table 1.2**: `Data Sample Profile.png` + `data_sample_profile.csv` — *Scope, Delimitations & Federal Data Foundation*
* **Delimitation Guide**: `Inclusion of top 25 network approach.png` + `inclusion_of_top_25_network_approach.csv`

### Chapter II: Literature Review (`ch02_lit_review/`)
* **Figure 2.1**: `pax stochastic arrival.png` + `passenger_stochastic_arrival_parameters.csv` — *The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)*
* **Table 2.1**: `exploratory metric criteria research .png` + `exploratory_metric_criteria_research.csv` — *Comparative Synthesis of Airport Flow Paradigms*
* **Figure 2.2**: `Model walk through.png` + `model_walkthrough_architecture.csv` — *Two-Stage Sequential Hybrid Architecture*
* **Framework**: `clusting and connecting paradox.png` + `clustering_and_connecting_paradox.csv` — *The Connecting Passenger Paradox*
* **Framework**: `otp & tsa.png` + `otp_and_tsa_volume_coupling.csv` — *TSA & OTP Volume Coupling vs. Volatility*
* **Framework**: `OTP volatility.png` + `otp_volatility.csv` — *Flight Departure Delay Volatility Regimes*

### Chapter III: Methodology (`ch03_methodology/`)
* **Figure 1**: `models and tests.png` + `models_and_tests.csv` — *Forecasting Model Family Comparison (Word Callout P18)*
* **Figure 2**: `Evaluation Metric Definition.png` + `evaluation_metric_definition.csv` — *Evaluation Metric Definitions (Callout P56)*
* **Figure 3**: `Combined_Data_Pipeline_and_Funnel_Lifecycle.png` + `combined_data_pipeline_and_funnel_lifecycle.csv` — *Design and Procedure Phases (Callout P61)*
* **Figure 4**: `Airport selection strategy document.png` + `airport_selection_strategy_document.csv` — *Sample Framework for Terminal Capacity & Checkpoints (Callout P101)*
* **Figure 5**: `airport clusters.png` + `airport_clusters.csv` — *Airport Operational Archetypes & Terminal Configurations (Callout P103)*
* **10 Supporting Diagrams & Schemas**: `checkpoint examples.png`, `Combined_Data_Threats_and_Remediation_Matrix.png`, `Control and test process.png`, `imputed defs.png`, `metrics.png`, `physical transfer lead lag time.png`, `post-pandemic justification.png`, `Power of 9 airports.png`, `t100 schema.png`, `TSA Schema.png` (each paired with its `.csv`).
* **Companion Workbooks (`workbooks/`)**: `01_Sample_and_Airport_Selection.xlsx`, `02_Data_Pipelines_and_Threats.xlsx`, `03_Modeling_and_Evaluation.xlsx`.

### Chapter IV: Results & Findings (`ch04_results/`)
* **Figure 4.2**: `01_annual_volatility_tsa_otp_clustering.png` + `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv` — *Annual Volatility Dynamics & Coupled Volatility Clusters*
* **Figure 4.3**: `02_day_of_week_volatility_dynamics.png` + `table_4_4a_master_day_of_week_operational_volatility_regimes.csv` — *Day-of-Week Volatility Dynamics Across the National Network*
* **Figure 4.4**: `03_diurnal_hourly_volatility_clusters_by_dow.png` + `table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv` — *Intraday Diurnal Hourly Volatility Clusters (Bimodal Peaks)*
* **Figure 4.5**: `figure_4_5_lead_lag_convolution_curves.png` + `table_4_9_empirical_lead_lag_transfer_dynamics.csv` — *Empirical Lead-Lag Passenger Show-Up Curve Convolution*
* **Diagnostic**: `04_sample_sufficiency_distribution.png` + `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv` — *Sample Sufficiency Distribution*

### Chapter V: Discussion & Conclusions (`ch05_discussion/`)
* **Figure 5.1**: `figure_5_1_asymmetric_trade_off_triangle.png` + `table_5_4_master_asymmetric_trade_off_matrix.csv` — *The Asymmetric Trade-Off Evaluation Triangle ($H_1$)*
* **Table 5.1**: `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv` — *Evaluation Dimension 1: Routine Operational Accuracy*
* **Table 5.2**: `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv` — *Evaluation Dimension 2: Resilience Under Disruption*
* **Table 5.3**: `table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv` — *Evaluation Dimension 3: Generalizability Across Facilities*
* **Table 5.4**: `table_5_4_master_asymmetric_trade_off_matrix.csv` — *Master Asymmetric Trade-Off Matrix ($H_1$ Synthesis)*
* **Policy**: `dual_track_model_selection_policy.csv` — *Dual-Track Model Selection Policy*

### Appendix: Reference & Architecture (`appendix/` & `04_Appendix_and_Reference/`)
* `BTS-DB1B_Appendix.png` + `bts_db1b_table_hierarchy.csv` — *BTS DB1B Survey Relational Hierarchy*
* `Backups organization.png` + `backups_organization.csv` — *Research Archive Backup Directory Structure*
* `Diagrams and Screenshot Layout.png` + `diagrams_and_screenshot_layout.csv` — *Diagram & Screenshot Layout Tree*
* `data profile top9.png` + `data_profile_top9.csv` — *Nine-Airport Target Cohort Parquet Feature Store Partitions*
* `database profiles.png` + `database_profiles.csv` — *Base Feeds Database Profiles & Record Census*
* `dataset breakdown.png` + `dataset_breakdown.csv` — *Feature Store Dataset Breakdown*
* `methodological assumptions.png` + `methodological_assumptions.csv` — *Master 14-Point Assumptions Framework*
* `04_Appendix_and_Reference.xlsx` — *Consolidated Multi-Tab Appendix Workbook*

---

## 3. Maintenance and Synchronization

To regenerate all 4 multi-tab APA 7 Excel workbooks from the conformed CSV datasets, run:
```bash
python3 src/analysis/generate_figures_tables_excel.py
```
To run the verification test suite:
```bash
python3 -m unittest tests/test_figure_workbooks.py
```
