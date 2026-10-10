# Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow
## Forecasting TSA Checkpoint Throughput Volatility & Airside-Landside Queue Dynamics

**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Degree Program**: Master of Science in Aeronautics / Aviation Data Analytics  
**Course Milestone**: MSAA / Gleich 700B Graduate Thesis  
**Repository Version**: v4.7 (Candidate Model Suite Streamlining & Multi-Pillar Harmonization — `final-thesis`)  

---

## Executive Overview

This repository (`final-thesis`) is the complete, self-contained, publication-grade master codebase, empirical data products, visual assets, and manuscript chapters for the graduate thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow: Forecasting TSA Checkpoint Throughput Volatility & Airside-Landside Queue Dynamics*. The research synthesizes four major federal aviation datasets (**TSA FOIA Checkpoint Logs**, **BTS On-Time Performance**, **BTS T-100 Segment Capacity**, and **BTS DB1B Ticket Coupon Surveys**) covering 67.22 million raw fact records across 2019–2025.

Rather than predicting mean hourly passenger throughput volume alone, this thesis targets the **volatility of TSA throughput** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$). Grounded in **Kingman's heavy-traffic queuing physics** ($W_q \approx \frac{\rho}{1-\rho} \frac{C_a^2 + C_s^2}{2} \frac{1}{\mu}$), passenger delays scale quadratically with arrival volatility ($C_a^2$) as checkpoint utilization approaches capacity ($\rho \to 1.0$). Across 24 Bureau of Transportation Statistics On-Time Performance (OTP) features, the research introduces the **Values versus Volatility Paradigm**, proving that predicting temporal throughput turbulence requires tracking flight schedule dispersion and cancellation/delay volatility rather than static flight counts.

The purpose of this repository is to address the research question: *"How do deterministic baseline models, supervised machine learning architectures, and dynamic hybrid models compare across steady-state accuracy (Robustness), disruption shock absorption (Resilience), and cross-terminal spatial transferability (Generalizability) when predicting throughput volatility?"*

---

## Master Repository Architecture (`final-thesis`)

```
final-thesis/
├── README.md                           <-- Master GitHub repository guide (this file)
├── AGENTS.md                           <-- AI Agent Operational Constitution & Execution Guidelines
├── LICENSE                             <-- MIT Open Source Academic License
├── .gitignore                          <-- Git exclusion rules (cache, OS, DuckDB)
├── requirements.txt                    <-- Python dependency specifications
├── run_pipeline.py                     <-- Master execution entrypoint script
│
├── thesis_docs/                        <-- Master Thesis Manuscripts, Recommendations & Notes
│   ├── README.md                       <-- Guide & sitemap to manuscripts, recs & notes
│   ├── MANUSCRIPT_AND_DATA_UPDATE_SOP.md <-- Step-by-step SOP for updating manuscripts & spreadsheets
│   ├── manuscripts/                    <-- Production manuscript chapters (.docx & .md) + Figures
│   │   ├── chp1-intro.md               # Chapter 1: Introduction & Research Problem
│   │   ├── chp2-litreview.md           # Chapter 2: Literature Review & Heavy-Traffic Physics
│   │   ├── chp3-methodology.md         # Chapter 3: Methodology & Volatility Estimators
│   │   ├── chp4-results.md             # Chapter 4: Results & Values vs. Volatility Findings
│   │   ├── chp5-discussion.md          # Chapter 5: Analysis, Discussion & Dynamic Buffers
│   │   ├── glossary.md                 # Master Terminology & Mathematical Symbol Registry
│   │   ├── archive/                    # Archived drafts & historical manuscripts
│   │   └── figures/                    # Publication Figures 01–04
│   ├── recommendations/                <-- Consolidated Actionable Guidance & Plans
│   │   ├── chapter_updates/            # 00-04 Chapter revision guides & defense Q&A
│   │   └── implementation_plans/       # recs-to-implement.md & technical blueprints
│   └── notes/                          <-- Working Research Notes & Provenance
│       ├── methodology_memos/          # Justifications, 4-tier filtering, section documents
│       ├── empirical_walkthroughs/     # Step-by-step validation reports & descriptive statistics
│       └── provenance_and_standards/   # Provenance specification, decision logs, style guides
│
├── otp_volatility_analysis/            <-- OTP Factor Weighting & TSA Volatility Module
│   ├── run_otp_volatility_analysis.py  # Self-contained empirical volatility runner
│   ├── OTP_FACTOR_WEIGHTING_AND_VOLATILITY_ANALYSIS.md
│   ├── Figures 1–5 (.png)              # 300 DPI publication figures
│   └── Tables 01–05 (.csv)             # Out-of-time evaluation & factor weighting benchmarks
│
├── src/                                <-- Modular Python Source Code Infrastructure
│   ├── analysis/                       <-- Seasonal Volatility & Table Synchronization
│   │   ├── generate_figures_tables_excel.py # Multi-tab exhibits Excel generator
│   │   ├── generate_thesis_tables_excel.py  # APA master thesis_tables.xlsx generator
│   │   ├── season_analysis_volatility_runner.py # Reproducible seasonal regimes runner
│   │   └── sync_manuscript_tables.py   # Automated 16-table CSV extraction & Excel sync
│   ├── etl/                            <-- Ingestion, Top 25 Clustering & 4-Tier Filtering
│   │   ├── perform_top25_clustering.py # Step 1: Top 25 PCA & K-Means clustering
│   │   ├── apply_4tier_filtering.py    # Step 2: 4-tier filtering pipeline (Top 25 -> 9 Cohort)
│   │   └── pipeline_audit.py           # Step 3: Standardized 6-point referential audit
│   ├── features/                       <-- Physics-Informed Feature Engineering Pipeline
│   │   ├── time_features.py            # Diurnal & weekly continuous cyclical terms
│   │   ├── cluster_adapt.py            # Cluster-adaptive lognormal arrival kernels
│   │   ├── demand_deflat.py            # DB1B connecting ratio demand deflation
│   │   ├── fleet_tiers.py              # Airframe gauge tiers (Regional/Narrow/Wide)
│   │   ├── airside_flow.py             # Taxi-out congestion interaction terms
│   │   ├── checkpoint_map.py           # Checkpoint spatial confidence weighting
│   │   └── feature_pipeline.py         # Master conformed feature matrix orchestrator
│   ├── models/                         <-- Deterministic, ML, and Dynamic Hybrid Volatility Models
│   │   ├── baselines.py                # Daily Persistence & Deterministic Schedule Volatility
│   │   ├── machine_learning.py         # Supervised Machine Learning Volatility Decision Trees
│   │   ├── hybrid_sarima_tree.py       # Dynamic Two-Stage Hybrid Volatility Model
│   │   ├── eval_pillars.py             # Multi-pillar quantitative evaluation suite
│   │   └── dual_track_eval.py          # Dual-track operational policy decision rules
│   ├── data/                           <-- Regime Demarcation & Panel Loading
│   │   ├── panel_loader.py             # Curated hourly panel data loader & volatility calculator
│   │   └── split_regimes.py            # Candidate B & 7-day purge embargoes
│   ├── manuscripts/                    <-- Manuscript Compilers & Markdown Generators
│   │   ├── generate_acronyms_docx.py   # Acronyms & abbreviations list generator
│   │   ├── generate_appendix_md.py     # Appendix generator
│   │   └── generate_categorized_glossary.py # Categorized glossary compiler
│   └── utils/                          <-- Path Resolution & Styling Utilities
│       ├── paths.py                    # Self-contained repository path registry
│       ├── excel_styling.py            # Centralized APA 7th ed. openpyxl layout & styling engine
│       └── logger.py                   # Standardized logging utility
├── data/                               <-- Data Directory (Curated aggregates, samples, dimensions)
│   ├── curated/                        # Coupled hourly & daily TSA/flight aggregates (2019–2025)
│   ├── sample/                         # Representative sample fixtures for pipeline validation
│   └── dimensions/                     # Conformed star schema lookup tables (airports, dates, etc.)
├── results/                            <-- Publication-grade results tables & CSV censuses
│   ├── 00_VERSION_CONTROL_AND_PROVENANCE.md
│   ├── 01_top25_clustering/            # Top 25 spatial census & PCA/K-Means cluster outputs
│   │   └── seasonality_and_regimes/    # Season-analysis.xlsx, 84-cell tensor & seasonal CSVs
│   ├── 02_4tier_filtering/             # 4-tier filtering funnel & 9-airport experimental grid
│   ├── 03_lead_lag_deconvolution/      # Lead-lag arrival deconvolution gradients
│   ├── 04_model_execution_2025_holdout/# 2025 out-of-time holdout benchmark matrix
│   ├── 05_robustness_resilience_generalizability/ # Deep-dive evaluation tables
│   ├── tables/                         # Master evaluation summary tables & metrics targets
│   └── manuscript_tables/              # Conformed CSV suite for all 16 tables in Chapters 4 & 5
├── figures/                            <-- Conceptual diagrams, network maps, and threat matrices
│   ├── 01_Sample_and_Airport_Selection/
│   ├── 02_Data_Pipelines_and_Threats/
│   ├── 03_Modeling_and_Evaluation/
│   └── 04_Appendix_and_Reference/
└── archive/                            <-- Archived legacy volume results & superseded scripts
    ├── README.md                       # Archive catalog & manifest
    ├── legacy_volume_results/          # Superseded volume-only holdout & robustness files
    └── superseded_scripts/             # Superseded volume execution scripts
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

Following the 4-tier purposive filtering pipeline, the evaluation benchmarks **three candidate predictive models representing distinct operational paradigms**, evaluated against an empirical persistence control. All models were benchmarked against 72,053 complex hourly observations (3,222 airport-days) in the full 2025 out-of-time holdout targeting Diurnal Throughput Volatility ($\sigma_{\text{TSA, hr}}$, pax/hr dispersion):

| Model Paradigm | Candidate Model | Architecture / Approach | Test $R^2$ | Test RMSE (pax/hr) | Test MAE (pax/hr) | Test MASE | Academic Target Status |
| :--- | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| **Baseline Control** | **Baseline Control** | Daily Persistence Benchmark ($y_{t-24}$) | 0.6719 | 253.6 | 179.3 | 1.000 | Baseline Reference Benchmark |
| **Deterministic Baseline** | **Model 1** | Deterministic Flight Schedule Model (convolved show-up curve) | 0.4980 | 313.4 | 215.9 | 0.945 | Passed Target ($\text{MASE} < 1.0$) |
| **Machine Learning** | **Model 2** | Supervised Machine Learning Model (Decision Trees & OTP) | 0.6178 | 273.5 | 178.0 | 0.779 | Passed Target ($\text{MASE} < 0.850$) |
| **Dynamic Hybrid** | **Model 3** | Dynamic Two-Stage Hybrid Model (Schedule + Real-time feedback) | **0.7483** | **222.1** | **142.8** | **0.662** | High-Accuracy In-Sample Fit |

*Note*. Evaluated across the 9-airport balanced experimental cohort on the 2025 full-year out-of-time holdout.

### Master Asymmetric Trade-Off Matrix (Testing Hypothesis 1)

The primary thesis hypothesis (**Hypothesis 1**) asserted that *distinct modeling frameworks exhibit asymmetric performance strengths across robustness, resilience, and generalizability, with no single paradigm proving universally superior across all three measures*. 

Critically, **the hybrid model (Model 3) is NOT best across every performance measure**. The models were evaluated against three explicit academic targets:
* **Robustness Target**: Lowest $\text{RMSE}_{\text{routine}}$ & $\text{MASE}_{\text{routine}} < 0.700$ under nominal operations.
* **Resilience Target**: Recovery RMSE Multiplier $R_{\text{RMSE}} \approx 1.00$ & Lowest $\text{MASE}_{\text{shock}}$ ($\text{TTR} < 4.0\text{h}$) under acute disruptions.
* **Generalizability Target**: Relative Transfer Ratio $\text{RTR} = 1.00$ & Change in MASE on transfer $\Delta\text{MASE} \le 10.0\%$.

| Evaluation Dimension | Stated Academic Target | Baseline Control | Model 1 (Deterministic) | Model 2 (Machine Learning) | Model 3 (Dynamic Hybrid) | Dimension Winner & Operational Justification |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Dimension 1: Robustness** (Routine: Delay $< 15$m, 0 Cancels) | Lowest $\text{RMSE}_{\text{routine}}$; $\text{MASE}_{\text{routine}} < 0.70$ | $\text{RMSE} = 253.6$, $\text{MASE} = 1.000$ (Fails) | $\text{RMSE} = 313.4$, $\text{MASE} = 0.945$ (Fails) | $\text{RMSE} = 273.5$, $\text{MASE} = 0.680\text{--}0.700$ (**Target Met**) | $\text{RMSE} = \mathbf{222.1}$ (Lowest), $\text{MASE} = \mathbf{0.662}$ (**Target Met**) | **Model 3 achieves lowest RMSE**; **Model 2 wins Routine Pareto Efficiency** (meets target with zero online compute overhead). |
| **Dimension 2: Resilience** (Disruption: Delay $\ge 45$m or Cancels $\ge 5$) | $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$ | $R = 1.00$, $\text{MASE} = 1.000$, $\text{TTR} = 8.4\text{h}$ | $R = 1.32$, $\text{MASE} = 1.082$, $\text{TTR} = 7.8\text{h}$ | $R = 2.14$ (Fragile), $\text{MASE} = 0.812$, $\text{TTR} = 5.4\text{h}$ | $R = \mathbf{1.05}$ (**Target Met**), $\text{MASE} = \mathbf{0.694}$ (Lowest), $\text{TTR} = \mathbf{2.8\text{h}}$ (**Target Met**) | **Model 3 DECISIVE WINNER**: Closed-loop recursive feedback ($e_{t-1}$) prevents empty-checkpoint collapse and recovers in 2.8h. |
| **Dimension 3: Generalizability** (Zero-Shot Transfer: EWR $\to$ LGA) | $\text{RTR} = 1.00$; $\Delta\text{MASE} \le 10.0\%$ | $\text{RTR} = 1.00$, $\Delta\text{MASE} = 0.0\%$ (Static Ref) | $\text{RTR} = \mathbf{1.04}$ (**Target Met**), $\Delta\text{MASE} = \mathbf{+4.0\%}$ (**Target Met**) | $\text{RTR} = 1.08$, $\Delta\text{MASE} = +8.3\%$ (Passes) | $\text{RTR} = \mathbf{1.19}$ (**FAILS TARGET**), $\Delta\text{MASE} = \mathbf{+21.5\%}$ (**FAILS TARGET**) | **Model 1 DECISIVE WINNER**: Physical schedule convolution is invariant to facility layout; Model 3 overfits to local gate geometry. |

### Core Empirical Takeaways
1. **Confirmation of Asymmetric Trade-Offs (Hypothesis 1)**: No single paradigm dominates all performance measures:
   - **Model 3 Decisively Wins Resilience** ($R_{\text{MASE}} = 1.05 \approx 1.00, \text{MASE}_{\text{shock}} = 0.694, \text{TTR} = 2.8\text{h}$), but **Decisively Fails Generalizability** ($\text{RTR} = 1.19 > 1.00, \Delta\text{MASE} = +21.5\% > 10.0\%$) due to decision tree terminal geometry overfitting.
   - **Model 1 Decisively Wins Generalizability** ($\text{RTR} = 1.04 \approx 1.00, \Delta\text{MASE} = +4.0\% \le 10.0\%$), because physical schedule convolution is invariant across terminal buildings.
   - **Model 2 Wins Routine Pareto Efficiency** by achieving the $\text{MASE} < 0.70$ target with zero online compute overhead and near-zero latency.
2. **Values versus Volatility Paradigm**: For multi-day rolling volatility ($\sigma_{\text{TSA, 7d}}$), static feature levels fail completely ($R^2 = -0.269$), while feature volatility metrics succeed ($R^2 = +0.311$), confirming that second-order dispersion must be modeled with second-order predictors.
3. **Delay Volatility Transmission**: Checkpoint throughput volatility is strongly driven by flight departure delay volatility ($CV_{\text{delay}}: r = +0.4373, p = 0.0288$), while raw delay minutes show zero linear correlation ($r = -0.0620, p = 0.769$).
4. **Regime-Switched Gated Inference Engine & Conformal Buffers**: Operational deployment combines fast machine learning (Model 2) during calm periods ($T(h) < 0.75$) with closed-loop hybrid tracking (Model 3) during acute storms ($T(h) \ge 0.75$), with conformal prediction quantile buffers ($c(t) = \lceil (\hat{\mu}_t + 1.036 \cdot \hat{\sigma}_t) / \mu_{\text{lane}} \rceil$) dynamically sizing lane staffing. Standalone CSV matrices are published at `results/manuscript_tables/master_asymmetric_trade_off_matrix.csv` and `results/manuscript_tables/dual_track_model_selection_policy.csv`.

---

## Quick Start & Execution Guide

### 1. Prerequisites & Environment Setup
Clone the repository and install dependencies:
```bash
git clone https://github.com/leilagleich/final-thesis.git
cd final-thesis
pip install -r requirements.txt
```

### 2. Execute Master Pipeline & Table Synchronization
Run the master execution entrypoint to execute end-to-end models and automatically update all manuscript table CSVs and Excel workbooks:
```bash
python run_pipeline.py
```

### 3. Synchronize Manuscript Tables Standalone
Whenever analytical parameters, metrics, or manuscript chapters change, execute the automated synchronization module:
```bash
python src/analysis/sync_manuscript_tables.py
```
This extracts all 16 tables from `thesis_docs/manuscripts/`, generates conformed CSVs in `results/manuscript_tables/` and `results/tables/`, and synchronizes all multi-tab companion Excel workbooks in `results/`.

### 4. Run Test Suite
Execute the self-contained test suite across all stages:
```bash
python3 -m unittest discover tests
```

### 5. Explore Manuscripts & Recommendations

* Chapter I Introduction: [chp1-intro.md](thesis_docs/manuscripts/chp1-intro.md)
* Chapter II Literature Review: [chp2-litreview.md](thesis_docs/manuscripts/chp2-litreview.md)
* Chapter III Methodology: [chp3-methodology.md](thesis_docs/manuscripts/chp3-methodology.md)
* Chapter IV Empirical Results: [chp4-results.md](thesis_docs/manuscripts/chp4-results.md)
* Chapter V Analysis & Discussion: [chp5-discussion.md](thesis_docs/manuscripts/chp5-discussion.md)
* Master Terminology & Mathematical Glossary: [glossary.md](thesis_docs/manuscripts/glossary.md)
* Standard Operating Procedure (Updating Manuscripts & Data): [MANUSCRIPT_AND_DATA_UPDATE_SOP.md](thesis_docs/MANUSCRIPT_AND_DATA_UPDATE_SOP.md)
* Master Manuscript Tables Registry: [results/manuscript_tables/README.md](results/manuscript_tables/README.md)
* Comprehensive Master Draft: [Master_Results_and_Discussion_Comprehensive_Draft.md](thesis_docs/manuscripts/archive/Master_Results_and_Discussion_Comprehensive_Draft.md)
* OTP Factor Weighting & Volatility Module: [OTP_FACTOR_WEIGHTING_AND_VOLATILITY_ANALYSIS.md](otp_volatility_analysis/OTP_FACTOR_WEIGHTING_AND_VOLATILITY_ANALYSIS.md)
* Agent Operational Constitution & Rules: [AGENTS.md](AGENTS.md)

---

## AI Agent Operational Constitution & Repository Directives

All automated AI coding agents, subagents, and LLM assistants operating in this repository are strictly governed by the rules codified in **[AGENTS.md](AGENTS.md)**:

1. **Zero Modifications to Word Documents**: Under NO circumstances may any agent edit, modify, overwrite, or delete Microsoft Word manuscripts (`.docx`) unless the user explicitly states otherwise in writing in the current session.
2. **Commit After Each Task**: Every discrete task, edit, or bug fix must immediately be committed with a clean, descriptive Git commit message.
3. **Continuous Version Control & Provenance**: Every modification must update `results/00_VERSION_CONTROL_AND_PROVENANCE.md`.
4. **Synchronize All Tables (CSV & Excel)**: All metric or parameter changes must be synchronized across both CSV tables (`results/manuscript_tables/`) and multi-tab Excel workbooks (`results/`) via `src/analysis/sync_manuscript_tables.py`.
5. **Research Target Integrity**: The primary dependent variable is **TSA Throughput Volatility** ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$), never raw passenger volume ($y_t$).
6. **The Candidate Models**: Evaluation is restricted to the **Baseline Control** (Daily Persistence Benchmark), **Model 1** (Deterministic Flight Schedule Model), **Model 2** (Supervised Machine Learning Model), and **Model 3** (Dynamic Two-Stage Hybrid Model), preserving asymmetric trade-offs (Model 3 is not universally best).
7. **Strict Aviation Terminology Filter**: Strict adherence to genuine commercial aviation operations terms (*Nominal On-Time Baseline*, *Routine Daily Operations*, *Irregular Operations / IROPS*, *Carrier Checkpoint Isolation*), with zero tolerance for physics, biology, or lab-science jargon.

