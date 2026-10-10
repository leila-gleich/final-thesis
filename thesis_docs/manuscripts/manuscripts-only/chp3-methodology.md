# Chapter III: Methodology

This chapter details the methodological architecture and empirical research design used to evaluate predictive techniques for modeling airport passenger security screening throughput volatility. Commercial airport landside subsystems—specifically ticketing halls, Transportation Security Administration (TSA) security checkpoints, and departure gate hold-rooms—operate as a tightly coupled stochastic queuing network (De Neufville & Odoni, 2014). To evaluate how different analytical paradigms perform within this volatile operating environment, this study systematically benchmarks deterministic flight schedule baselines, supervised machine learning decision trees, and dynamic two-stage hybrid models against an empirical baseline control.

To ensure clarity, rigor, and academic conciseness, the methodology is structured across eight core sections. Section 3.1 traces the chronological evolution of predictive modeling in airport operations, demonstrating how analytical paradigms transitioned from static flight schedule lookups to supervised machine learning and culminated in the dynamic two-stage hybrid architecture, while establishing the three-pillar evaluation triad (Robustness, Resilience, and Generalizability). Section 3.2 outlines the research design and sequential procedural phases. Section 3.3 describes the computational apparatus and materials. Section 3.4 details the sample framework and the four-tiered purposive filtering pipeline that isolates dedicated single-carrier screening facilities. Section 3.5 identifies the primary federal data sources and explains the connecting passenger deflator. Section 3.6 addresses research validity and explains the rationale for modeling throughput volatility rather than raw volume. Section 3.7 summarizes data treatment, while Section 3.8 provides an extensive drill-down on the COVID-19 catalyst, post-pandemic operational equilibrium, and temporal demarcation protocols.

## Research Approach: Chronological Evolution of Predictive Paradigms

Understanding how predictive analytics can optimize airport security screening demand requires examining the historical trajectory of forecasting methodologies in commercial aviation. Over recent decades, terminal demand modeling has evolved through four distinct analytical stages, reflecting an ongoing effort to balance structural schedule fidelity against live operational responsiveness.

### Phase 1: Deterministic Flight Schedules and Fixed Passenger Lead Times
The foundational starting point for airport terminal planning relies on published airline flight schedules. Under this deterministic approach, planners take published aircraft departure times and shift them forward by fixed lead times based on empirical traveler arrival distributions—most notably the lognormal passenger show-up curves formalized in Airport Cooperative Research Program (ACRP) Report 40 (*Airport Passenger Terminal Planning and Design*; Transportation Research Board [TRB], 2010). Because domestic commercial passengers typically arrive at the terminal 90 to 120 minutes prior to scheduled departure, convolving scheduled departing flight seats across lead arrival horizons ($t+1, t+2, t+3$) produces an expected passenger demand curve that mirrors planned flight bank rhythms. 

The conceptual strength of this deterministic approach lies in its intuitive transparency: it requires no statistical training, relies exclusively on publicly known airline timetables, and easily transfers across airport facilities. However, its operational limitation is substantial: deterministic schedule convolution operates under a rigid clear-weather assumption, completely blind to day-of-operations delays, runway taxi queues, and tactical cancellations. When flights are held at gates or ground-stopped, deterministic models continue forecasting passenger arrival waves based on outdated schedules, failing to reflect actual terminal conditions.

### Phase 2: Classical Queuing Theory and Statistical Time-Series Forecasting
To account for stochastic variability and waiting lines, transportation researchers integrated classical queuing theory (such as Poisson and Non-Homogeneous Poisson processes) and statistical time-series models (such as ARIMA and Seasonal ARIMA). Linear time-series formulations effectively capture the pronounced diurnal (24-hour) and weekly (168-hour) cyclical cadences of commercial airport operations, estimating future passenger throughput based on historical recurring patterns and seasonal autoregressive lags.

While linear time-series models provide computationally lightweight forecasts with established statistical properties, their operational utility degrades rapidly during systemic disruptions. Classical queuing models assume stationary arrival rates and independent passenger arrivals, assumptions that are severely violated by clustered airline flight banks and airside connecting passenger transfers. Furthermore, linear time-series models cannot accommodate sudden non-linear flight delay cascades: during major storm events or air traffic control ground delay programs, historical autoregressive lags project phantom passenger demand based on past patterns, missing the operational reality that flights have been delayed or cancelled.

### Phase 3: Supervised Machine Learning and Decision-Tree Ensembles
To move beyond linear assumptions, the aviation forecasting literature embraced data-driven machine learning, particularly supervised decision-tree ensembles such as Gradient-Boosted Decision Trees (GBM). Unlike linear statistical models, tree-based regressors can ingest multi-dimensional operational feeds from the Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) database, learning complex non-linear interactions among flight departure delays, tactical cancellations, runway taxi-out queues, aircraft seating capacities, and route load factors.

Supervised machine learning dramatically improves routine forecasting accuracy by discovering multi-variable operational rules (for instance, learning how an increase in departure delay dispersion dampens passenger arrivals in subsequent hours). Nevertheless, pure machine learning introduces a dangerous operational vulnerability during severe disruptions: the "Empty Checkpoint Fallacy." When convective thunderstorms or winter blizzards induce cascading gate holds and rolling ground delays, the machine learning model observes delayed departure timestamps and erroneously predicts an immediate collapse in security screening demand. In reality, ticketed passengers arrived at the terminal according to their original flight schedules and remain stranded in terminal lobbies and security lines. By predicting an empty checkpoint during gate delays, static machine learning models recommend reducing screening lane staffing precisely when terminal crowding reaches its peak.

### Phase 4: Culmination in the Dynamic Two-Stage Hybrid Architecture
To overcome the vulnerabilities of both deterministic schedules and static machine learning, modern transportation literature has converged toward dynamic hybrid architectures that synthesize the physical stability of flight schedules with data-driven adaptability and real-time operational feedback. This study culminates in a Dynamic Two-Stage Hybrid Model designed specifically for high-stakes airport security environments:
- **Stage 1 (Operational Schedule Foundation)**: A deterministic operational model captures the macro flight schedule structure, convolving published departure banks across empirical ACRP Report 40 passenger show-up curves and deflating seat capacities using ticket survey connecting ratios to isolate true local originating passengers.
- **Stage 2 (Non-Linear Residual Estimation)**: A supervised decision tree predicts operational residual adjustments caused by airside delays, tactical cancellations, and surface taxi queues, capturing non-linear flight performance variations without discarding the structural schedule base.
- **Dynamic 1-Step Error Innovation Feedback ($e_{t-1}$)**: A recursive error-correction loop continuously ingests actual passenger screening throughput from the preceding hour ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). If terminal screening counts exceed what flight schedules and delay indicators predicted, the feedback loop immediately alerts the model that passengers are accumulating landside, adjusting the forecast upward in real time.

By coupling structural flight bank geometry with live checkpoint floor feedback, the dynamic hybrid model eliminates the Empty Checkpoint Fallacy, provides rapid recovery following severe shocks, and ensures continuous operational alignment with live terminal conditions.

### The Multi-Dimensional Evaluation Triad
Rather than evaluating models using a single average point-accuracy metric (such as clear-weather RMSE or MAPE), this study establishes an operational evaluation triad evaluating models across three orthogonal dimensions:
1. **Robustness (Routine Operational Accuracy)**: Consistency and low forecast error under nominal on-time operations and everyday flight bank churn, minimizing routine error and meeting established scaled error targets ($MASE_{\text{routine}} < 0.700$).
2. **Resilience (Performance Under Severe Disruption)**: Error containment, resistance to demand collapse, and rapid Time-to-Recovery ($TTR < 4.0\text{ hours}$) following acute operational shocks such as severe convective storms, ground delay programs, and winter freezes.
3. **Generalizability (Cross-Airport Zero-Shot Portability)**: The capability of a model calibrated at one facility to transfer zero-shot across divergent terminal geometries and airline hub networks without requiring local historical retraining ($RTR \approx 1.00, \Delta MASE \le 10.0\%$).

All mathematical formulas, queuing equations, and statistical test derivations are compiled in the appendix (Appendix D, Appendix E, and Appendix L).

## Design and Procedures

This investigation follows an exploratory, quantitative, non-experimental design executed across four sequential phases:
- **Phase 1: Ingestion and Harmonization (ETL)**: Compiling, cleansing, and relationally joining multi-source federal datasets spanning 2019 to 2025 across common spatial and temporal dimensions.
- **Phase 2: Model Configuration and Training**: Calibrating the candidate modeling suite—the Baseline Control (daily persistence), Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model)—across the post-pandemic development partition.
- **Phase 3: Out-of-Time Holdout Execution**: Benchmarking all candidate models against the untouched full-year 2025 holdout dataset under nominal, routine, and disrupted operational regimes.
- **Phase 4: Comparative Evaluation and Strategic Synthesis**: Assessing models across the evaluation triad to determine asymmetric trade-offs, evaluating the Values versus Volatility paradigm, and formulating an operational decision playbook.

## Apparatus and Materials

To execute high-volume data engineering and predictive modeling across tens of millions of records, this study utilizes:
- **Google Antigravity & Python Analytics Stack**: The primary computational environment for automated data ingestion, spatial key resolution, relational joins, and machine learning model training.
- **Vega High-Performance Computing (HPC) Cluster**: The institutional computing environment deployed for large-scale iterative data processing, hyperparameter tuning, and cross-airport transfer evaluations.
- **Persistent Cloud Data Warehouse**: Secure, version-controlled cloud storage maintaining complete conformed master datasets, relational lookup dimensions, and audit logs to ensure scientific reproducibility.

## Sample and Four-Tiered Purposive Filtering

The candidate sampling universe comprises commercial airfields within the contiguous United States. To systematically isolate the direct relationship connecting airline flight operations to landside checkpoint demand, the dataset was screened through a four-tiered purposive filtering pipeline:
- **Tier 1 (Macro Filter - Scale and Congestion)**: Focuses on the Top 25 U.S. commercial airfields by passenger enplanements (capturing 67.2% of nationwide domestic operations). Regional airfields operate with low traffic intensity, preventing queue formation; Top 25 hubs routinely reach screening saturation, generating the empirical queue dynamics necessary to train congestion-aware models.
- **Tier 2 (Meso Filter - Airline Symmetry and Invariance)**: Narrows candidate airfields to 14 hubs operating concurrent mainline domestic services by American Airlines, Delta Air Lines, and United Airlines under identical regional weather and airspace conditions, while excluding Southwest Airlines due to its distinctive bimodal passenger arrival timing.
- **Tier 3 (Micro Filter - Checkpoint Carrier Exclusivity)**: Restricts analysis to terminal complexes where screening checkpoints exclusively serve a single carrier ($P(\text{Carrier} = j^* \mid \text{Checkpoint}) = 1.0$). In shared terminals, concurrent flight banks create severe multi-carrier schedule collinearity; dedicated checkpoints eliminate passenger mixing and isolate carrier-specific arrival waves.
- **Tier 4 (Balanced Factorial Cohort)**: Finalizes a balanced 9-airport experimental cohort across 12 carrier-exclusive screening complexes (exactly four dedicated facilities each for American, Delta, and United across four distinct terminal layout archetypes: BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL).

Full architectural specifications and filtering criteria are detailed in Appendix I.

## Sources of the Data

Empirical data was compiled from four primary authorized federal reporting repositories covering 2019 to 2025:
1. **TSA FOIA Hourly Checkpoint Screening Logs**: Department of Homeland Security disclosures reporting hourly passenger screening counts disaggregated by physical screening lane.
2. **BTS On-Time Flight Performance (Form 234)**: Flight-by-flight domestic departure records tracking scheduled and actual pushback times, departure delays, taxi-out durations, tactical cancellations, and causal delay attributions.
3. **BTS Form 41 Schedule T-100 Segment Data**: Monthly carrier-route records providing available departing aircraft seats, transported revenue passengers, and route load factors.
4. **BTS DB1B / DB1C Origin-Destination Ticket Surveys**: A 10% randomized sample of airline ticket coupons detailing passenger itineraries and connecting transfer ratios.

### The Connecting Passenger Deflator (The Hub Disconnect)
A critical operational challenge in airport demand modeling is that connecting passengers in hub-and-spoke networks transfer between aircraft airside, never entering landside ticketing lobbies or passing through security screening checkpoints. At major connecting fortress hubs (such as Charlotte, Atlanta, or Dallas/Fort Worth), 50% to 76% of passengers are airside transfers. Treating total departing aircraft seats as security demand overestimates checkpoint volume by more than two-fold. By multiplying flight seats by $(1 - \text{ConnectingRatio})$ derived from quarterly DB1B ticket surveys, the methodology isolates true local originating passenger demand.

## Validity and Operational Volatility Formulation

To protect internal, construct, and statistical conclusion validity:
- **Focus on Throughput Volatility Rather Than Volume**: Grounded in heavy-traffic queuing principles (Kingman's formula), checkpoint queues and passenger delays scale non-linearly with passenger arrival burstiness and volatility ($C_a^2$), not average volume. The study therefore models diurnal throughput dispersion ($\sigma_{\text{TSA, hr}}$) and scale-free relative volatility ($CV_{\text{TSA, hr}}$).
- **Prevention of Lookahead Bias**: Realized flight delays are unknown until flights push back. The model strictly utilizes prior-hour delays ($t-1$) and pre-scheduled departure banks, preserving operational information availability.
- **Operational Buffers Between Partitions**: Strict 7-day operational purge buffers are enforced between training, validation, and holdout partitions to prevent multi-day storm cascades from leaking across boundaries.

Detailed mathematical formulas for volatility targets are compiled in Appendix E.

## Treatment of the Data

Data preparation followed a sequential Extract, Transform, Load (ETL) pipeline:
- Standardizing all timestamps to local solar operational airport time.
- Performing automated spatial entity resolution to map checkpoint strings and isolate corrupted records to a dedicated null surrogate key, preventing the creation of distorted demand baselines.
- Preserving scheduled overnight checkpoint closures (00:00 to 03:59) as true operational structural zeros rather than imputing artificial volume.
- Separating advance cancellations (>24 hours prior) from tactical cancellations (<2 hours prior), reflecting the operational reality that booked passengers had already completed security screening before same-day cancellations occurred.
- Convolving scheduled flight departure banks across empirical ACRP Report 40 passenger show-up curves and weighting by route load factors to generate conformed feature stores.

Complete ETL specifications and data hygiene protocols are detailed in Appendix K.

## The COVID-19 Catalyst and Post-Pandemic Demarcation

The COVID-19 pandemic represents the definitive empirical catalyst that disrupted commercial aviation operations and underscored the necessity of this research. The pandemic produced unprecedented operational shocks: nationwide passenger screening volume plummeted by more than 90% in spring 2020, followed by a multi-year recovery characterized by erratic business travel demand, altered booking curves, and heightened operational volatility. These structural disruptions permanently invalidated legacy forecasting models calibrated on undisturbed pre-pandemic averages, demonstrating that clear-weather historical accuracy is fundamentally insufficient for volatile airport operating environments.

### The Post-Pandemic Operational Equilibrium Approach
To ensure econometric validity and prevent transient historic anomalies from skewing predictive models, this study established the post-pandemic operational equilibrium beginning **May 1, 2022**. This demarcation point was determined through rigorous structural break analysis, variance convergence monitoring, and regulatory milestones:
1. **Federal Transit Mask Mandate Vacatur**: The nationwide judicial vacatur of federal transportation mask requirements on April 18, 2022 restored unconstrained traveler behavior across commercial aviation. By May 1, 2022, airline passenger load factors rebounded to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stabilization**: During the acute pandemic period (2020–2021), airline flight cancellations and travel restrictions produced an artificial correlation between scheduled flights and checkpoint throughput ($r = 0.607, R^2 = 36.85\%$). In the post-May 2022 operating environment, this relationship stabilized to an equilibrium level ($r = 0.553, R^2 = 30.61\%$), reflecting normalized booking patterns and passenger show-up behaviors.

### Development and Out-of-Time Partitioning Architecture
The May 1, 2022 demarcation establishes a 44-month post-pandemic longitudinal window spanning May 1, 2022 through December 31, 2025. This window is partitioned into:
- **Training Partition**: May 1, 2022 to December 31, 2023 (20 months; 122,847 hourly observations across the 9-airport complex cohort), capturing seasonal cycles and operational rhythms.
- **Validation Partition**: January 1, 2024 to December 31, 2024 (12 months; 72,723 hourly observations), strictly reserved for model calibration and hyperparameter tuning.
- **Out-of-Time Holdout Partition**: January 1, 2025 to December 31, 2025 (12 months; 72,053 complex-level screening hours across 3,222 airport-days), kept untouched for final out-of-time evaluation.

A 7-day operational purge buffer between partitions ensures that multi-day storm cascades and delay backlogs do not leak across evaluation boundaries. Complete statistical verification and CUSUM structural break audits are documented in Appendix G.
