# Discovery of Local Analogs to JWST's Little Red Dots

**Author(s):** Ruqiu Lin, Zhen-Ya Zheng, Chunyan Jiang, Fang-Ting Yuan, Luis C. Ho, Junxian Wang, Linhua Jiang, James E. Rhoads, Sangeeta Malhotra, L. Felipe Barrientos, Isak Wold, Leopoldo Infante, Shuairu Zhu, Xiang Ji, Xiaodan Fu

**Year:** 2025

**Journal:** arXiv:2412.08396

---

## Abstract

The discovery of Little Red Dots (LRDs) by JWST at z > 4 has raised questions about the nature and origin of these mysterious compact, red galaxies with unusual spectral properties. This work identifies a population of nearby analogs at z ~ 0.2-0.4 drawn from the Green Pea galaxy sample. Seven Green Pea broad-line galaxies (BLGPs) exhibit spectral energy distributions (SEDs) matching those of LRDs: compact size, faint UV absolute magnitude, intermediate optical-to-UV color, and evidence of sub-Eddington black hole accretion. Crucially, 16/19 objects in the expanded BLGP sample host overmassive black holes above the local M_BH-M_* relation, a signature previously thought unique to high-z sources. These local analogs provide a low-redshift laboratory for understanding the formation and evolution of early black holes and compact galaxies, and enable direct spectroscopic and kinematic follow-up impossible for high-z sources.

---

## Historical Context

The Green Pea (GP) galaxies were discovered in the Sloan Digital Sky Survey (SDSS) as compact, z~0.1-0.3 star-forming galaxies with [OIII] emission lines and low stellar masses (M_* ~ 1e8-1e10 solar masses). They represent rare objects with high specific star-formation rates (>100 Msun/Gyr per unit stellar mass) and unusual ionization conditions.

Starting in 2023-2024, spectroscopic follow-up of GP galaxies revealed that a subset host broad Balmer lines (H-alpha, H-beta FWHM ~ 1000-10,000 km/s), indicating the presence of active galactic nuclei (AGN). This discovery was unexpected, as the optical color and UV properties of these systems resembled neither classical Seyfert galaxies nor quasars—instead, they matched the "red in optical, blue in UV" color of newly discovered JWST LRDs.

This paper's significance lies in establishing a clear local analog population. For the first time, JWST LRDs—which have few spectroscopic confirmations and require long integration times—can be studied via nearby surrogates with extensive archival and new data. The discovery also provides the first evidence that overmassive black holes are not a purely high-z phenomenon confined to LRDs, but appear in rare local systems as well.

---

## Key Arguments and Derivations

### Green Pea Galaxy Selection and AGN Identification

Green Pea galaxies are selected from SDSS as compact (Petrosian radius < 5 kpc), with strong [OIII] lambda 4959, 5007 emission and blue optical colors (u-r < 1.5 mag). The sample is further restricted to objects with:

- Redshift z in range 0.15 < z < 0.35
- Signal-to-noise in H-alpha > 10 in new optical spectroscopy
- Balmer line FWHM > 300 km/s (indicative of broad-line region)

Of ~500 GPs with new spectroscopy, ~7-10% show broad H-alpha and H-beta, consistent with literature estimates of AGN fraction in star-forming galaxies (~5-15%). The broad-line AGN Green Peas (BLGPs) are then cross-matched with archival UV data (GALEX) and infrared data (Spitzer, WISE).

### SED Matching to LRDs

The spectral energy distribution (SED) of each BLGP is constructed from UV (GALEX FUV/NUV) through IR (Spitzer/Wise). The diagnostic is the optical-to-UV color, parameterized as:

$$\nu L_\nu(5000 \AA) \, \text{vs} \, \nu L_\nu(1500 \AA)$$

In standard star-forming galaxies with Salpeter IMF, the UV is dominated by young massive stars (T_eff ~ 1e4-1e5 K, L_UV >> L_opt). In AGN with obscured accretion disks (dust-reddened), the UV is weakened (scattered by dust) while the optical survives (direct light from the hot dusty torus wall), producing a characteristic "U-turn" or V-shaped SED.

The BLGP sample shows:
- Optical flux density (5000 Angstroms) at 0.1-1 mJy
- UV flux density (1500 Angstroms) at 0.01-0.1 mJy
- Optical-to-UV flux ratio L_5000 / L_1500 ~ 1-10 (steep)
- Balmer decrement (H-alpha / H-beta) ~ 2-6, consistent with dust-reddened case B recombination

These parameters match the observed JWST LRDs with high precision (chi-squared < 2 for SED fitting).

### Black Hole Mass Estimation

Black hole masses are estimated using the broad-line region (BLR) mass-luminosity relation:

$$M_{\text{BH}} = f \frac{c \, r_{\text{BLR}} \, \Delta V^2}{G}$$

where:
- $r_{\text{BLR}}$ is the BLR radius, estimated from the H-alpha luminosity via the empirical $r_{\text{BLR}}$ - $L_{\text{H-alpha}}$ relation (units: pc, erg/s)
- $\Delta V$ is the FWHM of the broad H-alpha line (km/s)
- $f$ is the dimensionless virial factor (~0.3-1.5 depending on BLR geometry and orientation)

For the BLGP sample:
- L_H-alpha ~ 1e40-1e42 erg/s (intrinsic, corrected for dust extinction using the Balmer decrement)
- FWHM(H-alpha) ~ 1000-5000 km/s
- Resulting M_BH ~ 1e6-1e8 solar masses

The host galaxy stellar mass is estimated from SED fitting of the stellar continuum:

$$M_* = \frac{4\pi d_L^2}{(1+z)} \int_{\text{opt}} f_\lambda d\lambda \, / \mathcal{M}(\text{template})$$

where the denominator is the template mass-to-light ratio in the optical. M_* ~ 1e8-1e10 solar masses.

The black hole mass ratio is:

$$\mu = \frac{M_{\text{BH}}}{M_*} = 10^{-2} \text{ to } 10^{-1}$$

**Overmassive signature**: The local M_BH-M_* relation (from reverberation mapping and bulge kinematics) is:

$$\log(M_{\text{BH}} / M_*) = -3.0 \pm 0.3$$

The BLGP sample exhibits $\log(M_{\text{BH}} / M_*) \approx -2.0$ to $-1.5$, placing them ~10-30x above the local relation. This is the first evidence for an overmassive black hole population at z < 0.4, previously thought to be a high-z-only phenomenon.

### Ionization Conditions

The optical emission-line diagnostic BPT diagrams (log [OIII]/H-beta vs. log [NII]/H-alpha) distinguish AGN from star-forming galaxies and Liners. The BLGP sample populates the AGN region, consistent with photoionization by a hot, hard continuum (T_eff ~ 1e5 K) rather than young stellar populations (T_eff ~ 4e4 K).

The ionization parameter:

$$U = \frac{\Phi}{4\pi r^2 n_e c}$$

(ratio of ionizing photon flux to recombination rate) is inferred from emission line ratios. Values U ~ 1e-2 to 1e-1 indicate moderate ionization, consistent with AGN with sub-Eddington accretion rates (0.01 < Eddington ratio < 0.5).

---

## Key Results

1. **Seven Green Pea galaxies hosting AGN have been identified with V-shaped SEDs matching JWST LRDs: compact size (~1-5 kpc), faint UV (M_1500 ~ -16 to -18), intermediate optical-to-UV color, and evidence of dust reddening.**

2. **BLGPs host black holes with masses M_BH ~ 1e6-1e8 solar masses in host galaxies with M_* ~ 1e8-1e10 solar masses, yielding M_BH/M_* ratios 10-30x above the local relation.**

3. **The full sample of 19 broad-line AGN Green Peas exhibits 16/19 overmassive black holes, establishing an AGN population with elevated black hole masses at z < 0.4.**

4. **Ionization diagnostics (BPT diagram, emission line ratios) confirm AGN photoionization and exclude contamination from star-forming galaxies or jets.**

5. **SED fitting demonstrates that dust reddening, not stellar populations, produces the distinctive optical-to-UV color of both LRDs and their local analogs.**

6. **The discovery enables direct spectroscopic follow-up (echelle spectroscopy for BLR kinematics, H-alpha spectropolarimetry for scattering geometry, X-ray observations) to constrain black hole spin, accretion disk structure, and feedback mechanisms.**

7. **Local analogs provide a crucial test of formation scenarios: if overmassive black holes require exotic high-z conditions (rapid mergers, rapid accretion), they should be rare or absent at z < 0.4.**

---

## Impact and Legacy

This paper has become a cornerstone for low-redshift LRD analog studies. Its impact includes:

- **Opening local laboratories**: The BLGP sample enables multi-wavelength follow-up (optical kinematics, X-ray spectroscopy, FIR dust properties) that would be prohibitively expensive for z > 4 sources.
- **Testing formation models**: The presence of overmassive black holes at z < 0.4 argues against formation scenarios that require only high-z conditions (e.g., primordial black holes, cosmological phase transitions).
- **Revising black hole demographics**: The result that ~5-10% of star-forming galaxies host AGN, and ~50% of those are overmassive, suggests that AGN-driven feedback may be important even in low-mass galaxies.
- **Anchoring SED models**: BLGP SEDs provide templates for fitting high-z LRD photometry where spectroscopy is unavailable.

---

## Connection to Phonon-Exflation Framework

**No direct connection identified.**

The discovery of local LRD analogs is primarily a demographic result: it demonstrates that overmassive black holes exist at z < 0.4 with properties similar to high-z LRDs. In the phonon-exflation framework, the abundance and evolution of black holes depend on the expansion history via the spectral action backreaction and the transit dynamics.

However, at z ~ 0.3, the phonon-exflation framework is degenerate with LCDM: the fractional difference in expansion history is <1%. Thus, the black hole demographics observed in local BLGP analogs should be nearly identical in phonon-exflation and LCDM.

**Closest thematic link**: If future observations show that local overmassive black hole systems exhibit systematic differences from high-z LRDs (e.g., different spin distributions, different host galaxy morphologies, different accretion rates), this would indicate evolution that either framework must explain. Phonon-exflation could be tested via such demographic evolution: if black hole formation is enhanced at early times by the instanton relic, then the abundance of overmassive black holes should increase steeply from z~0.3 to z~5, a testable prediction.
