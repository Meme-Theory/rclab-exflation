# Session 63 Wave 2 Working Paper

**Date**: 2026-03-30
**Session**: S63 — Folding CC
**Format**: Parallel single-agent computations across 7 waves
**Plan**: `sessions/session-plan/session-63-plan.md`
**Motivation**: CC problem = integrability problem (8 closures). Push CC frontier (LOCAL-ENTANGLE, JACOBSON-GGE, RICHARDSON-GAUDIN, fermionic q-theory) + execute ALL pre-registered S63 gates from S62 workshop synthesis + ALL reviewer recommendations from 12 collab files.
**Master Gate**: LOCAL-ENTANGLE-63 -- local entanglement entropy of GGE across Rindler cut on CG(24)

---

## Agent Instructions

```
When writing your results section:
1. **Verdict first**: PASS / FAIL / INFO with the decisive number
2. **Key numbers**: All computed values with units and precision
3. **Cross-checks**: What independent verification was performed
4. **Data files**: Full paths to scripts, data, plots produced
5. **Assessment**: 2-3 sentences on structural implications
```

---

## Wave 2: Convergence and Structure (8 parallel)

### W2-01: SHELL-HESSIAN-63 — Shell-by-Shell FRG Proxy (nazarewicz-nuclear-structure-theorist)

**Status**: COMPLETE
**Gate**: SHELL-HESSIAN-63 | W2-01 | STRUCTURAL | all 36 positive at all shells | **FAIL: stability depends on UV completion**

**Results**:

**Verdict: FAIL.** All 36 eigenvalues negative at L=0,1,2. All 36 positive only at L=3. The transition is sharp and total -- fold stability requires the full UV spectrum.

**Key numbers:**
- PW shells: L=0 (16 modes), L=1 (288), L=2 (2,176), L=3 (10,400). Total: 12,880.
- Eigenvalue sign count at each shell cutoff:
  - L=0: 0+, 36- (lambda_min = -147.87)
  - L=1: 0+, 36- (lambda_min = -135.65)
  - L=2: 0+, 36- (lambda_min = -61.83)
  - L=3: 36+, 0- (lambda_min = +31.04)
- All 36 eigenvalues monotonically increasing with L (no oscillatory behavior).
- Per-shell contribution to one-loop Frobenius norm:
  - L=0: 0.17%, L=1: 2.52%, L=2: 17.41%, L=3: 79.90%
- One-loop / tree Frobenius ratio: 0.005 (L=0), 0.088 (L=1), 0.658 (L=2), 3.275 (L=3).
  One-loop overtakes tree-level ONLY when L=3 shell is included.
- Cross-check to S62 full spectrum: max|S62 - S63| = 3.55e-06 (finite-difference accuracy).
- Cluster structure (7-8 clusters from Jensen 3+4+1 block decomposition) preserved at all L.
- Symmetry error in all shell Hessians: 0.00e+00 (exact machine symmetry).
- Computation: 119s total (36 diagonal + 630 off-diagonal perturbations, each shell-resolved).

**Cluster analysis at L=3 (full spectrum):**
| Cluster | Size | Mean eigenvalue | Width |
|---------|------|-----------------|-------|
| 0 | 1 | 31.04 | 0 |
| 1 | 5 | 56.61 | 4.17 |
| 2 | 9 | 73.75 | 1.44 |
| 3 | 3 | 125.38 | 0.0002 |
| 4 | 12 | 159.07 | 5.62 |
| 5 | 1 | 240.09 | 0 |
| 6 | 5 | 330.63 | 0.002 |

The 1+5+9+3+12+1+5 = 36 clustering is structurally tied to the Jensen metric blocks. Sizes 1, 3, 5 correspond to SU(2) multiplets (j=0,1,2). The 9 and 12 arise from cross-block mixing of SU(2) x coset directions. This cluster structure is preserved at every PW shell, with only the overall scale changing.

**Nuclear structure interpretation:**
This result has an exact parallel in nuclear DFT. In nuclear physics, the bulk Liquid Drop Model energy is always negative (attractive), and it is the shell correction energy (from occupied single-particle levels near the Fermi surface) that provides the additional binding and determines stability. But the key difference: nuclear shell corrections are perturbative (delta_E_shell/E_bulk ~ 1-5%). Here, the one-loop correction must REVERSE the sign of all 36 tree-level eigenvalues, requiring ||H_1loop||/||H_tree|| > 1. This only happens when the L=3 shell (80% of the one-loop norm) is included.

In Strutinsky terms: the smooth (Weyl) background from L=0-2 is insufficient. The oscillatory shell correction from L=3 is not a small perturbation -- it is the dominant contribution. The ratio ||H_1loop(L=3)||/||H_tree|| = 3.28 means the L=3 shell alone carries 3.3x the tree-level Hessian norm. This is NON-PERTURBATIVE one-loop stabilization, not a shell correction.

The FRG interpretation: integrating out UV modes shell-by-shell, the effective action at the fold point only acquires positive curvature (stability) when the last shell (L=3) is included. The functional renormalization group flow has a sign change at the boundary between L=2 and L=3. All eigenvalues cross zero simultaneously -- there is no sequential stabilization.

**Constraint map update:**
- CLOSED: "Fold stability is IR-robust (independent of UV completion)" -- definitively falsified.
- CONSTRAINED: Fold stabilization requires contributions from ALL PW shells up to at least L=3. The L=3 shell with its 10,400 modes (81% of total) provides 80% of the one-loop Hessian norm.
- OPEN: Whether L=4 and higher shells reinforce or dilute the stabilization. The monotonic increase of all 36 eigenvalues with L suggests reinforcement, but this is uncomputed.
- Pre-registered for future: SHELL-HESSIAN-EXT-64 -- extend to L=4 (max_pq_sum=4) to test whether the stabilization grows monotonically or saturates.

**Assessment:**
The FAIL is structurally informative, not catastrophic. It tells us that fold stability is a UV-sensitive property of the one-loop effective action. The spectral action's one-loop correction from the L=3 PW shell is not a perturbative correction -- it is the dominant term. This means any truncation scheme that omits high-L modes will fail to reproduce fold stability. For the framework, this constrains the UV completion: the full SU(3) representation content up to at least (p,q) with p+q=3 is required. The monotonic increase suggests convergence is from below -- adding more shells makes the fold MORE stable, not less. But this must be verified at L=4.

**Data files**:

- Script: `computations/s63_shell_hessian.py`
- Data: `computations/s63_shell_hessian.npz`
- Plot: `computations/s63_shell_hessian.png`
- Input: `computations/s62_hessian_oneloop.npz`, `computations/s61_moduli_hessian.npz`, `computations/s61_trace_formula_geometric.npz`

---

### W2-02: TENSOR-SCALAR-63 — Tensor-to-Scalar Ratio r (schwarzschild-penrose-geometer)

**Status**: COMPLETE
**Gate**: TENSOR-SCALAR-63 | W2-02 | EXISTENTIAL | r < 0.036 | PASS: survives BICEP/Keck | FAIL at r > 0.1: framework excluded

**Verdict**: **FAIL** (r = 0.346 > 0.1)

**Results**:

**Key numbers:**
- r = 16 * epsilon_H = 16 * 0.0216 = **0.346** (9.6x above BICEP/Keck r < 0.036)
- epsilon_H = 0.02163 (from S62 KZ-NS-62, spectral action Hubble method)
- Need epsilon < 0.00225 for PASS (9.6x reduction)

**Three suppression routes investigated, all CLOSED:**

| Channel | Mechanism | Result | Status |
|:--------|:----------|:-------|:-------|
| Starobinsky R^2 | Scalaron from a_4 enhances P_s, reduces r | m_s = 0.276 M_KK = 2.1e16 GeV; m_s/H = 141x. **Frozen** (m_s >> H). exp(-m_s^2/2H^2) = exp(-9897) ~ 0 | **CLOSED** |
| Multi-field | Jensen projection onto trace mode suppresses tensor coupling | cos(alpha) = 0 **exactly** (volume-preserving). BUT: P_t = 2H^2/(pi^2 M_Pl^2) is geometric theorem, independent of inflaton type. sin^2(alpha)=0 does NOT suppress tensors | **CLOSED** |
| Isocurvature | 36 light modes enhance P_s | Lightest mass = 5.57 M_KK; m_min/H = 2838. All modes frozen. Enhancement = 1.000001 | **CLOSED** |

**Sound speed c_s assessment:**
- W1-04 found c_s = 0.485 from Z_spectral / d^2S. This is a modulus-space diagnostic, NOT the DBI sound speed.
- For canonical scalar L = Z(tau)*X - V(tau): c_s^2 = P_X/(P_X+2XP_XX) = 1 (P_XX = 0).
- Even if c_s = 0.485 were physical: r = 16*eps*c_s = 0.168, still FAILS (r > 0.1).

**a_4 Gilkey decomposition:**
- a_4 integrand at fold: 500*R^2 (101.6%) + (-32)*|Ric|^2 (-0.8%) + (-28)*K (-0.7%)
- R^2 dominates a_4 by 183x (fold is near-Einstein: |S|^2/|Ric|^2 = 0.93%)
- In Weyl basis: 495*R^2 - 50.7*|S|^2 - 28*|C|^2. Weyl contributes -0.5% (negative).
- WCH connection: low Weyl at fold gives lightest scalaron. Even so, m_s ~ M_KK >> H.

**Structural (Penrose) analysis:**
- The hierarchy m_s ~ M_KK >> H ~ sqrt(A_s)*M_Pl is FUNDAMENTAL: A_s ~ 10^{-9} suppresses H.
- In the conformal diagram, the transit (N_e = 0.17 e-folds) is nearly a point event -- insufficient expansion to dilute epsilon.
- The tensor spectrum P_t = 2H^2/(pi^2 M_Pl^2) is a de Sitter vacuum property (geometric theorem). Cannot be suppressed by internal space dynamics.

**Escape routes (uncomputed):**
- 1-loop modified epsilon: tree Hessian reversal (H_1loop/|H_tree| = 3.5) suggests 1-loop spectral action could modify epsilon_H. Need: epsilon_1loop < 0.00225.
- Non-Bunch-Davies vacuum from supersonic transit (Mach = 13.8): modifies initial state of perturbations.
- Modified dispersion from KK tower: omega^2 = k^2 + lambda_n^2 alters UV tensor modes.
- Gauss-Bonnet modification: r = 16*eps*(1 - 8*alpha_GB*H^2), needs alpha_GB*H^2 ~ 0.5.

**Secondary predictions:**
- Scalaron mass: m_s = 2.05e16 GeV = 0.0084 M_Pl (too heavy for Starobinsky inflation)
- If c_s = 0.485 physical: f_NL_equil ~ 4.3 (testable by future CMB)
- M_Pl from spectral action: 8.38e17 GeV (0.34x PDG value; needs Lambda ~ 2.9x M_KK)

**Cross-checks:**
- S54 alpha_R2 = 14.16 reproduced. Scalaron mass consistent between ratio and direct methods.
- Gilkey coefficients verified against S20a/S61 curvature invariants at fold.
- Volume-preservation (sum dg/g = 0) verified algebraically: 3*(-2)+4*(1)+1*(2) = 0.
- Isocurvature masses from S62 HESSIAN-ONELOOP-62 (all 36 positive eigenvalues).

**Assessment:**
This is the most serious FAIL in the framework's observational constraint map. The tensor-to-scalar ratio r = 0.346 exceeds the BICEP/Keck bound by 9.6x. All three proposed suppression channels (Starobinsky, multi-field, isocurvature) are closed by the mass hierarchy m_s, m_iso >> H. The FAIL is GEOMETRIC: it traces to epsilon_H = 0.0216 from the spectral action on SU(3), and no phononic mechanism modifies it. The most promising escape is 1-loop epsilon modification (the tree-to-1-loop Hessian reversal already demonstrates O(1) 1-loop corrections). This should be computed as a high-priority gate.

**Phononic classification**: GEOMETRIC (no BCS/GGE content in r)

**Data files**:
- Script: `computations/s63_tensor_scalar.py`
- Data: `computations/s63_tensor_scalar.npz`
- Plot: `computations/s63_tensor_scalar.png`

---

### W2-03: F0-MATCHING-63 — Both f_0 Interpretations for m_H (einstein-theorist)

**Status**: COMPLETE
**Gate**: F0-MATCHING-63 | W2-03 | CONSISTENCY | both give m_H in [120,135] | PASS: matching consistent | FAIL: f_0 ambiguity kills Higgs prediction

**Verdict**: **FAIL**. The two f_0 interpretations yield m_H = 131.8 GeV (Interp 1, Gaussian) vs m_H = 416.7 GeV (Interp 2, Gaussian). Disagreement 284.8 GeV exceeds the 20 GeV threshold. The internal f_0 = 4.26 interpretation is **excluded** as a standalone matching procedure for the Higgs mass.

**Results**:

1. **Interp 1 (external, f_0 = 9.82, alpha_GUT = 1/25)**:
   - Uses SM 2-loop running to determine g_3(M_KK) = 0.5161, then applies KK threshold correction delta(1/g_3^2) from W1-02.
   - Gaussian regulator (delta = 2.353): g_3(eff) = 0.4046, lambda_CCM = 0.0904, **m_H = 131.8 GeV** [IN BAND].
   - Sharp regulator (delta = 4.231): g_3(eff) = 0.3539, lambda_CCM = 0.0691, **m_H = 119.4 GeV** [marginal low].
   - Cross-checked against s63_kk_threshold.npz: agreement to 0.00 GeV (identical code path).
   - delta_BCS = 0.065 brings m_H to 125.1 GeV. Consistent with S62 BdG screening at 7%.

2. **Interp 2A (internal, f_0 = 4.26, alpha_GUT = 1/10.8, g_3 from SA)**:
   - SA predicts g_3^2(cutoff) = 4*pi/10.8 = 1.159. g_1, g_2, y_t from SM running.
   - Gaussian: g_3(eff) = 0.5577, lambda_CCM = 0.1717, **m_H = 416.7 GeV** [catastrophic overshoot].
   - Sharp: g_3(eff) = 0.4431, lambda_CCM = 0.1083, **m_H = 143.6 GeV** [marginal high].
   - delta_BCS = 0.322 required for m_H = 125.1 GeV. Unphysically large (32% screening).

3. **Interp 2B (internal, full SA unification, g_1 = g_2 = g_3 from SA)**:
   - All gauge couplings set to g = 1.077 at M_KK. RGE integration produces **NaN** for both regulators.
   - g_2(M_Z) = 3.10 (observed: 0.65) -- factor 4.8x overshoot. SU(2) coupling far too strong.
   - Full unification at M_KK is **structurally excluded** by SM gauge running.

4. **Consistency check (task item 4)**:
   - f_0 ratio: f_0(ext)/f_0(int) = 9.82/4.26 = 2.306. 1/alpha ratio: 25/10.8 = 2.306 (exact match).
   - Threshold fraction (Gaussian, Interp 1 SA basis): delta/(1/g^2 + delta) = 0.542.
   - Self-consistency ratio: 1/(1-0.542) = **2.183**, close to the predicted 1/(1-0.52) = 2.083. The 5% discrepancy traces to the exact Gaussian delta value (2.353 vs the approximate 2.0 that would yield 0.52 exactly).
   - Physical meaning: the KK threshold contributes 54% of the total 1/g_3^2 in Interp 1. This dominance is why both interpretations can converge in the SHARP limit (where delta = 4.23 overwhelms the bare coupling difference), but diverge catastrophically in the GAUSSIAN limit (where delta = 2.35 does not).

5. **Physical interpretation**:
   - The threshold correction is **additive in 1/g^2 space**. For Interp 1, 1/g^2(bare) = 1.99 and delta = 2.35, so the threshold is 54% of the total. For Interp 2, 1/g^2(bare) = 0.86 and delta = 2.35, so the threshold is 73% of the total. Despite contributing a larger fraction, the smaller bare 1/g^2 in Interp 2 leaves g_3(eff) = 0.558 (vs 0.405 for Interp 1), resulting in lambda_CCM 1.9x larger and m_H catastrophically heavy.
   - **Structural conclusion**: The Higgs mass prediction requires f_0 > ~7 (alpha_GUT < 1/18) for m_H to land in [120, 135] with the Gaussian regulator. The internal f_0 = 4.26 is too small by a factor ~2, producing a coupling too strong for the RGE to tame.
   - The sharp-cutoff Interp 2A result (m_H = 143.6 GeV) suggests that with a sufficiently aggressive cutoff, even the internal f_0 could work -- but the sharp cutoff at L=6 is NOT converged (ratio L6/L5 = 1.32, still growing). The Gaussian is the physical regulator.

6. **Constraint on solution space**:
   - **Interp 1 (SM running + KK threshold) is the correct matching**. It produces m_H = 131.8 GeV (Gaussian), within [120, 135].
   - **Interp 2 (SA determines g_3) is excluded** for the Higgs mass. The internal f_0 = 4.26 sets the scale of the gravitational sector (a_2/a_0 matching), NOT the gauge coupling.
   - The two f_0 values describe DIFFERENT physical quantities: f_0(ext) = gauge coupling normalization, f_0(int) = gravitational trace-log contribution. They are not alternative matchings of the same quantity.

**Data files**:

- Script: `computations/s63_f0_matching.py`
- Data: `computations/s63_f0_matching.npz`
- Plot: `computations/s63_f0_matching.png`

---

### W2-04: YUKAWA-HYBRID-63 — Generation-Dependent Overlaps at Hybridization Gaps (phonon-first-cosmologist)

**Status**: COMPLETE
**Gate**: YUKAWA-HYBRID-63 | W2-04 | STRUCTURAL | rank >= 3, splitting > 100 | PASS: hierarchy from phononic crystal | INFO/FAIL: rank-1 persists

**Verdict**: **INFO** — Rank=2 (need 3). Splitting=23,935. V_AB rank-1 forces basic Yukawa to rank-1. B-sector triality lifts to rank-2. Third generation direction blocked by t=1/t=2 CPT symmetry.

**Results**:

**Key numbers:**

| Quantity | Value | Units/Notes |
|:---------|:------|:------------|
| V_AB rank (SVD) | 1 | sigma_2/sigma_1 = 1.0e-16. Separable: V_AB[a,b] = f(a)*g(b) |
| Yukawa rank (basic triality) | 1 | All triality sectors see identical B-mode profile |
| Yukawa rank (Jensen-enhanced) | 1 | Jensen scale factors multiply outside, cannot break rank-1 |
| Yukawa rank (A+B triality) | 2 | B-sector t=1/t=2 modes create second independent direction |
| Best splitting (rank-2 eigenvalues) | 23,935 | lambda_max/lambda_min of positive eigenvalues |
| Jensen max splitting | (L1/L2)^2 = 4.57 | e^{8*tau_fold} at tau=0.19 |
| Required splitting | ~135,000 | m_t/m_u observed |
| Unique crossings identified | 10 | From 19 tight gaps (deduped by A-mode, B-mode, k-point) |
| Triality population (992 modes) | t=0: 464, t=1: 264, t=2: 264 | CPT exact: N_t1 = N_t2 |
| Triality angles (v_0, v_1, v_2) | all 0.000 deg | All proportional -- rank-1 confirmed |

**Three methods tested, in order of physical refinement:**

1. **Basic triality** (Section 7): Classify 36 A-sector modes by Z_3 triality t = (p-q) mod 3. Compute triality-projected coupling v_t[beta] = sum_alpha V_AB[alpha, beta] * triality_A[alpha, t]. Result: all three v_t vectors are exactly proportional (angle = 0.000 deg). Rank = 1. Root cause: V_AB = f(alpha) * g(beta) is separable, so the triality sum factorizes: v_t[beta] = c_t * g(beta).

2. **Jensen-enhanced** (Section 9): Include triality-dependent Jensen scale factors (L1 = e^{2*tau}, L2 = e^{-2*tau}, L3 = e^tau) inside the coupling vertex. Result: still rank-1 (SVD sigma_2/sigma_1 = 1.1e-17). The Jensen factors multiply each y_g uniformly across crossings.

3. **Full A+B triality** (Section 12): Assign triality to B-sector modes: B2 (flat bands) at t=1,t=2; B1/B3 at t=0. Apply triality selection rule: coupling suppressed 10x when A and B trialities mismatch. Result: **rank = 2, splitting = 23,935**. B-sector triality creates a second independent direction because crossings involving B2 modes (t=1 or t=2) suppress one generation while enhancing another. But t=1 and t=2 B-modes contribute equally by CPT, blocking the third independent direction.

**Structural diagnosis:**

The rank-1 obstruction is an exact mathematical consequence of the S62 V_AB construction: V_AB[alpha, beta] = A_coset * proj(alpha) * |dE_sp(beta)/dtau| / sqrt(omega_A(alpha) * omega_B(beta)) separates in alpha and beta. Any triality weighting of the alpha index changes the scalar prefactor, not the B-mode profile. The phononic crystal avoided crossings modulate the OVERALL Yukawa scale at each crossing but cannot differentiate between generations through this channel.

The rank-2 from Method 3 is physically meaningful: the 8 BCS modes decompose as B2 (4 modes, t=1 and t=2) + B1 (1 mode, t=0) + B3 (3 modes, t=0). When a crossing involves a B2 mode with t=1, generation 3 (fundamental) gets enhanced while generation 1 (anti-fundamental) gets suppressed. But CPT enforces N(t=1) = N(t=2) exactly, so the TOTAL coupling for gen1 and gen3 stays equal. The splitting comes from t=0 versus t=1,2 distinction only.

**Cross-pillar connection:** Structurally identical to the "flavor-blind interaction" problem in nuclear physics (Pillar IV/V). A central potential gives degenerate single-particle energies; the spin-orbit interaction (rank > 1) breaks the degeneracy. The analog: V_AB needs a "spin-orbit-like" non-separable term. The Jensen deformation is the analog of quadrupole deformation -- breaks symmetry but does not alone create the full hierarchy.

**Constraint map update:**
- CONSTRAINED: Hybridization gaps cannot produce rank >= 3 Yukawa while V_AB is rank-1
- OPEN: Whether d^2 S_A / d(phi) d(E_sp) gives V_AB with rank >= 3
- OPEN: Whether B-sector triality (rank-2, splitting 23,935) survives with non-separable V_AB
- Pre-registered: VAB-RANK-64 -- compute rank of spectral action second variation

**Data files**:

- Script: `computations/s63_yukawa_hybrid.py`
- Data: `computations/s63_yukawa_hybrid.npz`
- Plot: `computations/s63_yukawa_hybrid.png`
- Output log: `computations/s63_yukawa_hybrid_output.txt`
- Input: `computations/s62_phonon_dispersion_full.npz`, `computations/s62_yukawa_hierarchy.npz`, `computations/s61_trace_formula_geometric.npz`, `computations/s55_bogoliubov_992.npz`

---

### W2-05: TWO-LOOP-ESTIMATE-63 — Quartic SA Convergence Test (volovik-superfluid-universe-theorist)

**Status**: COMPLETE
**Gate**: TWO-LOOP-ESTIMATE-63 | W2-05 | CONVERGENCE | S_2loop/S_b < 0.30 | **PASS** (S_2loop/S_b = 3.7e-5)

**Results**:

**GATE VERDICT: PASS.** S_2loop/S_b = 3.7e-5, far below the 0.30 threshold. The two-loop correction is negligible compared to tree level. But the physics is more interesting than a simple PASS suggests.

1. **Quartic couplings V_{iijj} = d^4 S_eff / dphi_i^2 dphi_j^2** computed by 4th-order finite differencing (5-point stencil) along the 5 softest Hessian eigenvectors at step h = 0.01, with Richardson extrapolation at h/2 = 0.005 for error control.
   - Self-quartic V_{iiii}: range [4.03, 15.49] (dimensionful, in SA units)
   - Cross-quartic V_{iijj}: full 5x5 matrix computed. Off-diagonal entries range [2.89, 6.35]
   - Richardson extrapolation confirms convergence: V(h) and V(h/2) agree to 0.1%
   - Clear cluster structure: modes 2,3,4 (nearly degenerate lambda ~ 57.4) have large self-quartic (V ~ 15.5) while softest mode 0 (lambda = 31.0) has V ~ 4.0

2. **Two-loop sunset diagram** S_2 = (1/8) sum_{i,j} V_{iijj} / (lambda_i * lambda_j):
   - 5 soft modes only: S_2loop = 0.0080 (S_2/S_b = 7.2e-7)
   - Uniform V extrapolation to 36 modes: S_2loop = 0.098 (S_2/S_b = 8.8e-6)
   - Scaled V extrapolation (best estimate): S_2loop = 0.414 (S_2/S_b = 3.7e-5)
   - All three methods give S_2/S_b << 0.30

3. **Popov self-energy correction**: delta_lambda_i / lambda_i ranges from 0.43% (mode 1) to 0.92% (mode 0). The Popov contribution S_Popov = -0.016 is twice the sunset and opposite sign, but both are negligible relative to S_b.

4. **The central discovery: species-counting vs. coupling strength.**
   S62 found S_1loop/S_b = 0.519, suggesting "strong coupling." The two-loop result demolishes this interpretation:
   - The dimensionless quartic coupling g = V_{iijj}/(lambda_i * lambda_j) = **0.0026 +/- 0.0014** (WEAK)
   - S_2loop/S_1loop = 7.2e-5 (5 modes) to 7.2e-2 (extrapolated), NOT ~ 0.52 as geometric convergence would predict
   - The resolution: S_1loop = (1/2) sum_{n=1}^{12880} ln(lambda_n^2) sums over **12,880 Dirac eigenvalues** while S_2loop sums over **36x36 = 1,296 Hessian mode pairs**. The large one-loop ratio is a **species-counting effect**, not strong coupling.
   - Verification: S_1loop = (1/2) * 12880 * 0.893 = 5751.35 (exact). Each Dirac eigenvalue contributes <ln(lambda^2)> ~ 0.89, and 12,880 of them produce the 52% ratio relative to the spectral action (which also sums over these 12,880 modes).

5. **Volovik perspective: the superfluid analog is 3He-B far from T_c, not near T_c.**
   - In 3He-B: the quartic coupling g_4 ~ (T_c/E_F)^2 ~ 10^{-6}, while quantum depletion ~ T/T_c
   - Here: g ~ 0.003 while quantum depletion = 0.447
   - Same pattern: one-loop (zero-point energy, species counting) >> two-loop (actual mode-mode interactions)
   - The system is **weakly interacting in the moduli space** despite having many modes
   - S62's "strong coupling" verdict was a MISDIAGNOSIS: the correct expansion parameter is g ~ 0.003, not S_1/S_b ~ 0.52

6. **Geometric convergence test:**
   - Geometric prediction: S_2/S_b = (S_1/S_b)^2 = 0.269. WRONG by factor 7,300
   - Correct prediction: S_2/S_b ~ g * (N_hessian/N_Dirac) ~ 0.003 * (36^2/12880) ~ 3e-4. Observed: 3.7e-5. Reasonable given approximations.
   - The loop expansion is NOT geometric in the naive sense. It is controlled by g ~ 0.003 per loop, with a large one-loop contribution from species counting.

7. **Implications for the partition function:**
   - Z_eff = Z_tree * (1 + O(g)) where g = 0.003. Two-loop corrections to Z are 0.3%.
   - The S62 one-loop determinant det(H_eff) = 5.7e74 is reliable: two-loop shifts to eigenvalues are O(1%) (Popov).
   - The CC gap (114-117 orders) is COMPLETELY UNAFFECTED by two-loop corrections (shift < 0.001 orders).
   - G_N correction: the S62 shift of -0.75% receives a further O(g) = O(0.3%) two-loop correction, negligible.
   - **The partition function is perturbatively stable.** The alarming S_1loop/S_b = 52% from S62 does not signal breakdown; it is species-counting, and the actual interaction is weak.

**Data files**:

- Script: `computations/s63_two_loop_estimate.py`
- Data: `computations/s63_two_loop_estimate.npz`
- Plot: `computations/s63_two_loop_estimate.png`

---

### W2-06: HESSIAN-CASIMIR-63 — Ad(U(2)) Irrep Assignment of Hessian Clusters (baptista-spacetime-analyst)

**Status**: COMPLETE
**Gate**: HESSIAN-CASIMIR-63 | W2-06 | STRUCTURAL | all 36 assigned to irreps | **PASS** | Cluster structure PERMANENT

**Results**:

**Verdict: PASS** -- All 36 Hessian eigenvectors assigned to Ad(U(2)) irreps. The 10-cluster eigenvalue structure of H_eff is EXACTLY the decomposition of Sym^2(su(3)) under Ad(U(2)) = Ad(SU(2) x U(1)). Structural result (Schur's lemma); cannot be changed by equivariant perturbative corrections.

**Method**: Constructed 4 generators T_alpha (alpha=0,1,2,7) of Ad(U(2)) as 36x36 skew-symmetric matrices on Sym^2(R^8) via SU(3) structure constants. Computed C_2(U(2)) = sum T_alpha^2, C_2(SU(2)) = T_0^2+T_1^2+T_2^2, and T_7^2. Anti-Hermitian convention: C_2(SU(2)) = -j(j+1), T_7^2 = -Y^2.

**Decomposition table** (su(3) = k[j=1,Y=0] + y[j=0,Y=0] + m[j=1/2,Y=+/-q]):

| Irrep | j | Y^2 | C_2(U2) | dim | Cluster(s) | Obs dim |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|
| Sym^2(k) quintet | 2 | 0 | -6 | 5 | Cl9 (330.6) | 5 |
| Sym^2(m) j=1,Y=+/-2q | 1 | 3 | -5 | 3+3 | Cl4 (74.2) | 6 |
| k*m j=3/2,Y=+/-q | 3/2 | 3/4 | -9/2 | 4+4 | Cl7 (160.9) | 8 |
| k*y + Sym^2(m) j=1,Y=0 | 1 | 0 | -2 | 3+3 | Cl3+Cl5 (72.8,125.4) | 6 |
| k*m + y*m j=1/2,Y=+/-q | 1/2 | 3/4 | -3/2 | (2+2)+(2+2) | Cl2+Cl6 (57.4,155.3) | 8 |
| 3 singlets j=0,Y=0 | 0 | 0 | 0 | 1+1+1 | Cl0,1,8 (31.0,53.3,240.1) | 3 |
| **Total** | | | | **36** | **10 clusters** | **36** |

**Key numbers**:
- C_2 spread within clusters: < 1e-8 (machine precision)
- Max ||C_2 v - c_2 v||: 1.92e-4 (simultaneous eigenvector PASS)
- [H_eff, C_2] in tree eigenbasis: 9.93e-3 (one-loop FD noise)
- Generators exactly skew-symmetric (error: 0)
- All 6 C_2(U(2)) eigenvalues match predicted multiplicities (5,6,8,6,8,3)

**Cross-checks**: (1) C_2(SU(2)) on adj=3D block gives -2 (j=1), on coset=4D gives -3/4 (j=1/2). (2) T_7 eigenvalues on coset: +/-sqrt(3)/2, on SU(2) block: 0. (3) 10 clusters each carry single C_2 value. (4) Predicted = observed dimension for all 6 eigenspaces.

**Structural assessment**: PERMANENT. The pattern {1,1,4,3,6,3,4,8,1,5} is representation-theoretic. Ten clusters (not 9) because the three j=0 singlets from Sym^2(k), Sym^2(y), Sym^2(m) have distinct Hessian eigenvalues (physically: SU(2)-radial, U(1)-radial, coset-radial deformations). Non-singlet multiplets are exactly degenerate up to ~1e-4 one-loop noise.

**Classification**: GEOMETRIC.

**Data files**:

- Script: `computations/s63_hessian_casimir.py`
- Data: `computations/s63_hessian_casimir.npz`
- Input: `computations/s62_hessian_oneloop.npz`

---

### W2-07: RUNNING-NS-63 — Spectral Index Running dn_s/d(ln k) (mack-cosmic-bridge)

**Status**: COMPLETE
**Gate**: RUNNING-NS-63 | W2-07 | OBSERVATIONAL | |dn_s/dlnk| < 0.013 | **PASS** (0.78-sigma from Planck)

**Results**:

**GATE VERDICT: PASS** -- dn_s/dlnk = 0.000715, |dn_s/dlnk| = 0.000715 < 0.013.

**Key numbers:**
- dn_s/dlnk (adopted, median of 5 MS methods) = **0.000715**
- Planck 2018: dn_s/dlnk = -0.0045 +/- 0.0067 (68% CL)
- Tension with Planck: **0.78-sigma**
- Power-law exact (constant epsilon): dn_s/dlnk = 0.0000 identically
- MS-based method spread: [-0.008, +0.009] (6 methods, all PASS)

**Spectral action derivatives at fold (tau = 0.19):**
- S = 250360.68, S' = 58672.78, S'' = 317888.49, S''' = 97818 (spline+FD average)
- d3S/dtau3: spline = 93296, FD(h=0.005) = 102340, adopted = 97818

**Slow-roll parameters (both conventions):**

| Parameter | S62 Geometric | Standard Potential |
|:----------|:--------------|:-------------------|
| epsilon | eps_geom = 0.02163 | eps_V = 0.02746 |
| eta | eta_geom = -22.12 | eta_V = 1.270 |
| xi^2 | S'S'''/S^2 = 0.0916 | same |
| 4*eps*eta | **-1.91** (WRONG param) | **0.139** (right param) |

**Convention clarification (the central finding):**

The task asked whether 4*eps*eta = -1.9 produces catastrophic running. The answer is **NO**, for two independent reasons:

1. **Convention mismatch**: The eta_H = -22 is the S62 definition (1 - S*S''/S'^2), a geometric shape parameter measuring how rapidly eps_geom changes along the spectral action. The standard running formula uses eta_V = V''/V = S''/S = 1.27. With the correct eta_V, the cross-term is 0.14, not -1.9.

2. **Slow-roll breakdown**: Even with eta_V = 1.27, the perturbative slow-roll expansion diverges (|eta_V| >> 0.01). The first-order n_s formula gives n_s = 3.37 (meaningless). The power-law resummation n_s = (1-3eps)/(1-eps) = 0.956 absorbs all powers of eta into the exact result for constant epsilon. Running then tracks only the residual variation of eps with scale.

3. **Physical running from MS P(k)**: The Mukhanov-Sasaki mode equation P(k) (40 k-values, Bessel/numerical) shows n_s is nearly constant across the fold, with curvature |alpha| < 0.01 at all interior scales.

**Pathology identified: tau-to-N mapping artifact.** Mapping eps(tau) to eps(N) using dN = d(ln S)/2 compresses the entire S(tau) profile into 0.023 effective e-folds, producing dn_s/dN ~ -4 (590-sigma!). This is a mapping artifact: tau is the SU(3) modulus, not physical conformal time. The MS mode equation bypasses this mapping entirely.

**Second-order n_s (diagnostic only):**
- n_s (1st PSR) = 3.37 (divergent, eta_V >> eps_V)
- n_s (2nd PSR) = 3.46 (also divergent)
- n_s (power-law exact) = 0.9558 (correct, resummed)
- C_SL = -0.730

**Cross-checks:**
- 5-point FD at 4 step sizes converges to d3S ~ 102000 (consistent to 0.8%)
- Spline vs FD discrepancy: 8.8% (cubic spline is 3rd-order, FD samples the same interpolant)
- Quadratic fit P(k) residual: 2.65e-4 (quadratic captures the shape well)
- All 6 MS-derived running estimates satisfy |alpha| < 0.013

**Assessment**: The spectral action running is small because epsilon is nearly constant at the fold. The large eta_H = -22 measures the curvature of S(tau), which is absorbed into n_s itself (making n_s ~ 0.96 rather than ~1.00) but does not generate running. This is structurally analogous to power-law inflation, where n_s departs from 1 but dn_s/dlnk = 0 exactly. The O(0.001) residual running from the MS numerical P(k) is well within Planck bounds at 0.78-sigma.

**Data files**:
- `computations/s63_running_ns.py` -- computation script
- `computations/s63_running_ns.npz` -- all results, parameters, profiles
- `computations/s63_running_ns.png` -- 6-panel diagnostic plot

---

### W2-08: DDG-POWER-LAW-63 — Full 992-Mode KK Power-Law Running (kaluza-klein-theorist)

**Status**: COMPLETE
**Gate**: DDG-POWER-LAW-63 | W2-08 | STRUCTURAL | unification within 10% | PASS: GUT consistent | INFO: report f_0 resolution

**Verdict**: **INFO** — SM 1-loop unification quality 51.7% at M_KK (exceeds 10% gate). SU(2)-SU(3) near-unified (0.3% spread). U(1) is the outlier. f_0(running) = 88.79, far from both 4.26 (internal) and 9.82 (external). KK tower spans only 2.7% of logarithmic running range — DDG is a perturbative correction, not a resolution.

**Results**:

**Key numbers:**

| Quantity | Value | Units/Notes |
|:---------|:------|:------------|
| 1/alpha_1(M_KK) | 60.67 | GUT-normalized, SM 2-loop upward run |
| 1/alpha_2(M_KK) | 46.60 | SM 2-loop upward run |
| 1/alpha_3(M_KK) | 47.19 | SM 2-loop upward run |
| Spread (2-3) | 0.59 | 1/alpha_2 - 1/alpha_3 at M_KK |
| Spread (1-3) | 13.48 | 1/alpha_1 - 1/alpha_3 at M_KK |
| Unification quality | 51.7% | max spread / mean (1-loop SM at M_KK) |
| Required alpha_GUT^{-1} from U(1) | 75.97 | From observed alpha_1(M_Z) |
| Required alpha_GUT^{-1} from SU(2) | 46.89 | From observed alpha_2(M_Z) |
| Required alpha_GUT^{-1} from SU(3) | 46.73 | From observed alpha_3(M_Z) |
| f_0 (from mean alpha_GUT) | 88.79 | pi * mean(alpha_GUT^{-1}) / 2 |
| f_0 (internal, SECTOR-ENERGY-RATIO-62) | 4.26 | alpha_GUT = 1/10.8 |
| f_0 (external, CUTOFF-LONDON-62) | 9.82 | alpha_GUT = 1/25 |
| KK modes total | 992 | At fold tau=0.19 |
| Modes with omega < 1 (below M_KK) | 38 | Only 3.8% of tower |
| Modes with omega >= 1 (at/above M_KK) | 954 | 96.2% of tower |
| omega range | [0.820, 2.061] | M_KK units |
| KK log span | 0.922 | ln(omega_max/omega_min) |
| Total running range | 34.33 | ln(M_KK/M_Z) |
| KK fraction of running | 2.7% | Log span / total range |
| Max possible DDG correction | 145.5 | N_KK * delta_ln / (2*pi) |
| zeta(2) = sum omega^{-2} | 495.9 | Spectral zeta |
| zeta(4) = sum omega^{-4} | 299.7 | Spectral zeta |
| DDG integral sum ln(1/omega) | -384.6 | Net negative (most modes above M_KK) |

**Cross-checks:**
1. SM couplings at M_Z reproduced from PDG 2024 values: alpha_s = 0.1180, sin^2(theta_W) = 0.23122, alpha_em^{-1} = 127.955.
2. SM running to M_KK agrees with s62_higgs_bcs_threshold (g_3(M_KK) = 0.516, g_2(M_KK) = 0.519).
3. SU(2)-SU(3) near-unification (spread 0.59) consistent with known SM 1-loop result at ~ 10^{16} GeV (the standard MSSM GUT scale is 2 x 10^{16} GeV, and M_KK = 7.4 x 10^{16} GeV sits nearby).
4. 992-mode spectrum at fold verified against s44_dos_tau.npz. Sector counts: (0,0)=16, (1,0)/(0,1)=96, (2,0)/(0,2)=192, (1,1)=128, (3,0)/(0,3)=320, (2,1)/(1,2)=240.

**Assessment:**

The DDG power-law running computation reveals five structural facts:

1. **SU(2)-SU(3) near-unification is automatic.** The SM 2-loop running brings 1/alpha_2 and 1/alpha_3 to within 1.3% at M_KK = 7.4 x 10^16 GeV. This is the well-known "MSSM GUT miracle" surviving even without SUSY, because M_KK is close to the standard GUT scale. The KK tower cannot improve this further (it already agrees).

2. **U(1) hypercharge is the structural obstacle.** The 1/alpha_1 - 1/alpha_3 gap of 13.48 requires the 992-mode tower to contribute DIFFERENTIALLY (shifting U(1) more than SU(3)). This demands the explicit CSDR branching rules of SU(3) irreps under SU(3)_C x SU(2)_L x U(1)_Y from the Forgacs-Manton embedding. The computation is currently representation-agnostic. Pre-registered for CSDR-BRANCH-64.

3. **The KK tower is too narrow for power-law acceleration.** With 96.2% of modes above M_KK and the tower spanning only 2.7% of the logarithmic running range, the DDG enhancement is a perturbative correction at the few-percent level, not the order-of-magnitude effect needed to reconcile f_0 = 4.26 with f_0 = 88.79. DDG power-law running (which depends on many KK levels spread over a wide mass range) is structurally inapplicable to our compactification: the SU(3) fiber produces a CONCENTRATED tower near M_KK, not a SPREAD tower reaching to TeV scales.

4. **f_0 discrepancy confirmed and sharpened.** The effective f_0 from SM running (88.79) exceeds both the internal (4.26) and external (9.82) values by 10-20x. This confirms the W2-03 (F0-MATCHING-63) finding that f_0(internal) and f_0(external) describe DIFFERENT physical quantities: the former is a gravitational trace-log, the latter is the gauge coupling normalization. The DDG mechanism cannot bridge this gap because the tower is too narrow.

5. **The spectral action boundary condition is self-consistent.** Starting from unified alpha_GUT at M_KK and running down with SM betas, the predicted alpha_2(M_Z) and alpha_3(M_Z) approximately match observations for alpha_GUT^{-1} ~ 46.8 (i.e., f_0 ~ 73.5). This is the standard SU(5) unification prediction, which works for SU(2) and SU(3) but fails for U(1) by the well-known factor of ~1.6. The 992-mode tower, being concentrated near M_KK, cannot resolve this standard problem.

**Constraint map update:** DDG power-law running is NOT a viable mechanism for reconciling the f_0 discrepancy. The tower is too narrow. The two f_0 values (4.26 and 9.82) parametrize different sectors of the spectral action. Differential KK contributions require CSDR branching (pre-registered: CSDR-BRANCH-64).

**Data files**:

- Script: `computations/s63_ddg_power_law.py`
- Data: `computations/s63_ddg_power_law.npz`
- Plot: `computations/s63_ddg_power_law.png`

---

## Constraint Map Updates

| Entity | Type | Old State | New State | Gate/Evidence | Session |
|:-------|:-----|:----------|:----------|:--------------|:--------|
| DDG-POWER-LAW-63 | GATE | UNCOMPUTED | INFO | SM 1-loop unification 51.7% | S63 |
| DDG-narrow-tower | THEOREM | -- | PERMANENT | KK tower 2.7% of running range | S63 |
| f_0-discrepancy | OPEN-CHANNEL | OPEN | SHARPENED | f_0(run)=88.79 vs 4.26/9.82 | S63 |
| CSDR-BRANCH-64 | OPEN-CHANNEL | -- | PRE-REGISTERED | Differential KK -> U(1) fix | S63 |

*(Fill as gate verdicts arrive. Types: THEOREM, GATE, CLOSED, OPEN-CHANNEL, EQUATION)*

---

## Files Produced

| File | Wave | Description |
|:-----|:-----|:------------|
| `computations/s63_ddg_power_law.py` | W2-08 | DDG power-law running script |
| `computations/s63_ddg_power_law.npz` | W2-08 | All DDG results (spectrum, running, f_0) |
| `computations/s63_ddg_power_law.png` | W2-08 | 4-panel: SM running, DDG model, KK spectrum, f_0 scan |
