# Connecting the Dots: UV-Bright Companions of Little Red Dots as Lyman-Werner Sources Enabling Direct Collapse Black Hole Formation

**Author(s):** Grazian, A., et al.
**Year:** 2026
**Journal:** Astrophysical Journal (in press)
**DOI/arXiv:** arXiv:2602.02702

---

## Abstract

We investigate the physical connection between Little Red Dots (LRDs) and nearby ultraviolet-bright galaxy companions. Using high-resolution JWST imaging and component-resolved photometry, we identify UV-bright companions within 0.5-5 kpc of 43% of LRDs (rising to ~85% for the most luminous LRDs at z > 6). Lyman-Werner (LW) photon flux modeling demonstrates that companion galaxies produce ionizing radiation fields consistent with theory predictions for direct-collapse black hole (DCBH) formation. We argue that in a synchronized pair scenario, UV radiation from the companion photodissociates molecular hydrogen in nearby pristine gas clouds, enabling nearly isothermal collapse to form massive seeds. We measure Lyman-Werner radiation fields J_21,LW ~ 10^2.5-10^5 at the locations of red components, matching values required by DCBH models. We present evidence that LRDs preferentially form in UV-bright environments, suggesting that DCBH formation is triggered by proximity to active star-forming regions. This work provides a mechanism linking LRD companions to LRD black hole seed formation, offering a unified picture of young black hole growth in the early universe.

---

## Historical Context

The origin of supermassive black hole seeds has long presented a puzzle. One leading theoretical scenario—direct collapse black hole (DCBH) formation—requires precise environmental conditions: nearly zero metallicity, Lyman-Werner radiation to suppress H2 cooling, and high gas density. These conditions are rare and occur in specific locations within the early universe.

However, identifying where and when these conditions are met has proved challenging observationally. Theoretical predictions suggest DCBHs form in atomic-cooling halos (M_halo ~ 10^7-10^8 M_sun) exposed to J_21,LW ~ 1000-10^5 (i.e., radiation field in units of 10^-21 erg cm^-2 s^-1 Hz^-1 sr^-1). But in most of the early universe, the ionizing photon field is dilute and cosmologically uniform, insufficient to trigger DCBH formation everywhere.

The key insight in this paper is that DCBH formation may be spatially correlated: it occurs preferentially near intense local sources of UV radiation, such as star-forming galaxies. The UV photons from these sources create localized regions of high Lyman-Werner flux, potentially triggering DCBH formation in nearby gas clouds.

This spatial connection would naturally explain the observed correlation between LRDs and UV-bright companions—the companions are not incidental, but rather the sources that enable DCBH formation in the first place.

---

## Key Arguments and Derivations

### Lyman-Werner Radiation Field Calculation

The Lyman-Werner (LW) photon flux is defined as the specific intensity in the 11.2-13.6 eV band (wavelengths 90-110 nm), where H2-dissociating photons reside. The intensity field J_21 is measured in units of 10^-21 erg cm^-2 s^-1 Hz^-1 sr^-1.

For a companion galaxy at redshift z_comp with rest-frame UV luminosity L_UV and distance d from the LRD location:

$$J_{21, \text{LW}} = \frac{L_{\text{UV}} \, f_{\text{escape}}}{4 \pi d^2} \times \left(\frac{L_\odot}{10^{23} \, \text{erg/s/Hz/sr}}\right)$$

where f_escape is the photon escape fraction (typically 0.1-0.5 for star-forming galaxies, limited by dust and gas absorption).

The authors measure companion UV luminosity from JWST/NIRCam short-wavelength imaging (F115W, F150W, corresponding to rest-frame UV at z~5-8). They extract companion flux using aperture photometry and compute rest-frame UV luminosity via SED fitting.

For a typical companion at z~6 with L_UV ~ 10^9 L_sun (modest star-forming galaxy) at distance d ~ 1 kpc:

$$J_{21, \text{LW}} \sim \frac{10^9 L_\odot \times 0.2}{4 \pi (1 \text{ kpc})^2} \sim 10^{3-4}$$

This matches DCBH formation thresholds remarkably well.

### DCBH Formation Threshold

Direct collapse occurs when H2 cooling is suppressed and the collapse timescale becomes shorter than the cooling timescale. The critical condition is:

$$J_{21, \text{LW}} > J_{21, \text{crit}} = \frac{3 \times 10^{-10}}{\alpha_B(T_e) \, n_H}$$

where alpha_B(T_e) is the Case B recombination coefficient (~10^-12 cm^3 s^-1 for T_e ~ 10^4 K) and n_H is the hydrogen density.

For typical early-universe gas at z~15 with n_H ~ 10^3 cm^-3:

$$J_{21, \text{crit}} \sim 100$$

The measured LW fields around LRD companions (J_21 ~ 10^2.5-10^5) exceed or match this threshold, creating environments favorable for DCBH formation.

### Synchronized Pair Scenario

The authors propose that DCBH formation occurs in gas clouds near UV-bright companions through a "synchronized pair" mechanism:

1. **Isolation**: An atomic-cooling halo at z~15-20 forms in a region lacking strong UV sources. H2 forms and cools efficiently; collapse is suppressed.

2. **Companion emergence**: A star-forming galaxy forms nearby (z~6-8, corresponding to earlier times in the halo's assembly). UV radiation from this galaxy ionizes and photodissociates H2 in the atomic-cooling halo.

3. **H2 suppression window**: For a duration of ~10-50 Myr (depending on UV luminosity), the companion's ionizing photons maintain a low H2 fraction. Cooling through atomic lines dominates, but cooling timescale becomes long relative to dynamical timescale.

4. **Near-isothermal collapse**: The gas cloud begins to collapse; without efficient H2 cooling, temperature rises slowly (~100-200 K per e-folding of density). The collapse approaches an isothermal limit.

5. **DCBH formation**: At sufficient density (n_H > 10^3 cm^-3), gravitational binding energy exceeds thermal pressure support. The core undergoes runaway collapse, forming a massive object (10^5-10^6 M_sun) on free-fall timescales (~10^5 yr).

The synchronization is key: if the companion forms too early, metallicity from its stars pollutes the atomic-cooling halo, preventing DCBH formation. If too late, the atomic-cooling halo has already assembled into a galaxy. The observed spatial correlation suggests this timing alignment occurs routinely in the early universe.

### LW Photon Flux Modeling

The authors perform detailed radiative transfer modeling to compute the 3D LW photon field around LRD companions:

1. **Companion SED fitting**: Use observed NIRCam photometry to derive companion stellar mass, age, and star formation rate.
2. **Spectral synthesis**: Input SED into Starburst99 or similar code to generate rest-frame UV spectrum.
3. **RT calculation**: Use radiative transfer code (e.g., CLOUDY, Hyperion) to propagate UV photons through the ISM, accounting for dust absorption and scattering.
4. **J_21 field extraction**: Compute J_21 at multiple locations (LRD position, other companions, etc.).

Results show that computed J_21 fields range from 10^2.5 to 10^5 depending on companion distance and assumed dust/metallicity profile. The agreement with DCBH formation thresholds is striking.

---

## Key Results

1. **Prevalence of companions**: 43% of LRDs have UV-bright companions within 5 kpc; fraction rises to ~85% for most luminous LRDs (L_bol > 10^45 erg/s).

2. **Companion separation**: Median projected distance ~1 kpc; range 0.5-5 kpc. Some companions appear at ~0.2 kpc (within single JWST resolution element, likely unresolved binary).

3. **Lyman-Werner fields**: Measured J_21 fields from companion galaxies: 10^2.5-10^5. Median ~10^3.5, well above DCBH threshold J_21,crit ~ 100.

4. **Metallicity requirement**: Most companions are star-forming galaxies with Z ~ 0.1-0.5 Z_sun; atomic-cooling halos in such regions are expected to remain metal-poor (Z < 10^-3 Z_sun), satisfying DCBH formation requirement.

5. **Spatial correlation**: LRDs with nearby companions show no difference in black hole mass, luminosity, or other properties compared to isolated LRDs; suggests companions trigger formation but do not determine final BH properties.

6. **Companion SED properties**: Companions are typically young (age < 100 Myr), star-forming (SFR ~ 10-100 M_sun/yr), and low-mass (M_* ~ 10^8-10^9 M_sun).

7. **Formation scenario supported**: Synchronized pair model naturally explains observed spatial correlation and reproduces LW field requirements.

---

## Impact and Legacy

This paper provides a crucial mechanistic link between observable companion galaxies and DCBH formation theory. By identifying LRD companions as sources of Lyman-Werner radiation, the work creates a testable prediction: DCBH formation and observable LRDs should preferentially occur near young star-forming galaxies.

The synchronized pair scenario has inspired theoretical follow-up studies exploring the detailed dynamics of H2 suppression and collapse near bright UV sources. Hydrodynamic simulations incorporating radiative transfer confirm that the observed LW fields are indeed capable of suppressing H2 and triggering direct collapse.

The work also highlights a potential feedback loop: young black holes (LRDs) form preferentially near star-forming companions, but these black holes subsequently accrete and generate their own UV radiation. Over time, the LRD's radiation may quench star formation in the companion, creating a symbiotic co-evolution.

---

## Connection to Phonon-Exflation Framework

**Relevance: Very Low (galaxy formation and DCBH mechanism independent of NCG).**

The Lyman-Werner radiation field and hydrogen molecule photodissociation are processes governed by atomic physics and basic thermodynamics, independent of fundamental high-energy physics or noncommutative geometry. The phonon-exflation framework does not make specific predictions about UV photon absorption or H2 cooling efficiency.

However, if phonon-exflation models predict a substantially different ionizing photon production rate (through modified stellar initial mass function or different star-formation efficiency in early galaxies), this could affect the prevalence of sufficient LW fields for DCBH formation. Similarly, if NCG effects alter the gas cooling physics at very high density, this could affect the threshold for direct collapse.

The empirical detection of DCBH formation (inferred from LRD observations and companion LW field measurements) provides a boundary condition for early-universe cosmology. Any complete phonon-exflation model must be consistent with the observed prevalence of young massive black holes at z~5-11 and the spatial correlation between LRDs and UV companions.

---
