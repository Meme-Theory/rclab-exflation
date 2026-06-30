# Non-abelian vortices on compact Riemann surfaces

**Author(s):** J. M. Baptista
**Year:** 2008 (published 2009)
**Journal:** Commun. Math. Phys. 291, 799 (2009)
**arXiv:** 0810.3220
**Relevance:** LOW (vortex foundations, not directly used in KK program)

---

## Abstract

We consider the vortex equations for a U(n) gauge field A coupled to a Higgs field phi with values on the n x n matrices. It is known that when these equations are defined on a compact Riemann surface Sigma, their moduli space of solutions is closely related to a moduli space of tau-stable holomorphic n-pairs on that surface. Using this fact and a local factorization result for the matrix phi, we show that the vortex solutions are entirely characterized by the location in Sigma of the zeros of det phi and by the choice of a vortex internal structure at each of these zeros. We describe explicitly the vortex internal spaces and show that they are compact and connected spaces.

---

## Key Results

1. **Local factorization theorem**: Any holomorphic n x n matrix function phi(z) with an isolated zero of det phi of order k at z = 0 has a unique factorization phi(z) = A(z) z^{k_0} T_{V_l}(z) ... T_{V_1}(z), where A(z) is invertible, k_0 >= 0, and V_1,...,V_l are non-zero proper subspaces of C^n satisfying V_{j+1} cap V_j^perp = {0}.

2. **Vortex internal structure**: A vortex internal structure I_n is defined as a set (k_0, V_1, ..., V_l) of an integer and a sequence of subspaces of C^n satisfying the non-intersection condition. Its order is nk_0 + sum dim V_l.

3. **Main theorem (Theorem 1.3)**: For large volume Vol(Sigma) > 2 pi d/(e^2 tau), vortex solutions are in bijection with finite sets of pairs {(z_j, I^j_n)} of distinct points on Sigma and associated internal structures with sum of orders = degree d. All solutions with det phi not identically zero are obtained this way.

4. **Compact connected internal spaces**: The space I_{n,k} of all internal structures of fixed order k is compact and connected in a natural topology. There is a surjective map phi: (CP^{n-1})^k -> I_{n,k}.

5. **Hitchin-Kobayashi correspondence**: The proof uses the tau-stability results of Bertram-Daskalopoulos-Wentworth and Bradlow et al., which guarantee that stable holomorphic n-pairs correspond to vortex solutions via complex gauge transformations.

6. **k=1 case**: I_{n,1} = CP^{n-1} (the classical result for a single non-abelian vortex).

7. **k=2 case**: I_{n,2} is isomorphic to CP^{n-1} x CP^{n-1} with the "orthogonal diagonal" S collapsed into Gr(2,n), consistent with results of Eto et al.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Yang-Mills-Higgs energy | $E(A,\phi) = \int_\Sigma \frac{1}{2e^2}|F_A|^2 + |d_A\phi|^2 + \frac{e^2}{2}|\phi\phi^\dagger - \tau\mathbf{1}|^2$ | Eq. (1) |
| Vortex equations | $\bar{\partial}_A\phi = 0, \quad *F_A - ie^2(\phi\phi^\dagger - \tau\mathbf{1}) = 0$ | Eq. (2) |
| Local factorization | $\phi(z) = A(z)(z-z_j)^{k_0} T_{V_l}(z-z_j)\cdots T_{V_1}(z-z_j)$ | Eq. (3) |
| Elementary transformation | $T_V(z) := z\Pi_V + \Pi_V^\perp : \mathbb{C}^n \to \mathbb{C}^n$ | Def. 1.2 |
| Algebraic identity | $T_{V_2}(z)T_{V_1}(z) = T_{V_2 \cap W^\perp}(z)T_{W \oplus V_1}(z), \quad W = V_2 \cap V_1^\perp$ | Eq. (7) |
| BPS energy | $E(A,\phi) = 2\pi\tau d$ (at vortex solutions) | Sec. 1.1 |

## Relevance to Phonon-Exflation

This paper establishes the complete characterization of non-abelian U(n) vortex moduli spaces on compact Riemann surfaces via the local factorization theorem and internal structures. The internal degrees of freedom of non-abelian vortices (captured by sequences of subspaces of C^n satisfying intersection conditions) provide a concrete model for understanding how gauge-theoretic solitons on compact spaces carry internal quantum numbers. The factorization technique and Hitchin-Kobayashi correspondence are part of Baptista's toolkit for analyzing gauge fields on compact manifolds, which feeds into his KK program.
