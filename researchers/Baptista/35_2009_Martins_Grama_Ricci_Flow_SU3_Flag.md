# The Ricci Flow of Left Invariant Metrics on Full Flag Manifold SU(3)/T from a Dynamical Systems Point of View

**Author(s):** Lino Grama, Ricardo M. Martins
**Year:** 2009
**Journal:** [not stated in PDF]
**arXiv:** 0903.2761
**Relevance:** MEDIUM

---

## Abstract

In this paper we study the behavior of the Ricci flow at infinity for the full flag manifold SU(3)/T using techniques of the qualitative theory of differential equations, in special the Poincare Compactification and Lyapunov exponents. We prove that there are four invariant lines for the Ricci flow equation, each one associated with a singularity corresponding to a Einstein metric. In such manifold, the bi-invariant normal metric is Einstein. Moreover, around each invariant line there is a cylinder of initial conditions such that the limit metric under the Ricci flow is the corresponding Einstein metric; in particular we obtain the convergence of left-invariant metrics to a bi-invariant metric under the Ricci flow.

---

## Key Arguments and Derivations

### Section 2: Invariant Metrics and Ricci Tensor Equations in Flag Manifolds

The paper studies the full flag manifold $\mathbb{F}(3) = SU(3)/T$, where $T = S(U(1) \times U(1) \times U(1))$ is the maximal torus of $SU(3)$. The tangent space decomposes into three irreducible non-equivalent $\text{Ad}(H)$-submodules $\mathfrak{m} = \mathfrak{m}_{12} \oplus \mathfrak{m}_{23} \oplus \mathfrak{m}_{13}$, so an invariant metric is parametrized by three positive constants $(\lambda_{12}, \lambda_{13}, \lambda_{23})$ via $B(X,Y) = \lambda_{12} K(X,Y)|_{\mathfrak{m}_{12}} \oplus \lambda_{23} K(X,Y)|_{\mathfrak{m}_{23}} \oplus \lambda_{13} K(X,Y)|_{\mathfrak{m}_{13}}$.

The Ricci tensor components are computed (following Sakane and Arvanitoyergos) and the Ricci flow $\dot{\lambda}_{ij} = -2r_{ij}$ reduces to an autonomous nonlinear ODE system.

### Section 3: Poincare Compactification

The Ricci flow ODE, after the time reparametrization $\rho = 6/(\lambda_{12}\lambda_{13}\lambda_{23})$, becomes the polynomial quadratic system (8). The Poincare compactification method is used to study the behavior at infinity, projecting $\mathbb{R}^3$ onto $S^3$ via central projection. The system is expressed in three local charts $U_1, U_2, U_3$.

### Section 4: Qualitative Behavior of the Ricci Flow

**Theorem 1:** The Ricci flow of left-invariant metrics on $\mathbb{F}(3)$ has no singularities in finite time for any initial condition.

After compactification, 10 distinct singularities at infinity are found on the equator of $S^3$. Four of these lie in the positive octant (the physically meaningful region):
- $p_1' \sim (0.198756, 0.959682, 0.198756)$
- $p_2' \sim (0.577350, 0.577350, 0.577350)$ -- the bi-invariant normal metric
- $p_3' \sim (0.198756, 0.198756, 0.959682)$
- $p_4' \sim (0.959682, 0.198756, 0.198756)$

**Theorem 2:** The four lines $\gamma_j(t) = t p_j'$ are solutions of the Ricci flow system (both (4) and (8)).

The points $p_1, p_3, p_4$ are saddles and $p_2$ (the normal metric) is an attractor.

Lyapunov exponents are computed in chart $U_1$ for all four invariant lines. All exponents are negative for all four solutions, confirming stability.

**Theorem 3:** For initial conditions sufficiently close to any invariant line $\gamma_j$ and sufficiently far from the origin, solutions remain close to $\gamma_j$ and converge to $p_j$ in the compactification.

**Theorem 4 (Geometric translation):** For the Ricci flow $g_t$ with initial metric $g_0$ near an invariant line:
- If $j \in \{1, 3, 4\}$, then $g_\infty$ is an Einstein metric.
- If $j = 2$, then $g_\infty$ is the normal (Einstein) metric. In particular, if $g_0$ is left-invariant but not on $\gamma_2$, then $g_\infty$ is bi-invariant.

## Key Results

1. The Ricci flow of left-invariant metrics on $SU(3)/T$ has no finite-time singularities (Theorem 1).
2. There are exactly four invariant lines for the Ricci flow equation, each associated with an Einstein metric at infinity (Theorem 2).
3. All Lyapunov exponents for all four invariant lines are negative (Table 1), establishing stability.
4. Around each invariant line there is a cylinder of initial conditions whose Ricci flow converges to the corresponding Einstein metric (Theorem 3).
5. Left-invariant metrics near the normal metric line converge under Ricci flow to the bi-invariant (normal) Einstein metric (Theorem 4).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Ricci flow | $\frac{\partial g(t)}{\partial t} = -2\text{Ric}(g(t))$ | Eq. (1) |
| Flag manifold | $M = \frac{SU(3)}{S(U(1) \times U(1) \times U(1))}$ | Eq. (2) |
| Ricci component $r_{12}$ | $r_{12} = \frac{1}{2\lambda_{12}} + \frac{1}{12}\left(\frac{\lambda_{12}}{\lambda_{13}\lambda_{23}} - \frac{\lambda_{13}}{\lambda_{12}\lambda_{23}} - \frac{\lambda_{23}}{\lambda_{12}\lambda_{13}}\right)$ | Eq. (3) |
| Ricci component $r_{13}$ | $r_{13} = \frac{1}{2\lambda_{13}} + \frac{1}{12}\left(\frac{\lambda_{13}}{\lambda_{12}\lambda_{23}} - \frac{\lambda_{12}}{\lambda_{13}\lambda_{23}} - \frac{\lambda_{23}}{\lambda_{12}\lambda_{13}}\right)$ | Eq. (3) |
| Ricci component $r_{23}$ | $r_{23} = \frac{1}{2\lambda_{23}} + \frac{1}{12}\left(\frac{\lambda_{23}}{\lambda_{12}\lambda_{13}} - \frac{\lambda_{13}}{\lambda_{23}\lambda_{12}} - \frac{\lambda_{12}}{\lambda_{23}\lambda_{13}}\right)$ | Eq. (3) |
| Flow ODE | $\dot{\lambda}_{ij} = -2r_{ij}, \quad 1 \le i < j \le 3$ | Eq. (4) |
| Polynomial system | $\dot{\lambda}_{12} = 6\lambda_{13}\lambda_{23} + \lambda_{12}^2 - \lambda_{13}^2 - \lambda_{23}^2$ (and cyclic permutations) | Eq. (8) |

## Relevance to Phonon-Exflation

This paper characterizes the Ricci flow on the exact internal space $SU(3)/T$ of the phonon-exflation framework. The four Einstein metrics and their basins of attraction under the Ricci flow define the possible asymptotic geometries the internal space can evolve toward. The fact that the normal metric $p_2$ (the bi-invariant metric with $\lambda_{12} = \lambda_{13} = \lambda_{23}$) is an attractor means the Ricci flow drives generic left-invariant metrics toward the maximally symmetric configuration. This is directly relevant to the tau-evolution: if the internal geometry is modeled as a 3-parameter family of invariant metrics on $SU(3)/T$, the Ricci flow provides a concrete dynamical system governing its evolution, with the four invariant lines corresponding to distinct Einstein attractors. The three saddle-type Einstein metrics ($p_1, p_3, p_4$) with broken permutation symmetry among the $\lambda_{ij}$ correspond to geometries where one fiber direction is enhanced relative to the others -- potentially relevant to the fold dynamics at finite tau.
