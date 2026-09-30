# STATUS: NOT IMPLEMENTED

# Recommendation REC-14: Standardized 3-Phase ETL Pipeline & Data Integrity Audit Suite

**Recommendation ID**: REC-14  
**Target Module**: `src/etl/pipeline_audit.py` (or `src/etl/`)  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: NOT IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Data format inconsistencies (single-digit hours, non-standard FAA LID codes, airport name typos, missing values) distort model training across millions of fact rows.

A standardized 3-Phase ETL pipeline and automated data integrity audit suite must be integrated into `final-thesis/src/etl/`.

---

## 2. Technical Specification

### 2.1 Remediations
1. **Timestamp Standardisation**: Standardize all timestamps with leading zero hour padding (`0:00` $\to$ `00:00`) across 71,473 rows.
2. **Airport LID Code Resolution**: Map 12 non-standard FAA LID codes to official IATA codes across 201,192 rows (`GPI` $\to$ `FCA`, `IWA` $\to$ `AZA`, `GSN` $\to$ `SPN`, etc.) and synchronize checkpoint prefixes.
3. **Typo Remediation**: Correct 23,529 systematic airport name typos (`"Atlanta,"`, `"New  Windor"`, `"Utha County"`) and impute 3,032 empty airport names.
4. **Referential Integrity Audit**: Execute automated 6-point verification audit verifying 100% row preservation, zero format errors, and exact passenger aggregate matching against weekly source PDFs.

---

## 3. Implementation Code

```python
"""
Data integrity audit snippet in src/etl/pipeline_audit.py
"""

import pandas as pd

FAA_TO_IATA_MAP = {
    "GPI": "FCA", "IWA": "AZA", "GSN": "SPN"
}

def clean_airport_codes(df: pd.DataFrame, col: str = "Airport") -> pd.DataFrame:
    res = df.copy()
    res[col] = res[col].replace(FAA_TO_IATA_MAP)
    return res
```

---

## 4. Verification & Acceptance Criteria

- [ ] 100% row preservation post-ETL verified.
- [ ] Zero malformed hour strings (`0:00` padded to `00:00`).
- [ ] All FAA LID codes mapped to official IATA codes.
- [ ] 6-point audit suite passes with exit code 0.
