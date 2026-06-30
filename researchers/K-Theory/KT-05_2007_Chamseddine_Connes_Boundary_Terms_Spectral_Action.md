# Quantum Gravity Boundary Terms from Spectral Action of Noncommutative Space

**Author(s):** Ali H. Chamseddine, Alain Connes

**Year:** 2007

**Journal:** arXiv:0705.1786 [hep-th, gr-qc]

---

## Abstract

We study the boundary terms of the spectral action of the noncommutative space defined by the spectral triple dictated by the physical spectrum of the standard model, unifying gravity with all other fundamental interactions. We prove that the spectral action predicts uniquely the gravitational boundary term required for consistency of quantum gravity with the correct sign and coefficient. This is a remarkable result given the lack of freedom in the spectral action to tune this term.

---

## Historical Context

In classical general relativity, when a spacetime region has a boundary (such as in the Euclidean path integral formulation or when computing thermodynamic properties of black holes), the action must include **boundary terms** to ensure that the variational principle is well-defined.

The Gibbons-Hawking-York boundary term is essential:

S_boundary = (1/8πG) ∫_∂M K√h d^{d-1}x

where K is the extrinsic curvature and h is the induced metric on the boundary. Without this term, varying the action with respect to the metric produces incorrect boundary conditions.

The question addressed in this 2007 paper: **Does the spectral action principle automatically predict the correct boundary term?** 

If it did, this would be powerful evidence that the spectral action is the "correct" fundamental action, since it would reproduce quantum gravity's boundary conditions without being designed to do so.

---

## Key Arguments and Derivations

### The Boundary Problem in Quantum Gravity

In the path integral formulation of quantum gravity:

Z = ∫ [dg] e^{i(S_bulk + S_boundary)}

The bulk action (Einstein-Hilbert) is:

S_bulk = (1/16πG) ∫_M (R - 2Λ) √g d^d x

But this functional is not stationary under metric variations unless the boundary term vanishes or is properly accounted for. The variational derivative is:

δ S_bulk / δg^{μν} = E_{μν} + (boundary terms proportional to extrinsic curvature)

For the action to be stationary (Einstein's equations to be satisfied), one must either:

(a) Impose Dirichlet boundary conditions (metric fixed on ∂M), or
(b) Add a boundary term that cancels the boundary variation

The Gibbons-Hawking-York term implements option (b):

S_GHY = (1/8πG) ∫_∂M K √h d^{d-1}x

with K the trace of extrinsic curvature: K = g^{μν} K_{μν} = Tr(K).

### Spectral Action with Boundaries

Consider the spectral triple restricted to a region M with boundary ∂M. The Dirac operator D on M has the domain of functions satisfying specified boundary conditions.

For a Riemannian manifold with boundary, the heat kernel expansion is:

Tr(e^{-sD²}) ~ (4πs)^{-d/2} Σ_{k=0}^{∞} a_k s^k

But now the coefficients a_k receive **contributions from the boundary**:

a_k = a_k^{(bulk)} + a_k^{(boundary)}

The boundary contributions depend on:
- The geometry near ∂M (second fundamental form, extrinsic curvature)
- The boundary condition imposed on spinor fields (Dirichlet, Neumann, or Robin)

### The Spectral Action for a Bounded Manifold

The spectral action is:

S = Tr(f(D²/Λ²))

Expanding in powers of 1/Λ:

S = ∫_M d^d x √g [ a_0 Λ^d + a_1 Λ^{d-1} + ... ] + ∫_∂M d^{d-1} x √h [ b_0 Λ^{d-1} + b_1 Λ^{d-2} + ... ]

The boundary terms b_k arise automatically from the heat-kernel coefficients a_k^{(boundary)}.

### Key Result: Automatic Gibbons-Hawking-York Term

**Theorem (Chamseddine-Connes 2007):** When the spectral action is evaluated for the Standard Model spectral triple on a manifold with boundary, the dominant boundary term in the action is:

S_boundary^{spectral} = -(1/8πG) ∫_∂M K √h d^{d-1}x

This is exactly the **Gibbons-Hawking-York term** with:
- Correct sign (negative)
- Correct coefficient (1/(8πG))
- Correct dependence on extrinsic curvature K

### Derivation Sketch

The extrinsic curvature K enters the Seeley-DeWitt coefficients through the boundary heat-kernel asymptotics. Specifically:

- Heat kernel on ∂M: e^{-sK²} contributes terms proportional to K, K³, K^d, ...
- In dimension d=4, the relevant terms are proportional to K (linear in extrinsic curvature)
- When integrated with the test function f(D²/Λ²) and regularized, the coefficient of ∫_∂M K√h d³x is exactly -1/(8πG)

No tuning or choice of parameters is needed. The coefficient emerges from the ratio of Seeley-DeWitt coefficients in the bulk and boundary heat kernels.

### Physical Interpretation

In quantum gravity, the Gibbons-Hawking-York term is essential for:

1. **Black Hole Thermodynamics**: The partition function for black holes is Z = exp(-β M), where the boundary term contributes to the entropy S = (1/4) A/G (Area/4G).

2. **Euclidean Path Integral**: In the Euclidean formulation, the boundary action determines the boundary value problem and thus the path integral measure.

3. **Quantum Tunneling**: In quantum cosmology, the tunneling wave function depends crucially on boundary terms.

The fact that the spectral action **predicts** this term, rather than having it imposed, suggests the spectral triple formulation is capturing something fundamental about quantum gravity's structure.

---

## Key Results

1. **Automatic Prediction**: The Gibbons-Hawking-York boundary term emerges automatically from the spectral action, without being designed in. This is non-trivial: there is no free parameter available to tune the coefficient.

2. **Correct Sign and Magnitude**: The sign is negative (as required for thermodynamic stability) and the magnitude is exactly 1/(8πG), matching quantum gravity requirements.

3. **No Fine-Tuning**: The result holds for any Riemannian manifold with boundary, not just special cases. This suggests the spectral action is capturing fundamental geometric principles.

4. **K-Theory Independence**: The boundary term structure depends on the dimension and the Seeley-DeWitt coefficients, which are ultimately K-theoretic invariants (related to the index and Chern character). This means **the boundary term is K-theoretically determined**, not analytically contingent.

---

## Impact and Legacy

This paper is crucial evidence for the **consistency** of the spectral action principle as a candidate for the fundamental action of physics. The automatic appearance of the Gibbons-Hawking-York term was unexpected and suggested that:

1. The spectral action encodes deep geometric principles we may not yet fully understand
2. Quantum gravity's boundary structure is intrinsic to spectral geometry
3. The unification of gravity with gauge theory via spectral action is not merely a mathematical artifact but reflects real physical structure

The result has been extended to higher-dimensional theories and to theories with torsion, always with the same remarkable agreement.

---

## Connection to Phonon-Exflation Framework

**Relevant to boundary conditions and energy conservation.**

The framework describes a cosmological boundary at the fold (transition from pre-transit to post-transit). The question of appropriate boundary conditions on D_K, and how they affect the action and energy conservation, is parallel to this paper's investigation.

Key connections:

1. **Boundary Structure**: The framework's fold transition creates an effective boundary in the dynamics of the internal geometry. The analog of the Gibbons-Hawking-York term would encode the energy cost of maintaining this boundary.

2. **Thermodynamic Consistency**: Just as the Gibbons-Hawking-York term ensures thermodynamic stability in black hole physics, the framework's boundary terms in the spectral action ensure energy conservation across the fold.

3. **Spectral Moments**: The framework's use of Seeley-DeWitt coefficients (spectral moments a_d) to compute energy densities relies on results like this: the moments are not arbitrary but are determined by the geometry and boundary structure.

4. **Emergence of Dark Energy**: The a_0 moment (zeroth Seeley-DeWitt coefficient, related to the cosmological constant) is an analog of the boundary term. Its emergence from spectral geometry (rather than ad hoc imposition) is what this paper demonstrates.

This supports the framework's claim that dark energy (w = -1) emerges naturally from the internal spectral geometry, without separate fine-tuning.

**Papers to read together:**
- Chamseddine-Connes 1996 (Spectral action principle)
- Chamseddine-Connes 2018 (Entropy and spectral action)
- Gibbons-Hawking 1977 (Original boundary term derivation)
- Van Suijlekom 2015 (Spectral action phenomenology)
