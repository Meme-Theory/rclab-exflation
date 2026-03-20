# Session 52 Plan: The 12D Reduction

**Date**: TBD
**Author**: Team-lead (synthesized from 23 atlas collaborative reviews)
**Format**: Parallel single-agent computations across 3 waves
**Source**: 23 atlas collaborative reviews (`summary/atlas-*-collab.md`)
**Motivation**: Universal convergence -- 23/23 reviewers identify EFOLD-MAPPING-52 as the single decisive computation. 18/23 identify the 12D submersion decomposition as the missing calculation. SP proves Type D simplifies this to a separable scalar problem. Quantum-Foam + Hawking prove the no-boundary condition selects tau_i = 0, potentially converting the razor-thin e-fold margin to a structural result.
**Results file**: `sessions/session-52/session-52-results-workingpaper.md`

---

## I. Session Objective

Derive the modulus equation of motion from the 12D Einstein equations on M^4 x SU(3), determine M_KK from gauge coupling calibration, compute the e-fold mapping, and resolve whether K_pivot < K* = 0.087 M_KK. Secondary: execute all queued low-cost computations from the 23 reviews that inform or depend on the reduction.

---

## II. Wave Structure

### Wave 1: Foundation and Quick Wins (parallel, no dependencies)

All Wave 1 computations run simultaneously. Each is self-contained and LOW or MEDIUM cost. They feed into the Wave 2 decisive computation or close carry-forward items.

---

#### W1-A: WDW-INITIAL-52 -- Wheeler-DeWitt initial condition
- **Recommended by**: Quantum-Foam, Hawking, Einstein, String, Tesla, Volovik (6 reviewers)
- **Agent**: Hawking-Theorist or Quantum-Foam-Theorist (Opus)
- **Cost**: LOW (2D minisuperspace ODE, ~50 lines Python)
- **Script**: `s52_wdw_initial.py`
- **Input**: G_mod = 5.0 (S40), V_SA(tau) from spectral action data (`s44_dos_tau.npz`), Hartle-Hawking boundary condition
- **Computation**: Solve Hat{H} Psi[tau, a] = 0 on the minisuperspace (tau, a) with no-boundary (Euclidean regularity) boundary condition. Extract |Psi(tau)|^2 and determine peak location.
- **Gate**: WDW-INITIAL-52
  - **PASS**: |Psi|^2 peaks at tau < 10^{-5}. Initial condition is derived, not assumed. Converts EFOLD margin from 0.2 to >> 1.
  - **FAIL**: |Psi|^2 peaks at tau > 0.01. Initial condition requires fine-tuning at 10^{-4} level.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_wdw_initial.py`

---

#### W1-B: DDG-MKK-52 -- Power-law gauge coupling running for M_KK
- **Recommended by**: KK, Baptista, SP, Einstein, String (5 reviewers)
- **Agent**: KK-Theorist or Einstein-Theorist (Opus)
- **Cost**: LOW (standard 1-loop running with 992-mode tower)
- **Script**: `s52_ddg_mkk.py`
- **Input**: 992-mode Dirac spectrum (`s44_dos_tau.npz`), measured gauge couplings alpha_1(M_Z), alpha_2(M_Z), alpha_3(M_Z) from PDG 2024
- **Computation**: Run DDG (Dienes-Dudas-Gherghetta) power-law KK threshold corrections above M_KK. Match to measured couplings at M_Z = 91.2 GeV. Extract M_KK.
- **Gate**: DDG-MKK-52
  - **PASS**: M_KK determined within 1 OOM from gauge coupling matching. Value consistent with Sakharov ratio (S44: 0.36 OOM).
  - **FAIL**: No consistent M_KK from all three couplings (spread > 3 OOM). KK tower structure insufficient for unification.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_ddg_mkk.py`

---

#### W1-C: CASIMIR-JOSEPHSON-52 -- J_12/J_23 from Casimir algebra
- **Recommended by**: Paasch, Landau, Tesla, Berry (4 reviewers)
- **Agent**: Paasch-Analyst or Landau-Theorist (Opus)
- **Cost**: LOW (algebraic computation from known V matrix)
- **Script**: `s52_casimir_josephson.py`
- **Input**: Kosmann pairing V_nm (S34), Casimir eigenvalues C_2(p,q)
- **Computation**: Express J_12/J_23 = 19.52 as a function of Casimir operators of B1, B2, B3. Test whether the phi crossing condition reduces to an algebraic equation in Casimir eigenvalues.
- **Gate**: CASIMIR-JOSEPHSON-52
  - **PASS**: J_12/J_23 derivable algebraically from C_2 values. Phi crossing explained by representation theory.
  - **INFO**: Ratio involves non-Casimir matrix elements. Structural but not purely algebraic.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_casimir_josephson.py`

---

#### W1-D: ETA-B-52 -- Baryogenesis CP-odd phase and eta_B estimate
- **Recommended by**: Dirac, Hawking, Volovik, Feynman, Connes (5 reviewers)
- **Agent**: Dirac-Antimatter-Theorist (Opus)
- **Cost**: LOW-MEDIUM (BdG diagonalization at fold, extract Bogoliubov U matrix, compute CP phase)
- **Script**: `s52_eta_b.py`
- **Input**: BdG Hamiltonian at tau = 0.19, K_7 charge assignments, selection rules (E15)
- **Computation**: (a) Diagonalize BdG at fold, extract Bogoliubov transformation U. (b) Compute relative phase between particle and antiparticle components of Cooper pair wavefunction. (c) If CP-odd phase != 0, estimate eta_B from pair number (59.8), CP phase, and selection rules.
- **Gate**: ETA-B-52
  - **PASS**: CP-odd phase nonzero. eta_B within 3 OOM of 6e-10. Baryogenesis mechanism identified.
  - **INFO**: CP-odd phase nonzero but eta_B wrong by > 3 OOM (like electroweak baryogenesis).
  - **FAIL**: CP-odd phase exactly zero (CP preserved). No intrinsic baryogenesis.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_eta_b.py`

---

#### W1-E: TORSION-52 -- Analytic torsion on Jensen SU(3)
- **Recommended by**: Spectral-Geom, Connes, Berry, Hawking, KK (5 reviewers)
- **Agent**: Spectral-Geometer (Opus)
- **Cost**: MEDIUM (requires spectral zeta function evaluation at multiple tau)
- **Script**: `s52_analytic_torsion.py`
- **Input**: Full D_K eigenvalue data at 5+ tau values
- **Computation**: Compute Ray-Singer torsion log(tau_RS) = -sum_p (-1)^p p zeta_p'(0) across the Jensen family. This is the canonical cutoff-free spectral invariant.
- **Gate**: TORSION-52
  - **PASS**: tau_RS(tau) has nontrivial structure (minimum, inflection, or discontinuity at fold). Provides cutoff-independent probe.
  - **INFO**: tau_RS(tau) monotone (no new structure beyond spectral action).
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_analytic_torsion.py`

---

#### W1-F: GL-JOSEPHSON-52 -- Ginzburg-Landau fabric dynamical matrix
- **Recommended by**: Landau, Tesla, QA, Berry, Volovik, Nazarewicz, Cosmic-Web (7 reviewers)
- **Agent**: Landau-Condensed-Matter-Theorist (Opus)
- **Cost**: MEDIUM (6x6 matrix at 14 K-shells on 32-cell lattice)
- **Script**: `s52_gl_josephson.py`
- **Input**: GL coefficients a = 14.02, b = 15.18 (S43); rho_s tensor (S47); Josephson hierarchy J_C2 = 0.933, J_su2 = 0.059, J_u1 = 0.034 (S47); Leggett modes (S48)
- **Computation**: Construct 6x6 dynamical matrix (3 amplitudes + 3 phases) for the 3-sector GL functional on the 32-cell lattice. Diagonalize at each K. Extract 6 dispersion branches. Test for anomalous dispersion.
- **Gate**: GL-JOSEPHSON-52
  - **PASS**: Any mode has |alpha_eff - 2| > 0.05 at K < 0.2 M_KK. New dispersion physics identified.
  - **FAIL**: All modes K^2. Fabric physics confirms single-cell picture.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_gl_josephson.py`
- **Note**: Include Feshbach coupling diagnostic at the phi crossing within this computation (Landau recommendation).

---

#### W1-G: QM-DISPERSION-52 -- Quantum metric K^4 correction (C-12)
- **Recommended by**: Berry, QA, Spectral-Geom, Landau (4 reviewers)
- **Agent**: Berry-Geometric-Phase-Theorist (Opus)
- **Cost**: MEDIUM (Bloch eigenstate computation on 32-cell lattice, numerical differentiation)
- **Script**: `s52_qm_dispersion.py`
- **Input**: Josephson Hamiltonian (S47), BCS ground state (S48), tessellation geometry (S41)
- **Computation**: Compute quantum metric tensor g_ij(K) for the Goldstone Bloch state on the 32-cell fabric. Extract K^4 coefficient alpha_QM from the quantum metric integral over the Brillouin zone.
- **Gate**: QM-DISPERSION-52
  - **PASS**: K^4 correction modifies effective power-law index by > 0.01 at K_pivot. Third route to viable n_s (orthogonal to Window 1 and W7).
  - **FAIL**: K^4 correction < 0.001 at K_pivot. Quantum metric negligible for dispersion.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_qm_dispersion.py`

---

#### W1-H: PL-TDUALITY-52 -- Poisson-Lie T-duality feasibility check
- **Recommended by**: String, KK, Connes (3 reviewers)
- **Agent**: String-Theory-Theorist (Opus)
- **Cost**: LOW (algebraic: identify Drinfeld double, construct dual metric, check spectral action structure)
- **Script**: `s52_pl_tduality.py`
- **Input**: SU(3) structure constants, Jensen metric components, Borel subalgebra of sl(3,C)
- **Computation**: (a) Identify the Drinfeld double D = SU(3) bowtie G* for the simplest Manin triple. (b) Construct the dual metric on G*. (c) Compute the first 50 Dirac eigenvalues on G* at the dual of the fold. (d) Check whether the spectral action has a minimum (non-monotone).
- **Gate**: PL-TDUALITY-52
  - **PASS**: Dual-frame spectral action has a minimum. W4 is frame-dependent. New stabilization route.
  - **FAIL**: Dual spectral action also monotone. W4 is frame-independent. Stabilization definitively closed.
  - **INFO**: Dual metric ill-defined or non-compact. Computation blocked.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_pl_tduality.py`

---

#### W1-I: N-PAIR-FULL-52 -- Full-spectrum pair number
- **Recommended by**: Nazarewicz, Volovik, Landau, Sagan, Feynman, Tesla, Cosmic-Web, Connes, Kitaev, Berry, Quantum-Foam (11 reviewers)
- **Agent**: Nazarewicz-Nuclear-Structure-Theorist (Opus)
- **Cost**: MEDIUM (992-mode ED, standard shell-model diagonalization)
- **Script**: `s52_n_pair_full.py`
- **Input**: 992-mode Dirac spectrum (`s44_dos_tau.npz`), Kosmann V matrix
- **Computation**: Exact diagonalization of the BCS Hamiltonian on the full 992-mode spectrum at the van Hove fold. Extract N_pair from the ground state occupation numbers.
- **Gate**: N-PAIR-FULL-52
  - **PASS**: N_pair >= 2. Q-theory CC crossing at tau* = 0.170 survives (Window 2).
  - **FAIL**: N_pair = 1 (confirming 8-mode truncation). CC problem has no surviving internal route.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_n_pair_full.py`
- **Note**: This has been queued since S46. 11 reviewers flag it. Execute it.

---

#### W1-J: HAWKING-T-SWEEP-52 -- T_acoustic parametric sweep
- **Recommended by**: Hawking, QA, Volovik (3 reviewers)
- **Agent**: Hawking-Theorist or QA-Theorist (Opus)
- **Cost**: LOW (evaluate Barcelo formula at 5-10 off-Jensen points using existing data)
- **Script**: `s52_hawking_t_sweep.py`
- **Input**: S36 V matrix, S40 dispersion data, off-Jensen eigenvalue data (S41)
- **Computation**: Compute T_acoustic and T_Gibbs at 5-10 different geometry points (including off-Jensen). Test whether T_acoustic/T_Gibbs = 0.993 is structural or coincidental.
- **Gate**: HAWKING-T-SWEEP-52
  - **PASS**: T_acoustic/T_Gibbs stable within 5% across all geometry points. Structural theorem.
  - **FAIL**: Ratio varies > 20% off-Jensen. Coincidence at the Jensen fold.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_hawking_t_sweep.py`

---

#### W1-K: LIOUVILLIAN-52 -- Liouvillian spectral gap
- **Recommended by**: Kitaev (1 reviewer, but computation is 10 lines on 8x8 matrix)
- **Agent**: Kitaev-Chaos-Diagnostics (Opus)
- **Cost**: LOW (64x64 matrix diagonalization)
- **Script**: `s52_liouvillian.py`
- **Input**: N_pair = 1 BCS Hamiltonian (8 modes)
- **Computation**: Construct Liouvillian L[rho] = -i[H, rho] as a 64x64 matrix. Diagonalize. Extract the Ruelle-Pollicott gap (smallest nonzero Re(lambda)).
- **Gate**: LIOUVILLIAN-52
  - **INFO**: gamma_RP value. If < 0.005 M_KK, confirms exact integrability. If > 0.005, partial chaoticity in the Liouvillian.
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_liouvillian.py`

---

### Wave 2: The Decisive Computation (depends on W1-A, W1-B)

#### W2-A: 12D-REDUCTION-52 -- Submersion decomposition of M^4 x SU(3)

**This is the computation that 23 reviewers converge on. It has never been performed in 51 sessions.**

- **Recommended by**: Baptista, KK, SP, Einstein, Feynman, Volovik, Hawking, Tesla, Sagan, Connes, Landau, QA, Spectral-Geom, Quantum-Foam, String, Cosmic-Web, Neutrino, Dirac (18 explicit, 23 implicit)
- **Agent**: Baptista-Spacetime-Analyst + SP-Geometer (Opus, 2 agents if team format; single agent if solo)
- **Cost**: HIGH (tensor algebra on specific geometry, fiber integration, coupled ODE system)
- **Script**: `s52_12d_reduction.py`
- **Input**:
  - Baptista Paper 13 eq 1.4 (submersion metric)
  - R_K(tau) (E3, computed analytically, D07 Section III)
  - Four curvature invariants (D07 Section III)
  - G_mod = 5.0 (S40)
  - M_KK from W1-B (DDG-MKK-52)
  - tau_i from W1-A (WDW-INITIAL-52)
  - Type D simplification (SP S50): Weyl reduces to single scalar Psi_2

- **Procedure** (following Baptista S1):
  1. Write the 12D metric as g_P = g_M(x) + 2 A_mu(x) dx^mu otimes Killing + g_K(tau(x))
  2. Compute the submersion decomposition R_P = R_M + R_K - |F|^2 - |S|^2 - |N|^2 - 2 delta N
  3. N = 0 under volume preservation (G6); |S|^2 from Killing vector integrals on fiber
  4. Integrate over SU(3) fiber with tau-dependent volume form to get S_4D[tau, g_M]
  5. Read off modulus kinetic term G_mod(tau) tau_dot^2 and potential V_KK(tau)
  6. Write coupled Friedmann-modulus equations:
     - H^2 = (8 pi G / 3) [G_mod tau_dot^2 / 2 + V_KK(tau)]
     - tau'' + 3H tau' + (1/G_mod) dV_KK/dtau = 0
  7. Integrate numerically from tau_i (from W1-A) to tau_fold
  8. Extract: w(tau), N_e (total e-folds), K_pivot = k_CMB * exp(N_e) / M_KK

- **Gate**: EFOLD-MAPPING-52 (the master gate)
  - **PASS**: K_pivot < K* = 0.087 M_KK (equivalently, N_e >= 3.1 from tau_i <= 1.7e-5). Framework's cosmological predictions live in the SA-Goldstone mixing window.
  - **MARGINAL**: K_pivot in [0.087, 0.5] M_KK. Partial mixing. n_s prediction shifts but may not reach 0.965.
  - **FAIL**: K_pivot > 0.5 M_KK. All cosmological predictions excluded. Publish the mathematics.

- **Secondary outputs**:
  - V_KK(tau) from KK reduction (compare to spectral action V_SA -- if they differ, S3 is resolved)
  - w(tau) during stiff epoch (confirm or deny w = 1 assumption)
  - G_N(tau) from the reduction (compare to Sakharov ratio)
  - Mixing parameter beta(K) from gauge-gravity cross-terms (KK recommendation: if beta > 0.9 derived, Window 1 opens from coupling side)

- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_12d_reduction.py`

---

#### W2-B: SIGMA8-MIXING-52 -- sigma_8 in the SA-Goldstone mixing regime
- **Recommended by**: Feynman, Sagan, Cosmic-Web (3 reviewers)
- **Agent**: Cosmic-Web-Theorist (Opus)
- **Cost**: LOW (recompute sigma_8 integral with corrected alpha_s from mixing)
- **Script**: `s52_sigma8_mixing.py`
- **Input**: K_pivot and beta from W2-A, SA correlator data (S51), Planck normalization
- **Computation**: If W2-A produces K_pivot < K*, recompute sigma_8 with the mixing-regime alpha_s (in [-0.040, 0]) instead of the rigid alpha_s = -0.069. This resolves the sigma_8 logical inconsistency identified by Sagan.
- **Gate**: SIGMA8-MIXING-52
  - **PASS**: sigma_8(mixing) in [0.77, 0.83]. Framework has a consistent prediction suite.
  - **FAIL**: sigma_8(mixing) outside [0.75, 0.85]. Mixing regime produces unphysical sigma_8.
- **Depends on**: W2-A (K_pivot and beta values)
- **Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe" tier0-computation/s52_sigma8_mixing.py`

---

### Wave 3: Follow-ups (conditional on Wave 2 results)

#### W3-A: NS-PREDICTION-52 -- Full n_s prediction in mixing regime
- **Condition**: W2-A PASSES (K_pivot < K*)
- **Recommended by**: All 23 reviewers (implicit)
- **Agent**: Connes-NCG-Theorist or Tesla-Resonance (Opus)
- **Cost**: LOW (evaluate SA-Goldstone mixing model at derived K_pivot and beta)
- **Script**: `s52_ns_prediction.py`
- **Input**: K_pivot, beta, SA correlator sector weights (S51), Goldstone propagator (S50)
- **Computation**: Compute n_s and alpha_s from the full mixing model at the physically derived K_pivot.
- **Gate**: NS-PREDICTION-52
  - **PASS**: n_s in [0.955, 0.975], alpha_s in [-0.040, 0]. Consistent with Planck.
  - **FAIL**: n_s outside Planck 3-sigma range. Mixing model insufficient.

---

#### W3-B: FIRST-SOUND-BAO-52 -- Anisotropic BAO imprint
- **Condition**: W2-A produces the full acoustic metric (c_fabric tensor from the reduction)
- **Recommended by**: QA, Volovik, Cosmic-Web, Landau, Tesla (5 reviewers)
- **Agent**: QA-Theorist (Opus)
- **Cost**: MEDIUM (Boltzmann transfer with anisotropic sound speed)
- **Script**: `s52_first_sound_bao.py`
- **Input**: Fabric sound speed tensor c_ij (from W2-A or S47), tessellation geometry (S41), S44 first-sound estimate
- **Computation**: Compute the first-sound BAO ring position and angular dependence from the anisotropic Josephson coupling tensor. This is the one acoustic observable distinct from LCDM that does NOT depend on K_pivot.
- **Gate**: FIRST-SOUND-BAO-52
  - **PASS**: Secondary ring detectable at > 2 sigma with DESI Y5. Distinct from LCDM.
  - **FAIL**: Ring amplitude below 1 sigma. Undetectable.

---

#### W3-C: OFFJENSEN-PMNS-52 -- Off-Jensen PMNS overlap
- **Condition**: Independent of W2 (can run if resources permit)
- **Recommended by**: Neutrino, Berry, KK, SP, Connes, Sagan, Spectral-Geom, String, Baptista (9 reviewers)
- **Agent**: Neutrino-Detection-Specialist or Berry-Theorist (Opus)
- **Cost**: MEDIUM (2-5 hours per off-Jensen point, need 5-10 points)
- **Script**: `s52_offjensen_pmns.py`
- **Input**: D_K construction code, 5 off-Jensen metric directions in the U(2)-invariant family
- **Computation**: (a) Compute D_K eigenvalues at 5-10 off-Jensen points. (b) Extract the 3x3 PMNS overlap matrix between eigenspaces at off-Jensen and Jensen reference. (c) Test for nonzero mixing angles.
- **Gate**: PMNS-OFFJENSEN-52
  - **PASS**: sin^2(theta_12) in [0.25, 0.35] at any off-Jensen point. Mixing exists.
  - **FAIL**: All mixing angles < 0.01 at all tested points. Jensen and off-Jensen equally locked.
  - **Depends on**: Neutrino pre-registered gate table

---

#### W3-D: WDAVG-DS-52 -- WDW-averaged spectral dimension
- **Condition**: W1-A produces Psi(tau) wavefunction
- **Recommended by**: Quantum-Foam (2 new gates proposed)
- **Agent**: Quantum-Foam-Theorist (Opus)
- **Cost**: LOW (integral over tau with known heat kernel)
- **Script**: `s52_wdavg_ds.py`
- **Input**: Psi(tau) from W1-A, D_K eigenvalue data at multiple tau
- **Computation**: d_s(t) = -2 d/d(log t) log[ integral dtau |Psi[tau]|^2 Tr(exp(-t D_K^2(tau))) ]
- **Gate**: DS-QUANTUM-52
  - **PASS**: d_s(t -> 0) in [1.5, 2.5]. CDT d_s = 2 reproduced quantum-mechanically.
  - **FAIL**: d_s(t -> 0) > 5. No CDT connection.

---

## III. Gate Registry

All gate IDs use S52 prefix to avoid collision with S50/S51 gates.

| Gate ID | Wave | PASS Criterion | FAIL Criterion | Upstream |
|:--------|:-----|:---------------|:---------------|:---------|
| WDW-INITIAL-52 | W1-A | |Psi|^2 peaks at tau < 10^{-5} | Peak at tau > 0.01 | None |
| DDG-MKK-52 | W1-B | M_KK within 1 OOM, 3 couplings consistent | Spread > 3 OOM | None |
| CASIMIR-JOSEPHSON-52 | W1-C | J_12/J_23 algebraic in C_2 | Non-Casimir | None |
| ETA-B-52 | W1-D | CP-odd phase nonzero, eta_B within 3 OOM | Phase = 0 | None |
| TORSION-52 | W1-E | tau_RS has nontrivial structure | Monotone | None |
| GL-JOSEPHSON-52 | W1-F | |alpha_eff - 2| > 0.05 at K < 0.2 | All K^2 | None |
| QM-DISPERSION-52 | W1-G | K^4 index shift > 0.01 at K_pivot | < 0.001 | None |
| PL-TDUALITY-52 | W1-H | Dual SA has minimum | Also monotone | None |
| N-PAIR-FULL-52 | W1-I | N_pair >= 2 | N_pair = 1 | None |
| HAWKING-T-SWEEP-52 | W1-J | T_acoustic/T_Gibbs stable within 5% | Varies > 20% | None |
| LIOUVILLIAN-52 | W1-K | gamma_RP value (INFO) | -- | None |
| **EFOLD-MAPPING-52** | **W2-A** | **K_pivot < 0.087 M_KK** | **K_pivot > 0.5 M_KK** | W1-A, W1-B |
| SIGMA8-MIXING-52 | W2-B | sigma_8 in [0.77, 0.83] | Outside [0.75, 0.85] | W2-A |
| NS-PREDICTION-52 | W3-A | n_s in [0.955, 0.975] | Outside Planck 3-sigma | W2-A |
| FIRST-SOUND-BAO-52 | W3-B | Detectable > 2 sigma DESI Y5 | < 1 sigma | W2-A |
| PMNS-OFFJENSEN-52 | W3-C | sin^2(theta_12) in [0.25, 0.35] | All < 0.01 | None |
| DS-QUANTUM-52 | W3-D | d_s(UV) in [1.5, 2.5] | > 5 | W1-A |

---

## IV. Decision Points

**Decision Point 1 (after Wave 1)**:
- If WDW-INITIAL-52 PASSES: tau_i = 0 is the natural initial condition. Proceed to W2-A with large e-fold margin.
- If WDW-INITIAL-52 FAILS: tau_i requires fine-tuning. W2-A proceeds but EFOLD-MAPPING-52 margin is thin.
- If DDG-MKK-52 FAILS: M_KK undetermined. W2-A cannot produce a physical K_pivot. Reassess.
- If N-PAIR-FULL-52 PASSES (N >= 2): CC crossing survives. Carry to W3.
- If GL-JOSEPHSON-52 PASSES: New dispersion mode found. This is a potential third route to n_s independent of K_pivot.

**Decision Point 2 (after Wave 2)**:
- If EFOLD-MAPPING-52 PASSES: Execute all W3 computations. Framework lives in the SA-Goldstone mixing window. Probability revises upward.
- If EFOLD-MAPPING-52 MARGINAL: Execute W3-A (n_s prediction) and W3-B (BAO). Assess whether partial mixing produces viable predictions.
- If EFOLD-MAPPING-52 FAILS: Do NOT execute W3-A or W3-B. Execute W3-C (off-Jensen, independent of K_pivot). Publish the mathematics. Session closes the cosmological program.

---

## V. Wave 4: Everything Else (parallel, no dependencies)

Every reviewer suggestion that isn't closed or subsumed gets computed. No deferrals.

### W4-A: Unified Action S[tau, Delta, theta] (UNIFIED-ACTION-52)
**Recommended by**: Feynman, Connes, Tesla | **Agent**: feynman-theorist | **Cost**: MEDIUM
Write the unified action from existing data (spectral action for tau, BCS for Delta, Josephson for theta). W2-A refines it; this is the FIRST DRAFT.
**Gate**: INFO (does the action have a consistent variational structure?)

### W4-B: Full HFB Self-Consistent Gap at N_pair = 1 AND 2 (HFB-FULL-52)
**Recommended by**: Nazarewicz | **Agent**: nazarewicz | **Cost**: MEDIUM
Run at both N_pair values. If N_pair = 1 it's a cross-check. If N_pair = 2 it's new physics. Don't wait for N-PAIR-FULL.
**Gate**: PASS if converges at both N_pair values

### W4-C: Tree-Level Bogoliubov Scattering Amplitude (BOGOLIUBOV-AMP-52)
**Recommended by**: Feynman | **Agent**: feynman-theorist | **Cost**: LOW
The ONE number Feynman says the framework should compute. A scattering amplitude IS the Feynman Test.
**Gate**: INFO (does a finite amplitude emerge from the spectral triple?)

### W4-D: Bekenstein Bound on Spectral Triple (BEKENSTEIN-52)
**Recommended by**: Hawking | **Agent**: hawking-theorist | **Cost**: LOW
Structural math. The bound constrains the information content of the internal space.
**Gate**: INFO (is the bound saturated, violated, or far from saturated?)

### W4-E: Friedrich-Kirchberg Weyl Bound (FK-BOUND-52)
**Recommended by**: Spectral-Geom | **Agent**: spectral-geometer | **Cost**: LOW
Sharpens the eigenvalue floor. 30 minutes of computation on existing data.
**Gate**: INFO (does the bound improve on Lichnerowicz?)

### W4-F: Ricci Flow vs Modulus Dynamics (RICCI-FLOW-52)
**Recommended by**: Baptista | **Agent**: baptista-spacetime-analyst | **Cost**: MEDIUM
Compare Ricci flow on Jensen SU(3) to the modulus trajectory. Independent of W2-A.
**Gate**: INFO (does Ricci flow reproduce the spectral action gradient?)

### W4-G: LOG-SIGNED-40 Tau Sweep (LOG-SIGNED-52)
**Recommended by**: Paasch | **Agent**: gen-physicist | **Cost**: LOW (~30 min)
Uncomputed since S40. Signed boson-fermion log sum on 2912 eigenvalues across tau.
**Gate**: INFO (does the signed sum have a zero crossing?)

### W4-H: Internal MSW During Transit (MSW-TRANSIT-52)
**Recommended by**: Neutrino | **Agent**: neutrino-detection-specialist | **Cost**: MEDIUM
Transit dynamics ARE computed (S38 dt_transit, v_terminal). Apply MSW formalism to the sector-resolved spectrum during the quench.
**Gate**: INFO (does MSW modify the neutrino mass hierarchy prediction R = 27.2?)

### W4-I: Multi-Temperature Jacobson Derivation (JACOBSON-MULTI-T-52)
**Recommended by**: Hawking | **Agent**: hawking-theorist | **Cost**: MEDIUM
Derives the modulus EOM from thermodynamics of the GGE. Independent cross-check of W2-A.
**Gate**: PASS if the Jacobson derivation reproduces the KK modulus equation

### W4-J: Stochastic Metric Noise from Tessellation (METRIC-NOISE-52)
**Recommended by**: Quantum-Foam | **Agent**: quantum-foam-theorist | **Cost**: LOW
GQuEST-class prediction. It's a TESTABLE PREDICTION — compute it.
**Gate**: INFO (amplitude and frequency spectrum of the noise)

### W4-K: Void Size Function at Both alpha_s Values (VOID-FUNCTION-52)
**Recommended by**: Cosmic-Web | **Agent**: cosmic-web-theorist | **Cost**: MEDIUM
Compute at alpha_s = -0.069 (O-Z) AND alpha_s from the mixing regime. Don't wait for W3-A.
**Gate**: INFO (15-25% excess voids at R = 15-20 h^{-1} Mpc predicted by CW)

### W4-L: Petrov Type Transition at tau = 0.895 (PETROV-0895-52)
**Recommended by**: SP | **Agent**: schwarzschild-penrose-geometer | **Cost**: LOW
Mathematical structure. The Weyl zero-crossing IS a GW polarization transition. Compute it.
**Gate**: INFO (D → O → D transition confirmed or denied?)

## Items Genuinely Closed (not computed)

| Suggestion | Status | Reason |
|:-----------|:-------|:-------|
| Cheeger constant | SUBSUMED by GL-JOSEPHSON (W1-F) |
| CDM free-streaming | PRE-EMPTED: LRD confirms framework CDM = LCDM at all scales |
| Classical lattice spectral dimension | CLOSED (S50 Route 4) |
| ALPHA-ENV-43 | CLOSED (S43 W6-4) |
| PHI-GOLDEN-22, SIX-SEQUENCE | CLOSED (S48) |
| Polariton model | CLOSED (S51 POLARITON-51 FAIL) |
| Off-Jensen Berry curvature | SUBSUMED by W3-C (off-Jensen PMNS includes Berry diagnostics) |

---

## VI. Execution Notes

### Agent Assignment (if team format, max 3 agents)

**Option A: 3-agent team**
- Agent 1 (Baptista/SP): W1-B, W2-A, W2-B (the KK reduction chain)
- Agent 2 (Nazarewicz/Landau): W1-F, W1-I, W1-K (many-body computations)
- Agent 3 (Hawking/Quantum-Foam): W1-A, W1-J, W3-D (quantum cosmology chain)
- Remaining W1 items (C, D, E, G, H) distributed by bandwidth

**Option B: Solo agent, 3 waves**
- Wave 1: Execute all 11 W1 items in parallel batches of 3-4
- Wave 2: Execute W2-A after W1-A and W1-B complete
- Wave 3: Execute W3 items conditional on W2 results

### Computational Resources
- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- GPU: AMD RX 9070 XT (17.1 GB VRAM) -- useful for large eigenvalue problems in W1-I and W2-A
- RAM: 128 GB -- sufficient for 992-mode ED
- Estimated total runtime: 4-8 hours for all W1 items; 2-4 hours for W2; 2-4 hours for W3
- Script prefix: `s52_`
- Constants: Import from `tier0-computation/canonical_constants.py`

### Output Files
- Results: `sessions/session-52/session-52-results-workingpaper.md`
- Gate verdicts: Record in results file with PASS/FAIL/INFO/MARGINAL
- New scripts: `tier0-computation/s52_*.py`

---

## VII. What Changes If EFOLD-MAPPING-52 Passes

If the master gate passes, Session 52 transforms the framework from "2-4% probability, conditional on an uncomputed mapping" to a testable theory with:
- A derived (not assumed) initial condition (from WDW)
- A derived (not assumed) M_KK (from DDG)
- A derived (not assumed) K_pivot (from the 12D reduction)
- A consistent prediction suite: n_s, alpha_s, sigma_8, w_0 = -1, w_a = 0
- The first cosmological predictions from a dimensional reduction on a compact Lie group with Jensen deformation

The framework probability would revise upward from the structural floor. The exact revision depends on whether the derived n_s and sigma_8 match observations.

## VIII. What Changes If EFOLD-MAPPING-52 Fails

If the master gate fails, Session 52 produces:
- A definitive answer: the cosmological interpretation of the spectral geometry does not work as assumed
- 36 (or 12-25, per Sagan) publishable mathematical results that survive regardless
- The first explicit KK reduction on Jensen-deformed SU(3), which is a mathematical contribution to the KK literature
- Closure of the cosmological program with an honest, computed verdict rather than an assumed one

The mathematics is permanent. The cosmology is conditional. Session 52 resolves the condition.

---

## IX. Reviewer Attribution Summary

Every computation in this plan traces to specific reviewer recommendations:

| Computation | # Reviewers | Named Reviewers |
|:-----------|:------------|:----------------|
| EFOLD-MAPPING-52 (W2-A) | 23 | All |
| N-PAIR-FULL-52 (W1-I) | 11 | Nazarewicz, Volovik, Landau, Sagan, Feynman, Tesla, Cosmic-Web, Connes, Kitaev, Berry, Quantum-Foam |
| Off-Jensen PMNS (W3-C) | 9 | Neutrino, Berry, KK, SP, Connes, Sagan, Spectral-Geom, String, Baptista |
| GL-JOSEPHSON (W1-F) | 7 | Landau, Tesla, QA, Berry, Volovik, Nazarewicz, Cosmic-Web |
| WDW-INITIAL (W1-A) | 6 | Quantum-Foam, Hawking, Einstein, String, Tesla, Volovik |
| Baryogenesis (W1-D) | 5 | Dirac, Hawking, Volovik, Feynman, Connes |
| DDG M_KK (W1-B) | 5 | KK, Baptista, SP, Einstein, String |
| Analytic torsion (W1-E) | 5 | Spectral-Geom, Connes, Berry, Hawking, KK |
| First-sound BAO (W3-B) | 5 | QA, Volovik, Cosmic-Web, Landau, Tesla |
| Casimir-Josephson (W1-C) | 4 | Paasch, Landau, Tesla, Berry |
| QM-Dispersion (W1-G) | 4 | Berry, QA, Spectral-Geom, Landau |
| PL T-duality (W1-H) | 3 | String, KK, Connes |
| Hawking T-sweep (W1-J) | 3 | Hawking, QA, Volovik |
| sigma_8 mixing (W2-B) | 3 | Feynman, Sagan, Cosmic-Web |
| Liouvillian gap (W1-K) | 1 | Kitaev |
| WDW spectral dim (W3-D) | 1 | Quantum-Foam |
