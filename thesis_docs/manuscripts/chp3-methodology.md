# Chapter III

# Methodology

## Overview and Research Approach
This chapter details the methodological architecture and empirical framework developed to model, forecast, and optimize passenger security screening throughput volatility at commercial airports. Traditional airport passenger flow modeling has historically focused on predicting mean passenger volume through static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in halls, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queueing network subject to severe non-linear queuing friction and arrival burstiness (De Neufville & Odoni, 2014).

Under heavy-traffic queuing physics (Kingman, 1961; Whitt, 1993; Allen-Cunneen formula for $G/G/s$ queue facilities), expected queue wait time ($W_q$) and queue backlogs escalate not with average passenger arrivals ($\lambda$), but linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint utilization. As screening lanes approach saturation ($\rho \to 1.0$), arrival volatility ($C_a^2$) generates acute queue spikes, lane starvation, and severe passenger processing delays that propagate downline into delayed aircraft boarding and gate pushback holds ($r = +0.4375, p < 0.05$).

Consequently, this research targets the **volatility of TSA passenger screening throughput** as its primary dependent variable. The investigation evaluates:
1. **The Values versus Volatility Paradigm Comparison**: Whether forecasting TSA checkpoint volatility requires tracking the *values* (levels, volumes, and counts) of Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) flight features, the *volatility* (dispersion, standard deviations, and coefficients of variation) of those features, or a dual *hybrid/combined* representation.
2. **The Candidate Predictive Models and Baseline Control**: Comparative forecasting performance across three candidate predictive models representing distinct operational paradigms—the Deterministic Flight Schedule Model (Model 1), the Supervised Machine Learning Model (Model 2), and the Dynamic Two-Stage Hybrid Model (Model 3)—evaluated against an empirical daily persistence baseline control.
3. **Multi-Pillar Operational Dimensions**: Model performance evaluated across **Robustness** (routine operational accuracy), **Resilience** (stability under severe disruptions), and **Generalizability** (spatial cross-airport portability).

### Core Research Hypotheses
The investigation evaluates model performance across three independent operational dimensions:
* **Dimension 1: Robustness (Routine Operational Accuracy)**: Consistency and precision under nominal flow conditions ($\text{DepDelay} < 15\text{ min}$, zero flight cancellations).
* **Dimension 2: Resilience (Disruption Recovery)**: Stability, error bounded-ness, and speed of recovery during severe exogenous shocks (convective summer storm ground stops, winter freeze events, and gate holds).
* **Dimension 3: Generalizability (Spatial Cross-Airport Transferability)**: Portability of trained model structures across divergent airport geometries and carrier hub topologies under direct zero-shot deployment without local retraining.

**Core Research Hypothesis ($H_1$ - Master Asymmetric Trade-Off Hypothesis)**: Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no single architecture will prove universally superior across all three operational performance dimensions. Rather, each modeling paradigm possesses inherent operational properties that create stark, asymmetric trade-offs:
* **Dimension 1: Robustness (Routine Operations Target: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$)**:
  * *Hypothesis $H_{1\text{A}}$*: Under nominal operating conditions ($\text{DepDelay} < 15\text{ min}$, zero cancellations), the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) will successfully achieve the robustness target ($\text{MASE}_{\text{routine}} < 0.700$) by capturing non-linear passenger show-up and flight timing interactions, whereas the Naive Baseline Control and Deterministic Flight Schedule Model (Model 1) will fail the robustness threshold ($\text{MASE} \ge 0.94$). Machine learning (Model 2) will deliver a computationally lightweight, Pareto-efficient routine solution.
* **Dimension 2: Resilience (Severe Disruption Target: Recovery Multiplier $R_{\text{RMSE}} \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$, and $\text{TTR} < 4.0\text{ hours}$)**:
  * *Hypothesis $H_{1\text{B}}$*: Under severe operational disruptions ($\text{DepDelay} \ge 45\text{ min}$ or cancellations $\ge 5$), the Dynamic Two-Stage Hybrid Model (Model 3) will be the sole architecture to satisfy the resilience target ($R_{\text{RMSE}} \approx 1.00, R_{\text{MASE}} \approx 1.00, \text{TTR} < 4.0\text{ h}$) due to live 1-step error innovation feedback ($e_{t-1}$). Pure machine learning (Model 2) will suffer severe performance degradation ($R \ge 2.0$) due to the Empty Checkpoint Fallacy (failing to recognize stranded passenger crowds waiting in the concourse), while deterministic schedules (Model 1) will remain blind to downstream delay cascades.
* **Dimension 3: Generalizability (Zero-Shot Spatial Transfer Target: Relative Transfer Ratio $\text{RTR} \approx 1.00$ and Transfer MASE Change $\Delta \text{MASE}_{\text{transfer}} \le 10.0\%$)**:
  * *Hypothesis $H_{1\text{C}}$*: Under zero-shot cross-airport transfer without local retraining (e.g., deploying from Newark to LaGuardia), the Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($\text{RTR} \approx 1.00, \Delta \text{MASE} \le 10.0\%$) because published flight schedule convolution is strictly invariant to local terminal layout. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($\text{RTR} \gg 1.00, \Delta \text{MASE} > 10.0\%$) due to decision tree terminal geometry overfitting (memorization of specific carrier bank timings and gate configurations at the training airport).

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

## Predictive Modeling Frameworks for Throughput Volatility

To determine how to best forecast passenger arrival volatility at airport screening checkpoints, this study evaluates **three candidate models representing three distinct operational paradigms**, benchmarked against an empirical baseline control:

### The Baseline Control Benchmark (Daily Persistence)
* **Operational Logic**: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the exact same hour yesterday ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$).
* **Evaluation Role**: Serves as the non-parametric reference standard ($\text{MASE} \equiv 1.000$). Any operational model worth deploying must prove that it beats this simple historical benchmark.

### Model 1: Deterministic Flight Schedule Model (Physical Baseline)
* **Operational Logic**: Uses published airline flight schedules, shifted forward in time using empirical passenger show-up distributions from ACRP Report 40 (*Airport Passenger Terminal Planning and Design*). 
* **Mechanics**: Because passengers arrive 90 to 120 minutes before takeoff, scheduled flight departure banks are convolved across lead arrival horizons ($t+1, t+2, t+3$). This captures the physical ebb and flow of scheduled flight waves without requiring real-time delay telemetry or statistical machine learning.

### Model 2: Supervised Machine Learning Model (Flight Operations & Delays)
* **Operational Logic**: Uses an automated decision-tree algorithm trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features.
* **Mechanics**: The decision trees learn non-linear operational rules (e.g., how departure delays, tactical cancellations, and surface taxi queues ripple into checkpoint arrival dispersion). It tests whether airside operational data improves checkpoint forecasts over flight schedules alone.

### Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)
* **Operational Logic**: Combines the structured foundation of airline flight schedules with live real-time feedback from the checkpoint floor.
* **Mechanics**: 
  * *Stage 1*: Captures recurring daily and weekly flight schedule cycles.
  * *Stage 2*: A decision tree predicts residual volatility shocks caused by flight delays and weather ground stops, dynamically incorporating live 1-step error feedback from the previous hour ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). If lines are longer than the flight schedule predicted, the model immediately adjusts upward to track stranded passengers.

### Dataset Partitioning and Validation Protocol
Models were trained and validated across the 32-month Candidate B development partition:
* **Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days).
* **Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days), used for hyperparameter tuning.
* **Out-of-Time Holdout Window**: January 1, 2025 to December 31, 2025 (3,222 airport-days; 72,053 complex-level screening hours), strictly reserved for final out-of-time evaluation.
* **Operational Separation Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades do not leak across evaluation boundaries.

## Multi-Pillar Quantitative Evaluation Dimensions and Operational Regimes
To evaluate the research hypotheses rigorously against empirical holdout operations, model performance is benchmarked across three orthogonal evaluation dimensions, grounded in real-world airport operations:

### The Three-Tier Operational Taxonomy
Real-world airport operations do not operate in a simple binary state. Rather, airport checkpoint demands reflect three operational environments:
1. **Tier 1: Nominal On-Time Baseline**: Departure delays $< 15\text{ minutes}$ and zero tactical cancellations ($N_{\text{cancels}} = 0$). Grounded in the FAA/DOT A14 regulatory standard, this pristine state serves as an experimental control to observe pure passenger show-up curves without airside delay distortion.
2. **Tier 2: Routine Daily Operations**: Everyday commercial hub reality, characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.
3. **Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays $\ge 45\text{ minutes}$ or tactical cancellations $\ge 5$.

### Dimension 1: Robustness (Nominal & Routine Operations)
* **Operational Focus**: Verifying that a model delivers dependable, low-error volatility forecasts during standard daily flight banks.
* **Governing Metrics**: Root Mean Squared Error ($\text{RMSE}_{\text{routine}}$) and Mean Absolute Scaled Error ($\text{MASE}_{\text{routine}}$).
* **Explicit Model Target**: $\min \text{RMSE}_{\text{routine}}$ and $\mathbf{\text{MASE}_{\text{routine}} < 0.700}$ (achieving at least a 30% error reduction over daily persistence).

### Dimension 2: Resilience (Severe Disruption Recovery)
* **Operational Focus**: Verifying that a model resists demand collapse and recovers rapidly during severe storm ground stops and irregular operations (IROPS).
* **Governing Metrics**:
  * **Disruption Error Multipliers ($R_{\text{RMSE}}$ and $R_{\text{MASE}}$)**: Measuring whether error doubles under storms or remains stable ($R \approx 1.00$).
  * **Disruption Error ($\text{MASE}_{\text{shock}}$)**: Average relative error during active disruption hours.
  * **Time-to-Recovery ($\text{TTR}$)**: How many operational hours it takes for the model to re-converge to normal error bounds once flight operations resume.
* **Explicit Model Target**: $\mathbf{R_{\text{RMSE}} \approx 1.00 \quad (R_{\text{MASE}} \approx 1.00)}, \quad \min \text{MASE}_{\text{shock}}$, and $\mathbf{\text{TTR} < 4.0\text{ hours}}$.

### Dimension 3: Generalizability (Cross-Airport Transferability)
* **Operational Focus**: Verifying whether a model calibrated at one airport (e.g., Newark Liberty, EWR) can be deployed directly to a different airport with distinct gate layouts (e.g., New York LaGuardia, LGA) without site-specific retraining.
* **Governing Metrics**: Relative Transfer Ratio ($\text{RTR} = \text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}}$) and Percentage Change in Transfer MASE ($\Delta \text{MASE}_{\text{transfer}}$).
* **Explicit Model Target**: $\mathbf{\text{RTR} \approx 1.00 \quad (1.00 \pm 0.05)}$ and $\mathbf{\Delta \text{MASE}_{\text{transfer}} \le 10.0\%}$.
