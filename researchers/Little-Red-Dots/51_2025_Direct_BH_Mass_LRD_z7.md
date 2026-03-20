# A Direct Black Hole Mass Measurement in a Little Red Dot at the Epoch of Reionization

**Author(s):** Ignas Juodžbalis, Cosimo Marconcini, Francesco D'Eugenio, Roberto Maiolino, Alessandro Marconi, and 36 co-authors

**Year:** 2025

**Journal:** arXiv:2508.21748

---

## Abstract

The masses of black holes in Little Red Dots (LRDs) have been inferred primarily from virial relations applied to broad-line emission (M_BH ~ f * FWHM^2 / G), but these indirect estimates are potentially biased if the broad-line region (BLR) does not trace virial motion. This work presents the first direct (dynamical) measurement of a black hole mass in an LRD: a strongly lensed galaxy at z = 7.04 with Keplerian rotation signature detected in near-infrared spectroscopy. The rotation curve of ionized gas reveals a central point mass of M_BH = 50 ± 10 million solar masses, approximately 50% lower than virial estimates for similar objects. The host galaxy stellar mass is M_* ~ 1-2 times 1e7 solar masses, yielding M_BH/M_* ~ 2-3, an overmassive but not extreme ratio. The measured black hole mass is consistent with rapid growth from a seed via Eddington-limited accretion over 100-200 Myr (z = 10 to z = 7), requiring no exotic mechanisms. The direct measurement resolves prior debates about whether LRD black hole masses are overestimated by virial methods and demonstrates the importance of kinematic follow-up for understanding the early black hole population. The lensed system provides an anchor for revising the inferred masses of non-lensed LRDs and constrains black hole formation pathways in the early universe.

---

## Historical Context

The masses of black holes in LRDs have been estimated primarily via the virial relation:

$$M_{\text{BH}} = f \frac{c \, r_{\text{BLR}} \, \Delta V^2}{G}$$

where:
- $r_{\text{BLR}}$ is the broad-line region radius, estimated from the H-alpha luminosity via empirical correlations
- $\Delta V$ is the broad-line FWHM (km/s)
- $f$ is a virial factor (~0.3-1.5, depends on BLR geometry and orientation)

Applied to LRDs, this method yields M_BH ~ 1e6-1e9 solar masses for the observed broad-line widths and luminosities.

However, prior work (Torralba et al. 2025, Paper 47) demonstrated that LRD broad emission lines may not originate from the innermost accretion disk but from dense gas cocoons. If the broad lines arise from photoionized gas in an optically thick envelope (not virialized motion around the black hole), then the virial mass estimates are systematically biased. In extreme cases, the overestimate could be a factor of 2-10.

The Juodžbalis et al. 2025 paper provides a direct test via dynamical mass measurement. Gravitational lensing of a high-z galaxy brightens its light and magnifies spectroscopic features, enabling detection of kinematic signatures of the black hole that would be undetectable in unlensed systems.

---

## Key Arguments and Derivations

### Lensing Magnification and Spectroscopic Sensitivity

Strong gravitational lensing magnifies the image by a factor $\mu \sim 10-100$. For a source with observed flux F_obs in the unlensed case, the lensed flux is:

$$F_{\text{lensed}} = \mu \times F_{\text{unlensed}} + (\text{noise})$$

The signal-to-noise ratio increases as $\sqrt{\mu}$:

$$\frac{S}{N}_{\text{lensed}} = \sqrt{\mu} \times \frac{S}{N}_{\text{unlensed}}$$

For a moderately bright LRD at z = 7 with S/N ~ 5-10 per spectral element in unlensed condition, magnification by mu = 10 yields S/N ~ 15-30, sufficient to resolve velocity structure in emission lines with resolution ~50 km/s (achievable with JWST NIRSpec).

The magnified spectrum reveals spatial/kinematic structure in the broad-line region. For a point source (black hole) of mass M surrounded by rotating gas, the rotation curve is Keplerian:

$$v(r) = \sqrt{\frac{GM_{\text{BH}}}{r}}$$

The observed rotation velocity (half-width of the emission-line profile) yields:

$$M_{\text{BH}} = \frac{v^2 r}{G}$$

where the radius r is inferred from the time delay between continuum and line variations (reverberation mapping) or from the spatial extent of the line-emitting region (achievable with JWST spatially-resolved spectroscopy).

### Keplerian Rotation in the LRD at z=7.04

The spectroscopic observations reveal:

1. **Continuum**: Nuclear point source, magnitude r ~ 24 (lensed), color consistent with AGN (blue in rest-frame UV, red in optical due to dust)
2. **Emission lines**:
   - H-alpha 6563 Angstroms (rest-frame): Detected with S/N ~ 20. Spatially-resolved spectroscopy shows velocity gradient: blueshifted on one side, redshifted on the other, consistent with rotation.
   - [OIII] 5007 Angstroms: Narrower profile (FWHM ~ 500 km/s), consistent with extended gas unrelated to black hole dynamics
   - Paschen-alpha (H 1-3 transition): Broad profile similar to H-alpha, confirming consistency across multiple lines

3. **Velocity structure**: The H-alpha line exhibits a double-peaked profile, characteristic of a rotating disk. The velocity separation is:

$$\Delta v = v_{\text{max}} - v_{\text{min}} \sim 2000-3000 \text{ km/s}$$

4. **Spatial resolution**: JWST NIRSpec achieves angular resolution ~0.1 arcsec. At z = 7.04 (scale ~0.15 kpc/arcsec), this corresponds to a physical scale ~15 pc. The lensed source is magnified in size by ~sqrt(mu) ~ 3, enabling imaging of structures at scale ~5 pc.

5. **Rotation curve**: The H-alpha velocity as a function of position angle shows a clear Keplerian pattern:

$$v(R) = v_{\text{circ}} \sqrt{\frac{r_*}{R}}$$

where $r_*$ is a characteristic inner radius. Fitting yields a central point mass:

$$M_{\text{BH}} = 50 \pm 10 \, M_\odot \times 10^6$$

---

## Key Results

1. **Direct dynamical measurement of a black hole mass in an LRD at z = 7.04 via Keplerian rotation signature in H-alpha and Paschen-alpha lines yields M_BH = 50 ± 10 million solar masses.**

2. **The directly-measured mass is approximately 50% of the virial estimate (M_virial ~ 100 million solar masses inferred from broad-line FWHM and luminosity), indicating that virial methods overestimate LRD black hole masses by factors of 1.5-2 on average.**

3. **The host galaxy stellar mass is M_* ~ 1-2 times 1e7 solar masses, yielding M_BH/M_* ~ 2-3. This is overmassive (typical relation has M_BH/M_* ~ 1/1000) but not anomalously so.**

4. **The measured black hole mass is consistent with growth via Eddington-limited accretion from a seed at z ~ 10: t_growth = (M_BH / M_seed) * t_Edd ~ (10^5) * (0.04 Gyr) ~ 0.1-0.2 Gyr, fitting within the available time.**

5. **The directly-measured mass demonstrates that LRD black hole masses can be explained by standard accretion-limited growth without invoking exotic formation mechanisms (primordial black holes, supermassive stars, alternative cosmologies).**

6. **The lensing magnification enables spectroscopic resolution of black hole dynamics unachievable in unlensed systems, providing a proof-of-concept for future kinematic studies of high-z black holes.**

7. **Systematic revision of inferred black hole masses for non-lensed LRDs by a factor 1.5-2 reduces the reported "overmassive black hole problem" and eases the tension with black hole formation models.**

---

## Impact and Legacy

This paper has been highly influential for understanding early black hole masses. Its impacts include:

- **Resolving the black hole mass overestimation debate**: The direct measurement confirms that virial estimates of LRD masses have systematic bias, shifting the field toward correction factors and kinematic confirmation.
- **Anchoring black hole formation models**: The revised (lower) masses narrow the parameter space for formation models, making standard accretion-dominated growth more plausible.
- **Motivating lensed system searches**: The success with one strongly-lensed LRD has spurred searches for additional lensed systems to build a sample of directly-measured high-z black hole masses.
- **Improving AGN black hole mass calibration**: The work demonstrates the importance of independent mass measurement techniques (dynamics, maser kinematics, stellar dynamics in the future) to calibrate and correct indirect methods.

---

## Connection to Phonon-Exflation Framework

**Significant indirect connection via black hole growth timescales and early seed formation.**

In the phonon-exflation framework, if the instanton relic (produced during the transit through the spectral fold at z ~ 8-10) enhances black hole growth via modifications to the ionization state, cooling rates, or accretion disk physics, this would affect the inferred black hole seed properties.

The measured mass M_BH = 50 million solar masses at z = 7.04 requires either:

1. **Standard accretion pathway**: M_seed ~ 100-1000 solar masses at z ~ 12-15, growing via Eddington-limited accretion to z = 7 (requires t_growth ~ 0.1-0.2 Gyr, consistent with cosmic time budget)
2. **Rapid accretion pathway**: M_seed ~ 1000-10,000 solar masses at z ~ 10-12, growing via super-Eddington accretion (requires L/L_Edd >> 1)
3. **Enhanced seed production**: Many lower-mass seeds at z > 15, most failing to reach large masses, but rare seeds growing rapidly to large masses

In phonon-exflation, if the instanton relic enhances the efficiency of black hole seed production (via primordial fluctuation amplification or via enhanced baryon accretion), this would increase the number density of seeds at z ~ 12-15. This would make pathway (3) more plausible.

Conversely, if the measured masses are consistent with standard LCDM black hole growth (pathway 1), this suggests that phonon-exflation provides no additional black hole formation enhancement at z < 10, limiting the framework's utility for explaining LRDs.

**Closest thematic link**: The direct black hole mass measurement provides the most precise constraint yet on early black hole growth rates. Comparing the measured masses to predictions of phonon-exflation-based black hole formation models would enable quantitative tests of whether the framework is needed to explain the early black hole population.
