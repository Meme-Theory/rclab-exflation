---
name: S74 W3-D GS-OVERLAP-CG24-74 Result
description: Josephson GS overlap on CG(24) Laplacian; INFO verdict; structural theorem kappa_LLY(CG24) = +1/3 overturns S73A workshop assumption
type: project
---

# S74 W3-D GS-OVERLAP-CG24-74

**Date**: 2026-04-11
**Gate verdict**: **INFO**

## Headline Numbers
- F_A (flat Mott closed form) = 0.4043  [in PASS band 0.38-0.50]
- F_B (Mott with CG24 variance)  = 0.2558  [below INFO]
- F_C (Debye-Waller per site)    = 0.9299  [above INFO]
- F_D (density amplitude)        = 0.6391  [above INFO]
- Spread ratio F_C / F_B = 3.64

**Why:** The pre-registered PASS band assumed F_CG24 ~ F_1j with a ~10% negative correction. The actual computation reveals four valid fidelity definitions that disagree by factor 3.64, and the CG(24) correction sign is OPPOSITE to the workshop's assumption (which was based on assumed negative Ollivier curvature).

**How to apply:** Report F_1j = 0.4043 as the flat closed form (matches S73A workshop target). Report CG(24) as INFO with the four definitions shown. For future A_s budget discussions, F_CG24 is bounded ABOVE by F_1j (the CG(24) graph correction goes in the MORE coherent direction under Debye-Waller/density interpretations, which bounds the Mott channel's decoherence OOM above).

## Structural Theorem (PERMANENT)
**kappa_LLY(CG24) = +1/3 (exactly)**

The Lin-Lu-Yau Ricci curvature of the Cayley graph of S_4 on the transposition generating set is exactly +1/3. Classical Ollivier at alpha=0 is 0 (no common neighbors of adjacent vertices). The positive curvature reflects:
- Vertex-transitive AND distance-transitive structure
- Generating set closed under conjugation
- Maximal symmetry among 6-regular triangle-free graphs

This OVERTURNS the S73A phonon-first-hawking workshop assumption kappa ~ -0.1 "typical for triangle-free 6-regular graphs." CG(24) is NOT a generic random expander; it is a distance-transitive Cayley graph with positive Ricci curvature.

**Why:** Propagates to all curvature-dependent quantities on CG(24): phase-variance correction, GSL rate bounds, spectral-gap optimality arguments.

**How to apply:** Whenever a computation assumes or uses the Ollivier curvature sign on CG(24), use +1/3 (LLY) not -0.1. This permanently closes the workshop assumption channel and any downstream results that depended on it.

## Spectral Invariant R_spectral
R_spectral(CG24) = (1/N) sum_{lambda>0} lambda_alpha^(-1/2) = 0.4002 (exact)

Decomposition:
- lambda=4 (mult 9): contribution 0.1875
- lambda=6 (mult 4): contribution 0.0680
- lambda=8 (mult 9): contribution 0.1326
- lambda=12 (mult 1): contribution 0.0120

**Identity (permanent)**: sigma_phi^2(CG24 on-site) = sigma_sj^2 * R_spectral for any vertex-transitive graph. Independent of E_C, E_J. The CG(24) per-site phase variance is 2.5x SMALLER than an isolated junction (R_spectral < 1 means stiffer network).

## Bogoliubov Variances (at canonical E_C = 0.4643, E_J = 7.042)
- sigma_sj^2 = sqrt(2 E_C/E_J) = 0.3631
- sigma_phi^2(CG24 on-site) = 0.1453
- sigma_phi(CG24) = 0.381 rad (RMS phase noise per site in harmonic approx)

## Workshop Formula Error (S73A phonon-first-hawking)
The formula F = (2/pi)^(N/4) * (E_J/E_C)^(N/8) stated in the S73A workshop has:
1. SIGN error: should be (E_C/E_J)^(N/8) with opposite sign
2. With N=2 and corrected sign: gives F_1j = sqrt(2/pi)*(E_C/E_J)^(1/4) = 0.4043 (the physical Mott single-junction overlap)

The correct formula is F_1j = sqrt(2/pi)*(E_C/E_J)^(1/4), NOT the stated form.

## A_s Budget Implications
- Does NOT add a new delta_OOM contribution to the budget.
- Provides independent check of W2-F MOTT-REFINED-CG24-74.
- The graph correction BOUNDS the Mott channel decoherence ABOVE (not below) — contra workshop expectation.
- F_1j = 0.4043 consistent with W2-F delta_OOM_Mott = 0.141 (the Mott-refined closure).

## Files
- `computations/s74_gs_overlap_cg24.py`
- `computations/s74_gs_overlap_cg24.npz`
- `computations/s74_gs_overlap_cg24.png`

## Cross-References
- W1-D E_C-RESOLUTION-74: canonical E_C = 0.4643 M_KK (Method A)
- W2-F MOTT-REFINED-CG24-74: delta_OOM_Mott = 0.141
- S55: E_J stiffness = 7.042 M_KK
- S73A phonon-first-hawking workshop: carry-forwards #6, #9 (consolidated here)
- S73A Delta_OES / MOTT-CHARGE-NOISE W1-E: F = 0.461 (different definition, Mott noise sum)
