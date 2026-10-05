# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow

## Chapter 1: Introduction

### 1.1 Context and Operational Motivation
The contemporary commercial aviation ecosystem is characterized by an escalating infrastructure capacity gap, wherein passenger volume growth systematically outpaces the physical expansion capabilities of airport terminal facilities (Adacher et al., 2017). This operational friction is most acutely manifested at passenger security screening checkpoints, which function as restrictive bottlenecks within the terminal complex. From a systems engineering perspective, an airport terminal can be conceptualized as a stochastic queueing network (De Neufville & Odoni, 2014), where the security checkpoint represents a critical subsystem characterized by non-stationary arrival processes and variable service times. The physical constraint of the checkpoint boundary necessitates predictive modeling to proactively align resource allocation (e.g., open lanes, staffing) with anticipated throughput. 

### 1.2 Significance of the Study
The significance of this study resides in its introduction of an evaluation triad—comprising robustness, resilience, and generalizability—as a novel contribution to the domain of aviation operations research. While existing literature predominantly evaluates predictive models through narrow accuracy metrics on homogenous datasets, this study asserts that operational viability requires a multi-dimensional assessment. By formalizing these three dimensions mathematically and empirically testing them across a diverse cohort of airports, this research provides a rigorous framework for evaluating the true utility of predictive architectures in stochastic environments.

### 1.3 Statement of the Problem
The persistent inability to accurately forecast security checkpoint throughput stems from a tri-fold gap in the prevailing literature and operational methodologies. First, there exists an inadequate definition of demand that erroneously conflates departing seat capacity with localized checkpoint demand, failing to account for connecting passenger biases and spatio-temporal show-up distributions. Second, existing models suffer from a lack of regime-aware training, treating highly volatile, post-pandemic operational landscapes as stationary phenomena. Third, there is insufficient cross-airport validation; predictive models are routinely overfit to the idiosyncratic data generating processes of a single facility, rendering them brittle when exposed to structural variations across different terminal layouts and carrier networks.

### 1.4 Purpose Statement
The purpose of this study is to systematically compare deterministic (Models M0, M1), probabilistic/machine learning (Models M2, M3, M4), and hybrid (Model M5) architectures for predicting airport passenger security screening throughput. By employing a tightly controlled, purposively filtered dataset, this study isolates the predictive efficacy of these model families under varying operational conditions, thereby establishing empirical benchmarks for performance.

### 1.5 Research Question
This study is guided by the following central research question: "Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing robustness, resilience, or generalizability?"

### 1.6 Delimitations
To ensure statistical validity and control for exogenous variance, this study is demarcated by several precise boundaries. The spatial scope is delimited to a cohort of nine major U.S. airports representing the primary hubs of the "Big 3" network carriers (American Airlines: DFW, PHL, ORD; Delta Air Lines: DTW, LGA, BOS; United Airlines: EWR, IAH, LAX), filtered from the Top 25 U.S. airports. The temporal scope is restricted to the post-pandemic recovery phase, spanning May 2022 through December 2025, ensuring regime stationarity. Furthermore, deep neural networks (DNNs) are explicitly excluded from the model suite to preserve strict econometric interpretability and parameter transparency.

### 1.7 Limitations and Assumptions
This research is subject to limitations inherent in the utilized data architectures. The reliance on the Airline Origin and Destination Survey (DB1B) introduces an assumption of quarterly stationarity regarding connecting passenger ratios, which may lag dynamic network adjustments. Furthermore, the study relies exclusively on publicly available federated datasets, precluding the integration of proprietary, real-time carrier manifest data. The modeling also assumes a rigid carrier-exclusive checkpoint boundary, abstracting away the phenomenon of passenger cross-terminal migration when physical infrastructure permits.

This thesis is structured as follows: Chapter 2 synthesizes the theoretical and methodological literature governing passenger flow and time-series forecasting. Chapter 3 details the rigorous methodology, including the four-tiered filtering pipeline and the mathematical formulation of the M0-M5 model suite. Chapter 4 presents the empirical results, structural validation, and formal comparative analysis utilizing defined metrics (e.g., $R\_MASE$, $RTR$, $MASE$, and Diebold-Mariano tests), demonstrating a benchmarked 14.2% error reduction. Chapter 5 concludes with operational recommendations and directions for future research.

## Chapter 2: Review of the Literature

### 2.1 Traditional Approaches to Airport Passenger Flow Modeling
The foundational paradigms of airport passenger flow modeling are rooted in deterministic queueing theory and static empirical distributions. Early frameworks, synthesized extensively by De Neufville and Odoni (2014), relied on homogeneous Poisson processes to approximate passenger arrivals. However, these models systematically failed to capture the non-stationary, bursty nature of flight schedules. Subsequent refinements introduced the concept of the "show-up curve," an empirical probability density function defining the arrival time of a passenger relative to their scheduled departure (Ashford et al., 2011). While foundational, standard show-up curve models often assume temporal invariance, rendering them suboptimal in highly volatile contemporary environments. 

### 2.2 Simulation-Based Modeling of Terminal Operations
To address the stochastic complexities of terminal subsystems, researchers transitioned toward discrete-event simulation (DES) architectures. Brunetta et al. (1999) and later Solak et al. (2009) demonstrated the utility of DES in evaluating checkpoint configurations under varying load factors. More recently, agent-based modeling (ABM) has been utilized to capture emergent behaviors of heterogeneous passenger typologies (Schultz & Reitmann, 2019). While simulation excels at operational impact analysis and bottleneck identification, its computational intensity and reliance on extensive calibration parameterizations limit its efficacy for near-real-time predictive forecasting.

### 2.3 Time-Series Forecasting in Transportation Systems
The evolution of predictive analytics in transportation has heavily leveraged univariate and multivariate time-series methodologies. The application of Seasonal Autoregressive Integrated Moving Average (SARIMA) models has been ubiquitous for capturing cyclical demand patterns (Gillen & Hasheminia, 2013). However, traditional econometric models struggle with non-linear disruption impacts. In response, probabilistic and machine learning techniques, such as Gradient Boosting Machines (GBMs), have gained prominence. Kim and Lee (2023) demonstrated the superior capability of tree-based ensembles in handling high-dimensional, non-linear feature spaces related to flight schedules, though often at the cost of inferential transparency.

### 2.4 Hybrid and Multi-Source Architectures
Contemporary literature increasingly advocates for hybrid architectures that synthesize disparate modeling philosophies.

#### 2.4.1 Feature-Level Fusion
Feature-level fusion seeks to integrate structured schedule data with exogenous indicators. Gao et al. (2022) established that the inclusion of real-time delay telemetry significantly enhances short-term predictive horizons. The integration of spatial metrics and advanced schedule parsing has been shown to reduce localized forecast variance, provided the input streams are rigidly conformed (Nie et al., 2022).

#### 2.4.2 Dynamic Feedback/Kalman Filtering
Advanced hybrid systems employ error-correction mechanisms to adapt to stochastic shocks. The integration of Kalman filtering with base-level predictions allows models to dynamically update state estimates based on observed residuals (Sun et al., 2021). This continuous correction is critical for maintaining model resilience during irregular operations where theoretical show-up profiles decouple from physical reality.

### 2.5 Post-Pandemic Volatility and Structural Regime Changes
The systemic shock of the COVID-19 pandemic necessitated a fundamental reevaluation of stationarity assumptions in aviation modeling (ICAO, 2020). Post-pandemic operational environments exhibit heightened volatility, altered booking curves, and structural shifts in passenger behavior (Yoo & Kang, 2023). Takakura et al. (2019) and Gupta et al. (2021) highlight the necessity of regime-aware algorithms capable of identifying and adapting to these macro-level shifts, thereby emphasizing the need for robust feature engineering and dynamic modeling architectures over static historical averaging.

The limitations identified in the prevailing literature—specifically the over-reliance on static show-up profiles, the computational burden of simulation for real-time forecasting, and the vulnerability of traditional time-series models to structural regime shifts—motivate the methodological framework detailed in Chapter 3.

## Chapter 3: Methodology

### 3.1 Context and Operational Motivation
This chapter delineates the methodological architecture required to isolate and model the underlying data generating process (DGP) of airport passenger flow. The checkpoint is modeled as a stochastic queueing network, where the state of the system is a function of non-stationary arrivals. The methodology is structured to synthesize disparate operational telemetry into a unified, mathematically rigorous evaluation framework.

### 3.2 Significance of the Study
The core methodological contribution is the implementation of a four-tiered purposive filtering pipeline. By systematically pruning exogenous variance and structural anomalies from the dataset, this pipeline creates a controlled experimental environment. This rigor ensures that the comparative performance of the predictive architectures is a function of algorithmic efficacy rather than artifactual noise, thereby enabling fair and generalizable comparisons.

### 3.3 Statement of the Problem
The methodology addresses three specific analytical gaps: (i) the demand definition gap, addressed by computationally extracting local originating passengers from aggregate seat capacities; (ii) the regime training gap, addressed via a coupled volatility index and hierarchical temporal stratification; and (iii) the cross-airport validation gap, addressed through the factorial grid design of the cohort.

### 3.4 Purpose Statement
The purpose of this methodology is to (a) engineer a conformed data warehouse integrating four federated federal feeds; (b) execute a purposive filtering strategy to yield a mathematically robust 9-airport cohort; and (c) deploy a benchmarked suite of six predictive architectures (M0-M5) evaluated against stringent quantitative metrics.

### 3.5 Research Question
Within this methodological context, the research question is operationalized as: "How do variations in model architecture (deterministic, probabilistic, hybrid) mathematically influence predictive accuracy ($MASE$), resilience under shock ($RTR$), and robustness across varied checkpoint topologies?"

### 3.6 Delimitations
Geographically, the study is delimited to a 9-airport cohort strategically selected from the Top 25 U.S. airports. Temporally, the modeling period spans May 2022 to December 2025. Data granularity is aggregated to the terminal complex level to mitigate micro-routing variances. Finally, the model family explicitly excludes deep neural networks to maintain strict parameter interpretability.

### 3.7 Limitations and Assumptions
Methodological limitations include the assumption of DB1B quarterly stationarity for connection ratios and the mathematical treatment of zero-throughput periods. Furthermore, cancellation asymmetry is acknowledged. However, statistical power is guaranteed, with 98.8% of spatial-temporal cells maintaining $N \geq 50$ observations.

### 3.8 Established Foundations (Checkout Main)
The baseline for this analysis is grounded in established queueing theory and standard operational parameters. Let the utilization factor at time $t$ be defined as $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$, where $\lambda(t)$ is the arrival rate, $c(t)$ is server capacity, and $\mu$ is the service rate. Passenger arrival profiles are governed by ACRP Report 40 standard show-up curves, heavily reliant on the lognormal arrival density where the time prior to departure $\tau$ is distributed as $\tau \sim Lognormal(\mu \approx 4.65, \sigma \approx 0.35)$. Crucially, the methodology enforces the physical arrow of time, rejecting contemporaneous modeling artifacts and ensuring predictions rely solely on strictly antecedent data vectors.

### 3.9 Four-Tiered Purposive Filtering (Merge Working-Dev)
To construct the definitive evaluation cohort, a four-tiered filtering algorithm was applied:
1. **Macro Filter:** Restricted to Top 25 U.S. airports exhibiting a power-law distributed demand profile $P(X > x) \sim x^{-\alpha}$ where $\alpha \approx 1.15$, capturing 67.2% of national throughput.
2. **Meso Filter:** Enforced co-location of the "Big 3" carriers and structurally excluded Southwest Airlines (WN) due to its unique bimodal arrival distribution, defined mathematically as a mixture model $\tau_{WN} \sim w_1 N(\mu_1, \sigma_1^2) + w_2 N(\mu_2, \sigma_2^2)$.
3. **Micro Filter:** Required strict carrier-to-checkpoint isolation probabilities such that $P(\text{Carrier} = j^* | \text{Checkpoint } k) = 1.0$ for primary tenants, with the number of secondary carriers $\kappa < 25$.
4. **Factorial Filter:** Yielded a balanced $3 \times 3$ grid of 9 hub airports (AA: DFW/PHL/ORD, DL: DTW/LGA/BOS, UA: EWR/IAH/LAX).

### 3.10 Data Sources and Warehouse Conformance
The integrated data warehouse conforms four disparate sources. TSA FOIA records (reduced from 19.5M to 6.4M usable observations across 955 lanes representing 2.70B passengers) provide the target variable. BTS OTP (45.8M filtered to 13.2M flights across 17 carriers) supplies schedule telemetry. Form 41 (1.9M to 422K) provides load factors, and DB1B (12.9M to 22.1M coupons) furnishes the crucial connection-ratio vectors.

### 3.11 Coupled Volatility & Diurnal Turbulence
To quantify operational instability, a Coupled Volatility Index ($CVI$) was engineered. Defining the coefficient of variation for TSA throughput as $CV_{TSA}$ and the standard deviation of arrival delays as $\sigma_{Delay}$, the index is defined as $CVI = CV_{TSA} \times \sigma_{Delay}$. A temporal shock index $T(h)$ was clustered using 1D K-Means to objectively classify hours into OFF_PEAK, MID_PEAK, and PEAK regimes, explicitly accommodating non-consecutive dual peaks.

### 3.12 Hierarchical Cross-Classification
To control for temporal heterogeneity, the data space is projected into an 84-cell tensor defined by $\delta \times D \times H = 4 \times 7 \times 3$, corresponding to 4 annual seasonal regimes, 7 days of the week, and 3 diurnal classifications.

### 3.13 Statistical Power and Sample Size (Push Origin Main)
The temporal origin (Candidate B) was set to May 2022, structurally verified via a Chow test ($p \geq 0.15$) and CUSUM analysis to guarantee post-pandemic stationarity. The final dataset comprises 270,460 total observations (Train: 122,847; Validation: 72,723; Test: 72,053) incorporating a 7-day buffer. Statistical power is mathematically robust: 83 of 84 cells (98.8%) contain $N \geq 50$, 65 of 84 (77.4%) achieve $N \geq 100$, and the test set alone maintains $N \geq 30$ in 70 of 84 cells (83.3%).

### 3.14 Model Benchmark Suite
The predictive suite comprises:
- **M0 (Diurnal Naive):** $y_t = y_{t-24}$
- **M1 (SARIMAX):** Baseline econometric formulation.
- **M2 (Show-Up Curve Regressor):** Deterministic convolution of schedules.
- **M3 (LightGBM):** Non-linear gradient boosting parameterized with a Tweedie objective ($p=1.3$) to handle zero-inflation.
- **M4 (Tri-Modal Pipeline):** Ensemble logic routed by temporal regime.
- **M5 (Sequential SARIMA-Tree Hybrid):** Fuses structural forecasting with non-linear residual learning using Kalman feedback $e_t = y_t - C \cdot \hat{x}_{t|t-1}$.

### 3.15 Evaluation Metrics
Formal evaluation relies on the Mean Absolute Scaled Error:
$$ MASE = \frac{MAE}{\frac{1}{T-m} \sum_{t=m+1}^{T} |y_t - y_{t-m}|} $$
Robustness ($R\_MASE$) is calculated over the 95th percentile of errors. Resilience To Recovery ($RTR$) measures the integral of error decay following an operational shock. Statistical significance between forecasts is established via the Diebold-Mariano test.

### 3.16 Validity
Construct validity is enforced by mathematically decoupling total seats from true demand via the formula $Demand_{orig} = Seats \times LF \times (1 - C_{ratio})$. Checkpoint heterogeneity is aggregated safely via $Y_{kt} = \sum y_{klt}$. Overnight closures (where 98.6% of zeros occur between 00:00-04:00) are explicitly modeled, and structural bias from tactical versus advance cancellations is addressed in feature processing.

### 3.17 Treatment of the Data (Checkout Working-Dev)
The data underwent rigorous Extract, Transform, and Load (ETL) routines, prioritizing imputation transparency and enforcing strict chronological splits to prevent data leakage, ensuring all findings represent genuine predictive capability suitable for future iterative refinement.

## Chapter 4: Results

### 4.1 Master Descriptive Statistics and Data Health Census
Table 4.1 details the Data Foundation Census. Through algorithmic spatial key resolution, 7,489 distinct localized facility strings were recovered, and 22,190 ambiguous strings were mapped to surrogate key 0, preventing the ingestion of 9.71 million phantom passenger counts. Analysis of nighttime closures revealed 450,973 absolute zero throughput observations, with 98.6% localized to the 00:00–04:00 window, empirically justifying the Tweedie variance parameter $p=1.3$. Regarding operational fidelity, the master dataset exhibited a mean flight delay of 12.70 minutes, with 20.12% of flights delayed $\geq 15$ minutes and a 2.03% global cancellation rate.

### 4.2 Four-Tiered Filtering Pipeline Results
#### 4.2.1 Macro Filter
The macro-level restriction to the Top 25 U.S. airports successfully retained 67.2% of national throughput while driving the utilization convergence $\rho(t) \to 1.0$ during peak hours, ensuring sufficient signal density.
#### 4.2.2 Meso Filter
The algorithmic exclusion of Southwest Airlines (WN) removed severe bimodal distortion, reducing the variance of the aggregate show-up curve by 18.4%.
#### 4.2.3 Micro Filter
Enforcing carrier isolation probabilities ($P=1.0$) for primary tenants and capping secondary carrier noise ($\kappa < 25$) yielded structurally pure terminal modeling environments.
#### 4.2.4 Factorial Grid
The final 9-airport grid (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL) was finalized. LGA was selected over JFK to minimize international long-haul distortion, and PHL superseded SLC due to superior spatial layout clarity.

### 4.3 Operational Clusters
Principal Component Analysis (PCA) captured 77% of the variance across three principal components. K-Means clustering ($K=4$) identified distinct operational archetypes.
#### 4.3.1 Hub Disconnect
Analysis of extreme hub environments (e.g., CLT) demonstrated a 76% connecting passenger ratio. Unfiltered deterministic models generated a 200% overprediction error, validating the absolute necessity of the DB1B connection ratio dampening function.
#### 4.3.2 Delay Divergence
Cluster 2 exhibited a mean delay of 11.6 minutes, compared to Cluster 3’s structurally degraded 16.1 minutes, highlighting distinct operational resilience profiles.
#### 4.3.3 Coupled Volatility
Table 4.3b illustrates that across the 4 seasonal regimes, the $CVI$ deteriorated from a baseline of 27.85 during optimal periods to 39.36 during disruption intervals, representing a +41.3% escalation in joint variance.
#### 4.3.4 DOW Dynamics
Table 4.4a confirms profound Day-Of-Week dynamics. The Monday morning surge generated the highest volatility ($CV = 0.604$), whereas Sunday evenings exhibited cascading operational degradation with a mean delay of 17.78 minutes.
#### 4.3.5 Diurnal Turbulence
Table 4.4b maps the non-consecutive peak structures, validating the 1D K-Means regime boundaries. Table 4.4c confirms that the 84-cell hierarchical tensor provides sufficient granularity to capture these fluctuations without compromising statistical power.

### 4.4 Temporal Demarcation
The selection of Candidate B (May 2022) as the temporal origin was statistically justified. Post-mask mandate cessation, predictive structural stability recovered significantly, with baseline explanatory power returning to $R^2 = 0.672$, confirming the resumption of predictable stochasticity.

### 4.5 Econometric Validation
Rigorous econometric testing confirmed baseline assumptions. Volume conservation checks yielded $\rho = 1.00 \pm 0.04$. Dummy variable regressions testing zero-flight conditions produced $\beta_0 = 12.4$ ($p=0.40$, not significant). Cross-carrier interference was negligible ($\beta_{other} = 0.002, p=0.62$), and layout invariance testing demonstrated robust uniformity ($D=0.032, p=0.28$).

### 4.6 Feature Engineering
Feature predictive power was evaluated sequentially. A purely contemporaneous schedule base yielded poor explanatory power ($R^2 = 0.1988$). Implementing a $t+2$ peak lead vector improved performance to $0.4054$. Integrating empirical show-up curve convolution raised $R^2$ to $0.4878$, and final inclusion of dynamic load factor estimations finalized the baseline feature set at $R^2 = 0.4985$.

### 4.7 Model Benchmark
The formal evaluation of the M0-M5 suite yielded definitive statistical separations. The baseline M0 (Diurnal Naive) performed poorest. M1 and M2 established functional deterministic floors. M3 (LightGBM) captured significant non-linearities, while M4 provided strong regime-specific robustness. However, M5 (Sequential SARIMA-Tree Hybrid) demonstrated statistically dominant performance, achieving a peak $R^2 = 0.6270$ and a globally minimized $MASE = 0.846$.

#### 4.7.1 Regime Stratification
Diebold-Mariano testing across the 84-cell tensor confirmed that M5's superiority was not uniform but was most statistically significant during PEAK regimes and high $CVI$ intervals, successfully reducing aggregate error by 14.2% relative to the deterministic baselines.
