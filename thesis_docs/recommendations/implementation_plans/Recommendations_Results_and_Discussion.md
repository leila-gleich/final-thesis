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
  * Interpret physical mechanics, evaluate performance trade-offs across Routine Operational Accuracy, Resilience Under Disruption, and Cross-Airport Transferability, and synthesize policy recommendations.

### 2.2 Highlight Key Quantitative Artifacts
When presenting Chapter IV in manuscript or defense slides, prioritize these core empirical benchmarks:
1. **Data Health Census**: 67.22M raw fact records cleaned to 42.06M post-ETL records across 25 airfields, with 100% referential integrity and 35.8k malformed records remediated.
2. **The Hub Disconnect**: Demonstrating that total departing seat capacity overpredicts landside security demand by >200% at connecting hubs (e.g., Charlotte CLT 76% connecting ratio; Dallas DFW 56% connecting ratio).
3. **Econometric Exclusivity Proofs**: Volume Conservation ($\rho = 1.00 \pm 0.04$), Zero-Flight Intercept ($\beta_0 = 12.4$ pax/hr, $p=0.40$), and Cross-Carrier Orthogonality ($\beta_{\text{other}} = 0.002, p=0.62$).
4. **Passenger Show-Up Curve Estimation**: Contemporaneous flights explain $<20\%$ of variance ($R^2 = 0.1988$), whereas 2-hour lead passenger show-up curves interacted with T-100 load factors achieve $R^2 = 0.4985$ (citing ACRP Report 40).
5. **Out-of-Time Benchmark Matrix**: 2025 holdout performance comparing Deterministic Naive ($R^2 = 0.4508$), Rebuilt Deterministic 2-Hr Static Lead ($R^2 = 0.5293, \text{MASE} = 0.942$), LightGBM Tweedie ($R^2 = 0.5880, \text{MASE} = 0.910$), and Sequential SARIMA-Tree Hybrid ($R^2 = 0.6270, \text{MASE} = 0.846$).

---

## 3. Academic Recommendations for Chapter V (Discussion & Interpretation)

### 3.1 Structure Analysis Around the Three Core Evaluation Dimensions

#### Dimension 1: Robustness (Routine Operational Accuracy)
* **Finding**: Supervised Machine Learning (Model 2) and Dynamic Two-Stage Hybrids (Model 3) achieved $\text{MASE}_{\text{routine}} \le 0.700$ and $0.662$ under nominal operational conditions, significantly outperforming the Deterministic Flight Schedule Model (Model 1: $\text{MASE} = 0.945$; Diebold-Mariano $DM = 42.15$ and $48.72, p < 0.0001$).
* **Interpretation**: Non-parametric tree models excel at capturing complex diurnal seasonality, day-of-week interactions, and non-linear aircraft seating capacity distributions without rigid parametric distributional assumptions.

#### Dimension 2: Resilience Under Disruption (Shock Absorption & Dynamic Recovery)
* **Finding**: During severe operational disruptions (severe convective storms and ground delay programs), pure ML models suffered acute degradation ($R_{\text{MASE}} = 2.14$). In contrast, the **Dynamic Two-Stage Hybrid Framework (Model 3)** maintained resilience ($R_{\text{MASE}} = 1.05$).
* **Interpretation**: When flights are delayed past midnight, pure ML models falsely predict empty checkpoints because future gate push-backs vanish from the schedule. Live error innovation feedback ($t-1$) corrects for latent passenger dwell, reducing recovery time to 2.8 hours.

#### Dimension 3: Generalizability (Cross-Airport Transferability)
* **Finding**: Complex tree models suffered error surges on zero-shot transfer across terminal layouts. Deterministic flight schedule baselines (Model 1: +4.0%, $\text{RTR} = 1.04$) and Supervised ML (Model 2: +8.3%, $\text{RTR} = 1.08$) maintained high transferability, while the Dynamic Hybrid (Model 3) experienced elevated transfer degradation (+21.5%, $\text{RTR} = 1.19$) due to terminal geometry overfitting.
* **Interpretation**: Over-parameterized models overfit to terminal-specific gate topologies and local carrier departure bank timing. Grounding demand in empirical passenger show-up curves decouples terminal layout specifics from macro schedule dynamics.

---

## 4. Practical & Operational Recommendations for TSA & Airport Authorities

1. **Adopt Empirical 2-Hour Lead Passenger Show-Up Schedules**:
   * TSA Checkpoint TSO (Transportation Security Officer) staffing schedules should replace static time-of-day templates with empirical 2-hour lead passenger show-up curves based on flight bank timing (peaking 90–120 minutes prior to departure, per ACRP Report 40).
2. **Dynamically Integrate Airline O&D Survey Ratios**:
   * Centralized security operations centers should dynamically scale passenger demand estimates using BTS DB1B connecting ratios to avoid over-allocating screening lanes at connecting hub fortresses.
3. **Deploy Two-Stage Hybrid Estimators**:
   * Operational control centers should implement two-stage hybrid models that rely on machine learning for routine staffing while incorporating physical queue feedback during convective ground stop disruptions.

---

## 5. Thesis Defense Presentation & Slide Recommendations

### Slide Deck Architecture (20–25 Slides)
* **Slides 1–3**: Title, Research Problem, Thesis Objectives & Scope.
* **Slides 4–6**: Multi-Source Federal Data Foundation & Referential Integrity.
* **Slides 7–9**: **Top 25 Operational Clustering (PCA + K-Means)** & The Hub Disconnect.
* **Slides 10–12**: **Four-Tiered Purposive Filtering Pipeline** & 9-Airport Factorial Grid.
* **Slides 13–15**: Econometric Carrier Checkpoint Isolation Proofs & Empirical Passenger Show-Up Curves.
* **Slides 16–18**: 2025 Holdout Benchmark Matrix (Model Execution Results).
* **Slides 19–21**: Comparative Analysis (Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability).
* **Slides 22–24**: Strategic Policy Recommendations & Practical Implementation.
* **Slide 25**: Conclusion & Q&A.

### Key Defense Talking Points
* *"By isolating carrier-exclusive screening lanes, we eliminated multi-carrier collinearity ($\kappa < 25$), enabling clean econometric mapping of flight schedules to checkpoint queues."*
* *"Evaluating models across a full 12-month out-of-time holdout dataset (2025) ensures zero temporal data leakage and proves real-world generalizability."*
* *"While pure machine learning wins on routine operational accuracy, two-stage hybrid models are essential for operational resilience during extreme weather disruptions."*
