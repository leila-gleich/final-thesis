# Appendix B In-Text Reference Guide
## *Comparative Modeling Paradigms and Literature Equation Registry*

> **Source Document**: All sentences below are quoted verbatim from **`master-docs/Thesisv3.docx`** (the current authoritative thesis draft). Paragraph numbers refer to the internal paragraph index of `Thesisv3.docx`.
>
> **Purpose**: This guide specifies every location across the thesis chapters (Chapters II, III, and IV) where in-text references to **Appendix B** should be inserted. For each anchor, the **full sentence as it currently appears in `Thesisv3.docx`** is quoted first, followed by the exact parenthetical callout to insert and the resulting sentence.
>
> **Appendix B Contents Covered**:
> - **Section B.1**: *Comparative Modeling Paradigm Taxonomy for Airport Screening Facilities* (Detailed operational trade-offs across Classical Queuing, Discrete Event Simulation [DES], Linear Statistical Time Series [ARIMA/SARIMA], Deep Sequence Neural Networks [LSTM/GRU], Supervised Machine Learning Ensembles, and Sequential Two-Stage Dynamic Hybrids).
> - **Table B.1**: *Comparative Modeling Paradigm Taxonomy for Airport Security Screening Facilities* (Summary comparison matrix spanning computational latency, explainability, and disruption behavior).
> - **Table B.2**: *Master Literature Equation Registry: 20 Peer-Reviewed Operational Equations* (Cataloging all 20 formal equations utilized in the thesis, including Kingman queuing, ACRP Report 40 lead-lag show-up distributions, DB1B connecting passenger deflation, forecast evaluation metrics, econometric tests, and conformal dynamic lane staffing bounds).

---

## Chapter II — Review of the Relevant Literature

### Anchor 1 of 11
**Section**: `From Analytical Queuing to Simulation Modeling and Real-Time Management` → `Micro-Simulation in Terminal Planning and Asset Allocation` (Para 94)

**Full sentence as it appears in Thesisv3.docx**:

> To overcome the rigid mathematical assumptions of analytical queuing equations, airport planners widely adopted micro-simulation – a modeling approach that simulates individual system entities rather than aggregate flows – primarily implemented through Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011; Verki et al., 2013).

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Section B.1 and Table B.1 for a comparative taxonomy of discrete-event simulation versus alternative terminal modeling paradigms)
```

**Result after insertion**:
> To overcome the rigid mathematical assumptions of analytical queuing equations, airport planners widely adopted micro-simulation – a modeling approach that simulates individual system entities rather than aggregate flows – primarily implemented through Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011; Verki et al., 2013; see Appendix B, Section B.1 and Table B.1 for a comparative taxonomy of discrete-event simulation versus alternative terminal modeling paradigms).

---

### Anchor 2 of 11
**Section**: `Advanced Predictive Models and Machine Learning` → `Statistical Time-Series Foundations and Linear Limitations` (Para 101)

**Full sentence as it appears in Thesisv3.docx**:

> However, while SARIMA excels at internal pattern recognition, because it relies on historical data, it does not account for the direct correlation between fluctuating passenger volumes and specific, real-time flight arrangements (Lin et al., 2023).

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Section B.1 for structural limitations and operational trade-offs of linear statistical time-series models)
```

**Result after insertion**:
> However, while SARIMA excels at internal pattern recognition, because it relies on historical data, it does not account for the direct correlation between fluctuating passenger volumes and specific, real-time flight arrangements (Lin et al., 2023; see Appendix B, Section B.1 for structural limitations and operational trade-offs of linear statistical time-series models).

---

### Anchor 3 of 11
**Section**: `Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability` (Para 113)

**Full sentence as it appears in Thesisv3.docx**:

> Finally, during catastrophic ground stops where static schedules collapse and falsely predict zero demand (the "Empty Checkpoint Fallacy"), incorporating recursive real-time error feedback allows models to monitor live checkpoint sensors and dynamically update queue states, ensuring rapid recovery (Anupam & Lawal, 2024; Ebert et al., 2021; Wu et al., 2024).

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Section B.1 and Table B.1 for complete operational comparisons across all six candidate modeling paradigms)
```

**Result after insertion**:
> Finally, during catastrophic ground stops where static schedules collapse and falsely predict zero demand (the "Empty Checkpoint Fallacy"), incorporating recursive real-time error feedback allows models to monitor live checkpoint sensors and dynamically update queue states, ensuring rapid recovery (Anupam & Lawal, 2024; Ebert et al., 2021; Wu et al., 2024; see Appendix B, Section B.1 and Table B.1 for complete operational comparisons across all six candidate modeling paradigms).

---

## Chapter III — Methodology

### Anchor 4 of 11
**Section**: `Research Approach` (Para 133)

**Full sentence as it appears in Thesisv3.docx**:

> Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Section B.1 and Table B.1 for formal classification and operational characteristics of candidate modeling paradigms)
```

**Result after insertion**:
> Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects (see Appendix B, Section B.1 and Table B.1 for formal classification and operational characteristics of candidate modeling paradigms).

---

### Anchor 5 of 11
**Section**: `Validity` (Para 180)

**Full sentence as it appears in Thesisv3.docx**:

> To reduce this bias, origin-and-destination data is used to estimate and remove connecting traffic from passenger flow calculations.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equation EQ-06 for the formal mathematical accounting identity)
```

**Result after insertion**:
> To reduce this bias, origin-and-destination data is used to estimate and remove connecting traffic from passenger flow calculations (see Appendix B, Table B.2, Equation EQ-06 for the formal mathematical accounting identity).

---

## Chapter IV — Results

### Anchor 6 of 11
**Section**: `The Hub Disconnect` (Para 207)

**Full sentence as it appears in Thesisv3.docx**:

> Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equation EQ-06 for the DB1B originating passenger demand accounting formulation)
```

**Result after insertion**:
> Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling (see Appendix B, Table B.2, Equation EQ-06 for the DB1B originating passenger demand accounting formulation).

---

### Anchor 7 of 11
**Section**: `Implications for Model Development` → `Connecting Passenger Deflation via DB1B Surveys` (Para 234)

**Full sentence as it appears in Thesisv3.docx**:

> Connecting Passenger Deflation via DB1B Surveys: Departing seat capacity must be deflated by empirical BTS DB1B connecting ratios:

**Callout to insert** — append after the colon / heading text:

```
(see Appendix B, Table B.2, Equation EQ-06)
```

**Result after insertion**:
> Connecting Passenger Deflation via DB1B Surveys: Departing seat capacity must be deflated by empirical BTS DB1B connecting ratios (see Appendix B, Table B.2, Equation EQ-06):

---

### Anchor 8 of 11
**Section**: `Model Development and Execution` → `Feature Engineering` (Para 244)

**Full sentence as it appears in Thesisv3.docx**:

> Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985), and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061).

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equations EQ-04 and EQ-07 for lognormal arrival distributions and discrete empirical convolution formulas)
```

**Result after insertion**:
> Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985), and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061; see Appendix B, Table B.2, Equations EQ-04 and EQ-07 for lognormal arrival distributions and discrete empirical convolution formulas).

---

### Anchor 9 of 11
**Section**: `Model Testing` (Para 257)

**Full sentence as it appears in Thesisv3.docx**:

> Models were benchmarked across standard operational performance criteria: Coefficient of Determination (), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equations EQ-09, EQ-10, EQ-13, EQ-14, and EQ-15 for formal mathematical formulations of all evaluation metrics)
```

**Result after insertion**:
> Models were benchmarked across standard operational performance criteria: Coefficient of Determination (), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias (see Appendix B, Table B.2, Equations EQ-09, EQ-10, EQ-13, EQ-14, and EQ-15 for formal mathematical formulations of all evaluation metrics).

---

### Anchor 10 of 11
**Section**: `Implications for Final Result Interpretation` → `Conformal Staffing Buffers` (Para 264)

**Full sentence as it appears in Thesisv3.docx**:

> Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equation EQ-20 for the conformal volatility-buffered dynamic lane staffing formulation)
```

**Result after insertion**:
> Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility (see Appendix B, Table B.2, Equation EQ-20 for the conformal volatility-buffered dynamic lane staffing formulation).

---

### Anchor 11 of 11
**Section**: `General Model Performance Across the 9-Airport Cohort` → `Supervised Machine Learning (Model 2)` (Para 273)

**Full sentence as it appears in Thesisv3.docx**:

> Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ().

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix B, Table B.2, Equation EQ-11 for the formal econometric derivation and Newey-West HAC variance formulation)
```

**Result after insertion**:
> Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive (see Appendix B, Table B.2, Equation EQ-11 for the formal econometric derivation and Newey-West HAC variance formulation).

---

## Summary Table of All 11 Appendix B Reference Anchors

| Anchor | Chapter | Section / Header | Thesisv3 Para | Appendix B Element Referenced | Primary Topic / Operational Rationale |
|:------:|:-------:|:-----------------|:-------------:|:------------------------------|:---------------------------------------|
| **1** | **II** | `Micro-Simulation in Terminal Planning` | Para 94 | Section B.1, Table B.1 | Discrete Event Simulation (DES) vs alternative modeling paradigms |
| **2** | **II** | `Statistical Time-Series Foundations` | Para 101 | Section B.1 | Structural limitations and operational trade-offs of ARIMA/SARIMA models |
| **3** | **II** | `Hybrid Architectures` | Para 113 | Section B.1, Table B.1 | Comprehensive comparison of all 6 candidate modeling paradigms |
| **4** | **III** | `Research Approach` | Para 133 | Section B.1, Table B.1 | Three candidate model families (deterministic, ML, dynamic hybrid) |
| **5** | **III** | `Validity` | Para 180 | Table B.2 (EQ-06) | DB1B connecting passenger deflation accounting identity |
| **6** | **IV** | `The Hub Disconnect` | Para 207 | Table B.2 (EQ-06) | Originating passenger demand formula eliminating transfer inflation |
| **7** | **IV** | `Implications for Model Development` | Para 234 | Table B.2 (EQ-06) | Mathematical definition of connecting passenger deflation |
| **8** | **IV** | `Feature Engineering` | Para 244 | Table B.2 (EQ-04, EQ-07) | ACRP Report 40 lognormal distribution and 3-hour lead-lag convolution |
| **9** | **IV** | `Model Testing` | Para 257 | Table B.2 (EQ-09, 10, 13–15) | Formal mathematical formulations of evaluation metrics ($R^2$, RMSE, MAE, MASE, Bias) |
| **10** | **IV** | `Conformal Staffing Buffers` | Para 264 | Table B.2 (EQ-20) | Conformal dynamic volatility-buffered lane dimensioning formula |
| **11** | **IV** | `General Model Performance (Model 2)`| Para 273 | Table B.2 (EQ-11) | Diebold-Mariano econometric test and Newey-West HAC variance formulation |

---

*Note. This reference guide is a read-only planning document and does not modify any manuscript files. All insertions must be applied manually by the author in the corresponding Word (`Thesisv3.docx`) chapter files. Source: `master-docs/Thesisv3.docx`. Generated: October 2026. Version: v5.24.*
