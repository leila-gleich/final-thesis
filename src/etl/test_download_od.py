import os
import sys
import subprocess
import zipfile
import csv
import io
import time

def download_and_process_od(table_type="DB1BMarket", year=2024, quarter=1, output_dir=None):
    """
    Downloads a BTS O&D Survey quarter, streams directly from the zip archive,
    standardizes headers, removes trailing delimiter artifacts, and outputs a clean CSV.
    """
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 
                                  "data", "raw", "db1b_test")
    os.makedirs(output_dir, exist_ok=True)
    
    zip_name = f"Origin_and_Destination_Survey_{table_type}_{year}_{quarter}.zip"
    clean_csv_name = f"Origin_and_Destination_Survey_{table_type}_{year}_{quarter}.csv"
    
    zip_path = os.path.join(output_dir, zip_name)
    clean_csv_path = os.path.join(output_dir, clean_csv_name)
    
    url = f"https://transtats.bts.gov/PREZIP/{zip_name}"
    print(f"===========================================================")
    print(f"1. DOWNLOADING / VERIFYING: {table_type} {year} Q{quarter}")
    print(f"   Source URL: {url}")
    print(f"===========================================================")
    
    if not (os.path.exists(zip_path) and os.path.getsize(zip_path) > 10000000):
        t0 = time.time()
        cmd = ["curl", "-L", "-s", "-S", "--retry", "3", "-o", zip_path, url]
        res = subprocess.run(cmd)
        if res.returncode != 0 or not os.path.exists(zip_path) or os.path.getsize(zip_path) < 10000:
            print(f"Error: Failed to download from {url}")
            return None
        download_size_mb = os.path.getsize(zip_path) / (1024 * 1024)
        print(f"✓ Download complete: {download_size_mb:.2f} MB in {time.time() - t0:.1f}s")
    else:
        print(f"✓ ZIP archive already downloaded ({os.path.getsize(zip_path)/(1024*1024):.2f} MB)")
        
    print(f"\n2. STREAMING & CONVERTING CSV WITH STANDARDIZED HEADERS...")
    t_start = time.time()
    
    with zipfile.ZipFile(zip_path, 'r') as zf:
        csv_members = [f for f in zf.namelist() if f.endswith('.csv')]
        if not csv_members:
            print("Error: No CSV file found in downloaded zip archive.")
            return None
            
        target_csv_member = csv_members[0]
        print(f"   Reading stream from: {target_csv_member} (Uncompressed: ~{zf.getinfo(target_csv_member).file_size/(1024*1024):.2f} MB)")
        
        with zf.open(target_csv_member, 'r') as raw_file, \
             open(clean_csv_path, 'w', encoding='utf-8', newline='') as outfile:
            
            text_stream = io.TextIOWrapper(raw_file, encoding='utf-8', errors='ignore')
            reader = csv.reader(text_stream)
            writer = csv.writer(outfile)
            
            raw_header = next(reader)
            # Remove trailing empty column caused by BTS line-ending comma
            clean_headers = [col.strip() for col in raw_header if col.strip()]
            num_fields = len(clean_headers)
            
            writer.writerow(clean_headers)
            
            row_count = 0
            for row in reader:
                row_count += 1
                clean_row = [val.strip() for val in row[:num_fields]]
                writer.writerow(clean_row)
                if row_count % 1000000 == 0:
                    print(f"   Processed {row_count:,} records...")

    clean_size_mb = os.path.getsize(clean_csv_path) / (1024 * 1024)
    elapsed = time.time() - t_start
    print(f"\n===========================================================")
    print(f"✓ CONVERSION COMPLETE: {clean_csv_name}")
    print(f"✓ File Size: {clean_size_mb:.2f} MB")
    print(f"✓ Total Records: {row_count:,}")
    print(f"✓ Total Columns: {len(clean_headers)}")
    print(f"✓ Elapsed Processing Time: {elapsed:.1f}s")
    print(f"===========================================================")
    
    print(f"\n--- STANDARDIZED HEADERS ({len(clean_headers)} columns) ---")
    for i, col in enumerate(clean_headers, 1):
        print(f"  [{i:02d}] {col}")
        
    print(f"\n--- SAMPLE RECORD ---")
    with open(clean_csv_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)
        sample = next(reader)
        for h, val in zip(header, sample):
            print(f"  {h}: {val}")
            
    return clean_csv_path

if __name__ == "__main__":
    table = sys.argv[1] if len(sys.argv) > 1 else "DB1BMarket"
    yr = int(sys.argv[2]) if len(sys.argv) > 2 else 2024
    qtr = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    download_and_process_od(table_type=table, year=yr, quarter=qtr)
