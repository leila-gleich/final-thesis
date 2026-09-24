# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
## TSA Checkpoint Throughput Forecasting & Airside-Landside Queue Dynamics

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Degree Program**: Master of Science in Aeronautics / Aviation Data Analytics  
**Course Milestone**: MSAA / Gleich 700B Graduate Thesis  
**Repository Version**: v3.0 (Publication-Grade GitHub Release — `final-thesis`)  

---

## Executive Overview

This repository (`final-thesis`) is the complete, self-contained, publication-grade master codebase, empirical data products, visual assets, and manuscript chapters for the graduate thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*. The research synthesizes four major federal aviation datasets (**TSA FOIA Checkpoint Logs**, **BTS On-Time Performance**, **BTS T-100 Segment Capacity**, and **BTS DB1B Ticket Coupon Surveys**) covering 67.22 million raw fact records across 2019–2025.

---

## Master Repository Architecture (`final-thesis`)

```
final-thesis/
├── README.md                           <-- Master GitHub repository guide (this file)
├── LICENSE                             <-- MIT Open Source Academic License
├── .gitignore                          <-- Git exclusion rules (cache, OS, DuckDB)
├── requirements.txt                    <-- Python dependency specifications
├── run_pipeline.py                     <-- Master execution entrypoint script
│
├── thesis/                             <-- Master Thesis Manuscripts & Recommendations Directory
│   ├── README.md                       <-- Guide & sitemap to thesis manuscripts & notes
│   ├── manuscripts/                    <-- Production manuscript chapters (.docx & .md)
│   │   ├── Chapter_1_Introduction.docx
│   │   ├── Chapter_2_Literature_Review.docx
│   │   ├── Chapter_3_Methodology.docx
│   │   ├── Chapter_4_Results_Empirical_Findings.md
│   │   ├── Chapter_4_Results_Empirical_Findings.docx
│   │   ├── Chapter_5_Analysis_and_Discussion.md
│   │   ├── Gleich_700B_Proposal.docx
│   │   └── Master_References_APA7.docx
│   └── notes_and_recommendations/      <-- Outlines & Recommendations Guides
│       ├── DATA_CLEANING_MODELING_AND_METRICS_FRAMEWORK.txt
│       ├── Recommendations_Results_and_Discussion.md
│       ├── Top25_Clustering_and_4Tier_Filtering_Guide.md
│       ├── Chapter_4_Chapter_5_Outline_Roadmap.md
│       └── VERSION_CONTROL_AND_PROVENANCE.md
│
├── src/                                <-- Modular Python Source Code Infrastructure
│   ├── etl/                            <-- Ingestion, Top 25 Clustering & 4-Tier Filtering
│   │   ├── build_db1v0.py
│   │   ├── perform_top25_clustering.py # Step 1: Top 25 PCA & K-Means clustering
│   │   └── apply_4tier_filtering.py    # Step 2: 4-tier filtering pipeline (Top 25 -> 9 Cohort)
│   ├── features/                       <-- Lead-Lag Deconvolution & Feature Engineering
│   │   ├── temporal_features.py
│   │   └── lead_lag_convolution.py     # Continuous passenger arrival kernel deconvolution
│   ├── models/                         <-- Deterministic, ML, and Dynamic Hybrid Models
│   │   ├── baselines.py                # Diurnal Naive & Contemporaneous SARIMAX
│   │   ├── machine_learning.py         # LightGBM / XGBoost Tweedie Regressors
│   │   └── hybrid_sarima_tree.py       # Sequential SARIMA-Tree Hybrid & State-Space
│   └── utils/                          <-- DB Connection & Logging Utilities
│       ├── db_connection.py
│       └── logger.py
│
├── dimensions/                         <-- Conformed dimension lookup tables (airports, dates, etc.)
├── results/                            <-- Publication-grade results tables & CSV censuses
│   ├── 01_top25_clustering/            # Top 25 spatial census & PCA/K-Means cluster outputs
│   ├── 02_4tier_filtering/             # 4-tier filtering funnel & 9-airport experimental grid
│   ├── 03_lead_lag_deconvolution/      # Lead-lag arrival deconvolution gradients
│   ├── 04_model_execution_2025_holdout/# 2025 out-of-time holdout benchmark matrix
│   └── 05_robustness_resilience_generalizability/ # Deep-dive evaluation tables
└── figures/                            # High-resolution diagrams, network maps, and PCA biplots
```

---

## Methodological Progression & Experimental Cohort Selection

Per the thesis methodology, candidate airfields are selected and processed through a strict two-stage spatial hierarchy:

### Stage 1: Top 25 Operational Clustering (Unsupervised Machine Learning)
1. **Scale Selection**: Restricting analysis to the Top 25 U.S. commercial airfields captures 67.2% of domestic flight movements and isolates heavy-traffic congestion dynamics ($\rho(t) \to 1.0$).
2. **PCA & K-Means Clustering**: PCA extracts 3 principal components (77.0% cumulative variance), while K-Means identifies 4 foundational operational archetypes:
   * **Cluster 0: Mega-Connecting Gateways** (ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO)
   * **Cluster 1: High-Density O&D Focus** (AUS, BOS, CLT, DCA, IAH, TPA)
   * **Cluster 2: High-Reliability Fortress Hubs** (DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC)
   * **Cluster 3: Congested Coastal Originators** (EWR, JFK, LGA)

### Stage 2: Four-Tiered Purposive Filtering Pipeline
1. **Tier 1 (Macro)**: Top 25 scale asymptotics.
2. **Tier 2 (Meso)**: Big 3 mainline carrier symmetry (American, Delta, United) & Southwest Airlines (WN) bimodal arrival exclusion.
3. **Tier 3 (Micro)**: Carrier-exclusive checkpoint screening lanes ($P(\text{Carrier}=j^* \mid \text{Checkpoint } k) = 1.0$).
4. **Tier 4 (Orthogonal Factorial Grid)**: The 9-Airport Experimental Cohort ($3 \times 3$ matrix):
   * **American Airlines (AA)**: DFW, PHL, ORD
   * **Delta Air Lines (DL)**: DTW, LGA, BOS
   * **United Airlines (UA)**: EWR, IAH, LAX

---

## Key Empirical Findings & Model Benchmarks (2025 Out-of-Time Holdout)

All models were trained on Candidate B data (May 2022 – Dec 2023), tuned on 2024 validation data, and benchmarked against 215,562 hourly observations in the full 2025 out-of-time holdout dataset:

| Model Paradigm | ID | Architecture | Test $R^2$ | Test RMSE | Test MAE | Test MASE | Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **Deterministic Baseline** | M0 | Diurnal Seasonal Naive ($y_{t-24}$) | 0.4508 | 1377.3 | 939.8 | 1.000 | Control |
| **Deterministic Baseline** | M1 | Contemporaneous Sched SARIMAX | 0.4375 | 1393.8 | 1042.6 | 1.109 | Baseline |
| **Probabilistic / ML** | M3 | LightGBM Tweedie (Convolved + OTP) | 0.5880 | 1192.9 | 855.1 | 0.910 | High Accuracy |
| **Dynamic Hybrid** | **M5** | **Sequential SARIMA-Tree Hybrid** | **0.6270** | **1135.0** | **795.0** | **0.846** | **WINNER** |

---

## Quick Start & Execution Guide

### 1. Prerequisites & Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/leilagleich/final-thesis.git
cd final-thesis
pip install -r requirements.txt
```

### 2. Execute Master Pipeline
Run the master execution entrypoint:
```bash
python run_pipeline.py
```

### 3. Explore Manuscripts & Recommendations
* Chapter IV Empirical Results: [`thesis/manuscripts/Chapter_4_Results_Empirical_Findings.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis-1/thesis/manuscripts/Chapter_4_Results_Empirical_Findings.md)
* Chapter V Analysis & Discussion: [`thesis/manuscripts/Chapter_5_Analysis_and_Discussion.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis-1/thesis/manuscripts/Chapter_5_Analysis_and_Discussion.md)
* Academic & Operational Recommendations: [`thesis/notes_and_recommendations/Recommendations_Results_and_Discussion.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis-1/thesis/notes_and_recommendations/Recommendations_Results_and_Discussion.md)
* Clustering & 4-Tier Filtering Guide: [`thesis/notes_and_recommendations/Top25_Clustering_and_4Tier_Filtering_Guide.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis-1/thesis/notes_and_recommendations/Top25_Clustering_and_4Tier_Filtering_Guide.md)
* Research Framework & Data Cleaning: [`thesis/notes_and_recommendations/DATA_CLEANING_MODELING_AND_METRICS_FRAMEWORK.txt`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis-1/thesis/notes_and_recommendations/DATA_CLEANING_MODELING_AND_METRICS_FRAMEWORK.txt)
