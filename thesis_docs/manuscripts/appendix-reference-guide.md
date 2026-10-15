# Master Appendix Reference Guide for Thesis v3
## *Complete In-Text Callout Mapping for Appendices A through G*

> **Source Documents**:
> - **Thesis Chapters**: Quoted verbatim from **`master-docs/Thesisv3.docx`** (authoritative current thesis manuscript). Paragraph numbers cite the internal paragraph indices of `Thesisv3.docx`.
> - **Appendix Architecture**: Grounded in **`master-docs/Master_Appendix_final.docx`** (7 streamlined appendices: A through G).
>
> **Callout Policy**: Per author instructions, all callouts reference **strictly the overarching appendix** (`(see Appendix X)`), omitting internal subsection numbering (e.g., no "Section C.1", "Table B.2", or equation IDs).

---

## Overview of the 7-Appendix Architecture

| Appendix | Authoritative Title in `Master_Appendix_final.docx` | Core Subject Matter |
|:--------:|:---------------------------------------------------|:-------------------|
| **Appendix A** | *Delimitations, Research Limitations, and Methodological Assumptions* | Geographic scope, temporal boundaries, public data boundaries, monthly load factor disaggregation, failure-mode assumptions. |
| **Appendix B** | *Comparative Modeling Paradigms and Literature Equation Registry* | 6-paradigm taxonomy (queuing, DES, ARIMA, deep learning, supervised ML, two-stage dynamic hybrids) & 20 peer-reviewed operational equations. |
| **Appendix C** | *Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations* | Poisson, Erlang-C, NHPP, Kingman/Allen-Cunneen heavy traffic, Tweedie compound Poisson dispersion ($p=1.3$), within-day and multi-day volatility metrics ($\sigma_{\text{TSA, hr}}$, $CV_{\text{TSA}}$, $\sigma_{\text{TSA, 7d}}$). |
| **Appendix D** | *The Diebold-Mariano (DM) Forecast Accuracy Test* | Econometric derivation of pairwise DM forecast comparison, Newey-West HAC spectral density estimator, empirical test statistics. |
| **Appendix E** | *Candidate Predictive Models, Operational Evaluation Triad Metrics, and Holdout Benchmarks* | Mathematical specifications of the 4 candidate models, formal definitions of Robustness, Resilience ($R_{\text{MASE}}$, TTR), Generalizability ($RTR$), and 2025 holdout benchmark tables. |
| **Appendix F** | *The Values versus Volatility Operational Coupling* | Values vs. Volatility paradigm proof, flight delay volatility coupling ($CV_{\text{delay}}$ vs $CV_{\text{TSA}}$), multi-day temporal decoupling ($R^2 < 0$ vs $R^2 > 0.31$). |
| **Appendix G** | *Operational Disruption Dynamics, Lead-Lag Asynchrony, Resilience Mechanics, and the Empty Checkpoint Fallacy* | Disruption regimes (A14 baseline, routine churn, IROPS), lead-lag asynchrony mechanism, the Empty Checkpoint Fallacy, live error innovation feedback ($\alpha = 0.35$). |

---

## Appendix A: Delimitations, Research Limitations, and Methodological Assumptions

### Anchor A.1
* **Chapter**: Chapter I — Introduction
* **Section**: `Delimitations` (Para 69)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > Dynamic queuing models and simulation-based methods are assessed using standard statistical measures, including p-value, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE) (see Appendix A).
* **Callout**: `(see Appendix A)`

---

### Anchor A.2
* **Chapter**: Chapter I — Introduction
* **Section**: `Limitations and Assumptions` (Para 71)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level (see Appendix A).
* **Callout**: `(see Appendix A)`

---

## Appendix B: Comparative Modeling Paradigms and Literature Equation Registry

### Anchor B.1
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `From Analytical Queuing to Simulation Modeling and Real-Time Management` → `Micro-Simulation in Terminal Planning and Asset Allocation` (Para 94)
* **Status in Thesisv3**: *Recommended Insertion / Verification*
* **Full Sentence in Thesisv3**:
  > To overcome the rigid mathematical assumptions of analytical queuing equations, airport planners widely adopted micro-simulation – a modeling approach that simulates individual system entities rather than aggregate flows – primarily implemented through Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011; Verki et al., 2013).
* **Callout to Insert**: `(see Appendix B)`
* **Result after Insertion**:
  > To overcome the rigid mathematical assumptions of analytical queuing equations, airport planners widely adopted micro-simulation – a modeling approach that simulates individual system entities rather than aggregate flows – primarily implemented through Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011; Verki et al., 2013; see Appendix B).

---

### Anchor B.2
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `Advanced Predictive Models and Machine Learning` → `Statistical Time-Series Foundations and Linear Limitations` (Para 101)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > However, while SARIMA excels at internal pattern recognition, because it relies on historical data, it does not account for the direct correlation between fluctuating passenger volumes and specific, real-time flight arrangements (Lin et al., 2023).
* **Callout to Insert**: `(see Appendix B)`
* **Result after Insertion**:
  > However, while SARIMA excels at internal pattern recognition, because it relies on historical data, it does not account for the direct correlation between fluctuating passenger volumes and specific, real-time flight arrangements (Lin et al., 2023; see Appendix B).

---

### Anchor B.3
* **Chapter**: Chapter III — Methodology
* **Section**: `Research Approach` (Para 133)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects.
* **Callout to Insert**: `(see Appendix B)`
* **Result after Insertion**:
  > Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects (see Appendix B).

---

### Anchor B.4
* **Chapter**: Chapter IV — Results
* **Section**: `Model Development and Execution` → `Feature Engineering` (Para 244)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985), and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061).
* **Callout to Insert**: `(see Appendix B)`
* **Result after Insertion**:
  > Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985), and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061; see Appendix B).

---

### Anchor B.5
* **Chapter**: Chapter IV — Results
* **Section**: `Implications for Final Result Interpretation` → `Conformal Staffing Buffers` (Para 264)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility.
* **Callout to Insert**: `(see Appendix B)`
* **Result after Insertion**:
  > Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility (see Appendix B).

---

## Appendix C: Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations

### Anchor C.1
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `Classical Queuing Theory: Volume Versus Volatility` (Para 89)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > NHPP formulations are constrained due to a dependence on expected mean volume and the assumption of independent arrivals, failing to account for the high correlation among passengers arriving for the same ticketed flight bank and ignoring the impact of airside connecting passengers (Adeke, 2018; Guo et al., 2022; See Appendix C).
* **Callout**: `(see Appendix C)`

---

### Anchor C.2
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `The "Values versus Volatility" Paradigm in Transportation Demand` (Para 91)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > As checkpoint lanes operate near full capacity during morning and evening departure peaks, any sudden increase in passenger arrival swings causes wait times and crowd congestion to grow exponentially (Adeke, 2018; Guo et al., 2022; See Appendix C).
* **Callout**: `(see Appendix C)`

---

### Anchor C.3
* **Chapter**: Chapter III — Methodology
* **Section**: `Core Research Variables` (Para 141)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > Dependent variables include TSA checkpoint throughput, queue wait times, and bottleneck formation rates (see Appendix C).
* **Callout**: `(see Appendix C)`

---

### Anchor C.4
* **Chapter**: Chapter III — Methodology
* **Section**: `Validity` (Para 180)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates.
* **Callout to Insert**: `(see Appendix C)`
* **Result after Insertion**:
  > Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates (see Appendix C).

---

### Anchor C.5
* **Chapter**: Chapter IV — Results
* **Section**: `Implications for Model Development` → `Zero-Bounded and Hurdle Formulations` (Para 238)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > Predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models () or two-stage hurdle structures (a logistic model predicting whether the checkpoint is active, followed by a positive count model predicting passenger volume) – to accommodate positive throughput skewness and structural zeros without generating negative volume forecasts (see Appendix C).
* **Callout**: `(see Appendix C)`

---

### Anchor C.6
* **Chapter**: Chapter V — Conclusions and Recommendations
* **Section**: `Implications and Recommendations for Predictive Forecasting in Airport Operations` (Para 331)
* **Status in Thesisv3**: *Already present in manuscript*
* **Full Sentence in Thesisv3**:
  > The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models (see Appendix C).
* **Callout**: `(see Appendix C)`

---

## Appendix D: The Diebold-Mariano (DM) Forecast Accuracy Test

### Anchor D.1
* **Chapter**: Chapter IV — Results
* **Section**: `General Model Performance Across the 9-Airport Cohort` → `Supervised Machine Learning (Model 2)` (Para 273)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ().
* **Callout to Insert**: `(see Appendix D)`
* **Result after Insertion**:
  > Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive (see Appendix D).

---

## Appendix E: Candidate Predictive Models, Operational Evaluation Triad Metrics, and Holdout Benchmarks

### Anchor E.1
* **Chapter**: Chapter I — Introduction
* **Section**: `Research Question` (Para 63)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule baselines, machine learning, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?
* **Callout to Insert**: `(see Appendix E)`
* **Result after Insertion**:
  > Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule baselines, machine learning, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric (see Appendix E)?

---

### Anchor E.2
* **Chapter**: Chapter III — Methodology
* **Section**: `Research Hypothesis` (Para 143)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > The Asymmetric Trade-Off : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability); rather, each modeling paradigm exhibits distinct operational strengths and stark asymmetric trade-offs:
* **Callout to Insert**: `(see Appendix E)`
* **Result after Insertion**:
  > The Asymmetric Trade-Off : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability); rather, each modeling paradigm exhibits distinct operational strengths and stark asymmetric trade-offs (see Appendix E):

---

### Anchor E.3
* **Chapter**: Chapter IV — Results
* **Section**: `Model Development and Execution` → `Candidate Predictive Models` (Para 246)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control:
* **Callout to Insert**: `(see Appendix E)`
* **Result after Insertion**:
  > To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control (see Appendix E):

---

### Anchor E.4
* **Chapter**: Chapter IV — Results
* **Section**: `Model Performance and Hypothesis Testing` (Para 280)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Table 4.7 presents the formal multi-pillar hypothesis evaluation matrix with clear operational descriptions for each metric.
* **Callout to Insert**: `(see Appendix E)`
* **Result after Insertion**:
  > Table 4.7 presents the formal multi-pillar hypothesis evaluation matrix with clear operational descriptions for each metric (see Appendix E).

---

## Appendix F: The Values versus Volatility Operational Coupling

### Anchor F.1
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `The "Values versus Volatility" Paradigm in Transportation Demand` (Para 91)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > This dynamic establishes the "Values versus Volatility" paradigm in transportation demand, which manifests across two operational horizons (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005).
* **Callout to Insert**: `(see Appendix F)`
* **Result after Insertion**:
  > This dynamic establishes the "Values versus Volatility" paradigm in transportation demand, which manifests across two operational horizons (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005; see Appendix F).

---

### Anchor F.2
* **Chapter**: Chapter IV — Results
* **Section**: `Initial Exploratory Analysis` → `Asynchronous Delay Propagation and Checkpoint Volatility Coupling` (Para 208)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Hourly checkpoint arrival volatility () is significantly coupled with flight departure delay volatility ().
* **Callout to Insert**: `(see Appendix F)`
* **Result after Insertion**:
  > Hourly checkpoint arrival volatility () is significantly coupled with flight departure delay volatility (see Appendix F).

---

## Appendix G: Operational Disruption Dynamics, Lead-Lag Asynchrony, Resilience Mechanics, and the Empty Checkpoint Fallacy

### Anchor G.1
* **Chapter**: Chapter II — Review of the Relevant Literature
* **Section**: `Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability` (Para 113)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > During operational disruptions – such as flight delays and cancellations – supervised tree ensembles (Gradient-Boosted Decision Trees or Random Forests) predict the residual error between scheduled demand and actual throughput (Brun et al., 2025; Hopfe et al., 2024; Ribeiro et al., 2025).
* **Callout to Insert**: `(see Appendix G)`
* **Result after Insertion**:
  > During operational disruptions – such as flight delays and cancellations – supervised tree ensembles (Gradient-Boosted Decision Trees or Random Forests) predict the residual error between scheduled demand and actual throughput (Brun et al., 2025; Hopfe et al., 2024; Ribeiro et al., 2025; see Appendix G).

---

### Anchor G.2
* **Chapter**: Chapter IV — Results
* **Section**: `Empirical Confirmation of Asymmetric Trade-Offs` → `Dimension 2: Resilience (Severe Disruption)` (Para 287)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > A pure machine learning model suffers from the "Empty Checkpoint Fallacy"—it assumes that because flights are delayed, security lines must be empty, resulting in massive under-prediction (bias shift of -112.4 pax/hr).
* **Callout to Insert**: `(see Appendix G)`
* **Result after Insertion**:
  > A pure machine learning model suffers from the "Empty Checkpoint Fallacy"—it assumes that because flights are delayed, security lines must be empty, resulting in massive under-prediction (bias shift of -112.4 pax/hr; see Appendix G).

---

### Anchor G.3
* **Chapter**: Chapter V — Conclusions and Recommendations
* **Section**: `Spatial Architecture and Passenger Behavioral Dynamics` → `Initial Training and Passenger Show-Up Dynamics` (Para 305)
* **Status in Thesisv3**: *Recommended Insertion*
* **Full Sentence in Thesisv3**:
  > Passenger screening throughput temporally precedes terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turnaround times and network delays compound.
* **Callout to Insert**: `(see Appendix G)`
* **Result after Insertion**:
  > Passenger screening throughput temporally precedes terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turnaround times and network delays compound (see Appendix G).

---

## Master Lookup Table of All Anchors Across Appendices A through G

| Anchor | Target Appendix | Chapter | Section / Header | Thesisv3 Para | Status in Thesisv3 | Primary Operational Topic |
|:------:|:---------------:|:-------:|:-----------------|:-------------:|:------------------:|:--------------------------|
| **A.1** | **Appendix A** | **I** | `Delimitations` | Para 69 | Already in MS | Study scope, metrics, and temporal boundaries |
| **A.2** | **Appendix A** | **I** | `Limitations and Assumptions` | Para 71 | Already in MS | Public data constraints and load factor assumptions |
| **B.1** | **Appendix B** | **II** | `Micro-Simulation in Terminal Planning` | Para 94 | Needs insertion | Discrete Event Simulation (DES) vs alternative paradigms |
| **B.2** | **Appendix B** | **II** | `Statistical Time-Series Foundations` | Para 101 | Needs insertion | Autoregressive models (ARIMA/SARIMA) and univariate limits |
| **B.3** | **Appendix B** | **III** | `Research Approach` | Para 133 | Needs insertion | Three model families classification (deterministic, ML, hybrid) |
| **B.4** | **Appendix B** | **IV** | `Feature Engineering` | Para 244 | Needs insertion | Empirical ACRP 40 passenger show-up convolution |
| **B.5** | **Appendix B** | **IV** | `Conformal Staffing Buffers` | Para 264 | Needs insertion | Risk-adjusted volatility dynamic lane dimensioning |
| **C.1** | **Appendix C** | **II** | `Classical Queuing Theory` | Para 89 | Already in MS | NHPP limitations and batch flight arrival dynamics |
| **C.2** | **Appendix C** | **II** | `Values versus Volatility Paradigm` | Para 91 | Already in MS | Heavy-traffic Kingman queuing exponential backlog |
| **C.3** | **Appendix C** | **III** | `Core Research Variables` | Para 141 | Already in MS | Dependent variables: throughput volatility & wait times |
| **C.4** | **Appendix C** | **III** | `Validity` | Para 180 | Needs insertion | Checkpoint heterogeneity and screening mode variance |
| **C.5** | **Appendix C** | **IV** | `Zero-Bounded and Hurdle Formulations` | Para 238 | Already in MS | Tweedie compound Poisson & hurdle models |
| **C.6** | **Appendix C** | **V** | `Implications & Recommendations` | Para 331 | Already in MS | Staffing transition from static volume to volatility |
| **D.1** | **Appendix D** | **IV** | `General Model Performance (Model 2)` | Para 273 | Needs insertion | Diebold-Mariano test of forecast accuracy superiority |
| **E.1** | **Appendix E** | **I** | `Research Question` | Para 63 | Needs insertion | 4-model candidate suite across evaluation triad |
| **E.2** | **Appendix E** | **III** | `Research Hypothesis` | Para 143 | Needs insertion | The Asymmetric Trade-Off master hypothesis |
| **E.3** | **Appendix E** | **IV** | `Candidate Predictive Models` | Para 246 | Needs insertion | 3 candidate models + baseline control definitions |
| **E.4** | **Appendix E** | **IV** | `Model Performance and Hypothesis Testing` | Para 280 | Needs insertion | Master multi-pillar evaluation matrix and holdout benchmarks |
| **F.1** | **Appendix F** | **II** | `Values versus Volatility Paradigm` | Para 91 | Needs insertion | Theoretical foundation of Values vs. Volatility |
| **F.2** | **Appendix F** | **IV** | `Delay Propagation & Volatility Coupling` | Para 208 | Needs insertion | Checkpoint arrival volatility coupled with flight delay volatility |
| **G.1** | **Appendix G** | **II** | `Hybrid Architectures` | Para 113 | Needs insertion | Disruption prediction and recursive error feedback |
| **G.2** | **Appendix G** | **IV** | `Dimension 2: Resilience (Severe Disruption)` | Para 287 | Needs insertion | Empty Checkpoint Fallacy under flight delay shocks |
| **G.3** | **Appendix G** | **V** | `Passenger Show-Up Dynamics` | Para 305 | Needs insertion | Lead-lag asynchrony between security lines and departure delays |

---

*Note. This reference guide is a read-only planning specification and does not modify any manuscript Word documents. All additions must be made by the author directly in `Thesisv3.docx`. Source: `master-docs/Thesisv3.docx` and `master-docs/Master_Appendix_final.docx`. Generated: October 2026. Version: v5.25.*
