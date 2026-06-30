# Tropical Spectral Curves, Fay's Trisecant Identity, and Generalized Ultradiscrete Toda Lattice

**Authors:** Rei Inoue and Shinsuke Iwao
**Year:** 2010
**Journal:** arXiv:1003.0057v2 [math.AG] (May 2010)
**DOI/arXiv:** [arXiv:1003.0057](https://arxiv.org/abs/1003.0057)

---

## Abstract

This paper studies the generalized ultradiscrete periodic Toda lattice T(M,N), which possesses tropical spectral curves. The authors introduce a tropical analogue of Fay's trisecant identity for both hyperelliptic and more general tropical curves, then apply it to construct general solutions to T(M,N). The work connects tropical geometry to integrable systems through the explicit construction of tropical Jacobian varieties and tropical Riemann theta functions.

---

## Historical Context

Tropical geometry emerged in the early 2000s as a combinatorial algebraic geometry rooted in non-Archimedean valuation theory. This paper is a landmark contribution that demonstrates deep connections between tropical geometry and classical integrable systems. The ultradiscrete Toda lattice itself arises as a piecewise-linear approximation to the continuous Toda lattice through a process called ultradiscretization. Inoue and Iwao's work shows that this discrete limit naturally exhibits tropical structure, with spectral curves becoming piecewise-linear objects in the tropical setting. This bridges the classical theory of integrable systems (Lax pairs, Jacobi varieties, theta functions) with the newer tropical algebraic geometry, revealing a hidden geometric structure that simplifies both the mathematics and the physics of the system.

---

## Key Arguments and Derivations

### Tropical Geometry Fundamentals

The paper begins with the construction of tropical curves as the limit of algebraic curves under non-Archimedean valuation. For a field $K_\varepsilon$ of convergent Puiseux series in $\varepsilon = e^{-1/\varepsilon}$ over a field $K$, and a polynomial $f_\varepsilon \in K_\varepsilon[x,y]$, the **tropical polynomial** is defined as:

$$\text{Val}(X, Y; f_\varepsilon) := \min_{w \in \mathbb{Z}^2} [\text{val}(a_w) + w_1 X + w_2 Y]$$

where $\text{val}$ is the natural valuation. The tropical curve $TV(f_\varepsilon)$ is the set of points $(X,Y) \in \mathbb{R}^2$ where this piecewise-linear function is not smooth (the "bend locus").

### Good Tropicalization and Hyperelliptic Curves

A curve $C(f_\varepsilon)$ has a **good tropicalization** if:
1. $C(f_\varepsilon)$ is an irreducible, reduced, nonsingular curve over $K_\varepsilon$
2. At each point $P$ on the tropical curve, the "fiber polynomial" $f_\varepsilon^P = \sum_{w \in \Lambda(P)} a_w x^{w_1} y^{w_2}$ defines a nonsingular (possibly reducible) affine curve

This ensures that the tropical curve inherits the essential topological properties of the algebraic curve (genus, dimension, intersection multiplicities).

### Tropical Riemann Theta Function

For a positive-definite symmetric matrix $B \in M_g(\mathbb{R})$ and $\beta \in \mathbb{R}^g$, the **tropical Riemann theta function** is:

$$\Theta(Z; B) = \min_{m \in \mathbb{Z}^g} \left[\tfrac{1}{2} m^\top B m + m(Z + \beta B)^\top \right]$$

where the minimum is taken over integer vectors $m$. This satisfies quasi-periodicity:

$$\Theta^{[\beta]}(Z + K l) = -\tfrac{1}{2} l^\top K l - l Z^\top + \Theta^{[\beta]}(Z)$$

for $l \in \mathbb{Z}^g$. The tropical theta function plays the same role in tropical geometry as the classical Riemann theta function does in algebraic geometry.

### Tropical Fay's Trisecant Identity (Theorem 2.2)

The paper's centerpiece is a tropical analogue of Fay's trisecant identity, a classical identity from the theory of algebraic curves that relates theta functions at four points:

**Theorem 2.2** (Tropical Fay): For a smooth tropical curve $\Gamma = TV(f_\varepsilon)$ of genus $g$ and points $P_1, P_2, P_3, P_4$ on its universal cover, with appropriate sign assignments $s_i \in \{\pm 1\}$ determined by theta characteristic data, define:

$$F_1(Z) = \Theta(Z + \int_{P_3}^{P_1}) + \Theta(Z + \int_{P_4}^{P_2}) + \Theta^{[\beta]}(\int_{P_2}^{P_3}) + \Theta^{[\beta]}(\int_{P_4}^{P_1})$$

and similarly for $F_2(Z), F_3(Z)$. Then:

$$F_i(Z) = \min[F_{i+1}(Z), F_{i+2}(Z)]$$

This is a tropical version of a classical identity, where the additive structure of the classical identity becomes the min structure of tropical arithmetic.

### Generalized Ultradiscrete Toda Lattice T(M,N)

The continuous Toda lattice is a classical integrable system; its discrete version reads:

$$I_n^{t+1} + V_n^{t+1}_M - I_n^t - V_n^t = 0$$

The **generalized ultradiscrete version** T(M,N) is defined by the piecewise-linear map:

$$Q_n^{t+1} = \min[W_n^t, Q_n^t - X_n^t]$$
$$W_n^{t+1}_M = Q_n^{t+1} + W_n^t - Q_n^{t+1}$$

where the evolution is indexed by $n \in \mathbb{Z}/N\mathbb{Z}$ (spatial index) and $t \in \mathbb{Z}/M$ (temporal index). The variables $(Q_n^t, W_n^t)$ are the tropical logs of the original variables $(I_n^t, V_n^t)$.

The spectral curve of this system is characterized by a Lax matrix $L^t(y)$, and the tropicalization of the spectral curve equation yields the tropical polynomial space $\mathcal{F}$ (Eq. 3.7), a set of piecewise-linear functions on the phase space.

### Proposition 3.1: Functional Independence

The paper proves that all spectral polynomial invariants in $\mathcal{F}$ are functionally independent in the coordinate ring $\mathbb{C}[L]$. This is the tropical analogue of a classical result by Mumford and van Moerbeke: the Jacobian of the map $\psi: \mathcal{T} \to L$ (from phase space to Lax matrix space) has full rank generically, guaranteeing that the isolevel sets of the spectral curves form Jacobian varieties.

### Example: T(3,2) and Bilinear Solutions

For the T(3,2) case, the spectral curve is:

$$f_\varepsilon = y^4 + y^3 f_{30} + y^2(x f_{21} + f_{20}) + y(-x^2 + x f_{11} + f_{10}) + f_0$$

The corresponding tropical curve $\Gamma$ has genus $g = 2$. The period matrix is:

$$B = \begin{pmatrix} 2F_0 - 7F_{11} + F_{20} & F_{11} - F_{20} \\ F_{11} - F_{20} & F_{11} + F_{20} \end{pmatrix}$$

and the tropical Jacobian is $J(\Gamma) = \mathbb{R}^2 / \mathbb{Z}^2 B$. By applying the tropical Fay identity to points $R, Q, P, A_i$ on $\tilde{\Gamma}$, Inoue and Iwao construct explicit bilinear solutions:

$$T_n^t = \Theta(Z_0 - \vec{L}_n + \vec{\lambda}_t)$$

where $\vec{L}_n$ and $\vec{\lambda}_t$ are appropriately chosen integration paths, satisfying the bilinear form:

$$T_n^t + T_{n+1}^{t+1+1/3M} = \min[T_n^{t+1} + T_n^{t+1/3M}, T_{n-1}^{t+1+1/3M} + T_{n+1}^t + \theta[t]]$$

The general solution to T(3,2) is then obtained via a transformation relating the bilinear variables to $(Q_n^t, W_n^t)$.

### Proposition 4.3: General Solution to T(3,2)

Fixing $Z_0 \in \mathbb{R}^2$ and choosing $\{i,j\} \subset \{1,2,3\}$, define:

$$T_n^t = \Theta(Z_0 - \vec{L}_n + \vec{\lambda}_t)$$
$$T_{3n}^{t+1} = \Theta(Z_0 - \vec{L}_n + \vec{\lambda}_t + \vec{\lambda}_i)$$
$$T_{3n}^{t+2} = \Theta(Z_0 - \vec{L}_n + \vec{\lambda}_t + \vec{\lambda}_i + \vec{\lambda}_j)$$

Then $(T_n^t)$ satisfies the bilinear equation with appropriate quasi-periodic constants, and the transformation (4.2) yields a general solution to T(3,2). The choice of $\{i,j\}$ yields $3! = 6$ distinct solution types.

### Conjectures on T(M,N)

The paper proposes two conjectures extending the T(3,2) analysis to arbitrary M and N (with $\gcd(M,N) = 1$):

**Conjecture 4.1:** For $\sigma \in S_M$ (the symmetric group of order M) and $Z_0 \in \mathbb{R}^g$,

$$T_n^{t+k/M} = \Theta(Z_0 - \vec{L}_n + \vec{\lambda}_{t+k} + \sum_{i=1}^k \vec{\lambda}_{\sigma(i)})$$

then $(T_n^t)$ satisfies the bilinear equation and yields a general solution to T(M,N).

**Conjecture 4.2:** The solutions induced from Conjecture 4.1 establish an isomorphism $J(\Gamma)^{\oplus M!} \cong \Phi^{-1}(\xi)$, where $\Phi^{-1}(\xi)$ is the isolevel set of the tropical polynomial $\xi$.

These conjectures have been fully proven for T(1,g+1) and T(2g-1,2).

---

## Key Results

1. **Tropical Algebraic Geometry Applied to Integrable Systems**: The paper establishes that integrable systems naturally exhibit tropical structure when placed in a non-Archimedean limit.

2. **Tropical Fay Identity Generalization**: A tropical analogue of Fay's trisecant identity is proved for general tropical curves (Theorem 2.2), extending previous results limited to hyperelliptic cases.

3. **Explicit Theta Function Solutions**: General solutions to the ultradiscrete Toda lattice are constructed explicitly in terms of tropical Riemann theta functions, providing a complete algebraic-geometric characterization.

4. **Tropical Jacobian Isomorphism**: For generic spectral curves with good tropicalization, the isolevel sets of spectral polynomials are isomorphic to tropical Jacobian varieties.

5. **Functional Independence of Spectral Invariants**: Proposition 3.1 establishes that all spectral polynomial invariants in the tropical setting are functionally independent (a rank-full result).

6. **Connection to Box-Ball Systems**: The paper establishes a correspondence between the generalized ultradiscrete Toda lattice and the periodic box-ball system (pBBS) of M types of balls, relating their tropical geometric structures.

---

## Impact and Legacy

This paper opened a major research direction connecting tropical geometry and classical integrable systems. The tropical Fay identity has become a fundamental tool in the study of piecewise-linear integrable systems and cellular automata. Subsequent work has extended these methods to:
- Box-ball systems and tropical soliton cellular automata
- The study of generalized Bethe ansatz in the tropical setting
- Tropical Riemann-Roch theorem applications to integrable dynamics
- Generalized hydrodynamics of integrable soliton gases

The paper is cited as a canonical reference for understanding how classical integrable structure (Lax pairs, spectral curves, theta functions) maps into the tropical piecewise-linear world. It demonstrates that topological and algebraic invariants are preserved under tropicalization, providing a powerful tool for analyzing discrete and ultradiscrete systems.

---

## Connection to Phonon-Exflation Framework

**DIRECT RELEVANCE**: The tropical spectral curves framework is a potential model for understanding the **BCS ground-state energy staircase $E_{GS}(N)$ as a tropicalization of the spectral action**.

In phonon-exflation, the spectral action $S_{spec}[\mathcal{D}]$ is the sum of eigenvalues of the Dirac operator $\mathcal{D}$ in the NCG formalism. The ground-state energy as a function of particle number N exhibits a staircase pattern due to BCS level-crossings and avoided crossings.

**Mechanism parallel:**
- In the Toda lattice, the integrable structure ensures that solutions remain finite and well-ordered despite the coupling complexity.
- In the BCS pairing problem, the ground state energy can be approximated by a piecewise-linear function when one tracks which pair-levels are occupied.
- Both systems have **spectral curves** (algebraic in the classical case, tropical in the piecewise limit).
- Both admit **theta-function parameterizations** of their solution spaces.

The BCS staircase could potentially be viewed as a tropical limit of the spectral action: the smooth algebraic curve becomes piecewise-linear, and the eigenvalue sum becomes a minimum over configurations. If this analogy holds, the tropical Fay identity could provide a tool for proving properties of the BCS pairing staircase without solving the full Bogoliubov-de Gennes equations.

**Gap**: The paper does not explicitly address spectral actions or Dirac operators, only Toda-lattice-type systems. However, the generalized spectral-curve framework (genus, period matrices, theta functions) is exactly the structure that appears in both the Dirac spectrum and the integrable systems studied here.

