# The Host Galaxy (If Any) of the Little Red Dots

**Author(s):** Chang-Hao Chen, Luis C. Ho, Ruancun Li, Ming-Yang Zhuang
**Year:** 2024 (submitted November 7, 2024; revised January 12, 2025)
**Journal:** The Astrophysical Journal (accepted)
**arXiv:** 2411.04446

---

## Abstract

Chen et al. examine the host galaxy properties of eight little red dots (LRDs) selected from
the JWST UNCOVER survey, applying a novel technique (GalfitS) that simultaneously fits the
source morphology and spectral energy distribution using multi-band NIRCam images. The host
galaxy is detected in only one of the eight LRDs -- MSAID38108 at $z = 4.96$ -- which has
a stellar mass $\log(M_*/M_\odot) = 8.66$, effective radius $R_e = 0.66$ kpc, and Sersic
index $n = 0.71$ (consistent with a disk-like morphology). For the remaining seven LRDs, no
host emission centered on the central point source is found. Stellar mass upper limits are
at least a factor of 10 below the expected mass from the local $M_{\rm BH}$--$M_*$ scaling
relation if the (naively estimated) broad-line virial black hole masses are correct. Four
of the eight LRDs (50%) show extended, off-center emission whose origin is unclear but may
represent satellite clumps, tidal debris, or projected neighbors.

---

## Historical Context

### The BH-to-Galaxy Mass Ratio Problem

In the local universe, the mass of a supermassive black hole correlates tightly with the
mass of its host galaxy's stellar bulge:

$$\log\!\left(\frac{M_{\rm BH}}{10^8 M_\odot}\right) = 1.16 \log\!\left(\frac{M_{\rm bulge}}
{10^{11} M_\odot}\right) - 0.10$$

(Kormendy & Ho 2013). This "Magorrian relation" implies co-evolution between the black hole
and the host galaxy, mediated by AGN feedback. At $z \sim 5$, if LRDs have $M_{\rm BH} \sim
10^7$--$10^9 M_\odot$ (from naive virial estimates), the expected host galaxy mass would be:

$$M_* \sim 10^{10} - 10^{12} M_\odot$$

Such massive hosts would be easily detectable in JWST NIRCam imaging. Yet LRDs appear point-
source-like with no clear extended emission -- implying either: (a) the host is present but
too compact or faint to resolve, (b) the black hole is "overmassive" relative to a sub-typical
host (the LRD is in an early phase where BH precedes galaxy growth), or (c) the virial mass
estimates are wrong (supporting Rusakov et al. 2025).

### GalfitS: A New Morpho-SED Tool

The standard approach to detecting host galaxies is PSF subtraction: subtract the central
point source (the AGN) and look for residual extended emission. This works well for bright
nearby AGN but fails for faint high-redshift sources where the PSF is uncertain and the host
signal-to-noise is low. GalfitS (Morphology+SED fitting Simultaneously) is a new code
developed by the authors that fits a multi-band, multi-component model (point source + Sersic
profile) simultaneously to all available NIRCam filter images, using the SED information to
break degeneracies between AGN and host colors. This is more constraining than single-band
PSF subtraction.

---

## Key Arguments and Derivations

### 1. GalfitS Methodology

For each LRD, the authors model the observed flux in each NIRCam filter ($F_\lambda^{\rm obs}$)
as a sum of AGN (point source) and host (Sersic) components:

$$F_\lambda^{\rm obs}(\mathbf{x}) = F_\lambda^{\rm AGN} \cdot \text{PSF}(\mathbf{x}) +
F_\lambda^{\rm host} \cdot \text{Sersic}(\mathbf{x}; R_e, n, q, \phi)$$

The AGN SED is parameterized as a power law ($F_\lambda \propto \lambda^\alpha$) plus emission
lines. The host SED is parameterized by a stellar population model (age, metallicity, star
formation history). Both components are fit simultaneously across all filters, which breaks
the degeneracy: an AGN and a host at different redshifts (or with different spectral slopes)
can be distinguished even when spatially unresolved.

The morphological parameters of the Sersic component (effective radius $R_e$, Sersic index
$n$, axis ratio $q$, position angle $\phi$) are free parameters. The fit is performed using
a modified version of GALFIT with a coupled SED likelihood.

### 2. Results for the Detected Host: MSAID38108

For MSAID38108 at $z = 4.96$, the GalfitS fit finds a statistically significant ($> 3\sigma$)
Sersic component with:

$$R_e = 0.66 \, \rm kpc, \quad n = 0.71, \quad \log(M_*/M_\odot) = 8.66$$

The Sersic index $n \sim 0.7$ is characteristic of disk-like systems (pure exponential disk
has $n = 1$; bulge-dominated systems have $n \sim 4$). The stellar mass $M_* = 4.6 \times
10^8 M_\odot$ is low compared to the virial BH mass estimate of $M_{\rm BH} \sim 10^8 M_\odot$
from broad-line fitting, giving a $M_{\rm BH}/M_* \sim 0.2$ -- about 3 orders of magnitude
above the local scaling relation (which gives $M_{\rm BH}/M_* \sim 3 \times 10^{-4}$).

This extreme ratio is one of the most direct evidence points for LRDs being "overmassive"
black holes relative to their hosts -- if the virial BH masses are correct.

### 3. Upper Limits for the Non-detections

For the seven undetected hosts, the $2\sigma$ upper limits on Sersic model flux (after fitting
the point source component) are converted to stellar mass upper limits:

$$M_* < 10^{8.5} - 10^{9.5} M_\odot$$

depending on the assumed stellar age and dust content. For $M_{\rm BH} \sim 10^8 M_\odot$,
the expected host mass from the local scaling relation is $M_* \sim 10^{10.5} M_\odot$ --
a factor of $10$--$100$ above the upper limits. Two interpretations:

- **Overmassive BH**: The BH genuinely outgrew its host in the first Gyr; early BH growth
  is decoupled from host galaxy growth.
- **Overestimated BH mass**: Virial mass estimates are inflated (e.g., by electron scattering
  as shown in Rusakov et al. 2025), so the "true" $M_{\rm BH} \sim 10^5$--$10^6 M_\odot$
  and the expected host mass from scaling relations would be $M_* \sim 10^7$--$10^8 M_\odot$,
  consistent with the upper limits.

The authors favor the latter interpretation.

### 4. Off-center Extended Emission

Four of the eight LRDs show extended emission that is NOT centered on the central point source.
This off-center emission has several possible origins:

1. Satellite galaxies or tidal debris at projected separations $\sim 2$--$5$ kpc
2. Chance projections of unrelated objects (though the statistics suggest this is unlikely
   for all four)
3. Star-forming clumps in a disturbed host, as seen in submillimeter galaxy mergers at
   similar redshifts
4. Reionization-era companion structures illuminated by the LRD AGN (a "fluorescent halo")

The off-center emission has blue UV colors, suggesting young stellar populations rather than
extended AGN emission. This is consistent with the "UV-bright companion" picture of Baggen
et al. (2026, arXiv:2602.02702), where the companion is a separate star-forming system.

---

## Key Results

1. Host galaxy detected in 1/8 LRDs (MSAID38108, $z = 4.96$): $M_* = 4.6 \times 10^8 M_\odot$,
   $R_e = 0.66$ kpc, $n = 0.71$ (disk-like).
2. For the 7 non-detected hosts: $M_* < 10^{8.5}$--$10^{9.5} M_\odot$ at $2\sigma$.
3. BH-to-host mass ratio: $M_{\rm BH}/M_* \sim 0.2$ for the detected host -- ~1000x above
   local scaling relation if virial BH masses taken at face value.
4. 4/8 LRDs (50%) show off-center extended emission -- possibly companion galaxies or
   tidal debris.
5. Results support either overmassive BHs in early universe OR inflated virial mass estimates.
6. GalfitS technique demonstrated as a new tool for host galaxy decomposition in faint
   high-z AGN.

---

## Impact and Legacy

Chen et al. (2024) is one of the most direct morphological analyses of LRD host galaxies
published to date. The combination of GalfitS morphology+SED fitting with multi-band NIRCam
data represents a methodological advance over simple PSF subtraction. The result -- that
hosts are undetected or extremely faint -- deepens the mystery of LRDs regardless of whether
one believes the virial mass estimates.

The finding that 50% of LRDs show off-center extended emission is also significant: it suggests
that the "isolated point source" view of LRDs is incomplete, and that environment (companions,
tidal debris) is common. This reinforces the picture emerging from Tanaka et al. (2024,
arXiv:2412.14246) and Baggen et al. (2026, arXiv:2602.02702) that LRDs rarely live in
isolation.

---

## Connection to Phonon-Exflation Framework

The host galaxy detection (or non-detection) for LRDs directly tests whether early black holes
are "overmassive" relative to the scaling relations established in the local universe. In the
phonon-exflation framework, the local $M_{\rm BH}$--$M_*$ scaling relation emerges from a
long history of co-evolution between black hole growth and star formation, modulated by AGN
feedback. If the compactification parameter tau has been constant since recombination (as
required by the clock constraint from Session 22d), then the effective gravitational constant
G_eff and the Eddington luminosity per unit mass have been constant -- which would predict
that LRD black holes should not be systematically more or less overmassive than local AGN.

The observed factor-of-1000 overmassiveness (if real) would therefore represent a genuine
departure from what any constant-G framework predicts, and could motivate considering whether
a phase transition in the early universe (e.g., a non-perturbative event at $z \sim 5$--$8$,
as explored in the phonon-exflation P2b route) altered the effective coupling constants during
the LRD epoch.
