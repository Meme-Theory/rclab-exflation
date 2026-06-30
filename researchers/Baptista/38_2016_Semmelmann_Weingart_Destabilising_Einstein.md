# Destabilising Compact Warped Product Einstein Manifolds

**Author(s):** Wafaa Batat, Stuart Hall, Thomas Murphy
**Year:** 2016 (v3: 2019)
**Journal:** [not stated in PDF]
**arXiv:** 1607.05766
**Relevance:** HIGH

---

## Abstract

The linear stability of warped product Einstein metrics as fixed points of the Ricci flow is investigated. We generalise the results of Gibbons, Hartnoll and Pope and show that in sufficiently low dimensions, all warped product Einstein metrics are unstable. By exploiting the relationship between warped product Einstein metrics, quasi-Einstein metrics and Ricci solitons, we introduce a new destabilising perturbation (the Ricci variation) and show that certain infinite families of warped product Einstein metrics will be unstable in high dimensions.

---

## Key Arguments and Derivations

### Section 2.1: Warped Product Einstein Metrics

A warped product on $M = B \times F$ is $g = \bar{g} \oplus (f \circ \pi_B)^2 \tilde{g}$, where $f \in C^\infty(B)$ is the warping function. If $(M, g)$ is Einstein with $\text{Ric}(g) = \lambda g$ ($\lambda > 0$), then:
- $(F, \tilde{g})$ is Einstein with $\text{Ric}(\tilde{g}) = \mu\tilde{g}$ for some $\mu > 0$
- $f\Delta f + (m-1)|\nabla f|^2 + \lambda f^2 = \mu$ (constraint equation)
- $\text{Ric}(\bar{g}) - mf^{-1}\nabla^2 f = \lambda\bar{g}$ (quasi-Einstein equation on the base)

### Section 2.2: Linear Stability for Ricci Flow

The linear stability of Einstein metrics is determined by the spectrum of the Lichnerowicz Laplacian $\Delta_L h = \Delta h + 2\text{Rm}(h, \cdot) - \text{Ric} \cdot h - h \cdot \text{Ric}$. Using Perelman's $\nu$-entropy:

**Definition 2.2:** An Einstein metric with $\text{Ric}(g) = \lambda g$ is:
- **Linearly stable** if $\kappa > 2\lambda$ (all eigenvalues of $\Delta_L$ on TT-tensors satisfy $-\kappa < -2\lambda$)
- **Neutrally stable** if $\kappa = 2\lambda$
- **Linearly unstable** if $\kappa < 2\lambda$

### Section 4: GHP Variations (Theorems A and E)

**Definition 4.1 (GHP variations):** For a warped product $\bar{g} \oplus f^2\tilde{g}$, the destabilising tensors are:
$$h = \frac{f^k}{n}\bar{g} \oplus \frac{(m+k)f^{k+2}}{mn}\tilde{g}, \quad k \in \mathbb{R}\setminus\{0\}$$

These are always divergence-free. The stability integral evaluates to:
$$\langle N(h+cg), h+cg \rangle = C^1_{n,m,k}\int_B f^{2k+m-2}|\nabla f|^2 dV_{\bar{g}} + \lambda(\|h\|^2 - \ldots)$$
where $C^1_{n,m,k} = -\frac{\text{Vol}(F)}{2}\frac{k^2(4k + 2m + mn + (m+k)^2)}{n^2 m}$.

**Proof of Theorem A:** $C^1_{n,m,k} \ge 0$ requires $(n-2)m \le 4$. This holds when:
- $n = 3, m \in \{2, 3, 4\}$ (base dim 3, fiber dim 2, 3, or 4)
- $n = 4, m = 2$ (base dim 4, fiber dim 2)

This covers all warped products with $\dim(M) \le 6$.

### Section 5: Ricci Variation (Theorem B)

**Definition 5.1 (Ricci variation):** $h_i = \text{Ric}(\bar{g}_i) \oplus c_i f_i^2 \tilde{g}$, where $c_i$ is chosen for gauge-fixing.

For a sequence of quasi-Einstein metrics converging to a Ricci soliton as $m_i \to \infty$, the Ricci variation always destabilises: $\langle N(h_2), h_2 \rangle = \lambda\|h_2\|^2 > 0$.

**Theorem B:** If $(B, \bar{g}_i, f_i, m_i)$ converge in $C^\infty$ to a non-trivial Ricci soliton, then there exists $K$ such that the warped product Einstein metrics are unstable for $k \ge K$.

### Section 4 (Theorem C): Fiber Instability

**Theorem C:** If the fiber $(F, \tilde{g})$ has a divergence-free, trace-free eigentensor of the Lichnerowicz Laplacian with eigenvalue $-\kappa$ satisfying $\kappa < \mu$, then the warped product is unstable.

**Corollary D:** Fiber-unstable warped products include those with:
- Riemannian product fibers $(F_1 \times F_2, g_1 \oplus g_2)$
- Kahler-Einstein fibers with $h^{1,1} > 1$
- Fibers that are themselves fiber-unstable warped products

## Key Results

1. **Theorem A:** All warped product Einstein manifolds with $\dim(M) \le 6$ are unstable as fixed points of the Ricci flow.
2. **Theorem B:** Warped products from quasi-Einstein metrics converging to a non-trivial Ricci soliton are unstable for sufficiently large fiber dimension.
3. **Theorem C:** If the fiber Einstein metric has a Lichnerowicz eigentensor with $\kappa < \mu$, the warped product is unstable.
4. **Corollary D:** Product fibers, Kahler-Einstein fibers with $h^{1,1} > 1$, and recursively fiber-unstable warped products are all unstable.
5. **Theorem E:** Warped product Einstein metrics with 3-dimensional base and 2- or 3-dimensional fiber yield unstable Schwarzschild-Tangherlini black holes.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Warped product metric | $g = \bar{g} \oplus f^2\tilde{g}$ on $M = B \times F$ | Sec. 2.1 |
| Constraint equation | $f\Delta f + (m-1)|\nabla f|^2 + \lambda f^2 = \mu$ | Eq. (2.1) |
| Quasi-Einstein eq. | $\text{Ric}(\bar{g}) - mf^{-1}\nabla^2 f = \lambda\bar{g}$ | Eq. (2.2) |
| Ricci soliton eq. | $\text{Ric}(g) + \nabla^2\varphi = \lambda g$ | Eq. (2.3) |
| Stability operator | $N(h) = \frac{1}{2}\Delta_L h + 2\lambda h$ (Einstein case, gauge-fixed) | Eq. (2.4) |
| Lichnerowicz Laplacian | $\Delta_L h = \Delta h + 2\text{Rm}(h,\cdot) - \text{Ric}\cdot h - h\cdot\text{Ric}$ | Eq. (2.5) |
| GHP variation | $h = \frac{f^k}{n}\bar{g} \oplus \frac{(m+k)f^{k+2}}{mn}\tilde{g}$ | Eq. (4.1) |
| Instability coefficient | $C^1_{n,m,k} = -\frac{\text{Vol}(F)}{2}\frac{k^2(4k+2m+mn+(m+k)^2)}{n^2 m}$ | Prop. 4.2 |
| Black hole instability | Unstable if $\kappa < \frac{(9-n)\lambda}{4}$ (for trace-free eigentensors) | Prop. 2.5 |

## Relevance to Phonon-Exflation

This paper is directly relevant because the phonon-exflation framework models spacetime as $M^4 \times F$ where $F = SU(3)/T$ is a 6-dimensional fiber. The framework's "exflation" mechanism involves the internal space evolving under dynamics that can be modeled as a warped product. Theorem A proves that ALL warped product Einstein metrics in $\dim \le 6$ are Ricci flow unstable, which applies to warped products $B^3 \times F^3$ or $B^4 \times F^2$. More critically, Theorem C and Corollary D show that if the fiber itself has product structure or Kahler-Einstein structure with $h^{1,1} > 1$, the warped product is fiber-unstable. Since $SU(3)/T$ is a flag manifold with multiple Einstein metrics (cf. paper 35), its Lichnerowicz spectrum determines whether warped products using it as fiber are stable. The destabilisation mechanism (GHP "ballooning mode" -- changing relative volumes of base and fiber) is precisely the dynamical instability that could drive the tau-evolution: the internal space spontaneously wants to change its relative size. The Ricci variation (Theorem B) connects this to Ricci soliton limits, relevant to the framework's use of Ricci flow on the internal geometry.
