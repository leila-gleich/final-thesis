# Thesis Appendix & Reference Figures and Data Tables
## Evaluating Predictive Techniques to Model Stochastic Airport Passenger Flow (MSAA / Gleich 700B)

> **Chapter Purpose**: Reference database profiles, BTS DB1B relational hierarchies, feature store partition manifests, backup storage hierarchies, and methodological assumption matrices for the **Thesis Appendix**.

---

### Appendix Exhibit Inventory

| Visual Graphic (`.png`) | Companion Data (`.csv`) | Appendix Location | Description & Operational Function |
| :--- | :--- | :--- | :--- |
| `BTS-DB1B_Appendix.png` | `bts_db1b_table_hierarchy.csv` | Appendix Section C | Bureau of Transportation Statistics 10% ticket coupon survey relational hierarchy (DB1BTicket $\to$ DB1BMarket $\to$ DB1BCoupon). |
| `Backups organization.png` | `backups_organization.csv` | Appendix Section H | Master backup hierarchy and directory structure governing raw feeds, processed feature stores, and codebase. |
| `Diagrams and Screenshot Layout.png` | `diagrams_and_screenshot_layout.csv` | Appendix Section H | Master layout directory tree mapping diagrams and screenshots across thesis chapters. |
| `data profile top9.png` | `data_profile_top9.csv` | Appendix Section B | Filtered 9-airport target research cohort feature store parquet partitions and Zstandard compression metrics. |
| `database profiles.png` | `database_profiles.csv` | Appendix Section A | Summary census of upstream raw ingested records versus cleaned conformed records preserved in the warehouse. |
| `dataset breakdown.png` | `dataset_breakdown.csv` | Appendix Section A | Architectural specifications of conformed analytics tables stored in Apache Parquet format. |
| `methodological assumptions.png` | `methodological_assumptions.csv` | Appendix Section D | Master 14-point methodological and operational assumptions framework and failure modes table. |
| *Workbook Asset* | `04_Appendix_and_Reference.xlsx` | Appendix Reference | Multi-tab APA 7 consolidated Excel workbook containing all 7 appendix data tables. |
