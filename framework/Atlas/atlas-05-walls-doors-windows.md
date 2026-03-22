# Atlas D05: Walls, Doors, and Windows

---

## I. Walls (Structural Obstructions)

### W1: Weyl Asymptotic F/B Ratio

- **Statement**: The ratio of fermionic to bosonic spectral weight on Jensen-deformed SU(3) is F/B = 16/44 = 0.364 (fiber dimension), asymptotically tau-independent by Weyl's law. The spectral-weighted ratio is F/B = 0.55. Any volume-preserving deformation of any compact manifold produces a tau-independent F/B ratio in the UV.
- **Proof session**: S18 (first observed), S20b (proven structural via Weyl's law), S22c (Trap 3)
- **Scope**: Blocks ALL perturbative spectral functionals that depend on the UV balance of bosonic and fermionic modes. Specifically: Coleman-Weinberg, Casimir energy (all field content), spectral back-reaction, Higgs-sigma portal, signed gauge-threshold corrections. Any mechanism that requires the F/B ratio to vary with tau to produce a minimum is killed.
- **Closures attributed**: 6 (mechanisms #2, 3, 4, 8, 12, 15 in D02)
- **Escape**: Low-mode regime (N < 200) where autocorrelation corrections are O(N^{-1/8}) ~ 50-60%. BCS operates in this regime. The UV tail controls the spectral action, but BCS condensation depends on the IR density of states near the van Hove fold.

---

### W2: Peter-Weyl Block-Diagonality

- **Statement**: D_K is exactly block-diagonal in the Peter-Weyl basis for ANY left-invariant metric on ANY compact semisimple Lie group. Three independent proofs (algebraic, representation-theoretic, numerical at 8.4e-15). The off-diagonal matrix elements C_nm between distinct (p,q) sectors vanish identically.
- **Proof session**: S22b (8.4e-15, three proofs)
- **Scope**: Blocks ALL mechanisms requiring cross-sector coupling in the Dirac spectrum. Inter-sector cancellation of spectral sums, inter-sector energy transfer, coupled delta_T crossing, coupled V_IR minimum. The signed-sums escape route (b_1 - b_2 sign change) is killed because each sector is independently monotone with no possibility of inter-sector cancellation.
- **Closures attributed**: 3 (mechanisms #13, 14, 20 in D02)
- **Escape**: Nothing -- this is exact. Block-diagonality is a consequence of representation theory, not an approximation. However, it does NOT prevent the physical BCS condensate from carrying inter-sector quantum numbers (Cooper pairs carry K_7 charge from B2, which connects to B1/B3 through the Josephson coupling in the many-body Hamiltonian, not through D_K matrix elements).

---

### W3: Spectral Gap at mu = 0

- **Statement**: D_K has spectral gap lambda_min > 0 at all tau on the Jensen curve. D_total gap minimum = 0.790 M_KK at tau = 0.27. The gap never closes. At mu = 0, there is no Fermi surface, and BCS pairing in the standard sense (Cooper instability at the Fermi surface) is absent.
- **Proof session**: S17a (gap observed), S19a S-4 (fermion condensate killed), S23a K-1e (Kosmann-BCS decisive), S30Ab (Pfaffian trivial, gap > 0 confirmed at 75 tau values)
- **Scope**: Blocks ALL mechanisms requiring a Fermi surface or zero-energy states at mu = 0. Banks-Casher fermion condensate, Kosmann-BCS at mu = 0, gap-edge self-coupling. Also blocks canonical and grand canonical mu != 0 routes via particle-hole symmetry (S34).
- **Closures attributed**: 5 (mechanisms #5, 17, 18, 25, 26 in D02)
- **Escape**: BCS at finite effective mu (the KC chain, which generates mu_eff through phonon collisions). The van Hove singularity at the B2 fold produces a divergent DOS that triggers BCS through the 1D theorem (any g > 0, RG-BCS-35) without requiring a Fermi surface. The escape is the recognition that BCS on a compact manifold is NOT the same as BCS in a metal -- the critical coupling is zero.

---

### W4: Spectral Action Monotonicity (Structural Monotonicity Theorem)

- **Statement**: The weighted spectral mean <lambda^2>(tau) increases monotonically under volume-preserving Jensen deformation. For any monotonically decreasing cutoff function f, the spectral action S_f(tau) = Tr f(D^2/Lambda^2) decreases monotonically. For any increasing f, S_f increases. No local minimum exists at any tau in [0, 0.5] for any monotone f, any Lambda > 0, any of the 10 tested Peter-Weyl sectors. Verified at 9,600 individual checks (10 cutoffs x 6 Lambda x 16 tau x 10 sectors).
- **Proof session**: S37 CUTOFF-SA-37 (definitive), with precursors at S17a (V_tree), S18 (CW), S20a (SD), S24a (V_spec), S36 (S_full)
- **Scope**: Blocks ALL single-trace spectral action mechanisms with monotone cutoff functions. This is the most powerful wall, closing the entire category of "spectral action tau-stabilization." Includes: V_tree, CW, Casimir (all modes), Seeley-DeWitt, V_spec at all rho, Connes 8-cutoff, V'' spinodal, Kerner bridge, V_total on U(2)-inv surface, Freund-Rubin, full 28D Hessian, foam non-monotone, occupied-state SA, unexpanded SA. The wall extends to all smooth monotone cutoffs, all Lambda, and all 28 dimensions of the left-invariant metric space (HESS-40).
- **Closures attributed**: 13+ (mechanisms #1, 7, 9, 10, 11, 19, 22, 23, 24, 30, 37, 45, 47, 48 in D02)
- **Escape**: (1) Wheeler-DeWitt quantum localization (wavefunction can peak on a monotone slope). (2) Instanton-averaged path integral (breaks single-vacuum assumption). (3) Multi-trace spectral action (product of monotone functions is not necessarily monotone). (4) Off-Jensen moduli (theorem proven only on Jensen; multi-parameter landscape may have saddle points). (5) Non-spectral-action functionals entirely.

---

### W5: Berry Curvature Vanishing

- **Statement**: K_a is anti-Hermitian (||K_a + K_a^dag|| < 1.12e-16, structural) for the Kosmann derivative on Jensen-deformed SU(3). This implies Berry curvature Omega = 0 identically for ALL eigenstates, ALL sectors, ALL tau. Extends to ANY compact Lie group with left-invariant metric.
- **Proof session**: S25 (definitive, machine epsilon)
- **Scope**: Blocks ALL topological mechanisms based on Berry phase physics (Berry curvature monopoles, Chern numbers of eigenvalue bundles, topological transitions driven by Berry flux). The S21a "Berry curvature monopoles" were reclassified as quantum metric (Provost-Vallee), not Berry curvature.
- **Closures attributed**: 0 directly (Berry-based mechanisms were never independently proposed and tested as tau-stabilization candidates). The wall preemptively closes a class of mechanisms.
- **Escape**: Off-Jensen deformations where K_a may not be anti-Hermitian. Pfaffian Z_2 (which is a discrete topological invariant, not a Berry curvature quantity). Note: Pfaffian = +1 on Jensen at all tau (W5b in mega-matrix), but off-Jensen is untested.

---

### W6: NCG-KK Scale Irreconcilability

- **Statement**: The NCG spectral action cutoff Lambda_SA and the KK mass scale M_KK are irreconcilable. Lambda_SA/M_KK = 10^6 at tau = 0.21, and 10^15 at tau = 0.57. The spectral action identification (Lambda_SA = M_KK) fails by 6-15 orders of magnitude at all tested tau values.
- **Proof session**: S30Bb (B-30nck), S31Ba (B-31nck)
- **Scope**: Blocks the identification of the NCG spectral action cutoff with the KK compactification scale. This does not close the mathematical structure (D_K eigenvalues, selection rules, etc.) but closes the physical interpretation connecting the spectral action to 4D gauge kinetic terms at M_KK.
- **Closures attributed**: 0 directly (this is an interpretive wall, not a mechanism closure)
- **Escape**: (1) Abandon NCG identification entirely (pure KK interpretation). (2) Threshold corrections from heavy KK modes (unprecedented but theoretically possible). (3) Non-standard M_KK.

---

### W7: alpha_s = n_s^2 - 1 Structural Identity (NEW, S50)

- **Statement**: For ANY equilibrium propagator with K^2 dispersion on a compact Josephson lattice with broken U(1), the spectral running alpha_s is algebraically determined by the tilt n_s through alpha_s = n_s^2 - 1. Five independent proofs: (1) 3-pole degeneracy (poles 99.95% degenerate), (2) running mass algebraic bound gamma < 1-n_s = 0.035, (3) zero-mode protection preventing eikonal damping, (4) RPA vertex correction suppressed by mass hierarchy, (5) Goldstone theorem enforcing K^2 dispersion.
- **Proof session**: S50 (five proofs in W1-A, W1-F, W1-H, W2-A, W2-B)
- **Scope**: Blocks ALL mechanisms for generating the observed alpha_s = -0.008 from a K^2 Josephson propagator with n_s = 0.965. The identity gives alpha_s = -0.069 at 6-8 sigma from Planck. Closes 3-pole Leggett, running mass, anomalous dispersion within the phase sector.
- **Closures attributed**: 3 (mechanisms #56.1, 56.3, 56.5 in D02)
- **Escape**: Correlators from OUTSIDE the Josephson phase sector. The SA correlator has 110% pole spread and breaks the identity. Pair-transfer sinc^2 form factor also breaks it. The escape requires mixing between the phase sector and other spectral sectors.

---

### W8: Anderson-Higgs Impossibility for U(1)_7 (NEW, S51)

- **Statement**: K_7 cannot be gauged within the NCG inner fluctuation framework. Three independent proofs: (1) Commutant obstruction: [D_K, K_7] = 0 implies trivial 1-form A_7 = a[D_K, K_7] = 0 at tree level. This propagates to all loop orders because any function Sigma(D_K) satisfies [K_7, Sigma(D_K)] = 0. (2) Categorical distinction: K_7 is a Kosmann derivative (diffeomorphism generator), not an inner automorphism of A_F (gauge generator). NCG gauge fields arise exclusively from inner automorphisms. (3) Even forcing the off-diagonal breaking (epsilon = 0.117) gives m_gauge = 0.12-0.54 M_KK, 15-65x below the [8,16] target.
- **Proof session**: S51 W1-C (GAUGE-U1K7-51)
- **Scope**: Blocks the Anderson-Higgs mechanism as a route to giving the Goldstone a mass. The Goldstone boson of U(1)_7 breaking cannot be eaten by a gauge field. Closes the sole surviving Goldstone theorem loophole identified by Landau in S50 collab.
- **Closures attributed**: 1 (mechanism #56.18 in D02)
- **Escape**: Physics outside the NCG inner fluctuation framework. External gauging of K_7 (not from the spectral triple), or a mass mechanism that does not involve gauge field absorption.

---

### W9: Convex Combination Theorem for Additive Mixing (NEW, S51)

- **Statement**: The spectral index of an additive mixture P_phys(K) = (1-beta)*P_G(K) + beta*chi_SA(K) is a convex combination of the individual spectral indices, bounded by [min(n_s_G, n_s_SA), max(n_s_G, n_s_SA)] at each K. At K_pivot = 2.0 M_KK: n_s(Goldstone) = -0.996, n_s(SA) = +0.150. The mixed n_s is bounded above by +0.150, while the target is 0.965.
- **Proof session**: S51 W2-A (SA-GOLDSTONE-MIXING-51)
- **Scope**: Blocks additive SA-Goldstone mixing at K_pivot = 2.0 M_KK. The obstruction is the mass problem: K_pivot/K* = 22.9, placing the Goldstone deep in its K^{-2} regime. The Goldstone mass 0.070 M_KK is 170x below the required 11.85 M_KK.
- **Closures attributed**: 1 (mechanism #56.20 in D02)
- **Escape**: Remapping K_pivot to K < K* = 0.087 M_KK. At these scales, both correlators are nearly flat, the SA pole spread breaks the identity, and n_s = 0.965 is achievable with beta > 0.9 and alpha_s in [-0.040, 0]. This requires >= 3.1 e-folds from the stiff epoch, obtainable from tau_i <= 1.7e-5 (EFOLD-MAPPING-52).

---

### W10: Zero-Mode Protection on T^2 (NEW, S50-S51)

- **Statement**: The Goldstone is a KK n = 0 mode on T^2 (the torus of the tessellation cell). Its wavefunction psi_0 = 1/sqrt(A) is constant, hence orthogonal to ALL higher KK eigenstates. This gives <0|V|n> = 0 to ALL ORDERS in the Born series for any position-diagonal operator V. Extended in S51 from first-order to all-orders Born.
- **Proof session**: S50 W1-H (eikonal damping), S51 W1-B (local resonance)
- **Scope**: Blocks ALL mechanisms that attempt to scatter the Goldstone into higher KK modes via position-dependent potentials. Eikonal texture damping, local resonance T-matrix mass enhancement, texture Born scattering.
- **Closures attributed**: 2 (mechanisms #56.4, 56.17 in D02)
- **Escape**: Mechanisms that are NOT position-diagonal (e.g., derivative coupling d/dx). The zero-point parametric mechanism (S51 W1-B) achieves m_eff = 2.45 M_KK precisely because it couples through d^2c/dphi^2 (a medium property, not a potential), circumventing the zero-mode protection. But this is still 5x short of the target.

---

## II. Doors (Permanently Open Routes)

These are results that survive unconditionally. No future computation can close them.

### Door 1: BCS Mechanism Chain (Unconditional, 5/5 links)

- **What it is**: The complete chain from van Hove fold through BCS condensation: I-1 (van Hove singularity, structurally stable A_2 catastrophe) -> RPA (M_max = 1.674, 38x above threshold) -> Turing (W = 1.9-3.2x, pairing coherence across wall) -> WALL (rho = 14.02, Z = 1.016, Eckart worst-case) -> BCS (E_cond = -0.115, unconditional for any g > 0 by 1D theorem).
- **What it gives**: BCS condensation OCCURS at the van Hove fold. Cooper pairs carry K_7 charge +/-1/2. The condensate breaks U(1)_7 spontaneously. The Bogoliubov quasiparticle spectrum is the candidate CDM.
- **What it does not solve**: WHY tau reaches the fold (no tau-stabilization mechanism), WHAT the 4D observer sees (transit dynamics), HOW n_s = 0.965 emerges.
- **Sessions**: S28 (KC chain), S32 (RPA PASS), S33 (TRAP PASS), S34 (corrected), S35 (unconditional)

### Door 2: Pure Mathematics Publications

- **What it is**: Twelve publishable standalone mathematical results that survive regardless of the framework's physical fate (permanent-results-registry.md Section I). Includes block-diagonality theorem, monotonicity theorem, algebraic traps, van Hove zero-critical-coupling, LZ retraction, Cl(8) bridge, Berry curvature vanishing, spectral Bianchi identity, 8D Petrov classification, spectral flow = 0 theorem, grading theorem, perturbative exhaustion.
- **What it gives**: JGP/CMP/JMP/PRD-level papers on spectral geometry of Dirac operators on compact Lie groups. New connections between NCG, Berry geometry, and Clifford algebra.
- **What it does not solve**: These are mathematical facts about D_K on SU(3), not cosmological predictions.
- **Sessions**: S7-S28 (accumulated)

### Door 3: SA Correlator Identity Breaking

- **What it is**: The spectral action two-point function chi_SA(K) = Sum W_{(p,q)}/(K^2 + C_2(p,q)) has 110% pole spread (C_2 from 1.33 to 9.33), qualitatively distinct from the Josephson phase propagator (0.051% pole spread). Goldstone's theorem does NOT protect it. The alpha_s = n_s^2 - 1 identity IS broken by chi_SA (deviation = 0.066, effective alpha = 0.86).
- **What it gives**: A structurally distinct correlator that escapes W7. The mixing of SA and Goldstone sectors at K < K* produces viable (n_s, alpha_s) pairs.
- **What it does not solve**: The K_pivot mapping (whether the physical CMB scale maps to K < K*). The SA correlator is also cutoff-dependent in its sector weights (S51 CUTOFF-CONV-51: alpha_eff stable at 4.7% variation, but identity deviation at 33% variation).
- **Sessions**: S50 cross-domain (discovery), S51 W1-D (cutoff convergence), S51 W2-A (mixing model)

### Door 4: sigma_8 = 0.799 (Observationally Viable Prediction)

- **What it is**: The O-Z rigid prediction with alpha_s = -0.069 gives sigma_8 = 0.799, sitting between Planck (0.811 +/- 0.006) and lensing (~0.76 +/- 0.03). Within 2.0 sigma of Planck and 1.6 sigma of lensing.
- **What it gives**: A zero-free-parameter cosmological prediction that is observationally viable. If the sigma_8 tension between Planck and lensing persists, this prediction discriminates: it favors the lensing value.
- **What it does not solve**: The n_s and alpha_s predictions are at 6-8 sigma from Planck (IF K_pivot = 2.0). sigma_8 is the sole surviving observational prediction.
- **Sessions**: S50 W2-F (confirmed viable, S49 overestimate corrected by 14x)

### Door 5: Leggett Dipolar Identification

- **What it is**: The Leggett mode on Jensen-deformed SU(3) maps to the Leggett frequency of superfluid 3He within 18%. Quality factor Q = 670,000 (all pair-breaking channels energetically forbidden). The Leggett mass is physical and undamped.
- **What it gives**: A concrete identification between internal BCS dynamics and known condensed matter physics. The ratio omega_L2/omega_L1 = phi_paasch at the crossing tau = 0.211686 (confirmed to 6 significant figures). This is a geometric identity connecting many-body BCS to single-particle Dirac spectral geometry.
- **What it does not solve**: The Leggett mass m_L = 0.070 M_KK is 170x below the mass required for n_s = 0.965.
- **Sessions**: S48 (identification), S49 (phi crossing), S50 W1-D/W1-E (Q factor and crossing confirmation)

### Door 6: Phi Crossing Geometric Identity

- **What it is**: At tau = 0.211686, the ratio of the two Leggett mode frequencies equals phi_paasch = 1.53158 to machine precision (4.4e-15). The ratio J_12/J_23 = 19.52 is algebraically constant. This is a pure geometric identity -- it connects the BCS collective dynamics (Josephson coupling ratio) to the Dirac eigenvalue ratio that defines phi_paasch.
- **What it gives**: A deep structural connection between the framework's two layers (single-particle geometry and many-body physics). Publishable as pure mathematics.
- **What it does not solve**: The physical significance of the crossing. It occurs at tau = 0.2117, close to but distinct from the van Hove fold at tau = 0.190.
- **Sessions**: S49 (discovery), S50 W1-E (confirmed 6 sig figs)

### Door 7: Acoustic Hawking Temperature

- **What it is**: T_acoustic agrees with T_Gibbs to 0.7% (zero free parameters). The 4D acoustic metric derived from the BdG sound speed on the tessellation fabric produces a Hawking-analogue temperature that matches the thermodynamic temperature from the Gibbs ensemble.
- **What it gives**: A non-trivial self-consistency check of the framework's thermodynamic structure. The acoustic Hawking temperature is determined by the BCS sound speed and the tessellation geometry, both of which are derived from D_K.
- **What it does not solve**: This is a consistency check, not a prediction.
- **Sessions**: S40

### Door 8: CDM by Construction

- **What it is**: CDM-CONSTRUCT-44 PASS. T^{0i}_4D = 0 exact (homogeneous creation). v_eff = 3.48e-6 c. The Bogoliubov quasiparticles from the transit are automatically cold and pressureless in 4D.
- **What it gives**: CDM without a dark sector Lagrangian. The quasiparticles are fiber-localized (no 4D spatial momentum), giving zero free-streaming length.
- **What it does not solve**: The CDM abundance (requires knowing the pair creation rate and transit dynamics quantitatively). The sigma/m ratio is 5.7e-51 cm^2/g (unobservably small self-interaction).
- **Sessions**: S42, S44

---

## III. Windows (Conditional Routes)

Each window has a specific condition that determines whether it opens or remains shut.

### Window 1: SA-Goldstone Mixing at K < K* (THE decisive window)

- **Condition**: The physical CMB pivot k = 0.05 Mpc^{-1} must map to K_fabric < K* = 0.087 M_KK. This requires >= 3.1 e-folds of expansion from the stiff epoch, obtainable from tau_i <= 1.7e-5 (0.009% of tau_fold).
- **What computation decides it**: EFOLD-MAPPING-52 -- compute the full expansion history from tau = 0 to present, including stiff epoch, transit, GGE relic epoch, and transition to radiation domination. Extract the physical K_pivot mapping from total e-folds.
- **Current status**: PRELIMINARY PASS. E-fold estimate gives N_e = 3.3 from tau_i = 10^{-5} (margin 0.2). The natural initial condition (near-round metric) gives tau_i << 10^{-5}, providing ample margin. But the computation is approximate (stiff-epoch w = 1 assumed, no backreaction).
- **If PASS**: SA-Goldstone additive mixing produces n_s = 0.965 with beta > 0.9 and alpha_s in [-0.040, 0]. The identity IS broken at K < K*. The framework's n_s prediction survives.
- **If FAIL**: All cosmological predictions are excluded. The mathematics survives as pure spectral geometry.
- **Depends on**: W9 (convex combination theorem establishes the K_pivot threshold), S51 W2-A (mixing model parametrics)

### Window 2: Q-Theory CC Crossing at N >= 2

- **Condition**: The physical BCS ground state at the fold must have pair number N >= 2. At N = 1, the self-consistent B3 gap (Delta_B3 = 0.084) falls below the 0.13 threshold and the Gibbs-Duhem zero-crossing is eliminated. At N = 2, the crossing reappears at tau* = 0.170.
- **What computation decides it**: Full 992-mode exact diagonalization of the BCS Hamiltonian at the fold (versus the current 8-mode truncation). The physical pair number depends on the full spectrum.
- **Current status**: OPEN. The 8-mode truncation gives N = 1 (marginal). The N = 2 crossing exists but requires a full-spectrum computation to confirm physical relevance.
- **If PASS**: The CC problem reduces from 120 orders to a question about the functional form of the q-theory adjustment near the crossing.
- **If FAIL**: The CC problem has no surviving mechanism within the framework. The 120-order gap persists.
- **Depends on**: S45 Q-THEORY-BCS-45 (first PASS), S46 W1-1/W2-5 (self-consistent gap analysis)

### Window 3: Off-Jensen 5D Moduli Landscape

- **Condition**: The full 5-parameter U(2)-invariant moduli space (or the 36-dimensional full left-invariant metric space) must contain a saddle point, minimum, or topologically nontrivial feature not accessible on the 1-parameter Jensen line.
- **What computation decides it**: Full 5D Hessian at tau ~ 0.18, off-Jensen Dirac spectrum, off-Jensen Pfaffian. The T4 instability at the boundary (eigenvalue -9.9 at tau = 0.60, eps = +0.15) suggests the U(2)-invariant surface is itself unstable toward full 5D.
- **Current status**: UNTESTED. This has never been computed. The Interior Mixing Theorem breaks when the Killing/non-Killing decomposition changes under U(2)-breaking. The spectral gap could close and the Pfaffian could flip off-Jensen.
- **If features found**: Potentially reopens topological mechanisms (Berry phase, Pfaffian transitions) that are closed on Jensen by W5 and the Pfaffian triviality. Could provide a geometric mechanism for tau-stabilization that the 1D Jensen scan cannot see.
- **If featureless**: Confirms the full moduli landscape is as monotone as the Jensen line. Closes the last geometric escape route.
- **Depends on**: Computational infrastructure for 5-parameter metric families on SU(3). Estimated cost: 2-5 hours for Dirac + Pfaffian at a single off-Jensen point.

### Window 4: Higher PW Truncation Spectrum

- **Condition**: Eigenvalues at max_pq_sum = 30 must reach 12 M_KK. The scaling law (S51 HIGH-PW-51) gives max|lambda| = 0.633*sqrt(C_2) + 0.555, predicting R = 12.05 M_KK at N = 30.
- **What computation decides it**: Weight-space irrep construction (avoiding the exponentially large tensor-product-then-project algorithm). The Dirac matrix diagonalization at (30,0) is 7936x7936 -- trivial for numpy. The bottleneck is constructing the representation.
- **Current status**: INFO. S51 computed N = 8 (spectral radius 3.92 M_KK). N = 30 is computationally accessible with proper irrep construction but has not been implemented. The spectral tilt n_s > 1 structurally for any finite truncation of a compact Riemannian manifold's Dirac spectrum (Weyl density grows as lambda^{d-1}).
- **If spectrum reaches 12 M_KK**: Does NOT solve the n_s problem (n_s > 1 structurally from heat kernel). But it characterizes the SA correlator at the scale where the 170x mass ratio is resolved.
- **If growth slower than predicted**: Lowers the SA correlator's effective mass scale, potentially affecting the mixing model.
- **Depends on**: S51 HIGH-PW-51 (scaling law), computational implementation of weight-space algorithm

### Window 5: Strutinsky Shell Correction to chi_SA

- **Condition**: The shell correction to the SA susceptibility chi_SA = d^2S/dtau^2 is 49% of the smooth part (S51 STRUTINSKY-51). If the shell structure at higher PW truncation changes the balance, the effective n_s from the SA sector could shift.
- **What computation decides it**: Strutinsky decomposition at max_pq_sum >= 12, where the spectrum has enough levels for reliable smoothing. The current N = 6 computation has only 784 unique eigenvalues.
- **Current status**: FAIL at current truncation (n_s_smooth = -0.80 at Lambda = 12 M_KK). Neither smooth nor shell part produces n_s near 0.965.
- **Depends on**: Window 4 (higher PW truncation required)

---

## IV. Cross-Reference: Walls vs. Doors

| Wall | Doors it DOES NOT block | Explanation |
|:-----|:----------------------|:------------|
| W1 (F/B ratio) | Door 1 (BCS chain) | BCS operates in the IR near the van Hove fold, not in the UV where W1 holds |
| W2 (block-diagonal) | Door 1 (BCS chain) | BCS Hamiltonian couples sectors through the many-body V matrix, not through D_K |
| W3 (spectral gap) | Door 1 (BCS chain) | Van Hove divergent DOS triggers BCS through the 1D theorem, not through a Fermi surface |
| W4 (monotonicity) | Door 3 (SA correlator) | The SA correlator chi_SA = d^2S/dtau^2 involves derivatives of S, not S itself |
| W7 (identity) | Door 3 (SA correlator) | SA correlator has K^{-alpha} with alpha != 2, not K^{-2} |
| W9 (convex combination) | Window 1 (K < K*) | The bound is K-dependent; at K < K*, both correlators are flat |

---

## V. The Constraint Surface in One Diagram

```
CLOSED (by wall)                    OPEN (conditional)
=================                   ==================

W4: All spectral action             Window 1: SA-Goldstone
    tau-stabilization                   at K < K*
    (13+ mechanisms)                    (K_pivot mapping)
         |                                   |
W1: All perturbative                Window 2: Q-theory CC
    F/B-dependent                       at N >= 2
    (6 mechanisms)                      (full-spectrum ED)
         |                                   |
W3: All mu=0 BCS                   Window 3: Off-Jensen
    (5 mechanisms)                      landscape
         |                              (never computed)
W7: All Josephson-sector
    n_s mechanisms
    (3 mechanisms)                  PERMANENTLY OPEN
         |                          ================
W8: Anderson-Higgs                  Door 1: BCS chain
    for U(1)_7                      Door 2: Pure math
    (1 mechanism)                   Door 3: SA correlator
         |                          Door 4: sigma_8 = 0.799
W9: Additive mixing                 Door 5: Leggett dipolar
    at K = 2.0                      Door 6: Phi crossing
    (1 mechanism)                   Door 7: Acoustic T_H
         |                          Door 8: CDM by construction
W10: Zero-mode protection
     (2 mechanisms)
```

The entire framework's cosmological viability reduces to Window 1: the K_pivot scale mapping. This is the EFOLD-MAPPING-52 master gate. If it passes, the SA-Goldstone mixing produces viable (n_s, alpha_s). If it fails, the mathematics survives (Doors 1-8) but the cosmological predictions are excluded.

---

*Compiled from: permanent-results-registry.md, constraint-mega-matrix.md, atlas-01-session-timeline.md, atlas-02-mechanism-lifecycle.md, session-50-oz-crossdomain-finding.md, session-50-naz-deepdive.md, session-50-51-collective-analysis.md, session working papers S39-S51, framework/spectral-post-mortem.md, and MEMORY.md. This document is the authoritative structural landscape -- walls block, doors open, windows depend on one computation.*
