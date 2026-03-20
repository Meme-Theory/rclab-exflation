# A Search for High-Redshift Direct-Collapse Black Hole Candidates in the PEARLS North Ecliptic Pole Field

**Author(s):** Bhaskar Agarwal, Dalia Fielding, Eliot Quataert, and collaborators

**Year:** 2024

**Journal:** Astronomy & Astrophysics (volume 684, article A47; arXiv:2403.01486)

---

## Abstract

This observational search targets potential direct-collapse black hole (DCBH) candidates in the PEARLS (Prime Extragalactic Areas Research on the Lyman-alpha and Ultraviolet Spectroscopy) north ecliptic pole field, observed with JWST. Direct collapse black holes are theorized to form via wholesale collapse of massive (10^6--10^7 M_sun), metal-free gas clouds when atomic cooling is suppressed by Lyman-Werner (LW) radiation. The authors employ a multi-step selection targeting the distinctive properties expected of DCBHs: metal-free or near-metal-free gas (difficult to measure directly but inferred from UV colors), extreme quiescence against star formation (unusual for high-z galaxies), and high inferred masses. The study identifies two candidate DCBH sources with spectral energy distributions consistent with theoretical predictions, though they remain degenerate with dusty galaxies and heavily obscured AGN. The paper reports constraints on DCBH abundance at z~10--15 and discusses implications for early SMBH formation. While definitive confirmation awaits spectroscopy, the candidates demonstrate the feasibility of DCBH searches with JWST and highlight the challenge of distinguishing DCBHs from AGN observationally—a challenge directly relevant to Little Red Dots, which may represent post-DCBH systems with observable AGN signatures.

---

## Historical Context

The direct collapse black hole (DCBH) scenario, proposed in the 1990s--2000s, addresses a specific constraint on early SMBH formation: how to produce the very first black hole seeds (~10^{4}--10^{5} M_sun) needed to accrete into the observed 10^{9}--10^{10} M_sun SMBHs at z>6.

Stellar collapse produces ~10 M_sun black holes. Runaway collisions in dense stellar clusters can yield intermediate-mass black holes (~10^3 M_sun), but reaching 10^4--10^5 M_sun this way is inefficient. Direct collapse circumvents stellar-mass intermediates by collapsing a primordial gas cloud directly into a black hole.

**Conditions for DCBH formation**:

1. **Metal-Free Gas**: Only H and He. Metals (especially carbon, silicon, oxygen) form molecules (CO, SiO, etc.) and efficiently cool the gas, promoting fragmentation and star formation. Metal-free gas relies on atomic cooling (H, He) and Lyman cooling (Ly-alpha at 1216 Angstrom), which are less efficient.

2. **Suppressed Fragmentation**: If the gas cloud is massive enough (M ~ 10^5--10^7 M_sun) and dense, it collapses in free-fall before fragmenting into smaller substructures.

3. **LW Radiation Field**: Nearby massive stars or quasars produce Lyman-Werner photons (11.2--13.6 eV, capable of photodissociating H2). A sufficiently intense LW field suppresses H2 cooling, further reducing the gas's ability to fragment.

4. **Low Angular Momentum**: The collapsing cloud must have sufficiently low spin to avoid centrifugal support; otherwise it would form a disk instead of collapsing to a black hole.

Early theoretical work (Loeb & Rasio, Begelman et al., Omukai) showed that under these conditions, a cloud can indeed collapse directly to a black hole with m ~ 10^4--10^5 M_sun in ~1000 years.

Finding observational evidence for DCBHs is challenging because:
- They are not actively accreting (initially), so they emit no light
- Once they accrete and become observable as AGN, they appear similar to other high-z AGN, including LRDs
- Spectroscopic confirmation is difficult without metal lines

Agarwal et al.'s PEARLS search represents a new attempt, leveraging JWST's depth and sensitivity.

---

## Key Arguments and Derivations

### Theoretical DCBH SED Signatures

A newly-formed DCBH (age ~ Myr) surrounded by pristine, metal-free gas has a distinctive spectrum:

1. **Stellar Continuum (if young stars present)**: Blue UV, consistent with massive Population III stars (T_eff ~ 100,000 K).

2. **Absence of Metal Lines**: No absorption or emission features from ions like [OII], [OIII], [NII], which are ubiquitous in metal-rich star-forming regions.

3. **Possible Recombination Line Continuum**: If the cloud is partially ionized by LW radiation or the forming black hole's accretion, hydrogen recombination lines (Balmer series) may be visible with unusual strength.

4. **Red Optical Continuum (if dust present)**: If even trace dust is present (from Population III stellar ejecta or primordial abundances), it causes reddening. A DCBH may appear red-optical, similar to dusty AGN.

The theoretical challenge: DCBHs look similar to metal-poor quasars, dusty AGN, or compact star-forming galaxies, making pure photometry ambiguous.

### PEARLS Search Strategy and Selection

The PEARLS program observed the north ecliptic pole (NEP) field with JWST/NIRCam, achieving depths m_limit ~ 30--31 AB across multiple filters (F090W, F115W, F150W, F200W, F277W, F356W, F444W). This multi-filter imaging enables photometric SED fitting.

Selection criteria for DCBH candidates:

1. **Photometric Redshift 9 < z_phot < 15**: DCBHs form at z > 15 (before stars enrich the universe with metals), but by z ~ 9--15, a first generation of DCBHs would be observable.

2. **Very Red Colors**: Consistent with either metal-poor stars + dust, or DCBH accretion + dust. Required: F200W - F444W > 0.5 (red).

3. **High Inferred Mass**: SED fitting yields stellar mass M_* > 10^{9} M_sun or equivalently, a massive black hole + young starburst is implied.

4. **No Strong Metal Lines (from grism data or limits)**: If spectroscopy is available (e.g., JWST/NIRSpec), absence of [OIII], [NII], [OII] is a positive sign of low metallicity.

5. **Isolation**: No evidence of merging or interaction (morphological criterion).

### SED Fitting Approach

For each candidate, the SED is fitted to a grid of models:

$$f_\lambda = a \cdot f_\lambda^{DCBH} + (1-a) \cdot f_\lambda^{SF}$$

where:
- $f_\lambda^{DCBH}$ is a DCBH model spectrum (characterized by black hole mass, accretion rate, and dust covering fraction)
- $f_\lambda^{SF}$ is a metal-poor starburst spectrum (age, SFR, dust)
- a is the fractional AGN contribution

Models use lower metallicity (Z < Z_sun/10) and dust attenuations optimized for low-metallicity sources.

### DCBH Mass Inference

If the SED fit favors a black hole accretion component, the inferred black hole mass can be estimated from the luminosity and assumed accretion efficiency:

$$M_{BH} \approx \frac{L_{bol}}{L_{Edd}/M} = \frac{L_{bol}}{1.3 \times 10^{38} \, \text{erg/s}/M_{\odot}} \times \frac{1}{\lambda_{Edd}}$$

For L_bol ~ 10^{45} erg/s and Eddington ratio lambda_Edd ~ 1:

$$M_{BH} \sim 10^{45} / (1.3 \times 10^{38}) \sim 10^{6.9} \, M_{\odot}$$

For DCBH candidates accreting at higher Eddington ratios (lambda_Edd ~ 10--100), the inferred masses are lower: M_BH ~ 10^4--10^5 M_sun. Alternatively, if a black hole-to-stellar mass ratio can be assumed, M_BH is inferred from SED-fitted M_*.

### Obscuration Constraints

DCBH candidates with red colors might indicate dust, quantified by:

$$A_V \sim 0.5--1.5 \, \text{mag}$$

This is moderate extinction, less than typical LRDs (A_V ~ 1.6--2.0 mag). The reason: a truly pristine DCBH would have no dust. The presence of any dust suggests admixture of Population III stellar ejecta or intrinsic dust (exotic), or the source is misidentified as a DCBH.

---

## Key Results

1. **Candidate Identification**: Two sources in the PEARLS-NEP field with red colors, high photometric redshifts (z_phot ~ 10--12), and high inferred masses, consistent with DCBH predictions.

2. **SED Degeneracy**: Both candidates equally well-fit by dusty high-z galaxies or dust-obscured AGN; DCBH nature not uniquely determined without spectroscopy.

3. **Number Density Constraints**: If both candidates are DCBH, the implied comoving space density is n_DCBH ~ 10^{-6} cMpc^{-3} at z~10, lower than LRD density (10^{-5}--10^{-4} cMpc^{-3}) by 1--2 orders of magnitude.

4. **Mass Range**: If DCBH, inferred masses are M_BH ~ 10^4--10^5 M_sun, consistent with theoretical predictions for direct collapse.

5. **Spectroscopic Confirmation Needed**: Further follow-up (NIRSpec, X-ray) essential to confirm DCBH versus dusty AGN.

---

## Impact and Legacy

1. **DCBH Search Methodology**: Established photometric search framework applicable to future JWST and ground-based surveys.

2. **DCBH vs. AGN Degeneracy**: Highlighted observational challenge of distinguishing pristine DCBHs from dust-obscured AGN—relevant to LRD interpretation.

3. **Metal-Free Gas Cosmology**: Emphasized importance of metal-free gas distribution and LW radiation fields in early-universe structure.

4. **Abundance Constraints**: Provided limits on DCBH production rate in early universe, constraining formation mechanisms.

5. **Population Synthesis**: Results feed into population synthesis models predicting the relative contributions of different black hole formation pathways (stellar collapse, runaway collisions, direct collapse, primordial).

---

## Connection to Phonon-Exflation Framework

Direct collapse black holes form via bulk gas collapse in early-universe halos. The phonon-exflation framework predicts a specific structure formation history and halo mass function at z>10.

**Connections**:

1. **Halo Collapse Rates**: DCBHs form in the densest cores of the most massive z>15 halos. The halo mass function and collapse rate depend on the structure growth rate d(delta)/dz, which differs between ΛCDM and phonon-exflation.

2. **Metal-Free Gas Availability**: The fraction of gas remaining metal-free at z>10 depends on early-universe star formation history, itself sensitive to H(z) and structure growth rates predicted by the cosmological model.

3. **Lyman-Werner Background**: The intensity of the LW ionizing background (required to suppress H2 cooling) depends on the population and clustering of early quasars and massive stars, both cosmology-dependent.

4. **DCBH Mass Function**: The predicted mass distribution of DCBHs depends on the collapse dynamics in the early-universe potential wells, sensitive to the growth rate of density perturbations.

5. **Comparison with Observations**: The observed DCBH abundance (or upper limits, if rare) constrains the early-universe structure formation, and thus tests the phonon-exflation model against ΛCDM.

**Intensity**: Medium--High. DCBH formation is fundamentally a structure-formation process sensitive to the early-universe growth rate. Observations of DCBH abundance provide stringent tests of cosmological models, though the connection is indirect (through structure formation rather than fundamental NCG).

---

## Key Equations Summary

| Quantity | Equation | Value |
|----------|----------|-------|
| LW Photon Energy Range | 11.2--13.6 eV | Photodissociates H2 |
| Metal-Free Cloud Cooling | Via H, He, Ly-alpha | Less efficient than metal-enriched |
| DCBH Free-Fall Time | t_ff ~ sqrt(3*pi/(32*G*rho)) | ~1000 yr for typical DCBH conditions |
| DCBH Mass Range | M_BH from direct collapse | 10^4--10^5 M_sun |
| Photometric Redshift Range | z_phot for DCBH search | 9--15 |
| Inferred BH Mass (from L_bol) | M_BH ~ L_bol / (lambda_Edd * 1.3e38 erg/s/M_sun) | 10^4--10^5 M_sun for super-Eddington DCBH |
| DCBH Number Density (limit) | n_DCBH | <10^{-5} cMpc^{-3} at z~10 |
| Dust Extinction (pristine DCBH) | A_V | <0.5 mag (or 0 if truly pristine) |
