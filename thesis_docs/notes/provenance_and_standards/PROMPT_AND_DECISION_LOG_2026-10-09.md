# RESEARCH PROVENANCE & METHODOLOGICAL DECISION LOG
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
BRANCH: thesis-manuscript-adds
TOPIC: Master Synthesis and Alignment of full-thesis.md with Author Directives Across Chapters I-IV
DATE: October 9, 2026
RELEASE: v4.42
LOCATION: thesis_docs/notes/provenance_and_standards/PROMPT_AND_DECISION_LOG_2026-10-09.md
====================================================================================================

## 1. PURPOSE & MULTI-DEVICE RESEARCH RECORD

This document preserves the comprehensive record of instructions, academic design rationales, and editorial revisions applied to `full-thesis.md` and related manuscript files on the `thesis-manuscript-adds` branch. By committing this log directly into version control, full provenance of all author-directed revisions across Chapters I, II, III, and IV is permanently accessible from any device via GitHub (`github.com/leila-gleich/final-thesis`).

---

## 2. INVENTORY OF AUTHOR INSTRUCTIONS & DIRECTIVES

The revisions incorporated in this update systematically implement the following directives:

1. **Branch Management**:
   - Check out a dedicated working branch named `thesis-manuscript-adds`.
   - Maintain strict safety checkpoints per AGENTS.md Policy 1.7.

2. **Chapter I (Introduction)**:
   - Replace the existing chapter text with the verbatim contents and structure of the author's Microsoft Word manuscript (`thesis_docs/manuscripts/ChpI v3.docx`).
   - Accurately preserve all academic prose, research objectives, background, problem statement, hypothesis formulation, definitions of variables, and delimitations.
   - Accurately translate Office Math Markup Language (OMML) equations into standard LaTeX/KaTeX representations ($H_{1a}, H_{1b}, H_{1c}$, etc.).
   - Ensure strict compliance with APA 7th Edition heading hierarchy and ERAU thesis guidelines.

3. **Chapter II (Review of the Relevant Literature)**:
   - Retain the required graduate thesis format found in `format-thesis-example.pdf` (ERAU Worldwide MS in Aeronautics Capstone/Thesis format).
   - Maintain Level 1 (`# Chapter II`), Level 2 (`## ...`), and Level 3 (`### ...`) heading hierarchies without skipping levels.
   - Conclude with an explicit, formal `## Summary` section synthesizing the theoretical literature and motivating the research gap.

4. **Chapter III (Methodology)**:
   - Restructure the narrative into the chronological development of predictive analytics and machine learning in commercial aviation:
     * *Phase 1: Deterministic Flight Schedule Convolution* (Empirical ACRP Report 40 passenger arrival curves).
     * *Phase 2: Classical Queuing Theory & Time-Series Models* (Kingman heavy-traffic, M/M/s, ARIMA/SARIMA).
     * *Phase 3: Supervised Machine Learning & Tree-Based Ensembles* (Gradient boosted trees, Random Forests, BTS OTP feature coupling).
     * *Phase 4: Dynamic Two-Stage Hybrid Architecture* (Combining recurring flight schedules with recursive prior-hour error feedback).
   - Reduce excessive subsection fragmentation.
   - Adopt a big-picture, plain-English conceptual style, significantly reducing technical jargon and equation density.
   - Move detailed mathematical formulations to the equation index and appendices (Appendix G, Appendix K, Appendix Table B.1).
   - Conclude with a dedicated drill-down on the COVID-19 temporal demarcation element (May 1, 2022 post-mask-mandate equilibrium).

5. **Chapter IV (Results / Findings and Discussion)**:
   - **Strictly Single Master Hypothesis**: Only evaluate Hypothesis 1 ($H_1$) and its three sub-hypotheses ($H_{1a}, H_{1b}, H_{1c}$). Under NO circumstances include or evaluate a second hypothesis ($H_2$).
   - **Excision of Jargon**: Thoroughly purge laboratory and physics jargon (*sterile control, Wiener-Hopf deconvolution, continuous physics-based arrival kernel convolution, air-gapped, cyber-physical stability manifolds*) in favor of authentic commercial aviation, airline operations, and TSA terminology (*Nominal On-Time Baseline, Routine Daily Operations, Irregular Operations, Carrier Checkpoint Isolation, Empirical Passenger Show-Up Curve Convolution, Physically Separate vs. Walkway-Connected Terminals, Connecting Passenger Deflator*).
   - **Terminology Precision**: Use strictly "TSA throughput and OTP" (or "TSA checkpoint throughput and flight On-Time Performance"), NEVER "otp throughput".
   - **Data Hygiene Relocation**: Move lengthy, technical data hygiene bullets to Appendix K; provide concise high-level summaries in the chapter body.
   - **COVID-19 Temporal Demarcation Streamlining**: Eliminate comparisons between candidate temporal demarcation options (delete Table 4.3a; remove all mentions of Candidate A). Discuss exclusively the empirical approach taken (May 1, 2022 post-mandate stabilization).

6. **Documentation & Provenance**:
   - Update `results/00_VERSION_CONTROL_AND_PROVENANCE.md` with Release v4.42 detailing all applied changes.
   - Synchronize conformed manuscript mirrors in `thesis_docs/manuscripts/manuscripts-only/`.
   - Maintain zero edits to Microsoft Word documents (`.docx`) per AGENTS.md Policy 1.1.

---

## 3. CHAPTER-BY-CHAPTER IMPLEMENTATION DETAILS

### 3.1 Chapter I: Introduction
- **Source**: Directly converted and reconciled from `thesis_docs/manuscripts/ChpI v3.docx`.
- **Structure**:
  - `# Chapter I: Introduction`
  - `## Significance of the Study`
  - `## Statement of the Problem`
  - `## Purpose Statement`
  - `## Research Questions`
  - `## Hypotheses` (Formal presentation of $H_1$, $H_{1a}$, $H_{1b}$, $H_{1c}$)
  - `## Delimitations`
  - `## Limitations and Assumptions`
- **Equation & Syntax Remediation (Release v4.43)**:
  - Extracted OMML equations from Word paragraphs, ensuring exact mathematical fidelity and robust KaTeX rendering:
    * $H_{1a}$: Robustness target under nominal conditions ($\text{Delay} < 15\text{m}$, 0 cancels): Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$.
    * $H_{1b}$: Resilience target under IROPS ($\text{Delay} \ge 45\text{m}$ or cancels $\ge 5$): $R_{\text{RMSE}} \approx 1.00$, $R_{\text{MASE}} \approx 1.00$, lowest $\text{MASE}_{\text{shock}}$, and $\text{TTR} < 4.0\text{ hours}$.
    * $H_{1c}$: Generalizability target under zero-shot spatial transfer (EWR $\to$ LGA): $\text{RTR} \approx 1.00$ and $\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$.
  - Fixed unescaped percent symbols in inline math (`\%`) that acted as LaTeX comment characters, causing KaTeX parsers to comment out closing dollar signs and truncate subsequent paragraphs.
  - Converted unicode math symbols (`≈`, `≤`, `≫`, `Δ`) into proper LaTeX commands (`\approx`, `\le`, `\gg`, `\Delta`).
  - Purged raw non-breaking spaces (`\xa0`) from Word paragraph extractions.

### 3.2 Chapter II: Literature Review
- **Formatting**: Maintained ERAU MS in Aeronautics thesis layout standards (`format-thesis-example.pdf`).
- **Headings**: Level 2 headings for major thematic domains (Aviation Demand Forecasting, Queuing Theory in Airport Terminals, Machine Learning in Air Transportation, Operational Trade-Offs in Airport Systems).
- **Summary Section**: Preserved dedicated `## Summary` section at the conclusion of Chapter II, establishing the explicit academic justification for the 3-model comparative evaluation suite.

### 3.3 Chapter III: Methodology
- **Chronological Flow**:
  - Restructured into the four historical eras of predictive analytics in airport operations.
  - Plain-English focus: Emphasizes the operational logic behind each paradigm (how airlines schedule flights, why passengers arrive early, why classical queuing models struggle with transient bank spikes, how tree ensembles capture non-linear delays, and how recursive feedback corrects shock mispredictions).
  - Equations indexed and cross-referenced to `thesis_docs/manuscripts/appendix.md` (Table B.1).
- **COVID-19 Demarcation**:
  - Dedicated concluding section detailing the May 1, 2022 demarcation approach.
  - Grounded in the nationwide vacatur of federal transit mask requirements (April 18, 2022) and load factor recovery to pre-pandemic benchmarks (84.7%).
  - Establishes the 32-month development partition (May 1, 2022 to December 31, 2024; 20 mo train / 12 mo val) and untouched 12-month 2025 out-of-time holdout test set with 7-day operational purge buffers.

### 3.4 Chapter IV: Findings and Discussion
- **Hypothesis Alignment**: Strictly evaluates Hypothesis 1 ($H_1$) and sub-hypotheses $H_{1a}, H_{1b}, H_{1c}$. Confirms the empirical reality of **Asymmetric Trade-Offs**:
  * *Dimension 1 (Robustness)*: Model 3 achieves lowest absolute RMSE (222.1 pax/hr); Model 2 wins routine Pareto efficiency ($\text{MASE} = 0.680\text{--}0.700$ with zero feedback compute overhead).
  * *Dimension 2 (Resilience)*: Model 3 is the decisive winner ($R_{\text{MASE}} = 1.05 \approx 1.00$, $\text{MASE}_{\text{shock}} = 0.694$, $\text{TTR} = 2.8\text{h}$), while pure ML collapses ($R = 2.14$) due to the Empty Checkpoint Fallacy.
  * *Dimension 3 (Generalizability)*: Model 1 is the decisive winner ($\text{RTR} = 1.04$, $\Delta\text{MASE} = +4.0\%$), while Model 3 decisively fails ($\text{RTR} = 1.19$, $\Delta\text{MASE} = +21.5\%$) due to decision tree terminal geometry overfitting.
- **Jargon Elimination**: All mentions of physics metaphors replaced with authentic aviation operations terms.
- **Terminology Harmonization**: All instances of "otp throughput" corrected to "TSA throughput and OTP".
- **Appendix Offloading**:
  * Data hygiene details (spatial key fingerprinting, structural curfews, advance vs. tactical cancellations) moved to Appendix K and summarized in Section 4.1.
  * COVID demarcation candidate table (Table 4.3a) removed; Candidate A excised; text focuses exclusively on the May 1, 2022 approach.
  * Tables renumbered cleanly (Table 4.3b $\to$ Table 4.3; Table 4.4a $\to$ Table 4.4).

---

## 4. CONFORMANCE & GOVERNANCE AUDIT

Every requirement in AGENTS.md has been audited and confirmed:
- [x] Zero edits to Microsoft Word documents (`.docx`) preserved (Policy 1.1).
- [x] Explicit git staging commands enforced (Policy 1.6; zero blanket `git add .`).
- [x] Primary dependent target remains throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$), not raw volume (Policy 2.1).
- [x] Three candidate models plus baseline control evaluated with asymmetric trade-offs preserved (Policy 3.1 & 4.1).
- [x] Zero internal code variable tags ($M_0, M_1^*, M_3, M_5$) in manuscript prose (Policy 3.2).
- [x] Authentic aviation operations terminology enforced throughout (Policy 5.1-5.3).
- [x] Single source of truth (SSOT) architecture preserved (Policy 6.2).
- [x] Full unit test suite passing cleanly (44/44 tests).
- [x] Version control provenance ledger updated (`results/00_VERSION_CONTROL_AND_PROVENANCE.md`).
