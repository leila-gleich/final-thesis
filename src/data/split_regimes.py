"""
src/data/split_regimes.py
-------------------------
Candidate B Demarcation & 7-Day Purge Embargo Partitioning (REC-06).

Enforces:
1. Quarantine of Pandemic Structural Distortion (2020-03-01 to 2022-04-30).
2. Candidate B Post-Mandate Regimes: 2022-05-01 to 2025-12-31.
3. Zero-Leakage Chronological Partitions with 7-day Purge Embargoes:
   - Training Partition: 2022-05-01 to 2023-12-24
   - Validation Partition: 2024-01-01 to 2024-12-24
   - Test/Holdout Partition: 2025-01-01 to 2025-12-31
"""

import pandas as pd
from typing import Tuple, Dict

# Demarcation Boundary Constants
CANDIDATE_B_START = "2022-05-01"
CANDIDATE_B_END   = "2025-12-31"

PANDEMIC_QUARANTINE_START = "2020-03-01"
PANDEMIC_QUARANTINE_END   = "2022-04-30"

PRE_PANDEMIC_START = "2019-01-01"
PRE_PANDEMIC_END   = "2020-02-29"

# Chronological partition bounds with 7-day purge embargoes
TRAIN_START = "2022-05-01"
TRAIN_END   = "2023-12-24"  # 7-day purge before 2024-01-01

VAL_START   = "2024-01-01"
VAL_END     = "2024-12-24"  # 7-day purge before 2025-01-01

TEST_START  = "2025-01-01"
TEST_END    = "2025-12-31"

def filter_quarantine_pandemic(df: pd.DataFrame, date_col: str = "Date") -> pd.DataFrame:
    """
    Quarantines observations falling within the pandemic disruption window
    (2020-03-01 to 2022-04-30) where CARES Act ghost flights severely distorted load factors.
    """
    res = df.copy()
    dates = pd.to_datetime(res[date_col])
    in_quarantine = (dates >= PANDEMIC_QUARANTINE_START) & (dates <= PANDEMIC_QUARANTINE_END)
    return res[~in_quarantine].copy()

def filter_candidate_b(df: pd.DataFrame, date_col: str = "Date") -> pd.DataFrame:
    """
    Extracts strictly the Candidate B regime window (2022-05-01 to 2025-12-31).
    """
    res = df.copy()
    dates = pd.to_datetime(res[date_col])
    in_cand_b = (dates >= CANDIDATE_B_START) & (dates <= CANDIDATE_B_END)
    return res[in_cand_b].copy()

def apply_candidate_b_partitions(df: pd.DataFrame, date_col: str = "Date") -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Partitions the dataset into Train, Validation, and Holdout partitions
    adhering to Candidate B boundaries and 7-day purge embargoes.
    
    Returns:
        (train_df, val_df, test_df)
    """
    res = df.copy()
    res["_dt_temp"] = pd.to_datetime(res[date_col])
    
    train_mask = (res["_dt_temp"] >= TRAIN_START) & (res["_dt_temp"] <= TRAIN_END)
    val_mask   = (res["_dt_temp"] >= VAL_START)   & (res["_dt_temp"] <= VAL_END)
    test_mask  = (res["_dt_temp"] >= TEST_START)  & (res["_dt_temp"] <= TEST_END)
    
    train_df = res[train_mask].drop(columns=["_dt_temp"]).copy()
    val_df   = res[val_mask].drop(columns=["_dt_temp"]).copy()
    test_df  = res[test_mask].drop(columns=["_dt_temp"]).copy()
    
    return train_df, val_df, test_df

def get_partition_summary(train_df: pd.DataFrame, val_df: pd.DataFrame, test_df: pd.DataFrame, date_col: str = "Date") -> Dict:
    """
    Returns summary statistics for the generated partitions.
    """
    return {
        "train_rows": len(train_df),
        "train_start": str(train_df[date_col].min()) if not train_df.empty else None,
        "train_end": str(train_df[date_col].max()) if not train_df.empty else None,
        "val_rows": len(val_df),
        "val_start": str(val_df[date_col].min()) if not val_df.empty else None,
        "val_end": str(val_df[date_col].max()) if not val_df.empty else None,
        "test_rows": len(test_df),
        "test_start": str(test_df[date_col].min()) if not test_df.empty else None,
        "test_end": str(test_df[date_col].max()) if not test_df.empty else None,
    }

if __name__ == "__main__":
    # Create sample date range covering 2019 to 2025
    dates = pd.date_range("2019-01-01", "2025-12-31", freq="D")
    sample_df = pd.DataFrame({"Date": dates, "value": range(len(dates))})
    
    no_pandemic = filter_quarantine_pandemic(sample_df)
    train_df, val_df, test_df = apply_candidate_b_partitions(sample_df)
    summary = get_partition_summary(train_df, val_df, test_df)
    
    print("=" * 60)
    print("CANDIDATE B PARTITIONING REPORT (REC-06)")
    print("=" * 60)
    for k, v in summary.items():
        print(f"  {k:<15}: {v}")
    print("=" * 60)
    assert summary["train_rows"] > 0 and summary["val_rows"] > 0 and summary["test_rows"] > 0
    print("Self-test passed.")
