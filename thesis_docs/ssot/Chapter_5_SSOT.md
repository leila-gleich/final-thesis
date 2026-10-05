# CHAPTER V SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DOCUMENT: Chapter V Single Source of Truth (SSOT) Reference Specification
RELEASE VERSION: v4.0 (SemVer-Data) | DATE: October 2026
CANONICAL LOCATION: thesis_docs/ssot/Chapter_5_SSOT.md
COMPANION DRAFT: thesis_docs/manuscripts/Chapter_5_Analysis_and_Discussion.md
====================================================================================================

## 1. PURPOSE AND SCOPE OF THE SSOT DOCUMENT

This document serves as the **definitive, immutable Single Source of Truth (SSOT)** for Chapter V (Analysis & In-Depth Discussion) of the graduate thesis.

It formalizes the theoretical interpretation, operational behavioral mechanisms, empirical hypothesis evaluation matrices ($H_1, H_{1a}, H_{1b}, H_{1c}$), cross-project synthesis (Projects 1, 2, and 3), and policy recommendations (including the Regime-Switched Gated Inference Engine). Any theoretical claims, metric interpretations, or strategic implications presented in Chapter V must strictly align with the specifications anchored herein.

---

## 2. CANONICAL CHAPTER V OUTLINE ARCHITECTURE

Chapter V is structured into seven comprehensive sections:

```
CHAPTER V: ANALYSIS & IN-DEPTH DISCUSSION
├── 5.1 Spatial Architecture and Passenger Behavioral Dynamics
│   ├── Connecting Passenger Shielding (The Hub Disconnect)
│   ├── Terminal Complex Aggregation vs. Administrative TSO Noise
│   └── Behavioral Invariance Across Terminal Layouts (CAT Scanners & Luggage Barriers)
├── 5.2 Initial Training and Passenger Show-Up Dynamics
│   ├── Lead-Lag Operational Time Offset (ACRP Report 40)
│   ├── Flight Delay Information Causality (t - 1 Proxy)
│   └── 5.2.1 The Lead-Lag Asynchrony Mechanism (Morning 05:00–08:00 vs. Evening 14:00–22:00)
├── 5.3 Deep-Dive: Evaluation Dimension 1 – Robustness (Routine Operational Accuracy)
│   ├── Benchmark Matrix: M1 (1.083 MASE) vs. M3 (0.890 MASE) vs. M5 (0.834 MASE, DM = 79.12)
│   ├── Evaluation of Hypothesis H_1a (Routine Non-Linear Accuracy)
│   └── 5.3.1 Robustness Across the 84-Cell Grid & Prevention of Weather Delay Distortion
├── 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience Under Disruption
│   ├── Benchmark Matrix: M1 (0.89 R_MASE) vs. M3 (0.87 R_MASE) vs. M5 (0.737 MASE, 0.88 R_MASE)
│   ├── Severe Disruption Degradation (Winter Storm Elliott: Pure ML R_MASE = 2.14 vs. Hybrid = 1.28)
│   ├── Kaplan-Meier Time-to-Recovery (Hybrid TTR = 3.2h vs. ML = 6.7h vs. SARIMA = 8.4h)
│   ├── Evaluation of Hypothesis H_1b (Hybrid Resilience Under Shock)
│   └── 5.4.1 Resilience Mechanics and the "Empty Checkpoint Fallacy" vs. State-Space Innovation
├── 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Cross-Airport Transferability)
│   ├── Benchmark Matrix: M1 (+4.4%, RTR = 1.04) vs. M3 (+7.9%, RTR = 1.08) vs. M5 (+18.7%, RTR = 1.19)
│   ├── Deep Neural Network Overfitting & Failure (Δ = +48.2%)
│   ├── Project 3 State-Space Zero-Shot Stability (EWR → LGA: Δ = 0.0%, RTR = 1.00; DTW → PHL: RTR = 0.86)
│   ├── Evaluation of Hypothesis H_1c (Structural Portability)
│   └── 5.5.1 Generalizability via Standardized Volatility Archetypes
├── 5.6 Master Synthesis and Operational Recommendations
│   ├── Cross-Dimensional Paradigm Evaluation Matrix
│   ├── 5.6.1 The Regime-Switched Gated Inference Engine (CVI < 30 vs. CVI ≥ 35)
│   └── 5.6.2 Strategic Implications for TSA and Airport Authorities
└── 5.7 Empirical Cross-Project Synthesis (Projects 1, 2, and 3)
    ├── Project 1 (Supervised ML): Out-of-Time Accuracy & Holdout Evaluation (M5 R^2 = 0.6270, MASE = 0.846)
    ├── Project 2 (Queuing Simulation): Dynamic Allocation Slashes Delays by 80.1% (5,514 vs 27,763 pax-hrs)
    └── Project 3 (State-Space Modeling): Recursive Innovation Tracking & Perfect Portability (RTR = 1.00)
```

---

## 3. MASTER SYNTHESIS & HYPOTHESIS EVALUATION REGISTRY

### 3.1 Evaluation of Overarching Thesis Hypothesis ($H_1$)

> **Core Hypothesis ($H_1$)**: Across the three forecasting paradigms (deterministic, machine learning, and two-stage hybrid), **no individual architecture will prove universally superior across all three evaluation dimensions**. Rather, systematic trade-offs exist across robustness, resilience, and generalizability.

The empirical findings **decisively confirm** $H_1$, as summarized in the master performance matrix:

| Evaluation Dimension | Primary Operational Metric | Deterministic Baselines ($M_0, M_1$) | Probabilistic & Machine Learning ($M_2, M_3, M_4$) | Sequential Two-Stage State-Space Hybrid ($M_5$) | Winning Paradigm |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Dimension 1: Robustness** | $\text{MASE}_{\text{routine}}$ (Undisturbed flow) | 1.083 (Inferior) | 0.890 (Target $< 0.90$) | **0.834 (SUPERIOR; DM = 79.12)** | **Hybrid ($M_5$) / ML ($M_3$)** |
| **Dimension 2: Resilience** | $R_{\text{MASE}}$ & Time-to-Recovery ($\text{TTR}$) | $\text{TTR} = 8.4\text{ h}$ (Sluggish) | $R_{\text{MASE}} = 2.14, \text{TTR} = 6.7\text{ h}$ (Fragile) | **$R_{\text{MASE}} = 1.28, \text{TTR} = 3.2\text{ h}$ (SUPERIOR)** | **Two-Stage Hybrid ($M_5$)** |
| **Dimension 3: Generalizability** | Relative Transfer Ratio ($\text{RTR}$) | **$\text{RTR} = 1.04$ ($\Delta = +4.4\%$)** | $\text{RTR} = 1.08$ ($\Delta = +7.9\%$) | $\text{RTR} = 1.19$ ($\Delta = +18.7\%$) / State-Space $\mathbf{1.00}$ | **Deterministic ($M_1$) / ML ($M_3$) / State-Space** |

### 3.2 Sub-Hypothesis Verification Proofs

1. **Sub-Hypothesis $H_{1a}$ (Robustness: Routine Operational Accuracy)**:
   - *Hypothesis Statement*: Non-linear machine learning models ($M_3$) and two-stage hybrids ($M_5$) will achieve superior routine operational accuracy ($\text{MASE}_{\text{routine}} < 0.90$), outperforming linear baselines ($M_1$).
   - *Empirical Proof*: Confirmed. $M_5$ achieves $\text{MASE}_{\text{routine}} = 0.834$ ($\text{RMSE} = 1114.7$), and $M_3$ achieves $\text{MASE}_{\text{routine}} = 0.890$ ($\text{RMSE} = 1167.9$), compared to $M_1$ at $\text{MASE} = 1.083$ ($\text{RMSE} = 1365.7$). Diebold-Mariano tests confirm statistical significance ($DM = 79.123, p < 0.0001$ for $M_5$; $DM = 74.247, p < 0.0001$ for $M_3$).

2. **Sub-Hypothesis $H_{1b}$ (Resilience: Stability Under Severe Disruption)**:
   - *Hypothesis Statement*: Sequential two-stage hybrid models ($M_5$) will demonstrate superior disruption resilience ($R_{\text{MASE}} \le 1.30$, $\text{TTR} \le 4.0\text{ hours}$), resisting the "empty checkpoint fallacy" that degrades pure machine learning during flight delay cascades.
   - *Empirical Proof*: Confirmed. Under acute disruption (Winter Storm Elliott and summer convective storms), pure ML models suffered acute degradation ($R_{\text{MASE}} = 2.14, \text{TTR} = 6.7\text{ hours}$). The Two-Stage Hybrid maintained $R_{\text{MASE}} = 1.28$ ($\le 1.30$) and achieved a Time-to-Recovery of **3.2 hours** ($\le 4.0\text{ hours}$), driven by recursive state-space innovation updates ($e_t = y_t - C\hat{x}_{t|t-1}$).

3. **Sub-Hypothesis $H_{1c}$ (Generalizability: Cross-Airport Portability)**:
   - *Hypothesis Statement*: Simple deterministic physical baselines ($M_1^*$) and distributed show-up machine learning models ($M_3$) will exhibit superior zero-shot spatial transferability ($\text{RTR} \le 1.10$, error degradation $\le 10\%$), avoiding the severe facility over-fitting typical of deep neural networks.
   - *Empirical Proof*: Confirmed. Direct cross-airport deployment within Cluster 3 (EWR Terminal C $\to$ LGA Terminal C) resulted in transfer degradations of only **+4.4%** for $M_1$ ($\text{RTR} = 1.04$) and **+7.9%** for $M_3$ ($\text{RTR} = 1.08$). In contrast, deep neural networks suffered a **+48.2%** error explosion. In Project 3, the Extended Kalman Filter State-Space Hybrid achieved absolute transfer stability ($\text{RTR} = 1.00, \Delta = 0.0\%$).

---

## 4. BEHAVIORAL & OPERATIONAL MECHANISMS

### 4.1 The Hub Disconnect (Connecting Passenger Shielding)
* At fortress hub airports (e.g., DFW, DTW, IAH), between 50.7% and 76.0% of departing passengers arrive via inbound connecting flights and transfer entirely airside.
* Treating total scheduled departing seats as landside demand overestimates security screening requirements by **up to 2.5-fold**.
* Multiplying flight seats by $(1 - \text{ConnectingRatio})$ derived from quarterly BTS DB1B coupons eliminates this structural bias, aligning scheduled capacity with originating passenger demand.

### 4.2 Lead-Lag Asynchrony Mechanism
A fundamental finding of this thesis is the empirical decoupling of passenger screening demand from flight departure delays across the operating day:

```
       [ MORNING SURGE: 05:00 - 08:00 ]                  [ EVENING CASCADE: 14:00 - 22:00 ]
     ───────────────────────────────────              ───────────────────────────────────
     • Checkpoint Demand: MAXIMUM                     • Checkpoint Demand: MODERATE / DECAYING
     • Screening Volatility: σ_TSA > 11,380/hr        • Screening Volatility: LOW / STABLE
     • Flight Delays: MINIMAL (< 5 min)               • Flight Delays: PEAK (σ_Delay > 63 min)
     • Schedule Buffer: Fresh, unexhausted            • Schedule Buffer: Completely exhausted across NAS
```

* **Morning Phase**: High screening arrival volatility driven by outbound bank departures adhering to ACRP Report 40 lognormal show-up curves (passengers arriving 90–120 minutes prior to departure).
* **Evening Phase**: High flight delay dispersion driven by aircraft turnaround propagation across the National Airspace System.
* **Core Insight**: Checkpoint throughput is a **leading indicator** of gate departure activity; flight delay is a **lagging consequence** of network operations. Models assuming contemporaneous relationships fail ($R^2 < 0.20$).

### 4.3 The "Empty Checkpoint Fallacy"
* During severe summer convective weather, flights scheduled for 18:00 are delayed to 22:00.
* A pure machine learning model relying on shifted flight departures predicts that the screening checkpoint will be empty at 16:30.
* In reality, passengers arrived at the terminal according to their original flight schedules. The terminal lobby experiences extreme passenger dwell, gate-change re-screening, and crowding.
* Pure ML suffers severe under-prediction ($R_{\text{MASE}} = 2.14$).
* The Two-Stage State-Space Hybrid ($M_5$) resolves this fallacy through recursive innovation tracking ($e_t = y_t - C\hat{x}_{t|t-1}$), updating the latent queue state using live prior-hour throughput ($y_{t-1}$).

---

## 5. MASTER OPERATIONAL DECISION ARCHITECTURE

### 5.1 The Regime-Switched Gated Inference Engine

To operationalize the findings, airport operations centers should implement dynamic inference switching governed by the Coupled Volatility Index ($\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$):

```
                       [ INCOMING HOURLY INFERENCE REQUEST ]
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     [ Coupled Volatility < 30 ]                     [ Coupled Volatility ≥ 35 ]
     • 1_OFF_PEAK Seasons                            • 3_PEAK Summer Convective Storms
     • Midweek (Tue / Wed) Baseline                  • Monday Outbound / Sunday Return
     • Midday Steady Plateau (08:00–13:00)           • Dual Turbulence Peaks (05:00, 17:00)
                 │                                               │
                 ▼                                               ▼
       ┌───────────────────┐                           ┌───────────────────┐
       │   HistGBM (M3)    │                           │ Hybrid EKF (M5)   │
       │  Fast, Automated  │                           │ Dynamic Feedback  │
       │    MASE ≈ 0.60    │                           │  R_MASE ≤ 1.28    │
       └───────────────────┘                           └───────────────────┘
```

1. **Gate 1: Routine Regime ($\text{CVI} < 30$)**:
   - Routes inference to the Gradient-Boosted Count Regressor ($M_3$).
   - Provides superior point accuracy ($\text{MASE} \approx 0.60$) with sub-second execution overhead and full transparency.
2. **Gate 2: Disruption Regime ($\text{CVI} \ge 35$)**:
   - Routes inference to the Sequential Two-Stage State-Space Hybrid ($M_5$).
   - Activates recursive Kalman queue innovations using live throughput ($y_{t-1}$), suppressing the "empty checkpoint fallacy" and maintaining $R_{\text{MASE}} \le 1.28$.
3. **Hysteresis Band ($30 \le \text{CVI} < 35$)**:
   - Preserves the previous hour's operational state to prevent rapid toggling between model architectures.

---

## 6. EMPIRICAL CROSS-PROJECT SYNTHESIS (PROJECTS 1, 2, AND 3)

The graduate research portfolio integrates three complementary computational paradigms to achieve robust tri-modal validation:

### 6.1 Project 1: Supervised Machine Learning & Conformed Warehouse
* Evaluated six candidate architectures ($M_0$ through $M_5$) across 270,460 modeled observations.
* Proved that incorporating ACRP Report 40 distributed passenger show-up curves elevates explanatory power from $R^2 = 0.5293$ (contemporaneous) to $R^2 = 0.7081$ (lead-lag).
* Demonstrated that Champion Model $M_5$ achieves $R^2 = 0.6270, \text{RMSE} = 1135.0, \text{MASE} = 0.846$ on the untouched 2025 out-of-time holdout dataset.

### 6.2 Project 2: First-Principles Queuing Simulation & Dynamic Lane Allocation
* Simulated queuing dynamics across 955 screening lanes at Detroit Metropolitan (DTW McNamara Terminal).
* Proved that under nominal operations, matching active lanes to incoming passenger banks maintains low average wait times ($\mu_{\text{wait}} = 0.9\text{ min}, P_{95} \le 7.7\text{ min}$).
* Exposed the failure of static lane allocations during severe disruptions (50% lane outage combined with flight surge), where wait times capped at 60 minutes and delay reached 27,763 passenger-hours.
* Proved that the **Dynamic Hybrid Allocation Model** slashes cumulative passenger delay by **80.1%** (reducing delay to 5,514 passenger-hours and capping 95th-percentile wait times at 11.5 minutes) by dynamically mobilizing reserve screening capacity.

### 6.3 Project 3: Dynamic State-Space Modeling & Spatial Generalizability
* Deployed recursive state-space tracking (Extended Kalman Filter) across matched airport pairs sharing identical airspace (EWR $\to$ LGA in New York TRACON).
* Demonstrated that while naive moving horizon baselines degraded by +86.7% ($\text{RTR} = 1.86$) and probabilistic sequence models degraded by +43.8% ($\text{RTR} = 1.44$), the **Extended Kalman Filter State-Space Hybrid achieved absolute transfer stability ($\Delta = 0.0\%, \text{RTR} = 1.00$ on EWR $\to$ LGA; $\text{RTR} = 0.86$ on DTW $\to$ PHL)**.
* Validated that recursive innovation feedback ($e_t = y_t - C\hat{x}_{t|t-1}$) enables seamless cross-airport portability without site-specific retraining.

---

## 7. TERMINOLOGY & GOVERNANCE RULES

Strictly enforce `thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`:
* **Use**: "Empirical Passenger Show-Up Curve" (or "Lead-Lag Passenger Arrival Distribution"). **Never use**: "physics-based continuous arrival kernel convolution".
* **Use**: "Carrier Checkpoint Isolation". **Never use**: "orthogonal Wiener-Hopf deconvolution operator".
* **Use**: "Connecting Passenger Deflator" (or "The Hub Disconnect"). **Never use**: "DB1B transfer deflation manifold".
* **Use**: "Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability". **Never use**: "cyber-physical stability manifolds".
* **Use**: "Regime-Switched Gated Inference Engine". **Never use**: "multi-agent cybernetic orchestrator".

---

## 8. CROSS-CHAPTER INTEGRATION ROADMAP

* **Handoff from Chapter I**: Chapter I introduces the primary research question and hypothesis $H_1$; Chapter V delivers the final verdict confirming $H_{1a}, H_{1b}$, and $H_{1c}$.
* **Handoff from Chapter II**: Chapter II critiques past modeling silos; Chapter V synthesizes how hybrid state-space models resolve those historical limitations.
* **Handoff from Chapter III**: Chapter III specifies the three evaluation metrics; Chapter V analyzes their trade-offs across the 84-cell interaction grid.
* **Handoff from Chapter IV**: Chapter IV presents the empirical benchmark results; Chapter V interprets their operational meaning, exposes the "empty checkpoint fallacy," and defines the Regime-Switched Gated Inference Engine.

====================================================================================================
END OF CHAPTER V SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
