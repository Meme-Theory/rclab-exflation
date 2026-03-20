# Session 46 — Wave 4: Remaining Items (21 tasks, shorter prompts)

**Date**: 2026-03-15
**Source**: `sessions/session-plan/session-46-plan.md`, `sessions/session-plan/s46-rollup-from-s45.md`
**Prerequisite**: Waves 1-3 complete. Results feed into W5 reconciliation.

**Global rules for all W4 tasks**:
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- Working dir: `C:\sandbox\Ainulindale Exflation` (quote all paths with spaces)
- Import constants from `tier0-computation/canonical_constants.py`
- Script prefix: `s46_`
- Output to `tier0-computation/`
- Formula audit: every computation must include (a) formula with units, (b) dimensional check, (c) limiting case, (d) citation

---

## n_s Remaining (6 tasks)

### W4-1: Landau-Zener k-Dependent Adiabaticity (LANDAU-ZENER-NS-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #19

Compute the Landau-Zener adiabaticity parameter Q_k = delta_k^2 / (hbar * v_k) as a function of Casimir wavenumber k for all 992 modes at the fold. The transit is sudden on average (Q_median = 19.5 from S45), but Q_k varies with k through the band structure. If Q_k ~ k (linear), the transition between adiabatic and diabatic regimes provides an effective hose-count alpha ~ 1. The pair creation probability per mode is P_k = 1 - exp(-2 pi Q_k). Compute n_s from P(k) * (Weyl degeneracy at k) and compare to the W1-2 BdG pair-mode result.

**Input**: `tier0-computation/s45_kz_ns.npz`, `tier0-computation/s44_dos_tau.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_landau_zener_ns.py`, `.npz`, `.png`
**Gate**: Part of HOSE-COUNT-46 (same alpha target [0.8, 1.2]).
**Formula audit**: Q_k = Delta_k^2 / (v_k * |d(gap)/d(tau)|). [Q] dimensionless. Limiting case: Q >> 1 (adiabatic, P -> 0); Q << 1 (diabatic, P -> 1).

---

### W4-2: Band Inversion Berry Phase (BAND-INVERSION-BERRY-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #21

Compute the Berry phase along a path in (p,q) representation space that encircles the band-inversion point at tau = 0. At tau = 0 (round SU(3)), eigenvalues are degenerate. As tau increases, bands invert (levels cross). If the Berry phase accumulated along a closed loop in (p,q) space equals pi, pair creation at that point is topologically protected, producing exactly one pair per Chern sector per transit -- giving alpha = 1 from topology, not BCS.

Construct the Berry connection A_pq = i <u_k(tau)| d/d(tau) |u_k(tau)> from the eigenstates in s44_dos_tau.npz. Integrate around closed loops in (p,q,tau) space. Report Berry phases for the 10 largest sectors.

**Input**: `tier0-computation/s44_dos_tau.npz`, `tier0-computation/s45_acoustic_ns.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_berry_phase.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report Berry phase per sector and whether any equals pi.

---

### W4-3: Anomalous Dispersion of RPA Collective Mode (ANOMALOUS-DISPERSION-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #22

Recompute the RPA collective mode dispersion with full k-dependent V_{kl}(tau) from the Dirac eigenvalue structure (not constant-V). S45 COLLECTIVE-NS-RPA used a constant pairing interaction; the actual V_{kl} inherits anomalous dispersion from the parent band (band inversion, negative group velocity v_g = -0.197 at the fold). If d(omega_coll)/dk becomes positive and k-linear for some k range, the collective mode acquires a tilt contribution to alpha.

**Input**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s45_collective_ns_rpa.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_anomalous_dispersion.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report d(omega)/dk sign and magnitude.

---

### W4-4: Forward/Backward Pair Creation Full Computation (FWD-BWD-NS-46)

**Agent**: `volovik-superfluid-universe-theorist` | **Model**: opus | **Rollup item**: #20

Complete the forward/backward pair creation computation. S45 sanity check PASSED (red tilt confirmed, ratio decreases with k from 755,000x to 865x). The d_eff converges to 3 at tau_back = 0.50. Now: compute n_s at intermediate tau_back values where d_eff crosses the sweet spot for Planck. If d_eff(tau_back) passes through d_eff = 1.02 (giving n_s = 0.965) at some tau_back, identify the physical mechanism that selects that tau_back.

**Input**: `tier0-computation/s45_fwd_bwd_ns.npz`, `tier0-computation/s45_kz_ns.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_fwd_bwd_ns.py`, `.npz`, `.png`
**Gate**: FWD-BWD-NS-46. PASS: n_s in [0.955, 0.975]. FAIL: n_s outside [0.80, 1.10].

---

### W4-5: Non-Singlet Mode Dissipation (NONSINGLET-DISSIPATION-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #18

Estimate one-body dissipation from the 101,968 non-singlet modes (d > 1 sectors). The S45 WKB assessment (Q_median = 19.5) was computed for BCS-active modes only. Non-singlet modes have different adiabaticity parameters because they respond diabatically at different rates. Compute the effective viscosity from the non-singlet bath and report whether 101,968 modes provide sufficient friction for the 829x velocity reduction needed for n_s = 0.965.

**Input**: `tier0-computation/s44_dos_tau.npz`, `tier0-computation/s45_kz_ns.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_nonsinglet_dissipation.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report gamma_nonsinglet / gamma_Hubble.

---

### W4-6: Fabric Tessellation Modulation of Pair Creation (FABRIC-TESSELLATION-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #24

The 32-cell Voronoi tessellation (KZ domain structure, S42) imposes a geometric filter on the pair creation spectrum. The number of domain walls intercepted by a mode of wavenumber k grows as ~k in the transit direction (1D). This provides a geometric alpha = 1 that is independent of the BCS pair counting. Compute the domain-wall modulation function M(k) = (number of wall crossings at wavenumber k) / k_max, and extract alpha_tess from M(k) ~ k^{alpha_tess}.

**Input**: `tier0-computation/s44_voronoi_fnl.npz`, `tier0-computation/s44_coherent_wall.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_fabric_tessellation.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report alpha_tess.

---

## CC / Tau-Stabilization Remaining (4 tasks)

### W4-7: Bayesian GP Emulator for tau* Posterior (BAYESIAN-GP-46)

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus | **Rollup item**: #6

Construct a Gaussian process emulator for tau*(Delta_B2, Delta_B1, Delta_B3) using the S45 60-point scan from Q-THEORY-BCS-45. Compute the posterior tau* = 0.209 +/- sigma_tau. This gives the first ERROR BAR on tau*. Nuclear DFT always provides error bars; the framework should too.

**Input**: `tier0-computation/s45_qtheory_bcs.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_bayesian_gp.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report sigma_tau. Nazarewicz prediction: sigma_tau ~ 0.03-0.05, 68% CI includes fold.

---

### W4-8: Multi-T Jacobson Sector-by-Sector (MULTI-JACOBSON-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #5

Compute the 8 sector-by-sector Gibbs-Duhem conditions at tau* = 0.209 (or updated W1-1 value). Each GGE sector contributes independently to the gravitating stress-energy via the multi-temperature Jacobson identity. The Gibbs-Duhem cancellation rho_k(tau*) = 0 must hold sector-by-sector for consistency.

**Input**: `tier0-computation/s44_multi_t_jacobson.npz`, `tier0-computation/s45_qtheory_bcs.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_multi_jacobson.py`, `.npz`, `.png`
**Gate**: MULTI-JACOBSON-QTHEORY-46. PASS: all 8 sectors |rho_k(tau*)| < 0.1 M_KK^4. FAIL: any |rho_k| > 1.0.

---

### W4-9: GCM Zero-Point Correction for Tau Stabilization (GCM-ZERO-POINT-46)

**Agent**: `nazarewicz-nuclear-structure-theorist` | **Model**: opus | **Rollup item**: #4

Compute Generator Coordinate Method (GCM) norm overlaps G(tau, tau') for 5 tau values in [0.10, 0.25] using BCS Pfaffian overlap. Diagonalize the 5x5 GCM equation. The zero-point correction is the difference between the lowest GCM eigenvalue and V(tau) minimum. Nuclear analog: 0.5-1 MeV lowering. This correction could provide the final 0.019 shift to bring tau* from 0.209 to 0.190.

**Input**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s44_dos_tau.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_gcm_zero_point.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report zero-point correction in units of tau and whether it shifts tau* toward tau_fold.

---

### W4-10: Three-Frequency Universe Cavity Radiation (THREE-FREQ-UNIVERSE-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #48

The 3 GGE beat frequencies (B2-B1 = 0.052, B2-B3 = 0.266, B1-B3 = 0.318 M_KK) form a cavity radiation pattern. Compute the radiation spectrum from a cavity with these 3 resonant frequencies during the transit phase. The cavity Q-factors are determined by the GGE lifetime (infinite, by integrability). The radiation pattern imprints on the 4D power spectrum through the Friedmann transfer function (complements W3-4).

**Input**: `tier0-computation/s45_gge_beating.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_three_freq_universe.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report the cavity radiation spectrum and k-space positions of beat peaks.

---

## DM/DE (1 task)

### W4-11: Dissolution Singlet-Only Partition (DISSOLUTION-SINGLET-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #29

Compute S(eps_c) restricted to singlet-singlet partition only (16 modes, A = 8, B = 8). The S45 dissolution entropy computation exists but was NOT STARTED in the working paper. If S_singlet/S_page_singlet > 0.95, suppression is purely from block-diagonality (geometric). If ~ 0.47 (matching the full spectrum), the suppression is intrinsic to BCS structure (dynamical). This distinguishes geometric from dynamical information suppression.

**Input**: `tier0-computation/s45_dissolution_entropy.npz` (script exists), `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_dissolution_singlet.py`, `.npz`, `.png`
**Gate**: DISSOLUTION-STRUCTURE-46. PASS: S_singlet/S_page > 0.95. INFO: ~ 0.47.

---

## Structural / NCG (7 tasks)

### W4-12: Peter-Weyl Censorship Retry (PETER-WEYL-CENSORSHIP-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #36

Complete the Peter-Weyl censorship computation killed in S45 (agent stuck in loop). Determine whether the Peter-Weyl decomposition of the spectral action censors information about the BCS state: does the singlet projection erase all non-singlet correlations, or do they survive in the off-diagonal heat kernel coefficients?

**Input**: `tier0-computation/s44_eih_grav.npz`, `tier0-computation/s44_dissolution_scaling.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_peter_weyl_censorship.py`, `.npz`, `.png`
**Gate**: Original S45 gate (from s45_peter_weyl_censorship.py).

---

### W4-13: Spectral Form Factor (SPECTRAL-FORM-FACTOR-46)

**Agent**: `spectral-geometer` | **Model**: opus | **Rollup item**: #35

Compute K(t) = |sum_k d_k e^{i lambda_k t}|^2 / (sum d_k)^2 for the truncated D_K spectrum at the fold. Identify the Heisenberg time t_H (onset of plateau), the ramp-plateau structure (GUE vs GOE vs Poisson), and tau dependence. K(t) is a Tier 1 quantity probing two-point eigenvalue correlations. The SFF diagnostic determines whether the spectrum has random-matrix-like correlations or is integrable.

**Input**: `tier0-computation/s44_dos_tau.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_spectral_form_factor.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report t_H and universality class (GUE/GOE/Poisson).

---

### W4-14: Spectral Zeta at Non-Integer s (SPECTRAL-ZETA-NONINT-46)

**Agent**: `spectral-geometer` | **Model**: opus | **Rollup item**: #37

Compute zeta_D(s) = sum_k d_k |lambda_k|^{-2s} for non-integer s = 1/2, 3/2, 5/2, 7/2. The spectral zeta at integer s gives the Seeley-DeWitt coefficients. At non-integer s, the zeta interpolates between UV-sensitive (small s) and IR-sensitive (large s) regimes. Report how the q-theory crossing tau* depends on s (does it vary smoothly or have a discontinuity at integer s?).

**Input**: `tier0-computation/s44_dos_tau.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_spectral_zeta_nonint.py`, `.npz`, `.png`
**Gate**: Diagnostic.

---

### W4-15: Spectral Action on Combined (tau) x (Omega^1_D) Space (SA-ON-OMEGA-TAU-46)

**Agent**: `connes-ncg-theorist` | **Model**: opus | **Rollup item**: #38

If W2-4 (OMEGA-CLASSIFY) finds any tachyonic direction, compute the spectral action landscape on the combined 343-dimensional (tau) x (Omega^1_D) moduli space. The S40 Hessian was 1D (tau only). This extends to the full 343D space. If the combined landscape has a saddle point at the fold, this is a NEW stabilization mechanism.

**Dependency**: Requires W2-4 results. If W2-4 finds all directions massive, this computation is moot -- report "no tachyonic direction found, SA-ON-OMEGA-TAU not computed."

**Input**: W2-4 output (`s46_omega_classify.npz`), `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_sa_omega_tau.py`, `.npz`, `.png`
**Gate**: Part of OMEGA-CLASSIFY-46.

---

### W4-16: Pseudo-Riemannian Spectral Triple on SU(2,1) (PSEUDO-RIEMANNIAN-46)

**Agent**: `connes-ncg-theorist` | **Model**: opus | **Rollup item**: #39

Replace SU(3) with the non-compact real form SU(2,1). Compute D_K on SU(2,1) with the Killing metric (indefinite signature (5,3)). Verify which spectral triple axioms survive. Paper 36 (de Groot 2026) provides the mathematical framework. If the transit corresponds to SU(3) -> SU(2,1) deformation, the pseudo-Riemannian triple is the correct framework. Speculative but structurally motivated.

**Input**: `researchers/Connes/36_2026_de_Groot_Pseudo_Riemannian_Spectral_Triples_SU11.md`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_pseudo_riemannian.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report which axioms hold.

---

## Specialist Tasks (7 tasks)

### W4-17: Phonon Magnetic Moment from Hall Conductivity (PHONON-MAGNETIC-MOMENT-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #49

Compute the Hall conductivity sigma_xy of the BCS state on SU(3) at the fold. The phonon magnetic moment mu_phonon = sigma_xy / n (where n is the phonon number density) provides a dimensionless coupling to external magnetic fields. If mu_phonon is nonzero, phononic excitations carry an effective magnetic moment despite being charge-neutral -- a distinctive signature.

**Input**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_phonon_magnetic_moment.py`, `.npz`, `.png`
**Gate**: Diagnostic.

---

### W4-18: Kapitza Parametric Resonance from GGE Beats (KAPITZA-PARAMETRIC-46)

**Agent**: `tesla-resonance` | **Model**: opus | **Rollup item**: #50

The 3 GGE beat frequencies modulate the effective potential for the tau modulus. If any beat frequency is near 2*omega_tau (where omega_tau = 8.27 M_KK is the modulus oscillation frequency), parametric resonance amplifies modulus oscillations (Kapitza pendulum). Compute the Mathieu stability diagram for the modulated potential and identify resonance zones. Kapitza ratio = 0.030 (S38, corrected) may place the system near a resonance tongue.

**Input**: `tier0-computation/s45_gge_beating.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_kapitza_parametric.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report whether any beat is within 10% of 2*omega_tau.

---

### W4-19: Bekenstein Bound on Singlet Torsion (BEKENSTEIN-TORSION-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #54

Compute the Bekenstein entropy bound S_Bek = 2*pi*E*R for the singlet sector. S45 Hawking review (Section I.2) showed S_torsion/S_Bek ~ 10^{-30} (vast undersaturation, confirming no horizon). Extend to the BCS state: does the BCS condensation energy change the bound? Is there a tau value where the Bekenstein bound is approached?

**Input**: `tier0-computation/s45_truncated_torsion.npz` (if exists), `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_bekenstein_torsion.py`, `.npz`, `.png`
**Gate**: Diagnostic.

---

### W4-20: GSL Consistency at q-Theory Crossing (GSL-QTHEORY-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #55

Verify the Generalized Second Law (GSL) at the q-theory crossing tau* = 0.209. The GSL requires S_gen = S_matter + A/(4 G_N) to be non-decreasing. At the crossing, the vacuum energy vanishes by construction. Does the total entropy (matter + gravitational) increase through the crossing? This is a consistency check on the thermodynamic interpretation.

**Input**: `tier0-computation/s45_qtheory_bcs.npz`, `tier0-computation/s42_gge_energy.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_gsl_qtheory.py`, `.npz`, `.png`
**Gate**: Diagnostic. PASS if dS_gen/dtau > 0 at tau*. FAIL if dS_gen/dtau < 0.

---

### W4-21: WCH Consistency at tau* (WCH-QTHEORY-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #56

Verify the Weak Cosmic Censorship Hypothesis at the q-theory crossing. In the modulus space picture, tau* = 0.209 is an equilibrium point. The WCH requires that no naked singularity forms during the transit through this point. Compute the Kretschmer scalar K = R_{abcd} R^{abcd} at tau* and verify it is finite and bounded.

**Input**: `tier0-computation/s45_kretschner.npz` (if exists), `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_wch_qtheory.py`, `.npz`, `.png`
**Gate**: Diagnostic.

---

### W4-22: Spectral Action as von Neumann Entropy (SA-ENTROPY-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #57

Test the identity S_spectral = S_vN proposed by the entropy-spectral action correspondence (Paper 20, CCS 2019). The spectral action Tr f(D^2/Lambda^2) at specific f may equal the von Neumann entropy of the density matrix rho = D^2 / Tr(D^2). Compute both sides at the fold and report whether any cutoff function f establishes the identity.

**Input**: `tier0-computation/s42_hauser_feshbach.npz`, `tier0-computation/s42_gge_energy.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_sa_entropy.py`, `.npz`, `.png`
**Gate**: Diagnostic.

---

### W4-23: Trans-Planckian Universality (TRANSPLANCKIAN-46)

**Agent**: `hawking-theorist` | **Model**: opus | **Rollup item**: #58

Test whether the n_s prediction is robust against trans-Planckian modifications. The framework has a natural UV cutoff at M_KK (not M_Pl). Modes with k > M_KK experience modified dispersion. Implement the Brandenberger-Martin trans-Planckian modifications (omega^2 = k^2 + beta_n k^{2n} / M_KK^{2n-2}) and compute the resulting correction to n_s for n = 2, 3. Report whether the correction is < 0.001 (robust) or > 0.01 (UV-sensitive).

**Input**: `tier0-computation/s45_kz_ns.npz`, `tier0-computation/canonical_constants.py`
**Output**: `tier0-computation/s46_transplanckian.py`, `.npz`, `.png`
**Gate**: Diagnostic. Report delta(n_s) from trans-Planckian corrections.
