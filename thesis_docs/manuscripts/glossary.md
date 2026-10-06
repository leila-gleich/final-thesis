# Glossary of Technical Terms by Operational Category

This glossary defines the operational concepts, aviation data systems, statistical metrics, and predictive modeling methods used across Chapters I through V of this manuscript. In accordance with the *Publication Manual of the American Psychological Association* (7th ed.; APA, 2020) guidelines for academic dissertations and technical manuscripts, terms are organized hierarchically into six operational categories that mirror the functional workflow of commercial airport operations and predictive analytics.

To support airport Federal Security Directors (FSDs), operational planners, and transportation researchers without an advanced background in machine learning, each definition is written in plain, intuitive language and grounded in airport operations. A central contribution of this research is establishing that terminal queue stability and passenger wait times are governed not simply by expected passenger counts, but by the **volatility of checkpoint throughput** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$). Terms within each category are arranged in strict alphabetical order. The Alphabetical Quick-Finder Index below provides immediate navigation to all entries.

## Alphabetical Quick-Finder Index

| Technical Term | Category Classification |
| :--- | :--- |
| [4-Model Canonical Evaluation Suite](#4-model-canonical-evaluation-suite) | Predictive Modeling |
| [84-Cell Operational Condition Matrix ($\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H}$)](#84-cell-operational-condition-matrix-g-s-d-h) | Volatility & Filtering |
| [Advance Flight Cancellation](#advance-flight-cancellation) | Datasets & Data Hygiene |
| [Air Traffic Control (ATC)](#air-traffic-control-atc) | Infrastructure, Agencies & Programs |
| [Airborne Flight Duration](#airborne-flight-duration) | Datasets & Data Hygiene |
| [Airport Cooperative Research Program (ACRP) Report 40](#airport-cooperative-research-program-acrp-report-40) | Queuing & Passenger Dynamics |
| [Airport Operations Center (AOC)](#airport-operations-center-aoc) | Infrastructure, Agencies & Programs |
| [Airside](#airside) | Infrastructure, Agencies & Programs |
| [Allen-Cunneen / Kingman Volatility Queuing Approximation ($W_q \propto C_a^2$)](#allen-cunneen-kingman-volatility-queuing-approximation-wq-ca2) | Queuing & Passenger Dynamics |
| [Autoregressive Integrated Moving Average (ARIMA / SARIMA / SARIMAX)](#autoregressive-integrated-moving-average-arima-sarima-sarimax) | Predictive Modeling |
| [Baseline Control Benchmark (Daily Persistence)](#baseline-control-benchmark-daily-persistence) | Predictive Modeling |
| [Available Seats per Route-Month](#available-seats-per-route-month) | Datasets & Data Hygiene |
| [Batch Arrival Dynamics](#batch-arrival-dynamics) | Queuing & Passenger Dynamics |
| [Bimodal Arrival Mixture](#bimodal-arrival-mixture) | Queuing & Passenger Dynamics |
| [BTS DB1B / DB1C Origin-Destination Ticket Surveys](#bts-db1b-db1c-origin-destination-ticket-surveys) | Datasets & Data Hygiene |
| [BTS Form 234 (On-Time Performance / OTP)](#bts-form-234-on-time-performance-otp) | Datasets & Data Hygiene |
| [BTS Form 41 Schedule T-100 Domestic Segment Data](#bts-form-41-schedule-t-100-domestic-segment-data) | Datasets & Data Hygiene |
| [Bureau of Transportation Statistics (BTS)](#bureau-of-transportation-statistics-bts) | Datasets & Data Hygiene |
| [Candidate B Demarcation](#candidate-b-demarcation) | Datasets & Data Hygiene |
| [Change in MASE on Transfer ($\Delta\text{MASE}$)](#change-in-mase-on-transfer-deltamase) | Evaluation & Statistics |
| [Checkpoint Fingerprinting Algorithm](#checkpoint-fingerprinting-algorithm) | Datasets & Data Hygiene |
| [Checkpoint Lane Throughput ($y_{k,l,t}$)](#checkpoint-lane-throughput-yklt) | Queuing & Passenger Dynamics |
| [Coefficient of Determination ($R^2$)](#coefficient-of-determination-r-squared) | Evaluation & Statistics |
| [Coefficient of Variation ($CV_{\text{TSA}}$)](#coefficient-of-variation-cvtsa) | Volatility & Filtering |
| [Conformal Quantile Prediction Bounds](#conformal-quantile-prediction-bounds) | Evaluation & Statistics |
| [Connecting Passenger Deflator](#connecting-passenger-deflator) | Queuing & Passenger Dynamics |
| [Connecting Passenger Ratio](#connecting-passenger-ratio) | Queuing & Passenger Dynamics |
| [Consensus Factor Weight ($W_j$)](#consensus-factor-weight-wj) | Volatility & Filtering |
| [Convolved Passenger Show-Up Curve](#convolved-passenger-show-up-curve) | Queuing & Passenger Dynamics |
| [Coupled Volatility Index ($\text{CVI}_d$)](#coupled-volatility-index-cvid) | Volatility & Filtering |
| [Credential Authentication Technology (CAT)](#credential-authentication-technology-cat) | Infrastructure, Agencies & Programs |
| [Cumulative Sum (CUSUM) Structural Break Test](#cumulative-sum-cusum-structural-break-test) | Evaluation & Statistics |
| [Dedicated Terminal Screening Complex](#dedicated-terminal-screening-complex) | Queuing & Passenger Dynamics |
| [Diebold-Mariano ($DM$) Test](#diebold-mariano-dm-test) | Evaluation & Statistics |
| [Discrete Event Simulation (DES)](#discrete-event-simulation-des) | Predictive Modeling |
| [Disruption Error Multiplier ($R_{\text{MASE}}$)](#disruption-error-multiplier-rmase) | Evaluation & Statistics |
| [Diurnal Non-Consecutive Dual Turbulence Peaks](#diurnal-non-consecutive-dual-turbulence-peaks) | Volatility & Filtering |
| [Divestiture](#divestiture) | Queuing & Passenger Dynamics |
| [Empty Checkpoint Fallacy](#empty-checkpoint-fallacy) | Queuing & Passenger Dynamics |
| [Federal Aviation Administration (FAA)](#federal-aviation-administration-faa) | Infrastructure, Agencies & Programs |
| [Federal Security Director (FSD)](#federal-security-director-fsd) | Infrastructure, Agencies & Programs |
| [Flight Bank (Departure Wave)](#flight-bank-departure-wave) | Queuing & Passenger Dynamics |
| [Flight Departure Delay ($\text{DepDelay}$)](#flight-departure-delay-depdelay) | Datasets & Data Hygiene |
| [Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)](#flight-departure-delay-dispersion-delay-d) | Volatility & Filtering |
| [Flight Departure Delay Volatility ($\text{CV}_{\text{delay}}$)](#flight-departure-delay-volatility-cvdelay) | Volatility & Filtering |
| [Freedom of Information Act (FOIA)](#freedom-of-information-act-foia) | Infrastructure, Agencies & Programs |
| [Gated Recurrent Unit (GRU)](#gated-recurrent-unit-gru) | Predictive Modeling |
| [Generalizability (Evaluation Dimension 3)](#generalizability-evaluation-dimension-3) | Evaluation & Statistics |
| [Generalizability Target ($\text{RTR} = 1.00, \Delta\text{MASE} \le 10\%$)](#generalizability-target-rtr-100-deltamase-10) | Evaluation & Statistics |
| [Gradient-Boosted Decision Trees (GBM / HistGBM)](#gradient-boosted-decision-trees-gbm-histgbm) | Predictive Modeling |
| [Ground Delay Program (GDP)](#ground-delay-program-gdp) | Infrastructure, Agencies & Programs |
| [Hierarchical Domain Variance Decomposition](#hierarchical-domain-variance-decomposition) | Volatility & Filtering |
| [Hub-and-Spoke Network](#hub-and-spoke-network) | Queuing & Passenger Dynamics |
| [Hub Disconnect](#hub-disconnect) | Queuing & Passenger Dynamics |
| [Kalman Filtering / State-Space Innovation Feedback](#kalman-filtering-state-space-innovation-feedback) | Predictive Modeling |
| [Kaplan-Meier Survival Analysis](#kaplan-meier-survival-analysis) | Evaluation & Statistics |
| [Landside](#landside) | Infrastructure, Agencies & Programs |
| [Lead-Lag Asynchrony](#lead-lag-asynchrony) | Queuing & Passenger Dynamics |
| [Level of Service (LOS)](#level-of-service-los) | Queuing & Passenger Dynamics |
| [Load Factor](#load-factor) | Volatility & Filtering |
| [Long Short-Term Memory (LSTM)](#long-short-term-memory-lstm) | Predictive Modeling |
| [Lookahead Bias](#lookahead-bias) | Datasets & Data Hygiene |
| [Master Asymmetric Trade-Off Matrix](#master-asymmetric-trade-off-matrix) | Evaluation & Statistics |
| [Mean Absolute Error (MAE)](#mean-absolute-error-mae) | Evaluation & Statistics |
| [Mean Absolute Percentage Error (MAPE)](#mean-absolute-percentage-error-mape) | Evaluation & Statistics |
| [Mean Absolute Scaled Error (MASE)](#mean-absolute-scaled-error-mase) | Evaluation & Statistics |
| [Mean Forecast Bias](#mean-forecast-bias) | Evaluation & Statistics |
| [Model 1: Deterministic Flight Schedule Model](#model-1-deterministic-flight-schedule-model-physical-baseline) | Predictive Modeling |
| [Model 2: Supervised Machine Learning Model](#model-2-supervised-machine-learning-model-flight-operations--delays) | Predictive Modeling |
| [Model 3: Dynamic Two-Stage Hybrid Model](#model-3-dynamic-two-stage-hybrid-model-schedule--real-time-feedback) | Predictive Modeling |
| [Multi-Carrier Schedule Collinearity](#multi-carrier-schedule-collinearity) | Queuing & Passenger Dynamics |
| [Multi-Day Temporal Volatility ($\sigma_{\text{TSA, 7d}}$)](#multi-day-temporal-volatility-tsa-7d) | Volatility & Filtering |
| [National Airspace System (NAS)](#national-airspace-system-nas) | Infrastructure, Agencies & Programs |
| [Nine-Airport Balanced Experimental Cohort](#nine-airport-balanced-experimental-cohort) | Volatility & Filtering |
| [Non-Homogeneous Poisson Process (NHPP)](#non-homogeneous-poisson-process-nhpp) | Predictive Modeling |
| [Operational Separation Buffer](#operational-separation-buffer) | Datasets & Data Hygiene |
| [Operational Turbulence Shock Index ($T_{dow}(h)$)](#operational-turbulence-shock-index-tdowh) | Volatility & Filtering |
| [Origin and Destination (O&D)](#origin-and-destination-od) | Queuing & Passenger Dynamics |
| [Originating Passenger (Local Originating Demand)](#originating-passenger-local-originating-demand) | Queuing & Passenger Dynamics |
| [Out-of-Time Holdout Evaluation](#out-of-time-holdout-evaluation) | Evaluation & Statistics |
| [Overnight Structural Zero](#overnight-structural-zero) | Datasets & Data Hygiene |
| [Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)](#peak-surge-shock-ratio-stsa-d) | Volatility & Filtering |
| [Purposive Four-Tiered Filtering Funnel](#purposive-four-tiered-filtering-funnel) | Volatility & Filtering |
| [Queuing Theory](#queuing-theory) | Queuing & Passenger Dynamics |
| [Regime-Switched Gated Inference Engine](#regime-switched-gated-inference-engine) | Predictive Modeling |
| [Relative Transfer Ratio (RTR)](#relative-transfer-ratio-rtr) | Evaluation & Statistics |
| [Resilience (Evaluation Dimension 2)](#resilience-evaluation-dimension-2) | Evaluation & Statistics |
| [Resilience Target ($R_{\text{RMSE}} \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$)](#resilience-target-rrmse-100-lowest-maseshock) | Evaluation & Statistics |
| [Robustness (Evaluation Dimension 1)](#robustness-evaluation-dimension-1) | Evaluation & Statistics |
| [Robustness Target ($\text{RMSE}_{\text{routine}}$ Lowest, $\text{MASE}_{\text{routine}} < 0.70$)](#robustness-target-rmseroutine-lowest-maseroutine-070) | Evaluation & Statistics |
| [Root Mean Squared Error (RMSE)](#root-mean-squared-error-rmse) | Evaluation & Statistics |
| [Runway Taxi-Out Queue Time](#runway-taxi-out-queue-time) | Datasets & Data Hygiene |
| [Scale-Free Diurnal Arrival Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$)](#scale-free-diurnal-arrival-volatility-cvtsa-hr) | Volatility & Filtering |
| [Second-Order Stochastic Moment](#second-order-stochastic-moment) | Volatility & Filtering |
| [Show-Up Curve](#show-up-curve) | Queuing & Passenger Dynamics |
| [Tactical Flight Cancellation](#tactical-flight-cancellation) | Datasets & Data Hygiene |
| [Terminal Radar Approach Control (TRACON)](#terminal-radar-approach-control-tracon) | Infrastructure, Agencies & Programs |
| [Throughput Volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$)](#throughput-volatility-tsa-and-cvtsa) | Volatility & Filtering |
| [Time-to-Recovery ($\text{TTR}_{\text{shock}}$)](#time-to-recovery-ttrshock) | Evaluation & Statistics |
| [Traffic Intensity ($\rho(t)$)](#traffic-intensity-t) | Queuing & Passenger Dynamics |
| [Transfer Error Penalty ($\Delta_{\text{transfer}}$)](#transfer-error-penalty-transfer) | Evaluation & Statistics |
| [Transportation Security Administration (TSA)](#transportation-security-administration-tsa) | Infrastructure, Agencies & Programs |
| [Transportation Security Officer (TSO)](#transportation-security-officer-tso) | Infrastructure, Agencies & Programs |
| [TSA PreCheck](#tsa-precheck) | Infrastructure, Agencies & Programs |
| [Tweedie Compound Poisson Distribution](#tweedie-compound-poisson-distribution) | Predictive Modeling |
| [Ultra-Low-Cost Carrier (ULCC)](#ultra-low-cost-carrier-ulcc) | Infrastructure, Agencies & Programs |
| [Values versus Volatility Paradigm](#values-versus-volatility-paradigm) | Volatility & Filtering |
| [Welch's $t$-Test](#welchs-t-test) | Evaluation & Statistics |
| [Wilcoxon Signed-Rank Test](#wilcoxon-signed-rank-test) | Evaluation & Statistics |
| [Zero-Flight Intercept Test](#zero-flight-intercept-test) | Evaluation & Statistics |
| [Zero-Shot Transfer Deployment](#zero-shot-transfer-deployment) | Evaluation & Statistics |

---

## Category 1: Aviation Infrastructure, Federal Agencies, and Programs

*This category defines the physical airport terminal zones, federal regulatory bodies, operational coordination command centers, and traveler security programs that govern commercial aviation across the National Airspace System.*

### Air Traffic Control (ATC)
The Federal Aviation Administration (FAA) service responsible for directing aircraft safely on runways, taxiways, and throughout the national airspace system, managing ground traffic flow and en-route flight separations.

### Airport Operations Center (AOC)
The central facility at a commercial airport where airport staff, airline representatives, and security personnel coordinate daily operations, monitoring passenger terminal flow, gate assignments, runway conditions, and emergency responses.

### Airside
The secure area of an airport terminal located past the passenger security screening checkpoints. Airside facilities include departure concourses, passenger boarding gates, concession shops, aircraft ramps, taxiways, and runways. Once passengers cross into the airside area, they do not pass through security again unless they exit the secure perimeter.

### Credential Authentication Technology (CAT)
Digital identity scanners deployed at TSA checkpoint entrances that scan a traveler's photo identification to confirm flight reservations directly against airline manifest databases, without requiring a paper or mobile boarding pass.

### Federal Aviation Administration (FAA)
The federal agency within the U.S. Department of Transportation responsible for the safety, regulation, and air traffic control management of all civil aviation in the United States.

### Federal Security Director (FSD)
The senior Transportation Security Administration official stationed at an airport, responsible for overseeing screening personnel, managing lane configurations, and maintaining terminal security standards.

### Freedom of Information Act (FOIA)
A federal public-records law (5 U.S.C. § 552) through which the multi-year dataset of hourly passenger screening volumes per checkpoint lane was disclosed by the Transportation Security Administration for this study.

### Ground Delay Program (GDP)
An air traffic management initiative implemented by the FAA that holds aircraft on the ground at their departure airports when bad weather or capacity constraints reduce the number of planes that can safely land at their destination airport.

### Landside
The publicly accessible areas of an airport terminal located before the security screening checkpoints. Landside facilities include curbside passenger drop-off zones, airline ticketing and baggage check counters, and pre-security waiting areas.

### National Airspace System (NAS)
The comprehensive network of United States airspace, air navigation facilities, airports, air traffic control towers, and operational regulations overseen by the FAA.

### Terminal Radar Approach Control (TRACON)
An FAA air traffic control facility that guides aircraft within a 30- to 50-mile radius of busy metropolitan airports, sequencing arrivals and departures between airport control towers and high-altitude flight routes (e.g., the New York TRACON managing EWR, LGA, and JFK).

### Transportation Security Administration (TSA)
The federal agency within the U.S. Department of Homeland Security responsible for civil aviation security, passenger screening, and baggage inspection across all commercial U.S. airports.

### Transportation Security Officer (TSO)
A federal security officer employed by the TSA who conducts passenger identity verification, manages checkpoint queue lanes, coaches passenger divestiture, and operates security screening equipment.

### TSA PreCheck
An expedited screening program administered by the TSA for pre-approved, vetted travelers. PreCheck lanes process passengers faster because travelers are not required to remove shoes, light outerwear, laptops, or travel-sized liquids.

### Ultra-Low-Cost Carrier (ULCC)
A category of budget airlines (such as Spirit or Frontier) that unbundle airfares and charge separate fees for carry-on bags and seat selection. ULCCs were excluded from the core modeling cohort to prevent their unique baggage and boarding practices from confounding legacy airline passenger comparisons.

---

## Category 2: Federal Aviation Datasets, Data Hygiene, and Conformance

*This category covers the official federal aviation data sources, data hygiene protocols, timeline integrity standards, and relational warehouse conformance rules used across the multi-source 2019–2025 study baseline.*

### Advance Flight Cancellation
A flight cancellation announced by an airline more than 24 hours before scheduled departure. Because passengers receive early notification and do not travel to the airport, advance cancellations are removed from scheduled seat counts so models do not falsely predict passenger demand that will never arrive.

### Airborne Flight Duration
The total elapsed flying time, in minutes, from when an aircraft lifts off the runway at the departure airport (wheels-off) to when its tires touch the runway at the arrival airport (wheels-on), recorded in Bureau of Transportation Statistics (BTS) Form 234 records.

### Available Seats per Route-Month
A monthly capacity measure reported in BTS Schedule T-100 data representing the total passenger seats scheduled by an airline between two specific airports over a calendar month.

### BTS DB1B / DB1C Origin-Destination Ticket Surveys
The Airline Origin and Destination Survey, a quarterly 10% random sample of all airline ticket itineraries collected by the Bureau of Transportation Statistics. In this study, it is used to determine the exact proportion of passengers who are merely connecting between flights airside versus true local passengers who begin their trip at the airport and pass through security checkpoints.

### BTS Form 234 (On-Time Performance / OTP)
A monthly flight-level database published by the Bureau of Transportation Statistics tracking every scheduled domestic flight by major carriers. It records scheduled and actual departure times, tarmac taxi-out delays, flight cancellations, and the causes of delays (such as weather, carrier issues, or air traffic control).

### BTS Form 41 Schedule T-100 Domestic Segment Data
A monthly federal database of airline capacity and traffic that records the number of departing flights, aircraft seats, transported passengers, and load factors for all domestic route segments flown by commercial carriers.

### Bureau of Transportation Statistics (BTS)
A statistical agency within the U.S. Department of Transportation (USDOT) that collects, verifies, and publishes national aviation data, including flight on-time performance, monthly passenger volumes, and airline ticket surveys.

### Candidate B Demarcation
The post-pandemic start date selected for model training and evaluation, spanning May 1, 2022 through December 31, 2025. This date was chosen because federal transportation mask mandates were vacated in late April 2022, marking the return of normalized, stable passenger travel habits and booking curves.

### Checkpoint Fingerprinting Algorithm
A data-cleaning procedure developed to resolve ambiguous or corrupted airport codes in raw TSA log files. It matched unique physical checkpoint names against known terminal maps to restore valid records, while isolating unidentifiable records to prevent the creation of false "phantom" airport totals.

### Flight Departure Delay ($\text{DepDelay}$)
The difference, in minutes, between an aircraft's actual gate pushback time and its scheduled departure time. Flights pushing back 15 minutes or more after schedule are officially classified by the FAA and BTS as significantly delayed.

### Lookahead Bias
A serious modeling error that occurs when information from the future is accidentally fed into a forecast. For example, using the *actual* flight departure delay at 18:00 to forecast passenger volume at 16:00 is impossible in real life, because airport staff do not know the exact future delay two hours in advance. Models must rely only on information available at the time of the forecast.

### Operational Separation Buffer
A seven-day pause placed between the training data (2022–2023) and validation data (2024) to ensure that multi-day storm disruptions and cascading delays from late December do not artificially leak into the next evaluation period.

### Overnight Structural Zero
A recorded passenger count of exactly zero that occurs because a security checkpoint is physically closed during the night (typically 00:00 to 03:59), representing a true physical closure rather than a missing sensor reading.

### Runway Taxi-Out Queue Time
The time, in minutes, that an aircraft spends taxiing from its departure gate to the runway before taking off (BTS Form 234). Long taxi-out times indicate tarmac congestion and runway queues.

### Tactical Flight Cancellation
A flight cancellation enacted within two hours of scheduled departure. These flights are kept in passenger demand calculations because affected travelers have already arrived at the terminal and cleared security before the airline cancels the flight.

---

## Category 3: Terminal Queuing Dynamics and Passenger Arrival Behavior

*This category details the physical, temporal, and behavioral dynamics of passenger movement through airport terminals, including passenger arrival show-up curves, airline flight bank waves, connecting passenger transfers, and queuing bottlenecks.*

### Airport Cooperative Research Program (ACRP) Report 40
A foundational airport planning guidebook titled *Airport Passenger Terminal Planning and Design*, published by the Transportation Research Board (2010). It provides empirical guidelines for passenger terminal planning, including the standard observation that domestic airline passengers typically arrive at security checkpoints 90 to 120 minutes before their scheduled flight departure time.

### Allen-Cunneen / Kingman Volatility Queuing Approximation ($W_q \propto C_a^2$)
A foundational queuing theory formulation governing non-Poisson ($G/G/s$) service facilities such as airport security screening checkpoints. It proves that expected passenger wait times ($W_q$) do not scale merely with average arrival rate ($\lambda$), but escalate linearly with the **squared coefficient of variation of arrival times ($C_a^2$)**:
$$W_q \approx \left( \frac{\rho^{\sqrt{2(s+1)}-1}}{s(1-\rho)} \right) \left( \frac{C_a^2 + C_s^2}{2} \right) \frac{1}{\mu}$$
This mathematical reality establishes why predicting **throughput volatility** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) is the vital operational imperative for airport planners: as lane utilization approaches capacity ($\rho \to 1.0$), arrival volatility generates runaway queue spikes, lane starvation, and downline flight boarding delays ($r = +0.4375, p < 0.05$).

### Batch Arrival Dynamics
The tendency of airline passengers to arrive at airport checkpoints in concentrated "waves" rather than a steady, continuous trickle. These waves are caused by airline flight schedules, which cluster flight departures into tight morning and evening banks, resulting in sudden surges of passengers arriving at security within short 30- to 60-minute windows.

### Bimodal Arrival Mixture
A two-peaked passenger arrival pattern observed among Southwest Airlines (WN) travelers. Because Southwest historically used an open-seating system (boarding groups A, B, and C) and allowed two free checked bags, passengers tended to arrive in two separate groups: early arrivals (averaging 135 minutes before departure) seeking prime boarding positions, and late business travelers with carry-ons (averaging 65 minutes before departure). This dual-peaked pattern contrasts with the single-peaked arrival curve of legacy airlines.

### Checkpoint Lane Throughput ($y_{k,l,t}$)
The number of passengers processed through an individual physical screening lane $l$ within terminal complex $k$ during a single one-hour period $t$.

### Connecting Passenger Deflator
A mathematical correction factor, calculated as $(1 - \text{Connecting Ratio})$, applied to scheduled airline seats to subtract passengers who are simply transferring between flights airside. Because these passengers never pass through landside security checkpoints, removing them prevents severe over-prediction of checkpoint demand.

### Connecting Passenger Ratio
The percentage of arriving airline passengers who transfer to another flight airside without exiting through security. At major connecting hub airports (such as Charlotte at 76.0% or Atlanta at 70.1%), more than two-thirds of all passengers never enter the airport's security screening checkpoints.

### Convolved Passenger Show-Up Curve
A mathematical representation of passenger arrival timing that spreads scheduled flight departures across the two to three hours before takeoff. Based on empirical ACRP Report 40 guidelines, departing seats are distributed across lead horizons: approximately 35% of passengers arrive one hour before departure, 50% arrive two hours before, and 15% arrive three hours before.

### Dedicated Terminal Screening Complex
A security checkpoint area that exclusively serves flights for a single airline or alliance (for example, Terminal C at LGA serving Delta Air Lines). Because only one carrier's flights use the checkpoint, the relationship between that carrier's flight schedules and security wait lines can be analyzed without interference from other airlines.

### Divestiture
The physical step at an airport security checkpoint where passengers place carry-on luggage, outerwear, shoes, laptops, and liquids into bins for X-ray or computed tomography (CT) inspection.

### Empty Checkpoint Fallacy
A systematic forecasting failure that occurs when standard machine learning models rely solely on delayed flight departure times. For example, if an 18:00 flight is delayed until 23:00 due to weather, a naive model expects the checkpoint to be empty at 16:30. In reality, passengers arrived at the terminal according to their original ticketed schedule and are waiting in security lines, causing the model to severely under-predict checkpoint demand.

### Flight Bank (Departure Wave)
A coordinated flight scheduling practice in which an airline schedules dozens of arrivals to land within a short period, followed by a tight 45- to 90-minute wave of departing flights. This allows connecting passengers to transfer between flights with minimal layover time.

### Hub-and-Spoke Network
An airline route strategy that connects multiple smaller "spoke" cities through a central "hub" airport. Passengers from various origin cities fly into the hub, transfer to connecting gates, and continue to their final destinations.

### Hub Disconnect
The planning error of assuming that every departing airline seat corresponds to a passenger passing through landside security checkpoints. At major connecting hubs, over half of departing passengers transfer between gates airside and never enter the security queue.

### Lead-Lag Asynchrony
The natural time gap between passenger security screening and flight departures. Passenger screening volume is a *leading indicator* that peaks 90 to 120 minutes before flights depart, whereas flight delays are a *lagging consequence* of aircraft turnaround bottlenecks that accumulate later in the day. Treating flight schedules and checkpoint demand as happening at the same time introduces significant forecast error.

### Level of Service (LOS)
Industry-standard performance targets established by airport authorities and the International Air Transport Association (IATA) governing passenger comfort, space per traveler, and maximum acceptable wait times at terminal checkpoints.

### Multi-Carrier Schedule Collinearity
An operational condition that occurs when competing airlines in a shared terminal schedule their flight departures at the exact same times (e.g., both scheduling departure banks at 08:00 and 17:00). In shared checkpoints, this makes it mathematically impossible to tell how many passengers in line belong to each individual airline.

### Origin and Destination (O&D)
A standard airline industry classification distinguishing the true beginning and end points of a passenger's complete journey from intermediate hub connecting stops.

### Originating Passenger (Local Originating Demand)
A passenger who begins their journey at the local metropolitan airport. These passengers arrive from the street, enter the landside terminal, check luggage, and must pass through security screening.

### Queuing Theory
The mathematical study of waiting in line. It models the relationships between passenger arrival rates ($\lambda$), screening lane processing speed ($\mu$), and the number of open lanes ($c$) to calculate line lengths, wait times, and queue backlogs.

### Show-Up Curve
The empirical distribution describing how many minutes or hours in advance of flight departure passengers arrive at airport security checkpoints. In domestic commercial aviation, the peak arrival window occurs between 90 and 120 minutes before flight departure.

### Traffic Intensity ($\rho(t)$)
A fundamental queuing metric defined as the ratio of passenger arrival rate to screening capacity:
$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$
When traffic intensity approaches 1.0 (or 100%), screening lanes are saturated, meaning any additional arriving passenger immediately creates a growing queue.

---

## Category 4: Operational Volatility, Seasonality, and Experimental Filtering

*This category encompasses the mathematical indices, cyclical volatility metrics, and purposive sampling funnels used to quantify airport operational turbulence, evaluate feature values versus feature volatility, and isolate unconfounded research cohorts.*

### 84-Cell Operational Condition Matrix ($\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H}$)
A structured grid used to organize airport data into 84 distinct operational scenarios before training and testing forecasting models. Rather than treating all days the same, the data is grouped by four seasonal periods ($\mathcal{S}$: winter lull, spring ramp, summer storms, and holidays), seven days of the week ($\mathcal{D}$: Monday through Sunday), and three times of day ($\mathcal{H}$: overnight lull, midday steady flow, and peak rush hours), giving $4 \times 7 \times 3 = 84$ unique operating conditions. This ensures models are tested fairly across all real-world airport conditions without small-sample distortion (83 of 84 conditions have at least 50 historical observations).

### Coefficient of Variation ($CV_{\text{TSA}}$)
A standard measure of relative volatility calculated by dividing the standard deviation by the mean ($\sigma / \mu$). In this study, within-day $CV_{\text{TSA}}$ measures how "spiky" or uneven passenger screening demand is throughout a 24-hour day. A high $CV$ indicates sharp morning or evening rushes separated by quiet valleys, while a low $CV$ indicates an even, steady flow.

### Consensus Factor Weight ($W_j$)
A synthesized predictive contribution metric (ranging from 0% to 100%) that aggregates variable importance across regularized linear models (Ridge, Lasso, Elastic Net), tree-based ensembles (Random Forest MDI, Gradient Boosted Gain), and out-of-fold permutation importance. In Chapter IV, it establishes the empirical ranking of all 24 Bureau of Transportation Statistics On-Time Performance (OTP) operational attributes for forecasting TSA throughput volatility.

### Coupled Volatility Index ($\text{CVI}_d$)
A daily operational turbulence score calculated by multiplying the landside passenger arrival variation ($CV_{\text{TSA}}$) by the airside flight departure delay spread ($\sigma_{\text{Delay}}$):
$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$
This index identifies days when both landside passenger surges and airside flight delays occur simultaneously, signaling severe operational stress across the airport.

### Diurnal Non-Consecutive Dual Turbulence Peaks
The empirical finding that commercial airport operational volatility concentrates in two distinct daily periods: a morning rush (05:00–08:00) driven by high passenger screening surges while flights depart on time, and an evening disruption period (14:00–22:00) driven by cascading flight delays across the national airspace system even as passenger arrivals decline.

### Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)
The standard deviation of departure delays across all domestic flights on a given day. Rather than looking only at the average delay, this metric measures how widely scattered flight delays are across the schedule, capturing the severity of delay cascades across the airport network.

### Flight Departure Delay Volatility ($\text{CV}_{\text{delay}}$)
The coefficient of variation of departure delays across scheduled flights. Across the Top 25 U.S. commercial airfields, delay volatility is the single strongest operational predictor of landside checkpoint throughput volatility ($r = +0.4373, R^2 = 19.13\%, p = 0.0288$). Conversely, raw delay minutes exhibit zero correlation ($r = -0.0620, p = 0.769$).

### Hierarchical Domain Variance Decomposition
The empirical grouping of 24 OTP attributes into five functional operational domains to assess their collective explanatory share for passenger throughput volatility: Schedule Scale & Density (64.47%), Tactical Cancellations (16.48%), Network Buffers & Gauge (7.85%), Flight Delay Dynamics (7.00%), and Surface Taxi Queues (4.21%).

### Load Factor
The percentage of available passenger seats filled by paying travelers on a flight or route segment (BTS Schedule T-100), calculated by dividing passenger miles by available seat miles.

### Multi-Day Temporal Volatility ($\sigma_{\text{TSA, 7d}}$)
The rolling 7-day standard deviation of daily passenger throughput (measured in passengers per day). It quantifies medium-term passenger flow turbulence caused by severe winter storms, convective ground stops, and multi-day cancellation cascades.

### Nine-Airport Balanced Experimental Cohort
The selected group of nine commercial hub airports (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL) encompassing 12 dedicated terminal screening complexes across American Airlines, Delta Air Lines, and United Airlines. This cohort provides a balanced matrix for comparing how models perform across different airlines and airport layouts.

### Operational Turbulence Shock Index ($T_{dow}(h)$)
A diurnal formula that calculates how turbulent each hour of the day is, based on both the spread of passenger security volume and the severity of flight departure delays. It automatically categorizes hours into Off-Peak (overnight lull, $T < 0.35$), Mid-Peak (midday steady flow, $0.35 \le T < 0.75$), and Peak (morning rushes and evening delay cascades, $T \ge 0.75$).

### Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)
The ratio of the single busiest hour of passenger throughput on a given day to that day's average hourly volume:
$$S_{\text{TSA}, d} = \frac{\max(y_h)}{\mu_d}$$
It identifies days when passenger arrivals are heavily concentrated into an acute rush hour.

### Purposive Four-Tiered Filtering Funnel
The sequential screening process used in Chapter III to isolate clean, unconfounded airport data:
1. *Macro Filter*: Selects the Top 25 large commercial airfields where checkpoints routinely experience peak-hour passenger congestion ($\rho(t) \to 1.0$).
2. *Meso Filter*: Requires concurrent operations by legacy airlines (American, Delta, United) while removing Southwest Airlines bimodal boarding variations.
3. *Micro Filter*: Isolates dedicated single-airline checkpoints, eliminating multi-carrier scheduling overlap.
4. *Factorial Cohort*: Balances the final sample across airlines and terminal layout types.

### Scale-Free Diurnal Arrival Volatility ($CV_{\text{TSA, hr}} = \sigma / \mu$)
Within-day hourly passenger arrival volatility normalized by average daily flow. By removing the baseline size of the airport, this scale-free metric isolates genuine arrival burstiness and queue surge spikiness.

### Second-Order Stochastic Moment
In statistical forecasting, the first moment represents the expected value or mean volume ($\mu = E[Y]$), while the second central moment represents the variance or volatility ($\sigma^2 = E[(Y - \mu)^2]$). This thesis specifically models and predicts the second moment of TSA checkpoint operations.

### Throughput Volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$)
The primary predictive target of this thesis, measuring the dispersion, burstiness, and temporal irregularity of passenger security screening demand across hours of the day ($\sigma_{\text{TSA, hr}}$, in pax/hr), scale-free arrival ratios ($CV_{\text{TSA, hr}}$), or multi-day rolling periods ($\sigma_{\text{TSA, 7d}}$, in pax/day).

### Values versus Volatility Paradigm
The central methodological comparison evaluating whether forecasting TSA throughput volatility requires tracking the *values* (levels, volumes, and counts) of OTP features, the *volatility* (dispersion, standard deviations, and coefficients of variation) of those features, or a dual *hybrid/combined* representation.

---

## Category 5: Predictive Modeling Paradigms and Architectures

*This category covers the benchmark forecasting models, decision-tree machine learning algorithms, time-series baselines, and dynamic cyber-physical hybrid methods evaluated for forecasting passenger throughput volatility across Chapters III, IV, and V.*

### The Candidate Predictive Models and Baseline Control
The definitive suite of three candidate forecasting models representing distinct operational paradigms, evaluated against an empirical daily persistence baseline control:
1. *Baseline Control*: Diurnal Volatility Naive Persistence benchmark ($y_{t-24}$).
2. *Model 1 (Deterministic Flight Schedule Model)*: Derived from published flight schedules convolved across empirical ACRP Report 40 passenger show-up curves.
3. *Model 2 (Supervised Machine Learning Model)*: Supervised decision-tree model combining flight schedule dispersion and 24 BTS OTP operational attributes (delays, cancellations, taxi queues).
4. *Model 3 (Dynamic Two-Stage Hybrid Model)*: Two-stage sequential model combining schedule baselines with live 1-step error innovation feedback ($e_{t-1}$).

### Autoregressive Integrated Moving Average (ARIMA / SARIMA / SARIMAX)
A standard statistical time-series forecasting method. In plain terms, it predicts future values using a combination of recent past values (autoregression) and recent forecast errors (moving average). In volatility forecasting, seasonal SARIMA models capture recurring daily (24-hour) and weekly (168-hour) baseline volatility cycles.

### Baseline Control Benchmark (Daily Persistence)
The canonical baseline control benchmark that assumes checkpoint throughput volatility today will be identical to volatility observed during the exact same period yesterday ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$). Establishes the scale-free reference standard ($\text{MASE} \equiv 1.000$).

### Discrete Event Simulation (DES)
A computer simulation method that models the movement of individual passengers through each step of an airport terminal (e.g., waiting in line, ticket scanning, removing shoes, body scanning, and gathering belongings). While detailed, DES requires extensive computing time and detailed lane staffing data that are not publicly available in real time.

### Gated Recurrent Unit (GRU)
A type of advanced neural network designed to analyze time-series sequences. While capable of learning complex temporal patterns, it operates as a "black box" that is difficult for airport managers to interpret and tends to overfit to the layout of specific airports.

### Gradient-Boosted Decision Trees (GBM / HistGBM)
An automated machine learning method that builds a sequence of simple, rule-based decision trees. In throughput volatility modeling, trees capture complex non-linear interactions between flight schedule bank dispersion, tactical flight cancellations, and airside delay turbulence.

### Kalman Filtering / Live Error Innovation Feedback
A real-time error-correction tracking method. In volatility forecasting, it functions like an intelligent thermostat: if actual checkpoint queue turbulence exceeds schedule-based expectations, the system feeds the 1-step residual error ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) directly into the next hour's forecast, preventing runaway queue collapses during severe flight delays.

### Long Short-Term Memory (LSTM)
A specialized neural network architecture designed to learn long sequences of time-series data. Although widely used in computer science research, it requires massive amounts of training data, functions as an opaque "black box," and often memorizes airport-specific terminal layouts rather than general travel patterns.

### Model 1: Deterministic Flight Schedule Model (Physical Baseline)
Derives predicted passenger screening volatility directly from published airline flight departure banks convolved across empirical ACRP Report 40 passenger arrival curves ($t+1, t+2, t+3$). It operates as a deterministic physical baseline without requiring statistical machine learning or airside delay telemetry, proving highly portable across airports.

### Model 2: Supervised Machine Learning Model (Flight Operations & Delays)
A supervised decision-tree regressor trained on convolved flight departures and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) attributes (incorporating schedule dispersion, tactical flight cancellations, prior-hour delay turbulence, and taxi-out queues). Achieves optimal routine operational efficiency ($\text{MASE} \le 0.70$) with zero real-time feedback latency.

### Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)
A sequential two-stage forecasting framework that combines recurring flight schedule cycles with live real-time error feedback. In Stage 1, recurring daily and weekly flight schedules capture baseline passenger rhythms. In Stage 2, decision trees estimate residual volatility shocks caused by flight delays, utilizing live 1-step error feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the checkpoint floor to achieve decisive resilience during severe convective disruptions ($\text{TTR} = 2.8\text{h}, R_{\text{MASE}} = 1.05$).

### Non-Homogeneous Poisson Process (NHPP)
A standard queuing model where arrival rates change over the course of the day (e.g., higher in the morning, lower at night) but still assumes that each arriving passenger enters the line independently of all others.

### Regime-Switched Gated Inference Engine (The Airport Operator's Playbook)
A recommended operational decision framework for airport command centers that monitors real-time airport turbulence: deploying the fast, automated Supervised Machine Learning Model (Model 2) during routine operations, and automatically engaging the Dynamic Two-Stage Hybrid Model (Model 3) with live error feedback during severe convective storms and ground delay programs.

### Tweedie Compound Poisson Distribution
A statistical distribution used in generalized linear modeling that handles positive continuous numbers while accommodating exact zeros. In airport checkpoint modeling, it ensures non-negative predictions and properly handles overnight structural closures.

---

## Category 6: Operational Evaluation Dimensions, Forecast Metrics, and Statistical Tests

*This category defines the multi-dimensional evaluation criteria (robustness, resilience, and generalizability), quantitative accuracy metrics, and formal hypothesis tests used to assess model performance in predicting throughput volatility.*

### Change in MASE on Transfer ($\Delta\text{MASE}$)
A generalizability metric quantifying the degradation in forecast skill when a volatility model is deployed zero-shot to an unfamiliar airport facility:
$$\Delta\text{MASE} = \left( \frac{\text{MASE}_{\text{transfer}} - \text{MASE}_{\text{in-sample}}}{\text{MASE}_{\text{in-sample}}} \right) \times 100\%$$
A shift $\le 10.0\%$ indicates robust cross-facility stability, whereas shifts $> 20.0\%$ indicate severe local overfitting.

### Coefficient of Determination ($R^2$)
A standard statistical metric ranging from 0.0 to 1.0 (or 0% to 100%) that measures the proportion of variance in throughput volatility successfully explained by the forecast model.

### Conformal Quantile Prediction Bounds
A statistical method that provides a reliable safety buffer around a volatility forecast. Rather than predicting only the expected volatility, the model calculates an 85th-percentile upper bound ($\hat{y}_{0.85}$). Airport security planners can use this bound to establish dynamic lane buffers ($c(t) = \lceil \hat{y}_{0.85} / \mu \rceil$) that absorb sudden passenger surges without long queue lines.

### Cumulative Sum (CUSUM) Structural Break Test
A statistical monitoring test that tracks cumulative prediction errors over time to determine when a major structural shift has occurred. In this study, it was used to identify when post-COVID air travel volatility stabilized.

### Diebold-Mariano ($DM$) Test
A standard statistical test used to verify whether the difference in forecast accuracy between two volatility models is statistically significant ($p < 0.001$), confirming that machine learning improvements are genuine rather than random chance.

### Disruption Error Multiplier ($R_{\text{MASE}}$)
A resilience metric that measures how much a forecasting model's error increases during severe flight disruptions compared to routine operating days:
$$R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
A score of 1.0 to 1.3 indicates a resilient model whose accuracy remains stable during disruptions, whereas a score above 2.0 indicates a fragile model whose errors double during storms.

### Generalizability (Evaluation Dimension 3)
One of the three primary performance dimensions in this study. It evaluates whether a volatility forecasting model calibrated on one airport terminal can be deployed to a different airport without needing to be retrained on local historical data.

### Generalizability Target ($\text{RTR} = 1.00, \Delta\text{MASE} \le 10\%$)
The stated academic performance target for cross-airport transferability: achieving a Relative Transfer Ratio ($\text{RTR}$) of approximately 1.00 and a change in MASE upon transfer ($\Delta\text{MASE}$) less than or equal to 10.0%. Successfully met by the Deterministic Flight Schedule Model (Model 1, $\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$), but failed by the Dynamic Hybrid (Model 3, $\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$) due to decision tree terminal geometry overfitting.

### Kaplan-Meier Survival Analysis
A statistical method used to calculate how long it takes for an event to occur. In this study, it measures the Time-to-Recovery ($\text{TTR}$): how many hours it takes for a forecasting model's prediction error to return to normal baseline levels after a major flight disruption event.

### Master Asymmetric Trade-Off Matrix
The master synthesis evaluation matrix (Table 5.4) that formalizes Hypothesis 1 by benchmarking the candidate models (Model 1, Model 2, Model 3) and baseline control across Robustness, Resilience, and Generalizability against explicit academic targets. Conclusively demonstrates that no single model dominates across all dimensions: Model 3 wins Resilience, Model 1 wins Generalizability, and Model 2 wins Routine Pareto Efficiency.

### Mean Absolute Error (MAE)
An accuracy metric that calculates the average absolute difference between predicted volatility and actual volatility:
$$\text{MAE} = \frac{1}{N} \sum_{t=1}^N |y_t - \hat{y}_t|$$

### Mean Absolute Percentage Error (MAPE)
A common percentage accuracy metric that measures error relative to actual volume. In airport checkpoint forecasting, MAPE is mathematically unusable because checkpoints close overnight (0 passengers), which results in division-by-zero errors.

### Mean Absolute Scaled Error (MASE)
A scale-free forecasting metric that compares a model's volatility forecast error against a simple reference benchmark: guessing that today's volatility will simply repeat yesterday's volatility at the same period.
* A MASE of **1.0** means the model is no better than repeating yesterday's volatility.
* A MASE **below 1.0** indicates genuine forecasting skill (e.g., a MASE of 0.662 represents a 33.8% improvement over persistence).
* A MASE **above 1.0** means the model performs worse than a simple persistence guess.

### Mean Forecast Bias
The average directional error of a volatility model across all evaluation intervals:
$$\text{Bias} = \frac{1}{N} \sum_{t=1}^N (\hat{y}_t - y_t)$$

### Out-of-Time Holdout Evaluation
A rigorous forecasting validation method where an entire future year of data (the full 12 months of 2025; 8,760 hours / 3,222 airport-days) is locked away and completely unobserved while models are developed and tuned. The models are then tested on this unseen year once, simulating how they would perform in real-world airport operations.

### Relative Transfer Ratio (RTR)
A generalizability metric that evaluates how well a volatility model performs when deployed to an unfamiliar airport without retraining, calculated as:
$$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
A score near 1.0 indicates that the model transfers seamlessly across airports with minimal loss of accuracy.

### Resilience (Evaluation Dimension 2)
One of the three core evaluative pillars defined in this study, assessing how well a forecast model maintains reasonable accuracy and avoids volatility collapse during severe operational shocks, such as winter freezes, thunderstorms, or ground stops.

### Resilience Target ($R_{\text{RMSE}} \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$)
The stated academic performance target for operational disruptions: maintaining a Recovery Multiplier $R_{\text{RMSE}} \approx 1.00$ ($R_{\text{MASE}} \approx 1.00$), the lowest $\text{MASE}_{\text{shock}}$ during flight delays $\ge 45$ min or cancellations $\ge 5$, and rapid recovery ($\text{TTR} < 4.0\text{ hours}$). Decisively won by the Dynamic Two-Stage Hybrid (Model 3, $R_{\text{MASE}} = 1.05, \text{MASE}_{\text{shock}} = 0.694, \text{TTR} = 2.8\text{h}$).

### Robustness (Evaluation Dimension 1)
One of the three core evaluative pillars defined in this study, assessing the day-in, day-out accuracy and consistency of a forecasting model under normal, on-time operating conditions.

### Robustness Target ($\text{RMSE}_{\text{routine}}$ Lowest, $\text{MASE}_{\text{routine}} < 0.70$)
The stated academic performance target for routine operations: achieving the lowest root mean squared error under routine conditions (departure delays $< 15$ min, 0 cancellations) and an out-of-time $\text{MASE}_{\text{routine}} < 0.700$. Achieved by Model 3 ($\text{RMSE} = 222.1, \text{MASE} = 0.662$) and Model 2 ($\text{MASE} = 0.680\text{--}0.700$).

### Root Mean Squared Error (RMSE)
A standard forecasting accuracy metric that measures the overall spread of prediction errors:
$$\text{RMSE} = \sqrt{\frac{1}{N} \sum_{t=1}^N (y_t - \hat{y}_t)^2}$$
Because errors are squared before being averaged, RMSE penalizes large errors heavily, detecting when a model severely misses a major volatility surge.

### Time-to-Recovery ($\text{TTR}_{\text{shock}}$)
The time, in hours, required for a forecasting model's prediction error to return to normal baseline levels after a major flight disruption event.

### Transfer Error Penalty ($\Delta_{\text{transfer}}$)
The percentage increase in forecast error when a model trained on one airport is deployed zero-shot to a different airport without local retraining:
$$\Delta_{\text{transfer}} = \left( \frac{\text{RMSE}_{\text{transfer}} - \text{RMSE}_{\text{in-sample}}}{\text{RMSE}_{\text{in-sample}}} \right) \times 100\%$$

### Welch's $t$-Test
A standard statistical test used to check if the average values of two groups are significantly different without assuming that both groups have identical variability. In this study, it was used to verify when travel habits returned to pre-pandemic baselines.

### Wilcoxon Signed-Rank Test
A non-parametric statistical test used to determine whether the difference between paired model predictions is statistically significant, confirming that machine learning improvements hold true across individual airport facilities.

### Zero-Flight Intercept Test
A validation test confirming that dedicated single-airline checkpoints truly isolate carrier demand: when an airline has zero flights scheduled during an hour, predicted and observed checkpoint throughput is statistically indistinguishable from zero.

### Zero-Shot Transfer Deployment
An operational test in which a forecasting model trained and calibrated on one airport is deployed directly to an unfamiliar airport without any local retraining, evaluating its out-of-the-box portability.
