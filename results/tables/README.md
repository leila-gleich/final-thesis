# Master Model Evaluation Metrics & Results Tables Directory

This directory contains conformed empirical evaluation benchmarks comparing the four canonical modeling paradigms for **TSA Throughput Volatility Forecasting** across the **2025 Out-of-Time Holdout Dataset** (3,222 holdout airport-days; 72,053 hourly complex screening observations) and the **Three Core Evaluation Dimensions**:
1. **Robustness** (Lowest RMSE under Routine Conditions; $\text{MASE}_{\text{routine}} < 0.700$)
2. **Resilience** (Recovery RMSE Multiplier $R_{\text{RMSE}} \approx 1.00$; Lowest $\text{MASE}_{\text{shock}}$; $\text{TTR} < 4.0\text{h}$)
3. **Generalizability** (Zero-Shot Spatial Transfer: $\text{RTR} = 1.00$; $\Delta\text{MASE}_{\text{transfer}} \le 10.0\%$)

Additionally, this directory contains standalone operational decision matrices:
* [`master_asymmetric_trade_off_matrix.csv`](./master_asymmetric_trade_off_matrix.csv): Master Asymmetric Trade-Off Matrix benchmarking canonical models against stated academic targets.
* [`dual_track_model_selection_policy.csv`](./dual_track_model_selection_policy.csv): Gated operational deployment rules for Gate 1 (Routine Flow Track $\to M_3$) and Gate 2 (Tactical Shock Track $\to M_5$).

For the dedicated catalog of all 16 manuscript tables with documentation and short links, see [`results/manuscript_tables/`](../manuscript_tables/README.md).

---

## Automated Synchronization with Analysis Changes

> [!IMPORTANT]
> **To ensure all CSV tables and Excel workbooks stay synchronized whenever changes occur in the analysis, ETL pipelines, or model evaluation:**
> 
> Execute the synchronization runner:
> ```bash
> python src/analysis/sync_manuscript_tables.py
> ```
> Or execute the end-to-end master pipeline:
> ```bash
> python run_pipeline.py
> ```
> 
> This process automatically:
> 1. Extracts all 16 empirical tables directly from the manuscript chapters (`thesis_docs/manuscripts/chp4-results.md` and `thesis_docs/manuscripts/chp5-discussion.md`).
> 2. Cleans mathematical notations, LaTeX formatting, and special characters into standard, publication-grade CSVs in `results/manuscript_tables/` and `results/tables/`.
> 3. Synchronizes the multi-tab companion Excel workbooks (`04_model_execution_2025_holdout.xlsx`, `03_lead_lag_deconvolution.xlsx`, `05_robustness_resilience_generalizability.xlsx`, `02_top9_cohort_comprehensive_analysis.xlsx`, etc.).
> 4. Validates column/row alignment with zero manual data entry errors.

---

## File Index

* **Master Evaluation Matrix CSV**: [`master_model_evaluation_metrics_and_targets.csv`](./master_model_evaluation_metrics_and_targets.csv)
  * Comprehensive tabular CSV containing 16 performance metrics, formulas, targets, empirical holdout scores for $M_0$, $M_1^*$, $M_3$, and $M_5$, dimension winners, and operational significance.
* **Summary Evaluation CSV**: [`model_evaluation_metrics_summary.csv`](./model_evaluation_metrics_summary.csv)
  * Summary evaluation matrix across the three evaluation dimensions.
* **Master Asymmetric Trade-Off Matrix CSV**: [`master_asymmetric_trade_off_matrix.csv`](./master_asymmetric_trade_off_matrix.csv)
  * Formal empirical proof of Hypothesis 1 demonstrating that no single paradigm dominates across all three dimensions.
* **Dual-Track Policy CSV**: [`dual_track_model_selection_policy.csv`](./dual_track_model_selection_policy.csv)
  * Operational deployment policy mapping operational turbulence regimes ($T(h) < 0.75$ vs. $T(h) \ge 0.75$) to candidate model architectures.
* **Dedicated Manuscript Tables Directory**: [`results/manuscript_tables/`](../manuscript_tables/README.md)
  * Complete suite of all 16 manuscript tables (Table 4.1 through Table 5.4) available as canonical CSVs and convenience links (`table_4_1.csv`, etc.).

---

## Master Evaluation Table Summary (Throughput Volatility Forecasting)

| Evaluation Dimension | Performance Metric | Academic Stated Target | Baseline Control ($M_0$: Diurnal Persistence) | Deterministic Baseline ($M_1^*$: Schedule Bank Baseline) | Probabilistic ML ($M_3$: Supervised GBR) | Dynamic Hybrid ($M_5$: SARIMA-Tree) | Operational Interpretation & Hypothesis Finding |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :--- |
| **Overall 2025 Fit** | **Test $R^2$** | $> 0.600$ | 0.6719 | 0.4980 | 0.6178 | **0.7483 (CHAMPION)** | $M_5$ captures 74.8% of all throughput volatility variance on unobserved 2025 data. |
| **Overall 2025 Fit** | **Test RMSE** | $< 300$ pax/hr | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | **222.1 pax/hr (LOWEST)** | $M_5$ slashes large prediction errors by 91.3 pax/hr compared to $M_1^*$. |
| **Overall 2025 Fit** | **Test MAE** | $< 200$ pax/hr | 179.3 pax/hr | 215.9 pax/hr | 178.0 pax/hr | **142.8 pax/hr (LOWEST)** | $M_5$ achieves exceptional precision with MAE of 142.8 pax/hr across dedicated complexes. |
| **Overall 2025 Fit** | **Test MASE** | $< 0.700$ | 1.000 | 0.945 | 0.779 | **0.662 (CHAMPION)** | $M_5$ achieves the stretch target, delivering 33.8% error reduction over daily persistence. |
| **Overall 2025 Fit** | **Mean Bias** | $\approx 0$ pax/hr | -0.7 pax/hr | -42.1 pax/hr | -18.4 pax/hr | **-8.5 pax/hr** | $M_5$ exhibits negligible bias of -8.5 pax/hr during peak arrival waves. |
| **Robustness** | **$\text{RMSE}_{\text{routine}}$** | Lowest Routine RMSE | 253.6 pax/hr | 313.4 pax/hr | 273.5 pax/hr | **222.1 pax/hr (LOWEST)** | $M_5$ lowest RMSE; $M_3$ wins Routine Pareto Efficiency (low-compute, zero online feedback). |
| **Robustness** | **$\text{MASE}_{\text{routine}}$** | $\text{MASE} < 0.700$ | 1.000 | 0.945 | **0.680–0.700 (MET)** | **0.662 (MET)** | Confirms H1(a): Both $M_3$ and $M_5$ meet target under nominal operations (Delays $< 15$m). |
| **Robustness** | **Diebold-Mariano Stat** | $p < 0.001$ | Reference | Control Baseline | $DM = 42.15$ ($p < 0.0001$) | **$DM = 48.72$ ($p < 0.0001$)** | Statistically proves that ML and Hybrid improvements over $M_1^*$ are mathematically genuine. |
| **Resilience** | **$\text{RMSE}_{\text{shock}}$** | Lowest Shock RMSE | 398.2 pax/hr | 412.8 pax/hr | 318.4 pax/hr | **254.2 pax/hr (LOWEST)** | $M_5$ maintains tight error bounds during severe weather storms and airport ground stops. |
| **Resilience** | **$\text{MASE}_{\text{shock}}$** | Lowest Shock MASE | 1.000 | 1.082 | 0.812 | **0.694 (LOWEST)** | $M_5$ performs 30.6% better than naive guessing during disruptions. |
| **Resilience** | **Resilience Multiplier ($R_{\text{MASE}}$)** | $R \approx 1.00$ | 1.00 (Static) | 1.32 (Blind) | 2.14 (Fragile) | **1.05 (MET / WINNER)** | **$M_5$ DECISIVE WINNER**: Recursive feedback ($e_{t-1}$) prevents empty-checkpoint collapse. |
| **Resilience** | **Time-to-Recovery ($\text{TTR}$)** | $\text{TTR} < 4.0$ hrs | 8.4 hrs | 7.8 hrs | 5.4 hrs | **2.8 hrs (MET / WINNER)** | $M_5$ returns to normal error bounds 5.0 hrs faster than $M_1^*$ and 2.6 hrs faster than $M_3$. |
| **Generalizability** | **Zero-Shot $\text{RMSE}_{\text{transfer}}$** | Minimize Transfer RMSE | 253.6 pax/hr | 326.5 pax/hr | 295.1 pax/hr | 264.3 pax/hr | Prediction error deploying model zero-shot from EWR to LGA without local retraining. |
| **Generalizability** | **Relative Transfer Ratio ($\text{RTR}$)** | $\text{RTR} = 1.00$ | 1.00 | **1.04 (MET / WINNER)** | 1.08 (Passes) | **1.19 (FAILS TARGET)** | **$M_1^*$ DECISIVE WINNER**: Invariant schedule rules generalize; $M_5$ overfits to local gate geometry. |
| **Generalizability** | **Transfer Degradation ($\Delta_{\text{transfer}}\%$)** | $\le 10.0\%$ | 0.0% | **+4.2% (MINIMAL)** | +7.9% (LOW) | +19.0% (ELEVATED) | Physical rules lose only 4.2% accuracy; hybrid decision trees lose 19.0%. |
| **Generalizability** | **$\Delta\text{MASE}_{\text{transfer}}$** | $\Delta\text{MASE} \le 10.0\%$ | 0.0% | **+4.0% (MET / WINNER)** | +8.3% (Passes) | **+21.5% (FAILS TARGET)** | **$M_1^*$ passes target (+4.0% shift)**; $M_5$ fails target (+21.5% shift) due to local tree overfitting. |
