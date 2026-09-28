# CHAPTER III: METHODOLOGY

---

## 3.1 Overview and Research Approach

This chapter details the methodological architecture and empirical framework developed to model, forecast, and optimize passenger security screening throughput at commercial airports. Traditional airport passenger flow modeling has historically relied upon static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queueing network subject to severe non-linear queuing friction and schedule-driven volatility (De Neufville & Odoni, 2014). 

The primary objective of this research is to evaluate the comparative predictive accuracy and operational utility of three distinct forecasting paradigms:
1. **Deterministic Baselines ($M_0, M_1$)**: Classical reference benchmarks relying on diurnal seasonal persistence ($y_{t-24}$) and contemporaneous scheduled flight departures.
2. **Probabilistic and Machine Learning Architectures ($M_2, M_3, M_4$)**: Data-driven, non-linear formulations—including empirical passenger show-up arrival distributions, Gradient Boosted Tweedie Regressors (LightGBM), and multi-source operational feature pipelines incorporating flight delays and cancellations.
3. **Sequential Two-Stage Hybrid Frameworks ($M_5$)**: Integrated architectures combining queueing dynamics and time-series error correction with non-linear machine learning to dynamically correct for latent queue states during severe operational disruptions.

### 3.1.1 Core Research Hypotheses
The investigation evaluates model performance across three orthogonal operational dimensions:
* **Dimension 1: Robustness (Routine Operational Accuracy)**: Consistency and precision under nominal flow conditions ($\text{DepDelay} < 15\text{ min}$).
* **Dimension 2: Resilience (Disruption Recovery)**: Stability, error bounded-ness, and speed of recovery during severe exogenous shocks (convective summer storm ground stops, winter freeze events, and gate holds).
* **Dimension 3: Generalizability (Spatial Cross-Airport Transferability)**: Portability of trained model structures across divergent airport geometries and carrier hub topologies under zero-shot transfer.

**Core Research Hypothesis ($H_1$)**: Across the three forecasting paradigms (deterministic, probabilistic/ML, and two-stage hybrid), no individual architecture will prove uniformly superior across all three evaluation dimensions. Rather:
* Probabilistic and Machine Learning models will demonstrate superior accuracy during routine operations ($\text{MASE}_{\text{routine}} < 0.70$) by learning complex non-linear calendar and show-up interactions.
* Two-Stage Hybrid frameworks will demonstrate superior resilience during systemic disruptions ($R_{\text{MASE}} \le 1.30$, time-to-recovery $\text{TTR} \le 4.0\text{ hours}$) due to closed-loop queue innovation corrections.
* Structurally parameterized baselines and standardized volatility archetypes will exhibit superior spatial generalizability ($\text{Transfer Degradation} \le 15\%$) by abstracting away airport-specific gate and concourse over-fitting.

### 3.1.2 Methodological Execution Phases
The implementation follows four sequential, interconnected phases:
* **Phase 1: Multi-Source Conformed ETL Warehouse Development**: Automated extraction, spatial entity resolution, structural zero preservation, and conformed relational synthesis across four federal aviation data feeds spanning 2019 to 2025.
* **Phase 2: Purposive Four-Tiered Filtering & Experimental Cohort Isolation**: Implementation of Macro congestion, Meso continuity/carrier homogeneity, Micro checkpoint exclusivity, and orthogonal factorial balance to isolate unconfounded carrier-checkpoint pairs.
* **Phase 3: Coupled Volatility Clustering & Hierarchical Stratification**: Mathematical formulation of within-day TSA arrival variation, flight delay dispersion, the Coupled Volatility Index, and the Diurnal Operational Turbulence Shock Index, establishing the 84-cell cross-classification tensor.
* **Phase 4: Empirical Model Training, Tuning, and Out-of-Time Holdout Evaluation**: Walk-forward calibration across Candidate B partitions, hyperparameter optimization, and rigorous statistical benchmarking against the full 12-month 2025 holdout dataset.

---

## 3.2 Four-Tiered Purposive Filtering and Experimental Design

To isolate the physical relationship connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel designed to eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding anomalies.

### 3.2.1 Macro Filter: Scale and Congestion Regimes
Commercial aviation passenger volumes follow a heavy-tailed power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$). Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures. In airport queueing dynamics, an arrival rate $\lambda(t)$ passing through $c(t)$ screening lanes with service rate $\mu$ yields traffic intensity:
$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$
At small regional airfields, traffic intensity remains sparse ($\rho(t) \ll 0.3$), preventing queue formation and causing throughput to mirror arrivals without boundary resistance. In contrast, Top 25 hub facilities routinely approach or exceed capacity ($\rho(t) \to 1.0$) during morning and evening departure banks (05:00–08:30 and 16:00–18:30), creating the non-linear queue delays and buffer depletion necessary to train and validate congestion-aware models.

### 3.2.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion
To ensure cross-carrier comparisons are evaluated under identical exogenous airspace conditions ($\delta_t$), candidate environments were required to operate concurrent domestic mainline services by American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA), neutralizing common weather and Air Traffic Control (ATC) delay confounders.

Concurrently, Southwest Airlines (WN) was systematically excluded from checkpoint pairing. Legacy carrier passengers display consistent, unimodal lognormal arrival timing:
$$\tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105\text{ minutes}$$
In contrast, Southwest's historical open-seating boarding structure, boarding group positioning (Groups A, B, C), and two-free-checked-bags policy generate a bimodal arrival mixture:
$$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$
where $\mu_1 \approx 135\text{ minutes}$ for boarding position maximizers and $\mu_2 \approx 65\text{ minutes}$ for carry-on-only business travelers. Pooling Southwest passenger streams with legacy carriers violates show-up distribution homogeneity.

### 3.2.3 Micro Filter: Carrier Checkpoint Isolation
In shared terminal complexes (e.g., Salt Lake City International or Phoenix Sky Harbor), multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, flight departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), creating an indeterminate collinear system where individual airline demand contributions cannot be mathematically decoupled. Restricting analysis to carrier-exclusive screening environments enforces:
$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$
This eliminates inter-carrier schedule crosstalk ($\kappa < 25$), directly mapping carrier flight banks to physical checkpoint throughput.

### 3.2.4 Orthogonal Factorial Cohort (The 9-Airport Experimental Cohort)
Applying the four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort**:
* **American Airlines (AA)**: Dallas/Fort Worth (DFW), Philadelphia (PHL), Chicago O'Hare (ORD)
* **Delta Air Lines (DL)**: Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)
* **United Airlines (UA)**: Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles (LAX)

This cohort achieves complete factorial symmetry: exactly 3 legacy carriers $\times$ 3 dedicated terminal environments, spanning all four operational archetypes identified in national clustering.

---

## 3.3 Data Sources and Warehouse Conformance

The analytical data foundation integrates four primary federal aviation data feeds over the continuous 7-year baseline from January 1, 2019 to December 31, 2025:

### 3.3.1 TSA FOIA Security Screening Checkpoint Logs
Obtained via Freedom of Information Act (FOIA) disclosures, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### 3.3.2 BTS On-Time Performance (Form 234)
Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

### 3.3.3 BTS Form 41 Schedule T-100 Domestic Segment Data
Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

### 3.3.4 BTS DB1B / DB1C Origin & Destination Ticket Surveys
A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), utilized to extract quarterly connecting passenger ratios across airport pairs.

---

## 3.4 Threats to Validity and Remediation Protocols

### 3.4.1 Connecting Passenger Bias (The Hub Disconnect)
In hub-and-spoke operations, up to 76% of passengers deplane from inbound flights and transfer to outbound gates entirely airside, never passing through landside security checkpoints. Treating scheduled flight departures or departing seats as raw security demand grossly inflates demand estimates. To eliminate this bias, flight seat capacity is deflated using empirical connecting fractions derived from BTS DB1B surveys:
$$\text{Demand}_{\text{originating}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$

### 3.4.2 Checkpoint Heterogeneity and Administrative Staffing Shifts
Evaluating individual screening lanes introduces administrative variance resulting from Transportation Security Officer (TSO) shift rotations and dynamic lane reassignments between TSA PreCheck and standard screening. To achieve physical stability, hourly throughput is aggregated across all lanes within a dedicated terminal complex:
$$Y_{kt} = \sum_{l \in \mathcal{L}_k} y_{k,l,t}$$
Summing across lane complexes transforms noisy lane-level counts into a robust aggregate demand signal that maps to outbound flight banks.

### 3.4.3 Structural Zeros vs. Missing Data
Across the warehouse, 450,973 records report zero throughput. Cross-referencing against flight schedules revealed that 98.6% of zero intervals occur during overnight checkpoint closures (00:00–03:59). Rather than applying naive moving-average imputation—which would introduce artificial passenger traffic during physical closures—these intervals are preserved as true structural zeros and modeled using Tweedie deviance ($p = 1.3$) or zero-inflated hurdle structures.

### 3.4.4 Tactical vs. Advance Cancellations
A critical source of lookahead leakage in predictive models is the handling of cancelled flights. Flight cancellations are treated asymmetrically based on information causality:
* **Advance Cancellations (>24 hours pre-departure)**: Purged from departing seat capacity.
* **Tactical Cancellations (<2 hours pre-departure)**: Retained in the passenger arrival curve, because affected passengers have already arrived at the terminal and crossed security checkpoints prior to the carrier issuing the cancellation notice.

---

## 3.5 Coupled Volatility and Variance Formulations

Traditional terminal planning models categorize time using static calendar bins. However, empirical regression between static scheduled flight movements and airport queue delays yields negligible explanatory power ($R^2 \approx 2.50\%$). Systemic queue breakdown and checkpoint congestion are driven not by baseline volumes, but by **coupled volatility and variance mismatch** between landside passenger arrivals and airside flight departures.

To formally parameterize operational turbulence, the following daily metrics are calculated for each calendar day $d$ in the analytical window (Candidate B: May 1, 2022 to December 31, 2025):

### 3.5.1 Within-Day TSA Screening Volatility ($CV_{\text{TSA}, d}$)
The coefficient of variation of hourly passenger screening volume measures the intraday concentration and peakiness of passenger arrival waves:
$$CV_{\text{TSA}, d} = \frac{\sigma_{\text{hourly},\text{TSA}, d}}{\mu_{\text{hourly},\text{TSA}, d}} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (\text{TSA}_{d,h} - \bar{\text{TSA}}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} \text{TSA}_{d,h}}$$

### 3.5.2 Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)
Captures the maximum single-hour screening demand impulse relative to average daily load:
$$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$

### 3.5.3 Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)
The sample standard deviation of departure delays across all uncancelled domestic flights departing the candidate network on day $d$:
$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$
This metric measures the dispersion of airside schedule unreliability and tarmac delay propagation across the National Airspace System (NAS).

### 3.5.4 The Coupled Volatility Index ($\text{CVI}_d$)
The joint product of landside arrival variation and airside delay dispersion:
$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$
The Coupled Volatility Index serves as an econometric measure of systemic operational vulnerability, directly reflecting the co-occurrence of landside screening surges and airside flight delay dispersion.

---

## 3.6 Diurnal Operational Turbulence Shock Index ($T(h)$)

Standard aviation operational schedules typically enforce rigid, arbitrary hourly blocks (e.g., morning 06:00–12:00, afternoon 12:00–18:00). To identify diurnal regimes conditioned on each Day of Week ($DOW \in [1, 7]$) without imposing artificial consecutive boundaries, we define the **Operational Turbulence Shock Index** $T_{dow}(h)$ for each hour $h \in [0, 23]$:

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$

Where:
* $\sigma_{\text{TSA}, dow}(h)$ is the across-week standard deviation of passenger screening throughput at hour $h$.
* $\sigma_{\text{intra}, dow}(h)$ is the mean within-hour flight departure delay standard deviation.
* $\sigma_{\text{inter}, dow}(h)$ is the across-week standard deviation of mean hourly departure delay.
* $\mathbb{I}(\bar{F}_{dow}(h) \ge 20)$ is an operational activity indicator that filters overnight curfew hours where commercial departures are sparse ($<20$ flights network-wide).

Applying 1D K-Means clustering ($k = 3$) on $T_{dow}(h)$ ordered monotonically by turbulence score partitions diurnal operations into three regimes:
* **`1_OFF_PEAK`**: Low Volatility / Overnight Curfew Quiescence ($T < 0.35$).
* **`2_MID_PEAK`**: Moderate Volatility / Midday Steady Flow and Ramp ($0.35 \le T < 0.75$).
* **`3_PEAK`**: High Volatility / Queuing Turbulence ($T \ge 0.75$).

Because $T(h)$ evaluates the upper bound of passenger arrival variance and airside delay dispersion, it empirically uncovers **non-consecutive dual peaks**:
1. **Morning Bank Surge (05:00–08:00)**: Governed by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380\text{ pax/hr}$).
2. **Evening Delay Cascade (14:00/17:00–22:00)**: Governed by network-wide flight delay dispersion ($\sigma_{\text{Delay}} > 63.4\text{ min}$).

---

## 3.7 Hierarchical Cross-Classification Architecture

To establish an unconfounded factorial space for training and benchmarking, the methodology constructs an 84-cell cross-classification tensor:
$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \times 7 \times 3 = 84 \text{ cells})$$

The three constituent axes comprise:
1. **Annual Macro Regimes ($\mathcal{S}$, 4 Regimes)**:
   * `1_OFF_PEAK`: Winter Lull & Mid-Autumn Shoulder (Weeks 3–7, 9, 37–50)
   * `2_MID_PEAK`: Spring Ramps & Late-Summer Shoulder (Weeks 1–2, 8, 10–21, 23, 33–36, 51)
   * `3_PEAK`: Summer Severe Weather & Convective Surge (Weeks 22, 24–32: June–August)
   * `4_HOLIDAY`: National Holiday Travel Corridors (Thanksgiving, Christmas/New Year, Memorial Day, July 4th, Labor Day, MLK, Presidents Day)
2. **Weekly Operational Cycles ($\mathcal{D}$, 7 Days, ISO 8601)**:
   * Monday ($1$) through Sunday ($7$), isolating distinct business outbound, midweek baseline, and Sunday leisure return profiles.
3. **Diurnal Regimes ($\mathcal{H}$, 3 Non-Consecutive Categories per DOW)**:
   * Off-Peak, Mid-Peak, and Peak blocks conditioned on day-of-week queuing dynamics.

---

## 3.8 Statistical Power and Sample Size Sufficiency Proofs

To prevent small-sample estimator degradation and ensure statistical degrees of freedom across all 84 cells, sample sizes were audited across the experimental dataset.

### 3.8.1 Dataset Partitioning (Candidate B Window)
* **Training Partition**: May 1, 2022 to December 31, 2024 ($975$ calendar days = $23,400$ hourly observations).
* **Holdout Testing Partition**: January 1, 2025 to December 31, 2025 ($365$ calendar days = $8,760$ hourly observations).
* **Purge Window**: A strict 7-day embargo between training and test sets to eliminate serial autocorrelation leakage.

### 3.8.2 Degrees-of-Freedom Compliance
* **Training Viability ($N_{\text{train}} \ge 50$)**: Exactly **83 of 84 cells (98.8%)** meet or exceed the minimum training threshold, with a median training depth of **215 observations per cell**. The single cell with $N = 48$ is Holiday Off-Peak Overnight ($00:00\text{--}03:00$).
* **Well-Powered Non-Linear Tree Splits ($N_{\text{train}} \ge 100$)**: **65 of 84 cells (77.4%)** exceed 100 training observations, ensuring sufficient sample depth for gradient boosted decision trees.
* **Asymptotic Holdout Validity ($N_{\text{test}} \ge 30$)**: **70 of 84 cells (83.3%)** meet Central Limit Theorem asymptotic holdout thresholds (Median $N_{\text{test}} = 76$). Remaining cells have 18 to 24 observations, fully satisfying non-parametric Wilcoxon and Diebold-Mariano test requirements.

---

## 3.9 Comparative Evaluation Framework and Model Architectures

### 3.9.1 Model Benchmark Suite ($M_0$ through $M_5$)
* **$M_0$ (Diurnal Seasonal Naive)**: Baseline persistence forecasting $y_t = y_{t-24}$.
* **$M_1$ (Contemporaneous SARIMAX)**: Seasonal autoregressive integrated moving average with contemporaneous scheduled departures.
* **$M_2$ (Empirical Show-Up Curve Regressor)**: Linear model driven by distributed lag passenger arrival curves ($\tau \in [t+1, t+3]$).
* **$M_3$ (Operational LightGBM Regressor)**: Gradient boosted decision tree under Tweedie deviance ($p = 1.3$) combining passenger show-up curves with BTS OTP delay and cancellation features.
* **$M_4$ (Full Tri-Modal Pipeline)**: Gradient boosted regressor interacting show-up curves with T-100 route load factors and carrier gauge.
* **$M_5$ (Sequential Two-Stage SARIMA-Tree Hybrid)**: First-stage SARIMA capturing linear cyclical trends, cascaded into a secondary LightGBM tree predicting residual errors, equipped with recursive Kalman state innovation feedback ($e_t = y_t - C \hat{x}_{t|t-1}$).

### 3.9.2 Evaluation Metrics
* **Root Mean Squared Error (RMSE)**: Penalizes large peak-hour forecast errors.
* **Mean Absolute Error (MAE)**: Measures average absolute volume deviation.
* **Mean Absolute Scaled Error (MASE)**: Scaled against the naive in-sample persistence benchmark:
  $$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N |y_t - \hat{y}_t|}{\frac{1}{N-24}\sum_{t=25}^N |y_t - y_{t-24}|}$$
  where $\text{MASE} < 1.0$ indicates outperformance relative to diurnal persistence.
* **Disruption Error Multiplier ($R_{\text{MASE}}$)**:
  $$R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
  evaluating performance stability under convective disruptions ($R_{\text{MASE}} \le 1.30$ denoting resilience).
* **Transfer Error Penalty (Relative Transfer Ratio, RTR)**:
  $$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
  evaluating spatial portability under zero-shot transfer across terminal complexes.
* **Diebold-Mariano Hypothesis Testing**: Assesses the pairwise statistical significance of forecast error differentials between competing architectures.
