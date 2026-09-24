# Executive Summary Suite: BTS OTP vs. TSA Checkpoint Coupling
**Author**: Leila Gleich | **Institution**: Embry-Riddle Aeronautical University  
**Degree**: Master of Science in Aeronautics / Aviation Data Analytics  
**Temporal Window**: Continuous 7-Year Census (January 1, 2019 – December 31, 2025)

---

## 1. Overview
This directory contains the **curated executive summary dataset** designed to provide readers, faculty, and peer researchers with a rapid, comprehensive ("big picture") understanding of the empirical relationship between **Bureau of Transportation Statistics (BTS) On-Time Performance (OTP)** flight operations and **Transportation Security Administration (TSA)** passenger checkpoint screening throughput across the **Top 25 U.S. commercial airfields**.

---

## 2. File Inventory & Reading Guide

### File 1: [01_Executive_Top25_Airport_Coupled_Master_Census.csv](./01_Executive_Top25_Airport_Coupled_Master_Census.csv)
* **Scope**: Complete 25-airport master census (N = 25 rows).
* **Contents**: For each airport, maps scheduled flight movements, completed departures, cancellations, delay minutes, taxi-out queues, total TSA passenger throughput, daily and hourly screening volumes, DB1B connecting ratios, and calculated true local landside passenger demand.
* **Core Takeaway**: Resolves the **Connecting Ratio Paradox**—explaining why high-frequency connecting mega-hubs like Charlotte (CLT: 227k flights) process far fewer TSA passengers (28.2M) than origin-and-destination gateways like New York JFK (133k flights; 116.0M passengers) and Los Angeles (LAX: 277k flights; 129.1M passengers).

### File 2: [02_Executive_Cross_Dataset_Statistical_Relationships_and_Volatility.csv](./02_Executive_Cross_Dataset_Statistical_Relationships_and_Volatility.csv)
* **Scope**: 14 primary econometric and statistical relationships (N = 14 rows).
* **Contents**: Pearson correlation coefficients (r), variance explained (R^2), t-statistics, p-values, and explicit operational interpretations.
* **Core Takeaway**: 
  - Raw flight volume explains only 20.90% of raw checkpoint passenger throughput (r = 0.4572). Adjusting for connecting passengers via DB1B ticket surveys increases explained variance by +115% to **R^2 = 44.94%** (r = 0.6704, p < 0.001).
  - Hourly checkpoint screening volatility directly drives flight departure delay volatility (**r = +0.4375, R^2 = 19.14%, p < 0.05**), proving that security screening bottlenecks propagate into aircraft boarding and pushback instability.
  - Surface taxi-out queue duration is strongly coupled to departure delays (**r = +0.4971, R^2 = 24.71%, p < 0.001**).

### File 3: [03_Executive_Coupled_Seasonality_and_Operational_Regimes.csv](./03_Executive_Coupled_Seasonality_and_Operational_Regimes.csv)
* **Scope**: Multi-dimensional temporal synthesis (N = 28 rows).
* **Contents**: Combines four distinct temporal dimensions:
  1. **Operational Regimes**: *Off-Peak*, *Mid-Peak*, *Peak*, and *Event / Severe Shock*.
  2. **Weekly Cadence (DOW 0–6)**: Sunday leisure peak to Tuesday/Wednesday operational troughs (r = +0.9022 between TSA throughput and departure delays).
  3. **Annual Calendar Months (1–12)**: Summer congestion peaks vs. the Autumn Punctuality Decoupling (October optimal operations).
  4. **Diurnal Time-of-Day Blocks**: 5 time blocks illustrating the 90–150 minute lead-lag transfer function between screening queues and aircraft pushbacks.
* **Core Takeaway**: Quantifies the **non-linear phase transition** in airport congestion: flight operations expand by +74.5% between Off-Peak and Peak with only a 7.4-minute delay increase, but when entering an *Event* regime, flight cancellations jump 20-fold (13.75%) and departure delays triple (30.96 min).

### File 4: [04_Executive_Airport_Archetypes_Cross_Dataset_Synthesis.csv](./04_Executive_Airport_Archetypes_Cross_Dataset_Synthesis.csv)
* **Scope**: 4 operational archetypes derived from PCA and Hierarchical Clustering (N = 4 rows).
* **Contents**: Aggregated operational characteristics for:
  - **Cluster 0: Mega Connecting Hubs** (*ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO*): High volume (91.9M TSA pax; 266k flights); 56.1% connecting ratio buffering landside queues.
  - **Cluster 1: High Local Demand / O&D Focus** (*AUS, BOS, CLT, DCA, IAH, TPA*): Sharp morning/evening surges producing the highest peak-to-median surge ratio (1.82).
  - **Cluster 2: High-Reliability Fortress Hubs** (*DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC*): Punctuality leaders with lowest delays (11.56 min), lowest cancellations (1.10%), and lowest passenger volatility (CV = 0.192).
  - **Cluster 3: Congested Coastal Originators** (*EWR, JFK, LGA*): Space-constrained originators with high local originations (62.6%), chronic taxi queues (25.13 min), and highest delay volatility (CV = 1.37).

---

## 3. Related Granular Files
For complete underlying checkpoint-lane-hour, flight-level, and daily operational files, refer to:
* Data sources: 
* Domain analyses: 
* Chapter drafts: 
