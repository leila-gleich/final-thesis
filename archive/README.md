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
└── legacy_parquet/                 <-- 49 conformed legacy tables compressed to Snappy Parquet
    ├── 01_Executive_Top25_Airport_Coupled_Master_Census.parquet
    ├── 02_Executive_Cross_Dataset_Statistical_Relationships_and_Volatility.parquet
    ├── 03_Executive_Coupled_Seasonality_and_Operational_Regimes.parquet
    ├── BTS_DB1B_Top25_Connecting_Ratio_Census.parquet
    ├── Section_1A_to_5A_*.parquet
    └── TSA_Top25_*.parquet
```

---

## Storage & Compression Standards

1. **Parquet Conversion**: Legacy CSV tables have been converted into compressed Apache Parquet (`.parquet`) using Snappy compression, enabling direct zero-copy queries via DuckDB and Pandas (`pd.read_parquet(...)`) while minimizing repository size.
2. **Provenance**: Official production workbooks are maintained in `results/01_top25_clustering.xlsx` through `results/05_robustness_resilience_generalizability.xlsx`.
