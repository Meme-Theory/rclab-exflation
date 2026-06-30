---
name: S77 GGE Occupation Correction
description: FAIL. GGE occupation correction to chi_2 is 4-5 OOM too small to resolve 8.2% direct-conjecture overshoot. BCS modes = 6.9e-7 of weighted spectrum.
type: project
---

## S77-C7-GGE-OCC: FAIL

**Gate**: delta_chi_2 in [-0.10, -0.07] for PASS. Computed: -9.63e-6 (Mechanism B, bosonic). FAIL: |delta| < 0.01.

**Key numbers**:
- chi_2(L=9) = 0.741419, Omega_Lambda = 0.685, overshoot = 8.2%
- delta_chi_2 needed: -0.0564
- delta_chi_2(A, Bogoliubov): -4.22e-6 (correct sign, 4.1 OOM too small)
- delta_chi_2(B, bosonic pair): -9.63e-6 (correct sign, 3.8 OOM too small)
- delta_chi_2(max, remove BCS): +3.76e-7 (even total removal insufficient)
- BCS modes: 284 / 408,721,760 = 6.9e-7 of d^2-weighted mode count at L=9

**Why**: chi_2 is a spectral fill factor over 408M modes. GGE excites 8. Mode fraction is 10^{-7}. No occupation correction on 8 modes shifts a 10^8-mode average by 7.6%.

**How to apply**: CLOSES GGE occupation route to direct-conjecture resolution. Overshoot resolution requires either: (a) factor-3 Friedmann normalisation (chi_2/3 route, 0.44 OOM gap), or (b) L_max -> infinity chi_2 convergence.
