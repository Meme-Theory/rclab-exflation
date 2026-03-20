---
name: session-49-leggett-gge-detail
description: S49 LEGGETT-GGE-49 INFO -- Leggett correlator trivial at N=1 (non-interacting), fragmented at N=2
type: project
---

## LEGGETT-GGE-49: INFO

### Key Finding
The Leggett relative-phase correlator C_L(t) in the GGE shows NO collective mode survival.

### N=1 Sector (Physical System)
- H_int(N=1) = 0 EXACTLY (density-density V*n_k*n_{k'} vanishes with 1 particle)
- Oscillation at omega = 0.133 M_KK = E_B3 - E_B2 (bare single-particle splitting)
- Enhancement = 1.00x (no pair physics possible with zero pairs)
- PR = 2.0 (two frequencies: +/- omega_sp)
- Nuclear analog: two-neutron transfer in doubly-magic nucleus with zero valence pairs

### N=2 Sector (Interaction Non-Trivial)
- ||H_int|| / ||H_free|| = 0.163 (16.3% interaction)
- Eigenvalues shift up to 0.78 M_KK
- Enhancement = 1.00x (sum rule saturation: total strength independent of V)
- PR = 50.8 (FRAGMENTED from PR=2.0 free into 122 transitions)
- Dominant frequency shifts 0.133 -> 0.432 M_KK (3.2x upshift from level repulsion)
- Nuclear analog: Landau damping of pair vibration above T_c

### Sum Rule Argument (Structural)
Non-energy-weighted sum rule: sum_n |<n|F|0>|^2 = <F^dag F>
This is independent of V. Enhancement = 1.00 at ALL N.
Broglia effect enhances SPECIFIC energy window, not total strength.
Infinite-T GGE averages over ALL states, erasing energy-window selectivity.

### phi_rel Independence
- Formally [H, phi_rel] != 0 (commutator norm 0.133 at N=1, 0.491 at N=2)
- This means phi_rel PRECESSES, NOT that it is a new conserved integral
- 9th integral would require [H, I_9] = 0 -- opposite of what was found
- phi_rel carries sector-transfer quantum numbers, not conservation laws

### Self-Correction (v1 -> v2)
v1 declared PASS based on formal criteria (C_L oscillates, phi_rel independent).
Self-check found N=1 is exactly non-interacting, making oscillation trivial.
Enhancement = 1.00 confirmed. Corrected to INFO.

### Confirms W1-H (Landau agent)
W1-H found Leggett mode ceases to exist post-transit (Delta=0, J=0).
W1-T confirms: even the CORRELATOR shows no collective content.
The ordered veil's integrability-protected GGE retains individual quasiparticle
numbers, not collective phase information.
