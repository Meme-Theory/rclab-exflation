---
name: S61 W9 QA-Connes workshop results
description: Key structural findings from W9 iterative workshop - dictionary corrections, ghost resolution, cutoff identification conjecture, shriek map correction
type: project
---

## S61 W9 Workshop Key Results (2026-03-28)

### Dictionary Corrections (R2, accepted from QA)
- a_2 maps to SINGLE-CELL stiffness (bulk modulus of one Voronoi cell), NOT lattice elastic modulus
- E_J = lattice stiffness (inter-cell spring constant), separate from a_2
- Sector B (BA modes) does NOT map to a_4 term (non-local vs local mismatch)
- Sector C (Leggett) does NOT map to fermionic action (bosonic collective vs fermionic)
- Casimir ratio descent = ASYMPTOTIC INTERACTION (not freedom). High-PW modes MORE coupled.
- 8/10 dictionary entries survive. Failed: a_2<->elastic modulus, sector<->SDW mapping.

### Ghost Problem Resolution (CQ1)
- 36 negative Hessian = internal-space analog of conformal factor problem in Euclidean gravity
- Resolution: contour rotation in Euclidean path integral (Gibbons-Hawking-Perry 1978 analog)
- Fold is dominant Euclidean saddle point. Physical masses = tunneling rates, not oscillation frequencies
- One-loop fermion determinant may flip some eigenvalues positive -> HESSIAN-ONELOOP-62 pre-registered
- 4 of 36 directions are pure gauge (U(2) isometry). 32 physical directions remain.

### Shriek Map Correction (CQ3, self-correction)
- eq NCG-3 from R1 was WRONG. Shriek map = standard fiber integration, NOT det(D_K)^{-1} weighted
- Confirmed by SHRIEK-FIBERINT-61 (exact to 2.2e-16)
- No regularization needed: D_K gapped (Delta=0.137), spectrum discrete, no van Hove divergence

### Cutoff Identification Conjecture (E3)
- Strutinsky gamma ~ 0.23 (Thomas-Fermi) vs London gamma ~ 0.19 (1/sqrt(D_s)) -- 23% discrepancy
- Entropy maximization gives gamma = 1.53 -- 8x too large, does NOT produce 0.23
- Dilaton and bootstrap methods uncomputed
- Identification Lambda_cutoff ~ 1/lambda_L is physically natural but NOT derivable from NCG axioms
- Pre-registered: CUTOFF-LONDON-62

### Sigma-Maximum Connection (CQ4)
- Sigma tachyon IS one of 36 directions (breathing mode = Sym^2(u(1)))
- But sigma instability (n=4.51>4, Yukawa origin) is INDEPENDENT of Hessian negativity (spectral action landscape)
- Tree-level Higgs 134 GeV stands WITHOUT sigma correction precisely because fold is a maximum
- Structural argument: M4xSU(3) gives better m_H than finite NCG because sigma correction is inapplicable

### Mode Conversion (E1)
- |A|^2 = 2.20 Born approximation gives 69% conversion. Expansion parameter 0.35 -> ~12% systematic error
- A-tensor is GEOMETRIC quantity (submersion property), inner fluctuation A is ALGEBRAIC (bimodule)
- For acoustic holography: total shriek map is FULL fiber integral, not decomposed by A-tensor
- A-tensor conversion characterizes INTERNAL STRUCTURE of integral, not physical signal splitting

### Pre-registered Gates for S62
- CUTOFF-LONDON-62: S_b(gamma) on SU(3) spectrum, test gamma=0.19 vs 0.23 vs constraint triad
- HESSIAN-ONELOOP-62: S_eff = S_b + (1/2) sum ln(lambda_n^2), check if any Hessian eigenvalue flips positive
- BDG-GAUGE-FRACTION-62: delta a_4^{BCS}/a_4 vs delta a_2^{BCS}/a_2

### QA R3 Answers to NQ1-NQ5 (W9-05)
- NQ1: DOS enhancement factor Q_B2=52 at flat band. Not stimulated emission but density-of-states amplification.
- NQ2: DM mass too high (3.6e14 GeV) for direct detection. GGE gas, not single particle. Meissner suppression 10^{-5}.
- NQ3: BA spectrum (31 modes) is correct. Geometric SA (992 modes) already smooth by Gilkey. Oscillatory content in collective modes.
- NQ4: Yes, from stored D_K eigenvalues. Hessian requires 72 perturbed diagonalizations (~10 min). Route (a) numerical.
- NQ5: t_BCS ~ 7.3 M_KK^{-1} ~ t_decay ~ 7 M_KK^{-1} (comparable, factor 1.04). Josephson adiabaticity (gap 93x) protects condensate.

### Final Convergence (W9-06, 12 items)
- CF-1 through CF-12a all ACCEPTED. No remaining corrections needed.
- CF-12a (Higgs 134 GeV stands because fold is maximum) is strongest new structural argument.
- CF-9 (Berry = NCG = A-tensor triple identification) is most consequential mathematical identification.

### Final Dissent (W9-06, 3 items)
- D-1 (mode conversion 69%): physical splitting vs integral structure. RESOLVABLE by BERRY-PROJECTION-62.
- D-2 (SA maximum interpretation): CC maximized vs Euclidean saddle. PARTIALLY RESOLVABLE by HESSIAN-ONELOOP-62.
- D-3 (gamma identification): 0.19 vs 0.23 vs 1.53. RESOLVABLE by CUTOFF-LONDON-62.

### S62 Priority Queue (W9-06 final)
- : #1 CUTOFF-LONDON-62, #2 BERRY-PROJECTION-62, #3 KZ-NS-62, #4 HIGGS-BCS-THRESHOLD-62, #5 HIGGS-ORDER-ONE-62
- Critical path: #1 and #2 parallel -> #3 (n_s). Higgs track (#4, #5) independent.
- Minimum viable S62: compute n_s (#1->#2->#3).
- P = 25% (16-37%), bimodal on n_s. PASS -> 40-55%, FAIL -> 8-12%.
