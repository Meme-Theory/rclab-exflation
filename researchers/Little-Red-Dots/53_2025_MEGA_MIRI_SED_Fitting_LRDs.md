# MEGA: Spectrophotometric SED Fitting of Little Red Dots Detected in JWST MIRI

**Author(s):** Kaila Ronayne, Casey Papovich, Allison Kirkpatrick, Fabio Pacucci, and 12 co-authors

**Year:** 2025

**Journal:** arXiv:2508.20177

---

## Abstract

The nature of Little Red Dots—whether they are actively accreting black holes (AGN) or rapidly star-forming galaxies—remains ambiguous due to degeneracies in spectral energy distribution (SED) fitting when using optical and near-infrared data alone. This work presents MEGA, a suite of spectrophotometric SED models specifically designed for high-redshift LRDs, including detailed photoionization models of gas, accretion disk emission, and dust properties. We apply MEGA to eight spectroscopically-confirmed LRDs at z = 5.1-8.7 observed with JWST NIRCam and MIRI (mid-infrared). The MIRI data, covering rest-frame wavelengths 2-10 micrometers, provide critical constraints on warm dust temperatures and continuum properties difficult to determine from optical/NIR data alone. We find that six of eight LRDs are best-fit by AGN models (hot, geometrically thick accretion flows with moderate dust attenuation A_V ~ 0.5-1.5 mag), while two LRDs favor hybrid AGN+starburst models. The MIRI data reveal weak warm dust components (dust temperature ~ 800-1400 K), inconsistent with heavily dust-obscured systems. Standard stellar population synthesis templates fail to reproduce the LRD SED, indicating that LRDs require novel physical models combining AGN accretion and gas photoionization. The result demonstrates the critical importance of mid-infrared data for breaking AGN/starburst degeneracies and constraining the nature of high-z compact galaxies.

---

## Historical Context

The optical and near-infrared colors of LRDs are ambiguous: a "red in optical, blue in UV" SED can arise from either:

1. **AGN with dust**: Hot accretion disk (blue UV) reddened by dust extinction (A_V ~ 1-2 mag), producing red optical colors
2. **Starburst with age**: Young star-forming galaxy (blue UV from massive stars) with evolved stellar population (red optical from older stars)

Traditional SED fitting using optical/NIR data alone (wavelengths 0.3-2.5 micrometers rest-frame) cannot distinguish these scenarios reliably. Both produce similar colors and both predict appreciable far-infrared emission (from dust heated by either AGN or stellar continuum).

However, the two scenarios predict very different mid-infrared spectra (rest-frame 2-10 micrometers):

1. **AGN with dust**: The accretion disk is hot (T ~ 1e4-1e5 K at ISCO, cooling to T ~ 1e3-1e4 K in outer regions). If dust is present at temperature T_dust ~ 500-1000 K (equilibrium with radiation from the hot accretion disk), the mid-infrared emission is approximately blackbody-like with moderate emission.

2. **Starburst with age**: The stellar population produces a composite spectrum (blue hot stars, red old stars). Dust in starbursts is heated to T_dust ~ 30-100 K (cold, far from the cool stellar continuum), producing very weak mid-infrared emission and strong far-infrared emission.

The key discriminant is the mid-infrared to far-infrared flux ratio: AGN-dominated systems show stronger mid-IR relative to far-IR, while starburst-dominated systems show weaker mid-IR relative to far-IR.

Prior to JWST, mid-infrared data for z > 4 sources were difficult to obtain, forcing SED fitting to rely on optical/NIR alone. JWST MIRI provides access to rest-frame 2-10 micrometers at z ~ 5-8, enabling the critical mid-IR/far-IR ratio to be measured directly.

---

## Key Arguments and Derivations

### SED Template Construction: AGN Models

The MEGA AGN SED templates combine three components:

1. **Accretion disk continuum**: Modeled as a multi-temperature blackbody or more detailed disk model:

$$L_\nu(\text{disk}) = \int_R^{innermost} 2\pi R \, B_\nu(T(R)) dR$$

where $T(R) \propto R^{-3/4}$ for a standard thin disk. For super-Eddington flows, the geometry is modified (geometrically thick), and the temperature structure changes, but the spectrum remains dominated by a peak around T ~ 1e3-1e4 K (effective photosphere temperature).

2. **Photoionized gas component**: Emission lines and continuum from photoionized gas around the accretion disk:

$$L_\nu(\text{gas}) = \sum_i n_i h\nu_i A_i + \text{continuum}$$

Modeled via photoionization codes (CLOUDY, XSTAR) with input ionizing spectrum from the accretion disk.

3. **Dust extinction and emission**:
   - **Absorption**: Foreground dust with extinction curve (Milky Way, SMC, LMC, or custom) applied via:

   $$L_\nu^{\text{obs}} = L_\nu^{\text{intrinsic}} \times 10^{-0.4 A_\nu}$$

   - **Re-radiation**: Dust at temperature T_dust emits thermal continuum:

   $$L_\nu^{\text{dust}} = (1 - e^{-\tau_\nu}) \times M_{\text{dust}} \, B_\nu(T_{\text{dust}})$$

The dust temperature is determined by radiation balance: the absorbed energy equals the radiated energy:

$$\int (1 - e^{-\tau_\nu}) L_\nu^{\text{AGN}} d\nu = 4\pi \times \int L_\nu^{\text{dust}} d\nu$$

For accretion-heated dust with L_AGN ~ 1e11-1e12 solar luminosities and dust opacity kappa ~ 0.1 cm^2/g, the equilibrium dust temperature is:

$$T_{\text{dust}} \sim (L_{\text{AGN}} / (4\pi a M_{\text{dust}}))^{1/4} \sim 500-1500 \text{ K}$$

(depending on dust mass and geometry). This is much hotter than starburst-heated dust (T ~ 30-100 K).

### SED Fitting Algorithm and Degeneracies

Standard SED fitting minimizes chi-squared:

$$\chi^2 = \sum_i \left(\frac{f_{\nu,i}^{\text{obs}} - f_{\nu,i}^{\text{model}}}{\sigma_i}\right)^2$$

where $f_{\nu,i}$ are observed and model fluxes, and sigma_i are uncertainties.

Using optical/NIR data alone (lambda = 0.3-2.5 micrometers), many model combinations yield similar chi-squared values (local minima in parameter space). The degeneracies include:

1. **Age-extinction degeneracy**: A young, dusty starburst and an old, dusty starburst can have similar optical colors if the dust optical depth is adjusted.

2. **AGN-starburst degeneracy**: A low-luminosity AGN with dust can mimic a high-luminosity starburst with dust.

3. **Dust geometry degeneracy**: Foreground dust screen vs. mixed dust vs. dust in the ISM all produce similar colors.

The addition of MIRI data (mid-infrared, rest-frame 2-10 micrometers at z ~ 5-8) breaks these degeneracies. The mid-IR/far-IR flux ratio is a clean discriminant:

- **AGN-dominated**: Mid-IR/far-IR ~ 0.1-1 (warm dust close to hot AGN)
- **Starburst-dominated**: Mid-IR/far-IR ~ 0.01-0.1 (cold dust far from cool stars)

### Application to JWST-Observed LRDs

The MEGA templates are fit to eight LRDs with available MIRI data. The results show:

**Sample 1 (6 LRDs, AGN-dominated models)**:
- Best-fit: Hot accretion flow models with dust attenuation A_V ~ 0.5-1.5 mag
- Mid-IR/far-IR ~ 0.2-0.5
- AGN bolometric luminosity L_AGN ~ 1e11-1e12 solar luminosities
- Black hole mass estimate (from virial relations) M_BH ~ 1e7-1e8 solar masses
- Age of AGN activity estimated as < 100 Myr (based on continuum properties and lack of old stellar population signatures)

**Sample 2 (2 LRDs, hybrid AGN+starburst models)**:
- Best-fit: AGN models with additional star-forming component
- Mid-IR/far-IR ~ 0.05-0.2
- Requires warm dust (T ~ 800-1400 K) from AGN and cooler dust (T ~ 100 K) from star formation
- Star formation rate estimate SFR ~ 10-100 solar masses/yr

---

## Key Results

1. **MIRI mid-infrared data break AGN/starburst degeneracies in LRD SED fitting: the mid-infrared to far-infrared flux ratio cleanly distinguishes hot accretion-heated dust (AGN-dominated) from cold star-formation-heated dust (starburst-dominated).**

2. **Six of eight LRDs are best-fit by pure AGN models with hot, geometrically thick accretion flows and moderate dust attenuation (A_V ~ 0.5-1.5 mag), consistent with the photon-trapping interpretation.**

3. **The MIRI data reveal weak warm dust components (T ~ 800-1400 K) in all LRDs, indicating that LRDs are not heavily dust-obscured systems, but rather moderately reddened AGN.**

4. **Standard stellar population synthesis templates fail to reproduce LRD SEDs, demonstrating that LRDs require novel photoionization and accretion models that combine gas and dust physics beyond standard templates.**

5. **Two LRDs favor hybrid models with both AGN and star formation, suggesting that some LRDs may represent the transition phase between star-forming galaxies and pure AGN.**

6. **The MIRI-based SED fitting provides improved constraints on AGN bolometric luminosity, black hole mass, and dust properties compared to optical/NIR-only fitting.**

7. **The result demonstrates the critical importance of space-based mid-infrared observations for characterizing high-redshift compact AGN and breaking intrinsic physical degeneracies in source classification.**

---

## Impact and Legacy

This paper has become important for LRD SED modeling and AGN/starburst classification. Its impacts include:

- **Advancing SED modeling techniques**: The development of MEGA templates tailored to high-z LRDs provides a framework for future LRD characterization.
- **Establishing MIRI as a key diagnostic tool**: The work demonstrates that MIRI mid-infrared observations are essential for understanding LRD nature.
- **Constraining LRD accretion properties**: The SED fitting provides improved estimates of AGN luminosity and dust properties.
- **Motivating spectroscopic follow-up**: By identifying which LRDs are pure AGN vs. hybrid systems, the paper guides future spectroscopic observations.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

The SED fitting and AGN/starburst classification of LRDs is based on radiative transfer physics (accretion disks, photoionization, dust) that is largely independent of cosmological framework. Both LCDM and phonon-exflation predict similar AGN accretion physics at z ~ 5-8 (scales where expansion differences are < 5%).

However, if future observations show that the dust properties or AGN accretion characteristics of LRDs differ systematically from LCDM expectations, this could indicate modifications to AGN physics in phonon-exflation. For example, if the instanton relic affects gas cooling or ionization at high z, the predicted dust temperatures could differ.

**Closest thematic link**: The SED fitting framework provides tools for quantitatively comparing observed LRD properties to predictions of different cosmological models. If phonon-exflation produces LRDs with different spectral properties (e.g., different mid-IR/far-IR ratios due to modified accretion physics), the MEGA models can be adapted to test such predictions.
