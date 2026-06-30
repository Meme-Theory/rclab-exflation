---
name: S74 BCS-GAP-K-SCALE-74 result (W4-GG)
description: BCS gap inverse coherence length in acoustic channel, redshifted to LSS — INFO (ultra-UV), closes Framework section 10 deferred #10
type: project
---

# S74 BCS-GAP-K-SCALE-74 Results (W4-GG)

**Gate**: INFO. k_BCS = 1.8635e+25 Mpc^{-1}, above the [1e-4, 1] PASS band by 25 OOM.

**Why**: Framework section 10 deferred item #10 — BCS gap imprint on LSS P(k). Independent, computable from canonical constants alone. Closes this deferred item with a clean structural answer: the mechanism exists but the scale is unobservable.

**How to apply**: When anyone asks about a BCS feature in P(k) at observable k, cite this gate. The BCS gap alone cannot print any feature at BOSS/DESI/Euclid scales; redshift crushes it 25 OOM into the UV. Only the Leggett-channel k_J (W4-FF) has a shot at the LSS window.

## Derivation summary (Landau analysis)

1. Natural units: k_BCS_nat = Delta_BCS / c_Gold = 0.4642547 / 0.915 = 0.50738 (M_KK)
   - Interpretation: inverse coherence length in the Goldstone sound channel (the one that propagates into the emergent metric). This is the substrate analog of k_BCS = Delta / v_F from ordinary BCS.
   - The choice of c_s = c_Gold is unique: among the mode speeds in the phonon spectrum, only the Goldstone acoustic branch sources emergent curvature. Leggett/Higgs modes are gapped.

2. Physical at fold: k_BCS_fold = k_BCS_nat * M_KK_gravity = 3.7692e16 GeV

3. Redshift via S66 canonical expansion history:
   - a_fold/a_today = T_CMB / M_KK_gravity = 3.1616e-30
   - N_e_total = ln(M_KK/T_CMB) = 67.93 (matches s66_two_component.py line 355)

4. Today: k_BCS_today = k_BCS_fold * (a_fold/a_today) = 1.1917e-13 GeV = k_BCS_nat * T_CMB
   - The M_KK cancels EXACTLY: the observable k is k_BCS_nat * T_CMB, independent of the fold scale.

5. In Mpc^{-1}: k_BCS_today * Mpc_to_GeV_inv = 1.8635e+25 Mpc^{-1}

## Key permanent identity

**k_BCS_today = (Delta_BCS / c_Gold) * T_CMB** in natural units, independent of M_KK.

This is a clean structural statement: the observable BCS k-scale is pinned to the CMB temperature (acoustic) rescaled by the dimensionless Delta/c_Gold. No hidden dependence on the fold scale. The M_KK cancels because it enters multiplicatively in k_BCS_fold and inverse-multiplicatively in a_fold/a_today.

## Cross-checks (all exact)

- Dimensional consistency: [E]/[v] = [k] in natural units. Check.
- Algebraic reduction: residual = 0.000e+00 between direct calculation and k_BCS_nat * T_CMB.
- Hubble reference: H_0 / c = 2.25e-4 Mpc^{-1}, recovering standard from H_0 = 67.4 km/s/Mpc.
- Expansion consistency: N_e = 67.93 matches S66 two-component Friedmann integration.

## Comparison to LSS

- LSS window: [1e-4, 1] Mpc^{-1}
- k_BCS: 1.86e25 Mpc^{-1}
- Ratio k_BCS / (H_0/c): 8.29e28 (log10 = 28.92)

## Assessment

**PERMANENT (BCS-GAP-K-SCALE-74)**: The substrate BCS gap imprints its acoustic inverse coherence length at ~1.86e25 Mpc^{-1} today. Invisible to every present or planned LSS survey. The mechanism exists as claimed but is observationally inert in P(k).

This is NOT a failure — it is a structural theorem constraining where the gap can and cannot appear. Any claim of a BCS P(k) feature at observable scales would need a separate redshift mechanism (sub-horizon exit scale, or non-substrate late-time restoration). Currently not posited by the framework.

The relevant k-imprint to watch at LSS is the Leggett-channel Jeans scale k_J (W4-FF), not the BCS gap.

## Files

- Script: `computations/s74_bcs_gap_k_scale.py`
- Data: `computations/s74_bcs_gap_k_scale.npz`
- Working paper: Section W4-GG of `sessions/archive/session-74/session-74-results-workingpaper.md`
