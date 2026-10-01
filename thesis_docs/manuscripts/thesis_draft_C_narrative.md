# DRAFT C — PRACTITIONER-VOICE / NARRATIVE-FORWARD
### *Gleich, L. (2026). Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: TSA Checkpoint Throughput Forecasting and Airside-Landside Queue Dynamics. Master of Science in Aeronautics, Embry-Riddle Aeronautical University.*

---

> **DRAFT NOTES — DRAFT C PHILOSOPHY**
> Draft C prioritizes narrative continuity, operational storytelling, and plain-language accessibility without sacrificing academic rigor or empirical precision. Mathematical formulas are present but introduced through operational context rather than leading with them. The voice is closer to a policy-facing report or aviation industry white paper that a Federal Security Director, airport operations director, or thesis committee with mixed technical backgrounds could follow. Chapter 1 and Chapter 3 maintain the same parallel top-level heading structure as Drafts A and B. All empirical claims are identical to Drafts A and B; only the presentation order and prose framing differ.

---

# CHAPTER I: INTRODUCTION

## 1.1 Background and Operational Motivation

At 5:30 on a Monday morning at Dallas/Fort Worth International Airport, something remarkable and entirely predictable is about to happen. Within the next ninety minutes, thousands of passengers will converge on American Airlines' dedicated security checkpoints from every direction—curbside drops, rideshares, rental car shuttles, hotel vans. The checkpoints will absorb this wave and reach near-saturation before most of the departing flights have even begun boarding. By 8:00 a.m., the morning bank will be gone, the checkpoint lanes will quiet, and the Tuesday morning crew will look at the passenger counts and wonder what on earth happened.

This moment—the morning surge—is not a surprise. It is a structural feature of hub airport operations. Yet across the National Airspace System, security staffing decisions are frequently made from tables that were built years ago, calibrated against historical averages, and never updated to reflect the behavioral and operational shifts that followed the COVID-19 pandemic (Hopfe et al., 2024). The result is a chronic mismatch: too many lanes open during slow midday plateaus, too few during explosive morning banks and Sunday evening return cascades.

This mismatch is the problem this research addresses. The solution is not more checkpoints or more screeners—it is smarter, more adaptive forecasting.

As commercial air travel demand continues to outpace the capacity of landside airport terminal infrastructure, inefficient resource allocation at passenger security screening checkpoints has emerged as a critical operational bottleneck across the National Airspace System (Adacher et al., 2017). Traditionally, terminal passenger flow forecasting has relied on static, time-of-day planning tables or direct proportional scaling of published airline flight schedules. The post-pandemic era has exposed severe structural limitations in these conventional approaches: they assume away the very volatility they must plan for.

In modern airport operations, the most valuable predictive model is not necessarily the one with the lowest average forecast error under ideal conditions. It is the one that:

1. **Remains reliable during routine operations (Robustness):** Providing consistent, low-error baseline staffing recommendations during undisturbed flight banks and nominal departure schedules.
2. **Maintains stability and recovers rapidly during disruptions (Resilience):** Absorbing severe exogenous shocks—such as winter freeze events or summer convective ground delay programs—without generating catastrophic under-predictions or runaway queue backlogs that strand thousands of passengers.
3. **Transfers effectively across operational contexts (Generalizability):** Carrying its predictive logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific retraining that limits scalability.

This study systematically evaluates predictive modeling frameworks—spanning deterministic operational baselines, data-driven gradient-boosted decision-tree architectures, and sequential state-space hybrid models—for forecasting Transportation Security Administration (TSA) checkpoint throughput across routine, volatile, and disrupted demand regimes at the Top 25 U.S. commercial airfields from 2019 through 2025.

---

## 1.2 Significance of the Study

For decades, airport planners have answered the question "How many passengers will pass through security this hour?" by looking at the flight schedule. If forty flights are departing between 7:00 and 8:00 a.m., multiply by average seats, multiply by average load factor, and staff accordingly. It sounds reasonable. It is structurally wrong.

The problem is the hub disconnect. At a major connecting hub like Charlotte Douglas (CLT) or Dallas/Fort Worth (DFW), more than half of every departing passenger never touches landside security at all. They arrive on an inbound flight, walk airside from one concourse to another, and board their outbound flight without ever passing through a checkpoint. Treating raw scheduled departures as security demand inflates the estimate by more than 200% at some hub airports.

The second problem is timing. Passengers do not arrive at security when their flight departs—they arrive 90 to 120 minutes before pushback. A forecast built on contemporaneous flight counts is forecasting the wrong moment. It is like counting cars entering a highway at 7:00 a.m. to predict rush-hour congestion at 9:00 a.m. and calling them the same event.

This research advances a multidimensional, regime-aware evaluation framework that corrects both errors and introduces a third dimension that the existing literature largely ignores: what happens when the system breaks down? The findings demonstrate that integrating airline ticket coupon connecting ratios (BTS DB1B) with an empirical 90-to-120-minute passenger show-up curve reduces forecast error by approximately 14.2% compared to conventional schedule-based approaches—and that a regime-switched Two-Stage Hybrid model prevents the catastrophic under-prediction that pure machine learning architectures produce during severe weather delay cascades.

The result is actionable: a Regime-Switched Gated Inference Engine that airport operations centers can deploy across the Top 25 U.S. hub network, dynamically routing staffing decisions through computationally efficient gradient-boosted decision trees during routine operations and activating Kalman state-space feedback during high-disruption weather events.

---

## 1.3 Statement of the Problem

Airport passenger arrivals and queuing behaviors are inherently unpredictable, fluctuating dynamically based on departure bank structures, traveler booking characteristics, and air traffic control disruptions (Cheng et al., 2012; Dönmez et al., 2025). Existing models for managing passenger security screening demand frequently rely on static time-of-day curves or pre-pandemic operational assumptions that fail to reflect contemporary travel patterns (Ebert et al., 2021).

This mismatch between checkpoint lane allocation and fluctuating passenger demand creates chronic congestion at peak hours, excessive wait times, and inefficient staffing utilization. But the deeper problem is structural: the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond aggregate, undisturbed accuracy metrics.

Traditional evaluation asks only: *how close was the prediction on an average day?* It does not ask: *how badly did the model fail during the January 2023 winter freeze? How quickly did it recover? Could it be deployed at Philadelphia without retraining it on Philadelphia data?* These are the questions that actually matter for operational deployment—and they are the questions this research is designed to answer.

---

## 1.4 Purpose Statement

The primary objective of this research is to evaluate and compare predictive modeling frameworks—including deterministic time-series baselines, operational gradient-boosted decision-tree models, and sequential two-stage hybrid architectures—to optimize airport checkpoint capacity through data-driven operational decision tools rather than costly capital facility expansion.

By analyzing the empirical relationship between airside flight operations and landside TSA security screening throughput across the Top 25 U.S. commercial airfields from 2019 to 2025, this study assesses model performance against three primary operational criteria: **Robustness**, **Resilience**, and **Generalizability**. Rather than seeking a single, universally optimal model, this research determines which forecasting frameworks perform best under each operational demand state, providing airport authorities with the empirical justification needed to deploy regime-switched forecasting systems calibrated to operational context.

---

## 1.5 Research Question

Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts and hub topologies) as the primary operational evaluation metric?

---

## 1.6 Delimitations

This study is bounded as follows:

1. **Geographic Scope:** The contiguous United States, focusing on the Top 25 commercial airfields by FAA hub classification. The experimental cohort is narrowed to nine airports—Boston Logan (BOS), Dallas/Fort Worth (DFW), Detroit Metropolitan (DTW), Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles International (LAX), New York LaGuardia (LGA), Chicago O'Hare (ORD), and Philadelphia International (PHL)—representing American Airlines, Delta Air Lines, and United Airlines in a balanced $3 \times 3$ factorial design.
2. **Temporal Scope:** January 1, 2019 through December 31, 2025. Model training and evaluation focus on the post-pandemic operational equilibrium beginning May 1, 2022. The full calendar year 2025 is reserved as a strict out-of-time holdout window and was not observed during model development.
3. **Carrier Scope:** American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA). Southwest Airlines is excluded because its open-seating boarding structure and free-checked-bag policy create a fundamentally different passenger arrival timing profile—one that violates the distributional assumptions required for comparable modeling.
4. **Data Sources:** TSA FOIA hourly screening counts, BTS On-Time Flight Performance (Form 234), BTS Schedule T-100 Segment data, and BTS DB1B/DB1C 10% ticket coupon surveys.
5. **Evaluation Standards:** RMSE, MAE, MASE, the Disruption Error Multiplier ($R_{\text{MASE}}$), the Relative Transfer Ratio (RTR), Time-to-Recovery (TTR), and Diebold-Mariano statistical significance tests.

---

## 1.7 Limitations and Assumptions

Every study operates within constraints, and this one is no exception. Four limitations shape what the findings can and cannot claim:

1. **Staffing and Lane Configuration Opacity:** TSA does not publicly disclose exact Transportation Security Officer (TSO) shift allocations, active lane counts by 15-minute interval, or queue reconfigurations between PreCheck and standard screening. The methodology controls for this by aggregating lane-level throughput counts into terminal complex totals—a single, stable demand signal that maps cleanly to departing flight banks.

2. **Passenger Show-Up Curve Generalization:** Pre-security lead times are characterized using the empirical arrival distributions established in ACRP Report 40, discretized into three hourly weights (25% at one hour before departure, 55% at two hours, 20% at three hours). These weights represent the national average for legacy network carrier passengers and may vary marginally by day of week or seasonal corridor.

3. **Connecting Passenger Survey Stability:** BTS DB1B connecting ratios are estimated quarterly and applied monthly. The framework assumes these ratios remain stable within given carrier-terminal complexes across the modeling window—a reasonable assumption for the post-May 2022 steady-state regime but one that should be revisited if carrier hub strategy shifts materially.

4. **Operational Exogeneity:** Severe weather disruptions are captured through departure delay distributions and cancellation indicators from BTS Form 234. Internal TSA operational decisions—PreCheck lane activations, canine team deployments, screening technology upgrades—are treated as exogenous noise rather than modeled variables.

---

# CHAPTER II: REVIEW OF RELEVANT LITERATURE

## 2.1 Traditional Approaches and Operational Complexity

For most of commercial aviation's history, the question of how many passengers would show up at a security checkpoint was answered with a rule of thumb, a staffing table, or a gut check from an experienced operations manager. The academic literature eventually formalized these instincts into queuing theory and discrete event simulation—tools that brought mathematical rigor to terminal planning but introduced their own limitations when applied to the volatile, real-time demands of a modern hub airport (De Neufville & Odoni, 2014).

Airport landside subsystems—ticketing halls, security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security, the effect does not stay in security: congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### 2.1.1 Uncertainty, Batch Arrival Dynamics, and Flight Banks

The most fundamental challenge in airport passenger demand forecasting is that passengers do not arrive in a smooth, predictable stream. They arrive in concentrated batches, pulled forward by the flight bank schedules that define hub-and-spoke operations (Peterson et al., 1995; Cheng et al., 2012). Airlines deliberately cluster departures into 45-to-90-minute waves to maximize connecting passenger transfer opportunities—a practice that is economically rational for the carrier but creates severe demand surges that can saturate checkpoint capacity within minutes (Dönmez et al., 2025).

### 2.1.2 Classical Queuing Theory Foundations and Limitations

To translate unpredictable passenger movements into manageable system states, airport planners turned to queuing theory (Odoni, 1986; Wang, 2017). Early terminal capacity models used Poisson arrival distributions ($M/M/s$ or $M/G/s$ queues) to calculate expected queue lengths and waiting times against a target Level of Service (Araujo & Repolho, 2015).

The core problem with classical Poisson models is their central assumption: that the arrival rate $\lambda$ is constant over time. At a major hub airport, this assumption fails completely. Flight banks generate violent, non-linear fluctuations in arrival demand (Wang, 2018). Researchers subsequently adopted Non-Homogeneous Poisson Processes (NHPP) to let arrival rates vary by hour (Brunetta et al., 1999), but even NHPP assumes that individual arrivals are statistically independent. In reality, the passengers on the same inbound flight arrive as a correlated cluster—and at connecting hubs, a substantial fraction of scheduled departing passengers never enter the security queue at all (Guo et al., 2022).

---

## 2.2 Simulation Modeling and Real-Time Terminal Management

### 2.2.1 Discrete Event Simulation and Operational Limits

To escape the mathematical rigidities of analytical queuing equations, airport planners widely adopted Discrete Event Simulation (DES)—software environments that model individual passengers progressing through ticket scan, divestiture, metal detector, and item retrieval (Brown & Madhavan, 2011; Leone & Liu, 2011).

DES produces compelling visual outputs and has genuine value in terminal design. But it carries critical limitations for real-time operations management. First, small changes in baseline assumptions—secondary bag-search alarm rates, TSO divestiture coaching times—produce disproportionately large swings in modeled queue wait times, a calibration sensitivity that makes DES brittle (Brown & Madhavan, 2011). Second, simulating hundreds of thousands of individual passenger agents in real time, during an unfolding flight disruption, requires computational time that a live operations center simply does not have (Takakuwa & Oyama, 2004; Bießlich et al., 2014). Third, most DES models treat passengers as passive rule-followers—they do not reflect how a traveler actually responds to a push notification saying her 7:45 flight is delayed to 10:30 (Alodhaibi et al., 2017).

---

## 2.3 Time-Series Analysis and Data-Driven Predictive Frameworks

### 2.3.1 Statistical Time-Series Foundations

Seeking faster and more automatable forecasts, transportation planners turned to ARIMA and Seasonal ARIMA (SARIMA) models (Li et al., 2017). These econometric tools capture the dominant 24-hour and 168-hour rhythms of airport operations with mathematical elegance. When augmented with exogenous variables like scheduled seat capacity (SARIMAX), they offer transparent, interpretable baselines that airport planners can inspect and audit.

Their limitation is structural: linear autoregressive models assume fixed relationships between inputs and outputs. When a severe weather event breaks the normal relationship between scheduled departures and passenger arrivals—when flights are cancelled, delayed by five hours, or rerouted—SARIMA models keep forecasting as if the schedule is still intact.

### 2.3.2 Non-Linear Machine Learning and Sequential Neural Networks

The past decade has seen an explosion of machine learning applications in aviation, including Long Short-Term Memory (LSTM) networks, Gated Recurrent Units (GRU), and Gradient-Boosted Decision Trees (GBM) applied to passenger flow forecasting (Hopfe et al., 2024; Ribeiro et al., 2025). These models can capture complex, non-linear interactions across dozens of input features simultaneously—weather indices, search engine booking trends, real-time flight delay feeds.

Two operational challenges have limited their deployment at major airports. First, the interpretability barrier: when a deep neural network predicts a sudden 40% spike in security demand at 3:00 p.m. on a Tuesday, a Federal Security Director cannot determine whether the prediction reflects a genuine operational signal or a data artifact. Committing staffing based on an opaque model output is a decision most operations managers are unwilling to make (Adadi & Berrada, 2018; Viaña et al., 2024). Second, the over-specialization trap: highly parameterized neural networks memorize the specific gate layouts, local carrier bank structures, and idiosyncratic physical geometry of the airports they were trained on. Deploy them at an unfamiliar airport and accuracy collapses (Wang et al., 2025).

Recent multi-layer fusion architectures partially address these limitations by distributing feature extraction across specialized components—Convolutional Neural Networks for local pattern detection, Bidirectional LSTMs for temporal context, GRUs for computational efficiency (He et al., 2024)—but the fundamental interpretability and transfer challenges remain.

---

## 2.4 Hybrid Architectures and Causal Transparency

### 2.4.1 Integrating Queuing Principles with Decision-Tree Algorithms

The most promising direction in the literature combines the transparency of first-principles operational models with the adaptability of machine learning (Brun et al., 2025; Had et al., 2025). Rather than building an end-to-end black box, effective hybrid architectures establish a physically grounded baseline—using published flight schedules, empirical passenger show-up curves (ACRP Report 40), and airline connecting passenger survey data (BTS DB1B)—and then layer an interpretable Gradient-Boosted Decision Tree on top to correct residual demand shifts caused by real-time delays, gate holds, and cancellations (Ribeiro et al., 2025).

Decision trees offer a crucial operational advantage: their branching logic can be read as plain English. "If the departure delay on a 180-seat aircraft exceeds 45 minutes, reduce predicted security demand in the scheduled departure hour and increase it in the preceding two hours." An operations manager can audit that rule, agree or disagree with it, and override it with local knowledge. That auditability is what makes a model deployable in a safety-critical environment.

### 2.4.2 Glass-Box Models and Causal Transparency

Bayesian Networks (BNs) take interpretability further by mapping probabilistic dependencies in an explicit causal structure—showing not just what the model predicts, but why (Guo et al., 2025). Hybrid Queue-Based Bayesian Networks (HQBN) combine queuing principles with Bayesian reasoning to identify the physical causes of congestion within terminal processes, supporting more informed resource management decisions (Wu et al., 2014).

### 2.4.3 Dynamic Feedback and Real-Time State Tracking

The final critical capability for operational deployment is real-time adaptation. During severe weather events, flight schedules become unreliable indicators of future demand almost immediately—passengers who arrived expecting a 6:00 p.m. departure crowd the terminal even as the flight slips to 10:00 p.m., then to the next morning. Models that track live checkpoint throughput from the previous hour ($t-1$) and dynamically update their demand state—using techniques like Kalman filter state-space innovation—maintain forecast accuracy during disruptions where static models fail catastrophically (Ebert et al., 2021; Wu et al., 2024).

---

## 2.5 Post-Pandemic Operational Volatility and the Multi-Dimensional Evaluation Paradigm

Before March 2020, most airport forecasting models were evaluated on a single dimension: how accurately they predicted passenger volumes on a typical operational day. The COVID-19 pandemic demonstrated, with brutal clarity, that this standard was insufficient (Sun et al., 2022; Li et al., 2023).

When the pandemic collapsed air travel by 95% in weeks, restructured every terminal process, replaced in-person check-in with digital boarding passes, and introduced constant procedural uncertainty, even the most sophisticated forecasting models had no framework for what they were experiencing (Mota et al., 2021). A model optimized for "average day" accuracy was as useful in May 2020 as a weather forecast from the previous year.

The pandemic drove a fundamental paradigm shift in how airport operational models must be evaluated—one that this research formalizes across three dimensions:

1. **Robustness (Routine Operational Accuracy):** The consistency and precision of forecast models under nominal, clear-weather operating conditions. As digital and self-service processes introduced new sources of processing time variability, models must treat these as active variables rather than stable baselines (Lin, 2022).

2. **Resilience (Performance Under Severe Disruption):** The capacity of a forecasting framework to maintain error boundedness, resist demand collapse, and recover rapidly during Ground Delay Programs, winter blizzards, and summer convective ground stops. Terminals restructured around decentralized queues, curtailed staffing, and sudden physical capacity changes require models that can absorb—not break under—severe systemic shocks (Schultz et al., 2021; Kazda et al., 2022).

3. **Generalizability (Cross-Airport Portability):** The external validity of trained model structures when deployed across structurally diverse airport terminal complexes. The pandemic revealed that "similar" airports harbored drastically different structural vulnerabilities, and that evaluating throughput without contextualizing infrastructure changes leads to systematically flawed assumptions (Güner & Seçkin Codal, 2024; Tang et al., 2023).

By formalizing these three pillars as primary evaluation dimensions rather than secondary considerations, this study provides a domain-grounded framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.

---

# CHAPTER III: METHODOLOGY

## 3.1 Overview and Research Approach

The methodological challenge at the center of this research is deceptively simple to state and remarkably difficult to solve: *how do you forecast the number of passengers who will arrive at an airport security checkpoint in a given hour, given that the only reliable data you have in advance is a published flight schedule?*

The difficulty is that the flight schedule answers the wrong question. It tells you when flights are scheduled to depart, not when the passengers on those flights will show up at the checkpoint. It counts all the seats on every departing aircraft, including the seats occupied by connecting passengers who never touch landside security. And it treats severe weather disruptions as if they were simply fewer flights—when in reality they generate stranded passengers who crowd the terminal long after their original flights have come and gone.

This chapter details the methodological architecture developed to address each of these problems in sequence, building toward an empirically rigorous, leak-free modeling framework for airport passenger security screening demand.

The primary objective is to evaluate the comparative predictive accuracy and operational utility of three distinct forecasting paradigms:
1. **Deterministic Baselines ($M_0, M_1$):** Classical reference benchmarks relying on diurnal seasonal persistence ($y_{t-24}$) and contemporaneous scheduled flight departures.
2. **Probabilistic and Machine Learning Architectures ($M_2, M_3, M_4$):** Data-driven, non-linear formulations incorporating empirical passenger show-up distributions (ACRP Report 40), Gradient Boosted Count Regressors (LightGBM, Tweedie distribution), and multi-source operational feature pipelines.
3. **Sequential Two-Stage Hybrid Frameworks ($M_5$):** Integrated architectures combining time-series error correction, queuing dynamics, and Kalman state innovation feedback to dynamically correct queue backlogs during severe operational disruptions.

### 3.1.1 Core Research Hypotheses

The investigation evaluates model performance across three independent operational dimensions:
- **Dimension 1 – Robustness:** Consistency and precision under nominal flow conditions (departure delays < 15 min). Probabilistic ML models are hypothesized to excel.
- **Dimension 2 – Resilience:** Stability and recovery speed during severe exogenous shocks. Two-Stage Hybrid frameworks are hypothesized to demonstrate superior resilience ($R_{\text{MASE}} \le 1.30$; Time-to-Recovery ≤ 4.0 hours).
- **Dimension 3 – Generalizability:** Portability across divergent airport geometries without local retraining. Deterministic baselines and empirical show-up curve models are hypothesized to exhibit superior transferability (Transfer Degradation ≤ 15%).

### 3.1.2 Methodological Execution Phases

- **Phase 1:** Multi-source conformed ETL warehouse development.
- **Phase 2:** Purposive four-tiered filtering to isolate unconfounded carrier-checkpoint pairs.
- **Phase 3:** Coupled volatility clustering and 84-cell hierarchical stratification.
- **Phase 4:** Empirical model training, tuning, and strict out-of-time holdout evaluation.

---

## 3.2 Data Sources and Conformed ETL Pipeline

The analytical foundation draws on four federal aviation data feeds, each capturing a distinct dimension of the airside-to-landside demand chain, over the continuous seven-year period from January 1, 2019 to December 31, 2025.

### 3.2.1 TSA FOIA Security Screening Checkpoint Logs

The backbone of the study. Obtained via Freedom of Information Act (FOIA) disclosures, these records capture hourly passenger screening counts per physical lane at every commercial airport (19,500,286 raw records). The ETL pipeline downloads TSA Throughput files from the FOIA reading room, parses PDF-format records into tabular structure, cross-references GitHub repository data for completeness verification, standardizes timestamps to a uniform operational clock, normalizes airport codes and checkpoint identifiers, and loads the conformed output to the master warehouse. After cleaning: 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers over seven years.

### 3.2.2 BTS On-Time Performance (Form 234)

The primary source for flight-level departure timing, delay causes, and cancellations (45,777,091 raw records). A critical ETL design decision separates scheduled flight parameters (`CRSDepTime`, planned seats, carrier routing) from realized operational parameters (`DepTime`, `WheelsOff`, taxi-out), ensuring that pre-departure forecasting models can only consume information that was knowable before the event—preventing the data leakage that would render results operationally invalid. Post-ETL: 13,153,654 domestic departures across 17 reporting carriers.

### 3.2.3 BTS Form 41 Schedule T-100 Domestic Segment Data

Monthly carrier-route-equipment capacity data (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors. Load factors are matched to flight records by carrier-origin-month key and used to scale scheduled seat counts into estimated passenger counts—a critical step because a 180-seat aircraft operating at 92% load factor generates a fundamentally different checkpoint demand profile than the same aircraft at 61%.

### 3.2.4 BTS DB1B / DB1C Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed records). These surveys reveal the proportion of each airport's traffic that is connecting rather than originating—the single most important correction factor in the entire modeling pipeline. The connecting deflation formula that results:

$$\text{Demand}_{\text{originating}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$

turns a systematically overstated demand estimate into one that aligns with physical reality at the checkpoint.

---

## 3.3 Four-Tiered Purposive Filtering and Study Sample

To isolate the direct operational link between airside flight schedules and landside checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel designed to eliminate confounding from multi-carrier passenger mixing, unconstrained regional flow, and airline-specific boarding anomalies.

### 3.3.1 Macro Filter: Scale and Congestion Regimes

The filter begins at national scale. Commercial aviation passenger volumes follow a heavy-tailed power-law distribution in which the largest airports handle a disproportionate share of traffic. Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures.

The operational rationale is about queuing physics. In a multi-server queuing system, the traffic intensity—the ratio of incoming demand to processing capacity—determines whether queues actually form. At small regional airports, traffic intensity remains sparse and throughput simply mirrors arrivals without boundary friction. At Top 25 hub facilities, traffic intensity routinely approaches saturation during morning and evening departure banks, creating the non-linear queue delays and buffer depletion dynamics that make forecasting both difficult and operationally consequential.

### 3.3.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion

The second filter ensures that when comparing how American, Delta, and United passengers behave at security checkpoints, the comparison is fair. Candidate airfields were required to operate concurrent domestic mainline services by all three carriers, ensuring that when a winter storm or FAA Ground Delay Program disrupts operations, all three carriers in the study experience the same disruption simultaneously.

Southwest Airlines was excluded for a technically precise reason. Legacy network carrier passengers—on flights operated by American, Delta, and United—arrive at security following a consistent, unimodal distribution peaking approximately 105 minutes before departure. Southwest's open-seating boarding structure and two-free-checked-bags policy create a bimodal pattern: early arrivers competing for boarding position (approximately 135 minutes early) and baggage-free business travelers racing to the gate (approximately 65 minutes early). Mixing these behaviorally distinct passenger streams into the same model would violate the distributional consistency assumptions required for reliable parameter estimation.

### 3.3.3 Micro Filter: Carrier Checkpoint Isolation

Even within airports that operate all three legacy carriers, the analysis faces a mathematical problem: at shared terminals, all three airlines' flight banks arrive at roughly the same times. Their schedules are so correlated that it is statistically impossible to disentangle whose passengers are producing the checkpoint demand. This collinearity renders individual carrier demand contributions mathematically unidentifiable under any standard estimation approach.

The solution is to restrict analysis to carrier-exclusive screening environments—checkpoints where essentially all traffic belongs to a single carrier. This establishes the clean one-to-one mapping between an airline's departure schedule and the checkpoint throughput that serves its passengers.

### 3.3.4 Balanced Factorial Cohort: The 9-Airport Experimental Sample

Applying the four-tiered funnel across the Top 25 airfields yielded the **9-Airport Balanced Experimental Cohort**:
- **American Airlines (AA):** Dallas/Fort Worth (DFW), Chicago O'Hare (ORD), Philadelphia (PHL)
- **Delta Air Lines (DL):** Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)
- **United Airlines (UA):** Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles International (LAX)

This cohort achieves complete $3 \times 3$ factorial symmetry: three carriers, three dedicated terminal environments per carrier, spanning all four operational archetypes from the national clustering analysis. Two specific selections merit brief explanation. LaGuardia (LGA) was chosen over JFK because United permanently vacated JFK in October 2022, breaking the Meso continuity requirement. Philadelphia (PHL) was chosen over Salt Lake City (SLC) because SLC's single consolidated central checkpoint makes carrier isolation impossible.

---

## 3.4 Threats to Validity and Remediation Protocols

Every modeling decision involves a tradeoff, and intellectual honesty demands that those tradeoffs be named and addressed explicitly.

### 3.4.1 Connecting Passenger Bias (The Hub Disconnect)

The most significant threat. At major connecting hubs, treating scheduled departing seats as proxy for security demand inflates the estimate by over 200% at some airports. The remedy—multiplying seats by the local originating fraction derived from BTS DB1B quarterly surveys—reduces demand to the passengers who physically pass through the checkpoint.

### 3.4.2 Checkpoint Heterogeneity and Administrative Staffing Shifts

Individual screening lanes are subject to TSO shift rotations and dynamic reassignments between PreCheck and standard lanes that introduce noise unrelated to underlying passenger demand. The solution is to aggregate throughput across all lanes within a dedicated terminal complex, converting erratic lane-level counts into a single, stable demand signal that aligns with departing flight banks.

### 3.4.3 Overnight Checkpoint Closures versus Missing Data

Of the 6.4 million lane-hour records in the warehouse, 450,973 (2.31%) report zero passengers. These zeros are not sensor failures—98.6% occur during scheduled overnight checkpoint closures (00:00–03:59), when no flights are departing. Imputing non-zero values during these periods would be factually wrong. They are preserved as structural zeros and modeled accordingly.

### 3.4.4 Tactical versus Advance Cancellations

Flight cancellations are handled asymmetrically, reflecting operational timeline causality. Flights cancelled more than 24 hours before departure are removed from the demand pipeline because passengers had time to make alternative arrangements. Flights cancelled within two hours of departure are retained—because the passengers on those flights had already arrived at the airport and cleared security before learning their flight was cancelled.

### 3.4.5 Strict Information Causality

Perhaps the most consequential modeling constraint. Predictive models for staffing decisions must rely only on information that was available before the fact. Realized departure delays, actual pushback times, and wheels-off timestamps are all determined after passengers have already passed through security. Including them in a pre-departure staffing forecast would be cheating—producing a model that appears accurate in retrospect but would have no operational information to consume in real time. Only scheduled parameters are used as inputs; prior-hour delays ($t-1$) serve as causally valid proxies for current airside congestion.

---

## 3.5 Temporal Dynamics and Post-Pandemic Demarcation

### 3.5.1 The Physical Arrow of Time and Passenger Show-Up Lead Offset

Passengers do not arrive at security when their flight departs. They arrive before it departs—typically 90 to 120 minutes before pushback. This creates a fundamental phase-shift misspecification in any model that correlates checkpoint throughput directly with contemporaneous flight departures.

The physical logic is straightforward. Boarding doors close 15 minutes before scheduled departure. Passengers must be at the gate 35 to 50 minutes before that. Traversing a major concourse takes 12 to 25 minutes. Security screening takes 10 to 30 minutes under normal conditions. Working backward from pushback, the modal passenger arrives at the checkpoint approximately 92 minutes in advance—corresponding precisely to the peak of the empirical lognormal arrival distribution established in ACRP Report 40. This distribution is discretized into three hourly weights:

- 25% of a departing flight's passengers arrive at security one hour before departure
- 55% arrive two hours before departure (the peak hour)
- 20% arrive three hours before departure

Interacting this convolved demand estimate with monthly T-100 route load factors elevates baseline explanatory power from $R^2 = 0.20$ (contemporaneous departures alone) to $R^2 = 0.50$ before any temporal cyclical encodings are added.

### 3.5.2 Post-Pandemic Temporal Demarcation

The modeling framework is restricted to the post-pandemic operational equilibrium, anchored to **May 1, 2022**. This date was not chosen arbitrarily—it was verified through three independent statistical tests: CUSUM residual stabilization (cumulative forecast residuals stabilized within their control boundary beginning May 2022), Chow structural break testing (parameter constancy confirmed at $p = 0.18$ post-May 2022), and network-wide load factor verification (Top 25 national load factors stabilized at $84.6\% \pm 1.2\%$). The federal transportation mask mandate was also rescinded on April 18, 2022, marking the legal conclusion of pandemic-era travel restrictions.

The resulting data partitioning:
- *Training:* May 2022 – December 2023 (122,847 hourly complex observations)
- *Validation:* January 2024 – December 2024 (72,723 observations; full seasonal cycle for parameter selection)
- *Holdout Test:* January 2025 – December 2025 (72,053 hourly observations; never seen during model development)
- *Purge Buffer:* A 7-day quarantine embargo between each partition prevents multi-day delay cascades from contaminating evaluation periods.

---

## 3.6 Coupled Volatility Framework

The most counterintuitive empirical finding in this research comes from a simple test: regress daily TSA checkpoint throughput directly against daily scheduled flight volumes. The result—$R^2 \approx 2.50\%$—is essentially zero. Scheduled flight volumes explain almost nothing about how busy the checkpoint will be on a given day.

What does explain it is volatility. Not how many flights depart, but how chaotically they depart relative to how chaotically passengers arrive. When morning arrivals surge unpredictably at the same time departure delays ripple across the network, the checkpoint is in danger of failing catastrophically. When both are stable, it hums along.

Four daily metrics formalize this insight:

**Within-Day TSA Screening Volatility ($CV_{\text{TSA}, d}$):** The coefficient of variation of hourly passenger screening volume—how peaked versus smooth the arrival wave is on a given day.

$$CV_{\text{TSA}, d} = \frac{\sigma_{\text{hourly},\text{TSA}, d}}{\mu_{\text{hourly},\text{TSA}, d}}$$

**Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$):** The ratio of peak-hour screening demand to the daily average—how extreme the worst hour is.

$$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$

**Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$):** The standard deviation of departure delays across all uncancelled flights—how broadly the schedule is eroding.

$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

**The Coupled Volatility Index ($\text{CVI}_d$):** The joint product of landside arrival variation and airside delay dispersion—the single number that best characterizes systemic operational vulnerability on any given day.

$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

---

## 3.7 Hierarchical Cross-Classification Architecture

Using the coupled volatility metrics as a foundation, the methodology constructs an 84-cell operational taxonomy that organizes every hour of the study period into one of 84 precisely defined operational contexts:

$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \text{ seasons} \times 7 \text{ days} \times 3 \text{ diurnal blocks} = 84 \text{ cells})$$

**The four annual macro regimes** range from winter lull (Off-Peak) through spring ramps and summer shoulder (Mid-Peak) to summer severe weather (Peak) and national holiday travel corridors (Holiday). Each is defined by its empirical Coupled Volatility Index.

**The seven weekly operational cycles** are indexed by ISO 8601 day of week, isolating the distinct business outbound surge on Mondays, the stable midweek baseline on Tuesdays and Wednesdays, and the leisure return delay cascade on Sundays.

**The three diurnal regimes** are determined empirically for each day of the week via the Operational Turbulence Shock Index $T_{dow}(h)$—a normalized measure that takes the maximum of hourly passenger arrival variance and hourly flight delay dispersion:

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$

The most operationally important output of this framework is that the `3_PEAK` high-turbulence diurnal regime consists of two **non-consecutive** time windows: the Morning Bank Surge (05:00–08:00), driven by extreme passenger arrival variance, and the Evening Delay Cascade (14:00–22:00), driven by network-wide flight delay propagation. These two windows look completely different from a schedule perspective but are operationally equivalent in their demand on screening resources. Standard consecutive time-block categorization would miss this equivalence entirely.

---

## 3.8 Statistical Power and Sample Size Sufficiency

Academic rigor demands that every modeling cell have enough data to support reliable parameter estimation. With 84 cells, some operational combinations—particularly Holiday overnight hours—are inherently rare.

The audit results are reassuring: 83 of the 84 cells (98.8%) meet or exceed the minimum training threshold of 50 observations, with a median of 215 observations per cell. The single cell that falls short is Holiday Off-Peak Overnight (00:00–03:00, $N = 48$)—hours when airports are essentially closed and no forecasting decision is consequential. 65 of 84 cells (77.4%) have 100 or more training observations, ensuring well-powered gradient-boosted decision tree splits. 70 of 84 cells (83.3%) meet the Central Limit Theorem sample size threshold of 30 test observations; the remainder satisfy the requirements of non-parametric Wilcoxon and Diebold-Mariano tests.

---

## 3.9 Comparative Evaluation Framework and Model Architectures

### 3.9.1 Model Benchmark Suite ($M_0$ through $M_5$)

Six model architectures span the three forecasting paradigms:

- **$M_0$ (Diurnal Seasonal Naive):** The universal benchmark. Simply predicts that throughput in hour $t$ will equal throughput in the same hour yesterday ($y_t = y_{t-24}$). Any model worth deploying must outperform this.
- **$M_1$ (Contemporaneous SARIMAX):** Seasonal autoregressive integrated moving average with contemporaneous scheduled departures—the current industry standard.
- **$M_2$ (Empirical Show-Up Curve Regressor):** Linear model driven by distributed lag passenger arrival curves ($w_1 = 0.25, w_2 = 0.55, w_3 = 0.20$) aligned to ACRP Report 40.
- **$M_3$ (Operational Count Regressor):** Gradient boosted decision tree under zero-bounded count regression (Tweedie distribution, $p = 1.3$) combining passenger show-up curves with OTP delay and cancellation features.
- **$M_4$ (Full Tri-Modal Pipeline):** Gradient boosted regressor interacting show-up curves with T-100 load factors and carrier aircraft gauge.
- **$M_5$ (Sequential Two-Stage SARIMA-Tree Hybrid):** First-stage SARIMA capturing linear cyclical trends, cascaded into a secondary decision tree predicting residuals, equipped with recursive Kalman state innovation feedback. When live throughput $y_t$ exceeds the delayed flight schedule expectation, the innovation update ($e_t = y_t - C\hat{x}_{t|t-1}$) immediately forces the state estimator to correct—recognizing stranded passengers and maintaining low error multipliers even during severe disruptions.

### 3.9.2 Evaluation Metrics

Five metrics answer the three research questions:

- **MASE** (routine conditions) answers the robustness question: does this model outperform a naive 24-hour lag?
- **$R_{\text{MASE}} = \text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$** answers the resilience question: how much does accuracy degrade during severe weather events?
- **RTR $= \text{RMSE}_{\text{transfer}} / \text{RMSE}_{\text{in-sample}}$** answers the generalizability question: how much accuracy is lost when deploying without local retraining?
- **RMSE and MAE** provide scale-grounded absolute error context.
- **Diebold-Mariano tests** confirm that observed accuracy differences between models are statistically significant, not artifacts of sample variation.

---

# CHAPTER IV: RESULTS (EMPIRICAL FINDINGS)

## 4.1 Master Descriptive Statistics and Data Health Census

Seven years of airport operational data. Four federal data sources. Sixty-seven million raw records cleaned to forty-two million conformed observations. The numbers are large, but what matters is what they represent: a complete picture of how passengers flow through the Top 25 U.S. commercial airports from 2019 through 2025—before, during, and after the most disruptive event in commercial aviation history.

**Table 4.1: Master Post-ETL Multi-Source Data Foundation Census (Full Candidate Commercial Network)**

| Primary Data Feed | Raw Records | Post-ETL Records | Coverage |
| :--- | :---: | :---: | :--- |
| TSA FOIA Checkpoint Logs (Lane-Hour) | 19,500,286 | **6,434,732** | 25 Airfields, 955 Lanes, 2.70B Passengers |
| BTS On-Time Performance / Form 234 (Flight) | 45,777,091 | **13,153,654** | 17 Carriers, 13.15M Domestic Departures |
| BTS Form 41 / T-100 (Carrier-Route-Month) | 1,945,451 | **422,096** | 2.09B Departing Seats, 1.70B Passengers |
| BTS DB1B / DB1C Ticket Surveys (Coupon) | 12,910,384 | **22,051,557** | 62.16M Ticketed Travelers |
| **Combined Analytical Warehouse** | **67,222,828** | **42,062,039** | 100% Referential Integrity |

**Table 4.2: Post-ETL Master Summary Descriptive Statistics**

| Domain | Variable | N | Mean | Std Dev | 5th–95th Pct |
| :--- | :--- | :---: | :---: | :---: | :---: |
| TSA Throughput | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 444.84 | 10–1,316 |
| Flight Delays | Departure Delay (minutes) | 13,153,654 | 12.70 | 52.75 | -10 to 83 |
| Flight Delays | Significant Delay Rate (≥ 15 min) | 13,153,654 | 20.12% | — | — |
| Flight Operations | Cancellation Rate | 13,153,654 | 2.03% | — | — |
| Flight Operations | Runway Taxi-Out Time (min) | 13,153,654 | 18.84 | 10.03 | 8–39 |
| Route Capacity | Route Load Factor (%) | 422,096 | 81.21% | 11.80% | 58.4–94.2% |
| Passenger Surveys | Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 11.74% | 35.7–70.1% |

Three data quality observations deserve specific mention.

**Spatial Key Recovery:** Upstream TSA FOIA records contained 35,809 entries with missing or malformed airport identifiers. An automated checkpoint fingerprinting algorithm—matching historical checkpoint naming signatures to conformed dimension keys—recovered 7,489 records. The remaining 22,190 unresolvable records were mapped to a surrogate key rather than silently dropped. Without this remediation, approximately 9.71 million passengers would have been aggregated into an unidentified "phantom airport" that would severely distort national baseline models.

**Structural Zeros:** Of the 6.4 million lane-hour records, 450,973 (2.31%) report zero passengers. Cross-referencing with airport operational schedules confirmed that 98.6% of these zeros occur during scheduled overnight checkpoint closures (00:00–03:59). These are preserved as genuine operational zeros rather than imputed with artificial values.

**Cancellation Asymmetry:** Of 13.15 million domestic departures tracked, 267,019 (2.03%) were cancelled. The operationally critical distinction: flights cancelled more than 24 hours out were removed from the demand pipeline; flights cancelled within two hours were retained, because by then the passengers were already in the terminal.

---

## 4.2 The Four-Tiered Purposive Filtering Pipeline

### 4.2.1 Macro Filter

Top 25 airfields: 67.2% of national domestic flight movements. Peak-hour checkpoint congestion ($\rho(t) \to 1.0$) during morning and evening departure banks.

### 4.2.2 Meso Filter

Concurrent AA, Delta, and United operations provide airspace shock invariance. Southwest excluded due to bimodal arrival timing ($\mu_1 \approx 135$ min; $\mu_2 \approx 65$ min).

### 4.2.3 Micro Filter

Carrier-exclusive checkpoints eliminate schedule collinearity ($\kappa < 25$), establishing a clean one-to-one mapping between carrier flight banks and checkpoint throughput.

### 4.2.4 The 9-Airport Experimental Cohort

**BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL** — three carriers, three airports each, spanning all four operational archetypes.

---

## 4.3 Empirical Operational Clusters and Systemic Trends

Unsupervised machine learning—PCA coupled with K-Means and Ward's Hierarchical Clustering—revealed four distinct operational archetypes across the Top 25 airfields.

| Cluster | Airfields | Mean TSA | Connecting Ratio | Mean Delay | Character |
| :--- | :--- | :-: | :-: | :-: | :--- |
| **0: Mega-Connecting Gateways** | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 56.1% | 15.6 min | High volume, high connecting, delay-exposed |
| **1: High-Density O&D Focus** | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 48.4% | 15.0 min | Moderate volume, high originating fraction |
| **2: High-Reliability Fortress Hubs** | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 54.1% | 11.6 min | High connecting, exceptional delay reliability |
| **3: Congested Coastal Originators** | EWR, JFK, LGA | 85.6M | 37.4% | 16.1 min | Low connecting, severe chronic delay burden |

### 4.3.1 The Hub Disconnect in Practice

Charlotte (CLT) is one of the clearest illustrations in the dataset. Total scheduled departing seat capacity: over 34 million passengers annually. Total TSA checkpoint throughput: 28.2 million. The BTS DB1C data resolves the discrepancy: 76.0% of CLT's traffic is connecting. Over 26 million passengers transfer between concourses airside. They represent real airline revenue—but zero security screening demand. Failing to apply the connecting passenger deflator would cause any checkpoint staffing model to overestimate demand by more than 200%.

### 4.3.2 Delay Transmission Divergence

The contrast between Cluster 2 and Cluster 3 airports is striking. Detroit (DTW), Minneapolis (MSP), Salt Lake City (SLC), and Philadelphia (PHL) collectively handle immense connecting volume with exceptional operational fluidity—mean delay just 11.6 minutes, taxi-out 18.7 minutes. Meanwhile, Newark (EWR), JFK, and LaGuardia (LGA) suffer chronic, structural delay burdens—mean delay 16.1 minutes, taxi-out 24.3 minutes—despite operating smaller, regional aircraft gauge. The cause is airspace: slot caps and runway geometry constraints at New York metro airports create congestion that passenger volume cannot explain.

### 4.3.3 Annual Coupled Volatility Regimes

**Table 4.3: Annual Seasonal Volatility Regimes (Top 25 Airfields, May 2022 – December 2025)**

| Regime | Days (Share) | Mean Daily TSA | TSA Arrival CV | Delay Dispersion | Coupled Volatility Index | Cancel Rate |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| `1_OFF_PEAK` (Winter/Autumn) | 500 (37.3%) | 1,123,386 | 0.605 | 46.09 min | **27.85** | 0.89% |
| `2_MID_PEAK` (Spring/Shoulder) | 426 (31.8%) | 1,187,095 | 0.589 | 55.06 min | **32.38** | 1.36% |
| `3_PEAK` (Summer Convective) | 224 (16.7%) | 1,305,968 | 0.576 | 68.43 min | **39.36** | 3.16% |
| `4_HOLIDAY` (Holiday Corridors) | 191 (14.2%) | 1,215,636 | 0.597 | 55.78 min | **33.07** | 1.82% |

The numbers tell a coherent operational story. Summer flight delay dispersion ($\sigma_{\text{Delay}} = 68.43$ min) is 48.5% higher than winter ($46.09$ min). The Coupled Volatility Index escalates by 41.3% from winter lull to summer peak. Flight cancellation rates more than triple from 0.89% in winter to 3.16% in summer. These are not statistical artifacts—they reflect the known physics of convective thunderstorm season in the continental United States.

### 4.3.4 Day-of-Week Cyclical Dynamics

**Table 4.4a: Day-of-Week Volatility Dynamics**

| Day | Operational Archetype | Mean Daily TSA | TSA CV | Delay Dispersion | CVI |
| :---: | :--- | :---: | :---: | :---: | :---: |
| Monday | Outbound Business Surge | 1,246,150 | **0.604** | 56.56 min | **34.00** |
| Tuesday | Midweek Reset (Lowest Turbulence) | 1,076,625 | 0.601 | **50.09 min** | **29.99** |
| Wednesday | Minimum Volatility Baseline | 1,123,368 | 0.594 | **49.27 min** | **29.13** |
| Thursday | Corporate Outbound & Early Weekend Ramp | 1,254,744 | 0.589 | 54.65 min | 31.96 |
| Friday | Business & Leisure Surge | 1,241,359 | 0.592 | 55.58 min | 32.77 |
| Saturday | Volume Trough & Fleet Repositioning | 1,089,699 | 0.602 | 54.16 min | 32.45 |
| Sunday | Leisure Return & Delay Cascade | 1,279,017 | 0.577 | **58.07 min** | **33.40** |

Tuesdays and Wednesdays are operationally the most stable days of the week—the lowest delay dispersion, the lowest Coupled Volatility Index, the most predictable screening demand. Mondays carry the highest intraday screening volatility ($CV = 0.604$), driven by concentrated early-morning business traveler surges. Sundays deliver the highest network-wide delay cascades, the highest mean departure delay (17.78 min), and the worst delay dispersion ($\sigma = 58.07$ min)—a predictable consequence of weekend leisure travel volume exhausting aircraft turn buffers across the national airspace.

### 4.3.5 Diurnal Non-Consecutive Dual Peaks

The most operationally consequential clustering result is the structure of the diurnal Peak regime. Rather than one continuous busy period from morning through evening, the `3_PEAK` category identifies two distinct, non-consecutive turbulence windows:

- **The Morning Bank Surge (05:00–08:00):** Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr). Schedule adherence is high; flights are on time; the challenge is pure volume—thousands of passengers converging simultaneously.
- **The Evening Delay Cascade (14:00–22:00):** Driven by network-wide flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min). Individual departures may be sparse and delayed, but actual passengers remain in the terminal—stranded, rerouted, or waiting for gate assignments that keep shifting.

These two windows require the same operational response—more screening capacity—but for completely different reasons. The morning surge is a volume problem. The evening cascade is a dwell problem. A forecasting model that treats them identically because they both have high CVI values will staff correctly for entirely different reasons.

---

## 4.4 Temporal Demarcation: Post-Pandemic Regime Selection

The choice of when the "post-pandemic" period begins is not a philosophical question—it is an empirical one that directly shapes how much training data is available and which operational disruptions the models learn from.

| Criteria | Candidate A (Jan 1, 2023) | **Candidate B (May 1, 2022 — Selected)** |
| :--- | :--- | :--- |
| Statistical Method | Rolling Welch's t-test | CUSUM stabilization + Chow structural break |
| Training Span | 24 months | **32 months** |
| Captures Winter Storm Elliott (Dec 2022)? | ❌ No | ✅ Yes |
| Captures Summer 2023 Convective Season? | ✅ Yes | ✅ Yes |
| Training Observations (9-Airport Cohort) | ~80k | **122,847** |

The May 2022 demarcation is confirmed by three independent tests. CUSUM residuals stabilize within control boundaries beginning May 2022. The Chow structural break test fails to reject parameter constancy ($p = 0.18$) beginning May 2022. Network-wide load factors reach $84.6\% \pm 1.2\%$ beginning May 2022—the steady state required for reliable model training.

---

## 4.5 Econometric Validation of Carrier Checkpoint Isolation

Before building any forecasting models, the study validates the foundational assumption: that carrier-exclusive checkpoints actually isolate individual carrier demand. Three econometric tests confirm they do.

| Test | Result | Implication |
| :--- | :--- | :--- |
| Volume Conservation ($\rho = \text{TSA}/\text{Est}$) | $\rho = 1.00 \pm 0.04$ ($p < 0.001$) | Terminal volumes match carrier originating passengers exactly |
| Zero-Flight Intercept ($\beta_0$) | $\beta_0 = 12.4$ pax/hr ($p = 0.40$) | Zero scheduled flights = zero checkpoint demand (no structural phantom queue) |
| Cross-Carrier Independence ($\beta_\text{other}$) | $\beta = 0.002$ ($p = 0.62$) | Non-tenant carrier flights add zero demand to exclusive checkpoints |

Using carrier-filtered flight data achieves $R^2 = 0.708$–$0.774$ for checkpoint demand prediction. Using total pooled airport departures: $R^2 < 0.420$. The improvement is statistically decisive ($p < 0.0001$).

A final test compares physically separate terminal buildings (BOS, DTW, LGA, ORD, EWR) against walkway-connected terminals (LAX, DFW, IAH, PHL). Kolmogorov-Smirnov: $D = 0.032, p = 0.28$. Connected terminals behave identically to air-gapped ones—baggage re-check requirements and biometric CAT boarding passes prevent passengers from crossing to adjacent carrier facilities.

---

## 4.6 Feature Engineering and Passenger Show-Up Curve Estimation

The lead-lag analysis tells the story of the physical arrow of time in data:

| Flight Feature | $R^2$ | Pearson $r$ | Regression Slope |
| :--- | :---: | :---: | :---: |
| Contemporaneous Departures ($t$) | 0.1988 | 0.4459 | 38.42 pax/flight |
| Lead 1 hr before ($t+1$) | 0.3723 | 0.6102 | 62.15 pax/flight |
| **Lead 2 hrs before ($t+2$) — PEAK** | **0.4054** | **0.6367** | **74.98 pax/flight** |
| Lead 3 hrs before ($t+3$) | 0.3299 | 0.5744 | 51.20 pax/flight |
| Full Show-Up Curve (Convolved) | 0.4878 | 0.6985 | 74.98 pax/flight |
| **Show-Up Curve × T-100 Load Factor** | **0.4985** | **0.7061** | **90.56 pax/flight** |

A contemporaneous schedule model explains less than 20% of checkpoint variance. Adding the two-hour lead window more than doubles explanatory power. Incorporating the full lognormal show-up distribution lifts it further. Multiplying by monthly load factors takes it to $R^2 = 0.50$—before any temporal cyclical features are added. Each step has a clear physical rationale; none is a statistical black box.

---

## 4.7 Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)

The 2025 holdout evaluation is the study's central empirical judgment. Models trained through December 2023, validated through December 2024, and never permitted to see a single 2025 observation during development were evaluated against the full 12-month 2025 calendar—72,053 hourly complex observations representing 215,562 facility-level screening hours.

**Table 4.7: Master Model Benchmark Matrix (2025 Out-of-Time Holdout)**

| Paradigm | ID | Architecture | Val $R^2$ | Test $R^2$ | RMSE | MAE | MASE |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| Deterministic Baseline | M0 | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1377.3 | 939.8 | 1.000 |
| Deterministic Baseline | M1 | Contemporaneous Sched SARIMAX | 0.4338 | 0.4375 | 1393.8 | 1042.6 | 1.109 |
| Probabilistic / ML | M2 | Passenger Show-Up Curve Only | 0.5443 | 0.5862 | 1195.5 | 856.2 | 0.911 |
| Probabilistic / ML | M3 | Show-Up Curve + OTP Delays | 0.5450 | 0.5880 | 1192.9 | 855.1 | 0.910 |
| Probabilistic / ML | M4 | Full Tri-Modal (Load Factor Scaled) | 0.5798 | 0.5771 | 1208.6 | 856.3 | 0.911 |
| **Two-Stage Hybrid** | **M5** | **Sequential SARIMA-Tree Hybrid** | **0.6644** | **0.6270** | **1135.0** | **795.0** | **0.846** |

Several findings stand out immediately. The contemporaneous schedule model (M1) performs *worse* than simply repeating yesterday's hourly throughput (M0), confirming that contemporaneous flight counts are actively misleading as demand predictors. The passenger show-up curve models (M2, M3) deliver a meaningful accuracy improvement with a clear physical mechanism. The Sequential Hybrid (M5) achieves the highest accuracy across every metric—but the most interesting findings emerge when the data is stratified by volatility regime.

### 4.7.1 Performance Stratification Across Volatility Regimes

During routine, low-volatility operating conditions, the Gradient Boosted Count Regressor (M3) and the Sequential Hybrid (M5) perform almost identically—both achieving MASE around 0.60 to 0.62. In calm, predictable operational environments, the additional complexity of the Kalman state-space tracking in M5 adds only marginal benefit.

During high-volatility summer convective events, the divergence becomes dramatic. Extreme convective storms delay flights by three to five hours. A pure machine learning model sees that the flights scheduled for 18:00 have been delayed to 22:00 and predicts that the 16:00 checkpoint will be empty. It is not empty—the passengers arrived based on their original tickets and are now stranded. M3 degrades to MASE = 1.025 under these conditions. M5, tracking prior-hour congestion feedback in real time, maintains MASE = 0.737. The difference between these two numbers represents tens of thousands of stranded passengers either served or abandoned by a checkpoint staffing decision.

---

*END OF DRAFT C — Chapters I through IV*
