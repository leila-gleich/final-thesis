# CHAPTER III SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DOCUMENT: Chapter III Single Source of Truth (SSOT) Reference Specification
RELEASE VERSION: v4.0 (SemVer-Data) | DATE: October 2026
CANONICAL LOCATION: thesis_docs/ssot/Chapter_3_SSOT.md
COMPANION DRAFT: thesis_docs/manuscripts/Chapter_3_Methodology.md
====================================================================================================

## 1. PURPOSE AND SCOPE OF THE SSOT DOCUMENT

This document serves as the **definitive, immutable Single Source of Truth (SSOT)** for Chapter III (Methodology) of the graduate thesis.

It defines all mathematical formulations, the four-tiered filtering pipeline, the 84-cell interaction tensor ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$), Candidate B dataset partitioning, degrees-of-freedom proofs, model architectural specifications (Baseline Control, Model 1, Model 2, and Model 3), and the formal evaluation metrics for the three operational dimensions (Robustness, Resilience, Generalizability). Every equation, filter rule, and sample size certified here is binding across the thesis.

---

## 2. CANONICAL CHAPTER III OUTLINE ARCHITECTURE

Chapter III is structured into five core methodological components matching the authorized committee manuscript architecture:

```
CHAPTER III: METHODOLOGY
├── 3.1 Research Approach
│   ├── Theoretical Framework & Stochastic Queuing Principles (Kingman Formula, Ca^2)
│   ├── Core Research Variables (Independent, Dependent Volatility Targets, Performance)
│   ├── Research Hypotheses (H1 Master Asymmetric Trade-Off, H1A, H1B, H1C)
│   ├── Design and Procedures (Phases 1–4, Model Suite, Partitioning, Evaluation Regimes)
│   └── Apparatus and Materials (Google Antigravity & Python, Excel/Power BI, Vega HPC Cluster)
├── 3.2 Sample
│   ├── Macro Categorization: Terminal-to-Airline Distribution (Four Structural Archetypes)
│   ├── Micro-Level Refinement: Checkpoint Co-Location & Isolation (Centralized vs. Decentralized)
│   ├── Four-Tiered Purposive Filtering Pipeline & Southwest Exclusion
│   ├── Balanced Factorial Cohort (9 Airfields, 3 Carriers, 12 Screening Complexes)
│   └── Temporal Scope and Boundary Definition (Pre-Pandemic Baseline, Candidate B Demarcation)
├── 3.3 Sources of Data
│   ├── TSA FOIA Security Screening Checkpoint Logs (6,434,732 lane-hours, 2.70B pax)
│   ├── BTS On-Time Flight Performance Form 234 (13,153,654 departures)
│   ├── BTS Form 41 Schedule T-100 Domestic Segment Capacity (422,096 route-months)
│   └── BTS DB1B Origin & Destination Ticket Surveys and Airport Reports (22,051,557 coupons)
├── 3.4 Validity
│   ├── Internal Validity Threats & Remediation (Connecting Passenger Hub Disconnect, Partition Buffers, Airspace Shocks)
│   ├── Construct Validity Threats & Remediation (Screening Lane Heterogeneity, Scale-Free CV)
│   └── Mathematical Formulation of Volatility Targets (σ_TSA,hr, CV_TSA,hr, σ_TSA,7d, σ_Delay, CVI, T_dow)
└── 3.5 Treatment of Data
    ├── Sequential Extract Pipeline (FOIA PDFs, Tabular CSVs, BTS Feeds, Longitudinal Audits)
    ├── Sequential Transform Pipeline (Clock Normalization, Spatial Key Resolution, Structural Zeros, ACRP-40 Convolution)
    ├── Feature Space Engineering (Values vs. Volatility: 14 Values, 10 Volatilities, 24 Combined)
    └── Sequential Load Pipeline (Master Warehouses, Analytic Lookup Tensors, Verification Audits)
```

---

## 3. MASTER MATHEMATICAL REGISTRY

### 3.1 Queuing Intensity and Capacity Mechanics

The traffic intensity $\rho(t)$ at a screening complex with $c(t)$ active physical lanes, hourly passenger arrival rate $\lambda(t)$, and mean lane service rate $\mu$:
$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$

* **Macro Threshold**: Top 25 hubs routinely operate at peak $\rho(t) \to 1.0$ (05:00–08:30 and 16:00–18:30), creating non-linear queuing delays. Regional hubs operate at $\rho(t) \ll 0.3$, failing to exhibit queuing resistance.

### 3.2 Passenger Arrival Timing Distributions

1. **Legacy Network Carrier Unimodal Lognormal Distribution** (American, Delta, United):
   $$\tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105 \text{ minutes}$$
2. **Southwest Airlines (WN) Bimodal Arrival Mixture** (Open-seating / boarding group positioning):
   $$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$
   where $\mu_1 \approx 135 \text{ minutes}$ (boarding position maximizers) and $\mu_2 \approx 65 \text{ minutes}$ (carry-on business travelers). Southwest is systematically excluded to prevent arrival distribution contamination.

### 3.3 Carrier Checkpoint Isolation Condition

$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0, \quad \kappa < 25$$
where $\kappa$ is the multicollinearity condition number between competing airline flight schedules.

### 3.4 Connecting Passenger Deflator (The Hub Disconnect)

$$\text{Demand}_{\text{originating}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$
where $\text{ConnectingRatio}_{\text{airport}}$ is derived from quarterly BTS DB1B ticket survey coupons.

### 3.5 Checkpoint Complex Aggregation

$$Y_{kt} = \sum_{l \in \mathcal{L}_k} y_{k,l,t}$$
Aggregates hourly counts across all physical screening lanes $l \in \mathcal{L}_k$ within dedicated terminal screening complex $k$, neutralizing administrative TSO lane-rebalancing noise.

### 3.6 Coupled Volatility Metrics

1. **Within-Day TSA Screening Volatility ($CV_{\text{TSA}, d}$)**:
   $$CV_{\text{TSA}, d} = \frac{\sigma_{\text{hourly},\text{TSA}, d}}{\mu_{\text{hourly},\text{TSA}, d}} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (\text{TSA}_{d,h} - \bar{\text{TSA}}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} \text{TSA}_{d,h}}$$

2. **Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)**:
   $$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$

3. **Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)**:
   $$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

4. **Coupled Volatility Index ($\text{CVI}_d$)**:
   $$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

### 3.7 Diurnal Operational Turbulence Shock Index ($T_{dow}(h)$)

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$
where $\mathbb{I}(\bar{F}_{dow}(h) \ge 20)$ suppresses overnight curfew hours with sparse flight operations.

### 3.8 The 84-Cell Interaction Tensor ($\mathcal{G}$)

$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \times 7 \times 3 = 84 \text{ cells})$$
* **$\mathcal{S}$ (4 Annual Regimes)**: `1_OFF_PEAK`, `2_MID_PEAK`, `3_PEAK`, `4_HOLIDAY`.
* **$\mathcal{D}$ (7 Days of Week)**: Monday (1) through Sunday (7), ISO 8601.
* **$\mathcal{H}$ (3 Diurnal Regimes)**: `1_OFF_PEAK` ($T < 0.35$), `2_MID_PEAK` ($0.35 \le T < 0.75$), `3_PEAK` ($T \ge 0.75$).

---

## 4. THE CANDIDATE PREDICTIVE MODELS AND BASELINE CONTROL

Following the Phase 2 Four-Tiered Purposive Filtering pipeline (Macro congestion, Meso airspace invariance, Micro checkpoint exclusivity, and balanced factorial design), the research evaluates **three candidate predictive models representing distinct operational paradigms**, benchmarked against an empirical baseline control:

| Model ID | Paradigm | Formal Nomenclature | Algorithmic Formulation | Primary Explanatory Features & Role |
| :--- | :--- | :--- | :--- | :--- |
| **Baseline Control** | **Baseline Control** | Diurnal Volatility Naive Persistence | $\widehat{\text{Vol}}_{\text{Base}, t} = \text{Vol}_{t-24}$ | Historical lagged checkpoint volatility 24 hours prior; scale-free MASE denominator. |
| **Model 1** | **Deterministic Baseline** | Deterministic Flight Schedule Model | $\widehat{\text{Vol}}_{1, t} = \beta_0 + \beta_1 \cdot \text{Vol}_{\text{sched\_conv}, t}$ | Scheduled flight bank departure dispersion convolved with ACRP Report 40 passenger arrival curves; **Generalizability Winner**. |
| **Model 2** | **Machine Learning** | Supervised Machine Learning Model | $\widehat{\text{Vol}}_{2, t} = f_{\text{Tree}}(\mathbf{x}_t^{\text{convolved}}, \mathbf{x}_t^{\text{Values}}, \mathbf{x}_t^{\text{Volatilities}})$ | Convolved arrivals + 24 OTP feature attributes (14 values, 10 volatilities); **Routine Pareto Winner**. |
| **Model 3** | **Dynamic Hybrid** | Dynamic Two-Stage Hybrid Model | $\widehat{\text{Vol}}_{3, t} = \widehat{\text{Vol}}_{\text{Schedule}, t} + g_{\text{Tree}}(\mathbf{x}_t^{\text{airside}}, e_{t-1})$ | Stage 1 schedule cycles + Stage 2 decision tree with **live 1-step error innovation feedback ($e_{t-1}$)**; **Resilience Winner**. |

---

## 5. FORMAL EVALUATION METRICS REGISTRY AND EXPLICIT ACADEMIC TARGETS

1. **Root Mean Squared Error (RMSE)**:
   $$\text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (\text{Vol}_t - \widehat{\text{Vol}}_t)^2}$$
2. **Mean Absolute Scaled Error (MASE)** (Hyndman & Koehler, 2006):
   $$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N |\text{Vol}_t - \widehat{\text{Vol}}_t|}{\frac{1}{N-24}\sum_{t=25}^N |\text{Vol}_t - \text{Vol}_{t-24}|}$$
3. **Dimension 1: Robustness Operational Regime and Targets**:
   - *Operational Regime*: Nominal flight operations ($\text{DepDelay} < 15\text{ min}$, zero flight cancellations).
   - *Explicit Targets*: $\mathbf{\min \text{RMSE}_{\text{routine}}}$ and $\mathbf{\text{MASE}_{\text{routine}} < 0.700}$.
4. **Dimension 2: Resilience Operational Regime and Targets**:
   - *Operational Regime*: Severe systemic disruptions ($\text{DepDelay} \ge 45\text{ min}$ or cancellations $\ge 5$).
   - *Governing Metrics*: Disruption Error Multiplier $R_{\text{RMSE}} = \frac{\text{RMSE}_{\text{shock}}}{\text{RMSE}_{\text{routine}}}$, $R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$, Shock MASE ($\text{MASE}_{\text{shock}}$), Time-to-Recovery ($\text{TTR}$).
   - *Explicit Targets*: $\mathbf{R_{\text{RMSE}} \approx 1.00 \ (R_{\text{MASE}} \approx 1.00)}$, $\mathbf{\min \text{MASE}_{\text{shock}}}$, and $\mathbf{\text{TTR} < 4.0\text{ hours}}$.
5. **Dimension 3: Generalizability Operational Regime and Targets**:
   - *Operational Regime*: Zero-shot spatial deployment from Source (EWR) to Target (LGA) without local retraining.
   - *Governing Metrics*: Relative Transfer Ratio $\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$, Percentage Change in MASE on Transfer $\Delta\text{MASE}_{\text{transfer}} = \frac{\Delta\text{MASE}}{\text{MASE}_{\text{in}}} \times 100\%$.
   - *Explicit Targets*: $\mathbf{\text{RTR} \approx 1.00 \ (1.00 \pm 0.05)}$ and $\mathbf{\Delta\text{MASE}_{\text{transfer}} \le 10.0\%}$.
6. **Diebold-Mariano Hypothesis Test Statistic ($DM$)**:
   $$DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d}) / N}} \sim \mathcal{N}(0, 1)$$
   Evaluates statistical significance of loss differentials relative to the deterministic benchmark ($p < 0.001$).

---

## 6. CANONICAL DATASET PARTITIONS (CANDIDATE B)

* **Baseline Longitudinal Warehouse**: Jan 1, 2019 to Dec 31, 2025 (7 continuous years; 61,344 calendar hours).
* **Demarcation Cutoff**: May 1, 2022 (44 continuous post-mask-mandate months).
* **Development Partition (32 Months)**: May 1, 2022 to Dec 31, 2024 ($975$ calendar days = $23,400$ system hours).
  * **Training Fold**: May 1, 2022 to Dec 31, 2023 (20 months; **122,847 observations** in 9-airport filtered complex cohort).
  * **Validation Fold**: Jan 1, 2024 to Dec 31, 2024 (12 months; **72,723 observations** in 9-airport filtered complex cohort).
  * **Inter-Fold Separation Buffer**: 7 calendar days (**2,837 observations**) to purge serial delay autocorrelation.
* **Testing Holdout Partition (12 Months)**: Jan 1, 2025 to Dec 31, 2025 ($365$ calendar days = $8,760$ system hours; **72,053 observations** in 9-airport filtered complex cohort; **215,562 facility screening hours** across candidate network).
* **Total Modeled Complex Dataset**: **270,460 observations**.

---

## 7. STATISTICAL DEGREES-OF-FREEDOM PROOFS

* **Training Viability ($N_{\text{train}} \ge 50$)**: Exactly **83 of 84 cells (98.8%)** meet or exceed the threshold (Median $N_{\text{train}} = 215$). The sole cell with $N = 48$ is Holiday Off-Peak Overnight ($00:00\text{--}03:00$).
* **Well-Powered Tree Splits ($N_{\text{train}} \ge 100$)**: **65 of 84 cells (77.4%)** exceed 100 observations.
* **CLT Sample Size Sufficiency ($N_{\text{test}} \ge 30$)**: **70 of 84 cells (83.3%)** meet Central Limit Theorem sample size requirements (Median $N_{\text{test}} = 76$). Remaining cells have 18 to 24 observations, fully satisfying non-parametric Wilcoxon rank-sum and Diebold-Mariano testing requirements.

---

## 8. TERMINOLOGY & GOVERNANCE RULES

Strictly enforce `thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`:
* **Use**: "Empirical Passenger Show-Up Curve" (or "Lead-Lag Passenger Arrival Distribution"). **Never use**: "physics-based continuous arrival kernel convolution".
* **Use**: "Carrier Checkpoint Isolation". **Never use**: "orthogonal Wiener-Hopf deconvolution operator".
* **Use**: "Connecting Passenger Deflator" (or "The Hub Disconnect"). **Never use**: "DB1B transfer deflation manifold".
* **Use**: "Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability". **Never use**: "cyber-physical stability manifolds".

---

## 9. CROSS-CHAPTER INTEGRATION ROADMAP

* **Handoff from Chapter I & II**: Chapter I provides the research questions and delimitations; Chapter II provides the theoretical foundation and literature gap; Chapter III provides the mathematical formulations and execution pipeline.
* **Handoff to Chapter IV (Findings)**: Chapter III defines the 84-cell interaction grid, the Candidate B partition counts, and the candidate model suite; Chapter IV reports the empirical results (descriptive stats, filtering yield, model error tables, Diebold-Mariano tests).
* **Handoff to Chapter V (Discussion)**: Chapter III specifies the three evaluation metrics ($RMSE, R_{\text{MASE}}, RTR$); Chapter V evaluates $H_{1a}, H_{1b}, H_{1c}$ against these metrics to synthesize the Regime-Switched Gated Inference Engine.

====================================================================================================
END OF CHAPTER III SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
