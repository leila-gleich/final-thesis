# Chapter IV

# Results

## Initial Exploratory Data Analysis

### Descriptive Statistics
To construct an empirically rigorous, leak-free predictive modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw fact records across four primary federal feeds:
1. **TSA FOIA Checkpoint Logs**: Hourly passenger throughput records disaggregated by physical screening lane.
2. **Bureau of Transportation Statistics (BTS) On-Time Performance (OTP, Form 234)**: Flight-level departure movements tracking scheduled and actual departure times, tarmac taxi-out durations, departure delays, cancellations, and causal delay attributions.
3. **BTS Form 41 Schedule T-100 Domestic Segment Data**: Monthly carrier-route-equipment records reporting available departing seats, transported revenue passengers, and load factors.
4. **BTS DB1B / DB1C Origin-Destination Ticket Surveys**: A 10% randomized sample of airline passenger itineraries detailing coupon routes, connecting transfer ratios, and true local originating passenger fractions.

Following conformed extraction, automated entity resolution, data cleaning, and star-schema relational synthesis across conformed dimension keys (*dim_date*, *dim_time_block*, *dim_airport*, *dim_airline*, *dim_aircraft*, *dim_checkpoint*), the nationwide post-ETL analytical warehouse retains **42,062,039 conformed records** across the candidate network of the Top 25 U.S. commercial airfields. Table 4.1 documents the post-ETL data foundation census across all four federal data sources.

Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)*

## Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)

Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

## Table 4.2: Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)

At the macro network level, the 25 candidate airfields processed an annual mean of 192,160 scheduled commercial domestic departures ($\sigma = 69,376$; median = 177,182), ranging from 95,849 departures at Washington Dulles (IAD) to 360,571 departures at Chicago O'Hare (ORD). Systemwide passenger screening throughput averaged 68.50 million passengers per airfield annually ($\sigma = 27.76\text{M}$; median = 66.01M), with Charlotte Douglas (CLT) recording 28.17 million passengers and Los Angeles International (LAX) processing 129.07 million passengers across the multi-year study period.

Three essential data hygiene protocols were established during warehouse staging to guarantee econometric and machine learning validity:
1. **Spatial Key Resolution and Unidentified Airport Isolation**: Upstream raw TSA logs contained 35,809 records with missing or corrupted airport strings. An automated checkpoint fingerprinting algorithm successfully mapped 7,489 records by identifying unique physical checkpoint string signatures (*dim_checkpoint*). The remaining 22,190 unresolvable records were assigned to a dedicated null surrogate key (*airportId* = 0, flagged with *airportMissing* = 1), preventing the creation of an artificial 9.71-million passenger "phantom airport" that would have distorted econometric demand baselines. All downstream analyses strictly enforce *airportMissing* = 0 and *airportId* > 0.
2. **Scheduled Checkpoint Closures vs. Missing Sensor Data**: A critical operational feature of airport checkpoints is zero throughput during overnight curfews. Across the warehouse, 450,973 records (2.31%) reported zero passengers. Cross-referencing flight movements established that 98.6% of zero values occur between 00:00 and 03:59 local time. Rather than applying moving-average or spline imputations—which would fabricate passenger volume during scheduled overnight lane closures—these intervals were preserved as true operational structural zeros and modeled through zero-bounded count regression (a Tweedie compound Poisson distribution, $p = 1.3$, which naturally accommodates real zero counts without producing impossible negative passenger estimates or requiring artificial data smoothing).
3. **Advance vs. Tactical Cancellation Causality**: Across the 13,153,654 domestic departures, flight cancellations averaged 2.03% (267,019 operations), with 99.4% of unassigned aircraft tail numbers occurring on cancelled flights. To prevent lookahead bias in passenger forecasting (the error of using future information that an airport operations manager would not possess in real time), advance cancellations (>24 hours prior to scheduled departure) were purged from departing seat supply curves, while tactical cancellations (<2 hours prior) were retained, reflecting the operational reality that booked passengers had already completed landside security screening before the carrier issued the cancellation.

### Temporal Boundaries
A core methodological requirement of this thesis is that **defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset**. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on idiosyncratic facility characteristics rather than learning generalizable aviation temporal dynamics.

#### Post-Pandemic Regime Selection and Structural Break Analysis.
The seven-year dataset captures two unprecedented macroeconomic disruptions: the COVID-19 pandemic demand collapse (2020–2021) and the post-pandemic operational rebound (2022–2025). To identify the point at which commercial aviation resumed structural equilibrium, rolling Welch's $t$-tests, Cumulative Sum (CUSUM) structural break tests, and longitudinal correlation metrics were computed across the Top 25 airfields. Table 4.3a contrasts the candidate temporal demarcation baselines.

Table 4.3a  
*Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network*

## Table 4.3a: Post-Pandemic Temporal Demarcation Evaluation Across the Top 25 Network

Structural break tests confirmed **May 1, 2022** as the optimal demarcation point for empirical model development:
1. **Federal Transit Mask Mandate Repeal**: The nationwide vacatur of federal transit mask requirements on April 18, 2022 restored unconstrained business and leisure travel behavior. By May 1, 2022, load factors recovered to 84.7%, matching pre-pandemic baselines.
2. **Coupling Stability**: During the acute pandemic (2020–2021), the correlation between scheduled flights and checkpoint throughput spiked to an artificial $r = 0.607$ ($R^2 = 36.85\%$) because airline capacity cuts mirrored strict travel bans. In the post-May 2022 equilibrium, the relationship stabilized to $r = 0.553$ ($R^2 = 30.61\%$), reflecting normalized booking curves.
3. **Partitioning Design**: Candidate B establishes a 32-month development span partitioned into a 20-month training set (May 1, 2022 to December 31, 2023; 122,847 hourly observations across the filtered 9-airport complex cohort; 404,324 multi-facility observations across the Top 25 network), a 12-month validation set (January 1, 2024 to December 31, 2024; 72,723 hourly observations), and an untouched 12-month out-of-time holdout test set (January 1, 2025 to December 31, 2025; 72,053 complex-level observations; 215,562 facility-level observations). A 7-day operational buffer between partitions prevents multi-day delay cascades from leaking across evaluation boundaries.

### Defining Seasonality
Just as temporal boundaries must be established on the complete Top 25 network, **defining seasonality requires capturing the full variance of nationwide commercial aviation**. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and diurnal non-consecutive dual turbulence peaks.

#### Annual Seasonal Regimes and Coupled Volatility.
Airport operational stress is not uniform across the calendar year. By analyzing daily within-day passenger arrival coefficient of variation ($CV_{\text{TSA}}$) alongside flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 post-demarcation days across the Top 25 network, four distinct annual volatility regimes were established (Table 4.3b). The Coupled Volatility Index is defined as:
$$\text{CVI} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$$

Table 4.3b  
*Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)*

## Table 4.3b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

Across the annual calendar, delay dispersion ($\sigma_{\text{Delay}}$) expands monotonically from 46.09 minutes during the winter lull to 68.43 minutes during the summer peak (+48.5% dispersion expansion), driving the Coupled Volatility Index from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

#### Day-of-Week Cyclical Dynamics and Archetypes.
Weekly commercial aviation movements follow structural cycles dictated by corporate versus leisure travel demand. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) across all Top 25 airfields yields three primary weekly operational archetypes (Table 4.4a):
1. **Midweek Operational Reset (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($19.44\%$ and $20.05\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Corporate Surge (Monday & Thursday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).

Table 4.4a  
*Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)*

## Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes (Top 25 Airfields)

#### Diurnal Non-Consecutive Dual Turbulence Peaks.
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

## Table 4.5: Master Cross-Dataset Econometric Relationships (Top 25 Airfields)

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

## Data Filtering and Subset Selection

### Four-Phase Filtering Pipeline
To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, commercial airfields were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling.

The four sequential filtering stages of this pipeline progress as follows:
1. **Phase 1: Macro Filter (Scale and Congestion)**: Filters the national candidate universe of 450+ commercial airfields down to the Top 25 airfields. Enforces queue intensity $\rho(t) \to 1.0$ during departure banks, captures 67.2% of nationwide domestic flight movements, and yields a baseline correlation of $r = 0.4572$ ($R^2 = 20.90\%$) between raw flights and TSA throughput.
2. **Phase 2: Meso Filter (Symmetry and Invariance)**: Narrows the Top 25 airfields to 14 candidate hubs requiring concurrent American Airlines, Delta Air Lines, and United Airlines mainline presence (>10% seat share) while excluding Southwest bimodal arrival mixtures and ultra-low-cost carrier noise. Scheduled flight coupling strengthens to $r = 0.5015$ ($R^2 = 25.15\%$).
3. **Phase 3: Micro Filter (Checkpoint Exclusivity)**: Filters the 14 candidate airfields to nine selected hubs with strict dedicated terminal checkpoints ($P(\text{Carrier} = j^* \mid \text{Checkpoint}) = 1$), eliminating shared-terminal carrier collinearity ($\kappa < 25$). Checkpoint coupling rises to $r = 0.5453$ ($R^2 = 29.74\%$) for raw movements and $r = 0.6466$ ($R^2 = 41.81\%$) when adjusted for DB1B local originating passengers.
4. **Phase 4: Factorial Cohort (Factorial Matrix Balance)**: Finalizes the balanced nine-airport cohort comprising 12 dedicated screening complexes (exactly four dedicated complexes each for American, Delta, and United) across all four operational cluster archetypes, achieving dedicated checkpoint-to-flight coupling of $R^2 = 70.80\%$ to $77.40\%$.

#### Phase 1: Macro Filter (Heavy-Traffic Scale and Checkpoint Congestion).
* **Filtering Criteria**: Restrict the national candidate universe of 450+ commercial airports to the Top 25 commercial airfields ranked by domestic passenger enplanements, capturing 67.2% of nationwide domestic flight movements.
* **Methodological Justification**: In airport queueing dynamics, traffic intensity $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$ determines queue behavior. At small regional airports, passenger flow is sparse ($\rho(t) \ll 0.3$), preventing queue accumulation and causing throughput to mirror unconstrained arrivals without boundary friction. In contrast, Top 25 hub airports reach peak-hour saturation ($\rho(t) \to 1.0$) during morning (06:00–08:30) and evening (16:00–18:30) departure banks, generating the empirical queue delays and non-linear dynamics required to train and evaluate congestion-aware models.
* **TSA-OTP Relationship Evolution**: Across the nationwide universe of all commercial airfields, the linear correlation between scheduled flight departures and TSA throughput is low ($r \approx 0.35, R^2 \approx 12.25\%$). At the Top 25 macro scale, this relationship strengthens to $r = 0.4572$ ($R^2 = 20.90\%$) for raw volume, and $r = 0.6704$ ($R^2 = 44.94\%$) when deflated by DB1B connecting ratios.

#### Phase 2: Meso Filter (Operational Homogeneity and Southwest Exclusion).
* **Filtering Criteria**: Require concurrent domestic mainline operations by American Airlines, Delta Air Lines, and United Airlines ($>10\%$ market share each), while systematically excluding Southwest Airlines (WN) and Ultra-Low-Cost Carriers (ULCCs). This reduced the pool from 25 to 14 candidate hub airfields.
* **Methodological Justification**: Concurrent legacy carrier operations ensure that cross-carrier comparisons evaluate under identical exogenous airspace conditions ($\delta_t$), canceling common weather ground delay programs and FAA flow management initiatives. Furthermore, Southwest Airlines was excluded due to its passenger arrival behavior: legacy carrier passengers display consistent, unimodal lognormal arrival timing ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \approx 105\text{ min}$), whereas Southwest's historical open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture ($\mu_1 \approx 135\text{ min}$ for boarding group maximizers; $\mu_2 \approx 65\text{ min}$ for carry-on business travelers), violating arrival distribution homogeneity.
* **TSA-OTP Relationship Evolution**: In the 14-airfield Meso cohort, eliminating Southwest and ULCC scheduling volatility elevated the scheduled flight to TSA throughput correlation to $r = 0.5015$ ($R^2 = 25.15\%$).

#### Phase 3: Micro Filter (Carrier Checkpoint Exclusivity).
* **Filtering Criteria**: Require strict single-carrier dedicated screening checkpoint complexes ($P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$). Airfields with shared multi-carrier central screening checkpoints were excluded. This filtered the 14 candidate hubs down to 9 selected airfields.
* **Methodological Justification**: In shared terminal facilities (e.g., Salt Lake City or Phoenix), multiple airlines funnel passengers into shared security queues. Because hub carriers coordinate flight banks, carrier departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$, condition number $\kappa > 10^4$), preventing mathematical separation of individual carrier demand. Restricting analysis to dedicated checkpoint complexes collapses collinearity ($\kappa < 25$), directly mapping carrier flight banks to landside checkpoint queues.
* **TSA-OTP Relationship Evolution**: At the airport-wide level for the 9 selected airfields, scheduled flights versus total TSA passengers achieve $r = 0.5453$ ($R^2 = 29.74\%$), while scheduled flights versus true local originating TSA demand (DB1B adjusted) reaches $r = 0.6466$ ($R^2 = 41.81\%$). Furthermore, when evaluated at the dedicated checkpoint complex level, carrier-filtered departing seats explain **70.80% to 77.40%** ($R^2$) of checkpoint throughput variance.

#### Phase 4: Factorial Cohort (Factorial Matrix Balance).
* **Filtering Criteria**: Construct a balanced factorial matrix across legacy carriers and operational archetypes, retaining the **9-Airport Experimental Cohort** comprising **12 Dedicated Checkpoint Complexes** across **BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL**.
* **Methodological Justification**: Complete factorial symmetry requires exactly 4 dedicated terminal screening complexes per legacy carrier (American: 4, Delta: 4, United: 4) spanning all four operational clusters, ensuring unconfounded cross-carrier and cross-airport transfer evaluation.
* **Crucial Methodological Distinction**: These evolving correlations and seasonal dynamics serve exclusively to justify the four-tier filtering rationale and confirm data validity. **These relationships and dynamics are not used in training the downstream predictive models**, preserving strict econometric separation and preventing data leakage. Furthermore, the analysis at this stage evaluates the **9 selected airports as complete facilities**, rather than premature facility checkpoints.

### Pipeline Results
The filtering pipeline isolated 9 commercial airfields representing 12 carrier-exclusive screening environments, achieving complete factorial balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

Table 4.6  
*The Nine-Airport Experimental Cohort Factorial Specification*

## Table 4.6: The Nine-Airport Experimental Cohort Factorial Specification

#### Key Airport Selection Contrasts.
* **LGA vs. JFK Selection**: United Airlines permanently ceased operations at JFK in October 2022 (failing Meso multi-carrier continuity). In contrast, LGA opened Delta's state-of-the-art consolidated Terminal C in June 2022, providing unconfounded screening lanes with 100% carrier exclusivity.
* **PHL vs. SLC Selection**: Salt Lake City International (SLC) channels all airlines through a single consolidated central screening checkpoint, making carrier isolation structurally impossible. Philadelphia International (PHL) provides dedicated American Airlines checkpoints in Terminals B and C, ensuring carrier isolation within Cluster 2.

#### Econometric Validation of Carrier Checkpoint Isolation.
To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed:
1. **Volume Conservation Test**: Total daily checkpoint throughput tracks carrier ticketed boardings with slope $\rho = 1.00 \pm 0.04$ ($R^2 > 0.95$).
2. **Zero-Flight Intercept Test**: Checkpoint demand when zero carrier flights are scheduled is statistically indistinguishable from zero ($\beta_0 = 12.4$ pax/hr, $p = 0.40$).
3. **Cross-Carrier Orthogonality Test**: Regressing dedicated checkpoint throughput against concurrent departures by other airlines operating in adjacent terminals yields non-significant coefficients ($\beta_{\text{other}} = 0.002, p = 0.62$).
4. **Terminal Layout Invariance Test**: A two-sample Kolmogorov-Smirnov test comparing physically separate terminals (e.g., LGA, DTW) against walkway-connected terminals (e.g., DFW, LAX) yielded $D = 0.032$ ($p = 0.28$), confirming that airside walkway connections do not induce statistically significant cross-terminal throughput leakage.

### Descriptive Statistics for Subset

Table 4.7 presents the descriptive summary statistics for the nine-airport experimental cohort compared against the Top 25 candidate universe.

Table 4.7  
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe*

## Table 4.7: Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25 Universe

Compared to the broader Top 25 network, the 9-airport cohort exhibits:
* **Higher Flight Movement Density**: Scheduled flights are +16.9% higher (224,576 vs. 192,160), ensuring screening checkpoints operate under heavy, bank-synchronized arrival loads.
* **Higher Delay and Cancellation Exposure**: Average departure delay is +7.2% higher (15.23 min vs. 14.21 min), cancellation rate is +14.1% higher (1.63% vs. 1.43%), and taxi-out time is +4.5% higher (20.59 min vs. 19.69 min), reflecting genuine operational congestion.
* **Higher Local Originating Demand**: Local originating passenger share is +8.1% higher (52.55% vs. 48.61%), and true local originating volume is +25.0% higher (16.38M vs. 13.10M), concentrating demand directly into landside security checkpoint queues.

#### Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports.

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airfields display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 reports the day-of-week passenger throughput distribution across the nine airports.

Table 4.8  
*Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports*

## Table 4.8: Day-of-Week Mean Daily Passenger Throughput Across the Nine Selected Airports

The 9 airports exhibit three distinct weekly demand dynamics:
1. **The Pure Corporate Profile (LGA)**: LaGuardia exhibits an extreme day-of-week ratio of **2.30**. Throughput peaks on Monday (49,002 pax) and Sunday (48,000 pax) driven by corporate business travel in the Northeast corridor, while Friday drops to 21,310 pax due to business travelers returning home early and leisure travelers avoiding slot-constrained short-haul airfields.
2. **The Corporate-to-Weekend Profile (BOS, EWR, PHL, DTW, DFW)**: These facilities peak on Friday (52,244 at BOS; 73,625 at DFW; 69,206 at EWR) as business travelers depart for weekend destinations and leisure getaways overlap, with Tuesday serving as the weekly volume trough (Peak/Trough ratio = 1.14 to 1.23).
3. **The Energy Sector & Midweek Profile (IAH, ORD)**: Houston Bush and Chicago O'Hare experience Thursday peaks (53,351 at IAH; 50,706 at ORD) driven by consulting, engineering, and corporate travel schedules, followed by steep Saturday troughs.

### Implications for Model
The empirical findings from subset selection dictate essential modeling choices:
1. **Separation of Dedicated Checkpoint Complexes from Airport Aggregates**: Modeling passenger security throughput at the entire airport level confounds multi-carrier flight banks and masks terminal-specific surges. Models must be trained and evaluated at the **dedicated screening complex grain** ($Y_{kt}$), mapping carrier-exclusive flight banks to dedicated screening lanes.
2. **Deflating Capacity by Connecting Ratios**: Because connecting passengers bypass security queues, departing flight seats must be deflated by $(1 - \text{ConnectingRatio}_{\text{airport}})$ from DB1B surveys. Failure to apply this deflator causes models to overpredict checkpoint volume by over 200% at connecting hubs (DFW, DTW, ORD).
3. **Handling Asymmetric Delay Information**: Same-hour flight delay information cannot be used in real-time forecasting without creating lookahead bias, because actual departure delays are not known until after flights push back. Instead, prior-hour delays ($t-1$) and tactical cancellations provide actionable indicators of terminal congestion while preserving strict information availability.
4. **Zero-Bounded Distributional Assumptions**: Checkpoint throughput data exhibits positive skewness and structural zeros during overnight curfews. Standard ordinary least squares (OLS) regression produces negative predictions during night hours. Models must incorporate zero-bounded formulations, such as Tweedie compound Poisson generalized linear models ($p = 1.3$) or two-stage hurdle structures.

## Model Development and Execution

### Feature Engineering
A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)*

## Table 4.9: Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)

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
### The Candidate Predictive Models and Baseline Control

Following the four-tiered purposive filtering pipeline (which established the balanced 9-airport experimental cohort across 12 carrier-exclusive terminal screening complexes), the research benchmarks **three candidate predictive models representing distinct operational paradigms**, evaluated against an empirical persistence control:

* **Baseline Control Benchmark (Daily Persistence)**:
  * *Operational Approach*: Assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion exactly ($\widehat{\text{Vol}}_t = \text{Vol}_{t-24}$). This non-parametric reference standard establishes the scaling baseline ($\text{MASE} \equiv 1.000$).
* **Model 1: Deterministic Flight Schedule Model (Operational Baseline)**:
  * *Operational Approach*: Derives expected passenger arrival dispersion directly from published airline flight departure banks convolved across empirical ACRP Report 40 passenger show-up curves ($t+1, t+2, t+3$). It captures macro schedule geometry without requiring statistical machine learning or airside delay telemetry.
* **Model 2: Supervised Machine Learning Model (Flight Operations & Delays)**:
  * *Operational Approach*: An automated decision-tree model trained across the convolved flight schedule and 24 Bureau of Transportation Statistics (BTS) On-Time Performance (OTP) operational features (incorporating tactical flight cancellations, prior-hour delay dispersion, and surface taxi queues).
* **Model 3: Dynamic Two-Stage Hybrid Model (Schedule + Real-Time Feedback)**:
  * *Operational Approach*: Combines daily and weekly flight schedule cycles with live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from actual checkpoint screening counts. When unexpected flight delays hold passengers landside, the dynamic error correction senses the accumulation and immediately adjusts the forecast upward.

#### Training Window and Partitioning Design.
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

## Model Evaluation and Results

### Results from Running Models
Table 4.10 reports the out-of-time evaluation benchmark matrix across the candidate model architectures on the 2025 holdout dataset (3,222 test airport-days; 72,053 hourly complex observations).

Table 4.10  
*Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)*

## Table 4.10: Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Out-of-Time Holdout)

### General Model Performance Across the 9-Airport Cohort
The empirical results reveal clear performance separations across the modeling paradigms:
1. **The Deterministic Schedule Baseline (Model 1)**:
   By shifting scheduled flight departures across empirical ACRP Report 40 passenger arrival curves, Model 1 achieves $\text{Test } R^2 = 0.4980$ ($\text{RMSE} = 313.4\text{ pax/hr}, \text{MASE} = 0.945$). It outperforms simple persistence by 5.5% without requiring real-time flight tracking or machine learning infrastructure.
2. **Supervised Feature Coupling (Model 2)**:
   Incorporating 24 BTS OTP feature attributes (departure delay dispersion, tactical cancellations, and taxi queues) elevates explained variance to **$R^2 = 0.6178$** ($\text{RMSE} = 273.5\text{ pax/hr}, \text{MASE} = 0.779$). Statistical loss differential tests confirm that Model 2's error reductions over deterministic scheduling are statistically decisive ($DM = 42.15, p < 0.0001$).
3. **The Dynamic Two-Stage Hybrid (Model 3)**:
   By coupling a daily flight schedule foundation with live real-time error feedback, Model 3 explains **74.83% of total passenger throughput volatility variance** on unobserved holdout data ($\text{Test } R^2 = 0.7483$), achieving an RMSE of **222.1 pax/hr** and a holdout MASE of **0.662**.

### Model Performance in the Context of the Thesis (Asymmetric Hypothesis Testing)
The primary thesis hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. 

Critically, **the hybrid model (Model 3) is NOT the winner across all performance measures**. To determine model efficacy, the candidate architectures were evaluated against explicit performance targets across the three operational dimensions:
* **Robustness Target**: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.70$ under nominal flight conditions.
* **Resilience Target**: Recovery RMSE Multiplier $R_{\text{RMSE}} \approx 1.00$ and lowest $\text{MASE}_{\text{shock}}$ under acute disruptions.
* **Generalizability Target**: Relative Transfer Ratio $\text{RTR} = 1.00$ and Change in MASE on transfer $\Delta \text{MASE} \le 10.0\%$.

Table 4.11 presents the formal multi-pillar hypothesis evaluation matrix.

Table 4.11  
*Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)*

## Table 4.11: Master Multi-Pillar Hypothesis Evaluation Matrix Across the Four Models (Throughput Volatility)

#### Empirical Confirmation of Asymmetric Trade-Offs (Hypothesis 1 Verified).
1. **Dimension 1: Robustness (Nominal & Routine Conditions)**:
   Both the Supervised Machine Learning model (Model 2) and Dynamic Hybrid (Model 3) achieve the academic target of $\text{MASE} < 0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and zero feedback latency, making it the preferred operational choice for everyday routine staffing.
2. **Dimension 2: Resilience (Severe Disruption / IROPS)**:
   The Dynamic Hybrid Framework (Model 3) is the **decisive champion of Resilience**. While pure machine learning (Model 2) suffers from the "Empty Checkpoint Fallacy" during delayed flight holds ($R_{\text{MASE}} = 2.14$), Model 3's recursive error feedback ($e_{t-1}$) maintains a resilient multiplier of $R_{\text{MASE}} = 1.05 \approx 1.00$ and achieves the fastest Time-to-Recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dimension 3: Generalizability (Zero-Shot Portability)**:
   The Deterministic Flight Schedule Model (Model 1) is the **decisive champion of Generalizability**. It successfully meets both stated targets: $\text{RTR} = 1.04 \approx 1.00$ and $\Delta\text{MASE} = +4.0\% \le 10.0\%$. Conversely, **the Hybrid model (Model 3) decisively fails the Generalizability targets** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$) because its decision-tree component overfits to Newark's specific terminal geometry and carrier bank timings. This empirical failure disproves universal hybrid dominance and decisively confirms Hypothesis 1.

## The Values versus Volatility Paradigm Empirical Results

The central empirical comparison of this thesis evaluates whether predicting TSA throughput volatility requires tracking the **values (levels) of OTP attributes**, the **volatility of OTP attributes**, or a **combined dual model**. Evaluating across the 2025 out-of-time holdout ($N = 3,222$ test days) across the three volatility targets reveals:

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
   * **Feature Volatility Succeeds**: In sharp contrast, Feature Volatility metrics achieve **$R^2 = +0.2313$ (linear) and $R^2 = +0.3105$ (decision trees)**, improving to **$R^2 = +0.3166$** in the Combined Model, with RMSE dropping from 4,090.7 to 3,002.3 pax/day. This confirms Hypothesis $H_2$.

### Master Factor Weighting Hierarchy of OTP Attributes
Synthesizing variable importance across models establishes the consensus predictive weights of all 24 OTP attributes:
* **Schedule Scale & Density (64.47% Consensus Share)**: Governed by `sched_rolling_7d_mean` (23.73%), `actual_daily_total` (11.64%), and `sched_hourly_mean` (6.91%).
* **Tactical Cancellations (16.48% Share)**: Driven by cancellation rate volatility (`otp_cancellation_volatility_cv`: 8.79%).
* **Network Buffers & Capacity (7.85% Share)**: Aircraft seating capacity (`aircraft_gauge_seats`: 4.26%) smooths day-to-day volatility.
* **Flight Delays & Punctuality (7.00% Share)**: **Flight Departure Delay Volatility ($\text{CV}_{\text{delay}}$)** contributes 4.32% weight, acting as a potent transmission vector into checkpoint surges ($r = +0.4373, p = 0.0288$).
* **Surface Taxi Queues (4.21% Share)**: Runway taxi-out queues (`avg_taxi_out_minutes`: 4.21%) indicate departure bank congestion.

### Implications of Model Performance for Predictive Forecasting in Aviation
1. **Deploying Dual-Paradigm Volatility Models for Staffing**: Rather than allocating security lanes based on static flight departure counts, TSA planners must incorporate **feature volatility metrics** (rolling 7-day schedule variance and cancellation volatility) to forecast queue dispersion.
2. **Operational Deployment via a Dual-Track Decision Engine**:
   * *Nominal Tracking Track*: During clear weather ($T(h) < 0.75$), operational planning should rely on the **Supervised Machine Learning Model (Model 2)**, delivering high accuracy ($\text{MASE} = 0.779$) and superior spatial portability ($RTR = 1.08$).
   * *Tactical Shock Track*: When severe storms or ground stops occur ($T(h) \ge 0.75$), the system should engage the **Dynamic Two-Stage Hybrid (Model 3)**, utilizing live error feedback to achieve rapid recovery ($\text{TTR} = 2.8\text{ hours}$).
3. **Dynamic Lane Buffers via Conformal Prediction**: By pairing predicted volatility with conformal quantile bounds ($\hat{y}_{0.85}$), security directors can establish dynamic lane buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$) that absorb queue surges without chronic overstaffing.
