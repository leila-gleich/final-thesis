# DRAFT B — TECHNICALLY EXPANDED / COMMITTEE-READY
### *Gleich, L. (2026). Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: TSA Checkpoint Throughput Forecasting and Airside-Landside Queue Dynamics. Master of Science in Aeronautics, Embry-Riddle Aeronautical University.*

---

> **DRAFT NOTES — DRAFT B PHILOSOPHY**
> Draft B is the most technically rigorous version, aimed at satisfying a committee or defense audience. It expands the Chapter 1 hypothesis section into three formally stated sub-hypotheses, adds a definitions section, strengthens Chapter 2 with more differentiated literature coverage (glass-box models, stochastic optimization, COVID impact section), tightens Chapter 3 to lead with the data pipeline before the filtering funnel (matching the Updated Structure Recommendation), and adds the PCA loading matrix and sample size audit table directly into Chapter 4 for completeness. Chapter 1 and Chapter 3 share structurally parallel heading levels.

---

# CHAPTER I: INTRODUCTION

## 1.1 Background and Operational Motivation

As commercial air travel demand continues to outpace the capacity of landside airport terminal infrastructure, inefficient resource allocation at passenger security screening checkpoints has emerged as a critical operational bottleneck across the National Airspace System (Adacher et al., 2017). Airport terminal operators and federal security authorities face a persistent dual challenge: sustaining stringent screening standards while minimizing passenger queue delays—goals that are inherently in tension under stochastic and volatile demand conditions. Traditionally, terminal passenger flow forecasting has relied on static time-of-day planning tables or direct proportional scaling of published airline flight schedules. However, the systemic demand shocks and operational disruptions of the post-pandemic era have exposed severe structural limitations in these conventional forecasting approaches (Hopfe et al., 2024).

Conventional forecast evaluation in transportation planning has historically emphasized aggregate error metrics—such as Root Mean Squared Error (RMSE) or Mean Absolute Percentage Error (MAPE)—computed under routine, undisturbed operating conditions. Yet in volatile airport operating environments, an evaluation framework built solely on nominal-day accuracy is insufficient for operational deployment. A forecasting model that achieves low average error during calm, clear-weather periods may fail catastrophically during severe convective weather ground delay programs, unexpected terminal lane closures, or sudden schedule cascades driven by upstream network failures.

In modern airport operations, the most operationally valuable predictive model is not necessarily the one with the lowest marginal error under ideal conditions, but the model that satisfies three complementary operational properties:

1. **Robustness (Routine Operational Reliability):** Providing consistent, low-error baseline staffing recommendations during undisturbed flight banks and nominal demand conditions.
2. **Resilience (Disruption Stability and Recovery):** Absorbing severe exogenous shocks—such as winter freeze events or summer convective ground delay programs—without generating false demand collapses, runaway queue backlogs, or recovery times that exceed staffing reallocation windows.
3. **Generalizability (Spatial Transferability):** Porting its structural predictive logic across divergent airport terminal layouts and airline hub network topologies without requiring extensive, site-specific historical retraining that would limit scalability across the national airspace.

This study systematically evaluates predictive modeling frameworks—spanning deterministic operational baselines, data-driven gradient-boosted decision-tree architectures, and sequential state-space hybrid models—for forecasting Transportation Security Administration (TSA) checkpoint throughput across routine, volatile, and disrupted demand regimes at the Top 25 U.S. commercial airfields from 2019 through 2025.

---

## 1.2 Significance of the Study

This research contributes to both transportation science theory and practical airport operations by advancing a multidimensional, regime-aware evaluation framework that moves beyond single-metric accuracy benchmarking. While traditional airport planning literature treats passenger demand as a static reflection of published departures, this study demonstrates that passenger arrivals at security screening follow complex behavioral show-up curves (ACRP Report 40, *Airport Passenger Terminal Planning and Design*) that are fundamentally decoupled from contemporaneous flight departure timestamps by a 90-to-120-minute physical lead time offset.

By identifying the conditions under which distinct predictive modeling paradigms maintain or lose operational fidelity, this research provides airport Federal Security Directors (FSDs), airline hub operations managers, and FAA planners with actionable, empirically grounded decision tools. Specifically, the findings demonstrate that integrating airline ticket coupon connecting ratios (BTS DB1B) with real-time flight delay feedback reduces checkpoint forecast error by approximately 14.2% compared to contemporaneous schedule-based benchmarks, and that a regime-switched Two-Stage Hybrid model prevents the severe under-prediction characteristic of pure machine learning architectures during severe weather delay cascades.

The strategic implication is the deployment of a **Regime-Switched Gated Inference Engine**: a computationally efficient framework that routes staffing inferences through gradient-boosted decision trees during routine operations and activates Kalman state-space feedback during high-disruption periods, enabling a single unified architecture to satisfy all three operational criteria simultaneously.

---

## 1.3 Statement of the Problem

Airport passenger arrivals and queuing behaviors are inherently stochastic, fluctuating dynamically based on departure bank structures, traveler booking characteristics, and air traffic control disruptions (Cheng et al., 2012; Dönmez et al., 2025). Existing models for managing passenger security screening demand frequently rely on static time-of-day curves or pre-pandemic operational assumptions that fail to reflect contemporary travel patterns (Ebert et al., 2021). This mismatch between checkpoint lane allocation and fluctuating passenger demand contributes to chronic congestion at peak hours, excessive passenger wait times, and inefficient staffing utilization.

Critically, the aviation sector currently lacks a dynamic framework for evaluating predictive models beyond aggregate, undisturbed accuracy metrics. Because modern airport operations cannot be assumed to follow static, deterministic flight schedules—particularly given post-pandemic demand volatility, extreme weather frequency, and ongoing airline schedule restructuring—the absence of a multidimensional evaluation methodology leaves airport authorities at risk of deploying decision tools that collapse during sudden operational disruptions or fail when transferred across unfamiliar terminal complexes. Static models also fail to account for the structural fact that at major hub airports, over half of scheduled departing passengers transfer airside and never pass through landside security checkpoints, rendering raw seat-count-based demand estimates grossly inaccurate.

---

## 1.4 Purpose Statement

The primary objective of this research is to evaluate and compare predictive modeling frameworks—including deterministic time-series baselines, operational gradient-boosted decision-tree models, and sequential two-stage hybrid architectures—to optimize airport checkpoint capacity through data-driven operational decision tools rather than costly capital facility expansion.

By analyzing the empirical relationship between airside flight operations and landside TSA security screening throughput across the Top 25 U.S. commercial airfields from 2019 to 2025, this study assesses model performance against three primary operational criteria: **Robustness**, **Resilience**, and **Generalizability**. Rather than seeking a single, universally optimal model, this research determines which forecasting frameworks perform best under each operational demand state, providing airport authorities with the empirical justification needed to deploy regime-switched forecasting systems calibrated to operational context.

---

## 1.5 Research Questions and Hypotheses

### 1.5.1 Research Question

Which predictive modeling frameworks are most effective for forecasting airport passenger security screening throughput when prioritizing **robustness** (routine operational accuracy), **resilience** (stability under convective weather and delay disruptions), or **generalizability** (cross-airport portability across terminal layouts and hub topologies) as the primary operational evaluation metric?

### 1.5.2 Formal Research Hypotheses

**Overarching Hypothesis ($H_1$):** No single predictive modeling architecture will prove uniformly superior across all three evaluation dimensions (Robustness, Resilience, and Generalizability). Rather, asymmetric performance advantages will emerge across paradigms, necessitating a regime-switched deployment strategy:

- **$H_{1a}$ (Robustness):** Probabilistic and Machine Learning models (M3, M4) will demonstrate superior routine operational accuracy during nominal conditions (departure delays < 15 min), achieving $\text{MASE}_{\text{routine}} < 0.70$ by learning complex non-linear calendar, diurnal, and passenger show-up interactions.
- **$H_{1b}$ (Resilience):** Two-Stage Hybrid frameworks (M5) will demonstrate superior resilience during systemic disruptions ($R_{\text{MASE}} \le 1.30$; Time-to-Recovery ≤ 4.0 hours) through closed-loop Kalman queue innovation corrections that detect stranded passengers before staffing collapses.
- **$H_{1c}$ (Generalizability):** Structurally parameterized deterministic baselines (M1) and empirical show-up curve models (M2) will exhibit superior spatial generalizability (Transfer Degradation ≤ 15%) by abstracting away airport-specific facility over-specialization that causes over-parameterized neural networks to degrade upon transfer.

---

## 1.6 Delimitations

1. **Geographic Scope:** This study evaluates commercial air traffic and TSA security screening operations within the contiguous United States, focusing on the Top 25 commercial airfields categorized under FAA hub classifications. The experimental cohort is narrowed to nine airports—BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, and PHL—representing American Airlines, Delta Air Lines, and United Airlines in a balanced $3 \times 3$ factorial design.
2. **Temporal Scope:** The longitudinal dataset spans January 1, 2019 through December 31, 2025. Model training and evaluation are focused on the verified post-pandemic operational regime beginning May 1, 2022. The full calendar year 2025 is reserved as a strict out-of-time holdout evaluation window.
3. **Carrier Scope:** American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA). Southwest Airlines is excluded due to its bimodal passenger arrival profile.
4. **Data Sources:** TSA FOIA hourly screening counts, BTS On-Time Performance (Form 234), BTS Schedule T-100 Segment data, and BTS DB1B/DB1C 10% ticket coupon surveys.
5. **Evaluation Standards:** RMSE, MAE, MASE, Disruption Error Multiplier ($R_{\text{MASE}}$), Relative Transfer Ratio (RTR), Time-to-Recovery (TTR), and Diebold-Mariano hypothesis tests.

---

## 1.7 Limitations and Assumptions

1. **Staffing and Lane Configuration Opacity:** Exact TSO shift allocations, active lane counts per 15-minute interval, and manual queue reconfigurations are not publicly available. The methodology controls for this by aggregating lane-level counts into terminal complex throughput totals.
2. **Passenger Show-Up Curve Generalization:** Pre-security lead times are characterized using ACRP Report 40 empirical arrival distributions with discrete hourly weights (25% at $t+1$; 55% at $t+2$; 20% at $t+3$). These weights represent the national average for legacy network carrier passengers and may vary marginally by day of week or seasonal regime.
3. **Connecting Passenger Survey Stability:** BTS DB1B connecting ratios are computed quarterly and applied monthly. The framework assumes quarterly connecting ratios remain stable within given carrier-terminal complexes across the modeling window.
4. **Operational Exogeneity:** Severe weather disruptions are captured through departure delay distributions and cancellation indicators from BTS Form 234. Internal TSA operational decisions (e.g., PreCheck lane activations, canine team deployments) are not modeled explicitly.
5. **Non-Traveler Exit Negligibility:** Gate pass escorts and aborted-boarding passengers are assumed to represent < 1% of peak bank screening volume, consistent with federal gate pass restrictions under 49 CFR § 1544.205.

---

## 1.8 Definition of Key Terms

- **Robustness:** The consistency and precision of a forecast model under nominal clear-weather operating conditions (departure delays < 15 min), measured by $\text{MASE}_{\text{routine}}$.
- **Resilience:** The capacity of a forecasting framework to maintain error boundedness and recover rapidly from severe exogenous disruptions, measured by the Disruption Error Multiplier ($R_{\text{MASE}}$) and Time-to-Recovery (TTR).
- **Generalizability:** The external validity and portability of a trained model when deployed across structurally diverse airport terminal complexes without site-specific historical recalibration, measured by the Relative Transfer Ratio (RTR).
- **Coupled Volatility Index (CVI):** The daily product of within-day TSA arrival coefficient of variation ($CV_{\text{TSA}}$) and flight departure delay dispersion ($\sigma_{\text{Delay}}$), representing joint operational vulnerability.
- **The Hub Disconnect:** The structural phenomenon whereby connecting passengers at hub airports transfer airside and never pass through landside security checkpoints, causing raw seat-based demand estimates to overpredict actual screening volume by up to 200%.
- **MASE (Mean Absolute Scaled Error):** A scale-independent accuracy metric computed relative to the naive 24-hour diurnal persistence baseline; values below 1.0 indicate outperformance.
- **RTR (Relative Transfer Ratio):** The ratio of out-of-sample RMSE after direct cross-airport deployment to in-sample RMSE; values near 1.0 indicate high spatial portability.
- **Traffic Intensity ($\rho$):** The ratio of passenger arrival rate to total screening lane service capacity ($\rho = \lambda / (c \cdot \mu)$); values approaching 1.0 indicate near-saturation queuing conditions.

---

# CHAPTER II: REVIEW OF RELEVANT LITERATURE

## 2.1 Traditional Approaches and Operational Complexity

As commercial aviation navigates a period of sustained traffic expansion that threatens to outpace the physical limitations of existing terminal infrastructure, the impracticality of continuous brick-and-mortar expansion has shifted operational focus toward software-driven, data-informed terminal capacity management (De Neufville & Odoni, 2014). Airport landside subsystems—specifically ticketing halls, passenger security screening checkpoints, and departure gate hold-rooms—operate as tightly coupled queuing networks. When demand outstrips processing capacity at security screening, congestion ripples backward into check-in areas and forward into departure concourses, inducing ground delays and passenger misconnections across the National Airspace System (Adacher et al., 2017).

### 2.1.1 Uncertainty, Batch Arrival Dynamics, and Flight Banks

A fundamental challenge in airport passenger demand forecasting is that passenger arrivals do not follow a uniform, steady stream. Rather, arrivals are characterized by high variability and concentrated waves induced by airline flight bank scheduling (Peterson et al., 1995; Cheng et al., 2012). Airlines operating hub-and-spoke networks intentionally cluster flight departures into narrow 45-to-90-minute waves to maximize connecting passenger transfer opportunities, generating severe demand surges that saturate screening lane capacity far more rapidly than smooth, uncoordinated traffic streams (Dönmez et al., 2025).

### 2.1.2 Classical Queuing Theory Foundations and Limitations

Traditional airport planning has relied upon queuing theory (Odoni, 1986; Wang, 2017). Early terminal capacity models utilized Poisson arrival distributions ($M/M/s$ or $M/G/s$ queues) to calculate queue lengths and average waiting times relative to a target Level of Service (Araujo & Repolho, 2015). However, classical Poisson models assume a constant, time-invariant arrival rate ($\lambda$), which fails in commercial airports where flight banks generate severe non-linear fluctuations (Wang, 2018). While researchers subsequently adopted Non-Homogeneous Poisson Processes (NHPP) (Brunetta et al., 1999), NHPP models still assume independent arrivals. In operational reality, passengers on the same flight are strongly correlated, and hub connecting passengers never enter landside queues at all (Guo et al., 2022)—limitations that restrict the utility of analytical queuing equations for volatile contemporary terminal operations (Adeke, 2018).

---

## 2.2 Simulation Modeling and Real-Time Terminal Management

### 2.2.1 Discrete Event Simulation and Operational Limits

Airport planners widely adopted Discrete Event Simulation (DES) to overcome the mathematical rigidities of analytical queuing equations (Brown & Madhavan, 2011; Leone & Liu, 2011). Despite high visual fidelity, DES models exhibit critical limitations in real-time operational deployment: calibration sensitivity to baseline assumptions (Brown & Madhavan, 2011); computational latency that renders them impractical for tactical lane reallocation (Takakuwa & Oyama, 2004; Bießlich et al., 2014); and passive traveler assumptions that fail to reflect how passengers dynamically adjust arrival timing in response to mobile flight delay notifications (Alodhaibi et al., 2017).

---

## 2.3 Time-Series Analysis and Data-Driven Predictive Frameworks

### 2.3.1 Statistical Time-Series Foundations

To achieve faster, automated forecasts, transportation planners turned to ARIMA and Seasonal ARIMA (SARIMA) formulations (Li et al., 2017). When augmented with exogenous variables (SARIMAX), they provide computationally lightweight, transparent baseline estimates that capture dominant diurnal and day-of-week rhythms. However, linear time-series formulations struggle during operational structural breaks because they assume fixed autoregressive relationships that cannot accommodate sudden delay cascades.

### 2.3.2 Non-Linear Machine Learning and Sequential Neural Networks

Recent aviation literature has explored Long Short-Term Memory (LSTM) networks, Gated Recurrent Units (GRU), and Gradient-Boosted Decision Trees (GBM) to model complex non-linear relationships (Hopfe et al., 2024; Ribeiro et al., 2025). While capable of approximating complex multi-source interactions, these architectures introduce significant operational challenges: the interpretability barrier that prevents FSDs from validating sudden volume spike predictions (Adadi & Berrada, 2018; Viaña et al., 2024), and facility-specific over-specialization where highly parameterized networks memorize terminal-specific gate layouts and degrade upon transfer (Wang et al., 2025).

Multi-layered fusion architectures extend these foundations. For example, the Fusion Intelligence Network Model proposed by He et al. (2024) combines Convolutional Neural Networks for local feature extraction, Bidirectional LSTMs for temporal context, and GRUs for computational efficiency—improving stability under rapidly changing traffic conditions while maintaining dependency on data quality and calibration.

---

## 2.4 Hybrid Architectures and Causal Transparency

### 2.4.1 Integrating Queuing Principles with Decision-Tree Algorithms

To resolve the tension between transparency and non-linear flexibility, transportation researchers have converged toward hybrid architectures (Brun et al., 2025; Had et al., 2025). Effective hybrid designs combine first-principles operational baselines—using established flight schedules, empirical passenger show-up curves (ACRP Report 40), and connecting passenger survey ratios (BTS DB1B)—with transparent decision-rule adjustments via Gradient-Boosted Decision Trees that predict residual demand shifts caused by real-time flight delays and cancellations (Ribeiro et al., 2025). Decision trees offer a critical operational advantage: their branching structure can be directly mapped to auditable operational rules that airport managers can validate before committing staffing resources.

### 2.4.2 Glass-Box Models and Causal Transparency

Multi-layered models possess considerable predictive power yet remain difficult to interpret (Wang et al., 2025). Bayesian Networks (BNs) offer a potential solution by representing probabilistic dependencies in a transparent, causal structure. Guo et al. (2025) extend this framework by integrating BNs with the Best-Worst Method to quantify interdependencies among terminal resilience factors. Similarly, Hybrid Queue-Based Bayesian Networks (HQBN) combine queuing theory with probabilistic reasoning to identify the causes of congestion within terminal processes, supporting more informed and explainable decision-making (Wu et al., 2014).

### 2.4.3 Dynamic Feedback and Real-Time State Tracking

During severe disruptions, static schedules become obsolete. Incorporating recursive error-correction feedback (such as Kalman filtering or sequential residual tracking) allows forecasting models to monitor live checkpoint throughput ($t-1$) and dynamically adjust queue demand states in real time, preventing the massive under-prediction typical of static flight schedule models (Ebert et al., 2021; Wu et al., 2024). Nonlinear Autoregressive with Exogenous Input (NARX) models complement this approach by incorporating external variables like weather, improving forecast transparency compared to purely deep learning architectures (Anupam & Lawal, 2024).

### 2.4.4 Stochastic Optimization

Metaheuristic methods—such as Particle Swarm Optimization with Back Propagation (PSO-BP)—are widely used to tune neural network parameters on non-linear variables like baggage flow and waiting times (Wu, 2024). Likelihood-free inference methods can estimate system behavior during unpredictable disruptions (Ebert et al., 2021), while ensemble methods such as Random Forests improve robustness by aggregating multiple decision pathways (Xia et al., 2020).

---

## 2.5 Post-Pandemic Operational Volatility and the Multi-Dimensional Evaluation Paradigm

While predictive modeling literature has historically focused on maximizing point accuracy under nominal conditions, the unprecedented disruptions of the COVID-19 pandemic demonstrated that single-metric evaluations are fundamentally inadequate (Sun et al., 2022; Li et al., 2023). The pandemic fundamentally altered terminal operations, restructuring passenger handling away from speed-centric throughput toward health-risk minimization (Mota et al., 2021). Even highly sophisticated models struggled to forecast flow accurately amidst profound procedural and spatial changes, demonstrating that raw predictive accuracy could no longer serve as the sole benchmark for model efficacy (Li et al., 2023).

In volatile modern aviation environments, predictive models must be evaluated across three distinct, complementary operational dimensions:

1. **Robustness (Routine Operational Accuracy):** The consistency and precision of forecast models under nominal, clear-weather operating conditions with on-time flight operations. The rapid post-pandemic adoption of digital and self-service processes introduced highly volatile processing times, requiring models to treat dynamic processing rates as active variables rather than stable baselines (Lin, 2022).
2. **Resilience (Performance Under Severe Disruption):** The capacity of a forecasting framework to maintain error boundedness, resist demand collapse, and recover rapidly during Ground Delay Programs, severe winter blizzards, and summer convective ground stops. This requires models that can absorb decentralized queue structures, curtailed staffing, and sudden physical capacity constraints (Schultz et al., 2021; Kazda et al., 2022).
3. **Generalizability (Cross-Airport Portability):** The external validity and portability of trained model structures when deployed across structurally diverse terminal complexes. The pandemic revealed that ostensibly "similar" airports harbored drastically different structural vulnerabilities, and that evaluating raw throughput without contextualizing infrastructure changes leads to flawed assumptions (Güner & Seçkin Codal, 2024; Tang et al., 2023).

By formalizing these three operational pillars, this study provides a comprehensive, domain-grounded evaluation framework that bridges the gap between theoretical machine learning and defensible, deployable airport operations planning.

---

# CHAPTER III: METHODOLOGY

## 3.1 Overview and Research Approach

This chapter details the methodological architecture and empirical framework developed to model, forecast, and evaluate passenger security screening throughput at commercial airports. Traditional airport passenger flow modeling has historically relied on static time-of-day profile tables or direct deterministic scaling of published airline flight schedules. However, airport terminal subsystems constitute a tightly coupled, stochastic queuing network subject to severe non-linear queuing friction and schedule-driven volatility (De Neufville & Odoni, 2014).

The primary objective is to evaluate the comparative predictive accuracy and operational utility of three distinct forecasting paradigms:
1. **Deterministic Baselines ($M_0, M_1$):** Classical reference benchmarks relying on diurnal seasonal persistence ($y_{t-24}$) and contemporaneous scheduled flight departures.
2. **Probabilistic and Machine Learning Architectures ($M_2, M_3, M_4$):** Data-driven, non-linear formulations incorporating empirical passenger show-up arrival distributions (ACRP Report 40), Gradient Boosted Count Regressors (LightGBM, Tweedie distribution, $p = 1.3$), and multi-source operational feature pipelines incorporating flight delays and cancellations.
3. **Sequential Two-Stage Hybrid Frameworks ($M_5$):** Integrated architectures combining queuing dynamics, time-series error correction, and Kalman state-space innovation feedback to dynamically correct queue backlogs during severe operational disruptions.

### 3.1.1 Core Research Hypotheses

- **Dimension 1 – Robustness:** Consistency and precision under nominal flow conditions (DepDelay < 15 min). Probabilistic ML models are hypothesized to excel at capturing continuous baseline variance.
- **Dimension 2 – Resilience:** Stability, error boundedness, and speed of recovery during severe exogenous shocks. Two-Stage Hybrid frameworks are hypothesized to demonstrate superior resilience ($R_{\text{MASE}} \le 1.30$; TTR ≤ 4.0 hours) through closed-loop queue innovation corrections.
- **Dimension 3 – Generalizability:** Portability of trained model structures across divergent airport geometries. Deterministic baselines and empirical show-up curve models are hypothesized to exhibit superior spatial transferability (Transfer Degradation ≤ 15%).

### 3.1.2 Methodological Execution Phases

- **Phase 1:** Multi-Source Conformed ETL Warehouse Development across four federal aviation data feeds.
- **Phase 2:** Purposive Four-Tiered Filtering and Experimental Cohort Isolation.
- **Phase 3:** Coupled Volatility Clustering and Hierarchical Stratification (84-cell tensor).
- **Phase 4:** Empirical Model Training, Tuning, and Out-of-Time Holdout Evaluation.

---

## 3.2 Data Sources and Conformed ETL Pipeline

The analytical data foundation integrates four primary federal aviation data feeds over the continuous seven-year baseline from January 1, 2019 to December 31, 2025.

### 3.2.1 TSA FOIA Security Screening Checkpoint Logs

Obtained via Freedom of Information Act (FOIA) disclosures, this feed records hourly passenger screening counts per physical lane across all commercial airports (19,500,286 raw records). The three-phase ETL pipeline (Extract → Transform → Load) encompasses: downloading TSA Throughput files from the FOIA reading room; parsing PDF records into tabular format; cross-referencing with GitHub repository data for completeness; standardizing timestamps to a uniform operational clock; normalizing airport codes and checkpoint identifiers; and loading the conformed output to the master data warehouse. Following conformed extraction, the warehouse preserves 6,434,732 lane-hour records across 955 screening lanes at the Top 25 airfields, tracking 2.70 billion screened passengers.

### 3.2.2 BTS On-Time Performance (Form 234)

This feed records individual domestic flight movements (45,777,091 raw records). The ETL pipeline separately retains scheduled flights (`CRSDepTime`, planned seats, carrier routing) and actual flights (`DepTime`, `WheelsOff`, taxi-out), enforcing strict information causality by ensuring that pre-departure predictive models consume only planned parameters. The post-ETL warehouse retains 13,153,654 domestic departures across 17 reporting carriers.

### 3.2.3 BTS Form 41 Schedule T-100 Domestic Segment Data

Form 41 captures monthly carrier-route-equipment capacity (1,945,451 raw records; 422,096 cleaned observations), providing departing seats, transported passengers, and route load factors. Load factors are applied to scale scheduled seat counts into estimated passenger counts, and matched to flight records by carrier-origin-month key.

### 3.2.4 BTS DB1B / DB1C Origin and Destination Ticket Surveys

A 10% randomized sample of airline ticket itineraries (12,910,384 raw coupons; 22,051,557 conformed coupon records), utilized to extract quarterly connecting passenger ratios across airport pairs. These ratios directly support the connecting passenger deflation formula:

$$\text{Demand}_{\text{originating}, t} = \sum_{f \in \mathcal{F}_t} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}_{\text{airport}})$$

---

## 3.3 Four-Tiered Purposive Filtering and Study Sample

To isolate the direct operational link connecting airside flight schedules to landside checkpoint demand, candidate airfields were filtered through a four-tiered purposive funnel.

### 3.3.1 Macro Filter: Scale and Congestion Regimes

Restricting the initial sampling universe to the Top 25 U.S. commercial airfields captures 67.2% of nationwide domestic flight departures under a power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$). Traffic intensity $\rho(t) = \lambda(t) / (c(t) \cdot \mu)$ approaches saturation ($\rho(t) \to 1.0$) at Top 25 hubs during morning and evening departure banks, creating the non-linear queue dynamics necessary to train and validate congestion-aware models.

### 3.3.2 Meso Filter: Airspace Shock Invariance and Southwest Exclusion

Candidate environments were required to operate concurrent domestic mainline services by American Airlines (AA), Delta Air Lines (DL), and United Airlines (UA), neutralizing common weather and ATC delay confounders. Southwest Airlines (WN) was systematically excluded because its open-seating boarding structure and two-free-checked-bags policy generate a bimodal passenger arrival mixture:

$$\tau_{\text{WN}} \sim w_1 \mathcal{N}(\mu_1, \sigma_1^2) + (1 - w_1) \mathcal{N}(\mu_2, \sigma_2^2)$$

where $\mu_1 \approx 135$ minutes (boarding position maximizers) and $\mu_2 \approx 65$ minutes (carry-on-only business travelers), violating the show-up distribution homogeneity assumption required for carrier-comparable modeling.

### 3.3.3 Micro Filter: Carrier Checkpoint Isolation

In shared terminal complexes, multiple airlines feed shared screening lanes. Because hub carriers synchronize departure banks, flight schedules are collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), creating an ill-conditioned Gram matrix ($\kappa(\mathbf{X}^\top\mathbf{X}) \gg 10^4$) under which individual airline demand contributions are structurally unidentifiable. Restricting analysis to carrier-exclusive environments enforces $P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$, reducing the condition number to $\kappa < 25$.

### 3.3.4 Balanced Factorial Cohort: The 9-Airport Experimental Sample

The four-tiered funnel yielded the **9-Airport Balanced Experimental Cohort**:
- **American Airlines (AA):** Dallas/Fort Worth (DFW), Chicago O'Hare (ORD), Philadelphia (PHL)
- **Delta Air Lines (DL):** Detroit Metropolitan (DTW), New York LaGuardia (LGA), Boston Logan (BOS)
- **United Airlines (UA):** Newark Liberty (EWR), Houston Intercontinental (IAH), Los Angeles International (LAX)

This cohort achieves complete $3 \times 3$ factorial symmetry spanning all four operational archetypes from the national clustering analysis. LGA was selected over JFK because United permanently vacated JFK in October 2022; PHL was selected over SLC because SLC's consolidated central checkpoint prevents carrier isolation.

---

## 3.4 Threats to Validity and Remediation Protocols

### 3.4.1 Connecting Passenger Bias (The Hub Disconnect)

In hub-and-spoke operations, up to 76% of passengers transfer airside and never pass through landside security checkpoints. Treating scheduled flight departures as raw security demand grossly inflates demand estimates. Flight seat capacity is deflated using empirical connecting fractions derived from BTS DB1B surveys (above formula).

### 3.4.2 Checkpoint Heterogeneity and Administrative Staffing Shifts

Individual lane evaluation introduces administrative variance from TSO shift rotations and dynamic lane reassignments. Hourly throughput is aggregated across all lanes within a dedicated terminal complex ($Y_{kt} = \sum_{l \in \mathcal{L}_k} y_{k,l,t}$), transforming noisy lane-level counts into a robust aggregate demand signal.

### 3.4.3 Overnight Checkpoint Closures versus Missing Data

Exactly 450,973 records (2.31%) report zero throughput. Cross-referencing confirmed that 98.6% of zero intervals occur during scheduled overnight closures (00:00–03:59). These are preserved as structural zeros modeled using zero-bounded count regression (Tweedie distribution, $p = 1.3$) rather than naive imputation.

### 3.4.4 Tactical versus Advance Cancellations

Advance cancellations (>24 hours pre-departure) are purged from departing seat capacity. Tactical cancellations (<2 hours pre-departure) are retained in the passenger arrival curve because affected passengers have already crossed security checkpoints prior to the carrier issuing the cancellation notice.

### 3.4.5 Strict Information Causality and Zero Lookahead Leakage

Predictive models consume only scheduled, pre-departure parameters known prior to departure (`CRSDepTime`, scheduled seats, historical rolling reliability). Realized operational timestamps (`DepTime`, `WheelsOff`, `TaxiOut`) are never ingested into pre-departure prediction pipelines; prior-hour delays ($t-1$) serve as causally valid proxies for airside apron congestion.

---

## 3.5 Temporal Dynamics and Post-Pandemic Demarcation

### 3.5.1 The Physical Arrow of Time and Lead-Lag Offset

A fundamental modeling requirement is replacing naive contemporaneous scheduling ($t \leftrightarrow t$) with a forward-looking 90-to-120-minute lead time window. The unidirectional physical pipeline of airport operations is:

```
Curbside → TSA Screening → Airside Transit → Boarding Closes → Pushback
[T–120 m]   [T–100 m]       [T–70 m]          [T–15 m]         [T = 0]
```

Contemporaneous scheduled flights explain less than 20% of checkpoint throughput variance ($R^2 < 0.20$); explanatory power peaks at Lead $t+2$ ($R^2 = 0.4054$), confirming ACRP Report 40 empirical standards.

### 3.5.2 Empirical Passenger Show-Up Curve (Lognormal Arrival Density Kernel)

Passenger arrival lead time $\tau$ follows a lognormal distribution:

$$\tau \sim \text{Lognormal}(\mu \approx 4.65, \sigma \approx 0.35)$$

yielding mode $\tau^* \approx 92.5$ minutes. Discrete hourly convolution weights:

$$w_1 = 0.25, \quad w_2 = 0.55, \quad w_3 = 0.20$$

Interacting convolved demand with BTS T-100 monthly load factors elevates baseline explanatory power to $R^2 = 0.4985$ prior to introducing temporal cyclical encodings.

### 3.5.3 Post-Pandemic Temporal Demarcation

The contemporary operational equilibrium begins **May 1, 2022**, validated by:
1. Federal mask mandate rescission (April 18, 2022).
2. CUSUM residual stabilization ($|S_t| \le 4.2 < 5.0$) post-May 2022.
3. Network-wide load factor stabilization at $84.6\% \pm 1.2\%$.
4. Chow structural break test fails to reject parameter constancy ($p = 0.18$) beginning May 2022.

Partitioning design:
- *Training:* May 2022 – December 2023 (20 months; 122,847 hourly observations)
- *Validation:* January 2024 – December 2024 (12 months; 72,723 observations)
- *Holdout Test:* January 2025 – December 2025 (12 months; 72,053 hourly observations; 215,562 facility-level screening hours)
- *Purge Buffer:* 7-day embargo between periods

---

## 3.6 Coupled Volatility Framework

Traditional terminal planning models categorize time using static calendar bins. However, static scheduled flight volumes correlate poorly with operational breakdown ($R^2 \approx 2.50\%$). Systemic queue breakdown is driven by coupled volatility and variance mismatch.

### 3.6.1 Within-Day TSA Screening Volatility ($CV_{\text{TSA}, d}$)

$$CV_{\text{TSA}, d} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (\text{TSA}_{d,h} - \bar{\text{TSA}}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} \text{TSA}_{d,h}}$$

### 3.6.2 Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)

$$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$

### 3.6.3 Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)

$$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2}$$

### 3.6.4 The Coupled Volatility Index ($\text{CVI}_d$)

$$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$

---

## 3.7 Hierarchical Cross-Classification Architecture

The methodology constructs an 84-cell cross-classification tensor:

$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \times 7 \times 3 = 84 \text{ cells})$$

**Annual Macro Regimes ($\mathcal{S}$):**
- `1_OFF_PEAK`: Winter Lull & Mid-Autumn Shoulder
- `2_MID_PEAK`: Spring Ramps & Late-Summer Shoulder
- `3_PEAK`: Summer Severe Weather & Convective Surge (June–August)
- `4_HOLIDAY`: National Holiday Travel Corridors

**Weekly Operational Cycles ($\mathcal{D}$):** ISO 8601 Monday through Sunday.

**Diurnal Regimes ($\mathcal{H}$):** Three non-consecutive categories per DOW derived from the Operational Turbulence Shock Index:

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$

1D K-Means clustering ($k = 3$) on $T_{dow}(h)$ yields: `1_OFF_PEAK` ($T < 0.35$); `2_MID_PEAK` ($0.35 \le T < 0.75$); `3_PEAK` ($T \ge 0.75$).

The `3_PEAK` regime captures empirically non-consecutive dual peaks: the **Morning Bank Surge (05:00–08:00)** driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr), and the **Evening Delay Cascade (14:00–22:00)** driven by network-wide flight delay dispersion ($\sigma_{\text{Delay}} > 63.4$ min).

---

## 3.8 Statistical Power and Sample Size Sufficiency

To prevent small-sample estimator degradation across all 84 cells:

- **Training Partition (32 Months):** May 2022 – December 2024; 122,847 training + 72,723 validation observations.
- **Holdout Partition (12 Months):** January 2025 – December 2025; 72,053 hourly complex observations.
- **$N_{\text{train}} \ge 50$ (Minimum Viable):** 83 of 84 cells (98.8%); median $N_{\text{train}} = 215$.
- **$N_{\text{train}} \ge 100$ (Well-Powered):** 65 of 84 cells (77.4%).
- **$N_{\text{test}} \ge 30$ (CLT Asymptotic Validity):** 70 of 84 cells (83.3%); remaining cells satisfy non-parametric test requirements.

---

## 3.9 Comparative Evaluation Framework and Model Architectures

### 3.9.1 Model Benchmark Suite ($M_0$ through $M_5$)

- **$M_0$:** Diurnal Seasonal Naive ($y_t = y_{t-24}$) — universal baseline benchmark.
- **$M_1$:** Contemporaneous Sched SARIMAX — linear autoregressive with scheduled departures.
- **$M_2$:** Empirical Show-Up Curve Regressor — distributed lag passenger arrival curves ($w_1, w_2, w_3$) per ACRP Report 40.
- **$M_3$:** Operational Count Regressor — LightGBM under Tweedie loss ($p = 1.3$) combining show-up curves with OTP delay/cancellation features.
- **$M_4$:** Full Tri-Modal Pipeline — LightGBM interacting show-up curves with T-100 load factors and carrier aircraft gauge.
- **$M_5$:** Sequential Two-Stage SARIMA-Tree Hybrid — first-stage SARIMA capturing linear cyclical trends cascaded into a secondary decision tree, equipped with recursive Kalman state innovation feedback:
  $$e_t = y_t - C\hat{x}_{t|t-1}$$

### 3.9.2 Evaluation Metrics

| Metric | Formula | Operational Interpretation |
| :--- | :--- | :--- |
| **RMSE** | $\sqrt{\frac{1}{N}\sum(y_t - \hat{y}_t)^2}$ | Penalizes large peak-hour errors |
| **MAE** | $\frac{1}{N}\sum\|y_t - \hat{y}_t\|$ | Average absolute volume deviation |
| **MASE** | $\frac{\frac{1}{N}\sum\|y_t - \hat{y}_t\|}{\frac{1}{N-24}\sum\|y_t - y_{t-24}\|}$ | < 1.0 beats naive persistence |
| **$R_{\text{MASE}}$** | $\frac{\text{MASE}_{\text{shock}}}{\text{MASE}_{\text{routine}}}$ | ≤ 1.30 denotes resilience |
| **RTR** | $\frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$ | Near 1.0 = high portability |
| **Diebold-Mariano** | Pairwise forecast error differentials | Statistical significance of accuracy gains |

---

# CHAPTER IV: RESULTS (EMPIRICAL FINDINGS)

## 4.1 Master Descriptive Statistics and Data Health Census

To construct an empirically rigorous and leak-free modeling architecture for airport passenger security screening demand, this study synthesized multi-source operational data covering the continuous seven-year period from January 1, 2019 to December 31, 2025. The initial upstream repository encompassed 67.22 million raw fact records across four federal aviation data feeds.

Following conformed extraction, cleansing, and relational joining across standardized dimension keys, the nationwide post-ETL analytical warehouse contains **42,062,039 cleaned records** across all 25 candidate commercial airfields.

**Table 4.1: Master Post-ETL Multi-Source Data Foundation Census**

| Primary Data Feed | Raw Rows | Post-ETL Rows | Conformance Status |
| :--- | :---: | :---: | :--- |
| TSA FOIA Checkpoint Logs (Checkpoint-Lane-Hour) | 19,500,286 | 6,434,732 | 100% Non-Null; 2.70 Billion Passengers Screened |
| BTS On-Time Performance / Form 234 (Flight Departure) | 45,777,091 | 13,153,654 | 100% Non-Null; 17 Carriers; 13.15M Domestic Departures |
| BTS Form 41 / T-100 (Carrier-Route-Month) | 1,945,451 | 422,096 | 2.09 Billion Departing Seats; 1.70 Billion Pax |
| BTS DB1B / DB1C Ticket Surveys (Coupon Itinerary) | 12,910,384 | 22,051,557 | 62.16 Million Ticketed Travelers |
| **Combined Analytical Warehouse** | **67,222,828** | **42,062,039** | 100% Referential Integrity |

**Table 4.2: Post-ETL Summary Descriptive Statistics**

| Domain | Variable | N | Mean | Std Dev | 5th Pct | 95th Pct |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| TSA Throughput | Hourly Lane Throughput (pax/hr) | 6,434,732 | 420.17 | 444.84 | 10.00 | 1,316.00 |
| Flight Delays | Departure Delay (min) | 13,153,654 | 12.70 | 52.75 | -10.00 | 83.00 |
| Flight Delays | Significant Delay Rate (≥ 15 min) | 13,153,654 | 20.12% | 40.09% | 0.00% | 100.00% |
| Flight Operations | Cancellation Rate | 13,153,654 | 2.03% | 14.09% | 0.00% | 0.00% |
| Flight Operations | Taxi-Out Time (min) | 13,153,654 | 18.84 | 10.03 | 8.00 | 39.00 |
| Route Capacity | Available Seats per Route-Month | 422,096 | 4,962.40 | 7,019.66 | 120 | 19,200 |
| Route Capacity | Route Load Factor (%) | 422,096 | 81.21% | 11.80% | 58.40% | 94.20% |
| Passenger Surveys | Connecting Passenger Fraction (%) | 22,051,557 | 51.39% | 11.74% | 35.69% | 70.09% |

### 4.1.1 Spatial Key Resolution

Upstream TSA FOIA records exhibited 35,809 records with missing or malformed airport identifiers. An automated checkpoint fingerprinting algorithm recovered 7,489 records by matching historical naming signatures. The remaining 22,190 unresolvable records were mapped to a surrogate key (airportId = 0), preventing approximately 9.71 million passengers from aggregating into phantom airport records.

### 4.1.2 Nighttime Checkpoint Closures

Exactly 450,973 records (2.31%) report zero passengers. Cross-referencing confirmed 98.6% of zeros occur during scheduled overnight closures (00:00–03:59) and are preserved as structural zeros under Tweedie regression.

### 4.1.3 Flight Delays and Cancellations

Mean departure delay: 12.70 minutes. 20.12% of flights experienced delays ≥ 15 minutes. Flight cancellations: 2.03% (267,019 flights). Advance cancellations (>24 hours) were purged from demand capacity; tactical cancellations (<2 hours) were retained because affected passengers had already cleared security.

---

## 4.2 The Four-Tiered Purposive Filtering Pipeline

### 4.2.1 Macro Filter

Top 25 airfields capture 67.2% of national domestic flight movements. Top 25 hubs reach $\rho(t) \to 1.0$ during peak departure banks, creating the non-linear queuing dynamics required for model training.

### 4.2.2 Meso Filter

Concurrent AA, Delta, and United operations enforce airspace shock invariance. Southwest is excluded due to its bimodal arrival mixture ($\mu_1 \approx 135$ min; $\mu_2 \approx 65$ min).

### 4.2.3 Micro Filter

Carrier-exclusive checkpoints eliminate multi-carrier schedule collinearity ($\kappa < 25$), mapping carrier flight banks directly to landside checkpoint throughput.

### 4.2.4 9-Airport Experimental Cohort

**BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL** — complete $3 \times 3$ factorial balance across three legacy carriers and four operational clusters.

---

## 4.3 Empirical Operational Clusters and Systemic Trends

Unsupervised machine learning (PCA coupled with K-Means and Ward's Hierarchical Clustering) revealed four operational archetypes.

**PCA Component Loading Matrix:**

| Feature | PC1 (Scale & Congestion, 33.8%) | PC2 (Gauge vs. Vulnerability, 25.5%) | PC3 (Connecting Dominance, 17.7%) |
| :--- | :---: | :---: | :---: |
| log_actual_tsa | 0.364 | 0.357 | -0.001 |
| log_estimated_tsa | 0.432 | 0.199 | -0.054 |
| connecting_ratio | -0.151 | 0.108 | 0.583 |
| avg_aircraft_seats | 0.105 | 0.519 | 0.187 |
| route_load_factor | 0.308 | 0.410 | 0.003 |
| avg_dep_delay | 0.368 | -0.321 | 0.363 |
| depDel15_rate | 0.355 | -0.183 | 0.500 |
| cancel_rate | 0.275 | -0.466 | 0.011 |
| avg_taxi_out | 0.347 | -0.172 | -0.295 |
| **Cumulative Variance** | **33.8%** | **59.3%** | **77.0%** |

**Cluster Profiles:**

| Cluster | Count | Member Airfields | Mean TSA | Conn. Ratio | Mean Delay |
| :--- | :-: | :--- | :-: | :-: | :-: |
| **0: Mega-Connecting Gateways** | 8 | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 56.1% | 15.6 min |
| **1: High-Density O&D Focus** | 6 | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 48.4% | 15.0 min |
| **2: High-Reliability Fortress Hubs** | 8 | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 54.1% | 11.6 min |
| **3: Congested Coastal Originators** | 3 | EWR, JFK, LGA | 85.6M | 37.4% | 16.1 min |

### 4.3.1 The Hub Disconnect

At Charlotte (CLT), total departing seats exceeded 34 million, yet TSA checkpoint throughput was only 28.2 million. The BTS DB1C 76.0% connecting ratio resolves this: over 26 million passengers transferred airside. Failing to apply the connecting passenger deflator causes demand overestimation by over 200%.

### 4.3.2 Delay Transmission Divergence

Cluster 2 (DTW, MSP, SLC, PHL): mean delay = 11.6 min; taxi-out = 18.7 min. Cluster 3 (EWR, JFK, LGA): mean delay = 16.1 min; taxi-out = 24.3 min despite smaller gauge—demonstrating congestion driven by airspace slot caps rather than passenger volume.

### 4.3.3 Annual Coupled Volatility Regimes

**Table 4.3: Master Annual Seasonal Volatility Regimes**

| Regime | Days | Mean Daily TSA | TSA CV | $\sigma_{\text{Delay}}$ | CVI | Cancel Rate |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| `1_OFF_PEAK` (Winter/Autumn) | 500 | 1,123,386 | 0.605 | 46.09 min | 27.85 | 0.89% |
| `2_MID_PEAK` (Spring/Shoulder) | 426 | 1,187,095 | 0.589 | 55.06 min | 32.38 | 1.36% |
| `3_PEAK` (Summer Convective) | 224 | 1,305,968 | 0.576 | 68.43 min | 39.36 | 3.16% |
| `4_HOLIDAY` (Holiday Corridors) | 191 | 1,215,636 | 0.597 | 55.78 min | 33.07 | 1.82% |

### 4.3.4 Day-of-Week Dynamics

**Table 4.4a: Day-of-Week Volatility Dynamics**

| Day | Archetype | Mean Daily TSA | TSA CV | $\sigma_{\text{Delay}}$ | CVI |
| :---: | :--- | :---: | :---: | :---: | :---: |
| Mon | Outbound Business Surge | 1,246,150 | **0.604** | 56.56 min | **34.00** |
| Tue | Midweek Reset | 1,076,625 | 0.601 | **50.09 min** | **29.99** |
| Wed | Minimum Volatility Baseline | 1,123,368 | 0.594 | **49.27 min** | **29.13** |
| Thu | Corporate Outbound Ramp | 1,254,744 | 0.589 | 54.65 min | 31.96 |
| Fri | Business & Weekend Surge | 1,241,359 | 0.592 | 55.58 min | 32.77 |
| Sat | Volume Trough | 1,089,699 | 0.602 | 54.16 min | 32.45 |
| Sun | Leisure Return & Delay Cascade | 1,279,017 | 0.577 | **58.07 min** | **33.40** |

### 4.3.5 Diurnal Operational Turbulence

**Table 4.4b: Empirical Diurnal Hourly Regimes Conditioned on Day of Week**

| Day | `1_OFF_PEAK` | `2_MID_PEAK` | `3_PEAK` (Dual Non-Consecutive) |
| :--- | :--- | :--- | :--- |
| Monday | 00:00, 02:00–03:00 | 01:00, 04:00, 08:00–13:00 | **Morning:** 05:00–07:00 & **Evening:** 14:00–23:00 |
| Tuesday | 00:00, 02:00–03:00 | 01:00, 04:00, 08:00–16:00, 23:00 | **Morning:** 05:00–07:00 & **Evening:** 17:00–22:00 |
| Wednesday | 00:00–03:00 | 04:00, 09:00–13:00, 23:00 | **Morning:** 05:00–08:00 & **Evening:** 14:00–22:00 |
| Thursday | 00:00, 02:00–03:00 | 01:00, 04:00, 10:00–11:00 | **Morning:** 05:00–09:00 & **Evening:** 12:00–23:00 |
| Friday | 00:00, 02:00–03:00 | 01:00, 04:00, 09:00–11:00, 13:00 | **Morning:** 05:00–08:00 & **Evening:** 12:00, 14:00–23:00 |
| Saturday | 00:00, 02:00–03:00 | 01:00, 04:00, 08:00–13:00 | **Morning:** 05:00–07:00 & **Evening:** 14:00–23:00 |
| Sunday | 00:00, 02:00–03:00 | 01:00, 04:00, 10:00–11:00 | **Morning:** 05:00–09:00 & **Evening:** 12:00–23:00 |

**Table 4.4c: Sample Size Sufficiency Audit (84 Cross-Classification Cells)**

| Seasonal Regime | Diurnal Block | Cells | Min $N_{\text{train}}$ | Median $N_{\text{train}}$ | $N_{\text{train}} \ge 50$ (%) | Min $N_{\text{test}}$ | $N_{\text{test}} \ge 30$ (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Off-Peak (Winter/Fall) | Mid-Peak | 7 | 208 | 378.0 | 100% | 71 | 100% |
| Off-Peak (Winter/Fall) | Off-Peak | 7 | 156 | 156.0 | 100% | 53 | 100% |
| Off-Peak (Winter/Fall) | Peak | 7 | 468 | 702.0 | 100% | 171 | 100% |
| Mid-Peak (Spring/Shoulder) | Mid-Peak | 7 | 168 | 328.0 | 100% | 72 | 100% |
| Mid-Peak (Spring/Shoulder) | Off-Peak | 7 | 123 | 126.0 | 100% | 51 | 100% |
| Mid-Peak (Spring/Shoulder) | Peak | 7 | 369 | 615.0 | 100% | 153 | 100% |
| Peak (Summer Surge) | Mid-Peak | 7 | 95 | 168.0 | 100% | 32 | 100% |
| Peak (Summer Surge) | Off-Peak | 7 | 71 | 72.0 | 100% | 24 | 85.7% |
| Peak (Summer Surge) | Peak | 7 | 216 | 312.0 | 100% | 72 | 100% |
| Holiday Corridors | Mid-Peak | 7 | 68 | 132.0 | 100% | 24 | 71.4% |
| Holiday Corridors | Off-Peak | 7 | 48 | 66.0 | 85.7% | 18 | 57.1% |
| Holiday Corridors | Peak | 7 | 156 | 286.0 | 100% | 65 | 100% |

---

## 4.4 Temporal Demarcation: Post-Pandemic Regime Selection

| Evaluation Criteria | Candidate A (Jan 1, 2023) | **Candidate B (May 1, 2022 — RECOMMENDED)** |
| :--- | :--- | :--- |
| Statistical Justification | Rolling Welch's t-test convergence | CUSUM stabilization; Chow structural break; Mask Mandate Repeal |
| Training Span | 24 Months | **32 Months (captures Elliott & Summer 2023)** |
| Resilience Coverage | Misses Winter Storm Elliott (Dec 2022) | **Superior** |
| Generalizability | Smaller spoke airfield sample | **Superior (122k+ training observations)** |

---

## 4.5 Econometric Validation of Carrier Checkpoint Isolation

| Test | Result | Interpretation |
| :--- | :--- | :--- |
| Volume Conservation ($\rho = \text{TSA}/\text{Est}$) | $\rho = 1.00 \pm 0.04$ ($p < 0.001$) | Terminal volume matches carrier originating passengers |
| Zero-Flight Intercept ($\beta_0$) | $\beta_0 = 12.4$ pax/hr ($p = 0.40$) | Zero flights yield zero demand; no structural phantom queue |
| Cross-Carrier Independence ($\beta_{\text{other}}$) | $\beta_{\text{other}} = 0.002$ ($p = 0.62$) | Non-tenant carriers contribute zero demand |
| Layout Invariance (KS Test) | $D = 0.032, p = 0.28$ | Connected terminals behaviorally equivalent to air-gapped |

Using carrier-filtered flights: $R^2 = 0.708$–$0.774$. Using total pooled airport departures: $R^2 < 0.420$ ($p < 0.0001$).

---

## 4.6 Feature Engineering and Passenger Show-Up Curve Estimation

| Flight Feature Representation | $R^2$ | Pearson $r$ | Slope |
| :--- | :---: | :---: | :---: |
| Contemporaneous Departures ($t$) | 0.1988 | 0.4459 | 38.42 pax/flight |
| Lead $t+1$ | 0.3723 | 0.6102 | 62.15 pax/flight |
| **Lead $t+2$ (PEAK)** | **0.4054** | **0.6367** | **74.98 pax/flight** |
| Lead $t+3$ | 0.3299 | 0.5744 | 51.20 pax/flight |
| Show-Up Curve (Lead-Lag Distribution) | 0.4878 | 0.6985 | 74.98 pax/flight |
| **Show-Up Curve × T-100 Load Factor** | **0.4985** | **0.7061** | **90.56 pax/flight** |

Explanatory power peaks at Lead $t+2$, confirming the 90–120 minute modal passenger show-up window (ACRP Report 40). Interacting convolved demand with monthly T-100 load factors elevates $R^2$ to 0.4985 before temporal cyclical encodings.

---

## 4.7 Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)

**Table 4.7: Master Model Benchmark Matrix (72,053 Holdout Hours, 9-Airport Cohort)**

| Paradigm | ID | Architecture | Val $R^2$ | Test $R^2$ | RMSE | MAE | MASE | Bias |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| Deterministic | M0 | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1377.3 | 939.8 | 1.000 | -0.7 |
| Deterministic | M1 | Contemporaneous Sched SARIMAX | 0.4338 | 0.4375 | 1393.8 | 1042.6 | 1.109 | -327.4 |
| Probabilistic / ML | M2 | Passenger Show-Up Curve Only | 0.5443 | 0.5862 | 1195.5 | 856.2 | 0.911 | -296.8 |
| Probabilistic / ML | M3 | Show-Up Curve + OTP Delays | 0.5450 | 0.5880 | 1192.9 | 855.1 | 0.910 | -295.3 |
| Probabilistic / ML | M4 | Full Tri-Modal (Load Factor Scaled) | 0.5798 | 0.5771 | 1208.6 | 856.3 | 0.911 | -430.8 |
| **Two-Stage Hybrid** | **M5** | **Sequential SARIMA-Tree Hybrid** | **0.6644** | **0.6270** | **1135.0** | **795.0** | **0.846** | **-402.9** |

### 4.7.1 Performance Stratification Across Volatility Regimes

- **Low-Volatility (`1_OFF_PEAK`):** M3 and M5 achieve near-identical MASE (≈ 0.60–0.62). Kalman state corrections offer marginal incremental benefit over gradient boosted trees in stable environments.
- **High-Volatility (`3_PEAK` / Summer Severe Weather):** The performance gap widens dramatically. M3 suffers the "empty checkpoint fallacy," degrading to MASE = 1.025. M5 maintains MASE = 0.737 (RMSE = 1,023.2) through prior-hour terminal congestion feedback ($t-1$) and real-time Kalman queue innovation updates.

---

*END OF DRAFT B — Chapters I through IV*
