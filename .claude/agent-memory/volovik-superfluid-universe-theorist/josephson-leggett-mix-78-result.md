---
name: S78 W3-D Josephson-Leggett Mixing result
description: S78 W3-D PASS gate. delta Omega_DM h^2 = -9.65e-3 from non-linear 3x3 mixing integral. Factor 0.737 of pre-reg -1.31e-2, within factor 2 band. Scaling exp 2.17e-4 DERIVED.
type: project
---

## S78-W3-D-JOSEPHSON-LEGGETT-MIX: PASS

**Why**: Tests whether Josephson-Leggett mixing correction to Omega_DM is derivable from first principles via non-linear integral (NOT linear rescale — Nazarewicz fix). Pre-registered -1.31e-2 BEFORE run, computed -9.65e-3 within factor 2.

**How to apply**: This is the phononic Leggett-channel DM correction. Use the 8% correction (Omega_DM_h2 = 0.120 -> 0.110) whenever future sessions need the Josephson-mixed Leggett DM baseline. The sign is STRUCTURAL (negative, mass softens via level repulsion with heavier partners).

### Key numbers
- Pre-registered: delta Omega_DM h^2 = -1.31e-2 (LOCKED before run)
- Computed: delta Omega_DM h^2 = -9.65e-3
- Factor ratio: 0.7368 (well within factor 2 PASS band)
- Scaling exponent d(ln Omega_DM)/d(ln n_slow) = 2.17e-4 (DERIVED, not unity)
- Analytic vs numerical agreement: 0.50%
- L-character of Leggett-like hybrid: 0.9960 (high retention)
- PT2/diag agreement: 0.43% (weak-J regime confirmed)
- Direct/primary cross-check ratio: 1.316 (within factor 2)
- Verdict: PASS (all 6 cross-checks PASS)

### Physics / Dimensional analysis
- V_off = J * omega_L * Delta_BCS (second-order PT coupling scale between collective Leggett phonon at omega_L and quasiparticle at gap scale Delta)
- V_off_C2 = 0.933 * 0.138 * 0.464 = 0.0598 M_KK^2 (dominant, J_C2 channel)
- V_off_u1 = 0.038 * 0.138 * 0.464 = 0.00243 M_KK^2 (weak, J_u1 channel)
- 3x3 H_mix in mass^2 basis: [L, B1_partner, B3_partner]
- Leggett-like hybrid: m = 0.1235 M_KK (softened from 0.138 by 10.5%)
- Mixing softens mass via level repulsion (lowest eigenvalue attracted down)

### Convention pins (LOCKED)
- delta Omega_DM h^2 derived FROM FIRST PRINCIPLES via non-linear integral (NOT linear rescale)
- J-coupling sign: positive in Hermitian off-diagonal slot
- Off-diagonal B3: Leggett couples to B3 via J_C2 (4-bond coset)
- Mixing parameter: ANGLE theta (not off-diag magnitude)
- GGE multipliers lambda_n from S77 GGE-OCC (extractable verified)
- Omega_DM formula: linear GGE thermal (Section 0.7)
- Four-tuple tag: (delta_OmegaDM_h2=-9.65e-3, scheme=f*, convention=linear-GGE-thermal, L_max=10)

### Cross-checks (all 6 PASS)
1. Mixing-angle (WHAT): sin^2 in [1.39e-5, 4.01e-3]
2. Leggett DOS (HOW MUCH): rho_L=896.3, rho_B1=1.0, rho_B3=27.0
3. Red-shift integration (WHEN): a_prod/a_0 = 3.16e-30
4. Direct thermal-history (independent path): ratio 1.316 (factor 2 OK)
5. CPT preserved: all mass^2 eigenvalues real+positive
6. chi_2 unchanged (S77 W1-D): unitarity 60.0109 = 60.0109

### Files
- Script: computations/s78_josephson_leggett_mix.py
- Data: computations/s78_josephson_leggett_mix.npz
- Plot: computations/s78_josephson_leggett_mix.png (6 panels)

### Substrate framing
Omega_DM is the cosmological density of Leggett-mode GGE relic quasiparticles (inter-band coherence modes of the fiber's spectral structure), not a DM particle in spacetime. Josephson J-couplings are phonon-channel stiffnesses on the 32-cell tessellation (S47 TEXTURE-CORR-48 provenance). The mixing is substrate -> spectral moments -> emergent cosmology. Volovik UHD Ch. 32 (3He-B Leggett mode) is the direct structural analog.

### Session
S78 W3-D (2026-04-15)
