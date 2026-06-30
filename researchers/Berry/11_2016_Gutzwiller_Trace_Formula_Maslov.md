# Gutzwiller's Semiclassical Trace Formula and Maslov-Type Index Theory for Symplectic Paths

**Author(s):** Shanzhong Sun
**Year:** 2016
**Journal:** [not stated in PDF]
**arXiv:** 1608.08294
**Relevance:** MEDIUM

---

## Abstract

Gutzwiller's famous semiclassical trace formula plays an important role in theoretical and experimental quantum mechanics with tremendous success. We review the physical derivation of this deep periodic orbit theory in terms of the phase space formulation with a view towards the Hamiltonian dynamical systems. The Maslov phase appearing in the trace formula is clarified by Meinrenken as Conley-Zehnder index for periodic orbits of Hamiltonian systems. We also survey and compare various versions of Maslov indices to establish this fact. A refinement and improvement to Conley-Zehnder's index theory which we will recall all essential ingredients is the Maslov-type index theory for symplectic paths developed by Long and his collaborators which would shed new light on the computations and understandings on the semiclassical trace formula. The insights in Gutzwiller's work also seems plausible to the studies on Hamiltonian systems.

---

## Key Arguments and Derivations

### Section 1: Introduction

Classical mechanics evolved from Newtonian to Lagrangian (variational) to Hamiltonian (symplectic geometric) formulations. Poincare discovered classical chaos and emphasized the importance of periodic orbits. Einstein (1917) raised the question of quantum analogues of classical chaos. Gutzwiller (1970s) was the first to systematically study the classical-quantum correspondence in chaotic systems via a trace formula expressing the density of states in terms of periodic orbits of the classical Hamiltonian system. The Gutzwiller trace formula states that for hbar -> 0, the density of states rho(E) is approximated (up to the Weyl term) by a sum over all closed periodic orbits gamma with energy E, involving the classical action A_gamma, period T_gamma, linearized Poincare map P_gamma, and Conley-Zehnder index i_gamma. Berry generalized the random matrix ideas of Wigner and Dyson to quantum chaos. The Selberg trace formula for constant negative curvature surfaces is an exact special case.

### Section 2: Maslov Index from Lagrangian Grassmannian Perspective

The Lagrangian Grassmannian Lambda(n) = U(n)/O(n) has fundamental group pi_1 = Z. The Maslov index of a closed curve in Lambda(n) is its intersection number with the Maslov singular cycle. The triple Maslov index s(L_1, L_2, L_3) is the signature of the quadratic form Q on triples of Lagrangian subspaces, with properties including Sp(2n)-invariance, antisymmetry, cocycle identity, and symplectic additivity. The intersection number for pairs of Lagrangian paths and the Leray index on the universal cover are defined and their properties catalogued.

### Section 3: Maslov Index from Symplectic Group Perspective

The symplectic group Sp(2n) has pi_1 = Z (Gelfand-Lidskii theorem). The regular subset Sp(2n)*_omega has two simply connected components for each omega on the unit circle. The Conley-Zehnder/Maslov-type index i_1(gamma) is defined for paths gamma in P_tau(2n) starting at the identity. For nondegenerate paths, the index is the winding number k of the concatenation beta * gamma. For degenerate paths, the index is defined as the infimum over nearby nondegenerate paths. The Maslov-type index (i_1(gamma), nu_1(gamma)) is a pair of integers uniquely determined by five axioms: homotopy invariance, symplectic additivity, clockwise continuity, counterclockwise jumping, and normality. The Bott-type iteration formula relates indices of iterated paths to omega-indices. Splitting numbers S^+/- detect jumps of the index function at eigenvalues on the unit circle. The basic normal forms for symplectic matrices allow computational reduction.

### Section 4: Maslov Index and Morse Index

The Maslov-type index is a finite-dimensional representation of the infinite Morse index. For periodic boundary value problems of Hamiltonian systems, the saddle point reduction gives m^-(z) = d + i_1(x), m^0(z) = nu_1(x). For Lagrangian systems with Legendre convexity, m^-(x) = i_1(gamma_x), m^0(x) = nu_1(gamma_x) (Viterbo, An-Long).

### Section 5: Gutzwiller's Semiclassical Trace Formula (Physical Derivation via WKB)

The derivation proceeds through: (1) WKB ansatz psi_sc = A exp(iR/hbar) inserted into the Schrodinger equation yields the Hamilton-Jacobi equation and Madelung flow conservation; (2) the semiclassical Van Vleck propagator is obtained by evolving the short-time propagator with Jacobian determinants and Maslov indices; (3) Laplace transform gives the semiclassical Green function, with stationary phase yielding the action functional A_gamma = integral of p dq; (4) taking the trace with stationary phase gives the condition p = p' (periodic orbits); (5) the final formula involves the period T_gamma, monodromy matrix (I - M_gamma), classical action, and Maslov index. The zero-length (Weyl) contribution is computed separately via short-time propagator asymptotics, recovering the average density of states.

### Section 5.3: Selberg Trace Formula

The Selberg trace formula for compact Riemann surfaces of constant negative curvature is an exact trace formula relating the spectrum of the Laplacian to lengths of closed geodesics. It is derived by: (1) writing the Green function on Gamma\H^2 as a sum over the Fuchsian group; (2) regularizing by differentiating with respect to lambda; (3) evaluating the trace in two ways (eigenfunction expansion vs. conjugacy class decomposition). The heat kernel choice h(r) = exp(-tr^2) gives the trace of the heat operator.

### Section 5.4: Trace Formula and Maslov-type Index

Meinrenken clarified that the Maslov phase in the Gutzwiller trace formula is the Conley-Zehnder index for a symplectic path associated to the Poincare map of the periodic orbit. The Maslov-type index theory of Long provides effective computational tools through basic normal form decomposition and iteration formulas.

## Key Results

1. **Gutzwiller trace formula**: Density of states approximated by Weyl term plus sum over periodic orbits weighted by period, action, monodromy, and Maslov index
2. **Maslov phase = Conley-Zehnder index**: Meinrenken's identification of the phase appearing in the trace formula
3. **Five-axiom characterization** of the Maslov-type index (Long): homotopy invariance, symplectic additivity, clockwise continuity, counterclockwise jumping, normality
4. **Bott-type iteration formula**: i_z(gamma, m) = sum_{omega^m=z} i_omega(gamma) relates iterated indices to omega-indices
5. **Morse-Maslov correspondence**: m^-(z) = d + i_1(x) connects infinite Morse indices to finite Maslov-type indices
6. **Selberg trace formula** as an exact special case of Gutzwiller's formula for constant negative curvature surfaces
7. **Basic normal form decomposition** reduces Maslov index computation to 2x2 and 4x4 symplectic matrices

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Density of states | $\rho(E) := \sum_{j=0}^\infty \delta(E - E_j) = \bar{\rho}(E) + \tilde{\rho}(E)$ | Sec. 1 |
| Gutzwiller trace formula | $\tilde{\rho}(E) \approx \frac{1}{\pi\hbar}\operatorname{Re}\sum_\gamma \sqrt{-1}^{-i_\gamma}\frac{T_\gamma e^{\frac{\sqrt{-1}}{\hbar}\mathcal{A}_\gamma}}{\sqrt{\lvert\det(P_\gamma - I)\rvert}}$ | Sec. 1 |
| Symplectic group | $\operatorname{Sp}(2n) := \{M \in GL(2n,\mathbb{R}) \mid M^\top J M = J\}$ | Sec. 2.1 |
| Lagrangian Grassmannian | $\Lambda(n) = U(n)/O(n), \quad \pi_1(\Lambda(n)) \cong \mathbb{Z}$ | Prop. 1-2 |
| Triple Maslov index | $s(L_1,L_2,L_3) := \operatorname{sgn}(Q(L_1,L_2,L_3))$ | Sec. 2.2 |
| Maslov-type index (degenerate) | $i_1(\gamma) := \inf\{i_1(\beta) \mid \beta \in \mathcal{P}_\tau^*(2n),\;\beta\text{ close to }\gamma\}$ | Def. 18/Thm. 19 |
| Bott-type iteration | $i_z(\gamma,m) = \sum_{\omega^m=z} i_\omega(\gamma)$ | Thm. 22 |
| Van Vleck propagator | $K_{sc}(q,q',t) = \sum_\gamma \frac{\lvert\det(-\partial_q\partial_{q'}R_\gamma)\rvert^{1/2}}{(2\pi\sqrt{-1}\hbar)^{n/2}} e^{\sqrt{-1}R_\gamma/\hbar - \sqrt{-1}\pi i_\gamma/2}$ | Sec. 5.1 |
| Green function trace | $\operatorname{Tr}G_\gamma = \frac{T_\gamma\, e^{\sqrt{-1}\mathcal{A}_\gamma/\hbar - \sqrt{-1}\pi i_\gamma/2}}{\sqrt{-1}\hbar\,\lvert\det(I-M_\gamma)\rvert^{1/2}}$ | Sec. 5.1 |
| Selberg trace formula | $\sum_{k=0}^\infty h(r_k) = \frac{\operatorname{Area}(\Gamma\backslash\mathbb{H}^2)}{4\pi}\int_{-\infty}^{\infty} h(r)\tanh(\pi r)\,r\,dr + \sum_{\gamma\in H_*}\sum_{k=1}^\infty \frac{\tau_\gamma g(k\tau_\gamma)}{2\sinh(k\tau_\gamma/2)}$ | Thm. 32 |

## Relevance to Phonon-Exflation

The Gutzwiller trace formula and its Maslov index structure are relevant to the phonon-exflation framework's spectral action computations. The spectral action Tr(f(D/Lambda)) involves a trace over the Dirac operator eigenvalues whose asymptotic expansion connects to heat kernel coefficients -- the same Weyl-term + oscillatory structure that appears in the Gutzwiller formula. The Maslov index counts phase losses at caustics (turning points) in semiclassical propagation; in the M4 x SU(3) fiber geometry, the analogous quantity would be the eta invariant or spectral asymmetry of the Dirac operator on the compactified fiber, which enters the index theorems governing fermion number. The Selberg trace formula section is relevant because the hyperbolic geometry of constant negative curvature surfaces has structural parallels to the compactification geometry when the fiber metric has negative scalar curvature regions.
