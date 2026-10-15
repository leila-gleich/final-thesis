# Comprehensive Master Thesis Defense Outline: Slides 3–26
## Grounded in Thesis v3 (`master-docs/Thesisv3.docx` / `master-docs/master_thesis_audited.md`)
### Master of Science in Aeronautics (MSAA / Gleich 700B) — Embry-Riddle Aeronautical University
**Candidate**: Leila Gleich  
**Thesis Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: An Evaluation of Multi-Pillar Performance Measures for TSA Throughput Volatility*  
**Synchronized Slide Deck**: `thesis_final_package/Gleich-Thesis-Defense-Final.pptx` (Slides 3–26)

---

## Executive Overview of the Defense Architecture

This document provides a comprehensive academic description and operational discussion for Slides 3 through 26 of the master's thesis defense presentation deck (`Gleich-Thesis-Defense-Final.pptx`). Rather than serving as a verbatim oral speaking script, this outline functions as a rigorous, synthesized summary of the authoritative thesis manuscript (`Thesisv3`). It articulates the theoretical foundations, econometric data pipeline, empirical findings, prospective holdout model benchmarks, and strategic implications that govern the modeling of passenger screening throughput volatility across commercial airport hubs.

---

### Slide 3: Research Problem

#### Slide Description
* **Header & Title**: *Research Problem: Terminal Queuing Fragility & Fixed Physical Capacity*
* **Visual Elements & Layout**:
  - Two-column layout juxtaposing airport operational constraints against mathematical queuing physics.
  - Centered formal display of Kingman's Heavy-Traffic Approximation Formula:
    $$W_q \approx \left[ \frac{\rho}{c(1-\rho)} \right] \cdot \left[ \frac{C_a^2 + C_s^2}{2} \right] \cdot \frac{1}{\mu}$$
  - Key bulleted thematic anchors:
    1. *Inflexible Physical Capacity*: Advanced Imaging Technology (AIT) screening lanes and certified Transportation Security Officer (TSO) shift allocations cannot expand dynamically in real time.
    2. *Quadratic Delay Scaling*: Passenger waiting times ($W_q$) scale quadratically with arrival volatility ($C_a^2$) as checkpoint utilization ($\rho$) approaches capacity saturation ($\rho \to 1.0$).
    3. *Static Staffing Fragility*: Historical headcount volume tables fail during airside delay cascades and convective weather ground stops.
    4. *Core Research Objective*: Airport screening checkpoints require volatility-aware stochastic forecasting rather than static volume averages.

#### Thesis Summary & In-Depth Discussion
* **Physical Infrastructure Inflexibility**: Commercial airport passenger security screening checkpoints represent the most rigid physical bottleneck in civil aviation infrastructure. Unlike air traffic control sectors or airline flight dispatch that can implement tactical vectoring or en-route speed adjustments, terminal screening capacity is bounded by fixed architectural envelopes, certified AIT equipment footprints, and rigid Transportation Security Administration (TSA) shift rosters. Adding screening capacity requires weeks of federal administrative lead time, credentialed officer onboarding, and physical checkpoint lane reconfigurations.
* **Queuing Theory Under Heavy-Traffic Saturation**: Terminal crowding is fundamentally governed by heavy-traffic queuing dynamics formalized in Kingman's formula. In airport security operations, passenger queue wait times ($W_q$) do not scale linearly with passenger volume ($y_t$). Instead, as checkpoint lane utilization ($\rho$) nears full capacity ($\rho \to 1.0$), queue lengths and waiting delays escalate quadratically with the coefficient of variation of passenger arrivals ($C_a^2$). A minor 10% surge in arrival burstiness during peak bank hours generates disproportionate line spillbacks, cascading into ticketing lobbies and tarmac departures.
* **The Failure of Static Staffing**: TSA checkpoint staffing allocations historically rely on static time-of-day tables or historical enplanement volume projections. These static heuristics assume deterministic passenger arrival behaviors under clear-weather, on-time airline operations. When convective weather ground delay programs, ground stops, or mechanical delay cascades disrupt airline schedules, static tables collapse, causing severe staffing misallocations—understaffing during delayed flight departure waves and overstaffing during dead periods. Checkpoints require stochastic forecasting targeted explicitly at *throughput volatility* ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$).

---

### Slide 4: Research Question

#### Slide Description
* **Header & Title**: *Research Question: Predictive Frameworks & Multi-Pillar Performance*
* **Visual Elements & Layout**:
  - Central highlighted research question framed prominently across the upper half of the slide.
  - Three distinct operational performance pillars displayed as structured card elements:
    - **Robustness**: Routine operational accuracy under nominal on-time baseline conditions.
    - **Resilience**: Error stability and recovery speed under irregular operations (IROPS) and severe convective disruptions.
    - **Generalizability**: Cross-airport spatial portability across unfamiliar terminal layouts under zero-shot transfer without local retraining.

#### Thesis Summary & In-Depth Discussion
* **Formulation of the Core Research Question**:
  > *Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule baselines, supervised machine learning, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?*
* **The Evaluative Void in Airport Research**: Classical transportation modeling literature historically evaluates predictive algorithms using a single, static aggregate metric—most commonly the Coefficient of Determination ($R^2$), Mean Absolute Error (MAE), or Root Mean Squared Error (RMSE) calculated across an entire multi-year dataset. In commercial aviation operations, an aggregate metric provides misleading guidance: an algorithm that minimizes average annual error during calm weather may suffer catastrophic collapse during a 3-hour thunderstorm ground stop. This research establishes that model efficacy is inherently multi-dimensional, requiring explicit evaluation across distinct operating regimes.

---

### Slide 5: Hypothesis (The Asymmetric Trade-Off $H_1$)

#### Slide Description
* **Header & Title**: *Research Hypothesis: The Master Asymmetric Trade-Off ($H_1$)*
* **Visual Elements & Layout**:
  - Display of Master Hypothesis $H_1$ as an overarching principle of aviation predictive modeling.
  - Three sub-hypothesis cards delineating expected model performance per operational dimension:
    - $H_{1a}$ (Robustness): Supervised Machine Learning (Model 2) & Dynamic Hybrid (Model 3) $\implies \text{MASE}_{\text{routine}} < 0.700$, lowest RMSE.
    - $H_{1b}$ (Resilience): Dynamic Two-Stage Hybrid (Model 3) $\implies R_{\text{MASE}} \approx 1.00$, lowest $\text{RMSE}_{\text{shock}}$, $\text{TTR} < 4.0\text{h}$; Supervised ML collapses ($R \gg 1.00$).
    - $H_{1c}$ (Generalizability): Deterministic Flight Schedule Model (Model 1) $\implies \text{RTR} \approx 1.00$, $\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$; Complex models fail due to layout overfitting.

#### Thesis Summary & In-Depth Discussion
* **The Core Theoretical Tenet**: Thesis v3 establishes that no single predictive modeling paradigm can universally dominate across all operational conditions. Complex data-driven architectures optimize routine conditions but exhibit acute brittleness during severe disruptions; conversely, first-principles deterministic models exhibit superior spatial portability across facilities but lack dynamic adaptation during tactical delay surges.
* **Formal Sub-Hypotheses**:
  - **$H_{1a}$ (Robustness Under Routine Operations)**: Under nominal on-time baseline conditions (departure delays $< 15$ min, zero cancellations), Supervised Machine Learning (Model 2) and Dynamic Two-Stage Hybrid (Model 3) will satisfy the routine target ($\text{MASE} < 0.700$), significantly outperforming naive persistence and deterministic schedules.
  - **$H_{1b}$ (Resilience Under Irregular Operations)**: Under acute disruption regimes (departure delays $\ge 45$ min or cancellations $\ge 5$), the Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience target ($R_{\text{MASE}} \approx 1.00, \text{TTR} < 4.0\text{h}$). Pure machine learning (Model 2) will suffer severe performance collapse due to structural misalignment between scheduled flights and physical lobby crowds (the Empty Checkpoint Fallacy).
  - **$H_{1c}$ (Generalizability Across Disparate Facilities)**: Under zero-shot spatial transfer (EWR $\to$ LGA) without local retraining, the first-principles Deterministic Flight Schedule Model (Model 1) will satisfy the generalizability target ($\text{RTR} \approx 1.00, \Delta\text{MASE} \le 10\%$). Complex models will fail due to terminal geometry and flight-bank overfitting.

---

### Slide 6: Literature Review & Theoretical Foundations

#### Slide Description
* **Header & Title**: *Literature Review & Theoretical Foundations: Six Operational Domains*
* **Visual Elements & Layout**:
  - Horizontal conceptual lineage diagram tracking the academic progression of airport terminal modeling across six core operational domains:
    1. Traditional Queuing & Deterministic Formulations
    2. Discrete-Event Simulation & Micro-Simulation
    3. Advanced Predictive Machine Learning
    4. Cyber-Physical & Sequential Hybrid Frameworks
    5. Post-Pandemic Structural Demarcation (COVID-19)
    6. Multi-Dimensional Performance Evaluation (The Triad)

#### Thesis Summary & In-Depth Discussion
* **Academic Evolution of Terminal Modeling**: Airport terminal research originated in static deterministic models and basic $M/M/s$ or $M/G/s$ queuing approximations (Horonjeff & McKelvey, 1994; Newell, 1982). These early models treated passenger arrival rates as uniform distributions derived from daily flight schedules. As terminal complexity grew, researchers recognized that airport subsystems (curbside, ticketing, TSA security, concourse dwell, gate boarding) operate as an interconnected, stochastic network with pronounced peaking phenomena.
* **The Six Domains of the Theoretical Framework**:
  1. *Traditional Models*: Schedule-based convolutions based on empirical passenger show-up distributions (ACRP Report 40).
  2. *Micro-Simulation*: Agent-based and discrete-event tools (CAST, SimWalk, AirTOP) modeling microscopic passenger interactions.
  3. *Statistical & Machine Learning*: Autoregressive time series (SARIMA), decision trees, and ensemble boosting capturing airside operational covariates.
  4. *Hybrid Architectures*: Combining physical domain queuing principles with live sensor error innovation feedback.
  5. *Structural Disruptions*: Identifying that the COVID-19 pandemic induced permanent behavioral shifts in passenger arrival curves, leisure vs. business passenger ratios, and checkpoint dwell.
  6. *Dynamic Evaluation Standards*: Transitioning from single global error metrics to a condition-responsive evaluation trio (Robustness, Resilience, Generalizability).

---

### Slide 7: Traditional Models (The Gap: Volatility vs. Volume)

#### Slide Description
* **Header & Title**: *Traditional Models: The Values Versus Volatility Operational Decoupling*
* **Visual Elements & Layout**:
  - Comparative statistical split illustrating the complete failure of raw passenger volume to capture operational delay dynamics:
    - **Raw Volume vs. Flight Delays**: $r = -0.062, p = 0.77, R^2 = 2.5\%$ (*Failure to Correlate*).
    - **Throughput Volatility vs. Delay Volatility**: $r = +0.4373, p < 0.05, R^2 = 19.1\%$ (*Operational Coupling*).
  - Mathematical definition of scale-free intraday arrival burstiness:
    $$CV_{\text{TSA, hr}} = \frac{\sigma_{\text{TSA, hr}}}{\mu_{\text{TSA, hr}}}$$
  - Callout on Kingman's Heavy-Traffic Approximation asserting that arrival variance ($C_a^2$), not volume, drives queue spillbacks.

#### Thesis Summary & In-Depth Discussion
* **The Empirical Decoupling Discovery**: Traditional airport management literature assumes that airport terminal congestion is directly correlated with aggregate passenger volume. However, empirical analysis of federal data across the Top 25 U.S. airports reveals a profound econometric disconnect: raw passenger volume ($y_t$) exhibits virtually zero correlation with flight departure delay minutes ($r = -0.062, p = 0.77$). An airport can process 50,000 daily passengers with zero delays if flights are uniformly spaced, or collapse under severe line backlogs with 30,000 passengers if arrivals compress into narrow 45-minute banks.
* **Throughput Volatility as the True Operational Driver**: When evaluated in the volatility domain, the statistical relationship becomes decisive: checkpoint throughput volatility ($CV_{\text{TSA}}$) is positively and significantly coupled with flight departure delay volatility ($CV_{\text{delay}}$: $r = +0.4373, p < 0.05$). Checkpoint congestion is fundamentally an arrival burstiness problem.
* **Queuing Physics Implications**: Under Kingman's heavy-traffic approximation, queue waiting time scales quadratically with the square of the arrival coefficient of variation ($C_a^2$). Forecasting static headcounts leaves security supervisors blind to the arrival spikes that induce runaway checkpoint queues.

---

### Slide 8: Shift to Micro-Simulation Modeling

#### Slide Description
* **Header & Title**: *Shift to Micro-Simulation Modeling: Capabilities and Operational Latency*
* **Visual Elements & Layout**:
  - Architectural breakdown of Discrete-Event Simulation (DES) and Agent-Based Modeling (ABM) in airport terminal engineering.
  - Two-column comparative matrix:
    - **Analytical Capabilities**: Granular spatial modeling, passenger walking trajectories, baggage-drop interactions, and boarding gate constraints.
    - **Operational Bottlenecks**: Extreme compute latency (hours to simulate a single day), parameter over-parameterization, calibration fragility, and complete inability to support real-time tactical re-rostering during live operations.

#### Thesis Summary & In-Depth Discussion
* **The Rise of Micro-Simulation**: To address the spatial limitations of closed-form queuing equations, airport planners turned to discrete-event simulation software (e.g., CAST Terminal, AirTOP, SimWalk). These platforms model individual passenger agents navigating terminal corridors, selecting security lanes, and reacting to boarding announcements.
* **The Tactical Operational Dilemma**: While discrete-event micro-simulations provide invaluable insights for long-range terminal master planning and architectural capital design, they are structurally unsuited for tactical day-of-operations management. Simulating 24 hours of flight banks across a complex multi-terminal hub requires hours of computational runtime, dozens of unobservable behavioral parameters (e.g., walking speed distributions, concession dwell probabilities), and extensive manual calibration. During severe convective weather or air traffic ground delay programs, airport dispatchers require real-time forecasts generated in milliseconds—a requirement that discrete-event simulation cannot satisfy.

---

### Slide 9: Advanced Predictive Models

#### Slide Description
* **Header & Title**: *Advanced Predictive Models: Machine Learning & Operational Regimes*
* **Visual Elements & Layout**:
  - Structural diagram illustrating the integration of supervised machine learning algorithms (Random Forests, Gradient-Boosted Decision Trees) with Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) covariates.
  - Visual callout illustrating the **Empty Checkpoint Fallacy**:
    - Convective storm $\implies$ Published flights cancelled/delayed $\implies$ ML model predicts 0 passengers $\implies$ Real checkpoint packed with stranded passengers.
  - Core trade-off: High routine statistical accuracy vs. vulnerability to out-of-distribution regime shocks.

#### Thesis Summary & In-Depth Discussion
* **Data-Driven Supervised Learning**: With the availability of large-scale aviation databases, researchers developed supervised machine learning architectures—particularly Gradient-Boosted Decision Trees (GBDT)—capable of ingesting multi-dimensional airside covariates. These models process 24 operational attributes from the BTS OTP database, including aircraft equipment seating capacities, taxi-out queue lengths, rolling carrier delay distributions, and cancellation rates.
* **The Regime Brittleness of Pure Machine Learning**: While machine learning models achieve high statistical precision during normal operating conditions by capturing complex nonlinear relationships, they exhibit dangerous fragility under severe irregular operations (IROPS). The thesis identifies this vulnerability as the **Empty Checkpoint Fallacy**: when convective weather grounds flights, scheduled departures disappear from real-time flight status feeds. A pure supervised machine learning model observes zero scheduled flights and predicts that the security checkpoint will be vacant. In reality, thousands of ticketed travelers have already arrived at the terminal and are physically stranded in screening lobbies awaiting rescheduled flights. Pure machine learning lacks a physical feedback mechanism to observe accumulated human mass.

---

### Slide 10: Architecture Overview

#### Slide Description
* **Header & Title**: *Architecture Overview: The Two-Stage Sequential Hybrid Model*
* **Visual Elements & Layout**:
  - Two-stage block diagram illustrating the sequential coupling of deterministic flight physics with dynamic real-time floor telemetry:
    - **Stage 1 (Domain Schedule Baseline)**: Published Airline Flight Timetables $\to$ Empirical ACRP Report 40 Show-Up Curve Convolution ($t+1, t+2, t+3$) $\to$ DB1B Connecting Deflator ($1 - \text{Connecting Ratio}$) $\to$ Baseline Expected Volatility.
    - **Stage 2 (Floor Telemetry Error Innovation)**: Live TSA Checkpoint Sensor Counts ($y_{t-1}$) $\to$ Recursive Innovation Residual ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) $\to$ Dynamic In-Flight Volatility Forecast Adjustment.

#### Thesis Summary & In-Depth Discussion
* **Bridging Physics and Data**: To resolve the trade-off between deterministic stability and machine learning flexibility, Thesis v3 formalizes a **Two-Stage Sequential Hybrid Model (Model 3)**.
* **Stage 1 (Deterministic Operational Core)**: Stage 1 models the fundamental deterministic physics of passenger arrival. Scheduled departing flight banks are extracted from published airline timetables and convolved across empirical three-hour passenger show-up curves derived from ACRP Report 40 ($t+1, t+2, t+3$). Crucially, scheduled seating capacity is deflated by historical airline connecting ratios ($1 - \text{Connecting Ratio}$) extracted from the BTS DB1B survey, ensuring that transferring passengers who remain airside are excluded from landside screening demand.
* **Stage 2 (Real-Time Error Innovation Feedback)**: Stage 2 introduces a dynamic 1-step recursive feedback loop from the physical checkpoint floor. By computing the prior-hour forecast residual:
  $$e_{t-1} = y_{t-1} - \hat{y}_{t-1}$$
  the model senses whether passengers are accumulating in the lobby due to upstream flight delays. This live residual updates the Stage 1 baseline, providing the dynamic adaptation necessary to survive irregular operations without suffering from the Empty Checkpoint Fallacy.

---

### Slide 11: Design and Procedures: 4 Phases

#### Slide Description
* **Header & Title**: *Design and Procedures: The Four-Phase Research Methodology*
* **Visual Elements & Layout**:
  - Structured four-phase workflow diagram illustrating the research execution pipeline:
    - **Phase 1: Ingestion & Structural Demarcation**: Fusion of 67.2M raw records; identification of post-pandemic equilibrium (May 1, 2022).
    - **Phase 2: Econometric Filtering Funnel**: Four-tier purposive filtering isolating 9 airports and 12 carrier-exclusive screening complexes.
    - **Phase 3: Feature Engineering & Model Calibration**: Lead-lag show-up curve convolution, connecting deflator, and 7-day operational purge buffer.
    - **Phase 4: Prospective Out-of-Time Holdout Evaluation**: Full-year 2025 testing across the Multi-Pillar Performance Matrix (Robustness, Resilience, Generalizability).

#### Thesis Summary & In-Depth Discussion
* **Phase 1 (Data Foundation & Harmonization)**: The research synthesized 67.2 million raw records across four federal databases into a post-ETL analytical warehouse of 42.1 million conformed records. Using Bai-Perron structural break tests, the research established May 1, 2022, as the formal post-pandemic equilibrium point, quarantining distorted pandemic lockdown records from training data.
* **Phase 2 (Purposive Filtering Funnel)**: To prevent spatial and carrier cross-contamination, a four-tier filtering funnel was executed across 450+ U.S. commercial airfields, isolating nine large hub airports characterized by carrier-exclusive terminal screening complexes.
* **Phase 3 (Feature Engineering & Partitioning)**: Raw flight records were convolved across ACRP Report 40 show-up distributions. Data were partitioned into 15,976 training complex-days and 3,293 validation complex-days, separated from the 2025 test set by an immutable 7-day (168-hour) operational purge buffer to eliminate autoregressive lookahead bias.
* **Phase 4 (Prospective Multi-Pillar Holdout Testing)**: All candidate models were evaluated on the untouched 2025 holdout dataset (3,222 complex-days; 72,053 hourly observations) across the formal evaluation triad: Robustness, Resilience, and Generalizability.

---

### Slide 12: Findings and Discussion (Section Divider)

#### Slide Description
* **Header & Title**: *Findings and Discussion: Empirical Discovery & Evaluation Roadmap*
* **Visual Elements & Layout**:
  - Section transition slide establishing the narrative progression of the research findings:
    - *Empirical Data Foundation & Macro Census*
    - *The Four-Tier Filtering Funnel & Cohort Extraction*
    - *Top 9 Cohort Descriptive Statistics & Decoupling*
    - *Candidate Model Development & Holdout Benchmarks*
    - *Hypothesis Testing & Empirical Trade-Off Confirmation*
    - *Operational Implications & The Practitioner's Playbook*

#### Thesis Summary & In-Depth Discussion
* **Bridging Methodology to Empirical Discovery**: This slide marks the pivotal transition from research methodology to empirical evidence. The subsequent findings systematically dismantle traditional aviation assumptions: proving that passenger arrival burstiness decouples from static volume; demonstrating that terminal geometry acts as a physical filter; and validating through prospective 2025 holdout testing that no single predictive model is universally optimal across all operational regimes.

---

### Slide 13: Initial Dataset

#### Slide Description
* **Header & Title**: *Initial Dataset: 67.2 Million Federal Records & Macro Census*
* **Visual Elements & Layout**:
  - Summary table of the Master Post-ETL Multi-Source Data Foundation Census (Table 4.1 in Thesis v3):
    - **TSA Hourly Throughput**: 1,234,488 records (hourly passenger screening counts across all checkpoint lanes).
    - **BTS On-Time Performance (OTP)**: 39,268,754 flight movement records (gate departure, wheel-off, taxi-out, delay minutes, cancellations).
    - **BTS DB1B Passenger Origin & Destination**: 1,558,797 coupon records (true itineraries, connecting ratios, carrier market share).
    - **BTS Form 41 Financial & Traffic**: conformed route-level load factors.
  - Total Conformed Records: **42,062,039 records** across the Top 25 large hub airfields.
  - Temporal coverage: January 1, 2019 to December 31, 2025 (7 calendar years; 44 continuous post-pandemic months from May 1, 2022 to Dec 31, 2025).

#### Thesis Summary & In-Depth Discussion
* **Scale of the Data Foundation**: The empirical foundation represents one of the largest unified airport landside-airside operational databases in aviation research. By merging hourly TSA checkpoint screening throughput with granular FAA/DOT flight telemetry and DB1B passenger ticket surveys, the study eliminates reliance on simulated or self-reported passenger arrival times.
* **Post-Pandemic Structural Demarcation**: Incorporating data from 2019 through 2025 allowed the research to rigorously examine structural shifts. Autoregressive and structural break analyses demonstrated that passenger travel behaviors during 2020 and 2021 were structurally dislocated. Establishing the post-pandemic baseline on May 1, 2022, ensured that the predictive models were calibrated against modern, stabilized commercial airline operating patterns.
* **Representativeness of the Top 25**: Capturing 67.2% of all domestic commercial operations, the candidate network reflects the highly congested, banked hub operating conditions where checkpoint queuing volatility is most acute.

---

### Slide 14: The Four-Tier Filtering Funnel

#### Slide Description
* **Header & Title**: *The Four-Tier Filtering Funnel: Purposive Cohort Extraction*
* **Visual Elements & Layout**:
  - Funnel diagram illustrating the sequential elimination of confounding terminal environments across four hierarchical tiers:
    - **Tier 1 (Macro: Airfield Operational Scale)**: 450+ Commercial Airfields $\to$ Top 25 Large Hubs ($\ge 90,000$ operations; 67.2% US traffic).
    - **Tier 2 (Meso: Carrier Longitudinal Stability)**: Continuous Big-Three presence (American, Delta, United) across all 44 post-pandemic months.
    - **Tier 3 (Micro: Checkpoint Carrier Isolation)**: Elimination of consolidated multi-carrier central checkpoints; isolation of dedicated carrier complexes ($\ge 85\%$ departures by dominant carrier).
    - **Tier 4 (Physical: Concourse Geometry & Security Barriers)**: Classification into Physically Separate Terminals vs. Walkway-Connected Terminals with CAT scanner barriers.

#### Thesis Summary & In-Depth Discussion
* **The Necessity of Purposive Filtering**: In observational aviation data, directly predicting airport-wide checkpoint volume introduces severe confounding variables: multiple airlines sharing central checkpoints, passengers drifting between terminals post-security, and unobservable codeshare flows. To isolate the direct relationship between airline flight schedules and security screening arrivals, the research engineered a four-tier filtering funnel.
* **Tier-by-Tier Rationale**:
  - *Tier 1 (Macro)*: Restricts the sample to high-density commercial hubs with sustained passenger queuing demand.
  - *Tier 2 (Meso)*: Selects facilities with continuous operations from the Big-Three legacy carriers (AA, DL, UA), ensuring stable fleet types and standardized operating procedures.
  - *Tier 3 (Micro)*: Enforces strict Carrier Checkpoint Isolation. Airfields with consolidated central checkpoints (e.g., Denver, Seattle, Atlanta Main) were excluded because departing passengers from dozens of airlines merge into a single queuing lobby, making it impossible to attribute passenger arrival bursts to specific carrier flight banks.
  - *Tier 4 (Physical)*: Categorizes terminal security architecture to examine whether physical terminal separation influences predictive generalizability.

---

### Slide 15: Pipeline Results

#### Slide Description
* **Header & Title**: *Pipeline Results: The Nine-Airport Experimental Cohort*
* **Visual Elements & Layout**:
  - Cohort breakdown showing the 9 isolated commercial airports representing 12 carrier-exclusive screening environments:
    - **American Airlines Complexes**: DFW (Terminal D), PHL (Terminals B & C), ORD (Terminal 3).
    - **Delta Air Lines Complexes**: BOS (Terminal A), DTW (McNamara Terminal), LGA (Terminal C), LAX (Terminals 2 & 3).
    - **United Airlines Complexes**: EWR (Terminal C), IAH (Terminal C), ORD (Terminal 1), LAX (Terminal 7), BOS (Terminal B).
  - Comparative KPI metric callouts (Top 9 Cohort vs. Top 25 National Average):
    - **+16.9%** Higher Flight Density (224,576 annual flights vs. 192,160).
    - **+14.1%** Higher Flight Cancellation Rate (1.63% vs. 1.43%).
    - **+25.0%** Higher Local Originating Volume (16.4M vs. 13.1M passengers).

#### Thesis Summary & In-Depth Discussion
* **Statistical Rigor of the Cohort**: The four-tier filtering funnel successfully isolated nine commercial hub airports representing 12 carrier-exclusive screening complexes. This cohort achieves complete balance across the Big Three legacy network carriers (AA: 3 complexes, DL: 4 complexes, UA: 5 complexes) and spans major geographic and climatic regions (Northeast convective/icing, Midwest winter, South convective, West Coast coastal).
* **The Ideal Operational Stress Test**: Compared to the broader Top 25 national average, the 9-airport cohort exhibits 16.9% higher flight movement density, 14.1% higher flight cancellation rates, and 25.0% higher local originating passenger volume. This confirms that the cohort represents an ideal, highly rigorous operational stress test: terminal checkpoints are heavily congested, arrival queues are governed by landside passenger show-up curves rather than airside transfers, and operations are routinely perturbed by weather and air traffic ground delays.

---

### Slide 16: Top 9 Descriptive Statistics (PAX Throughput)

#### Slide Description
* **Header & Title**: *Top 9 Descriptive Statistics: Checkpoint Throughput Dispersion Matrix*
* **Visual Elements & Layout**:
  - Formally formatted APA 7th summary statistics table matching Slide 16 / Table 4.2 in Thesis v3:
    | Airport | Observations ($N$) | Mean ($M$) | Std Dev ($SD$) | Median | Maximum | Dedicated Screening Complex |
    | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
    | **BOS** | 28,400 | 2,243.7 | 1,298.9 | 2,314.0 | 7,341 | Terminals A & B |
    | **DFW** | 28,266 | 3,201.0 | 1,750.2 | 3,597.0 | 7,963 | Terminal D Screening Complex |
    | **DTW** | 32,023 | 1,443.7 | 1,012.1 | 1,629.0 | 4,394 | McNamara Terminal Complex |
    | **EWR** | 32,034 | 2,738.8 | 1,774.6 | 3,094.0 | 6,959 | Terminal C Screening Complex |
    | **IAH** | 28,185 | 2,342.1 | 1,312.2 | 2,666.0 | 6,029 | Terminal C Screening Complex |
    | **LAX** | 30,984 | 4,165.7 | 2,127.4 | 4,450.0 | 9,569 | Terminals 2, 3 & 7 Complexes |
    | **LGA** | 31,438 | 1,687.0 | 1,367.5 | 1,759.0 | 5,496 | Terminal C Screening Complex |
    | **ORD** | 32,036 | 1,985.2 | 1,653.8 | 1,944.0 | 9,380 | Terminals 1 & 3 Complexes |
    | **PHL** | 27,094 | 1,492.2 | 906.7 | 1,560.0 | 6,157 | Terminals B & C Complexes |

#### Thesis Summary & In-Depth Discussion
* **Intra-Day Dispersion and Non-Normality**: The descriptive statistics reveal extreme intraday dispersion across all dedicated screening complexes. While mean throughput ranges from 1,443.7 pax/hr at DTW to 4,165.7 pax/hr at LAX, standard deviations are massive—consistently approaching 50% to 80% of the mean (e.g., LGA: $M = 1,687.0, SD = 1,367.5$; EWR: $M = 2,738.8, SD = 1,774.6$).
* **Peak-to-Trough Operational Swings**: Maximum observed hourly throughput peaks at 7,341 pax/hr at BOS, 7,963 at DFW, 9,380 at ORD, and 9,569 at LAX. These enormous peak-to-trough ratios (often exceeding 10:1 between early morning flight banks and midday valleys) demonstrate the severity of passenger arrival burstiness. Treating passenger flow through daily averages hides the massive, concentrated surges that overwhelm physical screening lanes.

---

### Slide 17: Implications for Model Development

#### Slide Description
* **Header & Title**: *Implications for Model Development: Four Structural Requirements*
* **Visual Elements & Layout**:
  - Four quadrant cards summarizing the architectural rules established by the empirical findings:
    1. *Lead-Lag Show-Up Curves*: Flight departure schedules must be convolved across empirical 90–120 minute show-up horizons ($t+1, t+2, t+3$).
    2. *The Hub Disconnect (Connecting Deflator)*: Checkpoint demand must be scaled by airline connecting ratios ($1 - \text{Connecting Ratio}$) derived from DB1B coupons.
    3. *Terminal Complex Spatial Aggregation*: Analysis must aggregate across dedicated complexes to eliminate lane-type administrative noise.
    4. *Asymmetric Delay Conditioning*: Models must avoid same-hour lookahead delay bias; use prior-hour operational delays ($\text{Delay}_{t-1}$).

#### Thesis Summary & In-Depth Discussion
* **Translating Empirical Discoveries into Model Architecture**: The empirical analysis of federal data dictated four non-negotiable architectural requirements for any valid airport passenger flow model:
  1. *Lead-Lag Asynchrony*: Unshifted scheduled departures in the same hour explain only 11.58% of checkpoint throughput variance ($r = 0.3403$). Explanatory power peaks at Lead $t+1$ and Lead $t+2$ ($R^2 \approx 24\%$), matching the 90-to-120 minute modal show-up window in ACRP Report 40. Convolving flights across a 3-hour empirical arrival curve elevates explained variance to 48.8% ($r = 0.6985$).
  2. *The Hub Disconnect*: At fortress hubs like DFW, DTW, and IAH, over 50% of departing passengers connect airside without passing through landside TSA checkpoints. Treating total aircraft seats as checkpoint demand overestimates screening loads by up to 2.5-fold. Multiplying seats by local origin-destination ratios is mandatory.
  3. *Spatial Complex Aggregation*: Individual screening lane throughput fluctuates erratically due to TSO shift rotations, meal breaks, and tactical queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms noisy operational telemetry into a stable, continuous response signal.
  4. *Information Availability*: Incorporating same-hour flight departure delays introduces severe lookahead bias, as actual departure delays cannot be known until aircraft push back from gates. Models must utilize strictly lagged operational metrics ($\text{Delay}_{t-1}$) to preserve real-world forecasting validity.

---

### Slide 18: Model Development & Execution

#### Slide Description
* **Header & Title**: *Model Development & Execution: Metric Standards & Conformal Buffers*
* **Visual Elements & Layout**:
  - Three structured panels corresponding to the core sub-topics:
    - **Panel 1: Dispersion Scale vs. Volume Scale**: Contextualizing error metrics. Mean throughput is ~1,750 pax/hr; diurnal standard deviation is 540–880 pax/hr. An RMSE of ~220 pax/hr represents an exceptionally close fit against intraday arrival swings.
    - **Panel 2: MASE as the Primary Standard**:
      $$\text{MASE} = \frac{\text{MAE}_{\text{model}}}{\text{MAE}_{\text{persistence}}}$$
      $\text{MASE} < 1.000 \implies$ Outperforms daily persistence; $\text{MASE} < 0.850 \implies$ Substantial skill; $\text{MASE} < 0.700 \implies$ Exceptional accuracy.
    - **Panel 3: Conformal Staffing Buffers**: Transforming predicted throughput volatility ($\hat{\sigma}$) directly into risk-adjusted lane capacity cushions.

#### Thesis Summary & In-Depth Discussion
* **Interpreting Error on the Dispersion Scale**: A critical contribution of Thesis v3 is clarifying how model error metrics must be interpreted. In traditional volume forecasting, an RMSE of 220 passengers might appear substantial against a quiet overnight period. However, in volatility modeling, where diurnal standard deviations average 540 to 880 pax/hr, an RMSE of 220 pax/hr indicates that the model tracks the sharp morning and afternoon passenger arrival spikes with remarkable fidelity.
* **The Mathematical Elegance of MASE**: Mean Absolute Scaled Error (MASE; Hyndman & Koehler, 2006) serves as the primary benchmark metric because it is scale-free, numerically stable, and benchmarked directly against non-parametric daily persistence ($\text{MASE}_{\text{persistence}} \equiv 1.000$). Unlike percentage errors (MAPE) that explode toward infinity during low-volume overnight hours, MASE provides an unconfounded, scale-invariant measure across both moderate-sized complexes (PHL) and mega-terminals (LAX).
* **Conformal Staffing Buffers in Practice**: Rather than staffing checkpoints to match expected mean passenger volume (which guarantees queue backlogs 50% of the time under high arrival variance), security directors can use predicted volatility ($\hat{\sigma}_{\text{TSA}}$) to calculate conformal safety buffers. Checkpoint lane rosters are sized to cover $\hat{\mu} + k\hat{\sigma}$, guaranteeing designated service-level queue wait times without chronic overstaffing.

---

### Slide 19: Model Development (Four Candidate Paradigms)

#### Slide Description
* **Header & Title**: *Model Development: The 3-Model Candidate Evaluation Suite & Control*
* **Visual Elements & Layout**:
  - Four-column paradigm architecture cards:
    - **Baseline Control**: Naive Daily Persistence ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$, non-parametric $\text{MASE} \equiv 1.000$).
    - **Model 1 (Deterministic Flight Schedule Model)**: ACRP Report 40 Show-Up Curve Convolution ($t+1, t+2, t+3$), zero ML overhead.
    - **Model 2 (Supervised Machine Learning Model)**: Gradient-Boosted Decision Trees with 24 BTS OTP operational flight attributes.
    - **Model 3 (Dynamic Two-Stage Hybrid Model)**: Sequential Schedule Baseline coupled with Live 1-Step Error Innovation Feedback ($e_{t-1}$).
  - Calibration Dataset Partitioning Table (Table 4.5 in Thesis v3):
    - Training Partition: 15,976 complex-days (May 1, 2022 – Dec 31, 2024).
    - Validation Partition: 3,293 complex-days.
    - Operational Purge Buffer: 7 days (168 hours) to prevent leakage.
    - Out-of-Time Holdout Partition: 3,222 complex-days (72,053 hourly observations; full-year 2025).

#### Thesis Summary & In-Depth Discussion
* **The Candidate Modeling Suite**: The thesis evaluates three candidate predictive frameworks representing fundamentally distinct operational paradigms, benchmarked against an empirical baseline control:
  1. *Baseline Control (Daily Persistence)*: Assumes today's hourly volatility mirrors yesterday's observed values ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$).
  2. *Model 1 (Deterministic Operational Baseline)*: Relies strictly on published airline flight timetables, convolving scheduled departing seats across empirical ACRP Report 40 passenger arrival distributions ($t+1, t+2, t+3$). It requires no machine learning infrastructure, live data feeds, or historical delay telemetry.
  3. *Model 2 (Supervised Machine Learning)*: An automated Gradient-Boosted Decision Tree regressor trained across convolved flight features and 24 BTS OTP operational covariates (rolling delays, cancellations, taxi queues).
  4. *Model 3 (Dynamic Two-Stage Hybrid)*: Combines the structural stability of the Model 1 schedule baseline with live recursive error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from physical checkpoint sensors.
* **Strict Experimental Partitioning & The Purge Buffer**: To eliminate autoregressive lookahead contamination and temporal data leakage, an immutable 7-day (168-hour) operational purge buffer was inserted between the training/validation period and the prospective 2025 holdout dataset. Models were completely frozen prior to holdout evaluation.

---

### Slide 20: Model Performance (Overall Holdout Benchmarks)

#### Slide Description
* **Header & Title**: *Model Performance: Full-Year 2025 Holdout Evaluation Matrix*
* **Visual Elements & Layout**:
  - Full-width APA 7th benchmark performance table matching Table 4.6 in Thesis v3 / Table 4.10 in the pipeline:
    | Predictive Architecture | Out-of-Time $R^2$ | RMSE (pax/hr) | MAE (pax/hr) | Holdout MASE | Systematic Bias (pax/hr) |
    | :--- | :---: | :---: | :---: | :---: | :---: |
    | **Baseline Control (Persistence)** | 0.000 | 253.6 | 198.4 | 1.000 | 0.0 |
    | **Model 1 (Deterministic Schedule)** | 0.498 | 313.4 | 187.6 | 0.945 | -42.1 |
    | **Model 2 (Supervised Machine Learning)** | 0.697 | 273.5 | 138.2 | 0.696 | -18.4 |
    | **Model 3 (Dynamic Two-Stage Hybrid)** | **0.748** | **222.1** | **131.4** | **0.662** | **-6.2** |
  - Statistical significance callout: Diebold-Mariano loss differential test confirms error reductions are statistically decisive across all 9 airports ($DM = 42.15, p < 0.0001$ for Model 2; $DM = 48.72, p < 0.0001$ for Model 3).

#### Thesis Summary & In-Depth Discussion
* **Prospective Holdout Validation**: The out-of-time 2025 holdout evaluation spans 3,222 complex-days and 72,053 hourly screening observations. Because this data was strictly withheld during all training and tuning phases, the results reflect genuine real-world operational forecasting performance.
* **Analysis of Empirical Performance Hierarchy**:
  - *Baseline Control*: Serves as the non-parametric anchor ($\text{MASE} \equiv 1.000, \text{RMSE} = 253.6\text{ pax/hr}$).
  - *Model 1 (Deterministic)*: Explains 49.8% of holdout arrival volatility variance ($R^2 = 0.498, \text{MASE} = 0.945$). Published flight schedules provide an effective baseline, outperforming daily persistence by 5.5%. However, because Model 1 is completely blind to live airside flight delays, it exhibits a persistent negative forecast bias of -42.1 pax/hr (systematically underestimating crowds when delays push passengers into later hours).
  - *Model 2 (Supervised ML)*: Incorporating 24 BTS OTP delay and cancellation features increases explained variance to 69.7% ($R^2 = 0.697$) and reduces error to $\text{MASE} = 0.696$ and $\text{RMSE} = 273.5\text{ pax/hr}$, successfully hitting the $\text{MASE} < 0.700$ target.
  - *Model 3 (Dynamic Hybrid)*: Injects real-time checkpoint floor feedback ($e_{t-1}$), achieving the highest overall statistical fit: $R^2 = 0.748$, $\text{RMSE} = 222.1\text{ pax/hr}$, $\text{MASE} = 0.662$, and capping systematic forecast bias at just -6.2 pax/hr.

---

### Slide 21: Model Performance (Multi-Pillar Hypothesis Matrix)

#### Slide Description
* **Header & Title**: *Model Performance: Multi-Pillar Testing & Asymmetric Trade-Offs*
* **Visual Elements & Layout**:
  - Comprehensive 3-pillar evaluation matrix matching Table 4.7 in Thesis v3 / Table 4.11 in the pipeline:
    | Evaluation Dimension | Operational Regime & Metric | Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Supervised ML) | Model 3 (Dynamic Hybrid) | Winning Paradigm |
    | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
    | **Dimension 1: Robustness** | Routine On-Time Ops ($\text{MASE}_{\text{routine}}$) | $< 0.700$ | 1.000 | 0.945 | **0.696** *(Target Met)* | **0.662** *(Target Met)* | **Model 3 (Accuracy)** / **Model 2 (Pareto)** |
    | | Routine Absolute Error ($\text{RMSE}_{\text{routine}}$) | Lowest | 253.6 | 313.4 | 273.5 | **222.1** | **Model 3** |
    | **Dimension 2: Resilience** | Severe IROPS Error Multiplier ($R_{\text{MASE}}$) | $\approx 1.00$ | 1.000 | 1.14 | 2.14 *(Fragile Collapse)* | **1.05** *(Target Met)* | **Model 3 DECISIVE WINNER** |
    | | Severe Disruption Error ($\text{MASE}_{\text{shock}}$) | Lowest | 1.000 | 1.082 | 0.812 | **0.694** *(Target Met)* | **Model 3 DECISIVE WINNER** |
    | | Time-to-Recovery ($\text{TTR}$, hours) | $< 4.0\text{h}$ | N/A | 7.8h | 5.4h | **2.8h** *(Target Met)* | **Model 3 DECISIVE WINNER** |
    | **Dimension 3: Generalizability** | Zero-Shot Transfer Ratio (EWR $\to$ LGA $\text{RTR}$) | $\approx 1.00$ | N/A | **1.04** *(Target Met)* | 1.08 | 1.19 *(Failed Target)* | **Model 1 DECISIVE WINNER** |
    | | Transfer Error Degradation ($\Delta\text{MASE}$) | $\le 10.0\%$ | N/A | **+4.0\%** *(Target Met)* | +7.9\% | +21.5\% *(Failed Target)* | **Model 1 DECISIVE WINNER** |

#### Thesis Summary & In-Depth Discussion
* **Empirical Validation of Hypothesis $H_1$**: The multi-pillar evaluation matrix provides definitive, empirical proof of Master Hypothesis $H_1$: *no individual predictive modeling paradigm is universally superior across all three operational performance measures*. Each framework possesses distinct operational strengths and stark asymmetric trade-offs:
  - **Robustness ($H_{1a}$ Confirmed)**: Both Model 2 ($\text{MASE} = 0.696$) and Model 3 ($\text{MASE} = 0.662$) satisfy the routine target ($\text{MASE} < 0.700$). While Model 3 minimizes absolute error, Model 2 achieves Practical Pareto Efficiency—meeting the target with zero real-time floor telemetry and zero compute latency.
  - **Resilience ($H_{1b}$ Confirmed)**: During severe irregular operations (delays $\ge 45$ min or cancellations $\ge 5$), Model 3 is the undisputed champion: $R_{\text{MASE}} = 1.05$, $\text{MASE}_{\text{shock}} = 0.694$, and $\text{TTR} = 2.8\text{h}$. Pure machine learning (Model 2) suffers a catastrophic fragility collapse ($R_{\text{MASE}} = 2.14, \text{TTR} = 5.4\text{h}$) due to the Empty Checkpoint Fallacy.
  - **Generalizability ($H_{1c}$ Confirmed)**: Under zero-shot spatial transfer (EWR $\to$ LGA) without local retraining, Model 1 is the decisive champion: $\text{RTR} = 1.04$ and $\Delta\text{MASE} = +4.0\%$. Conversely, Model 3 decisively fails the generalizability target ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$) because its decision trees overfit to Newark's specific terminal geometry and flight-bank timing structures.

---

### Slide 22: Importance of Dynamic Performance Measures

#### Slide Description
* **Header & Title**: *Importance of Dynamic Performance Measures: The Evaluation Triad*
* **Visual Elements & Layout**:
  - Three-axis Radar Chart / Triad Architecture Diagram illustrating the operational coverage of each modeling framework across:
    - **Axis 1: Robustness** (Nominal on-time accuracy; routine staffing optimization).
    - **Axis 2: Resilience** (Shock resistance during convective IROPS ground stops; rapid recovery).
    - **Axis 3: Generalizability** (Spatial portability across terminal geometries without retraining).
  - Visual summary demonstrating that each model covers a distinct sector of the operational radar, proving that single-metric evaluations are fundamentally inadequate.

#### Thesis Summary & In-Depth Discussion
* **The Danger of Monolithic Metrics**: In conventional academic literature, models are selected based on global $R^2$ or aggregate RMSE. In airport operations, selecting a model based solely on global metrics creates critical blind spots. An operator deploying Model 3 based on its superior holdout RMSE (222.1 pax/hr) would experience severe forecast degradation (+21.5% error surge) if transferring it to a new terminal without months of local retraining. Conversely, deploying Model 2 would result in catastrophic under-prediction during severe summer thunderstorms.
* **The Operational Triad Defined**:
  - *Robustness*: Measures routine consistency and advance planning efficiency. Essential for long-term shift scheduling 48 to 72 hours prior.
  - *Resilience*: Measures tactical survivability under severe operational turbulence. Essential for emergency operations centers during convective line halts.
  - *Generalizability*: Measures architectural portability. Essential for airport authorities managing multi-airport systems (e.g., PANYNJ: EWR, LGA, JFK) seeking a universal baseline model without facility-specific engineering.

---

### Slide 23: Discussion and Analysis of Results

#### Slide Description
* **Header & Title**: *Discussion and Analysis: Spatial Architecture & Behavioral Dynamics*
* **Visual Elements & Layout**:
  - Conceptual diagrams illustrating the three core physical mechanisms identified in the thesis:
    1. *Connecting Passenger Shielding (The Hub Disconnect)*: Fortress hubs vs. Origin & Destination (O&D) facilities.
    2. *Terminal Complex Spatial Aggregation*: Dedicated carrier complexes acting as natural statistical filters.
    3. *Behavioral Invariance Across Terminal Layouts*: The role of checked luggage and TSA Credential Authentication Technology (CAT) scanners as behavioral barriers.
    4. *The Empty Checkpoint Fallacy Unpacked*: Visualizing the airside vs. landside discrepancy during ground stops.

#### Thesis Summary & In-Depth Discussion
* **Spatial Architecture Dictates Model Efficacy**: The empirical findings confirm that terminal spatial layout directly governs forecasting performance.
  - *Connecting Passenger Shielding*: At fortress hubs like DFW, DTW, and IAH, connecting passengers transfer seamlessly airside between concourses, shielded from landside security checkpoints. Consequently, airside flight delay cascades at connecting hubs have a muted direct impact on security screening lines. Conversely, at high-originating facilities like LGA and EWR, checkpoint throughput is tightly coupled with local landside access; an airside delay immediately strands local travelers in the ticketing hall.
  - *Behavioral Invariance Across Layouts*: The research revealed econometric equivalence between physically separate terminal buildings (e.g., LGA Terminal C) and walkway-connected terminals (e.g., DFW Terminal D). Digital TSA CAT scanners and checked baggage drop requirements act as rigid behavioral barriers that prevent post-security passenger cross-over between carrier complexes.
  - *Mechanism of the Empty Checkpoint Fallacy*: During severe convective ground stops, departure flights are cancelled or delayed on dispatch boards. Pure machine learning models lack physical presence sensors and interpret missing flights as zero passenger arrivals. Dynamic hybrids overcome this through recursive error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$), immediately detecting accumulated passenger mass landside.

---

### Slide 24: Real World Application (The Operational Playbook)

#### Slide Description
* **Header & Title**: *Real World Application: The Airport Operator & TSA Decision Playbook*
* **Visual Elements & Layout**:
  - Three actionable operational policy directives for airport authorities and TSA leadership:
    - **Recommendation 1: Dynamic Checkpoint Rostering**: Abandon static tables; implement empirical lead-lag ($t+1, t+2$) flight bank schedules convolved with conformal volatility buffers ($\hat{\mu} + k\hat{\sigma}$).
    - **Recommendation 2: Connecting Ratio Integration**: Scale flight bank capacity dynamically by BTS DB1B coupon origin-destination ratios ($1 - \text{Connecting Ratio}$).
    - **Recommendation 3: The Regime-Switched Gated Inference Engine**: A dual-track operational architecture deploying Model 2 for routine scheduling and dynamically gating to Model 3 feedback during IROPS.

#### Thesis Summary & In-Depth Discussion
* **Actionable Policy Directives for Airport Operations**: Thesis v3 translates empirical conclusions into a concrete operational playbook for airport operators, airline hub directors, and TSA Federal Security Directors (FSDs):
  1. *Dynamic Checkpoint Rostering*: TSA shift supervisors should replace rigid time-of-day tables with dynamic rosters driven by empirical two-hour lead ($t+2$) flight bank schedules. Checkpoint lane rosters should incorporate conformal safety buffers proportional to predicted throughput volatility ($\hat{\sigma}$), protecting checkpoints against sudden arrival spikes without incurring chronic overtime costs.
  2. *Connecting Ratio Integration*: Centralized security dispatchers at connecting hub airports must dynamically deflate scheduled flight seats using empirical DB1B connecting ratios, eliminating the chronic overstaffing that results from treating transferring passengers as landside screening demand.
  3. *The Regime-Switched Gated Inference Engine*: Airport operations centers should implement a condition-responsive forecasting architecture. During nominal operating conditions (delays $< 15$ min), the system runs Supervised Machine Learning (Model 2), delivering high-precision advance rosters with zero live sensor compute overhead. When convective ground stops or severe delays occur (delays $\ge 45$ min or cancellations $\ge 5$), the inference engine automatically switches to the Dynamic Two-Stage Hybrid (Model 3), injecting live checkpoint error innovation feedback ($e_{t-1}$) to stabilize forecasts and guide tactical lane recovery.

---

### Slide 25: Recommendations for Future Research

#### Slide Description
* **Header & Title**: *Recommendations for Future Research: Methodological Extensions*
* **Visual Elements & Layout**:
  - Four structured research recommendation cards:
    1. *Screening Lane Modality Disaggregation*: Modeling discrete queue splits between standard screening, TSA PreCheck, and CLEAR lanes.
    2. *Landside Multimodal Telemetry*: Integrating real-time highway traffic sensor feeds, parking shuttle telemetry, and regional rail transit delays.
    3. *Multi-Step Recursive Forecasting*: Extending tactical forecasting horizons from 1 hour ahead to rolling 4-to-6 hour operational windows.
    4. *Single-Facility High-Fidelity Micro Case Studies*: Modeling bespoke concourse geometries, carrier-specific bank timing structures, and local passenger show-up curves without multi-airport confounding variance.

#### Thesis Summary & In-Depth Discussion
* **Avenues for Advancing Aviation Operations Research**:
  1. *Lane-Level Modality Disaggregation*: A recognized boundary of this study was aggregating throughput across entire terminal complexes. Future research should capture micro-level lane dynamics, examining how the proportion of TSA PreCheck versus standard screening passengers alters lane processing rates ($\mu$) and queue balking behaviors.
  2. *Multimodal Landside Telemetry*: Integrating smart-city telemetry—such as municipal highway congestion indexes, automated parking structure occupancy, and public transit arrival feeds—would capture upstream passenger travel friction before travelers physically arrive at terminal curbsides.
  3. *Multi-Step Ahead Forecasting Horizons*: While 1-step ahead recursive forecasting ($t+1$) provides exceptional tactical fidelity, extending the mathematical framework to multi-step recursive horizons ($t+2$ through $t+6$) would allow airport operations centers to plan gate holds and tarmac ground delays hours in advance.
  4. *Single-Airport Longitudinal Deep Dives*: Conducting focused, single-airport investigations would enable researchers to model carrier-specific gate pushback queues and bespoke local show-up curves without the confounding variance inherent in nationwide multi-airport cohorts.

---

### Slide 26: Conclusion & Final Remarks

#### Slide Description
* **Header & Title**: *Conclusion & Final Remarks: Paradigm Shift to Volatility-Aware Operations*
* **Visual Elements & Layout**:
  - Summary synthesis card highlighting the major contributions of the thesis:
    - **Paradigm Shift**: Airport passenger flow is governed by *throughput volatility* and arrival burstiness ($C_a^2$), not static volume.
    - **Hypothesis Confirmation**: Empirical proof of the Asymmetric Trade-Off ($H_1$) across 44 continuous post-pandemic months and 72,053 holdout observations.
    - **Operational Synergy**: Deterministic physics generalize best; machine learning optimizes routine staffing; dynamic hybrid feedback survives disruptions.
    - **Capital Optimization**: Synchronizing flight schedules, connecting deflators, and live floor telemetry optimizes existing airport capacity through software intelligence rather than costly physical expansion.

#### Thesis Summary & In-Depth Discussion
* **Synthesis of Research Contributions**: This graduate thesis resolves a fundamental operational disconnect in commercial aviation. By demonstrating that passenger queue formation is governed by Kingman's heavy-traffic volatility dynamics rather than static passenger volumes, the research establishes that security screening checkpoints must be managed through the lens of throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$).
* **The Strategic Legacy of the Asymmetric Trade-Off**: Through prospective out-of-time holdout testing across 44 post-pandemic months, the research proved that no single predictive model is universally optimal. Deterministic flight schedule convolution (Model 1) delivers superior zero-shot spatial portability across facilities; supervised machine learning (Model 2) achieves optimal Pareto efficiency for routine advance staffing; and dynamic two-stage hybrid models (Model 3) are essential for surviving convective weather disruptions and overcoming the Empty Checkpoint Fallacy.
* **Transforming Airport Operations**: Ultimately, these findings prove that commercial airports and federal security authorities can achieve substantial capacity optimization without capital-intensive physical expansions. By synchronizing airside flight schedules, connecting passenger deflators, and real-time floor telemetry within a condition-responsive regime-switched architecture, airports can transform passenger security checkpoints from reactive bottlenecks into proactive, resilient, and synchronized operational systems.
