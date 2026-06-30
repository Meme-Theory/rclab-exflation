# A Universal Action Formula

**Author(s):** Ali Chamseddine, Alain Connes

**Year:** 1996

**Journal:** arXiv:hep-th/9606056

---

## Abstract

A universal formula for an action associated with a noncommutative geometry, defined by a spectral triple (A, H, D), is proposed. It is based on the spectrum of the Dirac operator and is a geometric invariant. The new symmetry principle is the automorphism of the algebra A which combines both diffeomorphisms and internal symmetries. Applying this to the geometry defined by the spectrum of the standard model gives an action that unifies gravity with the standard model at a very high energy scale.

---

## Historical Context

This is the foundational 1996 paper that introduced the **spectral action principle**. Rather than imposing an action Lagrangian by hand (as in the Standard Model), Chamseddine and Connes propose that the action is **derived from the spectrum of the Dirac operator D** through a purely geometric construction.

The spectral action is defined as:

S = Tr(f(D/Λ))

where f is a test function, Λ is a cutoff scale, and the trace is taken over the full Hilbert space H. The remarkable claim is that when applied to the Standard Model spectral triple, this formula **automatically** produces the Einstein-Hilbert action (gravity), Yang-Mills action (gauge interactions), and Higgs potential—without imposing any of them by hand.

This is the origin of the spectral action principle and represents a paradigm shift: **from imposed symmetries to emergent symmetries derived from spectral geometry**.

---

## Key Arguments and Derivations

### Section 1: The Spectral Action Principle

Given a spectral triple (A, H, D), define:

**Spectral Action**: S_ϕ = Tr(ϕ(D²/Λ²))

where:
- ϕ: ℝ⁺ → ℝ is a test function (often taken to be a step function or smooth approximation)
- D²: The square of the Dirac operator, a positive self-adjoint operator
- Λ: A UV cutoff scale
- Tr: Spectral trace (sum of eigenvalues weighted by ϕ)

The trace can be expanded in terms of heat-kernel asymptotics:

Tr(ϕ(D²/Λ²)) ~ Σ_{d=0}^{n} ∫_0^∞ ϕ(t) a_d(t^{-d/2}) dt

where a_d are the Seeley-DeWitt coefficients of the heat kernel expansion of e^{-sD²}.

### Heat Kernel Expansion

For a Dirac operator on a spin manifold M of dimension n:

Tr(e^{-sD²}) ~ s^{-n/2} Σ_d a_d s^{d/2}

Key Seeley-DeWitt coefficients:

- **a_0**: Topological (Euler characteristic, related to index)
- **a_{(n-4)/2}**: Einstein-Hilbert term, proportional to ∫_M R√g d^n x (Ricci scalar)
- **a_n/2**: Fourth-order gravity or Gauss-Bonnet term
- Higher a_d: Interaction terms, cosmological constant, etc.

When ϕ(t) = 1 for t ≤ 1 (a step function), the integral ∫_0^∞ ϕ(t) t^{d/2} dt diverges at the lower limit for negative d. Regularization picks out specific heat-kernel coefficients depending on dimension.

### The Standard Model Spectral Triple

The authors apply the spectral action to:

A = C(M⁴) ⊗ (ℂ ⊕ ℂ ⊕ M_3(ℂ) ⊕ M_2(ℂ))

This is an almost-commutative geometry:
- C(M⁴): Functions on spacetime
- ℂ ⊕ ℂ: Right-handed leptons and quarks (U(1)_Y hypercharge)
- M_3(ℂ): SU(3) color
- M_2(ℂ): SU(2) weak isospin

The internal Dirac operator D_f encodes all fermion masses and mixing angles.

### Result: Automatic Gauge Symmetries

A key observation: the automorphism group of the algebra A is:

Aut(A) = Diff(M⁴) × Aut(A_f) = Diffeomorphisms × Internal Gauge Symmetries

When the spectral action is evaluated on the Standard Model geometry, the automorphisms of A **naturally include** both coordinate transformations (gravity) and internal gauge transformations (Yang-Mills). No separate symmetry principle is imposed.

### The Action Formula in Dimension 4

For a 4-dimensional geometry, the spectral action reduces to:

S = a₀ Λ⁴ + a₂ Λ² ∫_M R√g d⁴x + a₄ ∫_M (R² + Ricci² + Weyl²) √g d⁴x + ...

where:
- **a₀ Λ⁴**: Cosmological constant (proportional to vacuum action a_0)
- **a₂ Λ² R term**: Einstein-Hilbert action (Newton's constant ~ a₂/Λ²)
- **a₄ terms**: Higher-order gravity corrections

Applied to the Standard Model:

S = ∫_M d⁴x √g [ (1/16πG)(R - 2Λ) + other terms ]

where 1/(16πG) arises from a₂, and Λ is extracted from a₀.

**The crucial point**: The action emerges entirely from the spectrum of D. No Lagrangian is written down. Gravity and gauge theory are unified at the level of spectral geometry.

### Unification of Gravity and Standard Model

In standard physics:
- Gravity (GR) involves the Ricci scalar R
- Electroweak and strong interactions involve non-abelian gauge fields and Higgs potential
- These are imposed by separate symmetry principles

In spectral geometry:
- All three emerge from Tr(ϕ(D²/Λ²))
- The gravitation coefficient depends on a₂
- The gauge interaction strength depends on a₄ and the internal geometry
- Unification occurs at the scale where these heat-kernel terms become comparable: Λ ~ M_Planck

---

## Key Results

1. **Geometry Encodes Physics**: The spectrum of the Dirac operator D on an (almost) commutative spectral triple contains all the information needed to construct the Einstein-Hilbert action and Standard Model Lagrangian.

2. **Emergent Symmetries**: Diffeomorphisms and internal gauge symmetries are not imposed by separate principles; they emerge as automorphisms of the spectral triple's algebra.

3. **Automatic Unification**: Gravity and Yang-Mills interactions are unified at the scale Λ where different heat-kernel coefficients contribute comparably.

4. **Dimensionless Fundamental Constants**: The parameters (Newton's constant, gauge couplings, Higgs mass) arise as ratios of Seeley-DeWitt coefficients, which are dimensionless in natural units. This addresses the question of why fundamental constants are what they are—they are determined by the internal spectral geometry.

5. **No Free Parameters in Geometry**: Once the spectral triple is fixed, the action formula is automatic. There are no additional coupling constants to dial in.

---

## Impact and Legacy

This 1996 paper revolutionized the approach to fundamental physics. It showed that the **geometric approach to physics** (starting from the Dirac operator) is not just mathematically elegant but can reproduce all known physics automatically.

The paper has been cited thousands of times and has inspired:
- Phenomenological applications to particle physics
- Refined spectral action principles for specific physics scenarios
- Connections to renormalization group flow
- Applications in quantum cosmology

It remains the canonical reference for the spectral action principle.

---

## Connection to Phonon-Exflation Framework

**Foundational to the framework's approach.**

The phonon-exflation framework applies the spectral action principle to an internal geometry D_K on M⁴ × SU(3)_Jensen rather than to the Standard Model geometry directly. Key connections:

1. **Same Principle, Different Geometry**: Instead of using the Standard Model's algebra, the framework uses a spectral triple whose internal Dirac operator encodes different physics:
   - Phononic modes (excitations of the internal structure)
   - GGE quasiparticles instead of elementary fermions
   - A Jensen-deformed SU(3) encoding the internal spectral moments

2. **Unification via Heat Kernel**: Like Chamseddine-Connes, the framework relies on Seeley-DeWitt coefficients to encode:
   - Gravitational coupling (a₂ moment)
   - Gauge coupling (a₄ moment)
   - Particle masses (higher moments)
   - Dark energy (a₀ moment vacuum action)

3. **K-Theoretic vs. Analytical**: This paper introduces the fundamental tension:
   - K-theoretically: The spectral triple structure (which automorphisms, which topological charges) is determined by index theory
   - Analytically: The actual values of coupling constants and masses depend on the detailed Seeley-DeWitt coefficients, which are **not** K-theoretically protected

The S71 workshop's findings about scheme-dependent vs. scheme-independent predictions are rooted in this 1996 paper's distinction.

**Papers to read together:**
- Chamseddine-Connes 2018 (Entropy and spectral action) — explains what determines the test function ϕ
- Connes 2008 (Reconstruction theorem) — establishes which spectral data is geometrically determined
- Van Suijlekom 2015 (Spectral action phenomenology) — applies spectral action to specific physics
- S71 workshop (Scheme-dependent/independent partition) — modern refinement of which parts are protected
