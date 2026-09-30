# STATUS: IMPLEMENTED

# Recommendation REC-10: Principal Component Analysis (PCA) Dimensionality Reduction & Loadings Synthesis

**Recommendation ID**: REC-10  
**Target Manuscripts**: `thesis_docs/manuscripts/` & `src/etl/perform_top25_clustering.py`  
**Warehouse Status**: IMPLEMENTED  
**final-thesis Status**: IMPLEMENTED  
**Date**: September 30, 2026  

---

## 1. Executive Summary & Problem Context

Table 4.3 in Chapter 4 presents column headers labeled "PC1", "PC2", and "PC3" without explicitly defining "PC", specifying the eigenvalue threshold criteria, or providing factor loading interpretations. Furthermore, Chapter 3 lacks the formal mathematical derivation of PCA as the pre-clustering orthogonalization step.

Raw airport operational indicators exhibit substantial pairwise collinearity ($\text{Corr} > 0.85$). Directly clustering in high-dimensional space distorts Euclidean distance calculations in K-Means.

---

## 2. Technical Specification

### 2.1 PCA Derivation for Chapter 3 (Methodology)
Nine standardized operational metrics ($z$-score normalized) are projected onto an orthogonal lower-dimensional subspace:
$$\mathbf{Z} = \mathbf{X} \mathbf{W}$$
where $\mathbf{\Sigma} = \frac{1}{n-1}\mathbf{X}^T \mathbf{X}$.

Components satisfying the Kaiser–Guttman criterion ($\lambda_j \ge 1.0$) and achieving $>75\%$ cumulative explained variance compress the nine correlated attributes into three uncorrelated coordinate axes ($k=3$).

### 2.2 Factor Loading Interpretations for Chapter 4 (Results)
- **PC1: Scale and Airfield Congestion (33.8% Explained Variance)**: Heavy positive loadings on estimated throughput (+0.432), departure delays (+0.368), actual TSA throughput (+0.364), and taxi-out duration (+0.347).
- **PC2: Aircraft Gauge vs. Schedule Vulnerability (25.5% Explained Variance)**: Positive loadings on aircraft seats (+0.519) and load factor (+0.410); negative loadings on cancellation rate (−0.466) and departure delays (−0.321).
- **PC3: Connecting Dominance & Airside Transfer (17.7% Explained Variance)**: Positive loadings on DB1B connecting ratio (+0.583) and departure delay rate (+0.500); negative loading on taxi-out (−0.295).

---

## 3. Publication Draft Text

```markdown
### 3.2.1 Stage 1: Dimensionality Reduction via Principal Component Analysis (PCA)

To categorize the Top 25 commercial airfields into objective operational archetypes without imposing arbitrary heuristic thresholds, this study implements an unsupervised machine learning pipeline. However, raw airport operational indicators exhibit substantial pairwise collinearity (e.g., Corr(Seats, Throughput) > 0.85). Directly clustering in high-dimensional, correlated feature space distorts Euclidean distance metrics.

To resolve this multicollinearity, Principal Component Analysis (PCA) is applied as an orthogonal linear dimensionality-reduction technique prior to clustering...
```

---

## 4. Verification & Acceptance Criteria

- [ ] PCA mathematical derivation inserted into Chapter 3 Section 3.2.1.
- [ ] Factor loading narrative inserted above Table 4.3 in Chapter 4.
- [ ] 3 PCs confirmed ($\lambda \ge 1.0$, 77.0% cumulative variance).
