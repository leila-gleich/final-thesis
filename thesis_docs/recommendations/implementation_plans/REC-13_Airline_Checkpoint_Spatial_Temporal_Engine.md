# STATUS: NOT IMPLEMENTED

# Recommendation REC-13: Airline-to-Checkpoint Spatial-Temporal Integration Engine

**Recommendation ID**: REC-13  
**Target Module**: `src/features/airline_checkpoint_integration.py` (or `src/features/checkpoint_map.py`)  
**Warehouse Status**: FORMULATED  
**final-thesis Status**: NOT IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Aggregating flight departure data at the whole-airport level introduces severe spatial mismatch at multi-terminal airports (e.g. comparing LGA Terminal B checkpoints against airport-wide departures creates an artificial 46.2% connecting ratio error).

Building an explicit spatial-temporal mapping between specific airline flight banks and dedicated security checkpoints eliminates inter-terminal crosstalk.

---

## 2. Technical Specification

### 2.1 Checkpoint Confidence Tiers
Classify checkpoints into three confidence tiers:
- **Tier 1: Exclusive Airline Checkpoints** ($CSF_c = 1.0$): Checkpoints physically dedicated to a single airline (e.g., DTW McNamara, EWR Term C, BOS Term A, LGA Term C).
- **Tier 2: Shared Terminal Checkpoints** ($CSF_c = 0.80$): Checkpoints serving 2–3 dominant carriers in a single terminal (e.g., LGA Term B).
- **Tier 3: Multi-Concourse Central Checkpoints** ($CSF_c = 0.50$): Centralized checkpoints serving all airport carriers (e.g., IAD Main, SLC Central).

### 2.2 Dynamic Spatial Weights & Loss Function
Calculate dynamic spatial airline weights:
$$\mathbf{W}_{c, a, t} = \frac{\sum_{f \in \mathcal{F}_{c, a, t}} \text{Seats}(f) \times LF(f)}{\sum_{a' \in \mathcal{A}_c} \sum_{f \in \mathcal{F}_{c, a', t}} \text{Seats}(f) \times LF(f)}$$

Train models using **Confidence-Weighted Huber Loss**:
$$\mathcal{L} = \frac{1}{N}\sum \sum_c CSF_c \cdot \text{HuberLoss}(y_{c, t}, \hat{y}_{c, t})$$

---

## 3. Implementation Code

```python
"""
src/features/airline_checkpoint_integration.py
Computes spatial airline-checkpoint confidence weights, DDI, CSI, and confidence-weighted Huber loss.
"""

import numpy as np
import pandas as pd

CHECKPOINT_CONFIDENCE_TIERS = {
    "DTW_McNamara_Blue1": 1.0, "EWR_TermC_CKPT1": 1.0, "BOS_TermA_CKPT1": 1.0,
    "LGA_TermB_CHK": 0.8, "LGA_TermC_CHK": 0.8, "ORD_Term3_CKPT4B": 0.8,
    "IAD_Main_EastMezz": 0.5, "DFW_TermA_A21": 0.5, "LAX_Term7_Pass": 0.5
}

def get_checkpoint_confidence(checkpoint_code: str) -> float:
    return CHECKPOINT_CONFIDENCE_TIERS.get(checkpoint_code, 0.7)
```

---

## 4. Verification & Acceptance Criteria

- [ ] Checkpoints correctly assigned to Tier 1 ($1.0$), Tier 2 ($0.8$), or Tier 3 ($0.5$).
- [ ] Spatial airline weights calculated dynamically per checkpoint-hour.
- [ ] Huber loss weighted by confidence score during model fitting.
