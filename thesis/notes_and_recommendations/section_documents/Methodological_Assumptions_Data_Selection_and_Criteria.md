# Methodological Assumptions: Data Selection, Screening Criteria, and Volatility Modeling of TSA Passenger Throughput

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University  
**Degree Program**: Master of Science in Aeronautics / Aviation Data Analytics  
**Target Document**: Thesis Chapter III (Methodology) Supporting Technical Treatise  
**Target Repository Directory**: `Gleich-Thesis/Thesis Section Documents/`  
**Primary Analytical Datasets**: TSA Checkpoint Throughput, BTS On-Time Performance (OTP), BTS Form 41 T-100 Segment Capacity, BTS DB1B/DB1C Ticket Surveys  
**Study Horizon**: 2019-01-01 through 2025-12-31 (Post-COVID Baseline: May 1, 2022 onwards)  

---

## 1. Executive Summary & Methodological Framing

Forecasting the volatility of landside airport passenger security screening throughput presents a fundamental challenge in air transportation analytics: **bridging the structural gap between airside aircraft movements and landside human passenger processing**. Airside flight departures are measured at the aircraft gate level via carrier dispatch logs, whereas landside screening throughput is recorded as aggregate human body counts through physical Transportation Security Administration (TSA) security checkpoint lanes.

To formulate, train, and evaluate predictive models—ranging from baseline distributed lag models to multi-quantile Gradient-Boosted Decision Trees (GBDT) and two-stage hybrid queueing architectures—a series of rigorous methodological assumptions must be established across **data selection**, **terminal flow geometry**, **temporal lead-lag dynamics**, and **model evaluation criteria**. 

These assumptions are grounded in airport terminal operations, stochastic queueing theory, econometrics, and federal terminal planning standards (notably **FAA ACRP Report 25** and **ACRP Report 40**). The primary objective is to protect the modeling framework against phase-shift misspecification, multicollinear pooling endogeneity, unobserved passenger mixture bias, and target data leakage.

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        DATA GENERATING PROCESS (DGP) ARCHITECTURE                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                            │
   1. FLIGHT CAPACITY                       ▼
      Scheduled Flight Departures [f ∈ F(A)] × Aircraft Gauge Seats(f)
                                            │
   2. PASSENGER LOAD FACTOR                 ▼
      × Route Segment Load Factor [BTS T-100 Monthly Segment Average]
                                            │
   3. THE HUB DISCONNECT                    ▼
      × Local Originating Fraction [1 - Connecting Ratio C(A) from BTS DB1B/DB1C]
                                            │
   4. SHOW-UP TIME CONVOLUTION              ▼
      Convolved Across Empirical Passenger Show-Up Curve [w_1=0.25, w_2=0.55, w_3=0.20]
                                            │
   5. CARRIER CHECKPOINT ISOLATION          ▼
      Mapped to Carrier-Exclusive Dedicated Checkpoints [P(Carrier = j* | Chk k) = 1.0]
                                            │
                                            ▼
                       ESTIMATED HOURLY CHECKPOINT THROUGHPUT
```

---

## 2. Terminal Screening Flow & Passenger Movement Assumptions

### 2.1 Non-Traveling Entrants, Aborted Boardings, and Landside Exits Are Statistically Negligible
* **Core Assumption**: Individuals who pass through a carrier-exclusive security checkpoint and subsequently exit without boarding a departing flight from that terminal—such as non-traveling individuals issued airline gate passes (e.g., guardians escorting unaccompanied minors, companions assisting elderly or disabled passengers, military send-offs), ticketed passengers who cancel or miss their flights and exit the sterile concourse, airport or concession staff utilizing passenger lanes, or individuals clearing security solely to access airside amenities and leaving—represent a **statistically negligible fraction** ($\ll 1\%$) of total hourly screening volume.
* **Operational & Mathematical Justification**: 
  1. *Volume Magnitude Disparity*: Public TSA throughput logs report aggregate physical screening counts per lane per hour without passenger identification. In the commercial hub terminals analyzed (such as LGA Terminal C, EWR Terminal C, or LAX Terminal 4), peak departure banks generate screening volumes between 1,800 and 4,500 passengers per hour. Gate pass issuance is tightly restricted by federal security directives (49 CFR § 1544.205) and airline operating rules, typically limited to a handful of occurrences per bank.
  2. *Signal-to-Noise Ratio*: Aborted boardings (passengers voluntarily leaving after screening) and non-flying entrants remain within the stochastic noise floor of the counting process. Modeling landside checkpoint screening as a direct $1:1$ physical mapping to departing flight manifests avoids introducing arbitrary latent parameters that cannot be measured directly without violating data privacy.

### 2.2 Decoupling of Originating and Connecting Passengers (The Hub Disconnect)
* **Core Assumption**: Only **local originating (Origin and Destination / O&D) passengers** pass through TSA security checkpoints at an airport. Domestic connecting passengers arriving on inbound feeder flights transfer between gates within the sterile airside area and **never enter landside security screening** at the connecting hub.
* **Operational & Mathematical Justification**:
  1. *Physical Reality of Domestic Transfers*: Federal aviation security architecture guarantees that domestic passengers remain behind the sterile security perimeter during intermediate transfers. Under normal operating conditions, a passenger connecting at Atlanta (`ATL`), Dallas/Fort Worth (`DFW`), or Chicago O'Hare (`ORD`) never clears TSA security at that intermediate facility.
  2. *Elimination of the Throughput Paradox*: Treating total departing aircraft seats as checkpoint demand creates catastrophic forecasting errors at hub airports. For example, at Charlotte (`CLT`), total scheduled departing seat capacity exceeds 34 million annual passengers, yet annual TSA checkpoint throughput is only 28.2 million. Incorporating coupon-level routing sequences from BTS DB1B/DB1C reveals that 76.0% of Charlotte's passengers are connecting transfers. Multiplying seat capacity by the local originating fraction:
     $$L(A) = 1 - C(A)$$
     (where $C(A) = 0.760$ at CLT, $0.701$ at ATL, and $0.663$ at DFW) deflates airside seat capacity to true landside security demand, resolving the discrepancy.

### 2.3 Strict Exclusion of Inbound and Arriving Aircraft
* **Core Assumption**: Inbound flights terminating at candidate airfields generate **zero direct screening demand** on that airport's TSA checkpoints and must be strictly excluded from the flight schedule feature store ($0$ records in the demand pipeline).
* **Operational & Mathematical Justification**: Deplaning passengers flow through dedicated, monitored one-way exit portals directly to baggage claim and ground transport. Arriving passenger volume has no physical access to security screening lanes. Including arriving flights in predictive demand models introduces spurious lagged correlations and phantom volume spikes.

### 2.4 Nationwide Network Departure Completeness (Demand Completeness Principle)
* **Core Assumption**: Every scheduled flight departing from a target airfield to **any of the 294+ domestic destinations nationwide** and across **all 18 reporting carriers** must be retained in the demand pipeline, regardless of destination size or whether it is operated by a mainline carrier or a regional commuter affiliate.
* **Operational & Mathematical Justification**: Physical security screening occurs landside prior to concourse entry. Checkpoint queues do not differentiate between a traveler boarding a Boeing 777 to London, a Boeing 737 to Chicago, or a regional Embraer 175 to Traverse City. Restricting flight schedules strictly to flights between the Top 25 airfields or strictly to Big 3 mainline flights would discard **over 50% of originating passengers**, creating artificial volatility and unexplained surges in physical screening.

### 2.5 Minimal Post-Security Terminal Cross-Over
* **Core Assumption**: In terminals designated as carrier-exclusive, the proportion of passengers who clear security at that terminal but walk or take airside shuttles to board a flight departing from a different terminal (or vice versa) is statistically negligible or physically constrained.
* **Operational & Mathematical Justification**: The experimental cohort intentionally prioritizes terminals with standalone landside footprints or isolated concourses (e.g., LGA Terminal C, DTW McNamara, EWR Terminal C, and BOS Terminal A). Where airside connectors exist (such as between Terminals 4 and 5 at LAX), passengers overwhelmingly use the security checkpoint directly adjacent to their ticket counter and departure gate to minimize walking distance and dwell time.

---

## 3. Temporal Dynamics & Passenger Arrival Curve Assumptions

```
Landside Curbside       TSA Screening         Airside Transit / Dwell      Boarding Door Closes     Pushback (CRSDepTime)
      │                       │                            │                          │                        │
      ▼                       ▼                            ▼                          ▼                        ▼
[ T - 120 min ] ──────> [ T - 100 min ] ───────────> [ T - 70 min ] ────────────> [ T - 15 min ] ─────────> [ T = 0 ]
```

### 3.1 The Physical Arrow of Time (Rejection of Contemporaneous Modeling)
* **Core Assumption**: Naive contemporaneous modeling ($t \leftrightarrow t$) that correlates hourly checkpoint throughput directly with flights departing in that same hour introduces a fundamental **phase-shift misspecification error** and must be replaced by a forward-looking **90- to 120-minute lead time window**.
* **Operational & Mathematical Justification**: Airport terminals operate as unidirectional physical pipelines governed by mandatory downstream temporal thresholds:
  1. *Boarding Door Closure ($T - 15$ to $T - 20$ min)*: Federal regulations and airline standard operating procedures require boarding doors to close strictly 15 minutes before scheduled pushback (`CRSDepTime`).
  2. *Boarding Commencement ($T - 35$ to $T - 50$ min)*: Passengers must assemble at the gate 35 to 50 minutes prior to pushback.
  3. *Airside Transit and Concourse Dwell ($T - 70$ to $T - 40$ min)*: Traversing concessions, restrooms, and automated people movers (e.g., DFW Skylink) requires 12 to 25 minutes.
  4. *Security Screening ($T - 100$ min)*: Checkpoint queues, ID verification, divestiture, and scanning consume 10 to 30 minutes during normal banks.
  
  Under a contemporaneous model ($t \leftrightarrow t$), a passenger clearing security at 06:35 is incorrectly modeled as demand for a flight departing between 06:00 and 06:59. In reality, that flight's doors closed at 06:15; the passenger clearing at 06:35 is boarding a flight scheduled between 07:45 and 08:45. Contemporaneous alignment correlates disjoint events.

### 3.2 Empirical Passenger Show-Up Curve (Lognormal Arrival Density Kernel)
* **Core Assumption**: Human passenger arrival lead time $\tau$ relative to scheduled departure follows a continuous, right-skewed, unimodal **lognormal probability distribution**:
  $$\tau \sim \text{Lognormal}(\mu \approx 4.65, \, \sigma \approx 0.35)$$
  yielding an empirical mode at $\tau^* \approx 92.5\text{ minutes}$ prior to pushback, a median lead time of $\approx 104.6\text{ minutes}$, and discrete hourly convolution weights:
  $$w_1 (\text{lead } 1\text{ hr}) = 0.25, \quad w_2 (\text{lead } 2\text{ hr}) = 0.55, \quad w_3 (\text{lead } 3\text{ hr}) = 0.20$$
* **Operational & Mathematical Justification**:
  1. *Literature Grounding*: Validated by airport planning standards (**FAA ACRP Report 25**, **ACRP Report 40**) and transport literature (de Neufville & Odoni, 2013). Passengers do not arrive as a single discrete block; their arrival distribution exhibits a sharp cut-off near $T - 20$ minutes (gate closure) and a long, positive tail extending past 180 minutes (leisure travelers and checked-baggage drop).
  2. *Distributed Lag Model Verification*: In unconstrained distributed lag regressions ($Y_t = \alpha + \sum_{k=0}^4 \beta_k X_{t+k} + \varepsilon_t$), empirical estimation consistently demonstrates that $\beta_1$ (60 min lead) and $\beta_2$ (120 min lead) capture $>80\%$ of total model weight, while contemporaneous coefficients ($\beta_0$) approach zero.

### 3.3 Strict Information Causality & Zero Lookahead Target Leakage
* **Core Assumption**: Pre-flight models predicting checkpoint demand and flight delay volatility must strictly rely on scheduled, planned parameters known prior to departure (`CRSDepTime`, scheduled seats, historical rolling reliability) and must never consume realized operational timestamps (`DepTime`, `WheelsOff`, `TaxiOut`).
* **Operational & Mathematical Justification**: Realized departure delays, pushback timestamps, and actual wheels-off times are determined hours after passengers have cleared security. Incorporating realized flight performance into pre-departure screening forecasts introduces severe target data leakage, rendering models operationally unusable for TSA staffing allocations and terminal resource planning.

### 3.4 Diurnal Periodic Continuity (Trigonometric Time-of-Day Encodings)
* **Core Assumption**: Time-of-day features must be encoded as continuous periodic functions across the 1,440 minutes of the day using trigonometric sine and cosine transformations:
  $$\sin\left(\frac{2\pi \cdot \text{MinOfDay}}{1440}\right), \quad \cos\left(\frac{2\pi \cdot \text{MinOfDay}}{1440}\right)$$
* **Operational & Mathematical Justification**: Raw integer representations of hour or minute-of-day introduce an artificial mathematical discontinuity between 23:59 (minute 1439) and 00:00 (minute 0). Trigonometric transformations preserve cyclic proximity, allowing machine learning models to smoothly interpolate late-night arrivals into early-morning red-eye banks.

---

## 4. Data Selection & Purposive Filtering Pipeline Assumptions

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                    FOUR-TIERED PURPOSIVE SAMPLING PIPELINE                       │
└──────────────────────────────────────────────────────────────────────────────────┘
                                        │
                                        ▼
 1. MACRO FILTER: Systemic Scale & Throughput Volume
    └── Restrict to Top 25 commercial airfields by flight departures and TSA volume.
    └── Captures ~67% of total U.S. commercial aviation activity (Pareto distribution).
    └── Eliminates low-frequency regional anomalies and erratic small-hub queues.
                                        │
                                        ▼
 2. MESO FILTER: Legacy Big 3 Carrier Co-Location
    └── Mandatory concurrent scheduled service by American, Delta, and United.
    └── Enforces competitive operational parity and eliminates network-absence bias.
    └── Excludes low-cost carriers (e.g. Southwest) due to divergent boarding models.
                                        │
                                        ▼
 3. MICRO FILTER: Causal Identification via Checkpoint Exclusivity
    └── Checkpoints must serve an individual carrier exclusively (or near-exclusively).
    └── Eliminates cross-carrier passenger pooling contamination.
    └── Maps airline schedule directly to physical checkpoint arrivals.
                                        │
                                        ▼
 4. EXPERIMENTAL FILTER: Orthogonal Factorial Symmetry (3x3 / 4x4 Design)
    └── 3 to 4 dedicated checkpoint environments per carrier (AA, DL, UA).
    └── Balanced coverage across all 4 operational clusters and 4 terminal archetypes.
    └── Enables zero-shot Generalizability and Twin Disruption Resilience testing.
```

### 4.1 Macro Scale Truncation & Heavy-Traffic Asymptotics (Top 25 Census)
* **Core Assumption**: Empirical modeling of passenger throughput volatility requires truncating the national airport census to the **Top 25 commercial airfields**, capturing **67.2% of nationwide commercial passenger movements** under a Pareto power-law distribution ($\mathbb{P}(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$).
* **Operational & Mathematical Justification**:
  1. *Heavy-Traffic Queueing Limits*: In multi-server queueing systems ($G_t/G/c_t$), traffic intensity is $\rho(t) = \frac{\lambda(t)}{c(t)\mu}$. Small and regional airports operate in light-traffic regimes ($\rho \ll 0.3$), where queue delay is near zero ($W_q \approx 0$) and throughput trivially equals arrival rate ($Y_t \approx \lambda_t$). In contrast, Top 25 hubs reach $\rho(t) \to 1.0$ during peak morning and afternoon departure banks, producing non-linear queue friction, lane spillover, and balking dynamics necessary to train and validate congestion-aware models.
  2. *Signal-to-Noise Ratio (SNR)*: Relative counting error scales as $CV = 1/\sqrt{\lambda}$. At low-volume regional airports ($\lambda \approx 50\text{ pax/hr}$), $CV \approx 0.14$, meaning stochastic noise obscures the scheduled signal. At Top 25 hubs ($\lambda > 3{,}000\text{ pax/hr}$), $CV < 0.018$, guaranteeing parameter stability.

### 4.2 Micro Carrier Checkpoint Exclusivity (Causal Identification)
* **Core Assumption**: To establish causal identification between an airline's flight schedule and security checkpoint throughput, the modeling sample must be restricted to **carrier-exclusive screening checkpoints** where:
  $$\mathbb{P}(\text{Passenger Airline} = j^* \mid \text{Checkpoint } k) = 1.0$$
* **Operational & Mathematical Justification**: In shared multi-airline terminals (such as Salt Lake City `SLC` or Phoenix `PHX` Terminal 4), multiple airlines funnel passengers into common screening lanes. Because hub carriers synchronize departure banks to maximize connecting banks, their departure schedules are highly collinear:
  $$\text{Corr}(S_{j, t+m}, S_{j', t+m}) \ge 0.88$$
  This causes the empirical Gram matrix $\mathbf{X}^\top \mathbf{X}$ to become severely ill-conditioned ($\kappa(\mathbf{X}^\top \mathbf{X}) \gg 10^4$). Under ordinary least squares or regularized estimation, individual carrier response functions are structurally unidentifiable. Isolating carrier-exclusive checkpoints collapses the mixture, reducing estimation to an orthogonal Wiener-Hopf deconvolution with condition number $\kappa < 25$.

### 4.3 Meso Big 3 Carrier Symmetry & Co-Location (Shock Invariance)
* **Core Assumption**: Candidate airfields must maintain concurrent, continuous scheduled operations from all three major legacy network carriers: **American Airlines (AA)**, **Delta Air Lines (DL)**, and **United Airlines (UA)**.
* **Operational & Mathematical Justification**: In panel econometrics:
  $$Y_{ijt} = \mathbf{x}_{ijt}^\top \boldsymbol{\beta} + \gamma_i + \delta_t + \eta_{jt} + \varepsilon_{ijt}$$
  Requiring concurrent Big 3 presence ensures that when computing contrasts between carriers ($\Delta Y_{(j - j')it}$), unobserved airport terminal geometry effects ($\gamma_i$) and common regional weather/FAA ground delay programs ($\delta_t$) cancel out identically:
  $$\Delta Y_{(j - j')it} = (\mathbf{x}_{ijt} - \mathbf{x}_{ij't})^\top \boldsymbol{\beta} + (\eta_{jt} - \eta_{j't}) + (\varepsilon_{ijt} - \varepsilon_{ij't})$$
  Observed throughput differences are thus strictly isolated to carrier scheduling, fleet gauge, and passenger behavior.

### 4.4 Southwest Airlines (WN) Exclusion (Arrival Timing Consistency)
* **Core Assumption**: Southwest Airlines must be excluded from the carrier-exclusive micro-cohort.
* **Operational & Mathematical Justification**: Legacy network carriers (AA, DL, UA) utilize assigned seating, checked baggage fees, and elite priority boarding, producing a unimodal parametric arrival distribution ($\mathbb{E}[\tau] \approx 105\text{ min}$). In contrast, Southwest Airlines operates an open boarding-group structure (A, B, C) combined with a "Bags Fly Free" policy. This generates a **bimodal arrival mixture**:
  - *Group 1 ($\mu_1 \approx 135\text{ min}$)*: Early arrivers seeking favorable boarding positions.
  - *Group 2 ($\mu_2 \approx 65\text{ min}$)*: Baggage-free business travelers bypassing ticket counters right before gate close.
  
  Mixing Southwest passengers into legacy queues violates the assumption of **consistent passenger arrival timing** ($f_j(\tau) = f(\tau)$), inducing unobserved heteroskedasticity and distorting the arrival density kernel.

### 4.5 Post-COVID Study Period (May 1, 2022 to December 31, 2025)
* **Core Assumption**: The contemporary post-pandemic operational equilibrium begins on **May 1, 2022**, established at the **network-wide aggregate level** rather than on individual airports.
* **Operational & Mathematical Justification**: 
  1. *Federal Policy Demarcation*: The nationwide federal transportation mask mandate was struck down on April 18, 2022, marking the legal and operational conclusion of emergency travel restrictions.
  2. *Mitigating Uneven Recovery*: Leisure-oriented airports (e.g., Orlando `MCO`, Las Vegas `LAS`) rebounded to 2019 volumes by mid-2021, whereas coastal business and international hubs (e.g., Boston `BOS`, Newark `EWR`, New York `LGA`, San Francisco `SFO`) remained suppressed until mid-2022. Defining the temporal threshold across the Top 25 network aggregate eliminates localized recovery distortions, ensuring models are trained on an equilibrium regime characterized by stable national load factors ($\ge 84\%$) and re-banked airline schedules.

---

## 5. Model Evaluation, Factorial Design & Resilience Assumptions

### 5.1 Orthogonal Factorial ANOVA Balance
* **Core Assumption**: Evaluating model performance differences across carriers and airport operational clusters requires an orthogonal, balanced experimental layout (e.g., 3 carriers $\times$ 3 to 4 distinct operational clusters).
* **Operational & Mathematical Justification**: In an unbalanced design, Sum of Squares decompositions in two-way ANOVA are non-orthogonal ($\text{Cov}(\hat{\alpha}_i, \hat{\beta}_j) \ne 0$), resulting in variance inflation and test statistic ambiguity (Type I vs. Type II vs. Type III Sum of Squares). In the balanced 9-Airport Experimental Cohort, design matrix column orthogonality guarantees that main effects and interaction effects are independent, maximizing statistical power in hypothesis testing.

### 5.2 Statistical Domain Adaptation & Spatial Layout Transferability
* **Core Assumption**: Generalizability can be rigorously evaluated by isolating physical terminal layout penalties from macro operational regime shifts using statistical learning domain adaptation bounds:
  $$\epsilon_{\mathcal{T}}(h) \le \epsilon_{\mathcal{S}}(h) + \frac{1}{2} d_{\mathcal{H}\Delta\mathcal{H}}(\mathcal{D}_{\mathcal{S}}, \, \mathcal{D}_{\mathcal{T}}) + \lambda^*$$
* **Operational & Mathematical Justification**:
  - *Intra-Cluster Transfer (e.g., United EWR Terminal C $\to$ Delta LGA Terminal C)*: Both airfields share identical New York metroplex thunderstorm delays, taxi-out congestion ($\sim 24\text{ min}$), and $\sim 60\%$ local passenger ratios ($d_{\mathcal{H}\Delta\mathcal{H}}^{\text{Regime}} = 0$). Any zero-shot predictive error degradation isolates the **pure physical terminal layout transfer penalty**.
  - *Inter-Cluster Transfer (e.g., United ORD vs. United EWR vs. United IAH)*: Holding carrier and terminal dedication constant, predictive degradation isolates macro operational schedule volatility and connecting passenger dynamics.

### 5.3 Matched Natural Experiments for Disruption Resilience (Twin Shocks)
* **Core Assumption**: Co-located terminals within the same Terminal Radar Approach Control (TRACON) airspace (e.g., `EWR` Terminal C and `LGA` Terminal C under New York TRACON) experience identical exogenous weather shock treatments ($W = 1$).
* **Operational & Mathematical Justification**: Under the Rubin Causal Model, evaluating checkpoint resilience requires comparing recovery trajectories under equivalent shocks. When convective weather triggers FAA Ground Delay Programs across New York, both facilities receive simultaneous exogenous disruptions, serving as natural counterfactual twin controls to evaluate Time-to-Recovery (TTR) and resilience without local weather bias.

### 5.4 Structural Nighttime Closures vs. Missing Sensor Data
* **Core Assumption**: Hours with zero recorded throughput during late-night periods ($00:00\text{--}04:00$) represent **planned operational checkpoint closures (structural zeros)** rather than sensor dropouts or missing data.
* **Operational & Mathematical Justification**: Checkpoint lanes are intentionally closed overnight when no scheduled flights depart. Treating these records as missing data and imputing non-zero values would distort overnight variance. Filtering to active screening windows (`vw_tsa_active_throughput`) and modeling log-transformed counts ($\ln(1 + \text{throughput})$) preserves zero-bounded count properties while preventing negative throughput predictions.

---

## 6. Synthesis Master Reference Matrix

| Category | Key Methodological Assumption | Plain Aviation Terminology | Mathematical & Empirical Justification | Failure Mode / Bias Prevented |
| :--- | :--- | :--- | :--- | :--- |
| **Terminal Flow** | **Non-traveler exits are negligible** | Checkpoint Exclusivity / Minimal Non-Passenger Exits | Gate passes and aborted boardings are $\ll 1\%$ of peak bank volume ($1,800\text{--}4,500\text{ pax/hr}$). | Over-parameterized noise modeling; artificial uncoupling. |
| **Terminal Flow** | **Connecting passengers bypass security** | The Hub Disconnect (Connecting Deflator) | Connecting passengers remain airside. Scaled by $(1 - C_A)$ via BTS DB1B/DB1C ticket surveys. | Throughput paradoxes (e.g., CLT 76% connecting traffic). |
| **Terminal Flow** | **Exclusion of inbound arrivals** | One-Way Deplaning Exit Isolation | Arriving passengers flow directly to baggage claim; zero physical access to security screening. | Spurious correlation and phantom demand spikes. |
| **Terminal Flow** | **Exhaustive nationwide departures** | Demand Completeness Principle | Physical screening serves all 294+ domestic destinations and 18 regional/trunk carriers. | Truncation bias (>50% omitted originating passenger demand). |
| **Temporal Coupling** | **90–120 min lead time window** | The Physical Arrow of Time | Boarding doors close at $T-15\text{m}$; screening occurs at $T-100\text{m}$. Forward lead convolution. | Phase-shift misspecification ($t \leftrightarrow t$ correlation error). |
| **Temporal Coupling** | **Lognormal arrival density kernel** | Empirical Passenger Show-Up Curve | $\tau \sim \text{Lognormal}(4.65, 0.35)$; mode $\approx 92.5\text{m}$; discrete weights $(0.25, 0.55, 0.20)$ (ACRP 40). | Rigid scalar shifts failing to capture human behavioral variance. |
| **Temporal Coupling** | **Zero lookahead leakage** | Strict Information Causality | Only planned pre-departure schedules (`CRSDepTime`, planned seats) are fed into pre-flight models. | Severe target leakage from realized flight delays and pushback times. |
| **Sample Filtering** | **Top 25 macro power-law cut-off** | Scale & Heavy-Traffic Asymptotics | Captures 67.2% of NAS volume; Kingman limit $\rho \to 1.0$ produces non-linear queue friction; $CV < 0.018$. | Light-traffic triviality ($\rho \ll 0.3$) and low signal-to-noise ratio. |
| **Sample Filtering** | **Micro checkpoint exclusivity** | Carrier Checkpoint Isolation | In shared terminals, departure banks are collinear ($\text{Corr} \ge 0.88$). Exclusive checkpoints yield $\kappa < 25$. | Ill-conditioned Gram matrix ($\kappa \gg 10^4$) and unidentifiable models. |
| **Sample Filtering** | **Meso Big 3 co-location** | Exogenous Shock Invariance | Common FAA Ground Delay Programs and weather shocks cancel out ($\delta_t - \delta_t = 0$) when differencing. | Carrier performance confounded by regional airspace weather. |
| **Sample Filtering** | **Exclusion of Southwest (WN)** | Consistent Passenger Arrival Timing | Open-seating and free checked bags create a bimodal arrival mixture ($\mu_1 \approx 135\text{m}, \mu_2 \approx 65\text{m}$). | Violation of parameter exchangeability ($f_j(\tau) \ne f(\tau)$). |
| **Sample Filtering** | **Post-COVID May 1, 2022 boundary** | Post-COVID Study Period | Federal mask mandate lifting; network-wide aggregate inflection point smooths recovery disparities. | Localized leisure vs. business recovery distortions; unstable load factors. |
| **Evaluation** | **Orthogonal factorial design** | Balanced Factorial Evaluation Grid | Equal carrier environments across distinct operational clusters ensures $\mathbf{X}_A^\top \mathbf{X}_B = \mathbf{0}$. | Unbalanced ANOVA variance inflation; non-additive Sum of Squares. |
| **Evaluation** | **Twin TRACON disruption controls** | Matched Twin Disruption Shocks | Co-located New York TRACON terminals (EWR T-C vs. LGA T-C) receive simultaneous convective treatments. | Localized weather confounding in resilience and recovery evaluation. |
| **Data Engineering** | **Structural zeros vs. sensor drops** | Nighttime Checkpoint Closures | Overnight zeros reflect scheduled lane closures; zero-bounded count regression / log-transforms. | Imputing artificial non-zero counts; negative passenger predictions. |

---
*This document serves as an authoritative technical reference for Chapter III (Methodology) of the Master's Thesis.*
