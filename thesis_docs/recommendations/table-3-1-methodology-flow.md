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

# Table 3.1: Sequential Four-Phase Methodology and Results Operational Architecture

**Target Location:** Chapter III, Section *Design and Procedure Phases*, directly above or replacing Figure 3 (Paragraphs 28–31 in `ChpIII v4.docx`).

<div class="table-number">Table 3.1</div>
<div class="table-title">Sequential Four-Phase Methodology and Results Operational Architecture</div>

| Phase & Title | Operational Inputs & Data Sources | Core Methodological Specifications | Empirical Outputs & Findings |
| :--- | :--- | :--- | :--- |
| **Phase 1: Ingestion & Harmonization (ETL)** | • TSA Checkpoint Passenger Records (2019–2025)<br>• BTS Form 234 On-Time Performance (13.15M flights)<br>• BTS DB1B 10% Ticket Survey<br>• FAA ASPM Environmental Data | • Multi-source relational alignment across 15-min and 60-min bins<br>• DB1B airside transfer deflation to isolate checkpoint demand<br>• Four-Tier Cohort Filtering (Macro, Meso, Micro, Factorial)<br>• Empirical fitting of ACRP Report 40 lognormal arrival profiles | • Harmonized multi-year panel dataset<br>• Balanced 9-Airport Experimental Cohort<br>• Airport-specific airside connecting transfer deflator weights |
| **Phase 2: Model Architecture & Calibration** | • Pre-processed development partition (2021–2024)<br>• Published carrier flight schedules<br>• Diurnal & seasonal cyclical indices<br>• Upstream flight delay indicators | • Calibration of four candidate architectures:<br>&nbsp;&nbsp;– Baseline Control (M0: Daily Persistence)<br>&nbsp;&nbsp;– Model 1 (M1: Deterministic ACRP 40 Schedule Base)<br>&nbsp;&nbsp;– Model 2 (M2: Supervised GBDT / LightGBM)<br>&nbsp;&nbsp;– Model 3 (M3: Dynamic Two-Stage Hybrid)<br>• 15,976 training complex-days & 3,293 validation complex-days<br>• **7-Day Operational Purge Buffer** (zero autoregressive leakage) | • Calibrated model parameter weights<br>• Optimized hyperparameter configurations<br>• Relative feature importance rankings<br>• In-sample residual error distributions |
| **Phase 3: Out-of-Time Holdout Evaluation** | • Untouched 2025 Full-Year Prospective Holdout (3,285 complex-days)<br>• Convective thunderstorm ground stops<br>• Flight bank clustering shocks | • Prospective execution across three operational regimes:<br>&nbsp;&nbsp;– Nominal Operating Conditions<br>&nbsp;&nbsp;– Routine Seasonal Peak Regimes<br>&nbsp;&nbsp;– Acute Irregular Disruption Shocks<br>• Benchmarking across the Evaluation Triad:<br>&nbsp;&nbsp;1. Nominal Accuracy (R2, RMSE, MAE)<br>&nbsp;&nbsp;2. Disruption Resilience (MASE, Peak Error)<br>&nbsp;&nbsp;3. Zero-Shot Generalizability (Spatial Portability) | • Prospective diurnal volatility forecasts (σTSA, hr)<br>• Scale-free relative volatility forecasts (CVTSA, hr)<br>• Quantified operational error metrics<br>• Cross-regime performance scorecards |
| **Phase 4: Comparative Synthesis & Findings** | • Prospective holdout forecast errors<br>• Checkpoint lane physical constraints<br>• TSA screening staffing cost matrices | • Pairwise Diebold-Mariano statistical superiority testing<br>• Evaluation of the Values versus Volatility paradigm<br>• Translation of predicted volatility into dynamic safety buffers<br>• Factorial cross-facility generalizability audit | • Empirical findings for Chapter IV<br>• Cross-airport generalizability matrix<br>• Tactical Checkpoint Staffing Playbook<br>• Recommendations for Airport Operations Centers |

<div class="table-note"><em>Note.</em> This sequential architecture operationalizes the research methodology from raw federal data ingestion to Chapter IV empirical synthesis. The 7-day operational purge buffer between Phases 2 and 3 guarantees strict temporal independence and zero data leakage. All candidate models are prospectively benchmarked against the untouched 2025 full-year holdout partition.</div>
