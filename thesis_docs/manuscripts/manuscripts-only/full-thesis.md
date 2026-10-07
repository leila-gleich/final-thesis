# Chapter I

## Introduction

As air travel demand outpaces airport infrastructure growth, inefficient resource allocation has become a critical operational bottleneck (Adacher, Flamini, Guaita & Romano, 2017). While existing predictive models are increasingly used to forecast airport passenger flow management, the systemic shocks of the COVID-19 pandemic underscored limitations within traditional, accuracy-centric performance metrics to handle abrupt demand shocks, structural breaks, and changing operating constraints. These unprecedented operational disruptions demonstrated that conventional accuracy metrics, while necessary, are insufficient as the sole basis for evaluating models intended for volatile airport operating environments. Specifically, the pandemic revealed that a singular evaluation standard is inadequate across highly variable operational contexts, necessitating the assessment of predictive models through a broader, multidimensional set of performance measures. In airport operations, the most useful predictive model is therefore not necessarily the one with the lowest average forecast error but the model that:

- **Remains reliable during routine operations (Robustness)**: Providing consistent, low-error baseline volatility forecasts during undisturbed flight banks.

- **Maintains stability and recovers rapidly during disruptions (Resilience)**: Absorbing severe exogenous shocks (such as winter freeze events or summer convective ground delay programs) without generating false demand collapses or runaway queue backlogs.

- **Transfers effectively across operational contexts (Generalizability)**: Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study systematically examines the suitability of predictive modeling frameworks – spanning deterministic operational baselines (such as persistence and scheduled flight bank dispersion), data-driven decision-tree architectures (automated rule-based machine learning models), and sequential two-stage hybrid models (combining schedule baselines with real-time error correction) – for forecasting Transportation Security Administration (TSA) checkpoint throughput volatility across routine, volatile, and disrupted demand regimes.

## Significance of the Study

This research aims to contribute to both theory and practice by shifting the paradigm of how predictive models are evaluated in unpredictable airport operations. While traditional approaches emphasize static accuracy, this study advances the field by establishing a multidimensional, dynamic evaluation framework that assesses models based on their robustness, resilience, and generalizability. By identifying which forecasting techniques remain reliable during operational disruptions and structural breaks, it offers airport operators actionable, data-driven insights for selecting models that sustain TSA throughput, safety, and service rates under fluctuating post-pandemic conditions.

## Statement of the Problem

Airport passenger arrivals and behaviors are inherently stochastic, varying significantly by time of day, flight schedules, and external factors (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Existing models for managing airport passenger flow tend to rely on static or pre‑pandemic assumptions, consequentially failing to account for unpredictable post‑pandemic travel patterns (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Lee & Yu, 2024). This mismatch between capacity planning and fluctuating passenger demand contributes to bottlenecks at check‑in counters, TSA checkpoints, and boarding gates, ultimately leading to congestion and inefficient resource allocation. While recent global disruptions have proven that historical baselines are insufficient for contemporary airport logistics, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond standard accuracy metrics. Because modern forecasting can no longer remain predicated on deterministic conditions, the absence of an adaptable evaluation methodology leaves airports at risk of deploying tools that fail to respond to sudden demand shocks or generalize across shifting operational realities.

## Purpose Statement

The primary objective is to evaluate predictive modeling techniques, such as regression, machine learning, and queuing simulation, to optimize airport capacity via technological rather than physical – and more costly – intervention. By analyzing the relationship between flight operations and TSA throughput, this study evaluates various predictive modeling frameworks against the primary criteria of robustness, resilience, and generalizability. Rather than seeking a singular, universally optimal model, this research identifies which frameworks perform best under each distinct metric. Ultimately, this comparative analysis provides management with the strategic flexibility to adopt the most appropriate forecasting approach based on their specific operational priorities.

## Research Questions

Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule dispersion baselines, supervised machine learning tree ensembles, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility ($\sigma _{TSA}$ and $CV_{TSA}$) when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts) as the primary operational evaluation metric?

**Master Asymmetric Trade-Off Hypothesis **$H_{1}$ : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability).

## Delimitations

This study focuses on U.S. airports and uses post-pandemic TSA throughput and flight performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where needed to define the post-pandemic baseline. Dynamic queuing models and simulationbased methods are assessed using standard statistical measures, including pvalue, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE). These delimitations are detailed in the appendix.

- **Geographic Scope**: This study evaluates commercial air traffic and security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications, capturing 67.2% of nationwide domestic flight departures.

- **Temporal Scope**: The longitudinal dataset spans January 1, 2019 through December 31, 2025 ($N=22,491$ airport-days; 42.06 million conformed fact records). Model training and evaluation are focused on the verified post-pandemic operational regime starting May 1, 2022 (following the nationwide rescission of federal transportation mask mandates), reserving the full 12-month calendar year of 2025 (3,222 airport-days) as a strict out-of-time holdout evaluation window.

- **Data Sources**: Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including TSA Freedom of Information Act (FOIA) hourly screening logs per physical lane, Bureau of Transportation Statistics (BTS) On-Time Flight Performance records (Form 234; capturing flight-level departure delays and cancellations), BTS Schedule T-100 Segment traffic (reporting monthly aircraft seating capacity and load factors), and BTS DB1B/DB1C 10% ticket coupon surveys (identifying local originating vs. airside connecting passenger proportions).

- **Evaluation Standards**: Model performance is measured using rigorous operational forecasting metrics: Root Mean Squared Error (RMSE; capturing overall forecast spread while penalizing peak-hour misses), Mean Absolute Scaled Error (MASE; scaling errors against a simple persistence baseline where values below 1.0 indicate superior skill), the Disruption Error Multiplier ($R_{MASE}$; measuring whether forecast errors grow or remain stable during severe storm disruptions), and the Relative Transfer Ratio (RTR; assessing the accuracy penalty when deploying a model to a new airport without retraining).

## Limitations and Assumptions

Due to reliance on public data, confidential variables like staffing and manual queue management fall outside the scope of this analysis. While external factors such as weather, regulatory impacts, or IT outages may not be fully accounted for, the framework assumes that utilized data is consistent and findings from the selected airports are generalizable across similar facilities and circumstances. Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level. These limitations are detailed in the appendix.

- **Staffing and Lane Configuration Opacity**: Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential operational variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue snake reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.

- **Connecting Passenger Surveys**: The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.

- **Operational Exogeneity**: Exogenous severe weather disruptions (convective storm lines, winter blizzards) are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234.


---

# Chapter II

## Review of the Relevant Literature

As the air transportation network navigates a period of expansion that threatens to outpace the physical limitations of existing infrastructure, the impractical expectation of immediate structural capacity expansion has pivoted operational priorities toward refining asset distribution. Traditional optimization methods often rely on static, deterministic approaches – which operate on the premise of predictable, non-random outcomes – but intrinsically fail to account for the stochastic nature of real-time terminal activity. To address these gaps, researchers are developing models designed to optimize resource allocation, such as staffing and throughput management, while maintaining efficient, high-quality service. Integrating advanced predictive frameworks offers the potential to build the robust, resilient, and generalizable tools necessary to manage variability and balance competing operational demands under uncertainty. Historically, literature on airport passenger flow modeling has prioritized statistical fit and throughput optimization. The unprecedented systemic shocks of the COVID-19 pandemic exposed the limitations of relying solely on historical data for predictive accuracy. Consequently, this review traces the evolution of flow prediction from static operational models to advanced deep learning architectures, ultimately highlighting a recent paradigm shift toward frameworks that prioritize systemic resilience and robustness in the face of extreme disruptions.

## Traditional Approaches and Operational Complexity

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays, boarding holds, and passenger misconnections across the National Airspace System (Adacher et al., 2017).

**Uncertainty, Batch Arrival Dynamics, and Flight Banks. **A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated "batches" induced by airline flight bank scheduling (Cheng et al., 2012; Peterson et al., 1995). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities. Consequently, landside screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

**Classical Queuing Theory: First Moment (Volume) vs. Second Moment (Volatility). **To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon Queuing Theory (Odoni, 1986; Wang, 2017)—the mathematical study of waiting lines and congestion. Early terminal capacity models utilized Poisson arrival distributions (such as $M/M/s$ or $M/G/s$ queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) relative to an airport's target Level of Service (LOS; industry benchmarks defining acceptable passenger waiting times and crowding thresholds) (Araujo & Repolho, 2015).

However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP; queuing equations where passenger arrival rates vary across hourly intervals to reflect daily peaks and valleys) (Brunetta et al., 1999), NHPP models still evaluate queuing solely through the lens of expected volume (the first-order moment: $\mu =E\left[Y\right]$).

In operational reality, heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993) demonstrate that expected queue wait times ($W_{q}$) and queue backlogs in general $G/G/s$ screening facilities scale not with mean volume, but linearly with the **squared coefficient of variation of arrival times (**$C_{a}^{2}$**) and service times (**$C_{s}^{2}$**)** via the Allen-Cunneen approximation:

$W_{q}\approx \left(\frac{\rho ^{\sqrt{2\left(s+1\right)}-1}}{s\left(1-\rho \right)}\right)\left(\frac{C_{a}^{2}+C_{s}^{2}}{2}\right)\frac{1}{\mu }$

where $\rho =\frac{\lambda }{s\mu }$ represents checkpoint utilization. As checkpoint utilization approaches capacity ($\rho \to 1.0$) during morning and evening departure peaks, any increase in arrival volatility ($C_{a}^{2}$) triggers exponential queue length expansion and terminal crowd surges. Modeling and forecasting **throughput volatility** ($\sigma _{TSA}$ and $CV_{TSA}$) is therefore the vital prerequisite for robust lane staffing and queue stability (Adeke, 2018; Guo et al., 2022).

## The "Values versus Volatility" Paradigm in Transportation Demand

In modern econometric and volatility forecasting literature (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005), a central research question is whether predicting the volatility of a stochastic process requires tracking the **values** (levels, volumes, and magnitudes) of explanatory variables, the **volatility** (dispersion, standard deviations, and coefficients of variation) of those variables, or a **dual combined representation**.

In commercial aviation operations, this duality manifests across two operational horizons:

**Intraday Diurnal Volatility**: The within-day standard deviation ($\sigma _{TSA, hr}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($Var\left(Y\right)\propto \mu ^{p}$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor. However, when normalized into scale-free relative burstiness ($CV_{TSA, hr}=\sigma /\mu$), volume levels lose explanatory power.

**Multi-Day Rolling Volatility**: Over multi-day horizons ($\sigma _{TSA, 7d}$), static flight volumes remain largely unchanged across seasonal schedules. Consequently, models relying exclusively on static feature values fail to anticipate medium-term passenger turbulence. Forecasting disruption-driven turbulence requires tracking the volatility of operational features—specifically rolling schedule variance ($\sigma _{sched}$), flight cancellation volatility ($CV_{cancel}$), and departure delay dispersion ($\sigma _{Delay}$) (Hopfe et al., 2024).

## Simulation Modeling and Real-Time Terminal Management

**Discrete Event Simulation and Operational Limits. **To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static spreadsheets, DES models track individual simulated passengers through a chronological sequence of discrete physical milestones: ticket scanning, divestiture (removing shoes, jackets, laptops, and liquids for X-ray inspection), body scanning, and item retrieval.

Despite high visual fidelity, DES models exhibit critical operational limitations when deployed for real-time airport management:

- **Calibration Sensitivity**: Small changes in baseline assumptions—such as secondary bag-search alarm rates or Transportation Security Officer (TSO; federal screening personnel) divestiture coaching times—produce disproportionately large shifts in modeled queue wait times (Brown & Madhavan, 2011).

- **Computational Latency**: Simulating hundreds of thousands of individual passenger agents during severe, unfolding flight disruptions requires immense computational time, rendering DES impractical for real-time tactical lane reallocation (Bießlich et al., 2014; Takakuwa & Oyama, 2004).

- **Passive Traveler Assumptions**: Standard simulation models treat passengers as passive entities following rigid rules, failing to reflect how travelers dynamically adjust arrival timing based on mobile flight delay notifications (Alodhaibi et al., 2017).

## Time-Series Analysis and Data-Driven Predictive Frameworks

**Statistical Time-Series Foundations. **To achieve faster, automated forecasts, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). These models predict future hours by capturing the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations. When augmented with exogenous variables (SARIMAX)—such as published airline scheduled seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed historical relationships that cannot accommodate sudden delay cascades.

**Non-Linear Machine Learning and Sequential Neural Networks. **To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including deep sequence models such as Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and tree ensembles like Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025).

While deep neural networks can approximate complex multi-source interactions (e.g., weather indices, search engine trends, flight departure status), they introduce significant operational challenges in airport settings:

- **The "Black-Box" Interpretability Hurdle**: Airport Federal Security Directors (FSDs) and TSA operations planners cannot verify why a deep neural network predicts a sudden passenger volume spike, making them reluctant to commit staffing based on opaque model outputs (Adadi & Berrada, 2018; Viaña et al., 2024).

- **Facility-Specific Over-Specialization**: Highly parameterized neural networks tend to memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic terminal layouts and gate configurations, causing their forecast accuracy to degrade sharply when transferred to unfamiliar airports (Wang et al., 2025).

## Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability

To resolve the tension between the transparency of traditional queuing models and the non-linear flexibility of modern machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025).

**Integrating Queuing Principles with Decision-Tree Algorithms. **Rather than deploying fully end-to-end black-box models, effective hybrid architectures combine:

- **First-Principles Operational Baselines**: Using established flight schedules, empirical passenger show-up curves (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010), and airline connecting passenger survey ratios (BTS DB1B) to establish a deterministic baseline volatility estimate.

- **Transparent Decision-Rule Adjustments**: Deploying interpretable machine learning—specifically Gradient-Boosted Decision Trees—to predict residual volatility shifts caused by real-time flight delays, gate holds, and severe weather cancellations (Ribeiro et al., 2025).

- Decision trees offer a critical operational advantage over deep neural networks: their branching structure functions like intuitive, transparent operational rules (e.g., *"If departure delay dispersion exceeds 45 minutes and cancellation rate exceeds 5%, adjust expected security volatility upward by +35%"*).

**Dynamic Feedback and Real-Time State Tracking. **During severe operational disruptions (such as summer convective thunderstorm ground stops), static schedules become obsolete. Recent research demonstrates that incorporating recursive error-correction feedback (such as Kalman filtering, which functions like an automated tracking system that compares predicted volatility to actual volatility at time $t-1$ and immediately updates the expected backlog) allows forecasting models to monitor live checkpoint throughput and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024).

**Multi-Dimensional Operational Evaluation. **While predictive modeling literature has historically focused on maximizing point accuracy under nominal operating conditions, the unprecedented disruptions of the COVID-19 pandemic and subsequent recovery demonstrated that single-metric evaluations are fundamentally inadequate (Li et al., 2023; Sun et al., 2022). In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

- **Robustness (Routine Operational Accuracy)**: The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations (Lin, 2022).

- **Resilience (Performance Under Severe Disruption)**: The capacity of a forecasting framework to maintain error bounded-ness, resist demand collapse, and recover rapidly during major exogenous shocks, such as Ground Delay Programs (GDP; FAA traffic initiatives holding departures at origin gates during destination weather bottlenecks), severe winter blizzards, and summer convective thunderstorm ground stops (Kazda et al., 2022; Schultz et al., 2021).

- **Generalizability (Cross-Airport Portability)**: The external validity and portability of trained model structures when deployed across structurally diverse airport terminal complexes without requiring site-specific historical recalibration (Güner & Seçkin Codal, 2024; Tang et al., 2023).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.


---

# Chapter III

## Methodology

This chapter details the approach and analytical framework to evaluate and optimize passenger flow forecasting, specifically at airport security checkpoints. To provide a structural roadmap for this investigation, the methodology is organized into five components:

**Research Approach**: Establishes the theoretical framework, research variables, hypotheses, experimental design, and the technical apparatus utilized.

**Sample**: Outlines the multi-tiered macro and micro sampling frameworks used to categorize physical checkpoint environments and terminal architectures.

**Sources of Data**: Identifies the primary authorized data repositories supplying the longitudinal datasets.

**Validity**: Addresses and controls internal and construct threats, specifically related to passenger flow bias and screening lane heterogeneity.

**Treatment of Data**: Details the sequential pipeline used to ingest, clean, standardize, and align the data sources.

## Research Approach

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

**Feature Paradigm Hypothesis (**$H_{2}$**)**: Predicting multi-day temporal rolling volatility ($\sigma _{TSA, 7d}$) cannot be achieved using static flight volume levels (Feature Values), which collapse during structural shocks ($R^{2}<0$), but requires tracking operational dispersion (Feature Volatility metrics, achieving $R^{2}>0.30$).

### Design and Procedures

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

### Predictive Modeling Frameworks and Baseline Control

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

### Dataset Partitioning and Validation Protocol

Models were trained, tuned, and evaluated across the 32-month Candidate B development partition:

**Training Window**: May 1, 2022 to December 31, 2023 (15,976 airport-days; 122,847 hourly observations across the filtered cohort).

**Validation Window**: January 1, 2024 to December 31, 2024 (3,293 airport-days; 72,723 hourly observations), strictly reserved for hyperparameter tuning.

**Out-of-Time Holdout Window**: January 1, 2025 to December 31, 2025 (3,222 airport-days; 72,053 complex-level screening hours), strictly reserved for final out-of-time evaluation.

**Operational Separation Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades and severe convective storm disruptions do not leak across evaluation boundaries.

### Quantitative Evaluation Dimensions and Operational Regimes

Airport operations are structured into a three-tier operational taxonomy:

**Tier 1: Nominal On-Time Baseline**: Departure delays $<15 minutes$ and zero tactical cancellations ($N_{cancels}=0$). Grounded in the FAA/DOT A14 regulatory reference benchmark, this state serves as an experimental control to observe pure passenger show-up curves without airside delay distortion.

**Tier 2: Routine Daily Operations**: Everyday commercial hub reality, characterized by ambient 15–30 minute delays, gate holds, and normal 1–2% cancellation churn.

**Tier 3: Irregular Operations (IROPS)**: Severe convective disruptions, ground delay programs (GDP), and winter weather cascades, defined as hours where departure delays $\ge 45 minutes$ or tactical cancellations $\ge 5$.

Performance is evaluated across three orthogonal dimensions:

**Dimension 1: Robustness (Nominal & Routine Operations)**: Verifying that a model delivers dependable, low-error volatility forecasts during standard daily flight banks. Governing metrics: Root Mean Squared Error ($RMSE_{routine}$) and Mean Absolute Scaled Error ($MASE_{routine}$). Explicit target: $min\left(RMSE_{routine}\right)$ and $MASE_{routine}<0.700$.

**Dimension 2: Resilience (Severe Disruption Recovery)**: Verifying that a model resists demand collapse and recovers rapidly during severe storm ground stops and irregular operations. Governing metrics: Disruption Error Multipliers ($R_{RMSE}$ and $R_{MASE}$), Disruption Error ($MASE_{shock}$), and Time-to-Recovery ($TTR$). Explicit target: $R_{RMSE}\approx 1.00 \left(R_{MASE}\approx 1.00\right),min\left(MASE_{shock}\right)$, and $TTR<4.0 hours$.

**Dimension 3: Generalizability (Cross-Airport Transferability)**: Verifying whether a model calibrated at one airport (e.g., Newark Liberty, EWR) can be deployed directly to a different airport with distinct gate layouts (e.g., New York LaGuardia, LGA) without site-specific retraining. Governing metrics: Relative Transfer Ratio ($RTR=RMSE_{transfer}/RMSE_{in-sample}$) and Percentage Change in Transfer MASE ($\Delta MASE_{transfer}$). Explicit target: $RTR\approx 1.00 \left(1.00\pm 0.05\right)$ and $\Delta MASE_{transfer}\le 10.0%$.

### Apparatus and Materials

To manage, parse, and evaluate the large datasets required for this study, the following software and computing resources are used:

**Google Antigravity and Python**: Utilized as an integrated agentic framework and primary data ingestion engine to manage high-volume government data dumps during the ETL process. To ensure data integrity at this scale, custom scripts handled automated data pulling, unzipping, spatial parsing, and relational joining workflows in the data pipeline for downstream predictive modeling.

**Microsoft Excel for Mac & Microsoft Power BI**: Deployed locally for advanced data transformation, tabular synthesis, and visual validation.

**Vega High-Performance Computing (HPC) Cluster**: The remote institutional environment used to execute resource-intensive Python algorithms, filtering large-scale raw data down to determine airport and airline parameters.

## Sample

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

**Balanced Factorial Cohort**: Applying this four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort** across 12 carrier-exclusive screening complexes:

**American Airlines (AA)**: Dallas/Fort Worth (DFW), Philadelphia (PHL), Chicago O'Hare (ORD)

**Delta Air Lines (DL)**: Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)

**United Airlines (UA)**: Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles (LAX) This cohort achieves complete factorial symmetry: exactly 3 legacy carriers $\times$ 3 dedicated terminal environments, spanning all four operational archetypes identified in national clustering.

### Temporal Scope and Boundary Definition

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic operational volatility induced by the COVID-19 pandemic (Sun et al., 2021; Gao, 2022). While a baseline 'post-pandemic' operational era is provisionally considered as beginning January 1, 2023, an exploratory analysis is performed during data preprocessing to refine this demarcation due to varying definitions of ‘post-pandemic’ (ICAO, 2024; Centre for Aviation, 2025).

This preprocessing step evaluates pre-pandemic baseline patterns against longitudinal 2019–2025 data to pinpoint the empirical inflection point where system throughput and schedule deviations returned to steady-state normalization. Structural break tests, rolling Welch's $t$-tests, and CUSUM analyses identified **May 1, 2022** (Candidate B demarcation) as the empirical inflection point, coinciding with the vacatur of the federal transit mask mandate and the rebound of airline load factors to 84.7%, matching pre-pandemic baselines. Restricting the active dataset to this verified window enables the forecasting models to capture contemporary queue dynamics and schedule-driven variability without being skewed by transient historic anomalies.

## Sources of Data

Secondary operational data will be compiled from four primary authorized repositories covering the 2019 to 2025 period (TSA, 2026; BTS, 2026; LAWA, 2026):

### TSA FOIA Security Screening Checkpoint Logs

Obtained via Freedom of Information Act (FOIA) disclosures and cross-referenced with public archival repositories, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### BTS On-Time Flight Performance

Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

### BTS Form 41 Schedule T-100 Domestic Segment Data

Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

### BTS Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), supplemented by authorized monthly airport traffic reports (such as LAX Air Traffic Statistics). These feeds are utilized to extract quarterly connecting passenger ratios across airport pairs to support originating passenger flow estimation.

## Validity

### Internal Validity Threats and Remediation Protocols

A primary threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand (the "Hub Disconnect"). To reduce this bias, origin-and-destination survey data (BTS DB1B) and airport-specific O&D ratios are used to estimate and remove connecting traffic from passenger flow calculations, isolating true originating landside checkpoint demand.

Additional internal validity controls include:

**Operational Partition Boundary Leakage**: Multi-day delay cascades and weather ground stops can create artificial temporal dependency across model evaluation boundaries. To prevent lookahead bias and contamination, strict 7-day operational purge buffers are enforced between training, validation, and testing partitions.

**Exogenous Airspace Shock Confounders**: Localized thunderstorm systems or regional FAA ground delay programs could confound cross-carrier comparisons. Enforcing meso-level filtering guarantees that all carrier complexes within the study cohort operate under identical airspace shocks ($\delta _{t}$).

### Construct Validity Threats and Operational Formulations

Construct validity is affected by checkpoint heterogeneity, as raw lane counts obtained from TSA throughput data combine different screening modes, such as TSA PreCheck, with standard screening lanes, each exhibiting disparate processing rates ($\approx 250–300$ pax/lane-hr for PreCheck vs. $\approx 150–180$ pax/lane-hr for standard). To resolve this heterogeneity threat, the methodology constructs scale-free relative volatility metrics ($CV_{TSA}$) and standardized lane measures rather than unadjusted raw totals.

Furthermore, construct validity requires establishing explicit mathematical formulations that measure passenger throughput volatility rather than static volume levels:

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

## Treatment of Data

The execution of data preparation follows a rigorous, sequential Extract, Transform, Load (ETL) pipeline designed to ingest, clean, standardize, and align the longitudinal aviation datasets:

### Extract

Download TSA Throughput files from the FOIA reading room (PDFs) spanning 2019 to 2026.

Parse PDFs into standardized tabular format (CSV).

Download TSA Throughput PDFs and CSVs (2022–2025) from public repository archives (e.g., https://github.com/mikelor/TsaThroughput).

Cross-reference TSA datapoints to identify temporal gaps, duplicates, and reporting inconsistencies.

Download On-Time Flight Performance data (CSVs) spanning 2019 to 2026 for all domestic flights in the United States.

Download BTS Form 41 Schedule T-100 Segment Airline Traffic Data and calculate monthly route load factors.

Download BTS DB1B ticket survey coupon files and airport-specific origin-and-destination summary statistics.

Perform an audit across the 7-year sequence to identify missing data and reporting discontinuities.

### Transform

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

Construct the Values versus Volatility feature representation space:

*Feature Values (Levels, 14 Attributes)*: Schedule Scale (sched_daily_total, actual_daily_total, sched_hourly_mean, sched_rolling_7d_mean), Cancellations (daily_cancellations, daily_cancel_rate, cancel_rolling_7d_mean, cancel_rate_rolling_7d_mean), Delays (avg_dep_delay_minutes, flights_delayed_15min_pct), Surface Queues (avg_taxi_out_minutes), and Network Buffers (aircraft_gauge_seats, route_load_factor_pct, connecting_passenger_share_pct).

*Feature Volatilities (Dispersion, 10 Attributes)*: Schedule Dispersion (sched_hourly_std, sched_hourly_cv, actual_hourly_std, actual_hourly_cv, sched_rolling_7d_std, sched_rolling_7d_cv), Cancellation Dispersion (cancel_rolling_7d_std, cancel_rate_rolling_7d_std, otp_cancellation_volatility_cv), and Delay Dispersion (otp_departure_delay_volatility_cv).

*Combined Dual Paradigm (24 Attributes)*: Interacts both feature spaces to test predictive complementarity.

### Load

Load master conformed data copies to secure persistent cloud storage (OneDrive) and local data warehouse directories.

Build relational analytics tables, lookup dimensions, and multidimensional interaction tensors.

Automate verification audits for schema validity, referential integrity, and row preservation across the 7-year sequence.


---

# Chapter IV

## Findings and Discussion

This chapter presents the empirical findings and comparative performance evaluations for modeling the stochastic volatility of airport passenger screening throughput ($\sigma _{TSA}$ and $CV_{TSA}$). The study evaluates three candidate operational models – Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model) – against an empirical Baseline Control across a 2025 holdout dataset. The empirical results reveal that no single forecasting architecture is universally superior across all operational regimes. Instead, models exhibit distinct asymmetric trade-offs.

To systematically present and discuss these results (see Figure 4.1), this chapter is organized into four sections: Section 4.1 presents the initial exploratory data analysis across the multi-source data warehouse; Section 4.2 details the four-tier filtering pipeline that establishes the nine-airport, twelve-complex experimental cohort; Section 4.3 outlines feature engineering, training configurations, and 2025 holdout execution protocols; and Section 4.4 discusses the comparative model evaluations across robustness, resilience, and generalizability.

Figure 4.1

## Initial Exploratory Data Analysis

### Descriptive Statistics

To construct an empirically rigorous predictive modeling architecture that eliminates temporal and feature lookahead leakage for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw operational transaction records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys (Appendix for details).

Following conformed extraction, automated entity resolution, data cleaning, and relational synthesis across standardized operational dimensions (calendar date, departure time block, airport, operating carrier, fleet aircraft type, and dedicated screening complex), the nationwide post-ETL analytical warehouse retains 42,062,039 conformed records across the candidate network of the Top 25 U.S. commercial airports. Table 4.1 documents the post-ETL data foundation census across all four federal data sources. Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census*

Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

See Appendix for a discussion of descriptive statistics for post ETL Data

### Temporal Boundaries

A core methodological requirement of this thesis is that defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on individual facility characteristics rather than learning generalizable aviation temporal dynamics.

**Post-Pandemic Regime Selection and Structural Break Analysis. **Structural break analysis – combining rolling Welch’s $t$-tests and Cumulative Sum (CUSUM) trajectory tracking across the Top 25 airports – confirmed May 1, 2022, as the structural equilibrium demarcation point for predictive model development. This demarcation is grounded in three empirical realities: the nationwide rescission of federal transit mask requirements on April 18, 2022, which restored unconstrained traveler behavior and returned domestic passenger load factors to 84.7%; the stabilization of commercial coupling between scheduled flights and screening demand from an artificial pandemic high ($r=0.607,R^{2}=36.85%$) down to normalized post-recovery equilibrium ($r=0.553,R^{2}=30.61%$); and the establishment of a clean 32-month development baseline. This development window was partitioned into a 20-month training window (May 1, 2022 – December 31, 2023), a 12-month validation window (January 1, 2024 – December 31, 2024), and an untouched 12-month out-of-time holdout test set (January 1, 2025 – December 31, 2025), separated by a 7-day operational purge buffer to prevent multi-day delay cascades from leaking across partition boundaries.

### Defining Seasonality

Just as temporal boundaries must be established on the complete Top 25 network, defining seasonality requires capturing the full variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and non-consecutive turbulence peaks. See appendix for Seasonality Dimensions detail. It is important to define these for models to take into account so like for like is being compared.

***TSA and OTP Throughput Data***

Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airports reveals fundamental econometric dynamics. Refer to the appendix which synthesizes the master cross-dataset econometric correlations. This analysis provided distinct empirical insights:

**The Hub Disconnect**. Raw scheduled flight departures explain only 20.90% ($R^{2}$) of TSA security checkpoint passenger throughput across the Top 25 network ($r=0.4572,p<0.05$). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to 44.94% ($r=0.6704,p<0.001$), an increase of +115%. For instance, major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70% to 76% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.

**Coupled Volatility and Asynchronous Lag Dynamics**. While raw delay rates show weak same-hour linear correlation with passenger volumes ($r=0.2019,R^{2}=4.08%$), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ($CV_{TSA}$) is significantly coupled with flight departure delay volatility ($r=0.4375,R^{2}=19.14%,p<0.05$). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume tracks tightly with weekly flight departure delay variance ($r=0.9022,R^{2}=81.40%,p<0.01$), reflecting synchronized macro peak seasonal demand across the network rather than landside queues causing airside pushback delays.

## *Implications for Subset*

Establishing temporal boundaries (the May 1, 2022 post-mask demarcation) and seasonal dynamics across the full Top 25 network ensures that baseline operational patterns reflect macroeconomic aviation behavior rather than idiosyncratic facility quirks. To maintain strict methodological integrity and prevent predictive errors, these macro-level seasonal regimes and cross-dataset relationships are not used as direct regression features. Instead, they serve strictly to justify the operational filtering pipeline, inform feature architectures (such as cyclical encodings and lead-lag show-up windows), and establish an uncompromised foundation for downstream modeling.

The exploratory analysis also reveals that commercial airports must initially be evaluated as whole facilities to verify operational scale and hub cluster diversity but cannot be modeled at the aggregate airport level. In shared-terminal facilities, coordinated airline flight banks generate severe multi-carrier collinearity (see appendix for equation) making it mathematically impossible to separate individual airline passenger contributions and restricting explained checkpoint variance to only ~20%. Isolating dedicated, single-carrier screening complexes is therefore essential to eliminate shared-terminal confounding and reveal the true empirical relationship between airline departure banks and landside security queue arrivals.

## Data Filtering and Subset Selection

### Four-Phase Filtering Pipeline

To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, airports were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling.

The four-phase purposive filtering pipeline systematically isolates single-carrier screening dynamics from confounding network interactions. In Phase 1 (Macro Filter), the national candidate pool of 450+ commercial airports was filtered down to the Top 25 airports, enforcing heavy queuing intensity ($\rho _{t}\to 1.0$) during departure banks, capturing 67.2% of nationwide domestic departures, and establishing a baseline correlation of $r=0.4572$($R^{2}=20.90%$) between raw flights and screening throughput. Phase 2 (Meso Filter) restricted these facilities to 14 candidate hubs exhibiting concurrent mainline operations ($>10%$ seat share) across American, Delta, and United, excluding low-cost carrier scheduling fluctuations and raising coupling to $r=0.5015$($R^{2}=25.15%$). Phase 3 (Micro Filter) screened for strict carrier checkpoint exclusivity ($P\left(Carrier=j^{*}\mid Checkpoint=1\right)=1$), eliminating shared-terminal multi-carrier collinearity ($\kappa <25$) and elevating coupling to $r=0.5453$($R^{2}=29.74%$) for raw flights and $r=0.6466$($R^{2}=41.81%$) when adjusting for local connecting ratios. Finally, Phase 4 (Balanced Experimental Cohort) established a factorial design across 12 dedicated screening complexes (exactly four complexes each for American, Delta, and United) spanning all four operational cluster archetypes, achieving final dedicated checkpoint-to-flight coupling of $R^{2}=70.80%$to $77.40%$. For an in depth outline of the phases, please refer to the appendix

### Pipeline Results

The filtering pipeline isolated 9 commercial airports representing 12 carrier-exclusive screening environments, achieving complete balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

Table 4.6  
*The Nine-Airport Experimental Cohort Specification*

To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed: Carrier Ticket Boarding Dominance, No-Mainline Zero Activity, Cross-Carrier Leakage, and Airside Concourse Isolation (detailed in the Appendix).

### Descriptive Statistics for Subset

Table 4.7 presents the descriptive summary statistics for the nine-airport experimental cohort compared against the Top 25 candidates.

Table 4.7  
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25*

Compared to the broader Top 25 network, the 9-airport cohort exhibits higher flight movement density, higher delay and cancellation exposure, and high local originating demand. For details on comparing the top 25 network to the 9 airport cohort, please refer to the appendix.

***Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports***

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airports display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 in the appendix reports the day-of-week passenger throughput distribution across the nine airports. The 9 airports exhibit three distinct weekly demand dynamics, which can be found in the Appendix.

### Implications for Model Development

The empirical findings from subset selection establish four mandatory architectural requirements for airport passenger flow modeling. First, passenger throughput must be modeled at dedicated single-carrier screening complexes rather than airport-wide aggregates to eliminate multi-carrier bank confounding and capture terminal-specific arrival surges. Second, departing seat capacity must be deflated by empirical DB1B connecting ratios ($1-ConnectingRatio_{airport}$), preventing the $>200%$ throughput overprediction that occurs when airside connecting passengers at hubs such as DFW, DTW, and ORD are erroneously assumed to enter landside checkpoints. Third, models must enforce strict information availability by using prior-hour operational indicators ($t-1$) and tactical cancellations rather than concurrent departure delays, avoiding lookahead bias since flight delays are unconfirmed until pushback occurs. Finally, predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models ($p=1.3$) or two-stage hurdle structures – to accommodate positive throughput skewness and structural zeros during overnight curfew hours without generating impossible negative volume prediction.

## Model Development and Execution

### Feature Engineering

A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)*

Unshifted scheduled flights in the same departure hour explain less than 12% of checkpoint throughput variance. Explanatory power peaks across the Lead $t+1$ and Lead $t+2$ horizons ($R^{2}\approx 24%$), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). After scaling by booked load factors and deflating airside connecting passengers who never enter landside security, this transformation converts published flight timetables into an accurate baseline forecast of checkpoint queuing demand. See appendix for the complete feature engineering pipeline.

### Model Training

To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control. The Baseline Control assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion. Model 1 (Deterministic Flight Schedule Model) projects passenger arrival dispersion by convolving scheduled airline flight departure banks across empirical ACRP Report 40 show-up curves ($t+1,t+2,t+3$), capturing schedule geometry without requiring machine learning or live delay telemetry. Model 2 (Supervised Machine Learning Model) uses an automated decision-tree architecture trained across convolved schedule features and 24 Bureau of Transportation Statistics (BTS) On-Time Performance operational attributes (cancellations, prior-hour delays, and taxi queues). Model 3 (Dynamic Two-Stage Hybrid Model) couples scheduled flight cycles with live prior-hour recursive error correction ($e_{t-1}=y_{t-1}-\hat{y}_{t-1}$) from actual screening counts to sense passenger accumulation during flight delays. Using the partitions and 7-day purge buffer established in Section 4.1, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation.

***Model Testing***

All candidate architectures were evaluated against the untouched 2025 Full-Year Out-of-Time Holdout Dataset. Forecast performance was evaluated against the primary thesis target of diurnal throughput volatility ($\sigma _{TSA, hr}$, measured as pax/hr standard deviation across the 24 hours of each day) alongside scale-free relative volatility ($CV_{TSA, hr}=\sigma /\mu$). Models were benchmarked across standard operational performance criteria, including the Coefficient of Determination ($R^{2}$), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias. Please see appendix for details on how to interpret these standard operational performance criteria.

### Implications for Final Result Interpretation

When interpreting model evaluation metrics, several operational realities must be considered:

**Dispersion Scale vs. Volume Scale**. Unlike mean hourly throughput volume (which averages ~1,750 pax/hr across dedicated complexes), diurnal throughput standard deviation ($\sigma _{TSA, hr}$) averages 540 to 880 passengers per hour across hub complexes. An RMSE of ~220 pax/hr represents an exceptionally close fit to intraday arrival swings.

**MASE as the Primary Standard for Volatility Forecasting**. MASE normalizes errors against daily persistence ($Vol_{t-24}$). A MASE below 0.85 indicates substantial predictive skill beyond historical patterns, while a MASE below 0.70 represents outstanding accuracy.

**Conformal Staffing Buffers**. Airport security planners can translate predicted throughput volatility directly into risk-buffered lane allocations to prevent queue overflow during peak departure banks.

## Model Results and Evaluation

### Results

Table 4.10 reports the out-of-time evaluation benchmark matrix across the candidate model architectures on the 2025 holdout dataset.

Table 4.10  
*Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Holdout)*

### General Model Performance Across the 9-Airport Cohort

The empirical results reveal clear performance separations across the modeling paradigms:

**The Deterministic Schedule Baseline (Model 1)**. Relying solely on published flight schedules, Model 1 achieved $Test R^{2}=0.4980$($RMSE=313.4$ pax/hr, $MASE=0.945$). This outperforms daily persistence by 5.5% ($MASE<1.000$), demonstrating that schedule geometry alone captures approximately half of total checkpoint arrival variance without requiring machine learning infrastructure

**Supervised Machine Learning (Model 2)**. Adding operational flight delays and cancellations elevated explained variance to $R^{2}=0.6178$($RMSE=273.5$ pax/hr, $MASE=0.779$). Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ($DM=42.15,p<0.0001$).

**The Dynamic Two-Stage Hybrid (Model 3):** Incorporating live prior-hour error feedback yielded the highest overall holdout fit, explaining 74.83% of passenger throughput volatility variance ($Test R^{2}=0.7483$, $RMSE=222.1$pax/hr, $MASE=0.662$).

### Model Performance and Hypothesis Testing

The thesis hypothesis (Hypothesis 1) asserts that distinct modeling frameworks exhibit asymmetric performance strengths across operational robustness, resilience, and generalizability, with no single paradigm proving universally superior across all operational regimes. To test this hypothesis, candidate architectures were evaluated against explicit performance targets defined across three operational dimensions: Robustness, defined as achieving the lowest $RMSE_{routine}$and $MASE_{routine}<0.70$under Nominal On-Time Baseline conditions; Resilience, defined as maintaining a Recovery Multiplier $R_{RMSE}\approx 1.00$and the lowest $MASE_{shock}$during irregular operations; and Generalizability, defined as maintaining a Relative Transfer Ratio $RTR\approx 1.00$with $\Delta MASE_{transfer}\le 10.0%$under zero-shot spatial transfer without model retraining.

### Empirical Confirmation of Asymmetric Trade-Offs

**Dimension 1: Robustness (Nominal & Routine Conditions)**. Both the Machine Learning model (Model 2) and Dynamic Hybrid (Model 3) achieve the academic target of $MASE<0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport managers to generate staffing schedules days in advance rather than waiting on live hourly sensor updates.

**Dimension 2: Resilience (Severe Disruption). **The Dynamic Hybrid Framework (Model 3) is the decisive champion of Resilience. While the Machine Learning (Model 2) suffers from the "Empty Checkpoint Fallacy" during delayed flight holds ($R_{MASE}=2.14$), Model 3's recursive error feedback ($e_{t-1}$) maintains a resilient multiplier of $R_{MASE}=1.05\approx 1.00$ and achieves the fastest Time-to-Recovery ($TTR=2.8 hours$).

**Dimension 3: Generalizability (Zero-Shot Portability)**. The Deterministic Model (Model 1) is the decisive champion of Generalizability. It successfully meets both stated targets: $RTR=1.04\approx 1.00$ and $\Delta MASE=+4.0%\le 10.0%$. Conversely, the Hybrid model (Model 3) decisively fails the Generalizability targets ($RTR=1.19>1.00,\Delta MASE=+21.5%>10.0%$) because its decision-tree component overfits to Newark's specific terminal layout and carrier bank timings.

The out-of-time holdout evaluations confirm the thesis hypothesis: no single predictive modeling paradigm is universally superior across all operational regimes. Instead, airport security demand forecasting is governed by fundamental asymmetric trade-offs across robustness, resilience, and generalizability. The Dynamic Hybrid model (Model 3) is best during severe flight delays and irregular operations, the Deterministic Schedule model (Model 1) transfers most reliably to new airports without retraining, and the Supervised Machine Learning model (Model 2) is the most practical choice for routine advance staffing. Airport operators and TSA leadership should therefore select their forecasting tool based on daily operating conditions rather than relying on a single method.


---

# Chapter V: Conclusions and Recommendations

These findings demonstrate that airport authorities and TSA planners should not seek a singular, monolithic forecasting tool. Instead, operational efficiency requires a contingent forecasting framework: utilizing deterministic schedule convolution for multi-airport master planning, supervised machine learning for advance weekly lane scheduling, and dynamic hybrid feedback for tactical day-of-operations management when convective disruptions occur.

## Spatial Architecture and Passenger Behavioral Dynamics

The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:

### Connecting Passenger Shielding (The Hub Disconnect)

At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by $\left(1-ConnectingRatio\right)$ derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.

### Terminal Complex Aggregation

Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.

### Behavioral Invariance Across Terminal Layouts

The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.

## Initial Training and Passenger Show-Up Dynamics

The striking performance gap between unshifted flight schedules ($R^{2}=-0.0586$ on out-of-time volatility) and lead-lag passenger show-up schedules ($R^{2}=0.5344$ to $0.6178$) resolves the operational lead-lag time offset inherent in air travel (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior. Incorporating lead horizons ($t+1,t+2,t+3$) enables the model to anticipate incoming passenger surges well before gate departure times. Furthermore, flight delays must be handled asymmetrically: including same-hour actual flight delays introduces severe lookahead bias (since departure delays are not known until after aircraft push back), whereas incorporating prior-hour delays ($t-1$) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict operational information availability.

Passenger screening throughput temporally precedes terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turnaround times and network delays compound. Aligning flight departures and passenger throughput in the same hour without lead-lag structure introduces severe misspecification error ($R^{2}<0.20$ on volume, and negative $R^{2}=-0.0586$ on volatility). Importantly, landside security queues do not cause flight departure delays – airlines enforce strict gate closure rules and depart without missing passengers – rather, systemic airside delays and ground holds cascade backward into the terminal, stranding ticketed passengers landside and creating passenger dwell that unshifted models fail to predict.

Table 5.1  
*Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models*

## Empirical Evaluation of Robustness

The primary research hypothesis asserted that distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures. Under this first dimension the methodology established two explicit performance targets:

- Lowest $RMSE_{routine}$ to minimize absolute forecast error during standard flight waves.

- $MASE_{routine}<0.700$, demonstrating substantial error reduction relative to simple daily persistence.

The findings confirm that both the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) successfully meet the target threshold, achieving $MASE_{routine}\le 0.700$ and $0.662$ respectively, compared to the daily persistence baseline ($MASE=1.000$) and deterministic flight scheduling (Model 1, $MASE=0.945$). In terms of absolute dispersion error, Model 3 achieves the lowest routine RMSE (222.1 pax/hr), capturing 74.83% of holdout volatility variance ($R^{2}=0.7483$) by combining daily flight schedules with decision-tree corrections. Standard statistical loss differential tests confirm that error reductions are statistically decisive ($DM=42.15$ and $DM=48.72,p<0.0001$) across all nine cohort airfields. Crucially, from an airport management perspective, Model 2 delivers the optimal practical choice for routine everyday operations: it meets the stringent $MASE<0.70$ target without requiring live real-time feedback or continuous data connections to security lane sensors, making it the preferred choice for routine day-to-day checkpoint staffing.

## Empirical Evaluation of Resilience Under Disruption

Evaluating the second dimension, the methodology posited that dynamic hybrid models combining scheduled flight baselines with live operational error feedback would demonstrate superior resilience during acute disruptions. Under severe disruption regimes (hours with departure delays $\ge 45$ min or tactical cancellations $\ge 5$), the performance targets were defined:

- **Disruption Error Multiplier (**$R_{MASE}\approx 1.00$**)**, demonstrating that error does not inflate relative to routine performance.

- **Lowest **$MASE_{shock}$, maintaining maximum operational accuracy during irregular operations.

- **Time-to-Recovery (**$TTR<4.0 hours$**)**, returning to nominal error bounds quickly.

The empirical findings establish the Dynamic Two-Stage Hybrid Model (Model 3) as the decisive, undisputed winner of Resilience. Model 3 achieves $RMSE_{shock}=254.2 pax/hr$ and $MASE_{shock}=0.694$ (the lowest across all models), outperforming daily persistence by 30.6% and deterministic scheduling by 35.9%. Model 3 successfully hits the Disruption Multiplier target with $R_{MASE}=1.05\approx 1.00$, proving that its prediction fidelity remains stable during severe ground stops. Time-to-Recovery analysis indicates a rapid recovery of 2.8 hours, easily beating the $<4.0 hour$ benchmark, and recovering 5.0 hours faster than deterministic schedules ($7.8h$) and 2.6 hours faster than pure machine learning ($5.4h$). In contrast, pure supervised machine learning (Model 2) suffers an acute fragility collapse ($R=2.14>2.0$), and deterministic schedules (Model 1) degrade significantly ($R=1.32,MASE=1.082$) due to complete blindness to real-time ground hold dynamics.

## Empirical Evaluation of Generalizability Across Facilities

Evaluating the third dimension of Hypothesis 1, the methodology posited that first-principles deterministic models would generalize significantly better across distinct terminal layouts than complex, over-parameterized models. To rigorously test zero-shot transferability without local retraining, models trained on United at Newark Liberty (EWR Terminal C) were directly deployed to Delta at New York LaGuardia (LGA Terminal C), holding macro New York regional airspace congestion constant while testing spatial transfer across different carrier bank structures and facility geometries.

The performance targets for Generalizability were strictly specified:

- **Relative Transfer Ratio (**$RTR=RMSE_{transfer}/RMSE_{in-sample}=1.00$**)**.

- **Change in MASE on Transfer (**$\Delta MASE_{transfer}\le 10.0%$**)**, ensuring minimal performance penalty.

The Deterministic Flight Schedule Model (Model 1) is the decisive of Generalizability. Model 1 achieves an $RTR$ of 1.04 ($\approx 1.00$, target met) and a $\Delta MASE$ of only +4.0% (+0.038, well below the 10.0% ceiling), suffering a mere +4.2% RMSE transfer degradation. Because Model 1 relies on universal flight schedule convolution and empirical passenger show-up curves, its structural logic is completely invariant to facility-specific quirks. In cross-cluster transfer (DTW $\to$ PHL), Model 1 achieves an $RTR$ of 1.003, verifying complete spatial generalizability. The Dynamic Hybrid (Model 3) decisively fails the Generalizability Targets. Model 3 experiences a severe +19.0% transfer degradation, with an $RTR$ of 1.19 (failing the target of 1.00) and a $\Delta MASE$ surge of +21.5% (+0.142, failing the $\le 10.0%$ threshold). This empirical failure confirms the central thesis of asymmetric trade-offs: the decision-tree component of Model 3 overfits to Newark's specific terminal geometry, flight bank timings, and local gate configurations. When transferred to LaGuardia without local recalibration, those specialized decision boundaries fail, imposing a heavy transfer penalty. Supervised Machine Learning (Model 2) exhibits robust intermediate portability ($RTR=1.08$, $\Delta MASE=+8.3%\le 10%$), passing the transfer targets due to standardized OTP feature scaling.

## Implications and Recommendations for Predictive Forecasting in Airport Operations

The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models. Rather than forcing a single model across all conditions, aviation planners should adopt a dual-track strategy that routes routine, clear-weather days through automated machine learning, while engaging dynamic feedback models during convective weather storms and flight cascading delays. By pairing predicted volatility with dynamic safety buffers rather than staffing to simple daily averages, security planners can insulate checkpoint throughput against sudden flight disruption waves without incurring unnecessary labor costs. The following represent the main implications and resulting recommendations based on study results:

- **Dynamic Checkpoint Allocation**: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.

- **Connecting Ratio Integration**: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.

- **Deployment of Two-Stage Hybrid Estimators**: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ($t-1$) during severe convective ground stop disruptions.

Collectively, these three strategic adjustments transform airport checkpoint management from a rigid, reactive posture into a synchronized, demand-responsive operational system. By incorporating empirical lead-lag curves and connecting passenger ratios, security planners eliminate the persistent spatial and temporal mismatches that plague legacy time-of-day staffing tables. This prevents both the over-allocation of screening resources at major transfer hubs and the localized under-staffing caused by compressed departure banks. Furthermore, integrating live throughput feedback during convective weather disruptions resolves the vulnerability of purely schedule-driven forecasts, ensuring that checkpoint capacity rapidly recalibrates when flight delays cascade across the terminal. Rather than treating security screening as an isolated landside function, this unified predictive architecture bridges airline flight schedules, passenger arrival behaviors, and live checkpoint queuing dynamics to protect passenger throughput standards without inflating annual operating budgets.
