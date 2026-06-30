---
name: S84 W7a-74 DET-P-K-THEORY FAIL — det(P)=1 has no K-theoretic uplift to Witten 1998
description: S84 gate DET-P-K-THEORY returned FAIL with homotopy_level=1 (weak Z-linear map only); det(P)=1 is a purely spectral-triple identity with no D-brane K-theoretic parent
type: project
---

# S84-DET-P-K-THEORY: FAIL (homotopy_level=1)

**Gate**: S84-DET-P-K-THEORY
**Verdict**: FAIL
**value**: 1 (homotopy_level: weak Z-linear map exists but not an iso or homotopy equivalence)
**sha256**: def5d0cdb8a39d16017820a602cb8821fefcbbc8720700f3eb6e5b095d4af1d2

**Why**: No K-theoretic uplift of det(P)=1 to Witten 1998 D-brane anomaly cancellation
exists at either the structure-preserving K_0 level (PASS) or the classifying-space
homotopy equivalence level (INFO). Four obstructions identified:

1. K_0 rank mismatch: rank K_0(A_F) = 3 (A_F = C + H + M_3(C)) vs rank K^0(X) = 1
2. Torsion mismatch: K_0(A_F) torsion-free vs KO^6(pt) = Z/2 torsion
3. Witten integral: ch_0 * A-roof(TM^4) = 16 * 1 = 16, but Witten single-brane requires 1
4. Bott period: 16 mod 8 = 0 (KO), 16 mod 2 = 0 (K); neither hits 1

**How to apply**:
- Use this result as the authority on the det(P)=1 / Witten D-brane question — the
  answer is SETTLED: they are distinct ledgers.
- For any future claim that "string theory explains det(P)=1 via D-brane anomaly
  cancellation": invoke this gate's FAIL verdict and the four obstructions.
- For correspondence table maintenance: add as new ANTI-CORRESPONDENCE (#30) in the
  "no-Bott-structure, no-unitary-target" cluster (joining no-T-duality, no-S-duality,
  no-Hagedorn from S64).
- Rep-content embedding (§W7-72 HET-DECOMP PASS) and K-theoretic identity uplift
  (this gate FAIL) are structurally DIFFERENT tests. A framework can pass one and
  fail the other without inconsistency — this pattern is consistent with Scenario A
  of the plan's §VII.N decision tree: rank-6 gear-machine classification UPGRADES
  because it hosts SM content while its core identity remains framework-independent.

**Correspondence table implication**: one new ANTI-CORRESPONDENCE entry. Framework
continues to DIVERGE from string theory at the structural-identity level while
CONVERGING toward Volovik emergent gravity (consistent with post-S64 memory).

**Script**: `computations/s84_w7a_det_p_k_theory.py`
**Data**: `computations/s84_w7a_74_data.npz`
**WP section**: `sessions/archive/session-84/session-84-w7-workingpaper.md` §W7-74
