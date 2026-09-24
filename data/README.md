# Data Provenance & Ingestion Directory

This directory stores the primary federal aviation datasets, curated aggregates, representative sample fixtures, and intermediate processed artifacts utilized in the graduate thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*.

---

## Directory Organization

```
data/
├── curated/            <-- Version-controlled multi-year aggregated operational datasets
│   ├── hourly_aggregated_data.csv   # Coupled hourly TSA throughput & flight departures (2019–2025)
│   └── daily_aggregated_data.csv    # Daily consolidated throughput & flight counts
│
├── sample/             <-- Lightweight representative sample fixtures for CI/CD & local testing
│   ├── sample_otp_raw.csv           # 10,000-row BTS OTP flight movements sample
│   ├── sample_db1b_market.csv       # 10,000-row BTS DB1B Origin-Destination Market sample
│   ├── sample_db1c.csv              # 5,000-row BTS DB1C monthly coupon itinerary sample
│   ├── sample_t100.csv              # 5,000-row BTS T-100 carrier segment seats sample
│   └── sample_tsa_hourly.csv        # 5,000-row hourly checkpoint throughput sample
│
├── raw/                <-- Full federal source files & local staging (excluded from Git tracking)
│   ├── otp/            # BTS On-Time Performance flight movement records
│   ├── db1b/           # BTS DB1B Market 10% ticket survey archives
│   ├── db1c/           # BTS DB1C monthly coupon parquet/csv files
│   ├── t100/           # BTS T-100 Segment aircraft capacity & seats
│   └── tsa/            # TSA FOIA passenger checkpoint hourly logs
│
└── processed/          <-- Intermediate sanitized datasets & parquet databases (git-ignored)
    ├── archive/        # Archived baseline partitions (e.g. v0)
    └── warehouse/      # DuckDB local analytics instances
```

---

## Federal Data Sources & Acquisition

1. **TSA FOIA Checkpoint Screening Logs (2019–2025)**:
   * Source: Transportation Security Administration (TSA) Freedom of Information Act Office.
   * Granularity: Hourly throughput per screening lane / checkpoint across commercial airports.
   
2. **BTS Airline On-Time Performance (OTP) (2019–2025)**:
   * Source: Bureau of Transportation Statistics (BTS), U.S. Department of Transportation.
   * Access: [TranStats On-Time Performance Data](https://www.transtats.bts.gov/).
   * Content: Flight-level pushback times, scheduled vs. actual departures, taxi-out times, delay codes.

3. **BTS T-100 Domestic Segment Data (2019–2025)**:
   * Source: Bureau of Transportation Statistics (BTS).
   * Access: [TranStats T-100 Segment](https://www.transtats.bts.gov/).
   * Content: Monthly carrier-segment seats, departures scheduled vs. performed, payload capacities.

4. **BTS DB1B / DB1C Ticket Coupon Survey (2022–2025)**:
   * Source: Bureau of Transportation Statistics (BTS).
   * Access: [TranStats DB1B Coupon / Market](https://www.transtats.bts.gov/).
   * Content: 10% sample of all airline passenger tickets, itinerary routing, connecting vs. origin passengers.

---

## Self-Contained Execution & Replication

To ensure the repository is completely self-contained and reproducible without requiring users to download the full 85+ GB multi-year federal census:
- **Curated Multi-Year Aggregates:** Pre-aggregated hourly and daily coupled tables are provided directly in `data/curated/` (`hourly_aggregated_data.csv` and `daily_aggregated_data.csv`).
- **Representative Sample Data:** Micro-fixtures are provided in `data/sample/` to test and validate every stage of the ETL pipeline (`build_db1v0.py`, `profile_db1b.py`, etc.).
- **Dimensions:** Complete star schema lookup tables are version-controlled in `dimensions/`.
- **Benchmark Findings:** Publication-grade empirical results are version-controlled in `results/`.

### External Storage & Environment Overrides
If working with the full uncompressed 85+ GB census files, scripts support environment variable overrides:
- `RAW_DB1B_DIR` or `SSOT_DB1B_DIR`: Path to external DB1B market/coupon folder (defaults to `data/raw/db1b`).
- `DB1C_DIR`: Path to external DB1C monthly parquet folder (defaults to `data/raw/db1c`).
