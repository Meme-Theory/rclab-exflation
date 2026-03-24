# Session 46 Quicklook

**Date**: 2026-03-15
**Prior**: S45 -- Q-THEORY-BCS PASS (tau* = 0.209), ALPHA-EFF 0.410 (1.06x), d=3 KZ universality (n_s = -0.68 internal), 31 closures
**Format**: Parallel single-agent computations, 5 waves
**Plan**: `sessions/session-plan/session-46-plan.md`
**Master gates**: Q-THEORY-SELFCONSISTENT-46, HOSE-COUNT-46
**Wave count**: W1 (4), W2 (5), W3 (6), W4 (22 including V-B3B3-46 and addenda)
**Computations**: 37 attempted, 37 completed, 0 killed

---

## Executive Summary

Session 46 tested the S45 q-theory CC mechanism and the hose-count n_s mechanism to destruction. The self-consistent BCS gap kills the q-theory crossing at N=1 (Delta_B3 = 0.084 falls below the 0.13 threshold) but a crossing reappears at N=2 (tau* = 0.170). The direct V_B3B3 extraction from the Dirac spectrum (0.059, PASS 3.9x above threshold) reveals the B3 gap is entirely proximity-induced by the B2 condensate. The S45 alpha_eff = 0.410 is RETRACTED (entropy functional mismatch); the corrected range is 0.7--1.2 from Zubarev/Keldysh derivation. Every single-particle and collective-mode n_s route is closed: hose-count alpha is structurally ill-defined (pair transfer is a BLOCK property, R^2 = 0.002), spectral flow gives alpha = 4.03, Landau-Zener gives alpha = 8.13, the transfer function is flat at CMB scales (56-order separation), quasi-static inflation has three independent obstructions, and the forward/backward d_eff sweep fails at 244 sigma. Non-singlet dissipation narrows the velocity shortfall from 1,700x to 3.8x -- the tightest ever. Topologically, 13 pi Berry phases establish a Z_2 = -1 nontrivial skeleton that reconciles with zero Berry curvature (Zak phase, not Chern number). The Peter-Weyl censorship survives dissolution with only 2% degradation (sum-rule protected). All 279 scalar inner fluctuations are universally tachyonic at all tau -- reinterpreted as the transit mechanism (SU(3) analog of electroweak symmetry breaking). Pseudo-Riemannian SU(2,1) preserves KO-dim 6 with Killing signature (4,4). The S38 CHAOS-1 level spacing ratio is corrected from <r> = 0.321 to 0.439 (Poisson on unique levels).

---

## Wave-by-Wave Results

### WAVE 1 (4 tasks)

- **Q-THEORY-SELFCONSISTENT-46** = INFO; Q-THEORY-T3T5-46 = FAIL -- Self-consistent gap gives Delta_B3 = 0.084 (2.1x below FLATBAND 0.176), eliminating the Gibbs-Duhem crossing at N=1. Crossing requires Delta_B3 > 0.13. Coupling 26% from existence.
- **HOSE-COUNT-46** = INFO -- alpha_GPV = 0.72 +/- 0.52, alpha_raw = 1.81, neither hits 1.65 target. n_s = 0.04 (GPV) or 1.13 (raw). Only 5 k-values; R^2 = 0.38.
- **A2-GEOMETRIC-46** = INFO (structural) -- Spectral a_2 (2776.17) and geometric Seeley-DeWitt a_2^SD (0.728) differ by 3812x: structurally different objects. Lichnerowicz bound verified (1.08x margin). R(tau) variation 0.91% across fold.
- **ZUBAREV-DERIVATION-46** = PASS -- Zubarev (alpha = 1.15) and Keldysh (alpha = 0.70) agree within 39.4% (< 50%). **S45 ALPHA-EFF 0.410 RETRACTED** (Shannon/FD entropy mismatch). Corrected consistent range: 0.7--1.2.

### WAVE 2 (5 tasks)

- **SPECTRAL-FLOW-NS-46** = FAIL -- alpha_j = 4.03 +/- 0.34, decomposition: counting 1.53 + dimension 1.88 + velocity 0.62. UV-dominated. Velocity weighting adds 0.62 but cannot compensate counting.
- **RG-PAIR-TRANSFER-46** = INFO -- Exact 256-state ED confirms B2 GPV at 91.3% (stronger than nuclear 60-80%). Pair-transfer sum rule has alpha = 0.14, R^2 = 0.002. Pair transfer is a BLOCK property, not k-dependent. No Anderson-Bogoliubov dispersion.
- **QUASISTATIC-NS-46** = INFO (N_e = 0.667) -- Three obstructions: (1) no capture (KE/PE = 2.7e11), (2) virial theorem (<eps_H> = 3/2 for harmonic), (3) phi^2 excluded by Planck at >10 sigma. CLOSED.
- **OMEGA-CLASSIFY-46** = FAIL -- All 279 scalars tachyonic at all tau for all 6 cutoffs. Structural (f' < 0). No fold-specific instability. Gram matrix PSD theorem (kinetic mass always positive, PERMANENT). Module dim = 342 (173 linear + 169 CCS 2013), tau-independent.
- **NUMBER-PROJECTED-BCS-46** = INFO -- PBCS N=1 gives Delta_B3 = 0.054 (SMALLER than BCS 0.084). Moves AWAY from crossing. PBCS matches ED to 0.1%. BCS overestimates all gaps by 60%. Crossing EXISTS at N=2 (tau* = 0.170).

### WAVE 3 (6 tasks)

- **GPV-FRAGMENTATION-46** = INFO -- Single GPV peak at 0.870 M_KK carries 90.6% of pair-addition strength. EWSR verified to 7.6e-14. alpha_GPV = -0.11 (R^2 = 0.001). Block-counting confirmed independently for third time.
- **TWIST-BDG-46** = FAIL -- KO-dim 6 preserved, Krein (8,8) not (3,1). Orientability fails. Fundamental obstruction: BCS order parameter is a Hilbert space rotation, not an algebra automorphism. No non-trivial twist when A_F diagonal in Nambu space. 32nd closure.
- **GGE-FRICTION-46** = INFO -- gamma_CL/gamma_H = 6.8e-3 (1,700x shortfall). 8 modes cannot dissipate 992-mode spectral gradient. Structural ceiling from bath size.
- **TRANSFER-FUNCTION-46** = INFO -- n_s - 1 = 1.8e-7 from GGE beats (need -0.035). Three multiplicative suppressions: f_s = 5.68e-5, energy ratio 4.18e-3, timescale. Internal n_s = -0.68 is FLAT at CMB scales (56-order separation). CLOSED.
- **CONNES-DISTANCE-46** = INFO -- Frobenius-Lipschitz distance confirms Jensen anisotropy. Diameter 250 Planck lengths. su(2) contracts, u(1) stretches. 88% fidelity to geodesic prediction. Adjoint (1,1) metrically softest (lambda_min = 1.11).
- **MAX-PQ-SUM-4** = INFO -- d_Weyl improves from 6.81 to 7.38 (deficit halved). Spectral gap unchanged at 0.8197. Kerner-gravity tension widens from 0.83 to 1.06 decades. a_2/a_0 decreases 25.6% (Seeley-DeWitt ratios converge).

### V-B3B3-46 (standalone, between W3 and W4)

- **V-B3B3-46** = PASS -- V_B3B3_rms = 0.059 > 0.015 threshold (3.9x margin). Prior estimate was 7.5x too low. B3 gap entirely proximity-induced by B2. Isolated B3: Delta = 0. Full 8-mode ED: Delta_B3 = 0.094, still 1.4x short of 0.13. Prior alpha* = 3.91 RETRACTED (correct: 0.775).

### WAVE 4 (22 tasks including addenda)

- **LANDAU-ZENER-NS-46** = FAIL -- alpha = 8.13 (v_k ~ k^2.36, d_k^2 ~ k^3.75). Opposite extreme from Bogoliubov. Both bracket Planck and miss.
- **BAND-INVERSION-BERRY-46** = INFO -- 13 pi Berry phases, Z_2 = (-1)^13 = -1 (nontrivial). Zero band inversions. B1: 2, B2: 1, B3: 10. PW-weighted: 131 (2.19x the 59.8 BCS pairs). 492 non-quantized (degenerate multiplets, need non-Abelian Wilson loop).
- **ANOMALOUS-DISPERSION-46** = INFO -- d(omega_coll)/dk positive at all k. Anomalous dispersion covers 4.5% of Planck gap at best (Model C). Collective mode n_s remains ~-0.2.
- **FWD-BWD-NS-46** = FAIL (244 sigma) -- d_eff floor = 3 (topological, from [iK_7, D_K] = 0). Planck requires d_eff = 0.063. Asymptotic d_eff = 3 confirmed; 5th n_s route closed.
- **NONSINGLET-DISSIPATION-46** = INFO -- gamma_LZ/gamma_H = 3.2. Shortfall 3.8x (down from 1,700x). Non-singlet coupling 14,700x above singlet. Tightest dissipation result ever.
- **FABRIC-TESSELLATION-46** = INFO -- alpha_tess = 1.997 (Rayleigh, k_BdG 7x below k_c). Not geometric optics. Tessellation alpha = 1 CLOSED by scale hierarchy.
- **BAYESIAN-GP-46** = INFO -- tau* = 0.221 +/- 0.117. tau_fold at 0.26 sigma. Dominant uncertainty: gap model choice (99.2% of variance). dtau*/dB2 = 8.64 (steep sensitivity).
- **MULTI-JACOBSON-46** = PASS (marginal) -- max per-mode |rho_k| = 0.0915 < 0.1 threshold. Aggregate, not sector-by-sector. B3 dominates (69% of |rho|). B1 and B2 cross earlier (tau ~ 0.13-0.14).
- **GCM-ZERO-POINT-46** = INFO -- GCM norm kernel > 0.999. BCS rigid in tau. Zero-point correction negligible. CLOSED as tau* correction mechanism.
- **THREE-FREQ-UNIVERSE-46** = INFO -- All beat features at k ~ 10^25 Mpc^-1. delta_P/P ~ 2e-6. Unobservable. Effectively two-frequency (B1-B3 amplitude null). Transit-limited Q < 10^-4.
- **DISSOLUTION-SINGLET-46** = INFO (dynamical) -- S_singlet/S_page = 0.436 +/- 0.014 at dissolution. Suppression is DYNAMICAL (eigenvalue degeneracy pattern), not from block structure.
- **PETER-WEYL-CENSORSHIP-46** = INFO (ROBUST) -- At eps_c: degradation 1.02x (2% change). Sum-rule protected. Spectral action censorship survives block-diagonality dissolution. 137x suppression (6-sector truncation).
- **SPECTRAL-FORM-FACTOR-46** = INFO -- Poisson class (no ramp, R^2 = 0.0002). <r> = 0.439 (Poisson). Sub-Poisson number variance = arithmetical spectrum (representation-theoretic, not chaotic). S38 CHAOS-1 <r>=0.321 CORRECTED to 0.439.
- **SPECTRAL-ZETA-NONINT-46** = INFO -- R(s) = fold/round < 1 for all s > 0. Minimum at s = 2.5 (4.24% suppression). Half-integers interpolate smoothly. Extends CUTOFF-SA-37 to all spectral moments.
- **PSEUDO-RIEMANNIAN-46** = PASS (4/7 axioms) -- KO-dim 6 PRESERVED (p-q = 0 mod 8). Killing signature (4,4). Genuinely complex Dirac spectrum. Cartan = Jensen decomposition exact. Compact resolvent FAILS (non-compact). SU(2,1) as direct replacement CLOSED; 4 open sub-routes.
- **PHONON-MAGNETIC-MOMENT-46** = INFO -- Z_2 = -1 nontrivial. nu = 6.5 Hall channels. mu_total = 3.25 M_KK. Omega = 0 (S25) and Z_2 = -1 (S46) consistent (different invariants, PERMANENT).
- **KAPITZA-PARAMETRIC-46** = INFO -- All beats 52-317x below 2*omega_tau. Arnold tongues < 10^-100 wide. No parametric resonance. Adiabatic regime. CLOSED.
- **BEKENSTEIN-TORSION-46** = PASS -- All 12 (E,R,S) combinations satisfy bound. Worst case: 4.03x margin. Holographic saturation 27% (full spectrum estimate).
- **GSL-QTHEORY-46** = PASS -- 0/599 negative entropy steps. Monotonicity structural (Bogoliubov overlap). Grav/matter ratio 35,983x at tau*. Consistent with GSL-40 and GSL-43.
- **TRANSPLANCKIAN-46** = PASS -- CMB pivot at 7.58e29 l_Planck during transit. B2 Bogoliubov coefficients EXACTLY invariant under modified dispersion (van Hove protection). n_s crisis confirmed as IR problem.
- **SA-ON-OMEGA-TAU-46** = INFO -- 2D landscape S(tau, phi) is a SADDLE at fold. 0.2 degree flow deflection. Transit effectively 1D (phi decoupled).
- **ADDENDUM-TACHYONIC-TRANSIT** = INTERPRETIVE -- 279 tachyonic directions reframed as transit mechanism (EWSB writ large). Configuration/state distinction: spectral triple is the stage, inner fluctuations are the play.
- **ADDENDUM-BERRY-PROTECTION** = INTERPRETIVE + STRUCTURAL -- Reconciles S25 Omega=0 with S46 pi phases (Zak phase, not Chern number). 13 pi-phase states form topological skeleton of transit. Z_2 per sector from BDI.

---

## Scorecard

| Verdict | Count | Gates |
|:--------|:------|:------|
| PASS | 6 | ZUBAREV-DERIVATION-46, V-B3B3-46, MULTI-JACOBSON-46, BEKENSTEIN-TORSION-46, GSL-QTHEORY-46, TRANSPLANCKIAN-46 |
| FAIL | 6 | Q-THEORY-T3T5-46, SPECTRAL-FLOW-NS-46, OMEGA-CLASSIFY-46, TWIST-BDG-46, LANDAU-ZENER-NS-46, FWD-BWD-NS-46 |
| INFO | 23 | Q-THEORY-SELFCONSISTENT-46, HOSE-COUNT-46, A2-GEOMETRIC-46, RG-PAIR-TRANSFER-46, QUASISTATIC-NS-46, NUMBER-PROJECTED-BCS-46, GPV-FRAGMENTATION-46, GGE-FRICTION-46, TRANSFER-FUNCTION-46, CONNES-DISTANCE-46, MAX-PQ-SUM-4, NONSINGLET-DISSIPATION-46, FABRIC-TESSELLATION-46, BAYESIAN-GP-46, GCM-ZERO-POINT-46, THREE-FREQ-UNIVERSE-46, DISSOLUTION-SINGLET-46, PETER-WEYL-CENSORSHIP-46, SPECTRAL-FORM-FACTOR-46, SPECTRAL-ZETA-NONINT-46, PHONON-MAGNETIC-MOMENT-46, KAPITZA-PARAMETRIC-46, SA-ON-OMEGA-TAU-46 |
| PASS (axiom gate) | 1 | PSEUDO-RIEMANNIAN-46 (4/7) |
| INTERPRETIVE | 2 | Tachyonic transit addendum, Berry protection addendum |
| KILLED | 0 | -- |
| **Total** | **38** | 37 computations + 1 axiom gate (PSEUDO-RIEMANNIAN-46 counted once) |

---

## Structural Results (PERMANENT)

1. **Gram matrix PSD theorem**: Kinetic mass Tr([D,phi]^dag [D,phi]) >= 0 for any Hermitian D, any self-adjoint phi. Eliminates all kinetic tachyon mechanisms.
2. **Universal spectral action tachyonic instability**: For any monotone decreasing cutoff f, delta^2 S_b < 0 on all scalar fluctuations. Structural (f' < 0). Not fold-specific.
3. **Module dimensions tau-independent**: dim(Omega^1_D) = 342 = 173 + 169 at all tau.
4. **Mixed grading**: gamma_9 does not cleanly separate gauge from scalar (continuous eigenvalues, not bimodal).
5. **Twisted BdG obstruction**: No non-trivial twist from Aut(A_F) when A_F acts diagonally in Nambu space. Structural.
6. **B3 pairing is proximity-induced**: Isolated B3 sector has Delta = 0. All B3 gap comes from B2-B3 leakage.
7. **Pair transfer is a BLOCK property**: Triple confirmed (W1-2, W2-2, W3-1). Not k-dependent. R^2 = 0.002.
8. **13 pi Berry phases**: Z_2 = (-1)^13 = -1 nontrivial. Zero band inversions. Zak phase reconciles with Omega = 0 (S25). Immune to smooth perturbation (gap protection).
9. **Peter-Weyl censorship sum-rule protection**: Singlet spectral action degrades by only 2% at dissolution eps_c. Survives beyond block-diagonality.
10. **Poisson spectral statistics**: <r> = 0.439 (unique-level). Arithmetical spectrum from representation theory. No quantum chaos.
11. **R(s) < 1 for all s > 0**: All spectral zeta moments suppressed at fold vs round. Extends CUTOFF-SA-37 to half-integers.
12. **KO-dim 6 preserved under SU(2,1)**: p - q = 0 mod 8 for both (8,0) and (4,4) signatures.
13. **Spectral gap truncation-independent**: 0.8197 M_KK set by trivial sector, unchanged at max_pq_sum = 4.
14. **d_eff = 3 floor**: Topological consequence of [iK_7, D_K] = 0 (3 BCS sector channels).
15. **Virial theorem for harmonic quasi-static**: <eps_H> = 3/2 structurally, no slow roll.
16. **Omega = 0 and Z_2 = -1 consistent**: Different invariants (Berry curvature vs Zak phase). PERMANENT.
17. **EWSR Thouless form correct**: Double-commutator form gives 50% of correct answer (channels overlap). Verified to 7.6e-14.
18. **Lichnerowicz bound verified**: lambda_1^2 = 0.672 > (2/7)R = 0.577 (8% margin).
19. **Saddle at fold in (tau, phi) space**: 2D Hessian eigenvalues (-0.64, +2.34), Det < 0. Transit effectively 1D.

---

## New Closures

| # | Closure | Session | Reason |
|:--|:--------|:--------|:-------|
| 32 | TWIST-BDG-46 | S46 W3-2 | A_F diagonal in Nambu space; no non-trivial twist |
| 33 | Quasi-static inflation at q-theory equilibrium | S46 W2-3 | Three obstructions: no capture (KE/PE = 2.7e11), virial (<eps_H>=3/2), phi^2 Planck-excluded |
| 34 | Transfer function GGE beats to 4D CMB | S46 W3-4 | Three multiplicative suppressions, delta(n_s - 1) = 1.8e-7 |
| 35 | Kapitza parametric resonance of tau | S46 W4-18 | 52-317x frequency mismatch, Arnold tongues < 10^-100 |
| 36 | GCM zero-point shift of tau* | S46 W4-9 | BCS rigid in tau, norm kernel > 0.999 |
| 37 | Fabric tessellation alpha = 1 | S46 W4-6 | Rayleigh regime (alpha = 2), k_BdG 7x below k_c |
| 38 | Anomalous dispersion tilt | S46 W4-3 | Covers 4.5% of Planck gap at maximum |

**Running total**: 38 closures (31 prior + 7 new).

---

## The CC After S46

The q-theory cosmological constant mechanism is the framework's only surviving CC path. Its status after S46:

- **Self-consistent gap at N=1**: Crossing ELIMINATED. Delta_B3 = 0.084 < 0.13 threshold (W1-1). The FLATBAND crossing at tau* = 0.210 was an artifact of the ad hoc B3 gap value.
- **Self-consistent gap at N=2**: Crossing EXISTS at tau* = 0.170 (W2-5). At N=2, Delta_B3 = 0.086 and the trace-log is positive enough to cross zero.
- **V_B3B3 direct from Dirac spectrum**: PASS, 3.9x above threshold (V-B3B3-46). But the B3 gap is proximity-induced, not self-consistent. Isolated B3 has Delta = 0.
- **Full 8-mode ED**: Delta_B3 = 0.094, still 1.4x short of 0.13 threshold.
- **Bayesian GP**: tau* = 0.221 +/- 0.117 (fold at 0.26 sigma within 68% CI). Dominant uncertainty is gap model choice (99.2%).
- **GCM zero-point**: Negligible (BCS rigid in tau).
- **Multi-Jacobson**: PASS marginal (max per-mode |rho_k| = 0.0915). Aggregate not sector-by-sector.
- **Prior alpha* = 3.91 RETRACTED**: Correct rescaling is alpha* = 0.775 with exact V_phys.

**Net status**: The CC crossing depends on the physical pair number N. At N=1, it is 1.4x short. At N=2, it exists. The decisive question is whether the physical ground state at the fold has N >= 2 pairs, which requires the full 992-mode spectrum (not the 8-mode truncation).

---

## The n_s After S46

All single-particle pair creation mechanisms and the collective mode are closed.

| Route | alpha / n_s | Status | Session |
|:------|:------------|:-------|:--------|
| Hose count (GPV) | alpha = 0.72, n_s = 0.04 | Structurally ill-defined (R^2 = 0.002) | S46 W1-2 |
| Hose count (raw) | alpha = 1.81, n_s = 1.13 | Too blue | S46 W1-2 |
| Spectral flow | alpha = 4.03 | UV-dominated (velocity + counting + dimension) | S46 W2-1 |
| Landau-Zener | alpha = 8.13 | Opposite extreme from Bogoliubov | S46 W4-1 |
| Transfer function (GGE beats) | n_s - 1 = 1.8e-7 | FLAT at CMB scales, CLOSED | S46 W3-4 |
| Quasi-static at q-theory | N_e = 0.667 | Three obstructions, CLOSED | S46 W2-3 |
| Forward/backward d_eff | d_eff floor = 3 | 244 sigma from Planck, CLOSED (5th route) | S46 W4-4 |
| Anomalous dispersion | n_s = -0.19 best | 4.5% of gap, perturbative | S46 W4-3 |
| Bogoliubov quench (S45) | n_s = -0.588 | 370 sigma, CLOSED | S45 |
| Non-singlet dissipation | shortfall 3.8x | Tightest ever (down from 1,700x) | S46 W4-5 |

**Key structural findings**:
- Pair transfer is a BLOCK property (B1/B2/B3), not k-dependent. Triple confirmed.
- d=3 KZ universality CONFIRMED as floor (S45) AND from d_eff convergence (W4-4).
- Internal n_s = -0.68 is structurally correct but FLAT at CMB scales (56-order xi_KZ/lambda_CMB separation).
- n_s confirmed as IR problem (trans-Planckian PASS, W4-21).
- Non-singlet dissipation provides the ONLY path with single-digit shortfall (3.8x).

---

## Topological Results

- **13 pi Berry phases** across 9 sectors, Z_2 = (-1)^13 = -1 (nontrivial). By branch: B1 = 2, B2 = 1, B3 = 10.
- **Zero band inversions**: Eigenvalue ordering preserved; pi phases from eigenvector half-rotations (Mobius strip, not level crossing).
- **Zak phase reconciles with Omega = 0** (S25 ERRATUM). Berry curvature is local; Zak phase is global. Different invariants.
- **PW-weighted topological channel count**: 131 (2.19x BCS pair count 59.8). Topology provides menu; BCS selects meal.
- **Peter-Weyl censorship**: Sum-rule protected. 2% degradation at dissolution (where level statistics are already GOE).
- **Poisson spectral statistics**: <r> = 0.439. Sub-Poisson number variance = arithmetical spectrum (SU(3) representation theory).
- **Bekenstein bound**: Satisfied at all 12 combinations (4.03x margin worst case). Holographic saturation 27% (full spectrum).
- **GSL**: Monotonic at all 599 steps. Zero negative entropy increments.

---

## NCG Results

- **Omega^1_D inner fluctuation classification**: 342 = 173 + 169 directions, all 279 scalars tachyonic at all tau. Gram matrix PSD (kinetic mass positive, PERMANENT). Universal instability from f' < 0. Reinterpreted as transit mechanism.
- **Twisted BdG**: FAIL (32nd closure). A_F acts diagonally in Nambu space; no non-trivial twist exists.
- **Connes distance**: 88% fidelity to geodesic prediction. Diameter 250 Planck lengths at fold. Adjoint metrically softest (lambda_min = 1.11).
- **Pseudo-Riemannian SU(2,1)**: KO-dim 6 PRESERVED (p-q = 0 mod 8). Killing signature (4,4), not (5,3). Complex Dirac spectrum. Cartan = Jensen exact. Compact resolvent FAILS (non-compact). 4/7 axioms survive.
- **SA on tau x Omega^1_D**: Saddle at fold (Det(H) < 0). 0.2 degree flow deflection. Effectively 1D.
- **Spectral zeta at half-integers**: R(s) < 1 everywhere, minimum at s = 2.5. No half-integer anomaly.
- **Truncation extension (max_pq_sum = 4)**: d_Weyl 6.81 -> 7.38, gap unchanged, Kerner tension widens 0.83 -> 1.06 dec.

---

## S45 Corrections

| Quantity | S45 Value | S46 Corrected | Reason |
|:---------|:----------|:-------------|:-------|
| ALPHA-EFF | 0.410 (1.06x observed) | **RETRACTED**. Range: 0.7--1.2 | Shannon/FD entropy functional mismatch |
| CHAOS-1 <r> | 0.321 ("sub-Poisson") | **0.439** (Poisson) | S38 computed on full spectrum (88% zero spacings from degeneracies); correct value uses unique levels |
| alpha* (coupling rescale) | 3.91 | **0.775** | Prior used approximate V_full; correct V_phys from s39 is much larger |

---

## Key Numbers Table

| Quantity | Value | Source |
|:---------|:------|:------|
| Delta_B3 (self-consistent, N=1) | 0.084 M_KK | W1-1 |
| Delta_B3 (PBCS, N=1) | 0.054 M_KK | W2-5 |
| Delta_B3 (ED, N=1) | 0.053 M_KK | W2-5 |
| Delta_B3 threshold for crossing | 0.13 M_KK | W1-1 |
| V_B3B3_rms (direct, Dirac) | 0.059 M_KK | V-B3B3-46 |
| V_B3B3_rms (prior estimate) | 0.008 M_KK | pre-S46 |
| tau* (Bayesian GP, posterior mean) | 0.221 +/- 0.117 | W4-7 |
| tau* (PBCS N=2 crossing) | 0.170 | W2-5 |
| alpha_eff (Zubarev, E/P) | 1.152 | W1-4 |
| alpha_eff (Keldysh, E/sigma) | 0.698 | W1-4 |
| alpha_eff (S45, RETRACTED) | 0.410 | W1-4 |
| alpha (hose count, GPV) | 0.72 +/- 0.52 | W1-2 |
| alpha (spectral flow) | 4.03 +/- 0.34 | W2-1 |
| alpha (Landau-Zener) | 8.13 | W4-1 |
| n_s (transfer function) | 1.000000181 | W3-4 |
| d_eff floor | 3 (topological) | W4-4 |
| B2 GPV fraction | 91.3% | W2-2 |
| gamma_CL/gamma_H (singlet) | 6.8e-3 | W3-3 |
| gamma_LZ/gamma_H (non-singlet) | 3.2 | W4-5 |
| Dissipation shortfall | 3.8x | W4-5 |
| N_pi (Berry phases) | 13 | W4-2 |
| PW-weighted pi count | 131 | W4-2 |
| Z_2 invariant | -1 (nontrivial) | W4-2 |
| <r> (level spacing, corrected) | 0.439 | W4-13 |
| d_Weyl (max_pq_sum=4) | 7.38 | W3-6 |
| Spectral gap | 0.8197 M_KK (unchanged) | W3-6 |
| Kerner-gravity tension | 1.06 decades | W3-6 |
| a_2^SD (geometric) | 0.728 | W1-3 |
| a_2 (spectral zeta) | 2776.17 | W1-3 |
| SU(2,1) Killing signature | (4,4) | W4-16 |
| Bekenstein worst-case saturation | 24.8% (PASS) | W4-19 |
| GSL negative steps | 0/599 | W4-20 |
| KE/PE at q-theory well | 2.72e11 | W2-3 |
| omega_tau / omega_beat (closest) | 52x | W4-18 |

---

## Open Channels

### CC (q-theory crossing)
1. **Physical pair number at fold**: If N >= 2, crossing exists at tau* = 0.170. Requires full 992-mode ED (beyond 8-mode truncation).
2. **Tau-dependent V(tau)**: Pairing interaction may vary with Jensen deformation. Could shift B2-B3 energy gap.
3. **V_B2B3 enhancement at different tau**: Narrowing B2-B3 gap may enhance induced Delta_B3 above 0.13.

### n_s
4. **Non-singlet dissipation (3.8x shortfall)**: Multi-mode LZ transitions, resonant coupling at lower omega_eff, or extended transit.
5. **Block-resolved n_s**: 3-block structure directly, not wavenumber scaling. Requires full KK projection.
6. **Physics external to single-mode pair creation**: Topological defects, domain-wall correlations, curvaton.

### NCG
7. **Enlarged algebra A_BdG = A_F x M_2(C)**: Non-diagonal Nambu action could enable non-trivial twists.
8. **SU(2,1) discrete series restriction** or compact quotient route.
9. **Non-Abelian Wilson loop**: 492 degenerate-multiplet states need non-Abelian Berry phase.

### DM/DE ratio
10. **Correct vacuum energy functional for GGE**: Zubarev gives 1.15, Keldysh gives 0.70. Definition ambiguity for non-equilibrium state.

---

## Pre-Registered Gates for S47

| Gate | Criterion | Source |
|:-----|:----------|:------|
| WILSON-LOOP-47 | Total pi-count (Abelian + non-Abelian) in [13, 50] | Berry addendum |
| DISSOLUTION-BERRY-47 | All 13 pi-phase states survive at eps = 0.5 * eps_c | Berry addendum |
| CLOSED-LOOP-47 | Closed-loop gamma = 0 for all non-degenerate states (S25 consistency) | Berry addendum |
| N-PAIR-FULL-47 | Physical pair number from 992-mode spectrum: PASS if N >= 2 | W1-1, W2-5 |
| NONSINGLET-SELFCONSIST-47 | Self-consistent LZ with negative feedback: PASS if shortfall < 2x | W4-5 |
| V-TAU-SWEEP-47 | V_{kk'}(tau) variation: PASS if Delta_B3(tau_fold) > 0.13 at any tau | W1-1, V-B3B3-46 |

---

## Files Produced

38 scripts in `tier0-computation/`:

```
s46_anomalous_dispersion.py     s46_kapitza_parametric.py
s46_bayesian_gp.py              s46_landau_zener_ns.py
s46_bekenstein_torsion.py       s46_max_pq_sum_4.py
s46_berry_phase.py              s46_multi_jacobson.py
s46_connes_distance.py          s46_nonsinglet_dissipation.py
s46_dissolution_singlet.py      s46_number_projected_bcs.py
s46_fabric_tessellation.py      s46_omega_classify.py
s46_fwd_bwd_ns.py               s46_omega_verify.py
s46_gcm_zero_point.py           s46_peter_weyl_censorship.py
s46_geometric_a2.py             s46_phonon_magnetic_moment.py
s46_gge_friction.py             s46_pseudo_riemannian.py
s46_gpv_fragmentation.py        s46_qtheory_selfconsistent.py
s46_gsl_qtheory.py              s46_quasistatic_ns.py
s46_hose_count.py               s46_rg_pair_transfer.py
s46_sa_omega_tau.py              s46_spectral_flow_ns.py
s46_spectral_form_factor.py     s46_spectral_zeta_nonint.py
s46_three_freq_universe.py      s46_transfer_function.py
s46_transplanckian.py           s46_twist_bdg.py
s46_v_b3b3.py                   s46_zubarev_derivation.py
```

Plus corresponding `.npz` data and `.png` plots for each.

2 addenda in `sessions/session-46/`:

```
s46_addendum_tachyonic_transit.md
s46_addendum_berry_protection.md
```
