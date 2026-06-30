---
name: S74 W1-D E_C-RESOLUTION-74 Result
description: Canonical E_C^{OES,CG24} = 0.4643 M_KK via single-cell spectral invariant (Method A)
type: project
---

# S74 W1-D E_C-RESOLUTION-74 (2026-04-11)

**Verdict**: PASS. E_C^{OES,CG24} = 0.4643 M_KK.

## Three methods computed

| Method | Value (M_KK) | Physical content |
|---|---:|---|
| A - spectral invariant | 0.4643 | CANONICAL: Delta_OES from single-cell 8-mode Fock-space ED |
| B - Bogoliubov CG24 | 9.0098 | Phase-stiffness pair-addition on inter-cell graph |
| C - 4-cell 2nd-diff | 0.0610 | Josephson-softened charging curvature at integer filling |

Three distinct physical observables, not three estimates of one quantity.

## Canonical argument (Method A)

Delta_OES is a single-cell spectral invariant. Three structural reasons it survives on CG(24) unchanged:
1. 8-mode spectrum set by Jensen-deformed SU(3) fiber geometry within one C^2 cell
2. D_K block-diagonal in cell index (S58-S67 permanent)
3. Second-order perturbative correction (t/Delta_OES)^2 / N_cells^2 < 0.4%

The CG(24) inter-cell Josephson coupling contributes to the PHASE STIFFNESS (Route 3) but not to the pair-addition gap. Method A is what the S73A Route 2 physical identification was actually computing.

## Three-route R1/R2/R3 on CG(24)

- R1 (BCS compressibility): 12.39 M_KK (single-cell, graph-invariant)
- R2 (OES pair-addition): 0.4643 M_KK CANONICAL
- R3 (GL coherence): 0.01093 M_KK (1/N_cells scaling from 4-cell 0.0656)

Spread R1/R3 = 1134x (S73A 4-cell was 189x). This is NOT a finite-size artifact -- it reflects the true three-way split of distinct physical observables.

## PERMANENT RESULT

**Delta_OES is a graph-topology invariant on CG(24).** Delta_OES = 0.4643 M_KK survives the transition from single-cell (S73A) to full 24-cell tessellation because the 8-mode BCS spectrum is a property of the single-cell D_K eigendistribution, not of the inter-cell Josephson network. Finite-size corrections bounded by (t/Delta)^2 / N_cells^2 < 0.4%.

**The Bogoliubov pair-addition gap (Method B, 9.01 M_KK) is a DIFFERENT observable.** It measures the phase-stiffness contribution to pair transport across the Josephson graph. It is an order of magnitude larger than Method A but diagnoses a different process.

**The 4-cell 2nd-difference charging curvature (Method C, 0.061 M_KK) is yet another observable.** It measures the Josephson-renormalised charging compressibility at finite density, about 1/8 of the bare Delta_OES, consistent with deep-superfluid softening (t/U = 2.0).

## Regime

- t/U = 2.010 (Bose-Hubbard Mott boundary ~ 0.085 for 3D, so DEEP SUPERFLUID)
- E_J^{stiffness}/U = 15.17 (S55 criterion >50 is deep SF; this is crossover)
- At n_0 = 1.87 (S55 physical filling), E_J^{stiffness}/U = 9.4 (closer to Mott boundary in the stiffness convention)

## Files

- computations/s74_ec_resolution.py
- computations/s74_ec_resolution.npz (20 fields)
- computations/s74_ec_resolution.png

## Key insight for A_s budget

The A_s closure problem uses E_C = 0.4643 M_KK (Method A canonical) going forward. The Mott delta_OOM calculation should NOT use the Bogoliubov Method B value (9.01) because that conflates phase stiffness with pair-addition gap. The 189x spread between S73A routes was genuinely a three-way split of distinct observables, not a methodological ambiguity. The canonical Route 2 identification E_C = Delta_OES survives the 4-to-24 cell extension to within 0.4%.
