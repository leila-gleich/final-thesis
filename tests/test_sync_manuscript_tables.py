"""
tests/test_sync_manuscript_tables.py
------------------------------------
Tests extraction, formatting, and synchronization of manuscript tables into conformed CSVs.
"""

import unittest
from pathlib import Path
import csv
from src.analysis.sync_manuscript_tables import (
    TABLE_SPECS,
    MANUSCRIPT_TABLES_DIR,
    sync_all,
    clean_markdown_cell,
)


class TestManuscriptTableSynchronization(unittest.TestCase):
    def test_clean_cell_transformations(self):
        self.assertEqual(clean_markdown_cell(r"**Bold Text**"), "Bold Text")
        self.assertEqual(clean_markdown_cell(r"*Italic Text*"), "Italic Text")
        self.assertEqual(clean_markdown_cell(r"$\text{RMSE}_{\text{routine}}$"), "RMSE_routine")
        self.assertEqual(clean_markdown_cell(r"$M_1^*$"), "M1*")
        self.assertEqual(clean_markdown_cell(r"$p < 0.001$"), "p < 0.001")
        self.assertEqual(clean_markdown_cell(r"$\ge 15$m"), ">= 15m")

    def test_sync_execution_and_file_generation(self):
        records = sync_all()
        self.assertEqual(len(records), 16)
        
        # Verify that all 16 canonical and short CSV files exist and have content
        for spec in TABLE_SPECS.values():
            canonical_file = MANUSCRIPT_TABLES_DIR / f"{spec['slug']}.csv"
            short_file = MANUSCRIPT_TABLES_DIR / f"{spec['short_name']}.csv"
            
            self.assertTrue(canonical_file.exists(), f"Missing canonical file: {canonical_file}")
            self.assertTrue(short_file.exists(), f"Missing short file: {short_file}")
            
            with open(canonical_file, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                rows = list(reader)
                self.assertGreater(len(rows), 1, f"Table {spec['slug']} has no data rows!")
                # Header row count matches all data row counts
                header_len = len(rows[0])
                for idx, r in enumerate(rows[1:]):
                    self.assertEqual(len(r), header_len, f"Row {idx} mismatch in {canonical_file}")


if __name__ == "__main__":
    unittest.main()
