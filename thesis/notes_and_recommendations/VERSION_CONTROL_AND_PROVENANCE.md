# RESEARCH DATA PROVENANCE, INTEGRITY & VERSION CONTROL SPECIFICATION
====================================================================================================
PROJECT: Empirical Modeling of Airport Security Screening Demand and Flight Performance Coupling
AUTHOR: Leila Gleich | INSTITUTION: Embry-Riddle Aeronautical University
DEGREE: Master of Science in Aeronautics / Aviation Data Analytics
LOCATION: Results_and_Analysis/00_VERSION_CONTROL_AND_PROVENANCE.md
RELEASE VERSION: v3.0 (Unified Publication-Grade Results Architecture)
DATE: September 2026
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
| v3.0    | 2026-09-17 | Unified Results Architecture Release: Consolidates all four federal feeds, |
|         |            | the Executive Summary Suite, the 25-airport master census, coupled cross-  |
|         |            | dataset dynamics, and domain-organized results into Results_and_Analysis/. |
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
The Results_and_Analysis/ directory is structured into four primary hubs:

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
