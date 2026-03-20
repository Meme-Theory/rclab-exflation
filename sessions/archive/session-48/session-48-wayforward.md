# Session 48 Way Forward

**Source**: 4 collaborative reviews (Volovik, Einstein, Schwarzschild-Penrose, Nazarewicz, Tesla)
**Date**: 2026-03-17

---

## Reviewer Convergence

All 4 reviewers independently converge on the same structural conclusion: the mass problem and the CC problem are the same problem, and the solution lives at the fabric-cosmological interface, not at the single-cell BCS level. The Leggett mode is unanimously recognized as the session's strongest positive. The Zak phase retraction is unanimously endorsed.

---

## Unique Contributions by Reviewer

### Volovik
- The 3He dipolar interaction (external to BCS Hamiltonian) is the structural template for U(1)_7 breaking
- **84-order scale crisis**: J * K_pivot^2 ~ 3.7 M_KK^2 dominates m_G^2 ~ 10^{-84} M_KK^2. Even the correct mass (m ~ H_0) is overwhelmed by the Josephson coupling at KK scale. The Friedmann computation must address this ratio, not just produce m ~ H.
- Four mass candidates analyzed: Hubble damping (3 OOM short), horizon finite-size (3 OOM short), GGE as explicit breaking (UV scale, fails), running stiffness (requires near-criticality)
- Updated 9-correspondence table with S48 results. Correspondence 5 modified: K_7 is number charge (3He-B class), not chiral charge (3He-A)

### Einstein
- Trace theorem classified as a *principle* (Birkhoff analog): spectral action is the correct functional for gravity, wrong functional for Goldstone sector
- **Three-observer gedankenexperiment**: Observer A (single cell, m=0), Observer B (boundary, omega_L), Observer C (fabric, m_G). Only C sees the mass. Computation must be fabric-level by construction.
- **EIH constraint**: Goldstone mass must be parameter-free — determined entirely by rho_s, J, N_cells, GGE initial conditions
- Multi-T Euler failure (W5-C) means standard Friedmann equation needs modification for GGE relic
- Self-tuning runaway identified as Weinberg's no-go theorem applied to Goldstone sector

### Schwarzschild-Penrose
- **Geometric phase transition at tau=0.537** elevated to "most geometrically significant new discovery"
- [0.537, 0.78] window identified: mixed-sign sectional curvature but SEC still holds. Previously unrecognized regime.
- Transition is NEC-violation precursor: negative sectional curvature before Ricci eigenvalue reaches zero
- Analog horizons classified as 1D sonic surfaces on T^2, not 2D trapped surfaces. Penrose diagram is (1+1)D.
- TT transversality theorem linked to Kruskal vs Schwarzschild coordinate distinction
- lambda_min local maximum at fold = Regge-Wheeler photon sphere analog
- 5 pre-registered computations for the tau=0.537 regime

### Nazarewicz
- **Geometric phase transition as U(1)_7 breaking source** (new idea): if two vacua exist (fold at 0.19 and post-transition at >0.537), their phase mismatch is explicit breaking. Breaking parameter epsilon from WKB tunneling through curvature barrier. Nuclear analog: proton-neutron phase mismatch at high spin.
- **Fabric pair number**: 32 cells x 1 pair = 32 effective pairs. BCS-BEC crossover (N=1) transitions to weak-coupling BCS (N=32). PBCS/BCS ratio improves from 0.63 to ~0.9. CC crossing shortfall shrinks from 2.5x to 1.7x.
- 8 nuclear benchmarks all within range (quantitative table provided)
- Leggett mode recognized as multi-band pairing vibration (Broglia analog). May add 9th conserved integral to GGE.
- Bayesian alpha_s uncertainty analysis from J_ij propagation proposed

### Tesla
- **Mass problem as impedance mismatch**: Z_int/Z_cosmo ~ 10^{120}. Goldstone mass is the frequency where impedance matching allows radiation from crystal to cosmological background.
- **Bragg reflection as mass mechanism**: 32-cell tessellation is a phononic crystal for Goldstone waves. Bragg gap at k_BZ from Z_3 wall impedance contrast (sigma = 4.50 M_KK) could produce effective mass from geometry alone.
- omega_L2/omega_L1 = 1.529 is 0.17% from phi_paasch (flagged, likely coincidence given V-matrix uncertainties)
- **Cavity resonance unification**: if analog horizon normal modes match Leggett frequencies, Leggett modes are cavity resonances of the internal analog spacetime
- Full frequency hierarchy documented (9 frequencies, 2 orders of magnitude, zero free parameters)
- KZ cross-check can be sharpened with 3-component formula (u(1) separated from su(2))

---

## S49 Computations (Priority-Ordered)

### Tier 1 — Central Questions

| # | Computation | What | Agent | Input |
|:--|:-----------|:-----|:------|:------|
| 1 | FRIEDMANN-GOLDSTONE-49 | Fabric phase field coupled to Friedmann through rho_s. GGE initial conditions. Must be parameter-free (EIH). Must address 84-order scale crisis. | Volovik + Landau | s47_rhos_tensor, s47_texture_corr, s38 GGE data |
| 2 | FABRIC-NPAIR-49 | 32-cell Josephson network, N=1/cell. Effective N_pair? CC crossing recomputed at fabric level. | Nazarewicz | s48_npair_full, s47_texture_corr |
| 3 | BRAGG-GOLDSTONE-49 | Goldstone dispersion on 32-cell phononic crystal. Bragg gap at k_BZ? Z_3 wall impedance contrast. | Tesla/Landau | s48_curv_extend (Z_3 wall), s47_texture_corr |
| 4 | GEOMETRIC-BREAKING-49 | WKB tunneling between fold (0.19) and post-transition (>0.537). Phase mismatch = explicit U(1)_7 breaking? Compute epsilon. | Nazarewicz | s48_curv_extend, s40_hessian_offjensen |
| 5 | MULTI-T-FRIEDMANN-49 | Friedmann equation for 8-temperature GGE (negative Euler pressure). Does non-standard thermodynamics shift w_0? | Einstein/Volovik | s48_dmde_refine, s39_richardson_gaudin |

### Tier 2 — Structural

| # | Computation | What | Agent | Input |
|:--|:-----------|:-----|:------|:------|
| 6 | CONFORMAL-TRANSITION-49 | Penrose diagram of internal manifold through tau=0.537. Conformal boundary topology change. | SP | s48_curv_extend |
| 7 | ANALOG-TRAPPED-49 | theta_+/- at Mach-1 contour on T^2. Trapped surface or sonic surface? | SP | s48_volovik_string (Akama-Diakonov data) |
| 8 | LEGGETT-TRANSIT-49 | Leggett EOM coupled to tau(t) during transit. Post-transit amplitude. 9th conserved integral? | Nazarewicz | s48_leggett_mode, s38 transit data |
| 9 | HFB-BACKREACTION-49 | Fully self-consistent Dirac-BCS iteration (Delta modifies D_K which modifies Delta). 3.7% backreaction effect on crossing. | Nazarewicz | s48_hfb_selfconsist |
| 10 | CAVITY-RESONANCE-49 | Normal modes of analog cavity bounded by Mach-1 horizon. Match Leggett frequencies? | Tesla | s48_volovik_string |
| 11 | GAUSS-CODAZZI-TRANSITION-49 | K_cross at tau=0.537. Backreaction on 4D Einstein tensor. | SP | s48_curv_extend, s45_kretschner |

### Tier 3 — Observational Predictions

| # | Computation | What | Agent | Input |
|:--|:-----------|:-----|:------|:------|
| 12 | ALPHA-S-BAYES-49 | Bayesian uncertainty on alpha_s = -0.038 from J_ij errors. Does error band reach Planck? | Nazarewicz | s48_aniso_oz, s46_bayesian_gp |
| 13 | KZ-3COMPONENT-49 | 3-component KZ formula (u(1) separated). Sharpen 6.5% to <3%? | Tesla/Gen | s48_curv_extend (KZ data) |
| 14 | LEGGETT-PHI-SCAN-49 | omega_L2/omega_L1 vs tau. Converges to phi_paasch at any tau? | Tesla/Landau | s48_leggett_mode |
| 15 | DESI-DR3-PREP-49 | Bayes factor for framework vs LCDM at corrected alpha range. Ready for DR3 comparison. | Nazarewicz | s48_dmde_refine |

### Tier 4 — Geometric Characterization

| # | Computation | What | Agent | Input |
|:--|:-----------|:-----|:------|:------|
| 16 | COSMIC-CENSORSHIP-49 | Does ballistic transit overshoot to tau>0.537? 4D T_mu_nu from negative curvature. | SP | s40_collective_inertia, s48_curv_extend |
| 17 | CMPP-TRANSITION-49 | Higher-D Petrov classification at tau=0.537. | SP | s48_curv_extend |
| 18 | NON-LI-TT-49 | Non-left-invariant TT modes. First negative eigenvalue at what tau? | Spectral Geometer | s48_tt_lichnerowicz |
| 19 | DIPOLAR-CATALOG-49 | Catalog all interactions external to BCS Hamiltonian on SU(3). Which ones break U(1)_7? Gravity? Torsion? WZW? | Volovik | researchers/Volovik/ |
| 20 | LEGGETT-GGE-49 | Does Leggett relative phase survive as conserved quantity in the P_exc=1 GGE? Nuclear pair fluctuations above T_c analog. | Nazarewicz | s38 quench data, s48_leggett_mode |

---

## Key Tensions to Resolve

| Tension | Current Status | What Resolves It |
|:--------|:--------------|:----------------|
| m_G requires 10^{-56} M_KK, no microscopic source produces it | OPEN | FRIEDMANN-GOLDSTONE-49 or GEOMETRIC-BREAKING-49 |
| O-Z needs m* = 11.87 M_KK, but physical m ~ H_0 ~ 10^{-58} M_KK | 84-order gap (Volovik) | Scale mapping from tessellation to CMB (BRAGG-GOLDSTONE-49) |
| alpha_s = -0.038 is 4.9 sigma from Planck | Testable by CMB-S4 | ALPHA-S-BAYES-49 may soften with J uncertainties |
| w_0 in [-0.47, -0.59] is 2.8 sigma from DESI DR2 | Structural (Z-K definitional) | MULTI-T-FRIEDMANN-49 or DESI-DR3-PREP-49 |
| N=1 singlet closes CC crossing | CLOSED at singlet | FABRIC-NPAIR-49 (32 cells) |
| Zak phase retracted, Jensen topologically trivial | CLOSED on-Jensen | Off-Jensen P-30w (future) |

---

## Structural Results to Carry Forward

These S48 results constrain all future computations:

1. **Spectral action trace theorem**: S[UDU^dag] = S[D]. Permanent wall. No trace functional generates Goldstone mass.
2. **Self-tuning has no finite fixed point**: Runaway is structural (lattice sum monotonicity). Applies at any cell count.
3. **N=1 exact in singlet**: 8 modes IS complete. CC crossing requires fabric level.
4. **Leggett mode**: omega_L = {0.070, 0.107} M_KK, sharp. Lowest energy scale in BCS sector.
5. **HFB converges**: Multi-gap BCS self-consistent. BCS is 5% perturbation on geometry.
6. **KZ-aniso matches S38 to 6.5%**: Curvature geometry predicts quench dynamics.
7. **Geometric phase transition at tau=0.537**: Negative curvature onset. [0.537, 0.78] is mixed-curvature window.
8. **Analog horizons**: Mach 54 on T^2. 1D sonic surfaces confining quasiparticles.
9. **Swampland PASS**: c=52.8. Permanent. Jensen path in landscape.
10. **B2 eigenvector weights = {3/8, 1/8, 4/8}**: Exact dimension ratios. Flat-band protection is energetic.
11. **n3 = dim(3,0) = T_4 = 10**: Sole surviving Paasch-NCG bridge. Alpha to 0.9 ppm.
12. **Z-K discrepancy = 39.4%**: Structural and definitional. Two legitimate decompositions of the same non-equilibrium state.
