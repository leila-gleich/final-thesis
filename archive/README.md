# Repository Archive & Legacy Data Artifacts

This directory contains historical precursors, early diagram drafts, and legacy tabular datasets from earlier research milestones. All current production models, empirical findings, and conformed datasets are maintained in `data/`, `results/`, and `thesis_docs/`.

---

## Directory Index

```
archive/
├── README.md                       <-- Archive catalog & manifest (this file)
│
├── precursor_workbooks/            <-- Early drafting spreadsheets (superseded by results/01-05)
│   ├── Gleich_Thesis_Hypotheses.xlsx
│   ├── Top25 Analysis.xlsx
│   ├── Top9 Metrics.xlsx
│   ├── master-evaluation-metrics.xlsx
│   └── Table_C_Summary_Descriptive_Statistics_of_9_Filtered_Airfields.parquet
│
├── early_diagram_drafts/           <-- Preliminary drafting flowcharts & unmerged diagrams
│   ├── 01_Sample_and_Airport_Selection/
│   ├── 02_Data_Pipelines_and_Threats/
│   ├── 03_Modeling_and_Evaluation/
│   ├── 04_Appendix_and_Reference/
│   └── *.png
│
├── legacy_parquet/                 <-- 49 conformed legacy tables compressed to Snappy Parquet
│   ├── 01_Executive_Top25_Airport_Coupled_Master_Census.parquet
│   ├── 02_Executive_Cross_Dataset_Statistical_Relationships_and_Volatility.parquet
│   ├── 03_Executive_Coupled_Seasonality_and_Operational_Regimes.parquet
│   ├── BTS_DB1B_Top25_Connecting_Ratio_Census.parquet
│   ├── Section_1A_to_5A_*.parquet
│   └── TSA_Top25_*.parquet
│
├── legacy_volume_results/          <-- Archived volume-only models, benchmark results & tables (v4.3)
│   ├── 04_model_execution_2025_holdout.xlsx
│   ├── 05_robustness_resilience_generalizability.xlsx
│   └── tables/                     # Legacy volume forecasting CSV tables
│
└── superseded_scripts/             <-- Historical ETL, modeling and warehouse analysis scripts
    ├── run_pipeline_volume_legacy.py # Legacy volume-level throughput pipeline
    ├── candidate_b_deep_dive.py    # Pre-demarcation DuckDB exploration (results compiled)
    ├── regime_analysis.py          # Pre-demarcation regime analysis (results compiled)
    ├── filter_top_20pct_airports.py# Historical Top 78 filter (superseded by 4-tier filtering)
    ├── filter_datasets_by_otp.py   # Legacy warehouse filter (superseded by conformed data)
    ├── generate_v1_datasets.py     # Initial batch ETL pipeline for warehouse v1
    ├── transform_otp_time.py       # Vectorized timestamp script (modularized to time_features.py)
    ├── temporal_features.py        # Legacy rolling average query (modularized to time_features.py)
    ├── db_connection.py            # Obsolete DuckDB connector targeting data/warehouse.duckdb
    ├── airport_selector.py         # Legacy volume-based airport selector targeting archive Parquet
    ├── lead_lag_convolution.py     # Static lognormal arrival kernel (superseded by cluster_adapt.py)
    ├── download_2022_2025_db1b.py  # One-off TranStats curl download for historical DB1B ZIPs
    ├── combine_db1c_datasets.py    # One-off concatenation of 2025-07 to 2025-12 DB1C monthly files
    ├── process_od_coupon.py        # One-off coupon streaming/cleaning ZIP preprocessor
    ├── profile_db1b.py             # One-off random sampling and schema profiler for raw DB1B
    ├── build_db1v0.py              # Precursor fact table builder (superseded by conformed curated feeds)
    ├── enrich_dimensions.py        # One-off dimension metadata builder for airport/date dimensions
    ├── perform_top9_analysis.py    # Standalone Top 9 vs Top 25 script (superseded by conformed tables)
    └── test_features_legacy.py     # Legacy unit tests for archived lead_lag_convolution & airport_selector
```

---

## Storage & Compression Standards

1. **Parquet Conversion**: Legacy CSV tables have been converted into compressed Apache Parquet (`.parquet`) using Snappy compression, enabling direct zero-copy queries via DuckDB and Pandas (`pd.read_parquet(...)`) while minimizing repository size.
2. **Provenance**: Official production workbooks are maintained in `results/01_top25_clustering.xlsx` through `results/05_robustness_resilience_generalizability.xlsx`.
