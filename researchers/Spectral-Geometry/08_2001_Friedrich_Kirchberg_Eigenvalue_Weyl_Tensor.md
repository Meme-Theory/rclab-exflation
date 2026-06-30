# Eigenvalue estimates for the Dirac operator depending on the Weyl tensor

**Author(s):** Thomas Friedrich, Klaus-Dieter Kirchberg
**Year:** 2001
**Journal:** arXiv preprint (math.DG)
**arXiv:** math/0105055
**Relevance:** HIGH

---

## Abstract

We prove new lower bounds for the first eigenvalue of the Dirac operator on compact manifolds whose Weyl tensor or curvature tensor, respectively, is divergence free. In the special case of Einstein manifolds, we obtain estimates depending on the Weyl tensor.

---

## Key Arguments and Derivations

### 1. Curvature Endomorphisms

On a Riemannian spin manifold $(M^n, g)$ with $n \geq 4$, the spinor curvature $C(X,Y)$ and Weyl-derived endomorphism $B(X,Y) := \frac{1}{4}X_k \cdot W(X,Y)(X_k)$ generate nonnegative self-adjoint endomorphisms:
$$F = -C(X_k, X_l)C(X_k, X_l), \quad H = -B(X_k, X_l)B(X_k, X_l)$$

These are related by:
$$F = H + \frac{1}{2(n-2)}\left|\text{Ric} - \frac{R}{n}\right|^2 + \frac{R^2}{4n(n-1)}$$

The smallest eigenvalue $\nu_0 = \inf\{\nu(x) : x \in M^n\}$ of $H$ measures the "Weyl curvature obstruction" to parallel spinors.

### 2. The Operator $P^t$ (Section 3)

For manifolds with divergence-free Weyl tensor, the operator $P^t: \Gamma(S) \to \Gamma(TM^n \otimes S)$ is:
$$P^t_X\psi := \nabla_X\psi + \frac{1}{n}X\cdot D\psi - t\,B(X, X_k)\cdot\nabla_{X_k}\psi$$

Its Weitzenb\"ock formula (Lemma 3.1, assuming $\nabla_{X_k}W(X_k, Y) = 0$):
$$|P^t\psi|^2 = |\nabla\psi|^2 - \frac{1}{n}|D\psi|^2 - t\langle H\psi, \psi\rangle + t^2\langle G(X_k,X_l)\nabla_{X_k}\psi, \nabla_{X_l}\psi\rangle - 2t\,\text{div}\langle B\psi, \nabla\psi\rangle$$

### 3. Main Theorem (Theorem 3.1)

For compact spin manifolds with divergence-free Weyl tensor, any Dirac eigenvalue $\lambda$ satisfies:
$$\lambda^2 \geq \frac{nR_0}{4(n-1)} + \frac{2\nu_0^2}{n\mu_0^2\left(R_0 + \sqrt{R_0^2 + \frac{n-1}{n}\left(\frac{4\nu_0}{\mu_0}\right)^2}\right)}$$
where $\mu_0^2 = \max\frac{1}{16}\|W_{XY,ij}X_i\cdot X_j\|^2$ over orthonormal $X, Y$.

### 4. Special Cases

**Einstein manifolds** (Corollary 3.1): The Weyl tensor is automatically divergence-free, so the bound applies directly.

**Vanishing scalar curvature** (Corollary 3.2): $\lambda^2 \geq \frac{\nu_0}{2\mu_0}\sqrt{n(n-1)}$.

**Conformally Ricci-flat manifolds** (Corollary 3.3): If $\nu_0 > 0$, no harmonic spinors exist.

### 5. Symmetric Spaces (Proposition 3.1)

For irreducible symmetric spaces of compact type, $H_4 = 0$ (the degree-4 Clifford part of $H$ vanishes), so $\nu_0 = \frac{1}{8}|W|^2$. The Casimir operators of $G$ and $K$ control the curvature term.

### 6. Divergence-Free Curvature (Section 4)

If the full curvature tensor $K$ (not just the Weyl tensor) is divergence-free, a stronger operator $Q^t$ is used:
$$Q^t_X\psi = \mathcal{D}_X\psi - t\,C(X, X_k)\cdot\nabla_{X_k}\psi$$
leading to estimates depending on both the Ricci and Weyl tensors simultaneously.

---

## Key Results

1. Lower bound for Dirac eigenvalues depending on the Weyl tensor for manifolds with $\nabla \cdot W = 0$ (Theorem 3.1)
2. On Einstein manifolds, the bound improves the classical Friedrich bound by a Weyl-tensor-dependent correction
3. $\nu_0 > 0$ obstructs harmonic spinors on conformally Ricci-flat manifolds (Corollary 3.3)
4. For symmetric spaces: $\nu_0 = \frac{1}{8}|W|^2$ (Proposition 3.1)
5. 4D K\"ahler-Einstein manifolds: recovers the bound $\lambda^2 \geq R/2$
6. Combined Ricci+Weyl estimates for harmonic curvature (Section 4)

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Weyl endomorphism | $B(X,Y) = \frac{1}{4}X_k\cdot W(X,Y)(X_k)$ | Section 2 |
| $H$ endomorphism | $H = -B(X_k,X_l)B(X_k,X_l)$ | Section 2 |
| $F$-$H$ relation | $F = H + \frac{1}{2(n-2)}|\text{Ric} - \frac{R}{n}|^2 + \frac{R^2}{4n(n-1)}$ | Eq. (14) |
| Main bound | $\lambda^2 \geq \frac{nR_0}{4(n-1)} + \frac{2\nu_0^2}{n\mu_0^2(R_0 + \sqrt{R_0^2 + \frac{n-1}{n}(\frac{4\nu_0}{\mu_0})^2})}$ | Eq. (25) |
| $R = 0$ bound | $\lambda^2 \geq \frac{\nu_0}{2\mu_0}\sqrt{n(n-1)}$ | Eq. (27) |
| Symmetric space | $\nu_0 = \frac{1}{8}|W|^2$ | Prop 3.1 |
| $H$ decomposition | $H = H_0 + H_4 = \frac{1}{8}|W|^2 + H_4$ | Section 3 |
| 4D formula | $\nu_0 = \min\{\frac{1}{4}|W^+ + *W|^2, \frac{1}{4}|W^- - *W|^2\}$ | Section 3 |
| Divergence-free Weyl | $(n-3)[(\nabla_X T)(Y) - (\nabla_Y T)(X)] = 0$ | Eq. (26) |

---

## Relevance to Phonon-Exflation

The Weyl tensor estimates are directly relevant to the internal SU(3) geometry where the metric varies with $\tau$. Since SU(3) is a symmetric space with bi-invariant metric, $\nu_0 = \frac{1}{8}|W|^2$ provides an exact formula for the Weyl obstruction. As $\tau$ deforms the metric away from bi-invariance, the Weyl tensor becomes non-trivial and these bounds constrain the Dirac spectral gap. The relation $F = H + (\text{Ricci traceless})^2 + R^2/(4n(n-1))$ connects the full spinor curvature endomorphism to the decomposition of the Riemann tensor, which is the mathematical structure underlying the constant-ratio trap analysis.
