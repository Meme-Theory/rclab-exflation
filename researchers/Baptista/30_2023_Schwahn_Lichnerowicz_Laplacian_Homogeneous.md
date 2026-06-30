# The Lichnerowicz Laplacian on Normal Homogeneous Spaces

**Author(s):** Paul Schwahn
**Year:** 2023 (revised 2024)
**Journal:** [Not stated in PDF]
**arXiv:** 2304.10607
**Relevance:** CRITICAL (51 new stable Einstein examples; exact Casimir formula for Delta_L; directly determines Jensen stability)

---

## Abstract

We give a new formula for the Lichnerowicz Laplacian on normal homogeneous spaces in terms of Casimir operators. We derive some practical estimates and apply them to the known list of non-symmetric, compact, simply connected homogeneous spaces G/H with G simple whose standard metric is Einstein. This yields many new examples of Einstein metrics which are stable in the Einstein-Hilbert sense, which have long been lacking in the positive scalar curvature setting.

---

## Key Arguments and Derivations

### 1. Introduction and Context (Section 1)

The Lichnerowicz Laplacian Delta_L = nabla*nabla + K(R) acts on tensor fields. For Einstein metrics with Ric = Eg, the stability condition is Delta_L > 2E on S^2_tt(M). For a long time, no non-symmetric examples of stable positive scalar curvature Einstein metrics were known. This paper produces 107 new examples.

**Key classes of normal homogeneous Einstein manifolds with G simple:**
1. Irreducible symmetric spaces (Cartan, 1927)
2. Strongly isotropy irreducible spaces (Wolf, 1968)
3. Non-symmetric, non-strongly isotropy irreducible normal homogeneous Einstein manifolds (Wang-Ziller, 1985)

### 2. Decomposition of Delta_L (Section 3, Lemma 3.1)

On Sym^p(M) for a normal homogeneous space:

**Lemma 3.1:** Delta_L = Delta_bar + A* nabla_bar + (1/2) A*A

where Delta_bar = nabla_bar* nabla_bar + K(R_bar) is the standard Laplacian of the canonical reductive connection, and A is the tensor field measuring failure to be locally symmetric.

Key fact: On normal homogeneous spaces, Delta_bar = Cas^g_ell (the Casimir operator of the left-regular representation), by Eq. (7).

### 3. The Exact Casimir Formula (Section 3, Corollary 3.5)

**Corollary 3.5 (Main Formula):** If (M,g) is Einstein, then on C^infty(G, Sym^p m)^H:

Delta_L = (3/2) Cas^g_ell + pr_{Sym^p m}(Cas^g_{Sym^p g} - (1/2) Cas^g_{ell otimes Ad^{otimes p}}) - (3/2) Cas^h_{Sym^p m} - pE + p/4

This reduces the Lichnerowicz Laplacian entirely to Casimir operators, making its spectrum a representation-theoretic computation.

### 4. The Crude Estimate (Theorem 3.6)

For any Fourier mode gamma in hat{G}:

Delta_L|_gamma >= Cas^g_gamma + (1/2) lambda_min[A*A] - sqrt{lambda_max[A*A] . (Cas^g_gamma - lambda_min[Cas^h_{Sym^p m}])}

This rules out all but finitely many Fourier modes as candidates for instabilities.

### 5. The Refined Estimate (Theorem 3.7)

A sharper bound using the full structure of the Casimir formula, applicable mode-by-mode to the finitely many candidates identified by the crude estimate.

### 6. Algorithm and Results (Sections 6-7)

**Algorithm 6.1:** Systematic procedure combining crude + refined estimates:
1. Compute fibrewise data (A*A eigenvalues, Casimir constants) once
2. Apply crude estimate to rule out all but finitely many Fourier modes
3. Apply refined estimate to each remaining mode
4. Identify potential destabilizing modes

**Results (107 stable examples total):**
- 51 members of isotropy irreducible families I, II, III, VII, IX (Tables 1, 5)
- 22 members of isotropy reducible families XV, XVI, XVIIa (Tables 2, 8), including full flag manifolds SO(2n)/T^n
- 18 isotropy irreducible exceptional spaces (Tables 3, 4)
- 16 isotropy reducible exceptional spaces (Table 6)

### 7. Key Intermediate Results

**Lemma 3.2 (A*A formula):** On m^{otimes p}:
A*A = pr_{m^{otimes p}} Cas^g_{g^{otimes p}} - Cas^h_{m^{otimes p}} - Der(Cas^h_m)

**Lemma 3.4 (A*nabla_bar formula):** On C^infty(G, m^{otimes p})^H:
A*nabla_bar = (1/2) Cas^g_ell + (1/2) pr_{m^{otimes p}}(Cas^g_{g^{otimes p}} - Cas^g_{ell otimes Ad^{otimes p}}) - Cas^h_{m^{otimes p}}

**Corollary 3.3:** If (M,g) is Einstein with constant E, on m^{otimes p}:
A*A = pr_{m^{otimes p}} Cas^g_{g^{otimes p}} - Cas^h_{m^{otimes p}} - 2pE + p/2

### 8. tt-Tensors and Killing Fields (Section 5)

The short exact sequence relating tt-tensors, symmetric 2-tensors, and conformal Killing fields:

0 -> ker(theta) -> Omega^1(M) -> S^2_0(M) -> S^2_tt(M) -> 0

This allows a dimension formula for the tt-eigenspaces in terms of eigenspaces on 1-forms and trace-free symmetric 2-tensors.

---

## Key Results

1. **Corollary 3.5**: Exact formula for Delta_L on normal homogeneous spaces purely in terms of Casimir operators. First such formula extending Koiso's symmetric space result.

2. **107 new stable Einstein metrics** of positive scalar curvature on non-symmetric homogeneous spaces, disproving the prior belief that such examples are scarce.

3. **Crude Estimate** (Theorem 3.6): Universal lower bound on Delta_L using only the Casimir eigenvalue and fibrewise A*A data, reducing the stability check to finitely many modes.

4. **Refined Estimate** (Theorem 3.7): Sharper mode-by-mode bound from the full Casimir formula.

5. **E_7/PSO(8) confirmed stable**: Previously established G-stable, now proved fully stable (first p.s.c. example).

6. **Sufficient criterion**: K(R) > E on trace-free symmetric 2-tensors implies stability (from estimate (1): Delta_L >= 2K(R) on S^2_tt).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Lichnerowicz Laplacian | $\Delta_L = \nabla^*\nabla + K(R)$ | Sec. 2.1 |
| Delta_L decomposition | $\Delta_L = \bar{\Delta} + A^*\bar{\nabla} + \frac{1}{2}A^*A$ | Lemma 3.1 |
| Casimir = reductive Laplacian | $\bar{\Delta} = \mathrm{Cas}^{\mathfrak{g}}_\ell$ | Eq. (7) |
| Main Casimir formula | $\Delta_L = \frac{3}{2}\mathrm{Cas}^{\mathfrak{g}}_\ell + \mathrm{pr}\left(\mathrm{Cas}^{\mathfrak{g}}_{\mathrm{Sym}^p\mathfrak{g}} - \frac{1}{2}\mathrm{Cas}^{\mathfrak{g}}_{\ell\otimes\mathrm{Ad}^{\otimes p}}\right) - \frac{3}{2}\mathrm{Cas}^{\mathfrak{h}}_{\mathrm{Sym}^p\mathfrak{m}} - pE + \frac{p}{4}$ | Cor. 3.5 |
| Crude estimate | $\Delta_L\big|_\gamma \geq \mathrm{Cas}^{\mathfrak{g}}_\gamma + \frac{1}{2}\lambda_{\min}[A^*A] - \sqrt{\lambda_{\max}[A^*A]\cdot(\mathrm{Cas}^{\mathfrak{g}}_\gamma - \lambda_{\min}[\mathrm{Cas}^{\mathfrak{h}}_{\mathrm{Sym}^p\mathfrak{m}}])}$ | Thm 3.6 |
| Stability criterion | $\Delta_L > 2E$ on $S^2_{\mathrm{tt}}(M)$ | Sec. 1 |
| Fibrewise shortcut | $\Delta_L \geq 2K(R)$ on $S^2_{\mathrm{tt}}(M)$ | Eq. (1) |
| Einstein from Casimir | Standard metric Einstein iff $\mathrm{Cas}^{\mathfrak{h}}_{\mathfrak{m}}$ has one eigenvalue $c = 2E - \frac{1}{2}$ | Sec. 2.3 |
| Freudenthal formula | $\mathrm{Cas}^{\mathfrak{g},Q}_\lambda = Q^*(\lambda, \lambda + 2\delta_{\mathfrak{g}})$ | Eq. (3) |
| A*A on Einstein space | $A^*A = \mathrm{pr}\,\mathrm{Cas}^{\mathfrak{g}}_{\mathfrak{g}^{\otimes p}} - \mathrm{Cas}^{\mathfrak{h}}_{\mathfrak{m}^{\otimes p}} - 2pE + \frac{p}{2}$ | Cor. 3.3 |

---

## Relevance to Phonon-Exflation

This paper is **the most directly applicable** of the stability trilogy (Papers 28-30) to the framework:

1. **SU(3) as a normal homogeneous space**: The standard (bi-invariant) metric on SU(3) is Einstein and normal homogeneous. Schwahn's Casimir formula (Corollary 3.5) gives the exact Lichnerowicz Laplacian spectrum, reducible to pure representation theory. This can be evaluated for the SU(3) fiber to determine whether the Jensen deformation endpoint is stable.

2. **Casimir-based computation**: The formula Delta_L = (3/2)Cas^g_ell + corrections means the Lichnerowicz spectrum is computable from the same Casimir data (SU(3) representations, branching rules) already used in the framework's Dirac operator analysis. No new geometric input is needed beyond what the project already has.

3. **Crude estimate for finiteness**: The crude estimate (Theorem 3.6) guarantees that only finitely many Fourier modes can potentially destabilize the Einstein metric. This converts the stability question from an infinite-dimensional spectral problem to a finite computation, directly implementable in computations scripts.

4. **107 stable examples as context**: The existence of 107 stable positive-curvature Einstein metrics (including some on SU(n) quotients) establishes that stability of the standard metric is not merely a symmetric space phenomenon. This is relevant context for whether the SU(3) endpoint of the Jensen deformation might be stable.

5. **The fibrewise estimate Delta_L >= 2K(R) on S^2_tt**: This provides a shortcut stability criterion that only requires evaluation of the curvature endomorphism K(R), which is algebraic (no derivatives). For the SU(3) fiber, K(R) is completely determined by the structure constants.
