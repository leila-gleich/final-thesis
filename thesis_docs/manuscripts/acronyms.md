# List of Acronyms and Abbreviations

> **Thesis Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*  
> **Author**: Leila Gleich | **Degree**: Master of Science in Aeronautics (MSAA / Gleich 700B)  
> **Institution**: Embry-Riddle Aeronautical University, College of Aeronautics  
> **Standards Compliance**: APA 7th Edition, Strict Aviation Terminology, Throughput Volatility Focus

---

## Operational Scope and Purpose

This document compiles and defines the comprehensive inventory of technical acronyms, federal agency abbreviations, aviation data schemas, airport and carrier codes, queuing theory notations, machine learning architectures, and econometric evaluation metrics used across Chapters I through V of this manuscript. In commercial aviation and airport security operations, interdisciplinary communication bridges federal regulatory bodies (FAA, TSA), statistical data providers (BTS), airline operators, and terminal security planners. To eliminate ambiguity and support dissertation committee review in accordance with the *Publication Manual of the American Psychological Association* (7th ed.; APA, 2020), this document provides a dual-presentation architecture:

1. **Part I: Master Alphabetical Index (Table 1)**: A unified, quick-reference master table listing all 100+ acronyms in strict alphabetical order, specifying each term's formal expansion, operational domain classification, and primary function in the thesis methodology.
2. **Part II: Categorized Operational Descriptions**: In-depth narrative profiles organized into seven operational categories matching the functional workflow of airport terminal analytics.

A foundational methodological principle of this research is that airport terminal queue stability and passenger delay risks are governed not merely by static passenger volumes, but by the **volatility of checkpoint throughput** (within-day standard deviation $\sigma_{\text{TSA, hr}}$, scale-free Coefficient of Variation $CV_{\text{TSA}}$, and multi-day temporal dispersion $\sigma_{\text{TSA, 7d}}$). Under Kingman's heavy-traffic queuing formula ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), expected waiting times scale quadratically with arrival volatility ($C_a^2$) as checkpoint lane utilization approaches capacity ($\rho \to 1.0$). Accordingly, all operational terms, model formulations, and evaluation metrics defined herein are grounded in authentic commercial aviation operations, airline flight scheduling cycles, and airport passenger flow dynamics.

---

## Part I: Master Alphabetical Index

Table 1  
*Master Index of Acronyms, Operational Expansions, and Thesis Applications*

| Acronym / Abbreviation | Full Expansion / Stand-For Term | Operational Category | Primary Thesis Application |
| :--- | :--- | :--- | :--- |
| **A14** | Air Carrier On-Time Reporting Benchmark (14-Minute Arrival Delay Tolerance) | Regulatory & Air Traffic Management | The federal regulatory reporting benchmark established by the Federal Aviation Administration (FAA) and Bureau of Transportation Statistics (BTS) under 14 CFR Part 234. A commercial domestic flight is classified as on-time if it arrives at the gate within 14 minutes and 59 seconds of its scheduled gate arrival time. In the thesis, A14 defines the boundary of the Nominal On-Time Baseline regime (departure delays < 15 minutes, zero cancellations). |
| **AA** | American Airlines | Commercial Air Carriers | Major U.S. network legacy carrier (IATA code: AA). In the thesis, carrier-exclusive terminal complexes operated by American Airlines are analyzed at Dallas/Fort Worth (DFW), Charlotte Douglas (CLT), Philadelphia (PHL), and New York LaGuardia (LGA) during the purposive 4-tier filtering process to isolate unconfounded flight bank arrivals. |
| **ACRP** | Airport Cooperative Research Program | Aviation Research & Literature | An applied research program sponsored by the FAA and administered by the Transportation Research Board (TRB). ACRP Report 40 ('Airport Passenger Convergent and Terminal Processing') provides the empirical passenger show-up curves convolved across scheduled airline flight banks in Model 1 (Deterministic Flight Schedule Model). |
| **AI** | Artificial Intelligence | Predictive Modeling & Computational Methods | The overarching computer science discipline encompassing machine learning, statistical pattern recognition, and autonomous operational decision systems; evaluated in the literature review to contrast empirical data-driven forecasting with deterministic operational models. |
| **ANN** | Artificial Neural Network | Predictive Modeling & Computational Methods | A class of machine learning models structured as interconnected artificial neuron layers; reviewed in terminal passenger flow and delay modeling literature and contrasted with tree-based regressors and two-stage hybrid models. |
| **ANOVA** | Analysis of Variance | Evaluation Metrics & Econometric Statistics | Statistical hypothesis testing framework used in empirical exploratory data analysis to evaluate variance components and statistical significance across airport clusters, days of the week, and operational disturbance regimes. |
| **AOC** | Airport Operations Center | Airport Infrastructure & Operations | The central operational command facility at a commercial airport where airport authority staff, airline operations dispatchers, TSA security leadership, and law enforcement monitor real-time passenger terminal flow, gate assignments, runway conditions, and emergency responses. |
| **APA** | American Psychological Association | Academic & Publishing Standards | The authoritative academic publishing standard (APA 7th edition, 2020) governing manuscript layout, heading hierarchy, in-text citations, statistical reporting format, and table structure (three horizontal rules, zero vertical rules) across the thesis. |
| **APE** | Absolute Percentage Error | Evaluation Metrics & Econometric Statistics | The observation-level forecasting error ratio defined as \|y_t - ŷ_t\| / y_t. In the thesis, shown to produce catastrophic division-by-zero explosions during overnight checkpoint curfew hours when actual screening volumes approach zero (y_t ≈ 0), methodologically invalidating Mean Absolute Percentage Error (MAPE). |
| **ARIMA** | Autoregressive Integrated Moving Average | Predictive Modeling & Computational Methods | Classical linear time-series forecasting model combining autoregressive lags (p), integrated differencing (d), and moving average error innovations (q); serves as a benchmark in time-series passenger demand and terminal queue literature. |
| **ATC** | Air Traffic Control | Regulatory & Air Traffic Management | The Federal Aviation Administration operational service responsible for directing aircraft safely on runways, taxiways, and throughout the National Airspace System, managing ground traffic sequencing and en-route flight separations. |
| **ATCSCC** | Air Traffic Control System Command Center | Regulatory & Air Traffic Management | Centralized FAA air traffic management facility in Warrenton, Virginia, that monitors nationwide airspace demand and coordinates traffic management initiatives, including Ground Delay Programs (GDPs), ground stops, and airspace routing reconfigurations. |
| **ATL** | Hartsfield-Jackson Atlanta International Airport | Airport Cohort & Airfield Codes | Major commercial connecting hub (IATA code: ATL; Delta Air Lines primary mega-complex). Evaluated in the Top 25 network clustering census; excluded from the primary 9-airport experimental cohort during 4-tier filtering due to extreme connecting transfer ratios (>65%) that confound TSA checkpoint throughput. |
| **BI** | Business Intelligence | Data Systems & Information Architecture | Data systems, dashboards, and reporting architectures deployed by airport authorities and federal directors to track terminal checkpoint throughput, queue waiting times, and resource allocation. |
| **BOS** | Boston Logan International Airport | Airport Cohort & Airfield Codes | Commercial airport (IATA code: BOS). Evaluated in Top 25 network clustering and 4-tier filtering as a prominent Northeast commercial origin-and-destination complex. |
| **BTS** | Bureau of Transportation Statistics | Federal Aviation Datasets & Schemas | Statistical operating administration within the U.S. Department of Transportation (USDOT) that collects, compiles, and publishes official national transportation datasets, including BTS Form 234 (On-Time Performance), Form 41 (Schedule T-100), and the DB1B Origin and Destination Survey. |
| **BTS Form 234** | BTS Form 234 Airline On-Time Performance Survey | Federal Aviation Datasets & Schemas | Mandatory monthly flight-by-flight operational database providing departure delays, arrival delays, taxi-out queue durations, airborne times, and cause-of-delay categories (Carrier, Weather, NAS, Security, Late Aircraft) across reporting air carriers. |
| **BTS Form 41** | BTS Form 41 Financial and Operating Statistics (Schedule T-100) | Federal Aviation Datasets & Schemas | Federal regulatory reporting schedule filed by commercial airlines containing monthly non-stop domestic flight segment records, available aircraft seat capacity, flown revenue passenger counts, and passenger load factors. |
| **CAT** | Credential Authentication Technology | Airport Infrastructure & Operations | Digital identity verification scanners deployed at TSA checkpoint lanes that scan traveler photo identification (driver's licenses, passports) to confirm flight reservations directly against airline manifest databases in real time without requiring a boarding pass. |
| **CKPT** | Checkpoint | Airport Infrastructure & Operations | Standard operational abbreviation used in TSA screening logs, database schemas, and terminal facility blueprints denoting a physical passenger screening checkpoint complex. |
| **CLT** | Charlotte Douglas International Airport | Airport Cohort & Airfield Codes | Major connecting hub (IATA code: CLT) dominated by American Airlines. Evaluated during 4-tier filtering and Top 25 network clustering to examine connecting transfer passenger deconvolution. |
| **CNN** | Convolutional Neural Network | Predictive Modeling & Computational Methods | Deep artificial neural network architecture employing convolutional filter banks over temporal sequences; reviewed in terminal passenger flow and delay modeling literature. |
| **COVID-19** | Coronavirus Disease 2019 | Operational Regimes & Demarcation | Global viral pandemic causing historic structural disruption across the commercial aviation sector; in the thesis, the study baseline utilizes Candidate B demarcation (May 1, 2022 to December 31, 2025) to isolate post-mask-mandate stable passenger behavior from pandemic anomalies. |
| **CSV** | Comma-Separated Values | Data Systems & Information Architecture | Standard tabular data file format used across the thesis repository to store reproducible research tables, benchmark outputs, and conformed experimental metrics. |
| **CT** | Computed Tomography | Airport Infrastructure & Operations | Advanced 3D X-ray screening technology deployed at TSA checkpoint lanes that generates high-resolution volumetric scans of carry-on baggage, altering lane service times and processing efficiency. |
| **CTU** | Central Terminal Unit | Airport Infrastructure & Operations | Architectural classification for centralized airport passenger processing terminal facilities, as distinguished from decentralized or modular satellite concourses. |
| **CUSUM** | Cumulative Sum Structural Break Test | Evaluation Metrics & Econometric Statistics | Sequential statistical quality control chart and econometric test used in Chapter III to detect structural parameter shifts and change-points across time-series error residuals, validating post-COVID sample stability. |
| **CV** | Coefficient of Variation | Evaluation Metrics & Econometric Statistics | Dimensionless scale-free measure of relative dispersion defined as the ratio of the standard deviation to the mean (CV = σ / μ). Used throughout the thesis to quantify passenger arrival burstiness independent of airport size. |
| **CVI** | Coupled Volatility Index (Landside-Airside Volatility Interaction Term) | Evaluation Metrics & Econometric Statistics | Operational interaction term defined as the product of scale-free passenger throughput volatility (CV_TSA) and flight departure delay dispersion (σ_Delay), measuring compounding operational turbulence when landside surges coincide with airside flight delays. |
| **CV_TSA** | Coefficient of Variation of TSA Passenger Screening Throughput | Evaluation Metrics & Econometric Statistics | Primary scale-free dependent target of the thesis, defined as the hourly standard deviation of passenger screening throughput divided by mean hourly throughput across the diurnal cycle (CV_TSA,hr = σ_hr / μ_hr). Captures checkpoint arrival burstiness. |
| **DB1B** | Airline Origin and Destination Survey (Data Bank 1B) | Federal Aviation Datasets & Schemas | A 10% random sample of all commercial airline passenger tickets collected quarterly by the Bureau of Transportation Statistics, reporting complete itinerary routings, operating carriers, and true origin-destination pairs. |
| **DB1C** | Origin and Destination Ticket Coupon Survey (Data Bank 1C) | Federal Aviation Datasets & Schemas | Flight-coupon segment table within the BTS DB1B database used in Chapter III to calculate carrier-specific transfer ratios and derive the Connecting Passenger Deflator. |
| **DCA** | Ronald Reagan Washington National Airport | Airport Cohort & Airfield Codes | Perimeter-restricted, slot-controlled commercial airport in Arlington, Virginia (IATA code: DCA), evaluated in Top 25 network clustering. |
| **DDL** | Data Definition Language | Data Systems & Information Architecture | SQL schema specification syntax defining table structures, column data types, primary keys, and relational constraints in the conformed research warehouse. |
| **DEN** | Denver International Airport | Airport Cohort & Airfield Codes | Major connecting hub and commercial mega-airport (IATA code: DEN). Analyzed during Top 25 network clustering as a dual-carrier hub complex (United / Southwest). |
| **DES** | Discrete Event Simulation | Predictive Modeling & Computational Methods | Computational simulation modeling technique that represents an airport terminal as a discrete sequence of events in time (passenger arrivals, ID checks, bag divestiture, X-ray scanning). Evaluated in Chapter II as high-fidelity but computationally prohibitive for real-time dispatch. |
| **DFW** | Dallas Fort Worth International Airport | Airport Cohort & Airfield Codes | American Airlines primary mega-connecting hub (IATA code: DFW). Evaluated in Top 25 clustering and 4-tier filtering to benchmark terminal passenger transfer dynamics. |
| **DL** | Delta Air Lines | Commercial Air Carriers | Major U.S. network legacy carrier (IATA code: DL). Operates dedicated terminal complexes analyzed at Detroit (DTW McNamara Terminal), Salt Lake City (SLC), and New York LaGuardia (LGA Terminal C). |
| **DM** | Diebold-Mariano Test Statistic | Evaluation Metrics & Econometric Statistics | Non-parametric econometric test comparing the predictive accuracy of competing time-series forecasts under serial correlation and heteroskedasticity. Formulated in Appendix C to establish rigorous statistical significance of Model 2 and Model 3 over Model 1. |
| **DOT** | Department of Transportation | Regulatory & Air Traffic Management | United States Department of Transportation (USDOT), the cabinet department overseeing federal transportation agencies including the FAA and BTS. |
| **DOW** | Day of Week | Operational Regimes & Demarcation | Categorical temporal feature capturing cyclical weekly demand fluctuations (e.g., Thursday/Friday business travel waves versus Sunday leisure return peaks). |
| **DTW** | Detroit Metropolitan Wayne County Airport | Airport Cohort & Airfield Codes | Major connecting hub (IATA code: DTW). The McNamara Terminal at DTW represents an isolated carrier-dedicated screening facility (Delta Air Lines) evaluated in the balanced 4x4 experimental cohort. |
| **ETL** | Extract, Transform, and Load | Data Systems & Information Architecture | The three-stage data pipeline architecture utilized to ingest raw federal records (TSA FOIA, BTS OTP, BTS T-100, DB1B), execute data cleansing and schema conformance, and load star-schema analytical tables. |
| **EWR** | Newark Liberty International Airport | Airport Cohort & Airfield Codes | Primary commercial hub (IATA code: EWR). Terminal C, an isolated United Airlines screening complex, serves as the primary development testbed airfield for lead-lag deconvolution and the in-sample baseline for zero-shot spatial transfer. |
| **FAA** | Federal Aviation Administration | Regulatory & Air Traffic Management | Operating administration of the U.S. Department of Transportation responsible for the safety, air traffic management, regulatory oversight, and infrastructure standards of civil aviation. |
| **FIFO** | First-In, First-Out | Queuing Theory & Passenger Dynamics | Classical queuing discipline where passengers are screened in the exact sequential order of their arrival at the checkpoint queue entrance. |
| **FINM** | Fusion Intelligence Network Model | Predictive Modeling & Computational Methods | Predictive multi-source intelligence architecture cited in literature integrating heterogeneous data feeds across airside and landside operations. |
| **FOIA** | Freedom of Information Act | Federal Aviation Datasets & Schemas | Federal public records disclosure statute (5 U.S.C. § 552) through which the multi-year, hourly checkpoint-lane passenger screening dataset was acquired from the TSA for this research. |
| **FSD** | Federal Security Director | Airport Infrastructure & Operations | Senior executive official appointed by the TSA stationed at commercial airports, exercising operational authority over checkpoint staffing, screening procedures, and terminal security compliance. |
| **GBDT** | Gradient-Boosted Decision Trees | Predictive Modeling & Computational Methods | Alternative designation for Gradient Boosting Machines emphasizing tree-based weak learners. |
| **GBM** | Gradient Boosting Machine | Predictive Modeling & Computational Methods | Supervised machine learning ensemble architecture that builds sequential decision trees to minimize empirical loss. Serves as the core regressor in Model 2 (Supervised Machine Learning Model). |
| **GDP** | Ground Delay Program | Regulatory & Air Traffic Management | FAA air traffic management initiative implemented during severe weather or congestion that holds departing aircraft on the ground at origin airports, inducing lead-lag flight departure delays. |
| **G/G/c** | General Arrival / General Service / c-Server Queuing Model | Queuing Theory & Passenger Dynamics | Kendall notation for a multi-server queuing system with arbitrary inter-arrival distributions, arbitrary service times, and c parallel screening lanes operating in parallel. |
| **GI/G/1** | General Independent Arrival / General Service / Single Server Queuing Model | Queuing Theory & Passenger Dynamics | Kendall queuing notation representing single-server queues with general independent arrivals and service distributions, underlying Kingman's heavy-traffic approximation. |
| **GRU** | Gated Recurrent Unit | Predictive Modeling & Computational Methods | Gated recurrent neural network architecture that models sequential temporal dependencies with reset and update gates; evaluated in Chapter II deep learning literature. |
| **GSPN** | Generalized Stochastic Petri Nets | Predictive Modeling & Computational Methods | Mathematical and graphical modeling formalism utilized in terminal simulation literature to analyze concurrent, stochastic passenger movements. |
| **HAC** | Heteroskedasticity and Autocorrelation Consistent | Evaluation Metrics & Econometric Statistics | Econometric covariance matrix estimator (Newey-West) that yields robust, unconfounded standard errors and test statistics when time-series residuals exhibit autocorrelation and conditional heteroskedasticity. |
| **HistGBM** | Histogram-Based Gradient Boosting Machine | Predictive Modeling & Computational Methods | Optimized decision-tree gradient boosting implementation (scikit-learn HistGradientBoostingRegressor) that discretizes continuous features into integer bins; utilized in Model 2 for fast, robust execution. |
| **HOD** | Hour of Day | Operational Regimes & Demarcation | Categorical temporal unit representing each of the 24 discrete hours within an operational day, capturing diurnal passenger bank rhythms. |
| **HPC** | High-Performance Computing | Data Systems & Information Architecture | Distributed multi-core server infrastructure utilized for intensive ETL data processing, deconvolution algorithms, and machine learning cross-validation. |
| **HQBN** | Hybrid Queue-based Bayesian Network | Predictive Modeling & Computational Methods | Probabilistic graphical modeling architecture combining Bayesian inference with queuing formulas to predict multi-stage airport delay propagation. |
| **IAD** | Washington Dulles International Airport | Airport Cohort & Airfield Codes | Commercial hub airport (IATA code: IAD) in Northern Virginia operated by MWAA; evaluated in Top 25 network clustering as a United Airlines East Coast hub. |
| **IAH** | George Bush Intercontinental Airport (Houston) | Airport Cohort & Airfield Codes | United Airlines primary southern hub complex (IATA code: IAH). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline for dedicated terminal screening analysis. |
| **IATA** | International Air Transport Association | Aviation Research & Literature | Global trade association representing commercial airlines, establishing international air transport standards, schedule data formats, and airport Level of Service (LOS) passenger space criteria. |
| **ICAO** | International Civil Aviation Organization | Regulatory & Air Traffic Management | Specialized agency of the United Nations establishing global international civil aviation principles, airspace safety regulations, and airport design standards. |
| **IEEE** | Institute of Electrical and Electronics Engineers | Academic & Publishing Standards | Professional technical organization publishing peer-reviewed research in transportation engineering, intelligent systems, and computational algorithms. |
| **ILP** | Integer Linear Programming | Predictive Modeling & Computational Methods | Mathematical optimization technique used in terminal resource allocation and lane scheduling literature to determine optimal lane opening schedules subject to discrete constraints. |
| **IROPS** | Irregular Operations | Operational Regimes & Demarcation | Severe operational disruptions (convective storms, equipment failures, ground stops; departure delays ≥ 45 min or cancellations ≥ 5) driving checkpoint queue spikes. Constitutes the core test regime for Dimension 2 (Resilience). |
| **ISO** | International Organization for Standardization | Academic & Publishing Standards | Independent international non-governmental organization developing worldwide industrial, quality, and data security standards. |
| **IT** | Information Technology | Data Systems & Information Architecture | Enterprise computing, database architecture, and network infrastructure supporting airline reservation systems and airport operational command systems. |
| **JFK** | John F. Kennedy International Airport | Airport Cohort & Airfield Codes | Major international gateway in New York (IATA code: JFK). Analyzed during Top 25 network clustering and contrasted with LGA in 4-tier filtering to examine decentralized multi-terminal structures. |
| **KS** | Kolmogorov-Smirnov Test | Evaluation Metrics & Econometric Statistics | Non-parametric statistical goodness-of-fit test comparing empirical distributions; utilized in Chapter III to confirm distributional invariance across airport terminal layouts (D = 0.032, p = 0.28). |
| **LAWA** | Los Angeles World Airports | Airport Infrastructure & Operations | The proprietary municipal airport authority governing Los Angeles International Airport (LAX) and Van Nuys Airport, providing operational terminal passenger statistics. |
| **LAX** | Los Angeles International Airport | Airport Cohort & Airfield Codes | Major West Coast commercial mega-airport (IATA code: LAX). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline as a multi-carrier origin-and-destination complex. |
| **LGA** | LaGuardia Airport | Airport Cohort & Airfield Codes | Commercial hub airport in New York (IATA code: LGA). Terminal B/C serves as the zero-shot spatial transfer evaluation airfield (EWR → LGA) for testing model generalizability without retraining in Dimension 3. |
| **LOS** | Level of Service | Queuing Theory & Passenger Dynamics | Standardized qualitative metric framework (IATA Airport Development Reference Manual) rating passenger waiting times, terminal crowding, and space availability from LOS A (excellent) to LOS F (system breakdown). |
| **LR** | Linear Regression | Predictive Modeling & Computational Methods | Fundamental statistical modeling approach estimating linear relationships between operational predictors and passenger flow. |
| **LSTM** | Long Short-Term Memory | Predictive Modeling & Computational Methods | Advanced recurrent neural network architecture with input, forget, and output gating mechanisms that capture long-term sequential dependencies in time-series data. |
| **MAE** | Mean Absolute Error | Evaluation Metrics & Econometric Statistics | Standard linear loss metric calculating the average magnitude of absolute forecasting errors in original physical units (pax/hr or pax/day): MAE = (1/n) Σ \|y_t - ŷ_t\|. |
| **MAPE** | Mean Absolute Percentage Error | Evaluation Metrics & Econometric Statistics | Relative percentage error metric: MAPE = (100/n) Σ \|(y_t - ŷ_t) / y_t\|. In the thesis, proven to be mathematically invalid for hourly checkpoint modeling due to overnight structural zeros (y_t ≈ 0 pax/hr) causing division-by-zero explosions. |
| **MASE** | Mean Absolute Scaled Error | Evaluation Metrics & Econometric Statistics | Scale-independent forecast accuracy metric (Hyndman & Koehler, 2006) normalizing model MAE against the in-sample mean absolute error of a naive diurnal persistence baseline. Values < 1.000 indicate superiority over persistence. |
| **MATLAB** | Matrix Laboratory | Data Systems & Information Architecture | Proprietary numerical computing and simulation environment frequently cited in early airport terminal simulation and queue optimization literature. |
| **MB** | Megabyte | Data Systems & Information Architecture | Standard digital storage unit (1,048,576 bytes) used in reporting raw data feed sizes and memory footprints. |
| **MDI** | Mean Decrease in Impurity | Predictive Modeling & Computational Methods | Gini or variance-based feature importance metric in tree ensembles measuring the total reduction in criterion impurity contributed by each operational predictor. |
| **M/G/c** | Markovian Arrival / General Service / c-Server Queuing Model | Queuing Theory & Passenger Dynamics | Kendall notation for a queuing system with Poisson arrivals, arbitrary service time distributions, and c parallel screening lanes. |
| **ML** | Machine Learning | Predictive Modeling & Computational Methods | Automated algorithmic discipline learning predictive patterns from data; instantiated in Model 2 (Supervised Machine Learning Model). |
| **M/M/1** | Markovian Arrival / Markovian Service / Single-Server Queuing Model | Queuing Theory & Passenger Dynamics | Classical queuing model with Poisson arrivals and exponential service times operating with a single server; foundational baseline in queuing literature. |
| **M/M/c** | Markovian Arrival / Markovian Service / c-Server Queuing Model | Queuing Theory & Passenger Dynamics | Multi-server Erlang delay queuing model assuming Poisson arrivals and memoryless service rates across c parallel screening lanes. |
| **MPC** | Model Predictive Control | Predictive Modeling & Computational Methods | Advanced feedback control methodology optimizing operational control actions (e.g., lane staffing schedules) over a rolling finite time horizon using dynamic system models. |
| **MSAA** | Master of Science in Aeronautics | Academic & Publishing Standards | The graduate degree program at Embry-Riddle Aeronautical University under which this thesis (Gleich 700B) was conducted and submitted. |
| **MSE** | Mean Squared Error | Evaluation Metrics & Econometric Statistics | Quadratic error loss metric calculating the mean of squared residuals: MSE = (1/n) Σ (y_t - ŷ_t)². |
| **NARX** | Nonlinear Autoregressive with Exogenous Input | Predictive Modeling & Computational Methods | Dynamic neural network architecture incorporating recurrent autoregressive feedback alongside external driving time-series inputs. |
| **NAS** | National Airspace System | Regulatory & Air Traffic Management | The comprehensive common network of United States airspace, air navigation facilities, airports, air traffic control towers, and operational regulations overseen by the FAA. |
| **NASA** | National Aeronautics and Space Administration | Aviation Research & Literature | U.S. government agency conducting advanced aerospace research and developing air traffic management decision-support systems. |
| **NHPP** | Non-Homogeneous Poisson Process | Queuing Theory & Passenger Dynamics | Stochastic arrival point process where the arrival intensity rate λ(t) varies continuously over time, capturing time-varying passenger arrival intensity across flight banks. |
| **OAG** | Official Aviation Guide | Federal Aviation Datasets & Schemas | Commercial global aviation data provider supplying scheduled airline timetables, flight numbers, and aircraft equipment assignments. |
| **O&D** | Origin and Destination | Federal Aviation Datasets & Schemas | Classification of air passengers denoting true originating trip origin and final destination, distinguishing local originating travelers entering security checkpoints from connecting transfer passengers. |
| **OLS** | Ordinary Least Squares | Evaluation Metrics & Econometric Statistics | Classical linear regression estimation technique minimizing the sum of squared differences between observed and predicted values. |
| **ORD** | Chicago O'Hare International Airport | Airport Cohort & Airfield Codes | Major domestic connecting mega-hub (IATA code: ORD). Evaluated in Top 25 network clustering as a dual-carrier connecting hub (United Terminal 1 / American Terminal 3). |
| **OTP** | On-Time Performance | Federal Aviation Datasets & Schemas | Airline operational reliability database (BTS Form 234) tracking flight departure delays, arrival delays, taxi times, and cancellation dynamics across reporting U.S. carriers. |
| **PAR** | Passenger Arrival Rate | Queuing Theory & Passenger Dynamics | The instantaneous or hourly volume of passengers entering the security checkpoint queuing area per unit time (pax/hr). |
| **PHL** | Philadelphia International Airport | Airport Cohort & Airfield Codes | Commercial airport (IATA code: PHL). Evaluated in the Top 25 clustering and 4-tier filtering pipeline as an American Airlines hub complex. |
| **PreCheck** | TSA PreCheck Expedited Screening Program | Airport Infrastructure & Operations | TSA trusted traveler program allowing vetted passengers to utilize dedicated screening lanes with reduced divestiture protocols (shoes, belts, light jackets remain on), resulting in higher service throughput rates. |
| **PSO** | Particle Swarm Optimization | Predictive Modeling & Computational Methods | Computational metaheuristic optimization algorithm inspired by biological flocking behaviors, evaluated in terminal literature for hyperparameter tuning. |
| **PSO-BP** | Particle Swarm Optimization with Back Propagation | Predictive Modeling & Computational Methods | Hybrid machine learning optimization algorithm combining particle swarm optimization with backpropagation neural networks to optimize network weights. |
| **R²** | Coefficient of Determination (R-Squared) | Evaluation Metrics & Econometric Statistics | Statistical goodness-of-fit metric measuring the proportion of total variance in the dependent target (throughput volatility or volume) explained by the predictive model. |
| **RF** | Random Forest | Predictive Modeling & Computational Methods | Ensemble supervised machine learning regressor constructing multiple randomized decision trees to capture non-linear feature interactions. |
| **R_MASE** | Disruption Error Multiplier (Resilience Multiplier) | Evaluation Metrics & Econometric Statistics | Core evaluation metric for Dimension 2 (Resilience) defined as the ratio of forecast error under irregular operations to nominal baseline error: R_MASE = MASE_shock / MASE_nominal. Values close to 1.00 denote robust operational recovery. |
| **RMSE** | Root Mean Squared Error | Evaluation Metrics & Econometric Statistics | Standard quadratic performance metric calculating the square root of mean squared forecasting errors in original physical units (pax/hr or pax/day): RMSE = √[(1/n) Σ (y_t - ŷ_t)²]. |
| **RTR** | Relative Transfer Ratio (Transfer Error Penalty) | Evaluation Metrics & Econometric Statistics | Core evaluation metric for Dimension 3 (Generalizability) quantifying zero-shot spatial transfer degradation: RTR = RMSE_transfer / RMSE_in-sample. Ratios near 1.00 denote portable model logic. |
| **SARIMA** | Seasonal Autoregressive Integrated Moving Average | Predictive Modeling & Computational Methods | Linear time-series model extending ARIMA with seasonal lag polynomials (P, D, Q)_s to capture recurring 24-hour diurnal operational cycles. |
| **SARIMAX** | Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors | Predictive Modeling & Computational Methods | SARIMA model augmented with time-varying external covariates (scheduled departures, flight delays, weather indicators). |
| **SEA** | Seattle-Tacoma International Airport | Airport Cohort & Airfield Codes | Pacific Northwest commercial hub (IATA code: SEA) dominated by Alaska Airlines; analyzed in Top 25 network clustering. |
| **SESAR** | Single European Sky ATM Research | Regulatory & Air Traffic Management | European operational and technological modernization initiative harmonizing air traffic management systems across European airspace. |
| **SLAM** | Simple Landside Aggregate Model | Predictive Modeling & Computational Methods | Operations research macroscopic passenger simulation model (Brunetta et al., 1999) translating airline schedules into aggregate terminal area occupancies. |
| **SLC** | Salt Lake City International Airport | Airport Cohort & Airfield Codes | Commercial hub airport (IATA code: SLC). Delta Air Lines consolidated terminal evaluated in 4-tier filtering for single-terminal hub processing. |
| **SSOT** | Single Source of Truth | Academic & Publishing Standards | Architectural repository governance principle maintaining authoritative, conformed specification files (e.g., Chapter 1–5 SSOTs) to eliminate version conflict. |
| **SVM** | Support Vector Machine | Predictive Modeling & Computational Methods | Supervised learning model using hyperplanes in high-dimensional space for classification or regression, evaluated in airport literature. |
| **T-100** | BTS Form 41 Schedule T-100 Domestic Segment Data | Federal Aviation Datasets & Schemas | Monthly regulatory airline reporting dataset providing non-stop domestic flight segment seat capacities, transported passengers, and aircraft load factors. |
| **TRACON** | Terminal Radar Approach Control | Regulatory & Air Traffic Management | FAA air traffic control radar facility managing aircraft arrivals, departures, and sequencing within a 30- to 50-mile radius of high-density metropolitan airports (e.g., New York TRACON for EWR, LGA, JFK). |
| **TRB** | Transportation Research Board | Aviation Research & Literature | Division of the National Academies of Sciences, Engineering, and Medicine that manages national transportation research programs including the Airport Cooperative Research Program (ACRP). |
| **TSA** | Transportation Security Administration | Regulatory & Air Traffic Management | Federal homeland security agency within the Department of Homeland Security responsible for civil aviation security, passenger screening, and checkpoint operations across U.S. commercial airports. |
| **TSO** | Transportation Security Officer | Airport Infrastructure & Operations | Frontline federal security personnel employed by the TSA staffing checkpoint screening lanes, operating CAT scanners, body scanners (AIT), and baggage inspection systems. |
| **TTR** | Time-to-Recovery | Evaluation Metrics & Econometric Statistics | Resilience evaluation metric quantifying the operational elapsed time (in hours) required for forecast residuals to return to nominal baseline accuracy bounds following an IROPS disruption shock. |
| **UA** | United Airlines | Commercial Air Carriers | Major U.S. network legacy carrier (IATA code: UA). Operates dedicated hub terminal complexes analyzed at Newark (EWR Terminal C), Chicago (ORD Terminal 1), and Houston (IAH Terminal C). |
| **ULCC** | Ultra-Low-Cost Carrier | Commercial Air Carriers | Airline operating point-to-point routes with unbundled fares and aggressive ancillaries (e.g., Spirit, Frontier, Allegiant); characterized by unique passenger check-in arrival curves and bag divestiture patterns. |
| **USDOT** | United States Department of Transportation | Regulatory & Air Traffic Management | Cabinet-level federal department responsible for national transportation policy, funding, and administrative oversight of the FAA and BTS. |
| **VIF** | Variance Inflation Factor | Evaluation Metrics & Econometric Statistics | Multicollinearity diagnostic measuring the inflation of regression coefficient variance due to collinearity among predictors; used in Chapter III to assess flight schedule collinearity. |
| **VM** | Virtual Machine | Data Systems & Information Architecture | Virtualized computing environment used in research data pipeline execution and reproducible analytics. |
| **WN** | Southwest Airlines | Commercial Air Carriers | Major domestic air carrier (IATA code: WN). In the thesis, Southwest is excluded from the primary experimental cohort during 4-tier filtering because its point-to-point network, multi-carrier terminal sharing, and lack of assigned seat banks confound carrier-exclusive checkpoint isolation. |
| **WSC** | Winter Simulation Conference | Academic & Publishing Standards | Premier international conference on discrete-event and continuous computer simulation, cited in airport queuing simulation literature. |
| **XAI** | Explainable Artificial Intelligence | Predictive Modeling & Computational Methods | Methodological frameworks (e.g., SHAP, permutation feature importance) that render complex machine learning decisions interpretable to airport operations directors. |

*Note.* All terms and acronyms are grounded in authentic aviation operations, queuing theory, and empirical econometric modeling across Chapters I through V of this thesis. Primary evaluation models include Baseline Control (Diurnal Persistence), Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model). Internal variable tags ($M_0, M_1^*, M_3, M_5$) are excluded in compliance with repository governance rules.

---

## Part II: Categorized Operational Descriptions

To provide deeper contextual understanding for airport Federal Security Directors (FSDs), operational planners, and graduate committee reviewers, this section organizes all technical abbreviations into seven operational domains.

### Category 1: Federal Aviation Agencies, Regulatory Bodies, and Research Organizations

*This category covers the federal government departments, regulatory authorities, international standards organizations, and national transportation research boards that govern civil aviation safety, airspace management, and transportation research across the National Airspace System.*

#### A14 – Air Carrier On-Time Reporting Benchmark (14-Minute Arrival Delay Tolerance)
The federal regulatory reporting benchmark established by the Federal Aviation Administration (FAA) and Bureau of Transportation Statistics (BTS) under 14 CFR Part 234. A commercial domestic flight is classified as on-time if it arrives at the gate within 14 minutes and 59 seconds of its scheduled gate arrival time. In the thesis, A14 defines the boundary of the Nominal On-Time Baseline regime (departure delays < 15 minutes, zero cancellations).

#### ACRP – Airport Cooperative Research Program
An applied research program sponsored by the FAA and administered by the Transportation Research Board (TRB). ACRP Report 40 ('Airport Passenger Convergent and Terminal Processing') provides the empirical passenger show-up curves convolved across scheduled airline flight banks in Model 1 (Deterministic Flight Schedule Model).

#### DOT – Department of Transportation
United States Department of Transportation (USDOT), the cabinet department overseeing federal transportation agencies including the FAA and BTS.

#### FAA – Federal Aviation Administration
Operating administration of the U.S. Department of Transportation responsible for the safety, air traffic management, regulatory oversight, and infrastructure standards of civil aviation.

#### IATA – International Air Transport Association
Global trade association representing commercial airlines, establishing international air transport standards, schedule data formats, and airport Level of Service (LOS) passenger space criteria.

#### ICAO – International Civil Aviation Organization
Specialized agency of the United Nations establishing global international civil aviation principles, airspace safety regulations, and airport design standards.

#### NASA – National Aeronautics and Space Administration
U.S. government agency conducting advanced aerospace research and developing air traffic management decision-support systems.

#### SESAR – Single European Sky ATM Research
European operational and technological modernization initiative harmonizing air traffic management systems across European airspace.

#### TRB – Transportation Research Board
Division of the National Academies of Sciences, Engineering, and Medicine that manages national transportation research programs including the Airport Cooperative Research Program (ACRP).

#### TSA – Transportation Security Administration
Federal homeland security agency within the Department of Homeland Security responsible for civil aviation security, passenger screening, and checkpoint operations across U.S. commercial airports.

#### USDOT – United States Department of Transportation
Cabinet-level federal department responsible for national transportation policy, funding, and administrative oversight of the FAA and BTS.

### Category 2: Airport Infrastructure, Air Traffic Control, and Terminal Security Operations

*This category defines the physical airport terminal zones, centralized command centers, air traffic radar facilities, passenger identity hardware, and security screening personnel that manage terminal passenger flow and airspace sequencing.*

#### AOC – Airport Operations Center
The central operational command facility at a commercial airport where airport authority staff, airline operations dispatchers, TSA security leadership, and law enforcement monitor real-time passenger terminal flow, gate assignments, runway conditions, and emergency responses.

#### ATC – Air Traffic Control
The Federal Aviation Administration operational service responsible for directing aircraft safely on runways, taxiways, and throughout the National Airspace System, managing ground traffic sequencing and en-route flight separations.

#### ATCSCC – Air Traffic Control System Command Center
Centralized FAA air traffic management facility in Warrenton, Virginia, that monitors nationwide airspace demand and coordinates traffic management initiatives, including Ground Delay Programs (GDPs), ground stops, and airspace routing reconfigurations.

#### CAT – Credential Authentication Technology
Digital identity verification scanners deployed at TSA checkpoint lanes that scan traveler photo identification (driver's licenses, passports) to confirm flight reservations directly against airline manifest databases in real time without requiring a boarding pass.

#### CKPT – Checkpoint
Standard operational abbreviation used in TSA screening logs, database schemas, and terminal facility blueprints denoting a physical passenger screening checkpoint complex.

#### CT – Computed Tomography
Advanced 3D X-ray screening technology deployed at TSA checkpoint lanes that generates high-resolution volumetric scans of carry-on baggage, altering lane service times and processing efficiency.

#### CTU – Central Terminal Unit
Architectural classification for centralized airport passenger processing terminal facilities, as distinguished from decentralized or modular satellite concourses.

#### FSD – Federal Security Director
Senior executive official appointed by the TSA stationed at commercial airports, exercising operational authority over checkpoint staffing, screening procedures, and terminal security compliance.

#### GDP – Ground Delay Program
FAA air traffic management initiative implemented during severe weather or congestion that holds departing aircraft on the ground at origin airports, inducing lead-lag flight departure delays.

#### LAWA – Los Angeles World Airports
The proprietary municipal airport authority governing Los Angeles International Airport (LAX) and Van Nuys Airport, providing operational terminal passenger statistics.

#### NAS – National Airspace System
The comprehensive common network of United States airspace, air navigation facilities, airports, air traffic control towers, and operational regulations overseen by the FAA.

#### PreCheck – TSA PreCheck Expedited Screening Program
TSA trusted traveler program allowing vetted passengers to utilize dedicated screening lanes with reduced divestiture protocols (shoes, belts, light jackets remain on), resulting in higher service throughput rates.

#### TRACON – Terminal Radar Approach Control
FAA air traffic control radar facility managing aircraft arrivals, departures, and sequencing within a 30- to 50-mile radius of high-density metropolitan airports (e.g., New York TRACON for EWR, LGA, JFK).

#### TSO – Transportation Security Officer
Frontline federal security personnel employed by the TSA staffing checkpoint screening lanes, operating CAT scanners, body scanners (AIT), and baggage inspection systems.

### Category 3: Federal Aviation Datasets, Data Hygiene, and Information Architecture

*This category details the official federal regulatory data feeds, ticket survey archives, flight segment schedules, pipeline architectures, and relational warehouse schemas synthesized over the 2019–2025 study baseline.*

#### BI – Business Intelligence
Data systems, dashboards, and reporting architectures deployed by airport authorities and federal directors to track terminal checkpoint throughput, queue waiting times, and resource allocation.

#### BTS – Bureau of Transportation Statistics
Statistical operating administration within the U.S. Department of Transportation (USDOT) that collects, compiles, and publishes official national transportation datasets, including BTS Form 234 (On-Time Performance), Form 41 (Schedule T-100), and the DB1B Origin and Destination Survey.

#### BTS Form 234 – BTS Form 234 Airline On-Time Performance Survey
Mandatory monthly flight-by-flight operational database providing departure delays, arrival delays, taxi-out queue durations, airborne times, and cause-of-delay categories (Carrier, Weather, NAS, Security, Late Aircraft) across reporting air carriers.

#### BTS Form 41 – BTS Form 41 Financial and Operating Statistics (Schedule T-100)
Federal regulatory reporting schedule filed by commercial airlines containing monthly non-stop domestic flight segment records, available aircraft seat capacity, flown revenue passenger counts, and passenger load factors.

#### CSV – Comma-Separated Values
Standard tabular data file format used across the thesis repository to store reproducible research tables, benchmark outputs, and conformed experimental metrics.

#### DB1B – Airline Origin and Destination Survey (Data Bank 1B)
A 10% random sample of all commercial airline passenger tickets collected quarterly by the Bureau of Transportation Statistics, reporting complete itinerary routings, operating carriers, and true origin-destination pairs.

#### DB1C – Origin and Destination Ticket Coupon Survey (Data Bank 1C)
Flight-coupon segment table within the BTS DB1B database used in Chapter III to calculate carrier-specific transfer ratios and derive the Connecting Passenger Deflator.

#### DDL – Data Definition Language
SQL schema specification syntax defining table structures, column data types, primary keys, and relational constraints in the conformed research warehouse.

#### ETL – Extract, Transform, and Load
The three-stage data pipeline architecture utilized to ingest raw federal records (TSA FOIA, BTS OTP, BTS T-100, DB1B), execute data cleansing and schema conformance, and load star-schema analytical tables.

#### FOIA – Freedom of Information Act
Federal public records disclosure statute (5 U.S.C. § 552) through which the multi-year, hourly checkpoint-lane passenger screening dataset was acquired from the TSA for this research.

#### HPC – High-Performance Computing
Distributed multi-core server infrastructure utilized for intensive ETL data processing, deconvolution algorithms, and machine learning cross-validation.

#### IT – Information Technology
Enterprise computing, database architecture, and network infrastructure supporting airline reservation systems and airport operational command systems.

#### MATLAB – Matrix Laboratory
Proprietary numerical computing and simulation environment frequently cited in early airport terminal simulation and queue optimization literature.

#### MB – Megabyte
Standard digital storage unit (1,048,576 bytes) used in reporting raw data feed sizes and memory footprints.

#### OAG – Official Aviation Guide
Commercial global aviation data provider supplying scheduled airline timetables, flight numbers, and aircraft equipment assignments.

#### O&D – Origin and Destination
Classification of air passengers denoting true originating trip origin and final destination, distinguishing local originating travelers entering security checkpoints from connecting transfer passengers.

#### OTP – On-Time Performance
Airline operational reliability database (BTS Form 234) tracking flight departure delays, arrival delays, taxi times, and cancellation dynamics across reporting U.S. carriers.

#### T-100 – BTS Form 41 Schedule T-100 Domestic Segment Data
Monthly regulatory airline reporting dataset providing non-stop domestic flight segment seat capacities, transported passengers, and aircraft load factors.

#### VM – Virtual Machine
Virtualized computing environment used in research data pipeline execution and reproducible analytics.

### Category 4: Study Airport Cohort and Commercial Air Carrier Codes

*This category lists the official IATA/FAA three-letter airport codes evaluated across the Top 25 network clustering census and the balanced 9-airport experimental cohort, along with two-letter air carrier codes and operational business models.*

#### AA – American Airlines
Major U.S. network legacy carrier (IATA code: AA). In the thesis, carrier-exclusive terminal complexes operated by American Airlines are analyzed at Dallas/Fort Worth (DFW), Charlotte Douglas (CLT), Philadelphia (PHL), and New York LaGuardia (LGA) during the purposive 4-tier filtering process to isolate unconfounded flight bank arrivals.

#### ATL – Hartsfield-Jackson Atlanta International Airport
Major commercial connecting hub (IATA code: ATL; Delta Air Lines primary mega-complex). Evaluated in the Top 25 network clustering census; excluded from the primary 9-airport experimental cohort during 4-tier filtering due to extreme connecting transfer ratios (>65%) that confound TSA checkpoint throughput.

#### BOS – Boston Logan International Airport
Commercial airport (IATA code: BOS). Evaluated in Top 25 network clustering and 4-tier filtering as a prominent Northeast commercial origin-and-destination complex.

#### CLT – Charlotte Douglas International Airport
Major connecting hub (IATA code: CLT) dominated by American Airlines. Evaluated during 4-tier filtering and Top 25 network clustering to examine connecting transfer passenger deconvolution.

#### DCA – Ronald Reagan Washington National Airport
Perimeter-restricted, slot-controlled commercial airport in Arlington, Virginia (IATA code: DCA), evaluated in Top 25 network clustering.

#### DEN – Denver International Airport
Major connecting hub and commercial mega-airport (IATA code: DEN). Analyzed during Top 25 network clustering as a dual-carrier hub complex (United / Southwest).

#### DFW – Dallas Fort Worth International Airport
American Airlines primary mega-connecting hub (IATA code: DFW). Evaluated in Top 25 clustering and 4-tier filtering to benchmark terminal passenger transfer dynamics.

#### DL – Delta Air Lines
Major U.S. network legacy carrier (IATA code: DL). Operates dedicated terminal complexes analyzed at Detroit (DTW McNamara Terminal), Salt Lake City (SLC), and New York LaGuardia (LGA Terminal C).

#### DTW – Detroit Metropolitan Wayne County Airport
Major connecting hub (IATA code: DTW). The McNamara Terminal at DTW represents an isolated carrier-dedicated screening facility (Delta Air Lines) evaluated in the balanced 4x4 experimental cohort.

#### EWR – Newark Liberty International Airport
Primary commercial hub (IATA code: EWR). Terminal C, an isolated United Airlines screening complex, serves as the primary development testbed airfield for lead-lag deconvolution and the in-sample baseline for zero-shot spatial transfer.

#### IAD – Washington Dulles International Airport
Commercial hub airport (IATA code: IAD) in Northern Virginia operated by MWAA; evaluated in Top 25 network clustering as a United Airlines East Coast hub.

#### IAH – George Bush Intercontinental Airport (Houston)
United Airlines primary southern hub complex (IATA code: IAH). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline for dedicated terminal screening analysis.

#### JFK – John F. Kennedy International Airport
Major international gateway in New York (IATA code: JFK). Analyzed during Top 25 network clustering and contrasted with LGA in 4-tier filtering to examine decentralized multi-terminal structures.

#### LAX – Los Angeles International Airport
Major West Coast commercial mega-airport (IATA code: LAX). Evaluated in the Top 25 network clustering and 4-tier filtering pipeline as a multi-carrier origin-and-destination complex.

#### LGA – LaGuardia Airport
Commercial hub airport in New York (IATA code: LGA). Terminal B/C serves as the zero-shot spatial transfer evaluation airfield (EWR → LGA) for testing model generalizability without retraining in Dimension 3.

#### ORD – Chicago O'Hare International Airport
Major domestic connecting mega-hub (IATA code: ORD). Evaluated in Top 25 network clustering as a dual-carrier connecting hub (United Terminal 1 / American Terminal 3).

#### PHL – Philadelphia International Airport
Commercial airport (IATA code: PHL). Evaluated in the Top 25 clustering and 4-tier filtering pipeline as an American Airlines hub complex.

#### SEA – Seattle-Tacoma International Airport
Pacific Northwest commercial hub (IATA code: SEA) dominated by Alaska Airlines; analyzed in Top 25 network clustering.

#### SLC – Salt Lake City International Airport
Commercial hub airport (IATA code: SLC). Delta Air Lines consolidated terminal evaluated in 4-tier filtering for single-terminal hub processing.

#### UA – United Airlines
Major U.S. network legacy carrier (IATA code: UA). Operates dedicated hub terminal complexes analyzed at Newark (EWR Terminal C), Chicago (ORD Terminal 1), and Houston (IAH Terminal C).

#### ULCC – Ultra-Low-Cost Carrier
Airline operating point-to-point routes with unbundled fares and aggressive ancillaries (e.g., Spirit, Frontier, Allegiant); characterized by unique passenger check-in arrival curves and bag divestiture patterns.

#### WN – Southwest Airlines
Major domestic air carrier (IATA code: WN). In the thesis, Southwest is excluded from the primary experimental cohort during 4-tier filtering because its point-to-point network, multi-carrier terminal sharing, and lack of assigned seat banks confound carrier-exclusive checkpoint isolation.

### Category 5: Terminal Queuing Dynamics, Passenger Flow, and Arrival Processes

*This category encompasses the formal queuing theory models, stochastic point processes, Kendall queue classifications, service level ratings, and empirical show-up curves governing traveler arrival burstiness and checkpoint bottlenecks.*

#### DES – Discrete Event Simulation
Computational simulation modeling technique that represents an airport terminal as a discrete sequence of events in time (passenger arrivals, ID checks, bag divestiture, X-ray scanning). Evaluated in Chapter II as high-fidelity but computationally prohibitive for real-time dispatch.

#### FIFO – First-In, First-Out
Classical queuing discipline where passengers are screened in the exact sequential order of their arrival at the checkpoint queue entrance.

#### G/G/c – General Arrival / General Service / c-Server Queuing Model
Kendall notation for a multi-server queuing system with arbitrary inter-arrival distributions, arbitrary service times, and c parallel screening lanes operating in parallel.

#### GI/G/1 – General Independent Arrival / General Service / Single Server Queuing Model
Kendall queuing notation representing single-server queues with general independent arrivals and service distributions, underlying Kingman's heavy-traffic approximation.

#### LOS – Level of Service
Standardized qualitative metric framework (IATA Airport Development Reference Manual) rating passenger waiting times, terminal crowding, and space availability from LOS A (excellent) to LOS F (system breakdown).

#### M/G/c – Markovian Arrival / General Service / c-Server Queuing Model
Kendall notation for a queuing system with Poisson arrivals, arbitrary service time distributions, and c parallel screening lanes.

#### M/M/1 – Markovian Arrival / Markovian Service / Single-Server Queuing Model
Classical queuing model with Poisson arrivals and exponential service times operating with a single server; foundational baseline in queuing literature.

#### M/M/c – Markovian Arrival / Markovian Service / c-Server Queuing Model
Multi-server Erlang delay queuing model assuming Poisson arrivals and memoryless service rates across c parallel screening lanes.

#### NHPP – Non-Homogeneous Poisson Process
Stochastic arrival point process where the arrival intensity rate λ(t) varies continuously over time, capturing time-varying passenger arrival intensity across flight banks.

#### PAR – Passenger Arrival Rate
The instantaneous or hourly volume of passengers entering the security checkpoint queuing area per unit time (pax/hr).

### Category 6: Predictive Modeling Architectures, Machine Learning, and Time-Series Methods

*This category covers the mathematical forecasting paradigms, econometric time-series models, decision-tree ensembles, deep recurrent neural networks, and feedback control architectures benchmarked in the predictive modeling suite.*

#### AI – Artificial Intelligence
The overarching computer science discipline encompassing machine learning, statistical pattern recognition, and autonomous operational decision systems; evaluated in the literature review to contrast empirical data-driven forecasting with deterministic operational models.

#### ANN – Artificial Neural Network
A class of machine learning models structured as interconnected artificial neuron layers; reviewed in terminal passenger flow and delay modeling literature and contrasted with tree-based regressors and two-stage hybrid models.

#### ARIMA – Autoregressive Integrated Moving Average
Classical linear time-series forecasting model combining autoregressive lags (p), integrated differencing (d), and moving average error innovations (q); serves as a benchmark in time-series passenger demand and terminal queue literature.

#### CNN – Convolutional Neural Network
Deep artificial neural network architecture employing convolutional filter banks over temporal sequences; reviewed in terminal passenger flow and delay modeling literature.

#### FINM – Fusion Intelligence Network Model
Predictive multi-source intelligence architecture cited in literature integrating heterogeneous data feeds across airside and landside operations.

#### GBDT – Gradient-Boosted Decision Trees
Alternative designation for Gradient Boosting Machines emphasizing tree-based weak learners.

#### GBM – Gradient Boosting Machine
Supervised machine learning ensemble architecture that builds sequential decision trees to minimize empirical loss. Serves as the core regressor in Model 2 (Supervised Machine Learning Model).

#### GRU – Gated Recurrent Unit
Gated recurrent neural network architecture that models sequential temporal dependencies with reset and update gates; evaluated in Chapter II deep learning literature.

#### GSPN – Generalized Stochastic Petri Nets
Mathematical and graphical modeling formalism utilized in terminal simulation literature to analyze concurrent, stochastic passenger movements.

#### HistGBM – Histogram-Based Gradient Boosting Machine
Optimized decision-tree gradient boosting implementation (scikit-learn HistGradientBoostingRegressor) that discretizes continuous features into integer bins; utilized in Model 2 for fast, robust execution.

#### HQBN – Hybrid Queue-based Bayesian Network
Probabilistic graphical modeling architecture combining Bayesian inference with queuing formulas to predict multi-stage airport delay propagation.

#### ILP – Integer Linear Programming
Mathematical optimization technique used in terminal resource allocation and lane scheduling literature to determine optimal lane opening schedules subject to discrete constraints.

#### LR – Linear Regression
Fundamental statistical modeling approach estimating linear relationships between operational predictors and passenger flow.

#### LSTM – Long Short-Term Memory
Advanced recurrent neural network architecture with input, forget, and output gating mechanisms that capture long-term sequential dependencies in time-series data.

#### MDI – Mean Decrease in Impurity
Gini or variance-based feature importance metric in tree ensembles measuring the total reduction in criterion impurity contributed by each operational predictor.

#### ML – Machine Learning
Automated algorithmic discipline learning predictive patterns from data; instantiated in Model 2 (Supervised Machine Learning Model).

#### MPC – Model Predictive Control
Advanced feedback control methodology optimizing operational control actions (e.g., lane staffing schedules) over a rolling finite time horizon using dynamic system models.

#### NARX – Nonlinear Autoregressive with Exogenous Input
Dynamic neural network architecture incorporating recurrent autoregressive feedback alongside external driving time-series inputs.

#### PSO – Particle Swarm Optimization
Computational metaheuristic optimization algorithm inspired by biological flocking behaviors, evaluated in terminal literature for hyperparameter tuning.

#### PSO-BP – Particle Swarm Optimization with Back Propagation
Hybrid machine learning optimization algorithm combining particle swarm optimization with backpropagation neural networks to optimize network weights.

#### RF – Random Forest
Ensemble supervised machine learning regressor constructing multiple randomized decision trees to capture non-linear feature interactions.

#### SARIMA – Seasonal Autoregressive Integrated Moving Average
Linear time-series model extending ARIMA with seasonal lag polynomials (P, D, Q)_s to capture recurring 24-hour diurnal operational cycles.

#### SARIMAX – Seasonal Autoregressive Integrated Moving Average with Exogenous Regressors
SARIMA model augmented with time-varying external covariates (scheduled departures, flight delays, weather indicators).

#### SLAM – Simple Landside Aggregate Model
Operations research macroscopic passenger simulation model (Brunetta et al., 1999) translating airline schedules into aggregate terminal area occupancies.

#### SVM – Support Vector Machine
Supervised learning model using hyperplanes in high-dimensional space for classification or regression, evaluated in airport literature.

#### XAI – Explainable Artificial Intelligence
Methodological frameworks (e.g., SHAP, permutation feature importance) that render complex machine learning decisions interpretable to airport operations directors.

### Category 7: Predictive Evaluation Metrics, Econometric Statistics, and Operational Regimes

*This category defines the formal statistical error loss functions, scale-free volatility indices, asymptotic econometric tests, temporal operational regimes, and multi-dimensional evaluation pillars (Robustness, Resilience, Generalizability).*

#### ANOVA – Analysis of Variance
Statistical hypothesis testing framework used in empirical exploratory data analysis to evaluate variance components and statistical significance across airport clusters, days of the week, and operational disturbance regimes.

#### APA – American Psychological Association
The authoritative academic publishing standard (APA 7th edition, 2020) governing manuscript layout, heading hierarchy, in-text citations, statistical reporting format, and table structure (three horizontal rules, zero vertical rules) across the thesis.

#### APE – Absolute Percentage Error
The observation-level forecasting error ratio defined as |y_t - ŷ_t| / y_t. In the thesis, shown to produce catastrophic division-by-zero explosions during overnight checkpoint curfew hours when actual screening volumes approach zero (y_t ≈ 0), methodologically invalidating Mean Absolute Percentage Error (MAPE).

#### COVID-19 – Coronavirus Disease 2019
Global viral pandemic causing historic structural disruption across the commercial aviation sector; in the thesis, the study baseline utilizes Candidate B demarcation (May 1, 2022 to December 31, 2025) to isolate post-mask-mandate stable passenger behavior from pandemic anomalies.

#### CUSUM – Cumulative Sum Structural Break Test
Sequential statistical quality control chart and econometric test used in Chapter III to detect structural parameter shifts and change-points across time-series error residuals, validating post-COVID sample stability.

#### CV – Coefficient of Variation
Dimensionless scale-free measure of relative dispersion defined as the ratio of the standard deviation to the mean (CV = σ / μ). Used throughout the thesis to quantify passenger arrival burstiness independent of airport size.

#### CVI – Coupled Volatility Index (Landside-Airside Volatility Interaction Term)
Operational interaction term defined as the product of scale-free passenger throughput volatility (CV_TSA) and flight departure delay dispersion (σ_Delay), measuring compounding operational turbulence when landside surges coincide with airside flight delays.

#### CV_TSA – Coefficient of Variation of TSA Passenger Screening Throughput
Primary scale-free dependent target of the thesis, defined as the hourly standard deviation of passenger screening throughput divided by mean hourly throughput across the diurnal cycle (CV_TSA,hr = σ_hr / μ_hr). Captures checkpoint arrival burstiness.

#### DM – Diebold-Mariano Test Statistic
Non-parametric econometric test comparing the predictive accuracy of competing time-series forecasts under serial correlation and heteroskedasticity. Formulated in Appendix C to establish rigorous statistical significance of Model 2 and Model 3 over Model 1.

#### DOW – Day of Week
Categorical temporal feature capturing cyclical weekly demand fluctuations (e.g., Thursday/Friday business travel waves versus Sunday leisure return peaks).

#### HAC – Heteroskedasticity and Autocorrelation Consistent
Econometric covariance matrix estimator (Newey-West) that yields robust, unconfounded standard errors and test statistics when time-series residuals exhibit autocorrelation and conditional heteroskedasticity.

#### HOD – Hour of Day
Categorical temporal unit representing each of the 24 discrete hours within an operational day, capturing diurnal passenger bank rhythms.

#### IEEE – Institute of Electrical and Electronics Engineers
Professional technical organization publishing peer-reviewed research in transportation engineering, intelligent systems, and computational algorithms.

#### IROPS – Irregular Operations
Severe operational disruptions (convective storms, equipment failures, ground stops; departure delays ≥ 45 min or cancellations ≥ 5) driving checkpoint queue spikes. Constitutes the core test regime for Dimension 2 (Resilience).

#### ISO – International Organization for Standardization
Independent international non-governmental organization developing worldwide industrial, quality, and data security standards.

#### KS – Kolmogorov-Smirnov Test
Non-parametric statistical goodness-of-fit test comparing empirical distributions; utilized in Chapter III to confirm distributional invariance across airport terminal layouts (D = 0.032, p = 0.28).

#### MAE – Mean Absolute Error
Standard linear loss metric calculating the average magnitude of absolute forecasting errors in original physical units (pax/hr or pax/day): MAE = (1/n) Σ |y_t - ŷ_t|.

#### MAPE – Mean Absolute Percentage Error
Relative percentage error metric: MAPE = (100/n) Σ |(y_t - ŷ_t) / y_t|. In the thesis, proven to be mathematically invalid for hourly checkpoint modeling due to overnight structural zeros (y_t ≈ 0 pax/hr) causing division-by-zero explosions.

#### MASE – Mean Absolute Scaled Error
Scale-independent forecast accuracy metric (Hyndman & Koehler, 2006) normalizing model MAE against the in-sample mean absolute error of a naive diurnal persistence baseline. Values < 1.000 indicate superiority over persistence.

#### MSAA – Master of Science in Aeronautics
The graduate degree program at Embry-Riddle Aeronautical University under which this thesis (Gleich 700B) was conducted and submitted.

#### MSE – Mean Squared Error
Quadratic error loss metric calculating the mean of squared residuals: MSE = (1/n) Σ (y_t - ŷ_t)².

#### OLS – Ordinary Least Squares
Classical linear regression estimation technique minimizing the sum of squared differences between observed and predicted values.

#### R² – Coefficient of Determination (R-Squared)
Statistical goodness-of-fit metric measuring the proportion of total variance in the dependent target (throughput volatility or volume) explained by the predictive model.

#### R_MASE – Disruption Error Multiplier (Resilience Multiplier)
Core evaluation metric for Dimension 2 (Resilience) defined as the ratio of forecast error under irregular operations to nominal baseline error: R_MASE = MASE_shock / MASE_nominal. Values close to 1.00 denote robust operational recovery.

#### RMSE – Root Mean Squared Error
Standard quadratic performance metric calculating the square root of mean squared forecasting errors in original physical units (pax/hr or pax/day): RMSE = √[(1/n) Σ (y_t - ŷ_t)²].

#### RTR – Relative Transfer Ratio (Transfer Error Penalty)
Core evaluation metric for Dimension 3 (Generalizability) quantifying zero-shot spatial transfer degradation: RTR = RMSE_transfer / RMSE_in-sample. Ratios near 1.00 denote portable model logic.

#### SSOT – Single Source of Truth
Architectural repository governance principle maintaining authoritative, conformed specification files (e.g., Chapter 1–5 SSOTs) to eliminate version conflict.

#### TTR – Time-to-Recovery
Resilience evaluation metric quantifying the operational elapsed time (in hours) required for forecast residuals to return to nominal baseline accuracy bounds following an IROPS disruption shock.

#### VIF – Variance Inflation Factor
Multicollinearity diagnostic measuring the inflation of regression coefficient variance due to collinearity among predictors; used in Chapter III to assess flight schedule collinearity.

#### WSC – Winter Simulation Conference
Premier international conference on discrete-event and continuous computer simulation, cited in airport queuing simulation literature.
