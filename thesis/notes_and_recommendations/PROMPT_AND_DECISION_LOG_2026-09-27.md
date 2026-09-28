# RESEARCH PROVENANCE & METHODOLOGICAL DECISION LOG
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
TOPIC: Coupled Volatility Seasonality, Post-Pandemic Demarcation Metrics, and Sample Size Harmonization
DATE: September 27, 2026
RELEASE: v3.3
LOCATION: thesis/notes_and_recommendations/PROMPT_AND_DECISION_LOG_2026-09-27.md
====================================================================================================

## 1. PURPOSE & MULTI-DEVICE RESEARCH RECORD

This document preserves the comprehensive mathematical, econometric, and data engineering rationale 
for harmonizing the empirical findings across Chapters III, IV, and V of the graduate thesis manuscript. 
By committing this log directly into version control, full provenance is permanently accessible from 
any device via GitHub (`github.com/leila-gleich/final-thesis`).

---

## 2. INQUIRY & METHODOLOGICAL QUESTIONS

The updates documented herein resolve three central research questions regarding the impact of the 
updated analysis on the coupled seasonality between TSA passenger throughput volatility and 
Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) flight volatility:

1. **How are the metrics for the definition of the post-pandemic regime impacted?**
2. **Given that the post-pandemic start date remains unchanged (May 1, 2022; Candidate B), what specific numbers in the results must be updated or clarified?**
3. **Should any numbers in the descriptive statistics as currently documented be changed?**

---

## 3. METHODOLOGICAL RESOLUTIONS & STATISTICAL JUSTIFICATIONS

### 3.1 Impact on Post-Pandemic Demarcation Metrics

* **Original Justification (1D Volume & Mean Flow)**:
  Candidate B (May 1, 2022 start date) was initially justified using policy triggers (Federal Mask Mandate repeal), 
  CUSUM structural break stabilization, and a simple 1D correlation rebound between scheduled flight seats and 
  checkpoint volume ($R^2$ rebounding from 0.579 during COVID to 0.672 post-May 2022).
  
* **Updated Justification (Higher-Order Coupled Volatility & Factorial Power)**:
  The updated coupled volatility analysis elevates the post-pandemic definition from static volume tracking to 
  higher-order operational turbulence equilibrium:
  1. **Coupled Volatility Index (CVI) Stationarity**: Across the 1,341 calendar days of Candidate B (May 1, 2022 to December 31, 2025), 
     the interaction between intraday passenger screening surge volatility ($CV_{\text{TSA}}$) and airside flight departure delay 
     dispersion ($\sigma_{\text{Delay}}$) establishes stable, repeatable cyclical regimes:
     - Off-Peak Lull: $\text{CVI} = 27.85$ ($\sigma_{\text{Delay}} = 46.09$ min, Cancellations = $0.89\%$)
     - Mid-Peak Shoulder: $\text{CVI} = 32.38$ ($\sigma_{\text{Delay}} = 55.06$ min, Cancellations = $1.36\%$)
     - Convective Summer Peak: $\text{CVI} = 39.36$ ($\sigma_{\text{Delay}} = 68.43$ min, Cancellations = $3.16\%$)
     - Holiday Corridors: $\text{CVI} = 33.07$ ($\sigma_{\text{Delay}} = 55.78$ min, Cancellations = $1.82\%$)
  2. **Asynchronous Mechanism Invariance**: Morning passenger screening surges ($05:00\text{--}08:00, \sigma_{\text{TSA}} > 11,380$ pax/hr) 
     and evening flight delay cascades ($14:00\text{--}22:00, \sigma_{\text{Delay}} > 63.4$ min) consistently decouple by 8–10 hours, 
     confirming that modern queue dynamics follow structural lead-lag physics rather than transient pandemic distortions.
  3. **The 84-Cell Degrees-of-Freedom Power Proof**: In the $4 \times 7 \times 3 = 84$ cross-classification tensor, Candidate B provides 
     $23,400$ training time-steps (Top 25 system hours) and $195,570$ development observations (9-airport complex hours). Exactly 
     **83 of 84 cells (98.8%) satisfy the $N_{\text{train}} \ge 50$ threshold** (median $N = 215$). If Candidate A (Jan 1, 2023) had been chosen, 
     $25\%$ of training depth would have been lost, causing multiple holiday and off-peak diurnal cells to collapse into small-sample bias ($N < 50$).

---

### 3.2 Audit of Results Numbers & Disambiguation of Observation Counts

A rigorous audit identified three specific areas where numbers required arithmetic correction or explicit grain disambiguation:

| Location | Prior Manuscript Text | Corrected / Harmonized Text | Methodological Rationale |
| :--- | :--- | :--- | :--- |
| **Chapter IV, Section 4.4 (Table)** | `36 Months (2022-05 to 2024-12)` | **`32 Months (2022-05 to 2024-12)`** | May 1, 2022 to Dec 31, 2024 is exactly 32 months (8 mo in 2022 + 12 in 2023 + 12 in 2024). Full Candidate B window to Dec 31, 2025 spans 44 continuous months. |
| **Chapter IV, Section 4.4 (Impact row & item 3)** | `404k+ training observations`<br>`(20 months; 404,324 hourly observations)` | **`122,847 modeled / 404k+ network observations`**<br>`(20 months; 122,847 hourly observations across the 9-airport filtered complex cohort; 404,324 multi-facility observations across the candidate network)` | Disambiguates the modeled 9-airport experimental cohort ($N_{\text{train}} = 122,847$) from multi-lane/facility observations across the full candidate pool ($404,324$). |
| **Chapter IV, Section 4.7 (Holdout Benchmark intro)** | `evaluated against the 215,562 hourly observations of the 2025 out-of-time holdout` | **`evaluated against the 72,053 hourly complex observations (8,760 continuous system hours) of the 2025 out-of-time holdout across the 9-airport cohort (representing 215,562 facility-level screening hours across the wider candidate network)`** | Corrects internal contradiction with Section 3 ($N_{\text{test}} = 72,053$ across 9 airports). $215,562$ reflects the wider candidate network ($25\text{ airfields} \times 8,760\text{ hrs} \approx 219\text{k}$). |
| **Chapter III, Section 3.8.1 (Dataset Partitioning)** | Broad training partition description | **Explicit specification of dual grains**: Top 25 system hours ($23,400$ train / $8,760$ test) vs. 9-airport complex observations ($122,847$ train / $72,723$ val / $72,053$ test; Total = $270,460$). | Aligns methodology with data foundation and sample size sufficiency audit. |
| **thesis/README.md (Line 50)** | `May 2022 – Dec 2024; 23,400 observations ... 215,562 hourly observations across the 9-airport cohort` | **`May 2022 – Dec 2024; 23,400 system hours / 195,570 development observations ... 72,053 hourly complex observations / 8,760 system hours across the 9-airport cohort`** | Ensures public repository README accurately mirrors thesis manuscript counts. |

---

### 3.3 Audit of Descriptive Statistics

1. **Tables 4.1 & 4.2 (Master Post-ETL Multi-Source Foundation Census)**:
   - **Status: UNCHANGED**.
   - Scope: Documents all $42,062,039$ conformed records across the complete 7-year baseline ($2019\text{--}2025$) for all 25 candidate airfields ($N_{\text{TSA}} = 6,434,732$ lane-hours; $N_{\text{OTP}} = 13,153,654$ flights; mean throughput $= 420.17$; mean delay $= 12.70$ min; load factor $= 81.21\%$). 
   - Rationale: Foundational macro data health baseline prior to downstream filtering.

2. **Table C & Section 3 (9-Airport Filtered Modeling Dataset)**:
   - **Status: UNCHANGED**.
   - Scope: Total sample size $N = 270,460$ hourly complex records across Candidate B ($2022\text{--}2025$). Mean throughput $= 2,367.49$ pax/hr; mean convolved flights $= 20.88$; mean prior delay $= 12.08$ min; load factor $= 0.83$.
   - Rationale: The physical 9-airport filtered dataset and Candidate B boundaries remain valid.

3. **Legacy Static-Volume Regime Statistics**:
   - **Status: SUPERSEDED & REPLACED**.
   - Legacy quartiles (e.g. Off-Peak $= 24,600$ daily pax, Mid-Peak $= 52,800$, Peak $= 76,500$) are completely replaced by the empirical figures in **Table 4.3b**:
     * `1_OFF_PEAK`: $500$ days ($37.3\%$) | Mean Daily TSA: $1,123,386$ pax | $\sigma_{\text{Delay}} = 46.09$ min | $\text{CVI} = 27.85$
     * `2_MID_PEAK`: $426$ days ($31.8\%$) | Mean Daily TSA: $1,187,095$ pax | $\sigma_{\text{Delay}} = 55.06$ min | $\text{CVI} = 32.38$
     * `3_PEAK`: $224$ days ($16.7\%$) | Mean Daily TSA: $1,305,968$ pax | $\sigma_{\text{Delay}} = 68.43$ min | $\text{CVI} = 39.36$
     * `4_HOLIDAY`: $191$ days ($14.2\%$) | Mean Daily TSA: $1,215,636$ pax | $\sigma_{\text{Delay}} = 55.78$ min | $\text{CVI} = 33.07$

---

## 4. VERSION CONTROL COMMITS & REPOSITORY TRACKING

* Release Tag: `v3.3`
* SemVer-Data Specification: Harmonized Sample Size & Partitioning Provenance
* Primary Git Repository: `final-thesis` (`origin: https://github.com/leila-gleich/final-thesis.git`)
* Mirrored Local Sandbox: `Gleich-Thesis`
====================================================================================================
