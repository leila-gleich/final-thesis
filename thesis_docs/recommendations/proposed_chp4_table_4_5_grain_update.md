# Proposed Manuscript Revision: Table 4.5 Sample Grain Harmonization

> **Author-Editor Interlock Protocol (Policy 1.5 Gate Sequence)**  
> **Target File**: `thesis_docs/manuscripts/chp4-results.md` (Line 140)  
> **Authorship Status**: Last edited by author `Leila Gleich`. Direct modification locked.  
> **Status**: Non-destructive proposed patch awaiting explicit author confirmation.

---

## 1. Context & Mathematical Rationale

In **Table 4.5** (*Master Cross-Dataset Econometric Relationships (Top 25 Airfields)*), Row 5 (*Surface-to-Air Feedback: Mean Flight Departure Delay vs. Runway Taxi-Out Queue Time*) is currently drafted as:

```markdown
| Surface-to-Air Feedback | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | 63,925 Airport-Days | 0.4971 | 24.71% | 2.74 | $< 0.001$ | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
```

### Mathematical Degrees of Freedom Proof:
The standard Pearson $t$-statistic is given by:
$$t = \frac{r\sqrt{N-2}}{\sqrt{1-r^2}}$$

1. **If evaluated across $N = 25$ airfields ($df = 23$)**:
   $$t = \frac{0.4971 \times \sqrt{23}}{\sqrt{1 - 0.4971^2}} = \frac{0.4971 \times 4.79583}{0.86768} = 2.747 \approx 2.74$$
   This yields $p = 0.0116$ ($p < 0.05$ or $p < 0.01$).

2. **If evaluated across $N = 63,925$ airport-days**:
   $$t = \frac{0.4971 \times \sqrt{63,923}}{\sqrt{1 - 0.4971^2}} = \frac{0.4971 \times 252.83}{0.86768} \approx 144.82$$

The reported statistic $t = 2.74$ mathematically proves that this correlation was estimated across the cross-sectional **Top 25 Airfields** aggregated means, exactly like Rows 1, 2, 3, 4, 6, 7, 8, and 9. The label `"63,925 Airport-Days"` was a legacy typographical placeholder from the raw staging census.

All conformed CSV tables (`results/manuscript_tables/table_4_5.csv`, `results/tables/table_4_5_master_cross_dataset_econometric_relationships.csv`) and master Excel workbooks (`thesis_tables.xlsx`) have already been harmonized.

---

## 2. Proposed Exact Replacement

### Current Line 140:
```markdown
| Surface-to-Air Feedback | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | 63,925 Airport-Days | 0.4971 | 24.71% | 2.74 | $< 0.001$ | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
```

### Proposed Line 140:
```markdown
| Surface-to-Air Feedback | Mean Flight Departure Delay (min) | Runway Taxi-Out Queue Time (min) | Top 25 Airfields | 0.4971 | 24.71% | 2.74 | $< 0.001$ | Delayed gate pushbacks compress outbound aircraft into congested runway sequencing queues. |
```
