# Session 46 — Wave 2: HIGH (5 tasks, parallel)

**Date**: 2026-03-15
**Source**: `sessions/session-plan/session-46-plan.md`, `sessions/session-plan/s46-rollup-from-s45.md`
**Prerequisite**: Wave 1 Decision Point 1 complete. Wave 2 configuration depends on Q-THEORY-SELFCONSISTENT and HOSE-COUNT verdicts.

---

## W2-1: Spectral Flow n_s from Eigenvalue Velocities (SPECTRAL-FLOW-NS-46)

**Agent**: `spectral-geometer`
**Model**: opus
**Rollup item**: #13 (spectral current j(lambda, tau))
**Gate ID**: SPECTRAL-FLOW-NS-46

**Prompt**:

You are computing the spectral current j(lambda, tau) and extracting the effective hose-count exponent alpha from eigenvalue velocities. This provides an independent route to n_s that weights modes by their VELOCITY in the spectral plane, producing an intermediate alpha between the single-particle extreme (alpha = 6) and the collective extreme (alpha = 0).

**Background.** S45 established that the internal KZ spectral index is n_s = -0.68 (d=3 universality). The Planck target n_s = 0.965 requires a +1.65 shift, decomposed as n_s - 1 = alpha - beta where beta = 1.68 from d=3 KZ. The spectral current weights modes not by their degeneracy (Weyl, alpha = 6) nor by a uniform weight (collective, alpha = 0), but by their SPEED of motion in the spectral plane during the transit. Modes near van Hove singularities (where d(lambda)/d(tau) = 0) contribute zero spectral current; modes moving fast through the fold contribute proportionally to their velocity. This intermediate weighting may give alpha ~ 1.

**Computation Steps**:

1. **Load data.** Eigenvalues lambda_k(tau) from `tier0-computation/s44_dos_tau.npz` and `tier0-computation/s44_vanhove_track.npz` (van Hove singularity tracking). Import from `tier0-computation/canonical_constants.py`: tau_fold, a2_fold.

2. **Compute eigenvalue velocities.** For each of the 992 eigenvalues, compute the spectral velocity:

   v_k(tau) = d(lambda_k)/d(tau)

   Use centered differences from the tau grid in s44_dos_tau.npz. At tau_fold = 0.19, record v_k for all modes. Modes near van Hove singularities have v_k -> 0.

3. **Define spectral current.** The spectral current at wavenumber k = sqrt(C_2(p,q)) is:

   j(k, tau) = sum_{k' in sector(k)} d_{k'} * |v_{k'}(tau)| * |beta_{k'}|^2

   where |beta_{k'}|^2 is the Bogoliubov pair creation coefficient from `tier0-computation/s45_kz_ns.npz` and d_{k'} is the Peter-Weyl degeneracy. The spectral current measures the TOTAL pair creation flux at each Casimir wavenumber, weighted by spectral velocity.

4. **Extract alpha.** Plot j(k) vs k on log-log axes. Fit j(k) ~ k^{alpha_flow}. The velocity weighting |v_k| suppresses van Hove modes (v_k = 0) and enhances fast-moving modes, tilting alpha from the Weyl value of 6 toward a lower value. Report alpha_flow and the goodness of fit.

5. **Compute n_s.** With beta = 1.68 (d=3 KZ):

   n_s = 1 + alpha_flow - beta

   Report n_s and compare to Planck 0.965.

6. **Fourier analysis.** Compute the Fourier transform of j(lambda, tau) in lambda:

   J(k_lambda, tau) = integral j(lambda, tau) * exp(i k_lambda lambda) d(lambda)

   The power spectrum |J(k_lambda)|^2 at the fold gives the spectral distribution of pair creation in the eigenvalue-frequency domain. This is a Tier 1 quantity (computed from eigenvalues and their derivatives, no model assumptions).

7. **Van Hove correlation.** At the fold, which fraction of the total spectral current comes from modes within 10% of a van Hove singularity? If this fraction is > 50%, the van Hove structure dominates the spectral flow and alpha_flow is determined by the distribution of van Hove singularities across Casimir wavenumbers.

**Formula Audit**:
- (a) j(k, tau) = sum d_k |v_k| |beta_k|^2. [j] = M_KK (velocity has dimensions M_KK; beta dimensionless; d_k dimensionless).
- (b) [v_k] = d(M_KK)/d(tau) = M_KK (tau is dimensionless).
- (c) Limiting case: v_k = 0 for all k (static spectrum) gives j = 0 (no spectral flow). Constant v_k recovers Weyl-weighted pair creation.
- (d) Citation: Berry-Tabor (1977) spectral flow; S44 VAN-HOVE-TRACK-44; S45 tinfoil -0.68.

**Pre-registered gate SPECTRAL-FLOW-NS-46**:
- PASS: alpha_flow in [0.8, 1.2]
- FAIL: alpha_flow outside [0.5, 2.0]

**Input files**:
- `tier0-computation/s44_dos_tau.npz` — eigenvalue evolution
- `tier0-computation/s44_vanhove_track.npz` — van Hove singularity tracking
- `tier0-computation/s45_kz_ns.npz` — Bogoliubov beta coefficients
- `tier0-computation/s42_hauser_feshbach.npz` — sector labels, Casimir values
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_spectral_flow_ns.py`
- Data: `tier0-computation/s46_spectral_flow_ns.npz`
- Plot: `tier0-computation/s46_spectral_flow_ns.png`

**Working paper section**: W2-R1

**Critical notes**:
- Read `sessions/session-45/s45_tinfoil_minus068.md` FIRST for the d=3 KZ universality result.
- The spectral velocity v_k(tau) is a DERIVATIVE quantity. Use sufficient numerical precision (centered differences, step h small enough).
- Van Hove singularities are where v_k = 0 or diverges. They are tracked in s44_vanhove_track.npz.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

## W2-2: Richardson-Gaudin Pair Transfer Spectral Function (RG-PAIR-TRANSFER-46)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Rollup item**: #14 (pair transfer from GGE)
**Gate ID**: subsumes HOSE-COUNT-46

**Prompt**:

You are computing the pair transfer spectral function S(omega, k) from the 8-mode Richardson-Gaudin GGE state. This provides the most physical count of independent pair creation channels because it uses the ACTUAL post-transit state (the GGE), not the ground state.

**Background.** The GGE state is NOT the BCS ground state. It is a highly excited state with 59.8 quasiparticle pairs (S38), described by 8 conserved Richardson-Gaudin integrals. Pair transfer FROM the GGE involves de-excitation with different selection rules than pair creation from the ground state. In nuclear physics, the pair transfer spectral function S(omega, k) from a deformed nucleus reveals the Giant Pairing Vibration (GPV) fragmentation pattern: the pair-addition strength concentrates into 2-4 fragments per sector rather than a single collective peak.

The pair transfer spectral function is:

    S(omega, k) = sum_n |<n|P^+_k|GGE>|^2 * delta(omega - omega_n)

where P^+_k is the pair creation operator at Casimir wavenumber k, |GGE> is the post-transit GGE state, and |n> are the eigenstates of the RG Hamiltonian. For the Richardson-Gaudin integrable model, the pair creation operator decomposes as:

    P^+ = sum_a sum_k g_a(k) / (z_a - epsilon_k)

where z_a are the Richardson parameters (pair rapidities) and epsilon_k are the single-particle energies.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_gge_energy.npz`: GGE occupation numbers, energies, Richardson-Gaudin parameters. From `tier0-computation/s42_hauser_feshbach.npz`: eigenvalues, pairing interaction V_{kl}, sector labels, K_7 charges.

2. **Construct the Richardson-Gaudin Hamiltonian.** For the 8-mode system (4 B2 + 1 B1 + 3 B3):

   H_RG = sum_k epsilon_k n_k + g * sum_{k != l} P^+_k P^-_l

   where P^+_k = c_{k,up} c_{k,down} creates a pair in mode k, epsilon_k = |lambda_k| at the fold, and g = g_eff from the pairing interaction.

3. **Solve the RG equations.** The Richardson equations for N_pair pairs on M = 8 levels:

   1/g + sum_k 1/(2 epsilon_k - z_a) = sum_{b != a} 2/(z_b - z_a)   for a = 1, ..., N_pair

   Find the pair rapidities z_a for the GGE state (not the ground state -- the GGE has specific occupation numbers that select a particular set of rapidities).

4. **Compute pair transfer matrix elements.** For each sector with Casimir k:

   |<n|P^+_k|GGE>|^2 = |det(G(n,k)) / det(G(GGE))|^2

   where G is the Gaudin matrix and the formula follows from the Slavnov determinant representation (Richardson-Gaudin, Dukelsky-Pittel-Sierra review, Paper 17 in researchers/Landau/).

5. **Count peaks per sector.** For each k, compute S(omega, k) as a function of omega. Count the number of distinct peaks above 10% of the maximum. Plot peak count vs k. Fit n_peaks(k) ~ k^{alpha_RG}.

6. **Extract alpha.** The pair transfer spectral function gives the physically correct hose count: each peak corresponds to an independent pair creation channel with its own spectral weight. The exponent alpha_RG should agree with the BdG pair mode count from W1-2 if the physics is consistent.

7. **Nuclear comparison.** In sd-shell nuclei (your expertise), the GPV fragmentation gives 2-4 fragments per major shell. The SU(3) analog: B2 (4 modes) should give 2-3 fragments; B1 (1 mode) gives 1; B3 (3 modes) gives 1-2. Total per Casimir quantum number k: scales as sqrt(d(p,q)) from the nuclear sum rule. Compare.

**Formula Audit**:
- (a) S(omega, k) = sum |<n|P^+_k|GGE>|^2 delta(omega - omega_n). [S] = M_KK^{-1} (spectral weight per energy). [omega] = M_KK.
- (b) [z_a] = M_KK (pair rapidities have energy dimensions). [g] = M_KK (coupling). Richardson equation dimensionally consistent.
- (c) Limiting case: In the ground state (all pairs in lowest levels), S(omega) has a single peak at omega = 2*Delta (pair-addition energy). In the limit g -> 0 (no pairing), S(omega) is a sum of delta functions at each 2*epsilon_k.
- (d) Citation: Richardson (1963), Paper 16; Dukelsky-Pittel-Sierra (2004), Paper 17; Ring-Schuck Ch. 8 (pair transfer); Cappuzzello et al. (2015), Paper 23 (GPV).

**Pre-registered gate**: Subsumes HOSE-COUNT-46 (same alpha counting, different method). Same criteria: alpha in [0.8, 1.2].

**Input files**:
- `tier0-computation/s42_gge_energy.npz` — GGE state, occupations, temperatures
- `tier0-computation/s42_hauser_feshbach.npz` — eigenvalues, V matrix, sector labels
- `tier0-computation/canonical_constants.py`
- `researchers/Landau/16_1963_Richardson_Exact_Eigenstates_Pairing_Hamiltonian.md`
- `researchers/Landau/17_2004_Dukelsky_Pittel_Sierra_Richardson_Gaudin_Review.md`

**Output files**:
- Script: `tier0-computation/s46_rg_pair_transfer.py`
- Data: `tier0-computation/s46_rg_pair_transfer.npz`
- Plot: `tier0-computation/s46_rg_pair_transfer.png`

**Working paper section**: W2-R2

**Critical notes**:
- The Richardson equations are EXACT for integrable pairing Hamiltonians. No approximation.
- The GGE is characterized by specific occupation numbers, not by a single temperature. The pair rapidities for the GGE differ from the ground-state rapidities.
- Read Papers 16 and 17 FIRST (Richardson solution, Dukelsky review).
- The GPV fragmentation prediction (alpha ~ 1 from nuclear sum rules) is the physical expectation from your nuclear structure expertise.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

## W2-3: Quasi-Static Phase at q-Theory Equilibrium (QUASISTATIC-NS-46)

**Agent**: `hawking-theorist`
**Model**: opus
**Rollup item**: #16 (quasi-static deceleration)
**Gate ID**: QUASISTATIC-NS-46

**Prompt**:

You are computing the dwell time and e-fold count at the q-theory equilibrium point tau* = 0.209 (or the W1-1 self-consistent value if available). If the modulus lingers near tau* with near-zero velocity, a quasi-de Sitter phase emerges whose perturbation spectrum can produce n_s near the Planck value.

**Background.** The n_s crisis has two independent parameters: the spectral tilt of the internal pair creation (beta = 1.68 from d=3 KZ) and the transfer function from internal to 4D Friedmann dynamics. All prior n_s computations assumed the modulus transits through the fold at terminal velocity v_terminal = 26.5 M_KK (S38), giving epsilon_H = v^2 / (2 H^2) = 3.0 (far from slow-roll). But if the q-theory equilibrium at tau* acts as an ATTRACTOR, the modulus decelerates near tau*, reducing epsilon_H.

The key S45 result: epsilon_V = 0.016 at the q-theory equilibrium (from QNM-NS-45). The potential IS flat enough for Planck. The problem is the KINETIC ENERGY: epsilon_H = 3.0. If the modulus can be trapped at tau* even temporarily (N_e > 10 e-folds), the kinetic energy redshifts away (epsilon_H ~ exp(-3 N_e)) and the potential flatness determines n_s.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s45_qnm_ns.npz`: epsilon_V at tau* = 0.209, potential landscape. From `tier0-computation/s45_qtheory_bcs.npz`: q-theory crossing profile rho_gs(tau). From `tier0-computation/s44_friedmann_bcs_audit.npz`: Friedmann equation parameters, H(tau), v(tau). Import from `tier0-computation/canonical_constants.py`: H_fold, v_terminal, tau_fold, G_DeWitt.

2. **Equation of motion near tau*.** The modulus tau obeys the Klein-Gordon equation in the FRW background:

   G_DeWitt * (d^2 tau / dt^2) + 3 H (d tau / dt) + dV_eff/d tau = 0

   where G_DeWitt = 5.0 is the DeWitt kinetic coefficient (canonical_constants.py), H is the Hubble parameter, and V_eff(tau) is the q-theory effective potential. Near tau*, expand V_eff as:

   V_eff(tau) = (1/2) m_eff^2 (tau - tau*)^2

   Extract m_eff from the second derivative of rho_gs(tau) at tau*.

3. **Damping analysis.** The Hubble friction term 3 H (d tau / dt) damps the modulus velocity. The critical question: is the damping sufficient to trap the modulus? Compute:

   gamma_H = 3 H / (2 G_DeWitt)    (Hubble friction rate)
   omega_osc = m_eff / sqrt(G_DeWitt)    (oscillation frequency)

   If gamma_H > omega_osc: overdamped (modulus stalls at tau*). N_e is large.
   If gamma_H < omega_osc: underdamped (modulus oscillates through tau*). N_e < 1.
   If gamma_H ~ omega_osc: critical damping. Intermediate N_e.

4. **Dwell time computation.** Solve the modulus EOM numerically from initial conditions (tau_init = 0, v_init = v_terminal = 26.5) through tau*. The dwell time dt_dwell is the interval during which |tau - tau*| < tau_width, where tau_width is defined by V_eff(tau* +/- tau_width) = 0.01 * V_eff(tau_fold).

5. **E-fold count.** N_e = integral(H dt) during the dwell phase. Compute:

   N_e = integral_{t_enter}^{t_exit} H(t) dt

   where t_enter and t_exit bracket the quasi-static phase.

6. **n_s from quasi-static phase.** If N_e > 10:

   n_s = 1 - 6 epsilon_V + 2 eta_V

   where epsilon_V = (1/(2 G_DeWitt)) (V'/V)^2 and eta_V = (1/G_DeWitt) (V''/V) evaluated at tau*. With epsilon_V = 0.016 (from S45 QNM-NS-45), this gives:

   n_s = 1 - 6(0.016) + 2 eta_V = 0.904 + 2 eta_V

   Compute eta_V and report n_s.

7. **Velocity damping factor.** If N_e < 10, compute the velocity reduction factor:

   v_exit / v_enter = exp(-gamma_H * dt_dwell)

   The S45 assessment requires 829x velocity reduction for n_s = 0.965. Report whether the q-theory equilibrium provides sufficient deceleration.

**Formula Audit**:
- (a) N_e = integral H dt. [N_e] dimensionless. [H] = M_KK (in natural units). [t] = M_KK^{-1}.
- (b) epsilon_V = (V')^2 / (2 G_DeWitt V^2). [V'] = M_KK^5. [V] = M_KK^4. [G_DeWitt] dimensionless. epsilon_V dimensionless. Verified.
- (c) Limiting case: V_eff = constant (pure de Sitter) gives epsilon_V = 0, n_s = 1. V_eff = m^2 tau^2 (chaotic inflation) gives n_s = 1 - 2/N_e.
- (d) Citation: Mukhanov-Chibisov (1981); Hawking (1982); Stewart-Lyth (1993); Jacobson (1995) for thermodynamic equilibrium interpretation.

**Pre-registered gate QUASISTATIC-NS-46**:
- PASS: N_e > 10 during dwell at tau*
- FAIL: N_e < 0.1

**Input files**:
- `tier0-computation/s45_qnm_ns.npz` — epsilon_V at tau*
- `tier0-computation/s45_qtheory_bcs.npz` — rho_gs(tau) profile
- `tier0-computation/s44_friedmann_bcs_audit.npz` — Friedmann parameters
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_quasistatic_ns.py`
- Data: `tier0-computation/s46_quasistatic_ns.npz`
- Plot: `tier0-computation/s46_quasistatic_ns.png`

**Working paper section**: W2-R3

**Critical notes**:
- The existing S22d result: epsilon_V = 0.016 at the q-theory crossing. This is already flat enough for Planck. The entire question is whether epsilon_H can be reduced from 3.0 to < 0.1.
- The q-theory equilibrium (rho_gs = 0) is a LOCAL property of the potential landscape. Whether the modulus actually decelerates there depends on the GLOBAL dynamics (how fast it arrives).
- The 829x velocity reduction needed (S45 assessment) is a severe requirement. Report the computed reduction factor honestly.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

## W2-4: Inner Fluctuation Module Omega^1_D Classification (OMEGA-CLASSIFY-46)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Rollup item**: #30 (Omega^1_D 342 directions)
**Gate ID**: OMEGA-CLASSIFY-46

**Prompt**:

You are classifying the 342-dimensional inner fluctuation module Omega^1_D(A_F) on the Jensen-deformed SU(3) at the fold. The 169 quadratic directions from the order-one violation are uncomputed scalar fields. If any direction is tachyonic at the fold but not at the round metric, this constitutes a NEW tau-stabilization mechanism bypassing all 31 spectral action closures.

**Background.** S45 WEAK-ORDER-ONE-45 established that the order-one condition [[D_K, a], b^0] = 0 fails MAXIMALLY on D_K(tau): the gauge-gauge block is the worst violator (GG/Full = 1.000), the violation scales as (5/sqrt(3))*exp(tau), and the Bochniak-Sitarz weak order-one condition (Paper 25) is violated with GG:GS:SS = 1:1/2:1/4.

In the Chamseddine-Connes-van Suijlekom (CCS 2013, Paper 23) framework, when the order-one condition fails, the inner fluctuation D -> D + A + JAJ^{-1} acquires quadratic terms:

    A_quad = sum_{i,j} c_{ij} [D, a_i] [D, a_j]

The total inner fluctuation module has dimension:
- 173 linear directions (standard inner fluctuations)
- 169 quadratic directions (CCS 2013 quadratic fluctuations)
- 342 total at the (1,0) representation

Each direction corresponds to a scalar field. The spectral action S(D + A) expanded to second order in A around the vacuum D_K(tau) gives the mass-squared matrix M^2. The eigenvalues of M^2 determine whether each direction is massive (M^2 > 0), massless (M^2 = 0, Goldstone), or tachyonic (M^2 < 0, instability).

**The connection to tau-stabilization.** If a direction has M^2 < 0 at the fold (tau = 0.19) but M^2 > 0 at the round metric (tau = 0), the fold is UNSTABLE in the inner-fluctuation moduli space. The spectral action as a function of tau alone (the 31 closures) is monotone, but the spectral action on the COMBINED (tau) x (Omega^1_D) space may have a saddle point at the fold. This would be an entirely new stabilization mechanism.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: eigenvalues, commutant structure, algebra generators. From `tier0-computation/s45_weak_order_one.npz`: order-one violation data, Omega^1_D dimension count. Import from `tier0-computation/canonical_constants.py`.

2. **Construct the algebra A_F and its inner fluctuations.** The finite algebra is A_F = C(SU(3)/Ad, M_16(C)) (the algebra of 16x16 matrix-valued functions on SU(3) modulo adjoint action). The inner fluctuations at the (1,0) representation are:

   A = sum_i a_i [D_K, b_i]     (linear, 173 directions)
   A_quad = sum_{i,j} c_{ij} [D_K, a_i] [D_K, a_j]     (quadratic, 169 directions)

   Enumerate a basis {phi_alpha} for alpha = 1, ..., 342 of the full module Omega^1_D(A_F).

3. **Mass-squared matrix.** For each pair (alpha, beta), compute:

   M^2_{alpha,beta} = (d^2 / d(t_alpha) d(t_beta)) S(D_K + sum_gamma t_gamma phi_gamma) |_{t=0}

   This is the Hessian of the spectral action in the inner fluctuation directions. For the finite discrete spectrum:

   M^2_{alpha,beta} = sum_k d_k * [phi_alpha, phi_beta]_k / lambda_k^2

   where [phi_alpha, phi_beta]_k is the matrix element of the second-order perturbation in the k-th eigenvalue. Compute numerically using second-order perturbation theory on the finite Dirac operator.

4. **Diagonalize M^2.** Find the eigenvalues {mu_alpha^2} and eigenvectors of the 342 x 342 mass matrix.

5. **Tachyonic directions.** Count the number of negative eigenvalues at tau_fold = 0.19. Repeat at tau = 0 (round). If any direction is tachyonic at the fold but massive at the round, the fold is an INSTABILITY in the inner fluctuation landscape.

6. **Gauge quantum numbers.** For each direction phi_alpha, compute its transformation under the commutant Inn(A_F). Classify into irreducible representations. Identify which directions are gauge singlets (potential Higgs-like fields) and which transform non-trivially.

7. **Connection to HESS-40.** S40 computed the Hessian of the spectral action in the TAU direction (1D), finding all 22 transverse eigenvalues positive at the fold (minimum +1572). The Omega^1_D directions are ORTHOGONAL to tau. Verify that the combined (tau) x (Omega^1_D) Hessian block-diagonalizes (no tau-phi cross terms) or compute the cross terms.

**Formula Audit**:
- (a) M^2_{alpha,beta} = d^2 S / d(t_alpha) d(t_beta). [M^2] = M_KK^2 (mass-squared). [S] dimensionless.
- (b) [phi_alpha] has dimensions such that t_alpha * phi_alpha is dimensionless (phi is an operator perturbation). [t_alpha] = M_KK^{-1} if phi is in M_KK units.
- (c) Limiting case: For the standard NCG-SM (order-one satisfied), the 169 quadratic directions vanish and the linear directions give the Higgs doublet (4 real, 2 massive). Verify that the 173 linear directions reduce to the known SM content in the appropriate limit.
- (d) Citation: Chamseddine-Connes-van Suijlekom (2013), Paper 23 (inner fluctuations without order-one); CCS (2013), Paper 24 (Pati-Salam application); Bochniak-Sitarz (2021), Paper 25 (weak order-one); S45 WEAK-ORDER-ONE-45.

**Pre-registered gate OMEGA-CLASSIFY-46**:
- PASS: Any tachyonic direction at fold but not at round
- FAIL: All directions massive at all tau

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz` — eigenvalues, algebra structure
- `tier0-computation/s45_weak_order_one.npz` — order-one violation data
- `tier0-computation/canonical_constants.py`
- `researchers/Connes/23_2013_Chamseddine_Connes_vSuijlekom_Inner_Fluctuations.md`
- `researchers/Connes/24_2013_Chamseddine_Connes_vSuijlekom_Pati_Salam.md`
- `researchers/Connes/25_2021_Bochniak_Sitarz_Weak_Order_One.md`

**Output files**:
- Script: `tier0-computation/s46_omega_classify.py`
- Data: `tier0-computation/s46_omega_classify.npz`
- Plot: `tier0-computation/s46_omega_classify.png`

**Working paper section**: W2-R4

**Critical notes**:
- Read Papers 23, 24, 25 FIRST. Paper 23 defines the quadratic inner fluctuations. Paper 24 applies them to Pati-Salam. Paper 25 defines weak order-one.
- The 342-dimensional module has never been classified on D_K. This is genuinely new territory.
- If a tachyonic direction exists, this opens an entirely new stabilization pathway that bypasses all 31 spectral action closures. Report carefully.
- The computation is algebraically intensive but finite (the Dirac operator is a matrix). Use the existing infrastructure for D_K at the fold.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.

---

## W2-5: Number-Projected BCS for Trace-Log (NUMBER-PROJECTED-BCS-46)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Rollup item**: #3 (PBCS for trace-log)
**Gate ID**: None explicit; diagnostic for tau* uncertainty

**Prompt**:

You are implementing number-projected BCS (PBCS) on the 8-mode system to eliminate the spurious particle-number fluctuations that shifted E_cond by 59% between BCS and ED (S45 crosscheck). The PBCS-corrected trace-log provides a more accurate q-theory crossing tau* with controlled uncertainty.

**Background.** S45 ECOND-RECONCILE-45 found that E_cond differs by 16% between BCS (0.115 M_KK, 5-mode) and ED (0.137 M_KK, 8-mode, canonical value). The BCS gap equation conserves particle number only ON AVERAGE, not exactly. In nuclear physics, number projection eliminates this error and typically shifts the condensation energy by 10-30% for systems with ~10 pairs.

The PBCS ground state is:

    |PBCS> = P_N |BCS> / ||P_N |BCS>||

where P_N = (1/2pi) integral_0^{2pi} exp(i phi (N_hat - N)) d(phi) is the number projection operator, N is the target particle number, and |BCS> = product_k (u_k + v_k c^+_k c^+_{-k}) |0>.

For the Richardson-Gaudin integrable model (which this system is, by S38), the exact ground state is available through the Richardson solution. PBCS provides an intermediate approximation that is (a) more accurate than BCS, (b) less computationally intensive than full ED for larger systems, and (c) gives a smooth interpolation parameterized by the projection.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: eigenvalues, V matrix, BCS coherence factors (u_k, v_k). From `tier0-computation/s42_gge_energy.npz`: exact occupation numbers from ED. Import from `tier0-computation/canonical_constants.py`: E_cond, E_cond_ED_8mode, Delta_0_GL.

2. **BCS solution.** At the fold (tau = 0.19), solve the BCS gap equation for the 8-mode system (4 B2 + 1 B1 + 3 B3). Record the BCS coherence factors (u_k, v_k), gap Delta_BCS, and condensation energy E_cond_BCS.

3. **Number projection.** Implement the Pfaffian overlap formula for PBCS:

   <PBCS|H|PBCS> = (1/2pi) integral_0^{2pi} integral_0^{2pi} <BCS(phi)|H|BCS(phi')> * exp(i(phi-phi')(N_hat-N)) d(phi) d(phi') / (normalization)

   For the 8-mode system, the gauge-rotated BCS state is |BCS(phi)> = product_k (u_k + v_k e^{2i phi} c^+_k c^+_{-k}) |0>.

   The overlap <BCS(phi)|BCS(phi')> = product_k (u_k^2 + v_k^2 e^{2i(phi'-phi)}) is a Pfaffian.

   Discretize the phi integral on a 64-point grid and compute numerically.

4. **PBCS trace-log.** With the PBCS occupation numbers n_k^{PBCS} = <PBCS|n_k|PBCS>, compute the PBCS-corrected trace-log:

   TL_PBCS(tau) = (1/2) sum_k d_k * ln((lambda_k^2 + Delta_PBCS^2 * (2 n_k^{PBCS} - 1)^2) / mu_ref^2)

   Compare to the BCS trace-log (S45) and the ED trace-log (exact).

5. **Shift in tau*.** Recompute the q-theory Gibbs-Duhem crossing rho_gs(tau) = 0 using PBCS occupations instead of BCS. Report:
   - tau*(BCS) from S45 = 0.209
   - tau*(PBCS) from this computation
   - tau*(ED) if computable
   - Shift delta_tau = tau*(PBCS) - tau*(BCS)

6. **Uncertainty estimate.** The difference |tau*(PBCS) - tau*(BCS)| provides a lower bound on the systematic uncertainty from particle-number fluctuations. The difference |tau*(PBCS) - tau*(ED)| provides an upper bound on the PBCS residual error. Report the 68% confidence interval for tau*.

**Formula Audit**:
- (a) E_PBCS = <PBCS|H|PBCS> / <PBCS|PBCS>. [E] = M_KK. The Pfaffian overlap is dimensionless.
- (b) [u_k] = [v_k] = dimensionless (coherence factors, u^2 + v^2 = 1). [phi] = radians.
- (c) Limiting case: For Delta -> 0, BCS and PBCS give the same result (v_k = 0, no pairs). For a single pair (N_pair = 1), PBCS is exact.
- (d) Citation: Ring-Schuck Ch. 11 (number projection); Anguiano et al. (2001) PRC 63, 034310 (Pfaffian overlap); S36 ED-CONV-36 (exact E_cond).

**Pre-registered gate**: No explicit gate. Diagnostic: report delta_tau and whether tau* shifts toward tau_fold = 0.190.

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz` — eigenvalues, V matrix
- `tier0-computation/s42_gge_energy.npz` — ED occupations for comparison
- `tier0-computation/s45_qtheory_bcs.npz` — BCS crossing at 0.209
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_number_projected_bcs.py`
- Data: `tier0-computation/s46_number_projected_bcs.npz`
- Plot: `tier0-computation/s46_number_projected_bcs.png`

**Working paper section**: W2-R5

**Critical notes**:
- This is standard nuclear structure methodology (your core expertise). Ring-Schuck Ch. 11.
- The 8-mode system is small enough that both PBCS and ED are feasible. The value of PBCS is its scalability to max_pq_sum = 6 (where ED becomes prohibitive).
- The Pfaffian overlap formula avoids explicit construction of the projected state in Fock space.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
