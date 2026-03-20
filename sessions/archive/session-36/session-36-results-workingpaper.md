# Session 36 Results Working Paper

**Date**: 2026-03-07
**Format**: Parallel single-agent computations, 3 waves (11 tasks)
**Plan**: `sessions/session-plan/session-36-plan.md`
**Master Gate**: SC-HFB-36 (self-consistent M_max)

---

## Instructions for Contributing Agents

Each agent writes ONLY to their designated section below. Include:
1. **Verdict** — PASS/FAIL/NEUTRAL with the gate ID
2. **Key numbers** — the critical quantitative results
3. **Cross-checks** — independent verification of results
4. **Data files** — paths to scripts, data, and plots produced
5. **Assessment** — brief interpretation (2-3 sentences max)

Do NOT modify other agents' sections. Do NOT write to any other file.

---

# Wave 1: Zero-Cost Workshop Diagnostics

---

### W1-A: M_max Authoritative Resolution (nazarewicz)

**Status**: COMPLETE
**Gate**: MMAX-AUTH-36. B2-only 4x4 M_max = 1.351 > 1.2. Multi-band treatment VALID.

**Results**:

**Verdict**: MMAX-AUTH-36 **GATE CRITERION MET** (B2-only 4x4 M_max = 1.351 > 1.2 threshold). Multi-band treatment is VALID.

**Key Numbers** (all at tau = 0.20, smooth van Hove DOS, MS = 1.046, impedance = 1.0):

| Subspace | dim | M_max | Status |
|:---------|:----|:------|:-------|
| 8x8 full (B1+B2+B3) | 8x8 | 1.6740 | PASS |
| 7x7 (B2+B3, no B1) | 7x7 | 1.3569 | PASS |
| 5x5 (B2+B1) | 5x5 | 1.6701 | PASS |
| 4x4 (B2-only) | 4x4 | 1.3513 | PASS |
| 1x1 (B2 diag max) | 1x1 | 0.5446 | FAIL |

**Proximity decomposition**:
- B3 proximity contribution: M(7x7) - M(4x4) = 0.006 (0.42%)
- B1 proximity contribution: M(8x8) - M(7x7) = 0.317 (23.4%)
- B1 proximity is regulator-independent (tested eta = 1e-6 to 0.1, all identical)
- B1 weight in dominant eigenvector: 24.6%. Participation ratio: 6.36

**Root cause of "1.445" vs "1.674" discrepancy** (RESOLVED):
- The "1.445" was computed with rho_B1 = 1.0 (arbitrary, Session 34 convention).
  Confirmed: smooth DOS + MS + rho_B1=1.0 gives M_max = 1.4449 exactly.
- The "1.670" uses rho_B1 = 3.94 (computed from group velocity, Session 35).
- With proper rho_B1, the B1 proximity channel V(B1,B2) = 0.080 activates,
  adding 0.225 to M_max.
- This is NOT a regulator artifact: B1 at mu=0 has |xi_B1| = E_B1 = 0.819,
  which is large. The proximity effect is a genuine physical coupling.

**Cross-checks** (all passed):
1. S34 5x5 (step+MS+imp1.56) reproduced: M = 0.9018 vs stored 0.9019 (disc = 1.4e-4)
2. S35 5x5 reproduced: M = 1.6701 vs stored 1.6701 (disc = 0)
3. S35 8x8 reproduced: M = 1.6740 vs stored 1.6740 (disc = 0)
4. All V matrix elements match S35 stored values to machine precision
5. Regulator insensitivity: M_max constant over 5 orders of magnitude in eta

**Nuclear DFT assessment**: The multi-band 8x8 Thouless is valid. V(B1,B1) = 0 (Trap 1) and V(B1,B3) = 0 (selection rule) are structural zeros correctly handled by the Thouless matrix. B1 is a "proximity donor" (nuclear analog: core polarization), not a blocked orbital. The B2-only 4x4 serves as conservative lower bound.

**Authoritative M_max range: [1.351, 1.674]**
- Conservative (B2-only): 1.351 (35% margin above threshold)
- With B1 proximity: 1.670 (67% margin above threshold)
- The "1.445" is SUPERSEDED (artifact of rho_B1 = 1.0 convention)

**Data files**:
- Script: `tier0-computation/s36_mmax_authoritative.py`
- Data: `tier0-computation/s36_mmax_authoritative.npz`

**Assessment**: The authoritative M_max lives in [1.351, 1.674] depending on whether B1 proximity coupling is included. Both bounds exceed 1.0. The conservative B2-only value (1.351) has 35% margin, comfortable for self-consistency corrections of order 20-30%. The "1.445" was a Session 34 workshop estimate using rho_B1 = 1.0, which suppressed the B1 proximity channel. The proper computation gives M_max(5x5) = 1.670. The Bayesian posterior p(M_max(SC) > 1) should be evaluated at the conservative bound M_max = 1.351, not at either 1.445 or 1.674.

---

### W1-B: Phase Transition Order — GL Cubic Term (connes)

**Status**: COMPLETE
**Gate**: GL-CUBIC-36. First-order (R* in R tensor_sym R) or second-order (standard BCS).

**Results**:

**Verdict: GL-CUBIC-36 = SECOND ORDER. No cubic GL invariant exists. U(1)_7 charge conservation forbids all cubic monomials. Standard BCS universality class (Z_2).**

**1. Representation analysis**

The BCS order parameter Delta carries K_7 charge q = -1/2 (pairing within the q = -1/4 doublet sector). Under the residual symmetry U(2) = SU(2) x U(1)_7:

| Quantity | Value |
|:---------|:------|
| R (order parameter) | (j=0, q_7 = -1/2), dim = 1 |
| R* (conjugate) | (j=0, q_7 = +1/2) |
| R x_sym R | (j=0, q_7 = -1), dim = 1 |
| R* in R x_sym R? | **NO** (q_7: +1/2 != -1) |
| Cubic GL invariant | **FORBIDDEN** |

**2. Analytic proof (U(1)_7 parity)**

Every field (Delta, Delta*) carries K_7 charge +/-1/2. A cubic monomial sums three such charges: q_total = (a + b + c)/2 where a, b, c in {-1, +1}. The sum a + b + c in {-3, -1, +1, +3} is always ODD, so q_total in {-3/2, -1/2, +1/2, +3/2} is never zero. All 20 distinct cubic monomials in (Delta_{--}, Delta_{++}, Delta_{--}*, Delta_{++}*) were checked exhaustively: zero charge-neutral invariants found. QED.

**3. Key numbers**

| Quantity | Value | Source |
|:---------|:------|:-------|
| K_7 eigenvalues on B2 | +/-0.25 (exact to 2.2e-16) | s35_k7_thouless.npz |
| SU(2) Casimir on B2 charge sector | 0.0932 * I (= alpha^2 * 3/4, alpha = 0.353) | This computation |
| [K_0, K_1] / K_2 ratio | 0.352589 (uniform, confirms rescaled su(2)) | This computation |
| SU(2) cross-block leakage | 0.000000 (exact) | This computation |
| max |c_3| across all tau | 1.57e-03 (fitting artifact, structurally zero) | s36_gl_cubic_check.npz |
| Leading pairing channel V | 0.1557 (symmetric/triplet) | This computation |
| Subleading channel V | 0.0314 (antisymmetric/singlet) | This computation |
| ||[K_7, D_K]|| | 1.89e-15 (machine epsilon) | Confirmed at tau = 0.20 |
| Latent heat | L = 0 EXACTLY (second-order) | Definition |
| Specific heat jump | Delta C / C_n = 1.426 (universal BCS) | BCS theory |

**4. SU(3) d-symbol check**

The non-abelian SU(3) embedding does NOT generate a cubic GL term because:
(a) Jensen deformation breaks SU(3) -> U(1)_7 in the Dirac spectrum. Only K_7 commutes with D_K (1.89e-15); all other generators are broken at O(0.24-0.29).
(b) The order parameter is 1-dimensional under the residual symmetry. The d_{abc} structure constants require a multi-component field (dim >= 3) to form a cubic invariant.
(c) Even if one attempted to embed Delta into the SU(3) adjoint, the U(1)_7 charge constraint still kills the cubic term by the analytic proof above.

**5. Universality class**

After J-pinning (Theorem B, S35 Workshop), the Goldstone manifold reduces from U(1) to Z_2. The physical order parameter is Delta_0 in R (real). The GL free energy is F = a * Delta_0^2 + b * Delta_0^4 with NO cubic or other odd terms. This is the Z_2 (mean-field Ising) universality class with standard BCS critical exponents: beta = 1/2, gamma = 1, delta = 3, alpha = 0 (jump).

The gap vanishes continuously: Delta(tau) ~ sqrt(tau_c - tau). Self-consistency corrections are PERTURBATIVE -- no discontinuous jump, no metastable coexistence region, no latent heat. The mean-field analysis is qualitatively correct.

**6. Bonus finding: triplet channel leads**

The symmetric (triplet) pairing channel V = 0.1557 dominates over the antisymmetric (singlet) V = 0.0314 by a factor of 5.0. This matches the Schur Casimir 0.1557 = V(B2,B2) diagonal, confirming that the leading instability is in the triplet channel. However, the cubic term conclusion is INDEPENDENT of channel: U(1)_7 charges +/-1/2 forbid cubic invariants for ANY spin j of the order parameter.

**7. Cross-checks**

1. Exhaustive monomial enumeration: 20/20 cubic monomials carry nonzero U(1)_7 charge
2. Numerical GL fit: c_3/c_2 < 7e-4 at all 8 tau values (fitting residual, not physical)
3. Structural: F(Delta) = sum sqrt(xi^2 + |Delta|^2) depends only on |Delta|^2, guaranteeing only even powers
4. SU(2) algebra closure verified: [K_0, K_1] = alpha * K_2 with alpha = 0.3526 uniform across all matrix elements
5. Cross-block vanishing: SU(2) generators have exactly zero matrix elements between q = -1/4 and q = +1/4 blocks

**8. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_gl_cubic_check.py` | Script (330 lines, 9 steps) |
| `tier0-computation/s36_gl_cubic_check.npz` | Results (8.8 KB) |
| `tier0-computation/s36_gl_cubic_check.png` | 4-panel plot |

**9. Assessment**

The BCS phase transition in the phonon-exflation framework is SECOND ORDER, resolving the workshop question (string-theory's 30% first-order estimate is ruled out). The cubic GL term is forbidden by an exact symmetry -- U(1)_7 charge conservation with charges +/-1/2 -- which makes the argument robust against perturbative corrections, higher PW sectors, or modified pairing kernels. This means the 44.5% margin in M_max is meaningful: the gap grows smoothly from zero, and self-consistency corrections are perturbative rather than catastrophic. The framework's mean-field BCS analysis is qualitatively reliable.

---

### W1-C: Collectivity Decomposition — Weisskopf Units (landau)

**Status**: COMPLETE
**Gate**: COLL-36. chi/chi_sp ratio: O(1) = no collectivity, O(10) = vibrational, O(100) = rotational.

**Results**:

**Verdict: COLL-36 = 12.1 W.u. => VIBRATIONAL (moderate coherence). Gate PASS (chi/chi_sp > 10).**

**1. Key numbers**

| Quantity | Value | Definition |
|:---------|:------|:-----------|
| chi_RPA (total) | 20.429 | d^2S/dtau^2 at tau = 0.20 (3-point FD on S_singlet) |
| chi_sp(max) | 1.689 | Largest single-mode curvature (B1) |
| chi_sp(B2) | 1.179 | Per-mode curvature in 4-fold degenerate B2 branch |
| chi_sp(B3) | 1.268 | Per-mode curvature in 3-fold degenerate B3 branch |
| chi_sp(avg) | 1.276 | Average over all 8 positive modes |
| chi/chi_sp(max) | **12.09 W.u.** | Collectivity ratio (most conservative) |
| chi/chi_sp(B2) | 17.32 W.u. | Using B2 as single-particle unit |
| chi/chi_sp(avg) | 16.01 W.u. | Using mean single-particle unit |
| N_eff | 12.1 | Effective number of coherent single-particle units |
| N_max | 16 | Total modes (8 positive x 2 for spectral pairing) |

**Branch decomposition of d^2S/dtau^2** (x2 for +/- pairing):
- B1 (1 mode): 3.378 (16.5%)
- B2 (4 modes): 9.435 (46.2%)
- B3 (3 modes): 7.609 (37.3%)
- Total bare: 20.422

**Energy-weighted sum rule (EWSR)**:
- m_0 = 20.42 (non-energy-weighted = bare chi)
- m_1 = 18.19 (energy-weighted: sum_k E_k * d^2|lambda_k|/dtau^2)
- Mean excitation energy <E> = m_1/m_0 = 0.890
- m_1(sum rule) = sum_k mult_k * (dlambda_k/dtau)^2 = 2.846
- EWSR fraction m_1/m_1(SR) = 6.39 (chi exhausts 6.4x the first-moment sum rule, consistent with second-derivative response dominating over first-derivative)
- chi_RPA / chi_bare = 1.0003 (RPA exhausts 100.0% of bare sum rule -- no missing strength)

**2. Cross-checks**
- Spline d^2/dtau^2 vs strutinsky mode sum: exact agreement (diff = 0.00e+00 for all 8 modes)
- 3-point finite difference of S_singlet at tau=0.20: 20.429, matching RPA d2S_abs to 0.03%
- All mode curvatures positive: constructive coherence (no cancellation between branches)
- Off-diagonal RPA coupling chi_sep = 0.728 (3.6% of total): collective enhancement is modest but nonzero

**3. Data files**
- Script: `tier0-computation/s36_collectivity.py`
- Data: `tier0-computation/s36_collectivity.npz`
- Input: `s33a_strutinsky.npz` (mode decomposition), `s32b_rpa1_thouless.npz` (RPA), `s23a_eigenvectors_extended.npz` (eigenvalues), `s27_multisector_bcs.npz` (eigenvalue tracks)

**4. Assessment**

The Jensen deformation response at tau = 0.20 is a *vibrational* collective mode in the Weisskopf classification. The ratio chi/chi_sp(max) = 12.1 means that 12 effective single-particle units contribute coherently to the spectral action curvature, out of a maximum of 16. This is not the trivial single-particle regime (ratio ~ 1), nor the maximally collective rotational regime (ratio ~ 100), but sits squarely in the vibrational band (10-30 W.u.). All three branches (B1, B2, B3) contribute constructively with positive curvature, and the off-diagonal RPA coupling adds a further 3.6% collective enhancement. The response is dominated by the B2 fold (46%) and B3 Debye tail (37%), with B1 contributing 17% -- consistent with the picture of a moderately collective multi-mode response driven by the Jensen deformation.

---

### W1-D: Anomaly Cancellation at KK Levels 1-3 (kaluza-klein)

**Status**: COMPLETE
**Gate**: ANOM-KK-36. All vector-like = PASS. Any chiral = FAIL.

**Results**:

**Verdict: ANOM-KK-36 = PASS. ALL KK levels 0-3 are VECTOR-LIKE at all tau.**

**1. Key numbers**

| Level | Sectors | dim(total spinor) | |A1| worst | |A3| worst | |A_grav| worst | Spectral pairing | Verdict |
|:------|:--------|:------------------|:-----------|:-----------|:--------------|:-----------------|:--------|
| 0 | (0,0) | 16 | 0.0 | 0.0 | 0.0 | exact | VECTOR-LIKE |
| 1 | (1,0), (0,1) | 48+48 | 0.0 | 0.0 | 0.0 | exact | VECTOR-LIKE |
| 2 | (1,1), (2,0), (0,2) | 128+96+96 | 0.0 | 0.0 | 0.0 | exact | VECTOR-LIKE |
| 3 | (3,0), (0,3), (2,1), (1,2) | 160+160+240+240 | 0.0 | 0.0 | 0.0 | exact | VECTOR-LIKE |

All three anomaly coefficients Tr(gamma_9 K_7) = Tr(gamma_9 K_7^3) = Tr(gamma_9) = 0 **exactly** (to machine epsilon) across all 10 sectors at all 5 tau values {0.00, 0.10, 0.19, 0.30, 0.50}. This is 150 independent anomaly coefficient evaluations, all identically zero.

Conjugate sector spectral matching:
- (1,0) vs (0,1): max_diff < 2.0e-15
- (2,0) vs (0,2): max_diff < 3.3e-15
- (3,0) vs (0,3): max_diff < 4.9e-15
- (2,1) vs (1,2): max_diff < 1.2e-14

**2. Cross-checks** (4 independent methods, all consistent)

1. **Spectral pairing**: Every eigenvalue of iD_K in every sector comes in +lambda/-lambda pairs with zero residual. No unpaired modes at any tau.
2. **Chirality index**: Tr(I tensor gamma_9) = 0 in every sector. Zero-mode index = 0 everywhere.
3. **Conjugate sector matching**: |spectrum(p,q)| = |spectrum(q,p)| to machine epsilon at all tau (see table above).
4. **Representation validation**: All 10 irreps verified as Lie algebra homomorphisms (max error < 8.3e-16) and anti-Hermitian (max error < 2.5e-16).

**Structural argument**: The result is a **structural theorem**, not numerical:
- pi_1(SU(3)) = 0: no orbifold projections to break vector-like pairing.
- For p != q: sectors (p,q) and (q,p) are complex conjugates. Combined content is automatically vector-like.
- For p = q (self-conjugate, here (1,1)): adjoint of compact Lie group is REAL representation. Dirac sector inherits reality, forcing A1 = A3 = 0.
- D_K block-diagonality (Session 22b): no inter-sector mixing can break per-sector vector-like structure.

**3. Data files**
- Script: `tier0-computation/s36_anomaly_kk.py`
- Data: `tier0-computation/s36_anomaly_kk.npz`

**4. Assessment**

The KK tower on SU(3)_Jensen is anomaly-free at all tested levels. This is guaranteed by the topology (pi_1 = 0) and representation theory (complex conjugation pairs sectors, real representations are self-conjugating) of the simply connected compact fiber, combined with the block-diagonality theorem that prevents inter-sector contamination. The framework is consistent above M_KK with no anomaly wall.

---

# Wave 2: Medium-Cost Computations

---

### W2-A: Inter-Sector PMNS via Inner Fluctuations (neutrino)

**Status**: COMPLETE
**Gate**: INTER-SECTOR-PMNS-36. PASS at R in [10, 100]. FAIL at R < 5.9.

**Results**:

**GATE VERDICT: FAIL** -- Singlet eigenspace mixing is IDENTICALLY ZERO on the Jensen curve. Schur-protected U(2) representation structure forces U = I (trivial PMNS).

**Script**: `tier0-computation/s36_intersector_pmns.py`
**Data**: `tier0-computation/s36_intersector_pmns.npz`
**Plot**: `tier0-computation/s36_intersector_pmns.png`

**Three-Part Computation**:

**Part 1 -- NCG inner fluctuation cross-sector: ZERO (confirmed)**
- Constructed D_K direct sum on V_{(0,0)} + V_{(1,0)} at tau = 0.190
- Off-diagonal block = 0.00e+00 (exact machine zero)
- Structural: phi = Id_geometric x phi_F (tensor product) cannot change Peter-Weyl labels
- CLOSES NCG inner fluctuations as a route to inter-sector PMNS

**Part 2 -- H_eff structural bound: CLOSED**
- Computed R x sin^2(theta_23) analytic bound at 6 tau values (0.12 to 0.30)
- Best achievable: 16.886 at tau = 0.30, vs required 17.8 (1.1x shortfall)
- At fold tau = 0.20: bound = 0.904, shortfall = 19.7x
- 100K MC trials at each tau: zero gate passes at any tau

| tau  | E_G1   | E_B2   | E_B3   | dE_12  | R_bare | Bound R*sin2_23 |
|:-----|:-------|:-------|:-------|:-------|:-------|:----------------|
| 0.12 | 0.835  | 0.848  | 0.927  | 0.013  | 6.6    | 0.130           |
| 0.15 | 0.837  | 0.846  | 0.945  | 0.009  | 11.2   | 0.278           |
| 0.18 | 0.838  | 0.845  | 0.965  | 0.007  | 18.9   | 0.566           |
| 0.20 | 0.840  | 0.845  | 0.978  | 0.005  | 27.2   | 0.904           |
| 0.24 | 0.844  | 0.847  | 1.007  | 0.003  | 59.8   | 2.395           |
| 0.30 | 0.852  | 0.852  | 1.053  | 0.001  | 336.0  | 16.886          |

**Part 3 -- Paper 18 misalignment (Phi-tilde overlap): ZERO MIXING**

Implemented eigenspinor overlap between D_K(tau) and D_K(0) eigenspaces. Identified B1 (1D trivial), B2 (4D fundamental), B3 (3D adjoint) branches. Computed subspace overlaps O_{ij} = Tr(Pi_{B_i}(tau) * Pi_{B_j}(ref)).

**Subspace overlap matrix is EXACTLY DIAGONAL at all tau**:

At tau = 0.20:
```
B_i\B_j(ref)   B1(1D)     B2(4D)     B3(3D)
B1(tau):       1.000000   0.000000   0.000000
B2(tau):       0.000000   3.977030   0.000000
B3(tau):       0.000000   0.000000   3.000000
```

PMNS estimates: sin^2(theta_13) = sin^2(theta_23) = sin^2(theta_12) = 0.000000 at ALL tau.

**Physical reason**: B1, B2, B3 are irreducible representations of U(2), preserved as residual isometry at all tau > 0 on the Jensen curve. Schur's lemma: irreps of different types CANNOT mix under U(2)-equivariant perturbation. Eigenspaces are locked to representation-theoretic subspaces. The 8D degenerate space at tau = 0 decomposes as 1+4+3 under U(2), matching B1+B2+B3 identically. This answers workshop FQ2: the decomposition is NOT a single irreducible -- it splits as 1+4+3. But because the Jensen deformation preserves U(2), both decompositions (at tau_0 and at tau = 0) use the SAME U(2) and hence are automatically aligned. U = I.

**Cross-checks**: Containment B1: 1.000, B2: 3.977/4, B3: 3.000/3. Unitarity err < 1.34e-02. Off-diagonal max = 0.000 at all tau.

**Surviving escape routes** (require NEW computation):
1. **Off-Jensen deformation (Paper 18 Step 3)**: Breaks U(2), allows B2 splitting and eigenspace rotation. OPEN.
2. **KK modified Lie derivative tilde{L}_{e_a}**: Couples modes from different Peter-Weyl sectors (not eigenstate overlap). OPEN.

**Assessment**: The inter-sector PMNS gate FAILS because eigenspace mixing is identically zero on the Jensen curve -- a consequence of Schur's lemma applied to the U(2)-invariant Jensen deformation. The bare eigenvalue ratio R_inter can reach the gate window [10, 100] via the B2-G1 near-degeneracy (R = 27.2 at tau = 0.20, R = 59.8 at tau = 0.24), confirming the mass hierarchy is structurally available, but the PMNS mixing angles are all zero. Only off-Jensen U(2)-breaking or the full KK gauge coupling can produce non-trivial mixing.

---

### W2-B: Self-Consistent GCM Kernel Integrals (nazarewicz)

**Status**: COMPLETE
**Gate**: SC-HFB-36 (MASTER). PASS at M_max(GCM) > 1.0. FAIL at M_max(GCM) < 1.0.

**Results**:

**Verdict: SC-HFB-36 = FAIL (unconstrained GCM). M_max(GCM, B2 eff) = 0.646 < 1.0. The BCS pocket does NOT form a global minimum in E_total(tau). CONDITIONAL PASS if tau is externally constrained near the fold.**

**1. Methodology**

Full GCM (Generator Coordinate Method) computation on a 47-point fine grid (dense sampling around tau_fold = 0.190). At each tau:
- Eigenvalues interpolated via cubic spline from 9 coarse-grid Dirac spectra
- Van Hove DOS modeled as Lorentzian enhancement (gamma = 0.020, peak at tau_fold)
- V matrix interpolated from nearest coarse-grid Kosmann kernel
- BCS gap equation solved self-consistently (B2 4-mode subspace)
- Thouless M_max computed (B2-only and 8x8 full)

GCM kernels: Gaussian Overlap Approximation (GOA) with midpoint Hamiltonian prescription (Ring & Schuck eq 11.57). Hill-Wheeler equation solved via N^{-1/2} transformation with regularization threshold 1e-6.

**2. Key numbers**

| Quantity | Value | Note |
|:---------|:------|:-----|
| M_max(GCM, B2 eff, SC sigma) | **0.646** | Self-consistent sigma = 0.219 |
| M_max(GCM, 8x8 eff, SC sigma) | 0.942 | MARGINAL |
| M_max(GCM, B2 eff, sigma=0.015) | 0.842 | Pairing-width sigma |
| M_max(GCM, 8x8 eff, sigma=0.015) | 1.134 | PASS for 8x8 |
| M_max(GCM, B2 eff, sigma=0.0075) | 0.952 | Narrowest sigma |
| M_max(GCM, 8x8 eff, sigma=0.0075) | 1.248 | PASS for 8x8 |
| M_max at fold (B2, fine grid) | 1.353 | Confirms MMAX-AUTH-36 |
| M_max at fold (8x8, fine grid) | 1.675 | Confirms MMAX-AUTH-36 |
| alpha(B2, SC) | 0.478 | Self-consistency correction |
| alpha(8x8, SC) | 0.563 | Less severe for 8x8 |
| E_GCM_corr (SC sigma) | -3802 | GOA pathology at large sigma |
| E_BCS at fold | -0.156 | BCS pocket depth |
| S(fold) - S(0) | +0.374 | Spectral action gradient |
| E_total(fold) - E_total(0) | +0.218 | Fold is NOT global minimum |
| B2 pairing window | [0.175, 0.205] | Width 0.030 in tau |
| 8x8 pairing window | [0.160, 0.500] | Width 0.340 in tau |
| Constrained GCM M_max_eff(B2) | 0.994 | Pairing region only, 26 points |
| Constrained GCM M_max_eff(8x8) | 1.292 | Pairing region only |
| p(M_max(SC)>1 \| B2 conservative) | 0.004 | Bayesian, sigma_alpha=0.10 |
| p(M_max(SC)>1 \| 8x8 peak) | 0.823 | Bayesian |

**3. The decisive physics: E_total has no minimum at the fold**

The spectral action S(tau) = sum |lambda_k(tau)| is monotonically increasing. The BCS condensation energy E_BCS(tau) creates a pocket of depth -0.156 near tau_fold = 0.190. But S(fold) - S(0) = +0.374. The BCS pocket subtracts only 0.156 from this 0.374 deficit, leaving E_total(fold) 0.218 ABOVE E_total(0). The global minimum of E_total is at tau = 0, where there is no pairing (M_max = 0.43).

The GCM correctly finds that the unconstrained ground state wavefunction delocalizes away from the fold. The self-consistent sigma = 0.219 corresponds to a wavefunction that spans the entire tau range, peaked at the boundaries (tau = 0 and tau = 0.5) rather than at the fold. The effective M_max, averaged over this wavefunction, is 0.646 (B2) -- below threshold.

**4. Two physical scenarios**

- **Scenario A (tau dynamical)**: tau is a quantum-mechanical degree of freedom and the GCM ground state determines the physical state. Result: FAIL. The BCS pocket is too shallow relative to the S-gradient to trap the wavefunction. M_max(GCM, B2) = 0.646.

- **Scenario B (tau externally constrained)**: tau is fixed by the spectral action equations of motion (e.g., cosmic evolution drives tau to the fold, or the FULL spectral action including all KK levels creates a minimum at tau_fold). Result: PASS. M_max = 1.353 (B2) to 1.675 (8x8) at the fold, confirming MMAX-AUTH-36.

The distinction is: does the singlet-sector energy E_total(tau) determine tau, or does the FULL multi-sector spectral action S_full(tau) = 1,034,401 (which is 73,000x larger) determine tau?

Nuclear analog: this is the difference between a nucleus with a soft potential energy surface (GCM wavefunction delocalizes -- shape coexistence/gamma-soft) versus a well-deformed rotor (GCM wavefunction tightly localized at the deformation minimum). The framework is in the "soft" regime for the singlet sector alone, but may be "rigid" when all sectors contribute.

**5. Cross-checks**

1. Fine-grid M_max at fold (1.353 B2, 1.675 8x8) matches MMAX-AUTH-36 to within 0.2% -- consistent interpolation
2. BCS gap at fold: Delta_max = 0.770, E_BCS = -0.156, all converged
3. Pairing window width 0.030 (B2): consistent with van Hove Lorentzian half-width 0.020
4. Constrained GCM (pairing region only): M_max_eff(B2) = 0.994, M_max_eff(8x8) = 1.292 -- confirms that IF confined near fold, pairing survives self-consistency for 8x8
5. E_BCS / (dS * delta_tau) = 1.33: BCS CAN compete locally with the S-gradient but CANNOT overcome the global S(fold)-S(0) deficit
6. GCM correlation energies at small sigma are well-behaved (E_GCM ~ -55 to -79); the large-sigma values (-3802) are GOA pathologies from near-singular norm kernels

**6. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_gcm_self_consistent.py` | Script (530 lines, 10 steps) |
| `tier0-computation/s36_gcm_self_consistent.npz` | Results (14.2 KB) |
| `tier0-computation/s36_gcm_self_consistent.png` | 6-panel plot |

**7. Assessment**

The GCM computation reveals a structural tension in the mechanism chain: the BCS condensation energy at the van Hove fold (-0.156) is insufficient to create a global minimum in the singlet-sector E_total(tau). The spectral action gradient S(fold) - S(0) = +0.374 overwhelms the pairing pocket by 2.4x. Under unconstrained GCM, M_max(B2 eff) = 0.646 -- a FAIL by 35%. However, this conclusion applies ONLY if tau is determined by the singlet sector alone. The full multi-sector spectral action S_full = 1,034,401 dwarfs the singlet contribution S_singlet = 14.27 by a factor of 73,000. Whether the full spectral action has a minimum near the fold is an UNCOMPUTED question that would resolve this gate. The constrained GCM (tau pinned near fold) gives M_max_eff(8x8) = 1.292 (PASS). The mechanism chain fate thus depends on whether S_full(tau) provides external stabilization -- a question the GCM cannot answer from singlet data alone.

---

### W2-C: Edge Mode Winding Number — BDI Z-Invariant (berry)

**Status**: COMPLETE
**Gate**: WIND-36. nu = 0 (trivial) vs nu != 0 (topological, Level 4 candidate).

**Results**:

**Verdict: WIND-36 = nu = 0. BCS condensate is topologically TRIVIAL. No Majorana edge modes at the BCS domain boundary. Level 4 candidate prediction DOES NOT APPLY.**

**1. Key numbers**

| Quantity | Value | Source |
|:---------|:------|:-------|
| BDI winding number nu | **0** (all channels, all gap models) | This computation |
| E_B2_min (band bottom) | 0.8452 | s23a eigenvalues, tau ~ 0.19 |
| Delta_BCS (at gap) | 0.02527 | s35_rg_bcs_flow.npz |
| Ratio E_B2/Delta | **33.4x** | Measures distance from topological transition |
| mu | 0 (forced by PH symmetry) | Session 34 MU-35a |
| mu_c (topological transition) | 0.845 (= E_B2_min) | Requires mu = band bottom |
| min quasiparticle gap | 0.826 | Triplet channel, across all tau |
| Zero-energy spectral flow crossings | 0 | Both singlet and triplet |
| sgn(Pf(C1*D_K)) | -1 at all 34 tau | s35_pfaffian (DIFFERENT invariant) |

**2. Computation method**

The BDI winding number for a 1D topological superconductor is nu = (1/2pi*i) oint d(log det q(k)), where q(k) is the off-diagonal block of the BdG Hamiltonian in the chiral basis. For the B2 sector:

- 4 modes with K_7 charges {-1/4, -1/4, +1/4, +1/4}
- Cooper pairs carry K_7 charge +-1/2 (same-sign pairing)
- Each K_7 charge channel is a 2x2 BdG block
- Singlet: q = xi*I_2 + Delta*i*sigma_y, det(q) = xi^2 + Delta^2 > 0 always
- Triplet: q = xi*I_2 + Delta*sigma_x, det(q) = xi^2 - Delta^2 > 0 since xi >> Delta

Six independent computations (3 gap models x 2 pairing channels) all give nu = 0. Three independent cross-checks (phase winding, spectral flow, boundary formula) all confirm.

**3. Structural analysis (why nu = 0)**

The result is STRUCTURAL, not numerical. It follows from two permanent constraints:
1. **PH symmetry forces mu = 0** (Session 34, proven canonical + grand canonical)
2. **Spectral gap open**: E_B2 > 0 at all tau (minimum 0.845 at fold)

For nu != 0, det(q) must change sign, requiring |xi| = |E_B2 - mu| < Delta somewhere. With mu = 0, this needs Delta > E_B2 = 0.845, but Delta = 0.025 (33x too small). The system sits deep in the trivial phase.

The topological transition would require mu = E_B2_min = 0.845, which violates PH symmetry. This is a WALL: no parameter variation within the framework can reach the topological phase without breaking a structural constraint.

**4. Relation to bare Pfaffian**

The bare Dirac Pfaffian sgn(Pf(C1*D_K)) = -1 is a Z_2 invariant of the NORMAL STATE (unpaired D_K). It reflects nontrivial BDI topology of the Dirac operator itself. However, this is NOT the BCS winding number -- they are different topological invariants on different Hilbert spaces (16-dim D_K vs 8-dim D_BdG). The normal-state topology is a necessary but insufficient condition for topological BCS; one additionally needs mu inside a band (band inversion), which mu = 0 does not provide.

**5. Cross-checks**

1. Phase winding: arg(det q) = 0 throughout (det q real and positive)
2. Spectral flow: 0 zero-energy crossings in BdG spectrum
3. Boundary formula: sgn(det q) identical at both domain boundaries
4. Gap models: step, BCS mean-field, fold-enhanced all give same result
5. Pairing channels: singlet and triplet both give nu = 0
6. Quasiparticle gap: 2*E_qp > 1.69 at all tau (never closes)

**6. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_bdi_winding.py` | Script (500+ lines, 12 steps) |
| `tier0-computation/s36_bdi_winding.npz` | Results (33 arrays) |
| `tier0-computation/s36_bdi_winding.png` | 4-panel plot |

**7. Assessment**

The BCS condensate in the phonon-exflation framework is topologically trivial (nu = 0). The workshop prediction of Majorana-type edge modes at the BCS domain boundary is ruled out: the system is 33x away from the topological transition in the ratio E_B2/Delta. This is a STRUCTURAL closure -- as long as PH symmetry (mu = 0) and the spectral gap (E_B2 > 0) hold, no parameter variation can reach the topological phase. The bare Pfaffian sgn(Pf) = -1 confirms nontrivial normal-state topology, but this does not transmit to the BCS sector because mu = 0 lies below all bands. The Level 4 edge-mode prediction does not apply.

---

### W2-D: Species Scale Computation — W6 Resolution (spectral-geometer)

**Status**: COMPLETE
**Gate**: W6-SPECIES-36. **THIN (PASS)** at both d=4 and d=8 conventions.

**Results**:

**What was computed.** The self-consistent species scale Lambda_species(tau) from the KK spectrum of D_K on Jensen-deformed SU(3). The species scale satisfies Lambda_species = M_P / N_species^{1/(d-2)} where N_species counts KK modes below Lambda_species itself (self-consistency condition). N(Lambda) follows from Weyl's law: N = C_Weyl * (Lambda/M_KK)^8, calibrated from the L_max=6 Dirac spectrum (28 Peter-Weyl sectors, 439,488 modes with multiplicity).

**Self-consistent solution (algebraic).** The self-consistency equation x*M_KK = M_P / (C_Weyl * x^8)^{1/(d-2)}, where x = Lambda_species/M_KK, has the closed-form solution:
- d=4: x = (M_P / (M_KK * sqrt(C_Weyl)))^{1/5}
- d=8: x = (M_P / (M_KK * C_Weyl^{1/6}))^{3/7}

**Key numbers at the fold (tau = 0.190):**

| Quantity | d=4 (standard Swampland) | d=8 (synthesis convention) |
|:---------|:-------------------------|:---------------------------|
| C_Weyl | 42.80 | 42.80 |
| Lambda_species / M_KK | **2.061** | **8.059** |
| Lambda_species (GeV) | 2.061 x 10^16 | 8.059 x 10^16 |
| N_species (self-consistent) | 1.395 x 10^4 | 7.611 x 10^8 |
| log10(Lambda_species / M_KK) | +0.31 | +0.91 |

**Gate verdict: THIN (PASS) under both conventions.** Lambda_species/M_KK lies in [0.1, 10] for all tau in [0, 0.5] under both d=4 and d=8 species formulas. The W6 wall is resolved: the species scale matches the KK scale to within one order of magnitude.

**Why the synthesis's 10^{48} species count was wrong.** The earlier estimate (synthesis Section III.4) naively counted ALL modes below Lambda_SA ~ 10^22 GeV, giving N ~ C_Weyl * (10^6)^8 ~ 5 x 10^49 and Lambda_sp ~ 10^{-7} GeV (unphysical). This is the wrong computation. The species scale is defined self-consistently: you count modes below Lambda_species, not below Lambda_SA. The self-consistent solution gives N ~ 10^4 (d=4) or N ~ 10^9 (d=8), both yielding Lambda_species ~ few x M_KK.

**Convergence check (L_max dependence).** At tau=0.20:

| L_max | N_total | C_Weyl | x(d=4) | x(d=8) |
|:------|:--------|:-------|:-------|:-------|
| 2 | 2,480 | 34.66 | 2.105 | 8.181 |
| 4 | 50,176 | 38.63 | 2.083 | 8.118 |
| 6 | 439,488 | 39.95 | 2.076 | 8.098 |

C_Weyl converges to within 3% between L_max=4 and L_max=6. The species scale ratio x is stable to 1% across all L_max >= 3. L_max=10 extrapolation is unnecessary: the result has already converged.

**Weyl law cross-check.** The effective dimension d_eff = d(log N)/d(log Lambda) approaches 8 for Lambda in [2.0, 2.5] at tau=0: d_eff = 8.1, consistent with dim(SU(3)) = 8. The Weyl extrapolation is reliable.

**Tau dependence.** Lambda_species/M_KK increases monotonically with tau (from 1.86 at tau=0 to 2.55 at tau=0.5 for d=4). The species scale sits firmly above M_KK at all tau. The wall is thin everywhere, not just at the fold.

**Scale hierarchy at the fold (tau=0.190):**
M_KK (10^16) < Lambda_sp(d=4) (2 x 10^16) < Lambda_sp(d=8) (8 x 10^16) < M_P (2.4 x 10^18) < Lambda_SA (10^22)

Both species scales sit between M_KK and M_P, exactly where the EFT is valid. The Lambda_SA cutoff lives well above the species scale, but this is expected: Lambda_SA is the spectral action cutoff, not the gravity cutoff.

**Structural interpretation.** The self-consistent species scale is insensitive to the spectral action cutoff Lambda_SA because the solution depends only on the ratio M_P/M_KK and the Weyl coefficient C_Weyl. The 10^6 ratio Lambda_SA/M_KK is physically irrelevant for the species bound -- it enters only if one naively counts all modes below Lambda_SA. The correct self-consistent counting renders W6 a non-wall: the two descriptions (NCG spectral action and KK tower) match at the species scale, which is within one order of magnitude of M_KK.

**Data files produced:**
- `tier0-computation/s36_species_scale.py` (computation script)
- `tier0-computation/s36_species_scale.npz` (all results: tau, C_Weyl, x(d=4,d=8), N_species)
- `tier0-computation/s36_species_scale.png` (4-panel plot: species scale vs tau, N_species vs tau, scale hierarchy, Weyl coefficient)

**Assessment.** The W6 wall identified in Sessions 30-31 and flagged as the framework's most serious tension is resolved by the correct self-consistent species scale computation. The naive species count of 10^{48-50} that produced Lambda_sp ~ 10^{-7} GeV was a methodological error -- it counted modes up to Lambda_SA rather than up to Lambda_species itself. The self-consistent solution gives Lambda_species = 2-8 x M_KK at the fold, firmly in the THIN regime. This removes the last structural wall between the NCG and KK descriptions of the internal space.

---

### W2-E: Multi-Sector ED at N > 5 (quantum-acoustics)

**Status**: COMPLETE
**Gate**: ED-CONV-36. E_cond convergence from N=5 (32 states) to N=8 (256 states).

**Results**:

**Verdict: ED-CONV-36 = ENHANCED. |E_cond(N=8)| = 0.1369 > |E_cond(N=5)| = 0.1151. B3 modes actively enhance pairing. Fractional change 18.9% (within 20% threshold). Gate PASS (strongest category).**

**1. Convergence sequence**

| Config | N_modes | N_states | M_max(MF) | E_cond | Paired | Pair content | Corr_max |
|:-------|:--------|:---------|:----------|:-------|:-------|:-------------|:---------|
| B2-only | 4 | 16 | 1.292 | 0.000 | NO | 0.000 | 0.000 |
| S35 baseline (4B2+1B1) | 5 | 32 | 1.385 | -0.1151 | YES | 1.000 | 0.266 |
| +1 B3 | 6 | 64 | 1.389 | -0.1214 | YES | 1.000 | 0.265 |
| +2 B3 | 7 | 128 | 1.392 | -0.1289 | YES | 1.000 | 0.264 |
| Full (4B2+1B1+3B3) | 8 | 256 | 1.396 | -0.1369 | YES | 1.000 | 0.263 |
| B2+B3 only (no B1) | 7 | 128 | 1.304 | 0.000 | NO | 0.000 | 0.000 |

**2. Step-by-step convergence**

| Step | Delta E_cond | Fractional change | Direction |
|:-----|:-------------|:------------------|:----------|
| 4 -> 5 (add B1) | -0.1151 | -- (from zero) | PAIRING ONSET |
| 5 -> 6 (add B3[0]) | -0.0063 | 5.5% | DEEPER |
| 6 -> 7 (add B3[1]) | -0.0074 | 6.1% | DEEPER |
| 7 -> 8 (add B3[2]) | -0.0080 | 6.2% | DEEPER |
| Total S35 -> Full | -0.0218 | 18.9% | MONOTONIC ENHANCEMENT |

Each B3 mode deepens E_cond by 5.5-6.2% (near-constant per-mode contribution). Convergence is monotonic with no sign change. The total 18.9% change is within the pre-registered 20% threshold and is in the ENHANCEMENT direction.

**3. Critical structural finding: B1 is the pairing catalyst**

B2-only (M_max=1.292>1) gives E_cond=0 (vacuum ground state). B2+B3 without B1 (M_max=1.304>1) also gives E_cond=0. Pairing ONLY occurs when B1 is included, despite V(B1,B1)=0 (Trap 1). B1 acts as a proximity donor: V(B2,B1)=0.080 is the largest off-diagonal coupling in the V matrix. At the pair Hamiltonian level, the B1 mode mediates pair hopping between B2 modes through B1-assisted virtual processes, even though B1 itself carries only 10% of pair occupation.

This resolves why the S34 "rho_B1=1.0" convention underestimated M_max: B1's role is not through its own DOS but through its cross-coupling V(B2,B1) which connects all four B2 modes coherently.

**4. Pair-pair correlator structure**

The off-diagonal pair-pair correlator <b_n^dag b_m> is stable across all configurations:
- B2-B2 block: 0.18-0.27 (strong coherent hopping, dominant)
- B2-B3 block: 0.023-0.032 (weak but nonzero cross-branch coherence)
- B3-B3 block: 0.003-0.004 (minimal intra-B3 pairing)

The correlator maximum decreases monotonically from 0.266 to 0.263 as B3 modes are added -- a 1.0% reduction indicating the pairing REDISTRIBUTES slightly across more modes but does not weaken.

**5. Number sector analysis**

At all paired configurations, the ground state lives ENTIRELY in the N_pair=1 sector (probability = 1.000000 to machine precision). Higher pair sectors contribute at < 10^{-30}. This is a single delocalized Cooper pair shared across all available modes, consistent with the BCS-BEC crossover picture at discrete N_eff.

**6. Cross-checks**

1. S35 reproduction: E_cond = -0.1150766072 matches stored value to 0.00e+00 (exact)
2. V matrix: all elements match S35 stored V_5x5_bare to machine precision
3. E_vec: eigenvalues match to machine precision
4. Selection rules verified: V(B1,B1) = 3.4e-29, V(B1,B3) = 5.8e-30 (both machine zero)
5. Hermiticity: H = 0.5*(H+H^T) enforced; all eigenvalues real
6. Number conservation: |<b_m>| = 0 for all m at all N (expected for number-conserving ED)

**7. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_multisector_ed.py` | Script (470 lines, 6 configurations) |
| `tier0-computation/s36_multisector_ed.npz` | Results (24.5 KB, all configs stored) |
| `tier0-computation/s36_multisector_ed.png` | 6-panel convergence plot |

**8. Assessment**

The ED pairing survives enlargement to the full positive-sector Hilbert space (8 modes, 256 states) and is ENHANCED by B3 modes, not screened. Each B3 mode contributes a near-constant -0.006 to -0.008 deepening of E_cond, consistent with additional virtual pair-scattering channels opening through V(B2,B3) cross-coupling. The critical structural insight is that B1 is the pairing catalyst: despite V(B1,B1)=0, its large V(B2,B1)=0.080 coupling mediates coherent pair hopping across all four B2 modes. Without B1, even M_max>1 does not produce pairing at this discrete N_eff. The monotonic enhancement with B3 inclusion means the S35 result was a LOWER BOUND on |E_cond|, and the full-sector treatment strengthens the BCS mechanism.

---

### W2-F: BBN Lithium Prediction — delta_H/H at T_BBN (feynman)

**Status**: COMPLETE
**Gate**: BBN-LITHIUM-36. **FAIL (NEGLIGIBLE)**. delta_H/H = -6.6 x 10^{-5}, which is 500x below the minimum threshold of -0.03.

**Results**:

**Verdict: BBN-LITHIUM-36 = FAIL_NEGLIGIBLE. The BCS gap produces a negligible modification to the spectral action coefficients. delta_H/H = -6.58 x 10^{-5}, far below the [-0.15, -0.03] lithium window.**

**1. Method**

Computed the spectral action change from D_K to D_BdG at the fold point tau = 0.190 (interpolated between tau = 0.15 and tau = 0.20 from the eigenvalue grid). The BdG operator D_BdG = [[D_K, Delta], [Delta^dag, -D_K*]] has eigenvalues +/- sqrt(lambda_k^2 + Delta^2) for each D_K eigenvalue lambda_k. The heat kernel factorizes exactly:

K_BdG(t) = 2 * exp(-t * Delta^2) * K_DK(t)

yielding the exact relations:
- a_0(BdG) = 2 * a_0(DK) [Nambu doubling, bookkeeping only]
- a_2(BdG) = 2 * a_2(DK) - 2 * Delta^2 * a_0(DK) [physical shift]

The definitive result uses direct spectral sums S_n = sum_k |lambda_k|^{2n} (Method D), which are exact for the finite spectrum and bypass heat-kernel fitting uncertainties.

**2. Key numbers**

| Quantity | Value | Source |
|:---------|:------|:-------|
| tau (interpolated) | 0.190 | Bracket: 0.15 and 0.20 |
| Delta/W | 0.29 | RG-BCS-35 |
| Delta (spectrum units) | 0.01680 | 0.29 x W_B2 |
| lambda_min | 0.8191 | D_K spectral gap at tau=0.20 |
| Delta/lambda_min | 0.0205 | BCS gap is 2% of spectral gap |
| N_full (modes with mult.) | 439,488 | max_pq_sum = 6, 28 sectors |
| delta_S1/S1 (a_2 proxy) | +1.305 x 10^{-4} | Direct spectral sum |
| delta_G/G | -1.305 x 10^{-4} | -delta_S1/S1 |
| delta_H/H (tau=0.15) | -6.81 x 10^{-5} | Direct computation |
| delta_H/H (tau=0.20) | -6.52 x 10^{-5} | Direct computation |
| delta_H/H (tau=0.190, interp.) | **-6.58 x 10^{-5}** | Linear interpolation |
| Required for Li-7 | [-0.15, -0.03] | Pre-registered gate |
| Shortfall factor | ~500x | |delta_H/H| / 0.03 = 0.002 |

**3. Structural reason for negligibility**

The BCS gap (Delta ~ 0.017) is a perturbation of order Delta^2/lambda^2 ~ 4 x 10^{-4} on each mode. The spectral action sums S_n = sum |lambda_k|^{2n} are UV-dominated: modes at the gap edge (61 modes within W_B2 of lambda_min) carry negligible spectral weight compared to the 439,488-mode UV tower. The fractional shift scales as Delta^2 * <lambda^4> / <lambda^6> ~ Delta^2 / lambda_typ^2 ~ 5 x 10^{-5}. No choice of Delta/W within the physical range [0, 0.50] can overcome this: even at Delta/W = 0.50, delta_H/H = -1.9 x 10^{-4}, still 150x below threshold.

This is the same structural conclusion recorded in Session 35: "delta-a_4 from BdG gap is ~10^{-7} (negligible). BCS role is tau-pinning, not spectral shift." The present computation extends this to a_0 and a_2 with the same result.

**4. g_* counting at BBN**

The BCS condensate does not change the effective number of relativistic species g_*(T_BBN). The physical gap scale Delta_phys ~ Delta x M_KK ~ 0.017 x 10^{10} ~ 10^8 GeV is 10^{11} times above T_BBN ~ 1 MeV. All KK modes (gapped and ungapped) are frozen out at BBN temperatures. The g_* counting is unaffected.

**5. Cross-checks**

1. Heat kernel factorization K_BdG = 2*exp(-t*Delta^2)*K_DK verified to machine precision (relative error < 2.1 x 10^{-16}) at 5 test values of t.
2. Independent polynomial fit of K_BdG(t) reproduces the analytic a_0(BdG), a_2(BdG) to 3.5 x 10^{-5} relative error.
3. Leading-order expansion delta_S1 ~ 3*Delta^2*S2 agrees with exact delta_S1 to 0.005%.
4. Tau bracketing: delta_H/H varies by only 4% between tau = 0.15 and tau = 0.20. The result is insensitive to the exact fold location.
5. Sensitivity scan: delta_H/H stays in the range [-2 x 10^{-4}, 0] for all Delta/W in [0, 0.50].

**6. Level 4 assessment**

NOT Level 4. The spectral action change from BCS is structurally negligible (UV dominance of spectral sums). The BCS condensate's role in the framework is tau-pinning (selecting the fold point), not modifying gravitational couplings at BBN. Lithium-7 resolution would require a separate mechanism: modified tau(t) trajectory, domain wall energy density at BBN, or new physics beyond the internal spectral action. Any such mechanism would require additional free parameters (wall density, nucleation rate), precluding Level 4 status.

**7. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_bbn_lithium.py` | Script (14 steps, 280 lines) |
| `tier0-computation/s36_bbn_lithium.npz` | Full results: spectral sums, heat kernel coefficients, sensitivity scan |

**8. Assessment**

The BBN lithium gate is definitively FAIL. The BCS gap modifies the spectral action at the 10^{-4} level, producing delta_H/H ~ -7 x 10^{-5} -- three orders of magnitude below the lithium resolution window. This is not a fine-tuning failure but a structural one: the spectral action is UV-dominated (Weyl's law), and the BCS gap is a low-energy perturbation that touches a negligible fraction (0.014%) of the spectral weight. The result is robust against tau uncertainty, gap magnitude, and fitting method. The BCS mechanism's physical role is tau-pinning, not gravitational coupling modification.

---

# Wave 3: Dependent Computations

---

### W3-A: Bayesian Self-Consistency Posterior (sagan)

**Status**: COMPLETE
**Gate**: BAYES-SC-36. p(M_max(SC) > 1) under three scenarios. Revised Sagan probability.

**Results**:

**Verdict: BAYES-SC-36 = ASSESSMENT COMPLETE. Session 36 is a MIXED session (6 PASS, 4 FAIL, net BF ~ 1.20). Mechanism chain status downgraded from UNCONDITIONAL to CONDITIONAL on tau stabilization. Revised Sagan probability: 28% (14-40%).**

**1. Bayesian Posteriors for M_max(SC) > 1**

Three scenarios, all using alpha ~ N(mu, sigma=0.10) where alpha = M_max(SC)/M_max(MF):

| Scenario | alpha | M_MF | p(>1.0) | p(>1.2) | 90% CI for M_max(SC) |
|:---------|:------|:-----|:--------|:--------|:---------------------|
| A: Unconstrained (B2) | 0.478 | 1.351 | 0.44% | 0.002% | [0.42, 0.87] |
| B: Constrained (B2 internal) | 0.736 | 1.351 | 48.2% | 6.4% | [0.77, 1.22] |
| C: Constrained (8x8 full) | 0.772 | 1.674 | 95.9% | 70.9% | [1.02, 1.57] |

Under unconstrained GCM (Scenario A), M_max(SC) > 1 is excluded at 99.6% confidence. Under constrained 8x8 (Scenario C), it is supported at 95.9% confidence. The outcome depends entirely on tau stabilization.

**2. Scenario Weights**

P(constrained) = 0.25 (range: 0.15-0.40). P(unconstrained) = 0.75.

Reasoning: The direct GCM computation shows E_total has no minimum at the fold. The Perturbative Exhaustion Theorem (Session 22c) closes all smooth spectral action potentials. Eight cutoff functions tested in Session 25 all yield monotonic S(tau). Weyl's law makes S_full UV-dominated, and the fold is an IR feature. Against this: S_full(tau) at the fold is genuinely UNCOMPUTED (73,000x the singlet contribution), non-perturbative effects lie outside PET scope, and the fold is a geometric feature all sectors feel. I weight 75% to the computation + structural theorems, 25% to the uncomputed multi-sector possibility.

**3. Marginal Posterior**

p(M_max(SC) > 1.0) = P(cnstr) x p_C + P(uncnstr) x p_A = 0.25 x 0.960 + 0.75 x 0.004 = **24.3%** (range: 14.7%-38.8%)

p(M_max(SC) > 1.2) = 0.25 x 0.709 + 0.75 x 0.00002 = **17.7%**

The mechanism chain is no longer unconditional. Its viability is a ~24% proposition.

Sensitivity to sigma_alpha (the uncertainty on alpha):

| sigma_alpha | p_A (uncnstr) | p_C (cnstr) | p_marginal |
|:------------|:--------------|:------------|:-----------|
| 0.05 | 0.000% | 99.98% | 25.0% |
| 0.10 | 0.44% | 95.95% | 24.3% |
| 0.15 | 4.04% | 87.76% | 25.0% |
| 0.20 | 9.52% | 80.84% | 27.4% |

The marginal is INSENSITIVE to sigma_alpha because the scenarios are well-separated. The dominant uncertainty is P(constrained), not the width of the alpha distribution.

**4. Session 36 Gate Bayes Factors**

| Gate | Verdict | BF | Rationale |
|:-----|:--------|:---|:----------|
| MMAX-AUTH-36 | PASS | 1.10 | Confirms S35, resolves M_max ambiguity |
| GL-CUBIC-36 | PASS | 1.20 | Second order, perturbative SC |
| COLL-36 | PASS | 1.20 | Vibrational 12.1 W.u., multi-mode coherence |
| ANOM-KK-36 | PASS | 1.35 | 150/150 anomaly coefficients = 0 |
| W6-SPECIES-36 | PASS | 2.00 | W6 wall RESOLVED, largest structural concern removed |
| ED-CONV-36 | PASS | 1.50 | ED ENHANCED 18.9%, B1 catalyst confirmed |
| PMNS-36 | FAIL | 0.60 | All 3 PMNS routes CLOSED on Jensen |
| SC-HFB-36 | FAIL | 0.50 | Unconstrained M_max=0.65 < 1; chain conditional |
| WIND-36 | FAIL | 0.90 | nu=0, topologically trivial |
| BBN-LITHIUM-36 | FAIL | 0.90 | 500x below lithium threshold |

Correlation-corrected net BF: 1.20 (range: 0.36-3.48). Product with correlation groups: fold-related passes (1.32), structural passes (2.70), ED (1.38), major failures (0.30), minor failures (0.81).

**5. Revised Sagan Probability**

BF computation gives 36% from 32% prior. However, after reflection, I apply a QUALITATIVE DOWNWARD ADJUSTMENT of -8 percentage points for the mechanism chain's status change from unconditional to conditional.

Rationale: The BF of 0.50 for SC-HFB captures the direct computation's failure but does not fully encode the STRUCTURAL change from "chain 5/5 unconditional" (S35 claim) to "chain conditional on unverified hypothesis." At Session 35, the chain's unconditional status was the single strongest argument for the framework. Losing it is not merely one gate failing -- it retroactively weakens the evidential force of all prior chain gates (RPA, Turing, WALL, BCS) because they were all evaluated under the assumption that tau is at the fold. A BF of 0.50 is adequate for a single gate failure but underestimates the cascading effect on the entire chain's credibility.

**REVISED SAGAN PROBABILITY: 28% (14-40%)**

| Checkpoint | Probability | BF | Gate |
|:-----------|:------------|:---|:-----|
| Post-S35 (prior) | 32% (18-45%) | -- | -- |
| S36 BF computation | 36% | 1.20 | All 10 gates |
| Qualitative adjustment | -8pp | -- | Chain status: unconditional -> conditional |
| **Post-S36** | **28% (14-40%)** | **net ~0.82** | -- |

Change from S35: -4 percentage points. Direction: DOWNWARD.

**6. Assessment (5 sentences)**

Session 36 is the most comprehensive single-session computation in the project (11 gates, 12 agents, 2 waves of parallel computation). The results are genuinely mixed: six structural/consistency gates PASS (W6 species scale resolved, anomaly-free KK tower, vibrational collectivity, second-order transition, ED convergence enhanced, M_max authoritative confirmed), while four gates FAIL (PMNS mixing identically zero on Jensen, unconstrained GCM self-consistency below threshold, winding number trivial, BBN lithium negligible). The decisive finding is the SC-HFB fork: the BCS mechanism chain, which was "5/5 unconditional" at mean-field level after Session 35, is now CONDITIONAL on tau stabilization by the full multi-sector spectral action -- an uncomputed quantity 73,000x larger than the singlet contribution. The W6 resolution (Lambda_species/M_KK = 2.06) is the session's most significant positive result, removing the framework's largest structural concern by correcting a methodological error in the species count. The framework remains at Evidence Level 3 (internal quantitative predictions) with no Level 4 predictions achieved; its fate hinges on whether S_full(tau) has a minimum near the Jensen fold -- a computation that should be the highest priority for Session 37.

**7. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_bayesian_posterior.py` | Script (11 steps, ~350 lines) |
| `tier0-computation/s36_bayesian_posterior.npz` | All results: posteriors, BFs, scenario weights, sensitivity |

---

### W3-B: PMNS Path Forward Decision (gen-physicist)

**Status**: COMPLETE
**Gate**: PMNS-PATH-36. Verdict: **LEVEL 5 (CONDITIONAL ON K7-G1-37)**. Mass hierarchy and normal ordering survive as zero-parameter predictions. Mixing angles require Step 3 (SU(2)-breaking) extension. Pre-registered two-stage gate for Session 37.

**Results**:

**Verdict: PMNS-PATH-36 = LEVEL 5 (conditional)**. The Jensen curve produces zero PMNS mixing (structural, Schur's lemma on U(2) irreps). The mass hierarchy ratio R = 27.2 at the fold and normal ordering (B1 < B2 < B3) survive as zero-parameter predictions. Mixing angles require breaking SU(2) within U(2), which is Baptista's Step 3 (Paper 18, Appendix E, p.54). The decisive next test is K7-G1-37 (K_7 charge of G1 in the (1,0) sector).

**1. Complete Closure Inventory (5 routes closed)**

| Route | Session | Closure Mechanism |
|:------|:--------|:------------------|
| Singlet tridiagonal PMNS | S35 | R < 5.9 ceiling from dE_23/dE_12 = 5.09 (Schur on U(2) irreps) |
| NCG inner fluctuation cross-sector | S36 W2-A P1 | Cross-sector norm = 0.00e+00 (phi = Id_geom x phi_F, tensor product) |
| H_eff structural bound | S36 W2-A P2 | max R * sin^2(theta_23) = 16.9 at tau = 0.30, need 17.8. 0/600,000 MC passes |
| Paper 18 Phi-tilde misalignment | S36 W2-A P3 | O_matrix = I at all 6 tau. sin^2(theta) < 10^{-17}. Schur locks U(2) irreps |
| Off-Jensen within U(2)-invariant family | This analysis | Schur still applies for ANY (lambda_1, lambda_2, lambda_3). U(2)-invariant metrics change eigenvalue POSITIONS but not eigenspace STRUCTURE |

All five closures are STRUCTURAL (representation-theoretic), not numerical. They survive at any tau, any U(2)-invariant metric, and any coupling strength.

**2. Surviving Structural Resources**

The W2-A computation confirms that while mixing angles are zero, the mass hierarchy is structurally available:

| tau | R_bare | B2-G1 gap | Normal ordering |
|:----|:-------|:----------|:----------------|
| 0.12 | 6.6 | 0.0127 | B1=0.829 < B2=0.848 < B3=0.927 |
| 0.15 | 11.2 | 0.0094 | B1=0.824 < B2=0.846 < B3=0.945 |
| 0.18 | 18.9 | 0.0068 | B1=0.821 < B2=0.845 < B3=0.965 |
| 0.20 | 27.2 | 0.0053 | B1=0.819 < B2=0.845 < B3=0.978 |
| 0.24 | 59.8 | 0.0029 | B1=0.818 < B2=0.847 < B3=1.007 |
| 0.30 | 336.0 | 0.0007 | B1=0.822 < B2=0.852 < B3=1.053 |

R_bare reaches the gate window [10, 100] for tau >= 0.15. Normal ordering (B1 < B2 < B3) holds at ALL tau > 0, protected by Schur's lemma. The B2-G1 inter-sector gap shrinks monotonically, providing a tunable mass hierarchy ratio in the inter-sector channel.

**3. Assessment of Surviving Options**

**Option A: Off-Jensen SU(2)-Breaking (Paper 18, Step 3)**

The metric parameter space on SU(3) is stratified by isometry group:

```
bi-invariant [Iso = (SU(3) x SU(3))/Z3, 0 parameters]
    |
    | Jensen deformation (Paper 15, eq 3.68)
    v
Jensen curve [Iso = (SU(3) x U(2))/Z3 = G_SM, 1 parameter s]
    |
    | Off-Jensen within U(2)-invariant (Paper 15, eq 3.60)
    v
U(2)-invariant family [Iso = G_SM, 2 parameters (vol.-preserving)]
    |
    | SU(2)-breaking (Paper 15, ref [71]; Paper 18, Step 3)
    v
SU(3) x U(1) metrics [Iso = SU(3) x U(1)_7, >= 4 parameters]
```

Framework status: **WITHIN the framework**. Paper 18, Appendix E, p.54 explicitly calls for "a perturbed left-invariant metric that breaks the isometry group from G_SM to SU(3) x U(1)" as Step 3 of the PMNS computation program. This is not a post-hoc rescue; Baptista identified this step before our computation confirmed Step 2 gives zero mixing.

Physical mechanism: SU(2)-breaking corresponds to the second stage of symmetry breaking in the KK picture. Baptista argues (Paper 18, p.53-54) this arises from higher-order corrections to the Einstein-Hilbert action that stabilize the unraveling internal metric. These corrections break G_SM -> SU(3) x U(1) at the electroweak scale, producing light gauge bosons and non-degenerate fermion masses.

Quantum number analysis after SU(2) -> U(1)_3:

| Mode | q_7 | q_3 | dim | Mixes with |
|:-----|:----|:----|:----|:-----------|
| B1 | 0 | 0 | 1 | B3_0 only |
| B2++ | +1/4 | +1/2 | 1 | B2-+ only |
| B2+- | +1/4 | -1/2 | 1 | B2-- only |
| B2-+ | -1/4 | +1/2 | 1 | B2++ only |
| B2-- | -1/4 | -1/2 | 1 | B2+- only |
| B3_0 | 0 | 0 | 1 | B1 only |
| B3_+ | 0 | +1 | 1 | none in singlet |
| B3_- | 0 | -1 | 1 | none in singlet |

The permanent constraint [iK_7, D_K] = 0 (Session 34) makes q_7 an exact quantum number at ALL tau and for ANY left-invariant metric. This blocks B1-B2 mixing (q_7 = 0 vs +/-1/4). Within the singlet (0,0) sector, only B1 and B3_0 share quantum numbers (q_7 = 0, q_3 = 0) after SU(2) breaking, producing a 2x2 rotation -- NOT a full 3x3 PMNS.

Full 3x3 PMNS requires an inter-sector mode with q_7 = 0. The G1 mode in the (1,0) sector is the candidate. Its K_7 charge is UNCOMPUTED but structurally constrained: K_7 is a right-invariant operator, Peter-Weyl labels are left-regular, and left/right commute. Therefore every Peter-Weyl sector has modes with q_7 = 0 (B1-type and B3-type spinor structure) and modes with q_7 = +/-1/4 (B2-type). The G1 mode (lowest eigenvalue in (1,0), multiplicity 1 in positive spectrum) has degeneracy consistent with B1-type (q_7 = 0), but this is not proven.

Test: K7-G1-37 -- compute the matrix element of K_7 in the G1 eigenstate of D_K on the (1,0) sector.

**Option B: Full KK Modified Lie Derivative Coupling**

Framework status: **EXTENSION**. The modified Lie derivative tilde{L}_{e_a} (Paper 18, eq 1.4) generically mixes Peter-Weyl sectors when e_a is not Killing. However, W2-A Part 1 proved that NCG inner fluctuations phi = sum_i a_i [D, b_i] preserve sectors identically (tensor product structure). These are categorically different mathematical objects. The framework as currently formulated (NCG spectral action on almost-commutative geometry M^4 x F) uses inner fluctuations, not KK Lie derivatives. Importing KK coupling into the NCG framework requires replacing the algebraic inner fluctuation with a geometric gauge coupling, which is a framework change, not an internal computation.

Assessment: Viable in principle but deferred. The NCG-KK dichotomy (W2-A Theorem, Session 35 neutrino-baptista workshop B1) is a structural result that cannot be bypassed within the current spectral triple formalism.

**Option C: Classify PMNS as Level 5 (Requires New Input)**

What the framework predicts with zero free parameters:
1. Normal mass ordering B1 < B2 < B3 (structural, all tau > 0, testable by JUNO/DUNE)
2. Mass hierarchy scale R ~ 27 at fold (in gate window [10, 100])
3. Three generations from Z_3 center of right SU(3) (Paper 18, p.54)

What requires Step 3 input (at least one free parameter epsilon):
1. PMNS mixing angles theta_12, theta_13, theta_23
2. CP-violating phase delta_CP
3. Absolute neutrino masses (requires M_KK stabilization)

This is analogous to LCDM predicting the expansion history but not the primordial perturbation spectrum without inflation as input. The framework's structural content (mass hierarchy, ordering, generation count) is non-trivial. The mixing angles are determined by the electroweak-scale symmetry breaking of the internal metric, which introduces the SU(2)-breaking parameter.

**4. Pre-Registered Gates for Session 37**

**Stage 1: K7-G1-37** (zero-cost, prerequisite for Stage 2)

Compute: K_7 eigenvalue of the G1 mode in the (1,0) sector of D_K at tau = 0.20.

Method: Construct K_7 = (1/8) sum_{r,s} A^7_{rs} gamma_r gamma_s in the (1,0) Peter-Weyl sector (48 x 48 matrix). Diagonalize. Identify the G1 eigenstate (lowest |eigenvalue| of D_K in (1,0)). Compute q_7(G1) = expectation value of K_7 in this eigenstate.

Pass/Fail:
- q_7(G1) = 0 (to machine epsilon): PROCEED to Stage 2
- q_7(G1) = +/-1/4: FALL BACK to Option C

**Stage 2: OFF-JENSEN-PMNS-37** (medium-cost, conditional on Stage 1 PASS)

Compute: Dirac spectrum on SU(3) with SU(2)-broken metric (Paper 15, ref [71]) at tau = 0.20, epsilon in [0.01, 0.10]. Extract 3x3 PMNS matrix from (B1, B3_0, G1) triad.

Method: Modify the metric g_hat (Paper 15, eq 3.60) to break SU(2): set lambda_2 -> (lambda_2 + epsilon, lambda_2 - epsilon/2, lambda_2 - epsilon/2) for the three su(2) generators. Diagonalize the 64 x 64 matrix D_K on (0,0) + (1,0) sectors. Extract eigenvalue ratios and mixing angles from the 3 lowest q_7 = 0 modes.

Pass/Fail:
- PASS: R in [10, 100] AND sin^2(theta_23) in [0.3, 0.7] AND sin^2(theta_13) in [0.005, 0.05]
- FAIL: R < 5 OR sin^2(theta_23) < 0.01

**5. Impact on Framework Probability**

The PMNS closure on the Jensen curve exerts MILD downward pressure (BF ~ 0.85):

Mitigating factors:
- Paper 18, Appendix E explicitly requires Step 3 for mixing. Our W2-A confirms Step 2 (= Jensen) gives zero mixing. This is CONSISTENT with Baptista's published program, not a failure.
- Mass hierarchy IS structurally predicted (R = 27.2 at fold).
- Normal ordering IS a zero-parameter Level 4 candidate prediction.
- Three-generation structure from Z_3 center survives.

Aggravating factors:
- The framework does not autonomously predict PMNS angles without Step 3.
- Step 3 introduces at least one free parameter (epsilon).
- The NCG-KK dichotomy raises questions about which formalism applies.

The decisive future test is OFF-JENSEN-PMNS-37. If it produces PMNS angles consistent with data from a 1-parameter SU(2)-breaking deformation, the Bayes factor would be ~ 3-5 upward (actual mixing angle prediction from geometry). If it fails, BF ~ 0.5 downward (framework structurally cannot produce PMNS).

**6. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_intersector_pmns.npz` | W2-A input data (3-part closure) |
| `tier0-computation/s36_pmns_path_analysis.py` | This analysis script (190 lines) |
| `tier0-computation/s35_k7_thouless.npz` | K_7 charge data for singlet sector |
| `tier0-computation/s35_sector_10_spectrum.npz` | (1,0) sector eigenvalue data |

**7. Assessment**

The PMNS problem on the Jensen curve is comprehensively closed by five independent structural arguments, all rooted in Schur's lemma for U(2) irreducible representations. The framework's mass hierarchy and normal ordering predictions survive untouched. The path forward is Baptista's Step 3: break SU(2) within U(2) to produce non-trivial mixing between the q_7 = 0 modes. This is a well-defined computation within the published KK framework, requiring diagonalization of D_K with an SU(2)-broken metric. The prerequisite check is K7-G1-37: the K_7 charge of the G1 mode in the (1,0) sector determines whether a full 3x3 PMNS triad exists. If q_7(G1) = 0, the Off-Jensen PMNS computation is the single most important open gate in the framework. If q_7(G1) != 0, PMNS mixing is classified as Level 5 (requires input beyond the current geometric structure).

---

### W4-A: Multi-Sector S_full Landscape (baptista)

**Status**: COMPLETE
**Gate**: TAU-STAB-36 — S_full(tau) monotonicity establishes the STATIC needle hole.

**1. What was computed**

S_full(tau) = sum_{(p,q)} dim(p,q)^2 * S_{(p,q)}(tau), where S_{(p,q)}(tau) = sum_k |lambda_k^{(p,q)}(tau)| is the spectral action on Peter-Weyl sector (p,q) and dim(p,q)^2 is the multiplicity. Computed for 11 sectors through KK level 3 on a 16-point tau grid combining existing s27 data (9 points: 0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50) with 7 fresh eigenvalue computations at tau = 0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22.

**2. Key numbers**

| tau | S_full | dS/dtau (spline) | d2S/dtau2 |
|:---:|:------:|:----------------:|:---------:|
| 0.000 | 244,839 | 3.55 | — |
| 0.100 | 246,355 | — | — |
| 0.150 | 248,267 | 46,039 | 313,800 |
| 0.190 | 250,361 | 58,673 | 317,862 |
| 0.200 | 250,963 | 61,856 | 318,879 |
| 0.300 | 258,761 | — | — |
| 0.500 | 284,364 | — | — |

- dS_full/dtau > 0 at ALL tau. Minimum |dS/dtau| = 3.55 at tau = 0.000.
- d2S/dtau2 > 0 everywhere (convex, accelerating). The function curves AWAY from any minimum.
- All 10 individual sectors are separately monotonically increasing.

**3. Per-level contribution at fold (tau = 0.190)**

| Level | Sectors | S_level | Fraction | dS_level/dtau |
|:-----:|:--------|:-------:|:--------:|:-------------:|
| 0 | (0,0) | 14.2 | 0.006% | 3.9 |
| 1 | (1,0), (0,1) | 962.0 | 0.384% | 243.2 |
| 2 | (1,1), (2,0), (0,2) | 20,620.5 | 8.24% | 4,959.7 |
| 3 | (3,0), (0,3), (2,1), (1,2) | 228,763.9 | 91.37% | 53,466.0 |

Level 3 dominates (91.4% of S_full, 91.1% of the gradient). Growth ratios: L3/L2 = 11.1, L2/L1 = 21.4. Higher KK levels would add MORE monotonically increasing contributions, strengthening the monotonicity result.

**4. Cross-checks**

- Each sector verified anti-Hermitian (D + D^dag < 1e-12) at all 7 new tau values.
- Connection metric compatibility error: 0.00e+00 at all tau.
- Conjugate sectors (p,q) and (q,p) verified to have identical spectral actions.
- Cubic spline interpolation on 16-point grid; no sign change in dS/dtau on 5000-point fine grid.
- Individual sector monotonicity: min dS_{(0,0)}/dtau = 0.026 (smallest), all positive.

**5. Structural argument**

S_{(p,q)}(tau) = sum_k |lambda_k| is a sum of absolute eigenvalues of D_K on the sector. As tau increases from 0, the Jensen deformation breaks SU(3) bi-invariance: coset directions expand (L3 = e^tau), SU(2) contracts (L2 = e^{-2tau}), U(1) expands (L1 = e^{2tau}). The spectral spreading is asymmetric and UV-dominated: higher eigenvalues grow faster than lower ones shrink. The sum of absolute eigenvalues is controlled by Weyl's law (average |lambda| grows with the Casimir of the sector), ensuring monotonic increase in every sector. Since every sector is individually monotonic, no cancellation between sectors can produce a minimum.

**6. Gate verdict**

**TAU-STAB-36: FAIL**

- S_full(tau) is monotonically increasing on [0, 0.5]. No minimum exists.
- At the fold tau = 0.190: dS_full/dtau = +58,673, d2S/dtau2 = +317,862.
- The BCS condensation energy E_BCS = -0.156 (from SC-HFB-36) cannot overcome dS_full/dtau = +58,673.
- The mechanism chain is BROKEN at self-consistent level.
- The constrained GCM regime (M_max = 1.292) is invalid because there is no external stabilization of tau near the fold.

**7. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_sfull_tau_stabilization.py` | Computation script (400 lines) |
| `tier0-computation/s36_sfull_tau_stabilization.npz` | All S_full data, per-sector, per-level, eigenvalues |
| `tier0-computation/s36_sfull_tau_stabilization.png` | 4-panel plot (S_full, derivative, stacked levels, normalized sectors) |

**8. Assessment**

The spectral action S_full(tau) is monotonically increasing across all tau in [0, 0.5], with all 10 individual Peter-Weyl sectors (through KK level 3) separately monotonic. The gradient at the fold is 58,673 — roughly 376,000 times the BCS condensation energy of -0.156. Higher KK levels would only increase both the value and the gradient. This closes the "constrained regime" of SC-HFB-36: there is no external tau stabilization from the spectral action, and the mechanism chain cannot achieve self-consistency. The framework's BCS instability at the van Hove fold is real, but the internal geometry does not cooperate to pin tau at the fold.

---

### W4-B: Tau Dynamics -- Moduli Trajectory Through the Fold (nazarewicz)

**Status**: COMPLETE

**Gate**: TAU-DYN-36

**1. What was computed**

The equation of motion for the Jensen deformation parameter tau(t), treated as a modulus field rolling in the effective potential V_eff(tau) = S_full(tau) from the spectral action. The computation solves:

G_mod * d^2 tau/dt^2 + 3*H*G_mod * dtau/dt + dV_eff/dtau = 0

coupled to the Friedmann equation H^2 = (1/3)*[(1/2)*G_mod*(dtau/dt)^2 + V_eff(tau)], for 9 scenarios (4 initial conditions with S_full, 1 with BCS back-reaction, 4 with S_singlet) and 2 analytical estimates.

The moduli space metric G_mod is computed from the DeWitt supermetric on the space of Jensen left-invariant metrics:

G_mod = (1/4) * sum_I n_I * (d ln g_I / dtau)^2

For the Jensen deformation (lambda_1 = e^{2tau} on U(1), lambda_2 = e^{-2tau} on SU(2) x3, lambda_3 = e^{tau} on coset x4):
- d ln g / dtau = [2, -2, -2, -2, 1, 1, 1, 1]
- Trace = 0 (volume-preserving, confirmed)
- G_mod = (1/4)*[1*4 + 3*4 + 4*1] = 5.0 (CONSTANT, tau-independent)

**2. Key numbers**

| Quantity | S_full | S_singlet | Unit |
|:---------|:------:|:---------:|:----:|
| G_mod | 5.0 | 5.0 | dimensionless |
| V_eff(fold) | 1,032,041 | 14.23 | spectral action |
| dV/dtau(fold) | 233,540 | 3.92 | -- |
| d2V/dtau2(fold) | 1,274,488 | 20.43 | -- |
| H(fold) | 586.5 | 2.18 | -- |
| omega(fold) | 504.9 | 2.02 | -- |
| Damping ratio 3H/(2*omega) | 1.74 | 1.62 | -- (overdamped) |
| v_terminal | -26.5 | -0.120 | -- |
| epsilon(fold) | 0.00512 | 0.00757 | -- |
| eta(fold) | 0.247 | 0.287 | -- |
| t_dwell (numerical, tau0=0.40) | 1.04e-3 | 0.226 | spectral time |
| t_dwell / tau_BCS | 2.59e-5 | 5.65e-3 | -- |
| Shortfall factor (tau_BCS / t_dwell) | 38,600x | 177x | -- |

BCS formation timescale: tau_BCS = 1/Delta_max = 40.0 (from Session 35 BCS data, Delta_max = 0.025).

**3. Dynamics regime**

The system is OVERDAMPED at the fold: 3H/(2*omega) = 1.74. This means tau does not oscillate but rolls monotonically toward tau = 0 with a terminal velocity determined by the balance of Hubble friction and potential gradient:

v_terminal = -V'/(3*H*G_mod) = -233,540/(3 * 586.5 * 5.0) = -26.5

The BCS pairing window [0.175, 0.205] has width 0.030. Transit time: 0.030/26.5 = 1.13e-3. This is 35,400x shorter than tau_BCS = 40.

The slow-roll parameter epsilon = 0.00512 < 1, which nominally qualifies as "slow roll." However, this is MISLEADING: epsilon = (V'/V)^2 / (2*G_mod) is small because V ~ 10^6 is enormous, not because the gradient is gentle. The absolute gradient dV/dtau = 233,540 drives rapid passage through the fold. The relevant diagnostic is the dwell time ratio, not epsilon.

Nuclear analogy: this is like a heavy nucleus passing through a compound-nuclear resonance at high bombarding energy. The level density at the resonance is high (van Hove fold), but the transit time is too short for the compound state to equilibrate. The Ericson fluctuations average out.

**4. BCS back-reaction**

For S_full: NEGLIGIBLE. |E_BCS(fold)|/|dV/dtau| = 6.7e-7. The BCS condensation energy (-0.156) cannot compete with the spectral action gradient (233,540). Dwell time with and without BCS back-reaction: identical to 4 significant figures.

For S_singlet (hypothetical): DETECTABLE but insufficient. With BCS back-reaction, the singlet-only dwell time increases from 0.226 to 3.85 (17x enhancement), reaching dwell/tau_BCS = 0.096. This is because E_BCS ~ -0.156 is ~4% of dV/dtau(singlet) = 3.92, creating a local friction that partially traps the trajectory near the fold. However, even this enhanced dwell is 10.4x too short for BCS condensation.

**5. Initial-condition independence**

For S_full, the dwell time is nearly independent of initial conditions:

| tau_0 | t_dwell | t_dwell/tau_BCS | v at fold |
|:-----:|:-------:|:---------------:|:---------:|
| 0.50 | 1.035e-3 | 2.59e-5 | -29.07 |
| 0.40 | 1.035e-3 | 2.59e-5 | -29.06 |
| 0.25 | 1.065e-3 | 2.66e-5 | -28.30 |
| 0.21 | 1.294e-3 | 3.23e-5 | -24.35 |

This is because the overdamped dynamics quickly reaches terminal velocity. The velocity at the fold is determined by the LOCAL potential gradient and Hubble rate, not by initial conditions. This makes the result ROBUST: no choice of initial tau_0 can change the dwell time by more than ~25%.

**6. Gate verdict**

**TAU-DYN-36: FAST ROLL (FAIL)**

- t_dwell / tau_BCS = 2.59e-5 (primary, S_full, tau_0 = 0.40). FAIL threshold: need > 1.
- Shortfall: 38,600x. The trajectory rushes through the BCS window in ~10^{-3} spectral time units, while BCS condensation requires tau_BCS = 40.
- epsilon(fold) = 0.00512 < 1 (formally slow-roll, but misleading; absolute gradient dominates).
- BCS back-reaction: NEGLIGIBLE for S_full (enhancement 1.0000x). Detectable for S_singlet (17x) but still insufficient.
- Regime: OVERDAMPED (damping ratio 1.74). Terminal velocity |v| ~ 26.5.
- Initial-condition independence: confirmed (spread < 25% across tau_0 in [0.21, 0.50]).

**7. Data files**

| File | Description |
|:-----|:------------|
| `tier0-computation/s36_tau_dynamics.py` | Computation script (460 lines) |
| `tier0-computation/s36_tau_dynamics.npz` | Trajectories, slow-roll params, analytical estimates |
| `tier0-computation/s36_tau_dynamics.png` | 6-panel plot (potential, epsilon, trajectories, dwell, phase space) |

**8. Assessment**

The dynamical trajectory tau(t) passes through the van Hove fold at terminal velocity |v| ~ 26.5, traversing the BCS pairing window in ~10^{-3} spectral time units. BCS condensation requires tau_BCS = 40, yielding a shortfall factor of 38,600. This is INDEPENDENT of initial conditions because the overdamped regime (3H/(2*omega) = 1.74) locks the dynamics to terminal velocity. The BCS back-reaction energy (-0.156) is 6.7e-7 of the spectral action gradient at the fold (233,540) and produces no measurable trapping.

This result is structurally deeper than the static SC-HFB-36 finding (which showed S_full monotonic). Even if tau were somehow brought to the fold, the dynamical passage time is 38,600x too short for condensation. The nuclear analogy is a direct reaction at above-barrier energy: the projectile transits the interaction region before the compound nucleus can form.

The singlet-only case is 177x too slow and represents an unphysical scenario (higher KK sectors cannot be suppressed in the spectral action). The only scenario that approaches condensation is the singlet+BCS case (dwell/tau_BCS = 0.096), which requires both (a) suppressing ~10^6 of spectral action weight from higher sectors and (b) the BCS friction partially trapping the roll. Neither condition is available within the framework as formulated.

---

### The Needle Hole — Quantitative Target for the Cutoff Function

W4-A (static) and W4-B (dynamical) independently constrain the same quantity: how much must the effective spectral action gradient be suppressed for the mechanism chain to function?

| Constraint | Source | Ratio | What it means |
|:-----------|:-------|:------|:--------------|
| **Static**: E_BCS must compete with dS/dtau | W4-A | dS/dtau / \|E_BCS\| = **376,000** | Cutoff must reduce effective gradient by ~4×10⁵ |
| **Dynamic**: τ_dwell must exceed τ_BCS | W4-B | τ_BCS / τ_dwell = **38,600** | Cutoff must slow the roll by ~4×10⁴ |
| **Level 3 dominance** | W4-A | L3 fraction = **91.4%** | Cutting L3 removes 91% of the gradient |
| **Singlet-only shortfall** | W4-B | τ_BCS / τ_dwell(singlet) = **177** | Even without ALL KK modes, singlet alone is 177× too fast |
| **Singlet+BCS friction** | W4-B | τ_BCS / τ_dwell(singlet+BCS) = **10.4** | BCS back-reaction on singlet gives 17× boost, still 10× short |

**The needle hole**: The cutoff function f in Tr f(D²/Λ²) must satisfy:

1. **Suppress Level 3 contribution by ≥ 99.7%** (to bring gradient from 58,673 down to ~170, the singlet+BCS-friction regime)
2. **Then the remaining ~10× shortfall** requires either:
   - A cutoff that also reshapes the singlet landscape (creating curvature near fold), OR
   - Additional friction from multi-sector BCS (not just singlet), OR
   - Modified moduli kinetic term G_mod (if heavier than 5.0)

**Why this is a well-defined target**: The Connes spectral action uses Tr f(D²/Λ²) where f is a smooth positive function with f(0) = 1 and f(x) → 0 for x → ∞. The eigenvalue |λ_k| at Level 3 is ~10× larger than at Level 0. A cutoff Λ set between Level 1 and Level 3 eigenvalues would naturally suppress Level 3 while preserving the fold structure. The question is whether the fold (van Hove singularity) produces sufficient curvature in S_f(tau) once the UV contamination is removed.

**Pre-registered gate for Session 37**:
- **CUTOFF-SA-37**: Compute S_f(tau) = Σ_{(p,q)} dim(p,q)² × Σ_k f(|λ_k^{(p,q)}(tau)|²/Λ²) for physically motivated cutoff scales Λ
- PASS: S_f(tau) has minimum near fold AND τ_dwell(f) / τ_BCS > 1
- FAIL: S_f(tau) still monotonic for all Λ → mechanism chain CLOSED at all levels

---

# Synthesis

**Status**: COMPLETE

## Session 36 Synthesis

### Narrative

Session 36 executed 14 computations across 4 waves (4 zero-cost, 6 medium-cost, 2 dependent, 2 decisive fork) with 11 distinct specialist agents. The session resolved 6 of the 10 open questions from the nazarewicz × string-theory workshop, confirmed 6 structural results, and precisely quantified the framework's deepest structural obstacle — the needle hole for the cutoff function. (4 zero-cost, 6 medium-cost, 2 dependent, 1 decisive fork) with 11 distinct specialist agents. The session resolved 6 of the 10 open questions from the nazarewicz × string-theory workshop, permanently closed 7 mechanisms, confirmed 6 structural results, and identified the framework's deepest structural obstacle.

**The central result is the needle hole.** Two independent computations — W4-A (static landscape) and W4-B (dynamical trajectory) — converge on the same quantitative target. The linear spectral action S = Σ|λ_k| on Jensen-deformed SU(3) is monotonically increasing, with a gradient 376,000× larger than the BCS energy (static) and a fold transit time 38,600× shorter than the BCS formation timescale (dynamical). Level 3 KK modes dominate (91.4% of gradient). The mechanism chain (Van Hove → RPA → Turing → Wall → BCS) remains internally valid as mathematics but cannot engage within the linear spectral action.

**The needle hole defines the cutoff target.** Connes' physical spectral action is Tr f(D²/Λ²) with a smooth cutoff f, NOT the linear sum. Suppressing Level 3 removes 91% of the gradient. The remaining ~10× shortfall (singlet-only is still 10.4× too fast with BCS friction) requires the cutoff to reshape the low-mode landscape. This is a well-defined, quantitative target for Session 37's CUTOFF-SA-37 gate.

**The mechanism chain trajectory: UNCONDITIONAL(S35) → CONDITIONAL(S36 W2-B) → NEEDLE HOLE(S36 W4).** The chain's validity is contingent on the cutoff function — which is not a free parameter but a physical requirement of the Connes spectral action.

**PMNS is comprehensively closed on the Jensen curve** by five independent structural arguments (all Schur's lemma on U(2) irreps). The mass hierarchy (R = 27.2) and normal ordering survive as zero-parameter predictions. The path forward is off-Jensen deformation (breaking SU(2) within U(2)), contingent on a zero-cost check: the K₇ charge of the G1 mode in the (1,0) sector.

### Session 36 Permanent Results

1. **GL-CUBIC-36**: Phase transition is SECOND ORDER. U(1)_7 charges ±1/2 forbid all cubic GL invariants (analytic proof: sum of three half-integers is never zero). Z₂ universality class.
2. **ANOM-KK-36**: KK tower is anomaly-free at levels 0-3. 150 anomaly coefficients = 0 exactly. Structural theorem from π₁(SU(3)) = 0.
3. **COLL-36**: Jensen response is VIBRATIONAL (chi/chi_sp = 12.1 W.u.). Moderate collectivity from constructive multi-mode coherence.
4. **MMAX-AUTH-36**: Authoritative M_max range [1.351, 1.674]. "1.445" SUPERSEDED (rho_B1 = 1.0 artifact). B1 proximity adds 23.4% via V(B1,B2) = 0.080.
5. **W6-SPECIES-36**: W6 wall RESOLVED. Λ_species/M_KK = 2.06 (THIN). Self-consistent species counting corrects the ~10^{48} overestimate.
6. **ED-CONV-36**: Pairing ENHANCED by multi-band (E_cond: -0.115 → -0.137, monotonic with N). B1 is essential proximity catalyst despite V(B1,B1) = 0.

### Session 36 Closures (7 mechanisms)

7. **INTER-SECTOR-PMNS-36**: All PMNS routes CLOSED on Jensen curve. Inner fluctuations preserve Peter-Weyl (structural zero). H_eff analytic bound R·sin²θ < 17.8. Φ-tilde locked by Schur's lemma.
8. **WIND-36**: BDI winding ν = 0. Topologically trivial condensate. E_B2/Δ = 33.4 (deep trivial). Level 4 edge modes CLOSED.
9. **BBN-LITHIUM-36**: δH/H = -6.6×10⁻⁵, 500× below lithium window. During BBN (tau ~ 0.34-0.54), no BCS condensate exists (outside pairing window). CLOSED by two independent routes.
10. **SC-HFB-36 (unconstrained)**: M_max(GCM) = 0.646. BCS energy cannot overcome singlet spectral gradient.
11. **TAU-STAB-36**: S_full(tau) monotonically increasing. dS/dtau = +58,673 at fold, overwhelms E_BCS by 376,000×. All 10 sectors separately monotonic. Constrained regime CLOSED.
12. **SC-HFB-36 (constrained)**: CLOSED by TAU-STAB-36 FAIL. No external stabilization exists.

### Surviving Escape Routes

**Route 1 (HIGHEST PRIORITY): Cutoff-modified spectral action**
- Connes' physical spectral action is Tr f(D²/Λ²) with smooth cutoff f, NOT S = Σ|λ_k|
- Linear sum dominated by Level 3 (91.4%). Cutoff suppresses high eigenvalues
- If cutoff restores low-mode (fold) dominance → minimum could emerge
- Pre-registered gate: **CUTOFF-SA-37** — compute S_f(tau) = Σ f(|λ_k|²/Λ²) for physical f

**Route 2: Off-Jensen metric family**
- Monotonic increase may be specific to 1-parameter Jensen subfamily
- 5-parameter Milnor family (3-parameter U(2)-invariant) unexplored
- Pre-registered gate: **MILNOR-SA-37** — map S on 2-3 parameter family

**Route 3: K7-G1-37 (PMNS)**
- Compute q₇(G1) in (1,0) sector
- If q₇ = 0 → full 3×3 PMNS via (B1, B3₀, G1) triad under off-Jensen
- If q₇ ≠ 0 → PMNS classified Level 5

### Probability Assessment

**Post-36 Sagan: 28%(W3-A pre-TAU-STAB) → revised ~12% (6-20%) post-TAU-STAB.**

Pre-TAU-STAB assessment (W3-A):
- Upward: W6 resolved (BF 2.0), anomaly-free (1.2), ED enhanced (1.3), second-order (1.1), vibrational (1.1).
- Downward: SC-HFB unconstrained FAIL (0.50), PMNS closed on Jensen (0.60), WIND trivial (0.85), BBN negligible (0.90).

TAU-STAB-36 additional downward pressure (BF ~ 0.40):
- Constrained regime CLOSED → removes the 25% × 48.2% conditional survival path
- Chain status: UNCONDITIONAL → CONDITIONAL → BROKEN (for linear spectral action)
- Structural floor: 3% (Sagan), 4% (panel) — Kepler-solids regime

Offsetting the floor collapse:
- Cutoff escape route is physically motivated (Connes NEVER uses linear sum)
- The linear sum result may be the wrong computation — physical spectral action requires cutoff
- Pure math results (anomaly-free, second-order, vibrational, W6, ED enhanced) all stand
- Trajectory: 40%(pre-22) → 46%(22a) → 38%(22b) → 44%(22c) → 27%(22d) → 6%(23a) → 3%(24b) → 18%(33b) → 18%(34) → 32%(35) → **12%(36)**

## Gate Verdicts Summary

| ID | Verdict | Key Number | Agent |
|:---|:--------|:-----------|:------|
| MMAX-AUTH-36 | **MULTI-BAND VALID** | B2-only M_max = 1.351 > 1.2. Range [1.351, 1.674] | nazarewicz |
| GL-CUBIC-36 | **SECOND ORDER** | R* ∉ R ⊗_sym R. U(1)_7 forbids cubic. Z₂ universality | connes |
| COLL-36 | **VIBRATIONAL (PASS)** | chi/chi_sp = 12.1 W.u. > 10 threshold | landau |
| ANOM-KK-36 | **ALL VECTOR-LIKE (PASS)** | 150 coefficients = 0 exactly. Levels 0-3 | kaluza-klein |
| INTER-SECTOR-PMNS-36 | **FAIL** | All 3 routes closed. Structural (Schur). R=27.2 survives | neutrino |
| SC-HFB-36 | **FAIL (unconstrained) / PASS (constrained)** | M_max(GCM) = 0.646 / 1.292. Fork on S_full(tau) | nazarewicz |
| WIND-36 | **ν = 0 (TRIVIAL)** | E_B2/Δ = 33.4. Deep trivial. Level 4 CLOSED | berry |
| W6-SPECIES-36 | **THIN (PASS)** | Λ_species/M_KK = 2.06. W6 resolved | spectral-geometer |
| ED-CONV-36 | **ENHANCED** | E_cond: -0.115 → -0.137. B1 catalyst. Monotonic | quantum-acoustics |
| BBN-LITHIUM-36 | **FAIL (NEGLIGIBLE)** | δH/H = -6.6×10⁻⁵. 500× below threshold | feynman |
| BAYES-SC-36 | **28% (14-40%)** | Marginal p(SC>1) = 24.3%. BF = 0.82 | sagan |
| PMNS-PATH-36 | **LEVEL 5 (CONDITIONAL)** | K7-G1-37 pre-registered. Off-Jensen viable if q₇=0 | gen-physicist |
| TAU-STAB-36 | **FAIL (MONOTONIC)** | dS_full/dtau = +58,673 at fold. All 10 sectors monotonic. No minimum | baptista |

## Constraint Map Updates

| Constraint | Type | Session | Status |
|:-----------|:-----|:--------|:-------|
| GL cubic term | Structural | 36 W1-B | CLOSED (U(1)_7 parity) |
| KK anomaly wall | Consistency | 36 W1-D | CLOSED (π₁=0, vector-like) |
| Inter-sector PMNS (Jensen) | Existential | 36 W2-A | CLOSED (Schur's lemma) |
| BDI edge modes | Structural | 36 W2-C | CLOSED (ν=0, trivial) |
| BBN lithium via BCS | Predictive | 36 W2-F | CLOSED (500× below threshold) |
| W6 wall | Framework | 36 W2-D | RESOLVED (Λ_sp/M_KK = 2.06) |
| Tau stabilization (linear SA) | Existential | 36 W4-A | CLOSED (S_full monotonic, all sectors) |
| Mechanism chain (linear SA) | Existential | 36 W2-B+W4-A | BROKEN (no self-consistent tau pinning) |
| SC-HFB constrained | Existential | 36 W4-A | CLOSED (no external stabilization exists) |
| ED convergence | Existential | 36 W2-E | CONFIRMED (enhanced, monotonic) |

## Files Produced

| File | Gate | Agent |
|:-----|:-----|:------|
| tier0-computation/s36_mmax_authoritative.py/.npz | MMAX-AUTH-36 | nazarewicz |
| tier0-computation/s36_gl_cubic_check.py/.npz/.png | GL-CUBIC-36 | connes |
| tier0-computation/s36_collectivity.py/.npz | COLL-36 | landau |
| tier0-computation/s36_anomaly_kk.py/.npz | ANOM-KK-36 | kaluza-klein |
| tier0-computation/s36_intersector_pmns.py/.npz/.png | INTER-SECTOR-PMNS-36 | neutrino |
| tier0-computation/s36_gcm_self_consistent.py/.npz/.png | SC-HFB-36 | nazarewicz |
| tier0-computation/s36_bdi_winding.py/.npz/.png | WIND-36 | berry |
| tier0-computation/s36_species_scale.py/.npz/.png | W6-SPECIES-36 | spectral-geometer |
| tier0-computation/s36_multisector_ed.py/.npz/.png | ED-CONV-36 | quantum-acoustics |
| tier0-computation/s36_bbn_lithium.py/.npz | BBN-LITHIUM-36 | feynman |
| tier0-computation/s36_bayesian_posterior.py/.npz | BAYES-SC-36 | sagan |
| tier0-computation/s36_pmns_path_analysis.py | PMNS-PATH-36 | gen-physicist |
| tier0-computation/s36_sfull_tau_stabilization.py/.npz/.png | TAU-STAB-36 | baptista |
