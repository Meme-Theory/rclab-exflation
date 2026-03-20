# Little Red Dots (JWST) Paper Index

**Researcher**: Composite (Matthee, Labbe, Greene, Kokorev, Maiolino, Yue, Volonteri, Agarwal, Pacucci, Draca, Inayoshi, Ho, Das, Akins, Rusakov, Baggen, Zhang, Casey, Tanaka, Chen, Carranza-Escudero, de Graaff, Hviding, Simmonds, De Luca, Mehta, Jiang, Woo, Bak, Escala, Delvecchio, Torralba, Li, Madau, Chon, Nandal, Lin, Burke, Khan, Chisholm, Merida, Juodbalis, Liu, Ronayne, McClymont, Roberts, Kocevski, Ferrara, Dunne, Zeidler, Wang, Capak, Stekelenburg, Grazian)
**Papers**: 66 (2023-2026)
**Primary domain**: JWST high-z AGN discovery, BH demographics, accretion physics, BH seeds, multi-wavelength diagnostics, dark matter models, cosmological tensions
**Project relevance**: LRDs at z~4-8 constrain early BH assembly timescales, testing whether LCDM (and phonon-exflation's CDM-like prediction) can accommodate 10^6-10^9 M_sun BHs in <1 Gyr. Framework is degenerate with LCDM at z<10^28; discriminant is DM sector (CDM vs SIDM/FDM halo profiles).

---

## Dependency Graph

```
DISCOVERY & FOUNDATIONAL CENSUS
  01 (Matthee LRDs) ---> 03 (Greene UNCOVER) ---> 04 (Kokorev census)
  02 (Labbe compact)  __/                          |
  05 (Maiolino GN-z11)                             v
  06 (Yue X-ray) <--- 01, 03               14 (Akins demographics)
       |                                     |
       v                                     v
  26 (Simmonds Chandra) -----------> 24 (Inayoshi-Ho synthesis)
                                     ^
BH SEEDS & FORMATION THEORY          |
  07 (Volonteri light seeds) ------> 13 (Das tension)
  08 (Agarwal DCBH) ---> 16 (Baggen companions) ---> 17 (Pacucci DCBH)
                          |                            |
  58 (Kocevski DCBH) <---+                            |
  63 (Grazian LW) <------+                            v
                                              27 (Pacucci-Ferrara review)

ELECTRON SCATTERING DEBATE
  15 (Rusakov cocoons) ---> 31 (e-scattering ruled out) ---> 37 (Raman/Thomson)
  57 (Dunne cocoons)  __/                                     |
       |                                                      v
       +---> 47 (Torralba FeII/Balmer) -----------> 25 (de Graaff BH Stars)

MULTI-WAVELENGTH DIAGNOSTICS
  06 (Yue X-ray) ---> 26 (Simmonds Chandra deep)
  10 (Draca radio) ---> independent
  18 (Zhang variability) ---> 45 (Burke non-variability decades)
       |                       |
       v                       v
  59 (Zeidler variability) <--+---> 44 (Lin local variability)
  20 (Zhang narrow-line) ---> 64 (Stekelenburg narrow-line)

DUST & SED FITTING
  09 (Pacucci dust envelopes) ---> 19 (Casey ALMA) ---> 46 (Chen dust crisis)
       |                            |                     |
       v                            v                     v
  36 (Delvecchio AGN dust) ---> 53 (Ronayne MEGA MIRI) ---> 60 (Chen ALMA)
  52 (Liu Balmer break super-Edd) <--- independent

HOST GALAXIES & MORPHOLOGY
  22 (Chen hosts) ---> 25 (de Graaff 116-source) ---> 51 (Juodbalis direct mass)
  61 (Wang morphology)                                  |
  66 (Capak extended emission)                          v
                                              28 (Hviding RUBIES census)

DEMOGRAPHICS & POPULATION
  14 (Akins) ---> 28 (Hviding RUBIES) ---> 35 (Escala fate)
       |           |                         |
       v           v                         v
  39 (Madau LRD/LBD unification) ---> 50 (Merida environment)
  48 (Khan binary disappearance) <--- 35

COSMOLOGICAL & ALTERNATIVE MODELS
  13 (Das tension) ---> 29 (De Luca PBH) ---> 30 (Mehta cosmo vs astro)
       |                                        |
       v                                        v
  40 (Chon rapid emergence) -----------> 54 (McClymont gas-rich DM)

DARK MATTER MODELS
  32 (uSIDM core collapse) ---> 55 (Roberts SIDM clustering)
       |                          |
       v                          v
  56 (Jiang SIDM formation) <---+
  33 (Woo fuzzy DM soliton) ---> 34 (Bak ULDM soliton)

MASS ESTIMATION & SELECTION BIAS
  15 (Rusakov) ---> 31 (e-scattering ruled out) ---> 38 (Li selection bias)
  37 (Raman/Thomson) ---> 47 (Torralba FeII)
  41 (Nandal supermassive stars) <--- independent

LOCAL ANALOGS & ALTERNATIVE INTERPRETATIONS
  43 (Lin local analogs) ---> 44 (Lin local variability)
  45 (Burke non-variability) <--- independent
  49 (Chisholm globular clusters) <--- independent
  42 (Pacucci low-spin halos) <--- independent
```

---

## Duplicate/Shared arXiv Pairs

Several papers share arXiv IDs (same underlying work, different file entries):

| Paper A | Paper B | arXiv | Content |
|:--------|:--------|:------|:--------|
| 15 (Rusakov) | 57 (Dunne) | 2503.16595 / Nature DOI | Electron-scattering cocoon model |
| 16 (Baggen) | 63 (Grazian) | 2602.02702 | UV companions / LW flux |
| 17 (Pacucci DCBH) | 58 (Kocevski) | 2601.14368 | DCBH interpretation |
| 20 (Zhang NL) | 64 (Stekelenburg) | 2506.04350 | Narrow-line LRDs |
| 23 (Carranza-Escudero) | 65 (Pacucci) | 2506.04004 | Lonely LRDs / galaxy BIC |
| 24 (Inayoshi-Ho) | 62 (Inayoshi) | 2512.03130 | Critical evaluation / BHE model |
| 19 (Casey) | 60 (Chen) | 2505.18873 | ALMA dust limits |

---

## Topic Map

### A. Discovery & Foundational Census
Papers: 01, 02, 03, 04, 05, 06
Initial JWST discovery of compact red z>4 sources. Matthee coins "Little Red Dots." Greene confirms broad-line AGN. Kokorev establishes photometric census (260 LRDs). Maiolino detects BH at z=10.6 in GN-z11. Yue constrains X-ray weakness via Chandra stacking.

### B. BH Seeds & Formation Theory
Papers: 07, 08, 16, 17, 58, 63
Theoretical pathways for producing 10^4-10^6 M_sun seeds. Volonteri shows light seeds viable with super-Edd growth. Agarwal searches for DCBH candidates. Baggen finds UV-bright companions providing LW flux. Pacucci/Kocevski argue LRDs ARE accreting DCBHs. Grazian confirms LW field measurements.

### C. Electron Scattering & Line Broadening Debate
Papers: 15, 31, 37, 47, 57
Critical debate on whether broad lines reflect virial motion or e-scattering. Rusakov/Dunne (Nature) argue e-scattering reduces M_BH by 100x. Paper 31 (MNRAS) rules out dominant e-scattering via Paschen ratios and [SII]. Paper 37 shows Raman+Thomson scattering inflates masses by 2-10x. Torralba models warm cocoon producing FeII and collisional Balmer. UNRESOLVED as of 2026.

### D. Multi-wavelength Diagnostics
Papers: 10, 18, 19, 20, 36, 45, 59, 60, 64
Radio silence (Draca: 95% undetected, log R ~ -4 to -6). Variability: 97.5% non-variable (Zhang). Non-variability persists over decades in local analogs (Burke). ALMA dust upper limits M_dust < 10^6 M_sun (Casey, Chen). Narrow-line LRDs constitute ~20% of photometric sample. AGN-heated hot dust (100-400 K) confirmed by MIRI (Delvecchio).

### E. Demographics & Population Statistics
Papers: 14, 28, 35, 39, 50
Akins: BHMF peaks at M_BH ~ 10^7 M_sun at z~5, duty cycle 50-500 Myr. Hviding/RUBIES: all V-shaped point sources have broad lines (unified AGN). Escala: LRDs are transient (collisional runaway, ~0.1-0.5 Gyr). Madau: LRDs = obscured LBDs (orientation unification). Merida: environment modulates LRD rise/fall.

### F. Host Galaxies & Morphology
Papers: 15, 22, 25, 51, 61, 66
Chen: 1/8 hosts detected, 10-100x below local scaling. de Graaff: 116-source "Black Hole Stars" with T_eff ~ 4900 K. Juodbalis: first direct (dynamical) BH mass = 50 +/- 10 million M_sun at z=7.04. Wang: 85% PSF-dominated. Capak: off-center extended emission in 50% of LRDs.

### G. Dust & SED Fitting
Papers: 09, 19, 36, 46, 52, 53, 60
Pacucci proposes kpc-scale dusty envelopes. Casey/Chen ALMA: M_dust < 10^6 M_sun. Dust budget crisis (Chen): A_V = 0.5-1.5, not 2-3. Liu: Balmer break from super-Edd accretion, not stellar populations. Ronayne/MEGA: MIRI data favor AGN models in 6/8 LRDs.

### H. Cosmological & Alternative Models
Papers: 13, 29, 30, 40
Das: SMBH growth timescale as cosmology probe. De Luca: PBHs as seeds (viable window at 10^2-10^4 M_sun but subdominant). Mehta: CMB lensing vs kSZ distinguishes modified cosmology from modified astrophysics (Simons Observatory by 2028). Chon: heavy seeds form naturally in LCDM without exotic DM.

### I. Dark Matter Models
Papers: 32, 33, 34, 42, 54, 55, 56
uSIDM core collapse (sigma/m ~ 1-100 cm^2/g) produces 10^5-10^7 M_sun seeds. Fuzzy DM soliton collapse (m_chi ~ 10^{-22} eV). ULDM soliton confinement. Low-spin halos (lambda < 0.01) in standard CDM. Gas-rich DM-dominated galaxies explain overmassive ratio. SIDM clustering predictions. ALL bosonic/SIDM models incompatible with phonon-exflation (sigma/m ~ 10^{-51}).

### J. Local Analogs & Alternative Interpretations
Papers: 23, 41, 43, 44, 45, 48, 49
Carranza-Escudero: BIC prefers galaxy-only in 75% of LRDs; "lonely" clustering. Lin: Green Pea local analogs with overmassive BHs. Burke: local analogs non-variable over decades. Khan: SMBH binaries explain LRD disappearance at z<4. Chisholm: LRDs as proto-globular clusters. Nandal: supermassive star spectra match LRDs.

### K. Mass Estimation & Selection Bias
Papers: 31, 37, 38, 41, 51, 57
Li: JWST selection bias inflates apparent masses by 10-100x; corrected masses consistent with LCDM. Paper 31: e-scattering subdominant (<20%). Paper 37: radiative transfer inflates masses by 2-10x. Juodbalis: direct dynamical mass 50% below virial. Nandal: supermassive stars mimic broad lines.

### L. Reviews & Synthesis
Papers: 12, 24, 27
Maiolino (Nature Reviews 2024): foundational review. Inayoshi-Ho (2025): critical evaluation, BHE model preferred. Pacucci-Ferrara (2026 Frontiers): updated review with BH Stars framework.

## Quick Reference

| If your task involves... | Read these papers | Priority |
|:---|:---|:---|
| LRD definition, selection, discovery | 01, 04, 12 | CRITICAL |
| BH mass estimates and uncertainties | 15, 25, 31, 37, 38, 51 | CRITICAL |
| X-ray/radio constraints | 06, 10, 26 | CRITICAL |
| Dust and SED fitting | 19, 36, 46, 52, 53 | HIGH |
| BH seed formation (DCBH) | 08, 16, 17, 58, 63 | HIGH |
| BH seed formation (SIDM/FDM) | 32, 33, 34, 55, 56 | HIGH |
| Cosmological tension assessment | 13, 29, 30, 38, 40, 54 | CRITICAL |
| Variability diagnostics | 18, 44, 45, 59 | HIGH |
| Host galaxy morphology | 22, 25, 51, 61, 66 | MEDIUM |
| Demographics and evolution | 14, 28, 35, 39, 48, 50 | HIGH |
| Galaxy-only interpretation | 23, 41, 49 | MEDIUM |
| Phonon-exflation connection | 15, 30, 32, 38, 40 | CRITICAL |

---

## Paper Entries

### Paper 01: Little Red Dots: An Abundant Population of Faint AGN at z~5
- **File**: `01_2024_Matthee_Little_Red_Dots.md`
- **arXiv**: 2306.05448
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: discovery, photometric selection, number density, broad-line AGN, EIGER, FRESCO

**Summary**: Seminal paper coining "Little Red Dots." ~20 spectroscopically confirmed broad-line AGN at z=4.2-5.5 from EIGER/FRESCO. Establishes V-shaped SED, compact morphology (<300 pc), A_V ~ 1.6-2.0, M_BH ~ 10^6-10^8 M_sun, n_LRD ~ 10^{-5} cMpc^{-3} (10-100x UV quasars).

**Key Results**:
- n_LRD ~ 10^{-5} cMpc^{-3} at z~5
- Broad Halpha FWHM 1200-3700 km/s
- Near-Eddington accretion (lambda_Edd ~ 1-5)

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| Virial mass | M_BH = f * dv^2 * R_BLR / G | Standard |
| L_Edd | 1.3e46 * (M/10^8 M_sun) erg/s | Eq. in text |

**Dependencies**: Foundational. Upstream to 03, 04, 06, 12, 14.

### Paper 02: Compact Red Massive Galaxies at z=7-9
- **File**: `02_2023_Labbe_Compact_Red_Massive_Galaxies.md`
- **arXiv**: N/A (ApJL 951, L35)
- **Year**: 2023
- **Relevance**: HIGH
- **Tags**: photometric selection, stellar mass, compact morphology, z>7, size-mass relation

**Summary**: 13 compact massive galaxy candidates at z=7-9: M_* ~ 10^{10}-10^{11} M_sun, r_e ~ 80-300 pc. Establishes "too massive too early" tension. Some later reclassified as AGN (linking to LRDs).

**Key Results**:
- r_e ~ 80-300 pc, 10-20x smaller than local at fixed mass
- Sersic n ~ 3-5; surface density ~ 10^5 M_sun/pc^2

**Dependencies**: Pre-cursor to LRD field. Upstream to 01, 04.

### Paper 03: UNCOVER Broad-Line AGN at z=4.47
- **File**: `03_2024_Greene_UNCOVER_Broad_Line_AGN.md`
- **arXiv**: 2309.05714
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: spectroscopy, broad Halpha, Balmer break, M_BH/M_* ratio, virial mass

**Summary**: Ultradeep UNCOVER NIRSpec of LRD at z=4.47. FWHM ~ 4500 km/s, EW ~ 500-1000 A. M_BH ~ 10^9 M_sun, M_* ~ 10^{10} M_sun, ratio ~0.1 (100x local). Balmer break age 50-200 Myr.

**Key Equations**:

| Label | Description | Reference |
|:---|:---|:---|
| R_BLR-L | log(R_BLR/ld) = 0.513*log(L_Halpha) - 7.02 | Calibration |

**Dependencies**: Builds on 01. Upstream to 12, 15, 25.

### Paper 04: Census of Photometric LRDs at 4<z<9
- **File**: `04_2024_Kokorev_Census_Photometric.md`
- **arXiv**: 2401.09981
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: photometric census, 260 LRDs, number density, V-shape selection

**Summary**: 260 candidates over 640 arcmin^2, z=4-9. n ~ 10^{-5} to 10^{-4} cMpc^{-3}. A_V ~ 1.6. AGN dominates 50-90% of optical flux.

**Dependencies**: Builds on 01, 02. Upstream to 14, 23, 42.

### Paper 05: GN-z11 Black Hole at z=10.6
- **File**: `05_2023_Maiolino_GN_z11_Black_Hole.md`
- **arXiv**: 2305.12492
- **Year**: 2024 (Nature 627, 59)
- **Relevance**: HIGH
- **Tags**: z=10.6, spectroscopic BH, AGN diagnostics, outflow

**Summary**: AGN at z=10.6 via [NeIV], broad Halpha. M_BH ~ 1.6e6 M_sun. CIV outflow 800-1000 km/s. lambda_Edd ~ 1-5. Earliest spectroscopic AGN.

**Dependencies**: Independent. Referenced by 07, 13, 27.

### Paper 06: X-ray Stacking of LRDs
- **File**: `06_2024_Yue_X_ray_Stacking.md`
- **arXiv**: 2404.13290
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: X-ray, Chandra stacking, X-ray weakness, Compton-thick

**Summary**: 34 LRDs stacked in Chandra. Combined 4.1sigma. L_X 100-10,000x below L_X-L_Halpha. Requires N_H > 10^{24} cm^{-2}.

**Dependencies**: Builds on 01, 03. Upstream to 11, 24, 26.

### Paper 07: Light Seed BH Growth
- **File**: `07_2025_Volonteri_Black_Hole_Seeds.md`
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: light seeds, Pop III, super-Eddington, cosmological simulation

**Summary**: Light seeds (100 M_sun at z=20) reach 10^6-10^8 by z=6 via Eddington + merger bursts. ~80% of z=4-8 AGN dust-obscured. LCDM viable.

**Dependencies**: Independent theory. Referenced by 12, 13, 27.

### Paper 08: DCBH Search in PEARLS
- **File**: `08_2024_Agarwal_Direct_Collapse_DCBH.md`
- **arXiv**: 2403.01486
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: DCBH, PEARLS, photometric search, LW radiation

**Summary**: Two DCBH candidates at z~10-12 in PEARLS-NEP. Degenerate with dusty AGN. n_DCBH ~ 10^{-6} cMpc^{-3}.

**Dependencies**: Independent. Upstream to 16, 17, 58.

### Paper 09: Dusty Envelope Model
- **File**: `09_2024_Pacucci_Dust_Envelopes.md`
- **arXiv**: 2407.17341
- **Year**: 2024
- **Relevance**: MEDIUM
- **Tags**: dust envelopes, kpc-scale, radiative transfer, SED modeling

**Summary**: LRDs as BHs in kpc-scale radiation-driven dusty outflows. V-shaped SED from AGN + scatter + dust. N_H ~ 10^{23}-10^{24}. High EW from continuum suppression.

**Dependencies**: Builds on 01, 06. Upstream to 36, 46.

### Paper 10: Radio Properties
- **File**: `10_2025_Draca_Radio_Properties.md`
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: radio, VLA, ALMA, radio-quiet, free-free absorption

**Summary**: ~50 LRDs at 1.4/3 GHz: 95% undetected. log R ~ -4 to -6. Free-free absorption + jet suppression.

**Dependencies**: Independent. Referenced by 12, 24.

### Paper 11: Thick Accretion Disks (RIAF)
- **File**: `11_2024_Inayoshi_Gas_Envelopes.md`
- **arXiv**: 2312.15387
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: RIAF, super-Eddington, thick disk, X-ray weakness

**Summary**: Super-Eddington RIAF: epsilon ~ 0.001-0.01, L_X naturally weak. P_wind ~ 10 L_Edd. Rapid BH growth with modest luminosity.

**Dependencies**: Builds on 06. Upstream to 24, 62.

### Paper 12: Nature Reviews LRDs
- **File**: `12_2024_Nature_Reviews_LRDs.md`
- **Year**: 2024 (Nat Rev Phys 6, 739)
- **Relevance**: HIGH
- **Tags**: review, synthesis, demographics, physical models

**Summary**: Comprehensive synthesis of LRD properties, 5 interpretations, seed scenarios. Standard reference. Superseded by 27.

**Dependencies**: Synthesizes 01-11.

### Paper 13: SMBH-LCDM Tension
- **File**: `13_2024_Das_SMBH_LCDM_Tension.md`
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: growth timescale, seeding scenarios, cosmology-dependent

**Summary**: Light seeds need lambda_Edd ~ 8, heavy seeds ~ 4-5. D(z) differs between cosmologies. LRD demographics constrain seed efficiency.

**Dependencies**: Builds on 05, 07. Upstream to 29, 30, 40.

### Paper 14: LRD Demographics
- **File**: `14_2024_Akins_LRD_Population.md`
- **arXiv**: 2410.02991
- **Year**: 2024
- **Relevance**: CRITICAL
- **Tags**: demographics, BHMF, duty cycle, evolutionary track

**Summary**: ~500 LRDs. BHMF peak M_BH ~ 10^7 at z~5. Duty cycle 50-500 Myr. Steep M_BH-M_* at z>4. Evolutionary track: LRD -> obscured AGN -> local ellipticals.

**Dependencies**: Builds on 01, 04. Upstream to 28, 35.

### Paper 15: Young SMBH in Ionized Cocoons (Rusakov)
- **File**: `15_2025_Rusakov_Young_SMBH_Ionized_Cocoons.md`
- **arXiv**: 2503.16595
- **Year**: 2025 (Nature 649, 574)
- **Relevance**: CRITICAL
- **Tags**: electron scattering, BH mass revision, ionized cocoon, Nature

**Summary**: Nature letter. Broad lines from e-scattering (tau_e ~ 0.5-2), not virial. M_BH revised to 10^5-10^7 (100x lower). Dense cocoon suppresses X-ray/radio. CONTESTED by Paper 31.

**Dependencies**: Builds on 06. Central to mass debate.

### Paper 16: UV-Bright Companions (Baggen)
- **File**: `16_2026_Baggen_UV_Bright_Companions_Direct_Collapse.md`
- **arXiv**: 2602.02702
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: DCBH environment, LW flux, UV companions, synchronized pairs

**Summary**: 43% of 83 LRDs have UV companion within 0.5-5 kpc (85% for luminous). J_21,LW ~ 10^{2.5}-10^5 exceeds DCBH threshold. First environmental evidence for DCBH seeding.

**Dependencies**: Builds on 08. Upstream to 17, 63.

### Paper 17: LRDs Are DCBHs (Pacucci)
- **File**: `17_2026_Pacucci_LRDs_Direct_Collapse_Black_Holes.md`
- **arXiv**: 2601.14368
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: DCBH, radiation-hydrodynamics, V-shaped SED, Compton-thick

**Summary**: Radiation-hydro simulations of DCBHs reproduce LRD SEDs, broad Balmer, X-ray/radio suppression. Super-Edd with photon trapping. LRD phase 100-300 Myr.

**Dependencies**: Builds on 08, 16. Upstream to 27.

### Paper 18: Multi-epoch Variability of ~300 LRDs
- **File**: `18_2024_Zhang_Multepoch_Variability_300_LRDs.md`
- **arXiv**: 2411.02729
- **Year**: 2025 (ApJ 985, 119)
- **Relevance**: CRITICAL
- **Tags**: variability, DRW model, super-Eddington, variable subset

**Summary**: 314 LRDs: 97.5% non-variable (mean |dm| = 0.04 mag). 8/314 variable (0.24-0.82 mag). Supports super-Eddington or galaxy-dominated.

**Dependencies**: Builds on 01. Upstream to 44, 45, 59.

### Paper 19: ALMA Dust Upper Limits (Casey)
- **File**: `19_2025_Casey_ALMA_Dust_Upper_Limits_60_LRDs.md`
- **arXiv**: 2505.18873
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: ALMA, 1.3mm, dust mass, stacking, modified blackbody

**Summary**: 60 LRDs at ALMA 1.3mm: none detected. Stacked 3sigma: M_dust < 10^6 M_sun. Favors gas-dominated reddening.

**Dependencies**: Builds on 06, 09. Upstream to 24, 46.

### Paper 20: Narrow-Line LRDs
- **File**: `20_2025_Zhang_Narrow_Line_LRDs.md`
- **arXiv**: 2506.04350
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: narrow-line, FWHM 250 km/s, line contamination, 20% contamination

**Summary**: 5 narrow-line LRDs at z~5. ~20% of photometric LRDs lack red continuum (line contamination). Either compact starbursts or super-Edd low-mass BHs.

**Dependencies**: Builds on 01, 04. Parallel to 64.

### Paper 21: Dual LRDs and Clustering
- **File**: `21_2024_Tanaka_Dual_LRDs_Excess_Clustering.md`
- **arXiv**: 2412.14246
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: dual LRDs, clustering, COSMOS-Web, kpc-scale, 300x ACF excess

**Summary**: 3 dual LRD pairs at 1-2 kpc. Expected chance: 0.01. ACF excess ~300x. Implies mergers, correlated formation, or DCBH pairs.

**Dependencies**: Independent. Referenced by 16, 23.

### Paper 22: Host Galaxy Properties
- **File**: `22_2024_Chen_Host_Galaxy_LRDs.md`
- **arXiv**: 2411.04446
- **Year**: 2024
- **Relevance**: HIGH
- **Tags**: host galaxies, GalfitS, M_BH/M_*, off-center emission

**Summary**: 1/8 hosts detected (M_* = 4.6e8, R_e=0.66 kpc). M_BH/M_* ~ 0.2 (1000x local). 4/8 show off-center extended emission.

**Dependencies**: Builds on 03. Referenced by 24, 66.

### Paper 23: Lonely LRDs (Carranza-Escudero)
- **File**: `23_2025_Carranza-Escudero_Lonely_LRDs_AGN_Challenges.md`
- **arXiv**: 2506.04004
- **Year**: 2025 (ApJL 989, L50)
- **Relevance**: CRITICAL
- **Tags**: BIC galaxy-only preferred, clustering, lonely, low halo mass

**Summary**: 124 LRDs: BIC prefers galaxy-only in 75% (79% with MIRI). Low-density environments. b ~ 1.5-2.5, M_h ~ 10^{10}-10^{11.5}. Challenges AGN interpretation.

**Dependencies**: Independent. Debated by 24.

### Paper 24: Critical Evaluation (Inayoshi-Ho)
- **File**: `24_2025_Inayoshi_Ho_Critical_Evaluation_LRDs.md`
- **arXiv**: 2512.03130
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: synthesis, BHE model, virial uncertainty, decisive tests

**Summary**: Most comprehensive review. M_BH ~ 10^6-10^7 in dense gas envelope. Virial masses uncertain by 2-3 dex. 4 decisive tests identified.

**Dependencies**: Synthesizes 06, 11, 15, 18, 19, 22, 23.

### Paper 25: Black Hole Stars (de Graaff / RUBIES)
- **File**: `25_2025_de_Graaff_Black_Hole_Stars_RUBIES.md`
- **arXiv**: 2511.21820
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: 116-source, Black Hole Stars, Hayashi track, Balmer decrement, unified

**Summary**: 116 LRDs z=2.3-9.3. Hydrostatic gas envelopes, T_eff ~ 4900 K. Balmer decrement ~ L_bol^{0.8} (collisional). Tight Halpha-continuum linearity. n_e > 10^9.

**Dependencies**: Builds on 03, 15. Upstream to 27, 28.

### Paper 26: Chandra Rules Out Super-Eddington
- **File**: `26_2025_Simmonds_Chandra_Super_Eddington_Ruled_Out.md`
- **arXiv**: 2505.09669
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Chandra 400 Ms, N_H > 10^25, Compton-thick

**Summary**: 55 LRDs in 400 Ms Chandra: no detection. L_X < 10^{42}. N_H > 10^{25} required. Standard super-Edd ruled out at >99% CL.

**Dependencies**: Builds on 06.

### Paper 27: LRD SMBH Review (Pacucci-Ferrara 2026)
- **File**: `27_2026_Pacucci_Ferrara_LRD_SMBH_Review.md`
- **arXiv**: 2601.00089
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: review, BH Stars, DCBH, super-Eddington, roadmap

**Summary**: Updated review consolidating BH Star phenomenology, DCBH pathway, accretion physics. Supersedes Paper 12. Roadmap for 2026-2030.

**Dependencies**: Terminal review node.

### Paper 28: RUBIES Census (Hviding)
- **File**: `28_2025_Hviding_RUBIES_Spectroscopic_Census.md`
- **arXiv**: 2506.05459
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: RUBIES, V-shape equivalence, unified definition, data release

**Summary**: 1500 galaxies, 36 LRDs. ALL V-shaped point sources have broad lines. M_BH ~ 10^7-10^{10}. Unified LRD definition.

**Dependencies**: Builds on 01, 25.

### Paper 29: Cosmologist's Take (De Luca)
- **File**: `29_2025_De_Luca_Cosmologist_Take_LRDs.md`
- **arXiv**: 2512.19666
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: PBH, mu-distortion, CMB constraints, merger timescale

**Summary**: PBH excluded by CMB mu-distortion. Viable window M ~ 10^2-10^4 (Omega < 10^{-2}). Mergers too slow. PBH not favored over DCBH.

**Dependencies**: Builds on 13.

### Paper 30: Modified Cosmology vs Astrophysics (Mehta)
- **File**: `30_2025_Modified_Cosmology_vs_Astrophysics.md`
- **arXiv**: 2509.21952
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: CMB lensing, kSZ, Simons Observatory, degeneracy breaking

**Summary**: Weak lensing enhanced only by modified cosmology; kSZ by both. SO: 10.4sigma discrimination. Phonon-exflation predicts unchanged lensing (CDM-like). Decisive test ~2028.

**Dependencies**: Builds on 13. Directly tests framework.

### Paper 31: Electron Scattering Ruled Out
- **File**: `31_2025_Electron_Scattering_Ruled_Out_LRDs.md`
- **arXiv**: N/A (MNRAS Lett 544, L167)
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: Paschen ratios, [SII] diagnostic, e-scattering <20%, virial restored

**Summary**: 25 LRDs: P-alpha/P-beta = 2.7 (photoionization, not scattering). Broad [SII] in 72%. E-scattering <20%. Virial masses restored. CONTRADICTS Paper 15/57.

**Dependencies**: Directly contests 15. Central to mass debate.

### Paper 32: uSIDM Core Collapse
- **File**: `32_2025_uSIDM_LRD_Core_Collapse.md`
- **arXiv**: 2507.03230
- **Year**: 2025 (JCAP 2026)
- **Relevance**: HIGH
- **Tags**: uSIDM, gravothermal collapse, seed mass, INCOMPATIBLE with framework

**Summary**: sigma/m ~ 1-100 cm^2/g: core collapse in ~100 Myr. Seeds 10^5-10^7. n(z=5) ~ 0.2-0.8 Gpc^{-3}. 46+ orders of magnitude mismatch with phonon-exflation.

**Dependencies**: Independent. Upstream to 55, 56.

### Paper 33: Fuzzy DM Soliton Collapse
- **File**: `33_2026_Fuzzy_DM_Soliton_LRD_Origin.md`
- **arXiv**: 2601.00044
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: fuzzy DM, soliton, m_chi ~ 10^{-22} eV, INCOMPATIBLE with framework

**Summary**: FDM soliton cores (r_c ~ 100 pc) collapse when baryon mass exceeds ~10% soliton mass. Seeds 10^6-10^7. Bosonic DM incompatible with phonon-exflation.

**Dependencies**: Independent. Parallel to 34.

### Paper 34: ULDM Soliton Seeds
- **File**: `34_2026_ULDM_Soliton_SMBH_Seeds.md`
- **arXiv**: 2601.21676
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: ULDM, shock heating, direct collapse, INCOMPATIBLE with framework

**Summary**: ULDM soliton confinement + shock heating to ~10^4 K. Seeds 10^5-10^6 without Pop III. INCOMPATIBLE with phonon-exflation (fermionic vs bosonic DM).

**Dependencies**: Builds on 33.

### Paper 35: Fate of Little Red Dots
- **File**: `35_2025_Fate_of_Little_Red_Dots.md`
- **arXiv**: 2509.20453
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: collisional runaway, transient phase, dynamical timescale, descendants

**Summary**: tau_dyn ~ 0.1-1 Gyr. Collisional runaway produces 10^5-10^7 M_sun central object in ~10^7-10^8 yr. LRDs transient (~0.1-0.5 Gyr). Descendants: z~2-3 quasars.

**Dependencies**: Builds on 14. Upstream to 48.

### Paper 36: AGN-Heated Dust
- **File**: `36_2025_AGN_Heated_Dust_LRDs.md`
- **arXiv**: N/A (A&A 704, A313)
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: MIRI, hot dust 100-400 K, AGN confirmed, ALMA reconciled

**Summary**: 50-70% show hot AGN dust (100-400 K). Mid-IR diagnostics confirm AGN. N_H > 10^{24}. Cold dust negligible. Resolves ALMA non-detection.

**Dependencies**: Builds on 09, 19. Upstream to 53.

### Paper 37: Raman/Thomson Scattering
- **File**: `37_2025_Raman_Thomson_Scattering_LRD_Lines.md`
- **arXiv**: 2508.08768
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Monte Carlo RT, resonance scattering, mass inflation 2-10x

**Summary**: 3D MC radiative transfer. Thomson adds 100-200 km/s. Resonance at tau>10 inflates widths 50-100%. Net mass inflation 2-10x (0.3-1 dex).

**Dependencies**: Independent. Referenced by 24.

### Paper 38: Selection Bias ("Tip of the Iceberg")
- **File**: `38_2025_Li_Selection_Bias_Overmassive_BH.md`
- **arXiv**: 2509.08120
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: selection bias, luminosity-limited, corrected mass function, CDM consistent

**Summary**: JWST luminosity-limited. High-M BHs preferentially detected. Corrected phi(M) ~ M^{-2.5}, peaks at 10^6-10^7 (not 10^8-10^9). Consistent with hierarchical LCDM. SUPPORTS phonon-exflation CDM prediction.

**Dependencies**: Independent. Key for framework assessment.

### Paper 39: LRDs as Obscured LBDs (Unification)
- **File**: `39_2026_LRDs_Obscured_LBDs_Unification.md`
- **arXiv**: 2602.22386
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: orientation unification, inclination, self-shadowing

**Summary**: LRDs and LBDs = same super-Edd systems at different inclinations. Edge-on: dust obscured (LRD). Face-on: blue (LBD). Combined n ~ 0.08 Gpc^{-3}.

**Dependencies**: Builds on 14, 25.

### Paper 40: Rapid Emergence of Overmassive BH
- **File**: `40_2026_Rapid_Emergence_Overmassive_BH.md`
- **arXiv**: 2601.04955
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: AREPO simulation, LCDM, heavy seeds natural, no exotic DM

**Summary**: Full radiation-hydro in LCDM. Heavy seeds (10^5-10^6) form naturally at z~15-20. Super-Edd grows to 3e7 by z~8. No exotic physics. VALIDATES phonon-exflation CDM.

**Dependencies**: Builds on 07, 13.

### Paper 41: Supermassive Star Spectra
- **File**: `41_2025_Supermassive_Stars_LRD_Spectra.md`
- **arXiv**: 2507.12618
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: supermassive stars, non-LTE, FWHM mimicry, alternative

**Summary**: M ~ 10^6 M_sun metal-free stars reproduce LRD spectra via non-LTE broadening. Transient ~10^4-10^6 yr. If correct, no BHs needed at z>5.

**Dependencies**: Independent alternative.

### Paper 42: Low-Spin Halos
- **File**: `42_2025_Low_Spin_Halos_LRD_Explanation.md`
- **arXiv**: 2506.03244
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: angular momentum, lambda < 0.01, LCDM preserved, clustering

**Summary**: LRDs from low-spin tail (~1-5% of halos). Compact disks ~100-300 pc. Enhanced clustering b~3-4. Preserves LCDM.

**Dependencies**: Independent.

### Paper 43: Local Analogs (Lin)
- **File**: `43_2025_Lin_Local_Analogs_LRDs.md`
- **arXiv**: 2412.08396
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: Green Pea galaxies, local analogs, overmassive BH

**Summary**: 7 Green Pea BL galaxies at z~0.2-0.4 match LRD SEDs. 16/19 overmassive BHs. Low-z laboratory.

**Dependencies**: Independent. Upstream to 44.

### Paper 44: Local Analog Variability
- **File**: `44_2026_Local_Analogs_Variability_AGN.md`
- **arXiv**: 2603.01473
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: ZTF, DRW, AGN-driven variability

**Summary**: 3/7 local analogs show AGN variability via ZTF. Supports AGN interpretation; high-z non-variability may be observational.

**Dependencies**: Builds on 43, 18.

### Paper 45: Non-Variability Over Decades
- **File**: `45_2025_Non_Variability_Decades_LRDs.md`
- **arXiv**: 2511.16082
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: <3-4% rms, 15yr baseline, super-Eddington

**Summary**: 3 local analogs: <3-4% rms over 15 yr. Non-variability is physical. Supports photon-trapped/super-critical accretion.

**Dependencies**: Builds on 18, 43.

### Paper 46: Dust Budget Crisis
- **File**: `46_2025_Dust_Budget_Crisis_LRDs.md`
- **arXiv**: 2505.22600
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: A_V correction, gas opacity, ALMA tension resolved

**Summary**: A_V = 0.5-1.5 (not 2-3). Gas opacity primary reddening agent. Resolves dust budget crisis.

**Dependencies**: Builds on 19, 36.

### Paper 47: Warm Outer Layer (Torralba)
- **File**: `47_2025_Warm_Outer_Layer_FeII_Balmer.md`
- **arXiv**: 2510.00103
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: [FeII], collisional Balmer, warm cocoon ~7000 K, mass overestimate 2-10x

**Summary**: [FeII] and anomalous Balmer ratios from dense warm gas cocoon (n_e ~ 10^9-10^{10}, ~7000 K). Virial masses overestimated 2-10x.

**Dependencies**: Builds on 15, 25.

### Paper 48: SMBH Binary Disappearance
- **File**: `48_2026_SMBH_Binary_LRD_Disappearance.md`
- **arXiv**: 2503.07711
- **Year**: 2026
- **Relevance**: LOW
- **Tags**: SMBH binary, slingshot, core expansion, z<4 disappearance

**Summary**: SMBH binary slingshot ejects core mass (10x density reduction in 100-800 Myr). Explains LRD absence at z<4.

**Dependencies**: Builds on 35.

### Paper 49: LRDs as Proto-Globular Clusters
- **File**: `49_2026_LRDs_Globular_Clusters_Formation.md`
- **arXiv**: 2602.15935
- **Year**: 2026
- **Relevance**: LOW
- **Tags**: globular clusters, stellar populations, alternative

**Summary**: LRDs as young proto-GCs. UV LF evolves to local GC mass function. Fringe interpretation, contradicted by 28.

**Dependencies**: Independent.

### Paper 50: Environmental Rise and Fall
- **File**: `50_2025_Environment_Rise_Fall_LRDs.md`
- **arXiv**: 2510.06408
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: environment, galaxy group, transitional AGN

**Summary**: Stingray system z=5.12: transitional AGN in group. Environment modulates LRD properties/lifetimes.

**Dependencies**: Builds on 21, 23.

### Paper 51: Direct BH Mass at z=7.04
- **File**: `51_2025_Direct_BH_Mass_LRD_z7.md`
- **arXiv**: 2508.21748
- **Year**: 2025
- **Relevance**: CRITICAL
- **Tags**: lensed, Keplerian rotation, direct dynamical mass, anchor

**Summary**: First direct BH mass in LRD: M_BH = 50 +/- 10 million M_sun at z=7.04. ~50% below virial. M_BH/M_* ~ 2-3. Consistent with Eddington growth from seed.

**Dependencies**: Builds on 03, 15. Anchors mass calibration.

### Paper 52: Balmer Break from Super-Eddington
- **File**: `52_2025_Balmer_Break_Super_Eddington.md`
- **arXiv**: 2507.07190
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: Balmer break, accretion physics, Hayashi track, no stars needed

**Summary**: Balmer break from super-Edd accretion photosphere (T ~ 4000-6000 K), not stellar populations. Temperature insensitive to dot{M} (Hayashi-like).

**Dependencies**: Independent. Parallel to 25.

### Paper 53: MEGA MIRI SED Fitting
- **File**: `53_2025_MEGA_MIRI_SED_Fitting_LRDs.md`
- **arXiv**: 2508.20177
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: MIRI, spectrophotometric, AGN models, warm dust

**Summary**: 8 LRDs with MIRI: 6/8 AGN models preferred. Warm dust 800-1400 K. Stellar templates fail. MIRI critical for breaking degeneracies.

**Dependencies**: Builds on 36.

### Paper 54: Gas-Rich DM-Dominated Galaxies
- **File**: `54_2026_Gas_Rich_DM_Dominated_Overmassive.md`
- **arXiv**: 2506.13852
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: dynamical mass, gas fraction, DM-dominated, THESAN

**Summary**: "Overmassive" is artifact of M_* denominator. M_BH/M_dyn ~ 0.001 (consistent with local). High-z galaxies DM-dominated (f_gas ~ 0.5-0.8). No exotic physics. Supports CDM.

**Dependencies**: Builds on 22. Supports phonon-exflation.

### Paper 55: SIDM Clustering of LRDs
- **File**: `55_2025_SIDM_Clustering_LRDs.md`
- **arXiv**: 2512.18000
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: SIDM clustering, halo mass, bias prediction

**Summary**: uSIDM predicts LRDs in M_h ~ 8e10 with b_eff ~ 4.5. Stronger clustering than LCDM AGN. Testable.

**Dependencies**: Builds on 32.

### Paper 56: SIDM Core Collapse Formation
- **File**: `56_2026_SIDM_Core_Collapse_LRD_Formation.md`
- **arXiv**: 2503.23710
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: SIDM velocity-dependent, sigma ~ 30 cm^2/g, cosmological

**Summary**: Velocity-dependent SIDM: sigma ~ 30 cm^2/g at v~80 km/s. Seeds 10^6-10^8 in M_h ~ 10^{10}-10^{11}. t_collapse ~ 10-100 Myr.

**Dependencies**: Builds on 32.

### Paper 57: Young SMBH in Cocoons (Dunne)
- **File**: `57_2025_Dunne_Little_Red_Dots_Young_SMBH.md`
- **Year**: 2026 (Nature)
- **Relevance**: HIGH
- **Tags**: Nature, electron scattering, M_BH 10^5-10^7

**Summary**: Same result as Paper 15 (shared DOI). 33 LRDs. M_BH ~ 10^5-10^7 via e-scattering deconvolution.

**Dependencies**: = Paper 15.

### Paper 58: LRDs Are DCBHs (Kocevski)
- **File**: `58_2025_Kocevski_Little_Red_Dots_DCBH.md`
- **arXiv**: 2601.14368
- **Year**: 2026
- **Relevance**: HIGH
- **Tags**: DCBH, 6 puzzles resolved

**Summary**: = Paper 17 (same arXiv). DCBH accretion resolves 6 LRD puzzles.

**Dependencies**: = Paper 17.

### Paper 59: LRD Variability (Zeidler)
- **File**: `59_2025_Zeidler_Little_Red_Dots_Variability.md`
- **Year**: 2025 (ApJ 985, 119)
- **Relevance**: MEDIUM
- **Tags**: variability, lensed time delays, systematic photometry

**Summary**: ~300 LRDs: >90% non-variable. 8 variable. 2 lensed with ~130 yr rest-frame delays. Parallel to Paper 18.

**Dependencies**: Parallel to 18.

### Paper 60: Dust Mass Limits (Chen ALMA)
- **File**: `60_2025_Chen_Dust_Mass_Limits_ALMA.md`
- **arXiv**: 2505.18873
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: ALMA, dust mass, gas opacity

**Summary**: = Paper 19 (same arXiv). M_dust < 10^6. Gas opacity primary reddening.

**Dependencies**: = Paper 19.

### Paper 61: Morphology and Compactness (Wang)
- **File**: `61_2025_Wang_Morphology_Compactness_JWST.md`
- **arXiv**: 2509.21236
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: PSF fitting, morphological limits, 85% PSF-dominated

**Summary**: 99 LRDs: 85% PSF-dominated, 15% extended. SNR < 25 makes morphology unreliable. PSF fraction better metric.

**Dependencies**: Independent methodology.

### Paper 62: Dense Gas Enshrouded AGN (Inayoshi)
- **File**: `62_2025_Inayoshi_Dense_Gas_Enshrouded_AGN.md`
- **arXiv**: 2512.03130
- **Year**: 2025
- **Relevance**: HIGH
- **Tags**: gas envelope, Balmer absorption, outflows

**Summary**: = Paper 24 (same arXiv). Dense gas-enshrouded BH model. Transient 100-500 Myr phase.

**Dependencies**: = Paper 24.

### Paper 63: LW and DCBH Formation (Grazian)
- **File**: `63_2026_Grazian_Lyman_Werner_DCBH_Formation.md`
- **arXiv**: 2602.02702
- **Year**: 2026
- **Relevance**: MEDIUM
- **Tags**: LW flux, companion photometry, DCBH threshold

**Summary**: = Paper 16 (same arXiv). Confirms supercritical J_21,LW from companions.

**Dependencies**: = Paper 16.

### Paper 64: Narrow-Line LRDs (Stekelenburg)
- **File**: `64_2025_Stekelenburg_Narrow_Line_LRDs.md`
- **arXiv**: 2506.04350
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: narrow-line, BPT, ~40 candidates, heterogeneous

**Summary**: = Paper 20 (same arXiv). ~40 narrow-line candidates. BPT consistent with SF, not AGN.

**Dependencies**: = Paper 20.

### Paper 65: LRD Clustering and SED (Pacucci)
- **File**: `65_2024_Pacucci_Clustering_SED_AGN.md`
- **arXiv**: 2506.04004
- **Year**: 2025
- **Relevance**: MEDIUM
- **Tags**: clustering, BIC galaxy-only

**Summary**: = Paper 23 (same arXiv). Low clustering. BIC prefers starburst in 60-75%.

**Dependencies**: = Paper 23.

### Paper 66: Extended Emission (Capak)
- **File**: `66_2025_Capak_Extended_Emission_Host_Galaxies.md`
- **Year**: 2025 (ApJL 989, L12)
- **Relevance**: MEDIUM
- **Tags**: extended emission, multi-band, companion structures, [OIII]

**Summary**: 4 LRD systems with off-center emission. 2/3 show [OIII] (photoionized by AGN). Extended M_* ~ 10^8. LRDs in complex multi-component systems.

**Dependencies**: Builds on 22.

---

## Cross-Paper Equation Concordance

### Virial BH Mass Estimator
Appears in Papers 01, 03, 05, 15, 24, 25, 28, 31, 37, 47, 51
$$M_{BH} = f \cdot \frac{\Delta v^2 \cdot R_{BLR}}{G}$$
- Standard calibration: f ~ 0.3-1.5, R_BLR from L_Halpha
- Paper 15/57: v_obs >> v_true (e-scattering), M_BH reduced 100x
- Paper 31: e-scattering <20%, virial restored
- Paper 37: radiative transfer inflates 2-10x
- Paper 51: direct dynamical mass ~50% of virial
- STATUS: Virial formula systematically overestimates by ~2x (Paper 51), possibly up to 10x (Paper 37)

### Eddington Luminosity
Appears in Papers 01, 05, 07, 11, 13, 17, 24, 26, 27
$$L_{Edd} = \frac{4\pi G M_{BH} m_p c}{\sigma_T} \approx 1.3 \times 10^{38} (M_{BH}/M_\odot) \text{ erg/s}$$

### BH Exponential Growth
Appears in Papers 07, 13, 17, 27, 29, 32, 40
$$M_{BH}(t) = M_{seed} \exp(t/t_{Eff}), \quad t_{Eff} = t_{Edd}/\lambda_{Edd}$$
- t_Edd definitions vary: ~45 Myr (Salpeter) vs ~0.5 Gyr (e-folding)

### Comoving Number Density
Appears in Papers 01, 04, 14, 32, 33, 34, 42
$$n_{LRD}(z) = N \cdot f_{corr} / V_{comoving}$$
- z~4: ~10^{-4} cMpc^{-3}; z~8: ~10^{-5}; z~10: ~10^{-6}
- Corrected for ~20% photometric contamination (Paper 20)

### X-ray Luminosity
Appears in Papers 06, 26
$$L_X = 4\pi d_L^2 F_X (1+z)^{\Gamma-2}$$
- Observed: 100-10,000x below L_X-L_Halpha prediction

### Electron Scattering Profile
Appears in Papers 15, 31, 37, 57
$$P(\Delta\lambda) \propto \int \phi(\Delta\lambda') \exp(-\tau_e[...]) d\Delta\lambda'$$
- tau_e ~ 0.5-2 (Rusakov). Contested: contribution <20% (Paper 31)

### Modified Blackbody (Dust)
Appears in Papers 19, 36, 46, 53, 60
$$S_{1.3mm} = \frac{(1+z)}{D_L^2} \kappa_{dust} M_{dust} B_\nu(T_{dust})$$
- Upper limit: M_dust < 10^6 M_sun

### BH Star Effective Temperature
Appears in Papers 25, 27, 52
$$T_{eff} = (L_{AGN} / 4\pi \sigma_B R_{env}^2)^{1/4} \approx 4900 \pm 600 \text{ K}$$
- Hayashi-like (insensitive to accretion rate)

---

## Notation Conventions

| Symbol | Meaning | Typical LRD Value |
|:---|:---|:---|
| M_BH | Black hole mass | 10^5-10^9 M_sun (disputed) |
| M_* | Host stellar mass | 10^7-10^{10} M_sun |
| r_e | Effective radius | 80-300 pc |
| A_V | Visual extinction | 0.5-2.0 mag |
| lambda_Edd | Eddington ratio | 1-10 |
| n_e | Electron density | 10^7-10^{10} cm^{-3} |
| N_H | Column density | 10^{23}-10^{25} cm^{-2} |
| tau_e | Electron optical depth | 0.5-2 |
| FWHM | Full width half max | 1000-5000 km/s (broad) |
| J_21 | LW flux units | 10^{2.5}-10^5 |
| n_LRD | Number density | 10^{-5}-10^{-4} cMpc^{-3} |
| sigma/m | DM self-interaction | CDM: ~0; uSIDM: 1-100 cm^2/g |

---

## Computational Verification Status

| Paper | Equation/Result | Verified? | Where |
|:---|:---|:---|:---|
| 01 | n_LRD ~ 10^{-5} cMpc^{-3} | No | Observational |
| 06 | L_X deficit 100-10,000x | No | Observational |
| 13 | Growth timescale requirements | No | Analytic |
| 15 | tau_e ~ 0.5-2 model | No | Forward model |
| 19 | M_dust < 10^6 M_sun | No | Observational |
| 25 | T_eff ~ 4900 K Hayashi-like | No | SED fitting |
| 30 | SO 10.4sigma discriminant | No | Fisher forecast |
| 31 | Paschen ratio 2.7 vs 1.2 | No | Observational |
| 32 | uSIDM tau_collapse ~ 100 Myr | No | Semi-analytic |
| 38 | Corrected phi(M) ~ M^{-2.5} | No | Monte Carlo |
| 40 | Heavy seeds natural in LCDM | No | AREPO simulation |
| 51 | M_BH = 50 +/- 10 M M_sun | No | Keplerian fit |
