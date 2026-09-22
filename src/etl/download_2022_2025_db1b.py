import os
import subprocess
import zipfile
import sys
import time

DEST_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/Initial Repo/700b-data-warehouse/data/raw/db1b"
os.makedirs(DEST_DIR, exist_ok=True)

# Target periods: 2022 Q1-Q4, 2023 Q1-Q4, 2024 Q1-Q4, 2025 Q1-Q2 (Excluding 2025 Q3 and Q4)
TARGET_PERIODS = [
    (2022, 1), (2022, 2), (2022, 3), (2022, 4),
    (2023, 1), (2023, 2), (2023, 3), (2023, 4),
    (2024, 1), (2024, 2), (2024, 3), (2024, 4),
    (2025, 1), (2025, 2)
]

def download_and_extract(year, q):
    zip_name = f"Origin_and_Destination_Survey_DB1BMarket_{year}_{q}.zip"
    csv_name = f"Origin_and_Destination_Survey_DB1BMarket_{year}_{q}.csv"
    zip_path = os.path.join(DEST_DIR, zip_name)
    csv_path = os.path.join(DEST_DIR, csv_name)
    
    # Check if already downloaded and extracted
    if os.path.exists(csv_path) and os.path.getsize(csv_path) > 100000000:
        print(f"[{year} Q{q}] CSV already exists ({os.path.getsize(csv_path)/(1024*1024):.1f} MB). Skipping.")
        return True

    url = f"https://transtats.bts.gov/PREZIP/{zip_name}"
    print(f"\n[{year} Q{q}] Downloading {url} ...")
    
    # Use curl with retry and follow redirects
    cmd = ["curl", "-L", "-s", "-S", "--retry", "3", "-o", zip_path, url]
    res = subprocess.run(cmd)
    if res.returncode != 0 or not os.path.exists(zip_path) or os.path.getsize(zip_path) < 10000:
        print(f"[{year} Q{q}] FAILED download for {url}")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False
        
    print(f"[{year} Q{q}] Downloaded ({os.path.getsize(zip_path)/(1024*1024):.1f} MB). Unzipping...")
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
                print(f"[{year} Q{q}] Extracted {csv_name} ({os.path.getsize(csv_path)/(1024*1024):.1f} MB)")
                # Remove zip to conserve disk space
                os.remove(zip_path)
                return True
            else:
                print(f"[{year} Q{q}] No CSV found in zip.")
                return False
    except Exception as e:
        print(f"[{year} Q{q}] Error extracting zip: {e}")
        if os.path.exists(zip_path):
            os.remove(zip_path)
        return False

if __name__ == "__main__":
    total = len(TARGET_PERIODS)
    print(f"Starting batch download for DB1B Market data ({total} quarters total: 2022 Q1 - 2025 Q2)...")
    
    success_count = 0
    start_time = time.time()
    
    for idx, (yr, qtr) in enumerate(TARGET_PERIODS, 1):
        print(f"\n=======================================================")
        print(f"Progress: [{idx}/{total}] - Processing {yr} Q{qtr}")
        print(f"=======================================================")
        success = download_and_extract(yr, qtr)
        if success:
            success_count += 1
            
    elapsed = time.time() - start_time
    print(f"\n=======================================================")
    print(f"BATCH COMPLETE: {success_count}/{total} quarters successfully processed.")
    print(f"Total Elapsed Time: {elapsed/60:.2f} minutes")
    print(f"=======================================================")
