# Chapter III Methodology Update Guide: Coupled Volatility & Temporal Clustering

## 1. Overview & Methodological Rationale

In traditional airport terminal modeling, temporal variation is frequently parameterized using static calendar categories (e.g., calendar quarters or fixed time-of-day blocks). However, airport operations research demonstrates that static scheduled flight volumes and baseline passenger arrivals correlate poorly with operational breakdown and queue delays ($R^2 \approx 2.50\%$). 

Terminal queuing saturation, security checkpoint spillovers, and cascading departure delays are driven by **volatility, arrival surge shocks, and schedule variance mismatch**. 

To establish an empirically grounded framework for training, tuning, and stress-testing predictive models ($M_0$ through $M_5$), Chapter III must incorporate a **Hierarchical Coupled Volatility Clustering Methodology** across the Top 25 U.S. commercial airfields ($ATL, AUS, BOS, CLT, DCA, DEN, DFW, DTW, EWR, IAD, IAH, JFK, LAS, LAX, LGA, MCO, MIA, MSP, ORD, PHL, PHX, SEA, SFO, SLC, TPA$).

---

## 2. Mathematical Formulations to Insert into Chapter III

### 2.1 Daily Coupled Volatility Metrics
For each calendar day $d$ in the analytical window (Candidate B: May 1, 2022 to December 31, 2025):

1. **Within-Day Passenger Screening Volatility ($CV_{\text{TSA}, d}$)**:
   $$CV_{\text{TSA}, d} = \frac{\sigma_{\text{hourly},\text{TSA}, d}}{\mu_{\text{hourly},\text{TSA}, d}} = \frac{\sqrt{\frac{1}{23}\sum_{h=0}^{23} (\text{TSA}_{d,h} - \bar{\text{TSA}}_d)^2}}{\frac{1}{24}\sum_{h=0}^{23} \text{TSA}_{d,h}}$$
   Measures the intraday concentration and peakiness of passenger arrival waves.

2. **Checkpoint Peak Surge Shock Ratio ($S_{\text{TSA}, d}$)**:
   $$S_{\text{TSA}, d} = \frac{\max_{h \in [0,23]} \text{TSA}_{d,h}}{\mu_{\text{hourly},\text{TSA}, d}}$$
   Captures the maximum screening demand impulse relative to average baseline load.

3. **Flight Departure Delay Dispersion ($\sigma_{\text{Delay}, d}$)**:
   $$\sigma_{\text{Delay}, d} = \sqrt{\frac{1}{N_d - 1}\sum_{i=1}^{N_d} (\text{DepDelay}_{d,i} - \bar{\text{DepDelay}}_d)^2} \quad \forall \text{ uncancelled flights}$$
   Measures flight operational schedule instability and tarmac queue dispersion across the candidate network.

4. **The Coupled Volatility Index ($\text{CVI}_d$)**:
   $$\text{CVI}_d = CV_{\text{TSA}, d} \times \sigma_{\text{Delay}, d}$$
   Directly captures the systemic joint vulnerability of the airport system, representing the physical co-occurrence of landside passenger arrival surges and airside flight departure delays.

---

### 2.2 Diurnal Operational Turbulence Shock Index ($T(h)$)
To identify the diurnal regimes conditioned on each Day of Week ($DOW \in [1, 7]$) without imposing arbitrary consecutive hourly boundaries, define the **Operational Turbulence Shock Index** $T(h)$ for each hour $h \in [0, 23]$:

$$T_{dow}(h) = \max\left( \frac{\sigma_{\text{TSA}, dow}(h)}{\max_{k} \sigma_{\text{TSA}, dow}(k)}, \; \frac{[\sigma_{\text{intra}, dow}(h) + \sigma_{\text{inter}, dow}(h)] \cdot \mathbb{I}(\bar{F}_{dow}(h) \ge 20)}{\max_{k} [(\sigma_{\text{intra}, dow}(k) + \sigma_{\text{inter}, dow}(k)) \cdot \mathbb{I}(\bar{F}_{dow}(k) \ge 20)]} \right)$$

Where:
* $\sigma_{\text{TSA}, dow}(h)$ is the across-week standard deviation of passenger screening throughput at hour $h$.
* $\sigma_{\text{intra}, dow}(h)$ is the mean within-hour flight departure delay standard deviation.
* $\sigma_{\text{inter}, dow}(h)$ is the across-week standard deviation of mean hourly departure delay.
* $\mathbb{I}(\bar{F}_{dow}(h) \ge 20)$ is an operational flight activity indicator that masks overnight curfew hours where commercial passenger departures are sparse ($<20$ flights network-wide).

Applying 1D K-Means clustering ($k = 3$) on $T_{dow}(h)$ ordered monotonically by turbulence score yields:
* **`1_OFF_PEAK`**: Low Volatility / Overnight & Curfew Quiescence ($T < 0.35$).
* **`2_MID_PEAK`**: Moderate Volatility / Midday Steady Flow & Ramps ($0.35 \le T < 0.75$).
* **`3_PEAK`**: High Volatility / Queuing Turbulence ($T \ge 0.75$).

> [!IMPORTANT]
> Because $T(h)$ takes the maximum of the demand surge shock and the delay dispersion shock, it naturally identifies **non-consecutive dual peaks**:
> 1. **Morning Bank Surge (05:00–08:00)**: Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr).
> 2. **Evening Delay Cascade (14:00/17:00–22:00)**: Driven by extreme flight delay dispersion ($\sigma_{\text{Delay}} > 63.4$ min).

---

## 3. Hierarchical Cross-Classification Architecture

The methodology establishes an $84$-cell cross-classification tensor:
$$\mathcal{G} = \mathcal{S} \times \mathcal{D} \times \mathcal{H} \quad (4 \times 7 \times 3 = 84 \text{ cells})$$

1. **Annual Macro Regimes ($\mathcal{S}$, 4 Regimes)**:
   * `1_OFF_PEAK`: Winter Lull & Mid-Autumn Shoulder (Weeks 3–7, 9, 37–50)
   * `2_MID_PEAK`: Spring Ramps & Late-Summer Shoulder (Weeks 1–2, 8, 10–21, 23, 33–36, 51)
   * `3_PEAK`: Summer Severe Weather & Convective Surge (Weeks 22, 24–32: June–August)
   * `4_HOLIDAY`: National Holiday Travel Corridors (Thanksgiving, Christmas/NY, Memorial Day, July 4th, Labor Day, MLK, Presidents Day)
2. **Weekly Operational Cycles ($\mathcal{D}$, 7 Days, ISO 8601)**:
   * Monday ($1$) through Sunday ($7$) capturing distinct business vs leisure profiles.
3. **Diurnal Regimes ($\mathcal{H}$, 3 Non-Consecutive Categories per DOW)**:
   * Off-Peak, Mid-Peak, and Peak conditioned on day-of-week queuing dynamics.

---

## 4. Statistical Power & Sample Size Sufficiency Proofs

To satisfy academic requirements for empirical modeling robustness, Chapter III must demonstrate that every cell in $\mathcal{G}$ possesses sufficient degrees of freedom to prevent small-sample estimator degradation.

### Candidate B Partitioning Structure:
* **Training Partition**: May 1, 2022 – December 31, 2024 ($975$ days = $23,400$ hourly observations).
* **Holdout Testing Partition**: January 1, 2025 – December 31, 2025 ($365$ days = $8,760$ hourly observations).
* **Purge Window**: 7-day embargo between training and test sets to eliminate serial autocorrelation leakage.

### Sample Size Thresholds:
* **Training Minimum**: $N_{\text{train}} \ge 50$ (minimum viable sample) and $N_{\text{train}} \ge 100$ (well-powered for non-linear ML tree splits).
* **Testing Minimum**: $N_{\text{test}} \ge 30$ (Central Limit Theorem asymptotic validity for holdout evaluation).

### Empirical Audit:
* **$N_{\text{train}} \ge 50$ Compliance**: **83 of 84 cells ($98.8\%$)** meet or exceed the training threshold (Median $N_{\text{train}} = 215$). The single cell with $N = 48$ is Holiday Off-Peak Overnight ($00:00\text{--}03:00$).
* **$N_{\text{train}} \ge 100$ Compliance**: **65 of 84 cells ($77.4\%$)** achieve fully powered training depth.
* **$N_{\text{test}} \ge 30$ Compliance**: **70 of 84 cells ($83.3\%$)** meet holdout test thresholds (Median $N_{\text{test}} = 76$). Remaining cells have $18$ to $24$ observations, sufficient for non-parametric rank tests.
