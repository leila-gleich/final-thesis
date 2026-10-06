# Chapter I

# Introduction

## Context and Operational Motivation
As commercial air travel demand continues to outpace the capacity of landside airport terminal infrastructure, inefficient resource allocation at passenger security screening checkpoints has emerged as a critical operational bottleneck across the National Airspace System (NAS; Adacher et al., 2017). Airport terminal operators and federal security authorities face the dual challenge of sustaining stringent screening standards while minimizing passenger queue delays. Traditionally, terminal passenger flow forecasting has relied on static, time-of-day planning tables or direct proportional scaling of published airline flight schedules. However, the systemic demand shocks and operational disruptions of the post-pandemic era have exposed severe structural flaws in these conventional forecasting approaches (Hopfe et al., 2024).

A foundational limitation of existing aviation terminal research is the conflation of **passenger throughput volume** (the first-order moment: average flow $\mu$, passengers per hour) and **passenger throughput volatility** (the second-order moment: variance $\sigma^2$, dispersion $\sigma$, and scale-free coefficient of variation $CV = \sigma / \mu$). In stochastic queuing theory (Kingman, 1961; Allen-Cunneen approximation for $G/G/s$ queue systems), expected passenger waiting time ($W_q$) does not scale merely with average arrival rate ($\lambda$), but escalates linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint lane utilization. 

As screening lanes approach saturation ($\rho \to 1.0$), arrival volatility generates acute queue spikes, lane starvation, and severe passenger processing delays that propagate downline into delayed aircraft boarding and gate pushback holds ($r = +0.4375, p < 0.05$). While mean throughput volume is largely governed by published flight schedules, average aircraft gauge, and seasonal calendar demand, **throughput volatility** governs terminal crowd surges, operational instability, and checkpoint staffing failure.

Conventional forecast evaluation in transportation planning has historically emphasized average error metrics—such as Root Mean Squared Error (RMSE) or Mean Absolute Percentage Error (MAPE)—evaluated under routine, undisturbed operating conditions. Yet, in volatile airport operating environments, an evaluation framework based solely on nominal-day volume accuracy is insufficient. A forecasting model that achieves low average error during calm, clear-weather periods may fail catastrophically during severe convective weather ground delay programs, unexpected terminal lane closures, or sudden schedule collapses.

In modern airport operations, the most valuable predictive model is not necessarily the one with the lowest marginal error under ideal conditions, but the model that:
1. **Remains reliable during routine operations (Robustness)**: Providing consistent, low-error baseline volatility forecasts during undisturbed flight banks.
2. **Maintains stability and recovers rapidly during disruptions (Resilience)**: Absorbing severe exogenous shocks (such as winter freeze events or summer convective ground delay programs) without generating false demand collapses or runaway queue backlogs.
3. **Transfers effectively across operational contexts (Generalizability)**: Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study systematically examines the suitability of predictive modeling frameworks—spanning deterministic operational baselines (such as persistence and scheduled flight bank dispersion), data-driven decision-tree architectures (automated rule-based machine learning models), and sequential two-stage hybrid models (combining schedule baselines with real-time error correction)—for forecasting Transportation Security Administration (TSA) checkpoint throughput volatility across routine, volatile, and disrupted demand regimes.

## Significance of the Study
This research contributes to both transportation science theory and practical airport operations by advancing a multidimensional, regime-aware volatility evaluation framework:
1. **Queuing Theory Grounding**: By shifting the predictive target from raw volume levels to arrival dispersion and coefficient of variation ($CV_{\text{TSA}}$), the research directly addresses the operational root cause of airport queue surges identified in heavy-traffic queuing principles ($W_q \propto C_a^2$).
2. **The "Values versus Volatility" Paradigm**: The study resolves a foundational empirical question in aviation analytics: *Does forecasting TSA checkpoint volatility require tracking the values (levels/counts) of airside flight features, the volatility (dispersion/variability) of those features, or a dual combined representation?*
3. **Airside-to-Landside Volatility Transmission**: By evaluating all 24 operational attributes from Bureau of Transportation Statistics (BTS) On-Time Performance (Form 234), Form 41 Schedule T-100, and DB1B ticket surveys across the Top 25 commercial airfields, this research establishes the first empirical factor weighting hierarchy for checkpoint volatility, proving that flight departure delay volatility ($\text{CV}_{\text{delay}}$) is the primary operational driver of landside screening turbulence ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$).
4. **Actionable Operational Decision Tools**: By identifying the conditions under which distinct predictive modeling paradigms maintain operational fidelity, this research provides airport Federal Security Directors (FSDs), airline hub operations managers, and FAA planners with data-driven decision tools. Specifically, it establishes conformal quantile prediction bounds ($\hat{y}_{0.85}$) to dynamically size screening lane buffers, preventing the severe under-prediction common during convective weather delay cascades.

## Statement of the Problem
Airport passenger arrivals and queuing behaviors are inherently uncertain and fluctuate dynamically based on departure bank structures, traveler booking characteristics, and air traffic disruptions (Cheng et al., 2012; Dönmez et al., 2025). Existing models for managing passenger security screening demand frequently rely on static time-of-day curves or pre-pandemic operational assumptions that fail to reflect contemporary travel patterns (Ebert et al., 2021).

This mismatch between checkpoint lane allocation and fluctuating passenger demand contributes to chronic congestion at peak hours, excessive passenger wait times, and inefficient staffing utilization. Crucially, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond aggregate, undisturbed volume accuracy metrics. Because modern airport operations cannot be assumed to follow static, deterministic flight schedules, the absence of an operational volatility forecasting framework leaves airport authorities at risk of deploying decision tools that collapse during sudden operational disruptions or fail when deployed across unfamiliar terminal complexes.

## Purpose Statement
The primary objective of this research is to evaluate and compare predictive modeling frameworks—including deterministic time-series baselines, operational decision-tree models, and sequential two-stage hybrid architectures—to forecast the **volatility of TSA checkpoint passenger throughput**, optimizing airport checkpoint capacity through data-driven operational decision tools rather than costly capital facility expansion.

By analyzing the empirical relationship between airside flight operations and landside TSA security throughput across the Top 25 U.S. commercial airfields from 2019 to 2025, this study assesses model performance against three primary operational criteria: **Robustness**, **Resilience**, and **Generalizability**. Rather than seeking a single, universally optimal model, this research determines which forecasting frameworks perform best under each operational demand state, providing airport authorities with the empirical justification needed to deploy regime-switched forecasting systems.

## Research Questions
This thesis investigates three interconnected research questions:
1. **Primary Forecasting Architecture Question**: Which predictive modeling frameworks—spanning deterministic persistence controls, deterministic schedule dispersion baselines, supervised machine learning tree ensembles, and sequential two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts) as the primary operational evaluation metric?
2. **Feature Representation Paradigm Question**: Does accurately predicting TSA throughput volatility require tracking the **values** (levels, volumes, and counts) of BTS On-Time Performance (OTP) features, the **volatility** (dispersion, standard deviations, and coefficients of variation) of those features, or a dual **hybrid/combined** representation?
3. **Cross-Dataset Volatility Transmission Question**: How do specific airside flight operational attributes (such as departure delays, tactical cancellations, and schedule bank concentration) transmit volatility across the airside-landside boundary into landside checkpoint screening queues?

## Delimitations
1. **Geographic Scope**: This study evaluates commercial air traffic and security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications, capturing 67.2% of nationwide domestic flight departures.
2. **Temporal Scope**: The longitudinal dataset spans January 1, 2019 through December 31, 2025 ($N = 22,491$ airport-days; 42.06 million conformed fact records). Model training and evaluation are focused on the verified post-pandemic operational regime starting May 1, 2022 (following the nationwide rescission of federal transportation mask mandates), reserving the full 12-month calendar year of 2025 (3,222 airport-days) as a strict out-of-time holdout evaluation window.
3. **Data Sources**: Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including TSA Freedom of Information Act (FOIA) hourly screening logs per physical lane, Bureau of Transportation Statistics (BTS) On-Time Flight Performance records (Form 234; capturing flight-level departure delays and cancellations), BTS Schedule T-100 Segment traffic (reporting monthly aircraft seating capacity and load factors), and BTS DB1B/DB1C 10% ticket coupon surveys (identifying local originating vs. airside connecting passenger proportions).
4. **Evaluation Standards**: Model performance is measured using rigorous operational forecasting metrics: Root Mean Squared Error (RMSE; capturing overall forecast spread while penalizing peak-hour misses), Mean Absolute Scaled Error (MASE; scaling errors against a simple persistence baseline where values below 1.0 indicate superior skill), the Disruption Error Multiplier ($R_{\text{MASE}}$; measuring whether forecast errors grow or remain stable during severe storm disruptions), the Relative Transfer Ratio (RTR; assessing the accuracy penalty when deploying a model to a new airport without retraining), and Diebold-Mariano tests for statistical significance.

## Limitations and Assumptions
1. **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
2. **Passenger Checked Baggage and Curb Dwell**: Granular airline bag-drop and ticket counter processing logs are proprietary to individual air carriers. The analysis incorporates passenger show-up distributions established in ACRP Report 40 (*Airport Passenger Terminal Planning and Design*; Transportation Research Board, 2010) as empirical representations of pre-security lead times.
3. **Connecting Passenger Surveys**: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.
4. **Operational Exogeneity**: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234.

---

# Chapter II

# Review of the Relevant Literature

## Traditional Approaches and Operational Complexity
As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays, boarding holds, and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### Uncertainty, Batch Arrival Dynamics, and Flight Banks
A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated "batches" induced by airline flight bank scheduling (Cheng et al., 2012; Peterson et al., 1995). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities. Consequently, landside screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

### Classical Queuing Theory: First Moment (Volume) vs. Second Moment (Volatility)
To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon Queuing Theory (Odoni, 1986; Wang, 2017)—the mathematical study of waiting lines and congestion. Early terminal capacity models utilized Poisson arrival distributions (such as $M/M/s$ or $M/G/s$ queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) relative to an airport's target Level of Service (LOS; industry benchmarks defining acceptable passenger waiting times and crowding thresholds) (Araujo & Repolho, 2015).

However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP; queuing equations where passenger arrival rates vary across hourly intervals to reflect daily peaks and valleys) (Brunetta et al., 1999), NHPP models still evaluate queuing solely through the lens of expected volume (the first-order moment: $\mu = E[Y]$). 

In operational reality, heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993) demonstrate that expected queue wait times ($W_q$) and queue backlogs in general $G/G/s$ screening facilities scale not with mean volume, but linearly with the **squared coefficient of variation of arrival times ($C_a^2$) and service times ($C_s^2$)** via the Allen-Cunneen approximation:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
where $\rho = \frac{\lambda}{s \mu}$ represents checkpoint utilization. As checkpoint utilization approaches capacity ($\rho \to 1.0$) during morning and evening departure peaks, any increase in arrival volatility ($C_a^2$) triggers exponential queue length expansion and terminal crowd surges. Modeling and forecasting **throughput volatility** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is therefore the vital prerequisite for robust lane staffing and queue stability (Adeke, 2018; Guo et al., 2022).

## The "Values versus Volatility" Paradigm in Transportation Demand
In modern econometric and volatility forecasting literature (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005), a central research question is whether predicting the volatility of a stochastic process requires tracking the **values** (levels, volumes, and magnitudes) of explanatory variables, the **volatility** (dispersion, standard deviations, and coefficients of variation) of those variables, or a **dual combined representation**.

In commercial aviation operations, this duality manifests across two operational horizons:
1. **Intraday Diurnal Volatility**: The within-day standard deviation ($\sigma_{\text{TSA, hr}}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($\text{Var}(Y) \propto \mu^p$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor. However, when normalized into scale-free relative burstiness ($CV_{\text{TSA, hr}} = \sigma / \mu$), volume levels lose explanatory power.
2. **Multi-Day Rolling Volatility**: Over multi-day horizons ($\sigma_{\text{TSA, 7d}}$), static flight volumes remain largely unchanged across seasonal schedules. Consequently, models relying exclusively on static feature values fail to anticipate medium-term passenger turbulence. Forecasting disruption-driven turbulence requires tracking the volatility of operational features—specifically rolling schedule variance ($\sigma_{\text{sched}}$), flight cancellation volatility ($CV_{\text{cancel}}$), and departure delay dispersion ($\sigma_{\text{Delay}}$) (Hopfe et al., 2024).

## Simulation Modeling and Real-Time Terminal Management

### Discrete Event Simulation and Operational Limits
To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static spreadsheets, DES models track individual simulated passengers through a chronological sequence of discrete physical milestones: ticket scanning, divestiture (removing shoes, jackets, laptops, and liquids for X-ray inspection), body scanning, and item retrieval.

Despite high visual fidelity, DES models exhibit critical operational limitations when deployed for real-time airport management:
1. **Calibration Sensitivity**: Small changes in baseline assumptions—such as secondary bag-search alarm rates or Transportation Security Officer (TSO; federal screening personnel) divestiture coaching times—produce disproportionately large shifts in modeled queue wait times (Brown & Madhavan, 2011).
2. **Computational Latency**: Simulating hundreds of thousands of individual passenger agents during severe, unfolding flight disruptions requires immense computational time, rendering DES impractical for real-time tactical lane reallocation (Bießlich et al., 2014; Takakuwa & Oyama, 2004).
3. **Passive Traveler Assumptions**: Standard simulation models treat passengers as passive entities following rigid rules, failing to reflect how travelers dynamically adjust arrival timing based on mobile flight delay notifications (Alodhaibi et al., 2017).

## Time-Series Analysis and Data-Driven Predictive Frameworks

### Statistical Time-Series Foundations
To achieve faster, automated forecasts, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). These models predict future hours by capturing the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations. When augmented with exogenous variables (SARIMAX)—such as published airline scheduled seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed historical relationships that cannot accommodate sudden delay cascades.

### Non-Linear Machine Learning and Sequential Neural Networks
To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including deep sequence models such as Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and tree ensembles like Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025).

While deep neural networks can approximate complex multi-source interactions (e.g., weather indices, search engine trends, flight departure status), they introduce significant operational challenges in airport settings:
* **The "Black-Box" Interpretability Hurdle**: Airport Federal Security Directors (FSDs) and TSA operations planners cannot verify why a deep neural network predicts a sudden passenger volume spike, making them reluctant to commit staffing based on opaque model outputs (Adadi & Berrada, 2018; Viaña et al., 2024).
* **Facility-Specific Over-Specialization**: Highly parameterized neural networks tend to memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic terminal layouts and gate configurations, causing their forecast accuracy to degrade sharply when transferred to unfamiliar airports (Wang et al., 2025).

## Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability
To resolve the tension between the transparency of traditional queuing models and the non-linear flexibility of modern machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025).

### Integrating Queuing Principles with Decision-Tree Algorithms
Rather than deploying fully end-to-end black-box models, effective hybrid architectures combine:
1. **First-Principles Operational Baselines**: Using established flight schedules, empirical passenger show-up curves (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010), and airline connecting passenger survey ratios (BTS DB1B) to establish a deterministic baseline volatility estimate.
2. **Transparent Decision-Rule Adjustments**: Deploying interpretable machine learning—specifically Gradient-Boosted Decision Trees—to predict residual volatility shifts caused by real-time flight delays, gate holds, and severe weather cancellations (Ribeiro et al., 2025).

Decision trees offer a critical operational advantage over deep neural networks: their branching structure functions like intuitive, transparent operational rules (e.g., *"If departure delay dispersion exceeds 45 minutes and cancellation rate exceeds 5%, adjust expected security volatility upward by +35%"*).

### Dynamic Feedback and Real-Time State Tracking
During severe operational disruptions (such as summer convective thunderstorm ground stops), static schedules become obsolete. Recent research demonstrates that incorporating recursive error-correction feedback (such as Kalman filtering, which functions like an automated tracking system that compares predicted volatility to actual volatility at time $t-1$ and immediately updates the expected backlog) allows forecasting models to monitor live checkpoint throughput and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024).

## Multi-Dimensional Operational Evaluation
While predictive modeling literature has historically focused on maximizing point accuracy under nominal operating conditions, the unprecedented disruptions of the COVID-19 pandemic and subsequent recovery demonstrated that single-metric evaluations are fundamentally inadequate (Li et al., 2023; Sun et al., 2022). In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

1. **Robustness (Routine Operational Accuracy)**: The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations (Lin, 2022).
2. **Resilience (Performance Under Severe Disruption)**: The capacity of a forecasting framework to maintain error bounded-ness, resist demand collapse, and recover rapidly during major exogenous shocks, such as Ground Delay Programs (GDP; FAA traffic initiatives holding departures at origin gates during destination weather bottlenecks), severe winter blizzards, and summer convective thunderstorm ground stops (Kazda et al., 2022; Schultz et al., 2021).
3. **Generalizability (Cross-Airport Portability)**: The external validity and portability of trained model structures when deployed across structurally diverse airport terminal complexes without requiring site-specific historical recalibration (Güner & Seçkin Codal, 2024; Tang et al., 2023).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.

---

# Chapter III

# Methodology

## Overview and Research Approach
This chapter details the methodological architecture and empirical framework developed to model, forecast, and optimize passenger security screening throughput volatility at commercial airports. Traditional airport passenger flow modeling has historically focused on predicting mean passenger volume through static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in halls, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queueing network subject to severe non-linear queuing friction and arrival burstiness (De Neufville & Odoni, 2014).

Under heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993; Allen-Cunneen formula for $G/G/s$ queue facilities), expected queue wait time ($W_q$) and queue backlogs escalate not with average passenger arrivals ($\lambda$), but linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
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
* **1_OFF_PEAK**: Low Volatility / Overnight Curfew Period ($T < 0.35$).
* **2_MID_PEAK**: Moderate Volatility / Midday Steady Flow ($0.35 \le T < 0.75$).
* **3_PEAK**: High Volatility / Queuing Turbulence ($T \ge 0.75$).

## Predictive Modeling Frameworks for Throughput Volatility

To determine how to best forecast passenger arrival volatility at airport screening checkpoints, this study evaluates **three candidate models representing three distinct operational paradigms**, benchmarked against an empirical baseline control:

### The Baseline Control Benchmark (Daily Persistence)
* **Operational Logic**: Assumes that checkpoint arrival volatility today will exactly mirror the volatility observed at the exact same hour yesterday ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$).
* **Evaluation Role**: Serves as the non-parametric reference standard ($\text{MASE} \equiv 1.000$). Any operational model worth deploying must prove that it beats this simple historical benchmark.

### Model 1: Deterministic Flight Schedule Model (Operational Baseline)
* **Operational Logic**: Uses published airline flight schedules, shifted forward in time using empirical passenger show-up distributions from ACRP Report 40 (*Airport Passenger Terminal Planning and Design*). 
* **Mechanics**: Because passengers arrive 90 to 120 minutes before takeoff, scheduled flight departure banks are convolved across lead arrival horizons ($t+1, t+2, t+3$). This captures the operational ebb and flow of scheduled flight waves without requiring real-time delay telemetry or statistical machine learning.

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

---

# Chapter IV

# Results

## Initial Exploratory Data Analysis

### Descriptive Statistics
To construct an empirically rigorous, leak-free predictive modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw fact records across four primary federal feeds:
1. **TSA FOIA Checkpoint Logs**: Hourly passenger throughput records disaggregated by physical screening lane.
2. **Bureau of Transportation Statistics (BTS) On-Time Performance (OTP, Form 234)**: Flight-level departure movements tracking scheduled and actual departure times, tarmac taxi-out durations, departure delays, cancellations, and causal delay attributions.
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Monthly carrier-route-equipment records reporting available departing seats, transported revenue passengers, and load factors.
4. **BTS DB1B / DB1C Origin-Destination Ticket Surveys**: A 10% randomized sample of airline passenger itineraries detailing coupon routes, connecting transfer ratios, and true local originating passenger fractions.

Following conformed extraction, automated entity resolution, data cleaning, and star-schema relational synthesis across conformed dimension keys (*dim_date*, *dim_time_block*, *dim_airport*, *dim_airline*, *dim_aircraft*, *dim_checkpoint*), the nationwide post-ETL analytical warehouse retains **42,062,039 conformed records** across the candidate network of the Top 25 U.S. commercial airfields. Table 4.1 documents the post-ETL data foundation census across all four federal data sources.

Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)*

## Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)

Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

## Table 4.2: Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($\sigma = 69,376$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually ($\sigma = 27.76\text{M}$; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period.

Three essential data hygiene protocols were established during warehouse staging to guarantee econometric and machine learning validity:
1. **Spatial Key Resolution and Unidentified Airport Isolation**: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (*dim_checkpoint*). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (*airportId* = 0, flagged with *airportMissing* = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce *airportMissing* = 0 and *airportId* > 0.
2. **Scheduled Checkpoint Closures vs. Missing Sensor Data**: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p = 1.3$, which naturally accommodates real zero counts without producing impossible negative passenger estimates or requiring artificial data smoothing).
3. **Advance vs. Tactical Cancellation Causality**: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting (the error of using future information that an airport operations manager would not possess in real time), advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.

### Temporal Boundaries
A core methodological requirement of this thesis is that **defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset**. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on idiosyncratic facility characteristics rather than learning generalizable aviation temporal dynamics.

#### Post-Pandemic Regime Selection and Structural Break Analysis.
The seven-year dataset captures two unprecedented macroeconomic disruptions: the COVID-19 pandemic demand collapse (2020–2021) and the post-pandemic operational rebound (2022–2025). To identify the point at which commercial aviation resumed structural equilibrium, rolling Welch's $t$-tests, Cumulative Sum (CUSUM) structural break tests, and longitudinal correlation metrics were computed across the Top 25 airfields. Table 4.3a contrasts the candidate temporal demarcation baselines.

Table 4.3a  
*Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network*

## Table 4.3a: Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network

Structural break tests confirmed **May 1, 2022** as the optimal demarcation point for empirical model development:
1. **Federal Transit Mask Mandate Repeal**: The nationwide vacatur of federal transit mask requirements on April 18, 2022 restored unconstrained business and leisure travel behavior. By May 1, 2022, load factors recovered to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stability**: During the acute pandemic (2020–2021), the correlation between scheduled flights and checkpoint throughput spiked to an artificial $r = 0.607$ ($R^2 = 36.85\%$) because airline capacity cuts mirrored strict travel bans. In the post-May 2022 equilibrium, the relationship stabilized to $r = 0.553$ ($R^2 = 30.61\%$), reflecting normalized booking curves.
3. **Partitioning Design**: Candidate B establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations; 215,562 facility-level observations). A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.

### Defining Seasonality
Just as temporal boundaries must be established on the complete Top 25 network, **defining seasonality requires capturing the full variance of nationwide commercial aviation**. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks.

#### Annual Seasonal Regimes and Coupled Volatility.
Airport operational stress is not uniform across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b). The Coupled Volatility Index is defined as:
$$\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$$

Table 4.3b  
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)*

## Table 4.3b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

#### Day-of-Week Cyclical Dynamics and Archetypes.
Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes (Table 4.4a):
1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($19.44\%$ and $20.05\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

Table 4.4a  
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)*

## Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)

#### Diurnal Non-Consecutive Dual Turbulence Peaks.
Rather than dividing the 24 hours of each operational day into arbitrary consecutive time blocks, diurnal hours were categorized by the Operational Turbulence Shock Index ($T(h)$), which evaluates passenger screening surge volatility and flight departure delay dispersion:
* **1_OFF_PEAK (Overnight & Curfew Valley)**: Typically covering 00:00 to 03:00 (3–4 hours/day), where commercial departures are sparse and checkpoint demand is minimal.
* **2_MID_PEAK (Midday Plateau & Transition)**: Covering 08:00 to 13:00/16:00 (4–12 hours/day), characterized by steady passenger screening flow and balanced aircraft turnaround buffers.
* **3_PEAK (High Queuing Turbulence / Dual Peaks)**: Uniquely groups non-consecutive turbulence periods into a single operational regime:
  1. *Morning Bank Surge (05:00–08:00)*: Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr).
  2. *Evening Delay Cascade (14:00/17:00–22:00)*: Driven by upstream flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min).

The cross-classification of the 4 annual seasonal regimes ($\mathcal{S}$), 7 days of the week ($\mathcal{D}$), and 3 diurnal blocks ($\mathcal{H}$) forms an **84-cell interaction tensor** ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$). Across this tensor, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $N_{\text{train}} \ge 50$ (median $N_{\text{train}} = 215$), confirming that defining temporal baselines on the Top 25 airfields establishes ample sample power without sparse-sample estimation bias.

### TSA and OTP Throughput Data
Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airfields reveals fundamental econometric dynamics. Table 4.5 synthesizes the master cross-dataset econometric correlations.

Table 4.5  
*Master Cross-Dataset Econometric Relationships (Top 25 Airfields)*

## Table 4.5: Master Cross-Dataset Econometric Relationships (Top 25 Airfields)

Two overarching empirical insights emerge from Table 4.5:
1. **The Hub Disconnect**: Raw scheduled flight departures explain only 20.90% ($R^2$) of TSA security checkpoint passenger throughput across the Top 25 network ($r = 0.4572, p < 0.05$). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to **44.94%** ($r = 0.6704, p < 0.001$), an increase of +115%. At major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70% to 76% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.
2. **Coupled Volatility and Asynchronous Lag Dynamics**: While raw delay rates show weak same-hour linear correlation with passenger volumes ($r = 0.2019, R^2 = 4.08\%$), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ($CV_{\text{TSA}}$) is significantly coupled with flight departure delay volatility ($r = 0.4375, R^2 = 19.14\%, p < 0.05$). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume tracks tightly with weekly flight departure delay variance ($r = 0.9022, R^2 = 81.40\%, p < 0.01$), reflecting synchronized macro peak seasonal demand across the network rather than landside queues causing airside pushback delays.

### Implications for Subset
The findings from the Top 25 exploratory data analysis establish critical empirical foundations and constraints for subsequent data filtering and model development:
1. **Necessity of Macro-Scale Baseline Derivation**: Establishing temporal boundaries (May 1, 2022 post-mask demarcation) and seasonal dynamics (the 4-regime annual calendar, 3 weekly archetypes, and diurnal dual-peak blocks) on the complete Top 25 network ensures that statistical baselines reflect macroeconomic aviation behavior rather than localized facility noise. This prevents models from overtraining on idiosyncratic scheduling quirks of individual hubs.
2. **Identification of Multi-Carrier Schedule Collinearity**: In shared terminal facilities across the Top 25 airfields, hub carriers coordinate departure banks. Carrier departure schedules exhibit extreme collinearity ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), making it mathematically impossible to separate individual airline passenger contributions in shared checkpoint queues.
3. **Requirement for Checkpoint-Level Carrier Exclusivity**: Because unshifted scheduled departures in the same hour explain only ~20% of raw checkpoint variance at the airport-wide level, isolating pure carrier-checkpoint pairs where single-carrier operations feed dedicated screening lanes is essential to unmask the true empirical lead-lag relationship between flight schedules and landside arrivals.
4. **Strict Partitioning Between Macro Dynamics and Feature Training**: While the Top 25 dataset uncovers seasonal dynamics, cyclical archetypes, and cross-dataset correlations, **these relationships and dynamics must not be used as direct trained regression targets or predictive leakage within the downstream model**. Instead, they justify the purposive filtering pipeline, inform feature architectures (e.g., lead-lag arrival distributions and cyclical encodings), and guide the selection of candidate airfields for experimental modeling.
5. **Evaluating Complete Facilities Before Checkpoints**: During initial candidate screening, commercial airports must be evaluated as whole facilities to verify scale, multi-carrier representation, and operational clusters before isolating dedicated checkpoint complexes.

## Data Filtering and Subset Selection

### Four-Phase Filtering Pipeline
To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, commercial airfields were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling.

The four sequential filtering stages of this pipeline progress as follows:
1. **Phase 1: Macro Filter (Scale and Congestion)**: Filters the national candidate universe of 450+ commercial airfields down to the Top 25 airfields. Enforces queue intensity $\rho(t) \to 1.0$ during departure banks, captures 67.2% of nationwide domestic flight movements, and yields a baseline correlation of $r = 0.4572$ ($R^2 = 20.90\%$) between raw flights and TSA throughput.
2. **Phase 2: Meso Filter (Symmetry and Invariance)**: Narrows the Top 25 airfields to 14 candidate hubs requiring concurrent American Airlines, Delta Air Lines, and United Airlines mainline presence (>10% seat share) while excluding Southwest bimodal arrival mixtures and ultra-low-cost carrier noise. Scheduled flight coupling strengthens to $r = 0.5015$ ($R^2 = 25.15\%$).
3. **Phase 3: Micro Filter (Checkpoint Exclusivity)**: Filters the 14 candidate airfields to nine selected hubs with strict dedicated terminal checkpoints ($P(\text{Carrier} = j^* \mid \text{Checkpoint}) = 1$), eliminating shared-terminal carrier collinearity ($\kappa < 25$). Checkpoint coupling rises to $r = 0.5453$ ($R^2 = 29.74\%$) for raw movements and $r = 0.6466$ ($R^2 = 41.81\%$) when adjusted for DB1B local originating passengers.
4. **Phase 4: Factorial Cohort (Factorial Matrix Balance)**: Finalizes the balanced nine-airport cohort comprising 12 dedicated screening complexes (exactly four dedicated complexes each for American, Delta, and United) across all four operational cluster archetypes, achieving dedicated checkpoint-to-flight coupling of $R^2 = 70.80\%$ to $77.40\%$.

#### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion).
* **Filtering Criteria**: Restrict the national candidate universe of 450+ commercial airports to the Top 25 commercial airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* **Methodological Justification**: In airport queueing dynamics, traffic intensity $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$ determines queue behavior. At small regional airports, passenger flow is sparse ($\rho(t) \ll 0.3$), preventing queue accumulation and causing throughput to mirror unconstrained arrivals without boundary friction. In contrast, Top 25 hub airports reach peak-hour saturation ($\rho(t) \to 1.0$) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue delays and non-linear dynamics required to train and evaluate congestion-aware models.
* **TSA-OTP Relationship Evolution**: Across the nationwide universe of all commercial airfields, the linear correlation between scheduled flight departures and TSA throughput is low ($r \approx 0.35, R^2 \approx 12.25\%$). At the Top 25 macro scale, this relationship strengthens to $r = 0.4572$ ($R^2 = 20.90\%$) for raw volume, and $r = 0.6704$ ($R^2 = 44.94\%$) when deflated by DB1B connecting ratios.

#### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion).
* **Filtering Criteria**: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ($>10\%$ market share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* **Methodological Justification**: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical exogenous airspace conditions ($\delta_t$), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to its passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \approx 105\text{ min}$), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ($\mu_1 \approx 135\text{ min}$ for boarding group maximizers; $\mu_2 \approx 65\text{ min}$ for carry-on business travelers), violating arrival distribution homogeneity.
* **TSA-OTP Relationship Evolution**: In the 14-airfield Meso cohort, eliminating Southwest and ULCC scheduling volatility elevated the scheduled flight to TSA throughput correlation to $r = 0.5015$ ($R^2 = 25.15\%$).

#### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity).
* **Filtering Criteria**: Require strict single-carrier dedicated screening checkpoint complexes ($P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* **Methodological Justification**: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), preventing mathematical separation of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint queues.
* **TSA-OTP Relationship Evolution**: At the airport-wide level for the 9 selected airfields, scheduled flights versus total TSA passengers achieve $r = 0.5453$ ($R^2 = 29.74\%$), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r = 0.6466$ ($R^2 = 41.81\%$). Furthermore, when evaluated at the dedicated checkpoint complex level, carrier-filtered departing seats explain **70.80% to 77.40%** ($R^2$) of checkpoint throughput variance.

#### Phase 4: Factorial Cohort (Factorial Matrix Balance).
* **Filtering Criteria**: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the **9-Airport Experimental Cohort** comprising **12 Dedicated Checkpoint Complexes** across **BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL**.
* **Methodological Justification**: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters, ensuring unconfounded cross-carrier and cross-airport transfer evaluation.
* **Crucial Methodological Distinction**: These evolving correlations and seasonal dynamics serve exclusively to justify the four-tier filtering rationale and confirm data validity. **These relationships and dynamics are not used in training the downstream predictive models**, preserving strict econometric separation and preventing data leakage. Furthermore, the analysis at this stage evaluates the **9 selected airports as complete facilities**, rather than premature facility checkpoints.

### Pipeline Results
The filtering pipeline isolated 9 commercial airfields representing 12 carrier-exclusive screening environments, achieving complete factorial balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

Table 4.6  
*The Nine-Airport Experimental Cohort Factorial Specification*

## Table 4.6: The Nine-Airport Experimental Cohort Factorial Specification

#### Key Airport Selection Contrasts.
* **LGA vs. JFK Selection**: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's state-of-the-art consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* **PHL vs. SLC Selection**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring carrier isolation within Cluster 2.

#### Econometric Validation of Carrier Checkpoint Isolation.
To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed:
1. **Volume Conservation Test**: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $\rho = 1.00 \pm 0.04$ ($R^2 > 0.95$).
2. **Zero-Flight Intercept Test**: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ($\beta_0 = 12.4$ pax/hr, $p = 0.40$).
3. **Cross-Carrier Orthogonality Test**: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ($\beta_{\text{other}} = 0.002, p = 0.62$).
4. **Terminal Layout Invariance Test**: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA, DTW) against walkway-connected terminals (e.g., DFW, LAX) yielded $D = 0.032$ ($p = 0.28$), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput leakage.

### Descriptive Statistics for Subset

Table 4.7 presents the descriptive summary statistics for the nine-airport experimental cohort compared against the Top 25 candidate universe.

Table 4.7  
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe*

## Table 4.7: Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe

Compared to the broader Top 25 network, the 9-airport cohort exhibits:
* **Higher Flight Movement Density**: Scheduled flights are +16.9% higher (224,576 vs. 192,160), ensuring screening checkpoints operate under heavy, bank-synchronized arrival loads.
* **Higher Delay and Cancellation Exposure**: Average departure delay is +7.2% higher (15.23 min vs. 14.21 min), cancellation rate is +14.1% higher (1.63% vs. 1.43%), and taxi-out time is +4.5% higher (20.59 min vs. 19.69 min), reflecting genuine operational congestion.
* **Higher Local Originating Demand**: Local originating passenger share is +8.1% higher (52.55% vs. 48.61%), and true local originating volume is +25.0% higher (16.38M vs. 13.10M), concentrating demand directly into landside security checkpoint queues.

#### Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports.

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airfields display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 reports the day-of-week passenger throughput distribution across the nine airports.

Table 4.8  
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports*

## Table 4.8: Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports

The 9 airports exhibit three distinct weekly demand dynamics:
1. **The Pure Corporate Profile (LGA)**: LaGuardia exhibits an extreme day-of-week ratio of **2.30**. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.
2. **The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW)**: These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).
3. **The Energy Sector & Midweek Profile (IAH, ORD)**: Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate travel schedules, followed by steep Saturday troughs.

### Implications for Model
The empirical findings from subset selection dictate essential modeling choices:
1. **Separation of Dedicated Checkpoint Complexes from Airport Aggregates**: Modeling passenger security throughput at the entire airport level confounds multi-carrier flight banks and masks terminal-specific surges. Models must be trained and evaluated at the **dedicated screening complex grain** ($Y_{kt}$), mapping carrier-exclusive flight banks to dedicated screening lanes.
2. **Deflating Capacity by Connecting Ratios**: Because connecting passengers bypass security queues, departing flight seats must be deflated by $(1 - \text{ConnectingRatio}_{\text{airport}})$ from DB1B surveys. Failure to apply this deflator causes models to overpredict checkpoint volume by over 200% at connecting hubs (DFW, DTW, ORD).
3. **Handling Asymmetric Delay Information**: Same-hour flight delay information cannot be used in real-time forecasting without creating lookahead bias, because actual departure delays are not known until after flights push back. Instead, prior-hour delays ($t-1$) and tactical cancellations provide actionable indicators of terminal congestion while preserving strict information availability.
4. **Zero-Bounded Distributional Assumptions**: Checkpoint throughput data exhibits positive skewness and structural zeros during overnight curfews. Standard ordinary least squares (OLS) regression produces negative predictions during night hours. Models must incorporate zero-bounded formulations, such as Tweedie compound Poisson generalized linear models ($p = 1.3$) or two-stage hurdle structures.

## Model Development and Execution

### Feature Engineering
A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)*

## Table 4.9: Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)

Unshifted scheduled flights in the same departure hour explain less than 12% of checkpoint throughput variance. Explanatory power peaks across the Lead $t+1$ and Lead $t+2$ horizons ($R^2 \approx 24\%$), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010).

Based on these findings, an empirical passenger show-up distribution was constructed by convolving scheduled departing seats across lead horizons ($t+1, t+2, t+3$):
$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$$
where weights $w_1 = 0.35$, $w_2 = 0.50$, and $w_3 = 0.15$ match empirical ACRP Report 40 arrival distributions.

The complete feature engineering pipeline encompasses five functional operational domains:
1. **Convolved Flight Schedule Volatility Features**: Lead-lag convolved seats, carrier-exclusive scheduled bank dispersion (`sched_hourly_std`, `sched_hourly_cv`), and rolling schedule volatility (`sched_rolling_7d_std`, `sched_rolling_7d_cv`).
2. **Airside Delay and Congestion Features**: Lagged mean departure delay ($t-1$), departure delay dispersion ($\sigma_{\text{Delay}, t-1}$), long-term delay volatility (`otp_departure_delay_volatility_cv`), tactical cancellation counts, and taxi-out queue duration.
3. **Temporal Cyclical Encodings**: Sine and cosine harmonic transformations of hour-of-day ($24\text{ hr}$) and day-of-week ($7\text{ days}$), capturing diurnal and weekly rhythms without arbitrary step discontinuities.
4. **Operational Regime Indicators**: Categorical encodings of the 84-cell interaction grid ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$).
5. **Facility and Aircraft Features**: Screening lane count, checkpoint configuration type (finger pier vs. linear), aircraft seating gauge (`aircraft_gauge_seats`), route load factors, and connecting passenger ratios.

### Model Training
To evaluate the research hypotheses, the canonical evaluation suite—representing each distinct modeling paradigm along with the persistence baseline—was calibrated and benchmarked against the 2025 out-of-time holdout partition:
### The Candidate Predictive Models and Baseline Control

Following the four-tiered purposive filtering pipeline (which established the balanced 9-airport experimental cohort across 12 carrier-exclusive terminal screening complexes), the research benchmarks **three candidate predictive models representing distinct operational paradigms**, evaluated against an empirical persistence control:

* **Baseline Control Benchmark (Daily Persistence)**:
  * *Operational Approach*: Assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion exactly ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$). This non-parametric reference standard establishes the scaling baseline ($\text{MASE} \equiv 1.000$).
* **Model 1: Deterministic Flight Schedule Model (Operational Baseline)**:
  * *Operational Approach*: Derives expected passenger arrival dispersion directly from published airline flight departure banks convolved across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$). It captures macro schedule geometry without requiring statistical machine learning or airside delay telemetry.
* **Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**:
  * *Operational Approach*: An automated decision-tree model trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features (incorporating tactical flight cancellations, prior-hour delay dispersion, and surface taxi queues).
* **Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**:
  * *Operational Approach*: Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward.

#### Training Window and Partitioning Design.
Models were trained and validated across the 32-month Candidate B development partition:
* **Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days across the 9-airport filtered complex cohort).
* **Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days), used for model calibration.
* **Operational Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades from December 2023 do not leak into the January 2024 validation partition.

### Model Testing
All models were evaluated against the untouched **2025 Full-Year Out-of-Time Holdout Dataset**:
* **Evaluation Period**: January 1, 2025 to December 31, 2025 (12 continuous months; 3,222 test airport-days; 72,053 complex-level screening hours).
* **Primary Target**: Intraday Diurnal Throughput Volatility ($\sigma_{\text{TSA, hr}}$, measured in passengers per hour dispersion across the 24 hours of day $d$) and Scale-Free Relative Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$).
* **Evaluation Metrics**: Models were benchmarked across standard operational metrics: Coefficient of Determination ($R^2$), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias.

### Implications for How to Interpret Final Results
When interpreting model evaluation metrics, several operational realities must be considered:
1. **Dispersion Scale vs. Volume Scale**: Unlike mean hourly throughput volume (which averages ~1,750 pax/hr across dedicated complexes), diurnal throughput standard deviation ($\sigma_{\text{TSA, hr}}$) averages 540 to 880 passengers per hour across hub complexes. An RMSE of ~220 pax/hr represents an exceptionally close fit to intraday arrival swings.
2. **MASE as the Primary Standard for Volatility Forecasting**: MASE normalizes errors against daily persistence ($\text{Vol}_{t-24}$). A MASE below 0.85 indicates substantial predictive skill beyond historical patterns, while a MASE below 0.70 represents outstanding accuracy.
3. **Conformal Staffing Buffers**: Airport security planners can translate predicted throughput volatility directly into risk-buffered lane allocations ($c(t) = \lceil (\hat{\mu}_t + z_q \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$) to prevent queue overflow during peak departure banks.

## Model Evaluation and Results

### Results from Running Models
Table 4.10 reports the out-of-time evaluation benchmark matrix across the candidate model architectures on the 2025 holdout dataset (3,222 test airport-days; 72,053 hourly complex observations).

Table 4.10  
*Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)*

## Table 4.10: Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)

### General Model Performance Across the 9-Airport Cohort
The empirical results reveal clear performance separations across the modeling paradigms:
1. **The Deterministic Schedule Baseline (Model 1)**:
   By shifting scheduled flight departures across empirical ACRP Report 40 passenger arrival curves, Model 1 achieves $\text{Test } R^2 = 0.4980$ ($\text{RMSE} = 313.4\text{ pax/hr}, \text{MASE} = 0.945$). It outperforms simple persistence by 5.5% without requiring real-time flight tracking or machine learning infrastructure.
2. **Supervised Feature Coupling (Model 2)**:
   Incorporating 24 BTS OTP feature attributes (departure delay dispersion, tactical cancellations, and taxi queues) elevates explained variance to **$R^2 = 0.6178$** ($\text{RMSE} = 273.5\text{ pax/hr}, \text{MASE} = 0.779$). Statistical loss differential tests confirm that Model 2's error reductions over deterministic scheduling are statistically decisive ($DM = 42.15, p < 0.0001$).
3. **The Dynamic Two-Stage Hybrid (Model 3)**:
   By coupling a daily flight schedule foundation with live real-time error feedback, Model 3 explains **74.83% of total passenger throughput volatility variance** on unobserved holdout data ($\text{Test } R^2 = 0.7483$), achieving an RMSE of **222.1 pax/hr** and a holdout MASE of **0.662**.

### Model Performance in the Context of the Thesis (Asymmetric Hypothesis Testing)
The primary thesis hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. 

Critically, **the hybrid model (Model 3) is NOT the winner across all performance measures**. To determine model efficacy, the candidate architectures were evaluated against explicit performance targets across the three operational dimensions:
* **Robustness Target**: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.70$ under nominal flight conditions.
* **Resilience Target**: Recovery RMSE Multiplier $R_{\text{RMSE}} \approx 1.00$ and lowest $\text{MASE}_{\text{shock}}$ under acute disruptions.
* **Generalizability Target**: Relative Transfer Ratio $\text{RTR} = 1.00$ and Change in MASE on transfer $\Delta \text{MASE} \le 10.0\%$.

Table 4.11 presents the formal multi-pillar hypothesis evaluation matrix.

Table 4.11  
*Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)*

## Table 4.11: Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)

#### Empirical Confirmation of Asymmetric Trade-Offs (Hypothesis 1 Verified).
1. **Dimension 1: Robustness (Nominal & Routine Conditions)**:
   Both the Supervised Machine Learning model (Model 2) and Dynamic Hybrid (Model 3) achieve the academic target of $\text{MASE} < 0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and zero feedback latency, making it the preferred operational choice for everyday routine staffing.
2. **Dimension 2: Resilience (Severe Disruption / IROPS)**:
   The Dynamic Hybrid Framework (Model 3) is the **decisive champion of Resilience**. While pure machine learning (Model 2) suffers from the "Empty Checkpoint Fallacy" during delayed flight holds ($R_{\text{MASE}} = 2.14$), Model 3's recursive error feedback ($e_{t-1}$) maintains a resilient multiplier of $R_{\text{MASE}} = 1.05 \approx 1.00$ and achieves the fastest Time-to-Recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dimension 3: Generalizability (Zero-Shot Portability)**:
   The Deterministic Flight Schedule Model (Model 1) is the **decisive champion of Generalizability**. It successfully meets both stated targets: $\text{RTR} = 1.04 \approx 1.00$ and $\Delta\text{MASE} = +4.0\% \le 10.0\%$. Conversely, **the Hybrid model (Model 3) decisively fails the Generalizability targets** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$) because its decision-tree component overfits to Newark's specific terminal geometry and carrier bank timings. This empirical failure disproves universal hybrid dominance and decisively confirms Hypothesis 1.

## The Values versus Volatility Paradigm Empirical Results

The central empirical comparison of this thesis evaluates whether predicting TSA throughput volatility requires tracking the **values (levels) of OTP attributes**, the **volatility of OTP attributes**, or a **combined dual model**. Evaluating across the 2025 out-of-time holdout ($N = 3,222$ test days) across the three volatility targets reveals:

1. **Intraday Diurnal Absolute Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion)**:
   * *Values Only*: Achieves $R^2 = 0.6229$ ($\text{RMSE} = 271.6$). Because raw variance naturally scales with airport passenger volume, flight volume counts anchor the base magnitude of the facility.
   * *Volatility Only*: Achieves $R^2 = 0.4980$ ($\text{RMSE} = 313.4$).
   * *Combined Representation*: Achieves $R^2 = 0.6178$ in non-linear decision trees ($\text{RMSE} = 273.5, \text{MAE} = 178.0$).
2. **Intraday Scale-Free Relative Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$, ratio)**:
   * Under this scale-free regime, Values Only drops to $R^2 = 0.1823$.
   * Volatility Only captures $R^2 = 0.1853$ in decision trees.
   * **The Combined Dual Model outperforms all architectures ($R^2 = 0.2208$, $\text{RMSE} = 0.1853$, $\text{MAE} = 0.1010$)**, proving that scale-free arrival burstiness reflects an interaction between carrier schedule volume and operational disruption.
3. **Multi-Day Temporal Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)**:
   * **Feature Values Completely Collapse**: Yielding negative test scores ($R^2 = -0.2688$ in linear regression; $R^2 = -0.0506$ in decision trees). Because static flight counts remain relatively constant across seasons, static volume levels are blind to temporal turbulence.
   * **Feature Volatility Succeeds**: In sharp contrast, Feature Volatility metrics achieve **$R^2 = +0.2313$ (linear) and $R^2 = +0.3105$ (decision trees)**, improving to **$R^2 = +0.3166$** in the Combined Model, with RMSE dropping from 4,090.7 to 3,002.3 pax/day. This confirms Hypothesis $H_2$.

### Master Factor Weighting Hierarchy of OTP Attributes
Synthesizing variable importance across models establishes the consensus predictive weights of all 24 OTP attributes:
* **Schedule Scale & Density (64.47% Consensus Share)**: Governed by `sched_rolling_7d_mean` (23.73%), `actual_daily_total` (11.64%), and `sched_hourly_mean` (6.91%).
* **Tactical Cancellations (16.48% Share)**: Driven by cancellation rate volatility (`otp_cancellation_volatility_cv`: 8.79%).
* **Network Buffers & Capacity (7.85% Share)**: Aircraft seating capacity (`aircraft_gauge_seats`: 4.26%) smooths day-to-day volatility.
* **Flight Delays & Punctuality (7.00% Share)**: **Flight Departure Delay Volatility ($\text{CV}_{\text{delay}}$)** contributes 4.32% weight, acting as a potent transmission vector into checkpoint surges ($r = +0.4373, p = 0.0288$).
* **Surface Taxi Queues (4.21% Share)**: Runway taxi-out queues (`avg_taxi_out_minutes`: 4.21%) indicate departure bank congestion.

### Implications of Model Performance for Predictive Forecasting in Aviation
1. **Deploying Dual-Paradigm Volatility Models for Staffing**: Rather than allocating security lanes based on static flight departure counts, TSA planners must incorporate **feature volatility metrics** (rolling 7-day schedule variance and cancellation volatility) to forecast queue dispersion.
2. **Operational Deployment via a Dual-Track Decision Engine**:
   * *Nominal Tracking Track*: During clear weather ($T(h) < 0.75$), operational planning should rely on the **Supervised Machine Learning Model (Model 2)**, delivering high accuracy ($\text{MASE} = 0.779$) and superior spatial portability ($RTR = 1.08$).
   * *Tactical Shock Track*: When severe storms or ground stops occur ($T(h) \ge 0.75$), the system should engage the **Dynamic Two-Stage Hybrid (Model 3)**, utilizing live error feedback to achieve rapid recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dynamic Lane Buffers via Conformal Prediction**: By pairing predicted volatility with conformal quantile bounds ($\hat{y}_{0.85}$), security directors can establish dynamic lane buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$) that absorb queue surges without chronic overstaffing.

---

# Chapter V

# Discussion

## Spatial Architecture and Passenger Behavioral Dynamics
The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:

1. **Connecting Passenger Shielding (The Hub Disconnect)**: At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by $(1 - \text{ConnectingRatio})$ derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.
2. **Terminal Complex Aggregation**: Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.
3. **Behavioral Invariance Across Terminal Layouts**: The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA Credential Authentication Technology (CAT) scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.
4. **Heavy-Traffic Queuing Dynamics (The Second-Order Driver)**: Traditional models focus exclusively on mean passenger volume $\lambda$. However, from Kingman's heavy-traffic approximation and the Allen-Cunneen formula:
   $$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \frac{1}{\mu}$$
   where $\rho = \lambda / (c \mu)$ represents traffic intensity, $C_a = \sigma_a / \mu_a$ is the coefficient of variation of passenger arrivals, and $C_s$ is the coefficient of variation of screening service time. As traffic intensity approaches saturation ($\rho \to 1.0$) during morning and evening departure banks, queue delay $W_q$ scales non-linearly with the square of arrival volatility ($C_a^2$). Consequently, predicting the volatility of TSA throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is fundamentally more consequential for checkpoint stability than forecasting average volume alone.

## Initial Training and Passenger Show-Up Dynamics
The striking performance gap between unshifted flight schedules ($R^2 = -0.0586$ on out-of-time volatility) and lead-lag passenger show-up schedules ($R^2 = 0.5344$ to $0.6178$) resolves the operational lead-lag time offset inherent in air travel (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010):
* Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior (standard ACRP Report 40 passenger show-up distribution; Transportation Research Board, 2010).
* Incorporating lead horizons ($t+1, t+2, t+3$) enables the model to anticipate incoming passenger surges well before gate departure times.
* Furthermore, flight delays must be handled asymmetrically: including same-hour actual flight delays introduces severe lookahead bias (since departure delays are not known until after aircraft push back), whereas incorporating prior-hour delays ($t-1$) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict operational information availability.

### The Lead-Lag Asynchrony Mechanism
Traditional queuing models in airport terminal planning often assume that passenger arrival intensity $\lambda(t)$ is directly proportional to departing flights in the same time window $t$. The empirical results completely dismantle this unshifted schedule assumption. Across the Top 25 network, the operational cycle is governed by an asynchronous dual-peak structure:

* **Morning Peak (05:00–08:00)**:
  * *Checkpoint Volume*: Peak passenger screening throughput.
  * *Screening Volatility*: Extreme surge volatility ($\sigma_{\text{TSA}} > 11,380$ pax/hr network-wide; complex-level $\sigma_{\text{TSA, hr}} \sim 540\text{--}880$ pax/hr).
  * *Flight Departure Delays*: Low average departure delays (<5 minutes).
  * *Schedule Buffer*: Fresh, unexhausted aircraft turnaround buffers.
* **Evening Peak (14:00–22:00)**:
  * *Checkpoint Volume*: Moderate and tapering screening volumes.
  * *Screening Volatility*: Low to steady arrival volatility.
  * *Flight Departure Delays*: Peak network-wide departure delay dispersion ($\sigma_{\text{Delay}} > 63$ minutes).
  * *Schedule Buffer*: Turnaround buffers fully eroded across the National Airspace System.

* **Pre-Departure Passenger Surge Window (Morning)**: Passengers arrive at screening checkpoints 90 to 120 minutes prior to scheduled departure (conforming to ACRP Report 40 distributions; Transportation Research Board, 2010). Checkpoint arrival volatility peaks early in the day when early-morning outbound banks depart with high schedule reliability.
* **Operational Lag Phase (Evening)**: As the day progresses, delay propagation across the National Airspace System (NAS) compounds. Aircraft turnaround buffers are exhausted by late afternoon, causing departure delay dispersion ($\sigma_{\text{Delay}}$) to peak between 14:00 and 22:00.
* **Synthesis**: Passenger screening throughput temporally **precedes** terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turn times and network delays compound. Aligning flight departures and passenger throughput in the same hour without lead-lag structure introduces severe misspecification error ($R^2 < 0.20$ on volume, and negative $R^2 = -0.0586$ on volatility). Importantly, landside security queues do not cause flight departure delays—airlines enforce strict gate closure rules and depart without missing passengers—rather, systemic airside delays and ground holds cascade backward into the terminal, stranding ticketed passengers landside and creating passenger dwell that unshifted models fail to predict.

## Evaluation Dimension 1: Robustness (Nominal & Routine Daily Operations)

Table 5.1  
*Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models*

## Table 5.1: Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models

### Empirical Evaluation of Robustness
The primary research hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. Under this first dimension—standard daily operations—the methodology established two explicit performance targets:
1. **Lowest $\text{RMSE}_{\text{routine}}$** to minimize absolute forecast error during standard flight waves.
2. **$\text{MASE}_{\text{routine}} < 0.700$**, demonstrating substantial error reduction relative to simple daily persistence.

* The findings confirm that both the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) successfully meet the target threshold, achieving $\text{MASE}_{\text{routine}} \le 0.700$ and $0.662$ respectively, compared to the daily persistence baseline ($\text{MASE} = 1.000$) and deterministic flight scheduling (Model 1, $\text{MASE} = 0.945$).
* In terms of absolute dispersion error, Model 3 achieves the lowest routine RMSE (**222.1 pax/hr**), capturing 74.83% of holdout volatility variance ($R^2 = 0.7483$) by combining daily flight schedules with decision-tree corrections.
* Standard statistical loss differential tests confirm that error reductions are statistically decisive ($DM = 42.15$ and $DM = 48.72, p < 0.0001$) across all nine cohort airfields.
* Crucially, from an airport management perspective, **Model 2 delivers the optimal practical choice for routine everyday operations**: it meets the stringent $\text{MASE} < 0.70$ target without requiring live real-time feedback or continuous data connections to security lane sensors, making it the preferred choice for routine day-to-day checkpoint staffing.

### The Values versus Volatility Paradigm in Routine Operations
Evaluating the Values versus Volatility Paradigm under routine operations provides foundational insights into how checkpoint volatility originates:
1. **Absolute Intraday Dispersion ($\sigma_{\text{TSA, hr}}$)**:
   Predicting daily throughput standard deviation benefits from both feature types: Feature Values achieve $R^2 = 0.6229$ ($\text{RMSE} = 271.6$), while Feature Volatility achieves $R^2 = 0.4980$ ($\text{RMSE} = 313.4$). Because raw passenger spread naturally scales with total airport volume, flight volume counts anchor the base size of the facility. Combining values and volatility in Model 2 yields $R^2 = 0.6178$ ($\text{RMSE} = 273.5, \text{MAE} = 178.0$).
2. **Scale-Free Arrival Burstiness ($CV_{\text{TSA, hr}} = \sigma / \mu$)**:
   When normalizing for facility size, Feature Values alone drop to $R^2 = 0.1823$. Feature Volatility models capture $R^2 = 0.1853$. Crucially, the **Combined Dual Model achieves the highest performance ($R^2 = 0.2208$, $\text{RMSE} = 0.1853$)**, proving that relative arrival burstiness reflects the interplay between scheduled bank volume and operational disruption.

### Robustness Across the Interaction Grid and Prevention of Delay Distortion
The coupled volatility analysis substantiates why routine accuracy holds consistently across the commercial airport network:
1. **Preventing Extreme Storm Outliers from Distorting Normal-Day Decision Rules**:
   When a predictive model is trained across all weather regimes simultaneously without separation, the model's rules become distorted by rare, extreme summer storm delays ($\sigma_{\text{Delay}} = 68.43\text{ min}$). Under pooled training, decision trees warp their rules to accommodate these rare storm spikes, degrading accuracy during clear, on-time operations. By conditioning training on distinct operational regimes, decision trees focus on direct operational drivers (route load factors, aircraft seat gauge, and empirical passenger show-up curves) rather than convective storm noise.
2. **Empirical Verification of Sample Depth**:
   The sample size audit confirms that **83 of 84 operational cells (98.8%)** meet the minimum sample threshold ($N_{\text{train}} \ge 50$), with a median training depth of **215 observations per cell**, refuting any concern that temporal stratification creates sparse, over-specialized rules.

## Evaluation Dimension 2: Resilience (Performance Under Severe Disruption)

Table 5.2  
*Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption*

## Table 5.2: Evaluation Dimension 2: Resilience and Shock Performance Under Severe Operational Disruption

### Empirical Evaluation of Resilience Under Disruption
Evaluating the second dimension of **Hypothesis 1**, the methodology posited that **dynamic hybrid models combining scheduled flight baselines with live operational error feedback would demonstrate superior resilience during acute disruptions**. Under severe disruption regimes (hours with departure delays $\ge 45$ min or tactical cancellations $\ge 5$), the performance targets were strictly defined:
1. **Disruption Error Multiplier ($R_{\text{MASE}} \approx 1.00$)**, demonstrating that error does not inflate relative to routine performance.
2. **Lowest $\text{MASE}_{\text{shock}}$**, maintaining maximum operational accuracy during irregular operations.
3. **Time-to-Recovery ($\text{TTR} < 4.0\text{ hours}$)**, returning to nominal error bounds quickly.

* The empirical findings establish the Dynamic Two-Stage Hybrid Model (Model 3) as the **decisive, undisputed winner of Resilience**:
  * Model 3 achieves $\text{RMSE}_{\text{shock}} = 254.2\text{ pax/hr}$ and $\text{MASE}_{\text{shock}} = 0.694$ (the lowest across all models), outperforming daily persistence by 30.6% and deterministic scheduling by 35.9%.
  * Model 3 successfully hits the Disruption Multiplier target with $R_{\text{MASE}} = 1.05 \approx 1.00$, proving that its prediction fidelity remains stable during severe ground stops.
  * Time-to-Recovery analysis indicates a rapid recovery of **2.8 hours**, easily beating the $< 4.0\text{ hour}$ benchmark, and recovering 5.0 hours faster than deterministic schedules ($7.8\text{h}$) and 2.6 hours faster than pure machine learning ($5.4\text{h}$).
* In stark contrast, pure supervised machine learning (Model 2) suffers an acute fragility collapse ($R = 2.14 > 2.0$), and deterministic schedules (Model 1) degrade significantly ($R = 1.32, \text{MASE} = 1.082$) due to complete blindness to real-time ground hold dynamics.

### Resilience Mechanics and the Empty Checkpoint Fallacy
The coupled volatility findings explain the exact operational bottleneck mechanism during severe convective disruptions:
1. **The "Empty Checkpoint Fallacy" in Pure Machine Learning**:
   During summer severe weather events, flight departure delays surge and cancellations spike. A pure machine learning model relying on flight schedules shifted by static show-up curves assumes that because flights scheduled for 18:00 have been delayed to 22:00 or ground-stopped, security checkpoints will experience an immediate demand collapse at 16:00. In reality, passengers arrived at the airport based on their original ticketed itineraries. Thousands of stranded travelers crowd security lines, re-screen after gate changes, or remain landside. Pure machine learning predicts an empty checkpoint, resulting in massive under-prediction errors ($R = 2.14$).
2. **Live Error Correction in the Dynamic Hybrid (Model 3)**:
   The Dynamic Hybrid actively senses real-time checkpoint conditions using 1-step recursive error feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). In practical terms, this functions like an automated safety valve: when live passenger throughput at the checkpoint exceeds what delayed flight schedules predicted, the error correction immediately alerts the model that passengers are accumulating in the terminal. The model adjusts its demand forecast upward, preventing the empty checkpoint fallacy and maintaining low disruption error multipliers ($R_{\text{MASE}} = 1.05$).

## Evaluation Dimension 3: Generalizability (Cross-Airport Transferability)

Table 5.3  
*Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance*

## Table 5.3: Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance

### Empirical Evaluation of Generalizability Across Facilities
Evaluating the third dimension of **Hypothesis 1**, the methodology posited that **first-principles deterministic models would generalize significantly better across distinct terminal layouts than complex, over-parameterized models**. To rigorously test zero-shot transferability without local retraining, models trained on United at Newark Liberty (EWR Terminal C) were directly deployed to Delta at New York LaGuardia (LGA Terminal C), holding macro New York regional airspace congestion constant while testing spatial transfer across different carrier bank structures and facility geometries.

The performance targets for Generalizability were strictly specified:
1. **Relative Transfer Ratio ($\text{RTR} = \text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}} = 1.00$)**.
2. **Change in MASE on Transfer ($\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$)**, ensuring minimal performance penalty.

* **The Deterministic Flight Schedule Model (Model 1) is the DECISIVE WINNER of Generalizability**:
  * Model 1 achieves an $\text{RTR}$ of **1.04** ($\approx 1.00$, target met) and a $\Delta\text{MASE}$ of only **+4.0%** (+0.038, well below the 10.0% ceiling), suffering a mere +4.2% RMSE transfer degradation.
  * Because Model 1 relies on universal flight schedule convolution and empirical passenger show-up curves, its structural logic is completely invariant to facility-specific quirks. In cross-cluster transfer (DTW $\to$ PHL), Model 1 achieves an $\text{RTR}$ of **1.003**, verifying complete spatial generalizability.
* **The Dynamic Hybrid (Model 3) DECISIVELY FAILS the Generalizability Targets**:
  * Model 3 experiences a severe **+19.0% transfer degradation**, with an $\text{RTR}$ of **1.19** (failing the target of 1.00) and a $\Delta\text{MASE}$ surge of **+21.5%** (+0.142, failing the $\le 10.0\%$ threshold).
  * This empirical failure confirms the central thesis of asymmetric trade-offs: the decision-tree component of Model 3 overfits to Newark's specific terminal geometry, flight bank timings, and local gate configurations. When transferred to LaGuardia without local recalibration, those specialized decision boundaries fail, imposing a heavy transfer penalty.
* **Supervised Machine Learning (Model 2)** exhibits robust intermediate portability ($\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\% \le 10\%$), passing the transfer targets due to standardized OTP feature scaling.

## Master Synthesis and Operational Recommendations

Table 5.4  
*Master Asymmetric Trade-Off Matrix Across the Candidate Models*

## Table 5.4: Master Asymmetric Trade-Off Matrix Across the Candidate Models

### Deep-Dive: Values versus Volatility Paradigm Across Temporal Horizons
A core theoretical contribution of this thesis is the empirical demonstration of the **Values versus Volatility Paradigm**:
1. **Multi-Day Rolling Volatility ($\sigma_{\text{TSA, 7d}}$, pax/day)**:
   * **Feature Values Completely Collapse**: Standard feature values (raw scheduled flights, average delay minutes) generate negative out-of-time test scores ($R^2 = -0.2688$ in linear regression; $R^2 = -0.0506$ in decision trees). Because scheduled flight counts remain relatively stable across consecutive weeks, static volume features cannot detect shifts in temporal turbulence.
   * **Feature Volatility Succeeds**: In contrast, Feature Volatility attributes (rolling 7-day schedule variance, cancellation volatility, and delay dispersion) achieve **$R^2 = +0.2313$ (linear) and $R^2 = +0.3105$ (decision trees)**, improving to **$R^2 = +0.3166$** in the Combined Model, while slashing RMSE from 4,090.7 to 3,002.3 pax/day.
2. **Delay Volatility Transmission**:
   Cross-dataset econometric correlation demonstrates that **Flight Departure Delay Volatility ($CV_{\text{delay}}$)** is significantly coupled with checkpoint arrival volatility ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$). Conversely, raw flight departure delay minutes show zero linear correlation ($r = -0.0620, p = 0.769$). Delays only disrupt checkpoint operations when they are erratic and disperse passenger arrival timing across banks.
3. **Master Consensus Factor Weights**:
   Synthesizing variable importance across models confirms that schedule dispersion (`sched_rolling_7d_mean`, 23.73%; `sched_hourly_mean`, 6.91%) and operational volatility (`otp_cancellation_volatility_cv`, 8.79%; `CV_{\text{delay}}`, 4.32%) dominate predictive power, accounting for over 80% of consensus importance.

### The Regime-Switched Gated Inference Engine: The Airport Operator's Playbook
To operationalize these empirical findings, the Transportation Security Administration (TSA) and Airport Operations Centers (AOC) should deploy a **Regime-Switched Gated Inference Engine**—an automated decision playbook that monitors airport turbulence and automatically selects the most suitable forecasting model:

* **Gate 1: Routine Flow Track ($\text{Turbulence Shock Index } T(h) < 0.75$)**
  * *Operating Regimes*: Calm seasonal periods, midweek baseline days (Tuesday and Wednesday), and steady midday hours.
  * *Assigned Architecture*: **The Supervised Machine Learning Model (Model 2)**.
  * *Operational Justification*: Fast, automated execution delivering superior point accuracy ($\text{MASE} = 0.779$) with near-zero computing overhead and high portability across diverse terminal layouts ($RTR = 1.08$). Running a complex live-updating model 24/7 during calm periods imposes unnecessary IT costs and latency; Model 2 provides the optimal balance of speed and precision.
* **Gate 2: Tactical Shock Track ($\text{Turbulence Shock Index } T(h) \ge 0.75$)**
  * *Operating Regimes*: Summer severe thunderstorms, peak holiday travel corridors, concentrated Monday morning flight waves, Sunday evening return cascades, and acute departure delay dispersion ($\sigma_{\text{Delay}} > 45$ min).
  * *Assigned Architecture*: **The Dynamic Two-Stage Hybrid (Model 3)**.
  * *Operational Justification*: Activates live checkpoint queue feedback ($e_{t-1}$), maintaining tight error bounds ($R_{\text{MASE}} = 1.05$) and rapid recovery ($\text{TTR} = 2.8$ hours) during acute flight delay cascades to prevent checkpoint staffing shortfalls.

### Connecting Queuing Principles to Dynamic Lane Staffing: The Staffing Safety Cushion
A primary contribution of this thesis is bridging theoretical queuing theory with practical checkpoint lane allocation:

1. **The Checkpoint Tipping Point (Kingman's Queuing Law)**:
   In heavy-traffic queuing theory (Kingman, 1961), expected passenger waiting time ($W_q$) does not increase in a smooth, straight line. Rather, it follows a non-linear curve:
   $$W_q \approx \left( \frac{\rho}{1-\rho} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
   where $\rho = \frac{\lambda}{c \mu}$ is checkpoint lane utilization and $C_a^2$ is passenger arrival volatility. When screening lanes operate near capacity ($\rho \ge 0.85\text{--}0.90$), the multiplier $\frac{\rho}{1-\rho}$ grows exponentially. Even a modest burst of arriving passengers ($C_a^2$) instantly tips the checkpoint into a runaway queue backlog.

2. **The Dynamic Staffing Safety Cushion**:
   Under traditional deterministic staffing, security lanes are opened based solely on expected average volume ($\hat{\mu}_t$). During flight departure waves, this guarantees that arrival surges push utilization past $\rho = 0.90$, triggering queue spikes. 
   
   To solve this, airport checkpoint administrators can translate predicted throughput volatility ($\hat{\sigma}_{\text{TSA}, t}$) directly into risk-buffered lane configurations using conformal prediction principles:
   $$c(t) = \left\lceil \frac{\hat{\mu}_t + z_q \cdot \hat{\sigma}_{\text{TSA}, t}}{\mu_{\text{lane}}} \right\rceil$$
   where $\mu_{\text{lane}}$ is nominal screening lane capacity (~180 to 220 pax/lane/hr) and $z_q$ is the coverage quantile factor ($z_{0.85} = 1.036$ for an 85% service guarantee). By adding a dynamic volatility buffer ($z_q \cdot \hat{\sigma}_t$) to lane scheduling, checkpoint administrators cap utilization at a safe threshold ($\rho(t) \le 0.85$), effectively clamping the $\frac{\rho}{1-\rho}$ multiplier and preventing exponential wait-time explosions.

### Strategic Implications for Airport and Security Authorities
1. **Dynamic Checkpoint Allocation**: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.
2. **Connecting Ratio Integration**: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.
3. **Deployment of Two-Stage Hybrid Estimators**: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ($t-1$) during severe convective ground stop disruptions.
