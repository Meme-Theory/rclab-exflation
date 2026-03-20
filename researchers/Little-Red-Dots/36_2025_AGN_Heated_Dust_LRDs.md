# AGN-Heated Dust Revealed in Little Red Dots

**Author(s):** Delvecchio et al. (14 authors)
**Year:** 2025
**Journal:** Astronomy & Astrophysics, Volume 704, Article A313

---

## Abstract

JWST MIRI near-infrared imaging and ground-based ALMA millimeter observations of >100 Little Red Dots at z~5-7 reveal that approximately 50-70% of the LRD population harbor active galactic nuclei with hot dust heated by accretion. Stacking analysis of the infrared spectral energy distribution (SED) shows a characteristic rising near-infrared continuum (1-30 μm) consistent with dust temperatures of order 100-500 K, produced by AGN accretion luminosity rather than star formation. The hot dust component is luminous (L_IR ~ 10^{44}-10^{46} erg/s), confirming that LRDs are accreting systems. Critically, Compton-thick gas columns ($N_H > 10^{24}$ cm^-2) are inferred from the dust IR opacity, while broad emission lines remain visible in some objects—a puzzle indicating that the gas distribution is patchy or that the broad-line region is located above the Compton-thick screen. ALMA non-detections of cold dust at rest-frame submillimeter wavelengths are resolved: the cold dust component is simply absent or negligible; LRDs are dominated by hot AGN dust, not extended star-forming reservoirs. This finding unifies the LRD population as a new class of heavily obscured, accreting black holes at the epoch of reionization.

---

## Historical Context

Little Red Dots earned their name from their distinctive infrared colors: faint in optical (JWST NIRCam optical filters), conspicuously red in near-infrared (NIRCam 3.56 μm), and variable redward into the mid-infrared. Initial interpretations of this color were ambiguous:

1. **Dust-obscured star-forming galaxies**: Maybe LRDs are extreme dusty starbursts with SFR > 1000 M_sun/yr, not AGN
2. **Early massive galaxies with stellar continuum**: Maybe LRDs are passively-evolving galaxies, their red color coming from old stellar populations
3. **Dust-obscured quasars**: Maybe LRDs are heavily obscured AGN, with dust-reprocessed accretion light dominating the infrared

A critical observational puzzle emerged: ALMA observations of many LRDs yielded **non-detections** at rest-frame submillimeter wavelengths (100-850 μm). This was surprising because dusty star-forming galaxies (DSFGs) at z~2-3 are bright at submillimeter wavelengths; if LRDs were similarly dusty starbursts, ALMA should detect them easily.

The non-detections were initially interpreted as problematic—perhaps AGN feedback suppresses star formation in LRDs, or perhaps the dust is structured in ways ALMA cannot detect. Alternatively, perhaps LRDs genuinely lack the extended cold dust reservoirs characteristic of normal galaxies, suggesting a different physical origin altogether.

This paper resolved the tension by demonstrating that **LRDs have extremely hot dust dominated by AGN heating, with negligible cold dust**. The submillimeter non-detections are expected: at temperatures T > 100 K, dust emits primarily in the near-infrared and mid-infrared, not at millimeter wavelengths where the Rayleigh-Jeans approximation ($I_\nu \propto \nu^2$) predicts dimming. LRDs are simply not cold-dust-rich systems.

---

## Key Arguments and Derivations

### Dust Temperature Measurement from SED Fitting

The dust-dominated infrared SED of an AGN can be approximated as a modified blackbody:

$$F_\nu = A \left(\frac{\nu}{\nu_0}\right)^\beta B_\nu(T_d)$$

where $B_\nu(T_d)$ is the Planck function at dust temperature $T_d$, $\beta$ is the emissivity index (~1.5-2 for silicate dust), and $A$ is a normalization.

By fitting the SED in the 1-30 μm range (MIRI photometry and spectroscopy) and the 100-870 μm range (ALMA/NOEMA), one can extract both $T_d$ and $\beta$. The paper employed Bayesian SED fitting with multiple dust component models:

**Single-temperature model**:
$$\chi^2 = \sum_i \frac{(F_{obs,i} - F_{model,i}(T_d, \beta, A))^2}{\sigma_i^2}$$

**Two-temperature model** (hot + cold dust):
$$\chi^2 = \sum_i \frac{(F_{obs,i} - [A_h F_{hot,i} + A_c F_{cold,i}])^2}{\sigma_i^2}$$

Results for ~100 LRDs with sufficient data quality show:

- **Hot dust component**: $T_{hot} = 150-400$ K, $L_{hot} = 10^{44}-10^{46}$ erg/s
- **Cold dust component**: $T_{cold} = 30-60$ K, $L_{cold} \sim 10^{42}-10^{43}$ erg/s (when detectable)
- **Dominant contribution**: Hot dust accounts for >70% of infrared luminosity in 75% of LRDs

The characteristic near-infrared rising continuum (flux increasing with frequency in the 1-5 μm region) is a smoking gun for hot dust with $T \sim 100-300$ K, which is far hotter than dust in normal starbursts ($T \sim 30-60$ K) but typical of AGN dusty tori (T ~ 100-1000 K).

### AGN Accretion as Heat Source

The luminosity of hot dust must be powered by a radiation source. Possible mechanisms include:

1. **AGN accretion**: A black hole accreting at near-Eddington rates produces an accretion-disk continuum that heats surrounding dust
2. **Star formation**: Intense star formation produces ultraviolet radiation that heats dust
3. **Shock heating**: Kinetic energy from jets or outflows heats dust to high temperatures

Spectral decomposition distinguishes these sources. The paper uses infrared spectral diagnostics:

- **Mid-infrared emission lines**: [OIV] 25.89 μm, [NEIII] 15.56 μm, [NIII] 57.3 μm are AGN-powered in Seyfert 2 galaxies but not in starbursts
- **Silicate absorption feature** at 9.7 μm: strength indicates column density and dust geometry
- **Continuum slope**: AGN-heated dust shows rising continuum from 3-20 μm; starburst dust shows declining slope

Results show:
- **[OIV]/[NEIII] ratios**: 0.3-1.5 (typical AGN values; starbursts have ratios ~0.1)
- **Silicate equivalent width**: -1.0 to -2.0 (consistent with Compton-thick obscured AGN; star-forming galaxies have -0.5 or less)
- **3-20 μm continuum slope**: rising in 60-80% of LRDs (AGN signature); declining in starbursts

**Conclusion**: The infrared heating is dominated by AGN accretion, not star formation. The dust is heated by the intense radiation from an accreting black hole.

### Compton-Thickness and Gas Column Density

The optical depth of dust in the infrared is related to gas column density by:

$$\tau_{IR} = \sigma_d n_H N_H$$

where $\sigma_d \sim 10^{-21}$ cm^2 is the dust absorption cross-section per hydrogen atom, $n_H$ is the hydrogen number density, and $N_H$ is the column density. The paper infers $N_H$ by modeling the infrared-to-X-ray flux ratio.

X-ray observations (Chandra stacking) reveal that LRDs are extremely X-ray faint. The X-ray-to-infrared luminosity ratio is:

$$\frac{L_X}{L_{IR}} \sim 10^{-3}-10^{-4}$$

compared to unobscured AGN, which typically have $L_X/L_{IR} \sim 0.1$. This suppression is consistent with Compton-thick obscuration.

Using the relation:

$$L_X^{intrinsic} = L_X^{observed} / \exp(-N_H \sigma_T)$$

where $\sigma_T$ is the Thomson cross-section, the paper estimates:

$$N_H \sim 10^{24}-10^{25} \text{ cm}^{-2}$$

This is the definition of Compton-thick material: even Thomson scattering (which dominates at high energies) cannot penetrate the gas.

### Puzzle: Broad Emission Lines in Compton-Thick AGN

A surprising feature is that **some LRDs show broad emission lines** (FWHM ~ 1000-5000 km/s) in infrared spectroscopy, particularly in Paschen-α (1.875 μm) and Brackett-α (4.05 μm) transitions. Broad emission lines are a signature of gas moving at high velocity near the black hole—the broad-line region (BLR).

However, in a uniformly Compton-thick obscuration geometry, the BLR should be hidden. The gas between us and the BLR should absorb the broad-line photons before they escape.

Possible resolutions:

1. **Patchy obscuration**: The Compton-thick gas is not uniformly distributed but clumpy. Some sightlines to the BLR are unobscured or lightly obscured, allowing broad lines through
2. **High-latitude geometry**: The BLR is located at high galactic latitude, above the dusty torus plane. Photons escape along the polar direction, above the Compton-thick equatorial screen
3. **Polar outflow**: An AGN-driven wind creates a low-density "wind cone" along the polar axis, allowing BLR photons to escape

The paper favors the patchy obscuration + high-latitude BLR scenario, supported by infrared interferometry hints of clumpy dust structure around some LRDs.

### ALMA Non-detection Resolution

ALMA observations at 870 μm (rest-frame ~135 μm at z~6) set deep limits on the cold dust luminosity:

$$L_{cold} < 10^{43}-10^{44} \text{ erg/s (3-sigma limits)}$$

For a normal dusty star-forming galaxy with $T_{dust} \sim 30$ K and dust emitting in the Rayleigh-Jeans regime ($I_\nu \propto \nu^2 T$), this translates to:

$$L_{cold} = 4\pi d^2 F_{870\mu m} \nu^2 / (2 k_B T)$$

Typical star-forming galaxies at z~2-3 have $L_{IR,cold} \sim 10^{45} \text{ erg/s}$, producing $F_{870\mu m} \sim 1-10$ mJy. ALMA limits of ~0.1 mJy thus imply that LRDs have ~10-100 times less cold dust than similar-mass starbursts.

This is *not* a puzzle: it simply reflects that LRDs are AGN-dominated, not starburst-dominated. Their infrared luminosity comes from hot dust near the black hole, not extended cold dust in star-forming disks.

---

## Key Results

1. **Hot dust dominates LRD infrared luminosity**: 50-70% of LRDs show clear evidence of hot dust with temperatures 100-400 K, characteristic of AGN tori rather than star-forming regions.

2. **AGN accretion confirmed as primary heat source**: Mid-infrared diagnostics ([OIV]/[NEIII] ratios, silicate absorption, continuum slope) confirm that AGN accretion, not star formation, powers the infrared luminosity.

3. **Compton-thick gas columns inferred**: X-ray faintness combined with infrared brightness indicates gas column densities $N_H > 10^{24}$ cm^-2, consistent with Compton-thick obscured AGN.

4. **Broad emission lines persist through obscuration**: Some LRDs show broad hydrogen recombination lines despite Compton-thick gas, indicating patchy obscuration or high-latitude BLR geometry.

5. **ALMA non-detections explained**: Cold dust is simply absent or negligible in LRDs. The submillimeter non-detections are expected given that LRD dust is hot (NIR/MIR-dominated), not cold (submillimeter-dominated).

6. **Unified AGN population**: LRDs are a distinct population of heavily obscured, accreting supermassive black holes at z~5-7, analogous to Compton-thick quasars observed at lower redshift but appearing at an unexpectedly early epoch.

7. **Star formation rates low or absent**: The lack of cold dust implies minimal active star formation. LRD infrared luminosity is accretion-powered, not star-formation-powered.

---

## Impact and Legacy

This paper transformed the interpretation of LRDs from a heterogeneous population of unknown objects to a coherent class of **heavily obscured active galactic nuclei**. It provided strong evidence that LRDs are legitimate quasars—accreting supermassive black holes—rather than exotic stellar systems or alternative black hole formation products.

The work has motivated:
- Higher-resolution infrared spectroscopy of individual LRDs to map the dust geometry
- X-ray spectroscopy attempts to constrain the gas composition and ionization state
- Studies of the AGN-galaxy connection: how do LRD black holes grow so massive while their host galaxies remain relatively compact?
- Modeling of the AGN-driven winds and outflows that likely shape LRD morphologies

---

## Connection to Phonon-Exflation Framework

**OBSERVATIONAL RELEVANCE**: This paper establishes that LRDs are genuine AGN, not alternative objects. This is important for the framework's discriminant.

**Black hole seeding question unchanged**: Confirming that LRDs are AGN does not resolve whether their seeds formed via CDM (direct collapse, mergers), uSIDM (gravothermal collapse), or ULDM (solitonic collapse). The paper provides the **phenomenology** of LRDs but not the **origin** of their seeds.

**Implication for phonon-exflation**: If LRDs are confirmed AGN, then the question "How do 10^9 M_sun black holes form so early?" remains acute. The phonon-exflation framework predicts that seed formation occurs via standard CDM physics (direct collapse, stellar mergers). For this to be viable, LRD seeds must have formed by z~7-8, with growth to 10^8-10^9 M_sun by z~5 occurring via rapid accretion (~Eddington or super-Eddington).

The hot dust temperatures (100-400 K) are consistent with Eddington accretion (L ~ L_E) or super-Eddington accretion ($L > L_E$), supporting rapid growth. This is *consistent* with phonon-exflation's CDM-based predictions.

**Verdict**: This paper is an **observational characterization** of LRDs as AGN. It does not directly test phonon-exflation's dark matter prediction, but it confirms that LRDs are genuine accreting systems, establishing that the "early SMBH problem" is real and must be resolved by one of the mechanisms (CDM, uSIDM, ULDM, or alternatives).
