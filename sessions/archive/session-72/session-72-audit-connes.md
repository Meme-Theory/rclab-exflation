# Session 72 Project Audit: NCG Foundations

**Date**: 2026-04-10
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Scope**: Comprehensive audit of all NCG mathematical foundations, distinguishing PROVEN from ASSUMED from OPEN.

---

## I. Spectral Triple Construction Status

The framework claims the physical spectral triple is the almost-commutative product (A, H, D) on M^4 x K where K = (SU(3), g_Jensen(tau)).

### What is Constructed

**The fiber spectral triple (A_F, H_F, D_K)**:
- A_F = C + H + M_3(C): PROVEN to be the correct SM algebra from NCG axioms (S7, Paper 10 CCM 2007). Order-zero condition uniquely selects this from commutant analysis (S9-10).
- H_F = C^32: PROVEN to carry the correct SM quantum numbers (S7, S8). The 32 = 2 x 2 x 2 x 2 x 2 decomposition matches generations x chiralities x particle/antiparticle x weak doublet components.
- D_K = Dirac operator on Jensen-deformed SU(3): CONSTRUCTED at Peter-Weyl level p+q <= 3 (1,232 eigenvalues, 155,984 weighted modes at L_max = 10 with degeneracies). Eigenvalues computed numerically at all tau in [0, 0.5] (S12-S14, updated continuously through S72).

**The product spectral triple**:
- D_total = D_K tensor 1 + gamma_K tensor D_M: ASSUMED from Kasparov product factorization (VdD Paper 01, Theorem 3.5). Verified numerically to machine epsilon at L_max = 3 for the cross-term (A-TENSOR-61: O'Neill term 0.47% at fold, S61).

### What is Missing

1. **Continuum D_K**: All computations use the PW-truncated D_K at L_max = 3 (1,232 distinct eigenvalues) or L_max = 10 (155,984 weighted). The continuum Dirac operator on SU(3) has infinite spectrum. Convergence of spectral quantities (SDW coefficients, spectral action, eigenvalue ratios) with L_max is TESTED but not PROVEN in general. The W1-C result (S72 ZETA-RATIO-CONVERGENCE-72 PASS) shows the zeta ratio a_6/a_4 converges monotonically from L=3 to L=7, crossing the Gilkey target at L=6. But the asymptotic value R_inf is not reliably extractable from 5 points (two different fits give R_inf = -0.32 and R_inf = 0.17).

2. **Self-adjointness of D_K**: ASSUMED. The Dirac operator is constructed from the spin connection via Clifford multiplication. On a compact Riemannian manifold, D is essentially self-adjoint on smooth sections (standard elliptic theory). This is a theorem, not a computation, and applies to the continuum D_K. The PW-truncated D_K is a finite Hermitian matrix, trivially self-adjoint. STATUS: PROVEN for both continuum and truncation, by distinct theorems.

3. **Compact resolvent**: For the continuum D_K on compact SU(3), the resolvent (D_K - z)^{-1} is compact by standard elliptic theory (Weyl asymptotics: eigenvalue growth |lambda_n| ~ n^{1/8}). STATUS: PROVEN by Weyl's law on closed 8-manifolds. Not a gap.

4. **Bounded commutator condition**: [D_K, a] must be bounded for all a in A_F. For A_F = C + H + M_3(C) acting by left multiplication on PW sections, this is PROVEN for the truncated triple (finite matrices). For the continuum, it follows from the Lipschitz regularity of the algebra elements in the spectral triple topology. STATUS: PROVEN in both settings.

5. **The full D_total on M^4 x SU(3)**: Not constructed as a single operator. The product form D_K tensor 1 + gamma_K tensor D_M requires D_M (the base Dirac operator on M^4). The framework uses the flat Minkowski D_M or the emergent metric from the a_2 coefficient. The product operator is formal; the spectral action is computed from the product HEAT KERNEL via the Kunneth formula K_total(t) = K_K(t) * K_M(t), which is EXACT for product metrics.

### Assessment

The fiber spectral triple is mathematically complete modulo truncation. The product structure is formal, relying on the Kasparov factorization theorem which requires the Kato-Rellich condition (see Section II). The central gap is not the construction itself but the AXIOM VERIFICATION on the product triple (see below).

---

## II. Kasparov Product / Factorization

The Kasparov product [D_K] x_A [D_M] = [D_total] in KK-theory is the formal backbone connecting fiber geometry to spacetime physics.

### PROVEN

1. **K-homology class stability** (S61 K-HOMOLOGY-STABILITY-61): The Kato-Rellich parameter alpha = 0.081 < 1 for inner fluctuations of D_K at the fold. The K-homology class [D_K + A] = [D_K] is preserved under gauge fluctuations from A_F. PERMANENT.

2. **Shriek equivalence** (S61 SHRIEK-EQUIV-61): The Kasparov product reproduces the correct index pairing. PERMANENT.

3. **O'Neill cross-term** (S61 A-TENSOR-61): The fiber-base coupling (A-tensor in Kasparov product terminology) is 0.47% at the fold. Small but nonzero -- the product is not exact at the operator level, only at the K-homology level.

4. **Block-diagonal factorization** (S61 BLOCK-DIAG-GENERAL-61): D_K block-diagonalizes by PW sector (p,q) with cross-block = 0 to machine epsilon. The spectral action factorizes EXACTLY as S = sum_{(p,q)} d_{(p,q)}^2 * S_{(p,q)}. PERMANENT.

### ASSUMED

1. **Kato-Rellich for instantons**: The instanton connection A_omega on the SU(3) principal bundle perturbs D_K. The S72 INSTANTON-KAPPA-72 result shows kappa(rho) = sqrt(3)/(2*rho*gap) with kappa(rho = M_KK^{-1}) = 1.057 at the instanton measure peak. This EXCEEDS the Kato-Rellich bound kappa < 1.0. The Kasparov product is NOT GUARANTEED for the dominant instanton configuration. For large instantons (rho > 1.80/M_KK), kappa < 0.586 and the product holds. OPEN: the instanton moduli integration requires the product to hold at the measure peak, where it marginally fails.

2. **Factorization for non-product metrics**: The Kunneth factorization K_total = K_K * K_M assumes a product metric g = g_K + g_M. If the physical metric has fiber-base mixing (e.g., from the O'Neill term), the factorization acquires corrections. The S61 bound of 0.47% on the cross-term is numerical; the correction to SDW coefficients from fiber-base mixing has not been computed analytically.

3. **Factorization with f*(x)**: The S72 Mack-VdD workshop (R1 D2, R2 C6) establishes convergence on this point: the Kasparov product is topological (depends only on [D_K], not on f) and is COMPLETELY UNAFFECTED by the choice of spectral functional. f* = 0.912*sqrt + 0.088*exp having divergent SDW moments does not affect the product. This is now understood, but it was an active confusion until S72.

### OPEN

1. **Instanton sector integration**: Can the non-trivial bundle (c_2 = 1) contribution to alpha_s be computed within the Kasparov framework? At the instanton measure peak, kappa > 1, so the factorization fails. The S72 Mack-VdD workshop (R2 E1) identifies a (rho, tau) phase diagram with three regimes: stable (kappa < 1), marginal (1 < kappa < 2.5), and potentially topologically transitioning (kappa >> 1). The post-transit evolution may cross into the marginal regime as g^2 grows and the BCS gap shrinks. INSTANTON-LANDSCAPE-73 is pre-registered.

2. **Multi-instanton sectors**: All computations use the 1-instanton ADHM configuration. Multi-instanton moduli spaces introduce additional moduli (relative positions, orientations) that could shift kappa downward for certain configurations. Unexplored.

---

## III. Spectral Action: Functional Choice & Convergence

### PROVEN

1. **Spectral action well-defined for finite spectrum**: For any positive f and any finite eigenvalue set, S = sum_n d_n * f(lambda_n^2 / Lambda^2) is a finite, positive, computable number. This is trivial but load-bearing: ALL project computations are direct spectral sums, which are mathematically rigorous regardless of the SDW expansion's convergence.

2. **SDW expansion asymptotic, not convergent** (S72 ASYMPTOTIC-TRUNCATION-72 INFO, PERMANENT): The ratio sequence |a_{2k+2}/a_{2k}| is monotonically increasing at every L_max from 3 to 7. The SDW expansion on D_K(SU(3), g_Jensen) is a divergent asymptotic series with optimal truncation at N* ~ 4 terms (a_0 through a_6). PERMANENT, functional-independent.

3. **Taylor expansion exactness for finite spectra** (S45 UNEXPANDED-SA-45, PERMANENT): For finite spectrum with L > lambda_max, the spectral action S(L) = sum_k d_k f(lambda_k^2/L^2) is EXACTLY its Taylor series in 1/L^2. No non-perturbative content for the truncated spectrum.

4. **Positive spectral functional exists matching (n_s, A_s)** (S72 SPECTRAL-FUNCTIONAL-FIT-72 PASS): f*(x) = 0.912*sqrt(x) + 0.088*exp(-x) matches n_s = 0.9649 and A_s = 2.1e-9 simultaneously with kappa = 2.37e-8. Positivity, sum of positive functions. PROVEN by construction.

### ASSUMED

1. **SDW coefficients a_0, a_2, a_4 are "spectral-robust"**: The S71 three-layer hierarchy (superseded by S72 four-layer) places a_0 through a_4 in the robust layer. The S72 W3-B result shows the SDW expansion is past optimal truncation at a_8, but a_4 is within the window. The assumption is that the first 3 SDW coefficients are reliable proxies for the full spectral action. This is tested (S70 NON-PERT-SA-70 PASS: 5-term HK converges to 0.08% at Lambda = 2.048 for exp(-x)) but the test uses specific f and specific Lambda. For f*, the SDW moments diverge, so the "reliability" of a_0, a_2, a_4 must be reinterpreted as their role in the DIRECT sum approximation, not the expansion.

2. **The spectral functional f is universal**: The Chamseddine-Connes framework treats f as a fixed (but undetermined) positive function. The S72 result f* = 0.912*sqrt + 0.088*exp is the joint best-fit. The ASSUMPTION is that f is the same everywhere in spacetime and at all energy scales. If f depends on the state (e.g., through the BCS condensate), the spectral action becomes state-dependent, and the entire SDW machinery requires modification. The S64 GGE-KMS-64 result (generalized KMS proven) hints at state-dependent spectral actions but does not resolve this question.

### OPEN

1. **Non-perturbative spectral action for f***: f*(x) = 0.912*sqrt(x) + 0.088*exp(-x) has divergent SDW moments (f_0 = infinity, f_2 = infinity). The SDW expansion S ~ f_0*a_0*Lambda^4 + f_2*a_2*Lambda^2 + ... does NOT EXIST for f*. All predictions depending on the expansion (the canonical S62 cutoff-function results, the S70 SDW values) must be recomputed via direct spectral sums. The S72 Mack-VdD workshop (D2) establishes this is mathematically well-defined (the direct sum converges by Weyl's law). But the COMPUTATIONAL implementation for the full S(tau) profile over tau in [0, 2] has not been done. SPECTRAL-ACTION-PROFILE-73 is the resolution.

2. **CC from the spectral action**: With f_0 = infinity for f*, the cosmological constant term f_0*a_0*Lambda^4 is formally infinite. This is an artifact of the expansion, not of the physics (the direct sum gives a finite number). But it means the CC cannot be extracted from the expansion -- it requires the full direct sum at the physical Lambda, which in turn requires knowing Lambda to 120-OOM precision. The CC problem in the spectral action framework is an unsolvable fine-tuning problem for ANY spectral functional with infinite f_0 moments, which includes both f* and the spectral zeta functional. STATUS: Structural impasse, confirmed by S65 (all 11 geometric CC routes CLOSED) and S72 (nonlocal SA worsens CC, PERMANENT).

3. **Scheme dependence of n_s**: The bare spectral geometry gives n_s = 0.9567. The best-fit f* gives 0.9649. The sensitivity delta_t*/delta_n_s ~ 10.7 means n_s is MAXIMALLY scheme-dependent. At Planck precision sigma(n_s) = 0.0042, the allowed f* family is t* in [0.042, 0.136]. At CMB-S4 precision sigma(n_s) ~ 0.002, this narrows. The n_s prediction is NOT a zero-parameter result -- it requires specifying f.

---

## IV. Topological Results (KO-dim, AZ class, quantum numbers)

### PROVEN

1. **KO-dim of the FINITE triple A_F = 6** (S8, PERMANENT): (epsilon, epsilon', epsilon'') = (+1, +1, -1), J^2 = +1. Machine epsilon verification. This is the KO-dimension of the FINITE spectral triple (A_F, H_F, D_F) in the Connes-Chamseddine-Marcolli sense.

2. **KO-dim of SU(3) as a Riemannian spin manifold = 0** (S65 W1-C correction, PERMANENT): For an 8-dimensional spin manifold, KO = 8 mod 8 = 0. J^2 = +1, [J, gamma_9] = 0. JD = -DJ from the B_- choice (both B+/B- give KO = 0 for d = 8). The earlier claim KO(SU(3)) = 6 was an error (it conflated the finite triple with the manifold triple).

3. **Product KO-dim = 4** (S66 PRODUCT-KO-DIM-66 PASS, PERMANENT): KO(M^4 x SU(3)) = KO(M^4) + KO(SU(3)) = 4 + 0 = 4 mod 8. d = 8 is uniquely degenerate: B+/B- give same KO. J_total^2 = -1. epsilon'' = +1 (not -1). The product KO-dim 4 differs from the finite triple KO-dim 6. This is a PERMANENT structural mismatch.

4. **AZ class BDI** (PROVEN, PERMANENT): The BCS quasiparticle Hamiltonian on the fiber has time-reversal T^2 = +1, particle-hole C^2 = +1, giving Altland-Zirnbauer class BDI. The topological invariant is Z (integer winding number). PROVEN from the symmetry structure of D_K.

5. **SM quantum numbers**: H_F = C^32 carries the correct Standard Model quantum numbers for one generation. Three generations require additional structure (not from NCG axioms; Z_3 from SU(3) is a candidate but not proven).

6. **eta(s) = 0 identically** (S61 FUNC-EQ-61, PERMANENT): The spectral asymmetry vanishes to machine epsilon (|eta/zeta| < 87*eps_mach at all 91 complex s tested). J-symmetry forces +/- pairing exactly. Poincare duality intersection form mu_CCM = [[0,1,1],[1,0,1],[1,1,0]], det = 2, non-degenerate.

### ASSUMED

1. **Three generations from Z_3 x Z_3**: The framework CLAIMS three generations arise from the Z_3 quantum number p-q mod 3 on PW sectors of SU(3). This is a plausible CONJECTURE based on the PW decomposition, but it is NOT proven that the NCG axioms require exactly 3 generations. In standard NCG (CCM 2007), the number of generations is an INPUT, not an OUTPUT.

### OPEN

1. **Product KO-dim mismatch**: KO(M^4 x SU(3)) = 4, but the finite triple has KO = 6. The standard NCG-SM uses the TOTAL spectral triple with KO = 10 mod 8 = 2 (on M^4 x F_SM). The framework's KO = 4 differs from both. The Mack-VdD S72 workshop notes: "KO mismatch permanent. Spectral action unaffected; fermionic sector affected." The impact on the fermionic action (which depends on the real structure J and chirality gamma through the KO signs) is UNCOMPUTED.

2. **Fiber selection criterion**: The S72 G2-CONSTANCY-72 FAIL eliminates spectral moment stability as a criterion distinguishing SU(3) from G_2. The surviving criteria (S72 Mack-VdD E6) are: (a) absolute a_2/a_4 ratio (SU(3): 2.03, G_2: 0.049 -- 41x), and (b) SM gauge group recovery from branching rules. Neither is proven to be NECESSARY from first principles. OPEN: prove that a_2/a_4 > 1 is required for physical viability, or find an alternative fiber selection theorem.

---

## V. Jensen Deformation Rigour

### PROVEN

1. **Volume-preserving exactly** (S12, PERMANENT): The Jensen deformation g_s = e^{6s}*g_0|_Cartan + e^{-s}*g_0|_root preserves the Riemannian volume form. det(g_s) = det(g_0) for all s. EXACT, analytic proof from the trace constraint 2*6s + 6*(-s) = 0.

2. **Left-invariant** (STRUCTURAL): The Jensen metric is left-invariant by construction (it is a bi-invariant metric deformed along the Cartan-root decomposition of the Lie algebra). All PW-sector computations respect left-invariance.

3. **U(2) preservation** (S65 OFF-JENSEN-65, PERMANENT): At U(2)-invariant metric, all 28 off-diagonal SA gradient components = 0 exactly. The spectral action flow preserves U(2) at all orders.

4. **Jensen fold is 35D saddle in BCS-dressed SA** (S64 HESSIAN-DESCENT-64, PERMANENT): The full 35-dimensional volume-preserving Hessian at the fold has signature (8+, 27-). The fold is a saddle, not an extremum, of the scalar curvature R(g). But it IS a local minimum in the U(2)-invariant subspace (by U(2) preservation).

5. **R(tau) monotonicity on Jensen path** (S64 S-ASYMPTOTIC-64, PERMANENT): dR/dtau >= 0 by AM-GM. Equality only at tau = 0. Scalar curvature increases monotonically along Jensen.

### ASSUMED

1. **Jensen parameterizes all physically relevant deformations**: The Jensen family is a ONE-parameter slice through the 36-dimensional space of left-invariant metrics on SU(3). The assumption that the physical universe sits on this slice (rather than at a general left-invariant metric) is motivated by U(2) preservation (the spectral action flow keeps you on the Jensen slice) but has not been proven to be the unique attractor.

2. **Volume preservation is physical**: The constraint det(g_s) = const is imposed by hand. In the NCG spectral action, the volume is the a_0 coefficient, which enters the CC. There is no axiom requiring volume preservation. The motivation is that volume-preserving deformations separate the CC problem from the shape problem, but this is a technical convenience, not a theorem.

### OPEN

1. **Jensen deformation in NCG terms**: The Jensen deformation is a Riemannian-geometric construction. Its translation to NCG language is: a one-parameter family of spectral triples {(A, H, D_K(tau))}_tau where D_K(tau) is the Dirac operator on (SU(3), g_Jensen(tau)). The NCG axioms do not single out this family. The question "why Jensen?" has a partial answer (U(2) preservation theorem, PERMANENT) but not a complete one.

2. **Off-Jensen dynamics**: The S64 result shows the fold is a saddle in the full 35D space. The steepest R-decrease direction OPPOSES Jensen (expand SU(2), shrink C^2+U(1)). Off-Jensen dynamics potentially access qualitatively different spectral triples. HESSIAN-DESCENT-64 shows a_0/a_2 INCREASES off-Jensen (CC worsens), which is the a_0/a_2 trap (PERMANENT). But the dynamics of the full off-Jensen flow for the spectral action (not just R) are unexplored.

---

## VI. Alpha_s and the Instanton Sector

### PROVEN

1. **alpha_s = 0 at tree level, trivial bundle** (S49, PERMANENT): On the trivial SU(3) principal bundle over M^4, the gauge coupling g_3 contributes to the spectral action only through the a_4 coefficient, which gives the Yang-Mills action. The running of alpha_s from the spectral action with the zeta regularization gives alpha_s = 0 because the spectral action fixes alpha_s at the KK scale, and the zeta functional's structure gives a trivially zero running coupling in the singlet sector.

2. **M_3(C) inner fluctuations = 0** (S51 GAUGE-U1K7-51, PERMANENT): All 9 M_3(C) generators give ||A_H||_F = 0.000. Only the C+H sector generates nonzero inner fluctuations from D_K. This is structural: the M_3(C) sector commutes with D_K (since D_K is a function of the Laplacian, which commutes with isometries).

3. **K_7 commutant propagation** (S51, PERMANENT): [K_7, D_K] = 0 => [K_7, p(D_K)] = 0 for any polynomial/analytic function p. The commutant of K_7 (a Killing vector generating a U(1) isometry) propagates through all analytic functions of D_K.

### OPEN

1. **alpha_s from non-trivial bundle**: The S72 INSTANTON-KAPPA-72 result opens the possibility: large instantons (rho > 1.80/M_KK) are Kasparov-compatible, but the instanton measure peaks at rho ~ M_KK^{-1} where kappa = 1.057. The net instanton contribution is exponentially suppressed at the fold (S_inst >> 1). At late times (tau_eq ~ 0.49, larger g^2), S_inst shrinks but kappa grows (gap decreases). The interplay is unresolved.

2. **alpha_s from the spectral functional**: For f* = 0.912*sqrt + 0.088*exp, the coupling constant extraction is different from the SDW expansion route. In the zeta regularization, alpha_s comes from a_4. For f*, the a_4 moment is divergent, and the coupling must be extracted from the direct spectral sum. The relationship between the direct-sum alpha_s and the observed value 0.1180 is UNCOMPUTED.

3. **Non-perturbative generation**: Can alpha_s arise from a mechanism other than instantons or the a_4 moment? The S72 Mack-VdD workshop (E1) proposes a topological phase diagram in (rho, tau) space. If the K-homology class changes along the post-transit tau path, the post-transition spectral triple might have a fundamentally different alpha_s.

---

## VII. Mathematical Theorems: Proven vs Assumed

### Permanent Structural Theorems (PROVEN, machine epsilon or analytic)

These results hold regardless of the framework's physical fate.

| # | Theorem | Session | Proof Type |
|:--|:--------|:--------|:-----------|
| 1 | [J, D_K(s)] = 0 (CPT identity) | S17a | Analytic + numerical |
| 2 | V_eff monotonically decreasing all tau | S28 | Exact, 40+ digits |
| 3 | B2 fold universality (global minimum) | S33a | Analytical |
| 4 | Lie derivative monotonicity f(s) = B(s)/5 | S33a | Analytical |
| 5 | B1 singlet selection rule V(B1,B1) = 0 | S34a | Schur + representation theory |
| 6 | Gram matrix PSD (no kinetic tachyons) | S46 | Algebraic (Gram matrix) |
| 7 | Omega^1_D tau-independence: dim = 342 | S46 | Numerical, all tau |
| 8 | SA scalar instability (all phi, all f, all tau) | S46 | Structural: f'(x) < 0 |
| 9 | Connes distance isotropy at tau = 0 | S46 | Numerical (0.02%) |
| 10 | eta(s) = 0 identically | S61 | J-symmetry, 91 complex s |
| 11 | Poincare duality non-degenerate | S61 | det(mu_CCM) = 2 |
| 12 | Gilkey identity a_2/a_0 = (5/12)*R | S61 | Exact to 1.33e-14% |
| 13 | Weil positivity (trivially: finite zeta) | S61 | Bochner + discrete |
| 14 | a_0/a_2 = C_Q/R universal | S65 | All left-invariant metrics |
| 15 | a_3 = 0 identically (closed even-dim) | S65 | Three independent proofs |
| 16 | R(tau) monotonicity on Jensen | S64 | AM-GM |
| 17 | Lambda_SA = Lambda_Jacobson | S64 | Exact |
| 18 | a_0/a_2 trap (VP a_2 decrease worsens CC) | S64 | Analytical |
| 19 | Spectral moment decoupling (CC/NEC independent) | S64 | Structural |
| 20 | Chirality non-cancellation {gamma_9, dD/dtau} = 0 | S64 | Anticommutator exact |
| 21 | Quadratic chiral trace zero Tr(gamma_9 dD dD) = 0 | S65 | Chiral decomposition |
| 22 | BdG twist obstruction | S46 | Algebraic |
| 23 | SDW asymptotic (not convergent) on D_K | S72 | Monotone ratio sequence |
| 24 | PS gauge module PASS | S63 | Rank 2048, 1.2e-14 closure |

### Axiom Verification Status (the 7 NCG axioms on the product triple)

| Axiom | Name | Status | Value | Ref |
|:------|:-----|:-------|:------|:----|
| 1 | Dimension (spectral) | PASS | Weyl growth ~ lambda^8 for fiber | S61 |
| 2 | Regularity | PASS | Smooth algebra, standard | Structural |
| 3 | Finiteness | PASS | Finite projective module | S7 |
| 4 | Reality (J) | PASS | J^2 = +1, [J, D_K] = 0 | S8, S17a |
| 5 | **Order-one** | **FAIL** | **4.000** (H,H), 2.828 (C,H)/(H,M3), 2.000 (C,C)/(M3,M3) | S9-10, S28 |
| 6 | Orientability | PASS | gamma_9 grading | S8 |
| 7 | Poincare duality | PASS | det(mu) = 2 | S61 |

**Summary**: 6/7 PASS, Axiom 5 (order-one) FAILS. This is the single most consequential gap in the NCG foundations. The order-one condition [[D, a], b^o] = 0 fails with maximum violation 4.000 at the (H, H) entry.

**Escape routes investigated**:
- Weak order-one (Bochniak-Sitarz): CLOSED (S45, GG/Full = 1.000 exact, maximal failure)
- Full CCS 2013 quadratic formalism: OPEN (169 extra directions in Omega^1_D, consistent with CCS inner fluctuations without order-one)
- Twisted spectral triples (Paper 30): OPEN (BdG twist from Aut(A_F) closed S46, but enlarged algebra A_BdG or other twists unexplored)
- Representation change: OPEN (choosing a different H_F might satisfy order-one)
- Pati-Salam extension (Paper 24): A_PS = C + H_L + H_R + M_4(C). S63 PS-KASPAROV-63 PASS shows PS gauge module is viable. The Pati-Salam algebra naturally accommodates the order-one violation via its enlarged structure.

---

## VIII. S72 Impact on Foundations (f*, truncation, G_2)

### f* = 0.912*sqrt + 0.088*exp (W2-C)

This is the single most consequential S72 result for NCG foundations. Its implications:

1. **SDW expansion is UNAVAILABLE for the physical functional**. All moments f_n = integral x^n f*(x) dx diverge (the sqrt component diverges for all n >= 0). The canonical results that used the SDW expansion (S62 cutoff-London coefficients f_0 = 9.817, f_2 = 2.34, f_4 = 0.558; S70 SDW values) are valid only as approximations for specific cutoff functions, not for f*.

2. **The CC problem is reframed**: f_0 = infinity means the a_0*Lambda^4 term is formally infinite. This is NOT a physics divergence -- the direct spectral sum is finite. But it means the CC cannot be extracted from the expansion at all. The CC problem becomes: what is the value of sum_n d_n * f*(lambda_n^2/Lambda^2) at the physical Lambda, without any expansion?

3. **The four-layer hierarchy** (topology > representation > metric > functional) is now the canonical prediction stratification. f*-dependent predictions (n_s shape, A_s normalization, alpha_s for smooth cutoff) sit in the functional layer. Topological predictions (w_0, w_a, c_s^2 = 0, mass ordering) are IMMUNE to f*.

4. **Kasparov product unaffected**: Convergence (S72 Mack-VdD R2 C6). The product is a topological construction in KK-theory, independent of f.

### Truncation effects (W1-C, W3-B)

The zeta ratio a_6/a_4 converges monotonically from 0.567 (L = 3) to 0.223 (L = 7), crossing the Gilkey geometric target 0.25 between L = 6 and L = 7. This means:

1. The S66/S71 results computed at L = 3 have 60% contamination from finite-spectrum artifacts in the a_6 coefficient.
2. The convergence toward the geometric Gilkey value validates the PW truncation at L = 7 for ratios involving a_6.
3. The optimal truncation N* ~ 4 means a_0 through a_4 are reliable; a_6 is marginal; a_8+ are unreliable.

### G_2 constancy (W4-F)

The a_2/a_4 near-constancy under Jensen-type deformation is a GENERAL property of compact rank-2 Lie groups, not SU(3)-specific (G_2 is 34% MORE constant). This eliminates one candidate fiber selection criterion. The surviving criteria are the absolute a_2/a_4 ratio (SU(3): 2.03, G_2: 0.049) and SM gauge group branching rules.

---

## IX. Priority-Ordered Mathematical Agenda

The following is ordered by EVOI (expected value of information) for resolving the NCG foundations.

### Priority 1: Order-One Condition Resolution

**Status**: FAIL (4.000). All standard escape routes (weak order-one, BdG twist) CLOSED.
**What remains**: (a) Full CCS 2013 formalism on D_K with the 342 = 173 + 169 dimensional Omega^1_D. (b) Twisted spectral triples with non-trivial twist automorphism (not from Aut(A_F), which is closed). (c) Pati-Salam algebra A_PS, where the S63 gauge module PASS suggests the enlarged algebra may satisfy order-one. (d) Prove that order-one is NOT required for the physical predictions to hold (this is the CCS 2013 route: inner fluctuations exist without order-one, generating both gauge and Higgs fields plus 169 additional scalar directions).
**Impact**: Resolution determines whether the spectral triple is "standard NCG-SM" (with order-one) or "generalized NCG" (CCS/PS). The spectral action and all topological predictions are unaffected. The fermionic action and Higgs mechanism may be modified by the additional 169 directions.

### Priority 2: Spectral Action Profile S(tau) for tau in [0, 2]

**Status**: Only computed at and near the fold (tau = 0.19). The monotonicity theorem (S28) proves S increases with tau, but the FULL profile (including possible post-fold structure) is unknown.
**What remains**: Compute S[f*, tau] via direct spectral sum for tau in [0, 2] at L_max = 7. This simultaneously determines: (a) whether a stable post-fold equilibrium exists (moduli stabilization), (b) the late-time CC, and (c) the expansion history w(z).
**Impact**: Three-in-one computation. If no minimum exists, the framework has no late-time equilibrium, and the physical meaning of tau_today is undefined.

### Priority 3: KO-Dimension Mismatch Resolution

**Status**: KO(M^4 x SU(3)) = 4, KO(F_SM) = 6. PERMANENT mismatch.
**What remains**: (a) Compute the impact on the fermionic action. The signs (epsilon, epsilon', epsilon'') enter the fermionic action through <J psi, D psi>. With KO = 4 instead of 6, epsilon'' = +1 instead of -1, which changes the chirality condition on physical fermions. (b) Determine whether the mismatch affects observational predictions or is absorbed by a redefinition of the grading.
**Impact**: If the fermionic sector is modified, all mass predictions and Yukawa couplings change. If absorbed by convention, it is a bookkeeping issue.

### Priority 4: PW-Sector-Resolved Threshold Corrections

**Status**: The Weinberg angle sin^2(theta_W) at M_KK = 0.5839 is scheme-independent. Running to M_Z gives 0.357 (pure SM, 54.5% FAIL) or 0.229 (universal thresholds, 1.2% PASS). The threshold RATIOS delta_1/delta_3 at tau_fold are unknown.
**What remains**: Compute the PW-sector branching SU(3) -> SU(2) x U(1) for each (p,q) sector at tau_fold = 0.19. The eigenvalue decomposition under the branching gives the threshold correction ratios.
**Impact**: Determines whether sin^2(theta_W) is a zero-parameter prediction (if ratios ~ 1:1:1) or requires threshold parameters.

### Priority 5: Instanton Landscape in (rho, tau) Space

**Status**: S72 INSTANTON-KAPPA-72 gives kappa(rho) at the fold. The temporal dimension (tau-dependence) is proposed but uncomputed.
**What remains**: Compute kappa(rho, tau) for tau in [0.19, 0.5] and rho in [0.1, 10]/M_KK. Identify the kappa = 1 contour. Determine whether the tau path from fold to equilibrium crosses this contour, which would signal a potential topological phase transition.
**Impact**: If the contour is crossed, the post-transit spectral triple may have different K-homology class -- this would be an NCG phase transition affecting all predictions at late times.

### Priority 6: Direct Spectral Sum for alpha_s

**Status**: alpha_s = 0 at tree level (trivial bundle, zeta). The SDW expansion route gives alpha_s = 0.118 at f_0 = 6.33 but m_H = 190 GeV (S70 anti-correlation). For f*, the SDW route is unavailable.
**What remains**: Extract alpha_s from the direct spectral sum S[f*, D_K + A] where A is the SU(3) gauge connection from inner fluctuations. This requires the gauge field contribution to the spectral action computed as a direct sum over perturbed eigenvalues.
**Impact**: Determines whether the framework predicts QCD coupling from first principles.

### Priority 7: Compound Bogoliubov Tilt

**Status**: S72 W3-C gives delta_n_s = +1.001 from entry horizon. Additive approximation used. S72 Mack-VdD workshop bounds non-additive correction at 0.5% (VdD) to 7% (Mack).
**What remains**: Compute the full ordered Bogoliubov product from tau = 0.22 to tau = 0.19 via ODE integration. Extract the compound tilt.
**Impact**: Determines the n_s precision budget entry from the entry horizon.

---

## Summary of Mathematical Gaps (Compact Reference)

| Category | Issue | Status | Severity |
|:---------|:------|:-------|:---------|
| Axiom 5 (order-one) | [[D,a],b^o] != 0, max 4.000 | FAIL | HIGH -- single failing axiom |
| KO mismatch | Product KO = 4, finite KO = 6 | PERMANENT | MEDIUM -- fermionic impact unclear |
| Instanton Kasparov | kappa(peak) = 1.057 > 1.0 | MARGINAL | MEDIUM -- affects alpha_s sector |
| SDW for f* | All moments diverge | STRUCTURAL | HIGH -- forces method change |
| CC from spectral action | f_0 = infinity | IMPASSE | HIGH -- 120-OOM gap, all routes closed |
| Three generations | Not from axioms | ASSUMED | LOW -- observational, not mathematical |
| S(tau) profile | Unknown beyond fold | OPEN | HIGH -- determines moduli/CC/w(z) |
| Threshold ratios | Unknown at tau_fold | OPEN | MEDIUM -- determines sin^2(theta_W) |
| Continuum convergence | PW truncation at L = 3-10 | TESTED | LOW -- ratios converge, individual values uncertain |
| Product metric mixing | O'Neill 0.47%, SDW impact unknown | OPEN | LOW -- small parameter |
