# Chapter III: Methodology Exhibits, Figures & Companion Workbooks
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Research design, empirical schemas, purposive filtering progression, experimental cohort specifications, and mathematical evaluation frameworks for **Chapter III (*Methodology*)**.

---

### Master Methodology Figures & Companion Data Tables

| Figure Callout ID | Visual Graphic (`.png`) | Companion Data (`.csv`) | Word Callout | Operational Scope & Methodological Function |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 1** | `models and tests.png` | `models_and_tests.csv` | Callout P18 | **Forecasting Model Family Comparison**: Architectural schematic comparing Baseline Control, Model 1 (ACRP 40 convolution), Model 2 (supervised ML regressor), and Model 3 (sequential hybrid). |
| **Figure 2** | `Evaluation Metric Definition.png` | `evaluation_metric_definition.csv` | Callout P56 | **Evaluation Metric Definitions**: Mathematical specification of RMSE, MASE, $R_{\text{MASE}}$, TTR, RTR, and Diebold-Mariano ($DM$). |
| **Figure 3** | `Combined_Data_Pipeline_and_Funnel_Lifecycle.png` | `combined_data_pipeline_and_funnel_lifecycle.csv` | Callout P61 | **Design and Procedure Phases**: Four-phase experimental research progression (Phase 1: ETL & Data Hygiene $\to$ Phase 2: Model Development $\to$ Phase 3: Holdout Evaluation $\to$ Phase 4: Statistical Validation). |
| **Figure 4** | `Airport selection strategy document.png` | `airport_selection_strategy_document.csv` | Callout P101 | **Sample Framework for Terminal Capacity & Checkpoints**: Terminal architectural framework detailing physical screening lanes, checkpoint queuing snakes, dedicated carrier concourses, and spatial aggregation. |
| **Figure 5** | `airport clusters.png` | `airport_clusters.csv` | Callout P103 | **Airport Operational Archetypes & Terminal Configurations**: Four-cluster PCA/K-Means matrix categorizing candidate Top 25 airfields across transfer ratio, international share, flight scale, and delay dispersion. |

---

### Supporting Methodological Frameworks & Schemas

| Visual Diagram (`.png`) | Companion Data (`.csv`) | Topic & Methodological Rationale |
| :--- | :--- | :--- |
| `checkpoint examples.png` | `checkpoint_examples.csv` | Dedicated carrier checkpoint exclusivity configurations and normalization. |
| `Combined_Data_Threats_and_Remediation_Matrix.png` | `combined_data_threats_and_remediation_matrix.csv` | Methodological data threats, bias vulnerabilities, and engineering remediations. |
| `Control and test process.png` | `control_and_test_process.csv` | Operational test execution protocols (pure signal vs noisy shared design). |
| `imputed defs.png` | `imputed_defs.csv` | Missing data imputation protocols and boundary rules. |
| `metrics.png` | `probabilistic_and_selection_metrics.csv` | Probabilistic scoring rules (CRPS, PICP) and information criteria (AIC, BIC). |
| `physical transfer lead lag time.png` | `physical_transfer_lead_lag_timeline.csv` | ACRP Report 40 passenger arrival lead-lag convolution structure ($t+1, t+2, t+3$). |
| `post-pandemic justification.png` | `post_pandemic_justification.csv` | Temporal demarcation justification (May 1, 2022 to December 31, 2025 boundary). |
| `Power of 9 airports.png` | `power_of_9_airports.csv` | Factorial representation of the 9-airport, 12-complex experimental cohort. |
| `t100 schema.png` | `t100_schema.csv` | BTS Form 41 Schedule T-100 Segment Statistics conformed star schema. |
| `TSA Schema.png` | `tsa_schema.csv` | TSA FOIA Hourly Screening Throughput conformed star schema. |

---

### Multi-Tab Companion Excel Workbooks (`workbooks/`)

1. **`01_Sample_and_Airport_Selection.xlsx`**: Multi-tab APA 7 workbook consolidating all sample selection and cluster specification tables.
2. **`02_Data_Pipelines_and_Threats.xlsx`**: Multi-tab APA 7 workbook consolidating ETL data pipeline and threats tables.
3. **`03_Modeling_and_Evaluation.xlsx`**: Multi-tab APA 7 workbook consolidating forecasting models and evaluation metric specifications.
