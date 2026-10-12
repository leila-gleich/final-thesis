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

# Master Compilation of Approved Text Revisions and Crosswalk Tables

This document compiles all approved text revisions, exact replacement paragraphs, and academic substitutions across Chapters II, III, and IV.

---

## 1. Chapter II Revisions (Review of the Relevant Literature)

### Revision A: Micro-Simulation Heading & Definition (Paragraphs 20–22 in `ChpII v4.docx`)
* **Replaced Heading:** `Three Operational Limitations of Micro-Simulation` *(replaces "The Tripartite Operational Breakdown of Micro-Simulation")*
* **Drop-in Definition of Micro-Simulation (for Paragraph 20):**
  > "Broadly defined, micro-simulation is a modeling paradigm that simulates the trajectories, attributes, and interactions of individual entities—such as distinct passengers—rather than evaluating aggregate traffic flows; within airport operational research, Discrete Event Simulation (DES) serves as the predominant computational framework used to implement these entity-level models."

### Revision B: Operational Barriers to Deep Neural Architectures (Consolidated Single Paragraph, Paragraphs 32–35)
* **Consolidated Paragraph (with generalized administrative authorities, black-box terminology, and transition to hybrid models):**
  > Despite their theoretical expressiveness, end-to-end deep neural networks face severe operational and administrative barriers that impede their deployment in commercial airport security environments. First, highly parameterized architectures suffer from facility-specific over-specialization, memorizing terminal-specific spatial configurations, local carrier flight bank timings, and idiosyncratic walking distances. In a comprehensive spatial transferability study, Wang et al. (2025) demonstrated that deep neural models suffer acute performance collapse—with prediction error inflating by over 40%—when evaluated zero-shot on unfamiliar facilities, precluding multi-airport deployment without costly, site-specific retraining. Even more critically, these models present a profound "black-box" interpretability hurdle: airport security authorities and terminal operations planners operate under stringent administrative, regulatory, and budgetary constraints that preclude committing substantial labor allocations or authorizing high-cost staffing adjustments based on opaque, uninterpretable model weights (Adadi & Berrada, 2018; Viaña et al., 2024). When an algorithm forecasts an unexpected passenger surge, operational leadership requires defensible, rule-based explanations grounded in published flight schedules and upstream airside delays before reallocating critical screening personnel. This operational necessity—demanding both empirical predictive flexibility and auditable, schedule-grounded transparency—reveals the fundamental inadequacy of unconstrained deep learning and establishes the imperative for hybrid architectures that anchor machine-learned adjustments to first-principles physical baselines.

### Revision C: Rewording "First-Principles" (Paragraph 40)
* **Approved Replacement:**
  > "To resolve the tension between the domain transparency of **analytical queuing models** and the non-linear predictive flexibility of machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025; Jenčová et al., 2025)."

### Revision D: Rewording "Empirical Lognormal Curve" (Paragraph 42)
* **Approved Replacement:**
  > "...establishes that commercial passenger arrival distributions follow an **empirically fitted lognormal distribution**, with peak passenger arrivals concentrating between 90 and 120 minutes prior to scheduled domestic departures."

---

## 2. Chapter III Revisions (Methodology)

### Revision E: Phase 4 Heading Standardization (Paragraph 77)
* **Approved Heading:** `Phase 4: Factorial Cohort (Carrier-Archetype Matrix Balance):`
* **Rationale:** Resolves the repetitive "Factorial... Factorial" stutter and maintains parallel syntax with Phases 1–3 (*Macro Filter*, *Meso Filter*, *Micro Filter*).

### Revision F: Academic Substitutions for "Airport Universe"
* **Methodology / Filtering Context (450+ airports):** Use **"national candidate pool"** or **"national sampling frame"**.
* **Comparative / System Context (Top 25 airports):** Use **"Top 25 benchmark population"** or **"national commercial airport network"**.

---

## 3. Chapter IV Revisions (Findings and Discussion)

### Revision G: Seasonality Dimensions & Eliminating "Like for Like" (Paragraph 60)
* **Approved Replacement Paragraph:**
  > Just as temporal boundaries must be established across the Top 25 network, defining seasonality requires capturing the full empirical variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks (see Appendix C, including Table 4.3b for annual regimes and Table 4.4a for day-of-week archetypes). Formally defining these dimensions enables predictive models to control for cyclical variance, ensuring that model architectures are benchmarked across **equivalent operational conditions**.

### Revision H: Checkpoint Volatility Staffing Buffer (Concise Synthesis)
* **Approved Streamlined Paragraph (48 words, 49% reduction):**
  > Traditional airport models staff security lanes based on average passenger volume—a practice that guarantees severe backlogs during departure peaks because queuing delays scale non-linearly. Incorporating predicted arrival volatility into dynamic, risk-adjusted staffing buffers allows checkpoints to absorb sudden demand spikes without causing costly overstaffing during off-peak periods.

---

## 4. Master Terminology Crosswalk Table

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
