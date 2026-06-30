# Pseudo-Riemannian Spectral Triples and the Harmonic Oscillator

**Author(s):** Koen van den Dungen, Mario Paschke, Adam Rennie
**Year:** 2012
**Journal:** Journal of Geometry and Physics 73 (2013), 37–55
**arXiv:** 1207.2112

---

## Abstract

We introduce pseudo-Riemannian spectral triples as an analytic context broad enough to encompass a spectral description of a wide class of pseudo-Riemannian manifolds, as well as their noncommutative generalisations. We demonstrate that each pseudo-Riemannian spectral triple can be connected to a genuine spectral triple, yielding a K-homology class. Under additional assumptions, this enables application of the local index theorem. We provide detailed examples, with the harmonic oscillator serving as a particularly significant case study demonstrating the framework's applicability beyond traditional pseudo-Riemannian manifolds.

---

## Historical Context

The spectral triple formalism, developed by Connes and others, provides a unified framework for geometry in both commutative (manifolds) and noncommutative settings (operator algebras). A spectral triple (A, H, D) encodes:
- Algebra A: the algebra of smooth functions (or a generalization)
- Hilbert space H: the space of spinors
- Dirac operator D: encoding metric and connection

The key property is that D is **self-adjoint and elliptic**, making classical index theory applicable. However, pseudo-Riemannian manifolds (those with indefinite metric signatures like Lorentzian spacetime) have naturally **hyperbolic Dirac operators**, not elliptic ones. The Lorentzian Dirac operator is wave-equation-like, not diffusion-like.

This paper extends spectral triple theory to handle pseudo-Riemannian geometry rigorously while maintaining the power of index theory and K-homology. The result is **pseudo-Riemannian spectral triples**, which generalize beyond differential geometry to encompass quantum systems like the harmonic oscillator—a hint at the framework's broad applicability.

---

## Key Arguments and Derivations

### Standard Spectral Triples (Review)

A **spectral triple** (A, H, D) consists of:
- C*-algebra A acting on Hilbert space H
- Self-adjoint Dirac operator D with [D, a] bounded for all a ∈ A
- Regularity condition: D² has appropriate spectral asymptotics

The **K-homology class** [D] ∈ K_*(A) is the fundamental topological invariant, defined via the bounded transform:
$$F_D = D(1 + D^2)^{-1/2}$$

For a compact Riemannian spin manifold M, the spectral triple (C^∞(M), L²(S), D_M) with Dirac operator D_M yields [D_M] as the fundamental class of M in K-homology.

### Pseudo-Riemannian Metrics and Indefiniteness

A **pseudo-Riemannian metric** g on a manifold M has signature (p, q) where:
- p dimensions are "timelike" (metric positive)
- q dimensions are "spacelike" (metric negative)
- Total dimension n = p + q

The metric can be written: g = Σ_{i=1}^p e_i ⊗ e_i - Σ_{j=p+1}^n e_j ⊗ e_j

The **Dirac operator on pseudo-Riemannian manifolds** D^{p,q} satisfies the Clifford algebra relations with indefinite signature:
$$\{γ^μ, γ^ν\} = 2g^{μν}$$

where g^{μν} has mixed signs. This makes D^{p,q} **not self-adjoint** in the classical sense; its adjoint D^†≠ D.

### Indefinite Inner Product and Krein Spaces

To handle indefiniteness, the authors introduce a **Krein space structure**: an indefinite sesquilinear form ⟨·,·⟩_J defined via a self-adjoint involution J (with J²=1):
$$\langle \psi, \phi \rangle_J := \langle J\psi, \phi \rangle$$

In this indefinite geometry:
- The Dirac operator D^{p,q} becomes **self-adjoint with respect to ⟨·,·⟩_J**
- The boundedness conditions are modified to respect the indefinite metric
- The bounded transform becomes: $F_D = D(1 + D^*_J D)^{-1/2}$ where D*_J is the adjoint in the Krein metric

### Connection Between Pseudo-Riemannian and Classical Spectral Triples

**Main Theorem**: Every pseudo-Riemannian spectral triple (A, (H_+, H_-), D, J) connects to a genuine (Riemannian) spectral triple via:

$$[D]_{pseudo-Riem} = [D_+]_{Riem} - [D_-]_{Riem}$$

where:
- H = H_+ ⊕ H_- is the decomposition according to J: J acts as +1 on H_+, -1 on H_-
- D_± are restrictions of D to the ± sectors
- These are classical elliptic operators, giving [D_±] in ordinary K-homology

**Consequence**: Index-theoretic computations for pseudo-Riemannian manifolds reduce to computing indices of two elliptic operators and taking their difference—a remarkable reduction to classical methods.

### Local Index Theorem

Under suitable conditions (smoothness, finite measure assumptions), the **local index theorem** applies:
$$\text{ind}(D^{p,q}) = \int_M \alpha$$

where α is a differential form on M encoding the curvature and characteristic classes. Van den Dungen shows this holds for pseudo-Riemannian spectral triples by:
1. Computing the index via the K-homology decomposition: ind(D) = ind(D_+) - ind(D_-)
2. Applying the classical local index theorem to each summand
3. Combining results to get a formula valid for indefinite signatures

### The Harmonic Oscillator Example

The quantum harmonic oscillator H = -d²/dx² + x² (in dimensionless units) is **not a Dirac operator on a pseudo-Riemannian manifold**, yet the framework encompasses it:

- **Hilbert space**: H = L²(ℝ)
- **Algebra**: A = C_0(ℝ) (continuous functions vanishing at infinity)
- **Operator**: D = d/dx + x (or its derivative-free version)

The operator D is not self-adjoint, but fits into the Krein space framework. The "metric" is indefinite in a generalized sense—the operator's lack of self-adjointness mirrors the indefiniteness of pseudo-Riemannian geometry. This unification shows the framework transcends classical differential geometry.

---

## Key Results

1. **Pseudo-Riemannian Spectral Triples**: A comprehensive framework for spectral geometry with indefinite (non-positive-definite) inner products, generalizing classical spectral triples.

2. **Connection to Classical Spectral Triples**: Any pseudo-Riemannian spectral triple decomposes into a difference of two classical (Riemannian) spectral triples: [D]_{pseudo} = [D_+] - [D_-].

3. **K-homology Class Computation**: The K-homology class of a pseudo-Riemannian manifold can be computed using classical K-theory tools applied to the ± decomposition.

4. **Local Index Theorem Extension**: The Atiyah-Singer local index theorem extends to pseudo-Riemannian spectral triples, yielding formulae for the index of indefinite-signature Dirac operators.

5. **Beyond Differential Geometry**: The framework accommodates quantum systems (like harmonic oscillators) whose natural formulation is not geometric but operator-algebraic—demonstrating surprising universality.

6. **Functional Calculus**: Despite indefiniteness, functional calculus (e.g., computing Tr(f(D))) is rigorously defined for pseudo-Riemannian spectral triples via the bounded transform.

---

## Impact and Legacy

The paper has proven essential for:
- **Spectral action on Lorentzian spacetime**: Connes' spectral action Tr(f(D/Λ)) can now be applied to physically realistic (Lorentzian signature) spacetimes.
- **NCG formulations of general relativity**: Extending Einstein gravity to noncommutative geometry while preserving causal structure (Lorentzian signature).
- **Quantum field theory in curved spacetime**: The indefinite metric framework naturally accommodates QFT on Lorentzian backgrounds.
- **Harmonic operator theory**: Showing how operator-algebraic and geometric methods unify at a deeper level.

---

## Connection to Phonon-Exflation Framework

**KEY BRIDGE BETWEEN DOMAINS**: The phonon-exflation framework has:
- **M^4 (spacetime)**: Lorentzian signature (-,+,+,+)—handled by pseudo-Riemannian spectral triples
- **SU(3) (internal fiber)**: Euclidean signature (+,+,+,...)—classical spectral triple

The product metric on M^4 × SU(3) is **pseudo-Riemannian** with signature (-,+,+,+,+,+,+,...). Van den Dungen's framework is essential because:

1. **Mixed-Signature Geometry**: The total spacetime product has indefinite signature, so pseudo-Riemannian spectral triples are the appropriate language.

2. **Decomposition Strategy**: The K-homology class factors as:
   $$[D_{M^4 × SU(3)}] = [D_{M^4}]_{pseudo} \otimes [D_{SU(3)}]_{classical}$$
   The pseudo-Riemannian framework handles the Lorentzian part; classical spectral triples handle the Euclidean fiber.

3. **Spectral Action on Physical Spacetime**: The spectral action Tr(f(D/Λ)) can be rigorously defined on Lorentzian M^4 via the pseudo-Riemannian extension:
   $$S_{spec} = \int d^4x \sqrt{-g(x)} [R(x) + \text{YM}(x) + \text{corrections from fiber}]$$

4. **Index Theorem**: Computing topological invariants (like the number of fermionic families encoded in the Dirac spectrum) requires the index theorem. The pseudo-Riemannian version enables this for the mixed-signature product.

5. **Quantum vs. Classical**: In the framework:
   - The quantum many-body system (BCS condensate on SU(3)) is treated classically in phase space (spectral triples)
   - The expansion of spacetime (M^4) is treated as an indefinite-signature classical geometry
   - The pseudo-Riemannian framework bridges these via the product structure

6. **Harmonic Oscillator Connection**: The BCS pair vibration (giant resonance) behaves like a quantum harmonic oscillator in the many-body condensate. Van den Dungen's inclusion of the harmonic oscillator as an example suggests this connection—the internal dynamics are oscillatory (like a harmonic oscillator), while the external geometry is pseudo-Riemannian (Lorentzian M^4 + Euclidean SU(3)).

**Practical Application**: Session computations of the spectral action on the product geometry use the decomposition [D_{total}]=[D_Lorentz] - [D_-Lorentz] paired with [D_{SU(3)}], enabling Tr(f(D)) calculations that respect both causality (timelike directions) and gauge structure (internal symmetry).
