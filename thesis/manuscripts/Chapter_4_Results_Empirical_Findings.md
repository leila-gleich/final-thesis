# CHAPTER IV: RESULTS (EMPIRICAL FINDINGS)

---

## 4.1 Master Descriptive Statistics and Data Health Census

To construct an empirically rigorous and leak-free modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational data covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository encompassed 67.22 million raw fact records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys. 

Following conformed extraction and relational joining across conformed dimension surrogate keys, the filtered multi-airport warehouse represents an exhaustive census of commercial aviation activity across the nine purposively selected airfields (**BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL**).

| Primary Feed | Entity Grain | Processed Rows | Coverage & Conformance Status |
| :--- | :--- | :---: | :--- |
| **TSA FOIA Throughput** | Checkpoint-Hour | **3,127,078** | 100% Not Null; Zero Orphans |
| **BTS On-Time Performance** | Flight Departure | **10,275,065** | 294 Domestic Destinations; 18 Reporting Carriers |
| **BTS T-100 Segments** | Carrier-Segment-Month | **370,148** | 1.09 Billion Departing Mainline Seats |
| **BTS DB1B/DB1C Coupons** | Ticket Itinerary | **2,098,944** | Closed 9-Airport City Pairs Sample |

### 4.1.1 Spatial Key Resolution and Metadata Remediation
Upstream TSA FOIA records exhibited 35,809 records with missing or malformed airport identifiers. Rather than silently dropping or naively imputing these rows, an automated checkpoint fingerprinting algorithm successfully recovered 7,489 records by matching historical checkpoint naming signatures (dim_checkpoint). The remaining 22,190 unresolvable records were mapped to a conformed surrogate key (airportId = 0, flagged with airportMissing = 1). In the absence of this remediation, these unmapped rows aggregate into an artificial, composite phantom airport representing ~9.71 million passengers, which would severely distort national baseline models. All subsequent modeling queries strictly enforce WHERE airportMissing = 0 AND airportId > 0.

### 4.1.2 Operational Zeros versus Sensor Missingness
A critical distributional property of checkpoint operations is the occurrence of zero-throughput intervals. Exactly 450,973 records (2.31% of the warehouse volume) report zero passengers. Cross-referencing these intervals against airport operational schedules confirmed that 98.6% of zero values occur during the early morning non-operational window (00:00 to 03:59 local time). Rather than applying moving-average imputation—which would introduce artificial passenger flow during physical lane closures—these intervals are preserved as true structural zeros, modeled using Tweedie deviance loss functions (p = 1.3) or two-stage hurdle structures.

### 4.1.3 Flight Delays and Advance vs. Tactical Cancellations
Across the 10,275,065 domestic departures originating from the nine airfields, the mean departure delay was 11.64 minutes, with 17.82% of flights experiencing departure delays >= 15 minutes (depDel15). Taxi-out time averaged 18.71 minutes. Flight cancellations accounted for 2.16% of scheduled operations (221,941 flights). Crucially, 99.4% of unassigned aircraft tail numbers (aircraftId = 0) occurred on cancelled flights. To prevent lookahead leakage in passenger induction modeling:
1. Advance cancellations (>24 hours pre-departure) were purged from departing seat capacity.
2. Tactical cancellations (<2 hours pre-departure) were retained in the passenger demand curve, reflecting the physical reality that affected travelers had already crossed landside security checkpoints prior to the carrier issuing the cancellation.

---

## 4.2 The Four-Tiered Purposive Filtering Pipeline

To eliminate confounding from passenger pooling and isolate the pure mathematical transfer function connecting flight schedules to checkpoint queues, commercial airfields were screened through a four-tiered purposive filtering pipeline.

### 4.2.1 Macro Filter: Scale and Heavy-Traffic Asymptotics
Commercial aviation volume follows a power-law distribution (P(X > x) ~ x^(-alpha), alpha ~ 1.15). Restricting the initial candidate pool to the Top 25 commercial airfields captures 67.2% of nationwide domestic flight movements. In queueing theory, an arrival rate lambda(t) passing through c(t) screening lanes with service rate mu exhibits traffic intensity rho(t) = lambda(t) / (c(t)*mu). At small regional airfields (rho << 0.3), queue length Q(t) ~ 0 and throughput mirrors unconstrained arrivals without boundary friction. In contrast, Top 25 hubs reach rho(t) -> 1.0 during peak departure banks (06:00–08:30 and 16:00–18:30), creating the empirical queue delays and non-linear dynamics required to train and validate congestion-aware models.

### 4.2.2 Meso Filter: Shock Invariance and Southwest Exclusion
By requiring concurrent mainline operations by American, Delta, and United, cross-carrier contrasts evaluate under identical exogenous airspace disruptions (delta_t), canceling common weather and FAA ground delay confounders. Furthermore, Southwest Airlines (WN) was systematically excluded from checkpoint pairing. Legacy carriers exhibit unimodal lognormal arrival distributions (tau ~ Lognormal(mu, sigma^2), E[tau] ~ 105 min). In contrast, Southwest's open-seating boarding structure and free baggage policy generate a bimodal arrival mixture (mu_1 ~ 135 min for boarding group position; mu_2 ~ 65 min for baggage-free business travelers), violating parameter exchangeability across carrier arrival kernels.

### 4.2.3 Micro Filter: Checkpoint Exclusivity
In shared terminals (e.g., Salt Lake City or Phoenix), multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, carrier flight schedules are highly collinear (Corr(S_j, S_j') >= 0.88), yielding ill-conditioned Gram matrices (kappa(X^T X) >> 10^4) where individual airline demand contributions are mathematically unidentifiable. Restricting analysis to carrier-exclusive checkpoints collapses the mixture:
P(Carrier = j* | Checkpoint k) = 1.0
This reduces estimation to an orthogonal Wiener-Hopf deconvolution (kappa < 25), directly mapping carrier flight banks to physical checkpoint throughput.

### 4.2.4 Experimental Factorial Grid and Candidate Justifications
The filtering pipeline yielded the **9-Airport Experimental Cohort**, achieving complete factorial balance:
* **Carrier Symmetry**: Exactly 4 dedicated environments per legacy carrier (AA: 4, DL: 4, UA: 4).
* **Cluster Balance**: Representation across all 4 operational clusters identified in the cluster analysis.
* **LGA vs. JFK Rationale**: United Airlines permanently vacated JFK in October 2022 (failing Meso temporal continuity), whereas LGA opened Delta's B consolidated Terminal C in June 2022, providing unconfounded screening lanes (TC-CHK, CHK West).
* **PHL vs. SLC Rationale**: Salt Lake City funnels all carriers through a single consolidated central screening checkpoint, making carrier isolation impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints (Terminals B and C), establishing an East Coast fortress control counterpart to Delta's Midwestern fortress at DTW.

---

## 4.3 Empirical Operational Clusters and Systemic Trends

Unsupervised machine learning (PCA coupled with K-Means and Ward's Hierarchical Clustering) evaluated across standardized operational metrics revealed four distinct operational archetypes across the Top 25 airfields.

| Feature | PC1 (Scale & Congestion) | PC2 (Gauge vs Vulner.) | PC3 (Connecting Dominance) |
| :--- | :---: | :---: | :---: |
| log_actual_tsa | 0.364 | 0.357 | -0.001 |
| log_estimated_tsa | 0.432 | 0.199 | -0.054 |
| connecting_ratio | -0.151 | 0.108 | 0.583 |
| avg_aircraft_seats | 0.105 | 0.519 | 0.187 |
| route_load_factor | 0.308 | 0.410 | 0.003 |
| avg_dep_delay | 0.368 | -0.321 | 0.363 |
| depDel15_rate | 0.355 | -0.183 | 0.500 |
| cancel_rate | 0.275 | -0.466 | 0.011 |
| avg_taxi_out | 0.347 | -0.172 | -0.295 |
| **Explained Variance Ratio** | **33.8%** | **25.5%** | **17.7% (Cumulative: 77.0%)** |

| Cluster Archetype | Count | Member Airfields | Mean TSA | Est Demand | Conn Ratio | Load Fact | Gauge | Mean Delay |
| :--- | :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| **0: Mega-Connecting Gateways** | 8 | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 17.3M | 56.1% | 85.7% | 177.8 | 15.6 min |
| **1: High-Density O&D Focus** | 6 | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 11.2M | 48.4% | 83.4% | 164.0 | 15.0 min |
| **2: High-Reliability Fortress Hubs** | 8 | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 9.7M | 54.1% | 84.5% | 172.3 | 11.6 min |
| **3: Congested Coastal Originators** | 3 | EWR, JFK, LGA | 85.6M | 14.9M | 37.4% | 85.4% | 164.1 | 16.1 min |

### 4.3.1 The Connecting Ratio Paradox
A central finding is the structural decoupling between airside scheduled flight departures and landside security screening volume. At connecting fortresses such as Charlotte (CLT), total departing seat capacity exceeded 34 million passengers, yet total TSA checkpoint throughput was only 28.2 million. Incorporating the BTS DB1C **76.0% connecting ratio** resolves this paradox: over 26 million passengers transferred airside between concourses without ever entering landside security queues. Failing to account for connecting fractions causes baseline models to overpredict checkpoint volume by over 200%.

### 4.3.2 Delay Transmission Divergence
Cluster 2 airfields (DTW, MSP, SLC, PHL) handle immense connecting volume with exceptional fluidity (mean delay = 11.6 min; taxi-out = 18.7 min). Conversely, Cluster 3 airfields (EWR, JFK, LGA) suffer chronic delay burdens (mean delay = 16.1 min; taxi-out = 24.3 min) despite operating smaller regional gauge (154 seats at LGA), demonstrating that terminal congestion is driven by airspace slot caps and runway geometry rather than passenger volume alone.

---

## 4.4 Temporal Demarcation: Post-Pandemic Regime Selection

| Evaluation Criteria | Candidate A: Mature Post-Pandemic | Candidate B: Early Post-Mask Regime * |
| :--- | :--- | :--- |
| **Start Date** | January 1, 2023 | **May 1, 2022 (RECOMMENDED)** |
| **Statistical Justification** | Rolling Welch's t-test convergence | CUSUM stabilization; Mask Mandate Repeal |
| **Training Data Span** | 24 Months (2023-01 to 2024-12) | **36 Months (2022-05 to 2024-12)** |
| **Test Data Span** | 12 Months (2025 Holdout) | **12 Months (2025 Holdout)** |
| **Robustness Impact** | Excellent baseline stability | **Superior (Captures 2 full annual cycles)** |
| **Resilience Impact** | Fails to capture Winter Storm 2022 | **Superior (Captures Elliott & Summer '23)** |
| **Generalizability Impact**| Smaller sample for spoke airfields | **Superior (404k+ training observations)** |

Structural break tests confirmed **May 1, 2022** as the optimal demarcation point for model development:
1. **Mask Mandate Repeal**: The nationwide lifting of federal transit mask requirements in late April 2022 restored passenger boarding behaviors to equilibrium.
2. **Coupling Rebound**: Demand-to-schedule correlation (R^2), which dropped to 0.579 during COVID, rebounded to 0.672 post-May 2022.
3. **Partitioning Design**:
   * *Training Window*: May 1, 2022 – December 31, 2023 (20 months; 404,324 hourly observations).
   * *Validation Window*: January 1, 2024 – December 31, 2024 (12 months; full Q1–Q4 seasonal cycle for hyperparameter tuning).
   * *Holdout Test Window*: January 1, 2025 – December 31, 2025 (12 months; full Q1–Q4 seasonal cycle reserved strictly for final out-of-time evaluation).
   * *Purge Embargo*: A 7-day purge window between folds prevents temporal autocorrelation leakage.

---

## 4.5 Econometric Validation of Checkpoint Exclusivity

To empirically validate the methodological requirement of restricting analysis to carrier-exclusive checkpoints, three formal econometric tests were conducted.

| Econometric Test | Mathematical Formulation | Empirical Result & Interpretation |
| :--- | :--- | :--- |
| **1. Volume Conservation** | rho = TSA_actual / Est_Originating | **rho = 1.00 +/- 0.04 (p < 0.001)**; Terminal TSA volume equals carrier pax. |
| **2. Zero-Flight Intercept** | Y_kt = beta_0 + beta_1 * Seats_t | **beta_0 = 12.4 pax/hr (t = 0.84, p = 0.40)**; Zero flights = zero queue demand. |
| **3. Cross-Carrier Orthogonality** | Y_kt = b_1 S_carrier + b_2 S_other | **beta_other = 0.002 (p = 0.62, partial R^2 < 0.001)**; Other carriers add 0 demand. |

Furthermore, predicting dedicated terminal checkpoint throughput using carrier-filtered flights achieved R^2 = 0.708 to 0.774, whereas predicting using total pooled airport departures collapsed explanatory power to R^2 < 0.420 (F-statistic test for parameter exclusion: p < 0.0001). A two-sample Kolmogorov-Smirnov test of forecasting residuals between Type I (hard air-gapped: BOS, DTW, LGA, ORD, EWR) and Type II (airside connected: LAX, DFW, IAH, PHL) revealed no significant divergence (D = 0.032, p = 0.28), confirming that airside leakage in Type II layouts is statistically negligible (epsilon_k < 0.05).

---

## 4.6 Feature Engineering and Lead-Lag Arrival Deconvolution

Analysis of lead-lag dynamics between scheduled flight departure times and landside checkpoint throughput demonstrated severe temporal asynchrony:

| Flight Feature Representation | Linear R^2 | Pearson Corr (r) | Empirical Regression Slope |
| :--- | :---: | :---: | :---: |
| **Contemporaneous Departures (t)** | 0.1988 | 0.4459 | 38.42 pax / flight |
| **Lead Horizon t+1 (1 hr pre-dep)** | 0.3723 | 0.6102 | 62.15 pax / flight |
| **Lead Horizon t+2 (2 hr pre-dep)** | **0.4054 (PEAK)** | **0.6367** | **74.98 pax / flight** |
| **Lead Horizon t+3 (3 hr pre-dep)** | 0.3299 | 0.5744 | 51.20 pax / flight |
| **Continuous Convolved Lead Demand**| **0.4878** | **0.6985** | **74.98 pax / flight** |
| **Convolved Demand * T-100 Load Factor** | **0.4985** | **0.7061** | **90.56 pax / flight** |

Contemporaneous scheduled flights explain less than 20% of checkpoint variance. Explanatory power peaks at Lead t+2 (R^2 = 0.4054), corresponding precisely to the 90–120 minute modal arrival window identified in ACRP passenger behavior studies. Convolving scheduled seats through a continuous arrival density function (f_arr) and interacting with monthly T-100 route load factors elevates predictive capability to R^2 = 0.4985 prior to introducing temporal cyclical encodings.

---

## 4.7 Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)

Models spanning the three paradigms were trained on Candidate B data (May 2022 – Dec 2023), tuned on 2024 validation data, and evaluated against the 215,562 hourly observations of the 2025 out-of-time holdout:

| Model Paradigm | Id | Model Architecture & Mechanics | Val R^2 | Test R^2 | Test RMSE | Test MAE | Test MASE | Category / Mechanics |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deterministic Baseline** | M0 | Diurnal Seasonal Naive (y-24) | 0.4951 | 0.4508 | 1377.3 | 939.8 | 1.000 | Persistence Control |
| **Deterministic Baseline** | M1 | Rebuilt Deterministic 2-Hr Static Lead | 0.5312 | **0.5293** | **1265.4** | **902.1** | **0.942** | Deterministic (Static 2-Hr Lead) |
| **Probabilistic / ML** | M2 | Convolved Lead Flights Only | 0.5443 | 0.5862 | 1195.5 | 856.2 | 0.911 | Continuous Density Density |
| **Probabilistic / ML** | M3 | LightGBM Tweedie (Convolved + OTP) | 0.5450 | **0.5880** | **1192.9** | **855.1** | **0.910** | Probabilistic (Stochastic Volatility) |
| **Probabilistic / ML** | M4 | Full Tri-Modal Pipeline (LF) | 0.5798 | 0.5771 | 1208.6 | 856.3 | 0.911 | Tri-Modal Feature Space |
| **Dynamic Hybrid** | M5 | Sequential SARIMA-Tree Hybrid | **0.6644** | **0.6270** | **1135.0** | **795.0** | **0.846** | Dynamic Cyber-Physical Hybrid |

*Note on Model Mechanics*:
* **M1 (Rebuilt Deterministic Baseline)** applies a static, rigid 2-hour pre-departure shift ($t+2$) to scheduled flight seats without modeling stochastic passenger arrival volatility, weather disruptions, or flight delay propagation.
* **M3 (Probabilistic ML)** models passenger arrivals as a continuous stochastic lognormal probability distribution, incorporating load factor variance and real-time operational delay distributions via Tweedie deviance ($p=1.3$).
* **M5 (Dynamic Hybrid)** combines the static schedule trend with dynamic state-space error feedback.
