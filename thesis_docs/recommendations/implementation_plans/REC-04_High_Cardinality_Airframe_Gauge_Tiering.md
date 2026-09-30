# STATUS: NOT IMPLEMENTED

# Recommendation REC-04: High-Cardinality Airframe Gauge Tiering

**Recommendation ID**: REC-04  
**Target Module**: `src/features/fleet_tiers.py` (or `src/features/cluster_adaptive_features.py`)  
**Warehouse Status**: ANALYZED  
**final-thesis Status**: NOT IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Passengers boarding a 70-seat regional jet arrive on a significantly tighter temporal distribution than passengers boarding a 300-seat widebody aircraft. Convolving all aircraft types with a uniform show-up kernel introduces arrival variance error.

Between 2019 and 2025, fleet upgauging expanded marginal passengers screened per flight from 227.17 to 267.58 (+17.8%). Airlines permanently retired 50-seat regional jets in favor of 180–240 seat A321neo and 737 MAX 9 aircraft. Segmenting flights by structural airframe gauge tier ensures that arrival distributions scale naturally with physical aircraft capacity.

---

## 2. Technical Specification

### 2.1 Fleet Gauge Tiers
Segment all scheduled flights into three structural gauge tiers:

1. **Regional Tier** ($\le 76$ seats: CRJ-700/900, Embraer 170/175):
   - Modal lead: 55 minutes
   - Boarding gate cutoff: $T - 25$ minutes
2. **Narrowbody Mainline** ($77\text{--}210$ seats: A320/321, B737-800/900/MAX, A220):
   - Modal lead: 95 minutes
   - Boarding gate cutoff: $T - 35$ minutes
3. **Widebody Transcontinental/Intl** ($> 210$ seats: B777, B787, A350, A330):
   - Modal lead: 140 minutes
   - Boarding gate cutoff: $T - 50$ minutes

### 2.2 Execution Protocol
Convolve each fleet tier independently using its tier-specific modal arrival parameters before aggregating to total airport-hour originating passenger demand.

---

## 3. Implementation Code

```python
"""
Fleet gauge tiering snippet in src/features/fleet_tiers.py
"""

import pandas as pd
import numpy as np

def assign_fleet_gauge_tier(seats: int) -> str:
    if seats <= 76:
        return "Regional"
    elif seats <= 210:
        return "Narrowbody"
    else:
        return "Widebody"

def apply_fleet_tiering(df: pd.DataFrame, seat_col: str = "Scheduled_Seats") -> pd.DataFrame:
    res = df.copy()
    res["gauge_tier"] = res[seat_col].apply(assign_fleet_gauge_tier)
    return res
```

---

## 4. Verification & Acceptance Criteria

- [ ] Every scheduled flight is assigned to one of the 3 gauge tiers (`Regional`, `Narrowbody`, `Widebody`).
- [ ] Tier-specific convolution kernels applied before aggregating hourly demand.
- [ ] Feature `aircraft_gauge_seats` included in supervised learning feature matrix.
