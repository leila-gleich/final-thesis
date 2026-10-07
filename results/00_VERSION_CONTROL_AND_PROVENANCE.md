# RESEARCH DATA PROVENANCE, INTEGRITY & VERSION CONTROL SPECIFICATION
====================================================================================================
PROJECT: Empirical Modeling of Airport Security Screening Demand and Flight Performance Coupling
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
LOCATION: results/00_VERSION_CONTROL_AND_PROVENANCE.md
RELEASE VERSION: v4.36 (Author-Editor Interlock Protocol, File Ownership SOP, and Explicit Git Governance Deployment)
DATE: October 6, 2026
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
| v4.9    | 2026-10-06 | Table-Free Text Manuscripts & Master Full Thesis in manuscripts-only/:      |
|         |            | - Created thesis_docs/manuscripts/manuscripts-only/ containing individual  |
|         |            |   chapter markdown files (chp1-intro.md through chp5-discussion.md).       |
|         |            | - Replaced all embedded markdown tables with APA callout blocks: Table      |
|         |            |   number, italicized table title, and prominent large-font heading         |
|         |            |   (## Table X.Y: Title) for clear text-only review and print layout.       |
|         |            | - Compiled full-thesis.md containing sequential text across all 5 chapters. |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); 100% sync.     |
| v4.10   | 2026-10-06 | Chapter III Methodology Architecture Harmonization with Committee Draft:    |
|         |            | - Restructured Chapter III manuscripts (chp3-methodology.md in both main   |
|         |            |   and manuscripts-only/ folders, plus full-thesis.md) into 5 main headers: |
|         |            |   Research Approach, Sample, Sources of Data, Validity, Treatment of Data. |
|         |            | - Integrated structural descriptions, figure callouts (Figures 1–5), macro  |
|         |            |   archetypes, micro checkpoint isolation, and ETL lists from committee     |
|         |            |   draft while preserving queuing theory rigor, volatility targets, 3-model |
|         |            |   suite, and asymmetric trade-offs.                                        |
|         |            | - Updated Section 2 outline in thesis_docs/ssot/Chapter_3_SSOT.md.         |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.11   | 2026-10-06 | Chapter IV Introduction and Architecture Roadmap Standalone Deployment:     |
|         |            | - Authored thesis_docs/manuscripts/chp4-intro.md establishing the standalone |
|         |            |   introductory section for Chapter IV: Results.                             |
|         |            | - Provided dual formats: a structured 4-section roadmap (matching Chapter   |
|         |            |   III style) and a continuous-flow academic prose paragraph.                |
|         |            | - Synthesized core empirical findings: throughput volatility targeting,     |
|         |            |   asymmetric performance trade-offs across 3 candidate models, and the     |
|         |            |   values versus volatility paradigm (H1, H2).                               |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.12   | 2026-10-06 | Consolidated Master Multi-Tab Excel Workbook (thesis_tables.xlsx):          |
|         |            | - Authored src/analysis/generate_thesis_tables_excel.py compiling all 16   |
|         |            |   empirical manuscript tables (Table 4.1 to Table 5.4) plus the Dual-Track  |
|         |            |   Operational Model Selection Policy into a unified multi-tab workbook.     |
|         |            | - Configured worksheet tabs using standardized short names (table_4_1       |
|         |            |   through table_5_4, dual_track_policy).                                    |
|         |            | - Established 'Contents' interactive master navigation sheet with two-way   |
|         |            |   clickable hyperlinks (Table ID/Tab -> Sheet A1 and Back -> Contents A1).  |
|         |            | - Formatted all data sheets as native Excel Table objects (ListObject) with |
|         |            |   APA 7th headers, cell notes, auto-filters, and auto-adjusted widths.      |
|         |            | - Integrated workbook compilation into src/analysis/sync_manuscript_tables.py|
|         |            |   and deployed thesis_tables.xlsx to results/ and results/manuscript_tables/.|
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.13   | 2026-10-06 | Appendix Table Specification: Standard Literature Equations & Formulas:    |
|         |            | - Authored appendix_standard_literature_equations.csv in both              |
|         |            |   results/manuscript_tables/ and results/tables/ cataloging 20 peer-        |
|         |            |   reviewed mathematical equations and statistical metrics.                 |
|         |            | - Spans Kingman queuing approximations, ACRP Report 40 arrival curves,     |
|         |            |   BTS Form 41 / DB1B accounting identities, statistical dispersion targets,|
|         |            |   time-series error metrics (RMSE, MAE, MASE), and econometric tests.       |
|         |            | - Authored thesis_docs/recommendations/PROPOSED_EDITS_ELIMINATE_ORIGINAL_   |
|         |            |   FORMULAS.md outlining location-by-location text replacements to eliminate|
|         |            |   the 2 original formulas (T(h) and CVI) in favor of standard equivalents. |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.14   | 2026-10-06 | Master thesis_tables.xlsx APA 7th Edition Reformatting & Zero Filters:     |
|         |            | - Reformatted master multi-tab workbook thesis_tables.xlsx across all       |
|         |            |   worksheets to strictly conform with APA Style (7th ed.) matching         |
|         |            |   results/sample-tables.docx and the reference template tab table-format.   |
|         |            | - Eliminated all Excel table objects (ListObjects) and auto-filter dropdown |
|         |            |   arrows across all 19 worksheets.                                          |
|         |            | - Removed all colored fills and zebra shading, establishing clean white    |
|         |            |   backgrounds.                                                              |
|         |            | - Applied APA horizontal boundary rules: thin black rules above and below  |
|         |            |   header rows, thin black rule on terminal data rows, and zero internal     |
|         |            |   horizontal or vertical cell borders.                                      |
|         |            | - Preserved table-format reference template tab and maintained two-way     |
|         |            |   interactive navigation hyperlinks on Contents and all table sheets.       |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.15   | 2026-10-06 | Operational Metric Framework Defense Documentation Deployment:              |
|         |            | - Authored thesis_docs/manuscripts/operational-metric-framework.md          |
|         |            |   providing comprehensive statistical formulations, Kingman queuing        |
|         |            |   interpretations, and checkpoint floor operational translations for the    |
|         |            |   5 primary holdout evaluation metrics: R^2, RMSE, MAE, MASE, and Bias.    |
|         |            | - Embedded Table 4.10 certified 2025 holdout benchmarks across the 4 models.|
|         |            | - Synthesized committee defense talking points, addressing MAPE invalidity, |
|         |            |   diurnal persistence MASE scaling, and asymmetric trade-offs (H1).        |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.16   | 2026-10-06 | Academic Terminology Clarification and Replacement Guide Deployment:        |
|         |            | - Authored thesis_docs/notes/terminology_clarifications_and_replacements.md |
|         |            |   synthesizing terminology clarifications across 4 core areas:              |
|         |            |   1. Coupled Volatility Index -> Landside-Airside Volatility Interaction    |
|         |            |   2. Diurnal Dual Turbulence Peaks -> Bimodal Intraday Operational Peaks    |
|         |            |   3. 1-Step Error Innovation Feedback -> Real-Time Prior-Hour Error Correct |
|         |            |   4. Zero Feedback Latency -> Requires No Real-Time Checkpoint Data Feeds.  |
|         |            | - Formulated defense Q&A talking points for committee examination.          |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.17   | 2026-10-06 | Regime-Switched Gated Inference Engine Terminology Integration:             |
|         |            | - Updated thesis_docs/notes/terminology_clarifications_and_replacements.md |
|         |            |   incorporating Section 5 analysis and replacement recommendations for      |
|         |            |   "Regime-Switched Gated Inference Engine" -> "Dual-Track Operational       |
|         |            |   Decision Framework" / "Disruption-Adaptive Checkpoint Forecasting Playbook"|
|         |            | - Added summary cheat-sheet entry and defense Q&A talking point (Q4).       |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.18   | 2026-10-06 | Manuscript Appendix Deployment: Diebold-Mariano & Equation Registry:        |
|         |            | - Authored thesis_docs/manuscripts/appendix.md providing formal econometric |
|         |            |   derivations for the Diebold-Mariano (DM) test of forecast accuracy.       |
|         |            | - Articulated why time-series autocorrelation violates i.i.d. assumptions   |
|         |            |   and invalidates standard paired t-test p-values (spurious significance).  |
|         |            | - Formulated the HAC long-run variance estimator (Newey-West spectral       |
|         |            |   density at frequency zero) and asymptotic normality proofs.               |
|         |            | - Tabulated pairwise DM statistics across the 2025 holdout benchmark:       |
|         |            |   Model 2 vs Model 1 (DM = 42.15) and Model 3 vs Model 1 (DM = 48.72).      |
|         |            | - Cataloged all 20 peer-reviewed operational and statistical equations       |
|         |            |   in Table B.1 (Kingman, ACRP 40, DB1B, MASE, DM, Chow, CUSUM, lane safety).|
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.19   | 2026-10-06 | Figures Screenshot-to-CSV Structured Data Suite Deployment:                |
|         |            | - Generated 30 high-fidelity CSV files directly capturing tabular and       |
|         |            |   structural data from all 30 PNG screenshots in figures/ subdirectories:  |
|         |            |   * 01_Sample_and_Airport_Selection (7 CSVs): airport clusters matrix,      |
|         |            |     experimental power of 9 airports, post-pandemic justification, data     |
|         |            |     sample profile census, clustering & connecting paradox, top 25 network  |
|         |            |     inclusion guide, and airport selection strategy document.               |
|         |            |   * 02_Data_Pipelines_and_Threats (8 CSVs): master funnel progression,      |
|         |            |     unified data integrity & threat remediation matrix, OTP volatility      |
|         |            |     metrics, TSA schema DDL, checkpoint name variation audit, lineage       |
|         |            |     imputation metadata, OTP vs TSA volume coupling, and T-100 schema DDL. |
|         |            |   * 03_Modeling_and_Evaluation (8 CSVs): evaluation metric definitions,     |
|         |            |     exploratory metric criteria research benchmark, probabilistic and       |
|         |            |     information selection metrics, models and tests comparison, control vs  |
|         |            |     noisy test process, model walkthrough architecture, passenger           |
|         |            |     stochastic arrival parameters, and physical transfer lead-lag timeline. |
|         |            |   * 04_Appendix_and_Reference (7 CSVs): BTS DB1B table hierarchy, top-9     |
|         |            |     diagrams/screenshots layout catalog.                                    |
|         |            | - Validated all 30 CSV files with automated pandas integrity checks.         |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.20   | 2026-10-06 | Academic Terminology Notes Enhancement: Document Description & Leakage:     |
|         |            | - Authored dedicated Document Description & Operational Scope in           |
|         |            |   thesis_docs/notes/terminology_clarifications_and_replacements.md.         |
|         |            | - Formally delineated Temporal Lookahead Leakage (time-axis partitioning    |
|         |            |   and 7-day operational purge buffers) from Feature Lookahead Leakage       |
|         |            |   (covariate-space realized delay ingestion and cancellation causality)    |
|         |            |   grounded in Strict Information Causality and Granger/Sims principles.     |
|         |            | - Updated Executive Summary cheat sheet and added Question 6 to the        |
|         |            |   oral defense Q&A strategy.                                                |
|         |            | - Generated synchronized companion CSV files in thesis_docs/notes/ and      |
|         |            |   results/tables/ (terminology_replacements.csv).                           |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.21   | 2026-10-06 | Comprehensive Academic Terminology Harmonization & Defense Guide Expansion: |
|         |            | - Generated conformed 40-item companion CSV datasets in                     |
|         |            |   thesis_docs/notes/terminology_replacements.csv and                        |
|         |            |   results/tables/terminology_replacements.csv mapping draft jargon and     |
|         |            |   physics metaphors across 7 functional categories to authentic commercial  |
|         |            |   aviation operations and transportation econometrics terminology.          |
|         |            | - Expanded thesis_docs/notes/terminology_clarifications_and_replacements.md |
|         |            |   from 20 to 34 comprehensive narrative sections, adding in-depth           |
|         |            |   qualitative and operational analyses for: Tweedie count regression        |
|         |            |   (p = 1.3), carrier arrival consistency, overnight curfew periods vs.      |
|         |            |   quiescence, ambient operational churn vs. noise, irregular operations     |
|         |            |   (IROPS) vs. acute shocks, peak-hour congestion asymptotics, post-COVID    |
|         |            |   sample demarcation, the Empty Checkpoint Fallacy, unidentified airport    |
|         |            |   records (null key quarantining), multi-dimensional performance pillars    |
|         |            |   (Robustness, Resilience, Generalizability), disruption error multipliers  |
|         |            |   (R_MASE), transfer error penalties (RTR), and queuing burstiness vs.      |
|         |            |   fluid mechanics.                                                          |
|         |            | - Expanded Oral Defense Q&A Strategy from 7 to 12 comprehensive questions   |
|         |            |   and candidate defense scripts, equipping the candidate to defend queuing  |
|         |            |   theory, Tweedie regression, the Empty Checkpoint Fallacy, asymmetric      |
|         |            |   trade-offs, and Kingman lane staffing buffers before Embry-Riddle         |
|         |            |   qualitative aviation management faculty.                                  |
|         |            | - Enhanced src/analysis/sync_manuscript_tables.py with flexible manuscript   |
|         |            |   path resolution supporting both root and manuscripts-only/ layouts.       |
|         |            | - Validated 100% passing test suite across all 38 unit tests.               |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.22   | 2026-10-06 | Full Manuscript Appendix Overhaul & Committee Review Alignment:             |
|         |            | - Synthesized Appendix v1.docx and figures/04_Appendix_and_Reference into a|
|         |            |   comprehensive, publication-grade manuscript appendix deployed to both     |
|         |            |   thesis_docs/manuscripts/appendix.md and manuscripts-only/ layout.        |
|         |            | - Expanded appendix structure into eight dedicated appendices (A through H):|
|         |            |   * Appendix A: Statistical Foundation & Diebold-Mariano Test Derivation.   |
|         |            |   * Appendix B: Peer-Reviewed Equation Registry (Table B.1, EQ-01 to 20).   |
|         |            |   * Appendix C: Methodological Foundations, 4-Tier Filtering Pipeline,      |
|         |            |     Table C.1 (14-point assumptions), Figure C.1, Table C.2 (progression),  |
|         |            |     Figure C.2 (4-cluster matrix), Table C.3 (4 econometric tests for       |
|         |            |     carrier isolation), Table C.4 (census), Table C.5 (local DOW profiles). |
|         |            |   * Appendix D: Aviation Data Engineering, Warehouse Census (Table D.1,     |
|         |            |     Figure D.1), Feature Store Breakdown (Table D.2, Figure D.3), 9-Airport|
|         |            |     Parquet Profile (Table D.3, Figure D.2), DB1B Ticket Hierarchy &        |
|         |            |     Connecting Deflation (Table D.4, Figure D.4), Data Hygiene (surrogate   |
|         |            |     null key, Tweedie Poisson p=1.3 zeros, tactical cancellations), and     |
|         |            |     empirical show-up convolution with 24 dual-paradigm attributes.         |
|         |            |   * Appendix E: Seasonal Regimes, Operational Taxonomies (Three-Tier),      |
|         |            |     Table E.1 (Annual Regimes & CVI), Table E.2 (DOW Archetypes), Bimodal   |
|         |            |     Intraday Peaks (Morning Surge vs. Evening Delay Cascade), Turbulence    |
|         |            |     Shock Index T_dow(h), and 84-Cell Operational Matrix.                   |
|         |            |   * Appendix F: Holdout Benchmarks & Resilience Mechanics: Table F.1        |
|         |            |     (Multi-Pillar Matrix), Table F.2 (Resilience & Empty Checkpoint Fallacy |
|         |            |     under live feedback), Table F.3 (Generalizability & Spatial Penalty),   |
|         |            |     and Table F.4 (Values vs. Volatility Paradigm proof for H2).             |
|         |            |   * Appendix G: Operational Decision Playbook: Table G.1 (Dual-Track        |
|         |            |     Gated Policy), Kingman Queuing Law, and Volatility-Buffered Dynamic     |
|         |            |     Lane Dimensioning Rule (EQ-20).                                         |
|         |            |   * Appendix H: Research Limitations (4 operational boundary constraints),  |
|         |            |     Table H.1 (OneDrive Backup Manifest), Figure H.1 (Backup Tree), and     |
|         |            |     Figure H.2 (Diagrams & Screenshot Layout Catalog).                      |
|         |            | - Authored automated compiler script src/analysis/generate_appendix_md.py.  |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); synchronized.  |
| v4.23   | 2026-10-06 | Implementation Plans Archive Relocation & Active Recommendations Audit:     |
|         |            | - Relocated 17 completed recommendation files from implementation_plans/   |
|         |            |   into thesis_docs/recommendations/archive/completed_implementation_plans/ |
|         |            |   including REC-01 to REC-14, recs-to-implement.md, Updated_Thesis_Project_|
|         |            |   and_Structure_Recommendation.md, and Recommendations_Results_and_        |
|         |            |   Discussion.md.                                                           |
|         |            | - Updated all cross-references in recommendations/README.md, archive/      |
|         |            |   README.md, recs-to-implement.md, and thesis_docs/README.md.              |
|         |            | - Preserved active/pending recommendation files: OTP_FACTOR_WEIGHTING_AND_  |
|         |            |   TSA_VOLATILITY_RECOMMENDATIONS_AND_IMPLEMENTATION_PLAN.md (live JOC       |
|         |            |   operational telemetry) and PROPOSED_EDITS_ELIMINATE_ORIGINAL_FORMULAS.md |
|         |            |   (elimination of author-invented T(h) and CVI in favor of standard methods)|
|         |            | - Authored thesis_docs/recommendations/chapter_updates/chp5-recs.md         |
|         |            |   drafting Chapter V Section 5.6 operational telemetry recommendation text. |
|         |            | - Preserved zero edits to Microsoft Word documents (.docx); 38/38 tests ok.|
| v4.24   | 2026-10-06 | Word Review Manuscripts Direct Markdown Drafting & Prior Version Archiving:|
|         |            | - Archived existing markdown manuscript drafts into                        |
|         |            |   thesis_docs/manuscripts/archive/ with explicit older version identifiers  |
|         |            |   (chp1-intro_v2_archive.md through chp5-discussion_v2_archive.md and      |
|         |            |   chp4-intro_v2_archive.md).                                               |
|         |            | - Drafted updated markdown manuscripts for Chapters 1 through 5            |
|         |            |   (chp1-intro.md, chp2-litreview.md, chp3-methodology.md, chp4-results.md,  |
|         |            |   chp5-discussion.md) directly reflecting committee review Word documents  |
|         |            |   (ChpI v2.docx through ChpV v1.docx) with exact textual fidelity,         |
|         |            |   nothing added, clean APA 7 headings, and fully parsed LaTeX equations.   |
|         |            | - Synchronized table-free layout in manuscripts-only/ (including master    |
|         |            |   full-thesis.md).                                                         |
|         |            | - Enhanced get_manuscript_path in src/analysis/sync_manuscript_tables.py   |
|         |            |   with archive fallback for table extraction, keeping all 16 conformed CSVs|
|         |            |   and multi-tab companion Excel workbooks synchronized (38/38 tests pass).  |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx).                                                       |
| v4.25   | 2026-10-06 | Multi-Tab APA 7th Edition Excel Workbooks for All Figures Subfolders:       |
|         |            | - Authored src/analysis/generate_figures_tables_excel.py combining all 30  |
|         |            |   CSV files across the 4 figures/ subfolders into dedicated multi-tab      |
|         |            |   Excel workbooks formatted strictly to APA Style (7th ed.):               |
|         |            |   * figures/01_Sample_and_Airport_Selection/01_Sample_and_Airport_Selection|
|         |            |     .xlsx (7 tabs: Table 1.1 to Table 1.7 + interactive Contents).         |
|         |            |   * figures/02_Data_Pipelines_and_Threats/02_Data_Pipelines_and_Threats    |
|         |            |     .xlsx (8 tabs: Table 2.1 to Table 2.8 + interactive Contents).         |
|         |            |   * figures/03_Modeling_and_Evaluation/03_Modeling_and_Evaluation          |
|         |            |     .xlsx (8 tabs: Table 3.1 to Table 3.8 + interactive Contents).         |
|         |            |   * figures/04_Appendix_and_Reference/04_Appendix_and_Reference            |
|         |            |     .xlsx (7 tabs: Table 4.1 to Table 4.7 + interactive Contents).         |
|         |            | - Formatted all worksheets according to strict APA 7th rules: bold table ID |
|         |            |   on line 1, italicized title on line 2, thin horizontal boundary rules    |
|         |            |   (header top/bottom and terminal data row), zero internal borders, zero   |
|         |            |   vertical rules, zero background fills/shading, and zero auto-filters.    |
|         |            | - Added interactive navigation with clickable hyperlinks between Contents  |
|         |            |   and every table tab (Return to Table of Contents in Cell A1).             |
|         |            | - Mirrored all 4 workbooks to figures/ root for convenient accessibility.  |
|         |            | - Authored comprehensive unit tests in tests/test_figure_workbooks.py      |
|         |            |   validating structural integrity, hyperlinks, and APA 7 rules (39/39 ok). |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx).                                                       |
| v4.26   | 2026-10-06 | Manuscript Appendix Overhaul, Table Rendering Fixes & Cross-References:    |
|         |            | - Resolved table rendering failures across all 15 tables in appendix.md    |
|         |            |   and manuscripts-only/appendix.md by eliminating leading 'r|' syntax      |
|         |            |   artifacts and formatting with clean APA 7 headers and alignment.         |
|         |            | - Fully synthesized all narrative details, parameters, and econometric     |
|         |            |   formulations from author committee review draft Appendix v1.docx (read-  |
|         |            |   only): 15-step Transform / 8-step Extract protocols, spatial entity      |
|         |            |   resolution (35,809 records mapped to null key airportId=0,               |
|         |            |   airportMissing=1), structural zero preservation (450,973 Tweedie Poisson |
|         |            |   records in 00:00–03:59), advance vs. tactical cancellations (99.4%       |
|         |            |   unassigned tail numbers), purposive filtering sample validation, LGA/JFK |
|         |            |   and PHL/SLC selection contrasts, 84-cell interaction grid sample depth,  |
|         |            |   lead-lag asynchrony mechanics, Empty Checkpoint Fallacy under feedback,  |
|         |            |   and complete Values vs. Volatility numbers.                              |
|         |            | - Embedded explicit 'Note on Thesis Cross-References' in all eight         |
|         |            |   appendices (Appendices A through H) citing specific thesis chapters and   |
|         |            |   sections referencing each appendix.                                      |
|         |            | - Reordered appendices into logical A through H sequence.                  |
|         |            | - Rewrote src/analysis/generate_appendix_md.py using token substitution    |
|         |            |   and automated dual deployment.                                           |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); synchronized tables and workbooks (39/39 tests ok).   |
| v4.27   | 2026-10-06 | Master Table & Figure Recommendations Guide Deployment in figures/:        |
|         |            | - Authored comprehensive master visual and tabular guide in                |
|         |            |   figures/TABLE_AND_FIGURE_RECOMMENDATIONS.md mapping all recommended      |
|         |            |   tables and figures across Chapters 1 through 5.                          |
|         |            | - Provided theoretical rationales (queuing theory, Kingman's law, H1, H2),  |
|         |            |   exact narrative insertion points, and source asset paths in figures/,    |
|         |            |   results/manuscript_tables/, and companion Excel workbooks.               |
|         |            | - Provided actionable copy-paste prompt options for next-session execution |
|         |            |   (Options A through D).                                                   |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); synchronized tables and workbooks (39/39 tests ok).   |
| v4.28   | 2026-10-06 | Chapter II Literature Review Synthesis Recommendations (litreview-rec.md):|
|         |            | - Authored comprehensive synthesis recommendation report litreview-rec.md  |
|         |            |   (deployed to root and thesis_docs/recommendations/chapter_updates/).      |
|         |            | - Diagnosed word count and depth divergence between Chp2 v1.docx (3,894 w) |
|         |            |   and ChpII v2.docx / chp2-litreview.md (1,764 w).                         |
|         |            | - Formulated the 'V2 Backbone + V1 Empirical Depth' blueprint expanding    |
|         |            |   Chapter II to ~3,900–4,200 words while preserving V2's concise flow.     |
|         |            | - Completed forensic 100% census cataloging all 101 citations across both   |
|         |            |   drafts (91 in V1, 40 in V2) in the Master Harmonization Registry with     |
|         |            |   explicit section mapping and operational roles for all references.        |
|         |            | - Replaced telegraphic bullet points with continuous APA 7 academic prose.  |
|         |            | - Pruned off-topic baggage metaheuristics, fuzzy logic, and lab jargon.     |
|         |            | - Anchored the Allen-Cunneen queuing approximation (Ca^2) and econometrics |
|         |            |   'Values vs. Volatility' paradigm (H2) into the chapter narrative.         |
|         |            | - Formalized V1 Figures 2 & 3 into APA 7 Table 2.1 (Paradigm Taxonomy).     |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); synchronized tables and workbooks.                    |
| v4.29   | 2026-10-06 | Manuscript Appendix Expansion to 24 Dedicated Lettered Appendices (A-X):   |
|         |            | - Fully expanded the appendix architecture from 8 bundled appendices into  |
|         |            |   24 dedicated, lettered appendices (Appendix A through Appendix X),       |
|         |            |   establishing a 1:1 mapping with every individual topic and section from   |
|         |            |   the author committee review draft Appendix v1.docx.                      |
|         |            | - Programmatically extracted and integrated all 281 body paragraphs        |
|         |            |   directly from Appendix v1.docx (read-only) with 100% textual fidelity,   |
|         |            |   zero omissions, and converted OMML equations to KaTeX markup.            |
|         |            | - Embedded explicit 'Note on Thesis Cross-References' in all 24 appendices |
|         |            |   citing specific thesis chapters and sections referencing each appendix.  |
|         |            | - Reordered appendices into a coherent operational and academic sequence:  |
|         |            |   Delimitations (A) -> Limitations (B) -> Diebold-Mariano Derivation (C)   |
|         |            |   -> Equation Registry (D) -> Data Ingestion & Census (E) -> ETL Pipeline  |
|         |            |   (F) -> COVID Demarcation (G) -> 4-Tier Filtering (H) -> Top 25 Census    |
|         |            |   (I) -> Econometric Validation (J) -> Airport Contrasts (K) ->            |
|         |            |   Seasonality & DOW Dynamics (L) -> Diurnal Turbulence & Collinearity (M)  |
|         |            |   -> Construct Validity Targets (N) -> Evaluation Metrics (O) -> Feature   |
|         |            |   Engineering (P) -> Candidate Models (Q) -> Holdout Benchmarks (R) ->     |
|         |            |   Resilience Mechanics (S) -> Lead-Lag Asynchrony (T) -> Values vs.        |
|         |            |   Volatility (U) -> Operational Playbook (V) -> Dynamic Lane Staffing (W)  |
|         |            |   -> Archival Storage & Screenshot Catalog (X).                            |
|         |            | - Upgraded src/analysis/generate_appendix_md.py using direct docx paragraph|
|         |            |   extraction and token replacement, eliminating f-string syntax issues.    |
|         |            | - Formatted all 15 APA 7th edition tables and 2 figures cleanly.           |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); synchronized tables and workbooks (39/39 tests ok).   |
| v4.30   | 2026-10-06 | Two-Pillar Manuscript Exhibits & Results Architecture Reorganization:       |
|         |            | - Implemented clean two-pillar exhibit architecture separating Pre-Empirical|
|         |            |   Research Design from Empirical Results findings.                         |
|         |            | - Established thesis_docs/exhibits/ with chapter-dedicated subfolders for   |
|         |            |   Chapters I–III (ch01_intro/, ch02_lit_review/, ch03_methodology/)        |
|         |            |   housing conceptual frameworks, queuing curves, process diagrams, data    |
|         |            |   schemas, and companion multi-tab Excel workbooks.                        |
|         |            | - Established results/figures/ housing the empirical publication-ready      |
|         |            |   volatility figures (Figure 4.2 annual clusters, Figure 4.3 DOW dynamics, |
|         |            |   Figure 4.4 diurnal curves, Figure 4.5 lead-lag convolution, and sample   |
|         |            |   sufficiency distribution).                                               |
|         |            | - Updated src/utils/paths.py declaring EXHIBITS_DIR and RESULTS_FIGURES_DIR.|
|         |            | - Updated src/analysis/generate_figures_tables_excel.py and                 |
|         |            |   src/analysis/generate_thesis_tables_excel.py for exhibits synchronization.|
|         |            | - Pruned legacy pre-volatility PNG duplicates in thesis_docs/manuscripts/   |
|         |            |   figures/.                                                                |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx).                                                       |
|         |            | - Preserved strict user constraint: 100% zero edits to any appendix files.  |
|         |            | - Synchronized all 16 manuscript tables and Excel workbooks (39/39 tests ok)|
| v4.31   | 2026-10-06 | Chapter II Literature Review Synthesis, Word Draft & LaTeX Reconciliation:  |
|         |            | - Generated thesis_docs/manuscripts/ChpII v3.docx synthesizing content from |
|         |            |   author drafts Chp2 v1.docx (3,894 w) and ChpII v2.docx (1,764 w) into an  |
|         |            |   authoritative, publication-grade 4,060-word manuscript.                   |
|         |            | - Incorporated 100% census of all 101 peer-reviewed literature citations     |
|         |            |   across both drafts with zero omissions, verified via programmatic audit.  |
|         |            | - Matched exact Word formatting of ChpII v2.docx: Times New Roman 12 pt,   |
|         |            |   double spacing (2.0), 1.0-inch margins, 0.5-inch paragraph indents, flush-|
|         |            |   left bold headings, APA 7 Table 2.1, and native OMML math equation.       |
|         |            | - Reconciled all LaTeX parsing errors in chp2-litreview.md and              |
|         |            |   manuscripts-only/chp2-litreview.md (clean KaTeX syntax and display math). |
|         |            | - Explicit user authorization granted for ChpII v3.docx generation;        |
|         |            |   preserved ChpII v2.docx and all existing .docx files untouched.           |
|         |            | - Synchronized all 16 manuscript tables and Excel workbooks (39/39 tests ok)|
| v4.32   | 2026-10-06 | Sequential Chapter Citation Reordering of 24 Manuscript Appendices:         |
|         |            | - Reordered all 24 dedicated lettered appendices (Appendix A through X)    |
|         |            |   in thesis_docs/manuscripts/appendix.md and manuscripts-only/appendix.md  |
|         |            |   to match the exact sequential chronological order of citation across the  |
|         |            |   thesis manuscript chapters: Chapter I -> Chapter II -> Chapter III       |
|         |            |   -> Chapter IV -> Chapter V.                                              |
|         |            | - Strictly guaranteed that no appendix referenced in later chapters        |
|         |            |   precedes an appendix referenced in earlier chapters (e.g. Chapter II     |
|         |            |   appendices C, D, E strictly precede all Chapter III appendices F-N).     |
|         |            | - Verified 100% forensic mapping of all 270 content paragraphs from        |
|         |            |   Appendix v1.docx with zero omissions and zero overlaps.                  |
|         |            | - Re-labeled all 17 APA 7th edition tables and 2 figures to match new      |
|         |            |   parent appendix lettering (Tables B.1, D.1, H.1, I.1, J.1-3, L.1,        |
|         |            |   O.1-3, Q.1, R.1, T.1, U.1, W.1, X.1; Figures H.1 and H.2).               |
|         |            | - Updated src/analysis/generate_appendix_md.py for automated generation;   |
|         |            |   synchronized all 16 tables and workbooks via sync_manuscript_tables.py.  |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); all 39 unit tests pass.                               |
| v4.33   | 2026-10-06 | Chapter II Literature Review Synthesizing Conclusion Paragraph:             |
|         |            | - Added brief, concise, non-repetitive synthesizing conclusion paragraph    |
|         |            |   to Chapter II Literature Review across thesis_docs/manuscripts/           |
|         |            |   ChpII v3.docx (4,218 words), chp2-litreview.md (4,309 words), and         |
|         |            |   manuscripts-only/chp2-litreview.md (3,961 words).                         |
|         |            | - Synthesizes all 5 core theoretical domains reviewed: queuing principles   |
|         |            |   and Kingman's law (Ca^2) vs static volume, single-paradigm limitations   |
|         |            |   (schedules, DES, unconstrained ML), two-stage hybrid predictive modeling, |
|         |            |   and the operational evaluation triad (Robustness, Resilience,             |
|         |            |   Generalizability) motivating Chapter III methodology.                     |
|         |            | - Preserved 100% census of all 101 peer-reviewed literature citations.      |
|         |            | - Synchronized all 16 manuscript tables and Excel workbooks (39/39 tests ok)|
| v4.34   | 2026-10-06 | Comprehensive Word and Markdown Acronyms & Abbreviations Suite Deployment:  |
|         |            | - Compiled comprehensive inventory of 132 technical, aviation, queuing,     |
|         |            |   machine learning, and statistical acronyms used across Chapters I–V.      |
|         |            | - Generated thesis_docs/manuscripts/List_of_Acronyms_and_Abbreviations.docx |
|         |            |   and companion Acronyms v1.docx strictly following APA 7th Edition style    |
|         |            |   (Times New Roman, 1.0-inch margins, Table 1 with 133 rows, tblHeader,     |
|         |            |   cantSplit, 3 horizontal boundary rules, zero vertical rules).             |
|         |            | - Generated Part II detailed categorized narrative entries across 7 domains:|
|         |            |   Agencies/Regulators, Infrastructure/Security, Datasets/Architecture,      |
|         |            |   Airports/Carriers, Queuing/Flow, Predictive ML Models, and Metrics/Stats. |
|         |            | - Generated synchronized markdown counterparts in thesis_docs/manuscripts/  |
|         |            |   acronyms.md and manuscripts-only/acronyms.md.                             |
|         |            | - Authored test suite tests/test_acronyms_generation.py (44/44 unit tests ok)|
|         |            | - Explicit user authorization granted for Word (.docx) creation.            |
| v4.35   | 2026-10-06 | Two-Pillar Model A Finalization & Method 1 Test Redirection:                |
|         |            | - Completed two-pillar asset reorganization (Model A) separating            |
|         |            |   pre-empirical research exhibits (thesis_docs/exhibits/) from empirical    |
|         |            |   findings (results/figures/ and results/tables/).                         |
|         |            | - Pruned legacy non-appendix folders (figures/01, 02, 03) and root          |
|         |            |   workbook duplicates from figures/ to resolve clutter.                     |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); untracked review drafts left untouched.                |
|         |            | - Preserved strict user constraint: 100% zero edits to any appendix files   |
|         |            |   (figures/04_Appendix_and_Reference/ and 04_Appendix_and_Reference.xlsx). |
|         |            | - Refactored src/analysis/generate_figures_tables_excel.py to generate     |
|         |            |   workbooks strictly in canonical targets (Method 1).                      |
| v4.36   | 2026-10-06 | Author-Editor Interlock Protocol & Git Version Control SOP Deployment:       |
|         |            | - Codified Policy 1.5 (Author-Editor Interlock Protocol) in AGENTS.md:      |
|         |            |   Strict 4-Gate safety sequence locking all author-edited files against     |
|         |            |   direct modification, requiring explicit author notification, relevance    |
|         |            |   rationale, non-destructive proposed preview drafts, and written approval.|
|         |            | - Codified Policy 1.6 (Explicit Git Staging & Blanket Add Ban) in AGENTS.md: |
|         |            |   Strict prohibition of blanket staging (git add -A / git add . / git add -u)|
|         |            |   with mandatory explicit file path enumeration and worktree audit.         |
|         |            | - Codified Policy 1.7 (Branching & Checkpoint Safety Architecture) in        |
|         |            |   AGENTS.md with automated pre-task safety tags and author branch protection.|
|         |            | - Authored comprehensive thesis_docs/notes/AUTHOR_SAFETY_AND_GIT_SOP.md     |
|         |            |   establishing formal SOP-01, flowchart, and author rollback cheat sheet.   |
|         |            | - Updated Section 7 checklist in AGENTS.md with mandatory protocol checks.  |
|         |            | - Preserved strict Policy 1.1 constraint: zero edits to Microsoft Word     |
|         |            |   documents (.docx); untracked review drafts left 100% untouched.           |
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
   - appendix.md: Econometric foundations, Diebold-Mariano test derivation, and peer-reviewed equation registry.
   - operational-metric-framework.md: Statistical formulations, queuing theory dynamics, and committee defense guide.
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
