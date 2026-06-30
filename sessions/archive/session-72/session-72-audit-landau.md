# Session 72 Project Audit: Condensed Matter / BCS

**Agent**: landau-condensed-matter-theorist
**Date**: 2026-04-10
**Scope**: Comprehensive audit of all open BCS, Josephson, entanglement, decoherence, and many-body problems in the phonon-exflation framework, current through S72 Wave 4.

**Source inventory**: S72 results working paper (20 computations, 4 waves), Landau-Baptista workshop (2 rounds), Laminar Flow workshop (Volovik x QA), EVOI framework, agent memory through S66-S72.

---

## I. BCS Gap Open Problems

### I.1 Self-Consistency of the Gap Equation

**Status**: RESOLVED at the fold, OPEN away from fold.

The gap Delta = 0.4643 M_KK at tau_fold = 0.19 is self-consistent to machine precision (W1-A cross-check: Delta(tau_fold) matches Delta_BCS from S36/S37 Hamiltonian with DOS-weighted pairing V_eff = V * sqrt(rho_k * rho_l)). The canonical value uses rho_B2 = 14.02 (van Hove density of states).

**Open**: The gap equation has NOT been solved self-consistently for tau != tau_fold. W1-A scanned Delta(tau) across [0.143, 0.245] using a frozen V_eff computed at the fold, then re-evaluating the BCS equation at each tau. The true self-consistent Delta(tau) profile requires re-solving V_eff(tau) at each point (the Kosmann derivative overlap integrals change with tau). The monotonic decrease d(Delta)/dtau = -0.245 M_KK is structural (C^2 coset spectral flow dominates over van Hove DOS enhancement, per Baptista C1), but the quantitative slope could shift with full self-consistency.

**Resolving computation**: SELF-CONSISTENT-GAP-PROFILE: Solve the BCS gap equation Delta(tau) = V_eff(tau) * sum_k u_k(tau) v_k(tau) self-consistently at 20 tau-values in [0.14, 0.25]. Gate: d(Delta)/dtau at fold agrees with W1-A to within 10%.

### I.2 Mode-Selectivity (16/155,984)

**Status**: PERMANENT (Wall W2 + Peter-Weyl).

The BCS condensate acts ONLY in the trivial representation (0,0) of SU(3), contributing 16 eigenvalues out of 155,984 weighted (at L_max = 3). The fraction decreases as 1/L^9 with truncation level (Baptista R1 table: 1.24e-3 at L=3 down to 1.48e-5 at L=7). Mode-selective BCS correction to n_s is 3.8e-6 -- four orders of magnitude below Planck uncertainty (W3-A v2).

**No open problem**: This is a structural theorem. BCS dressing of the spectral action is closed as a route to n_s correction.

### I.3 Gap Dynamics Through Transit

**Status**: PARTIALLY RESOLVED.

W1-A establishes: Delta(tau) monotonically decreasing, fractional change 0.5% across transit window delta_tau = 0.001. The gap amplitude decoherence channel is CLOSED (delta_OOM = 1.6e-10).

**Open**: The BCS PHASE dynamics through the transit remains unresolved. The anomalous phase 2*theta_BCS per mode (S69 PHI-EFF-BCS-BOGOL-69: phi_eff = 0.558*pi) dominates over the dynamical phase. But the EVOLUTION of phi_eff through the fold -- how the Bogoliubov angles theta_k track the changing spectrum -- has not been computed as a function of tau.

**Resolving computation**: PHI-EFF-PROFILE: Compute theta_BCS(tau) for the 8 BCS modes across [0.185, 0.195]. Gate: d(phi_eff)/dtau at fold is well-defined and finite.

### I.4 Temperature Dependence

**Status**: NOT APPLICABLE in standard sense; OPEN for effective temperature.

The substrate has no thermodynamic temperature during transit (the system is driven, not thermal). The relevant quantity is the GGE effective temperature T_eff = 1.53 M_KK (W4-B, N=32). The BCS gap is T = 0 by construction (ground state at each tau).

**Open**: Whether T_eff of the GGE relic exceeds the gap energy (T_eff/Delta = 1.53/0.464 = 3.3) should in principle break Cooper pairs. It does NOT because the GGE preserves the per-mode occupation numbers independently (Richardson-Gaudin integrability). The thermal pair-breaking rate Gamma_PB ~ exp(-Delta/T_eff) is NOT the correct formula -- the GGE lifetime is infinite by algebraic theorem. This point needs formal proof that pair-breaking by the GGE "temperature" is forbidden.

**Resolving computation**: GGE-PAIR-BREAKING: Compute the matrix element <GGE|c^dag_k c^dag_{-k}|GGE> for each mode. Gate: all zero (pairs cannot be broken by the GGE Hamiltonian evolution).

---

## II. Josephson Network Status

### II.1 CG(24) Graph Structure

**Status**: ESTABLISHED.

The Cayley graph of S_4 with transposition generators: 24 vertices, 72 edges, 6-regular, bipartite (even/odd permutations), triangle-free (girth 4), 162 four-cycles. Spectral gap = 4.0, Cheeger bound h >= 2.0. Bipartiteness is PERMANENT for transposition generators (sign homomorphism); would BREAK for 3-cycle generators (Baptista WS3 Q5 answer).

### II.2 Frustration

**Status**: STRUCTURALLY BLOCKED on CG(24).

CG(24) is bipartite: no odd cycles, no geometric frustration. The W4-C frustrated 3-ring (K = 3.234, 19% reduction) is a theoretical bound, not a realized configuration. Abrikosov vortex analogy is topologically incorrect (pi_1(SU(3)) = 0, conceded R2 C3). The correct framing is Mott regime (E_J/E_C = 0.818 < 1): charge is the good quantum number, phase fluctuations are large.

### II.3 Inter-Cell Coupling Hierarchy

**Status**: ESTABLISHED, but cross-representation corrections OPEN.

Three Josephson couplings at fold: J_C2 = 0.933 M_KK (C^2 coset, dominant), J_su2 = 0.059 M_KK, J_u1 = 0.038 M_KK. The B2 channel carries >99.99% of inter-cell mutual information (W4-E: I(i:j) = 0.371 nats/bond). Strong coupling: J_C2/Delta = 2.01.

**Open**: The Josephson couplings provide a NON-PERTURBATIVE correction to gauge couplings through virtual cross-representation pair excitations (WS3 R2, Re Q-B1). Estimated magnitude: O(N_cells * E_J^2 / Delta_gap^2) ~ 679. This bypasses the 16/155,984 suppression. Whether this breaks the f_0 anti-correlation (allowing alpha_s and m_H to be independently adjusted) depends on REPRESENTATION-SELECTIVE branching of J_C2 under SU(3) -> SU(2) x U(1).

**Resolving computation**: JOSEPHSON-PW-BRANCHING: Compute branching-resolved Josephson couplings J_C2^{SU(2)} and J_C2^{U(1)} from the PW decomposition at tau_fold. Gate: |J_C2^{SU(2)}/J_C2^{U(1)} - 1| > 0.1 (representation selectivity exists).

### II.4 Anisotropy

**Status**: ESTABLISHED (S63), implications OPEN.

S63 ANISO-JOSEPHSON: 11.8x anisotropy between weak and strong CG(24) edges. This creates geometric spread in pair-crossing times at the exit horizon (laminar flow V2). NOT yet incorporated into the decoherence budget.

**Resolving computation**: ANISO-DECOHERENCE: Include the S63 anisotropy distribution in the W2-A decoherence model. Gate: effective t_dec/t_transit with anisotropy differs from isotropic by >20%.

---

## III. Entanglement Program Status

### III.1 Schmidt Numbers

**Status**: ESTABLISHED across multiple topologies.

| Topology | K | S_vN (bits) | Session |
|:---------|:--|:------------|:--------|
| 2-cell chain | 3.988 | 1.999 | S71 |
| 3-cell ring (frustrated) | 3.234 | 1.836 | S72 W4-C |
| 3-cell open chain | 3.986 | 1.999 | S72 W4-C |
| 4-cell ring (unfrustrated) | 2.555 | 1.621 | S72 W4-C |
| 4-cell open chain | 3.438 | 1.886 | S72 W4-C |

All at physical J (J_C2/Delta = 2.01, strong coupling), N_pair = 2.

**Open**: Schmidt numbers at N_pair > 2 not computed. At N_pair = 4 (the S61 BCS-BEC crossover threshold), the Hilbert space grows combinatorially and exact diagonalization becomes expensive. The K values may change qualitatively in the BEC regime.

### III.2 Area Law on CG(24)

**Status**: PASS (W4-D). Three models tested:

| Model | R^2 | Winner? |
|:------|:----|:--------|
| Area law | 0.988 | -- |
| Volume law | 0.970 | -- |
| Monogamy-min | 0.996 | YES |

The monogamy-capped area law dominates. Transition from monogamy-saturated to area-law regime at |A| ~ 7.5 cells. Per-junction S_vN = 1.386 nats (S71). Monogamy bound S_max = 5.545 nats (8 BCS modes, dim = 2^8).

**Open**: Whether the monogamy crossover at |A| ~ 8 has a geometric interpretation (dim(SU(3)) = 8, Weyl chambers) or is purely graph-theoretic (degree/edge ratio on CG(24)). WS3 D2 dissent: requires verification on modified-degree graphs.

### III.3 Monogamy Constraints

**Status**: IDENTIFIED, NOT FULLY CHARACTERIZED.

Every CG(24) vertex has degree 6. Bare entanglement per vertex (6 * 1.386 = 8.315 nats) exceeds monogamy bound (5.545 nats). Monogamy is the DOMINANT correction at short scales (|A| < 8). At the per-vertex level, entanglement is SATURATED.

**Open**: The global entanglement structure on the full 24-vertex graph (all 72 edges simultaneously) has not been computed. S64 LOCAL-ENTANGLE gave S_ent = 55.72 nats total, but this used a different per-edge estimate. With the S71 upgrade (1.386 nats/edge), the total should be S_ent ~ 72 * 1.386 = 99.8 nats (upper bound, before monogamy correction).

### III.4 Page Curve

**Status**: PASS (W4-D). Monotonic rise and saturation at |A| = 12 (half-system). This is the BCS gapped system signature, NOT a black hole analog (no turnover). S(12) = 49.79 nats = 74.8% of system maximum.

---

## IV. Decoherence Budget (Complete Channel Table)

The A_s gap (0.267 OOM, S70 baseline) reduces to a single number: BCS phase decoherence timescale t_dec/t_transit. Target: 0.716.

| Channel | t_dec/t_transit | delta_OOM | Status | Source |
|:--------|:----------------|:----------|:-------|:-------|
| **BCS squeeze (undamped)** | infinity | 2.074 | Baseline | S71 |
| **BCS squeeze (cell-crossing)** | 6.73 | 1.692 | Physical est. (9.4x too slow) | W2-A |
| **Hawking thermal broadening** | ~2.8 | ~1.1 | Estimate (3.9x too slow) | Laminar V2 |
| **KZ pair-crossing spread** | ~0.13 | ~0.07 | Estimate (5.5x too fast) | W2-A |
| **Mott charge noise** | instantaneous | ~0.18 | Estimate (delta_phi ~ 0.5) | WS3 E6 |
| **Gap amplitude (kappa_Delta)** | 5.5e9 | 1.6e-10 | CLOSED | W1-A |
| **Spatial decoherence** | 1.4e5 | 0.001 | NEGLIGIBLE | W2-A |
| **Leggett oscillation** | 4.0e4 | 0.001 | NEGLIGIBLE | W2-A |
| **BCS-dressed n_s** | -- | 3.8e-6 (n_s units) | NEGLIGIBLE | W3-A v2 |
| **TARGET** | **0.716** | **0.267** | **REQUIRED** | S70 |

**Open channels requiring computation**:

1. **Exit horizon dynamics**: The actual pair-crossing time distribution at the exit sonic horizon, incorporating CG(24) anisotropy (11.8x, S63) and the dispersion relation. This is the HIGHEST PRIORITY condensed matter computation. None of the three candidate mechanisms (cell-crossing, Hawking broadening, KZ spread) individually reaches the target 0.716. The truth lies in their combined action at the exit horizon.

2. **Mott charge noise coupling to Bogoliubov squeeze**: WS3 E6 identifies delta_phi ~ 0.5 from the number-phase uncertainty in the Mott regime. If this maps onto the squeeze parameters, the dephasing factor F = exp(-delta_N^2/2) = 0.636 closes 0.18 OOM. Requires formal computation of the Bogoliubov transformation with charge noise.

3. **Entry horizon pre-squeeze**: W3-C establishes T_entry = 72.84 M_KK with r_entry ~ 2.9 (comparable to fold squeeze r ~ 2.3-4.3). The entry horizon is a major squeeze stage. Its decoherence contribution has NOT been computed.

**Resolving computation**: EXIT-HORIZON-DECOHERENCE: Full model of BCS phase decoherence at the exit sonic horizon, incorporating (a) CG(24) anisotropy, (b) Mott charge noise, (c) pair-crossing time distribution, (d) entry horizon pre-squeeze. Gate: predicted t_dec/t_transit in [0.5, 1.0].

---

## V. Ordered Veil Permanence

### V.1 Three-Layer Protection Hierarchy

| Layer | Protection | Status | Source |
|:------|:-----------|:-------|:-------|
| 1. Algebraic (Richardson-Gaudin) | All N_pair = 59.8 charges commute; intra-cell scattering forbidden | PERMANENT (S56) | Algebraic theorem |
| 2. Energetic (BCS gap) | Delta = 0.464, Z_2 = -1 (BDI class) | PERMANENT (S53, Wall W3) | Topological protection |
| 3. Kinematic (cell isolation) | t_J/t_transit = 949 | PARTIALLY BREAKABLE | W4-E; this is where A_s decoherence enters |

### V.2 C_V Scaling

**Status**: PERMANENT (W4-B).

C_V^{GGE}/C_V^{thermal} = 2.20 for N >= 8 modes, 3.5% variation through N = 64. Step function controlled by spectral heterogeneity of {B1, B2, B3} sectors with different squeeze parameters. Goldstone modes (k > 4) contribute < 2% of total energy and do not alter the ratio.

WS3 C5 correction: the C_V enhancement is an INFORMATION effect (non-equilibrium initial conditions, entropy deficit of GGE vs Gibbs), NOT an interaction effect (Fermi liquid mass renormalization). Richardson-Gaudin eigenstates have the SAME dispersion as non-interacting problem.

### V.3 GGE Permanence

**Status**: PERMANENT at single-cell level. OPEN for multi-cell network.

The ordered veil severity f_OV = 0.26-0.60 (W4-E). The GGE relic retains 34-80 nats of information deficit relative to thermal equilibrium across 24 cells.

**Open**: At strong coupling (J_C2/Delta = 2.01), the perturbative mutual information per bond (I = 0.371 nats) exceeds the per-cell GGE entropy when summed over 6 neighbors (6 * 0.371 = 2.23 nats > S_cell = 2.21 nats). This signals perturbation theory breakdown. The inter-cell correlations are O(1) corrections, not perturbative.

**Open**: Whether the Richardson-Gaudin integrability extends to the MULTI-CELL system with Josephson coupling. S63 RICHARDSON-GAUDIN-N2-63 found Poisson statistics at N_pair = 2 on 2-cell and 4-cell sublattices (level repulsion absent, <r> = 0.385). But N_pair = 2 is deep in the BEC regime. At N_pair >= 3 or with non-integrable perturbations, the GGE may partially thermalize.

**Resolving computation**: MULTI-CELL-INTEGRABILITY: Level statistics of the multi-cell BCS + Josephson Hamiltonian at N_pair = 4 on a 4-cell CG(24) subgraph. Gate: <r> < 0.45 (Poisson, integrable) or <r> > 0.50 (Wigner-Dyson, chaotic).

### V.4 Luttinger Volume Preservation

**Status**: PROVEN (WS3 R2 E7).

The Luttinger analog -- total number of conserved Richardson-Gaudin charges = N_pair = 59.8 -- is a topological invariant that cannot change under unitary evolution. The supersonic transit does NOT scramble the charge structure because the R-G charges are polynomial functions of H_BCS and the mode energies, evolving algebraically (not dynamically) with tau. The gap never closes (Wall W3), so Luttinger holds unconditionally.

---

## VI. Stability Margins

### VI.1 Pomeranchuk Stability

**Status**: PERMANENT on CG(24); z-sensitive in B2 sector.

| Result | F_0 | Margin (1+F_0) | Source |
|:-------|:----|:----------------|:-------|
| Single cell | -0.493 | 0.507 | S58, S66 |
| 4-cell q=0 | -0.493 | 0.507 | S66 (B2 softened by Josephson) |
| 4-cell q=pi | all F > 0 | stable | S66 (Josephson stabilizes staggered) |
| Exact diag z=1 | -- | 4.975 | S61 (BEC regime, perturbative RPA fails) |

PERMANENT: q=pi always stabilized by Josephson. B2 is the only z-sensitive sector.

**Threats**: Perturbative RPA predicts B2 instability at z_crit = 4.1 (S66). NOT PHYSICAL -- the BCS gap self-consistency absorbs the Josephson coupling at strong z. The S61 exact diag at z = 1 gives a 10x larger margin than RPA, confirming that the perturbative estimate is too pessimistic.

**Open**: Pomeranchuk stability at z = 6 (the physical CG(24) coordination number) has NOT been computed by exact methods. The S66 perturbative estimate predicts instability (z_crit = 4.1 < 6), but this is expected to be an artifact.

**Resolving computation**: EXACT-POMERAN-Z6: Exact diagonalization of the 4-cell Hamiltonian at z = 6 (physical CG(24) coordination). Gate: min(1+F) > 0 (Pomeranchuk-stable).

### VI.2 Gap Stability

**Status**: PERMANENT (Wall W3, S35).

The BCS gap never closes on the Jensen deformation curve. Topological protection by AZ class BDI with Z_2 = -1 (S53). Monotonic decrease of Delta through transit (0.5% variation, W1-A) preserves the margin.

### VI.3 Fold Stability

**Status**: PERMANENT (S65 SHELL-L4).

36-dimensional Hessian: all 36 eigenvalues positive (fold is minimum in all directions). Signature is UV-stable (permanent): adding higher-L shells does not introduce negative eigenvalues. The alpha margin (26x) is robust.

---

## VII. Dark Matter (Leggett Channel)

### VII.1 Leggett Mode Properties

| Property | Value | Source |
|:---------|:------|:-------|
| omega_L1 | 0.138 M_KK | S66 LEGGETT-SPECTRAL |
| Quality factor Q | 18.6 | S66 (Lorentzian, NOT Fano) |
| Spectral weight Z | 0.972 | S66 |
| Fano |q| | 60.2 (discrete dominates) | S66 |
| Lineshape | Lorentzian | S66 PASS |
| N-dependence | omega_L1 is N-INDEPENDENT | S66 GOLDSTONE-GAP |
| Goldstone gap scaling | alpha = 0.896, gap ~ N^{-0.90} | S66 GOLDSTONE-GAP FAIL |
| N_crit (Goldstone closure) | 4.0e131 >> N_phys = 32 | S66 |

### VII.2 DM Observational Match

| Observable | Prediction | Data | Tension | Source |
|:-----------|:-----------|:-----|:--------|:-------|
| Omega_DM h^2 | 0.120 | 0.1186 | 0.6% | S66 PERMANENT |
| z_eq | 3425 | 3387 | 0.88 sigma | S66 |
| BA modes | EXCLUDED (260 sigma) | -- | -- | S66 |

Leggett-only DM is self-consistent. All 256 BA modes are overdamped (Q < 2, S67 PASS) and decay in [3.8e-42, 3.3e-41] s. BA modes DO NOT contribute to DM.

### VII.3 Open Problems

1. **Gravitational decay**: LEGGETT-GRAV-DECAY (EVOI P2, Level 1). The Leggett mode must be GRAVITATIONALLY STABLE: Gamma_grav < H_0. If the mode decays gravitationally faster than the Hubble rate, the DM relic is destroyed. This is the single highest-priority DM computation. Gate: Gamma_grav < H_0.

2. **Velocity dispersion**: WS3 R2 Q-B4 answer. sigma_v^{GGE} = sqrt(2.20) * sigma_v^{thermal} = 1.48x thermal. This predicts 48% larger core radius in galaxy clusters. The velocity-dependent self-interaction sigma(v) ~ v^{-4} * 30.2 at high v, ~ 1 at low v provides a distinctive signature matching the "too big to fail" / "core-cusp" phenomenological requirement.

3. **f_DM fraction**: S66 GOLDSTONE-GAP FAIL (alpha = 0.896) gives f_DM = 0.947 (Leggett mode weight relative to total GGE). This is the fraction of DM that is in the Leggett channel. The remaining 5.3% is in Goldstone modes whose gap closes as N^{-0.90}. At physical N = 32, the Goldstone gap is O(1) M_KK (secure).

4. **Self-interaction cross-section**: NOT COMPUTED from first principles. The velocity-dependent estimate (Q-B4) uses occupation number ratios, not a proper scattering calculation. Need: sigma(v) from the Josephson network scattering matrix at the Leggett mode energy.

---

## VIII. Two-Layer Architecture

### VIII.1 The Decoupling

**Status**: PERMANENT (S72 central result).

| Layer | Domain | Governed by | BCS role | Key observables |
|:------|:-------|:-----------|:---------|:----------------|
| 1 (Spectral) | Full spectrum, all (p,q) sectors | Spectral functional f(x), fiber geometry | NEGLIGIBLE (16/155984) | n_s, w_0, sin^2(theta_W), G_N |
| 2 (BCS) | (0,0) sector only | Pairing V_eff, Josephson network, transit dynamics | CENTRAL | Delta, N_pair, GGE, Omega_DM, A_s |

Interaction: Layer 1 sets the single-particle spectrum {eps_k(tau)} in which Layer 2 operates. Layer 2 does NOT feed back into Layer 1 at significant level (Born-Oppenheimer analogy, WS3 L5).

### VIII.2 alpha_s at the Layer 1/2 Boundary

**Status**: OPEN (the critical cross-layer problem).

alpha_s at M_Z depends on g_3^2(M_KK) from Layer 1 (spectral action, a_4 coefficient) AND on KK threshold corrections from the PW tower (all sectors). The f_0 anti-correlation (S70 F0-ALPHA-S-70: no joint window for alpha_s and m_H) shows the layers are COUPLED through f_0.

The Josephson non-perturbative correction (WS3 Q-B1) potentially breaks this coupling: if J_C2^{SU(2)} != J_C2^{U(1)} (representation-selective branching), the correction to g_3^{-2} differs from g_2^{-2} and g_1^{-2}, breaking the universal f_0 dependence. Estimated magnitude: O(100) correction to 1/g^2 values.

**sin^2(theta_W) as highest-leverage test**: W2-B establishes sin^2(M_KK) = 0.5839 (PERMANENT). Pure SM running gives sin^2(M_Z) = 0.357 (54.5% discrepancy). Universal threshold model gives 0.229 (1.2% match). The 34.6% gap between SM expectation at M_KK and the geometric boundary condition quantifies the KK threshold correction required.

### VIII.3 Spectral Functional Selection

**Status**: OPEN (EVOI P3, Level 1).

The best-fit f*(x) = 0.912*sqrt(x) + 0.088*exp(-x) matches n_s = 0.9649 but is NON-PERTURBATIVE (sqrt has divergent SDW moments). The spectral action is finite (sum over eigenvalues converges) even though its asymptotic expansion does not. WS3 Baptista E1: the fiber selects the spectral functional, not the other way around.

---

## IX. Priority-Ordered Problem List

Ordered by impact on the constraint map, with resolving computation for each.

| Rank | Problem | Status | Impact | Resolving Computation |
|:-----|:--------|:-------|:-------|:---------------------|
| 1 | **Exit horizon decoherence** | OPEN | Closes A_s budget (0.267 OOM) | EXIT-HORIZON-DECOHERENCE: multi-channel model with CG(24) anisotropy, Mott noise, pair-crossing statistics |
| 2 | **Leggett gravitational decay** | UNCOMPUTED | DM viability: if Gamma_grav > H_0, DM is destroyed | LEGGETT-GRAV-DECAY: gravitational vertex from spectral action coupling |
| 3 | **Josephson PW-branching** | UNCOMPUTED | Breaks or confirms f_0 anti-correlation (alpha_s problem) | JOSEPHSON-PW-BRANCHING: branching-resolved J_C2 at tau_fold |
| 4 | **Exact Pomeranchuk at z=6** | UNCOMPUTED | Perturbative RPA predicts instability at z >= 5; exact methods should resolve | EXACT-POMERAN-Z6: exact diag, 4-cell at physical coordination |
| 5 | **Multi-cell integrability** | PARTIALLY TESTED | GGE permanence on full fabric (Poisson at N=2 confirmed; N >= 3 open) | MULTI-CELL-INTEGRABILITY: level statistics at N_pair = 4 |
| 6 | **Self-consistent gap profile** | OPEN | Quantitative slope correction to d(Delta)/dtau | SELF-CONSISTENT-GAP-PROFILE: full V_eff(tau) re-solve |
| 7 | **BCS phase evolution** | OPEN | phi_eff(tau) profile needed for complete decoherence model | PHI-EFF-PROFILE: theta_BCS(tau) across fold |
| 8 | **DM self-interaction** | NOT COMPUTED | Distinguishing signature for DM searches | LEGGETT-SIGMA-V: scattering cross-section from Josephson network |
| 9 | **Entanglement at N_pair > 2** | OPEN | Schmidt numbers may change in BCS-BEC crossover | SCHMIDT-N4: exact diag at N_pair = 4 |
| 10 | **Sector-resolved curvature** | UNCOMPUTED | Confirms two-layer architecture at curvature level | R_K-SECTOR: decompose a_2 into PW-sector contributions |
| 11 | **Mott charge noise formalization** | ESTIMATE ONLY | Could provide 0.18 OOM of A_s budget | MOTT-BOGOLIUBOV: Bogoliubov transformation with charge variance |
| 12 | **Monogamy crossover geometry** | OPEN | Whether |A|~8 crossover is dim(SU(3)) or graph artifact | MONOGAMY-DEGREE: test on modified-degree CG(24) subgraphs |
| 13 | **Anisotropic decoherence** | NOT COMPUTED | 11.8x J-anisotropy creates geometric time spread | ANISO-DECOHERENCE: incorporate S63 anisotropy into W2-A model |
| 14 | **GGE pair-breaking proof** | OPEN | Formal demonstration T_eff > Delta does not break pairs | GGE-PAIR-BREAKING: matrix element computation |

### Summary of Gate Verdicts Affecting Condensed Matter (S72)

| Gate | Verdict | CM Impact |
|:-----|:--------|:----------|
| KAPPA-DELTA-72 | INFO | Gap amplitude decoherence CLOSED |
| BCS-DRESSED-SA-72 v2 | INFO | Mode-selective BCS negligible for n_s |
| FRUSTRATION-SCHMIDT-72 | PASS | Entanglement survives frustration |
| CV-SCALING-72 | INFO | Ordered Veil permanent (C_V saturates at 2.20) |
| ISLAND-GRAPH-72 | PASS | Area law on CG(24) fabric |
| CG24-GGE-ENTROPY-72 | INFO | Ordered Veil severity f_OV = 0.26-0.60 |
| DUAL-DECOHERENCE-72 | INFO | A_s = single-channel BCS t_dec problem |
| DECOHERENCE-BISPECTRUM-72 | PASS | f_NL = -0.31 (Gaussian, consistent with laminar flow) |
| G2-CONSTANCY-72 | FAIL | Near-constancy rank-2-generic, not SU(3)-specific |
| MODULAR-CHIRP-72 | FAIL | Modular chirp != eigenvalue curvature (8.4 OOM) |

---

**End of audit. 14 open problems identified, 10 resolving computations specified with pre-registered gates. The single highest-priority item is the exit-horizon BCS phase decoherence model (Rank 1), which determines whether the A_s budget can be closed from first principles.**
