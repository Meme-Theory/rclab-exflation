---
name: R-PROTECTED-TRIPLE-74 (S74 W2-O) -- convention structural FAIL
description: Three-route R_protected test FAILS because partial-sum and Gilkey conventions measure different mathematical objects
type: project
---

**R-PROTECTED-TRIPLE-74 (S74 W2-O) -- structural FAIL verdict**

**Why**: The gate was designed to test whether three routes (spectral partial sum, Gilkey curvature integral, zeta extrapolation) agree on R_protected_fold = a_0 * a_4 / a_2^2 to within 3%. The result was a structural FAIL (134% max deviation) that revealed the two conventions compute different mathematical quantities.

**How to apply**: Any downstream usage of R_protected_fold MUST specify which of two possible conventions:
  - `R_protected_fold_partialsum = 1.128655` (S73B L_max=3 partial-sum ratio). Used by the project's canonical_constants.py entry (W1-M).
  - `R_protected_fold_gilkey = 0.492288` (Gilkey heat-kernel curvature polynomial ratio, L_max=infty, tau_fold=0.19). Used by any Einstein-Hilbert matching or CC computation referring to Seeley-DeWitt invariants in the continuum sense.

**Numerical results (S74 W2-O)**:
- Route A (S73B partial sum, L_max=7): **1.140699**
- Route B (Gilkey curvature, exact): **0.492288**
- Route C (zeta extrapolation L_max -> infty): **1.152815**
- Routes A and C agree to 1.06% (confirming Route A is within 1% of the partial-sum limit)
- Routes A/C vs B differ by ratio ~2.33 (STRUCTURAL, not numerical)

**Closed form for Route B at tau_fold**:
```
R_protected^B = (1/1000) * (500 - 32 * |Ric|^2 / R^2 - 28 * K / R^2)
              = (1/1000) * (500 - 32 * 0.126169 - 28 * 0.131246)
              = 0.492288
```
At tau=0 (bi-invariant): exact 0.4925 = 492.5/1000.

**Why the two values differ**:
- Route A/C: a_k = 0.5 * sum d_n * |lam|^{-k} for k in {0,1,2}. Individually divergent as L^{8-k} in Weyl regime; ratio finite because leading Weyl cancels. This is a TRUNCATED SPECTRAL ZETA ratio.
- Route B: a_k = Gilkey Seeley-DeWitt heat-kernel coefficient. a_0 ~ rank(S)*Vol, a_2 ~ R*Vol, a_4 ~ (500R^2 - 32|Ric|^2 - 28K)*Vol/360. These are polynomial in local curvature invariants, independent of L_max. This is a LOCAL CURVATURE POLYNOMIAL ratio.
- They are related through the Mellin transform of the heat trace but only via pole residues; at finite L_max the partial-sum ratio and the heat-kernel ratio are NOT equal.

**Cross-checks (all 5 PASS)**:
- X1: W1-M drift prediction 1.067% reproduced to 0.0002%
- X2: Gilkey at tau=0 gives exact 0.4925
- X3: Vol(SU(3)) cancels to machine epsilon (1.67e-16)
- X4: (4pi)^{-4} prefactor cancels to machine epsilon
- X5: Route C power-law fit residuals < 6.2e-6 (essentially perfect fit)

**Recommendation for S75**: Split the canonical constant into two:
```python
R_protected_fold_partialsum = 1.128655  # S73B L_max=3 canonical (W1-M)
R_protected_fold_gilkey = 0.492288      # Gilkey heat-kernel curvature ratio
```

**Files**: computations/s74_r_protected_triple.py/.npz/.png

**Status**: FAIL (structural, meaningful). The two conventions are both legitimate spectral observables; they just measure different things. Downstream usage must document which scheme.
