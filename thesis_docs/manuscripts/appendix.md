# Appendix: Econometric Foundations, Methodological Architecture, and Peer-Reviewed Equation Registry
*Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)*  
*Author: Leila Gleich | Committee Review Draft | Embry-Riddle Aeronautical University*

---

## Executive Overview and Structural Organization

This appendix compiles the complete econometric derivations, data engineering profiles, sample filtering audits, empirical seasonal baselines, holdout evaluation benchmarks, and operational implementation frameworks supporting the thesis. To preserve full scientific transparency, comprehensive auditability, and immediate navigation for committee review, the appendix is organized across **twenty-four dedicated, lettered appendices (Appendix A through Appendix X)**, sequenced in the **exact chronological order in which they are introduced and referenced across the thesis manuscript chapters** (Chapter I $\to$ Chapter II $\to$ Chapter III $\to$ Chapter IV $\to$ Chapter V):

### Chapter I Cross-References (Introduction & Scope)
* **Appendix A**: Delimitations of the Study
* **Appendix B**: Research Limitations and Methodological Assumptions

### Chapter II Cross-References (Literature Review & Theoretical Foundations)
* **Appendix C**: Connecting Queuing Principles to Dynamic Lane Staffing and Safety Cushion
* **Appendix D**: Peer-Reviewed Literature Equation Registry and Mathematical Formulations
* **Appendix E**: Construct Validity and Passenger Throughput Volatility Formulations

### Chapter III Cross-References (Methodology, Data Engineering & Operational Apparatus)
* **Appendix F**: Candidate Predictive Modeling Suite and Operational Regimes
* **Appendix G**: Temporal Scope, Post-Pandemic Demarcation, and COVID-19 Boundary Definition
* **Appendix H**: Archival Data Storage Infrastructure, Directory Hierarchy, and Screenshot Catalog
* **Appendix I**: Four-Tier Purposive Filtering Pipeline Architecture and Progression
* **Appendix J**: Multi-Source Aviation Data Ingestion and Post-ETL Descriptive Statistics
* **Appendix K**: Treatment of Data: Extract, Transform, Load (ETL) Architecture and Hygiene Protocols
* **Appendix L**: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority
* **Appendix M**: Operational Evaluation Metrics and Performance Criteria Interpretation
* **Appendix N**: Feature Engineering Pipeline Details and Empirical Arrival Convolution

### Chapter IV Cross-References (Results, Empirical Filtering & Holdout Evaluation)
* **Appendix O**: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Local Weekly Profiles
* **Appendix P**: Diurnal Bimodal Turbulence Dynamics and Multi-Carrier Collinearity
* **Appendix Q**: Econometric Validation of Carrier Checkpoint Demand Isolation
* **Appendix R**: Top 25 Network Census vs. Nine-Airport Experimental Cohort
* **Appendix S**: Key Airport Selection Contrasts (LGA vs. JFK, PHL vs. SLC)
* **Appendix T**: Master Multi-Pillar Hypothesis Evaluation Matrix and Holdout Benchmarks
* **Appendix U**: The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons

### Chapter V Cross-References (Discussion, Mechanism Analysis & Decision Playbook)
* **Appendix V**: The Lead-Lag Asynchrony Mechanism and Shock Interaction Dynamics
* **Appendix W**: Resilience Mechanics and the Empty Checkpoint Fallacy Under Severe Disruption
* **Appendix X**: Dual-Track Operational Decision Playbook and Real-World Application

---

# Appendix A: Delimitations of the Study

> *Note on Thesis Cross-References*: This appendix establishes the formal boundaries, geographic coverage, longitudinal timeline, and evaluation standards restricting the research scope. It is referenced in **Chapter I (Introduction)**, Section 1.6 (*Delimitations*).

This study focuses on U.S. commercial airports and evaluates post-pandemic passenger throughput and flight operational performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where explicitly required to establish the post-pandemic recovery baseline. Dynamic queuing models and predictive estimation techniques are assessed using standard econometric and machine learning benchmarks, including $p$-values, $R^2$, Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and Mean Absolute Scaled Error (MASE). These delimitations are defined below across four operational dimensions:

* **Geographic Scope**: This study evaluates commercial air traffic and security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications, capturing 67.2% of nationwide domestic flight departures.
* **Temporal Scope**: The longitudinal dataset spans January 1, 2019 through December 31, 2025 ($N = 22,491$ airport-days; 42.06 million conformed fact records). Model training and operational calibration are focused on the verified post-pandemic operational regime starting May 1, 2022 (following the nationwide judicial vacatur of federal transportation mask mandates), reserving the full 12-month calendar year of 2025 (3,222 complex-days) as a strict out-of-time holdout evaluation window.
* **Data Sources**: Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including Transportation Security Administration (TSA) Freedom of Information Act (FOIA) hourly screening logs per physical lane, Bureau of Transportation Statistics (BTS) Airline On-Time Performance (Form 41 Schedule P-5.2), BTS Form 41 Schedule T-100 Domestic Segment Data, and the BTS Origin and Destination Survey (DB1B) 10% ticket sample.
* **Evaluation Standards**: Model comparisons are delimited to the 2025 holdout dataset across three distinct operational regimes: Nominal On-Time Baseline, Routine Daily Operations, and Irregular Operations (IROPS). Evaluation metrics strictly follow scale-free Mean Absolute Scaled Error (MASE), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and the Diebold-Mariano ($DM$) test of predictive accuracy. In accordance with queuing theory principles, Mean Absolute Percentage Error (MAPE) is formally invalidated and excluded due to mathematical instability during near-zero volume curfew hours.

---

# Appendix B: Research Limitations and Methodological Assumptions

> *Note on Thesis Cross-References*: This appendix outlines the operational boundary constraints of public federal datasets and documents the 14-point methodological assumption matrix designed to protect internal and external construct validity. It is referenced in **Chapter I (Introduction)**, Section 1.7 (*Limitations and Assumptions*); in **Chapter III (Methodology)**, Section 3.4 (*Internal Validity Threats and Remediation Protocols*); and in **Chapter V (Discussion)**, Section 5.6 (*Strategic Implications for Airport and Security Authorities (Operational and Methodological Boundaries)*).

## B.1 Operational and Data Source Limitations
## Limitations

These limitations are detailed below:

* Staffing and Lane Configuration Opacity: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
* Connecting Passenger Surveys: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.
* Operational Exogeneity: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234.

## B.2 Internal Validity Threats and Remediation Protocols
### Validity Detail


#### Internal Validity Threats and Remediation Protocols

A primary threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand (the "Hub Disconnect"). To reduce this bias, origin-and-destination survey data (BTS DB1B) and airport-specific O&D ratios are used to estimate and remove connecting traffic from passenger flow calculations, isolating true originating landside checkpoint demand.

## B.3 Methodological Assumptions and Threat Remediation Matrix
To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across the research design. Table B.1 documents these assumptions, their mathematical and operational justifications, and the critical failure modes prevented.

### Table B.1
*Methodological Assumptions and Failure Mode Prevention Matrix*

| Analysis Level | Key Methodological Assumption | Mathematical & Operational Justification | Failure Mode Prevented |
| :--- | :--- | :--- | :--- |
| Terminal Flow | Non-traveler exits are negligible | Gate passes / aborted boardings are << 1% of peak bank volume | Over-parameterized noise modeling; false uncoupling |
| Terminal Flow | Connecting passengers bypass security | Sterile area transfers never enter landside security screening | Throughput paradoxes (e.g., CLT 76% connecting traffic) |
| Terminal Flow | Exclusion of inbound arrivals | Arriving passengers exit directly via one-way sterile exits | Inbound flight ghost demand & spurious correlation |
| Terminal Flow | Exhaustive nationwide departures | Physical screening serves all destinations and carriers | Truncation bias (>50% omitted originating volume) |
| Temporal Coupling | 90–120 min lead time window | Unidirectional pipeline (doors close T - 15; screening T - 100) | Phase-shift misspecification (t <-> t correlation error) |
| Temporal Coupling | Lognormal arrival density kernel | Peak show-up mode approx 92.5 min; discrete weights (0.25, 0.55, 0.20) | Rigid scalar shifts failing to capture human variance |
| Temporal Coupling | Zero lookahead leakage | Models rely strictly on planned pre-departure schedules | Target leakage from realized operational delays |
| Sample Filtering | Top 25 macro power-law cut-off | Captures 67% of NAS volume; Kingman heavy-traffic limit rho -> 1.0 | Light-traffic triviality (rho << 0.3) and low SNR (CV ~ 0.14) |
| Sample Filtering | Micro checkpoint exclusivity | Eliminates cross-carrier collinearity (Corr approx 0.90) | Gram matrix inversion collapse (kappa >> 10^4) |
| Sample Filtering | Meso Big 3 co-location | Identical weather/airspace shock differencing (delta_t - delta_t = 0) | Carrier comparison confounded by regional weather |
| Sample Filtering | Exclusion of Southwest (WN) | Open-seating bimodal arrival distribution (mu_1 approx 135m, mu_2 approx 65m) | Violation of parameter exchangeability (f_j(tau) != f(tau)) |
| Sample Filtering | Post-pandemic May 1, 2022 boundary | Mask mandate repeal; network aggregate stability | Localized leisure vs. business recovery distortions |
| Evaluation | Orthogonal 4 x 4 factorial design | Exactly 4 exclusive checkpoints per carrier across 4 clusters | Unbalanced ANOVA variance inflation |
| Evaluation | Twin TRACON disruption controls | Matched weather shocks (EWR T-C vs. LGA T-C) | Localized convective bias in resilience / TTR testing |

*Note.* Adapted from `figures/04_Appendix_and_Reference/methodological_assumptions.csv`. Complete methodological and operational assumption framework governing the research design.

---

# Appendix C: Connecting Queuing Principles to Dynamic Lane Staffing and Safety Cushion

> *Note on Thesis Cross-References*: This appendix connects heavy-traffic queuing theory with practical checkpoint lane dimensioning rules and the Staffing Safety Cushion. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.2 (*Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation*); and in **Chapter V (Discussion)**, Section 5.6 (*Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion*).

## C.1 Connecting Queuing Principles to Dynamic Lane Staffing
### Connecting Queuing Principles to Dynamic Lane Staffing

A primary contribution of this thesis is bridging theoretical queuing theory with practical checkpoint lane allocation:

* The Checkpoint Tipping Point (Kingman's Queuing Law): In heavy-traffic queuing theory (Kingman, 1961), expected passenger waiting time ( $Wq$ ) does not increase in a smooth, straight line. Rather, it follows a non-linear curve:
where $ρ=λcμ$ is checkpoint lane utilization and $Ca2$ is passenger arrival volatility. When screening lanes operate near capacity ( $ρ≥0.85–0.90$ ), the multiplier $ρ1-ρ$ grows exponentially. Even a modest burst of arriving passengers ( $Ca2$ ) instantly tips the checkpoint into a runaway queue backlog.

* The Dynamic Staffing Safety Cushion: Under traditional deterministic staffing, security lanes are opened based solely on expected average volume ( $μt$ ). During flight departure waves, this guarantees that arrival surges push utilization past $ρ=0.90$ , triggering queue spikes.
To solve this, airport checkpoint administrators can translate predicted throughput volatility ( $σTSA,t$ ) directly into risk-buffered lane configurations using conformal prediction principles:

where $μlane$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $zq$ is the coverage quantile factor ( $z0.85=1.036$ for an 85% service guarantee). By adding a dynamic volatility buffer ( $zq⋅σt$ ) to lane scheduling, checkpoint administrators cap utilization at a safe threshold ( $ρt≤0.85$ ), effectively clamping the $ρ1-ρ$ multiplier and preventing exponential wait-time explosions.

---

# Appendix D: Peer-Reviewed Literature Equation Registry and Mathematical Formulations

> *Note on Thesis Cross-References*: This appendix establishes the comprehensive mathematical foundations, queuing theorems, and statistical metric definitions utilized throughout the study. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.1–2.5 (*Comparative Modeling Paradigm Taxonomy for Airport Passenger Screening Throughput*); and in **Chapter III (Methodology)**, Section 3.1 (*Predictive Modeling Frameworks and Baseline Control*).

## D.1 Comprehensive Peer-Reviewed Mathematical Formulations & Queuing Registry

Table D.1 compiles the complete inventory of 20 peer-reviewed mathematical formulations, queuing theory equations, and econometric tests operationalized throughout this thesis.

### Table D.1
*Peer-Reviewed Literature Equations and Statistical Metric Registry*

| Equation ID | Operational Domain | Formal Equation Name | Mathematical Formula | Target Operational Construct | Standard Aviation / Econometric Source | Thesis Operational Context |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| EQ-01 | Stochastic Queuing & Congestion Theory | Kingman's Heavy-Traffic Queuing Approximation (Single-Server) | W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu} | W_q = Mean waiting time in queue; rho = Server utilization (traffic intensity); C_a = Coefficient of variation of inter-arrival times; C_s = Coefficient of variation of service times; mu = Mean service rate. | Kingman, J. F. C. (1961). The single server queue in heavy traffic. Mathematical Proceedings of the Cambridge Philosophical Society, 57(4), 902–904; Kingman, J. F. C. (1962). On queues in heavy traffic. Journal of the Royal Statistical Society: Series B, 24(2), 383–392. | Establishes the fundamental theoretical queuing foundation of the thesis: checkpoint queues scale quadratically with arrival volatility (C_a^2) as checkpoint utilization approaches capacity (rho -> 1.0), proving why predicting throughput volatility is operationally superior to predicting raw mean volume. |
| EQ-02 | Stochastic Queuing & Congestion Theory | Kingman-Whitt Multi-Server Heavy-Traffic Approximation (G/G/s Queue) | W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu} | W_q = Expected queue wait time; s = Number of active parallel screening lanes; rho = Multi-server utilization (lambda / (s*mu)); C_a = Arrival CV; C_s = Service time CV; mu = Lane processing rate. | Whitt, W. (1993). Approximations for the GI/G/m queue. Production and Operations Management, 2(2), 114–161; Marchal, W. G. (1976). An approximate formula for waiting time in GI/G/1. Operations Research, 24(3), 473–474. | Extends Kingman queuing principles to multi-lane airport security screening checkpoints (s parallel lanes), demonstrating buffer depletion under high lane utilization across Top 25 commercial airfields. |
| EQ-03 | Stochastic Queuing & Congestion Theory | Traffic Intensity / Checkpoint Utilization Ratio | \rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu} | rho(t) = Instantaneous traffic intensity at hour t; lambda(t) = Hourly passenger arrival demand rate; c(t) = Number of open screening lanes at hour t; mu = Nominal screening throughput rate per lane (pax/lane-hr). | Kendall, D. G. (1953). Stochastic processes occurring in the theory of queues and their analysis by the method of the imbedded Markov chain. The Annals of Mathematical Statistics, 24(3), 338–354; Erlang, A. K. (1909). | Operationalized in Chapter III Macro Filtering (§3.4): small regional airfields operate at rho << 0.30 (preventing queue formation), whereas Top 25 hubs routinely hit rho -> 1.0 during bank surges (05:00–08:30 and 16:00–18:30). |
| EQ-04 | Passenger Lead-Time & Arrival Curves | Lognormal Passenger Show-Up Lead-Time Distribution | \tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105 \text{ min} | tau = Lead time (minutes before scheduled departure) that ticketed passengers present at security; mu = Log-scale mean; sigma = Log-scale dispersion; E[tau] = Expected show-up lead time (~105 minutes for domestic legacy flights). | Airport Cooperative Research Program (ACRP). (2010). ACRP Report 40: Airport Curbside and Terminal Area Planning. Transportation Research Board, National Academies of Sciences, Engineering, and Medicine. | Governs the empirical lead-lag passenger arrival distribution convolving scheduled flight banks into landside security arrival curves across American Airlines, Delta Air Lines, and United Airlines. |
| EQ-05 | Passenger Lead-Time & Arrival Curves | Gaussian Mixture Bimodal Boarding Arrival Distribution | \tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2) | tau_WN = Southwest passenger arrival lead time; w1 = Weight of boarding position maximizers (~135 min lead time); (1-w1) = Weight of carry-on business travelers (~65 min lead time). | ACRP Report 40 (TRB, 2010); Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Empirically demonstrates that unassigned boarding produces bimodal arrival distributions, justifying Southwest Airlines exclusion under Meso Filtering to prevent passenger show-up heterogeneity. |
| EQ-06 | Operational Accounting & Filtering | Local Originating Passenger Demand Accounting Identity | \text{Demand}_{\text{orig}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}}) | Demand_orig,t = True originating passenger demand entering landside screening at hour t; Seats_f = Aircraft seat capacity for flight f; LoadFactor_f = Route-level passenger load factor; ConnectingRatio = Quarterly airport connecting percentage from DB1B. | Bureau of Transportation Statistics (BTS). (2024). Form 41 Schedule T-100 Segment Data and DB1B Airline Origin and Destination Survey. U.S. Department of Transportation. | Resolves the Hub Disconnect: subtracts transferring passengers who never enter landside security queues, increasing explained schedule-to-checkpoint variance from 20.9% to 44.9% across the Top 25 airfields. |
| EQ-07 | Passenger Lead-Time & Arrival Curves | Discrete Empirical Lead-Time Convolution (Finite Impulse Response) | \text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right] | w_h = Empirical ACRP arrival weights: w_1 (t+1 hr lead) = 0.52, w_2 (t+2 hr lead) = 0.38, w_3 (t+3 hr lead) = 0.10, where sum(w_h) = 1.0; F_{t+h} = Set of scheduled departures at hours t+1, t+2, t+3. | ACRP Report 40 (TRB, 2010); Oppenheim, A. V., & Schafer, R. W. (2009). Discrete-Time Signal Processing (3rd ed.). Prentice Hall. | The physical operational engine of Model 1 (Deterministic Flight Schedule Model), convolving scheduled departure banks into landside arrival hours to forecast baseline passenger demand. |
| EQ-08 | Statistical Moments & Volatility Targets | Intraday Diurnal Absolute Volume Volatility (Dispersion) | \sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2} | sigma_TSA,hr(d) = Diurnal standard deviation of hourly passenger screening throughput on day d (pax/hr); y_{d,h} = Hourly TSA throughput at hour h; y_bar_d = Daily mean hourly throughput. | Pearson, K. (1894). Contributions to the mathematical theory of evolution. Philosophical Transactions of the Royal Society of London, 185, 71–110. | Primary dependent modeling target 1: captures within-day absolute demand dispersion across the 24 hours of each day (in pax/hr), isolating bank surge amplitudes. |
| EQ-09 | Statistical Moments & Volatility Targets | Intraday Scale-Free Relative Arrival Volatility (Coefficient of Variation) | CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}} | CV_TSA,hr = Dimensionless ratio of hourly standard deviation to daily mean throughput. | Pearson, K. (1895). Notes on regression and inheritance in the case of two parents. Proceedings of the Royal Society of London, 58, 240–242. | Primary dependent modeling target 2: removes facility baseline scale to quantify pure arrival burstiness and queue surge spikiness across different checkpoint geometries. |
| EQ-10 | Statistical Moments & Volatility Targets | Multi-Day Temporal Rolling Volatility | \sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2} | sigma_TSA,7d(d) = Rolling 7-day standard deviation of daily passenger volume (pax/day); Y_{d-k} = Total daily throughput on day d-k; Y_bar_7d = 7-day rolling mean daily throughput. | Box, G. E., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time Series Analysis: Forecasting and Control (5th ed.). John Wiley & Sons. | Primary dependent modeling target 3: captures medium-term multi-day network turbulence caused by severe winter storm systems, convective ground delay programs, and cancellation cascades. |
| EQ-11 | Statistical Moments & Volatility Targets | Daily Flight Departure Delay Dispersion | \sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2} | sigma_Delay,d = Sample standard deviation of flight departure delays across all uncancelled domestic departures on day d (minutes); DepDelay_i = Actual minus scheduled departure time for flight i; N_d = Total domestic departures. | Standard sample variance; Bureau of Transportation Statistics (BTS). (2024). Airline On-Time Performance Data Technical Reporting Directives. | Primary airside explanatory volatility metric: exhibits strong operational coupling with landside checkpoint arrival volatility (r = +0.4373, p < 0.05), while raw delay minutes show zero correlation (r = -0.062). |
| EQ-12 | Time-Series Forecasting & Error Metrics | Root Mean Squared Error (RMSE) | \text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (y_t - \hat{y}_t)^2} | RMSE = Quadratic loss forecast error (pax/hr); y_t = Actual observed volatility; y_hat_t = Model-predicted volatility; N = Sample evaluation hours. | Standard quadratic loss metric in statistical estimation and econometric forecasting. | Governing absolute error metric for Dimension 1 (Robustness): Model 3 achieves lowest RMSE (222.1 pax/hr) on the 2025 holdout dataset (-91.3 pax/hr vs Model 1). |
| EQ-13 | Time-Series Forecasting & Error Metrics | Mean Absolute Error (MAE) | \text{MAE} = \frac{1}{N} \sum_{t=1}^N \|y_t - \hat{y}_t\| | MAE = Linear loss forecast error (pax/hr); absolute difference between observed and predicted values. | Standard linear loss metric in time-series forecasting and regression. | Measures typical magnitude of point forecast errors without quadratic penalty for outliers; Model 3 achieves 142.8 pax/hr across dedicated screening complexes. |
| EQ-14 | Time-Series Forecasting & Error Metrics | Mean Forecast Bias (Directional Systematic Error) | \text{Bias} = \frac{1}{N} \sum_{t=1}^N (\hat{y}_t - y_t) | Bias = Mean directional error (pax/hr); negative values indicate systematic under-prediction; positive values indicate over-prediction. | Standard forecast bias metric in operations research and inventory management. | Evaluates systematic under-prediction during bank surges: Model 1 displays -42.1 pax/hr bias; Model 2 exhibits -18.4 pax/hr; Model 3 maintains near-zero bias (-8.5 pax/hr). |
| EQ-15 | Time-Series Forecasting & Error Metrics | Mean Absolute Scaled Error (MASE) | \text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N \|y_t - \hat{y}_t\|}{\frac{1}{N-24}\sum_{t=25}^N \|y_t - y_{t-24}\|} | MASE = Scale-free relative forecast accuracy metric; numerator is candidate model MAE; denominator is in-sample mean absolute error of 24-hour diurnal naive persistence control. | Hyndman, R. J., & Koehler, A. B. (2006). Another look at measures of forecast accuracy. International Journal of Forecasting, 22(4), 679–688. | Primary scale-free benchmark metric across all models and regimes: Baseline Control is calibrated at MASE = 1.000; Model 2 achieves MASE = 0.779; Model 3 achieves champion MASE = 0.662. |
| EQ-16 | Hypothesis & Significance Testing | Diebold-Mariano Test Statistic for Equal Predictive Accuracy | DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d}) / N}} \sim \mathcal{N}(0, 1) | d_t = e_{1,t}^2 - e_{2,t}^2 (Loss differential at time t); d_bar = Sample mean loss differential; Var_hat(d_bar) = Asymptotic long-run variance of loss differential. | Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. | Formally proves that Model 2 (DM = 42.15, p < 0.0001) and Model 3 (DM = 48.72, p < 0.0001) error reductions over Model 1 are genuine statistical improvements rather than random chance. |
| EQ-17 | Hypothesis & Significance Testing | Chow Test Statistic for Structural Breaks in Linear Regressions | F = \frac{(RSS_C - (RSS_1 + RSS_2)) / k}{(RSS_1 + RSS_2) / (N_1 + N_2 - 2k)} \sim F(k, N_1 + N_2 - 2k) | RSS_C = Residual sum of squares of pooled model; RSS_1, RSS_2 = Residual sums of squares of pre- and post-break sub-periods; k = Number of parameters; N_1, N_2 = Sample sizes. | Chow, G. C. (1960). Tests of equality between sets of coefficients in two linear regressions. Econometrica, 28(3), 591–605. | Statistically justified the Candidate B temporal demarcation point (May 1, 2022 post-mask mandate): Chow test confirms structural stability (p >= 0.15) for the post-mandate modern operational regime. |
| EQ-18 | Hypothesis & Significance Testing | CUSUM Test for Structural Parameter Stability | W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w} | W_t = Cumulative sum of standardized recursive residuals w_r; sigma_hat_w = Sample standard deviation of recursive residuals; k = Number of regression regressors. | Brown, R. L., Durbin, J., & Evans, J. M. (1975). Techniques for testing the constancy of regression relationships over time. Journal of the Royal Statistical Society: Series B, 37(2), 149–163. | Demonstrates that cumulative recursive residuals stay strictly within the 95% confidence bands from May 2022 through Dec 2025, validating model training data integrity. |
| EQ-19 | Statistical Moments & Volatility Targets | Peak-to-Average Ratio (PAR / Crest Factor) | \text{PAR}_d = \frac{\max_{h \in [0,23]} y_{d,h}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}} | PAR_d = Ratio of maximum hourly throughput on day d to that day's average hourly volume; measures acute demand concentration into a single peak hour. | Standard engineering and operational metrics (Crest Factor / Peak-to-Average Ratio); Oppenheim & Schafer (2009). | Standard literature replacement for S_TSA: identifies days where checkpoint queues experience extreme surge concentration into an acute morning or evening rush hour. |
| EQ-20 | Operational Dimensioning & Staffing | Volatility-Buffered Safety Capacity Lane Dimensioning Rule | c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil | c(t) = Recommended integer number of open screening lanes at hour t; mu_hat_t = Expected hourly passenger arrivals; sigma_hat_t = Forecasted arrival volatility; z_q = Normal service quantile (e.g., 1.645 for 95% service level); mu_lane = Lane throughput capacity (pax/lane-hr). | Erlang, A. K. (1917); Kolesar, P., & Green, L. (1998). Insights on capacity planning using a queuing model. Management Science; Whitt, W. (1992). Understanding the efficiency of multi-server service systems. Management Science, 38(5), 708–723. | Translates volatility forecasts into actionable security checkpoint lane dimensioning in Chapter V (§5.2), proving that buffering for volatility (sigma) prevents heavy-traffic queue collapse under Kingman's formula. |

*Note.* Adapted from `results/manuscript_tables/appendix_standard_literature_equations.csv`. Compiles all 20 formal academic formulations, queuing approximations, capacity identities, error loss functions, and econometric hypothesis tests operationalized in the research design.

---

# Appendix E: Construct Validity and Passenger Throughput Volatility Formulations

> *Note on Thesis Cross-References*: This appendix establishes the formal mathematical definitions of the primary dependent volatility targets and resolves construct validity threats. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.2 (*Volume Versus Volatility & The Values versus Volatility Paradigm*); and in **Chapter III (Methodology)**, Section 3.1 (*Core Research Variables*) and Section 3.4 (*Mathematical Formulation of Volatility Targets*).

## E.1 Establishing Construct Validity: Targets and Formulations
### Establishing Construct Validity

construct validity requires establishing explicit mathematical formulations that measure passenger throughput volatility rather than static volume levels:

1. Intraday Diurnal Absolute Dispersion ( $σTSA, hr$ ).

Measures the absolute dispersion of hourly screening counts across the 24 hours of calendar day $d$ (in passengers per hour):

This target reflects the absolute peak-to-trough amplitude of passenger arrival waves.

2. Intraday Scale-Free Relative Volatility ( $CVTSA, hr$ ).

Normalizes intraday dispersion by average daily throughput:

By removing baseline airport scale, this scale-free metric measures arrival burstiness and queue surge spikiness independent of facility size.

3. Multi-Day Temporal Rolling Volatility ( $σTSA, 7d$ ).

Measures the 7-day rolling standard deviation of daily passenger volume (in passengers per day):

This target captures medium-term multi-day passenger flow turbulence induced by convective storms, winter blizzards, and cascading cancellation shocks.

4. Flight Departure Delay Dispersion and Coupled Volatility.

Systemic queue breakdown is driven by coupled volatility mismatch between landside passenger arrivals and airside flight departures:

* Flight Departure Delay Dispersion: Sample standard deviation of departure delays across uncancelled domestic flights on day $d$ :
* The Coupled Volatility Index: Joint product of landside arrival variation and airside delay dispersion:
* Diurnal Operational Turbulence Shock Index: For each hour $h∈023$ conditioned on Day of Week ( $dow$ ):
Applying 1D K-Means clustering ( $k=3$ ) establishes three operational diurnal regimes: 1_OFF_PEAK ( $T<0.35$ , overnight curfew), 2_MID_PEAK ( $0.35≤T<0.75$ , midday steady flow), and 3_PEAK ( $T≥0.75$ , queuing turbulence).

## E.2 Construct Validity Threats and Operational Formulations
#### Construct Validity Threats and Operational Formulations

Construct validity is affected by checkpoint heterogeneity, as raw lane counts obtained from TSA throughput data combine different screening modes, such as TSA PreCheck, with standard screening lanes, each exhibiting disparate processing rates ( $≈250–300$ pax/lane-hr for PreCheck vs. $≈150–180$ pax/lane-hr for standard). To resolve this heterogeneity threat, the methodology constructs scale-free relative volatility metrics ( $CVTSA$ ) and standardized lane measures rather than unadjusted raw totals.

---

# Appendix F: Candidate Predictive Modeling Suite and Operational Regimes

> *Note on Thesis Cross-References*: This appendix details the mathematical architectures and operational paradigms of the three candidate models and baseline control across the three evaluation dimensions and three operational regimes. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Predictive Modeling Frameworks and Baseline Control*) and Section 3.1 (*Quantitative Evaluation Dimensions and Operational Regimes*).

## F.1 Candidate Predictive Modeling Suite & Operational Architecture
## Model Selection

To evaluate the research questions, the investigation establishes three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:

* The Baseline Control Benchmark (Daily Persistence):
* Operational Logic: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the exact same hour yesterday ( $Vol^t=Volt-24$ ).
* Evaluation Role: Serves as the non-parametric reference standard ( $MASE≡1.000$ ). Any operational model worth deploying must prove that it beats this simple historical benchmark.
* Model 1: Deterministic Flight Schedule Model (Operational Baseline):
* Operational Logic: Uses published airline flight schedules, shifted forward in time using empirical passenger show-up distributions from ACRP Report 40 (Airport Passenger Terminal Planning and Design).
* Mechanics: Because passengers arrive 90 to 120 minutes before takeoff, scheduled flight departure banks are convolved across lead arrival horizons ( $t+1,t+2,t+3$ ). This captures the operational ebb and flow of scheduled flight waves without requiring real-time delay telemetry or statistical machine learning.
* Model 2: Supervised Machine Learning Model (Flight Operations & Delays):
* Operational Logic: Uses an automated decision-tree algorithm trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features.
* Mechanics: The decision trees learn non-linear operational rules (e.g., how departure delays, tactical cancellations, and surface taxi queues ripple into checkpoint arrival dispersion). It tests whether airside operational data improves checkpoint forecasts over flight schedules alone.
* Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback):
* Operational Logic: Combines the structured foundation of airline flight schedules with live real-time feedback from the checkpoint floor.
* Mechanics:
* Stage 1: Captures recurring daily and weekly flight schedule cycles.
* Stage 2: A decision tree predicts residual volatility shocks caused by flight delays and weather ground stops, dynamically incorporating live 1-step error feedback from the previous hour ( $et-1=yt-1-yt-1$ ). If lines are longer than the flight schedule predicted, the model immediately adjusts upward to track stranded passengers.

## Quantitative Evaluation Dimensions and Operational Regimes.

Airport operations are structured into a three-tier operational taxonomy:

* Tier 1: Nominal On-Time Baseline: Departure delays <15 minutes and zero tactical cancellations (N_cancels =0). Grounded in the FAA/DOT A14 regulatory reference benchmark, this state serves as an experimental control to observe pure passenger show-up curves without airside delay distortion.
* Tier 2: Routine Daily Operations: Everyday commercial hub reality, characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.
* Tier 3: Irregular Operations (IROPS): Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays ≥45 minutes or tactical cancellations ≥5.

---

# Appendix G: Temporal Scope, Post-Pandemic Demarcation, and COVID-19 Boundary Definition

> *Note on Thesis Cross-References*: This appendix establishes the empirical justification for excluding pandemic-period volatility and documents the post-pandemic demarcation and partitioning design. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Temporal Scope and Boundary Definition*) and Section 3.1 (*Dataset Partitioning and Validation Protocol*); and in **Chapter IV (Results)**, Section 4.2 (*Temporal Boundaries*).

## G.1 Temporal Scope and Boundary Definition
### Temporal Scope and Boundary Definition

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic operational volatility induced by the COVID-19 pandemic (Sun et al., 2021; Gao, 2022). While a baseline 'post-pandemic' operational era is provisionally considered as beginning January 1, 2023, an exploratory analysis is performed during data preprocessing to refine this demarcation due to varying definitions of ‘post-pandemic’ (ICAO, 2024; Centre for Aviation, 2025).

This preprocessing step evaluates pre-pandemic baseline patterns against longitudinal 2019–2025 data to pinpoint the empirical inflection point where system throughput and schedule deviations returned to steady-state normalization. Structural break tests, rolling Welch's t-tests, and CUSUM analyses identified May 1, 2022 (Candidate B demarcation) as the empirical inflection point, coinciding with the vacatur of the federal transit mask mandate and the rebound of airline load factors to 84.7%, matching pre-pandemic baselines. Restricting the active dataset to this verified window enables the forecasting models to capture contemporary queue dynamics and schedule-driven variability without being skewed by transient historic anomalies.

## G.2 Partitioning Design and Post-Pandemic Demarcation Verification
### Temporal boundaries- covid, partitioning design

The selected temporal boundary establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations; 215,562 facility-level observations). A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.


### Post pandemic temporal demarcation

Table 4.4b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

Across the annual calendar, delay dispersion ( $σDelay$ ) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed to track carrier ticket boarding, a absence of carrier flights, a cross-carrier throughput, and a test for terminal layout. For more details, please see the appendix.

---

# Appendix H: Archival Data Storage Infrastructure, Directory Hierarchy, and Screenshot Catalog

> *Note on Thesis Cross-References*: This appendix documents the persistent cloud storage backup manifest, repository organization, and visual evidence screenshot catalog. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Apparatus and Materials: Archival Storage and Reproducibility Environment*) and Section 3.3 (*Sources of Data*).

## H.1 Archival Data Storage Infrastructure and Persistent Cloud Repository

To ensure full auditability, scientific reproducibility, and long-term data preservation, the master raw and conformed aviation datasets are archived in a standardized directory hierarchy replicated across secure persistent cloud storage (OneDrive) and local data warehouse paths. Table H.1 documents the backup structure and directory contents.

### Table H.1
*OneDrive Archival Backup Directory Structure and Repository Manifest*

| Archival Directory Path | Hierarchy Level | Description and Preserved Contents |
| :--- | :--- | :--- |
| OneDrive-Backups/ | Root | Root backup archive directory |
| OneDrive-Backups/00_FOLDER_INDEX.txt | Level 1 | Plaintext reference guide and manifest |
| OneDrive-Backups/01_Datasets/ | Level 1 | Raw and source aviation datasets |
| OneDrive-Backups/01_Datasets/BTS_Flight_Data/ | Level 2 | BTS flight & delay datasets |
| OneDrive-Backups/01_Datasets/TSA_Throughput_Data/ | Level 2 | TSA throughput PDFs & passenger CSVs |
| OneDrive-Backups/01_Datasets/Aviation_DB1C_Data/ | Level 2 | Air passenger O&D survey datasets |
| OneDrive-Backups/01_Datasets/Other_Raw_Datasets/ | Level 2 | General raw data tables |
| OneDrive-Backups/02_Processed_SSOT/ | Level 1 | Master Single Source of Truth CSVs |
| OneDrive-Backups/03_Projects_and_Code/ | Level 1 | Development code scripts and version control |
| OneDrive-Backups/03_Projects_and_Code/Python_and_ETL/ | Level 2 | Python scripts (.py) & notebooks (.ipynb) |
| OneDrive-Backups/03_Projects_and_Code/Git_Repositories/ | Level 2 | Git repositories & codebase snapshots |
| OneDrive-Backups/04_System_and_ISOs/ | Level 1 | Windows installation ISOs & VM images |
| OneDrive-Backups/05_Archives/ | Level 1 | Zip snapshots & historical backup archives |

*Note.* Adapted from `figures/04_Appendix_and_Reference/backups_organization.csv`. Directory manifest establishing repository backup protocols and persistent cloud storage organization.

Figure H.1 and Figure H.2 document the backup organization and directory structure of the visual evidence screenshots.

Figure H.1  
*Archival Data Storage and OneDrive Directory Organization*

![Figure H.1: Archival Data Storage and OneDrive Directory Organization](../../figures/04_Appendix_and_Reference/Backups%20organization.png)

*Note.* Folder tree structure of the persistent cloud storage backup repository.

---

## H.2 Visual Evidence Screenshot Catalog

Figure H.2 illustrates the organization of the 30 high-resolution visual evidence screenshots across the four analytical subdirectories.

Figure H.2  
*Diagrams and Screenshot Layout Structure*

![Figure H.2: Diagrams and Screenshot Layout Structure](../../figures/04_Appendix_and_Reference/Diagrams%20and%20Screenshot%20Layout.png)

*Note.* Directory organization and chapter mapping for the 30 visual evidence screenshots across the thesis repository.

---

# Appendix I: Four-Tier Purposive Filtering Pipeline Architecture and Progression

> *Note on Thesis Cross-References*: This appendix details the progressive multi-phase filtering architecture that isolates dedicated single-carrier screening facilities from confounding network interactions. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Sample: Four-Tiered Purposive Filtering Pipeline*); and in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection*).

## I.1 Four-Tier Purposive Filtering Pipeline Rationale
### 4 Tier Filter Pipeline Detail

Phase 1: Macro Filter (Scale and Congestion). Filters the national candidate universe of 450+ commercial airfields down to the Top 25 airfields. Enforces queue intensity $ρt→1.0$ during departure banks, captures 67.2% of nationwide domestic flight movements, and yields a baseline correlation of $r=0.4572$ ( $R2=20.90%$ ) between raw flights and TSA throughput.

Phase 2: Meso Filter (Symmetry and Invariance). Narrows the Top 25 airfields to 14 candidate hubs requiring concurrent American Airlines, Delta Air Lines, and United Airlines mainline presence (>10% seat share) while excluding Southwest bimodal arrival mixtures and ultra-low-cost carrier volatility. Scheduled flight coupling strengthens to $r=0.5015$ ( $R2=25.15%$ ).

Phase 3: Micro Filter (Checkpoint Exclusivity). Filters the 14 candidate airfields to nine selected hubs with strict dedicated terminal checkpoints ( $PCarrier=j*∣Checkpoint=1$ ), eliminating shared-terminal carrier collinearity ( $κ<25$ ). Checkpoint coupling rises to $r=0.5453$ ( $R2=29.74%$ ) for raw movements and $r=0.6466$ ( $R2=41.81%$ ) when adjusted for DB1B local originating passengers.

Phase 4: Balanced Experimental Cohort (Carrier-Cluster Factorial Matrix). Finalizes the balanced nine-airport cohort comprising 12 dedicated screening complexes (exactly four dedicated complexes each for American, Delta, and United) across all four operational cluster archetypes, achieving dedicated checkpoint-to-flight coupling of $R2=70.80%$ to $77.40%$ .

Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion).

* Filtering Criteria: Restrict the national candidate universe of 450+ commercial airports to the Top 25 commercial airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* Methodological Justification: In airport queueing dynamics, traffic intensity $ρt=λt/ct⋅μ$ determines queue behavior. At small regional airports, passenger flow is sparse ( $ρt≪0.3$ ), preventing queue accumulation and causing throughput to mirror unconstrained arrivals without boundary friction. In contrast, Top 25 hub airports reach peak-hour saturation ( $ρt→1.0$ ) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue delays and non-linear dynamics required to train and evaluate congestion-aware models.
* TSA-OTP Relationship Evolution: Across the nationwide universe of all commercial airfields, the linear correlation between scheduled flight departures and TSA throughput is low ( $r≈0.35,R2≈12.25%$ ). At the Top 25 macro scale, this relationship strengthens to $r=0.4572$ ( $R2=20.90%$ ) for raw volume, and $r=0.6704$ ( $R2=44.94%$ ) when deflated by DB1B connecting ratios.
Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion).

* Filtering Criteria: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ( $>10%$ market share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* Methodological Justification: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical exogenous airspace conditions ( $δt$ ), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to its passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ( $τ∼Lognormalμσ2,Eτ≈105 min$ ), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ( $μ1≈135 min$ for boarding group maximizers; $μ2≈65 min$ for carry-on business travelers), violating arrival distribution homogeneity.
* TSA-OTP Relationship Evolution: In the 14-airfield Meso cohort, eliminating Southwest and ULCC scheduling volatility elevated the scheduled flight to TSA throughput correlation to $r=0.5015$ ( $R2=25.15%$ ).
Phase 3: Micro Filter (Carrier Checkpoint Exclusivity).

* Filtering Criteria: Require strict single-carrier dedicated screening checkpoint complexes ( $PCarrier=j*∣Checkpoint k=1.0$ ). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* Methodological Justification: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ( $CorrSjSj'≥0.88$ , condition number $κ>104$ ), preventing mathematical separation of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ( $κ<25$ ), directly mapping carrier flight banks to landside checkpoint queues.
* TSA-OTP Relationship Evolution: At the airport-wide level for the 9 selected airfields, scheduled flights versus total TSA passengers achieve $r=0.5453$ ( $R2=29.74%$ ), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r=0.6466$ ( $R2=41.81%$ ). Furthermore, when evaluated at the dedicated checkpoint complex level, carrier-filtered departing seats explain 70.80% to 77.40% ( $R2$ ) of checkpoint throughput variance.
Phase 4: Factorial Cohort (Factorial Matrix Balance).

* Filtering Criteria: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the 9-Airport Experimental Cohort comprising 12 Dedicated Checkpoint Complexes across BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL.
* Methodological Justification: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters, ensuring unconfounded cross-carrier and cross-airport transfer evaluation.
* Crucial Methodological Distinction: These evolving correlations and seasonal dynamics serve exclusively to justify the four-tier filtering rationale and confirm data validity. These relationships and dynamics are not used in training the downstream predictive models, preserving strict econometric separation and preventing data leakage. Furthermore, the analysis at this stage evaluates the 9 selected airports as complete facilities, rather than premature facility checkpoints.

### Table I.1
*Four-Tier Purposive Filtering Pipeline Architecture and Progression Rationale*

| Filtering Tier | Candidate Universe | Inclusion & Exclusion Criteria | Methodological & Queuing Rationale | Threat Remediation Justification | Empirical Filtering Outcome |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Phase 1: Macro Filter** | $N = 450+ \to 25$ Hubs | Top 25 airfields by commercial operations and passenger scale; heavy queuing utilization ($\rho \to 1.0$). | Captures 67.2% of nationwide domestic flight departures; establishes baseline airport-level flight-to-throughput coupling ($r = +0.2871$). | Eliminates small non-hub / regional airfields where zero queuing congestion occurs and Kingman asymptotes do not apply. | **25 candidate airfields retained** for network-wide baseline evaluation. |
| **Phase 2: Meso Filter** | $N = 25 \to 14$ Hubs | Mainline legacy carrier operations across American (AA), Delta (DL), and United (UA); minimum 60% combined seat share; Southwest (WN) exclusion. | Eliminates low-cost point-to-point churn and mixed unassigned concourses; raises flight-to-throughput coupling to $r = +0.4124$. | Removes point-to-point carrier network distortions where show-up curves deviate from standard hub-and-spoke banking. | **14 carrier-hub candidates retained**; preserves balanced network representation. |
| **Phase 3: Micro Filter** | $N = 14 \to 9$ Hubs | Physical terminal layout isolation: single-carrier dedicated security checkpoints ($\ge 85\%$ carrier gate exclusivity). | Completely eliminates shared-terminal multi-carrier collinearity ($\text{Corr}(S_j, S_k) \ge 0.75, \text{VIF} \ge 4.0$); elevates coupling to $r = +0.7104$ (raw) and $r = +0.8412$ (connecting-deflated). | Overcomes the fatal shared-terminal bottleneck where multi-airline schedules overlap in common lobbies. | **9 airfields retained** providing unconfounded single-carrier checkpoint isolation. |
| **Phase 4: Factorial Cohort** | $N = 9$ Hubs / 12 Complexes | Orthogonal $4 \times 4$ factorial experimental design balancing 12 carrier-exclusive complexes across 4 operational cluster archetypes. | Exactly 4 complexes each for AA, DL, and UA; final dedicated checkpoint-to-flight correlation reaches $r = +0.880$ to $+0.940$. | Guarantees zero-shot spatial transfer generalizability and eliminates carrier-specific geographic bias. | **Final 9-Airport Experimental Cohort established** across 12 dedicated carrier facilities. |

*Note.* Adapted from `figures/02_Data_Pipelines_and_Threats/master_funnel_progression.csv` and `figures/01_Sample_and_Airport_Selection/clustering_and_connecting_paradox.csv`. Progression of the purposive sampling architecture from the national air transport system to the final 9-airport experimental cohort.

## I.2 Methodological Foundations of Purposive Filtering
Four-Tiered Purposive Filtering Pipeline

To systematically evaluate forecasting performance across deterministic baselines, probabilistic architectures, and hybrid queueing models, a multi-tiered, purposive sampling framework was employed to select nine target airfields (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL). Candidate airports were filtered according to four sequential operational criteria:

Systemic Scale & Throughput Volume (Macro Filter): Airfields were restricted to the Top 25 commercial airports by annual passenger and flight throughput. This ensures sufficient traffic density, queue formation, and schedule-induced operational friction necessary to evaluate volatility, while excluding erratic low-frequency regional anomalies.

Legacy Carrier Co-Location (Meso Filter): Selected airports were required to maintain continuous, high-frequency scheduled operations for all three major legacy network air carriers: American Airlines, Delta Air Lines, and United Airlines. This establishes competitive operational parity and ensures model comparisons are not biased by carrier-specific network absences.

Causal Identification via Checkpoint Exclusivity (Micro Filter): Checkpoint demand forecasting requires convolving scheduled aircraft seats, load factors, and tactical flight delays into physical passenger arrivals. In shared screening environments, multi-carrier pooling introduces severe latent confounding. Therefore, candidate airports were required to feature physically segregated checkpoints serving an individual carrier exclusively (or near-exclusively).

Orthogonal Factorial Symmetry (Experimental Transfer Filter): The resulting 9-airport cohort establishes a balanced 4x4 experimental design: exactly four dedicated, carrier-exclusive checkpoint environments for each of the three legacy carriers (AA: 4, DL: 4, UA: 4), evenly spanning all four empirical operational clusters (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortress Hubs, and Congested Coastal Originators) and all four terminal physical archetypes (Decentralized, Linear Mega-Concourse, Multi-Terminal Ring, and Satellite). This orthogonal variation is structurally required to evaluate zero-shot Generalizability across diverse spatial configurations.

## I.3 Crucial Methodological Distinction: Filtering Correlations for Validation Only

A crucial methodological principle must be emphasized regarding the flight-to-throughput correlations reported across the four filtering phases:

> **The correlation metrics calculated during the 4-tier filtering pipeline serve strictly as sample validation diagnostics to verify that single-carrier isolation has been econometrically achieved.**  
> **Under NO circumstances are these correlations utilized as model feature weights, regression coefficients, or algorithmic inputs in any downstream forecasting model.**

The candidate models (Baseline Control, Model 1, Model 2, and Model 3) are trained and calibrated strictly on the conformed feature store within the development partition, completely independent of the diagnostic correlations established during sample filtering.

---

# Appendix J: Multi-Source Aviation Data Ingestion and Post-ETL Descriptive Statistics

> *Note on Thesis Cross-References*: This appendix documents the multi-source data feeds, conformed Star Schema staging pipeline, ETL transformations, and descriptive baseline profiles. It is referenced in **Chapter III (Methodology)**, Section 3.3 (*Sources of Data: TSA FOIA, BTS OTP, BTS Form 41 T-100, BTS DB1B*); and in **Chapter IV (Results)**, Section 4.2 (*Descriptive Statistics for Post ETL Data*).

## J.1 Sample Detail and Source Data Profiles
### Sample Detail

TSA FOIA Security Screening Checkpoint Logs

Obtained via Freedom of Information Act (FOIA) disclosures and cross-referenced with public archival repositories, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

BTS On-Time Flight Performance

Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

BTS Form 41 Schedule T-100 Domestic Segment Data

Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

BTS Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), supplemented by authorized monthly airport traffic reports (such as LAX Air Traffic Statistics). These feeds are utilized to extract quarterly connecting passenger ratios across airport pairs to support originating passenger flow estimation.

### Table J.1
*Master Multi-Source Aviation Data Foundation Census & Base Feed Profiles*

| Metric / Characteristic | TSA FOIA Checkpoint Logs (TSA-V0) | BTS Flight Performance (OTP-V0) | BTS T-100 Segment Data (T100-V0) |
| :--- | :--- | :--- | :--- |
| File Size on Disk | 542 MB | 6.5 GB | 81 MB |
| Total Record Count | 19,500,286 | 45,777,091 | 1,945,451 |
| Schema Column Count | 7 columns | 39 columns | 11 columns |
| Temporal Coverage | Jan 1, 2019 – Jun 13, 2026 | Jan 1, 2019 – Dec 31, 2025 | Jan 1, 2019 – May 31, 2026 |
| Distinct Time Units | 2,721 days (65,304 hrs) | 2,557 days (7 full years) | 89 calendar months |
| Distinct Airports | 460 airports | 376 airports | 518 airports |
| Distinct Airlines | — (All screened pax) | 21 carriers | 18 carriers |
| Distinct Aircraft | — | 7,617 tail numbers | 40 aircraft models |
| Primary Unit of Analysis | Hourly Checkpoint Lane | Individual Flight Leg | Monthly Route Segment |
| Data Health / Nulls | 0.00% Nulls | 0.00% Key Nulls | 0.00% Nulls |

*Note.* Adapted from `figures/04_Appendix_and_Reference/database_profiles.csv`. Summary census of upstream raw ingested records versus cleaned conformed records preserved in the research warehouse.

## J.2 Conformed Feature Store Parquet Dataset Breakdown
Table J.2 provides the architectural breakdown of the conformed feature store stored in Apache Parquet format.

### Table J.2
*Conformed Feature Store Parquet Dataset Breakdown*

| Dataset / File | Analytical Grain | Record Count (Rows) | Attribute Count (Columns) | Parquet Compressed Size | In-Memory Arrow Footprint | Primary Operational Purpose |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| otpv1.parquet | Individual Flight Leg | 8,351,307 | 37 | 166.2 MB | ~750 MB | Deduplicated BTS flight records with zero key nulls. |
| tsav1.parquet | Checkpoint Hour | 6,880,725 | 7 | 31.6 MB | ~110 MB | Cleaned TSA hourly screening throughput. |
| db1v1.parquet | Ticket Coupon Sample | 12,910,384 | 10 | 35.1 MB | ~320 MB | 10% ticket survey used to calibrate connecting ratios. |
| t100v1.parquet | Route Month | 269,895 | 11 | 2.2 MB | ~12 MB | Carrier route segment capacity with clamped load factors. |
| warehouse.duckdb | Feature Store Views & DDL | — | — | 3.3 MB | — | Precomputed relational schemas and views. |
| Dimensions (dimensions/) | Lookup tables (CSV) | — | — | 0.34 MB | — | Conformed star schema dimensions (airport, airline, date, time). |
| Total Feature Store Records | — | 28,412,311 | — | ~246.5 MB | ~1.2 GB | Precomputed lead-lag demand view vw_airport_hourly_demand contains 1,494,570 convolved records. |

*Note.* Adapted from `figures/04_Appendix_and_Reference/dataset_breakdown.csv`. Architectural specifications of conformed analytics tables stored in Apache Parquet format.

## J.3 BTS Data Source Detail and Post-ETL Descriptive Statistics
### Data source detail

* TSA FOIA Checkpoint Logs: Hourly passenger throughput records disaggregated by physical screening lane.
* Bureau of Transportation Statistics (BTS) On-Time Performance (OTP, Form 234): Flight-level departure movements tracking scheduled and actual departure times, tarmac taxi-out durations, departure delays, cancellations, and causal delay attributions.
* BTS Form 41 Schedule T-100 Domestic Segment Data: Monthly carrier-route-equipment records reporting available departing seats, transported revenue passengers, and load factors.
* BTS DB1B / DB1C Origin-Destination Ticket Surveys: A 10% randomized sample of airline passenger itineraries detailing coupon routes, connecting transfer ratios, and true local originating passenger fractions.

### Descriptive Statistics for Post ETL Data

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures (σ=69,376; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually (σ=27.76M ; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period. (Refer to appendix for data filtering and quality assurance protocols).

## J.4 Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy
Table J.3 summarizes the 3-tier hierarchy of the BTS DB1B origin-destination ticket survey.

### Table J.3
*Bureau of Transportation Statistics DB1B Ticket Survey Data Hierarchy*

| BTS Table Level | Table Acronym | Analytical Unit / Grain | Itinerary Representation | Thesis Operational Utility |
| :--- | :--- | :--- | :--- | :--- |
| 1. DB1BTicket | DB1BTicket | Whole Itinerary | 1 row for the entire round-trip ticket purchase ($520 total fare, 2 round-trip components). | Yes (all legs) |
| 2. DB1BMarket | DB1BMarket | Directional Market (O&D) | 2 rows: Outbound Market (BOS -> LAX) and Return Market (LAX -> BOS). | Yes (a market can combine 2+ connecting flight legs) |
| 3. DB1BCoupon (DB1C) | DB1BCoupon | Individual Flight Segment | 3 rows (physical takeoff-to-landing flight legs): Leg 1: BOS -> ORD; Leg 2: ORD -> LAX; Leg 3: LAX -> BOS | No (pure single nonstop flight segments) |

*Note.* Adapted from `figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv`. Bureau of Transportation Statistics 10% ticket coupon survey relational hierarchy.

## J.5 Dataset Parameters
### Dataset Parameters

* Evaluation Period: January 1, 2025 to December 31, 2025 (12 continuous months; 3,222 test airport-days; 72,053 complex-level screening hours).
* Primary Target: Diurnal Throughput Volatility ( $σTSA, hr$ , measured in passengers per hour dispersion across the 24 hours of day $d$ ) and Scale-Free Relative Volatility ( $CVTSA, hr=σ/μ$ ).

---

# Appendix K: Treatment of Data: Extract, Transform, Load (ETL) Architecture and Hygiene Protocols

> *Note on Thesis Cross-References*: This appendix details the 8-step Extract protocol, 15-step Transform protocol, 3-step Load protocol, spatial entity resolution, structural zero preservation, and flight cancellation handling. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Treatment of Data: Extract, Transform, Load*) and Section 3.5 (*Data Hygiene Protocols*); and in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection*).

## K.1 Sequential Extract, Transform, Load (ETL) Pipeline Architecture
### Treatment of Data: ETL Detail

The execution of data preparation follows a rigorous, sequential Extract, Transform, Load (ETL) pipeline designed to ingest, clean, standardize, and align the aviation datasets:


#### Extract

* Download TSA Throughput files from the FOIA reading room (PDFs) spanning 2019 to 2026.
* Parse PDFs into standardized tabular format (CSV).
* Download TSA Throughput PDFs and CSVs (2022–2025) from public repository archives (e.g., ).
* Cross-reference TSA datapoints to identify temporal gaps, duplicates, and reporting inconsistencies.
* Download On-Time Flight Performance data (CSVs) spanning 2019 to 2026 for all domestic flights in the United States.
* Download BTS Form 41 Schedule T-100 Segment Airline Traffic Data and calculate monthly route load factors.
* Download BTS DB1B ticket survey coupon files and airport-specific origin-and-destination summary statistics.
* Perform an audit across the 7-year sequence to identify missing data and reporting discontinuities.

#### Transform

* Standardize timestamps across all feeds to a uniform operational clock (local airport solar operational time).
* Map and resolve typographical errors, airport names, data mismatches, and checkpoint naming variations.
* Normalize airport codes, checkpoint prefixes, and common terms (e.g., Checkpoint $→$ CKPT).
* Spatial entity resolution: Map upstream corrupted airport strings; assign unidentifiable strings to a dedicated null surrogate key (airportId = 0, airportMissing = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport."
* Preserve scheduled checkpoint closures: 98.6% of zero-volume records occur between 00:00 and 03:59 local time during scheduled overnight curfews. Rather than applying artificial smoothing or spline imputations, these intervals are preserved as true operational structural zeros.
* Information causality and cancellation handling: Purge advance cancellations (>24 hours prior) from departing seat supply curves, while retaining tactical cancellations (<2 hours prior), reflecting the operational reality that booked passengers had already completed landside security screening before the flight was cancelled.
* Separate scheduled flights from actual operated flights to distinguish planned bank structures from tactical executions.
* Estimate aircraft seat capacities using flight distance, carrier identity, and aircraft equipment/tail-number characteristics.
* Scale seat counts using route-level load factor data to estimate departing passenger volume.
* Merge datasets to determine terminal-specific connecting passengers within target complexes using DB1B ticket survey deflators.
* Empirical passenger show-up curve convolution: Convolve scheduled flight departure banks across empirical lead-time distributions ( $t+1,t+2,t+3$ from ACRP Report 40) and align them with hourly TSA throughput intervals to produce the final conformed modeling dataset.
* Construct the Values versus Volatility feature representation space:
* Feature Values (Levels, 14 Attributes): Schedule Scale (sched_daily_total, actual_daily_total, sched_hourly_mean, sched_rolling_7d_mean), Cancellations (daily_cancellations, daily_cancel_rate, cancel_rolling_7d_mean, cancel_rate_rolling_7d_mean), Delays (avg_dep_delay_minutes, flights_delayed_15min_pct), Surface Queues (avg_taxi_out_minutes), and Network Buffers (aircraft_gauge_seats, route_load_factor_pct, connecting_passenger_share_pct).
* Feature Volatilities (Dispersion, 10 Attributes): Schedule Dispersion (sched_hourly_std, sched_hourly_cv, actual_hourly_std, actual_hourly_cv, sched_rolling_7d_std, sched_rolling_7d_cv), Cancellation Dispersion (cancel_rolling_7d_std, cancel_rate_rolling_7d_std, otp_cancellation_volatility_cv), and Delay Dispersion (otp_departure_delay_volatility_cv).
* Combined Dual Paradigm (24 Attributes): Interacts both feature spaces to test predictive complementarity.

#### Load

* Load master conformed data copies to secure persistent cloud storage (OneDrive) and local data warehouse directories.
* Build relational analytics tables, lookup dimensions, and multidimensional interaction grids.
* Automate verification audits for schema validity, referential integrity, and row preservation across the 7-year sequence.

## K.2 Data Hygiene Protocols and Anomaly Remediation
### Data Hygiene Protocols

Three essential data hygiene protocols were established during warehouse staging to guarantee econometric and machine learning validity:

* Spatial Key Resolution and Unidentified Airport Isolation: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (dim_checkpoint). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (airportId = 0, flagged with airportMissing = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce airportMissing = 0 and airportId > 0.
* Scheduled Checkpoint Closures vs. Missing Sensor Data: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p=1.3$ , which naturally accommodates real zero counts without producing impossible negative passenger estimates or requiring artificial data smoothing).
* Advance vs. Tactical Cancellation Causality: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting (the error of using future information that an airport operations manager would not possess in real time), advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.

---

# Appendix L: Statistical Foundation and Derivation of the Diebold-Mariano ($DM$) Test for Predictive Superiority

> *Note on Thesis Cross-References*: This appendix provides the formal mathematical derivations, asymptotic theory, and degrees-of-freedom audits for the statistical significance tests operationalized throughout the thesis. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Dataset Partitioning and Validation Protocol*) and Section 3.1 (*Apparatus and Materials: Evaluation Metric Definition*); and in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*).

## L.1 The Methodological Dilemma: Why a Standard $p$-Value from a Paired $t$-Test Fails in Time-Series Forecasting

A frequent question encountered in applied statistics and operational forecasting is: *Why must researchers utilize the Diebold-Mariano test to establish statistical significance rather than simply calculating a standard $p$-value from a paired $t$-test or regression ANOVA?*

To answer this question rigorously, one must first clarify the relationship between hypothesis tests and probability metrics: **a $p$-value is not an independent statistical test; it is the numerical output generated by a specific test statistic.** A researcher cannot report a $p$-value without selecting an underlying test. Therefore, the methodological issue is not whether to report a $p$-value, but rather *which statistical test must be used to calculate a valid, mathematically defensible $p$-value when comparing time-series forecasting models.*

In standard cross-sectional data analysis, researchers routinely evaluate differences in model error using a standard paired Student's $t$-test on the loss differentials ($d_t = L(e_{1,t}) - L(e_{2,t})$). In the context of commercial aviation time series, however, standard paired tests are statistically invalid because they violate the foundational **independent and identically distributed (i.i.d.)** assumption.

### The Autocorrelation Problem in Airport Security Operations
Hourly passenger throughput at Transportation Security Administration (TSA) security checkpoints and its associated volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) are characterized by strong **serial autocorrelation**:
1. **Diurnal Schedule Waves**: Airlines coordinate departure banks in tightly synchronized waves (e.g., morning 06:00–08:30 and afternoon 16:00–18:30). If a predictive model underpredicts passenger arrivals at 07:00, the physical accumulation of queuing passengers and lingering terminal lobby congestion ensures that the model's error at 08:00 is not independent of its error at 07:00.
2. **Propagating Flight Delays**: During convective weather disruptions or Air Traffic Control (ATC) ground delay programs, departure delays cascade across connecting aircraft turnarounds throughout the operating day. Consequently, forecast errors exhibit persistent temporal dependency over multi-hour operational horizons.
3. **Multi-Step Forecast Horizons**: When forecasting over an $h$-step horizon ($h > 1$), forecast errors are mathematically guaranteed to follow at least a moving average process of order $h - 1$ ($\text{MA}(h-1)$), directly violating the independence assumption of classical tests.

### The Spurious Statistical Significance Hazard
When standard paired $t$-tests are applied to positively autocorrelated loss differentials, the standard sample variance formula:

$$\widehat{\text{Var}}_{\text{iid}}(\bar{d}) = \frac{s_d^2}{N} = \frac{\frac{1}{N-1}\sum_{t=1}^N (d_t - \bar{d})^2}{N}$$

**severely underestimates the true variance of the mean loss differential.** Because the standard error in the denominator is artificially deflated, the resulting test statistic ($t = \bar{d} / \text{SE}$) is artificially inflated. Consequently, the resulting textbook $p$-value collapses toward zero, producing **spurious statistical significance** (a massive escalation in Type I error rates). A standard paired $t$-test will routinely declare minor, random fluctuations between two models to be "statistically significant at $p < 0.001$" simply because it fails to account for temporal persistence in the underlying flight data.

Furthermore, airport passenger volumes display pronounced **heteroskedasticity** (variance during midday and evening peaks is orders of magnitude greater than variance during overnight curfew hours) and non-Gaussian error tails. The **Diebold-Mariano ($DM$) test** (Diebold & Mariano, 1995) was explicitly formulated to overcome these exact econometric hurdles.

---

## L.2 Mathematical Derivation and Econometric Architecture of the Diebold-Mariano Test

The Diebold-Mariano procedure tests the null hypothesis that two competing forecasting models possess equal predictive accuracy over a given out-of-time evaluation sample, while explicitly correcting for serial correlation and heteroskedasticity in the forecast error differentials.

### Step 1: Formulation of the Loss Differential Series
Let $y_t$ denote the observed passenger throughput volatility at hour $t$ ($t = 1, 2, \dots, N$). Let $\hat{y}_{1,t}$ and $\hat{y}_{2,t}$ denote the forecasts generated by Model 1 and Model 2, respectively, producing forecast errors:

$$e_{1,t} = y_t - \hat{y}_{1,t}, \quad e_{2,t} = y_t - \hat{y}_{2,t}$$

The operational loss associated with each forecast error is determined by a specified loss function $g(e_t)$. While classical regression assumes quadratic loss ($g(e_t) = e_t^2$), the Diebold-Mariano framework permits arbitrary, asymmetric, or scale-free loss functions, such as linear absolute loss ($g(e_t) = |e_t|$) or scaled error loss:

$$d_t = g(e_{1,t}) - g(e_{2,t})$$

The null hypothesis of equal forecast accuracy is formulated as:

$$H_0: \mathbb{E}[d_t] = 0 \quad \text{versus} \quad H_1: \mathbb{E}[d_t] \neq 0$$

### Step 2: Asymptotic Behavior of the Sample Mean Loss Differential
The sample mean loss differential across the evaluation window of length $N$ is:

$$\bar{d} = \frac{1}{N} \sum_{t=1}^N d_t$$

Under the assumption that the loss differential sequence $\{d_t\}$ is covariance stationary and satisfies standard mixing conditions, the Central Limit Theorem establishes that the normalized mean differential converges asymptotically to a Gaussian distribution:

$$\sqrt{N}(\bar{d} - \mu) \xrightarrow{d} \mathcal{N}(0, 2\pi f_d(0))$$

where $f_d(0)$ represents the spectral density of the loss differential sequence at frequency zero. The quantity $2\pi f_d(0)$ equals the **long-run asymptotic variance** ($\sigma_{LR}^2$), which sums the contemporaneous variance and all autocovariances:

$$\sigma_{LR}^2 = \lim_{N \to \infty} \text{Var}(\sqrt{N} \bar{d}) = \gamma_0 + 2 \sum_{k=1}^{\infty} \gamma_k$$

where $\gamma_k = \text{Cov}(d_t, d_{t-k})$ is the $k$-th order autocovariance of the loss differential.

---

## L.3 Heteroskedasticity and Autocorrelation Consistent (HAC) Long-Run Covariance Estimation

To construct a valid test statistic, the long-run variance $\sigma_{LR}^2$ must be estimated consistently. To ensure mathematical robustness against arbitrary autocorrelation and conditional heteroskedasticity, this research operationalizes the **Newey-West (1987) Bartlett kernel estimator**:

$$\widehat{\sigma}_{LR}^2 = \hat{\gamma}_0 + 2 \sum_{k=1}^{K} w(k, K) \hat{\gamma}_k$$

where the sample autocovariances are computed as:

$$\hat{\gamma}_k = \frac{1}{N} \sum_{t=k+1}^N (d_t - \bar{d})(d_{t-k} - \bar{d})$$

and the Bartlett triangular lag window weights are defined as:

$$w(k, K) = 1 - \frac{k}{K + 1}$$

The bandwidth truncation parameter $K$ is set following the asymptotic rate established by Newey and West:

$$K = \left\lfloor 4 \cdot \left(\frac{N}{100}\right)^{2/9} \right\rfloor$$

### Step 4: The Diebold-Mariano Test Statistic and Exact $p$-Value Calculation
The standardized Diebold-Mariano test statistic is defined as:

$$DM = \frac{\bar{d}}{\sqrt{\frac{\widehat{\sigma}_{LR}^2}{N}}} \xrightarrow{d} \mathcal{N}(0, 1)$$

Under the null hypothesis $H_0$, $DM$ asymptotically follows a standard normal distribution. For a two-tailed test, the **exact, mathematically defensible $p$-value** is calculated directly from the standard normal cumulative distribution function $\Phi(\cdot)$:

$$p = 2 \cdot \left(1 - \Phi(|DM|)\right)$$

If $|DM| > 1.96$, the null hypothesis of equal predictive accuracy is rejected at the $\alpha = 0.05$ significance level ($p < 0.05$).

---

## L.4 Empirical Pairwise Statistical Significance Matrix (2025 Out-of-Time Holdout)

Applying the Diebold-Mariano test across the certified 2025 holdout evaluation dataset ($N = 3,222$ test complex-days) yields the pairwise significance matrix reported in Table L.1.

### Table L.1
*Diebold-Mariano Pairwise Statistical Significance Matrix (2025 Holdout Benchmark)*

| Model Comparison | Baseline Model ($M_A$) | Competing Model ($M_B$) | Evaluation Sample | Diebold-Mariano Stat ($DM$) | $p$-Value | Statistical Conclusion |
| :--- | :--- | :--- | :--- | :---: | :---: | :--- |
| **Model 2 vs. Model 1** | Model 1 (Deterministic) | Model 2 (Machine Learning) | 2025 Holdout (All 9 Hubs) | **42.15** | **< 0.0001** | Reject $H_0$; ML significantly outperforms deterministic schedule. |
| **Model 3 vs. Model 1** | Model 1 (Deterministic) | Model 3 (Dynamic Hybrid) | 2025 Holdout (All 9 Hubs) | **48.72** | **< 0.0001** | Reject $H_0$; Dynamic hybrid significantly outperforms deterministic schedule. |
| **Model 3 vs. Model 2** | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | 2025 Holdout (All 9 Hubs) | **18.94** | **< 0.0001** | Reject $H_0$; Dynamic hybrid significantly outperforms pure ML. |
| **Model 3 vs. Model 2 (IROPS)** | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Shock Regime (Delays $\ge 45$m) | **31.40** | **< 0.0001** | Reject $H_0$; Hybrid decisively prevents ML empty checkpoint collapse. |

*Note.* Adapted from `figures/03_Modeling_and_Evaluation/models_and_tests.csv`. All pairwise tests evaluated under squared error loss ($L(e) = e^2$) with Newey-West HAC covariance correction. Degrees of freedom: $N = 3,222$ complex-days ($77,328$ hourly evaluations). All $p$-values are two-tailed.

---

# Appendix M: Operational Evaluation Metrics and Performance Criteria Interpretation

> *Note on Thesis Cross-References*: This appendix defines the mathematical formulations, Kingman queuing interpretations, and operational floor translations for the primary holdout evaluation metrics, alongside the mathematical invalidation of MAPE. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Quantitative Evaluation Dimensions and Operational Regimes*) and Section 3.1 (*Apparatus and Materials: Evaluation Metric Definition*); and in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*).

## M.1 Evaluation Metrics and Dataset Parameters
### Evaluation Metrics

Models were benchmarked across standard operational metrics: Coefficient of Determination ( $R2$ ), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias.

Power of 9 airports figure

## M.2 Operational Forecasting Metrics and Checkpoint Floor Translations

Evaluating passenger throughput volatility forecasts requires criteria grounded in queuing theory and operational utility. Models were benchmarked across five standard metrics:

1. **Coefficient of Determination ($R^2$)**: Quantifies the proportion of throughput variance explained by the model:
   $$R^2 = 1 - \frac{\sum_{t=1}^N (y_t - \hat{y}_t)^2}{\sum_{t=1}^N (y_t - \bar{y})^2}$$
   In time-series volatility forecasting, $R^2 < 0$ indicates that the model performs worse than the simple sample mean.
2. **Root Mean Squared Error (RMSE; pax/hr)**: Quadratically penalizes large forecast misses:
   $$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{t=1}^N (y_t - \hat{y}_t)^2}$$
   In checkpoint staffing, peak-hour underpredictions cause non-linear queue explosions; RMSE heavily penalizes these severe errors.
3. **Mean Absolute Error (MAE; pax/hr)**: Measures average absolute point accuracy:
   $$\text{MAE} = \frac{1}{N} \sum_{t=1}^N |y_t - \hat{y}_t|$$
4. **Mean Absolute Scaled Error (MASE)**: Compares forecast errors against the non-parametric diurnal persistence baseline:
   $$\text{MASE} = \frac{\frac{1}{N} \sum_{t=1}^N |y_t - \hat{y}_t|}{\frac{1}{N - 24} \sum_{t=25}^N |y_t - y_{t-24}|}$$
   $\text{MASE} < 1.00$ proves that the predictive model provides value-add skill beyond naive persistence; $\text{MASE} \ge 1.00$ indicates that deploying the model offers zero operational benefit.
5. **Mean Forecast Bias**: Measures systematic over- or under-prediction ($\text{Bias} = \frac{1}{N} \sum (y_t - \hat{y}_t)$). Negative bias indicates systematic overstaffing (wasted labor costs); positive bias indicates systematic understaffing (long passenger wait times).

---

## M.3 Methodological Invalidation of Mean Absolute Percentage Error (MAPE)

A critical methodological contribution of this research is the **formal mathematical invalidation of Mean Absolute Percentage Error (MAPE) in airport checkpoint demand forecasting**:

$$\text{MAPE} = \frac{1}{N} \sum_{t=1}^N \left| \frac{y_t - \hat{y}_t}{y_t} \right| \cdot 100\%$$

During overnight curfew hours (00:00 to 03:59), observed passenger throughput ($y_t$) approaches zero ($y_t \approx 0$). In these intervals, even minor forecast errors (e.g., predicting 5 passengers when 1 passenger arrives) produce astronomical percentage errors ($|1 - 5| / 1 = 400\%$). If an overnight hour records zero passengers ($y_t = 0$), MAPE is mathematically undefined (division by zero).

Reporting MAPE in airport operations produces severely distorted error statistics that reflect overnight division artifacts rather than operational forecasting skill. Mean Absolute Scaled Error (MASE) completely overcomes this deficiency by scaling against the daily persistence benchmark, providing a stable, non-parametric metric that remains fully defined across all operational hours.

---

# Appendix N: Feature Engineering Pipeline Details and Empirical Arrival Convolution

> *Note on Thesis Cross-References*: This appendix details the ACRP Report 40 empirical passenger show-up curve convolution, feature domains, and the 84-cell interaction grid. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Treatment of Data: Feature Engineering Pipeline Details*); and in **Chapter IV (Results)**, Section 4.3 (*Model Development and Execution: Feature Engineering*).

## N.1 Feature Engineering Pipeline Details
### Feature Engineering Pipeline Details

Based on these findings, an empirical passenger show-up distribution was constructed by convolving scheduled departing seats across lead horizons ( $t+1,t+2,t+3$ ):

where weights $w1=0.35$ , $w2=0.50$ , and $w3=0.15$ match empirical ACRP Report 40 arrival distributions. In operational terms, this convolution maps scheduled airline departure banks backward in time to reflect when travelers physically enter the terminal. Rather than assuming passengers arrive during their flight’s departure hour, the convolution distributes departing seat capacity across the preceding three hours according to empirical behavioral show-up curves. The distribution allocates 50% of originating passengers to the primary arrival window two hours prior ( $t-2$ ), 35% to the final hour ( $t-1$ ), and 15% to early arrivals three hours prior ( $t-3$ ).

The complete feature engineering pipeline encompasses five functional operational domains:

* Convolved Flight Schedule Volatility Features: Lead-lag convolved seats, carrier-exclusive scheduled bank dispersion (sched_hourly_std, sched_hourly_cv), and rolling schedule volatility (sched_rolling_7d_std, sched_rolling_7d_cv).
* Airside Delay and Congestion Features: Lagged mean departure delay ( $t-1$ ), departure delay dispersion ( $σDelay,t-1$ ), long-term delay volatility (otp_departure_delay_volatility_cv), tactical cancellation counts, and taxi-out queue duration.
* Temporal Cyclical Encodings: Sine and cosine harmonic transformations of hour-of-day ( $24 hr$ ) and day-of-week ( $7 days$ ), capturing diurnal and weekly rhythms without arbitrary step discontinuities.
* Operational Regime Indicators: Categorical encodings of the 84-cell interaction grid ( $S×D×H$ ).
* Facility and Aircraft Features: Screening lane count, checkpoint configuration type (finger pier vs. linear), aircraft seating gauge (aircraft_gauge_seats), route load factors, and connecting passenger ratios.

---

# Appendix O: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Local Weekly Profiles

> *Note on Thesis Cross-References*: This appendix establishes the three coupled seasonality dimensions: annual volatility regimes, day-of-week demand archetypes, and local weekly airport profiles. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Initial Exploratory Data Analysis: Defining Seasonality*) and Section 4.3 (*Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports*).

## O.1 Annual Seasonal Regimes and Day-of-Week Dynamics
### 3 Seasonality dimensions

Annual Seasonal Regimes and Coupled Volatility. Airport operational stress is not uniform across the calendar year. By analyzing daily within – day passenger arrival coefficient of variation ( $CVTSA$ ) alongside flight departure delay dispersion ( $σDelay$ ) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3). The Coupled Volatility Index is defined as:

Table 4.3Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

Day-of-Week Cyclical Dynamics and Archetypes. Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ( $1=Monday,…,7=Sunday$ ) across all Top 25 airfields yields three primary weekly operational archetypes (See appendix).

Bimodal Intraday Operational Peaks: Morning Surges and Evening Delay Cascades.

Rather than dividing each operational day into arbitrary uniform hourly intervals, intraday operations are categorized into three operational regimes capturing the bimodal diurnal congestion structure of commercial airfields. The Off-Peak regime (00:00–03:00, 3–4 hours daily) represents the overnight curfew valley characterized by sparse departures and minimal checkpoint activity. The Mid-Peak regime (08:00 to 13:00/16:00, 4–12 hours daily) reflects a steady midday plateau marked by consistent passenger screening rates and sufficient aircraft turnaround buffers. In contrast, the Peak regime unifies two non-consecutive queuing congestion windows driven by distinct operational mechanisms: the Morning Bank Surge (05:00–08:00), which is governed by extreme passenger arrival variance ( $σTSA>11,380$ pax/hr) as business travelers converge on initial departure banks; and the Evening Delay Cascade (14:00/17:00–22:00), which is driven by cumulative upstream flight delay propagation ( $σDelay>63.4$ min) that disrupts scheduled passenger show-up patterns.

### Table O.1
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields, $N = 1,341$ Days)*

| Seasonal Regime | Operational Regime Description | Calendar Days (N) | Share of Sample | Mean Daily Passengers | Intraday Scale-Free Volatility ($CV_{\text{TSA}}$) | Departure Delay Volatility ($\sigma_{\text{Delay}}$) | Coupled Volatility Index ($CVI$) | Daily Cancellation Count | Extreme Delay Exposure (>45m) | Operational Regimes Classification |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 1_OFF_PEAK | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | 27.85 | 9.85 min | 18.00% | 0.89% |
| 2_MID_PEAK | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | 32.38 | 15.14 min | 23.23% | 1.36% |
| 3_PEAK | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | 39.36 | 24.17 min | 31.04% | 3.16% |
| 4_HOLIDAY | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | 33.07 | 16.51 min | 24.33% | 1.82% |

*Note.* Adapted from `results/manuscript_tables/table_4_3b.csv`. Annual seasonal baseline regimes demonstrating the monotonic expansion of the Coupled Volatility Index ($CVI = \sigma_{\text{TSA}} \cdot \sigma_{\text{Delay}}$) from winter lull to holiday peaks.

### Table O.2
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields, $N = 1,341$ Days)*

| Day of Week | DOW Name | Operational Volatility Archetype | Study Days (N) | Mean Daily Passengers | Intraday Volatility Ratio ($CV / \overline{CV}$) | Departure Delay Volatility ($\sigma_{\text{Delay}}$) | Cancellation Exposure (%) | Coupled Volatility Shock Rank | Operational Staffing Rule |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Monday | Outbound Business Surge & High Screening Volatility | 192 | 1,246,150 | 0.604 | 56.56 min | 34.0 | 15.78 min | 23.54% |
| 2 | Tuesday | Midweek Operational Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | 50.09 min | 29.99 | 11.69 min | 19.44% |
| 3 | Wednesday | Midweek Baseline Stability (Minimum Volatility) | 192 | 1,123,368 | 0.594 | 49.27 min | 29.13 | 12.22 min | 20.05% |
| 4 | Thursday | Corporate Outbound & Early Weekend Ramp | 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| 5 | Friday | Combined Business & Weekend Getaway Surge | 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| 6 | Saturday | Volume Trough & Fleet Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| 7 | Sunday | Leisure Return Peak & Evening Delay Propagation | 192 | 1,279,017 | 0.577 | 58.07 min | 33.4 | 17.78 min | 25.60% |

*Note.* Adapted from `results/manuscript_tables/table_4_4a.csv`. Weekly operational dynamics and staffing decision rules across the Top 25 commercial airport network.

## O.2 Local Seasonal and Day-of-Week Profiles Across the Nine Selected Airports
### Day-of-Week Cyclical Dynamics and Archetypes Detail – table 4-4a

* Midweek Operational Reset (Tuesday & Wednesday): Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ( $σDelay=50.09 min$ and $49.27 min$ ), the lowest share of delayed flights ( $19.44%$ and $20.05%$ ), and the lowest Coupled Volatility Indices ( $29.99$ and $29.13$ ).
* Outbound Corporate Surge (Monday & Thursday): Mondays experience the highest within-day TSA arrival volatility across the entire week ( $CV=0.604$ , Coupled Volatility Index = $34.00$ ), driven by concentrated early-morning business traveler screening banks.
* Leisure Return Delay Propagation (Sunday): Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ( $17.78 min$ ), the highest delay dispersion ( $σDelay=58.07 min$ ), and the highest rate of flights delayed $≥15$ minutes ( $25.60%$ ).

### Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airfields display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 in the appendix reports the day-of-week passenger throughput distribution across the nine airports. The 9 airports exhibit three distinct weekly demand dynamics, which can be found in the Appendix.

The Pure Corporate Profile (LGA). LaGuardia exhibits an extreme day-of-week ratio of 2.30. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.

The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW). These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).

The Energy Sector & Midweek Profile (IAH, ORD). Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate travel schedules, followed by steep Saturday troughs.

### Table O.3
*Day-of-Week Mean Daily Passenger Throughput and Ratio Profiles Across the Nine Selected Airports*

| Airport Code | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Peak Day | Trough Day | Weekend Surge Ratio | Dominant Demand Profile |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :--- | :---: | :--- |
| BOS | 48,480 | 42,606 | 45,175 | 50,464 | 52,244 | 44,552 | 49,359 | Friday | Tuesday | 1.23 | Business & Weekend Getaway |
| DFW | 69,808 | 60,600 | 65,285 | 73,310 | 73,625 | 60,733 | 68,963 | Friday | Tuesday | 1.21 | Connecting Bank Synchronization |
| DTW | 35,584 | 30,783 | 32,827 | 37,627 | 37,871 | 30,782 | 36,037 | Friday | Saturday | 1.23 | Midwest Corporate & Connecting |
| EWR | 66,949 | 60,812 | 63,989 | 68,765 | 69,206 | 61,039 | 67,550 | Friday | Tuesday | 1.14 | Coastal Business & Leisure |
| IAH | 52,107 | 45,585 | 47,757 | 53,351 | 50,946 | 42,177 | 52,646 | Thursday | Saturday | 1.26 | Energy Sector Corporate Travel |
| LAX | 99,048 | 87,693 | 92,361 | 100,603 | 101,502 | 89,502 | 103,045 | Sunday | Tuesday | 1.18 | Transcontinental Leisure & Long-Haul |
| LGA | 49,002 | 42,740 | 44,229 | 47,045 | 21,310 | 24,619 | 48,000 | Monday | Friday | 2.3 | Pure Corporate Outbound Profile |
| ORD | 49,381 | 43,406 | 45,713 | 50,706 | 50,620 | 42,697 | 49,468 | Thursday | Saturday | 1.19 | Dual Hub Synchronized Banks |
| PHL | 31,519 | 26,716 | 28,626 | 32,740 | 32,812 | 27,675 | 31,112 | Friday | Tuesday | 1.23 | Mid-Atlantic Fortress Outbound |

*Note.* Adapted from `results/manuscript_tables/table_4_8.csv`. Local day-of-week demand distributions illustrating corporate versus leisure archetypes across the 9-airport experimental cohort.

---

# Appendix P: Diurnal Bimodal Turbulence Dynamics and Multi-Carrier Collinearity

> *Note on Thesis Cross-References*: This appendix establishes the diurnal bimodal turbulence structure (morning surge vs. evening cascade), the 84-cell interaction grid, and the mathematical proof of shared-terminal collinearity. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Initial Exploratory Data Analysis: Validity of Diurnal Non-Consecutive Dual Turbulence Peaks*).

## P.1 Validity of Diurnal Non-Consecutive Dual Turbulence Peaks
### Validity of Diurnal Non-Consecutive Dual Turbulence Peaks.

The cross-classification of the 4 annual seasonal regimes ( $S$ ), 7 days of the week ( $D$ ), and 3 diurnal blocks ( $H$ ) forms an 84-cell operational grid ( $S×D×H$ ). Across this operational grid, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $Ntrain≥50$ (median $Ntrain=215$ ), confirming that defining temporal baselines on the Top 25 airfields establishes ample sample power without sparse-sample estimation bias.

Implications for subset – multi-carrier collinearity at airports ( $CorrSjSj'≥0.88,κ>104$ ),

## P.2 Mathematical Hazard of Shared-Terminal Multi-Carrier Collinearity

A primary finding of the exploratory analysis is that commercial airports cannot be accurately modeled at the aggregate airport level in shared-terminal facilities. In shared terminals, competing airlines schedule simultaneous departure banks (e.g., 08:00 morning departures across multiple carriers):

$$\text{Corr}(S_{j,t}, S_{k,t}) \ge 0.75$$

When multiple airline flight schedules $S_{j,t}$ and $S_{k,t}$ enter a regression model simultaneously, the **Variance Inflation Factor (VIF)** explodes:

$$\text{VIF}_j = \frac{1}{1 - R_j^2} \ge \frac{1}{1 - (0.75)^2} = \frac{1}{0.4375} \approx 2.29$$

Under severe multicollinearity, the variance of estimated regression coefficients escalates, standard errors inflate, parameter estimates become unstable, and models cannot identify which carrier's flight bank drove checkpoint arrivals. In shared terminals, regression models explain less than 20% of checkpoint throughput variance ($R^2 \approx 0.20$).

**Isolating dedicated single-carrier checkpoints (Phase 3 of the filtering pipeline) eliminates multi-carrier collinearity entirely**, enabling models to achieve dedicated checkpoint-to-flight correlations of $r = +0.880$ to $+0.940$.

---

# Appendix Q: Econometric Validation of Carrier Checkpoint Demand Isolation

> *Note on Thesis Cross-References*: This appendix documents the econometric tests verifying that single-carrier screening complexes isolate airline demand without confounding cross-carrier leakage. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Econometric Validation of Carrier Checkpoint Isolation*); and in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics*).

## Q.1 Econometric Testing Architecture for Single-Carrier Isolation
### Econometric Validation of Carrier Checkpoint Isolation.:

* Volume Conservation Test: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $ρ=1.00±0.04$ ( $R2>0.95$ ).
* Zero-Flight Intercept Test: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ( $β0=12.4$ pax/hr, $p=0.40$ ).
* Cross-Carrier Perpendicularity Test: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ( $βother=0.002,p=0.62$ ).
* Terminal Layout Invariance Test: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA, DTW) against walkway-connected terminals (e.g., DFW, LAX) yielded $D=0.032$ ( $p=0.28$ ), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput leakage.

### Table Q.1
*Econometric Tests for Carrier Checkpoint Demand Isolation*

| Econometric Validation Test | Econometric Specification / Statistic | Null Hypothesis ($H_0$) | Empirical Statistic & Rejection Rule | Construct Validity Determination |
| :--- | :--- | :--- | :--- | :--- |
| **1. Volume Conservation Test** | Regress daily checkpoint throughput on carrier ticketed boardings: $Y_d = \beta_0 + \beta_1 \cdot T_d + \epsilon_d$ | $H_0: \beta_1 = 1.0, \beta_0 = 0$ | $R^2 \ge 0.88$, $\hat{\beta}_1 \in [0.92, 1.05]$, $p < 0.001$ | Pass: Checkpoint throughput scales proportionally with originating airline boardings. |
| **2. Zero-Flight Intercept Test** | Evaluate expected checkpoint demand on days/hours with zero scheduled flights: $\mathbb{E}[Y \mid S = 0]$ | $H_0: \mathbb{E}[Y \mid S = 0] = 0$ | Intercept $\hat{\beta}_0 < 0.05 \cdot \bar{Y}$ ($p > 0.10$) | Pass: No phantom baseline demand exists when airline flights are absent. |
| **3. Cross-Carrier Perpendicularity Test** | Regress carrier checkpoint throughput on competing carriers' concurrent flight banks: $Y_{j,t} = \alpha + \gamma \cdot S_{k,t} + \eta_t$ | $H_0: \gamma = 0$ (orthogonal demand) | Partial $\Delta R^2 < 0.02$, $t < 1.20$ ($p > 0.25$) | Pass: Dedicated carrier checkpoints are completely unaffected by competing airline schedules. |
| **4. Terminal Layout Invariance Test** | Two-sample Kolmogorov-Smirnov test comparing forecast error distributions between physically separate and walkway-connected concourses | $H_0: F_{\text{separate}}(e) = F_{\text{connected}}(e)$ | KS statistic $D = 0.032$, $p = 0.28$ | Pass: Concourse connection geometry does not bias or distort checkpoint arrival models. |

*Note.* Econometric verification matrix proving causal identification and single-carrier isolation across the 12 selected carrier complexes.

---

# Appendix R: Top 25 Network Census vs. Nine-Airport Experimental Cohort

> *Note on Thesis Cross-References*: This appendix provides the empirical census comparing the broader Top 25 airport network against the Nine-Airport Experimental Cohort. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Pipeline Results: Top 25 vs 9 Airport Cohort*).

## R.1 Comparative Operational Profile and Representativeness
### Top 25 vs 9 Airport Cohort

Compared to the broader Top 25 network, the nine-airport experimental cohort demonstrates higher operational density and exposure to network congestion across three primary dimensions (Table 4.7). First, the cohort exhibits $+16.9%$ higher flight movement density (annual mean of 224,576 scheduled departures versus 192,160 network-wide), ensuring that checkpoints operate under heavy, bank-synchronized arrival loads. Second, these facilities experience heightened operational disruption, with average departure delays $+7.2%$ higher (15.23 min vs. 14.21 min), cancellation rates $+14.1%$ higher (1.63% vs. 1.43%), and taxi-out times $+4.5%$ longer (20.59 min vs. 19.69 min). Third, the cohort concentrates demand into landside security screening through an $+8.1%$ higher local originating passenger share (52.55% vs. 48.61%) and a $+25.0%$ increase in absolute local originating volume (16.38M vs. 13.10M passengers annually), confirming that screening queues at these complexes are driven by landside show-up curves rather than airside transfers.

Higher Flight Movement Density. Scheduled flights are +16.9% higher (224,576 vs. 192,160), ensuring screening checkpoints operate under heavy, bank-synchronized arrival loads.

Higher Delay and Cancellation Exposure. Average departure delay is +7.2% higher (15.23 min vs. 14.21 min), cancellation rate is +14.1% higher (1.63% vs. 1.43%), and taxi-out time is +4.5% higher (20.59 min vs. 19.69 min), reflecting genuine operational congestion.

Higher Local Originating Demand. Local originating passenger share is +8.1% higher (52.55% vs. 48.61%), and true local originating volume is +25.0% higher (16.38M vs. 13.10M), concentrating demand directly into landside security checkpoint queues.

### Table R.1
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort vs. Top 25 Airfields*

| Metric Category | Operational Metric | Unit | 9-Airport Mean | 9-Airport Std Dev | Top 25 Mean | Top 25 Std Dev | Relative Delta (%) | Operational Interpretation | Significance ($p$-Value) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| BTS OTP Operations | Scheduled Domestic Flights | flights | 224,576 | 78,441 | 206,024 | 138,372 (PHL) | 360,571 (ORD) | 192,160 | +16.9% |
| BTS OTP Operations | Cancelled Flights | flights | 3,623 | 1,599 | 2,920 | 1,777 (DTW) | 6,515 (DFW) | 2,738 | +32.3% |
| BTS OTP Operations | Flight Cancellation Rate | % | 1.63% | 0.50% | 1.47% | 0.99% (LAX) | 2.46% (LGA) | 1.43% | +14.1% |
| BTS OTP Delays | Average Departure Delay | min | 15.23 | 2.75 | 15.65 | 11.55 (DTW) | 19.85 (DFW) | 14.21 | +7.2% |
| BTS OTP Delays | Significant Delay Rate (>= 15m) | % | 21.42% | 3.30% | 20.14% | 17.93% (LAX) | 28.07% (DFW) | 20.31% | +5.5% |
| BTS OTP Delays | Runway Taxi-Out Queue Time | min | 20.59 | 2.58 | 20.35 | 16.96 (DTW) | 24.67 (EWR) | 19.69 | +4.5% |
| TSA Checkpoint | Total Passenger Throughput | pax | 71,145,628 | 27,465,238 | 63,720,916 | 40,429,531 (PHL) | 129,069,341 (LAX) | 68,495,531 | +3.9% |
| TSA Checkpoint | Average Daily Passenger Count | pax/day | 53,075 | 20,473 | 47,553 | 30,171 (PHL) | 96,249 (LAX) | 51,138 | +3.8% |
| TSA Checkpoint | Average Hourly Passenger Count | pax/hr | 418.53 | 157.02 | 388.40 | 239.60 (ORD) | 662.40 (LGA) | 540.34 | -22.5% |
| TSA Checkpoint | Peak Single-Hour Checkpoint Rush | pax/hr | 2,673 | 881 | 2,654 | 1,385 (DTW) | 4,020 (EWR) | 2,784 | -4.0% |
| TSA Checkpoint | Demand Volatility (CV_TSA) | ratio | 0.8728 | 0.2000 | 0.9064 | 0.6488 (BOS) | 1.1240 (LGA) | 0.8250 | +5.8% |
| BTS DB1B Surveys | Connecting Passenger Share | % | 47.45% | 10.98% | 44.41% | 33.58% (EWR) | 66.32% (DFW) | 51.39% | -7.7% |
| BTS DB1B Surveys | Local Originating Passenger Share | % | 52.55% | 10.98% | 55.59% | 33.68% (DFW) | 66.42% (EWR) | 48.61% | +8.1% |
| BTS DB1B Surveys | True Local Originating TSA Demand | pax | 16,376,561 | 5,167,458 | 15,995,278 | 10,555,299 (DTW) | 26,293,897 (LAX) | 13,103,484 | +25.0% |
| T-100 Aircraft Gauge | Seating Capacity per Flight | seats | 168.42 | 7.49 | 168.00 | 154.20 (LGA) | 182.30 (LAX) | 171.10 | -1.6% |
| T-100 Load Factor | Route Passenger Load Factor | % | 85.08% | 0.82% | 85.26% | 83.85% (DTW) | 86.12% (EWR) | 84.73% | +0.4% |

*Note.* Adapted from `results/manuscript_tables/table_4_7.csv`. Statistical comparison validating the experimental power and operational representativeness of the nine selected airports relative to the broader national hub network.

---

# Appendix S: Key Airport Selection Contrasts (LGA vs. JFK, PHL vs. SLC)

> *Note on Thesis Cross-References*: This appendix documents the operational and structural justifications for airport inclusion and exclusion contrasts across the candidate hub universe. It is referenced in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection: Key Airport Selection Contrasts*); and in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics*).

## S.1 Operational Rationale for Specific Airport Inclusion and Exclusion
### Key Airport Selection Contrasts - Appendix

* LGA vs. JFK Selection: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's state-of-the-art consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* PHL vs. SLC Selection: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring carrier isolation within Cluster 2.

---

# Appendix T: Master Multi-Pillar Hypothesis Evaluation Matrix and Holdout Benchmarks

> *Note on Thesis Cross-References*: This appendix compiles the certified empirical evaluation benchmarks across all three candidate models and baseline control evaluated against the 2025 out-of-time holdout dataset. It is referenced in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*) and Section 4.4 (*Empirical Confirmation of Asymmetric Trade-Offs*); and in **Chapter V (Discussion)**, Section 5.3–5.5 (*Master Synthesis and Operational Recommendations*).

## T.1 Model Tradeoffs and Evaluation Overview
### Model Tradeoffs:

Model 3 achieves decisive error recovery and resilience during irregular, Model 2 provides optimal Pareto efficiency under routine daily operations, and Model 1 provides unmatched zero-shot spatial generalizability across airfields without local retraining. Furthermore, empirical tests validate the values versus volatility paradigm, confirming that checkpoint throughput volatility is coupled with flight departure delay variance (r = +0.4373, p < .05) rather than static volume or raw delay levels.

## T.2 Holdout Benchmark Execution
### Model Testing

Full Year Out of Time Holdout Dataset - spanning January 1 to December 31, 2025 (12 continuous months; 3,222 test complex-days; 72,053 complex-level screening hours).


### Hypothesis Evaluation Matrix

### Table T.1
*Master Multi-Pillar Hypothesis Evaluation Matrix (2025 Out-of-Time Holdout Suite, $N = 3,222$ Complex-Days)*

| Operational Dimension | Performance Metric | Formula / Definition | Academic Stated Target | Baseline Control (Daily Persistence) | Model 1 (Deterministic Schedule) | Model 2 (Supervised Machine Learning) | Model 3 (Dynamic Two-Stage Hybrid) | Strategic Operational Reality |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Dimension 1: Robustness | RMSE_routine (Nominal: Delay < 15m; 0 Cancels) | sqrt(mean((y - y_hat)^2)) | Lowest RMSE; MASE < 0.700 | 335.6 (MASE = 1.000) | 317.2 (MASE = 0.945) | 234.8 (MASE = 0.700) | **222.1 (MASE = 0.662)** | **Model 3 wins lowest RMSE**; Model 2 wins Routine Pareto Efficiency (zero feedback compute latency). |
| Dimension 2: Resilience | Disruption Error Multiplier (R_RMSE = RMSE_shock / RMSE_routine) | RMSE_shock / RMSE_routine | R_RMSE approx 1.00; Lowest MASE_shock; TTR < 4.0h | R = 1.00 (MASE = 1.000, TTR = 8.4h) | R = 1.32 (MASE = 1.248, TTR = 7.8h) | R = 2.14 (MASE = 1.498, TTR = 5.4h) | **R = 1.05 (MASE = 0.694, TTR = 2.8h)** | **Model 3 DECISIVE WINNER**: R = 1.05, MASE_shock = 0.694, TTR = 2.8h. Pure ML (Model 2) collapses (R = 2.14) due to Empty Checkpoint Fallacy. |
| Dimension 3: Generalizability | Relative Transfer Ratio (RTR = RMSE_target / RMSE_source) | RMSE_target / RMSE_source | RTR approx 1.00; Delta MASE <= 10.0% | RTR = 1.00 (Delta MASE = 0.0%) | **RTR = 1.04 (Delta MASE = +4.0%)** | RTR = 1.08 (Delta MASE = +8.3%) | RTR = 1.19 (Delta MASE = +21.5%) | **Model 1 DECISIVE WINNER**: RTR = 1.04, Delta MASE = +4.0%. Dynamic Hybrid (Model 3) fails zero-shot transfer due to terminal geometry overfitting. |

*Note.* Adapted from `results/manuscript_tables/table_4_10.csv`. Certified out-of-time holdout evaluation suite demonstrating Asymmetric Performance Trade-Offs ($H_1$).

---

# Appendix U: The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons

> *Note on Thesis Cross-References*: This appendix establishes the econometric proof for the Values versus Volatility operational coupling across intraday absolute, scale-free relative, and multi-day temporal horizons. It is referenced in **Chapter IV (Results)**, Section 4.4 (*The Values versus Volatility Operational Coupling*); and in **Chapter V (Discussion)**, Section 5.4 (*Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons*).

## U.1 Empirical Validation of the Values versus Volatility Operational Coupling
### The Values versus Volatility Paradigm Empirical Results

The central empirical comparison of this thesis evaluates whether predicting TSA throughput volatility requires tracking the values (levels) of OTP attributes, the volatility of OTP attributes, or a combined dual model. Evaluating across the 2025 out-of-time holdout ( $N=3,222$ test days) across the three volatility targets reveals:

* Intraday Diurnal Absolute Volatility ( $σTSA, hr$ , pax/hr dispersion):
* Values Only: Achieves $R2=0.6229$ ( $RMSE=271.6$ ). Because raw variance naturally scales with airport passenger volume, flight volume counts anchor the base magnitude of the facility.
* Volatility Only: Achieves $R2=0.4980$ ( $RMSE=313.4$ ).
* Combined Representation: Achieves $R2=0.6178$ in non-linear decision trees ( $RMSE=273.5,MAE=178.0$ ).
* Intraday Scale-Free Relative Volatility ( $CVTSA, hr=σ/μ$ , ratio):
* Under this scale-free regime, Values Only drops to $R2=0.1823$ .
* Volatility Only captures $R2=0.1853$ in decision trees.
* The Combined Dual Model outperforms all architectures ( $R2=0.2208$ , $RMSE=0.1853$ , $MAE=0.1010$ ), proving that scale-free arrival burstiness reflects an interaction between carrier schedule volume and operational disruption.
* Multi-Day Temporal Rolling Volatility ( $σTSA, 7d$ , pax/day):
* Feature Values Completely Collapse: Yielding negative test scores ( $R2=-0.2688$ in linear regression; $R2=-0.0506$ in decision trees). Because static flight counts remain relatively constant across seasons, static volume levels are blind to temporal turbulence.
* Feature Volatility Succeeds: In sharp contrast, Feature Volatility metrics achieve $R2=+0.2313$ (linear) and $R2=+0.3105$ (decision trees), improving to $R2=+0.3166$ in the Combined Model, with RMSE dropping from 4,090.7 to 3,002.3 pax/day. This confirms the operational coupling between feature volatility and passenger throughput volatility.

## U.2 Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons
### Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons

A core theoretical contribution of this thesis is the empirical demonstration of the Values versus Volatility Paradigm:

* Multi-Day Rolling Volatility ( $σTSA, 7d$ , pax/day):
* Feature Values Completely Collapse: Standard feature values (raw scheduled flights, average delay minutes) generate negative out-of-time test scores ( $R2=-0.2688$ in linear regression; $R2=-0.0506$ in decision trees). Because scheduled flight counts remain relatively stable across consecutive weeks, static volume features cannot detect shifts in temporal turbulence.
* Feature Volatility Succeeds: In contrast, Feature Volatility attributes (rolling 7-day schedule variance, cancellation volatility, and delay dispersion) achieve $R2=+0.2313$ (linear) and $R2=+0.3105$ (decision trees), improving to $R2=+0.3166$ in the Combined Model, while slashing RMSE from 4,090.7 to 3,002.3 pax/day.
* Delay Volatility Transmission: Cross-dataset econometric correlation demonstrates that Flight Departure Delay Volatility ( $CVdelay$ ) is significantly coupled with checkpoint arrival volatility ( $r=+0.4373,R2=19.13%,p=0.0288$ ). Conversely, raw flight departure delay minutes show zero linear correlation ( $r=-0.0620,p=0.769$ ). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.
* Master Consensus Factor Weights: Synthesizing variable importance across models confirms that schedule dispersion (sched_rolling_7d_mean, 23.73%; sched_hourly_mean, 6.91%) and operational volatility (otp_cancellation_volatility_cv, 8.79%; CV_{\text{delay}}, 4.32%) dominate predictive power, accounting for over 80% of consensus importance.

### Table U.1
*The Values versus Volatility Operational Coupling Across Multi-Day Temporal Horizons (Empirical Validation)*

| Volatility Target Regime | Feature Space Paradigm | Regressor Architecture | Out-of-Time Test Score ($R^2$) | Holdout RMSE | Holdout MAE | Empirical Behavioral Interpretation |
| :--- | :--- | :--- | :---: | :---: | :---: | :--- |
| 1. Intraday Diurnal Absolute Volatility (\sigma_{\text{TSA, hr}}) | Values Only (Flight Volumes) | Linear / GBDT Regressor | 0.6229 | 271.6 | 179.4 | Because raw variance scales naturally with airport passenger volume, flight counts anchor facility base scale. |
| 1. Intraday Diurnal Absolute Volatility (\sigma_{\text{TSA, hr}}) | Volatility Only (Schedule Dispersion) | Linear / GBDT Regressor | 0.4980 | 313.4 | 212.1 | Captures arrival variance structure but lacks absolute facility scale anchoring. |
| 1. Intraday Diurnal Absolute Volatility (\sigma_{\text{TSA, hr}}) | Combined Dual Model (Values + Volatility) | HistGradientBoosting | 0.6178 | 273.5 | 178.0 | Provides balanced point accuracy and surge capture across nominal operations. |
| 2. Intraday Scale-Free Relative Volatility (CV_{\text{TSA, hr}}) | Values Only (Flight Volumes) | Linear / GBDT Regressor | 0.1823 | 0.1982 | 0.1145 | Static volume counts lose predictive power once baseline scale is normalized out. |
| 2. Intraday Scale-Free Relative Volatility (CV_{\text{TSA, hr}}) | Volatility Only (Schedule Dispersion) | Decision Tree Regressor | 0.1853 | 0.1965 | 0.1120 | Directly targets scale-free arrival burstiness independent of airport size. |
| 2. Intraday Scale-Free Relative Volatility (CV_{\text{TSA, hr}}) | Combined Dual Model (Values + Volatility) | HistGradientBoosting | 0.2208 | 0.1853 | 0.1010 | Champion architecture for relative volatility; proves burstiness reflects volume and operational disruption interactions. |
| 3. Multi-Day Temporal Rolling Volatility (\sigma_{\text{TSA, 7d}}) | Values Only (Flight Volumes) | OLS Linear Regression | -0.2688 | 4,090.7 | 3,115.4 | Catastrophic failure; negative R^2 proves static volume levels perform worse than sample mean. |
| 3. Multi-Day Temporal Rolling Volatility (\sigma_{\text{TSA, 7d}}) | Values Only (Flight Volumes) | Decision Tree Regressor | -0.0506 | 3,718.2 | 2,842.1 | Non-linear trees also collapse (R^2 < 0); static flight counts are blind to multi-day weather turbulence. |
| 3. Multi-Day Temporal Rolling Volatility (\sigma_{\text{TSA, 7d}}) | Volatility Only (Schedule Dispersion) | OLS Linear Regression | +0.2313 | 3,184.5 | 2,345.8 | Decisive turnaround; feature volatility captures propagating multi-day schedule turbulence. |
| 3. Multi-Day Temporal Rolling Volatility (\sigma_{\text{TSA, 7d}}) | Volatility Only (Schedule Dispersion) | Decision Tree Regressor | +0.3105 | 3,015.6 | 2,189.2 | Robust non-linear capture; demonstrates feature dispersion is essential for multi-day horizons. |
| 3. Multi-Day Temporal Rolling Volatility (\sigma_{\text{TSA, 7d}}) | Combined Dual Model (Values + Volatility) | HistGradientBoosting | +0.3166 | 3,002.3 | 2,175.4 | Champion multi-day architecture; confirms the operational coupling between feature volatility and passenger throughput dispersion. |

*Note.* Out-of-time holdout performance proving the complete collapse of static feature values ($R^2 < 0$) and the decisive predictive success of feature volatility representations ($R^2 > +0.31$) across multi-day operational horizons.

---

# Appendix V: The Lead-Lag Asynchrony Mechanism and Shock Interaction Dynamics

> *Note on Thesis Cross-References*: This appendix documents the landside-airside queuing disconnect, morning vs. evening shock dynamics, and the 84-cell interaction grid sample depth. It is referenced in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics: The Lead-Lag Asynchrony Mechanism*) and Section 5.2 (*Robustness Across the Interaction Grid and Prevention of Delay Distortion*).

## V.1 The Lead-Lag Asynchrony Mechanism and Shock Shielding
### The Lead-Lag Asynchrony Mechanism

Traditional queuing models in airport terminal planning often assume that passenger arrival intensity $λt$ is directly proportional to departing flights in the same time window $t$ . The empirical results completely dismantle this unshifted schedule assumption. Across the Top 25 network, the operational cycle is governed by an asynchronous dual-peak structure:

* Morning Peak (05:00–08:00):
* Checkpoint Volume: Peak passenger screening throughput.
* Screening Volatility: Extreme surge volatility ( $σTSA>11,380$ pax/hr network-wide; complex-level $σTSA, hr∼540–880$ pax/hr).
* Flight Departure Delays: Low average departure delays (<5 minutes).
* Schedule Buffer: Fresh, unexhausted aircraft turnaround buffers.
* Evening Peak (14:00–22:00):
* Checkpoint Volume: Moderate and tapering screening volumes.
* Screening Volatility: Low to steady arrival volatility.
* Flight Departure Delays: Peak network-wide departure delay dispersion ( $σDelay>63$ minutes).
* Schedule Buffer: Turnaround buffers fully eroded across the National Airspace System.
* Pre-Departure Passenger Surge Window (Morning): Passengers arrive at screening checkpoints 90 to 120 minutes prior to scheduled departure (conforming to ACRP Report 40 distributions; Transportation Research Board, 2010). Checkpoint arrival volatility peaks early in the day when early-morning outbound banks depart with high schedule reliability.
* Operational Lag Phase (Evening): As the day progresses, delay propagation across the National Airspace System (NAS) compounds. Aircraft turnaround buffers are exhausted by late afternoon, causing departure delay dispersion ( $σDelay$ ) to peak between 14:00 and 22:00.

## V.2 Robustness Across the Interaction Grid and Prevention of Delay Distortion
### Robustness Across the Interaction Grid and Prevention of Delay Distortion

The coupled volatility analysis substantiates why routine accuracy holds consistently across the commercial airport network:

Preventing Extreme Storm Outliers from Distorting Normal-Day Decision Rules. When a predictive model is trained across all weather regimes simultaneously without separation, the model's rules become distorted by rare, extreme summer storm delays ( $σDelay=68.43 min$ ). Under pooled training, decision trees warp their rules to accommodate these rare storm spikes, degrading accuracy during clear, on-time operations. By conditioning training on distinct operational regimes, decision trees focus on direct operational drivers (route load factors, aircraft seat gauge, and empirical passenger show-up curves) rather than convective storm noise.

Empirical Verification of Sample Depth. The sample size audit confirms that 83 of 84 operational cells (98.8%) meet the minimum sample threshold ( $Ntrain≥50$ ), with a median training depth of 215 observations per cell, refuting any concern that temporal stratification creates sparse, over-specialized rules.

Evaluation Dimension 2: Resilience (Performance Under Severe Disruption)

Table 5.2Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption

Table 5.2: Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption

---

# Appendix W: Resilience Mechanics and the Empty Checkpoint Fallacy Under Severe Disruption

> *Note on Thesis Cross-References*: This appendix details the behavioral mechanics of forecast failures during severe weather and the live error feedback remediation in the Dynamic Hybrid. It is referenced in **Chapter V (Discussion)**, Section 5.3 (*Empirical Evaluation of Resilience Under Disruption: Resilience Mechanics and the Empty Checkpoint Fallacy*).

## W.1 Resilience Mechanics and Disruption Performance
### Resilience Mechanics and the Empty Checkpoint Fallacy

The coupled volatility findings explain the exact operational bottleneck mechanism during severe convective disruptions:

* The "Empty Checkpoint Fallacy" in Pure Machine Learning: During summer severe weather events, flight departure delays surge and cancellations spike. A pure machine learning model relying on flight schedules shifted by static show-up curves assumes that because flights scheduled for 18:00 have been delayed to 22:00 or ground-stopped, security checkpoints will experience an immediate demand collapse at 16:00. In reality, passengers arrived at the airport based on their original ticketed itineraries. Thousands of stranded travelers crowd security lines, re-screen after gate changes, or remain landside. Pure machine learning predicts an empty checkpoint, resulting in massive under-prediction errors ( $R=2.14$ ).
* Live Error Correction in the Dynamic Hybrid (Model 3): The Dynamic Hybrid actively senses real-time checkpoint conditions using 1-step recursive error feedback ( $et-1=yt-1-yt-1$ ). In practical terms, this functions like an automated safety valve: when live passenger throughput at the checkpoint exceeds what delayed flight schedules predicted, the error correction immediately alerts the model that passengers are accumulating in the terminal. The model adjusts its demand forecast upward, preventing the empty checkpoint fallacy and maintaining low disruption error multipliers ( $RMASE=1.05$ ).
Evaluation Dimension 3: Generalizability (Cross-Airport Transferability)

Table 5.3Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance

Table 5.3: Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance

### Table W.1
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

| Model Family | Model Name | Operational Approach | RMSE_shock (pax/hr) | MASE_shock | Disruption Multiplier ($R_{\text{RMSE}}$) | Time-to-Recovery (TTR) | Empty Checkpoint Failure Mode | Strategic Reality & Recommendation |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- | :--- |
| Baseline Control | Baseline Control | Daily Persistence Benchmark (y_t-24) | 398.2 | 1.0 | 1.0 | Static Reference | 8.4 hours | Static persistence benchmark; slow natural dissipation |
| Deterministic Schedule | Model 1 | Deterministic Flight Schedule Model | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades; high disruption error |
| Machine Learning | Model 2 | Supervised Machine Learning Model | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| Dynamic Hybrid | Model 3 | Dynamic Two-Stage Hybrid Model | 254.2 | 0.694 | 1.05 | TARGET MET (WINNER) | 2.8 hours | Decisive Winner: Live error feedback prevents collapse |

*Note.* Adapted from `results/manuscript_tables/table_5_2.csv`. Operational resilience metrics during severe disruptions (delays $\ge 45$m or cancellations $\ge 5$).

---

# Appendix X: Dual-Track Operational Decision Playbook and Real-World Application

> *Note on Thesis Cross-References*: This appendix translates the empirical modeling findings into an actionable operational decision playbook and regime-switched gated inference engine. It is referenced in **Chapter V (Discussion)**, Section 5.5 (*Implications and Recommendations for Predictive Forecasting in Airport Operations: Real-World Operational Application*).

## X.1 Real-World Operational Application
### Real-World Application

To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a Regime-Switched Gated Inference Engine an automated decision playbook that monitors airport turbulence and automatically selects the most suitable forecasting model:

* Gate 1: Routine Flow Track ( $Turbulence Shock Index Th<0.75$ )
* Operating Regimes: Calm seasonal periods, midweek baseline days (Tuesday and Wednesday), and steady midday hours.
* Assigned Architecture: The Supervised Machine Learning Model (Model 2).
* Operational Justification: Fast, automated execution delivering superior point accuracy ( $MASE=0.779$ ) with near-zero computing overhead and high portability across diverse terminal layouts ( $RTR=1.08$ ). Running a complex live-updating model 24/7 during calm periods imposes unnecessary IT costs and latency; Model 2 provides the optimal balance of speed and precision.
* Gate 2: Tactical Shock Track ( $Turbulence Shock Index Th≥0.75$ )
* Operating Regimes: Summer severe thunderstorms, peak holiday travel corridors, concentrated Monday morning flight waves, Sunday evening return cascades, and acute departure delay dispersion ( $σDelay>45$ min).
* Assigned Architecture: The Dynamic Two-Stage Hybrid (Model 3).
* Operational Justification: Activates live checkpoint queue feedback ( $et-1$ ), maintaining tight error bounds ( $RMASE=1.05$ ) and rapid recovery ( $TTR=2.8$ hours) during acute flight delay cascades to prevent checkpoint staffing shortfalls.

### Table X.1
*Dual-Track Operational Model Selection Policy Matrix*

| Operational Track | Operating Regime | Assigned Canonical Architecture | Target Objective / Thresholds | Empirical Holdout Performance | Deployment Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Gate 1: Routine Flow Track (T(h) < 0.75) | Calm seasonal periods (1_OFF_PEAK), midweek baseline days (Tue/Wed), steady midday hours (08:00-13:00) | Model 2: Supervised Machine Learning Model | Lowest RMSE under routine conditions & MASE_routine < 0.70 | RMSE = 273.5 pax/hr; MASE = 0.680-0.700; RTR = 1.08; Transfer Delta = +7.9% | Fast automated execution delivering superior routine accuracy with zero online compute overhead and high spatial portability across diverse terminal layouts. |
| Gate 2: Tactical Shock Track (T(h) >= 0.75) | Summer convective thunderstorms (3_PEAK), peak holiday rushes, ground stops (Delay >= 45m or Cancels >= 5) | Model 3: Dynamic Two-Stage Hybrid Model | Recovery RMSE Multiplier R ≈ 1.00 & Lowest MASE_shock (TTR < 4.0h) | RMSE = 254.2 pax/hr; MASE = 0.694; R_MASE = 1.05; TTR = 2.8 hrs | Closed-loop 1-step recursive error innovation feedback (e_{t-1}) actively tracks live queue accumulation, preventing empty-checkpoint forecast collapse and recovering in 2.8 hours. |

*Note.* Adapted from `results/manuscript_tables/dual_track_model_selection_policy.csv`. Dual-track operational deployment policy mapping operational flight regimes to assigned model architectures.

---
