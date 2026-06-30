# On the Dirac Spectrum of Homogeneous 3-Spheres

**Author(s):** Jordi Kling, Dorothee Schueth
**Year:** 2022
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 2204.12990
**Relevance:** CRITICAL

---

## Abstract

We show that any two left-invariant metrics on S^3 ~ SU(2) which are isospectral for the associated classical Dirac operator D must be isometric. In the case of left-invariant metrics of positive scalar curvature, we compute and use the smallest eigenvalue of D^2. We show analogous results for left-invariant metrics on SO(3) = S^3/{+/-1} for each of its two spin structures.

---

## Key Arguments and Derivations

### 1. Setup and Homogeneous Metrics on S^3

The paper considers left-invariant Riemannian metrics on the Lie group S^3 ~ SU(2) and its quotient SO(3) = S^3/{+/-1}. Every left-invariant metric on S^3 is isometric to a metric of the form g_{abc}, where a, b, c > 0 are the inverses of the lengths of the standard basis elements {i, j, k} of T_1 S^3. The metric g_{abc} has orthonormal basis X_1 = ai, X_2 = bj, X_3 = ck.

For any permutation sigma of {a, b, c}, the metric g_{sigma(a)sigma(b)sigma(c)} is isometric to g_{abc} by an orientation-preserving isometry that descends to SO(3).

### 2. Dirac Operator on Homogeneous S^3

Following Bar's approach, the authors derive the Dirac operator D on (S^3, g_{abc}). After choosing an orientation and the unique spin structure, the spinor bundle is trivial: Sigma S^3 = S^3 x Sigma_3 where Sigma_3 ~ C^2. The Dirac operator takes the explicit form:

(D phi)(x) = sum_{l=1}^{3} e_l . X_l|_x(phi) + (1/2)(ab/c + bc/a + ca/b) e_1.e_2.e_3 . phi(x)

The key quantity C := (1/2)(ab/c + bc/a + ca/b) and mu := a + b + c - C appear throughout. Using Frobenius reciprocity, the Hilbert space L^2(S^3, Sigma_3) decomposes into isotypical components V_n tensor Hom(V_n, Sigma_3), and D restricts to Id tensor D_n on each component. The operator D_n is explicitly computed and has the form D_n = D'_n - C*Id, where D'_n is tridiagonal.

### 3. Spin Structures on SO(3)

SO(3) admits precisely two spin structures alpha_0 and alpha_1. The Dirac spectra of these are:
- spec(D_{alpha_0}) consists of eigenvalues of D_n for even n
- spec(D_{alpha_1}) consists of eigenvalues of D_n for odd n

### 4. Fundamental Tone under Positive Scalar Curvature (Theorem 1.1)

The scalar curvature of g_{abc} is scal = 4(a^2 + b^2 + c^2) - 2(a^2 b^2/c^2 + b^2 c^2/a^2 + c^2 a^2/b^2) = 8(a^2 + b^2 + c^2 - C^2).

Under the condition scal > 0, the authors prove explicit formulas for the smallest absolute eigenvalue:
- For D on S^3: min{|lambda|} = mu > 0
- For D_{alpha_0} on SO(3): min{|lambda|} = C >= mu
- For D_{alpha_1} on SO(3): min{|lambda|} = mu

The proof proceeds by: (i) Direct computation for small n (n = 0, 1, 2, 3, 4), and (ii) An inductive argument using the Gershgorin Circle Theorem applied to D_n^2 for n >= 5, establishing a "Triangle Induction" where G(n+2, k+1) > G(n,k) for all n, k.

### 5. Spectral Rigidity (Theorem 1.2)

The main spectral rigidity result: within the class of homogeneous metrics on S^3 (or SO(3)), the metric g_{abc} is determined by the Dirac spectrum up to isometry. For scal > 0, this follows from the smallest eigenvalue together with volume and scalar curvature (from heat invariants a_0, a_1). For scal <= 0, the third heat invariant a_2 from Dlubek-Friedrich is used instead. The Lichnerowicz bound lambda^2 >= (1/4) min(scal) is a key ingredient.

---

## Key Results

1. **Theorem 1.1**: For scal > 0, the smallest Dirac eigenvalue of (S^3, g_{abc}) is mu = a + b + c - C with multiplicity 4 (if a=b=c) or 2 (otherwise). For SO(3), the fundamental tone of D_{alpha_0} is C and of D_{alpha_1} is mu.

2. **Theorem 1.2**: Within homogeneous metrics on S^3, the Dirac spectrum determines the metric g_{abc} up to isometry. The same holds on SO(3) for each spin structure.

3. **Triangle Induction Lemma (3.9)**: If scal > 0, then G(n+2, k+1) > G(n, k) for all n >= 0 and k in {0,...,n}, providing the inductive step for Gershgorin estimates.

4. The heat invariant a_2 of D^2 suffices (with a_0, a_1) to distinguish homogeneous metrics on S^3 when scal <= 0.

5. The characteristic polynomials of the A' and B' blocks of D'_n coincide for all n, and the Gershgorin circle approach on the pentadiagonal D_n^2 gives explicit lower bounds on eigenvalues.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Dirac operator | $(D\varphi)(x) = \sum_{\ell=1}^{3} e_\ell \cdot X_\ell\|_x(\varphi) + C \, e_1 \cdot e_2 \cdot e_3 \cdot \varphi(x)$ | Eq. (1) |
| C definition | $C := \frac{1}{2}\left(\frac{ab}{c} + \frac{bc}{a} + \frac{ca}{b}\right)$ | Eq. (3) |
| mu definition | $\mu := a + b + c - C$ | Thm 1.1 |
| Scalar curvature | $\mathrm{scal} = 8(a^2 + b^2 + c^2 - C^2)$ | Prop 2.11 |
| Lichnerowicz bound | $\lambda^2 \geq \frac{1}{4}\min(\mathrm{scal})$ | Sec. 1 |
| Frobenius decomposition | $L^2(S^3, \Sigma_3) \cong \bigoplus_{n \in \mathbb{N}_0} V_n \otimes \mathrm{Hom}(V_n, \Sigma_3)$ | Eq. (2) |
| D_n formula | $D_n(f) = -\sum_{\ell=1}^{3} e_\ell \cdot f \circ \pi_{n*}(X_\ell) + C \, e_1 \cdot e_2 \cdot e_3 \cdot f$ | Prop 2.4 |
| D_n decomposition | $D_n = D'_n - C \cdot \mathrm{Id}$ | Cor 2.10 |
| Gershgorin bound | $G(n,k) := (a(n-2k)-C)^2 + (b-c)^2 k(n-k+1) + (b+c)^2(n-k)(k+1) - \ldots$ | Cor 3.7 |
| Triangle Induction | $G(n+2,k+1) - G(n,k) = 4(c^2 n - bC + ac + b^2 + c^2) > 0$ | Lemma 3.9 |
| scal factorization | $\mathrm{scal} = \frac{2}{a^2 b^2 c^2}(ab+bc+ca)(ab+bc-ca)(ab-bc+ca)(-ab+bc+ca)$ | Eq. (4) |
| Eigenvalues of D_1 | $a+b+c-C,\; a-b-c-C,\; -a+b-c-C,\; -a-b+c-C$ | Rmk 3.3(iv) |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the M4 x SU(3) framework because it establishes spectral rigidity of the Dirac operator on homogeneous S^3 ~ SU(2), and the project's Dirac spectrum computations on SU(2) and SU(3) depend on exactly this class of operators. The Frobenius reciprocity decomposition used here (L^2 into isotypical components) is the same decomposition used in the project's Peter-Weyl approach to D_K(tau). The Gershgorin circle technique for bounding eigenvalues of D_n^2 could be applied to sharpen bounds on the SU(3) Dirac spectrum at finite tau. The explicit dependence of the fundamental tone on metric parameters (a, b, c) directly informs how the spectral gap of D_K changes along the compactification parameter tau.
