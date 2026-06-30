# The Effects of Relativistic Hidden Sector Particles on the Matter Power Spectrum

**Author(s):** Himanish Ganjoo, Adrienne L. Erickcek, Weikang Lin, Katherine J. Mack

**Year:** 2022

**Journal/ArXiv:** arXiv:2209.02735

---

## Abstract

If dark matter resides in a hidden sector minimally coupled to the Standard Model, another particle within the hidden sector might dominate the energy density of the early universe temporarily, causing an early matter-dominated era (EMDE). During an EMDE, matter perturbations grow more rapidly than they would in a period of radiation domination, which leads to the formation of microhalos much earlier than in standard cosmological scenarios.

These microhalos boost the dark matter annihilation signal, but this boost is highly sensitive to the small-scale cut-off in the matter power spectrum. If the dark matter is sufficiently cold, this cut-off is set by the relativistic pressure of the particle that dominates the hidden sector.

This work determines the evolution of dark matter density perturbations in this scenario, obtaining the power spectrum at the end of the EMDE. The authors analyze the suppression of perturbations due to the relativistic pressure of the dominant hidden sector particle and express the cut-off scale and peak scale (for which the matter power spectrum is maximized) in terms of the particle's properties.

The work also supplies transfer functions to relate the matter power spectrum with a small-scale cut-off (resulting from the pressure of the dominant hidden sector particle) to the matter power spectrum from a cold hidden sector. These transfer functions facilitate quick computation of accurate matter power spectra in EMDE scenarios with initially hot hidden sectors and identify which models significantly enhance microhalo abundance.

---

## Historical Context

Hidden sector models postulate additional particles and interactions beyond the Standard Model that couple weakly or not at all to visible matter. Such models provide solutions to various cosmological problems, including the nature of dark matter, matter-antimatter asymmetry, and neutrino masses.

In conventional cosmology, the universe transitions from radiation domination (early times, z >> 1000) to matter domination (z ~ 10,000 to present). During radiation domination, density perturbations grow logarithmically with the scale factor. Once matter domination begins, perturbations grow linearly with the scale factor.

An early matter-dominated era (EMDE) occurs if a non-relativistic particle in the hidden sector becomes the dominant component before the Standard Model sector reheats. During EMDE, matter perturbations experience faster growth than in radiation-dominated periods, potentially creating structure at unprecedented early times.

Microhalos--tiny dark matter concentrations formed in such scenarios--could significantly boost dark matter annihilation signals. However, the abundance and properties of microhalos depend critically on the small-scale structure of the matter power spectrum. Understanding how hidden sector particle properties affect this spectrum is essential for predicting observational signatures.

---

## Key Arguments and Derivations

### Early Matter-Dominated Era Mechanism

In hidden sector models with a particle Y that becomes subdominant or dominant in the early universe:

1. If Y is non-relativistic and initially subdominant, it can eventually dominate the energy density as the radiation energy dilutes away
2. The transition occurs when rho_Y ~ rho_radiation, at scale factor a_EMDE
3. During EMDE, the Hubble parameter evolves as:

   H^2 ~ rho_total ~ rho_Y ~ a^(-3)

   (compared to H^2 ~ a^(-4) during radiation domination)

4. The EMDE phase lasts until the hidden sector reheats or the Standard Model sector catches up

### Perturbation Evolution in EMDE

For a fluid component with density rho and pressure p, density perturbations at wavenumber k evolve according to modified Euler and continuity equations:

d^2 delta/dt^2 + 2H (d delta/dt) - 4 pi G rho delta = 0

where delta = delta rho / rho is the density contrast. During radiation domination, perturbations at fixed k oscillate. During matter domination, they grow as delta ~ a.

Relativistic pressure modifies this evolution. For a particle species with pressure p = w rho (where w is the equation of state parameter):

c_s^2 = w (adiabatic sound speed squared)

For relativistic particles (w ~ 1/3), the sound speed c_s ~ 0.577 in natural units.

Perturbations with wavenumber k < k_J (the Jeans wavenumber, defined by k_J^2 ~ 4 pi G rho / c_s^2) grow sublinearly due to pressure support. Modes with k > k_J are suppressed by the relativistic pressure. This creates a sharp cut-off in the matter power spectrum at the Jeans scale.

### Matter Power Spectrum and Cut-Off Scale

In EMDE scenarios with an initially hot (relativistic) hidden sector particle Y:

The matter power spectrum P(k) shows two characteristic scales:

1. **The Cut-Off Scale k_cut**: Set by the Jeans wavenumber during EMDE:

   k_cut ~ sqrt(4 pi G rho_Y / c_s^2)

   Perturbations at k > k_cut are suppressed. The suppression factor depends on the time the perturbations spend in the EMDE phase and the relativistic pressure of Y.

2. **The Peak Scale k_peak**: The wavenumber at which P(k) is maximized, determined by the growth history:

   Modes entering the horizon during EMDE experience different growth rates than modes entering during radiation domination, creating a peak in the spectrum at a characteristic scale.

### Transfer Function Formalism

The work develops transfer functions T(k) that relate the power spectrum with a relativistic-pressure-induced cut-off to the power spectrum of a cold hidden sector:

P_hot(k) = T(k) * P_cold(k)

This allows fast computation of power spectra in scenarios with initially hot hidden sectors without solving full perturbation equations for each model. The transfer function encodes:

- The evolution of the relativistic pressure during EMDE
- The duration of EMDE (determined by reheating dynamics)
- The coupling between dark matter and the hidden sector particle

### Microhalo Abundance

The small-scale cut-off in the power spectrum directly determines the microhalo abundance. Using the Press-Schechter formalism:

dn/dm ~ 1/m * |d(ln sigma(m))/d(ln m)| * exp(-nu^2/2)

where nu = delta_c / sigma(m) is the collapse threshold normalized by the r.m.s. density contrast sigma(m) smoothed on mass scale m.

With a cut-off at k_cut, the minimum mass of microhalos increases, and the abundance changes accordingly. The work quantifies how different hidden sector models (varying Y mass, Y velocity dispersion, EMDE duration) affect the microhalo population.

---

## Key Results

1. **Relativistic Pressure Suppression**: The relativistic pressure of a dominant hidden sector particle suppresses matter power spectrum perturbations at scales smaller than the Jeans scale, creating a sharp cut-off.

2. **Jeans Scale Prediction**: The cut-off scale is determined by the Jeans wavenumber during EMDE:

   k_cut ~ sqrt(4 pi G rho_Y / c_s^2)

   For relativistic Y particles, this translates to specific suppression across different hidden sector models.

3. **Transfer Function Library**: The authors provide transfer functions for multiple EMDE scenarios (initially subdominant Y particles, initially dominant Y particles, varying Y properties) enabling rapid computation of accurate power spectra.

4. **Peak Scale Dependence**: The peak scale k_peak depends on the EMDE duration and the transition dynamics, shifting to larger scales for longer EMDE periods.

5. **Microhalo Abundance Enhancement**: Models that extend EMDE (larger parameter space) show significant enhancement of microhalo abundance compared to standard CDM, with factors of 10-10,000 enhancement depending on scenario.

6. **Observational Prospects**: Enhanced microhalo populations produce detectable signatures in dark matter annihilation signals (gamma-ray background), 21-cm absorption features from early star formation, and indirect detection experiments.

---

## Impact and Legacy

This work established the systematic framework for understanding how hidden sector properties affect structure formation in early-universe scenarios. The transfer function approach became standard for rapidly assessing dark matter power spectra in EMDE models.

The quantitative connection between hidden sector particle properties (mass, velocity dispersion, coupling) and microhalo abundance informed subsequent searches for signatures of early structure formation in observations ranging from gamma-ray astronomy to 21-cm cosmology.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework addresses dark matter and dark energy through spectral geometry of M4 x SU(3). The framework predicts both visible matter (phononic excitations of Dirac spectrum) and dark matter (from spectral geometry evolution).

Specific connections include:

- **Hidden Sector as Internal Geometry**: In phonon-exflation, the "hidden sector" is the internal SU(3) geometry. Just as hidden sector particles affect large-scale structure, the internal geometry's excitations shape cosmic evolution.

- **Early Universe Modifications**: Both frameworks involve modifications to the early-universe expansion history. EMDE scenarios demonstrate how subdominant components can dramatically affect structure formation. Phonon-exflation's spectral action provides an alternative mechanism for early-universe modifications.

- **Matter Power Spectrum Constraints**: The matter power spectrum observations constrain both hidden sector models and spectral geometry scenarios. The framework's predictions for structure formation must satisfy the same constraints as hidden sector EMDE models.

- **Dark Matter Multiphase**: If phonon-exflation produces both phononic dark matter (from Dirac spectrum excitations) and geometric dark matter (from internal compactification modes), the combined system parallels hidden sector scenarios with multiple particle species affecting structure formation.

The systematic approach to understanding how internal degrees of freedom affect cosmological structure in this paper directly applies to testing phonon-exflation predictions.
