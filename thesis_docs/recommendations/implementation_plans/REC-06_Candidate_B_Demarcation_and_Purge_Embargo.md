# STATUS: NOT IMPLEMENTED

# Recommendation REC-06: Candidate B Demarcation & 7-Day Purge Embargo

**Recommendation ID**: REC-06  
**Target Module**: `src/data/split_regimes.py` (or `src/etl/generate_v1_datasets.py`)  
**Warehouse Status**: JUSTIFIED (May 22)  
**final-thesis Status**: NOT IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

The COVID-19 pandemic broke the foundational relationship between flight schedules and passenger demand. CARES Act minimum service rules forced airlines to fly skeletal "ghost flights," plummeting passengers per flight from 330 to 22.7, producing severe Chow structural breaks ($F = 19,657.5, p < 10^{-300}$). Training models across the pandemic produces a negative forecast bias of **-382 passengers/hour** and drops out-of-time test $R^2$ to 0.6810.

Conversely, Candidate B (May 1, 2022 – December 31, 2025) anchors training to the exact breakpoint of nationwide mask-free normalization (following the April 18, 2022 federal court vacatur) and international test rescission. Candidate B provides **757,765 conformed hourly records across 44 months**, encompassing 4 summer peaks and 3 holiday surges with stationary coupling ($356.9$ pax/flight, $CV = 0.1096$, load factor mean $84.78\%$). Training exclusively on Candidate B boosts out-of-time test $R^2$ to **0.7506 (+11.6% RMSE reduction, 71.5% bias reduction)**.

---

## 2. Technical Specification

### 2.1 Date Boundaries
```python
CANDIDATE_B_START_DATE_ID = 20220501
CANDIDATE_B_END_DATE_ID   = 20251231

PRE_PANDEMIC_START_ID     = 20190101
PRE_PANDEMIC_END_ID       = 20200229

PANDEMIC_QUARANTINE_START = 20200301
PANDEMIC_QUARANTINE_END   = 20220430
```

### 2.2 Zero-Leakage Chronological Partitions & Purge Embargo
Partition Candidate B into strict chronological sets with 7-day non-leakage purge embargo buffers:
- **Training Partition**: May 1, 2022 – December 31, 2023 ($N = 404,324$ conformed hourly records)
- **Validation Partition**: January 1, 2024 – December 31, 2024 ($N = 207,328$ conformed hourly records)
- **Out-of-Time Holdout Partition**: January 1, 2025 – December 31, 2025 ($N = 215,562$ conformed hourly records)
- **Purge Embargo**: 7-day buffer between adjacent partitions to eliminate rolling feature overlap leakage.

---

## 3. Implementation Code

```python
"""
Temporal partition snippet in src/data/split_regimes.py
"""

import pandas as pd

def apply_candidate_b_partitions(df: pd.DataFrame, date_col: str = "Date") -> tuple:
    df[date_col] = pd.to_datetime(df[date_col])
    
    # Exclude pandemic quarantine
    clean_df = df[(df[date_col] < "2020-03-01") | (df[date_col] >= "2022-05-01")].copy()
    
    # Candidate B partitions
    train_df = clean_df[(clean_df[date_col] >= "2022-05-01") & (clean_df[date_col] <= "2023-12-24")] # 7-day purge before Jan 1
    val_df   = clean_df[(clean_df[date_col] >= "2024-01-01") & (clean_df[date_col] <= "2024-12-24")]   # 7-day purge before Jan 1
    test_df  = clean_df[(clean_df[date_col] >= "2025-01-01") & (clean_df[date_col] <= "2025-12-31")]
    
    return train_df, val_df, test_df
```

---

## 4. Verification & Acceptance Criteria

- [ ] All records between March 1, 2020 and April 30, 2022 are quarantined from model training.
- [ ] Training partition starts May 1, 2022.
- [ ] Test partition strictly covers full calendar year 2025 (Jan 1 – Dec 31, 2025).
- [ ] 7-day purge embargo prevents feature leakage between adjacent partitions.
