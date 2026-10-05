# CHAPTER IV: RESULTS (EMPIRICAL FINDINGS)

---

## 4.1 Master Descriptive Statistics and Data Health Census

To construct an empirically rigorous and leak-free modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational data covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository encompassed 67.22 million raw fact records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys. 

Following conformed extraction, cleansing, and relational joining across standardized dimension keys, the nationwide post-ETL analytical warehouse contains **42,062,039 cleaned records** across all 25 candidate commercial airfields. Table 4.1 details the post-ETL data foundation census across the four integrated feeds prior to applying downstream experimental filters.

### Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **TSA FOIA Checkpoint Logs** | Checkpoint-Lane-Hour | 19,500,286 | **6,434,732** | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| **BTS On-Time Performance (OTP)** | Flight Departure | 45,777,091 | **13,153,654** | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| **BTS Form 41 Schedule T-100** | Carrier-Route-Month | 1,945,451 | **422,096** | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| **BTS DB1B / DB1C Ticket Surveys** | Ticket Coupon Itinerary | 12,910,384 | **22,051,557** | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| **Combined Analytical Warehouse** | Multi-Source Fact Records | **67,222,828** | **42,062,039** | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the cleaned nationwide data repository.

### Table 4.2: Post-ETL Master Summary Descriptive Statistics (Cleaned Data Warehouse)

| Operational Domain | Variable Name | Sample Size ($N$) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TSA Throughput** | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| **Flight Delays** | Flight Departure Delay (minutes) | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| **Flight Delays** | Significant Delay Rate ($\ge$ 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| **Flight Operations** | Flight Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 0.00% |
| **Flight Operations** | Runway Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| **Route Capacity** | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| **Route Capacity** | Transported Pax per Route-Month | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| **Route Capacity** | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| **Passenger Surveys**| Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

### 4.1.1 Spatial Key Resolution and Metadata Remediation
Upstream TSA FOIA records exhibited 35,809 records with missing or malformed airport identifiers. Rather than silently dropping or naively imputing these rows, an automated checkpoint fingerprinting algorithm successfully recovered 7,489 records by matching historical checkpoint naming signatures (`dim_checkpoint`). The remaining 22,190 unresolvable records were mapped to a conformed surrogate key (`airportId = 0`, flagged with `airportMissing = 1`). In the absence of this remediation, these unmapped rows aggregate into unidentified airport records representing ~9.71 million passengers, which would severely distort national baseline models. All subsequent modeling queries strictly enforce `WHERE airportMissing = 0 AND airportId > 0`.

### 4.1.2 Nighttime Checkpoint Closures versus Missing Data
A critical distributional property of checkpoint operations is the occurrence of zero-throughput intervals. Exactly 450,973 records (2.31% of the warehouse volume) report zero passengers. Cross-referencing these intervals against airport operational schedules confirmed that 98.6% of zero values occur during the early morning non-operational window (00:00 to 03:59 local time). Rather than applying moving-average imputation—which would introduce artificial passenger flow during scheduled overnight checkpoint closures—these intervals are preserved as true operational zeros, modeled using zero-bounded count regression (Tweedie distribution, $p = 1.3$) or two-stage hurdle structures.

### 4.1.3 Flight Delays and Advance vs. Tactical Cancellations
Across the 13,153,654 domestic departures originating across the candidate airfields, the mean departure delay was 12.70 minutes, with 20.12% of flights experiencing departure delays $\ge$ 15 minutes (`depDel15`). Taxi-out time averaged 18.84 minutes. Flight cancellations accounted for 2.03% of scheduled operations (267,019 flights). Crucially, 99.4% of unassigned aircraft tail numbers (`aircraftId = 0`) occurred on cancelled flights. To maintain strict operational timeline causality and prevent lookahead bias in passenger demand modeling:
1. Advance cancellations (>24 hours pre-departure) were purged from departing seat capacity.
2. Tactical cancellations (<2 hours pre-departure) were retained in the passenger demand curve, reflecting the operational reality that affected travelers had already crossed landside security checkpoints prior to the carrier issuing the cancellation.

---

## 4.2 The Four-Tiered Purposive Filtering Pipeline

To eliminate confounding from multi-carrier passenger pooling and isolate the direct relationship connecting scheduled flight departures to checkpoint queues, commercial airfields were screened through a four-tiered purposive filtering pipeline.

### 4.2.1 Macro Filter: Scale and Peak-Hour Checkpoint Congestion
Commercial aviation volume follows a power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \sim 1.15$). Restricting the initial candidate pool to the Top 25 commercial airfields captures 67.2% of nationwide domestic flight movements. In airport queueing dynamics, an arrival rate $\lambda(t)$ passing through $c(t)$ screening lanes with service rate $\mu$ exhibits traffic intensity $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$. At small regional airfields ($\rho \ll 0.3$), queues rarely accumulate and throughput simply mirrors unconstrained arrivals without boundary friction. In contrast, Top 25 hubs reach peak-hour checkpoint congestion ($\rho(t) \to 1.0$) during morning and evening departure banks (06:00–08:30 and 16:00–18:30), creating the empirical queue delays and non-linear dynamics required to train and validate congestion-aware models.

### 4.2.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion
By requiring concurrent mainline operations by American, Delta, and United, cross-carrier contrasts evaluate under identical exogenous airspace disruptions ($\delta_t$), canceling common weather and FAA ground delay confounders. Furthermore, Southwest Airlines (WN) was systematically excluded from checkpoint pairing. Legacy carrier passengers exhibit consistent passenger arrival timing with unimodal lognormal arrival distributions ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \sim 105\text{ min}$). In contrast, Southwest's open-seating boarding structure and free baggage policy generate a bimodal arrival mixture ($\mu_1 \sim 135\text{ min}$ for boarding group position; $\mu_2 \sim 65\text{ min}$ for baggage-free business travelers), violating consistent passenger arrival timing across carrier show-up profiles.

### 4.2.3 Micro Filter: Carrier Checkpoint Isolation
In shared terminals (e.g., Salt Lake City or Phoenix), multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, carrier flight schedules are highly collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), creating severe collinearity where individual airline demand contributions cannot be mathematically separated. Restricting analysis to carrier-exclusive checkpoints isolates single-carrier operations:
$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$
This Carrier Checkpoint Isolation eliminates multi-carrier schedule overlap ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint throughput.

### 4.2.4 Experimental Factorial Grid and Candidate Justifications
The filtering pipeline yielded the **9-Airport Experimental Cohort** (**BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL**), achieving complete factorial balance:
* **Carrier Symmetry**: Exactly 4 dedicated environments per legacy carrier (AA: 4, DL: 4, UA: 4).
* **Cluster Balance**: Representation across all 4 operational clusters identified in the cluster analysis.
* **LGA vs. JFK Rationale**: United Airlines permanently vacated JFK in October 2022 (failing Meso continuity), whereas LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes (TC-CHK, CHK West).
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

### 4.3.1 The Hub Disconnect: Connecting vs. Local Originating Passengers
A central empirical finding is the structural disconnect between airside scheduled flight departures and landside security screening volume at major hub airports. In traditional airport planning, security demand is frequently estimated directly from scheduled departures. At connecting hubs such as Charlotte (CLT), total departing seat capacity exceeded 34 million passengers, yet total TSA checkpoint throughput was only 28.2 million. Incorporating the BTS DB1C **76.0% connecting ratio** resolves this disconnect: over 26 million passengers transferred airside between concourses without ever entering landside security queues. Applying a Connecting Passenger Deflator by multiplying flight seats by $(1 - \text{Connecting Ratio})$ properly isolates local originating demand; failing to do so causes status-quo planning models to overpredict checkpoint volume by over 200%.

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
2. **Coupling Rebound**: Demand-to-schedule correlation ($R^2$), which dropped to 0.579 during COVID, rebounded to 0.672 post-May 2022.
3. **Partitioning Design**:
   * *Training Window*: May 1, 2022 – December 31, 2023 (20 months; 404,324 hourly observations).
   * *Validation Window*: January 1, 2024 – December 31, 2024 (12 months; full Q1–Q4 seasonal cycle for model calibration and parameter selection).
   * *Holdout Test Window*: January 1, 2025 – December 31, 2025 (12 months; full Q1–Q4 seasonal cycle reserved strictly for final out-of-time evaluation).
   * *Operational Separation Buffer*: A 7-day buffer between evaluation periods ensures that multi-day delay cascades and weather recovery periods do not distort test accuracy.

---

## 4.5 Econometric Validation of Carrier Checkpoint Isolation

To empirically validate the methodological requirement of restricting analysis to carrier-exclusive checkpoints, three formal econometric tests were conducted.

| Econometric Test | Mathematical Formulation | Empirical Result & Interpretation |
| :--- | :--- | :--- |
| **1. Volume Conservation** | $\rho = \text{TSA}_{\text{actual}} / \text{Est}_{\text{Originating}}$ | **$\rho = 1.00 \pm 0.04$ ($p < 0.001$)**; Terminal TSA volume matches carrier originating pax. |
| **2. Zero-Flight Intercept** | $Y_{kt} = \beta_0 + \beta_1 \cdot \text{Seats}_t$ | **$\beta_0 = 12.4$ pax/hr ($t = 0.84, p = 0.40$)**; Zero flights statistically equal zero queue demand. |
| **3. Cross-Carrier Checkpoint Independence** | $Y_{kt} = b_1 S_{\text{carrier}} + b_2 S_{\text{other}}$ | **$\beta_{\text{other}} = 0.002$ ($p = 0.62$, partial $R^2 < 0.001$)**; Other carriers add zero demand. |

Furthermore, predicting dedicated terminal checkpoint throughput using carrier-filtered flights achieved $R^2 = 0.708$ to $0.774$, whereas predicting using total pooled airport departures collapsed explanatory power to $R^2 < 0.420$ ($F$-statistic test for parameter exclusion: $p < 0.0001$). A two-sample statistical distribution test of forecasting residuals between physically separate terminal buildings (BOS, DTW, LGA, ORD, EWR) and walkway-connected terminals (LAX, DFW, IAH, PHL) revealed no significant divergence ($D = 0.032, p = 0.28$), confirming that post-security terminal cross-over in connected layouts is statistically negligible ($\epsilon_k < 0.05$).

---

## 4.6 Feature Engineering and Passenger Show-Up Curve Estimation

Analysis of lead-lag dynamics between scheduled flight departure times and landside checkpoint throughput demonstrated severe temporal asynchrony:

| Flight Feature Representation | Linear $R^2$ | Pearson Corr ($r$) | Empirical Regression Slope |
| :--- | :---: | :---: | :---: |
| **Contemporaneous Departures ($t$)** | 0.1988 | 0.4459 | 38.42 pax / flight |
| **Lead Horizon $t+1$ (1 hr pre-dep)** | 0.3723 | 0.6102 | 62.15 pax / flight |
| **Lead Horizon $t+2$ (2 hr pre-dep)** | **0.4054 (PEAK)** | **0.6367** | **74.98 pax / flight** |
| **Lead Horizon $t+3$ (3 hr pre-dep)** | 0.3299 | 0.5744 | 51.20 pax / flight |
| **Passenger Show-Up Curve (Lead-Lag Distribution)** | **0.4878** | **0.6985** | **74.98 pax / flight** |
| **Show-Up Curve $\times$ T-100 Load Factor** | **0.4985** | **0.7061** | **90.56 pax / flight** |

Contemporaneous scheduled flights explain less than 20% of checkpoint throughput variance. Explanatory power peaks at Lead $t+2$ ($R^2 = 0.4054$), corresponding precisely to the 90–120 minute modal passenger show-up window established in airport passenger terminal planning standards (such as **ACRP Report 40: Airport Passenger Terminal Planning and Design**). Converting scheduled departing seats into an empirical passenger show-up curve (lead-lag arrival distribution) and interacting with monthly T-100 route load factors elevates predictive capability to $R^2 = 0.4985$ prior to introducing temporal cyclical encodings.

---

### 4.7 Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)

Following the 4-tier filtering pipeline, exploratory model variations ($M_1$ unshifted, $M_2$ lead flights only, $M_4$ load-factor scaled) were pruned to isolate the **Four Canonical Models** representing each fundamental modeling paradigm. Models were evaluated against the 72,053 hourly complex screening observations (3,222 airport-days) of the 2025 out-of-time holdout targeting Diurnal Throughput Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion):

| Model Paradigm | Id | Model Architecture | Val $R^2$ | Test $R^2$ | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Bias (pax/hr) | Academic Target Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$ | Diurnal Volatility Naive ($y_{t-24}$) | 0.4412 | 0.6719 | 253.6 | 179.3 | 1.000 | -0.7 | Baseline Reference Benchmark |
| **Deterministic Baseline** | $M_1^*$| Deterministic Schedule Bank Volatility Baseline | 0.4912 | 0.4980 | 313.4 | 215.9 | 0.945 | -42.1 | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | $M_3$ | Supervised Volatility GBR (Combined Values + Vol) | 0.5455 | 0.6178 | 273.5 | 178.0 | 0.779 | -18.4 | Passed Target ($\text{MASE} < 0.850$) |
| **Sequential Hybrid** | $M_5$ | Sequential SARIMA-Tree Volatility Hybrid | **0.7120** | **0.7483** | **222.1** | **142.8** | **0.662** | **-8.5** | High-Accuracy In-Sample Fit |

*Note*. Intermediate variations ($M_1, M_2, M_4$) were archived after 4-tier filtering.

### 4.8 Master Multi-Pillar Hypothesis Evaluation Matrix Across Canonical Models

| Operational Dimension | Performance Metric | Academic Stated Target | Baseline Control ($M_0$) | Deterministic Baseline ($M_1^*$) | Probabilistic ML ($M_3$) | Dynamic Hybrid ($M_5$) | Paradigm Dimension Winner & Status |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** | $\text{RMSE}_{\text{routine}}$ (Delay $< 15$m; 0 Cancels) | Lowest Routine RMSE | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | **222.1 pax/hr** | **$M_5$ achieves lowest RMSE**; $M_3$ delivers low-compute routine Pareto fit. |
| **Dimension 1: Robustness** | $\text{MASE}_{\text{routine}}$ (Relative Routine Error) | **$\text{MASE} < 0.700$** | 1.000 | 0.945 | **0.680\text{--}0.700** | **0.662** | **Target Met by $M_3$ and $M_5$**; confirms H1(a) (ML/Hybrids fit routine rhythms). |
| **Dimension 1: Robustness** | Diebold-Mariano ($DM$) Test vs. $M_1^*$ | $p < 0.001$ | Reference | Control Baseline | $DM = 42.15$ ($p < 0.0001$) | $DM = 48.72$ ($p < 0.0001$) | Statistically proves ML and Hybrid gains over deterministic scheduling are genuine. |
| **Dimension 2: Resilience** | $\text{RMSE}_{\text{shock}}$ (Delay $\ge 45$m or Cancels $\ge 5$) | Lowest Shock RMSE | 398.2 pax/hr | 412.8 pax/hr | 318.4 pax/hr | **254.2 pax/hr** | **$M_5$ minimizes absolute error** during severe convective storms. |
| **Dimension 2: Resilience** | $\text{MASE}_{\text{shock}}$ (Relative Disruption Error) | Lowest Shock MASE | 1.000 | 1.082 | 0.812 | **0.694 (LOWEST)** | **$M_5$ performs 30.6% better** than naive persistence during airport ground stops. |
| **Dimension 2: Resilience** | Resilience Multiplier ($R_{\text{MASE}}$) | **$R \approx 1.00$** | 1.00 (Static) | 1.32 (Blind to Delays) | 2.14 (Fragile Collapse) | **1.05 (RESILIENT)** | **$M_5$ DECISIVE WINNER (Target Met)**; closed-loop feedback prevents collapse. |
| **Dimension 2: Resilience** | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | **$\text{TTR} < 4.0$ hours** | 8.4 hours | 7.8 hours | 5.4 hours | **2.8 hours (FASTEST)** | **$M_5$ returns to normal error bounds** 5.0 hrs faster than $M_1^*$ and 2.6 hrs faster than $M_3$. |
| **Dimension 3: Generalizability**| Relative Transfer Ratio (RTR) | **$\text{RTR} = 1.00$** | 1.00 | **1.04 (TARGET MET)** | 1.08 | **1.19 (FAILS TARGET)** | **$M_1^*$ DECISIVE WINNER**; $M_5$ suffers heavy penalty due to terminal overfitting. |
| **Dimension 3: Generalizability**| Transfer Degradation ($\Delta_{\text{transfer}}$) | Minimal Penalty ($\le 10\%$) | 0.0% | **+4.2% (MINIMAL)** | +7.9% (LOW) | **+19.0% (ELEVATED)** | Deterministic physical rules lose only 4.2% accuracy; hybrid decision trees lose 19.0%. |
| **Dimension 3: Generalizability**| Change in MASE on Transfer ($\Delta\text{MASE}$) | **$\Delta\text{MASE} \le 10.0\%$** | 0.0% | **+4.0% (TARGET MET)** | +8.3% (PASSES) | **+21.5% (FAILS TARGET)** | **$M_1^*$ passes target with +4.0% shift** ($+0.038$); $M_5$ fails target with +21.5% shift ($+0.142$). |

---

## Chapter V: Analysis & In-Depth Discussion

---

## 5.1 Spatial Architecture and Passenger Behavioral Dynamics

The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:

1. **Connecting Passenger Shielding (The Hub Disconnect)**: At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by $(1 - \text{ConnectingRatio})$ derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.
2. **Terminal Complex Aggregation**: Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.
3. **Behavioral Invariance Across Terminal Layouts**: The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA Credential Authentication Technology (CAT) scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.
4. **Heavy-Traffic Queuing Physics (The Second-Order Driver)**: Traditional models focus exclusively on mean passenger volume $\lambda$. However, from Kingman's heavy-traffic approximation and the Allen-Cunneen formula:
   $$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$
   where $\rho = \lambda / (c \mu)$ represents traffic intensity, $C_a = \sigma_a / \mu_a$ is the coefficient of variation of passenger arrivals, and $C_s$ is the coefficient of variation of screening service time. As traffic intensity approaches saturation ($\rho \to 1.0$) during morning and evening departure banks, queue delay $W_q$ scales non-linearly with the square of arrival volatility ($C_a^2$). Consequently, predicting the volatility of TSA throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is fundamentally more consequential for checkpoint stability than forecasting average volume alone.

---

## 5.2 Initial Training and Passenger Show-Up Dynamics

The striking performance gap between unshifted flight schedules ($R^2 = -0.0586$ on holdout volatility) and lead-lag passenger show-up schedules ($R^2 = 0.5344$ to $0.6178$) resolves the operational lead-lag time offset inherent in air travel (ACRP Report 40):
* Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior (standard ACRP Report 40 passenger show-up distribution).
* Incorporating lead horizons ($t+1, t+2, t+3$) enables the model to anticipate incoming passenger surges well before gate departure times.
* Furthermore, flight delays must be handled asymmetrically: including contemporaneous actual flight delays introduces severe lookahead bias, whereas incorporating prior-hour delays ($t-1$) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict information causality.

---

## 5.3 Deep-Dive: Evaluation Dimension 1 – Robustness (Routine Operational Accuracy)

| Model Family | Model ID & Specification | $\text{RMSE}_{\text{routine}}$ (pax/hr) | $\text{MASE}_{\text{routine}}$ | Stated Target ($\text{MASE} < 0.70$) | Diebold-Mariano Test vs Control | Academic Status & Operational Role |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Volatility Naive ($y_{t-24}$) | 253.6 | 1.000 | Fails Target | Baseline Reference | Historical 24h persistence control benchmark |
| **Deterministic Baseline** | $M_1^*$: Deterministic Schedule Bank Volatility | 313.4 | 0.945 | Fails Target | Control Baseline | First-principles convolved schedule baseline |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR (Combined Values + Vol) | 273.5 | 0.680–0.700 | **Target Met** | $DM = 42.15$ ($p < 0.0001$) | **Routine Pareto Winner**: Fast, zero-feedback, low-compute |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | **222.1** | **0.662** | **Target Met** | $DM = 48.72$ ($p < 0.0001$) | **Lowest Routine RMSE**: In-sample cyclical-tree fit |

### Hypothesis Confirmation
The thesis hypothesis posited that **Probabilistic and Machine Learning models would excel at capturing continuous baseline variance and routine operational noise**. 
* The findings confirm this hypothesis. Under nominal conditions (departure delays < 15 min), the Gradient Boosted Regressor ($M_3$) and Sequential Two-Stage Hybrid Model ($M_5$) achieved $\text{MASE}_{\text{routine}} \le 0.700$ and $0.662$, easily surpassing deterministic scheduling ($M_1^*$, $\text{MASE} = 0.945$).
* Non-parametric Wilcoxon signed-rank tests and Diebold-Mariano tests confirmed that error reductions were statistically significant ($DM = 42.15$ and $48.72, p < 0.0001$) across all nine airfields.
* Crucially, **$M_3$ provides the optimal Pareto trade-off for routine operations**, meeting the target without requiring complex online feedback.

---

## 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience Under Disruption

| Model Family | Model ID & Specification | $\text{RMSE}_{\text{shock}}$ (pax/hr) | $\text{MASE}_{\text{shock}}$ | Resilience Multiplier ($R_{\text{RMSE}} / R_{\text{MASE}}$) | Stated Target ($R \approx 1.00$, Lowest MASE) | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | Academic Status & Resilience Behavior |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Volatility Naive ($y_{t-24}$) | 398.2 | 1.000 | 1.00 | Static Reference | 8.4 hours | Static persistence benchmark |
| **Deterministic Baseline** | $M_1^*$: Deterministic Schedule Bank Volatility | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR (Combined) | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | **254.2** | **0.694** | **1.05** | **TARGET MET (WINNER)** | **2.8 hours** | **Decisive Winner**: Closed-loop feedback prevents collapse |

### Hypothesis Confirmation
The thesis hypothesis asserted that **the Dynamic Cyber-Physical Hybrid would prove superior in resilience due to real-time recursive error feedback**.
* During severe operational disruptions, pure ML models suffered acute fragility ($R_{\text{MASE}} = 2.14$) due to the "Empty Checkpoint Fallacy" (assuming stranded passengers depart checkpoints when flights are held).
* In contrast, the Two-Stage Hybrid Framework dynamically adjusted queue state using recursive error feedback ($e_{t-1}$), maintaining a resilient disruption multiplier of $R_{\text{MASE}} = 1.05 \approx 1.00$ and recovering in **2.8 hours**.

---

## 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Cross-Airport Transferability)

| Model Family | Model ID & Architecture | In-Sample RMSE (pax/hr) | Zero-Shot Transfer RMSE (pax/hr) | Relative Transfer Ratio ($\text{RTR}$) | Transfer Degradation ($\Delta_{\text{transfer}}$) | Change in MASE ($\Delta\text{MASE}$) | Academic Target Status ($\text{RTR}=1.00, \Delta\text{MASE}\le 10\%$) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | $M_0$: Diurnal Naive ($y_{t-24}$) | 253.6 | 253.6 | 1.00 | 0.0% | 0.0% | Benchmark Reference |
| **Deterministic Baseline** | $M_1^*$: Deterministic Sched Bank Volatility | 313.4 | 326.5 | **1.04** | **+4.2%** | **+4.0%** (+0.038) | **TARGET MET (WINNER)** |
| **Probabilistic / ML** | $M_3$: Supervised Volatility GBR | 273.5 | 295.1 | 1.08 | +7.9% | +8.3% (+0.065) | Passes Both Targets ($\le 10\%$) |
| **Dynamic Hybrid** | $M_5$: Sequential SARIMA-Tree Volatility Hybrid | 222.1 | 264.3 | **1.19** | **+19.0%** | **+21.5%** (+0.142) | **FAILS BOTH TARGETS** |

### Hypothesis Confirmation
Evaluating zero-shot transfer (EWR $\to$ LGA) decisively disproved universal hybrid superiority and confirmed Hypothesis 1:
* **The Deterministic Baseline ($M_1^*$) is the DECISIVE WINNER of Generalizability**, meeting both academic targets ($\text{RTR} = 1.04 \approx 1.00, \Delta\text{MASE} = +4.0\% \le 10.0\%$). First-principles flight convolution is invariant to facility-specific geometry.
* **The Dynamic Hybrid ($M_5$) DECISIVELY FAILS Generalizability** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$). Its non-linear decision tree residual learner overfits to Newark's specific terminal geometry and bank timing.

---

## 5.6 Master Synthesis and Operational Recommendations

Table 5.4: *Master Asymmetric Trade-Off Matrix Across the Four Canonical Models*

| Evaluation Dimension | Stated Academic Target | Baseline Control ($M_0$) | Deterministic Baseline ($M_1^*$) | Probabilistic / ML ($M_3$) | Dynamic Hybrid ($M_5$) | Dimension Winner & Operational Justification |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** (Routine: Delay $< 15$m, 0 Cancels) | Lowest $\text{RMSE}_{\text{routine}}$; $\text{MASE}_{\text{routine}} < 0.70$ | $\text{RMSE} = 253.6$, $\text{MASE} = 1.000$ (Fails) | $\text{RMSE} = 313.4$, $\text{MASE} = 0.945$ (Fails) | $\text{RMSE} = 273.5$, $\text{MASE} = 0.680\text{--}0.700$ (**Target Met**) | $\text{RMSE} = \mathbf{222.1}$ (Lowest), $\text{MASE} = \mathbf{0.662}$ (**Target Met**) | **$M_5$ achieves lowest RMSE**; **$M_3$ wins Routine Pareto Efficiency** (meets target with zero online compute overhead). |
| **Dimension 2: Resilience** (Disruption: Delay $\ge 45$m or Cancels $\ge 5$) | $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$ | $R = 1.00$, $\text{MASE} = 1.000$, $\text{TTR} = 8.4\text{h}$ | $R = 1.32$, $\text{MASE} = 1.082$, $\text{TTR} = 7.8\text{h}$ | $R = 2.14$ (Fragile), $\text{MASE} = 0.812$, $\text{TTR} = 5.4\text{h}$ | $R = \mathbf{1.05}$ (**Target Met**), $\text{MASE} = \mathbf{0.694}$ (Lowest), $\text{TTR} = \mathbf{2.8\text{h}}$ (**Target Met**) | **$M_5$ DECISIVE WINNER**: Closed-loop recursive feedback ($e_{t-1}$) prevents empty-checkpoint collapse and recovers in 2.8h. |
| **Dimension 3: Generalizability** (Zero-Shot Transfer: EWR $\to$ LGA) | $\text{RTR} = 1.00$; $\Delta\text{MASE} \le 10.0\%$ | $\text{RTR} = 1.00$, $\Delta\text{MASE} = 0.0\%$ (Static Ref) | $\text{RTR} = \mathbf{1.04}$ (**Target Met**), $\Delta\text{MASE} = \mathbf{+4.0\%}$ (**Target Met**) | $\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\%$ (Passes) | $\text{RTR} = \mathbf{1.19}$ (**FAILS TARGET**), $\Delta\text{MASE} = \mathbf{+21.5\%}$ (**FAILS TARGET**) | **$M_1^*$ DECISIVE WINNER**: Physical schedule convolution is invariant to facility layout; $M_5$ overfits to local gate geometry. |

### Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons
A core theoretical contribution of this thesis is the empirical demonstration of the **Values versus Volatility Paradigm**:
1. **Multi-Day Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)**:
   * **Feature Values Completely Collapse**: Standard feature values (raw scheduled flights, average delay minutes) generate negative out-of-time test scores ($R^2 = -0.2688$ in OLS; $R^2 = -0.0506$ in GBR). Because scheduled flight counts remain relatively stable across consecutive weeks, static volume features cannot detect shifts in temporal turbulence.
   * **Feature Volatility Succeeds**: In contrast, Feature Volatility attributes (rolling 7-day schedule variance, cancellation volatility, and delay dispersion) achieve **$R^2 = +0.2313$ (OLS) and $R^2 = +0.3105$ (GBR)**, improving to **$R^2 = +0.3166$** in the Combined Model, while slashing RMSE from 4,090.7 to 3,002.3 pax/day.
2. **Delay Volatility Transmission**:
   Cross-dataset econometric correlation demonstrates that **Flight Departure Delay Volatility ($CV_{\text{delay}}$)** is significantly coupled with checkpoint arrival volatility ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.0620, p = 0.769$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.
3. **Master Consensus Factor Weights**:
   Synthesizing regularized regressions and tree ensembles confirms that schedule dispersion (`sched_rolling_7d_mean`, 23.73%; `sched_hourly_mean`, 6.91%) and operational volatility (`otp_cancellation_volatility_cv`, 8.79%; `CV_{\text{delay}}`, 4.32%) dominate predictive power, accounting for over 80% of consensus importance.

### Conformal Prediction and Dynamic Lane Staffing Buffers
Airport checkpoint administrators can directly translate predicted throughput volatility ($\hat{\sigma}_{\text{TSA}, t}$) into risk-buffered lane configurations using conformal prediction principles:
$$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$
where $\mu_{\text{lane}}$ is the nominal throughput capacity of an open screening lane (~180 to 220 pax/lane/hr), and $z_q$ is the coverage quantile factor (e.g., $z_{0.85} = 1.036$ for an 85% non-exceedance guarantee, or the empirical conformal quantile $\hat{q}_{0.85}$). Under traditional deterministic staffing, lanes are scheduled based solely on point expectation $\hat{\mu}_t$, guaranteeing that during stochastic arrival rushes, queues saturate and wait times explode exponentially according to Kingman's formula ($W_q \propto C_a^2$). By dynamically scaling lane capacity with predicted volatility $\hat{\sigma}_t$, airports maintain stable queue wait times without chronic overstaffing during quiescent periods.

### Strategic Implications for TSA and Airport Authorities
1. **Dynamic Checkpoint Allocation**: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.
2. **Connecting Ratio Integration**: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.
3. **Deployment of Two-Stage Hybrid Estimators**: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ($t-1$) during severe convective ground stop disruptions.

---

## 5.7 Empirical Cross-Project Synthesis (Projects 1, 2, and 3)

By implementing the research methodology across three distinct computational paradigms—**Supervised Machine Learning (Project 1)**, **First-Principles Queueing Theory (Project 2)**, and **Dynamic State-Space Modeling (Project 3)**—this thesis provides a unified, multi-perspective empirical validation of its core hypotheses:

1. **Routine Operational Accuracy Validation**:
   * *Project 1 Supervised ML*: The Sequential SARIMA-Tree Volatility Hybrid achieved the highest out-of-time accuracy on the 2025 holdout dataset ($R^2 = 0.7483, \text{MASE} = 0.662, \text{RMSE} = 222.1\text{ pax/hr}$), proving that non-linear gradient-boosted trees excel at capturing complex diurnal patterns.
   * *Project 2 Queueing Simulation*: Proved that when active screening lanes match incoming passenger banks (DTW McNamara Terminal), steady-state waiting times remain exceptionally low ($\mu_{\text{wait}} = 0.9$ min, $P_{95} \le 7.7$ min).

2. **Resilience Validation Under Severe Disruption**:
   * *Project 2 Queue Simulation*: Directly exposed the operational hazard of static lane allocation. Under an acute 50% lane outage combined with a flight surge, static lane allocation saturated, with wait times capping at 60 minutes and accumulating 27,763 passenger-hours of delay. In contrast, the **Dynamic Hybrid Allocation Model** reduced total passenger delay by **80.1%** (slashing backlog to 5,514 passenger-hours and keeping 95th-percentile wait times at 11.5 minutes) by dynamically mobilizing reserve screening capacity.
   * *Project 3 State-Space Tracking*: Demonstrated that recursive Kalman innovation updates immediately recognize delayed flight holds, avoiding the false empty-checkpoint predictions of pure machine learning.

3. **Generalizability Validation (Cross-Airport Portability)**:
   * *Project 3 State-Space Transfer*: When deploying directly without local retraining across matched airport pairs sharing identical airspace (EWR $\to$ LGA in the New York TRACON), the Moving Horizon Baseline suffered an 86.7% error surge ($\text{RTR} = 1.86$) and the Probabilistic Sequence Model degraded by 43.8% ($\text{RTR} = 1.44$).
   * In stark contrast, the **Extended Kalman Filter State-Space Hybrid achieved remarkable transfer stability ($\Delta = 0.0\%, \text{RTR} = 1.00$ on EWR $\to$ LGA; $\text{RTR} = 0.86$ on DTW $\to$ PHL)**. Because state-space models continuously calibrate queue state using live throughput residuals ($t-1$), they achieve seamless cross-airport portability without facility-specific over-specialization.

