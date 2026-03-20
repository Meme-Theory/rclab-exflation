# Dust Budget Crisis in Little Red Dots

**Author(s):** Kejian Chen, Zhengrong Li, Kohei Inayoshi, Luis C. Ho

**Year:** 2025

**Journal:** arXiv:2505.22600

---

## Abstract

The Little Red Dots (LRDs) discovered by JWST exhibit optical-to-infrared colors that suggest significant dust extinction (A_V > 2-3 mag in naive interpretations), yet ALMA observations and JWST MIRI photometry reveal anomalously faint far-infrared and millimeter continua inconsistent with the expected dust mass implied by such optical reddening. This work reconciles the discrepancy via detailed spectral energy distribution (SED) fitting, constraining the visual extinction to A_V = 0.5-1.5 mag, lower than initially inferred from color arguments alone. We show that the apparent reddening arises from a combination of dust (A_V ~ 0.5 mag) and warm gas cocoon emission (rest-frame optical continuum from super-heated gas layers), not from dust extinction alone. The dust budget crisis—a tension between required dust mass and observed far-infrared non-detections—is resolved by rejecting the high-extinction hypothesis. Instead, LRDs are dust-moderate systems enshrouded in optically thick gas layers, consistent with photon-trapping models and dense outflow geometries. The result has implications for black hole growth timescales, AGN feedback efficiency, and the nature of early black holes.

---

## Historical Context

The optical-to-infrared colors of LRDs (red in rest-frame optical, faint in rest-frame ultraviolet) naturally suggested dust extinction as the cause. Early JWST observations interpreted the reddening via simple dust models:

$$F_\lambda^{\text{obs}} = F_\lambda^{\text{intrinsic}} \times 10^{-0.4 A_\lambda}$$

where $A_\lambda$ is the wavelength-dependent extinction (following Galactic reddening law, calibrated by Cardelli et al.). High visual extinction (A_V = 2-3 mag) was inferred.

However, the dust mass implied by such extinction—$M_{\text{dust}} = 0.01-0.1 M_*$ (assuming gas-to-dust ratio ~ 100-150)—seemed inconsistent with the observed far-infrared and millimeter non-detections from ALMA. If LRDs contain such large dust masses, the thermal re-radiation of absorbed UV and optical light should produce strong far-infrared continua (rest-frame wavelengths 30-300 micrometers).

The detection of typical LRDs at rest-frame 160 micrometers (JWST MIRI) was surprisingly faint: L_FIR ~ 1e11 solar luminosities, compared to expected L_FIR ~ 1e12 solar luminosities if A_V > 2 mag. ALMA observations at 1.2 mm and 3 mm showed similar deficits relative to expectation.

This "dust budget crisis" spurred investigation: either the dust masses are lower than optical colors suggest, or the dust properties are unusual (e.g., dust at temperatures lower than standard models predict, or dust with anomalous emissivity).

---

## Key Arguments and Derivations

### Spectral Energy Distribution (SED) Modeling

The observed flux density at wavelength lambda and redshift z is:

$$F_\nu^{\text{obs}} = \frac{1}{4\pi d_L^2 (1+z)} \int_0^\infty d\nu' \, \epsilon(\nu') L_\nu'(\nu') \, T(\nu'; A_V, R_V)$$

where:
- $L_\nu'$ is the luminosity per unit frequency (rest-frame, in the AGN rest frame)
- $\epsilon(\nu')$ is the emissivity (dust and gas continua)
- $T(\nu'; A_V, R_V)$ is the dust transmission (depends on A_V and R_V, the wavelength-dependent reddening parameter)
- $d_L$ is the luminosity distance

The AGN continuum $L_\nu'(\nu')$ is typically parameterized as a broken power law:
- **UV-optical** (1000-5000 Angstroms, rest): $L_\nu \propto \nu^{-0.5}$ (from accretion disk hot inner regions)
- **Infrared** (5-100 micrometers): $L_\nu \propto \nu^{-2}$ (from dust-heated regions, re-radiation)

For LRDs, the SED exhibits an anomaly: the optical continuum is relatively strong (no UV-optical break as expected for heavily extincted sources), but the infrared is faint. This suggests the "blue" (non-reddened) optical/NUV and the "red" color are not due to dust extinction alone.

### Dust Extinction Model vs. Gas Cocoon Emission

If dust extinction with A_V = 2.5 mag were the cause, the transmission function is:

$$T(\nu) = \exp\left(-0.4 \, A_V \times \frac{f(\lambda)}{\lambda}\right)$$

where $f(\lambda)$ is the extinction curve shape parameter (varies with wavelength and dust properties). For Milky Way dust with A_V = 2.5 mag:
- At 1000 Angstroms (UV): T ~ 0.1 (strong attenuation)
- At 5000 Angstroms (optical): T ~ 0.3-0.5 (moderate attenuation)
- At 10 micrometers (infrared): T ~ 1.0 (transparent)

The thermal re-radiation of absorbed energy would produce:

$$L_{\text{FIR}} = \int (1 - T(\nu)) L_\nu(\nu) d\nu$$

For A_V = 2.5 mag and luminosity L_UV ~ 1e12 solar luminosities, this predicts L_FIR ~ 1e12 solar luminosities. Observed LRD far-infrared luminosities are typically L_FIR ~ 0.1-1.0 times this prediction—a factor 10-100 deficit.

An alternative interpretation is that the reddening comes from gas cocoon emission (warm gas photoionized by the AGN continuum, not dust extinction). The optical continuum in this case arises from:
- **Central accretion disk**: Hot (T ~ 1e4-1e5 K), blue continuum, small flux
- **Gas cocoon photosphere**: Warm (T ~ 1e3-1e4 K), red continuum, large flux

The combined SED naturally produces a "red in optical, blue in UV" appearance without requiring high dust extinction. The dust mass is constrained to A_V ~ 0.5-1.0 mag (enough to scatter and redden the small blue inner disk light, but not enough to dominate the optical continuum).

### Dust Mass Estimates from FIR-to-Optical Ratio

The dust mass can be estimated from the far-infrared luminosity and dust temperature:

$$M_{\text{dust}} = \frac{L_{\text{FIR}}}{4\pi B_\nu(T_{\text{dust}}) \kappa_\nu}$$

where:
- $B_\nu(T_{\text{dust}})$ is the Planck function at dust temperature T_dust
- $\kappa_\nu$ is the dust mass absorption coefficient (cm^2/g)

For typical AGN dust (a mix of silicates and graphites), $\kappa_\nu$ ~ 0.1 cm^2/g at 100 micrometers. For L_FIR ~ 1e11 solar luminosities and T_dust ~ 40-60 K:

$$M_{\text{dust}} \sim 1e6 - 1e7 M_\odot$$

This is consistent with modest dust masses, or equivalently A_V ~ 0.5-1.5 mag if the dust is distributed throughout the system.

In contrast, the dust mass implied by high visual extinction (A_V = 2.5 mag) and standard gas-to-dust ratio is:

$$M_{\text{dust}} \sim \frac{A_V}{1.86 \times 10^{-22}} \sim 1e7 - 1e8 M_\odot$$

(factor 10x higher). The FIR observations and ALMA constraints favor the lower dust mass scenario.

### ALMA Constraints

ALMA observations at 1.2 mm (rest-frame ~ 200 micrometers at z~6) provide millimeter continuum fluxes. For a dust temperature T ~ 40 K and mass M_dust ~ 1e7 solar masses, the predicted flux at 1.2 mm is:

$$F_{1.2 \text{ mm}} = \frac{M_{\text{dust}} \kappa_\nu B_\nu(40\text{ K})}{4\pi d_L^2}$$

For a z = 6 source at 1e-2 mJy ALMA sensitivity, the predicted flux for high M_dust is 0.1-1 mJy (easily detectable). ALMA observations yield upper limits F_1.2mm < 0.01-0.05 mJy, constraining M_dust < 1e7 solar masses.

This is consistent with dust masses from FIR fitting and argues against the high-extinction (A_V > 2 mag) scenario.

---

## Key Results

1. **Visual extinction in LRDs is constrained to A_V = 0.5-1.5 mag via joint fitting of JWST optical/infrared, Herschel, and ALMA observations, lower than initially inferred from optical-to-UV color ratios alone.**

2. **The far-infrared luminosity of LRDs (L_FIR ~ 1e10-1e11 solar luminosities) is insufficient to explain dust masses implied by high visual extinction (A_V > 2.5 mag), indicating that the reddening is NOT due to dust extinction alone.**

3. **Dust masses are constrained by ALMA millimeter observations to M_dust ~ 0.1-1.0 times 1e7 solar masses, requiring only moderate dust columns that are consistent with optically thick gas cocoons rather than heavily dust-obscured systems.**

4. **The optical-to-ultraviolet color of LRDs arises from a combination of dust attenuation (A_V ~ 0.5 mag) and warm gas cocoon emission, not from dust extinction alone.**

5. **The "dust budget crisis" is resolved by rejecting high dust extinction (A_V > 2 mag) and adopting the gas cocoon model, where the optical continuum is dominated by warm gas photospheres rather than direct disk light.**

6. **LRDs are dust-moderate systems with properties consistent with dense, optically thick outflows and gas cocoons, supporting photon-trapping interpretations of the non-variability observed in separate papers.**

7. **The low dust mass and moderate extinction have implications for AGN feedback: if LRDs are not heavily dust-obscured, then radiation-driven winds may be less efficient, and momentum-driven outflows dominate.**

---

## Impact and Legacy

This paper has become essential for understanding LRD dust and gas properties. Its impacts include:

- **Constraining dust via multi-wavelength SED fitting**: The result demonstrates the importance of joint FIR and millimeter constraints for breaking degeneracies in dust extinction models.
- **Supporting photon-trapping models**: Low dust masses and moderate extinction are consistent with dense gas cocoons (not dust cocoons) as the source of photon trapping.
- **Resolving AGN feedback physics**: Rejection of heavily dust-obscured models implies radiation-driven winds are less effective in LRDs, shifting emphasis to momentum-driven outflows.
- **Informing dusty AGN demographics**: The result that LRDs are not part of the heavily-obscured AGN population (like Compton-thick AGN) suggests they represent a distinct evolutionary phase.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

The dust budget crisis and its resolution (moderate dust masses, gas cocoon dominance) are observational constraints on AGN accretion physics independent of cosmological framework. Both LCDM and phonon-exflation predict similar AGN physics for black holes at z ~ 4-8 (as long as the expansion histories remain degenerate, which they do at z < 7).

However, if future observations establish that LRDs are predominantly non-dust-obscured systems with optically thick gas outflows, this constrains the AGN feedback physics. In the phonon-exflation framework, if the instanton relic (from the spectral fold transit at z ~ 8-10) enhances gas cooling and black hole accretion rate at high z, this would lead to denser gas cocoons and stronger outflows. The dust masses and FIR properties could thus become distinctive signatures of phonon-exflation vs. LCDM.

**Closest thematic link**: The dominance of gas cocoons over dust in LRDs suggests that gas dynamics (cooling, accretion, outflow) are more important than dust at high redshifts. In phonon-exflation, the instanton relic may affect cooling via modifications to the ionization state or via enhanced density perturbations. Testing such predictions requires detailed hydrodynamic simulations of gas cocoons in phonon-exflation vs. LCDM.
