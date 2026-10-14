# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
**Author:** Leila Gleich | **Institution:** Embry-Riddle Aeronautical University
**Degree:** Master of Science in Aeronautics / Aviation Data Analytics
**Document Edition:** Thesisv2 Audited & Certified Final Master Text (APA 7th Edition)
**Date:** October 2026

---

AN EVALUATION OF PERFORMANCE MEASURES FOR PREDICTIVE APPROACHES TO MODEL TSA THROUGHPUT VOLATILITY

by

Leila Gleich

A Graduate Capstone Project Submitted to the College of Aviation,

Department of Aeronautics, in Partial Fulfillment

of the Requirements for the Degree of

Master of Science in Aeronautics

Embry-Riddle Aeronautical University

Worldwide Campus

October 2026

AN EVALUATION OF PERFORMANCE MEASURES FOR PREDICTIVE APPROACHES TO MODEL TSA THROUGHPUT VOLATILITY

by

Leila Gleich

This Graduate Capstone Project was prepared under the direction of the candidate’s Graduate Capstone Project Chair, Mark Miller,

Worldwide Campus and has been approved. It was submitted to the

Department of Graduate Studies in partial fulfillment

of the requirements for the degree of

Master of Science in Aeronautics

Graduate Capstone Project:

___________________________________________

Mark Miller

Graduate Capstone Project Chair

________________

Date

# Acknowledgements

I'd like to thank the opportunities I’ve had to understand the extent airport operations can be improved and support both local and global communities.

# Abstract

Scholar:	Leila Gleich

Title:	An Evaluation of Performance Measures for Predictive Approachs to Model TSA Throughput Volatility

Institution:	Embry-Riddle Aeronautical University

Degree:	Master of Science in Aeronautics

Year:	2026

As commercial air travel expands against fixed terminal infrastructure, airport operators and security authorities face severe bottlenecks at passenger screening checkpoints where arrival surges create runaway wait times. Because checkpoint lines escalate rapidly with sudden bursts in passenger arrivals rather than steady passenger volume, forecasting the volatility of screening throughput is essential for operational stability. This research evaluates distinct forecasting paradigms across routine operations, severe flight disruptions, and cross-airport transfer. The findings demonstrate that no individual predictive model is universally superior across every operational environment. Supervised machine learning excels at routine advance staffing schedules, while dynamic hybrid models prove essential during irregular operations to absorb severe flight delays and prevent forecast collapse. Conversely, deterministic schedule baselines prove superior when deploying directly to unfamiliar airport facilities without local retraining because airline schedules remain independent of specific terminal layouts. Ultimately, this study provides airport authorities and federal security directors with an adaptable decision framework that matches the right predictive tool to real-time operating conditions, optimizing checkpoint screening capacity without costly physical expansion.

# Chapter I

# Introduction

As air travel demand outpaces airport infrastructure growth, inefficient resource allocation has become a critical operational bottleneck (Adacher, Flamini, Guaita & Romano, 2017). Barriers such as prohibitive capital costs and municipal land constraints severely restrict physical terminal expansion (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). Consequently, airport operators and federal security authorities must extract maximum operational throughput from fixed physical assets through software-driven predictive intelligence. While existing predictive models are increasingly used to forecast airport passenger flow management, the systemic shocks of the COVID-19 pandemic underscored limitations within traditional, accuracy-centric performance metrics to handle abrupt demand shocks, structural breaks, and changing operating constraints. These unprecedented operational disruptions demonstrated that conventional accuracy metrics, while necessary, are insufficient as the sole basis for evaluating models intended for volatile airport operating environments. The pandemic revealed that a singular evaluation standard is inadequate across highly variable operational contexts, necessitating the assessment of predictive models through a broader, multidimensional set of performance measures. In airport operations, the most useful predictive model is therefore not necessarily the one with the lowest average forecast error, but the one that remains reliable during disruption (robustness), recovers effectively as conditions evolve (resilience), and transfers across operational contexts (generalizability). This study examines the suitability of predictive models – specifically for forecasting TSA throughput – across routine, traditional, and disrupted demand conditions when model performance accuracy is assessed in the context of resilience, robustness, and generalizability.

## Significance of the Study

This research aims to contribute to airport capacity optimization by shifting the paradigm of how predictive models are evaluated under unpredictable airport operations. By analyzing the relationship between flight operations and TSA throughput, it seeks to assess these frameworks across robustness, resilience, and generalizability, for the purpose of providing airport management with strategic flexibility to select tailored forecasting tools.

## Statement of the Problem

Airport passenger arrivals and behaviors are inherently stochastic, varying significantly by time of day, flight schedules, and external factors (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Existing models for managing airport passenger flow tend to rely on static or pre‑pandemic assumptions, often failing to account for unpredictable post‑pandemic travel patterns (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Lee & Yu, 2024). This mismatch between capacity planning and fluctuating passenger demand contributes to bottlenecks at check‑in counters, TSA checkpoints, and boarding gates, leading to congestion and inefficient resource allocation. The pandemic demonstrated that static historical baselines are insufficient for modern operations; without an adaptable and dynamic evaluation methodology, airports risk deploying tools that fail to absorb day-to-day demand fluctuations, respond to sudden operational shocks, or account for unique airport characteristics.

## Purpose Statement

The primary objective is to evaluate predictive modeling techniques, such as regression, machine learning, and queuing simulation, to optimize airport capacity via technological rather than physical, more costly interventions. By analyzing the relationship between flight operations and TSA throughput, this study evaluates various predictive modeling frameworks against the primary criteria of robustness, resilience, and generalizability. Rather than seeking a singular, universally optimal model, this research aims to identify which frameworks perform best under each distinct metric.

## Research Question

Which predictive modeling frameworks – spanning deterministic persistence controls, deterministic schedule baselines, machine learning, and sequential two-stage hybrids – are most effective for forecasting airport passenger security screening throughput volatility when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?

The Asymmetric Trade-Off  : Across the candidate modeling paradigms evaluated, no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability).

(Robustness): Supervised machine learning (Model 2) and two-stage dynamic hybrids (Model 3) will successfully achieve the robustness target under nominal operating conditions, whereas naive persistence (Baseline Control) and deterministic flight schedules (Model 1) will fail this threshold.

(Resilience): The Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience. Static supervised machine learning (Model 2) will experience severe performance degradation, while deterministic baselines (Model 1) will remain blind to downline delay cascades.

(Generalizability): The Deterministic Flight Schedule Model (Model 1) will satisfy the generalizability target without local. Conversely, the Dynamic Hybrid (Model 3) will fail the generalizability target.

Delimitations

This study focuses on U.S. airports and uses post-pandemic TSA throughput and flight performance data from 2019 to 2025. It excludes pre-pandemic and pandemic-period activity except where needed to define the post-pandemic baseline. Dynamic queuing models and simulation-based methods are assessed using standard statistical measures, including p-value, R2 squared, mean squared error (MSE), root mean squared error (RMSE), and mean absolute percentage error (MAPE).

## Limitations and Assumptions

Due to reliance on public data, confidential variables like staffing and manual queue management fall outside the scope of this analysis. While external factors such as weather, regulatory impacts, or IT outages may not be fully accounted for, the framework assumes that utilized data is consistent and findings from the selected airports are generalizable across similar facilities and circumstances. Additionally, the methodology relies on the ability to apply monthly data on load factor to the prediction of TSA throughput on an hourly and seasonal level.

# Chapter II

Review of the Relevant Literature

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure (Federal Aviation Administration [FAA], 2024; International Air Transport Association [IATA], 2026), the prohibitive financial and spatial costs of continuous brick-and-mortar expansion have shifted operational focus toward software-driven, data-informed terminal capacity management (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). To address these gaps, researchers are developing models designed to optimize resource allocation, such as staffing and throughput management, while maintaining efficient, high-quality service. When passenger demand surges surpass processing capacity at security screening, congestion ripples backward into ticketing halls and forward into departure concourses, inducing boarding holds, tarmac delays, and passenger misconnections across the system (Adacher et al., 2017). Historically, airport passenger flow modeling prioritized statistical fit and mean throughput optimization under static operating assumptions. However, the unprecedented systemic shocks of the COVID-19 pandemic and subsequent recovery demonstrated that models calibrated solely on clear-weather historical data fail during operational disruptions (Sun et al., 2022). Integrating advanced predictive frameworks offers the potential to build the robust, resilient, and generalizable tools necessary to manage variability and balance competing operational demands under uncertainty.

To address these vulnerabilities, this literature review traces the evolution of airport passenger flow prediction across five core theoretical domains: (a) traditional approaches and operational complexity; (b) simulation modeling and real-time terminal management; (c) advanced predictive; (d) hybrid predictive architectures; (e) the impact of covid; and (f) multi-dimensional operational evaluation, establishing the theoretical foundations for the evaluation trio – Robustness, Resilience, and Generalizability – that governs this research.

Figure 2.1: Literature Review Outline

Traditional Approaches and Operational Complexity

Commercial airport terminals are complex operational ecosystems where physical infrastructure, traveler behavior, and airline schedules intersect (Birolini & Jacquillat, 2023; Nazir et al., 2022; Zhang et al., 2012). With domestic passenger demand projected to grow by 2.4% annually while physical airport capacity expands by only 0.8%, commercial aviation faces an operational gap that physical construction cannot resolve due to severe financial, spatial, and environmental constraints (Balliauw & Onghena, 2020; FAA, 2024; Fernandes & Pacheco, 2002; IATA, 2026; Lemer, 1988). Consequently, airport research has shifted away from long-term capital expansion toward dynamic landside operational optimization, utilizing computational models to maximize existing terminal footprints (AlKheder et al., 2024; De Neufville & Odoni, 2014; Solak et al., 2009). Historically, terminal planning relied on deterministic formulas assuming that fixed passenger volumes produce predictable, linear service requirements (Parizi & Braaksma, 1994). In operational reality, however, terminal subsystems – specifically check-in halls, security screening checkpoints, and boarding gates – function as highly interdependent, stochastic queuing networks (Araujo & Repolho, 2015). To maintain a target Level of Service (LOS) – the operational benchmark governing acceptable passenger wait times and crowding thresholds – without prohibitive capital investments, terminal operators must actively identify and eliminate transient bottlenecks that restrict passenger throughput (Di Mascio et al., 2020).

The delicate interdependency of airport subsystems further complicates operational shifts, as localized failures in one segment are particularly vulnerable to time-related constraints, potentially triggering a systemic collapse of flow (Orhan & Orhan, 2020; Bießlich et al., 2014; Brown & Madhavan, 2011). Systemic fragility is exacerbated by the interlocking nature of landside and airside events, where a delay in one sector propagates a cascade of congestion across the entire airport ecosystem (Nazir et al., 2022). Furthermore, congestion does not occur linearly; traffic frequently occurs in high concentrations – "starving" capacity for hours before suddenly "saturating" it in minutes – transforming flow optimization into a moving target that outpaces nominal capacity growth (Chiti et al., 2018). Even when a facility remains under its total daily limits, unexpected arrival fluctuations create "ripples" of upstream congestion, inevitably disrupting downstream processes like security screening (Adacher & Flamini, 2020; Marzuoli et al., 2019). This operational friction is intensified by a persistent temporal lag: a systemic mismatch in which the time required to detect a surge forces additional resources to become available only after the peak has subsided. Ultimately, these bottlenecks are rooted in the unpredictable, stochastic nature of passenger behavior, making resource allocation a complex balancing act between operational costs and quality service levels.

Batch Arrival Dynamics and Flight Bank Synchronization

Understanding modern airport capacity and the corresponding resource allocation challenge requires looking beyond the simple reality of demand exceeding supply (Fernandes & Pacheco, 2002). A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, passenger arrivals are characterized by extreme non-linear fluctuations and concentrated "batches" induced by airline flight bank scheduling (Cheng et al., 2012). Modern hub-and-spoke networks intentionally compress 20 to 40 flight departures into synchronized 45-to-90-minute "flight banks" to maximize connecting passenger transfer opportunities (Schultz & Fricke, 2011). When multiple high-capacity aircraft share overlapping departure banks, thousands of ticketed travelers descend on terminal entrances simultaneously, creating non-linear surges that saturate screening lane capacity far more rapidly than smooth arrival streams (Brunetta et al., 1999; Dönmez et al., 2025; Lemer, 1988; Marzuoli et al., 2019). As Peterson et al. (1995) established in their foundational queuing analysis, flight bank synchronization generates transient, non-stationary queuing states where sudden demand bursts produce congestion that persists long after the scheduled bank has departed.

Classical Queuing Theory: Volume Versus Volatility

To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has utilized Queuing Theory (Horie, 1985; Odoni, 1986). Queuing Theory models how stochastic arrival patterns and concentrated "batches" of passengers interact with various service points throughout the terminal (Wang, 2017). In this framework, every terminal process – from check-in to security screening – is treated as a "server" processing "entities." Early iterations of these models applied a Poisson process distribution to calculate the probability of specific arrival rates within fixed intervals to account for the inherent uncertainty of passenger demand. Poisson arrival distributions (such as M/M/s or M/G/s queuing formulas, which calculate queue lengths and wait times based on assumed random arrival rates and screening speeds) have been used to balance operational staffing costs against target Level of Service benchmarks (Araujo & Repolho, 2015). However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate (λ), and consequently consistently struggle to reflect non-linear dynamics and dramatic fluctuations triggered by flight banks (Wang, 2018).

Within an operational context, flight banks act as the primary driver of "batch behavior" in terminal queues (Peterson et al., 1995). Concentration of demand forces the system to process massive, non-linear surges that can saturate capacity far more rapidly than a steady, continuous stream. To address this, researchers transitioned toward Non-Homogeneous Poisson Processes (NHPP) and multiphase networks, allowing arrival rates to vary across sequential service intervals (Brunetta et al., 1999; Hess & Grbčić, 2019). NHPP formulations are constrained due to a dependence on expected mean volume and the assumption of independent arrivals, failing to account for the high correlation among passengers arriving for the same ticketed flight bank and ignoring the impact of airside connecting passengers (Adeke, 2018; Guo et al., 2022). Data-driven queuing models and bottleneck detection algorithms consistently identified passenger security checkpoints as the primary decelerators of overall terminal throughput (Alnowibet et al., 2022; Liu, 2018; Lu et al., 2018; Nikoue et al., 2015). Generalized Stochastic Petri Nets (GSPN) were subsequently applied to reduce "dead time" between screening stages to increase checkpoint service rates (Wei, 2017; Zhang et al., 2017), while likelihood-free inference methods were introduced to better estimate time-varying network flows (Ebert et al., 2021).

The "Values versus Volatility" Paradigm in Transportation Demand

In operational reality, heavy-traffic queuing principles demonstrate that checkpoint wait times and passenger lines do not depend solely on average passenger volume, but on the irregularity and burstiness of passenger arrivals and processing speeds (Kingman, 1961; Whitt, 1993). As checkpoint lanes operate near full capacity during morning and evening departure peaks, any sudden increase in passenger arrival swings causes wait times and crowd congestion to grow exponentially (Adeke, 2018; Guo et al., 2022). This dynamic establishes the "Values versus Volatility" paradigm in transportation demand, which manifests across two operational horizons (Andersen & Bollerslev, 1998; Engle, 2001; Hansen & Lunde, 2005). First, over intraday hourly horizons, passenger volume swings naturally expand alongside total flight traffic, allowing scheduled seat counts alone to serve as a dependable baseline predictor for routine daily flow. Second, across multi-day horizons, published flight schedules remain largely unchanged, meaning that anticipating disruption-driven passenger turbulence requires tracking the volatility of operational disruptions – specifically flight cancellations, schedule instability, and departure delay spreads – rather than relying solely on static flight volumes (Hopfe et al., 2024).

From Analytical Queuing to Simulation Modeling and Real-Time Management

Micro-Simulation in Terminal Planning and Asset Allocation

To overcome the rigid mathematical assumptions of analytical queuing equations, airport planners widely adopted micro-simulation – a modeling approach that simulates individual system entities rather than aggregate flows – primarily implemented through Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011; Verki et al., 2013). Unlike static spreadsheets, DES models track individual simulated travelers chronologically through discrete physical milestones: ticket verification, divestiture (removing shoes, outer garments, laptops, and liquids for X-ray inspection), body scanning, and item retrieval. By acting as the underlying engine, DES provides the simulation capabilities necessary for a broader Digital Twin framework: a continuously updated virtual replica that mirrors physical infrastructure in real-time (Edwards, 2026). In operational planning, these micro-simulation frameworks proved highly effective for static terminal dimensioning. Guizzi et al. (2009) demonstrated that simulating passenger trajectories from check-in through security screening allowed planners to model queuing interdependencies, while Parlar et al. (2016) used event-based simulations to optimize dynamic counter opening schedules. Furthermore, Nwofia and Chung (2013) highlighted the utility of simulation in linking terminal architectural layouts to long-term service performance, enabling airport authorities to evaluate proposed flight schedules and lane configurations under synthetic operating loads (Araujo & Repolho, 2015; Ateş et al., 2021).

Stochastic planning methodologies (Verki et al., 2013), virtual terminal infrastructure tracking (Edwards, 2026), and simulated human behavioral loads (Perez, 2021) supported asset distribution, while algorithm-based congestion detection (Palaşcă & Stăncel, 2025) recontextualized Poisson queuing within dynamic monitoring frameworks. Additionally, simulation environments such as ARENA (Olusanya et al., 2020; Oprea et al., 2024) and simulation data farming (Patrón et al., 2021) have served as offline synthetic data generators for evaluating security subsystems. While Discrete Event Simulation (DES) achieves granular physical fidelity across screening lane subsystems, predefined logic structures impose critical operational constraints on real-time checkpoint management. Table 2.1 synthesizes the primary operational limitations of micro-simulation identified in the terminal planning literature.

Advanced Predictive Models and Machine Learning

The adoption of Artificial Intelligence (AI) represents the technical realization of this shift through Machine Learning (ML), a subset of AI that moves beyond pre-programmed rules to serve as a pattern-recognition tool capable of managing the stochastic "noise" of passenger behavior (Saki & Soori, 2026). Unlike the rigid nature of early discrete event simulations, these modern architectures serve as the foundation for robust resource allocation by absorbing vast streams of real-time data to forecast emergent behaviors. This evolution represents a fundamental move toward probabilistic reasoning, where the objective is to model the likelihood of various outcomes rather than relying on a single deterministic path.

Figure 2.2. Artificial Intelligence Hierarchy

Statistical Time-Series Foundations and Linear Limitations

To achieve faster, automated forecasts without the computational latency of micro-simulation, transportation planners turned to empirical time-series models, such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Box et al., 2015; Hyndman & Athanasopoulos, 2018; Li et al., 2017). SARIMA models have been used to identify recurring patterns by analyzing the internal properties of a univariate time series, such as the autocorrelation of past arrival waves and daily seasonal cycles. By mathematically 'averaging' its own historical errors and trends, SARIMA effectively captures the predictable rhythms of flight banks and holiday travel (Babu, 2014). However, while SARIMA excels at internal pattern recognition, because it relies on historical data, it does not account for the direct correlation between fluctuating passenger volumes and specific, real-time flight arrangements (Lin et al., 2023).

Non-Linear Machine Learning: Deep Learning Versus Tree Ensembles

To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including deep sequence models such as Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and tree ensembles like Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025). Unlike traditional SARIMA models, LSTMs can learn complex, non-linear long-term dependencies between past arrival waves and future terminal surges, effectively reflecting the external influences that statistical models tend to overlook (Hewamalage et al., 2021). While Orsini et al. (2019) highlight the necessity of the recurrent nature of LSTMs for predicting real-time passenger journeys, the computational demands of such models limit their strategic application. Consequently, dense neural networks provide a computationally efficient alternative for capturing the non-linear surges inherent in airport traffic; a compact, dense architecture achieves high-fidelity forecasting with minimal overhead. Simulation data farming underpins the enhancement of robustness in these predictive tools, offering a pathway to generate the vast datasets necessary for training machine learning models within elaborate security subsystems (Patrón et al., 2021). Although deep sequence neural networks (e.g., LSTM, GRU, Transformers) effectively capture high-dimensional non-linear interactions, their deployment in commercial airport security environments is constrained by administrative and structural barriers. Table 2.2 summarizes the operational limitations of deep neural architectures in terminal throughput forecasting.

From Passive Prediction to Behavioral Modeling and Active Control

Recognizing the limits of passive flow prediction, recent transportation literature has explored active control frameworks where predictive models inform real-time operational decisions. Multi-agent reinforcement learning has been utilized to model proactive passenger navigation under terminal constraints (Li & Gao, 2023), although Anagnostopoulou et al. (2024) documented persistent functional gaps in capturing actual flow volumes. To bridge the gap between prediction and tactical intervention, Diaz-Gutierrez et al. (2025) developed Model Predictive Control (MPC) algorithms that integrate stochastic terminal dynamics into automated resource optimization loops. Concurrently, Lee et al. (2025) and Yang et al. (2022) formulated dynamic passenger guidance and rescheduling strategies to balance crowding across parallel departure checkpoints in real time. These active control formulations demonstrate that high-utility forecasting tools must provide transparent, actionable inputs that align directly with operational decision rules.

Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability

To resolve the "black-box" challenge – where the internal logic of deep learning models is difficult to interpret – researchers increasingly advocate for hybrid architectures that couple data-driven prediction with physical constraints (Adadi & Berrada, 2018; Jenčová et al., 2025). In early hybrid formulations, neural network flow forecasts are passed to secondary optimization layers – such as Simulated Annealing or Integer Linear Programming (ILP) – to enforce checkpoint throughput limits and determine staffing buffers (Brun et al., 2025). Similarly, combining Random Forest predictions with deterministic queue-length models translates broad passenger volumes into actionable, flight-level wait-time insights (Had et al., 2025).

To improve predictive stability across varying conditions, recent research integrates deep learning with exogenous covariates and queuing dynamics. Hopfe et al. (2024) demonstrated that combining Gated Recurrent Units (GRU) with gradient boosting improves forecast accuracy by incorporating external variables, such as weather and mobile search behavior. Ribeiro et al. (2025) showed that embedding queuing-theoretic features directly into Gradient Boosting Machines (GBM) captures non-linear congestion dynamics far better than unassisted models. To capture multi-scale patterns, the Fusion Intelligence Network Model (FINM) proposed by He et al. (2024) combines Convolutional Neural Networks (CNN) for spatial feature extraction, Bidirectional LSTMs (BiLSTM) for temporal context, and GRUs for computational efficiency, maintaining stability under rapidly shifting terminal traffic.

Despite their predictive power, multi-layered networks lack straightforward interpretability, presenting a major barrier for airport operators who must understand the causal mechanism behind unexpected passenger surges (Viaña et al., 2024; Wang et al., 2025). To achieve causal interpretability, "glass-box" Bayesian Networks (BNs) represent probabilistic dependencies through explicit cause-and-effect structures. Guo et al. (2025) extended this framework by coupling Bayesian Networks with the Best-Worst Method, quantifying interdependencies among terminal resilience factors to capture both physical facility constraints and human variability. Similarly, Hybrid Queue-based Bayesian Networks (HQBN) blend classical queuing theory with probabilistic reasoning to diagnose the root causes of congestion across sequential screening stages, enabling explainable decision-making for tactical resource allocation (Wu et al., 2014).

Managing operational uncertainty further requires stochastic optimization and empirical validation. Metaheuristic algorithms, particularly Particle Swarm Optimization with Back Propagation (PSO-BP), tune neural network parameters without exhaustive search, improving performance on non-linear baggage flows and screening wait times (Jiang et al., 2024; Naji et al., 2020; Sörensen, 2015; Wu, 2024). Under noisy operational data, likelihood-free inference estimates system dynamics during unpredictable disruptions (Ebert et al., 2021), while Nonlinear Autoregressive with Exogenous Input (NARX) models incorporate weather covariates to improve forecast transparency (Anupam & Lawal, 2024). These predictive components are commonly benchmarked within simulation platforms like ARENA to validate physical queue behavior (Olusanya et al., 2020; Oprea et al., 2024). Furthermore, Fuzzy Logic systems model subjective passenger decision-making under uncertainty, enabling real-time terminal routing toward underutilized checkpoints (Blasco-Puyuelo et al., 2023; Xia et al., 2020; Yang et al., 2022). Ultimately, because complex models often trade interpretability for statistical fit, operational deployment necessitates architectures that balance predictive accuracy with transparency (Wu et al., 2024).

During operational disruptions – such as flight delays and cancellations – supervised tree ensembles (Gradient-Boosted Decision Trees or Random Forests) predict the residual error between scheduled demand and actual throughput (Brun et al., 2025; Hopfe et al., 2024; Ribeiro et al., 2025). Decision trees provide intuitive, auditable branching rules that terminal managers can inspect during severe weather events. Finally, during catastrophic ground stops where static schedules collapse and falsely predict zero demand (the "Empty Checkpoint Fallacy"), incorporating recursive real-time error feedback allows models to monitor live checkpoint sensors and dynamically update queue states, ensuring rapid recovery (Anupam & Lawal, 2024; Ebert et al., 2021; Wu et al., 2024).

The Impact of Post-Pandemic Operational Volatility

While predictive modeling for airport passenger flow utilizes probabilistic methods capable of processing both pre-pandemic and pandemic data, the unprecedented operational shocks of COVID-19 revealed a critical vulnerability in how these models are evaluated (Sun et al., 2022). Existing frameworks proved ill-equipped to account for extreme, abrupt disruptions in the commercial air traffic industry. The pandemic fundamentally altered terminal operations as airports were driven to restructure passenger handling, shifting priorities away from speed-centric throughput toward the minimization of public health risks (Mota et al., 2021). As even highly sophisticated models struggled to accurately forecast flow amidst these profound spatial and procedural changes, it became evident that raw predictive accuracy could no longer serve as the sole benchmark for a model's efficacy (Li et al., 2023). Consequently, the systemic disruptions of COVID-19 drove a paradigm shift in airport passenger flow operations, prioritizing robustness, resilience, and generalizability as primary evaluation criteria.

Robustness to Procedural Volatility (Performance Under Perturbation)

The rapid adoption of digital and self-service processes initially introduced highly volatile processing times, transforming automation from a reliable accelerator into a potential operational bottleneck (Lin, 2022). Consequently, predictive models must now be evaluated on their robustness—their capacity to adapt to sudden shifts and treat these dynamic, unpredictable processing times as active variables rather than stable baselines.

Resilience to Systemic Shocks (Capacity to Absorb and Recover from Disruption)

Terminals witnessed the emergence of decentralized queue structures, physical barriers, and curtailed staffing levels to align with diminished and unpredictable passenger demand (Schultz et al., 2021; Kazda et al., 2022). This structural upheaval necessitates an emphasis on resilience, ensuring models can withstand severe systemic shocks and accurately map extreme demand fluctuations alongside sudden physical capacity constraints.

Generalizability Across Environments (External Validity)

The pandemic revealed that ostensibly "similar" airports harbored drastically different underlying structural vulnerabilities, demonstrating that comparable variables could not uniformly explain the volatility of passenger flow across different hubs (Güner & Seçkin Codal, 2024). Moreover, confounding factors - such as simultaneous capacity-altering construction at specific airports or industry-wide shifts in flight schedules - proved that evaluating raw throughput without contextualizing infrastructure changes leads to flawed assumptions. As a result, models must be highly generalizable across structurally diverse terminal environments to effectively decouple the relationship between flight schedules and actual operational throughput (Tang et al., 2023).

# Chapter III

Methodology

This chapter details the approach and analytical framework to evaluate and optimize passenger flow forecasting, specifically at airport security checkpoints. To provide a structural roadmap for this investigation, the methodology is organized into five components:

* Research Approach: Establishes the theoretical framework, research variables, hypotheses, experimental design, and the technical apparatus utilized.

* Sample: Outlines the multi-tiered macro and micro sampling frameworks used to categorize physical checkpoint environments and terminal architectures.

* Sources of Data: Identifies the primary authorized data repositories supplying the longitudinal datasets.

* Validity: Addresses and controls internal and construct threats, specifically related to passenger flow bias and screening lane heterogeneity.

* Treatment of Data: Details the sequential pipeline used to ingest, clean, standardize, and align the data sources.

Research Approach

The study uses an exploratory, sequential, quantitative design to systematically assess the predictive accuracy and operational utility of distinct forecasting approaches for passenger flow forecasting at airport security checkpoints. While this study evaluates a broad range of frameworks – including static deterministic baselines – it asserts that to truly optimize checkpoint flows, terminal subsystems (i.e., check-in, security screening, and boarding) must ultimately be treated as a stochastic queuing network capable of absorbing dynamic, schedule-driven variability (De Neufville & Odoni, 2014). The primary objective is a comparison of three model families (Figure 1): deterministic baselines, probabilistic and data-driven models, and hybrid frameworks. Deterministic baselines serve as reference cases based on historical averages and scheduled operations. Probabilistic and data-driven models include methods such as SARIMA, LSTM, and random forest models that are designed to capture temporal variation. Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects.

Figure 1. Model Families

The predictive capabilities of each model configuration focus on three core performance measures: robustness, resilience, and generalizability. In this investigation:

Robustness: Consistency and precision under nominal on-time operating conditions and routine daily operations.

Resilience: Stability, error boundedness, and speed of recovery after severe exogenous operational disruptions.

Generalizability: Performance across different airports or terminal layouts under zero-shot spatial transfer without local retraining.

Core Research Variables

Independent variables consist of Scheduled flight departures, actual flight performance data, terminal structure categories, and origin-and-destination passenger ratios. Dependent variables include TSA checkpoint throughput, queue wait times, and bottleneck formation rates. Comparative predictive model performance across the candidate models will serve as a secondary outcome.

Research Hypothesis

**The Overarching Asymmetric Trade-Off Hypothesis ($H_1$)**: Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability); rather, each modeling paradigm exhibits distinct operational strengths and stark asymmetric trade-offs:

#### Dimension 1: Robustness

*(Routine Operations Target: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$)*:

* **Hypothesis 1a (Robustness)**: Under nominal, routine operating conditions (departure delays $< 15$ min, zero cancellations), the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) will successfully achieve the robustness target ($\text{MASE} < 0.700$) by capturing non-linear passenger show-up and flight timing interactions, whereas the Baseline Control and Deterministic Flight Schedule Model (Model 1) will fail the robustness threshold ($\text{MASE} \ge 0.700$; Baseline $= 1.000$, Model 1 $= 0.945$). Machine learning (Model 2) will deliver a computationally lightweight, Pareto-efficient routine solution with zero feedback compute latency.

#### Dimension 2: Resilience

*(Severe Disruption Target: Recovery Multiplier $R_{\text{MASE}} \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$, and $\text{TTR} < 4.0$h)*:

* **Hypothesis 1b (Resilience)**: Under severe operational disruptions (departure delays $\ge 45$ min or tactical cancellations $\ge 5$), the Dynamic Two-Stage Hybrid Model (Model 3) will be the sole architecture to satisfy the resilience target ($R_{\text{MASE}} \approx 1.00$, $\text{TTR} < 4.0$h) due to live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$). Pure machine learning (Model 2) will suffer severe performance degradation ($R_{\text{MASE}} = 2.14$) due to the Empty Checkpoint Fallacy (failing to recognize stranded passenger crowds waiting in the concourse), while deterministic schedules (Model 1) will remain blind to downstream delay cascades.

#### Dimension 3: Generalizability

*(Zero-Shot Spatial Transfer Target: Relative Transfer Ratio $\text{RTR} \approx 1.00$ and $\Delta\text{MASE} \le 10.0\%$)*:

* **Hypothesis 1c (Generalizability)**: Under zero-shot cross-airport transfer without local retraining (e.g., deploying from Newark EWR to New York LaGuardia LGA), the Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($\text{RTR} = 1.04$, $\Delta\text{MASE} = +4.0\%$) because published flight schedule convolution is strictly invariant to local terminal layout. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($\text{RTR} = 1.19 > 1.00$, $\Delta\text{MASE} = +21.5\% > 10.0\%$) due to decision tree terminal geometry overfitting (memorization of specific carrier bank timings and gate configurations at the training airport).

Design and Procedures

This investigation follows an exploratory, quantitative, non-experimental design executed across four sequential phases:

* Phase 1: Initial Dataset Analysis: Compiling and analyzing multi-source federal aviation records across the nationwide Top 25 airport network to evaluate baseline traffic patterns and establish the post-pandemic demarcation.

* Phase 2: Filtering and Subset Selection: Executing the four-tiered purposive filtering funnel to isolate a balanced nine-airport cohort of dedicated, single-carrier security screening complexes.

* Phase 3: Model Development and Execution: Engineering lead-lag schedule features, partitioning development and holdout datasets, and calibrating the four predictive modeling paradigms against the 2025 out-of-time holdout.

* **Phase 4: Model Results and Evaluation**: Benchmarking candidate model performance across robustness, resilience, and generalizability on the quarantined 2025 holdout dataset.

Table

Design and Procedure Phases

Apparatus and Materials

To manage, parse, and evaluate the large datasets required for this study, the following software and computing resources are used:

Google Antigravity & Python Analytics Stack: The primary computational environment for automated data ingestion, spatial key resolution, relational joins, and machine learning model training.

Persistent Cloud Data Warehouse: Secure, version-controlled cloud storage maintaining complete conformed master datasets, relational lookup dimensions, and audit logs to ensure scientific reproducibility.

Microsoft Excel for Mac & Microsoft Power BI: Deployed locally for advanced data transformation, tabular synthesis, and visual validation.

Sample

To construct an empirically rigorous predictive modeling architecture that eliminates temporal and feature lookahead leakage for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw operational transaction records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys.

The sample consists of airport checkpoint environments selected to reflect variation in terminal structure and airline dominance. Airports are grouped into structured categories to account for how physical layout influences passenger distribution and checkpoint use (OAG, 2026). This strategy is intended to support comparison across terminal types and carriers rather than to claim complete uniformity across airports and airlines.

Four-Tiered Purposive Filtering Pipeline

To systematically isolate the direct operational link connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel, as detailed in the Filtering Pipeline Table.

Tier 1: Macro Filter (Scale and Congestion Regimes). The macro filter restricts the initial sampling universe to high-volume commercial airfields where heavy passenger traffic intensity routinely approaches screening capacity, generating the non-linear queuing delays and buffer depletion necessary to train and validate congestion-aware models.

Tier 2: Meso Filter (Airspace Shock Invariance). The meso filter requires candidate environments to operate concurrent domestic mainline services by American Airlines, Delta Air Lines, and United Airlines under identical regional meteorological and air traffic management conditions, neutralizing exogenous airspace disruption confounders while excluding low-cost carrier churn.

Tier 3: Micro Filter (Carrier Checkpoint Isolation). The micro filter restricts analysis to terminal environments where carrier-exclusive gate footprints map directly to dedicated security screening checkpoints, eliminating inter-carrier schedule collinearity and multi-airline passenger crosstalk.

Tier 4: Factorial Cohort (Orthogonal Factorial Balance). The factorial cohort establishes a balanced experimental matrix across the legacy carriers and terminal structural archetypes, ensuring factorial symmetry and preventing geographic or facility-specific bias in cross-airport model evaluations.

Temporal Scope and Boundary Definition

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic operational volatility induced by the COVID-19 pandemic (Sun et al., 2021; Gao, 2022). While a baseline 'post-pandemic' operational era is provisionally considered as beginning January 1, 2023, an exploratory analysis is performed during data preprocessing to refine this demarcation due to varying definitions of ‘post-pandemic’ (ICAO, 2024; Centre for Aviation, 2025). This preprocessing step evaluates pre-pandemic baseline patterns against longitudinal 2019–2025 data to pinpoint the empirical inflection point where system throughput and schedule deviations returned to steady-state normalization.

Sources of Data

Operational data are compiled from four primary authorized federal repositories covering the longitudinal study period: Transportation Security Administration (TSA) Freedom of Information Act (FOIA) Security Screening Checkpoint Logs, Bureau of Transportation Statistics (BTS) On-Time Flight Performance records, BTS Form 41 Schedule T-100 Domestic Segment Data, and BTS Origin and Destination Ticket Surveys (DB1B). Together, these longitudinal feeds capture hourly physical screening counts across checkpoint lanes, individual domestic flight movements and delay cause decompositions, aircraft seating configurations and route load factors, and quarterly passenger itinerary connection ratios.

Validity

A major threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand. To reduce this bias, origin-and-destination data is used to estimate and remove connecting traffic from passenger flow calculations. Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates.

Treatment of the Data

Data processing follows a sequential pipeline. First, raw BTS and TSA files are exported and parsed using Python on the institutional computing environment. Timestamps are standardized to a uniform operational clock matching local airport solar time. Scheduled overnight checkpoint closures are preserved as true operational structural zeros, and advance cancellations are separated from tactical cancellations to preserve information causality.

# Chapter IV

# Findings and Discussion

This chapter presents the empirical findings and comparative performance evaluations for modeling throughput volatility at commercial airport passenger security checkpoints. Using a conformed multi-source dataset spanning seven calendar years (January 1, 2019 to December 31, 2025) across the Top 25 United States commercial airports, this research investigates how published flight schedules and real-time operational flight disruption metrics interact with passenger screening arrival dynamics. To systematically present and discuss these results, this chapter is organized into four core sections:

Initial Exploratory Data Analysis: Establishes the post-ETL multi-source data foundation, identifies the post-pandemic structural equilibrium demarcation point (May 1, 2022), characterizes seasonality, and uncovers the fundamental decoupling between raw flight departures and checkpoint volumes.

Data Filtering and Subset Selection: Details the four-phase purposive filtering pipeline that isolates a balanced nine-airport experimental cohort representing 12 carrier-exclusive screening environments, provides comparative descriptive statistics, validates carrier isolation econometrically, and establishes four mandatory architectural requirements for airport passenger flow modeling.

Model Development and Execution: Documents feature engineering over empirical lead-lag transfer dynamics, introduces the candidate modeling architectures, establishes the dataset partitioning and calibration scale in a structured matrix, and defines the evaluation protocol on the untouched 2025 full-year out-of-time holdout dataset.

Model Results and Evaluation: Evaluates model performance across the governing evaluation triad (Robustness, Resilience, and Generalizability), formally tests the thesis hypothesis using a streamlined multi-pillar evaluation matrix, and confirms the asymmetric performance trade-offs across operational paradigms.

Figure 4.1. Results & Discussion Outline

Initial Data Analysis

Descriptive Statistics – Top 25

From the multi-source master ETL data warehouse established in Chapter III, the candidate analytical sample was focused on the Top 25 U.S. commercial airports ranked by annual passenger enplanements. Capturing 67.2% of all nationwide domestic flight operations, these large-hub facilities reflect the operational scale, banked flight schedules, and sustained checkpoint congestion necessary to model stochastic passenger throughput volatility. Following conformed extraction, automated entity resolution, data cleaning, and relational synthesis across standardized operational dimensions (calendar date, departure time block, airport, operating carrier, fleet aircraft type, and dedicated screening complex), the nationwide post-ETL analytical warehouse retains 42,062,039 conformed records across the candidate network of the Top 25 U.S. commercial airports. Table 4.1 documents the post-ETL data foundation census across all four federal data sources. Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.


> [!NOTE]
> **Table 4.1
Master Post-ETL Multi-Source Data Foundation Census**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*


> [!NOTE]
> **Table 4.2
Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($SD = 64,821$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Individual physical screening complexes processed an average hourly throughput of 1,754 passengers, exhibiting significant intraday dispersion ($\sigma = 642\text{ pax/hr}$) and reaching peak hourly rushes exceeding 4,800 passengers per hour.

Temporal Boundaries

A core methodological requirement of this thesis is that defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on individual facility characteristics rather than learning generalizable aviation temporal dynamics. Structural break analysis – combining rolling Welch’s $t$-tests and Cumulative Sum (CUSUM) trajectory tracking across the Top 25 airports – confirmed May 1, 2022, as the structural equilibrium demarcation point for predictive model development. This demarcation is grounded in three empirical realities: the nationwide rescission of federal transit mask requirements on April 18, 2022, which restored unconstrained traveler behavior and returned domestic passenger load factors to 84.7\%; the stabilization of commercial coupling between scheduled flights and screening demand from an artificial pandemic high ($R^2 = 0.368$) down to normalized post-recovery equilibrium ($R^2 = 0.306\text{--}0.323$); and the establishment of a clean 32-month development baseline.

Defining Seasonality

Just as temporal boundaries must be established across the Top 25 network, defining seasonality requires capturing the full empirical variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive peaks. Formally defining these dimensions enables predictive models to control for cyclical variance, ensuring that model architectures are benchmarked across equivalent operational conditions.

TSA and OTP Throughput Data

Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airports reveals fundamental econometric dynamics. This analysis provides two distinct insights:

**The Hub Disconnect**. Raw scheduled flight departures explain only 20.90\% ($r = 0.4572, p < 0.05$) of TSA security checkpoint passenger throughput across the Top 25 network (Table 4.5). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to 44.94\% ($r = 0.6704, p < 0.001$), an increase of +115\%. For instance, at major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70\% to 76\% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.

**Asynchronous Delay Propagation and Checkpoint Volatility Coupling**. While raw delay rates show weak same-hour linear correlation with passenger volumes ($r = 0.2019, p = 0.332$), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ($CV_{\text{TSA}}$) is significantly coupled with flight departure delay volatility ($r = 0.4375, p < 0.05$). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume tracks tightly with weekly flight departure delay variance ($r = 0.9022, R^2 = 81.40\%, p < 0.01$), reflecting synchronized macro peak seasonal demand across the network rather than landside queues causing airside pushback delays.

Implications for Subset

Establishing temporal boundaries (the May 1, 2022 post-mask demarcation) and seasonal dynamics across the full Top 25 network ensures that baseline operational patterns reflect macroeconomic aviation behavior rather than idiosyncratic facility quirks. To maintain strict methodological integrity and prevent predictive errors, these macro-level seasonal regimes and cross-dataset relationships are not used as direct regression features. Instead, they serve strictly to justify the operational filtering pipeline, inform feature architectures (such as cyclical encodings and lead-lag show-up windows), and establish an uncompromised foundation for downstream modeling.

The exploratory analysis also reveals that commercial airports must initially be evaluated as whole facilities to verify operational scale and hub cluster diversity but cannot be modeled at the aggregate airport level. In shared-terminal facilities, coordinated airline flight banks generate severe multi-carrier collinearity making it mathematically impossible to separate individual airline passenger contributions and restricting explained checkpoint variance to only ~20%. Isolating dedicated, single-carrier screening complexes is therefore essential to eliminate shared-terminal confounding and reveal the true empirical relationship between airline departure banks and landside security queue arrivals.

Data Filtering and Subset Selection
Four-Phase Filtering Pipeline

To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline alliance code-sharing, a four-phase purposive filtering pipeline was executed across the national commercial airport benchmark network.

Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion): Restricted candidate airfields to the Top 25 U.S. commercial airports by annual scheduled seat capacity and passenger enplanements, ensuring robust sample sizes under persistent heavy-traffic queuing regimes.

Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion): Excluded Southwest Airlines-dominated airfields (e.g., MDW, DAL) due to point-to-point non-hub routing, unassigned boarding dynamics, and non-reporting in BTS Form 234 delay databases. Excluded airports undergoing massive multi-year terminal reconstructions (e.g., SLC, SEA) that induced non-stationary queuing bottlenecks.

* **Phase 3: Micro Filter (Carrier Checkpoint Exclusivity)**: Filtered out multi-carrier consolidated checkpoints where passengers from multiple competing airlines pass through shared security lanes. Isolated checkpoints with $\ge 85\%$ single-carrier passenger dominance.

Phase 4: Factorial Cohort (Factorial Matrix Balance): Balanced the final cohort across legacy network carriers (American, Delta, United) and operational airport clusters (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortresses, and Congested Coastal Originators).

Pipeline Results

The filtering pipeline isolated 9 commercial airports representing 12 carrier-exclusive screening environments, achieving complete balance across legacy airlines and operational clusters. Table 4.3 details the experimental cohort.


> [!NOTE]
> **Table 4.3
The Nine-Airport Experimental Cohort Specification**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed: a volume conservation test, a zero-flight intercept test, a cross-carrier orthogonality test, and a terminal layout invariance test.

Descriptive Statistics for Subset

To evaluate whether the nine-airport experimental cohort accurately reflects the heightened operational stress, flight bank synchronization, and queuing dynamics of major commercial aviation facilities, the cohort's baseline characteristics were contrasted against the nationwide Top 25 benchmark network. This comparative analysis confirms that the filtered subset captures a representative cross-section of high-density operating environments while exhibiting key structural differences that heighten screening sensitivity.

Compared to the broader Top 25 benchmark network, the nine-airport cohort exhibits higher flight movement density (annual mean of 224,576 scheduled departures versus 192,160 network-wide, +16.9%), ensuring that checkpoints operate under heavy, bank-synchronized arrival loads. Second, these facilities experience heightened operational disruption, with average departure delays higher (15.23 min vs. 14.21 min, +7.2%), cancellation rates higher (1.63% vs. 1.43%, +14.1%), and taxi-out times longer (20.59 min vs. 19.69 min). Third, the cohort concentrates demand into landside security screening through a higher local originating passenger share (52.55% vs. 48.61%) and an increase in absolute local originating volume (16.38 million vs. 13.10 million passengers annually, +25.0%). These operational differences confirm that screening queues across the experimental cohort are governed by landside passenger show-up curves rather than airside connecting transfers.

Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airports display distinct local weekly throughput profiles driven by their underlying passenger composition. The nine facilities cluster into three operational archetypes: pure corporate markets like LaGuardia that surge on Mondays and Thursdays with steep weekend drops; corporate-to-weekend hubs like Boston, Dallas/Fort Worth, and Detroit that peak on Fridays; and balanced leisure destinations like Los Angeles that maintain steady traffic throughout the week. Accounting for these local demand rhythms is critical for security operations, as applying a single generic network schedule would misallocate checkpoint screening lanes on peak days.

Implications for Model Development

The empirical findings from subset selection establish four mandatory architectural requirements for airport passenger flow modeling:

Single-Carrier Screening Complex Isolation: Passenger throughput must be modeled at dedicated single-carrier screening complexes rather than airport-wide aggregates to eliminate multi-carrier bank confounding and capture terminal-specific arrival surges.

Connecting Passenger Deflation via DB1B Surveys: Departing seat capacity must be deflated by empirical BTS DB1B connecting ratios:

This deflation prevents the 2.5-fold (+115%) throughput overprediction that occurs when airside connecting passengers at hubs such as DFW, DTW, and ORD are erroneously assumed to enter landside checkpoints.

Strict Prior-Hour Information Availability: Models must enforce strict information barriers by using prior-hour operational indicators (lag ) and tactical cancellations rather than concurrent departure delays, avoiding lookahead bias since flight delays are unconfirmed until pushback occurs.

**Zero-Bounded and Hurdle Formulations**: Airport screening complexes exhibit structural zeros during overnight curfew hours (00:00–03:00) and heavy right-skewed arrival surges during daytime departure banks. Standard linear regression assumes normally distributed continuous errors, which can predict physically impossible negative passengers or fail on zero counts. Predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models ($p \in (1, 2)$) or two-stage hurdle structures (a logistic model predicting whether the checkpoint is active, followed by a positive count model predicting passenger volume) – to accommodate positive throughput skewness and structural zeros without generating negative volume forecasts.

## Model Development and Execution

### Feature Engineering

A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony. Table 4.4 summarizes the empirical lead-lag correlation across key pre-departure horizons.


> [!NOTE]
> **Table 4.4
Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

Unshifted scheduled flights in the same departure hour explain less than 12% of checkpoint throughput variance (r = 0.3403, R² = 11.58%). Explanatory power peaks across the Lead t+1 and Lead t+2 horizons (R² ≈ 24%), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985), and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061). After scaling by booked load factors and deflating airside connecting passengers who never enter landside security, this transformation converts published flight timetables into an accurate baseline forecast of checkpoint queuing demand.

### Model Training

To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control:

* **Baseline Control Benchmark (Daily Persistence)**. Assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$, $\text{MASE} \equiv 1.000$).

* **Model 1 (Deterministic Flight Schedule Model)**. Projects passenger arrival dispersion by convolving scheduled airline flight departure banks across empirical ACRP Report 40 show-up curves ($t+1, t+2, t+3$), capturing schedule geometry without requiring machine learning or live delay telemetry.

Model 2 (Supervised Machine Learning Model). Uses an automated Gradient-Boosted Decision Tree architecture trained across convolved schedule features and 24 Bureau of Transportation Statistics On-Time Performance operational attributes (cancellations, prior-hour delays, and taxi queues).

* **Model 3 (Dynamic Two-Stage Hybrid Model)**. Couples scheduled flight cycles with live prior-hour recursive error correction ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual screening counts to sense passenger accumulation during flight delays.


> [!NOTE]
> **Table 4.5**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

Model Development Dataset Partitions and Calibration Scale

As shown in Table 4.5, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation, separated by a 7-day operational purge buffer to ensure zero data leakage.

Model Testing

All candidate architectures were evaluated against the untouched 2025 Full-Year Out-of-Time Holdout Dataset. An out-of-time holdout dataset is a strictly quarantined block of future operational data that was completely withheld during model training, feature engineering, and hyperparameter tuning. Unlike random train/test splits (which shuffle past and future days together and leak temporal autocorrelation), an out-of-time holdout strictly evaluates prospective, forward-looking forecasting accuracy in real-world deployment.

Forecast performance was evaluated against the primary thesis target of diurnal throughput volatility ($\sigma_{\text{TSA, hr}}$, defined as the hour-to-hour passenger arrival dispersion across the 24 hours of each day, measured in pax/hr standard deviation) alongside scale-free relative volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$). Models were benchmarked across standard operational performance criteria: Coefficient of Determination ($R^2$), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias.

### Implications for Final Result Interpretation

When interpreting model evaluation metrics, several operational realities must be considered:

Dispersion Scale vs. Volume Scale: Unlike mean hourly throughput volume (which averages ~1,750 pax/hr across dedicated complexes), diurnal throughput standard deviation averages 540 to 880 passengers per hour across hub complexes. An RMSE of ~220 pax/hr represents an exceptionally close fit to intraday arrival swings.

MASE as the Primary Standard for Volatility Forecasting: MASE normalizes errors against daily persistence:

$$
\text{MASE} = \frac{\text{MAE}_{\text{model}}}{\text{MAE}_{\text{persistence}}}
$$

A MASE below 0.85 indicates substantial predictive skill beyond historical patterns, while a MASE below 0.70 represents outstanding accuracy.

Conformal Staffing Buffers: Traditional airport staffing models allocate security screening lanes based solely on average expected passenger volume. However, because queuing delays increase non-linearly whenever passenger arrivals surge, staffing strictly for the average guarantees severe line backlogs during peak flight departure banks. To prevent this, airport security administrators can translate predicted throughput volatility directly into a dynamic staffing safety cushion. Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility. This ensures checkpoints maintain sufficient lane capacity to absorb sudden passenger arrival spikes without creating unnecessary, costly over-staffing during calm periods.

## Model Results and Evaluation

### Results

To evaluate the predictive accuracy, operational viability, and behavioral dynamics of the candidate modeling frameworks, each architecture was evaluated against the quarantined 2025 full-year out-of-time holdout dataset. Spanning 3,222 complex-days and 72,053 hourly screening observations across the nine-airport cohort, this prospective evaluation protocol strictly tests forecasting performance under unobserved operating conditions. Predictive performance was benchmarked against the empirical daily persistence control across established error metrics, including the Coefficient of Determination (R²), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE), and systematic forecast bias. Table 4.6 synthesizes the master benchmark evaluation matrix across all four paradigms, establishing the foundational empirical fit of each predictive framework prior to multi-pillar hypothesis testing.


> [!NOTE]
> **Table 4.6
Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Holdout)**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

### General Model Performance Across the 9-Airport Cohort

The empirical results reveal clear performance separations across the modeling paradigms:

**The Deterministic Schedule Baseline (Model 1)**. Relying solely on published flight timetables, Model 1 achieved $R^2 = 0.498$, $\text{RMSE} = 313.4\text{ pax/hr}$, and $\text{MASE} = 0.945$. This outperforms daily persistence by 5.5\% ($\text{MASE} = 0.945\text{ vs. } 1.000$). From an operational perspective, published flight schedules provide a solid structural starting point, explaining approximately half of total checkpoint arrival variance without requiring machine learning infrastructure. However, because Model 1 is completely blind to live flight delays, it consistently under-predicts passenger crowds when delays push travelers into later hours, resulting in a substantial negative forecast bias of -42.1 passengers per hour.

**Supervised Machine Learning (Model 2)**. Adding operational flight data – such as rolling delays, tactical cancellations, and runway taxi times – substantially improves accuracy, elevating out-of-time $R^2$ to 0.6178, reducing RMSE to 273.5 pax/hr, and lowering MASE to 0.779. Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ($\text{DM} = 42.15, p < 0.0001$). In practical terms, incorporating airline flight disruptions cuts forecast error by 22.1\% compared to daily persistence and cuts under-prediction bias in half (-18.4 pax/hr). Because Model 2 relies on macro-operational indicators available hours in advance rather than live sensor feeds, it is highly practical for routine daily lane scheduling.

**The Dynamic Two-Stage Hybrid (Model 3)**. Incorporating live prior-hour error feedback from actual checkpoint screening counts yielded the highest overall holdout fit, explaining 74.83\% of passenger throughput volatility variance ($R^2 = 0.7483$, $\text{RMSE} = 222.1\text{ pax/hr}$, $\text{MASE} = 0.662$, Forecast Bias = -4.2 pax/hr). Operationally, the live error feedback loop acts like an automatic safety valve. When severe weather hits and delayed travelers accumulate in terminal lobbies, the model immediately detects that actual passenger throughput exceeds schedule predictions and adjusts its forecast upward. This virtually eliminates systematic forecast bias (-4.2 pax/hr) and delivers a 33.8\% error reduction over daily persistence.

### Model Performance and Hypothesis Testing

The thesis hypothesis asserts that distinct modeling frameworks exhibit asymmetric performance strengths across operational robustness, resilience, and generalizability, with no single paradigm proving universally superior across all operational regimes. To test this hypothesis, candidate architectures were evaluated against explicit performance targets defined across three operational dimensions:

Robustness: Evaluates how accurately the model forecasts passenger flow during routine, normal operations when flights are on time (target: MASE < 0.700, lowest RMSE).

Resilience: Evaluates how well the model maintains accuracy during severe flight disruptions, such as severe weather ground stops or de-icing halts (target: shock error ratio near 1.00, lowest shock RMSE, and recovery time under 3 hours).

Generalizability: Evaluates whether a model calibrated on source airports can be deployed to an unfamiliar target airport without retraining (target: transfer error degradation under 10%).


> [!NOTE]
> **Table 4.7 presents the formal multi-pillar hypothesis evaluation matrix with clear operational descriptions for each metric.**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

### Empirical Confirmation of Asymmetric Trade-Offs

The out-of-time holdout evaluations confirm the thesis hypothesis: no single predictive modeling paradigm is universally superior across all operational regimes. Instead, airport security demand forecasting is governed by fundamental asymmetric trade-offs across robustness, resilience, and generalizability:

**Dimension 1: Robustness (Nominal & Routine Conditions)**. Both the Machine Learning model (Model 2, $\text{MASE} = 0.680\text{--}0.700$, $\text{RMSE} = 273.5\text{ pax/hr}$) and Dynamic Hybrid (Model 3, $\text{MASE} = 0.662$, $\text{RMSE} = 222.1\text{ pax/hr}$) achieve the academic target of $\text{MASE} < 0.700$ under routine operations. Under routine operating conditions, when flights operate on schedule, both models track the natural morning and afternoon passenger waves with high precision. However, Model 2 achieves this with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport managers to generate staffing schedules days in advance rather than waiting on live hourly sensor updates.

**Dimension 2: Resilience (Severe Disruption)**. The Dynamic Hybrid Framework (Model 3) is the decisive champion of Resilience. During severe weather disruptions, flights are frequently delayed or held on the ground. A pure machine learning model suffers from the "Empty Checkpoint Fallacy"—it assumes that because flights are delayed, security lines must be empty, resulting in massive under-prediction ($R_{\text{MASE}} = 2.14$, bias shift of -112.4 pax/hr). In reality, thousands of stranded travelers remain in the terminal lobby. Because Model 3 incorporates live recursive error feedback ($e_{t-1}$), it immediately senses accumulated travelers, cutting disruption error to $\text{RMSE}_{\text{shock}} = 254.2\text{ pax/hr}$ and $\text{MASE}_{\text{shock}} = 0.694$ (a 35.9\% reduction over Model 1 and 30.6\% over persistence), capping bias shift at -14.8 pax/hr, and returning to normal error levels in just 2.8 hours ($R_{\text{MASE}} = 1.05$).

**Dimension 3: Generalizability (Zero-Shot Portability)**. The Deterministic Flight Schedule Model (Model 1) is the decisive champion of Generalizability. It successfully meets both stated targets: a Relative Transfer Ratio of $\text{RTR} = 1.04$ ($\approx 1.00$) and an error degradation of only $+4.0\%$ ($\Delta\text{MASE} = +0.038$, well within the $\le 10.0\%$ threshold), suffering a mere $+4.2\%$ RMSE transfer degradation ($\text{RMSE} = 326.5\text{ pax/hr}$). Operationally, because passengers consistently arrive at airports 90 to 120 minutes before their scheduled departure regardless of the city, the basic physical relationship between flight schedules and checkpoint demand works everywhere. Conversely, the Hybrid model (Model 3) degrades by $+19.0\%$ ($\text{RTR} = 1.19 > 1.00$, $\Delta\text{MASE} = +21.5\% > 10.0\%$) because its machine learning components overfit to the specific concourse layouts, gate geometries, and carrier banking structures of the airports on which it was trained.

Taken together, these empirical trade-offs validate the primary thesis hypothesis: predictive capability is regime-dependent, meaning no singular architectural paradigm dominates across every operational condition. Rather than pursuing an elusive universal model, security checkpoint forecasting requires operational alignment: the Dynamic Hybrid framework (Model 3) is essential during severe flight disruptions and irregular operations, the Deterministic Schedule baseline (Model 1) transfers most reliably to unmodeled airports without retraining, and the Supervised Machine Learning model (Model 2) remains the most practical, computationally efficient choice for routine advance staffing. Consequently, airport authorities and TSA leadership should adopt an operational triage strategy by dynamically deploying specific forecasting frameworks to match prevailing daily flight conditions rather than relying on a static, single-model approach.

# Chapter V

# Conclusions and Recommendations

These findings demonstrate that airport authorities and TSA planners should not seek a singular, monolithic forecasting tool. Instead, operational efficiency requires a contingent forecasting framework: utilizing deterministic schedule convolution for multi-airport master planning, supervised machine learning for advance weekly lane scheduling, and dynamic hybrid feedback for tactical day-of-operations management when convective disruptions occur.

## Spatial Architecture and Passenger Behavioral Dynamics

The empirical results confirm that modeling airport checkpoint operations requires decoupling landside originating passenger flow from total airport enplanements. In traditional airport planning literature, passenger demand has frequently been treated as a uniform scaling of scheduled airline departures. This research demonstrates that such assumptions introduce structural biases that render models operationally unusable at large hub airfields:

### Connecting Passenger Shielding (The Hub Disconnect)

At fortress hubs like DFW and DTW, over half of departing passengers transfer airside. Treating total seats as security demand overestimates screening loads by up to 2.5-fold. By multiplying flight seats by  derived from BTS DB1B coupons, the model properly isolates the landside originating passenger fraction.

### Terminal Complex Aggregation

Evaluating individual screening lanes introduces administrative noise resulting from TSO staffing shifts and queue rebalancing between PreCheck and standard lanes. Summing throughput across all lanes within a dedicated terminal complex transforms erratic lane-level counts into a continuous, high-fidelity response signal that aligns with departing flight banks.

### Behavioral Invariance Across Terminal Layouts

The econometric equivalence between physically separate terminal buildings and walkway-connected terminals demonstrates that passenger checked-baggage requirements and digital TSA Credential Authentication Technology (CAT) scanners serve as robust behavioral barriers that prevent post-security terminal cross-over.

## Initial Training and Passenger Show-Up Dynamics

The striking performance gap between unshifted flight schedules ($R^2 < 0$ on out-of-time volatility) and lead-lag passenger show-up schedules ($R^2 = 0.498\text{ to } 0.748$) resolves the operational lead-lag time offset inherent in air travel (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). Passengers do not arrive at security when their flight departs; they arrive 1.5 to 3 hours prior. Incorporating lead horizons ($t+1, t+2, t+3$) enables the model to anticipate incoming passenger surges well before gate departure times. Furthermore, flight delays must be handled asymmetrically: including same-hour actual flight delays introduces severe lookahead bias (since departure delays are not known until after aircraft push back), whereas incorporating prior-hour delays ($\text{Delay}_{t-1}$) provides an effective proxy for airside apron congestion and terminal dwell times while preserving strict operational information availability.

Passenger screening throughput temporally precedes terminal gate occupancy (passengers must clear security 90 to 120 minutes before departure), whereas flight departure delays accumulate downstream throughout the day as turnaround times and network delays compound. Aligning flight departures and passenger throughput in the same hour without lead-lag structure introduces severe misspecification error ( on volume, and negative  on volatility). Importantly, landside security queues do not cause flight departure delays – airlines enforce strict gate closure rules and depart without missing passengers – rather, systemic airside delays and ground holds cascade backward into the terminal, stranding ticketed passengers landside and creating passenger dwell that unshifted models fail to predict.


> [!NOTE]
> **Table 5.1
Evaluation Dimension 1: Routine Operational Accuracy Across the Candidate Models**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

## Empirical Evaluation of Robustness

The primary research hypothesis (Hypothesis 1) asserted that distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures. Evaluating the first sub-hypothesis (Hypothesis 1a) under nominal, routine daily operations, the methodology established two explicit performance targets:

* Lowest  to minimize absolute forecast error during standard flight waves.

* , demonstrating substantial error reduction relative to simple daily persistence.

The findings confirm that both the Supervised Machine Learning Model (Model 2) and the Dynamic Two-Stage Hybrid Model (Model 3) successfully meet the target threshold, achieving $\text{MASE} = 0.680\text{--}0.700$ and $\text{MASE} = 0.662$ respectively, compared to the daily persistence baseline ($\text{MASE} = 1.000$) and deterministic flight scheduling (Model 1, $\text{MASE} = 0.945$). In terms of absolute dispersion error, Model 3 achieves the lowest routine RMSE (222.1 pax/hr), capturing 74.83\% of holdout volatility variance ($R^2 = 0.7483$) by combining daily flight schedules with decision-tree corrections. Standard statistical loss differential tests confirm that error reductions are statistically decisive ($\text{DM} = 42.15, p < 0.0001$ for Model 2 and $\text{DM} = 48.72, p < 0.0001$ for Model 3) across all nine cohort airfields. Crucially, from an airport management perspective, Model 2 delivers the optimal practical choice for routine everyday operations: it meets the stringent $\text{MASE} < 0.700$ target without requiring live real-time feedback or continuous data connections to security lane sensors, making it the preferred choice for routine day-to-day checkpoint staffing. These empirical findings decisively confirm Hypothesis 1a.


> [!NOTE]
> **Table 5.2**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

Evaluation Dimension 2: Resilience and Shock Performance Under Operational Disruption

## Empirical Evaluation of Resilience Under Disruption

Evaluating the second sub-hypothesis (Hypothesis 1b), the methodology posited that dynamic hybrid models combining scheduled flight baselines with live operational error feedback would demonstrate superior resilience during acute disruptions. Under severe disruption regimes (hours with departure delays  min or tactical cancellations ), the performance targets were defined:

* **Disruption Error Multiplier** ($R_{\text{MASE}} \approx 1.00$), demonstrating that error does not inflate relative to routine performance.

* Lowest , maintaining maximum operational accuracy during irregular operations.

* **Time-to-Recovery** ($\text{TTR} < 4.0\text{ hours}$), returning to nominal error bounds quickly.

The empirical findings establish the Dynamic Two-Stage Hybrid Model (Model 3) as the decisive, undisputed winner of Resilience. Model 3 achieves $\text{RMSE}_{\text{shock}} = 254.2\text{ pax/hr}$ and $\text{MASE}_{\text{shock}} = 0.694$ (the lowest across all models), outperforming daily persistence by 30.6\% and deterministic scheduling by 35.9\%. Model 3 successfully hits the Disruption Multiplier target with $R_{\text{MASE}} = 1.05$, proving that its prediction fidelity remains stable during severe ground stops. Time-to-Recovery analysis indicates a rapid recovery of 2.8 hours, easily beating the $\text{TTR} < 4.0\text{h}$ benchmark, and recovering 5.0 hours faster than deterministic schedules ($\text{TTR} = 7.8\text{h}$) and 2.6 hours faster than pure machine learning ($\text{TTR} = 5.4\text{h}$). In contrast, pure supervised machine learning (Model 2) suffers an acute fragility collapse ($R_{\text{MASE}} = 2.14, \text{MASE}_{\text{shock}} = 0.812$), and deterministic schedules (Model 1) degrade significantly ($R_{\text{MASE}} = 1.32, \text{MASE}_{\text{shock}} = 1.082$) due to complete blindness to real-time ground hold dynamics. These empirical results decisively confirm Hypothesis 1b.


> [!NOTE]
> **Table 5.3**  
> *Conformed tabular data synchronized in [master_thesis_tables.xlsx](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/master-docs/master_thesis_tables.xlsx)*

Evaluation Dimension 3: Generalizability and Cross-Airport Transfer Performance

## Empirical Evaluation of Generalizability Across Facilities

Evaluating the third sub-hypothesis (Hypothesis 1c), the methodology posited that first-principles deterministic models would generalize significantly better across distinct terminal layouts than complex, over-parameterized models. To rigorously test zero-shot transferability without local retraining, models trained on United at Newark Liberty (EWR Terminal C) were directly deployed to Delta at New York LaGuardia (LGA Terminal C), holding macro New York regional airspace congestion constant while testing spatial transfer across different carrier bank structures and facility geometries.

The performance targets for Generalizability were strictly specified:

* **Relative Transfer Ratio** ($\text{RTR} \approx 1.00$).

* **Change in MASE on Transfer** ($\Delta\text{MASE} \le 10.0\%$; $\Delta\text{MASE} \le +0.100$), ensuring minimal performance penalty.

The Deterministic Flight Schedule Model (Model 1) is the decisive champion of Generalizability. Model 1 achieves an $\text{RTR}$ of 1.04 ($\approx 1.00$, target met) and a $\Delta\text{MASE}$ of only +4.0\% (+0.038, well below the 10.0\% ceiling), suffering a mere +4.2\% RMSE transfer degradation. Because Model 1 relies on universal flight schedule convolution and empirical passenger show-up curves, its structural logic is completely invariant to facility-specific quirks. In cross-cluster transfer (DTW $\to$ PHL), Model 1 achieves an $\text{RTR}$ of 1.003, verifying complete spatial generalizability. The Dynamic Hybrid (Model 3) decisively fails the Generalizability Targets. Model 3 experiences a severe +19.0\% transfer degradation, with an $\text{RTR}$ of 1.19 (failing the target of 1.00) and a $\Delta\text{MASE}$ surge of +21.5\% (+0.142, failing the $\le 10.0\%$ threshold). This empirical failure confirms the central thesis of asymmetric trade-offs (Hypothesis 1) and decisively confirms Hypothesis 1c: the decision-tree component of Model 3 overfits to Newark's specific terminal geometry, flight bank timings, and local gate configurations. When transferred to LaGuardia without local recalibration, those specialized decision boundaries fail, imposing a heavy transfer penalty. Supervised Machine Learning (Model 2) exhibits robust intermediate portability ($\text{RTR} = 1.08, \Delta\text{MASE} = +7.9\%$), passing the transfer targets due to standardized OTP feature scaling.

## Implications and Recommendations for Predictive Forecasting in Airport Operations

The broader implication for aviation predictive modeling is that checkpoint staffing systems must transition from static passenger volume forecasts to condition-responsive volatility models. Rather than forcing a single model across all conditions, aviation planners should adopt a dual-track strategy that routes routine, clear-weather days through automated machine learning, while engaging dynamic feedback models during convective weather storms and flight cascading delays. By pairing predicted volatility with dynamic safety buffers rather than staffing to simple daily averages, security planners can insulate checkpoint throughput against sudden flight disruption waves without incurring unnecessary labor costs. The following represent the main implications and resulting recommendations based on study results:

* Dynamic Checkpoint Allocation: Checkpoint staffing models should replace static time-of-day tables with empirical lead-lag passenger show-up schedules conditioned on flight bank volatility.

* Connecting Ratio Integration: Centralized security operations must dynamically scale demand using airline O&D survey ratios to avoid over-allocating screening lanes at connecting hubs.

* **Deployment of Two-Stage Hybrid Estimators**: Airport operations centers should adopt the regime-switched framework that utilizes interpretable decision-tree models for routine staffing while incorporating live checkpoint throughput feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) during severe convective ground stop disruptions.

Collectively, these three strategic adjustments transform airport checkpoint management from a rigid, reactive posture into a synchronized, demand-responsive operational system. By incorporating empirical lead-lag curves and connecting passenger ratios, security planners eliminate the persistent spatial and temporal mismatches that plague legacy time-of-day staffing tables. This prevents both the over-allocation of screening resources at major transfer hubs and the localized under-staffing caused by compressed departure banks. Furthermore, integrating live throughput feedback during convective weather disruptions resolves the vulnerability of purely schedule-driven forecasts, ensuring that checkpoint capacity rapidly recalibrates when flight delays cascade across the terminal. Rather than treating security screening as an isolated landside function, this unified predictive architecture bridges airline flight schedules, passenger arrival behaviors, and live checkpoint queuing dynamics to protect passenger throughput standards without inflating annual operating budgets.

## Recommendations for Future Research

Building upon the empirical findings and acknowledging the structural boundaries of this study, several critical recommendations for future research and methodological refinement are proposed. First, future predictive frameworks should incorporate extenuating external factors – such as severe meteorological disruptions, FAA Air Traffic Management Ground Delay Programs and ground stops, airline IT infrastructure outages, and tactical TSA staffing constraints – that introduce exogenous arrival volatility independent of published flight schedules. Second, future research should acquire more granular, high-resolution operational data; while a recognized limitation of this thesis was applying a single month of baseline data and monthly load factor aggregates down to hourly time horizons, incorporating longitudinal datasets spanning multiple seasons alongside flight-specific passenger booking profiles and minute-level throughput records would significantly improve predictive fidelity. Third, future investigations should look at more checkpoints by disaggregating beyond terminal-level complexes to model discrete security screening areas and dedicated lane modalities (such as standard screening, TSA PreCheck, and CLEAR), capturing localized passenger diversion and queue rebalancing dynamics. Finally, future research could benefit from focusing intensively on a single airport facility as an in-depth case study, allowing researchers to capture unique concourse geometries, carrier-specific bank timing structures, and local passenger show-up curves without the confounding variance present across diverse multi-airport cohorts.

## Conclusion

The primary purpose of this thesis was to evaluate and optimize predictive modeling frameworks – spanning deterministic flight schedule convolution, supervised machine learning, and dynamic two-stage hybrid architectures – to enhance airport security checkpoint capacity management and throughput volatility forecasting across diverse operational conditions. The empirical findings definitively confirmed the overarching asymmetric trade-off hypothesis (Hypothesis 1) and its constituent sub-hypotheses (Hypothesis 1a, 1b, and 1c), demonstrating that no single paradigm is universally superior across all operational regimes: supervised machine learning maximizes routine baseline accuracy (robustness, confirming Hypothesis 1a), dynamic hybrid feedback provides unmatched resilience during acute flight delays and convective disruption shocks (resilience, confirming Hypothesis 1b), and deterministic schedule baselines deliver superior cross-facility generalizability (generalizability, confirming Hypothesis 1c). Ultimately, these results illustrate that airport authorities and security planners can achieve substantial operational capacity optimization without capital-intensive physical expansions by transitioning from static, monolithic models to a synchronized, condition-responsive regime-switched forecasting architecture.

References

Adacher, L., & Flamini, M. (2020). Optimizing airport land side operations: Check-in, passengers’ minor flow and security checkpoints. Transportation Research Procedia, 47, 585–592. https://doi.org/10.1016/j.trpro.2020.03.135

Adacher, L., Flamini, M., Guaita, M., & Romano, D. (2017). A model to optimize the airport terminal departure operations. Transportation Research Procedia, 27, 856–863. https://doi.org/10.1016/j.trpro.2017.12.086

Adadi, A., & Berrada, M. (2018). Peeking inside the black-box: A survey on Explainable Artificial Intelligence (XAI). IEEE Access, 6, 52138–52160. https://doi.org/10.1109/ACCESS.2018.2870052

Adeke, P. (2018). Modelling of queuing process at airport check-in system: A case study of Manchester Airport. American Journal of Traffic and Transportation Engineering, 3(2), 23–29. https://doi.org/10.11648/j.ajtte.20180302.12

AlKheder, S., Alhadeyah, S., & Albaghli, Z. (2024). Simulation modeling of passengers flow at airport terminal: A case study of Kuwait International Airport. International Journal of Transportation Science and Technology, 13(2), 350–363. https://doi.org/10.1016/j.ijtst.2023.04.004

Alnowibet, K., Khireldin, A., Abdelawwad, M., & Wagdy Mohamed, A. (2022). Airport terminal building capacity planning: A case study of King Khalid International Airport (KKIA). Sustainability, 14(18), Article 11467. https://doi.org/10.3390/su141811467

Anagnostopoulou, A., Tolikas, D., Spyrou, E., Akac, A., & Kappatos, V. (2024). The analysis and AI solutions in aviation passenger flow: A systematic literature review. Smart Cities, 7(5), 2372–2398. https://doi.org/10.3390/smartcities7050094

Andersen, T. G., & Bollerslev, T. (1998). Answering the skeptics: Yes, standard volatility models do provide accurate forecasts. International Economic Review, 39(4), 885–905. https://doi.org/10.2307/2527343

Anupam, A., & Lawal, I. (2024). Forecasting air passenger travel: A case study of Norwegian aviation industry. Journal of Forecasting, 43(4), 1105–1123. https://doi.org/10.1002/for.3060

Araujo, G. E., & Repolho, H. M. (2015). Optimizing the airport check-in counter allocation problem. Journal of Air Transport Management, 47, 177–185. https://doi.org/10.1016/j.jairtraman.2015.06.002

Ateş, S., Koç, G., Koç, T., & Bolat, M. (2021). Departure passenger flow simulation: Case study on Istanbul Airport. Pamukkale University Journal of Engineering Sciences, 27(7), 896–906. https://doi.org/10.5505/pajes.2021.21852

Babu, C. N., & Reddy, B. E. (2014). A moving-average filter based hybrid ARIMA–ANN model for forecasting time series data. Applied Soft Computing, 23, 27–38. https://doi.org/10.1016/j.asoc.2014.05.028

Balliauw, M., & Onghena, E. (2020). Expanding airport capacity of cities under uncertainty: Strategic investment in capacity flexibility. Transportation Research Part A: Policy and Practice, 138, 262–282. https://doi.org/10.1016/j.tra.2020.06.003

Bießlich, P., Schacht, M., & Wenzel, S. (2014). Application of discrete-event simulation for the analysis of passenger flow at airport terminals. In Proceedings of the 2014 Winter Simulation Conference (pp. 2011–2022). IEEE. https://doi.org/10.1109/WSC.2014.7020047

Birolini, S., & Jacquillat, A. (2023). Day-ahead aircraft routing with data-driven primary delay predictions. Transportation Science, 57(5), 1163–1188. https://doi.org/10.1287/trsc.2023.1215

Blasco-Puyuelo, J., Burrieza-Galán, J., Cantú Ros, O. G., Herranz, R., & Mocholí, D. (2023). A machine learning approach to predict airport passenger queue times using operational data. Aerospace, 10(7), Article 592. https://doi.org/10.3390/aerospace10070592

Box, G. E. P., Jenkins, G. M., Reinsel, G. C., & Ljung, G. M. (2015). Time series analysis: Forecasting and control (5th ed.). John Wiley & Sons.

Brown, J. R., & Madhavan, P. (2011). Examining passenger flow choke points at airports using discrete event simulation. In Proceedings of the Human Factors and Ergonomics Society Annual Meeting (Vol. 55, No. 1, pp. 1827–1831). SAGE Publications. https://doi.org/10.1177/1071181311551381

Brun, A., Feron, E., Alam, S., & Delahaye, D. (2025). Schedule optimization and staff allocation for airport security checkpoints under stochastic passenger arrival. Journal of Air Transport Management, 123, Article 102715. https://doi.org/10.1016/j.jairtraman.2024.102715

Brunetta, L., Righi, L., & Andreatta, G. (1999). An operations research model for the evaluation of an airport terminal: SLAM (Simple Landside Aggregate Model). Computers & Operations Research, 26(4), 359–375. https://doi.org/10.1016/S0305-0548(98)00067-1

Bureau of Transportation Statistics. (2026). Airline on-time performance data. U.S. Department of Transportation. https://www.transtats.bts.gov/

Centre for Aviation. (2025). Airline industry completes full recovery with exceptional operational performance. CAPA - Centre for Aviation. https://centreforaviation.com/

Cheng, S., Zhang, Y., & Guo, Y. (2012). Theory of allocating and scheduling resources at airport passenger terminals: A review. Advanced Engineering Forum, 5, 66–70. https://doi.org/10.4028/www.scientific.net/AEF.5.66

Chiti, F., Fantacci, R., & Rizzo, A. (2018). An integrated software platform for airport queues prediction: A cognitive approach. IEEE Systems Journal, 13(2), 1957–1968. https://doi.org/10.1109/JSYST.2018.2868254

De Neufville, R., & Odoni, A. R. (2014). Airport systems: Planning, design, and management (2nd ed.). McGraw-Hill Education.

Di Mascio, P., Moretti, L., & Piacitelli, M. (2020). Airport landside sustainable capacity and level of service: A case study. Sustainability, 12(17), Article 7122. https://doi.org/10.3390/su12177122

Diaz-Gutierrez, J., Nazir, N., Longo, N., & Ranjbari, A. (2025). Mitigating airport passenger congestion through predictive model control and tactical lane allocation. Transportation Research Part C: Emerging Technologies, 171, Article 104950. https://doi.org/10.1016/j.trc.2024.104950

Diebold, F. X., & Mariano, R. S. (1995). Comparing predictive accuracy. Journal of Business & Economic Statistics, 13(3), 253–263. https://doi.org/10.1080/07350015.1995.10524599

Dönmez, K., Tükenmez, İ., & Çeçen, R. K. (2025). A novel stochastic matheuristic approach for the dynamic utilisation of arrival route structures: Modelling of Istanbul Airport point merge system. The Aeronautical Journal, 129(1331), 589–617. https://doi.org/10.1017/aer.2024.96

Ebert, A., Dutta, R., Mengersen, K., Mira, A., Ruggeri, F., & Wu, P. P.-Y. (2021). Likelihood-free parameter estimation for dynamic queueing networks: Case study of passenger flow in an international airport. Journal of the Royal Statistical Society: Series C (Applied Statistics), 70(3), 770–792. https://doi.org/10.1111/rssc.12480

Edwards, J. (2026, April 8). Digital twin technology for airport operations: Real-time simulation and predictive queue management. Airport Technology. https://www.airport-technology.com/features/digital-twins-airports/

Engle, R. (2001). GARCH 101: The use of ARCH/GARCH models in applied econometrics. Journal of Economic Perspectives, 15(4), 157–168. https://doi.org/10.1257/jep.15.4.157

Federal Aviation Administration. (2024). FAA aerospace forecasts: Fiscal years 2024–2044. U.S. Department of Transportation. https://www.faa.gov/data_research/aviation/aerospace_forecasts

Fernandes, E., & Pacheco, R. R. (2002). Efficient use of airport capacity. Transportation Research Part A: Policy and Practice, 36(3), 225–238. https://doi.org/10.1016/S0965-8564(00)00046-X

Gao, Y. (2022). Benchmarking the recovery of air travel demands for US airports during the COVID-19 pandemic. Journal of Air Transport Management, 102, Article 102229. https://doi.org/10.1016/j.jairtraman.2022.102229

Guizzi, G., Murino, T., & Romano, E. (2009). A discrete event simulation to model passenger flow in the airport terminal. In Proceedings of the 8th WSEAS International Conference on System Science and Simulation in Engineering (pp. 427–434). WSEAS.

Güner, S., & Seçkin Codal, K. (2024). Airport productivity and network centrality in the pandemic outbreak: Lessons from the Turkish airports. Journal of Air Transport Management, 115, Article 102552. https://doi.org/10.1016/j.jairtraman.2024.102552

Guo, J., Tong, X., Yang, Y., Yuan, J., & Xu, S. (2025). Resilience analysis of airport systems based on causal Bayesian networks and passenger propagation dynamics. Reliability Engineering & System Safety, 254, Article 110580. https://doi.org/10.1016/j.ress.2024.110580

Guo, X., Grushka-Cockayne, Y., & De Reyck, B. (2022). Forecasting airport transfer passenger flow using real-time flight status and itinerary data. Production and Operations Management, 31(5), 2112–2130. https://doi.org/10.1111/poms.13670

Had, P., Volt, J., & Stojić, S. (2025). Calculation of queue formation in airport security checks using hybrid random forest estimators. Transportation Letters, 17(2), 145–158. https://doi.org/10.1080/19427867.2024.2311450

Hansen, P. R., & Lunde, A. (2005). A forecast comparison of volatility models: Does anything beat a GARCH(1,1)? Journal of Applied Econometrics, 20(7), 873–889. https://doi.org/10.1002/jae.800

He, J., Li, Y., & Chao, Y. (2024). Research on prediction and optimization of airport express passenger flow using fused intelligence networks. Journal of Advanced Transportation, 2024, Article 8841295. https://doi.org/10.1155/2024/8841295

Hess, S., & Grbčić, A. (2019). The multiphase queuing system of the Rijeka Airport passenger terminal. Pomorstvo, 33(2), 154–160. https://doi.org/10.31217/p.33.2.5

Hewamalage, H., Bergmeir, C., & Bandara, K. (2021). Recurrent neural networks for time series forecasting: Current status and future directions. International Journal of Forecasting, 37(1), 388–427. https://doi.org/10.1016/j.ijforecast.2020.06.008

Hopfe, D. H., Lee, K., & Yu, C. (2024). Short-term forecasting airport passenger flow during periods of disruption using machine learning with exogenous variables. Transportation Research Record: Journal of the Transportation Research Board, 2678(6), 312–326. https://doi.org/10.1177/03611981231198544

Horie, M. (1985). Analysis of passenger flows in airport terminals. Journal of Airport Management, 10(2), 123–135.

Hyndman, R. J., & Athanasopoulos, G. (2018). Forecasting: Principles and practice (2nd ed.). OTexts.

International Air Transport Association. (2026, March 17). Air travel demand will more than double by 2040. https://www.iata.org/en/pressroom/2026-releases/2026-03-17-01/

International Civil Aviation Organization. (2024). Effects of novel coronavirus (COVID-19) on civil aviation: Economic impact analysis. https://www.icao.int/sustainability/Documents/COVID-19/ICAO_Coronavirus_Econ_Impact.pdf

Jenčová, E., Gajdušková, T., Jezný, M., & Hudák, P. (2025). Identification of bottlenecks in passenger handling processes at international airports using explainable machine learning. Applied Sciences, 15(3), Article 1142. https://doi.org/10.3390/app15031142

Jiang, B., Zhang, J., Fu, J., Ding, G., & Zhang, Y. (2024). Research on check-in baggage flow prediction in airport terminal based on deep spatio-temporal residual network. IEEE Access, 12, 45120–45132. https://doi.org/10.1109/ACCESS.2024.3381204

Kazda, A., Badanik, B., & Serrano, F. (2022). Pandemic vs. post-pandemic airport operations: Hard impact, slow recovery. Aerospace, 9(12), Article 810. https://doi.org/10.3390/aerospace9120810

Kingman, J. F. C. (1961). The single server queue in heavy traffic. Mathematical Proceedings of the Cambridge Philosophical Society, 57(4), 902–904. https://doi.org/10.1017/S0305004100036100

Lee, Y., Choi, S. C., Lee, K., & Cho, S. W. (2025). Dynamic rescheduling strategy for passenger congestion relief at airport checkpoints based on reinforcement learning. Computers & Industrial Engineering, 199, Article 110752. https://doi.org/10.1016/j.cie.2024.110752

Lemer, A. C. (1988). Measuring airport landside capacity. Transportation Research Record, 1199, 12–18. http://onlinepubs.trb.org/Onlinepubs/trr/1988/1199/1199-002.pdf

Leone, K., & Liu, R. (2011). Improving airport security screening checkpoint operations in the US via discrete-event simulation. Journal of Air Transport Management, 17(6), 358–361. https://doi.org/10.1016/j.jairtraman.2011.02.006

Li, L., Liu, Y., & Liu, X. (2017). Passenger flow forecasting research for airport terminal based on SARIMA model. In Proceedings of the 2017 International Conference on Computer Technology, Electronics and Communication (pp. 58–62). IEEE. https://doi.org/10.1109/ICCTEC.2017.00021

Li, X., de Groot, M., & Bäck, T. (2023). Using forecasting to evaluate the impact of COVID‐19 on passenger air transport demand. Decision Sciences, 54(4), 394–409. https://doi.org/10.1111/deci.12549

Li, Y., & Gao, G. (2023). Large-scale passenger behavior learning and prediction in airport terminals: A deep learning perspective. Journal of Air Transport Management, 107, Article 102341. https://doi.org/10.1016/j.jairtraman.2022.102341

Liao, M., Cheung, T. K. Y., Wong, C. W. H., & Zhang, A. (2025). Resilience in the face of disruptions: Assessing the impacts of COVID-19 and geopolitical conflicts on global airport connectivity. Journal of the Air Transport Research Society, 4, Article 100069. https://doi.org/10.1016/j.jatrs.2025.100069

Lin, L., Liu, X., Liu, X., Zhang, T., & Cao, Y. (2023). A prediction model to forecast passenger flow in airport terminal based on deep learning and actual flight operations. Aerospace, 10(4), Article 341. https://doi.org/10.3390/aerospace10040341

Lin, W. (2022). Atmospheric conditioning: Airport automation, labour and the COVID‐19 pandemic. Transactions of the Institute of British Geographers, 47(1), 214–228. https://doi.org/10.1111/tran.12499

Liu, Y. (2018). Research on airport security based on virtual queuing theory. Advances in Intelligent Systems Research, 161, 285–289. https://doi.org/10.2991/iccia-18.2018.57

Lu, C.-H., Zhou, H.-Q., & Wang, S.-H. (2018). Bottleneck detection of security checking process for airport based on generalized stochastic Petri nets. Journal of Central South University (Science and Technology), 49(5), 1290–1297. https://doi.org/10.11817/j.issn.1672-7207.2018.05.034

Marzuoli, A., Boidot, E., Feron, E., & Srivastava, A. (2019). Implementing and validating air passenger flow models at international airports: A data-driven approach. In Proceedings of the 8th International Conference on Research in Air Transportation (ICRAT) (pp. 1–8). FAA/Eurocontrol.

Mota, M. M., Scala, P., Bernardi, A. D., & Orozco, A. (2021). Restart: Analysis of post-COVID 19 capacity in security checkpoints at Mexico City Airport. Transportation Research Procedia, 59, 234–243. https://doi.org/10.1016/j.trpro.2021.11.115

Naji, M., Braytee, A., Al-Ani, A., Anaissi, A., Goyal, M., & Kennedy, P. J. (2020). Design of airport security checkpoint using multi-objective genetic algorithm and discrete-event simulation. IEEE Transactions on Intelligent Transportation Systems, 22(11), 7013–7024. https://doi.org/10.1109/TITS.2020.3003661

Nazir, N., Vasisht, S., Choudhury, S., Zoepf, S., & Dowling, C. (2022). Mitigating landside congestion in airport terminals via dynamic flight-to-gate assignment and stochastic queue modeling. Transportation Research Part C: Emerging Technologies, 142, Article 103780. https://doi.org/10.1016/j.trc.2022.103780

Nikoue, H., Marzuoli, A., Clarke, J.-P., Feron, E., & Peters, J. (2015). Passenger flow predictions and operational decision support at airport security checkpoints. In 15th AIAA Aviation Technology, Integration, and Operations Conference (Article 2931). AIAA. https://doi.org/10.2514/6.2015-2931

Nwofia, O., & Chung, C. A. (2013). A methodology for designing airports for enhanced security using computer simulation. Journal of Transportation Security, 6(2), 147–163. https://doi.org/10.1007/s12198-013-0108-7

OAG. (2026). Infographic: The busiest airports in the US. https://www.oag.com/blog/infographic-the-busiest-airports-in-the-us

Odoni, A. R. (1986). Stochastic, dynamic queuing models for an airport terminal or a network of terminals. In Transportation Research Board Special Report (No. 210, pp. 24–40). Transportation Research Board.

Olusanya, O., Obetta, J., Oyediram, M., & Elegbede, A. (2020). Developing an Arena simulation model for passenger flow at Muritala Muhammed Airport 2, Lagos, Nigeria. Journal of Applied Sciences and Environmental Management, 24(8), 1403–1409. https://doi.org/10.4314/jasem.v24i8.15

Oprea, C., Rosca, M., Rosca, E., Costea, I., Ilie, A., Dinu, O., & Ruscă, A. (2024). Analyzing passenger flows in airport terminals through discrete-event simulation. Sustainability, 16(4), Article 1625. https://doi.org/10.3390/su16041625

Orhan, İ., & Orhan, G. (2020). Modelling and managing airport passenger flow: A case of Hasan Polatkan Airport. Journal of Aviation, 4(2), 173–182. https://doi.org/10.30518/jav.786520

Orsini, F., Gastaldi, M., Mantecchini, L., & Rossi, R. (2019). Neural network models for passenger arrival forecasting in airport terminals. Transportation Research Procedia, 47, 593–600. https://doi.org/10.1016/j.trpro.2020.03.136

Ozores, C. (2026, April 29). Airports must monetize their assets to fund growth. ICF Aviation Insights. https://www.icf.com/insights/transportation/airports-monetize-assets

Palaşcă, A., & Stăncel, I. (2025). Poisson distribution for dynamic passenger management: An operational framework for airport check-in queues. Scientific Bulletin of Politehnica University of Timisoara, 70(2), 85–94. https://doi.org/10.59277/SBPUT.2025.2.08

Parizi, M. S., & Braaksma, J. P. (1994). Optimum design of airport enplaning curbside areas. Journal of Transportation Engineering, 120(4), 536–551. https://doi.org/10.1061/(ASCE)0733-947X(1994)120:4(536)

Parlar, M., Rodrigues, B., & Moosa, S. (2016). Event‐based allocation of airline check‐in counters: A queueing approach. Naval Research Logistics, 63(8), 652–668. https://doi.org/10.1002/nav.21727

Patrón, R., Scala, P., Mota, M., & Mendoza, A. (2021). Airport passenger flow prediction using simulation data farming and machine learning algorithms. Aerospace, 8(12), Article 395. https://doi.org/10.3390/aerospace8120395

Perez, E., Taunton, L., & Sefair, J. A. (2021). A simulation-optimization approach to improve the allocation of security screening resources at international airports. Computers & Industrial Engineering, 159, Article 107481. https://doi.org/10.1016/j.cie.2021.107481

Peterson, M. D., Bertsimas, D. J., & Odoni, A. R. (1995). Models and algorithms for transient queueing congestion at airports. Management Science, 41(8), 1279–1295. https://doi.org/10.1287/mnsc.41.8.1279

Ribeiro, N. A., Tay, J., Ng, W., & Birolini, S. (2025). Delay predictive analytics for airport capacity management: A physics-informed deep learning approach. Transportation Science, 59(1), 112–134. https://doi.org/10.1287/trsc.2024.0321

Saki, S., & Soori, M. (2026). Artificial intelligence, machine learning and deep learning in advanced passenger flow management: A comprehensive review. Journal of Air Transport Management, 124, Article 102742. https://doi.org/10.1016/j.jairtraman.2025.102742

Schultz, M., Luo, M., Lubig, D., Mota, M. M., & Scala, P. (2021). Covid-19-related challenges for new normality in airport terminal operations. In Proceedings of the 2021 Winter Simulation Conference (pp. 1–12). IEEE. https://doi.org/10.1109/WSC52266.2021.9715417

Schultz, T., & Fricke, H. (2011). Passenger flow modeling and simulation at airport terminals. Transportation Research Record, 2214(1), 101–108. https://doi.org/10.3141/2214-13

Solak, S., Clarke, J. P. B., Johnson, E. L., & Barnes, E. R. (2009). Optimization of airport terminal capacity allocation under demand uncertainty. Transportation Research Part B: Methodological, 43(5), 579–595. https://doi.org/10.1016/j.trb.2008.10.003

Sörensen, K. (2015). Metaheuristics—the metaphor exposed. International Transactions in Operational Research, 22(1), 3–18. https://doi.org/10.1111/itor.12001

Sun, X., Wandelt, S., & Zhang, A. (2022). COVID-19 pandemic and air transportation: Summary of recent research, policy consideration and future research directions. Transportation Research Interdisciplinary Perspectives, 16, Article 100718. https://doi.org/10.1016/j.trip.2022.100718

Sun, X., Wandelt, S., Zheng, C., & Zhang, A. (2021). COVID-19 pandemic and air transportation: Successfully managing the crisis through containment and government policies. Transport Policy, 106, 145–160. https://doi.org/10.1016/j.tranpol.2021.04.001

Tang, H., Yu, J., Lin, B., Geng, Y., Wang, Z., Chen, X., Yang, L., Lin, T., & Xiao, F. (2023). Airport terminal passenger forecast under the impact of COVID-19 outbreaks: A case study from China. Journal of Building Engineering, 65, Article 105740. https://doi.org/10.1016/j.jobe.2022.105740

Transportation Research Board. (2010). Airport passenger terminal planning and design (ACRP Report 40, Vols. 1 & 2). The National Academies Press. https://doi.org/10.17226/14427

Transportation Security Administration. (2026). FOIA electronic reading room. U.S. Department of Homeland Security. https://www.tsa.gov/foia-readingroom

Verki, H., Mamdoohi, A., & Saffarzadeh, M. (2013). Stochastic planning approach to airport passenger terminals capacity allocation. Journal of Advanced Transportation, 47(8), 738–750. https://doi.org/10.1002/atr.1225

Viaña, J., Cohen, K., Saunders, S., Marx, N., & Cobb, B. (2024). Explainable algorithm to predict passenger flow at airport security screening checkpoints. Transportation Research Part C: Emerging Technologies, 161, Article 104561. https://doi.org/10.1016/j.trc.2024.104561

Wang, C. (2018). A queueing analysis of a security-check system with two types of inspection channels in an airport terminal. Computers & Industrial Engineering, 125, 431–442. https://doi.org/10.1016/j.cie.2018.09.006

Wang, M. (2017). Application of the queuing theory in characterizing and optimizing the passenger flow at airport security checkpoints. American Journal of Traffic and Transportation Engineering, 2(6), 118–123. https://doi.org/10.11648/j.ajtte.20170206.14

Wang, Y., Jiang, W., Zhang, M., & Li, D. (2025). Airspace monitoring around airports using neural networks and causal inference on surveillance radar data. IEEE Transactions on Intelligent Transportation Systems, 26(1), 780–792. https://doi.org/10.1109/TITS.2024.3431102

Wei, Y. (2017). Optimization model of airport security screening based on queuing theory and cost-benefit analysis. In Proceedings of the 2017 International Conference on Economics, Finance and Statistics (ICEFS 2017) (pp. 214–218). Atlantis Press. https://doi.org/10.2991/icefs-17.2017.47

Whitt, W. (1993). Approximations for the GI/G/m queue. Production and Operations Management, 2(2), 114–161. https://doi.org/10.1111/j.1937-5956.1993.tb00094.x

Wu, P. P.-Y., Pitchforth, J., & Mengersen, K. (2014). A hybrid queue-based Bayesian network framework for passenger flow forecasting at international airports. PLoS ONE, 9(3), Article e91195. https://doi.org/10.1371/journal.pone.0091195

Wu, S. (2024). Research on airport passenger flow forecast based on PSO-BP neural network. In M. Mikut, et al. (Eds.), Proceedings of the 34th Workshop Computational Intelligence (pp. 115–128). KIT Scientific Publishing. https://doi.org/10.5445/KSP/1000174209

Wu, Y., Yang, J., Chen, X., Lin, Y., & Yang, H. (2024). Long-term airport network performance forecast: A multi-task learning approach. Transportation Research Part C: Emerging Technologies, 160, Article 104523. https://doi.org/10.1016/j.trc.2024.104523

Xia, Z., Li, B., Huang, H., Huang, L., Wang, X., & Li, J. (2020). An ensemble learning model for short-term airport passenger flow forecasting during holidays and extreme weather events. IEEE Access, 8, 189124–189136. https://doi.org/10.1109/ACCESS.2020.3031980

Yang, S., Tang, T., & Wang, T. (2022). How to raise the check-in efficiency at airport: A cooperative game theoretic and simulation approach. Journal of Advanced Transportation, 2022, Article 4153920. https://doi.org/10.1155/2022/4153920

Zhang, B., Wang, J., Liu, C., & Zhao, Y. (2012). Evaluating the technical efficiency of airport security and passenger processing resources using Fuzzy-DEA. Transport Policy, 24, 212–221. https://doi.org/10.1016/j.tranpol.2012.08.005

Zhang, X., Li, J., & Xiang, N. (2017). Airport security process optimization based on GSPN and queuing theory. In Proceedings of the 2017 2nd International Conference on Civil, Transportation and Environmental Engineering (ICCTE 2017) (pp. 382–387). Atlantis Press. https://doi.org/10.2991/iccte-17.2017.72
