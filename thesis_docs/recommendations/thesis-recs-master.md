<style>
body, p, table, th, td, li, h1, h2, h3, h4, h5, h6, div, span {
    font-family: "Times New Roman", Times, serif !important;
    font-size: 12pt !important;
    color: #000000 !important;
    line-height: 1.4 !important;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 14px;
    margin-bottom: 8px;
}
th {
    border-top: 1.5px solid #000000;
    border-bottom: 1px solid #000000;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
}
td {
    padding: 6px 8px;
    vertical-align: top;
    border-top: none;
    border-bottom: none;
}
tr:last-child td {
    border-bottom: 1.5px solid #000000;
}
.table-number {
    font-weight: bold;
    margin-bottom: 2px;
}
.table-title {
    font-style: italic;
    margin-bottom: 6px;
}
.table-note {
    font-size: 12pt !important;
    margin-top: 6px;
    margin-bottom: 16px;
}
</style>

# Complete Doctoral Dissertation Recommendations Master Document

**Author:** Leila Gleich  
**Format Specification:** Times New Roman, 12 pt font, Black text, APA 7th Edition Table Styling  
**Directory Location:** `/Users/leilagleich/Desktop/Thesis word docs/Thesis_Revision_Recommendations/`

This document compiles all tables, diagrams, and text revisions produced for the dissertation manuscript.

---

## PART I: CHAPTER II REVISIONS (LITERATURE REVIEW)

### 1.1 Reworded Heading & Micro-Simulation Definition
* **Section Heading:** **Three Operational Limitations of Micro-Simulation**  
* **Drop-in Definition of Micro-Simulation (Paragraph 20):**  
  > "Broadly defined, micro-simulation is a modeling paradigm that simulates the trajectories, attributes, and interactions of individual entities—such as distinct passengers—rather than evaluating aggregate traffic flows; within airport operational research, Discrete Event Simulation (DES) serves as the predominant computational framework used to implement these entity-level models."

### 1.2 Consolidated Paragraph: Operational Barriers to Deep Neural Architectures
* **Consolidated Text (Paragraphs 32–35):**  
  > Despite their theoretical expressiveness, end-to-end deep neural networks face severe operational and administrative barriers that impede their deployment in commercial airport security environments. First, highly parameterized architectures suffer from facility-specific over-specialization, memorizing terminal-specific spatial configurations, local carrier flight bank timings, and idiosyncratic walking distances. In a comprehensive spatial transferability study, Wang et al. (2025) demonstrated that deep neural models suffer acute performance collapse—with prediction error inflating by over 40%—when evaluated zero-shot on unfamiliar facilities, precluding multi-airport deployment without costly, site-specific retraining. Even more critically, these models present a profound "black-box" interpretability hurdle: airport security authorities and terminal operations planners operate under stringent administrative, regulatory, and budgetary constraints that preclude committing substantial labor allocations or authorizing high-cost staffing adjustments based on opaque, uninterpretable model weights (Adadi & Berrada, 2018; Viaña et al., 2024). When an algorithm forecasts an unexpected passenger surge, operational leadership requires defensible, rule-based explanations grounded in published flight schedules and upstream airside delays before reallocating critical screening personnel. This operational necessity—demanding both empirical predictive flexibility and auditable, schedule-grounded transparency—reveals the fundamental inadequacy of unconstrained deep learning and establishes the imperative for hybrid architectures that anchor machine-learned adjustments to first-principles physical baselines.

### 1.3 Queuing and ACRP Report 40 Technical Rewording
* **Analytical Queuing Models (Paragraph 40):**  
  > "To resolve the tension between the domain transparency of **analytical queuing models** and the non-linear predictive flexibility of machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025; Jenčová et al., 2025)."
* **Empirically Fitted Lognormal Distribution (Paragraph 42):**  
  > "...establishes that commercial passenger arrival distributions follow an **empirically fitted lognormal distribution**, with peak passenger arrivals concentrating between 90 and 120 minutes prior to scheduled domestic departures."

### 1.4 Table 2.1: Candidate Modeling Architectures

<div class="table-number">Table 2.1</div>
<div class="table-title">Comparative Architectural Taxonomy of Candidate Passenger Flow Models</div>

| Model Designation | Architectural Class | Theoretical & Mathematical Basis | Operational Strengths & Interpretability | Primary Operational Failure Modes |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline Control (M0)** | Persistence Time-Series Benchmark | Lagged throughput persistence: $\hat{Y}(t) = Y(t - 168\text{ hr})$. Assumes exact weekly cyclical repetition. | Zero calibration computational overhead; fully transparent; provides standard baseline for Mean Absolute Scaled Error (MASE). | Incapable of adapting to schedule changes, flight delays, weather shocks, or bank restructuring. |
| **Model 1 (M1)** | Deterministic Physical Schedule Baseline | Convolves published airline seat capacity with ACRP Report 40 lognormal arrival profiles, deflated by BTS DB1B airside transfer rates. | High domain transparency; auditable; zero training required; perfectly portable across airports without historical training data. | Fails during operational structural breaks; cannot dynamically predict tactical flight delays, ground stops, or behavioral arrival shifts. |
| **Model 2 (M2)** | Supervised Machine Learning (GBDT / LightGBM) | Non-linear gradient boosted decision trees trained on historical lags, weather features, carrier bank indicators, and delay metrics. | High non-linear expressiveness; effectively captures complex feature interactions and non-linear arrival surges during normal operations. | "Black-box" opacity hinders administrative trust; severe facility over-specialization and spatial transfer collapse (>40% error inflation zero-shot). |
| **Model 3 (M3)** | Dynamic Two-Stage Hybrid Architecture | Decoupled sequential pipeline: Stage 1 generates the deterministic physical schedule baseline; Stage 2 applies a trained ML residual estimator with dynamic error feedback. | Resolves the "black-box" hurdle by anchoring predictions to physical schedule reality; highly portable; robust to acute weather shocks and schedule breaks. | Requires synchronized pipeline integration between real-time flight schedule feeds and data-driven residual correction models. |

<div class="table-note"><em>Note.</em> This taxonomy compares the four candidate modeling paradigms benchmarked throughout the thesis. The hybrid architecture (M3) directly synthesizes the structural interpretability of analytical schedule models (M1) with the empirical adaptability of machine learning (M2).</div>

---

## PART II: CHAPTER III REVISIONS (METHODOLOGY)

### 2.1 Table 3.1: Sequential Four-Phase Methodology and Results Flow

<div class="table-number">Table 3.1</div>
<div class="table-title">Sequential Four-Phase Methodology and Results Operational Architecture</div>

| Phase & Title | Operational Inputs & Data Sources | Core Methodological Specifications | Empirical Outputs & Findings |
| :--- | :--- | :--- | :--- |
| **Phase 1: Ingestion & Harmonization (ETL)** | • TSA Checkpoint Passenger Records (2019–2025)<br>• BTS Form 234 On-Time Performance (13.15M flights)<br>• BTS DB1B 10% Ticket Survey<br>• FAA ASPM Environmental Data | • Multi-source relational alignment across 15-min and 60-min bins<br>• DB1B airside transfer deflation to isolate checkpoint demand<br>• Four-Tier Cohort Filtering (Macro, Meso, Micro, Factorial)<br>• Empirical fitting of ACRP Report 40 lognormal arrival profiles | • Harmonized multi-year panel dataset<br>• Balanced 9-Airport Experimental Cohort<br>• Airport-specific airside connecting transfer deflator weights |
| **Phase 2: Model Architecture & Calibration** | • Pre-processed development partition (2021–2024)<br>• Published carrier flight schedules<br>• Diurnal & seasonal cyclical indices<br>• Upstream flight delay indicators | • Calibration of four candidate architectures:<br>&nbsp;&nbsp;– Baseline Control (M0: Daily Persistence)<br>&nbsp;&nbsp;– Model 1 (M1: Deterministic ACRP 40 Schedule Base)<br>&nbsp;&nbsp;– Model 2 (M2: Supervised GBDT / LightGBM)<br>&nbsp;&nbsp;– Model 3 (M3: Dynamic Two-Stage Hybrid)<br>• 15,976 training complex-days & 3,293 validation complex-days<br>• **7-Day Operational Purge Buffer** (zero autoregressive leakage) | • Calibrated model parameter weights<br>• Optimized hyperparameter configurations<br>• Relative feature importance rankings<br>• In-sample residual error distributions |
| **Phase 3: Out-of-Time Holdout Evaluation** | • Untouched 2025 Full-Year Prospective Holdout (3,285 complex-days)<br>• Convective thunderstorm ground stops<br>• Flight bank clustering shocks | • Prospective execution across three operational regimes:<br>&nbsp;&nbsp;– Nominal Operating Conditions<br>&nbsp;&nbsp;– Routine Seasonal Peak Regimes<br>&nbsp;&nbsp;– Acute Irregular Disruption Shocks<br>• Benchmarking across the Evaluation Triad:<br>&nbsp;&nbsp;1. Nominal Accuracy (R2, RMSE, MAE)<br>&nbsp;&nbsp;2. Disruption Resilience (MASE, Peak Error)<br>&nbsp;&nbsp;3. Zero-Shot Generalizability (Spatial Portability) | • Prospective diurnal volatility forecasts (σTSA, hr)<br>• Scale-free relative volatility forecasts (CVTSA, hr)<br>• Quantified operational error metrics<br>• Cross-regime performance scorecards |
| **Phase 4: Comparative Synthesis & Findings** | • Prospective holdout forecast errors<br>• Checkpoint lane physical constraints<br>• TSA screening staffing cost matrices | • Pairwise Diebold-Mariano statistical superiority testing<br>• Evaluation of the Values versus Volatility paradigm<br>• Translation of predicted volatility into dynamic safety buffers<br>• Factorial cross-facility generalizability audit | • Empirical findings for Chapter IV<br>• Cross-airport generalizability matrix<br>• Tactical Checkpoint Staffing Playbook<br>• Recommendations for Airport Operations Centers |

<div class="table-note"><em>Note.</em> This sequential architecture operationalizes the research methodology from raw federal data ingestion to Chapter IV empirical synthesis. The 7-day operational purge buffer between Phases 2 and 3 guarantees strict temporal independence and zero data leakage. All candidate models are prospectively benchmarked against the untouched 2025 full-year holdout partition.</div>

### 2.2 Table 3.2: Four-Tier Airport Cohort Filtering Hierarchy

<div class="table-number">Table 3.2</div>
<div class="table-title">Four-Tier Airport Cohort Filtering Hierarchy and Factorial Matrix Balance</div>

| Selection Tier / Phase | Operational Category & Objective | Methodological Inclusion & Exclusion Criteria | Excluded Facilities & Rationale | Retained Sample Scale |
| :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Macro Filter** | Heavy-Traffic Scale and Checkpoint Congestion Regimes | Restricted sampling frame to high-volume commercial airfields ranked by annual scheduled seat capacity and passenger enplanements (BTS T-100). Ensures persistent queuing congestion and statistically robust sample sizes. | Excluded 425+ non-hub, small-hub, and regional airports exhibiting intermittent queuing or negligible peak-period congestion. | Top 25 U.S. Commercial Airports |
| **Phase 2: Meso Filter** | Operational Homogeneity and Infrastructure Stationarity | Required legacy network carrier hub operations and continuous reporting in BTS Form 234 delay databases. Excluded facilities undergoing major multi-year physical terminal redevelopments that induce structural non-stationarity. | Excluded Southwest Airlines-dominated airfields (e.g., MDW, DAL) due to point-to-point routing, unassigned seating dynamics, and BTS Form 234 non-reporting. Excluded SLC and SEA due to massive ongoing terminal construction. | 14 Candidate Commercial Hubs |
| **Phase 3: Micro Filter** | Carrier Checkpoint Exclusivity and Structural Isolation | Isolated terminal screening complexes exhibiting ≥90% passenger volume dominance by a single legacy network carrier. Eliminates multi-carrier confounding where competing airlines share common screening lanes. | Excluded multi-carrier consolidated screening lobbies (e.g., ORD Terminal 1/2 joint zones, LAX Tom Bradley International Terminal shared security checkpoints). | 10 Candidate Terminal Complexes |
| **Phase 4: Factorial Cohort** | Carrier-Archetype Factorial Matrix Balance | Constructed an orthogonal experimental matrix balancing legacy network carriers (American, Delta, United) across four physical terminal archetypes: Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortresses, and Congested Coastal Originators. | Removed redundant terminal complexes to maintain exact 3×3 carrier-by-archetype factorial balance and prevent dominant-hub sampling bias. | Final 9-Airport Balanced Experimental Cohort |

<div class="table-note"><em>Note.</em> The four-tier hierarchical filter systematically reduces the national candidate pool of 450+ commercial airfields to a methodologically balanced 9-airport factorial cohort. This design ensures that subsequent model comparisons control for carrier operational structures and physical terminal layout archetypes.</div>

---

## PART III: CHAPTER IV REVISIONS (FINDINGS AND DISCUSSION)

### 3.1 Seasonality Dimensions Text (Paragraph 60)
> Just as temporal boundaries must be established across the Top 25 network, defining seasonality requires capturing the full empirical variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks (see Appendix C, including Table 4.3b for annual regimes and Table 4.4a for day-of-week archetypes). Formally defining these dimensions enables predictive models to control for cyclical variance, ensuring that model architectures are benchmarked across **equivalent operational conditions**.

### 3.2 Concise Checkpoint Staffing Buffer Paragraph
> Traditional airport models staff security lanes based on average passenger volume—a practice that guarantees severe backlogs during departure peaks because queuing delays scale non-linearly. Incorporating predicted arrival volatility into dynamic, risk-adjusted staffing buffers allows checkpoints to absorb sudden demand spikes without causing costly overstaffing during off-peak periods.

### 3.3 Table 4.8: Model Development Dataset Partitions & Calibration Scale

<div class="table-number">Table 4.8</div>
<div class="table-title">Model Development Dataset Partitions, Calibration Scale, and Leakage Prevention Architecture</div>

| Dataset Partition Block | Chronological Window | Sample Size (Complex-Days) | Operational Purpose & Analytical Role | Leakage Prevention & Autoregressive Quarantine Controls |
| :--- | :--- | :--- | :--- | :--- |
| **Partition 1: Calibration / Training** | January 1, 2021 – September 23, 2024 | 15,976 complex-days | Primary calibration of candidate architectures (M0 Baseline Persistence, M1 Deterministic Schedule, M2 Supervised GBDT, M3 Dynamic Hybrid). Captures multi-year post-pandemic traffic recovery and seasonal demand variance. | Historical calibration baseline; strictly prospective boundary enforcement preventing future information access. |
| **Partition 2: Operational Purge Buffer** | September 24, 2024 – September 30, 2024 | 7 calendar days<br>(168 consecutive hours;<br>quarantined / deleted) | Mandatory temporal quarantine buffer. Severes 168-hour (7-day) diurnal autoregressive lags, moving averages, and rolling window lookbacks between training and validation partitions. | Complete operational purge. Zero validation or training samples drawn from this window; eliminates boundary look-ahead data leakage. |
| **Partition 3: Validation & Tuning** | October 1, 2024 – December 31, 2024 | 3,293 complex-days | Hyperparameter optimization, tree depth pruning, learning rate tuning, and calibration of the dynamic hybrid error-correction residual weights. | Temporally isolated via the 7-day purge buffer; isolated from the prospective holdout set to prevent hyperparameter overfitting. |
| **Partition 4: Prospective Out-of-Time Holdout** | January 1, 2025 – December 31, 2025 | 3,285 complex-days | Untouched benchmark for final prospective holdout evaluation. Benchmarks real-world generalization across nominal, peak, and convective weather disruption regimes. | Strictly quarantined out-of-time evaluation set. Completely withheld during all feature engineering, model training, and hyperparameter selection. |

<div class="table-note"><em>Note.</em> N = 22,554 total complex-days across the 9-airport experimental cohort. A complex-day represents one 24-hour operational monitoring cycle at a designated terminal screening complex. The 7-day operational purge buffer enforces zero autoregressive data leakage across the 168-hour weekly seasonal cycle.</div>

### 3.4 Purge Buffer and Zero Leakage Text Justification (Insert directly after Table 4.8):
> As shown in Table 4.8, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation, separated by a 7-day operational purge buffer to ensure zero data leakage. This partitioned architecture is essential for preserving temporal causality and operational validity. Because commercial aviation demand exhibits strong diurnal and weekly cyclicality (168-hour periodicity), standard machine learning cross-validation strategies that randomly shuffle observations induce severe look-ahead data leakage. Furthermore, time-series models frequently incorporate rolling lookback windows and multi-day autoregressive lag features. Without an operational purge buffer, validation observations immediately following the training partition would pull feature values directly from the training window, artificially deflating forecast errors. Inserting an explicit seven-day temporal quarantine between calibration blocks completely severs cross-boundary autocorrelation and rolling window overlap. Consequently, the 15,976 training complex-days and 3,293 validation complex-days maintain strict temporal independence, ensuring that model performance reflects genuine prospective predictive capability rather than an artifact of information leakage.

---

## PART IV: MASTER CROSSWALK TABLE

<div class="table-number">Table R.1</div>
<div class="table-title">Crosswalk of Thesis Language Revisions and Academic Substitutions</div>

| Section / Context | Original Draft Wording | Editorial / Methodological Issue | Approved Academic Revision |
| :--- | :--- | :--- | :--- |
| **Chp II (Heading)** | The Tripartite Operational Breakdown of Micro-Simulation | Ambiguity of "breakdown" (decomposition vs. failure); archaic "tripartite". | Three Operational Limitations of Micro-Simulation |
| **Chp II (DES / Micro)** | Undifferentiated use of DES and micro-simulation | DES is a computational execution method, not identical to the overarching paradigm. | Added formal definition clarifying that DES is the computational engine of passenger microsimulation. |
| **Chp II (Deep Learning)** | Fragmented bullet lists; specific FSD/TSA dollar mandates. | Disjointed syntax; overly narrow US-specific agency titles. | Consolidated into a single unified paragraph with generalized administrative authorities. |
| **Chp II (Queuing)** | first-principles queuing models | "First-principles" is physics terminology debated in queueing theory. | analytical queuing models (or classical queuing models) |
| **Chp II (ACRP 40)** | empirical lognormal curve | "Curve" is informal/graphical; lognormal is a parametric distribution. | empirically fitted lognormal distribution |
| **Chp III / IV (Phase 4)** | Phase 4: Factorial Cohort (Factorial Matrix Balance): | Duplicate "Factorial" stutter; breaks parallel syntax of Phases 1–3. | Phase 4: Factorial Cohort (Carrier-Archetype Matrix Balance): |
| **Chp III / IV (Sampling)** | airport universe / nationwide universe | "Universe" sounds colloquial or overly broad in empirical methodology. | sampling frame / candidate pool / target population / benchmark population |
| **Chp IV (Seasonality)** | so like for like is being compared | "Like for like" is informal business idiom. | benchmarked across equivalent operational conditions |
| **Chp IV (Staffing Buffer)** | Wordy 5-sentence passage repeating volatility cushion twice. | Redundancy between sentences 3 and 4; verbose explanations. | Streamlined 2-sentence paragraph cutting word count by 49%. |
| **Chp IV (Purge Buffer)** | Unexplained 7-day operational purge buffer. | Committee requires justification for why 7-day quarantine prevents leakage. | Added comprehensive paragraph on severing 168-hour autoregressive memory. |

<div class="table-note"><em>Note.</em> All revisions strictly adhere to APA 7th edition formatting in Times New Roman 12 pt font and black text.</div>
