#!/usr/bin/env python3
"""
filter_top_20pct_airports.py

Filters tsav0.csv, otpv0.csv, and t100v0.csv in data/processed
to retain only the top 20th percentile (Top 78) commercial airport network.
"""

import os
import sys
import time
import shutil
import csv
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
DIM_DIR = os.path.join(BASE_DIR, "dimensions")

OTP_PATH = os.path.join(DATA_DIR, "otpv0.csv")
TSA_PATH = os.path.join(DATA_DIR, "tsav0.csv")
T100_PATH = os.path.join(DATA_DIR, "t100v0.csv")
DIM_AIRPORT_PATH = os.path.join(DIM_DIR, "dim_airport.csv")

def get_top_20pct_airports(n_top=78):
    print(f"[Step 1] Ranking airports by flight activity in {OTP_PATH}...")
    start = time.time()
    otp_dep = defaultdict(int)
    with open(OTP_PATH, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        oidx = header.index("originAirportId")
        count = 0
        for line in f:
            parts = line.strip().split(",")
            otp_dep[int(parts[oidx])] += 1
            count += 1
            if count % 10000000 == 0:
                print(f"  Scanned {count:,} OTP rows...")

    otp_sorted = sorted(otp_dep.items(), key=lambda x: x[1], reverse=True)
    top_airports = set(aid for aid, v in otp_sorted[:n_top])
    
    # Load metadata for display
    id2meta = {}
    with open(DIM_AIRPORT_PATH, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            id2meta[int(row["airportId"])] = row

    print(f"\nTop {n_top} Airports Identified in {time.time()-start:.2f}s:")
    for i, (aid, v) in enumerate(otp_sorted[:n_top], 1):
        meta = id2meta.get(aid, {})
        print(f"  {i:2d}. ID {aid:3d} ({meta.get('airportCode','???'):3s}) - {meta.get('airportName','???')[:30]:30s} | {v:>9,d} departures")

    return top_airports

def filter_otp(top_airports):
    print(f"\n[Step 2] Filtering OTP dataset ({OTP_PATH})...")
    start = time.time()
    tmp_path = OTP_PATH + ".tmp"
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(OTP_PATH, "r", encoding="utf-8") as fin, open(tmp_path, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        oidx = col_names.index("originAirportId")
        didx = col_names.index("destAirportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            orig = int(parts[oidx])
            dest = int(parts[didx])

            if orig in top_airports and dest in top_airports:
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

            if total_rows % 10000000 == 0:
                print(f"  Processed {total_rows:,} OTP rows (kept {kept_rows:,})...")

    shutil.move(tmp_path, OTP_PATH)
    elapsed = time.time() - start
    print(f"  OTP Filtering Complete in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def filter_tsa(top_airports):
    print(f"\n[Step 3] Filtering TSA dataset ({TSA_PATH})...")
    start = time.time()
    tmp_path = TSA_PATH + ".tmp"
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(TSA_PATH, "r", encoding="utf-8") as fin, open(tmp_path, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        aidx = col_names.index("airportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            aid = int(parts[aidx])

            if aid in top_airports:
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

            if total_rows % 5000000 == 0:
                print(f"  Processed {total_rows:,} TSA rows (kept {kept_rows:,})...")

    shutil.move(tmp_path, TSA_PATH)
    elapsed = time.time() - start
    print(f"  TSA Filtering Complete in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def filter_t100(top_airports):
    print(f"\n[Step 4] Filtering T-100 dataset ({T100_PATH})...")
    start = time.time()
    tmp_path = T100_PATH + ".tmp"
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(T100_PATH, "r", encoding="utf-8") as fin, open(tmp_path, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        oidx = col_names.index("originAirportId")
        didx = col_names.index("destAirportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            orig = int(parts[oidx])
            dest = int(parts[didx])

            if orig in top_airports and dest in top_airports:
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

    shutil.move(tmp_path, T100_PATH)
    elapsed = time.time() - start
    print(f"  T-100 Filtering Complete in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def main():
    print("=" * 80)
    print("FILTERING ALL DATASETS TO TOP 20th PERCENTILE (TOP 78 AIRPORTS)")
    print("=" * 80)
    top_airports = get_top_20pct_airports(n_top=78)
    filter_otp(top_airports)
    filter_tsa(top_airports)
    filter_t100(top_airports)
    print("\n" + "=" * 80)
    print("TOP 20th PERCENTILE FILTERING COMPLETED SUCCESSFULLY!")
    print("=" * 80)

if __name__ == "__main__":
    main()
