---
name: S49 Detailed Results
description: Full S49 results from QA perspective — Bragg closure, Leggett dipolar, alpha_s tension, analog horizon retraction, KZ identity
type: project
---

## S49 Results (2026-03-17) — 20 computations, 8 PASS, 7 INFO, 4 FAIL, 1 retraction

### Acoustic-Relevant Results

- **BRAGG-GOLDSTONE-49 INFO (CLOSURE)**: Bragg gap at KK scale (m=0.269 M_KK). eta=1/2 exact from Z_3
  phase rotation cos^2(pi/3)=1/4. 3D: same eta in all directions despite 4x anisotropy. 10% disorder
  survives. Z_3 quantization is TOPOLOGICAL — no parameter tunes eta toward 1.

- **CAVITY-RESONANCE-49 INFO**: 111 subsonic cavities on T^2. Largest at Z_3 center (R=1.237).
  omega_cav_min=0.800 M_KK vs omega_L1=0.070 M_KK (11.5x mismatch). Q~exp(23). Two-scale structure:
  acoustic hard (c/R~0.8) vs Josephson soft (sqrt(J/rho)~0.07). Different physics, no unification.

- **DIPOLAR-CATALOG-49 PASS**: Leggett mode breaks U(1)_7 with epsilon=0.00248. m_G=omega_L1=0.070 M_KK.
  omega_L1/m_req = 1.18 (18% from n_s target). FIRST mechanism at correct order in 12+ routes.
  Structural analog of 3He-A dipolar: H_J=-J_23 cos(phi_B2-phi_B3) breaks U(1)_7 because B2 carries
  K_7 charge +/-1/2 while B3 is neutral. 2/10 mechanisms break U(1)_7, 8/10 preserve.
  omega_L1/Delta_B2 = 0.095 (cf 3He: 10^{-3}).

- **ANALOG-TRAPPED-49 PASS (S48 RETRACTION)**: No superflow in BCS ground state (phi=0 everywhere).
  S48 "Mach 54" was amplitude gradient, not phase gradient. Acoustic spacetime globally static.
  Eikonal breakdown on 78.3% of T^2 (WKB diagnostic, not horizon).

- **KZ-3COMPONENT-49 PASS**: n=59.82 vs target 59.8 (0.04%). 163x improvement over S48.
  Additive LZ by su(3) decomposition: B2 93.3% (rho=14.023), B3 5.0%, B1 1.7%.
  Block-diagonal theorem confirmed: inter-sector coupling <0.04% during transit.

- **ALPHA-S-BAYES-49 FAIL**: alpha_s = n_s^2 - 1 = -0.069 (exact O-Z identity). 6.0 sigma from Planck.
  J_ij errors contribute 0% variance. Tension INCREASED from S48's -0.038 (finite-diff artifact).
  CMB-S4 would detect at 8 sigma or exclude at 20 sigma. Rigid prediction.

### Other Key S49 Results

- **FRIEDMANN-GOLDSTONE-49 INFO**: 5 Hubble-scale masses in gate window, all parameter-free.
  n_s tilt = 5.9e-117 (115 OOM short). CMB pivot at mode n=115, BZ boundary at n=16.
  Superfluid destroyed post-transit (rho_s=0 from GGE P_exc=1). Mass problem = CC problem.

- **FABRIC-NPAIR-49 PASS (conditional)**: N_eff=32, ec_fabric=1.586 > ec_min=1.264.
  CC crossing at tau*=0.417. J/E_C=0.152 (Mott crossover). CONDITIONAL on J_pair>0.096.

- **LEGGETT-TRANSIT-49 FAIL**: Leggett mode destroyed post-transit. Phase frozen (dt/T_L=1.25e-5).
  Wrong-sign gap equation: (1-2n_k)->-1 at P_exc=1. Delta_SC=0. omega_L=0.

- **LEGGETT-GGE-49 INFO**: N=1 interaction identically zero. omega=0.133=bare E_B3-E_B2.
  No collective content. Sum rule saturation prevents enhancement. PR(N=2)=50.8 (fragmented).

- **CONFORMAL-TRANSITION-49 PASS**: 4-zone Penrose diagram. Singularity direction-dependent.
  BCS = cosmic censor. WCH consistent (|C|^2 monotone).

- **COSMIC-CENSORSHIP-49 PASS**: Triple-layered: energy budget (65x deficit), BCS friction
  (Gamma=4424), no trapped surfaces (traceless K). tau_max=0.088 (free), 0.218 (from fold).

- **HFB-BACKREACTION-49 PASS**: 1.2% at nuclear g_ph=0.03. V state-independent (Peter-Weyl).
  CC crossing survives.

- **MULTI-T-FRIEDMANN-49 PASS**: w_0 shifts 25% toward DESI (multi-T). alpha shortfall 4.0x.

- **DESI-DR3-PREP-49 PASS**: B=20.9 (1D, preferred over LCDM). B=0.073 (2D, w_a kills it).
  Pre-registered: w_0=-0.509+/-0.079, w_a=-0.009+/-0.02.

- **NON-LI-TT-49 PASS**: All eigenvalues positive through tau=0.78. Casimir floor structural.

### New Closures (S49)
1. O-Z Friedmann mass for n_s (115 OOM short)
2. Bragg gap for n_s mass (KK scale, Z_3 quantized)
3. CMPP type transition at 0.537 (Type II locked)
4. Leggett mode post-transit (destroyed)
5. S48 analog horizons (amplitude != phase)
6. Cavity-Leggett unification (11.5x mismatch)

### Key New Constants
- eta_Z3 = 1/2 (impedance contrast, topological)
- omega_cav_min = 0.800 M_KK
- epsilon_Leggett = 0.00248 (U(1)_7 breaking)
- m_G = omega_L1 = 0.070 M_KK (Leggett Goldstone mass)
- m_req = 0.059 M_KK (n_s=0.965 target)
- alpha_s = n_s^2 - 1 = -0.069 (exact O-Z)
