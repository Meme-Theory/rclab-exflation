---
name: S50 Deep-Dive on O-Z and W1 FAILs
description: Validation of 4 FAIL verdicts, sub-quadratic dispersion discovery, Schur Lemma Trap, nuclear precedent analysis
type: project
---

## S50 Deep-Dive: O-Z and Wave 1 FAILs

### FAIL Validations (all rigorous)
- W1-A (3-pole): 10/10. Equal-stiffness theorem structural. Multi-pole effect 5.8e-9. Identity survives at 4000x Josephson.
- W1-C (Bogoliubov): 9/10. B2 modulation 1.1e-6 bulletproof. B3 4.2% but only 5% of pairs. Minor gap: ground-state symmetry argument has <cos(phi_0)> = 0.83, not 0, but doesn't change verdict.
- W1-F (running mass): 10/10. Algebraic bound gamma < 1-n_s = 0.035. Physical gamma = -6.76e-4 (wrong sign). Structural.
- W1-H (eikonal): 10/10. KK zero-mode exactly decoupled from internal texture. <V>=0 by construction.

### Key Discovery: Sub-Quadratic Dispersion
For P(K) = T/(J K^alpha + m^2):
- alpha_s = -(1-n_s)(alpha - 1 + n_s) [EXACT]
- alpha=2: alpha_s = -0.0688 (8.4 sigma, FAIL)
- alpha=0.5: alpha_s = -0.016 (1.8 sigma, Planck-compatible)
- Need alpha < 0.55 for 2-sigma Planck

### Schur Lemma Trap
V(B2,B2) = 0.1557 is Casimir (k-independent by Schur). All modes see identical interaction. Nuclear analog has k-dependent V(k,k') from finite NN range. Framework has k-independent V from representation theory. This kills running at mean-field level.

### Nuclear Precedents
- Shell model gives right levels, wrong transition rates (factor 2-5). Fix: effective charges from core polarization.
- Nuclear pairing Delta(k) varies 3x across window (finite-range force). Framework Delta is constant (Schur).
- Nuclear gamma_nuclear ~ 2 from k-dependent gap. Framework gamma ~ 0 from Schur trap.
- Proton-neutron coupling (analog of Josephson) gives splitting delta_omega/omega ~ 0.01-0.1 in nuclei. Framework: 5.1e-4.

### Root Cause of All 4 FAILs
Mass hierarchy: m_star^2 = 140.5 >> J_max = 0.072 M_KK^2. The n_s = 0.965 constraint forces enormous mass. Leggett mass provides m_L^2 = 0.0048 (0.003% of needed). The MASS PROBLEM is unsolved.

### O-Z Status
- O-Z FORM: alive (K^{-2} Goldstone, massive propagator, phi_paasch crossing)
- O-Z identity (alpha_s = n_s^2 - 1): structural within K^2 dispersion
- O-Z MASS: wrong by factor 170

### Recommended S51 Gates
1. ANOMALOUS-DISPERSION-51: Phonon G(K) on actual Voronoi lattice with Z_3 disorder. PASS if alpha_eff < 0.55.
2. FABRIC-RPA-51: RPA-screened phonon propagator on 32-cell fabric. PASS if alpha_s in [-0.04, 0].
3. KZ-SPATIAL-51: Cell-dependent quench rates from Voronoi geometry. PASS if n_s in [0.95, 0.98].
4. DISPERSION-SURVEY-51: Map alpha vs alpha_s (INFO, parametric survey).
