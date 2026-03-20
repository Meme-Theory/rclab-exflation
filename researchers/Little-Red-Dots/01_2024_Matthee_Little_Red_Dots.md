# Little Red Dots: An Abundant Population of Faint AGN at z~5 Revealed by the EIGER and FRESCO JWST Surveys

**Author(s):** Jorryt Matthee, Rohan P. Naidu, Gabriel Brammer, Andy Goulding, Jenny Greene, Ivo Labbe, Erica Nelson, and 21 others

**Year:** 2024

**Journal:** The Astrophysical Journal (originally arXiv:2306.05448, revised Feb 2024)

---

## Abstract

This seminal paper coins the term "Little Red Dots" (LRDs) and establishes them as an abundant population of compact, high-redshift AGN. Using deep JWST/NIRCam imaging and spectroscopy from the EIGER and FRESCO surveys, Matthee et al. identify and characterize a sample of objects displaying broad Hα emission lines at z~4-5.5 (corresponding to ~1-1.5 billion years after the Big Bang). The study demonstrates that LRDs represent a previously undetected AGN population with number densities approximately 100 times higher than UV-selected quasars of comparable brightness. The objects are characterized by compact morphologies (<500 pc), strong dust reddening (A_V ~ 1-2), and modest black hole masses (10^6-10^8 M_sun) accreting at near-Eddington rates. The discovery fundamentally challenges conventional understanding of early AGN demographics and raises critical questions about black hole formation pathways in the early universe.

---

## Historical Context

Prior to JWST, the census of high-redshift AGN relied primarily on ultraviolet (UV) selection techniques through surveys like SDSS (Sloan Digital Sky Survey) and later through X-ray and mid-infrared selections. However, these methods inherently bias against dusty, obscured AGN—particularly those in dust-enshrouded host galaxies. The early promise of JWST (launched December 2021, operational by mid-2022) was that its superior infrared sensitivity would reveal previously hidden AGN populations.

By 2023, initial JWST observations (from programs like CEERS, NIRSpec GTO, GLASS, and other early-release data) had hinted at unexpected populations of compact, red optical-infrared sources at z>4. Labbe et al. (2023) noted massive galaxy candidates that were surprisingly compact. However, it remained unclear whether these red sources were dusty star-forming galaxies, heavily obscured AGN, or something entirely new.

Matthee and collaborators, leading the EIGER (JWST/NIRCam program 1243) and FRESCO (JWST/NIRCam program 1895) surveys, conducted systematic spectroscopic follow-up of candidate red sources. Their key innovation was the use of JWST/NIRCam wide-field slitless spectroscopy (WFSS) via the grism mode to obtain low-resolution but sensitive spectroscopy across wide fields. This enabled simultaneous detection of redshifts and broad emission lines for large samples.

The coincidence of JWST's unprecedented infrared sensitivity, the availability of deep imaging from multiple programs, and strategic spectroscopic follow-up campaigns created the ideal conditions for this discovery. Matthee et al.'s work was first posted as arXiv:2306.05448 in June 2023 and published in ApJ in 2024, immediately sparking intense interest and follow-up across the community.

---

## Key Arguments and Derivations

### Photometric Selection and Discovery

The study begins with deep JWST/NIRCam imaging spanning multiple filters covering the rest-frame UV through near-infrared at z~5. The team targets specifically those sources displaying a distinctive spectral energy distribution (SED) characterized by:

- **Blue UV continuum**: Rest-frame FUV-NUV colors consistent with young stellar populations or AGN
- **Red optical colors**: Strong drop in flux between rest-frame optical and near-infrared, consistent with dust attenuation
- **Compact morphology**: JWST's superior angular resolution (diffraction-limited ~70-100 mas) reveals effective radii typically <300 pc

The "red dot" nickname emerges from their appearance in color-composite images where the optical is extremely faint while infrared channels are bright, rendering them as small, isolated red points.

### Spectroscopic Confirmation

NIRSpec prism spectroscopy reveals the diagnostic signature: **broad Balmer emission lines** (Hα, Hβ) with full-width at half-maximum (FWHM) values of 1200--3700 km/s. This breadth far exceeds that of typical star-forming regions (FWHM ~ 100-300 km/s) and is characteristic of virialized gas in broad-line regions (BLRs) around supermassive black holes.

The width-luminosity relationship for broad emission lines yields black hole mass estimates:

$$M_{BH} = \frac{f \cdot \Delta v^2 \cdot R_{BLR}}{G}$$

where Delta v ~ FWHM ~ 1500-3000 km/s, and the radius R_BLR can be derived from the emission line flux assuming a standard AGN geometry. For typical LRDs:

$$\log(M_{BH}/M_{\odot}) \approx 6.0 \text{ to } 8.0$$

These masses are surprisingly modest—one to two orders of magnitude lower than those inferred from earlier optical/UV spectroscopy of bright z>6 quasars (e.g., SDSS J1148+5251 with M_BH ~ 10^{10} M_sun).

### Number Density Calculation

The authors count LRD candidates in their spectroscopic survey (finalized sample of ~20 confirmed broad-line sources) and cross-reference against the survey volume and completeness. The comoving number density is estimated as:

$$n_{LRD} \sim 10^{-5} \, \text{cMpc}^{-3}$$

By contrast, the space density of UV-selected quasars of comparable bolometric luminosity at z~5 is:

$$n_{UV} \sim 10^{-6} \, \text{cMpc}^{-3}$$

Thus, **LRDs are roughly an order of magnitude more abundant** than UV-selected quasars of comparable luminosity. However, LRDs represent only a small fraction (<1%) of all star-forming galaxies at z~5.

### Obscuration and Dust Properties

Dust extinction is quantified by fitting the observed SED to models combining stellar populations and AGN contributions. The dust attenuation law is characterized by:

$$A_V \sim 1.6 \text{ to } 2.0 \, \text{mag}$$

This is higher than the Galactic extinction law (A_V ~ 0.3 mag per magnitude of color excess in Milky Way; E(B-V) ~ 0.1) and suggests local dust environments in the host galaxy or circumnuclear region. The presence of significant dust is crucial: without it, these AGN would appear as normal (blue) broad-line quasars in UV-selected surveys.

### Bolometric Luminosity Estimates

Given the observed infrared luminosity L_IR and accounting for absorption corrections:

$$L_{bol} = f(A_V) \cdot L_{obs}$$

where f(A_V) is a dust-correction factor (typically 10--100 depending on geometry and dust temperature). Typical LRD bolometric luminosities range:

$$L_{bol} \sim 10^{45} \text{ to } 10^{47} \, \text{erg/s}$$

Eddington-limit comparison: The Eddington luminosity for a black hole of mass M_BH is:

$$L_{Edd} = \frac{4 \pi G M_{BH} m_p c}{\sigma_T} \approx 1.3 \times 10^{46} \left(\frac{M_{BH}}{10^8 M_{\odot}}\right) \, \text{erg/s}$$

For a 10^7 M_sun BH, L_Edd ~ 1.3 x 10^{45} erg/s. Many LRDs have L_bol ~ L_Edd or slightly higher, suggesting near-Eddington or mildly super-Eddington accretion.

---

## Key Results

1. **Sample Definition**: A spectroscopically confirmed sample of ~20 broad-line AGN at z=4.2--5.5, distinguished by red rest-frame optical colors, blue rest-frame UV, and compact morphologies.

2. **Number Densities**: LRDs are ~10-100 times more abundant than UV-selected quasars at z~5, suggesting significant "hidden" AGN populations missed by traditional surveys.

3. **Black Hole Masses**: Central black holes have masses 10^6--10^8 M_sun, lower than those of bright high-z quasars but sufficient to power luminous AGN.

4. **Dust Extinction**: Typical A_V ~ 1.6--2.0 mag, indicating substantial dust in the nuclear regions or host galaxy. This dust explains why these objects were not detected in UV-selected surveys.

5. **Accretion Rates**: Near-Eddington to slightly super-Eddington (lambda_Edd ~ 1--5), characteristic of rapidly growing black holes.

6. **Fraction of z~5 Galaxies**: LRDs comprise <1% of all star-forming galaxies at z~5, yet dominate the faint AGN census.

---

## Impact and Legacy

The discovery of Little Red Dots has become a focal point of high-z astrophysics in the JWST era. Within months of publication, the LRD designation was adopted across dozens of follow-up studies. Immediate impacts include:

1. **Demographic Recount**: Realization that traditional AGN surveys (Chandra X-ray, ALMA far-infrared, SDSS/2dF spectroscopy) have systematically undercounted heavily obscured AGN at z>4.

2. **Black Hole Formation Challenge**: The abundance of 10^6--10^8 M_sun black holes at z~5 raises the question: how did such objects form so early? This directly motivates theoretical work on black hole seeds and rapid accretion.

3. **Reionization Reconnection**: While individually less luminous than bright quasars, LRDs' high number density means they could contribute significantly to the ultraviolet ionizing photon budget during the epoch of reionization (z~6--15).

4. **Observational Campaigns**: Sparked intensive follow-up with JWST/NIRSpec, ALMA, Chandra, and ground-based observatories to characterize LRD spectral properties, demographics, and X-ray constraints.

5. **Theoretical Modeling**: Motivated new theoretical frameworks attempting to explain rapid early black hole growth through direct collapse, accelerated accretion, or primordial black hole scenarios.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework posits that particles are phononic excitations of a compactified M4 x SU(3) spacetime, with cosmological expansion driven by internal geometry rather than a scalar field. Little Red Dots provide two potentially important connections:

**Early Universe Constraints**: LRD observations probe the universe at z~4--5 (cosmic age ~1 Gyr), a regime in which the phonon-exflation model makes predictions about the expansion rate and equation of state. LRDs' existence as common objects constrains the early-universe AGN production rate and would be sensitive to the background cosmology's H(z) and rho(z).

**Black Hole Seed Formation Tension**: LRDs exemplify the "early black hole problem"—the need for black holes more massive than stellar-collapse remnants (m ~ 10--20 M_sun) to form within the first ~1 Gyr. The phonon-exflation framework's prediction of cosmological parameters at z~4 (e.g., density contrast growth, temperature, reheating history) would affect the viability of mechanisms proposed to form LRD progenitors (e.g., direct collapse, runaway stellar collisions). While the connection is indirect, LRD observations place constraints on early-universe physics that any cosmological framework must accommodate.

**Intensity**: Medium. LRDs provide phenomenological anchors at z~4 but do not directly probe the NCG spectral triple or internal metric deformation that are core to phonon-exflation.

---

## Key Equations Summary

| Quantity | Equation | Typical LRD Value |
|----------|----------|------------------|
| Black Hole Mass (from line width) | $M_{BH} = f \cdot \Delta v^2 \cdot R_{BLR} / G$ | 10^6--10^8 M_sun |
| Eddington Luminosity | $L_{Edd} = 1.3 \times 10^{46} (M_{BH}/10^8 M_{\odot})$ erg/s | 10^{44}--10^{46} erg/s |
| Number Density | $n_{LRD} \sim 10^{-5}$ cMpc^-3 | 10x UV quasar density |
| Dust Extinction | $A_V$ | 1.6--2.0 mag |
| Effective Radius | $r_e$ | <300 pc, typically ~150 pc |
