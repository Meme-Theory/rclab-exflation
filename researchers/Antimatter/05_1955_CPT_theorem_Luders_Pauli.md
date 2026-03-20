# The CPT Theorem (1954-1957)

**Authors**: Gerhart Lüders (1954), Wolfgang Pauli (1955), John S. Bell (1955), Res Jost (1957)
**Key Papers**:
- Lüders, "On the Equivalence of Invariance under Time Reversal and under Particle-Antiparticle Conjugation," Dansk. Mat. Fys. Medd. 28, no. 5 (1954)
- Pauli, "Exclusion Principle, Lorentz Group and Reflection of Space-Time and Charge," in Niels Bohr and the Development of Physics (1955)
- Jost, "A remark on the C.T.P. theorem," Helv. Phys. Acta 30, 409 (1957)

## Statement of the Theorem

**CPT Theorem**: Any quantum field theory that is:
1. Lorentz invariant (obeys special relativity)
2. Local (fields at spacelike separation commute/anticommute)
3. Unitary (probability is conserved)
4. Has a Hermitian Hamiltonian bounded from below (stable vacuum)

is **invariant under the combined operation CPT**, where:
- **C** (Charge conjugation): particle ↔ antiparticle
- **P** (Parity): spatial reflection (**x** → -**x**)
- **T** (Time reversal): t → -t

## The Three Discrete Symmetries

### C — Charge Conjugation
Replaces every particle with its antiparticle:
- e⁻ ↔ e⁺, p ↔ p̄, ν ↔ ν̄
- Reverses all internal quantum numbers (charge, baryon number, lepton number)
- Preserves mass, spin, and momentum

### P — Parity (Spatial Inversion)
Reflects spatial coordinates through the origin:
- (t, **x**) → (t, -**x**)
- Reverses momentum: **p** → -**p**
- Preserves angular momentum: **L** → **L** (axial vector)
- Distinguishes left-handed from right-handed

### T — Time Reversal
Reverses the direction of time:
- (t, **x**) → (-t, **x**)
- Reverses momentum: **p** → -**p**
- Reverses angular momentum: **J** → -**J**
- Implemented as ANTI-unitary operator (Wigner)

## Consequences of CPT Invariance

### 1. Equal Masses
Every particle and its antiparticle have exactly the same mass:

    m(particle) = m(antiparticle)

Tested to extraordinary precision:
- m(p̄)/m(p) = 1 to 16 parts per trillion (BASE collaboration, CERN, Borchert et al. 2022)
- m(e⁺)/m(e⁻) = 1 to parts per billion

### 2. Equal Lifetimes
Every unstable particle and its antiparticle have the same total decay rate:

    τ(particle) = τ(antiparticle)

### 3. Opposite Charges
Every additive quantum number has opposite sign:

    Q(particle) = -Q(antiparticle)

for charge, baryon number, lepton number, strangeness, etc.

### 4. Equal Magnetic Moments (magnitude)
    |μ(particle)| = |μ(antiparticle)|

Tested by BASE: antiproton magnetic moment measured to 1.5 ppb precision, consistent with proton.

## Violations of Individual Symmetries

While CPT is exact, individual symmetries CAN be violated:

| Symmetry | Status | Discovery |
|----------|--------|-----------|
| P | VIOLATED | Wu experiment (1957): ⁶⁰Co β-decay |
| C | VIOLATED | Implied by P violation in chiral weak interaction |
| CP | VIOLATED | Cronin-Fitch (1964): K⁰ system; later B mesons |
| T | VIOLATED | CPLEAR (1998), BaBar (2012): implied by CP violation + CPT |
| CPT | CONSERVED | No violation observed at any precision |

### The Weak Interaction
The weak force maximally violates P and C separately:
- Only LEFT-handed neutrinos participate (P violation)
- C conjugation of left-handed neutrinos gives left-handed antineutrinos, which do NOT participate (C violation)
- But LEFT-handed neutrinos and RIGHT-handed antineutrinos both participate (CP approximately conserved)
- CP is violated at the ~10⁻³ level in K and B meson systems

## Jost's Proof (1957)

The most rigorous proof, due to Res Jost, uses the **Wightman axioms** for quantum field theory:

1. **Spectral condition**: Energy-momentum lies in or on the forward light cone
2. **Lorentz covariance**: Fields transform covariantly under the proper orthochronous Lorentz group
3. **Locality**: Fields at spacelike separation commute (bosons) or anticommute (fermions)
4. **Completeness**: The vacuum is cyclic for the field algebra

From these axioms, Jost proved that the Wightman functions (vacuum expectation values) satisfy:

    W(x₁,...,xₙ) = W(-xₙ,...,-x₁)   (with appropriate factors)

which is the CPT theorem in its most general form.

## Connection to the Phonon-Exflation Framework

### 1. The Real Structure J
In Connes' NCG, the **real structure J** on the spectral triple (A, H, D) is the algebraic encoding of charge conjugation. The conditions:

    J² = ε, JD = ε'DJ, Jγ = ε''γJ

where (ε, ε', ε'') depend on the KO-dimension mod 8, are the NCG avatar of CPT relations. For KO-dim 6: ε = 1, ε' = 1, ε'' = -1.

### 2. CPT in the Internal Space
On M⁴ × K, the full CPT operation decomposes:
- **M⁴ part**: Standard CPT of spacetime QFT
- **K part**: J acts on the internal space, implementing C
- The KO-dimension condition ensures consistency between these two pieces

### 3. Antiparticle Sector
The 32-dimensional H_F splits as 16 ⊕ 16 under the particle/antiparticle grading:
- γ_PA = diag(+I₁₆, -I₁₆) — particle-antiparticle grading
- J maps the +1 eigenspace to the -1 eigenspace
- This is CPT's C operation made algebraic

### 4. Experimental Anchor
ALPHA's antihydrogen spectroscopy provides precision tests of CPT at the parts-per-trillion level. If CPT were violated, the entire NCG framework would require fundamental revision since J's defining relations encode CPT.

## Key Equations

| Equation | Expression |
|----------|-----------|
| CPT transformation | Θ = CPT |
| CPT on scalar field | Θφ(x)Θ⁻¹ = φ†(-x) |
| CPT on spinor field | ΘΨ(x)Θ⁻¹ = γ₅Ψ*(-x) |
| Mass equality | m = m̄ (exact) |
| NCG real structure | JaJ⁻¹ ∈ A' (opposite algebra) |

## References

- G. Lüders, Dansk. Mat. Fys. Medd. 28, no. 5 (1954)
- W. Pauli, in Niels Bohr and the Development of Physics (1955)
- R. Jost, Helv. Phys. Acta 30, 409 (1957)
- J. S. Bell, Proc. R. Soc. A 231, 479 (1955)
- R. F. Streater and A. S. Wightman, PCT, Spin and Statistics, and All That (1964)
