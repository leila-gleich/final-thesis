# Master Recommendations & Implementation Index

**Document**: `recs-to-implement.md`  
**Location**: `thesis_docs/recommendations/implementation_plans/recs-to-implement.md`  
**Author**: Leila Gleich | **Institution**: Embry-Riddle Aeronautical University (ERAU)  
**Degree Program**: Master of Science in Aeronautics / Aviation Data Analytics  
**Course Milestone**: MSAA / Gleich 700B Graduate Thesis  
**Target Repository**: `final-thesis` (100% Autonomous Master Project)  
**Document Version**: v4.0 (Harmonized Modular Implementation Blueprint)  
**Date of Current Update**: September 30, 2026  

---

## Executive Overview

This master index provides direct access to the 14 individual, modular recommendation implementation files for Leila Gleich's graduate thesis, *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*.

Each recommendation is housed in a standalone Markdown document in `thesis_docs/recommendations/implementation_plans/`, allowing each task to be implemented independently and updated with `STATUS: IMPLEMENTED` upon completion.

---

## Inventory of Modular Recommendation Files

| ID | Recommendation Title | Status Header | Target Implementation Module | Standalone Implementation File |
| :---: | :--- | :---: | :--- | :--- |
| **REC-01** | High-Precision Minute-of-Day & Diurnal Cyclical Features | `NOT IMPLEMENTED` | `src/features/time_features.py` | [`REC-01_Minute_of_Day_and_Diurnal_Cyclical_Terms.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-01_Minute_of_Day_and_Diurnal_Cyclical_Terms.md) |
| **REC-02** | Cluster-Adaptive Lognormal Arrival Deconvolution Kernels | `NOT IMPLEMENTED` | `src/features/cluster_adapt.py` | [`REC-02_Cluster_Adaptive_Lognormal_Arrival_Kernels.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-02_Cluster_Adaptive_Lognormal_Arrival_Kernels.md) |
| **REC-03** | Mandatory DB1B/DB1C Connecting Ratio Capacity Deflation | `NOT IMPLEMENTED` | `src/features/demand_deflat.py` | [`REC-03_Mandatory_DB1B_Connecting_Ratio_Deflation.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-03_Mandatory_DB1B_Connecting_Ratio_Deflation.md) |
| **REC-04** | High-Cardinality Airframe Gauge Tiering | `NOT IMPLEMENTED` | `src/features/fleet_tiers.py` | [`REC-04_High_Cardinality_Airframe_Gauge_Tiering.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-04_High_Cardinality_Airframe_Gauge_Tiering.md) |
| **REC-05** | Dual-Track Model Selection Framework | `NOT IMPLEMENTED` | `src/models/dual_track_eval.py` | [`REC-05_Dual_Track_Model_Selection_Framework.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-05_Dual_Track_Model_Selection_Framework.md) |
| **REC-06** | Strict Standardization on Candidate B (May 1, 2022) | `NOT IMPLEMENTED` | `src/data/split_regimes.py` | [`REC-06_Candidate_B_Demarcation_and_Purge_Embargo.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-06_Candidate_B_Demarcation_and_Purge_Embargo.md) |
| **REC-07** | Airside Surface Taxi-Out & GDP Interaction | `NOT IMPLEMENTED` | `src/features/airside_flow.py` | [`REC-07_Airside_Surface_Taxi_Out_and_GDP_Interaction.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-07_Airside_Surface_Taxi_Out_and_GDP_Interaction.md) |
| **REC-08** | 100% Self-Contained Curated Data Architecture | `NOT IMPLEMENTED` | `data/curated/` & `run_pipe.py` | [`REC-08_Self_Contained_Curated_Data_Architecture.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-08_Self_Contained_Curated_Data_Architecture.md) |
| **REC-09** | Thesis Manuscript & Provenance Synchronization | `NOT IMPLEMENTED` | `thesis/manuscripts/Ch 3-5` | [`REC-09_Thesis_Manuscript_and_Provenance_Synchronization.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-09_Thesis_Manuscript_and_Provenance_Synchronization.md) |
| **REC-10** | PCA Dimensionality Reduction & Loadings Synthesis | `NOT IMPLEMENTED` | `thesis/manuscripts/Ch 3 & 4` | [`REC-10_PCA_Dimensionality_Reduction_and_Loadings.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-10_PCA_Dimensionality_Reduction_and_Loadings.md) |
| **REC-11** | Multi-Pillar Quantitative Evaluation Framework | `NOT IMPLEMENTED` | `src/models/eval_pillars.py` | [`REC-11_Multi_Pillar_Quantitative_Evaluation_Framework.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-11_Multi_Pillar_Quantitative_Evaluation_Framework.md) |
| **REC-12** | Forecasting Paradigm Deployment Strategy | `NOT IMPLEMENTED` | `src/models/paradigms.py` | [`REC-12_Forecasting_Paradigm_Deployment_Strategy.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-12_Forecasting_Paradigm_Deployment_Strategy.md) |
| **REC-13** | Airline-Checkpoint Spatial-Temporal Engine | `NOT IMPLEMENTED` | `src/features/checkpoint_map.py` | [`REC-13_Airline_Checkpoint_Spatial_Temporal_Engine.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-13_Airline_Checkpoint_Spatial_Temporal_Engine.md) |
| **REC-14** | Standardized 3-Phase ETL & Integrity Audit Suite | `NOT IMPLEMENTED` | `src/etl/pipeline_audit.py` | [`REC-14_Standardized_3Phase_ETL_and_Integrity_Audit.md`](file:///Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/final-thesis/thesis_docs/recommendations/implementation_plans/REC-14_Standardized_3Phase_ETL_and_Integrity_Audit.md) |

---

## Recommendation Folder Hierarchy

```
thesis_docs/recommendations/
├── implementation_plans/
│   ├── recs-to-implement.md                                  <-- Master Index (This File)
│   ├── REC-01_Minute_of_Day_and_Diurnal_Cyclical_Terms.md     <-- Individual REC-01 Plan
│   ├── REC-02_Cluster_Adaptive_Lognormal_Arrival_Kernels.md  <-- Individual REC-02 Plan
│   ├── REC-03_Mandatory_DB1B_Connecting_Ratio_Deflation.md  <-- Individual REC-03 Plan
│   ├── REC-04_High_Cardinality_Airframe_Gauge_Tiering.md    <-- Individual REC-04 Plan
│   ├── REC-05_Dual_Track_Model_Selection_Framework.md       <-- Individual REC-05 Plan
│   ├── REC-06_Candidate_B_Demarcation_and_Purge_Embargo.md  <-- Individual REC-06 Plan
│   ├── REC-07_Airside_Surface_Taxi_Out_and_GDP_Interaction.md <-- Individual REC-07 Plan
│   ├── REC-08_Self_Contained_Curated_Data_Architecture.md  <-- Individual REC-08 Plan
│   ├── REC-09_Thesis_Manuscript_and_Provenance_Synchronization.md <-- Individual REC-09 Plan
│   ├── REC-10_PCA_Dimensionality_Reduction_and_Loadings.md  <-- Individual REC-10 Plan
│   ├── REC-11_Multi_Pillar_Quantitative_Evaluation_Framework.md <-- Individual REC-11 Plan
│   ├── REC-12_Forecasting_Paradigm_Deployment_Strategy.md   <-- Individual REC-12 Plan
│   ├── REC-13_Airline_Checkpoint_Spatial_Temporal_Engine.md <-- Individual REC-13 Plan
│   ├── REC-14_Standardized_3Phase_ETL_and_Integrity_Audit.md <-- Individual REC-14 Plan
│   ├── OTP_FACTOR_WEIGHTING_AND_TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md
│   ├── EXECUTION_PLAN_NOTES_AND_RECOMMENDATIONS_UPDATES.md
│   ├── Recommendations_Results_and_Discussion.md
│   └── Updated_Thesis_Project_and_Structure_Recommendation.md
└── chapter_updates/
    ├── 00_README_AND_ROADMAP.md                              <-- Master Manuscript Update Index
    ├── 01_CHAPTER_3_METHODOLOGY_GUIDE.md                     <-- Chapter III Methodological Guide
    ├── 02_CHAPTER_4_RESULTS_TEXT_AND_TABLES.md               <-- Chapter IV Results Text & Tables
    ├── 03_CHAPTER_5_DISCUSSION_AND_ANALYSIS_GUIDE.md         <-- Chapter V Discussion & Analysis
    └── 04_DEFENSE_TALKING_POINTS_AND_COMMITTEE_QA.md         <-- Defense Slide Deck & Committee Q&A
```
