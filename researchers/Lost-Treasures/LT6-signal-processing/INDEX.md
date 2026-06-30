# LT6: Signal Processing View of Spectral Theory

## Overview

This collection explores spectral theory through signal processing lenses, addressing the central question: **Is Lambda_residual (the cosmological constant) the DC component of the spectral action viewed as a filtered power spectral density?**

Three complementary papers establish the mathematical framework:

1. **Spectral action as power spectral density** (Sakellariadou) -- The noncommutative geometry spectral action sum over eigenvalues directly maps to power spectral density analysis.

2. **Eigenvalue density and random matrix universality** (Livan, Novaes, Vivo) -- Random matrix theory provides tools for analyzing spectral density as universal PSD, independent of matrix realization.

3. **DC component in dissipative systems** (Akemann, Fyodorov, Savin) -- Non-Hermitian spectral theory reveals that the zero-frequency (DC) component is universal and physically significant in open systems.

---

## Papers at a Glance

| # | Year | Authors | Topic | Lines | Key Result |
|---|------|---------|-------|-------|-----------|
| 01 | 2015 | Sakellariadou | Bosonic Spectral Action | 181 | f(0) = DC component of spectral expansion encodes cosmological constant |
| 02 | 2017 | Livan, Novaes, Vivo | Random Matrices Introduction | 177 | Wigner semicircle law: bulk eigenvalue density universal; DC ρ(0) encodes zero-frequency power |
| 03 | 2025 | Akemann, Fyodorov, Savin | Non-Hermitian Spectral Density | 164 | DC component ρ(0,0) universal in dissipative systems; eigenvector non-orthogonality quantified |

---

## Thematic Progression

### Part 1: Geometric Spectral Action (Sakellariadou)

The spectral action principle unifies gravity and the Standard Model:

S_Λ = Tr(f(D_A^2 / Λ^2))

The heat kernel expansion yields three key terms:
- **f_4 Λ^4**: cosmological constant (DC component f(0) at highest order)
- **f_2 Λ^2**: gravitational coupling
- **f_0**: coupling unification (constant term)

**Signal processing insight**: f(0) is the cutoff function's zero-frequency value, extracting the **DC baseline** of the spectral integral. This is where vacuum energy emerges.

Zeta function regularization improves on traditional cutoff approach by eliminating scale dependence and clarifying that the action is fundamentally spectral (eigenvalue-based), not coordinate-dependent.

### Part 2: Universal Spectral Density (Livan, Novaes, Vivo)

Random matrix theory shows that eigenvalue distributions (spectral densities) are **universal**: they depend only on symmetry class, not matrix details.

**Wigner semicircle law** (Hermitian case):
ρ(λ) = (1/πσ²) √(4σ² - λ²)

**Key properties**:
- Bulk density at center: ρ(0) = 1/(πσ²) -- this is the **DC (zero-frequency) power spectral density**
- Eigenvalues repel each other (Coulomb gas picture), preventing clustering
- Level spacing follows non-Poisson distributions

**Signal processing language**:
- ρ(λ) is PSD
- λ = 0 is the DC component
- The semicircular profile is the universal response of a "white noise + harmonic oscillator potential" system

This universality is crucial: **Lambda_residual, if interpreted as the DC component, would be robust across different UV regularizations** (different cutoff functions f), explaining why it appears universal in Nature.

### Part 3: Dissipative and Non-Hermitian Spectral Density (Akemann, Fyodorov, Savin)

Real systems involve dissipation (energy loss, decay rates). Non-Hermitian random matrices model open quantum systems where eigenvalues are complex:

λ = λ_R + i λ_I

where λ_I < 0 represents decay rates.

**Complex symmetric class AI†**:
- Eigenvalues populate the complex plane (not just real axis)
- Spectral density ρ(λ_R, λ_I) is 2D
- **DC component**: ρ(0, 0) = 1/π (the zero-frequency power at the center of the complex plane)
- This DC component is **universal** and independent of eigenvector non-orthogonality

**Eigenvector non-orthogonality condition number** κ:
κ = 1 / |⟨u | v⟩|

measures sensitivity of eigenvalues. High κ (weak eigenvector overlap) indicates instability; low κ (orthogonal eigenvectors) indicates stable, decoupled modes.

**Signal processing insight**: In a dissipative vacuum, the DC component ρ(0, 0) is the constant, zero-frequency power budget. The imaginary parts encode relaxation timescales. Eigenvector non-orthogonality predicts transitions (instabilities) in the vacuum state.

---

## Connection to Phonon-Exflation

The three papers establish a **unified spectral framework** for understanding the cosmological constant:

1. **Geometric origin** (Sakellariadou): Lambda emerges from the zero-frequency moment f(0) of the spectral action.

2. **Universal robustness** (Livan et al.): The DC component is universal across equivalent systems; this explains why Lambda appears in Nature independent of microphysical details.

3. **Dissipative vacuum dynamics** (Akemann et al.): The vacuum is not static but dissipative (particles decay, pair creation). Its effective Hamiltonian is non-Hermitian, with spectrum populating the complex plane. The DC component ρ(0, 0) survives this dissipation and is the **cosmological constant**.

**Framework synthesis**:
- M4 × SU(3) geometry (Kaluza-Klein) has a spectral triple (A, H, D)
- The spectrum of D encodes particle masses and the internal metric
- When vacuum dynamics become non-equilibrium (dissipative), the spectrum becomes non-Hermitian
- The cosmological constant Lambda_residual is the DC (zero-frequency) power of this dissipative spectrum
- This DC component is universal by random matrix theory, robust against UV regularization choices

---

## Open Questions

1. **Quantitative mapping**: How precisely does f(0) from the spectral action scale Tr(f(D²/Λ²)) relate to ρ(0) from RMT? Are there loop corrections?

2. **Eigenvector interpretation**: What do the phonon-exflation framework's "excitation modes" correspond to in the eigenvector structure? Are they orthogonal or do they exhibit non-trivial condition numbers κ?

3. **Dissipation mechanism**: What causes the phonon-exflation vacuum to be dissipative? Is it quantum (vacuum fluctuations) or geometric (KK compactification instability)?

4. **Edge vs. bulk**: Papers 1-3 emphasize bulk (DC) behavior. Does the spectral edge (highest-energy modes) play a cosmological role? Could it encode inflation?

5. **Experimental signatures**: Can the condition number κ (eigenvector non-orthogonality) be probed observationally? Does it predict specific galaxy cluster configurations or large-scale structure anomalies?

---

## Sources and Further Reading

### Primary Papers
- [Sakellariadou 2015 - Bosonic Spectral Action](01_2015_Sakellariadou_Bosonic_Spectral_Action.md)
- [Livan, Novaes, Vivo 2017 - Random Matrices](02_2017_Livan_Novaes_Vivo_Random_Matrices_Introduction.md)
- [Akemann, Fyodorov, Savin 2025 - Non-Hermitian Spectral Density](03_2025_Akemann_Fyodorov_Savin_NonHermitian_Spectral_Density.md)

### Related Works in Repository
- `researchers/Connes/` -- Foundational NCG and spectral action papers
- `researchers/Baptista/` -- KK geometry and higher-dimensional spectral aspects
- `researchers/Volovik/` -- Analog gravity and dissipative vacuum models
- `sessions/framework/` -- Phonon-exflation mechanism discussion files

---

## Notation Quick Reference

| Symbol | Meaning |
|--------|---------|
| D, D_A | Dirac operator (possibly fluctuated) |
| f(x) | Cutoff function in spectral action |
| Λ | Energy scale (cutoff) |
| Tr(...) | Trace over Hilbert space |
| ρ(λ) | Spectral density (density of eigenvalues) |
| a_n | Seeley-de Witt heat kernel coefficients |
| κ | Eigenvector condition number (non-orthogonality) |
| λ_I | Imaginary part of complex eigenvalue (decay rate) |
| ζ(0, D²) | Zeta function regularization of spectral action |

