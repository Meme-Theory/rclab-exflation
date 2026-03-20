# Connecting the Dots: UV-Bright Companions of Little Red Dots as Lyman-Werner Sources Enabling Direct Collapse Black Hole Formation

**Author(s):** Josephine F. W. Baggen, Matthew T. Scoggins, Pieter van Dokkum, Zoltan Haiman,
Alberto Torralba, Jorryt Matthee
**Year:** 2026
**Journal:** Submitted to Astrophysical Journal (preprint)
**arXiv:** 2602.02702
**Submitted:** February 2, 2026

---

## Abstract

The authors present a JWST imaging study of 83 Little Red Dots in which they systematically
search for spatially separated UV-bright companion galaxies. Approximately 43% of LRDs have
at least one UV-bright companion within 0.5--5 kpc, rising to ~85% for the most luminous LRDs.
Using component-resolved photometry, they estimate that these blue companions produce
Lyman-Werner (LW) radiation fields of $J_{21,LW} \sim 10^{2.5}$--$10^5$ at the LRD location,
matching or exceeding the critical threshold required for direct collapse black hole (DCBH)
formation. The spatial and photometric properties of the red-blue pairs are quantitatively
consistent with the theoretical picture in which a UV-bright star-forming neighbor irradiates
a nearby pristine atomic-cooling halo, suppressing $H_2$ cooling and enabling the gas to
collapse monolithically to a very massive black hole seed. This paper provides the first direct
observational evidence linking the spatial environment of LRDs to the DCBH seeding mechanism.

---

## Historical Context

### The Direct Collapse Black Hole Seeding Scenario

The origin of the seeds that grew into the $10^9 M_\odot$ quasars observed at $z > 6$
has been debated since the discovery of those objects. Two broad categories of seeds are
discussed: "light seeds" from Population III stellar remnants ($M \sim 10^2$ M_sun) and
"heavy seeds" from direct collapse of massive gas clouds ($M \sim 10^4$--$10^6$ M_sun).
Light seeds require very high accretion efficiencies maintained for hundreds of Myr to reach
observed masses -- in tension with periods of super-Eddington growth.

The DCBH scenario, pioneered by Loeb & Rasio (1994) and developed by Bromm & Loeb (2003),
Begelman et al. (2006), and many others, posits that pristine gas in an atomic-cooling halo
(virial temperature $T_{\rm vir} \gtrsim 10^4$ K) collapses directly to a supermassive star
and then a black hole seed of $\sim 10^4$--$10^6 M_\odot$, bypassing normal star formation.
The critical ingredient is suppression of $H_2$ -- the primary coolant that would otherwise
allow gas to fragment into normal stars. $H_2$ is photo-dissociated by photons in the
Lyman-Werner (LW) band ($11.2$--$13.6$ eV), so a nearby UV-bright galaxy providing a LW
flux above a critical threshold $J_{\rm crit} \sim 10^2$--$10^3 \times 10^{-21}$
erg s$^{-1}$ cm$^{-2}$ Hz$^{-1}$ sr$^{-1}$ is the key environmental requirement.

### Why JWST Changes Everything

Before JWST, the spatial environments of high-redshift AGN candidates could not be probed
at kpc resolution. JWST's combination of NIRCam sensitivity and 0.03--0.06 arcsec pixels
at $z \sim 5$ (corresponding to 0.2--0.4 kpc physical) for the first time allows detection
of companion galaxies separated by 0.5--5 kpc from compact sources. Baggen et al. exploit
this capability to test a specific, quantitative prediction of the DCBH scenario: LRDs --
if they are DCBHs -- should preferentially have UV-bright neighbors at kpc separations
providing supercritical LW fluxes.

---

## Key Arguments and Derivations

### 1. Sample Selection and Photometric Methodology

The authors use the JWST UNCOVER, COSMOS-Web, JADES, and CEERS datasets, selecting 83 LRDs
with spectroscopic redshifts in the range $z \sim 3.5$--$7$ that have multi-band NIRCam
coverage. For each LRD, they perform component-resolved photometry: the central red source
is modeled as a PSF-dominated point source plus optional Sersic component, and residuals in
adjacent resolution elements are searched for blue UV-bright companions.

Companion detection thresholds are set at $5\sigma$ above the local background in at
least two NIRCam filters. The companion color (measured in F115W minus F277W or F150W minus
F356W) must be blue ($< 0.5$ mag) to distinguish star-forming companions from dusty blobs
or satellite fragments of the LRD itself.

### 2. Observed Companion Fraction and Radial Distribution

Of 83 LRDs, 36 (43%) have at least one detected UV-bright companion within a projected
separation of 0.5--5 kpc. For the 20 most UV-luminous LRDs in the sample, the companion
fraction rises to 17/20 (85%). The radial distribution peaks at 1--2 kpc projected separation,
with few companions detected either at $< 0.5$ kpc (possibly blended with the LRD point
spread function) or at $> 5$ kpc.

This companion fraction is significantly higher than found for matched samples of galaxy-
selected (non-LRD) compact sources at similar redshifts, suggesting the association is
physical rather than a projection effect.

### 3. Lyman-Werner Flux Estimation

For each confirmed companion, the authors estimate the LW flux at the LRD position as:

$$J_{21,LW} = \frac{L_{LW}}{4\pi r^2 \Delta\nu_{LW}} \cdot \frac{1}{10^{-21}\,\rm erg\,s^{-1}\,cm^{-2}\,Hz^{-1}\,sr^{-1}}$$

where $L_{LW}$ is the companion's LW-band luminosity derived from SED fitting to the rest-
frame UV photometry, $r$ is the physical separation, and $\Delta\nu_{LW}$ captures the
relevant frequency interval. Using stellar population models fit to the NIRCam photometry,
they find companion star formation rates of $1$--$50 M_\odot$ yr$^{-1}$ and young ages
($< 100$ Myr), yielding hard UV spectra rich in LW photons.

The resulting LW fields at LRD positions span $J_{21,LW} \sim 10^{2.5}$--$10^5$, with a
median around $10^{3.5}$. This is well above the critical threshold ($J_{\rm crit} \sim
10^{2}$--$10^{3}$) required in DCBH models to suppress $H_2$ and enable direct collapse.

The Lyman-Werner photodissociation rate of $H_2$ is:

$$k_{dis} = 1.38 \times 10^9 \, J_{21,LW} \, \rm s^{-1}$$

At $J_{21,LW} = 10^3$, this gives $k_{dis} \approx 10^{-6}$ s$^{-1}$, exceeding the
$H_2$ formation rate in pristine gas at $T \sim 10^4$ K and $n \sim 10^3$ cm$^{-3}$ by
a factor $> 10$.

### 4. Redshift and Luminosity Matching

The authors check that companion and LRD photometric (and where available, spectroscopic)
redshifts are consistent, ruling out chance projections. For 12 systems with spectroscopic
redshifts for both components, the velocity separations are $|\Delta v| < 500$ km/s,
consistent with physical association within the same dark matter halo or adjacent halos
separated by $\sim 1$--$5$ Mpc (comoving).

Halo mass estimates from abundance matching place LRD host halos at $M_h \sim 10^{11}$--
$10^{12} M_\odot$ and companion halos at $M_h \sim 10^{10}$--$10^{11} M_\odot$ at
$z \sim 5$, consistent with the "nearby halo pair" configuration required for DCBH
formation (Dijkstra et al. 2008).

### 5. Comparison to DCBH Theoretical Predictions

The theoretical DCBH rate density at $z \sim 5$--$7$ depends sensitively on the number of
pristine-atomic-cooling haloes receiving supercritical LW flux from a neighbor. Simulations
by Regan et al. (2017) and Lupi et al. (2021) find that synchronized pairs (star-forming
halo + pristine neighbor within 3--5 kpc) occur with a comoving number density of
$\sim 10^{-3}$--$10^{-2}$ Mpc$^{-3}$ at $z \sim 6$. The LRD comoving number density
from Matthee et al. (2024) and others is $\sim 10^{-4}$--$10^{-3}$ Mpc$^{-3}$ -- broadly
consistent with DCBH formation rates if only a fraction of synchronized pairs actually
produce a detectable LRD.

---

## Key Results

1. 43% of LRDs (rising to 85% for the most luminous) have a UV-bright companion galaxy
   within 0.5--5 kpc -- a significantly higher fraction than non-LRD compact sources.
2. Companion LW flux at LRD positions: $J_{21,LW} \sim 10^{2.5}$--$10^5$, exceeding the
   critical DCBH threshold of $J_{21,LW} \sim 10^{2}$--$10^3$ in all detected pairs.
3. Velocity separations $|\Delta v| < 500$ km/s for spectroscopic pairs -- physically
   associated, not chance projections.
4. Halo masses and separations are quantitatively consistent with the DCBH "synchronized
   pair" model of Dijkstra et al. and Regan et al.
5. LRD comoving number density is consistent with DCBH formation rates estimated from
   simulations, within the uncertainties.
6. This is the first observational evidence directly linking LRD environments to the LW
   irradiation condition of DCBH seeding theory.

---

## Impact and Legacy

Baggen et al. 2026 provides what may be the strongest observational argument yet for the DCBH
interpretation of LRDs. Unlike prior theoretical arguments based on demographic statistics
alone, this paper points to a specific, testable environmental signature -- UV-bright companion
at kpc separation with supercritical LW flux -- and finds it present in the majority of the
most luminous LRDs.

The paper stimulates immediate follow-up: (1) spectroscopic confirmation of companion redshifts
for the full sample, (2) searches for the "pristine halo" signature (Lyman-alpha emission,
lack of metals) in the LRD neighborhood, and (3) tests of whether the LRD-companion separation
evolves with redshift as predicted by DCBH models. It also connects directly to the Kocevski,
Pacucci & Ferrara (2026) paper (arXiv:2601.14368) which provides the radiation-hydrodynamic
framework for how such collapse proceeds.

---

## Connection to Phonon-Exflation Framework

The DCBH formation scenario requires suppression of internal cooling channels ($H_2$ cooling)
by external irradiation from a companion. This is a physical analogue of the spectral-action
mechanism in phonon-exflation, where the compactification of the internal SU(3) fiber
suppresses certain field modes (those with large momentum quantum numbers in the internal
space) while allowing others to propagate. The "photodissociation" of $H_2$ by LW photons
maps loosely onto the "gap" structure in the Dirac spectrum $D_K$: just as the spectral gap
kills BCS condensation (K-1e, Session 23a), the $H_2$ gap in the cooling function kills
fragmentation and enables monolithic collapse.

The kpc-scale separation between LRD and UV companion also raises the question of whether
early universe clustering of compact objects (which appears anomalously high on sub-arcsec
scales, as found by Tanaka et al. 2024) is a signature of correlated formation in connected
dark matter filaments -- a geometry that the M4 x SU(3) compactification would need to
accommodate in its cosmological sector.
