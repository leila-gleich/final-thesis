# Single Source of Truth (SSOT) Master Directory Specification
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DIRECTORY: thesis_docs/ssot/
RELEASE VERSION: v4.1 (SemVer-Data) | DATE: October 2026
====================================================================================================

## 1. PURPOSE AND GOVERNANCE OF THE SSOT SYSTEM

The `thesis_docs/ssot/` directory houses the **definitive, immutable Single Source of Truth (SSOT)** specifications for all five chapters of the graduate thesis.

In large-scale data analytics research—integrating multi-million-row federal datasets (TSA FOIA, BTS OTP Form 234, BTS Form 41 T-100, and BTS DB1B), longitudinal time-series partitions, multiple machine learning and queuing models, and rigorous econometric significance tests—discrepancies between early exploratory drafts and final empirical models easily emerge.

The SSOT system establishes an unalterable benchmark contract:
1. **Zero Discrepancy Tolerance**: Every numerical metric (sample size $N$, $R^2$, RMSE, MAE, MASE, $R_{\text{MASE}}$, RTR, $t$, $p$, and Diebold-Mariano statistics), mathematical formulation, and operational definition used in thesis manuscripts, committee presentations, and research publications must be anchored directly in its respective chapter SSOT.
2. **Decoupled Architecture**: Manuscript prose and explanatory narratives are separated from empirical and mathematical benchmarks. Drafts may be edited for stylistic flow, but their underlying numbers, sample sizes, and model specifications must reference these authoritative SSOT documents.
3. **SemVer-Data Version Control**: All SSOT documents follow semantic data versioning (`v4.1` as of October 2026), coordinated with `results/00_VERSION_CONTROL_AND_PROVENANCE.md`.

---

## 2. SSOT DIRECTORY SITEMAP & COMPANION DRAFT MAPPING

| SSOT Document | Chapter Title | Core Content & Governance Authority | Companion Production Manuscript |
| :--- | :--- | :--- | :--- |
| [**Chapter_1_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_1_SSOT.md) | Chapter I: Introduction & Scope | Verbatim Primary Research Question; Overarching Hypothesis ($H_1, H_{1a}, H_{1b}, H_{1c}$); Evaluation Triad (Robustness, Resilience, Generalizability); Delimitations and Assumptions. | [`Chapter_1_Introduction.docx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_1_Introduction.docx) |
| [**Chapter_2_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_2_SSOT.md) | Chapter II: Literature Review | Modeling Paradigm Comparative Taxonomy; Theoretical Critiques (Batch Queuing, DES Latency, ARIMA Linearity, DNN Black-Box Opacity); Full Formal Academic Citations. | [`Chapter_2_Literature_Review.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_2_Literature_Review.md) / [`.docx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_2_Literature_Review.docx) |
| [**Chapter_3_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_3_SSOT.md) | Chapter III: Methodology | Mathematical Formulations; 4-Tier Purposive Filtering Pipeline; 84-Cell Interaction Tensor ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$); Degrees-of-Freedom Proofs; Model Benchmark Suite ($M_0$ through $M_5$). | [`Chapter_3_Methodology.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_3_Methodology.md) / [`.docx`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_3_Methodology.docx) |
| [**Chapter_4_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_4_SSOT.md) | Chapter IV: Empirical Findings & Model Evaluation | Master Numerical Registry (42.06M conformed records); 122,847 Train / 72,723 Val / 72,053 Test Partitions; 17-Subsection Canonical Outline; Complete Model Error Matrices & DM Tests. | [`Chapter_4_Results_Empirical_Findings.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_4_Results_Empirical_Findings.md) |
| [**Chapter_5_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_5_SSOT.md) | Chapter V: Analysis & In-Depth Discussion | Formal Hypothesis Evaluation Proofs ($H_{1a}, H_{1b}, H_{1c}$); Behavioral Mechanics (The Hub Disconnect, Lead-Lag Asynchrony, Empty Checkpoint Fallacy); Cross-Project Synthesis; Regime-Switched Gated Inference Engine. | [`Chapter_5_Analysis_and_Discussion.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/Chapter_5_Analysis_and_Discussion.md) |

---

## 3. MASTER CANONICAL BENCHMARK NUMBERS SUMMARY

Every SSOT in this directory is cross-synchronized to the following immutable empirical metrics:

* **Longitudinal Multi-Source Analytical Warehouse**: January 1, 2019 to December 31, 2025 (7 years; 61,344 calendar hours).
* **Conformed Federal Records**: **42,062,039 conformed fact records** (synthesized from 67,222,828 raw federal rows across TSA FOIA, BTS OTP, BTS T-100, and BTS DB1B).
* **Candidate B Demarcation**: **May 1, 2022** (44 continuous post-mask-mandate months; 32 months development / 12 months untouched holdout).
* **Candidate B Partitions**:
  - **Training Fold**: May 1, 2022 to Dec 31, 2023 (**122,847 complex observations** in 9-airport filtered cohort).
  - **Validation Fold**: Jan 1, 2024 to Dec 31, 2024 (**72,723 complex observations** in 9-airport filtered cohort).
  - **Inter-Fold Separation Buffer**: 7 calendar days (**2,837 complex observations**).
  - **Holdout Testing Fold**: Jan 1, 2025 to Dec 31, 2025 (**72,053 complex observations** in 9-airport filtered cohort; **215,562 facility-level screening hours** across candidate network).
  - **Total Modeled Complex Dataset**: **270,460 observations**.
* **The 9-Airport Experimental Cohort (12 Screening Complexes)**:
  - **American Airlines (AA)**: Dallas/Fort Worth (DFW Terminal A/C/D), Philadelphia (PHL Terminal B/C), Chicago O'Hare (ORD Terminal 3).
  - **Delta Air Lines (DL)**: Detroit Metropolitan (DTW McNamara Terminal), New York LaGuardia (LGA Terminal C), Boston Logan (BOS Terminal A).
  - **United Airlines (UA)**: Newark Liberty (EWR Terminal C), Houston Intercontinental (IAH Terminal C/E), Los Angeles (LAX Terminal 7/8).
* **The 84-Cell Interaction Tensor ($\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H}$)**:
  - Exactly **83 of 84 cells (98.8%)** meet $N_{\text{train}} \ge 50$ (median $N = 215$).
  - **70 of 84 cells (83.3%)** meet Central Limit Theorem test sufficiency ($N_{\text{test}} \ge 30$; median $N = 76$).
* **Champion Model Performance ($M_5$ Sequential Two-Stage Tree Hybrid)**:
  - Out-of-Time 2025 Holdout: $R^2 = 0.6270, \text{RMSE} = 1135.0\text{ pax/hr}, \text{MAE} = 730.4\text{ pax/hr}, \text{MASE} = 0.846$.
  - Routine Operational Accuracy (Dimension 1): $\text{MASE}_{\text{routine}} = 0.834, \text{RMSE} = 1114.7, DM = 79.123$ ($p < 0.0001$).
  - Disruption Resilience (Dimension 2): $R_{\text{MASE}} = 1.28 \le 1.30$, Time-to-Recovery $\text{TTR} = 3.2\text{ hours}$.
  - Spatial Generalizability (Dimension 3): Relative Transfer Ratio $\text{RTR} = 1.00$ to $1.19$.

---

## 4. TERMINOLOGY & GOVERNANCE RULES

All authors, editors, and analytical tools modifying text or code associated with these chapters must strictly enforce the standards established in [`thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md):
* **Prohibited**: "physics-based continuous arrival kernel convolution" $\to$ **Mandatory**: "Empirical Passenger Show-Up Curve" (or "Lead-Lag Passenger Arrival Distribution").
* **Prohibited**: "orthogonal Wiener-Hopf deconvolution operator" $\to$ **Mandatory**: "Carrier Checkpoint Isolation".
* **Prohibited**: "DB1B transfer deflation manifold" $\to$ **Mandatory**: "Connecting Passenger Deflator" (or "The Hub Disconnect").
* **Prohibited**: "cyber-physical stability manifolds" $\to$ **Mandatory**: "Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability".
* **Prohibited**: "multi-agent cybernetic orchestrator" $\to$ **Mandatory**: "Regime-Switched Gated Inference Engine".

====================================================================================================
END OF SSOT MASTER DIRECTORY SPECIFICATION
====================================================================================================
