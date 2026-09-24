#!/usr/bin/env python3
"""
build_db1v0.py

Generates the conformed db1v0 fact dataset in data/processed
from raw DB1BMarket and DB1C datasets, mapping all foreign keys
to dim_airport, dim_airline, and dim_date.
"""

import os
import sys
import time
import duckdb

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DEFAULT_RAW_DIR = os.path.join(REPO_ROOT, "data", "raw", "db1b")
RAW_DIR = os.getenv("RAW_DB1B_DIR", os.getenv("SSOT_DB1B_DIR", DEFAULT_RAW_DIR))
PROCESSED_DIR = os.path.join(REPO_ROOT, "data", "processed")
DIM_DIR = os.path.join(REPO_ROOT, "dimensions")
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Prefer full raw dataset if present, otherwise fall back to local sample dataset
candidates = [
    os.path.join(RAW_DIR, "DB1BMarket_22-25.csv"),
    os.path.join(RAW_DIR, "sample_db1b.csv"),
    os.path.join(REPO_ROOT, "data", "sample", "sample_db1b_market.csv")
]
MKT_PATH = next((p for p in candidates if os.path.exists(p)), candidates[0])
DIM_AIRPORT = os.path.join(DIM_DIR, "dim_airport.csv")
DIM_AIRLINE = os.path.join(DIM_DIR, "dim_airline.csv")


OUT_CSV = os.path.join(PROCESSED_DIR, "db1v0.csv")
OUT_PARQUET = os.path.join(PROCESSED_DIR, "db1v0.parquet")

def main():
    print("=" * 75)
    print("STARTING CONFORMED DB1 FACT TABLE GENERATION (db1v0)")
    print(f"Source Raw File : {MKT_PATH}")
    print(f"Dimensions Dir  : {DIM_DIR}")
    print(f"Target Processed: {OUT_CSV}")
    print("=" * 75 + "\n")
    
    t0 = time.time()
    con = duckdb.connect()
    
    # Configure DuckDB for maximum performance and temporary disk spill if needed
    con.execute("PRAGMA threads=8;")
    con.execute("PRAGMA preserve_insertion_order=false;")
    
    print("[Step 1] Creating conformed db1v0 table via DuckDB...")
    
    create_view_sql = f"""
    CREATE OR REPLACE TEMPORARY TABLE db1_conformed AS
    SELECT 
        CAST(m.Year AS INT) AS year,
        CAST(m.Quarter AS INT) AS quarter,
        0 AS month,
        orig.airportId AS originAirportId,
        dest.airportId AS destAirportId,
        COALESCE(rp.airlineId, 0) AS rpAirlineId,
        COALESCE(tk.airlineId, 0) AS tkAirlineId,
        COALESCE(op.airlineId, 0) AS opAirlineId,
        CAST(m.MktCoupons AS INT) AS mktCoupons,
        CAST(m.Passengers AS DOUBLE) AS passengers,
        ROUND(CAST(m.MktFare AS DOUBLE), 2) AS mktFare,
        ROUND(CAST(m.MktDistance AS DOUBLE), 1) AS mktDistance,
        ROUND(CAST(m.NonStopMiles AS DOUBLE), 1) AS nonStopMiles
    FROM read_csv('{MKT_PATH}', header=true, max_line_size=2000000) m
    JOIN read_csv('{DIM_AIRPORT}', header=true) orig ON m.Origin = orig.airportCode
    JOIN read_csv('{DIM_AIRPORT}', header=true) dest ON m.Dest = dest.airportCode
    LEFT JOIN read_csv('{DIM_AIRLINE}', header=true) rp ON m.RPCarrier = rp.reportingAirline
    LEFT JOIN read_csv('{DIM_AIRLINE}', header=true) tk ON m.TkCarrier = tk.reportingAirline
    LEFT JOIN read_csv('{DIM_AIRLINE}', header=true) op ON m.OpCarrier = op.reportingAirline
    WHERE orig.airportId > 0 AND dest.airportId > 0;
    """
    
    t_stage1 = time.time()
    con.execute(create_view_sql)
    count = con.execute("SELECT count(*) FROM db1_conformed").fetchone()[0]
    print(f"  ✓ Processed and conformed {count:,} records in {time.time() - t_stage1:.1f}s")
    
    # Export Parquet
    print(f"\n[Step 2] Exporting to Parquet: {OUT_PARQUET} ...")
    t_pq = time.time()
    con.execute(f"COPY db1_conformed TO '{OUT_PARQUET}' (FORMAT PARQUET, COMPRESSION 'ZSTD');")
    pq_size_mb = os.path.getsize(OUT_PARQUET) / (1024 * 1024)
    print(f"  ✓ Exported Parquet ({pq_size_mb:.1f} MB) in {time.time() - t_pq:.1f}s")
    
    # Export CSV
    print(f"\n[Step 3] Exporting to CSV: {OUT_CSV} ...")
    t_csv = time.time()
    con.execute(f"COPY db1_conformed TO '{OUT_CSV}' (HEADER, DELIMITER ',');")
    csv_size_mb = os.path.getsize(OUT_CSV) / (1024 * 1024)
    print(f"  ✓ Exported CSV ({csv_size_mb:.1f} MB / {csv_size_mb/1024:.2f} GB) in {time.time() - t_csv:.1f}s")
    
    total_time = time.time() - t0
    print("\n" + "=" * 75)
    print("CONFORMED DB1 FACT TABLE GENERATION COMPLETE!")
    print(f"Total Records : {count:,}")
    print(f"CSV Size      : {csv_size_mb/1024:.2f} GB")
    print(f"Parquet Size  : {pq_size_mb:.2f} MB")
    print(f"Total Runtime : {total_time:.1f}s ({total_time/60:.2f} minutes)")
    print("=" * 75)

if __name__ == "__main__":
    main()
