# Master Roadmap & Outline: Chapter IV (Findings) & Chapter V (Discussion)

## Chapter IV: Findings / Empirical Results (Before Analysis)

### 4.1 Master Descriptive Statistics and Data Health Census
* Multi-source data foundation (67.22M raw rows -> 42.06M post-ETL rows across 25 airfields).
* Spatial key fingerprinting and phantom airport isolation (35.8k malformed records remediated; surrogate key 0).
* Operational zeros vs. sensor dropouts (450k structural zero hours preserved).
* Flight delays and advance vs. tactical cancellations.
* *Companion CSV Data Tables*:
  * `Section_1A_Data_Foundation_Census.csv`
  * `Section_1B_Post_ETL_Master_Descriptive_Statistics.csv`
  * `Section_1C_Top25_Candidate_Airports_Post_ETL_Census.csv`
  * `Section_1D_Top25_Macro_Summary_Statistics.csv`

### 4.2 The Four-Tiered Purposive Filtering Pipeline
* Macro Filter: Scale and heavy-traffic asymptotics ($\rho(t) \to 1.0$).
* Meso Filter: Shock invariance and Southwest Airlines (WN) bimodal arrival exclusion.
* Micro Filter: Checkpoint exclusivity ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$).
* Factorial Grid: The 9-Airport Experimental Cohort ($3 \times 3$ matrix across AA, DL, UA).
* *Companion CSV Data Tables*:
  * `Section_2A_Four_Tiered_Purposive_Filtering_Funnel.csv`
  * `Section_2B_Nine_Airport_Experimental_Cohort_Factorial_Grid.csv`

### 4.3 Empirical Operational Clusters and Systemic Trends
* Unsupervised PCA & K-Means clustering across Top 25 airfields (4 operational archetypes).
* The Connecting Ratio Paradox ($50\%\text{--}76\%$ connecting passenger deflation).
* Delay transmission divergence across clusters.

### 4.4 Temporal Demarcation: Post-Pandemic Regime Selection
* Evaluation of Candidate A (Jan 2023) vs. Candidate B (May 1, 2022).
* Mask mandate repeal, CUSUM stabilization, and coupling rebound ($R^2 = 0.672$).
* 3-fold temporal partition (Train: 2022–2023, Val: 2024, Holdout Test: 2025).

### 4.5 Econometric Validation of Checkpoint Exclusivity
* Volume Conservation Test ($\rho = 1.00 \pm 0.04$).
* Zero-Flight Intercept Test ($\beta_0 = 12.4$ pax/hr, $p=0.40$).
* Cross-Carrier Orthogonality Test ($\beta_{\text{other}} = 0.002, p=0.62$).
* Layout Invariance (Type I vs. Type II Kolmogorov-Smirnov test: $D = 0.032, p = 0.28$).
* *Companion CSV Data Table*: `Section_2C_Econometric_Exclusivity_Validation.csv`

### 4.6 Feature Engineering and Lead-Lag Arrival Deconvolution
* Temporal lead horizons ($t+1, t+2, t+3$).
* Continuous convolved arrival kernels interacted with T-100 load factors ($R^2 = 0.4985$).
* *Companion CSV Data Table*: `Section_4B_Lead_Lag_Arrival_Deconvolution_Gradient.csv`

### 4.7 Model Benchmark Matrix (2025 Out-of-Time Holdout)
* Full year 2025 out-of-time evaluation across 215,562 hourly observations.
* Performance metrics across Naive (M0), SARIMAX (M1), LightGBM Tweedie (M3), and SARIMA-Tree Hybrid (M5).
* *Companion CSV Data Table*: `Section_5A_Master_Model_Execution_2025_Holdout_Matrix.csv`

---

## Chapter V: Analysis & In-Depth Discussion

### 5.1 Physical and Behavioral Checkpoint Mechanics
* Connecting passenger shielding, terminal complex aggregation, and CAT scanner sorting invariance.

### 5.2 Initial Training and Feature Deconvolution Dynamics
* Resolving physical lead-lag asynchrony (90–120 min modal arrival windows).

### 5.3 Deep-Dive: Evaluation Dimension 1 – Robustness (Continuous Static Stability)
* Routine operational performance ($\text{MASE}_{\text{routine}} \sim 0.60$), Diebold-Mariano statistical significance tests ($p < 0.0001$).

### 5.4 Deep-Dive: Evaluation Dimension 2 – Resilience (Shock Absorption & Recovery)
* Performance during Winter Storm Elliott ($R_{\text{MASE}} = 1.28$ Hybrid vs. $2.14$ pure ML).
* Kaplan-Meier Time-to-Recovery (3.2 hrs Hybrid vs. 8.4 hrs SARIMA).

### 5.5 Deep-Dive: Evaluation Dimension 3 – Generalizability (Spatial Transferability)
* Zero-shot spatial transfer across New York airspace (EWR $\to$ LGA).
* Overfitting in deep neural networks (+48.2% error surge) vs. Physics-Informed Hybrids (+11.4%).

### 5.6 Master Synthesis and Operational Recommendations
* Strategic recommendations for TSA checkpoint staffing, O&D connecting ratios, and gray-box hybrid estimators.

### 5.7 Empirical Cross-Project Synthesis
* Synthesizing Supervised Machine Learning (Project 1), First-Principles Queueing Physics (Project 2: 80.1% backlog reduction), and Digital Twin Extended Kalman Filters (Project 3: $\text{RTR} = 1.00$ transfer).
