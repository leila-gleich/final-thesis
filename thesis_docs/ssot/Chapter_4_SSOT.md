# CHAPTER IV SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
PROJECT: Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
DOCUMENT: Chapter IV Single Source of Truth (SSOT) Reference Specification
RELEASE VERSION: v4.0 (SemVer-Data) | DATE: October 2026
CANONICAL LOCATION: thesis_docs/ssot/Chapter_4_SSOT.md
COMPANION DRAFT: thesis_docs/manuscripts/Chapter_4_Results_Empirical_Findings.md
====================================================================================================

## 1. PURPOSE AND SCOPE OF THE SSOT DOCUMENT

This document serves as the **definitive, immutable Single Source of Truth (SSOT)** for Chapter IV (Empirical Findings and Model Evaluation) of the graduate thesis. 

Every statistical measure, sample size ($N$), econometric coefficient ($r, R^2, t, p, \beta$), model performance metric ($\text{RMSE}, \text{MAE}, \text{MASE}, \text{Bias}, DM$), and operational classification used in the thesis manuscript, defense presentations, and accompanying publications is anchored herein. No downstream text, table, or figure in Chapter IV may deviate from the numbers certified in this document.

---

## 2. CANONICAL CHAPTER IV OUTLINE ARCHITECTURE

Chapter IV strictly adheres to a four-part, seventeen-subsection progression designed to separate objective empirical results from subsequent theoretical analysis (reserved for Chapter V):

```
CHAPTER IV: EMPIRICAL FINDINGS AND MODEL EVALUATION
├── 4.1 Initial Exploratory Data Analysis
│   ├── 4.1.1 Descriptive Statistics
│   ├── 4.1.2 Temporal Boundaries
│   ├── 4.1.3 Defining Seasonality
│   ├── 4.1.4 TSA & OTP Throughput Data
│   └── 4.1.5 Implications for Subset
├── 4.2 Data Filtering and Subset Selection
│   ├── 4.2.1 Four-Phase Filtering Pipeline
│   ├── 4.2.2 Pipeline Results
│   ├── 4.2.3 Descriptive Statistics for Subset
│   └── 4.2.4 Implications for Model
├── 4.3 Model Development and Execution
│   ├── 4.3.1 Feature Engineering
│   ├── 4.3.2 Model Training
│   ├── 4.3.3 Model Testing
│   └── 4.3.4 Implications for How to Interpret Final Results
└── 4.4 Model Evaluation and Results
    ├── 4.4.1 Results from Running Models
    ├── 4.4.2 General Model Performance
    ├── 4.4.3 Model Performance in the Context of the Thesis
    └── 4.4.4 Implications of Model Performance for Predictive Forecasting in Aviation
```

---

## 3. MASTER NUMERICAL REGISTRY (HARMONIZED EMPIRICAL METRICS)

### 3.1 Data Foundation Census (Full Candidate Commercial Network)

| Entity / Dimension | Raw Ingested Grain | Post-ETL Cleaned Grain | Facility & Carrier Scope | Conformance & Integrity Certification |
| :--- | :---: | :---: | :--- | :--- |
| **TSA FOIA Checkpoint Logs** | 19,500,286 | **6,434,732** lane-hours | 25 Airfields, 955 Screening Lanes | 100% Non-Null; 0 orphans; 2.703,694,229 screened passengers |
| **BTS OTP (Form 234)** | 45,777,091 | **13,153,654** departures | 25 Airfields, 17 Reporting Carriers | 13.15M domestic flights; delay causes & cancellations |
| **BTS Form 41 Schedule T-100** | 1,945,451 | **422,096** route-months | 25 Airfields, 18 Operating Carriers | 2.095B departing seats; 1.701B transported passengers |
| **BTS DB1B / DB1C Surveys** | 12,910,384 | **22,051,557** coupon records | Closed 25-Airport City Pairs | 62.158M ticketed passengers; connecting ratios |
| **Synthesized Analytical Warehouse**| **67,222,828** | **42,062,039** conformed rows | Top 25 Candidate Network | 100% referential integrity across 6 conformed dimensions |

### 3.2 Data Hygiene Protocols and Anomaly Remediation

1. **Spatial Key Resolution & Unidentified Airport Quarantine**:
   - Total raw records with missing/corrupted airport strings: **35,809**.
   - Recovered via text pattern matching in `dim_checkpoint`: **7,489** records.
   - Quarantined to null surrogate key (`airportId = 0`, `airportMissing = 1`): **22,190** records.
   - Remediation Impact: Prevented the creation of an artificial **9.71-million passenger "phantom airport"**.
   - Production Filter: Strictly enforce `WHERE airportMissing = 0 AND airportId > 0`.
2. **Structural Zeros vs. Sensor Dropouts**:
   - Post-ETL zero-throughput lane-hours: **450,973** (2.31% of warehouse).
   - Overnight concentration (00:00 to 03:59 local): **98.6%** of all zero values.
   - Operational Rule: Preserved as true physical lane closures during night curfews; zero values are never naively imputed with moving averages.
3. **Flight Cancellations & Information Causality**:
   - National cancellation rate: **2.03%** (267,019 domestic operations).
   - Unassigned aircraft tail numbers occurring on cancelled flights: **99.4%**.
   - Advance cancellations (> 24 hours prior to scheduled departure): Purged from passenger demand supply curves.
   - Tactical cancellations (< 2 hours prior to scheduled departure): Retained in passenger demand curves, recognizing that passengers crossed security before flight cancellation.

### 3.3 Post-ETL Master Summary Descriptive Statistics (Top 25 Cleaned Warehouse)

| Variable Name | Sample Size ($N$) | Mean | Median | Std Dev | IQR | Min | Max | 5th Pct | 95th Pct |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Hourly Lane Throughput (pax/hr)** | 6,434,732 | 420.17 | 293.00 | 444.84 | 447.00 | 0.00 | 5,336.00 | 10.00 | 1,316.00 |
| **Flight Departure Delay (minutes)** | 13,153,654 | 12.70 | -2.00 | 52.75 | 14.00 | -105.00 | 3,695.00 | -10.00 | 83.00 |
| **Significant Delay Rate ($\ge$ 15m)** | 13,153,654 | 20.12% | 0.00% | 40.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| **Flight Cancellation Rate (%)** | 13,153,654 | 2.03% | 0.00% | 14.09% | 0.00% | 0.00% | 100.00% | 0.00% | 100.00% |
| **Runway Taxi-Out Queue Time (min)** | 13,153,654 | 18.84 | 16.00 | 10.03 | 9.00 | 1.00 | 180.00 | 8.00 | 39.00 |
| **Airborne Flight Duration (min)** | 13,153,654 | 141.50 | 126.00 | 75.40 | 92.00 | 15.00 | 720.00 | 45.00 | 310.00 |
| **Scheduled Flight Distance (miles)** | 13,153,654 | 1,052.12 | 867.00 | 624.80 | 820.00 | 67.00 | 5,095.00 | 230.00 | 2,550.00 |
| **Available Seats per Route-Month** | 422,096 | 4,962.40 | 2,512.00 | 7,019.66 | 5,480.00 | 1.00 | 145,200.00 | 120.00 | 19,200.00 |
| **Transported Pax per Route-Month** | 422,096 | 4,030.05 | 1,927.00 | 5,938.42 | 4,380.00 | 0.00 | 128,500.00 | 85.00 | 15,800.00 |
| **Route Load Factor (%)** | 422,096 | 81.21% | 83.40% | 11.80% | 12.50% | 0.00% | 100.00% | 58.40% | 94.20% |
| **Connecting Passenger Fraction (%)** | 22,051,557 | 51.39% | 50.73% | 11.74% | 16.20% | 33.58% | 76.04% | 35.69% | 70.09% |

### 3.4 Temporal Demarcation and Dataset Partitioning (Candidate B)

* **Selected Demarcation Point**: **May 1, 2022** (Candidate B).
* **Policy Catalyst**: Nationwide vacatur of federal transit mask requirements (April 18, 2022); passenger load factors normalized to pre-pandemic baselines (84.7%) by May 1, 2022.
* **Econometric Rationale**: Scheduled flight-to-TSA throughput coupling stabilized to $r = 0.553$ ($R^2 = 30.61\%$), recovering from artificial COVID-19 lockdown distortions ($R^2 = 36.85\%$).
* **Continuous Candidate B Span**: **44 continuous months** (May 1, 2022 to December 31, 2025).
* **Development Span**: **32 continuous months** (May 1, 2022 to December 31, 2024).
* **Training Partition**: May 1, 2022 to December 31, 2023 (**20 months**; **122,847** hourly observations across the 9-airport complex cohort; **404,324** multi-facility candidate observations; **23,400** Top 25 system hours).
* **Validation Partition**: January 1, 2024 to December 31, 2024 (**12 months**; **72,723** hourly complex observations).
* **Holdout Test Partition**: January 1, 2025 to December 31, 2025 (**12 months**; **72,053** hourly complex observations; **8,760** continuous system hours; **215,562** facility-level candidate screening hours).
* **Information Purge Buffer**: A strict **7-day operational embargo** between training, validation, and testing partitions prevents multi-day delay cascades from leaking across evaluation splits.

### 3.5 Seasonality, Volatility, and Interaction Tensor

#### Annual Seasonal Regimes Across the Top 25 Network
$$\text{Coupled Volatility Index (CVI)} = CV_{\text{TSA}} \times \sigma_{\text{Delay}}$$

| Regime Code | Regime Name | Calendar Days ($N$) | Share (%) | Mean Daily TSA (Pax) | Within-Day $CV_{\text{TSA}}$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Delayed $\ge 15$m (%) | Cancellation Rate (%) |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`1_OFF_PEAK`** | Winter Lull & Mid-Autumn | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | **27.85** | 9.85 min | 18.00% | 0.89% |
| **`2_MID_PEAK`** | Spring Ramp & Late-Summer | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | **32.38** | 15.14 min | 23.23% | 1.36% |
| **`3_PEAK`** | Summer Severe Weather | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | **39.36** | 24.17 min | 31.04% | 3.16% |
| **`4_HOLIDAY`** | Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | **33.07** | 16.51 min | 24.33% | 1.82% |

#### Day-of-Week Operational Archetypes (Top 25 Airfields)

| DOW | Day Name | Operational Archetype | Days ($N$) | Mean Daily TSA | Within-Day $CV$ | Delay Disp ($\sigma_{\text{Delay}}$) | Coupled Volatility | Mean Delay | Delayed $\ge 15$m (%) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Monday | Outbound Business Surge | 192 | 1,246,150 | **0.604** | 56.56 min | **34.00** | 15.78 min | 23.54% |
| **2** | Tuesday | Midweek Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | **50.09 min** | **29.99** | 11.69 min | 19.44% |
| **3** | Wednesday | Midweek Baseline Stability | 192 | 1,123,368 | 0.594 | **49.27 min** | **29.13** | 12.22 min | 20.05% |
| **4** | Thursday | Corporate Outbound & Early Ramp| 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| **5** | Friday | Business & Leisure Getaway Surge| 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| **6** | Saturday | Volume Trough & Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| **7** | Sunday | Leisure Return & Evening Cascade| 192 | 1,279,017 | 0.577 | **58.07 min** | **33.40** | **17.78 min** | **25.60%** |

#### Diurnal Dual-Peak Non-Consecutive Blocks and 84-Cell Tensor
* **`1_OFF_PEAK`**: 00:00 to 03:00 (Overnight curfew valley).
* **`2_MID_PEAK`**: 08:00 to 13:00/16:00 (Midday plateau and scheduled turnaround buffer).
* **`3_PEAK`**: Dual non-consecutive turbulence peaks:
  - Morning Bank Surge (05:00–08:00): $\sigma_{\text{TSA}} > 11,380$ pax/hr.
  - Evening Delay Cascade (14:00/17:00–22:00): $\sigma_{\text{Delay}} > 63.4$ min.
* **The 84-Cell Tensor**: $4 \text{ Seasons} \times 7 \text{ Days of Week} \times 3 \text{ Diurnal Blocks} = 84 \text{ cells}$.
* **Degrees of Freedom Certification**: **83 of 84 cells (98.8%)** satisfy the statistical minimum power threshold of $N_{\text{train}} \ge 50$ (median $N = 215$).

### 3.6 Master Cross-Dataset Econometric Relationships (Top 25 Airfields)

| Relationship Category | Metric 1 (OTP / Capacity) | Metric 2 (TSA Demand / Queue) | Sample Grain | Pearson $r$ | $R^2$ (%) | $t$-statistic | $p$-value | Operational Law Confirmed |
| :--- | :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Volume Coupling** | Raw Scheduled Flights | Total TSA Throughput | Top 25 Airfields | 0.4572 | 20.90% | 2.47 | $< 0.05$ | Scheduled flights alone explain only 20.9% of raw throughput. |
| **Connecting Deflation** | Raw Scheduled Flights | Local Originating TSA Demand | Top 25 Airfields | **0.6704** | **44.94%** | 4.33 | $< 0.001$ | DB1B connecting deflation increases explained variance by +115%. |
| **Hub Scale vs. Connecting**| Connecting Ratio (%) | Scheduled Flight Volume | Top 25 Airfields | 0.4503 | 20.28% | 2.42 | $< 0.05$ | Mega-hubs exhibit high connecting shares (CLT 76.0%, ATL 70.1%). |
| **Surface Queue Feedback** | Taxi-Out Queue Time | Total TSA Throughput | Top 25 Airfields | 0.2867 | 8.22% | 1.44 | $0.163$ | Higher volume correlates directionally with longer tarmac queues. |
| **Surface-to-Air Feedback** | Mean Departure Delay | Taxi-Out Queue Time | 63,925 Days | **0.4971** | **24.71%** | 2.74 | $< 0.001$ | Gate pushback delays feed congested runway sequencing queues. |
| **Schedule Delay Coupling** | Significant Delays (%) | Total TSA Throughput | Top 25 Airfields | 0.2019 | 4.08% | 0.99 | $0.332$ | Raw flight delays are decoupled contemporaneously from landside volume. |
| **Hourly Volatility Trans** | Hourly Throughput $CV$ | Flight Departure Delay $CV$ | Top 25 Airfields | **0.4375** | **19.14%** | 2.33 | $< 0.05$ | Checkpoint surge volatility injects variance into boarding gate closures. |
| **Daily Volatility Coupling**| Daily Throughput $CV$ | Daily Delay $CV$ | Top 25 Airfields | 0.3714 | 13.79% | 1.92 | $0.067$ | Day-to-day throughput volatility tracks network flight delays. |
| **Surge vs Delay Volatility**| Peak-to-Median Surge | Flight Departure Delay $CV$ | Top 25 Airfields | 0.3480 | 12.11% | 1.78 | $0.088$ | Spiky checkpoint rushes correlate with schedule instability. |
| **Weekly Cyclical Coupling** | DOW Mean Daily TSA | DOW Mean Departure Delay | 7 Days ($N=7$) | **0.9022** | **81.40%** | 4.68 | $< 0.01$ | Passenger demand volume explains 81.4% of weekly flight delay variance. |
| **Weekly Delay Rate Coupl** | DOW Mean Daily TSA | DOW DepDel15 Rate (%) | 7 Days ($N=7$) | **0.9000** | **81.00%** | 4.62 | $< 0.01$ | Passenger rushes directly drive weekly flight delay rates. |
| **Annual Monthly Coupling** | Monthly Mean Daily TSA | Monthly Mean Departure Delay | 12 Months ($N=12$) | **0.6313** | **39.85%** | 2.57 | $< 0.05$ | Summer passenger peaks align with convective weather delay peaks. |

### 3.7 The 9-Airport Experimental Cohort and Factorial Matrix

* **Macro Funnel Attrition**: 450+ commercial airports $\to$ Top 25 airfields $\to$ 14 candidate hubs (Southwest excluded) $\to$ 9 selected hubs (12 dedicated complexes).
* **Factorial Balance**: Exactly **4 dedicated screening complexes per legacy carrier** across **4 operational cluster archetypes**:
  - **American Airlines (AA)**: DFW (Cluster 0), ORD (Cluster 0), BOS (Cluster 1), PHL (Cluster 2).
  - **Delta Air Lines (DL)**: LAX (Cluster 0), BOS (Cluster 1), DTW (Cluster 2), LGA (Cluster 3).
  - **United Airlines (UA)**: ORD (Cluster 0), LAX (Cluster 0), IAH (Cluster 1), EWR (Cluster 3).
* **Econometric Proofs of Checkpoint Exclusivity**:
  - Volume Conservation: $\rho = 1.00 \pm 0.04$ ($R^2 > 0.95$).
  - Zero-Flight Intercept: $\beta_0 = 12.4$ pax/hr ($p = 0.40$).
  - Cross-Carrier Orthogonality: $\beta_{\text{other}} = 0.002$ ($p = 0.62$).
  - Terminal Layout Invariance (Separated vs. Walkway-Connected): Kolmogorov-Smirnov $D = 0.032, p = 0.28$.

### 3.8 Lead-Lag Passenger Arrival Distribution (ACRP Report 40 Baseline)

$$\text{Demand}_{\text{convolved}, t} = \sum_{h=1}^{3} w_h \cdot \left[ \sum_{f \in \mathcal{F}_{t+h}} \text{Seats}_f \cdot \text{LoadFactor}_f \cdot (1 - \text{ConnectingRatio}) \right]$$
* **Empirical Arrival Weights**: $w_1 = 0.35$ (Lead $t+1$), $w_2 = 0.50$ (Lead $t+2$), $w_3 = 0.15$ (Lead $t+3$).

| Lead-Lag Horizon | Pearson Correlation ($r$) | Explanatory Power ($R^2$) | Regression Slope (pax/flight) | Operational Planning Interpretation |
| :--- | :---: | :---: | :---: | :--- |
| **Lag $t-1$ (1 hr post-departure)** | 0.1987 | 3.95% | 16.06 | Passenger already boarded; residual spurious correlation. |
| **Contemporaneous $t$ (Gate departure)** | 0.3403 | 11.58% | 27.49 | Contemporaneous flight schedule explains only 11.6% of checkpoint variance. |
| **Lead $t+1$ (1 hr pre-departure)** | 0.4913 | 24.13% | 39.70 | Captures late business travelers and carry-on-only passengers. |
| **Lead $t+2$ (2 hr pre-departure)** | **0.4876** | **23.78%** | **39.40** | **Modal show-up window conforming to ACRP Report 40 standards.** |
| **Lead $t+3$ (3 hr pre-departure)** | 0.3800 | 14.44% | 30.70 | Captures holiday families and international passenger check-ins. |
| **Convolved Passenger Show-Up Curve** | **0.6985** | **48.78%** | **74.98** | **Full lead-lag kernel deconvolution across $t+1, t+2, t+3$.** |
| **Show-Up Curve $\times$ T-100 Load Factor**| **0.7061** | **49.85%** | **90.56** | **Convolved seats weighted by monthly carrier route load factor.** |

### 3.9 Master Model Benchmark Matrix (2025 Out-of-Time Holdout)
* **Sample Size**: **72,053** hourly complex observations (8,760 continuous system hours) across the 12 dedicated screening complexes of the 9-airport experimental cohort.

| Paradigm | Model ID | Model Architecture | Validation $R^2$ | Test $R^2$ | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Forecast Bias (pax/hr) | Academic Target Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **Deterministic Baseline** | **$M_0$** | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4951 | 0.4508 | 1,377.3 | 939.8 | 1.000 | -0.7 | Baseline Reference |
| **Deterministic Baseline** | **$M_1$** | Contemporaneous Sched SARIMAX *(Old)* | 0.4338 | 0.4375 | 1,393.8 | 1,042.6 | 1.109 | -327.4 | Failed ($\text{MASE} > 1.0$) |
| **Deterministic Baseline** | **$M_1^*$**| Rebuilt 2-Hour Static Sched Baseline | 0.5312 | **0.5293** | **1,265.4** | **902.1** | **0.942** | **-184.2** | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_2$** | Convolved Lead Flights Only | 0.5443 | 0.5862 | 1,195.5 | 856.2 | 0.911 | -296.8 | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_3$** | Convolved Lead + OTP Delays/Cancels | 0.5450 | **0.5880** | **1,192.9** | **855.1** | **0.910** | **-295.3** | Passed Target ($\text{MASE} < 1.0$) |
| **Probabilistic / ML** | **$M_4$** | Full Tri-Modal Pipeline (Load Factor Scaled) | 0.5798 | 0.5771 | 1,208.6 | 856.3 | 0.911 | -430.8 | Passed Target ($\text{MASE} < 1.0$) |
| **Sequential Hybrid** | **$M_5$** | Sequential SARIMA-Tree Hybrid | **0.6644** | **0.6270** | **1,135.0** | **795.0** | **0.846** | **-402.9** | **CHAMPION ARCHITECTURE** |

* **Statistical Significance (Diebold-Mariano Test vs. Rebuilt $M_1^*$)**:
  - Model $M_3$ (LightGBM Tweedie): $DM = 74.25, p < 0.0001$.
  - Model $M_5$ (Sequential Hybrid): $DM = 79.12, p < 0.0001$.

### 3.10 Master Multi-Pillar Hypothesis Evaluation Matrix Across the Three Dimensions

| Dimension | Metric | Definition | Target | Deterministic ($M_1^*$) | Probabilistic ML ($M_3$) | Dynamic Hybrid ($M_5$) | Hypothesis Confirmation |
| :--- | :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **1: Robustness** | $\text{RMSE}_{\text{routine}}$ | Delay $< 15$m; 0 Cancels | $< 1,150$ | 1,265.4 pax/hr | 1,167.9 pax/hr | **1,114.7 pax/hr** | **Confirms H1(a)**: ML and Hybrid fit nominal curves tighter. |
| **1: Robustness** | $\text{MASE}_{\text{routine}}$ | Relative Routine Error | $< 0.900$ | 0.942 | 0.890 | **0.834 (SUPERIOR)**| $M_5$ delivers 11.5% accuracy gain over deterministic planning. |
| **1: Robustness** | $DM$ Test Stat | Loss Differential Test | $p < 0.001$ | Control | $DM = 74.25$ ($p < 0.0001$) | **$DM = 79.12$ ($p < 0.0001$)** | Gains are mathematically decisive and reproducible. |
| **2: Resilience** | $\text{RMSE}_{\text{shock}}$ | Delay $\ge 45$m or Cancels $\ge 5$| $< 1,100$ | 1,228.9 pax/hr | 1,024.9 pax/hr | **1,023.2 pax/hr** | Dynamic models maintain tight error bounds under severe weather. |
| **2: Resilience** | $\text{MASE}_{\text{shock}}$ | Relative Disruption Error | $< 0.850$ | 0.966 | 0.772 | **0.737 (SUPERIOR)**| Dynamic models perform 26% better than naive guessing. |
| **2: Resilience** | $R_{\text{MASE}}$ | $\text{MASE}_{\text{shock}} / \text{MASE}_{\text{routine}}$ | $< 1.30$ | 1.03 (Static blind) | 0.87 (Acute surge: 2.14) | **0.88 (Maintains $\le 1.28$)** | **Confirms H1(b)**: Pure ML collapses during delayed flight holds ($R = 2.14$); Hybrid stays resilient via queue feedback. |
| **2: Resilience** | $\text{TTR}_{\text{shock}}$ | Kaplan-Meier survival to $\pm 2\sigma$ | $< 4.0$ hrs | 8.4 hours | 6.7 hours | **3.2 hours (FASTEST)** | $M_5$ recovers 5.2 hrs faster than $M_1^*$ and 3.5 hrs faster than $M_3$. |
| **3: Generalizability**| Zero-Shot $\text{RMSE}_{\text{transfer}}$ | EWR to LGA Zero-Shot | $< 1,350$ | 1,321.0 pax/hr | **1,162.8 pax/hr** | 1,237.4 pax/hr | Out-of-the-box accuracy on unfamiliar airport facility. |
| **3: Generalizability**| $RTR$ | $\text{RMSE}_{\text{trans}} / \text{RMSE}_{\text{in}}$ | $\le 1.10$ | **1.04 (EXCELLENT)** | **1.08 (EXCELLENT)** | 1.19 (Moderate penalty) | **Confirms H1(c)**: Physical rules ($RTR=1.04$) and convolved ML ($RTR=1.08$) generalize better than decision trees. |
| **3: Generalizability**| $\Delta_{\text{transfer}}$ | $((\text{RMSE}_{\text{trans}} - \text{RMSE}_{\text{in}})/\text{RMSE}_{\text{in}})\%$ | $\le 10.0\%$ | **+4.4% (MINIMAL)** | **+7.9% (LOW)** | +18.7% (Elevated) | Simple physical rules lose only 4.4% accuracy; complex residual trees lose 18.7% due to local terminal overfitting. |
| **3: Generalizability**| $\Delta\text{MASE}$ | $\text{MASE}_{\text{trans}} - \text{MASE}_{\text{in}}$ | $< +0.100$ | **+0.041** | **+0.071** | +0.158 | Rebuilt $M_1^*$ and $M_3$ beat $+0.100$ threshold, confirming high zero-shot portability. |

---

## 4. SOURCE FILE TRACEABILITY & REPOSITORY PROVENANCE

Every empirical number in Section 3 is programmatically linked to canonical data artifacts in the project repository:

| Manuscript Table | Analytical Scope | Canonical Script / Pipeline | Source Data Files & Workbooks |
| :--- | :--- | :--- | :--- |
| **Table 4.1** | Multi-Source Post-ETL Census | `src/etl/build_db1v0.py` | `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Census_Master`) |
| **Table 4.2** | Post-ETL Master Descriptives | `src/etl/profile_db1b.py` | `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Descriptive_Stats`) |
| **Table 4.3a** | Post-Pandemic Demarcation | `src/analysis/run_regime_analysis.py` | `thesis_docs/notes/methodology_memos/candidate_b_deep_dive_justification.md` |
| **Table 4.3b** | Annual Volatility Regimes | `season-analysis/run_season_analysis.py` | `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Seasonality_Regimes`) |
| **Table 4.4a** | Day-of-Week Archetypes | `season-analysis/run_season_analysis.py` | `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `DOW_Archetypes`) |
| **Table 4.5** | TSA-OTP Econometric Corrs | `otp_volatility_analysis/run_analysis.py` | `results/01_top25_clustering/01_top25_clustering.xlsx` (Sheet: `Econometric_Correlations`) |
| **Table 4.6** | 9-Airport Factorial Specification | `src/analysis/run_4tier_filtering.py` | `results/02_4tier_filtering/02_4tier_filtering.xlsx` (Sheet: `Factorial_Matrix`) |
| **Table 4.7** | 9-Airport DOW Profile | `src/analysis/run_top9_analysis.py` | `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` |
| **Table 4.8** | 9-Airport vs Top 25 Stats | `src/analysis/run_top9_analysis.py` | `results/02_4tier_filtering/02_top9_cohort_comprehensive_analysis.xlsx` |
| **Table 4.9** | Lead-Lag Arrival Dynamics | `src/features/build_features.py` | `results/03_lead_lag_deconvolution/03_lead_lag_deconvolution.xlsx` |
| **Table 4.10** | Master 2025 Holdout Matrix | `src/models/evaluate_models.py` | `results/04_model_execution_2025_holdout/04_model_execution_2025_holdout.xlsx` |
| **Table 4.11** | Multi-Pillar Hypothesis Matrix| `src/models/evaluate_multipillar.py` | `results/05_robustness_resilience_generalizability/05_robustness_resilience_generalizability.xlsx` |

---

## 5. TERMINOLOGY & NOMENCLATURE GOVERNANCE

All prose in Chapter IV strictly follows the **Academic & Operational Guide: Replacing Jargon and Buzzwords with Defensible Aviation Terminology** (`thesis_docs/notes/provenance_and_standards/Jargon_and_Buzzword_Replacement_Guide.md`):

1. **Empirical Passenger Show-Up Curve** (or **Lead-Lag Passenger Arrival Distribution**): Used instead of *"physics-based continuous arrival kernel convolution"*. Anchored in ACRP Report 40 terminal planning guidelines.
2. **Carrier Checkpoint Isolation**: Used instead of *"orthogonal Wiener-Hopf deconvolution operator"*. Represents dedicated single-carrier screening complexes.
3. **Connecting Passenger Deflator** (or **Local Originating Passenger Fraction**): Multiplying flight seats by $(1 - \text{Connecting Ratio})$ to isolate landside passengers; resolves the **"Hub Disconnect"**.
4. **Physically Separate Terminals vs. Walkway-Connected Terminals**: Used instead of *"Type I vs Type II complexes"*.
5. **Peak-Hour Checkpoint Congestion**: Used instead of *"heavy-traffic asymptotics and boundary saturation"*.
6. **Routine Operational Accuracy, Resilience Under Disruption, Cross-Airport Transferability**: The three core operational evaluation dimensions evaluating Hypothesis 1.
7. **Disruption Error Multiplier ($R_{\text{MASE}}$)** and **Transfer Error Penalty ($\Delta_{\text{transfer}}$)**: Used instead of obscure cyber-physical jargon.
8. **Nighttime Checkpoint Closures vs. Missing Data**: Preserving true operational structural zeros during scheduled airport curfews.
9. **Unidentified Airport Records**: Quarantining blank airport records to surrogate key `airportId = 0` to prevent phantom airports.
10. **Strict Information Causality**: Enforcing that models only receive data physically available prior to the forecast horizon (prior-hour delays, tactical cancellations, advance schedules).

---

## 6. CROSS-CHAPTER INTEGRATION ROADMAP

* **Integration with Chapter III (Methodology)**:
  - Section 4.1 validates the multi-source data extraction pipeline and 84-cell interaction tensor defined in Section 3.8.
  - Section 4.2 provides the empirical proof of the four-phase filtering pipeline conceptualized in Section 3.9.
  - Section 4.3 operationalizes the ACRP Report 40 lead-lag passenger arrival kernels defined in Section 3.10.
  - Section 4.4 tests the model suite (M0 through M5) against the 2025 out-of-time holdout protocol defined in Section 3.12.
* **Handoff to Chapter V (Analysis & Discussion)**:
  - Chapter IV provides the unvarnished factual numbers; Chapter V interprets why those numbers occur.
  - Section 5.1 analyzes the physical and behavioral mechanics behind the Hub Disconnect.
  - Section 5.2 explores the behavioral drivers of passenger show-up curves.
  - Sections 5.3, 5.4, and 5.5 perform deep dives into Dimension 1 (Robustness), Dimension 2 (Resilience & Empty Checkpoint Fallacy), and Dimension 3 (Generalizability & Spatial Portability).
  - Section 5.6 details the operational deployment of the Regime-Switched Dual-Track Decision Engine.
  - Section 5.7 provides the cross-project synthesis.

====================================================================================================
END OF CHAPTER IV SINGLE SOURCE OF TRUTH (SSOT) SPECIFICATION
====================================================================================================
