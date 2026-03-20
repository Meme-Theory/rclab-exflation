# Gauge Theory for Spectral Triples and the Unbounded Kasparov Product

**Author(s):** Simon Brain, Bram Mesland, Walter D. van Suijlekom
**Year:** 2016
**Journal:** Journal of Noncommutative Geometry, Vol. 10(1), pp. 135-206
**arXiv:** 1306.1951 [math-ph]
**Submitted:** June 13, 2013 (revised January 2015)

---

## Abstract

This paper develops a natural bundle-theoretic formulation of gauge theories arising from spectral triples through unbounded KK-theory (Kasparov-Kunneth theory). The authors demonstrate that the unitary group of a noncommutative spectral triple functions as the structure group of endomorphisms of a Hilbert bundle, and show how inner fluctuations of the Dirac operator decompose into connections and endomorphisms of this bundle structure. The framework is illustrated through concrete examples including Yang-Mills theory, noncommutative tori, and theta-deformed Hopf fibrations. The work bridges spectral geometry and traditional gauge theory, providing mathematical tools for understanding how gauge fields emerge from operator algebra fluctuations in noncommutative geometry.

---

## Historical Context

Since the 1980s, spectral geometry has offered a framework for deriving gauge theories from the structure of spectral triples. However, the connection between abstract spectral geometry and conventional gauge theory (with connections on principal bundles) was not entirely transparent. How do the "inner fluctuations" of a Dirac operator relate to gauge connections? Under what circumstances does a spectral triple encode a Yang-Mills theory?

Brain, Mesland, and van Suijlekom's 2016 paper provides the missing link: a precise mathematical framework showing that spectral triples naturally give rise to principal bundles with gauge connections. The tool is **unbounded Kasparov theory** (KK-theory), an extension of K-theory designed to handle unbounded operators.

This work is important for understanding the foundation of the spectral action framework and for clarifying how KK-theory (the abstract K-theory, not Kaluza-Klein) relates to physical gauge theories. For the Baptista program and phonon-exflation, it provides mathematical rigor for the claim that gauge interactions emerge from spectral properties of the internal geometry.

---

## Key Arguments and Derivations

### Spectral Triples and Dirac Operators

A spectral triple $(A, H, D)$ consists of:
- $A$: A $*$-algebra (e.g., $C^*(X)$ for a compact space $X$, or a noncommutative C*-algebra)
- $H$: A Hilbert space (e.g., $L^2(X, S)$, the space of square-integrable spinor sections)
- $D$: A self-adjoint Dirac-type operator on $H$ with compact resolvent

A key property is that $D$ has a bounded commutator with elements of $A$:

$$[D, a] = Da - aD$$

is bounded for all $a \in A$. This commutator encodes the action of the algebra on the Hilbert space.

### Inner Fluctuations and Gauge Fields

An **inner fluctuation** is a perturbation of the Dirac operator by elements of the algebra:

$$D \to D' = D + A + JAJ^*$$

where $A$ is a self-adjoint element of the algebra (thought of as a "gauge field") and $J$ is a real structure operator (related to charge conjugation in the physical case).

The key insight is that such fluctuations can be written as:

$$D' = U D U^*$$

where $U$ is a unitary element of the algebra. This is an **inner perturbation**. The unitary $U$ is the gauge transformation, and the change in $D$ under this transformation gives the gauge field.

### Hilbert Bundle Structure

The authors show that these fluctuations can be organized using the language of principal bundles. Specifically:
- The base space is the space of states or the parameter space of the gauge transformations
- The structure group is the unitary group $\mathcal{U}(A)$ of the algebra
- The total space is a Hilbert bundle with Hilbert fiber $H$ over each base point

A section of this bundle is a family of spinors $\psi_\alpha$ (indexed by a gauge transformation parameter $\alpha$), with the property that:

$$\psi'_\alpha = U_\alpha \psi_\alpha$$

under gauge transformations.

### Connections and Covariant Derivatives

A **connection** on the Hilbert bundle is a covariant derivative operator:

$$\nabla: \Gamma(H) \to \Gamma(T^* \otimes H)$$

that respects the gauge structure:

$$\nabla(U_\alpha \psi) = U_\alpha (\nabla \psi) + d(U_\alpha) \otimes \psi$$

(up to appropriate pullback operators).

The authors demonstrate that the structure of inner fluctuations of the Dirac operator naturally induces such a connection:

$$\nabla_a = [D, a]$$

where $a \in A$ is an element of the algebra and $[D, a]$ is the commutator (which is bounded by assumption).

The curvature of this connection is:

$$R(a, b) = \nabla_a \nabla_b - \nabla_b \nabla_a = [[D, a], b]$$

This is the noncommutative geometry curvature.

### Kasparov Theory and Spectral Triples

Kasparov theory extends K-theory to handle unbounded operators. The **Kasparov product** is an operation combining two spectral triples (or more generally, unbounded Kasparov modules) to produce a new one.

For two spectral triples $(A, H_1, D_1)$ and $(B, H_2, D_2)$, the Kasparov product is:

$$(A, H_1, D_1) \otimes_C (B, H_2, D_2) = (A \otimes B, H_1 \otimes H_2, D_1 \otimes 1 + 1 \otimes D_2)$$

(plus additional technical requirements about the commutation relations).

This product is associative (up to homotopy) and has a unit element (the trivial spectral triple). In this sense, spectral triples form a category-like structure.

### Application: Yang-Mills Theory on Noncommutative Torus

As a concrete example, the authors apply the framework to the **noncommutative torus** $T^2_\theta$, which is the C*-algebra generated by two unitaries $U, V$ satisfying:

$$UV = e^{2\pi i \theta} VU$$

where $\theta$ is an irrational number (the noncommutativity parameter).

A spectral triple on $T^2_\theta$ is constructed using:
- $A = C^*(U, V)$ (the noncommutative torus algebra)
- $H = \ell^2(\mathbb{Z}^2)$ (square-summable sequences indexed by $\mathbb{Z}^2$)
- $D = \sum_j m_j e_j$ (Dirac operator with appropriate mass terms)

Inner fluctuations of this Dirac operator correspond to gauge connections on the noncommutative torus. The authors compute explicitly that the noncommutative Yang-Mills theory emerges from the spectral action applied to this triple.

### Theta-Deformed Hopf Fibration Example

Another example is a theta-deformation of the Hopf fibration $S^3 \to S^2$. The C*-algebra is constructed from quantum group generators, and the Dirac operator is defined using quantum group differential calculus.

The inner fluctuations of this Dirac operator are shown to encode the gauge structure of a quantum principal bundle, with structure group the quantum SU(2) (q-deformed version).

This example illustrates the power of the framework: it naturally handles both commutative and noncommutative spaces, classical and quantum group symmetries, all within a unified spectral triple language.

---

## Key Results

1. **Gauge Theories from Spectral Triples**: Inner fluctuations of a Dirac operator on a spectral triple naturally decompose into a connection (gauge field) and endomorphisms of the Hilbert bundle.

2. **Principal Bundle Structure**: The space of inner fluctuations forms a principal bundle with structure group being the unitary group of the algebra.

3. **Covariant Derivative from Commutators**: The gauge covariant derivative is naturally given by the commutator with the Dirac operator: $\nabla_a = [D, a]$.

4. **Curvature and Gauge Theory**: The gauge field strength tensor is encoded in the double commutator: $R(a,b) = [[D,a],b]$, recovering the standard Yang-Mills structure.

5. **Kasparov Product as Composition**: The Kasparov product provides a natural composition rule for spectral triples, making them into a higher categorical structure.

6. **Universality**: The framework applies equally to commutative spaces (where it reproduces classical Riemannian geometry and Yang-Mills), noncommutative algebras, and quantum groups.

---

## Impact and Legacy

This work has been foundational for the mathematical development of noncommutative geometry:

- **Rigorous Foundations**: It placed the spectral action approach on solid mathematical ground by clarifying the relationship to traditional gauge theory.
- **Computational Tools**: The Kasparov product and unbounded KK-theory provide practical tools for computing gauge structures from algebraic data.
- **Generality**: By showing that the framework handles quantum groups and noncommutative spaces, it expanded the scope of geometric unification.

The paper has influenced subsequent work on:
- Quantum groups and gauge theory
- Deformation quantization
- Loop quantum gravity and its algebraic structures
- K-theory and index theory applications to physics

---

## Connection to Phonon-Exflation Framework

For phonon-exflation, this paper is important for several reasons:

1. **Mathematical Rigor**: It provides rigorous mathematical foundations for how the internal SU(3) geometry (encoded as a spectral triple or deformed spectral structure) generates gauge interactions.

2. **Gauge Emergence from Geometry**: The theorem that gauge fields emerge from inner fluctuations of the Dirac operator directly supports the phonon-exflation picture: phonons (metric vibrations) induce changes in the Dirac spectrum, which in turn modify gauge couplings.

3. **Noncommutative Deformations**: As the internal metric deforms during phonon-exflation, the internal space can develop noncommutativity (slight deviations from classical geometry). The framework naturally handles this.

4. **Hilbert Bundle Picture**: The identification of the Hilbert bundle as the natural geometric object suggests that fermionic zero modes should be understood as sections of a bundle over the space of internal metric deformations.

5. **Covariant Derivatives and Connections**: The formula $\nabla_a = [D,a]$ suggests that in phonon-exflation, the gauge covariant derivative should be computed from commutators of the Dirac operator with metric deformation parameters.

6. **Unified Framework**: By showing that spectral geometry encompasses both classical and quantum geometric structures, the paper supports the phonon-exflation view that all particle physics emerges from a single geometric principle (the internal metric and its vibrations).

---

## References

- Brain, S., Mesland, B., & van Suijlekom, W. D. (2016). "Gauge Theory for Spectral Triples and the Unbounded Kasparov Product." *Journal of Noncommutative Geometry*, 10(1), 135-206. arXiv:1306.1951 [math-ph].
- Kasparov, G. G. (1987). "Equivariant KK-Theory and the Novikov Conjecture." *Inventiones Mathematicae*, 91(1), 147-201.
- Connes, A., & Cuntz, J. (1997). "Quasihomomorphisms and Stable Homology." *Inventiones Mathematicae*, 139(3), 541-572.
- Chamseddine, A. H., & Connes, A. (1997). "The Spectral Action Principle." *Communications in Mathematical Physics*, 186(3), 731-750.
