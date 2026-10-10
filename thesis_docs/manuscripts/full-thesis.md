# Chapter I: Introduction


As air travel demand outpaces airport infrastructure growth, inefficient resource allocation has become a critical operational bottleneck (Adacher, Flamini, Guaita & Romano, 2017). Barriers such as prohibitive capital costs and municipal land constraints severely restrict physical terminal expansion (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). Consequently, airport operators and federal security authorities must extract maximum operational throughput from fixed physical assets through software-driven predictive intelligence.


While predictive models are widely deployed to anticipate terminal demand, the systemic disruptions of the COVID-19 pandemic and subsequent recovery exposed critical vulnerabilities in traditional, accuracy-centric evaluation standards (Sun, Wandelt, & Zhang, 2022). These unprecedented operational disruptions demonstrated that conventional accuracy metrics, while necessary, are insufficient as the sole basis for evaluating models intended for volatile airport operating environments. Specifically, the pandemic revealed that a singular evaluation standard is inadequate across highly variable operational contexts, necessitating the assessment of predictive models through a broader, multidimensional set of performance measures. In airport operations, the most useful predictive model is therefore not necessarily the one with the lowest average forecast error but the model that:

- **Robustness (Remains reliable during routine operations)**: Providing consistent, low-error baseline volatility forecasts during undisturbed flight banks.
- **Resilience (Maintains stability and recovers rapidly during disruptions)**: Absorbing severe exogenous shocks (such as winter freeze events or summer convective ground delay programs) without generating false demand collapses or runaway queue backlogs.
- **Generalizability (Transfers effectively across operational contexts)**: Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study examines the suitability of predictive modeling frameworks – spanning deterministic operational baselines (such as persistence and scheduled flight bank dispersion), data-driven decision-tree architectures (automated rule-based machine learning models), and sequential two-stage hybrid models (combining schedule baselines with real-time error correction) – for forecasting Transportation Security Administration (TSA) checkpoint throughput volatility across routine, volatile, and disrupted demand regimes.


## Significance of the Study


This research aims to contribute to both theory and practice by shifting the paradigm of how predictive models are evaluated in unpredictable airport operations. While traditional approaches emphasize static accuracy, this study advances the field by establishing a multidimensional, dynamic evaluation framework that assesses models based on their robustness, resilience, and generalizability. By identifying which forecasting techniques remain reliable during operational disruptions and structural breaks, it offers airport operators actionable, data-driven insights for selecting models that sustain TSA throughput, safety, and service rates under fluctuating post-pandemic conditions.


## Statement of the Problem


Airport passenger arrivals and behaviors are inherently stochastic, varying significantly by time of day, flight schedules, and external factors (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Existing models for managing airport passenger flow tend to rely on static or pre‑pandemic assumptions, consequentially failing to account for unpredictable post‑pandemic travel patterns (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Lee & Yu, 2024). This mismatch between capacity planning and fluctuating passenger demand contributes to bottlenecks at check‑in counters, TSA checkpoints, and boarding gates, ultimately leading to congestion and inefficient resource allocation. While recent global disruptions have proven that historical baselines are insufficient for contemporary airport logistics, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond standard accuracy metrics. Because modern forecasting can no longer remain predicated on deterministic conditions, the absence of an adaptable evaluation methodology leaves airports at risk of deploying tools that fail to respond to sudden demand shocks or generalize across shifting operational realities.


## Purpose Statement


The primary objective is to evaluate predictive modeling techniques, such as regression, machine learning, and queuing simulation, to optimize airport capacity via technological rather than physical – and more costly – intervention. By analyzing the relationship between flight operations and TSA throughput, this study evaluates various predictive modeling frameworks against the primary criteria of robustness, resilience, and generalizability. Rather than seeking a singular, universally optimal model, this research identifies which frameworks perform best under each distinct metric. Ultimately, this comparative analysis provides management with the strategic flexibility to adopt the most appropriate forecasting approach based on their specific operational priorities.


## Research Questions


Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule dispersion baselines, supervised machine learning tree ensembles, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?


The Asymmetric Trade-Off $H_1$ : Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability).

- $H_{1a}$ (Robustness Target: Lowest $RMSE_{\text{routine}}$ and $MASE_{\text{routine}} < 0.700$): Supervised machine learning (Model 2) and two-stage dynamic hybrids (Model 3) will successfully achieve the robustness target ($MASE_{\text{routine}} < 0.700$) under nominal operating conditions by capturing non-linear flight schedule dispersion and lead-lag passenger arrivals, whereas naive persistence (Baseline Control) and deterministic flight schedules (Model 1) will fail this threshold ($MASE \ge 0.94$). Supervised machine learning (Model 2) will deliver the computationally lightweight, Pareto-efficient routine solution with zero online feedback latency.
- $H_{1b}$ (Resilience Target: $RRMSE≈1.00 RMASE≈1.00$, Lowest $MASE_{\text{shock}}$, and $TTR<4.0 hours$): The Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience target due to recursive 1-step error innovation feedback ($e_{t-1}$). Static supervised machine learning (Model 2) will experience severe performance degradation ($R \ge 2.0$) resulting from the Empty Checkpoint Fallacy during flight ground delays, while deterministic baselines (Model 1) will remain blind to downline delay cascades.
- $H_{1c}$ (Generalizability Target: $RTR \approx 1.00$ and $\Delta MASE_{\text{transfer}} \le 10.0\%$): The Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($RTR≈1.00,ΔMASE≤10.0%$) under zero-shot spatial transfer without local retraining because flight schedule convolution is invariant to local terminal geometry. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($RTR≫1.00,ΔMASE>10.0%$) due to decision tree terminal geometry overfitting.

## Delimitations


This study focuses on U.S. airports and uses post-pandemic TSA throughput and flight performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where needed to define the post-pandemic baseline. Dynamic queuing models and simulationbased methods are assessed using standard statistical measures, including pvalue, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE). These delimitations are detailed in the appendix.


## Limitations and Assumptions


Due to reliance on public data, confidential variables like staffing and manual queue management fall outside the scope of this analysis. While external factors such as weather, regulatory impacts, or IT outages may not be fully accounted for, the framework assumes that utilized data is consistent and findings from the selected airports are generalizable across similar facilities and circumstances. Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level. These limitations are detailed in the appendix.

---

# Chapter II

## Review of the Relevant Literature

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure (Federal Aviation Administration [FAA], 2024; International Air Transport Association [IATA], 2026), the prohibitive financial and spatial costs of continuous brick-and-mortar expansion have shifted operational focus toward software-driven, data-informed terminal capacity management (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). Airport landside subsystems—specifically ticketing lobbies, security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled stochastic queuing networks. When passenger demand surges outstrip processing capacity at security screening, congestion ripples backward into ticketing halls and forward into departure concourses, inducing boarding holds, tarmac delays, and passenger misconnections across the National Airspace System (Adacher et al., 2017). Historically, airport passenger flow modeling prioritized statistical fit and mean throughput optimization under static operating assumptions. However, the unprecedented systemic shocks of the COVID-19 pandemic and subsequent recovery demonstrated that models calibrated solely on clear-weather historical averages fail catastrophically during operational disruptions (Sun et al., 2022).

To address these vulnerabilities, this literature review traces the evolution of airport passenger flow prediction across five core theoretical domains: (a) traditional approaches and operational complexity, examining how airline flight banks violate classical Poisson assumptions and demonstrating why heavy-traffic queuing principles mandate modeling throughput volatility rather than mean volume; (b) simulation modeling and real-time terminal management, evaluating the structural strengths of Discrete Event Simulation alongside its severe tactical limitations during live disruptions; (c) time-series analysis and machine learning, comparing linear statistical models with deep sequence architectures and tree-based ensembles while examining administrative barriers of black-box opacity and spatial transfer degradation; (d) hybrid predictive architectures, exploring methodologies that couple deterministic flight schedules and empirical show-up curves with machine-learned residual estimators and recursive state-space error feedback; and (e) multi-dimensional operational evaluation, establishing the theoretical foundations for the evaluation triad—Robustness, Resilience, and Generalizability—that governs this research.

## Traditional Approaches and Operational Complexity

### Subsystem Coupling, Terminal Capacity Limits, and Security Bottlenecks

Commercial airport terminals are complex operational ecosystems where physical space, human behavior, and airline schedules intersect (Birolini & Jacquillat, 2023; Nazir et al., 2022; Solak et al., 2009; Zhang et al., 2012). Grounded in the foundational infrastructure planning principles of De Neufville and Odoni (2014), terminal landside subsystems operate in a state of delicate interdependency: local bottlenecks at upstream ticketing check-in counters or downstream security checkpoints rapidly propagate across the entire facility (Adacher & Flamini, 2020; Chiti et al., 2018). In an empirical assessment of terminal processing subsystems, Alnowibet et al. (2022) demonstrated at Cairo International Airport that server utilization routinely exceeds physical processing capacity during scheduled peak hours, triggering acute passenger queues that cascade across concourses.

To quantify terminal congestion, early civil engineering frameworks established Level of Service (LOS) standards based on spatial passenger density and allowable waiting times (Fernandes & Pacheco, 2002; Lemer, 1988; Parizi & Braaksma, 1994). However, as passenger demand approached terminal capacity limits, static LOS thresholds proved inadequate for managing dynamic queues (Di Mascio et al., 2020; Orhan & Orhan, 2020). Using bottleneck detection algorithms and virtual queuing simulations, Liu (2018) and Lu et al. (2018) identified Transportation Security Administration (TSA) passenger screening checkpoints as the primary rate-limiting decelerator of overall passenger flow. Furthermore, Marzuoli et al. (2019) verified that screening line delays propagate directly into airside operations, inducing gate pushback holds and slot misallocations. In modeling sequential terminal operations, Hess and Grbčić (2019) demonstrated that terminals function as multiphase queuing networks where upstream delays multiply downstream service backlogs. Micro-level analyses by Wei (2017) and Zhang et al. (2017) using Generalized Stochastic Petri Nets (GSPN) proved that idle "dead time" between divestiture, walk-through metal detectors, and luggage retrieval severely depresses effective checkpoint service rates ($\mu$), making security screening the pivotal operational bottleneck in airport landside infrastructure.

### Batch Arrival Dynamics and Flight Bank Synchronization

A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, passenger arrivals are characterized by extreme non-linear fluctuations and concentrated "batches" induced by airline flight bank scheduling (Cheng et al., 2012; Peterson et al., 1995). In hub-and-spoke networks, commercial airlines deliberately compress 20 to 40 flight departures into narrow 45-to-90-minute waves to maximize passenger transfer opportunities (Schultz & Fricke, 2011). Consequently, terminal screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, continuous arrival streams (Dönmez et al., 2025). As Peterson et al. (1995) proved in their foundational mathematical analysis of airport congestion, flight banking produces transient, non-stationary queuing states where sudden demand bursts generate queues that persist long after the flight bank has departed.

### Classical Queuing Theory: Volume Versus Volatility

To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon Queuing Theory (Horie, 1985; Odoni, 1986; Wang, 2017)—the mathematical study of waiting lines and server allocation. Early terminal capacity models utilized Poisson arrival distributions (such as $M/M/s$ or $M/G/s$ queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) relative to target Level of Service benchmarks (Araujo & Repolho, 2015). However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP; Brunetta et al., 1999) to incorporate time-varying arrival rates $\lambda(t)$ and reconcile published schedules with observed arrival waves (Nikoue et al., 2015), NHPP formulations remain conceptually constrained in two decisive ways. First, NHPP models evaluate queuing almost exclusively through expected mean volume (the first-order moment: $\mu = \mathbb{E}[Y]$). Second, by preserving the Poisson assumption of independent inter-arrival times, NHPP models fail to account for the high correlation among passengers arriving for the same ticketed flight bank and ignore the shielding effect of airside connecting passengers (Adeke, 2018; Guo et al., 2022).

### Second-Order Queuing Volatility: The Kingman and Allen-Cunneen Formulation

In operational reality, heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993) demonstrate that expected queue wait times ($W_q$) and passenger backlogs in general $G/G/s$ screening facilities scale not with mean volume, but linearly with the squared coefficient of variation of arrival times ($C_a^2$) and service times ($C_s^2$) via the Allen-Cunneen approximation:

$$W_q \approx \left(\frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)}\right)\left(\frac{C_a^2 + C_s^2}{2}\right)\frac{1}{\mu}$$

where $\rho = \frac{\lambda}{s\mu}$ represents checkpoint lane utilization. As checkpoint utilization approaches capacity ($\rho \to 1.0$) during morning and evening departure peaks, the utilization multiplier grows exponentially. Under these heavy-traffic conditions, any increase in arrival volatility ($C_a^2$) triggers dramatic queue length expansion and terminal crowd surges. Modeling and forecasting throughput volatility ($\sigma_{\text{TSA}}$ and $\text{CV}_{\text{TSA}}$) is therefore the vital prerequisite for robust lane staffing, operational stability, and passenger delay mitigation (Adeke, 2018; Guo et al., 2022).

### The "Values versus Volatility" Paradigm in Transportation Demand

In modern econometric and volatility forecasting literature (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005), a central research question is whether predicting the volatility of a stochastic process requires tracking the values (levels, volumes, and magnitudes) of explanatory variables, the volatility (dispersion, standard deviations, and coefficients of variation) of those variables, or a dual combined representation. In commercial aviation operations, this duality manifests across two operational horizons:

**Intraday Diurnal Volatility.** The within-day standard deviation ($\sigma_{\text{TSA, hr}}$) naturally scales with airport passenger volume due to Tweedie-Poisson compound dispersion ($\text{Var}(Y) \propto \mu^p$), allowing feature values (e.g., total scheduled flights, aircraft seats) to serve as a strong baseline predictor. However, when normalized into scale-free relative burstiness ($\text{CV}_{\text{TSA, hr}} = \sigma / \mu$), volume levels lose explanatory power.

**Multi-Day Rolling Volatility.** Over multi-day horizons ($\sigma_{\text{TSA, 7d}}$), static flight volumes remain largely unchanged across seasonal schedules. Consequently, models relying exclusively on static feature values fail to anticipate medium-term passenger turbulence. Forecasting disruption-driven turbulence requires tracking the volatility of operational features—specifically rolling schedule variance ($\sigma_{\text{sched}}$), flight cancellation volatility ($\text{CV}_{\text{cancel}}$), and departure delay dispersion ($\sigma_{\text{Delay}}$) (Hopfe et al., 2024).

## Simulation Modeling and Real-Time Terminal Management

### Discrete Event Simulation in Terminal Planning and Asset Allocation

To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static analytical spreadsheets, DES models track individual simulated passengers through a chronological sequence of discrete physical milestones: ticket scanning, divestiture (removing shoes, outer garments, laptops, and liquids for X-ray inspection), body scanning, and item retrieval. In operational planning, these micro-simulation frameworks proved highly effective for static terminal dimensioning. Guizzi et al. (2009) demonstrated that simulating passenger trajectories from check-in through security screening allowed planners to model queuing interdependencies, while Parlar et al. (2016) used event-based simulations to optimize dynamic counter opening schedules. Furthermore, Nwofia and Chung (2013) highlighted the utility of simulation in linking terminal architectural layouts to long-term service performance, enabling airport authorities to evaluate proposed flight schedules and lane configurations under synthetic operating loads (Araujo & Repolho, 2015; Ateş et al., 2021). Stochastic planning methodologies (Verki et al., 2013), virtual terminal infrastructure tracking (Edwards, 2026), and simulated human behavioral loads (Perez, 2021) supported asset distribution, while algorithm-based congestion detection (Palaşcă & Stăncel, 2025) recontextualized Poisson queuing within dynamic monitoring frameworks. Additionally, simulation environments such as ARENA (Olusanya et al., 2020; Oprea et al., 2024) and simulation data farming (Patrón et al., 2021) have served as offline synthetic data generators for evaluating security subsystems.

### The Tripartite Operational Breakdown of Micro-Simulation

Despite high visual fidelity and granular representation of physical terminal corridors, Discrete Event Simulation models exhibit three critical operational failure modes when deployed for real-time tactical airport management:

**Calibration Sensitivity and Parameter Brittleness.** Discrete event simulations are hyper-sensitive to micro-level behavioral calibrations. Brown and Madhavan (2011) demonstrated that minor fluctuations in baseline operational assumptions—such as a 5% increase in secondary carry-on baggage search alarm rates or slight variations in Transportation Security Officer (TSO; federal screening personnel) divestiture coaching times—produce disproportionately massive non-linear swings in predicted checkpoint queue lengths. Because human behaviors during high-stress terminal surges do not adhere to fixed parameter distributions, small calibration errors compound across sequential service stages, undermining forecast credibility for tactical staffing.

**Computational Latency During Unfolding Disruption.** Tactical airport terminal management requires actionable forecast revisions within a 15-to-30-minute operational window. However, simulating hundreds of thousands of individual entity interactions across a multi-terminal hub requires substantial computational time (Takakuwa & Oyama, 2004). During severe flight disruptions, such as summer convective thunderstorm ground stops, airline flight schedules change dynamically every few minutes. Bießlich et al. (2014) showed that DES models suffer acute fidelity collapse during unpredicted flight delays because the computational latency required to re-seed, execute, and average stochastic Monte Carlo runs prevents airport operations centers from deploying them for real-time lane reallocation.

**The Passive Traveler Behavioral Assumption.** Standard discrete event simulations treat airline passengers as passive physical particles adhering to rigid, pre-programmed logic paths (Alodhaibi et al., 2017). In modern commercial aviation, however, passengers are proactive, information-empowered agents. When airlines issue mobile flight delay alerts, passenger arrival distributions shift dynamically: business travelers delay their arrival at the airport, while leisure travelers with checked luggage may arrive early to negotiate flight rebookings. Because DES architectures cannot readily incorporate real-time behavioral adaptation without cumbersome rule re-engineering, their ability to model live terminal volatility remains fundamentally constrained.

## Time-Series Analysis and Data-Driven Predictive Frameworks

### Statistical Time-Series Foundations and Linear Limitations

To achieve faster, automated forecasts without the computational latency of micro-simulation, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Box et al., 2015; Hyndman & Athanasopoulos, 2018; Li et al., 2017). These models predict future passenger throughput by capturing the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations (Babu, 2014; Saki & Soori, 2026). When augmented with exogenous variables (SARIMAX)—such as published airline scheduled seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed historical relationships that cannot accommodate sudden delay cascades (Lin et al., 2023). When flight schedules diverge from historical patterns, SARIMA's autoregressive error lags predict phantom demand or miss delayed surges entirely, highlighting the necessity of non-linear predictive techniques.

### Non-Linear Machine Learning: Deep Learning Versus Tree Ensembles

To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including deep sequence models such as Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and tree ensembles like Gradient-Boosted Decision Trees (GBM) (Hewamalage et al., 2021; Hopfe et al., 2024; Orsini et al., 2019; Ribeiro et al., 2025). While deep neural networks can approximate complex multi-source interactions (e.g., weather indices, search engine trends, flight departure status), tabular decision-tree ensembles have demonstrated superior empirical efficacy in aviation operational prediction. In a rigorous comparative benchmark of terminal passenger flow models, Hopfe et al. (2024) proved that Gradient-Boosted Decision Trees systematically outperform deep recurrent architectures on structured tabular flight data, achieving lower forecast error and greater numerical stability while avoiding the massive compute requirements of neural networks. Furthermore, Ribeiro et al. (2025) demonstrated that tree-based gradient boosting enables interpretable decision rules under flight delay uncertainty, allowing operational controllers to extract actionable screening queue thresholds.

### Operational Barriers to Deep Neural Architectures in Security Infrastructure

Despite their theoretical expressiveness, end-to-end deep neural networks face severe operational and administrative barriers that prevent their adoption in commercial airport security environments:

**The "Black-Box" Interpretability Hurdle.** Airport Federal Security Directors (FSDs) and TSA operations planners operate under strict administrative, security, and staffing budget mandates. FSDs cannot commit multimillion-dollar security screening labor allocations or deploy overtime checkpoint personnel based on opaque, uninterpretable neural network weights (Adadi & Berrada, 2018; Viaña et al., 2024). When an algorithm predicts an unexpected surge, security leadership requires defensible, rule-based explanations grounded in scheduled flight departures and upstream airside delays before reallocating federal screening officers.

**Facility-Specific Over-Specialization and Spatial Transfer Degradation.** Highly parameterized deep neural networks tend to memorize terminal-specific spatial configurations, local carrier flight bank timings, and idiosyncratic gate walking distances. In a comprehensive spatial transferability study, Wang et al. (2025) proved that end-to-end deep learning models suffer severe performance degradation (error inflation exceeding 40%) when transferred zero-shot to an unfamiliar airport facility. This facility over-specialization prevents the national deployment of deep neural networks across heterogeneous commercial airports without costly, site-specific retraining.

### From Passive Prediction to Active Control and Passenger Guidance

Recognizing the limits of passive flow prediction, recent transportation literature has explored active control frameworks where predictive models inform real-time operational decisions. Multi-agent reinforcement learning has been utilized to model proactive passenger navigation under terminal constraints (Li & Gao, 2023), although Anagnostopoulou et al. (2024) documented persistent functional gaps in capturing actual flow volumes. To close the loop between prediction and tactical intervention, Diaz-Gutierrez et al. (2025) developed Model Predictive Control (MPC) algorithms that integrate stochastic terminal dynamics into automated resource optimization loops. Concurrently, Lee et al. (2025) and Yang et al. (2022) formulated dynamic passenger guidance and rescheduling strategies to balance crowding across parallel departure checkpoints in real time. These active control formulations demonstrate that high-utility forecasting tools must provide transparent, actionable inputs that align directly with operational decision rules.

## Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability

### Coupling Physical Flow Conservation with Machine Learning

To resolve the tension between the domain transparency of first-principles queuing models and the non-linear predictive flexibility of machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025; Jenčová et al., 2025). Rather than treating terminal demand as an unconstrained black-box regression problem, effective hybrid frameworks decouple terminal passenger flow into a two-stage sequential pipeline: a deterministic operational baseline capturing physical schedule structure, paired with a machine-learned residual estimator capturing operational disruptions, augmented by dynamic feedback. While deep fusion models (He et al., 2024) and decision forest ensembles (Blasco-Puyuelo et al., 2023; Xia et al., 2020) combine heterogeneous predictive pathways, operational viability in airport security environments requires structural simplicity and auditability.

### First-Principles Operational Baseline: Flight Schedules, ACRP Report 40, and DB1B Connecting Deflation

The structural foundation of a defensible terminal model relies on published flight schedules convolved across empirical passenger arrival behavior. The definitive federal engineering guideline, Airport Cooperative Research Program (ACRP) Report 40 (Airport Passenger Terminal Planning and Design; Transportation Research Board [TRB], 2010), establishes that commercial passenger arrival distributions follow an empirical lognormal curve, with peak passenger arrivals concentrating between 90 and 120 minutes prior to scheduled domestic departures. However, applying raw flight schedules directly to checkpoint demand introduces severe distortion in hub airports. Guo et al. (2022) established that airside transfer passengers in hub-and-spoke networks never enter landside ticketing lobbies or pass through security screening. Therefore, an operational baseline must incorporate a connecting passenger deflator derived from Bureau of Transportation Statistics (BTS) DB1B origin-destination ticket surveys, isolating true checkpoint-originating passenger demand from airside connections. This deterministic base provides an interpretable, highly portable operational baseline that operates without complex training.

### Transparent Residual Adjustments via Decision Trees

While scheduled operations provide a stable baseline under nominal conditions, real-world terminal volatility is driven by tactical airside disruptions: departure delays, ground delay programs, gate holds, and cancellations. Rather than discarding the structural baseline during disruptions, hybrid models deploy supervised machine learning to predict the residual error between scheduled demand and actual checkpoint throughput (Brun et al., 2025; Hopfe et al., 2024; Ribeiro et al., 2025). Utilizing Gradient-Boosted Decision Trees (GBM) for residual estimation offers a decisive operational advantage over deep neural networks: their hierarchical branching structure functions like intuitive, transparent decision rules (e.g., "If departure delay dispersion exceeds 45 minutes and cancellation rate exceeds 5%, adjust expected security volatility upward by +35%"). This decision-rule transparency enables airport controllers to verify and audit model behavior during severe weather disruptions.

### Dynamic Feedback and Recursive State-Space Error Estimation

During catastrophic disruptions—such as severe summer convective storms where flight departure times are repeatedly rolled back—static flight schedules lose predictive validity. Under these conditions, static baseline models suffer from the "Empty Checkpoint Fallacy," predicting zero demand when flights are delayed, even as stranded passengers crowd terminal screening lobbies. To prevent forecast divergence, recent transportation literature incorporates recursive error-correction feedback grounded in Kalman filtering and state-space estimation (Anupam & Lawal, 2024; Ebert et al., 2021; Wu et al., 2024). By continuously monitoring live checkpoint throughput and calculating the 1-step error innovation ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$), the model dynamically adjusts its expected passenger backlog in real time. This dynamic feedback loop bridges the gap between pre-flight scheduling and live terminal floor operations, allowing the system to absorb severe demand shocks and recover rapidly.

### Contextualizing Heuristic and Optimization Lineages

Earlier literature in airport systems planning explored stochastic optimization and probabilistic graphical models to manage operational uncertainty. Hybrid Queue-based Bayesian Networks (HQBN; Wu et al., 2014) combined analytical queuing equations with directed acyclic graphs to diagnose bottleneck causes, while Guo et al. (2025) coupled Bayesian networks with the Best-Worst Method to evaluate terminal resilience factors. In parallel, metaheuristic optimization algorithms—such as Particle Swarm Optimization (PSO) and simulated annealing (Jiang et al., 2024; Naji et al., 2020; Sörensen, 2015; Wu, 2024)—were deployed to optimize parameter spaces in complex airport baggage and ground transit networks. While valuable for offline optimization, these metaheuristic frameworks lack the sub-second inference speeds and transparent decision rules required for tactical TSA checkpoint lane reallocation, underscoring the superior operational alignment of two-stage tree-based hybrid architectures.

Table 2.1  
*Comparative Modeling Paradigm Taxonomy for Airport Passenger Screening Throughput*

| Modeling Paradigm | Mathematical Foundation | Operational Strengths | Critical Operational Limitations | Key Citations |
| :--- | :--- | :--- | :--- | :--- |
| **Classical Queuing Theory** | Poisson / Exponential: $M/M/s$, $M/G/s$, NHPP | Closed-form solutions; transparent parameterization; negligible compute latency. | Fails under batch flight banks; ignores airside connecting passenger shielding; assumes static arrival rates. | Odoni (1986); Wang (2018); Brunetta et al. (1999); Guo et al. (2022). |
| **Discrete Event Simulation (DES)** | Stochastic entity tracking through discrete physical screening stages. | High micro-level spatial and lane layout fidelity; granular TSO lane configuration. | Extreme calibration sensitivity; high compute latency during disruptions; passive traveler assumptions. | Brown & Madhavan (2011); Takakuwa & Oyama (2004); Bießlich et al. (2014). |
| **Linear Statistical Time-Series** | Autoregressive moving average: $\text{SARIMAX}(p,d,q) \times (P,D,Q)_s$ | Lightweight; captures diurnal (24h) and weekly (168h) cycles; clear confidence bounds. | Fails during structural breaks and severe weather ground stops; cannot model non-linear delays. | Li et al. (2017); Box et al. (2015); Hyndman & Athanasopoulos (2018). |
| **Supervised Machine Learning (GBM)** | Non-linear decision trees: Gradient Boosting (HistGBM) minimizing Tweedie loss | Captures non-linear delays, aircraft gauge, and weather; fast inference; auditable rules. | Susceptible to "Empty Checkpoint Fallacy" during flight delays; overfits to local terminal geometry. | Hopfe et al. (2024); Ribeiro et al. (2025); Chen & Guestrin (2016). |
| **Deep Neural Networks (LSTM / GRU)** | Recurrent hidden state: Gated recurrent units $h_t = \sigma(W_{hh} h_{t-1} + W_{xh} x_t + b)$ | Directly models complex long-sequence dependencies without manual feature engineering. | Complete "black-box" opacity; FSD adoption resistance; severe spatial transfer degradation (>40% error). | Hochreiter & Schmidhuber (1997); Adadi & Berrada (2018); Viaña et al. (2024); Wang et al. (2025). |
| **Sequential Two-Stage State-Space Hybrids** | Stage 1 Physical Schedule + Stage 2 Tree Residual + Kalman Innovation Feedback | Superior routine accuracy; high disruption resilience ($R_{\text{MASE}}$); high cross-airport portability. | Multi-stage training complexity; requires automated ingestion of live prior-hour floor throughput ($y_{t-1}$). | Brun et al. (2025); Had et al. (2025); Ebert et al. (2021); Wu et al. (2024). |

*Note.* Table synthesized from thesis literature review. Taxonomy formalizes the theoretical trade-offs across candidate modeling paradigms evaluated in Chapter IV.

## Post-Pandemic Operational Volatility and the Triad of Operational Evaluation

### The COVID-19 Catalyst and the Breakdown of Single-Metric Benchmarks

The COVID-19 pandemic represents the definitive empirical catalyst that fundamentally reshaped commercial aviation operations and exposed the severe limitations of legacy terminal forecasting methodologies (Li et al., 2023; Sun et al., 2022). Prior to the 2020 global disruption, academic literature and airport planning practice evaluated passenger flow forecasting algorithms almost exclusively through single-metric point accuracy—minimizing average statistical loss such as Root Mean Squared Error (RMSE) or Mean Absolute Error (MAE) under nominal on-time conditions. This historical paradigm rested upon a foundational, unstated assumption of operational stationarity: planners assumed that passenger arrival behaviors, diurnal peaking factors, and airline schedule structures would remain stable over multi-year planning horizons, permitting static time-of-day tables and linear enplanement scaling to guide security checkpoint staffing.

The unprecedented operational shocks of the COVID-19 pandemic permanently dismantled this stationarity assumption. The pandemic imposed abrupt, systemic structural breaks on terminal operations: commercial passenger volumes plummeted by over 90% in spring 2020, followed by an asymmetric, highly turbulent multi-year recovery characterized by permanent shifts in passenger composition, altered business-to-leisure traveler ratios, volatile passenger arrival lead times, and decentralized terminal queue processing (Mota et al., 2021). As highly tuned historical models collapsed amidst these procedural shifts, the pandemic exposed that evaluating a forecasting tool solely on its clear-weather, nominal historical accuracy creates a dangerous illusion of reliability: a model that achieves minimal average forecast error during undisturbed, calm flight banks frequently experiences catastrophic failure during irregular operations (Li et al., 2023).

Crucially, the post-pandemic operational environment demonstrated that security checkpoints do not experience operational tipping points from gradual changes in average daily volume. Rather, terminal screening failures are driven by acute surges in **passenger arrival volatility**. When airline departure banks compress hundreds of passengers into narrow arrival windows, or when convective weather ground delay programs cascade across hub networks, arrival bursts overwhelm screening lane capacity, triggering exponential queue wait-time escalation under stochastic queuing dynamics. Therefore, the COVID-19 disruption provides the concrete operational imperative for this study: it demonstrates why predictive modeling must transition from static volume forecasting to condition-responsive volatility modeling, and why candidate predictive architectures must be evaluated across a multidimensional performance triad rather than a singular point error metric:

### Dimension 1: Robustness (Routine Operational Accuracy)

Grounded in the operational frameworks of Lin (2022), robustness reflects the consistency, precision, and low dispersion of forecast errors under nominal, on-time operating conditions (the FAA A14 reference benchmark: departure delays < 15 minutes and cancellations = 0). A robust operational model must reliably minimize baseline RMSE without exhibiting high residual variance or excessive computational overhead during everyday hub operations.

### Dimension 2: Resilience (Performance Under Severe Disruption)

Formalized by Schultz et al. (2021) and Kazda et al. (2022), resilience evaluates a model's stability and recovery trajectory during severe Irregular Operations (IROPS), such as FAA Ground Delay Programs (GDP; traffic initiatives holding departures at origin gates during destination bottlenecks), severe winter blizzards, and summer convective thunderstorm ground stops (departure delays ≥ 45 minutes or cancellations ≥ 5). Resilient models resist demand collapse, avoid the "Empty Checkpoint Fallacy," maintain error boundedness ($R_{\text{MASE}} \approx 1.00$), and demonstrate a rapid Time-to-Recovery ($\text{TTR} \le 4$ hours) following acute operational shocks.

### Dimension 3: Generalizability (Cross-Airport Zero-Shot Portability)

Drawing upon the infrastructure transferability principles of Tang et al. (2023) and Güner & Seçkin Codal (2024), generalizability measures the external validity and portability of a model when deployed across structurally diverse airport terminal facilities without requiring site-specific historical recalibration. A generalizable architecture achieves a Relative Transfer Ratio ($\text{RTR} \approx 1.00$) and minimizes transfer error degradation ($\Delta\text{MASE} \le 10\%$), preventing the costly facility over-fitting typical of complex machine learning systems.

### Theoretical Synthesis, Asymmetric Trade-Offs, and Chapter III Handoff

Crucially, this three-dimensional evaluation framework reveals inherent operational trade-offs ($H_1$): no single forecasting paradigm universally dominates all three operational dimensions (Hopfe et al., 2024). A model engineered to maximize routine accuracy (Robustness) may collapse during severe weather shocks (Resilience), while a complex architecture tuned to absorb disruption may overfit to local terminal geometry and fail zero-shot spatial deployment (Generalizability). By formalizing these three pillars, this research establishes an objective, domain-grounded evaluation methodology that bridges the gap between theoretical data science and defensible TSA security checkpoint management, providing the direct theoretical handoff to the 4-tier filtering pipeline, the 3-model candidate evaluation suite, and the empirical benchmarks in Chapters III, IV, and V.

## Summary

In summary, this literature review establishes that modeling airport security checkpoint passenger flow requires moving beyond static, volume-centric assumptions toward dynamic, volatility-informed paradigms. Commercial air terminals operate as tightly coupled queuing networks where flight bank clustering, connecting passenger flows, and severe convective weather induce acute arrival burstiness that scales queue delays quadratically under Kingman's principles ($C_a^2$). The literature demonstrates that isolated analytical approaches are insufficient: deterministic schedules cannot adapt to tactical delay cascades, micro-simulations demand prohibitive calibration overhead, and unconstrained machine learning models fall victim to the Empty Checkpoint Fallacy during severe operational shocks. Conversely, hybrid predictive frameworks that couple deterministic flight schedule baselines with machine learning residual adjustments and recursive error feedback synthesize the structural stability of schedule dynamics with the empirical flexibility of data-driven learning. Evaluating these candidate architectures across the operational triad of nominal robustness, disruption resilience, and zero-shot generalizability provides the theoretical foundation for the empirical methodology and experimental design formulated in Chapter III.

---

---

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

---

# Chapter IV: Findings and Discussion

This chapter presents the empirical findings and comparative performance evaluations for modeling the stochastic volatility of airport passenger screening throughput ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$). The study evaluates three candidate operational models—Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model)—against an empirical Baseline Control across the 2025 out-of-time holdout dataset. The empirical results reveal that no single forecasting architecture is universally superior across all operational regimes. Instead, models exhibit distinct asymmetric trade-offs.

To systematically present and discuss these results, this chapter is organized into four core sections: Section 4.1 presents the initial exploratory data analysis across the multi-source data warehouse; Section 4.2 details the four-tier purposive filtering pipeline that establishes the nine-airport, twelve-complex experimental cohort; Section 4.3 outlines feature engineering, training configurations, and 2025 holdout execution protocols; and Section 4.4 discusses the comparative model evaluations across robustness, resilience, and generalizability, including the values versus volatility operational coupling.

## 4.1 Initial Exploratory Data Analysis

### Descriptive Statistics
To construct an empirically rigorous, leak-free predictive modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw fact records across four primary federal feeds:
1. **TSA FOIA Checkpoint Logs**: Hourly passenger throughput records disaggregated by physical screening lane.
2. **Bureau of Transportation Statistics (BTS) On-Time Performance (OTP, Form 234)**: Flight-level departure movements tracking scheduled and actual departure times, tarmac taxi-out durations, departure delays, cancellations, and causal delay attributions.
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Monthly carrier-route-equipment records reporting available departing seats, transported revenue passengers, and load factors.
4. **BTS DB1B / DB1C Origin-Destination Ticket Surveys**: A 10% randomized sample of airline passenger itineraries detailing coupon routes, connecting transfer ratios, and true local originating passenger fractions.

Following conformed extraction, automated entity resolution, data cleaning, and relational synthesis across conformed dimension keys (*dim_date*, *dim_time_block*, *dim_airport*, *dim_airline*, *dim_aircraft*, *dim_checkpoint*), the nationwide post-ETL analytical warehouse retains **42,062,039 conformed records** across the candidate network of the Top 25 U.S. commercial airfields. Table 4.1 documents the post-ETL data foundation census across all four federal data sources.

Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)*

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| TSA FOIA Checkpoint Logs | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| BTS On-Time Performance (OTP) | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| BTS Form 41 Schedule T-100 | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| BTS DB1B / DB1C Ticket Surveys | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| Combined Analytical Warehouse | Multi-Source Fact Records | 67,222,828 | 42,062,039 | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

| Operational Domain | Variable Name | Sample Size ($N$) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| TSA Throughput | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| Flight Delays | Flight Departure Delay (minutes) | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| Flight Delays | Significant Delay Rate ($\ge$ 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Flight Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Runway Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| Flight Operations | Airborne Flight Duration (min) | 13,153,654 | 141.50 | 126.00 | 75.40 | 92.00 | 15.00 | 720.00 | 45.00 | 310.00 |
| Flight Operations | Scheduled Flight Distance (miles) | 13,153,654 | 1,052.12 | 867.00 | 624.80 | 820.00 | 67.00 | 5,095.00 | 230.00 | 2,550.00 |
| Route Capacity | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| Route Capacity | Transported Pax per Route-Month | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| Route Capacity | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| Passenger Surveys| Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($\sigma = 69,376$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually ($\sigma = 27.76\text{M}$; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period.

To guarantee econometric and machine learning validity, comprehensive data hygiene protocols—including spatial key resolution to isolate unidentifiable airport records, preservation of scheduled overnight curfew closures as true operational structural zeros, and strict advance versus tactical flight cancellation causality filtering—were enforced during warehouse staging. The full operational definitions and failure-mode remediations for these data hygiene protocols are detailed in Appendix K.

### Temporal Boundaries

A core methodological requirement of this thesis is that **defining temporal boundaries must be performed on the broad Top 25 airport dataset** to prevent localized facility overfitting.

#### Post-Pandemic Regime Demarcation and Structural Break Analysis
The post-pandemic operational equilibrium was established beginning **May 1, 2022** based on structural break stabilization and regulatory milestones:
1. **Federal Transit Mask Mandate Repeal**: The nationwide vacatur of federal transit mask requirements on April 18, 2022 restored unconstrained business and leisure travel behavior. By May 1, 2022, load factors recovered to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stability**: In the post-May 2022 equilibrium, the relationship between scheduled flights and checkpoint throughput stabilized to $r = 0.553$ ($R^2 = 30.61\%$), reflecting normalized booking curves.
3. **Partitioning Design**: The post-pandemic window establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations). A 7-day operational purge buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries. Complete structural break details are documented in Appendix G.

### Defining Seasonality
Just as temporal boundaries must be established on the complete Top 25 network, **defining seasonality requires capturing the full variance of nationwide commercial aviation**. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks.

#### Annual Seasonal Regimes and Coupled Volatility
Airport operational stress is not uniform across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3). The Coupled Volatility Index is defined as:
$$\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$$

Table 4.3  
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)*

| Seasonal Regime | Operational Regime Description | Calendar Days ($N$) | Share of Days (%) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) | Cancellation Rate (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1_OFF_PEAK | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | 27.85 | 9.85 min | 18.00% | 0.89% |
| 2_MID_PEAK | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | 32.38 | 15.14 min | 23.23% | 1.36% |
| 3_PEAK | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | 39.36 | 24.17 min | 31.04% | 3.16% |
| 4_HOLIDAY | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | 33.07 | 16.51 min | 24.33% | 1.82% |

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

#### Day-of-Week Cyclical Dynamics and Archetypes
Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes (Table 4.4):
1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($19.44\%$ and $20.05\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

Table 4.4  
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)*

| Day of Week | DOW Name | Operational Volatility Archetype | Study Days ($N$) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Monday | Outbound Business Surge & High Screening Volatility | 192 | 1,246,150 | 0.604 | 56.56 min | 34.00 | 15.78 min | 23.54% |
| 2 | Tuesday | Midweek Operational Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | 50.09 min | 29.99 | 11.69 min | 19.44% |
| 3 | Wednesday | Midweek Baseline Stability (Minimum Volatility) | 192 | 1,123,368 | 0.594 | 49.27 min | 29.13 | 12.22 min | 20.05% |
| 4 | Thursday | Corporate Outbound & Early Weekend Ramp | 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| 5 | Friday | Combined Business & Weekend Getaway Surge | 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| 6 | Saturday | Volume Trough & Fleet Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| 7 | Sunday | Leisure Return Peak & Evening Delay Propagation | 192 | 1,279,017 | 0.577 | 58.07 min | 33.40 | 17.78 min | 25.60% |

#### Diurnal Non-Consecutive Dual Turbulence Peaks
Rather than dividing the 24 hours of each operational day into arbitrary consecutive time blocks, diurnal hours were categorized by the Operational Turbulence Shock Index ($T(h)$), which evaluates passenger screening surge volatility and flight departure delay dispersion:
* **1_OFF_PEAK (Overnight & Curfew Valley)**: Typically covering 00:00 to 03:00 (3–4 hours/day), where commercial departures are sparse and checkpoint demand is minimal.
* **2_MID_PEAK (Midday Plateau & Transition)**: Covering 08:00 to 13:00/16:00 (4–12 hours/day), characterized by steady passenger screening flow and balanced aircraft turnaround buffers.
* **3_PEAK (High Queuing Turbulence / Dual Peaks)**: Uniquely groups non-consecutive turbulence periods into a single operational regime:
  1. *Morning Bank Surge (05:00–08:00)*: Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr).
  2. *Evening Delay Cascade (14:00/17:00–22:00)*: Driven by upstream flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min).

The cross-classification of the 4 annual seasonal regimes ($\mathcal{S}$), 7 days of the week ($\mathcal{D}$), and 3 diurnal blocks ($\mathcal{H}$) forms an **84-cell interaction tensor** ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$). Across this tensor, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $N_{\text{train}} \ge 50$ (median $N_{\text{train}} = 215$), confirming that defining temporal baselines on the Top 25 airfields establishes ample sample power without sparse-sample estimation bias.

### TSA Throughput and Flight On-Time Performance (OTP) Data
Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airfields reveals fundamental econometric dynamics. Table 4.5 synthesizes the master cross-dataset econometric correlations.

Table 4.5  
*Master Cross-Dataset Econometric Relationships (Top 25 Airfields)*

| Relationship Category | Metric 1 (OTP / Capacity) | Metric 2 (TSA Demand / Queue) | Sample Grain | Pearson $r$ | $R^2$ (%) | $t$-statistic | $p$-value | Operational Significance & Interpretation |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| Volume Coupling | Raw Scheduled Flight Departures | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.4572 | 20.90% | 2.47 | $< 0.05$ | Modest linear coupling; scheduled flights alone explain only 20.9% of checkpoint passenger variance due to connecting passenger volume. |
| Connecting Deflation | Raw Scheduled Flight Departures | True Local Originating TSA Demand | Top 25 Airfields | 0.6704 | 44.94% | 4.33 | $< 0.001$ | Strong linear coupling; removing connecting transfers via DB1B ticket surveys increases explained variance by +115% (from 20.9% to 44.9%). |
| Hub Scale vs. Connecting| Connecting Passenger Ratio (%) | Scheduled Flight Volume | Top 25 Airfields | 0.4503 | 20.28% | 2.42 | $< 0.05$ | Hub scale effect; larger airline hub operations inherently possess higher connecting passenger fractions (e.g., CLT 76.0%, ATL 70.1%). |
| Surface Queue Feedback | Runway Taxi-Out Queue Time (min) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2867 | 8.22% | 1.44 | $0.163$ | Directional trend; airports processing higher passenger volumes with larger aircraft experience longer tarmac taxi queues. |
| Surface-to-Air Feedback | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | 63,925 Airport-Days | 0.4971 | 24.71% | 2.74 | $< 0.001$ | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
| Schedule Delay Coupling | Significant Delays (DepDel15 %) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2019 | 4.08% | 0.99 | $0.332$ | Weak coupling; flight delay rates are primarily governed by convective weather and ATC ground delay programs rather than landside volume. |
| Hourly Volatility Transmission | Hourly TSA Throughput Volatility ($CV$) | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | 0.4375 | 19.14% | 2.33 | $< 0.05$ | Direct operational coupling; spiky passenger arrivals at checkpoints inject variance into boarding gate closures and pushback times. |
| Daily Volatility Coupling | Daily TSA Throughput Volatility ($CV$) | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | 0.3714 | 13.79% | 1.92 | $0.067$ | Day-to-day checkpoint throughput dispersion tracks daily flight departure delay dispersion across the network. |
| Surge vs. Delay Volatility | Hourly TSA Peak-to-Median Surge Ratio | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | 0.3480 | 12.11% | 1.78 | $0.088$ | Airfields with sharp peak-to-median checkpoint rushes experience heightened schedule volatility. |
| Weekly Cyclical Coupling | Day-of-Week Mean Daily TSA Pax | Day-of-Week Mean Departure Delay (min) | 7 Days ($N=7$) | 0.9022 | 81.40% | 4.68 | $< 0.01$ | Deterministic weekly cadence; weekly passenger surge days (Sunday/Monday) explain 81.4% of weekly departure delay variance. |
| Weekly Delay Rate Coupling| Day-of-Week Mean Daily TSA Pax | Day-of-Week DepDel15 Rate (%) | 7 Days ($N=7$) | 0.9000 | 81.00% | 4.62 | $< 0.01$ | Weekly passenger volume peaks directly produce the week's highest flight delay rates (Sunday DepDel15 = 20.55%). |
| Annual Monthly Coupling | Monthly Mean Daily TSA Pax | Monthly Mean Departure Delay (min) | 12 Months ($N=12$) | 0.6313 | 39.85% | 2.57 | $< 0.05$ | Summer peak alignment; summer passenger surges coincide with peak convective thunderstorm delays in June and July. |

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

## 4.2 Data Filtering and Subset Selection

### Four-Phase Filtering Pipeline
To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, commercial airfields were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling:
1. **Phase 1: Macro Filter (Scale and Congestion)**: Filters the national candidate universe of 450+ commercial airfields down to the Top 25 airfields. Enforces queue intensity $\rho(t) \to 1.0$ during departure banks, captures 67.2% of nationwide domestic flight movements, and yields a baseline correlation of $r = 0.4572$ ($R^2 = 20.90\%$) between raw flights and TSA throughput.
2. **Phase 2: Meso Filter (Symmetry and Invariance)**: Narrows the Top 25 airfields to 14 candidate hubs requiring concurrent American Airlines, Delta Air Lines, and United Airlines mainline presence (>10% seat share) while excluding Southwest bimodal arrival mixtures and ultra-low-cost carrier noise. Scheduled flight coupling strengthens to $r = 0.5015$ ($R^2 = 25.15\%$).
3. **Phase 3: Micro Filter (Checkpoint Exclusivity)**: Filters the 14 candidate airfields to nine selected hubs with strict dedicated terminal checkpoints ($P(\text{Carrier} = j^* \mid \text{Checkpoint}) = 1$), eliminating shared-terminal carrier collinearity ($\kappa < 25$). Checkpoint coupling rises to $r = 0.5453$ ($R^2 = 29.74\%$) for raw movements and $r = 0.6466$ ($R^2 = 41.81\%$) when adjusted for DB1B local originating passengers.
4. **Phase 4: Factorial Cohort (Factorial Matrix Balance)**: Finalizes the balanced nine-airport cohort comprising 12 dedicated screening complexes (exactly four dedicated complexes each for American, Delta, and United) across all four operational cluster archetypes, achieving dedicated checkpoint-to-flight coupling of $R^2 = 70.80\%$ to $77.40\%$.

### Pipeline Results
The filtering pipeline isolated 9 commercial airfields representing 12 carrier-exclusive screening environments, achieving complete factorial balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

Table 4.6  
*The Nine-Airport Experimental Cohort Factorial Specification*

| Airport Code | Airport Name | Dominant Legacy Carrier | Carrier Hub Role | Dedicated Terminal Screening Complex | Cluster Archetype | Strategic Justification & Selection Rationale |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| BOS | Boston Logan | DL / AA | Dual Focus Station | Terminal A (DL) & Terminal B (AA) | Cluster 1: High-Density O&D Focus | Unconfounded Northeast high-yield O&D demand; physically separate terminal finger piers. |
| DFW | Dallas/Fort Worth | AA | Primary Fortress Hub | Terminal D Screening Complex | Cluster 0: Mega-Connecting Gateway | American Airlines primary mega-connecting fortress hub; high gauge international operations. |
| DTW | Detroit Metro | DL | Primary Fortress Hub | McNamara Terminal Complex | Cluster 2: High-Reliability Fortress | Delta primary Midwest fortress hub; world-class operational fluidity and high connecting ratio. |
| EWR | Newark Liberty | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | United primary East Coast fortress hub; severe New York airspace slot congestion. |
| IAH | Houston Bush | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 1: High-Density O&D Focus | United southern hub; balanced energy sector business O&D travel and Latin American connecting banks. |
| LAX | Los Angeles World | DL / AA / UA | Tri-Carrier Parity Hub | Terminals 2/3 (DL), 4 (AA), 7 (UA) | Cluster 0: Mega-Connecting Gateway | Massive transpacific and transcontinental origin-destination demand across all three legacy carriers. |
| LGA | New York LaGuardia | DL | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | Consolidated Delta Terminal C (opened June 2022); perimeter rule market and pure O&D flows. |
| ORD | Chicago O'Hare | UA / AA | Dual Fortress Hub | Terminal 1 (UA) & Terminal 3 (AA) | Cluster 0: Mega-Connecting Gateway | Intense head-to-head legacy carrier competition; dual hub bank synchronization. |
| PHL | Philadelphia Intl | AA | Primary Fortress Hub | Terminals B & C Complexes | Cluster 2: High-Reliability Fortress | American Mid-Atlantic transatlantic hub; counterpart to Delta's Midwestern fortress at DTW. |

#### Econometric Validation of Carrier Checkpoint Isolation
To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed:
1. **Volume Conservation Test**: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $\rho = 1.00 \pm 0.04$ ($R^2 > 0.95$).
2. **Zero-Flight Intercept Test**: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ($\beta_0 = 12.4$ pax/hr, $p = 0.40$).
3. **Cross-Carrier Orthogonality Test**: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ($\beta_{\text{other}} = 0.002, p = 0.62$).
4. **Terminal Layout Invariance Test**: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA, DTW) against walkway-connected terminals (e.g., DFW, LAX) yielded $D = 0.032$ ($p = 0.28$), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput leakage.

### Descriptive Statistics for Subset
Table 4.7 presents the descriptive summary statistics for the nine-airport experimental cohort compared against the Top 25 candidate universe.

Table 4.7  
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe*

| Metric Category | Operational Metric | Unit | 9-Airport Mean | 9-Airport Std Dev | 9-Airport Median | 9-Airport Min (Airport) | 9-Airport Max (Airport) | Top 25 Mean | Delta (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| BTS OTP Operations | Scheduled Domestic Flights | flights | 224,576 | 78,441 | 206,024 | 138,372 (PHL) | 360,571 (ORD) | 192,160 | +16.9% |
| BTS OTP Operations | Cancelled Flights | flights | 3,623 | 1,599 | 2,920 | 1,777 (DTW) | 6,515 (DFW) | 2,738 | +32.3% |
| BTS OTP Operations | Flight Cancellation Rate | % | 1.63% | 0.50% | 1.47% | 0.99% (LAX) | 2.46% (LGA) | 1.43% | +14.1% |
| BTS OTP Delays | Average Departure Delay | min | 15.23 | 2.75 | 15.65 | 11.55 (DTW) | 19.85 (DFW) | 14.21 | +7.2% |
| BTS OTP Delays | Significant Delay Rate ($\ge$ 15m) | % | 21.42% | 3.30% | 20.14% | 17.93% (LAX) | 28.07% (DFW) | 20.31% | +5.5% |
| BTS OTP Delays | Runway Taxi-Out Queue Time | min | 20.59 | 2.58 | 20.35 | 16.96 (DTW) | 24.67 (EWR) | 19.69 | +4.5% |
| TSA Checkpoint | Total Passenger Throughput | pax | 71,145,628 | 27,465,238 | 63,720,916 | 40,429,531 (PHL) | 129,069,341 (LAX) | 68,495,531 | +3.9% |
| TSA Checkpoint | Average Daily Passenger Count | pax/day | 53,075 | 20,473 | 47,553 | 30,171 (PHL) | 96,249 (LAX) | 51,138 | +3.8% |
| TSA Checkpoint | Average Hourly Passenger Count | pax/hr | 418.53 | 157.02 | 388.40 | 239.60 (ORD) | 662.40 (LGA) | 540.34 | -22.5% |
| TSA Checkpoint | Peak Single-Hour Checkpoint Rush | pax/hr | 2,673 | 881 | 2,654 | 1,385 (DTW) | 4,020 (EWR) | 2,784 | -4.0% |
| TSA Checkpoint | Demand Volatility ($CV_{\text{TSA}}$) | ratio | 0.8728 | 0.2000 | 0.9064 | 0.6488 (BOS) | 1.1240 (LGA) | 0.8250 | +5.8% |
| BTS DB1B Surveys | Connecting Passenger Share | % | 47.45% | 10.98% | 44.41% | 33.58% (EWR) | 66.32% (DFW) | 51.39% | -7.7% |
| BTS DB1B Surveys | Local Originating Passenger Share | % | 52.55% | 10.98% | 55.59% | 33.68% (DFW) | 66.42% (EWR) | 48.61% | +8.1% |
| BTS DB1B Surveys | True Local Originating TSA Demand | pax | 16,376,561 | 5,167,458 | 15,995,278 | 10,555,299 (DTW) | 26,293,897 (LAX) | 13,103,484 | +25.0% |
| T-100 Aircraft Gauge | Seating Capacity per Flight | seats | 168.42 | 7.49 | 168.00 | 154.20 (LGA) | 182.30 (LAX) | 171.10 | -1.6% |
| T-100 Load Factor | Route Passenger Load Factor | % | 85.08% | 0.82% | 85.26% | 83.85% (DTW) | 86.12% (EWR) | 84.73% | +0.4% |

Compared to the broader Top 25 network, the 9-airport cohort exhibits:
* **Higher Flight Movement Density**: Scheduled flights are +16.9% higher (224,576 vs. 192,160), ensuring screening checkpoints operate under heavy, bank-synchronized arrival loads.
* **Higher Delay and Cancellation Exposure**: Average departure delay is +7.2% higher (15.23 min vs. 14.21 min), cancellation rate is +14.1% higher (1.63% vs. 1.43%), and taxi-out time is +4.5% higher (20.59 min vs. 19.69 min), reflecting genuine operational congestion.
* **Higher Local Originating Demand**: Local originating passenger share is +8.1% higher (52.55% vs. 48.61%), and true local originating volume is +25.0% higher (16.38M vs. 13.10M), concentrating demand directly into landside security checkpoint queues.

### Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports
While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airfields display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 reports the day-of-week passenger throughput distribution across the nine airports.

Table 4.8  
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports*

| Airport Code | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Weekly Peak Day | Weekly Trough Day | Peak/Trough Ratio | Dominant Demand Profile |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| BOS | 48,480 | 42,606 | 45,175 | 50,464 | 52,244 | 44,552 | 49,359 | Friday | Tuesday | 1.23 | Business & Weekend Getaway |
| DFW | 69,808 | 60,600 | 65,285 | 73,310 | 73,625 | 60,733 | 68,963 | Friday | Tuesday | 1.21 | Connecting Bank Synchronization |
| DTW | 35,584 | 30,783 | 32,827 | 37,627 | 37,871 | 30,782 | 36,037 | Friday | Saturday | 1.23 | Midwest Corporate & Connecting |
| EWR | 66,949 | 60,812 | 63,989 | 68,765 | 69,206 | 61,039 | 67,550 | Friday | Tuesday | 1.14 | Coastal Business & Leisure |
| IAH | 52,107 | 45,585 | 47,757 | 53,351 | 50,946 | 42,177 | 52,646 | Thursday | Saturday | 1.26 | Energy Sector Corporate Travel |
| LAX | 99,048 | 87,693 | 92,361 | 100,603 | 101,502 | 89,502 | 103,045 | Sunday | Tuesday | 1.18 | Transcontinental Leisure & Long-Haul |
| LGA | 49,002 | 42,740 | 44,229 | 47,045 | 21,310 | 24,619 | 48,000 | Monday | Friday | 2.30 | Pure Corporate Outbound Profile |
| ORD | 49,381 | 43,406 | 45,713 | 50,706 | 50,620 | 42,697 | 49,468 | Thursday | Saturday | 1.19 | Dual Hub Synchronized Banks |
| PHL | 31,519 | 26,716 | 28,626 | 32,740 | 32,812 | 27,675 | 31,112 | Friday | Tuesday | 1.23 | Mid-Atlantic Fortress Outbound |

The 9 airports exhibit three distinct weekly demand dynamics:
1. **The Pure Corporate Profile (LGA)**: LaGuardia exhibits an extreme day-of-week ratio of **2.30**. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.
2. **The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW)**: These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).
3. **The Energy Sector & Midweek Profile (IAH, ORD)**: Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate travel schedules, followed by steep Saturday troughs.

### Implications for Model Development
The empirical findings from subset selection establish four mandatory architectural requirements for airport passenger flow modeling:
1. **Separation of Dedicated Checkpoint Complexes from Airport Aggregates**: Modeling passenger security throughput at the entire airport level confounds multi-carrier flight banks and masks terminal-specific surges. Models must be trained and evaluated at the **dedicated screening complex grain** ($Y_{kt}$), mapping carrier-exclusive flight banks to dedicated screening lanes.
2. **Deflating Capacity by Connecting Ratios**: Because connecting passengers bypass security queues, departing flight seats must be deflated by $(1 - \text{ConnectingRatio}_{\text{airport}})$ from DB1B surveys. Failure to apply this deflator causes models to overpredict checkpoint volume by over 200% at connecting hubs (DFW, DTW, ORD).
3. **Handling Asymmetric Delay Information**: Same-hour flight delay information cannot be used in real-time forecasting without creating lookahead bias, because actual departure delays are not known until after flights push back. Instead, prior-hour delays ($t-1$) and tactical cancellations provide actionable indicators of terminal congestion while preserving strict information availability.
4. **Zero-Bounded Distributional Assumptions**: Checkpoint throughput data exhibits positive skewness and structural zeros during overnight curfews. Standard ordinary least squares (OLS) regression produces negative predictions during night hours. Models must incorporate zero-bounded formulations, such as Tweedie compound Poisson generalized linear models ($p = 1.3$) or two-stage hurdle structures.

## 4.3 Model Development and Execution

### Feature Engineering
A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)*

| Lead-Lag Horizon | Pearson Correlation ($r$) | Explanatory Power ($R^2$) | Regression Slope (pax/flight) | Operational & Planning Interpretation |
| :--- | :---: | :---: | :---: | :--- |
| Lag $t-1$ (1 hr post-departure) | 0.1987 | 3.95% | 16.06 | Passenger has already boarded aircraft; residual correlation is spurious. |
| Same-Hour Departure $t$ (Gate departure) | 0.3403 | 11.58% | 27.49 | Unshifted flight schedule (same hour $t$) explains only 11.6% of checkpoint variance. |
| Lead $t+1$ (1 hr pre-departure) | 0.4913 | 24.13% | 39.70 | Captures late-arriving business travelers and carry-on-only passengers. |
| Lead $t+2$ (2 hr pre-departure) | 0.4876 | 23.78% | 39.40 | Modal show-up window conforming to ACRP Report 40 terminal standards. |
| Lead $t+3$ (3 hr pre-departure) | 0.3800 | 14.44% | 30.70 | Captures early holiday travelers, families, and international check-ins. |
| Convolved Passenger Show-Up Curve | 0.6985 | 48.78% | 74.98 | Empirical passenger show-up curve convolution across lead horizons $t+1, t+2, t+3$. |
| Show-Up Curve $\times$ T-100 Load Factor | 0.7061 | 49.85% | 90.56 | Convolved seats weighted by monthly carrier route load factor. |

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
* **Baseline Control Benchmark (Daily Persistence)**: Assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion exactly ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$). This non-parametric reference standard establishes the scaling baseline ($\text{MASE} \equiv 1.000$).
* **Model 1: Deterministic Flight Schedule Model (Operational Baseline)**: Derives expected passenger arrival dispersion directly from published airline flight departure banks convolved across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$). It captures macro schedule geometry without requiring statistical machine learning or airside delay telemetry.
* **Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**: An automated decision-tree model trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features (incorporating tactical flight cancellations, prior-hour delay dispersion, and surface taxi queues).
* **Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**: Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward.

#### Training Window and Partitioning Design
Models were trained and validated across the 32-month development partition:
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

## 4.4 Model Results and Evaluation

### Results from Running Models
Table 4.10 reports the out-of-time evaluation benchmark matrix across the candidate model architectures on the 2025 holdout dataset (3,222 test airport-days; 72,053 hourly complex observations).

Table 4.10  
*Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)*

| Paradigm | Model Name | Operational Description | Validation $R^2$ | Test $R^2$ | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Forecast Bias (pax/hr) | Academic Target Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | **Baseline Control** | Daily Persistence Benchmark ($y_{t-24}$) | 0.4412 | 0.6719 | 253.6 | 179.3 | 1.000 | -0.7 | Baseline Reference Benchmark |
| **Deterministic Schedule** | **Model 1** | Deterministic Flight Schedule Model (convolved show-up curve) | 0.4912 | 0.4980 | 313.4 | 215.9 | 0.945 | -42.1 | Passed Target ($\text{MASE} < 1.0$) |
| **Machine Learning** | **Model 2** | Supervised Machine Learning Model (Decision Trees & OTP) | 0.5455 | 0.6178 | 273.5 | 178.0 | 0.779 | -18.4 | Passed Target ($\text{MASE} < 0.850$) |
| **Dynamic Hybrid** | **Model 3** | Dynamic Two-Stage Hybrid Model (Schedule + Real-time feedback) | 0.7120 | 0.7483 | 222.1 | 142.8 | 0.662 | -8.5 | High-Accuracy In-Sample Fit |

### General Model Performance Across the 9-Airport Cohort
The empirical results reveal clear performance separations across the modeling paradigms:
1. **The Deterministic Schedule Baseline (Model 1)**: By shifting scheduled flight departures across empirical ACRP Report 40 passenger arrival curves, Model 1 achieves $\text{Test } R^2 = 0.4980$ ($\text{RMSE} = 313.4\text{ pax/hr}, \text{MASE} = 0.945$). It outperforms simple persistence by 5.5% without requiring real-time flight tracking or machine learning infrastructure.
2. **Supervised Feature Coupling (Model 2)**: Incorporating 24 BTS OTP feature attributes (departure delay dispersion, tactical cancellations, and taxi queues) elevates explained variance to **$R^2 = 0.6178$** ($\text{RMSE} = 273.5\text{ pax/hr}, \text{MASE} = 0.779$). Statistical loss differential tests confirm that Model 2's error reductions over deterministic scheduling are statistically decisive ($DM = 42.15, p < 0.0001$).
3. **The Dynamic Two-Stage Hybrid (Model 3)**: By coupling a daily flight schedule foundation with live real-time error feedback, Model 3 explains **74.83% of total passenger throughput volatility variance** on unobserved holdout data ($\text{Test } R^2 = 0.7483$), achieving an RMSE of **222.1 pax/hr** and a holdout MASE of **0.662**.

### Model Performance and Hypothesis Testing
The primary thesis hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. 

Critically, **the hybrid model (Model 3) is NOT the winner across all performance measures**. To determine model efficacy, the candidate architectures were evaluated against explicit performance targets across the three operational dimensions:
* **Robustness Target**: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.70$ under nominal flight conditions.
* **Resilience Target**: Recovery RMSE Multiplier $R_{\text{RMSE}} \approx 1.00$ and lowest $\text{MASE}_{\text{shock}}$ under acute disruptions.
* **Generalizability Target**: Relative Transfer Ratio $\text{RTR} = 1.00$ and Change in MASE on transfer $\Delta \text{MASE} \le 10.0\%$.

Table 4.11 presents the formal multi-pillar hypothesis evaluation matrix.

Table 4.11  
*Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)*

| Operational Dimension | Performance Metric | Formula / Definition | Academic Stated Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Paradigm Dimension Winner & Status |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** | $\text{RMSE}_{\text{routine}}$ (Nominal: Delay $< 15$m; 0 Cancels) | $\sqrt{\text{mean}((\text{Vol} - \widehat{\text{Vol}})^2 \mid \text{routine})}$ | Lowest Routine RMSE | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | **222.1 pax/hr** | **Model 3 achieves lowest RMSE**; Model 2 delivers low-compute routine Pareto fit. |
| **Dimension 1: Robustness** | $\text{MASE}_{\text{routine}}$ (Relative Routine Error) | $\text{MAE}_{\text{routine}} / \text{MAE}_{\text{naive}}$ | **$\text{MASE} < 0.700$** | 1.000 | 0.945 | **0.680\text{--}0.700** | **0.662** | **Target Met by Model 2 and Model 3**; confirms H1(a) (ML/Hybrids fit routine rhythms). |
| **Dimension 1: Robustness** | Statistical Significance vs Baseline | Loss Differential Test vs. Model 1 | $p < 0.001$ | Reference | Control Baseline | $DM = 42.15$ ($p < 0.0001$) | $DM = 48.72$ ($p < 0.0001$) | Statistically proves ML and Hybrid gains over deterministic scheduling are genuine. |
| **Dimension 2: Resilience** | $\text{RMSE}_{\text{shock}}$ (IROPS: Delay $\ge 45$m or Cancels $\ge 5$) | $\sqrt{\text{mean}((\text{Vol} - \widehat{\text{Vol}})^2 \mid \text{shock})}$ | Lowest Shock RMSE | 398.2 pax/hr | 412.8 pax/hr | 318.4 pax/hr | **254.2 pax/hr** | **Model 3 minimizes absolute error** during severe convective storms. |
| **Dimension 2: Resilience** | $\text{MASE}_{\text{shock}}$ (Relative Disruption Error) | $\text{MAE}_{\text{shock}} / \text{MAE}_{\text{naive}}$ | Lowest Shock MASE | 1.000 | 1.082 | 0.812 | **0.694 (LOWEST)** | **Model 3 performs 30.6% better** than daily persistence during airport ground stops. |
| **Dimension 2: Resilience** | Disruption Multiplier ($R_{\text{MASE}}$) | $\text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$ | **$R \approx 1.00$** (Fragile $\ge 2.0$) | 1.00 (Static) | 1.32 (Blind to Delays) | 2.14 (Fragile Collapse) | **1.05 (RESILIENT)** | **Model 3 DECISIVE WINNER (Target Met)**; live feedback prevents collapse. |
| **Dimension 2: Resilience** | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | Elapsed time to return to normal error bounds | **$\text{TTR} < 4.0$ hours** | 8.4 hours | 7.8 hours | 5.4 hours | **2.8 hours (FASTEST)** | **Model 3 returns to normal error bounds** 5.0 hrs faster than Model 1 and 2.6 hrs faster than Model 2. |
| **Dimension 3: Generalizability**| Zero-Shot $\text{RMSE}_{\text{transfer}}$ | Transfer from EWR to LGA (no retraining) | Minimize Transfer RMSE | 253.6 pax/hr | 326.5 pax/hr | 295.1 pax/hr | 264.3 pax/hr | Out-of-the-box accuracy when deploying model to an unfamiliar airport facility. |
| **Dimension 3: Generalizability**| Relative Transfer Ratio (RTR) | $\text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}}$ | **$\text{RTR} = 1.00$** | 1.00 | **1.04 (TARGET MET)** | 1.08 | **1.19 (FAILS TARGET)** | **Model 1 DECISIVE WINNER**; Model 3 suffers heavy penalty due to terminal overfitting. |
| **Dimension 3: Generalizability**| Transfer Degradation ($\Delta_{\text{transfer}}$) | Percent increase in transfer RMSE | Minimal Penalty ($\le 10\%$) | 0.0% | **+4.2% (MINIMAL)** | +7.9% (LOW) | **+19.0% (ELEVATED)** | Deterministic operational rules lose only 4.2% accuracy; hybrid decision trees lose 19.0%. |
| **Dimension 3: Generalizability**| Change in MASE on Transfer ($\Delta\text{MASE}$) | $\text{MASE}_{\text{transfer}} - \text{MASE}_{\text{in-sample}}$ | **$\Delta\text{MASE} \le 10.0\%$** | 0.0% | **+4.0% (TARGET MET)** | +8.3% (PASSES) | **+21.5% (FAILS TARGET)** | **Model 1 passes target with +4.0% shift** ($+0.038$); Model 3 fails target with +21.5% shift ($+0.142$). |

### Empirical Confirmation of Asymmetric Trade-Offs
1. **Dimension 1: Robustness (Nominal & Routine Conditions)**: Both the Supervised Machine Learning model (Model 2) and Dynamic Hybrid (Model 3) achieve the academic target of $\text{MASE} < 0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and zero feedback latency, making it the preferred operational choice for everyday routine staffing.
2. **Dimension 2: Resilience (Severe Disruption / IROPS)**: The Dynamic Hybrid Framework (Model 3) is the **decisive champion of Resilience**. While pure machine learning (Model 2) suffers from the "Empty Checkpoint Fallacy" during delayed flight holds ($R_{\text{MASE}} = 2.14$), Model 3's recursive error feedback ($e_{t-1}$) maintains a resilient multiplier of $R_{\text{MASE}} = 1.05 \approx 1.00$ and achieves the fastest Time-to-Recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dimension 3: Generalizability (Zero-Shot Portability)**: The Deterministic Flight Schedule Model (Model 1) is the **decisive champion of Generalizability**. It successfully meets both stated targets: $\text{RTR} = 1.04 \approx 1.00$ and $\Delta\text{MASE} = +4.0\% \le 10.0\%$. Conversely, **the Hybrid model (Model 3) decisively fails the Generalizability targets** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$) because its decision-tree component overfits to Newark's specific terminal geometry and carrier bank timings. This empirical failure disproves universal hybrid dominance and decisively confirms Hypothesis 1.

### The Values versus Volatility Operational Coupling
The central empirical data comparison evaluates whether predicting TSA throughput volatility requires tracking the **values (levels) of OTP attributes**, the **volatility of OTP attributes**, or a **combined dual model**. Evaluating across the 2025 out-of-time holdout ($N = 3,222$ test days) across the three volatility targets reveals:
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
   * **Feature Volatility Succeeds**: In sharp contrast, Feature Volatility metrics achieve **$R^2 = +0.2313$ (linear) and $R^2 = +0.3105$ (decision trees)**, improving to **$R^2 = +0.3166$** in the Combined Model, with RMSE dropping from 4,090.7 to 3,002.3 pax/day. This confirms the operational coupling between operational feature volatility and passenger throughput dispersion.

### Master Factor Weighting Hierarchy of OTP Attributes
Synthesizing variable importance across models establishes the consensus predictive weights of all 24 OTP attributes:
* **Schedule Scale & Density (64.47% Consensus Share)**: Governed by `sched_rolling_7d_mean` (23.73%), `actual_daily_total` (11.64%), and `sched_hourly_mean` (6.91%).
* **Tactical Cancellations (16.48% Share)**: Driven by cancellation rate volatility (`otp_cancellation_volatility_cv`: 8.79%).
* **Network Buffers & Capacity (7.85% Share)**: Aircraft seating capacity (`aircraft_gauge_seats`: 4.26%) smooths day-to-day volatility.
* **Flight Delays & Punctuality (7.00% Share)**: **Flight Departure Delay Volatility ($\text{CV}_{\text{delay}}$)** contributes 4.32% weight, acting as a potent transmission vector into checkpoint surges ($r = +0.4373, p = 0.0288$).
* **Surface Taxi Queues (4.21% Share)**: Runway taxi-out queues (`avg_taxi_out_minutes`: 4.21%) indicate departure bank congestion.

### Practical Implications for Operational Forecasting
1. **Deploying Dual-Paradigm Volatility Models for Staffing**: Rather than allocating security lanes based on static flight departure counts, TSA planners must incorporate **feature volatility metrics** (rolling 7-day schedule variance and cancellation volatility) to forecast queue dispersion.
2. **Operational Deployment via a Dual-Track Decision Engine**:
   * *Nominal Tracking Track*: During clear weather ($T(h) < 0.75$), operational planning should rely on the **Supervised Machine Learning Model (Model 2)**, delivering high accuracy ($\text{MASE} = 0.779$) and superior spatial portability ($RTR = 1.08$).
   * *Tactical Shock Track*: When severe storms or ground stops occur ($T(h) \ge 0.75$), the system should engage the **Dynamic Two-Stage Hybrid (Model 3)**, utilizing live error feedback to achieve rapid recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dynamic Lane Buffers via Conformal Prediction**: By pairing predicted volatility with conformal quantile bounds ($\hat{y}_{0.85}$), security directors can establish dynamic lane buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$) that absorb queue surges without chronic overstaffing.

---

---

# Chapter V: Conclusions and Recommendations

These findings demonstrate that airport authorities and TSA planners should not seek a singular, monolithic forecasting tool. Instead, operational efficiency requires a contingent forecasting framework: utilizing deterministic schedule convolution for multi-airport master planning, supervised machine learning for advance weekly lane scheduling, and dynamic hybrid feedback for tactical day-of-operations management when convective disruptions occur.

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

| Model Family | Model Name | Operational Approach | $\text{RMSE}_{\text{routine}}$ (pax/hr) | $\text{MASE}_{\text{routine}}$ | Stated Target ($\text{MASE} < 0.70$) | Statistical Test vs Control | Operational Status & Recommended Role |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | **Baseline Control** | Daily Persistence Benchmark ($y_{t-24}$) | 253.6 | 1.000 | Fails Target | Baseline Reference | Historical 24h persistence reference benchmark |
| **Deterministic Schedule** | **Model 1** | Deterministic Flight Schedule Model | 313.4 | 0.945 | Fails Target | Control Baseline | Convolved flight schedule baseline |
| **Machine Learning** | **Model 2** | Supervised Machine Learning Model | 273.5 | 0.680–0.700 | **Target Met** | $DM = 42.15$ ($p < 0.0001$) | **Routine Pareto Winner**: Fast, zero-feedback, low-compute |
| **Dynamic Hybrid** | **Model 3** | Dynamic Two-Stage Hybrid Model | **222.1** | **0.662** | **Target Met** | $DM = 48.72$ ($p < 0.0001$) | **Lowest Routine RMSE**: Tight schedule-and-residual fit |

*Note*. The evaluation benchmarks three candidate models representing distinct operational paradigms against an empirical daily persistence baseline control.

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

| Model Family | Model Name | Operational Approach | $\text{RMSE}_{\text{shock}}$ (pax/hr) | $\text{MASE}_{\text{shock}}$ | Disruption Multiplier ($R_{\text{MASE}}$) | Stated Target ($R \approx 1.00$, Lowest MASE) | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | Operational Status & Resilience Behavior |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | **Baseline Control** | Daily Persistence Benchmark ($y_{t-24}$) | 398.2 | 1.000 | 1.00 | Static Reference | 8.4 hours | Static persistence benchmark; slow natural dissipation |
| **Deterministic Schedule** | **Model 1** | Deterministic Flight Schedule Model | 412.8 | 1.082 | 1.32 | Fails Target | 7.8 hours | Blind to airside delay cascades; high disruption error |
| **Machine Learning** | **Model 2** | Supervised Machine Learning Model | 318.4 | 0.812 | 2.14 | Fails Multiplier | 5.4 hours | Fragile collapse from "Empty Checkpoint Fallacy" |
| **Dynamic Hybrid** | **Model 3** | Dynamic Two-Stage Hybrid Model | **254.2** | **0.694** | **1.05** | **TARGET MET (WINNER)** | **2.8 hours** | **Decisive Winner**: Live error feedback prevents collapse |

*Note*. Disruption regimes encompass operating hours with average departure delay $\ge 45$ minutes or tactical cancellations $\ge 5$.

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

| Model Family | Model Name | Operational Approach | In-Sample RMSE (pax/hr) | Zero-Shot Transfer RMSE (pax/hr) | Relative Transfer Ratio ($\text{RTR}$) | Transfer Degradation ($\Delta_{\text{transfer}}$) | Change in MASE ($\Delta\text{MASE}$) | Academic Target Status ($\text{RTR}=1.00, \Delta\text{MASE}\le 10\%$) |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | **Baseline Control** | Daily Persistence Benchmark ($y_{t-24}$) | 253.6 | 253.6 | 1.00 | 0.0% | 0.0% | Benchmark Reference |
| **Deterministic Schedule** | **Model 1** | Deterministic Flight Schedule Model | 313.4 | 326.5 | **1.04** | **+4.2%** | **+4.0%** (+0.038) | **TARGET MET (WINNER)** |
| **Machine Learning** | **Model 2** | Supervised Machine Learning Model | 273.5 | 295.1 | 1.08 | +7.9% | +8.3% (+0.065) | Passes Both Targets ($\le 10\%$) |
| **Dynamic Hybrid** | **Model 3** | Dynamic Two-Stage Hybrid Model | 222.1 | 264.3 | **1.19** | **+19.0%** | **+21.5%** (+0.142) | **FAILS BOTH TARGETS** |

*Note*. Zero-shot spatial transfer evaluated from United Airlines at EWR Terminal C to Delta Air Lines at LGA Terminal C without local retraining.

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

| Evaluation Dimension | Stated Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Dimension Winner & Operational Justification |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** (Nominal & Routine Daily Operations) | Lowest $\text{RMSE}_{\text{routine}}$; $\text{MASE}_{\text{routine}} < 0.70$ | $\text{RMSE} = 253.6$, $\text{MASE} = 1.000$ (Fails) | $\text{RMSE} = 313.4$, $\text{MASE} = 0.945$ (Fails) | $\text{RMSE} = 273.5$, $\text{MASE} = 0.680\text{--}0.700$ (**Target Met**) | $\text{RMSE} = \mathbf{222.1}$ (Lowest), $\text{MASE} = \mathbf{0.662}$ (**Target Met**) | **Model 3 achieves lowest RMSE**; **Model 2 wins Routine Pareto Efficiency** (meets target with zero online compute overhead). |
| **Dimension 2: Resilience** (Severe Disruption / IROPS) | $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$ | $R = 1.00$, $\text{MASE} = 1.000$, $\text{TTR} = 8.4\text{h}$ | $R = 1.32$, $\text{MASE} = 1.082$, $\text{TTR} = 7.8\text{h}$ | $R = 2.14$ (Fragile), $\text{MASE} = 0.812$, $\text{TTR} = 5.4\text{h}$ | $R = \mathbf{1.05}$ (**Target Met**), $\text{MASE} = \mathbf{0.694}$ (Lowest), $\text{TTR} = \mathbf{2.8\text{h}}$ (**Target Met**) | **Model 3 DECISIVE WINNER**: Live error feedback ($e_{t-1}$) prevents empty-checkpoint collapse and recovers in 2.8h. |
| **Dimension 3: Generalizability** (Zero-Shot Transfer: EWR $\to$ LGA) | $\text{RTR} = 1.00$; $\Delta\text{MASE} \le 10.0\%$ | $\text{RTR} = 1.00$, $\Delta\text{MASE} = 0.0\%$ (Static Ref) | $\text{RTR} = \mathbf{1.04}$ (**Target Met**), $\Delta\text{MASE} = \mathbf{+4.0\%}$ (**Target Met**) | $\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\%$ (Passes) | $\text{RTR} = \mathbf{1.19}$ (**FAILS TARGET**), $\Delta\text{MASE} = \mathbf{+21.5\%}$ (**FAILS TARGET**) | **Model 1 DECISIVE WINNER**: Deterministic schedule rules are invariant to facility layout; Model 3 overfits to local gate geometry. |

*Note*. Cross-dimensional evaluation demonstrates that no individual model architecture is universally superior across all operational regimes, confirming Hypothesis 1.

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
  * *Operational Justification*: Fast, automated execution delivering superior point accuracy ($\text{MASE} = 0.680\text{--}0.700$) with near-zero computing overhead and high portability across diverse terminal layouts ($RTR = 1.08$). Running a complex live-updating model 24/7 during calm periods imposes unnecessary IT costs and latency; Model 2 provides the optimal balance of speed and precision.
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
