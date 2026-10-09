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
