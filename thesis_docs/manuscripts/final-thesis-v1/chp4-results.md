# Chapter IV: Findings and Discussion

This chapter presents the empirical findings and comparative performance evaluations for modeling throughput volatility at commercial airport passenger security checkpoints. Using a conformed multi-source dataset spanning seven calendar years (January 1, 2019 to December 31, 2025) across the Top 25 United States commercial airports, this research investigates how published flight schedules and real-time operational flight disruption metrics interact with passenger screening arrival dynamics. To systematically present and discuss these results, this chapter is organized into four core sections:

* **Initial Exploratory Data Analysis: Establishes the post-ETL multi-source data foundation, identifies the post-pandemic structural equilibrium demarcation point (May 1, 2022), characterizes macro annual and day-of-week seasonality, and uncovers the fundamental econometric decoupling between raw flight departures and checkpoint volumes.**
* **Data Filtering and Subset Selection: Details the four-phase purposive filtering pipeline that isolates a balanced nine-airport experimental cohort representing 12 carrier-exclusive screening environments, provides comparative descriptive statistics, validates carrier isolation econometrically, and establishes four mandatory architectural requirements for airport passenger flow modeling.**
* **Model Development and Execution: Documents feature engineering over empirical lead-lag transfer dynamics, introduces the candidate modeling architectures, establishes the dataset partitioning and calibration scale in a structured matrix, and defines the evaluation protocol on the untouched 2025 full-year out-of-time holdout dataset.**
* **Model Results and Evaluation: Evaluates model performance across the governing evaluation triad (Robustness, Resilience, and Generalizability), formally tests the thesis hypothesis using a streamlined multi-pillar evaluation matrix, and confirms the asymmetric performance trade-offs across operational paradigms.**
* **Initial Exploratory Data AnalysisDescriptive StatisticsTemporal BaselinesDefining SeasonalityOTP & TSA Throughput dataImplications for Data SubsetData Filtering and Subset Selection4 Phase Filtering PipelinePipeline ResultsDescriptive Statistics for Data SubsetImplications for Model SelectionModel development and executionFeature EngineeringModel TrainingModel TestingImplications for Results InterpretationModel Results and EvaluationModel ResultsGeneral Model PerformanceHypothesis TestingReal-World ApplicationInitial Exploratory Data AnalysisDescriptive StatisticsTemporal BaselinesDefining SeasonalityOTP & TSA Throughput dataImplications for Data SubsetData Filtering and Subset Selection4 Phase Filtering PipelinePipeline ResultsDescriptive Statistics for Data SubsetImplications for Model SelectionModel development and executionFeature EngineeringModel TrainingModel TestingImplications for Results InterpretationModel Results and EvaluationModel ResultsGeneral Model PerformanceHypothesis TestingReal-World ApplicationFigure 4.1**

## Initial Exploratory Data Analysis


### Descriptive Statistics

To construct an empirically rigorous predictive modeling architecture that eliminates temporal and feature lookahead leakage for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw operational transaction records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys (Appendix for details). Following conformed extraction, automated entity resolution, data cleaning, and relational synthesis across standardized operational dimensions (calendar date, departure time block, airport, operating carrier, fleet aircraft type, and dedicated screening complex), the nationwide post-ETL analytical warehouse retains 42,062,039 conformed records across the candidate network of the Top 25 U.S. commercial airports. Table 4.1 documents the post-ETL data foundation census across all four federal data sources. Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.


Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census*

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSA FOIA Checkpoint Logs | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| BTS On-Time Performance (OTP) | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| BTS Form 41 Schedule T-100 | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| BTS DB1B / DB1C Ticket Surveys | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| Combined Analytical Warehouse | Multi-Source Fact Records | 67,222,828 | 42,062,039 | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

*Note.* Full candidate commercial network across the Top 25 airfields (2019-2025).


Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

| Operational Domain | Variable Name | Sample Size (N) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| TSA Throughput | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| Flight Delays | Flight Departure Delay (minutes) | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| Flight Delays | Significant Delay Rate (>= 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Flight Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| Flight Operations | Runway Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| Flight Operations | Airborne Flight Duration (min) | 13,153,654 | 141.50 | 126.00 | 75.40 | 92.00 | 15.00 | 720.00 | 45.00 | 310.00 |
| Flight Operations | Scheduled Flight Distance (miles) | 13,153,654 | 1,052.12 | 867.00 | 624.80 | 820.00 | 67.00 | 5,095.00 | 230.00 | 2,550.00 |
| Route Capacity | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| Route Capacity | Transported Pax per Route-Month | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| Route Capacity | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| Passenger Surveys | Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

*Note.* Parametric and non-parametric dispersion metrics across 42,062,039 conformed records.

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ( $σ=69,376$ ; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Individual physical screening complexes processed an average hourly throughput of 1,754 passengers, exhibiting significant intraday dispersion ( $σ=1,184$  pax/hr) and reaching peak hourly rushes exceeding 4,800 passengers per hour. See Appendix A for a detailed operational breakdown of descriptive statistics for post-ETL data.


### Temporal Boundaries

A core methodological requirement of this thesis is that defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on individual facility characteristics rather than learning generalizable aviation temporal dynamics.

Post-Pandemic Regime Selection and Structural Break Analysis. Structural break analysis – combining rolling Welch’s  $t$ -tests and Cumulative Sum (CUSUM) trajectory tracking across the Top 25 airports – confirmed May 1, 2022, as the structural equilibrium demarcation point for predictive model development. This demarcation is grounded in three empirical realities: the nationwide rescission of federal transit mask requirements on April 18, 2022, which restored unconstrained traveler behavior and returned domestic passenger load factors to 84.7%; the stabilization of commercial coupling between scheduled flights and screening demand from an artificial pandemic high ( $r=0.607,R^{2}=36.85\%$ ) down to normalized post-recovery equilibrium ( $r=0.553,R^{2}=30.61\%$ ); and the establishment of a clean 32-month development baseline. Table 4.3a in Appendix B details the complete structural break evaluation and statistical demarcation analysis.


### Defining Seasonality

Just as temporal boundaries must be established across the Top 25 network, defining seasonality requires capturing the full empirical variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive peaks (see Appendix C, including Table 4.3b for annual regimes and Table 4.4a for day-of-week archetypes). Formally defining these dimensions enables predictive models to control for cyclical variance, ensuring that model architectures are benchmarked across equivalent operational conditions.


### TSA and OTP Throughput Data

Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airports reveals fundamental econometric dynamics. Refer to Table 4.5 in Appendix D, which synthesizes the master cross-dataset econometric correlations. This analysis provides two distinct insights:

The Hub Disconnect. Raw scheduled flight departures explain only 20.90% ( $R^{2}$ ) of TSA security checkpoint passenger throughput across the Top 25 network ( $r=0.4572,p<0.05$ ). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to 44.94% ( $r=0.6704,p<0.001$ ), an increase of +115%. For instance, major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70% to 76% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.

Asynchronous Delay Propagation and Checkpoint Volatility Coupling. While raw delay rates show weak same-hour linear correlation with passenger volumes ( $r=0.2019,R^{2}=4.08\%$ ), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ( $CV_{TSA}$ ) is significantly coupled with flight departure delay volatility ( $r=0.4375,R^{2}=19.14\%,p<0.05$ ). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume tracks tightly with weekly flight departure delay variance ( $r=0.9022,R^{2}=81.40\%,p<0.01$ ), reflecting synchronized macro peak seasonal demand across the network rather than landside queues causing airside pushback delays.


## Implications for Subset

Establishing temporal boundaries (the May 1, 2022 post-mask demarcation) and seasonal dynamics across the full Top 25 network ensures that baseline operational patterns reflect macroeconomic aviation behavior rather than idiosyncratic facility quirks. To maintain strict methodological integrity and prevent predictive errors, these macro-level seasonal regimes and cross-dataset relationships are not used as direct regression features. Instead, they serve strictly to justify the operational filtering pipeline, inform feature architectures (such as cyclical encodings and lead-lag show-up windows), and establish an uncompromised foundation for downstream modeling.

The exploratory analysis also reveals that commercial airports must initially be evaluated as whole facilities to verify operational scale and hub cluster diversity but cannot be modeled at the aggregate airport level. In shared-terminal facilities, coordinated airline flight banks generate severe multi-carrier collinearity (see appendix for equation) making it mathematically impossible to separate individual airline passenger contributions and restricting explained checkpoint variance to only ~20%. Isolating dedicated, single-carrier screening complexes is therefore essential to eliminate shared-terminal confounding and reveal the true empirical relationship between airline departure banks and landside security queue arrivals.


### Data Filtering and Subset SelectionFour-Phase Filtering Pipeline

To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline alliance code-sharing, a four-phase purposive filtering pipeline was executed across the national commercial airport benchmark network


#### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion): Restricted candidate airfields to the Top 25 U.S. commercial airports by annual scheduled seat capacity and passenger enplanements, ensuring robust sample sizes under persistent heavy-traffic queuing regimes.


#### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion): Excluded Southwest Airlines-dominated airfields (e.g., MDW, DAL) due to point-to-point non-hub routing, unassigned boarding dynamics, and non-reporting in BTS Form 234 delay databases. Excluded airports undergoing massive multi-year terminal reconstructions (e.g., SLC, SEA) that induced non-stationary queuing bottlenecks.


#### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity): Filtered out multi-carrier consolidated checkpoints where passengers from multiple competing airlines pass through shared security lanes. Isolated checkpoints with  $≥90\%$  single-carrier passenger dominance.


#### Phase 4: Factorial Cohort (Factorial Matrix Balance): Balanced the final cohort across legacy network carriers (American, Delta, United) and operational airport clusters (Mega-Connecting Gateways, High-Density O&D Focus, High-Reliability Fortresses, and Congested Coastal Originators).


### Pipeline Results

The filtering pipeline isolated 9 commercial airports representing 12 carrier-exclusive screening environments, achieving complete balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.


Table 4.6  
*The Nine-Airport Experimental Cohort Specification*

| Airport Code | Airport Name | Dominant Legacy Carrier | Carrier Hub Role | Dedicated Terminal Screening Complex | Cluster Archetype | Strategic Justification & Selection Rationale |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BOS | Boston Logan | DL / AA | Dual Focus Station | Terminal A (DL) & Terminal B (AA) | Cluster 1: High-Density O&D Focus | Unconfounded Northeast high-yield O&D demand; physically separate terminal finger piers. |
| DFW | Dallas/Fort Worth | AA | Primary Fortress Hub | Terminal D Screening Complex | Cluster 0: Mega-Connecting Gateway | American Airlines primary mega-connecting fortress hub; high gauge international operations. |
| DTW | Detroit Metro | DL | Primary Fortress Hub | McNamara Terminal Complex | Cluster 2: High-Reliability Fortress | Delta primary Midwest fortress hub; world-class operational fluidity and high connecting ratio. |
| EWR | Newark Liberty | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | United primary East Coast fortress hub; severe New York airspace slot congestion. |
| IAH | Houston Bush | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 1: High-Density O&D Focus | United southern hub; balanced energy sector business O&D travel and Latin American connecting banks. |
| LAX | Los Angeles World | DL / AA / UA | Tri-Carrier Parity Hub | Terminals 2/3 (DL), 4 (AA), 7 (UA) | Cluster 0: Mega-Connecting Gateway | Massive transpacific and transcontinental origin-destination demand across all three legacy carriers. |
| LGA | New York LaGuardia | DL | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | Consolidated Delta Terminal C (opened June 2022); perimeter rule market and pure O&D flows. |
| ORD | Chicago O'Hare | UA / AA | Dual Fortress Hub | Terminal 1 (UA) & Terminal 3 (AA) | Cluster 0: Mega-Connecting Gateway | Intense head-to-head legacy carrier competition; dual hub bank synchronization. |
| PHL | Philadelphia Intl | AA | Primary Fortress Hub | Terminals B & C Complexes | Cluster 2: High-Reliability Fortress | American Mid-Atlantic transatlantic hub; counterpart to Delta's Midwestern fortress at DTW. |

*Note.* Balanced 4x4 factorial design isolating 12 carrier-exclusive terminal complexes across 9 commercial airfields.

To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed: a volume conservation test, a zero-flight intercept test, a cross-carrier orthogonality test, and a terminal layout invariance test (see appendix for details and test statistics).


### Descriptive Statistics for Subset

To evaluate whether the nine-airport experimental cohort accurately reflects the heightened operational stress, flight bank synchronization, and queuing dynamics of major commercial aviation facilities, the cohort's baseline characteristics were contrasted against the nationwide Top 25 benchmark network. As documented in Table 4.7 in Appendix E, this comparative analysis confirms that the filtered subset captures a representative cross-section of high-density operating environments while exhibiting key structural differences that heighten screening sensitivity.

Compared to the broader Top 25 benchmark network, the nine-airport cohort exhibits higher flight movement density (annual mean of 224,576 scheduled departures versus 192,160 network-wide, +16.9%), ensuring that checkpoints operate under heavy, bank-synchronized arrival loads. Second, these facilities experience heightened operational disruption, with average departure delays higher (15.23 min vs. 14.21 min, +7.2%), cancellation rates higher (1.63% vs. 1.43%, +14.1%), and taxi-out times longer (20.59 min vs. 19.69 min). Third, the cohort concentrates demand into landside security screening through a higher local originating passenger share (52.55% vs. 48.61%) and an increase in absolute local originating volume (16.38 million vs. 13.10 million passengers annually, +25.0%). These operational differences confirm that screening queues across the experimental cohort are governed by landside passenger show-up curves rather than airside connecting transfers.

Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airports display distinct local weekly throughput profiles driven by their underlying passenger composition. As reported in Table 4.8 in the appendix, the nine facilities cluster into three operational archetypes: pure corporate markets like LaGuardia that surge on Mondays and Thursdays with steep weekend drops; corporate-to-weekend hubs like Boston, Dallas/Fort Worth, and Detroit that peak on Fridays; and balanced leisure destinations like Los Angeles and Orlando that maintain steady traffic throughout the week. Accounting for these local demand rhythms is critical for security operations, as applying a single generic network schedule would misallocate checkpoint screening lanes on peak days.


### Implications for Model Development

The empirical findings from subset selection establish four mandatory architectural requirements for airport passenger flow modeling:

Single-Carrier Screening Complex Isolation: Passenger throughput must be modeled at dedicated single-carrier screening complexes rather than airport-wide aggregates to eliminate multi-carrier bank confounding and capture terminal-specific arrival surges.

Connecting Passenger Deflation via DB1B Surveys: Departing seat capacity must be deflated by empirical BTS DB1B connecting ratios:

$ρ_{connect}=\frac{Pax_{connect}}{Pax_{total}}$

This deflation prevents the 2.5-fold (+115%) throughput overprediction that occurs when airside connecting passengers at hubs such as DFW, DTW, and ORD are erroneously assumed to enter landside checkpoints.

Strict Prior-Hour Information Availability: Models must enforce strict information barriers by using prior-hour operational indicators (lag  $t-1$ ) and tactical cancellations rather than concurrent departure delays, avoiding lookahead bias since flight delays are unconfirmed until pushback occurs.

Zero-Bounded and Hurdle Formulations: Airport screening complexes exhibit structural zeros during overnight curfew hours (00:00–03:00) and heavy right-skewed arrival surges during daytime departure banks. Standard linear regression assumes normally distributed continuous errors, which can predict physically impossible negative passengers or fail on zero counts. Predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models ( $p=1.3$ ) or two-stage hurdle structures (a logistic model predicting whether the checkpoint is active, followed by a positive count model predicting passenger volume) – to accommodate positive throughput skewness and structural zeros without generating negative volume forecasts.


## Model Development and Execution


### Feature Engineering

A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony. Table 4.9 summarizes the empirical lead-lag correlation across key pre-departure horizons.


Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Volume)*

| Lead-Lag Horizon | Pearson Correlation (r) | Explanatory Power (R^2) | Regression Slope (pax/flight) | Operational & Planning Interpretation |
| :--- | :--- | :--- | :--- | :--- |
| Lag t-1 (1 hr post-departure) | 0.1987 | 3.95% | 16.06 | Passenger has already boarded aircraft; residual correlation is spurious. |
| Same-Hour Departure t (Gate departure) | 0.3403 | 11.58% | 27.49 | Unshifted flight schedule (same hour t) explains only 11.6% of checkpoint variance. |
| Lead t+1 (1 hr pre-departure) | 0.4913 | 24.13% | 39.7 | Captures late-arriving business travelers and carry-on-only passengers. |
| Lead t+2 (2 hr pre-departure) | 0.4876 | 23.78% | 39.4 | Modal show-up window conforming to ACRP Report 40 terminal standards. |
| Lead t+3 (3 hr pre-departure) | 0.38 | 14.44% | 30.7 | Captures early holiday travelers, families, and international check-ins. |
| Convolved Passenger Show-Up Curve | 0.6985 | 48.78% | 74.98 | Empirical passenger show-up curve convolution across lead horizons t+1, t+2, t+3. |
| Show-Up Curve x T-100 Load Factor | 0.7061 | 49.85% | 90.56 | Convolved seats weighted by monthly carrier route load factor. |

*Note.* Evaluated across 72,053 complex-hours on the 2025 holdout dataset.

Unshifted scheduled flights in the same departure hour explain less than 12% of checkpoint throughput variance (r = 0.3403, R² = 11.58%). Explanatory power peaks across the Lead t+1 and Lead t+2 horizons (R² ≈ 24%), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). Convolving scheduled departing seats across a three-hour empirical passenger show-up curve elevates explained variance to 48.8% (r = 0.6985, and weighting by route load factors further increases explanatory power to 49.85% (r = 0.7061). After scaling by booked load factors and deflating airside connecting passengers who never enter landside security, this transformation converts published flight timetables into an accurate baseline forecast of checkpoint queuing demand. See Appendix F for the complete regression specification and slope parameters across all lead-lag horizons.


### Model Training

To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control:

Baseline Control Benchmark (Daily Persistence). Assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion ( $y_{t}=y_{t-24}$ ).

Model 1 (Deterministic Flight Schedule Model). Projects passenger arrival dispersion by convolving scheduled airline flight departure banks across empirical ACRP Report 40 show-up curves ( $w_{1}=0.35$ ,  $w_{2}=0.50$ ,  $w_{3}=0.15$ ), capturing schedule geometry without requiring machine learning or live delay telemetry.

Model 2 (Supervised Machine Learning Model). Uses an automated Gradient-Boosted Decision Tree architecture trained across convolved schedule features and 24 Bureau of Transportation Statistics On-Time Performance operational attributes (cancellations, prior-hour delays, and taxi queues).

Model 3 (Dynamic Two-Stage Hybrid Model). Couples scheduled flight cycles with live prior-hour recursive error correction ( $α=0.35$ ) from actual screening counts to sense passenger accumulation during flight delays.


Table 4.8  
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Cohort Airports*

| Airport Code | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Weekly Peak Day | Weekly Trough Day | Peak/Trough Ratio | Dominant Demand Profile |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| BOS | 48,480 | 42,606 | 45,175 | 50,464 | 52,244 | 44,552 | 49,359 | Friday | Tuesday | 1.23 | Business & Weekend Getaway |
| DFW | 69,808 | 60,600 | 65,285 | 73,310 | 73,625 | 60,733 | 68,963 | Friday | Tuesday | 1.21 | Connecting Bank Synchronization |
| DTW | 35,584 | 30,783 | 32,827 | 37,627 | 37,871 | 30,782 | 36,037 | Friday | Saturday | 1.23 | Midwest Corporate & Connecting |
| EWR | 66,949 | 60,812 | 63,989 | 68,765 | 69,206 | 61,039 | 67,550 | Friday | Tuesday | 1.14 | Coastal Business & Leisure |
| IAH | 52,107 | 45,585 | 47,757 | 53,351 | 50,946 | 42,177 | 52,646 | Thursday | Saturday | 1.26 | Energy Sector Corporate Travel |
| LAX | 99,048 | 87,693 | 92,361 | 100,603 | 101,502 | 89,502 | 103,045 | Sunday | Tuesday | 1.18 | Transcontinental Leisure & Long-Haul |
| LGA | 49,002 | 42,740 | 44,229 | 47,045 | 21,310 | 24,619 | 48,000 | Monday | Friday | 2.3 | Pure Corporate Outbound Profile |
| ORD | 49,381 | 43,406 | 45,713 | 50,706 | 50,620 | 42,697 | 49,468 | Thursday | Saturday | 1.19 | Dual Hub Synchronized Banks |
| PHL | 31,519 | 26,716 | 28,626 | 32,740 | 32,812 | 27,675 | 31,112 | Friday | Tuesday | 1.23 | Mid-Atlantic Fortress Outbound |

*Note.* Average daily screened volume (pax/day) across dedicated carrier complexes.

* **Model Development Dataset Partitions and Calibration Scale**
As shown in Table 4.8, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation, separated by a 7-day operational purge buffer to ensure zero data leakage.


### Model Testing

All candidate architectures were evaluated against the untouched 2025 Full-Year Out-of-Time Holdout Dataset. An out-of-time holdout dataset is a strictly quarantined block of future operational data that was completely withheld during model training, feature engineering, and hyperparameter tuning. Unlike random train/test splits (which shuffle past and future days together and leak temporal autocorrelation), an out-of-time holdout strictly evaluates prospective, forward-looking forecasting accuracy in real-world deployment.

Forecast performance was evaluated against the primary thesis target of diurnal throughput volatility ( $σ_{TSA, hr}$ , defined as the hour-to-hour passenger arrival dispersion across the 24 hours of each day, measured in pax/hr standard deviation) alongside scale-free relative volatility ( $CV_{TSA, hr}=σ/μ$ ). Models were benchmarked across standard operational performance criteria: Coefficient of Determination ( $R^{2}$ ), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias. Please see Appendix G for details on how to interpret these standard operational performance criteria.


### Implications for Final Result Interpretation

When interpreting model evaluation metrics, several operational realities must be considered:

Dispersion Scale vs. Volume Scale: Unlike mean hourly throughput volume (which averages ~1,750 pax/hr across dedicated complexes), diurnal throughput standard deviation averages 540 to 880 passengers per hour across hub complexes. An RMSE of ~220 pax/hr represents an exceptionally close fit to intraday arrival swings.

MASE as the Primary Standard for Volatility Forecasting: MASE normalizes errors against daily persistence:

$MASE=\frac{MAE_{model}}{MAE_{persistence}}=1.000$

A MASE below 0.85 indicates substantial predictive skill beyond historical patterns, while a MASE below 0.70 represents outstanding accuracy.

Conformal Staffing Buffers: Traditional airport staffing models allocate security screening lanes based solely on average expected passenger volume. However, because queuing delays increase non-linearly whenever passenger arrivals surge, staffing strictly for the average guarantees severe line backlogs during peak flight departure banks. To prevent this, airport security administrators can translate predicted throughput volatility directly into a dynamic staffing safety cushion. Rather than opening lanes to match average volume, supervisors add a risk-adjusted buffer proportional to the predicted arrival volatility. This ensures checkpoints maintain sufficient lane capacity to absorb sudden passenger arrival spikes without creating unnecessary, costly over-staffing during calm periods.


## Model Results and Evaluation


### Results

To evaluate the predictive accuracy, operational viability, and behavioral dynamics of the candidate modeling frameworks, each architecture was evaluated against the quarantined 2025 full-year out-of-time holdout dataset. Spanning 3,222 complex-days and 72,053 hourly screening observations across the nine-airport cohort, this prospective evaluation protocol strictly tests forecasting performance under unobserved operating conditions. Predictive performance was benchmarked against the empirical daily persistence control across established error metrics, including the Coefficient of Determination (R²), Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE), and systematic forecast bias. Table 4.10 synthesizes the master benchmark evaluation matrix across all four paradigms, establishing the foundational empirical fit of each predictive framework prior to multi-pillar hypothesis testing.


Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census*

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSA FOIA Checkpoint Logs | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| BTS On-Time Performance (OTP) | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| BTS Form 41 Schedule T-100 | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| BTS DB1B / DB1C Ticket Surveys | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| Combined Analytical Warehouse | Multi-Source Fact Records | 67,222,828 | 42,062,039 | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

*Note.* Full candidate commercial network across the Top 25 airfields (2019-2025).


### General Model Performance Across the 9-Airport Cohort

The empirical results reveal clear performance separations across the modeling paradigms:

The Deterministic Schedule Baseline (Model 1). Relying solely on published flight timetables, Model 1 achieved  $R^{2}=0.4980$ ,  $RMSE=313.4$  pax/hr, and  $MASE=0.945$ . This outperforms daily persistence by 5.5% ( $ΔMASE=-0.055$ ). From an operational perspective, published flight schedules provide a solid structural starting point, explaining approximately half of total checkpoint arrival variance without requiring machine learning infrastructure. However, because Model 1 is completely blind to live flight delays, it consistently under-predicts passenger crowds when delays push travelers into later hours, resulting in a substantial negative forecast bias of -42.1 passengers per hour.

Supervised Machine Learning (Model 2). Adding operational flight data—such as rolling delays, tactical cancellations, and runway taxi times—substantially improves accuracy, elevating out-of-time  $R^{2}$  to 0.6178, reducing RMSE to 273.5 pax/hr, and lowering MASE to 0.779. Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ( $DM=42.15,p<0.0001$ ). In practical terms, incorporating airline flight disruptions cuts forecast error by 22.1% compared to daily persistence and cuts under-prediction bias in half (-18.4 pax/hr). Because Model 2 relies on macro operational indicators available hours in advance rather than live sensor feeds, it is highly practical for routine daily lane scheduling.

The Dynamic Two-Stage Hybrid (Model 3). Incorporating live prior-hour error feedback from actual checkpoint screening counts yielded the highest overall holdout fit, explaining 75.88% of passenger throughput volatility variance ( $R^{2}=0.7588,RMSE=222.1$  pax/hr,  $MASE=0.662$ , Forecast Bias = -4.2 pax/hr). Operationally, the live error feedback loop acts like an automatic safety valve. When severe weather hits and delayed travelers accumulate in terminal lobbies, the model immediately detects that actual passenger throughput exceeds schedule predictions and adjusts its forecast upward. This virtually eliminates systematic forecast bias (-4.2 pax/hr) and delivers a 33.8% error reduction over daily persistence.


### Model Performance and Hypothesis Testings

The thesis hypothesis asserts that distinct modeling frameworks exhibit asymmetric performance strengths across operational robustness, resilience, and generalizability, with no single paradigm proving universally superior across all operational regimes. To test this hypothesis, candidate architectures were evaluated against explicit performance targets defined across three operational dimensions:

Robustness: Evaluates how accurately the model forecasts passenger flow during routine, normal operations when flights are on time (target: MASE < 0.700, lowest RMSE).

Resilience: Evaluates how well the model maintains accuracy during severe flight disruptions, such as severe weather ground stops or de-icing halts (target: shock error ratio near 1.00, lowest shock RMSE, and recovery time under 3 hours).

Generalizability: Evaluates whether a model calibrated on source airports can be deployed to an unfamiliar target airport without retraining (target: transfer error degradation under 10%).


Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census*

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| TSA FOIA Checkpoint Logs | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| BTS On-Time Performance (OTP) | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| BTS Form 41 Schedule T-100 | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| BTS DB1B / DB1C Ticket Surveys | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| Combined Analytical Warehouse | Multi-Source Fact Records | 67,222,828 | 42,062,039 | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

*Note.* Full candidate commercial network across the Top 25 airfields (2019-2025).


### Empirical Confirmation of Asymmetric Trade-Offs

The out-of-time holdout evaluations confirm the thesis hypothesis: no single predictive modeling paradigm is universally superior across all operational regimes. Instead, airport security demand forecasting is governed by fundamental asymmetric trade-offs across robustness, resilience, and generalizability:


#### Dimension 1: Robustness (Nominal & Routine Conditions). Both the Machine Learning model (Model 2, MASE = 0.680) and Dynamic Hybrid (Model 3, MASE = 0.662) achieve the academic target of MASE < 0.700 under routine operations. Under routine operating conditions, when flights operate on schedule, both models track the natural morning and afternoon passenger waves with high precision. However, Model 2 achieves this with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport managers to generate staffing schedules days in advance rather than waiting on live hourly sensor updates.


#### Dimension 2: Resilience (Severe Disruption). The Dynamic Hybrid Framework (Model 3) is the decisive champion of Resilience. During severe weather disruptions, flights are frequently delayed or held on the ground. A pure machine learning model suffers from the "Empty Checkpoint Fallacy"—it assumes that because flights are delayed, security lines must be empty, resulting in massive under-prediction (bias shift of -112.4 pax/hr). In reality, thousands of stranded travelers remain in the terminal lobby. Because Model 3 incorporates live recursive error feedback (α = 0.35), it immediately senses accumulated travelers, cutting disruption error to 284.5 pax/hr (a 39% reduction over Model 2), capping bias shift at -14.8 pax/hr, and returning to normal error levels in just 2.8 hours.


#### Dimension 3: Generalizability (Zero-Shot Portability). The Deterministic Flight Schedule Model (Model 1) is the decisive champion of Generalizability. It successfully meets both stated targets: a transfer MASE of 0.867 and an error degradation of only +4.2% (well within the ≤ 10% threshold). Operationally, because passengers consistently arrive at airports 90 to 120 minutes before their scheduled departure regardless of the city, the basic physical relationship between flight schedules and checkpoint demand works everywhere. Conversely, the Hybrid model (Model 3) degrades by +42.3% (MASE = 0.942) because its machine learning components overfit to the specific concourse layouts, gate geometries, and carrier banking structures of the airports on which it was trained.

The out-of-time holdout evaluations confirm the thesis hypothesis: no single predictive modeling paradigm is universally superior across all operational regimes. Instead, airport security demand forecasting is governed by fundamental asymmetric trade-offs across robustness, resilience, and generalizability. The Dynamic Hybrid model (Model 3) is best during severe flight delays and irregular operations, the Deterministic Schedule model (Model 1) transfers most reliably to new airports without retraining, and the Supervised Machine Learning model (Model 2) is the most practical choice for routine advance staffing. Airport operators and TSA leadership should therefore select their forecasting tool based on daily operating conditions rather than relying on a single method.
