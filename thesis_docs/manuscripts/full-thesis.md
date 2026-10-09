# Chapter I: Introduction

As commercial aviation navigates sustained post-pandemic passenger traffic expansion, air travel demand increasingly outpaces physical airport terminal infrastructure, rendering inefficient resource allocation a primary bottleneck across the National Airspace System (Adacher, Flamini, Guaita, & Romano, 2017). Prohibitive capital costs, municipal land constraints, and multi-year environmental reviews severely restrict physical terminal expansion (AlKheder et al., 2024; Balliauw & Onghena, 2020; De Neufville & Odoni, 2014; Ozores, 2026). Consequently, airport operators and federal security authorities must extract maximum operational throughput from fixed physical assets through software-driven predictive intelligence.

Commercial airport landside subsystems—ticketing lobbies, Transportation Security Administration (TSA) security checkpoints, and departure concourses—operate as a tightly coupled stochastic queuing network (De Neufville & Odoni, 2014). When passenger arrival surges saturate security screening lanes, lines spill backward into ticketing halls and concourses, inducing terminal gridlock, gate holds, delayed pushbacks, and missed flight connections across the national network (Adacher et al., 2017).

While predictive models are widely deployed to anticipate terminal demand, the systemic disruptions of the COVID-19 pandemic and subsequent recovery exposed critical vulnerabilities in traditional, accuracy-centric evaluation standards (Sun, Wandelt, & Zhang, 2022). Historically, airport flow forecasts were evaluated almost exclusively through clear-weather, undisturbed error metrics such as Root Mean Squared Error (RMSE) or Mean Absolute Percentage Error (MAPE). These conventional metrics evaluate performance solely during nominal operating conditions, implicitly assuming stationary demand and undisturbed flight operations. However, airport operations are characterized by severe non-linear disruptions: convective thunderstorm ground stops, winter freeze events, and rolling air traffic control gate holds. A model that achieves low mean forecast error during undisturbed operations may catastrophically collapse when flight delays cascade, generating false demand collapses or runaway queue backlogs (Li, Zhang, & Wang, 2023). Singular, undisturbed evaluation metrics are therefore fundamentally insufficient for selecting predictive models intended for volatile operational environments.

To resolve this gap, this study establishes a dynamic, multi-dimensional evaluation framework evaluating predictive models across three orthogonal operational dimensions:

- **Robustness (Routine Operational Accuracy)**: The ability of a model to deliver reliable, low-error baseline volatility forecasts during nominal on-time operations and ambient daily flight bank churn, minimizing routine Root Mean Squared Error ($RMSE_{\text{routine}}$) and satisfying Mean Absolute Scaled Error targets ($MASE_{\text{routine}} < 0.700$).

- **Resilience (Performance Under Severe Disruption)**: The capacity of a model to absorb severe exogenous shocks (such as summer convective ground delay programs or winter blizzards) without suffering runaway error inflation, maintaining a Disruption Error Multiplier ($R_{\text{MASE}} \approx 1.00$), minimizing disruption error ($MASE_{\text{shock}}$), and achieving rapid recovery ($TTR < 4.0\text{ hours}$).

- **Generalizability (Cross-Airport Transferability)**: The capability of a model architecture calibrated at one hub facility to transfer zero-shot across divergent terminal layouts and airline hub network topologies without requiring site-specific historical retraining, maintaining a Relative Transfer Ratio ($RTR \approx 1.00$) and minimal transfer error degradation ($\Delta MASE_{\text{transfer}} \le 10.0\%$).

This research systematically compares candidate modeling frameworks—spanning an empirical baseline control, deterministic flight schedule baselines, supervised machine learning decision trees, and dynamic two-stage hybrid architectures—to determine which framework excels across each dimension of the evaluation triad.

## Section 1: Significance of the Study

### Decoupling Flight Schedules from Passenger Show-Up Timing
A fundamental challenge in terminal capacity planning is the operational decoupling of airline flight schedules from actual passenger checkpoint arrivals. Published flight schedules indicate when aircraft depart the gate, not when passengers arrive at security screening. Passengers arrive according to empirical lead-time distributions 90 to 180 minutes prior to departure (Transportation Research Board [TRB], 2010), while airside connecting passengers bypass security checkpoints entirely. 

By integrating empirical ACRP Report 40 passenger show-up curves with origin-and-destination transfer deflators derived from Bureau of Transportation Statistics (BTS) DB1B ticket surveys, this study establishes the mathematical mechanisms that decouple landside security queue arrivals from airside gate movements. Furthermore, by demonstrating that checkpoint queue wait times scale quadratically with arrival volatility ($C_a^2$) under heavy-traffic queuing principles (Kingman, 1961; Whitt, 1993), this study shifts the analytical paradigm from static volume forecasting ($y_t$) to stochastic throughput volatility modeling ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$).

### Operational Value for Federal Security Directors and Airline Planners
This research provides actionable operational utility for both Transportation Security Administration leadership and airline hub operations planners. Federal Security Directors (FSDs) must schedule Transportation Security Officer (TSO) screening lane shifts days in advance, while dynamically reallocating lanes during day-of-operations flight delays. By identifying which forecasting techniques provide superior routine accuracy versus disruption resilience, this study delivers a transparent, regime-switched decision framework. Planners can deploy lightweight machine learning models for routine advance staffing, while activating dynamic hybrid error feedback during irregular operations to prevent checkpoint queue overflow and flight delays.

## Section 2: Statement of the Problem

### Post-Pandemic Volatility and Inadequacy of Pre-Pandemic Assumptions
Airport passenger arrivals and screening demands are inherently stochastic, driven by complex interactions between airline flight schedules, passenger behavioral variations, and airside operational delays (Cheng, Zhang, & Guo, 2012; Dönmez, Tükenmez, & Cecen, 2025). Contemporary passenger flow management tools frequently rely on static pre-pandemic planning assumptions, failing to accommodate the heightened volatility, erratic business travel patterns, and structural shifts characterizing post-pandemic commercial aviation (Ebert, Dutta, Mengersen, Mira, Ruggeri, & Wu, 2021; Hopfe, Schultz, & Fricke, 2024; Sun et al., 2022).

This misalignment between static capacity planning and fluctuating passenger arrival surges creates severe queuing bottlenecks at TSA screening checkpoints. When screening throughput drops below surge arrival rates, queues expand non-linearly, stranding ticketed travelers, inflating TSA wait times, and causing cascading aircraft departure delays.

### Absence of a Dynamic, Multi-Dimensional Evaluation Framework
Despite the vulnerability of terminal operations to systemic disruptions, the aviation sector lacks a standardized, multi-dimensional framework for evaluating predictive models beyond clear-weather point accuracy. Existing literature predominantly benchmarks models using static, single-metric criteria evaluated over calm historical periods. Because real-world airport operations fluctuate between nominal flow, ambient churn, and severe irregular operations (IROPS), deploying a model selected solely on baseline accuracy exposes airport authorities to catastrophic failure during severe flight delays. Without an adaptable evaluation framework that accounts for robustness, resilience, and generalizability, airport operators cannot determine which forecasting tool is suitable for distinct operational regimes.

## Section 3: Purpose Statement

### Objective Comparison of Forecasting Paradigms
The primary objective of this quantitative study is to systematically evaluate and compare distinct predictive modeling paradigms—representing an empirical baseline control, deterministic operational baselines, supervised machine learning decision trees, and dynamic two-stage hybrid models—for forecasting airport passenger security screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$). Rather than seeking a single, universally optimal model, this research examines the asymmetric performance trade-offs inherent in each architecture when tested across routine operations, severe convective weather shocks, and zero-shot spatial transfer across airport facilities.

### Capacity Optimization via Software Intelligence vs. Capital Infrastructure
By establishing the empirical relationships connecting airside flight schedules, flight delay dispersion, and landside screening throughput, this study demonstrates how software intelligence and predictive analytics can optimize terminal screening capacity without requiring costly brick-and-mortar terminal expansion. The ultimate deliverable is a regime-switched operational playbook empowering airport authorities and security directors to deploy the appropriate predictive paradigm based on real-time operational conditions.

## Section 4: Research Question

### Verbatim Primary Operational Inquiry
This study is guided by the following primary research inquiry:

> **Which predictive modeling frameworks—spanning an empirical baseline control, deterministic flight schedule baselines, supervised machine learning models, and dynamic two-stage hybrids—are most effective for forecasting airport passenger security screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) when prioritizing robustness (routine operational accuracy), resilience (stability under convective weather and delay disruptions), or generalizability (cross-airport portability across terminal layouts) as the primary operational evaluation metric?**

### Core Research Hypothesis ($H_1$ - Master Asymmetric Trade-Off Hypothesis)
Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), benchmarked against an empirical daily persistence baseline control, **no individual architecture will prove universally superior across all three evaluation dimensions**. Rather, inherent operational properties establish distinct, asymmetric performance trade-offs:

- **$H_{1a}$ (Robustness Target: Lowest $RMSE_{\text{routine}}$ and $MASE_{\text{routine}} < 0.700$)**: Supervised machine learning (Model 2) and two-stage dynamic hybrids (Model 3) will successfully achieve the robustness target ($MASE_{\text{routine}} < 0.700$) under nominal operating conditions by capturing non-linear flight schedule dispersion and lead-lag passenger arrivals, whereas naive persistence (Baseline Control) and deterministic flight schedules (Model 1) will fail this threshold ($MASE \ge 0.94$). Supervised machine learning (Model 2) will deliver the computationally lightweight, Pareto-efficient routine solution with zero online feedback latency.

- **$H_{1b}$ (Resilience Target: $R_{\text{RMSE}} \approx 1.00 \ (R_{\text{MASE}} \approx 1.00)$, Lowest $MASE_{\text{shock}}$, and $TTR < 4.0\text{ hours}$)**: The Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience target due to recursive 1-step error innovation feedback ($e_{t-1}$). Static supervised machine learning (Model 2) will experience severe performance degradation ($R \ge 2.0$) resulting from the Empty Checkpoint Fallacy during flight ground delays, while deterministic baselines (Model 1) will remain blind to downline delay cascades.

- **$H_{1c}$ (Generalizability Target: $RTR \approx 1.00$ and $\Delta MASE_{\text{transfer}} \le 10.0\%$)**: The Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target ($RTR \approx 1.00, \Delta MASE \le 10.0\%$) under zero-shot spatial transfer without local retraining because flight schedule convolution is invariant to local terminal geometry. Conversely, the Dynamic Hybrid (Model 3) will decisively fail the generalizability target ($RTR \gg 1.00, \Delta MASE > 10.0\%$) due to decision tree terminal geometry overfitting.

## Section 5: Delimitations

### Geographic Scope
This study evaluates commercial air traffic and security screening operations within the contiguous United States, restricted to the candidate universe of the **Top 25 commercial airfields** ranked by FAA passenger enplanements (capturing 67.2% of nationwide domestic operations). Purposive multi-tier filtering further narrows this universe to the **9-Airport Experimental Cohort** across 12 carrier-exclusive screening complexes (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL).

### Temporal Scope
The multi-source analytical warehouse spans **January 1, 2019 through December 31, 2025** (7 continuous years; 61,344 calendar hours; 42.06 million conformed fact records). Model development is delimited to the verified post-pandemic operational equilibrium beginning **May 1, 2022** (Candidate B demarcation; 44 continuous months), reserving the full 12-month calendar year of **2025** (365 days; 8,760 hours; 72,053 complex-level observations) as an untouched out-of-time holdout evaluation window.

### Data Feed Boundaries
The investigation exclusively uses publicly available and FOIA-disclosed federal aviation datasets:
1. TSA FOIA hourly screening logs disaggregated by physical screening lane.
2. BTS On-Time Flight Performance Form 234 flight-level domestic departure records.
3. BTS Form 41 Schedule T-100 Segment capacity and load factor data.
4. BTS DB1B/DB1C 10% origin-and-destination ticket coupon surveys.

### Metric Standards
Model performance is evaluated using standardized statistical and operational metrics: Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE; relative to daily persistence), the Disruption Error Multiplier ($R_{\text{MASE}}$), Time-to-Recovery ($TTR$), the Relative Transfer Ratio ($RTR$), and Diebold-Mariano ($DM$) loss differential tests.

## Section 6: Limitations and Assumptions

### Checkpoint Staffing and Lane Configuration Opacity
Due to federal security regulations, real-time Transportation Security Officer (TSO) shift rosters, active lane counts per 15-minute interval, and manual queue snake reconfigurations are confidential. The methodology controls for this operational opacity by aggregating lane-level counts into dedicated terminal complex throughput totals ($Y_{kt}$), transforming administrative lane-switching noise into a smooth, stable demand signal.

### Passenger Checked-Baggage and Pre-Security Dwell
Airline ticketing counter transactions and checked-baggage drop dwell times are proprietary to operating carriers. Pre-security passenger lead times are modeled through empirical passenger show-up curves derived from **ACRP Report 40 (*Airport Passenger Terminal Planning and Design*)** guidelines.

### Connecting Transfer Ratio Stability
Airside connecting ratios are estimated using quarterly BTS DB1B ticket coupon surveys. The methodology assumes that connecting ratios remain stable across monthly operating blocks within specific carrier-terminal complexes.

### Operational Exogeneity
Severe convective weather disruptions, FAA ground stops, and flight cancellations reported in BTS Form 234 are treated as exogenous airside inputs capturing terminal apron congestion and National Airspace System traffic management initiatives.

## Section 7: List of Acronyms

To facilitate precise technical interpretation across commercial aviation operations, federal security oversight, and econometric modeling, Table 1.1 defines the primary operational acronyms and abbreviations utilized throughout this manuscript. For the complete catalog of over 100 domain terms, refer to the master index in [acronyms.md](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/manuscripts/acronyms.md).

### Table 1.1
*Master Operational Acronyms and Federal Reporting Classifications*

| Acronym | Formal Expansion | Operational Category | Primary Thesis Application |
| :--- | :--- | :--- | :--- |
| **A14** | Air Carrier On-Time Reporting Benchmark (14-min tolerance) | Regulatory Reference | FAA/DOT on-time arrival threshold defining Nominal On-Time Baseline regime ($DepDelay < 15$m). |
| **AA** | American Airlines | Commercial Air Carrier | Network legacy carrier evaluated across dedicated complexes at DFW, PHL, and ORD. |
| **ACRP** | Airport Cooperative Research Program | Research Literature | TRB program; Report 40 provides empirical passenger show-up curves ($t+1, t+2, t+3$). |
| **BTS** | Bureau of Transportation Statistics | Federal Data Provider | USDOT operating administration publishing Form 234, Form 41 T-100, and DB1B survey data. |
| **CKPT** | Checkpoint | Terminal Infrastructure | Physical passenger security screening complex operated by TSA. |
| **CV** | Coefficient of Variation | Evaluation Metric | Scale-free relative volatility metric ($\sigma / \mu$) capturing passenger arrival burstiness. |
| **$CV_{\text{TSA}}$** | Coefficient of Variation of TSA Throughput | Primary Dependent Target | Primary scale-free dependent variable measuring intraday passenger throughput volatility. |
| **CVI** | Coupled Volatility Index | Operational Interaction | Interaction term ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$) quantifying landside-airside compounding disruption. |
| **DB1B** | Airline Origin and Destination Survey (Data Bank 1B) | Federal Data Provider | 10% ticket sample used to calculate connecting passenger ratios and isolate originating traffic. |
| **DL** | Delta Air Lines | Commercial Air Carrier | Network legacy carrier evaluated across dedicated complexes at DTW, LGA, and BOS. |
| **DM** | Diebold-Mariano Test Statistic | Statistical Evaluation | Non-parametric loss differential test verifying pairwise forecast significance under autocorrelation. |
| **DOW** | Day of Week | Operational Regime | Cyclical weekly calendar variation controlling for business vs. leisure travel waves. |
| **FAA** | Federal Aviation Administration | Regulatory Authority | Agency overseeing National Airspace System air traffic management and airport certification. |
| **FOIA** | Freedom of Information Act | Data Source | Statutory disclosure (5 U.S.C. § 552) through which 7 years of hourly lane screening logs were obtained. |
| **FSD** | Federal Security Director | Operational Authority | Senior TSA official exercising operational authority over checkpoint lane staffing and configuration. |
| **GBDT** | Gradient-Boosted Decision Trees | Predictive Modeling | Supervised machine learning ensemble architecture implemented in Model 2. |
| **GDP** | Ground Delay Program | Air Traffic Management | FAA traffic management initiative holding departing aircraft at origin airports during adverse conditions. |
| **HOD** | Hour of Day | Temporal Demarcation | Discrete 24-hour diurnal cycle capturing morning, midday, and evening passenger screening banks. |
| **IROPS** | Irregular Operations | Operational Regime | Severe disruptions ($DepDelay \ge 45$m or $Cancels \ge 5$) governing Dimension 2 (Resilience). |
| **MASE** | Mean Absolute Scaled Error | Evaluation Metric | Scale-independent accuracy metric relative to naive diurnal persistence ($MASE < 1.000$ indicates skill). |
| **NAS** | National Airspace System | Airspace Network | Network of U.S. airspace, navigation facilities, airports, and air traffic management initiatives. |
| **OTP** | On-Time Performance | Federal Data Provider | BTS Form 234 flight-by-flight operational database tracking delays, taxi queues, and cancellations. |
| **PreCheck** | TSA PreCheck Expedited Screening | Security Operations | Dedicated screening lanes with expedited divestiture protocols yielding higher processing throughput. |
| **$R_{\text{MASE}}$** | Disruption Error Multiplier | Resilience Metric | Ratio of shock error to nominal error ($MASE_{\text{shock}} / MASE_{\text{nominal}}$); values near 1.00 denote resilience. |
| **RMSE** | Root Mean Squared Error | Evaluation Metric | Quadratic loss metric penalizing large forecast errors in physical throughput units (pax/hr). |
| **RTR** | Relative Transfer Ratio | Generalizability Metric | Ratio of transfer error to in-sample error ($RMSE_{\text{transfer}} / RMSE_{\text{in-sample}}$); values near 1.00 denote portability. |
| **T-100** | BTS Form 41 Schedule T-100 Segment Data | Federal Data Provider | Monthly carrier route reporting providing aircraft seat capacity, flown passengers, and load factors. |
| **TSA** | Transportation Security Administration | Federal Security Agency | Department of Homeland Security agency managing civil aviation security screening checkpoints. |
| **TSO** | Transportation Security Officer | Frontline Personnel | Federal security personnel staffing checkpoint lanes and operating screening technologies. |
| **TTR** | Time-to-Recovery | Resilience Metric | Operational elapsed hours required for model error residuals to return to baseline bounds post-shock. |
| **UA** | United Airlines | Commercial Air Carrier | Network legacy carrier evaluated across dedicated complexes at EWR, IAH, and LAX. |
| **WN** | Southwest Airlines | Commercial Air Carrier | Point-to-point carrier excluded during 4-tier filtering due to bimodal arrival mixture and shared concourses. |

*Note.* Adapted from master acronym catalog in `thesis_docs/manuscripts/acronyms.md`. Primary modeling paradigms include Baseline Control (Diurnal Persistence), Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model).

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

In summary, this literature review establishes that modeling airport security checkpoint passenger flow requires moving beyond static, volume-centric assumptions toward dynamic, volatility-informed paradigms. Commercial air terminals operate as tightly coupled queuing networks where flight bank clustering, connecting passenger flows, and severe convective weather induce acute arrival burstiness that scales queue delays quadratically under Kingman's principles ($C_a^2$). The literature demonstrates that isolated analytical approaches are insufficient: deterministic schedules cannot adapt to tactical delay cascades, micro-simulations demand prohibitive calibration overhead, and unconstrained machine learning models fall victim to the Empty Checkpoint Fallacy during severe operational shocks. Conversely, hybrid predictive frameworks that couple deterministic flight schedule baselines with machine learning residual adjustments and recursive error feedback synthesize the structural stability of schedule dynamics with the empirical flexibility of data-driven learning. Evaluating these candidate architectures across the operational triad of nominal robustness, disruption resilience, and zero-shot generalizability provides the theoretical foundation for the empirical methodology and experimental design formulated in Chapter III.

---

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

Three essential data hygiene protocols were established during warehouse staging to guarantee econometric and machine learning validity:
1. **Spatial Key Resolution and Unidentified Airport Isolation**: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (*dim_checkpoint*). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (*airportId* = 0, flagged with *airportMissing* = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce *airportMissing* = 0 and *airportId* > 0.
2. **Scheduled Checkpoint Closures vs. Missing Sensor Data**: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p = 1.3$, which naturally accommodates real zero counts without producing impossible negative passenger estimates or requiring artificial data smoothing).
3. **Advance vs. Tactical Cancellation Causality**: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting (the error of using future information that an airport operations manager would not possess in real time), advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.

### Temporal Boundaries
A core methodological requirement of this thesis is that **defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset**. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on idiosyncratic facility characteristics rather than learning generalizable aviation temporal dynamics.

#### Post-Pandemic Regime Selection and Structural Break Analysis
The seven-year dataset captures two unprecedented macroeconomic disruptions: the COVID-19 pandemic demand collapse (2020–2021) and the post-pandemic operational rebound (2022–2025). To identify the point at which commercial aviation resumed structural equilibrium, rolling Welch's $t$-tests, Cumulative Sum (CUSUM) structural break tests, and longitudinal correlation metrics were computed across the Top 25 airfields. Table 4.3a contrasts the candidate temporal demarcation baselines.

Table 4.3a  
*Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network*

| Evaluation Criteria | Candidate A: Mature Post-Pandemic | Candidate B: Early Post-Mask Regime *(Selected)* |
| :--- | :--- | :--- |
| Start Date | January 1, 2023 | May 1, 2022 (RECOMMENDED) |
| Statistical Demarcation Rationale | Rolling Welch's $t$-test variance convergence | CUSUM structural break stabilization; Mask Mandate Repeal |
| Training Span | 24 Months (2023-01 to 2024-12) | 32 Months (2022-05 to 2024-12; 20 mo train / 12 mo val) |
| Holdout Test Span | 12 Months (2025 Full-Year Holdout) | 12 Months (2025 Full-Year Holdout) |
| Robustness Impact | Excellent baseline stability; limited historical depth | Superior: Captures two complete annual seasonal cycles |
| Resilience Impact | Misses Winter Storm Elliott (Dec 2022) | Superior: Encapsulates severe winter freeze and summer storms |
| Generalizability Impact | Narrower training variance across spoke airfields | Superior: 404,324 candidate multi-facility hourly records |
| Coupling Rebound ($R^2$) | $R^2 = 0.323$ (Macro scheduled-to-TSA daily) | $R^2$ rebounds from 0.368 (COVID) to 0.306–0.323 (Equilibrium) |

Structural break tests confirmed **May 1, 2022** as the optimal demarcation point for empirical model development:
1. **Federal Transit Mask Mandate Repeal**: The nationwide vacatur of federal transit mask requirements on April 18, 2022 restored unconstrained business and leisure travel behavior. By May 1, 2022, load factors recovered to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stability**: During the acute pandemic (2020–2021), the correlation between scheduled flights and checkpoint throughput spiked to an artificial $r = 0.607$ ($R^2 = 36.85\%$) because airline capacity cuts mirrored strict travel bans. In the post-May 2022 equilibrium, the relationship stabilized to $r = 0.553$ ($R^2 = 30.61\%$), reflecting normalized booking curves.
3. **Partitioning Design**: Candidate B establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations; 215,562 facility-level observations). A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.

### Defining Seasonality
Just as temporal boundaries must be established on the complete Top 25 network, **defining seasonality requires capturing the full variance of nationwide commercial aviation**. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks.

#### Annual Seasonal Regimes and Coupled Volatility
Airport operational stress is not uniform across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b). The Coupled Volatility Index is defined as:
$$\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$$

Table 4.3b  
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)*

| Seasonal Regime | Operational Regime Description | Calendar Days ($N$) | Share of Days (%) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) | Cancellation Rate (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| 1_OFF_PEAK | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | 27.85 | 9.85 min | 18.00% | 0.89% |
| 2_MID_PEAK | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | 32.38 | 15.14 min | 23.23% | 1.36% |
| 3_PEAK | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | 39.36 | 24.17 min | 31.04% | 3.16% |
| 4_HOLIDAY | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | 33.07 | 16.51 min | 24.33% | 1.82% |

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

#### Day-of-Week Cyclical Dynamics and Archetypes
Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes (Table 4.4a):
1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($19.44\%$ and $20.05\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

Table 4.4a  
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

### TSA and OTP Throughput Data
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
