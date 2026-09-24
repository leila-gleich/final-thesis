import os
import sys
import glob
import time
import csv
import io
import duckdb
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
_DEFAULT_LOCAL_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/d1b1 OD/DB1C folders"
DB1C_DIR = os.getenv(
    "DB1C_DIR",
    _DEFAULT_LOCAL_DIR if os.path.exists(_DEFAULT_LOCAL_DIR) else os.path.join(REPO_ROOT, "data", "raw", "db1c")
)

def combine_db1c_coupon():
    """
    Combines all DB1C monthly Coupon parquet files (2025-07 through 2025-12)
    into unified master DB1C_coupon_25-25.parquet and DB1C_coupon_25-25.csv.
    """
    print("\n" + "=" * 70)
    print("STAGE 1: COMBINING DB1C COUPON DATASETS (2025-07 to 2025-12)")
    print("=" * 70)
    
    t0 = time.time()
    con = duckdb.connect()
    
    parquet_pattern = os.path.join(DB1C_DIR, "DB1C_Coupon_25-*", "DB1C_Coupon_25-*.parquet")
    out_parquet = os.path.join(DB1C_DIR, "DB1C_coupon_25-25.parquet")
    out_csv = os.path.join(DB1C_DIR, "DB1C_coupon_25-25.csv")
    
    print(f"Reading from pattern: {parquet_pattern}")
    
    # 1. Export Parquet
    print(f"Exporting combined Parquet to: {out_parquet} ...")
    t_pq = time.time()
    con.execute(f"""
        COPY (
            SELECT * FROM '{parquet_pattern}'
            ORDER BY RpYear, RpMonth, ItinID, SeqNum
        ) TO '{out_parquet}' (FORMAT PARQUET, COMPRESSION 'ZSTD')
    """)
    pq_size_mb = os.path.getsize(out_parquet) / (1024 * 1024)
    print(f"✓ Created {out_parquet} ({pq_size_mb:,.1f} MB) in {time.time() - t_pq:.1f}s")
    
    # 2. Export CSV
    print(f"Exporting combined CSV to: {out_csv} ...")
    t_csv = time.time()
    con.execute(f"""
        COPY (
            SELECT * FROM '{out_parquet}'
        ) TO '{out_csv}' (HEADER, DELIMITER ',')
    """)
    csv_size_mb = os.path.getsize(out_csv) / (1024 * 1024)
    print(f"✓ Created {out_csv} ({csv_size_mb:,.1f} MB / {csv_size_mb/1024:,.2f} GB) in {time.time() - t_csv:.1f}s")
    
    row_count = con.execute(f"SELECT count(*) FROM '{out_parquet}'").fetchone()[0]
    print(f"✓ Total DB1C Coupon Rows: {row_count:,} | Total Stage 1 Time: {time.time() - t0:.1f}s")
    return row_count

def parse_asc_to_db1c_row(line):
    """
    Parses a single line from a historical pipe-delimited DB1B .asc file
    into the standardized 288-column DB1C schema.
    """
    parts = line.rstrip('\r\n').split('|')
    if len(parts) < 21:
        return None
        
    row = [''] * 288
    
    total_amt = parts[0]
    rp_carrier = parts[1]
    yq = parts[2]
    num_coupons = int(parts[3])
    num_pax = parts[4]
    apt_1 = parts[5]
    via_apt_1 = parts[6]
    city_mkt_1 = parts[7]
    dollar_cred = parts[8]
    wac_1 = parts[9]
    
    yr = yq[:4] if len(yq) >= 4 else ''
    
    row[0] = rp_carrier         # RpCarrier
    row[1] = yr                 # RpYear
    row[2] = ''                 # RpMonth
    row[3] = str(num_coupons)   # CouponSeg
    row[4] = rp_carrier         # IssueCarrier
    row[5] = total_amt          # TotalAmt
    row[6] = ''                 # TaxAmt
    row[7] = dollar_cred        # DollarCred
    row[8] = num_pax            # NumPax
    row[9] = ''                 # PurWinGrp
    
    row[10] = yr                # SchFlYr_1
    row[11] = ''                # SchFlMo_1
    row[12] = apt_1             # Apt_1
    row[13] = wac_1             # WAC_1
    row[14] = city_mkt_1        # CityMktID_1
    row[15] = via_apt_1         # ViaApt_1
    
    for c in range(1, num_coupons + 1):
        idx = 10 + (c - 1) * 11
        if idx + 10 >= len(parts):
            break
        op_carrier = parts[idx]
        op_class = parts[idx + 1]
        mkt_carrier = parts[idx + 2]
        mkt_class = parts[idx + 3]
        trip_bk1 = parts[idx + 4]
        dist = parts[idx + 5]
        dest_apt = parts[idx + 6]
        trip_bk2 = parts[idx + 7]
        dest_city_mkt = parts[idx + 8]
        dest_via = parts[idx + 9]
        dest_wac = parts[idx + 10]
        
        if c == 1:
            row[16] = op_carrier   # OpCarrier_1
            row[17] = mkt_carrier  # MktCarrier_1
            
        k = c + 1
        if k <= 23:
            base_k = 18 + (k - 2) * 12
            row[base_k] = yr
            row[base_k + 1] = ''
            row[base_k + 2] = dest_apt
            row[base_k + 3] = dist
            row[base_k + 4] = ''
            row[base_k + 5] = trip_bk1
            row[base_k + 6] = trip_bk2
            row[base_k + 7] = dest_city_mkt
            row[base_k + 8] = dest_wac
            row[base_k + 9] = dest_via
            if c < num_coupons:
                next_idx = 10 + c * 11
                if next_idx + 2 < len(parts):
                    row[base_k + 10] = parts[next_idx]     # OpCarrier_k
                    row[base_k + 11] = parts[next_idx + 2] # MktCarrier_k
                    
    return row

def combine_db1c_master():
    """
    Combines historical DB1B .asc files (2022-2025 Q2) and DB1C monthly parquet files (2025-07 to 2025-12)
    into unified master DB1C_22-25.csv and DB1C_22-25.parquet.
    """
    print("\n" + "=" * 70)
    print("STAGE 2: COMBINING DB1C DATASETS (2022 to 2025)")
    print("=" * 70)
    
    t0 = time.time()
    con = duckdb.connect()
    
    sample_pq = glob.glob(os.path.join(DB1C_DIR, "DB1C_25-7", "*.parquet"))[0]
    headers = [c[0] for c in con.execute(f"DESCRIBE SELECT * FROM '{sample_pq}'").fetchall()]
    print(f"Target DB1C schema contains {len(headers)} columns.")
    
    out_csv = os.path.join(DB1C_DIR, "DB1C_22-25.csv")
    out_parquet = os.path.join(DB1C_DIR, "DB1C_22-25.parquet")
    
    asc_files = sorted(glob.glob(os.path.join(DB1C_DIR, "DB1B_*.asc")))
    db1c_folders = sorted([
        d for d in os.listdir(DB1C_DIR)
        if d.startswith("DB1C_25-") and os.path.isdir(os.path.join(DB1C_DIR, d)) and "Coupon" not in d
    ])
    
    total_asc_rows = 0
    total_db1c_rows = 0
    
    with open(out_csv, 'w', encoding='utf-8', newline='') as out_fp:
        writer = csv.writer(out_fp)
        writer.writerow(headers)
        
        # 1. Stream ASC files
        print("\n--- Processing Historical DB1B ASC Files (2022 Q1 - 2025 Q2) ---")
        for asc_path in asc_files:
            fname = os.path.basename(asc_path)
            t_f = time.time()
            cnt = 0
            with open(asc_path, 'r', encoding='utf-8', errors='ignore') as f_in:
                for line in f_in:
                    row = parse_asc_to_db1c_row(line)
                    if row:
                        writer.writerow(row)
                        cnt += 1
            total_asc_rows += cnt
            print(f"  ✓ {fname}: {cnt:,} rows written ({time.time() - t_f:.1f}s)")
            
        # 2. Stream DB1C monthly files
        print("\n--- Processing Monthly DB1C Folders (2025 M7 - 2025 M12) ---")
        for folder in db1c_folders:
            folder_path = os.path.join(DB1C_DIR, folder)
            pq_files = glob.glob(os.path.join(folder_path, "*.parquet"))
            if not pq_files:
                continue
            pq_path = pq_files[0]
            fname = os.path.basename(pq_path)
            t_f = time.time()
            
            cnt = 0
            cursor = con.cursor()
            cursor.execute(f"SELECT * FROM '{pq_path}'")
            while True:
                chunk = cursor.fetchmany(100000)
                if not chunk:
                    break
                for row_tuple in chunk:
                    clean_row = [str(x) if x is not None else '' for x in row_tuple]
                    writer.writerow(clean_row)
                    cnt += 1
            total_db1c_rows += cnt
            print(f"  ✓ {folder}/{fname}: {cnt:,} rows written ({time.time() - t_f:.1f}s)")
            
    csv_size_mb = os.path.getsize(out_csv) / (1024 * 1024)
    print(f"\n✓ Created {out_csv} ({csv_size_mb:,.1f} MB / {csv_size_mb/1024:,.2f} GB)")
    print(f"  Total Historical ASC rows: {total_asc_rows:,}")
    print(f"  Total Monthly DB1C rows:   {total_db1c_rows:,}")
    print(f"  Total DB1C Master rows:    {total_asc_rows + total_db1c_rows:,}")
    
    # 3. Create Parquet version for ultrafast analysis
    print(f"\nCreating compressed Parquet: {out_parquet} ...")
    t_pq = time.time()
    con.execute(f"""
        COPY (
            SELECT * FROM read_csv('{out_csv}', header=true, all_varchar=true)
        ) TO '{out_parquet}' (FORMAT PARQUET, COMPRESSION 'ZSTD')
    """)
    pq_size_mb = os.path.getsize(out_parquet) / (1024 * 1024)
    print(f"✓ Created {out_parquet} ({pq_size_mb:,.1f} MB / {pq_size_mb/1024:,.2f} GB) in {time.time() - t_pq:.1f}s")
    print(f"✓ Total Stage 2 Time: {time.time() - t0:.1f}s")
    return total_asc_rows + total_db1c_rows

def main():
    start_time = time.time()
    print("=======================================================================")
    print("STARTING COMPLETE DB1C & DB1C COUPON MASTER DATASET PIPELINE")
    print(f"Directory: {DB1C_DIR}")
    print("=======================================================================")
    
    coupon_rows = combine_db1c_coupon()
    db1c_rows = combine_db1c_master()
    
    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print("ALL PIPELINE STAGES COMPLETE!")
    print(f"✓ DB1C Coupon Master: {coupon_rows:,} rows")
    print(f"✓ DB1C Itinerary Master: {db1c_rows:,} rows")
    print(f"✓ Total Execution Time: {elapsed/60:.2f} minutes")
    print("=" * 70)

if __name__ == "__main__":
    main()
