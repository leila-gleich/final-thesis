# Master Tables and Figures Directory
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Core Purpose**: This unified directory serves as the **single authoritative home** for all presentation tables, companion Excel workbooks, and visual figures across the thesis. It eliminates version ambiguity and folder fragmentation, providing an intuitive chapter-by-chapter reference for the thesis committee and airport operational planners.

---

## 1. Directory Structure at a Glance

All presentation tables and visual assets are organized into three primary operational domains:

```
tables and figures/
│
├── appendix/
│   ├── appendix_tables.xlsx             <- Master APA 7th workbook containing ALL 30 Appendix tables (A.1 to N.1)
│   ├── BTS-DB1B_Appendix.png            <- BTS DB1B hierarchical data flow diagram
│   ├── Backups organization.png         <- Primary archival and version backup architecture
│   ├── Diagrams and Screenshot Layout.png <- Visual layout catalog of empirical exhibits
│   ├── data profile top9.png            <- 9-airport experimental cohort baseline profile
│   ├── database profiles.png            <- Federal reporting feed profiles and schema grain
│   ├── dataset breakdown.png            <- Longitudinal dataset breakdown across reporting years
│   └── methodological assumptions.png   <- Formal methodological assumptions and limitations matrix
│
├── methodology/
│   ├── methodology-tables.xlsx          <- Master procedural and design pipeline workbook (Tables 3.1, A.1, A.2, A.3)
│   ├── 01_Sample_and_Airport_Selection.xlsx <- Purposive 4-tier filtering & cohort selection workbook
│   ├── 02_Data_Pipelines_and_Threats.xlsx   <- Data engineering, schema DDL, and threats workbook
│   ├── 03_Modeling_and_Evaluation.xlsx     <- Modeling architecture, show-up curves, and evaluation workbook
│   └── [Figure PNGs]                    <- Architecture flowcharts, schema layouts, and model family comparisons
│
└── results/
    ├── thesis_tables.xlsx               <- Master Results & Findings workbook (ALL 16 Tables: Ch. 4 & 5 + Dual-Track Policy)
    ├── 01_annual_volatility_tsa_otp_clustering.png   <- Macro annual seasonal volatility clusters
    ├── 02_day_of_week_volatility_dynamics.png        <- Day-of-week burstiness and demand archetypes
    ├── 03_diurnal_hourly_volatility_clusters_by_dow.png <- Diurnal bimodal flight bank surge curves
    ├── figure_4_2_annual_volatility_clusters.png     <- Coupled volatility regimes across national airfields
    ├── figure_4_3_day_of_week_volatility_dynamics.png <- Daily throughput variation and operational archetypes
    ├── figure_4_4_diurnal_hourly_volatility_clusters.png <- Hourly screening volume dispersion across the 24-hour cycle
    ├── figure_4_5_lead_lag_convolution_curves.png    <- Empirical ACRP Report 40 passenger arrival distributions
    └── figure_5_1_asymmetric_trade_off_triangle.png  <- Multi-dimensional radar chart proving Hypothesis 1 (H1)
```

---

## 2. Where to Find Specific Tables

### A. Methodology Tables
Located in `tables and figures/methodology/`:
- **`methodology-tables.xlsx`**:
  - `Design_Procedures_Summary`: Table 3.1: Four-Phase Sequential Methodological Pipeline.
  - `Design_Procedures_Detailed`: Table A.1: Detailed Procedural Execution Framework & Protocols.
  - `Dataset_Partitioning`: Table A.2: Longitudinal Dataset Partitioning (20-mo train / 12-mo val / 12-mo holdout).
  - `Data_Sources_Summary`: Table A.3: Primary Authorized Secondary Data Repositories & Record Census.
- **`01_Sample_and_Airport_Selection.xlsx`**:
  - `airport_clusters`: Master 4-cluster by 3-carrier experimental matrix mapping airports to carrier-exclusive checkpoints.
  - `selection_strategy`: Four-tiered purposive filtering pipeline justification.
  - `connecting_paradox`: Unsupervised clustering parameters and DB1B connecting bypass dynamics.
  - `data_sample_profile`: Multi-source conformed analytical data foundation census (42,062,039 records).
  - `top25_network_approach`: Rhetorical function and placement of Top 25 network exploratory baselines.
  - `power_of_9_airports`: Balanced 4x4 factorial design with 12 carrier facilities across 9 hubs.
  - `post_pandemic_justification`: Empirical justification for the May 1, 2022 demarcation baseline.
- **`02_Data_Pipelines_and_Threats.xlsx`**:
  - Checkpoint examples, pipeline funnel lifecycle, threats remediation matrix, imputed value definitions, volume coupling, OTP volatility dispersion, and TSA/T-100 relational schemas.
- **`03_Modeling_and_Evaluation.xlsx`**:
  - Control and test process, evaluation metric definitions, model walkthrough pipeline, empirical show-up curves, lead-lag timelines, and probabilistic evaluation metrics.

### B. Results & Findings Tables (Chapters IV & V)
Located in `tables and figures/results/thesis_tables.xlsx`:
All 16 empirical tables are formatted according to APA Style (7th ed.) with thin horizontal boundary rules, zero auto-filters, and an interactive Table of Contents tab:

| Table ID | Sheet Name | Academic Table Title | Scope & Role |
| :---: | :--- | :--- | :--- |
| **Table 4.1** | `table_4_1` | *Master Post-ETL Multi-Source Data Foundation Census* | 42,062,039 conformed federal records across 4 feeds |
| **Table 4.2** | `table_4_2` | *Post-ETL Master Summary Descriptive Statistics* | Macro scale across Top 25 (1,754 pax/hr; $\sigma=1,184$) |
| **Table 4.3** | `table_4_3` | *Master Annual Seasonal Volatility Regimes Summary* | 4 macro seasonal regimes across 1,341 post-demarcation days |
| **Table 4.4** | `table_4_4` | *Master Day-of-Week Operational Volatility Regimes* | 3 DOW archetypes (Midweek Surge, Weekend Churn, Hybrid) |
| **Table 4.5** | `table_4_5` | *Master Cross-Dataset Econometric Relationships* | The Hub Disconnect ($R^2$ jumps +115%) & volatility coupling |
| **Table 4.6** | `table_4_6` | *Nine-Airport Experimental Cohort Factorial Specification* | Balanced 4x4 matrix across 12 carrier-exclusive complexes |
| **Table 4.7** | `table_4_7` | *Summary Descriptive Statistics: Nine-Airport Cohort vs. Top 25* | Methodological contrast confirming cohort representativeness |
| **Table 4.8** | `table_4_8` | *Day-of-Week Mean Daily Passenger Throughput Across Nine Airports* | Local facility operational throughput baselines |
| **Table 4.9** | `table_4_9` | *Empirical Lead-Lag Transfer Dynamics* | Lead-time distributions ($t+1, t+2, t+3$) raising $R^2$ to 48.78% |
| **Table 4.10** | `table_4_10` | *Master Model Benchmark Matrix (2025 Full-Year Holdout)* | Holdout accuracy: $R^2$, RMSE, MAE, MASE across 4 models |
| **Table 4.11** | `table_4_11` | *Master Multi-Pillar Hypothesis Evaluation Matrix* | Multi-pillar evaluation confirming Master Hypothesis 1 ($H_1$) |
| **Table 5.1** | `table_5_1` | *Evaluation Dimension 1: Routine Operational Accuracy (Robustness)* | Nominal A14 conditions: Model 3 lowest RMSE, Model 2 Pareto fit |
| **Table 5.2** | `table_5_2` | *Evaluation Dimension 2: Resilience Under Disruption (IROPS Regimes)* | Ground stops: Model 3 decisive winner ($R_{\text{MASE}}=1.05$, TTR=2.8h) |
| **Table 5.3** | `table_5_3` | *Evaluation Dimension 3: Generalizability Across Facilities (Zero-Shot)* | Uncalibrated transfer (EWR $\to$ LGA): Model 1 decisive winner ($RTR=1.04$) |
| **Table 5.4** | `table_5_4` | *Master Asymmetric Trade-Off Matrix (H1 Synthesis)* | Strategic synthesis proving asymmetric trade-offs ($H_1$) |
| **Dual-Track** | `dual_track_policy` | *Dual-Track Operational Decision Playbook for Checkpoint Managers* | Tactical deployment decision tree & $q_{85}$ dynamic lane staffing |

### C. Appendix Tables
Located in `tables and figures/appendix/appendix_tables.xlsx`:
Contains all **30 canonical appendix tables** spanning Appendices A through N:
- **Appendix A**: `Table_A1_Assumptions` (Methodological Assumptions), `Table_A2_Delimitations` (Delimitations & Geographic Scope).
- **Appendix B**: `Table_B1_Paradigms` (Historical Modeling Paradigms), `Table_B2_Equations` (Master 20-Equation Registry).
- **Appendix C**: `Table_C1_Queuing` (Kingman Queuing Dynamics & Volatility Dispersion Metrics).
- **Appendix D**: `Table_D1_Partitioning` (Dataset Partitioning Design), `Table_D2_Demarcation` (Post-Pandemic Single Demarcation Specification & Structural Break Verification).
- **Appendix E**: `Table_E1_Top25_Census` (Top 25 Commercial Airport Census), `Table_E2_Cohort_Matrix` (12-Complex Cohort Census), `Table_E3_Selection_Contrasts` (Purposive Filtering Rationale).
- **Appendix F**: `Table_F1_Data_Feeds` (Federal Feed Registry), `Table_F2_Data_Threats` (Threats & Remediation Matrix), `Table_F3_Descriptive_Stats` (Post-ETL Summary Statistics).
- **Appendix G**: `Table_G1_Statistical_Tests` (Diebold-Mariano, Chow, and CUSUM Statistical Test Suite).
- **Appendix H**: `Table_H1_Feature_Dictionary` (24 OTP Operational Attributes), `Table_H2_Showup_Curves` (Empirical ACRP Report 40 Lead-Time Distributions).
- **Appendix I**: `Table_I1_Seasonal_Regimes` (4 Annual Volatility Regimes), `Table_I2_DOW_Archetypes` (3 DOW Demand Archetypes), `Table_I3_Airport_DOW` (Facility DOW Baseline Profiles).
- **Appendix J**: `Table_J1_Evaluation_Targets` (Governing Evaluation Triad Stated Targets), `Table_J2_Holdout_Benchmarks` (2025 Quarantined Holdout Results), `Table_J3_Hypothesis_Matrix` (Hypothesis 1 Evaluation Matrix).
- **Appendix K**: `Table_K1_Values_vs_Volatility` (Values versus Volatility Cross-Dataset Econometric Coupling).
- **Appendix L**: `Table_L1_Disruption_Resilience` (IROPS Shock Multipliers & TTR Metrics), `Table_L2_Lead_Lag_Dynamics` (Lead-Lag Asynchrony & Empty Checkpoint Fallacy Breakdown).
- **Appendix M**: `Table_M1_Routine_Accuracy` (Dimension 1 Synthesis), `Table_M2_Spatial_Transfer` (Dimension 3 Zero-Shot Metrics), `Table_M3_Asymmetric_Tradeoffs` (Master Trade-Off Matrix).
- **Appendix N**: `Table_N1_Archival_Hierarchy` (Cloud Warehouse Infrastructure & Exhibits Mapping).

---

## 3. Structural Harmonization & De-Duplication Protocol

1. **Elimination of Multiple COVID Demarcation Candidates**:
   - In accordance with thesis revisions, exploratory comparisons of "Candidate A vs. Candidate B" have been removed.
   - The thesis establishes **May 1, 2022** as the single authoritative post-pandemic demarcation baseline across all 44 months of empirical modeling, verified by Chow parameter stability ($F = 1.42, p = 0.18$) and CUSUM residual convergence.
2. **Elimination of Secondary Hypotheses**:
   - The thesis evaluates a single primary research hypothesis: **Hypothesis 1 ($H_1$ – Master Asymmetric Trade-Off Hypothesis)** across three operational dimensions (Robustness, Resilience, Generalizability).
3. **Consolidation of Standalone CSVs into Master Excel Workbooks**:
   - Redundant standalone CSV files whose contents are already stored as sheets within master Excel workbooks have been removed to eliminate clutter.
4. **Zero Edits to Word Documents**:
   - In strict compliance with repository safety policy, all Microsoft Word documents (`.docx`) in `thesis_docs/manuscripts/no-touch/` remain untouched.
