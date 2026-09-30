# Recommendations Directory Index & Architecture

**Location**: `thesis_docs/recommendations/`  
**Author**: Leila Gleich  
**Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Target Repository**: `final-thesis`  
**Date**: September 30, 2026  

---

## Executive Workflow & Maintenance Protocols

To ensure all 14 technical recommendations are implemented consistently, consult the master workflow guide:
- 📖 **[`EXECUTION_WORKFLOW_AND_MAINTENANCE_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/EXECUTION_WORKFLOW_AND_MAINTENANCE_GUIDE.md)**: Establishes the uniform 5-step implementation loop, status transition lifecycle (`STATUS: NOT IMPLEMENTED` $\to$ `STATUS: IMPLEMENTED` $\to$ `STATUS: VERIFIED`), code standards, and unit testing requirements.

---

## Directory Architecture

```
thesis_docs/recommendations/
├── README.md                                       <-- Master Index (This File)
├── EXECUTION_WORKFLOW_AND_MAINTENANCE_GUIDE.md     <-- Uniform Implementation Protocol & Workflow
├── implementation_plans/   <-- Modular, task-by-task code implementation plans (REC-01 to REC-14)
└── chapter_updates/        <-- Step-by-step manuscript chapter update guides (Chapters 3, 4, 5 & Defense)
```

---

## 1. Technical Implementation Plans (`implementation_plans/`)

Each recommendation is housed in an individual Markdown file in [`implementation_plans/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/). Every file contains a tracking header (`# STATUS: NOT IMPLEMENTED`) that should be updated to `# STATUS: IMPLEMENTED` once complete.

| Recommendation ID | Focus & Target Module | Modular File Path |
| :---: | :--- | :--- |
| **REC-01** | High-Precision Minute-of-Day & Diurnal Cyclical Features | [`REC-01_Minute_of_Day_and_Diurnal_Cyclical_Terms.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-01_Minute_of_Day_and_Diurnal_Cyclical_Terms.md) |
| **REC-02** | Cluster-Adaptive Lognormal Arrival Deconvolution Kernels | [`REC-02_Cluster_Adaptive_Lognormal_Arrival_Kernels.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-02_Cluster_Adaptive_Lognormal_Arrival_Kernels.md) |
| **REC-03** | Mandatory DB1B/DB1C Connecting Ratio Capacity Deflation | [`REC-03_Mandatory_DB1B_Connecting_Ratio_Deflation.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-03_Mandatory_DB1B_Connecting_Ratio_Deflation.md) |
| **REC-04** | High-Cardinality Airframe Gauge Tiering | [`REC-04_High_Cardinality_Airframe_Gauge_Tiering.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-04_High_Cardinality_Airframe_Gauge_Tiering.md) |
| **REC-05** | Dual-Track Model Selection Framework | [`REC-05_Dual_Track_Model_Selection_Framework.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-05_Dual_Track_Model_Selection_Framework.md) |
| **REC-06** | Candidate B Demarcation (May 1, 2022) & 7-Day Purge Embargo | [`REC-06_Candidate_B_Demarcation_and_Purge_Embargo.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-06_Candidate_B_Demarcation_and_Purge_Embargo.md) |
| **REC-07** | Airside Surface Taxi-Out & GDP Interaction | [`REC-07_Airside_Surface_Taxi_Out_and_GDP_Interaction.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-07_Airside_Surface_Taxi_Out_and_GDP_Interaction.md) |
| **REC-08** | 100% Self-Contained Curated Data Architecture | [`REC-08_Self_Contained_Curated_Data_Architecture.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-08_Self_Contained_Curated_Data_Architecture.md) |
| **REC-09** | Thesis Manuscript & Provenance Synchronization | [`REC-09_Thesis_Manuscript_and_Provenance_Synchronization.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-09_Thesis_Manuscript_and_Provenance_Synchronization.md) |
| **REC-10** | PCA Dimensionality Reduction & Loadings Synthesis | [`REC-10_PCA_Dimensionality_Reduction_and_Loadings.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-10_PCA_Dimensionality_Reduction_and_Loadings.md) |
| **REC-11** | Multi-Pillar Quantitative Evaluation Framework | [`REC-11_Multi_Pillar_Quantitative_Evaluation_Framework.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-11_Multi_Pillar_Quantitative_Evaluation_Framework.md) |
| **REC-12** | Forecasting Paradigm Deployment Strategy | [`REC-12_Forecasting_Paradigm_Deployment_Strategy.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-12_Forecasting_Paradigm_Deployment_Strategy.md) |
| **REC-13** | Airline-Checkpoint Spatial-Temporal Engine | [`REC-13_Airline_Checkpoint_Spatial_Temporal_Engine.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-13_Airline_Checkpoint_Spatial_Temporal_Engine.md) |
| **REC-14** | Standardized 3-Phase ETL & Integrity Audit Suite | [`REC-14_Standardized_3Phase_ETL_and_Integrity_Audit.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-14_Standardized_3Phase_ETL_and_Integrity_Audit.md) |

---

## 2. Manuscript Chapter Update Guides (`chapter_updates/`)

The [`chapter_updates/`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/) subdirectory provides turn-key text, mathematical equations, markdown tables, and slide deck guides for editing the manuscript:

| Guide File | Target Chapter / Purpose | Key Focus |
| :--- | :--- | :--- |
| **[`00_README_AND_ROADMAP.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/00_README_AND_ROADMAP.md)** | Master Roadmap & Index | Overall manuscript update sequence & checklist. |
| **[`01_CHAPTER_3_METHODOLOGY_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/01_CHAPTER_3_METHODOLOGY_GUIDE.md)** | Chapter III: Methodology | PCA derivation, lognormal kernel equations, Candidate B split. |
| **[`02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md)** | Chapter IV: Empirical Findings | Tables 4.1–4.10, PCA factor loadings, 2025 holdout benchmark matrix. |
| **[`03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md)** | Chapter V: Discussion & Analysis | Dual-track policy, lead-lag asynchrony, security-airside delay coupling. |
| **[`04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/chapter_updates/04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md)** | Defense Deck & Committee Defense | 20–25 slide deck outline, talking points, anticipated committee Q&A. |
