#!/usr/bin/env python3
"""
transform_otp_time.py
======================
High-Precision Time Transformation & Temporal Standardization for On-Time Performance (otpv1).

Purpose:
--------
Raw and v1 BTS flight records store scheduled timestamps (CRSDepTime, CRSArrTime) as 4-character
string or integer representations (HHMM, e.g., '0709', '1445'). In downstream machine learning
models and time-series aggregations, this introduces three critical defects:
  1. Non-linear step jumps across hour boundaries (e.g., 0759 + 1 minute -> 0800, creating
     an artificial numeric discontinuity of 41 units).
  2. Midnight discontinuity (2359 -> 0000) that distorts neural networks, linear regressors,
     and distance metrics.
  3. Inability to calculate minute-level lead-lag queues or sliding concurrent flight pressure
     without costly on-the-fly string manipulations.

Transformations Applied:
------------------------
  - crsDepMinOfDay: Continuous integer minute from midnight in [0, 1439] (e.g., '0709' -> 429).
  - crsArrMinOfDay: Continuous integer minute from midnight in [0, 1439] (e.g., '0910' -> 550).
  - crsDepTimeSin, crsDepTimeCos: Cyclical trigonometric encodings capturing continuous diurnal phase.
  - crsArrTimeSin, crsArrTimeCos: Cyclical trigonometric arrival encodings.

Execution:
----------
Utilizes DuckDB's columnar vectorized execution engine to process 32.5M rows in memory,
writing the conformed result directly to otpv1.parquet with ZSTD compression.
"""

import os
import sys
import time
import duckdb

# Determine base paths dynamically relative to script location
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")
INPUT_PARQUET = os.path.join(PROCESSED_DIR, "otpv1.parquet")
TEMP_PARQUET = os.path.join(PROCESSED_DIR, "otpv1_transformed.parquet")

def transform_otp_timestamps():
    print("=" * 80)
    print("STARTING HIGH-PRECISION TEMPORAL TRANSFORMATION ON OTP (otpv1)")
    print(f"Source File : {INPUT_PARQUET}")
    print(f"Target File : {TEMP_PARQUET}")
    print("=" * 80)
    
    start_time = time.time()
    con = duckdb.connect()
    con.execute("PRAGMA threads=8;")
    con.execute("PRAGMA preserve_insertion_order=false;")
    
    # Verify input exists
    if not os.path.exists(INPUT_PARQUET):
        raise FileNotFoundError(f"Input dataset not found: {INPUT_PARQUET}")
        
    initial_count = con.execute(f"SELECT COUNT(*) FROM read_parquet('{INPUT_PARQUET}')").fetchone()[0]
    print(f"Initial otpv1 record count: {initial_count:,}")
    
    print("\n[Step 1] Constructing vectorized SQL query with minute-of-day and cyclical terms...")
    
    # Vectorized SQL transformation:
    # 1. Pads string time to 4 digits (e.g., '709' -> '0709')
    # 2. Extracts hours (pos 1-2) and minutes (pos 3-4)
    # 3. Calculates total minutes: (hours * 60 + minutes) % 1440 to seamlessly handle midnight/2400
    # 4. Computes sine and cosine transforms scaled to 2*pi / 1440 radians
    transform_query = f"""
    COPY (
        SELECT 
            dateId,
            airlineId,
            aircraftId,
            originAirportId,
            destAirportId,
            crsDepTime,
            -- Continuous integer minute of day [0, 1439]
            CASE 
                WHEN crsDepTime IS NULL OR TRIM(crsDepTime) = '' THEN NULL
                ELSE (
                    (CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                     CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 3, 2) AS INTEGER)) % 1440
                )
            END AS crsDepMinOfDay,
            -- Cyclical diurnal encodings for scheduled departure
            CASE 
                WHEN crsDepTime IS NULL OR TRIM(crsDepTime) = '' THEN NULL
                ELSE SIN(2.0 * PI() * (
                    ((CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                      CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 3, 2) AS INTEGER)) % 1440) / 1440.0
                ))
            END AS crsDepTimeSin,
            CASE 
                WHEN crsDepTime IS NULL OR TRIM(crsDepTime) = '' THEN NULL
                ELSE COS(2.0 * PI() * (
                    ((CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                      CAST(SUBSTRING(LPAD(TRIM(crsDepTime), 4, '0'), 3, 2) AS INTEGER)) % 1440) / 1440.0
                ))
            END AS crsDepTimeCos,
            depTime,
            depDel,
            depDel15,
            depTimeBlockId,
            taxiOut,
            wheelsOff,
            wheelsOn,
            taxiIn,
            crsArrTime,
            -- Continuous integer minute of day [0, 1439]
            CASE 
                WHEN crsArrTime IS NULL OR TRIM(crsArrTime) = '' THEN NULL
                ELSE (
                    (CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                     CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 3, 2) AS INTEGER)) % 1440
                )
            END AS crsArrMinOfDay,
            -- Cyclical diurnal encodings for scheduled arrival
            CASE 
                WHEN crsArrTime IS NULL OR TRIM(crsArrTime) = '' THEN NULL
                ELSE SIN(2.0 * PI() * (
                    ((CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                      CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 3, 2) AS INTEGER)) % 1440) / 1440.0
                ))
            END AS crsArrTimeSin,
            CASE 
                WHEN crsArrTime IS NULL OR TRIM(crsArrTime) = '' THEN NULL
                ELSE COS(2.0 * PI() * (
                    ((CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 1, 2) AS INTEGER) * 60 + 
                      CAST(SUBSTRING(LPAD(TRIM(crsArrTime), 4, '0'), 3, 2) AS INTEGER)) % 1440) / 1440.0
                ))
            END AS crsArrTimeCos,
            arrTime,
            arrDel,
            arrDel15,
            arrTimeBlockId,
            cancelled,
            cancellationId,
            diverted,
            crsElapsedTime,
            airTime,
            distance,
            carrierDel,
            weatherDel,
            nasDel,
            securityDel,
            lateAircraftDel,
            delayTypeId
        FROM read_parquet('{INPUT_PARQUET}')
    ) TO '{TEMP_PARQUET}' (FORMAT PARQUET, COMPRESSION 'ZSTD');
    """
    
    print("[Step 2] Executing transformation and writing temporary parquet...")
    t_exec = time.time()
    con.execute(transform_query)
    print(f"  -> Transformation and export completed in {time.time() - t_exec:.2f}s")
    
    print("\n[Step 3] Verifying record integrity and null counts...")
    audit = con.execute(f"""
        SELECT 
            COUNT(*) AS total_rows,
            COUNT(crsDepMinOfDay) AS dep_min_valid,
            COUNT(crsArrMinOfDay) AS arr_min_valid,
            MIN(crsDepMinOfDay) AS min_dep_min,
            MAX(crsDepMinOfDay) AS max_dep_min,
            MIN(crsDepTimeSin) AS min_sin,
            MAX(crsDepTimeSin) AS max_sin
        FROM read_parquet('{TEMP_PARQUET}')
    """).fetchone()
    
    print(f"  Total Rows         : {audit[0]:,}")
    print(f"  Valid Dep Minutes  : {audit[1]:,} ({audit[1]/audit[0]*100:.2f}%)")
    print(f"  Valid Arr Minutes  : {audit[2]:,} ({audit[2]/audit[0]*100:.2f}%)")
    print(f"  Dep Minute Range   : [{audit[3]}, {audit[4]}] (Expected: [0, 1439])")
    print(f"  Dep Sin Range      : [{audit[5]:.4f}, {audit[6]:.4f}] (Expected: [-1.0, 1.0])")
    
    if audit[0] != initial_count:
        raise ValueError(f"Row count mismatch: {audit[0]} vs {initial_count}")
        
    print("\n[Step 4] Atomically replacing otpv1.parquet with transformed dataset...")
    # Replace original file atomically
    os.replace(TEMP_PARQUET, INPUT_PARQUET)
    
    final_size_mb = os.path.getsize(INPUT_PARQUET) / (1024 * 1024)
    total_duration = time.time() - start_time
    print("=" * 80)
    print(f"SUCCESS: otpv1.parquet successfully transformed!")
    print(f"New File Size : {final_size_mb:.2f} MB")
    print(f"Total Duration: {total_duration:.2f}s")
    print("=" * 80)

if __name__ == '__main__':
    transform_otp_timestamps()
