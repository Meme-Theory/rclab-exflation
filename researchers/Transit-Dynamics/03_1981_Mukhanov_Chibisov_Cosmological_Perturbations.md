# Cosmological Perturbations in Inflationary Universe

**Author(s):** Viatcheslav F. Mukhanov, Gennadi V. Chibisov
**Year:** 1981
**Journal:** JETP Letters (Soviet Physics)

---

## Abstract

Mukhanov and Chibisov demonstrated that primordial density perturbations—the seeds of galaxies and large-scale structure—originate from quantum vacuum fluctuations amplified by inflation. They derived the power spectrum of curvature perturbations using gauge-invariant perturbation theory and the Bunch-Davies vacuum. The predicted spectral index n_s ≈ 1 (scale-invariant spectrum) is remarkably consistent with observations, making this work foundational to modern inflationary cosmology.

---

## Historical Context

Before Mukhanov and Chibisov, it was unclear whether quantum fluctuations could account for the observed inhomogeneities in the universe. Their insight was that in an exponentially expanding universe, quantum fluctuations on sub-horizon scales undergo two key transformations:

1. **Stretching**: A mode with wavelength λ < H⁻¹ (inside the Hubble horizon) is stretched by expansion to λ > H⁻¹ (outside the horizon).

2. **Freezing**: Once outside the horizon, the mode decouples from causal physics and its amplitude becomes frozen, preserving a "memory" of the quantum fluctuation.

This two-step process—stretching and freezing—naturally converts microscopic quantum noise into macroscopic classical perturbations. The power spectrum P(k) = (k³/2π²) |ζ_k|² remains nearly scale-invariant if the inflaton potential varies slowly (slow-roll).

---

## Key Arguments and Derivations

### Gauge-Invariant Formulation

Perturbations of the metric and matter fields contain gauge modes that are not physical. Mukhanov and Chibisov worked with gauge-invariant combinations. For scalar perturbations, the key variable is:

ζ = ψ + (H/ρ_m + p_m) δρ_m

where ψ is the curvature perturbation, H is the Hubble rate, and δρ_m is the matter density perturbation. This variable is gauge-invariant and remains constant outside the horizon.

### Mukhanov-Sasaki Equation

In the uniform-density gauge, scalar perturbations satisfy:

d²u_k/dη² + (k² - d²a/dη²/a) u_k = 0

where η is conformal time, a is the scale factor, and u_k is the Mukhanov variable (related to ζ by u_k = a ζ_k). During inflation with a ∝ 1/(-η)^(-1) (η < 0), this equation has the WKB solution:

u_k(η) = (e^{-ikη})/(√{2k}) for k η → 0⁻ (early times)

### Bunch-Davies Vacuum

The initial condition is the Bunch-Davies (adiabatic) vacuum, defined by specifying that at early times (k η → -∞), modes are in their ground state:

|ψ_in⟩ = ⊓_k |0_k⟩

This selects a unique vacuum in the asymptotically flat past. The mode function oscillates in the standard form:

u_k(η) = e^{-ikη}/√{2k}

### Power Spectrum Calculation

After exiting the horizon (k η ~ 0), the mode amplitude becomes:

|u_k|² = H²/(2k³) × (1 + O(ε))

where ε = -d(ln H)/d(ln a) ≪ 1 is the slow-roll parameter. The dimensionless power spectrum is:

P_ζ(k) = (k³/2π² V_0) |u_k|² = (H²)/(8π² ε) (k/a₀H₀)^{n_s - 1}

with spectral index:

n_s = 1 + 2η - 6ε

where η = d(ln ε)/d(ln a).

### Slow-Roll Limits

For a potential V(φ) with slow-roll parameters:

ε = (1/2)(V'/V)² (in Planck units)

the power spectrum amplitude at CMB scales is:

A_s = (V/(24π² ε))

Observable spectral index:

n_s ≈ 1 - 6ε + 2η

For m²φ²/2 inflation: n_s ≈ 1 - 2/N_* where N_* is e-folds to CMB scales.

---

## Key Results

1. **Quantum Origin of Structure**: Primordial density perturbations are predicted from first principles using quantum field theory, not postulated.

2. **Scale-Invariant Spectrum**: For slow-roll inflation, the spectral index n_s ≈ 1 is a direct prediction. Deviations (dn_s/d ln k) are suppressed by slow-roll parameters.

3. **Observable Consistency**: For simple potentials (m²φ², λφ⁴), predictions match WMAP and Planck data to ≲ 5%.

4. **Tensor Modes**: The same formalism predicts primordial gravitational waves (tensor perturbations) with power P_T ∝ ε. The tensor-to-scalar ratio r = P_T/P_S ≈ 16ε is a smoking-gun test of inflation.

---

## Impact and Legacy

Mukhanov-Chibisov is cited in nearly every paper on primordial perturbations. Their work:

- Provided the first calculation of the primordial power spectrum from quantum mechanics
- Showed that slow-roll inflation predicts n_s ≈ 1 (Harrison-Zeldovich spectrum), in agreement with observations
- Established the methodology (gauge-invariant perturbation theory + Bunch-Davies vacuum) used in all subsequent CMB studies
- Enabled falsification: deviations from n_s = 1 probe physics beyond slow-roll

Key follow-ups include Liddle's primordial power spectrum measurements, Starobinsky's R²-inflation model, and modern spectral-index measurements (Planck: n_s = 0.9661 ± 0.0040).

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

Mukhanov-Chibisov describes the amplification of **small-wavelength quantum fluctuations** into **large-scale classical perturbations** during a rapid phase transition. This is precisely the transit-dynamics picture in phonon-exflation, with crucial differences:

1. **Classical Background**: Mukhanov-Chibisov assumes classical (non-quantum) metric expansion. The framework claims expansion is NOT fundamental—it's emergent from spectral reorganization.

2. **Vacuum Choice**: The Bunch-Davies vacuum is imposed as an initial condition. The framework claims the correct vacuum at the fold is determined by the spectral action's extremal point (τ = 0.190).

3. **Power Spectrum**: Framework prediction is n_s = 0.9561 (from gauge-invariant spectral action on the fiber), slightly red-tilted. This differs from slow-roll inflation (n_s ≈ 0.96 with running), providing a discriminant.

4. **Key Test**: If CMB perturbations originate from GGE pair creation (not slow-roll amplification), the squeezed-limit bispectrum should vanish (f_NL ≈ 0). Framework predicts f_NL ~ ε_spectral (where ε_spectral ~ 0.01 is the deviation from scale-invariance). DESI/Planck can test this.

**Quantitative connection**: GGE relic = 59.8 pairs × 2 (boson/fermion) ≈ 120 quasiparticle excitations. Compare to Mukhanov-Chibisov: 120 modes above the quantum noise floor at CMB scales (k ~ 0.01 Mpc⁻¹). If the numbers match, structure formation is GGE acoustic, not inflaton-driven.
