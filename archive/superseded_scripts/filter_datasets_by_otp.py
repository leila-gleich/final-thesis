#!/usr/bin/env python3
"""
filter_datasets_by_otp.py

Filters tsav0.csv and t100v0.csv in data/processed to strictly contain
airports that exist in otpv0.csv (originAirportId OR destAirportId).
"""

import os
import sys
import time
import shutil

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

OTP_PATH = os.path.join(DATA_DIR, "otpv0.csv")
TSA_PATH = os.path.join(DATA_DIR, "tsav0.csv")
T100_PATH = os.path.join(DATA_DIR, "t100v0.csv")

def get_otp_airports():
    print(f"[Step 1] Extracting distinct airport set from {OTP_PATH}...")
    start = time.time()
    otp_airports = set()
    total_rows = 0
    with open(OTP_PATH, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        oidx = header.index("originAirportId")
        didx = header.index("destAirportId")
        for line in f:
            total_rows += 1
            parts = line.strip().split(",")
            otp_airports.add(int(parts[oidx]))
            otp_airports.add(int(parts[didx]))
            if total_rows % 10000000 == 0:
                print(f"  Processed {total_rows:,} OTP rows...")
    print(f"  Extracted {len(otp_airports)} distinct airports from {total_rows:,} OTP rows in {time.time()-start:.2f}s.")
    return otp_airports

def filter_tsa(otp_airports):
    print(f"\n[Step 2] Filtering TSA dataset ({TSA_PATH})...")
    start = time.time()
    tmp_path = TSA_PATH + ".tmp"
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0
    airports_before = set()
    airports_after = set()

    with open(TSA_PATH, "r", encoding="utf-8") as fin, open(tmp_path, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        aidx = col_names.index("airportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            aid = int(parts[aidx])
            airports_before.add(aid)
            if aid in otp_airports:
                fout.write(line)
                kept_rows += 1
                airports_after.add(aid)
            else:
                dropped_rows += 1
            if total_rows % 5000000 == 0:
                print(f"  Processed {total_rows:,} TSA rows (kept {kept_rows:,})...")

    # Replace file atomically
    shutil.move(tmp_path, TSA_PATH)
    elapsed = time.time() - start
    print(f"  TSA Filtering Complete in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")
    print(f"    - Airports before: {len(airports_before)}")
    print(f"    - Airports after : {len(airports_after)}")
    print(f"    - Airports removed: {len(airports_before - airports_after)}")

def filter_t100(otp_airports):
    print(f"\n[Step 3] Filtering T-100 dataset ({T100_PATH})...")
    start = time.time()
    tmp_path = T100_PATH + ".tmp"
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0
    airports_before = set()
    airports_after = set()

    with open(T100_PATH, "r", encoding="utf-8") as fin, open(tmp_path, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        oidx = col_names.index("originAirportId")
        didx = col_names.index("destAirportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            o = int(parts[oidx])
            d = int(parts[didx])
            airports_before.add(o)
            airports_before.add(d)

            if o in otp_airports and d in otp_airports:
                fout.write(line)
                kept_rows += 1
                airports_after.add(o)
                airports_after.add(d)
            else:
                dropped_rows += 1

    # Replace file atomically
    shutil.move(tmp_path, T100_PATH)
    elapsed = time.time() - start
    print(f"  T-100 Filtering Complete in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")
    print(f"    - Airports before: {len(airports_before)}")
    print(f"    - Airports after : {len(airports_after)}")
    print(f"    - Airports removed: {len(airports_before - airports_after)}")

def main():
    print("=" * 80)
    print("FILTERING DATASETS TO MATCH OTP AIRPORT SET")
    print("=" * 80)
    otp_airports = get_otp_airports()
    filter_tsa(otp_airports)
    filter_t100(otp_airports)
    print("\n" + "=" * 80)
    print("ALL DATASETS SUCCESSFULLY FILTERED AND ALIGNED WITH OTP AIRPORTS!")
    print("=" * 80)

if __name__ == "__main__":
    main()
