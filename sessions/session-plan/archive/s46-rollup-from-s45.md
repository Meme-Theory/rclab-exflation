# S46 Rollup: Every Suggestion, Gate, and Open Question from S45

**Date**: 2026-03-15
**Author**: gen-physicist (extraction agent)
**Sources**: 13 documents read in full (4 Landau review files do not exist; noted in metadata)
**Purpose**: SOLE INPUT for S46 planning. Nothing not in this document will be planned.

**Documents read**:
1. `session-45-quicklook.md`
2. `session-45-results-workingpaper.md` (2300+ lines, read in full across 5 sections)
3. `session-45-quicklook-tesla-collab.md`
4. `session-45-quicklook-nazarewicz-collab.md`
5. `session-45-quicklook-spectral-collab.md`
6. `session-45-quicklook-connes-collab.md`
7. `session-45-quicklook-hawking-collab.md`
8. `s45_cc_balance_sheet.md`
9. `s45_addendum_hose_count_ns.md`
10. `s45_addendum_forward_backward_ns.md`
11. `s45_tinfoil_minus068.md`
12. `s45_formula_audit.md`
13. `tier0-computation/s45_heat_kernel_audit.md`

**Files NOT found** (listed in task but absent from disk): `s45_landau_review_nazarewicz.md`, `s45_landau_review_qa.md`, `s45_landau_review_einstein.md`, `s45_landau_review_tesla.md`.

---

## 1. CONVERGENT PROPOSALS (suggested by 2+ sources)

Sorted by convergence count (number of independent sources proposing the same computation).

### 1.1 Self-consistent Delta(tau) for q-theory (CONVERGENCE: 7/7)

- **Sources**: Quicklook (Section "Open Channels"), Working paper (W2-R5, W5-R2 Section VI), Tesla review (Section 2, 5.1), Nazarewicz review (Way Forward 1, 2, Summary Priority 1), Spectral-geometer review (Section V, VII), Connes review (Section V.A), Hawking review (Section I.1, VI.1), CC balance sheet (Section VII.A)
- **Proposer**: Every reviewer independently
- **What**: Solve the BCS gap equation Delta_k(tau) self-consistently at each tau, then recompute the q-theory Gibbs-Duhem crossing. Couple the gap equation 1/g = sum d_k/(2 E_k) with the Gibbs-Duhem condition rho_gs(tau) = epsilon(tau) - tau * d_epsilon/dtau = 0.
- **Why**: Determines whether the CC crossing at tau* = 0.209 locks onto tau_fold = 0.190 when the gap becomes tau-dependent. This is the single most important open computation.
- **Input data**: `s45_qtheory_bcs.npz`, `s42_hauser_feshbach.npz`, `s41_spectral_refinement.npz`, `s44_dos_tau.npz`
- **Priority**: CRITICAL
- **Pre-registered gate**: Q-THEORY-SELFCONSISTENT-46. PASS: tau* in [0.17, 0.21]. FAIL: No crossing in [0.05, 0.35].
- **Nazarewicz prediction**: tau* shifts by 10-20% (nuclear frozen-gap analogy); may lock onto fold.
- **Spectral-geometer note**: The T3-T5 true crossing at tau = 0.19104 may PULL the BCS gap discontinuity, locking tau* to the spectral crossing (see item 1.5).

### 1.2 Hose-count pair mode counting (CONVERGENCE: 6/7)

- **Sources**: Quicklook (Section "Open Channels"), Hose-count addendum, Tesla review (Section 3 Failure 2), Nazarewicz review (Way Forward 1, Section III), Spectral-geometer review (Section IV), Hawking review (Section IV.3), Connes review (Section V.B)
- **Proposer**: User (original concept), Tesla, Nazarewicz, Spectral-geometer, Hawking, Connes
- **What**: Count the number of independent BCS pair modes per (p,q) sector as a function of Casimir k = sqrt(C_2). The pair modes are eigenvectors of the 16x16 BdG Hamiltonian restricted to each sector. Determine whether the count grows as k^alpha with alpha in [0.8, 1.2].
- **Why**: n_s - 1 = alpha - beta. Single-particle gives alpha = 6 (Weyl), collective gives alpha = 0. Planck needs alpha ~ 1. The pair mode count is the missing intermediate quantity.
- **Input data**: `s42_hauser_feshbach.npz`, `s44_dos_tau.npz`, `s45_collective_ns_rpa.npz`
- **Priority**: CRITICAL
- **Pre-registered gate**: HOSE-COUNT-46. PASS: n_s in [0.955, 0.975] from pair mode count ~ k^alpha with alpha in [0.8, 1.2]. FAIL: alpha < 0.5 or alpha > 2.0.
- **Nazarewicz mechanism**: GPV fragmentation gives 2-4 fragments per sector; strength ~ d^{1/2} ~ k^{alpha_frag} with alpha_frag ~ 1.0 from nuclear pair-transfer sum rules.
- **Hawking mechanism**: Pair modes on a 1D chain in representation space give alpha = 1 from 1D topology.
- **Tesla mechanism**: BCS pair count min(d, 8) grows as d ~ k for low k, saturates at 8 for high k; crossover determines n_s.

### 1.3 Zubarev derivation cross-check (CONVERGENCE: 5/7)

- **Sources**: Quicklook (Section "Open Channels"), Working paper (ALPHA-EFF-45 assessment), Tesla review (Section 2), Formula audit (MODERATE violation #1), CC balance sheet (estimated factors)
- **Proposer**: Formula audit, Tesla, quicklook
- **What**: Trace the formula alpha = S_GGE/(S_max - S_GGE) to a specific published equation in Zubarev's "Nonequilibrium Statistical Thermodynamics" (1974), OR derive it from first principles. Cross-check with Keldysh/Schwinger-Keldysh formalisms.
- **Why**: The Zubarev formula is the ONLY method giving alpha = 0.410 (1.06x observed). Its derivation chain is unpinned. If it is a specific approximation within the Zubarev framework, the agreement may be an artifact.
- **Input data**: `s45_alpha_eff.npz`, `s42_gge_energy.npz`
- **Priority**: HIGH
- **Pre-registered gate**: ZUBAREV-DERIVATION-46. PASS: Zubarev and Keldysh agree (< 50% discrepancy). FAIL: Disagree by > 50%.

### 1.4 Independent geometric a_2 from Jensen metric (CONVERGENCE: 4/7)

- **Sources**: Spectral-geometer review (Way Forward 4), Connes review (Section V.D), Heat kernel audit (Section 6.3, uncomputed priority), Quicklook (HEAT-KERNEL-AUDIT-45)
- **Proposer**: Spectral-geometer, Connes, Heat kernel audit
- **What**: Compute a_2 = (4pi)^{-4} * 16 * integral(R(tau)/6 * dV) directly from the known Jensen metric Ricci scalar R(tau). Compare to spectral a_2 = 2776.17 at fold.
- **Why**: Quantifies the 30-50% truncation error on a_2, determines whether the 0.83-decade M_KK tension is a truncation artifact, and closes the loop on Tier 2 validity. Purely analytic -- costs nothing.
- **Input data**: `r20a_riemann_tensor.npz` (R(tau) known analytically from S20a), `canonical_constants.py`
- **Priority**: HIGH
- **Pre-registered gate**: A2-GEOMETRIC-46. PASS: spectral a_2 agrees with geometric a_2 within 30%. FAIL: disagreement > 100%.

### 1.5 T3-T5 crossing lock-on for q-theory (CONVERGENCE: 3/7)

- **Sources**: Spectral-geometer review (Section VII), Tesla review (Section 3 Failure 7 in-text), Nazarewicz review (implicit in self-consistency discussion)
- **Proposer**: Spectral-geometer
- **What**: Solve the self-consistent BCS gap equation Delta(tau) across the T3-T5 true crossing at tau = 0.19104. Does Delta(tau) have a discontinuity or kink? Does the q-theory crossing tau* lock onto tau = 0.191?
- **Why**: The T3-T5 crossing is where the singlet top eigenvalue and the non-singlet bottom eigenvalue coincide. The BCS gap hierarchy may be locked to this spectral crossing, pulling tau* from 0.209 to 0.191 (0.5% from fold).
- **Input data**: `s45_dos_fine_scan.npz`, `s45_qtheory_bcs.npz`, `s42_hauser_feshbach.npz`
- **Priority**: HIGH (subsumes 1.1 if computed jointly)
- **Pre-registered gate**: Q-THEORY-T3T5-46. PASS: tau* locks onto [0.188, 0.194]. FAIL: tau* outside [0.15, 0.25].

### 1.6 Anderson-Bogoliubov collective mode for n_s (CONVERGENCE: 3/7)

- **Sources**: Quicklook (Section "Open Channels"), Nazarewicz review (Way Forward 5), Working paper (W5-R4 COLLECTIVE-NS, pre-registered but not computed)
- **Proposer**: Nazarewicz, quicklook
- **What**: Compute the Anderson-Bogoliubov (Goldstone) mode dispersion omega_AB(k) = v_pair * k for the BCS condensate on SU(3). The pair velocity v_pair is determined by the superfluid stiffness from V_{kl}. Compute the resulting n_s from the AB pair-creation spectrum.
- **Why**: The AB mode creates pairs with zero energy cost at long wavelength (Goldstone theorem), giving a flat spectrum at low k (n_s ~ 1). The correction from dispersion curvature gives n_s - 1 = -(2/3)(omega_AB''/omega_AB')^2 * k^2.
- **Input data**: `s42_hauser_feshbach.npz` (V matrix), `s44_dos_tau.npz`
- **Priority**: HIGH
- **Pre-registered gate**: COLLECTIVE-NS-46. PASS: n_s in [0.955, 0.975] from AB GRPA. FAIL: n_s outside [0.80, 1.10].

### 1.7 max_pq_sum = 6 computation (CONVERGENCE: 3/7)

- **Sources**: Spectral-geometer review (Way Forward 1, Section II), Connes review (Way 3), Tesla review (Section 3 Failure 4)
- **Proposer**: Spectral-geometer, Connes, Tesla
- **What**: Compute the Dirac spectrum at max_pq_sum = 6. Track d_Weyl convergence toward 8, M_KK tension narrowing, and Taylor expansion behavior.
- **Why**: Tests whether the Taylor exactness theorem develops non-perturbative corrections as the spectrum approaches the continuum. Sharpens G_N from a_2. Determines whether the 0.83-decade M_KK tension is a truncation artifact.
- **Input data**: `tier1_dirac_spectrum.py` (computational infrastructure)
- **Priority**: MEDIUM (computationally intensive -- ~8.7s per s-value, new irreps add sectors with dim^2 up to 441)
- **Pre-registered gate**: None explicitly stated. Diagnostics: d_Weyl closer to 8? |c_{n+1}/c_n| growing (asymptotic onset)? M_KK tension < 0.5 decades?

### 1.8 GGE-to-4D transfer function for n_s (CONVERGENCE: 3/7)

- **Sources**: Tesla review (Section 4 "Three-Frequency Universe", Section 5.3), Tinfoil -0.68 document (constraint map update), Hawking review (Section IV.2)
- **Proposer**: Tesla (primary), Hawking, tinfoil analysis
- **What**: Compute the 4D power spectrum from the convolution of the 3 GGE beat frequencies (B2-B1 = 0.052, B2-B3 = 0.266, B1-B3 = 0.318 M_KK) with the Friedmann dynamics during transit. The transfer function maps internal beats to 4D density perturbations.
- **Why**: The tilt n_s may be a property of the convolution (transfer function), not of the internal spectrum alone. Every failed n_s route looked at one end of the convolution.
- **Input data**: `s45_gge_beating.npz`, `s44_friedmann_bcs_audit.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None explicitly stated.

---

## 2. n_s PROPOSALS (ALL -- this is the crisis)

### 2.1 HOSE-COUNT-46 (pair mode counting per sector)
See item 1.2 above. CRITICAL. Pre-registered gate stated.

### 2.2 Anderson-Bogoliubov GRPA collective modes
See item 1.6 above. HIGH. Pre-registered gate stated.

### 2.3 GGE beat-to-4D transfer function
See item 1.8 above. MEDIUM.

### 2.4 Spectral current j(lambda, tau) for n_s
- **Source**: Spectral-geometer review (Section IV, Way Forward 2)
- **Proposer**: Spectral-geometer
- **What**: Define spectral current j(lambda, tau) = sum_k delta(lambda - lambda_k(tau)) * (d lambda_k / d tau). Fourier transform in lambda. Extract effective alpha from k-dependence.
- **Why**: Tier 1 quantity (computed from eigenvalues and derivatives). Weights modes by VELOCITY in spectral plane, producing intermediate alpha between 0 and 6. Modes near van Hove singularities contribute disproportionately.
- **Input data**: `s44_dos_tau.npz`, `s44_vanhove_track.npz`
- **Priority**: HIGH
- **Pre-registered gate**: SPECTRAL-FLOW-NS-46. PASS: alpha in [0.8, 1.2]. FAIL: alpha outside [0.5, 2.0].

### 2.5 Richardson-Gaudin pair transfer spectral function from GGE
- **Source**: Nazarewicz review (Way Forward 1)
- **Proposer**: Nazarewicz
- **What**: Using the 8 Richardson-Gaudin conserved integrals, compute S(omega, k) = sum_n |<n|P^+_k|GGE>|^2 delta(omega - omega_n). The pair creation operator P^+ decomposes as P^+ = sum_a sum_k g_a(k)/(z_a - epsilon_k). The number of peaks at each k determines alpha.
- **Why**: The GGE is NOT the BCS ground state -- pair transfer FROM the GGE involves de-excitation with different selection rules. Nuclear sd-shell analog predicts 2-4 fragments per sector.
- **Input data**: `s42_gge_energy.npz`, `s42_hauser_feshbach.npz`
- **Priority**: HIGH
- **Pre-registered gate**: Subsumes HOSE-COUNT-46 (same alpha counting, different method).
- **Nazarewicz prediction**: alpha_frag ~ 1.0 from nuclear sum rules, halved to ~1.0 by K_7 selection rules.

### 2.6 K_7 selection rules halving the hose count
- **Source**: Nazarewicz review (Section III Mechanism B), Hose-count addendum (connection to T11-T12)
- **Proposer**: Nazarewicz
- **What**: Determine how many pair modes per sector are K_7-forbidden (pair operator carries K_7 = +/-1/2). If half are forbidden, alpha -> alpha/2.
- **Why**: Starting from pair degeneracy alpha ~ 2, K_7 restriction gives alpha ~ 1.
- **Input data**: `s42_hauser_feshbach.npz` (K_7 charges known)
- **Priority**: HIGH (quick analytic check)
- **Pre-registered gate**: Part of HOSE-COUNT-46.

### 2.7 Landau-Zener k-dependent adiabaticity filter
- **Source**: Tesla review (Section 3 Failure 2), Nazarewicz review (Section III Mechanism C), Hose-count addendum
- **Proposer**: Tesla, Nazarewicz
- **What**: Compute the Landau-Zener adiabaticity parameter Q_k = delta_k^2/(hbar * v_k) as a function of Casimir k. If Q_k ~ k, the transition between adiabatic and diabatic regimes provides alpha ~ 1.
- **Why**: Transit is sudden (Q_median = 19.5) but Q_k varies with k. If the gap delta_k and sweep rate v_k both depend on k through the band structure, P_k = exp(-2pi Q_k) could have the correct intermediate tilt.
- **Input data**: `s45_kz_ns.npz`, `s44_dos_tau.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: Part of HOSE-COUNT-46.

### 2.8 Forward/backward pair creation n_s
- **Source**: Forward/backward addendum
- **Proposer**: User/team
- **What**: Full computation of the forward/backward pair creation interference. Sanity check PASSED (red tilt confirmed, ratio decreases with k from 755,000x to 865x). The d_eff converges to 3 at tau_back = 0.50.
- **Why**: Interference between two populations could bypass both Weyl degeneracy (it's a ratio) and collective flatness (k-dependent Delta/lambda).
- **Input data**: `s45_fwd_bwd_ns.npz`
- **Priority**: MEDIUM (sanity check done; full computation available for S46)
- **Pre-registered gate**: FWD-BWD-NS-46. PASS: n_s in [0.955, 0.975]. FAIL: n_s outside [0.80, 1.10].

### 2.9 Quasi-static phase at q-theory equilibrium for eps_H reduction
- **Source**: Hawking review (Section IV.2, VI.1)
- **Proposer**: Hawking
- **What**: If the q-theory crossing at tau* = 0.209 is an attractor, the modulus spends time near tau* with near-zero velocity. During this quasi-static phase, eps_H << 1, and eps_V = 0.016 supports quasi-de Sitter. Compute the residence time and resulting N_e.
- **Why**: eps_V = 0.016 is already flat enough for Planck. The problem is eps_H = 3.0 (velocity). The q-theory equilibrium provides a natural slow-roll phase IF the modulus can be trapped.
- **Input data**: `s45_qnm_ns.npz`, `s45_qtheory_bcs.npz`
- **Priority**: HIGH
- **Pre-registered gate**: QUASISTATIC-NS-46. PASS: N_e > 10 during dwell at tau*. FAIL: N_e < 0.1.

### 2.10 GGE dissipative friction (Caldeira-Leggett) on modulus
- **Source**: Hawking review (Section IV.2, VI.2), Nazarewicz review (Way Forward 6)
- **Proposer**: Hawking, Nazarewicz
- **What**: Model the 8 Richardson-Gaudin modes as a finite heat bath providing Caldeira-Leggett friction on the tau modulus. Compute gamma_eff and the resulting velocity reduction factor.
- **Why**: 829x velocity reduction needed for n_s = 0.965. If 8 modes provide sufficient friction, the flat potential (eps_V = 0.016) can generate the tilt.
- **Input data**: `s45_gge_beating.npz`, `s44_friedmann_bcs_audit.npz`, `s42_gge_energy.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: GGE-FRICTION-46. No explicit criteria stated; diagnostic computation.

### 2.11 Non-singlet mode dissipation for velocity reduction
- **Source**: Nazarewicz review (Way Forward 6)
- **Proposer**: Nazarewicz
- **What**: Estimate one-body dissipation rate for the tau modulus from energy absorption of non-singlet modes (101,968 modes in sectors with d > 1). If non-singlet modes respond diabatically, they provide maximum dissipation.
- **Why**: The S45 WKB assessment (Q_median = 19.5) was computed for BCS-active modes. Non-singlet modes have different adiabaticity parameters. 101,968 modes could provide much larger effective viscosity than 8 BCS modes.
- **Input data**: `s44_dos_tau.npz`, `s45_kz_ns.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated.

### 2.12 Band inversion Berry phase for topological pair creation
- **Source**: Tesla review (Section 4 "Band Inversion and Topological Protection")
- **Proposer**: Tesla
- **What**: Compute the Berry phase along a path in (p,q) space that encircles the band-inversion point at tau = 0. If Berry phase = pi, pair creation at this point is topologically protected and produces exactly one pair per Chern sector per transit.
- **Why**: Would provide alpha = 1 from topology, not from BCS pair counting. Quantized pair creation rate is k-independent, giving a discrete contribution to the power spectrum.
- **Input data**: `s45_acoustic_ns.npz`, `s44_dos_tau.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated.

### 2.13 Anomalous dispersion of RPA collective mode
- **Source**: Tesla review (Section 3 Failure 3)
- **Proposer**: Tesla
- **What**: Recompute the RPA with full k-dependent V_{kl}(tau) from the Dirac eigenvalue structure (not constant-V). Check whether d(omega_coll)/dk becomes positive and k-linear for some k range.
- **Why**: If the pairing interaction inherits the anomalous dispersion of the parent band (band inversion, negative group velocity v_g = -0.197), the RPA collective mode acquires k-dependent push that compensates Weyl dispersion.
- **Input data**: `s42_hauser_feshbach.npz`, `s45_collective_ns_rpa.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated.

### 2.14 Pair-mode 1D topology for alpha = 1
- **Source**: Hawking review (Section IV.3)
- **Proposer**: Hawking
- **What**: Compute the pair mode density as a function of Casimir wavenumber. If pair modes form a 1D chain in representation space connected by nearest-neighbor couplings V(p,q;p',q'), alpha = 1 follows from the 1D topology.
- **Why**: Independent of SU(3) dimensionality.
- **Input data**: `s42_hauser_feshbach.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: Subsumes HOSE-COUNT-46.

---

## 3. CC PROPOSALS (q-theory follow-ups)

### 3.1 Self-consistent q-theory + BCS
See item 1.1 above. CRITICAL.

### 3.2 T3-T5 crossing lock-on
See item 1.5 above. HIGH.

### 3.3 Number-projected BCS (PBCS) for trace-log
- **Source**: Nazarewicz review (Way Forward 2)
- **Proposer**: Nazarewicz
- **What**: Implement PBCS on the 8-mode system using the Pfaffian overlap formula. The PBCS-corrected trace-log will provide a more accurate q-theory crossing tau* with controlled uncertainty.
- **Why**: The 16% BCS/ED gap in E_cond maps to ~20% error in tau*. PBCS closes this gap systematically. Richardson exact solution gives EXACT ground-state energy.
- **Input data**: `s42_hauser_feshbach.npz`, `s37_pair_susceptibility.npz`
- **Priority**: HIGH
- **Pre-registered gate**: None stated explicitly. Diagnostic: how much does tau* shift with PBCS vs BCS?

### 3.4 GCM zero-point correction for tau-stabilization
- **Source**: Nazarewicz review (Way Forward 3)
- **Proposer**: Nazarewicz
- **What**: Compute GCM norm overlaps G(tau, tau') for 5 tau values in [0.10, 0.25] using BCS Pfaffian overlap. Diagonalize 5x5 GCM equation. The zero-point correction is the difference between lowest GCM eigenvalue and V(tau) minimum.
- **Why**: GCM adds zero-point fluctuation energy. Nuclear analog: 0.5-1 MeV lowering. Could provide the final 0.019 shift to bring tau* from 0.209 to 0.190.
- **Input data**: `s42_hauser_feshbach.npz`, `s44_dos_tau.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated. Nazarewicz prediction: GCM correction ~0.5-2% of spectral action at fold.

### 3.5 Multi-T Jacobson sector-by-sector consistency
- **Source**: Hawking review (Section I.1)
- **Proposer**: Hawking
- **What**: Compute the 8 sector-by-sector Gibbs-Duhem conditions at tau* = 0.209. Each GGE sector contributes independently to the gravitating stress-energy.
- **Why**: Non-trivial consistency check: the Gibbs-Duhem cancellation must hold sector-by-sector.
- **Input data**: `s44_multi_t_jacobson.npz`, `s45_qtheory_bcs.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: MULTI-JACOBSON-QTHEORY-46. PASS: all 8 sectors |rho_k(tau*)| < 0.1 M_KK^4. FAIL: any |rho_k| > 1.0.

### 3.6 Bayesian GP emulator for tau*(Delta) posterior
- **Source**: Nazarewicz review (Way Forward 4)
- **Proposer**: Nazarewicz
- **What**: Construct a Gaussian process emulator for tau*(Delta_B2, Delta_B1, Delta_B3) using the 60-point scan from Q-THEORY-BCS-45. Compute posterior tau* = 0.209 +/- sigma_tau.
- **Why**: Every nuclear DFT prediction comes with an error bar. tau* has none.
- **Input data**: `s45_qtheory_bcs.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated. Nazarewicz prediction: sigma_tau ~ 0.03-0.05, 68% CI includes fold.

### 3.7 Perturbative stability of q-theory equilibrium
- **Source**: CC balance sheet (Section VII.D), Working paper (W5-R2 Section VI)
- **Proposer**: Quicklook, CC balance sheet
- **What**: Does the tau* = 0.209 crossing survive quantum corrections? Backreaction is 3.7% (perturbative). Higher-order effects are uncomputed.
- **Input data**: `s45_qtheory_bcs.npz`, `s38_cc_instanton.npz`
- **Priority**: LOW
- **Pre-registered gate**: None stated.

### 3.8 Continuum limit spectral zeta
- **Source**: CC balance sheet (Section VII.B), Tesla review (Section 3 Failure 4), Spectral-geometer review (Section IX)
- **Proposer**: Multiple
- **What**: As max_pq_sum -> infinity, the spectral zeta develops genuine poles. Non-perturbative corrections to the CC could arise. Compute spectral action at max_pq_sum = 6, 7 and track Taylor coefficient ratios.
- **Why**: Taylor exactness is specific to finite truncation. Continuum limit restores asymptotic character.
- **Input data**: Requires new Dirac spectrum computation at higher truncation.
- **Priority**: MEDIUM (expensive)
- **Pre-registered gate**: None stated.

---

## 4. DM/DE PROPOSALS

### 4.1 Zubarev derivation and Keldysh cross-check
See item 1.3 above. HIGH.

### 4.2 DESI DR2/3 w_a = 0 test
- **Source**: Quicklook (Section "Open Channels"), Working paper (TWO-FLUID-DESI-45), Tesla review (Section 2)
- **Proposer**: Multiple
- **What**: When DESI DR2/3 data become available, test w_a = 0 prediction. Currently 0.76sigma from DESI DR1.
- **Why**: The framework's strongest falsifiable test. GGE is time-independent by integrability.
- **Input data**: `s45_two_fluid_desi.npz`
- **Priority**: HIGH (observational, not computational -- external data dependency)
- **Pre-registered gate**: DESI-WA-46. PASS: |w_a| < 0.3 in DESI DR2. FAIL: |w_a| > 1.0 at > 3 sigma.

### 4.3 ALPHA-ENV void vs filament test
- **Source**: Quicklook (Section "Open Channels")
- **Proposer**: Queued from S42
- **What**: Compute delta_alpha/alpha ~ 10^{-6} between void and filament regions.
- **Why**: Sole surviving LSS discriminant.
- **Input data**: Requires cosmological simulation or observational data.
- **Priority**: LOW (queued since S42)
- **Pre-registered gate**: None stated.

### 4.4 Island formula for GGE-to-Gibbs thermalization
- **Source**: Hawking review (Section VI.2)
- **Proposer**: Hawking
- **What**: Apply the island formula S_gen = S_vN(R+I) + A(dI)/(4G_N) to the GGE-to-Gibbs transition at t_therm ~ 6. Check whether the generalized entropy has a non-trivial extremum.
- **Why**: Geometric interpretation of thermalization. Half-Page value S/S_page ~ 0.47 may have island interpretation.
- **Input data**: `s45_gl_gge.npz`, `s42_gge_energy.npz`
- **Priority**: LOW
- **Pre-registered gate**: ISLAND-GGE-46. No explicit criteria stated.

### 4.5 Dissolution singlet-only partition
- **Source**: Hawking review (Section II.3)
- **Proposer**: Hawking
- **What**: Compute S(eps_c) restricted to singlet-singlet partition only (16 modes, A=8, B=8). If S_singlet/S_page_singlet > 0.95, suppression is purely from block-diagonality.
- **Why**: Distinguishes geometric vs dynamical information suppression.
- **Input data**: `s45_dissolution_entropy.npz` (NOT STARTED in S45, data exists)
- **Priority**: LOW
- **Pre-registered gate**: DISSOLUTION-STRUCTURE-46. PASS: S_singlet/S_page > 0.95. INFO: ~ 0.47.

---

## 5. STRUCTURAL / MATHEMATICAL PROPOSALS

### 5.1 Omega^1_D classification (342 inner fluctuation directions)
- **Source**: Connes review (Section II, Way 1)
- **Proposer**: Connes
- **What**: For each of the 342 directions phi_alpha in Omega^1_D(A_F) (173 linear + 169 quadratic from CCS 2013), compute: (a) S(D + phi_alpha) to second order -- mass-squared matrix M^2. (b) Eigenvalues of M^2. (c) Gauge quantum numbers. Determine if any direction is tachyonic at fold but not at round.
- **Why**: If a tachyonic direction exists, the fold is an instability in the inner-fluctuation moduli space -- a NEW tau-stabilization mechanism bypassing all 31 spectral action closures. The 343-dimensional combined space (tau) x (Omega^1_D) is entirely unexplored.
- **Input data**: `s42_hauser_feshbach.npz`, `s45_weak_order_one.npz`
- **Priority**: HIGH (highest NCG priority per Connes)
- **Pre-registered gate**: OMEGA-CLASSIFY-46. PASS: any tachyonic direction at fold but not at round. FAIL: all directions massive at all tau.

### 5.2 Twisted BdG spectral triple construction
- **Source**: Connes review (Section III, Way 2)
- **Proposer**: Connes
- **What**: Combine the twist (Papers 30, 33, 44) with BdG extension (S35): construct (A_F, H_BdG, D_{BdG,sigma}, J_BdG, gamma_BdG). Verify axioms. Does the Krein signature match (3,1)?
- **Why**: The twist converts Riemannian BdG to Krein-space triple, potentially bridging BCS condensation (internal, Riemannian) to emergent spacetime (external, Lorentzian).
- **Input data**: S35 BdG spectral triple results, Papers 30/33/44
- **Priority**: MEDIUM
- **Pre-registered gate**: TWIST-BDG-46. PASS: KO-dim preserved and Krein signature matches (3,1). FAIL: axioms violated.

### 5.3 Connes distance on truncated Jensen SU(3)
- **Source**: Spectral-geometer review (Way Forward 5)
- **Proposer**: Spectral-geometer
- **What**: Compute d(e, g) = sup{|f(e) - f(g)| : ||[D,f]|| <= 1} for the identity e and selection of group elements in the Jensen-deformed metric.
- **Why**: Gives effective diameter, anisotropy, and a well-defined Connes-distance analog of spectral dimension on the finite crystal. Connects to Connes-van Suijlekom 2021 (Paper 28) convergence theorems.
- **Input data**: `s42_hauser_feshbach.npz`
- **Priority**: MEDIUM
- **Pre-registered gate**: None stated.

### 5.4 Spectral form factor and eigenvalue correlations
- **Source**: Spectral-geometer review (Way Forward 6)
- **Proposer**: Spectral-geometer
- **What**: Compute K(t) = |sum_k d_k e^{i lambda_k t}|^2 / (sum d_k)^2. Identify the Heisenberg time t_H, ramp-plateau structure, and tau-dependence.
- **Why**: Tier 1 quantity. Probes two-point eigenvalue correlations. Heisenberg time is a natural scale in the finite crystal. Non-trivial tau-dependent structure would provide intrinsic observables.
- **Input data**: `s44_dos_tau.npz`
- **Priority**: LOW
- **Pre-registered gate**: None stated.

### 5.5 Peter-Weyl censorship (killed in S45, available for S46)
- **Source**: Working paper (W4-R5, KILLED)
- **Proposer**: S45 plan
- **What**: Complete the Peter-Weyl censorship computation that was killed when the agent stuck in a loop.
- **Why**: Was pre-registered but not completed.
- **Input data**: `s44_eih_grav.npz`, `s44_dissolution_scaling.npz`
- **Priority**: LOW
- **Pre-registered gate**: Original gate from S45.

### 5.6 Spectral action moment ratios at non-integer s
- **Source**: Spectral-geometer review (Way Forward 3)
- **Proposer**: Spectral-geometer
- **What**: Compute zeta(s) for non-integer s (s = 1/2, 3/2, 5/2). Interpolate between well-behaved (large s) and UV-sensitive (small s) regimes.
- **Why**: Reveals how the q-theory crossing tau* depends on UV completion. Tier 1 quantity.
- **Input data**: `s44_dos_tau.npz`
- **Priority**: LOW
- **Pre-registered gate**: None stated.

### 5.7 Spectral action on combined (tau) x (Omega^1_D) moduli space
- **Source**: Connes review (Section II, connection to HESS-40)
- **Proposer**: Connes
- **What**: The S40 Hessian was computed over tau only (1D). Omega^1_D adds 342 directions. Compute the spectral action landscape on the combined 343-dimensional space.
- **Why**: HESS-40 found all 22 transverse eigenvalues positive at fold. The Omega^1_D directions are orthogonal to tau. The combined landscape is entirely unexplored.
- **Input data**: Results from 5.1 (Omega classification) + HESS-40
- **Priority**: MEDIUM (depends on 5.1)
- **Pre-registered gate**: Part of OMEGA-CLASSIFY-46.

### 5.8 Pseudo-Riemannian spectral triple on SU(2,1)
- **Source**: Connes review (Section IV)
- **Proposer**: Connes
- **What**: Replace SU(3) with non-compact real form SU(2,1). Compute D_K on SU(2,1) with Killing metric. Verify which axioms survive.
- **Why**: If the transit corresponds to SU(3) -> SU(2,1) deformation, the pseudo-Riemannian spectral triple is the correct framework.
- **Input data**: Paper 36 (de Groot 2026)
- **Priority**: LOW (speculative)
- **Pre-registered gate**: None stated.

---

## 6. DIAGNOSTICS AND INFRASTRUCTURE

### 6.1 Formula audit compliance target 80%
- **Source**: Formula audit (S46 Recommendations)
- **What**: Require every formula audit block to contain all four items (formula, dimensional check, limiting case, citation) as a formatted sub-block. Target 80% clean (up from 57.9%).
- **Priority**: HIGH (process)

### 6.2 Pin Zubarev citation
- **Source**: Formula audit (MODERATE violation #1)
- **What**: Cite Zubarev, "Nonequilibrium Statistical Thermodynamics" (Consultants Bureau, 1974), with specific equation number for alpha = S/(S_max - S), OR explicitly derive from first principles.
- **Priority**: HIGH (blocks ALPHA-EFF from PASS promotion)

### 6.3 Rename COLLECTIVE-NS
- **Source**: Formula audit (MODERATE violation #2)
- **What**: The S45 computation named "collective phonon pair creation" implements single-particle Bogoliubov. Either rename to "condensate-destruction pair creation" or implement the actual Anderson-Bogoliubov GRPA.
- **Priority**: MEDIUM

### 6.4 Torsion code validation on known space
- **Source**: Formula audit (MINOR violation, S46 Recommendation 4)
- **What**: Compute T for S^1, S^3, or flat torus using the same code path. Compare to known analytic result.
- **Priority**: LOW

### 6.5 Fill working paper stub sections
- **Source**: Formula audit (S46 Recommendation 5)
- **What**: W3-R2 (MKK-TENSION), W3-R3 (TRUNCATED-TORSION), W4-R1 (RUNNING-GN), W4-R3 (GL-GGE) have incomplete working paper entries.
- **Priority**: LOW

### 6.6 Dissolution entropy computation (NOT STARTED in S45)
- **Source**: Working paper (W5-4), Hawking review (Section II)
- **What**: Script `s45_dissolution_entropy.py` was created but computation was not run. Complete it.
- **Input data**: Script exists in `tier0-computation/`
- **Priority**: LOW
- **Pre-registered gate**: Original S45 gate.

---

## 7. CORRECTIONS NEEDED (formula audit items, S44 corrections)

### 7.1 S44 Euler deficit claim DISPROVED
- **Source**: EULER-DEFICIT-45, Working paper
- **Status**: CORRECTED in S45. S44 claim "deficit / |E_cond| = 1.000" was ensemble artifact. Actual value: 0.843. No further action needed.

### 7.2 Vol(SU(3)) -- both prior values wrong
- **Source**: Working paper Section "Corrections to S44"
- **Status**: CORRECTED in S45. Correct value: 8 sqrt(3) pi^4 = 8480.67 (Weyl integration formula). Neither 1349.74 nor 8880.93 from prior sessions. However, Vol(SU(3)) does NOT enter either M_KK route (confirmed `vol_affects_MKK = False`). Moot for gate verdicts. No further action needed.

### 7.3 E_cond 0.115 was dead code
- **Source**: ECOND-RECONCILE-45
- **Status**: CORRECTED in S45. The value at line 105 of s42_gge_energy.py was never propagated. All downstream scripts use correct ED value 0.13685 from npz. No reruns needed. No further action.

### 7.4 Heat kernel reclassifications
- **Source**: HEAT-KERNEL-AUDIT-45
- **Status**: d_s is Tier 3 ARTIFACT. Analytic torsion is Tier 3 ARTIFACT. Spectral action is Tier 1 VALID. Seeley-DeWitt a_n are Tier 2 APPROXIMATION. These are PERMANENT reclassifications. No further action except awareness.

### 7.5 DIMFLOW-44 reclassified as artifact
- **Source**: Heat kernel audit
- **Status**: The S44 computation that extracted n_s = 0.961 at sigma = 1.10 was operating on a Tier 3 artifact. The sigma value has no intrinsic meaning on the truncated spectrum. This n_s route is CLOSED. No further action except not citing DIMFLOW-44 as an n_s result.

---

## 8. THE -0.68 UNIVERSALITY RESULT

### Summary
- **Source**: `s45_tinfoil_minus068.md`
- **Finding**: n_s(tau_back -> infinity) = -0.6815, matching the KZ formula with d=3 (sector count B1/B2/B3 from [iK_7, D_K] = 0) and z=2 (Bogoliubov), nu = 0.6301 (3D XY). Agreement: 0.13% at tau_back = 0.50. d_eff converges to 3 from above.
- **Significance**: This is the WRONG answer for the CMB (gap of 1.65 units to Planck 0.965) but it identifies WHAT the framework IS: a d=3 Kibble-Zurek system. The 1.65-unit gap is the transfer function problem.
- **Implication for S46**: The hose-count mechanism (alpha ~ +1 to +2) must shift n_s from -0.68 to +0.96. This requires alpha - beta change of +1.65 units.

---

## 9. FULL ITEM LIST (every single item, numbered, with source)

### CC / Tau-Stabilization
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 1 | Self-consistent Delta(tau) for q-theory | ALL (7/7 convergence) | All reviewers | CRITICAL |
| 2 | T3-T5 crossing lock-on | Spectral-geometer VII, Tesla | Spectral-geometer | HIGH |
| 3 | Number-projected BCS for trace-log | Nazarewicz WF2 | Nazarewicz | HIGH |
| 4 | GCM zero-point correction | Nazarewicz WF3 | Nazarewicz | MEDIUM |
| 5 | Multi-T Jacobson sector-by-sector | Hawking I.1 | Hawking | MEDIUM |
| 6 | Bayesian GP emulator for tau* | Nazarewicz WF4 | Nazarewicz | MEDIUM |
| 7 | Perturbative stability of q-theory | CC balance sheet VII.D | Multiple | LOW |
| 8 | Continuum limit spectral zeta | CC balance sheet VII.B, Tesla | Multiple | MEDIUM |
| 9 | Parametric resonance at q-theory crossing | Hawking IV.2(c) | Hawking | LOW |

### n_s Crisis
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 10 | Hose-count pair mode counting | ALL (6/7 convergence) | All | CRITICAL |
| 11 | K_7 selection rules halving hose count | Nazarewicz III.B, Hose addendum | Nazarewicz | HIGH |
| 12 | Anderson-Bogoliubov GRPA collective | Nazarewicz WF5, Quicklook | Nazarewicz | HIGH |
| 13 | Spectral current j(lambda, tau) | Spectral-geometer IV | Spectral-geometer | HIGH |
| 14 | Richardson-Gaudin pair transfer from GGE | Nazarewicz WF1 | Nazarewicz | HIGH |
| 15 | GGE beat-to-4D transfer function | Tesla 4, Hawking IV.2 | Tesla | MEDIUM |
| 16 | Quasi-static phase at q-theory equilibrium | Hawking VI.1 | Hawking | HIGH |
| 17 | GGE Caldeira-Leggett friction on modulus | Hawking VI.2, Nazarewicz WF6 | Hawking, Nazarewicz | MEDIUM |
| 18 | Non-singlet mode dissipation | Nazarewicz WF6 | Nazarewicz | MEDIUM |
| 19 | Landau-Zener k-dependent adiabaticity | Tesla 3.2, Nazarewicz III.C, Hose addendum | Tesla, Nazarewicz | MEDIUM |
| 20 | Forward/backward pair creation | FWD-BWD addendum | User/team | MEDIUM |
| 21 | Band inversion Berry phase | Tesla 4.2 | Tesla | MEDIUM |
| 22 | Anomalous dispersion of RPA collective | Tesla 3.3 | Tesla | MEDIUM |
| 23 | Pair-mode 1D topology | Hawking IV.3 | Hawking | MEDIUM |
| 24 | Fabric tessellation modulation | Hose addendum, Tesla 3.2 | Tesla | MEDIUM |

### DM/DE
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 25 | Zubarev derivation + Keldysh cross-check | ALL (5/7 convergence) | Multiple | HIGH |
| 26 | DESI DR2/3 w_a = 0 test | Quicklook, Tesla, Working paper | Multiple | HIGH (ext) |
| 27 | ALPHA-ENV void vs filament | Quicklook | S42 queue | LOW |
| 28 | Island formula GGE-to-Gibbs | Hawking VI.2 | Hawking | LOW |
| 29 | Dissolution singlet-only partition | Hawking II.3 | Hawking | LOW |

### Structural / NCG
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 30 | Omega^1_D classification (342 directions) | Connes II, Way 1 | Connes | HIGH |
| 31 | Independent geometric a_2 | Spectral-geometer WF4, Connes V.D, HK audit | Multiple (4/7) | HIGH |
| 32 | Twisted BdG spectral triple | Connes III, Way 2 | Connes | MEDIUM |
| 33 | Connes distance on truncated Jensen SU(3) | Spectral-geometer WF5 | Spectral-geometer | MEDIUM |
| 34 | max_pq_sum = 6 computation | Spectral-geometer, Connes, Tesla (3/7) | Multiple | MEDIUM |
| 35 | Spectral form factor | Spectral-geometer WF6 | Spectral-geometer | LOW |
| 36 | Peter-Weyl censorship (killed S45) | Working paper W4-R5 | S45 plan | LOW |
| 37 | Spectral zeta at non-integer s | Spectral-geometer WF3 | Spectral-geometer | LOW |
| 38 | SA on combined (tau) x (Omega^1_D) space | Connes II | Connes | MEDIUM |
| 39 | Pseudo-Riemannian triple on SU(2,1) | Connes IV | Connes | LOW |
| 40 | Spectral action as entropy (Paper 20) | Hawking VI.3 | Hawking | LOW |

### Diagnostics / Infrastructure
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 41 | Formula audit 80% compliance target | Formula audit | gen-physicist | HIGH |
| 42 | Pin Zubarev citation | Formula audit | gen-physicist | HIGH |
| 43 | Rename COLLECTIVE-NS | Formula audit | gen-physicist | MEDIUM |
| 44 | Torsion code validation on known space | Formula audit | gen-physicist | LOW |
| 45 | Fill working paper stubs | Formula audit | gen-physicist | LOW |
| 46 | Dissolution entropy computation | Working paper, Hawking | Multiple | LOW |
| 47 | Spectral Penrose reference dictionary | Working paper SPECTRAL-PENROSE-45 | gen-physicist | LOW |

### Tesla-Specific
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 48 | Three-Frequency Universe: cavity radiation pattern | Tesla 4 | Tesla | MEDIUM |
| 49 | Phonon magnetic moment from Hall conductivity | Tesla 4.3 | Tesla | LOW |
| 50 | Kapitza/parametric resonance from GGE beats | Tesla 3.7 | Tesla | LOW |

### Nazarewicz-Specific
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 51 | Cranking inertia for velocity reduction | Nazarewicz WF6 | Nazarewicz | MEDIUM |
| 52 | GPV fragmentation pattern in RG framework | Nazarewicz III.A | Nazarewicz | HIGH |
| 53 | Bayes factor q-theory vs spectral action | Nazarewicz IV | Nazarewicz | LOW |

### Hawking-Specific
| # | Item | Source | Proposer | Priority |
|:--|:-----|:-------|:---------|:---------|
| 54 | Bekenstein bound on singlet torsion | Hawking I.2 | Hawking | LOW |
| 55 | GSL consistency at q-theory crossing | Hawking V.1 | Hawking | LOW |
| 56 | WCH consistency at tau* = 0.209 | Hawking V.2 | Hawking | LOW |
| 57 | Spectral action = von Neumann entropy identity | Hawking VI.3 | Hawking | LOW |
| 58 | Trans-Planckian universality for n_s robustness | Hawking V.3 | Hawking | LOW |

---

## 10. PRE-REGISTERED GATES SUMMARY

| Gate ID | PASS Criterion | FAIL Criterion | Source |
|:--------|:--------------|:---------------|:-------|
| Q-THEORY-SELFCONSISTENT-46 | tau* in [0.17, 0.21] with self-consistent Delta(tau) | No crossing in [0.05, 0.35] | Quicklook, CC balance sheet |
| Q-THEORY-T3T5-46 | tau* locks onto [0.188, 0.194] | tau* outside [0.15, 0.25] | Spectral-geometer VII |
| HOSE-COUNT-46 | n_s in [0.955, 0.975] from pair mode count ~ k^alpha, alpha in [0.8, 1.2] | alpha < 0.5 or alpha > 2.0 | Hose-count addendum |
| COLLECTIVE-NS-46 | n_s in [0.955, 0.975] from Anderson-Bogoliubov GRPA | n_s outside [0.80, 1.10] | Working paper V.C |
| SPECTRAL-FLOW-NS-46 | alpha in [0.8, 1.2] from spectral current | alpha outside [0.5, 2.0] | Spectral-geometer IV |
| QUASISTATIC-NS-46 | N_e > 10 during dwell at tau* | N_e < 0.1 | Hawking VI.1 |
| ZUBAREV-DERIVATION-46 | Zubarev and Keldysh agree (< 50%) | Disagree by > 50% | ALPHA-EFF-45, formula audit |
| DESI-WA-46 | \|w_a\| < 0.3 in DESI DR2 | \|w_a\| > 1.0 at > 3 sigma | TWO-FLUID-DESI-45 |
| OMEGA-CLASSIFY-46 | Any tachyonic direction at fold not at round | All directions massive at all tau | Connes Way 1 |
| TWIST-BDG-46 | KO-dim preserved, Krein signature (3,1) | Axioms violated | Connes Way 2 |
| A2-GEOMETRIC-46 | Spectral a_2 agrees with geometric within 30% | Disagreement > 100% | Spectral-geometer WF4, HK audit |
| MULTI-JACOBSON-QTHEORY-46 | All 8 sectors \|rho_k(tau*)\| < 0.1 | Any \|rho_k\| > 1.0 | Hawking I.1 |
| FWD-BWD-NS-46 | n_s in [0.955, 0.975] | n_s outside [0.80, 1.10] | FWD-BWD addendum |
| GGE-FRICTION-46 | (diagnostic) | (diagnostic) | Hawking VI.2 |
| DISSOLUTION-STRUCTURE-46 | S_singlet/S_page > 0.95 | (INFO at ~ 0.47) | Hawking II.3 |

---

## 11. PRIORITY TRIAGE

### CRITICAL (must be in W1)
1. Self-consistent Delta(tau) for q-theory [item 1]
2. Hose-count pair mode counting [item 10]

### HIGH (W1-W2)
3. Independent geometric a_2 [item 31] (analytic, zero cost)
4. Anderson-Bogoliubov GRPA collective n_s [item 12]
5. Spectral current j(lambda, tau) for n_s [item 13]
6. Richardson-Gaudin pair transfer from GGE [item 14]
7. K_7 selection rules [item 11] (quick analytic check)
8. Quasi-static phase at q-theory equilibrium [item 16]
9. Zubarev derivation + Keldysh cross-check [item 25]
10. Omega^1_D classification [item 30]
11. T3-T5 crossing lock-on [item 2]
12. Number-projected BCS [item 3]
13. Pin Zubarev citation [item 42]
14. GPV fragmentation in RG framework [item 52]

### MEDIUM (W3-W5)
15-34: All MEDIUM items from the full list.

### LOW (later sessions or as time permits)
35-58: All LOW items from the full list.

---

*This document is the SOLE INPUT for S46 planning. Every item extracted from every S45 document is listed above. Items not in this document will not be planned.*
