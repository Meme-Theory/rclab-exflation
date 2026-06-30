# Session 61 Plan: Zetas, and Transits, and CC; OH MY!

**Date**: 2026-03-28
**Format**: Parallel single-agent computations across 5 execution waves
**Source**: `sessions/archive/session-60/session-60-wayforward.md` (99-entry deduplicated agenda, 96 unique tasks)
**Results file**: `sessions/archive/session-61/session-61-results-workingpaper.md`
**Motivation**: S60 retracted H_0=68.8 (PW divergence), closed 6 CC mechanisms, broke GGE integrability, killed leptogenesis. Framework needs a_2 computed correctly, plus six open fronts: spectral zeta, transit dynamics, CC stabilization, GGE survival, observational signatures, deep VdD theory.

---

## Execution Wave Structure

```
Wave 1 (FOUNDATION — 5)
  ╠══ DECISION POINT 1: a_2 + spin connection + A-tensor ══
Wave 2 (THREE-LANE PARALLEL — 20)
  ├── Lane 1: a_2 cross-checks (6)
  ├── Lane 2: GGE survival (11)
  └── Lane 3: Zeta core (4)
  ╠══ DECISION POINT 2: GGE + zeta + a_2 gauntlet ══
Wave 3 (ALPHA + TRANSIT + CC + ZETA-DEP — 20)
  ╠══ DECISION POINT 3: alpha regime + transit SA ══
Wave 4 (SIGNATURES + DEEP THEORY — 16)
Wave 5 (EXTENSIONS + DEPENDENT + SPECULATIVE — 29)
Wave 6 (LOST TREASURES WORKSHOP — 6, workshop mode)
```

**Python**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"` | **Script prefix**: `s61_` | **Output**: `computations/` | **Constants**: `from canonical_constants import *` always | **S60 data**: `computations/s60_*.npz`

---

## Wave 1 — FOUNDATION (5 entries)

### USER-1: Compound Staircase Modification
**Agent**: landau-condensed-matter-theorist | **Priority**: HIGH | **Cost**: MEDIUM (~30 min CPU)
**Computation**: Rebuild BCS ground-state energy staircase E_GS(N) with three corrections self-consistently: (1) Penrose back-reaction (delta_F = 0.482 M_KK), (2) Josephson-broken Richardson-Gaudin integrals (delta_k = 0.328), (3) Bekenstein entropy constraint (S_max/S_Bek = 6.44 for (0,0) sector).
**Method**: Load s60_staircase_ext.npz for baseline E_GS(N=0..4). Add Penrose back-reaction via delta_F from s60_penrose_superrad.npz. Add Josephson integrability breaking via delta_k = 0.328 from s60_rg_integrals.npz to compute GGE→Gibbs correction. Add Bekenstein constraint: for each N, check S_BCS(N) < S_Bek(N), project if violated. Compute corrected epsilon(N) = E_GS(N) - E_GS(N-1).
**Input**: computations/s60_staircase_ext.npz, computations/s60_penrose_superrad.npz, computations/s60_rg_integrals.npz, computations/s60_bekenstein_pw.npz, canonical_constants.py
**Output**: s61_compound_staircase.py, s61_compound_staircase.npz, s61_compound_staircase.png
**Gate**: COMPOUND-STAIRCASE-61. PASS if corrected epsilon differs from 0.046 by >10x. FAIL if ~0.046. INFO if 2-10x.
**Depends On**: none

---

### USER-2 / SP-1: Heat Kernel a_2 from Local Curvature Integral
**Agent**: spectral-geometer | **Priority**: HIGH | **Cost**: LOW (~1 min CPU)
**Computation**: Compute the Seeley-DeWitt a_2(D_K^2) from local curvature integral on Jensen-deformed SU(3). THE single most important uncomputed quantity.
**Method**: (1) Compute Ricci scalar R(tau) from Milnor's formula for left-invariant metrics using su(3) structure constants and Jensen metric g_ab(tau). Cross-check: R(0)=12 for round metric. (2) Lichnerowicz endomorphism E = R/4. (3) a_2 = (4pi)^{-4} * 16 * (5R/12) * Vol(SU(3),g(tau)). (4) Evaluate at 100 tau points in [0,0.5]. (5) At tau_fold=0.19, extract H_0 via CCM dictionary: M_Pl^2 = 2*a_2/(4pi)^2, H_0 = sqrt(Lambda_obs/(3*M_Pl^{-2})). Lambda_obs = 1.1056e-52 m^{-2}. (6) Compare to PW partial sums from s60_pw_h0_conv.npz.
**Input**: canonical_constants.py (structure constants, Jensen metric, M_KK, Vol_SU3), computations/s60_pw_h0_conv.npz, Baptista Paper 13 eq 2.40
**Output**: s61_heat_kernel_a2.py, s61_heat_kernel_a2.npz (a_2(tau), R(tau), Vol(tau), M_Pl^2, H_0), s61_heat_kernel_a2.png
**Gate**: HEAT-KERNEL-A2-61. PASS if a_2(tau_fold) finite and H_0 in [60,80] km/s/Mpc. FAIL if H_0 outside [40,100] or divergent. INFO if H_0 well-defined but outside [60,80].
**Depends On**: none
**Cross-agent perspectives**: VOL-10 (superfluid vacuum = finite), PHONON-1 (PW=UV catastrophe, heat kernel=NCG density functional), VDD-1 (Paper 01 guarantees a_2 finite), SPEC-1 (closed-form in seconds)

---

### USER-4 / VDD-2: O'Neill A-Tensor Cross-Terms (Kasparov Factorization)
**Agent**: van-den-dungen-bridge-theorist | **Priority**: CRITICAL | **Cost**: ~1 hr CPU
**Computation**: Verify spectral action on M^4 x SU(3) correctly decomposes into base+fiber by computing O'Neill A-tensor and T-tensor. For product metric, confirm A=T=0 (exact factorization). Then re-check when gauge connections are introduced via inner fluctuations.
**Method**: (1) For product metric: verify horizontal vector fields have horizontal Lie brackets (A=0), fibers totally geodesic (T=0). (2) Introduce inner fluctuations (NCG gauge connection) and recompute effective metric. (3) If A or T nonzero, compute cross-term corrections to a_2(D_total^2) = a_2(D_M^2)*a_0(D_K^2) + a_0(D_M^2)*a_2(D_K^2) + cross-terms.
**Input**: Jensen metric g_K(tau), inner fluctuation formula from VdD Paper 06, canonical_constants.py
**Output**: s61_oneill_crossterms.py, s61_oneill_crossterms.npz
**Gate**: A-TENSOR-61. PASS if cross-terms < 1%. FAIL if > 10%. INFO if 1-10%.
**Depends On**: none
**Paper Reference**: VdD Paper 01 Main Theorem; O'Neill 1966

---

### BAP-5: PW Data Audit — (1,2) Irrep Contamination Scope
**Agent**: baptista-spacetime-analyst | **Priority**: HIGH | **Cost**: ZERO (file scanning)
**Computation**: Determine which S27-S60 results are contaminated by the missing (1,2) irrep in S44 eigenvalue data (54% correction to cross-sector PW sums).
**Method**: Inventory all computation scripts S27-S60 that load s44_dos_tau.npz or eigenvalue data using cross-sector PW sums. Classify each as SAFE (singlet-only or per-sector) or CONTAMINATED (uses full PW sums). For CONTAMINATED, estimate fractional correction.
**Input**: computations/ and computations/ script directories
**Output**: s61_pw_audit.md (table), s61_pw_audit.py (automated scanner)
**Gate**: PW-AUDIT-61. INFO (audit). Contaminated results flagged for recomputation.
**Depends On**: none

---

### SPEC-5: Spin Connection Curvature Term in a_2
**Agent**: spectral-geometer | **Priority**: HIGH | **Cost**: LOW (~minutes)
**Computation**: Determine whether (1/12)*tr(Omega^2) in Gilkey a_2 formula is negligible vs R/6*tr(id) on Jensen-deformed SU(3).
**Method**: Compute spin connection omega^a_{bc} from su(3) structure constants + Jensen metric at tau_fold=0.19. Compute Omega = d(omega) + omega^omega. Evaluate (1/12)*tr(Omega^2) and compare to (5R/12)*16.
**Input**: canonical_constants.py, su(3) structure constants
**Output**: s61_spin_curvature.py, s61_spin_curvature.npz
**Gate**: SPIN-CURV-61. PASS if |tr(Omega^2)| < 0.1*(5R/12)^2. FAIL if > (5R/12)^2. INFO if 0.1-1.0.
**Depends On**: none

---

## Wave 2 — THREE-LANE PARALLEL (20 entries)

### Lane 1: a_2 Cross-Check Gauntlet

### HAWK-1: Zeta-Function Regularization Cross-Check of a_2
**Agent**: hawking-theorist | **Priority**: HIGH | **Cost**: ~30 min CPU
**Computation**: Compute spectral zeta zeta_{D_K^2}(s) from PW eigenvalues at fold, analytically continue to s=3, extract Res(zeta,s=3) giving a_2 by Minakshisundaram-Pleijel.
**Method**: (1) Compute zeta_{D_K^2}(s) for Re(s)>4 from PW eigenvalues at L_max=3..6. (2) Fit analytic structure using Pade/Richardson. (3) Extract residue at s=3. (4) Cross-check: Res(zeta,s=4) = a_0 = Vol*16/(4pi)^4.
**Input**: computations/s60_pw_h0_conv.npz, canonical_constants.py
**Output**: s61_zeta_regularization.py, s61_zeta_regularization.npz, s61_zeta_regularization.png
**Gate**: ZETA-A2-61. PASS if agrees with Gilkey a_2 within 5%. FAIL if >20%. INFO if 5-20% or W1 unavailable.
**Depends On**: USER-2 (for comparison)

---

### QA-8: Regularized Spectral Sum via Heat Kernel — Debye Analogy
**Agent**: quantum-acoustics-theorist | **Priority**: HIGH | **Cost**: ~5 min CPU
**Computation**: Replace divergent PW sum Tr(|D_K|) with heat-kernel-regularized Tr(|D_K|*exp(-t*D_K^2)). Evaluate at physical scale t=1/Lambda_KK^2. Verify regularized sum reproduces Seeley-DeWitt expansion.
**Method**: Compute Tr(|D_K|*exp(-t*lambda_n^2)) at 20 values of t from 10^{-4} to 10. Fit to polynomial in t to extract a_0, a_2, a_4.
**Input**: D_K eigenvalue files, canonical_constants.py
**Output**: s61_regularized_spectral_sum.py, s61_regularized_spectral_sum.npz, s61_regularized_spectral_sum.png
**Gate**: REG-SPECTRAL-61. PASS if converges (relative change <1% from L=5 to 6) and a_2 agrees with USER-2 to 10%. FAIL if divergent or disagrees. INFO if converges but a_2 unavailable.
**Depends On**: USER-2

---

### HAWK-9: Heat Kernel a_2 Tau Derivative
**Agent**: hawking-theorist | **Priority**: HIGH | **Cost**: ~1 hr CPU
**Computation**: Compute d(a_2)/d(tau) along transit tau in [0,0.25]. Determines whether G_eff changes during transit, feeds W3 transit SA.
**Method**: (1) R(tau) at 50 tau points via Milnor formula. (2) a_2(tau) = (4pi)^{-4}*16*(R/6+R/4)*Vol(tau). (3) Numerical and analytic derivatives. (4) Identify zeros/sign changes.
**Input**: canonical_constants.py, Jensen metric eigenvalues
**Output**: s61_a2_tau_derivative.py, s61_a2_tau_derivative.npz, s61_a2_tau_derivative.png
**Gate**: A2-TRANSIT-61. PASS if monotonic nonzero. FAIL if constant. INFO if sign change.
**Depends On**: USER-2

---

### SP-2: Conformal Interpretation of PW Spectral Sum Divergence
**Agent**: schwarzschild-penrose-geometer | **Priority**: MED | **Cost**: ~5 min CPU
**Computation**: Test whether heat kernel suppression plays the role of conformal factor in compactifying the PW sum. Compute partial zeta sums zeta_L(s) at L=0..7 for s=1..5, analytically continue to s=-1/2, compare with local a_2.
**Method**: (1) Partial zeta sums from PW eigenvalues. (2) Richardson/Shanks extrapolation. (3) Compare analytically continued value with SP-1 result.
**Input**: computations/s60_pw_h0_conv.npz, USER-2 output
**Output**: s61_pw_conformal_zeta.py, s61_pw_conformal_zeta.npz, s61_pw_conformal_zeta.png
**Gate**: PW-CONFORMAL-ZETA-61. PASS if agrees with local a_2 to <10%. FAIL if >100% or fails to converge. INFO if 10-100%.
**Depends On**: USER-2

---

### SPEC-4: Weyl Law Verification on Jensen SU(3)
**Agent**: spectral-geometer | **Priority**: MED | **Cost**: ~minutes
**Computation**: Verify eigenvalue asymptotics N(lambda) ~ C_8*Vol*lambda^8. Independent volume measurement.
**Method**: From 48-irrep data, compute N(lambda), fit Weyl term. Compare Weyl volume to analytic Vol(SU(3)).
**Input**: computations/s60_pw_h0_conv.npz, Vol(SU(3))
**Output**: s61_weyl_law.py, s61_weyl_law.npz, s61_weyl_law.png
**Gate**: WEYL-VERIFY-61. PASS if within 5%. FAIL if >20%. INFO if 5-20%.
**Depends On**: none

---

### NAZ-1: Particle-Number Projection for the Heat Kernel
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: HIGH | **Cost**: Moderate
**Computation**: Compute a_2(D_K^2) in number-projected BCS state (PBCS) and compare to unprojected BCS result. BCS breaks U(1)_7; PAV restores it.
**Method**: Exact number projection via gauge-angle integral P_N = (1/2pi) integral_0^{2pi} e^{i*phi*(N_hat-N)} d_phi. Compute a_2 from projected density using local curvature integral.
**Input**: S52 data (s52_hfb_full.npz), canonical_constants.py, Jensen curvature
**Output**: s61_proj_a2.py, s61_proj_a2.npz
**Gate**: PROJ-A2-61. PASS if |a_2^{PBCS} - a_2^{BCS}|/a_2^{BCS} < 5%. FAIL if >20%. INFO if 5-20%.
**Depends On**: USER-2

---

### Lane 2: GGE Survival — Multi-Method Assault

### TESLA-1: Thouless Time from Fabric Spectral Form Factor
**Agent**: tesla-resonance | **Priority**: HIGH | **Cost**: ~minutes CPU
**Computation**: Compute Thouless energy E_Th and time t_Th of the 32-cell Josephson fabric via SFF. Compare t_Th/t_transit.
**Method**: Diagonalize full fabric Hamiltonian (BCS+Josephson on CG(24)). Compute K(t) = |Tr(e^{-iHt})|^2/|Tr(1)|^2. Extract t_Th from ramp-plateau transition. Cross-check: D ~ E_J*a^2/hbar, t_Th ~ L^2/D.
**Input**: computations/s60_rg_integrals.npz (E_J=3.4, delta_k=0.328), computations/s60_pair_transfer.npz, canonical_constants.py
**Output**: s61_thouless_time.py, s61_thouless_time.npz, s61_thouless_time.png
**Gate**: GGE-THERM-61. PASS if t_Th/t_transit > 100. FAIL if < 1. INFO if [1,100].
**Depends On**: USER-1

---

### PHONON-3: Thouless Time on CG(24) via Spectral Gap
**Agent**: phonon-first-cosmologist | **Priority**: HIGH | **Cost**: seconds
**Computation**: Compute Thouless time from CG(24) = Cayley(S_4, 6 transpositions) graph Laplacian spectral gap. t_Th ~ d^2/E_J ~ 1.3 M_KK^{-1} — genuine race with transit.
**Method**: (1) CG(24) Laplacian eigenvalues lambda_pi from S_4 character table. (2) Spectral gap = smallest nonzero. (3) t_Th = 1/(E_J*lambda_1). (4) Spectral dimension d_s(t) from return probability on CG(24).
**Input**: S_4 character table, E_J from canonical_constants.py, t_transit from S38
**Output**: s61_thouless_cayley.py, s61_thouless_cayley.npz, s61_thouless_cayley.png
**Gate**: GGE-THERM-61. PASS if t_Th/t_transit > 10. FAIL if < 0.1. INFO if [0.1,10].
**Depends On**: none

---

### VOL-2: GGE Thermalization via Thouless Time
**Agent**: volovik-superfluid-universe-theorist | **Priority**: HIGH | **Cost**: minutes
**Computation**: Thouless time t_Th for Josephson fabric at N=2,4,8,16,32 via scaling formula. 3He-B expectation: FAIL (E_J=655 >> Delta).
**Method**: E_Th(N) = E_J/N^{2/3} for d=3. t_Th(N) = 1/E_Th(N). Compare to omega_tau^{-1}. Also Fermi golden rule Gamma_qp.
**Input**: E_J=655 M_KK, omega_tau=8.27, computations/s60_rg_integrals.npz, canonical_constants.py
**Output**: s61_gge_therm.py, s61_gge_therm.npz, s61_gge_therm.png
**Gate**: GGE-THERM-61. PASS if t_Th > 10*t_transit at N=32. FAIL if < 0.1*t_transit. INFO otherwise.
**Depends On**: none

---

### HAWK-2: Thouless Time — Many-Body ED
**Agent**: hawking-theorist | **Priority**: HIGH | **Cost**: ~1 hr GPU
**Computation**: Compute t_Th = hbar/delta_E for multi-cell Josephson BCS system via exact diagonalization, extrapolate to N~10^80.
**Method**: (1) N_cell Hilbert space (N=2,4,8) with Josephson coupling. (2) Diag many-body H. (3) Extract delta_E near E_F. (4) t_Th = hbar/delta_E. (5) Diffusive: t_Th(N) ~ N^2/D. (6) Extrapolate.
**Input**: computations/s60_rg_integrals.npz, computations/s59_page_curve.npz, canonical_constants.py
**Output**: s61_thouless_time.py, s61_thouless_time.npz, s61_thouless_time.png
**Gate**: THOULESS-GGE-61. PASS if t_Th > 10^3*t_transit. FAIL if < t_transit. INFO if [1, 10^3].
**Depends On**: none

---

### NAZ-3: GGE Thermalization via Compound Nucleus Formalism
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: HIGH | **Cost**: Moderate
**Computation**: Thouless time via compound nucleus doorway-state formalism. Spreading width D_spread. Compare t_Th to t_transit.
**Method**: Hauser-Feshbach averaging over RG quasi-integrals as resonances. Ericson fluctuation width from pair hopping. Gamma_CN -> 1/t_Th.
**Input**: computations/s60_rg_integrals.npz (delta_k=0.328), S49 fabric ED, canonical_constants.py
**Output**: s61_gge_thermalization.py, s61_gge_thermalization.npz
**Gate**: GGE-THERM-61. PASS if t_Th > 10*t_transit. FAIL if < 0.1*t_transit. INFO if [0.1,10].
**Depends On**: none

---

### SP-3: Thouless Time vs Conformal Time Budget
**Agent**: schwarzschild-penrose-geometer | **Priority**: HIGH | **Cost**: <1 min CPU
**Computation**: Does Josephson breaking have time to thermalize GGE within the causal domain? Compare t_Th to conformal time budget from S55.
**Method**: (1) Extract conformal time eta(tau) at BCS transition and horizon crossing. (2) t_Th from CG(24) spectral gap. (3) Compare.
**Input**: computations/s55_conformal_diagram.npz, computations/s60_rg_integrals.npz, computations/s57_percolation_cc.npz, canonical_constants.py
**Output**: s61_gge_therm_window.py, s61_gge_therm_window.npz, s61_gge_therm_window.png
**Gate**: GGE-THERM-61. PASS if t_Th/Delta_eta > 10. FAIL if < 0.1. INFO if [0.1,10].
**Depends On**: none

---

### PHONON-7: Integrability Breaking Scaling with N_cells
**Agent**: phonon-first-cosmologist | **Priority**: HIGH | **Cost**: Hours (GPU for N=32,64)
**Computation**: delta_k=0.328 at N=32. Scaling: delta_k ~ N^{-beta}? beta>0: GGE permanent. beta=0: thermalizes.
**Method**: For N=2,4,8,16,32,64: construct RG integrals I_k, add H_J, compute delta_k = ||[I_k,H_J]||/||I_k||. Fit delta_k(N) ~ N^{-beta}.
**Input**: canonical_constants.py, RG integrals from S57
**Output**: s61_integrability_scaling.py, s61_integrability_scaling.npz, s61_integrability_scaling.png
**Gate**: INTEG-SCALING-61. PASS if beta > 0.5. FAIL if < 0.1. INFO if 0.1-0.5.
**Depends On**: none

---

### TESLA-6: Josephson Collective Mode Integrability
**Agent**: tesla-resonance | **Priority**: HIGH | **Cost**: ~minutes
**Computation**: Level spacing statistics of Josephson Hamiltonian on CG(24). Poisson=integrable (GGE protected) vs GOE=chaotic (thermalizes).
**Method**: Construct H_J on CG(24) (degree 6, 32 vertices). Diag. Level spacing <r>. Compare S38 CHAOS-1.
**Input**: CG(24) adjacency matrix, E_J=3.4, V_pairing=0.081 (from computations/s60_pair_transfer.npz)
**Output**: s61_josephson_integrability.py, s61_josephson_integrability.npz, s61_josephson_integrability.png
**Gate**: JOSEPHSON-INTEG-61. PASS if <r> < 0.45 (Poisson). FAIL if > 0.50 (GOE). INFO if [0.45,0.50].
**Depends On**: none

---

### LANDAU-4: Fermi Liquid Parameters with Josephson Coupling
**Agent**: landau-condensed-matter-theorist | **Priority**: HIGH | **Cost**: ~30 min CPU
**Computation**: Extract Landau parameters F_l^{s,a} from 2-cell H_full including Josephson. Check Pomeranchuk stability.
**Method**: Diag 2-cell H_full. Extract scattering amplitudes. Decompose into angular harmonics. Check F_l > -(2l+1).
**Input**: computations/s60_rg_integrals.npz, computations/s58_pomeranchuk_gge.npz
**Output**: s61_fabric_landau_params.py, s61_fabric_landau_params.npz
**Gate**: POMERAN-FABRIC-61. PASS if all F_l stable. FAIL if Pomeranchuk violation. INFO if marginal.
**Depends On**: none

---

### LANDAU-8: Ginzburg Criterion for the CC Staircase
**Agent**: landau-condensed-matter-theorist | **Priority**: MED | **Cost**: ~15 min CPU
**Computation**: Compute Gi = (delta_F/F_0)^2 where delta_F = inter-cell fluctuation from Josephson, F_0 = 0.046. Gi>1 means mean-field staircase unreliable.
**Method**: delta_F ~ E_J*S_+(1)^2/N_modes with E_J=3.40, S_+(1)=0.936. If Gi>1, recompute with 2nd-order perturbation.
**Input**: computations/s60_staircase_ext.npz, computations/s60_pair_transfer_n4.npz, computations/s60_rg_integrals.npz
**Output**: s61_ginzburg_staircase.py, s61_ginzburg_staircase.npz
**Gate**: GINZBURG-CC-61. PASS if Gi < 0.1. FAIL if > 10. INFO if [0.1,10].
**Depends On**: none

---

### Lane 3: Spectral Zeta Core

### CONNES-1: Spectral Zeta Zero Location
**Agent**: connes-ncg-theorist | **Priority**: HIGH | **Cost**: minutes CPU
**Computation**: Construct zeta_{D_K}(s) from PW eigenvalues at fold (9280 eigenvalues). Locate ALL nontrivial zeros in 0 < Re(s) < 8.
**Method**: Evaluate |zeta(s)| on grid Re(s) in [0,8], Im(s) in [-50,50], spacing 0.1. Refine zeros via Newton-Raphson/Muller. Verify |zeta(s_0)| < 1e-10. Repeat at 3+ truncation levels (5,7,10 sectors).
**Input**: D_K eigenvalues at tau=0.19, canonical_constants.py
**Output**: s61_zeta_zeros.py, s61_zeta_zeros.npz, s61_zeta_zeros.png
**Gate**: ZETA-ZEROS-61. PASS if >80% zeros within |Re(s)-4| < 0.5 AND fraction increases with truncation. FAIL if scatter uniformly. INFO if cluster near sigma_0 != 4.
**Depends On**: none

---

### CONNES-2: Level Spacing Statistics at the Fold
**Agent**: connes-ncg-theorist | **Priority**: MED | **Cost**: minutes CPU
**Computation**: P(s) of D_K eigenvalues after unfolding. Compare GUE (Montgomery-Odlyzko), GOE (BDI), Poisson (integrable).
**Method**: Unfold via staircase N(lambda). Spacing ratios r_n. Histogram P(s). Fit Wigner surmises. Number variance Sigma^2(L), spectral rigidity Delta_3(L). Per-sector and combined.
**Input**: D_K eigenvalues at tau=0.19
**Output**: s61_level_spacing.py, s61_level_spacing.npz, s61_level_spacing.png
**Gate**: LEVEL-STATS-61. INFO (classification). Cross-ref: S38 CHAOS-1 found <r>=0.321.
**Depends On**: none

---

### CONNES-3: Functional Equation and J-Symmetry Constraints
**Agent**: connes-ncg-theorist | **Priority**: HIGH | **Cost**: minutes CPU
**Computation**: (a) Verify eta(s) vanishes identically (J-symmetry forces +lambda paired with -lambda). (b) Construct functional equation zeta(s) = C(s)*zeta(4-s). (c) Test Poincare duality constraints.
**Method**: (a) Evaluate eta(s) at 50+ complex s with Re(s)>4. (b) Compute ratio zeta(s)/zeta(4-s) at 100+ points. (c) Check C(s) matches Gamma form from Seeley 1967. (d) Intersection form on K_0(A_F)=Z^3.
**Input**: D_K eigenvalues all sectors, canonical_constants.py
**Output**: s61_functional_eq.py, s61_functional_eq.npz, s61_functional_eq.png
**Gate**: FUNC-EQ-61. PASS if |eta(s)| < 1e-12 everywhere AND functional eq holds. FAIL if functional eq breaks. INFO if non-standard C(s).
**Depends On**: none

---

### CONNES-4: Heat Kernel Trace Formula — Geometric Side
**Agent**: connes-ncg-theorist | **Priority**: MED | **Cost**: Hours CPU
**Computation**: Compute geometric side of trace formula for D_K on Jensen-deformed SU(3). Involves conjugacy class integrals. Yields "geometric primes" (closed geodesics).
**Method**: Parametrize conjugacy classes via maximal torus T^2. Weyl integration formula. For Jensen metric, compute modified volume factor. Evaluate K(t,g,g) per class. Compare spectral side vs geometric side at tau=0 (verification) and tau=0.19.
**Input**: Jensen metric, PW eigenvalues, SU(3) root system and Weyl group
**Output**: s61_trace_formula_geometric.py, s61_trace_formula_geometric.npz, s61_trace_formula_geometric.png
**Gate**: TRACE-FORMULA-61. PASS if spectral=geometric within 1% at tau=0 AND computable at fold. FAIL if >5% at tau=0. INFO if <50 primitive geodesics.
**Depends On**: none

---

## Wave 3 — ALPHA + TRANSIT + CC + ZETA-DEPENDENT (20 entries)

### PHONON-2: Physical Alpha Parameter on Jensen Metric
**Agent**: phonon-first-cosmologist | **Priority**: HIGH | **Cost**: minutes
**Computation**: Determine alpha = f_2*Lambda^2/f_0. HESSIAN-3D-60 found alpha_crit=55. Zero-parameter test: if alpha<55, fold is stable a_4 minimum.
**Method**: For each cutoff — heat kernel f=e^{-x} (f_0=1,f_2=1); sharp (f_0=1,f_2=1/2); Gaussian; erfc(x-1); Chamseddine-Connes optimal — compute alpha at Lambda in {M_KK, 10*M_KK, M_Pl}. Check positivity/unitarity/ghost-freedom. Hausdorff moment tractability in a_4 regime.
**Input**: computations/s60_hessian_3d.npz, canonical_constants.py, W1 a_2 output
**Output**: s61_alpha_physical.py, s61_alpha_physical.npz, s61_alpha_physical.png
**Gate**: ALPHA-REGIME-61. PASS if alpha < 55 for any standard cutoff at Lambda<=M_KK. FAIL if >55 for ALL. INFO if within factor 2.
**Depends On**: USER-2

---

### SP-5: Alpha_crit = 55 Conformal Selection Rule
**Agent**: schwarzschild-penrose-geometer | **Priority**: MED | **Cost**: <5 min CPU
**Computation**: Why 55? Decompose Riemann tensor at fold into Weyl, traceless Ricci, scalar. Express a_2, a_4 in Penrose-Rindler components. Identify geometric origin of alpha_crit.
**Method**: (1) Penrose-Rindler decomposition at fold. (2) Express a_2, a_4 in 8D Gilkey coefficients. (3) Ratio a_4/a_2 as function of tau. (4) Check 8D conformal anomaly.
**Input**: computations/s60_hessian_3d.npz, canonical_constants.py
**Output**: s61_alpha_crit_conformal.py, s61_alpha_crit_conformal.npz, s61_alpha_crit_conformal.png
**Gate**: ALPHA-CRIT-CONFORMAL-61. PASS if conformal invariance origin. FAIL if accidental. INFO if known geometric ratio.
**Depends On**: USER-2

---

### BAP-6: Proper Heat Kernel Ratio a_4/a_2 for Higgs Mass
**Agent**: baptista-spacetime-analyst | **Priority**: MED | **Cost**: Moderate
**Computation**: Compute true a_4^Gilkey/a_2^Gilkey from local curvature integrals. A4-TRACE-60 found truncated PW ratio 1.823 (35% Higgs mass shift).
**Method**: Extend SP-1 method to a_4 (R^2, R_{mu nu}R^{mu nu}, R_{mu nu rho sigma}R^{mu nu rho sigma}, nabla^2 R from Paper 15 eq 3.70). Integrate over SU(3). Compare to 1.823.
**Input**: computations/s60_a4_trace.npz, USER-2 output, Paper 15 curvature tensors, canonical_constants.py
**Output**: s61_heat_kernel_a4.py, s61_heat_kernel_a4.npz
**Gate**: HK-RATIO-61. PASS if PW ratio confirmed within 10%. FAIL if >50% off. INFO if 10-50%.
**Depends On**: USER-2

---

### VDD-6 / USER-3: Transit Spectral Action from Families of Spectral Triples
**Agent**: van-den-dungen-bridge-theorist | **Priority**: CRITICAL | **Cost**: ~30 min GPU
**Computation**: SA ALONG transit path using Paper 02's Product Spectral Triple Theorem. D_transit = d/dtau ⊗ 1 + 1 ⊗ D_K(tau). The S38 paradigm shift computation.
**Method**: (1) Tr(f(D_K(tau)^2/Lambda^2)) at 50 tau points. (2) Integrate over tau. (3) Compute d/dtau corrections from eigenvalue derivatives. (4) Total transit SA vs static SA.
**Input**: D_K(tau) eigenvalues at 50 tau points, HAWK-9 output (da_2/dtau), canonical_constants.py
**Output**: s61_transit_spectral_action.py, s61_transit_spectral_action.npz, s61_transit_spectral_action.png
**Gate**: TRANSIT-SA-61. PASS if transit differs from static by >10%. FAIL if <1%. INFO if 1-10%.
**Depends On**: USER-2, HAWK-9

---

### VDD-4: Spectral Flow of D_K(tau)
**Agent**: van-den-dungen-bridge-theorist | **Priority**: HIGH | **Cost**: ~20 min CPU
**Computation**: Compute sf(D_K(tau)) from tau=0 to tau_fold=0.19. INTEGER by APS index theorem. Compare S_inst=0.069. Callias: sf depends ONLY on endpoints.
**Method**: Track each eigenvalue vs tau, count zero-crossings (+1 up, -1 down). Verify endpoint dependence.
**Input**: D_K eigenvalue data at dense tau sampling (existing PW data), canonical_constants.py
**Output**: s61_spectral_flow.py, s61_spectral_flow.npz, s61_spectral_flow.png
**Gate**: SPECTRAL-FLOW-61. PASS if sf=0 (WKB interpretation). FAIL if sf!=0, contradicts S38. INFO if sf!=0 but compatible.
**Depends On**: none

---

### HAWK-4: Back-Reaction Corrected Parker Spectrum
**Agent**: hawking-theorist | **Priority**: MED | **Cost**: ~2 hr GPU
**Computation**: Self-consistent BdG with back-reaction. n_k(tau) feeds into V_eff(tau). S38: n_Bog=0.999 with 3.7% back-reaction.
**Method**: (1) BdG H(tau) with eigenvalues from D_K(tau). (2) Bogoliubov coefficients at each tau. (3) E_br = sum omega_k|beta_k|^2. (4) Modify transit velocity. (5) Iterate to convergence.
**Input**: computations/s59_bogoliubov_coeff.npz, computations/s60_transplanckian_bogo.npz, canonical_constants.py
**Output**: s61_backreaction_parker.py, s61_backreaction_parker.npz, s61_backreaction_parker.png
**Gate**: BACKREACTION-PARKER-61. PASS if n_Bog^{sc} in [0.95,1.00]. FAIL if <0.5. INFO if [0.5,0.95].
**Depends On**: none

---

### HAWK-5: GSL-Timescape Jensen Convexity
**Agent**: hawking-theorist | **Priority**: MED | **Cost**: ~30 min CPU
**Computation**: Verify convexity of S_spec(tau) guarantees Delta_S_gen > 0 under spatial inhomogeneity via Jensen's inequality.
**Method**: d^2(S_spec)/d(tau)^2 at 100 tau points. Jensen bound for delta_tau/tau = {0.01, 0.1, 0.5}. Verify S_gen monotone.
**Input**: D_K eigenvalues at 100 tau points, canonical_constants.py
**Output**: s61_gsl_timescape_jensen.py, s61_gsl_timescape_jensen.npz, s61_gsl_timescape_jensen.png
**Gate**: GSL-TIMESCAPE-61. PASS if convexity holds and Jensen bound positive. FAIL if non-convex. INFO if marginal.
**Depends On**: none

---

### TESLA-3: Dynamic J-Symmetry Breaking During Transit
**Agent**: tesla-resonance | **Priority**: HIGH | **Cost**: ~minutes CPU
**Computation**: Test [J, D_K(tau(t))] for nonzero time-dependent component during transit. Static [J,D_K]=0 proven. Does the quench introduce Berry phase terms?
**Method**: (1) D_K eigenvectors at 50 tau points. (2) Berry connection A_tau = <psi_n|d/dtau|psi_m>. (3) [J, A_tau]. (4) If nonzero, H_eff = D_K + i*tau_dot*A_tau breaks J. CP-violating amplitude ~ tau_dot*||[J,A_tau]||.
**Input**: D_K(tau) eigenvalue solver, J operator, canonical_constants.py
**Output**: s61_dynamic_j_breaking.py, s61_dynamic_j_breaking.npz, s61_dynamic_j_breaking.png
**Gate**: J-DYNAMIC-61. PASS if max ||[J,A_tau]|| > 0.01. FAIL if = 0 to machine precision. INFO if nonzero but <0.01.
**Depends On**: none

---

### VOL-7: J-Breaking Mechanism Catalog for Baryogenesis
**Agent**: volovik-superfluid-universe-theorist | **Priority**: MED | **Cost**: minutes
**Computation**: Catalog all mechanisms that could break [J,D_K]=0: (E1) UV completion, (E2) twisted spectral triple, (E3) cosmological CPT violation during transit (Berry phase), (E4) gravitational CP anomaly. Quantitative eta_B estimates for each.
**Method**: For E3: compute [J,D_K(tau(t))] during quench. For E2: evaluate twisted order-one condition. For each: epsilon_1, eta_B estimate.
**Input**: D_K(tau) eigenvalues/vectors at 50 tau, J operator, canonical_constants.py
**Output**: s61_j_breaking_catalog.py, s61_j_breaking_catalog.npz, s61_j_breaking_catalog.md
**Gate**: J-BREAKING-CATALOG-61. PASS if any eta_B within 3 OOM of 6e-10. FAIL if all <10^{-20}. INFO otherwise.
**Depends On**: none

---

### PHONON-9: Twisted Spectral Triple for CP Violation
**Agent**: phonon-first-cosmologist | **Priority**: LOW | **Cost**: Hours
**Computation**: Does Jensen deformation generate a twist sigma with nonzero eta? NCG escape from J-wall.
**Method**: (1) Check a->a(tau) defines twist with [D,a]_sigma bounded. (2) sigma-twisted J-reality. (3) T^2 under twist. (4) If T^2 != +1, compute eta.
**Input**: D_K(tau), J operator, algebra A
**Output**: s61_twisted_triple.py, s61_twisted_triple.npz
**Gate**: TWIST-CP-61. PASS if nonzero eta. FAIL if no twist or eta=0. INFO if exponentially small.
**Depends On**: none

---

### PHONON-8: BCS Phase Boundary vs Soliton Domain Wall
**Agent**: phonon-first-cosmologist | **Priority**: LOW | **Cost**: minutes
**Computation**: With fold=SA maximum, DW at tau_DW=0.1135 is NOT between minima. Classify: Lifshitz transition, topological Dirac transition, or A-B interface analog?
**Method**: (1) BCS Delta(tau) discontinuity check. (2) D_K zero crossings through tau_DW. (3) Pfaffian Z_2 on both sides. (4) Compare to 3He A-B interface.
**Input**: D_K eigenvalues at 50+ tau bracketing tau_DW, BCS Delta(tau), S35 Pfaffian data
**Output**: s61_dw_classification.py, s61_dw_classification.npz, s61_dw_classification.png
**Gate**: DW-CLASS-61. PASS if cleanly classifiable. FAIL if no transition. INFO if ambiguous.
**Depends On**: none

---

### LANDAU-1: Ginzburg-Landau Free Energy for CC Staircase
**Agent**: landau-condensed-matter-theorist | **Priority**: HIGH | **Cost**: ~30 min CPU
**Computation**: Fit E_GS(N)={0,-0.046,+0.268,+0.875,+1.850} to Landau polynomial F(n)=F_0+a*n+b*n^2+c*n^3 in pair density n=N/8. Extract n_eq, chi_q, CC gap. Repeat at 10 tau values.
**Method**: Polynomial regression at each tau. ED of 8-mode BCS at each tau for E_GS(N). chi_q from curvature of F(n). Sector independence test. chi_q(tau) scan at 20 steps.
**Input**: computations/s60_staircase_ext.npz, canonical_constants.py
**Output**: s61_gl_staircase.py, s61_gl_staircase.npz, s61_gl_staircase.png
**Gate**: GL-STAIRCASE-61. PASS if chi_q minimum < 0.1. FAIL if >0.5 everywhere. INFO if [0.1,0.5].
**Depends On**: none

---

### VOL-8: Multi-Pair Q-Theory at Finite N
**Agent**: volovik-superfluid-universe-theorist | **Priority**: HIGH | **Cost**: minutes
**Computation**: Extend staircase to N=5,6,7,8. Does Lambda_residual oscillation amplitude decrease (3He thermodynamic limit) or stay O(1) (discrete q-theory locked)?
**Method**: ED of 8-mode BCS at N=1..8. Extract E_GS(N), Lambda_residual(N). Quadratic interpolation for N_eq. Fit oscillation envelope.
**Input**: canonical_constants.py, computations/s60_staircase_ext.npz
**Output**: s61_multi_pair_qtheory.py, s61_multi_pair_qtheory.npz, s61_multi_pair_qtheory.png
**Gate**: MULTI-PAIR-QTHEORY-61. PASS if amplitude decays as 1/N. FAIL if O(1) at N=8. INFO if non-monotone.
**Depends On**: none

---

### NAZ-2: Bayesian CC Model Comparison
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Low
**Computation**: Bayes factor comparison of surviving CC mechanisms: (a) q-theory, (b) heat kernel a_0, (c) a_4-dominated alpha<55.
**Method**: Define priors. Compute marginal likelihoods from 60 sessions of gate verdicts. Report Bayes factors.
**Input**: knowledge-index.json gate verdicts, computations/s60_hessian_3d.npz, computations/s60_bayesian_h0.npz
**Output**: s61_cc_bayes_comparison.py, s61_cc_bayes_comparison.npz
**Gate**: CC-BAYES-MODEL-61. INFO. Upgrade to PASS if B>10 for one model.
**Depends On**: none

---

### PHONON-12: Nuclear Odd-Even Staggering in CC Staircase
**Agent**: phonon-first-cosmologist | **Priority**: LOW | **Cost**: seconds
**Computation**: Delta^{(3)}(N) = (-1)^N*[E(N+1)-2E(N)+E(N-1)]/2 from staircase. Classifies BCS-BEC crossover.
**Input**: computations/s60_staircase_ext.npz
**Output**: s61_oddeven_stagger.py, s61_oddeven_stagger.npz, s61_oddeven_stagger.png
**Gate**: ODDEVEN-61. INFO (diagnostic).
**Depends On**: none

---

### BAP-2: Off-Jensen Screening Ratio on 2D Volume-Preserving Surface
**Agent**: baptista-spacetime-analyst | **Priority**: HIGH | **Cost**: Moderate
**Computation**: R_screen on 2D volume-preserving surface. Jensen line gives 16.1. Any off-Jensen direction with R_screen > 10^4 enables timescape-viable decoupling.
**Method**: General 3-parameter left-invariant metric, volume-preserving constraint. At each point compute da_2/d(lambda_i) and d(alpha)/d(lambda_i). Scan 100x100 grid. Reuse s60_hessian_3d.npz.
**Input**: computations/s60_hessian_3d.npz, computations/s60_sector_dim_reduct.npz, canonical_constants.py
**Output**: s61_offjensen_screening.py, s61_offjensen_screening.npz, s61_offjensen_screening.png
**Gate**: OFFJ-SCREEN-61. PASS if max R_screen > 10^4. FAIL if <100. INFO if [100, 10^4].
**Depends On**: none

---

### BAP-4: Lichnerowicz Gap vs Sectional Curvature at Domain Wall
**Agent**: baptista-spacetime-analyst | **Priority**: MED | **Cost**: Low
**Computation**: Near-coincidence (Delta_tau=0.0025) between Lichnerowicz gap minimum and DW. Refine grid, track relationship.
**Method**: Refine tau grid to 0.0001 (200 points in [0.10,0.12]). Track all 31 TT eigenvalues and K_sec^min simultaneously. Test monotonic relationship.
**Input**: computations/s60_lichnerowicz_dw.npz, Paper 13 curvature formulas
**Output**: s61_lichnerowicz_kmin.py, s61_lichnerowicz_kmin.npz, s61_lichnerowicz_kmin.png
**Gate**: LICH-KSEC-61. PASS if coincidence <0.001. FAIL if >0.01. INFO if [0.001,0.01].
**Depends On**: none

---

### CONNES-6: Weil Positivity Test
**Agent**: connes-ncg-theorist | **Priority**: MED | **Cost**: minutes after CONNES-1
**Computation**: Test Weil positivity Tr(f*f-tilde) >= 0. GRH for zeta_{D_K} equivalent to this.
**Method**: (1) Weil distribution from spectral zeta zeros. (2) Evaluate W(f) for Hermite functions. (3) Minimize over test functions.
**Input**: CONNES-1 zeros, Hermite functions (order up to 50)
**Output**: s61_weil_positivity.py, s61_weil_positivity.npz, s61_weil_positivity.png
**Gate**: WEIL-POS-61. PASS if min W(f) >= 0. FAIL if <0. INFO if margin <1%.
**Depends On**: CONNES-1

---

### CONNES-7: Spectral Zeta Residues vs Physical Constants
**Agent**: connes-ncg-theorist | **Priority**: MED | **Cost**: minutes
**Computation**: Residues at s=4,3,2 yield a_0,a_2,a_4. Verify positive G_N, correct couplings, bounded Higgs potential.
**Method**: Res_{s=k} via lim (s-k)*zeta(s). Convert to physical constants via CCM dictionary. Compare a_2 to USER-2.
**Input**: D_K^2 eigenvalues at fold, canonical_constants.py, USER-2 output
**Output**: s61_zeta_residues.py, s61_zeta_residues.npz
**Gate**: ZETA-RESIDUES-61. PASS if a_2 matches within 5% AND G_N>0. FAIL if >20%. INFO if couplings off.
**Depends On**: USER-2, CONNES-3

---

### CONNES-8: Connes Distance Between Spectral Projections
**Agent**: connes-ncg-theorist | **Priority**: LOW | **Cost**: Hours
**Computation**: d(P_m,P_n) = sup{|phi_m(a)-phi_n(a)| : ||[D,a]||<=1} for first 50 pairs. Test correlation with zeta zeros.
**Method**: SDP via CLARABEL (0.16s/pair). Compare to eigenvalue gaps and zeta-zero oscillations.
**Input**: D_K eigenvalues/vectors at tau=0.19, A_F generators, CONNES-1 zeros
**Output**: s61_connes_distance_projections.py, s61_connes_distance_projections.npz, s61_connes_distance_projections.png
**Gate**: CONNES-DIST-PROJ-61. INFO (monotone vs non-monotone in eigenvalue gap).
**Depends On**: CONNES-1

---

## Wave 4 — SIGNATURES + DEEP THEORY (16 entries)

### NAZ-14: Yukawa Couplings from D_F
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: HIGH | **Cost**: Moderate
**Computation**: Construct D_F from L-homomorphism failure on framework's SU(3). Extract Y_u, Y_d, Y_e, Y_nu. Compare mass ratios.
**Method**: LEFT action L_{su(3)} on Psi_+ for C^2 coset at tau_fold. L-failure terms define D_F. Extract 3x3 Yukawa matrices. Diagonalize for masses and mixing.
**Input**: S16 L-action matrices, Jensen metric at tau_fold, canonical_constants.py
**Output**: s61_yukawa_first_principles.py, s61_yukawa_first_principles.npz
**Gate**: YUKAWA-FIRST-PRINCIPLES-61. PASS if any mass ratio within 30%. FAIL if all off by >OOM. INFO if structure correct but needs RG.
**Depends On**: none

---

### QA-1: Van Hove Dispersion — Tau-Resolved B2 Spectrum
**Agent**: quantum-acoustics-theorist | **Priority**: HIGH | **Cost**: ~10 min GPU
**Computation**: Full dispersion omega(k,tau) for B2. Extract group velocity, effective mass, DOS at van Hove energy.
**Method**: Diag D_K(tau) at 50 tau, project B2, numerical derivatives vs CG(24) wavevector k.
**Input**: canonical_constants.py, D_K solver, B2 sector projection
**Output**: s61_vanhove_dispersion.py, s61_vanhove_dispersion.npz, s61_vanhove_dispersion.png
**Gate**: VANHOVE-DISP-61. PASS if dE/dtau=0 at VH for all tau. FAIL if >0.01. INFO if <0.01 but nonzero.
**Depends On**: none

---

### QA-4: Mode-Resolved Leggett Squeezing Spectrum
**Agent**: quantum-acoustics-theorist | **Priority**: HIGH | **Cost**: ~3 min CPU
**Computation**: |beta_L(k)|^2 for Leggett branch vs wavevector on CG(24). Is n(k) thermal or structured?
**Method**: For each k, solve BdG with tau-dependent omega_L(k,tau). r(k) = integral of d(omega_L)/dtau/(2*omega_L). |beta|^2=sinh^2(r). Compare to Bose-Einstein.
**Input**: computations/s59_epsilon_canonical.npz, computations/s55_fabric_coupling.npz, CG(24) spectrum
**Output**: s61_leggett_squeezing_spectrum.py, s61_leggett_squeezing_spectrum.npz, s61_leggett_squeezing_spectrum.png
**Gate**: LEGGETT-SPECTRUM-61. PASS if non-thermal (chi^2/dof>3). FAIL if thermal. INFO if intermediate.
**Depends On**: none

---

### QA-5: B2 Flat Band Robustness Under Josephson Coupling
**Agent**: quantum-acoustics-theorist | **Priority**: HIGH | **Cost**: ~2 min CPU
**Computation**: B2 bandwidth in fabric for N_cells=2,4,8,16,24,32. Compare to sweep rate at van Hove.
**Method**: Tight-binding for B2 on CG(N) with J_L=epsilon*E_J. Diag. Extract bandwidth vs N.
**Input**: computations/s54_tb_hamiltonian.npz, computations/s59_epsilon_canonical.npz, computations/s55_fabric_coupling.npz
**Output**: s61_b2_fabric_bandwidth.py, s61_b2_fabric_bandwidth.npz, s61_b2_fabric_bandwidth.png
**Gate**: B2-FABRIC-61. PASS if W_fabric < d(omega)/dtau for all N. FAIL if >. INFO if marginal.
**Depends On**: none

---

### QA-3: Acoustic Metric — Unruh Form
**Agent**: quantum-acoustics-theorist | **Priority**: MED | **Cost**: ~5 min CPU
**Computation**: Construct Unruh-form acoustic metric from phonon dispersion. Compute R_acoustic, T_Parker. Test sonic horizon.
**Method**: From c_BA=0.399 and sweep rate, construct 1+1D acoustic metric. Christoffel symbols. Ricci scalar at 50 tau. Sonic horizon: v_sweep=c_BA.
**Input**: computations/s56_ba_spectrum.npz, computations/s57_bogoliubov.npz, canonical_constants.py
**Output**: s61_acoustic_metric.py, s61_acoustic_metric.npz, s61_acoustic_metric.png
**Gate**: ACOUSTIC-METRIC-61. PASS if T_Parker ~ T_squeeze within 3x. FAIL if >10x. INFO if no sonic horizon.
**Depends On**: none

---

### NAZ-4: Pair Transfer CMB Propagation
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Low-moderate
**Computation**: Propagate S_+(N) through chain delta_N -> delta_Delta -> delta_J -> delta_T to get delta_T/T.
**Input**: computations/s60_pair_transfer_n4.npz, S52 ED gaps, canonical_constants.py
**Output**: s61_pair_cmb.py, s61_pair_cmb.npz, s61_pair_cmb.png
**Gate**: PAIR-CMB-61. PASS if delta_T/T has structure in [10^{-6},10^{-4}]. FAIL if flat or outside [10^{-8},10^{-2}]. INFO if below Planck.
**Depends On**: none

---

### NAZ-11: Pair-Transfer Scaling on Larger Fabrics
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: High (8-cell may need truncation)
**Computation**: Does bosonic scaling S_+(N)=(N+1)(1-N/16)/2 survive at 4-cell and 8-cell?
**Method**: ED of 4-cell and 8-cell Josephson at N=1-4. Test scaling. Track mode uniformity.
**Input**: computations/s60_pair_transfer_n4.npz, 4/8-cell Hamiltonians, canonical_constants.py
**Output**: s61_pair_transfer_fabric.py, s61_pair_transfer_fabric.npz, s61_pair_transfer_fabric.png
**Gate**: PAIR-FABRIC-61. PASS if holds <10% at 8 cells. FAIL if suppressed below (N+1)/2. INFO if intermediate.
**Depends On**: none

---

### NAZ-8: Nuclear Pairing Chain Attenuation
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: HIGH | **Cost**: Low
**Computation**: Delta/E_F at each inheritance level: Level 0 (substrate), Level 3 (nuclear), Level 5 (3He-B). Systematic attenuation?
**Method**: Collect framework Delta from S35, nuclear Delta from Paper 02, 3He-B experimental ~10^{-3}. Ratios. Plot.
**Input**: S35 BCS data, S53 spectrum, Paper 02, 3He-B literature
**Output**: s61_pairing_chain.py, s61_pairing_chain.npz, s61_pairing_chain.png
**Gate**: PAIRING-CHAIN-61. INFO (monotonic decrease = inheritance support).
**Depends On**: none

---

### VOL-4: Dipolar Thermalization on Fabric
**Agent**: volovik-superfluid-universe-theorist | **Priority**: MED | **Cost**: minutes
**Computation**: Damping rate of Leggett mode (m_G=0.070) in Josephson fabric via Fermi golden rule.
**Input**: m_G, E_J=655, BCS spectrum, canonical_constants.py
**Output**: s61_dipolar_thermalization.py, s61_dipolar_thermalization.npz
**Gate**: DIPOLAR-THERM-61. INFO (Leggett lifetime characterization).
**Depends On**: none

---

### PHONON-6: a_4-Dominated Spectral Action with q-Theory Vacuum
**Agent**: phonon-first-cosmologist | **Priority**: HIGH | **Cost**: minutes
**Computation**: If alpha<55, fold IS stable, CC set by a_0 in INDEX regime. BCS provides departure from Lambda_eq=0 at Q=29.9.
**Method**: (1) a_0. (2) Lambda_eff = a_0*f_0/(a_4*f_4). (3) q-theory departure from s60_qtheory_geodesic.npz. (4) Lambda_residual. (5) Compare Lambda_obs.
**Input**: computations/s60_hessian_3d.npz, computations/s60_pw_h0_conv.npz, computations/s60_qtheory_geodesic.npz, computations/s60_staircase_ext.npz, PHONON-2 output, canonical_constants.py
**Output**: s61_a4_qtheory_compound.py, s61_a4_qtheory_compound.npz
**Gate**: A4-QT-COMPOUND-61. PASS if |Lambda_residual/Lambda_obs - 1| < 10. FAIL if >10^5. INFO if [10, 10^5].
**Depends On**: PHONON-2

---

### TESLA-5: Physical Debye Cutoff for PW Tower
**Agent**: tesla-resonance | **Priority**: MED | **Cost**: ~minutes
**Computation**: Maximum physical PW level L_max by Debye cutoff analogy. L_max from eigenvalue = Lambda.
**Method**: L_max = (Lambda/M_KK)^{8/9.14}. Map L_max(Lambda). Compute regularized traces vs L_max.
**Input**: PW eigenvalue data, alpha_{a_2}=9.14, canonical_constants.py
**Output**: s61_debye_cutoff_pw.py, s61_debye_cutoff_pw.npz, s61_debye_cutoff_pw.png
**Gate**: DEBYE-STABLE-61. PASS if converge within 5% at L_crit. FAIL if never converge. INFO if cutoff-dependent.
**Depends On**: PHONON-2

---

### VDD-3: Jensen Deformation as Locally Bounded Perturbation
**Agent**: van-den-dungen-bridge-theorist | **Priority**: HIGH | **Cost**: ~30 min CPU
**Computation**: Verify D_K(tau)-D_K(0) satisfies Paper 10 conditions: ||(D_K(tau)-D_K(0))*phi|| <= C*(||D_K(0)*phi||+||phi||). If so, [D_K(tau)]=[D_K(0)] in K-homology for all tau.
**Method**: (1) Express difference as 1st-order operator with tau-dependent coefficients. (2) Bound via compactness. (3) Find C(tau). (4) Numerical: |lambda_n(tau)-lambda_n(0)|/(|lambda_n(0)|+1) bounded uniformly.
**Input**: D_K eigenvalue data at multiple tau, canonical_constants.py
**Output**: s61_perturbation_bound.py, s61_perturbation_bound.npz
**Gate**: K-HOMOLOGY-STABILITY-61. PASS if C(tau) finite for all tau. FAIL if unbounded. INFO if C>100.
**Depends On**: none

---

### VDD-5: Order-One Condition vs Gauge Module Conditions
**Agent**: van-den-dungen-bridge-theorist | **Priority**: HIGH | **Cost**: ~1 hr CPU
**Computation**: D_K fails standard order-one at 4.000 for (H,H). Does it define a gauge module per Paper 05?
**Method**: (1) Paper 05 gauge module conditions. (2) Evaluate for A_F, H_F=C^16, D_K(tau). (3) Determine gauge group. (4) Compare to SM.
**Input**: A_F algebra (S6-10), D_K matrix in C^16, J_C matrix
**Output**: s61_gauge_module_check.py, s61_gauge_module_check.npz
**Gate**: GAUGE-MODULE-61. PASS if gauge module with SM group. FAIL if also fails. INFO if different group.
**Depends On**: none

---

### VDD-7: First Explicit Kasparov Product Verification
**Agent**: van-den-dungen-bridge-theorist | **Priority**: MED | **Cost**: ~2 hr CPU
**Computation**: FIRST computational verification of Kasparov factorization on non-trivial compact fiber. Jensen breaks bi-invariance while preserving U(2).
**Method**: (1) K-homology class [D_K] from spectral data. (2) Kasparov product [D_K]⊗[D_{M^4}]. (3) Compare direct [D_{M^4 x SU(3)}]. (4) Verify Paper 01 Main Theorem.
**Input**: Full PW dataset, D_{M^4} spectral data
**Output**: s61_kasparov_product_verification.py, s61_kasparov_product_verification.npz
**Gate**: KASPAROV-VERIFY-61. PASS if factorization holds. FAIL if violated. INFO if partial.
**Depends On**: VDD-2

---

### VDD-9: BdG Spectral Action
**Agent**: van-den-dungen-bridge-theorist | **Priority**: MED | **Cost**: ~1 hr GPU
**Computation**: a_n(D_K^{BdG}) for BdG Dirac operator. FIRST NCG spectral action on BCS system. Compare to a_n(D_K).
**Method**: (1) Construct D_K^{BdG} from D_K + pairing in B2. (2) Diag. (3) Gilkey a_0,a_2,a_4. (4) delta_a_n = condensate back-reaction.
**Input**: D_K eigenvalues, BCS pairing from S34 (E_cond=-0.137), BdG from S34
**Output**: s61_bdg_spectral_action.py, s61_bdg_spectral_action.npz
**Gate**: BDG-SA-61. PASS if delta_a_2/a_2 < 0.01. FAIL if >1. INFO if 0.01-1.
**Depends On**: USER-2

---

### VDD-10: Block-Diagonal Theorem Generality
**Agent**: van-den-dungen-bridge-theorist | **Priority**: MED | **Cost**: ~2 hr CPU
**Computation**: Is exact block-diagonality (S22b, 8.4e-15) from left-invariance alone, or SU(3)-specific?
**Method**: (1) General proof attempt for left-invariant metrics. (2) Test on SU(2) Berger sphere. (3) Identify minimal algebraic condition.
**Input**: D_K block-diagonal data, su(3) and su(2) structure constants
**Output**: s61_block_diagonal_generality.py, s61_block_diagonal_generality.md
**Gate**: BLOCK-DIAG-GENERAL-61. PASS if left-invariance suffices. FAIL if SU(3)-specific. INFO if semisimple only.
**Depends On**: none

---

## Wave 5 — EXTENSIONS + DEPENDENT + SPECULATIVE (29 entries)

### NAZ-18: Cosmological Transit Baryogenesis Estimate
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Moderate
**Computation**: Transit provides T-breaking for baryogenesis. Compute effective epsilon_CP from transit dynamics via ATDHFB-style computation.
**Method**: Time-dependent D_K(tau(t)) pair-creation/annihilation amplitudes. Interference generates CP violation. Asymmetry between forward/backward pair amplitudes.
**Input**: D_K(tau) eigenvalues at 50 tau points, S57 transit rate, canonical_constants.py
**Output**: s61_transit_baryogenesis.py, s61_transit_baryogenesis.npz
**Gate**: TRANSIT-BARYOGEN-61. PASS if eta_B within 3 OOM of 6e-10. FAIL if <10^{-20}. INFO if [10^{-20}, 10^{-7}].
**Depends On**: VDD-6

---

### NAZ-15: Higgs Mass from Sector-Resolved Spectral Action
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Low
**Computation**: m_H from spectral action with PW sector correction sqrt(N_{a_4}/N_{a_2})=1.35.
**Method**: m_H^2 = 2*lambda*v^2 with lambda from a_4/a_2. Include sector correction. Apply CCM formula.
**Input**: computations/s60_a4_trace.npz, USER-2 a_2/a_4, NAZ-14 Yukawas
**Output**: s61_higgs_mass.py, s61_higgs_mass.npz
**Gate**: HIGGS-MASS-61. PASS if m_H in [110,140]. FAIL if outside [80,200]. INFO if [80,200]\[110,140].
**Depends On**: USER-2, NAZ-14

---

### VDD-12: Jensen Moduli Space Completeness (36D Hessian)
**Agent**: van-den-dungen-bridge-theorist | **Priority**: MED | **Cost**: ~4 hr GPU
**Computation**: HESSIAN-3D-60 found fold is maximum in 3D subspace. Full moduli is 36D. Is fold maximum in ALL directions?
**Method**: (1) Parametrize 36D left-invariant metrics on su(3). (2) NCG constraints (KO-dim 6, J^2=+1, volume). (3) Restricted Hessian at fold. (4) Index.
**Input**: Jensen metric at fold, su(3) structure constants, computations/s60_hessian_3d.npz
**Output**: s61_moduli_hessian.py, s61_moduli_hessian.npz
**Gate**: MODULI-HESS-61. PASS if all eigenvalues <=0. FAIL if saddle. INFO if flat directions.
**Depends On**: VDD-3

---

### QA-6: Multimode Covariance of Squeezed Leggett Modes
**Agent**: quantum-acoustics-theorist | **Priority**: MED | **Cost**: ~10 min CPU
**Computation**: Covariance C_{ij} for Leggett modes at different k after transit. Mandel Q parameter.
**Method**: Evolve multimode squeezed state. Common driver introduces correlations. Full covariance from multimode Bogoliubov.
**Input**: QA-4 output, CG(24) Laplacian, omega_L(k,tau)
**Output**: s61_multimode_covariance.py, s61_multimode_covariance.npz, s61_multimode_covariance.png
**Gate**: MULTIMODE-COV-61. PASS if Q>0.1. FAIL if |Q|<0.01. INFO if [0.01,0.1].
**Depends On**: QA-4

### VDD-8: Shriek Map vs Baptista Fiber Integration
**Agent**: van-den-dungen-bridge-theorist | **Priority**: MED | **Cost**: ~1 hr
**Computation**: Verify pi_! (K-theoretic pushforward) = Baptista fiber integration (Paper 13 eq 3.41).
**Input**: D_K spectral data, vol_{g_K(tau)}, Paper 13 eq 3.41
**Output**: s61_shriek_vs_fiberint.py, s61_shriek_vs_fiberint.npz
**Gate**: SHRIEK-EQUIV-61. PASS if equal. FAIL if differ. INFO if index but not K-homology.
**Depends On**: VDD-7

---

### VDD-13: Paper 05 Topological Corrections
**Agent**: van-den-dungen-bridge-theorist | **Priority**: LOW | **Cost**: ~1 hr
**Computation**: Chern classes, instanton numbers from non-trivial bundle. Relate to S_inst=0.069.
**Gate**: CHERN-INST-61. PASS if ind=integer, relates to S_inst. FAIL if contradicts. INFO if ind=0.
**Depends On**: VDD-2, VDD-4

---

### VDD-14: Fredholm Complex for BdG System
**Agent**: van-den-dungen-bridge-theorist | **Priority**: LOW | **Cost**: ~2 hr
**Computation**: Paper 14 generalized Fredholm theory on BdG 2-term complex. K_0 index vs Z_2 Pfaffian.
**Gate**: FREDHOLM-BDG-61. PASS if K_0 non-trivial. FAIL if trivial. INFO if unexpected.
**Depends On**: VDD-9

---

### VDD-16: Ruelle Zeta Function and Arithmetic Content
**Agent**: van-den-dungen-bridge-theorist | **Priority**: LOW | **Cost**: ~4 hr
**Computation**: Ruelle zeta of geodesic flow on (SU(3),g_K). Euler product over primitive geodesics? Compare zeros to spectral zeta.
**Gate**: RUELLE-ARITH-61. PASS if zeros correlated (p<0.01). FAIL if not. INFO if marginal.
**Depends On**: USER-2

---

### VDD-17: Pseudo-Riemannian Extension to Lorentzian
**Agent**: van-den-dungen-bridge-theorist | **Priority**: LOW | **Cost**: ~2 hr
**Computation**: Lorentzian spectral triple on M^{3,1}xSU(3). Krein space. Physical SA = difference of Euclidean SAs.
**Gate**: LORENTZ-SA-61. PASS if within 10% of Euclidean. FAIL if >50%. INFO if 10-50%.
**Depends On**: USER-2, VDD-6

---

### VDD-18: Inheritance Kasparov Product at Each Compositing Level
**Agent**: van-den-dungen-bridge-theorist | **Priority**: LOW | **Cost**: ~4 hr
**Computation**: Track K-theoretic invariants through compositing chain. Classify 22 correspondences.
**Gate**: INHERIT-CLASSIFY-61. PASS if >=15/22 inherited/universal. FAIL if >=10/22 coincidental. INFO if unexpected.
**Depends On**: VDD-7, VDD-8

---

### NAZ-6: SD-Shell Benchmark Comparison
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: HIGH | **Cost**: Moderate
**Computation**: RG exact pairing for nuclear sd-shell at N=1-3. Compare 5 observables to framework.
**Input**: Paper 15 RG eqs, Paper 07 sd-shell energies, S52-S60 data
**Output**: s61_sdshell_benchmark.py, s61_sdshell_benchmark.npz
**Gate**: SD-SHELL-BENCH-61. INFO (calibration).
**Depends On**: none

---

### NAZ-7: PBCS Correction Scaling with Fabric Size
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Moderate
**Computation**: PBCS correction for 2-cell at N=1 vs single-cell (S52: +0.97%).
**Gate**: PBCS-FABRIC-61. PASS if ratio decreases. FAIL if increases. INFO if <10% change.
**Depends On**: none

---

### NAZ-9: Seniority Quantum Numbers on the Fabric
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Low-moderate
**Computation**: Seniority purity of 2-cell Josephson eigenstates. High=integrability survives, low=thermalization.
**Gate**: SENIORITY-FABRIC-61. INFO.
**Depends On**: none

---

### NAZ-10: Pair-Transfer EWSR (Thouless Identity)
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Low
**Computation**: Verify m_1 = (1/2)<[S_+,[H,S_-]]> matches explicit sum.
**Gate**: GPV-EWSR-61. PASS if within 5%. FAIL if >20%. INFO if 5-20%.
**Depends On**: none

---

### NAZ-13: BDI to DIII Transition Through Compositing
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: LOW | **Cost**: Low
**Computation**: Trace T^2 through inheritance chain. Is 3He the UNIQUE path to DIII?
**Gate**: BDI-DIII-CHAIN-61. INFO.
**Depends On**: none

---

### NAZ-16: Heat Kernel Mode-Resolved Oscillations
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: MED | **Cost**: Moderate
**Computation**: Do regularized CC oscillatory corrections survive? Smooth part (Seeley-DeWitt) vs oscillatory residual.
**Gate**: HK-OSCILLATION-61. PASS if residual ~ Lambda_obs. FAIL if ->0. INFO if finite but >> Lambda_obs.
**Depends On**: USER-2

---

### NAZ-17: Bayesian Inheritance vs Analogy Discrimination
**Agent**: nazarewicz-nuclear-structure-theorist | **Priority**: LOW | **Cost**: Low
**Computation**: Bayes factor M_inherit vs M_analogy using condensate ranking.
**Gate**: INHERIT-BAYES-61. INFO (expected indeterminate).
**Depends On**: none

---

### LANDAU-3: BCS-BEC Crossover Diagnostic
**Agent**: landau-condensed-matter-theorist | **Priority**: MED | **Cost**: ~20 min CPU
**Computation**: 1/(k_F*a_s) from pair wavefunction. Condensate fraction n_0/N. Place on BCS-BEC phase diagram at each N.
**Gate**: BCS-BEC-61. PASS if N=1 BEC, N=4 crossover. FAIL if all same. INFO if unexpected N.
**Depends On**: none

---

### LANDAU-10: Landau Damping Threshold for Leggett Mode
**Agent**: landau-condensed-matter-theorist | **Priority**: LOW | **Cost**: ~10 min CPU
**Computation**: Compare omega_L to 2*Delta at N=1,2,3,4. Gap-protected or Landau damped?
**Gate**: LEGGETT-DAMPING-61. PASS if omega_L < 2*Delta at N=1,2. FAIL if > at N=1. INFO if crossing at N=3,4.
**Depends On**: none

---

### HAWK-6: (0,0) Sector Bekenstein Saturation — Physical Radius
**Agent**: hawking-theorist | **Priority**: LOW | **Cost**: ~20 min CPU
**Computation**: Correct Bekenstein bound using proper confinement radius (d_J, R_rms, R_IPR) instead of 1/M_KK.
**Gate**: BEKENSTEIN-RADIUS-61. PASS if corrected ratio <1. FAIL if >1 with correct R. INFO if [0.8,1.2].
**Depends On**: none

---

### HAWK-7: Volovik-Sakharov G_eff for Island Formula
**Agent**: hawking-theorist | **Priority**: LOW | **Cost**: ~20 min CPU
**Computation**: G_eff from trace-log formula. Does it rescue island mechanism?
**Gate**: VS-GEFF-ISLAND-61. PASS if G_VS ~ G_SDW and Area/Bulk >>1. FAIL if 6+ OOM larger. INFO if 2-5 OOM.
**Depends On**: USER-2

---

### HAWK-8: Extremal GGE Quantum Stability
**Agent**: hawking-theorist | **Priority**: LOW | **Cost**: ~30 min CPU
**Computation**: Stability of marginal GGE (lambda_min=0) after superradiance spindown. Phase transition?
**Gate**: EXTREMAL-GGE-61. PASS if chi finite. FAIL if chi diverges. INFO if fluctuations large but chi finite.
**Depends On**: none

---

### SP-4: Penrose Inequality Analog for BCS Sector
**Agent**: schwarzschild-penrose-geometer | **Priority**: MED | **Cost**: <1 min CPU
**Computation**: E_BCS >= C*sqrt(S_BCS). Test (0,0) saturation = extremality.
**Gate**: PENROSE-INEQ-BCS-61. PASS if (0,0) saturates <5%. FAIL if violates >2x. INFO if holds without saturation.
**Depends On**: USER-2

---

### SP-6: Post-Superradiance = Dump Point
**Agent**: schwarzschild-penrose-geometer | **Priority**: LOW | **Cost**: <1 min CPU
**Computation**: Terminal state of Penrose analog = dump point? Compare kappa, BPS, GGE.
**Gate**: SUPERRAD-DUMP-61. PASS if match <5%. FAIL if >20%. INFO if partial.
**Depends On**: none

---

### VOL-6: Bekenstein Saturation via de Sitter Thermodynamics
**Agent**: volovik-superfluid-universe-theorist | **Priority**: LOW | **Cost**: seconds
**Computation**: S_dS = pi*R_H^2/G_eff. Compare to S_max and S_Bek. Apply first law of de Sitter.
**Gate**: BEKENSTEIN-HOLOGRAPHIC-61. INFO. PASS if S_dS/S_BCS = O(1). FAIL if >>1 or <<1.
**Depends On**: none

---

### VOL-9: Inheritance Chain CFL Correspondence Count
**Agent**: volovik-superfluid-universe-theorist | **Priority**: LOW | **Cost**: Literature evaluation
**Computation**: Evaluate 22-correspondence scorecard for CFL phase. Inheritance predicts >22; analogy predicts same.
**Output**: s61_cfl_correspondence.md
**Gate**: CFL-CORRESPONDENCE-61. INFO.
**Depends On**: none

---

### PHONON-4: Superfluid Weight from Quantum Metric
**Agent**: phonon-first-cosmologist | **Priority**: MED | **Cost**: minutes
**Computation**: D_s via Peotta-Torma. D_s = 2*E_J*S_+(1)/V_cell. Compare Meissner mass to Leggett mass.
**Gate**: MEISSNER-LEGGETT-61. PASS if D_s>0 AND m_M ~ omega_L within 20%. FAIL if D_s=0 or >100%. INFO if 20-100%.
**Depends On**: none

---

### PHONON-5: Spectral Dimension from Pair Return Probability
**Agent**: phonon-first-cosmologist | **Priority**: MED | **Cost**: minutes to hours
**Computation**: d_s(t) from P(t)=|<GS|e^{-iHt}|GS>|^2. Delta_N ~ N^{-1.84} implies z=3.68.
**Gate**: SPEC-DIM-PAIR-61. PASS if d_s(short)=2.0±0.2. FAIL if constant. INFO if flows but !=2.
**Depends On**: none

---

### BAP-8: Pati-Salam Spectral Action Regime at GUT Scale
**Agent**: baptista-spacetime-analyst | **Priority**: LOW | **Cost**: seconds
**Computation**: alpha at GUT unification scale in Pati-Salam model. Which side of 55?
**Gate**: PS-REGIME-61. INFO (classification).
**Depends On**: none

---

## Wave 6 — LOST TREASURES WORKSHOP (6 entries, workshop mode)

**Format**: 2-agent iterative workshop via `/rclab-review --type workshop`
**Purpose**: Investigate novel mathematical disciplines for potential subsumption into the framework. These are exploratory — too nebulous for pre-registered compute gates. The workshop identifies which (if any) deserve full agent buildout and compute-grade test cases for S62+.

**Agents**: 2 (selected at workshop time based on Wave 1-5 results — likely gen-physicist + one domain specialist)
**Rounds**: 2-3

### Topics for Workshop Investigation

1. **LT-1: Lattice Basis Reduction** — Can SVP on SU(3) weight lattice find a short vector giving epsilon < 0.001? (Cryptography/lattice reduction meets CC staircase)
2. **LT-2: Tropical Geometry** — Is the CC staircase a tropicalization of the spectral action? (Algebraic geometry meets NCG)
3. **LT-3: KAM Threshold** — Is delta_k=0.33 above or below the KAM threshold for the 8-mode BCS system? (Dynamical systems meets GGE survival)
4. **LT-4: Coding Theory** — Does the SU(3) weight lattice have error-correcting properties that constrain Lambda_residual? (Algebraic coding meets CC)
5. **LT-5: Combinatorial Number Theory** — Does the staircase partition function Z(q) = sum E_GS(N)*q^N have modular properties? (Analytic number theory meets BCS)
6. **LT-6: Signal Processing** — Is Lambda_residual the DC component of a filtered spectral action PSD? (Acoustic physics meets CC)

### Workshop Input Documents
- `sessions/archive/session-60/session-60-wayforward.md` (Lost Treasures section, lines 1399-1429)
- Wave 1-5 results (available at workshop time)
- `computations/s60_staircase_ext.npz` (E_GS data for LT-1, LT-5)
- D_K eigenvalue data (for LT-6)

### Workshop Output
- `sessions/archive/session-61/session-61-lost-treasures-workshop.md`
- Per-topic verdict: PURSUE (promote to S62 compute) / PARK (interesting but not actionable) / CLOSE (doesn't apply)
- For PURSUE topics: draft computation spec in wayforward format

---

## Decision Points

### After Wave 1
- **HEAT-KERNEL-A2-61 PASS** → Proceed to Wave 2 with confidence
- **HEAT-KERNEL-A2-61 FAIL** → ABORT. Redirect to a_2 diagnosis
- **SPIN-CURV-61 FAIL** → Recompute a_2 with full Gilkey formula
- **A-TENSOR-61 FAIL** → Fiber-base decomposition compromised. Critical.

### After Wave 2
- **GGE-THERM-61 majority PASS** → DM mechanism intact
- **GGE-THERM-61 majority FAIL** → DM mechanism dead. CRITICAL pivot.
- **ZETA-ZEROS-61 PASS** → Upgrade CONNES entries to HIGH
- **a_2 gauntlet agreement** → H_0 permanent
- **a_2 gauntlet disagreement** → Diagnose before Wave 3

### After Wave 3
- **ALPHA-REGIME-61 PASS** (alpha<55) → PHONON-6 highest-priority CC
- **ALPHA-REGIME-61 FAIL** (alpha>55) → Transit dynamics THE question
- **TRANSIT-SA-61 PASS** → S38 paradigm validated
- **J-DYNAMIC-61 PASS** → Baryogenesis channel opens

---

## Execution Notes

- **No TeamCreate** — all agents are independent Agent tool calls
- **Windows Bash bug**: output always 0kb — check for .npz/.png files
- **Script naming**: `computations/s61_{descriptive_name}.py`
- **Agents write ONLY to their designated working paper section**
- **Model**: ALL physics agents use opus
- **Total**: 90 compute entries across 5 waves (5+20+20+16+29) + 6 workshop topics in Wave 6
- **Realistic scope**: Waves 1-3 target S61 (HIGH/CRIT entries). Waves 4-5 may extend to S62+.
