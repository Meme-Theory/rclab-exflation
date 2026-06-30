# Eigenvalue estimates of the Dirac operator depending on the Ricci tensor

**Author(s):** Thomas Friedrich, Klaus-Dieter Kirchberg
**Year:** 2001
**Journal:** arXiv preprint (math.DG)
**arXiv:** math/0104121
**Relevance:** HIGH

---

## Abstract

We prove a new lower bound for the first eigenvalue of the Dirac operator on a compact Riemannian spin manifold by refined Weitzenb\"ock techniques. It applies to manifolds with harmonic curvature tensor and depends on the Ricci tensor. Examples show how it behaves compared to other known bounds.

---

## Key Arguments and Derivations

### 1. The Operator $Q^t$

The authors introduce a one-parameter family of differential operators $Q^t: \Gamma(S) \to \Gamma(TM^n \otimes S)$ defined by:
$$Q^t_X \psi := \nabla_X D\psi + \frac{1}{n} X \cdot D^2\psi + t \cdot \left(\text{Ric} - \frac{R}{n}\right)(X) \cdot \psi$$
where $\text{Ric}$ is the Ricci tensor and $t \in \mathbb{R}$ is a parameter. The image of $Q^t$ lies in the kernel of Clifford multiplication.

### 2. Preliminary Weitzenb\"ock Formula (Lemma 1.1)

For any spinor field $\psi$:
$$|Q^t\psi|^2 = |\nabla D\psi|^2 - \frac{1}{n}|D^2\psi|^2 + \frac{2tR}{n}\text{Re}\langle D^2\psi, \psi\rangle + t^2\left|\text{Ric} - \frac{R}{n}\right|^2|\psi|^2 - 2t\,\text{Re}\langle\text{Ric}(X_k) \cdot \nabla_{X_k}D\psi, \psi\rangle$$

The last term is "uncontrollable" and must be expressed in terms of manageable quantities.

### 3. Harmonic Curvature Condition

Assuming the curvature tensor is harmonic ($\nabla_{X_k}K(X_k, Y) = 0$ for all $Y$), the second Bianchi identity simplifies the covariant derivative of the Ricci tensor to $(\nabla_X \text{Ric})(Y) = (\nabla_Y \text{Ric})(X)$ (Codazzi condition), and the scalar curvature $R$ is constant.

Under this condition, the uncontrollable term is expressed (Lemma 1.3) using spinor curvature endomorphisms $C(X,Y)$, the Schr\"odinger-Lichnerowicz formula $\nabla^*\nabla = D^2 - R/4$, and divergence terms that vanish upon integration.

### 4. Main Weitzenb\"ock Formula (Theorem 1.6)

For eigenspinors $D\psi = \lambda\psi$ on compact manifolds with harmonic curvature:
$$\int |Q^t\psi|^2 = \int \left\{\frac{n-1}{n}\lambda^4 - \frac{(n+2)(2n-1)}{4n^2}R\lambda^2 + \frac{n+8}{16n}R^2 - \frac{1}{4}\left|\text{Ric} - \frac{R}{n}\right|^2\right\}|\psi|^2$$
plus terms involving the parameter $t$ and the Ricci tensor.

### 5. Eigenvalue Estimates

Integrating $|Q^t\psi|^2 \geq 0$ and optimizing over $t$:

**For vanishing scalar curvature** ($R = 0$):
$$\lambda^2 > \frac{1}{4} \cdot \frac{|\text{Ric}|_0^2}{|\text{Ric}|_0\sqrt{\frac{n-1}{n}} + |\kappa_0|}$$
where $\kappa_0$ is the minimum Ricci eigenvalue and $|\text{Ric}|_0$ is the minimum of $|\text{Ric}|$.

**General case**: A lower bound depending on $R_0$ (minimum scalar curvature), $\kappa_0$, $|\text{Ric}|_0$, and $n$.

---

## Key Results

1. New lower bound for Dirac eigenvalues depending on the Ricci tensor (not just scalar curvature)
2. The Friedrich inequality $\lambda^2 \geq \frac{nR_0}{4(n-1)}$ is recovered when $\text{Ric} = \frac{R}{n}g$ (Einstein case)
3. For harmonic curvature with $R = 0$, Ricci curvature alone bounds Dirac eigenvalues from below
4. The parameter $t$ optimization provides the sharpest bound
5. Killing spinors ($\nabla_X\psi + \frac{\lambda_1}{n}X\cdot\psi = 0$) are the equality case of the classical bound

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Operator $Q^t$ | $Q^t_X\psi = \nabla_X D\psi + \frac{1}{n}X\cdot D^2\psi + t(\text{Ric} - \frac{R}{n})(X)\cdot\psi$ | Section 1 |
| Friedrich bound | $\lambda^2 \geq \frac{nR_0}{4(n-1)}$ | Eq. (1) |
| Schr\"odinger-Lichnerowicz | $\nabla^*\nabla = D^2 - \frac{1}{4}R$ | Eq. (11) |
| Weitzenb\"ock for twistor | $|\mathcal{D}\psi|^2 = |\nabla\psi|^2 - \frac{1}{n}|D\psi|^2$ | Eq. (7) |
| Spinor curvature | $C(X,Y)\psi = \frac{1}{4}g(K(X,Y)(X_k), X_l)X_k\cdot X_l\cdot\psi$ | Eq. (9) |
| $R = 0$ estimate | $\lambda^2 > \frac{1}{4}\frac{|\text{Ric}|_0^2}{|\text{Ric}|_0\sqrt{(n-1)/n} + |\kappa_0|}$ | Section 2 |
| Codazzi condition | $(\nabla_X\text{Ric})(Y) = (\nabla_Y\text{Ric})(X)$ | Harmonic curvature |
| Clifford identity | $X_k\cdot\text{Ric}(X_k) = -R$ | Eq. (5) |

---

## Relevance to Phonon-Exflation

This paper provides eigenvalue lower bounds for the Dirac operator that go beyond the classical Friedrich bound by incorporating Ricci tensor data. For the SU(3) internal geometry at generic $\tau$ values, the metric is not Einstein, so the Ricci tensor has non-trivial traceless part. These refined estimates constrain the Dirac spectrum gap as a function of the internal geometry's Ricci curvature, directly relevant to the spectral gap computations in the BDI classification and the mechanism chain's stability analysis.
