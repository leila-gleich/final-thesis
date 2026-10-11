# Master Recommendation Report: Appendix Cross-Referencing & Jargon Elimination
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)
**Document**: `finalthesisv1-rec.md`  
**Locations**: `thesis_docs/recommendations/finalthesisv1-rec.md` and repository root `finalthesisv1-rec.md`  
**Target Manuscript Suite**: Chapters I, II, III, IV, and V (`final-thesis-v1`)  
**Companion Documents**: [`Appendix v4.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Appendix%20v4.md), [`Appendix_Tables.xlsx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Appendix/Appendix_Tables.xlsx), [`AGENTS.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/AGENTS.md)  
**Date**: October 10, 2026  

---

## Executive Summary

This recommendation report provides a comprehensive, chapter-by-chapter blueprint to elevate the thesis manuscript (`final-thesis-v1`) to an authoritative, committee-ready master's thesis. A rigorous audit of the author's latest Microsoft Word revisions (`ChpI v4.docx`, `ChpII v5.docx`, `ChpIII v4.docx`, `ChpIV v5.docx`, and `ChpV v1.docx`) revealed two primary editorial priorities:

1. **Appendix Cross-Referencing Precision**: While the manuscript frequently refers to the Appendix, many citations are vague (e.g., *"see appendix for equation"* or *"detailed in the appendix"*), and several lettered references in Chapter IV have drifted from the authoritative 14-Appendix architecture (Appendices A through N). Specifically, Chapter IV currently refers to temporal demarcation as *Appendix B* (which is actually **Appendix D**), seasonality as *Appendix C* (which is **Appendix I**), cross-dataset correlations as *Appendix D* (which is **Appendix K**), and performance metric interpretation as *Appendix G* (which is **Appendix J**).
2. **Jargon Elimination & Plain Aviation Operational Language**: While overt pseudo-physics jargon (such as *Wiener-Hopf deconvolution*, *cyber-physical manifolds*, and *quiescent states*) has been successfully pruned, several academic, statistical, and computer science abstractions remain (e.g., *exogenous disruptions*, *zero-shot spatial transfer*, *show-up convolution*, *connecting passenger deflation*, *multi-carrier collinearity*, *hurdle formulations*). Replacing these terms with authentic commercial aviation, airline operations control, and TSA checkpoint security terminology makes the manuscript significantly more defensible and accessible to the ERAU graduate committee.

---

## Section 1: The Authoritative 14-Letter Appendix Architecture (Master Reference Key)

To ensure every in-text citation points to the exact letter and content, all references must align with the canonical 14-lettered Appendix suite compiled in `Appendix v4.md` and `thesis_docs/manuscripts/Appendix/Appendix_Tables.xlsx`:

| Appendix Letter | Formal Appendix Title | Primary Content & Methodological Purpose | Companion Analytical Tabs in `Appendix_Tables.xlsx` |
| :---: | :--- | :--- | :--- |
| **Appendix A** | *Delimitations, Research Limitations, and Methodological Assumptions* | Geographic boundaries (Top 25), institutional exclusions, unobserved concourse dwell times, missing flight-passenger linkage. | `methodological_assumptions`, `dataset_breakdown` |
| **Appendix B** | *Comparative Modeling Paradigms and Literature Equation Registry* | Theoretical foundations across 6 modeling paradigms; formal equation catalog (Kingman, Allen-Cunneen, Erlang-C, Tweedie). | `appendix_equations`, `modeling_paradigms` |
| **Appendix C** | *Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations* | Mathematical derivations of Kingman's heavy-traffic formula ($W_q \approx \frac{\rho}{1-\rho}\frac{C_a^2+C_s^2}{2}\frac{1}{\mu}$); volatility dispersion definitions ($\sigma_{\text{TSA}}$, $CV_{\text{TSA}}$). | `queuing_derivations`, `dispersion_formulas` |
| **Appendix D** | *Temporal Scope, Post-Pandemic Demarcation, and Dataset Partitioning* | Structural break tests (May 1, 2022 post-mask mandate equilibrium), CUSUM convergence, rolling Welch's $t$-tests, 2025 holdout protocol. | `temporal_demarcation`, `dataset_partitions` |
| **Appendix E** | *Four-Tier Purposive Filtering Pipeline, Nine-Airport Cohort Selection, and Airport Contrasts* | Macro/Meso/Micro/Factorial filtering steps; 9-airport / 12-complex cohort census (Table E.1); econometric tests for carrier isolation. | `Table_C_Summary_Descriptive`, `Top9_Master_Census` |
| **Appendix F** | *Multi-Source Aviation Data Feeds, ETL Architecture, and Data Hygiene Protocols* | Federal feed profiles (TSA FOIA, BTS OTP, T-100, DB1B); HPC pipeline flowchart; null handling and entity resolution. | `database_profiles`, `data_pipelines` |
| **Appendix G** | *Statistical Significance Testing: Diebold-Mariano, Chow, and CUSUM Foundations* | Econometric proofs of forecast error loss differentials; HAC long-run variance estimation; pairwise $DM$ test matrices. | `significance_tests`, `dm_loss_differentials` |
| **Appendix H** | *Feature Engineering Pipeline, ACRP Report 40 Show-Up Convolution, and DB1B Connecting Deflation* | Empirical passenger lead-time distributions ($t+1, t+2, t+3$); connecting passenger deflator formulas ($Q_t^{\text{adj}}$); cyclical time encodings. | `feature_engineering`, `pax_arrival_parameters` |
| **Appendix I** | *Seasonal Volatility Regimes, Day-of-Week Archetypes, and Diurnal Bimodal Dynamics* | 4 macro seasonal regimes (Table I.1); 3 DOW operational archetypes (Table I.2); bimodal diurnal flight bank curves. | `seasonal_regimes_summary`, `day_of_week_regimes_summary` |
| **Appendix J** | *Candidate Predictive Models, Operational Evaluation Triad Metrics, and Holdout Benchmarks* | Mathematical specifications of the 4 models; evaluation metric formulations ($R^2$, RMSE, MAE, MASE, Bias); certified holdout benchmarks. | `Table_4_10_Holdout_Benchmark`, `Table_4_11_Evaluation_Matrix` |
| **Appendix K** | *The Values versus Volatility Operational Coupling Across Temporal Horizons* | Empirical coupling regressions between flight departures and checkpoint volumes ($R^2 = 20.9\%$) vs. volatility ($r = +0.4373$); 84-cell interaction grid. | `otp_volatility`, `values_vs_volatility` |
| **Appendix L** | *Operational Disruption Dynamics, Lead-Lag Asynchrony, Resilience Mechanics, and the Empty Checkpoint Fallacy* | Micro-mechanics of convective delays; recovery time trajectories; mathematical breakdown of the Empty Checkpoint Fallacy under feedback. | `disruption_regimes`, `lead_lag_timeline` |
| **Appendix M** | *Dual-Track Operational Decision Playbook, Zero-Shot Spatial Transfer, and Dynamic Lane Staffing* | Airport manager's operational decision tree; uncalibrated cross-airport deployment rules; conformal quantile safety buffers ($q_{85}$). | `dual_track_policy`, `dynamic_staffing_bounds` |
| **Appendix N** | *Archival Data Storage Infrastructure, Directory Hierarchy, and Exhibits Catalog* | Cloud warehouse architecture; directory tree layout; mapping of all 30 analytical exhibits across repository hubs. | `backups_organization`, `diagrams_layout` |

---

## Section 2: Aviation Terminology Filter (Zero-Jargon Translation Dictionary)

To meet the highest standards of academic clarity and operational credibility, the following translation table replaces academic jargon, machine learning abstractions, and statistical shorthand with authentic aviation, airline operations center, and TSA checkpoint security terms:

| Academic / Lab Jargon | Authentic Aviation & Airport Operations Term | Operational Rationale |
| :--- | :--- | :--- |
| **Exogenous operational disruptions** | **External flight schedule disruptions (convective storms, FAA ground stops)** | Grounds abstract "shocks" in real-world weather and ATC ground delay programs. |
| **Stochastic passenger arrivals** | **Dynamic, variable passenger arrival patterns** | "Dynamic arrival patterns" is standard airport terminal planning terminology (ACRP Report 40). |
| **Zero-shot spatial transfer** | **Uncalibrated cross-airport deployment (cross-facility operational portability)** | Eliminates machine learning jargon; describes deploying a model to a new airport without local data. |
| **Lead-lag passenger show-up convolution** | **Aligning passenger checkpoint show-up curves with scheduled flight departure times** | Replaces mathematical "convolution" with intuitive operational alignment based on ACRP Report 40 lead times. |
| **Connecting passenger deflation (or deflator)** | **Connecting passenger discount (excluding airside transfer travelers)** | "Discounting connecting passengers" clearly explains the operational necessity of separating local origin passengers from transfer passengers. |
| **The Hub Disconnect** | **The Airside Transfer Gap (or Hub Connecting Passenger Gap)** | Preserves the conceptual breakthrough while highlighting that transferring passengers bypass landside security. |
| **Multi-carrier collinearity** | **Overlapping flight departure banks across shared airlines** | Explains why shared checkpoints cannot separate passenger flow: simultaneous airline flight waves confound individual passenger contributions. |
| **Zero-bounded / Hurdle formulation** | **Accounting for overnight checkpoint curfew periods (zero-passenger hours)** | Explains why specialized models are needed: commercial checkpoints close overnight (00:00–04:00), creating true zero-demand hours. |
| **Orthogonal factorial cohort** | **Balanced comparative sample of dedicated airline terminal complexes** | Communicates the scientific rigor of the 4x4 matrix (4 American, 4 Delta, 4 United complexes) without mathematical jargon. |
| **Metaheuristics / Algorithmic heuristics** | **Iterative optimization rules / Automated schedule solvers** | Translates computer science jargon into practical airline and airport planning terms. |
| **Tweedie Poisson hurdle regressor** | **Compound count-regression model tailored to overnight zero-screening periods** | Clarifies that the statistical technique handles low-volume and zero-throughput hours without predicting negative passengers. |
| **1-step error innovation feedback** | **Real-time prior-hour error correction ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$)** | Replaces time-series jargon with intuitive operational feedback from the checkpoint floor. |
| **Zero feedback compute latency** | **Requires no live checkpoint sensor feeds or real-time data integration** | Highlights the operational benefit of Model 2: it runs entirely on published airline data without expensive sensor infrastructure. |

---

## Section 3: Chapter-by-Chapter Audit & Exact Text Rewording Recommendations

### 3.1 Chapter I (Introduction)

#### Recommendation 1.1: Precise Appendix Citations for Delimitations and Limitations
* **Target Paragraphs**: Under `## Delimitations` and `## Limitations and Assumptions` in `chp1-intro.md`.
* **Current Text**:
  > *"These delimitations are detailed in the appendix."*  
  > *"These limitations are detailed in the appendix."*
* **Recommended Revision**:
  > *"A comprehensive operational catalog of research delimitations—including candidate airport selection thresholds, exclusive terminal focus, and the post-pandemic temporal scope—is provided in **Appendix A** (*Delimitations, Research Limitations, and Methodological Assumptions*)."*  
  > *"Methodological limitations, including unobserved passenger dwell time variability and the absence of linked flight-to-passenger boarding pass records, are formally detailed alongside sensitivity assumptions in **Appendix A**."*
* **Academic Rationale**: Replaces vague placeholder sentences with specific academic framing referencing the exact lettered appendix.

#### Recommendation 1.2: Jargon Refinement for Research Questions & Significance
* **Target Paragraphs**: Under `## Introduction` and `## Research Question`.
* **Current Text**:
  > *"Absorbing severe exogenous disruptions (hours with departure delays $\ge 45$ min or tactical cancellations $\ge 5$)..."*  
  > *"Porting its structural logic and parameters to new airport environments or distinct terminal geometries without local retraining (zero-shot spatial transfer)."*
* **Recommended Revision**:
  > *"Absorbing severe external flight schedule disruptions (such as convective weather ground stops with departure delays $\ge 45$ minutes or $\ge 5$ tactical cancellations)..."*  
  > *"Deploying its structural forecasting logic and parameter weights to new airport environments or unfamiliar terminal layouts without local recalibration (uncalibrated cross-airport deployment)."*
* **Academic Rationale**: Replaces mathematical abstractions (*exogenous disruptions*, *zero-shot spatial transfer*) with recognizable commercial aviation phenomena.

---

### 3.2 Chapter II (Review of the Relevant Literature)

#### Recommendation 2.1: Formatting Bold Paragraphs into APA 7th Level 2 and Level 3 Headings
* **Target Issue**: In `ChpII v5.docx`, section titles were formatted as unstyled bold text paragraphs (`Normal` style) rather than Word heading styles (`Heading 2` and `Heading 3`).
* **Resolved in `final-thesis-v1/chp2-litreview.md`**:
  * Level 2 (`##`):
    * `## Traditional Approaches and Operational Complexity`
    * `## From Analytical Queuing Models to Simulation Modeling and Real-Time Management`
    * `## Advanced Predictive Models and Machine Learning`
    * `## The Impact of Post-Pandemic Operational Volatility`
  * Level 3 (`###`):
    * `### Batch Arrival Dynamics and Flight Bank Synchronization`
    * `### Classical Queuing Theory: Volume Versus Volatility`
    * `### The "Values versus Volatility" Paradigm in Transportation Demand`
    * `### Micro-Simulation in Terminal Planning and Asset Allocation`
    * `### Operational Limitations of Micro-Simulation`
    * `### Statistical Time-Series Foundations and Linear Limitations`
    * `### Non-Linear Machine Learning: Deep Learning Versus Tree Ensembles`
    * `### Operational Limitations of Deep Neural Architectures`
    * `### From Passive Prediction to Behavioral Modeling and Active Control`
    * `### Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability`
    * `### Robustness to Procedural Volatility (Performance Under Perturbation)`
    * `### Resilience to Systemic Shocks (Capacity to Absorb and Recover from Disruption)`
    * `### Generalizability Across Environments (External Validity)`

#### Recommendation 2.2: Appendix Citations for Queuing Derivations and Paradigm Taxonomy
* **Target Paragraph 1**: In `### Classical Queuing Theory: Volume Versus Volatility`.
  * **Current Text**:
    > *"... (Kingman, 1961; Whitt, 1993; see Appendix for complete queuing derivations and mathematical formulas)."*
  * **Recommended Revision**:
    > *"... (Kingman, 1961; Whitt, 1993; see **Appendix C** for complete heavy-traffic queuing derivations, arrival variance formulations, and Kingman approximations)."*
* **Target Paragraph 2**: In `### Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability`.
  * **Current Text**:
    > *"... see Appendix for comparative paradigm taxonomy)."*
  * **Recommended Revision**:
    > *"... see **Appendix B** for the complete comparative modeling paradigm taxonomy and peer-reviewed equation registry)."*

#### Recommendation 2.3: Jargon Refinement in Chapter II
* **Target Terms**:
  * Replace *"metaheuristic search procedures"* $\to$ *"iterative schedule optimization techniques"*.
  * Replace *"stochastic passenger movements"* $\to$ *"unpredictable passenger arrival patterns"*.
  * Replace *"zero-shot generalizability"* $\to$ *"cross-facility operational portability"*.

---

### 3.3 Chapter III (Methodology)

#### Recommendation 3.1: Precision Appendix References for Methodology Components
* **Target Paragraph 1**: Under `### Research Hypothesis`.
  * **Current Text**:
    > *"Detailed hypothesis formulations, sub-hypotheses (H1a, H1b, H1c), formal mathematical evaluation thresholds, and Diebold-Mariano test specifications are compiled in the Appendix."*
  * **Recommended Revision**:
    > *"Formal hypothesis formulations, econometric evaluation thresholds, and Diebold-Mariano forecast accuracy test specifications are compiled in **Appendix G** (*Statistical Significance Testing*) and **Appendix J** (*Candidate Predictive Models and Evaluation Metrics*)."*
* **Target Paragraph 2**: Under `## Sources of Data`.
  * **Current Text**:
    > *"Secondary operational data are compiled from four primary authorized federal repositories summarized in Table 3.3 and the Appendix."*
  * **Recommended Revision**:
    > *"Secondary operational data are compiled from four primary authorized federal repositories summarized in Table 3.3 and detailed in **Appendix F** (*Multi-Source Aviation Data Feeds, ETL Architecture, and Data Hygiene Protocols*)."*
* **Target Paragraph 3**: Under `## Treatment of the Data`.
  * **Current Text**:
    > *"... with the exhaustive ETL data engineering protocol detailed in the Appendix."*
  * **Recommended Revision**:
    > *"... with the complete High-Performance Computing (HPC) data cleansing, dimension conformation, and relational alignment protocol detailed in **Appendix F**."*
* **Target Paragraph 4**: Under `### Temporal Scope and Boundary Definition`.
  * **Recommended Addition**:
    > *"The structural break evaluation, rolling Welch $t$-test convergence, and CUSUM statistical demarcation confirming the May 1, 2022 post-mask mandate equilibrium are detailed in **Appendix D**."*
* **Target Paragraph 5**: Under `### Four-Tiered Purposive Filtering Pipeline`.
  * **Recommended Addition**:
    > *"The complete facility inventory, terminal geometries, and carrier assignments for the resulting 9-airport experimental cohort are tabulated in **Appendix E** (Table E.1)."*

#### Recommendation 3.2: Figure 3 Callout & Image Integration
* **Target**: Paragraph P30 in `ChpIII v4.docx`.
* **Action Implemented**: Integrated explicit figure title, image link to `figures/ch03_methodology/Combined_Data_Pipeline_and_Funnel_Lifecycle.png`, and comprehensive APA 7 note explaining the sequential HPC pipeline.

---

### 3.4 Chapter IV (Findings and Discussion)

#### Recommendation 4.1: Critical Appendix Letter Re-Alignment
Chapter IV contained the largest number of misaligned appendix letters. The following corrections are essential:

| In-Text Location in Chapter IV | Current Text in Word Draft | Authoritative Target Appendix | Corrected Sentence for Manuscript |
| :--- | :--- | :--- | :--- |
| **Section 4.1: Initial EDA** | *"Appendix for details"* | **Appendix F** (Data Feeds & Schemas) | *"... across TSA checkpoint logs, BTS OTP, BTS T-100, and BTS DB1B/DB1C surveys (see **Appendix F** for complete data schemas and ingestion profiles)."* |
| **Section 4.1: Descriptive Stats** | *"See Appendix A for a detailed operational breakdown..."* | **Appendix F** & **Appendix J** (Data Warehouse & Holdout Stats) | *"See **Appendix F** for data warehouse descriptive statistics and **Appendix J** for holdout baseline metrics."* *(Appendix A is Delimitations).* |
| **Section 4.1: Temporal Boundaries** | *"Table 4.3a in Appendix B details the complete structural break evaluation..."* | **Appendix D** (Temporal Scope & Demarcation) | *"**Table D.1 in Appendix D** details the complete structural break evaluation, CUSUM statistics, and May 1, 2022 demarcation analysis."* *(Appendix B is Equation Registry).* |
| **Section 4.1: Defining Seasonality** | *"... (see Appendix C, including Table 4.4)..."* | **Appendix I** (Seasonal Volatility Regimes) | *"... (see **Appendix I**, including Table I.1 for annual regimes and Table I.2 for day-of-week demand archetypes)."* *(Appendix C is Queuing Derivations).* |
| **Section 4.1: Econometric Coupling** | *"Table 4.5 in Appendix D, which synthesizes the master cross-dataset econometric correlations."* | **Appendix K** (Values vs. Volatility Coupling) | *"**Table K.1 in Appendix K** (*The Values versus Volatility Operational Coupling*), which synthesizes the master cross-dataset econometric correlations."* *(Appendix D is Temporal Demarcation).* |
| **Section 4.2: Terminal Mixing** | *"... multi-carrier collinearity (see appendix for equation)..."* | **Appendix C** & **Appendix H** (Variance Formulations) | *"... overlapping multi-carrier flight banks (see **Appendix C** for arrival variance formulations and **Appendix H** for schedule dispersion equations)..."* |
| **Section 4.2: Carrier Isolation Tests** | *"... (see appendix for details and test statistics)."* | **Appendix E** & **Appendix G** (Filtering & Econometric Tests) | *"... terminal layout invariance test (see **Appendix E** and **Appendix G** for formal regression specifications and test statistics)."* |
| **Section 4.2: Subset vs. Top 25** | *"Table 4.7 in Appendix E, this comparative analysis..."* | **Appendix E** (Cohort Selection & Census) | *"**Table E.1 in Appendix E**, this comparative analysis confirms that the filtered cohort captures a representative cross-section..."* |
| **Section 4.2: DOW Archetypes** | *"Table 4.8 in the appendix, the nine facilities cluster..."* | **Appendix I** (Day-of-Week Demand Archetypes) | *"**Table I.2 in Appendix I**, the nine facilities cluster into three operational archetypes..."* |
| **Section 4.3: Lead-Lag Modeling** | *"See Appendix F for the complete regression specification..."* | **Appendix H** & **Appendix L** (Show-Up Curves & Asynchrony) | *"See **Appendix H** for passenger show-up convolution curves and **Appendix L** for lead-lag regression parameters across all horizons."* *(Appendix F is ETL).* |
| **Section 4.3: Metric Interpretation** | *"Please see Appendix G for details on how to interpret these standard operational performance criteria."* | **Appendix J** & **Appendix G** (Evaluation Metrics & Tests) | *"Please see **Appendix J** for operational interpretations of MASE, RMSE, and bias, and **Appendix G** for Diebold-Mariano test mechanics."* |

#### Recommendation 4.2: Restoration of Conformed Tables in Markdown
In `final-thesis-v1/chp4-results.md`, all callout placeholders were replaced with fully conformed APA 7th Edition Markdown tables synchronized directly with `results/manuscript_tables/`:
* **Table 4.1**: Master Post-ETL Multi-Source Data Foundation Census (5 data feeds, 42,062,039 conformed records).
* **Table 4.2**: Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse).
* **Table 4.6**: The Nine-Airport Experimental Cohort Specification (12 carrier-exclusive screening complexes).
* **Table 4.8**: Day-of-Week Mean Daily Passenger Throughput Across the Nine Cohort Airports.
* **Table 4.9**: Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Volume).
* **Table 4.10**: Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout).
* **Table 4.11**: Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models.

#### Recommendation 4.3: Visual Roadmap Integration (Figure 4.1)
Inserted an accessible Mermaid diagram illustrating the 4-phase architecture:
Section 4.1 (Initial EDA) $\to$ Section 4.2 (Data Filtering) $\to$ Section 4.3 (Model Development) $\to$ Section 4.4 (Model Results & Evaluation).

---

### 3.5 Chapter V (Discussion, Conclusions and Recommendations)

#### Recommendation 5.1: Reconstruction of OMML Mathematical Equations in Text
* **Target Issue**: In `ChpV v1.docx`, paragraph text had empty spaces where native Word OMML math equations were inserted.
* **Resolved in `final-thesis-v1/chp5-discussion.md`**: Fully extracted and formatted every equation into crisp KaTeX notation:
  * Section 5.3 (Robustness):
    * Target 1: Lowest $RMSE_{\text{routine}}$ to minimize absolute forecast error during standard flight waves.
    * Target 2: $MASE_{\text{routine}} \le 0.700$, demonstrating substantial error reduction relative to simple daily persistence.
    * Text: *"achieving $MASE_{\text{routine}} \le 0.700$ and $0.662$ respectively, compared to the daily persistence baseline ($MASE = 1.000$) and deterministic flight scheduling (Model 1, $MASE = 0.945$)... lowest routine RMSE (222.1 pax/hr), capturing 74.83% of holdout volatility variance ($R^2 = 0.7483$)... statistically decisive ($DM = 42.15$ and $DM = 48.72, p < 0.0001$)."*
  * Section 5.4 (Resilience):
    * Departure delays $\ge 45$ min or tactical cancellations $\ge 5$.
    * Disruption Error Multiplier ($R_{\text{MASE}} \approx 1.00$ or $R_{\text{RMSE}} \approx 1.00$).
    * Lowest $MASE_{\text{shock}}$, maintaining maximum operational accuracy during irregular operations.
    * Rapid Time-to-Recovery ($TTR < 4.0\text{h}$).
    * Text: *"Model 3 achieves $R_{\text{MASE}} = 1.05$ and $MASE_{\text{shock}} = 0.694$... recovery of 2.8 hours, easily beating the $TTR < 4.0\text{h}$ benchmark... recovering 5.0 hours faster than deterministic schedules ($TTR = 7.8\text{h}$) and 2.6 hours faster than pure machine learning ($TTR = 5.4\text{h}$)."*
  * Section 5.5 (Generalizability):
    * Relative Transfer Ratio ($RTR \approx 1.00$).
    * Change in MASE on Transfer ($\Delta MASE_{\text{transfer}} \le 10.0\%$).
    * Text: *"Model 1 achieves an $RTR$ of 1.04 ($RTR \approx 1.00$, target met) and a $\Delta MASE$ of only $+4.0\%$... In cross-cluster transfer (DTW $\to$ PHL), Model 1 achieves an $RTR$ of 1.003... Model 3 experiences an $RTR$ of 1.19 (failing target) and a $\Delta MASE$ surge of $+21.5\%$... Model 2 exhibits intermediate portability ($RTR = 1.08, \Delta MASE = +8.3\%$)."*

#### Recommendation 5.2: Embedding Tables 5.1 through 5.4 in APA 7 Format
* Replaced text table headers in Chapter V with complete conformed APA 7th Edition Markdown tables:
  * **Table 5.1**: Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models.
  * **Table 5.2**: Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption.
  * **Table 5.3**: Evaluation Dimension 3: Generalizability and Cross-Airport Spatial Transfer.
  * **Table 5.4**: Master Multi-Dimensional Model Evaluation Trade-Offs (Hypothesis 1 Summary).

#### Recommendation 5.3: Strategic Appendix Cross-References for Chapter V
Add the following high-value cross-references to give Chapter V strong scholarly grounding:
1. Under `### Connecting Passenger Shielding (The Hub Disconnect)`:
   > *"The econometric connecting passenger deflation formula ($Q_t^{\text{adj}}$) derived from the BTS DB1B ticket survey is detailed in **Appendix H**."*
2. Under `### Behavioral Invariance Across Terminal Layouts`:
   > *"Two-sample Kolmogorov-Smirnov test statistics confirming passenger flow invariance between physically separate terminals and walkway-connected complexes ($D = 0.032, p = 0.28$) are tabulated in **Appendix E**."*
3. Under `## Empirical Evaluation of Resilience Under Disruption`:
   > *"The operational mechanics of the Empty Checkpoint Fallacy—where unconstrained tree models overpredict screening queues during ground holds—are formally diagrammed in **Appendix L**."*
4. Under `## Implications and Recommendations for Predictive Forecasting in Airport Operations`:
   > *"The complete airport manager's decision tree and conformal quantile safety staffing bounds ($q_{85}$) are cataloged in **Appendix M** (*Dual-Track Operational Decision Playbook and Dynamic Lane Staffing*)."*

---

## Section 4. Verification & Synchronization Checklist

- [x] **Word Document Integrity (Policy 1.1)**: Exactly 0 Microsoft Word documents (`.docx`) modified, touched, or deleted. All source `.docx` files remain 100% read-only.
- [x] **Markdown Archiving & Compression**: Current chapter markdown files renamed as `v1` and compressed into `thesis_docs/manuscripts/archive/thesis_md_v1.zip`. Loose archived markdown drafts compressed into `superseded_loose_md_archive.zip`.
- [x] **New APA 7 Markdown Suite Deployed**: Generated `final-thesis-v1/` (`chp1-intro.md`, `chp2-litreview.md`, `chp3-methodology.md`, `chp4-results.md`, `chp5-discussion.md`, `final-thesis-v1.md`) with complete OMML math and APA 7 styling.
- [x] **Master Appendix Alignment**: Full 14-Appendix mapping (A through N) audited and cataloged with before/after rewording recommendations.
- [x] **Aviation Terminology Filter**: Complete jargon elimination guide formulated for all 5 chapters.
- [x] **Tabular Mathematical Parity (Policy 1.4)**: All 16 manuscript tables in CSV and multi-tab Excel workbooks verified and synchronized (`python3 -m unittest discover tests` passing 52/52 tests).
- [x] **Version Control & Provenance (Policy 1.3)**: `results/00_VERSION_CONTROL_AND_PROVENANCE.md` updated with release v4.53.
- [x] **Explicit Git Staging (Policy 1.6)**: Only explicitly modified files staged for commit.

---
*(End of Recommendation Report)*
