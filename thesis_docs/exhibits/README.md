# Thesis Manuscript Exhibits Directory (Chapters I–III)
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Directory Purpose**: This directory provides the intuitive, canonical home for all conceptual frameworks, theoretical process diagrams, data schemas, and research design exhibits for **Chapter I (*Introduction*)**, **Chapter II (*Literature Review*)**, and **Chapter III (*Methodology*)**. 
>
> **Separation of Concerns**:
> * **`thesis_docs/exhibits/`** (this directory): Pre-empirical research design, theoretical frameworks, data pipeline schemas, and sample selection exhibits.
> * **[`results/figures/`](../../results/figures/) & [`results/tables/`](../../results/tables/)**: Empirical findings, out-of-time model benchmark evaluations, and econometric hypothesis tests for Chapter IV (*Results*) and Chapter V (*Discussion*).
> * **[`figures/04_Appendix_and_Reference/`](../../figures/04_Appendix_and_Reference/)**: Dedicated reference profiles, DB1B hierarchies, and backup manifests preserved strictly for the Appendix.

---

## 1. Chapter I: Introduction (`ch01_intro/`)

| Exhibit Name | File Asset | Manuscript Insertion Point | Scope & Theoretical Function |
| :--- | :--- | :--- | :--- |
| **Figure 1.1** | `models and tests.png` / `models_and_tests.csv` | After Hypothesis 1 ($H_1$) statement | **Asymmetric Trade-Off Evaluation Triangle**: Schematically depicts that no single model is universally dominant across all operational dimensions (Model 3 wins Resilience, Model 1 wins Generalizability, Model 2 wins Routine Pareto Efficiency). |
| **Table 1.1** | Derived from `models_and_tests.csv` | Following Section `## Research Questions` | **The 3-Model Candidate Evaluation Suite & Baseline Control**: Establishes the 3 distinct modeling paradigms (Deterministic ACRP 40, Supervised ML Regressor, Dynamic Two-Stage Hybrid) and the empirical baseline control (Daily Persistence Benchmark). |
| **Table 1.2** | `Data Sample Profile.png` / `data_sample_profile.csv` | Within Section `## Delimitations` | **Scope, Delimitations & Federal Data Foundation**: Summarizes the 4 federal data repositories (TSA FOIA, BTS OTP, BTS T-100, BTS DB1B) covering 42,062,039 conformed records from 2019–2025. |
| **Reference** | `Inclusion of top 25 network approach.png` / `inclusion_of_top_25_network_approach.csv` | Section `## Delimitations` | **Top 25 Network Approach Rationale**: Contextualizes the macro 25-airport national hub network against the purposive 9-airport experimental cohort. |

---

## 2. Chapter II: Literature Review (`ch02_lit_review/`)

| Exhibit Name | File Asset | Manuscript Insertion Point | Scope & Theoretical Function |
| :--- | :--- | :--- | :--- |
| **Figure 2.1** | `pax stochastic arrival.png` / `passenger_stochastic_arrival_parameters.csv` | Under `## Traditional Approaches` | **The Checkpoint Tipping Point (Kingman's Heavy-Traffic Curve)**: Demonstrates that queue wait times escalate quadratically with arrival burstiness ($C_a^2$) under Kingman's formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2+C_s^2}{2} \frac{1}{\mu}$) as server utilization $\rho \to 1.0$. |
| **Table 2.1** | `exploratory metric criteria research .png` / `exploratory_metric_criteria_research.csv` | Following `## Simulation Modeling` | **Comparative Synthesis of Airport Flow Paradigms**: Contrasts historical modeling mechanisms (pure physics, queuing, time-series, supervised ML) across data latency, operational fidelity, and shock vulnerabilities. |
| **Figure 2.2** | `Model walk through.png` / `model_walkthrough_architecture.csv` | Following `## Hybrid Architectures` | **Two-Stage Sequential Hybrid Architecture**: Schematically illustrates Stage 1 (recurring flight bank schedule cycles) feeding baseline predictions into Stage 2 (live recursive error innovation feedback $e_{t-1}$). |
| **Framework** | `clusting and connecting paradox.png` / `clustering_and_connecting_paradox.csv` | Section `## Passenger Flow Dynamics` | **The Connecting Passenger Paradox**: Illustrates the hub disconnect where airside connecting passenger transfers bypass landside TSA checkpoints, requiring DB1B coupon deflation. |
| **Framework** | `otp & tsa.png` / `otp_and_tsa_volume_coupling.csv` | Section `## Flight Delays and Checkpoints` | **TSA & OTP Volume Coupling vs. Volatility**: Contrasts the decoupling of raw volume counts with the tight coupling of departure delay volatility and throughput volatility. |
| **Framework** | `OTP volatility.png` / `otp_volatility.csv` | Section `## Volatility Dynamics` | **Flight Departure Delay Volatility Regimes**: Formalizes delay standard deviation and coefficient of variation ($CV_{\text{delay}}$) metrics. |

---

## 3. Chapter III: Methodology (`ch03_methodology/`)

### A. Figures (`ch03_methodology/figures/`)
* **Figure 1**: `models and tests.png` — *Forecasting Model Family Comparison* (Word review draft Callout P18).
* **Figure 2**: `Evaluation Metric Definition.png` — *Evaluation Metric Definitions & Mathematical Formulas* (Callout P56).
* **Figure 3**: `Combined_Data_Pipeline_and_Funnel_Lifecycle.png` — *Design and Procedure Phases (4-Phase Research Pipeline)* (Callout P61).
* **Figure 4**: `Airport selection strategy document.png` — *Sample Framework for Terminal Capacity & Checkpoint Configuration* (Callout P101).
* **Figure 5**: `airport clusters.png` — *Airport Operational Archetypes & Terminal Configurations* (Callout P103).
* **Supporting Diagrams**: `physical transfer lead lag time.png`, `metrics.png`, `Control and test process.png`, `checkpoint examples.png`, `Combined_Data_Threats_and_Remediation_Matrix.png`, `TSA Schema.png`, `t100 schema.png`, `imputed defs.png`, `Power of 9 airports.png`, `post-pandemic justification.png`.

### B. Tables (`ch03_methodology/tables/`)
* `airport_clusters.csv`: Operational clustering archetypes across candidate airfields.
* `airport_selection_strategy_document.csv`: Four-tiered purposive filtering pipeline and causal identification criteria.
* `post_pandemic_justification.csv`: Temporal demarcation justification (May 1, 2022 to December 31, 2025 boundary).
* `power_of_9_airports.csv`: Factorial representation of the 9-airport, 12-complex experimental cohort.
* `combined_data_pipeline_and_funnel_lifecycle.csv`: Complete data lifecycle from raw ingestion to conformed star-schema tables.
* `combined_data_threats_and_remediation_matrix.csv`: Methodological data threats, bias vulnerabilities, and engineering remediations.
* `imputed_defs.csv`: Missing data imputation protocols and boundary rules.
* `checkpoint_examples.csv`: Dedicated carrier checkpoint exclusivity configurations.
* `t100_schema.csv` & `tsa_schema.csv`: Conformed star-schema data models.
* `control_and_test_process.csv`: Operational test execution protocols.
* `evaluation_metric_definition.csv`: Formal definitions of RMSE, MASE, $R_{\text{MASE}}$, TTR, RTR, and Diebold-Mariano ($DM$).
* `physical_transfer_lead_lag_timeline.csv`: ACRP Report 40 passenger arrival lead-lag convolution structure ($t+1, t+2, t+3$).
* `probabilistic_and_selection_metrics.csv`: Dual-track model selection metrics.

### C. Multi-Tab Companion Workbooks (`ch03_methodology/workbooks/`)
* `01_Sample_and_Airport_Selection.xlsx`: Multi-tab APA 7 workbook consolidating all sample selection and cluster specification tables.
* `02_Data_Pipelines_and_Threats.xlsx`: Multi-tab APA 7 workbook consolidating ETL data pipeline and threats tables.
* `03_Modeling_and_Evaluation.xlsx`: Multi-tab APA 7 workbook consolidating forecasting models and evaluation metric specifications.

---

## 4. Provenance & Maintenance

* All tabular assets are stored in standard comma-separated values (`.csv`) for version control transparency.
* High-resolution diagrams (`.png`) are styled to match thesis aesthetic standards and APA Style (7th ed.).
* To re-build the multi-tab Excel workbooks, execute:
  ```bash
  python3 src/analysis/generate_figures_tables_excel.py
  ```
