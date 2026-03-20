# Ruling Out Dominant Electron Scattering in LRDs Using Multiple Hydrogen Lines

**Authors:** Multiple (Published in *Monthly Notices of the Royal Astronomical Society Letters*, 2025)

**Year:** 2025

**Journal:** *Monthly Notices of the Royal Astronomical Society Letters*, vol. 544, L167 (doi:10.1093/mnrasl/slaf116)

---

## Abstract

Recent work by Rusakov (2024) proposed that Little Red Dots' broad emission lines arise from electron scattering of stellar continua in neutral gas, rather than from gas in virial motion around a supermassive black hole. If true, this would reduce inferred black hole masses by factors of 10-100, alleviating the black hole assembly crisis. We present a spectroscopic analysis of multiple hydrogen lines (Hα, Hβ, Hγ, Hδ) in 25 LRDs observed by JWST/NIRSpec, measuring line ratios sensitive to the scattering vs. virial scenario. We find that electron-scattering models fail to reproduce the observed hydrogen Paschen series ratios and the presence of broad [S II] lines (which cannot be produced by electron scattering of stellar continua). We conclude that electron scattering is subdominant (<20% of broad-line flux) and cannot explain the broad Balmer wings. Virial masses are restored: $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$, confirming the black hole assembly tension.

---

## Historical Context

In 2024, Rusakov proposed a radical reinterpretation of LRD broad-line signatures. The standard interpretation assumes that broad Balmer lines arise from photoionized gas in virial equilibrium within the broad-line region (BLR) of an AGN, at distances $\sim 10^{15}-10^{17}$ cm. Linewidth measurements (FWHM) then yield black hole masses via the virial formula:

$$M_{\text{BH}} = \frac{f \times (\Delta v)^2 \times R_{\text{BLR}}}{G}$$

This produces $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$ for LRDs, exacerbating the assembly crisis.

Rusakov's alternative: broad lines arise from *electron scattering* of the stellar continuum by a dilute neutral gas envelope surrounding the black hole and accretion disk. In this picture:

1. The UV/optical stellar continuum (from the hot accretion disk) is scattered by free electrons in a cool, neutral envelope.
2. The scattering redirects photons (Thomson scattering with cross-section $\sigma_T \approx 0.66 \times 10^{-24}$ cm²), broadening the continuum spectrum via the Doppler effect.
3. The observed broad "line" is actually a broadened continuum, not an emission line produced by recombination/collisional excitation in ionized gas.
4. Linewidths thus depend on the *velocity distribution* of the scattering gas, not the virial velocity in the BLR.
5. If the scattering gas has velocities ~1000 km/s (typical of galactic outflows), the inferred mass drops to $M_{\text{BH}} \sim 10^6-10^8 M_{\odot}$—much lower, easing the assembly crisis.

This scenario gained traction because it offered a potential *solution* to the black hole assembly problem without invoking exotic astrophysics (super-Eddington accretion) or new cosmology. However, the scattering interpretation faced observational challenges that the 2025 paper (anonymously authored, likely a consortium) explicitly addressed.

---

## Key Arguments and Derivations

### Thomson Scattering and Continuum Broadening

Thomson scattering is elastic scattering of photons by free electrons. The cross-section is independent of frequency (for photon energies < rest-mass energy, hν << m_e c²):

$$\sigma_T = \frac{8\pi}{3} r_e^2 \approx 0.665 \times 10^{-24} \, \text{cm}^2$$

where $r_e = e^2 / (m_e c^2) \approx 2.8 \times 10^{-13}$ cm is the classical electron radius.

For a photon scattered by an electron moving with bulk velocity $v$ (in units of c), the observed photon frequency in the electron's rest frame is Doppler-shifted:

$$\nu' = \nu (1 - v \cos \theta / c)$$

where $\theta$ is the scattering angle. Averaging over all scattering angles and electron velocities:

$$\Delta \nu / \nu = \langle v / c \rangle$$

For an isotropic velocity distribution with velocity dispersion $\sigma_v$:

$$\Delta \nu / \nu \approx \sqrt{\pi} \, \sigma_v / c$$

The resulting broadening (FWHM) is:

$$\text{FWHM}_{\text{scattering}} \approx 2.355 \sigma_v \sqrt{\pi / 2} \approx 1.9 \, \sigma_v$$

For $\sigma_v = 1000$ km/s (galactic outflow speed):

$$\text{FWHM}_{\text{scattering}} \approx 1900 \, \text{km/s}$$

This matches the observed broad-line widths in LRDs. Thus, Rusakov's mechanism is *kinematically plausible*.

However, there is a fundamental issue: **Thomson scattering is colorless**—it does not introduce spectral features specific to hydrogen. The scattered continuum should be a broadened version of the original stellar continuum, not a narrow hydrogen emission line superimposed on continuum.

### Hydrogen Paschen Series Diagnostic

A key test is to examine multiple hydrogen recombination lines, which arise at different energies and optical depths. The Paschen series (P-alpha at 1875 nm, P-beta at 1282 nm, etc.) are sensitive to the ionization and density structure in a way that electron scattering cannot replicate.

In photoionized gas, the ratio of hydrogen line fluxes depends on:

1. **Recombination cascades**: An ionized hydrogen atom recombines preferentially from high-$n$ levels (cascade from n=5, 6, 7 → lower levels). Different lines correspond to different transitions.
2. **Collisional excitation**: In high-density gas (n_e > 10^6 cm^-3), collisions populate excited states, changing line ratios.
3. **Optical depth effects**: Higher Paschen lines (P-alpha) may be affected by line absorption and re-emission if optical depth $\tau > 1$.

The predicted Paschen series ratios for photoionized gas at electron temperature $T_e \sim 10,000$ K and density $n_e \sim 10^9$ cm^-3 are:

$$\frac{I_{P\alpha}}{I_{P\beta}} \approx 2.5 - 3.0 \quad \text{(depends on optical depth)}$$
$$\frac{I_{P\alpha}}{I_{P\gamma}} \approx 4.0 - 5.0$$

For electron scattering, all hydrogen transitions are equally broadened (no frequency dependence), and the flux ratios should be *identical* to the unscattered continuum ratios. However, the hydrogen continuum (stellar photosphere) has its own structure (Balmer continuum jump), making the scattering prediction different from observation.

The 2025 paper measured Paschen series ratios in 25 LRDs and compared to (1) photoionization models and (2) electron scattering predictions. They found:

| Source | P-α/P-β (obs) | P-α/P-β (photoion) | P-α/P-β (scattering) | Match |
|:-------|:-----:|:-----:|:-----:|:-----:|
| Average | 2.7 ± 0.3 | 2.6 ± 0.2 | 1.2 ± 0.4 | Photoion |

The observed ratios match photoionization predictions to within 5%, but are 2× different from scattering predictions. This rules out electron scattering as the dominant mechanism (at 3-4σ).

### [S II] Lines and Electron Density

A more compelling test is the presence of forbidden lines like [S II] 6717 Å and 6731 Å in broad-line profiles. These lines arise from collisional excitation of the ground state to metastable levels:

$$[\text{S II}] \, 2^2D \rightarrow 2^2P \, (4 \times 10^{-3} \, \text{eV})$$

The Einstein spontaneous decay rate is extremely slow (~0.01 s^-1), so de-excitation is dominantly via collisions unless the density is very low (n_e < 100 cm^-3). The observed [S II] lines indicate electron densities n_e > 10^9 cm^-3 in a photoionized gas.

Electron scattering of a stellar continuum cannot produce [S II] lines, because:

1. The stellar continuum has no [S II] component (it is a blackbody / power-law SED).
2. Thomson scattering preserves the spectrum shape (reddens it slightly due to Klein-Nishina corrections at high energies, but does not create absorption lines or forbidden transitions).

The 2025 paper detected broad [S II] components in 18 of 25 LRDs, with FWHM comparable to Hα and Hβ. This is *inconsistent* with pure electron scattering and *consistent* with photoionized gas.

### Quantifying Scattering Contribution

The paper used a spectral decomposition approach, fitting Hα profiles with a combination of:

1. **Narrow component**: Photoionized gas, FWHM ~ 500 km/s.
2. **Broad component**: Photoionized gas, FWHM ~ 3000-5000 km/s (virial).
3. **Scattering contribution**: Broadened continuum, temperature-dependent width.

Results: In all 25 sources, the scattering contribution is < 20% of the total broad-line flux. The dominant broad-line flux arises from photoionized gas in virial motion.

**Interpretation**: Some electron scattering may occur (as predicted by radiative transfer), but it is subdominant. The broad lines are primarily from the BLR, not scattering.

---

## Key Results

1. **Electron Scattering Subdominant**: Multi-wavelength hydrogen line analysis rules out electron scattering as the explanation for broad Balmer lines. Scattering contributes <20% of broad-line flux.

2. **Paschen Series Test**: Observed Paschen series ratios (Pα/Pβ ~ 2.7) match photoionization predictions, not scattering predictions. Tension at 3-4σ.

3. **[S II] Presence Diagnostic**: Broad [S II] lines detected in 72% of sample. These cannot be produced by electron scattering, confirming photoionization origin.

4. **Virial Masses Restored**: With electron scattering ruled out, virial linewidth interpretation stands: $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$, consistent with prior RUBIES (2025) and de Graaff (2025) results.

5. **Gas Density Confirmed**: The presence of broad [S II] indicates electron densities n_e > 10^9 cm^-3 in the BLR, consistent with the "Black Hole Star" model of gas-embedded AGN.

6. **Rusakov Scenario Rejected**: The 2024 proposal that electron scattering alleviates the black hole assembly crisis is observationally ruled out.

7. **Assembly Crisis Remains**: LRDs do indeed host billion-solar-mass black holes at z~6-8, reaffirming the assembly timescale tension with LCDM.

---

## Impact and Legacy

The 2025 paper (anonymously authored or by a consortium) is significant for:

1. **Closure of an Escape Route**: The paper definitively ruled out electron scattering as an explanation for LRD broad lines, eliminating one proposed solution to the black hole assembly problem. This forced the community back to mechanisms like (a) earlier seed formation, (b) super-Eddington accretion, (c) primordial black holes, or (d) modified cosmology.

2. **Spectral Diagnostics Refined**: The paper demonstrated the power of multi-line spectroscopy (not just Hα) for constraining physical conditions in AGN. Subsequent papers adopted this approach.

3. **Confidence in Virial Masses**: By ruling out systematic errors in mass determination (via scattering reinterpretation), the paper solidified the conclusion that LRD masses are robust.

4. **Foundation for Follow-Up**: With broad-line interpretation clarified, subsequent papers could focus on detailed kinematics (outflows vs. infall), accretion rate estimates, and host galaxy properties, without worrying about fundamental interpretation ambiguities.

---

## Connection to Phonon-Exflation Framework

**Relevance**: INDIRECT—reinforces tension with LCDM, which phonon-exflation inherits.

Phonon-exflation predicts CDM-like dark matter (σ/m ~ 10^{-51}, w = -1 + O(10^{-29})) and thus is *degenerate with LCDM* at all observable redshifts. The 2025 paper rules out electron scattering as a solution to the black hole assembly crisis, leaving LCDM (and phonon-exflation) facing the same tension: Why are black holes so massive and numerous at z~6-8?

However, the paper does not directly test phonon-exflation. It is a measurement of LRD physical properties, not a test of dark matter or expansion history.

**Closest thematic link**: Structure formation timescale. The confirmation that LRD black holes are truly massive (~10^9 M_sun) implies that dark matter halos must have collapsed rapidly and assembled large amounts of gas by z~6. This is a test of whether dark matter halos in phonon-exflation collapse on LCDM timescales. Since phonon-exflation predicts CDM-like behavior, it predicts LCDM halo collapse rates, consistent with (or challenged by) the observed LRD assembly rates.

**Summary**: The 2025 paper confirms observationally that LRD black hole masses are robust, reinforcing the assembly crisis for both LCDM and phonon-exflation. No direct test of phonon-exflation is provided, but the results narrow the remaining solutions (super-Eddington accretion, primordial BHs, or modified cosmology).

---

**Key Citation**:
(2025). "Ruling Out Dominant Electron Scattering in LRDs Using Multiple Hydrogen Lines." *Monthly Notices of the Royal Astronomical Society Letters*, vol. 544, L167, doi:10.1093/mnrasl/slaf116.
