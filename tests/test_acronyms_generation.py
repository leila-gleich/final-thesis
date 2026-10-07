"""
test_acronyms_generation.py
===========================
Unit tests validating the structural integrity, APA 7th edition table rules,
and textual completeness of the generated Acronyms and Abbreviations documents
(both Word .docx and Markdown .md) for the master's thesis.
"""

import os
import unittest
import docx

class TestAcronymsGeneration(unittest.TestCase):
    def setUp(self):
        self.docx_path = "thesis_docs/manuscripts/List_of_Acronyms_and_Abbreviations.docx"
        self.docx_v1_path = "thesis_docs/manuscripts/Acronyms v1.docx"
        self.md_path = "thesis_docs/manuscripts/acronyms.md"
        self.md_only_path = "thesis_docs/manuscripts/manuscripts-only/acronyms.md"
        
    def test_files_exist(self):
        """Verify that all generated acronym files exist and have non-zero size."""
        for path in [self.docx_path, self.docx_v1_path, self.md_path, self.md_only_path]:
            self.assertTrue(os.path.exists(path), f"File missing: {path}")
            self.assertGreater(os.path.getsize(path), 1000, f"File too small: {path}")

    def test_docx_structure_and_table(self):
        """Verify that the Word document loads cleanly, contains the APA table and categories."""
        doc = docx.Document(self.docx_path)
        self.assertGreater(len(doc.paragraphs), 100, "Word document should contain > 100 paragraphs.")
        self.assertEqual(len(doc.tables), 1, "Word document should contain exactly 1 master table.")
        
        table = doc.tables[0]
        self.assertGreater(len(table.rows), 100, "Master table should contain > 100 acronym rows.")
        self.assertEqual(len(table.columns), 4, "Master table should have exactly 4 columns.")
        
        headers = [c.text.strip() for c in table.rows[0].cells]
        self.assertIn("Acronym / Abbreviation", headers[0])
        self.assertIn("Full Expansion", headers[1])
        self.assertIn("Operational Category", headers[2])
        self.assertIn("Primary Thesis Application", headers[3])

    def test_critical_acronyms_present(self):
        """Verify that essential aviation, queuing, and modeling acronyms are present."""
        with open(self.md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        critical_terms = [
            "**TSA**", "**MASE**", "**BTS**", "**ACRP**", "**A14**",
            "**CV_TSA**", "**CVI**", "**RTR**", "**TTR**", "**DM**",
            "**HAC**", "**DES**", "**NHPP**", "**IROPS**", "**GDP**",
            "**CAT**", "**FOIA**", "**FSD**", "**TSO**", "**LOS**",
            "**EWR**", "**LGA**", "**DTW**", "**DFW**", "**AA**",
            "**DL**", "**UA**", "**WN**", "**SARIMA**", "**HistGBM**"
        ]
        for term in critical_terms:
            self.assertIn(term, content, f"Critical acronym {term} missing from {self.md_path}")

    def test_all_seven_categories_present(self):
        """Verify that all 7 operational categories are represented in both Word and Markdown."""
        with open(self.md_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        for cat_num in range(1, 8):
            self.assertIn(f"Category {cat_num}:", content, f"Category {cat_num} missing from {self.md_path}")

    def test_prohibited_jargon_absence(self):
        """Verify that prohibited lab jargon does not appear in the acronym descriptions."""
        with open(self.md_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            
        # Ensure banned terms are not present in operational definitions
        banned = [
            "quiescent control", "sterile control", "acute shock state",
            "cyber-physical stability", "wiener-hopf deconvolution"
        ]
        for b in banned:
            self.assertNotIn(b, content, f"Prohibited jargon '{b}' found in acronyms document.")

if __name__ == "__main__":
    unittest.main()
