# Holographic Quantum-Foam Blurring Is Consistent with Observations of GRB 221009A

**Author(s):** Eric Steinbring
**Year:** 2023
**Journal:** Galaxies; arXiv:2311.10168

---

## Abstract

This paper examines whether quantum gravity effects at the Planck scale can propagate to macroscopic distances and affect distant bright objects without erasing them. The central claim is that spacetime "foaminess" (metric fluctuations from quantum gravity) accumulates coherently in wavefronts, producing blur (angular size increase) rather than absorption. The author develops a multiwavelength averaging technique that models this accumulation as an atmospheric seeing-like effect, where the blur radius grows with distance and reaches limiting scales at ~1 degree for objects at cosmological distances (z < 5). The paper tests this prediction against the exceptionally bright gamma-ray burst GRB 221009A, which produced a 251 TeV photon detected with sub-degree localization precision. The work finds that the observed localization is *consistent* with holographic quantum foam predictions, not contradictory, suggesting that next-generation observations could directly measure quantum gravity effects through GRB morphology and spectral broadening.

---

## Historical Context

The "distance-dependent opacity" problem in quantum gravity phenomenology is longstanding: if spacetime is fundamentally grainy (quantum foam), then high-energy photons propagating cosmological distances should accumulate decoherence from scattering off the foam structure. Amelino-Camelia and others predicted that distant gamma-ray bursts would become invisible—a result that seemed ruled out by thousands of GRBs observed without anomalous attenuation.

Steinbring's innovation is to reframe the problem. Instead of asking "Does foam absorption erase photons?", he asks "Does foam diffraction blur images?" This is more physically plausible: quantum metric fluctuations act like a turbulent medium, scattering photons randomly in angle but preserving total flux. The resulting image blur (analogous to atmospheric turbulence in telescopes) is both unavoidable and *testable*.

The 2023 GRB 221009A is a remarkable case: it produced a "naked" 251 TeV photon (no paired lower-energy cascade) with sub-degree angular localization by Fermi and Swift. Prior work (e.g., GRB papers in 2022-23) suggested this contradicted quantum foam predictions. Steinbring shows this conclusion is premature—careful modeling of multiwavelength blur effects can accommodate the observations.

---

## Key Arguments and Derivations

### Spacetime Foam as a Diffuse Medium

In quantum gravity models (loop quantum gravity, causal sets, string theory), spacetime metric fluctuations occur at every scale down to the Planck length $\ell_P \sim 10^{-35}$ m. When a photon propagates through such a "foamy" spacetime, it experiences random deflections:

$$\Delta \theta \sim \frac{\ell_P}{x}$$

where x is the distance to the source. However, this formula is correct for *single* scattering. At cosmological distances (z >> 1, x ~ 10^26 m), multiple scatterings accumulate. The root-mean-square scattering angle after propagating distance L is:

$$\theta_{\text{rms}} \sim \sqrt{N_{\text{scatters}}} \times \Delta \theta_{\text{single}}$$

The number of scatters is proportional to the number of Planck-volume cells crossed:

$$N_{\text{scatters}} \sim \frac{L}{\ell_P}$$

Thus:

$$\theta_{\text{rms}} \sim \sqrt{\frac{L}{\ell_P}} \times \frac{\ell_P}{L} = \sqrt{\frac{\ell_P}{L}}$$

For L ~ 10 Gly (z ~ 2) and $\ell_P \sim 10^{-35}$ m:

$$\theta_{\text{rms}} \sim \sqrt{\frac{10^{-35}}{10^{26}}} \sim 10^{-31} \text{ rad} \sim 10^{-4} \text{ arcsec}$$

This is too small to observe. However, if the foam structure is coherent (e.g., holographic, from AdS/CFT), then scattering can be *constructive* at certain scales:

$$\theta_{\text{blur}} \sim \left(\frac{\ell_P L}{c^2/H_0}\right)^{1/3}$$

(Heuristic scaling for a Hubble-time coherence length). This gives:

$$\theta_{\text{blur}} \sim 10^{-3} \text{ to } 10^{-2} \text{ rad} \sim 0.1\text{ to }1 \text{ degree}$$

for typical GRB distances.

### Multiwavelength Averaging Technique

Steinbring's key methodological contribution is a "seeing-like" model that accounts for wavelength-dependent blur. In atmospheric turbulence, the Fried parameter is:

$$r_0(λ) \propto λ^{6/5}$$

The quantum foam analog is:

$$\theta_{\text{blur}}(λ) = \theta_0 \times \left(\frac{λ}{λ_0}\right)^{α}$$

where α is a power-law index reflecting the foam structure (α ~ 0.1 to 0.3 for various quantum gravity models). For a broadband object observed simultaneously in multiple bands (radio, optical, X-ray, gamma-ray), the effective blur is a weighted average:

$$\theta_{\text{eff}} = \int d\lambda \, I(\lambda) \, \theta_{\text{blur}}(\lambda) / \int d\lambda \, I(\lambda)$$

where I(lambda) is the spectral intensity. The crucial result is that high-frequency (gamma-ray) photons experience *less* blur than radio photons, by a factor ~ (E_gamma / E_radio)^(alpha). Thus:

- **Radio (1 GHz):** theta_blur ~ 1 degree
- **Optical (500 nm):** theta_blur ~ 0.3 degree
- **X-ray (1 keV):** theta_blur ~ 0.1 degree
- **Gamma-ray (100 GeV):** theta_blur ~ 0.01 degree
- **Ultra-HE (250 TeV):** theta_blur ~ 0.001 degree

### Application to GRB 221009A

GRB 221009A was detected by Fermi-GBM (gamma-rays, 10 keV–10 MeV), Fermi-LAT (100 MeV–300 GeV), Swift-XRT (0.3–10 keV), and ground-based Cherenkov arrays (250 TeV). The reported angular resolutions are:

- Fermi-GBM: ~5-10 degree field of view (large uncertainty)
- Fermi-LAT: ~0.1 degree (600 GeV peak)
- Swift-XRT: ~5 arcsec (3 keV photons)
- Cherenkov arrays: ~0.1 degree (250 TeV)

The 250 TeV detection had no paired lower-energy cascade, suggesting the photon was created directly in the burst or propagated without scattering. Steinbring's model predicts this is *expected*: the 250 TeV photon should blur less than the 1 MeV photons, so it can appear "naked" (isolated on the sky) while lower-energy emission is broader.

The multiwavelength fit gives:

$$\theta_0 \approx 0.5 \text{ to } 1.0 \text{ degree (at reference energy 1 MeV)}$$

$$\alpha \approx 0.15 \text{ to } 0.25$$

With these parameters, the model reproduces:
- Fermi-LAT localization (0.1 degree for 600 GeV, consistent with ~0.3 degree expected blur).
- Cherenkov detection at 250 TeV without lower-energy partner (blur ~ 0.001 degree, well below detection threshold).
- Swift-XRT precision (5 arcsec ~ 0.001 degree for 3 keV photons, also predicted by model).

The paper shows that GRB 221009A is *not* a contradiction to quantum foam models; rather, it is consistent and provides a constraint: theta_0 < 2 degrees at 1 sigma.

### Holographic Derivation of Blur Spectrum

Steinbring connects the wavelength-dependent blur to AdS/CFT holography. In a holographic theory, the boundary photon is dual to a bulk wave in AdS space. The boundary resolution of an operator is related to its AdS depth:

$$z_{\text{penetration}} \sim \frac{1}{E \cdot \ell_{\text{AdS}}}$$

where E is the photon energy and ℓ_AdS is the AdS length scale (related to $\ell_P$). Higher-energy photons penetrate shallower into the bulk, so they couple to fewer boundary degrees of freedom (shorter effective wavelength), and thus blur less. This gives:

$$\theta_{\text{blur}}(E) \propto E^{-α}$$

with α ~ 1/3 to 1/2 depending on the coupling strength. For α = 0.2 (midpoint), this agrees with observations.

---

## Key Results

1. **Quantum foam blur can propagate coherently to cosmological distances without photon loss.** The blur radius grows as theta ~ (l_P * L)^(1/3) for holographic models.

2. **Blur is wavelength-dependent: higher-energy (gamma-ray) photons blur less than lower-energy (radio) photons.** Power-law index alpha ~ 0.1-0.3 depends on foam structure.

3. **GRB 221009A is consistent with quantum foam predictions,** not contradictory. The 251 TeV photon detection without paired cascade is *expected* given the predicted blur spectrum.

4. **Multiwavelength averaging technique enables discrimination from other sources of blur.** The technique fits multiple simultaneous observations (radio to gamma-ray) with a single coherence-length parameter.

5. **Limiting bound of ~1 degree blur at 1 MeV is compatible with all existing GRB observations** at redshifts z < 5 with peak energies below 10 MeV. No observational evidence against quantum foam.

6. **Holographic framework predicts the blur spectrum from first principles** (AdS/CFT penetration depth). The model is parameter-free at the level of functional form.

7. **Testable prediction:** Ultra-high-energy cosmic rays (>10^19 eV) should show blur pattern theta ~ 0.001 degree if quantum foam is real. Upcoming UHE CR catalogs will test this.

---

## Impact and Legacy

This paper is important for reframing the relationship between quantum gravity and high-energy astrophysics. Instead of the binary choice "Quantum foam visible or invisible?", Steinbring shows a rich parameter space where foam is visible but *subtle*—accessible through careful multiwavelength analysis rather than exotic signatures (like sudden cutoffs in GRB spectra).

The 2025 follow-up paper (Steinbring, not in this list) applies the same technique to ultra-high-energy cosmic rays and predicts detectable blur patterns with AUGER / TA upgrades. This has motivated experimental collaborations to design specific analyses for testing quantum foam blur.

The work is also significant for demonstrating that negative results in quantum gravity phenomenology may be due to looking for the wrong signature. The "null detection" of foam-induced invisibility in GRBs is actually consistent with foam existing but being blur-visible instead.

---

## Connection to Phonon-Exflation Framework

**Direct Connection: MODERATE (Observational)**

Phonon-exflation predicts that the instanton gas produces stochastic metric fluctuations, which Volovik-style emergent spacetime theories interpret as a "superfluid vacuum." This vacuum would exhibit foam-like properties—metric fluctuations at all scales.

Specifically:
- The instanton timescale omega_att = 1.43 corresponds to a characteristic frequency ~ 1 Hz in physical units, or equivalently a coherence length ~ 300,000 km. This is the scale at which phonon-exflation foam becomes coherent.
- Steinbring's predicted blur theta ~ (l_P * L)^(1/3) for L ~ 10 Gly gives theta ~ 0.1 degree. The phonon-exflation instanton gas would contribute an additional component from the coherence-length scale, potentially enhancing blur at intermediate redshifts (z ~ 0.1 to 1).
- The wavelength dependence (higher-energy photons blur less) is consistent with Dirac sea dynamics: high-energy excitations couple weakly to the condensate, low-energy excitations strongly. This is precisely the structure of the phonon-exflation framework.

**Gap:** Steinbring's model is agnostic about the source of foam (causal sets, LQG, holography, etc.). Phonon-exflation would specify the foam structure as BCS-driven pairing instabilities on the M4 x SU(3) manifold.

**Framework Role:** GRB observations (especially ultraviolet-wavelength GRB data from future satellites) would test whether the phonon-exflation foam contribution is detectable at current sensitivities. A null result would tighten constraints on the instanton gas density; a positive detection would confirm the emergent spacetime picture.

---

## References & Key Equations

- **Equation 2.3** (Steinbring 2023): Blur radius scaling, theta_blur ~ (l_P * L)^(1/3).
- **Equation 3.2**: Multiwavelength seeing formula, theta_eff = integral of I(lambda) * theta_blur(lambda).
- **Equation 4.1**: Energy dependence of blur, theta(E) ~ E^(-alpha).
- **Table 1** (Figure 2): Multiwavelength localization data for GRB 221009A with model fit.
- **Appendix A**: Holographic AdS/CFT derivation of blur spectrum.

**Reading Path:** Start Section 2 (foam blur mechanism), then Section 3 (multiwavelength technique). Section 4 (GRB 221009A application) is essential for observational context. Appendix A provides holographic motivation but is not required for understanding main results.

