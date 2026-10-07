# Chapter IV

## Findings and Discussion

This chapter presents the empirical findings and comparative performance evaluations for modeling the stochastic volatility of airport passenger screening throughput ($\sigma _{TSA}$ and $CV_{TSA}$). The study evaluates three candidate operational models – Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model) – against an empirical Baseline Control across a 2025 holdout dataset. The empirical results reveal that no single forecasting architecture is universally superior across all operational regimes. Instead, models exhibit distinct asymmetric trade-offs.

To systematically present and discuss these results (see Figure 4.1), this chapter is organized into four sections: Section 4.1 presents the initial exploratory data analysis across the multi-source data warehouse; Section 4.2 details the four-tier filtering pipeline that establishes the nine-airport, twelve-complex experimental cohort; Section 4.3 outlines feature engineering, training configurations, and 2025 holdout execution protocols; and Section 4.4 discusses the comparative model evaluations across robustness, resilience, and generalizability.

Figure 4.1

## Initial Exploratory Data Analysis

### Descriptive Statistics

To construct an empirically rigorous predictive modeling architecture that eliminates temporal and feature lookahead leakage for airport passenger security screening demand, this study synthesized multi-source operational records covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository captured 67.22 million raw operational transaction records across TSA checkpoint logs, Bureau of Transportation Statistics (BTS) On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys (Appendix for details).

Following conformed extraction, automated entity resolution, data cleaning, and relational synthesis across standardized operational dimensions (calendar date, departure time block, airport, operating carrier, fleet aircraft type, and dedicated screening complex), the nationwide post-ETL analytical warehouse retains 42,062,039 conformed records across the candidate network of the Top 25 U.S. commercial airports. Table 4.1 documents the post-ETL data foundation census across all four federal data sources. Table 4.2 presents the master post-ETL descriptive summary statistics for all primary operational variables across the nationwide Top 25 data repository.

Table 4.1  
*Master Post-ETL Multi-Source Data Foundation Census*

Table 4.2  
*Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Data Warehouse)*

See Appendix for a discussion of descriptive statistics for post ETL Data

### Temporal Boundaries

A core methodological requirement of this thesis is that defining temporal boundaries (specifically post-COVID recovery regimes) must be performed on the broad Top 25 airport dataset. Establishing macroeconomic baselines on a wide multi-airport dataset prevents overfitting: if temporal regimes were fitted exclusively to a narrow subset, downstream machine learning models would overtrain on individual facility characteristics rather than learning generalizable aviation temporal dynamics.

**Post-Pandemic Regime Selection and Structural Break Analysis. **Structural break analysis – combining rolling Welch’s $t$-tests and Cumulative Sum (CUSUM) trajectory tracking across the Top 25 airports – confirmed May 1, 2022, as the structural equilibrium demarcation point for predictive model development. This demarcation is grounded in three empirical realities: the nationwide rescission of federal transit mask requirements on April 18, 2022, which restored unconstrained traveler behavior and returned domestic passenger load factors to 84.7%; the stabilization of commercial coupling between scheduled flights and screening demand from an artificial pandemic high ($r=0.607,R^{2}=36.85%$) down to normalized post-recovery equilibrium ($r=0.553,R^{2}=30.61%$); and the establishment of a clean 32-month development baseline. This development window was partitioned into a 20-month training window (May 1, 2022 – December 31, 2023), a 12-month validation window (January 1, 2024 – December 31, 2024), and an untouched 12-month out-of-time holdout test set (January 1, 2025 – December 31, 2025), separated by a 7-day operational purge buffer to prevent multi-day delay cascades from leaking across partition boundaries.

### Defining Seasonality

Just as temporal boundaries must be established on the complete Top 25 network, defining seasonality requires capturing the full variance of nationwide commercial aviation. Aviation seasonality operates along three coupled dimensions: annual seasonal volatility regimes, day-of-week demand archetypes, and non-consecutive turbulence peaks. See appendix for Seasonality Dimensions detail. It is important to define these for models to take into account so like for like is being compared.

***TSA and OTP Throughput Data***

Evaluating the statistical relationships between TSA checkpoint throughput and Bureau of Transportation Statistics On-Time Performance data across all Top 25 airports reveals fundamental econometric dynamics. Refer to the appendix which synthesizes the master cross-dataset econometric correlations. This analysis provided distinct empirical insights:

**The Hub Disconnect**. Raw scheduled flight departures explain only 20.90% ($R^{2}$) of TSA security checkpoint passenger throughput across the Top 25 network ($r=0.4572,p<0.05$). However, when departing seats are deflated using BTS DB1B connecting ratios to isolate true local originating passengers, explained variance jumps to 44.94% ($r=0.6704,p<0.001$), an increase of +115%. For instance, major connecting hubs such as Charlotte (CLT) and Atlanta (ATL), up to 70% to 76% of passengers transfer between gates airside without entering landside security queues. Failing to account for connecting ratios creates a 2.5-fold distortion in checkpoint demand modeling.

**Coupled Volatility and Asynchronous Lag Dynamics**. While raw delay rates show weak same-hour linear correlation with passenger volumes ($r=0.2019,R^{2}=4.08%$), volatility measures exhibit strong coupling. Hourly checkpoint arrival volatility ($CV_{TSA}$) is significantly coupled with flight departure delay volatility ($r=0.4375,R^{2}=19.14%,p<0.05$). Furthermore, weekly cyclical aggregation demonstrates that passenger demand volume tracks tightly with weekly flight departure delay variance ($r=0.9022,R^{2}=81.40%,p<0.01$), reflecting synchronized macro peak seasonal demand across the network rather than landside queues causing airside pushback delays.

## *Implications for Subset*

Establishing temporal boundaries (the May 1, 2022 post-mask demarcation) and seasonal dynamics across the full Top 25 network ensures that baseline operational patterns reflect macroeconomic aviation behavior rather than idiosyncratic facility quirks. To maintain strict methodological integrity and prevent predictive errors, these macro-level seasonal regimes and cross-dataset relationships are not used as direct regression features. Instead, they serve strictly to justify the operational filtering pipeline, inform feature architectures (such as cyclical encodings and lead-lag show-up windows), and establish an uncompromised foundation for downstream modeling.

The exploratory analysis also reveals that commercial airports must initially be evaluated as whole facilities to verify operational scale and hub cluster diversity but cannot be modeled at the aggregate airport level. In shared-terminal facilities, coordinated airline flight banks generate severe multi-carrier collinearity (see appendix for equation) making it mathematically impossible to separate individual airline passenger contributions and restricting explained checkpoint variance to only ~20%. Isolating dedicated, single-carrier screening complexes is therefore essential to eliminate shared-terminal confounding and reveal the true empirical relationship between airline departure banks and landside security queue arrivals.

## Data Filtering and Subset Selection

### Four-Phase Filtering Pipeline

To eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding differences, airports were screened through a four-phase purposive filtering pipeline. For each phase, the relationship between TSA throughput and OTP flight data was tracked, demonstrating how progressive filtering refines operational coupling.

The four-phase purposive filtering pipeline systematically isolates single-carrier screening dynamics from confounding network interactions. In Phase 1 (Macro Filter), the national candidate pool of 450+ commercial airports was filtered down to the Top 25 airports, enforcing heavy queuing intensity ($\rho _{t}\to 1.0$) during departure banks, capturing 67.2% of nationwide domestic departures, and establishing a baseline correlation of $r=0.4572$($R^{2}=20.90%$) between raw flights and screening throughput. Phase 2 (Meso Filter) restricted these facilities to 14 candidate hubs exhibiting concurrent mainline operations ($>10%$ seat share) across American, Delta, and United, excluding low-cost carrier scheduling fluctuations and raising coupling to $r=0.5015$($R^{2}=25.15%$). Phase 3 (Micro Filter) screened for strict carrier checkpoint exclusivity ($P\left(Carrier=j^{*}\mid Checkpoint=1\right)=1$), eliminating shared-terminal multi-carrier collinearity ($\kappa <25$) and elevating coupling to $r=0.5453$($R^{2}=29.74%$) for raw flights and $r=0.6466$($R^{2}=41.81%$) when adjusting for local connecting ratios. Finally, Phase 4 (Balanced Experimental Cohort) established a factorial design across 12 dedicated screening complexes (exactly four complexes each for American, Delta, and United) spanning all four operational cluster archetypes, achieving final dedicated checkpoint-to-flight coupling of $R^{2}=70.80%$to $77.40%$. For an in depth outline of the phases, please refer to the appendix

### Pipeline Results

The filtering pipeline isolated 9 commercial airports representing 12 carrier-exclusive screening environments, achieving complete balance across legacy airlines and operational clusters. Table 4.6 details the experimental cohort.

Table 4.6  
*The Nine-Airport Experimental Cohort Specification*

To mathematically verify that dedicated checkpoints isolate single-carrier demand, four econometric tests were performed: Carrier Ticket Boarding Dominance, No-Mainline Zero Activity, Cross-Carrier Leakage, and Airside Concourse Isolation (detailed in the Appendix).

### Descriptive Statistics for Subset

Table 4.7 presents the descriptive summary statistics for the nine-airport experimental cohort compared against the Top 25 candidates.

Table 4.7  
*Summary Descriptive Statistics: Nine-Airport Experimental Cohort Versus Top 25*

Compared to the broader Top 25 network, the 9-airport cohort exhibits higher flight movement density, higher delay and cancellation exposure, and high local originating demand. For details on comparing the top 25 network to the 9 airport cohort, please refer to the appendix.

***Local Seasonal and Day-of-Week Differences Across the Nine Selected Airports***

While seasonal and day-of-week baselines were established across the Top 25 network, the nine selected airports display distinct local seasonal and weekly profiles reflecting their traffic composition and cluster archetype. Table 4.8 in the appendix reports the day-of-week passenger throughput distribution across the nine airports. The 9 airports exhibit three distinct weekly demand dynamics, which can be found in the Appendix.

### Implications for Model Development

The empirical findings from subset selection establish four mandatory architectural requirements for airport passenger flow modeling. First, passenger throughput must be modeled at dedicated single-carrier screening complexes rather than airport-wide aggregates to eliminate multi-carrier bank confounding and capture terminal-specific arrival surges. Second, departing seat capacity must be deflated by empirical DB1B connecting ratios ($1-ConnectingRatio_{airport}$), preventing the $>200%$ throughput overprediction that occurs when airside connecting passengers at hubs such as DFW, DTW, and ORD are erroneously assumed to enter landside checkpoints. Third, models must enforce strict information availability by using prior-hour operational indicators ($t-1$) and tactical cancellations rather than concurrent departure delays, avoiding lookahead bias since flight delays are unconfirmed until pushback occurs. Finally, predictive formulations must incorporate zero-bounded statistical structures – such as Tweedie compound Poisson generalized linear models ($p=1.3$) or two-stage hurdle structures – to accommodate positive throughput skewness and structural zeros during overnight curfew hours without generating impossible negative volume prediction.

## Model Development and Execution

### Feature Engineering

A foundational premise of airport passenger flow modeling is that passengers arrive at screening checkpoints well in advance of flight departure times. Testing lead-lag transfer dynamics between scheduled flight departure times and checkpoint throughput reveals severe temporal asynchrony (Table 4.9).

Table 4.9  
*Empirical Lead-Lag Transfer Dynamics (Scheduled Flights Versus Checkpoint Demand)*

Unshifted scheduled flights in the same departure hour explain less than 12% of checkpoint throughput variance. Explanatory power peaks across the Lead $t+1$ and Lead $t+2$ horizons ($R^{2}\approx 24%$), corresponding directly to the 90–120 minute modal passenger show-up window established in airport terminal planning guidelines (Airport Cooperative Research Program [ACRP] Report 40; Transportation Research Board, 2010). After scaling by booked load factors and deflating airside connecting passengers who never enter landside security, this transformation converts published flight timetables into an accurate baseline forecast of checkpoint queuing demand. See appendix for the complete feature engineering pipeline.

### Model Training

To test the thesis hypothesis, three candidate predictive models representing distinct operational paradigms were evaluated against an empirical persistence control. The Baseline Control assumes today's hourly checkpoint arrival volatility repeats yesterday's observed dispersion. Model 1 (Deterministic Flight Schedule Model) projects passenger arrival dispersion by convolving scheduled airline flight departure banks across empirical ACRP Report 40 show-up curves ($t+1,t+2,t+3$), capturing schedule geometry without requiring machine learning or live delay telemetry. Model 2 (Supervised Machine Learning Model) uses an automated decision-tree architecture trained across convolved schedule features and 24 Bureau of Transportation Statistics (BTS) On-Time Performance operational attributes (cancellations, prior-hour delays, and taxi queues). Model 3 (Dynamic Two-Stage Hybrid Model) couples scheduled flight cycles with live prior-hour recursive error correction ($e_{t-1}=y_{t-1}-\hat{y}_{t-1}$) from actual screening counts to sense passenger accumulation during flight delays. Using the partitions and 7-day purge buffer established in Section 4.1, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation.

***Model Testing***

All candidate architectures were evaluated against the untouched 2025 Full-Year Out-of-Time Holdout Dataset. Forecast performance was evaluated against the primary thesis target of diurnal throughput volatility ($\sigma _{TSA, hr}$, measured as pax/hr standard deviation across the 24 hours of each day) alongside scale-free relative volatility ($CV_{TSA, hr}=\sigma /\mu$). Models were benchmarked across standard operational performance criteria, including the Coefficient of Determination ($R^{2}$), Root Mean Squared Error (RMSE; pax/hr), Mean Absolute Error (MAE; pax/hr), Mean Absolute Scaled Error (MASE; relative to daily persistence), and Mean Forecast Bias. Please see appendix for details on how to interpret these standard operational performance criteria.

### Implications for Final Result Interpretation

When interpreting model evaluation metrics, several operational realities must be considered:

**Dispersion Scale vs. Volume Scale**. Unlike mean hourly throughput volume (which averages ~1,750 pax/hr across dedicated complexes), diurnal throughput standard deviation ($\sigma _{TSA, hr}$) averages 540 to 880 passengers per hour across hub complexes. An RMSE of ~220 pax/hr represents an exceptionally close fit to intraday arrival swings.

**MASE as the Primary Standard for Volatility Forecasting**. MASE normalizes errors against daily persistence ($Vol_{t-24}$). A MASE below 0.85 indicates substantial predictive skill beyond historical patterns, while a MASE below 0.70 represents outstanding accuracy.

**Conformal Staffing Buffers**. Airport security planners can translate predicted throughput volatility directly into risk-buffered lane allocations to prevent queue overflow during peak departure banks.

## Model Results and Evaluation

### Results

Table 4.10 reports the out-of-time evaluation benchmark matrix across the candidate model architectures on the 2025 holdout dataset.

Table 4.10  
*Master Model Benchmark Matrix for TSA Throughput Volatility (2025 Full-Year Holdout)*

### General Model Performance Across the 9-Airport Cohort

The empirical results reveal clear performance separations across the modeling paradigms:

**The Deterministic Schedule Baseline (Model 1)**. Relying solely on published flight schedules, Model 1 achieved $Test R^{2}=0.4980$($RMSE=313.4$ pax/hr, $MASE=0.945$). This outperforms daily persistence by 5.5% ($MASE<1.000$), demonstrating that schedule geometry alone captures approximately half of total checkpoint arrival variance without requiring machine learning infrastructure

**Supervised Machine Learning (Model 2)**. Adding operational flight delays and cancellations elevated explained variance to $R^{2}=0.6178$($RMSE=273.5$ pax/hr, $MASE=0.779$). Diebold-Mariano tests confirm that Model 2's error reduction over the deterministic schedule baseline is statistically decisive ($DM=42.15,p<0.0001$).

**The Dynamic Two-Stage Hybrid (Model 3):** Incorporating live prior-hour error feedback yielded the highest overall holdout fit, explaining 74.83% of passenger throughput volatility variance ($Test R^{2}=0.7483$, $RMSE=222.1$pax/hr, $MASE=0.662$).

### Model Performance and Hypothesis Testing

The thesis hypothesis (Hypothesis 1) asserts that distinct modeling frameworks exhibit asymmetric performance strengths across operational robustness, resilience, and generalizability, with no single paradigm proving universally superior across all operational regimes. To test this hypothesis, candidate architectures were evaluated against explicit performance targets defined across three operational dimensions: Robustness, defined as achieving the lowest $RMSE_{routine}$and $MASE_{routine}<0.70$under Nominal On-Time Baseline conditions; Resilience, defined as maintaining a Recovery Multiplier $R_{RMSE}\approx 1.00$and the lowest $MASE_{shock}$during irregular operations; and Generalizability, defined as maintaining a Relative Transfer Ratio $RTR\approx 1.00$with $\Delta MASE_{transfer}\le 10.0%$under zero-shot spatial transfer without model retraining.

### Empirical Confirmation of Asymmetric Trade-Offs

**Dimension 1: Robustness (Nominal & Routine Conditions)**. Both the Machine Learning model (Model 2) and Dynamic Hybrid (Model 3) achieve the academic target of $MASE<0.70$ under routine operations. However, Model 2 achieves this with near-zero computational overhead and requires no real-time checkpoint data feeds, allowing airport managers to generate staffing schedules days in advance rather than waiting on live hourly sensor updates.

**Dimension 2: Resilience (Severe Disruption). **The Dynamic Hybrid Framework (Model 3) is the decisive champion of Resilience. While the Machine Learning (Model 2) suffers from the "Empty Checkpoint Fallacy" during delayed flight holds ($R_{MASE}=2.14$), Model 3's recursive error feedback ($e_{t-1}$) maintains a resilient multiplier of $R_{MASE}=1.05\approx 1.00$ and achieves the fastest Time-to-Recovery ($TTR=2.8 hours$).

**Dimension 3: Generalizability (Zero-Shot Portability)**. The Deterministic Model (Model 1) is the decisive champion of Generalizability. It successfully meets both stated targets: $RTR=1.04\approx 1.00$ and $\Delta MASE=+4.0%\le 10.0%$. Conversely, the Hybrid model (Model 3) decisively fails the Generalizability targets ($RTR=1.19>1.00,\Delta MASE=+21.5%>10.0%$) because its decision-tree component overfits to Newark's specific terminal layout and carrier bank timings.

The out-of-time holdout evaluations confirm the thesis hypothesis: no single predictive modeling paradigm is universally superior across all operational regimes. Instead, airport security demand forecasting is governed by fundamental asymmetric trade-offs across robustness, resilience, and generalizability. The Dynamic Hybrid model (Model 3) is best during severe flight delays and irregular operations, the Deterministic Schedule model (Model 1) transfers most reliably to new airports without retraining, and the Supervised Machine Learning model (Model 2) is the most practical choice for routine advance staffing. Airport operators and TSA leadership should therefore select their forecasting tool based on daily operating conditions rather than relying on a single method.
