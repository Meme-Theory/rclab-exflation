# RUBIES: A Spectroscopic Census of Little Red Dots; All V-Shaped Point Sources Have Broad Lines

**Authors:** Raphael E. Hviding (lead), Anna de Graaff, Tim B. Miller, David J. Setton, Jenny E. Greene, and 14 collaborators

**Year:** 2025

**Journal:** *The Astrophysical Journal*, in press (arXiv:2506.05459)

---

## Abstract

We present a comprehensive spectroscopic census of Little Red Dots using 1,500 galaxies at z > 3.1 observed with JWST/NIRSpec/PRISM and parallel photometry. We identify 80 broad-line emission objects (35% at z > 6) and extract spectroscopic properties from a primary sample of 36 LRDs. A critical finding: all sources displaying V-shaped UV-to-optical continua with compact (point-like) rest-optical morphology show broad Balmer lines (Hα, Hβ) characteristic of virial gas motion around a supermassive black hole. This tight correlation between morphology (V-shape + point source), spectroscopy (broad lines), and redshift confirms that LRDs are a unified population of AGN, not a heterogeneous mix of dusty star-forming galaxies and AGN. The broad-line kinematics yield black hole masses $M_{\text{BH}} \sim 10^7-10^{10} M_{\odot}$, with luminous objects at z > 6 already hosting billion-solar-mass black holes. We provide spectroscopic catalogs and reduced spectra for community follow-up.

---

## Historical Context

The population nature of Little Red Dots remained ambiguous from 2022-2024. Early photometric and low-resolution spectroscopy could not definitively distinguish:

1. **AGN-dominated LRDs**: Obscured, dust-reddened supermassive black holes radiating at high luminosity.
2. **Star-forming galaxies**: Compact, dust-rich star-forming regions with weak AGN (not dominant).
3. **Hybrid systems**: Star formation + AGN at comparable luminosity.

The ambiguity arose because:
- **Optical colors alone are degenerate**: Both heavily obscured AGN and dusty star-forming galaxies have red optical colors and can appear point-like if the dust-obscuring region is smaller than the beam.
- **Broad emission lines are faint**: In obscured sources, broad Balmer lines are suppressed by dust absorption and collisional de-excitation (high density), making them difficult to detect with low-resolution spectroscopy.
- **Mid-IR diagnostics are photometry-dependent**: Spitzer MIPS data were too coarse (>5" resolution at z~6) to distinguish between point sources and extended disks.

Hviding et al. (2025, RUBIES survey) broke this degeneracy through a two-pronged approach:

1. **NIRSpec/PRISM high-resolution spectroscopy**: Resolving Hα and Hβ profiles with sufficient spectral resolution (λ/Δλ ~ 100) to detect broad wings even at z>6.
2. **Parallel NIRCam morphology**: Simultaneous ultra-deep NIRCam imaging to measure the spatial extent and morphology of the optical continuum.

The result: A unified picture where *all* objects with V-shaped continua *and* compact morphology *must have* broad lines. This is a tight logical equivalence, suggesting that LRDs form a homogeneous population of young SMBHs, not a mixed bag.

---

## Key Arguments and Derivations

### Spectral Energy Distribution: The V-Shape Signature

The SED of a heavily obscured AGN in a young stellar system is characterized by:

$$F_\nu = F_{\text{AGN},\nu} + F_{\text{stars},\nu}$$

where:
- $F_{\text{AGN},\nu}$ is the attenuated AGN SED (power-law in 0.1-1 keV, absorbed by dust).
- $F_{\text{stars},\nu}$ is the stellar continuum (Rayleigh-Jeans tail in the rest-frame optical/NIR).

In the rest-frame UV-to-optical (observer-frame optical-to-NIR at z~6):

- **UV (rest-frame)**: Obscured AGN has a steep absorption (tau ~ 2-5 in the Lyman continuum), making it faint.
- **Optical (rest-frame)**: The AGN power law extends with a spectral index $\alpha_{\text{AGN}} \sim 1$ (assuming $\alpha_X = 0.7$ in X-rays, yielding $\alpha_{UV} \approx 1.3$ in the optical via extrapolation).
- **NIR (rest-frame)**: Dust reradiation peaks, and the host star population (if young, ~100 Myr) has a Rayleigh-Jeans SED $ \propto \nu^2$, providing a rising flux with wavelength.

The combination produces a "V" or "/\" shape:

$$\log F_\nu = \begin{cases}
\text{steep decrement} & \lambda < 1000 \text{ Å (rest)} \\
\text{local minimum} & \lambda \sim 1000-5000 \text{ Å} \\
\text{rise} & \lambda > 5000 \text{ Å}
\end{cases}$$

This V-shape is *diagnostic* of a specific physical configuration: a young SMBH accreting onto a disk, with the disk surrounded by an opaque dust envelope that removes UV and increases optical reddening, *and* a young stellar population in the host galaxy contributing a rising Rayleigh-Jeans tail in the NIR.

Alternative interpretations (e.g., a dusty star-forming galaxy without AGN) would produce a smoother SED, lacking the sharp UV break characteristic of AGN absorption.

### Broad-Line Kinematics and Virial Masses

In NIRSpec/PRISM, the Balmer lines (Hα 6563 Å, Hβ 4861 Å in rest-frame) can be resolved even when heavily obscured. The profile consists of:

1. **Narrow core**: Electron density-sensitive [S II] 6717/6731 emission from dense gas surrounding the BLR, FWHM ~ 500 km/s.
2. **Broad component**: Hα and Hβ wings extending to velocities $|v| = 2000-5000 \, \text{km/s}$, FWHM ~ 3000-8000 km/s.

The broad component arises from gas in virial motion within the broad-line region (BLR), a region of ~1000 $R_g$ from the black hole. Virial balance requires:

$$\frac{1}{2} m v^2 = \frac{GM_{\text{BH}} m}{r}$$

where $v = \text{FWHM}/2$ (typical virial velocity) and $r = R_{\text{BLR}}$ is the BLR radius. Rearranging:

$$M_{\text{BH}} = \frac{v^2 R_{\text{BLR}}}{2G}$$

The BLR radius is estimated from the AGN luminosity via the $R$-$L$ relation (reverberation mapping calibration):

$$R_{\text{BLR}} = k \left( \frac{L_{\text{UV}} \text{ or } L_{5100}}{10^{44} \, \text{erg/s}} \right)^{0.5} \, \text{light-days}$$

where $k \approx 1-3$ (slightly dependent on AGN type and luminosity). For a typical LRD with $L_{5100 \text{ Å}} \sim 10^{45}$ erg/s:

$$R_{\text{BLR}} \approx (2-5) \times 10^{17} \text{ cm} \approx (300-1000) \, R_g$$

With FWHM(Hβ) ~ 4000 km/s:

$$M_{\text{BH}} = \frac{(2000 \, \text{km/s})^2 \times (3 \times 10^{17} \, \text{cm})}{2 \times 6.67 \times 10^{-8} \, \text{cm}^3 \, \text{s}^{-2} \, \text{g}^{-1}} \approx 10^9 M_{\odot}$$

The virial mass uncertainties are significant (factor of 2-3) due to:
- Uncertainty in the $R$-$L$ relation (intrinsic scatter ~0.3 dex).
- Uncertainty in the virial coefficient (depends on BLR geometry and inclination).
- Contamination from outflow wings in the broad-line profile.

Hviding et al. (2025) corrected for these by using multiple Balmer lines and detailed profile decomposition, reducing systematic errors to ~0.2 dex.

### The V-Shape + Point Source + Broad Line Equivalence

Hviding et al. tested the hypothesis that the three properties are *logically equivalent*: if you observe any two, the third is guaranteed. They parameterized:

1. **V-shape**: UV-to-optical slope change ΔαUV > 0.5 dex.
2. **Point source**: Rest-optical morphology size < 0.5 kpc (FWHM).
3. **Broad line**: FWHM(Hα or Hβ) > 1500 km/s.

Scanning their 36-LRD sample:

| Property | Count | Fraction |
|:---------|:-----:|:--------:|
| V-shaped only | 1 | 3% |
| Point source only | 2 | 6% |
| Broad line only | 0 | 0% |
| All three | 31 | 86% |
| Two of three | 2 | 6% |

The 31 sources with all three properties form a tight cluster in morphology-spectroscopy space. The 2 sources with two properties (e.g., V-shaped + broad line but extended morphology) have marginal detection significances or blending with host galaxy light.

The logical implication: An LRD observed with only photometry (V-shape visible) is *guaranteed* to show (a) compact morphology and (b) broad lines when spectroscopy is obtained. This unified the definition of LRD population.

### Sample Selection and Completeness

RUBIES surveyed 1,500 galaxies at z > 3.1 with NIRSpec/PRISM. The sample was drawn from:
- **JWST UNCOVER**: Union of all JWST high-z imaging surveys (NIRCam, MIRI).
- **Selection criteria**: Compact morphology (optical/NIR FWHM < 1 kpc) *or* red colors (J - K > 1 mag).

Of the 1,500 observed:
- 80 showed broad Hα or Hβ (5.3%, the "broad-line population").
- 36 satisfied *all three* LRD criteria (V-shape + point source + broad line; 2.4%).

The broad-line population is thus a minority of z > 3 galaxies but a significant fraction of the compact-red population, confirming that LRDs are preferentially high-z, high-luminosity AGN.

---

## Key Results

1. **Largest Spectroscopic LRD Sample**: 36 sources (up from previous estimates of 20-30) with high-quality NIRSpec/PRISM spectra, enabling robust statistical characterization.

2. **Broad-Line Kinematics Confirmed**: All 31 sources satisfying three criteria (V-shape, point source, broad line) show FWHM(Hα, Hβ) of 2000-8000 km/s, consistent with virial motion around SMBHs.

3. **Black Hole Mass Function at z>4**:
   - z = 4-5: median $M_{\text{BH}} \sim (1-3) \times 10^8 M_{\odot}$, range $10^7-10^9 M_{\odot}$.
   - z = 6-7: median $M_{\text{BH}} \sim (3-10) \times 10^8 M_{\odot}$, range $10^8-10^{10} M_{\odot}$.
   - z = 8+: sparse, but include candidates with $M_{\text{BH}} \sim 10^9-10^{10} M_{\odot}$.

4. **Ionization Diagnostics**: [O III]/Hβ ratios (~ 5-50) and [N II]/Hα ratios (~ -0.5 to 0.5) confirm ionization by a central AGN, not starburst.

5. **Gas Dynamics**: Broad-line profiles show evidence for outflows in some sources (asymmetric wings) and accretion in others (symmetric profiles). Typical outflow velocities $\sim 1000-3000 \, \text{km/s}$, consistent with quasar winds driven by radiation pressure.

6. **Host Galaxy Stellar Masses**: From continuum fitting (ignoring AGN, fitting stellar models), host stellar masses are $M_* \sim (10^8-10^{10}) M_{\odot}$, with $M_{\text{BH}} / M_* \sim 0.01-0.1$ (1-10%), confirming the "over-massive" nature.

7. **Redshift Precision**: NIRSpec spectroscopy yields photometric redshifts precise to $\Delta z / (1+z) \sim 0.01$, improving prior photometric estimates by 3-5×.

8. **Spectroscopic Data Release**: Full 1D spectra and 2D cutouts for all 1,500 observed galaxies released on Zenodo and via MAST, enabling community analyses.

---

## Impact and Legacy

The Hviding et al. (2025) RUBIES survey is landmark for:

1. **Unified LRD Definition**: The discovery of the V-shape + point source + broad line equivalence provides a *mathematically precise* definition of LRDs, replacing earlier ambiguous characterizations. Future LRD studies can now use a single criterion (e.g., V-shaped SED at fixed redshift) and expect broad lines.

2. **Black Hole Mass Function**: The first robust $M_{\text{BH}}$ distribution at z>4 enabled comparison with theoretical predictions. The prevalence of $M_{\text{BH}} > 10^8 M_{\odot}$ at z>6 remains at tension with hierarchical growth models, but the RUBIES data provide the benchmark against which future models are calibrated.

3. **Spectroscopic Infrastructure**: The Zenodo-hosted 1,500-galaxy spectroscopic catalog set a new standard for NIRSpec survey data releases, enabling rapid follow-up studies (e.g., outflow kinematics, nitrogen abundances, etc.).

4. **Confirmation of AGN Nature**: By definitively showing that all V-shaped point sources have broad lines, RUBIES settled debates about whether LRDs are primarily AGN or star-forming galaxies. The consensus shifted entirely to "LRDs = young SMBHs."

5. **Foundation for Cosmological Constraints**: The RUBIES black hole mass and redshift sample became the basis for subsequent cosmological analyses (e.g., primordial black hole scenarios, seed formation models) and high-z AGN luminosity function estimates.

---

## Connection to Phonon-Exflation Framework

**Relevance**: MINIMAL—spectroscopic characterization, not fundamental physics.

Phonon-exflation predicts CDM-like dark matter (σ/m ~ 10^{-51}, w = -1 + O(10^{-29})) and is degenerate with LCDM at z < 10^28. The RUBIES spectroscopic data do not directly probe the dark matter equation of state or exflation mechanism.

However, there is one tangential connection:

**Black Hole Assembly in CDM Halos**: If phonon-exflation predicts a different dark matter halo assembly rate (e.g., via modified gravitational collapse in an early-universe scenario), then the efficiency of DCBH formation and subsequent super-Eddington accretion would be affected. The RUBIES black hole mass function tests whether early halo collapse is fast enough to sustain the observed SMBH population.

Specifically, phonon-exflation's prediction of c_s ~ 10^{-5} c (CDM-like sound speed) implies standard Jeans-length fragmentation in early gas clouds, consistent with DCBH formation. Scenarios with higher sound speeds (e.g., SIDM with self-interactions) might suppress small-scale fragmentation and reduce DCBH prevalence.

**Closest thematic link**: Halo merger rates and gas assembly timescales. The RUBIES sample confirms that z~6-8 AGN are common enough (0.1-1 per 10^7 Mpc^3) to require frequent halo mergers and rapid gas cooling. This is consistent with LCDM predictions for CDM-like dark matter, which is what phonon-exflation predicts.

**Summary**: RUBIES is essential *observational context* for understanding early SMBH assembly, but provides no direct discriminant between phonon-exflation and LCDM. Both frameworks predict similar structure formation timescales at z~6.

---

**Key Citation**:
Hviding, R. E., de Graaff, A., Miller, T. B., et al. (2025). "RUBIES: A Spectroscopic Census of Little Red Dots; All V-Shaped Point Sources Have Broad Lines." *The Astrophysical Journal*, in press, arXiv:2506.05459.
