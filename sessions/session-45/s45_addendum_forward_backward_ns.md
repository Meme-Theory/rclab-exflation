# Addendum: Forward/Backward Pair Creation Asymmetry for n_s

**Date**: 2026-03-15
**Source**: S45 conversation — user identified that pairs "pulled to" vs "falling to" the q-theory equilibrium are physically distinct populations
**Status**: SANITY CHECK PASSED — launching full computation

---

## The Concept

The q-theory crossing at tau* = 0.209 is a thermodynamic attractor. Pairs created BEFORE the crossing (forward, tau < 0.209) and AFTER (backward, tau > 0.209 during overshoot/turnaround) are physically distinct:

- **Forward pairs**: Created while condensate exists (tau < 0.19) or has just died. BCS-dressed energies E_k = sqrt(lambda_k^2 + Delta^2). Carry K_7 condensate coherence.
- **Backward pairs**: Created during geometric overshoot/turnaround (no condensate). Bare energies E_k = |lambda_k|. No condensate quantum numbers.

## Sanity Check Result

Using singlet (0,0) eigenvalues at tau = 0.190, 0.209, 0.220:

| Sector | |beta_fwd|^2 | |beta_bwd|^2 | Ratio |
|:-------|:------------|:------------|:------|
| B1 (k≈0) | 2.55e-02 | 3.37e-08 | 755,000x |
| B2 (k≈1.2) | 2.30e-02 | 3.49e-08 | 659,000x |
| B3 (k≈1.8) | 1.34e-02 | 1.55e-05 | 865x |

- Forward pairs dominate by 10^3 to 10^6
- Ratio DECREASES with k → **RED TILT**
- Spread 874x across sectors — huge k-dependence
- Physics: Delta=0.770 >> eigenvalue change (0.001-0.013), so BCS dressing IS the asymmetry

## Why This Could Work Where Others Failed

Every prior n_s computation used a SINGLE pair creation event:
- KZ-NS: compare tau=0 to tau=0.19 (single-particle, Weyl wins)
- Collective RPA: compare condensed to uncondensed at tau=0.19 (no Weyl, too red)
- Acoustic: dispersion curvature (57-order scale gap)

This computation uses the INTERFERENCE between TWO populations arriving at tau* from opposite directions. The interference ratio is:
- NOT weighted by Weyl degeneracy (it's a RATIO, degeneracies cancel)
- k-dependent (because Delta/lambda_k varies across sectors)
- Red-tilted (forward pairs dominate more at low k)

## Pre-Registered Gate

**FWD-BWD-NS-45**:
- PASS: n_s in [0.955, 0.975] from forward/backward interference
- FAIL: n_s outside [0.80, 1.10]
- INFO: Mechanism produces red tilt but n_s not in Planck window
