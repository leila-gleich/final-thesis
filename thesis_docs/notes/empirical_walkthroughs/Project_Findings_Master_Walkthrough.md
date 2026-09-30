# Master Project Findings & Comprehensive Research Walkthrough

## 1. Executive Summary

This research project establishes a unified, high-integrity analytical data warehouse and machine learning foundation integrating three primary federal aviation datasets across the 2019–2026 observation period:
1. **TSA Hourly Passenger Checkpoint Throughput** (`tsa-transform-cloudv2.csv`): 19,500,286 hourly checkpoint observations capturing 5.24 billion screened passengers across 459 airports and 7,371 checkpoint lanes.
2. **BTS On-Time Performance Flight Departures** (`otp-transform-cloudv2.csv`): 45,777,091 domestic commercial flight observations across 21 reporting air carriers, 389 airports, and 7,617 unique aircraft tail registrations.
3. **BTS T-100 Domestic Segment Capacity Statistics** (`t100-transform-cloudv2.csv`): 1,945,451 carrier segment capacity records covering 6.67 billion available seats, 5.23 billion transported revenue passengers, and 40 distinct aircraft equipment models.

Across a combined total of **67,222,828 fact records** and **10 conformed dimension lookup tables** (8,452 dimension entities), the data architecture resolves historical anomalies, normalizes disparate temporal and spatial granularities into a conformed Star Schema, enforces 100% referential integrity (zero orphan keys), and establishes formal mathematical mitigations against machine learning data integrity threats.

---

## 2. Research Context: The Post-COVID Aviation Ecosystem

The post-COVID recovery period represents a profound structural shift in air transportation dynamics:
* **Decoupling of Traditional Demand Patterns**: Historical pre-2020 seasonalities and day-of-week load curves underwent substantial transformations due to remote work flexibility, hybrid business travel, and shifting leisure peaks.
* **Operational Friction at the Airport Boundary**: Airport security checkpoints serve as the critical bottleneck connecting landside passenger arrivals with airside aircraft departures. Understanding the exact quantitative relationship between checkpoint throughput and scheduled vs. actual departures requires bridging the temporal gap between when passengers clear screening and when aircraft push back from gates.
* **Capacity and Fleet Dynamics**: Incorporating aircraft seating capacities by equipment type and carrier-specific route load factors enables the translation of raw flight schedules into high-fidelity passenger demand curves.

---

## 3. Comprehensive Dataset Findings & Statistical Profiles

### A. TSA Checkpoint Throughput Findings
* **Temporal Span**: January 1, 2019 through June 13, 2026 (2,721 days).
* **Aggregate Volume**: 5,240,443,482 screened passengers with an overall system mean of 268.74 passengers per operational checkpoint hour.
* **Volume Distribution & Skewness**: Throughput exhibits strong positive right-skewness (coefficient = 2.72) and zero-inflation. Approximately 450,973 records (2.31%) represent non-operational overnight windows (01:00–03:59), while peak morning hours (05:00–08:00) at major hub airports reach up to 5,336 screened passengers per hour across consolidated checkpoint lanes.
* **Peak Volume Milestones**: System-wide peak post-COVID single-day travel occurred on November 3, 2025 (3,095,205 screened passengers), surpassing pre-pandemic benchmarks.
* **Top Hub Volumes**: Hartsfield-Jackson Atlanta International (ATL), Los Angeles International (LAX), Orlando International (MCO), Dallas/Fort Worth International (DFW), and Denver International (DEN) represent the highest cumulative passenger processing volumes.

### B. On-Time Performance (OTP) Flight Departures & Delays Findings
* **Temporal Span**: January 1, 2019 through December 31, 2025 (2,557 unique flight dates; 7 complete annual cycles).
* **Operational Flight Breakdown**:
  * Completed On-Time / Minor Delayed Flights: 36,265,825 flights (79.22%).
  * Significant Departure Delays (15 minutes or greater): 8,523,111 flights (18.62% delayed departure rate).
  * Flight Cancellations: 988,155 flights (2.16% overall cancellation rate).
  * Flight Diversions: 109,917 flights (0.24% diversion rate).
* **Delay Causality Hierarchy**: Among flights experiencing delays of 15 minutes or more, delay minutes are distributed across five federal reporting categories: Late Arriving Aircraft (dominant propagation factor), Carrier Operational Delays, National Airspace System (NAS) Traffic Management, Severe Weather, and Security Delays (least frequent, <0.1%).
* **Carrier Concentration**: Southwest Airlines (WN), Delta Air Lines (DL), American Airlines (AA), SkyWest Airlines (OO), and United Airlines (UA) account for the top five operational volumes, handling over 68% of all domestic commercial movements.

### C. T-100 Carrier Capacity, Equipment & Load Factor Findings
* **Temporal Span**: January 2019 through May 2026.
* **System Capacity & Passenger Load**: 6,667,727,408 available seats and 5,228,698,539 transported revenue passengers, yielding a system-wide aggregate load factor of 78.42%.
* **Load Factor Distribution**: Route-level load factors exhibit a bell curve centered between 78% and 86% during peak post-COVID quarters. Exactly 23 records out of 1.95 million (0.001%) report load factors slightly exceeding 1.00 (up to 101.45%) resulting from lap infant travel and overbooked passenger seat management.
* **Fleet Heterogeneity**: 40 distinct BTS aircraft equipment codes capture the full spectrum of domestic operations, from regional turboprops and regional jets (<76 seats) to narrowbody workhorses (Boeing 737 / Airbus A320 families, 140–190 seats) and widebody aircraft (Boeing 777 / 787 and Airbus A330 / A350, 250–400+ seats).

---

## 4. Star Schema & Referential Integrity Architecture

To support high-performance analytical queries and predictive modeling, the data warehouse implements an enterprise Star Schema centered on conformed surrogate keys across all dimensions:
1. `dim_airport` (460 records): Conforms 3-letter IATA airport codes, official names, and geographic classifications across all three fact datasets. Includes surrogate key 0 for unresolved airport entries.
2. `dim_date` (2,739 records): Conforms calendar dates from 2019 through mid-2026 with year, quarter, month, day of week, weekend indicators, and federal holiday classifications.
3. `dim_time_block` (19 records): Standardizes BTS hourly time intervals (0001–0559, hourly blocks 0600–2259, and 2300–2359) mapping seamlessly between TSA hourly timestamps and OTP departure scheduled blocks.
4. `dim_aircraft` (7,617 records): Conforms FAA tail registration numbers, linking physical aircraft airframes to operational histories.
5. `dim_airline` (21 records): Maps 2-letter IATA carrier codes to certified operating certificates.
6. `dim_delay_type` (7 records): Maps dominant flight delay causes (No Delay, Carrier, Weather, NAS, Security, Late Aircraft, Tied Causes).
7. `dim_cancellation_reason` (5 records): Maps operational cancellation categorizations.
8. `dim_checkpoint` (7,371 records): Uniquely identifies individual security screening lanes across all reporting airport terminals.
9. `L_AIRCRAFT_TYPE` (40 records): Reference table for BTS standard aircraft equipment codes.
10. `L_AIRCRAFT_CONFIG` (6 records): Reference table for seating and cargo payload configurations.

**Referential Integrity Status**: 100.0% of foreign keys across all 67.22M fact records resolve to valid conformed dimension primary keys, with zero orphaned records.

---

## 5. Machine Learning Modeling Dynamics & Threat Mitigations

### A. Lead-Lag Temporal Dynamics & Target Leakage
* In an operational setting, passengers clear security 90 to 150 minutes prior to scheduled departure. Using actual departure timestamps or actual departure delay minutes concurrently with throughput at hour $t$ represents severe target leakage.
* **Mitigation**: Models must construct scheduled departure seat capacity features lagged across future hours ($t+1, t+2, t+3$). Actual delays from prior hours ($t-1$) are utilized strictly as airport congestion state indicators.

### B. Post-COVID Structural Regime Breaks
* Pre-2020 behavioral parameters cannot be applied naively to post-2022 forecasts without introducing substantial concept drift.
* **Mitigation**: Model training pipelines must either isolate post-recovery windows (2022–2025) or utilize exponential time-decay sample weighting alongside walk-forward time-series validation.

### C. Zero-Inflation and Non-Negative Count Targets
* Standard Gaussian loss functions (MSE/RMSE) fail on TSA throughput by producing negative passenger forecasts at night and underestimating early morning surges.
* **Mitigation**: Utilization of Tweedie deviance loss ($p \approx 1.3\text{--}1.5$), Poisson regression, or two-stage Hurdle classification-regression pipelines.

### D. High-Cardinality Dimensionality Reduction
* Direct one-hot encoding of 7,617 aircraft tail numbers and 7,371 checkpoints leads to extreme sparsity and overfitting.
* **Mitigation**: Tail numbers are collapsed into 40 standardized aircraft type codes and 3 broad capacity tiers (Regional, Narrowbody, Widebody), supplemented by out-of-fold target encodings.

---

## 6. Synthesis & Strategic Conclusions

The conformed v2 analytical data infrastructure provides an empirically validated, leak-free, and structurally consistent foundation for econometric forecasting and machine learning modeling. By accounting for lead-time passenger arrival curves, load factor variance, and post-COVID behavioral shifts, predictive models can accurately forecast checkpoint congestion and passenger volume flows without human query bias or structural data degradation.
