# RESEARCH DATA PROVENANCE, INTEGRITY & VERSION CONTROL SPECIFICATION
====================================================================================================
PROJECT: Empirical Modeling of Airport Security Screening Demand and Flight Performance Coupling
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
LOCATION: results/00_VERSION_CONTROL_AND_PROVENANCE.md
RELEASE VERSION: v4.8 (Excision of 'Physics' & Theoretical Jargon for Qualitative Audience Calibration)
DATE: October 5, 2026
====================================================================================================

----------------------------------------------------------------------------------------------------
1. VERSION CONTROL & RELEASE HISTORY
----------------------------------------------------------------------------------------------------
This analytical repository adheres to strict Semantic Data Versioning (SemVer-Data) to ensure full 
auditability, reproducibility, and referential integrity across all empirical findings.

+---------+------------+----------------------------------------------------------------------------+
| Version | Release    | Scope, Milestones, and Architectural Changes                               |
+---------+------------+----------------------------------------------------------------------------+
| v0.1    | 2026-01-15 | Raw Upstream Data Ingestion: Extracted 67,222,828 raw federal records from |
|         |            | TSA FOIA logs, BTS OTP, BTS T-100, and BTS DB1B archives (7.12 GB staging).|
| v1.0    | 2026-03-20 | Initial Pre-ETL Staging: Established Star Schema conformed dimension tables|
|         |            | (dim_date, dim_time_block, dim_airport, dim_airline, dim_aircraft,         |
|         |            | dim_checkpoint). Initial data quality scans identified spatial missingness.|
| v2.0    | 2026-06-10 | Post-ETL Conformed Star Schema Warehouse: Vectorized DuckDB pipeline       |
|         |            | synthesized 42,062,039 conformed records. Applied checkpoint fingerprint-  |
|         |            | ing, structural zero preservation, and tactical cancellation rules.        |
| v2.2    | 2026-07-28 | Temporal Demarcation: Selected Candidate B (Post-Mask Mandate Regime:      |
|         |            | May 1, 2022 to December 31, 2025; 44 continuous months) via CUSUM tests    |
|         |            | and rolling Welch t-test convergence across passenger arrival curves.      |
| v2.5    | 2026-08-30 | Purposive 4-Tier Filtering & 9-Airport Experimental Cohort: Isolated       |
|         |            | carrier-exclusive screening lanes (BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, |
|         |            | PHL) for orthogonal Wiener-Hopf deconvolution; partitioned 2025 holdout.   |
| v3.0    | 2026-09-17 | Unified Results Architecture Release & Multi-Tab Excel Consolidation:      |
|         |            | Consolidates all four federal feeds, the Executive Summary Suite, the      |
|         |            | 25-airport master census, coupled cross-dataset dynamics, and domain-      |
|         |            | organized results into multi-tab Excel workbooks; archived component CSVs. |
| v3.1    | 2026-09-24 | Unified Results Hub: Consolidated Results_and_Analysis/ and results/ into a |
|         |            | single canonical results/ hub with full parity to final-thesis.             |
| v3.2    | 2026-09-27 | Coupled Volatility & Temporal Regimes Integration: Integrated Coupled      |
|         |            | Volatility Index, Diurnal Turbulence Shock Index, and 84-cell tensor into  |
|         |            | Chapter III; added Tables 4.3b, 4.4a-c and Figures 4.1–4.4 to Chapter IV;  |
|         |            | enriched Chapter V with Lead-Lag Asynchrony, Empty Checkpoint Fallacy,     |
|         |            | Volatility Archetypes, and Regime-Switched Gated Inference Engine.         |
| v3.3    | 2026-09-27 | Harmonized Sample Size & Partitioning Provenance: Corrected Candidate B    |
|         |            | training duration (32 mo dev / 44 mo total); disambiguated Top 25 system   |
|         |            | hours (23,400 / 8,760) and 9-airport complex counts (122,847 / 72,053)     |
|         |            | from raw candidate facility logs (404k / 215k); logged prompt rationale.   |
| v3.4    | 2026-09-28 | Methodological Harmonization & Two-Chapter Finalization:                   |
|         |            | - Formalized balanced 4x4 factorial design across 9 hubs.                  |
|         |            | - Verified OTP departing flights scope (unrestricted destinations).        |
|         |            | - Econometrically confirmed Type I vs. Type II layout invariance           |
|         |            |   via two-sample Kolmogorov-Smirnov test (D = 0.032, p = 0.28).            |
|         |            | - Rebuilt M1 deterministic static 2-hr lead baseline (R^2 = 0.5293).       |
|         |            | - Structured formal Chapter IV (Findings) and Chapter V (Analysis) split.  |
| v3.5    | 2026-09-30 | Self-Contained Repository Consolidation & Hypothesis Harmonization:        |
|         |            | - Migrated 71 supplementary assets from legacy Gleich-Thesis.              |
|         |            | - Integrated reproducible seasonal analysis runner and data tables.        |
|         |            | - Harmonized Chapter 5 to evaluate single overarching Hypothesis 1 across   |
|         |            |   three operational dimensions (Robustness, Resilience, Generalizability). |
|         |            | - Integrated master OTP factor weighting & TSA volatility plan (v3.2).     |
| v4.0    | 2026-09-30 | Full Implementation of Recommendations REC-01 through REC-14:              |
|         |            | - Phase 1: 6-point pipeline integrity audit (REC-14), self-contained paths  |
|         |            |   (REC-08), Candidate B temporal demarcation & 7-day purge embargo (REC-06).|
|         |            | - Phase 2: Live PCA & K-Means 80.5% variance clustering (REC-10), balanced  |
|         |            |   4x4 factorial design with 12 carrier facilities across 9 hubs.            |
|         |            | - Phase 3: Physics-informed feature pipeline: diurnal/weekly cyclical terms  |
|         |            |   (REC-01), cluster-adaptive lognormal kernels (REC-02), DB1B connecting     |
|         |            |   deflation (REC-03), gauge tiering (REC-04), taxi/GDP interaction (REC-07), |
|         |            |   checkpoint carrier spatial mapping (REC-13).                              |
|         |            | - Phase 4: Models & Multi-Pillar Engine: M0 seasonal naive, M1 rebuilt      |
|         |            |   2-hr lead, M3 Tweedie tree, M5 sequential SARIMA-Tree hybrid, 14-metric   |
|         |            |   MultiPillarEvaluator (REC-11), dual-track decision engine (REC-05),        |
|         |            |   conformal quantile intervals & q85 staffing bounds (REC-12).              |
|         |            | - Phase 5: Manuscript & Provenance Synchronization (REC-09), complete test  |
|         |            |   coverage (36/36 passing), zero test regressions, fully autonomous run.     |
| v4.1    | 2026-10-04 | Chapter IV Outline Harmonization, SSOT Deployment & Manuscript Cleanup:     |
|         |            | - Rewrote Chapter IV manuscript (Chapter_4_Results_Empirical_Findings.md)   |
|         |            |   to strictly follow the 4-part, 17-subsection outline (4.1 Initial EDA,    |
|         |            |   4.2 Data Filtering & Subset Selection, 4.3 Model Development & Execution, |
|         |            |   4.4 Model Evaluation & Results).                                          |
|         |            | - Authored Chapter IV Single Source of Truth data registry and spec.        |
|         |            | - Archived non-SSOT / superseded precursor files to                          |
|         |            |   thesis_docs/manuscripts/archive/ to eliminate version ambiguity.          |
|         |            | - Synchronized file trees across thesis_docs/README.md and provenance logs. |
| v4.2    | 2026-10-04 | Full SSOT Directory Deployment Across All Five Chapters:                    |
|         |            | - Created dedicated first-class directory: thesis_docs/ssot/.               |
|         |            | - Moved Chapter_4_SSOT.md to canonical location thesis_docs/ssot/.          |
|         |            | - Authored authoritative SSOT documents for Chapter 1 (Introduction/Scope), |
|         |            |   Chapter 2 (Literature Review), Chapter 3 (Methodology), Chapter 4         |
|         |            |   (Findings/Results), and Chapter 5 (Analysis/Discussion).                  |
|         |            | - Created thesis_docs/ssot/README.md establishing SSOT governance,          |
|         |            |   companion draft mapping, benchmark registries, and jargon rules.          |
|         |            | - Updated thesis_docs/README.md to establish the 4-pillar thesis structure. |
| v4.3    | 2026-10-05 | Codebase Modularization & Repository Architecture Consolidation:            |
|         |            | - Exposed splitters, transformers, and evaluation engines in src package    |
|         |            |   inits (src.data, src.features, src.models).                              |
|         |            | - Relocated seasonal volatility data to results/seasonality_and_regimes/    |
|         |            |   and migrated analysis runner to src/analysis/.                           |
|         |            | - Archived superseded DuckDB/ETL scripts to archive/superseded_scripts/.    |
|         |            | - De-duplicated draft recommendations to thesis_docs/manuscripts/archive/. |
|         |            | - Standardized requirements and docstrings for HistGradientBoostingRegressor.|
|         |            | - Validated 100% self-contained architecture check and 36/36 unit tests.   |
| v4.4    | 2026-10-05 | Manuscript Table CSV Suite & Results Excel Synchronization:                |
|         |            | - Created results/manuscript_tables/ containing conformed CSVs for all 16   |
|         |            |   tables across Chapters 4 & 5 (with canonical names and short aliases).   |
|         |            | - Re-synchronized all Excel workbooks in results/ (04_model_execution,     |
|         |            |   03_lead_lag, 05_robustness, 02_top9) with thesis updates.                |
|         |            | - Added M1* Deterministic 2-Hour Static Lead Baseline across holdout tables.|
|         |            | - Harmonized Table 4.9 lead-lag arrival transfer dynamics across workbooks. |
|         |            | - Deployed automated synchronization runner (src/analysis/sync_manuscript_  |
|         |            |   tables.py) integrated as Step 8 into run_pipeline.py.                    |
|         |            | - Updated all READMEs with automated synchronization instructions.          |
| v4.5    | 2026-10-05 | Throughput Volatility Overhaul & 4-Model Canonical Suite Audit:             |
|         |            | - Re-targeted core research from raw volume to TSA throughput volatility    |
|         |            |   (within-day sigma_TSA, scale-free CV_TSA, and 7-day rolling sigma_7d).    |
|         |            | - Consolidated model suite to exactly 4 canonical models (M0, M1*, M3, M5)  |
|         |            |   and documented pruning of exploratory variants (M1, M2, M4).             |
|         |            | - Formalized explicit academic performance targets across Robustness,       |
|         |            |   Resilience, and Generalizability.                                        |
|         |            | - Verified Master Asymmetric Trade-Off Matrix: M5 wins Resilience, M1* wins|
|         |            |   Generalizability, M3 wins Routine Pareto Efficiency.                     |
|         |            | - Replaced technical jargon with defensible APA 7 aviation terminology.     |
|         |            | - Safely archived legacy SSOT, early notes, and draft recs to archive/.     |
|         |            | - Validated 100% self-contained architecture check and 38/38 unit tests.   |
| v4.6    | 2026-10-05 | AI Agent Constitution & Repository Governance Deployment:                   |
|         |            | - Authored AGENTS.md at repository root establishing non-negotiable agent   |
|         |            |   operational policies and domain constraints.                             |
|         |            | - Codified Zero Modifications to Microsoft Word (.docx) documents policy    |
|         |            |   (no edits unless user explicitly states otherwise in session).            |
|         |            | - Mandated git commit after each individual task with appropriate message.  |
|         |            | - Mandated continuous updates to version control/provenance documents.      |
|         |            | - Mandated synchronization of all related CSV tables and Excel workbooks.   |
|         |            | - Reinforced throughput volatility targets and 4 canonical models.          |
|         |            | - Codified strict aviation terminology filter: Nominal On-Time Baseline,    |
|         |            |   Routine Daily Operations, Irregular Operations (IROPS); banned lab speak. |
|         |            | - Updated README.md referencing AGENTS.md and agent governance directives.  |
| v4.7    | 2026-10-05 | Candidate Model Suite Streamlining & Plain-Language Qualitative Calibration:|
|         |            | - Streamlined model nomenclature to 3 candidate models + baseline control:  |
|         |            |   Baseline Control (Daily Persistence), Model 1 (Deterministic Schedule),  |
|         |            |   Model 2 (Supervised Machine Learning), Model 3 (Dynamic Two-Stage Hybrid).|
|         |            | - Excised all internal code variable artifacts (M0, M1*, M3, M5) from       |
|         |            |   manuscripts, SSOTs, READMEs, and conformed CSV/Excel tables.              |
|         |            | - Grounded theoretical mechanics in intuitive operational frameworks:       |
|         |            |   "The Checkpoint Tipping Point" (Kingman's Law), "The Staffing Safety      |
|         |            |   Cushion" (Dynamic Lane Buffers), "The Airport Operator's Playbook"       |
|         |            |   (Regime-Switched Gated Engine), and "The Empty Checkpoint Fallacy".       |
|         |            | - Excised orphaned draft fragments and dead links in Chapter 5 and glossary.|
|         |            | - Synchronized all 16 manuscript tables across CSV and companion Excel      |
| v4.8    | 2026-10-05 | Excision of 'Physics' & Theoretical Jargon for Qualitative Audience:       |
|         |            | - Replaced "queuing physics" with "queuing principles", "queuing theory",  |
|         |            |   or "queuing dynamics" across Chapters I, II, III, IV, V, Glossary, and   |
|         |            |   SSOT to eliminate the pseudo-physics trap for qualitative ERAU readers.  |
|         |            | - Replaced "physical baseline" and "physical rules" with "operational       |
|         |            |   baseline" and "deterministic operational rules".                         |
|         |            | - Replaced "cyber-physical" with "two-stage hybrid" or "sequential hybrid".|
|         |            | - Replaced "quiescent" / "quiescence" with "minimal" / "curfew period".     |
|         |            | - Replaced "econometric deconvolution" with "mathematical separation".      |
|         |            | - Re-synchronized all 16 manuscript tables across CSV and Excel workbooks   |
|         |            |   (02, 03, 04, 05) via sync_manuscript_tables.py.                          |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); clean tests.   |
+---------+------------+----------------------------------------------------------------------------+

----------------------------------------------------------------------------------------------------
2. DATA SOURCE PROVENANCE & WAREHOUSE CENSUS
----------------------------------------------------------------------------------------------------
The multi-source analytical warehouse synthesizes four primary federal aviation data feeds over the 
continuous 7-year baseline from January 1, 2019 to December 31, 2025:

A. TSA FOIA Security Checkpoint Logs (Transportation Security Administration):
   - Raw Ingested Grain: Checkpoint-lane-hourly throughput (19,500,286 rows).
   - Post-ETL Cleaned Grain: 6,434,732 conformed lane-hour records across the Top 25 airfields.
   - Coverage: 25 commercial airfields, 955 physical screening lanes, 2,703,694,229 screened passengers.
   - Core Measure: Passenger screening count per lane-hour and airport consolidated hourly volume.

B. BTS On-Time Performance (Bureau of Transportation Statistics, Form 234):
   - Raw Ingested Grain: Individual domestic flight departure movements (45,777,091 rows).
   - Post-ETL Cleaned Grain: 13,153,654 domestic mainline departures across the Top 25 airfields.
   - Coverage: 17 reporting commercial air carriers, 294 destination spoke airports.
   - Core Measures: Departure delay minutes (signed and non-negative), DepDel15 indicator, taxi-out 
     duration, tactical cancellations, and delay cause decompositions (Carrier, Weather, NAS, Security, Late Aircraft).

C. BTS Form 41 Schedule T-100 Domestic Segment Capacity (BTS Office of Airline Information):
   - Raw Ingested Grain: Carrier-route-equipment-month segment records (1,945,451 rows).
   - Post-ETL Cleaned Grain: 422,096 conformed carrier-segment-month observations.
   - Coverage: 2,094,610,715 departing mainline seats; 1,701,068,172 transported revenue passengers.
   - Core Measures: Aircraft seating capacity gauge (mean = 171.1 seats) and route load factors (mean = 84.73%).

D. BTS DB1B / DB1C Origin-Destination Ticket Coupon Survey (10% Random Ticket Sample):
   - Raw Ingested Grain: 12,910,384 itinerary coupon records.
   - Post-ETL Cleaned Grain: 22,051,557 coupon records representing 62,158,071 ticketed passenger journeys.
   - Coverage: Closed 25-airport origin-destination network pairs.
   - Core Measures: Airside connecting transfer ratio (mean = 51.39%) and true local originating share (48.61%).

----------------------------------------------------------------------------------------------------
3. DATA HYGIENE, ANOMALY REMEDIATION & MISSINGNESS RESOLUTION
----------------------------------------------------------------------------------------------------
To guarantee machine learning and econometric validity, four critical remediation rules were enforced:

1. Spatial Key Fingerprinting & Phantom Airport Isolation:
   - Upstream raw TSA logs contained 35,809 records with null, corrupted, or non-IATA airport strings.
   - Automated checkpoint fingerprinting algorithm matched text patterns (dim_checkpoint) to recover 7,489 rows.
   - The remaining 22,190 unresolvable records were mapped to a dedicated null surrogate key (airportId = 0, 
     flagged with airportMissing = 1).
   - Validation Impact: Prevented the creation of an artificial, composite 9.71-million passenger phantom 
     airport that would have distorted national econometric baselines.

2. Structural Zeros versus Sensor Dropouts:
   - Exactly 64,743 records (1.01% of cleaned post-ETL observations) reported zero passenger throughput.
   - Cross-referencing flight schedules confirmed that 98.6% of zero values occurred during overnight 
     non-operational hours (00:00 to 03:59 local time).
   - Preserved as true physical terminal lane closures rather than naively imputed with moving averages.

3. Flight Cancellations and Advance vs. Tactical Demarcation:
   - 99.4% of unassigned aircraft tail numbers occurred on cancelled flights.
   - Advance cancellations (> 24 hours pre-departure) were purged from departing seat capacity curves.
   - Tactical cancellations (< 2 hours pre-departure) were retained in passenger demand curves, 
     reflecting that affected travelers had already crossed landside security checkpoints prior to the 
     carrier issuing the cancellation.

4. Referential Integrity Certification:
   - 100.0% of foreign keys across all conformed fact tables resolve directly to primary keys in 
     dim_airport, dim_date, dim_time_block, dim_airline, dim_aircraft, and dim_checkpoint.
   - Zero orphaned records exist in the conformed warehouse.

----------------------------------------------------------------------------------------------------
4. COMPLETE REPOSITORY FILE MANIFEST & SITEMAP
----------------------------------------------------------------------------------------------------
The foundational analysis suite (housed in `results/foundational_analysis/`) is structured into four primary hubs:

01_Executive_Summary/
   - 01_Executive_Top25_Airport_Coupled_Master_Census.csv: 25-airport master census combining OTP and TSA.
   - 02_Executive_Cross_Dataset_Statistical_Relationships_and_Volatility.csv: 14 econometric correlations (r, R^2, t, p).
   - 03_Executive_Coupled_Seasonality_and_Operational_Regimes.csv: 28 rows synthesizing regimes, DOW, months, and diurnal blocks.
   - 04_Executive_Airport_Archetypes_Cross_Dataset_Synthesis.csv: 4-cluster PCA/Hierarchical clustering profiles.
   - README.md: Executive summary user guide and methodological takeaways.

02_Data_Sources/
   - 01_TSA_Checkpoint_Throughput/: 16 CSVs capturing lane, hourly, and daily throughput dispersion.
   - 02_BTS_On_Time_Performance/: Flight-level and daily operational time-series tables, delay matrices, and models.
   - 03_BTS_T100_Capacity_and_Gauge/: Aircraft equipment gauge, seating capacity, and load factor profiles.
   - 04_BTS_DB1B_Ticket_Survey/: Ticket coupon samples, connecting transfer ratios, and local demand shares.

03_Analysis_Results/
   - 01_Spatial_Top25_Census/: Top 25 Candidate Airfield Census & Macro Benchmarks (includes Section 1A Foundation Census & Section 1B Post-ETL Master Statistics).
   - 02_Attribute_Volatility_Census/: Parametric and non-parametric dispersion across flight and daily grains.
   - 03_Coupled_Cross_Dataset_Dynamics/: Joint OTP-TSA coupling, correlation matrices, and volatility transmission.
   - 04_Seasonality_and_Regimes/: 4 operational regimes, DOW cycles, monthly seasonal curves, and diurnal banks.
   - 05_Extreme_Events_and_Anomalies/: Top +2 Sigma super peaks (Thanksgiving Sunday), -2 Sigma troughs, and shocks.
   - 06_Nine_Airport_Filtered_Cohort/: 4-Tier filtering pipeline, factorial grid, Table C summary, Table D census, 4Tier-Filtering-Stats.xlsx, and top9-desc-stats.xlsx.

04_Reports_and_Walkthroughs/
   - Thesis_Results_and_Discussion_Comprehensive_Draft.md: Full draft of Chapter IV Results and Empirical Findings.
   - Approach1_Results_and_Analysis_Summary.txt: Detailed econometric walkthrough of Approach 1 modeling results.
   - Section_1_Intro_and_Post_ETL_Descriptive_Statistics.txt: Comprehensive Section 1 outline and descriptive statistics.
   - Section_2_Spatial_and_Temporal_Filtering_Pipeline.txt: Section 2 filtering walkthrough and criteria.
   - Section_3_Filtered_Dataset_Descriptive_Statistics.txt: Section 3 descriptive statistics walkthrough.
   - Section_4_Hypothesis_Aligned_Representative_Model_Selection.txt: Section 4 model taxonomy and selection analysis.
   - Section_5_Empirical_Model_Execution_and_Output_Descriptive_Statistics.txt: Section 5 empirical execution report.
   - Findings_Outline_Master_Overview.txt: Master overview of all empirical findings chapters.
   - Methodology_with_4Tier_Filtering.md: Methodology documentation including 4-tier filtering criteria.
   - Data_Quality_and_Referential_Integrity_Walkthrough.md: Data engineering audit and validation report.
   - Project_Findings_Master_Walkthrough.md: Master research project findings and technical walkthrough.
====================================================================================================
