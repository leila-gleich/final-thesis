import os
import csv
import random
import zipfile

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SSOT_DIR = os.getenv("SSOT_DIR", os.path.join(os.path.dirname(REPO_ROOT), "SSOT"))
DEST_DIR = os.getenv("SSOT_DB1B_DIR", os.path.join(SSOT_DIR, "db1b"))

def profile_and_sample():
    # Look for any csv in DEST_DIR or unzip test_2019_1.zip if needed
    csv_files = [os.path.join(DEST_DIR, f) for f in os.listdir(DEST_DIR) if f.endswith('.csv')]
    
    if not csv_files:
        zip_files = [os.path.join(DEST_DIR, f) for f in os.listdir(DEST_DIR) if f.endswith('.zip')]
        if zip_files:
            zpath = zip_files[0]
            print(f"Unzipping {zpath} ...")
            with zipfile.ZipFile(zpath, 'r') as zf:
                cfiles = [f for f in zf.namelist() if f.endswith('.csv')]
                if cfiles:
                    zf.extract(cfiles[0], DEST_DIR)
                    extracted = os.path.join(DEST_DIR, cfiles[0])
                    renamed = os.path.join(DEST_DIR, 'Origin_and_Destination_Survey_DB1BMarket_2019_1.csv')
                    if os.path.exists(renamed): os.remove(renamed)
                    os.rename(extracted, renamed)
                    csv_files = [renamed]

    if not csv_files:
        print("No CSV files found to profile.")
        return

    target_csv = csv_files[0]
    print(f"\n=======================================================")
    print(f"DATABASE PROFILE: {os.path.basename(target_csv)}")
    print(f"File Size: {os.path.getsize(target_csv)/(1024*1024):.2f} MB")
    print(f"=======================================================\n")

    # Read header and first 1000 rows to sample & detect data types
    rows_reservoir = []
    total_rows = 0
    header = []
    
    with open(target_csv, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.reader(f)
        header = next(reader)
        # reservoir sampling for 20 random rows
        for idx, row in enumerate(reader):
            total_rows += 1
            if len(rows_reservoir) < 20:
                rows_reservoir.append(row)
            else:
                # Random replacement
                j = random.randint(0, total_rows - 1)
                if j < 20:
                    rows_reservoir[j] = row

    print(f"Total Rows in File: {total_rows:,}")
    print(f"Total Columns: {len(header)}\n")
    
    print("--- SCHEMA DEFINITION (Column Name & Index) ---")
    for i, col in enumerate(header):
        print(f"[{i:02d}] {col}")
        
    print("\n--- SAMPLE 20 RANDOM ROWS ---")
    # Clean empty trailing comma columns
    clean_header = [c.strip() for c in header if c.strip()]
    num_cols = len(clean_header)
    
    for r_idx, sample_row in enumerate(rows_reservoir, 1):
        print(f"\n[Sample Row {r_idx:02d}]:")
        for col_name, val in zip(clean_header, sample_row[:num_cols]):
            if val.strip():
                print(f"  {col_name}: {val}")

if __name__ == "__main__":
    profile_and_sample()
