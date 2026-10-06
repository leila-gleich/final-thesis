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
│   ├── Benchmark Matrix: Model 1 (0.945 MASE) vs. Model 2 (0.680–0.700 MASE) vs. Model 3 (0.662 MASE, DM = 48.72)
│   ├── Evaluation of Hypothesis H_1a (Routine Non-Linear Accuracy)
│   └── 5.3.1 Robustness Across the 84-Cell Grid & Prevention of Weather Delay Distortion
├── 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience Under Disruption
│   ├── Benchmark Matrix: Model 1 (1.32 R_MASE) vs. Model 2 (2.14 R_MASE) vs. Model 3 (0.694 MASE, 1.05 R_MASE)
│   ├── Severe Disruption Degradation (Pure ML R_MASE = 2.14 vs. Hybrid = 1.05)
│   ├── Kaplan-Meier Time-to-Recovery (Hybrid TTR = 2.8h vs. ML = 5.4h vs. Deterministic = 7.8h)
│   ├── Evaluation of Hypothesis H_1b (Hybrid Resilience Under Shock)
│   └── 5.4.1 Resilience Mechanics and the "Empty Checkpoint Fallacy" vs. Live Innovation Feedback
├── 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Cross-Airport Transferability)
│   ├── Benchmark Matrix: Model 1 (+4.2%, RTR = 1.04) vs. Model 2 (+7.9%, RTR = 1.08) vs. Model 3 (+19.0%, RTR = 1.19)
│   ├── Decision Tree Overfitting & Failure (Δ = +21.5%)
│   ├── Zero-Shot Facility Portability (EWR → LGA: Model 1 RTR = 1.04; DTW → PHL: RTR = 1.003)
│   ├── Evaluation of Hypothesis H_1c (Structural Portability)
│   └── 5.5.1 Generalizability via Standardized Flight Schedules
├── 5.6 Master Synthesis and Operational Recommendations
│   ├── Cross-Dimensional Paradigm Evaluation Matrix
│   ├── 5.6.1 The Regime-Switched Gated Inference Engine (CVI < 30 vs. CVI ≥ 35)
│   └── 5.6.2 Strategic Implications for TSA and Airport Authorities
└── 5.7 The Values versus Volatility Paradigm Across Temporal Horizons
    ├── Rolling Multi-Day Volatility (Feature Values R^2 < 0 vs. Feature Volatility R^2 > 0.31)
    ├── Flight Departure Delay Volatility Transmission (CV_delay r = +0.4373, p = 0.0288)
    └── Master Factor Importance Hierarchy (Schedule 64.5%, Cancels 16.5%, Buffers 7.9%, Delays 7.0%)
```

---

## 3. MASTER SYNTHESIS & HYPOTHESIS EVALUATION REGISTRY

### 3.1 Evaluation of Overarching Thesis Hypothesis ($H_1$ - Master Asymmetric Trade-Off Matrix)

> **Core Hypothesis ($H_1$)**: Across the candidate forecasting paradigms evaluated following four-tiered purposive filtering (baseline control, deterministic flight schedule baseline, supervised machine learning, and dynamic two-stage hybrid), **no individual architecture will prove universally superior across all three evaluation dimensions**. Rather, inherent operational properties establish stark, asymmetric trade-offs across robustness, resilience, and generalizability.

The empirical findings **decisively confirm** $H_1$, as summarized in the master asymmetric trade-off matrix:

| Evaluation Dimension | Stated Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Dimension Winner & Justification |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** (Routine: Delay $< 15$m, 0 Cancels) | Lowest $\text{RMSE}_{\text{routine}}$; $\text{MASE}_{\text{routine}} < 0.70$ | $\text{RMSE} = 253.6$, $\text{MASE} = 1.000$ (Fails) | $\text{RMSE} = 313.4$, $\text{MASE} = 0.945$ (Fails) | $\text{RMSE} = 273.5$, $\text{MASE} = 0.680\text{--}0.700$ (**Target Met**) | $\text{RMSE} = \mathbf{222.1}$ (Lowest), $\text{MASE} = \mathbf{0.662}$ (**Target Met**) | **Model 3 achieves lowest RMSE**; **Model 2 wins Routine Pareto Efficiency** (meets target with zero online compute overhead). |
| **Dimension 2: Resilience** (Disruption: Delay $\ge 45$m or Cancels $\ge 5$) | $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$ | $R = 1.00$, $\text{MASE} = 1.000$, $\text{TTR} = 8.4\text{h}$ | $R = 1.32$, $\text{MASE} = 1.082$, $\text{TTR} = 7.8\text{h}$ | $R = 2.14$ (Fragile), $\text{MASE} = 0.812$, $\text{TTR} = 5.4\text{h}$ | $R = \mathbf{1.05}$ (**Target Met**), $\text{MASE} = \mathbf{0.694}$ (Lowest), $\text{TTR} = \mathbf{2.8\text{h}}$ (**Target Met**) | **Model 3 DECISIVE WINNER**: Closed-loop live feedback ($e_{t-1}$) prevents empty-checkpoint collapse and recovers in 2.8h. |
| **Dimension 3: Generalizability** (Zero-Shot Transfer: EWR $\to$ LGA) | $\text{RTR} = 1.00$; $\Delta\text{MASE} \le 10.0\%$ | $\text{RTR} = 1.00$, $\Delta\text{MASE} = 0.0\%$ (Static Ref) | $\text{RTR} = \mathbf{1.04}$ (**Target Met**), $\Delta\text{MASE} = \mathbf{+4.0\%}$ (**Target Met**) | $\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\%$ (Passes) | $\text{RTR} = \mathbf{1.19}$ (**FAILS TARGET**), $\Delta\text{MASE} = \mathbf{+21.5\%}$ (**FAILS TARGET**) | **Model 1 DECISIVE WINNER**: Physical schedule convolution is invariant to facility layout; Model 3 overfits to local gate geometry. |

### 3.2 Sub-Hypothesis Verification Proofs

1. **Sub-Hypothesis $H_{1a}$ (Robustness Target: Lowest $\text{RMSE}_{\text{routine}}$ and $\text{MASE}_{\text{routine}} < 0.700$)**:
   - *Hypothesis Statement*: Non-linear machine learning models (Model 2) and two-stage hybrids (Model 3) will achieve the robustness target ($\text{MASE}_{\text{routine}} < 0.700$), outperforming linear and persistence baselines.
   - *Empirical Proof*: Confirmed. Model 3 achieves $\text{MASE}_{\text{routine}} = 0.662$ ($\text{RMSE} = 222.1\text{ pax/hr}$), and Model 2 achieves $\text{MASE}_{\text{routine}} = 0.680\text{--}0.700$ ($\text{RMSE} = 273.5\text{ pax/hr}$), compared to Model 1 at $\text{MASE} = 0.945$ and Baseline Control at $\text{MASE} = 1.000$. Diebold-Mariano tests confirm statistical significance ($DM = 48.72, p < 0.0001$ for Model 3; $DM = 42.15, p < 0.0001$ for Model 2). Model 2 provides the optimal Routine Pareto solution.

2. **Sub-Hypothesis $H_{1b}$ (Resilience Target: $R \approx 1.00$, Lowest $\text{MASE}_{\text{shock}}$, and $\text{TTR} < 4.0\text{ hours}$)**:
   - *Hypothesis Statement*: The Dynamic Two-Stage Hybrid (Model 3) will be the sole architecture to satisfy the resilience target ($R \approx 1.00, \text{TTR} < 4.0\text{h}$), resisting the "empty checkpoint fallacy" that degrades pure machine learning during flight delay cascades.
   - *Empirical Proof*: Confirmed. Under acute disruption ($\text{Delay} \ge 45\text{m}$ or $\text{Cancels} \ge 5$), pure ML (Model 2) collapses into fragility ($R = 2.14, \text{TTR} = 5.4\text{ hours}$). The Dynamic Hybrid maintains $R_{\text{MASE}} = 1.05 \approx 1.00$, lowest shock error ($\text{MASE}_{\text{shock}} = 0.694$), and recovers in **2.8 hours** ($\le 4.0\text{ hours}$), driven by recursive 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$).

3. **Sub-Hypothesis $H_{1c}$ (Generalizability Target: $\text{RTR} \approx 1.00$ and $\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$)**:
   - *Hypothesis Statement*: The Deterministic Flight Schedule Model (Model 1) will decisively satisfy the generalizability target, whereas the Dynamic Hybrid (Model 3) will decisively fail the target due to terminal geometry overfitting.
   - *Empirical Proof*: Confirmed. Zero-shot transfer from EWR Terminal C to LGA Terminal C shows Model 1 achieving $\text{RTR} = 1.04 \approx 1.00$ and $\Delta\text{MASE} = +4.0\% \le 10.0\%$ (penalty $+4.2\%$). In sharp contrast, Model 3 fails both targets ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$, penalty $+19.0\%$) because decision tree residual splits overfit to Newark's terminal geometry and carrier bank timings. This proves that Model 3 does not universally dominate and confirms the asymmetric trade-off thesis.

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
* The Dynamic Two-Stage Hybrid Model (Model 3) resolves this fallacy through live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$), updating the forecast using live prior-hour throughput from the checkpoint floor.

---

## 5. MASTER OPERATIONAL DECISION ARCHITECTURE

### 5.1 The Regime-Switched Gated Inference Engine: The Airport Operator's Playbook

To operationalize the findings, airport operations centers should implement dynamic inference switching governed by the Turbulence Shock Index $T(h)$ or Coupled Volatility:

```
                       [ INCOMING HOURLY INFERENCE REQUEST ]
                                         │
                 ┌───────────────────────┴───────────────────────┐
                 ▼                                               ▼
     [ Turbulence Shock Index T(h) < 0.75 ]          [ Turbulence Shock Index T(h) ≥ 0.75 ]
     • 1_OFF_PEAK Seasons                            • 3_PEAK Summer Convective Storms
     • Midweek (Tue / Wed) Baseline                  • Monday Outbound / Sunday Return
     • Midday Steady Plateau (08:00–13:00)           • Acute Flight Delays (σ_Delay > 45 min)
                 │                                               │
                 ▼                                               ▼
       ┌───────────────────┐                           ┌───────────────────┐
       │      Model 2      │                           │      Model 3      │
       │ Supervised ML Tree│                           │ Dynamic Hybrid    │
       │  Fast, Automated  │                           │ Live Innovation   │
       │  MASE = 0.68-0.70 │                           │  R_MASE = 1.05    │
       └───────────────────┘                           └───────────────────┘
```

1. **Gate 1: Routine Flow Track ($T(h) < 0.75$)**:
   - Routes inference to the **Supervised Machine Learning Model (Model 2)**.
   - Provides superior point accuracy ($\text{MASE} = 0.680\text{--}0.700$) with near-zero computational overhead and high spatial portability ($RTR = 1.08$).
2. **Gate 2: Tactical Shock Track ($T(h) \ge 0.75$)**:
   - Routes inference to the **Dynamic Two-Stage Hybrid Model (Model 3)**.
   - Activates live 1-step error innovation feedback ($e_{t-1} = y_{t-1} - \hat{y}_{t-1}$) from the checkpoint screening floor, resolving the "empty checkpoint fallacy" and maintaining resilient performance ($R_{\text{MASE}} = 1.05, \text{TTR} = 2.8\text{h}$).

---

## 6. EMPIRICAL VALIDATION ACROSS RESEARCH PILLARS

The thesis findings demonstrate cohesive empirical validation across three foundational analytical pillars:

### 6.1 Pillar 1: Empirical Volatility Forecasting & Holdout Evaluation
* Benchmarked candidate model architectures across 72,053 complex-level observations on the untouched 2025 out-of-time holdout dataset.
* Proved that incorporating ACRP Report 40 distributed passenger show-up curves ($t+1, t+2, t+3$) elevates explanatory power from $R^2 = 0.1158$ (unshifted schedule) to $R^2 = 0.4985$ (convolved load-factor weighted schedule).
* Demonstrated that Champion Model 3 achieves $R^2 = 0.7483, \text{RMSE} = 222.1\text{ pax/hr}, \text{MASE} = 0.662$ on holdout data, beating daily persistence by 33.8%.

### 6.2 Pillar 2: Heavy-Traffic Queuing Physics & Conformal Staffing Buffers
* Grounded checkpoint congestion in Kingman's heavy-traffic formula ($W_q \propto C_a^2$).
* Proved that as screening lanes approach capacity ($\rho \to 0.90$), arrival volatility generates exponential queue spikes.
* Operationalized conformal quantile bounds ($\hat{y}_{0.85}$) to size dynamic staffing buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$), capping lane utilization below runaway tipping points.

### 6.3 Pillar 3: Cross-Airport Spatial Generalizability
* Deployed models zero-shot without local retraining from Newark Liberty (EWR Terminal C) to New York LaGuardia (LGA Terminal C), holding TRACON regional airspace constant.
* Confirmed that the **Deterministic Flight Schedule Model (Model 1)** achieves near-perfect spatial transfer ($\text{RTR} = 1.04, \Delta\text{MASE} = +4.0\%$), and $\text{RTR} = 1.003$ on DTW $\to$ PHL, proving that physical flight schedule convolution is invariant across airport geometries.
* Confirmed that the **Dynamic Hybrid (Model 3)** fails zero-shot transfer ($\text{RTR} = 1.19, \Delta\text{MASE} = +21.5\%$) due to decision tree terminal geometry overfitting, proving Hypothesis $H_{1c}$.

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
