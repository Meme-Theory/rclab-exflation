# Session 29Bb: Structural Stability + Thermal Goldilocks + Josephson Coupling

**Date**: 2026-02-28
**Author**: Team-lead (decomposed from 29B plan)
**Depends on**: Session 28 (all sub-sessions). 29B-4 is standalone. 29B-3 and 29B-5 are gated by 29A results.
**Prerequisite**: For 29B-3 — 29A entropy balance must PASS (K-29b did not fire). For 29B-5 — 29A J_perp estimate from 29a-4 required. 29B-4 has no prerequisites and should start immediately.
**Input data**:
- `tier0-computation/tier1_dirac_spectrum.py` (core Dirac code, frame, connection, structure constants)
- `tier0-computation/s27_multisector_bcs.npz` (F_BCS at Jensen points, V_nm for all sectors)
- `tier0-computation/s28a_bogoliubov_coefficients.npz` (B_k(tau) for all sectors, 21 tau x 11,424 modes)
- `tier0-computation/s23a_kosmann_singlet.npz` (V_nm for (0,0) sector)
- `tier0-computation/s23a_eigenvectors_extended.npz` (D_K eigenvectors for all sectors)
- `tier0-computation/s28b_hessian.npz` (2D Hessian code, adaptable)
- `tier0-computation/s25_baptista_results.py` (G_{tau,tau} = 5 on Jensen curve)
- `tier0-computation/s29a_gate_verdicts.txt` (KC-3 and entropy verdicts — FROM 29A)
- `tier0-computation/s29a_inter_sector_coupling.npz` (J_perp zeroth-order — FROM 29A, for 29B-5)

## Motivation

This sub-session tackles the three medium-to-high-cost computations from the 29B plan:

1. **29B-4** (Jensen 5D Transverse Hessian): Is the BCS minimum on the Jensen curve structurally stable against off-Jensen perturbations? This gates the entire backreaction analysis AND the crown-jewel D_total Pfaffian computation (29Bc). **No 29A dependency — start immediately.**

2. **29B-3** (Bogoliubov BCS Gap): Does the non-equilibrium occupation from KC-1 parametric amplification support BCS condensation? The thermal Goldilocks resolution. **Gated by 29A entropy PASS.**

3. **29B-5** (Full 1-Loop Josephson): What is the inter-sector coupling magnitude between the load-bearing conjugate pair (3,0)↔(0,3)? Determines d_eff and whether mean-field BCS is justified. **Gated by 29A J_perp estimate.**

---

# 0. OPERATIONAL RULES

## COMPUTATION DISCIPLINE

Every result classified against its pre-registered gate BEFORE any interpretation. Report the number first. Classify second. Interpret third.

**Python environment**: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
**Output directory**: `tier0-computation/`
**Script prefix**: `s29b_`

## 29A GATE CHECK (for 29B-3 and 29B-5 only)

Before starting 29B-3 or 29B-5, read `tier0-computation/s29a_gate_verdicts.txt` and verify:
1. For 29B-3: Entropy balance = PASS (K-29b did not fire)
2. For 29B-5: J_perp estimate available from `s29a_inter_sector_coupling.npz`

If entropy FAILS, skip 29B-3 entirely. If J_perp data is missing, defer 29B-5 until 29A completes.

**29B-4 has NO gate check and should start immediately.**

## COMPLETION SIGNAL

Session ends ONLY when user approves shutdown explicitly. Idle agents are not finished agents.

---

# I. REQUIRED READING

## ALL agents (MANDATORY):

1. **Session 28 fusion synthesis**: `sessions/session-28/session-28-fusion-synthesis.md` — Section IV (XS-4: J operator maps (3,0)→(0,3)), Section V (modulus-space narrative), Section VIII (priorities 5, 7, 8).
2. **Session 29B plan**: `sessions/session-plan/session-29B-plan.md` — Section III (29B-3, 29B-4, 29B-5 computation specs), Section V (gate structure).
3. **Session 29Ba results**: `sessions/session-29/session-29Ba-synthesis.md` — 3-sector depth verdict and PMNS results (if available).
4. **MathVariables**: `sessions/framework/MathVariables.md` — Section 4 (BCS variables), Section 2 (Dirac operator).
5. **Your agent memory**: `.claude/agent-memory/{your-agent}/`

## Agent-specific required reading:

| Agent | Additional Reading |
|:------|:-------------------|
| phonon-exflation-sim | `tier0-computation/tier1_dirac_spectrum.py` (Dirac spectrum infrastructure), `tier0-computation/s28b_hessian.py` (Hessian code to extend), `tier0-computation/s27_multisector_bcs.py` (BCS solver) |
| baptista-spacetime-analyst | `researchers/Baptista/` — Paper 15 Section 3.7 (5D moduli space parameterization, eq 3.68), Paper 17 (Kosmann-Lichnerowicz derivative) |
| landau-condensed-matter-theorist | `researchers/Landau/index.md` — BCS gap equation, Bogoliubov occupation, Josephson coupling physics |
| coordinator | This prompt Section IV (gate conditions). Memorize ALL thresholds before first computation completes |

---

# II. COMPUTATIONS

## 29B-4: Jensen 5D Transverse Hessian [MEDIUM COST, STRUCTURAL PREREQUISITE]

**Fusion Priority**: 7 (new from fusion UT-2; entirely absent from any prior session)
**Dependency**: None — structural geometry, independent of KC-3 verdict. **START FIRST.**

**What**: Compute the 4 eigenvalues of the V_total Hessian in the 4 off-Jensen directions of the 5D moduli space of left-invariant metrics on SU(3), evaluated at the BCS minimum tau_0 = 0.35.

**Why this matters**: The entire BCS analysis lives on the 1D Jensen curve (parameterized by tau). The full moduli space of left-invariant metrics on SU(3) is 5-dimensional (Baptista Paper 15). If any of the 4 off-Jensen eigenvalues is negative at the BCS minimum, the modulus escapes the Jensen curve into the 5D interior. The BCS minimum location and depth would change — possibly disappearing entirely. This is a structural prerequisite for:
- The backreaction ODE (29A's 29b-2) to have physical meaning
- The D_total Pfaffian computation (29Bc) to be geometrically meaningful

**The 5D parameterization** (from Baptista Paper 15, Section 3.7): Left-invariant metrics on SU(3) are parameterized by 5 independent scale factors on the orthogonal decomposition su(3) = u(1) + su(2) + C^2. The Jensen family fixes 3 of these via the volume-preserving constraint and the particular scaling lambda_1 = e^{2s}, lambda_2 = e^{-2s}, lambda_3 = e^s. The 4 transverse directions break either:
- (a) the volume-preserving constraint (breathing mode: all scales change uniformly)
- (b) the Jensen proportionality within the su(2) block (SU(2) anisotropy)
- (c) the Jensen proportionality within the C^2 block (C^2 anisotropy)
- (d) the Jensen ratio between u(1) and su(2) blocks (cross-block mixing)

**Symmetry argument** (fusion UT-2): At tau = 0 (round metric), the enhanced SU(3) x SU(3)/Z_3 symmetry makes the Jensen direction an eigenmode. All transverse perturbations are also eigenmodes by symmetry, with eigenvalues determined by group theory. At tau > 0, transverse couplings are generated perturbatively and grow with tau.

**Method**:
1. From Paper 15 (eq 3.68 and surrounding), extract the 5D metric parameterization
2. Compute the Dirac spectrum at 8-16 off-Jensen metric points near the Jensen minimum (tau = 0.35 + small transverse perturbations delta_a in each of 4 directions)
3. Evaluate V_total = V_spec + F_BCS at each off-Jensen point
4. Construct the 4x4 transverse Hessian via finite differences
5. Diagonalize: if all 4 eigenvalues > 0, Jensen curve is a valley

**Gate condition (P-29d)**: All 4 eigenvalues > 0 at the BCS minimum. If satisfied: Jensen ansatz is structurally stable, backreaction ODE is physically meaningful.

**Constraint Condition (B-29d)**: If any eigenvalue < 0: the modulus is unstable off-Jensen. The BCS analysis must be repeated in the full 5D space (multi-session effort). The 1D backreaction from 29A is unreliable.

**Existing infrastructure**:
- `tier1_dirac_spectrum.py`: full Dirac spectrum computation for any left-invariant metric. Contains `jensen_metric(tau)` and `compute_structure_constants()`. Adaptable to general left-invariant metrics.
- `s25_baptista_results.py`: moduli space metric G_{tau,tau} = 5 on the Jensen curve
- `s28b_hessian.py`: 2D Hessian code, adaptable to higher dimensions

**What must be built new**:
1. General left-invariant metric parameterization (5 scale factors instead of Jensen's 1)
2. Off-Jensen Dirac spectrum driver (call `tier1_dirac_spectrum` with modified metric)
3. 4x4 transverse Hessian assembly from finite differences
4. Eigenvalue extraction and stability verdict

**Computational cost**: MEDIUM. Each off-Jensen Dirac spectrum takes ~8.7s at max_pq_sum = 6. Need 8-16 off-Jensen evaluations (2 per direction, finite difference). Total: ~70-140s for spectra + BCS evaluation. Dominated by spectrum computation.

**Agent**: phonon-exflation-sim (heavy computation) + baptista-spacetime-analyst (geometry)

**Output**: `s29b_jensen_transverse.npz`, `s29b_jensen_transverse.py`

---

## 29B-3: BCS Gap Equation with Bogoliubov Occupation [LOW COST, THERMAL GOLDILOCKS]

**Fusion Priority**: 5 (thermal Goldilocks resolution; UT-5)
**Dependency**: Requires 29A entropy balance PASS. If entropy FAILS, skip this computation.

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

**Gate condition (P-29c)**: Delta(n_k = B_k) / lambda_min > 0.01 at the 3 load-bearing sectors. If satisfied: thermal Goldilocks confirmed — the non-equilibrium distribution supports BCS condensation.

**Constraint Condition (B-29c)**: If Delta = 0 for all sectors at all tau with Bogoliubov occupation: the non-equilibrium distribution is too hot for condensation. The BCS mechanism requires a thermalization step not captured by KC-1/KC-2 alone.

**Inputs**: `s28a_bogoliubov_coefficients.npz`, `s23a_kosmann_singlet.npz` (V_nm for (0,0)), `s27_multisector_bcs.npz` (V_nm for other sectors)

**Script**: `s29b_bogoliubov_bcs.py` — modify from `s26_multimode_bcs.py` or `s23a_bcs_gap_equation.py`. Swap Fermi-Dirac for B_k interpolant. ~60 lines of modification.

**Computational cost**: < 5 minutes. Self-consistency loop converges in ~20 iterations.

**Agent**: phonon-exflation-sim (computation), landau-condensed-matter-theorist (BCS physics)

**Output**: `s29b_bogoliubov_bcs.npz`, `s29b_bogoliubov_bcs.py`

---

## 29B-5: Full 1-Loop Inter-Sector Josephson Coupling J_ij [HIGH COST, FUNDAMENTAL]

**Fusion Priority**: 8 (partially addressed by 29A's 29a-4 at zeroth order)
**Dependency**: Requires 29A's J_perp estimate. If J_perp / Delta_BCS > 1 from 29a-4, this computation is confirmatory. If J_perp / Delta_BCS < 1, this computation is decisive for d_eff.

**What**: Compute the full 1-loop inter-sector Josephson coupling between the load-bearing conjugate pair (3,0) and (0,3):

$$J_{(3,0),(0,3)} = \sum_{n,m} \psi_n^{*(3,0)} V_{nm}^{\text{inter}} \psi_m^{(0,3)}$$

where V_{nm}^{inter} is the inter-sector component of the 4-point pairing interaction, computed from exact SU(3) Clebsch-Gordan coefficients for the (3,0) x (0,3) decomposition.

**Why this matters**: The d_eff fork (Synthesis C, Section VI) determines whether the BCS condensate has true long-range order (d_eff >= 2, J_perp/Delta > 1) or quasi-long-range order (d_eff = 1, Luttinger liquid). The XS-4 algebraic argument (J maps (3,0) to (0,3), forcing nonzero J_pair) guarantees J_pair != 0 but does not determine its magnitude. The geometric estimate J ~ O(tau^2) ~ 0.12 gives J/Delta ~ 0.17 (Landau) — weak Josephson regime.

**Key structural constraint**: D_K is exactly block-diagonal in Peter-Weyl (Session 22b theorem). The Kosmann operator K_a (which generates V_nm) involves commutators with D_K, so it too respects block-diagonality at the 2-point level. The inter-sector coupling comes exclusively from the 4-point vertex — the full T-matrix cross-sector channel, not the Kosmann matrix itself.

**Method**:
1. Compute SU(3) Clebsch-Gordan coefficients for (3,0) x (0,3) → irreps. The CG coefficient for the (0,0) singlet channel gives the leading Josephson amplitude.
2. Use eigenvectors from `s23a_eigenvectors_extended.npz` for modes in (3,0) and (0,3) sectors
3. Evaluate the 4-point overlap integrals V_{abcd} with a in (3,0), c in (3,0), b in (0,3), d in (0,3)
4. Sum with free propagators G_n = 1/(E_n - mu + i*eta) to get the 1-loop coupling
5. Extract J_pair, compute J_perp = J_pair / Delta_BCS

**Gate condition (P-29e)**: J_perp > 1 at tau = 0.35 → d_eff >= 2 (true long-range order, mean-field valid). J_perp < 1 but > T/(N*Delta) ~ 0.006 → quasi-long-range order (operationally sufficient for modulus freezing but not BCS in strict sense).

**Constraint Condition (B-29e)**: J_perp < T/(N*Delta) → effectively decoupled sectors. Each sector must stabilize independently. d_eff = 1, Mermin-Wagner fluctuations may destroy the gap.

**What must be built new**:
1. SU(3) CG coefficient computation for (3,0) x (0,3) (either tabulated or computed via weight diagrams)
2. Cross-sector 4-point overlap integral evaluation (extend `s28c_phonon_tmatrix.py` cross-sector channel from bound to exact)
3. 1-loop Josephson coupling summation

**Inputs**: `s23a_eigenvectors_extended.npz`, `s22b_kosmann_matrix.npz`, `s27_multisector_bcs.npz`

**Computational cost**: HIGH. CG coefficient computation is O(dim^3) ~ O(10^3) per coefficient. 4-point overlaps require numerical integration over SU(3). Estimated: 30-60 minutes on 32-core.

**Agent**: phonon-exflation-sim (heavy computation)

**Output**: `s29b_josephson_coupling.npz`, `s29b_josephson_coupling.py`

---

# III. CONDITIONAL ARCHITECTURE

| 29A Outcome | 29B-4 | 29B-3 | 29B-5 |
|:------------|:------|:------|:------|
| **KC-3 PASS + entropy PASS** | RUN (always) | RUN | RUN |
| **KC-3 PASS + entropy MARGINAL** | RUN (always) | RUN (thermal resolution needed even if marginal) | RUN |
| **KC-3 FAIL** | RUN (always — standalone math) | SKIP | SKIP |
| **Entropy FAIL** | RUN (always — standalone math) | SKIP | SKIP (J_perp magnitude moot without BCS) |

Even in worst case (KC-3 FAIL), 29B-4 (Jensen 5D Hessian) produces a publishable mathematical result: the stability analysis of the moduli space of left-invariant metrics on SU(3), which is a pure differential geometry contribution (JGP/CMP level).

---

# IV. CONSTRAINT CONDITIONS AND GATE STRUCTURE

## Hard Closes

| ID | Condition | Consequence |
|:---|:----------|:------------|
| B-29c | Delta(n_k = B_k) = 0 for all sectors at all tau | Non-equilibrium distribution too hot for BCS. Thermalization mechanism needed. |
| B-29d | Any off-Jensen eigenvalue < 0 at tau = 0.35 | Jensen ansatz unstable. Full 5D moduli space analysis required (multi-session). |
| B-29e | J_perp < T/(N*Delta) | Sectors effectively decoupled. d_eff = 1. Mermin-Wagner destroys gap. |

## Positive Signals

| ID | Condition | Consequence |
|:---|:----------|:------------|
| P-29c | Delta(B_k)/lambda_min > 0.01 at 3 load-bearing sectors | Thermal Goldilocks resolved. BCS robust to non-equilibrium injection. |
| P-29d | All 4 off-Jensen eigenvalues > 0 | Jensen curve is a valley. Full 5D stability confirmed. Backreaction result reliable. **GATES 29Bc (D_total Pfaffian)**. |
| P-29e | J_perp / Delta > 1 | True long-range order. d_eff >= 2. Mean-field BCS fully justified. |

---

# V. OUTPUT FILES

| Computation | Output .npz | Output .py | Gate Verdict |
|:------------|:-----------|:-----------|:-------------|
| 29B-4 | `s29b_jensen_transverse.npz` | `s29b_jensen_transverse.py` | Off-Jensen stability |
| 29B-3 | `s29b_bogoliubov_bcs.npz` | `s29b_bogoliubov_bcs.py` | Thermal Goldilocks |
| 29B-5 | `s29b_josephson_coupling.npz` | `s29b_josephson_coupling.py` | J_perp / Delta gate |

Gate verdicts appended to: `tier0-computation/s29b_gate_verdicts.txt`

---

# VI. SUCCESS CRITERIA

Session 29Bb is successful if it produces:

1. **A Jensen transverse stability verdict** — all 4 off-Jensen eigenvalues positive or not. If PASS, this unlocks Session 29Bc (D_total Pfaffian).
2. **A thermal Goldilocks verdict** (conditional on 29A entropy PASS) — Bogoliubov-occupation BCS gap nonzero or zero at the 3 load-bearing sectors
3. **An inter-sector Josephson magnitude** (conditional on 29A J_perp) — J_pair, J_perp = J/Delta, d_eff determination

Computation order: 29B-4 first (no dependencies), then 29B-3 (after 29A entropy check), then 29B-5 (after 29A J_perp available). 29B-4 can run in parallel with late-stage 29A.

---

*Prompt decomposed from Session 29B Plan (Section III: 29B-3, 29B-4, 29B-5). 29B-4 has no dependencies and should start immediately. 29B-3 and 29B-5 wait for 29A gate check. Total runtime: ~90 minutes (dominated by 29B-5 CG coefficients + 4-point overlaps).*
