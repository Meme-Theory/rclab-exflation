# Session 46 — Wave 3: MEDIUM (6 tasks, parallel)

**Date**: 2026-03-15
**Source**: `sessions/session-plan/session-46-plan.md`, `sessions/session-plan/s46-rollup-from-s45.md`
**Prerequisite**: Waves 1-2 complete. Results from W1 (tau*, alpha) and W2 (n_s routes, PBCS) available.

---

## W3-1: GPV Fragmentation Pattern in Richardson-Gaudin Framework (GPV-FRAGMENTATION-46)

**Agent**: `nazarewicz-nuclear-structure-theorist`
**Model**: opus
**Rollup item**: #52 (GPV fragmentation -> alpha)

**Prompt**:

You are computing the Giant Pairing Vibration (GPV) fragmentation pattern on the SU(3) BCS system using the Richardson-Gaudin framework. The GPV fragmentation determines how pair-addition strength distributes across energy levels -- the nuclear analog of the hose count.

**Background.** In nuclear physics (your core expertise), the GPV is the collective pair-addition mode that exhausts most of the pair-transfer sum rule. In deformed nuclei, the GPV fragments into multiple components because the pairing interaction couples levels within the same j-shell but is blocked across shells by angular momentum selection rules. Cappuzzello et al. (2015, Paper 23) observed GPV fragmentation in ^{14}C + p -> ^{15}C, with 2-4 fragments carrying 85% of the pair-addition strength. Fortunato et al. (2019, Paper 24) extended this to heavy nuclei. The recent Paper 25 (2025) analyzes many-body fragmentation from first principles.

For the SU(3) system: the 8-mode BCS model has 3 sectors (B1, B2, B3) that play the role of nuclear shells. The pairing interaction V_{kl} couples modes within each sector (strong) and between sectors (weaker, controlled by K_7 selection rules). The GPV fragmentation pattern determines how many independent pair creation channels exist per Casimir quantum number -- the hose count exponent alpha.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: eigenvalues, V matrix, sector labels, K_7 charges. From `tier0-computation/s38_cc_instanton.npz`: instanton parameters, pair susceptibility.

2. **Pair-addition operator.** Define P^+_k = c^+_{k,up} c^+_{k,down} for each of the 8 BCS-active modes. The total pair-addition operator is P^+ = sum_k P^+_k. The sector-restricted operators are P^+_{B1}, P^+_{B2}, P^+_{B3}.

3. **Pair-addition strength function.** In the Richardson-Gaudin exact solution, compute:

   S(E) = sum_n |<n, N+2 | P^+ | 0, N>|^2 * delta(E - E_n)

   where |0, N> is the ground state with N pairs and |n, N+2> are eigenstates with N+2 pairs. For the 8-mode system, use exact diagonalization in the Fock space (2^8 = 256 states).

4. **Fragmentation analysis.** Count the number of peaks in S(E) above 10% of the maximum. Compute the fragmentation ratio f = S_max / S_total (fraction of strength in the largest peak). In nuclear physics, f ~ 0.5-0.8 for moderately deformed nuclei. Plot S(E) as a function of energy for comparison with nuclear GPV spectra.

5. **Sector-resolved fragmentation.** Repeat step 3 for each sector separately: S_{B1}(E), S_{B2}(E), S_{B3}(E). The sector-resolved fragmentation gives the per-sector hose count.

6. **Casimir scaling.** For each sector (p,q), the Casimir k = sqrt(C_2). Plot the number of fragments per sector vs k. Fit n_frag(k) ~ k^{alpha_GPV}. Compare to the W1-2 result (BdG pair mode count) and the W2-2 result (RG pair transfer).

7. **Sum rule.** Verify the energy-weighted sum rule: integral omega * S(omega) d(omega) = <[P^-, [H, P^+]]> / 2. This sum rule is model-independent and provides a cross-check on the computation.

**Formula Audit**:
- (a) S(E) = sum_n |<n|P^+|0>|^2 delta(E - E_n). [S] = M_KK^{-1}. [E] = M_KK.
- (b) Sum rule: integral omega S(omega) d(omega) = <[P^-, [H, P^+]]>/2 in [M_KK^2].
- (c) Limiting case: For a single level (1-mode), S(E) = delta(E - 2*epsilon) (one peak, no fragmentation). For non-interacting levels (g=0), S(E) = sum delta(E - 2*epsilon_k) (one peak per level, complete fragmentation).
- (d) Citation: Cappuzzello et al. (2015), Paper 23; Fortunato et al. (2019), Paper 24; GPV Fragmentation (2025), Paper 25; Ring-Schuck Ch. 6 (pair vibrations).

**Pre-registered gate**: Diagnostic (no explicit PASS/FAIL). Report alpha_GPV for constraint map.

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s38_cc_instanton.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Landau/23_2015_Cappuzzello_Giant_Pairing_Vibration_14C_15C.md`
- `researchers/Landau/24_2019_Fortunato_GPV_Heavy_Nuclei.md`
- `researchers/Landau/25_2025_GPV_Fragmentation_Many_Body.md`

**Output files**:
- Script: `tier0-computation/s46_gpv_fragmentation.py`
- Data: `tier0-computation/s46_gpv_fragmentation.npz`
- Plot: `tier0-computation/s46_gpv_fragmentation.png`

**Working paper section**: W3-R1

---

## W3-2: Twisted BdG Spectral Triple Construction (TWIST-BDG-46)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Rollup item**: #32 (twisted spectral triple with Delta as twist)
**Gate ID**: TWIST-BDG-46

**Prompt**:

You are constructing the twisted BdG spectral triple (A_F, H_BdG, D_{BdG,sigma}, J_BdG, gamma_BdG) and verifying the NCG axioms. The twist converts the Riemannian BdG triple (from S35) to a Krein-space triple, potentially bridging internal BCS condensation (Riemannian) to emergent spacetime (Lorentzian).

**Background.** Three papers develop the twist program: Filaci-Martinetti (2023, Paper 30, critical survey), Devastato-Lizzi-Martinetti-Kurkov (2021, Paper 33, minimal twist SM field content), and Martinetti (2026, Paper 44, Krein structure). The key result from Paper 44: the minimal twist induces an indefinite inner product on H, converting the Hilbert space to a Krein space. The unitary group of this Krein space contains U(2,2), recovering the conformal group of Minkowski spacetime.

For the framework: D_K on SU(3) is Riemannian. The BdG extension (S35) doubles the Hilbert space H -> H_BdG = H + H^* with the Nambu-Gorkov structure. The twist automorphism sigma, generated by the BCS order parameter Delta, converts the BdG triple to a Krein-space triple where the signature encodes the particle-hole structure.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: Dirac operator D_K, J operator, grading gamma. S35 BdG spectral triple results (from session notes).

2. **BdG Hilbert space.** Construct H_BdG = H + H^* where H is the 16-component spinor space. The BdG Dirac operator is:

   D_BdG = ((D_K, Delta), (Delta^*, -D_K^*))

   where Delta is the gap matrix (16 x 16, known from s42_hauser_feshbach.npz).

3. **Twist automorphism.** Define sigma: A_F -> A_F as the inner automorphism generated by the unitary part of the BCS transformation:

   sigma(a) = U_BCS * a * U_BCS^{-1}

   where U_BCS = product_k (u_k + v_k c^+_k c^+_{-k}) is the BCS unitary in operator form. For the finite algebra, represent U_BCS as a matrix on H_BdG.

4. **Twisted Dirac operator.** Following Paper 44:

   D_{sigma} = D_BdG + sigma^{-1} [D_BdG, sigma] + sigma^{-1} [D_BdG, sigma]^*

   Compute D_{sigma} explicitly as a matrix.

5. **Krein structure.** The twist induces the Krein fundamental symmetry eta = sigma^2 (Paper 44, Theorem 3.2). The Krein inner product is:

   <xi, zeta>_eta = <xi, eta * zeta>_H

   Compute eta and verify:
   - eta^2 = 1 (fundamental symmetry)
   - eta D_{sigma} = D_{sigma} eta (or anti-commutes, depending on the grading)
   - The Krein signature (p, q) where p = number of positive eigenvalues of eta, q = number of negative

6. **Axiom verification.** Check the 7 axioms of the real spectral triple (Connes 1995):
   - (A1) D is self-adjoint (in the Krein sense)
   - (A2) Compact resolvent (automatic for finite-dimensional)
   - (A3) [a, [D, b]] bounded for all a, b in A (order-one)
   - (A4) J^2 = epsilon, JD = epsilon' DJ, J gamma = epsilon'' gamma J (KO-dimension signs)
   - (A5) Poincare duality (K-theoretic)
   - (A6) Orientability (gamma exists)
   - (A7) Regularity (automatic for finite-dimensional)

   Report which axioms hold, which fail, and the KO-dimension modulo 8.

7. **Target Krein signature.** Paper 44 showed that the minimal twist of the SM spectral triple gives Krein signature (3,1) -- matching Lorentzian spacetime. Does the BdG twist on SU(3) give (3,1)? Or (4,4) from the BdG doubling? Report.

**Formula Audit**:
- (a) D_{sigma} = D_BdG + [corrections from twist]. [D] = M_KK.
- (b) [eta] dimensionless (unitary operator). Krein norm dimensionless.
- (c) Limiting case: sigma = 1 (no twist, Delta = 0) recovers the original spectral triple. Verify axioms reduce to S7 results.
- (d) Citation: Connes (1995) axioms; Martinetti (2026), Paper 44 (Krein structure); Filaci-Martinetti (2023), Paper 30 (twist survey); Devastato et al. (2021), Paper 33 (minimal twist SM).

**Pre-registered gate TWIST-BDG-46**:
- PASS: KO-dimension preserved AND Krein signature matches (3,1)
- FAIL: Axioms violated

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/s45_weak_order_one.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Connes/30_2023_Filaci_Martinetti_Critical_Survey_Twisted_Spectral_Triples.md`
- `researchers/Connes/33_2021_Devastato_Lizzi_Martinetti_Kurkov_Minimal_Twist_SM_Field_Content.md`
- `researchers/Connes/44_2026_Martinetti_Twisted_Standard_Model_Krein_Structure.md`

**Output files**:
- Script: `tier0-computation/s46_twist_bdg.py`
- Data: `tier0-computation/s46_twist_bdg.npz`
- Plot: `tier0-computation/s46_twist_bdg.png`

**Working paper section**: W3-R2

---

## W3-3: GGE Caldeira-Leggett Friction on Tau Modulus (GGE-FRICTION-46)

**Agent**: `hawking-theorist`
**Model**: opus
**Rollup items**: #17 (Caldeira-Leggett), #51 (cranking inertia)
**Gate ID**: GGE-FRICTION-46 (diagnostic)

**Prompt**:

You are modeling the 8 Richardson-Gaudin modes as a finite heat bath providing Caldeira-Leggett friction on the tau modulus. The question is whether the GGE modes can slow the modulus enough to reduce epsilon_H from 3.0 to < 0.1, enabling the quasi-static n_s mechanism from W2-3.

**Background.** The modulus tau transits through the fold at terminal velocity v_terminal = 26.5 M_KK (S38). The Hubble friction (3H dot-tau term) provides damping rate gamma_H = 3H / (2 G_DeWitt) but this is insufficient (S38 W4: transit completes with 3.7% backreaction). The 8 GGE modes are a FINITE environment coupled to the modulus through the tau-dependent eigenvalues. In condensed matter, a quantum system coupled to N oscillators experiences Caldeira-Leggett friction with dissipation rate gamma_CL proportional to the spectral density J(omega) of the bath.

For this system: the "bath" is the 8 Richardson-Gaudin modes with frequencies omega_k (known from S38) and coupling to the modulus through d(lambda_k)/d(tau) (known from S44). The cranking inertia (Nazarewicz suggestion, item #51) is the many-body analog: the effective mass of the modulus increases because dragging the modulus through the BCS medium requires rearranging the pair structure.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s45_gge_beating.npz`: GGE beat frequencies, mode amplitudes. From `tier0-computation/s44_friedmann_bcs_audit.npz`: Friedmann dynamics, H(tau), v(tau). From `tier0-computation/s42_gge_energy.npz`: GGE occupation numbers, temperatures, mode energies. Import from `tier0-computation/canonical_constants.py`: H_fold, v_terminal, G_DeWitt, omega_PV, omega_att.

2. **Bath spectral density.** Define the Caldeira-Leggett spectral density of the 8-mode GGE bath:

   J(omega) = sum_k |g_k|^2 * delta(omega - omega_k)

   where g_k = d(lambda_k)/d(tau)|_{fold} is the coupling of mode k to the modulus, and omega_k are the GGE mode frequencies (Richardson-Gaudin). Broaden the delta functions to Lorentzians with width gamma_k (natural linewidth from anharmonicity, estimate from S37 instanton data).

3. **Ohmic vs super-Ohmic.** Classify J(omega): if J(omega) ~ omega (Ohmic), friction is memoryless. If J(omega) ~ omega^s with s > 1 (super-Ohmic), friction has memory effects. With 8 modes, the spectral density is discrete. Fit the envelope.

4. **Caldeira-Leggett friction coefficient.** The friction coefficient is:

   gamma_CL = pi * J(omega_tau) / (2 * m_eff * omega_tau)

   where omega_tau = m_eff * v_terminal is the characteristic frequency of the modulus motion and m_eff = G_DeWitt = 5.0 is the modulus effective mass.

5. **Velocity reduction.** Solve the damped modulus equation:

   G_DeWitt * d^2(tau)/dt^2 + (gamma_H + gamma_CL) * d(tau)/dt + dV/d(tau) = 0

   with initial conditions tau(0) = 0, v(0) = v_terminal. Compute the velocity at tau = tau* and the reduction factor v(tau*) / v_terminal.

6. **Cranking inertia.** The Inglis-Belyaev cranking formula for the effective mass enhancement is:

   M_crank(tau) = G_DeWitt + 2 * sum_{k,l} |<k|dH/d(tau)|l>|^2 / (E_k - E_l)^2 * (n_k - n_l)

   where the sum is over BdG quasiparticle states. This is the MANY-BODY contribution to the modulus inertia. Compute M_crank at the fold.

7. **829x test.** The S45 assessment: need 829x velocity reduction for n_s = 0.965. Report:
   - gamma_CL / gamma_H (ratio of CL friction to Hubble friction)
   - v(tau*) / v_terminal (velocity reduction factor)
   - Whether 829x is achievable from 8 modes (likely not -- but report the shortfall)

**Formula Audit**:
- (a) J(omega) = sum |g_k|^2 delta(omega - omega_k). [J] = M_KK^2 * M_KK^{-1} = M_KK. [g_k] = M_KK (d(lambda)/d(tau)).
- (b) gamma_CL = pi J(omega) / (2 m omega). [gamma_CL] = M_KK (rate). Verified.
- (c) Limiting case: g_k = 0 (no coupling) gives gamma_CL = 0 (free transit). g_k -> infinity gives gamma_CL -> infinity (frozen modulus).
- (d) Citation: Caldeira-Leggett (1983) Physica A 121, 587; Inglis (1956) Phys. Rev. 103, 1786 (cranking formula); Belyaev (1959); S38 W4 (backreaction).

**Pre-registered gate GGE-FRICTION-46**: Diagnostic. Report gamma_CL and velocity reduction factor.

**Input files**:
- `tier0-computation/s45_gge_beating.npz`
- `tier0-computation/s44_friedmann_bcs_audit.npz`
- `tier0-computation/s42_gge_energy.npz`
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_gge_friction.py`
- Data: `tier0-computation/s46_gge_friction.npz`
- Plot: `tier0-computation/s46_gge_friction.png`

**Working paper section**: W3-R3

---

## W3-4: GGE Beat-to-4D Transfer Function (TRANSFER-FUNCTION-46)

**Agent**: `tesla-resonance`
**Model**: opus
**Rollup items**: #15 (GGE-to-4D transfer), #48 (Three-Frequency Universe)
**Gate ID**: None explicit; diagnostic

**Prompt**:

You are computing the 4D power spectrum from the convolution of the 3 GGE beat frequencies with the Friedmann dynamics during transit. Every failed n_s route examined one end of the convolution (internal spectrum OR 4D dynamics). This computation combines both.

**Background.** S45 established three beat frequencies from the GGE energy spectrum:
- B2-B1 = 0.052 M_KK (slow beat, period 120.8 t_KK)
- B2-B3 = 0.266 M_KK (medium beat, period 23.6 t_KK)
- B1-B3 = 0.318 M_KK (fast beat, period 19.7 t_KK)

These beats modulate the vacuum energy rho_vac(t) during transit, imprinting a characteristic pattern on the Friedmann expansion history a(t). The 4D density perturbations delta_rho/rho at each comoving wavenumber k are determined by the transfer function:

    delta(k) = integral T(k, omega) * rho_vac(omega) d(omega)

where T(k, omega) is the Friedmann transfer function that converts internal frequency omega to 4D wavenumber k. The tilt n_s is the slope of |delta(k)|^2 on a log-log plot.

The d=3 KZ universality (n_s = -0.68) describes the internal spectrum rho_vac(omega). The transfer function T(k, omega) maps this to 4D. The full n_s is:

    n_s - 1 = [tilt of rho_vac(omega)] + [tilt of T(k, omega)]

The first term is -1.68 (known). The second is the +1.65 gap that must be filled.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s45_gge_beating.npz`: GGE beat frequencies, amplitudes, phases. From `tier0-computation/s44_friedmann_bcs_audit.npz`: Friedmann equation, H(t), a(t) during transit.

2. **Internal vacuum energy spectrum.** Construct rho_vac(t) during transit as the sum of 3 beating cosines:

   rho_vac(t) = sum_{i=1}^3 A_i * cos(omega_i * t + phi_i)

   with amplitudes A_i and frequencies omega_i from the GGE beat data. The envelope is determined by the transit profile (S38 dynamics).

3. **Friedmann transfer function.** During transit, the scale factor a(t) obeys:

   (da/dt)^2 / a^2 = (8 pi G_N / 3) * rho_total(t)

   where rho_total includes the spectral action vacuum energy, the modulus kinetic energy, and the GGE beating component. Solve the Friedmann equation numerically with the beating source.

4. **Mode function evolution.** For each comoving mode k, the curvature perturbation zeta_k obeys:

   d^2(zeta_k)/dt^2 + (3H + d(ln epsilon)/dt) d(zeta_k)/dt + (k^2/a^2) zeta_k = 0

   Solve for 100 modes spanning k = 10^{-5} to 10^{-1} Mpc^{-1} (the CMB range in comoving coordinates). The initial conditions are Bunch-Davies vacuum.

5. **Power spectrum.** Compute P(k) = |zeta_k|^2 at the end of transit. Fit n_s - 1 = d ln P / d ln k at the pivot scale k_pivot = 0.05 Mpc^{-1}.

6. **Three-Frequency Universe.** The cavity radiation pattern (Tesla concept): if the 3 GGE beats resonate with the Friedmann dynamics, the power spectrum acquires a characteristic 3-frequency modulation. Compute the positions of the 3 beat peaks in k-space and their amplitudes relative to the smooth spectrum. These are potentially observable features in the CMB at high multipoles.

7. **Transfer function tilt.** Extract the tilt of T(k, omega) independent of the internal spectrum. Does T provide the +1.65 shift? Report.

**Formula Audit**:
- (a) Friedmann equation: H^2 = (8pi G_N / 3) rho. [H] = s^{-1} or M_KK. [rho] = GeV^4 or M_KK^4. G_N in appropriate units.
- (b) [k] = Mpc^{-1}. [zeta] dimensionless. [P(k)] = Mpc^3 (dimensionless power spectrum P = k^3 |zeta|^2 / (2 pi^2) is dimensionless).
- (c) Limiting case: rho_vac = constant gives de Sitter (n_s = 1 exactly). rho_vac ~ e^{-t/tau} gives n_s = 1 - 2/tau (slow-roll).
- (d) Citation: Mukhanov (2005), "Physical Foundations of Cosmology"; Baumann (2009) TASI lectures; Tesla S44 "Three-Frequency Universe" concept.

**Pre-registered gate**: None explicit. Diagnostic: report n_s from the full convolution.

**Input files**:
- `tier0-computation/s45_gge_beating.npz`
- `tier0-computation/s44_friedmann_bcs_audit.npz`
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_transfer_function.py`
- Data: `tier0-computation/s46_transfer_function.npz`
- Plot: `tier0-computation/s46_transfer_function.png`

**Working paper section**: W3-R4

---

## W3-5: Connes Distance on Truncated Jensen SU(3) (CONNES-DISTANCE-46)

**Agent**: `connes-ncg-theorist`
**Model**: opus
**Rollup item**: #33 (distance formula on truncated Jensen SU(3))
**Gate ID**: None explicit; structural diagnostic

**Prompt**:

You are computing the Connes spectral distance d(e, g) on the truncated Jensen-deformed SU(3), providing the effective diameter, anisotropy, and a well-defined distance analog of spectral dimension.

**Background.** The Connes distance formula:

    d(x, y) = sup{ |f(x) - f(y)| : ||[D, f]|| <= 1 }

defines a metric from a spectral triple (A, H, D). For the truncated D_K at max_pq_sum = 5, the algebra A is finite-dimensional and the supremum is over a finite set of functions. Paper 28 (Connes-van Suijlekom 2021, spectral truncations) proves that the truncated distance converges to the geodesic distance as the truncation level increases.

For the Jensen-deformed SU(3): the metric g(tau) deforms the root directions relative to the Cartan directions. This creates an anisotropic metric. The Connes distance at the fold (tau = 0.19) should reflect this anisotropy: distances along root directions are shorter (e^{-tau}) than along Cartan directions.

**Computation Steps**:

1. **Load data.** From `tier0-computation/s42_hauser_feshbach.npz`: Dirac operator D_K at the fold, algebra representation. Import from `tier0-computation/canonical_constants.py`: tau_fold.

2. **Define test points.** Choose 8 group elements g_i in SU(3): the identity e, the 6 root-direction exponentials exp(t * X_alpha) for the 6 roots, and one Cartan direction exponential exp(t * H_1). Set t = 0.1 (small displacement).

3. **Compute [D, f] for algebra elements.** For each f in the truncated algebra (functions on SU(3) restricted to the max_pq_sum = 5 truncation), compute the commutator [D_K, f] as a matrix. The operator norm ||[D_K, f]|| is the largest singular value.

4. **Optimize.** For each pair (e, g_i), find:

   d(e, g_i) = max_{f : ||[D,f]|| <= 1} |f(e) - f(g_i)|

   This is a linear programming problem: maximize |f(e) - f(g_i)| subject to the constraint that the largest singular value of [D, pi(f)] does not exceed 1, where pi(f) is the representation of f on H.

5. **Distance matrix.** Compute the 8x8 distance matrix d(g_i, g_j). Report:
   - Effective diameter: max_{i,j} d(g_i, g_j)
   - Anisotropy ratio: d(root direction) / d(Cartan direction)
   - tau dependence: repeat at tau = 0 (round, expect isotropic) and tau = 0.30

6. **Comparison to geodesic.** The geodesic distance on SU(3) with the Jensen metric is known analytically. Compare d_Connes to d_geodesic. The ratio d_Connes / d_geodesic quantifies the truncation's effect on the geometry (Paper 28 convergence theorem).

**Formula Audit**:
- (a) d(x,y) = sup |f(x)-f(y)| over ||[D,f]|| <= 1. [d] = M_KK^{-1} (length). [f] dimensionless. [D] = M_KK.
- (b) The constraint ||[D,f]|| <= 1 has dimension M_KK, so |f(x)-f(y)| <= ||[D,f]|| * L ~ M_KK * L, giving d ~ M_KK^{-1}. Verified.
- (c) Limiting case: For a commutative spectral triple (functions on M), d recovers the geodesic distance (Connes 1994, Theorem 1).
- (d) Citation: Connes (1994) "Noncommutative Geometry"; Connes-van Suijlekom (2021), Paper 28; Hekkelman-McDonald (2024), Paper 37.

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz`
- `tier0-computation/canonical_constants.py`
- `researchers/Connes/28_2021_Connes_van_Suijlekom_Spectral_Truncations.md`

**Output files**:
- Script: `tier0-computation/s46_connes_distance.py`
- Data: `tier0-computation/s46_connes_distance.npz`
- Plot: `tier0-computation/s46_connes_distance.png`

**Working paper section**: W3-R5

---

## W3-6: Dirac Spectrum at max_pq_sum = 6 (MAX-PQ-SUM-6)

**Agent**: `gen-physicist`
**Model**: opus
**Rollup item**: #34 (extend truncation, check d_Weyl convergence)
**Gate ID**: None explicit; infrastructure

**Prompt**:

You are extending the Dirac spectrum computation from max_pq_sum = 5 (992 modes) to max_pq_sum = 6 and tracking convergence of all derived quantities. This is the most computationally intensive task in the session.

**Background.** The entire framework's spectral data comes from the truncation at max_pq_sum = 5, which includes representations (p,q) with p + q <= 5. This gives 992 eigenvalues. At max_pq_sum = 6, new representations include (6,0), (5,1), (4,2), (3,3), (0,6), (1,5), (2,4) and their conjugates, adding sectors with dim^2 up to 7^2 * 7^2 = 2401 for (6,0). The total mode count increases substantially.

The S45 heat kernel audit showed that d_Weyl = 6.81 at max_pq_sum = 5, compared to the continuum value d_Weyl = 8. The deficit quantifies the truncation error. At max_pq_sum = 6, d_Weyl should be closer to 8. If it is not, the truncation error is non-perturbative.

The 0.83-decade M_KK tension between gravity and Kerner routes (S42) may be a truncation artifact. If a_2 increases significantly at max_pq_sum = 6, M_KK(gravity) decreases and the tension narrows.

**Computation Steps**:

1. **Enumerate new representations.** At max_pq_sum = 6, the new (p,q) pairs are all pairs with p + q = 6: (6,0), (5,1), (4,2), (3,3), (0,6), (1,5), (2,4). Compute dim(p,q) = (p+1)(q+1)(p+q+2)/2 for each. Total new modes = sum dim^2.

2. **Construct D_K at max_pq_sum = 6.** Using the existing tier1_dirac_spectrum.py infrastructure (if available) or constructing from the Lie algebra representation theory:
   - For each new (p,q), construct the representation matrices of the 8 SU(3) generators in the dim(p,q)-dimensional space.
   - Construct the Dirac operator D_K = sum gamma^a e_a^i nabla_i on the spinor bundle tensored with the representation.
   - Diagonalize to get eigenvalues lambda_k.

3. **Eigenvalue statistics.** Compute at tau = 0.19 (fold):
   - Total mode count N_6
   - Weyl counting dimension d_Weyl = lim_{Lambda -> inf} N(Lambda) / Lambda^d (from fitting N(Lambda) vs Lambda)
   - Seeley-DeWitt coefficients a_0 = sum d_k, a_2 = sum d_k / lambda_k^2, a_4 = sum d_k / lambda_k^4
   - Compare to max_pq_sum = 5 values (a_0 = 6440, a_2 = 2776.17, a_4 = 1350.72)

4. **Taylor coefficient ratios.** For the spectral action Taylor expansion (S45 UNEXPANDED-SA-45 structural theorem), compute the ratio |c_{n+1}/c_n| for n = 0, ..., 10. If these ratios are growing with n at max_pq_sum = 6 (asymptotic onset), the Taylor expansion is becoming asymptotic rather than convergent, signaling non-perturbative corrections.

5. **M_KK update.** From the new a_2, extract M_KK(gravity) = sqrt(1 / (48 pi G_N a_2)). Report the updated M_KK and the change in the 0.83-decade tension.

6. **Convergence diagnostics.** Plot a_0, a_2, a_4, d_Weyl as functions of max_pq_sum = 3, 4, 5, 6 (values at 3 and 4 from earlier sessions if available, otherwise omit). Does a_2 appear to converge? What is the extrapolation to max_pq_sum -> infinity?

**Formula Audit**:
- (a) D_K = sum gamma^a e_a^i (partial_i + omega_i). [D] = M_KK. [gamma] dimensionless. [e_a^i] = M_KK (vielbein). [omega_i] = M_KK (spin connection).
- (b) a_n = sum_k d_k / lambda_k^{2n} [dimensionless in M_KK units for even n].
- (c) Limiting case: Round SU(3) (tau = 0) has additional symmetry; the spectrum should be more degenerate. Verify degeneracy structure.
- (d) Citation: S7-S8 (Dirac spectrum construction); S20a (Riemann tensor verification); S42 (CONST-FREEZE-42).

**Pre-registered gate**: None explicit. Diagnostics: d_Weyl closer to 8? a_2 increasing? M_KK tension narrowing?

**Input files**:
- `tier0-computation/s42_hauser_feshbach.npz` — existing spectrum for comparison
- `tier0-computation/s42_constants_snapshot.npz` — a_0, a_2, a_4 at max_pq_sum = 5
- `tier0-computation/canonical_constants.py`

**Output files**:
- Script: `tier0-computation/s46_max_pq_sum_6.py`
- Data: `tier0-computation/s46_max_pq_sum_6.npz`
- Plot: `tier0-computation/s46_max_pq_sum_6.png`

**Working paper section**: W3-R6

**Critical notes**:
- This computation is EXPENSIVE. At max_pq_sum = 5, runtime is ~8.7s per s-value. At max_pq_sum = 6, the matrix dimensions are larger. Use the GPU (RX 9070 XT, 17 GB VRAM) if the matrix fits.
- Compute at tau_fold = 0.19 first. If successful, add tau = 0 and tau = 0.30 for convergence diagnostics.
- Use `"phonon-exflation-sim/.venv312/Scripts/python.exe"` for execution.
