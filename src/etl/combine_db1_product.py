import os
import sys
import glob
import zipfile
import csv
import io
import time

DB1C_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/d1b1 OD/DB1C folders"
OUTPUT_DIR = "/Users/leilagleich/Library/CloudStorage/OneDrive-Embry-RiddleAeronauticalUniversity/d1b1 OD"
OUTPUT_CSV = os.path.join(OUTPUT_DIR, "DB1_Product_2022_2025.csv")

HEADERS = [
    "Year", "Quarter", "Month", "RPCarrier", "Passengers", "TotalFare", "TaxAmt", "DollarCred", "PurWinGrp",
    "RoundTrip", "Coupons", "Origin", "Routing",
    "Dest_1", "OpCarrier_1", "TkCarrier_1", "FareClass_1",
    "Dest_2", "OpCarrier_2", "TkCarrier_2", "FareClass_2",
    "Dest_3", "OpCarrier_3", "TkCarrier_3", "FareClass_3",
    "Dest_4", "OpCarrier_4", "TkCarrier_4", "FareClass_4",
    "Dest_5", "OpCarrier_5", "TkCarrier_5", "FareClass_5",
    "Dest_6", "OpCarrier_6", "TkCarrier_6", "FareClass_6"
]

def parse_db1b_asc_line(line):
    """
    Parses a single line from a DB1B .asc pipe-delimited file.
    """
    parts = line.strip().split('|')
    if len(parts) < 21:
        return None
        
    fare = parts[0]
    rp_carrier = parts[1]
    yq = parts[2]
    rt = parts[3]
    pax = parts[4]
    orig = parts[5]
    
    yr = yq[:4] if len(yq) >= 4 else ""
    qtr = yq[4:] if len(yq) >= 5 else ""
    
    num_coupons = (len(parts) - 10) // 11
    if num_coupons < 1:
        return None
        
    routing_apts = [orig]
    leg_data = []
    
    for c in range(num_coupons):
        idx = 10 + c * 11
        op_carrier = parts[idx]
        tk_carrier = parts[idx + 2]
        fare_class = parts[idx + 4]
        dest = parts[idx + 6]
        
        routing_apts.append(dest)
            
        if c < 6:
            leg_data.extend([dest, op_carrier, tk_carrier, fare_class])
            
    # Pad leg_data to 6 legs (6 * 4 = 24 values)
    while len(leg_data) < 24:
        leg_data.append("")
        
    routing_str = ":".join(routing_apts)
    
    row = [
        yr, qtr, "", rp_carrier, pax, fare, "", "", "",
        rt, str(num_coupons), orig, routing_str
    ] + leg_data
    
    return row

def parse_db1c_csv_row(row_dict):
    """
    Parses a single row dictionary from a DB1C .csv file.
    """
    rp_carrier = row_dict.get("RpCarrier", "")
    yr = row_dict.get("RpYear", "")
    mo = row_dict.get("RpMonth", "")
    qtr = str((int(mo) - 1) // 3 + 1) if mo.isdigit() else ""
    
    coupons_str = row_dict.get("CouponSeg", "1")
    try:
        num_coupons = int(coupons_str)
    except ValueError:
        num_coupons = 1
        
    total_amt = row_dict.get("TotalAmt", "")
    tax_amt = row_dict.get("TaxAmt", "")
    dollar_cred = row_dict.get("DollarCred", "")
    num_pax = row_dict.get("NumPax", "")
    pur_win_grp = row_dict.get("PurWinGrp", "")
    
    orig = row_dict.get("Apt_1", "")
    final_dest = row_dict.get(f"Apt_{num_coupons + 1}", "")
    
    routing_apts = [orig]
    leg_data = []
    
    for c in range(1, num_coupons + 1):
        next_apt = row_dict.get(f"Apt_{c + 1}", "")
        if next_apt:
            routing_apts.append(next_apt)
            
        if c <= 6:
            op_carrier = row_dict.get(f"OpCarrier_{c}", "")
            mkt_carrier = row_dict.get(f"MktCarrier_{c}", "")
            leg_data.extend([next_apt, op_carrier, mkt_carrier, ""])
            
    while len(leg_data) < 24:
        leg_data.append("")
        
    routing_str = ":".join(routing_apts)
    
    # Infer roundtrip if origin == final_dest
    rt = "2" if orig and final_dest and orig == final_dest else "1"
    
    row = [
        yr, qtr, mo, rp_carrier, num_pax, total_amt, tax_amt, dollar_cred, pur_win_grp,
        rt, str(num_coupons), orig, routing_str
    ] + leg_data
    
    return row

def main():
    print("=================================================================")
    print("STARTING COMBINED DB1 PRODUCT / MARKET DATASET ETL (2022 - 2025)")
    print(f"Target Output: {OUTPUT_CSV}")
    print("=================================================================\n")
    
    t_start = time.time()
    total_records = 0
    
    # Identify all DB1B .asc files
    asc_files = sorted(glob.glob(os.path.join(DB1C_DIR, "DB1B_*.asc")))
    # Identify all DB1C monthly folders
    subfolders = sorted([d for d in os.listdir(DB1C_DIR) if d.startswith("DB1C_25-") and os.path.isdir(os.path.join(DB1C_DIR, d))])
    
    with open(OUTPUT_CSV, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(HEADERS)
        
        # 1. Process DB1B .asc files
        for asc_path in asc_files:
            file_name = os.path.basename(asc_path)
            print(f"Processing DB1B: {file_name} ...")
            t_file = time.time()
            count = 0
            with open(asc_path, "r", encoding="utf-8", errors="ignore") as f:
                for line in f:
                    row = parse_db1b_asc_line(line)
                    if row:
                        writer.writerow(row)
                        count += 1
                        total_records += 1
            elapsed = time.time() - t_file
            print(f"  ✓ {file_name}: {count:,} records written ({elapsed:.1f}s)")
            
        # 2. Process DB1C monthly subfolders
        for folder in subfolders:
            fpath = os.path.join(DB1C_DIR, folder)
            csv_zips = glob.glob(os.path.join(fpath, "*.csv.zip"))
            if not csv_zips:
                continue
            zip_path = csv_zips[0]
            file_name = os.path.basename(zip_path)
            print(f"Processing DB1C: {folder}/{file_name} ...")
            t_file = time.time()
            count = 0
            with zipfile.ZipFile(zip_path) as z:
                member_name = z.namelist()[0]
                with z.open(member_name) as f:
                    text_stream = io.TextIOWrapper(f, encoding="utf-8", errors="ignore")
                    reader = csv.DictReader(text_stream)
                    for row_dict in reader:
                        row = parse_db1c_csv_row(row_dict)
                        if row:
                            writer.writerow(row)
                            count += 1
                            total_records += 1
            elapsed = time.time() - t_file
            print(f"  ✓ {folder}: {count:,} records written ({elapsed:.1f}s)")
            
    total_elapsed = time.time() - t_start
    size_mb = os.path.getsize(OUTPUT_CSV) / (1024 * 1024)
    print("\n=================================================================")
    print("ETL COMPLETE!")
    print(f"Output File: {OUTPUT_CSV}")
    print(f"Total Rows: {total_records:,}")
    print(f"File Size: {size_mb:.2f} MB ({size_mb/1024:.2f} GB)")
    print(f"Total Time: {total_elapsed/60:.2f} minutes")
    print("=================================================================")

if __name__ == "__main__":
    main()
