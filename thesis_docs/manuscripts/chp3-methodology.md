# Chapter III: Methodology

This chapter details the approach and analytical framework to evaluate and optimize passenger flow forecasting, specifically at airport security checkpoints. Commercial airport landside subsystems—ticketing lobbies, Transportation Security Administration (TSA) security checkpoints, and boarding concourses—operate as a tightly coupled stochastic queuing network capable of absorbing dynamic, schedule-driven variability (De Neufville & Odoni, 2014). To evaluate how predictive models navigate this operational complexity, this investigation systematically compares deterministic flight schedule baselines, supervised machine learning decision trees, and dynamic two-stage hybrid architectures against an empirical daily persistence control.

To provide a structural roadmap for this investigation, the methodology is organized into five major sections. Section 1 (Research Approach) establishes the theoretical queuing framework, core research variables, formal hypotheses, sequential procedural design phases, candidate predictive model architectures, and technical computational apparatus. Section 2 (Sample) details the multi-tiered macro and micro sampling frameworks, carrier exclusivity isolation criteria, four-tiered purposive filtering pipeline, and the resulting balanced nine-airport experimental cohort. Section 3 (Sources of the Data) identifies the primary authorized federal reporting repositories supplying the conformed longitudinal datasets. Section 4 (Validity) addresses internal, construct, and statistical conclusion validity threats, formalizing the mathematical formulations of passenger throughput volatility. Finally, Section 5 (Treatment of Data) details the sequential data pipeline used to ingest, clean, standardize, feature-engineer, and load the multi-source analytical warehouse.

## Section 1: Research Approach

### Theoretical Framework & Stochastic Queuing Principles

The study uses an exploratory, sequential, quantitative design to systematically assess the predictive accuracy and operational utility of distinct forecasting approaches for passenger flow forecasting at airport security checkpoints. While this study evaluates a broad range of frameworks—including static deterministic baselines—it asserts that to truly optimize checkpoint flows, terminal subsystems (i.e., check-in, security screening, and boarding concourses) must ultimately be treated as a stochastic queuing network capable of absorbing dynamic, schedule-driven variability (De Neufville & Odoni, 2014).

Under heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993; Allen-Cunneen formula for $G/G/s$ queue facilities), expected queue wait times ($W_{q}$) and queue backlogs escalate not merely with average passenger arrivals ($\lambda$), but linearly with the **squared coefficient of variation of arrival times (**$C_{a}^{2}$**)**:

$W_{q}\approx \left(\frac{\rho ^{\sqrt{2\left(s+1\right)}-1}}{s\left(1-\rho \right)}\right)\left(\frac{C_{a}^{2}+C_{s}^{2}}{2}\right)\frac{1}{\mu }$

where $\rho =\frac{\lambda }{s\mu }$ represents checkpoint utilization. As screening lanes approach saturation ($\rho \to 1.0$), arrival volatility ($C_{a}^{2}$) generates acute queue spikes, lane starvation, and severe passenger processing delays that propagate downline into delayed aircraft boarding and gate pushback holds ($r=+0.4375,p<0.05$).

The primary objective is a rigorous comparison of three candidate model families evaluated against an empirical baseline control:

**Baseline Control**: Diurnal Volatility Naive Persistence Benchmark ($Vol^{^}_{t}=Vol_{t-24}$, non-parametric $MASE\equiv 1.000$).

**Model 1 (Deterministic Flight Schedule Model)**: Deterministic Operational Baseline convolving scheduled airline flight banks across empirical ACRP Report 40 passenger show-up curves ($t+1,t+2,t+3$).

**Model 2 (Supervised Machine Learning Model)**: Automated decision-tree regressor incorporating flight schedule dispersion and 24 BTS OTP operational attributes (delays, cancellations, taxi queues).

**Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential two-stage model coupling recurring schedule cycles with live 1-step error innovation feedback ($e_{t-1}=y_{t-1}-\hat{y}_{t-1}$) from the checkpoint floor.

Figure 1*Forecasting Model Family Comparison*

*Figure 1: Forecasting Model Family Comparison*

The predictive capabilities of each model configuration focus on three core performance measures: robustness, resilience, and generalizability. In this investigation:

**Robustness**: Refers to consistency and precision under nominal on-time operating conditions and routine daily operations.

**Resilience**: Refers to stability, error boundedness, and speed of recovery after severe exogenous operational disruptions.

**Generalizability**: Refers to performance across different airports or terminal layouts under zero-shot spatial transfer without local retraining.

### Core Research Variables

**Independent Variables**: Scheduled flight departures, actual flight performance data (departure delays, taxi-out queues, tactical cancellations), terminal structure categories, and origin-and-destination passenger ratios.

**Dependent Variables**: Volatility of TSA security checkpoint passenger throughput across multiple operational horizons:

*Intraday Diurnal Absolute Dispersion (*$\sigma _{TSA, hr}$*)*: Standard deviation across the 24 hours of calendar day $d$ (passengers per hour).

*Intraday Scale-Free Relative Volatility (*$CV_{TSA, hr}=\sigma /\mu$*)*: Scale-free arrival burstiness normalized across small versus mega checkpoints (dimensionless).

*Multi-Day Temporal Rolling Volatility (*$\sigma _{TSA, 7d}$*)*: Rolling 7-day standard deviation capturing network turbulence (passengers per day).

Checkpoint queue wait times and bottleneck formation rates.

**Secondary Outcome**: Comparative predictive model performance across the candidate modeling suite.

### Research Hypotheses

Distinct modeling frameworks and hybrid combinations thereof will exhibit asymmetric performance strengths across robustness, resilience, and generalizability. Probabilistic and supervised machine learning models are expected to outperform deterministic baselines under highly variable routine demand conditions, while dynamic hybrid models will perform better under disruption scenarios by combining operational system structure with real-time checkpoint error feedback.

**Core Research Hypothesis (**$H_{1}$** - Master Asymmetric Trade-Off Hypothesis)**: Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability). Rather, each modeling paradigm exhibits distinct operational strengths and stark asymmetric trade-offs:

**Dimension 1: Robustness (Routine Operations Target: Lowest **$RMSE_{routine}$** and **$MASE_{routine}<0.700$**)**:

*Hypothesis *$H_{1A}$: Under nominal operating conditions ($DepDelay<15 min$, zero cancellations), the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) will successfully achieve the robustness target ($MASE_{routine}<0.700$) by capturing non-linear passenger show-up and flight timing interactions, whereas the Naive Baseline Control and Deterministic Flight Schedule Model (Model 1) will fail the robustness threshold ($MASE\ge 0.94$). Machine learning (Model 2) will deliver a computationally lightweight, Pareto-efficient routine solution with zero feedback compute latency.

**Dimension 2: Resilience (Severe Disruption Target: Recovery Multiplier **$R_{RMSE}\approx 1.00$**, Lowest **$MASE_{shock}$**, and **$TTR<4.0 hours$**)**:

*Hypothesis *$H_{1B}$: Under severe operational disruptions ($DepDelay\ge 45 min$ or cancellations $\ge 5$), the Dynamic Two-Stage Hybrid Model (Model 3) will be the sole architecture to satisfy the resilience target ($R_{RMSE}\approx 1.00,R_{MASE}\approx 1.00,TTR<4.0 h$) due to live 1-step error innovation feedback ($e_{t-1}$). Pure machine learning (Model 2) will suffer severe performance degradation ($R\ge 2.0$) due to the Empty Checkpoint Fallacy (failing to recognize stranded passenger crowds waiting in the concourse), while deterministic schedules (Model 1) will remain blind to downstream delay cascades.

**Dimension 3: Generalizability (Zero-Shot Spatial Transfer Target: Relative Transfer Ratio **$RTR\approx 1.00$** and **$\Delta MASE_{transfer}\le 10.0%$**)**:

*Hypothesis *$H_{1C}$: Under zero-shot cross-airport transfer without local retraining (e.g., deploying from Newark to LaGuardia), the Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($RTR\approx 1.00,\Delta MASE\le 10.0%$) because published flight schedule convolution is strictly invariant to local terminal layout. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($RTR\gg 1.00,\Delta MASE>10.0%$) due to decision tree terminal geometry overfitting (memorization of specific carrier bank timings and gate configurations at the training airport).

### Section 1.1 Design and procedures

The execution of this research is structured into four sequential, iterative phases designed to translate raw aviation data streams into comparative model performance results:

**Phase 1: Data Collection & Preprocessing (ETL)**:

Pull origin-and-destination estimates, load factor, TSA throughput, and On-Time Flight Performance data from 2019 to 2025.

Filter 2019–2025 to preserve baseline operational validity and exclude systemic pandemic distortions.

Define metrics to evaluate each framework's robustness, resilience, and generalizability.

**Phase 2: Model Development**:

Construct and calibrate static deterministic operational baselines and queuing structures to establish an operational control group.

Train supervised machine learning time-series architectures to capture non-linear flight schedule dispersion and delay effects.

Program dynamic two-stage hybrid frameworks that dynamically integrate queuing theory with real-time flight schedule convolution and 1-step live error innovation feedback.

**Phase 3: Evaluation Framework**:

Run model inferences against standardized baseline historical testing datasets across the 12-month 2025 out-of-time holdout.

Stress-test frameworks under simulated and empirical disruption scenarios, such as peak asset constraints, convective ground stops, and zero-shot spatial cross-airport transfers.

Compute distinct metrics to evaluate each framework's robustness, resilience, and generalizability.

Figure 2*Evaluation Metric Definition*

*Figure 2: Evaluation Metric Definition*

**Phase 4: Analysis and Interpretation**:

Map empirical performance outputs to initial foundational literature alignment.

Segment predictive insights into system-wide trends (both macro and micro) to deliver actionable operational recommendations for airport operators and security planners.

Figure 3*Design and Procedure Phases*

*Figure 3: Design and Procedure Phases*

#### Candidate Predictive Models and Baseline Control

To evaluate the research questions, the investigation establishes three candidate models representing distinct operational paradigms, benchmarked against an empirical baseline control:

**The Baseline Control Benchmark (Daily Persistence)**:

*Operational Logic*: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the exact same hour yesterday ($Vol^{^}_{t}=Vol_{t-24}$).

*Evaluation Role*: Serves as the non-parametric reference standard ($MASE\equiv 1.000$). Any operational model worth deploying must prove that it beats this simple historical benchmark.

**Model 1: Deterministic Flight Schedule Model (Operational Baseline)**:

*Operational Logic*: Uses published airline flight schedules, shifted forward in time using empirical passenger show-up distributions from ACRP Report 40 (*Airport Passenger Terminal Planning and Design*).

*Mechanics*: Because passengers arrive 90 to 120 minutes before takeoff, scheduled flight departure banks are convolved across lead arrival horizons ($t+1,t+2,t+3$). This captures the operational ebb and flow of scheduled flight waves without requiring real-time delay telemetry or statistical machine learning.

**Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**:

*Operational Logic*: Uses an automated decision-tree algorithm trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features.

*Mechanics*: The decision trees learn non-linear operational rules (e.g., how departure delays, tactical cancellations, and surface taxi queues ripple into checkpoint arrival dispersion). It tests whether airside operational data improves checkpoint forecasts over flight schedules alone.

**Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**:

*Operational Logic*: Combines the structured foundation of airline flight schedules with live real-time feedback from the checkpoint floor.

*Mechanics*:

*Stage 1*: Captures recurring daily and weekly flight schedule cycles.

*Stage 2*: A decision tree predicts residual volatility shocks caused by flight delays and weather ground stops, dynamically incorporating live 1-step error feedback from the previous hour ($e_{t-1}=y_{t-1}-\hat{y}_{t-1}$). If lines are longer than the flight schedule predicted, the model immediately adjusts upward to track stranded passengers.

#### Dataset Partitioning and Validation Protocol

Models were trained, tuned, and evaluated across the 32-month Candidate B development partition:

**Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days; 122,847 hourly observations across the filtered cohort).

**Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days; 72,723 hourly observations), strictly reserved for hyperparameter tuning.

**Out-of-Time Holdout Window**: January 1, 2025 to December 31, 2025 (3,222 airport-days; 72,053 complex-level screening hours), strictly reserved for final out-of-time evaluation.

**Operational Separation Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades and severe convective storm disruptions do not leak across evaluation boundaries.

#### Quantitative Evaluation Dimensions and Operational Regimes

Airport operations are structured into a three-tier operational taxonomy:

**Tier 1: Nominal On-Time Baseline**: Departure delays $<15 minutes$ and zero tactical cancellations ($N_{cancels}=0$). Grounded in the FAA/DOT A14 regulatory reference benchmark, this state serves as an experimental control to observe pure passenger show-up curves without airside delay distortion.

**Tier 2: Routine Daily Operations**: Everyday commercial hub reality, characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.

**Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays $\ge 45 minutes$ or tactical cancellations $\ge 5$.

Performance is evaluated across three orthogonal dimensions:

**Dimension 1: Robustness (Nominal & Routine Operations)**: Verifying that a model delivers dependable, low-error volatility forecasts during standard daily flight banks. Governing metrics: Root Mean Squared Error ($RMSE_{routine}$) and Mean Absolute Scaled Error ($MASE_{routine}$). Explicit target: $min\left(RMSE_{routine}\right)$ and $MASE_{routine}<0.700$.

**Dimension 2: Resilience (Severe Disruption Recovery)**: Verifying that a model resists demand collapse and recovers rapidly during severe storm ground stops and irregular operations. Governing metrics: Disruption Error Multipliers ($R_{RMSE}$ and $R_{MASE}$), Disruption Error ($MASE_{shock}$), and Time-to-Recovery ($TTR$). Explicit target: $R_{RMSE}\approx 1.00 \left(R_{MASE}\approx 1.00\right),min\left(MASE_{shock}\right)$, and $TTR<4.0 hours$.

**Dimension 3: Generalizability (Cross-Airport Transferability)**: Verifying whether a model calibrated at one airport (e.g., Newark Liberty, EWR) can be deployed directly to a different airport with distinct gate layouts (e.g., New York LaGuardia, LGA) without site-specific retraining. Governing metrics: Relative Transfer Ratio ($RTR=RMSE_{transfer}/RMSE_{in-sample}$) and Percentage Change in Transfer MASE ($\Delta MASE_{transfer}$). Explicit target: $RTR\approx 1.00 \left(1.00\pm 0.05\right)$ and $\Delta MASE_{transfer}\le 10.0%$.

### Section 1.2 Apparatus and materials

To manage, parse, and evaluate the large datasets required for this study, the following software and computing resources are used:

**Google Antigravity and Python**: Utilized as an integrated agentic framework and primary data ingestion engine to manage high-volume government data dumps during the ETL process. To ensure data integrity at this scale, custom scripts handled automated data pulling, unzipping, spatial parsing, and relational joining workflows in the data pipeline for downstream predictive modeling.

**Microsoft Excel for Mac & Microsoft Power BI**: Deployed locally for advanced data transformation, tabular synthesis, and visual validation.

**Vega High-Performance Computing (HPC) Cluster**: The remote institutional environment used to execute resource-intensive Python algorithms, filtering large-scale raw data down to determine airport and airline parameters.

## Section 2: Sample

The sample consists of airport checkpoint environments selected to reflect variation in terminal structure and airline dominance. Airports are grouped into structured categories to account for how physical layout influences passenger distribution and checkpoint use (OAG, 2026). This strategy is intended to support comparison across terminal types and carriers rather than to claim complete uniformity across airports and airlines.

Figure 4*Sample Framework for Terminal Capacity and Checkpoint Configuration*

*Figure 4: Sample Framework for Terminal Capacity and Checkpoint Configuration*

Figure 5*Airport Operational Archetypes and Terminal Configuration*

*Figure 5: Airport Operational Archetypes and Terminal Configuration*

### Macro Categorization: Terminal-to-Airline Distribution

Airports are first classified into four structural archetypes to control for how airline market share impacts terminal distribution, with structural archetypes outlined below:

**Mega Hubs with No Dedicated Terminals (e.g., ATL, CLT, DEN)**: Sprawling operations where major legacy carriers share linear concourses or central ticketing, distributing passenger volume across shared screening areas.

**Decentralized Airline-Dedicated Terminals (e.g., LAX)**: Dispersed multi-terminal airports where distinct physical buildings are allocated exclusively to individual legacy carriers, isolating an airline's passenger wave to specific physical checkpoints.

**Single-Carrier Dedicated Mega-Terminals (e.g., DTW)**: Single-carrier "fortress" environments where a single dominant airline channels its entire domestic and international operation through one massive mega-terminal (e.g., Delta’s exclusive hold on the McNamara Terminal).

**Airports with Multiple Terminals Dedicated Exclusively to One Airline (e.g., DFW)**: Large-scale regional hubs requiring a single dominant carrier to distribute hub-and-spoke operations across multiple independent terminal buildings (e.g., American Airlines utilizing Terminals A, B, C, and E) to scale its operations.

### Micro-Level Refinement: Checkpoint Co-Location and Isolation

While macro terminal assignments establish an operational baseline, localized checkpoint-level configurations ultimately determine queue characteristics. American Airlines, Delta Air Lines, and United Airlines are selected for analysis. The explicit criterion for inclusion is a domestic enplanement market share exceeding 10% at major United States hub airports (BTS, 2026).

Recent reporting suggests Southwest’s boarding and carry-on system is both distinctive and inconsistent: the airline still relies on a differentiated low-fare brand, but its newer assigned-seating and baggage-fee policies have increased carry-on pressure and created boarding congestion (Boston 25 News, 2026). Furthermore, legacy carrier passengers display consistent, unimodal lognormal arrival timing:

$\tau \sim Lognormal\left(\mu \sigma ^{2}\right), E\left[\tau \right]\approx 105 minutes$

In contrast, Southwest's historical open-seating boarding structure, boarding group positioning (Groups A, B, C), and two-free-checked-bags policy generate a bimodal arrival mixture:

$\tau _{WN}\sim w_{1}N\left(\mu _{1}\sigma _{1}^{2}\right)+\left(1-w_{1}\right)N\left(\mu _{2}\sigma _{2}^{2}\right)$

where $\mu _{1}\approx 135 minutes$ for boarding position maximizers and $\mu _{2}\approx 65 minutes$ for carry-on-only business travelers. Pooling Southwest passenger streams with legacy carriers violates show-up distribution homogeneity. It is therefore not included in the study.

To isolate the effects of low-cost carriers and unaligned traffic from legacy airline operations, the following terminal and checkpoint characteristics are defined to account for the impact of extenuating variables:

**Shared Checkpoints with Limited Carrier-Level Separation (Centralized)**: In centralized hub models like Salt Lake City (SLC), a dominant carrier may hold the majority market share (70%), but a single consolidated terminal channels 100% of passengers through one primary security checkpoint. In these environments, it is not readily possible to isolate carrier-specific passenger flows using the available data structures.

**Isolated Checkpoints (Decentralized)**: To find checkpoints highly unlikely to see Delta, American, or United traffic, the methodology prioritizes decentralized layouts with extreme carrier polarization, such as the following:

*DCA (Terminal 1)*: Consisting of Gates A1–A9, this terminal exclusively serves Air Canada, Frontier, and Southwest. American, Delta, and United are completely segregated into Terminal 2, creating a strong comparison setting for low-cost and regional carrier processing behaviors.

*SEA (Decentralized Main Terminal)*: Utilizing five separate security checkpoints across a footprint dominated by Alaska Airlines (52% market share). Checkpoints feeding Alaska-heavy gates or dedicated satellite concourses offer a high statistical probability of isolating non-Big Three passenger flows.

*CLT (Extreme Dominance Isolation)*: Where American Airlines controls 90% of the market share. Because Delta (2.5%) and United (2%) maintain a negligible footprint across the airport's 5 checkpoints, nearly any selected lane acts as a functional monoculture for a single legacy carrier's hub behavior.

### Four-Tiered Purposive Filtering Pipeline

To systematically isolate the direct operational link connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel:

**Macro Filter: Scale and Congestion Regimes**: Commercial aviation passenger volumes follow a heavy-tailed power-law distribution ($P\left(X>x\right)\sim x^{-\alpha },\alpha \approx 1.15$). Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures. In airport queueing dynamics, traffic intensity $\rho \left(t\right)=\frac{\lambda \left(t\right)}{c\left(t\right)\cdot \mu }$ at small regional airfields remains sparse ($\rho \left(t\right)\ll 0.3$), preventing queue formation and causing throughput to mirror arrivals without boundary resistance. In contrast, Top 25 hub facilities routinely approach or exceed capacity ($\rho \left(t\right)\to 1.0$) during morning and evening departure banks (05:00–08:30 and 16:00–18:30), creating the non-linear queue delays and buffer depletion necessary to train and validate congestion-aware models.

**Meso Filter: Airspace Shock Invariance and Southwest Exclusion**: Candidate environments were required to operate concurrent domestic mainline services by American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA) under identical exogenous airspace conditions ($\delta _{t}$), neutralizing common weather and Air Traffic Control (ATC) delay confounders while excluding Southwest Airlines (WN).

**Micro Filter: Carrier Checkpoint Isolation**: In shared terminal complexes, synchronized departure banks produce collinear flight schedules ($Corr\left(S_{j}S_{j^{'}}\right)\ge 0.88$). Restricting analysis to carrier-exclusive screening environments enforces $P\left(Carrier=j^{*}\mid Checkpoint k\right)=1.0$, eliminating inter-carrier schedule crosstalk ($\kappa <25$) and directly mapping carrier flight banks to landside checkpoint throughput.

### Balanced Factorial Cohort

Applying this four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort** across 12 carrier-exclusive screening complexes:

**American Airlines (AA)**: Dallas/Fort Worth (DFW), Philadelphia (PHL), Chicago O'Hare (ORD)

**Delta Air Lines (DL)**: Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)

**United Airlines (UA)**: Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles (LAX) This cohort achieves complete factorial symmetry: exactly 3 legacy carriers $\times$ 3 dedicated terminal environments, spanning all four operational archetypes identified in national clustering.

### Temporal Scope and Boundary Definition

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic operational volatility induced by the COVID-19 pandemic (Sun et al., 2021; Gao, 2022). While a baseline 'post-pandemic' operational era is provisionally considered as beginning January 1, 2023, an exploratory analysis is performed during data preprocessing to refine this demarcation due to varying definitions of ‘post-pandemic’ (ICAO, 2024; Centre for Aviation, 2025).

This preprocessing step evaluates pre-pandemic baseline patterns against longitudinal 2019–2025 data to pinpoint the empirical inflection point where system throughput and schedule deviations returned to steady-state normalization. Structural break tests, rolling Welch's $t$-tests, and CUSUM analyses identified **May 1, 2022** (Candidate B demarcation) as the empirical inflection point, coinciding with the vacatur of the federal transit mask mandate and the rebound of airline load factors to 84.7%, matching pre-pandemic baselines. Restricting the active dataset to this verified window enables the forecasting models to capture contemporary queue dynamics and schedule-driven variability without being skewed by transient historic anomalies.

## Section 3: Sources of the Data

Secondary operational data will be compiled from four primary authorized repositories covering the 2019 to 2025 period (TSA, 2026; BTS, 2026; LAWA, 2026):

### TSA FOIA Security Screening Checkpoint Logs

Obtained via Freedom of Information Act (FOIA) disclosures and cross-referenced with public archival repositories, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### BTS On-Time Flight Performance

Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

### BTS Form 41 Schedule T-100 Domestic Segment Data

Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

### BTS Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), supplemented by authorized monthly airport traffic reports (such as LAX Air Traffic Statistics). These feeds are utilized to extract quarterly connecting passenger ratios across airport pairs to support originating passenger flow estimation.

## Section 4: Validity

### Internal Validity Threats and Remediation Protocols

A primary threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand (the "Hub Disconnect"). To reduce this bias, origin-and-destination survey data (BTS DB1B) and airport-specific O&D ratios are used to estimate and remove connecting traffic from passenger flow calculations, isolating true originating landside checkpoint demand.

Additional internal validity controls include:

**Operational Partition Boundary Leakage**: Multi-day delay cascades and weather ground stops can create artificial temporal dependency across model evaluation boundaries. To prevent lookahead bias and contamination, strict 7-day operational purge buffers are enforced between training, validation, and testing partitions.

**Exogenous Airspace Shock Confounders**: Localized thunderstorm systems or regional FAA ground delay programs could confound cross-carrier comparisons. Enforcing meso-level filtering guarantees that all carrier complexes within the study cohort operate under identical airspace shocks ($\delta _{t}$).

### Construct Validity Threats and Operational Formulations

Construct validity is affected by checkpoint heterogeneity, as raw lane counts obtained from TSA throughput data combine different screening modes, such as TSA PreCheck, with standard screening lanes, each exhibiting disparate processing rates ($\approx 250–300$ pax/lane-hr for PreCheck vs. $\approx 150–180$ pax/lane-hr for standard). To resolve this heterogeneity threat, the methodology constructs scale-free relative volatility metrics ($CV_{TSA}$) and standardized lane measures rather than unadjusted raw totals.

### Mathematical Formulation of Volatility Targets

Construct validity requires establishing explicit mathematical formulations that measure passenger throughput volatility rather than static volume levels:

#### 1. Intraday Diurnal Absolute Dispersion ($\sigma _{TSA, hr}$)

Measures the absolute dispersion of hourly screening counts across the 24 hours of calendar day $d$ (in passengers per hour):

$\sigma _{TSA, hr}\left(d\right)=\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h}-\hat{y}_{d})^{2}}$

This target reflects the absolute peak-to-trough amplitude of passenger arrival waves.

#### 2. Intraday Scale-Free Relative Volatility ($CV_{TSA, hr}$)

Normalizes intraday dispersion by average daily throughput:

$CV_{TSA, hr}\left(d\right)=\frac{\sigma _{TSA, hr}\left(d\right)}{\hat{y}_{d}}=\frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (y_{d,h}-\hat{y}_{d})^{2}}}{\frac{1}{24}\sum_{h=0}^{23} y_{d,h}}$

By removing baseline airport scale, this scale-free metric measures arrival burstiness and queue surge spikiness independent of facility size.

#### 3. Multi-Day Temporal Rolling Volatility ($\sigma _{TSA, 7d}$)

Measures the 7-day rolling standard deviation of daily passenger volume (in passengers per day):

$\sigma _{TSA, 7d}\left(d\right)=\sqrt{\frac{1}{6}\sum_{k=0}^{6} (Y_{d-k}-\hat{Y}_{7d})^{2}}$

This target captures medium-term multi-day passenger flow turbulence induced by convective storms, winter blizzards, and cascading cancellation shocks.

#### 4. Flight Departure Delay Dispersion and Coupled Volatility

Systemic queue breakdown is driven by coupled volatility mismatch between landside passenger arrivals and airside flight departures:

**Flight Departure Delay Dispersion**: Sample standard deviation of departure delays across uncancelled domestic flights on day $d$:

$\sigma _{Delay,d}=\sqrt{\frac{1}{N_{d}-1}\sum_{i=1}^{N_{d}} (DepDelay_{d,i}-DepDelay^{ˉ}_{d})^{2}}$

**The Coupled Volatility Index**: Joint product of landside arrival variation and airside delay dispersion:

$CVI_{d}=CV_{TSA,d}\times \sigma _{Delay,d}$

**Diurnal Operational Turbulence Shock Index**: For each hour $h\in \left[023\right]$ conditioned on Day of Week ($dow$):

$T_{dow}\left(h\right)=max\left(\left(\frac{\sigma _{TSA,dow}\left(h\right)}{max_{k}\sigma _{TSA,dow}\left(k\right)}  \frac{\left[\sigma _{intra,dow}\left(h\right)+\sigma _{inter,dow}\left(h\right)\right]\cdot I\left(\hat{F}_{dow}\left(h\right)\ge 20\right)}{max_{k}\left[\left(\sigma _{intra,dow}\left(k\right)+\sigma _{inter,dow}\left(k\right)\right)\cdot I\left(\hat{F}_{dow}\left(k\right)\ge 20\right)\right]}\right)\right)$

Applying 1D K-Means clustering ($k=3$) establishes three operational diurnal regimes: *1_OFF_PEAK* ($T<0.35$, overnight curfew), *2_MID_PEAK* ($0.35\le T<0.75$, midday steady flow), and *3_PEAK* ($T\ge 0.75$, queuing turbulence).

## Section 5: Treatment of Data

The execution of data preparation follows a rigorous, sequential Extract, Transform, Load (ETL) pipeline designed to ingest, clean, standardize, and align the longitudinal aviation datasets:

### Sequential Extract Pipeline

Download TSA Throughput files from the FOIA reading room (PDFs) spanning 2019 to 2026.

Parse PDFs into standardized tabular format (CSV).

Download TSA Throughput PDFs and CSVs (2022–2025) from public repository archives (e.g., https://github.com/mikelor/TsaThroughput).

Cross-reference TSA datapoints to identify temporal gaps, duplicates, and reporting inconsistencies.

Download On-Time Flight Performance data (CSVs) spanning 2019 to 2026 for all domestic flights in the United States.

Download BTS Form 41 Schedule T-100 Segment Airline Traffic Data and calculate monthly route load factors.

Download BTS DB1B ticket survey coupon files and airport-specific origin-and-destination summary statistics.

Perform an audit across the 7-year sequence to identify missing data and reporting discontinuities.

### Sequential Transform Pipeline

Standardize timestamps across all feeds to a uniform operational clock (local airport solar operational time).

Map and resolve typographical errors, airport names, data mismatches, and checkpoint naming variations.

Normalize airport codes, checkpoint prefixes, and common terms (e.g., Checkpoint $\to$ CKPT).

Spatial entity resolution: Map upstream corrupted airport strings; assign unidentifiable strings to a dedicated null surrogate key (*airportId* = 0, *airportMissing* = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport."

Preserve scheduled checkpoint closures: 98.6% of zero-volume records occur between 00:00 and 03:59 local time during scheduled overnight curfews. Rather than applying artificial smoothing or spline imputations, these intervals are preserved as true operational structural zeros.

Information causality and cancellation handling: Purge advance cancellations (>24 hours prior) from departing seat supply curves, while retaining tactical cancellations (<2 hours prior), reflecting the operational reality that booked passengers had already completed landside security screening before the flight was cancelled.

Separate scheduled flights from actual operated flights to distinguish planned bank structures from tactical executions.

Estimate aircraft seat capacities using flight distance, carrier identity, and aircraft equipment/tail-number characteristics.

Scale seat counts using route-level load factor data to estimate departing passenger volume.

Merge datasets to determine terminal-specific connecting passengers within target complexes using DB1B ticket survey deflators.

Empirical passenger show-up curve convolution: Convolve scheduled flight departure banks across empirical lead-time distributions ($t+1,t+2,t+3$ from ACRP Report 40) and align them with hourly TSA throughput intervals to produce the final conformed modeling dataset.

### Feature Space Engineering

Construct the Multi-Scale Operational Feature representation space:

*Feature Values (Levels, 14 Attributes)*: Schedule Scale (sched_daily_total, actual_daily_total, sched_hourly_mean, sched_rolling_7d_mean), Cancellations (daily_cancellations, daily_cancel_rate, cancel_rolling_7d_mean, cancel_rate_rolling_7d_mean), Delays (avg_dep_delay_minutes, flights_delayed_15min_pct), Surface Queues (avg_taxi_out_minutes), and Network Buffers (aircraft_gauge_seats, route_load_factor_pct, connecting_passenger_share_pct).

*Feature Volatilities (Dispersion, 10 Attributes)*: Schedule Dispersion (sched_hourly_std, sched_hourly_cv, actual_hourly_std, actual_hourly_cv, sched_rolling_7d_std, sched_rolling_7d_cv), Cancellation Dispersion (cancel_rolling_7d_std, cancel_rate_rolling_7d_std, otp_cancellation_volatility_cv), and Delay Dispersion (otp_departure_delay_volatility_cv).

*Combined Dual Paradigm (24 Attributes)*: Interacts both feature spaces to capture both baseline capacity scale and operational volatility.

### Sequential Load Pipeline

Load master conformed data copies to secure persistent cloud storage (OneDrive) and local data warehouse directories.

Build relational analytics tables, lookup dimensions, and multidimensional interaction tensors.

Automate verification audits for schema validity, referential integrity, and row preservation across the 7-year sequence.
