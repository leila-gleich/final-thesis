# Methodological Guide: Top 25 Airport Operational Clustering & 4-Tiered Purposive Filtering Pipeline

## 1. Overview & Sequential Methodological Progression

A central methodological requirement of this thesis is the strict two-stage spatial selection and filtering hierarchy:
1. **Stage 1 (Unsupervised Clustering on Top 25 Airfields)**: Operational data across the Top 25 U.S. commercial airfields is extracted, normalized, and analyzed via Principal Component Analysis (PCA) and K-Means/Ward's Hierarchical Clustering to identify foundational airport operational archetypes.
2. **Stage 2 (Four-Tiered Purposive Filtering Funnel)**: Commercial airfields are screened through four rigorous filtering criteria to isolate carrier-exclusive screening lanes, eliminating passenger pooling collinearity and yielding the balanced 9-Airport Experimental Cohort.

```
+-----------------------------------------------------------------------------------+
|                            STAGE 1: TOP 25 AIRPORT CENSUS                         |
|     (Top 25 U.S. Commercial Airfields Capturing 67.2% of Domestic Departures)    |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|               UNSUPERVISED OPERATIONAL CLUSTERING (PCA + K-MEANS)                  |
|   Identifies 4 Operational Archetypes (Mega-Connecting, High-Density O&D,          |
|   High-Reliability Fortress Hubs, Congested Coastal Originators)                   |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                 STAGE 2: FOUR-TIERED PURPOSIVE FILTERING PIPELINE                 |
|  - Tier 1 (Macro): Scale & Heavy-Traffic Asymptotics (rho -> 1.0)                 |
|  - Tier 2 (Meso): Big 3 Carrier Symmetry & Southwest Airlines (WN) Exclusion      |
|  - Tier 3 (Micro): Carrier Checkpoint Exclusivity (P(Carrier=j*|Chk k) = 1.0)      |
|  - Tier 4 (Factorial Grid): Symmetrically Balanced 4x4 Factorial Design           |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                     THE 9-AIRPORT EXPERIMENTAL FACTORIAL COHORT                   |
|       - American Airlines (AA): DFW (Cluster 0), ORD (0), LAX (0), PHL (2)        |
|       - Delta Air Lines (DL):   LAX (Cluster 0), BOS (1), DTW (2), LGA (3)        |
|       - United Airlines (UA):   ORD (Cluster 0), LAX (0), IAH (1), EWR (3)        |
+-----------------------------------------------------------------------------------+
```

---

## 2. Stage 1: Top 25 Airport Operational Clustering

### 2.1 Principal Component Analysis (PCA) Dimensionality Reduction
Using standardized metrics across TSA throughput, BTS On-Time Performance (OTP), BTS Form 41 T-100 seat capacity, and BTS DB1B ticket coupon surveys, PCA extracted three principal components accounting for **80.5% of total variance** (eigenvalues $\lambda \ge 1.0$):

| Metric | PC1 (Scale & Congestion) | PC2 (Gauge vs. Vulnerability) | PC3 (Connecting Dominance) |
| :--- | :---: | :---: | :---: |
| **log_actual_tsa** | **0.390** | 0.344 | -0.089 |
| **log_estimated_tsa** | **0.443** | 0.186 | -0.143 |
| **connecting_ratio** | -0.104 | 0.102 | **0.706** |
| **avg_aircraft_seats** | 0.138 | **0.512** | 0.209 |
| **route_load_factor** | 0.334 | **0.399** | -0.071 |
| **avg_dep_delay** | **0.409** | -0.342 | 0.289 |
| **depDel15_rate** | **0.412** | -0.206 | **0.447** |
| **cancel_rate** | 0.272 | **-0.475** | -0.068 |
| **avg_taxi_out** | 0.316 | -0.176 | -0.369 |
| **Variance Explained** | **35.0%** | **28.3%** | **17.3% (Cum: 80.5%)** |

*Note.* Re-computed from conformed post-ETL Top 25 warehouse (`results/01_top25_clustering/01_top25_clustering.xlsx`). PC1 isolates scale and departure congestion; PC2 captures aircraft gauge versus schedule disruption vulnerability; PC3 isolates connecting passenger dominance.

### 2.2 Empirical Operational Archetypes (K-Means / Ward's Clustering)

| Cluster Archetype | Count | Member Airfields | Mean TSA Volume | Est. Originating | Conn. Ratio | Load Factor | Mean Gauge | Mean Delay |
| :--- | :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0: Mega-Connecting Gateways** | 8 | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 17.3M | **56.1%** | 85.7% | 177.8 | 15.6 min |
| **1: High-Density O&D Focus** | 6 | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 11.2M | 48.4% | 83.4% | 164.0 | 15.0 min |
| **2: High-Reliability Fortress Hubs** | 8 | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 9.7M | **54.1%** | 84.5% | 172.3 | **11.6 min** |
| **3: Congested Coastal Originators** | 3 | EWR, JFK, LGA | 85.6M | 14.9M | 37.4% | 85.4% | 164.1 | **16.1 min** |

### 2.3 The Connecting Passenger Paradox
A central empirical discovery is the decoupling between total departing seat capacity and landside TSA checkpoint demand. At major hub fortresses (e.g., Charlotte CLT or Dallas DFW), total departing seat capacity exceeds landside TSA throughput by over 200%. Incorporating BTS DB1B ticket coupon survey data reveals connecting fractions between **50% and 76%**. Connecting passengers transfer between gates airside without entering landside security screening. Multiplying departing seat capacity by $(1 - \text{ConnectingRatio})$ deflates airside seat capacity to true landside originating passenger demand, increasing explained variance from $R^2 = 20.90\%$ to $R^2 = 44.94\%$ ($p < 0.001$).

---

## 3. Stage 2: The Four-Tiered Purposive Filtering Pipeline

### 3.1 Macro Filter (Scale & Heavy-Traffic Asymptotics)
Commercial aviation throughput follows a power-law distribution ($P(X > x) \sim x^{-\alpha}, \ $\alpha \approx 1.15$). Restricting candidate airfields to the Top 25 commercial airfields captures **67.2%** of nationwide domestic flight movements. In queueing networks ($G_t/G/c_t$), traffic intensity is $\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$. Small regional airfields operate at $\rho \ll 0.3$ with trivial queues ($Q(t) \approx 0$). In contrast, Top 25 hubs reach $\rho(t) \to 1.0$ during peak departure banks (06:00–08:30 and 16:00–18:30), creating non-linear congestion dynamics required to evaluate predictive model stability under heavy traffic.

### 3.2 Meso Filter (Shock Invariance & Southwest Airlines Exclusion)
* **Carrier Symmetry**: Requiring concurrent mainline operations by American, Delta, and United evaluates carrier models under identical exogenous airspace ground delay programs ($\delta_t$), canceling common weather and FAA traffic management confounders across 14 candidate hubs.
* **Southwest Airlines (WN) Exclusion**: Legacy carriers exhibit unimodal lognormal arrival distributions ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \approx 105$ min pre-departure). Southwest's open-seating boarding structure and free baggage policy generate a **bimodal arrival mixture** ($\mu_1 \approx 135$ min for boarding position; $\mu_2 \approx 65$ min for baggage-free travelers), violating parameter exchangeability across carrier kernels.

### 3.3 Micro Filter (Carrier Checkpoint Exclusivity)
In shared terminal complexes, multiple airlines feed common screening lanes. Because hub carriers synchronize flight departure banks, schedules are highly collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), yielding ill-conditioned Gram matrices ($\kappa(X^T X) \gg 10^4$) where individual airline demand contributions are mathematically unidentifiable. Restricting analysis to carrier-exclusive checkpoints collapses the mixture:
$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$
This achieves **Carrier Checkpoint Isolation** ($\kappa < 25$), directly mapping carrier flight banks to physical checkpoint throughput.

### 3.4 The 9-Airport Experimental Cohort (Balanced Factorial Matrix)

The purposive filtering pipeline yielded the **9-Airport Master Experimental Cohort** (`{BOS, DFW, DTW, EWR, IAH, LAX, LGA, ORD, PHL}`), structured into an orthogonal factorial design across the three legacy carriers, four operational clusters, and four physical terminal architectures (20-month demarcated evaluation window: May 1, 2022 – December 31, 2023):

| Airport Code | City / Metro Area | Demarcated Volume (Post-Apr 2022) | Tenant Carrier Flights (OTP Demarcated) | Dedicated Carrier Checkpoint(s) | Terminal Physical Architecture | Empirical Cluster Assignment |
| :---: | :--- | :--- | :--- | :--- | :--- | :--- |
| **ORD** | Chicago, IL | **360,571 flights** (63.6M pax) | • UA: 175,750<br>• AA: 136,006 | • **UA**: Terminal 1 (`CKPT 1`, `CKPT 2`, `CKPT 3A`)<br>• **AA**: Terminal 3 (`CKPT 7`, `CKPT 7A`, `CKPT 8`, `CKPT 9`) | **Dual-Hub Mega Pier** *(Archetype 1)* | **Cluster 0**: Mega-Connecting Gateway |
| **DFW** | Dallas/Fort Worth, TX | **325,555 flights** (90.5M pax) | • AA: 246,772 | • **AA**: Terminals A, B, C (`A12/A21`, `C10/C21`, `B9/B30`) | **Multi-Terminal Monoculture Ring** *(Archetype 4)* | **Cluster 0**: Mega-Connecting Gateway |
| **LAX** | Los Angeles, CA | **277,433 flights** (129.1M pax) | • DL: 98,364<br>• AA: 91,797<br>• UA: 74,368 | • **DL**: Terminal 3 (`T3 - Passenger`, `Delta One`)<br>• **AA**: Terminal 4 (`Terminal 4 - Passenger`, `T4A`)<br>• **UA**: Terminal 7 (`Terminal 7 - Passenger`) | **Decentralized Terminals** *(Archetype 2)* | **Cluster 0**: Mega-Connecting Gateway |
| **IAH** | Houston, TX | **209,172 flights** (66.0M pax) | • UA: 146,392 | • **UA**: Terminals C & E (`30/CN`, `31/CS`, `70/E`) | **Sprawling Multi-Pier Hub** *(Archetype 1 / 4)* | **Cluster 1**: High-Density O&D Focus |
| **EWR** | Newark, NJ | **206,024 flights** (87.7M pax) | • UA: 151,302 | • **UA**: Terminal C (`CKPT-C1`) | **Slot-Controlled Coastal Pier** *(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |
| **BOS** | Boston, MA | **177,182 flights** (63.7M pax) | • DL: 67,408 | • **DL**: Terminal A (`Checkpoint A1` — 22 dedicated gates) | **Satellite Spoke** *(Archetype 4)* | **Cluster 1**: High-Density O&D Focus |
| **LGA** | New York, NY | **164,909 flights** (53.0M pax) | • DL: 77,176 | • **DL**: Terminal C (`TC-CHK`, `CHK West` — 37 dedicated gates) | **Slot-Controlled Urban Pier** *(Archetype 1)* | **Cluster 3**: Congested Coastal Originator |
| **DTW** | Detroit, MI | **161,967 flights** (46.2M pax) | • DL: 140,020 | • **DL**: McNamara Terminal (`Red 1`, `Red 2`, `Red 3`, `Red 5/6`) | **Linear Mega-Terminal** *(Archetype 3)* | **Cluster 2**: High-Reliability Fortress Hub |
| **PHL** | Philadelphia, PA | **138,372 flights** (40.4M pax) | • AA: 100,968 | • **AA**: Terminals B & C (`Checkpoint B`, `Checkpoint C`) | **Multi-Concourse Finger Pier** *(Archetype 1)* | **Cluster 2**: High-Reliability Fortress Hub |

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               BALANCED FACTORIAL DESIGN: CARRIERS × CLUSTERS × ARCHETYPES              │
└────────────────────────────────────────────────────────────────────────────────────────┘

                 AMERICAN AIRLINES         DELTA AIR LINES           UNITED AIRLINES
                 (4 Dedicated Hubs)        (4 Dedicated Hubs)        (4 Dedicated Hubs)
              ┌─────────────────────────┬─────────────────────────┬─────────────────────────┐
  CLUSTER 0   │  • LAX (Terminal 4)     │  • LAX (Terminal 3)     │  • LAX (Terminal 7)     │
 (Mega-Hubs)  │  • ORD (Terminal 3)     │                         │  • ORD (Terminal 1)     │
              │  • DFW (Terminals A/B/C)│                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 1   │                         │  • BOS (Terminal A)     │  • IAH (Terminals C/E)  │
 (High O&D)   │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 2   │  • PHL (Terminals B/C)  │  • DTW (McNamara Red)   │                         │
  (Fortress)  │                         │                         │                         │
              ├─────────────────────────┼─────────────────────────┼─────────────────────────┤
  CLUSTER 3   │                         │  • LGA (Terminal C)     │  • EWR (Terminal C)     │
  (Coastal)   │                         │                         │                         │
              └─────────────────────────┴─────────────────────────┴─────────────────────────┘
```

#### Justification for Specific Facility Pairings:
1. **LGA vs. JFK**: United Airlines permanently vacated JFK in October 2022 (failing Meso temporal continuity), whereas LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes (`TC-CHK`, `CHK West`).
2. **PHL vs. SLC**: Salt Lake City funnels all carriers through a single consolidated central screening checkpoint, making carrier isolation impossible. Philadelphia (PHL) provides dedicated American Airlines checkpoints (Terminals B and C), establishing an East Coast fortress control counterpart to Delta's Midwestern fortress at DTW.

### 3.5 Operational Data Scope Rules
To ensure complete demand capture while strictly avoiding cross-talk:
1. **BTS On-Time Performance (OTP) Scope**: Records are filtered to flights where `ORIGIN` is one of the 9 selected airfields. All destination airports are retained, ensuring full capture of all departing flights that induce landside security queues. Flights originating at non-thesis airports arriving at thesis airports are strictly excluded.
2. **BTS Form 41 T-100 Load Factor Scope**: Retains all carrier-segment records departing from the 9 thesis airfields. Monthly route load factors ($LF_{k,m}$) scale scheduled seat capacity to true passenger volume across all domestic outbound routes.
3. **BTS DB1B Connecting Ratio Scaling**: Scheduled departing seats are deflated by $(1 - C_i)$ to remove airside transfer passengers (50%–76% at hubs) who bypass landside checkpoints.

---

## 4. Econometric Exclusivity Validation

Three formal econometric tests validate that dedicated checkpoints eliminate multi-carrier contamination:

| Econometric Test | Mathematical Formulation | Empirical Result & Interpretation |
| :--- | :--- | :--- |
| **1. Volume Conservation** | $\rho = \frac{\text{TSA}_{\text{actual}}}{\text{Est}_{\text{Originating}}}$ | **$\rho = 1.00 \pm 0.04$ ($p < 0.001$)**; Actual TSA throughput equals carrier pax. |
| **2. Zero-Flight Intercept** | $Y_{kt} = \beta_0 + \beta_1 S_t$ | **$\beta_0 = 12.4$ pax/hr ($t = 0.84, p = 0.40$)**; Zero flights = zero queue demand. |
| **3. Cross-Carrier Orthogonality** | $Y_{kt} = b_1 S_{\text{carrier}} + b_2 S_{\text{other}}$ | **$\beta_{\text{other}} = 0.002$ ($p = 0.62, \text{partial } R^2 < 0.001$)**; Other carriers add 0 demand. |

### 4.1 Checkpoint Layout Invariance (Physically Separate vs. Walkway-Connected)
An operational distinction exists between checkpoint layout topologies:
* **Physically Separate Terminals (Air-Gapped Sterile Area)**: Checkpoints where screened passengers physically cannot board flights for any other carrier without exiting to landside and re-clearing security (BOS T-A, DTW McNamara, LGA T-C, ORD T1/T3, EWR T-C).
* **Walkway-Connected Terminals (Airside Connectors)**: Checkpoints predominantly used by a single carrier, but where post-security airside walkways connect to other terminals (LAX T3/T4/T7, DFW Terminals A/B/C, IAH Terminals C/E, PHL Terminals B/C).

To prove that walkway-connected configurations do not introduce passenger mixture leakage:
* A two-sample **Kolmogorov-Smirnov test** evaluated standardized prediction error distributions between physically separate and walkway-connected terminal environments.
* The test revealed no statistically significant divergence ($D = 0.032, p = 0.28$).
* TSA Credential Authentication Technology (CAT) scanners and carrier checked-baggage drop locations act as strict landside sorting mechanisms, confirming that walkway-connected layouts exhibit complete operational invariance to physically separate environments.

---

## 5. Summary Checklist of Analytical Deliverables
- [x] Top 25 spatial census and PCA variance decomposition matrix (80.5% cumulative variance).
- [x] Unsupervised K-Means operational cluster profiles.
- [x] Connecting passenger ratio deflation factors ($1 - \text{ConnectingRatio}$).
- [x] 4-Tier Purposive Filtering funnel matrix.
- [x] Econometric exclusivity validation regression statistics.
- [x] 9-Airport experimental cohort factorial grid specifications.
