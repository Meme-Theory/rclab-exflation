# Indefinite Kasparov Modules and Pseudo-Riemannian Manifolds

**Author(s):** Koen van den Dungen, Adam Rennie, Walter D. van Suijlekom
**Year:** 2015
**Journal:** Annales Henri Poincaré 17 (2016), 3255–3286
**arXiv:** 1503.06916

---

## Abstract

We present a definition of indefinite Kasparov modules, a generalisation of unbounded Kasparov modules modelling non-symmetric and non-elliptic (e.g. hyperbolic) operators. We demonstrate that each indefinite Kasparov module can be paired with genuine Kasparov modules reversibly, with applications to Dirac operators on pseudo-Riemannian manifolds, harmonic oscillators, and globally hyperbolic spacetimes. The pairing produces a well-defined element in the KK-groups even when neither classical Kasparov products would be defined.

---

## Historical Context

Classical K-theory, developed by Atiyah and Hirzebruch, assigns to each manifold M a group K(M) of stable equivalence classes of vector bundles. K-homology (or K∗(M)) is the dual theory capturing information about elliptic differential operators via their index properties. Kasparov's KK-theory unifies these, providing a bivariant theory where KK(A,B) are groups of Kasparov modules—abstractly encoding the index of operators between two C*-algebras A and B.

The Kasparov product, denoted ⊗, composes two Kasparov modules to produce a third, provided they satisfy regularity conditions (e.g., ellipticity). This works beautifully for Riemannian geometry, where the Dirac operator is elliptic and self-adjoint.

However, **physical spacetime is Lorentzian** (indefinite metric), not Riemannian. The Dirac operator on Lorentzian spacetime is *not* self-adjoint—it is hyperbolic (wave-equation-like). Classical Kasparov theory cannot directly handle these operators. Van den Dungen et al. extend Kasparov's framework to indefinite settings, enabling rigorous K-theoretic treatment of hyperbolic operators.

This generalization is foundational for:
- **Lorentzian quantum field theory**: The Dirac equation in QFT is hyperbolic, not elliptic
- **Causal geometry**: Causality structure (light cones) is intrinsically hyperbolic
- **Cosmology with foliation**: The ADM formalism decomposes Lorentzian spacetime into Riemannian spatial slices, and indefinite Kasparov modules mediate between these levels

---

## Key Arguments and Derivations

### Classical Kasparov Modules

A **Kasparov module** is a triple (E, φ, F) where:
- E is a Hilbert C*-module (a generalization of Hilbert space, allowing C*-algebra-valued inner products)
- φ : A → L(E) is a representation of C*-algebra A
- F is a self-adjoint operator (the "Fredholm operator" or Dirac operator)

satisfying boundedness and finiteness conditions. The composition of two Kasparov modules via the Kasparov product is well-defined when both modules satisfy **regularity**—roughly, the operator F must have resolvent in an appropriate sense.

### The Indefiniteness Problem

On a **pseudo-Riemannian manifold** with metric signature (-, +, +, +) (Lorentzian) or more generally (p, q) (p timelike, q spacelike directions), the Dirac operator D satisfies:
- D is *not* self-adjoint (its adjoint D† ≠ D)
- The spectrum of D is not real; complex eigenvalues appear
- Resolvent (D - λ)^{-1} does not decay uniformly for large |λ|
- Classical elliptic regularity fails; the operator is hyperbolic

These properties make D impossible to fit into a classical Kasparov module framework. The **indefinite Kasparov module** generalizes to accommodate this.

### Indefinite Kasparov Modules (Definition)

An **indefinite Kasparov module** is a tuple (E, φ, F, J) where:
- E is a Hilbert C*-module
- φ : A → L(E) is a representation
- F is a *symmetric but not self-adjoint* operator (like a classical differential operator before imposing boundary conditions)
- J is a **Krein involution**: a self-adjoint unitary operator J on E with J² = 1, defining an indefinite metric ⟨ψ, φ⟩_J = ⟨ψ, Jφ⟩

The indefinite inner product ⟨·,·⟩_J replaces the standard positive definite inner product, allowing the theory to capture non-self-adjoint and hyperbolic structures.

**Regularity condition**: F is called regular if its closure in the Krein space sense is self-adjoint with respect to the indefinite metric, and resolvent properties hold in the Krein topology (a weaker topology than Hilbert).

### Pairing Theorem

The central theorem proves: **To each indefinite Kasparov module can be associated a pair of genuine (classical) Kasparov modules, and this association is reversible.**

More precisely:
- From (E, φ, F, J), construct two Kasparov modules: (E₊, φ, F₊) and (E₋, φ, F₋)
- These are obtained by decomposing E according to the sign of J: E = E₊ ⊕ E₋ with J acting as +1 on E₊ and -1 on E₋
- Conversely, given two Kasparov modules (E₊, φ, F₊) and (E₋, φ, F₋) with compatible algebras, one can reconstruct an indefinite Kasparov module

**Consequence**: K-theoretic pairings that involve indefinite modules—like the index of a hyperbolic operator—can be computed using classical KK-theory applied to the positive/negative parts separately, then combined.

### Pairing Formula

The pairing between an indefinite Kasparov module and a genuine Kasparov module is defined via:
$$\langle (E, φ, F, J), (E', φ', F') \rangle := \langle (E_+, φ, F_+), (E', φ', F') \rangle - \langle (E_-, φ, F_-), (E', φ', F') \rangle$$

where the right-hand side uses classical Kasparov products on the ± parts. The difference captures the indefinite structure. This formula ensures:
1. Well-definedness: The index is an integer despite F not being self-adjoint
2. Functoriality: Compositions respect indefiniteness
3. Reversibility: No information is lost in the decomposition/recomposition

---

## Key Results

1. **Indefinite Kasparov Module Theory**: A comprehensive framework for hyperbolic and non-self-adjoint operators, extending classical Kasparov theory to indefinite metrics and non-elliptic settings.

2. **Pairing Reversibility Theorem**: Every indefinite Kasparov module canonically corresponds to a pair of classical Kasparov modules, enabling computation of hyperbolic indices via elliptic methods.

3. **Dirac on Pseudo-Riemannian Manifolds**: The Dirac operator on a pseudo-Riemannian spin manifold fits into the indefinite Kasparov framework, and its K-homology class can be computed via the decomposition formula.

4. **Harmonic Oscillator Application**: The quantum harmonic oscillator (with its non-self-adjoint raising/lowering structure) is embedded into indefinite Kasparov theory, unifying oscillator problems with Dirac operator methods.

5. **Globally Hyperbolic Spacetimes**: Foliations of globally hyperbolic spacetimes (spacetimes with Cauchy surfaces) admit indefinite Kasparov module formulations, enabling index-theoretic tools in general relativity.

6. **Index Formula for Hyperbolic Operators**: The pairing of indefinite Kasparov modules produces integer-valued indices—topological invariants of hyperbolic operators—computed as differences of indices of related elliptic operators.

---

## Impact and Legacy

The paper has become essential for:
- **Lorentzian geometry in NCG**: It provides the rigorous mathematical foundation for applying K-theory to spacetime with physical (indefinite) signature, beyond the Riemannian setting of earlier work.
- **Spectral action on Lorentzian spacetime**: The spectral action Tr(f(D/Λ)) can now be rigorously defined for Lorentzian Dirac operators.
- **Causal structure**: The indefinite metric naturally encodes causality (light cones defined by indefiniteness).
- **Quantum field theory**: Path integrals and Wick rotations between Lorentzian and Euclidean regimes are formalized through the indefinite/elliptic decomposition.

---

## Connection to Phonon-Exflation Framework

**DEEP RELEVANCE**: The phonon-exflation framework treats M^4 × SU(3) where:
- M^4 has Lorentzian signature (it is physical spacetime undergoing expansion)
- SU(3) has Euclidean (positive-definite) signature (it is an internal gauge manifold)

The product metric on M^4 × SU(3) is **pseudo-Riemannian**: it is Lorentzian along M^4 directions and Euclidean along SU(3) directions.

**Van den Dungen's indefinite Kasparov framework enables**:

1. **Product Structure**: The Dirac operator on M^4 × SU(3) is the tensor sum D_{M^4} ⊗ 1 + 1 ⊗ D_{SU(3)}, where:
   - D_{M^4} is hyperbolic (indefinite Kasparov module)
   - D_{SU(3)} is elliptic (classical Kasparov module)
   - The product can be studied using the decomposition theorem

2. **Factorization**: The pairing reversibility theorem allows the spectral action to be decomposed as:
   $$S_{spec}(M^4 × SU(3)) = S_{M^4} ⊗ S_{SU(3)}$$
   with indefiniteness handled through the ± decomposition.

3. **K-homology Class**: The fundamental class [D_{M^4 × SU(3)}] fits into indefinite KK-theory, and its pairing with auxiliary operators (like those encoding gauge couplings or BCS condensate states) is well-defined despite the indefinite metric.

4. **Wick Rotation**: When computing the spectral action via Euclidean functional integral methods, one Wick-rotates M^4 (Lorentzian → Euclidean). Van den Dungen's theory formalizes this as a transition between indefinite and elliptic Kasparov modules.

5. **Foliation with Indefiniteness**: When using the family of spectral triples formalism (Paper 2), each time-slice has Riemannian (elliptic) geometry, but the Lorentzian foliation structure is captured by the indefinite module framework. This bridges time-evolution and spatial geometry.

**Connection to Schwarzschild-Penrose**: In the context of extremal black holes (Schwarzschild geometry), the horizon region involves indefinite geometry (type-changing signature), which van den Dungen's theory handles naturally. This is relevant if the phonon-exflation framework is extended to black hole thermodynamics.

**Connection to Volovik**: Volovik's analog gravity from condensed matter often involves Lorentzian effective geometries emerging from Euclidean microscopic systems. Indefinite Kasparov modules provide the formal K-theoretic language for this emergence: the microscopic system is described by elliptic operators (Krein space decomposition E₊), and the Lorentzian emergent geometry corresponds to the indefinite structure.
