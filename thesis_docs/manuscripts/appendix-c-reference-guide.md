# Appendix C In-Text Reference Guide
## *Queuing Theory Derivations, Heavy-Traffic Approximations, and Volatility Dispersion Formulations*

> **Purpose**: This file documents every location in the thesis manuscript (Chapters II–V) where `(see Appendix C...)` callouts should be inserted. For each anchor, the **full sentence as it currently appears in the manuscript** is quoted first, followed by the exact parenthetical to insert and the precise insertion point.
>
> **Appendix C Contents Covered**:
> - **C.1** — Classical Poisson/Erlang-C Queuing Derivations
> - **C.2** — Non-Homogeneous Poisson Process (NHPP) Formulations
> - **C.3** — Kingman / Allen-Cunneen Heavy-Traffic Approximations
> - **C.4** — Tweedie-Poisson Compound Dispersion Mechanics
> - **C.5** — Volatility Target Formulations ($\sigma_{\text{TSA,hr}}$, $CV_{\text{TSA,hr}}$, $\sigma_{\text{TSA,7d}}$)
> - **Table C.1** — Summary of All Formal Volatility Definitions

---

## Chapter II — Literature Review

### Anchor 1 of 9
**Section**: `### Classical Queuing Theory: Volume Versus Volatility`

**Full sentence (as it appears in the manuscript)**:

> While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP; Brunetta et al., 1999) to incorporate time-varying arrival rates $\lambda(t)$... NHPP models remain conceptually constrained because they model only mean arrival rate dynamics and cannot represent the second-order variance structure of arrival burstiness critical to understanding queue backlog formation.

**Callout to insert** — append to the end of the NHPP limitation sentence, before the period:

```
(see Appendix C, Sections C.1–C.2 for classical Poisson, Erlang-C, and NHPP mathematical derivations)
```

**Result after insertion**:
> ...NHPP models remain conceptually constrained because they model only mean arrival rate dynamics and cannot represent the second-order variance structure of arrival burstiness critical to understanding queue backlog formation (see Appendix C, Sections C.1–C.2 for classical Poisson, Erlang-C, and NHPP mathematical derivations).

---

### Anchor 2 of 9
**Section**: `### Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation`

**Full sentence (as it appears in the manuscript)**:

> Modeling and forecasting throughput volatility ($\sigma_{\text{TSA}}$ and $\text{CV}_{\text{TSA}}$) is therefore the vital prerequisite for robust lane staffing, operational stability, and passenger delay mitigation (Adeke, 2018; Guo et al., 2022).

**Callout to insert** — append to the end of the final sentence in this section, before the period:

```
(see Appendix C, Section C.3 for complete heavy-traffic queuing derivations and multi-server utilization thresholds)
```

**Result after insertion**:
> Modeling and forecasting throughput volatility ($\sigma_{\text{TSA}}$ and $\text{CV}_{\text{TSA}}$) is therefore the vital prerequisite for robust lane staffing, operational stability, and passenger delay mitigation (Adeke, 2018; Guo et al., 2022; see Appendix C, Section C.3 for complete heavy-traffic queuing derivations and multi-server utilization thresholds).

---

### Anchor 3 of 9
**Section**: `### The "Values versus Volatility" Paradigm in Transportation Demand`

**Full sentence (as it appears in the manuscript)**:

> The within-day standard deviation ($\sigma_{\text{TSA, hr}}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($\text{Var}(Y) \propto \mu^p$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C, Section C.4 for compound Poisson dispersion mechanics)
```

**Result after insertion**:
> The within-day standard deviation ($\sigma_{\text{TSA, hr}}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($\text{Var}(Y) \propto \mu^p$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor (see Appendix C, Section C.4 for compound Poisson dispersion mechanics).

---

## Chapter III — Methodology

### Anchor 4 of 9
**Section**: `### Core Research Variables`

**Full sentence (as it appears in the manuscript)**:

> Dependent Variables: Volatility of Transportation Security Administration (TSA) security checkpoint passenger throughput across multiple operational horizons (intraday diurnal absolute dispersion $\sigma_{\text{TSA, hr}}$, intraday scale-free relative volatility $CV_{\text{TSA, hr}}$, and multi-day temporal rolling volatility $\sigma_{\text{TSA, 7d}}$), queue wait times, and bottleneck formation rates.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C, Section C.5 and Table C.1 for formal mathematical volatility formulations and construct definitions)
```

**Result after insertion**:
> Dependent Variables: Volatility of Transportation Security Administration (TSA) security checkpoint passenger throughput across multiple operational horizons (intraday diurnal absolute dispersion $\sigma_{\text{TSA, hr}}$, intraday scale-free relative volatility $CV_{\text{TSA, hr}}$, and multi-day temporal rolling volatility $\sigma_{\text{TSA, 7d}}$), queue wait times, and bottleneck formation rates (see Appendix C, Section C.5 and Table C.1 for formal mathematical volatility formulations and construct definitions).

---

### Anchor 5 of 9
**Section**: `## Validity`

**Full sentence (as it appears in the manuscript)**:

> Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C for the queuing derivations justifying the volatility-over-volume construct choice)
```

**Result after insertion**:
> Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates (see Appendix C for the queuing derivations justifying the volatility-over-volume construct choice).

> [!NOTE]
> The next sentence in the manuscript already contains an existing callout to Appendix D, Appendix E, and Appendix J. **Do not replace it** — insert the Appendix C callout only in the sentence above, as shown.

---

## Chapter IV — Findings, Discussion, and Conclusions

### Anchor 6 of 9
**Section**: `### Defining Seasonality` → `#### Annual Seasonal Regimes and Coupled Volatility`

**Full sentence (as it appears in the manuscript)**:

> By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b).

**Callout to insert** — append after "(Table 4.3b)", before the period:

```
(see Appendix C, Section C.5 for scale-free relative arrival volatility formulations)
```

**Result after insertion**:
> By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b; see Appendix C, Section C.5 for scale-free relative arrival volatility formulations).

---

### Anchor 7 of 9
**Section**: `### Implications for Model Development` — Item 4: Heavy-Traffic Queuing Dynamics

**Full sentence (as it appears in the manuscript)**:

> Consequently, predicting the volatility of TSA throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is fundamentally more consequential for checkpoint stability than forecasting average volume alone.

**Callout to insert** — append to the end of this sentence, before the period:

```
(see Appendix C, Section C.3 for mathematical derivations and multi-lane utilization thresholds)
```

**Result after insertion**:
> Consequently, predicting the volatility of TSA throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is fundamentally more consequential for checkpoint stability than forecasting average volume alone (see Appendix C, Section C.3 for mathematical derivations and multi-lane utilization thresholds).

---

## Chapter V — Analysis and Recommendations

### Anchor 8 of 9
**Section**: `### Connecting Queuing Principles to Dynamic Lane Staffing` — Item 1: The Checkpoint Tipping Point

**Full sentence (as it appears in the manuscript)**:

> When screening lanes operate near capacity ($\rho \ge 0.85\text{--}0.90$), the multiplier $\frac{\rho}{c(1-\rho)}$ grows exponentially. Even a modest burst of arriving passengers ($C_a^2$) instantly tips the checkpoint into a runaway queue backlog.

**Callout to insert** — append to the end of the final sentence in this item ("...runaway queue backlog."), before the period:

```
(see Appendix C, Section C.3 for complete heavy-traffic queuing derivations)
```

**Result after insertion**:
> Even a modest burst of arriving passengers ($C_a^2$) instantly tips the checkpoint into a runaway queue backlog (see Appendix C, Section C.3 for complete heavy-traffic queuing derivations).

---

### Anchor 9 of 9
**Section**: `### Connecting Queuing Principles to Dynamic Lane Staffing` — Item 2: Volatility-Buffered Lane Dimensioning

**Full sentence (as it appears in the manuscript)**:

> To solve this, airport checkpoint administrators can translate predicted throughput volatility ($\hat{\sigma}_{\text{TSA}, t}$) directly into risk-buffered lane configurations using conformal prediction principles: [equation] ...where $\mu_{\text{lane}}$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $z_q$ is the coverage quantile factor.

**Callout to insert** — append to the end of the equation note sentence (after the $z_q$ definition), before the period:

```
(see Appendix C for heavy-traffic queuing bounds and volatility target formulations)
```

**Result after insertion**:
> ...where $\mu_{\text{lane}}$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $z_q$ is the coverage quantile factor (see Appendix C for heavy-traffic queuing bounds and volatility target formulations).

---

## Summary Table

| Anchor | Chapter | Section | Appendix C Subsection(s) Referenced |
|:------:|:--------|:--------|:-------------------------------------|
| 1 | II | Classical Queuing Theory: Volume Versus Volatility | C.1–C.2 (Poisson, Erlang-C, NHPP) |
| 2 | II | Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation | C.3 (Heavy-Traffic Queuing) |
| 3 | II | The "Values versus Volatility" Paradigm | C.4 (Tweedie-Poisson Dispersion) |
| 4 | III | Core Research Variables | C.5, Table C.1 (Volatility Formulations) |
| 5 | III | Validity | General Appendix C (Queuing Derivations) |
| 6 | IV | Annual Seasonal Regimes and Coupled Volatility | C.5 (Scale-Free Relative Volatility) |
| 7 | IV | Implications for Model Development — Item 4 | C.3 (Multi-Lane Heavy-Traffic Derivations) |
| 8 | V | Connecting Queuing Principles — Item 1 (Checkpoint Tipping Point) | C.3 (Complete Heavy-Traffic Derivations) |
| 9 | V | Connecting Queuing Principles — Item 2 (Lane Dimensioning) | General Appendix C (Bounds + Formulations) |

---

*Note. This reference guide is a read-only planning document and does not modify any manuscript files. All insertions must be applied manually by the author in the corresponding Word (.docx) thesis chapter files. Generated: October 2026. Version: v5.21.*
