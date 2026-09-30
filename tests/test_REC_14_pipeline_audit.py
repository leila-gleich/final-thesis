"""
tests/test_REC_14_pipeline_audit.py
-----------------------------------
Unit tests for REC-14 Standardized 3-Phase ETL & Integrity Audit Suite.
"""

import unittest
import pandas as pd
from src.etl.pipeline_audit import (
    standardize_timestamp_strings,
    remediate_airport_codes,
    remediate_airport_names,
    PipelineIntegrityAudit,
    FAA_LID_TO_IATA
)

class TestPipelineAudit(unittest.TestCase):
    def test_timestamp_padding(self):
        s = pd.Series(["0:00", "7:15", "12:30", "23:59", "2023-05-01 4:00:00"])
        padded = standardize_timestamp_strings(s)
        self.assertEqual(padded.iloc[0], "00:00")
        self.assertEqual(padded.iloc[1], "07:15")
        self.assertEqual(padded.iloc[2], "12:30")
        self.assertEqual(padded.iloc[3], "23:59")
        self.assertEqual(padded.iloc[4], "2023-05-01 04:00:00")

    def test_airport_code_remediation(self):
        df = pd.DataFrame({"Airport": ["GPI", "IWA", "GSN", "dfw"]})
        cleaned = remediate_airport_codes(df)
        self.assertEqual(cleaned["Airport"].tolist(), ["FCA", "AZA", "SPN", "DFW"])

    def test_airport_name_remediation(self):
        df = pd.DataFrame({"Airport_Name": ["Atlanta,", "New  Windor", "Utha County", None]})
        cleaned = remediate_airport_names(df)
        self.assertEqual(cleaned["Airport_Name"].iloc[0], "Atlanta")
        self.assertEqual(cleaned["Airport_Name"].iloc[1], "New Windsor")
        self.assertEqual(cleaned["Airport_Name"].iloc[2], "Utah County")
        self.assertEqual(cleaned["Airport_Name"].iloc[3], "Unknown / Unassigned")

    def test_6point_audit_passes_on_valid_data(self):
        valid_df = pd.DataFrame({
            "Airport": ["DFW", "ORD", "LAX"],
            "Date": ["2023-01-01", "2024-06-15", "2025-10-31"],
            "Time": ["06:00", "14:30", "21:00"],
            "Throughput": [1200, 2400, 1800]
        })
        auditor = PipelineIntegrityAudit(valid_df, key_cols=["Airport", "Date"], time_col="Time", value_col="Throughput")
        results = auditor.run_full_audit()
        self.assertTrue(results["all_passed"])

    def test_6point_audit_detects_flaws(self):
        flawed_df = pd.DataFrame({
            "Airport": ["DFW", "123", "TOOLONG"],
            "Date": ["2018-01-01", "2023-01-01", "2024-01-01"],  # 2018 is out of bounds
            "Time": ["6:00", "12:00", "18:00"],  # 6:00 is unpadded
            "Throughput": [-50, 100, 200]  # -50 is negative
        })
        auditor = PipelineIntegrityAudit(flawed_df, key_cols=["Airport", "Date"], time_col="Time", value_col="Throughput")
        results = auditor.run_full_audit()
        self.assertFalse(results["all_passed"])
        self.assertFalse(results["timestamp_format_passed"])
        self.assertFalse(results["airport_code_passed"])
        self.assertFalse(results["non_negative_passed"])
        self.assertFalse(results["date_bounds_passed"])

if __name__ == "__main__":
    unittest.main()
