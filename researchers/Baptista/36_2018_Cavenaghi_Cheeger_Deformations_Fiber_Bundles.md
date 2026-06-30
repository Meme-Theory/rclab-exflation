# The Concept of Cheeger Deformations on Fiber Bundles with Compact Structure Group

**Author(s):** Leonardo F. Cavenaghi, Lino Grama, Llohann D. Speranca
**Year:** 2018 (v3: 2022)
**Journal:** [not stated in PDF]
**arXiv:** 1801.06576
**Relevance:** MEDIUM

---

## Abstract

The purpose of this paper is two-fold: we systematically introduce the notion of Cheeger deformations on fiber bundles with compact structure groups, and recover in a very simple and unified fashion several results that either already appear in the literature or are known by experts, though are not explicitly written elsewhere. We re-prove: Schwachhofer-Tuschmann Theorem on bi-quotients, many results due to Fukaya and Yamaguchi, as well as, naturally extend the work of Searle-Solorzano-Wilhelm on regularization properties of Cheeger deformations, among others. In this sense, this paper should be understood as a survey intended to demonstrate the power of Cheeger deformations.

---

## Key Arguments and Derivations

### Section 2: Classical Cheeger Deformations

The paper reviews the Cheeger deformation procedure on a manifold $(M, g)$ with isometric $G$-action. Starting from the product $M \times G$ with metric $g + t^{-1}Q$ (where $Q$ is bi-invariant on $G$), two free actions yield two submersions: one recovering $g$ on $M$, the other producing the Cheeger deformation $g_t$. Three key tensors are defined:
- **Orbit tensor** $P: \mathfrak{m}_p \to \mathfrak{m}_p$ via $g(U^*, V^*) = Q(PU, V)$
- **Deformed orbit tensor** $P_t = P(1 + tP)^{-1}$
- **Metric tensor** $C_t: T_pM \to T_pM$ via $g_t(X, Y) = g(C_tX, Y)$

**Theorem 2.2:** The unreduced sectional curvature satisfies $\kappa_t(X, Y) = \kappa_0(X, Y) + \frac{t^3}{4}\|[PU, PV]\|_Q^2 + z_t(X, Y)$, where $z_t \ge 0$. Cheeger deformations do not create new zero-curvature planes.

### Section 3: Cheeger Deformations on Associated Fiber Bundles

Given a fiber bundle $F \hookrightarrow M \to B$ with compact structure group $G$, the deformation is defined on the associated principal bundle $P \times F \to M$ by Cheeger-deforming the metric on $P$ while keeping $g_F$ fixed.

**Theorem 3.1 (Sectional curvature):** For the deformed metric $h_t$, $\tilde{\kappa}_t(\tilde{X}, \tilde{Y}) = \kappa_t(X + U^\vee, Y + V^\vee) + K_{g_F}(X_F - (P_F^{-1}PU)^*, Y_F - (P_F^{-1}PV)^*) + \tilde{z}_t(\tilde{X}, \tilde{Y})$, where $\tilde{z}_t \ge 0$. The sectional curvature decomposes into a base Cheeger term, a fiber curvature term, and a non-negative remainder.

### Section 3.2: Regularization via Cheeger Deformations

**Theorem 3.2:** For fiber bundles with compact total space and structure group, after appropriate rescaling of fibers, the deformation $h_t$ converges in $C^p$-topology to a Riemannian submersion metric with totally geodesic fibers. Cheeger deformations act as a canonical regularization process.

### Section 4: Applications to Bi-quotients and Curvature

**Theorem 4.2 (Schwachhofer-Tuschmann):** A bi-quotient $G//K$ of a compact connected Lie group $G$ carries a metric of positive Ricci curvature if and only if its fundamental group is finite. The limiting Ricci curvature decomposes as:
$\lim_{t\to\infty} \text{Ric}_{h_t}(X + X_F + U^*) = \text{Ric}_{\bar{g}}(d\pi X) + \text{Ric}^h(X_F) + 3\sum_j |A_{X_F}^{\pi_F} e_j^F|^2 + \sum_k \frac{1}{4}\|[v_k(0), U]\|_Q^2$

**Theorem 4.3 (Fukaya-Yamaguchi type):** If $K_g \ge 0$ and $F$ has a $G$-invariant metric of non-negative sectional curvature, then $M$ admits almost non-negative sectional curvature.

**Theorem 4.5:** If $F$ carries $g_F$ with $\text{Ric}(g_F) \ge 0$ and $B$ carries $g_\epsilon$ with $\text{Ric}(g_\epsilon) \ge -\epsilon^2$, then $M$ carries $h_\epsilon$ with $\text{Ric}(h_\epsilon) \ge -\epsilon^2$.

### Section 5: Petersen-Wilhelm Fiber Dimension Conjecture

The paper conjectures that any $S^3$ or $SO(3)$ principal bundle over a positively curved manifold admits a metric with positive sectional curvature if and only if the submersion is fat. For $S^2$-bundles with fat structure, the deformation $h_1$ has positive vertizontal curvature.

## Key Results

1. A unified sectional curvature formula (Theorem 3.1) for Cheeger deformations on fiber bundles, decomposing into base, fiber, and non-negative remainder terms.
2. Cheeger deformations on fiber bundles converge (after rescaling) to metrics with totally geodesic fibers (Theorem 3.2).
3. Re-proof of Schwachhofer-Tuschmann: bi-quotients $G//K$ have positive Ricci curvature iff $\pi_1$ is finite (Theorem 4.2).
4. Re-proof of Fukaya-Yamaguchi: fiber bundles with non-negatively curved base and fiber admit almost non-negative sectional curvature (Theorem 4.3).
5. Almost non-negative Ricci curvature lifts from base to total space of fiber bundles (Theorem 4.5).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Deformed orbit tensor | $P_t = (P^{-1} + t\mathbf{1})^{-1} = P(1 + tP)^{-1}$ | Prop. 2.1 |
| Metric tensor | $C_t(X) = X + ((1+tP)^{-1}U)^*$ for $X = \bar{X} + U^*$ | Prop. 2.1 |
| Sectional curvature (classical) | $\kappa_t(X,Y) = \kappa_0(X,Y) + \frac{t^3}{4}\|[PU, PV]\|_Q^2 + z_t(X,Y)$ | Eq. (5) |
| Fiber bundle curvature | $\tilde{\kappa}_t(\tilde{X},\tilde{Y}) = \kappa_t(X+U^\vee, Y+V^\vee) + K_{g_F}(\ldots) + \tilde{z}_t$ | Thm. 3.1 |
| Horizontal lift | $L_\pi(X + X_F + U^*) = (X - (P_t^{-1}\tilde{P}_tU)^\vee, X_F + (P_F^{-1}\tilde{P}_tU)^*)$ | Eq. (22) |
| Combined orbit tensor | $\tilde{P}_t = (P_F^{-1} + P_t^{-1})^{-1}$ | Eq. (20) |
| Ricci curvature (Lemma 1) | $\text{Ric}_{g_t}(X) = \text{Ric}_g^h(C_tX) + \sum_i z_t(C_t^{1/2}e_i, C_tX) + \sum_i \frac{1}{1+t\lambda_i}(\ldots)$ | Eq. (7) |
| Kaluza-Klein metric | $g = g_B + Q(\omega, \omega)$ | Eq. (25) |

## Relevance to Phonon-Exflation

This paper provides the mathematical machinery for deforming metrics on fiber bundles of the form $F \hookrightarrow M \to B$ where the structure group is compact -- exactly the setting of the phonon-exflation framework where $M^4 \times SU(3)/T$ is a fiber bundle with $SU(3)$ structure. The Cheeger deformation provides a one-parameter family of metrics on the total space that interpolates between the original metric and a regularized metric with totally geodesic fibers. The sectional curvature formula (Theorem 3.1) decomposes curvature into base + fiber + non-negative contributions, directly relevant to computing curvature properties of the Kaluza-Klein-type metrics in the framework. The regularization theorem (Theorem 3.2) implies that any metric on the total space can be deformed to one with totally geodesic internal fibers, providing a canonical limit for the tau-evolution dynamics.
