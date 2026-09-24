#!/usr/bin/env python3
"""
generate_v1_datasets.py

Master ETL pipeline to generate v1 datasets across all 4 data warehouse feeds:
1. otpv1.csv & otpv1.parquet (BTS On-Time Performance)
2. tsav1.csv & tsav1.parquet (TSA Checkpoint Throughput)
3. t100v1.csv & t100v1.parquet (BTS T-100 Segment Capacity)
4. db1v1.csv & db1v1.parquet (BTS DB1B Market Fares - Normalized with dim_market)
5. dim_market.csv (Conformed City-Pair Market Dimension)

Methodology & Filtering Constraints:
- Active Airlines (Top 7 Tier): AA (2), AS (3), B6 (4), DL (5), OO (13), UA (15), WN (16)
- Active Airports: 187 airports with commercial service from American (AA), United (UA), or Delta (DL)
- City-Pair Markets: Normalized into dim_market.csv with conformed marketId surrogate keys
- Quarter Elimination: Quarter field dropped; month populated as quarter-start month (1, 4, 7, 10)
"""

import os
import sys
import time
import shutil
import csv
import duckdb

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DATA_DIR = os.path.join(BASE_DIR, "data", "processed")
ARCHIVE_V0_DIR = os.path.join(DATA_DIR, "archive", "v0")
DIM_DIR = os.path.join(BASE_DIR, "dimensions")

# Input v0 paths (from archive/v0)
OTP_V0 = os.path.join(ARCHIVE_V0_DIR, "otpv0.csv")
TSA_V0 = os.path.join(ARCHIVE_V0_DIR, "tsav0.csv")
T100_V0 = os.path.join(ARCHIVE_V0_DIR, "t100v0.csv")
DB1_V0 = os.path.join(ARCHIVE_V0_DIR, "db1v0.csv")

# Output v1 paths
OTP_V1 = os.path.join(DATA_DIR, "otpv1.csv")
TSA_V1 = os.path.join(DATA_DIR, "tsav1.csv")
T100_V1 = os.path.join(DATA_DIR, "t100v1.csv")
DB1_V1 = os.path.join(DATA_DIR, "db1v1.csv")

# Dimensions
DIM_AIRPORT_PATH = os.path.join(DIM_DIR, "dim_airport.csv")
DIM_MARKET_PATH = os.path.join(DIM_DIR, "dim_market.csv")

# Target Airline Set (Top 7)
# 2: AA, 3: AS, 4: B6, 5: DL, 13: OO, 15: UA, 16: WN
TARGET_AIRLINES = {2, 3, 4, 5, 13, 15, 16}
LEGACY_BIG3 = {2, 5, 15}  # AA, DL, UA

def get_big3_airports():
    print(f"[Step 1] Identifying airports with Big 3 (AA, DL, UA) flight movements from {OTP_V0}...")
    start = time.time()
    big3_airports = set()
    total_rows = 0
    with open(OTP_V0, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        aidx = header.index("airlineId")
        oidx = header.index("originAirportId")
        didx = header.index("destAirportId")
        for line in f:
            total_rows += 1
            parts = line.strip().split(",")
            al = int(parts[aidx])
            orig = int(parts[oidx])
            dest = int(parts[didx])
            if al in LEGACY_BIG3:
                big3_airports.add(orig)
                big3_airports.add(dest)
            if total_rows % 10000000 == 0:
                print(f"  Scanned {total_rows:,} OTP rows...")

    print(f"  Identified {len(big3_airports)} airports with Big 3 service in {time.time()-start:.2f}s.")
    return big3_airports

def build_dim_market(big3_airports):
    print(f"\n[Step 2] Building conformed city-pair market dimension ({DIM_MARKET_PATH})...")
    start = time.time()
    
    # Load airport codes
    id2code = {}
    with open(DIM_AIRPORT_PATH, "r", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            id2code[int(row["airportId"])] = row["airportCode"]

    # Extract all distinct (originAirportId, destAirportId, nonStopMiles) pairs across datasets
    market_distances = {}

    # Scan DB1B for static distances
    with open(DB1_V0, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        oidx = header.index("originAirportId")
        didx = header.index("destAirportId")
        midx = header.index("nonStopMiles")
        for line in f:
            parts = line.strip().split(",")
            orig = int(parts[oidx])
            dest = int(parts[didx])
            if orig in big3_airports and dest in big3_airports:
                pair = (orig, dest)
                if pair not in market_distances:
                    market_distances[pair] = int(float(parts[midx]))

    # Scan T-100 for any additional routes
    with open(T100_V0, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        oidx = header.index("originAirportId")
        didx = header.index("destAirportId")
        dist_idx = header.index("distance")
        for line in f:
            parts = line.strip().split(",")
            orig = int(parts[oidx])
            dest = int(parts[didx])
            if orig in big3_airports and dest in big3_airports:
                pair = (orig, dest)
                if pair not in market_distances:
                    market_distances[pair] = int(float(parts[dist_idx]))

    # Scan OTP for any additional routes
    with open(OTP_V0, "r", encoding="utf-8") as f:
        header = f.readline().strip().split(",")
        oidx = header.index("originAirportId")
        didx = header.index("destAirportId")
        dist_idx = header.index("distance")
        for line in f:
            parts = line.strip().split(",")
            orig = int(parts[oidx])
            dest = int(parts[didx])
            if orig in big3_airports and dest in big3_airports:
                pair = (orig, dest)
                if pair not in market_distances:
                    market_distances[pair] = int(float(parts[dist_idx]))

    # Sort market pairs deterministically
    sorted_pairs = sorted(market_distances.keys())
    market_lookup = {}

    with open(DIM_MARKET_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "marketId",
            "originAirportId",
            "destAirportId",
            "originAirportCode",
            "destAirportCode",
            "nonStopMiles",
            "distanceGroup"
        ])
        for market_id, (orig, dest) in enumerate(sorted_pairs, start=1):
            miles = market_distances[(orig, dest)]
            dist_group = min(11, max(1, (miles // 500) + 1))
            orig_code = id2code.get(orig, "???")
            dest_code = id2code.get(dest, "???")
            writer.writerow([
                market_id,
                orig,
                dest,
                orig_code,
                dest_code,
                miles,
                dist_group
            ])
            market_lookup[(orig, dest)] = market_id

    print(f"  dim_market.csv generated with {len(market_lookup):,} conformed city-pair markets in {time.time()-start:.2f}s.")
    return market_lookup

def generate_otp_v1(big3_airports):
    print(f"\n[Step 3] Generating {OTP_V1}...")
    start = time.time()
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(OTP_V0, "r", encoding="utf-8") as fin, open(OTP_V1, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        aidx = col_names.index("airlineId")
        oidx = col_names.index("originAirportId")
        didx = col_names.index("destAirportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            al = int(parts[aidx])
            orig = int(parts[oidx])
            dest = int(parts[didx])

            if (al in TARGET_AIRLINES) and (orig in big3_airports) and (dest in big3_airports):
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

            if total_rows % 10000000 == 0:
                print(f"  Processed {total_rows:,} OTP rows (kept {kept_rows:,})...")

    elapsed = time.time() - start
    print(f"  otpv1.csv Generated in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def generate_tsa_v1(big3_airports):
    print(f"\n[Step 4] Generating {TSA_V1}...")
    start = time.time()
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(TSA_V0, "r", encoding="utf-8") as fin, open(TSA_V1, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        aidx = col_names.index("airportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            aid = int(parts[aidx])

            if aid in big3_airports:
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

            if total_rows % 5000000 == 0:
                print(f"  Processed {total_rows:,} TSA rows (kept {kept_rows:,})...")

    elapsed = time.time() - start
    print(f"  tsav1.csv Generated in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def generate_t100_v1(big3_airports):
    print(f"\n[Step 5] Generating {T100_V1}...")
    start = time.time()
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(T100_V0, "r", encoding="utf-8") as fin, open(T100_V1, "w", encoding="utf-8") as fout:
        header = fin.readline()
        fout.write(header)
        col_names = header.strip().split(",")
        aidx = col_names.index("airlineId")
        oidx = col_names.index("originAirportId")
        didx = col_names.index("destAirportId")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            al = int(parts[aidx])
            orig = int(parts[oidx])
            dest = int(parts[didx])

            if (al in TARGET_AIRLINES) and (orig in big3_airports) and (dest in big3_airports):
                fout.write(line)
                kept_rows += 1
            else:
                dropped_rows += 1

    elapsed = time.time() - start
    print(f"  t100v1.csv Generated in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def generate_db1_v1(big3_airports, market_lookup):
    print(f"\n[Step 6] Generating normalized {DB1_V1} (with marketId, quarter dropped, month aligned)...")
    start = time.time()
    total_rows = 0
    kept_rows = 0
    dropped_rows = 0

    with open(DB1_V0, "r", encoding="utf-8") as fin, open(DB1_V1, "w", encoding="utf-8") as fout:
        # New 10-column header (quarter dropped, nonStopMiles offloaded, origin/dest replaced by marketId)
        fout.write("year,month,marketId,rpAirlineId,tkAirlineId,opAirlineId,mktCoupons,passengers,mktFare,mktDistance\n")
        
        header = fin.readline().strip().split(",")
        y_idx = header.index("year")
        q_idx = header.index("quarter")
        orig_idx = header.index("originAirportId")
        dest_idx = header.index("destAirportId")
        rp_idx = header.index("rpAirlineId")
        tk_idx = header.index("tkAirlineId")
        op_idx = header.index("opAirlineId")
        c_idx = header.index("mktCoupons")
        pax_idx = header.index("passengers")
        fare_idx = header.index("mktFare")
        dist_idx = header.index("mktDistance")

        for line in fin:
            total_rows += 1
            parts = line.strip().split(",")
            op_al = int(parts[op_idx])
            orig = int(parts[orig_idx])
            dest = int(parts[dest_idx])

            if (op_al in TARGET_AIRLINES) and (orig in big3_airports) and (dest in big3_airports):
                market_id = market_lookup.get((orig, dest))
                if market_id is not None:
                    year = parts[y_idx]
                    quarter = int(parts[q_idx])
                    month = (quarter - 1) * 3 + 1  # 1, 4, 7, 10
                    rp_al = parts[rp_idx]
                    tk_al = parts[tk_idx]
                    coupons = parts[c_idx]
                    passengers = parts[pax_idx]
                    fare = parts[fare_idx]
                    distance = parts[dist_idx]
                    
                    fout.write(f"{year},{month},{market_id},{rp_al},{tk_al},{op_al},{coupons},{passengers},{fare},{distance}\n")
                    kept_rows += 1
                else:
                    dropped_rows += 1
            else:
                dropped_rows += 1

            if total_rows % 10000000 == 0:
                print(f"  Processed {total_rows:,} DB1B rows (kept {kept_rows:,})...")

    elapsed = time.time() - start
    print(f"  db1v1.csv Generated in {elapsed:.2f}s:")
    print(f"    - Rows before: {total_rows:,}")
    print(f"    - Rows kept  : {kept_rows:,} ({kept_rows/total_rows*100:.2f}%)")
    print(f"    - Rows dropped: {dropped_rows:,} ({dropped_rows/total_rows*100:.2f}%)")

def build_parquet_files():
    print(f"\n[Step 7] Converting v1 CSV files to Parquet with harmonized relational schemas...")
    start = time.time()
    con = duckdb.connect()
    
    # 1. otpv1: Explicit integer, boolean, float casting (no unnecessary floats)
    con.execute(f"""
    COPY (
        SELECT 
            CAST(dateId AS INTEGER) AS dateId,
            CAST(airlineId AS UTINYINT) AS airlineId,
            CAST(aircraftId AS INTEGER) AS aircraftId,
            CAST(originAirportId AS USMALLINT) AS originAirportId,
            CAST(destAirportId AS USMALLINT) AS destAirportId,
            CAST(crsDepTime AS VARCHAR) AS crsDepTime,
            CAST(crsDepMinOfDay AS SMALLINT) AS crsDepMinOfDay,
            CAST(crsDepTimeSin AS FLOAT) AS crsDepTimeSin,
            CAST(crsDepTimeCos AS FLOAT) AS crsDepTimeCos,
            CAST(depTime AS VARCHAR) AS depTime,
            CAST(depDel AS SMALLINT) AS depDel,
            CAST(depDel15 AS BOOLEAN) AS depDel15,
            CAST(depTimeBlockId AS UTINYINT) AS depTimeBlockId,
            CAST(taxiOut AS SMALLINT) AS taxiOut,
            CAST(wheelsOff AS VARCHAR) AS wheelsOff,
            CAST(wheelsOn AS VARCHAR) AS wheelsOn,
            CAST(taxiIn AS SMALLINT) AS taxiIn,
            CAST(crsArrTime AS VARCHAR) AS crsArrTime,
            CAST(crsArrMinOfDay AS SMALLINT) AS crsArrMinOfDay,
            CAST(crsArrTimeSin AS FLOAT) AS crsArrTimeSin,
            CAST(crsArrTimeCos AS FLOAT) AS crsArrTimeCos,
            CAST(arrTime AS VARCHAR) AS arrTime,
            CAST(arrDel AS SMALLINT) AS arrDel,
            CAST(arrDel15 AS BOOLEAN) AS arrDel15,
            CAST(arrTimeBlockId AS UTINYINT) AS arrTimeBlockId,
            CAST(cancelled AS BOOLEAN) AS cancelled,
            CAST(cancellationId AS UTINYINT) AS cancellationId,
            CAST(diverted AS BOOLEAN) AS diverted,
            CAST(crsElapsedTime AS SMALLINT) AS crsElapsedTime,
            CAST(airTime AS SMALLINT) AS airTime,
            CAST(distance AS USMALLINT) AS distance,
            CAST(carrierDel AS SMALLINT) AS carrierDel,
            CAST(weatherDel AS SMALLINT) AS weatherDel,
            CAST(nasDel AS SMALLINT) AS nasDel,
            CAST(securityDel AS SMALLINT) AS securityDel,
            CAST(lateAircraftDel AS SMALLINT) AS lateAircraftDel,
            CAST(delayTypeId AS UTINYINT) AS delayTypeId
        FROM read_csv_auto('{OTP_V1}')
    ) TO '{DATA_DIR}/otpv1.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
    """)
    print("  -> otpv1.parquet generated (harmonized relational schema).")
    
    # 2. tsav1: Compact integers, boolean missing flag
    con.execute(f"""
    COPY (
        SELECT 
            CAST(dateId AS INTEGER) AS dateId,
            CAST(hour AS UTINYINT) AS hour,
            CAST(timeBlockId AS UTINYINT) AS timeBlockId,
            CAST(airportId AS USMALLINT) AS airportId,
            CAST(checkpointId AS USMALLINT) AS checkpointId,
            CAST(throughput AS INTEGER) AS throughput,
            CAST(airportMissing AS BOOLEAN) AS airportMissing
        FROM read_csv_auto('{TSA_V1}')
    ) TO '{DATA_DIR}/tsav1.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
    """)
    print("  -> tsav1.parquet generated (harmonized relational schema).")
    
    # 3. t100v1: Integer capacity, float load factor, integer distance
    con.execute(f"""
    COPY (
        SELECT 
            CAST(year AS SMALLINT) AS year,
            CAST(month AS UTINYINT) AS month,
            CAST(airlineId AS UTINYINT) AS airlineId,
            CAST(originAirportId AS USMALLINT) AS originAirportId,
            CAST(destAirportId AS USMALLINT) AS destAirportId,
            CAST(aircraftTypeId AS USMALLINT) AS aircraftTypeId,
            CAST(aircraftConfigId AS UTINYINT) AS aircraftConfigId,
            CAST(seats AS INTEGER) AS seats,
            CAST(passengers AS INTEGER) AS passengers,
            CAST(loadFactor AS FLOAT) AS loadFactor,
            CAST(distance AS USMALLINT) AS distance
        FROM read_csv_auto('{T100_V1}')
    ) TO '{DATA_DIR}/t100v1.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
    """)
    print("  -> t100v1.parquet generated (harmonized relational schema).")
    
    # 4. db1v1: Integer passengers, decimal currency, integer distance
    con.execute(f"""
    COPY (
        SELECT 
            CAST(year AS SMALLINT) AS year,
            CAST(month AS UTINYINT) AS month,
            CAST(marketId AS INTEGER) AS marketId,
            CAST(rpAirlineId AS UTINYINT) AS rpAirlineId,
            CAST(tkAirlineId AS UTINYINT) AS tkAirlineId,
            CAST(opAirlineId AS UTINYINT) AS opAirlineId,
            CAST(mktCoupons AS UTINYINT) AS mktCoupons,
            CAST(passengers AS INTEGER) AS passengers,
            CAST(mktFare AS DECIMAL(10,2)) AS mktFare,
            CAST(mktDistance AS USMALLINT) AS mktDistance
        FROM read_csv_auto('{DB1_V1}')
    ) TO '{DATA_DIR}/db1v1.parquet' (FORMAT PARQUET, COMPRESSION ZSTD);
    """)
    print("  -> db1v1.parquet generated (harmonized relational schema).")
    print(f"  All Parquet files successfully generated in {time.time()-start:.2f}s.")

def main():
    print("=" * 80)
    print("STARTING V1 DATASET & DIM_MARKET GENERATION PIPELINE")
    print("=" * 80)
    overall_start = time.time()
    
    big3_airports = get_big3_airports()
    market_lookup = build_dim_market(big3_airports)
    generate_otp_v1(big3_airports)
    generate_tsa_v1(big3_airports)
    generate_t100_v1(big3_airports)
    generate_db1_v1(big3_airports, market_lookup)
    build_parquet_files()
    
    print("\n" + "=" * 80)
    print(f"ALL V1 DATASETS & DIMENSIONS GENERATED SUCCESSFULLY IN {time.time()-overall_start:.2f}s!")
    print("=" * 80)

if __name__ == "__main__":
    main()
