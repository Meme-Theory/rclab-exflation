# Connes -- Collaborative Feedback on Session 25

**Author**: Connes-NCG-Theorist
**Date**: 2026-02-21
**Re**: Session 25 -- Through the Walls

---

## Section 1: Key Observations

The Session 25 directive asks us to move from defense to exploration. From the NCG standpoint, I read this through the lens of the spectral action principle (Paper 07, Chamseddine-Connes 1996) and its asymptotic expansion. The four walls (W1-W4) are, in spectral-theoretic language, statements about what functionals of the Dirac spectrum can and cannot do:

**W1 (Perturbative Exhaustion)** is a consequence of Weyl's law applied to the Dirac operator D_K on an 8-dimensional compact Riemannian manifold. Weyl's law guarantees that the eigenvalue counting function N(Lambda) ~ c * Lambda^8 for large Lambda, with the constant c determined by volume and fiber dimension. The fiber dimension ratio (bosonic 44 vs fermionic 16) gives F/B = 4/11 asymptotically. This is a theorem about the SPECTRUM -- it is spectral geometry at its most fundamental. Any smooth test function f integrated against this spectrum inherits the monotonicity from the asymptotic dominance of one sign.

**W2 (Block-Diagonality)** is the Peter-Weyl decomposition theorem applied to D_K. For any left-invariant metric on a compact Lie group, the Dirac operator decomposes into independent blocks indexed by irreducible representations. This is representation theory, not dynamics. It is as immovable as the structure theory of compact groups.

**W3 (Spectral Gap)** reflects the fact that D_K on a compact positively-curved manifold has a gap bounded below by the Lichnerowicz estimate: lambda_min >= sqrt(n/(4(n-1))) * R_min^{1/2}. On SU(3) with Jensen deformation, 2*lambda_min = 1.644. The BCS mechanism requires gapless excitations -- a Fermi surface. This is a conflict between compact spectral geometry and condensed matter physics.

**W4 (V_spec Monotone)** is the statement that in the Seeley-DeWitt expansion of Tr f(D_K^2/Lambda^2), the a_4 curvature-squared coefficient dominates a_2 by 1000:1 at the round metric. The coefficients a_k are computed from the Gilkey formulas (Paper 06, Connes-Moscovici 1995). For D^2 = nabla*nabla + R/4 on 16-dimensional spinors in 8 dimensions, the a_4 coefficient involves tr(E^2) = tr(R^2/16) = R^2/16 * dim_spinor = R^2, and the curvature endomorphism Omega_{ij} = (1/4)R_{ijkl}gamma^{kl} gives tr(Omega^2) = -2|Riem|^2 (Session 20a SD-1 verified this trace identity). The large dim_spinor = 16 inflates every trace in a_4, producing the 1000:1 dominance.

What strikes me most, reading this through the spectral paradigm, is that all four walls are SPECTRAL theorems. They are properties of the spectrum of D_K as a self-adjoint operator on L^2(SU(3), S). The walls define the boundary of what smooth functionals of Spec(D_K) can achieve. But smooth functionals are not the ONLY quantities that depend on the spectrum. There are quantities that depend on spectral DATA beyond eigenvalue magnitudes -- eigenvector correlations, spectral flow, Berry holonomy, eta invariants -- and these are precisely what Session 25 proposes to compute.

---

## Section 2: Assessment of Key Findings

### Goals 1-3 (Tier 1): NCG Evaluation

**Goal 1 (Graded Multi-Sector Spectral Sum)**: This is the computation I find most interesting from the NCG standpoint. The directive correctly identifies that the (-1)^F grading is the chirality grading gamma_9 within the spinor bundle. However, I must flag a structural issue.

For the Dirac operator D_K on SU(3), the BDI symmetry class (T^2 = +1, Session 17c) guarantees that eigenvalues come in (lambda, -lambda) pairs. The chiral grading gamma_9 anticommutes with D_K (this is the defining property of the grading: {gamma_9, D_K} = 0 in even dimensions). Therefore:

Tr(gamma_9 * f(D_K^2/Lambda^2)) = 0 EXACTLY.

This is because D_K^2 commutes with gamma_9 (since {gamma_9, D_K} = 0 implies [gamma_9, D_K^2] = 0), so f(D_K^2/Lambda^2) also commutes with gamma_9, and Tr(gamma_9 * A) = 0 for any A that commutes with gamma_9 when Tr(gamma_9) = 0 (which holds because dim(H+) = dim(H-) for the grading).

The directive anticipates this: "If this formulation gives zero by spectral symmetry (as it might for BDI)..." and proposes the THERMAL graded sum as alternative. But the thermal graded sum -- weighting different sectors by their representation dimensions d_{(p,q)} -- is not a "grading" in the NCG sense. It is a WEIGHTED sum over sectors, where the weights come from representation theory (not from any chirality operator). The competition between sectors with different spectral densities is physically real (it is how the Casimir effect works), but calling it "graded" is misleading.

From the NCG perspective, the relevant graded quantity is the SPECTRAL ASYMMETRY, which leads to Goal 4 (eta invariant). I will return to this.

The sector-weighted sum S_eff(tau) = sum d_{(p,q)} * V_{(p,q)}(tau) is still worth computing. Different sectors have different gap-edge behavior (bosonic gap fraction 4/9 vs fermionic 5/6 at tau=0), and the sector-specific spectral actions have genuinely different tau-dependence at low eigenvalue count. But note: the Perturbative Exhaustion theorem (W1) applies to EACH SECTOR individually (Weyl's law operates within each representation space). The sum over sectors does not escape W1 unless the test function or the grading introduces sign alternation. Without a physical (-1)^F grading that distinguishes sectors (which block-diagonality, W2, prevents from being a coupling), this remains a sum of monotone functions weighted by positive integers.

My assessment: P(success) is at the low end of the stated 10-15%, closer to 5%. The Casimir-like cancellation requires opposite signs, and all sector contributions carry the same sign in the bosonic spectral action.

**Goal 2 (Full Spectral Action at Finite Cutoff)**: This is the computation that most directly tests the central claim of Paper 07 (Chamseddine-Connes 1996). The spectral action is DEFINED as Tr f(D^2/Lambda^2) -- the asymptotic expansion is an APPROXIMATION, not a definition. The expansion is asymptotic in the precise mathematical sense: it diverges at finite order, and for finite Lambda the true value can differ from any truncation.

From Paper 14 (Section 5.3), Connes explicitly states: "At 'low temperature' (small Lambda), only the lowest eigenvalues contribute and the fine structure of the spectrum matters." This is the regime the directive proposes to explore. The Berry curvature B = 982.5 at tau = 0.10 is a direct signal that the spectrum has fine structure (near-degeneracies) invisible to the heat kernel expansion.

The test function f(x) = x*exp(-x) proposed is the standard Chamseddine-Connes choice. Computing V_full(tau; Lambda) = sum_n f(lambda_n^2/Lambda^2) is finite, well-defined, and requires no new theory. If V_full differs from V_HK by more than 20% at Lambda <= 5, we learn that W4 is an artifact of the asymptotic truncation at those scales.

My assessment: This is the cleanest computation. The result -- whether positive or negative -- is unambiguous. P(success) ~ 8-12% is reasonable. The 1000:1 a_4/a_2 ratio suggests the asymptotic expansion is badly behaved, which could mean the full sum behaves differently.

**Goal 3 (Berry Phase Accumulation)**: Berry curvature is NOT a standard NCG concept, but it connects to the NCG framework through the adiabatic theorem for families of Dirac operators. When the Dirac operator D_K(tau) varies with a parameter tau, the eigenstates trace out paths in the Hilbert space, and the Berry connection A(tau) = i * <n|d/dtau|n> measures the rate of rotation.

In the NCG context, the Berry phase is related to the SPECTRAL FLOW -- the number of eigenvalues that cross zero as the parameter varies. For a family of self-adjoint Fredholm operators D(t), the spectral flow sf(D(t), t in [0,1]) is a topological invariant that contributes to the index via the Atiyah-Patodi-Singer theorem.

The Berry curvature B = 982.5 at tau = 0.10 is large enough that non-adiabatic corrections to the effective action (which goes as exp(-Delta_E^2/(dE/dtau))) could be significant. With gap Delta_E = 0.822 and the near-crossing rate implied by B ~ 1000, these corrections warrant computation.

My assessment: The Berry phase computation is sound but addresses a question outside the standard spectral action framework. The spectral action Tr f(D^2/Lambda^2) is defined for a FIXED operator D, not for a family. The dependence on tau enters through D_K(tau), and the adiabatic approximation is implicit in treating V_eff(tau) as a classical potential. If the Berry phase reaches pi, the adiabatic approximation breaks -- but this tells us the effective potential picture is inadequate, not that a minimum exists.

### Goals 4-8 (Tier 2-3): NCG Evaluation

**Goal 4 (Spectral Flow / Eta Invariant)**: This is the goal I find most promising from the NCG standpoint. The eta invariant:

eta(D) = sum_n sign(lambda_n) * |lambda_n|^{-s} |_{s=0}

measures spectral asymmetry -- the difference between the number of positive and negative eigenvalues, weighted by their magnitudes. For the full Dirac operator D_K on SU(3), the BDI symmetry with the time-reversal T (satisfying T^2 = +1) forces eigenvalue pairing (lambda, -lambda), giving eta = 0 identically.

BUT -- and this is the critical point -- the spectral flow of the FAMILY {D_K(tau)} is NOT zero in general. The spectral flow counts eigenvalue crossings through zero. Even if no individual eigenvalue of D_K crosses zero (which is guaranteed in the (0,0) singlet by the Lichnerowicz bound), eigenvalues in higher sectors (p,q) with p+q >= 1 could cross zero if the curvature contribution becomes sufficiently negative.

From the Atiyah-Patodi-Singer index theorem (1975), the spectral flow contributes a topological term to the effective action that is invisible to the heat kernel expansion. This evades W1 (non-perturbative), W2 (sector-independent), W3 (gap-irrelevant for sectors where eigenvalues DO cross zero), and W4 (invisible to Seeley-DeWitt).

The computation is straightforward: check whether any eigenvalue in any sector crosses zero for tau in [0, 0.5]. This requires eigenvalue data for sectors (p,q) with p+q >= 1, which exists in s23a_eigenvectors_extended.npz.

**Goal 5 (Gap-Edge Topological Protection)**: The selection rule V(gap,gap) = 0 is intriguing. In NCG, zero matrix elements often reflect commutant conditions. If the gap-edge state |gap> satisfies <gap|K_a|gap> = 0 for all Killing vectors K_a, then |gap> is in the trivial representation of the isometry group restricted to the gap-edge subspace. This is a form of SYMMETRY PROTECTION.

The Berry connection matrix for the gap-edge Kramers pair defines a U(2) gauge field on the tau parameter space. If the holonomy (Wilson loop) is non-trivial, it would indicate topological protection analogous to Z_2 topological insulators.

**Goal 7 (Self-Consistent Chemical Potential)**: From the NCG standpoint, introducing a chemical potential mu modifies the Dirac operator: D -> D - mu*gamma_0. In the KK decomposition, this affects the 4D part, not the internal part. The spectral action becomes Tr f((D - mu*gamma_0)^2/Lambda^2), which is a THERMAL spectral action.

The backreaction equation proposed -- mu_eff ~ sqrt(rho_4/M_KK^2) -- is physically motivated but not derived from the spectral action formalism. A rigorous NCG derivation would require computing the spectral action for the full 12D Dirac operator D_{12} = D_4 tensor 1 + gamma_5 tensor D_K with a non-zero Matsubara frequency.

**Goal 8 (Higher Heat Kernel Coefficients)**: The Seeley-DeWitt coefficients a_6 and a_8 on Jensen-deformed SU(3) are computable in principle from the Gilkey formulas, but the expressions involve higher-order curvature invariants (R^3 for a_6, R^4 for a_8) that require the full Riemann tensor at each tau. Session 20a already computed the Riemann tensor in the Peter-Weyl basis (R-1), so the input data exists. The Gilkey formulas for a_6 involve 17 independent curvature invariants; for a_8, approximately 90.

---

## Section 3: Collaborative Suggestions

### 3.1 The Eta Invariant Computation (Priority 1)

The computation I recommend most strongly is NOT in the Tier 1 goals but in Tier 2: the spectral flow / eta invariant (Goal 4). Here is why, and here is how to do it rigorously.

The spectral action has TWO parts (Paper 07, Section 2.1):

S = Tr f(D^2/Lambda^2) + (1/2)<J*psi, D*psi>

The bosonic part Tr f(D^2/Lambda^2) is what we have been computing as V_spec. But the FERMIONIC part <J*psi, D*psi> also depends on tau through D_K(tau). For a family of Dirac operators, the one-loop fermionic effective action acquires an ANOMALOUS contribution from the eta invariant:

Gamma_ferm[tau] = -(1/2) * eta(D_K(tau)) + (spectral-action-like terms)

The eta invariant contribution is TOPOLOGICAL -- it jumps by integers when eigenvalues cross zero. This is the Atiyah-Patodi-Singer spectral flow. Even a single zero-crossing in a single sector would create a step-function contribution to the effective action that no heat kernel expansion captures.

The concrete computation: for each sector (p,q) with eigenvalue data available, track every eigenvalue as tau varies from 0 to 2.0 in the existing 21-point grid. Count zero crossings. If any eigenvalue changes sign, compute the spectral flow index sf = (number of upward crossings) - (number of downward crossings).

This costs nothing beyond reading existing data. The result is binary: either sf = 0 (in which case this path closes) or sf != 0 (in which case we have found a topological contribution to the effective action that evades all four walls).

### 3.2 The Full Spectral Action: Correct Implementation (Priority 2)

For Goal 2, I want to specify precisely what the NCG framework says the computation should be. The spectral action Tr f(D^2/Lambda^2) on the product geometry M^4 x K decomposes (using the product structure D = D_4 tensor 1 + gamma_5 tensor D_K) as:

Tr f(D^2/Lambda^2) = sum_{n,m} f((lambda_n^{(4)} + lambda_m^{(K)})^2 / Lambda^2)

where lambda_n^{(4)} are the 4D Dirac eigenvalues and lambda_m^{(K)} are the internal eigenvalues. After integrating over the continuous 4D spectrum (which produces the Seeley-DeWitt coefficients of the 4D part), the effective potential for tau is:

V_eff(tau) = sum_m g(lambda_m^{(K)}(tau)^2 / Lambda^2)

where g is a modified test function absorbing the 4D integration. For f(x) = x*exp(-x), the function g is explicitly computable. The key point: g is NOT the same as f. The 4D integration modifies the weighting.

I recommend computing V_full(tau; Lambda) = sum_m f(lambda_m(tau)^2/Lambda^2) as specified in the directive (this is the INTERNAL spectral action only), but ALSO computing V_eff^{full}(tau; Lambda) = sum_m g(lambda_m(tau)^2/Lambda^2) with the properly dimensionally-reduced test function. The difference between these two quantities measures the effect of 4D integration on the tau-potential.

### 3.3 The Graded Sum: Use the Index Pairing (Priority 3)

For Goal 1, instead of the thermal graded sum (which is physically motivated but not NCG-canonical), I propose computing the INDEX PAIRING. In NCG, the Chern character pairs with K-theory:

<[D], [e]> = index(e*D*e) = integer

where e is a projection in the algebra. For the Peter-Weyl decomposition of SU(3), each sector (p,q) defines a projection e_{(p,q)} onto the (p,q) subspace. The index pairing <[D_K(tau)], [e_{(p,q)}]> is an integer that can change only when eigenvalues cross zero -- it is PIECEWISE CONSTANT in tau.

Computing this for all sectors with p+q <= 6 gives a "topological phase diagram" of the Jensen deformation. Changes in the index pairing signal topological phase transitions that are invisible to the spectral action.

### 3.4 The Random NCG Perspective (Novel Suggestion)

Paper 14 (Section 8.2) proposes the random NCG integral:

Z = integral dD * exp(-Tr f(D^2/Lambda^2))

where D ranges over all Dirac operators compatible with the spectral triple structure. In our context, D_K(tau) parameterizes a ONE-DIMENSIONAL subspace of the space of all compatible Dirac operators (the Jensen deformation). But the MEASURE dD on the full space of Dirac operators is not the Lebesgue measure d(tau) on the parameter space.

The Jacobian of the map tau -> D_K(tau) is:

J(tau) = |det(dD_K/dtau)|

If J(tau) has a sharp peak at some tau_0 > 0, the random NCG measure would favor tau_0 even if V_spec is monotone. This is the "entropic stabilization" mechanism: the number of spectral geometries compatible with a given tau could peak away from tau = 0.

The computation requires: (1) the derivative dD_K/dtau at each tau (which we have from the Kosmann derivative data), and (2) the functional determinant of the map. For a matrix-truncated version (finite N modes), this reduces to det(dD_N/dtau), which is computable from the existing matrix representations.

This suggestion was identified in Session 22 (P5 in the priority list) but never computed. It directly uses Connes' own framework from Paper 14 and costs nothing beyond existing data.

### 3.5 The Chern-Simons Term (Novel Suggestion)

For odd-dimensional manifolds, the spectral action has a natural companion: the Chern-Simons functional. SU(3) is 8-dimensional (even), so the standard Chern-Simons does not apply directly. But the BOUNDARY of the Jensen deformation space [0, infinity) IS odd-dimensional (it is a half-line, with boundary at tau = 0).

The Atiyah-Patodi-Singer boundary correction to the spectral action on a manifold-with-boundary involves the eta invariant at the boundary. If we view the parameter space as a "moduli manifold" with tau = 0 as a boundary, the effective action acquires:

S_eff(tau) = V_spec(tau) + (1/2)*eta(D_K(0)) - (1/2)*eta(D_K(tau))

The eta terms are generically non-zero (even though the full spectrum is symmetric, the TRUNCATED spectrum -- with finite max_pq_sum -- need not be). This boundary correction is a topological contribution that the Seeley-DeWitt expansion does not capture.

---

## Section 4: Connections to Framework

The Session 25 computations connect to the NCG Standard Model derivation at several levels:

1. **The spectral action at finite cutoff (Goal 2) tests the convergence of the asymptotic expansion that underlies the ENTIRE NCG-SM derivation.** Papers 07 and 10 (CCM 2007) compute the SM Lagrangian from the Seeley-DeWitt coefficients a_0, a_2, a_4. If the expansion is unreliable on the internal space at finite Lambda (as the 1000:1 ratio at a_4/a_2 suggests), the coefficients we use for the SM derivation may need finite-Lambda corrections. This is not merely a question for the phonon-exflation framework -- it is a question for the NCG Standard Model itself. A result showing V_full != V_HK at moderate Lambda would be a contribution to NCG independent of this project.

2. **The spectral flow (Goal 4) is the NCG mechanism for anomaly cancellation.** Paper 10 (Section 4.3) shows that anomaly cancellation in the NCG-SM is AUTOMATIC: Tr(Y) = 0 and Tr(Y^3) = 0 follow from the bimodule structure of H_F. But this refers to the PERTURBATIVE anomaly. The non-perturbative anomaly -- which involves the spectral flow of the Dirac operator family -- has not been computed for D_K(tau). A non-trivial spectral flow would signal a GRAVITATIONAL anomaly in the internal space, with potential physical consequences.

3. **The sigma field identification (Paper 13) remains the deepest structural claim.** Paper 13 identifies the sigma field as a gauge singlet scalar from the Majorana sector of D_F. In the phonon-exflation framework, sigma = fluctuations of tau around tau_0. But Session 22c (Trap 3) showed that lambda_{H,sigma} is exactly constant -- a structural closure on the Higgs-sigma portal dynamics. This means: even if tau_0 exists (which V_spec says it does not), the sigma field would not communicate with the Higgs sector through the channel Connes proposed. The sigma field, if it exists, must interact with the Higgs through a mechanism beyond tree-level spectral action.

4. **The classification theorem (Paper 12) constrains extensions.** Any attempt to rescue the framework by extending the algebra A_F must respect Barrett's classification: A subset M_n(C) + M_n(C) at KO-dim 6. The Pati-Salam algebra M_2(H) + M_4(C) is the maximal choice. Extending beyond this violates the axioms.

---

## Section 5: Open Questions

1. **Does the asymptotic expansion of the spectral action on SU(3) converge at ALL?** The 1000:1 ratio a_4/a_2 is a WARNING signal. The Seeley-DeWitt expansion is asymptotic, not convergent -- the coefficients a_k grow factorially with k. If the expansion diverges already at k=4 for the internal space (as the 1000:1 ratio suggests), then the spectral action is fundamentally a FINITE SUM over eigenvalues, not a heat kernel series. This changes the entire framework: V_eff is not a polynomial in curvature invariants, but a sum over a finite number of eigenvalues, each contributing f(lambda_n^2/Lambda^2). This is the "inside-out view" (Claim A) stated precisely.

2. **Is the spectral action at finite Lambda the correct physical object?** Paper 14 (Section 5) identifies Tr f(D^2/Lambda^2) as a partition function with Lambda^{-2} playing the role of inverse temperature. At finite temperature, the partition function has DIFFERENT extrema than the free energy at zero temperature. The ground state (tau_0) of the finite-Lambda spectral action could differ from the ground state of the asymptotic (Lambda -> infinity) expansion. This is the physical content of Goal 2.

3. **What is the correct (-1)^F for the sector-weighted sum?** In the NCG-SM, the (-1)^F grading is the chirality gamma_5 tensor gamma_F, which acts on H = H_4 tensor H_F. On the internal space alone, the grading is gamma_F (= gamma_9 for SU(3)). The PHYSICAL grading -- which distinguishes bosons from fermions in the 4D effective theory -- arises from the tensor product structure, not from gamma_9 alone. The inter-sector grading would require identifying which (p,q) representations contribute to bosonic vs fermionic 4D fields. This is determined by the Baptista fiber integration (Paper 14 of the Baptista corpus), which maps spinor harmonics on SU(3) to 4D fields of definite spin. Without this identification, the "graded sum" is ill-defined.

4. **What role does the Dixmier trace play at finite N?** The noncommutative integral (Paper 01, Paper 02) is defined as Tr_omega(a|D|^{-n}) = lim (1/log N) sum_{j<N} mu_j. At finite max_pq_sum = 6, we have N ~ 11,000 eigenvalues. The Dixmier trace at finite N is not well-defined (it requires the N -> infinity limit). But the RATIO of Dixmier traces at different tau values could still be meaningful as a shape diagnostic. Computing Tr_omega(|D_K(tau)|^{-8}) / Tr_omega(|D_K(0)|^{-8}) for the existing eigenvalue data would give a noncommutative-integral-normalized shape comparison.

5. **Can the order-one condition ever be tested?** Session 22c (C-2) showed that the Baptista-Connes representation mismatch blocks the order-one test: [[D_K, a_F], J b_F J^{-1}] = 0 cannot be verified because the Baptista algebra representation and the Connes algebra representation on C^16 are not unitarily equivalent (different characters). This is the DEEPEST open structural gap. Without resolving it, the phonon-exflation spectral triple is not a verified spectral triple in the Connes sense -- it is a spectral triple candidate.

---

## Closing Assessment

The Session 25 directive is well-conceived from the NCG standpoint. The shift from "find a potential minimum" to "explore spectral quantities beyond the heat kernel" aligns with the fundamental insight of Paper 14: geometry is spectrum, and the spectrum contains more information than any polynomial approximation.

My ranking of the proposed computations, from the NCG perspective:

1. **Spectral flow (Goal 4)**: Topological, evades all walls, costs nothing. Binary result.
2. **Full spectral action at finite Lambda (Goal 2)**: Tests the core NCG computation. Clean, definitive.
3. **Random NCG Jacobian (my suggestion 3.4)**: Uses Connes' own framework from Paper 14. Novel.
4. **Berry phase (Goal 3)**: Sound physics but outside standard NCG.
5. **Sector-weighted sum (Goal 1)**: Likely zero by symmetry or monotone by W1. Lowest priority.

**Probability assessment**: The framework stands at 3-5% (Sagan/Panel). The Tier 1 computations collectively have perhaps a 15-20% chance of finding something non-monotone, with the strongest prospects from the full spectral action at finite Lambda and the spectral flow. If ALL computations return null, the probability drops to approximately 1.5%, and the framework becomes pure mathematics -- publishable and valuable as spectral geometry, but not physics.

At 3%, I am asked whether the framework could still be correct. From the NCG standpoint, I note this: the NCG-SM itself (Papers 07-14) does not address modulus stabilization. It assumes the product geometry M^4 x F exists and derives the SM from it. The question of WHY the internal space takes its particular shape -- why A_F = C + H + M_3(C) and not something else -- is answered by the classification theorem (Paper 12). But the question of why the METRIC on the internal space is what it is -- the dynamical question -- is open in Connes' own program. The phonon-exflation framework's failure to stabilize tau is, in a sense, the same failure as the NCG-SM's silence on the shape modulus. The difference is that the NCG-SM never claimed to address this question, while the phonon-exflation framework made stabilization its central claim and has now failed 18 times.

The mathematical structure -- KO-dim 6, SM quantum numbers, block-diagonality, three algebraic traps -- is permanent. It belongs to spectral geometry on compact Lie groups, and it will outlive any physical interpretation. Whether it also describes our universe is a question that three more computations may resolve, or may leave forever open.

The spectral action was always the right question. The asymptotic expansion may have been the wrong answer.

---

*Connes-NCG-Theorist, 2026-02-21. "The action depends only on the spectrum." -- Paper 07, opening line. The question is no longer whether the principle is true, but whether we have been reading the spectrum correctly.*
