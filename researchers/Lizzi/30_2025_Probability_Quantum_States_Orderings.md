# From classical probability densities to quantum states: quantization of Gaussians for arbitrary orderings

**Authors:** G. Lo Giudice, L. Leone, Fedele Lizzi
**Year:** 2024
**arXiv:** 2411.14043v2

---

## Abstract

We investigate mapping classical probability densities (especially Gaussians) to valid quantum states. The challenge: quantum operators don't commute, so position-momentum correspondence is ambiguous (operator ordering problem). For different orderings (antinormal, normal, Weyl, symmetric), a classical Gaussian maps to different quantum states. Remarkably, even a δ-function (ultra-localized classical state) maps to a valid quantum state under antinormal ordering.

---

## Key Arguments

### 1. Classical-Quantum Correspondence
Classical: ρ(x,p) is a probability density, sharply defined at each phase-space point.

Quantum: ρ̂ is an operator (density matrix) on Hilbert space. Many ρ̂ can correspond to same classical ρ depending on **operator ordering choice**.

### 2. Wigner Function Ambiguity
Given a classical Gaussian:
$$\rho_\text{classical}(x,p) = \exp(-(\Delta x)^{-2} x^2 - (\Delta p)^{-2} p^2)$$

Multiple quantum states give this Wigner function:
- **Weyl ordered**: Standard quantization, ρ̂ = ∫dx dp ρ(x,p) e^{i(p\hat{p} + x\hat{x})}
- **Normal ordered**: Creation/annihilation operator ordering—ground state can be modified
- **Antinormal ordered**: Opposite ordering—largest uncertainty
- **Symmetric**: Average of all orderings

### 3. Ordering Dependence
For a Gaussian with classical variance λ:
$$|\psi_\lambda\rangle_\text{Weyl} = \text{exp}(-\frac{\lambda}{2}\hat{x}^2), \quad |\psi_\lambda\rangle_\text{normal} \neq |\psi_\lambda\rangle_\text{Weyl}$$

The differences are **observable**: transition amplitudes, energy expectation values differ.

### 4. δ-Function Paradox Resolution
Classical δ-function (zero uncertainty):
$$\rho(x) = \delta(x), \quad \rho(p) = \text{const}$$

This has **no quantum equivalent** under Weyl ordering (would require infinite energy).

**But** under **antinormal ordering**, a valid quantum state exists:
$$|\psi_\delta\rangle_\text{anti} = | \text{eigenstate of } \hat{p} \rangle$$

The infinite position-uncertainty is "hidden" in the antinormal-ordered representation.

### 5. Physical Interpretation
Different orderings correspond to **different measurement contexts**:
- **Weyl**: Symmetric measurements (ideal)
- **Normal**: Absorptive process (particle creation measured first)
- **Antinormal**: Emissive process (particle annihilation measured first)

---

## Key Results

1. **No unique quantization**: Classical density ↔ many quantum states (all valid).

2. **Ordering is physical**: Different orderings give different observable consequences; the choice corresponds to measurement protocol.

3. **δ-function solved**: Even ultra-localized states have quantum realization under appropriate ordering choice.

4. **Planck-scale uncertainty**: At Planck scale, antinormal-ordered structures might dominate, explaining why position becomes indefinite (hidden in ordering).

---

## Technical Significance

**Arbitrary ordering formula**: For general ordering parameter s:
$$\hat{\rho}_s = \int \frac{dx dp}{2\pi\hbar} \rho(x,p) \, W_s(\hat{x}, \hat{p})$$

where W_s is s-dependent Wigner function (0 = antinormal, 1/2 = Weyl, 1 = normal).

---

## Connection to Phonon-Exflation

**Phonon quantization**: The framework's phonon operators might have operator-ordering ambiguities. This paper shows:

1. **Multiple phonon Fock spaces possible**: Depending on creation/annihilation ordering, the phonon Fock space has different structure.

2. **Measurement protocol matters**: Whether phonon creation or annihilation is "primary" determines which ordering applies, which determines the GGE relic structure.

3. **Antinormal ordering interpretation**: If framework uses antinormal ordering for phonon creation operators, this could explain why phonon position is fundamentally indefinite (antinormally-hidden uncertainty).

**Framework question**: Does the framework specify which **operator ordering** applies to phonon creation/annihilation? Different orderings would give different predictions for GGE relic properties.

This paper suggests the framework should **explicitly choose and justify** an ordering prescription, as observable consequences depend on this choice.
