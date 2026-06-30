# Noncommutative Geometry and Conformal Geometry. I. Local Index Formula and Conformal Invariants

**Author(s):** Raphael Ponge and Hang Wang
**Year:** 2014 (revised 2017)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 1411.3701
**Relevance:** MEDIUM

---

## Abstract

This paper is part of a series of articles on noncommutative geometry and conformal geometry. In this paper, we reformulate the local index formula in conformal geometry in such a way to take into account of the action of conformal diffeomorphisms. We also construct and compute a whole new family of geometric conformal invariants associated with conformal diffeomorphisms. This includes conformal invariants associated with equivariant characteristic classes. The approach of this paper involves using various tools from noncommutative geometry, such as twisted spectral triples and cyclic theory. An important step is to establish the conformal invariance of the Connes-Chern character of the conformal Dirac spectral triple of Connes-Moscovici. Ultimately, however, the main results of the paper are stated in a purely differential-geometric fashion.

---

## Key Arguments and Derivations

**Twisted spectral triples and conformal geometry.** The paper uses the framework of twisted spectral triples $(A, H, D)_\sigma$ introduced by Connes-Moscovici, where the usual commutator condition $[D, a]$ bounded is replaced by a twisted commutator $[D, a]_\sigma := Da - \sigma(a)D$ being bounded, with $\sigma$ an automorphism of $A$. The key example arises from conformal deformations: given a spectral triple $(A, H, D)$ and a positive element $k \in A$, the triple $(A, H, kDk)_\sigma$ with $\sigma(a) = k^2 a k^{-2}$ is a twisted spectral triple.

**Index theory for twisted spectral triples.** The authors develop an index theory using $\sigma$-connections on finitely generated projective modules over $A$. The twisted Dirac operator $D_{\nabla^E}$ is Fredholm, and its index depends only on the K-theory class of $E$.

**Connes-Chern character in conformal geometry.** A central result establishes that for smooth twisted spectral triples, the Connes-Chern character descends to a class $\text{Ch}(D)_\sigma \in HP^0(A)$ in the periodic cyclic cohomology of continuous cochains, and this class is invariant under conformal perturbations of the twisted spectral triple.

**Conformal Dirac spectral triple.** For a compact spin manifold $M$ with conformal structure $\mathcal{C}$ preserved by a group $G$ of diffeomorphisms, the conformal Dirac spectral triple $(C^\infty(M) \rtimes G, L^2_g(M, \slashed{S}), \slashed{D}_g)_{\sigma_g}$ has a Connes-Chern character that is an invariant of the conformal class $\mathcal{C}$.

**Computation via equivariant index theory.** Using the Ferrand-Obata theorem (for non-flat $\mathcal{C}$), the authors reduce to a $G$-invariant metric and express the Connes-Chern character in terms of curvatures and normal curvatures of fixed-point manifolds. This yields formulas reminiscent of the Atiyah-Segal-Singer equivariant index theorem.

**Construction of conformal invariants.** By pairing the Connes-Chern character with periodic cyclic cycles constructed via quasi-isomorphisms from equivariant cohomology, the authors obtain a family of geometric conformal invariants associated with conformal diffeomorphisms and mixed equivariant cycles.

## Key Results

1. **Theorem 7.7**: The Connes-Chern character $\text{Ch}(\slashed{D}_g)_{\sigma_g} \in HP^0(C^\infty(M) \rtimes G)$ is an invariant of the conformal class $\mathcal{C}$ (independent of the choice of metric $g \in \mathcal{C}$).
2. **Theorem 8.4**: Local index formula in conformal-diffeomorphism invariant geometry, expressing the Connes-Chern character in terms of explicit polynomials in curvatures and normal curvatures.
3. **Theorem 11.1**: Construction and explicit computation of a new family of geometric conformal invariants attached to conformal diffeomorphisms and mixed equivariant cycles.
4. **Theorem 11.4**: Conformal invariants associated with equivariant characteristic classes.
5. **Proposition 5.9**: For smooth twisted spectral triples, the Connes-Chern character descends to the cyclic cohomology of continuous cochains.
6. **Proposition 6.8**: Invariance of the Connes-Chern character under conformal perturbations of twisted spectral triples.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Index formula | $\text{ind}\, D_{\nabla^E} = \langle \text{Ch}(D), \text{Ch}(E) \rangle$ | Eq. (1.1) |
| Twisted commutator | $[D, a]_\sigma := Da - \sigma(a)D$ | Eq. (2.1) |
| Conformal twist | $\sigma(a) := k^2 a k^{-2}$ | Eq. (2.2) |
| $\sigma$-derivation | $d_\sigma(ab) = (d_\sigma a)b + \sigma(a) d_\sigma b$ | Eq. (2.5) |
| $\sigma$-connection | $\nabla^E(\xi a) = (\nabla^E \xi)a + \sigma_E(\xi) \otimes d_\sigma a$ | Eq. (2.6) |
| Twisted Dirac operator | $D_{\nabla^E}(\xi \otimes \zeta) := \sigma_E(\xi) \otimes D\zeta + c(\nabla^E)(\xi \otimes \zeta)$ | Eq. (2.12) |

## Relevance to Phonon-Exflation

The framework of twisted spectral triples is directly relevant to the M4 x SU(3) product geometry where the internal fiber undergoes conformal-type deformations parameterized by $\tau$. The conformal invariance of the Connes-Chern character (Theorem 7.7) provides a mathematical mechanism by which topological data (index, characteristic classes) are preserved under the geometric deformation that drives exflation. The $\sigma$-connection formalism could inform how gauge connections on the internal space transform as the fiber geometry evolves.
