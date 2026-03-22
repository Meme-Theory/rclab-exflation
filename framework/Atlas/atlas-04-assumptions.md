# Atlas D04: Foundation and Assumptions Registry

**Total entries**: 52
**PROVEN**: 15 | **ASSUMED**: 14 | **CONDITIONAL**: 8 | **BROKEN**: 11 | **DISSOLVED**: 4

---

## I. Geometric Foundations

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| G1 | M^4 x K product structure (spacetime is a product of 4D Lorentzian and compact internal) | ASSUMED | Input ansatz; not derived from any deeper principle. Standard KK starting point. | S1 |
| G2 | K = SU(3) specifically | ASSUMED | Selected because it yields SM quantum numbers on Psi_+ = C^16. Not unique: other compact groups might work. The choice is vindicated by the output (KO-dim=6, SM spectrum) but never derived. | S7 |
| G3 | Jensen 1-parameter deformation family (volume-preserving, tau single modulus) | ASSUMED | Simplest volume-preserving deformation on SU(3). The full moduli space is 28-dimensional (5-param Milnor). Off-Jensen directions untested. HESS-40 showed Jensen is a local minimum of S_full in all 28 dimensions, but that is a property of the spectral action, not a selection principle. | S12, S40 |
| G4 | KO-dimension = 6 | PROVEN | Computed from spectral triple on C^16. 10 checks at machine epsilon (<1e-15). Survives pseudo-Riemannian SU(2,1) extension (S46). | S7-8, S46 |
| G5 | SM quantum numbers from Psi_+ = C^16 | PROVEN | 6 multiplets match SM assignments exactly. L-homomorphism failure on C^2 = order-one condition. | S7 |
| G6 | Volume-preserving constraint (det g(tau) = 1) | ASSUMED | Imposed; not derived. Consequence: G_N has zero tau-dependence (exact). Removes one modulus. If relaxed, entire spectral landscape changes. | S12 |
| G7 | Left-invariant metrics only | ASSUMED | Standard for homogeneous spaces. Excludes inhomogeneous deformations. The Peter-Weyl block-diagonal theorem depends on this. | S22b |
| G8 | [J, D_K(tau)] = 0 (CPT exact) | PROVEN | Verified at 79,968 pairs, max deviation 3.29e-13. Structural: J commutes with D_K for any left-invariant metric on SU(3). | S17a |
| G9 | g_1/g_2 = e^{-2tau} (coupling ratio identity) | PROVEN | Derived from Jensen metric structure. Physical ratio g'/g = sqrt(3)*e^{-2tau}. | S17a |
| G10 | D_K block-diagonal in Peter-Weyl basis | PROVEN | Three independent proofs (algebraic, representation-theoretic, numerical at 8.4e-15). Holds for ANY left-invariant metric on ANY compact semisimple Lie group. | S22b |
| G11 | 67/67 Baptista geometry checks | PROVEN | All metric, connection, and curvature identities verified at machine epsilon across 51 tau values. | S17b |
| G12 | Riemann tensor 147/147 checks | PROVEN | All algebraic symmetries and differential Bianchi identities satisfied at machine epsilon. | S20a |

---

## II. BCS / Many-Body Physics

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| B1 | BCS pairing occurs at the van Hove fold | PROVEN | 1D theorem: any g>0 flows to strong coupling (3 independent methods). Van Hove singularity structurally stable (A_2 catastrophe). M_max = 1.674 > 1 threshold. | S35, S36 |
| B2 | Kosmann connection provides the BCS interaction | CONDITIONAL | K_a is the natural connection on the spinor bundle (metric-compatible, anti-Hermitian). V matrix computed correctly after 3 retractions (S23a, S33b, S34). V(B2,B2) = 0.1557, irreducible by Schur. But: "natural" is not "unique." | S23a-S34 |
| B3 | Singlet (0,0) sector dominates pairing | BROKEN | B2 is catalyst; B3 gap entirely proximity-induced (V_B3B3 = 0.059, PASS S46). Multi-sector ED essential. S36 showed full 8x8 M_max = 1.674 vs 4x4 B2-only M_max = 1.351. | S36, S46 |
| B4 | BCS mean-field adequate for N_pair = 1 | CONDITIONAL | N_pair = 1 exact reduction gives 8x8 matrix (agreement 1.2e-14 with full ED). Mean-field gaps overestimate by 60% (S46 PBCS). Adequate for instability criterion (yes/no), unreliable for gap magnitudes. | S39, S46 |
| B5 | AZ class BDI, T^2 = +1 | PROVEN | Corrected from DIII in S11. BDI confirmed with corrected J (S34-35). Pfaffian sgn = -1 at all 34 tau values. Spectral gap open (min 0.819). | S17c, S35 |
| B6 | Cooper pairs carry K_7 charge +/-1/2 | PROVEN | V(q+,q-) = 0 exactly. BCS condensate breaks U(1)_7 spontaneously. [iK_7, D_K] = 0 at all tau. | S34, S35 |
| B7 | Mechanism chain (I-1 -> RPA -> Turing -> WALL -> BCS) unconditional | CONDITIONAL | 5/5 links PASS. But chain assumes tau reaches the fold, which requires either trapping (BROKEN by monotonicity theorem) or transit (dwell time 38,600x too short for equilibrium BCS). Chain describes what CAN happen at the fold, not what DOES happen cosmologically. | S35, S36 |
| B8 | Instanton gas description of transit | CONDITIONAL | S_inst = 0.069, dense gas regime. Reclassified as quantum critical point (S38). But: Schwinger-instanton duality DEAD (coincidence, not identity, S39). GGE permanence RETRACTED (thermalizes in ~6 natural units, S39). The instanton gas is real; its cosmological consequences are unestablished. | S37-S39 |

---

## III. Spectral Action

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| S1 | SA stabilizes tau at the fold | DISSOLVED | Structural monotonicity theorem: S_f(tau) monotonic for ALL smooth monotone cutoffs, ALL Lambda, ALL tau, ALL 10 sectors. 9,600/9,600 checks. The question was reframed: transit paradigm replaces static trapping. | S37 |
| S2 | Cutoff function f is physical (not just mathematical) | ASSUMED | NCG says f is arbitrary (only moments a_0, a_2, a_4 matter in asymptotic expansion). But the SA correlator (S50-51) depends on f' and f''. The choice of f affects quantitative predictions. No selection principle exists. | S37, S51 |
| S3 | SA provides the correct effective action for modulus dynamics | ASSUMED | Standard NCG assumption (Chamseddine-Connes). But F.5 showed SA penalizes BCS pairing (wrong sign, +12.76 anti-trapping, 93x). SA is a spectral moment, not a total energy. The BCS condensation energy is a Fock-space quantity. These are categorically different functionals. | S37 |
| S4 | Perturbative expansion of SA adequate | DISSOLVED | Perturbative Exhaustion Theorem (H1-H5 verified): F_pert is not the true free energy. True free energy has branch structure. But the non-perturbative corrections (instanton, BCS) are 6 orders smaller than SA gradient. | S22c |
| S5 | Seeley-DeWitt a_2k hierarchy physically meaningful | PROVEN | a_4/a_2 = 1000:1 at fold (structural, from 16-component spinor on 8-manifold). a_4(K) = 0 at Einstein point (gauge kinetics emerge from deformation). These are mathematical facts about the heat kernel. | S20a, S33a |

---

## IV. Cosmological Mapping

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| C1 | tau parameterizes cosmic time (tau evolution = cosmic expansion) | ASSUMED | Core framework postulate. tau = 0 is the initial state (round SU(3)); increasing tau drives compactification. The mapping from internal modulus to FRW scale factor is not derived from first principles. | S1 |
| C2 | K_pivot = 2.0 M_KK (tessellation mapping for CMB scales) | BROKEN | Never rigorously derived. SA-Goldstone mixing FAILS at K = 2.0 (convex combination theorem, S51). Physical e-fold mapping gives K = 4.3e-57 M_KK (flat, n_s = 1). No physical mechanism places K at the intermediate K* = 0.087 where n_s = 0.965 works. | S51 |
| C3 | n_s from Ornstein-Zernike propagator on fabric | BROKEN | alpha_s = n_s^2 - 1 identity at 6 sigma from Planck within K^2 propagators (5 independent proofs, permanent theorem). SA-Goldstone mixing achieves n_s = 0.965 only at K < 0.087 M_KK, requiring >= 3.1 e-folds from tau_i <= 1.7e-5 (margin 0.2 e-folds). K_pivot mapping paradox unresolved. | S49-S51 |
| C4 | w_0 from GGE energy/pressure ratio | BROKEN | S42 derived w = -1 + O(10^{-29}). S45 two-fluid model gives w_0 = -0.509. Both excluded: w = -1 contradicts DESI DR2 (w_0 = -0.75); w_0 = -0.509 excluded by BAO chi^2/N = 23.2. The framework cannot simultaneously explain DESI's dynamical DE signal and its own w = -1 prediction. | S42, S50 |
| C5 | w_a = 0 (frozen modulus post-transit) | BROKEN | Triple-locked: trapping + integrability + frozen modulus all force w_a = 0 exactly. DESI DR2 measures w_a = -0.73 +/- 0.27. If DESI is correct, the framework's frozen-modulus assumption is wrong. If DESI's signal is statistical fluctuation, the framework is consistent with LCDM. Either way, the framework makes no dynamical DE prediction. | S50 |
| C6 | eta (baryon asymmetry) from pair-breaking during transit | CONDITIONAL | eta ~ 3.4e-9 (0.75 decades from observed 6.1e-10). Requires exactly 2 pair breaks during transit and specific M_KK. Plausible order-of-magnitude, not a precision prediction. M_KK undetermined. | S42 |
| C7 | CDM from GGE Bogoliubov quasiparticles | CONDITIONAL | T^{0i}_4D = 0 exact (homogeneous creation). sigma/m = 5.7e-51 cm^2/g (collisionless). Correct qualitative behavior (pressureless, collisionless). But: rho_DM/rho_Lambda = 5.4e5 (CC problem in disguise). The DM abundance is not predicted. | S42, S44 |
| C8 | G_N from Sakharov induced gravity | CONDITIONAL | Ratio 2.29 (0.36 OOM) at Lambda = 10 M_KK. Depends on effective 4D UV cutoff, which the framework does not fix. At Lambda = M_Pl: ratio 26.8 (1.43 OOM). Not a prediction; it is a consistency check that passes at the right cutoff. | S44 |
| C9 | sigma_8 = 0.799 from O-Z rigid prediction | PROVEN | Derived from alpha_s = -0.069 with n_s = 0.965. Sits between Planck (0.811) and lensing (0.766). 2.0 sigma from Planck, 1.6 sigma from lensing. Only surviving cosmological prediction. | S50 |

---

## V. Transit / Dynamics

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| T1 | Transit is sudden quench | PROVEN | dt/T_L = 1.25e-5. P_exc = 1.000. Dwell time 38,600x shorter than BCS formation time. The transit through the fold is parametric, not adiabatic. | S36, S38 |
| T2 | GGE forms post-transit | PROVEN | Analytic GGE with lambda_k = -ln|psi_pair[k]|^2. Three distinct Lagrange multipliers reflecting SU(3) branch structure. Product-state (S_ent = 0 identically). | S39 |
| T3 | GGE never thermalizes (Richardson-Gaudin integrability) | BROKEN | V_phys 13% non-separable. Brody beta = 0.633 (63% GOE). t_therm ~ 6 natural units. GGE valid during transit but thermalizes to Gibbs on cosmological timescales (t_therm/t_Hubble = 9e-48). S38 claim of permanent non-thermal relic retracted. | S39 |
| T4 | 59.8 quasiparticle pairs created during transit | PROVEN | From sudden-quench Bogoliubov calculation. N_pair = 1 exact reduction confirmed at 1.2e-14. Pair wavefunction 93% B2, 6.3% B1, 0.7% B3. | S38, S39 |
| T5 | Equilibrium tau-stabilization exists somewhere in moduli space | BROKEN | 27 equilibrium closures across S17-S40. HESS-40: all 22 transverse Hessian eigenvalues positive in full 28D moduli space. Jensen trajectory is robust local minimum of S_full. Constraint surface dimension = zero. No equilibrium mechanism survives. | S40 |
| T6 | Friedmann-BCS coupling can dynamically lock tau | BROKEN | FRIED-39: shortfall 133,200x. Gradient ratio |dV_bare/dtau|/|dE_BCS/dtau| = 6,596 at fold. Spectral action (155,984 modes) overwhelms BCS (8 modes) by construction. | S39 |

---

## VI. NCG / Algebraic Structure

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| N1 | R_{u(2)} as gauge choice (commutant) | PROVEN | R_{u(2)} uniquely gives center = 5, 3 Wedderburn factors matching A_F. Five gauge choices tested systematically. Acts as opposite algebra A_F^o = JA_FJ^{-1}. | S8-9 |
| N2 | Order-one condition extracts A_F = C + H + M3(C) | CONDITIONAL | C + M3(C) extracted (dim 20). H (quaternions) requires bimodule structure. Complete A_F extraction via o-map route identified but never fully computed. Structural obstruction for H identified. | S10 |
| N3 | Spectral triple axioms all satisfied | BROKEN | C-6 gate: 6/7 NCG axioms pass but axiom 5 (orientability for D_total) fails at 4.000. Order-one norm = 3.117 (C-3 FAIL). The D_K satisfies axioms; the full D including finite part does not satisfy all. | S28 |
| N4 | Anderson-Higgs mechanism for U(1)_7 Goldstone | BROKEN | Permanently closed S51. [iK_7, D_K] = 0 prevents gauging at all orders. K_7 is a Kosmann derivative (diffeomorphism), not an inner automorphism (gauge). Three independent proofs (categorical). | S51 |

---

## VII. Specific Claimed Predictions

| # | Assumption | Status | Evidence | Session |
|:--|:-----------|:-------|:---------|:--------|
| P1 | phi_paasch = 1.531580 as physical prediction | DISSOLVED | Mathematical property of Dirac spectrum at tau = 0.15 (z = 3.65). Reclassified from prediction (BF=5) to mathematical property (BF=2). Tau mismatch: BCS at 0.35 initially, later 0.190; phi at 0.15. The phi crossing at tau = 0.211686 (omega_L2/omega_L1 = phi to 4.4e-15) is a geometric identity, not a cosmological prediction. | S12-13, S28, S50 |
| P2 | Leggett mode as physical observable | CONDITIONAL | Q = 670,000 (undamped). Dipolar mass within 18% of 3He analog. But: mass problem 170x (m_required/m_Leggett). No mechanism to make Leggett mode observable at cosmological scales. | S49-S51 |
| P3 | n_s > 1 structural for bare KK tower | PROVEN | Spectral geometer proved the bare Dirac heat kernel on any compact manifold gives n_s >= 1. Red tilt REQUIRES 4D dynamics or correlator mixing. | S51 |
| P4 | All 279 scalar inner fluctuations universally tachyonic | PROVEN | Structural: f' < 0 for monotone cutoff. Gram matrix PSD theorem (kinetic mass always positive). Reinterpreted as transit mechanism. | S46 |

---

## Summary Assessment

The framework's mathematical foundations are remarkably solid. Of 52 entries, 15 are PROVEN at machine epsilon -- these are permanent results about spectral geometry on compact Lie groups that survive regardless of the framework's physical fate. The block-diagonal theorem, the structural monotonicity theorem, the BCS instability theorem, the Anderson-Higgs impossibility, and the alpha_s identity are publishable standalone mathematics.

The framework's cosmological mapping is where the assumptions break. Of the 9 entries in Section IV, 3 are BROKEN by observation (K_pivot mapping, w_0, w_a), 4 are CONDITIONAL on undetermined quantities (eta, CDM abundance, G_N cutoff, sigma_8 interpretation), and only 1 (sigma_8 = 0.799) survives as a viable prediction. The 14 ASSUMED entries cluster in two areas: the geometric ansatz (product structure, SU(3), Jensen family, volume-preserving) and the spectral action as effective action. Neither cluster is derived from deeper principles. The 11 BROKEN entries include 3 cosmological predictions excluded by DESI/Planck, the spectral action stabilization program (27 closures), and 3 specific mechanism failures (GGE permanence, Friedmann-BCS, Anderson-Higgs).

The single largest risk is the K_pivot scale mapping. The entire cosmological prediction suite -- n_s, alpha_s, sigma_8 -- is CONDITIONAL on a mapping between internal and CMB scales that has never been rigorously established. Two physically motivated mappings give contradictory answers (K = 4.3e-57 vs K = 2.0 M_KK). The framework may be correct mathematics that does not connect to CMB observables in the way assumed. This is not a refutation; it is a gap between proven spectral geometry and unproven cosmological interpretation. The gap is load-bearing.
