# Chapter III

# Methodology

## Overview and Research Approach
This chapter details the methodological architecture and empirical framework developed to model, forecast, and optimize passenger security screening throughput volatility at commercial airports. Traditional airport passenger flow modeling has historically focused on predicting mean passenger volume through static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in halls, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queueing network subject to severe non-linear queuing friction and arrival burstiness (De Neufville & Odoni, 2014).

Under heavy-traffic queuing physics (Kingman, 1961; Whitt, 1993; Allen-Cunneen formula for $G/G/s$ queue facilities), expected queue wait time ($W_q$) and queue backlogs escalate not with average passenger arrivals ($\lambda$), but linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint utilization. As screening lanes approach saturation ($\rho \to 1.0$), arrival volatility ($C_a^2$) generates acute queue spikes, lane starvation, and severe passenger processing delays that propagate downline into delayed aircraft boarding and gate pushback holds ($r = +0.4375, p < 0.05$).

Consequently, this research targets the **volatility of TSA passenger screening throughput** as its primary dependent variable. The investigation evaluates:
1. **The Values versus Volatility Paradigm Comparison**: Whether forecasting TSA checkpoint volatility requires tracking the *values* (levels, volumes, and counts) of Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) flight features, the *volatility* (dispersion, standard deviations, and coefficients of variation) of those features, or a dual *hybrid/combined* representation.
2. **The 4-Model Canonical Evaluation Suite ($M_0, M_1^*, M_3, M_5$)**: Comparative forecasting performance across four canonical model architectures representing distinct paradigms—baseline control ($M_0$), deterministic schedule convolution physics ($M_1^*$), supervised machine learning tree ensembles ($M_3$), and sequential cyber-physical hybrids ($M_5$)—with intermediate exploratory variants ($M_1, M_2, M_4$) systematically pruned following Phase 2 Four-Tier Filtering.
3. **Multi-Pillar Operational Dimensions**: Model performance evaluated across **Robustness** (routine operational accuracy), **Resilience** (stability under severe disruptions), and **Generalizability** (spatial cross-airport portability).

### Core Research Hypotheses
The investigation evaluates model performance across three independent operational dimensions:
* **Dimension 1: Robustness (Routine Operational Accuracy)**: Consistency and precision under nominal flow conditions ($\text{DepDelay} < 15\text{ min}$, zero flight cancellations).
* **Dimension 2: Resilience (Disruption Recovery)**: Stability, error bounded-ness, and speed of recovery during severe exogenous shocks (convective summer storm ground stops, winter freeze events, and gate holds).
* **Dimension 3: Generalizability (Spatial Cross-Airport Transferability)**: Portability of trained model structures across divergent airport geometries and carrier hub topologies under direct zero-shot deployment without local retraining.

**Core Research Hypothesis ($H_1$ - Master Asymmetric Trade-Off Hypothesis)**: Across the four canonical model paradigms evaluated following four-tiered purposive filtering (baseline control, deterministic schedule physics, supervised machine learning, and dynamic cyber-physical hybrid), no single architecture will prove universally superior across all three operational performance dimensions. Rather, each modeling paradigm possesses inherent mathematical properties that create stark, asymmetric trade-offs:
* **Dimension 1: Robustness (Routine Operations Target: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$)**:
  * *Hypothesis $H_{1\text{A}}$*: Under nominal operating conditions ($\text{DepDelay} < 15\text{ min}$, zero cancellations), Supervised Machine Learning ($M_3$) and the Cyber-Physical Hybrid ($M_5$) will successfully achieve the robustness target ($\text{MASE}_{\text{routine}} < 0.700$) by capturing non-linear arrival-to-flight temporal interactions, whereas the Naive Baseline Control ($M_0$) and Deterministic Baseline ($M_1^*$) will fail the robustness threshold ($\text{MASE} \ge 0.94$). Machine learning ($M_3$) will deliver a computationally lightweight, Pareto-efficient routine solution.
* **Dimension 2: Resilience (Severe Disruption Target: Recovery Multiplier $R_{\text{RMSE}} \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$, and $\text{TTR} < 4.0\text{ hours}$)**:
  * *Hypothesis $H_{1\text{B}}$*: Under severe exogenous disruptions ($\text{DepDelay} \ge 45\text{ min}$ or cancellations $\ge 5$), the Dynamic Cyber-Physical Hybrid ($M_5$) will be the sole architecture to satisfy the resilience target ($R_{\text{RMSE}} \approx 1.00, R_{\text{MASE}} \approx 1.00, \text{TTR} < 4.0\text{ h}$) due to recursive 1-step closed-loop error innovation feedback ($e_{t-1}$). Static supervised ML ($M_3$) will suffer catastrophic performance degradation ($R \ge 2.0$) due to the Empty Checkpoint Fallacy (failing to recognize un-screened passenger backlogs holding in concourses), while deterministic baselines will remain blind to downstream delay cascades.
* **Dimension 3: Generalizability (Zero-Shot Spatial Transfer Target: Relative Transfer Ratio $\text{RTR} \approx 1.00$ and Transfer MASE Change $\Delta \text{MASE}_{\text{transfer}} \le 10.0\%$)**:
  * *Hypothesis $H_{1\text{C}}$*: Under zero-shot cross-airport transfer without local retraining (e.g., EWR $\to$ LGA), the Deterministic Convolved Schedule Physics Baseline ($M_1^*$) will decisively satisfy the generalizability target ($\text{RTR} \approx 1.00, \Delta \text{MASE} \le 10.0\%$) because flight schedule convolution physics is strictly invariant to local facility geometry. Conversely, the Cyber-Physical Hybrid ($M_5$) will decisively fail the generalizability target ($\text{RTR} \gg 1.00, \Delta \text{MASE} > 10.0\%$) due to decision tree terminal geometry overfitting (structural memorization of carrier bank timings and terminal gate configurations specific to the source training airport).

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

## The 4-Model Canonical Evaluation Suite for Throughput Volatility
Following the Phase 2 Four-Tiered Purposive Filtering pipeline (Macro congestion, Meso airspace shock invariance, Micro checkpoint exclusivity, and balanced factorial design), the initial candidate model space was consolidated into **exactly four canonical models**—representing exactly one candidate architecture per modeling paradigm, plus the baseline control:

1. **Baseline Control — Model $M_0$ (Diurnal Volatility Naive Persistence)**:
   A strict persistence benchmark assuming intraday volatility today exactly mirrors the volatility observed at the same hour yesterday:
   $$\widehat{\text{Vol}}_{M0, t} = \text{Vol}_{t-24}$$
   This serves as the scale-free denominator for Mean Absolute Scaled Error ($\text{MASE}$).
2. **Deterministic Baseline — Model $M_1^*$ (Deterministic Schedule Bank Volatility Baseline)**:
   Derives predicted passenger screening volatility directly from scheduled flight departure bank dispersion convolved with the empirical passenger show-up distribution $\tau \sim \text{Lognormal}(\mu, \sigma^2)$:
   $$\widehat{\text{Vol}}_{M1^*, t} = \beta_0 + \beta_1 \cdot \text{Vol}_{\text{sched\_conv}, t}$$
   Unlike unshifted schedule profiles, $M_1^*$ embodies physical schedule bank convolution physics, establishing the pure deterministic benchmark.
3. **Probabilistic / Supervised Machine Learning — Model $M_3$ (Supervised Volatility Gradient Boosted Trees)**:
   A non-linear Histogram Gradient Boosted Decision Tree regressor trained across the convolved passenger arrival curve and all 24 conformed BTS On-Time Performance (OTP) feature attributes (14 feature values and 10 feature volatilities):
   $$\widehat{\text{Vol}}_{M3, t} = f_{\text{GBR}}(\mathbf{x}_t^{\text{convolved}}, \mathbf{x}_t^{\text{OTP\_Values}}, \mathbf{x}_t^{\text{OTP\_Volatilities}})$$
   Captures complex multi-attribute non-linear interactions across flight bank dispersion, tactical cancellations, surface taxi delays, and network load factors.
4. **Dynamic Cyber-Physical Hybrid — Model $M_5$ (Sequential SARIMA-Tree Volatility Hybrid with Error Innovation Feedback)**:
   A dynamic, two-stage closed-loop architecture designed to bridge physical queuing dynamics and real-time operational state innovations:
   * *Stage 1 (Linear Seasonal Volatility Baseline)*: A seasonal autoregressive integrated moving average $\text{SARIMA}(p,d,q)(P,D,Q)_{24}$ process capturing recurring diurnal and weekly baseline volatility cycles:
     $$\widehat{\text{Vol}}_{1, t} = \text{SARIMA}(\text{Vol}_{t-1}, \dots, \text{Vol}_{t-k})$$
   * *Residual Innovation Extraction*: Computes the unmodeled operational shock:
     $$e_t = \text{Vol}_t - \widehat{\text{Vol}}_{1, t}$$
   * *Stage 2 (Non-Linear Tree Residual Shock Estimation)*: A Gradient Boosted Decision Tree estimates residual shock volatility $\hat{e}_t$ using airside flight delays, cancellation rates, surface taxi queues, and convolved arrivals, dynamically augmented with **live 1-step recursive residual error feedback ($e_{t-1}$)**:
     $$\hat{e}_t = g_{\text{Tree}}(\mathbf{x}_t^{\text{airside}}, e_{t-1})$$
   * *Final Cyber-Physical Forecast Synthesis*:
     $$\widehat{\text{Vol}}_{M5, t} = \widehat{\text{Vol}}_{1, t} + \hat{e}_t$$

### Pruning of Intermediate Exploratory Variations
Prior to formal out-of-time evaluation, three intermediate exploratory model variations were systematically evaluated and pruned from the canonical test suite to eliminate mathematical redundancy and maintain a disciplined 4-model factorial comparison:
* **Model $M_1$ (Unshifted Flight Schedule Dispersion)**: Pruned because directly predicting checkpoint volatility from unshifted departure banks without passenger show-up convolution ignored the 105-minute mean lead-time lag, creating severe systematic phase distortion ($r = 0.12$). Superseded by the convolved formulation $M_1^*$.
* **Model $M_2$ (Lead Flights Only Baseline)**: Pruned because restricting flight departures to early bank lead flights introduced severe truncation bias during afternoon and evening secondary delay cascades.
* **Model $M_4$ (Load-Factor Scaled Linear Regression)**: Pruned because linear scaling by Form 41 monthly load factors proved mathematically redundant with the fully non-linear capacity interactions learned by $M_3$ and $M_5$.

### Dataset Partitioning and Validation Protocol
Models were trained and validated across the 32-month Candidate B development partition:
* **Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days).
* **Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days), used for hyperparameter tuning.
* **Out-of-Time Holdout Window**: January 1, 2025 to December 31, 2025 (3,222 airport-days; 72,053 complex-level screening hours), strictly reserved for final out-of-time evaluation.
* **Operational Separation Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades do not leak across evaluation boundaries.

## Multi-Pillar Quantitative Evaluation Dimensions and Explicit Operational Targets
To evaluate the research hypotheses rigorously against empirical holdout operations, model performance is benchmarked across three orthogonal evaluation dimensions, each governed by explicit quantitative operational targets:

### Dimension 1: Robustness (Routine Operations)
* **Operational Regime**: Nominal flight operations characterized by average departure delays $\text{DepDelay} < 15\text{ minutes}$ and zero tactical flight cancellations ($N_{\text{cancels}} = 0$).
* **Governing Metrics**:
  * **Root Mean Squared Error ($\text{RMSE}_{\text{routine}}$)**: Measures precision of volatility forecasts under unperturbed diurnal rhythms ($\text{pax/hr}$).
  * **Mean Absolute Scaled Error ($\text{MASE}_{\text{routine}}$)**: Evaluates forecast accuracy scaled relative to naive persistence ($M_0$):
    $$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N |\text{Vol}_t - \widehat{\text{Vol}}_t|}{\frac{1}{N-1}\sum_{t=2}^N |\text{Vol}_t - \text{Vol}_{t-1}|}$$
* **Explicit Model Targets**:
  $$\text{Target}_{\text{Robustness}}: \quad \min \text{RMSE}_{\text{routine}} \quad \text{and} \quad \mathbf{\text{MASE}_{\text{routine}} < 0.700}$$
  A model must achieve an error reduction exceeding 30% relative to naive persistence ($\text{MASE} < 0.700$) while minimizing absolute dispersion error ($\text{RMSE}$).

### Dimension 2: Resilience (Severe Disruption Recovery)
* **Operational Regime**: Severe systemic disruptions induced by convective weather, summer thunderstorm ground stops, or winter freeze events, defined as complex hours where average departure delays $\text{DepDelay} \ge 45\text{ minutes}$ or flight cancellations $N_{\text{cancels}} \ge 5$.
* **Governing Metrics**:
  * **Recovery Error Multipliers ($R_{\text{RMSE}}$ and $R_{\text{MASE}}$)**: Quantify degradation severity under shock conditions relative to routine baselines:
    $$R_{\text{RMSE}} = \frac{\text{RMSE}_{\text{shock}}}{\text{RMSE}_{\text{routine}}}, \qquad R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
  * **Disruption Error ($\text{MASE}_{\text{shock}}$)**: Mean absolute scaled error sustained during active disruption hours.
  * **Time-to-Recovery ($\text{TTR}$)**: The elapsed operational duration (in hours) following shock cessation required for forecast error to re-converge to within $\pm 10\%$ of routine pre-shock baselines.
* **Explicit Model Targets**:
  $$\text{Target}_{\text{Resilience}}: \quad \mathbf{R_{\text{RMSE}} \approx 1.00 \quad (R_{\text{MASE}} \approx 1.00)}, \quad \min \text{MASE}_{\text{shock}}, \quad \text{and} \quad \mathbf{\text{TTR} < 4.0\text{ hours}}$$
  A resilient model maintains error bounded-ness ($R \approx 1.00$), prevents error doubling ($R \ge 2.0$), and re-converges to steady state within four operational hours ($\text{TTR} < 4.0\text{ h}$).

### Dimension 3: Generalizability (Spatial Cross-Airport Transferability)
* **Operational Regime**: Zero-shot spatial deployment of a calibrated model from its source training airport (e.g., Newark Liberty, EWR) directly to a target validation airport with distinct terminal layout and bank structure (e.g., New York LaGuardia, LGA), without local retraining or parameter fine-tuning.
* **Governing Metrics**:
  * **Relative Transfer Ratio ($\text{RTR}$)**: Measures spatial error inflation under out-of-distribution transfer:
    $$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
  * **Percentage Change in Transfer MASE ($\Delta \text{MASE}_{\text{transfer}}$)**: Quantifies the relative accuracy degradation upon spatial migration:
    $$\Delta \text{MASE}_{\text{transfer}} = \left( \frac{\text{MASE}_{\text{transfer}} - \text{MASE}_{\text{in-sample}}}{\text{MASE}_{\text{in-sample}}} \right) \times 100\%$$
* **Explicit Model Targets**:
  $$\text{Target}_{\text{Generalizability}}: \quad \mathbf{\text{RTR} \approx 1.00 \quad (1.00 \pm 0.05)} \quad \text{and} \quad \mathbf{\Delta \text{MASE}_{\text{transfer}} \le 10.0\%}$$
  A generalizable architecture preserves predictive fidelity across diverse airport complexes without exhibiting terminal geometry overfitting ($\Delta \text{MASE} \le 10.0\%$).
