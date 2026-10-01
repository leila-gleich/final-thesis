# CHAPTER III – METHODOLOGY

## 1.1 Context and Operational Motivation
The methodological design follows the same operational motivations outlined in Chapter I: passenger‑screening checkpoints are a stochastic, demand‑driven subsystem whose capacity must be matched to landside arrivals.  To examine this, we construct a data‑centric pipeline that (i) captures the lead‑lag relationship between scheduled seats and actual checkpoint throughput, (ii) isolates carrier‑exclusive checkpoint flows, and (iii) quantifies volatility across temporal regimes.

## 1.2 Significance of the Study
By formalizing a **four‑tiered purposive filtering** process (macro‑scale congestion, meso‑scale airspace shock invariance, micro‑scale carrier‑checkpoint isolation, and balanced factorial cohort) we create a clean experimental dataset that eliminates confounding influences.  This enables a fair comparison of forecasting paradigms under the three evaluation dimensions (robustness, resilience, generalizability).

## 1.3 Statement of the Problem
Existing forecasting research suffers from three methodological gaps:
1. **Inadequate demand definition** – conflating total airline seats with checkpoint demand ignores the hub‑disconnect.
2. **Lack of regime‑aware training** – models trained on pooled data are dominated by extreme weather outliers, degrading routine‑day accuracy.
3. **Insufficient cross‑airport validation** – most studies train and test on a single airport, providing no evidence of portability.
Our methodology directly addresses these gaps.

## 1.4 Purpose Statement
The purpose of this chapter is to (a) describe the construction of a **conformed analytical warehouse** integrating TSA FOIA logs, BTS OTP, Form 41, and DB‑1B coupon surveys; (b) detail the **purposive four‑tier filtering** that yields a 9‑airport balanced experimental cohort; and (c) define the **forecasting model suite (M0‑M5)** with accompanying evaluation metrics.

## 1.5 Research Question
*How do deterministic baselines, probabilistic/machine‑learning models, and sequential two‑stage hybrid architectures compare across robustness, resilience, and generalizability when applied to a rigorously filtered airport checkpoint dataset?*

## 1.6 Delimitations
1. **Geographic scope** – Top 25 U.S. commercial airports; experimental cohort limited to 9 airports (AA: DFW, PHL, ORD; DL: DTW, LGA, BOS; UA: EWR, IAH, LAX).
2. **Temporal scope** – Data from Jan 1 2019 to Dec 31 2025; model development restricted to post‑mask‑repeal period (May 1 2022 – Dec 2024).
3. **Data granularity** – Checkpoint throughput aggregated across all lanes within a terminal complex; carrier‑exclusive checkpoints only.
4. **Model family** – Deep neural networks excluded to preserve interpretability.

## 1.7 Limitations and Assumptions
* **Connecting‑passenger ratios** are derived from quarterly BTS DB‑1B surveys and assumed stationary within each quarter.
* **Zero‑throughput intervals** during overnight closures are treated as true operational zeros.
* **Advance vs. tactical cancellations** are handled asymmetrically: cancellations >24 h pre‑departure are removed from seat counts; cancellations <2 h are retained because passengers have already passed security.
* **Statistical power** – Sample‑size audit confirms >98 % of the 84 cross‑classification cells meet the N ≥ 50 threshold.

---

## 3.8 Four‑Tiered Purposive Filtering and Experimental Design
The filtering funnel consists of:
1. **Macro filter** – selects the Top 25 hubs (≈ 67 % of domestic departures) to ensure traffic intensity ρ ≈ 1 during peak hours.
2. **Meso filter** – requires concurrent service by legacy carriers (AA, DL, UA) and excludes Southwest due to its bimodal arrival distribution.
3. **Micro filter** – isolates carrier‑exclusive checkpoints, eliminating schedule collinearity (Corr ≥ 0.88).
4. **Balanced factorial cohort** – yields a 3 × 3 × 3 experimental grid (carrier × airport × regime) forming the 9‑airport cohort.

## 3.9 Data Sources and Warehouse Conformance
We ingest four federal data feeds (TSA FOIA, BTS OTP, Form 41, DB‑1B/DB‑1C) spanning 2019‑2025.  After ETL, the warehouse contains **42 M** clean factual records across 25 airports.  Key transformations include:
* **Connecting‑ratio deflation**: `Demand_originating = Seats × LoadFactor × (1 – ConnectingRatio)`.
* **Zero‑throughput preservation** for 00:00‑03:59 operational windows.
* **Cancellation handling** as described above.

## 3.10 Threats to Validity and Remediation Protocols
We address (i) **connector bias**, (ii) **checkpoint heterogeneity**, (iii) **overnight closure mis‑classification**, and (iv) **cancellation timing** through explicit data‑cleaning rules and sensitivity analyses (see Section 3.8).

## 3.11 Coupled Volatility & Diurnal Turbulence Indices
Two composite metrics capture operational turbulence:
* **Coupled Volatility Index (CVI)** = `CV_TSA × σ_Delay` where `CV_TSA` is the coefficient of variation of hourly checkpoint throughput and `σ_Delay` is the standard deviation of departure delays.
* **Operational Turbulence Shock Index (T(h))** – a 1‑D K‑Means clustering of hourly volatility scores that produces three non‑consecutive diurnal regimes (`OFF_PEAK`, `MID_PEAK`, `PEAK`).
These indices stratify the data for regime‑aware model training.

## 3.12 Hierarchical Cross‑Classification Architecture
We construct an 84‑cell tensor (`Seasonal Regime × Day‑of‑Week × Diurnal Regime`) providing homogeneous training subsets.  Sample‑size audits confirm a median of 215 observations per cell, satisfying statistical power requirements.

## 3.13 Model Benchmark Suite (M0‑M5)
* **M0 – Diurnal Seasonal Naïve** (`y_t = y_{t‑24}`)
* **M1 – SARIMAX with contemporaneous scheduled departures**
* **M2 – Linear Show‑Up Curve Regressor**
* **M3 – Gradient‑Boosted Count Regressor (LightGBM, Tweedie distribution)**
* **M4 – Full Tri‑Modal Pipeline (Load‑Factor scaled Show‑Up + OTP features)**
* **M5 – Sequential SARIMA‑Tree Hybrid** (first‑stage SARIMA captures linear seasonality; second‑stage LightGBM predicts residuals with Kalman‑style state feedback).

## 3.14 Evaluation Metrics
* **RMSE**, **MAE**, **MASE** (scaled against naïve benchmark)
* **Disruption Error Multiplier (R_MASE)** – ratio of MASE under shock periods to routine MASE
* **Relative Transfer Ratio (RTR)** – cross‑airport RMSE degradation
* **Diebold‑Mariano tests** for statistical significance.

*The subsequent chapter reports empirical performance of each model across the three dimensions.*
