# DRAFT A — CONSERVATIVE INTEGRATION
### *Gleich, L. (2026). Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: TSA Checkpoint Throughput Forecasting and Airside-Landside Queue Dynamics. Master of Science in Aeronautics, Embry-Riddle Aeronautical University.*

---

> **DRAFT NOTES — DRAFT A PHILOSOPHY**
> This draft preserves the tone and accessibility of the submitted committee versions while incorporating the stronger technical specificity, empirical grounding, and structural consistency of the most recent manuscript files. Chapter 1 and Chapter 3 share parallel high-level heading structures (1.1 = Background/Motivation; 1.2 = Significance; 1.3 = Statement of the Problem; 1.4 = Purpose Statement; 1.5 = Research Question; 1.6 = Delimitations; 1.7 = Limitations and Assumptions // 3.1 = Overview and Research Approach; 3.2 = Study Sample and Four-Tiered Filtering; 3.3 = Data Sources; 3.4 = Threats to Validity; 3.5 = Temporal Dynamics; 3.6 = Volatility Framework; 3.7 = Hierarchical Cross-Classification; 3.8 = Statistical Power; 3.9 = Evaluation Framework). Southwest exclusion rationale is upgraded. The lead-lag mechanism is moved from Results into Methodology, and the Hub Disconnect equation appears in both Ch. 3 and Ch. 4.

---

# CHAPTER I: INTRODUCTION

## 1.1 Background and Operational Motivation

As commercial air travel demand continues to outpace the capacity of landside airport terminal infrastructure, inefficient resource allocation at passenger security screening checkpoints has emerged as a critical operational bottleneck across the National Airspace System (Adacher et al., 2017). Airport terminal operators and federal security authorities face a compounding dual challenge: sustaining stringent screening standards while minimizing passenger queue delays. Traditionally, terminal passenger flow forecasting has relied on static, time-of-day planning tables or direct proportional scaling of published airline flight schedules. However, the systemic demand shocks and operational disruptions of the post-pandemic era have exposed severe structural flaws in these conventional forecasting approaches (Hopfe et al., 2024).

Conventional forecast evaluation in transportation planning has historically emphasized average error metrics—such as Root Mean Squared Error (RMSE) or Mean Absolute Percentage Error (MAPE)—evaluated under routine, undisturbed operating conditions. Yet in volatile airport operating environments, a framework based solely on nominal-day accuracy is insufficient. A forecasting model that achieves low average error during calm, clear-weather periods may fail during severe convective weather ground delay programs, unexpected terminal lane closures, or sudden schedule collapses.

In modern airport operations, the most valuable predictive model is not necessarily the one with the lowest marginal error under ideal conditions, but the model that:

1. **Remains reliable during routine operations (Robustness):** Providing consistent, low-error baseline staffing recommendations during undisturbed flight banks.
2. **Maintains stability and recovers rapidly during disruptions (Resilience):** Absorbing severe exogenous shocks—such as winter freeze events or summer convective ground delay programs—without generating false demand collapses or runaway queue backlogs.
3. **Transfers effectively across operational contexts (Generalizability):** Porting its structural logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining.

This study systematically evaluates predictive modeling frameworks—spanning deterministic operational baselines, data-driven gradient-boosted decision-tree architectures, and sequential state-space hybrid models—for forecasting Transportation Security Administration (TSA) checkpoint throughput across routine, volatile, and disrupted demand regimes at the Top 25 U.S. commercial airfields from 2019 through 2025.

---

## 1.2 Significance of the Study

This research contributes to both transportation science theory and practical airport operations by advancing a multidimensional, regime-aware evaluation framework. While traditional airport planning literature treats passenger demand as a static reflection of published departures, this study establishes that passenger arrivals at security screening follow complex behavioral show-up curves (ACRP Report 40, Airport Passenger Terminal Planning and Design) that are decoupled from contemporaneous flight departure timestamps.

By identifying the conditions under which distinct predictive modeling paradigms maintain operational fidelity, this research provides airport Federal Security Directors (FSDs), airline hub operations managers, and FAA planners with actionable, data-driven decision tools. Specifically, the findings demonstrate how integrating airline ticket coupon connecting ratios (BTS DB1B) and real-time flight delay feedback reduces checkpoint forecast error by approximately 14.2% and prevents the severe under-prediction common during severe weather delay cascades. The result is a regime-switched inference framework with direct deployment applicability across the Top 25 U.S. hub network.

---

## 1.3 Statement of the Problem

Airport passenger arrivals and queuing behaviors are inherently uncertain, fluctuating dynamically based on departure bank structures, traveler booking characteristics, and air traffic disruptions (Cheng et al., 2012; Dönmez et al., 2025). Existing models for managing passenger security screening demand frequently rely on static time-of-day curves or pre-pandemic operational assumptions that fail to reflect contemporary travel patterns (Ebert et al., 2021).

This mismatch between checkpoint lane allocation and fluctuating passenger demand contributes to chronic congestion at peak hours, excessive passenger wait times, and inefficient staffing utilization. Critically, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond aggregate, undisturbed accuracy metrics. Because modern airport operations cannot be assumed to follow static, deterministic flight schedules, the absence of a multidimensional evaluation methodology leaves airport authorities at risk of deploying decision tools that collapse during sudden operational disruptions or fail when transferred across unfamiliar terminal complexes.

---

## 1.4 Purpose Statement

The primary objective of this research is to evaluate and compare predictive modeling frameworks—including deterministic time-series baselines, operational decision-tree models, and sequential two-stage hybrid architectures—to optimize airport checkpoint capacity through data-driven operational decision tools rather than costly capital facility expansion.

By analyzing the empirical relationship between airside flight operations and landside TSA security throughput across the Top 25 U.S. commercial airfields from 2019 to 2025, this study assesses model performance against three primary operational criteria: **Robustness**, **Resilience**, and **Generalizability**. Rather than seeking a single, universally optimal model, this research determines which forecasting frameworks perform best under each operational demand state, providing airport authorities with the empirical justification needed to deploy regime-switched forecasting systems.

---

## 1.5 Research Question

Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts and hub topologies) as the primary operational evaluation metric?

---

## 1.6 Delimitations

1. **Geographic Scope:** This study evaluates commercial air traffic and TSA security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications. The experimental cohort is further narrowed to nine airports—Boston Logan (BOS), Dallas/Fort Worth (DFW), Detroit Metropolitan (DTW), Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles International (LAX), New York LaGuardia (LGA), Chicago O'Hare (ORD), and Philadelphia International (PHL)—representing American Airlines, Delta Air Lines, and United Airlines in a balanced factorial design.
2. **Temporal Scope:** The longitudinal dataset spans January 1, 2019 through December 31, 2025. Model training and evaluation are focused on the verified post-pandemic operational regime beginning May 1, 2022 (following the nationwide rescission of federal transportation mask mandates). The full calendar year 2025 is reserved as a strict out-of-time holdout evaluation window.
3. **Data Sources:** Analysis is delimited to publicly accessible and FOIA-disclosed federal aviation datasets, including TSA FOIA hourly screening counts, Bureau of Transportation Statistics (BTS) On-Time Flight Performance (Form 234), BTS Schedule T-100 Segment traffic, and BTS DB1B/DB1C 10% ticket coupon surveys.
4. **Carrier Scope:** The study includes American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA) as the primary legacy network carriers. Southwest Airlines is excluded due to its structurally distinct bimodal passenger arrival timing profile resulting from open-seating boarding and free checked-bag policies.
5. **Evaluation Standards:** Model performance is measured using RMSE, Mean Absolute Error (MAE), Mean Absolute Scaled Error (MASE), the Disruption Error Multiplier ($R_{\text{MASE}}$), the Relative Transfer Ratio (RTR), and Diebold-Mariano tests for statistical significance.

---

## 1.7 Limitations and Assumptions

1. **Staffing and Lane Configuration Opacity:** Due to the proprietary and security-sensitive nature of TSA checkpoint operations, confidential variables—such as exact Transportation Security Officer (TSO) shift allocations, active lane counts per 15-minute interval, and manual queue reconfigurations—are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
2. **Passenger Checked Baggage and Curb Dwell:** Granular airline bag-drop and ticket counter processing logs are proprietary to individual air carriers. The analysis incorporates passenger show-up distributions established in ACRP Report 40 as empirical representations of pre-security lead times, with discrete hourly weights of 25% at $t+1$ (one hour before departure), 55% at $t+2$ (two hours before), and 20% at $t+3$ (three hours before).
3. **Connecting Passenger Survey Stability:** The proportion of transferring passengers who remain airside is estimated using quarterly BTS DB1B coupon surveys. The framework assumes that connecting ratios remain stable across monthly operating horizons within given carrier-terminal complexes.
4. **Operational Exogeneity:** Exogenous severe weather disruptions are captured through departure delay distributions and flight cancellation indicators reported in BTS Form 234 and are treated as exogenous shocks rather than endogenous model inputs.
5. **Non-Traveler Exits:** Individuals who pass through screening checkpoints and subsequently exit without boarding—such as gate pass escorts or aborted-boarding passengers—are assumed to represent a statistically negligible fraction (< 1%) of peak bank screening volume, consistent with federal gate pass restrictions under 49 CFR § 1544.205.

---

# CHAPTER II: REVIEW OF RELEVANT LITERATURE

## 2.1 Traditional Approaches and Operational Complexity

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### 2.1.1 Uncertainty, Batch Arrival Dynamics, and Flight Banks

A fundamental operational challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated waves induced by airline flight bank scheduling (Peterson et al., 1995; Cheng et al., 2012). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities. Consequently, landside screening checkpoints experience severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

### 2.1.2 Classical Queuing Theory Foundations and Limitations

To translate unpredictable passenger movements into quantifiable system states, traditional airport planning has relied upon queuing theory (Odoni, 1986; Wang, 2017). Early terminal capacity models utilized Poisson arrival distributions ($M/M/s$ or $M/G/s$ queues) to calculate queue lengths and average waiting times relative to a target Level of Service (LOS) (Araujo & Repolho, 2015).

However, classical Poisson models rest on the assumption of a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently transitioned toward Non-Homogeneous Poisson Processes (NHPP) to allow arrival rates to vary across hourly intervals (Brunetta et al., 1999), NHPP models still assume independent arrivals. In operational reality, passengers arriving on the same flight are strongly correlated, and hub connecting passengers never enter landside security queues at all (Guo et al., 2022). These simplifying assumptions limit the ability of purely analytical queuing equations to capture the volatility of contemporary terminal operations (Adeke, 2018).

---

## 2.2 Simulation Modeling and Real-Time Terminal Management

### 2.2.1 Discrete Event Simulation (DES) and Operational Limits

To overcome the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES) (Brown & Madhavan, 2011; Leone & Liu, 2011). Unlike static spreadsheets, DES models track individual passengers through a time-indexed sequence of discrete operational milestones—ticket scan, divestiture, metal detector screening, and item retrieval.

Despite high visual fidelity, DES models exhibit critical limitations when deployed for real-time airport management:
1. **Calibration Sensitivity:** Small changes in baseline assumptions—such as secondary bag-search alarm rates or TSO divestiture coaching times—produce disproportionately large shifts in modeled queue wait times (Brown & Madhavan, 2011).
2. **Computational Latency:** Simulating hundreds of thousands of individual passenger agents during severe, unfolding flight disruptions requires immense computational time, rendering DES impractical for real-time tactical lane reallocation (Takakuwa & Oyama, 2004; Bießlich et al., 2014).
3. **Passive Traveler Assumptions:** Standard simulation models treat passengers as passive entities following rigid rules, failing to reflect how travelers dynamically adjust arrival timing based on mobile flight delay notifications (Alodhaibi et al., 2017).

---

## 2.3 Time-Series Analysis and Data-Driven Predictive Frameworks

### 2.3.1 Statistical Time-Series Foundations (ARIMA and SARIMA)

To achieve faster, automated forecasts, transportation planners turned to empirical time-series models such as Autoregressive Integrated Moving Average (ARIMA) and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). These models capture the dominant diurnal (24-hour) and day-of-week (168-hour) cyclical rhythms of airport operations. When augmented with exogenous variables (SARIMAX)—such as scheduled airline seat capacity—they provide computationally lightweight, transparent baseline estimates. However, linear time-series formulations struggle during operational structural breaks, such as severe weather ground stops, because they assume fixed autoregressive relationships that cannot accommodate sudden delay cascades.

### 2.3.2 Non-Linear Machine Learning and Sequential Neural Networks

To model complex non-linear relationships that linear statistical models cannot represent, recent aviation literature has explored machine learning algorithms, including Long Short-Term Memory (LSTM) recurrent networks, Gated Recurrent Units (GRU), and Gradient-Boosted Decision Trees (GBM) (Hopfe et al., 2024; Ribeiro et al., 2025).

While deep neural networks can approximate complex multi-source interactions, they introduce significant operational challenges in airport settings:
- **The Interpretability Barrier:** Airport Federal Security Directors and TSA operations planners cannot verify why a deep neural network predicts a sudden passenger volume spike, making them reluctant to commit staffing resources based on opaque model outputs (Adadi & Berrada, 2018; Viaña et al., 2024).
- **Facility-Specific Over-Specialization:** Highly parameterized neural networks memorize terminal-specific gate layouts, unique local carrier flight banks, and idiosyncratic physical geometry, causing forecast accuracy to degrade sharply when transferred to unfamiliar airports (Wang et al., 2025).

---

## 2.4 Hybrid Architectures: Combining Operational Structure with Data-Driven Adaptability

To resolve the tension between the transparency of traditional queuing models and the non-linear flexibility of modern machine learning, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025).

### 2.4.1 Integrating Queuing Principles with Decision-Tree Algorithms

Rather than deploying fully end-to-end black-box models, effective hybrid architectures combine:
1. **First-Principles Operational Baselines:** Using established flight schedules, empirical passenger show-up curves (ACRP Report 40), and airline connecting passenger survey ratios (BTS DB1B) to establish a deterministic baseline demand estimate.
2. **Transparent Decision-Rule Adjustments:** Deploying interpretable machine learning—specifically Gradient-Boosted Decision Trees—to predict residual demand shifts caused by real-time flight delays, gate holds, and severe weather cancellations (Ribeiro et al., 2025).

Decision trees offer a critical operational advantage over deep neural networks: their branching structure can be directly mapped to operational rules that managers can audit and validate.

### 2.4.2 Dynamic Feedback and Real-Time State Tracking

During severe operational disruptions, static schedules become obsolete. Recent research demonstrates that incorporating recursive error-correction feedback (such as Kalman filtering or sequential residual tracking) allows forecasting models to monitor live checkpoint throughput ($t-1$) and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024).

---

## 2.5 Post-Pandemic Operational Volatility and the Need for Multi-Dimensional Evaluation

While predictive modeling literature has historically focused on maximizing point accuracy under nominal operating conditions, the unprecedented disruptions of the COVID-19 pandemic demonstrated that single-metric evaluations are fundamentally inadequate (Sun et al., 2022; Li et al., 2023). In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

1. **Robustness (Routine Operational Accuracy):** The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations (Lin, 2022).
2. **Resilience (Performance Under Severe Disruption):** The capacity of a forecasting framework to maintain error boundedness, resist demand collapse, and recover rapidly during major exogenous shocks, such as Ground Delay Programs (GDP), severe winter blizzards, and summer convective thunderstorm ground stops (Schultz et al., 2021; Kazda et al., 2022).
3. **Generalizability (Cross-Airport Portability):** The external validity and portability of trained model structures when deployed across structurally diverse airport terminal complexes without requiring site-specific historical recalibration (Tang et al., 2023; Güner & Seçkin Codal, 2024).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.

---

# CHAPTER III: METHODOLOGY

## 3.1 Overview and Research Approach

This chapter details the methodological architecture and empirical framework developed to model, forecast, and evaluate passenger security screening throughput at commercial airports. Traditional airport passenger flow modeling has historically relied on static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems—specifically check-in, passenger security screening checkpoints, and departure concourses—constitute a tightly coupled, stochastic queuing network subject to severe non-linear queuing friction and schedule-driven volatility (De Neufville & Odoni, 2014).

The primary objective is to evaluate the comparative predictive accuracy and operational utility of three distinct forecasting paradigms:
1. **Deterministic Baselines ($M_0, M_1$):** Classical reference benchmarks relying on diurnal seasonal persistence ($y_{t-24}$) and contemporaneous scheduled flight departures.
2. **Probabilistic and Machine Learning Architectures ($M_2, M_3, M_4$):** Data-driven, non-linear formulations incorporating empirical passenger show-up arrival distributions (ACRP Report 40), Gradient Boosted Count Regressors (LightGBM, Tweedie distribution, $p = 1.3$), and multi-source operational feature pipelines.
3. **Sequential Two-Stage Hybrid Frameworks ($M_5$):** Integrated architectures combining queuing dynamics and time-series error correction with non-linear decision trees to dynamically correct queue backlogs during severe operational disruptions.

### 3.1.1 Core Research Hypotheses

The investigation evaluates model performance across three independent operational dimensions:
- **Dimension 1 – Robustness:** Consistency and precision under nominal flow conditions (DepDelay < 15 min).
- **Dimension 2 – Resilience:** Stability, error boundedness, and speed of recovery during severe exogenous shocks (convective summer storm ground stops, winter freeze events).
- **Dimension 3 – Generalizability:** Portability of trained model structures across divergent airport geometries and carrier hub topologies without local retraining.

**Core Research Hypothesis ($H_1$):** Across the three forecasting paradigms, no individual architecture will prove uniformly superior across all three evaluation dimensions. Rather:
- Probabilistic and Machine Learning models will demonstrate superior accuracy during routine operations ($\text{MASE}_{\text{routine}} < 0.70$) by learning complex non-linear calendar and show-up interactions.
- Two-Stage Hybrid frameworks will demonstrate superior resilience during systemic disruptions ($R_{\text{MASE}} \le 1.30$; Time-to-Recovery $\le 4.0$ hours) due to closed-loop queue innovation corrections.
- Structurally parameterized baselines and standardized volatility archetypes will exhibit superior spatial generalizability (Transfer Degradation $\le 15\%$) by abstracting away airport-specific facility over-specialization.

### 3.1.2 Methodological Execution Phases

The implementation follows four sequential, interconnected phases:
- **Phase 1:** Multi-Source Conformed ETL Warehouse Development across four federal aviation data feeds spanning 2019 to 2025.
- **Phase 2:** Purposive Four-Tiered Filtering and Experimental Cohort Isolation to eliminate confounding from multi-carrier passenger mixing and shared checkpoints.
- **Phase 3:** Coupled Volatility Clustering and Hierarchical Stratification to establish the 84-cell cross-classification tensor.
- **Phase 4:** Empirical Model Training, Tuning, and Out-of-Time Holdout Evaluation against the full 12-month 2025 dataset.

---

## 3.2 Study Sample and Four-Tiered Purposive Filtering

To isolate the direct operational link connecting airside flight schedules to landside security checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel designed to eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding anomalies.

### 3.2.1 Macro Filter: Scale and Congestion Regimes

Commercial aviation passenger volumes follow a heavy-tailed power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$). Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures. In airport queuing dynamics, an arrival rate $\lambda(t)$ passing through $c(t)$ screening lanes with service rate $\mu$ yields traffic intensity:

$$\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$$

At small regional airfields, traffic intensity remains sparse ($\rho(t) \ll 0.3$), preventing queue formation and causing throughput to mirror arrivals without boundary resistance. In contrast, Top 25 hub facilities routinely approach or exceed capacity ($\rho(t) \to 1.0$) during morning and evening departure banks (05:00–08:30 and 16:00–18:30), creating the non-linear queue delays necessary to train and validate congestion-aware models.

### 3.2.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion

To ensure cross-carrier comparisons are evaluated under identical exogenous airspace conditions, candidate environments were required to operate concurrent domestic mainline services by American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA), neutralizing common weather and Air Traffic Control (ATC) delay confounders.

Southwest Airlines (WN) was systematically excluded from checkpoint pairing. Legacy carrier passengers display consistent, unimodal lognormal arrival timing:

$$\tau \sim \text{Lognormal}(\mu, \sigma^2), \quad E[\tau] \approx 105 \text{ minutes}$$

In contrast, Southwest's open-seating boarding structure and two-free-checked-bags policy generate a bimodal arrival mixture:

$$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$

where $\mu_1 \approx 135$ minutes for boarding position maximizers and $\mu_2 \approx 65$ minutes for carry-on-only business travelers. Pooling Southwest passenger streams with legacy carriers violates show-up distribution homogeneity and induces unobserved heteroskedasticity in the arrival density kernel.

### 3.2.3 Micro Filter: Carrier Checkpoint Isolation

In shared terminal complexes, multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, flight departure schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), creating an indeterminate collinear system where individual airline demand contributions cannot be mathematically decoupled. Restricting analysis to carrier-exclusive screening environments enforces:

$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$

This eliminates inter-carrier schedule crosstalk (condition number $\kappa < 25$), directly mapping carrier flight banks to landside checkpoint throughput.

### 3.2.4 Balanced Factorial Cohort: The 9-Airport Experimental Sample

Applying the four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort**:
- **American Airlines (AA):** Dallas/Fort Worth (DFW), Philadelphia (PHL), Chicago O'Hare (ORD)
- **Delta Air Lines (DL):** Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)
- **United Airlines (UA):** Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles International (LAX)

This cohort achieves complete factorial symmetry: exactly three legacy carriers × three dedicated terminal environments per carrier, spanning all four operational archetypes identified in national clustering analysis. Regarding specific airport selections: LaGuardia (LGA) was selected over JFK because United permanently vacated JFK in October 2022, failing the Meso continuity requirement; Philadelphia (PHL) was selected over Salt Lake City (SLC) because SLC funnels all carriers through a single consolidated checkpoint, making carrier isolation impossible.

---

## 3.3 Data Sources and Warehouse Conformance

The analytical data foundation integrates four primary federal aviation data feeds over the continuous seven-year baseline from January 1, 2019 to December 31, 2025.

### 3.3.1 TSA FOIA Security Screening Checkpoint Logs

Obtained via Freedom of Information Act (FOIA) disclosures, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### 3.3.2 BTS On-Time Performance (Form 234)

Maintained by the Bureau of Transportation Statistics, this feed records individual domestic flight movements (45,777,091 raw records). The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers, capturing departure delays, taxi-out times, tactical cancellations, and delay cause decompositions.

### 3.3.3 BTS Form 41 Schedule T-100 Domestic Segment Data

Published by the BTS Office of Airline Information, Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors.

### 3.3.4 BTS DB1B / DB1C Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), utilized to extract quarterly connecting passenger ratios across airport pairs. These surveys directly support the connecting passenger deflation formula:

$$\text{Demand}_{\text{originating}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$

---

## 3.4 Threats to Validity and Remediation Protocols

### 3.4.1 Connecting Passenger Bias (The Hub Disconnect)

In hub-and-spoke operations, up to 76% of passengers deplane from inbound flights and transfer to outbound gates entirely airside, never passing through landside security checkpoints. Treating scheduled flight departures or departing seats as raw security demand grossly inflates demand estimates. To eliminate this bias, flight seat capacity is deflated using empirical connecting fractions derived from BTS DB1B surveys, as expressed above.

### 3.4.2 Checkpoint Heterogeneity and Administrative Staffing Shifts

Evaluating individual screening lanes introduces administrative variance resulting from TSO shift rotations and dynamic lane reassignments between TSA PreCheck and standard screening. To achieve operational stability, hourly throughput is aggregated across all lanes within a dedicated terminal complex:

$$Y_{kt} = \sum_{l \in \mathcal{L}_k} y_{k,l,t}$$

Summing across lane complexes transforms noisy lane-level counts into a robust aggregate demand signal that maps to outbound flight banks.

### 3.4.3 Overnight Checkpoint Closures versus Missing Data

Across the warehouse, 450,973 records report zero throughput. Cross-referencing against flight schedules confirmed that 98.6% of zero intervals occur during overnight checkpoint closures (00:00–03:59). Rather than applying naive moving-average imputation—which would introduce artificial passenger traffic during scheduled overnight closures—these intervals are preserved as true operational zeros and modeled using zero-bounded count regression (Tweedie distribution, $p = 1.3$) or zero-inflated hurdle structures.

### 3.4.4 Tactical versus Advance Cancellations

Flight cancellations are treated asymmetrically based on operational timeline causality:
- **Advance Cancellations (>24 hours pre-departure):** Purged from departing seat capacity.
- **Tactical Cancellations (<2 hours pre-departure):** Retained in the passenger arrival curve, because affected passengers have already arrived at the terminal and crossed security checkpoints prior to the carrier issuing the cancellation notice.

---

## 3.5 Temporal Dynamics and Passenger Show-Up Curve Assumptions

### 3.5.1 The Physical Arrow of Time and Lead-Lag Offset

A fundamental modeling assumption is that passenger arrivals at security screening occur 90 to 120 minutes prior to scheduled flight departure, not contemporaneously. This 90-to-120-minute offset reflects the unidirectional physical pipeline of airport terminal operations:

```
Curbside Arrival → TSA Screening → Airside Dwell → Gate Boarding → Pushback
[T – 120 min]     [T – 100 min]   [T – 70 min]    [T – 15 min]   [T = 0]
```

Naive contemporaneous modeling correlates checkpoint throughput at hour $t$ with flights departing during that same hour, introducing a fundamental phase-shift misspecification error. Contemporaneous scheduled flights explain less than 20% of checkpoint throughput variance ($R^2 < 0.20$); explanatory power peaks at Lead $t+2$ ($R^2 = 0.4054$, Pearson $r = 0.6367$), consistent with ACRP Report 40 empirical passenger arrival standards.

### 3.5.2 Empirical Passenger Show-Up Curve (Lognormal Arrival Density Kernel)

Human passenger arrival lead time $\tau$ relative to scheduled departure follows a continuous, right-skewed, unimodal lognormal probability distribution:

$$\tau \sim \text{Lognormal}(\mu \approx 4.65, \sigma \approx 0.35)$$

yielding an empirical mode at $\tau^* \approx 92.5$ minutes prior to pushback. The continuous distribution is discretized into hourly convolution weights for the modeling pipeline:

$$w_1 (\text{lead } 1 \text{ hr}) = 0.25, \quad w_2 (\text{lead } 2 \text{ hr}) = 0.55, \quad w_3 (\text{lead } 3 \text{ hr}) = 0.20$$

Interacting the convolved demand estimate with BTS T-100 monthly route load factors elevates baseline explanatory power to $R^2 = 0.4985$ ($r = 0.7061$) prior to introducing temporal cyclical encodings.

### 3.5.3 Post-Pandemic Temporal Demarcation

The contemporary post-pandemic operational equilibrium is established beginning **May 1, 2022**, anchored by:
1. **Federal Policy Demarcation:** The nationwide federal transportation mask mandate was rescinded on April 18, 2022, marking the legal and operational conclusion of emergency travel restrictions.
2. **CUSUM Structural Stability:** Standardized cumulative residuals stabilize within the control boundary ($|S_t| \le 4.2 < 5.0$) post-May 2022.
3. **Load Factor Recovery:** Top 25 network-wide monthly load factors stabilized at $84.6\% \pm 1.2\%$, confirming steady-state rebound.

The resulting partitioning design:
- *Training Window:* May 1, 2022 – December 31, 2023 (20 months; 122,847 hourly complex observations).
- *Validation Window:* January 1, 2024 – December 31, 2024 (12 months; 72,723 hourly observations).
- *Holdout Test Window:* January 1, 2025 – December 31, 2025 (12 months; 72,053 hourly observations; 215,562 facility-level screening hours).
- *Operational Separation Buffer:* A 7-day purge embargo between evaluation periods eliminates serial delay autocorrelation spillover.

---

## 3.6 Coupled Volatility Framework and Variance Formulations

Traditional terminal planning models categorize time using static calendar bins. However, empirical regression between static scheduled flight movements and airport queue delays yields negligible explanatory power ($R^2 \approx 2.50\%$). Systemic queue breakdown and checkpoint congestion are driven not by baseline volumes, but by coupled volatility and variance mismatch between landside passenger arrivals and airside flight departures.

To formally parameterize operational turbulence, the following daily metrics are calculated for each calendar day $d$ in the analytical window:

### 3.6.1 Within-Day TSA Screening Volatility ($CV_{\text{TSA}, d}$)

$$CV_{\text{TSA}, d} = \frac{\sigma_{\text{hourly},\text{TSA}, d}}{\mu_{\text{hourly},\text{TSA}, d}} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (\text{TSA}_{d,h} - \bar{\text{TSA}}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} \text{TSA}_{d,h}}$$

### 3.6.2 Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)

$$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$

### 3.6.3 Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)

$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

### 3.6.4 The Coupled Volatility Index ($\text{CVI}_d$)

$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

The Coupled Volatility Index serves as an econometric measure of systemic operational vulnerability, directly reflecting the co-occurrence of landside screening surges and airside flight delay dispersion.

---

## 3.7 Hierarchical Cross-Classification Architecture

To establish an unconfounded factorial space for training and benchmarking, the methodology constructs an 84-cell cross-classification tensor:

$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \times 7 \times 3 = 84 \text{ cells})$$

The three constituent axes comprise:

1. **Annual Macro Regimes ($\mathcal{S}$, 4 Regimes):**
   - `1_OFF_PEAK`: Winter Lull & Mid-Autumn Shoulder (Weeks 3–7, 9, 37–50)
   - `2_MID_PEAK`: Spring Ramps & Late-Summer Shoulder (Weeks 1–2, 8, 10–21, 23, 33–36, 51)
   - `3_PEAK`: Summer Severe Weather & Convective Surge (Weeks 22, 24–32: June–August)
   - `4_HOLIDAY`: National Holiday Travel Corridors (Thanksgiving, Christmas/New Year, Memorial Day, July 4th, Labor Day, MLK, Presidents Day)

2. **Weekly Operational Cycles ($\mathcal{D}$, 7 Days, ISO 8601):** Monday through Sunday, isolating distinct business outbound, midweek baseline, and Sunday leisure return profiles.

3. **Diurnal Regimes ($\mathcal{H}$, 3 Non-Consecutive Categories per DOW):** Off-Peak, Mid-Peak, and Peak blocks conditioned on day-of-week queuing dynamics via the Diurnal Operational Turbulence Shock Index, defined as:

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$

Applying 1D K-Means clustering ($k = 3$) on $T_{dow}(h)$ ordered monotonically by turbulence score partitions diurnal operations into three regimes:
- **`1_OFF_PEAK`:** Low Volatility / Overnight Curfew Quiescence ($T < 0.35$)
- **`2_MID_PEAK`:** Moderate Volatility / Midday Steady Flow and Ramp ($0.35 \le T < 0.75$)
- **`3_PEAK`:** High Volatility / Queuing Turbulence ($T \ge 0.75$), capturing empirically non-consecutive dual peaks: Morning Bank Surge (05:00–08:00) driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr) and the Evening Delay Cascade (14:00–22:00) driven by network-wide flight delay dispersion ($\sigma_{\text{Delay}} > 63.4$ min).

---

## 3.8 Statistical Power and Sample Size Sufficiency

To prevent small-sample estimator degradation and ensure statistical degrees of freedom across all 84 cells, sample sizes were audited across the experimental dataset.

- **Training Partition (32 Months):** May 1, 2022 – December 31, 2024 (975 calendar days; 23,400 system hourly time-steps; 122,847 training observations across the 20-month training fold and 72,723 validation observations across the 12-month tuning fold).
- **Holdout Testing Partition (12 Months):** January 1, 2025 – December 31, 2025 (365 calendar days; 8,760 system hourly time-steps; 72,053 complex observations; 215,562 facility-level screening hours).
- **Training Viability ($N_{\text{train}} \ge 50$):** Exactly 83 of 84 cells (98.8%) meet or exceed the minimum training threshold, with a median training depth of 215 observations per cell. The single cell below threshold is Holiday Off-Peak Overnight (00:00–03:00, $N = 48$).
- **Well-Powered Decision-Tree Splits ($N_{\text{train}} \ge 100$):** 65 of 84 cells (77.4%) exceed 100 training observations.
- **Statistical Sample Size Sufficiency ($N_{\text{test}} \ge 30$):** 70 of 84 cells (83.3%) meet Central Limit Theorem sample size thresholds. Remaining cells (18 to 24 observations) satisfy non-parametric Wilcoxon and Diebold-Mariano test requirements.

---

## 3.9 Comparative Evaluation Framework and Model Architectures

### 3.9.1 Model Benchmark Suite ($M_0$ through $M_5$)

- **$M_0$ (Diurnal Seasonal Naive):** Baseline persistence forecasting $y_t = y_{t-24}$.
- **$M_1$ (Contemporaneous SARIMAX):** Seasonal autoregressive integrated moving average with contemporaneous scheduled departures.
- **$M_2$ (Empirical Show-Up Curve Regressor):** Linear model driven by distributed lag passenger arrival curves ($\tau \in [t+1, t+3]$) adhering to ACRP Report 40 distributions.
- **$M_3$ (Operational Count Regressor):** Gradient boosted decision tree under zero-bounded count regression (Tweedie distribution, $p = 1.3$) combining passenger show-up curves with BTS OTP delay and cancellation features.
- **$M_4$ (Full Tri-Modal Pipeline):** Gradient boosted regressor interacting show-up curves with T-100 route load factors and carrier aircraft gauge.
- **$M_5$ (Sequential Two-Stage SARIMA-Tree Hybrid):** First-stage SARIMA capturing linear cyclical trends, cascaded into a secondary decision tree predicting residual errors, equipped with recursive Kalman state innovation feedback ($e_t = y_t - C\hat{x}_{t|t-1}$).

### 3.9.2 Evaluation Metrics

- **Root Mean Squared Error (RMSE):** Penalizes large peak-hour forecast errors.
- **Mean Absolute Error (MAE):** Measures average absolute volume deviation.
- **Mean Absolute Scaled Error (MASE):** Scaled against the naive in-sample persistence benchmark:
  $$\text{MASE} = \frac{\frac{1}{N}\sum_{t=1}^N |y_t - \hat{y}_t|}{\frac{1}{N-24}\sum_{t=25}^N |y_t - y_{t-24}|}$$
  where $\text{MASE} < 1.0$ indicates outperformance relative to diurnal persistence.
- **Disruption Error Multiplier ($R_{\text{MASE}}$):**
  $$R_{\text{MASE}} = \frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$$
  evaluating performance stability under convective disruptions ($R_{\text{MASE}} \le 1.30$ denoting resilience).
- **Transfer Error Penalty (Relative Transfer Ratio, RTR):**
  $$\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$$
  evaluating spatial portability under direct cross-airport deployment without site-specific retraining.
- **Diebold-Mariano Hypothesis Testing:** Assesses the pairwise statistical significance of forecast error differentials between competing architectures.

---

# CHAPTER IV: RESULTS (EMPIRICAL FINDINGS)

## 4.1 Master Descriptive Statistics and Data Health Census

To construct an empirically rigorous and leak-free modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational data covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository encompassed 67.22 million raw fact records across TSA checkpoint logs, Bureau of Transportation Statistics On-Time Performance (OTP), BTS Form 41 Schedule T-100 Segment data, and BTS DB1B/DB1C ticket coupon surveys.

Following conformed extraction, cleansing, and relational joining across standardized dimension keys, the nationwide post-ETL analytical warehouse contains **42,062,039 cleaned records** across all 25 candidate commercial airfields. Table 4.1 details the post-ETL data foundation census across the four integrated feeds.

**Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)**

| Primary Data Feed | Entity Grain | Raw Rows | Post-ETL Rows | Network Coverage | Conformance Status |
| :--- | :--- | :---: | :---: | :--- | :--- |
| **TSA FOIA Checkpoint Logs** | Checkpoint-Lane-Hour | 19,500,286 | 6,434,732 | 25 Airfields, 955 Screening Lanes | 100% Non-Null; 2.70 Billion Passengers Screened |
| **BTS On-Time Performance (OTP)** | Flight Departure | 45,777,091 | 13,153,654 | 25 Airfields, 17 Reporting Carriers | 100% Non-Null; 13.15 Million Domestic Departures |
| **BTS Form 41 Schedule T-100** | Carrier-Route-Month | 1,945,451 | 422,096 | 25 Airfields, 18 Operating Carriers | 100% Non-Null; 2.09 Billion Departing Seats |
| **BTS DB1B / DB1C Ticket Surveys** | Ticket Coupon Itinerary | 12,910,384 | 22,051,557 | Closed 25-Airport City Pairs | 100% Non-Null; 62.16 Million Ticketed Travelers |
| **Combined Analytical Warehouse** | Multi-Source Fact | 67,222,828 | 42,062,039 | Full 25-Airfield Network | 100% Referential Integrity |

**Table 4.2: Post-ETL Master Summary Descriptive Statistics (Cleaned Data Warehouse)**

| Domain | Variable | N | Mean | Median | Std Dev | Min | Max |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **TSA Throughput** | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 293.00 | 444.84 | 0.00 | 5,336.00 |
| **Flight Delays** | Departure Delay (min) | 13,153,654 | 12.70 | -2.00 | 52.75 | -105.00 | 3,695.00 |
| **Flight Delays** | Significant Delay Rate (≥ 15 min) | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 100.00% |
| **Flight Operations** | Cancellation Rate | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 100.00% |
| **Flight Operations** | Taxi-Out Queue Time (min) | 13,153,654 | 18.84 | 16.00 | 10.03 | 1.00 | 180.00 |
| **Route Capacity** | Available Seats per Route-Month | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 1.00 | 145,200.00 |
| **Route Capacity** | Route Load Factor (%) | 422,096 | 81.21% | 83.40% | 11.80% | 0.00% | 100.00% |
| **Passenger Surveys** | Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 50.73% | 11.74% | 33.58% | 76.04% |

### 4.1.1 Spatial Key Resolution and Metadata Remediation

Upstream TSA FOIA records exhibited 35,809 records with missing or malformed airport identifiers. An automated checkpoint fingerprinting algorithm successfully recovered 7,489 records by matching historical checkpoint naming signatures. The remaining 22,190 unresolvable records were mapped to a conformed surrogate key (airportId = 0, flagged with airportMissing = 1). Without this remediation, these unmapped rows would aggregate approximately 9.71 million passengers into unidentified airport records, severely distorting national baseline models. All subsequent modeling queries strictly enforce `WHERE airportMissing = 0 AND airportId > 0`.

### 4.1.2 Nighttime Checkpoint Closures versus Missing Data

Exactly 450,973 records (2.31% of warehouse volume) report zero passengers. Cross-referencing these intervals against airport operational schedules confirmed that 98.6% of zero values occur during the early-morning non-operational window (00:00 to 03:59 local time). These intervals are preserved as true operational zeros and modeled using zero-bounded count regression (Tweedie distribution, $p = 1.3$).

### 4.1.3 Flight Delays and Advance versus Tactical Cancellations

Across the 13,153,654 domestic departures, the mean departure delay was 12.70 minutes, with 20.12% of flights experiencing departure delays ≥ 15 minutes. Flight cancellations accounted for 2.03% of scheduled operations (267,019 flights). To maintain strict operational timeline causality: advance cancellations (>24 hours pre-departure) were purged from departing seat capacity; tactical cancellations (<2 hours pre-departure) were retained in the passenger demand curve, reflecting that affected travelers had already crossed landside security checkpoints.

---

## 4.2 The Four-Tiered Purposive Filtering Pipeline

To eliminate confounding from multi-carrier passenger pooling and isolate the direct relationship connecting scheduled flight departures to checkpoint queues, commercial airfields were screened through the four-tiered purposive filtering pipeline detailed in Chapter III.

### 4.2.1 Macro Filter: Scale and Peak-Hour Checkpoint Congestion

Restricting to the Top 25 commercial airfields captures 67.2% of nationwide domestic flight movements. Top 25 hubs reach peak-hour checkpoint congestion ($\rho(t) \to 1.0$) during morning and evening departure banks, creating the empirical queue delays and non-linear dynamics required to train and validate congestion-aware models.

### 4.2.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion

By requiring concurrent mainline operations by American, Delta, and United, cross-carrier contrasts evaluate under identical exogenous airspace disruptions, canceling common weather and FAA ground delay confounders. Southwest Airlines was excluded due to its bimodal arrival mixture ($\mu_1 \approx 135$ min for boarding group position maximizers; $\mu_2 \approx 65$ min for baggage-free business travelers), violating show-up distribution homogeneity.

### 4.2.3 Micro Filter: Carrier Checkpoint Isolation

Restricting analysis to carrier-exclusive checkpoints isolates single-carrier operations ($P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$), eliminating multi-carrier schedule overlap (condition number $\kappa < 25$) and directly mapping carrier flight banks to landside checkpoint throughput.

### 4.2.4 The 9-Airport Experimental Factorial Grid

The filtering pipeline yielded the **9-Airport Experimental Cohort (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL)**, achieving complete factorial balance across three legacy carriers and four operational clusters identified in the national clustering analysis.

---

## 4.3 Empirical Operational Clusters and Systemic Trends

Unsupervised machine learning (PCA coupled with K-Means and Ward's Hierarchical Clustering) evaluated across standardized operational metrics revealed four distinct operational archetypes across the Top 25 airfields.

| Cluster Archetype | Count | Member Airfields | Mean TSA | Conn. Ratio | Load Factor | Mean Delay |
| :--- | :-: | :--- | :-: | :-: | :-: | :-: |
| **0: Mega-Connecting Gateways** | 8 | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 56.1% | 85.7% | 15.6 min |
| **1: High-Density O&D Focus** | 6 | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 48.4% | 83.4% | 15.0 min |
| **2: High-Reliability Fortress Hubs** | 8 | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 54.1% | 84.5% | 11.6 min |
| **3: Congested Coastal Originators** | 3 | EWR, JFK, LGA | 85.6M | 37.4% | 85.4% | 16.1 min |

### 4.3.1 The Hub Disconnect: Connecting versus Local Originating Passengers

A central empirical finding is the structural disconnect between airside scheduled flight departures and landside security screening volume at major hub airports. At Charlotte (CLT), total departing seat capacity exceeded 34 million passengers, yet total TSA checkpoint throughput was only 28.2 million. Incorporating the BTS DB1C 76.0% connecting ratio resolves this disconnect: over 26 million passengers transferred airside between concourses without ever entering landside security queues. Failing to apply the connecting passenger deflator causes status-quo planning models to overpredict checkpoint volume by over 200%.

### 4.3.2 Delay Transmission Divergence

Cluster 2 airfields (DTW, MSP, SLC, PHL) handle immense connecting volume with exceptional fluidity (mean delay = 11.6 min; taxi-out = 18.7 min). Conversely, Cluster 3 airfields (EWR, JFK, LGA) suffer chronic delay burdens (mean delay = 16.1 min; taxi-out = 24.3 min) despite operating smaller regional gauge, demonstrating that terminal congestion is driven by airspace slot caps and runway geometry rather than passenger volume alone.

### 4.3.3 Empirical Coupled Volatility Regimes

**Table 4.3: Master Annual Seasonal Volatility Regimes Summary**

| Seasonal Regime | Calendar Days | Mean Daily TSA | Within-Day TSA CV | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Cancellation Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`1_OFF_PEAK`** | 500 (37.3%) | 1,123,386 | 0.605 | 46.09 min | 27.85 | 0.89% |
| **`2_MID_PEAK`** | 426 (31.8%) | 1,187,095 | 0.589 | 55.06 min | 32.38 | 1.36% |
| **`3_PEAK`** | 224 (16.7%) | 1,305,968 | 0.576 | 68.43 min | 39.36 | 3.16% |
| **`4_HOLIDAY`** | 191 (14.2%) | 1,215,636 | 0.597 | 55.78 min | 33.07 | 1.82% |

Flight departure delay standard deviation scales monotonically from 46.09 minutes during the winter lull (Off-Peak) to 68.43 minutes during the summer convective peak—a 48.5% dispersion expansion. Concurrently, the Coupled Volatility Index escalates from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.

### 4.3.4 Day-of-Week Cyclical Dynamics

**Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes**

| Day | Archetype | Mean Daily TSA | Within-Day TSA CV | Delay Dispersion | Coupled Volatility Index |
| :---: | :--- | :---: | :---: | :---: | :---: |
| **Monday** | Outbound Business Surge | 1,246,150 | **0.604** | 56.56 min | **34.00** |
| **Tuesday** | Midweek Reset (Low Turbulence) | 1,076,625 | 0.601 | **50.09 min** | **29.99** |
| **Wednesday** | Midweek Baseline (Minimum Volatility) | 1,123,368 | 0.594 | **49.27 min** | **29.13** |
| **Thursday** | Corporate Outbound & Early Weekend Ramp | 1,254,744 | 0.589 | 54.65 min | 31.96 |
| **Friday** | Combined Business & Weekend Getaway Surge | 1,241,359 | 0.592 | 55.58 min | 32.77 |
| **Saturday** | Volume Trough & Fleet Repositioning | 1,089,699 | 0.602 | 54.16 min | 32.45 |
| **Sunday** | Leisure Return Peak & Evening Delay Cascade | 1,279,017 | 0.577 | **58.07 min** | **33.40** |

### 4.3.5 Diurnal Operational Turbulence and Non-Consecutive Dual Peaks

The 24 hours of each day were clustered into exactly three regimes based on the Operational Turbulence Shock Index $T(h)$, which captures the maximum of passenger screening surge volatility and flight departure delay dispersion:

1. **`1_OFF_PEAK` (Overnight & Curfew Valley):** Typically covering 00:00 to 03:00, where commercial departures are sparse and checkpoint demand is quiescent.
2. **`2_MID_PEAK` (Midday Plateau & Transition):** Covering 08:00 to 13:00/16:00, characterized by steady passenger screening flow and balanced aircraft turnaround buffers.
3. **`3_PEAK` (High Queuing Turbulence / Dual Non-Consecutive Peaks):** Groups two distinct, non-consecutive turbulence periods into a single operational regime: the **Morning Bank Surge (05:00–08:00)** driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr), and the **Evening Delay Cascade (14:00/17:00–22:00)** driven by upstream flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min).

---

## 4.4 Temporal Demarcation: Post-Pandemic Regime Selection

| Evaluation Criteria | Candidate A: Mature Post-Pandemic | **Candidate B: Early Post-Mask Regime (RECOMMENDED)** |
| :--- | :--- | :--- |
| **Start Date** | January 1, 2023 | **May 1, 2022** |
| **Statistical Justification** | Rolling Welch's t-test convergence | CUSUM stabilization; Mask Mandate Repeal |
| **Training Data Span** | 24 Months | **32 Months (2022-05 to 2024-12)** |
| **Robustness Impact** | Excellent baseline stability | **Superior (Captures 2 full annual cycles)** |
| **Resilience Impact** | Fails to capture Winter Storm Elliott (2022) | **Superior (Captures Elliott & Summer '23)** |
| **Generalizability Impact** | Smaller sample for spoke airfields | **Superior (122k+ modeled observations)** |

Structural break tests confirmed May 1, 2022 as the optimal demarcation point. The Chow Test null hypothesis of parameter constancy is rejected across 2020 through Q1 2022 ($p < 0.0001$), but fails to reject ($p = 0.18$) beginning May 2022.

---

## 4.5 Econometric Validation of Carrier Checkpoint Isolation

To empirically validate the methodological requirement of restricting analysis to carrier-exclusive checkpoints, three formal econometric tests were conducted:

| Econometric Test | Empirical Result |
| :--- | :--- |
| **Volume Conservation** ($\rho = \text{TSA}_\text{actual} / \text{Est}_\text{Originating}$) | **$\rho = 1.00 \pm 0.04$ ($p < 0.001$)**; terminal TSA volume matches carrier originating passengers. |
| **Zero-Flight Intercept** ($Y_{kt} = \beta_0 + \beta_1 \cdot \text{Seats}_t$) | **$\beta_0 = 12.4$ pax/hr ($t = 0.84, p = 0.40$)**; zero flights yield zero queue demand. |
| **Cross-Carrier Checkpoint Independence** | **$\beta_{\text{other}} = 0.002$ ($p = 0.62$, partial $R^2 < 0.001$)**; non-tenant carriers contribute zero demand. |

Furthermore, predicting dedicated terminal checkpoint throughput using carrier-filtered flights achieved $R^2 = 0.708$ to $0.774$, whereas predicting using total pooled airport departures collapsed explanatory power to $R^2 < 0.420$ ($p < 0.0001$). A Kolmogorov-Smirnov test between physically separate terminal buildings (BOS, DTW, LGA, ORD, EWR) and walkway-connected terminals (LAX, DFW, IAH, PHL) revealed no significant divergence ($D = 0.032, p = 0.28$), confirming that post-security terminal cross-over in connected layouts is statistically negligible.

---

## 4.6 Feature Engineering and Passenger Show-Up Curve Estimation

Analysis of lead-lag dynamics between scheduled flight departure times and landside checkpoint throughput demonstrated severe temporal asynchrony:

| Flight Feature Representation | Linear $R^2$ | Pearson Corr ($r$) | Regression Slope |
| :--- | :---: | :---: | :---: |
| **Contemporaneous Departures ($t$)** | 0.1988 | 0.4459 | 38.42 pax/flight |
| **Lead Horizon $t+1$ (1 hr pre-dep)** | 0.3723 | 0.6102 | 62.15 pax/flight |
| **Lead Horizon $t+2$ (2 hr pre-dep)** | **0.4054 (PEAK)** | **0.6367** | **74.98 pax/flight** |
| **Lead Horizon $t+3$ (3 hr pre-dep)** | 0.3299 | 0.5744 | 51.20 pax/flight |
| **Passenger Show-Up Curve (Lead-Lag Distribution)** | **0.4878** | **0.6985** | 74.98 pax/flight |
| **Show-Up Curve × T-100 Load Factor** | **0.4985** | **0.7061** | **90.56 pax/flight** |

Contemporaneous scheduled flights explain less than 20% of checkpoint throughput variance. Explanatory power peaks at Lead $t+2$ ($R^2 = 0.4054$), confirming the 90–120 minute modal passenger show-up window established in ACRP Report 40. Interacting the passenger show-up distribution with monthly T-100 route load factors elevates predictive capability to $R^2 = 0.4985$ prior to introducing temporal cyclical encodings.

---

## 4.7 Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)

Models were trained on Candidate B data (May 2022 – December 2023; 122,847 observations), tuned on 2024 validation data (72,723 observations), and evaluated against the 72,053 hourly complex observations of the 2025 out-of-time holdout across the 9-airport cohort:

| Model Paradigm | ID | Architecture | Val $R^2$ | Test $R^2$ | Test RMSE | Test MAE | Test MASE |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Deterministic Baseline** | M0 | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1377.3 | 939.8 | 1.000 |
| **Deterministic Baseline** | M1 | Contemporaneous Sched SARIMAX | 0.4338 | 0.4375 | 1393.8 | 1042.6 | 1.109 |
| **Probabilistic / ML** | M2 | Passenger Show-Up Curve Only | 0.5443 | 0.5862 | 1195.5 | 856.2 | 0.911 |
| **Probabilistic / ML** | M3 | Show-Up Curve + OTP Delays/Cancels | 0.5450 | 0.5880 | 1192.9 | 855.1 | 0.910 |
| **Probabilistic / ML** | M4 | Full Tri-Modal Pipeline (Load Factor Scaled) | 0.5798 | 0.5771 | 1208.6 | 856.3 | 0.911 |
| **Two-Stage Hybrid** | M5 | Sequential SARIMA-Tree Hybrid | **0.6644** | **0.6270** | **1135.0** | **795.0** | **0.846** |

### 4.7.1 Model Performance Stratification Across Volatility Regimes

Evaluating model architectures across the stratified volatility regimes reveals striking performance divergences:
- **In Low-Volatility Regimes (`1_OFF_PEAK`):** The Gradient Boosted Count Regressor (M3) and Sequential Hybrid (M5) achieve near-identical accuracy (MASE ≈ 0.60–0.62). In stable flow environments, complex Kalman state corrections offer marginal incremental benefit over gradient boosted decision trees.
- **In High-Volatility Regimes (`3_PEAK` Summer Severe Weather):** The performance gap between M3 and M5 widens dramatically. Because extreme convective storms cause flight delays exceeding 3–5 hours, M3 suffers from the "empty checkpoint fallacy," degrading to MASE = 1.025. In contrast, the Two-Stage Hybrid (M5) dynamically incorporates prior-hour terminal congestion feedback ($t-1$), maintaining robust error bounds (MASE = 0.737, RMSE = 1,023.2).

---

*END OF DRAFT A — Chapters I through IV*
