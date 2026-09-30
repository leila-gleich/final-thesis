# STATUS: IMPLEMENTED

# Recommendation REC-11: Multi-Pillar Quantitative Evaluation Framework

**Recommendation ID**: REC-11  
**Target Module**: `src/models/eval_pillars.py`  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Evaluating forecasting performance purely through global RMSE or MAE fails to capture off-peak stochasticity, worst-case shock vulnerability during severe weather disruptions, or spatial transfer penalties across airports.

A comprehensive 14-metric evaluation suite structured across three core operational pillars must be implemented.

---

## 2. Technical Specification

### 2.1 Pillar 1: Robustness (Routine Steady-State Accuracy)
- Validation RMSE & MAE
- Error Stability ($\sigma_{\text{RMSE}} = \text{std}(\text{RMSE}_{\text{day}} \le 90)$)
- Segment Consistency ($\sigma_{\text{segments}}$ across Slow, Avg, Mid-Peak, Peak demand tiers)
- Off-Peak Relative Stochasticity ($\text{CV}_{\text{off-peak}} = \frac{\text{RMSE}_{\text{Slow}}}{\mu_{\text{Slow}}}$)
- Mean Absolute Scaled Error ($\text{MASE}$, with seasonal lag $S=24\text{h}$)

### 2.2 Pillar 2: Resilience (Shock Absorption Under Disruption)
- Max Absolute Error ($\text{MaxAE} = \max |y_t - \hat{y}_t|$)
- Shock RMSE Degradation ($\Delta\text{RMSE}_{\text{shock}} = \frac{\text{RMSE}_{\text{shock}} - \text{RMSE}_{\text{base}}}{\text{RMSE}_{\text{base}}}$ under simulated 72-hour storms)
- Shock Recovery Speed ($T_{\text{recover}} \le 1.0\text{ hr}$ to return to $\text{MAE} + 1.5\sigma$)
- Residual Autocorrelation during stress ($r_{\text{resid}}(k)$)

### 2.3 Pillar 3: Generalizability (Zero-Shot Cross-Airport Transfer)
- Cross-Airport Transfer Loss ($\Delta\text{RMSE}_{\text{transfer}} = \text{RMSE}_{B \leftarrow A} - \text{RMSE}_B$)
- Cluster Generalization Ratio ($GR_{\text{cluster}} = \frac{\text{Mean RMSE}_{\text{Cluster 2}}}{\text{Mean RMSE}_{\text{Cluster 1}}} \approx 1.05$)
- Relative Transfer Ratio ($\text{RTR} = \frac{\text{RMSE}_{\text{transfer}}}{\text{RMSE}_{\text{in-sample}}}$)
- Cross-Era Structural Stability ($\Delta\text{RMSE}_{\text{era}}$ across 2019 / 2022+)
- Connecting Ratio Sensitivity ($\frac{\partial \text{RMSE}}{\partial R_{\text{conn}}}$)

---

## 3. Verification & Acceptance Criteria

- [x] All 14 metrics implemented in evaluation routines (`src/models/eval_pillars.py`).
- [x] Evaluation tables generated for 2025 out-of-time holdout.
- [x] Robustness, Resilience, and Generalizability reported in Chapter 4 and Chapter 5.
