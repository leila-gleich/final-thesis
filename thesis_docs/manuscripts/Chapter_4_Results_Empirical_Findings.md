# CHAPTER IV: EMPIRICAL FINDINGS AND MODEL EVALUATION

---

## 4.1 Initial Exploratory Data Analysis

### 4.1.1 Descriptive Statistics (Top 25 Airfields)
To construct an empirically rigorous, leak-free predictive modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw fact records across four federal feeds:
1. **TSA FOIA Checkpoint Logs**: Hourly passenger throughput records disaggregated by physical screening lane.
2. **Bureau of Transportation Statistics (BTS) On-Time Performance (OTP, Form 234)**: Flight-level departure movements tracking scheduled and actual departure times, tarmac taxi-out durations, departure delays, cancellations, and causal delay attributions.
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Monthly carrier-route-equipment records reporting available departing seats, transported revenue passengers, and load factors.
4. **BTS DB1B / DB1C Origin-Destination Ticket Surveys**: A 10% randomized sample of airline passenger itineraries detailing coupon routes, connecting transfer ratios, and true local originating passenger fractions.

Following conformed extraction, automated entity resolution, data cleaning, and star-schema relational synthesis across conformed dimension keys (`dim_date`, `dim_time_block`, `dim_airport`, `dim_airline`, `dim_aircraft`, `dim_checkpoint`), the nationwide post-ETL analytical warehouse retains **42,062,039 conformed records** across the candidate network of the Top 25 U.S. commercial airfields. Table 4.1 documents the post-ETL data foundation census across all four federal data sources.

#### Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)

| Primary Data Feed | Entity Grain | Raw Ingested Rows | Post-ETL Cleaned Rows | Network & Facility Coverage | Conformance & Data Health Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **TSA FOIA Checkpoint Logs** | Checkpoint-Lane-Hour | 19,500,286 | **6,434,732** | 25 Airfields, 955 Screening Lanes | 100% Non-Null; Zero Orphans; 2.70 Billion Passengers Screened |
| **BTS On-Time Performance (OTP)** | Flight Departure | 45,777,091 | **13,153,654** | 25 Airfields, 17 Reporting Carriers | 100% Non-Null Dimensions; 13.15 Million Domestic Departures Tracking Delays & Cancels |
| **BTS Form 41 Schedule T-100** | Carrier-Route-Month | 1,945,451 | **422,096** | 25 Airfields, 18 Operating Carriers | 100% Non-Null Dimensions; 2.09 Billion Departing Seats, 1.70 Billion Passengers |
| **BTS DB1B / DB1C Ticket Surveys** | Ticket Coupon Itinerary | 12,910,384 | **22,051,557** | Closed 25-Airport City Pairs | 100% Non-Null Dimensions; 22.05 Million Coupon Records (62.16 Million Ticketed Travelers) |
| **Combined Analytical Warehouse** | Multi-Source Fact Records | **67,222,828** | **42,062,039** | Full 25-Airfield Candidate Network | Comprehensive conformed relational warehouse; 100% referential integrity |

Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

#### Table 4.2: Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)

| Operational Domain | Variable Name | Sample Size ($N$) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **TSA Throughput** | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| **Flight Delays** | Flight Departure Delay (minutes) | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| **Flight Delays** | Significant Delay Rate ($\ge$ 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| **Flight Operations** | Flight Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| **Flight Operations** | Runway Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| **Flight Operations** | Airborne Flight Duration (min) | 13,153,654 | 141.50 | 126.00 | 75.40 | 92.00 | 15.00 | 720.00 | 45.00 | 310.00 |
| **Flight Operations** | Scheduled Flight Distance (miles) | 13,153,654 | 1,052.12 | 867.00 | 624.80 | 820.00 | 67.00 | 5,095.00 | 230.00 | 2,550.00 |
| **Route Capacity** | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| **Route Capacity** | Transported Pax per Route-Month | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| **Route Capacity** | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| **Passenger Surveys**| Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

At the macro level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($\sigma = 69,376$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually ($\sigma = 27.76\text{M}$; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period.

Three essential data hygiene protocols were established during warehouse staging:
1. **Spatial Key Resolution and Metadata Remediation**: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (`dim_checkpoint`). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (`airportId = 0`, flagged with `airportMissing = 1`), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce `WHERE airportMissing = 0 AND airportId > 0`.
2. **Physical Checkpoint Closures vs. Missing Sensor Data**: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through Tweedie compound Poisson distributions ($p = 1.3$) or two-stage hurdle structures.
3. **Advance vs. Tactical Cancellation Causality**: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting, advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.

---

### 4.1.2 Temporal Baselines and Seasonal Dynamics (Top 25 Airfields)
A core methodological requirement of this thesis is that **defining temporal boundaries (specifically post-COVID recovery regimes) and seasonal dynamics (annual cycles and day-of-week patterns) must be performed on the broad Top 25 airport dataset**. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes and calendar dynamics were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on idiosyncratic facility characteristics rather than learning generalizable aviation temporal dynamics.

#### Post-Pandemic Regime Selection and Structural Break Analysis
The seven-year dataset captures two unprecedented macroeconomic disruptions: the COVID-19 pandemic demand collapse (2020–2021) and the post-pandemic operational rebound (2022–2025). To identify the point at which commercial aviation resumed structural equilibrium, rolling Welch's $t$-tests, Cumulative Sum (CUSUM) structural break tests, and longitudinal correlation metrics were computed across the Top 25 airfields. Table 4.3a contrasts the candidate temporal demarcation baselines.

#### Table 4.3a: Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network

| Evaluation Criteria | Candidate A: Mature Post-Pandemic | Candidate B: Early Post-Mask Regime *(Selected)* |
| :--- | :--- | :--- |
| **Start Date** | January 1, 2023 | **May 1, 2022 (RECOMMENDED)** |
| **Statistical Demarcation Rationale** | Rolling Welch's $t$-test variance convergence | CUSUM structural break stabilization; Mask Mandate Repeal |
| **Training Span** | 24 Months (2023-01 to 2024-12) | **32 Months (2022-05 to 2024-12; 20 mo train / 12 mo val)** |
| **Holdout Test Span** | 12 Months (2025 Full-Year Holdout) | **12 Months (2025 Full-Year Holdout)** |
| **Robustness Impact** | Excellent baseline stability; limited historical depth | **Superior: Captures two complete annual seasonal cycles** |
| **Resilience Impact** | Misses Winter Storm Elliott (Dec 2022) | **Superior: Encapsulates severe winter freeze and summer storms** |
| **Generalizability Impact** | Narrower training variance across spoke airfields | **Superior: 404,324 candidate multi-facility hourly records** |
| **Coupling Rebound ($R^2$)** | $R^2 = 0.323$ (Macro scheduled-to-TSA daily) | **$R^2$ rebounds from 0.368 (COVID) to 0.306–0.323 (Equilibrium)** |

Structural break tests confirmed **May 1, 2022** as the optimal demarcation point for empirical model development:
1. **Federal Transit Mask Mandate Repeal**: The nationwide vacatur of federal transit mask requirements on April 18, 2022 restored unconstrained business and leisure travel behavior. By May 1, 2022, load factors recovered to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stability**: During the acute pandemic (2020–2021), the correlation between scheduled flights and checkpoint throughput spiked to an artificial $r = 0.607$ ($R^2 = 36.85\%$) because airline capacity cuts mirrored strict travel bans. In the post-May 2022 equilibrium, the relationship stabilized to $r = 0.553$ ($R^2 = 30.61\%$), reflecting normalized booking curves.
3. **Partitioning Design**: Candidate B establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations; 215,562 facility-level observations). A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.

#### Annual Seasonal Regimes and Coupled Volatility
Airport operational stress is not uniform across the year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b).

#### Table 4.3b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

| Seasonal Regime | Operational Regime Description | Calendar Days ($N$) | Share of Days (%) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) | Cancellation Rate (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`1_OFF_PEAK`** | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | **27.85** | 9.85 min | 18.00% | 0.89% |
| **`2_MID_PEAK`** | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | **32.38** | 15.14 min | 23.23% | 1.36% |
| **`3_PEAK`** | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | **39.36** | 24.17 min | 31.04% | 3.16% |
| **`4_HOLIDAY`** | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | **33.07** | 16.51 min | 24.33% | 1.82% |

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$) from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

#### Day-of-Week Cyclical Dynamics and Archetypes
Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes (Table 4.4a):
1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($19.44\%$ and $20.05\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

#### Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)

| Day of Week | DOW Name | Operational Volatility Archetype | Study Days ($N$) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Monday | Outbound Business Surge & High Screening Volatility | 192 | 1,246,150 | **0.604** | 56.56 min | **34.00** | 15.78 min | 23.54% |
| **2** | Tuesday | Midweek Operational Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | **50.09 min** | **29.99** | 11.69 min | 19.44% |
| **3** | Wednesday | Midweek Baseline Stability (Minimum Volatility) | 192 | 1,123,368 | 0.594 | **49.27 min** | **29.13** | 12.22 min | 20.05% |
| **4** | Thursday | Corporate Outbound & Early Weekend Ramp | 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| **5** | Friday | Combined Business & Weekend Getaway Surge | 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| **6** | Saturday | Volume Trough & Fleet Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| **7** | Sunday | Leisure Return Peak & Evening Delay Propagation | 192 | 1,279,017 | 0.577 | **58.07 min** | **33.40** | **17.78 min** | **25.60%** |

#### Diurnal Non-Consecutive Dual Turbulence Peaks
Rather than dividing the 24 hours of each operational day into arbitrary consecutive time blocks, diurnal hours were categorized by the Operational Turbulence Shock Index ($T(h)$), which evaluates passenger screening surge volatility and flight departure delay dispersion:
* **`1_OFF_PEAK` (Overnight & Curfew Valley)**: Typically covering 00:00 to 03:00 (3–4 hours/day), where commercial departures are sparse and checkpoint demand is quiescent.
* **`2_MID_PEAK` (Midday Plateau & Transition)**: Covering 08:00 to 13:00/16:00 (4–12 hours/day), characterized by steady passenger screening flow and balanced aircraft turnaround buffers.
* **`3_PEAK` (High Queuing Turbulence / Dual Peaks)**: Uniquely groups non-consecutive turbulence periods into a single operational regime:
  1. *Morning Bank Surge (05:00–08:00)*: Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr).
  2. *Evening Delay Cascade (14:00/17:00–22:00)*: Driven by upstream flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min).

The cross-classification of the 4 annual seasonal regimes ($\mathcal{S}$), 7 days of the week ($\mathcal{D}$), and 3 diurnal blocks ($\mathcal{H}$) forms an **84-cell interaction tensor** ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$). Across this tensor, 83 of 84 cells (98.8%) satisfy the statistical minimum power threshold of $N_{\text{train}} \ge 50$ (median $N_{\text{train}} = 215$), confirming that defining temporal baselines on the Top 25 airfields establishes ample sample power without sparse-sample estimation bias.

---

### 4.1.3 Relationship Between TSA Throughput and OTP Data (Top 25 Airfields)
Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airfields reveals fundamental econometric dynamics. Table 4.5 synthesizes the master cross-dataset econometric correlations.

#### Table 4.5: Master Cross-Dataset Econometric Relationships (Top 25 Airfields)

| Relationship Category | Metric 1 (OTP / Capacity) | Metric 2 (TSA Demand / Queue) | Sample Grain | Pearson $r$ | $R^2$ (%) | $t$-statistic | $p$-value | Operational Significance & Interpretation |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Volume Coupling** | Raw Scheduled Flight Departures | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.4572 | 20.90% | 2.47 | $< 0.05$ | Modest linear coupling; scheduled flights alone explain only 20.9% of checkpoint passenger variance due to connecting passenger volume. |
| **Connecting Deflation** | Raw Scheduled Flight Departures | True Local Originating TSA Demand | Top 25 Airfields | **0.6704** | **44.94%** | 4.33 | $< 0.001$ | Strong linear coupling; removing connecting transfers via DB1B ticket surveys increases explained variance by +115% (from 20.9% to 44.9%). |
| **Hub Scale vs. Connecting**| Connecting Passenger Ratio (%) | Scheduled Flight Volume | Top 25 Airfields | 0.4503 | 20.28% | 2.42 | $< 0.05$ | Hub scale effect; larger airline hub operations inherently possess higher connecting passenger fractions (e.g., CLT 76.0%, ATL 70.1%). |
| **Surface Queue Feedback** | Runway Taxi-Out Queue Time (min) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2867 | 8.22% | 1.44 | $0.163$ | Directional trend; airports processing higher passenger volumes with larger aircraft experience longer tarmac taxi queues. |
| **Surface-to-Air Feedback** | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | 63,925 Airport-Days | **0.4971** | **24.71%** | 2.74 | $< 0.001$ | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
| **Schedule Delay Coupling** | Significant Delays (DepDel15 %) | Total TSA Checkpoint Throughput | Top 25 Airfields | 0.2019 | 4.08% | 0.99 | $0.332$ | Weak coupling; flight delay rates are primarily governed by convective weather and ATC ground delay programs rather than landside volume. |
| **Hourly Volatility Transmission** | Hourly TSA Throughput Volatility ($CV$) | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | **0.4375** | **19.14%** | 2.33 | $< 0.05$ | Direct operational coupling; spiky passenger arrivals at checkpoints inject variance into boarding gate closures and pushback times. |
| **Daily Volatility Coupling** | Daily TSA Throughput Volatility ($CV$) | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | 0.3714 | 13.79% | 1.92 | $0.067$ | Day-to-day checkpoint throughput dispersion tracks daily flight departure delay dispersion across the network. |
| **Surge vs. Delay Volatility** | Hourly TSA Peak-to-Median Surge Ratio | Flight Departure Delay Volatility ($CV$) | Top 25 Airfields | 0.3480 | 12.11% | 1.78 | $0.088$ | Airfields with sharp peak-to-median checkpoint rushes experience heightened schedule volatility. |
| **Weekly Cyclical Coupling** | Day-of-Week Mean Daily TSA Pax | Day-of-Week Mean Departure Delay (min) | 7 Days ($N=7$) | **0.9022** | **81.40%** | 4.68 | $< 0.01$ | Deterministic weekly cadence; weekly passenger surge days (Sunday/Monday) explain 81.4% of weekly departure delay variance. |
| **Weekly Delay Rate Coupling**| Day-of-Week Mean Daily TSA Pax | Day-of-Week DepDel15 Rate (%) | 7 Days ($N=7$) | **0.9000** | **81.00%** | 4.62 | $< 0.01$ | Weekly passenger volume peaks directly produce the week's highest flight delay rates (Sunday DepDel15 = 20.55%). |
| **Annual Monthly Coupling** | Monthly Mean Daily TSA Pax | Monthly Mean Departure Delay (min) | 12 Months ($N=12$) | **0.6313** | **39.85%** | 2.57 | $< 0.05$ | Summer peak alignment; summer passenger surges coincide with peak convective thunderstorm delays in June and July. |

Two overarching empirical insights emerge from Table 4.5:
1. **The Hub Disconnect**: Raw scheduled flight departures explain only 20.90% ($R^2$) of TSA security checkpoint passenger throughput across the Top 25 network ($r = 0.4572, p < 0.05$). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to **44.94%** ($r = 0.6704, p < 0.001$), an increase of +115%. At major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70% to 76% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.
2. **Coupled Volatility and Asynchronous Lag Dynamics**: While raw delay rates show weak contemporaneous linear correlation with passenger volumes ($r = 0.2019, R^2 = 4.08\%$), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ($CV_{\text{TSA}}$) is significantly coupled with flight departure delay volatility ($r = 0.4375, R^2 = 19.14\%, p < 0.05$). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume explains **81.40%** of weekly flight departure delay variance ($r = 0.9022, p < 0.01$).

---

### 4.1.4 Implications for Subset and Filtering of Seasonal Dynamics and TSA-OTP Relationships
The findings from the Top 25 exploratory data analysis establish critical empirical foundations and constraints for subsequent data filtering and model development:
1. **Necessity of Macro-Scale Baseline Derivation**: Establishing temporal boundaries (May 1, 2022 post-mask demarcation) and seasonal dynamics (the 4-regime annual calendar, 3 weekly archetypes, and diurnal dual-peak blocks) on the complete Top 25 network ensures that statistical baselines reflect macroeconomic aviation behavior rather than localized facility noise. This prevents models from overtraining on idiosyncratic scheduling quirks of individual hubs.
2. **Identification of Multi-Carrier Schedule Collinearity**: In shared terminal facilities across the Top 25 airfields, hub carriers coordinate departure banks. Carrier departure schedules exhibit extreme collinearity ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), making it mathematically impossible to separate individual airline passenger contributions in shared checkpoint queues.
3. **Requirement for Checkpoint-Level Carrier Exclusivity**: Because contemporaneous scheduled departures explain only ~20% of raw checkpoint variance at the airport-wide level, isolating pure carrier-checkpoint pairs where single-carrier operations feed dedicated screening lanes is essential to unmask the true physical lead-lag relationship between flight schedules and landside arrivals.
4. **Strict Partitioning Between Macro Dynamics and Feature Training**: While the Top 25 dataset uncovers seasonal dynamics, cyclical archetypes, and cross-dataset correlations, **these relationships and dynamics must not be used as direct trained regression targets or predictive leakage within the downstream model**. Instead, they justify the purposive filtering pipeline, inform feature architectures (e.g., lead-lag arrival distributions and cyclical encodings), and guide the selection of candidate airfields for experimental modeling.

---

## 4.2 Data Filtering and Subset Selection

### 4.2.1 The Four-Phase Filtering Pipeline
To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, commercial airfields were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   PHASE 1: MACRO FILTER (Scale & Congestion)                │
│  Universe: 450+ U.S. Commercial Airfields  ──►  Retained: Top 25 Airfields  │
│  • Enforces queue intensity ρ(t) -> 1.0 during departure banks              │
│  • Captures 67.2% of national domestic flight departures                    │
│  • Raw Flight vs. TSA Throughput: r = 0.4572, R² = 20.90%                   │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 PHASE 2: MESO FILTER (Symmetry & Invariance)                │
│  Universe: Top 25 Airfields  ──────────────►  Retained: 14 Candidate Hubs   │
│  • Requires concurrent AA, DL, UA mainline presence (>10% seat share)       │
│  • Excludes Southwest (WN) bimodal arrival mixtures and ULCC noise          │
│  • Airspace ground delays (δ_t) affect carriers symmetrically                │
│  • Scheduled Flights vs. TSA Throughput: r = 0.5015, R² = 25.15%            │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                PHASE 3: MICRO FILTER (Checkpoint Exclusivity)               │
│  Universe: 14 Candidate Airfields  ────────►  Retained: 9 Selected Hubs     │
│  • Strict dedicated terminal checkpoints (P(Carrier = j* | Checkpoint) = 1) │
│  • Eliminates shared-terminal carrier collinearity (κ collapses < 25)       │
│  • Airport-level coupling: Raw r = 0.5453 (R² = 29.74%);                    │
│    DB1B Local Originating: r = 0.6466 (R² = 41.81%)                         │
└──────────────────────────────────────┬──────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│               PHASE 4: FACTORIAL COHORT (Factorial Matrix Balance)          │
│  Universe: 9 Selected Hubs  ───────────────►  Cohort: 9 Airfields           │
│  (12 Dedicated Screening Complexes)                                         │
│  • Exactly 4 dedicated complexes per legacy carrier (AA: 4, DL: 4, UA: 4)   │
│  • Complete representation across all 4 operational cluster archetypes      │
│  • Dedicated Checkpoint-to-Flight Coupling: R² = 70.80% to 77.40%            │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion)
* **Filtering Criteria**: Restrict the national candidate universe of 450+ commercial airports to the Top 25 commercial airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* **Methodological Justification**: In airport queueing dynamics, traffic intensity $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$ determines queue behavior. At small regional airports, passenger flow is sparse ($\rho(t) \ll 0.3$), preventing queue accumulation and causing throughput to mirror unconstrained arrivals without boundary friction. In contrast, Top 25 hub airports reach peak-hour saturation ($\rho(t) \to 1.0$) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue delays and non-linear dynamics required to train and evaluate congestion-aware models.
* **TSA-OTP Relationship Evolution**: Across the nationwide universe of all commercial airfields, the linear correlation between scheduled flight departures and TSA throughput is low ($r \approx 0.35, R^2 \approx 12.25\%$). At the Top 25 macro scale, this relationship strengthens to $r = 0.4572$ ($R^2 = 20.90\%$) for raw volume, and $r = 0.6704$ ($R^2 = 44.94\%$) when deflated by DB1B connecting ratios.

#### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion)
* **Filtering Criteria**: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ($>10\%$ market share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* **Methodological Justification**: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical exogenous airspace conditions ($\delta_t$), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to its passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \approx 105\text{ min}$), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ($\mu_1 \approx 135\text{ min}$ for boarding group maximizers; $\mu_2 \approx 65\text{ min}$ for carry-on business travelers), violating arrival distribution homogeneity.
* **TSA-OTP Relationship Evolution**: In the 14-airfield Meso cohort, eliminating Southwest and ULCC scheduling volatility elevated the scheduled flight to TSA throughput correlation to $r = 0.5015$ ($R^2 = 25.15\%$).

#### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity)
* **Filtering Criteria**: Require strict single-carrier dedicated screening checkpoint complexes ($P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* **Methodological Justification**: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), preventing econometric deconvolution of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint queues.
* **TSA-OTP Relationship Evolution**: At the airport-wide level for the 9 selected airfields, scheduled flights versus total TSA passengers achieve $r = 0.5453$ ($R^2 = 29.74\%$), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r = 0.6466$ ($R^2 = 41.81\%$). Furthermore, when evaluated at the dedicated checkpoint complex level, carrier-filtered departing seats explain **70.80% to 77.40%** ($R^2$) of checkpoint throughput variance.

#### Phase 4: Factorial Cohort (Factorial Matrix Balance)
* **Filtering Criteria**: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the **9-Airport Experimental Cohort** comprising **12 Dedicated Checkpoint Complexes** across **BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL**.
* **Methodological Justification**: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters, ensuring unconfounded cross-carrier and cross-airport transfer evaluation.
* **Crucial Methodological Distinction**: These evolving correlations and seasonal dynamics serve exclusively to justify the four-tier filtering rationale and confirm data validity. **These relationships and dynamics are not used in training the downstream predictive models**, preserving strict econometric separation and preventing data leakage. Furthermore, the analysis at this stage evaluates the **9 selected airports as complete facilities**, rather than premature facility checkpoints.

---

### 4.2.2 Pipeline Results: The Selected 9-Airport Experimental Cohort
The filtering pipeline isolated 9 commercial airfields representing 12 carrier-exclusive screening environments, achieving complete factorial balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

#### Table 4.6: The 9-Airport Experimental Cohort Factorial Specification

| Airport Code | Airport Name | Dominant Legacy Carrier | Carrier Hub Role | Dedicated Terminal Screening Complex | Cluster Archetype | Strategic Justification & Selection Rationale |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- |
| **BOS** | Boston Logan | DL / AA | Dual Focus Station | Terminal A (DL) & Terminal B (AA) | Cluster 1: High-Density O&D Focus | Unconfounded Northeast high-yield O&D demand; physically separate terminal finger piers. |
| **DFW** | Dallas/Fort Worth | AA | Primary Fortress Hub | Terminal D Screening Complex | Cluster 0: Mega-Connecting Gateway | American Airlines primary mega-connecting fortress hub; high gauge international operations. |
| **DTW** | Detroit Metro | DL | Primary Fortress Hub | McNamara Terminal Complex | Cluster 2: High-Reliability Fortress | Delta primary Midwest fortress hub; world-class operational fluidity and high connecting ratio. |
| **EWR** | Newark Liberty | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | United primary East Coast fortress hub; severe New York airspace slot congestion. |
| **IAH** | Houston Bush | UA | Primary Fortress Hub | Terminal C Screening Complex | Cluster 1: High-Density O&D Focus | United southern hub; balanced energy sector business O&D travel and Latin American connecting banks. |
| **LAX** | Los Angeles World | DL / AA / UA | Tri-Carrier Parity Hub | Terminals 2/3 (DL), 4 (AA), 7 (UA) | Cluster 0: Mega-Connecting Gateway | Massive transpacific and transcontinental origin-destination demand across all three legacy carriers. |
| **LGA** | New York LaGuardia | DL | Primary Fortress Hub | Terminal C Screening Complex | Cluster 3: Congested Coastal Originator | Consolidated Delta Terminal C (opened June 2022); perimeter rule market and pure O&D flows. |
| **ORD** | Chicago O'Hare | UA / AA | Dual Fortress Hub | Terminal 1 (UA) & Terminal 3 (AA) | Cluster 0: Mega-Connecting Gateway | Intense head-to-head legacy carrier competition; dual hub bank synchronization. |
| **PHL** | Philadelphia Intl | AA | Primary Fortress Hub | Terminals B & C Complexes | Cluster 2: High-Reliability Fortress | American Mid-Atlantic transatlantic hub; counterpart to Delta's Midwestern fortress at DTW. |

#### Key Airport Selection Contrasts
* **LGA vs. JFK Selection**: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's state-of-the-art consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* **PHL vs. SLC Selection**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation physically impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring carrier isolation within Cluster 2.

---

### 4.2.3 Differences in Seasonal Dynamics for the Selected 9 Airports
While seasonal and day-of-week baselines were established across the Top 25 network, the 9 selected airfields display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.7 reports the day-of-week passenger throughput distribution across the 9 airports.

#### Table 4.7: Day-of-Week Mean Daily Passenger Throughput Across the 9 Selected Airports

| Airport Code | Monday | Tuesday | Wednesday | Thursday | Friday | Saturday | Sunday | Weekly Peak Day | Weekly Trough Day | Peak/Trough Ratio | Dominant Demand Profile |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **BOS** | 48,480 | 42,606 | 45,175 | 50,464 | **52,244** | 44,552 | 49,359 | Friday | Tuesday | 1.23 | Business & Weekend Getaway |
| **DFW** | 69,808 | 60,600 | 65,285 | 73,310 | **73,625** | 60,733 | 68,963 | Friday | Tuesday | 1.21 | Connecting Bank Synchronization |
| **DTW** | 35,584 | 30,783 | 32,827 | 37,627 | **37,871** | 30,782 | 36,037 | Friday | Saturday | 1.23 | Midwest Corporate & Connecting |
| **EWR** | 66,949 | 60,812 | 63,989 | 68,765 | **69,206** | 61,039 | 67,550 | Friday | Tuesday | 1.14 | Coastal Business & Leisure |
| **IAH** | 52,107 | 45,585 | 47,757 | **53,351** | 50,946 | 42,177 | 52,646 | Thursday | Saturday | 1.26 | Energy Sector Corporate Travel |
| **LAX** | 99,048 | 87,693 | 92,361 | 100,603 | 101,502 | 89,502 | **103,045** | Sunday | Tuesday | 1.18 | Transcontinental Leisure & Long-Haul |
| **LGA** | **49,002** | 42,740 | 44,229 | 47,045 | 21,310 | 24,619 | 48,000 | Monday | Friday | **2.30** | Pure Corporate Outbound Profile |
| **ORD** | 49,381 | 43,406 | 45,713 | **50,706** | 50,620 | 42,697 | 49,468 | Thursday | Saturday | 1.19 | Dual Hub Synchronized Banks |
| **PHL** | 31,519 | 26,716 | 28,626 | 32,740 | **32,812** | 27,675 | 31,112 | Friday | Tuesday | 1.23 | Mid-Atlantic Fortress Outbound |

The 9 airports exhibit three distinct weekly demand dynamics:
1. **The Pure Corporate Profile (LGA)**: LaGuardia exhibits an extreme day-of-week ratio of **2.30**. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.
2. **The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW)**: These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).
3. **The Energy Sector & Midweek Profile (IAH, ORD)**: Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate corporate travel schedules, followed by steep Saturday troughs.

---

### 4.2.4 Descriptive Statistics for the Selected 9-Airport Subset
Table 4.8 presents the descriptive summary statistics for the 9-airport experimental cohort compared against the Top 25 candidate universe.

#### Table 4.8: Summary Descriptive Statistics: 9-Airport Experimental Cohort vs. Top 25 Universe

| Metric Category | Operational Metric | Unit | 9-Airport Mean | 9-Airport Std Dev | 9-Airport Median | 9-Airport Min (Airport) | 9-Airport Max (Airport) | Top 25 Mean | Delta (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **BTS OTP Operations** | Scheduled Domestic Flights | flights | 224,576 | 78,441 | 206,024 | 138,372 (PHL) | 360,571 (ORD) | 192,160 | +16.9% |
| **BTS OTP Operations** | Cancelled Flights | flights | 3,623 | 1,599 | 2,920 | 1,777 (DTW) | 6,515 (DFW) | 2,738 | +32.3% |
| **BTS OTP Operations** | Flight Cancellation Rate | % | 1.63% | 0.50% | 1.47% | 0.99% (LAX) | 2.46% (LGA) | 1.43% | +14.1% |
| **BTS OTP Delays** | Average Departure Delay | min | 15.23 | 2.75 | 15.65 | 11.55 (DTW) | 19.85 (DFW) | 14.21 | +7.2% |
| **BTS OTP Delays** | Significant Delay Rate ($\ge$ 15m) | % | 21.42% | 3.30% | 20.14% | 17.93% (LAX) | 28.07% (DFW) | 20.31% | +5.5% |
| **BTS OTP Delays** | Runway Taxi-Out Queue Time | min | 20.59 | 2.58 | 20.35 | 16.96 (DTW) | 24.67 (EWR) | 19.69 | +4.5% |
| **TSA Checkpoint** | Total Passenger Throughput | pax | 71,145,628 | 27,465,238 | 63,720,916 | 40,429,531 (PHL) | 129,069,341 (LAX) | 68,495,531 | +3.9% |
| **TSA Checkpoint** | Average Daily Passenger Count | pax/day | 53,075 | 20,473 | 47,553 | 30,171 (PHL) | 96,249 (LAX) | 51,138 | +3.8% |
| **TSA Checkpoint** | Average Hourly Passenger Count | pax/hr | 418.53 | 157.02 | 388.40 | 239.60 (ORD) | 662.40 (LGA) | 540.34 | -22.5% |
| **TSA Checkpoint** | Peak Single-Hour Checkpoint Rush | pax/hr | 2,673 | 881 | 2,654 | 1,385 (DTW) | 4,020 (EWR) | 2,784 | -4.0% |
| **TSA Checkpoint** | Demand Volatility ($CV_{\text{TSA}}$) | ratio | 0.8728 | 0.2000 | 0.9064 | 0.6488 (BOS) | 1.1240 (LGA) | 0.8250 | +5.8% |
| **BTS DB1B Surveys** | Connecting Passenger Share | % | 47.45% | 10.98% | 44.41% | 33.58% (EWR) | 66.32% (DFW) | 51.39% | -7.7% |
| **BTS DB1B Surveys** | Local Originating Passenger Share | % | 52.55% | 10.98% | 55.59% | 33.68% (DFW) | 66.42% (EWR) | 48.61% | +8.1% |
| **BTS DB1B Surveys** | True Local Originating TSA Demand | pax | 16,376,561 | 5,167,458 | 15,995,278 | 10,555,299 (DTW) | 26,293,897 (LAX) | 13,103,484 | +25.0% |
| **T-100 Aircraft Gauge** | Seating Capacity per Flight | seats | 168.42 | 7.49 | 168.00 | 154.20 (LGA) | 182.30 (LAX) | 171.10 | -1.6% |
| **T-100 Load Factor** | Route Passenger Load Factor | % | 85.08% | 0.82% | 85.26% | 83.85% (DTW) | 86.12% (EWR) | 84.73% | +0.4% |

Compared to the broader Top 25 network, the 9-airport cohort exhibits:
* **Higher Flight Movement Density**: Scheduled flights are +16.9% higher (224,576 vs. 192,160), ensuring that screening checkpoints operate under heavy, bank-synchronized arrival loads.
* **Higher Delay and Cancellation Exposure**: Average departure delay is +7.2% higher (15.23 min vs. 14.21 min), cancellation rate is +14.1% higher (1.63% vs. 1.43%), and taxi-out time is +4.5% higher (20.59 min vs. 19.69 min), reflecting genuine operational congestion.
* **Higher Local Originating Demand**: Local originating passenger share is +8.1% higher (52.55% vs. 48.61%), and true local originating volume is +25.0% higher (16.38M vs. 13.10M), concentrating demand directly into landside security checkpoint queues.

---

### 4.2.5 Implications for Model Selection
The empirical findings from subset selection dictate essential modeling choices:
1. **Separation of Dedicated Checkpoint Complexes from Airport Aggregates**: Modeling passenger security throughput at the entire airport level confounds multi-carrier flight banks and masks terminal-specific surges. Models must be trained and evaluated at the **dedicated screening complex grain** ($Y_{kt}$), mapping carrier-exclusive flight banks to dedicated screening lanes.
2. **Deflating Capacity by Connecting Ratios**: Because connecting passengers bypass security queues, departing flight seats must be deflated by $(1 - \text{ConnectingRatio}_{\text{airport}})$ from DB1B surveys. Failure to apply this deflator causes models to overpredict checkpoint volume by over 200% at connecting hubs (DFW, DTW, ORD).
3. **Handling Asymmetric Delay Information**: Contemporaneous delay information cannot be included directly without causing lookahead bias. Instead, prior-hour delays ($t-1$) and tactical cancellations provide actionable indicators of terminal congestion.
4. **Zero-Bounded Distributional Assumptions**: Checkpoint throughput data exhibits positive skewness and structural zeros during overnight curfews. Standard ordinary least squares (OLS) regression produces negative predictions during night hours. Models must incorporate zero-bounded formulations, such as Tweedie compound Poisson generalized linear models ($p = 1.3$) or two-stage hurdle structures.

---

## 4.3 Model Development and Execution

### 4.3.1 Feature Engineering and Passenger Show-Up Curve Estimation
A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

#### Table 4.9: Empirical Lead-Lag Transfer Dynamics (Scheduled Flights vs. Checkpoint Demand)

| Lead-Lag Horizon | Pearson Correlation ($r$) | Explanatory Power ($R^2$) | Regression Slope (pax/flight) | Operational & Planning Interpretation |
| :--- | :---: | :---: | :---: | :--- |
| **Lag $t-1$ (1 hr post-departure)** | 0.1987 | 3.95% | 16.06 | Passenger has already boarded aircraft; residual correlation is spurious. |
| **Contemporaneous $t$ (Gate departure)** | 0.3403 | 11.58% | 27.49 | Contemporaneous flight schedule explains only 11.6% of checkpoint variance. |
| **Lead $t+1$ (1 hr pre-departure)** | 0.4913 | 24.13% | 39.70 | Captures late-arriving business travelers and carry-on-only passengers. |
| **Lead $t+2$ (2 hr pre-departure)** | **0.4876** | **23.78%** | **39.40** | **Modal show-up window conforming to ACRP Report 40 terminal standards.** |
| **Lead $t+3$ (3 hr pre-departure)** | 0.3800 | 14.44% | 30.70 | Captures early holiday travelers, families, and international check-ins. |
| **Convolved Passenger Show-Up Curve** | **0.6985** | **48.78%** | **74.98** | **Full lead-lag kernel deconvolution across $t+1, t+2, t+3$.** |
| **Show-Up Curve $\times$ T-100 Load Factor** | **0.7061** | **49.85%** | **90.56** | **Convolved seats weighted by monthly carrier route load factor.** |

Contemporaneous scheduled flights explain less than 12% of checkpoint throughput variance. Explanatory power peaks across the Lead $t+1$ and Lead $t+2$ horizons ($R^2 \approx 24\%$), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (**ACRP Report 40: Airport Passenger Terminal Planning and Design**).

Based on these findings, an empirical passenger arrival kernel was constructed by convolving scheduled departing seats across lead horizons ($t+1, t+2, t+3$):
$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$$
where weights $w_1 = 0.35$, $w_2 = 0.50$, and $w_3 = 0.15$ match empirical ACRP Report 40 arrival distributions.

The complete feature engineering pipeline encompasses five feature domains:
1. **Convolved Flight Demand Features**: Lead-lag convolved seats, carrier-exclusive departing flights, and T-100 load-factor interactions.
2. **Airside Delay and Congestion Features**: Lagged mean departure delay ($t-1$), lagged delay dispersion ($\sigma_{\text{Delay}, t-1}$), tactical cancellation counts, and taxi-out queue duration.
3. **Temporal Cyclical Encodings**: Sine and cosine harmonic transformations of hour-of-day ($24\text{ hr}$) and day-of-week ($7\text{ days}$), capturing diurnal and weekly rhythms without arbitrary step discontinuities.
4. **Operational Regime Indicators**: Categorical encodings of the 84-cell interaction grid ($\mathcal{S} \times \mathcal{D} \times \mathcal{H}$).
5. **Facility Physical Features**: Screening lane count, checkpoint configuration type (finger pier vs. linear), and pre-security connector geometry.

---

### 4.3.2 Model Training Architecture
To evaluate the research hypotheses, six models across three paradigms were trained and calibrated:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODEL PARADIGM 1: DETERMINISTIC BASELINES                │
├─────────────────────────────────────────────────────────────────────────────┤
│  M0: Diurnal Seasonal Naive Benchmark                                       │
│      • Formula: ŷ_t = y_{t-24}                                              │
│      • Assumes yesterday's hourly throughput repeats exactly.               │
│  M1: Contemporaneous Scheduled Baseline (Rebuilt 2-Hour Static Shift)       │
│      • Uses published scheduled flight seats with static 2-hour lead.       │
│      • Represents status-quo deterministic airport planning tools.          │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│               MODEL PARADIGM 2: PROBABILISTIC & MACHINE LEARNING            │
├─────────────────────────────────────────────────────────────────────────────┤
│  M2: Convolved Passenger Show-Up Curve (No Delays)                          │
│      • Gradient Boosted Count Regressor (LightGBM, Tweedie p = 1.3).        │
│      • Features: Convolved lead flights (t+1, t+2, t+3), cyclical harmonics. │
│  M3: Stochastic Operational Tree (Show-Up Curve + OTP Delays/Cancels)       │
│      • Expands M2 with lagged delay indicators (t-1), cancellations, taxi.  │
│      • Tweedie objective: min Σ 2 (y^{2-p}/((1-p)(2-p)) - y ŷ^{1-p}/(1-p)   │
│        + ŷ^{2-p}/(2-p)).                                                    │
│  M4: Full Tri-Modal Pipeline (Load Factor Scaled)                           │
│      • Interacts convolved flight features with monthly T-100 load factors   │
│        and quarterly DB1B connecting ratios.                                │
└─────────────────────────────────────────────────────────────────────────────┘
                                       │
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                 MODEL PARADIGM 3: SEQUENTIAL TWO-STAGE HYBRID               │
├─────────────────────────────────────────────────────────────────────────────┤
│  M5: Sequential SARIMA-Tree Hybrid Architecture                             │
│      • Stage 1 (Linear Autoregressive Time-Series):                         │
│        SARIMA(2, 1, 2) × (1, 1, 1)_24 captures autocorrelation & seasonal  │
│        queue persistence, outputting linear forecast ŷ_{1, t}.              │
│      • Residual Extraction: e_t = y_t - ŷ_{1, t}                            │
│      • Stage 2 (Non-Linear Gradient Boosted Residual Correction):           │
│        Decision tree predicts residual ê_t using flight show-up curves,     │
│        delay features, taxi times, and operational regime indicators.       │
│      • Final Hybrid Prediction: ŷ_{M5, t} = ŷ_{1, t} + ê_t                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

#### Training Window and Partitioning Design
Models were trained and validated across the 32-month Candidate B development partition:
* **Training Window**: May 1, 2022 to December 31, 2023 (20 months; 122,847 hourly observations across the 9-airport complex cohort; 404,324 observations across the Top 25 network).
* **Validation Window**: January 1, 2024 to December 31, 2024 (12 months; 72,723 hourly observations), used for hyperparameter tuning (learning rate $\eta = 0.05$, max depth = 8, num leaves = 63, Tweedie variance power $p = 1.3$).
* **Operational Buffer**: A 7-day purge buffer between partitions ensures that multi-day delay cascades from December 2023 do not leak into the January 2024 validation partition.

---

### 4.3.3 Model Testing Protocol
All trained architectures were evaluated against the untouched **2025 Full-Year Out-of-Time Holdout Dataset**:
* **Evaluation Period**: January 1, 2025 to December 31, 2025 (12 continuous months; 8,760 calendar hours).
* **Sample Size**: 72,053 hourly observations across the 12 dedicated screening complexes of the 9-airport experimental cohort (representing 215,562 facility screening hours across the wider candidate network).
* **Evaluation Metrics**: Models were benchmarked across five standard accuracy metrics:
  1. **Coefficient of Determination ($R^2$)**: $1 - \frac{\sum (y_t - \hat{y}_t)^2}{\sum (y_t - \bar{y})^2}$, measuring the proportion of hourly demand variance explained.
  2. **Root Mean Squared Error (RMSE)**: $\sqrt{\frac{1}{N} \sum (y_t - \hat{y}_t)^2}$, heavily penalizing large forecast errors during peak departure banks.
  3. **Mean Absolute Error (MAE)**: $\frac{1}{N} \sum |y_t - \hat{y}_t|$, measuring typical hourly passenger forecasting error.
  4. **Mean Absolute Scaled Error (MASE)**: $\frac{\text{MAE}_{\text{model}}}{\text{MAE}_{\text{naive}}}$, evaluating accuracy relative to a seasonal naive baseline ($\text{MASE} < 1.0$ indicates superior performance over naive persistence).
  5. **Mean Forecast Bias**: $\frac{1}{N} \sum (\hat{y}_t - y_t)$, measuring systematic over-prediction (positive) or under-prediction (negative).

---

### 4.3.4 Implications for Interpreting Final Results
When interpreting model evaluation metrics, several operational realities must be considered:
1. **Terminal Complex Aggregation Scale**: Mean hourly throughput across dedicated screening complexes is approximately 1,750 passengers per hour, with peak hours exceeding 4,000 passengers per hour. An MAE of ~800 passengers per hour across a multi-lane complex represents an average variance of only 50–70 passengers per individual screening lane per hour, well within operational TSO queue management tolerances.
2. **MASE as the Gold Standard for Aviation Forecasting**: In high-variance time series with strong diurnal periodicity, $R^2$ can be inflated by day-night cycles. MASE normalizes errors against seasonal persistence ($y_{t-24}$). A MASE below 0.85 indicates substantial predictive value beyond historical persistence.
3. **Negative Forecast Bias During Peak Surges**: In count-based regression models, extreme holiday surges (+3 standard deviations) tend to be smoothed toward the conditional mean, producing a slight negative bias (-180 to -400 pax/hr). From a staffing perspective, operational planners must apply quantile adjustments (e.g., predicting the 85th percentile, $q = 0.85$) to buffer against queue overflow.

---

## 4.4 Model Evaluation and Results

### 4.4.1 Results from Running Models (2025 Full-Year Holdout Matrix)
Table 4.10 reports the out-of-time evaluation benchmark matrix across all six model architectures on the 2025 holdout dataset (72,053 hourly complex observations).

#### Table 4.10: Master Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)

| Paradigm | Model ID | Model Architecture | Validation $R^2$ | Test $R^2$ | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Forecast Bias (pax/hr) | Academic Target Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deterministic Baseline** | **$M_0$** | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1,377.3 | 939.8 | 1.000 | -0.7 | Baseline Reference |
| **Deterministic Baseline** | **$M_1$** | Contemporaneous Sched SARIMAX *(Old)* | 0.4338 | 0.4375 | 1,393.8 | 1,042.6 | 1.109 | -327.4 | Failed ($\text{MASE} > 1.0$) |
| **Deterministic Baseline** | **$M_1^*$**| Rebuilt 2-Hour Static Sched Baseline | 0.5312 | **0.5293** | **1,265.4** | **902.1** | **0.942** | **-184.2** | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_2$** | Convolved Lead Flights Only | 0.5443 | 0.5862 | 1,195.5 | 856.2 | 0.911 | -296.8 | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_3$** | Convolved Lead + OTP Delays/Cancels | 0.5450 | **0.5880** | **1,192.9** | **855.1** | **0.910** | **-295.3** | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_4$** | Full Tri-Modal Pipeline (Load Factor Scaled) | 0.5798 | 0.5771 | 1,208.6 | 856.3 | 0.911 | -430.8 | Passed Target ($\text{MASE} < 1.0$) |
| **Sequential Hybrid** | **$M_5$** | Sequential SARIMA-Tree Hybrid | **0.6644** | **0.6270** | **1,135.0** | **795.0** | **0.846** | **-402.9** | **CHAMPION ARCHITECTURE** |

---

### 4.4.2 General Model Performance
The empirical results reveal clear performance separations across the three modeling paradigms:

1. **Failure of Contemporaneous Deterministic Planning ($M_1$ vs. $M_1^*$)**:
   The traditional status-quo baseline using contemporaneous scheduled departures ($M_1$) completely failed out-of-time evaluation ($\text{Test } R^2 = 0.4375, \text{Test MASE} = 1.109$). Because flights depart 1.5 to 2 hours after passengers cross security, contemporaneous models misalign demand peaks, performing 10.9% worse than a naive persistence guess ($y_{t-24}$). Rebuilding the deterministic baseline with a static 2-hour pre-departure shift ($M_1^*$) elevates accuracy substantially ($\text{Test } R^2 = 0.5293, \text{Test RMSE} = 1,265.4, \text{Test MASE} = 0.942$), beating seasonal naive persistence.
2. **Gains from Machine Learning and Show-Up Kernels ($M_2, M_3, M_4$)**:
   Introducing empirical passenger show-up curves convolved across lead horizons ($t+1, t+2, t+3$) produces a major improvement. Model $M_2$ elevates explained variance to $R^2 = 0.5862$ ($\text{RMSE} = 1,195.5$), while incorporating lagged delay indicators and tactical cancellations ($M_3$) achieves $R^2 = 0.5880$ ($\text{RMSE} = 1,192.9, \text{MASE} = 0.910$). Formal Diebold-Mariano testing proves that $M_3$'s error reductions over the deterministic baseline are statistically significant ($DM = 74.25, p < 0.0001$).
3. **Superiority of the Sequential SARIMA-Tree Hybrid ($M_5$)**:
   The Sequential SARIMA-Tree Hybrid architecture emerges as the overall champion model across every accuracy metric. $M_5$ is the only architecture to surpass the academic target of $R^2 > 0.600$, explaining **62.70% of total passenger demand variance** on unobserved 2025 data ($\text{Test } R^2 = 0.6270$). It slashes RMSE to **1,135.0 pax/hr** (-130.4 pax/hr reduction vs. $M_1^*$), achieves the lowest MAE of **795.0 pax/hr**, and attains a MASE of **0.846**, surpassing the academic stretch target of $\text{MASE} < 0.850$. Diebold-Mariano tests confirm that $M_5$'s forecast superiority is mathematically decisive ($DM = 79.12, p < 0.0001$).

---

### 4.4.3 Model Performance in the Context of the Thesis Hypotheses
The primary thesis hypothesis (**Hypothesis 1**) stated that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. Table 4.11 evaluates the models across the three core operational dimensions.

#### Table 4.11: Master Multi-Pillar Hypothesis Evaluation Matrix Across the Three Dimensions

| Operational Dimension | Performance Metric | Formula / Definition | Academic Target Benchmark | Deterministic Baseline ($M_1^*$) | Probabilistic ML ($M_3$) | Dynamic Hybrid ($M_5$) | Hypothesis Confirmation Status |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** | $\text{RMSE}_{\text{routine}}$ (Delay $< 15$m; 0 Cancels) | $\sqrt{\text{mean}((y - \hat{y})^2 \mid \text{routine})}$ | $< 1,150$ pax/hr | 1,265.4 pax/hr | 1,167.9 pax/hr | **1,114.7 pax/hr** | **Confirms H1(a)**: ML and Hybrid models fit nominal daily curves tighter. |
| **Dimension 1: Robustness** | $\text{MASE}_{\text{routine}}$ (Relative Routine Error) | $\text{MAE}_{\text{routine}} / \text{MAE}_{\text{naive}}$ | $< 0.900$ | 0.942 | 0.890 | **0.834 (SUPERIOR)**| $M_5$ delivers an 11.5% accuracy gain over deterministic planning under normal conditions. |
| **Dimension 1: Robustness** | Diebold-Mariano ($DM$) Stat & $p$-value | $DM$ Loss Differential Test vs. $M_1^*$ | $p < 0.001$ | Baseline Control | $DM = 74.25$ ($p < 0.0001$) | **$DM = 79.12$ ($p < 0.0001$)** | Statistical significance proves ML and Hybrid gains are genuine and reproducible. |
| **Dimension 2: Resilience** | $\text{RMSE}_{\text{shock}}$ (Delay $\ge 45$m or Cancels $\ge 5$) | $\sqrt{\text{mean}((y - \hat{y})^2 \mid \text{shock})}$ | $< 1,100$ pax/hr | 1,228.9 pax/hr | 1,024.9 pax/hr | **1,023.2 pax/hr** | Dynamic models maintain tight error bounds during severe weather storms. |
| **Dimension 2: Resilience** | $\text{MASE}_{\text{shock}}$ (Relative Disruption Error) | $\text{MAE}_{\text{shock}} / \text{MAE}_{\text{naive}}$ | $< 0.850$ | 0.966 | 0.772 | **0.737 (SUPERIOR)**| Dynamic models perform 26% better than naive guessing during disruptions. |
| **Dimension 2: Resilience** | Resilience Multiplier ($R_{\text{MASE}}$) | $\text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$ | $< 1.30$ (Fragile $\ge 2.0$) | 1.03 (Static blind) | 0.87 (Acute surge: 2.14) | **0.88 (Maintains $\le 1.28$)** | **Confirms H1(b)**: Pure ML collapses during delayed flight holds ($R = 2.14$); Hybrid stays resilient via queue feedback. |
| **Dimension 2: Resilience** | Time-to-Recovery ($\text{TTR}_{\text{shock}}$) | Kaplan-Meier survival to $\pm 2\sigma$ error | $< 4.0$ hours | 8.4 hours | 6.7 hours | **3.2 hours (FASTEST)** | $M_5$ returns to normal error bounds 5.2 hrs faster than $M_1^*$ and 3.5 hrs faster than $M_3$. |
| **Dimension 3: Generalizability**| Zero-Shot $\text{RMSE}_{\text{transfer}}$ | Transfer from EWR to LGA (no retraining) | $< 1,350$ pax/hr | 1,321.0 pax/hr | **1,162.8 pax/hr** | 1,237.4 pax/hr | Out-of-the-box accuracy when deploying model to an unfamiliar airport facility. |
| **Dimension 3: Generalizability**| Relative Transfer Ratio (RTR) | $\text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}}$ | $\le 1.10$ | **1.04 (EXCELLENT)** | **1.08 (EXCELLENT)** | 1.19 (Moderate penalty) | **Confirms H1(c)**: Deterministic physical rules ($RTR = 1.04$) and convolved ML ($RTR = 1.08$) generalize better than decision trees. |
| **Dimension 3: Generalizability**| Transfer Penalty ($\Delta_{\text{transfer}}$) | $((\text{RMSE}_{\text{trans}} - \text{RMSE}_{\text{in}}) / \text{RMSE}_{\text{in}}) \times 100$ | $\le 10.0\%$ | **+4.4% (MINIMAL)** | **+7.9% (LOW)** | +18.7% (Elevated) | Simple physical rules lose only 4.4% accuracy; complex residual trees lose 18.7% due to local terminal overfitting. |
| **Dimension 3: Generalizability**| Change in MASE on Transfer ($\Delta\text{MASE}$) | $\text{MASE}_{\text{transfer}} - \text{MASE}_{\text{in-sample}}$ | $< +0.100$ | **+0.041** | **+0.071** | +0.158 | Rebuilt $M_1^*$ and $M_3$ beat the $+0.100$ threshold, confirming high zero-shot portability. |

#### Empirical Evaluation of Hypothesis Dimensions
1. **Dimension 1: Robustness (Confirmed)**:
   Under nominal operating conditions (delays < 15 min), the Gradient Boosted Tree ($M_3$) and Sequential Hybrid ($M_5$) achieve $\text{MASE}_{\text{routine}} = 0.890$ and $0.834$, substantially outperforming the deterministic baseline ($\text{MASE} = 0.942$). The non-linear models effectively capture cyclical harmonics, aircraft gauge tiers, and passenger show-up curves.
2. **Dimension 2: Resilience and the "Empty Checkpoint Fallacy" (Confirmed)**:
   During severe convective weather ground stops and winter freeze events (e.g., Winter Storm Elliott), pure machine learning models suffer from the **"empty checkpoint fallacy."** When flights scheduled for 18:00 are delayed to 23:00, pure ML models look at the delayed schedule and falsely predict empty screening checkpoints at 16:30. In reality, passengers have already arrived at the terminal and are queued at checkpoints. As a result, pure ML error spikes during acute disruption events ($R_{\text{MASE}} = 2.14$). In contrast, the Sequential Hybrid Model ($M_5$) dynamically incorporates prior-hour checkpoint congestion feedback ($t-1$), maintaining a disruption multiplier of $R_{\text{MASE}} = 1.28$ and returning to normal error bounds within **3.2 hours** (compared to 6.7 hours for pure ML and 8.4 hours for deterministic planning).
3. **Dimension 3: Generalizability and Cross-Airport Transferability (Confirmed)**:
   When models trained on United Airlines at Newark (EWR Terminal C) were deployed directly to Delta Air Lines at LaGuardia (LGA Terminal C) in zero-shot mode without retraining, the deterministic baseline ($M_1^*$) and convolved ML model ($M_3$) exhibited exceptional transferability ($RTR = 1.04$ and $1.08$, losing only +4.4% and +7.9% accuracy). In contrast, the decision-tree component of the Hybrid Model suffered an 18.7% accuracy degradation ($RTR = 1.19$) due to overfitting on Newark's specific terminal geometry and carrier schedule bank timings.

---

### 4.4.4 Implications of Model Performance for Predictive Forecasting in Aviation
The empirical findings carry substantial implications for operational practice and predictive analytics in commercial aviation:
1. **Dismantling the Contemporaneous Schedule Assumption**: Traditional airport terminal management systems that scale published flight departures contemporaneously are structurally flawed, lagging passenger arrival demand by 90 to 120 minutes. Implementing convolved lead-lag passenger show-up kernels is essential to generate actionable landside security forecasts.
2. **Operational Deployment via a Dual-Track Decision Engine**:
   Because no single modeling paradigm is universally optimal across all conditions, commercial airports and security agencies should deploy a **Regime-Switched Dual-Track Architecture**:
   * *Nominal Tracking Track*: During clear weather and routine schedule execution ($T(h) < \tau$), operational planning should rely on the **Probabilistic Show-Up Model ($M_3$)**, delivering high accuracy ($\text{MASE} = 0.890$) and superior spatial portability ($RTR = 1.08$) across diverse terminals.
   * *Tactical Shock Track*: When severe convective storms, ground delay programs, or gate holds occur ($T(h) \ge \tau$), the system should dynamically engage the **Sequential Two-Stage Hybrid Framework ($M_5$)**, leveraging closed-loop queue feedback to prevent the empty checkpoint fallacy and achieve rapid recovery ($\text{TTR} = 3.2\text{ hours}$).
3. **Risk-Aware Security Staffing and Conformal Prediction**:
   Mean forecasts inevitably smooth extreme passenger rushes. By pairing the Hybrid architecture with conformal quantile prediction bounds (specifically the 85th percentile, $q = 0.85$), airport security planners can generate robust staffing recommendations ($c(t) = \lceil \hat{y}_{0.85, t} / \mu \rceil$) that minimize passenger wait times during peak departure banks while maintaining efficient staffing allocations during operational valleys.
