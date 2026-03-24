# Session 49 Way Forward

**Source**: 6 collaborative reviews (Tesla, Volovik, SP, QA, Cosmic-Web, Landau)
**Date**: 2026-03-17

---

## Reviewer Convergence

All 6 converge on one point: **the alpha_s = n_s² - 1 identity is the sharpest constraint**. At 6σ from Planck (and Cosmic-Web notes it would shift σ_8 by 21%, already excluded by lensing), the O-Z functional form P(K) = T/(JK² + m²) is under severe observational pressure. The escape — identified independently by Landau and Tesla — is that the Leggett propagator has **3 poles, not 1**. The single-pole O-Z is an approximation; the true propagator from the 3-band Josephson system modifies both n_s and alpha_s. Computing this is the unanimous S50 priority.

Secondary convergence: the Leggett dipolar identification (mass within 18%) is the session's strongest positive, but Volovik identifies a paradox (mass exists only pre-transit, n_s must survive post-transit) and proposes Bogoliubov coefficients as the resolution.

---

## Unique Contributions

### Tesla
- **Two-functional architecture**: Spectral action for geometry, Josephson for mass. These are structurally different functionals and should not be mixed.
- Three alternative propagators: Leggett spectral function with GGE occupations, pair-transfer response, KZ quench spectrum.
- Frequency hierarchy analysis: 3 natural bands (Josephson 0.07-0.11, Gap 0.17-1.46, Breathing 1.43-8.27 M_KK).

### Volovik
- **Hierarchy mismatch**: omega_L/Delta = 0.095 in framework vs 10^{-3} in 3He (95x compression). Marginal pair-breaking separation → Beliaev damping significant.
- **Pre-transit/post-transit paradox**: Leggett mass exists only with condensate. Post-transit P_exc=1. Resolution: Bogoliubov coefficients carry frozen imprint (Paper 27).
- Proposes LEGGETT-DAMPING-50: Im[Sigma_L] from pair-breaking continuum.

### Schwarzschild-Penrose
- Triple censorship is sound but **conditional** on initial conditions (not unconditional Penrose-type). Layer 1 (energy budget, 65x) independently sufficient.
- Riemannian CMPP locking is signature artifact. **Lorentzian 12D CMPP is the real test** (highest priority from SP).
- Weyl zero-crossing at 0.895: potential GW polarization transition in bulk.

### Quantum Acoustics
- **Eikonal breakdown opacity**: 78% of T² where WKB fails could act as physical damping modifying the propagator.
- Modified dispersion from sub-gap proximity (omega_L/2Delta_B3 = 0.41 → anomalous group velocity near band edge).
- First-sound BAO imprint with directional anisotropy as leading acoustic discriminant.
- Bragg mechanism fully dead (Z_3 quantization, no escape routes viable).

### Cosmic-Web
- alpha_s = -0.069 → σ_8 shift 21% → **already excluded by lensing** if O-Z is the full story.
- w_0-w_a BAO joint constraint is most discriminating LSS observable.
- Framework in no-man's-land: between DESI and LCDM in w_0, identical to LCDM in w_a.
- DESI DR3 (sigma ~ 0.035) is the decisive external test.

### Landau
- **The alpha_s identity is a single-pole artifact.** The Leggett 3-band Josephson propagator has 3 poles. Multi-pole propagator modifies the running formula — alpha_s is NOT rigid if O-Z is wrong.
- GL free energy with Josephson phase terms → 96-mode fabric diagonalization.
- Fabric order parameter space M_fabric with Z_3 quotient structure.
- Running mass from anomalous dimension.

---

## S50 Computations (Priority-Ordered)

### Tier 1 — Central (the propagator question)

| # | Computation | What | Agent |
|:--|:-----------|:-----|:------|
| 1 | LEGGETT-PROPAGATOR-50 | 3-pole Leggett propagator on the 32-cell fabric. Compute P(K) with 3-band Josephson structure (not O-Z). Extract n_s and alpha_s. Does multi-pole structure resolve the 6σ alpha_s tension? | Landau |
| 2 | BOGOLIUBOV-IMPRINT-50 | Bogoliubov coefficients during transit with Leggett mass. Do they carry a frozen imprint of the pre-transit Leggett gap into the post-transit power spectrum? (Volovik Paper 27 resolution) | Volovik |
| 3 | LEGGETT-DAMPING-50 | Im[Sigma_L] from pair-breaking continuum. Is the Leggett mode broadened by Beliaev damping (omega_L/2Delta = 0.41, marginal)? | Volovik |
| 4 | J-PAIR-CALIBRATE-50 | Independent J_pair from explicit pair-transfer matrix element (not J_C2 * E_cond). FABRIC-NPAIR conditional PASS requires J_pair > 0.096. | Nazarewicz |

### Tier 2 — Observational predictions

| # | Computation | What | Agent |
|:--|:-----------|:-----|:------|
| 5 | SIGMA8-PREDICT-50 | Compute σ_8 from the 3-pole propagator P(K). Compare to Planck (0.811) and lensing (0.766). Does the multi-pole form resolve the σ_8 tension? | Cosmic-Web |
| 6 | DESI-DR3-JOINT-50 | w_0-w_a joint BAO constraint from the multi-T Friedmann. Forecast DR3 discrimination power. | Cosmic-Web |
| 7 | LEGGETT-PHI-CONFIRM-50 | Direct omega_L computation at tau=0.21 to confirm/deny the phi_paasch crossing at 0.2117. | Tesla |
| 8 | RUNNING-MASS-50 | Running mass m(K) from anomalous dimension and lattice RG. Need gamma > 1.7 for 2σ Planck compatibility. | Landau |

### Tier 3 — Geometric characterization

| # | Computation | What | Agent |
|:--|:-----------|:-----|:------|
| 9 | LORENTZIAN-CMPP-50 | 12D Lorentzian CMPP classification of M^4 × SU(3). | SP |
| 10 | WEYL-ZERO-50 | Physical interpretation of Weyl eigenvalue zero-crossing at tau=0.895. GW polarization transition? | SP |
| 11 | EIKONAL-DAMPING-50 | Does eikonal breakdown (78% of T²) produce physical damping in the fabric propagator? | QA |
| 12 | GL-JOSEPHSON-50 | GL free energy with Josephson phases. 96-mode fabric diagonalization. Fabric order parameter space. | Landau |

### Tier 4 — Remaining

| # | Computation | What | Agent |
|:--|:-----------|:-----|:------|
| 13 | FIRST-SOUND-BAO-50 | First-sound imprint with directional anisotropy. Leading acoustic discriminant vs LCDM. | QA |
| 14 | W_A-SOURCE-50 | What breaks w_a = 0? Fabric coupling? Transit dynamics? (DESI sees -0.73) | Einstein |
| 15 | NON-LI-TT-ADJOINT-50 | Extend non-LI TT to (1,1) adjoint representation. | Spectral Geom |
| 16 | STIFF-EPOCH-50 | Stiff-matter (w=1) epoch duration from transit. BBN constraints? | SP |
| 17 | INNER-FLUCT-GOLDSTONE-50 | Goldstone mass from inner fluctuations (epsilon=0.052, non-trace functional). | Gen |

---

## Key Tensions

| Tension | Status | What Resolves It |
|:--------|:-------|:----------------|
| alpha_s = -0.069, 6σ from Planck | Rigid if O-Z | LEGGETT-PROPAGATOR-50 (3-pole may break identity) |
| σ_8 shift 21% from alpha_s | Excluded if O-Z | Same — multi-pole P(K) changes σ_8 |
| w_a = 0, DESI sees -0.73 | Structural (GGE integrability) | W_A-SOURCE-50 |
| Leggett mass pre-transit only | Paradox | BOGOLIUBOV-IMPRINT-50 |
| FABRIC-NPAIR conditional on J_pair | J_pair > 0.096 needed | J-PAIR-CALIBRATE-50 |
| B=0.073 in 2D (w_0, w_a) | w_a drives disfavor | DESI-DR3-JOINT-50 |

---

## Structural Results to Carry Forward

All S49 permanent results from the synthesis, plus:
- The Leggett propagator question (3-pole vs 1-pole) is now the central theoretical question
- The "two-functional architecture" (Tesla): SA for geometry, Josephson for mass
- The pre-transit/post-transit paradox (Volovik): mass mechanism lives in a phase the universe has left
- The σ_8 exclusion (Cosmic-Web): if O-Z is literal, the framework is already falsified by lensing data
- The eikonal opacity (QA): WKB breakdown as physical damping, not just a diagnostic
