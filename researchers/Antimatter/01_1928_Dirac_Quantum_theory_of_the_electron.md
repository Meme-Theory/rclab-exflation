# The Quantum Theory of the Electron (1928)

**Author**: Paul Adrien Maurice Dirac
**Published**: Proceedings of the Royal Society A, Vol. 117, No. 778, pp. 610-624
**Received**: 2 January 1928

## Abstract

A relativistic wave equation is derived for the electron that is first-order in both time and space derivatives, consistent with both quantum mechanics and special relativity. The equation naturally produces spin-1/2 as an intrinsic property and predicts the existence of negative-energy solutions that are later interpreted as antimatter.

## Historical Context

By 1927, quantum mechanics had achieved remarkable success through the Schrödinger equation, but this equation was fundamentally non-relativistic. The Klein-Gordon equation (1926) provided a relativistic generalization but was second-order in time, leading to negative probability densities — an unacceptable feature for a quantum-mechanical wave equation. Dirac sought a first-order equation compatible with both special relativity and quantum-mechanical probability interpretation.

## The Problem

The non-relativistic Schrödinger equation:

    iℏ ∂ψ/∂t = Hψ = (p²/2m)ψ

is first-order in time but second-order in spatial derivatives (through p² = -ℏ²∇²). The relativistic energy-momentum relation:

    E² = p²c² + m²c⁴

leads naturally to the Klein-Gordon equation, which is second-order in both time and space:

    (∂²/∂t² - c²∇² + m²c⁴/ℏ²)ψ = 0

Dirac insisted on a first-order equation to preserve the probability interpretation.

## Dirac's Approach

Dirac sought an equation of the form:

    iℏ ∂ψ/∂t = (cα·p + βmc²)ψ

where α = (α₁, α₂, α₃) and β are matrices to be determined. For this to be consistent with the relativistic energy-momentum relation, squaring both sides must reproduce E² = p²c² + m²c⁴. This requires:

1. **Anticommutation relations**: {αᵢ, αⱼ} = 2δᵢⱼI (the Clifford algebra)
2. **Mixed anticommutation**: {αᵢ, β} = 0
3. **Squares**: αᵢ² = β² = I

These relations CANNOT be satisfied by 2×2 matrices (the Pauli matrices). The minimum dimension is **4×4**, leading to the famous **gamma matrices**:

    γ⁰ = β,  γⁱ = βαⁱ

satisfying the Clifford algebra:

    {γᵘ, γᵛ} = 2gᵘᵛI₄

## The Dirac Equation

In covariant notation:

    (iγᵘ∂ᵤ - m)ψ = 0

or equivalently:

    (iℏγᵘ∂ᵤ - mc)ψ = 0

where ψ is a **four-component spinor** (bispinor):

    ψ = (ψ₁, ψ₂, ψ₃, ψ₄)ᵀ

The four components encode:
- Two spin states (up/down) for positive-energy solutions
- Two spin states (up/down) for negative-energy solutions

## Key Results

### 1. Spin as Intrinsic Property
The equation automatically produces spin-1/2 angular momentum. The total angular momentum J = L + S is conserved, where S = (ℏ/2)Σ with Σ built from the gamma matrices. Spin was NOT assumed — it emerged from requiring first-order Lorentz-covariant dynamics.

### 2. Magnetic Moment
The equation predicts g = 2 for the electron's gyromagnetic ratio, in excellent agreement with experiment (the small deviation g - 2 ≈ 0.00232 comes from QED radiative corrections, calculated later by Schwinger).

### 3. Fine Structure of Hydrogen
Applied to the hydrogen atom, the Dirac equation reproduces the observed fine structure splitting, resolving discrepancies that plagued earlier theories.

### 4. Negative-Energy Solutions
The equation admits solutions with E < 0. These cannot be ignored — they are a mathematical necessity of the Lorentz-covariant structure. Their physical interpretation would occupy Dirac for the next several years and ultimately lead to the prediction of antimatter.

## The Negative-Energy Problem

For a free particle, the energy eigenvalues are:

    E = ±√(p²c² + m²c⁴)

The negative-energy solutions form a continuum from -mc² to -∞. An electron in a positive-energy state could, in principle, radiate photons and cascade into negative-energy states without limit. This catastrophic instability demanded resolution.

## Mathematical Structure

The four linearly independent plane-wave solutions at momentum **p** are:

    u₁(p), u₂(p) — positive energy (E = +√(p²c² + m²c⁴))
    v₁(p), v₂(p) — negative energy (E = -√(p²c² + m²c⁴))

The positive-energy spinors satisfy:

    (γᵘpᵤ - m)u(p) = 0

The negative-energy spinors satisfy:

    (γᵘpᵤ + m)v(p) = 0

## Significance for the Phonon-Exflation Framework

The Dirac equation's four-component structure is essential to the NCG spectral triple. In Connes' framework:
- The Hilbert space H_F = C³² contains both particle and antiparticle sectors
- The real structure J acts as charge conjugation, swapping these sectors
- The KO-dimension 6 (mod 8) classification depends on the signs of J², Jγ, and JD
- The Dirac operator D_K on the internal space SU(3) encodes mass terms through its spectrum

The negative-energy solutions, reinterpreted as antiparticles through the Dirac sea or (more properly) through quantum field theory's creation/annihilation operators, are not a defect but a **structural necessity** that any complete framework must reproduce.

## Key Equations Summary

| Equation | Expression |
|----------|-----------|
| Dirac equation (covariant) | (iγᵘ∂ᵤ - m)ψ = 0 |
| Clifford algebra | {γᵘ, γᵛ} = 2gᵘᵛI₄ |
| Energy eigenvalues | E = ±√(p²c² + m²c⁴) |
| Probability current | jᵘ = ψ̄γᵘψ (positive-definite j⁰) |
| Spin operator | S = (ℏ/2)Σ, where Σⁱ = (i/2)ε^{ijk}γⱼγₖ |
| Gyromagnetic ratio | g = 2 (exact, at tree level) |

## References

- P. A. M. Dirac, "The Quantum Theory of the Electron," Proc. R. Soc. A 117, 610 (1928)
- P. A. M. Dirac, "The Quantum Theory of the Electron. Part II," Proc. R. Soc. A 118, 351 (1928)
