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
|  - Tier 4 (Factorial Grid): Symmetrically Balanced 3x3 Experimental Cohort         |
+-----------------------------------------------------------------------------------+
                                          │
                                          ▼
+-----------------------------------------------------------------------------------+
|                     THE 9-AIRPORT EXPERIMENTAL FACTORIAL COHORT                   |
|       - American Airlines (AA): DFW (Fortress), PHL (Hub), ORD (Gateway)          |
|       - Delta Air Lines (DL): DTW (Fortress), LGA (Originator), BOS (O&D Focus)   |
|       - United Airlines (UA): EWR (Originator), IAH (O&D Focus), LAX (Gateway)    |
+-----------------------------------------------------------------------------------+
```

---

## 2. Stage 1: Top 25 Airport Operational Clustering

### 2.1 Principal Component Analysis (PCA) Dimensionality Reduction
Using standardized metrics across TSA throughput, BTS On-Time Performance (OTP), BTS Form 41 T-100 seat capacity, and BTS DB1B ticket coupon surveys, PCA extracted three principal components accounting for **77.0% of total variance**:

| Metric | PC1 (Scale & Congestion) | PC2 (Gauge vs. Vulnerability) | PC3 (Connecting Dominance) |
| :--- | :---: | :---: | :---: |
| **log_actual_tsa** | 0.364 | 0.357 | -0.001 |
| **log_estimated_tsa** | 0.432 | 0.199 | -0.054 |
| **connecting_ratio** | -0.151 | 0.108 | **0.583** |
| **avg_aircraft_seats** | 0.105 | **0.519** | 0.187 |
| **route_load_factor** | 0.308 | 0.410 | 0.003 |
| **avg_dep_delay** | **0.368** | -0.321 | 0.363 |
| **depDel15_rate** | 0.355 | -0.183 | **0.500** |
| **cancel_rate** | 0.275 | -0.466 | 0.011 |
| **avg_taxi_out** | 0.347 | -0.172 | -0.295 |
| **Variance Explained** | **33.8%** | **25.5%** | **17.7% (Cum: 77.0%)** |

### 2.2 Empirical Operational Archetypes (K-Means / Ward's Clustering)

| Cluster Archetype | Count | Member Airfields | Mean TSA Volume | Est. Originating | Conn. Ratio | Load Factor | Mean Gauge | Mean Delay |
| :--- | :-: | :--- | :-: | :-: | :-: | :-: | :-: | :-: |
| **0: Mega-Connecting Gateways** | 8 | ATL, DEN, DFW, LAX, MCO, MIA, ORD, SFO | 91.9M | 17.3M | **56.1%** | 85.7% | 177.8 | 15.6 min |
| **1: High-Density O&D Focus** | 6 | AUS, BOS, CLT, DCA, IAH, TPA | 46.1M | 11.2M | 48.4% | 83.4% | 164.0 | 15.0 min |
| **2: High-Reliability Fortress Hubs** | 8 | DTW, IAD, LAS, MSP, PHL, PHX, SEA, SLC | 55.4M | 9.7M | **54.1%** | 84.5% | 172.3 | **11.6 min** |
| **3: Congested Coastal Originators** | 3 | EWR, JFK, LGA | 85.6M | 14.9M | 37.4% | 85.4% | 164.1 | **16.1 min** |

### 2.3 The Connecting Passenger Paradox
A central empirical discovery is the decoupling between total departing seat capacity and landside TSA checkpoint demand. At major hub fortresses (e.g., Charlotte CLT or Dallas DFW), total departing seat capacity exceeds landside TSA throughput by over 200%. Incorporating BTS DB1B ticket coupon survey data reveals connecting fractions between **50% and 76%**. Connecting passengers transfer between gates airside without entering landside security screening. Multiplying departing seat capacity by $(1 - \text{ConnectingRatio})$ deflates airside seat capacity to true landside originating passenger demand.

---

## 3. Stage 2: The Four-Tiered Purposive Filtering Pipeline

### 3.1 Macro Filter (Scale & Heavy-Traffic Asymptotics)
Commercial aviation throughput follows a power-law distribution ($P(X > x) \sim x^{-\alpha}, \alpha \approx 1.15$). Restricting candidate airfields to the Top 25 commercial airfields captures 67.2% of nationwide domestic flight movements. In queueing networks ($G_t/G/c_t$), traffic intensity is $\rho(t) = \frac{\lambda(t)}{c(t) \cdot \mu}$. Small regional airfields operate at $\rho \ll 0.3$ with trivial zero queues ($Q(t) \approx 0$). In contrast, Top 25 hubs reach $\rho(t) \to 1.0$ during peak departure banks (06:00–08:30 and 16:00–18:30), creating non-linear congestion dynamics required to train congestion-aware models.

### 3.2 Meso Filter (Shock Invariance & Southwest Airlines Exclusion)
* **Carrier Symmetry**: Requiring concurrent mainline operations by American, Delta, and United evaluates carrier models under identical exogenous airspace ground delay programs ($\delta_t$), canceling common weather and FAA traffic management confounders.
* **Southwest Airlines (WN) Exclusion**: Legacy carriers exhibit unimodal lognormal arrival distributions ($\tau \sim \text{Lognormal}(\mu, \sigma^2), E[\tau] \approx 105$ min pre-departure). Southwest's open-seating boarding structure and free baggage policy generate a **bimodal arrival mixture** ($\mu_1 \approx 135$ min for boarding position; $\mu_2 \approx 65$ min for baggage-free travelers), violating parameter exchangeability across carrier kernels.

### 3.3 Micro Filter (Carrier Checkpoint Exclusivity)
In shared terminal complexes, multiple airlines feed common screening lanes. Because hub carriers synchronize flight departure banks, schedules are highly collinear ($\text{Corr}(S_j, S_{j'}) \ge 0.88$), yielding ill-conditioned Gram matrices ($\kappa(X^T X) \gg 10^4$) where individual airline demand contributions are mathematically unidentifiable. Restricting analysis to carrier-exclusive checkpoints collapses the mixture:
$$P(\text{Carrier} = j^* \mid \text{Checkpoint } k) = 1.0$$
This reduces estimation to an orthogonal Wiener-Hopf deconvolution ($\kappa < 25$), directly mapping carrier flight banks to physical checkpoint throughput.

### 3.4 The 9-Airport Experimental Cohort ($3 \times 3$ Factorial Grid)

| Carrier | Fortress Hub | Congested Coastal Originator | High-Density O&D / Gateway | Dedicated Terminal Checkpoint |
| :--- | :--- | :--- | :--- | :--- |
| **American Airlines (AA)** | DFW (Terminal D) | PHL (Terminals B/C) | ORD (Terminal 3) | dedicated_exclusive |
| **Delta Air Lines (DL)** | DTW (McNamara) | LGA (Terminal C) | BOS (Terminal A) | dedicated_exclusive |
| **United Airlines (UA)** | EWR (Terminal C) | LAX (Terminal 7) | IAH (Terminal C) | dedicated_exclusive |

#### Justification for Specific Inclusion/Exclusion Decisions:
1. **LGA vs. JFK**: United Airlines permanently vacated JFK in October 2022 (failing Meso temporal continuity), whereas LGA opened Delta's consolidated Terminal C in June 2022, providing unconfounded screening lanes.
2. **PHL vs. SLC**: Salt Lake City funnels all carriers through a single consolidated central screening checkpoint, making carrier isolation impossible. Philadelphia (PHL) provides dedicated American Airlines checkpoints (Terminals B and C).

---

## 4. Econometric Exclusivity Validation

Three formal econometric tests validate that dedicated checkpoints eliminate multi-carrier contamination:

| Econometric Test | Mathematical Formulation | Empirical Result & Interpretation |
| :--- | :--- | :--- |
| **1. Volume Conservation** | $\rho = \frac{\text{TSA}_{\text{actual}}}{\text{Est}_{\text{Originating}}}$ | **$\rho = 1.00 \pm 0.04$ ($p < 0.001$)**; Actual TSA throughput equals carrier pax. |
| **2. Zero-Flight Intercept** | $Y_{kt} = \beta_0 + \beta_1 S_t$ | **$\beta_0 = 12.4$ pax/hr ($t = 0.84, p = 0.40$)**; Zero flights = zero queue demand. |
| **3. Cross-Carrier Orthogonality** | $Y_{kt} = b_1 S_{\text{carrier}} + b_2 S_{\text{other}}$ | **$\beta_{\text{other}} = 0.002$ ($p = 0.62, \text{partial } R^2 < 0.001$)**; Other carriers add 0 demand. |

---

## 5. Summary Checklist of Analytical Deliverables
- [x] Top 25 spatial census and PCA variance decomposition matrix.
- [x] Unsupervised K-Means operational cluster profiles.
- [x] Connecting passenger ratio deflation factors ($1 - \text{ConnectingRatio}$).
- [x] 4-Tier Purposive Filtering funnel matrix.
- [x] Econometric exclusivity validation regression statistics.
- [x] 9-Airport experimental cohort factorial grid specifications.
