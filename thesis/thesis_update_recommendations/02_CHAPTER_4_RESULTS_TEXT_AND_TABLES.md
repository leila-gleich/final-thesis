# Chapter IV Results Update Guide: Text, Tables, and Figures

## 1. Overview & Insertion Map

This guide provides drop-in text blocks, Markdown/LaTeX tables, and figure captions for updating **Chapter IV: Results (Empirical Findings)**. 

### Suggested Chapter IV Insertion Map:
* **Section 4.3.3**: Insert *Empirical Coupled Volatility Regimes* (following Operational Clusters).
* **Table 4.3b**: Master Annual Seasonal Volatility Regimes Summary.
* **Figure 4.1**: Coupled Volatility Phase Space & Annual Seasonality.
* **Section 4.3.4**: Insert *Day-of-Week Cyclical Dynamics & Operational Archetypes*.
* **Table 4.4a**: Day-of-Week Volatility Summary.
* **Figure 4.2**: Day of Week Volatility Dynamics.
* **Section 4.3.5**: Insert *Diurnal Operational Turbulence & Dual-Peak Dynamics*.
* **Table 4.4b**: Diurnal Hourly Volatility Clusters conditioned on Day of Week.
* **Figure 4.3**: Empirical Diurnal Volatility Heatmap.
* **Table 4.4c**: Statistical Sample Size & Training Sufficiency Audit.
* **Figure 4.4**: Statistical Sample Size Sufficiency Boxplot.
* **Section 4.7 Revision**: Disaggregating Table 4.7 Benchmark Matrix across Volatility Regimes.

---

## 2. Drop-In Text: Section 4.3.3 Empirical Coupled Volatility Regimes

```markdown
### 4.3.3 Empirical Coupled Volatility Regimes (TSA Throughput vs. BTS Flight Operations)

While baseline flight movements follow published carrier schedules, security queue congestion and operational failure modes emerge from the dynamic variance mismatch between landside passenger arrivals and airside flight departures. To parameterize this operational turbulence, daily observations across the Top 25 airfields (May 1, 2022 to December 31, 2025; 1,341 calendar days) were clustered across coupled volatility dimensions: within-day TSA arrival coefficient of variation ($CV_{\text{TSA}}$), checkpoint peak-to-mean surge ratios, flight departure delay dispersion ($\sigma_{\text{Delay}}$), the Coupled Volatility Index ($CV_{\text{TSA}} \times \sigma_{\text{Delay}}$), and flight cancellation rates.

As detailed in Table 4.3b, the annual calendar separates into four distinct macroeconomic volatility regimes. Flight departure delay standard deviation ($\sigma_{\text{Delay}}$) scales monotonically from 46.09 minutes during the winter and mid-autumn lull (Off-Peak) to 68.43 minutes during the summer convective peak (a +48.5% dispersion expansion). Concurrently, the Coupled Volatility Index escalates from 27.85 to 39.36 (+41.3%), while flight cancellation rates more than triple from 0.89% to 3.16%.
```

### Table 4.3b: Master Annual Seasonal Volatility Regimes Summary (Top 25 Airfields)

```markdown
| Seasonal Regime | Operational Regime Description | Calendar Days ($N$) | Share of Days (%) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) | Cancellation Rate (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **`1_OFF_PEAK`** | Winter Lull & Mid-Autumn Shoulder | 500 | 37.3% | 1,123,386 | 0.605 | 46.09 min | **27.85** | 9.85 min | 18.00% | 0.89% |
| **`2_MID_PEAK`** | Spring Ramps & Late-Summer Shoulder | 426 | 31.8% | 1,187,095 | 0.589 | 55.06 min | **32.38** | 15.14 min | 23.23% | 1.36% |
| **`3_PEAK`** | Summer Severe Weather & Convective Surge | 224 | 16.7% | 1,305,968 | 0.576 | 68.43 min | **39.36** | 24.17 min | 31.04% | 3.16% |
| **`4_HOLIDAY`** | National Holiday Travel Corridors | 191 | 14.2% | 1,215,636 | 0.597 | 55.78 min | **33.07** | 16.51 min | 24.33% | 1.82% |
```

#### Figure 4.1 Caption & Callout:
```markdown
![Figure 4.1: Annual Seasonality & Coupled Volatility Phase Space](figures/01_annual_volatility_tsa_otp_clustering.png)

**Figure 4.1: Coupled Volatility Phase Space and Annual Monthly Volatility Dynamics.**
*(A) Scatter plot of within-day TSA arrival volatility ($CV_{\text{TSA}}$) versus flight departure delay dispersion ($\sigma_{\text{Delay}}$) across 1,341 study days, demonstrating clear separation across the four seasonal volatility regimes. (B) Monthly dual-axis profile illustrating the co-evolution of TSA arrival variance and summer convective delay spikes (June–August).*
```

---

## 3. Drop-In Text: Section 4.3.4 Day-of-Week Volatility Cycles

```markdown
### 4.3.4 Day-of-Week Cyclical Dynamics and Operational Archetypes

Weekly airline operations exhibit pronounced structural cycles governed by business versus leisure traveler distributions. Standardizing observations under ISO 8601 ($1 = \text{Monday}, \dots, 7 = \text{Sunday}$) reveals clear operational volatility archetypes across the Top 25 network (Table 4.4a):

1. **Midweek Operational Baseline (Tuesday & Wednesday)**: Tuesday and Wednesday represent the most stable operational periods of the week, characterized by the lowest departure delay dispersion ($\sigma_{\text{Delay}} = 50.09\text{ min}$ and $49.27\text{ min}$), the lowest share of delayed flights ($\approx 19.4\%\text{--}20.1\%$), and the lowest Coupled Volatility Indices ($29.99$ and $29.13$).
2. **Outbound Business Surge (Monday)**: Mondays experience the highest within-day TSA arrival volatility across the entire week ($CV = 0.604$, Coupled Volatility Index = $34.00$), driven by concentrated early-morning business traveler screening banks.
3. **Leisure Return Delay Propagation (Sunday)**: Sundays exhibit the most severe network-wide delay cascades, generating the highest mean departure delay ($17.78\text{ min}$), the highest delay dispersion ($\sigma_{\text{Delay}} = 58.07\text{ min}$), and the highest rate of flights delayed $\ge 15$ minutes ($25.60\%$).
```

### Table 4.4a: Day-of-Week Volatility Dynamics and Operational Archetypes

```markdown
| Day of Week | DOW Name | Operational Volatility Archetype | Study Days ($N$) | Mean Daily TSA (Pax) | Within-Day TSA $CV$ | Delay Dispersion ($\sigma_{\text{Delay}}$) | Coupled Volatility Index | Mean Departure Delay | Flights Delayed $\ge 15$m (%) |
| :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | Monday | Outbound Business Surge & High Screening Volatility | 192 | 1,246,150 | **0.604** | 56.56 min | **34.00** | 15.78 min | 23.54% |
| **2** | Tuesday | Midweek Operational Reset (Low Turbulence) | 192 | 1,076,625 | 0.601 | **50.09 min** | **29.99** | 11.69 min | 19.44% |
| **3** | Wednesday | Midweek Baseline Stability (Minimum Volatility) | 192 | 1,123,368 | 0.594 | **49.27 min** | **29.13** | 12.22 min | 20.05% |
| **4** | Thursday | Corporate Outbound & Early Weekend Ramp | 191 | 1,254,744 | 0.589 | 54.65 min | 31.96 | 15.39 min | 23.35% |
| **5** | Friday | Combined Business & Weekend Getaway Surge | 191 | 1,241,359 | 0.592 | 55.58 min | 32.77 | 16.61 min | 24.76% |
| **6** | Saturday | Volume Trough & Fleet Repositioning | 191 | 1,089,699 | 0.602 | 54.16 min | 32.45 | 14.64 min | 22.47% |
| **7** | Sunday | Leisure Return Peak & Evening Delay Propagation | 192 | 1,279,017 | 0.577 | **58.07 min** | **33.40** | **17.78 min** | **25.60%** |
```

#### Figure 4.2 Caption & Callout:
```markdown
![Figure 4.2: Day of Week Volatility Dynamics](figures/02_day_of_week_volatility_dynamics.png)

**Figure 4.2: Day-of-Week Volatility Dynamics and Operational Coupling.**
*(A) Mean within-day TSA arrival volatility ($CV_{\text{TSA}}$) and peak-to-mean arrival ratio. (B) Flight departure delay dispersion ($\sigma_{\text{Delay}}$) and the Coupled Volatility Index across Monday through Sunday, highlighting the contrast between the Monday business surge and the Sunday delay cascade.*
```

---

## 4. Drop-In Text: Section 4.3.5 Diurnal Operational Turbulence

```markdown
### 4.3.5 Diurnal Operational Turbulence & Non-Consecutive Dual Peaks

Rather than enforcing arbitrary, consecutive time blocks, the 24 hours of each day were clustered into exactly three regimes based on the empirical Operational Turbulence Shock Index ($T(h)$), which captures the maximum of passenger screening surge volatility and flight departure delay dispersion:

1. **`1_OFF_PEAK` (Overnight & Curfew Valley)**: Typically covering 00:00 to 03:00 (3–4 hours/day), where commercial departures are sparse and checkpoint demand is quiescent.
2. **`2_MID_PEAK` (Midday Plateau & Transition)**: Covering 08:00 to 13:00/16:00 (4–12 hours/day), characterized by steady passenger screening flow and balanced aircraft turnaround buffers.
3. **`3_PEAK` (High Queuing Turbulence / Dual Peaks)**: Uniquely groups non-consecutive turbulence periods into a single operational regime:
   * **Morning Bank Surge (05:00–08:00)**: Driven by extreme passenger arrival variance ($\sigma_{\text{TSA}} > 11,380$ pax/hr).
   * **Evening Delay Cascade (14:00/17:00–22:00)**: Driven by upstream flight delay propagation ($\sigma_{\text{Delay}} > 63.4$ min).
```

### Table 4.4b: Empirical Diurnal Hourly Regimes Conditioned on Day of Week

```markdown
| Day of Week | `1_OFF_PEAK` (Overnight Quiescence) | `2_MID_PEAK` (Midday Steady Flow & Ramp) | `3_PEAK` (Dual Non-Consecutive Turbulence Peaks) |
| :--- | :--- | :--- | :--- |
| **Monday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 08:00–13:00 (8 hrs) | **Morning:** 05:00–07:00 & **Evening:** 14:00–23:00 (13 hrs) |
| **Tuesday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 08:00–16:00, 23:00 (12 hrs) | **Morning:** 05:00–07:00 & **Evening:** 17:00–22:00 (9 hrs) |
| **Wednesday** | 00:00–03:00 (4 hrs) | 04:00, 09:00–13:00, 23:00 (7 hrs) | **Morning:** 05:00–08:00 & **Evening:** 14:00–22:00 (13 hrs) |
| **Thursday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 10:00–11:00 (4 hrs) | **Morning:** 05:00–09:00 & **Evening:** 12:00–23:00 (17 hrs) |
| **Friday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 09:00–11:00, 13:00 (6 hrs) | **Morning:** 05:00–08:00 & **Evening:** 12:00, 14:00–23:00 (15 hrs) |
| **Saturday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 08:00–13:00 (8 hrs) | **Morning:** 05:00–07:00 & **Evening:** 14:00–23:00 (13 hrs) |
| **Sunday** | 00:00, 02:00–03:00 (3 hrs) | 01:00, 04:00, 10:00–11:00 (4 hrs) | **Morning:** 05:00–09:00 & **Evening:** 12:00–23:00 (17 hrs) |
```

#### Figure 4.3 Caption & Callout:
```markdown
![Figure 4.3: Empirical Diurnal Volatility Heatmap](figures/03_diurnal_hourly_volatility_clusters_by_dow.png)

**Figure 4.3: Empirical Diurnal Volatility Heatmap (Conditioned on Day of Week).**
*Visual representation of the 168-cell matrix ($7 \times 24$) illustrating the non-consecutive dual peaks: the early-morning passenger screening surge (red, 05:00–08:00) and the afternoon/evening flight departure delay cascade (red, 14:00–22:00), separated by the midday operational plateau (green).*
```

---

## 5. Table 4.4c: Sample Size Sufficiency Audit (84 Cells)

```markdown
| Seasonal Regime | Diurnal Block | Cell Count | Min $N_{\text{train}}$ | Median $N_{\text{train}}$ | Total $N_{\text{train}}$ | Min $N_{\text{test}}$ | Median $N_{\text{test}}$ | Total $N_{\text{test}}$ | $N_{\text{train}} \ge 50$ (%) | $N_{\text{test}} \ge 30$ (%) |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Off-Peak (Winter/Fall)** | Mid-Peak Hours | 7 | 208 | 378.0 | 2,567 | 71 | 140.0 | 923 | 100% | 100% |
| **Off-Peak (Winter/Fall)** | Off-Peak Hours | 7 | 156 | 156.0 | 1,158 | 53 | 56.0 | 410 | 100% | 100% |
| **Off-Peak (Winter/Fall)** | Peak Hours | 7 | 468 | 702.0 | 5,095 | 171 | 260.0 | 1,828 | 100% | 100% |
| **Mid-Peak (Spring/Shoulder)** | Mid-Peak Hours | 7 | 168 | 328.0 | 2,089 | 72 | 136.0 | 876 | 100% | 100% |
| **Mid-Peak (Spring/Shoulder)** | Off-Peak Hours | 7 | 123 | 126.0 | 949 | 51 | 54.0 | 398 | 100% | 100% |
| **Mid-Peak (Spring/Shoulder)** | Peak Hours | 7 | 369 | 615.0 | 4,162 | 153 | 260.0 | 1,750 | 100% | 100% |
| **Peak (Summer Surge)** | Mid-Peak Hours | 7 | 95 | 168.0 | 1,175 | 32 | 56.0 | 392 | 100% | 100% |
| **Peak (Summer Surge)** | Off-Peak Hours | 7 | 71 | 72.0 | 526 | 24 | 24.0 | 176 | 100% | 85.7% |
| **Peak (Summer Surge)** | Peak Hours | 7 | 216 | 312.0 | 2,328 | 72 | 104.0 | 776 | 100% | 100% |
| **Holiday Corridors** | Mid-Peak Hours | 7 | 68 | 132.0 | 999 | 24 | 48.0 | 363 | 100% | 71.4% |
| **Holiday Corridors** | Off-Peak Hours | 7 | 48 | 66.0 | 430 | 18 | 24.0 | 158 | 85.7% | 57.1% |
| **Holiday Corridors** | Peak Hours | 7 | 156 | 286.0 | 1,928 | 65 | 104.0 | 773 | 100% | 100% |
```

#### Figure 4.4 Caption & Callout:
```markdown
![Figure 4.4: Sample Size Sufficiency Audit](figures/04_sample_sufficiency_distribution.png)

**Figure 4.4: Statistical Sample Size & Training Sufficiency Verification.**
*Log-scale distribution of training observations per cell across all 84 cross-classification cells plotted against the $N = 50$ (minimum viable) and $N = 100$ (well-powered) statistical power thresholds. 98.8% of cells meet the $N \ge 50$ threshold, confirming absence of sparse small-sample estimation bias.*
```

---

## 6. Revision Guidance for Section 4.7 (Model Benchmark Matrix)

In Section 4.7, retain the master nationwide Table 4.7, but append an explanatory paragraph and sub-table breaking down model error across the 4 Volatility Regimes:

```markdown
### 4.7.1 Model Performance Stratification Across Volatility Regimes

Evaluating model architectures across the stratified volatility regimes reveals striking performance divergences:
* **In Low-Volatility Regimes (`1_OFF_PEAK`)**: The Gradient Boosted Tweedie Regressor ($M_3$) and Sequential Hybrid ($M_5$) achieve near-identical accuracy ($\text{MASE} \approx 0.60\text{--}0.62$). In stable flow environments, complex Kalman state corrections offer marginal incremental benefit over gradient boosted decision trees.
* **In High-Volatility Regimes (`3_PEAK` Summer Severe Weather)**: The performance gap between $M_3$ and $M_5$ widens dramatically. Because extreme convective storms cause flight delays exceeding 3–5 hours, $M_3$ suffers from the "empty checkpoint fallacy," degrading to $\text{MASE} = 1.025$. In contrast, the Two-Stage Hybrid ($M_5$) dynamically incorporates prior-hour terminal congestion feedback ($t-1$), maintaining robust error bounds ($\text{MASE} = 0.737, \text{RMSE} = 1,023.2$).
```
