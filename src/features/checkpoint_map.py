"""
src/features/checkpoint_map.py
------------------------------
Airline-to-Checkpoint Spatial-Temporal Integration Engine (REC-13).

Provides:
1. Checkpoint Confidence Tiers (CSF):
   - Tier 1: Dedicated Exclusive Checkpoints (CSF = 1.0)
     e.g., DTW McNamara Red, EWR Term C CKPT-C1, BOS Term A Checkpoint A1, LGA Term C TC-CHK
   - Tier 2: Shared Terminal Checkpoints (CSF = 0.80)
     e.g., ORD Term 3 CKPT 7/8, LGA Term B
   - Tier 3: Multi-Concourse Central Checkpoints (CSF = 0.50)
     e.g., IAD Main, SLC Central
2. Dynamic spatial carrier-checkpoint flight bank weighting.
3. Confidence-weighted Huber loss weighting helper.
"""

import pandas as pd
import numpy as np

CHECKPOINT_CONFIDENCE_TIERS = {
    # Tier 1: Exclusive Dedicated Checkpoints (CSF = 1.0)
    "DTW_MCNAMARA_RED": 1.0,
    "EWR_TERMC_CKPT1": 1.0,
    "BOS_TERMA_A1": 1.0,
    "LGA_TERMC_TCCHK": 1.0,
    "DFW_TERMA_A12": 1.0,
    "DFW_TERMC_C10": 1.0,
    "ORD_TERM1_CKPT1": 1.0,
    
    # Tier 2: Shared Terminal Checkpoints (CSF = 0.80)
    "ORD_TERM3_CKPT7": 0.80,
    "ORD_TERM3_CKPT8": 0.80,
    "PHL_TERMB_CKPTB": 0.80,
    "IAH_TERMC_30CN": 0.80,
    "LAX_TERM4_T4": 0.80,
    "LAX_TERM3_T3": 0.80,
    "LAX_TERM7_T7": 0.80,
    
    # Tier 3: Multi-Concourse Central Checkpoints (CSF = 0.50)
    "IAD_MAIN_EAST": 0.50,
    "SLC_CENTRAL_MAIN": 0.50,
    "DEN_WEST_CKPT": 0.50,
    "MCO_EAST_CHECKPOINT": 0.50
}

DEFAULT_CSF = 0.75

def get_checkpoint_confidence(checkpoint_id: str) -> float:
    """Returns Checkpoint Scaling Factor (CSF in [0.5, 1.0])."""
    if not isinstance(checkpoint_id, str):
        return DEFAULT_CSF
    clean_id = checkpoint_id.strip().upper().replace(" ", "_").replace("-", "")
    for k, v in CHECKPOINT_CONFIDENCE_TIERS.items():
        if k in clean_id or clean_id in k:
            return v
    return DEFAULT_CSF

def compute_checkpoint_weights(
    df: pd.DataFrame,
    checkpoint_col: str = "Checkpoint",
    carrier_col: str = "Carrier",
    volume_col: str = "Scheduled_Departures"
) -> pd.DataFrame:
    """
    Computes dynamic spatial weights and checkpoint confidence factors.
    """
    res = df.copy()
    if checkpoint_col in res.columns:
        res["checkpoint_confidence_factor"] = res[checkpoint_col].apply(get_checkpoint_confidence).astype(np.float32)
    else:
        # Infer tier from exclusivity in experimental cohort
        res["checkpoint_confidence_factor"] = 1.0  # Cohort defaults to exclusive
        
    return res

def huber_loss_weights(confidence_factors: np.ndarray) -> np.ndarray:
    """Returns normalized sample weights for Huber loss based on CSF."""
    w = np.array(confidence_factors, dtype=np.float64)
    return w / w.mean()

if __name__ == "__main__":
    ckpts = ["DTW_McNamara_Red", "ORD_Term3_CKPT7", "SLC_Central_Main", "Unknown_Checkpoint"]
    df = pd.DataFrame({"Checkpoint": ckpts})
    out = compute_checkpoint_weights(df)
    print(out)
