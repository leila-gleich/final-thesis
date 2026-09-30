# Data Quality, Anomaly Resolution & Star Schema Architecture: Analytical Findings & Walkthrough

## 1. Executive Summary

This walkthrough details the complete data quality lifecycle, anomaly resolution methodology, and conformed Star Schema relational architecture across the 67,222,828 fact records and 10 conformed dimension lookup tables comprising the v2 analytical data warehouse:
* **TSA Checkpoint Fact Records**: 19,500,286 rows.
* **OTP Flight Departure Fact Records**: 45,777,091 rows.
* **T-100 Segment Capacity Fact Records**: 1,945,451 rows.
* **Conformed Dimension Records**: 8,452 rows across 10 dimension lookup tables.

Across all tables, the pipeline achieves **0.00% foreign key nulls**, **zero orphaned relational keys**, and complete conformed integrity across spatial, temporal, carrier, equipment, and operational categorization entities.

---

## 2. Conformed Dimension Tables & Entity Architecture

The 10 conformed dimension lookup tables establish a single source of truth (SSOT) that enables frictionless joins across disparate aviation data feeds:

1. **`dim_airport` (460 records)**:
   * Maps 3-letter IATA airport codes, official primary airport names, and geographic classifications.
   * Conforms all origin and destination airports across TSA, OTP, and T-100.
   * Assigns surrogate key `airportId = 0` to designate unmapped or missing airport records (`UNKNOWN`).
2. **`dim_date` (2,739 records)**:
   * Continuous calendar dimension spanning January 1, 2019 through June 30, 2026.
   * Encodes `dateId` in standard `YYYYMMDD` integer format alongside year, quarter, month, day of week, weekend indicator, and federal holiday classifications.
3. **`dim_time_block` (19 records)**:
   * Conforms Bureau of Transportation Statistics (BTS) standard time intervals: Block 1 (00:01–05:59), Blocks 2–18 (hourly intervals from 06:00 to 22:59), and Block 19 (23:00–23:59).
   * Enables direct hour-to-block mapping between TSA hourly counts and OTP scheduled flight blocks.
4. **`dim_aircraft` (7,617 records)**:
   * Conforms FAA tail registration numbers to integer surrogate keys.
   * Assigns surrogate key `aircraftId = 0` for unassigned aircraft.
5. **`dim_airline` (21 records)**:
   * Maps 2-letter IATA airline codes (e.g., AA, DL, UA, WN, OO) to certified operating certificate numbers.
6. **`dim_delay_type` (7 records)**:
   * Categorizes primary delay causes into mutually exclusive keys: 0 = No Delay, 1 = Air Carrier, 2 = Weather, 3 = National Airspace System, 4 = Security, 5 = Late Arriving Aircraft, 6 = Tied Causes.
7. **`dim_cancellation_reason` (5 records)**:
   * Standardizes flight cancellation causes: 0 = Not Cancelled, 1 = Air Carrier, 2 = Weather, 3 = National Airspace System, 4 = Security.
8. **`dim_checkpoint` (7,371 records)**:
   * Uniquely indexes physical airport security screening lanes, concourses, and checkpoint terminals.
9. **`L_AIRCRAFT_TYPE` (40 records)**:
   * BTS 3-digit aircraft model code reference table providing equipment descriptions and capacity profiles.
10. **`L_AIRCRAFT_CONFIG` (6 records)**:
    * Standardizes aircraft configuration codes (Code 1 = Scheduled Passenger Configuration).

---

## 3. Data Cleaning & Anomaly Resolution Findings

### A. Deduplication Lifecycle
* Across raw weekly TSA FOIA extractions, exactly **5,279 duplicate rows** were identified and purged where identical checkpoint volumes were logged across overlapping reporting windows.
* Fact tables enforce strict composite uniqueness constraints preventing multi-counting during data refreshes.

### B. Resolution of Missing Airport Identifiers in TSA Data
* In raw extractions, 35,809 records (0.18% of rows) contained blank airport codes and names.
* **Resolution Strategy**:
  * **Deterministic Checkpoint Recovery**: 7,489 rows were successfully backfilled by matching unique checkpoint name signatures to known airport terminals.
  * **Surrogate Unknown Conformation**: The remaining 22,190 unresolved rows (accounting for 9.71 million passengers) were assigned to `airportId = 0` (`UNKNOWN`) and flagged with `airportMissing = 1`.
  * **Integrity Result**: Complete preservation of national aggregate throughput volumes without corrupting airport-specific queries.

### C. Resolution of Late 2025 / Early 2026 Format Anomalies
* 154 records in late 2025 and early 2026 contained checkpoint abbreviations (`ACP`, `BCP`, `FIS`) in the airport code field with numeric string names (`'289'`, `'238'`).
* **Root Cause**: Upstream column misassignment during FOIA reporting template updates.
* **Resolution**: Re-mapped into the conformed checkpoint dimension without contaminating clean airport lookups.

### D. Conformation of Delay & Cancellation Nulls in OTP Data
* In raw flight records, non-delayed flights contain blank entries for delay causes, and completed flights contain blank cancellation codes.
* **Resolution**: Standardized to clean relational default keys (`delay_type_id = 0` for *No Delay*, `cancellation_id = 0` for *Not Cancelled*, and integer `0` for delay minutes), eliminating SQL `NULL` propagation risks.

---

## 4. Storage & Query Optimization

Through star schema normalization, integer surrogate key substitution, and numerical downcasting:
* **OTP Dataset**: Reduced from 9.2 GB to **6.5 GB** (29.3% reduction).
* **TSA Dataset**: Reduced from ~1.29 GB to **~518 MB** (59.8% reduction).
* **T-100 Dataset**: Normalized to a compact **81.0 MB**.
* **Query Performance**: Eliminated multi-column text joins; all fact-to-dimension relationships resolve via high-speed 32-bit and 64-bit integer index comparisons.
