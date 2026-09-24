import os
import sys
import subprocess
import zipfile
import csv
import io
import time
import glob

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), "data")
RAW_COUPON_DIR = os.path.join(DATA_DIR, "raw", "coupon")
os.makedirs(RAW_COUPON_DIR, exist_ok=True)

def process_coupon_zip(zip_path, output_csv_path=None):
    """
    Streams a Coupon ZIP archive (either DB1B quarterly or DB1C monthly),
    standardizes headers, cleans trailing commas, and exports clean CSV.
    """
    if output_csv_path is None:
        base_name = os.path.splitext(os.path.basename(zip_path))[0]
        output_csv_path = os.path.join(RAW_COUPON_DIR, f"{base_name}.csv")
        
    print(f"\n===========================================================")
    print(f"PROCESSING COUPON ARCHIVE: {os.path.basename(zip_path)}")
    print(f"===========================================================")
    
    t0 = time.time()
    with zipfile.ZipFile(zip_path, 'r') as zf:
        csv_members = [f for f in zf.namelist() if f.endswith('.csv') or f.endswith('.txt') or f.endswith('.dat')]
        if not csv_members:
            print(f"Error: No data file found in {zip_path}")
            return None
            
        target_file = csv_members[0]
        uncompressed_mb = zf.getinfo(target_file).file_size / (1024 * 1024)
        print(f"Reading stream from: {target_file} (~{uncompressed_mb:.2f} MB uncompressed)")
        
        with zf.open(target_file, 'r') as raw_file, \
             open(output_csv_path, 'w', encoding='utf-8', newline='') as outfile:
             
            text_stream = io.TextIOWrapper(raw_file, encoding='utf-8', errors='ignore')
            reader = csv.reader(text_stream)
            writer = csv.writer(outfile)
            
            raw_header = next(reader)
            clean_headers = [col.strip() for col in raw_header if col.strip()]
            num_fields = len(clean_headers)
            writer.writerow(clean_headers)
            
            row_count = 0
            for row in reader:
                row_count += 1
                clean_row = [val.strip() for val in row[:num_fields]]
                writer.writerow(clean_row)
                if row_count % 1000000 == 0:
                    print(f"   Processed {row_count:,} coupon rows...")
                    
    elapsed = time.time() - t0
    out_size_mb = os.path.getsize(output_csv_path) / (1024 * 1024)
    print(f"✓ Output saved: {output_csv_path} ({out_size_mb:.2f} MB)")
    print(f"✓ Total records: {row_count:,} | Columns: {len(clean_headers)} | Time: {elapsed:.1f}s")
    return output_csv_path

def download_and_process_transtats_coupon(year, quarter):
    """
    Downloads and converts pre-July 2025 quarterly coupon data from BTS TranStats.
    """
    zip_name = f"Origin_and_Destination_Survey_DB1BCoupon_{year}_{quarter}.zip"
    zip_path = os.path.join(RAW_COUPON_DIR, zip_name)
    url = f"https://transtats.bts.gov/PREZIP/{zip_name}"
    
    if not os.path.exists(zip_path) or os.path.getsize(zip_path) < 10000000:
        print(f"\nDownloading {url} ...")
        cmd = ["curl", "-L", "-s", "-S", "--retry", "3", "-o", zip_path, url]
        res = subprocess.run(cmd)
        if res.returncode != 0:
            print(f"Download failed for {url}")
            return None
            
    return process_coupon_zip(zip_path)

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].endswith('.zip'):
        # Process a specific local ZIP file (e.g. downloaded from BTS DB1C page)
        process_coupon_zip(sys.argv[1])
    else:
        # Download and process 2025 Q1 and Q2
        download_and_process_transtats_coupon(2025, 1)
        download_and_process_transtats_coupon(2025, 2)
