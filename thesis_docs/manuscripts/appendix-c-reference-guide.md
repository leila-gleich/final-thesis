# Appendix C In-Text Reference Guide
## *Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations*

> **Source Document**: All sentences below are quoted verbatim from **`master-docs/Thesisv3.docx`** (the current authoritative thesis draft). Paragraph numbers refer to the internal paragraph index of Thesisv3.docx.
>
> **Purpose**: This file documents every location in the thesis manuscript (Chapters II–V) where `(see Appendix C...)` callouts should be inserted. For each anchor, the **full sentence as it currently appears in the manuscript** is quoted first, followed by the exact parenthetical to insert and the precise insertion point.
>
> **Appendix C Contents Covered**:
> - **C.1** — Classical Poisson/Erlang-C Queuing Derivations
> - **C.2** — Non-Homogeneous Poisson Process (NHPP) Formulations
> - **C.3** — Kingman / Allen-Cunneen Heavy-Traffic Approximations
> - **C.4** — Tweedie-Poisson Compound Dispersion Mechanics
> - **C.5** — Volatility Target Formulations ($\sigma_{\text{TSA,hr}}$, $CV_{\text{TSA,hr}}$, $\sigma_{\text{TSA,7d}}$)
> - **Table C.1** — Summary of All Formal Volatility Definitions

> [!IMPORTANT]
> This guide was rebuilt from `Thesisv3.docx` (October 2026). An earlier draft was **significantly reorganized** — Chapter V no longer contains the "Connecting Queuing Principles to Dynamic Lane Staffing" section, Chapter III "Core Research Variables" no longer enumerates the three volatility targets explicitly, and Chapter IV "Defining Seasonality" now differs structurally. The 6 anchors below reflect what is **actually in the current thesis**.

---

## Chapter II — Review of the Relevant Literature

### Anchor 1 of 6
**Section**: `Classical Queuing Theory: Volume Versus Volatility` (Para 88–89)

**Full sentence(s) as they appear in Thesisv3.docx** (Para 88):

> Poisson arrival distributions (such as M/M/s or M/G/s queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) have been used to balance operational staffing costs against target Level of Service benchmarks (Araujo & Repolho, 2015). However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate (λ), and consequently consistently struggle to reflect non-linear dynamics and dramatic fluctuations triggered by flight banks (Wang, 2018).

**And** (Para 89):

> To address this, researchers transitioned toward Non-Homogeneous Poisson Processes (NHPP) and multiphase networks, allowing arrival rates to vary across sequential service intervals (Brunetta et al., 1999; Hess & Grbčić, 2019). NHPP formulations are constrained due to a dependence on expected mean volume and the assumption of independent arrivals, failing to account for the high correlation among passengers arriving for the same ticketed flight bank and ignoring the impact of airside connecting passengers (Adeke, 2018; Guo et al., 2022).

**Callout to insert** — append to the end of the NHPP limitation sentence (Para 89), before the period:

```
(see Appendix C, Sections C.1–C.2 for classical Poisson, Erlang-C, and NHPP mathematical derivations)
```

**Result after insertion**:
> NHPP formulations are constrained due to a dependence on expected mean volume and the assumption of independent arrivals, failing to account for the high correlation among passengers arriving for the same ticketed flight bank and ignoring the impact of airside connecting passengers (Adeke, 2018; Guo et al., 2022; see Appendix C, Sections C.1–C.2 for classical Poisson, Erlang-C, and NHPP mathematical derivations).

---

### Anchor 2 of 6
**Section**: `The "Values versus Volatility" Paradigm in Transportation Demand` (Para 91)

**Full sentence as it appears in Thesisv3.docx**:

> In operational reality, heavy-traffic queuing principles demonstrate that checkpoint wait times and passenger lines do not depend solely on average passenger volume, but on the irregularity and burstiness of passenger arrivals and processing speeds (Kingman, 1961; Whitt, 1993). As checkpoint lanes operate near full capacity during morning and evening departure peaks, any sudden increase in passenger arrival swings causes wait times and crowd congestion to grow exponentially (Adeke, 2018; Guo et al., 2022).

**Callout to insert** — append to the end of the second sentence (after the Adeke & Guo et al. citation), before the period:

```
(see Appendix C, Section C.3 for complete heavy-traffic queuing derivations)
```

**Result after insertion**:
> As checkpoint lanes operate near full capacity during morning and evening departure peaks, any sudden increase in passenger arrival swings causes wait times and crowd congestion to grow exponentially (Adeke, 2018; Guo et al., 2022; see Appendix C, Section C.3 for complete heavy-traffic queuing derivations).

---

## Chapter III — Methodology

### Anchor 3 of 6
**Section**: `Core Research Variables` (Para 141)

**Full sentence as it appears in Thesisv3.docx**:

> Dependent variables include TSA checkpoint throughput, queue wait times, and bottleneck formation rates.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C, Section C.5 and Table C.1 for formal mathematical volatility formulations)
```

**Result after insertion**:
> Dependent variables include TSA checkpoint throughput, queue wait times, and bottleneck formation rates (see Appendix C, Section C.5 and Table C.1 for formal mathematical volatility formulations).

---

### Anchor 4 of 6
**Section**: `Validity` (Para 180)

**Full sentence as it appears in Thesisv3.docx**:

> Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C for the queuing derivations justifying the volatility-over-volume construct choice)
```

**Result after insertion**:
> Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates (see Appendix C for the queuing derivations justifying the volatility-over-volume construct choice).

---

## Chapter IV — Results

### Anchor 5 of 6
**Section**: `Implications for Model Development` → Item: Zero-Bounded and Hurdle Formulations (Para 238)

**Full sentence as it appears in Thesisv3.docx**:

> Predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models or two-stage hurdle structures (a logistic model predicting whether the checkpoint is active, followed by a positive count model predicting passenger volume) – to accommodate positive throughput skewness and structural zeros without generating negative volume forecasts.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C, Section C.4 for Tweedie-Poisson compound dispersion mechanics)
```

**Result after insertion**:
> Predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models or two-stage hurdle structures (a logistic model predicting whether the checkpoint is active, followed by a positive count model predicting passenger volume) – to accommodate positive throughput skewness and structural zeros without generating negative volume forecasts (see Appendix C, Section C.4 for Tweedie-Poisson compound dispersion mechanics).

---

## Chapter V — Conclusions and Recommendations

### Anchor 6 of 6
**Section**: `Implications and Recommendations for Predictive Forecasting in Airport Operations` (Para 331)

**Full sentence as it appears in Thesisv3.docx**:

> The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C for formal queuing derivations and volatility target formulations underpinning this framework)
```

**Result after insertion**:
> The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models (see Appendix C for formal queuing derivations and volatility target formulations underpinning this framework).

---

## Summary Table

| Anchor | Chapter | Section | Appendix C Subsection(s) Referenced |
|:------:|:--------|:--------|:-------------------------------------|
| 1 | II | Classical Queuing Theory: Volume Versus Volatility | C.1–C.2 (Poisson, Erlang-C, NHPP) |
| 2 | II | The "Values versus Volatility" Paradigm in Transportation Demand | C.3 (Heavy-Traffic Queuing Derivations) |
| 3 | III | Core Research Variables | C.5, Table C.1 (Volatility Formulations) |
| 4 | III | Validity | General Appendix C (Queuing Construct Justification) |
| 5 | IV | Implications for Model Development — Zero-Bounded/Hurdle Formulations | C.4 (Tweedie-Poisson Dispersion) |
| 6 | V | Implications and Recommendations for Predictive Forecasting | General Appendix C (Queuing + Volatility Targets) |

---

## Notes on Thesisv3 Structural Changes vs. Prior Draft

> [!WARNING]
> The following sections **existed in the old draft** but are **NOT present in Thesisv3.docx** and therefore have been removed from this guide:
> - ~~Chapter II: "Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation"~~ — This standalone section no longer exists; its content is now folded into the "Values versus Volatility" paragraph (Anchor 2 above).
> - ~~Chapter IV: "Defining Seasonality / Annual Seasonal Regimes and Coupled Volatility"~~ — The seasonality section in Thesisv3 covers filtering pipeline results and descriptive statistics but does not reference $CV_{\text{TSA}}$ in a callout-suitable sentence.
> - ~~Chapter IV: "Implications for Model Development — Heavy-Traffic Queuing Dynamics (Item 4)"~~ — The Implications section in Thesisv3 is structured around four architectural requirements (single-carrier isolation, DB1B deflation, information barriers, zero-bounded formulations); there is no standalone "Heavy-Traffic Queuing Dynamics" item.
> - ~~Chapter V: "Connecting Queuing Principles to Dynamic Lane Staffing" (Items 1 & 2)~~ — Chapter V in Thesisv3 is a Conclusions and Recommendations chapter. It does not contain a "Connecting Queuing Principles" section or a "Volatility-Buffered Lane Dimensioning" derivation.

---

*Note. This reference guide is a read-only planning document and does not modify any manuscript files. All insertions must be applied manually by the author in the corresponding Word (.docx) thesis chapter files. Source: `master-docs/Thesisv3.docx`. Generated: October 2026. Version: v5.22.*
