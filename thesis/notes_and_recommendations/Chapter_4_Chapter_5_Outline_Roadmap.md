# Master Roadmap & Outline: Chapter IV (Findings) & Chapter V (Discussion)

## Chapter IV: Findings / Empirical Results (Before Analysis)

### 4.1 Master Descriptive Statistics and Data Health Census
* Multi-source data foundation (67.22M raw rows $\to$ 42.06M post-ETL cleaned rows across 25 airfields).
* Post-ETL summary statistics: 6.43M checkpoint-hours (2.70B pax screened), 13.15M domestic flights, 422k T-100 route-months, 22.05M DB1B ticket coupons.
* Spatial key fingerprinting and unidentified airport isolation (35.8k malformed records remediated; surrogate key 0).
* Nighttime checkpoint closures vs. missing data (450k structural zero hours preserved).
* Flight delays and advance vs. tactical cancellations (strict information causality).
* *Companion Results Deliverables*:
  * Master Census & Foundation: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheets: `Census_Master`, `Descriptive_Stats`)
  * Top 25 Cohort Summary: `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Top25_Summary`)

### 4.2 The Four-Tiered Purposive Filtering Pipeline
* Macro Filter: Scale and Peak-Hour Checkpoint Congestion ($\rho(t) \to 1.0$).
* Meso Filter: Airspace shock invariance and Southwest Airlines (WN) bimodal arrival exclusion.
* Micro Filter: Carrier Checkpoint Isolation ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$).
* Factorial Grid: The 9-Airport Experimental Cohort (Balanced $4 \times 4$ factorial design across AA, DL, UA).
* *Companion Results Deliverables*:
  * Filtering Funnel & Matrix: `results/02_4tier_filtering/02_4tier_filtering.xlsx` (Sheets: `Funnel_Attrition`, `Factorial_Matrix`)
  * Comprehensive Cohort Analysis: `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx`

### 4.3 Empirical Operational Clusters and Systemic Trends
* Unsupervised PCA & K-Means clustering across Top 25 airfields (4 operational archetypes).
* The Hub Disconnect: Connecting vs. Local Originating Passengers ($50\%\text{--}76\%$ connecting passenger deflation).
* Delay transmission divergence across clusters.

### 4.4 Temporal Demarcation: Post-Pandemic Regime Selection
* Evaluation of Candidate A (Jan 2023) vs. Candidate B (May 1, 2022).
* Mask mandate repeal, CUSUM stabilization, and coupling rebound ($R^2 = 0.672$).
* 3-fold temporal partition (Train: 2022–2023, Val: 2024, Holdout Test: 2025).

### 4.5 Econometric Validation of Carrier Checkpoint Isolation
* Volume Conservation Test ($\rho = 1.00 \pm 0.04$).
* Zero-Flight Intercept Test ($\beta_0 = 12.4$ pax/hr, $p=0.40$).
* Cross-Carrier Orthogonality Test ($\beta_{\text{other}} = 0.002, p=0.62$).
* Layout Invariance (Physically separate vs. Walkway-connected Kolmogorov-Smirnov test: $D = 0.032, p = 0.28$).
* *Companion Results Deliverables*: `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` (Sheet: `Econometric_Tests`)

### 4.6 Feature Engineering and Passenger Show-Up Curve Estimation
* Temporal lead horizons ($t+1, t+2, t+3$; peak at $t+2$ with $R^2 = 0.4054$).
* Empirical passenger show-up curves interacted with T-100 load factors ($R^2 = 0.4985$, citing ACRP Report 40).
* *Companion Results Deliverables*: `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx`

### 4.7 Model Benchmark Matrix (2025 Out-of-Time Holdout)
* Full year 2025 out-of-time evaluation across 215,562 hourly observations.
* Performance metrics across Diurnal Naive (M0), Rebuilt Deterministic 2-Hr Static Lead (M1: $R^2 = 0.5293, \text{RMSE} = 1265.4, \text{MASE} = 0.942$), LightGBM Tweedie (M3: $R^2 = 0.5880, \text{RMSE} = 1192.9, \text{MASE} = 0.910$), and Sequential SARIMA-Tree Hybrid (M5: $R^2 = 0.6270, \text{RMSE} = 1135.0, \text{MASE} = 0.846$).
* *Companion Results Deliverables*: `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx` and `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx`

---

## Chapter V: Analysis & In-Depth Discussion

### 5.1 Physical and Behavioral Checkpoint Mechanics
* Connecting passenger shielding, terminal complex aggregation, and CAT scanner sorting invariance.

### 5.2 Initial Training and Passenger Show-Up Dynamics
* Resolving physical lead-lag asynchrony (90–120 min modal passenger show-up windows).

### 5.3 Deep-Dive: Evaluation Dimension 1 – Robustness (Routine Operational Accuracy)
* Routine operational performance ($\text{MASE}_{\text{routine}} = 0.890$ for M3 and $0.834$ for M5 vs. $0.942$ for M1), Diebold-Mariano statistical significance tests ($DM = 74.25$ and $79.12, p < 0.0001$).

### 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience Under Disruption
* Performance during Winter Storm Elliott ($R_{\text{MASE}} = 1.28$ Hybrid vs. $2.14$ pure ML).
* Kaplan-Meier Time-to-Recovery (3.2 hrs Hybrid vs. 6.7 hrs ML vs. 8.4 hrs SARIMA).

### 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Cross-Airport Transferability)
* Zero-shot spatial transfer across New York airspace (EWR $\to$ LGA).
* Overfitting in deep neural networks (+48.2% error surge) vs. Rebuilt Deterministic (+4.4%, $\text{RTR} = 1.04$) and Probabilistic ML (+7.9%, $\text{RTR} = 1.08$), with state-space invariance ($\text{RTR} = 1.00$).

### 5.6 Master Synthesis and Operational Recommendations
* Strategic recommendations for TSA checkpoint staffing, O&D connecting ratios, and two-stage hybrid estimators.

### 5.7 Empirical Cross-Project Synthesis
* Synthesizing Supervised Machine Learning (Project 1), Queueing Theory Simulation (Project 2: 80.1% backlog reduction), and Digital Twin State-Space Filtering (Project 3: $\text{RTR} = 1.00$ transfer).
