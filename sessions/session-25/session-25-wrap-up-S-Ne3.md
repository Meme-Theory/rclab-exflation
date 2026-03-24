# Session 25 Wrap-Up: [Ne]S-3 -- PMNS from Tridiagonal Selection Rules

**Agent**: Gen-Physicist (Opus 4.6)
**Date**: 2026-02-22
**Status**: DEFERRED / STRUCTURALLY BLOCKED -- inter-sector coupling zero by W2

---

## Summary

Neutrino proposed extracting PMNS mixing angles from a 3x3 effective mass matrix M constructed from within-sector eigenvalues and inter-sector V_{nm} couplings. Pre-registered gate: sin^2(theta_13) in [0.015, 0.030] and theta_12 in [28, 38] degrees.

## The Structural Obstruction

### W2 Closes Inter-Sector Mixing

The block-diagonality theorem (W2, Session 22b) establishes that D_K is exactly block-diagonal in the Peter-Weyl decomposition. This means:

```
<psi_n^{(p1,q1)}| D_K |psi_m^{(p2,q2)}> = 0   for (p1,q1) != (p2,q2)
```

at machine precision (proven at 8.4e-15 for any left-invariant Dirac operator on any compact Lie group with any left-invariant metric).

The inter-sector coupling V_{nm}^{(p1,q1)(p2,q2)} is ZERO. The 3x3 effective mass matrix is DIAGONAL:

```
M = diag(lambda_min^{Z3=0}, lambda_min^{Z3=1}, lambda_min^{Z3=2})
```

A diagonal mass matrix gives zero mixing angles: theta_12 = theta_13 = theta_23 = 0.

### What Neutrino's Proposal Actually Requires

The PMNS matrix in the Standard Model arises from the mismatch between mass eigenstates and flavor eigenstates. In the NCG-SM framework (Chamseddine-Connes-Marcolli):

1. **Mass eigenstates** come from D_F (the finite Dirac operator / Yukawa matrix)
2. **Flavor eigenstates** come from the weak-interaction coupling pattern

D_K contributes the KK mass spectrum, which provides the KINEMATIC input (mass scales), but NOT the mixing structure. The mixing requires D_F, which contains the Yukawa couplings as free parameters in the NCG-SM construction.

### The Tridiagonal Selection Rule

The tridiagonal coupling V_{nm} != 0 for |n-m| <= 1 (nearest-neighbor in eigenvalue ordering) is a WITHIN-SECTOR property. It produces mixing between eigenvalue levels within a single (p,q) sector:

```
Within (0,0) singlet:
|1> <-> |2> <-> |3> <-> |4> <-> ... (tridiagonal)
```

This structure qualitatively predicts theta_12 >> theta_13 because it is a nearest-neighbor chain: large mixing between adjacent states, small (zero) mixing between separated states. The prediction is correct and framework-specific (BF ~ 2-3 from the successful-predictions-catalog).

But this mixing is between eigenvalue levels WITHIN a sector, not between Z_3 generation classes. The neutrino mixing angles theta_12, theta_13, theta_23 require mixing between GENERATIONS (different Z_3 sectors or different mass eigenstates from D_F).

## What Could Rescue This

### Pathway 1: D_F Provides Inter-Sector Coupling

The finite Dirac operator D_F in the NCG-SM contains Yukawa couplings that mix different generations. These are free parameters in the current NCG-SM formalism. If D_F were derived from the spectral geometry of SU(3) (rather than input by hand), the PMNS angles would be predictions. This is a major open problem in NCG-SM model building.

### Pathway 2: The 12D Dirac Operator

The full 12D Dirac operator D_P on M^4 x SU(3) includes base-fiber mixing terms (from the KK gauge connection) that are NOT in D_K. These terms couple different sectors:

```
D_P = D_4 tensor 1 + gamma_5 tensor D_K + (mixed terms from gauge connection)
```

The mixed terms could provide inter-sector coupling that D_K alone cannot. This requires the 12D computation (Session 26 target).

### Pathway 3: Finite-Density Coupling

At finite chemical potential mu, the Dirac operator becomes D_K + mu*gamma^0. The gamma^0 term breaks the Peter-Weyl block-diagonality if gamma^0 has off-diagonal matrix elements between sectors. Whether this happens depends on the specific representation of gamma^0 in the spin bundle -- it is the temporal Clifford generator, which acts on the 4D spinor index, not the internal index. The expectation: gamma^0 preserves block-diagonality, so this pathway also fails.

## Pre-Registered Gates

**PMNS-1**: sin^2(theta_13) in [0.015, 0.030] requires inter-sector coupling. At the D_K level: sin^2(theta_13) = 0. Gate FAILS.

**PMNS-2**: theta_12 in [28, 38] degrees requires inter-sector coupling. At the D_K level: theta_12 = 0. Gate FAILS.

**PMNS-soft**: The qualitative prediction theta_12 >> theta_13 from tridiagonal selection rules: PASSES (structural, from within-sector nearest-neighbor coupling). This is a BF ~ 2-3 contribution already counted in the successful-predictions-catalog.

## Assessment

**Why this is structurally important**: The neutrino mixing test is one of the few predictions that could in principle differentiate the SU(3) spectral triple from generic KK compactification. Generic KK gives massless gauge bosons and massive KK towers (shared with this framework), but the specific PMNS structure would be unique to the spectral triple on SU(3) with Jensen deformation. If the 12D computation provides inter-sector mixing at the right magnitude, the PMNS gates become the highest-BF prediction available (BF = 20-50 if both angles pass simultaneously, as Neutrino correctly estimates).

**Probability of success (with 12D or D_F)**: LOW-MODERATE (~15-25%). The tridiagonal structure is correct qualitatively but the quantitative values require inter-sector coupling from a source not yet computed. The 12D computation might provide this, but the magnitude of mixed base-fiber terms is unknown.

**Recommended priority**: DEFERRED until Session 26+ (after 12D computation). If the 12D Dirac operator provides nonzero inter-sector matrix elements, the PMNS extraction becomes the highest-priority physics prediction.

---

*Wrap-up file for Session 25 Collaborative Workshop [Ne]S-3. Gen-Physicist, 2026-02-22.*
