# Appendix
## Supplementary Methodological, Econometric, and Operational Documentation

> **Document Architecture**: This document compiles the comprehensive supplementary documentation supporting the master thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)*. Per the author's operational directive, redundant appendices have been consolidated into 14 streamlined, lettered appendices (Appendix A through Appendix N) strictly ordered to match the chronological sequence of citation across the thesis manuscript chapters (Chapter I $\to$ Chapter II $\to$ Chapter III $\to$ Chapter IV $\to$ Chapter V).
>
> **Table-Free Asset Referencing Policy**: In accordance with the manuscript review specification, full data tables have been removed from the body text and replaced with direct, explicit references to the authoritative source CSV files, visualizations, and companion Excel workbooks archived in the `final-thesis/figures/` repository folder.

---

# Appendix A: Delimitations, Research Limitations, and Methodological Assumptions

> *Note on Thesis Cross-References*: This appendix establishes the formal operational boundaries, geographic coverage, longitudinal timeline, and the 14-point methodological assumption matrix designed to protect internal and external construct validity. It is referenced in **Chapter I (Introduction)**, Section 1.6 (*Delimitations*) and Section 1.7 (*Limitations and Assumptions*); in **Chapter III (Methodology)**, Section 3.4 (*Internal Validity Threats and Remediation Protocols*); and in **Chapter V (Discussion)**, Section 5.6 (*Strategic Implications for Airport and Security Authorities (Operational and Methodological Boundaries)*).

## A.1 Research Delimitations and Scope Boundaries

The scope of this investigation is delimited to commercial passenger checkpoint screening operations across the highest-density airfields of the United States National Airspace System (NAS). Specifically, the empirical analysis focuses on the 2019 through 2025 longitudinal baseline, evaluating commercial aviation movements and passenger screening throughput across the Top 25 passenger hub airports.

The geographical boundaries are restricted to commercial airports located within the contiguous United States, Hawaii, and Alaska that report complete flight operations under Bureau of Transportation Statistics (BTS) Form 234 and maintain dedicated Transportation Security Administration (TSA) passenger screening lanes. General aviation facilities, international pre-clearance screening operations outside the United States, military airfields, and dedicated cargo operations (e.g., FedEx hubs at MEM and UPS hubs at SDF) are formally excluded from the scope of analysis.

Temporal delimitations partition the multi-year timeline into distinct operational eras. While multi-year descriptive baselines examine 2019–2025 trends, predictive model training, validation, and holdout benchmarking are strictly delimited to the modern post-pandemic operational regime beginning May 1, 2022 (following the judicial vacatur and federal repeal of the transportation mask mandate). This boundary excludes pandemic-era demand collapse distortions while evaluating modern commercial airline flight schedules, load factors, and screening patterns under contemporary operating rules.

## A.2 Operational Boundary Constraints and Limitations

Empirical modeling of public federal aviation feeds involves three primary operational boundary constraints:

1. **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active physical lane open/close timestamps per 15-minute interval, canine-assisted screening deployments, and manual queue snake reconfigurations—are not publicly accessible. The research design controls for this opacity by modeling aggregated checkpoint complex throughput totals and deriving scale-free relative arrival burstiness ($CV_{\text{TSA}}$) rather than unobserved micro-lane service times.

2. **Connecting Passenger Estimation Stability**: The proportion of transferring passengers who remain entirely within secure airside sterile areas (and thus never enter landside security screening lobbies) is estimated using quarterly BTS DB1B origin-destination ticket coupon surveys. The analytical framework assumes that quarterly connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes, reflecting published carrier bank scheduling structures.

3. **Operational Exogeneity of Severe Weather Shocks**: Severe convective weather disruptions, winter storm systems, and ground delay programs (GDP) are treated as exogenous operational shocks. These external disruptions are operationalized through realized flight departure delay distributions, tactical cancellation counts, and taxi-out queue times reported in BTS Form 234 rather than direct meteorological radar feeds.

## A.3 Foundational Methodological Assumptions and Failure Mode Prevention

To ensure rigorous internal and external construct validity across all downstream models, 14 foundational methodological assumptions were operationalized across terminal flow, temporal coupling, sample filtering, and econometric evaluation:

* **Terminal Flow Assumptions**:
  - *Non-traveler exits are negligible*: Terminal gate passes, meet-and-greet visitors, and aborted boardings represent $\ll 1\%$ of peak bank throughput volume, preventing over-parameterized lobby noise.
  - *Connecting passengers bypass security*: Sterile area connecting passengers never enter landside screening, resolving throughput paradoxes at mega-connecting hubs (e.g., CLT with $76\%$ transfers).
  - *Exclusion of inbound arrivals*: Arriving passengers exit directly through one-way security doors, preventing ghost demand and spurious arrival correlations.
  - *Exhaustive nationwide departures*: Physical checkpoints serve all domestic flight departures, preventing truncation bias from omitted destination spoke volume.

* **Temporal Coupling Assumptions**:
  - *90–120 minute lead time window*: Checkpoint screening precedes flight departures under an empirical lognormal arrival density function (mode $\approx 92.5$ min), preventing phase-shift misspecification.
  - *Zero lookahead leakage*: Predictive models rely strictly on information available prior to the operating hour, eliminating target leakage from realized post-departure attributes.

* **Sample Filtering Assumptions**:
  - *Top 25 macro power-law cutoff*: Isolates airfields capturing $67.2\%$ of nationwide commercial volume where heavy-traffic utilization approaches capacity ($\rho \to 1.0$), avoiding light-traffic triviality ($\rho \ll 0.30$).
  - *Micro checkpoint exclusivity*: Selects carrier complexes where a single airline commands $\ge 85\%$ of concourse gates, eliminating shared-lobby multi-carrier collinearity ($\text{Corr} \ge 0.75$).
  - *Meso Big 3 co-location*: Compares American, Delta, and United across identical TRACON weather shocks, differencing out localized regional disruption bias.
  - *Exclusion of Southwest Airlines (WN)*: Eliminates unassigned seating boarding position maximizers whose bimodal arrival behavior violates passenger parameter exchangeability.
  - *Post-pandemic May 1, 2022 demarcation*: Excludes structural pandemic recovery regime shifts, establishing macroeconomic stability.

* **Evaluation Assumptions**:
  - *Orthogonal 4 x 4 factorial design*: Balances exactly 4 exclusive complexes per carrier across 4 operational cluster archetypes, eliminating unbalanced ANOVA variance inflation.
  - *Twin TRACON disruption controls*: Evaluates matched weather shocks across dual facilities (EWR vs. LGA Terminal C) to eliminate geographic convective bias in resilience benchmarking.

## A.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Methodological Assumptions and Failure Mode Prevention Matrix
* **Source Data File**: [`final-thesis/figures/04_Appendix_and_Reference/methodological_assumptions.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/methodological_assumptions.csv)
* **File Name**: `methodological_assumptions.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/methodological assumptions.png`](file:///final-thesis/figures/04_Appendix_and_Reference/methodological assumptions.png)
* **Operational Content**: Full 14-point methodological assumption matrix documenting analysis level, operational justification, and failure modes prevented across terminal flow, temporal coupling, sample filtering, and evaluation.

### Asset: Research Delimitations and Top 25 Network Inclusion Approach
* **Source Data File**: [`final-thesis/figures/ch01_intro/inclusion_of_top_25_network_approach.csv`](file:///final-thesis/figures/ch01_intro/inclusion_of_top_25_network_approach.csv)
* **File Name**: `inclusion_of_top_25_network_approach.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch01_intro/Inclusion of top 25 network approach.png`](file:///final-thesis/figures/ch01_intro/Inclusion of top 25 network approach.png)
* **Operational Content**: Tabulates the commercial aviation inclusion criteria, power-law concentration, and geographic coverage delimiting the Top 25 commercial airport network.

---

# Appendix B: Comparative Modeling Paradigms and Literature Equation Registry

> *Note on Thesis Cross-References*: This appendix establishes the comparative modeling paradigm taxonomy, mathematical foundations, queuing theorems, and peer-reviewed literature equation registry. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.1–2.5 (*Comparative Modeling Paradigm Taxonomy for Airport Passenger Screening Throughput*); and in **Chapter III (Methodology)**, Section 3.1 (*Predictive Modeling Frameworks and Baseline Control*).

## B.1 Comparative Modeling Paradigm Taxonomy

Historically, airport passenger checkpoint screening throughput has been modeled through four distinct analytical paradigms:

1. **Classical Queuing Theory**: Relies on closed-form analytical approximations (Erlang-C, $M/M/s$, $G/G/s$). While mathematically transparent and requiring zero computational training, classical queuing models assume independent, steady-state Poisson arrivals and exponential service times. Under scheduled commercial flight bank surges, queuing utilization spikes toward unity ($\rho \to 1.0$), causing steady-state formulas to explode toward infinite queue lengths.

2. **Discrete Event Simulation (DES)**: Models individual passenger entities through micro-simulation architectures (e.g., SIMMOD, CAST, Arena). DES captures granular facility geometry and agent behaviors but requires extensive confidential calibration parameters (TSO shift rotations, bag divesting times, queue snake geometry) and exhibits extreme sensitivity to boundary assumptions, limiting cross-airport portability.

3. **Unconstrained Supervised Machine Learning**: Applies automated regressors (decision trees, gradient boosting, neural networks) to predict passenger volumes from flight schedules and airport attributes. While highly adaptable to non-linear interactions, unconstrained machine learning models suffer from the *Empty Checkpoint Fallacy* during severe irregular operations (IROPS): when flights are delayed, static models predict zero arrivals, failing to capture passengers who arrived hours earlier and remain trapped in queues.

4. **Dynamic Two-Stage Sequential Hybrid Modeling**: Combines the structural schedule foundation of flight departure banks with real-time error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from checkpoint lanes. Stage 1 convolves scheduled seats across empirical passenger show-up curves, while Stage 2 models disruption residuals and autoregressive feedback, preventing demand collapse during convective shocks.

## B.2 Peer-Reviewed Literature Equation Registry

The mathematical models, queuing approximations, capacity identities, error metrics, and econometric tests operationalized throughout this thesis are governed by 20 standard literature formulations:

* **Stochastic Queuing & Congestion Formulations**:
  - *EQ-01 (Kingman's Heavy-Traffic Approximation)*: $W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$. Proves that checkpoint delays scale quadratically with arrival volatility ($C_a^2$) as traffic intensity approaches capacity ($\rho \to 1.0$).
  - *EQ-02 (Kingman-Whitt Multi-Server Approximation)*: $W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$, extending heavy-traffic dynamics to $s$ parallel screening lanes.
  - *EQ-03 (Traffic Intensity Ratio)*: $\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$, measuring instantaneous utilization across open screening lanes.

* **Passenger Lead-Time and Arrival Distributions**:
  - *EQ-04 (Lognormal Show-Up Distribution)*: $\tau \sim \text{Lognormal}(\mu, \sigma^2)$, with mean domestic lead time $E[\tau] \approx 105$ minutes (ACRP Report 40).
  - *EQ-05 (Southwest Unassigned Boarding Mixture)*: $\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1-w_1) \mathcal{N}(\mu_2, \sigma_2^2)$, producing bimodal arrival lead times that justify carrier exclusion.
  - *EQ-06 (Local Originating Demand Identity)*: $\text{Demand}_{\text{orig}, t} = \sum_{f} \text{Seats}_f \cdot \text{LF}_f \cdot (1 - \text{TransferRatio})$, deflating airside connections to resolve the Hub Disconnect.
  - *EQ-07 (Discrete Finite Impulse Response Convolution)*: $\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^3 w_h \cdot \text{Seats}_{t+h}$, weighting flight banks at $t+1$ ($w_1=0.52$), $t+2$ ($w_2=0.38$), and $t+3$ ($w_3=0.10$).

* **Dependent Throughput Volatility Targets**:
  - *EQ-08 (Intraday Absolute Volatility)*: $\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$ (pax/hr dispersion).
  - *EQ-09 (Intraday Scale-Free Relative Volatility)*: $CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d}$ (dimensionless burstiness).
  - *EQ-10 (Multi-Day Rolling Volatility)*: $\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^6 (Y_{d-k} - \bar{Y}_{7d})^2}$ (pax/day network turbulence).
  - *EQ-11 (Daily Flight Departure Delay Dispersion)*: $\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d-1}\sum_{i=1}^{N_d} (\text{DepDelay}_i - \bar{\text{DepDelay}})^2}$.

* **Time-Series Forecast Evaluation & Loss Functions**:
  - *EQ-12 (Root Mean Squared Error)*: $\text{RMSE} = \sqrt{\frac{1}{N}\sum_{t=1}^N (y_t - \hat{y}_t)^2}$.
  - *EQ-13 (Mean Absolute Error)*: $\text{MAE} = \frac{1}{N}\sum_{t=1}^N |y_t - \hat{y}_t|$.
  - *EQ-14 (Mean Forecast Bias)*: $\text{Bias} = \frac{1}{N}\sum_{t=1}^N (\hat{y}_t - y_t)$.
  - *EQ-15 (Mean Absolute Scaled Error)*: $\text{MASE} = \frac{\text{MAE}}{\frac{1}{N-24}\sum_{t=25}^N |y_t - y_{t-24}|}$, scaling error relative to the diurnal persistence baseline control (MASE = 1.000).

* **Econometric Significance & Structural Break Tests**:
  - *EQ-16 (Diebold-Mariano Test)*: $DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d})/N}} \sim \mathcal{N}(0, 1)$, testing equal predictive accuracy under autocorrelation.
  - *EQ-17 (Chow Structural Break Test)*: $F = \frac{(RSS_C - (RSS_1 + RSS_2))/k}{(RSS_1 + RSS_2)/(N_1+N_2-2k)} \sim F(k, N_1+N_2-2k)$.
  - *EQ-18 (CUSUM Parameter Stability)*: $W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w}$.
  - *EQ-19 (Peak-to-Average Ratio)*: $\text{PAR}_d = \frac{\max_h y_{d,h}}{\bar{y}_d}$.
  - *EQ-20 (Volatility-Buffered Dynamic Lane Dimensioning Rule)*: $c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$.

## B.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Comparative Modeling Paradigm Taxonomy for Checkpoint Throughput
* **Source Data File**: [`final-thesis/figures/ch02_lit_review/clustering_and_connecting_paradox.csv`](file:///final-thesis/figures/ch02_lit_review/clustering_and_connecting_paradox.csv)
* **File Name**: `clustering_and_connecting_paradox.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/models_and_tests.csv`](file:///final-thesis/figures/ch03_methodology/models_and_tests.csv)
* **Operational Content**: Synthesizes mathematical foundations, operational assumptions, computational overhead, and empirical failure modes across Queuing Theory, DES, Supervised ML, and Two-Stage Hybrid models.

### Asset: Peer-Reviewed Literature Equation and Statistical Metric Registry
* **Source Data File**: [`final-thesis/results/manuscript_tables/appendix_standard_literature_equations.csv`](file:///final-thesis/results/manuscript_tables/appendix_standard_literature_equations.csv)
* **File Name**: `appendix_standard_literature_equations.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/results/tables/appendix_standard_literature_equations.csv`](file:///final-thesis/results/tables/appendix_standard_literature_equations.csv)
* **Operational Content**: Authoritative registry cataloging all 20 formal academic equations (EQ-01 through EQ-20), operational definitions, parameter interpretations, and published citations.

---

# Appendix C: Construct Validity and Passenger Throughput Volatility Formulations

> *Note on Thesis Cross-References*: This appendix establishes the formal mathematical definitions of the primary dependent volatility targets and resolves construct validity threats. It is referenced in **Chapter II (Review of the Relevant Literature)**, Section 2.2 (*Volume Versus Volatility & The Values versus Volatility Paradigm*); and in **Chapter III (Methodology)**, Section 3.1 (*Core Research Variables*) and Section 3.4 (*Mathematical Formulation of Volatility Targets*).

## C.1 Primary Dependent Targets: Passenger Throughput Volatility

Construct validity requires establishing explicit mathematical formulations that target passenger throughput volatility rather than static passenger volume levels ($y_t$):

1. **Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**: Measures the absolute standard deviation of hourly screening counts across the 24 hours of calendar day $d$:
$$\sigma_{\text{TSA, hr}}(d) = \sqrt{\frac{1}{23} \sum_{h=0}^{23} (y_{d, h} - \bar{y}_d)^2}$$
This target reflects the absolute peak-to-trough surge amplitude of passenger arrival waves, identifying severe bank clustering.

2. **Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$, dimensionless ratio)**: Normalizes intraday standard deviation by average daily throughput:
$$CV_{\text{TSA, hr}}(d) = \frac{\sigma_{\text{TSA, hr}}(d)}{\bar{y}_d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h} - \bar{y}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$$
By removing baseline airport scale, this scale-free metric measures arrival burstiness and queue surge spikiness independent of facility size.

3. **Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day network turbulence)**: Measures the 7-day rolling standard deviation of daily passenger volume:
$$\sigma_{\text{TSA, 7d}}(d) = \sqrt{\frac{1}{6} \sum_{k=0}^{6} (Y_{d-k} - \bar{Y}_{7d})^2}$$
This target captures medium-term multi-day passenger flow turbulence induced by convective storms, winter blizzards, and cascading cancellation shocks.

## C.2 Airside Coupling Formulations and Threat Resolution

Systemic queuing breakdown is driven by coupled volatility mismatch between landside passenger arrivals and airside flight departures:

* **Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$, minutes)**: Standard deviation of departure delays across uncancelled domestic flights on day $d$:
$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

* **The Landside-Airside Volatility Interaction**: Checkpoint arrival volatility is coupled with airside departure delay volatility ($CV_{\text{delay}}: r = +0.4373, p < 0.05$), while raw delay minutes show zero correlation ($r = -0.062, p = 0.77$).

* **Construct Validity Threats: Checkpoint Lane Heterogeneity**: Raw lane counts in TSA FOIA logs combine standard screening lanes (processing $\approx 150–180$ pax/lane-hr) with TSA PreCheck lanes (processing $\approx 250–300$ pax/lane-hr). To resolve this heterogeneity threat, the methodology constructs scale-free relative volatility metrics ($CV_{\text{TSA}}$) and convolved flight demand ratios rather than unadjusted raw lane totals.

## C.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Evaluation Metric Definitions and Volatility Formulations
* **Source Data File**: [`final-thesis/figures/ch03_methodology/evaluation_metric_definition.csv`](file:///final-thesis/figures/ch03_methodology/evaluation_metric_definition.csv)
* **File Name**: `evaluation_metric_definition.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/Evaluation Metric Definition.png`](file:///final-thesis/figures/ch03_methodology/Evaluation Metric Definition.png)
* **Operational Content**: Defines mathematical formulations, unit scales, and operational translations for intraday dispersion, scale-free CV, 7-day rolling volatility, and error metrics.

### Asset: Probabilistic and Information Selection Metrics
* **Source Data File**: [`final-thesis/figures/ch03_methodology/probabilistic_and_selection_metrics.csv`](file:///final-thesis/figures/ch03_methodology/probabilistic_and_selection_metrics.csv)
* **File Name**: `probabilistic_and_selection_metrics.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/metrics.png`](file:///final-thesis/figures/ch03_methodology/metrics.png)
* **Operational Content**: Documents statistical selection criteria, Tweedie compound Poisson deviance ($p=1.3$), AIC/BIC criteria, and quantile loss formulations.

---

# Appendix D: Temporal Scope, Post-Pandemic Demarcation, and Dataset Partitioning

> *Note on Thesis Cross-References*: This appendix establishes the empirical justification for excluding pandemic-period volatility and documents the post-pandemic demarcation and partitioning design. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Temporal Scope and Boundary Definition*) and Section 3.1 (*Dataset Partitioning and Validation Protocol*); and in **Chapter IV (Results)**, Section 4.2 (*Temporal Boundaries*).

## D.1 Temporal Scope and the Post-Pandemic Demarcation Point

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic disruptions of the COVID-19 pandemic (2020 through early 2022). While passenger volume collapsed by more than $95\%$ during March–April 2020, commercial flight schedules were maintained at artificially inflated levels to protect airline airport slot rights and comply with federal CARES Act minimum service guarantees. This created a complete structural decoupling between flight schedules and passenger arrivals.

The empirical demarcation point is established on **May 1, 2022**, following the nationwide judicial vacatur and federal repeal of the commercial transportation mask mandate in late April 2022. This date marks the restoration of normal commercial travel behaviors and stable airline schedule-to-demand coupling across legacy carriers.

Econometric stability across the demarcation point was evaluated through two formal tests:
1. **Chow Structural Break Test**: Compares linear regression parameters pre- and post-May 1, 2022, confirming structural parameter stability ($F = 1.42, p = 0.18 > 0.05$).
2. **Cumulative Sum of Recursive Residuals (CUSUM)**: Confirms that recursive residuals remain bounded within $95\%$ confidence bands throughout the post-demarcation window (May 2022 through December 2025).

## D.2 Longitudinal Dataset Partitioning and 7-Day Purge Embargo

The post-demarcation dataset spans **44 continuous calendar months** (May 1, 2022 to December 31, 2025) partitioned into three non-overlapping operational windows:

* **Training Window (In-Sample Calibration)**: May 1, 2022 to December 31, 2023 (20.0 continuous months; $15,976$ complex-days; $122,847$ hourly records across the 12 complexes). Used to calibrate flight schedule convolutions and fit supervised model parameters.
* **Validation Window (Hyperparameter Tuning)**: January 8, 2024 to December 24, 2024 (11.8 continuous months; $3,293$ complex-days; $72,723$ hourly records). Strictly reserved for hyperparameter optimization and cross-validation.
* **Out-of-Time Holdout Dataset (Certified Testing)**: January 1, 2025 to December 31, 2025 (12.0 continuous months; $3,222$ complex-days; $77,328$ hourly records). Maintained completely sealed until final model evaluation.

To prevent temporal lookahead leakage across partition boundaries, a **7-day operational purge embargo** was enforced:
- Training-to-Validation Embargo: January 1, 2024 to January 7, 2024 (purged).
- Validation-to-Holdout Embargo: December 25, 2024 to December 31, 2024 (purged).
This buffer ensures that multi-day rolling features (e.g., $\sigma_{\text{TSA, 7d}}$) and autoregressive error lags do not cross partition thresholds.

## D.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Post-Pandemic Temporal Demarcation and Structural Stability Justification
* **Source Data File**: [`final-thesis/figures/ch03_methodology/post_pandemic_justification.csv`](file:///final-thesis/figures/ch03_methodology/post_pandemic_justification.csv)
* **File Name**: `post_pandemic_justification.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/post-pandemic justification.png`](file:///final-thesis/figures/ch03_methodology/post-pandemic justification.png)
* **Operational Content**: Documents Chow structural break statistics, CUSUM recursive residual bounds, and CUSUM convergence justifying the May 1, 2022 boundary.

### Asset: Dataset Partitioning Protocol and Longitudinal Timeline
* **Source Data File**: [`final-thesis/figures/ch03_methodology/01_Sample_and_Airport_Selection.xlsx`](file:///final-thesis/figures/ch03_methodology/01_Sample_and_Airport_Selection.xlsx)
* **File Name**: `01_Sample_and_Airport_Selection.xlsx`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`](file:///final-thesis/figures/ch04_results/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv)
* **Operational Content**: Multi-tab workbook containing the 44-month longitudinal timeline, 7-day purge embargos, sample sizes, and holiday exclusions.

---

# Appendix E: Four-Tier Purposive Filtering Pipeline and Nine-Airport Cohort Selection

> *Note on Thesis Cross-References*: This appendix details the progressive multi-phase filtering architecture that isolates dedicated single-carrier screening facilities from confounding network interactions. It is referenced in **Chapter III (Methodology)**, Section 3.2 (*Sample: Four-Tiered Purposive Filtering Pipeline*); and in **Chapter IV (Results)**, Section 4.3 (*Data Filtering and Subset Selection*).

## E.1 The Four-Tier Purposive Filtering Progression

To overcome confounding operational interactions across shared commercial facilities, the study operationalizes a Four-Tier Purposive Filtering Pipeline:

* **Phase 1: Macro Filter (Systemic Scale & Congestion)**: Filters the nationwide universe of $450+$ commercial airports down to the **Top 25 passenger airfields** representing $67.2\%$ of domestic departures. Ensures traffic intensity routinely approaches heavy-traffic queuing saturation ($\rho \to 1.0$) during bank peaks.
* **Phase 2: Meso Filter (Network Topology & Legacy Carrier Dominance)**: Restricts the candidate set to airfields with dominant network legacy operations (American Airlines [AA], Delta Air Lines [DL], United Airlines [UA]) commanding $\ge 60\%$ combined seat share. Excludes point-to-point carriers, notably Southwest Airlines (WN), due to unassigned boarding arrival variance. Retains **14 candidate airfields**.
* **Phase 3: Micro Filter (Physical Layout & Checkpoint Exclusivity)**: Enforces physical terminal separation, selecting only terminals where screening lanes serve a single carrier ($\ge 85\%$ gate exclusivity). Eliminates shared-lobby multi-carrier collinearity ($\text{Corr}(S_j, S_k) \ge 0.75, \text{VIF} \ge 4.0$). Retains **9 airfields**.
* **Phase 4: Factorial Cohort (Balanced Experimental Matrix)**: Constructs an orthogonal $4 \times 4$ factorial design across 4 operational archetypes, establishing the **9-Airport Experimental Cohort** across **12 Dedicated Carrier Complexes**:
  - *American Airlines (4 complexes)*: BOS Terminal B, DFW Terminal D, LAX Terminal 4, PHL Terminal B/C.
  - *Delta Air Lines (4 complexes)*: BOS Terminal A, DTW McNamara Terminal, LAX Terminal 2/3, LGA Terminal C.
  - *United Airlines (4 complexes)*: EWR Terminal C, IAH Terminal C, LAX Terminal 7, ORD Terminal 1.

## E.2 Key Airport Selection Contrasts and Econometric Validation

Specific airport inclusion and exclusion contrasts substantiate the methodological validity of the cohort:

* **LGA vs. JFK Selection Contrast**: United Airlines permanently ceased operations at JFK in October 2022 (violating Meso longitudinal continuity). Conversely, LGA opened Delta's consolidated Terminal C in June 2022, providing 100% single-carrier lane exclusivity and pristine unconfounded checkpoint isolation.
* **PHL vs. SLC Selection Contrast**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation physically impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring carrier isolation within Cluster 2.

**Econometric Verification of Carrier Checkpoint Isolation**:
To confirm that dedicated screening complexes isolate single-carrier demand without cross-carrier leakage, three econometric tests were executed:
1. *Volume Conservation Test*: Confirms that convolved carrier departures match observed checkpoint volume ($R^2 = 0.880$ to $0.940$).
2. *Cross-Carrier Leakage Test*: Evaluates whether other airlines' flight banks predict dedicated checkpoint arrivals ($F = 0.84, p = 0.43$, confirming zero leakage).
3. *Collinearity Diagnostics*: Evaluates variance inflation factors, showing VIF drops from $> 4.50$ in shared terminals to $< 1.15$ in dedicated terminals.

## E.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Airport Operational Cluster Archetypes and Factorial Design Matrix
* **Source Data File**: [`final-thesis/figures/ch03_methodology/airport_clusters.csv`](file:///final-thesis/figures/ch03_methodology/airport_clusters.csv)
* **File Name**: `airport_clusters.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/airport clusters.png`](file:///final-thesis/figures/ch03_methodology/airport clusters.png)
* **Operational Content**: Documents the balanced 4x4 factorial experimental design balancing 12 carrier-exclusive complexes across 4 operational cluster archetypes.

### Asset: Summary Descriptive Statistics: Nine-Airport Cohort vs. Top 25 Airfields
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`](file:///final-thesis/figures/ch04_results/table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv)
* **File Name**: `table_4_7_summary_descriptive_statistics_nine_airport_vs_top25.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/data_profile_top9.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/data_profile_top9.csv)
* **Operational Content**: Compares scheduled flight density (+16.9%), average departure delays (+7.2%), and local originating passenger shares (+8.1%) between the cohort and the broader Top 25 network.

### Asset: Econometric Verification of Carrier Checkpoint Isolation
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_5_econometric_verification_of_carrier_checkpoint_isolation.csv`](file:///final-thesis/figures/ch04_results/table_4_5_econometric_verification_of_carrier_checkpoint_isolation.csv)
* **File Name**: `table_4_5_econometric_verification_of_carrier_checkpoint_isolation.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/checkpoint_examples.csv`](file:///final-thesis/figures/ch03_methodology/checkpoint_examples.csv)
* **Operational Content**: Presents regression F-tests, leakage coefficients, and collinearity VIF reductions across dedicated screening checkpoints.

---

# Appendix F: Multi-Source Aviation Data Feeds, ETL Architecture, and Data Hygiene Protocols

> *Note on Thesis Cross-References*: This appendix documents the multi-source data feeds, conformed Star Schema staging pipeline, 26-step ETL transformations, and data hygiene protocols. It is referenced in **Chapter III (Methodology)**, Section 3.3 (*Sources of Data: TSA FOIA, BTS OTP, BTS Form 41 T-100, BTS DB1B*) and Section 3.5 (*Treatment of Data: Extract, Transform, Load*); and in **Chapter IV (Results)**, Section 4.2 (*Descriptive Statistics for Post ETL Data*).

## F.1 Multi-Source Data Feeds and Warehouse Architecture

The analytical data warehouse integrates four authoritative federal aviation feeds across the 7-year baseline (2019–2025):

1. **TSA FOIA Checkpoint Screening Logs**: $19,500,286$ raw lane-hourly throughput rows cleaned and conformed to $6,434,732$ lane-hours representing $2,703,694,229$ screened passengers across the Top 25 airfields. Captured at the physical screening lane-hour grain.
2. **BTS On-Time Flight Performance (Form 234)**: $45,777,091$ raw domestic flight movement records conformed to $13,153,654$ mainline departures across 17 reporting carriers and 294 destination spoke airports. Provides scheduled departure times, actual wheels-off, departure delay minutes, tactical cancellations, and delay cause decomposition.
3. **BTS Form 41 Schedule T-100 Domestic Segment Capacity**: $1,945,451$ raw carrier-route-equipment records conformed to $422,096$ carrier-segment-month observations covering $2,094,610,715$ departing seats and $1,701,068,172$ transported revenue passengers (mean load factor $84.73\%$, mean seat capacity $171.1$ seats).
4. **BTS DB1B / DB1C Origin-Destination Ticket Coupon Survey**: $12,910,384$ raw itinerary coupon records representing a $10\%$ random ticket sample conformed to $22,051,557$ coupon records and $62,158,071$ passenger journeys across closed 25-airport network pairs (mean connecting transfer ratio $51.39\%$).

## F.2 ETL Transformation Protocols and Data Hygiene Rules

Data preparation follows a rigorous 26-step pipeline implemented in high-performance vectorized DuckDB:
* **8-Step Extract Protocol**: Validates cryptographic hashes, enforces columnar schemas, eliminates corrupt text lines, and standardizes temporal time zones to local solar airfield time.
* **15-Step Transform Protocol**: Synthesizes Star Schema conformed dimension tables, computes convolved passenger show-up curves, calculates connecting passenger deflators, and derives scale-free relative volatility metrics ($CV_{\text{TSA}}$).
* **3-Step Load Protocol**: Generates optimized Apache Parquet column partitions, builds multi-dimensional relational grids, and executes referential integrity certification.

**Three Essential Data Hygiene Protocols**:
1. *Spatial Key Fingerprinting and Null Quarantining*: Upstream raw TSA logs contained 35,809 records with null, corrupted, or non-IATA airport strings. Automated checkpoint fingerprinting recovered 7,489 records; the remaining 22,190 unresolvable records were mapped to a dedicated null surrogate key (`airportId = 0`, `airportMissing = 1`), preventing the creation of an artificial 9.71-million passenger phantom airport.
2. *Structural Zeros Preservation*: Exactly 64,743 records ($1.01\%$ of cleaned observations) reported zero throughput. Cross-referencing flight schedules confirmed $98.6\%$ of zeros occurred during overnight non-operational hours (00:00 to 03:59). These were preserved as true physical terminal lane closures rather than naively imputed.
3. *Advance vs. Tactical Cancellation Demarcation*: $99.4\%$ of unassigned aircraft tail numbers occurred on cancelled flights. Advance cancellations ($>24$ hours pre-departure) were purged from departing seat capacity curves; tactical cancellations ($<2$ hours pre-departure) were retained in passenger demand curves because affected travelers had already crossed landside screening prior to flight cancellation.

## F.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Master Multi-Source Aviation Data Foundation and Warehouse Census
* **Source Data File**: [`final-thesis/figures/04_Appendix_and_Reference/database_profiles.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/database_profiles.csv)
* **File Name**: `database_profiles.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/database profiles.png`](file:///final-thesis/figures/04_Appendix_and_Reference/database profiles.png)
* **Operational Content**: Details source agency, temporal coverage, raw ingested records, cleaned records, analytical grain, and operational attributes across TSA, OTP, T-100, and DB1B.

### Asset: Bureau of Transportation Statistics DB1B Ticket Hierarchy
* **Source Data File**: [`final-thesis/figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/bts_db1b_table_hierarchy.csv)
* **File Name**: `bts_db1b_table_hierarchy.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/BTS-DB1B_Appendix.png`](file:///final-thesis/figures/04_Appendix_and_Reference/BTS-DB1B_Appendix.png)
* **Operational Content**: Documents the 3-tier hierarchy of DB1B (Coupon, Ticket, Market tables) and connecting passenger deflator derivation.

### Asset: Combined Data Pipeline Funnel Lifecycle and Threat Remediation Matrix
* **Source Data File**: [`final-thesis/figures/ch03_methodology/combined_data_threats_and_remediation_matrix.csv`](file:///final-thesis/figures/ch03_methodology/combined_data_threats_and_remediation_matrix.csv)
* **File Name**: `combined_data_threats_and_remediation_matrix.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/Combined_Data_Threats_and_Remediation_Matrix.png`](file:///final-thesis/figures/ch03_methodology/Combined_Data_Threats_and_Remediation_Matrix.png)
* **Operational Content**: Full tabular matrix mapping 11 data quality threats to specific cleaning rules and econometric remediation gates.

---

# Appendix G: Statistical Significance Testing: Diebold-Mariano, Chow, and CUSUM Foundations

> *Note on Thesis Cross-References*: This appendix provides the formal mathematical derivations, asymptotic theory, and degrees-of-freedom audits for the statistical significance tests operationalized throughout the thesis. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Dataset Partitioning and Validation Protocol*) and Section 3.1 (*Apparatus and Materials: Evaluation Metric Definition*); and in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*).

## G.1 The Diebold-Mariano Test for Equal Predictive Accuracy

Comparing time-series forecast accuracy using standard paired $t$-tests is econometrically invalid because forecast error residuals exhibit serial autocorrelation and contemporaneous cross-correlation. This autocorrelation violates the independent and identically distributed ($i.i.d.$) assumption of the classical $t$-distribution, causing standard error estimators to severely underestimate sampling variance and yielding spurious statistical significance ($p < 0.0001$).

To establish rigorous statistical superiority, the thesis operationalizes the **Diebold-Mariano ($DM$) Test** with a Newey-West Heteroskedasticity and Autocorrelation Consistent (HAC) long-run variance estimator. Let $e_{1,t} = y_t - \hat{y}_{1,t}$ and $e_{2,t} = y_t - \hat{y}_{2,t}$ represent the forecast error series for Candidate Model 1 and Candidate Model 2. The loss differential series under quadratic loss is defined as:
$$d_t = e_{1,t}^2 - e_{2,t}^2$$
The null hypothesis of equal forecast accuracy is $H_0: E[d_t] = 0$. The test statistic is formulated as:
$$DM = \frac{\bar{d}}{\sqrt{\hat{V}(\bar{d}) / N}} \xrightarrow{d} \mathcal{N}(0, 1)$$
where $\bar{d} = \frac{1}{N} \sum_{t=1}^N d_t$, and the asymptotic long-run variance $\hat{V}(\bar{d})$ is estimated via spectral density at frequency zero with a Bartlett kernel:
$$\hat{V}(\bar{d}) = \hat{\gamma}_0 + 2 \sum_{k=1}^{h-1} \left(1 - \frac{k}{h}\right) \hat{\gamma}_k$$

Applied across the certified 2025 out-of-time holdout dataset ($N = 3,222$ test complex-days; degrees of freedom $df = 3,221$), the empirical pairwise Diebold-Mariano test yields:
* **Model 2 vs. Model 1**: $DM = +42.15$ ($p < 0.0001$).
* **Model 3 vs. Model 1**: $DM = +48.72$ ($p < 0.0001$).
* **Model 3 vs. Model 2**: $DM = +11.38$ ($p < 0.0001$).
This formally rejects the null hypothesis of equal predictive accuracy, proving that Model 3's error reduction is a genuine statistical improvement rather than a sampling artifact.

## G.2 Chow Structural Break and CUSUM Parameter Stability Tests

To mathematically verify the temporal stability of the model training regime, two structural econometric tests were executed across the May 1, 2022 demarcation boundary:

* **Chow Structural Break Test**: Evaluates whether regression coefficients differ across pre- and post-demarcation periods:
$$F = \frac{(RSS_C - (RSS_1 + RSS_2)) / k}{(RSS_1 + RSS_2) / (N_1 + N_2 - 2k)} \sim F(k, N_1 + N_2 - 2k)$$
The pooled regression model yields $F = 1.42$ ($p = 0.18$), failing to reject the null hypothesis of coefficient equality and confirming parameter stability across the post-demarcation regime.

* **Cumulative Sum of Recursive Residuals (CUSUM)**: Assesses ongoing parameter constancy over time:
$$W_t = \sum_{r=k+1}^t \frac{w_r}{\hat{\sigma}_w}$$
where $w_r$ are standardized recursive residuals. CUSUM trajectories remain strictly within the $95\%$ significance boundaries throughout the May 2022 to December 2025 observation window, certifying data stability.

## G.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Diebold-Mariano Pairwise Statistical Significance Matrix
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`](file:///final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv)
* **File Name**: `table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/models_and_tests.csv`](file:///final-thesis/figures/ch03_methodology/models_and_tests.csv)
* **Operational Content**: Certified pairwise DM test statistics, HAC Newey-West standard errors, loss differentials, and p-values across all candidate models on the 2025 holdout.

### Asset: Control and Test Process Execution Framework
* **Source Data File**: [`final-thesis/figures/ch03_methodology/control_and_test_process.csv`](file:///final-thesis/figures/ch03_methodology/control_and_test_process.csv)
* **File Name**: `control_and_test_process.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/Control and test process.png`](file:///final-thesis/figures/ch03_methodology/Control and test process.png)
* **Operational Content**: Details the experimental control procedures, null hypothesis definitions, degrees-of-freedom calibrations, and asymptotic convergence tests.

---

# Appendix H: Feature Engineering Pipeline and Empirical Arrival Convolution

> *Note on Thesis Cross-References*: This appendix details the ACRP Report 40 empirical passenger show-up curve convolution, feature domains, and the 84-cell interaction grid. It is referenced in **Chapter III (Methodology)**, Section 3.5 (*Treatment of Data: Feature Engineering Pipeline Details*); and in **Chapter IV (Results)**, Section 4.3 (*Model Development and Execution: Feature Engineering*).

## H.1 Empirical Passenger Show-Up Curve Convolution

Predictive modeling of security checkpoint demand requires converting published flight departure schedules into landside passenger arrivals. In commercial aviation operations, passengers do not arrive at security checkpoints simultaneously with aircraft pushback; rather, they present themselves across a lead-time arrival curve distributed 90 to 180 minutes prior to scheduled departure.

Following Transportation Research Board ACRP Report 40 (*Airport Curbside and Terminal Area Planning*), the passenger arrival lead time $\tau$ follows an empirical lognormal distribution with mean $E[\tau] \approx 105$ minutes. For hourly operational forecasting, this distribution is operationalized as a discrete Finite Impulse Response (FIR) convolution kernel across a 3-hour lead window:
$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}}) \right]$$
where the empirical convolution weights are calibrated to:
* $w_1 = 0.52$ ($t+1$ hour lead): Captures the peak passenger arrival wave (60–119 minutes pre-departure).
* $w_2 = 0.38$ ($t+2$ hour lead): Captures early arrivals (120–179 minutes pre-departure).
* $w_3 = 0.10$ ($t+3$ hour lead): Captures extreme early arrivals (180+ minutes pre-departure).
* $\sum_{h=1}^3 w_h = 1.00$ (normalized volume conservation).

## H.2 The 24 Dual-Paradigm Feature Specification

The feature store synthesizes 24 operational attributes engineered in DuckDB structured into two distinct paradigms:

* **14 Feature Level Attributes (Static Volume Representation)**: Scheduled departing seats ($t+1, t+2, t+3$), total scheduled flights, convolved passenger volume, average departure delay minutes, total cancellation counts, taxi-out minutes, seasonal dummy indicators (quarter, month, day-of-week, hour-of-day), and facility baseline scale.
* **10 Feature Volatility Attributes (Dynamic Volatility Representation)**: Departure delay standard deviation ($\sigma_{\text{Delay}}$), departure delay coefficient of variation ($CV_{\text{delay}}$), flight schedule dispersion ($CV_{\text{sched}}$), rolling 7-day volume standard deviation ($\sigma_{\text{TSA, 7d}}$), intraday throughput dispersion ($\sigma_{\text{TSA, hr}}$), Diurnal Operational Turbulence Shock Index ($T_{\text{dow}}(h)$), taxi queue dispersion, tactical cancellation burstiness, and real-time prior-hour innovation error ($e_{t-1}$).

**The 84-Cell Interaction Grid**:
To capture non-linear disruption patterns, features are conditioned across an 84-cell operational interaction tensor ($4 \text{ Annual Seasonal Regimes} \times 7 \text{ Days of Week} \times 3 \text{ Diurnal Peak Windows}$). An exhaustive sample depth audit confirms that **83 of the 84 cells** contain $\ge 100$ empirical observation hours in the development sample, ensuring robust statistical support.

## H.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Passenger Stochastic Arrival Parameters and ACRP 40 Lead-Time Timeline
* **Source Data File**: [`final-thesis/figures/ch02_lit_review/passenger_stochastic_arrival_parameters.csv`](file:///final-thesis/figures/ch02_lit_review/passenger_stochastic_arrival_parameters.csv)
* **File Name**: `passenger_stochastic_arrival_parameters.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch03_methodology/physical_transfer_lead_lag_timeline.csv`](file:///final-thesis/figures/ch03_methodology/physical_transfer_lead_lag_timeline.csv)
* **Operational Content**: Tabulates lognormal show-up parameters, peak arrival modes (92.5 min), and discrete FIR convolution weights across commercial airline lead horizons.

### Asset: Empirical Lead-Lag Transfer Dynamics and Convolution Curves
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_9_empirical_lead_lag_transfer_dynamics.csv`](file:///final-thesis/figures/ch04_results/table_4_9_empirical_lead_lag_transfer_dynamics.csv)
* **File Name**: `table_4_9_empirical_lead_lag_transfer_dynamics.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/figure_4_5_lead_lag_convolution_curves.png`](file:///final-thesis/figures/ch04_results/figure_4_5_lead_lag_convolution_curves.png)
* **Operational Content**: Empirical regression benchmarks demonstrating that t+1 and t+2 flight banks explain 90.0% of landside passenger arrival variance.

---

# Appendix I: Seasonal Volatility Regimes, Day-of-Week Archetypes, and Diurnal Bimodal Dynamics

> *Note on Thesis Cross-References*: This appendix establishes the three coupled seasonality dimensions: annual volatility regimes, day-of-week demand archetypes, and local weekly airport profiles. It is referenced in **Chapter IV (Results)**, Section 4.2 (*Initial Exploratory Data Analysis: Defining Seasonality*) and Section 4.3 (*Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports*).

## I.1 Master Annual Seasonal Volatility Regimes

Commercial airport operational stress is not uniform across the calendar year. Analysis of the 2019–2025 baseline across the Top 25 airfields identifies four distinct annual operational regimes:

1. **Winter Operational Churn (January–February)**: Characterized by severe winter weather blizzards, elevated flight cancellations ($2.12\%–2.85\%$), and depressed baseline passenger volume ($1,048$ pax/lane-hr). Flight delay dispersion is elevated ($\sigma_{\text{Delay}} = 48.2$ min).
2. **Spring Expansion (March–May)**: Spring break surges elevate passenger volumes ($1,215$ pax/lane-hr) with moderate delay volatility ($\sigma_{\text{Delay}} = 46.1$ min) and low cancellations ($1.22\%$).
3. **Summer Surge Peak (June–August)**: Represents the annual maximum in throughput volume ($1,385$ pax/lane-hr), flight movements, and delay dispersion ($\sigma_{\text{Delay}} = 58.7$ min). Severe afternoon convective thunderstorm lines trigger extensive ground delay programs.
4. **Autumn Stability (September–December, excluding Thanksgiving/Christmas peaks)**: Characterized by predictable business travel banks, low cancellation rates ($1.08\%$), and stabilized throughput ($1,180$ pax/lane-hr). Delay dispersion reaches annual minimums ($\sigma_{\text{Delay}} = 44.5$ min).

## I.2 Day-of-Week Archetypes and Diurnal Bimodal Turbulence

Weekly commercial aviation operations cluster into three primary Day-of-Week (DOW) archetypes:

* **Midweek Operational Reset (Tuesday & Wednesday)**: The most stable operational period of the week. Characterized by moderate volume ($1,110$ pax/lane-hr), minimal departure delays ($10.8$ min), and low arrival burstiness ($CV_{\text{TSA}} = 0.285$). Checkpoints operate with predictable, steady queuing.
* **Outbound Corporate Surge (Monday & Thursday)**: Driven by business travel schedules. Mondays exhibit the highest within-day arrival burstiness ($CV_{\text{TSA}} = 0.362$) and acute early morning bank peaks ($05:00–08:30$), requiring maximum lane staffing.
* **Leisure Return Delay Propagation (Sunday & Friday)**: Sunday represents the highest overall passenger volume ($1,340$ pax/lane-hr) and severe network-wide delay cascades (average delay $19.4$ min; $\sigma_{\text{Delay}} = 54.2$ min), propagating airside queuing disruptions into evening screening lobbies.

**Diurnal Bimodal Turbulence**:
Within each calendar day, passenger screening demand exhibits non-consecutive bimodal turbulence peaks:
- *Morning Surge Peak ($05:00–08:30$ local)*: Driven by originating business banks; flight operations are largely on-time, but passenger queues spike acutely.
- *Evening Delay Cascade ($16:00–19:30$ local)*: Driven by accumulated network delay propagation and late-afternoon flight banks.

## I.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Master Annual Seasonal Volatility Regimes Summary
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`](file:///final-thesis/figures/ch04_results/table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv)
* **File Name**: `table_4_3b_master_annual_seasonal_volatility_regimes_summary.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/figure_4_2_annual_volatility_clusters.png`](file:///final-thesis/figures/ch04_results/figure_4_2_annual_volatility_clusters.png)
* **Operational Content**: Tabulates monthly passenger throughput, seat capacity, departure delays, cancellations, and coupled volatility across the 4 annual regimes.

### Asset: Day-of-Week Volatility Dynamics and Operational Archetypes
* **Source Data File**: [`final-thesis/figures/ch04_results/02_day_of_week_volatility_dynamics.png`](file:///final-thesis/figures/ch04_results/02_day_of_week_volatility_dynamics.png)
* **File Name**: `02_day_of_week_volatility_dynamics.png`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/figure_4_3_day_of_week_volatility_dynamics.png`](file:///final-thesis/figures/ch04_results/figure_4_3_day_of_week_volatility_dynamics.png)
* **Operational Content**: Visualizes arrival burstiness (CV), delay cascades, and throughput volume across all seven days of the week.

### Asset: Diurnal Hourly Volatility Clusters and Bimodal Peaks
* **Source Data File**: [`final-thesis/figures/ch04_results/03_diurnal_hourly_volatility_clusters_by_dow.png`](file:///final-thesis/figures/ch04_results/03_diurnal_hourly_volatility_clusters_by_dow.png)
* **File Name**: `03_diurnal_hourly_volatility_clusters_by_dow.png`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/figure_4_4_diurnal_hourly_volatility_clusters.png`](file:///final-thesis/figures/ch04_results/figure_4_4_diurnal_hourly_volatility_clusters.png)
* **Operational Content**: Heatmap and line cluster charts establishing the non-consecutive bimodal diurnal turbulence peaks (morning surge vs evening cascade).

---

# Appendix J: Candidate Predictive Models, Evaluation Metrics, and Holdout Benchmarks

> *Note on Thesis Cross-References*: This appendix compiles the certified empirical evaluation benchmarks across all three candidate models and baseline control evaluated against the 2025 out-of-time holdout dataset. It is referenced in **Chapter IV (Results)**, Section 4.4 (*Model Results and Evaluation*) and Section 4.4 (*Empirical Confirmation of Asymmetric Trade-Offs*); and in **Chapter V (Discussion)**, Section 5.3–5.5 (*Master Synthesis and Operational Recommendations*).

## J.1 The 3-Model Candidate Evaluation Suite and Baseline Control

To evaluate the research questions, the study establishes three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:

1. **Baseline Control Benchmark (Daily Persistence)**: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the identical hour 24 hours prior ($\hat{y}_t = y_{t-24}$). Serves as the non-parametric reference standard ($	ext{MASE} \equiv 1.000$).
2. **Model 1: Deterministic Flight Schedule Model (Operational Baseline)**: Convolves published airline flight schedules across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$). Requires zero historical training data, exhibits zero feedback latency, and provides a deterministic physics-based baseline.
3. **Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**: Decision-tree regressor trained across convolved flight schedules, 24 BTS OTP flight delay features, tactical cancellations, and airport interaction variables.
4. **Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**: Sequential two-stage model. Stage 1 captures scheduled flight bank cycles; Stage 2 predicts residual shocks using operational delay features coupled with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from checkpoint lanes.

## J.2 Certified 2025 Out-of-Time Holdout Benchmarks and Asymmetric Trade-Offs

Model performance was evaluated across the certified 2025 holdout dataset ($N = 3,222$ test complex-days; $77,328$ hourly observations) across three orthogonal evaluation dimensions:

* **Dimension 1: Robustness (Routine Operations)**:
  - *Baseline Control*: $R^2 = 0.382$, $\text{RMSE} = 345.8$ pax/hr, $\text{MAE} = 224.5$ pax/hr, $\text{MASE} = 1.000$, $\text{Bias} = +2.4$.
  - *Model 1 (Deterministic)*: $R^2 = 0.529$, $\text{RMSE} = 313.4$ pax/hr, $\text{MAE} = 212.1$ pax/hr, $\text{MASE} = 0.945$, $\text{Bias} = -42.1$.
  - *Model 2 (Supervised ML)*: $R^2 = 0.762$, $\text{RMSE} = 238.4$ pax/hr, $\text{MAE} = 154.2$ pax/hr, $\text{MASE} = 0.700$, $\text{Bias} = -18.4$.
  - *Model 3 (Dynamic Hybrid)*: $R^2 = 0.814$, $\text{RMSE} = 222.1$ pax/hr, $\text{MAE} = 142.8$ pax/hr, $\text{MASE} = 0.662$, $\text{Bias} = -8.5$.

* **Empirical Confirmation of Master Asymmetric Trade-Offs ($H_1$)**:
  1. *Model 3 wins Dimension 1 (Robustness)* with lowest overall error ($\text{RMSE} = 222.1$, $\text{MASE} = 0.662$), while Model 2 wins *Routine Pareto Efficiency* (achieving $\text{MASE} = 0.700$ with zero live checkpoint feedback latency).
  2. *Model 3 decisively wins Dimension 2 (Resilience Under IROPS)*: under severe disruption, Model 3 maintains a shock recovery multiplier $R_{\text{MASE}} = 1.05$ and time-to-recovery $\text{TTR} = 2.8$ hours. Pure ML (Model 2) fragilely collapses ($R_{\text{MASE}} = 2.14, \text{TTR} = 5.4$ h) due to the Empty Checkpoint Fallacy.
  3. *Model 1 decisively wins Dimension 3 (Generalizability)*: under zero-shot spatial transfer (EWR $\to$ LGA Terminal C without retraining), Model 1 achieves a Relative Transfer Ratio $\text{RTR} = 1.04$ and transfer penalty $\Delta\text{MASE} = +4.0\%$. Model 3 decisively fails spatial transfer ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$) due to decision tree terminal geometry overfitting.

## J.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Master Model Benchmark Matrix (2025 Holdout Evaluation)
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_10_master_model_benchmark_matrix.csv`](file:///final-thesis/figures/ch04_results/table_4_10_master_model_benchmark_matrix.csv)
* **File Name**: `table_4_10_master_model_benchmark_matrix.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx`](file:///final-thesis/results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx)
* **Operational Content**: Certified empirical benchmarks detailing R^2, RMSE, MAE, MASE, and Bias across Baseline Control, Model 1, Model 2, and Model 3 on the 2025 holdout.

### Asset: Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`](file:///final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv)
* **File Name**: `table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch05_discussion/figure_5_1_asymmetric_trade_off_triangle.png`](file:///final-thesis/figures/ch05_discussion/figure_5_1_asymmetric_trade_off_triangle.png)
* **Operational Content**: Certified empirical multi-pillar matrix evaluating Baseline Control, Model 1 (Deterministic), Model 2 (Supervised Machine Learning), and Model 3 (Dynamic Two-Stage Hybrid) across Dimension 1 (Robustness), Dimension 2 (Resilience), and Dimension 3 (Generalizability) on the 2025 out-of-time holdout dataset.

### Asset: Master Asymmetric Trade-Off Matrix and Decision Policy
* **Source Data File**: [`final-thesis/figures/ch05_discussion/table_5_4_master_asymmetric_trade_off_matrix.csv`](file:///final-thesis/figures/ch05_discussion/table_5_4_master_asymmetric_trade_off_matrix.csv)
* **File Name**: `table_5_4_master_asymmetric_trade_off_matrix.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch05_discussion/figure_5_1_asymmetric_trade_off_triangle.png`](file:///final-thesis/figures/ch05_discussion/figure_5_1_asymmetric_trade_off_triangle.png)
* **Operational Content**: Multi-dimensional evaluation matrix synthesizing Robustness (routine), Resilience (shocks), and Generalizability (transfer) confirming Hypothesis H1.

---

# Appendix K: The Values versus Volatility Operational Coupling Across Temporal Horizons

> *Note on Thesis Cross-References*: This appendix establishes the econometric proof for the Values versus Volatility operational coupling across intraday absolute, scale-free relative, and multi-day temporal horizons. It is referenced in **Chapter IV (Results)**, Section 4.4 (*The Values versus Volatility Operational Coupling*); and in **Chapter V (Discussion)**, Section 5.4 (*Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons*).

## K.1 Empirical Formulation of the Operational Coupling

A core theoretical finding of this research is the empirical confirmation of the **Values versus Volatility Operational Coupling**. In standard airport planning practice, forecasters rely on static volume levels ($y_t$) to project staffing needs. However, under heavy-traffic queuing principles (Kingman's formula), checkpoint delays and queue lengths scale quadratically with arrival volatility ($C_a^2$), not static volume.

To test this operational coupling, models were trained across three controlled feature representations:
1. *Feature Values Only*: Utilizing standard static operational metrics (raw scheduled seats, average delay minutes, total cancellations, taxi queue lengths).
2. *Feature Volatility Only*: Utilizing statistical dispersion metrics (flight departure delay standard deviation $\sigma_{\text{Delay}}$, delay burstiness $CV_{\text{delay}}$, schedule dispersion, 7-day rolling volatility).
3. *Combined Dual Representation*: Integrating both feature values and feature volatilities.

## K.2 Empirical Results Across Temporal Horizons

Evaluating the three feature representations across three distinct temporal horizons demonstrates the necessity of volatility features:

* **Horizon 1: Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**:
  - *Values Only*: Achieves $R^2 = 0.584$ ($\text{RMSE} = 310.2$ pax/hr). Raw flight volume provides a baseline schedule diurnal shape.
  - *Volatility Only*: Achieves $R^2 = 0.612$ ($\text{RMSE} = 295.4$ pax/hr).
  - *Combined Dual Representation*: Achieves champion $R^2 = 0.732$ ($\text{RMSE} = 252.1$ pax/hr), capturing both baseline diurnal volume and peak bank surge dispersion.

* **Horizon 2: Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}}$, burstiness ratio)**:
  - *Values Only*: Collapses to $R^2 = 0.089$ ($\text{RMSE} = 0.098$). Static volume features cannot capture dimensionless arrival burstiness.
  - *Volatility Only*: Achieves $R^2 = 0.448$ ($\text{RMSE} = 0.072$).
  - *Combined Dual Representation*: Reaches $R^2 = 0.485$ ($\text{RMSE} = 0.069$), demonstrating that arrival burstiness is intrinsically driven by schedule and delay volatility.

* **Horizon 3: Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day network turbulence)**:
  - *Values Only*: Completely collapses to negative explanatory power ($R^2 = -0.142$, $\text{RMSE} = 3,420$ pax/day). Static daily flight volumes completely fail to forecast multi-day network turbulence.
  - *Volatility Only*: Successfully forecasts multi-day turbulence ($R^2 = +0.312$, $\text{RMSE} = 2,650$ pax/day).
  - *Combined Dual Representation*: Achieves champion $R^2 = +0.385$ ($\text{RMSE} = 2,480$ pax/day).

These results confirm that static feature levels are fundamentally blind to multi-day network turbulence ($R^2 < 0$), whereas feature volatility metrics succeed ($R^2 > 0.31$).

## K.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: The Values versus Volatility Operational Coupling Empirical Regression Matrix
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv`](file:///final-thesis/figures/ch04_results/table_4_11_master_multi_pillar_hypothesis_evaluation_matrix.csv)
* **File Name**: `table_4_12_the_values_versus_volatility_paradigm_feature_space_regression_benchmark.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch02_lit_review/otp_and_tsa_volume_coupling.csv`](file:///final-thesis/figures/ch02_lit_review/otp_and_tsa_volume_coupling.csv)
* **Operational Content**: Compares explanatory power (R^2 and RMSE) across Values Only, Volatility Only, and Combined models across intraday absolute, scale-free CV, and 7-day rolling horizons.

### Asset: Landside-Airside Volatility Coupling and Flight Delay Dispersion
* **Source Data File**: [`final-thesis/figures/ch02_lit_review/otp_volatility.csv`](file:///final-thesis/figures/ch02_lit_review/otp_volatility.csv)
* **File Name**: `otp_volatility.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch02_lit_review/OTP volatility.png`](file:///final-thesis/figures/ch02_lit_review/OTP volatility.png)
* **Operational Content**: Documents the strong empirical correlation between checkpoint throughput volatility and flight departure delay dispersion (r = +0.4373, p < 0.05).

---

# Appendix L: Operational Disruption Dynamics, Lead-Lag Asynchrony, and Resilience Mechanics

> *Note on Thesis Cross-References*: This appendix details the behavioral mechanics of forecast failures during severe weather and the live error feedback remediation in the Dynamic Hybrid. It is referenced in **Chapter V (Discussion)**, Section 5.1 (*Spatial Architecture and Passenger Behavioral Dynamics: The Lead-Lag Asynchrony Mechanism*) and Section 5.3 (*Empirical Evaluation of Resilience Under Disruption: Resilience Mechanics and the Empty Checkpoint Fallacy*).

## L.1 The Lead-Lag Asynchrony Mechanism and the Delay Disconnect

Traditional airport planning models assume that when flights are delayed, passenger arrivals at security checkpoints shift backward by an identical duration. Empirical analysis reveals that this assumption is fundamentally flawed:

* **Strict Asymmetry of the Security Checkpoint**: Passengers enter security checkpoints strictly prior to departure. Once passengers clear TSA screening into the sterile gate area, subsequent flight delays do not pull them back through security.
* **The Morning vs. Evening Disruption Split**:
  - *Morning Disruptions ($05:00–10:00$)*: Flight delays announced while passengers are en route or already in airport lobbies produce immediate queue surges. Passengers proceed through security regardless of delays to access gate amenities.
  - *Evening Disruptions ($16:00–22:00$)*: Severe ground delay programs produce extensive airside gate holding. Checkpoint screening demand drops to structural minimums because passenger banks completed screening hours earlier.
* **The Lead-Lag Disconnect**: Checkpoint arrival volatility is strongly coupled with flight delay dispersion ($CV_{\text{delay}}: r = +0.4373, p < 0.05$), while raw delay minutes show zero correlation ($r = -0.062, p = 0.77$). Static flight delays do not translate into contemporaneous checkpoint queues.

## L.2 Resilience Mechanics and the Empty Checkpoint Fallacy

During severe convective disruptions, ground delay programs (GDP), and winter storm cancellations (Tier 3 IROPS), pure machine learning models (Model 2) experience catastrophic forecast collapse:

* **The Empty Checkpoint Fallacy**: When carriers announce extensive flight delays (e.g., departing flights pushed back 2 to 4 hours), decision trees trained on flight schedules project that screening demand should instantaneously drop to near zero. However, on the terminal floor, hundreds of ticketed passengers have already arrived, creating severe queue congestion in front of closed screening lanes. Model 2's error multiplier spikes to $R_{\text{MASE}} = 2.14$ (a $114\%$ error explosion), and its time-to-recovery extends to $5.4$ hours.
* **Model 3 Live Feedback Remediation**: Model 3 prevents this failure mode by coupling scheduled flight banks with real-time 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from checkpoint lanes. When physical arrivals diverge from flight schedules during severe weather, the recursive feedback term immediately overrides the flight schedule regressor. As a result, Model 3 achieves Decisive Shock Resilience:
  - Shock Recovery Multiplier: $R_{\text{MASE}} = 1.05$ (stable performance, $R \approx 1.00$).
  - Shock Accuracy: $\text{MASE}_{\text{shock}} = 0.694$ (beating all models).
  - Time-to-Recovery: $\text{TTR} = 2.8$ hours (rapid error recovery, $\text{TTR} < 4.0$ h).

## L.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Evaluation Dimension 2: Resilience and Shock Performance Under Severe Disruption
* **Source Data File**: [`final-thesis/figures/ch05_discussion/table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv`](file:///final-thesis/figures/ch05_discussion/table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv)
* **File Name**: `table_5_2_evaluation_dimension_2_resilience_and_shock_performance.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx`](file:///final-thesis/results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx)
* **Operational Content**: Details MASE under nominal, routine, and shock regimes, shock error multipliers (R_MASE), and hours to recovery (TTR) across candidate models.

### Asset: Empirical Lead-Lag Transfer Dynamics Across Checkpoint Lead Horizons
* **Source Data File**: [`final-thesis/figures/ch04_results/table_4_9_empirical_lead_lag_transfer_dynamics.csv`](file:///final-thesis/figures/ch04_results/table_4_9_empirical_lead_lag_transfer_dynamics.csv)
* **File Name**: `table_4_9_empirical_lead_lag_transfer_dynamics.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch04_results/figure_4_5_lead_lag_convolution_curves.png`](file:///final-thesis/figures/ch04_results/figure_4_5_lead_lag_convolution_curves.png)
* **Operational Content**: Presents regression coefficients confirming that t+1 and t+2 flight banks explain 90.0% of screening arrivals, validating the physical lead-lag mechanism.

---

# Appendix M: Dual-Track Operational Decision Playbook and Volatility-Buffered Dynamic Lane Staffing

> *Note on Thesis Cross-References*: This appendix translates the empirical modeling findings into an actionable operational decision playbook, regime-switched gated inference engine, and dynamic lane staffing rules. It is referenced in **Chapter V (Discussion)**, Section 5.5 (*Implications and Recommendations for Predictive Forecasting in Airport Operations: Real-World Operational Application*) and Section 5.6 (*Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion*).

## M.1 The Dual-Track Operational Model Selection Policy

Because no single predictive architecture dominates across all operational dimensions (Hypothesis $H_1$), Airport Operations Centers (AOC) and TSA Joint Operations Centers (JOC) should deploy a **Dual-Track Operational Decision Framework**:

* **Track A: In-Sample Operational Checkpoint Forecasting & Severe Disruption Resilience**:
  - *Recommended Model*: **Model 3 (Dynamic Two-Stage Hybrid Model)**.
  - *Operational Deployment*: Deployed across established airport screening complexes equipped with live automated queue sensor feeds (e.g., LiDAR, computer vision, Bluetooth wait-time sensors).
  - *Performance Justification*: Delivers lowest routine error ($\text{RMSE} = 222.1$ pax/hr, $\text{MASE} = 0.662$) and decisive shock resilience ($R_{\text{MASE}} = 1.05, \text{TTR} = 2.8$ h), completely eliminating the Empty Checkpoint Fallacy during convective ground delay programs.
  - *Operational Fallback*: Under routine baseline operations (Delays $< 15$ min, 0 cancels), **Model 2 (Supervised Machine Learning)** serves as an efficient fallback, achieving $\text{MASE} = 0.700$ with zero live sensor compute latency.

* **Track B: Zero-Shot Spatial Transfer, Master Planning & Facility Expansions**:
  - *Recommended Model*: **Model 1 (Deterministic Flight Schedule Model)**.
  - *Operational Deployment*: Deployed for long-range terminal master planning, seasonal schedule evaluation, and newly constructed airport concourses where zero live queue sensor infrastructure exists.
  - *Performance Justification*: Achieves champion zero-shot spatial transferability ($\text{RTR} = 1.04$, transfer error shift $\Delta\text{MASE} = +4.0\%$, transfer penalty $4.2\%$) because flight schedule convolution relies strictly on universal physical passenger show-up curves rather than overfitted local terminal geometries. Model 3 decisively fails zero-shot transfer ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$) and must not be transferred without local retraining.

## M.2 Volatility-Buffered Dynamic Lane Dimensioning (The Staffing Safety Cushion)

Under Kingman's heavy-traffic queuing formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), opening screening lanes based solely on expected average passenger volume ($\hat{\mu}_t$) leads to catastrophic queue blowout during peak banks because traffic intensity approaches capacity ($\rho \to 1.0$).

To operationalize throughput volatility forecasts into dynamic lane staffing, the study formalizes the **Volatility-Buffered Lane Dimensioning Rule (EQ-20)**:
$$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$
where:
* $c(t)$ is the recommended integer number of active parallel screening lanes at hour $t$.
* $\hat{\mu}_t$ is the forecasted mean passenger arrival demand rate (pax/hr).
* $\hat{\sigma}_{\text{TSA}, t}$ is the forecasted arrival volatility (pax/hr dispersion).
* $z_q$ is the service safety factor corresponding to target queue clearance reliability (e.g., $z_q = 1.645$ for a $95\%$ service reliability level).
* $\mu_{\text{lane}}$ is the nominal screening throughput capacity per open lane (standard lane: $\approx 180$ pax/lane-hr; PreCheck lane: $\approx 250$ pax/lane-hr).

By buffering lane allocations with forecasted volatility ($\hat{\sigma}_{\text{TSA}}$), checkpoint operations establish a dynamic *Staffing Safety Cushion*, absorbing bursty passenger arrival waves and preventing traffic intensity from breaching the critical tipping point ($\rho \ge 0.85$).

## M.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: Dual-Track Operational Model Selection Policy Specification
* **Source Data File**: [`final-thesis/figures/ch05_discussion/dual_track_model_selection_policy.csv`](file:///final-thesis/figures/ch05_discussion/dual_track_model_selection_policy.csv)
* **File Name**: `dual_track_model_selection_policy.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch05_discussion/table_5_4_master_asymmetric_trade_off_matrix.csv`](file:///final-thesis/figures/ch05_discussion/table_5_4_master_asymmetric_trade_off_matrix.csv)
* **Operational Content**: Defines Track A (in-sample operations) vs Track B (spatial transfer) deployment rules, data requirements, and model recommendations.

### Asset: Evaluation Dimension 1: Routine Operational Accuracy (Robustness)
* **Source Data File**: [`final-thesis/figures/ch05_discussion/table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv`](file:///final-thesis/figures/ch05_discussion/table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv)
* **File Name**: `table_5_1_evaluation_dimension_1_routine_operational_accuracy.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/ch05_discussion/table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv`](file:///final-thesis/figures/ch05_discussion/table_5_3_evaluation_dimension_3_generalizability_and_cross_airport_transfer.csv)
* **Operational Content**: Tabulates RMSE, MAE, MASE, and Bias across Baseline Control, Model 1, Model 2, and Model 3 under nominal on-time baseline operations.

---

# Appendix N: Archival Data Storage Infrastructure, Directory Hierarchy, and Screenshot Catalog

> *Note on Thesis Cross-References*: This appendix documents the persistent cloud storage backup manifest, repository organization, and visual evidence screenshot catalog. It is referenced in **Chapter III (Methodology)**, Section 3.1 (*Apparatus and Materials: Archival Storage and Reproducibility Environment*) and Section 3.3 (*Sources of Data*).

## N.1 Archival Storage and Directory Organization

To ensure full scientific reproducibility, auditability, and data integrity, all raw and processed aviation data feeds, analytical code, and manuscript assets are preserved in a standardized directory hierarchy synchronized between persistent cloud storage (OneDrive) and local development paths:

* `00_Raw_Ingested_Federal_Data/`: Preserves raw upstream data feeds (TSA FOIA hourly screening logs, BTS Form 234 flight movements, BTS Form 41 T-100 domestic segments, BTS DB1B ticket coupon archives; $67,222,828$ raw records; $7.12$ GB staging).
* `01_Staging_ETL_DuckDB/`: Houses vectorized DuckDB pipelines, Star Schema dimension tables (`dim_date`, `dim_airport`, `dim_airline`, `dim_checkpoint`), and data hygiene quarantine tables.
* `02_Conformed_Star_Schema_Parquet/`: Stores final partitioned Apache Parquet datasets ($42,062,039$ conformed records).
* `results/manuscript_tables/`: Contains conformed CSV files for all 16 empirical manuscript tables.
* `results/tables/`: Houses companion analytical tables and equation registries.
* `figures/`: Structured into chapter-specific subdirectories containing publication-ready visual charts, CSV datasets, and multi-tab Excel workbooks (`figures/ch01_intro/`, `figures/ch02_lit_review/`, `figures/ch03_methodology/`, `figures/ch04_results/`, `figures/ch05_discussion/`, `figures/04_Appendix_and_Reference/`).
* `thesis_docs/manuscripts/`: Stores full thesis manuscripts, chapter drafts, acronym lists, and version-controlled review documents.

## N.2 Visual Evidence Diagrams and Screenshot Layout Catalog

To provide complete forensic provenance, 30 high-resolution visual evidence screenshots capturing data schemas, queuing curves, pipeline progressions, and econometric models are cataloged across four analytical subdirectories:

1. `figures/ch01_intro/`: Data sample profile census, inclusion of top 25 network approach, models and tests comparison.
2. `figures/ch02_lit_review/`: Clustering and connecting paradox, OTP flight delay volatility, OTP vs. TSA volume coupling, model walkthrough architecture, passenger stochastic arrival parameters.
3. `figures/ch03_methodology/`: Four-tier filtering funnel progression, combined data threats and remediation matrix, post-pandemic demarcation justification, power of 9 airports factorial design, physical transfer lead-lag timeline, evaluation metric definitions, TSA and T-100 schema DDL architectures.
4. `figures/04_Appendix_and_Reference/`: BTS DB1B table hierarchy, 9-airport data profile, database profiles, dataset breakdown, backups organization, diagrams and screenshot layout catalog, methodological assumptions matrix.

## N.Ref Referenced Tabular Datasets and Visual Evidence Assets

The following data tables and visual exhibits substantiate the empirical findings in this appendix. Full datasets are archived in the `final-thesis/figures/` repository and can be directly accessed at the locations specified below:

### Asset: OneDrive Archival Backup Directory Structure and Preserved Contents
* **Source Data File**: [`final-thesis/figures/04_Appendix_and_Reference/backups_organization.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/backups_organization.csv)
* **File Name**: `backups_organization.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/Backups organization.png`](file:///final-thesis/figures/04_Appendix_and_Reference/Backups organization.png)
* **Operational Content**: Full inventory of persistent cloud backup directories, storage hierarchy levels, and preserved datasets.

### Asset: Visual Evidence Diagrams and Screenshot Layout Catalog
* **Source Data File**: [`final-thesis/figures/04_Appendix_and_Reference/diagrams_and_screenshot_layout.csv`](file:///final-thesis/figures/04_Appendix_and_Reference/diagrams_and_screenshot_layout.csv)
* **File Name**: `diagrams_and_screenshot_layout.csv`
* **Companion Exhibit / Workbook**: [`final-thesis/figures/04_Appendix_and_Reference/Diagrams and Screenshot Layout.png`](file:///final-thesis/figures/04_Appendix_and_Reference/Diagrams and Screenshot Layout.png)
* **Operational Content**: Complete catalog of all 30 high-resolution visual evidence screenshots across the analytical subdirectories.

---
