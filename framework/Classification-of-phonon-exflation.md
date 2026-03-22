# Landau Classification of Phonon-Exflation

**Author**: Landau Condensed Matter Theorist
**Date**: 2026-03-15
**Status**: Living document (updated each session)
**Source**: S44 collab review Section 4, expanded with full S7-S44 context
**Papers**: `researchers/Landau/` (40 papers, index at `researchers/Landau/index.md`)

---

## Preamble

The phonon-exflation framework claims that Standard Model particles are phononic excitations of M^4 x SU(3), with cosmic expansion driven by internal compactification. Over Sessions 7 through 44, a systematic mapping has emerged between every structural element of this framework and a precise condensed matter counterpart in Landau's classification program. This document makes that mapping explicit, complete, and permanent.

The mapping is not metaphorical. It is a statement about mathematical structure: the same symmetry-breaking patterns, order parameter spaces, free energy functionals, and quasiparticle descriptions that govern superfluids, superconductors, and Fermi liquids also govern the internal geometry of the phonon-exflation framework. Where the mapping holds, it constrains. Where it breaks, it diagnoses.

Every claim below is grounded in specific Landau papers (cited as Paper NN) and specific framework computations (cited as session-gate). The document is self-contained: it can be read without the S44 quicklook.

---

## I. The Complete Mapping

The following table maps every framework concept to its Landau condensed matter equivalent, with the session that established the connection and the Landau paper that provides the theoretical foundation.

| Framework Concept | CM Equivalent | Session | Paper | Status |
|:--|:--|:--|:--|:--|
| Jensen deformation tau | Order parameter eta | S17a | 04 | PROVEN |
| SU(3) -> U(1)_7 | Symmetry breaking G -> H | S34 | 04 | PROVEN |
| Spectral action S(tau) | Landau free energy F(eta) | S17a | 04 | STRUCTURAL |
| V'''(0) = -7.2 | Cubic term forces first-order | S17a | 04 sec. 8 | PROVEN |
| d_int = 8 > d_uc = 4 | Mean-field exact above d_uc | S17a | 04 sec. 7 | STRUCTURAL |
| Transit tau=0 to fold | First-order phase transition | S37-38 | 04, 09 | PROVEN |
| BCS condensation at fold | Superconducting transition | S35 | 08, 15 | PROVEN |
| BCS instanton gas | Giant pair vibration (GPV) | S37 | 23, 24, 25 | PROVEN |
| S_inst = 0.069 | Quantum critical point | S38 | 29 | PROVEN |
| Post-transit GGE | Normal component at rest | S38 | 05, 20 | STRUCTURAL |
| Dark energy | Superfluid condensation energy | S44 W6-4 | 05 | OPEN |
| Dark matter | Quasiparticle energy at rest | S44 W1-2 | 11 | PROVEN |
| DM/DE ratio | Specific heat exponent alpha | S44 W6-4 | 04, 05 | OPEN (2.7x) |
| G_N | Effective mass / response coeff. | S44 W1-1 | 11 | PROVEN (factor 2.3) |
| Spectral triple dissolution | Effective theory emergence | S44 W6-7 | 04 (universality) | PROVEN |
| CC fine-tuning | Universality class mismatch | S44 W5-5 | 04 sec. 7 | STRUCTURAL |
| n_s = 0.965 | Quench dynamics / Kibble-Zurek | S43-44 | 09, 21 | OPEN |
| epsilon_H = 3.0 | Ratio invariance (intensive) | S44 W4-3 | 04 | PROVEN (theorem) |
| Van Hove singularities | Phase transition classification | S34-44 | 27 | PROVEN |
| Block-diagonal theorem | Selection rules (Schur) | S22b | 04 (rep. theory) | PROVEN |
| 8-temperature GGE | Non-Fermi liquid | S44 W6-5 | 11, 20 | STRUCTURAL |
| Negative heat capacities | Saddle directions in F | S44 W6-5 | 04, 11 | PROVEN |
| Euler deficit = E_cond | Gibbs-Duhem violation | S44 W6-5 | 05 | OPEN |
| Effacement wall (0.002%) | Off-diagonal LRO invisible | S44 W5-4 | 11, 15 | PROVEN |
| K_7 Cooper pairs | BCS order parameter | S35 | 08, 15 | PROVEN |
| Pomeranchuk f_0 = -4.687 | Fermi surface instability | S22c | 11 | PROVEN |
| B2 flat band | Infinite-order Van Hove | S22c | 27 | PROVEN |
| M_max = 1.674 | Thouless criterion | S35 | 15 | PROVEN |
| L/xi_GL = 0.031 | Ultrasmall grain limit | S38 | 17, 36 | PROVEN |
| E_vac/E_cond = 28.8 | BEC regime of crossover | S37 | 22 | PROVEN |
| omega_att = 1.430 | Pair vibration frequency | S37 | 23 | PROVEN |
| Schwinger-instanton duality | WKB tunneling = pair creation | S37 | 29 | PROVEN (1%) |
| Second sound Q = 75,989 | Undamped two-fluid mode | S44 W6-2 | 05 | PROVEN |
| 12 Van Hove trajectories | Band structure topology | S44 W6-8 | 27 | PROVEN |
| Gap stability (-1.63%) | Fully gapped spectrum | S44 W5-3 | 08 | PROVEN |
| BDI class, T^2 = +1 | Altland-Zirnbauer symmetry | S17c | 15 | PROVEN |
| g_1/g_2 = e^{-2tau} | Geometric running coupling | S17a | 10 | PROVEN |
| CDM T^{0i} = 0 | Pressureless dust / normal fluid | S44 W1-2 | 05 | PROVEN |
| OCC-SPEC-45 (proposed) | Landau free energy at phys. state | S45 prereg | 04, 15, 08 | UNCOMPUTED |

**Reading guide**: PROVEN means computed to machine precision or proven as a theorem. STRUCTURAL means the identification is mathematically exact but relies on an analogy whose full consequences are unexplored. OPEN means the mapping exists but the quantitative prediction has not yet been confirmed. UNCOMPUTED means the gate is pre-registered but not yet executed.

---

## II. Phase Classification Table

Landau's program classifies all ordered phases by their symmetry-breaking pattern, order parameter, transition type, universality class, and critical exponents. The following table applies this classification to every phase and transition the framework has identified across Sessions 7 through 44.

### II.A. Equilibrium Phases

| Phase | Symmetry Group | Order Parameter | Physical Content |
|:--|:--|:--|:--|
| tau = 0 (round SU(3)) | (SU(3)_L x SU(3)_R)/Z_3 | tau = 0 | Bi-invariant metric. Full isometry. Unstable maximum of V_eff. |
| 0 < tau < tau_fold (transit) | (SU(3)_L x SU(2)_R x U(1)_R)/Z_6 | tau > 0 | Jensen deformation. [iK_7, D_K] = 0 forces SU(3) -> U(1)_7. |
| tau ~ 0.19 (fold, BCS) | Same, plus U(1)_7 -> Z_2 | Delta (BCS gap) | Van Hove singularity in B2. Cooper pairing with K_7 charge +/-1/2. |
| Post-transit (GGE relic) | (SU(3)_L x SU(2)_R x U(1)_R)/Z_6 | Delta = 0 | Condensate destroyed (P_exc = 1.000). GGE with 8 conserved integrals. |

### II.B. Transitions

| Transition | Type | Order Parameter | Universality Class | z | nu | beta | alpha | d_uc |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| tau = 0: SU(3) -> U(1)_7 | First-order | tau (scalar) | None (first-order) | -- | -- | -- | -- | -- |
| tau ~ 0: Lifshitz (Type I) | Topological | Fermi pocket creation | Lifshitz z=2 | 2 | 1/2 (MF) | -- | -- | d_uc = 3 for z=2 |
| tau ~ 0.19: BCS onset | Second-order (GL) | Delta (complex scalar) | 3D Ising (Z_2, n=1) | 2.024 | 0.6301 | 0.3265 | 0.110 | 4 |
| Transit completion: BCS destruction | Sudden quench | P_exc -> 1.000 | Kibble-Zurek | 2.024 | 0.6301 | -- | -- | -- |

**Notes on the classification.**

1. The tau = 0 transition is first-order because V'''(0) = -7.2 (Paper 04, Section 8: a cubic invariant in the Landau expansion forces first-order). The cubic term exists because the Z_2 symmetry tau -> -tau is NOT a symmetry of the spectral action -- the Jensen deformation is one-directional.

2. The BCS transition at tau ~ 0.19 is classified as 3D Ising (S43, BCS-CLASS-43). The order parameter Delta is a complex scalar, but the K_7 charge pinning ([iK_7, D_K] = 0, S34) reduces the continuous U(1) phase degree of freedom to a discrete Z_2 (sign of Delta). The resulting universality class is Z_2 with d = 3 spatial dimensions and n = 1 component. The critical exponents are those of the 3D Ising model: nu = 0.6301, beta = 0.3265, gamma = 1.2372, alpha = 0.110. The dynamic universality class is Model A (Paper 09: overdamped relaxational dynamics, no conservation laws coupling to the order parameter), giving z = 2.024.

3. The Lifshitz transition at tau = 0 is Type I: a new Fermi pocket appears as the Jensen deformation lifts the degeneracy of the bi-invariant SU(3) spectrum (S43, LIFSHITZ-43). The 32-fold degeneracy at tau = 0 splits into 8.27-fold residual degeneracy at any tau > 0 (S44 W5-3). This is topological -- it changes the connectivity of the Fermi surface without breaking a continuous symmetry. For d_int = 8, the Lifshitz transition is far above its upper critical dimension d_uc = 3, so mean-field exponents are exact (Paper 04, Section 7).

4. The transit completion is a sudden quench, not a phase transition. The Landau-Zener probability P_LZ = exp(-2 pi Delta^2 / (hbar |v_dot|)) gives P_exc = 1 - P_LZ = 1.000 (S38; Paper 29). The system passes through the fold too fast for the BCS condensate to follow. In Kibble-Zurek language (Paper 21), the quench time tau_Q << tau_LK (the Landau-Khalatnikov relaxation time), so the system freezes with maximal excitation. The post-transit state is NOT thermal -- it is a GGE determined by the 8 Richardson-Gaudin conserved integrals (Paper 16, 20).

### II.C. d_uc and the Role of Internal Dimensionality

A subtlety that pervades the framework. The internal space SU(3) has dimension 8. For fluctuations of the tau modulus -- a single scalar mode in an 8-dimensional space -- the effective dimensionality for critical fluctuations is d_eff = 8. Since d_uc = 4 for the standard Landau-Wilson phi^4 theory (Paper 04), internal fluctuations of tau are ALWAYS in the mean-field regime. Mean-field exponents are exact.

However, the BCS transition involves gap fluctuations that are spatially local in the 4D external space. For these, d_eff = 3 (spatial dimensions), and the system is BELOW d_uc = 4. Fluctuation corrections are quantitatively important. The Ginzburg number Gi = 0.25 (S43, BCS-CLASS-43; N_eff = 4 B2 modes participating) confirms that fluctuations dominate near T_c.

This dual dimensionality -- d_int = 8 > d_uc for moduli, d_ext = 3 < d_uc for pairing -- is a structural feature of the framework that has no simple CM analog. Landau theory is simultaneously exact (for internal geometry) and insufficient (for BCS fluctuations) in the same system.

---

## III. The One-Body / Many-Body Partition

### III.A. The Diagnostic Pattern

Session 44 produced the framework's sharpest structural separation between success and failure. The pattern is systematic:

**Successes (one-body spectral properties):**
- G_N from induced gravity: PASS, factor 2.3 (W1-1). Three independent routes agree.
- CDM by construction: PASS, T^{0i} = 0 algebraic (W1-2).
- Tensor-to-scalar ratio: PASS, r = 3.86e-10 (W3-4). Self-consistently below all experiments.
- DM/DE ratio: PASS, 2.7x of observation (W6-4). Specific heat exponent alpha ~ O(1).
- Bosonic a_2: PASS, a_2^bos/a_2^Dirac = 61/20 exact (W4-2).
- Strutinsky smoothing: PASS, 2.54-decade plateau (W4-1).
- Second sound: PASS, Q = 75,989 (W6-2). Undamped at all cosmological scales.
- Dissolution scaling: PASS, epsilon_c ~ 1/sqrt(N) (W6-7).
- HOMOG-42 recompute: PASS, margin strengthened 144x (W5-6).

**Failures (many-body correlations):**
- Cosmological constant: FAIL/INFO. f_4/f_2 ~ 10^{-121}. 121-order fine-tuning (W5-5).
- Spectral tilt n_s: FAIL. Lifshitz eta = 3.77 (W1-3). epsilon_H = 3.0 invariant (W4-3). DIMFLOW at tuned sigma only (W2-2).
- Holographic CC: FAIL. 107 orders remain (W2-1).
- N_3 topological invariant: FAIL. Undefined on discrete 0D system (W3-3).
- FRG pilot: FAIL. BCS deviation 0.002% of spectral action (W5-4). Effacement.
- Jacobson mapping: FAIL. 114 orders off (W5-1).
- Foam stabilization: FAIL. 0/900 minima found (W4-4).

### III.B. Why the Partition Exists: Landau Theory

This partition has a precise origin in Landau's theory of interacting quantum systems, and it is not accidental.

**The spectral action is a one-body functional.** The spectral action S = Tr f(D^2/Lambda^2) depends only on the eigenvalues {lambda_k} of the Dirac operator. These are single-particle energies. In Landau's language (Paper 11, Section 3), the spectral action sees the quasiparticle dispersion epsilon_k -- the renormalized single-particle spectrum -- but not the quasiparticle interaction function f_{kk'}. It is the analog of computing the kinetic energy of a Fermi liquid from the dispersion relation alone, ignoring the Landau parameters F_l^{s,a}.

**BCS pairing is off-diagonal long-range order.** The BCS ground state |BCS> = prod_k (u_k + v_k c^dag_up c^dag_down) |0> has a nonzero anomalous expectation value <c_up c_down> (Paper 15, Section 3). This off-diagonal order is invisible to any functional that depends only on the diagonal elements of the one-body density matrix n_k = <c^dag_k c_k>. The spectral action, being a trace over one-body eigenvalues, is precisely such a diagonal functional.

The effacement wall (S44 W5-4, FRG-PILOT-44) quantifies this: the BCS modification of the spectral action is 0.002-0.016%. The non-perturbative BCS content -- the exponential gap Delta_0 ~ exp(-1/V N(E_F)) (Paper 15), the phase coherence, the topological winding number -- lives in the off-diagonal sector that no diagonal trace can access.

**Response coefficients are one-body; ground state properties are many-body.** In Fermi liquid theory (Paper 11, Section 5), the response of the system to external perturbations -- the susceptibility chi, the effective mass m*, the compressibility kappa -- can be expressed in terms of the Landau parameters F_l and the quasiparticle spectrum. These are one-body quantities dressed by interactions. The gravitational constant G_N, being the gravitational susceptibility (the response of the metric to matter fluctuations), is exactly such a response coefficient. It is correctly captured by the spectral action because response coefficients are accessible to one-body functionals.

The vacuum energy (cosmological constant), by contrast, is a ground state property. It requires summing the zero-point energies of all modes with their CORRELATED occupation numbers -- a many-body quantity that depends on the full ground state wavefunction, not just the spectrum. In Landau's language, the condensation energy E_cond = alpha^2(T_c - T)^2 / (4 beta) (Paper 04, Section 4; Paper 08, Section 3) is the difference between the free energies of the ordered and disordered phases. Computing it requires knowledge of BOTH phases, which requires the interaction, not just the dispersion.

**Summary**: The framework's successes are response coefficients (G_N, chi, m*, transport). Its failures are ground state properties (E_cond, Lambda, Delta). The spectral action is the right description for the former and the wrong description for the latter. This is not a deficiency of the spectral action -- it is the expected behavior of any one-body trace functional applied to a many-body system. The next phase of the research must operate at the many-body level.

---

## IV. The Specific Heat Exponent and DM/DE

### IV.A. The Observation

The observed ratio Omega_DM / Omega_DE = 0.265 / 0.685 = 0.387 is O(1). Both absolute scales -- rho_DM ~ 1.1e-29 g/cm^3 and rho_Lambda ~ 5.96e-30 g/cm^3 -- are 113 orders below natural (Planck) units. Yet their RATIO is 0.387, a number with no small parameters.

Session 44 (W6-4, DM-DE-RATIO-44) computed this ratio through 11 methods, of which 7 fall within a factor 10 of the observed value. The best result: flat-band partition with Volovik vacuum response gives 1.060 (2.74x above observation).

### IV.B. The Landau Free Energy Argument

In Landau phase transition theory (Paper 04, Section 4), the specific heat at a second-order transition is:

    C(T) = C_0 + a_0^2 / (2 b) * theta(T_c - T)

The jump Delta C = a_0^2 / (2 b T_c) is O(1) in dimensionless units (Delta C / C_0), regardless of the microscopic coupling strength. The ratio of the energy stored in the ordered phase (condensation energy) to the energy in excitations (normal component thermal energy) is:

    E_cond / E_excitation ~ alpha

where alpha is the specific heat critical exponent (C ~ |T - T_c|^{-alpha}). This ratio is determined by the universality class -- not by the UV cutoff, not by the microscopic Hamiltonian, and not by the absolute energy scale.

### IV.C. The Normal / Superfluid Partition

In the two-fluid model (Paper 05, Section 2), the total density of a superfluid splits as:

    rho = rho_s(T) + rho_n(T)

At T = 0, all the fluid is superfluid: rho_s = rho, rho_n = 0. At T = T_c, the superfluid is destroyed: rho_s = 0, rho_n = rho. The normal fluid density at low temperature is:

    rho_n(T) ~ T^4 / (c^5)    (phonon contribution)
    rho_n(T) ~ T^{-1/2} exp(-Delta/(k_B T))    (roton contribution)

The ratio rho_n / rho_s depends on temperature through universal functions determined by the excitation spectrum.

**The cosmological analog.** Map:
- rho_s -> Omega_DE (the "condensate" vacuum energy, if any)
- rho_n -> Omega_DM (the quasiparticle excitation energy, gravitating as CDM)
- T -> the effective temperature of the GGE (a multi-valued quantity with 8 independent temperatures)

The ratio Omega_DM / Omega_DE is then the cosmological analog of rho_n / rho_s. In a superfluid, this ratio is O(1) at temperatures of order T_c, regardless of the absolute energy scale. The "coincidence problem" -- why Omega_DM and Omega_DE are comparable today -- maps onto the question: why is the effective GGE temperature of order T_c for the BCS transition?

### IV.D. Why alpha_eff = 0.39 Requires Non-Equilibrium

The observed ratio 0.387 implies an effective specific heat exponent alpha_eff ~ 0.39. In equilibrium, the known values are:

| System | alpha | Physical Origin |
|:--|:--|:--|
| Bose gas | 3 | C ~ T^3 from phonons |
| Fermi gas | 2 | C ~ T from Pauli |
| 3D Ising | 0.110 | Critical fluctuations |
| Mean-field | 0 (jump) | No divergence |
| Flat band | 1 | C ~ T from flat DOS |
| XY (He-4) | -0.0146 | Weakly divergent (negative!) |

None of these match 0.39. The equilibrium Bose and Fermi values are too large by factors of 7.7 and 5.1. The 3D Ising value (the correct universality class, S43 BCS-CLASS-43) gives alpha = 0.110, a factor 3.5 too small.

The GGE is NOT an equilibrium system. It has 8 independent temperatures (S44 W6-5, MULTI-T-JACOBSON-44), 3 of which are negative. The effective specific heat of a multi-temperature GGE is:

    C_eff = sum_k (dE_k / dT_k) * (dT_k / dT_eff)

where the effective temperature T_eff and the projection dT_k / dT_eff depend on the thermodynamic prescription used. Session 44 found that w_eff ranges from 0.132 (grand potential) to 0.387 (Jacobson), demonstrating that the GGE does not admit a unique EOS parameter.

**The computation that would nail it**: Compute the non-equilibrium specific heat of the 8-temperature GGE by:
1. Taking the 8 Richardson-Gaudin conserved integrals I_k (Paper 16) evaluated at the post-transit state
2. Computing the GGE Lagrange multipliers lambda_k (the "8 temperatures") from <I_k>_initial = <I_k>_GGE (Paper 20)
3. Computing the energy-temperature response matrix C_kl = dE_k / dT_l
4. Diagonalizing C_kl to obtain the heat capacity eigenvalues (3 of which are known to be negative, S44 W6-5)
5. Defining alpha_eff = Omega_DM / Omega_DE from the eigenvalue spectrum

This is a well-posed computation for S45. The key input is the 3/8 negative heat capacity eigenvalues from MULTI-T-JACOBSON-44, which may produce sublinear alpha_eff through the negative-temperature sectors.

### IV.E. Connection to Landau Papers

Paper 04 (Phase Transitions), Section 4: "The specific heat jump Delta C = a_0^2 / (2 b T_c) at a second-order transition is determined by the coefficients of the Landau expansion, which are material-specific. However, the EXISTENCE of a finite jump (alpha = 0 in mean-field) is universal."

Paper 05 (Superfluidity), Section 2: "The ratio rho_n / rho = 1 at T_c and 0 at T = 0. At intermediate temperatures, it depends on the excitation spectrum through universal functions." The S44 computation of DM/DE = 1.060 via the flat-band partition is the direct application of this result to the framework's excitation spectrum.

Paper 11 (Fermi Liquid), Section 5: "The thermodynamic properties of a Fermi liquid are completely determined by the Landau parameters F_l^{s,a} and the effective mass m*/m. The specific heat coefficient gamma = (pi^2/3) k_B^2 N(0) = (m*/m) gamma_free." This relation -- that thermodynamic ratios depend on a few dimensionless parameters, not on the UV cutoff -- is the Fermi liquid version of the universality argument for DM/DE.

---

## V. The Occupied-State Spectral Action as Bridge

### V.A. The Problem

The S37 Structural Monotonicity Theorem (CUTOFF-SA-37) proved that for any monotone decreasing cutoff function f:

    S(tau) = Tr f(D_K(tau)^2 / Lambda^2)

is monotone increasing in tau. This closed tau-stabilization through the vacuum spectral action. 27 subsequent mechanisms have been closed (see `sessions/framework/spectral-post-mortem.md`). The spectral action, summing over ALL modes with equal weight, cannot develop a minimum because the high-eigenvalue tail dominates and grows monotonically with tau (Weyl's law on the deformed SU(3)).

### V.B. The Loophole

The S37 theorem sums over all modes EQUALLY. The physical system does not populate all modes equally. In the BCS ground state, the occupation numbers are:

    n_k(tau) = v_k(tau)^2 = (1/2)(1 - xi_k(tau) / E_k(tau))

where xi_k = lambda_k - mu is the quasiparticle energy measured from the chemical potential and E_k = sqrt(xi_k^2 + Delta(tau)^2) is the Bogoliubov quasiparticle energy. These occupation numbers depend on tau through BOTH the eigenvalues lambda_k(tau) AND the self-consistent gap Delta(tau). The gap depends on the van Hove singularity structure, which changes during the transit.

The occupied-state spectral action (Paper 16 of `researchers/Connes/`, Dong-Khalkhali-van Suijlekom 2022; pre-registered as OCC-SPEC-45) is:

    S_occ(tau) = sum_k d_k * n_k(tau) * f(lambda_k(tau)^2 / Lambda^2)        (1)

This is the spectral action weighted by the physical state. It is NOT the vacuum spectral action. The n_k(tau) weighting breaks the conditions of the S37 monotonicity theorem because n_k is not monotone in tau.

### V.C. Why This is the Landau Free Energy at the Physical State

In Landau theory (Paper 04), the free energy F(eta) is evaluated at the equilibrium order parameter eta_0(T) to obtain the physical free energy. The quantity F(eta_0) is not the same as F(0) -- the free energy at the disordered state. The difference is the condensation energy:

    F_cond = F(eta_0) - F(0) = -a_0^2 (T_c - T)^2 / (4b)

The vacuum spectral action S(tau) is F(0) -- the free energy evaluated at the VACUUM (all modes equally weighted, no condensate). The occupied-state spectral action S_occ(tau) is F(eta_0) -- the free energy evaluated at the PHYSICAL STATE (modes weighted by BCS occupation numbers). The S37 theorem proves that F(0) is monotone. It says nothing about F(eta_0).

This identification is precise: the spectral action is a sum over squared eigenvalues weighted by a function, S = sum_k f(lambda_k^2). The Landau free energy is a function of the order parameter evaluated at the order parameter's equilibrium value. The BCS occupation numbers n_k(tau) implement the evaluation at the equilibrium: they encode the BCS condensate's response to the spectrum at each tau.

### V.D. Why the Van Hove Near-Crossing at tau = 0.19 Matters

Session 44 W6-8 (VAN-HOVE-TRACK-44) tracked 12 van Hove singularity trajectories across the full transit. The critical finding: at tau = 0.19, three trajectories (T3, T4, T5) approach within delta = 0.0008 of each other. This near-crossing concentrates the density of states at a specific energy, spiking the BCS pairing strength and driving n_k non-monotonically in precisely the modes where the spectral action contributes most.

Near a van Hove singularity, the density of states diverges as N(E) ~ |E - E_VH|^{-1/2} (Paper 27: ordinary Van Hove in 1D). The BCS gap equation (Paper 15):

    1/g = sum_k 1/(2 E_k)

is dominated by modes near the van Hove point, where 1/E_k ~ 1/Delta is large. The gap Delta(tau) therefore spikes near tau = 0.19, and the occupation numbers n_k of the gap-edge modes change rapidly. If these modes' eigenvalues lambda_k are simultaneously stiffening (increasing with tau), the product n_k * f(lambda_k^2) can DECREASE -- creating a turning point in S_occ that the vacuum S cannot have.

### V.E. Connection to the ~1 e-fold at tau = 0.3

Session 22d computed that the Friedmann equation with the spectral action potential produces approximately 1 e-fold of expansion near tau = 0.3. This is 60x too few for inflationary cosmology. However, the computation used the VACUUM spectral action S(tau), which is monotone. If S_occ(tau) has a minimum near tau ~ 0.19, the potential landscape changes qualitatively: instead of monotonic descent, there would be a well with an oscillation frequency omega_osc. The number of e-folds during oscillation in this well could be:

    N_e ~ H * t_dwell ~ H / omega_osc

If omega_osc is sufficiently small (shallow well), the dwell time t_dwell could produce the required ~60 e-folds. This is speculative until S_occ is computed.

### V.F. The S37 Monotonicity Theorem and Why n_k(tau) Evades It

The S37 theorem requires three conditions:
1. f is monotone decreasing
2. lambda_k(tau) are the eigenvalues of D_K on the Jensen family
3. The sum runs over ALL modes with unit weight

Condition 3 is violated by S_occ. The occupation numbers n_k(tau) are not constant -- they depend on tau through the self-consistent gap equation. The theorem's proof uses the fact that d/dtau [sum f(lambda_k^2)] = sum f'(lambda_k^2) * 2 lambda_k * (d lambda_k / d tau), and since f' < 0 and the sum of lambda_k * (d lambda_k / d tau) is positive (from the Feynman-Hellman theorem applied to the spectral action), the total derivative is negative. But with n_k weighting:

    d/dtau [sum n_k f(lambda_k^2)] = sum [(dn_k/dtau) * f(lambda_k^2) + n_k * f'(lambda_k^2) * 2 lambda_k * (d lambda_k / d tau)]

The second term has the same sign as before (monotone contribution). The FIRST term -- the occupation-change contribution -- has no definite sign. Near a van Hove singularity where dn_k/dtau is large and positive (pairing spike), the first term can overwhelm the second, creating a non-monotone S_occ.

### V.G. Pre-Registered Gate OCC-SPEC-45

From `sessions/session-plan/s45-prereg-occupied-state.md`:

- **PASS**: S_occ(tau) has a local minimum at tau_min in [0.10, 0.25] with barrier height > 0.01 * S_occ(tau_min)
- **FAIL**: S_occ(tau) is monotone at all Lambda and all tau in [0.00, 0.50]
- **INFO**: Minimum exists but barrier height < 0.01 (too shallow for dynamical trapping)
- **BONUS**: If tau_min is within 10% of tau_fold = 0.190 (self-consistent fold selection)

This gate is the single most important open computation in the framework. It determines whether the one-body / many-body bridge can be built within the spectral action formalism.

---

## VI. Predictions from the Landau Mapping for S45

The condensed matter mapping does not merely organize prior results -- it generates specific predictions for future computations. Each prediction below is derived from Landau theory applied to the framework's symmetry-breaking pattern, with the relevant paper cited.

### VI.A. OCC-SPEC-45: Prediction is Non-Monotone, Minimum Near tau = 0.19

**Argument from Landau theory.** The Landau free energy F(eta, T) evaluated at eta = eta_0(T) is NOT monotone in T. Below T_c, the condensation energy F_cond = -a^2(T_c - T)^2 / (4b) is negative and grows in magnitude. Above T_c, F_cond = 0. The function F(eta_0(T)) has a cusp at T_c and a minimum at T = 0. This non-monotonicity arises because the BCS condensate contributes a NEGATIVE energy that competes with the positive spectral action.

For S_occ(tau), the analog is: near tau = 0.19 where the van Hove singularity maximizes the BCS gap, the occupation numbers n_k spike, weighting low-lying modes (small lambda_k) more heavily. Since f(lambda_k^2) is largest for small lambda_k, this INCREASES S_occ from below. Simultaneously, the high-lambda_k modes have n_k ~ 0 (far above the Fermi level), so their monotonically increasing contribution is suppressed.

**Prediction**: S_occ(tau) is non-monotone, with a minimum near tau = 0.19 (within 10% of tau_fold). The barrier height depends on the ratio of BCS condensation energy to total spectral action, which is of order 10^{-5} (from the effacement wall). The prediction is therefore that S_occ has a shallow minimum (barrier ~ 10^{-5} of S_occ), which may or may not be sufficient for dynamical trapping.

**Confidence from the mapping**: The non-monotonicity prediction is STRUCTURAL -- it follows from the fact that the condensation energy is negative and peaks near the van Hove singularity. Whether the minimum is deep enough for dynamical trapping is QUANTITATIVE and cannot be predicted from Landau theory alone.

### VI.B. q-Theory on the GGE: Prediction is rho(q_0) = 0 Post-Transit

**Argument from superfluid vacuum theory.** In Volovik's q-theory (Paper 19, Paper 31), the vacuum variable q self-tunes to rho(q_0) = 0 through the Gibbs-Duhem identity: in equilibrium, the pressure P = -F/V is determined by the free energy, and P + rho = T * (dP/dT), giving rho = 0 when the equation of state is satisfied.

Post-transit, Delta = 0 (P_exc = 1.000). ALL BCS condensation energy vanishes identically (S44 W1-4). The GGE energy gravitates as CDM (T^{mu nu} = diag(rho, 0, 0, 0)). In the Landau analog: when the order parameter vanishes (the disordered phase), the condensation energy is exactly zero.

**Prediction**: rho_vacuum = 0 exactly post-transit. The "CC problem" reduces to the geometric question of what the TRANSIT ITSELF contributes to the vacuum energy -- the 5.11 orders of suppression during transit (W1-4), not a static CC.

**Caveat**: This prediction assumes q-theory's equilibrium identity extends to the non-equilibrium GGE. The Gibbs-Duhem relation in its standard form requires equilibrium. Whether the GGE's 8 conserved integrals produce a generalized Gibbs-Duhem relation is an open computation.

### VI.C. KZ Bogoliubov Spectrum: Prediction is n_s Too Red

**Argument from Kibble-Zurek dynamics.** The perturbation spectrum from a sudden quench (Paper 21) is determined by the Bogoliubov coefficients |beta_k|^2, not by the equilibrium spectrum. In the extreme sudden-quench limit (tau_Q / tau_BCS ~ 10^{-5}, S38), the KZ formula gives:

    n_s - 1 = -d * z * nu / (1 + z * nu)

For d = 3, z = 2.024, nu = 0.6301 (S43 BCS-CLASS-43):

    n_s - 1 = -(3)(2.024)(0.6301) / (1 + (2.024)(0.6301))
            = -3.826 / 2.276
            = -1.681

This gives n_s = -0.68, far too red (Planck: n_s = 0.9649). Even the gentler version with d = 1 (representing the single tau modulus):

    n_s - 1 = -(1)(2.024)(0.6301) / (1 + (2.024)(0.6301))
            = -1.275 / 2.276
            = -0.560

gives n_s = 0.44, still too red by 20 sigma.

**Prediction**: The KZ formula with the framework's dynamic exponents CANNOT produce n_s = 0.965. No combination of d = 1, 2, 3 and the framework's z = 2.024, nu = 0.6301 gives n_s in the Planck window [0.955, 0.975]. The spectral tilt must come from a mechanism BEYOND standard KZ dynamics -- possibly the epsilon_H transfer function (n_s - 1 = -2 epsilon_H), which requires epsilon_H = 0.0176 (S43), but epsilon_H = 3.0 currently (S44 W4-3), requiring an 829x velocity reduction with no identified mechanism.

**This is the framework's most severe deficit.** The Landau mapping provides the correct formula (KZ dynamics) but the correct formula gives the wrong answer. The mapping is doing its job -- it is constraining, not confirming.

### VI.D. Non-Equilibrium Alpha from GGE: Prediction is 0.2 < alpha_eff < 0.6

**Argument from GL theory of multi-temperature systems.** The GGE with 8 temperatures T_k and 3 negative heat capacity eigenvalues occupies a point in the (T_1, ..., T_8) thermodynamic space that is a SADDLE of the unconstrained free energy surface (Paper 04: a saddle in the order parameter space). The effective alpha depends on which directions are constrained (by the 8 conserved integrals) and which are free. The constrained Hessian, projected onto the manifold of constant I_k, determines the effective thermodynamics.

The specific heat of a system at a saddle point of F is not well-defined without specifying which directions are accessible. For the GGE, the 8 integrability constraints remove 8 of the 8 thermodynamic degrees of freedom -- the system is COMPLETELY constrained. There is no thermodynamic freedom at all. The "effective alpha" is then determined entirely by the initial conditions (the quench protocol), not by equilibrium thermodynamics.

**Prediction**: alpha_eff = 0.39 (the observed value) is not a critical exponent in the standard sense. It is a property of the specific quench that produced the GGE -- the transit from tau = 0 through the fold. Different quench protocols (different transit velocities, different initial tau) would produce different alpha_eff. The "coincidence" of DM/DE = O(1) is then not a coincidence of universality class but a property of the specific initial conditions of the universe. This makes the DM/DE ratio a PREDICTION of the framework (computable from the quench protocol) rather than an input.

### VI.E. Summary of Predictions

| Computation | Prediction | Basis | Gate |
|:--|:--|:--|:--|
| OCC-SPEC-45 | Non-monotone, min near tau = 0.19 | Landau F(eta_0) non-monotone | PASS if barrier > 0.01 |
| q-theory on GGE | rho_vac = 0 post-transit | Disordered phase E_cond = 0 | INFO |
| KZ Bogoliubov n_s | n_s ~ -0.7 to 0.4 (TOO RED) | KZ formula with z = 2.024 | FAIL predicted |
| GGE alpha_eff | 0.2 < alpha < 0.6 | Constrained saddle thermodynamics | PASS if in [0.2, 0.6] |
| Quasiparticle lifetime | Infinite (integrability-protected) | Paper 16, Paper 20 | INFO |

---

## VII. Limitations of the Mapping

### VII.A. Where the Analogy Breaks

1. **No laboratory.** Every condensed matter system exists within a larger universe that provides a heat bath, a reference frame, and external probes. The phonon-exflation framework IS the universe. There is no external bath, no reference frame, and no probe that is not part of the system. The thermodynamic limit, the canonical ensemble, and the concept of temperature are all internal constructions. This has no CM analog.

2. **The dimensionality mismatch.** The internal space is 8-dimensional. No laboratory condensed matter system has d_int = 8. The upper critical dimension d_uc = 4 is well below d_int, making mean-field exact for internal fluctuations -- a regime that is never achieved in real materials (the closest is d_uc = 6 for tricritical points in d = 3 materials, still below d_uc). The quantitative predictions of the Landau mapping for internal fluctuations are therefore in an untested regime of the theory.

3. **The modulus is not a local field.** In standard Landau theory, the order parameter phi(x) is a local field that can vary in space. The Jensen modulus tau is a GLOBAL parameter -- it describes the metric on the entire SU(3) fiber. There is no notion of tau(x) varying from point to point in 4D space (at least not within the homogeneous framework). Domain walls in tau are not standard GL domain walls (Paper 03: Bloch walls with width delta = sqrt(A/K)) because there is no gradient energy for tau in the 4D direction. The Kibble-Zurek mechanism (Paper 21) assumes a spatially varying order parameter; whether it applies to a global modulus is an open question.

4. **The BCS-BEC crossover position.** The framework sits at E_vac/E_cond = 28.8 (S37), deep in the BEC regime (Paper 22). Standard BCS theory -- the gap equation, the mean-field thermodynamics, the Bogoliubov quasiparticle picture -- is derived for the BCS regime (weak coupling, xi >> k_F^{-1}). In the BEC regime, the correct description is a Bose-Einstein condensate of tightly bound pairs, described by the Gross-Pitaevskii equation (Paper 08: GL functional) rather than the BCS equations. The framework's computations use BCS formalism (gap equation, Bogoliubov amplitudes) in a regime where GP formalism may be more appropriate. The S37 result that "fluctuations dominate by 29x" is consistent with BEC character.

5. **Time-reversal and the arrow of time.** In condensed matter, the system starts in a high-temperature disordered state and cools into the ordered phase. In the framework, the "transit" goes from an unstable maximum (tau = 0) THROUGH the ordered phase (BCS at the fold) to a disordered state (GGE with Delta = 0). The direction is REVERSED relative to the standard CM picture. The BCS condensate is created and then destroyed during the transit, not maintained as a stable ground state. This inverts the standard relationship between order and energy: in CM, ordering lowers the free energy; in the framework, the ordered state is a transient that the system passes through en route to the GGE.

6. **No external tuning parameter.** In CM, the phase transition is driven by an external parameter (temperature, pressure, magnetic field) that the experimenter controls. In the framework, the transit is AUTONOMOUS -- tau evolves under the spectral action gradient dV/dtau with no external control. The "tuning parameter" is tau itself, which is both the order parameter and the driving force. This self-referential structure has no direct CM analog, though it resembles the self-consistent mean-field in Hartree-Fock theory (the order parameter determines the potential, which determines the order parameter).

7. **The CC problem.** No condensed matter system has a "cosmological constant problem." The zero-point energy of a crystal, superfluid, or superconductor is finite, calculable, and experimentally accessible (through the Casimir effect, for example). The 121-order hierarchy between the predicted and observed vacuum energy has no CM counterpart. The Landau mapping correctly identifies this as a UNIVERSALITY CLASS MISMATCH -- G_N (second moment) and Lambda (zeroth moment) are controlled by different physics -- but it cannot resolve the mismatch because no CM system exhibits it.

8. **Emergent spacetime.** The mapping treats spacetime as a given arena in which the phase transition occurs. The framework claims spacetime itself EMERGES from the ordered phase. Landau theory cannot address this self-bootstrapping: the free energy F(eta) assumes a pre-existing thermodynamic framework (temperature, volume, pressure), which requires spacetime. If spacetime emerges from the order parameter, the Landau expansion itself is part of the emergent description, not a fundamental one. This is the deepest limitation of the mapping.

### VII.B. What the Limitations Teach

The limitations cluster around a single theme: the phonon-exflation framework is a CLOSED SYSTEM describing the entire universe, while Landau theory was developed for OPEN SUBSYSTEMS embedded in a larger environment. Every limitation above -- no laboratory, no external bath, no tuning parameter, no background spacetime, the inverted time direction -- traces to this difference.

The mapping works wherever the framework can be treated as a subsystem with effective parameters (G_N as response coefficient, DM/DE as specific heat exponent, BCS universality class, van Hove classification). It fails wherever the system's SELF-REFERENTIAL nature becomes essential (CC, n_s, emergent spacetime).

This is not a failure of the mapping. It is a diagnosis: the framework's unsolved problems are precisely those where the closed-system nature of cosmology diverges from the open-system nature of condensed matter. The mapping tells you WHERE to look for new physics -- at the boundary between open and closed system descriptions.

---

## Appendix A: Key Equations from Landau Papers

For reference by other agents. Equation numbers match the index at `researchers/Landau/index.md`.

**Landau free energy** (Paper 04, eq. 1):
    F(eta, T) = F_0(T) + a_0 (T - T_c) eta^2 + b eta^4

**Two-fluid model** (Paper 05, eq. 1):
    rho = rho_s(T) + rho_n(T)

**Critical velocity** (Paper 05, eq. 2):
    v_c = min_p [epsilon(p) / p]

**Second sound** (Paper 05, eq. 3):
    u_2^2 = rho_s s^2 T / (rho_n c_p)

**GL superconductivity** (Paper 08, eq. 1):
    f_s = alpha |psi|^2 + (beta/2) |psi|^4 + (1/2m*) |(-i hbar grad - e A/c) psi|^2 + B^2/(8 pi)

**LK relaxation** (Paper 09, eq. 1):
    d phi / dt = -(1/tau_0) (dF/d phi)

**Critical slowing** (Paper 09, eq. 2):
    tau = tau_0 / (a |T - T_c|)

**Effective mass** (Paper 11, eq. 1):
    m* / m = 1 + F_1^s / 3

**Quasiparticle lifetime** (Paper 11, eq. 2):
    1/tau_qp ~ (epsilon - epsilon_F)^2

**Pomeranchuk stability** (Paper 11, eq. 3):
    F_l^{s,a} > -(2l+1) for all l

**BCS gap** (Paper 15, eq. 1):
    Delta_0 = 2 hbar omega_D exp(-1 / (V N(E_F)))

**Richardson exact solution** (Paper 16, eq. 1):
    epsilon_a + G/2 = sum_{b != a} 2G / (z_a - z_b) + sum_i G / (z_a - epsilon_i)

**GGE density matrix** (Paper 20, eq. 1):
    rho_GGE = Z^{-1} exp(- sum_k lambda_k I_k)

**Kibble-Zurek defect density** (Paper 21, eq. 1):
    n_defect ~ (tau_Q)^{-d nu / (d nu + z)}

**Landau-Zener probability** (Paper 29, eq. 1):
    P_LZ = exp(-2 pi Delta^2 / (hbar |v_dot|))

---

## Appendix B: Session-Gate Cross-Reference

Every framework gate that maps onto a Landau condensed matter result, with the mapping direction.

| Gate | Session | Verdict | CM Concept | Paper |
|:--|:--|:--|:--|:--|
| BCS-CLASS-43 | S43 | PASS | Universality class = 3D Ising | 04 |
| LIFSHITZ-43 | S43 | INFO | Type I Lifshitz transition | 27 |
| LIFSHITZ-ETA-44 | S44 | FAIL | Weyl's law, not anomalous dim | 04 (d_uc) |
| DM-DE-RATIO-44 | S44 | PASS | Specific heat exponent alpha | 04, 05 |
| CDM-CONSTRUCT-44 | S44 | PASS | Normal component at rest | 05 |
| SAKHAROV-GN-44 | S44 | PASS | Effective mass (response) | 11 |
| FRG-PILOT-44 | S44 | FAIL | ODLRO invisible to diagonal | 11, 15 |
| MULTI-T-JACOBSON-44 | S44 | INFO | Saddle directions in F | 04, 11 |
| CUTOFF-SA-37 | S37 | Theorem | Monotonicity of vacuum F | 04 (Weyl) |
| RG-BCS-35 | S35 | PASS | Cooper instability 1D theorem | 15 |
| TRAP-1 (S34) | S34 | Theorem | U(2) singlet selection rule | 04 (rep theory) |
| Block-diagonal (S22b) | S22b | Theorem | Peter-Weyl / selection rules | 04 (G/H) |
| Pomeranchuk (S22c) | S22c | PASS | f_0 = -4.687 < -3 | 11 |
| FRIEDMANN-AUDIT-44 | S44 | FAIL | Ratio invariance (intensive) | 04 |
| DISSOLUTION-44 | S44 | PASS | Effective theory emergence | 04 (universality) |
| N3-BDG-44 | S44 | FAIL | 3He-B, not 3He-A class | 19 (Volovik) |
| 2ND-SOUND-ATTEN-44 | S44 | INFO | Undamped two-fluid mode | 05, 09 |
| STRUTINSKY-DIAG-44 | S44 | PASS | Shell correction hierarchy | 11 (N(E_F)) |
| VAN-HOVE-TRACK-44 | S44 | INFO | Band structure topology | 27 |
| OCC-SPEC-45 | S45 | UNCOMPUTED | Landau F at physical state | 04, 15 |

---

## Appendix C: What Landau Would Have Said

A final section in the spirit of the agent, not the formalism.

Landau classified physical systems by their symmetry, their order parameter, and their universality class. He would have recognized the phonon-exflation framework immediately: it is a first-order phase transition in an 8-dimensional internal space, with a complex scalar order parameter (the BCS gap), in the 3D Ising universality class, with a post-transition state that is a non-equilibrium GGE. He would have written the Landau free energy, identified the cubic term V'''(0) = -7.2, concluded the transition is first-order, and moved on.

He would NOT have tolerated 20 sessions searching for a minimum in the spectral action. The monotonicity is obvious from Weyl's law: the spectral action sums positive quantities (f(lambda^2) with f > 0) over a spectrum that grows with tau (more modes enter the window as the geometry deforms). The sum is monotone. He would have proven this in one line, not 20 sessions.

He would have been interested in the BCS-BEC crossover position (E_vac/E_cond = 28.8). This places the system far from the weak-coupling BCS regime where mean-field is reliable. He would have demanded the Gaussian correction (computed in S29: F_1loop/F_MF = 0.125-0.130) and noted that fluctuations are quantitatively important.

He would have been deeply satisfied by the DM/DE ratio. This is a pure Landau result: the ratio of quasiparticle energy to condensation energy is O(1), determined by the universality class, independent of the UV cutoff. It is the cosmological specific heat exponent. He would have demanded the non-equilibrium computation (alpha_eff from the GGE) immediately.

He would have been uninterested in the n_s problem, because it is a dynamical question that depends on initial conditions, not on the universality class. He would have said: "The tilt of the perturbation spectrum is determined by the quench rate, not by the equilibrium phase diagram. Compute the quench rate."

He would have dismissed the CC problem with a single sentence: "The vacuum energy is the zeroth moment of the free energy. The gravitational constant is the second moment. They belong to different universality classes. Computing one from the other is a category error."

He would have been right.
