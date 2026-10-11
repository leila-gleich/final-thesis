# Chapter III: Methodology

This chapter details the approach and analytical framework to evaluate and optimize passenger flow forecasting, specifically at airport security checkpoints. To provide a structural roadmap for this investigation, the methodology is organized into five components:

* Research Approach: Establishes the theoretical framework, research variables, hypotheses, experimental design, and the technical apparatus utilized.
* Sample: Outlines the multi-tiered macro and micro sampling frameworks used to categorize physical checkpoint environments and terminal architectures.
* Sources of Data: Identifies the primary authorized data repositories supplying the longitudinal datasets.
* Validity: Addresses and controls internal and construct threats, specifically related to passenger flow bias and screening lane heterogeneity.
* Treatment of Data: Details the sequential pipeline used to ingest, clean, standardize, and align the data sources.

## Research Approach

The study uses an exploratory, sequential, quantitative design to systematically assess the predictive accuracy and operational utility of distinct forecasting approaches for passenger flow forecasting at airport security checkpoints. While this study evaluates a broad range of frameworks – including static deterministic baselines – it asserts that to truly optimize checkpoint flows, terminal subsystems (i.e., check-in, security screening, and boarding) must ultimately be treated as a stochastic queuing network capable of absorbing dynamic, schedule-driven variability (De Neufville & Odoni, 2014). The primary objective is a comparison of three model families (Figure 1): deterministic baselines, probabilistic and data-driven models, and hybrid frameworks. Deterministic baselines serve as reference cases based on historical averages and scheduled operations. Probabilistic and data-driven models include methods such as SARIMA, LSTM, and random forest models that are designed to capture temporal variation. Hybrid frameworks combine queueing theory with exogenous operational data to reflect both system structure and observed schedule effects.

The predictive capabilities of each model configuration focus on three core performance measures: robustness, resilience, and generalizability. In this investigation:

Robustness: Consistency and precision under nominal on-time operating conditions and routine daily operations.

Resilience: Stability, error boundedness, and speed of recovery after severe exogenous operational disruptions.

Generalizability: Performance across different airports or terminal layouts under zero-shot spatial transfer without local retraining.


### Core Research Variables

Independent Variables: Scheduled flight departures, actual flight performance data (departure delays, taxi-out queues, tactical cancellations), terminal structure categories, and origin-and-destination passenger ratios. Dependent variables include TSA checkpoint throughput, queue wait times, and bottleneck formation rates. Comparative predictive model performance across the candidate models will serve as a secondary outcome.


### Research Hypothesis

Core Research Hypothesis (H1 – Master Asymmetric Trade-Off Hypothesis). Across the candidate modeling paradigms evaluated following four-tiered purposive filtering (deterministic flight schedules, supervised machine learning, and dynamic two-stage hybrid), no individual approach will prove superior across all three performance measures (robustness, resilience, and generalizability); rather, each modeling paradigm exhibits distinct operational strengths and stark asymmetric trade-offs:

Robustness Performance: Under nominal operating conditions (departure delays < 15 minutes, zero cancellations), machine learning and dynamic hybrid models achieve target robustness (MASE < 0.700), with machine learning delivering a computationally lightweight, Pareto-efficient routine solution with zero feedback compute latency.

Resilience Performance: Under severe operational disruptions (departure delays ≥ 45 minutes or cancellations ≥ 5), the dynamic two-stage hybrid model demonstrates superior resilience (R_MASE ≈ 1.00, TTR < 4.0h) by utilizing live floor error feedback to track stranded passenger crowds, whereas pure machine learning collapses due to the Empty Checkpoint Fallacy.

Generalizability Performance: Under zero-shot cross-airport transfer without local retraining, the deterministic flight schedule model achieves superior generalizability (RTR ≈ 1.00, ΔMASE ≤ 10.0%) due to terminal geometry invariance, whereas hybrid models experience transfer penalties from terminal layout overfitting.

Detailed hypothesis formulations, sub-hypotheses (H1a, H1b, H1c), formal mathematical evaluation thresholds, and Diebold-Mariano test specifications are compiled in the Appendix.


### Design and Procedures

This investigation follows an exploratory, quantitative, non-experimental design executed across four sequential phases:

Phase 1: Ingestion and Harmonization (ETL): Compiling, cleansing, and relationally joining multi-source federal datasets spanning 2019 to 2025 across common spatial and temporal dimensions.

Phase 2: Model Configuration and Training: Calibrating the candidate modeling suite—the Baseline Control (daily persistence), Model 1 (Deterministic Flight Schedule Model), Model 2 (Supervised Machine Learning Model), and Model 3 (Dynamic Two-Stage Hybrid Model)—across the post-pandemic development partition.

Phase 3: Out-of-Time Holdout Execution: Benchmarking all candidate models against the untouched full-year 2025 holdout dataset under nominal, routine, and disrupted operational regimes.

Phase 4: Comparative Evaluation and Strategic Synthesis: Assessing models across the evaluation triad to determine asymmetric trade-offs, evaluating the Values versus Volatility paradigm, and formulating an operational decision playbook.


Figure 3  
*Design and Procedure Phases*

![Figure 3: Design and Procedure Phases](../../figures/ch03_methodology/Combined_Data_Pipeline_and_Funnel_Lifecycle.png)

*Note.* High-Performance Computing (HPC) sequential extract, transform, and load pipeline coupling TSA FOIA throughput records with BTS operational datasets.


### Apparatus and Materials

To manage, parse, and evaluate the large datasets required for this study, the following software and computing resources are used:

Google Antigravity & Python Analytics Stack: The primary computational environment for automated data ingestion, spatial key resolution, relational joins, and machine learning model training.

Persistent Cloud Data Warehouse: Secure, version-controlled cloud storage maintaining complete conformed master datasets, relational lookup dimensions, and audit logs to ensure scientific reproducibility.

Microsoft Excel for Mac & Microsoft Power BI: Deployed locally for advanced data transformation, tabular synthesis, and visual validation.


## Sample

The sample consists of airport checkpoint environments selected to reflect variation in terminal structure and airline dominance. Airports are grouped into structured categories to account for how physical layout influences passenger distribution and checkpoint use (OAG, 2026). This strategy is intended to support comparison across terminal types and carriers rather than to claim complete uniformity across airports and airlines.


### Macro Categorization: Terminal-to-Airline Distribution

Airports are first classified into four structural archetypes to control for how airline market share impacts terminal distribution, with structural archetypes outlined below:

Mega Hubs with No Dedicated Terminals (e.g., ATL, CLT, DEN): Sprawling operations where major legacy carriers share linear concourses or central ticketing, distributing passenger volume across shared screening areas.

Decentralized Airline-Dedicated Terminals (e.g., LAX): Dispersed multi-terminal airports where distinct physical buildings are allocated exclusively to individual legacy carriers, isolating an airline's passenger wave to specific physical checkpoints.

Single-Carrier Dedicated Mega-Terminals (e.g., DTW): Single-carrier "fortress" environments where a single dominant airline channels its entire domestic and international operation through one massive mega-terminal (e.g., Delta’s exclusive hold on the McNamara Terminal).

Airports with Multiple Terminals Dedicated Exclusively to One Airline (e.g., DFW): Large-scale regional hubs requiring a single dominant carrier to distribute hub-and-spoke operations across multiple independent terminal buildings (e.g., American Airlines utilizing Terminals A, B, C, and E) to scale its operations.


### Micro-Level Refinement: Checkpoint Co-Location and Isolation

While macro terminal assignments establish an operational baseline, localized checkpoint-level configurations ultimately determine queue characteristics. American Airlines, Delta Air Lines, and United Airlines are selected for analysis. The explicit criterion for inclusion is a domestic enplanement market share exceeding 10% at major United States hub airports (BTS, 2026). Recent reporting suggests Southwest’s boarding and carry-on system is both distinctive and inconsistent: the airline still relies on a differentiated low-fare brand, but its newer assigned-seating and baggage-fee policies have increased carry-on pressure and created boarding congestion (Boston 25 News, 2026). To isolate the effects of low-cost carriers and unaligned traffic from legacy airline operations, the following terminal and checkpoint characteristics are defined to account for the impact of extenuating variables:

Shared Checkpoints with Limited Carrier-Level Separation (Centralized): In centralized hub models like Salt Lake City (SLC), a dominant carrier may hold the majority market share (70%), but a single consolidated terminal channels 100% of passengers through one primary security checkpoint. In these environments, it is not readily possible to isolate carrier-specific passenger flows using the available data structures.

Isolated Checkpoints (Decentralized): To find checkpoints highly unlikely to see Delta, American, or United traffic, the methodology prioritizes decentralized layouts with extreme carrier polarization, such as the following:

DCA (Terminal 1): Consisting of Gates A1–A9, this terminal exclusively serves Air Canada, Frontier, and Southwest. American, Delta, and United are completely segregated into Terminal 2, creating a strong comparison setting for low-cost and regional carrier processing behaviors.

SEA (Decentralized Main Terminal): Utilizing five separate security checkpoints across a footprint dominated by Alaska Airlines (52% market share). Checkpoints feeding Alaska-heavy gates or dedicated satellite concourses offer a high statistical probability of isolating non-Big Three passenger flows.

CLT (Extreme Dominance Isolation): Where American Airlines controls 90% of the market share. Because Delta (2.5%) and United (2%) maintain a negligible footprint across the airport's 5 checkpoints, nearly any selected lane acts as a functional monoculture for a single legacy carrier's hub behavior.


### Four-Tiered Purposive Filtering Pipeline

To systematically isolate the direct operational link connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel:

Tier 1: Macro Filter (Scale and Congestion Regimes). The macro filter restricts the initial sampling universe to high-volume commercial airfields where heavy passenger traffic intensity routinely approaches screening capacity, generating the non-linear queuing delays and buffer depletion necessary to train and validate congestion-aware models.

Tier 2: Meso Filter (Airspace Shock Invariance). The meso filter requires candidate environments to operate concurrent domestic mainline services by American Airlines, Delta Air Lines, and United Airlines under identical regional meteorological and air traffic management conditions, neutralizing exogenous airspace disruption confounders while excluding low-cost carrier churn.

Tier 3: Micro Filter (Carrier Checkpoint Isolation). The micro filter restricts analysis to terminal environments where carrier-exclusive gate footprints map directly to dedicated security screening checkpoints, eliminating inter-carrier schedule collinearity and multi-airline passenger crosstalk.

Tier 4: Factorial Cohort (Orthogonal Factorial Balance). The factorial cohort establishes a balanced experimental matrix across the legacy carriers and terminal structural archetypes, ensuring factorial symmetry and preventing geographic or facility-specific bias in cross-airport model evaluations.


### Temporal Scope and Boundary Definition

To ensure structural modeling integrity, the temporal boundaries of this sample exclude the systemic operational volatility induced by the COVID-19 pandemic (Sun et al., 2021; Gao, 2022). While a baseline 'post-pandemic' operational era is provisionally considered as beginning January 1, 2023, an exploratory analysis is performed during data preprocessing to refine this demarcation due to varying definitions of ‘post-pandemic’ (ICAO, 2024; Centre for Aviation, 2025). This preprocessing step evaluates pre-pandemic baseline patterns against longitudinal 2019–2025 data to pinpoint the empirical inflection point where system throughput and schedule deviations returned to steady-state normalization. Structural break tests, rolling Welch's  $t$ -tests, and CUSUM analyses identified May 1, 2022 as the empirical inflection point, coinciding with the vacatur of the federal transit mask mandate and the rebound of airline load factors to 84.7%, matching pre-pandemic baselines. Restricting the active dataset to this verified window enables the forecasting models to capture contemporary queue dynamics and schedule-driven variability without being skewed by transient historic anomalies.


## Sources of Data

Secondary operational data are compiled from four primary authorized federal repositories covering the longitudinal study period: Transportation Security Administration (TSA) Freedom of Information Act (FOIA) Security Screening Checkpoint Logs, Bureau of Transportation Statistics (BTS) On-Time Flight Performance records, BTS Form 41 Schedule T-100 Domestic Segment Data, and BTS Origin and Destination Ticket Surveys (DB1B). Together, these longitudinal feeds capture hourly physical screening counts across checkpoint lanes, individual domestic flight movements and delay cause decompositions, aircraft seating configurations and route load factors, and quarterly passenger itinerary connection ratios. Complete repository profiles, entity grains, and operational attributes are detailed in Table A.3 and the Appendix.


## Validity

A major threat to internal model validity is the presence of connecting passengers who remain airside and do not pass through a public checkpoint in load factor data. Including them in checkpoint demand estimates inflates predicted originating demand. To reduce this bias, origin-and-destination data is used to estimate and remove connecting traffic from passenger flow calculations. Construct validity is also affected by checkpoint heterogeneity, as the raw lane counts obtained from TSA Throughput data combine different screening modes, such as TSA PreCheck, and their corresponding processing rates.


## Treatment of the Data

Data processing follows a sequential pipeline. First, raw BTS and TSA files are exported and parsed using Python on the institutional computing environment. Timestamps are standardized to a uniform operational clock matching local airport solar time. Scheduled overnight checkpoint closures are preserved as true operational structural zeros, and advance cancellations are separated from tactical cancellations to preserve information causality. Lastly, flight departure times are aligned with passenger lead-time assumptions from ACRP Report 40 and merged with hourly TSA throughput intervals to create a final modeling dataset, with the exhaustive ETL data engineering protocol detailed in the Appendix.
