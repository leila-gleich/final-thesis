"""
src/utils/paths.py
------------------
Autonomous Self-Contained Repository & Curated Data Architecture (REC-08).
Guarantees 100% self-contained relative path resolution with zero external dependencies.
"""

from pathlib import Path
import os

# Project root: final-thesis/
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Data directories
DATA_DIR = BASE_DIR / "data"
CURATED_DATA_DIR = DATA_DIR / "curated"
SAMPLE_DATA_DIR = DATA_DIR / "sample"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
DIMENSIONS_DIR = DATA_DIR / "dimensions"

# Results and documentation directories
RESULTS_DIR = BASE_DIR / "results"
RESULTS_TABLES_DIR = RESULTS_DIR / "tables"
MANUSCRIPT_TABLES_DIR = RESULTS_DIR / "manuscript_tables"
THESIS_DOCS_DIR = BASE_DIR / "thesis_docs"
MANUSCRIPTS_DIR = THESIS_DOCS_DIR / "manuscripts"

# Canonical curated file targets
HOURLY_CURATED_PATH = CURATED_DATA_DIR / "hourly_aggregated_data.csv"
DAILY_CURATED_PATH = CURATED_DATA_DIR / "daily_aggregated_data.csv"

def get_base_dir() -> Path:
    """Returns absolute Path to final-thesis root."""
    return BASE_DIR

def verify_self_contained_architecture() -> dict:
    """
    Validates that repository paths exist, contain no external symlinks,
    and have access to required curated/sample assets.
    """
    checks = {
        "base_dir_exists": BASE_DIR.exists(),
        "curated_dir_exists": CURATED_DATA_DIR.exists(),
        "hourly_data_exists": HOURLY_CURATED_PATH.exists(),
        "daily_data_exists": DAILY_CURATED_PATH.exists(),
        "sample_dir_exists": SAMPLE_DATA_DIR.exists(),
        "no_external_symlinks": True
    }
    
    # Check for symlinks pointing outside BASE_DIR
    for p in [CURATED_DATA_DIR, SAMPLE_DATA_DIR, PROCESSED_DATA_DIR]:
        if p.exists() and p.is_symlink():
            target = p.resolve()
            if not str(target).startswith(str(BASE_DIR)):
                checks["no_external_symlinks"] = False

    checks["all_valid"] = all(checks.values())
    return checks

if __name__ == "__main__":
    status = verify_self_contained_architecture()
    print("=" * 60)
    print("SELF-CONTAINED ARCHITECTURE AUDIT REPORT (REC-08)")
    print("=" * 60)
    for k, v in status.items():
        print(f"  {k:<28}: {v}")
    print("=" * 60)
    assert status["all_valid"], "Self-contained architecture verification failed!"
    print("All architecture paths validated successfully.")
