"""
tests/test_REC_06_splits.py
---------------------------
Unit tests for REC-06 Candidate B Demarcation & 7-Day Purge Embargo Partitioning.
"""

import unittest
import pandas as pd
from src.data.split_regimes import (
    filter_quarantine_pandemic,
    filter_candidate_b,
    apply_candidate_b_partitions,
    CANDIDATE_B_START,
    CANDIDATE_B_END,
    TRAIN_START,
    TRAIN_END,
    VAL_START,
    VAL_END,
    TEST_START,
    TEST_END
)

class TestSplitRegimes(unittest.TestCase):
    def setUp(self):
        dates = pd.date_range("2019-01-01", "2025-12-31", freq="D")
        self.df = pd.DataFrame({"Date": dates, "val": range(len(dates))})

    def test_pandemic_quarantine(self):
        clean = filter_quarantine_pandemic(self.df)
        clean_dates = pd.to_datetime(clean["Date"])
        # Check no dates in quarantine
        quarantine = (clean_dates >= "2020-03-01") & (clean_dates <= "2022-04-30")
        self.assertEqual(quarantine.sum(), 0)

    def test_candidate_b_filter(self):
        cand_b = filter_candidate_b(self.df)
        b_dates = pd.to_datetime(cand_b["Date"])
        self.assertEqual(b_dates.min(), pd.Timestamp("2022-05-01"))
        self.assertEqual(b_dates.max(), pd.Timestamp("2025-12-31"))

    def test_partition_boundaries_and_purge_embargo(self):
        train_df, val_df, test_df = apply_candidate_b_partitions(self.df)
        
        train_dates = pd.to_datetime(train_df["Date"])
        val_dates = pd.to_datetime(val_df["Date"])
        test_dates = pd.to_datetime(test_df["Date"])
        
        # Check train bounds
        self.assertEqual(train_dates.min(), pd.Timestamp(TRAIN_START))
        self.assertEqual(train_dates.max(), pd.Timestamp(TRAIN_END))
        
        # Check 7-day purge embargo between Train and Val: Dec 25-31 2023 must not be in train or val
        leakage_1 = (train_dates >= "2023-12-25") & (train_dates <= "2023-12-31")
        self.assertEqual(leakage_1.sum(), 0)
        self.assertEqual(val_dates.min(), pd.Timestamp(VAL_START))
        self.assertEqual(val_dates.max(), pd.Timestamp(VAL_END))
        
        # Check 7-day purge embargo between Val and Test: Dec 25-31 2024 must not be in val or test
        leakage_2 = (val_dates >= "2024-12-25") & (val_dates <= "2024-12-31")
        self.assertEqual(leakage_2.sum(), 0)
        self.assertEqual(test_dates.min(), pd.Timestamp(TEST_START))
        self.assertEqual(test_dates.max(), pd.Timestamp(TEST_END))

if __name__ == "__main__":
    unittest.main()
