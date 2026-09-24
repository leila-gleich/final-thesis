# Recommendations for Results & Discussion (Academic & Operational Guide)

## 1. Executive Summary & Purpose

This document provides actionable guidance for presenting, defending, and utilizing the empirical results and analysis of the graduate thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*. It establishes best practices for academic presentation, manuscript drafting, committee defense, and practical implementation by TSA and airport authorities.

---

## 2. Academic Recommendations for Chapter IV (Results Presentation)

### 2.1 Maintain Strict Separation Between Findings and Analysis
* **Chapter IV Purpose**: Answer *"What do the conformed data and model runs factually demonstrate?"*
  * Present baseline descriptive statistics, data health censuses, filtering funnel tables, econometric test metrics, and benchmark output tables.
  * Avoid speculative interpretations or operational rationale in Chapter IV; present unvarnished quantitative evidence.
* **Chapter V Purpose**: Answer *"What do these findings mean for thesis hypotheses, evaluation measures, and airport operations?"*
  * Interpret physical mechanics, evaluate performance trade-offs across Robustness, Resilience, and Generalizability, and perform formal hypothesis testing.

### 2.2 Rebuilt Deterministic Baseline (M1) vs. Probabilistic ML (M3)
* **Deterministic Baseline (M1 — Rebuilt 2-Hour Static Lead)**:  
  Reflects standard airport planning practice by applying a rigid, static 2-hour pre-departure arrival shift ($t+2$) to scheduled flight seats. Assumes constant average load factor and zero stochastic volatility modeling ($R^2 = 0.5293, \text{MASE} = 0.942$).
* **Probabilistic / Data-Driven ML (M3 — Stochastic Volatility Modeling)**:  
  Models passenger arrivals as a continuous stochastic probability distribution ($\tau \sim \text{Lognormal}$), incorporating load factor variance, route-level seat distributions, and lagged operational flight delays via Tweedie deviance ($p=1.3$) ($R^2 = 0.5880, \text{MASE} = 0.910$).
* **Dynamic Hybrid Framework (M5 — State-Space Cyber-Physical Model)**:  
  Combines the static schedule trend with dynamic state-space error feedback ($R^2 = 0.6270, \text{MASE} = 0.846$).

### 2.3 Core Quantitative Benchmarks for Presentation
1. **Data Health Census**: 67.22M raw fact records reduced to 42.06M conformed records across 25 airfields, with 100% referential integrity and 35.8k malformed records remediated.
2. **Connecting Ratio Paradox**: Demonstrating that total departing seat capacity overpredicts landside security demand by >200% at connecting hubs (e.g., Charlotte CLT 76% connecting ratio; Dallas DFW 56% connecting ratio).
3. **Econometric Exclusivity Proofs**: Volume Conservation ($\rho = 1.00 \pm 0.04$), Zero-Flight Intercept ($\beta_0 = 12.4$ pax/hr, $p=0.40$), and Cross-Carrier Orthogonality ($\beta_{\text{other}} = 0.002, p=0.62$).
4. **Lead-Lag Deconvolution**: Contemporaneous flights explain $<20\%$ of variance ($R^2 = 0.1988$), whereas 2-hour convolved lead flights interacted with T-100 load factors achieve $R^2 = 0.4985$.
5. **Out-of-Time Benchmark Matrix (2025 Holdout)**:
   * Naive Persistence M0 ($R^2 = 0.4508, \text{MASE} = 1.000$)
   * Rebuilt Deterministic M1 ($R^2 = 0.5293, \text{MASE} = 0.942$)
   * Stochastic Probabilistic ML M3 ($R^2 = 0.5880, \text{MASE} = 0.910$)
   * Sequential SARIMA-Tree Hybrid M5 ($R^2 = 0.6270, \text{MASE} = 0.846$)

---

## 3. Academic Recommendations for Chapter V (Discussion & Interpretation)

### 3.1 Structure Analysis Around the Three Core Evaluation Dimensions

#### Dimension 1: Robustness (Continuous Static Stability)
* **Finding**: Supervised Machine Learning (LightGBM Tweedie) and Sequential Hybrids achieved $\text{MASE}_{\text{routine}} \sim 0.83\text{--}0.89$ under nominal operational conditions, outperforming the rebuilt deterministic baseline ($\text{MASE} = 0.942$).
* **Interpretation**: The jump from M1 ($R^2 = 0.5293$) to M3 ($R^2 = 0.5880$) directly isolates **the incremental value of modeling stochastic passenger arrival distributions, route load factor volatility, and non-linear feature interactions**.

#### Dimension 2: Resilience (Shock Absorption & Dynamic Recovery)
* **Finding**: During severe operational disruptions (Winter Storm Elliott in December 2022), pure ML models suffered acute degradation ($R_{\text{MASE}} = 2.14$). In contrast, the **Dynamic Hybrid Framework** maintained resilience ($R_{\text{MASE}} = 1.28$).
* **Interpretation**: When flights are delayed past midnight, pure ML models falsely predict empty checkpoints because future gate push-backs vanish from the schedule. Dynamic state-space models and queue feedback loops ($t-1$) correct for latent passenger dwell, reducing recovery time from 8.4 hours to 3.2 hours.

#### Dimension 3: Generalizability (Zero-Shot Spatial Transferability)
* **Finding**: Deep neural networks suffered a +48.2% error surge on zero-shot transfer across terminal layouts. Rebuilt Deterministic Baselines (+4.4%) and Physics-Informed Hybrids (+7.9%) maintained high transferability ($\text{RTR} \sim 1.04\text{--}1.08$).
* **Interpretation**: Over-parameterized models overfit to terminal-specific gate topologies and local carrier departure bank timing. Physics-based representations of passenger arrival distributions decouple terminal layout specifics from macro schedule dynamics.

---

## 4. Practical & Operational Recommendations for TSA & Airport Authorities

1. **Adopt Convolved 2-Hour Lead Demand Schedules**:
   * TSA Checkpoint TSO staffing schedules should replace static time-of-day templates with convolved 2-hour lead-lag flight bank demand schedules to anticipate passenger surges before gate push-backs occur.
2. **Dynamically Integrate Airline O&D Survey Ratios**:
   * Centralized security operations centers should dynamically scale passenger demand estimates using BTS DB1B connecting ratios to avoid over-allocating screening lanes at connecting hub fortresses.
3. **Deploy Gray-Box Hybrid State-Space Estimators**:
   * Operational control centers should implement Extended Kalman Filter state-space hybrids that rely on machine learning for routine staffing while reverting to physical queue conservation during convective ground stop disruptions.

---

## 5. Thesis Defense Presentation & Slide Recommendations

### Key Defense Talking Points
* *"We rebuilt the deterministic planning baseline (M1) using a static 2-hour pre-departure shift ($t+2$), reflecting real-world airport master planning. This isolated the exact value of stochastic probability modeling ($R^2 = 0.5880$ vs $0.5293$)."*
* *"By filtering down to carrier-exclusive screening lanes, we eliminated multi-carrier collinearity ($\kappa < 25$), enabling orthogonal Wiener-Hopf deconvolution of passenger arrival kernels."*
* *"Evaluating models across a full 12-month out-of-time holdout dataset (2025) ensures zero temporal data leakage and proves real-world generalizability."*
* *"While pure machine learning wins on static steady-state accuracy, dynamic hybrid state-space models are mandatory for operational resilience during extreme weather shocks."*
