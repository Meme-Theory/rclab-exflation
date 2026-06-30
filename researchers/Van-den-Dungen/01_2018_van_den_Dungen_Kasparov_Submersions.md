# The Kasparov Product on Submersions of Open Manifolds

**Author(s):** Koen van den Dungen
**Year:** 2018
**Journal:** Journal of Topology and Analysis 14 (2022), 147-181
**arXiv:** 1811.07824

---

## Abstract

We study the Kasparov product on (possibly non-compact and incomplete) Riemannian manifolds. Specifically, we show on a submersion of Riemannian manifolds that the tensor sum of a regular vertically elliptic operator on the total space and an elliptic operator on the base space represents the Kasparov product of the corresponding classes in KK-theory. This construction works in general for symmetric operators (without assuming self-adjointness), and extends known results for submersions with compact fibres. The assumption of regularity for the vertically elliptic operator depends on the topology and geometry of the submersion, with explicit examples of non-regular operators provided. We apply our main result to obtain a factorisation in unbounded KK-theory of the fundamental class of a Riemannian submersion, as a Kasparov product of the shriek map of the submersion and the fundamental class of the base manifold.

---

## Historical Context

The theory of K-homology and KK-theory, developed primarily by Kasparov and extended by Baum-Douglas-Taylor, provides deep connections between elliptic differential operators and topological invariants. The Kasparov product captures the composition of K-homology classes—a fundamental operation in noncommutative geometry. Prior work established the Kasparov product for compact manifolds or submersions with compact fibres, but the treatment of non-compact, incomplete manifolds remained technically challenging.

Van den Dungen's work extends this framework systematically. A key innovation is showing that self-adjointness of the operator is not necessary: any closed symmetric extension of an elliptic differential operator yields the same K-homology class (via the bounded transform). This generality is crucial for applications in noncommutative geometry and spectral action theory, where operators arise naturally but need not satisfy strong regularity conditions a priori.

The application to Riemannian submersions is significant because submersions model fiber bundle structures—central to modern geometry and physics. Factorizing the fundamental class of a submersion as a Kasparov product reveals the underlying multiplicative structure and enables decomposition of index-theoretic invariants along fibre directions.

---

## Key Arguments and Derivations

### Unbounded Kasparov Modules and the Bounded Transform

An unbounded Kasparov module (A,H,D) over a C*-algebra A consists of:
- A Hilbert A-module H
- A symmetric, densely-defined, regular operator D on H (the "unbounded partner")

The **bounded transform** produces the K-homology class:
$$F_D = D(1 + D^* D)^{-1/2} : H \to H$$

This is a bounded operator in the multiplier algebra M(A), and represents the element [F_D] in KK(C_0(M), C) for a manifold M. Critically, different closed extensions of the same differential operator yield the *same* K-homology class under the bounded transform.

### The Vertical Ellipticity Condition

For a submersion π : E → B, an operator D on E is **vertically elliptic** if its principal symbol σ(D) is invertible in all directions orthogonal to the fibres (the vertical directions). This condition ensures:
- The operator is semi-Fredholm when restricted to fibres
- Spectral gap properties that enable functional calculus
- Regularity (in the sense of Kasparov modules) under mild topological conditions

### Tensor Sum on Submersions

The main theorem shows that if:
- D_E is a regular vertically elliptic operator on the total space E
- D_B is an elliptic operator on the base space B

Then the **tensor sum** D_E ⊗ 1 + 1 ⊗ D_B (appropriately interpreted on the Hilbert module of sections over the submersion) represents the Kasparov product:
$$[D_E \otimes 1 + 1 \otimes D_B] = [D_E] \otimes_{C_0(E)} [D_B]$$

in KK-theory. This is a non-trivial result because:
1. The tensor sum must be shown to be regular (closure of symmetric operator is self-adjoint)
2. The resulting operator must preserve the module structure
3. The bounded transforms must compose correctly to yield the Kasparov product formula

### Regularity and Examples

The condition that D_E be "regular" is not automatic—it depends on whether the closure of D_E (viewed as an operator on the Hilbert module C_0(E) ⊗ H_fib) is self-adjoint. Van den Dungen provides:

- Examples of non-compact submersions where vertically elliptic operators ARE regular
- Explicit counterexamples where regularity fails (typically when the base or fibres have geometric singularities or unbounded geometry)
- Sufficient conditions for regularity in terms of the submersion's geometry (e.g., geometric properties of the fibre bundle)

### Factorization of the Fundamental Class

For a Riemannian submersion π : M → B, the **fundamental class** is the K-homology class [D_M] of the Dirac operator on M. The theorem gives:
$$[D_M] = \pi_! \otimes [D_B]$$

where π_! is the **shriek map** (Gysin map in K-homology), which "pushes forward" the K-homology class from M to B along the submersion. This factorization is:
- Functorial: respects the composition of submersions
- Multiplicative: shows explicit structure via the Kasparov product
- Algorithmic: enables computation of index invariants by decomposing along the fibre direction

---

## Key Results

1. **Main Theorem (Kasparov Product on Submersions)**: On a Riemannian submersion E → B, if D_E is a regular vertically elliptic operator and D_B is an elliptic operator on B, then the tensor sum D_E ⊗ 1 + 1 ⊗ D_B represents the Kasparov product [D_E] ⊗ [D_B] in KK-theory.

2. **Regularity Criterion**: Regularity of vertically elliptic operators can fail, and van den Dungen provides explicit geometric characterizations of when it holds—crucial for non-compact or singular submersions.

3. **Fundamental Class Factorization**: The K-homology class of a Riemannian manifold M admitting a submersion to B factors as [D_M] = π_! ⊗ [D_B], making the fibral structure explicit.

4. **Extension to Non-Compact Geometry**: The construction works without compactness assumptions, using the framework of C*-modules and unbounded KK-theory—essential for applications in noncommutative cosmology.

5. **Symmetry Suffices**: Self-adjointness is not required; symmetric operators suffice, broadening applicability to differential operators arising in geometry.

---

## Impact and Legacy

This paper has become foundational in spectral geometry and noncommutative geometry. Its results are applied in:
- **Spectral action computations**: When the base space is M^4 (spacetime) and the fibres are a compact Riemannian manifold (like SU(3)), the Kasparov product enables efficient computation of the spectral action from lower-dimensional pieces.
- **K-theory calculations**: Factorizing the fundamental class simplifies index calculations on manifolds with natural fibration structures.
- **Finite spectral triples**: In almost-commutative geometry, the factorization formula helps relate the spectral triple on the total space to its submersion-induced structure.

The treatment of non-compact, non-complete manifolds extends the applicability far beyond classical Riemannian geometry, making it relevant to physical applications where spacetimes or configuration spaces are typically non-compact.

---

## Connection to Phonon-Exflation Framework

**CRITICAL BRIDGE:** This paper is the essential mathematical tool for the phonon-exflation framework. The framework treats spacetime as M^4 × SU(3) where:
- M^4 is the classical Riemannian base (expanding spacetime)
- SU(3) is the internal gauge fibre (the quark-color structure)

The spectral action Tr(f(D/Λ)) must be computed on this fiber bundle. Van den Dungen's submersion theorem allows factorization:

$$[D_{M^4 \times SU(3)}] = [D_{M^4}] \otimes_{C_0(M^4)} [D_{SU(3)}]$$

This means:
1. The spectral action can be split: $S_{spec} = S_{M^4} + S_{SU(3)} + \text{mixed terms}$
2. The Dirac operator on the fiber SU(3) (which encodes the internal structure, pairing, and BCS condensate) composes with the base M^4 Dirac operator via the Kasparov product.
3. The shriek map π_! encodes how geometric deformation (like compactification dynamics or Jensen deformation) affects the spectral action on the base.

**Practical Application**: In Session 35+ computations, the eigenvalue spectrum of D_K (the Dirac operator on the deformed SU(3) fiber) is paired with the FLRW metric on M^4 to compute corrections to the spectral action. This pairing is precisely the Kasparov product structure that van den Dungen formalizes.

**Gateway to Baptista-Connes Bridge**: Van den Dungen's submersion framework is the mathematical language in which Baptista's higher-dimensional Kaluza-Klein geometry (Riemannian submersion G/H → M^4) interfaces with Connes' spectral triple formalism (noncommutative K-homology). Without this tool, the bridge between Riemannian geometry and NCG would lack rigorous grounding.
