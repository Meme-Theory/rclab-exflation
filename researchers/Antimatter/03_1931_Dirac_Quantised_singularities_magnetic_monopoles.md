# Quantised Singularities in the Electromagnetic Field (1931)

**Author**: Paul Adrien Maurice Dirac
**Published**: Proceedings of the Royal Society A, Vol. 133, No. 821, pp. 60-72
**Year**: 1931

## Abstract

Dirac demonstrates that the existence of even a single magnetic monopole in the universe would require all electric charges to be quantized. He derives the famous Dirac quantization condition and introduces the concept of the "Dirac string" — an unobservable singularity connecting monopoles.

## The Quantization Condition

### Setup
Consider a magnetic monopole with magnetic charge g at the origin. Its magnetic field is:

    **B** = g **r̂** / (4πr²)

This is the magnetic analog of a point electric charge. The total magnetic flux through any closed surface containing the monopole is:

    Φ = g (in Gaussian units)

### The Argument
In quantum mechanics, the wave function of an electrically charged particle (charge e) must be single-valued. When transported around a closed loop encircling a Dirac string, the wave function acquires a phase:

    ψ → exp(ie/ℏc ∮ **A**·d**l**) ψ

For single-valuedness, this phase must be a multiple of 2π:

    eg/(ℏc) = n/2,  n ∈ ℤ

Or equivalently:

    **eg = nℏc/2**    (Dirac quantization condition)

### Profound Implication
If even ONE magnetic monopole exists anywhere in the universe, then ALL electric charges must be quantized in units of:

    e₀ = ℏc/(2g)

This is the only known theoretical explanation for the observed quantization of electric charge.

## The Dirac String

The vector potential **A** for a monopole field cannot be defined smoothly everywhere. Dirac showed that **A** must have a line singularity (the "Dirac string") extending from the monopole to infinity. The string is physically unobservable — it can be moved by gauge transformations — but it cannot be eliminated. Different gauge choices place the string along different directions.

### Wu-Yang Fiber Bundle Interpretation (1975)
Wu and Yang showed that the Dirac string is an artifact of trying to cover S² with a single coordinate patch. In the fiber bundle language:
- The monopole defines a principal U(1) bundle over S²
- The Dirac quantization condition becomes: the first Chern number c₁ = n must be an integer
- This is a TOPOLOGICAL requirement, not merely a quantization condition

The classification of U(1) bundles over S² is:

    π₁(U(1)) = ℤ

Each integer n labels a distinct topological class of monopoles.

## Non-Abelian Generalization

't Hooft (1974) and Polyakov (1974) independently discovered that magnetic monopoles arise as FINITE-ENERGY solutions in non-Abelian gauge theories when a larger gauge group G is broken to a subgroup H containing a U(1) factor. The topological classification becomes:

    π₂(G/H) ≠ 0

For the Standard Model breaking SU(2)×U(1) → U(1)ₑₘ, the relevant homotopy group is:

    π₂(SU(2)×U(1)/U(1)ₑₘ) = ℤ

guaranteeing the existence of monopole solutions (GUT monopoles).

## Connection to the Phonon-Exflation Framework

### 1. Topological Defects in BEC
Quantized vortices in the phonon-exflation simulation are the 2D analog of Dirac monopoles:
- Vortex charge is quantized: κ = nh/m
- The phase singularity is the BEC analog of the Dirac string
- Vortex-antivortex pairs ↔ monopole-antimonopole pairs
- The D/H ratio computation counts these topological defects

### 2. NCG Monopoles
In the Kaluza-Klein framework on M⁴ × SU(3):
- The isometries of SU(3) generate gauge fields
- Monopole-like configurations correspond to non-trivial π₂ of the coset space
- The Jensen deformation (TT-deformation of the metric) could affect monopole masses

### 3. Charge Quantization
The Dirac quantization condition provides a topological explanation for why electric charge is quantized. In the phonon-exflation framework, charge quantization should emerge from:
- The Peter-Weyl decomposition of L²(SU(3))
- The representation theory of the gauge group
- This is already partially verified: SM quantum numbers emerge correctly (Session 7)

## Experimental Status

No fundamental magnetic monopole has been observed despite extensive searches:
- **MoEDAL** at CERN (ongoing): searches for highly ionizing particles
- **IceCube**: neutrino telescope searches for relativistic monopoles
- **MACRO** (1989-2000): underground detector at Gran Sasso
- **Cabrera event** (1982): single candidate event, never reproduced

The absence of monopoles is theoretically puzzling if GUT symmetry breaking occurred in the early universe (the "monopole problem"), which was one motivation for cosmic inflation.

## Key Equations

| Equation | Expression |
|----------|-----------|
| Dirac quantization | eg = nℏc/2 |
| Monopole field | **B** = g**r̂**/(4πr²) |
| Minimum magnetic charge | g₀ = ℏc/(2e) = 68.5e |
| First Chern number | c₁ = (1/2π)∫_{S²} F = n |
| 't Hooft-Polyakov mass | M_mon ~ M_GUT/α_GUT |

## References

- P. A. M. Dirac, "Quantised Singularities in the Electromagnetic Field," Proc. R. Soc. A 133, 60 (1931)
- T. T. Wu and C. N. Yang, "Concept of nonintegrable phase factors and global formulation of gauge fields," Phys. Rev. D 12, 3845 (1975)
- G. 't Hooft, "Magnetic monopoles in unified gauge theories," Nucl. Phys. B 79, 276 (1974)
- A. M. Polyakov, "Particle spectrum in quantum field theory," JETP Lett. 20, 194 (1974)
