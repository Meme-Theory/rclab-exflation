# An Upper Limit of 10^6 Solar Masses in Dust from ALMA Observations of 60 Little Red Dots

**Author(s):** Chen, Y., et al.
**Year:** 2025
**Journal:** Astrophysical Journal 957, 123 (2025)
**DOI/arXiv:** arXiv:2505.18873

---

## Abstract

Little Red Dots (LRDs) are compact, red sources at high redshift that have been proposed to be dust-reddened AGN. To test whether dust is the dominant source of their red color, we conducted 1.3 mm continuum observations of 60 LRDs using ALMA. No individual sources were detected, and stacking analysis produced null results. We derive a 3-sigma upper limit of 10^6 M_sun on the dust mass in the LRD population, corresponding to dust luminosity $L_{\rm dust} < 10^{11} L_\odot$. This constraint is approximately 10x deeper than previous millimeter/submillimeter measurements. The dust mass limit implies either (1) LRDs contain modest dust reservoirs with extinction A_V ~ 2-4 mag, inconsistent with pure dust-reddening scenarios, or (2) the red optical colors arise from mechanisms other than dust, such as dense ionized gas providing opacity through electron scattering and free-free absorption. We discuss implications for LRD composition and suggest that gas opacity, not dust, is the primary source of reddening in the majority of LRDs.

---

## Historical Context

The discovery of LRDs raised an immediate observational question: what causes their distinctive red color? Three hypotheses were advanced:

1. **Dust reddening**: The sources are reddened by substantial dust masses (>10^7 M_sun), making them dusty AGN or dust-obscured starbursts. This scenario predicts strong millimeter/submillimeter emission due to thermal dust radiation.

2. **Gas opacity**: The red color arises from free-free absorption and electron scattering in dense, ionized gas surrounding an AGN. This scenario predicts minimal dust mass and weak millimeter flux.

3. **Balmer break**: The sources have extremely steep Balmer discontinuities arising from stellar mass functions or very young stellar populations, creating an artificial "reddening" in optical filters without requiring significant dust or gas opacity.

Previous infrared observations with JWST/MIRI provided some constraints. The SEDs of LRDs show a distinct near-infrared peak around 3-5 microns (rest frame), characteristic of hot dust emission from AGN tori. However, the absolute infrared luminosity was only modestly elevated compared to optical, suggesting that dust does not completely dominate the SED. The question remained: are LRDs dusty AGN with masses near the gas-opacity limit, or something fundamentally different?

ALMA observations provide a direct test. At 1.3 mm, we probe wavelengths well into the Rayleigh-Jeans tail of dust thermal emission, where the flux is directly proportional to dust mass (for optically-thin emission):

$$F_\nu \propto M_{\rm dust} \, T_{\rm dust} \, \kappa_\nu$$

High sensitivity at millimeter wavelengths can detect even modest dust masses (>10^5 M_sun at z~5-7).

---

## Key Arguments and Derivations

### ALMA Sensitivity and Detection Threshold

ALMA Band 3 (3.2 mm) observations achieve typical RMS noise of sigma_rms ~ 20-30 microJy after integration. For a 1.3 mm source at z~6, assuming dust temperature T_dust ~ 60 K (typical for AGN-heated dust) and emissivity beta ~ 1.8 (close to the Rayleigh-Jeans limit):

$$F_\nu = \frac{M_{\rm dust}}{4 \pi d_L^2} \kappa_0 \left(\frac{\lambda}{1 \text{ mm}}\right)^\beta \, B_\nu(T_{\rm dust})$$

where kappa_0 ~ 2 cm^2 g^-1 is the dust opacity per gram at 1 mm, d_L is the luminosity distance, and B_nu is the Planck function.

For M_dust = 10^7 M_sun at z~6, T_dust = 60 K:

$$F_{1.3 \text{ mm}} \approx 50-100 \, \mu Jy$$

For M_dust = 10^6 M_sun, the flux drops to 5-10 microJy, approaching the ALMA sensitivity limit. The authors' observations reach sigma_rms ~ 22 microJy, allowing detection of dust masses above ~2x10^6 M_sun (at 3-sigma significance).

### Non-detection and Stacking Analysis

Of 60 LRDs observed:
- **0 sources detected** at >3 sigma above the RMS noise.
- **Stacking of all 60 sources** in visibility space: The median flux is consistent with zero, with 1-sigma scatter comparable to measurement noise.

The stacking limit is computed as:

$$F_{\rm stack, 3\sigma} = 3 \sigma_{\rm rms} / \sqrt{N}$$

With sigma_rms ~ 22 microJy and N ~ 60 sources, the 3-sigma stacking limit is:

$$F_{\rm stack, 3\sigma} \approx 2.7 \, \mu Jy$$

Converting to dust mass via the relation above yields:

$$M_{\rm dust, 3\sigma} \approx 1.0 \times 10^6 M_\odot$$

### Implications for Dust-Reddening Scenario

If LRDs were dust-reddened galaxies with typical extinction A_V ~ 5-10 mag (as sometimes assumed for dusty starbursts), the dust column density would be:

$$N_{\rm dust} = \frac{A_V}{1.086 \kappa_V} \approx 10^{23}-10^{24} \, \text{cm}^{-2}$$

For a source of size R ~ 100 pc, this corresponds to dust mass:

$$M_{\rm dust} \approx N_{\rm dust} \, m_H \, \pi R^2 \approx 10^8 M_\odot$$

The observed upper limit of 10^6 M_sun is two orders of magnitude below this estimate, ruling out high-extinction dust-reddening scenarios.

However, a dust-reddening scenario with moderate extinction (A_V ~ 2-4 mag) is not completely ruled out. Such extinction would require dust mass ~ 10^6-10^7 M_sun, at the edge of or just above the observational limit. The authors argue that this scenario requires fine-tuning: the dust must be distributed in a thin, compact shell to produce the observed optical colors while remaining undetected at millimeter wavelengths.

### Alternative: Dense Ionized Gas Opacity

If instead the red color arises from electron scattering and free-free absorption in dense ionized gas (as proposed in the Dunne et al. paper), the expected millimeter flux is negligible. The gas is ionized, so dust (which requires neutral or molecular environments to survive) would be destroyed or minimally present.

The optical extinction from gas opacity arises from:

$$A_{\rm opt} = \int \sigma_{\rm ff}(h\nu) \, n_e \, ds$$

where sigma_ff is the free-free absorption cross-section and n_e is the electron density. For typical ionized gas (n_e ~ 10^9 cm^-3, T_e ~ 10^4 K) and path length L ~ 1000 AU, extinction A_V ~ 1-3 mag is easily achieved without invoking dust.

In this scenario, millimeter observations detect minimal dust because the gas is hot and ionized. Any dust present is confined to shielded neutral regions or destroyed by radiation, and the total dust mass is <10^6 M_sun.

---

## Key Results

1. **Zero ALMA detections**: 60 LRDs observed at 1.3 mm; 0 individual sources detected above 3-sigma (RMS noise ~ 22 microJy per source).

2. **Stacking limit**: Combined measurement of all 60 sources yields 3-sigma upper limit F_stack = 2.7 microJy.

3. **Dust mass limit**: Translates to M_dust < 1.0 x 10^6 M_sun (3-sigma) for typical AGN dust temperatures (~60 K).

4. **Dust luminosity limit**: L_dust < 10^11 L_sun; approximately 10x deeper than previous published limits.

5. **Dust-reddening inconsistency**: Pure dust-reddening with A_V ~ 5-10 (high extinction) ruled out. Moderate dust with A_V ~ 2-4 remains possible but requires fine-tuning.

6. **Gas opacity favored**: Results consistent with gas-opacity origin of red colors (electron scattering and free-free absorption in dense ionized gas).

7. **Composite picture**: Some LRDs may host both modest dust and dense gas; dust produces near-IR bump seen in JWST/MIRI, while gas produces optical/UV opacity and broad-line broadening.

---

## Impact and Legacy

This paper provides crucial constraints on the composition of LRDs. Prior to these ALMA observations, the dust content was essentially unconstrained, leaving room for multiple interpretations. The tight upper limit rules out high-dust-mass scenarios and pivots the field toward gas-based opacity explanations.

The work has catalyzed a shift in spectral modeling of LRDs. SED-fitting codes now incorporate both dust and gas-absorption components, rather than treating dust as the sole source of reddening. The improvement in fit quality and reduced tension in model parameters (particularly in derived AGN/starburst contribution ratios) indicates that the gas-opacity model is more accurate.

The findings also have implications for understanding the interstellar medium in high-redshift compact objects. If LRDs are indeed dominated by gas opacity rather than dust, it suggests that the early-universe ISM may be more highly ionized than at lower redshifts, possibly due to intense radiation from nearby sources or the absence of neutral-phase structure.

Future improvements in ALMA sensitivity and higher-frequency observations (millimeter and sub-millimeter) will enable detections of modest dust masses in individual LRDs, refining the composite dust+gas picture.

---

## Connection to Phonon-Exflation Framework

**Relevance: Very Low (ISM and dust physics disconnected from NCG mechanisms).**

The dust and gas composition of high-redshift AGN is determined by astrophysical processes (star formation, ISM evolution, radiation feedback) that operate largely independently of fundamental physics such as noncommutative geometry. The phonon-exflation framework focuses on particle mass generation and gauge coupling unification through spectral geometry, not on dust/gas properties.

However, an indirect connection may exist through cosmic dust production. In a phonon-exflation cosmology with a modified expansion history compared to LCDM, the rate of stellar nucleosynthesis and metal production would differ, affecting the abundance of dust-producing elements (C, Si, Fe) at early cosmic times. If phonon-exflation predicts either accelerated or decelerated dust production at z~5-11, this would alter the expected dust mass distribution in LRD populations.

The observation that LRD dust masses are low (< 10^6 M_sun) and insufficient to explain the red colors through dust opacity alone provides a consistency check on early-universe metal enrichment. Any complete phonon-exflation cosmological model must predict metal abundances consistent with the LRD dust limits presented here.

---
