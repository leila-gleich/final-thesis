import os
import subprocess
import zipfile
import csv
import random
import time
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SSOT_DIR = os.getenv("SSOT_DIR", os.path.join(os.path.dirname(REPO_ROOT), "SSOT"))
DEST_DIR = os.getenv("SSOT_DB1B_DIR", os.path.join(SSOT_DIR, "db1b"))
os.makedirs(DEST_DIR, exist_ok=True)

# 28 Quarters from 2019 Q1 to 2025 Q4
QUARTERS = []
for year in range(2019, 2026):
    for q in range(1, 5):
        QUARTERS.append((year, q))

def download_quarter(year, q):
    zip_name = f"Origin_and_Destination_Survey_DB1BMarket_{year}_{q}.zip"
    csv_name = f"Origin_and_Destination_Survey_DB1BMarket_{year}_{q}.csv"
    zip_path = os.path.join(DEST_DIR, zip_name)
    csv_path = os.path.join(DEST_DIR, csv_name)
    
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 1000000:
        print(f"[{year} Q{q}] CSV already exists ({os.path.getsize(csv_path)/(1024*1024):.1f} MB). Skipping.")
        return csv_path

    url = f"https://transtats.bts.gov/PREZIP/{zip_name}"
    print(f"[{year} Q{q}] Downloading from {url} ...")
    
    cmd = ["curl", "-L", "-s", "-S", "-o", zip_path, url]
    res = subprocess.run(cmd)
    if res.returncode != 0:
        print(f"[{year} Q{q}] Error downloading {url}")
        return None
        
    print(f"[{year} Q{q}] Unzipping {zip_name} ...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as zf:
            extracted_files = [f for f in zf.namelist() if f.endswith('.csv')]
            if extracted_files:
                zf.extract(extracted_files[0], DEST_DIR)
                extracted_path = os.path.join(DEST_DIR, extracted_files[0])
                if extracted_path != csv_path:
                    if os.path.exists(csv_path):
                        os.remove(csv_path)
                    os.rename(extracted_path, csv_path)
                print(f"[{year} Q{q}] Extracted {csv_path} ({os.path.getsize(csv_path)/(1024*1024):.1f} MB)")
                # Clean up zip to save disk space
                os.remove(zip_path)
                return csv_path
    except Exception as e:
        print(f"[{year} Q{q}] Error extracting zip: {e}")
        return None

if __name__ == "__main__":
    print(f"Starting batch download for {len(QUARTERS)} quarters...")
    for idx, (yr, qtr) in enumerate(QUARTERS, 1):
        print(f"\n--- Progress: [{idx}/{len(QUARTERS)}] Processing {yr} Q{qtr} ---")
        download_quarter(yr, qtr)
    print("\nAll downloads complete!")
