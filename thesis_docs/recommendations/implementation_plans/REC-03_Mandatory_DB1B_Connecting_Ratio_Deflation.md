# STATUS: NOT IMPLEMENTED

# Recommendation REC-03: Mandatory DB1B/DB1C Connecting Ratio Capacity Deflation

**Recommendation ID**: REC-03  
**Target Module**: `src/features/cluster_adaptive_features.py` (or `src/features/demand_deflat.py`)  
**Warehouse Status**: TESTED (Top 9)  
**final-thesis Status**: NOT IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Treating gross scheduled seat departures as originating local passengers overstates landside security checkpoint volumes by up to $2.5\times$ at hub airfields. At major connecting hubs, transfer passengers remain within the sterile airside concourse and **never enter TSA checkpoint screening queues** (e.g., DFW: 66.3% connecting; ORD: 60.0% connecting).

Deflating scheduled seat capacity by Bureau of Transportation Statistics (BTS) DB1B/DB1C passenger connecting ratios aligns physical seat supply with landside screening demand:
$$\text{NetOriginatingDemand}_{i, t} = \sum_k \text{Seats}_{k, t} \times \text{LoadFactor}_{m(t), i} \times (1.0 - \text{ConnectingRatio}_{q(t), i})$$

---

## 2. Technical Specification

### 2.1 Benchmark Connecting Ratios
- **DFW**: $66.3\%$ Connecting $\implies 33.7\%$ Originating multiplier ($0.337$)
- **ORD**: $60.0\%$ Connecting $\implies 40.0\%$ Originating multiplier ($0.400$)
- **DTW**: $52.8\%$ Connecting $\implies 47.2\%$ Originating multiplier ($0.472$)
- **IAH**: $48.5\%$ Connecting $\implies 51.5\%$ Originating multiplier ($0.515$)
- **PHL**: $41.2\%$ Connecting $\implies 58.8\%$ Originating multiplier ($0.588$)
- **LAX**: $32.0\%$ Connecting $\implies 68.0\%$ Originating multiplier ($0.680$)
- **EWR**: $28.5\%$ Connecting $\implies 71.5\%$ Originating multiplier ($0.715$)
- **BOS**: $18.4\%$ Connecting $\implies 81.6\%$ Originating multiplier ($0.816$)
- **LGA**: $8.2\%$ Connecting $\implies 91.8\%$ Originating multiplier ($0.918$)

### 2.2 Mathematical Formula
Applying DB1B connecting ratio deflation boosts explained variance across pooled airfields by **+40.6%** to $R^2 = 0.4181$ ($r = 0.6466$), preventing a 2.5-fold passenger over-prediction.

---

## 3. Implementation Code

```python
"""
Deflation calculation snippet in src/features/cluster_adaptive_features.py
"""

AIRPORT_CONNECTING_RATIOS = {
    "DFW": 0.663, "ORD": 0.600, "DTW": 0.528, "IAH": 0.485,
    "LAX": 0.320, "PHL": 0.412, "EWR": 0.285, "BOS": 0.184, "LGA": 0.082
}

def compute_originating_demand(df: pd.DataFrame) -> pd.DataFrame:
    res = df.copy()
    res["connecting_ratio"] = res["Airport"].map(AIRPORT_CONNECTING_RATIOS).fillna(0.30)
    lf = res["Load_Factor"] if "Load_Factor" in res.columns else 0.85
    res["net_originating_demand"] = res["Scheduled_Seats"] * lf * (1.0 - res["connecting_ratio"])
    return res
```

---

## 4. Verification & Acceptance Criteria

- [ ] DFW originating demand is reduced by $\approx 66.3\%$ relative to raw seats $\times$ load factor.
- [ ] LGA originating demand is reduced by only $\approx 8.2\%$.
- [ ] Explained variance $R^2$ improvement verified on holdout dataset.
- [ ] Unit tests pass in `tests/test_cluster_adaptive_pipeline.py`.
