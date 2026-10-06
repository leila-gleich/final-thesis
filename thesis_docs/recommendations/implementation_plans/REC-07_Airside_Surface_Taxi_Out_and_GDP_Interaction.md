# STATUS: IMPLEMENTED

# Recommendation REC-07: Airside Surface Taxi-Out & GDP Interaction for Coastal Originators

**Recommendation ID**: REC-07  
**Target Module**: `src/features/airside_flow.py`  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

High-density slot-constrained airfields (Cluster 3: EWR, LGA, JFK) experience severe runway surface queuing and FAA Ground Delay Programs (GDP) that back up gate pushbacks and screening lanes.

In dedicated carrier screening lanes, hourly TSA screening volatility (CV) strongly couples with downstream flight departure delay volatility ($r = 0.6272, R^2 = 39.34\%$ vs. $19.13\%$ across pooled airfields). Checkpoint congestion acts as an empirical leading indicator of aircraft pushback delays, closing the feedback loop between landside screening and airside operations.

---

## 2. Technical Specification

### 2.1 Interaction Features
Engineer airside surface queue interaction features specifically for Cluster 3 coastal originators:

1. `taxi_out_rolling_avg_1h`: Average runway taxi-out duration over the prior 60 minutes.
2. `faa_gdp_active`: Binary indicator for active FAA Ground Delay Programs.
3. `tsa_volatility_hourly_cv`: Prior-hour rolling checkpoint demand coefficient of variation ($\text{CV}_{\text{TSA}}$), exploiting the verified $r = 0.6272$ queue-to-pushback delay coupling.
4. `taxi_congestion_interaction`: Product of taxi-out minutes and convolved lead demand ($\text{Taxi\_Out} \times \text{Lead}_1$) applied conditionally for Cluster 3 airfields.

---

## 3. Implementation Code

```python
"""
Airside flow interaction snippet in src/features/airside_flow.py
"""

import numpy as np
import pandas as pd

def compute_airside_interactions(df: pd.DataFrame) -> pd.DataFrame:
    res = df.copy()
    if "Taxi_Out_Minutes" in res.columns and "convolved_lead1" in res.columns:
        res["taxi_congestion_interaction"] = np.where(
            res["cluster_id"] == 3,
            res["Taxi_Out_Minutes"] * res["convolved_lead1"],
            0.0
        )
    return res
```

---

## 4. Verification & Acceptance Criteria

- [ ] `taxi_congestion_interaction` active for Cluster 3 airports (EWR, LGA).
- [ ] Correlation $r \ge 0.60$ between TSA CV and departure delay CV verified in dedicated carrier lanes.
- [ ] Interaction terms integrated into tree-based model feature sets (Model 2 and Model 3).
