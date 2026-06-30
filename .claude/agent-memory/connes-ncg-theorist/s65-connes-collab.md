---
name: S65 Connes Collab Review
description: S65 key NCG results -- a_0/a_2=C/R universal theorem, KO=0 correction, BCS+1loop n_s, a_3=0, CC wall fully mapped, 11 geometric routes closed
type: project
---

## S65 Connes NCG Collab Review Summary

**Date**: 2026-04-03
**File**: `sessions/archive/session-65/session-65-connes-collab.md`

### My Computations (3)
1. **W3-A BCS-NS-FULL-65 = INFO**: n_s = 0.9590 (1.40 sigma from Planck). BCS dominates (+0.0031), 1-loop opposes (-0.0010). Cross-term 8.4%. Running -0.039 (6x Planck).
2. **W6-D SDW-A3-65 = FAIL**: a_3 = 0 structurally. Three proofs. Theta-vacuum CC CLOSED.
3. **W7-C INHOM-CC-65 = INFO**: Volume cancellation Q=C_Q/R. Jensen-mean shift: 9/36 modes improve Q but best delta ~8.6e-3*eps^2. Negligible.

### Key Structural Results
- **a_0/a_2 = C_Q/R**: Universal for ALL left-invariant metrics on SU(3). 36D -> 1D.
- **KO-dim(SU(3)) = 0, not 6**: W1-C self-correction. KO=6 is FINITE triple only. Product KO needs analysis.
- **B/F asymmetry = 0 exactly**: No B/F decomposition in SA on Riemannian triple.
- **All 11 geometric CC routes CLOSED**: Jensen, VP descent, orbifold, nonlocal f, EIH, Mott, a_3, torus, U(1) collapse, inhomogeneous, vortex.

### Recommendations for S66
1. Entropy SA f_S from Paper 15 -- non-monotone cutoff, different moment ratios
2. Finite-mu SDW coefficients from Paper 16 -- Bessel corrections O(1) at mu=0.82
3. Product KO-dim analysis (KO(M^4)=4 + KO(SU(3))=0 = 4, conflicts with verified J^2=+1)
4. Paper 28 truncation error bounds for n_s at L_max=3
5. Paper 33 minimal twist for Yukawa generation hierarchy
6. Papers 34-35 random NCG distribution of a_0/a_2

### CC Wall Status
**Why**: a_0/a_2 = C_Q/R for left-invariant metrics. R bounded above on physical metrics. Problem is FUNCTIONAL not GEOMETRIC.
**How to apply**: CC work must now target the spectral functional (which f?) not the fiber geometry (which g_K?). Papers 15-16 provide the only physically motivated alternatives.
