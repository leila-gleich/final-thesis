# Comprehensive Manuscript Audit & Recommendations Report
**Document Audited**: `thesis_docs/manuscripts/Gleich-FinalThesis.docx`  
**Author**: Leila Gleich  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics, Embry-Riddle Aeronautical University  
**Audit Date**: October 11, 2026  
**Auditor**: Antigravity AI Academic Review Assistant  
**Status**: First Draft Comprehensive Quality Assurance & Sanity Audit

---

## Executive Summary

A comprehensive, line-by-line automated and qualitative audit of `Gleich-FinalThesis.docx` (14,536 words, 451 paragraphs, 19 embedded exhibits) was conducted. This audit focused specifically on identifying:
1. **Critical/Egregious Flaws**: Unrendered LaTeX code, stripped mathematical expressions leaving empty parentheses `()` and orphaned punctuation, missing sections, and severe title page errors.
2. **Substantive Inconsistencies**: Numerical conflicts between Chapter IV and Chapter V (specifically regarding Resilience and Generalizability metrics), table renumbering disconnects between in-text citations and table titles, and misplaced empirical results.
3. **Verbatim Sentence Duplication & Redundancy**: Identical paragraphs and phrases repeated across chapters.
4. **Formatting, Citation, & APA 7th Compliance**: Adherence to ERAU thesis handbook guidelines, bibliography alignment, and figure/table styling.

The findings have been prioritized into four severity tiers:
- **Tier 1: Critical (Blockers)** — 5 Major Issues
- **Tier 2: High Severity (Substantive Contradictions & Structural Inconsistencies)** — 4 Major Issues
- **Tier 3: Medium Severity (Methodological Inconsistencies & APA Citations)** — 5 Issues
- **Tier 4: Low Severity / Polish (Stylistic & Typographical Enhancements)** — 4 Issues

---

## Tier 1: Critical Issues (Immediate Fixes Required)

### Issue 1.1: Systemic Mathematical Expression Stripping (The "Empty Parentheses" Defect)
* **Severity**: **CRITICAL (EGREGIOUS)**
* **Locations**: Affects over 25 paragraphs across Chapters I, III, IV, and V (e.g., P064–P067, P144–P153, P159, P205, P210, P211, P219, P234–P236, P247, P248, P250, P257, P272–P274, P302, P307–P309, P314–P318, P325–P327, P332).
* **Finding**: During the markdown-to-Word compilation or export process, dozens of inline LaTeX math expressions (`$...$`), Greek letters, equation blocks, and variable tags failed to render and were completely deleted. This leaves behind empty parentheses `()`, orphaned commas `(, )`, hanging punctuation, and broken sentence fragments throughout the core academic narrative:
  * **P064 & P144**: Displays `The Asymmetric Trade-Off  :` with an empty gap where `$H_1$` was located.
  * **P065, P066, P067**: Missing hypothesis sub-tags `H1a`, `H1b`, `H1c`. P066 ends abruptly with `satisfy the resilience.` (missing word "target/threshold"). P067 ends with `without local.` (missing word "retraining").
  * **P146**: Displays `(Routine Operations Target: Lowest   and  ):` where `$\text{RMSE}$` and `$\text{MASE} < 0.700$` were swallowed.
  * **P147**: Displays `Hypothesis : Under nominal operating conditions (, zero cancellations)... achieve the robustness target () ... fail the robustness threshold ().`
  * **P149**: Displays `(Severe Disruption Target: Recovery Multiplier , Lowest , and ):`
  * **P150**: Displays `Hypothesis : Under severe operational disruptions (  or cancellations )... satisfy the resilience target () due to live 1-step error innovation feedback ()... performance degradation ()...`
  * **P159**: Ends with `evaluate the master asymmetric trade-off hypothesis ().`
  * **P205**: Displays `...pandemic high () down to normalized post-recovery equilibrium ()...`
  * **P210**: Displays `Raw scheduled flight departures explain only 20.90% () ... across the Top 25 network () ... variance jumps to 44.94% (), an increase of +115%.`
  * **P211**: Displays `...passenger volumes (), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility () is significantly coupled with flight departure delay volatility () ... weekly flight departure delay variance ()...`
  * **P219**: Displays `Isolated checkpoints with   single-carrier passenger dominance.` (missing `$\ge 90\%$`).
  * **P234–P236**: P234 introduces: `Connecting Passenger Deflation via DB1B Surveys: Departing seat capacity must be deflated by empirical BTS DB1B connecting ratios:`. **Paragraph 235 is completely blank**, as the entire mathematical display formula was swallowed, followed by P236.
  * **P307–P309**: Displays `Lowest  to minimize absolute forecast error...`, `, demonstrating substantial error reduction...` (sentence begins with a comma and no subject!), and `...achieving   and   respectively, compared to the daily persistence baseline () and deterministic flight scheduling (Model 1, ). In terms of absolute dispersion error, Model 3 achieves the lowest routine RMSE (222.1 pax/hr), capturing 74.83% of holdout volatility variance () ... Standard statistical loss differential tests confirm that error reductions are statistically decisive (  and ) ... meets the stringent   target...`
  * **P314–P318**: Displays `departure delays   min or tactical cancellations `, `Disruption Error Multiplier ()`, `Time-to-Recovery ()`, and `beating the   benchmark... deterministic schedules () ... pure machine learning () ... fragility collapse () ... degrade significantly ()...`
  * **P327**: Displays `Model 1 achieves an   of 1.04 (, target met) and a   of only +4.0% ... In cross-cluster transfer (DTW   PHL), Model 1 achieves an   of 1.003... Model 3 experiences a severe +19.0% transfer degradation, with an   of 1.19 ... and a   surge of +21.5% (+0.142, failing the   threshold)... Supervised Machine Learning (Model 2) exhibits robust intermediate portability (, )...`
* **Recommendation**: 
  1. Re-insert all stripped mathematical formulas directly into Word using Word's native Equation Editor (`Alt` + `=`) or MathType.
  2. Restore missing symbols ($H_1, H_{1a}, H_{1b}, H_{1c}$, $\sigma_{\text{TSA}}$, $CV_{\text{TSA}}$, $\text{RMSE}$, $\text{MASE}$, $\text{RTR}$, $R_{\text{MASE}}$, $\text{TTR}$, $e_{t-1}$).
  3. Reconnect truncated sentences (e.g., replace `without local.` with `without local retraining`; replace `satisfy the resilience.` with `satisfy the resilience target`).

---

### Issue 1.2: Unrendered Raw LaTeX Code Burned into Embedded Table Images
* **Severity**: **CRITICAL (EGREGIOUS)**
* **Locations**: Embedded `image4.png` (Table 2.2 in Chapter II) and `image16.png` (Table 4.7 in Chapter IV).
* **Finding**: Several tables were generated using a script that failed to render LaTeX syntax before being captured as PNG images:
  1. **Table 2.2 (`image4.png`, paragraph 105)**: Under the column *Checkpoint Floor Impact* for "Spatial Transferability Collapse", the image literally reads:
     > `Models experience severe error inflation (>40%>40\%>40%) when deployed zero-shot across unfamiliar facilities...`
     The string `>40%>40\%>40%` is a visible rendering defect.
  2. **Table 4.7 (`image16.png`, paragraph 281)**: Under the row *Disruption Bias Shift*, column *Academic Target*, the cell contains unrendered raw LaTeX broken awkwardly across lines:
     > `$`  
     > `\Delta\text{Bias}`  
     > `< 20\text{ pax/hr}$`
* **Recommendation**: Re-export or recreate Table 2.2 and Table 4.7 as clean vector tables (or native Word tables) with properly rendered math ($\Delta\text{Bias} < 20\text{ pax/hr}$ and $> 40\%$).

---

### Issue 1.3: Severe Numerical Contradiction Between Chapter IV and Chapter V
* **Severity**: **CRITICAL (INCONSISTENCY)**
* **Locations**: Chapter IV Table 4.7 (`image16.png`, paragraph 281) versus Chapter V Table 5.2 (`image18.png`, paragraph 310) and Table 5.3 (`image19.png`, paragraph 319).
* **Finding**: The master hypothesis evaluation table in Chapter IV (Table 4.7) contains obsolete exploratory figures that **directly contradict** the official empirical findings presented in Chapter V (Tables 5.2 and 5.3) and the repository's Single Source of Truth (`thesis_docs/ssot/`):

| Evaluation Metric | Model | Chapter IV Table 4.7 (`image16.png`) | Chapter V Table 5.2 / 5.3 (`image18/19.png`) | Conflict Status |
| :--- | :--- | :--- | :--- | :--- |
| **Disruption RMSE** | Baseline Control | **487.2 pax/hr** | **398.2 pax/hr** | **Conflicting (-89.0)** |
| **Disruption RMSE** | Model 1 (Deterministic) | **512.4 pax/hr** | **412.8 pax/hr** | **Conflicting (-99.6)** |
| **Disruption RMSE** | Model 2 (Machine Learning) | **468.2 pax/hr** | **318.4 pax/hr** | **Conflicting (-149.8)** |
| **Disruption RMSE** | Model 3 (Dynamic Hybrid) | **284.5 pax/hr** | **254.2 pax/hr** | **Conflicting (-30.3)** |
| **Resilience Multiplier ($R_{\text{MASE}}$)** | Baseline Control | **1.921** | **1.00** | **Direct Contradiction** |
| **Resilience Multiplier ($R_{\text{MASE}}$)** | Model 1 (Deterministic) | **1.632** | **1.32** | **Direct Contradiction** |
| **Resilience Multiplier ($R_{\text{MASE}}$)** | Model 2 (Machine Learning) | **1.698** | **2.14** | **Direct Contradiction** |
| **Resilience Multiplier ($R_{\text{MASE}}$)** | Model 3 (Dynamic Hybrid) | **1.281** | **1.05** | **Direct Contradiction** |
| **Time-to-Recovery (TTR)** | Baseline Control | **18.4 hours** | **8.4 hours** | **Conflicting (-10.0h)** |
| **Time-to-Recovery (TTR)** | Model 2 (Machine Learning) | **6.5 hours** | **5.4 hours** | **Conflicting (-1.1h)** |
| **Zero-Shot Transfer Degradation** | Model 2 (Machine Learning) | **+26.4%** | **+8.3% (+0.065 $\Delta\text{MASE}$)** | **Severe Disconnect** |
| **Zero-Shot Transfer Degradation** | Model 3 (Dynamic Hybrid) | **+42.3%** | **+21.5% (+0.142 $\Delta\text{MASE}$)** | **Severe Disconnect** |

* A thesis committee member reading Chapter IV will see Table 4.7 claiming Model 2 collapses with a transfer degradation of $+26.4\%$, and then five pages later in Chapter V read Table 5.3 stating Model 2 degradation is only $+8.3\%$!
* **Recommendation**: Replace Table 4.7 in Chapter IV with the conformed master table that aligns with Table 5.1, 5.2, 5.3, and `results/manuscript_tables/thesis_tables.xlsx`.

---

### Issue 1.4: Systematic Table Renumbering Disconnects (In-Text Reference vs. Caption Mismatches)
* **Severity**: **CRITICAL (INCONSISTENCY)**
* **Locations**: Chapter III (P160) and Chapter IV (P222, P241, P254, P267, P280).
* **Finding**: In earlier drafts, tables were numbered according to a 14-table sequence. During condensation, table captions were changed to consecutive numbers (e.g., Table 4.1 to 4.6), but the in-text citations were never updated to match:
  1. **P160 vs P161**: P160 literally contains the single word `Table` on its own line without any number or letter, followed by P161: `Design and Procedure Phases` and `image7.png`. It should be **Table 3.1: Design and Procedure Phases**.
  2. **P222 vs P223**: P222 states: *"Table 4.6 details the experimental cohort."* But the table heading immediately below (P223) is **Table 4.3: The Nine-Airport Experimental Cohort Specification**.
  3. **P241 vs P242**: P241 states: *"Table 4.9 summarizes the empirical lead-lag correlation across key pre-departure horizons."* But the table heading immediately below (P242) is **Table 4.4: Empirical Lead-Lag Transfer Dynamics**. Worse, the embedded image (`image13.png`) literally has **Table 4.9** burned into the top of the graphic!
  4. **P254 vs P251**: P254 states: *"As shown in Table 4.8, models were calibrated across 15,976 training complex-days..."* But the table heading immediately above (P251) is **Table 4.5: Model Development Dataset Partitions and Calibration Scale**.
  5. **P267 vs P268**: P267 states: *"Table 4.10 synthesizes the master benchmark evaluation matrix across all four paradigms..."* But the table heading immediately below (P268) is **Table 4.6: Master Model Benchmark Matrix for TSA Throughput Volatility**.
  6. **P280 vs P281**: P280 states: *"Table 4.7 presents the formal multi-pillar hypothesis evaluation matrix..."* But at P281 there is NO table heading or caption whatsoever above `image16.png`.
* **Recommendation**: Synchronize all in-text citations with their respective table headers. Ensure that burned-in headers on graphics match the document text exactly.

---

### Issue 1.5: Deficient Front Matter & Title Page Typo
* **Severity**: **CRITICAL (FORMATTING & ACCREDITATION)**
* **Locations**: Paragraphs 043 to 076.
* **Finding**:
  1. **Typo in Abstract Title Block (P048)**:
     `Title: An Evaluation of Performance Measures for Predictive Approachs to Model TSA Throughput Volatility`
     The word `Approachs` is misspelled right in the formal submission metadata block.
  2. **One-Sentence Abstract (P052)**:
     The entire Abstract narrative is literally a single sentence (19 words):
     *"This study explores how to improve passenger flow operations in airports by analyzing different tools that employ predictive analytics."*
     ERAU Graduate Thesis specifications mandate a structured 150–250 word academic abstract summarizing the problem, dataset, candidate models, findings, and practical recommendations.
  3. **Empty Acronyms Section (P073–P076)**:
     The heading `Acronyms` appears at P073, followed by three empty paragraphs (P074, P075, P076) and zero content, immediately before Chapter II begins.
  4. **Missing Required Front Matter Components**:
     The document lacks a Table of Contents (TOC), List of Tables (LOT), and List of Figures (LOF).
* **Recommendation**: 
  - Correct `Approachs` to `Approaches`.
  - Replace the 1-sentence abstract with a complete, publication-grade academic abstract.
  - Populate the Acronyms list (TSA, BTS, OTP, FOIA, ACRP, IROPS, MASE, RMSE, RTR, TTR, etc.).
  - Generate automated TOC, LOT, and LOF fields in Word.

---

## Tier 2: High Severity Issues (Substantive & Structural Inconsistencies)

### Issue 2.1: Misplacement of Empirical Findings in Chapter V
* **Severity**: **HIGH (STRUCTURAL)**
* **Locations**: Chapter IV (P188–P289) vs. Chapter V (P290–P327).
* **Finding**: 
  - In standard ERAU and APA 7th thesis architecture, **Chapter IV is reserved for Empirical Results/Findings**, and **Chapter V is reserved for Discussion, Conclusions, and Recommendations**.
  - Currently, Chapter IV ends prematurely after a high-level summary of the hypotheses (P282–P286). The actual detailed empirical hypothesis evaluations—including Table 5.1 (Robustness), Table 5.2 (Resilience), Table 5.3 (Generalizability), Diebold-Mariano test statistics, and Time-to-Recovery metrics—are located in **Chapter V** (P304–P327).
  - This structure forces empirical data presentation into the discussion chapter, confusing the boundary between results and interpretation.
* **Recommendation**: Move the empirical evaluations and Tables 5.1, 5.2, and 5.3 into Chapter IV (as Tables 4.7, 4.8, 4.9 or 4.11, 4.12, 4.13). Reserve Chapter V strictly for interpreting why these phenomena occur (the Hub Disconnect, Terminal Complex Aggregation, Airport Operational Implications, and Future Research).

---

### Issue 2.2: Orphaned and Mislabeled Figures & Diagram Terminology
* **Severity**: **HIGH (EDITORIAL)**
* **Locations**: P108, P135–P136, P172–P173.
* **Finding**:
  1. **Orphaned Figure at P108 (`image5.png`)**: A table image titled *"Figure 3. Concept Comparison"* is inserted between P107 and P109 in Chapter II. It has no Word caption and is never cited in the prose.
  2. **Mislabeled Figure at P136 (`image6.png`)**: Labeled *"Figure 1. Model Families"*. In Chapter III, it should be numbered according to chapter context (**Figure 3.1**). Additionally, it is a tabular comparison rather than a figure, and lists the obsolete category name "Probabilistic" instead of "Supervised Machine Learning".
  3. **Uncaptioned Funnel Figure at P173 (`image8.png`)**:
     - P172 introduces it as *"the Filtering Pipeline Table"*, but it is an uncaptioned figure graphic.
     - The burned-in title reads *"FOUR-TIERED PURPOSE FILTERING PIPELINE"* (typo: `PURPOSE` instead of `PURPOSIVE`).
     - The bottom-right terminal bubble displays **9 CKPTs**, whereas Tier 4 isolates **12 dedicated carrier screening complexes** across 9 airports (4 complexes $\times$ 3 carriers = 12 complexes).
* **Recommendation**: 
  - Remove or properly integrate and caption Figure 3 in Chapter II.
  - Renumber Figure 1 in Chapter III to Figure 3.1 and update the column label from "Probabilistic" to "Supervised Machine Learning".
  - Add a proper caption to the filtering pipeline diagram (`Figure 3.2: Four-Tiered Purposive Filtering Pipeline`), correct "PURPOSE" to "PURPOSIVE", and correct "9 CKPTs" to "12 Screening Complexes".

---

### Issue 2.3: Verbatim Sentences and Repetitive Phrasing
* **Severity**: **HIGH (ACADEMIC WRITING INTEGRITY)**
* **Locations**: P286 (Chapter IV) vs. P327 (Chapter V); P064 (Chapter I) vs. P144 (Chapter III).
* **Finding**:
  1. **Verbatim Cross-Chapter Sentence**:
     - P286: *"The Deterministic Flight Schedule Model (Model 1) is the decisive champion of Generalizability."*
     - P327: *"The Deterministic Flight Schedule Model (Model 1) is the decisive champion of Generalizability."*
     (Exact duplicate opening sentence).
  2. **Verbatim Hypothesis Declarations**:
     - P064: *"The Asymmetric Trade-Off : Across the candidate modeling paradigms evaluated, no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability)."*
     - P144: repeats this sentence word-for-word.
* **Recommendation**: Paraphrase the opening in Chapter V to frame it as a discussion/retrospective reflection rather than a verbatim repetition of the Chapter IV findings sentence (e.g., *"When evaluated through the lens of zero-shot spatial transferability, the empirical findings confirm that deterministic scheduling models exhibit superior stability across disparate airport environments..."*).

---

### Issue 2.4: Table 4.2 Formatting Artifacts (`image11_from_pdf.png`)
* **Severity**: **HIGH (AESTHETICS & QUALITY)**
* **Location**: Paragraph 201 (`image11.emf` / `image11_from_pdf.png`).
* **Finding**: Table 4.2 (*Post-ETL Master Summary Descriptive Statistics*) contains noticeable export defects:
  1. Sample sizes ($N$) are formatted as raw Python floating-point numbers: `6434732.0`, `13153654.0`, `422096.0`, `22051557.0` instead of formatted integers (`6,434,732`, `13,153,654`, `422,096`, `22,051,557`).
  2. Under the *Variable Name* column, the first word of *"Reported Departure Delay (minutes)"* has **Reported** in bold font while the rest of the text is normal weight.
  3. Large numbers lack thousands commas (e.g., `4962`, `2512`, `7020`, `4030`, `5938`).
* **Recommendation**: Re-render Table 4.2 as a native Word table formatted strictly to APA 7th standards with commas and integer counts.

---

## Tier 3: Medium Severity Issues (Methodological Details & APA Compliance)

### Issue 3.1: Delimitations Mentions Prohibited Metric MAPE & "R2 squared" (P069)
* **Severity**: **MEDIUM**
* **Location**: Paragraph 069.
* **Finding**: The delimitations section states:
  > *"Dynamic queuing models and simulation-based methods are assessed using standard statistical measures, including p-value, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE)."*
* **Issues**:
  1. `R2 squared` is a redundant tautology (either $R^2$ or coefficient of determination).
  2. `MAPE` is mathematically invalid for airport security checkpoint modeling because overnight screening counts drop to zero passengers, causing division by zero and infinite error. The methodology explicitly uses **Mean Absolute Scaled Error (MASE)** to resolve this exact problem.
  3. Mentions "simulation-based methods", which were not part of the final candidate suite.
* **Recommendation**: Revise P069 to read: *"Predictive modeling frameworks are evaluated against standard statistical and operational performance criteria, including the Coefficient of Determination ($R^2$), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE), and forecast bias."*

---

### Issue 3.2: First-Citation Author Grouping in APA 7th (P059)
* **Severity**: **MEDIUM**
* **Location**: Paragraph 059.
* **Finding**: P059 lists all authors for works with 3+ authors:
  - `(Cheng, Zhang, & Guo, 2012)` $\to$ APA 7th mandates `Cheng et al. (2012)` from the first citation.
  - `(Dönmez, Tükenmez, & Cecen, 2025)` $\to$ Should be `Dönmez et al. (2025)`. Also, "Cecen" lacks Turkish diacritics (Çeçen).
  - `(Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021)` $\to$ Should be `Ebert et al. (2021)`.
  - `(Hopfe, Lee & Yu, 2024)` $\to$ Should be `Hopfe et al. (2024)`.
* **Recommendation**: Standardize all 3+ author citations to `et al.` format throughout Chapter I.

---

### Issue 3.3: Apparent DB1B Row Inversion in Table 4.1 (`image10.png`)
* **Severity**: **MEDIUM**
* **Location**: Paragraph 199–200.
* **Finding**: In Table 4.1 (*Master Post-ETL Multi-Source Data Foundation Census*), the row for *BTS DB1B / DB1C Ticket Surveys* reports:
  - Raw Ingested Rows: **12,910,384**
  - Post-ETL Cleaned Rows: **22,051,557**
* A committee reviewer may question how cleaned rows exceed raw ingested rows. In this ETL pipeline, round-trip itinerary records were directionally unrolled into directional airport-pair coupon legs, naturally expanding the row count.
* **Recommendation**: Add an explicit explanatory footnote to Table 4.1:  
  *Note. Post-ETL DB1B coupon counts exceed raw ingested itinerary records because round-trip passenger itineraries were directionally unrolled into discrete directional origin-destination coupon legs.*

---

### Issue 3.4: Reconciling Full Holdout MASE (0.779) vs. Routine MASE (0.680)
* **Severity**: **MEDIUM**
* **Locations**: Table 4.6 (P268) vs. Table 4.7 (P281) & Table 5.1 (P304).
* **Finding**: 
  - Table 4.6 reports Model 2 Test MASE as **0.779**.
  - Table 4.7 reports Model 2 Routine Relative Error (MASE) as **0.680**.
  - Table 5.1 reports Model 2 Routine MASE as **0.68–0.70**.
* To an outside reader, having three different MASE values for Model 2 appears contradictory.
* **Explanation**: `0.779` is the overall test MASE across all 72,053 holdout hours in 2025 (including weather disruptions and flight delays). `0.680` is the specific subset MASE evaluated strictly during nominal/routine operational hours ($\text{Delay} < 15$ min, 0 cancellations).
* **Recommendation**: Clarify the column headers and in-text prose: designate `0.779` as **Full Holdout Benchmark MASE** and `0.680` as **Nominal Routine Regime MASE**.

---

### Issue 3.5: Inconsistent Figure Caption Placement Relative to Images
* **Severity**: **MEDIUM**
* **Locations**: Figures 2.1, 2.2, 1 (Model Families), 4.1.
* **Finding**: Under APA 7th standards, Figure numbers and titles must appear **above** the visual figure, with Notes below. In the current document, several figure titles appear **below** the image (e.g., P082 below P081, P100 below P099, P136 below P135), while Table titles appear **above** the image.
* **Recommendation**: Standardize all figures so that Figure number (bold) and Title (italics) sit on lines directly preceding the figure graphic, with explanatory notes placed beneath.

---

## Tier 4: Low Severity Issues & Polish

1. **Word Style Anomalies**: Delimitations (P068) and Table 4.5 (P251) have paragraph style `code-line`, rendering them in monospaced font rather than Times New Roman Heading/Body styles. Reapply standard APA Heading styles.
2. **Uncited Reference**: `Liao, M., Cheung, T. K. Y., Wong, C. W. H., & Zhang, A. (2025)` is present in the Reference list (P399) but never cited in the body. Either cite Liao et al. in the Literature Review under resilience to disruptions or remove it from References.
3. **Acknowledgements Polish**: Expand the acknowledgements paragraph from the current 1-sentence draft into a formal 2–3 paragraph recognition of the thesis committee chair (Dr. Mark Miller), faculty mentors, industry data providers, and family support.
4. **Appendices Integration**: Confirm whether `Master Appendix.docx` will remain a separate volume or be merged as Appendix A through D at the end of `Gleich-FinalThesis.docx`.

---

## Master Checklist for Document Finalization

- [ ] **Front Matter**: Fix `Approachs` typo in Abstract header; expand Abstract to 150–250 words; populate Acronyms list; generate TOC, LOT, and LOF fields.
- [ ] **Math & Symbols**: Replace all empty parentheses `()` and orphaned commas with correct LaTeX/Equation Editor variables ($H_1, H_{1a}, H_{1b}, H_{1c}$, $\sigma_{\text{TSA}}$, $CV_{\text{TSA}}$, $\text{RMSE}$, $\text{MASE}$, $\text{RTR}$, $R_{\text{MASE}}$, $\text{TTR}$, $e_{t-1}$).
- [ ] **Table 4.7 Replacement**: Replace obsolete `image16.png` in Chapter IV with the conformed master hypothesis matrix matching Chapter V and the SSOT.
- [ ] **Table Renumbering**: Fix in-text table citations (P160 $\to$ Table 3.1; P222 $\to$ Table 4.3; P241 $\to$ Table 4.4; P254 $\to$ Table 4.5; P267 $\to$ Table 4.6).
- [ ] **Image Replacements**: Replace `image4.png` (fix `>40%>40\%>40%`); replace `image11.emf` (format sample sizes as integers with commas); replace `image8.png` (fix "PURPOSE" to "PURPOSIVE" and "9 CKPTs" to "12 Screening Complexes").
- [ ] **Structural Organization**: Consider moving empirical hypothesis results (Tables 5.1–5.3) into Chapter IV, keeping Chapter V focused on synthesis and discussion.
- [ ] **Text Polish**: Rephrase duplicate opening sentences in Chapter IV and V; correct `R2 squared` and `MAPE` in Delimitations.
