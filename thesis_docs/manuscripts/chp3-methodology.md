# Chapter III

# Methodology

## Overview and Research Approach
This chapter details the methodological architecture and empirical framework developed to model, forecast, and optimize passenger security screening throughput volatility at commercial airports. Traditional airport passenger flow modeling has historically focused on predicting mean passenger volume through static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in halls, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queueing network subject to severe non-linear queuing friction and arrival burstiness (De Neufville & Odoni, 2014).

Under heavy-traffic queuing physics (Kingman, 1961; Whitt, 1993; Allen-Cunneen formula for $G/G/s$ queue facilities), expected queue wait time ($W_q$) and queue backlogs escalate not with average passenger arrivals ($\lambda$), but linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint utilization. As screening lanes approach saturation ($\rho \to 1.0$), arrival volatility ($C_a^2$) generates acute queue spikes, lane starvation, and severe passenger processing delays that propagate downline into delayed aircraft boarding and gate pushback holds ($r = +0.4375, p < 0.05$).

Consequently, this research targets the **volatility of TSA passenger screening throughput** as its primary dependent variable. The investigation evaluates:
1. **The Values versus Volatility Paradigm Comparison**: Whether forecasting TSA checkpoint volatility requires tracking the *values* (levels, volumes, and counts) of Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) flight features, the *volatility* (dispersion, standard deviations, and coefficients of variation) of those features, or a dual *hybrid/combined* representation.
2. **Predictive Modeling Architectures ($M_0$ through $M_5$)**: Comparative forecasting performance across deterministic baselines, supervised machine learning decision trees, and dynamic cyber-physical hybrid architectures.
3. **Multi-Pillar Operational Dimensions**: Model performance evaluated across **Robustness** (routine operational accuracy), **Resilience** (stability under severe disruptions), and **Generalizability** (spatial cross-airport portability).

### Core Research Hypotheses
The investigation evaluates model performance across three independent operational dimensions:
* **Dimension 1: Robustness (Routine Operational Accuracy)**: Consistency and precision under nominal flow conditions ($\text{DepDelay} < 15\text{ min}$, zero flight cancellations).
* **Dimension 2: Resilience (Disruption Recovery)**: Stability, error bounded-ness, and speed of recovery during severe exogenous shocks (convective summer storm ground stops, winter freeze events, and gate holds).
* **Dimension 3: Generalizability (Spatial Cross-Airport Transferability)**: Portability of trained model structures across divergent airport geometries and carrier hub topologies under direct zero-shot deployment without local retraining.

**Core Research Hypothesis ($H_1$)**: Across the three forecasting paradigms (deterministic, supervised ML, and two-stage hybrid), no individual architecture will prove uniformly superior across all three evaluation dimensions:
* Probabilistic and Machine Learning models will demonstrate superior accuracy during routine operations ($\text{MASE}_{\text{routine}} \le 0.890$) by learning complex non-linear calendar and show-up interactions.
* Two-Stage Hybrid frameworks will demonstrate superior resilience during systemic disruptions ($R_{\text{MASE}} \le 1.30$, time-to-recovery $\text{TTR} \le 3.5\text{ hours}$) due to closed-loop queue innovation corrections.
* Structurally parameterized baselines and standardized volatility archetypes will exhibit superior spatial generalizability ($\text{Transfer Degradation} \le 8\%$) by abstracting away airport-specific facility over-specialization.

**Feature Paradigm Hypothesis ($H_2$)**: Predicting multi-day temporal rolling volatility ($\sigma_{\text{TSA, 7d}}$) cannot be achieved using static flight volume levels (Feature Values), which collapse during structural shocks ($R^2 < 0$), but requires tracking operational dispersion (Feature Volatility metrics, achieving $R^2 > 0.30$).

### Methodological Execution Phases
The implementation follows four sequential, interconnected phases:
* **Phase 1: Multi-Source Conformed ETL Warehouse Development**: Automated extraction, spatial entity resolution, overnight closure preservation, and conformed relational synthesis across four federal aviation data feeds spanning 2019 to 2025.
* **Phase 2: Purposive Four-Tiered Filtering and Experimental Cohort Isolation**: Implementation of Macro congestion, Meso continuity/carrier homogeneity, Micro checkpoint exclusivity, and balanced factorial design to isolate unconfounded carrier-checkpoint pairs.
* **Phase 3: Coupled Volatility Formulation and Hierarchical Stratification**: Mathematical formulation of within-day TSA arrival variation, flight delay dispersion, the Coupled Volatility Index, and the Diurnal Operational Turbulence Shock Index, establishing the 84-cell cross-classification tensor.
* **Phase 4: Empirical Model Training, Tuning, and Out-of-Time Holdout Evaluation**: Walk-forward calibration across Candidate B partitions, model parameter calibration, and rigorous statistical benchmarking against the full 12-month 2025 holdout dataset ($N = 3,222$ airport-days; 72,053 complex-level observations).

## Four-Tiered Purposive Filtering and Experimental Design
To isolate the direct operational link connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel designed to eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding anomalies.

### Macro Filter: Scale and Congestion Regimes
Commercial aviation passenger volumes follow a heavy-tailed power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$). Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures. In airport queueing dynamics, an arrival rate $\lambda(t)$ passing through $c(t)$ screening lanes with service rate $\mu$ yields traffic intensity:
$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$
At small regional airfields, traffic intensity remains sparse ($\rho(t) \ll 0.3$), preventing queue formation and causing throughput to mirror arrivals without boundary resistance. In contrast, Top 25 hub facilities routinely approach or exceed capacity ($\rho(t) \to 1.0$) during morning and evening departure banks (05:00–08:30 and 16:00–18:30), creating the non-linear queue delays and buffer depletion necessary to train and validate congestion-aware models.

### Meso Filter: Airspace Shock Invariance and Southwest Exclusion
To ensure cross-carrier comparisons are evaluated under identical exogenous airspace conditions ($\delta_t$), candidate environments were required to operate concurrent domestic mainline services by American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA), neutralizing common weather and Air Traffic Control (ATC) delay confounders.

Concurrently, Southwest Airlines (WN) was systematically excluded from checkpoint pairing. Legacy carrier passengers display consistent, unimodal lognormal arrival timing:
$$\tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105\text{ minutes}$$
In contrast, Southwest's historical open-seating boarding structure, boarding group positioning (Groups A, B, C), and two-free-checked-bags policy generate a bimodal arrival mixture:
$$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$
where $\mu_1 \approx 135\text{ minutes}$ for boarding position maximizers and $\mu_2 \approx 65\text{ minutes}$ for carry-on-only business travelers. Pooling Southwest passenger streams with legacy carriers violates show-up distribution homogeneity.

### Micro Filter: Carrier Checkpoint Isolation
In shared terminal complexes (e.g., Salt Lake City International or Phoenix Sky Harbor), multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, flight departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), creating an indeterminate collinear system where individual airline demand contributions cannot be mathematically decoupled. Restricting analysis to carrier-exclusive screening environments enforces:
$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$
This eliminates inter-carrier schedule crosstalk ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint throughput.

### Balanced Factorial Cohort
Applying the four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort**:
* **American Airlines (AA)**: Dallas/Fort Worth (DFW), Philadelphia (PHL), Chicago O'Hare (ORD)
* **Delta Air Lines (DL)**: Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)
* **United Airlines (UA)**: Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles (LAX)

This cohort achieves complete factorial symmetry: exactly 3 legacy carriers $\times$ 3 dedicated terminal environments, spanning all four operational archetypes identified in national clustering.

## Data Sources and Warehouse Conformance
The analytical data foundation integrates four primary federal aviation data feeds over the continuous 7-year baseline from January 1, 2019 to December 31, 2025:

### TSA FOIA Security Screening Checkpoint Logs
Obtained via Freedom of Information Act (FOIA) disclosures, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### BTS On-Time Performance
Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

### BTS Form 41 Schedule T-100 Domestic Segment Data
Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

### BTS Origin and Destination Ticket Surveys
A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), utilized to extract quarterly connecting passenger ratios across airport pairs.

## Mathematical Formulation of Throughput Volatility Targets
To capture the full temporal spectrum of checkpoint queue turbulence, the methodology defines three distinct dependent volatility targets across two operational timescales:

### 1. Intraday Diurnal Absolute Dispersion ($\sigma_{\text{TSA, hr}}$)
Measures the absolute dispersion of hourly screening counts across the 24 hours of calendar day $d$ (in passengers per hour):
$$\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$$
This target reflects the absolute peak-to-trough amplitude of passenger arrival waves.

### 2. Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$)
Normalizes intraday dispersion by average daily throughput:
$$CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$$
By removing the baseline size of the airport, this scale-free metric measures arrival burstiness and queue surge spikiness independent of facility scale.

### 3. Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$)
Measures the 7-day rolling standard deviation of daily passenger volume (in passengers per day):
$$\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2}$$
This target captures medium-term multi-day passenger flow turbulence induced by convective storms, winter blizzards, and cascading cancellation shocks.

## The Values versus Volatility Feature Representation Space
To evaluate feature weights and determine whether forecasting volatility requires tracking operational levels versus operational dispersion, 24 attributes from BTS OTP, T-100, and DB1B were structured into two competing representational paradigms across five functional domains:

1. **Feature Values (Levels, 14 Attributes)**:
   * *Domain 1 (Schedule Scale)*: `sched_daily_total`, `actual_daily_total`, `sched_hourly_mean`, `sched_rolling_7d_mean`
   * *Domain 2 (Cancellations)*: `daily_cancellations`, `daily_cancel_rate`, `cancel_rolling_7d_mean`, `cancel_rate_rolling_7d_mean`
   * *Domain 3 (Flight Delays)*: `avg_dep_delay_minutes`, `flights_delayed_15min_pct`
   * *Domain 4 (Surface Queues)*: `avg_taxi_out_minutes`
   * *Domain 5 (Network Buffers)*: `aircraft_gauge_seats`, `route_load_factor_pct`, `connecting_passenger_share_pct`
2. **Feature Volatilities (Dispersion, 10 Attributes)**:
   * *Domain 1 (Schedule Dispersion)*: `sched_hourly_std`, `sched_hourly_cv`, `actual_hourly_std`, `actual_hourly_cv`, `sched_rolling_7d_std`, `sched_rolling_7d_cv`
   * *Domain 2 (Cancellation Dispersion)*: `cancel_rolling_7d_std`, `cancel_rate_rolling_7d_std`, `otp_cancellation_volatility_cv`
   * *Domain 3 (Delay Dispersion)*: `otp_departure_delay_volatility_cv`
3. **Combined Dual Paradigm (24 Attributes)**: Interacts both feature sets to test orthogonal predictive complementarity.

## Coupled Volatility and Variance Formulations
Systemic queue breakdown and checkpoint congestion are driven by **coupled volatility mismatch** between landside passenger arrivals and airside flight departures. The methodology defines:

### Flight Departure Delay Dispersion
The sample standard deviation of departure delays across all uncancelled domestic flights departing the candidate network on day $d$:
$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

### The Coupled Volatility Index
The joint product of landside arrival variation and airside delay dispersion:
$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$
The Coupled Volatility Index serves as an econometric measure of systemic operational vulnerability.

### Diurnal Operational Turbulence Shock Index
To identify diurnal regimes conditioned on Day of Week ($DOW \in [1, 7]$) without arbitrary step boundaries, the Operational Turbulence Shock Index $T_{dow}(h)$ is defined for each hour $h \in [0, 23]$:
$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$
Applying 1D K-Means clustering ($k = 3$) on $T_{dow}(h)$ establishes three diurnal regimes:
* **1_OFF_PEAK**: Low Volatility / Overnight Curfew Quiescence ($T < 0.35$).
* **2_MID_PEAK**: Moderate Volatility / Midday Steady Flow ($0.35 \le T < 0.75$).
* **3_PEAK**: High Volatility / Queuing Turbulence ($T \ge 0.75$).

## Model Benchmark Suite for Throughput Volatility
To evaluate the research hypotheses, four primary model architectures were trained and calibrated to forecast throughput volatility:

* **Model $M_0$ (Diurnal Volatility Naive Benchmark)**: A baseline persistence forecast assuming volatility today repeats volatility observed yesterday ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$).
* **Model $M_1$ (Deterministic Schedule Bank Volatility Baseline)**: Derives predicted passenger screening volatility directly from convolved scheduled flight departure bank dispersion ($\sigma_{\text{sched}}$ or $CV_{\text{sched}}$):
  $$\widehat{\text{Vol}}_{M1, t} = \beta_0 + \beta_1 \cdot \text{Vol}_{\text{sched}, t}$$
* **Model $M_3$ (Supervised Volatility Gradient Boosted Trees)**: Histogram Gradient Boosted Decision Tree regressor trained across the 24 OTP feature attributes, capturing non-linear interactions across schedule bank dispersion, tactical cancellations, and delay turbulence.
* **Model $M_5$ (Sequential SARIMA-Tree Volatility Hybrid with Error Feedback)**:
  * *Stage 1 (Linear Seasonal Volatility Baseline)*: Captures recurring daily and weekly baseline volatility cycles ($\widehat{\text{Vol}}_{1, t}$).
  * *Residual Extraction*: $e_t = \text{Vol}_t - \widehat{\text{Vol}}_{1, t}$.
  * *Stage 2 (Non-Linear Tree Residual Correction)*: Decision tree predicts residual volatility shock $\hat{e}_t$ using airside delay dispersion, cancellations, and taxi queues, augmented with live 1-step residual error feedback ($e_{t-1}$).
  * *Final Hybrid Forecast*: $\widehat{\text{Vol}}_{M5, t} = \widehat{\text{Vol}}_{1, t} + \hat{e}_t$.

### Dataset Partitioning and Validation Protocol
Models were trained and validated across the 32-month Candidate B development partition:
* **Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days).
* **Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days), used for hyperparameter tuning.
* **Out-of-Time Holdout Window**: January 1, 2025 to December 31, 2025 (3,222 airport-days; 72,053 complex-level screening hours), strictly reserved for final out-of-time evaluation.
* **Operational Separation Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades do not leak across evaluation boundaries.

## Multi-Pillar Quantitative Evaluation Metrics
Model performance is benchmarked using five standard operational metrics:
* **Root Mean Squared Error (RMSE)**: Measures overall forecast error in throughput volatility ($\sqrt{\frac{1}{N}\sum (\text{Vol}_t - \widehat{\text{Vol}}_t)^2}$).
* **Mean Absolute Error (MAE)**: Measures average absolute volatility forecast error ($\frac{1}{N}\sum |\text{Vol}_t - \widehat{\text{Vol}}_t|$).
* **Mean Absolute Scaled Error (MASE)**: Normalizes error against the naive persistence baseline ($M_0$):
  $$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N |\text{Vol}_t - \widehat{\text{Vol}}_t|}{\frac{1}{N-1}\sum_{t=2}^N |\text{Vol}_t - \text{Vol}_{t-1}|}$$
  A score below 1.0 indicates superior forecasting skill over naive persistence.
* **Disruption Error Multiplier ($R_{\text{MASE}}$)**: Evaluates forecasting stability during severe weather disruptions, defined as the ratio of error during severe disruption hours ($\text{Delay} \ge 45\text{m}$ or $\text{Cancels} \ge 5$) to error during routine hours:
  $$R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
  A value $\le 1.30$ denotes a resilient model whose accuracy remains stable, whereas a value $\ge 2.0$ indicates a fragile model whose error doubles during storms.
* **Relative Transfer Ratio (RTR)**: Measures spatial portability when deploying a model trained on one airport directly to a different airport without retraining:
  $$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
  Values near 1.0 indicate seamless transfer with minimal accuracy loss.
