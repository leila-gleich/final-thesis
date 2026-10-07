"""
src/analysis/generate_figures_tables_excel.py
---------------------------------------------
Generates 4 consolidated multi-tab Excel workbooks corresponding to the 4 subfolders
in the `figures/` directory, formatted strictly according to APA Style (7th ed.):

Subfolders:
1. figures/01_Sample_and_Airport_Selection -> 01_Sample_and_Airport_Selection.xlsx
2. figures/02_Data_Pipelines_and_Threats  -> 02_Data_Pipelines_and_Threats.xlsx
3. figures/03_Modeling_and_Evaluation     -> 03_Modeling_and_Evaluation.xlsx
4. figures/04_Appendix_and_Reference      -> 04_Appendix_and_Reference.xlsx

APA 7th Edition Formatting Rules:
- No table auto-filters / dropdown arrows.
- Thin black horizontal rules:
    * Header row: thin horizontal rule above and below.
    * Data rows: zero internal horizontal or vertical borders.
    * Last data row: thin horizontal rule below.
- Zero background fills or zebra striping (clean white/transparent).
- Typography: Calibri throughout. Table ID bold on line 1, Table Title italicized on line 2.
- Data alignment: stub column left-aligned, numeric columns right-aligned with commas/decimals,
  short codes centered, descriptions left-aligned with wrap text.
- Note block below table: begins with italicized "Note. ", wrap text.
- Interactive navigation: First tab is 'Contents' with active clickable hyperlinks to each tab,
  and every table tab contains a return link '⬅ Return to Table of Contents' in Cell A1.
"""

import csv
from pathlib import Path
import openpyxl
from openpyxl.styles import Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

BASE_DIR = Path(__file__).resolve().parent.parent.parent
FIGURES_DIR = BASE_DIR / "figures"
EXHIBITS_DIR = BASE_DIR / "thesis_docs" / "exhibits"

# Master catalog of subfolders, workbooks, and table metadata
SUBFOLDER_WORKBOOKS = [
    {
        "folder_name": "01_Sample_and_Airport_Selection",
        "wb_filename": "01_Sample_and_Airport_Selection.xlsx",
        "target_dir": EXHIBITS_DIR / "ch03_methodology" / "workbooks",
        "csv_dir": EXHIBITS_DIR / "ch03_methodology" / "tables",
        "title": "SAMPLE AND AIRPORT SELECTION FIGURE & DATA TABLES",
        "subtitle": "Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow | Gleich 700B",
        "tables": [
            {
                "table_id": "Table 1.1",
                "short_name": "airport_clusters",
                "csv_file": "airport_clusters.csv",
                "title": "Operational Clustering Archetypes and Carrier Checkpoint Exclusivity Matrix",
                "scope": "Master 4-cluster by 3-carrier experimental matrix mapping airports to carrier-exclusive checkpoints",
                "dimension": "Sample Stratification",
                "note": "Note. Master 4-cluster by 3-carrier experimental matrix mapping candidate commercial airfields across operational archetypes to dedicated carrier checkpoints (American Airlines, Delta Air Lines, and United Airlines)."
            },
            {
                "table_id": "Table 1.2",
                "short_name": "selection_strategy",
                "csv_file": "airport_selection_strategy_document.csv",
                "title": "Airport Purposive Selection Strategy and Methodological Rationale",
                "scope": "Four-tiered purposive filtering pipeline and causal identification justifications",
                "dimension": "Methodological Rationale",
                "note": "Note. Methodological rationale and causal identification criteria for the four-tiered purposive filtering pipeline, detailing candidate inclusions and exclusions across the commercial hub network."
            },
            {
                "table_id": "Table 1.3",
                "short_name": "connecting_paradox",
                "csv_file": "clustering_and_connecting_paradox.csv",
                "title": "Unsupervised Clustering Archetypes and the Connecting Passenger Paradox",
                "scope": "Clustering characteristics and DB1B connecting transfer passenger bypass dynamics",
                "dimension": "Network Topography & Queuing",
                "note": "Note. Unsupervised clustering parameters across the Top 25 airfields and empirical demonstration of the connecting passenger paradox, where airside connecting passenger transfers bypass landside TSA checkpoints."
            },
            {
                "table_id": "Table 1.4",
                "short_name": "data_sample_profile",
                "csv_file": "data_sample_profile.csv",
                "title": "Multi-Source Conformed Analytical Data Foundation Census",
                "scope": "Census of 4 conformed federal reporting feeds covering 42,062,039 analytical records",
                "dimension": "Data Foundation Census",
                "note": "Note. Conformed star-schema data foundation across four federal reporting feeds (TSA FOIA, BTS On-Time Performance, BTS Form 41 Schedule T-100, and BTS DB1B/DB1C Survey) covering 42,062,039 conformed records."
            },
            {
                "table_id": "Table 1.5",
                "short_name": "top25_network_approach",
                "csv_file": "inclusion_of_top_25_network_approach.csv",
                "title": "Top 25 Network Approach: Manuscript Placement, Scope, and Rhetorical Function",
                "scope": "Delimitations, assumptions, sample categorization, and causal identification placement",
                "dimension": "Manuscript Structure",
                "note": "Note. Methodological mapping of delimitations, assumptions, sample categorization, and causal identification justifications across thesis manuscript chapters."
            },
            {
                "table_id": "Table 1.6",
                "short_name": "post_pandemic_justification",
                "csv_file": "post_pandemic_justification.csv",
                "title": "Post-Pandemic Temporal Demarcation Evaluation (Candidate A vs. Candidate B)",
                "scope": "Comparative evaluation of Candidate A (Mature) vs Candidate B (May 1, 2022 Boundary)",
                "dimension": "Temporal Demarcation",
                "note": "Note. Comparative evaluation of post-pandemic temporal demarcation regimes. Candidate B (May 1, 2022 to December 31, 2025; 44 months) was formally selected for maximum statistical power while preserving structural regime stability."
            },
            {
                "table_id": "Table 1.7",
                "short_name": "power_of_9_airports",
                "csv_file": "power_of_9_airports.csv",
                "title": "The Nine-Airport Experimental Cohort: Generalizability and Twin Disruption Controls",
                "scope": "Spatial transfer pairs, twin disruption shock absorber controls, and statistical balance",
                "dimension": "Experimental Cohort Design",
                "note": "Note. Experimental design and testing logic for the nine-airport cohort, establishing intra-cluster zero-shot generalizability pairs and twin disruption resilience controls."
            }
        ]
    },
    {
        "folder_name": "02_Data_Pipelines_and_Threats",
        "wb_filename": "02_Data_Pipelines_and_Threats.xlsx",
        "target_dir": EXHIBITS_DIR / "ch03_methodology" / "workbooks",
        "csv_dir": EXHIBITS_DIR / "ch03_methodology" / "tables",
        "title": "DATA PIPELINES AND THREAT REMEDIATION TABLES",
        "subtitle": "Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow | Gleich 700B",
        "tables": [
            {
                "table_id": "Table 2.1",
                "short_name": "checkpoint_examples",
                "csv_file": "checkpoint_examples.csv",
                "title": "TSA FOIA Checkpoint Lane Naming Anomaly and Disambiguation Examples",
                "scope": "Representative FOIA lane naming anomalies, prepended codes, and throughput duplicates",
                "dimension": "Data Anomaly Disambiguation",
                "note": "Note. Representative instances of alphanumeric checkpoint lane naming anomalies and phonetic/code duplicates identified in raw TSA FOIA records resolved during automated ingestion."
            },
            {
                "table_id": "Table 2.2",
                "short_name": "pipeline_funnel_lifecycle",
                "csv_file": "combined_data_pipeline_and_funnel_lifecycle.csv",
                "title": "Multi-Source Aviation Data Pipeline and Processing Funnel Lifecycle",
                "scope": "Three-stage processing funnel from raw feeds (v0) to feature store (v1) to top 9 target",
                "dimension": "ETL Lifecycle & Funnel",
                "note": "Note. Processing funnel and reduction progression across Stage 1 (Raw Ingested Feeds v0), Stage 2 (Feature Store Parquet v1), and Stage 3 (Nine-Airport Modeling Cohort top9v1)."
            },
            {
                "table_id": "Table 2.3",
                "short_name": "threats_remediation_matrix",
                "csv_file": "combined_data_threats_and_remediation_matrix.csv",
                "title": "Master Aviation Data Threats and Methodological Remediation Matrix",
                "scope": "Audit of data integrity threats, theoretical risks, prevalence, and ETL remediations",
                "dimension": "Threat Remediation Matrix",
                "note": "Note. Master audit of empirical data integrity threats, theoretical failure risks, prevalence statistics, and corresponding mathematical cleansing remediations implemented across the ETL pipeline."
            },
            {
                "table_id": "Table 2.4",
                "short_name": "imputed_defs",
                "csv_file": "imputed_defs.csv",
                "title": "Data Lineage and Auditability Imputation Indicator Definitions",
                "scope": "Schema definitions for tracking imputation status, resolution method, and confidence",
                "dimension": "Lineage & Auditability",
                "note": "Note. Metadata schema definitions for tracking imputation status, resolution methodology, and algorithmic confidence scores ensuring full provenance auditability across all conformed records."
            },
            {
                "table_id": "Table 2.5",
                "short_name": "otp_tsa_volume_coupling",
                "csv_file": "otp_and_tsa_volume_coupling.csv",
                "title": "Flight Volume and Checkpoint Throughput Coupling Across Hub Archetypes",
                "scope": "Departures vs. checkpoint throughput and connecting passenger ratios across major hubs",
                "dimension": "Throughput Paradox Analysis",
                "note": "Note. Comparison of scheduled flight departures against annual checkpoint passenger throughput, highlighting the connecting hub throughput paradox at major connecting complexes."
            },
            {
                "table_id": "Table 2.6",
                "short_name": "otp_volatility",
                "csv_file": "otp_volatility.csv",
                "title": "Volatility Taxonomy and Distributional Moments of Core Flight Operational Attributes",
                "scope": "Coefficient of variation (CV) hierarchy, skewness, and kurtosis of BTS OTP attributes",
                "dimension": "Feature Volatility Hierarchy",
                "note": "Note. Empirical volatility hierarchy of Bureau of Transportation Statistics On-Time Performance attributes, classified by scale-free coefficient of variation (CV) at daily and individual flight grains."
            },
            {
                "table_id": "Table 2.7",
                "short_name": "t100_schema",
                "csv_file": "t100_schema.csv",
                "title": "BTS Form 41 Schedule T-100 Segment Capacity Dimension Schema",
                "scope": "Relational schema, data types, nullability, and dimension keys for monthly route capacity",
                "dimension": "Data Warehouse DDL",
                "note": "Note. Relational schema specification, field data types, nullability constraints, and dimension references for BTS Form 41 Schedule T-100 monthly carrier segment capacity records."
            },
            {
                "table_id": "Table 2.8",
                "short_name": "tsa_schema",
                "csv_file": "tsa_schema.csv",
                "title": "TSA Checkpoint Hourly Throughput Fact Table Schema",
                "scope": "Relational fact table schema, data types, nullability, and surrogate keys for hourly throughput",
                "dimension": "Data Warehouse DDL",
                "note": "Note. Relational fact table schema specification, field data types, nullability constraints, and surrogate key lookups for TSA checkpoint hourly passenger screening counts."
            }
        ]
    },
    {
        "folder_name": "03_Modeling_and_Evaluation",
        "wb_filename": "03_Modeling_and_Evaluation.xlsx",
        "title": "MODELING ARCHITECTURE AND EVALUATION TABLES",
        "subtitle": "Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow | Gleich 700B",
        "tables": [
            {
                "table_id": "Table 3.1",
                "short_name": "control_and_test_process",
                "csv_file": "control_and_test_process.csv",
                "title": "Experimental Control and Test Design: Dedicated Versus Shared Checkpoint Complexes",
                "scope": "Pure causal signal in carrier-exclusive terminals vs noisy aggregate shared terminals",
                "dimension": "Experimental Design Control",
                "note": "Note. Methodological rationale comparing carrier-exclusive terminal environments (pure causal signal) against multi-carrier shared checkpoints (noisy aggregate demand)."
            },
            {
                "table_id": "Table 3.2",
                "short_name": "evaluation_metric_defs",
                "csv_file": "evaluation_metric_definition.csv",
                "title": "Core Performance Evaluation Dimensions and Operational Definitions",
                "scope": "Robustness, Resilience, and Generalizability definitions, hypotheses, and metrics",
                "dimension": "Performance Dimensions",
                "note": "Note. Operational definitions, theoretical rationales, formal hypotheses, and quantitative performance metrics for the three evaluation dimensions: Robustness, Resilience, and Generalizability."
            },
            {
                "table_id": "Table 3.3",
                "short_name": "exploratory_metric_criteria",
                "csv_file": "exploratory_metric_criteria_research.csv",
                "title": "Exploratory Model Benchmarking Across Candidate Architectures and Regimes",
                "scope": "Preliminary evaluation metrics across baseline and exploratory hybrid variants",
                "dimension": "Preliminary Model Selection",
                "note": "Note. Preliminary exploratory performance benchmarks across preliminary baseline and hybrid model formulations across Generalizability, Resilience, and Robustness dimensions."
            },
            {
                "table_id": "Table 3.4",
                "short_name": "model_walkthrough_arch",
                "csv_file": "model_walkthrough_architecture.csv",
                "title": "Candidate Predictive Modeling Architectures and Evaluation Pipeline Stages",
                "scope": "Three-model candidate architecture specification, subcomponents, and holdout windows",
                "dimension": "Model Family Pipeline",
                "note": "Note. Architectural pipeline specification detailing preprocessing, algorithmic subcomponents, operational paradigms, and out-of-sample holdout windows for the three candidate models."
            },
            {
                "table_id": "Table 3.5",
                "short_name": "models_and_tests",
                "csv_file": "models_and_tests.csv",
                "title": "Empirical Comparison: Deterministic Flight Schedule Model Versus Dynamic Hybrid Model",
                "scope": "Empirical findings across arrival convolution, delay feedback, robustness, and transfer",
                "dimension": "Architectural Synthesis",
                "note": "Note. Empirical comparative findings across arrival timing convolution, delay feedback integration, routine operational accuracy (robustness), and spatial transferability (generalizability)."
            },
            {
                "table_id": "Table 3.6",
                "short_name": "pax_arrival_parameters",
                "csv_file": "passenger_stochastic_arrival_parameters.csv",
                "title": "Passenger Stochastic Arrival Kernel Parameters and Machine Learning Hyperparameters",
                "scope": "Continuous Lognormal arrival density parameters, quantile losses, and GBDT settings",
                "dimension": "Arrival Dynamics & ML",
                "note": "Note. Mathematical parameters for the continuous Lognormal passenger arrival density kernel (ACRP Report 40), quantile pinball loss intervals, and gradient boosting decision tree ensembles."
            },
            {
                "table_id": "Table 3.7",
                "short_name": "lead_lag_timeline",
                "csv_file": "physical_transfer_lead_lag_timeline.csv",
                "title": "Physical Passenger Progression Timeline and Lead-Lag Horizon Specification",
                "scope": "Temporal milestones from curbside arrival to screening, concourse dwell, and pushback",
                "dimension": "Queuing & Airport Geometry",
                "note": "Note. Unidirectional progression of passengers from landside arrival through TSA security screening, airside concourse dwell, gate boarding door closure, and scheduled aircraft pushback."
            },
            {
                "table_id": "Table 3.8",
                "short_name": "probabilistic_metrics",
                "csv_file": "probabilistic_and_selection_metrics.csv",
                "title": "Probabilistic Forecast Verification Metrics and Model Selection Criteria",
                "scope": "CRPS, PICP, AIC, and BIC definitions, mathematical formulations, and selection roles",
                "dimension": "Statistical Verification Metrics",
                "note": "Note. Mathematical definitions, operational objectives, and model selection utilities for probabilistic scoring rules (CRPS, PICP) and information-theoretic criteria (AIC, BIC)."
            }
        ]
    },
    {
        "folder_name": "04_Appendix_and_Reference",
        "wb_filename": "04_Appendix_and_Reference.xlsx",
        "title": "APPENDIX AND REFERENCE DATA TABLES",
        "subtitle": "Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow | Gleich 700B",
        "tables": [
            {
                "table_id": "Table 4.1",
                "short_name": "backups_organization",
                "csv_file": "backups_organization.csv",
                "title": "Research Archive Directory Structure and Data Backup Organization",
                "scope": "Directory hierarchy and manifest for raw datasets, processed SSOT, and codebase",
                "dimension": "Data Repository Architecture",
                "note": "Note. Master backup hierarchy and directory structure governing raw source feeds, processed feature stores, single sources of truth (SSOT), and version-controlled codebase scripts."
            },
            {
                "table_id": "Table 4.2",
                "short_name": "bts_db1b_hierarchy",
                "csv_file": "bts_db1b_table_hierarchy.csv",
                "title": "Bureau of Transportation Statistics DB1B Survey Relational Hierarchy",
                "scope": "Relational levels of DB1BTicket, DB1BMarket, and DB1BCoupon passenger survey tables",
                "dimension": "Passenger Survey Hierarchy",
                "note": "Note. Hierarchical structural relationship between DB1BTicket (entire round-trip ticket), DB1BMarket (directional city-pair market), and DB1BCoupon (physical takeoff-to-landing flight segment)."
            },
            {
                "table_id": "Table 4.3",
                "short_name": "data_profile_top9",
                "csv_file": "data_profile_top9.csv",
                "title": "Nine-Airport Experimental Cohort Feature Store Partition Profile",
                "scope": "Target cohort parquet file paths, record counts, and Zstandard compression metrics",
                "dimension": "Feature Store Partitions",
                "note": "Note. Filtered data partitions, record counts, file paths, and Zstandard compression specifications for the conformed nine-airport experimental cohort (top9v1)."
            },
            {
                "table_id": "Table 4.4",
                "short_name": "database_profiles",
                "csv_file": "database_profiles.csv",
                "title": "Raw Federal Aviation Feed Database Profiles and Physical Storage Sizing",
                "scope": "File sizes, record counts, schema widths, and temporal coverage across raw federal feeds",
                "dimension": "Input Feed Profiling",
                "note": "Note. Comparative profiles of the raw input databases (TSA FOIA, BTS On-Time Performance, and BTS Form 41 Schedule T-100) including disk storage footprints, record counts, and temporal coverage."
            },
            {
                "table_id": "Table 4.5",
                "short_name": "dataset_breakdown",
                "csv_file": "dataset_breakdown.csv",
                "title": "Conformed Feature Store Storage Footprint and Entity Grain Breakdown",
                "scope": "Storage size, rows, columns, and operational notes for parquet and DuckDB stores",
                "dimension": "Data Warehouse Storage",
                "note": "Note. Summary breakdown of deduplicated feature store Parquet artifacts (v1), DuckDB warehouse feature store views, and conformed star-schema dimensions."
            },
            {
                "table_id": "Table 4.6",
                "short_name": "diagrams_layout",
                "csv_file": "diagrams_and_screenshot_layout.csv",
                "title": "Master Visual Artifact, Figure, and Manuscript Screenshot Layout Catalog",
                "scope": "Inventory mapping all 30 figure graphics to manuscript chapters and descriptions",
                "dimension": "Visual Artifact Inventory",
                "note": "Note. Complete inventory and chapter cross-reference catalog mapping figure graphics and visual artifacts to their manuscript sections and operational topics."
            },
            {
                "table_id": "Table 4.7",
                "short_name": "methodological_assumptions",
                "csv_file": "methodological_assumptions.csv",
                "title": "Master Methodological Assumptions, Operational Justifications, and Failure Mode Remediations",
                "scope": "Fourteen core assumptions across terminal flow, temporal coupling, and sample filtering",
                "dimension": "Operational Assumptions",
                "note": "Note. Fourteen-point master inventory of methodological assumptions across terminal passenger flow, temporal lead-lag coupling, and purposive sample filtering."
            }
        ]
    }
]


def clean_header_title(raw_header: str) -> str:
    """Converts raw CSV snake_case header to APA 7 Title Case with authentic aviation nomenclature."""
    h = raw_header.strip()
    
    # Custom exact header overrides
    exact_overrides = {
        "operational_cluster": "Operational Cluster Archetype",
        "member_airports": "Member Airports",
        "american_airlines_exclusive_checkpoint": "American Airlines Exclusive Checkpoint",
        "delta_air_lines_exclusive_checkpoint": "Delta Air Lines Exclusive Checkpoint",
        "united_airlines_exclusive_checkpoint": "United Airlines Exclusive Checkpoint",
        "component": "Filtering Component",
        "focus_area": "Methodological Focus Area",
        "implementation_details": "Implementation Specification",
        "methodological_rationale": "Methodological & Causal Rationale",
        "cluster_or_airport": "Cluster / Airport Code",
        "archetype_or_phenomenon": "Operational Archetype / Phenomenon",
        "connecting_ratio_pct": "Connecting Passenger Ratio (%)",
        "load_factor_pct": "Mean Load Factor (%)",
        "mean_delay_minutes": "Mean Departure Delay (Min)",
        "operational_insight_and_mathematical_solution": "Operational Insight & Mathematical Solution",
        "operational_feed_conformance": "Primary Federal Data Feed",
        "primary_grain": "Entity Analytic Grain",
        "cleaned_records": "Conformed Cleaned Records",
        "scope_and_network": "Network Coverage & Airfield Scope",
        "chapter_and_section": "Manuscript Chapter & Section",
        "specific_document_heading": "Specific Manuscript Heading",
        "content_to_place": "Operational Content Specification",
        "purpose_and_rhetorical_function": "Purpose & Rhetorical Function",
        "evaluation_criteria": "Demarcation Evaluation Dimension",
        "candidate_a_mature_post_pandemic": "Candidate A: Mature Post-Pandemic (Jan 2023)",
        "candidate_b_early_post_mask_regime_recommended": "Candidate B: Early Post-Mask Regime (May 2022; Selected)",
        "experimental_dimension": "Experimental Evaluation Dimension",
        "test_cohort_category": "Cohort Test Category",
        "source_airport_carrier_complex": "Source Airport Carrier Complex",
        "target_airport_carrier_complex": "Target Airport Carrier Complex",
        "experimental_controls_and_testing_logic": "Experimental Controls & Testing Logic",
        "checkpoint_name_variant_1": "FOIA Checkpoint Variant 1",
        "checkpoint_name_variant_2": "FOIA Checkpoint Variant 2 (Normalized)",
        "identical_throughput_tp": "Identical Hourly Screening Volume (Pax)",
        "domain_feed": "Domain Aviation Feed",
        "data_grain": "Physical Data Grain",
        "stage_1_raw_feeds_v0": "Stage 1: Raw Ingested Feeds (v0)",
        "stage_2_feature_store_v1": "Stage 2: Feature Store Parquet (v1)",
        "stage_3_filtered_9airport_target_top9v1": "Stage 3: 9-Airport Target Cohort (top9v1)",
        "cohort_reduction_pct": "Cohort Funnel Reduction (%)",
        "severity": "Severity Level",
        "integrity_threat": "Data Integrity Threat",
        "data_source": "Affected Data Feed",
        "prevalence_and_metric_symptom": "Empirical Prevalence & Diagnostic Symptom",
        "failure_mode_theoretical_risk": "Theoretical Risk & Model Failure Mode",
        "methodological_cleansing_and_ml_action": "Methodological Cleansing & ML Remediation",
        "new_column_name": "Audit Metadata Field",
        "data_type": "Data Type",
        "description_and_value_example": "Field Definition & Representative Value",
        "operational_purpose": "Operational Purpose & Model Utility",
        "airport_iata": "Airport IATA",
        "airport_name": "Airport Facility Name",
        "scheduled_domestic_departures": "Scheduled Domestic Departures",
        "annual_tsa_passengers_millions": "Annual TSA Checkpoint Passengers (M)",
        "local_originating_pct": "Local Originating Traffic (%)",
        "connecting_transfer_pct": "Connecting Transfer Traffic (%)",
        "operational_category_and_notes": "Operational Category & Empirical Notes",
        "metric_name": "Flight Operational Metric",
        "volatility_class": "Volatility Classification",
        "cv_daily": "Daily Scale-Free Volatility (CV_daily)",
        "cv_flight_grain": "Flight-Grain Volatility (CV_flight)",
        "mean_or_median": "Central Tendency (Mean / Median)",
        "iqr_or_range": "Dispersion (IQR / Range)",
        "kurtosis_skewness": "Higher Moments (Skewness / Kurtosis)",
        "operational_implications": "Operational Implications for Checkpoint Flow",
        "column_name": "Physical Field Name",
        "nullable": "Nullable Constraint",
        "description": "Functional Field Description",
        "foreign_key_or_lookup_dimension": "Relational Key / Dimension Reference",
        "experimental_role": "Experimental Cohort Role",
        "checkpoint_environment_type": "Terminal Topology Environment",
        "checkpoint_count": "Checkpoint Sample Count",
        "methodological_rationale_and_testing_logic": "Methodological Rationale & Testing Logic",
        "performance_measure": "Performance Evaluation Dimension",
        "operational_definition": "Operational Research Definition",
        "evaluation_rationale_and_hypothesis": "Evaluation Rationale & Stated Hypothesis",
        "quantitative_metrics": "Quantitative Benchmark Metrics",
        "quality_or_metric": "Performance Metric / Quality Criterion",
        "base_sarima": "Deterministic Benchmark (SARIMA)",
        "base_lstm_squeezed": "Deep Recurrent Network (LSTM)",
        "hybrid_1_seasonal_switch": "Hybrid Variant 1 (Seasonal Switch)",
        "hybrid_3_dynamic_ensemble": "Two-Stage Dynamic Hybrid (Model 3)",
        "pipeline_stage": "Pipeline Operational Stage",
        "model_architecture": "Candidate Model Architecture",
        "model_paradigm": "Operational Modeling Paradigm",
        "algorithmic_subcomponent": "Algorithmic Subcomponent & Loss Function",
        "evaluation_window_and_regimes": "Evaluation Window & Testing Regimes",
        "methodological_test": "Methodological Research Test",
        "deterministic_baseline_model_1": "Model 1: Deterministic Schedule Baseline",
        "probabilistic_ml_model_model_3": "Model 3: Dynamic Two-Stage Hybrid Model",
        "empirical_finding_proof": "Empirical Finding & Statistical Proof",
        "component_family": "Architectural Component Family",
        "modeling_approach": "Predictive Modeling Approach",
        "distribution_or_algorithm": "Mathematical Distribution / Algorithm",
        "parameters_and_hyperparameters": "Calibrated Parameters & Hyperparameters",
        "operational_mechanics_and_purpose": "Operational Mechanics & Purpose",
        "operational_milestone": "Passenger Journey Milestone",
        "airport_zone": "Physical Airport Zone",
        "lead_time_relative_to_departure": "Lead Time Relative to Departure",
        "operational_mechanics_and_feedback": "Operational Mechanics & Feedback Signal",
        "metric_family": "Metric Classification Family",
        "abbreviation": "Metric Symbol",
        "mathematical_operational_purpose": "Mathematical & Operational Objective",
        "model_selection_utility": "Model Selection & Verification Utility",
        "backup_directory_path": "Backup Directory Path",
        "directory_level": "Directory Level",
        "description_and_contents": "Directory Description & File Contents",
        "bts_table_level": "BTS Survey Relational Level",
        "table_acronym": "Table Acronym",
        "unit_or_grain": "Entity Analysis Grain",
        "example_itinerary_representation_bos_ord_lax": "Representative Itinerary Example (BOS-ORD-LAX)",
        "contains_connecting_itineraries": "Includes Connecting Itineraries",
        "dataset_name": "Analytical Feature Store Dataset",
        "parquet_file_path": "Processed Parquet File Path",
        "record_count": "Conformed Record Count",
        "compression_format": "Compression Standard",
        "tsa_throughput_tsav0_csv": "TSA Checkpoint Screening (tsav0.csv)",
        "on_time_performance_otpv0_csv": "BTS On-Time Performance (otpv0.csv)",
        "t100_segment_statistics_t100v0_csv": "BTS Form 41 Schedule T-100 (t100v0.csv)",
        "dataset_file": "Feature Store File",
        "storage_size_parquet": "Storage Size (Parquet)",
        "uncompressed_ram_approx": "Uncompressed RAM Footprint",
        "operational_notes": "Operational Grain & Lineage Notes",
        "folder": "Figure Subfolder",
        "filename": "Figure Graphic Filename",
        "chapter_mapping": "Manuscript Chapter Placement",
        "level": "Methodological Level",
        "key_assumption": "Key Research Assumption",
        "mathematical_operational_justification": "Mathematical & Operational Justification",
        "failure_mode_prevented": "Empirical Failure Mode Prevented"
    }
    
    if h in exact_overrides:
        return exact_overrides[h]
        
    special = {
        "iata": "IATA", "icao": "ICAO", "otp": "OTP", "tsa": "TSA",
        "bts": "BTS", "db1b": "DB1B", "db1c": "DB1C", "t100": "T-100",
        "cv": "CV", "mase": "MASE", "rmse": "RMSE", "mape": "MAPE",
        "sd": "SD", "iqr": "IQR", "ddl": "DDL", "sql": "SQL",
        "foia": "FOIA", "nas": "NAS", "gdp": "GDP", "faa": "FAA",
        "od": "O&D", "aic": "AIC", "bic": "BIC", "crps": "CRPS",
        "picp": "PICP", "ttr": "TTR", "rtr": "RTR", "pct": "(%)",
        "min": "(Min)", "hrs": "(Hrs)", "hr": "Hr", "pax": "Pax",
        "sarima": "SARIMA", "lstm": "LSTM", "ml": "ML"
    }
    words = h.replace("_", " ").split()
    cleaned = []
    for w in words:
        wl = w.lower()
        if wl in special:
            cleaned.append(special[wl])
        elif w.isupper() and len(w) > 1:
            cleaned.append(w)
        else:
            cleaned.append(w.capitalize())
    return " ".join(cleaned)


def parse_cell_value(val_str: str):
    """
    Parses raw CSV string into appropriate Python types with number formats and alignment.
    Returns: (parsed_value, number_format, horizontal_alignment)
    """
    s = str(val_str).strip()
    if not s:
        return "", None, "left"

    # Missing / Null representations or dashes
    if s in ("—", "-", "--", "N/A", "NA", "None", "NULL"):
        return s, None, "center"

    # Boolean values
    if s.upper() in ("TRUE", "FALSE", "YES", "NO"):
        return s, None, "center"

    # Formatted integer with commas e.g. '6,434,732' or '19,500,286'
    clean_int_s = s.replace(",", "")
    if clean_int_s.isdigit() and ("," in s or len(s) > 1):
        try:
            return int(clean_int_s), "#,##0", "right"
        except ValueError:
            pass

    # Pure signed integer
    if s.isdigit() or (s.startswith("-") and s[1:].isdigit()):
        try:
            return int(s), "#,##0", "right"
        except ValueError:
            pass

    # Floating point numbers
    try:
        f = float(s)
        if "." in s:
            decimals = len(s.split(".")[1])
            fmt = "0." + "0" * min(decimals, 4)
        else:
            fmt = "0.00"
        return f, fmt, "right"
    except ValueError:
        pass

    # Percentages e.g. '56.1%', '+108.4%', '0.0%', '-83.96%'
    if s.endswith("%"):
        clean_pct = s[:-1].replace("+", "").strip()
        try:
            float(clean_pct)
            return s, None, "right"
        except ValueError:
            pass

    # Checkpoint codes / Time stamps (e.g. 05:00) / Airport codes (BOS, DFW)
    if len(s) <= 5 and (s.isupper() or ":" in s or s in ("BP01", "LAN", "SBP")):
        return s, None, "center"

    return s, None, "left"


def generate_workbook_for_subfolder(subfolder_info: dict):
    """Builds a single multi-tab APA 7th Excel workbook for a figures subfolder."""
    folder_name = subfolder_info["folder_name"]
    wb_filename = subfolder_info["wb_filename"]
    tables = subfolder_info["tables"]
    wb_title = subfolder_info["title"]
    wb_subtitle = subfolder_info["subtitle"]
    
    subfolder_path = FIGURES_DIR / folder_name
    print(f"\n" + "=" * 80)
    print(f" BUILDING WORKBOOK: {wb_filename} (Folder: {folder_name})")
    print("=" * 80)

    wb = openpyxl.Workbook()
    wb.remove(wb.active)  # Remove default blank sheet

    # APA 7th Border Rules (Thin black horizontal lines, no vertical rules)
    thin_black = Side(style="thin", color="000000")
    border_header = Border(top=thin_black, bottom=thin_black)
    border_last_row = Border(bottom=thin_black)
    border_none = Border()

    # APA Typography (Calibri, black, no fill)
    font_toc_title = Font(name="Calibri", size=13, bold=True, color="000000")
    font_toc_sub = Font(name="Calibri", size=10, italic=True, color="444444")
    font_toc_instr = Font(name="Calibri", size=10, bold=False, color="333333")
    
    font_header = Font(name="Calibri", size=11, bold=True, color="000000")
    font_data = Font(name="Calibri", size=11, bold=False, color="000000")
    font_link = Font(name="Calibri", size=10, bold=True, color="000563C1", underline="single")
    font_table_id = Font(name="Calibri", size=11, bold=True, color="000000")
    font_table_title = Font(name="Calibri", size=11, italic=True, color="000000")
    font_note = Font(name="Calibri", size=10, italic=True, color="333333")

    # =========================================================================
    # 1. CREATE 'Contents' SHEET (First Sheet)
    # =========================================================================
    ws_toc = wb.create_sheet(title="Contents")
    ws_toc.views.sheetView[0].showGridLines = True
    ws_toc.freeze_panes = "A6"

    # Title block
    ws_toc["A1"] = wb_title
    ws_toc["A1"].font = font_toc_title
    ws_toc.row_dimensions[1].height = 24

    ws_toc["A2"] = wb_subtitle
    ws_toc["A2"].font = font_toc_sub
    ws_toc.row_dimensions[2].height = 18

    ws_toc["A3"] = "Interactive Table Index: Click any Sheet Name or Table ID to navigate directly to that table. Every worksheet includes a '⬅ Return to Table of Contents' link in Cell A1."
    ws_toc["A3"].font = font_toc_instr
    ws_toc.row_dimensions[3].height = 20

    ws_toc.row_dimensions[4].height = 10  # blank buffer

    # TOC Headers (Row 5)
    toc_headers = [
        "Table ID",
        "Sheet Tab (Click to Jump)",
        "Official Academic Table Title",
        "Entity Analysis Scope & Grain",
        "Table Dimensions",
        "Analytical Focus & Methodological Role"
    ]
    ws_toc.row_dimensions[5].height = 26
    for col_idx, h_text in enumerate(toc_headers, 1):
        cell = ws_toc.cell(row=5, column=col_idx, value=h_text)
        cell.font = font_header
        cell.border = border_header
        align_h = "left" if col_idx in (2, 3) else ("center" if col_idx in (1, 5) else "left")
        cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=True)

    # Populate TOC rows
    toc_current_row = 6
    for t_info in tables:
        csv_file = t_info["csv_file"]
        csv_path = subfolder_path / csv_file
        short_name = t_info["short_name"]
        table_id = t_info["table_id"]
        table_title = t_info["title"]
        scope = t_info["scope"]
        dimension = t_info["dimension"]

        num_rows = 0
        num_cols = 0
        if csv_path.exists():
            with open(csv_path, "r", encoding="utf-8") as f:
                reader = list(csv.reader(f))
                if len(reader) > 0:
                    num_rows = len(reader) - 1
                    num_cols = len(reader[0])

        dim_str = f"{num_rows} rows x {num_cols} cols"
        ws_toc.row_dimensions[toc_current_row].height = 22

        # Col 1: Table ID (Hyperlinked)
        c1 = ws_toc.cell(row=toc_current_row, column=1, value=table_id)
        c1.font = font_link
        c1.hyperlink = f"#'{short_name}'!A1"
        c1.alignment = Alignment(horizontal="center", vertical="center")
        c1.border = border_none

        # Col 2: Sheet Tab (Hyperlinked)
        c2 = ws_toc.cell(row=toc_current_row, column=2, value=short_name)
        c2.font = font_link
        c2.hyperlink = f"#'{short_name}'!A1"
        c2.alignment = Alignment(horizontal="left", vertical="center")
        c2.border = border_none

        # Col 3: Table Title
        c3 = ws_toc.cell(row=toc_current_row, column=3, value=table_title)
        c3.font = font_data
        c3.alignment = Alignment(horizontal="left", vertical="center")
        c3.border = border_none

        # Col 4: Scope
        c4 = ws_toc.cell(row=toc_current_row, column=4, value=scope)
        c4.font = font_data
        c4.alignment = Alignment(horizontal="left", vertical="center")
        c4.border = border_none

        # Col 5: Dimensions
        c5 = ws_toc.cell(row=toc_current_row, column=5, value=dim_str)
        c5.font = font_data
        c5.alignment = Alignment(horizontal="center", vertical="center")
        c5.border = border_none

        # Col 6: Dimension
        c6 = ws_toc.cell(row=toc_current_row, column=6, value=dimension)
        c6.font = font_data
        c6.alignment = Alignment(horizontal="left", vertical="center")
        c6.border = border_none

        toc_current_row += 1

    # Bottom border on last row of TOC table
    last_toc_row = toc_current_row - 1
    for c in range(1, 7):
        ws_toc.cell(row=last_toc_row, column=c).border = border_last_row

    # Note below TOC table
    toc_note_row = last_toc_row + 2
    ws_toc.row_dimensions[toc_note_row].height = 24
    c_toc_note = ws_toc.cell(row=toc_note_row, column=1, value=f"Note. Master consolidated tabular dataset corresponding to figures in {folder_name}. Formatted strictly according to APA Style (7th ed.) with horizontal boundary rules, zero auto-filters, and no background shading.")
    c_toc_note.font = font_note

    # Auto-adjust TOC column widths
    for col in ws_toc.iter_cols(min_row=5, max_row=last_toc_row):
        col_letter = get_column_letter(col[0].column)
        max_len = 0
        for cell in col:
            val_s = str(cell.value or "")
            if len(val_s) > max_len:
                max_len = len(val_s)
        ws_toc.column_dimensions[col_letter].width = max(min(max_len + 4, 60), 12)

    # =========================================================================
    # 2. CREATE INDIVIDUAL TABLE WORKSHEETS (APA 7th Format)
    # =========================================================================
    for t_info in tables:
        csv_file = t_info["csv_file"]
        csv_path = subfolder_path / csv_file
        short_name = t_info["short_name"]
        table_id = t_info["table_id"]
        table_title = t_info["title"]
        note_text = t_info["note"]

        if not csv_path.exists():
            print(f"  [WARNING] File missing: {csv_path}")
            continue

        with open(csv_path, "r", encoding="utf-8") as f:
            reader = list(csv.reader(f))

        raw_headers = reader[0]
        data_rows = reader[1:]
        num_rows = len(data_rows)
        num_cols = len(raw_headers)

        # Format column headers to APA 7 Title Case
        clean_headers = [clean_header_title(h) for h in raw_headers]

        ws_t = wb.create_sheet(title=short_name)
        ws_t.views.sheetView[0].showGridLines = True
        ws_t.freeze_panes = "A6"

        # Explicitly ensure NO Table objects and NO auto-filter
        ws_t.tables.clear()
        ws_t.auto_filter.ref = None

        # Row 1: Back link to Table of Contents
        ws_t.row_dimensions[1].height = 20
        c_back = ws_t.cell(row=1, column=1, value="⬅ Return to Table of Contents")
        c_back.font = font_link
        c_back.hyperlink = "#'Contents'!A1"
        c_back.alignment = Alignment(horizontal="left", vertical="center")

        # Row 2: Table ID (APA 7th: Line 1 in Bold)
        ws_t.row_dimensions[2].height = 22
        c_tid = ws_t.cell(row=2, column=1, value=table_id)
        c_tid.font = font_table_id
        c_tid.alignment = Alignment(horizontal="left", vertical="center")

        # Row 3: Table Title (APA 7th: Line 2 in Italic)
        ws_t.row_dimensions[3].height = 22
        c_ttitle = ws_t.cell(row=3, column=1, value=table_title)
        c_ttitle.font = font_table_title
        c_ttitle.alignment = Alignment(horizontal="left", vertical="center")

        ws_t.row_dimensions[4].height = 10  # Blank spacing buffer

        # Row 5: Column Headers (APA 7th: Thin border top and bottom, no fill)
        ws_t.row_dimensions[5].height = 28
        for c_idx, h_text in enumerate(clean_headers, 1):
            cell = ws_t.cell(row=5, column=c_idx, value=h_text)
            cell.font = font_header
            cell.border = border_header
            # Col 1 left-aligned; other columns centered
            align_h = "left" if c_idx == 1 else "center"
            cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=True)

        # Rows 6+: Data Rows (APA 7th: No internal horizontal rules, no vertical rules, no fill)
        for r_offset, r_vals in enumerate(data_rows, 0):
            current_row = 6 + r_offset
            ws_t.row_dimensions[current_row].height = 20
            is_last_data_row = (r_offset == num_rows - 1)

            # Check if this row is a total/summary row (e.g. 'TOTALS PER CARRIER')
            is_summary_row = False
            if len(r_vals) > 0 and any(keyword in str(r_vals[0]).upper() for keyword in ("TOTAL", "TOTALS", "OVERALL", "MEAN")):
                is_summary_row = True

            for c_idx, raw_val in enumerate(r_vals, 1):
                val, num_fmt, align_h = parse_cell_value(raw_val)
                cell = ws_t.cell(row=current_row, column=c_idx, value=val)
                
                # If summary row, bold font
                if is_summary_row:
                    cell.font = Font(name="Calibri", size=11, bold=True, color="000000")
                else:
                    cell.font = font_data
                    
                cell.alignment = Alignment(horizontal=align_h, vertical="center", wrap_text=True)

                # Boundary rule on last data row
                if is_last_data_row:
                    cell.border = border_last_row
                elif is_summary_row and r_offset > 0:
                    # Thin border above summary row if applicable
                    cell.border = Border(top=thin_black)
                else:
                    cell.border = border_none

                if num_fmt:
                    cell.number_format = num_fmt

        # Row (6 + num_rows + 1): APA Note (Below table, italic, no border)
        note_row_idx = 6 + num_rows + 1
        ws_t.row_dimensions[note_row_idx].height = 24
        c_note = ws_t.cell(row=note_row_idx, column=1, value=note_text)
        c_note.font = font_note
        c_note.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

        # Auto-adjust column widths with minimum and maximum bounds
        for col_idx in range(1, num_cols + 1):
            col_letter = get_column_letter(col_idx)
            max_len = len(str(clean_headers[col_idx - 1]))
            for r_offset in range(num_rows):
                val_str = str(data_rows[r_offset][col_idx - 1] if col_idx - 1 < len(data_rows[r_offset]) else "")
                if len(val_str) > max_len:
                    max_len = len(val_str)
            # Clamp width between 14 and 60
            ws_t.column_dimensions[col_letter].width = max(min(max_len + 4, 60), 14)

        print(f"  + Added sheet '{short_name}' ({table_id}: {num_rows} rows x {num_cols} cols)")

    # =========================================================================
    # 3. SAVE WORKBOOK
    # =========================================================================
    # Save inside subfolder AND copy to figures/ root
    dest_paths = [
        subfolder_path / wb_filename,
        FIGURES_DIR / wb_filename
    ]

    for p in dest_paths:
        p.parent.mkdir(parents=True, exist_ok=True)
        wb.save(p)
        print(f"  -> Saved workbook: {p}")

    # Synchronize non-appendix workbooks to thesis_docs/exhibits/ch03_methodology/workbooks/
    exhibits_wb_dir = BASE_DIR / "thesis_docs" / "exhibits" / "ch03_methodology" / "workbooks"
    if exhibits_wb_dir.exists() and "Appendix" not in folder_name:
        exhibit_dest = exhibits_wb_dir / wb_filename
        wb.save(exhibit_dest)
        print(f"  -> Synchronized exhibits workbook: {exhibit_dest}")

    return dest_paths


def build_all_figure_workbooks():
    """Generates APA-formatted Excel workbooks for all 4 subfolders in figures/."""
    print("=" * 80)
    print(" GENERATING APA 7TH EDITION EXCEL WORKBOOKS FOR ALL 4 FIGURES SUBFOLDERS")
    print("=" * 80)
    
    generated = []
    for sf_info in SUBFOLDER_WORKBOOKS:
        paths = generate_workbook_for_subfolder(sf_info)
        generated.extend(paths)

    print("\n" + "=" * 80)
    print(f" [SUCCESS] Generated {len(generated)} Excel workbooks across all 4 figures subfolders.")
    print("=" * 80)
    return generated


if __name__ == "__main__":
    build_all_figure_workbooks()
