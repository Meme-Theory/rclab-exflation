# Session 70 Synthesis: NCG Assessment of 46-Computation Spectral Landscape

**Date**: 2026-04-09
**Agent**: Connes-NCG-Theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/archive/session-70/session-70-results-workingpaper.md` (46 computations across 5 waves)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` (70-session accumulated NCG context)

---

## I. Session Outcome

S70 establishes three structural results of direct NCG significance: (1) the spectral action's 5-term heat kernel expansion converges to 0.08% at Lambda = 2.048 M_KK (NON-PERT-SA-70 PASS), validating the asymptotic expansion at the fold; (2) the dark energy sound speed c_s^2 = 0 is derived from the product geometry factorization of the spectral triple (Q-SOUND-70 PASS), converting an assumption into a theorem; and (3) the full 35-dimensional volume-preserving Hessian of the spectral action has all positive eigenvalues at the Jensen fold (OFF-JENSEN-HESS-70), confirming that the fold is a genuine local minimum of the spectral action in the physical moduli space. Against this, the alpha_s tension proves structural (F0-ALPHA-S-70 FAIL): no spectral function normalization f_0 simultaneously satisfies both the gauge coupling and Higgs mass constraints through the CCM matching formula.

---

## II. Key Results

### II.1. Spectral Action Validity at the Fold

**Result**: |S_exact - S_HK,5-term| / S_HK = 0.080% at Lambda = 2.048 M_KK for f(x) = exp(-x). Classification: GEOMETRIC.

The spectral action principle Tr f(D^2/Lambda^2) is the foundational dynamical object in the NCG framework. Its physical content is extracted through the heat kernel asymptotic expansion

S_b ~ f_4 Lambda^8 a_0 + f_2 Lambda^6 a_2 + f_0 Lambda^4 a_4 + ...   (1)

where a_{2k} are the Seeley-DeWitt coefficients. W1-G (NON-PERT-SA-70) computed the exact spectral action S_exact = sum_n d_n f(lambda_n^2/Lambda^2) directly from the 439,488 Plancherel-weighted eigenvalue instances at L_max = 6 and compared it to the 5-term truncation of (1) at multiple Lambda values.

The 0.08% convergence at Lambda = 2.048 M_KK -- precisely the swampland-determined cutoff from S69 -- is a nontrivial validation. The Seeley-DeWitt expansion is an asymptotic series, not a convergent one; its regime of validity depends on Lambda being large relative to lambda_max(D_K). At L_max = 6, lambda_max = 3.18 M_KK, giving Lambda/lambda_max = 0.64. That the 5-term expansion converges at all in this regime is a consequence of the Gaussian suppression: f(x) = exp(-x) exponentially suppresses eigenvalues above Lambda, effectively restricting the trace to a spectral window where the expansion is well-controlled.

Three critical observations from the NCG standpoint:

(i) **Three functionals span a 53x range in magnitude**: sqrt(x) gives S = 503,908; exp(-x) gives S = 122,872; the zeta action S_zeta = a_4 = 9,523.16. This demonstrates maximal scheme dependence in the full spectral action. The Seeley-DeWitt coefficients a_0, a_2, a_4, a_6 are functional-independent (they are spectral invariants of D_K), but the physical action depends on which moments are weighted by f.

(ii) **The 3-term expansion fails universally**: Including only a_0, a_2, a_4 gives the wrong sign at all Lambda tested. This is because the 3-term truncation's leading term f_4 Lambda^8 a_0 dominates with the wrong sign from the polynomial fit. The standard NCG literature (Chamseddine-Connes 1996, Chamseddine-Connes-Marcolli 2007) works at the level of the a_4 coefficient for the Yang-Mills action and a_2 for Einstein-Hilbert, implicitly assuming Lambda >> lambda_max. The S70 result shows this assumption breaks at the framework's operating scale.

(iii) **The spectral zeta sums are the reliable extraction method**: Direct computation of a_{2k} = sum_n d_n |lambda_n|^{-2k} gives a_0 = 219,744, a_2 = 42,862, a_4 = 9,523, a_6 = 2,590. These are exact for the truncated spectrum and convergent. The polynomial fit to the heat kernel K(t) is ill-conditioned (condition number 1.5e9) and fails for a_0 and a_2. This is a methodological finding: for finite spectral triples, spectral zeta sums are the canonical extraction procedure for Seeley-DeWitt coefficients, not heat kernel polynomial regression.

### II.2. Product Geometry Factorization and c_s^2 = 0

**Result**: c_s^2 = 0 at tree level from the algebraic dependence of S_b on g_K; one-loop correction c_s^2 = 3.36e-4, suppressed by exp(-M_KK/H_0). Classification: GEOMETRIC.

This is a structural consequence of the product spectral triple. For the almost-commutative geometry M^4 x F, the Dirac operator takes the form

D = D_M tensor 1_F + gamma_5 tensor D_F   (2)

where D_M acts on sections of the spinor bundle over M^4 and D_F acts on the finite-dimensional Hilbert space H_F. The eigenvalues of the internal operator D_K (the framework's replacement for D_F) depend on the internal metric g_K at each spacetime point x in M^4, but crucially, on g_K(x) itself and NOT on its spacetime derivatives d_mu g_K(x).

The proof chain is:
1. The heat kernel trace K(t) = sum_n d_n exp(-t lambda_n^2) is a function of the eigenvalues {lambda_n(g_K)} only.
2. The eigenvalues are determined by the internal geometry (g_K) at each point, not by how g_K varies across M^4.
3. Therefore delta^2 S / delta(d_mu g_K)^2 = 0 identically.
4. The sound speed c_s^2 = [kinetic coefficient] / [potential coefficient] = 0/finite = 0.

This is exact within the framework of product spectral triples. In the standard NCG almost-commutative geometry (Connes-Chamseddine 1996), D_F is constant across M^4 -- the finite noncommutative space F does not depend on the spacetime point. The framework's generalization to a point-dependent D_K(g_K(x)) preserves the product structure so long as the fibration remains a product (no warping, no non-trivial connection on the fiber bundle beyond inner fluctuations). The c_s^2 = 0 result holds whenever the product geometry factorization is exact.

**Departure from standard NCG**: In the Connes-Chamseddine-Marcolli formulation, D_F is a fixed matrix encoding Yukawa couplings and Majorana masses. It does not depend on a continuous modulus tau. The framework introduces tau as a continuous parameter labeling left-invariant metrics on SU(3), which replaces D_F with a one-parameter family D_K(tau). This is a genuine extension beyond the standard NCG-SM. The product factorization (and hence c_s^2 = 0) is preserved by this extension because D_K(tau) acts only on internal degrees of freedom, but the existence of the modulus tau itself has no analog in the CCM spectral triple, where D_F is unique (up to inner fluctuations) once the algebra A_F = C + H + M_3(C) is specified.

The one-loop correction c_s^2 = 3.36e-4 is formally nonzero but suppressed by the KK mass gap: all carrier modes have mass M_KK >> H_0, giving exponential suppression exp(-M_KK/H_0) ~ 0. This is the spectral gap protection mechanism: the compact resolvent property of D_K (a fundamental requirement of the spectral triple axioms) ensures that loop corrections from the tower of KK modes are exponentially suppressed at cosmological energy scales.

### II.3. Jensen Fold as True Minimum of the Spectral Action

**Result**: All 35 volume-preserving eigenvalues of the spectral action Hessian are positive at tau = 0.19. Softest eigenvalue = 29.81 (BCS-dressed). Classification: GEOMETRIC.

The Jensen deformation of SU(3) defines a one-parameter family of left-invariant metrics with U(2) symmetry, parameterized by tau. The fold at tau = 0.19 was identified as a special point by multiple criteria (van Hove singularity, spectral density extremum, B2 eigenvalue minimum). W4-G now establishes that this point is a genuine local minimum of the one-loop spectral action in the full 35-dimensional volume-preserving moduli space Sym_0^2(su(3)^*).

From the NCG standpoint, this is significant because the spectral action on the space of left-invariant metrics on SU(3) defines a natural functional on the moduli space of internal geometries. The equations of motion delta S / delta g_K = 0 select the physical internal geometry. The full Hessian computation shows:

(i) The Jensen line is an exact geodesic in the DeWitt metric on the 36D moduli space (the gradient vanishes in all 35 transverse directions by Schur's lemma, S69 permanent theorem).

(ii) All 35 transverse eigenvalues are positive, confirming the Jensen fold as a valley minimum, not a saddle point.

(iii) The eigenvalue cluster pattern {1, 4, 3, 6, 3, 1, 4, 8, 5} matches the Ad(U(2)) irreducible decomposition, reflecting the residual U(2) symmetry of the Jensen metric. This is a representation-theoretic structure, confirming that the Hessian respects the symmetry of the critical point.

(iv) The softest mode has Jensen overlap 0.478 and is predominantly the u(1) breathing mode -- the direction in moduli space that stretches the U(1) factor while compressing the SU(2) factor. This is the same mode identified in S63/S66/S69 as the lightest transverse excitation.

**Connection to the standard NCG framework**: In the CCM spectral triple, the internal geometry is fixed by the axioms (up to a finite number of Yukawa parameters). There is no analog of a moduli space of internal geometries. The framework's claim that the physical internal geometry is dynamically selected by the spectral action is an extension beyond the standard formulation. The S70 Hessian result supports this extension by showing that the selection is robust: the Jensen fold is not merely a critical point but a stable one.

### II.4. Alpha_s Tension as Structural Anti-Correlation

**Result**: F0-ALPHA-S-70 FAIL. alpha_s(M_Z) = 0.118 requires f_0 = 6.33 where m_H = 190 GeV. m_H = 125 GeV requires f_0 = 1.33 where alpha_s = 0.020. No joint solution. Classification: PARTICLE / GEOMETRIC.

The CCM matching formula relates the Higgs quartic coupling to the gauge coupling at the KK scale:

lambda_CCM(M_KK) = (4/3) g_3^2(M_KK) * (a_4/a_2)   (3)

where a_4/a_2 is the Gilkey ratio (0.4140 at the fold). Both g_3^2 and lambda_CCM depend on the spectral function normalization f_0 through the tree-level relation alpha_3(tree) = 2 pi^2 f_0 / a_4. Increasing f_0 simultaneously increases both alpha_s(M_Z) (via stronger QCD running) and m_H (via larger lambda_CCM), creating an algebraic anti-correlation.

This tension lives at the intersection of NCG and RG flow. The CCM formula (3) is a direct consequence of the spectral action: both the Yang-Mills action (a_4) and the Higgs potential (also a_4) arise from the same Seeley-DeWitt coefficient. The ratio a_4/a_2 is a geometric invariant of the spectral triple, computable from the curvature of SU(3) at the fold. The tension arises because this single geometric invariant must simultaneously control two independent physical observables (g_3 and lambda_H) that are measured at a scale 15 orders of magnitude below M_KK, after 2-loop RG evolution.

Three structural escape routes exist within NCG:
1. **Higher-order spectral action contributions**: The a_6 coefficient introduces corrections to both the gauge coupling and the Higgs quartic that are suppressed by Lambda^{-2} relative to a_4. At Lambda = 2.048 M_KK, the ratio a_6/a_4 = 0.272 -- not negligible. These corrections could break the anti-correlation by adding an f_0-independent contribution to lambda_CCM.
2. **Off-Jensen deformation**: Breaking U(2) invariance changes the spectral geometry and potentially alters the Gilkey ratio a_4/a_2 independently of g_3. The W4-G result (all 35 eigenvalues positive) constrains but does not exclude this route.
3. **Pati-Salam extension**: The enlarged algebra A_PS introduces 9 additional gauge generators (S63 PS-KASPAROV-63 PASS), modifying the a_4 coefficient and potentially decoupling the Higgs and gauge constraints.

### II.5. L_max = 7 Sign Reversal and Peter-Weyl Convergence

**Result**: At L_max = 7, all 8 new (p,q) sectors have omega_min > Lambda = 2.048 M_KK, producing a sign reversal in the KK threshold sum. Classification: GEOMETRIC.

The threshold sum S_inf = sum_{L>=1} S_L, where S_L is the contribution from the L-th Peter-Weyl level, governs the KK threshold correction to the gauge coupling at M_KK. For L = 0 through 6, each S_L is positive (the Gaussian weight exp(-omega^2/Lambda^2) is between 0 and 1, and the logarithmic factor ln(Lambda^2/omega_min^2) is positive because omega_min < Lambda). At L = 7, omega_min crosses Lambda, the logarithmic factor changes sign, and S_7 < 0.

This is a structural feature of the Gaussian regulation. The Peter-Weyl decomposition of the spectral action on SU(3) expresses S = Tr f(D_K^2/Lambda^2) as a sum over irreducible representations (p,q). Each representation contributes its eigenvalues weighted by the cutoff function f. When f is Gaussian, eigenvalues larger than Lambda are exponentially suppressed but the logarithmic prefactor changes sign at omega = Lambda.

From the NCG standpoint, this reveals a fundamental tension between two approaches to computing the spectral action:
(i) **Direct spectral computation**: S = sum_n d_n f(lambda_n^2/Lambda^2) is finite, well-defined, and exact for any truncation. It is the non-perturbative definition.
(ii) **Peter-Weyl level-by-level computation**: Each level contributes a finite amount, but the partial sums oscillate rather than converge monotonically once omega_min(L) > Lambda.

The resolution is that the spectral action is fundamentally a trace, not a series. The Peter-Weyl decomposition is a computational tool, not a physical principle. The oscillatory convergence at L >= 7 is an artifact of decomposing an inherently convergent trace into components that individually lose convergence beyond a certain level. The spectral zeta function route -- computing the trace directly from all eigenvalues without PW decomposition -- would bypass this issue entirely.

The practical consequence is that the S66 Aitken extrapolation (S_inf = 2.895, m_H = 127.5 GeV) was computed entirely in the monotone regime and is now an upper bound. The corrected range m_H in [127, 135] GeV reflects the oscillatory convergence uncertainty. The 8% agreement with the observed 125.1 GeV is preserved, but the prediction has widened.

### II.6. Functional Independence Map and alpha_s = 0

**Result**: alpha_s = 0 is FUNCTIONAL-INDEPENDENT (exact in all spectral action schemes). f_NL^equil = 0.853 is FI. n_s and r are SCHEME-DEPENDENT. Classification: GEOMETRIC.

W5-I (CONSISTENCY-FI-MAP-70) classifies each observable as functional-independent (FI) or scheme-dependent (SD) across the family of spectral actions Tr f(D^2/Lambda^2) parameterized by f. This classification is of fundamental NCG significance because the spectral action principle states that physics depends only on the spectrum of D, not on the choice of f. If a physical observable depends on f, then either (a) additional input is needed beyond the spectral triple (violating universality), or (b) the observable is not purely spectral.

The alpha_s = 0 result is the framework's cleanest functional-independent prediction. It follows from a chain of purely spectral arguments:
1. The spectral gap of D_K gives k_tach ~ Lambda ~ M_KK.
2. The hierarchy k_CMB/k_tach ~ 10^{-60} is set by post-transit expansion (not by f).
3. For k << k_tach, the Bogoliubov coefficient |beta_k|^2 = 1 (complete particle production, independent of the pump profile z''/z, which depends on f).
4. A flat |beta_k|^2 gives a pure power law P(k) ~ k^{n_s - 1}, and d^2(ln P)/d(ln k)^2 = 0 identically.

The n_s value itself is scheme-dependent because it depends on eps_H = (1/2)(S'/S)^2, which involves the spectral action profile S(tau). The S70 computation (W5-H) shows d(ln eps_H)/d(alpha) = 1.076 for the family f(x) = x^{alpha/2}, confirming that n_s spans a range of 0.046 over alpha in [0.5, 1.5]. The Planck-compatible window in alpha is [0.67, 1.10], with the framework's canonical alpha = 1.0 (corresponding to f(x) = sqrt(x)) near the upper edge.

### II.7. Seeley-DeWitt Coefficient Hierarchy

**Result**: a_0 = 219,744; a_2 = 42,862; a_4 = 9,523; a_6 = 2,590 from spectral zeta sums. Ratios: a_2/a_0 = 0.195, a_4/a_2 = 0.222, a_6/a_4 = 0.272. Classification: GEOMETRIC.

The standard NCG spectral action expansion (Eq. 1) assigns physical roles to each coefficient:
- a_0: cosmological constant (mode count, volume term)
- a_2: Einstein-Hilbert action (scalar curvature R)
- a_4: Yang-Mills + Higgs quartic (gauge coupling + symmetry breaking)
- a_6: higher-curvature corrections (R^3 invariants)

The S70 hierarchy a_0 >> a_2 >> a_4 >> a_6 is the expected pattern for an 8-dimensional compact manifold with moderate curvature (R = 2.018 at the fold). The Gilkey identity a_2/a_0 = (5/12)R, verified in S61 to 1.33e-14%, provides the dictionary between spectral moments and Riemannian geometry.

W3-G (LEGGETT-MOMENT-70) traces the sensitivity of the Leggett gap omega_L to each coefficient. The result is physically transparent from the NCG perspective:
- a_4 is the structural controller: the gauge coupling g^2 ~ 1/a_4 enters the BCS pairing vertex. This is representation-theoretic and functional-independent.
- a_0 provides numerically dominant sensitivity through BCS exponential amplification: the density of states rho ~ a_0 enters Delta ~ exp(-1/(g*rho)), giving d(ln omega_L)/d(ln a_0) = 2.907.
- a_6 is subleading (sensitivity 0.031, which is 94x below a_0 and 15x below a_4), confirming that the Leggett gap is not controlled by higher-curvature terms.

The Gilkey ratio a_4/a_2 = 0.222 (spectral zeta) versus ratio_gilkey = 0.4140 (pure curvature ratio) resolves the 14.9% discrepancy identified in W1-E. These are different mathematical objects: the spectral zeta value receives contributions from all heat kernel coefficients through the Mellin transform, while the Gilkey ratio is the pure curvature polynomial at order k = 4 divided by that at order k = 2. The CCM matching formula (3) uses ratio_gilkey, not the spectral zeta ratio, because it relates local curvature invariants to gauge couplings.

### II.8. BCS Shell Self-Conjugacy and 8/992 Exactness

**Result**: BCS-PROXIMITY-70 UNFLAGGED. Proximity-induced gap Delta_ind = 0 exactly by SU(3) selection rule. The 8 lowest eigenvalue branches form a self-conjugate set under (p,q) <-> (q,p). Classification: GEOMETRIC.

The BCS pairing in the framework acts on 8 modes out of 992 total eigenvalues at L_max = 6. The question of whether proximity-induced pairing extends to higher modes is answered by representation theory: s-wave (singlet) pairing requires sectors (p,q) and (q,p) to form a Cooper pair. The BCS shell {(0,1), (1,0), (0,0), (1,1), (0,2), (2,0), (1,2), (2,1)} is self-conjugate -- every sector's conjugate partner is already in the shell. None of the 8 proximity sectors have conjugate partners in the BCS shell.

This is a structural consequence of the representation theory of SU(3) and the ordering of eigenvalues by the Casimir C_2(p,q). The lowest-lying representations naturally pair into conjugate families, and the BCS shell is closed under conjugation. The 8/992 truncation is therefore EXACT, not approximate, for singlet pairing.

From the NCG perspective, this connects to the K-theoretic structure of the algebra A_F = C + H + M_3(C). The BCS pairing respects the K_0 classes of the algebra, and the self-conjugacy of the BCS shell is a manifestation of the Poincare duality in the finite spectral triple (S61: mu_CCM = [[0,1,1],[1,0,1],[1,1,0]], det = 2, non-degenerate). The pairing does not leak to higher modes because the K-theoretic pairing is exact.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| LEGGETT-VACUUM-70 | PASS | r_L = 0.617, eta = 1.56e-4 (sudden quench) |
| F0-ALPHA-S-70 | FAIL | Anti-correlated: alpha_s and m_H cannot be jointly matched via f_0 |
| Q-SOUND-70 | PASS | c_s^2 = 0 (tree exact), 3.36e-4 (1-loop) |
| NON-PERT-SA-70 | PASS | 0.080% (5-term HK at Lambda = 2.048) |
| BELL-GGE-70 | PASS | min S = 2.351, 8/8 modes violate Bell |
| TRAPPED-ACOUSTIC-70 | PASS | 0/800,000 trapped points, theta_+ > 585 |
| LMAX7-PW-70 | INFO | r_7 = -1.654, sign reversal (PERMANENT) |
| FULL-COV-PANTHEON-70 | INFO | Delta chi^2 = -7.82 (FW preferred, 2.80-sigma) |
| CLASS-ISW-70 | PASS | ISW auto-power 6.72% FW/Quint (Boltzmann) |
| VOID-SIZE-70 | PASS | chi^2/dof(FW) = 0.935 |
| OFF-JENSEN-HESS-70 | INFO | 35/35 eigenvalues positive; Jensen = true minimum |
| PARAMETRIC-GGE-70 | FAIL | delta_OOM = 3.86e-15 (zero growth) |
| CHIRP-PENUMBRA-70 | FAIL | WKB error 84.2% (structurally inapplicable) |
| SUPERLUMINAL-FRACTION-70 | FAIL | F_Leggett = 0.6% (multi-speed hierarchy) |
| DISCRETE-BERRY-DENNIS-70 | FAIL | chi^2/ndof = 329 (no discrete-graph convergence) |
| DM-PAIR-DECAY-70 | PASS | tau_DM = 4.93e82 s (57 OOM above FIRAS) |
| KURAMOTO-SYNC-70 | PASS | K_c = 1.052 < 3.60, E_J/T = 8.33 |
| BCS-PROXIMITY-70 | INFO | Delta_ind = 0 exactly (SU(3) selection rule) |
| CONSISTENCY-FI-MAP-70 | INFO | alpha_s = 0: FI; n_s, r: SD |
| GEODESIC-MODULI-70 | INFO | d(round,fold) = 0.4249, sub-Planckian by 2.35x |

---

## IV. Structural Implications

### IV.1. The Spectral Action at the Fold is Under Control

The convergence of the 5-term heat kernel expansion to 0.08% (W1-G), the positivity of all 35 Hessian eigenvalues (W4-G), the sub-Planckian modulus field excursion (W5-L), and the swampland conjecture satisfaction (c = 3.44 >> 1) collectively establish that the spectral action is a well-defined, stable dynamical functional at the fold. The spectral triple (A_F, H_F, D_K(tau=0.19)) defines a point in the moduli space of internal geometries that is a genuine critical point of the spectral action with no flat or tachyonic directions.

This is the strongest validation of the spectral action principle for the SU(3) internal geometry to date. The standard NCG-SM uses D_F as a fixed matrix; the framework's dynamical D_K(tau) extends this to a continuous family, and the S70 Hessian computation shows that the spectral action selects a unique point (the Jensen fold) from this family.

### IV.2. Product Geometry Factorization Has Observational Consequences

The c_s^2 = 0 derivation (W1-C) and the ISW Boltzmann confirmation (W2-C) demonstrate that the product structure of the spectral triple M^4 x F directly constrains dark energy perturbation physics. In the NCG almost-commutative geometry, the product factorization is an axiom, not an assumption. The S70 result converts this axiom into an observational prediction: the ISW auto-power spectrum differs by 6.7% between the framework (c_s^2 = 0, tracking DE) and quintessence (c_s^2 = 1, smooth DE).

This is a genuinely new connection between NCG structure and observable cosmology. The standard NCG-SM has no cosmological sector; the framework's extension to cosmology via the Jensen deformation makes the product factorization axiom empirically testable.

### IV.3. Alpha_s Tension Constrains the CCM Formula

The F0-ALPHA-S-70 FAIL does not invalidate the NCG framework -- it constrains the tree-level CCM matching formula (3). The anti-correlation between alpha_s and m_H through the single parameter g_3^2(M_KK) is a direct consequence of the spectral action generating both the Yang-Mills and Higgs sectors from the same coefficient a_4. This is a feature of the NCG Higgs mechanism (the Higgs is an inner fluctuation of D, not an independent field), and the S70 computation shows that this tight structural coupling creates tension at the quantitative level.

The escape routes (higher-order corrections, off-Jensen deformation, Pati-Salam extension) all involve modifying the relationship between a_4 and the observable couplings while preserving the NCG axiomatic structure. The alpha_s tension is a precision probe of the spectral action's predictions at the 2-loop RG level.

### IV.4. The KO-Dimension Issue Remains

The S66 result KO(SU(3)_manifold) = 0, KO(M^4 x SU(3)) = 4 established a permanent mismatch with the standard NCG-SM KO-dimension of 6. The S70 computations do not resolve this tension. The spectral action is unaffected by KO-dimension (it depends only on the spectrum of D, not on J or gamma), so all bosonic-sector results in S70 are valid regardless. However, the fermionic action <J psi, D psi> is sensitive to the real structure J, and the KO = 4 product assignment affects which fermionic terms are generated. This remains an open structural question for the framework.

### IV.5. Order-One Condition Violation Persists

The order-one condition [[D, a], b^o] = 0, the most commonly violated NCG axiom for D_K on SU(3), continues to fail at 4.000 in the (H,H) sector. Neither the weak order-one route (S45, CLOSED) nor the S70 computations address this structural issue. The Omega^1_D(A_F) space has 342 = 173 + 169 directions (S46, PERMANENT), with the 169 extra quadratic directions reflecting the order-one violation. The S70 Hessian eigenvalue cluster pattern {1, 4, 3, 6, 3, 1, 4, 8, 5} is consistent with this violation -- the lightest scalar direction involves the su(2)_L self-commutator responsible for the 4.000 violation (S46).

---

## V. Forward Projection

### V.1. Spectral Zeta Threshold Sum (HIGHEST PRIORITY from NCG perspective)

The L_max = 7 sign reversal (W1-J) reveals that the Peter-Weyl level-by-level computation of the KK threshold sum enters oscillatory convergence at L >= 7. The spectral zeta function approach -- computing the threshold sum directly as a trace functional of D_K^2 without PW decomposition -- would resolve the convergence and determine m_H to a precision limited only by the eigenvalue truncation, not by the PW resummation. This computation requires the full D_K eigenvalue spectrum at high PW levels but avoids the oscillatory convergence entirely. It is the NCG-natural approach: the spectral action is a trace, and traces converge.

### V.2. Higher-Order Spectral Action Corrections to CCM Matching

The alpha_s tension (W1-B) constrains the tree-level CCM formula. Computing the a_6 corrections to both the gauge coupling and the Higgs quartic would test whether higher-curvature terms in the spectral action break the f_0 anti-correlation. The S70 Seeley-DeWitt coefficient a_6 = 2,590 is now known; what remains is to compute the a_6 contributions to lambda_CCM and g_3^2 at the CCM matching scale.

### V.3. Pati-Salam Spectral Action at the Fold

The S63 PS-KASPAROV-63 result (all 9 PS generators in the enlarged Omega^1_D) establishes that the Pati-Salam extension is consistent with the spectral triple structure. Computing the spectral action for the PS algebra at the fold would provide a second matching relation (beyond CCM) that could decouple the alpha_s and m_H constraints through the 9 additional gauge generators.

### V.4. Fermionic Action with KO = 4

The fermionic action <J psi, D psi> with the product KO-dimension 4 (rather than the standard 6) generates a different set of fermionic terms. Computing the explicit fermionic Lagrangian from the KO = 4 real structure would determine whether the SM fermion content is correctly reproduced, or whether the KO mismatch produces observable deviations.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | HK 5-term converges to 0.08% at Lambda=2.048 | GEOMETRIC | PASS | Spectral action expansion valid at fold |
| 2 | c_s^2 = 0 from product geometry factorization | GEOMETRIC | PASS (PERMANENT) | ISW tracking is structural NCG prediction |
| 3 | 35/35 VP Hessian eigenvalues positive | GEOMETRIC | INFO (PERMANENT) | Jensen fold = true minimum of spectral action |
| 4 | alpha_s/m_H anti-correlated through f_0 | PARTICLE/GEOMETRIC | FAIL | CCM tree-level matching insufficient; higher-order or PS needed |
| 5 | L=7 sign reversal in PW threshold sum | GEOMETRIC | INFO (PERMANENT) | Oscillatory convergence; m_H in [127,135] GeV |
| 6 | alpha_s = 0 is functional-independent | GEOMETRIC | INFO (PERMANENT) | Strongest FI prediction; falsifiable by CMB-S4 |
| 7 | a_0=219744, a_2=42862, a_4=9523, a_6=2590 | GEOMETRIC | INFO | Complete SDW hierarchy; a_4 structural, a_0 numerically dominant |
| 8 | BCS shell self-conjugate under (p,q)<->(q,p) | GEOMETRIC | INFO (PERMANENT) | 8/992 BCS truncation exact by representation theory |
| 9 | WKB structurally inapplicable (Mach 54.73) | GEOMETRIC | FAIL (PERMANENT) | Sudden approximation required; transit non-adiabatic |
| 10 | d(round,fold) = 0.4249, sub-Planckian | GEOMETRIC | INFO | Swampland satisfied; Jensen = exact geodesic in 36D |
| 11 | Three functionals span 53x range at Lambda=2.048 | GEOMETRIC | INFO | Maximal scheme dependence; FI/SD classification essential |
| 12 | ratio_gilkey = 0.4140 != a_4/a_2 = 0.4866 | GEOMETRIC | INFO | Convention mismatch resolved; Gilkey is pure curvature ratio |
| 13 | Leggett gap controlled by a_4, amplified by a_0 | GEOMETRIC | INFO | Not a_6-dominated; safe for framework predictions |
| 14 | BCS backreaction is Ricci-only (Weyl invariant) | GEOMETRIC | INFO | No new singularity; censorship structure preserved |
| 15 | Pantheon+ full cov: Delta chi^2 = -7.82 | PHONONIC | INFO | FW preference strengthened to 2.80-sigma |
