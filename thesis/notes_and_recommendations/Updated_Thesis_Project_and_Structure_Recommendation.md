# Master Thesis Project & Chapter Structure Recommendation

**Project Title**: *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: TSA Checkpoint Throughput Forecasting & Airside-Landside Queue Dynamics*  
**Author**: Leila Gleich  
**Degree**: Master of Science in Aeronautics (MSAA) / Aviation Data Analytics  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Primary Research Codebase**: `final-thesis/`  
**Manuscripts & Supporting Documentation**: `Gleich-Thesis/`  
**Date**: September 28, 2026  

---

## Executive Summary & Core Architectural Strategy

This document provides the definitive, updated architectural recommendation for the graduate thesis project structure, data integration pipeline, and formal chapter organization.

The thesis evaluates three distinct modeling paradigms:
1. **Deterministic Baselines** (M0 Diurnal Seasonal Naive, M1 Rebuilt 2-Hour Static Lead Schedule)
2. **Probabilistic / Supervised Machine Learning** (M2 Convolved Density, M3 LightGBM Tweedie Deviance)
3. **Cyber-Physical Hybrids** (M5 Sequential SARIMA-Tree, State-Space Digital Twin)

These models are rigorously evaluated across **three core operational dimensions**:
* **Dimension 1: Robustness** (Routine steady-state accuracy, nominal operations, departure delays $< 15\text{ min}$, $\text{MASE}_{\text{routine}}$).
* **Dimension 2: Resilience** (Tactical shock absorption, extreme weather disruptions, delays $> 45\text{ min}$, $R_{\text{MASE}} = \text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$, Time-to-Recovery $\text{TTR}$).
* **Dimension 3: Generalizability** (Zero-shot spatial transferability across terminal physical geometries and airport operational clusters, $\Delta \text{MASE}_{\text{transfer}}$, $\text{RTR}$).

To satisfy both ERAU academic committee standards and operational utility for TSA Federal Security Directors (FSDs), the results and discussion are partitioned across **two dedicated chapters**:
* **Chapter IV (Empirical Findings)**: Answers *"What do the conformed data and model runs factually show?"* It strictly reports data censuses, filtering funnels, cluster statistics, econometric proofs, and benchmark metric tables without speculative interpretation.
* **Chapter V (Analysis, Discussion & Synthesis)**: Answers *"Why do models perform this way, and what does it mean for airport operations?"* It provides the physical and behavioral explanations, deep-dives into the three hypotheses, translates findings into staffing heuristics, and unifies the cross-project computational framework.

---

## 1. Master Thesis Five-Chapter Architecture

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        MASTER THESIS STRUCTURAL ARCHITECTURE                           │
└────────────────────────────────────────────────────────────────────────────────────────┘

  CHAPTER I: INTRODUCTION
  ├── 1.1 Problem Statement & Background (TSA Congestion & Schedule Disconnect)
  ├── 1.2 Purpose Statement & Research Questions (RQ1: Robustness, RQ2: Resilience, RQ3: Generalizability)
  ├── 1.3 Hypotheses (H1: ML Routine Superiority, H2: Hybrid Shock Resilience, H3: Physics Generalizability)
  ├── 1.4 Delimitations (9 Airports, Big 3 Carriers AA/DL/UA, May 1, 2022 Cutoff)
  ├── 1.5 Assumptions & Limitations (Top 25 Steady-State Assumption; Exclusive-Checkpoint Boundary)
  └── 1.6 Definition of Terms (Type I/II Exclusivity, MASE, RTR, TTR, Traffic Intensity ρ)

  CHAPTER II: REVIEW OF RELEVANT LITERATURE
  ├── 2.1 Airport Terminal Architectures & Queuing Networks (ACRP Report 25; de Neufville & Odoni)
  ├── 2.2 Passenger Arrival Distributions & Lead-Lag Dynamics (ACRP Report 40; Lognormal Kernel)
  ├── 2.3 Econometric Time Series vs. Machine Learning in Air Transportation
  ├── 2.4 Cyber-Physical & Physics-Informed Queueing Hybrids
  └── 2.5 Literature Synthesis & Identified Methodological Gaps

  CHAPTER III: METHODOLOGY
  ├── 3.1 Research Design & Conceptual Framework
  ├── 3.2 Multi-Source Data Engineering & Conformed ETL Pipeline (TSA, OTP, T-100, DB1B)
  ├── 3.3 Four-Tiered Purposive Filtering Pipeline (Macro, Meso, Micro, Factorial Symmetry)
  ├── 3.4 The 9-Airport Experimental Cohort Master Matrix & Spatial Boundary
  ├── 3.5 Temporal Scope: Network-Theoretic Post-Pandemic Demarcation (May 1, 2022 CUSUM/Chow)
  ├── 3.6 Econometric Validation of Carrier-Exclusive Checkpoints (Volume Conservation & KS Invariance)
  ├── 3.7 Feature Deconvolution & Passenger Show-Up Curve Convolution
  ├── 3.8 Model Architectures & Estimation Procedures (M0 through M5)
  └── 3.9 Multi-Metric Evaluation Framework (Robustness, Resilience, Generalizability Formulations)

  CHAPTER IV: FINDINGS (EMPIRICAL RESULTS)
  ├── 4.1 Master Descriptive Statistics & Data Health Census (67.22M Raw → 42.06M Cleaned)
  ├── 4.2 The Four-Tiered Purposive Filtering Pipeline (Funnel Counts & Factorial Balance)
  ├── 4.3 Empirical Operational Clusters (PCA & K-Means Archetypes 0, 1, 2, 3)
  ├── 4.4 Temporal Demarcation: Post-Pandemic Regime Selection Verification
  ├── 4.5 Econometric Validation of Checkpoint Exclusivity (Tests 1, 2, 3 & Layout Invariance)
  ├── 4.6 Feature Engineering & Lead-Lag Arrival Deconvolution Gradient
  └── 4.7 Master Model Benchmark Matrix (Full-Year 2025 Out-of-Time Holdout Execution)

  CHAPTER V: ANALYSIS, DISCUSSION, AND SYNTHESIS
  ├── 5.1 Physical and Behavioral Checkpoint Mechanics (Connecting Shielding, CAT Invariance)
  ├── 5.2 Initial Training and Passenger Show-Up Dynamics (Resolving the 90–120 Min Lag)
  ├── 5.3 Deep-Dive Dimension 1: Robustness (Routine Accuracy & DM Significance)
  ├── 5.4 Deep-Dive Dimension 2: Resilience (Shock Absorption During Winter Storm Elliott & TTR)
  ├── 5.5 Deep-Dive Dimension 3: Generalizability (Zero-Shot Cross-Terminal Transfer Matrix)
  ├── 5.6 Master Operational Recommendations for TSA & Airport Authorities (FSD Decision Heuristics)
  ├── 5.7 Empirical Cross-Project Synthesis (Supervised ML + Queueing Simulation + Digital Twin)
  ├── 5.8 Limitations of the Study
  └── 5.9 Recommendations for Future Research & Concluding Remarks
```

---

## 2. Comprehensive Blueprint for Chapter IV: Findings (Empirical Results)

> **Mandate**: Present verified, factual data artifacts without speculative interpretation. Every section is tied directly to companion workbooks in `final-thesis/results/`.

```
Chapter IV Content Flow:
  4.1 Data Census ──► 4.2 Filtering Funnel ──► 4.3 Cluster Profiles ──► 4.4 Temporal Demarcation 
         ──► 4.5 Econometric Tests ──► 4.6 Feature Lags ──► 4.7 2025 Holdout Benchmark Matrix
```

### 4.1 Master Descriptive Statistics and Data Health Census
* **Objective**: Establish the empirical validity and integrity of the conformed warehouse.
* **Empirical Scope**:
  * 67.22M raw upstream records cleaned to 42.06M conformed records across the 25 airfields.
  * Multi-source distribution: 3.13M checkpoint-hours (TSA), 10.28M domestic flight departures (BTS OTP across 294 destinations), 370.1k carrier-segment-months (BTS T-100 representing 1.09B seats), and 2.10M ticket coupons (BTS DB1B/DB1C).
* **Data Health Highlights**:
  * *Spatial Key Resolution*: Automated fingerprinting recovered 7,489 malformed TSA records; remaining 22,190 records mapped to surrogate key `airportId = 0` (preventing a 9.71M passenger artificial phantom airport).
  * *Structural Zeros*: 450,973 zero-throughput hours preserved (98.6% falling between 00:00 and 03:59 local time), modeled via Tweedie loss ($p=1.3$) rather than naive moving-average imputation.
  * *Causal Flight Departure Filtering*: Domestic flights retained only when departing from a thesis airport (all destination airports retained). Advance cancellations ($>24\text{h}$) purged; tactical cancellations ($<2\text{h}$) retained because passengers already cleared security.
* **Companion Deliverables**:
  * Table 4.1: *Conformed Data Warehouse Census & Entity Conformance Status*.
  * Table 4.2: *Summary Statistics for the 9-Airport Experimental Cohort (Post-May 2022)*.
  * Reference Workbook: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Census_Master`).

### 4.2 The Four-Tiered Purposive Filtering Pipeline
* **Objective**: Detail the sequential funnel that isolates unconfounded screening demand.
* **Funnel Stages**:
  1. *Macro Filter (Scale & Traffic Intensity)*: Restricting to Top 25 airfields captures 67.2% of national passengers, guaranteeing queue formation ($\rho(t) \to 1.0$) during peak departure banks.
  2. *Meso Filter (Shock Parity & WN Exclusion)*: Concurrent operations by American, Delta, and United subject all carriers to identical FAA Air Traffic Control ground stops. Southwest Airlines (WN) is excluded due to its bimodal arrival mixture ($\mu_1 \sim 135\text{ min}$, $\mu_2 \sim 65\text{ min}$) arising from open-seating boarding and free baggage policies.
  3. *Micro Filter (Carrier Checkpoint Isolation)*: Eliminating shared checkpoints collapses the collinear multi-carrier mixture ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$), reducing condition number from $\kappa > 10^4$ to $\kappa < 25$.
  4. *Factorial Symmetry*: Selecting the 9 airports provides exactly 4 dedicated checkpoints per carrier across 4 operational clusters and 4 terminal layouts.
* **Companion Deliverables**:
  * Table 4.3: *Four-Tiered Purposive Filtering Funnel Attrition Table*.
  * Table 4.4: *The 9-Airport Master Factorial Matrix (Carriers $\times$ Clusters $\times$ Terminal Archetypes)*.
  * Reference Workbook: `results/02_4tier_filtering/02_4tier_filtering.xlsx` and `02_top9_cohort_comprehensive_analysis.xlsx`.

### 4.3 Empirical Operational Clusters and Systemic Trends
* **Objective**: Present the unsupervised PCA and K-Means segmentation across the Top 25 commercial airfields.
* **Empirical Findings**:
  * Principal Components: PC1 (Scale & Congestion, 33.8% variance), PC2 (Gauge vs. Vulnerability, 25.5%), PC3 (Connecting Dominance, 17.7%)—cumulative 77.0% explained variance.
  * *Cluster 0 (Mega-Connecting Gateways, $n=8$)*: ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO. High volume (91.9M TSA), high connecting ratio (56.1%), heavy delay exposure (15.6 min).
  * *Cluster 1 (High-Density O&D Focus, $n=6$)*: AUS, BOS, CLT, DCA, IAH, TPA. Moderate volume (46.1M), high originating fraction, 83.4% load factor.
  * *Cluster 2 (High-Reliability Fortress Hubs, $n=8$)*: DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC. High connecting ratio (54.1%), exceptionally low delay propagation (11.6 min).
  * *Cluster 3 (Congested Coastal Originators, $n=3$)*: EWR, JFK, LGA. Severe delay burden (16.1 min, taxi-out 24.3 min), high load factor (85.4%), low connecting ratio (37.4%).
* **Companion Deliverables**:
  * Table 4.5: *PCA Component Loading Matrix Across Standardized Airport Attributes*.
  * Table 4.6: *Empirical Operational Cluster Profiles and Centroids*.
  * Figure 4.1: *Bi-plot of Top 25 Airfields in PC1-PC2 Feature Space with Cluster Assignments*.

### 4.4 Temporal Demarcation: Post-Pandemic Regime Selection
* **Objective**: Present statistical proof justifying the May 1, 2022 demarcation cutoff over Candidate A (January 1, 2023).
* **Empirical Tests**:
  * *Chow Test for Structural Stability*: The null hypothesis of parameter constancy ($H_0: \beta_{\text{pre}} = \beta_{\text{post}}$) is rejected across 2020 through Q1 2022 ($p < 0.0001$), but fails to reject ($p = 0.18$) beginning May 2022.
  * *CUSUM Residual Drift*: Standardized cumulative residuals stabilize within the control boundary ($|S_t| \le 4.2 < 5.0$) post-May 2022.
  * *Network-Wide Longitudinal Trends*: Time series plots of Top 25 monthly load factor ($84.6\% \pm 1.2\%$) and flight volume prove steady-state recovery across the network.
  * *Partitioning Strategy*: Training (May 1, 2022 – Dec 31, 2023; 404,324 obs), Validation (Jan 1, 2024 – Dec 31, 2024; full Q1–Q4 cycle), Holdout Test (Jan 1, 2025 – Dec 31, 2025; 215,562 obs) with 7-day purge embargoes.
* **Companion Deliverables**:
  * Table 4.7: *Comparative Evaluation of Training Demarcation Candidates A vs. B*.
  * Figure 4.2: *Top 25 Network-Level Longitudinal Recovery Profiles and CUSUM Trajectory (2019–2025)*.

### 4.5 Econometric Validation of Checkpoint Exclusivity
* **Objective**: Empirically validate that carrier-exclusive checkpoints isolate pure demand.
* **Statistical Proofs**:
  1. *Volume Conservation*: $\rho = \text{TSA}_{\text{actual}} / \text{Est}_{\text{originating}} = 1.00 \pm 0.04$ ($p < 0.001$).
  2. *Zero-Flight Intercept*: Regressing throughput on flight capacity yields intercept $\beta_0 = 12.4\text{ pax/hr}$ ($t = 0.84, p = 0.40$), confirming zero scheduled flights produce zero demand.
  3. *Cross-Carrier Orthogonality*: Non-tenant carrier flight parameter $\beta_{\text{other}} = 0.002$ ($p = 0.62$, partial $R^2 < 0.001$).
  4. *Layout Invariance (Type I vs. Type II)*: Kolmogorov-Smirnov test between hard air-gapped terminals (BOS, DTW, LGA, ORD, EWR) and connected concourses (LAX, DFW, IAH, PHL) yields $D = 0.032, p = 0.28$, confirming post-security airside leakage is statistically negligible.
* **Companion Deliverables**:
  * Table 4.8: *Econometric Validation of Carrier Checkpoint Exclusivity & Orthogonality*.
  * Reference Workbook: `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx`.

### 4.6 Feature Engineering and Lead-Lag Arrival Deconvolution
* **Objective**: Quantify the temporal relationship between airside departure times and landside screening queues.
* **Empirical Findings**:
  * Contemporaneous flight departures ($t$) explain only $R^2 = 0.1988$ of throughput variance.
  * Explanatory power peaks at lead horizon $t+2$ ($R^2 = 0.4054$, Pearson $r = 0.6367$, slope $= 74.98\text{ pax/flight}$).
  * Continuous lognormal arrival density convolution ($f_{\text{arr}}$) reaches $R^2 = 0.4878$.
  * Interacting convolved demand with BTS T-100 monthly segment load factors elevates baseline explanatory power to $R^2 = 0.4985$ ($r = 0.7061$, slope $= 90.56\text{ pax/flight}$).
* **Companion Deliverables**:
  * Table 4.9: *Explanatory Power of Flight Lead Horizons and Convolution Features*.
  * Figure 4.3: *Cross-Correlation Function (CCF) Between Scheduled Flight Departure Banks and Checkpoint Queues*.
  * Reference Workbook: `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx`.

### 4.7 Model Benchmark Matrix (2025 Full-Year Out-of-Time Holdout)
* **Objective**: Present final, unvarnished comparative performance on the 215,562 holdout observations.
* **Performance Summary Table**:

| Model Family | ID | Architecture & Features | Val $R^2$ | Test $R^2$ | Test RMSE | Test MAE | Test MASE |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: |
| **Deterministic Baseline** | M0 | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1377.3 | 939.8 | 1.000 |
| **Deterministic Baseline** | M1 | Rebuilt 2-Hr Static Lead ($t+2$) | 0.5312 | 0.5293 | 1265.4 | 902.1 | 0.942 |
| **Probabilistic / ML** | M2 | Convolved Lead Density Only | 0.5443 | 0.5862 | 1195.5 | 856.2 | 0.911 |
| **Probabilistic / ML** | M3 | LightGBM Tweedie ($p=1.3$) + OTP Delays | 0.5450 | **0.5880** | **1192.9** | **855.1** | **0.910** |
| **Probabilistic / ML** | M4 | Full Tri-Modal Pipeline (Convolved + OTP + LF) | 0.5798 | 0.5771 | 1208.6 | 856.3 | 0.911 |
| **Dynamic Cyber-Hybrid** | M5 | Sequential SARIMA-Tree Hybrid | **0.6644** | **0.6270** | **1135.0** | **795.0** | **0.846** |

* **Companion Deliverables**:
  * Table 4.10: *Master Model Benchmark Matrix on 2025 Holdout Data*.
  * Figure 4.4: *Comparative Observed vs. Forecasted Throughput Hydrographs Across Peak Operational Days*.
  * Reference Workbook: `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx`.

---

## 3. Comprehensive Blueprint for Chapter V: Analysis, Discussion, and Synthesis

> **Mandate**: Synthesize the findings, explain underlying behavioral and physical mechanisms, evaluate the three core hypotheses, and translate results into operational decision-support tools.

```
Chapter V Narrative Flow:
  5.1 Physical Mechanics ──► 5.2 Arrival Dynamics ──► 5.3 Dimension 1 (Robustness) 
         ──► 5.4 Dimension 2 (Resilience) ──► 5.5 Dimension 3 (Generalizability)
         ──► 5.6 TSA FSD Policy ──► 5.7 Cross-Project Triangulation ──► 5.8 Limitations & Future Work
```

### 5.1 Physical and Behavioral Checkpoint Mechanics
* **Deconstructing the Connecting Ratio Paradox**:
  * Explain why total scheduled departing seats overestimate landside passenger arrivals by $>200\%$ at hub fortresses (CLT 76%, DFW 56%, DTW 54%). 
  * Connecting passengers transfer concourse-to-concourse airside without passing through landside magnetometers. Multiplying scheduled seats by the BTS DB1B originating factor ($1 - C_i$) provides the necessary physical boundary correction.
* **Terminal Complex Aggregation**:
  * Address why lane-level forecasting fails: TSO dynamic lane switching (opening/closing PreCheck vs. standard lanes) introduces administrative noise. Aggregating across the terminal complex recovers a smooth, continuous demand signal.
* **Physical vs. Operational Dedication Invariance**:
  * Explain why Type II checkpoints (with airside secure connectors) behave identically to Type I (hard air-gapped terminals). Baggage re-check requirements, landside parking proximity, and CAT biometric boarding passes enforce strict passenger adherence to carrier-dedicated screening portals.

### 5.2 Initial Training and Passenger Show-Up Dynamics
* **Resolving Physical Lead-Lag Asynchrony**:
  * Passengers arrive 90 to 120 minutes prior to push-back (modal peak at $t+2$, validating ACRP Report 40).
  * Contemporaneous flights ($t$) correlate poorly ($R^2 < 0.20$) because passengers have already boarded.
* **Asymmetric Handling of Flight Delays**:
  * Tactical flight delays cannot be ingested contemporaneously without lookahead bias.
  * Prior-hour delays ($t-1$) serve as an effective proxy for apron congestion, passenger terminal dwell, and gate holdbacks.

### 5.3 Deep-Dive: Evaluation Dimension 1 – Robustness (Routine Operational Accuracy)
* **Statistical Evaluation**:
  * Under routine conditions ($\text{depDel} < 15\text{ min}$), Supervised ML (M3) and Dynamic Hybrids (M5) achieve $\text{MASE}_{\text{routine}} = 0.890$ and $0.834$, significantly outperforming the rebuilt deterministic baseline (M1: $\text{MASE} = 0.942$).
  * Diebold-Mariano tests confirm statistical significance ($DM = 74.25$ and $79.12$, $p < 0.0001$).
* **Hypothesis 1 Evaluation**:
  * *Confirmed*: Non-linear gradient boosted trees capture diurnal curves, day-of-week interactions, and aircraft seat capacity non-linearities without rigid distributional assumptions.
  * Isolating M1 vs. M3 proves the specific incremental value of modeling stochastic passenger arrivals and monthly load factor variations.

### 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience Under Disruption (Shock Absorption & Dynamic Recovery)
* **Performance Under Acute Stress**:
  * Evaluation during Winter Storm Elliott (Dec 2022) and major convective ground stops.
  * Pure ML models suffer acute degradation ($R_{\text{MASE}} = 2.14$): when flights are delayed past midnight, gate departures vanish from the evening schedule, causing ML to predict empty checkpoints while stranded passengers congest the terminal.
  * The Dynamic Hybrid (M5) maintains resilience ($R_{\text{MASE}} = 1.28 \le 1.30$) by ingesting state-space queue corrections and prior-hour delay residuals ($t-1$).
* **Kaplan-Meier Survival Analysis (Time-to-Recovery)**:
  * Hybrid models return to nominal error bounds ($\pm 2\sigma$) in **3.2 hours**, compared to **6.7 hours** for pure ML and **8.4 hours** for static SARIMAX.
* **Hypothesis 2 Evaluation**:
  * *Confirmed*: Cyber-physical hybrid models provide superior resilience by combining structural flight physics with dynamic state feedback.

### 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Spatial Transferability)
* **The $4 \times 4$ Zero-Shot Spatial Transfer Experiment**:
  * Intra-carrier transfer across layouts: UA at LAX (Decentralized) $\to$ ORD (Pier), EWR (Coastal Pier), IAH (Spoke Hub).
  * Cross-carrier transfer within identical geometry: LAX AA T4 $\to$ DL T3 and UA T7.
  * Cross-cluster transfer within identical TRACON airspace: EWR T-C $\to$ LGA T-C.
* **Findings on Architectural Transferability**:
  * Over-parameterized Deep Neural Networks overfit local gate topologies, suffering a **+48.2% error surge** upon zero-shot transfer.
  * Rebuilt Deterministic Baselines (+4.4%) and Probabilistic ML (+7.9%) exhibit robust transferability ($\text{RTR} \sim 1.04\text{--}1.08$).
  * State-Space Hybrids (Project 3 EKF) achieve near-perfect transfer ($\text{RTR} = 1.00$) because live innovation residuals continuously re-calibrate latent queue states.
* **Hypothesis 3 Evaluation**:
  * *Confirmed*: Grounding demand in empirical passenger show-up curves decouples terminal layout specifics from macro schedule dynamics.

### 5.6 Master Operational Recommendations for TSA & Airport Authorities
* **Actionable Decision Heuristics for Federal Security Directors (FSDs)**:
  1. *Replace Static Staffing with 2-Hour Lead-Lag Schedules*: Shift TSO roster planning from static historical tables to 2-hour pre-departure convolved flight schedules (peaking 90–120 minutes pre-departure).
  2. *Incorporate Real-Time DB1B Connecting Deflation*: Scale scheduled departing seats by local originating fractions ($1 - C_i$) to prevent over-staffing at connecting hubs.
  3. *Deploy Two-Stage Hybrid Estimators in Operations Centers*: Rely on LightGBM Tweedie for nominal next-day lane allocation, but activate state-space queue feedback during FAA Ground Delay Programs and severe convective weather.

### 5.7 Empirical Cross-Project Synthesis
* **Triangulating Three Computational Paradigms**:
  * *Project 1 (Supervised ML / Holdout Benchmark)*: Establishes out-of-time predictive accuracy ($R^2 = 0.627, \text{MASE} = 0.846$).
  * *Project 2 (Queueing Simulation)*: Demonstrates that dynamic lane allocation based on hybrid predictions reduces total passenger delay hours by **80.1%** during severe lane outages, keeping P95 wait times at 11.5 minutes versus 60-minute saturation under static staffing.
  * *Project 3 (Digital Twin State-Space Filtering)*: Demonstrates that Extended Kalman Filter state estimation achieves zero-shot spatial transfer ($\text{RTR} = 1.00$) across matched airspace nodes.

---

## 4. Key Methodological Commitments & Data Alignment Matrix

The table below outlines how recent methodological agreements map across the thesis chapters and repository assets:

| Methodological Pillar | Specific Operational Rule | Primary Thesis Home | Repository Source Asset |
| :--- | :--- | :--- | :--- |
| **9-Airport Cohort** | BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL (Balanced AA, DL, UA representation). | Ch. I (Delimitations); Ch. III (Sample); Ch. IV (Table 4.4) | `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` |
| **Flight OTP Boundary** | Retain departures from thesis airports only; destinations unrestricted (captures total terminal demand). | Ch. III (ETL Pipeline); Ch. IV (Census 4.1) | `src/etl/etl_otp.py`; `results/01_top25_clustering.xlsx` |
| **T-100 Load Factors** | Retain all route segments originating at thesis airfields to scale scheduled seats. | Ch. III (ETL Pipeline); Ch. IV (Lead-Lag 4.6) | `src/etl/etl_t100.py`; `results/03_lead_lag_deconvolution.xlsx` |
| **DB1B Originating Ratio** | Deflate seats by local originating fraction ($1 - C_i$) to eliminate airside connecting passengers. | Ch. III (Validity); Ch. V (Mechanics 5.1) | `dimensions/dim_airport_connecting_ratios.csv` |
| **Network Temporal Demarcation** | Post-pandemic baseline anchored to May 1, 2022 across the Top 25 commercial network (CUSUM/Chow break). | Ch. I (Delimitations); Ch. III (Temporal Scope); Ch. IV (4.4) | `Thesis Section Documents/Training_Demarcation_and_Model_Evaluation_Methodology.md` |
| **Checkpoint Exclusivity** | Proof that Type II (airside connected) behaves identically to Type I (hard air-gapped; KS $p = 0.28$). | Ch. III (Validity); Ch. IV (Econometric Tests 4.5) | `Thesis Section Documents/airport-criteria-selection.md` |
| **Evaluation Framework** | Three dimensions (Robustness, Resilience, Generalizability) evaluated across M0, M1, M3, M5. | Ch. III (Evaluation Design); Ch. IV (4.7); Ch. V (5.3–5.5) | `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |
| **Cross-Project Synthesis** | Unifying Supervised ML (Proj 1), Queue Sim (Proj 2: -80.1% delay), and Digital Twin EKF (Proj 3: $\text{RTR}=1.00$). | Ch. V (Section 5.7) | `Gleich-Thesis/thesis/notes_and_recommendations/Master_Results_and_Discussion_Comprehensive_Draft.md` |

---

## 5. Immediate Action Plan & Writing Roadmap

To finalize the thesis manuscript efficiently:

1. **Synchronize Chapter Manuscripts**:
   * Update `Chapter_4_Results_Empirical_Findings.md` to incorporate the exact subsection headers (4.1 through 4.7) and cross-reference the finalized Excel workbooks.
   * Update `Chapter_5_Analysis_and_Discussion.md` to integrate the full narrative for the three evaluation dimensions, the FSD operational heuristics, and the cross-project synthesis.
2. **Harmonize Chapter I & III Introductory Files**:
   * Ensure `Chapter_1_Introduction.docx` reflects the spatial (9 airports), carrier (Big 3), and temporal (May 1, 2022) delimitations.
   * Ensure `Chapter_3_Methodology.docx` contains the complete 4-tiered filtering pipeline and the 9-airport selection matrix.
3. **Compile Defense Presentation Slides**:
   * Structure the 25-slide defense deck following the outline provided in `Recommendations_Results_and_Discussion.md`, centering on the 2025 out-of-time holdout matrix and the three core evaluation dimensions.
