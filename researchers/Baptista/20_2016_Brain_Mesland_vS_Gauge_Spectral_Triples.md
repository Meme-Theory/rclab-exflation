# Gauge Theory for Spectral Triples and the Unbounded Kasparov Product

**Author(s):** Simon Brain, Bram Mesland and Walter D. van Suijlekom
**Year:** 2013 (revised 2015)
**Journal:** Journal of Geometry and Physics 100 (2016) 186-227
**arXiv:** 1306.1951
**Relevance:** HIGH

---

## Abstract

We explore factorizations of noncommutative Riemannian spin geometries over commutative base manifolds in unbounded KK-theory. After setting up the general formalism of unbounded KK-theory and improving upon the construction of internal products, we arrive at a natural bundle-theoretic formulation of gauge theories arising from spectral triples. We find that the unitary group of a given noncommutative spectral triple arises as the group of endomorphisms of a certain Hilbert bundle; the inner fluctuations split in terms of connections on, and endomorphisms of, this Hilbert bundle. Moreover, we introduce an extended gauge group of unitary endomorphisms and a corresponding notion of gauge fields. We work out several examples in full detail, to wit Yang-Mills theory, the noncommutative torus and the theta-deformed Hopf fibration over the two-sphere.

---

## Key Arguments and Derivations

### Section 1: Introduction

The paper addresses the fundamental question: can the gauge group of a noncommutative spectral triple be realized as endomorphisms of a vector bundle, and can inner fluctuations arise as connections thereon? The answer is yes, when one factorizes a noncommutative spectral triple (A, H, D) over a commutative base manifold (B, H_0, D_0) using unbounded KK-theory.

The factorization means (A, H, D) is unitarily equivalent to the Kasparov product (E, S, nabla) tensor_B (B, H_0, D_0) = (A, E tensor_B H_0, S tensor 1 + 1 tensor nabla D_0). The vertical part is a Hilbert bundle over the commutative base X, upon which U(A) acts as bundle endomorphisms. Inner fluctuations decompose into connections on this Hilbert bundle and endomorphisms thereof.

### Section 2: Operator Modules and Unbounded KK-Theory

**Definition 2.1 (Spectral triple):** (A, H, D) consists of a unital C*-algebra A, a Hilbert space H with faithful representation pi: A -> B(H), and an unbounded self-adjoint operator D with compact resolvent such that A := {a in A : [D, pi(a)] extends to B(H)} is dense in A.

**Definition 2.3 (Unbounded KK-cycle):** A pair (E, D) over graded C*-algebras A, B is an unbounded (A,B) KK-cycle if D has compact resolvents in K_B(E) and the Lipschitz subalgebra is dense.

The paper develops the theory of projective operator modules (Def. 2.12), allowing unbounded projection operators on the free module H_B. This is needed because the Peter-Weyl decomposition of SU(2) produces projections with growing differential norms. Lipschitz modules (Def. 2.24) carry connections nabla: E -> E tensor_B Omega^1_D(B).

**Theorem 2.35 (Unbounded Kasparov product):** For a Lipschitz cycle (E, S, nabla) in Psi^l_0(A, B) and (F, T) in Psi_0(B, C), the sum D = S tensor 1 + 1 tensor nabla T is essentially self-adjoint and regular, and (E tensor_B F, D) in Psi_0(A, C) represents the Kasparov product.

### Section 3: Gauge Theories from KK-Factorization

**Definition 3.3 (Gauge group):** The gauge group of spectral triple (B, H, D) is U(B), the unitary elements of the Lipschitz algebra B, acting via D -> D_u = uDu* = D + u[D, u*].

**Definition 3.7 (Lipschitz gauge group):** For a KK-factorization with Hilbert bundle E over X, the Lipschitz gauge group G(E) consists of unitary endomorphisms of E preserving Lipschitz structure. The internal gauge group U(A) is a normal subgroup of G(E).

**Proposition 3.5:** The Kasparov product of (E, 0, nabla) with (B, H, D) yields a spectral triple (H_E, D_nabla) over A. Inner fluctuations decompose into connections on E and endomorphisms.

**Proposition 3.10:** There is a short exact sequence 1 -> U(A) -> G(E) -> G(E)/U(A) -> 1, generalizing the structure group sequence of gauge theory.

### Section 4: Yang-Mills Theory

For a hermitian vector bundle E -> M, the spectral triple (A, H_E, D_E) with A = End*(E) and D_E = 1 tensor nabla slashed-partial_M factors as a Kasparov product. The gauge group G(E) equals U(A) in this case. Gauge fields are connections on E modulo endomorphisms.

**Theorem 4.7:** Almost-commutative manifolds M x F factor as KK-products, recovering the standard formulation of gauge theories from NCG.

### Section 5: Noncommutative Torus

The noncommutative torus A_theta is factorized as a circle bundle over a base circle. The Lipschitz module is the space of smooth sections of a line bundle, and the gauge group is U(1).

### Section 6: Noncommutative Hopf Fibration

The theta-deformed three-sphere S^3_theta is factored over S^2 using the Peter-Weyl decomposition into line bundles L_n over S^2, with unbounded projections. The Kasparov product reproduces the Dirac operator on S^3_theta. This is a topologically nontrivial example requiring the theory of unbounded projections developed in Section 2.

## Key Results

1. The gauge group of a spectral triple arises as the group of unitary endomorphisms of a Hilbert bundle when the triple is factored over a commutative base
2. Inner fluctuations split into horizontal (connections) and vertical (endomorphisms) components
3. The extended Lipschitz gauge group G(E) contains U(A) as a normal subgroup
4. Almost-commutative manifolds M x F naturally factor as unbounded Kasparov products
5. The noncommutative Hopf fibration S^3_theta -> S^2 is explicitly constructed as a Kasparov product, requiring the theory of unbounded projections
6. The Peter-Weyl decomposition produces an infinite direct sum of line bundles with growing projection norms, necessitating the extension to unbounded projections

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Kasparov product | $(A, E\hat{\otimes}_B H_0,\; S\otimes 1 + 1\otimes\nabla D_0)$ | Eq. after Thm 2.35 |
| Gauge transformation | $D \mapsto D_u = uDu^* = D + u[D, u^*]$ | Eq. (3.1) |
| Differential calculus | $\Omega^1_D(A) = \{\sum a_j[D,\pi(b_j)] \mid a_j, b_j \in A\}$ | Eq. (2.1) |
| Lipschitz representation | $\pi_D: B \to B(H\oplus H),\quad b\mapsto \begin{pmatrix}\pi(b) & 0 \\ [D,\pi(b)] & \pi(b)\end{pmatrix}$ | Eq. (2.3) |
| Morita equivalence | $(H_E, D_\nabla) = (E\otimes_A H,\; 1\otimes_\nabla D)$ | Eq. (3.2) |

## Relevance to Phonon-Exflation

1. **Kasparov product for M4 x SU(3):** The framework's product geometry M4 x SU(3) is precisely the type of factorization studied here. The spectral triple over M4 x SU(3) should factor as a Kasparov product, with the "internal" SU(3) part providing a Lipschitz cycle.

2. **Gauge fields from bundle structure:** The paper's result that inner fluctuations split into connections and endomorphisms is relevant to understanding how the U(1)_7 gauge symmetry and its breaking by Cooper pairs (Session 35) emerge from the bundle structure of the Peter-Weyl decomposition over SU(3).

3. **Peter-Weyl and unbounded projections:** The treatment of the Hopf fibration via Peter-Weyl decomposition with unbounded projections directly parallels the project's use of Peter-Weyl modes on SU(3). The growing norm of projections in higher representations is a structural feature encountered in the project's spectral computations.

4. **Block-diagonal theorem context:** The project's D_K block-diagonality theorem (Session 22b) operates within this Kasparov product framework, where the block structure reflects the decomposition of the internal Hilbert space into Peter-Weyl sectors.
