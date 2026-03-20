# Session 29B Plan: Structural Gates + Particle Physics + Thermal Self-Consistency

**Date**: 2026-02-28
**Author**: Team-lead (synthesized from 3 research agents + fusion synthesis)
**Phase**: B (follows 29A; inherits KC-3 verdict, backreaction trajectory, entropy balance)
**Source**: Session 28 Grand Fusion Synthesis (Sections II, VII, VIII), Session 29A plan gap analysis
**Motivation**: Session 29A addresses the two unanimous top priorities (KC-3 closure + backreaction ODE). Session 29B addresses the **five fusion priorities that 29A deliberately omits**: the zero-cost 3-sector check, the last particle physics gate, the thermal self-consistency resolution, the off-Jensen structural stability, and the full inter-sector Josephson coupling.

---

## I. Relation to Session 29A

### What 29A Delivers (Inputs to 29B)

| 29A Output | Data File (expected) | 29B Use |
|:-----------|:--------------------|:--------|
| KC-3 verdict (PASS/FAIL) | `s29a_tmatrix_high_tau.npz` | Gates 29B entirely: if KC-3 FAILS, 29B reduces to Priority 4 (PMNS) + Priority 7 (Jensen transverse) only |
| tau(t) trajectory | `s29b_modulus_ode.npz` | Physical tau for PMNS evaluation; dtau/dt for Bogoliubov BCS |
| t_BCS, H(t_BCS) | `s29b_modulus_ode.npz` | Sets the transition epoch |
| Entropy balance verdict | `s29a_entropy_balance.npz` | Hard veto: if violated, 29B is moot except structural math |
| One-loop Gaussian correction | `s29b_gaussian_correction.npz` | Validates mean-field BCS; if sign reversal, 29B gap equation is moot |
| J_perp zeroth-order estimate | `s29a_j_perp.npz` | Informs whether full 1-loop Josephson (29B-5) is needed |
| Free energy crossing tau_cross | `s29b_free_energy_comparison.npz` | Input to CDL saddle check and 3-sector depth condition |

### Phase Boundary

29A ends when: **KC-3 verdict + entropy verdict + backreaction trajectory** are in hand.

29B opens after 29A delivers, except for two computations that are **29A-independent**:
- **29B-1 (3-sector F_BCS^{eff})**: zero-cost from existing s28b data, no 29A dependency
- **29B-4 (Jensen 5D transverse Hessian)**: structural geometry, no 29A dependency

These two should run first, potentially in parallel with late-stage 29A.

---

## II. Conditional Architecture

Session 29B scope depends on the 29A verdict:

| 29A Outcome | 29B Scope |
|:------------|:----------|
| **KC-3 PASS + entropy PASS** | Full 29B (all 6 computations) |
| **KC-3 PASS + entropy MARGINAL** | 29B-1, 29B-2, 29B-3 (thermal resolution), 29B-4, 29B-5 |
| **KC-3 FAIL** | 29B-1 (diagnostic), 29B-2 (PMNS, standalone value), 29B-4 (structural math) |
| **Entropy FAIL** | 29B-2 (PMNS), 29B-4 (Jensen Hessian) — both have standalone mathematical value |

Even in the worst case (KC-3 FAIL), Priorities 2 and 4 produce publishable results: PMNS mixing angles from tridiagonal Kosmann structure and the Jensen 5D transverse Hessian are permanent mathematical results (JGP/CMP level).

---

## III. Computation Plan

### 29B-1: 3-Sector F_BCS^{eff} [ZERO-COST, POTENTIAL CLOSURE]

**Fusion Priority**: 3 (elevated from no team synthesis's top 3 through fusion deliberation, XS-6)
**29A Coverage**: None (gap identified by overlap analysis)
**Dependency**: None — runs from existing s28b data

**What**: Restrict the BCS free energy to the 3 permanently supercritical sectors identified by the LZ retraction (Synthesis D, Section 1.5):
- **(3,0)**: multiplicity 100, first-order (L-9, c = 0.00552)
- **(0,3)**: multiplicity 100, first-order (L-9, c = 0.00723)
- **(0,0)**: multiplicity 16 (Spin(8) spinor), always supercritical at mu = lambda_min

Compute:
$$F_{BCS}^{3\text{-sector}}(\tau, \mu) = \sum_{r \in \{(3,0),(0,3),(0,0)\}} \text{mult}(r) \cdot F_{\text{cond}}^{(r)}(\tau, \mu)$$

**Why this matters**: The full-sector F_total from `s27_multisector_bcs.npz` includes re-entrant sectors ((2,0), (0,2), (1,1), (2,1), etc.) that dissolve at second-order boundaries. If stabilization depends on sectors that dissolve, the mechanism is structurally unsound. The 3-sector restriction tests whether the permanently supercritical sectors alone satisfy the B-3 depth condition.

**Critical finding from agent research**: At mu/lambda_min = 1.20 (the S-3 interior minimum), F_3sect = -17.22 vs F_total = -18.56 (**93% of total** — load-bearing sectors dominate). But at mu/lambda_min = 1.50 (deepest Hessian-confirmed minimum), F_3sect = -3.72 vs F_total = -43.55 (**only 8.5%** — re-entrant sectors dominate at deeper mu). The 3-sector minimum may be at a DIFFERENT (tau, mu) location than the full-sector minimum.

**Gate condition**: |F_BCS^{3-sector}(tau_0)| > (G_{tau,tau}/2) * (dtau/dt)^2 at the 3-sector minimum. With G_{tau,tau} = 5 and dtau/dt ~ 0.2 (hierarchy estimate from Synthesis D): threshold = 0.1. F_3sect = -17.22 at mu/lmin = 1.20 comfortably exceeds this. But the 3-sector Hessian must confirm this is a genuine minimum (both eigenvalues positive).

**Constraint Condition**: If F_BCS^{3-sector} < threshold at ALL (tau, mu) grid points, stabilization requires re-entrant sectors and the L-8 divergence problem returns. Framework structurally weakened (not closed, but weakened).

**Inputs**: `s27_multisector_bcs.npz` (F_cond[9 sectors, 9 tau, 12 mu]), `s28b_hessian.npz` (reference)

**Script**: New, ~50 lines. Read s27 data, index sectors (3,0) = idx 6, (0,3) = idx 7, (0,0) = idx 0 with multiplicities 100, 100, 16. Sum. Locate minimum. Compute Hessian via finite differences. Check B-3.

**Computational cost**: < 1 minute. Pure numpy post-processing.

**Agent**: phonon-exflation-sim

**Output**: `s29b_3sector_fbcs.npz`, `s29b_3sector_fbcs.py`

---

### 29B-2: Tridiagonal PMNS Extraction [LOW COST, LAST PARTICLE PHYSICS GATE]

**Fusion Priority**: 4 (last surviving particle physics test; UV-safe)
**29A Coverage**: None (entirely absent from 29A)
**Dependency**: Standalone (independent of KC-3 verdict); uses 29A tau(t) trajectory only to determine which tau value is physical

**What**: Extract the full 3x3 PMNS mixing matrix from the tridiagonal Kosmann kernel in the (0,0) singlet sector. The tridiagonal selection rules measured in Session 23a are:
- V(L1, L2) = 0.07-0.13 (nearest-neighbor coupling)
- V(L1, L3) = 0 EXACTLY (next-nearest = zero, selection rule)
- V(L2, L3) = 0.01-0.03 (nearest-neighbor coupling)

The effective mass matrix H_eff = diag(E_1, E_2, E_3) + V_pairing is tridiagonal. Its eigenvectors U define the PMNS matrix.

**Existing infrastructure**:
- `s24a_neutrino.py`: computes R and theta_12 from H_eff. Needs extension to full 3x3 PMNS.
- `s23a_kosmann_singlet.npz`: V_pairing matrices and eigenvalues at 9 tau values
- `s23a_gap_equation.npz`: BCS gap for mode-dependent extension
- `s24a_eigenvalue_ratios.npz`: confirmed zero phi crossings in singlet; 16 eigenvalues split 2+8+6

**Method**:
1. Construct H_eff = diag(lambda_1, lambda_2, lambda_3) + V_tridiagonal at tau = 0.15, 0.25, 0.35
2. Diagonalize: H_eff U = U diag(m_1, m_2, m_3)
3. Extract PMNS angles: sin^2(theta_13) = |U_{e3}|^2, tan^2(theta_12) = |U_{e2}|^2/|U_{e1}|^2, tan^2(theta_23) = |U_{mu3}|^2/|U_{tau3}|^2
4. (Optional) Extract delta_CP from the Jarlskog invariant J = Im(U_{e1} U_{mu2} U_{e2}* U_{mu1}*)

**Gate condition**: sin^2(theta_13) in [0.015, 0.030] (PDG: 0.0218 +/- 0.0007). theta_12 in [28, 38] degrees (PDG: 33.44 +/- 0.77).

**Constraint Condition**: If sin^2(theta_13) < 0.005 or > 0.10, the tridiagonal structure fails to reproduce the reactor angle. The particle physics prediction program is fully closed.

**R_BCS = R_bare theorem** (Team Synthesis C, Section III.1): Under uniform BCS gap, Delta^2 cancels in mass-squared ratios. R = 5.68 is **independent of BCS dressing**. PMNS angles are the ONLY remaining neutrino test.

**Extension — mode-resolved BdG**: If the 3x3 PMNS from uniform-gap H_eff fails, the escape route is a mode-dependent gap Delta_n from solving the full BdG equation within (0,0) with the tridiagonal V_{nm}. This tests whether non-uniform dressing shifts theta_13 toward the measured value.

**Inputs**: `s23a_kosmann_singlet.npz`, `s24a_eigenvalue_ratios.npz`

**Script**: Extend `s24a_neutrino.py` with full 3x3 eigenvector extraction. ~80 additional lines.

**Computational cost**: < 2 minutes. 3x3 diagonalization at 9 tau values.

**Agent**: phonon-exflation-sim (computation) or neutrino-detection-specialist (physics context)

**Output**: `s29b_pmns_extraction.npz`, `s29b_pmns_extraction.py`

---

### 29B-3: BCS Gap Equation with Bogoliubov Occupation [LOW COST, THERMAL GOLDILOCKS]

**Fusion Priority**: 5 (thermal Goldilocks resolution; UT-5)
**29A Coverage**: Partial (29a-3 entropy balance checks thermodynamic permissibility; 29b-3 Gaussian correction validates mean-field). Neither solves the gap equation self-consistently with Bogoliubov occupation.
**Dependency**: Requires 29A entropy balance verdict. If entropy FAILS, this computation is moot.

**What**: Replace the Fermi-Dirac distribution in the BCS gap equation with the non-equilibrium Bogoliubov occupation from KC-1:
$$\Delta_n = -\sum_m V_{nm} \frac{n_m + 1/2}{\sqrt{(\lambda_m - \mu)^2 + \Delta_m^2}}$$
where $n_m = |beta_m|^2 = B_m(\tau)$ from `s28a_bogoliubov_coefficients.npz`.

**Why this matters**: The standard BCS gap equation assumes thermal equilibrium (Fermi-Dirac). The phonon-exflation mechanism injects quasiparticles via parametric amplification (KC-1), which produces a non-thermal occupation n_k = B_k. The B_k are concentrated at the gap edge (B_k peaks where omega(k) is closest to lambda_min), mimicking a van Hove singularity but with different statistics. Whether this non-equilibrium distribution produces a BCS gap is the thermal Goldilocks question (fusion UT-5: margin 1.1x to 5.3x depending on T_eff estimate).

**Method**:
1. Load B_k(tau, mode) from `s28a_bogoliubov_coefficients.npz` (shape: 21 tau x 11,424 modes)
2. Map B_k to the eigenvalue grid used in `s27_multisector_bcs.py` (9 sectors x ~20 modes per sector)
3. Replace Fermi-Dirac in the gap equation self-consistency loop with n_k = B_k_interpolated
4. Solve for Delta(tau) at the 3 load-bearing sectors: (3,0), (0,3), (0,0)
5. Extract effective temperature T_eff by fitting n_k to a Bose-Einstein distribution
6. Compare T_eff to T_BCS from `s27_multisector_bcs.npz` (T_critical per sector)

**Gate condition**: Delta(n_k = B_k) / lambda_min > 0.01 at the 3 load-bearing sectors. If satisfied: thermal Goldilocks confirmed — the non-equilibrium distribution supports BCS condensation.

**Constraint Condition**: If Delta = 0 for all sectors at all tau with Bogoliubov occupation: the non-equilibrium distribution is too hot for condensation. The BCS mechanism requires a thermalization step not captured by KC-1/KC-2 alone.

**Inputs**: `s28a_bogoliubov_coefficients.npz`, `s23a_kosmann_singlet.npz` (V_nm for (0,0)), `s27_multisector_bcs.npz` (V_nm for other sectors)

**Script**: Modify `s26_multimode_bcs.py` or `s23a_bcs_gap_equation.py`. Swap Fermi-Dirac for B_k interpolant. ~60 lines of modification.

**Computational cost**: < 5 minutes. Self-consistency loop converges in ~20 iterations.

**Agent**: phonon-exflation-sim (computation) or landau-condensed-matter-theorist (BCS physics)

**Output**: `s29b_bogoliubov_bcs.npz`, `s29b_bogoliubov_bcs.py`

---

### 29B-4: Jensen 5D Transverse Hessian [MEDIUM COST, STRUCTURAL PREREQUISITE]

**Fusion Priority**: 7 (new from fusion UT-2; entirely absent from any prior session)
**29A Coverage**: None (29A addresses only the 1D Jensen curve)
**Dependency**: None — structural geometry, independent of KC-3 verdict

**What**: Compute the 4 eigenvalues of the V_total Hessian in the 4 off-Jensen directions of the 5D moduli space of left-invariant metrics on SU(3), evaluated at the BCS minimum tau_0 = 0.35.

**Why this matters**: The entire BCS analysis lives on the 1D Jensen curve (parameterized by tau). The full moduli space of left-invariant metrics on SU(3) is 5-dimensional (Baptista Paper 15). If any of the 4 off-Jensen eigenvalues is negative at the BCS minimum, the modulus escapes the Jensen curve into the 5D interior. The BCS minimum location and depth would change — possibly disappearing entirely. This is a structural prerequisite for the backreaction ODE (29A's 29b-2) to have physical meaning.

**The 5D parameterization** (from Baptista Paper 15, Section 3.7): Left-invariant metrics on SU(3) are parameterized by 5 independent scale factors on the orthogonal decomposition su(3) = u(1) + su(2) + C^2. The Jensen family fixes 3 of these via the volume-preserving constraint and the particular scaling lambda_1 = e^{2s}, lambda_2 = e^{-2s}, lambda_3 = e^s. The 4 transverse directions break either:
- (a) the volume-preserving constraint (breathing mode: all scales change uniformly)
- (b) the Jensen proportionality within the su(2) block (SU(2) anisotropy)
- (c) the Jensen proportionality within the C^2 block (C^2 anisotropy)
- (d) the Jensen ratio between u(1) and su(2) blocks (cross-block mixing)

**Symmetry argument** (fusion UT-2): At tau = 0 (round metric), the enhanced SU(3) x SU(3)/Z_3 symmetry makes the Jensen direction an eigenmode. All transverse perturbations are also eigenmodes by symmetry, with eigenvalues determined by group theory. At tau > 0, transverse couplings are generated perturbatively and grow with tau. The impedance ratio for off-Jensen modes is O(1/tau) — suppressed at small tau, O(1) at tau = 0.35.

**Method**:
1. From Paper 15 (eq 3.68 and surrounding), extract the 5D metric parameterization
2. Compute the Dirac spectrum at 8-16 off-Jensen metric points near the Jensen minimum (tau = 0.35 + small transverse perturbations delta_a in each of 4 directions)
3. Evaluate V_total = V_spec + F_BCS at each off-Jensen point
4. Construct the 4x4 transverse Hessian via finite differences
5. Diagonalize: if all 4 eigenvalues > 0, Jensen curve is a valley

**Gate condition**: All 4 eigenvalues > 0 at the BCS minimum. If satisfied: Jensen ansatz is structurally stable, backreaction ODE is physically meaningful.

**Constraint Condition**: If any eigenvalue < 0: the modulus is unstable off-Jensen. The BCS analysis must be repeated in the full 5D space (multi-session effort). The 1D backreaction from 29A is unreliable.

**Existing infrastructure**:
- `tier1_dirac_spectrum.py`: full Dirac spectrum computation for any left-invariant metric. Contains `jensen_metric(tau)` and `compute_structure_constants()`. Adaptable to general left-invariant metrics.
- `s25_baptista_results.py`: moduli space metric G_{tau,tau} = 5 on the Jensen curve
- `s28b_hessian.py`: 2D Hessian code, adaptable to higher dimensions

**What must be built new**:
1. General left-invariant metric parameterization (5 scale factors instead of Jensen's 1)
2. Off-Jensen Dirac spectrum driver (call `tier1_dirac_spectrum` with modified metric)
3. 4x4 transverse Hessian assembly from finite differences
4. Eigenvalue extraction and stability verdict

**Inputs**: `tier1_dirac_spectrum.py` (core Dirac code), `s27_multisector_bcs.npz` (F_BCS at Jensen points), Baptista Paper 15 equations

**Computational cost**: MEDIUM. Each off-Jensen Dirac spectrum takes ~8.7s at max_pq_sum = 6. Need 8-16 off-Jensen evaluations (2 per direction, finite difference). Total: ~70-140s for spectra + BCS evaluation. Dominated by spectrum computation.

**Agent**: phonon-exflation-sim (heavy computation) + baptista-spacetime-analyst (geometry)

**Output**: `s29b_jensen_transverse.npz`, `s29b_jensen_transverse.py`

---

### 29B-5: Full 1-Loop Inter-Sector Josephson Coupling J_ij [HIGH COST, FUNDAMENTAL]

**Fusion Priority**: 8 (partially addressed by 29A's 29a-4 at zeroth order)
**29A Coverage**: 29a-4 computes J_perp from off-diagonal blocks of V_{abcd} — zeroth-order check
**Dependency**: Requires 29A's J_perp estimate. If J_perp / Delta_BCS > 1 from 29a-4, this computation is confirmatory. If J_perp / Delta_BCS < 1, this computation is decisive for d_eff.

**What**: Compute the full 1-loop inter-sector Josephson coupling between the load-bearing conjugate pair (3,0) and (0,3):

$$J_{(3,0),(0,3)} = \sum_{n,m} \psi_n^{*(3,0)} V_{nm}^{\text{inter}} \psi_m^{(0,3)}$$

where V_{nm}^{inter} is the inter-sector component of the 4-point pairing interaction, computed from exact SU(3) Clebsch-Gordan coefficients for the (3,0) x (0,3) decomposition.

**Why this matters**: The d_eff fork (Synthesis C, Section VI) determines whether the BCS condensate has true long-range order (d_eff >= 2, J_perp/Delta > 1) or quasi-long-range order (d_eff = 1, Luttinger liquid). The XS-4 algebraic argument (J maps (3,0) to (0,3), forcing nonzero J_pair) guarantees J_pair != 0 but does not determine its magnitude. The geometric estimate J ~ O(tau^2) ~ 0.12 gives J/Delta ~ 0.17 (Landau) — weak Josephson regime.

**Key structural constraint**: D_K is exactly block-diagonal in Peter-Weyl (Session 22b theorem). The Kosmann operator K_a (which generates V_nm) involves commutators with D_K, so it too respects block-diagonality at the 2-point level. The inter-sector coupling comes exclusively from the 4-point vertex — the full T-matrix cross-sector channel, not the Kosmann matrix itself.

**Method**:
1. Compute SU(3) Clebsch-Gordan coefficients for (3,0) x (0,3) -> irreps. The CG coefficient for the (0,0) singlet channel gives the leading Josephson amplitude.
2. Use eigenvectors from `s23a_eigenvectors_extended.npz` for modes in (3,0) and (0,3) sectors
3. Evaluate the 4-point overlap integrals V_{abcd} with a in (3,0), c in (3,0), b in (0,3), d in (0,3)
4. Sum with free propagators G_n = 1/(E_n - mu + i*eta) to get the 1-loop coupling
5. Extract J_pair, compute J_perp = J_pair / Delta_BCS

**Gate condition**: J_perp > 1 at tau = 0.35 = d_eff >= 2 (true long-range order, mean-field valid). J_perp < 1 but > T/(N*Delta) ~ 0.006 = quasi-long-range order (operationally sufficient for modulus freezing but not BCS in strict sense).

**Constraint Condition**: J_perp < T/(N*Delta) = effectively decoupled sectors. Each sector must stabilize independently. d_eff = 1, Mermin-Wagner fluctuations may destroy the gap.

**What must be built new**:
1. SU(3) CG coefficient computation for (3,0) x (0,3) (either tabulated or computed via weight diagrams)
2. Cross-sector 4-point overlap integral evaluation (extend `s28c_phonon_tmatrix.py` cross-sector channel from bound to exact)
3. 1-loop Josephson coupling summation

**Inputs**: `s23a_eigenvectors_extended.npz`, `s22b_kosmann_matrix.npz`, `s27_multisector_bcs.npz`

**Computational cost**: HIGH. CG coefficient computation is O(dim^3) ~ O(10^3) per coefficient. 4-point overlaps require numerical integration over SU(3). Estimated: 30-60 minutes on 32-core.

**Agent**: phonon-exflation-sim (heavy computation)

**Output**: `s29b_josephson_coupling.npz`, `s29b_josephson_coupling.py`

---

### 29B-6: 3-Sector Gradient Balance (B-1 Check) [ZERO-COST, DOWNSTREAM OF 29B-1]

**Fusion Priority**: Embedded in XS-8 (Lambda_crit ~ 3 estimate)
**29A Coverage**: None (29A uses full-sector V_total)
**Dependency**: Requires 29B-1 (3-sector F_BCS^{eff})

**What**: Verify the gradient balance B-1 for the 3-sector potential:

$$S_b'(\tau_0) + F_{BCS}^{3\text{-sector}'}(\tau_0) = 0$$

The fusion's XS-8 computed Lambda_crit ~ 3.0 using full-sector F_BCS''. With 3-sector restriction, Lambda_crit may shift.

**Method**: Finite-difference derivative of F_BCS^{3-sector}(tau) from 29B-1. Compare to S_b'(tau) from `s24a_vspec.npz`. Find tau_0 where sum vanishes. Compute delta_tau = |tau_0 - tau_0^{full-sector}|.

**Gate condition**: tau_0 exists in [0.20, 0.50] with Lambda_crit = O(1). If satisfied: natural stabilization at compactification scale with only permanently supercritical sectors.

**Inputs**: Output of 29B-1, `s24a_vspec.npz`

**Computational cost**: < 1 minute. Pure post-processing.

**Agent**: phonon-exflation-sim

**Output**: Included in `s29b_3sector_fbcs.npz`

---

### 29B-7: Pfaffian of D_total = D_K tensor 1_F + gamma_5 tensor D_F [HIGH COST, HIGHEST-CEILING GATE]

**Fusion Priority**: Elevated to top-tier by Session 18 wrapup (marked HIGHEST PRIORITY since Session 18, deferred for 13 sessions)
**29A Coverage**: None (entirely absent from 29A and original 29B-1 through 29B-6)
**Dependency**: Requires 29B-4 (Jensen transverse stability) as a structural prerequisite — if Jensen ansatz is unstable, D_total Pfaffian on the 1D curve is physically meaningless. Independent of KC-3 verdict.

#### The Central Question

The existing D_K Pfaffian computation (Session 17c, `d2_pfaffian_computation.py`) returned **Z_2 = +1 (trivial) for all tau in [0, 2.5]**. But D_K is only the Kaluza-Klein part. The full Dirac operator on the NCG spectral triple (A, H, D) for M^4 x K is:

$$D_{\text{total}} = D_K \otimes \mathbf{1}_F + \gamma_5^{(K)} \otimes D_F$$

where $D_F$ is the **finite Dirac operator** encoding Yukawa couplings and Majorana mass terms, acting on $H_F = \mathbb{C}^{32}$. The tensor product structure means $D_{\text{total}}$ acts on $H_{\text{internal}} = L^2(S_K) \otimes H_F$, and when restricted to a Peter-Weyl sector $(p,q)$, it acts on $V_{(p,q)} \otimes \mathbb{C}^{16} \otimes \mathbb{C}^{32}$.

If $D_{\text{total}}$ has a Pfaffian sign change at some $\tau_c$, it produces a **topologically protected massless fermion** — a Level 4 novel prediction testable by KATRIN ($\sum m_\nu$), Planck+DESI, and Project 8. This would be the framework's single strongest observational prediction.

#### What D_F Requires: A Rigorous Assessment

**The fundamental theoretical obstacle** must be stated clearly. There are two approaches to constructing $D_F$, and they give different answers to the question "is this computation zero-parameter?"

**Approach A: Connes-Chamseddine-Marcolli (NCG from finite geometry)**

In the standard NCG approach (Connes Papers 09, 10, 12), $D_F$ is the finite Dirac operator on the spectral triple $(A_F, H_F, D_F, J_F, \gamma_F)$ where $A_F = \mathbb{C} \oplus \mathbb{H} \oplus M_3(\mathbb{C})$. The structure of $D_F$ is:

$$D_F = \begin{pmatrix} S & T^* \\ T & \bar{S} \end{pmatrix}$$

where $S$ contains Yukawa coupling matrices ($Y_\nu, Y_e, Y_u, Y_d$) and $T$ contains the Majorana mass matrix $M_R$ for right-handed neutrinos (Connes Paper 09, Section 3.1).

**Critical point**: The Yukawa matrices are FREE PARAMETERS in standard NCG. The axioms constrain the STRUCTURE of $D_F$ (which blocks are nonzero, which symmetries are obeyed) but NOT the numerical values. The classification theorem (Chamseddine-Connes 2007) determines $A_F$, $H_F$, and the gauge group uniquely, but $D_F$ is determined only up to the Yukawa and Majorana parameters. There are ~20 free real parameters in $D_F$ per generation (before CKM/PMNS phase choices).

**Consequence for this computation**: If $D_F$ is constructed via Approach A, the Pfaffian of $D_{\text{total}}$ depends on ~20 experimentally-determined Yukawa couplings. The test is NOT zero-parameter. It tests whether the D_K spectrum combined with KNOWN Yukawa couplings produces a topological transition — interesting but not a prediction.

**Approach B: Baptista (D_F derived from KK geometry)**

In Baptista's framework (Papers 17, 18), $D_F$ is NOT an independent input. It emerges from the dimensional reduction of the higher-dimensional Dirac operator $D_P$ on $P = M^4 \times K$. Specifically, the Kosmann-Lichnerowicz derivative $\mathcal{L}_X$ of spinors along non-Killing vector fields $X$ on $K$ generates the chiral couplings that play the role of Yukawa couplings (Paper 17, eq 1.3-1.4). The mass mixing matrix $\langle \psi_\alpha, D\!\!\!/\,_K \psi_\beta \rangle_{L^2}$ between representation-basis spinors and mass-eigenspinors IS the CKM/PMNS-type matrix (Paper 18, Section 6-7).

In this approach, $D_F$ is constructed from:
1. The eigenspinors $\psi_n(\tau)$ of $D_K(\tau)$ — ALREADY COMPUTED (eigenvectors available from `tier1_dirac_spectrum.py` with minor modification)
2. The Kosmann operators $K_a$ for the 4 non-Killing directions ($a \in \mathbb{C}^2$) — ALREADY COMPUTED (`s23a_kosmann_singlet.py`)
3. The overlap integrals $\langle \psi_\alpha | K_a | \psi_\beta \rangle$ between D_K eigenspinors from different sectors — requires Peter-Weyl cross-sector integration (NEW, but the mathematical ingredients exist)

**Critical distinction**: In Approach B, $D_F(\tau)$ is a FUNCTION of $\tau$ derived entirely from the geometry of $(SU(3), g_\tau)$. It depends on no external parameters. If the Pfaffian of $D_{\text{total}}(\tau) = D_K(\tau) \otimes \mathbf{1} + \gamma_5 \otimes D_F(\tau)$ changes sign, this is a ZERO-PARAMETER topological prediction.

**However**: Approach B has a fundamental unresolved issue. The order-one condition (NCG Axiom 5) FAILS at $O(1)$ for the SU(3) spectral triple (Session 28c, C-6: 6/7 axioms pass, axiom 5 fails with norm 4.000). This means the Baptista-derived $D_F$ does NOT satisfy the standard Connes order-one condition $[[D_F, a], J b J^{-1}] = 0$. The failure is structural (norm = 4.000, not a small perturbation). This has two interpretations:

- **(i) The order-one condition is too restrictive for KK**: Baptista's framework uses the full diffeomorphism group Diff(K), not just the finite algebra $A_F$. The order-one condition may be an artifact of the finite-space formulation that does not apply to geometric spectral triples derived from KK reduction. The spectral triple is "almost-commutative" only approximately.
- **(ii) The framework is incomplete**: The order-one failure signals that the SU(3) spectral triple is NOT a valid NCG spectral triple in the Connes sense. $D_F$ cannot be consistently defined, and the D_total Pfaffian is ill-posed.

**This computation will empirically distinguish these interpretations.** If D_total has a Pfaffian sign change at a geometrically natural $\tau_c$ (near a BCS transition point, near the phi_paasch crossing, etc.), interpretation (i) is strongly supported. If the Pfaffian is trivial or chaotic, interpretation (ii) gains ground.

#### Mathematical Specification

**What is computed**: $\text{sgn}\,\text{Pf}(J \cdot D_{\text{total}}(\tau))$ as a function of $\tau \in [0, 2.5]$.

Here $D_{\text{total}}(\tau)$ acts on the **truncated** internal Hilbert space:

$$\mathcal{H}_{\text{trunc}} = \bigoplus_{p+q \leq N_{\max}} V_{(p,q)} \otimes \mathbb{C}^{16}$$

For $N_{\max} = 2$ (sectors (0,0), (1,0), (0,1), (2,0), (0,2), (1,1)): $\dim(\mathcal{H}_{\text{trunc}}) = (1 + 3 + 3 + 6 + 6 + 8) \times 16 = 432$. The D_K part is block-diagonal (Session 22b theorem); the $D_F$ part couples different sectors via Kosmann-derived off-diagonal matrix elements.

The antisymmetric matrix $M = \Xi \cdot D_{\text{total}}$ is $864 \times 864$ (including $\Psi_+ \oplus \Psi_-$), and the Parlett-Reid Pfaffian algorithm runs in $O(n^3)$ — entirely feasible.

#### Method (Step by Step)

**Step 0: Eigenvector extraction** (prerequisite modification)

Modify `tier1_dirac_spectrum.py` function `dirac_operator_on_irrep()` to return eigenvectors alongside eigenvalues. Currently the function calls `np.linalg.eigvals()` (eigenvalues only). Change to `np.linalg.eigh()` (eigenvalues + eigenvectors). This is a ~5-line modification.

Specifically: $D_\pi(\tau)$ on sector $(p,q)$ is a $(\dim(p,q) \cdot 16) \times (\dim(p,q) \cdot 16)$ Hermitian matrix. Its eigenvectors $|\psi_n^{(p,q)}(\tau)\rangle$ are the internal eigenspinors. Store them for all sectors with $p+q \leq N_{\max}$.

**Step 1: Kosmann overlap integrals (WITHIN sectors)**

These are ALREADY computed for the (0,0) sector (`s23a_kosmann_singlet.npz`). Extend to all sectors $(p,q)$ with $p+q \leq N_{\max}$:

$$V_{nm}^{(p,q), a} = \langle \psi_n^{(p,q)} | K_a | \psi_m^{(p,q)} \rangle$$

for $a = 3,4,5,6$ (the 4 non-Killing $\mathbb{C}^2$ directions). The Kosmann operator $K_a$ is already implemented in `s23a_kosmann_singlet.py` with the corrected antisymmetric formula (Session 23a). Extending to other sectors requires computing $K_a$ on $V_{(p,q)} \otimes \mathbb{C}^{16}$ (tensor the identity on $V_{(p,q)}$ with the 16x16 Kosmann matrix).

**Step 2: Kosmann overlap integrals (CROSS-sector)** [THE NEW INGREDIENT]

This is the step that does not exist in the current codebase and is the core of $D_F$. The cross-sector Yukawa-type coupling is:

$$Y_{nm}^{(p,q)(p',q'), a} = \langle \psi_n^{(p,q)} | K_a^{\text{full}} | \psi_m^{(p',q')} \rangle$$

where $K_a^{\text{full}}$ acts on the full $\mathcal{H}_{\text{trunc}}$ and the inner product integrates over $SU(3)$ (i.e., uses the Peter-Weyl orthonormality).

**Key structural constraint from Session 22b**: $D_K$ is exactly block-diagonal in Peter-Weyl (Theorem 2). But $K_a$ is NOT block-diagonal — it is the spinorial correction operator from the Kosmann-Lichnerowicz derivative, and it involves the connection coefficients $\Gamma^c_{ab}$ which couple different representation sectors when the frame rotates under the non-Killing directions. Specifically:

$$K_a = -\frac{1}{8} \sum_{r,s} [A^a_{rs}]\, \gamma_r \gamma_s$$

where $A^a_{rs} = \Gamma^s_{ra} - \Gamma^r_{sa}$ is the antisymmetric part of the connection. This acts on the 16-dimensional spinor factor as a $16 \times 16$ matrix. But when $K_a$ is applied to an eigenspinor $|\psi_n^{(p,q)}\rangle = |v_n^{(p,q)}\rangle \otimes |\chi_n\rangle$, the result involves:

$$K_a |\psi_n^{(p,q)}\rangle = |v_n^{(p,q)}\rangle \otimes K_a^{(16)} |\chi_n\rangle$$

because $K_a^{(16)}$ acts only on the $\mathbb{C}^{16}$ spinor factor, NOT on the $V_{(p,q)}$ representation factor. Therefore:

$$Y_{nm}^{(p,q)(p',q'), a} = \langle v_n^{(p,q)} | v_m^{(p',q')} \rangle \cdot \langle \chi_n | K_a^{(16)} | \chi_m \rangle$$

The first factor $\langle v_n^{(p,q)} | v_m^{(p',q')} \rangle$ is zero by Peter-Weyl orthogonality when $(p,q) \neq (p',q')$.

**THIS IS THE CRITICAL STRUCTURAL FINDING**: Because $K_a$ acts only on the spinor factor and $D_K$ is block-diagonal in Peter-Weyl, the Kosmann operator preserves Peter-Weyl sectors. The cross-sector coupling is ZERO by representation orthogonality.

This means $D_F$ constructed from Kosmann overlaps is ALSO block-diagonal in Peter-Weyl. And therefore:

$$D_{\text{total}} = D_K \otimes \mathbf{1}_F + \gamma_5 \otimes D_F$$

is block-diagonal sector by sector. Its determinant factorizes as the product of per-sector determinants. Its Pfaffian sign is the product of per-sector Pfaffian signs. And per the existing D_K Pfaffian computation (Session 17c), each per-sector D_K has no zero eigenvalue. Adding a block-diagonal $D_F$ (bounded, tau-continuous) to D_K cannot close the spectral gap unless $D_F$ eigenvalues are comparable to D_K eigenvalues.

**Wait** — this argument requires careful examination. The $D_F$ in the Connes formulation is NOT constructed from Kosmann overlaps alone. Let me re-examine the tensor product structure.

#### Re-examination of the Tensor Product Structure

The full NCG Dirac operator on the product geometry $M^4 \times F$ is (Connes Paper 10, Section 1.2):

$$D = D_M \otimes \mathbf{1}_F + \gamma_5^{(M)} \otimes D_F$$

Here $D_M$ is the 4D Dirac operator and $D_F$ acts on $H_F = \mathbb{C}^{32}$. In the phonon-exflation framework, the role of $D_M$ is played by $D_K$ (the internal manifold replaces the "finite geometry" of standard NCG). The question is: what replaces $D_F$?

In standard NCG, $D_F$ is a 32x32 matrix with Yukawa entries. In the Baptista KK framework, there is no separate "finite geometry" — the entire internal physics comes from $D_K$ on $K = SU(3)$. The 32 = 16 + 16 structure of $H_F$ comes from $\Psi_+ \oplus \Psi_-$ (the two chiralities of the Spin(8) spinor on the 8-dimensional SU(3)).

The correct identification is:

$$D_{\text{total}} = D_K \text{ (acting on } L^2(S_K) = L^2(S_K^+) \oplus L^2(S_K^-) \text{)}$$

where $D_K$ already acts on the FULL 32-dimensional spinor per sector (the $\Psi_+ \oplus \Psi_-$ structure is already built into the existing `d2_pfaffian_computation.py` via the $D_{32} = \text{diag}(\Omega, G_5 \cdot \overline{\Omega} \cdot G_5)$ construction).

So $D_{\text{total}}$ in the existing Pfaffian computation IS ALREADY the full internal Dirac operator — there is no separate $D_F$ to add. The Session 17c computation already computed $\text{Pf}(\Xi \cdot D_{32}(\tau))$ on the full $\mathbb{C}^{32}$ per sector.

**But this analysis is incomplete.** The Connes $D_F$ encodes couplings that are NOT captured by $D_K$ alone. In the Baptista framework, these are the couplings generated by the Kosmann-Lichnerowicz derivative when gauge fields are turned on (Paper 17, eq 1.3). With the gauge field background set to zero (the vacuum), these terms vanish. But the FLUCTUATIONS of the gauge fields (inner automorphisms of $A$) generate the Higgs field, and the Higgs field's vacuum expectation value produces Yukawa couplings.

The resolution is: $D_F$ in the phonon-exflation framework is the **Higgs-sector contribution** to the Dirac operator, arising from the second fundamental form $S$ of the fibration (Baptista Paper 15, eq for $|d_A g_K|^2$). When the internal metric $g_K$ is deformed from the bi-invariant metric, the non-zero $d_A g_K$ generates mass terms for gauge bosons AND Yukawa couplings for fermions. These are encoded in the Kosmann commutator $[D_K, \mathcal{L}_X]$ for non-Killing $X$ (Paper 17, eq 1.4).

**Concrete construction**: $D_F(\tau)$ is the $32 \times 32$ matrix (per sector) given by:

$$[D_F]_{\alpha\beta} = \sum_{a \in \mathbb{C}^2} \langle \psi_\alpha | [D_K, \mathcal{L}_{e_a}] | \psi_\beta \rangle$$

where $\{e_a\}_{a=3,4,5,6}$ are the 4 non-Killing frame vectors. This commutator was computed in Paper 17 (eq 1.4):

$$[D_K, \mathcal{L}_X]\psi = \frac{1}{2}\sum_{i,j} (\mathcal{L}_X g_K)(v_i, v_j)\, v_i \cdot v_j \cdot \psi + \frac{1}{4}\sum_{i,j}[\nabla_{v_i}(\mathcal{L}_X g_K)](v_i, v_j) - [\nabla_{v_j}(\mathcal{L}_X g_K)](v_i, v_i)]\, v_j \cdot \psi$$

This is nonzero only for non-Killing $X$ (vanishes when $\mathcal{L}_X g_K = 0$). For the Jensen deformation at $\tau > 0$, the 4 $\mathbb{C}^2$ directions have $\mathcal{L}_{e_a} g_\tau \neq 0$ (they are non-Killing). The commutator matrix elements can be computed from existing infrastructure: $g_\tau$, the frame, the connection coefficients, and the eigenvectors of $D_K$.

#### Revised Method (Step by Step)

**Step 0: Eigenvector extraction**
Modify `tier1_dirac_spectrum.py` to return eigenvectors. ~5-line change.

**Step 1: Compute $\mathcal{L}_{e_a} g_\tau$ for $a = 3,4,5,6$**
The Lie derivative of the Jensen metric along the non-Killing frame vectors. This is a $8 \times 8$ symmetric tensor per direction, computed from $(\mathcal{L}_{e_a} g)_{bc} = g_{bd} f^d_{ac} + g_{cd} f^d_{ab}$ in the left-invariant frame (where $f^d_{ac}$ are the frame structure constants). All ingredients exist in `tier1_dirac_spectrum.py`.

**Step 2: Compute the $[D_K, \mathcal{L}_{e_a}]$ matrix in the eigenbasis**
Using Paper 17 eq 1.4, compute the commutator as a matrix on the spinor space. For each sector $(p,q)$, project into the $D_K$-eigenbasis to get:

$$[D_K, \mathcal{L}_{e_a}]_{\alpha\beta} = (m_\alpha + m_\beta) \langle \psi_\alpha | \mathcal{L}_{e_a} | \psi_\beta \rangle_{\text{chiral}}$$

(from Paper 17 eq 1.6, the mass sum formula). The matrix elements $\langle \psi_\alpha | \mathcal{L}_{e_a} | \psi_\beta \rangle$ involve the Kosmann operator already computed.

**Step 3: Assemble $D_F(\tau)$ on the truncated Hilbert space**
Sum the contributions from all 4 non-Killing directions. $D_F(\tau)$ is Hermitian on $\mathcal{H}_{\text{trunc}}$ (self-adjoint Dirac operator requirement). Check: $D_F$ must anticommute with $\gamma_F$ (chirality condition, NCG Axiom 1 for the product geometry).

**Step 4: Construct $D_{\text{total}}(\tau)$ and the antisymmetric matrix $M(\tau)$**
$$D_{\text{total}} = D_K \otimes \mathbf{1}_{32} + \gamma_5^{(K)} \otimes D_F$$

in the full $\mathcal{H}_{\text{trunc}} \otimes \mathbb{C}^{32}$ space, or equivalently on the $\Psi_+ \oplus \Psi_-$ extended space. Construct $M = \Xi \cdot D_{\text{total}}$ and verify antisymmetry $M + M^T = 0$.

**Step 5: Pfaffian scan over $\tau \in [0, 2.5]$**
Use the Parlett-Reid algorithm (already implemented in `d2_pfaffian_computation.py`) to compute $\text{Pf}(M(\tau))$ at 50-100 $\tau$ values. Track the sign. Any sign change indicates a topological phase transition.

**Step 6: If sign change found, bisect to locate $\tau_c$**
Refine to $|\tau_c - \tau_{\text{grid}}| < 10^{-6}$ using bisection. Determine which eigenvalue of $D_{\text{total}}$ crosses zero. Identify the sector and mode.

#### Gate Conditions

**PASS (P-29f)**: $\text{Pf}(J \cdot D_{\text{total}}(\tau))$ changes sign at some $\tau_c \in [0, 2.5]$.
- Consequence: Topologically protected massless fermion at $\tau_c$. If $\tau_c$ coincides with the BCS transition point (from 29A), the vacuum is topologically selected. Level 4 prediction: a massless (or near-massless) fermion species at the stabilized $\tau_0$. Testable by KATRIN, Planck+DESI ($\sum m_\nu$), Project 8.
- Probability impact: Framework probability jumps to 20-40% (a zero-parameter, binary, topological prediction with no adjustable parameters).

**FAIL (B-29f)**: $\text{Pf}(J \cdot D_{\text{total}}(\tau)) = \text{const}$ for all $\tau$ (no sign change).
- Consequence: Topological route is fully exhausted. No protected zero modes from either $D_K$ or $D_{\text{total}}$. Modulus stabilization is entirely dynamical (BCS), with no topological selection. The framework has no Level 4 predictions.
- Probability impact: No change from current (topological route was already in "open" status, not counted toward probability).

**DIAGNOSTIC**: Even if no sign change occurs, the computation produces:
- The spectral gap of $D_{\text{total}}(\tau)$ as a function of $\tau$ (how close does it come to closing?)
- The tau-dependence of $D_F(\tau)$ (does it have a natural scale compared to $D_K$?)
- The order-one condition violation as a function of $\tau$ (does it improve at the BCS point?)
- Cross-validation of C-6 (6/7 NCG axioms) with the explicit $D_F$ construction

#### Constraint Conditions

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-29f | Pfaffian constant for all tau (no sign change) | Topological route fully exhausted. No Level 4 prediction. |
| B-29g | $D_F$ construction fails (Lie derivative formula ill-defined or numerically unstable) | Baptista approach to Yukawa couplings from KK geometry does not yield a consistent $D_F$. Must fall back to Approach A (experimental Yukawa inputs). |
| P-29f | Pfaffian sign change at $\tau_c$ | Level 4 topological prediction. Zero-parameter binary test. |
| P-29g | $\tau_c$ coincides with BCS transition $\tau_{\text{cross}}$ (within 10%) | Topological and dynamical stabilization AGREE. Dramatically strengthens framework. |

#### What Must Be Built New

1. **Eigenvector return from `dirac_operator_on_irrep()`** (~5 lines, modify existing function)
2. **Lie derivative $\mathcal{L}_{e_a} g_\tau$ computation** (~30 lines, new function using existing frame/structure constants)
3. **$[D_K, \mathcal{L}_{e_a}]$ commutator matrix assembly** (~80 lines, implements Paper 17 eq 1.4)
4. **$D_F(\tau)$ assembly on truncated Hilbert space** (~40 lines, sum over non-Killing directions)
5. **$D_{\text{total}}$ tensor product construction** (~30 lines, tensor product with chirality)
6. **Extended $\Xi_{32}$ to $\Xi_{\text{trunc}}$** (~20 lines, block-diagonal extension of existing $\Xi$)
7. **Pfaffian scan driver** (~50 lines, adapt from `d2_pfaffian_computation.py`)

**Total new code**: ~250-300 lines. The core algorithms (Pfaffian, Dirac spectrum, Kosmann) are all reused from existing infrastructure.

#### Inputs

- `tier1_dirac_spectrum.py`: D_K eigenvalues + eigenvectors (modified), frame, connection, structure constants
- `branching_computation_32dim.py`: Xi, G5, gamma_F, particle identification
- `d2_pfaffian_computation.py`: Parlett-Reid Pfaffian algorithm, (0,0) sector framework
- `s23a_kosmann_singlet.py`: Kosmann operator $K_a$ construction (corrected antisymmetric formula)
- Baptista Paper 17 eq 1.4: $[D_K, \mathcal{L}_X]$ formula
- Baptista Paper 18 Appendix E: SU(3) example with $(SU(3) \times SU(2) \times U(1))/\mathbb{Z}_6$ symmetries

#### Computational Cost

**MEDIUM-HIGH**. The dominant cost is the eigenvector computation at each $\tau$ value:
- Per sector $(p,q)$: diagonalization of $(\dim(p,q) \cdot 16)^2$ matrix. For (1,1): $128 \times 128$. For (2,0): $96 \times 96$.
- At $N_{\max} = 2$: 6 sectors, ~5 seconds per $\tau$ value for full eigenvector extraction.
- 50 $\tau$ values: ~250 seconds for spectra.
- Pfaffian computation: $864 \times 864$ matrix, $O(n^3) \approx 6 \times 10^8$ operations per $\tau$ value. ~1 second per evaluation.
- Total: ~6-8 minutes for complete scan at $N_{\max} = 2$.
- Extension to $N_{\max} = 3$: $\dim(\mathcal{H}_{\text{trunc}}) = (1+3+3+6+6+8+10+10+15+15+27) \times 16 = 1664$. Pfaffian on $3328 \times 3328$: ~30 seconds per $\tau$. Total ~25-30 minutes.

**Recommended**: Run at $N_{\max} = 2$ first (6 minutes). If sign change found, confirm at $N_{\max} = 3$. If no sign change at $N_{\max} = 2$, extend to $N_{\max} = 3$ to check truncation stability.

#### Agent

- **phonon-exflation-sim** (primary computation: eigenvectors, tensor products, Pfaffian)
- **einstein-theorist** (theoretical oversight: $D_F$ construction verification, order-one condition check, physical interpretation)
- **baptista-spacetime-analyst** (geometry: Lie derivative formula, cross-validation with Papers 17-18)

#### Output

`s29b_dtotal_pfaffian.npz`, `s29b_dtotal_pfaffian.py`

Contents of .npz:
- `tau_values`: scan grid
- `pf_values`: Pfaffian at each tau (complex, should be real to machine epsilon)
- `pf_signs`: sign(Re(Pf)) at each tau
- `min_gap_dtotal`: minimum |eigenvalue| of D_total at each tau
- `D_F_norm`: Frobenius norm of D_F at each tau (diagnostic)
- `order_one_norm`: order-one condition violation at each tau (diagnostic)
- `sign_change_tau`: tau value(s) where sign changes, if any (empty array if none)

#### Why This Has Been Deferred for 13 Sessions

The honest answer: the theoretical prerequisite — determining whether $D_F$ can be derived from KK geometry rather than inserted by hand — was unresolved. The Kosmann machinery needed for $[D_K, \mathcal{L}_X]$ was only developed in Session 23a (Kosmann operator computation). The eigenvector infrastructure was only built in Session 12 (Tier 1 Dirac spectrum) but eigenvectors were discarded. The order-one condition status (C-6, Axiom 5 fails) was only determined in Session 28c.

All prerequisites now exist. The computation is feasible. The theoretical framework (Baptista Papers 17-18) provides the explicit formula for $D_F$ from geometry. The only remaining question is whether the formula produces a consistent, tau-continuous $D_F$ that generates a Pfaffian sign change.

---

## IV. Priority Map and Dependencies

```
                    ┌─────────────────────────────────┐
                    │  29A OUTPUTS (inherited)         │
                    │  KC-3 verdict, tau(t), t_BCS,    │
                    │  entropy verdict, J_perp^{(0)}   │
                    └──────────┬──────────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
          ▼                    ▼                    ▼
  ┌──────────────┐   ┌──────────────┐    ┌──────────────┐
  │ 29B-1        │   │ 29B-2        │    │ 29B-4        │
  │ 3-Sector     │   │ PMNS         │    │ Jensen 5D    │
  │ F_BCS^{eff}  │   │ Extraction   │    │ Transverse   │
  │ [ZERO-COST]  │   │ [LOW]        │    │ Hessian      │
  │ NO 29A DEP   │   │ STANDALONE   │    │ [MEDIUM]     │
  └──────┬───────┘   └──────────────┘    │ NO 29A DEP   │
         │                               └──────┬───────┘
         ▼                                      │
  ┌──────────────┐                              │
  │ 29B-6        │                              │
  │ Gradient     │                              │
  │ Balance B-1  │                              │
  │ [ZERO-COST]  │                              │
  └──────────────┘                              │
                                                ▼
          ┌── Requires 29A entropy verdict ──┐  ┌──────────────┐
          │                                   │  │ 29B-7        │
          ▼                                   ▼  │ D_total      │
  ┌──────────────┐                   ┌──────────────┐ Pfaffian  │
  │ 29B-3        │                   │ 29B-5        │ [MED-HIGH]│
  │ Bogoliubov   │                   │ Josephson    │ needs 29B-4│
  │ BCS Gap      │                   │ 1-Loop       │ PASS      │
  │ [LOW]        │                   │ [HIGH]       └──────────────┘
  │ needs 29A    │                   │ needs 29A    │
  │ entropy PASS │                   │ J_perp^{(0)} │
  └──────────────┘                   └──────────────┘
```

**Critical path**: 29B-1 -> 29B-6 (zero-cost chain, can run before 29A finishes)

**Independent tracks**: 29B-2 (PMNS) can run at any time. 29B-4 (Jensen 5D) can run at any time and gates 29B-7.

**29A-gated**: 29B-3 (Bogoliubov BCS) and 29B-5 (Josephson 1-loop) wait for 29A results.

**29B-4-gated**: 29B-7 (D_total Pfaffian) requires 29B-4 PASS (Jensen transverse stability). If Jensen ansatz is unstable, the 1D Pfaffian scan on the Jensen curve is physically meaningless. Independent of KC-3 verdict — the Pfaffian is a topological quantity that does not depend on the BCS mechanism.

---

## V. Constraint Conditions and Gate Structure

### Hard Closes (any one terminates the corresponding computation)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-29a | F_BCS^{3-sector} < 0.1 at ALL (tau, mu) (29B-1) | Load-bearing sectors alone cannot stabilize. Re-entrant sectors required. L-8 divergence problem returns. |
| B-29b | sin^2(theta_13) < 0.005 or > 0.10 (29B-2) | Tridiagonal PMNS fails. Particle physics prediction program fully closed. |
| B-29c | Delta(n_k = B_k) = 0 for all sectors (29B-3) | Non-equilibrium distribution too hot for BCS. Thermalization mechanism needed. |
| B-29d | Any off-Jensen eigenvalue < 0 at tau = 0.35 (29B-4) | Jensen ansatz unstable. Full 5D moduli space analysis required (multi-session). |
| B-29e | J_perp < T/(N*Delta) (29B-5) | Sectors effectively decoupled. d_eff = 1. Mermin-Wagner destroys gap. |
| B-29f | Pf(J * D_total) constant for all tau (29B-7) | Topological route fully exhausted. No Level 4 prediction from topology. |
| B-29g | D_F construction fails: Lie derivative formula numerically unstable or ill-defined (29B-7) | Baptista KK-geometric Yukawa approach does not yield consistent D_F. Approach A (experimental Yukawa) required. |

### Positive Signals (increase probability)

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-29a | F_3sect > 0.1 with genuine minimum (29B-1) | 3-sector stabilization confirmed. L-8 evaporated for stabilization. |
| P-29b | sin^2(theta_13) in [0.015, 0.030] (29B-2) | First BCS-era particle physics PASS. Framework has a surviving prediction. |
| P-29c | Delta(B_k)/lambda_min > 0.01 (29B-3) | Thermal Goldilocks resolved. BCS robust to non-equilibrium injection. |
| P-29d | All 4 off-Jensen eigenvalues > 0 (29B-4) | Jensen curve is a valley. Full 5D stability confirmed. Backreaction result reliable. |
| P-29e | J_perp / Delta > 1 (29B-5) | True long-range order. d_eff >= 2. Mean-field BCS fully justified. |
| P-29f | Pf(J * D_total) sign change at tau_c (29B-7) | Level 4 topological prediction. Zero-parameter binary test. Massless fermion at tau_c. |
| P-29g | tau_c coincides with tau_cross (BCS transition) within 10% (29B-7) | Topological and dynamical stabilization agree. Framework probability jumps to 20-40%. |

---

## VI. Agent Assignments

| Agent | Role | Computations |
|:------|:-----|:-------------|
| **phonon-exflation-sim** | Primary computation | 29B-1, 29B-2, 29B-3, 29B-4 (spectrum), 29B-5 (overlaps), 29B-6, 29B-7 (eigenvectors + Pfaffian) |
| **baptista-spacetime-analyst** | Geometry for Jensen 5D + D_F construction | 29B-4 (metric parameterization from Paper 15), 29B-7 (Lie derivative formula from Paper 17 eq 1.4, cross-validation) |
| **einstein-theorist** | D_total theoretical oversight | 29B-7 (D_F construction verification, order-one condition check, physical interpretation of Pfaffian result) |
| **landau-condensed-matter-theorist** | BCS physics for Bogoliubov gap + Josephson | 29B-3 (gap equation), 29B-5 (d_eff assessment) |
| **neutrino-detection-specialist** | PMNS physics context | 29B-2 (mixing angle interpretation) |
| **coordinator** | Context + routing | Full session |

**Recommended team size**: 3-4 active agents + coordinator. Minimum viable: phonon-sim + coordinator.

**For 29B-7 specifically**: phonon-sim (computation) + einstein (theory) + baptista (geometry). The baptista agent is essential for validating the $[D_K, \mathcal{L}_X]$ formula implementation against Papers 17-18.

**Blast-first spawn workflow applies** (CLAUDE.md mandatory).

---

## VII. Estimated Timeline

| Block | Computations | Runtime | Dependencies |
|:------|:------------|:--------|:-------------|
| Block A (pre-29A) | 29B-1, 29B-6 | < 5 min | None |
| Block B (parallel with 29A) | 29B-2, 29B-4 | < 30 min | None |
| Block C (post-29A) | 29B-3, 29B-5 | < 90 min | 29A verdict |
| Block D (post-29B-4) | 29B-7 | < 30 min | 29B-4 PASS |

Total computation time: ~2.5 hours. Dominated by 29B-5 (Josephson CG coefficients + 4-point overlaps) and 29B-7 (eigenvector extraction + D_F assembly + Pfaffian scan). 29B-7 can run in parallel with Block C if 29B-4 passes early.

---

## VIII. Output Files

| Computation | Output .npz | Output .py | Gate Verdict |
|:------------|:-----------|:-----------|:-------------|
| 29B-1 | `s29b_3sector_fbcs.npz` | `s29b_3sector_fbcs.py` | B-3 depth, 3-sector |
| 29B-2 | `s29b_pmns_extraction.npz` | `s29b_pmns_extraction.py` | sin^2(theta_13) gate |
| 29B-3 | `s29b_bogoliubov_bcs.npz` | `s29b_bogoliubov_bcs.py` | Thermal Goldilocks |
| 29B-4 | `s29b_jensen_transverse.npz` | `s29b_jensen_transverse.py` | Off-Jensen stability |
| 29B-5 | `s29b_josephson_coupling.npz` | `s29b_josephson_coupling.py` | J_perp / Delta gate |
| 29B-6 | (included in 29B-1 output) | (included in 29B-1 script) | Gradient balance B-1 |
| 29B-7 | `s29b_dtotal_pfaffian.npz` | `s29b_dtotal_pfaffian.py` | Pfaffian sign change gate |

Gate verdicts file: `tier0-computation/s29b_gate_verdicts.txt`

---

## IX. Success Criteria

Session 29B is successful if it produces:

1. **A definitive 3-sector depth verdict** (F_BCS^{3-sector} sufficient or insufficient for B-3)
2. **PMNS mixing angles** (sin^2(theta_13), theta_12, theta_23) at tau = 0.15 and tau = 0.35
3. **A thermal Goldilocks verdict** (Bogoliubov-occupation BCS gap nonzero or zero)
4. **A Jensen transverse stability verdict** (all 4 eigenvalues positive or not)
5. **An inter-sector Josephson magnitude** (J_pair, J_perp = J/Delta, d_eff determination)
6. **A D_total Pfaffian verdict** (sign change exists or not; if exists, location tau_c and comparison to tau_cross)

Combined with 29A outputs, these complete the Session 28 Fusion Synthesis's full 8-priority list PLUS the long-deferred topological test from Session 18. The framework's state after Session 29 will be either:
- **KC-3 PASS + all 29B gates PASS + Pfaffian sign change**: probability rises to 25-40%, Level 4 topological prediction in hand, massless fermion prediction ready for confrontation with KATRIN/Planck+DESI
- **KC-3 PASS + all 29B gates PASS + Pfaffian trivial**: probability rises to 15-30%, no topological selection
- **KC-3 PASS + some 29B gates FAIL**: probability remains 7-10%, structural weaknesses identified
- **KC-3 FAIL**: probability drops to 3% (structural floor), but PMNS, Jensen 5D, and D_total Pfaffian results survive as standalone mathematics (JGP/CMP level)

---

*Plan synthesized from: Session 28 Grand Fusion Synthesis (Baptista, writer; Tesla, Landau, Dirac deliberation), Session 29A plan (Hawking, author), three research agent analyses (execution context, overlap analysis, infrastructure inventory), Session 29Ab Einstein contributions (backreaction, Friedmann, Bianchi). 29B-7 (D_total Pfaffian) designed by Einstein-Theorist, grounded in Baptista Papers 17-18 and Connes Papers 09-10-12, addressing the highest-priority computation deferred since Session 18. All equations cited to specific papers and sessions. Constraint Conditions pre-registered. Agents assigned. Dependencies mapped.*
