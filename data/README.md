# Data Provenance & Ingestion Directory

This directory stores the primary federal aviation datasets and intermediate processed artifacts utilized in the graduate thesis *Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow*.

---

## Directory Organization

```
data/
├── raw/            <-- Unprocessed federal source files (excluded from Git tracking)
│   ├── tsa/        # TSA FOIA passenger checkpoint hourly logs (2019–2025)
│   ├── otp/        # BTS On-Time Performance flight movement records
│   ├── t100/       # BTS T-100 Segment aircraft capacity & seats
│   └── db1b/       # BTS DB1B / DB1C 10% ticket survey itinerary & coupon files
│
└── processed/      <-- Intermediate sanitized datasets & parquet databases
    ├── archive/    # Archived baseline partitions (e.g. v0)
    └── warehouse/  # DuckDB local analytics instances
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

## Replication Note

Due to file sizes exceeding GitHub limits (67.22 million raw records totaling >35 GB uncompressed), raw data files in `data/raw/` and processed tables in `data/processed/` are excluded via `.gitignore`. 

All conformed lookup dimensions necessary for pipeline orchestration are version-controlled in the top-level `dimensions/` directory. All final empirical benchmark outputs are version-controlled in `results/`.
