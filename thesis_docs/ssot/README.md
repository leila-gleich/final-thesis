# Single Source of Truth (SSOT) Master Directory Specification
====================================================================================================
PROJECT: Forecasting the Volatility of Airport Passenger Security Screening Throughput
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DIRECTORY: thesis_docs/ssot/
RELEASE VERSION: v4.2 (SemVer-Data) | DATE: October 2026
====================================================================================================

## 1. PURPOSE AND GOVERNANCE OF THE SSOT SYSTEM

The `thesis_docs/ssot/` directory houses the **definitive, immutable Single Source of Truth (SSOT)** specifications for all five chapters of the graduate thesis.

In large-scale data analytics research—integrating multi-million-row federal datasets (TSA FOIA, BTS OTP Form 234, BTS Form 41 T-100, and BTS DB1B), longitudinal time-series partitions, multiple machine learning and queuing models, and rigorous econometric significance tests—discrepancies between early exploratory drafts and final empirical models easily emerge.

The SSOT system establishes an unalterable benchmark contract:
1. **Zero Discrepancy Tolerance**: Every numerical metric (sample size $N$, $R^2$, RMSE, MAE, MASE, $R_{\text{MASE}}$, RTR, $t$, $p$, and Diebold-Mariano statistics), mathematical formulation, and operational definition used in thesis manuscripts, committee presentations, and research publications must be anchored directly in its respective chapter SSOT.
2. **Decoupled Architecture**: Manuscript prose and explanatory narratives are separated from empirical and mathematical benchmarks. Drafts may be edited for stylistic flow, but their underlying numbers, sample sizes, and model specifications must reference these authoritative SSOT documents.
3. **SemVer-Data Version Control**: All SSOT documents follow semantic data versioning (`v4.2` as of October 2026), coordinated with `results/00_VERSION_CONTROL_AND_PROVENANCE.md`.

---

## 2. SSOT DIRECTORY SITEMAP & COMPANION DRAFT MAPPING

| SSOT Document | Chapter Title | Core Content & Governance Authority | Companion Production Manuscript |
| :--- | :--- | :--- | :--- |
| [**Chapter_1_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_1_SSOT.md) | Chapter I: Introduction & Scope | Verbatim Primary Research Question (Throughput Volatility); Overarching Hypothesis ($H_1$ Master Asymmetric Trade-Offs); Evaluation Triad (Robustness, Resilience, Generalizability); Explicit Targets. | [`chp1-intro.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/chp1-intro.md) |
| [**Chapter_2_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_2_SSOT.md) | Chapter II: Literature Review | Heavy-Traffic Queuing Theory ($W_q \propto C_a^2$); Modeling Paradigm Taxonomy; Theoretical Critiques; Full Formal Academic Citations. | [`chp2-litreview.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/chp2-litreview.md) |
| [**Chapter_3_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_3_SSOT.md) | Chapter III: Methodology | Mathematical Volatility Targets ($\sigma_{\text{TSA}}, CV_{\text{TSA}}$); 4-Tier Filtering Funnel; Candidate Models (Model 1, Model 2, Model 3) and Baseline Control; Explicit Stated Targets. | [`chp3-methodology.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/chp3-methodology.md) |
| [**Chapter_4_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_4_SSOT.md) | Chapter IV: Empirical Findings & Model Evaluation | Master Numerical Registry (42.06M conformed records; 72,053 holdout test hours); Out-of-Time Volatility Fit; Tables 4.10 and 4.11; Verification of Stated Targets. | [`chp4-results.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/chp4-results.md) |
| [**Chapter_5_SSOT.md**](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/ssot/Chapter_5_SSOT.md) | Chapter V: Analysis & In-Depth Discussion | Master Asymmetric Trade-Off Matrix; Proof that Model 3 Fails Generalizability while Model 1 Wins; Empty Checkpoint Fallacy; Regime-Switched Gated Inference Engine. | [`chp5-discussion.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/chp5-discussion.md) |

---

## 3. MASTER CANONICAL BENCHMARK NUMBERS SUMMARY

Every SSOT in this directory is cross-synchronized to the following immutable empirical metrics:

* **Longitudinal Multi-Source Analytical Warehouse**: January 1, 2019 to December 31, 2025 (7 years; 61,344 calendar hours).
* **Conformed Federal Records**: **42,062,039 conformed fact records** (synthesized from 67,222,828 raw federal rows across TSA FOIA, BTS OTP, BTS T-100, and BTS DB1B).
* **Candidate B Demarcation**: **May 1, 2022** (44 continuous post-mask-mandate months; 32 months development / 12 months untouched holdout).
* **Candidate B Partitions**:
  - **Training Fold**: May 1, 2022 to Dec 31, 2023 (**122,847 complex observations** in 9-airport filtered cohort; 15,976 airport-days).
  - **Validation Fold**: Jan 1, 2024 to Dec 31, 2024 (**72,723 complex observations** in 9-airport filtered cohort; 3,293 airport-days).
  - **Inter-Fold Separation Buffer**: 7 calendar days (**2,837 complex observations**).
  - **Holdout Testing Fold**: Jan 1, 2025 to Dec 31, 2025 (**72,053 complex observations** in 9-airport filtered cohort; 3,222 airport-days).
  - **Total Modeled Complex Dataset**: **270,460 observations** across 22,491 airport-days.
* **The 9-Airport Experimental Cohort (12 Dedicated Screening Complexes)**:
  - **American Airlines (AA)**: Dallas/Fort Worth (DFW Terminal D), Philadelphia (PHL Terminal B/C), Chicago O'Hare (ORD Terminal 3).
  - **Delta Air Lines (DL)**: Detroit Metropolitan (DTW McNamara Terminal), New York LaGuardia (LGA Terminal C), Boston Logan (BOS Terminal A).
  - **United Airlines (UA)**: Newark Liberty (EWR Terminal C), Houston Intercontinental (IAH Terminal C/E), Los Angeles (LAX Terminal 7/8).
* **The Candidate Predictive Models and Baseline Control (Throughput Volatility Target)**:
  - **Baseline Control**: $\text{RMSE} = 253.6\text{ pax/hr}, \text{MASE} = 1.000$ (Fails Robustness Target).
  - **Model 1 (Deterministic Flight Schedule Model)**: $\text{RMSE} = 313.4\text{ pax/hr}, \text{MASE} = 0.945$ (Fails Robustness; **Decisive Generalizability Winner: $\text{RTR} = 1.04 \approx 1.00, \Delta\text{MASE} = +4.0\% \le 10.0\%$**).
  - **Model 2 (Supervised Machine Learning Model)**: $\text{RMSE} = 273.5\text{ pax/hr}, \text{MASE} = 0.779$ holdout / $0.680\text{--}0.700$ routine (**Target Met; Routine Pareto Winner**; Fragile under shock: $R = 2.14$).
  - **Model 3 (Dynamic Two-Stage Hybrid Model)**: $\text{RMSE} = 222.1\text{ pax/hr}, \text{MASE} = 0.662$ (**Target Met; Decisive Resilience Winner: $R = 1.05 \approx 1.00, \text{TTR} = 2.8\text{h}$**; **Decisively Fails Generalizability: $\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$** due to terminal geometry overfitting).

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
