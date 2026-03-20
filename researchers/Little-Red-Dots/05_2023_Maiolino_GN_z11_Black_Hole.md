# A Small and Vigorous Black Hole in the Early Universe

**Author(s):** Roberto Maiolino, Sandro Tacchella, Michele Perna, Emma Curtis-Lake, and 35 co-authors

**Year:** 2024 (arXiv preprint May 2023)

**Journal:** Nature (volume 627, pages 59--63, January 2024; arXiv:2305.12492)

---

## Abstract

This landmark paper presents JWST/NIRSpec spectroscopy of GN-z11, a galaxy at redshift z=10.6 (cosmic age ~ 440 Myr after the Big Bang), revealing the presence of an accreting black hole in the early universe. Unlike previous claims of massive black holes at z>6 based on limited spectroscopic evidence, this study provides definitive detection through multiple independent diagnostics: rest-frame optical AGN emission lines ([NeIV], [NeV], [OII]), broad Hα (FWHM ~ 1000--2000 km/s, though narrower than some LRDs), and critically, semi-forbidden lines ([OII]*1663) diagnostic of high electron density (n_e > 10^9 cm^{-3}) characteristic of the broad-line region. Detailed analysis yields M_BH ~ 1.6 × 10^6 M_sun, substantially lower than anticipated from extrapolation of local black hole--bulge scaling relations but consistent with rapid black hole growth scenarios. The broad CIV1549 absorption trough indicates an AGN-driven outflow with velocity v ~ 800--1000 km/s, demonstrating that even modest black holes drive significant feedback in the early universe. The paper establishes GN-z11 as the most distant, and thus earliest, black hole with robust spectroscopic confirmation.

---

## Historical Context

Prior to JWST, claims of massive black holes at z>6 relied on either (1) broad-band photometric fits implying large stellar masses and, by extension, large black holes (with M_BH/M_* assumed local), or (2) X-ray detections with limited spectral information. A notable example is SDSS J1148+5251 at z=6.4, identified as hosting a black hole of M_BH ~ 3 × 10^{9} M_sun based on broad MgII and CIV line spectroscopy, but subsequent scrutiny revealed uncertainties in redshift and mass estimates.

GN-z11 itself was identified as a high-z candidate from photometric redshifts in GOODS-N deep imaging from Hubble and Spitzer, initially placed at z ~ 11. Early photometric SED fitting suggested an old stellar population with high stellar mass (M_* ~ 10^{11} M_sun), implying (via local M_BH--M_* scaling) a very massive black hole M_BH ~ 10^{9}--10^{10} M_sun. However, photometric redshifts and stellar mass estimates have large uncertainties at such distances.

JWST's on-orbit performance in 2022--2023 enabled spectroscopic follow-up of ultra-high-z candidates. The JWST/NIRSpec GTO programs (including JADES, PIs: D. Eisenstein, N. Luetzgendorf, and others), targeting GOODS fields, included GN-z11. Maiolino's team obtained deep prism-mode spectroscopy covering rest-frame optical wavelengths (lambda_rest ~ 3000--6000 Angstrom) across two epochs (Feb and May 2023), providing unprecedented sensitivity to faint AGN lines.

---

## Key Arguments and Derivations

### Spectroscopic Data: Detection of AGN Lines

JWST/NIRSpec/PRISM observations in MSA mode achieved wavelength coverage lambda_obs ~ 0.6--5.3 μm (rest-frame optical at z=10.6). Critical detections include:

1. **[NeIV]2423**: Semi-forbidden line emitted by Ne^{3+} ions, highly ionized. Presence indicates high-energy ionization (typical of AGN, not star formation).
2. **CII*1335**: Semi-forbidden carbon line, lower ionization than [NeIV].
3. **[OII]*1663**: Semi-forbidden oxygen line, critical for density diagnostic (see below).
4. **Broad Hα (6563 Angstrom rest)**: Detected with FWHM ~ 1000--2000 km/s (narrower than typical SDSS quasars but broader than narrow-line regions).

Detection of multiple AGN-diagnostic lines (especially [NeIV]) conclusively identifies GN-z11 as AGN-powered.

### Gas Density Diagnostic

Semi-forbidden lines have critical densities n_crit, above which collisional de-excitation dominates and the line is suppressed. The [OII]*1663 line has n_crit ~ 10^7 cm^{-3}, while [OIII]* has n_crit ~ 10^9 cm^{-3}. Detection of [OIII]* despite suppression by collisional de-excitation implies high density:

$$n_e >> n_{crit} \sim 10^9 \, \text{cm}^{-3}$$

This density is highly diagnostic of the broad-line region (BLR), where electrons are bound to black holes via gravitational potential and crowded into small volumes. By contrast, typical narrow-line regions have n_e ~ 10^2--10^4 cm^{-3}.

### Black Hole Mass Estimate

Several methods yield consistent M_BH:

**Method 1: Hα Line Width and Luminosity**

Using the virial relation (Eqn. 1 above) with Delta v ~ 1200 km/s (from Hα FWHM) and R_BLR derived from L_Halpha:

$$\log(R_{BLR} / \text{light-days}) = 0.513 \log(L_{Halpha}) - 7.02$$

yields R_BLR ~ 1--5 light-days ~ 10^{15}--10^{16} cm. With Delta v ~ 1.2 × 10^8 cm/s:

$$M_{BH} \approx 0.3 \times \frac{(1.2 \times 10^8)^2 \times 10^{15.5}}{6.67 \times 10^{-8}} \approx 10^6 \, M_{\odot}$$

**Method 2: Semi-forbidden Line Diagnostic**

The balance between collisional excitation and radiative decay of [OIII]* constrains density, and the line flux compared to nearby transitions constrains the ionization parameter U and distance to the ionizing source, yielding R_BLR and hence M_BH ~ (1--2) × 10^6 M_sun.

Both methods agree: M_BH ~ (1--2) × 10^6 M_sun.

### Outflow Kinematics

The rest-frame CIV1549 line shows a deep, blueshifted absorption trough, indicating an outflow along the line of sight. The velocity is:

$$v_{out} = c \cdot \frac{\Delta \lambda}{\lambda_0} \sim 800--1000 \, \text{km/s}$$

Outflows at this velocity are characteristic of AGN-driven winds, powered by radiation pressure or mechanical winds from the accretion disk. The presence of outflow indicates the black hole is not gravitationally quiescent but actively couples to the surrounding gas.

### Accretion Rate and Eddington Ratio

The accretion luminosity (from ionizing photon flux needed to maintain the observed ionization state) is:

$$L_{acc} \approx 10^{44}--10^{45} \, \text{erg/s}$$

The Eddington luminosity for M_BH ~ 1.6 × 10^6 M_sun is:

$$L_{Edd} = 1.3 \times 10^{38} \left(\frac{M_{BH}}{M_{\odot}}\right) \approx 1.3 \times 10^{38} \times 1.6 \times 10^{6} \approx 2.1 \times 10^{44} \, \text{erg/s}$$

Thus the Eddington ratio is:

$$\lambda_{Edd} = \frac{L_{acc}}{L_{Edd}} \sim 1--10$$

indicating near-Eddington to super-Eddington accretion.

### Cosmic Age and Black Hole Assembly

At z=10.6, the cosmic age is:

$$t(z) \approx \frac{2}{3H_0(1+z)^{3/2}} \approx 0.44 \, \text{Gyr}$$

For a black hole to reach M_BH ~ 1.6 × 10^6 M_sun within ~ 0.44 Gyr requires very rapid assembly. Starting from a stellar-collapse seed (m ~ 10 M_sun), continuous Eddington-limited accretion yields:

$$M_{BH}(t) = m_0 \exp(t / t_Edd)$$

where t_Edd ~ 0.5--1 Gyr is the Eddington timescale. To reach 10^6 M_sun:

$$\ln(10^6/10) = 11.5 \approx 0.44 / t_{Edd}$$

gives t_Edd ~ 0.04 Gyr, implying super-Eddington accretion or earlier seeding with intermediate-mass black holes (~10^3--10^4 M_sun).

---

## Key Results

1. **Redshift Confirmation**: Spectroscopic redshift z=10.6 confirmed via multiple emission lines (previously photometric z~11).

2. **Black Hole Detection**: Definitively established AGN presence via [NeIV], [OII]*, and other lines diagnostic of high ionization.

3. **Black Hole Mass**: M_BH ~ 1.6 × 10^6 M_sun, substantially lower than photometric estimates but consistent with some seed black hole scenarios.

4. **Gas Density**: Semi-forbidden lines indicate n_e > 10^9 cm^{-3}, confirming broad-line region conditions.

5. **Outflow**: CIV1549 absorption at v ~ 800--1000 km/s evidences AGN-driven wind.

6. **Eddington Ratio**: lambda_Edd ~ 1--5, indicating rapid accretion.

7. **Earliest Spectroscopic AGN**: At z=10.6, this is the most distant robustly-confirmed AGN, constraining black hole formation timescales to <0.5 Gyr.

---

## Impact and Legacy

1. **Spectroscopic Gold Standard**: GN-z11 became the benchmark for high-z AGN spectroscopy, with its detailed line diagnostics serving as templates for other z>6 sources.

2. **Black Hole Growth Timescale Constraint**: Demonstrated that black holes must form very early (z>15) or accrete super-Eddington rates, ruling out some formation scenarios.

3. **Outflow Discovery**: Confirmed that even modest-mass black holes drive significant outflows in the early universe, relevant to black hole--galaxy co-evolution.

4. **AGN Feedback at High-z**: Suggested that AGN feedback operates at z~10, affecting galaxy assembly and potentially contributing to reionization.

5. **JWST Spectroscopy Validation**: Showcased the power of JWST/NIRSpec for deep spectroscopic analysis of faint, high-z sources.

---

## Connection to Phonon-Exflation Framework

GN-z11 probes the universe at z=10.6 (t ~ 0.44 Gyr), in the very early cosmic epoch. The phonon-exflation framework makes predictions about expansion history, structure growth rates, and cosmic parameters at this epoch.

**Connections**:

1. **Black Hole Formation Timescale**: The requirement to form/grow M_BH ~ 10^6 M_sun by z=10.6 constrains the early-universe star formation efficiency and halo collapse timescales. Phonon-exflation's prediction of H(z) and density contrast growth d(delta)/dz affects the availability of gas and black hole seeds.

2. **Reionization Contribution**: GN-z11, as a representative high-z AGN, contributes ionizing photons to the reionization process. The phonon-exflation model's prediction of reionization epoch and ionizing photon sources would be constrained by the abundance of z~10 black holes.

3. **Structure Formation Rates**: The ease with which halos form and collapse (affecting black hole formation) depends on the predicted growth rate of density perturbations—a key discriminator between cosmological models.

4. **Early Universe Parameters**: H(z), rho(z), and T(z) at z~10 directly affect the feasibility of rapid black hole growth and galaxy assembly.

**Intensity**: Medium--High. GN-z11 provides direct empirical constraints on black hole formation and early-universe structure formation at z~10, a regime crucial for testing cosmological models including phonon-exflation.

---

## Key Equations Summary

| Quantity | Equation | GN-z11 Value |
|----------|----------|---------|
| Broad Hα Line Width | FWHM (from spectrum) | ~ 1000--2000 km/s |
| Black Hole Mass (virial) | $M_{BH} = f \cdot \Delta v^2 \cdot R_{BLR} / G$ | ~ 1.6 × 10^6 M_sun |
| BLR Radius | $\log(R_{BLR}/\text{ld}) = 0.513 \log(L_Halpha) - 7.02$ | ~ 1--5 light-days |
| Gas Density (semi-forbidden) | n_e from line balance | > 10^9 cm^{-3} |
| Outflow Velocity | v = c * Delta lambda / lambda_0 | ~ 800--1000 km/s |
| Eddington Luminosity | $L_{Edd} = 1.3 \times 10^{38} (M_{BH}/M_{\odot})$ erg/s | ~ 2.1 × 10^{44} erg/s |
| Eddington Ratio | lambda_Edd = L_acc / L_Edd | ~ 1--5 |
| Cosmic Age at z=10.6 | t = 2/(3*H_0*(1+z)^1.5) | ~ 0.44 Gyr |
| Redshift | z | 10.6 |
