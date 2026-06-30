# Indefinite Einstein metrics on simple Lie groups

**Author(s):** Andrzej Derdzinski, Swiatoslaw R. Gal
**Year:** 2012 (v2: 2013)
**Journal:** Indiana University Mathematics Journal (to appear at time of posting)
**arXiv:** 1209.6084
**Relevance:** MEDIUM-HIGH (directly determines Einstein metric isolation on SU(n))

---

## Abstract

The set $\mathcal{E}$ of Levi-Civita connections of left-invariant pseudo-Riemannian Einstein metrics on a given semisimple Lie group always includes $D$, the Levi-Civita connection of the Killing form. For the groups SU$(l,j)$ (or SL$(n,\mathbb{R})$, or SL$(n,\mathbb{C})$ or, if $n$ is even, SL$(n/2,\mathbb{H})$), with $0 \le j \le l$ and $j+l > 2$ (or, $n > 2$), we explicitly describe the connected component $\mathcal{C}$ of $\mathcal{E}$, containing $D$. It turns out that $\mathcal{C}$, a relatively-open subset of $\mathcal{E}$, is also an algebraic variety of real dimension $2lj$ (or, real/complex dimension $[n^2/2]$ or, respectively, real dimension $4[n^2/8]$), forming a union of $(j+1)(j+2)/2$ (or, $[n/2]+1$ or, respectively, $[n/4]+1$) orbits of the adjoint action. **In the case of SU$(n)$ one has $2lj = 0$, so that a positive-definite multiple of the Killing form is isolated among suitably normalized left-invariant Riemannian Einstein metrics on SU$(n)$.**

---

## Key Arguments and Derivations

### 1. Setup and Main Question (Section 1)

The Killing form $\beta$ of any semisimple real Lie group $G$ is a bi-invariant pseudo-Riemannian Einstein metric. The paper asks: what does the moduli space $\mathcal{E}$ of left-invariant Einstein connections look like near $D = [\ ,\ ]/2$ (the Levi-Civita connection of $\beta$)?

For compact simple groups other than SU(2) and SO(3), D'Atri-Ziller (1979) proved the existence of at least one left-invariant Riemannian Einstein metric not a multiple of $\beta$. Gibbons-Lu-Pope found more examples on SO(5) and $G_2$, plus an indefinite one on SU(3).

### 2. Outline of Method (Section 2)

The strategy replaces the cubic equation $H(S) = 0$ (weakly-Einstein condition, where $H: \mathcal{S} \to \mathcal{S}$ is a nonhomogeneous cubic polynomial) with a quadratic system. A bijective correspondence exists between:
- Weakly-Einstein connections $\mathcal{W} = D + H^{-1}(0)$
- Pairs $(S, \sigma) \in \mathcal{S} \times \mathcal{T}$ with $K(S, \sigma) = (0,0)$

where $K: \mathcal{S} \times \mathcal{T} \to \mathcal{S} \times \mathcal{T}$ is a nonhomogeneous quadratic mapping.

For $\mathfrak{g}$ in the list $\{\text{sl}(n,\mathbb{R}), \text{sl}(n,\mathbb{C}), \text{su}(l,j), \text{sl}(n/2,\mathbb{H})\}$ with $n \ge 3$, the authors parametrize solutions using special elements $\tau_a, \theta_a, \mu_a \in \mathcal{T}$ depending on $a \in \mathfrak{g}$, setting:
$$\lambda = x\tau_a + n^2 y\theta_a + z\mu_a, \quad \psi = p\tau_a + q\theta_a + r\mu_a + f\beta$$

The fundamental formula (eq. 2.7):
$$K(I_a[v]) - I_a[J(v)] - I_b[M(v)] \in \mathcal{N}$$
where $\mathcal{N}$ is the space of "negligible" functions (vanishing when $b = 0$), reduces the problem to algebraic conditions on vectors $v \in \mathbb{F}^9$.

### 3. The Family of Einstein Connections

A specific vector $u \in \mathbb{F}^9$ satisfies $J(u) = 0$ with $\xi = h = 0$. The family of Einstein connections is:
$$\mathcal{C} = D + \pi_{\mathcal{S}}(\{I_a[u] : a \in \mathfrak{g} \text{ and } a^2 = 0\})$$

Proof that $\mathcal{C} \subset \mathcal{E}$: When $a^2 = 0$ and $\xi = h = 0$, the condition $b = 0$ follows, negligible functions vanish, and $K(I_a[u]) = 0$.

### 4. Isolation Result

The crucial step: every real-analytic curve $[0,\delta) \ni t \mapsto D + S(t)$ of weakly-Einstein connections with $S(0) = 0$ lies entirely in $\mathcal{C}$ (proved by induction on jet order using the fundamental formula). By Milnor's curve-selection lemma (Corollary 4.2), $\mathcal{C}$ contains all weakly-Einstein connections sufficiently close to $D$.

**For $\mathfrak{g} = \text{su}(n)$**: The condition $a^2 = 0$ with $a \in \text{su}(n)$ forces $a = 0$ (since SU$(n)$ is compact, $a^2 = 0$ implies $\text{tr}(a^*a) = 0$). Therefore $\mathcal{C} = \{D\}$, and the Killing form is isolated.

**For remaining simple Lie algebras** (not in the list): The curvature operator $\Omega$ (acting on symmetric 2-tensors via the Killing metric) does not have eigenvalue 1. By Remark 12.3, this implies $D$ is an isolated point of $\mathcal{E}$. The converse holds except possibly for SU$(n)$ with $n \ge 3$.

### 5. The Curvature Operator $\Omega$ (from companion paper 1304.2801)

The operator $\Omega: [\mathfrak{g}^*]^{\odot 2} \to [\mathfrak{g}^*]^{\odot 2}$ acts on symmetric 2-tensors via:
$$[\Omega\sigma](x,y) = 2\text{tr}[(\text{Ad}_x)(\text{Ad}_y)\Sigma]$$
where $\sigma(x,y) = \beta(\Sigma x, y)$.

By Meyberg's theorem on trace formulas in simple Lie algebras, $\Omega$ is diagonalizable. The eigenvalue 1 occurs if and only if $\mathfrak{g} \cong \text{sl}(n,\mathbb{C})$ for $n \ge 3$ (and its real forms). For all other simple Lie algebras, 1 is NOT an eigenvalue of $\Omega$, ensuring isolation.

---

## Key Results

1. **MAIN THEOREM (Theorem 22.2)**: For $G$ in the list {SU$(l,j)$, SL$(n,\mathbb{R})$, SL$(n,\mathbb{C})$, SL$(n/2,\mathbb{H})$}, the connected component $\mathcal{C}$ of the Einstein connection moduli containing $D$ is an algebraic variety of dimension $d_\mathbb{F}$ over $\mathbb{F}$, parametrized by $\{a \in \mathfrak{g} : a^2 = 0\}$ via the explicit quadratic map $a \mapsto D + \pi_\mathcal{S}(I_a[u])$.

2. **ISOLATION ON SU$(n)$ (Theorem 22.3)**: On SU$(n)$, positive-definite multiples of the Killing form are isolated among suitably normalized left-invariant Riemannian Einstein metrics. This confirms a special case of the Bohm-Wang-Ziller conjecture.

3. **Dimension formula**: $\dim_\mathbb{F} \mathcal{C} = 2lj$ for SU$(l,j)$, $[n^2/2]$ for SL$(n,\mathbb{F})$, $4[n^2/8]$ for SL$(n/2,\mathbb{H})$. For SU$(n)$ (where $j=0$): $\dim = 0$, confirming isolation.

4. **Orbit decomposition**: $\mathcal{C}$ is a union of finitely many orbits of the adjoint action: $(j+1)(j+2)/2$ for SU$(l,j)$, $[n/2]+1$ for SL$(n,\mathbb{F})$, $[n/4]+1$ for SL$(n/2,\mathbb{H})$.

5. **All other simple groups**: For simple Lie algebras NOT isomorphic to sl$(n)$-type, $D$ is an isolated point of $\mathcal{E}$ — there are no nearby left-invariant Einstein metrics other than multiples of $\beta$.

6. **Holomorphic Einstein metrics on SL$(n,\mathbb{C})$ (Theorem 22.4)**: All left-invariant pseudo-Riemannian Einstein metrics on SL$(n,\mathbb{C})$ close to multiples of $\beta$ are real parts of holomorphic Einstein metrics (Kahler-Norden metrics).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Standard connection | $2D_v w = [v, w]$, so $D_v = \text{Ad}_v/2$ | Eq. (7.4) |
| Weakly-Einstein condition | $\nabla\{\nabla \cdot \nabla\} = 0$ | Eq. (2.1) |
| Quadratic reformulation | $K(S, \sigma) = (0,0)$ for $(S,\sigma) \in \mathcal{S} \times \mathcal{T}$ | Eq. (2.3) |
| Fundamental formula | $K(I_a[v]) - I_a[J(v)] - I_b[M(v)] \in \mathcal{N}$ | Eq. (2.7) |
| Einstein family | $\mathcal{C} = D + \pi_\mathcal{S}(\{I_a[u] : a \in \mathfrak{g}, a^2 = 0\})$ | Eq. (2.12) |
| Ricci tensor (unimodular) | $\rho(v,w) = -(\nabla_v, \nabla_w) = -\text{tr}(\nabla_v \circ \nabla_w)$ | Lemma 6.1(d) |
| Curvature operator | $[\Omega\sigma](x,y) = 2\text{tr}[(\text{Ad}_x)(\text{Ad}_y)\Sigma]$ | Eq. (1.2) of [46] |
| Dimension of $\mathcal{C}$ for SU$(l,j)$ | $\dim_\mathbb{R} \mathcal{C} = 2lj$ | Thm 22.2 |
| Dimension of $\mathcal{C}$ for SU$(n)$ | $\dim \mathcal{C} = 0$ (isolated) | Thm 22.3 |
| Eigenvalue condition for isolation | $1 \notin \text{Spec}(\Omega) \Rightarrow D$ isolated in $\mathcal{E}$ | Rem. 12.3 |

---

## Relevance to Phonon-Exflation

**This paper is critically important for the framework.** It establishes:

1. **The bi-invariant metric on SU(3) is ISOLATED among left-invariant Einstein metrics**: Since SU(3) = SU(3,0) has $j = 0$, the dimension of the Einstein moduli near $\beta$ is $2lj = 0$. This means there are no nearby left-invariant Riemannian Einstein metrics other than rescalings of the Killing form. This is exactly the framework's setup: Jensen deformation moves SU(3) OFF the Einstein locus — the deformed metric at $\tau \ne 0$ is NOT Einstein.

2. **The Jensen deformation is necessarily non-Einstein**: Combined with Theorem 22.3, the Jensen metric $g(\tau)$ for $\tau > 0$ cannot be Einstein (since positive multiples of $\beta$ are the only nearby Einstein metrics, and Jensen deformation changes the geometry non-trivially). This confirms that the spectral action on the deformed SU(3) sees a geometry that has departed from the Einstein condition — which is exactly what drives the tau-dynamics in the framework.

3. **Curvature operator eigenvalue 1**: For SU$(n)$ with $n \ge 3$, the eigenvalue 1 of $\Omega$ IS present (since SU$(n)$ is a real form of sl$(n,\mathbb{C})$, which has eigenvalue 1 by Meyberg's theorem via Lemma 2.2(d) of the companion paper). However, this does NOT prevent isolation in the Riemannian case — the moduli from eigenvalue-1 deformations are indefinite (pseudo-Riemannian), not positive-definite. The compact form SU$(n)$ has $a^2 = 0 \Rightarrow a = 0$, killing all deformations.

4. **Contrast with noncompact forms**: For SU$(l,j)$ with $j \ge 1$, there IS a moduli of dimension $2lj$ of nearby Einstein metrics — but these are all indefinite. This is relevant if the framework ever considers signature changes or analytic continuation to indefinite metrics on the internal space.
