# STATUS: IMPLEMENTED

# Recommendation REC-12: Forecasting Paradigm Deployment Strategy

**Recommendation ID**: REC-12  
**Target Module**: `src/models/hybrid_sarima_tree.py`, `src/models/machine_learning.py`, `src/models/baselines.py`  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Choosing a single model class (pure deterministic point estimators or pure probabilistic networks) forces an unnecessary trade-off between peak point precision and off-peak/crisis resilience.

---

## 2. Technical Specification

### 2.1 Paradigm Strategy
1. Deploy **Schedule-Informed Hybrid Models** (Deterministic Flight Schedule Engine + Conformalized Probabilistic Residual Calibration) as the primary thesis contribution.
2. Apply deterministic flight mapping during structured peak waves ($r > 0.70$) to maximize point precision.
3. Use probabilistic prediction intervals ($\hat{q}_{0.10} - \hat{q}_{0.90}$) during off-peak hours (addressing the Off-Peak Staffing Paradox) and severe operational disruptions.
4. Implement quantile-based staffing bounds ($\hat{q}_{0.85}$) for TSA lane allocation recommendations to safeguard against stochastic arrival spikes.

---

## 3. Verification & Acceptance Criteria

- [x] Deterministic (M1), Probabilistic / Tweedie ML (M3), and Hybrid (M5) paradigms evaluated on holdout dataset (`run_pipeline.py`).
- [x] Quantile upper bounds ($\hat{q}_{0.85}$) calculated for off-peak intervals (`predict_quantiles` in M5).
- [x] Performance tradeoffs documented in Chapter 5.
