<style>
body, p, table, th, td, li, h1, h2, h3, h4, h5, h6, div, span {
    font-family: "Times New Roman", Times, serif !important;
    font-size: 12pt !important;
    color: #000000 !important;
    line-height: 1.4 !important;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 14px;
    margin-bottom: 8px;
}
th {
    border-top: 1.5px solid #000000;
    border-bottom: 1px solid #000000;
    font-weight: bold;
    text-align: left;
    padding: 6px 8px;
}
td {
    padding: 6px 8px;
    vertical-align: top;
    border-top: none;
    border-bottom: none;
}
tr:last-child td {
    border-bottom: 1.5px solid #000000;
}
.table-number {
    font-weight: bold;
    margin-bottom: 2px;
}
.table-title {
    font-style: italic;
    margin-bottom: 6px;
}
.table-note {
    font-size: 12pt !important;
    margin-top: 6px;
    margin-bottom: 16px;
}
</style>

# Table 4.8: Model Development Dataset Partitions, Calibration Scale, and Leakage Prevention Architecture

**Target Location:** Chapter IV, Section 4.8, directly above or at Paragraph 112 (P110–P114 in `ChpIV v5.docx`).

<div class="table-number">Table 4.8</div>
<div class="table-title">Model Development Dataset Partitions, Calibration Scale, and Leakage Prevention Architecture</div>

| Dataset Partition Block | Chronological Window | Sample Size (Complex-Days) | Operational Purpose & Analytical Role | Leakage Prevention & Autoregressive Quarantine Controls |
| :--- | :--- | :--- | :--- | :--- |
| **Partition 1: Calibration / Training** | January 1, 2021 – September 23, 2024 | 15,976 complex-days | Primary calibration of candidate architectures (M0 Baseline Persistence, M1 Deterministic Schedule, M2 Supervised GBDT, M3 Dynamic Hybrid). Captures multi-year post-pandemic traffic recovery and seasonal demand variance. | Historical calibration baseline; strictly prospective boundary enforcement preventing future information access. |
| **Partition 2: Operational Purge Buffer** | September 24, 2024 – September 30, 2024 | 7 calendar days<br>(168 consecutive hours;<br>quarantined / deleted) | Mandatory temporal quarantine buffer. Severes 168-hour (7-day) diurnal autoregressive lags, moving averages, and rolling window lookbacks between training and validation partitions. | Complete operational purge. Zero validation or training samples drawn from this window; eliminates boundary look-ahead data leakage. |
| **Partition 3: Validation & Tuning** | October 1, 2024 – December 31, 2024 | 3,293 complex-days | Hyperparameter optimization, tree depth pruning, learning rate tuning, and calibration of the dynamic hybrid error-correction residual weights. | Temporally isolated via the 7-day purge buffer; isolated from the prospective holdout set to prevent hyperparameter overfitting. |
| **Partition 4: Prospective Out-of-Time Holdout** | January 1, 2025 – December 31, 2025 | 3,285 complex-days | Untouched benchmark for final prospective holdout evaluation. Benchmarks real-world generalization across nominal, peak, and convective weather disruption regimes. | Strictly quarantined out-of-time evaluation set. Completely withheld during all feature engineering, model training, and hyperparameter selection. |

<div class="table-note"><em>Note.</em> N = 22,554 total complex-days across the 9-airport experimental cohort. A complex-day represents one 24-hour operational monitoring cycle at a designated terminal screening complex. The 7-day operational purge buffer enforces zero autoregressive data leakage across the 168-hour weekly seasonal cycle.</div>

### Accompanying Text for Chapter IV (Insert directly after Table 4.8):

As shown in Table 4.8, models were calibrated across 15,976 training complex-days and 3,293 validation complex-days prior to holdout evaluation, separated by a 7-day operational purge buffer to ensure zero data leakage. This partitioned architecture is essential for preserving temporal causality and operational validity. Because commercial aviation demand exhibits strong diurnal and weekly cyclicality (168-hour periodicity), standard machine learning cross-validation strategies that randomly shuffle observations induce severe look-ahead data leakage. Furthermore, time-series models frequently incorporate rolling lookback windows and multi-day autoregressive lag features. Without an operational purge buffer, validation observations immediately following the training partition would pull feature values directly from the training window, artificially deflating forecast errors. Inserting an explicit seven-day temporal quarantine between calibration blocks completely severs cross-boundary autocorrelation and rolling window overlap. Consequently, the 15,976 training complex-days and 3,293 validation complex-days maintain strict temporal independence, ensuring that model performance reflects genuine prospective predictive capability rather than an artifact of information leakage.
