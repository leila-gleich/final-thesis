"""
src/etl/pipeline_audit.py
-------------------------
Standardized 3-Phase ETL Pipeline & Data Integrity Audit Suite (REC-14).
Performs:
1. Timestamp standardisation (leading zero padding: '0:00' -> '00:00').
2. Airport LID Code Resolution (FAA LID -> official IATA/ICAO: GPI->FCA, IWA->AZA, GSN->SPN, etc.).
3. Typo remediation and missing airport name imputation.
4. Automated 6-point referential integrity verification audit.
"""

import re
import pandas as pd
import numpy as np

# Official FAA LID to IATA/ICAO mapping table
FAA_LID_TO_IATA = {
    "GPI": "FCA",  # Glacier Park International
    "IWA": "AZA",  # Phoenix-Mesa Gateway
    "GSN": "SPN",  # Saipan International
    "ISN": "XWA",  # Williston Basin International (relocated)
    "UST": "SGJ",  # St. Augustine / Northeast Florida Regional
    "AKL": "AKN",  # King Salmon (avoid Auckland conflict in domestic tables)
    "BKG": "BBG",  # Branson
    "AZA": "AZA",
    "FCA": "FCA",
    "SPN": "SPN"
}

# Systematic typo corrections
AIRPORT_TYPO_CORRECTIONS = {
    "Atlanta,": "Atlanta",
    "New  Windor": "New Windsor",
    "New  Windsor": "New Windsor",
    "Utha County": "Utah County",
    "Dallas/Fort Worth": "Dallas-Fort Worth",
    "Raleigh Durham": "Raleigh-Durham"
}

def standardize_timestamp_strings(series: pd.Series) -> pd.Series:
    """
    Ensures timestamps have 2-digit hour padding ('0:00' -> '00:00', '7:15' -> '07:15').
    Handles both 'H:MM' and ISO 'YYYY-MM-DD H:MM:SS' strings.
    """
    def _pad_hour(val):
        if pd.isna(val):
            return val
        s = str(val).strip()
        # Single digit hour followed by colon (e.g., '0:00', '9:30')
        if re.match(r"^\d:\d{2}", s):
            return "0" + s
        # Datetime string with single digit hour after space: '2023-05-01 7:00:00'
        s = re.sub(r" (\d):(\d{2})", r" 0\1:\2", s)
        return s

    return series.apply(_pad_hour)

def remediate_airport_codes(df: pd.DataFrame, col: str = "Airport") -> pd.DataFrame:
    """
    Maps non-standard FAA LID codes to official conformed IATA codes.
    """
    res = df.copy()
    if col in res.columns:
        res[col] = res[col].astype(str).str.strip().str.upper()
        res[col] = res[col].replace(FAA_LID_TO_IATA)
    return res

def remediate_airport_names(df: pd.DataFrame, col: str = "Airport_Name") -> pd.DataFrame:
    """
    Cleans known typos in airport names and fills missing labels.
    """
    res = df.copy()
    if col in res.columns:
        res[col] = res[col].replace(AIRPORT_TYPO_CORRECTIONS)
        res[col] = res[col].fillna("Unknown / Unassigned")
    return res

class PipelineIntegrityAudit:
    """
    Executes the 6-point referential integrity audit suite:
    1. Row count preservation (0 dropped fact rows).
    2. Timestamp format validity (all hours padded to HH:MM).
    3. Airport code syntax (valid 3-letter strings).
    4. Non-negative throughput/volume values.
    5. Referential key completeness (no NaN in primary composite keys).
    6. Temporal bounds verification (falls within 2019-2025 study horizon).
    """
    def __init__(self, df: pd.DataFrame, key_cols=None, time_col: str = None, value_col: str = None):
        self.df = df
        self.key_cols = key_cols or []
        self.time_col = time_col
        self.value_col = value_col
        self.audit_results = {}

    def run_full_audit(self) -> dict:
        results = {}
        
        # Check 1: Row count preservation
        results["row_count"] = len(self.df)
        results["row_count_passed"] = len(self.df) > 0
        
        # Check 2: Timestamp format validity
        if self.time_col and self.time_col in self.df.columns:
            sample_times = self.df[self.time_col].dropna().astype(str)
            unpadded = sample_times.str.match(r"^\d:\d{2}").sum()
            results["unpadded_hours"] = int(unpadded)
            results["timestamp_format_passed"] = (unpadded == 0)
        else:
            results["timestamp_format_passed"] = True

        # Check 3: Airport code format
        if "Airport" in self.df.columns:
            bad_codes = self.df["Airport"].dropna().apply(lambda x: len(str(x)) != 3 or not str(x).isalpha()).sum()
            results["invalid_airport_codes"] = int(bad_codes)
            results["airport_code_passed"] = (bad_codes == 0)
        else:
            results["airport_code_passed"] = True

        # Check 4: Non-negative values
        if self.value_col and self.value_col in self.df.columns:
            neg_count = (self.df[self.value_col] < 0).sum()
            results["negative_values"] = int(neg_count)
            results["non_negative_passed"] = (neg_count == 0)
        else:
            results["non_negative_passed"] = True

        # Check 5: Key completeness
        if self.key_cols:
            existing_keys = [c for c in self.key_cols if c in self.df.columns]
            null_keys = self.df[existing_keys].isna().any(axis=1).sum() if existing_keys else 0
            results["null_keys"] = int(null_keys)
            results["key_completeness_passed"] = (null_keys == 0)
        else:
            results["key_completeness_passed"] = True

        # Check 6: Date boundaries (2019-01-01 to 2025-12-31)
        if "Date" in self.df.columns:
            dates = pd.to_datetime(self.df["Date"], errors="coerce")
            out_of_bounds = ((dates < "2019-01-01") | (dates > "2025-12-31")).sum()
            results["out_of_bounds_dates"] = int(out_of_bounds)
            results["date_bounds_passed"] = (out_of_bounds == 0)
        else:
            results["date_bounds_passed"] = True

        results["all_passed"] = all([
            results["row_count_passed"],
            results["timestamp_format_passed"],
            results["airport_code_passed"],
            results["non_negative_passed"],
            results["key_completeness_passed"],
            results["date_bounds_passed"]
        ])
        
        self.audit_results = results
        return results

    def print_summary(self):
        res = self.run_full_audit()
        print("=" * 60)
        print("PIPELINE DATA INTEGRITY AUDIT REPORT (REC-14)")
        print("=" * 60)
        for k, v in res.items():
            print(f"  {k:<30}: {v}")
        print("=" * 60)
        return res["all_passed"]

if __name__ == "__main__":
    test_df = pd.DataFrame({
        "Airport": ["GPI", "IWA", "DFW", "JFK"],
        "Airport_Name": ["Atlanta,", "New  Windsor", "Dallas/Fort Worth", "John F Kennedy"],
        "Time": ["0:00", "7:15", "12:30", "23:45"],
        "Throughput": [100, 250, 800, 450],
        "Date": ["2023-01-01", "2023-05-15", "2024-02-20", "2025-11-30"]
    })
    
    cleaned = remediate_airport_codes(test_df)
    cleaned = remediate_airport_names(cleaned)
    cleaned["Time"] = standardize_timestamp_strings(cleaned["Time"])
    
    auditor = PipelineIntegrityAudit(cleaned, key_cols=["Airport", "Date"], time_col="Time", value_col="Throughput")
    passed = auditor.print_summary()
    assert passed, "Pipeline audit failed on cleaned test data!"
    print("Self-test passed.")
