# What is the Geometry of Superspace?

**Author(s):** Domenico Giulini
**Year:** 1993
**Journal:** Contribution to the Proceedings of the conference on Mach's Principle: "From Newton's Bucket to Quantum Gravity", Tubingen, Germany, July 26-30, 1993. Freiburg THEP-93/26.
**arXiv:** gr-qc/9311017
**Relevance:** MEDIUM

---

## Abstract

We investigate certain properties of the Wheeler-DeWitt metric (for constant lapse) in canonical General Relativity associated with its non-definite nature.

---

## Key Arguments and Derivations

### Configuration Space and Superspace

The dynamics of General Relativity is formulated as a constrained Hamiltonian system. The configuration space for pure gravity is $\mathcal{Q}(\Sigma)$: the space of all Riemannian metrics on a 3-manifold $\Sigma$ of fixed but arbitrary topology. Spacetime is viewed as a history of dynamically evolving geometries on $\Sigma$, represented by a path $g_{ab}(s)$ in $\mathcal{Q}(\Sigma)$.

In the gauge $N=1$, $N^a = 0$, vacuum Einstein equations decompose into:

**Dynamical part:**
$$\ddot{g}_{ab} + \Gamma^{kl}_{ab}\dot{g}_{ij}\dot{g}_{kl} = -2(R_{ab} - \frac{1}{4}g_{ab}R)$$

**Hamiltonian constraint:**
$$G^{abcd}\dot{g}_{ab}\dot{g}_{cd} - 4\sqrt{g}R = 0$$

**Momentum constraint:**
$$G^{abcd}\nabla_b\dot{g}_{cd} = 0$$

The superspace $\mathcal{S}(\Sigma) := \mathcal{Q}(\Sigma)/\mathcal{D}(\Sigma)$ is obtained by quotienting by the diffeomorphism group, representing the space of geometries rather than metrics.

### Ultralocal Metrics: One-Parameter Family

The author introduces a one-parameter family of ultralocal metrics $G_\beta$ on $\mathcal{Q}(\Sigma)$:

$$G_\beta(h,k) := \int_\Sigma G^{abcd}_\beta h_{ab} k_{cd} \, d^3x$$

where:

$$G^{abcd}_\beta = \frac{\sqrt{g}}{2}(g^{ac}g^{bd} + g^{ad}g^{bc} - 2\beta g^{ab}g^{cd})$$

The Wheeler-DeWitt (WDW) metric corresponds to $\beta = 1$. The inverse metric uses $\alpha + \beta = 3\alpha\beta$.

**Signature properties:**
- For $\beta < 1/3$: positive definite
- For $\beta = 1/3$: degenerate (excluded)
- For $\beta > 1/3$: mixed signature with infinitely many plus and minus signs

### Warped Product Structure

Because the metrics are ultralocal, they arise from metrics on the 6-dimensional space $S^+_3$ of symmetric positive definite $3 \times 3$ matrices ($\cong GL(3,\mathbb{R})/SO(3) \cong \mathbb{R}^5 \times \mathbb{R}^+$). The metric takes warped-product form:

$$G^{abcd}_\beta dg_{ab} \otimes dg_{cd} = -\epsilon \, d\tau \otimes d\tau + \frac{\tau^2}{c^2}\text{tr}(r^{-1}dr \otimes r^{-1}dr)$$

where $c^2 = 16|\beta - 1/3|$, $\tau = cg^{1/4}$, $r_{ab} = g^{-1/3}g_{ab}$, and $\epsilon = \text{sign}(\beta - 1/3)$.

### Vertical and Horizontal Subspaces

Diffeomorphisms generate "vertical" directions in $\mathcal{Q}(\Sigma)$ via vector fields $X^\xi_{ab} = \nabla_a\xi_b + \nabla_b\xi_a$ (Killing fields of $G_\beta$). The "horizontal" subspace $H^\beta_g$ is the $G_\beta$-orthogonal complement. A vector $k_{ab}$ is horizontal iff:

$$\nabla^a(k_{ab} - \beta g_{ab}k^c_c) = 0$$

The critical question is whether horizontal and vertical subspaces intersect non-trivially. This is governed by the operator:

$$D_\beta = \delta d + 2(1-\beta)d\delta - 2\text{Ric}$$

where $\delta$ is minus the divergence on the first index, $d$ is the exterior derivative, and Ric is the map induced by $R^b_a$.

### Key Results for the WDW Metric ($\beta = 1$)

**Ricci-negative metrics:** For Ric $< 0$, $D_1$ is manifestly positive, so $V_g \cap H^1_g = \{0\}$. The WDW metric on superspace is well-defined with infinitely many plus and minus signs. Every 3-manifold admits Ricci-negative metrics (Gao and Yau 1986).

**Flat metrics:** For $\beta = 1$ and $g$ flat, vectors of the form $k_{ab} = \nabla_a\nabla_b\phi$ are simultaneously horizontal and vertical, giving an infinite-dimensional intersection $V_g \cap H^1_g$. This means the WDW metric is not defined for flat geometries.

**Einstein metrics (non-flat):** For $R_{ab} = \lambda g_{ab}$ with $\lambda \neq 0$, one can show $H^1_g \cap V_g = \{0\}$. The WDW metric exists and, for the round three-sphere, has Lorentzian signature $(-,+,+,+,\ldots)$.

### Three-Sphere Analysis

For the round metric on $S^3$, tensor harmonic decomposition reveals:
- For $1/3 < \beta < 1$: finitely many negative directions in $V_g$, infinitely many in $H^\beta_g$.
- At discrete values $\beta_n = (n^2-3)/(n^2-1)$ for $n \in \{3,4,5,\ldots\}$, $V_g \cap H^{\beta_n}_g$ is non-trivial with finite dimension $d_n > 0$.
- As $\beta$ increases through $\beta_n$, $d_n$ negative directions migrate from $H^\beta_g$ to $V_g$.
- At $\beta = 1$: only a single negative direction remains in $H^1_g$, giving Lorentzian signature $(-,+,+,+,\ldots)$ on superspace.

### Ellipticity Failure at $\beta = 1$

The principal symbol of $D_\beta$ is:

$$\sigma_\beta(\zeta)^a_b = \|\zeta\|^2\left(\delta^a_b + (1-2\beta)\frac{\zeta^a\zeta_b}{\|\zeta\|^2}\right)$$

- $\beta < 1$: strongly elliptic (positive definite)
- $\beta > 1$: elliptic but not strongly elliptic
- $\beta = 1$: degenerate elliptic (singular positive semi-definite). This means the WDW metric sits exactly at the boundary of ellipticity.

---

## Key Results

1. The WDW metric ($\beta = 1$) has a well-defined quotient metric on superspace at Ricci-negative geometries, with infinitely many plus and minus signs.
2. At flat geometries, the WDW metric fails to define a superspace metric due to infinite-dimensional intersection of vertical and horizontal subspaces.
3. For the round three-sphere, the superspace WDW metric has Lorentzian signature $(-,+,+,+,\ldots)$, directly related to the hyperbolicity of the Wheeler-DeWitt equation.
4. The transition from $\beta < 1$ to $\beta = 1$ is qualitatively singular: the operator $D_\beta$ changes from strongly elliptic to degenerate elliptic.
5. Signature changes necessarily occur in every superspace, signaled by non-trivial intersections of vertical and horizontal subspaces.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Dynamical Einstein eq | $\ddot{g}_{ab} + \Gamma^{kl}_{ab}\dot{g}_{ij}\dot{g}_{kl} = -2(R_{ab} - \frac{1}{4}g_{ab}R)$ | Eq. (1) |
| Hamiltonian constraint | $G^{abcd}\dot{g}_{ab}\dot{g}_{cd} - 4\sqrt{g}R = 0$ | Eq. (2) |
| Momentum constraint | $G^{abcd}\nabla_b\dot{g}_{cd} = 0$ | Eq. (3) |
| WDW metric | $G(h,k) = \int_\Sigma G^{abcd}h_{ab}k_{cd} \, d^3x$ | Eq. (4) |
| Ultralocal family | $G^{abcd}_\beta = \frac{\sqrt{g}}{2}(g^{ac}g^{bd} + g^{ad}g^{bc} - 2\beta g^{ab}g^{cd})$ | Eq. (6) |
| Warped product | $G^{abcd}_\beta dg_{ab} \otimes dg_{cd} = -\epsilon \, d\tau \otimes d\tau + \frac{\tau^2}{c^2}\text{tr}(r^{-1}dr \otimes r^{-1}dr)$ | Eq. (10) |
| Warped parameters | $c^2 = 16\|\beta - 1/3\|, \; \tau = cg^{1/4}, \; r_{ab} = g^{-1/3}g_{ab}, \; \epsilon = \text{sign}(\beta - 1/3)$ | Eq. (11) |
| Horizontal condition | $\nabla^a(k_{ab} - \beta g_{ab}k^c_c) = 0$ | Eq. (13) |
| Operator $D_\beta$ | $D_\beta = \delta d + 2(1-\beta)d\delta - 2\text{Ric}$ | Eq. (15) |
| $G_\beta$-norm of $X_\xi$ | $G_\beta(X_\xi, X_\xi) = 2\int_\Sigma \xi^a D_\beta \xi_a \, d^3x$ | Eq. (16) |
| Critical $\beta$ values | $\beta_n = \frac{n^2-3}{n^2-1}, \quad n \in \{3,4,5,\ldots\}$ | Eq. (17) |
| Principal symbol | $\sigma_\beta(\zeta)^a_b = \|\zeta\|^2(\delta^a_b + (1-2\beta)\frac{\zeta^a\zeta_b}{\|\zeta\|^2})$ | Eq. (18) |

---

## Relevance to Phonon-Exflation

The phonon-exflation framework restricts dynamics to the TT (transverse-traceless) sector of perturbations around the SU(3) fiber geometry during the tau-transit. Giulini's analysis shows that the WDW metric restricted to horizontal (physical) directions has Lorentzian signature $(-,+,+,+,\ldots)$, with the single negative direction corresponding to the conformal (trace) mode. The project's TT-restricted sector (Session 12, Session 20b) remains strictly Riemannian throughout the transit precisely because TT perturbations lie in the positive-definite subspace $H^1_g$, excluding the conformal direction. This paper provides the mathematical foundation for why the TT sector is well-behaved: Giulini's warped-product decomposition shows the negative direction is pure trace ($\tau$ coordinate), while the $SL(3,\mathbb{R})/SO(3)$ part (shape deformations, including TT modes) is positive definite.
