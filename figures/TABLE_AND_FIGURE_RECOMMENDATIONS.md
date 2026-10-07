# Master Table and Figure Recommendations for Thesis Manuscripts
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Document Purpose**: This reference guide provides the complete, authoritative specification for all tables and figures recommended for integration into the updated manuscript files (`chp1-intro.md` through `chp5-discussion.md`). It maps each visual asset and empirical table to its exact narrative insertion point, its underlying theoretical rationale (APA 7th Edition & heavy-traffic queuing principles), and its corresponding source asset in `figures/`, `results/manuscript_tables/`, and companion Excel workbooks.

---

## 1. Master Architecture & Chapter Allocation Overview

```
                      MASTER MANUSCRIPT VISUAL & TABULAR ALLOCATION
                      
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ Chapter I: Introduction (chp1-intro.md)                                                │
│  ├── Figure 1.1: Asymmetric Trade-Off Evaluation Triangle (H1 Framework)               │
│  ├── Table 1.1: Overview of the 3-Model Candidate Evaluation Suite & Baseline Control  │
│  └── Table 1.2: Research Delimitations, Geographical Scale & Federal Data Foundation   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Chapter II: Literature Review (chp2-litreview.md)                                      │
│  ├── Figure 2.1: The Checkpoint Tipping Point (Kingman Heavy-Traffic Queuing Curve)    │
│  ├── Table 2.1: Comparative Synthesis of Historical Airport Flow Modeling Paradigms    │
│  ├── Table 2.2: The "Values versus Volatility" Analytical Matrix (H2 Duality)          │
│  └── Figure 2.2: Conceptual Architecture of the Two-Stage Sequential Hybrid Model      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Chapter III: Methodology (chp3-methodology.md)                                         │
│  ├── Figure 1: Forecasting Model Family Comparison (Word Callout P18)                  │
│  ├── Figure 2: Evaluation Metric Definitions & Mathematical Formulas (Callout P56)    │
│  ├── Figure 3: Design and Procedure Phases (4-Phase Pipeline) (Callout P61)            │
│  ├── Figure 4: Sample Framework for Terminal Capacity & Checkpoints (Callout P101)     │
│  ├── Figure 5: Airport Operational Archetypes & Terminal Configurations (Callout P103) │
│  ├── Table 3.1: Three-Tier Operational Taxonomy & Scenario Boundary Thresholds         │
│  ├── Table 3.2: Four-Tier Purposive Filtering Pipeline Specification                  │
│  └── Table 3.3: Values vs. Volatility Dual-Paradigm Feature Specification (24 Attrs)   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Chapter IV: Results & Findings (chp4-results.md)                                       │
│  ├── Figure 4.1: Chapter IV Architecture & Empirical Roadmap (Callout P4)              │
│  ├── Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Callout P9)       │
│  ├── Table 4.2: Post-ETL Master Summary Descriptive Statistics (Callout P11)           │
│  ├── Table 4.3a: Post-Pandemic Temporal Demarcation Evaluation (May 1, 2022 Break)     │
│  ├── Table 4.3b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Network)   │
│  ├── Figure 4.2: Annual Volatility Dynamics & Coupled Volatility Clusters              │
│  ├── Table 4.4a: Master Day-of-Week Operational Volatility Regimes                     │
│  ├── Figure 4.3: Day-of-Week Burstiness Dynamics Across National Airfields             │
│  ├── Figure 4.4: Intraday Diurnal Volatility Curves & Dual Peak Clusters               │
│  ├── Table 4.5: Econometric Verification of Carrier Checkpoint Isolation (4 Tests)     │
│  ├── Table 4.6: The Nine-Airport Experimental Cohort Specification (Callout P32)       │
│  ├── Table 4.7: Summary Descriptive Statistics: Cohort vs. Top 25 (Callout P37)        │
│  ├── Table 4.8: Local Seasonal & DOW Volatility Profiles Across the 9 Cohort Airfields │
│  ├── Table 4.9: Empirical Lead-Lag Transfer Dynamics (Callout P47)                     │
│  ├── Figure 4.5: Empirical Lead-Lag Passenger Show-Up Curve Convolution                │
│  ├── Table 4.10: Master Model Benchmark Matrix (2025 Full-Year Holdout) (Callout P62)  │
│  ├── Table 4.11: Pairwise Diebold-Mariano Forecast Accuracy Divergence Tests           │
│  └── Table 4.12: The Values vs. Volatility Empirical Proof (H2 Regression Matrix)      │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Chapter V: Discussion & Conclusions (chp5-discussion.md)                               │
│  ├── Table 5.1: Evaluation Dimension 1: Routine Operational Accuracy (Callout P13)     │
│  ├── Table 5.2: Evaluation Dimension 2: Resilience Under Disruption (IROPS Regimes)    │
│  ├── Table 5.3: Evaluation Dimension 3: Generalizability Across Facilities (Zero-Shot) │
│  ├── Table 5.4: Master Asymmetric Trade-Off Matrix (H1 Synthesis & Strategic Playbook) │
│  ├── Figure 5.1: The Asymmetric Trade-Off Triangle (Multi-Dimensional Radar Chart)     │
│  ├── Figure 5.2: The Empty Checkpoint Fallacy & Error Feedback Recovery Trajectory     │
│  ├── Figure 5.3: Dual-Track Operational Decision Playbook for Airport JOCs             │
│  └── Figure 5.4: Volatility-Buffered Dynamic Lane Dimensioning Framework               │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Chapter I: Introduction (`thesis_docs/manuscripts/chp1-intro.md`)

### Proposed Table 1.1: The 3-Model Candidate Evaluation Suite & Baseline Control
* **Target Insertion Point**: Directly following Section `## Research Questions` and the Master Asymmetric Trade-Off Hypothesis ($H_1$) statement (after paragraph 15).
* **Academic Rationale**: Establishes the exact 3 candidate model paradigms and empirical baseline control early, preventing reader confusion regarding model selection.
* **Content Specification**:
  - *Baseline Control (Daily Persistence Benchmark)*: $\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$.
  - *Model 1 (Deterministic Flight Schedule Model)*: Flight timetable convolution across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$).
  - *Model 2 (Supervised Machine Learning Model)*: Automated gradient-boosted decision-tree regressor trained on flight schedules and 24 BTS OTP delay and cancellation features.
  - *Model 3 (Dynamic Two-Stage Hybrid Model)*: Sequential two-stage architecture coupling recurring scheduled banks with live prior-hour recursive error feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$).
* **Source / Reference**: `thesis_docs/ssot/Chapter_1_SSOT.md`, `results/tables/master_model_evaluation_metrics_and_targets.csv`.

### Proposed Table 1.2: Scope, Delimitations, and Federal Data Foundation Summary
* **Target Insertion Point**: Within Section `## Delimitations`, following paragraph 21.
* **Academic Rationale**: Summarizes the empirical boundaries of the investigation in an APA 7 table, contrasting the macro 25-airport network against the 9-airport experimental cohort.
* **Content Specification**:
  - Longitudinal span: January 1, 2019 to December 31, 2025 ($N = 22,491$ airport-days; 42.06 million conformed records).
  - Post-pandemic development window: May 1, 2022 to December 31, 2025.
  - Out-of-time evaluation holdout: Full calendar year 2025 (3,222 airport-days).
  - 4 Federal data repositories: TSA FOIA hourly screening logs, BTS OTP Form 234, BTS Form 41 T-100, BTS DB1B/DB1C 10% coupon surveys.
* **Source / Reference**: `figures/01_Sample_and_Airport_Selection/data_sample_profile.csv`.

### Proposed Figure 1.1: The Asymmetric Trade-Off Evaluation Triangle ($H_1$)
* **Target Insertion Point**: Directly following the statement of Hypothesis 1 ($H_1$, paragraph 15).
* **Academic Rationale**: Visually illustrates the thesis core hypothesis that no single model is universally best: Model 3 wins Resilience, Model 1 wins Generalizability, and Model 2 wins Routine Pareto Efficiency.
* **Source Asset**: Rendered as a vector diagram or radar plot from `figures/03_Modeling_and_Evaluation/models_and_tests.csv`.

---

## 3. Chapter II: Literature Review (`thesis_docs/manuscripts/chp2-litreview.md`)

### Proposed Figure 2.1: The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)
* **Target Insertion Point**: Under Section `## Traditional Approaches and Operational Complexity`, directly following the Allen-Cunneen approximation formula (after paragraph 10).
* **Academic Rationale**: Visually depicts Kingman’s queuing law ($W_q \approx \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), demonstrating that queue backlog escalates quadratically with arrival burstiness ($C_a^2$) as checkpoint utilization $\rho \to 1.0$.
* **Source Asset**: Custom plot generated from `figures/03_Modeling_and_Evaluation/passenger_stochastic_arrival_parameters.csv`.

### Proposed Table 2.1: Comparative Synthesis of Historical Airport Flow Modeling Paradigms
* **Target Insertion Point**: Following Section `## Simulation Modeling and Real-Time Terminal Management` (after paragraph 21).
* **Academic Rationale**: Contrasts the 4 major modeling paradigms in transportation literature across computational latency, input requirements, transparency, and failure modes.
* **Columns**: Modeling Paradigm, Theoretical Mechanism, Input Data Requirements, Computational Latency, Primary Operational Vulnerability, Aviation Literature Citations.
* **Source Asset**: Synthesized from `figures/03_Modeling_and_Evaluation/exploratory_metric_criteria_research.csv`.

### Proposed Table 2.2: The "Values versus Volatility" Analytical Matrix ($H_2$)
* **Target Insertion Point**: Following Section `## The "Values versus Volatility" Paradigm in Transportation Demand` (after paragraph 15).
* **Academic Rationale**: Articulates the mathematical and operational differences between feature levels (static counts) and feature volatilities (dispersion, standard deviation, CV) across intraday diurnal and multi-day horizons.
* **Source Asset**: Derived from `results/04_model_execution_2025_holdout.xlsx` (tab: `values_vs_volatility`).

### Proposed Figure 2.2: Conceptual Architecture of the Two-Stage Sequential Hybrid Model
* **Target Insertion Point**: Following Section `## Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability` (after paragraph 34).
* **Academic Rationale**: Schematically demonstrates how Stage 1 (recurring flight schedule cycles and empirical show-up curves) feeds baseline predictions into Stage 2 (live recursive error feedback $e_{t-1}$), preventing under-prediction during ground delays.
* **Source Asset**: `figures/03_Modeling_and_Evaluation/Model walk through.png` / `figures/03_Modeling_and_Evaluation/model_walkthrough_architecture.csv`.

---

## 4. Chapter III: Methodology (`thesis_docs/manuscripts/chp3-methodology.md`)

Chapter III contains five explicit figure callouts in the Word review draft that must be connected to their corresponding assets, plus three structural tables.

### Existing Figure Callouts in Chapter III:
1. **Figure 1: Forecasting Model Family Comparison**
   - *Callout Location*: Paragraphs 18–19.
   - *Recommended Asset*: [`figures/03_Modeling_and_Evaluation/models and tests.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/03_Modeling_and_Evaluation/models%20and%20tests.png) and companion data [`models_and_tests.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/03_Modeling_and_Evaluation/models_and_tests.csv).
   - *Description*: High-fidelity architectural schematic comparing Baseline Control, Model 1 (ACRP 40 convolution), Model 2 (supervised ML regressor), and Model 3 (sequential hybrid).

2. **Figure 2: Evaluation Metric Definition**
   - *Callout Location*: Paragraphs 56–57.
   - *Recommended Asset*: [`figures/03_Modeling_and_Evaluation/Evaluation Metric Definition.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/03_Modeling_and_Evaluation/Evaluation%20Metric%20Definition.png) and companion data [`evaluation_metric_definition.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/03_Modeling_and_Evaluation/evaluation_metric_definition.csv).
   - *Description*: Mathematical specification and operational interpretation of RMSE, MASE, $R_{\text{MASE}}$, TTR, RTR, and Diebold-Mariano ($DM$).

3. **Figure 3: Design and Procedure Phases**
   - *Callout Location*: Paragraphs 61–62.
   - *Recommended Asset*: [`figures/02_Data_Pipelines_and_Threats/Combined_Data_Pipeline_and_Funnel_Lifecycle.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/02_Data_Pipelines_and_Threats/Combined_Data_Pipeline_and_Funnel_Lifecycle.png) and [`combined_data_pipeline_and_funnel_lifecycle.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/02_Data_Pipelines_and_Threats/combined_data_pipeline_and_funnel_lifecycle.csv).
   - *Description*: Four-phase experimental research progression (Phase 1: ETL & Data Hygiene $\to$ Phase 2: Model Development $\to$ Phase 3: Holdout Evaluation $\to$ Phase 4: Statistical Validation).

4. **Figure 4: Sample Framework for Terminal Capacity and Checkpoint Configuration**
   - *Callout Location*: Paragraphs 101–102.
   - *Recommended Asset*: [`figures/01_Sample_and_Airport_Selection/Airport selection strategy document.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/01_Sample_and_Airport_Selection/Airport%20selection%20strategy%20document.png) and [`airport_selection_strategy_document.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/01_Sample_and_Airport_Selection/airport_selection_strategy_document.csv).
   - *Description*: Terminal architectural framework detailing physical screening lanes, checkpoint queuing snakes, dedicated carrier concourses, and spatial aggregation.

5. **Figure 5: Airport Operational Archetypes and Terminal Configuration**
   - *Callout Location*: Paragraphs 103–104.
   - *Recommended Asset*: [`figures/01_Sample_and_Airport_Selection/airport clusters.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/01_Sample_and_Airport_Selection/airport%20clusters.png) and [`airport_clusters.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/01_Sample_and_Airport_Selection/airport_clusters.csv).
   - *Description*: Four-cluster PCA/K-Means matrix categorizing candidate Top 25 airfields across transfer ratio, international share, flight scale, and delay dispersion.

### Additional Recommended Tables for Chapter III:
* **Table 3.1: Three-Tier Operational Taxonomy and Scenario Boundary Thresholds**
  - *Location*: Within Section `### Quantitative Evaluation Dimensions and Operational Regimes` (after paragraph 90).
  - *Content*: Explicitly specifies Tier 1 Nominal Baseline ($\text{Delay} < 15$m, 0 Cancels), Tier 2 Routine Operations (15–30m delay churn), and Tier 3 Irregular Operations / IROPS ($\text{Delay} \ge 45$m or Cancels $\ge 5$).
* **Table 3.2: Four-Tier Purposive Filtering Pipeline Specification**
  - *Location*: Within Section `### Four-Tiered Purposive Filtering Pipeline` (after paragraph 132).
  - *Content*: Drop progression table: Tier 1 (Macro: Top 25 volume), Tier 2 (Meso: Big-3 symmetry & WN exclusion, 14 retained), Tier 3 (Micro: Checkpoint exclusivity, 9 retained), Tier 4 (Orthogonal Factorial Grid: 12 complexes across 9 airfields). Source: `results/02_4tier_filtering.xlsx`.
* **Table 3.3: Values versus Volatility Dual-Paradigm Feature Specification (24 Attributes)**
  - *Location*: Within Section `### Transform` (after paragraph 202).
  - *Content*: Feature dictionary defining 14 Feature Level attributes and 10 Feature Volatility attributes engineered in DuckDB. Source: `results/04_model_execution_2025_holdout.xlsx`.

---

## 5. Chapter IV: Results (`thesis_docs/manuscripts/chp4-results.md`)

Chapter IV contains formal callouts and image placeholders in the Word draft. Replacing these placeholders with conformed APA 7 tables and restoring key diagnostic tables will produce an exhaustive empirical presentation.

| Table / Figure Number | Title | Target Location in `chp4-results.md` | Primary Source Asset |
| :--- | :--- | :--- | :--- |
| **Figure 4.1** | *Chapter IV Architecture Roadmap* | Replace Callout P4 | Flowchart diagram of Sections 4.1 $\to$ 4.2 $\to$ 4.3 $\to$ 4.4 |
| **Table 4.1** | *Master Post-ETL Multi-Source Data Foundation Census* | Replace Callout P9 | [`results/manuscript_tables/table_4_1_master_post_etl_multi_source_data_foundation_census.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_1_master_post_etl_multi_source_data_foundation_census.csv) |
| **Table 4.2** | *Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)* | Replace Callout P11 | [`results/manuscript_tables/table_4_2_post_etl_master_summary_descriptive_statistics_top25.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_2_post_etl_master_summary_descriptive_statistics_top25.csv) |
| **Table 4.3a** | *Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network* | Within Section `### Temporal Boundaries` (after paragraph 16) | [`results/manuscript_tables/table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_3a_post_pandemic_temporal_demarcation_evaluation.csv) |
| **Table 4.3b** | *Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)* | Within Section `### Defining Seasonality` (after paragraph 18) | [`results/manuscript_tables/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv) |
| **Figure 4.2** | *Annual Volatility Dynamics & Coupled Volatility Clusters* | Directly following Table 4.3b | [`thesis_docs/manuscripts/figures/01_annual_volatility_tsa_otp_clustering.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/figures/01_annual_volatility_tsa_otp_clustering.png) |
| **Table 4.4a** | *Master Day-of-Week Operational Volatility Regimes* | Following Figure 4.2 | [`results/manuscript_tables/table_4_4a_master_day_of_week_operational_volatility_regimes.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_4a_master_day_of_week_operational_volatility_regimes.csv) |
| **Figure 4.3** | *Day-of-Week Volatility Dynamics Across the National Network* | Directly following Table 4.4a | [`thesis_docs/manuscripts/figures/02_day_of_week_volatility_dynamics.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/figures/02_day_of_week_volatility_dynamics.png) |
| **Figure 4.4** | *Intraday Hourly Volatility Clusters (Bimodal Peaks by DOW)* | Under Section `TSA and OTP Throughput Data` (after paragraph 22) | [`thesis_docs/manuscripts/figures/03_diurnal_hourly_volatility_clusters_by_dow.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/figures/03_diurnal_hourly_volatility_clusters_by_dow.png) |
| **Table 4.5** | *Econometric Verification of Carrier Checkpoint Isolation* | Within Section `### Four-Phase Filtering Pipeline` (after paragraph 29) | [`results/manuscript_tables/table_4_5_econometric_verification_of_carrier_checkpoint_isolation.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_5_econometric_verification_of_carrier_checkpoint_isolation.csv) |
| **Table 4.6** | *The Nine-Airport Experimental Cohort Specification* | Replace Callout P32 | [`results/manuscript_tables/table_4_6_the_nine_airport_experimental_cohort_specification.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_6_the_nine_airport_experimental_cohort_specification.csv) |
| **Table 4.7** | *Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25* | Replace Callout P37 | [`results/manuscript_tables/table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv) |
| **Table 4.8** | *Local Seasonal and Day-of-Week Volatility Profiles Across the Nine Selected Airports* | Within Section `### Descriptive Statistics for Subset` (after paragraph 41) | [`results/manuscript_tables/table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_8_local_seasonal_and_dow_volatility_profiles_9_airports.csv) |
| **Table 4.9** | *Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)* | Replace Callout P47 | [`results/manuscript_tables/table_4_9_empirical_lead_lag_transfer_dynamics.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_9_empirical_lead_lag_transfer_dynamics.csv) |
| **Figure 4.5** | *Empirical Lead-Lag Passenger Show-Up Curve Convolution (t, t+1, t+2, t+3)* | Directly following Table 4.9 | [`figures/03_Modeling_and_Evaluation/physical transfer lead lag time.png`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/figures/03_Modeling_and_Evaluation/physical%20transfer%20lead%20lag%20time.png) |
| **Table 4.10** | *Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Holdout)* | Replace Callout P62 | [`results/manuscript_tables/table_4_10_master_model_benchmark_matrix_2025_holdout.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_10_master_model_benchmark_matrix_2025_holdout.csv) |
| **Table 4.11** | *Pairwise Diebold-Mariano Forecast Accuracy Divergence Tests* | Within Section `### General Model Performance` (after paragraph 68) | [`results/manuscript_tables/table_4_11_pairwise_diebold_mariano_tests.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_4_11_pairwise_diebold_mariano_tests.csv) |
| **Table 4.12** | *The "Values versus Volatility" Paradigm: Feature Space Regression Benchmark* | Within Section `### Model Performance and Hypothesis Testing` (after paragraph 70) | Proves $H_2$: Static volume levels fail on multi-day volatility ($R^2 < 0$), feature volatilities succeed ($R^2 > 0.31$). |

---

## 6. Chapter V: Discussion (`thesis_docs/manuscripts/chp5-discussion.md`)

Chapter V currently contains an image placeholder for Table 5.1. Adding the three dimensional evaluation tables and the master trade-off synthesis table directly substantiates the qualitative discussion.

| Table / Figure Number | Title | Target Location in `chp5-discussion.md` | Primary Source Asset |
| :--- | :--- | :--- | :--- |
| **Table 5.1** | *Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models* | Replace Callout P13 | [`results/manuscript_tables/table_5_1_evaluation_dimension_1_robustness.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_5_1_evaluation_dimension_1_robustness.csv) |
| **Table 5.2** | *Evaluation Dimension 2: Resilience Under Disruption (Irregular Operations / IROPS)* | Following Section `## Empirical Evaluation of Resilience Under Disruption` (after paragraph 24) | [`results/manuscript_tables/table_5_2_evaluation_dimension_2_resilience.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_5_2_evaluation_dimension_2_resilience.csv) |
| **Figure 5.2** | *The Empty Checkpoint Fallacy & Real-Time Error Innovation Recovery* | Directly following Table 5.2 | Time-series chart demonstrating Model 2 divergence during flight delays vs. Model 3 recursive error correction recovering nominal error within 2.8 hours. |
| **Table 5.3** | *Evaluation Dimension 3: Generalizability Across Facilities (Zero-Shot Spatial Transfer)* | Following Section `## Empirical Evaluation of Generalizability Across Facilities` (after paragraph 30) | [`results/manuscript_tables/table_5_3_evaluation_dimension_3_generalizability.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_5_3_evaluation_dimension_3_generalizability.csv) |
| **Table 5.4** | *Master Asymmetric Trade-Off Matrix ($H_1$ Synthesis & Operational Decision Matrix)* | Following Section `## Implications and Recommendations` (after paragraph 36) | [`results/manuscript_tables/table_5_4_master_asymmetric_trade_off_matrix.csv`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/results/manuscript_tables/table_5_4_master_asymmetric_trade_off_matrix.csv) |
| **Figure 5.1** | *The Asymmetric Trade-Off Triangle ($H_1$ Multi-Dimensional Radar Plot)* | Directly following Table 5.4 | Multi-axis radar/spider plot comparing Baseline Control, Model 1, Model 2, and Model 3 across Robustness, Resilience, and Generalizability. |
| **Figure 5.3** | *The Dual-Track Operational Decision Playbook for Airport Joint Operations Centers* | Within Section `## Implications and Recommendations` (after paragraph 36) | Flowchart illustrating operational deployment: Model 1 for master planning / new facilities, Model 2 for advance 7-day staffing, and Model 3 for tactical convective ground stops. |
| **Figure 5.4** | *Volatility-Buffered Dynamic Lane Dimensioning Framework* | Concluding paragraph of Chapter V | Operational diagram showing how predicted $\sigma_{\text{TSA}}$ translates into dynamic lane allocations via the conformal safety buffer equation to eliminate peak queue blowouts. |

---

## 7. Concrete Next-Step Prompts for Another Conversation

When you begin your next conversation, you can reference this file and use any of the targeted prompts below:

### Option A: Insert Tables into Chapter IV (Results)
> *"Please reference `figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md` Section 5. Replace the table image placeholders in `thesis_docs/manuscripts/chp4-results.md` with the formal conformed Markdown tables from `results/manuscript_tables/` (Tables 4.1, 4.2, 4.6, 4.7, 4.9, 4.10) and embed Figures 4.1 through 4.5."*

### Option B: Insert Tables into Chapter V (Discussion)
> *"Please reference `figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md` Section 6. In `thesis_docs/manuscripts/chp5-discussion.md`, replace the Table 5.1 placeholder and embed Tables 5.1, 5.2, 5.3, 5.4 along with Figures 5.1 through 5.4."*

### Option C: Insert Methodological Figures into Chapter III
> *"Please reference `figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md` Section 4. In `thesis_docs/manuscripts/chp3-methodology.md`, insert Figures 1 through 5 matching the existing Word callouts and add Tables 3.1, 3.2, and 3.3."*

### Option D: Batch Process All Chapters
> *"Please reference `figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md`. Execute the complete table and figure integration across all chapters (Chapters I through V) adhering strictly to APA 7th edition formatting and synchronizing with `results/manuscript_tables/` and companion Excel workbooks."*
