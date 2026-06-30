# The Asymptotic Expansion of the Heat Kernel on a Compact Lie Group

**Author(s):** Seunghun Hong (Show)
**Year:** 2011
**Journal:** arXiv preprint
**arXiv:** 1111.2643
**Relevance:** CRITICAL

---

## Abstract

Let G be a compact connected Lie group equipped with a bi-invariant metric. We calculate the asymptotic expansion of the heat kernel of the laplacian on G and the heat trace using Lie algebra methods. The Duflo isomorphism plays a key role.

---

## Key Arguments and Derivations

### 1. Setup and Motivation

For a compact connected Lie group $G$ with bi-invariant metric, the Laplacian $\Delta_G$ is a bi-invariant differential operator. The heat trace $Z(t) = \text{tr}(e^{t\Delta_G})$ has an asymptotic expansion as $t \to 0^+$ whose coefficients encode geometric information. The paper exploits the algebraic structure of $G$ (rather than purely analytic methods) to compute the full asymptotic expansion in closed form.

### 2. The Casimir Element and Laplacian

If $\{X_i\}_{i=1}^n$ is an orthonormal basis for $\mathfrak{g}$, then the Laplacian equals the Casimir element:
$$\Delta_G = \sum_{i=1}^n \tilde{X}_i \tilde{X}_i = \text{Cas}$$
where $\tilde{X}_i$ are left-invariant vector fields. This is proved by showing equality at the identity $e \in G$ in exponential coordinates (where $g_{ij}(e) = \delta_{ij}$ and $\partial_k g_{ij}(e) = 0$ because the Riemannian and Lie-theoretic exponential maps coincide for bi-invariant metrics).

### 3. The Duflo Isomorphism

The Duflo isomorphism $\text{Duf}: S(\mathfrak{g})^{\mathfrak{g}} \to Z(\mathfrak{g})$ is the key tool. Under the identification of $U(\mathfrak{g})$ with left-invariant differential operators on $G$ and $S(\mathfrak{g})$ with constant-coefficient operators on $\mathfrak{g}$:
$$\text{Duf}(\Delta_{\mathfrak{g}}) = \text{Cas} + \frac{1}{24}\text{tr}_{\mathfrak{g}}(\text{Cas}) = \Delta_G - \langle \rho, \rho \rangle$$
where $\rho$ is half the sum of positive roots and $\langle \rho, \rho \rangle$ is computed via the Kostant formula $\frac{1}{24}\text{tr}_{\mathfrak{g}}\text{Cas} = -\langle \rho, \rho \rangle$.

The Duflo map is $j \cdot \exp_*$, where $j(X) = \det^{1/2}\left(\frac{\sinh(\text{ad}_X/2)}{\text{ad}_X/2}\right)$ and $\exp_*$ is the push-forward along the exponential map.

### 4. Heat Kernel via Duflo (Lemma 3.5, 3.6)

**Lemma 3.5**: In exponential coordinates, $\text{Duf}(\Delta_{\mathfrak{g}})^{\exp} = j^{-1} \circ \Delta_{\mathfrak{g}} \circ j$.

**Lemma 3.6**: The convolution kernel $p_t$ of $e^{t\,\text{Duf}(\Delta_{\mathfrak{g}})}$ has the asymptotic expansion (in exponential coordinates):
$$p_t^{\exp} \sim h_t \cdot j^{-1}, \quad t \to 0^+$$
where $h_t(X) = e^{-\|X\|^2/4t}/(4\pi t)^{\dim\mathfrak{g}/2}$ is the Gaussian kernel on $\mathfrak{g}$.

### 5. Scalar Curvature (Lemma 3.8)

The scalar curvature of $G$ with bi-invariant metric is:
$$S = -\frac{1}{4}\text{tr}_{\mathfrak{g}}(\text{Cas})$$
proved from the Riemann curvature formula $\text{Rm}(\tilde{X},\tilde{Y},\tilde{Z},\tilde{W}) = -\frac{1}{4}\langle [X,Y],[Z,W]\rangle$.

### 6. Main Theorem (Theorem 3.9)

**Theorem**: The heat convolution kernel $k_t$ for the Laplacian on $G$ satisfies:
$$k_t^{\exp} \sim \frac{h_t}{j} \cdot e^{tS/6}$$
as $t \to 0^+$, in a neighborhood of $0 \in \mathfrak{g}$.

**Proof**: Since $e^{t\Delta_G} = e^{tS/6} e^{t\,\text{Duf}(\Delta_{\mathfrak{g}})}$ (from $\Delta_G = \text{Duf}(\Delta_{\mathfrak{g}}) + \langle\rho,\rho\rangle$ and $S = 4\langle\rho,\rho\rangle/6$... more precisely $S/6 = -\text{tr}_{\mathfrak{g}}(\text{Cas})/24 = \langle\rho,\rho\rangle$), we have $k_t = e^{tS/6} p_t$ and the result follows from Lemma 3.6.

### 7. Heat Trace (Corollary 3.10)

$$Z(t) \sim \text{vol}(G) \cdot e^{tS/6}$$
as $t \to 0^+$. This is a remarkably simple closed-form result: the heat trace is essentially $\text{vol}(G)$ times the exponential of a curvature-dependent constant.

---

## Key Results

1. Heat kernel on compact Lie group with bi-invariant metric is controlled by the Duflo $j$-function: $k_t^{\exp} \sim h_t/j \cdot e^{tS/6}$
2. Heat trace has the exact asymptotic form $Z(t) \sim \text{vol}(G)\,e^{tS/6}$
3. All heat trace coefficients are determined: $a_k = \text{vol}(G) \cdot (S/6)^k / k!$
4. Scalar curvature $S = -\frac{1}{4}\text{tr}_{\mathfrak{g}}(\text{Cas})$
5. The Duflo isomorphism provides the bridge: $\text{Duf}(\Delta_{\mathfrak{g}}) = \Delta_G - \langle\rho,\rho\rangle$
6. Riemannian and Lie-theoretic exponential maps coincide for bi-invariant metrics (from $\nabla_{\tilde{X}}\tilde{Y} = \frac{1}{2}[\tilde{X},\tilde{Y}]$)

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Laplacian = Casimir | $\Delta_G = \sum_{i=1}^n \tilde{X}_i\tilde{X}_i = \text{Cas}$ | Eq. (2.14) |
| Duflo image | $\text{Duf}(\Delta_{\mathfrak{g}}) = \text{Cas} + \frac{1}{24}\text{tr}_{\mathfrak{g}}(\text{Cas}) = \Delta_G - \langle\rho,\rho\rangle$ | Eqs. (3.2), (3.4) |
| $j$-function | $j(X) = \det^{1/2}\left(\frac{\sinh(\text{ad}_X/2)}{\text{ad}_X/2}\right)$ | Section (2.18) |
| Conjugation formula | $\text{Duf}(\Delta_{\mathfrak{g}})^{\exp} = j^{-1} \circ \Delta_{\mathfrak{g}} \circ j$ | Lemma (3.5) |
| Heat kernel asymptotic | $k_t^{\exp} \sim \frac{h_t}{j}\,e^{tS/6}$ | Thm (3.9) |
| Heat trace | $Z(t) \sim \text{vol}(G)\,e^{tS/6}$ | Cor (3.10) |
| Scalar curvature | $S = -\frac{1}{4}\text{tr}_{\mathfrak{g}}(\text{Cas})$ | Lemma (3.8) |
| Riemannian connection | $\nabla_{\tilde{X}}\tilde{Y} = \frac{1}{2}[\tilde{X},\tilde{Y}]$ | Eq. (2.16) |
| Riemann tensor | $\text{Rm}(\tilde{X},\tilde{Y},\tilde{Z},\tilde{W}) = -\frac{1}{4}\langle [X,Y],[Z,W]\rangle$ | Section (3.8) |
| Gaussian kernel | $h_t(X) = e^{-\|X\|^2/4t}/(4\pi t)^{\dim G/2}$ | Section (2.10) |

---

## Relevance to Phonon-Exflation

This paper is directly applicable to the internal SU(3) factor of the M4 x SU(3) geometry. For bi-invariant metrics on SU(3), the heat kernel is controlled by the Duflo $j$-function $j(X) = \det^{1/2}(\sinh(\text{ad}_X/2)/(\text{ad}_X/2))$, and ALL heat trace coefficients are given in closed form by $a_k = \text{vol}(\text{SU}(3))(S/6)^k/k!$. This is the exact result that computation Dirac spectrum computations should reproduce. The scalar curvature formula $S = -\frac{1}{4}\text{tr}_{\mathfrak{g}}(\text{Cas})$ connects directly to the Casimir eigenvalues computed in the Peter-Weyl basis. The $j$-function's role in the heat kernel is the mathematical underpinning for the spectral action on the internal space.
