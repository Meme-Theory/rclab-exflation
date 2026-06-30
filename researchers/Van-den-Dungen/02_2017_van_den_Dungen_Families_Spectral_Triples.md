# Families of Spectral Triples and Foliations of Space(time)

**Author(s):** Koen van den Dungen
**Year:** 2018
**Journal:** Journal of Mathematical Physics 59 (2018), 063507
**arXiv:** 1711.07299

---

## Abstract

We examine a noncommutative analogue of a spacetime foliated by spacelike hypersurfaces, in both Riemannian and Lorentzian signatures. We demonstrate how to reconstruct canonical Dirac operators on total spacetime from families of operators on constituent hypersurfaces. In the Riemannian case, the family construction yields a product spectral triple. In Lorentzian signature, the construction produces a Lorentzian spectral triple, which can also be viewed as the "reverse Wick rotation" of a product spectral triple. The Lorentzian construction fits well into the Krein space approach to noncommutative Lorentzian geometry.

---

## Historical Context

The classical foliation of spacetime by spacelike hypersurfaces is fundamental to relativistic physics: the "3+1" ADM decomposition, familiar in general relativity and cosmology, decomposes spacetime into a family of spatial slices parameterized by time. Each slice is a Riemannian manifold, and their evolution is governed by the Hamiltonian constraint equations.

In the commutative setting, the Dirac operator on spacetime can be reconstructed from the Dirac operators on each spatial slice plus evolution data. Van den Dungen extends this classical construction to noncommutative geometry, where spectral triples replace manifolds and Dirac operators are the fundamental objects. This is crucial for:

1. **Lorentzian spectral geometry**: Standard spectral triples work in Riemannian (positive-definite) metric. Physical spacetimes are Lorentzian (indefinite). Constructing Lorentzian spectral triples from Riemannian families naturally produces the indefinite signature.

2. **Dynamical geometry**: In the context of phonon-exflation, where the internal geometry (fiber SU(3)) evolves due to BCS pairing dynamics, families of spectral triples model time-dependent operators—a bridge between static K-theory and dynamical quantum mechanics.

3. **Foliation structure in NCG**: Noncommutative geometry has no a priori notion of time-slicing. Van den Dungen's construction provides a canonical way to introduce foliation structure respecting the algebraic framework.

---

## Key Arguments and Derivations

### Product Spectral Triples (Riemannian Case)

A **spectral triple** (A, H, D) consists of:
- A C*-algebra A (representing spacetime geometry)
- A Hilbert space H (fermion fields)
- A self-adjoint operator D (Dirac operator), with [D, a] bounded for all a in A

For a family of spectral triples {(A_t, H_t, D_t) : t ∈ [0, T]}, the **product spectral triple** is constructed on:
- Total Hilbert space: $H = L^2([0,T]) \otimes_{L^2([0,T])} H_t$
- Algebra: $A = C_0([0, T]) \otimes A_t$ (continuous functions on time × spacetime algebra)
- Total Dirac operator: $D = \frac{d}{dt} \otimes 1 + 1 \otimes D_t$

**Key property**: This product spectral triple is indeed a spectral triple—the commutators [D, a] are bounded (verified by direct calculation), and D is self-adjoint.

**Classical analogue**: In commutative geometry, if each A_t = C∞(M_t) is the algebra of smooth functions on a spatial slice M_t, then the product spectral triple recovers the Dirac operator on the spacetime M = [0,T] × M_t.

### Reconstruction Theorem (Riemannian)

The paper proves: **Given a family of spectral triples (A_t, H_t, D_t) parameterized by t ∈ [0,T], the product spectral triple recovers the spectral data of spacetime with foliation structure.**

Explicitly:
1. The spectrum of D in the product spectral triple reflects both temporal evolution (from d/dt) and spatial geometry (from D_t).
2. The spectral action Tr(f(D)) factorizes as an integral over time of the spectral actions on each slice.
3. The K-homology class [D] of the product triple relates to the K-homology classes [D_t] of the slices via a natural pairing.

### Lorentzian Spectral Triples

Classical Lorentzian spacetimes have indefinite metric signature (-,+,+,+). Standard spectral triples use the positive-definite metric. To obtain Lorentzian structure, van den Dungen employs **Krein spaces**—a generalization of Hilbert spaces where the inner product is indefinite.

**Construction**:
- Start with a family of Riemannian spectral triples (A_t, H_t, D_t).
- Construct the product spectral triple on $H = L^2([0,T], dt) \otimes H_t$
- Introduce the **Krein indefiniteness** via a sign operator J: apply J to the time component to flip the metric signature
- The **Lorentzian Dirac operator** becomes: $D_{Lor} = -i(\frac{d}{dt} \otimes J) + 1 \otimes D_t$

The minus sign and i in front produce a Lorentzian (indefinite) signature for the operator, while preserving the spectral triple axioms in the Krein space framework.

**Key result**: The Lorentzian spectral triple constructed this way is equivalent to a "reverse Wick rotation"—inverse to the standard analytic continuation from Lorentzian to Euclidean signature. This duality validates the construction: Lorentzian physics should emerge from Riemannian data via analytic continuation.

### Krein Space Formalism

A **Krein space** is a vector space with an indefinite sesquilinear form ⟨·,·⟩_J. The indefinite metric is captured by a self-adjoint involution J (with J² = 1):
$$\langle \psi, \phi \rangle_J = \langle \psi, J \phi \rangle_{Hilbert}$$

where ⟨·,·⟩_{Hilbert} is the standard Hilbert inner product. This allows:
- Operators with *non-self-adjoint spectra* to be studied rigorously
- Index theory to extend to indefinite settings
- Lorentzian geometry to be formulated in the spectral framework

---

## Key Results

1. **Product Spectral Triple Theorem**: A family {(A_t, H_t, D_t)} of spectral triples parameterized by t ∈ [0,T] yields a spectral triple on the product L^2([0,T]) ⊗ H_t with Dirac operator D = ∂_t ⊗ 1 + 1 ⊗ D_t.

2. **Riemannian Reconstruction**: The product spectral triple recovers the classical Dirac operator on foliated Riemannian manifolds, with spectral action factorization over time-slices.

3. **Lorentzian via Reverse Wick Rotation**: The Lorentzian spectral triple on indefinite-signature spacetime is constructible from Riemannian data via Krein space indefiniteness, formalizing reverse analytic continuation.

4. **Krein Space Index Theory**: The K-homology classes of Lorentzian spectral triples fit into the Krein space framework for unbounded KK-theory (developed in other van den Dungen papers), enabling index-theoretic computations in indefinite geometry.

5. **Foliation as Algebraic Structure**: Foliations are formalized purely algebraically via families of spectral triples—no a priori topological foliation leaf-structure needed.

---

## Impact and Legacy

This paper has become essential for:
- **Cosmological applications of NCG**: The foliation structure naturally models the expansion of spacetime as a family of spatial slices, each with its own spectral geometry.
- **Lorentzian noncommutative geometry**: Provides the rigorous framework for treating noncommutative spacetime with physical (indefinite) signature.
- **Quantum gravity with foliations**: Causal dynamical triangulations, loop quantum gravity, and other approaches that rely on spacetime foliations benefit from this algebraic formalization.

The paper bridges classical differential geometry (where foliation is topological) and functional analysis (where it becomes operator-algebraic), unifying discrete and continuous formulations.

---

## Connection to Phonon-Exflation Framework

**CRITICAL APPLICATION**: The phonon-exflation framework models the universe as:
- M^4 (base spacetime) undergoing Friedmann expansion
- SU(3)_fiber (internal color space) undergoing internal deformation (fiber compactification) as time progresses

This is precisely a *foliation of spacetime* where:
1. Each time-slice t has spatial geometry M^3_t (the 3D universe at time t)
2. The fibre SU(3) also evolves: deformation parameter τ(t) changes as the universe cools and BCS pairing dynamics proceed

**Van den Dungen's framework enables**:
- Spectral action computation at each time-slice, then integration over cosmic time
- Treatment of the fiber dynamics (τ(t)) as a time-dependent spectral triple family
- Formulation of the metric signature (Lorentzian on M^4, Euclidean on fibers) in a unified algebraic language

**Specific mechanism**:
- At each moment t, the spectral triple is (A_t, H_t, D_t(τ(t)))
- The Dirac operator D_t(τ) encodes both spatial geometry (Friedmann FLRW metric) and fiber geometry (deformed SU(3) with parameter τ)
- As τ evolves (due to BCS instability and instanton pair creation), the spectral action changes: dS/dt = ... reflects cosmological backreaction
- The product spectral triple structure allows separate treatment of metric expansion (d/dt from Friedmann equations) and fiber dynamics (dτ/dt from BCS evolution)

**Lorentzian signature**: The reverse Wick rotation formalism is essential because:
- The computational framework often works in Euclidean (Riemannian) signature for spectral action calculations
- The physical spacetime is Lorentzian (Wick rotated from Euclidean)
- Van den Dungen's reverse Wick rotation in Krein space formalizes the transition between these domains rigorously

**Connection to Volovik**: The foliation structure also resonates with Volovik's analog gravity program, where spacetime emerges from many-body condensed matter. The family of spectral triples models the emergence of spacetime from evolving condensate phases, each with its own "pseudo-spacetime" geometry.
