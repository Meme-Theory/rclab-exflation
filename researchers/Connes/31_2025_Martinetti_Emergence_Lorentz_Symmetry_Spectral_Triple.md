# Emergence of Lorentz Symmetry from an Almost-Commutative Twisted Spectral Triple

**Author:** Pierre Martinetti

**Year:** 2025

**Journal:** arXiv:2502.18105

---

## Abstract

This paper demonstrates how the transition from a Riemannian (Euclidean signature) twisted spectral triple to a pseudo-Riemannian (Lorentzian signature) spectral triple arises within an almost-commutative structure. The approach operates without introducing complex numbers or Wick rotation, instead acting directly on the metric and Christoffel symbols. The result shows that Lorentzian signature emerges naturally from the algebraic structure of almost-commutative geometry underlying the noncommutative Standard Model, suggesting that the signature change is a fundamental consequence of the model rather than an imposed symmetry.

---

## Historical Context

The question of metric signature in quantum gravity has persisted since the inception of path integral formulation. In Euclidean quantum field theory (used in lattice simulations and perturbative calculations), spacetime has positive-definite metric signature $(+,+,+,+)$. Physical observables, however, require Lorentzian signature $(+,-,-,-)$ or $(-,+,+,+)$.

The standard resolution is Wick rotation: analytically continue time to imaginary values, compute in Euclidean space, and rotate back to physical Lorentzian time. While this works pragmatically, it leaves a fundamental question unresolved: is the signature change a mathematical artifact (two descriptions of the same physics) or does it reflect a deeper transition in the underlying geometry?

Martinetti's work (2023-2025) argues for the latter: Lorentzian signature emerges from the almost-commutative structure as a phase transition in the geometry itself. The twist (automorphism of the spectral triple) becomes the driving mechanism. During the twist evolution, the metric signature changes from Riemannian to pseudo-Riemannian.

---

## Key Arguments and Derivations

### Metric Signature and Eigenvalues of the Metric Tensor

A Riemannian manifold has positive-definite metric $g_{\mu\nu} > 0$ (all eigenvalues positive). A pseudo-Riemannian (Lorentzian) manifold has indefinite signature: one negative eigenvalue and three positive (or vice versa in other conventions).

In the spectral triple formalism, the metric arises from the inverse of the spin structure and the Dirac operator's spatial derivatives. For a flat spacetime:

$$g_{\mu\nu} = \delta_{\mu\nu}$$

The Dirac operator acts as:

$$D = \sum_\mu \gamma^\mu \partial_\mu$$

where $\gamma^\mu$ are the Clifford algebra generators satisfying:

$$\{\gamma^\mu, \gamma^\nu\} = 2 g^{\mu\nu}$$

In Euclidean signature, $g_{\mu\nu} = \delta_{\mu\nu}$, and the Clifford algebra is positive-definite. In Lorentzian signature, $g_{\mu\nu}$ has indefinite signature, and the Clifford algebra is indefinite-metric (Minkowski algebra).

### The Twisted Transition Mechanism

Consider a family of twists parameterized by a parameter $s$ (which Martinetti interprets as emergent time):

$$\sigma(s) = \exp(i s \mathcal{K})$$

where $\mathcal{K}$ is a generator in the almost-commutative algebra. As $s$ varies, the twisted Dirac operator evolves:

$$D(s) = \sigma(s)^{-1} D \sigma(s) + i \dot{\sigma}(s) \sigma(s)^{-1}$$

The metric tensor, derived from the anticommutation relations, also evolves:

$$g_{\mu\nu}(s) = \langle \gamma_\mu | g(s) | \gamma_\nu \rangle$$

where $g(s)$ is constructed from the spectral triple at parameter value $s$.

Martinetti's key result: there exists a critical value $s_c$ such that:
- For $s < s_c$: $g_{\mu\nu}(s)$ is positive-definite (Euclidean)
- For $s > s_c$: $g_{\mu\nu}(s)$ has indefinite signature (Lorentzian)

At $s = s_c$, the metric is degenerate — one eigenvalue vanishes. This is the signature transition point.

### Direct Manipulation of Christoffel Symbols

Rather than using Wick rotation (complex analyticity), Martinetti directly transforms the Christoffel symbols:

$$\Gamma_{\mu\nu}^\lambda(s) = \frac{1}{2} g^{\lambda\rho}(s) \left( \frac{\partial g_{\nu\rho}}{\partial x^\mu} + \frac{\partial g_{\mu\rho}}{\partial x^\nu} - \frac{\partial g_{\mu\nu}}{\partial x^\rho} \right)$$

During the transition, the connection coefficients change continuously, but the curvature (Riemann tensor) exhibits a discontinuity in its signature properties. This is a geometric phase transition.

### Almost-Commutative Geometry Framework

In almost-commutative geometry, the space is a product:

$$M \times F$$

where $M$ is a smooth Lorentzian (or Euclidean) 4-manifold, and $F$ is a finite noncommutative space. The total spectral triple is:

$$D_\text{total} = D_M \otimes \mathbb{1}_F + \mathbb{1}_M \otimes D_F$$

The twist acts on both the $M$ part and the $F$ part. Crucially, the twist in the $F$ sector (internal geometry) induces a twist in the $M$ sector (spacetime metric).

This coupling is key: changing the internal geometry (what physicists call "compactification" or "internal space evolution") automatically changes the signature of the external spacetime. There is no separation.

The authors show that for the Standard Model's finite space $F$, the twist parameter naturally interpolates between Euclidean and Lorentzian signatures. The critical transition point corresponds to the Higgs condensate forming (in particle physics language).

### The Role of Complex Numbers — or Their Absence

Traditional Wick rotation uses complex analyticity: $t \to -i t$. This method relies on the assumption that correlation functions are analytic in the complex $t$-plane.

Martinetti's approach avoids complex numbers entirely. The signature change is purely geometric: it's a deformation of the metric tensor within the real manifold, driven by the twist parameter. This is conceptually cleaner and suggests that the signature change is fundamental, not a calculational trick.

Mathematically, the difference is subtle but important: in Wick rotation, the Euclidean and Lorentzian theories are related by analytic continuation of a third, complexified theory. In Martinetti's approach, they are related by geometric deformation of the spectral triple — a more direct connection.

---

## Key Results

1. **Signature emergence without Wick rotation**: Lorentzian signature emerges naturally from the almost-commutative structure through twist-induced deformation of the metric tensor.

2. **Critical transition point**: The transition occurs at a specific value of the twist parameter, where one eigenvalue of the metric vanishes. This is a geometric phase transition analogous to a critical point in condensed-matter physics.

3. **Coupling of internal and external geometry**: The twist in the finite space $F$ (internal geometry) directly induces the metric signature change in the external spacetime $M$. There is no separation between "internal symmetries" and "spacetime symmetry."

4. **Algebraic determination of signature**: The signature is determined purely by the algebraic structure of the almost-commutative geometry, not by external imposition or analytic continuation.

5. **Higgs connection**: The signature transition coincides with the Higgs condensate formation. In Euclidean space (before transition), there is no Higgs vev. In Lorentzian space (after transition), the Higgs acquires its physical vev.

---

## Impact and Legacy

This paper contributes to a growing body of work (2020s) on emergence of spacetime from quantum geometry. It influences:

- **Causal set theory**: signature emergence in causal sets as a discretization of emergent spacetime.
- **Asymptotic safety**: signature-dependent renormalization flows in quantum gravity.
- **Holographic duality**: the signature transition as a bulk/boundary crossing in AdS/CFT.
- **Inflation theories**: the idea that inflation initiates at a signature transition.

---

## Framework Relevance

**FUNDAMENTAL**: This paper provides the geometric foundation for the phonon-exflation framework's signature transition.

1. **Euclidean-to-Lorentzian transition**: The framework models the tau-fold transit as a signature change from Euclidean (internal, imaginary-time quantum dynamics) to Lorentzian (external, physical cosmological dynamics). Martinetti's formalism provides the exact mechanism: the twist parameter interpolates between signatures.

2. **Twist parameter = tau**: In the framework, tau parameterizes the fold geometry (internal curvature). Martinetti's result suggests that tau is the twist parameter driving the signature transition. The fold IS the signature change.

3. **Higgs condensate = critical point**: The BCS instability (phonon-exflation mechanism) can be interpreted as the critical point where the metric signature changes. The Cooper-pair condensate forms precisely because the geometric signature becomes Lorentzian, allowing particle creation (Schwinger-type tunneling becomes possible).

4. **Internal geometry drives cosmology**: The coupling between the finite-space twist and the external spacetime signature explains how internal quantum dynamics (the K_7 instanton gas) drives cosmic evolution. There is no ad hoc scalar field; rather, the curvature emerges from the signature change.

5. **No external time**: The framework predicts that classical time does not exist in the pre-transit state (Euclidean). Time emerges as the metric signature becomes Lorentzian. Martinetti's paper supports this: before the transition, $t$ is a coordinate in Euclidean space; after, it becomes the physical time of Lorentzian spacetime.

6. **Quantum critical point**: The signature transition is a quantum critical point (zero energy cost). The framework predicts that the transition occurs spontaneously at the initial state (tau=0 is unstable maximum), with any perturbation triggering the cascade. This is consistent with Martinetti's critical-point picture.

**Direct application**: Paper #31 should be used to formalize the geometric underpinnings of the fold transition in the framework's master equation. The spectral triple at tau should be written as a twisted family, with the twist parameter explicitly tracking the signature change. This would elevate the framework from phenomenological BCS + spectral action to a fully geometric noncommutative picture.

