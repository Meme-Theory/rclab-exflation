# Electrodynamics from Noncommutative Geometry

**Author(s):** Koen van den Dungen, Matilde Marcolli
**Year:** 2011
**Journal:** Journal of Noncommutative Geometry 7 (2013), 433–456
**arXiv:** 1103.2928

---

## Abstract

We demonstrate that abelian gauge theories can be described within Connes' noncommutative geometry framework, contrary to prior assumptions. We show that a commutative spectral triple based on the two-point space yields U(1) gauge theory. We then modify the construction to obtain the full classical theory of electrodynamics on a curved background manifold. The work addresses a long-standing gap in applying noncommutative geometry to abelian theories.

---

## Historical Context

Connes' noncommutative geometry had proven remarkably successful at reproducing the Standard Model, but a puzzle remained: the framework seemed to naturally produce non-abelian gauge theories (SU(2), SU(3)) from the finite spectral triple, but U(1) (electromagnetism) appeared to be difficult to derive. This was conceptually troubling because U(1) is simpler and should have a cleaner geometric origin.

The issue stemmed from a subtlety: in NCG, a gauge symmetry arises from *inner derivations* of the algebra—automorphisms of the form a ↦ uau† for a unitary u. For U(1), the gauge parameter is a function φ(x) on spacetime, and the corresponding unitary is e^{iφ}. However, constructing the spectral triple so that this leads to the correct U(1) gauge field requires care: the algebra and Dirac operator must have the right structure.

Van den Dungen and Marcolli resolved this by showing how to construct a spectral triple on a simple finite space (the two-point space) such that the resulting almost-commutative manifold automatically encodes U(1) gauge theory. This was a significant advance because:

1. It completes the NCG description of the Standard Model by including U(1) rigorously
2. It shows the geometric origin of hypercharge U(1)_Y in the electroweak sector
3. It provides a clean pedagogical example of how abelian theories emerge in NCG

---

## Key Arguments and Derivations

### The Two-Point Space

The simplest finite noncommutative space is the **two-point space** X_2, which has:
- Points: {0, 1}
- Algebra: A_F = ℂ ⊕ ℂ (functions on the two points)
- Hilbert space: H_F = ℂ ⊕ ℂ (one dimension per point)
- Dirac operator: D_F = diag(m₀, m₁) (a diagonal 2×2 matrix)

The algebra acts by multiplication: f = (f₀, f₁) ∈ ℂ ⊕ ℂ acts on (ψ₀, ψ₁) ∈ ℂ ⊕ ℂ by (f₀ψ₀, f₁ψ₁).

In classical terms, this is just the data of two distinct points with masses m₀ and m₁.

### The Almost-Commutative Product M^4 × X_2

Combine the two-point space with spacetime M^4:
- Total algebra: A = C^∞(M^4) ⊗ (ℂ ⊕ ℂ)
- Hilbert space: H = L²(M^4, S) ⊗ (ℂ ⊕ ℂ)
- Dirac operator: D = D_{M^4} ⊗ 1 + γ_5 ⊗ D_F

where D_{M^4} is the Dirac operator on M^4 and γ_5 is the chirality matrix.

### Gauge Field Emergence

**Key insight**: Compute the commutator [D, a] for a = (f₀(x), f₁(x)) ∈ A:

$$[D, a] = [D_{M^4}, f] ⊗ 1 + γ_5 ⊗ [D_F, f]$$

The first term is [D_{M^4}, f] = [γ^μ ∇_μ, f] = γ^μ ∂_μ f (the Dirac operator commutes with scalars up to derivatives).

The second term is [D_F, a] = 0 because D_F is diagonal.

But here's the crucial modification: Introduce a **fluctuation** in the finite Dirac operator:
$$D_F(A) = \begin{pmatrix} m₀ & A \\ A^† & m₁ \end{pmatrix}$$

where A is a complex scalar field on spacetime (playing the role of a "potential" in the finite geometry).

Now:
$$[D, a] = ... + γ_5 ⊗ [D_F(A), f]$$

and the commutator [D_F(A), f] is **non-zero**: it involves the off-diagonal A, which doesn't commute with the diagonal masses.

### Covariant Derivative and Connection

As one computes [D, a]² and the action of [D, a] on the Hilbert space, a **covariant derivative structure emerges**:

$$∇_μ^A f = ∂_μ f + i A_μ f$$

where A_μ (the U(1) gauge field) is related to the fluctuation A of the finite Dirac operator. Specifically:
- The off-diagonal entry A of D_F couples to the exterior derivative on spacetime
- Gauge transformations a → uau† (with u = e^{iθ}) automatically generate A_μ → A_μ + ∂_μ θ

This is the **inner automorphism principle**: gauge symmetries arise from the algebra's automorphisms.

### Spectral Action and Maxwell Theory

The spectral action is:
$$S = Tr(f(D/Λ))$$

For the two-point space with the modified D_F(A), the expansion yields:

$$S = ∫ d^4x √g [a₀ + a₂ R + a₄(R² + (∇A)² + \text{mass terms})]$$

The (∇A)² term is the **kinetic energy of the electromagnetic field** in 4D. This is exactly the Maxwell action (up to sign conventions).

### Extension to Curved Spacetime

The two-point space spectral triple naturally extends to curved background spacetime (not just flat Minkowski). The Dirac operator on M^4 includes the spin connection ∇, and the total spectral action becomes:

$$S = ∫ d^4x √g [R + F_μν F^{μν} + \text{matter terms}]$$

where the first term is the Einstein-Hilbert action (gravity) and the second is Maxwell electrodynamics. This unifies gravity and electromagnetism at the spectral action level.

### Why Abelian Theories Were "Missing"

The reason abelian gauge theories seemed absent in early NCG work was:
1. Most finite spaces used had gauge groups SU(2) or SU(3) (like the Standard Model fiber)
2. These naturally arise from non-commutative algebras (e.g., M_2(ℂ) for SU(2))
3. U(1) is abelian and was thought to require a different, simpler construction
4. In fact, U(1) *does* come from a simple abelian algebra (ℂ ⊕ ℂ), but the gauge field emergence required the subtle understanding of fluctuations in D_F

---

## Key Results

1. **Abelian Gauge Theories in NCG**: Contrary to prior belief, U(1) gauge theories emerge naturally from the almost-commutative product M^4 × (two-point space).

2. **Gauge Field from Finite Dirac Fluctuations**: The U(1) gauge field arises from off-diagonal fluctuations in the finite Dirac operator, following the inner automorphism principle.

3. **Maxwell Electrodynamics from Spectral Action**: The spectral action on the M^4 × X_2 almost-commutative manifold automatically produces Maxwell's theory on curved spacetime.

4. **Gravity-Electromagnetism Unification**: The same spectral action produces both Einstein gravity and electromagnetism, unifying the two classical theories at the geometric level.

5. **Simplest Non-Trivial Case**: The two-point space provides the simplest example of NCG applied to gauge theory, making it pedagogically valuable.

6. **Consistency with Standard Model**: The U(1) constructed this way is identified with hypercharge U(1)_Y in the Standard Model, completing the NCG description of the SM gauge group.

---

## Impact and Legacy

Van den Dungen-Marcolli's work has enabled:
- Complete NCG treatment of all Standard Model gauge groups
- Construction of more complex gauge theories by combining finite spaces
- Clearer understanding of how abelian and non-abelian gauge theories arise differently in NCG (abelian from simple algebras, non-abelian from matrix algebras)
- Foundation for studying modified electromagnetism in noncommutative settings

---

## Connection to Phonon-Exflation Framework

**STRUCTURAL CLARITY**: The phonon-exflation framework employs SU(3) color gauge symmetry (as in the Standard Model), but the elegant treatment of U(1) by van den Dungen-Marcolli illuminates key aspects:

1. **Gauge Field Emergence Mechanism**: The principle that gauge fields arise from fluctuations in the finite Dirac operator is central. In phonon-exflation:
   - The Higgs field emerges from fluctuations in D_F on SU(3)
   - The "deformation parameter" τ can be viewed as a fluctuation in the Dirac operator
   - Gauge fields are covariant derivatives, naturally arising from the algebraic structure

2. **Inner Automorphism Principle**: Gauge transformations in the framework are inner automorphisms of the algebra A = C^∞(M^4) ⊗ A_finite. This ensures:
   - Global consistency: no anomalies if the algebra is self-adjoint
   - Automatic conservation of currents: Noether's theorem is built into the algebra

3. **Spectral Action Universality**: Just as Maxwell emerges from the two-point space, the full spectral action in phonon-exflation generates both:
   - Gravity and gauge theory (as in Chamseddine-Connes)
   - BCS many-body energy (from the fiber Dirac operator spectrum)
   - Instanton corrections (from higher Seeley-DeWitt coefficients)

4. **Simplicity and Elegance**: Van den Dungen-Marcolli show that the simplest finite spaces (two-point, three-point, etc.) generate rich gauge theory structures. This suggests that the phonon-exflation framework, built on SU(3) (which is richer), should encode layers of physics not yet fully explored.

5. **Connection to Renormalization**: The spectral action approach naturally incorporates renormalization through the heat kernel expansion. This is essential for computing corrections to the classical spectral action, which affects BCS dynamics predictions in the framework.

**Practical Application**: When computing the spectral action contributions to the effective potential in phonon-exflation, van den Dungen-Marcolli's explicit formulas for abelian theories serve as a check on the correctness of the calculations—if the U(1) hypercharge part of the framework is computed incorrectly, the full result will be unreliable.
