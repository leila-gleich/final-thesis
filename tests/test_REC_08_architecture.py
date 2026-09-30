"""
tests/test_REC_08_architecture.py
---------------------------------
Unit tests for REC-08 100% Self-Contained Repository & Curated Data Architecture.
"""

import unittest
from pathlib import Path
from src.utils.paths import (
    BASE_DIR,
    CURATED_DATA_DIR,
    SAMPLE_DATA_DIR,
    HOURLY_CURATED_PATH,
    DAILY_CURATED_PATH,
    verify_self_contained_architecture
)

class TestArchitecture(unittest.TestCase):
    def test_base_dir_resolution(self):
        self.assertTrue(BASE_DIR.exists())
        self.assertTrue((BASE_DIR / "src").exists())
        self.assertTrue((BASE_DIR / "data").exists())

    def test_curated_data_presence(self):
        self.assertTrue(CURATED_DATA_DIR.exists())
        self.assertTrue(HOURLY_CURATED_PATH.exists(), f"Missing {HOURLY_CURATED_PATH}")
        self.assertTrue(DAILY_CURATED_PATH.exists(), f"Missing {DAILY_CURATED_PATH}")
        # Verify non-empty size
        self.assertGreater(HOURLY_CURATED_PATH.stat().st_size, 1000)
        self.assertGreater(DAILY_CURATED_PATH.stat().st_size, 1000)

    def test_sample_data_presence(self):
        self.assertTrue(SAMPLE_DATA_DIR.exists())

    def test_verify_architecture_helper(self):
        status = verify_self_contained_architecture()
        self.assertTrue(status["all_valid"])
        self.assertTrue(status["no_external_symlinks"])

if __name__ == "__main__":
    unittest.main()
