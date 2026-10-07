# Results Figures Directory
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Directory Purpose**: This directory houses the publication-ready empirical figures and visualization outputs generated across the research pipeline for Chapter IV (*Results & Findings*) and Chapter V (*Discussion & Conclusions*). All empirical visualizations focus strictly on passenger screening throughput volatility ($\sigma_{\text{TSA}}$ and $CV_{\text{TSA}}$) rather than raw passenger volume, grounded in heavy-traffic queuing principles.

---

## 1. Inventory of Empirical Figures

| Figure ID | Canonical Filename | Source / Generation Script | Manuscript Target & Location | Description & Theoretical Rationale |
| :--- | :--- | :--- | :--- | :--- |
| **Figure 4.2** | `figure_4_2_annual_volatility_clusters.png` (also `01_annual_volatility_tsa_otp_clustering.png`) | `src/analysis/season_analysis_volatility_runner.py` | `chp4-results.md` (Following Table 4.3b) | **Annual Volatility Dynamics & Coupled Volatility Clusters**: Demonstrates network-level annual volatility regimes across the Top 25 airfields, showing the positive coupling between flight delay dispersion and checkpoint arrival volatility ($CVI = \sigma_{\text{TSA}} \cdot \sigma_{\text{Delay}}$). |
| **Figure 4.3** | `figure_4_3_day_of_week_volatility_dynamics.png` (also `02_day_of_week_volatility_dynamics.png`) | `src/analysis/season_analysis_volatility_runner.py` | `chp4-results.md` (Following Table 4.4a) | **Day-of-Week Volatility Dynamics Across the National Network**: Illustrates day-of-week arrival burstiness ($CV_{\text{TSA}}$) across corporate-heavy (Mon/Thu/Fri peaks) vs. leisure-heavy (Sun/Fri peaks) commercial airfields. |
| **Figure 4.4** | `figure_4_4_diurnal_hourly_volatility_clusters.png` (also `03_diurnal_hourly_volatility_clusters_by_dow.png`) | `src/analysis/season_analysis_volatility_runner.py` | `chp4-results.md` (Under TSA & OTP Throughput Data) | **Intraday Diurnal Hourly Volatility Clusters (Bimodal Peaks by DOW)**: Resolves 24-hour diurnal passenger arrival profiles, highlighting morning (05:00–08:00) and afternoon/evening (16:00–19:00) peak shock windows. |
| **Figure 4.5** | `figure_4_5_lead_lag_convolution_curves.png` (also `physical transfer lead lag time.png`) | `src/features/lead_lag_convolution.py` | `chp4-results.md` (Directly following Table 4.9) | **Empirical Lead-Lag Passenger Show-Up Curve Convolution**: Depicts the temporal asynchrony between scheduled departure flight banks and landside checkpoint arrivals, highlighting the modal 90–120 minute show-up window ($t+1, t+2$). |
| **Diagnostic** | `figure_sample_sufficiency_distribution.png` (also `04_sample_sufficiency_distribution.png`) | `src/etl/perform_top9_analysis.py` | `chp4-results.md` / Appendix | **Sample Sufficiency Distribution**: Validates statistical sample size and temporal coverage across the post-pandemic demarcation window (May 1, 2022 to December 31, 2025; $N = 3,222$ holdout complex-days). |

---

## 2. Theoretical Queuing Framework

All empirical figures in this directory are grounded in **Kingman's Heavy-Traffic Queuing Formula**:

$$W_q \approx \left(\frac{\rho}{1-\rho}\right) \left(\frac{C_a^2 + C_s^2}{2}\right) \left(\frac{1}{\mu}\right)$$

Where:
* $W_q$: Expected passenger queue waiting time.
* $\rho = \frac{\lambda}{\mu}$: Checkpoint server utilization (approaching $1.0$ during peak flight banks).
* $C_a^2$: Squared coefficient of variation of passenger arrival intervals (intraday burstiness $CV_{\text{TSA}}^2$).
* $C_s^2$: Squared coefficient of variation of screening inspection service times.
* $\mu$: Mean screening processing rate per physical lane.

Because queue wait times escalate non-linearly with arrival volatility ($C_a^2$) as utilization $\rho \to 1.0$, accurately modeling arrival volatility is the vital operational imperative for airport Joint Operations Centers (JOCs) and TSA Federal Security Directors.

---

## 3. Provenance & Synchronization

* **Image Format**: PNG (300 DPI publication resolution).
* **Companion Tabular Data**: Conformed CSV files in [`results/tables/`](../tables/) and multi-tab Excel workbooks in [`results/`](../).
* **Manuscript Markdown Callouts**: Referenced in [`thesis_docs/manuscripts/chp4-results.md`](../../thesis_docs/manuscripts/chp4-results.md).
