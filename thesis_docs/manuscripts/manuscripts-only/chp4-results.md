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
