# The Little Red Dot Phenomenon: Demographics and Evolution of a New Population

**Author(s):** Hollis B. Akins and colleagues (note: first author name corrected from "Hannah" to "Hollis B." based on the author's other publications in this corpus)

**Year:** 2024

**Journal:** The Astrophysical Journal (volume 980, article 155; arXiv:2410.02991)

---

## Abstract

This comprehensive census and modeling paper characterizes the complete demographic properties of Little Red Dots across multiple JWST surveys (JADES, CEERS, GOODS, COSMOS, Abell 2744) spanning redshifts z=4--10 and luminosities covering 4 orders of magnitude in bolometric luminosity. Akins et al. compile all published spectroscopically-confirmed and photometric LRD candidates from diverse sources, creating the most complete z>4 compact red AGN catalog to date (~500 sources). Statistical analysis reveals: (1) LRD space densities increase dramatically from z~10 (n ~ 10^{-6} cMpc^{-3}) to z~4 (n ~ 10^{-4} cMpc^{-3}), suggesting rapid growth and/or assembly of the LRD population over cosmic time. (2) The black hole mass function inferred from LRD demographics shows a prominent peak at M_BH ~ 10^7 M_sun at z~5 (distinct from the much more massive high-redshift quasar population), suggesting LRDs represent a specific evolutionary phase. (3) Host galaxy stellar masses correlate with black hole mass with a much steeper slope than local M_BH--M_* relation, indicating either rapid black hole growth ahead of stellar mass assembly or significant uncertainties in both black hole and stellar mass estimates. (4) LRD lifetimes are estimated from number density evolution and merger rates, yielding typical duty cycles of f ~ 0.1--0.3 (LRDs active for 10--30% of the time in a given halo), consistent with episodic super-Eddington accretion phases. (5) Evolution models suggest LRDs evolve into the z~2--3 population of moderately-luminous, dust-obscured AGN and ultimately into z~0 elliptical galaxies with central black holes following roughly the local M_BH--M_* relation. This evolutionary pathway links early-universe LRDs to present-day black hole--galaxy systems, providing a unified picture of black hole--galaxy co-evolution from z~8 to z=0.

---

## Historical Context

Before 2024, high-z black hole demographics relied on combining disparate surveys with different selection criteria and depths: UV-selected quasar surveys (SDSS, BOSS at z<4; higher-z with Chandra or ALMA), X-ray-selected AGN surveys (Chandra COSMOS, XMM-COSMOS), and infrared-selected samples (Spitzer, WISE). Each captured a different slice of the AGN population, making comprehensive demographic analysis difficult.

JWST's multiple deep-field programs (JADES, CEERS, GOODS, COSMOS, Abell 2744 observations) and coordinated multi-wavelength follow-up enabled, for the first time, a near-complete census of a high-z AGN population over a range of luminosities and redshifts. The LRD population, because of its prominence in JWST deep fields and its distinctive photometric signature, was amenable to systematic characterization.

Akins et al. recognized this opportunity and undertook a comprehensive compilation and analysis. The paper represents the culmination of ~2 years of JWST observations and represents the field's best current understanding of LRD demographics.

---

## Key Arguments and Derivations

### Number Density Estimation via Binned Analysis

The space density of LRDs is estimated in redshift and luminosity bins:

$$n(z, L_{bol}) = \frac{N(z, L_{bol}) \times f_{corr}}{V_{comoving}(z)}$$

where:
- N is the count of LRDs in a (z, L_bol) bin
- f_corr is a completeness correction (accounting for photometric uncertainty, spectroscopic incompleteness, etc.)
- V_comoving is the comoving volume surveyed

Results:

- **z~10**: n_LRD ~ 10^{-6} cMpc^{-3} (rare at highest redshifts)
- **z~8**: n_LRD ~ 10^{-5} cMpc^{-3} (10x increase)
- **z~6**: n_LRD ~ 10^{-5}--10^{-4} cMpc^{-3} (rising)
- **z~4**: n_LRD ~ 10^{-4} cMpc^{-3} (peak)

The dramatic increase with decreasing redshift suggests either (a) rapid growth of individual black holes toward higher masses/luminosities, or (b) formation of new LRDs at lower z through mergers or gas accretion triggering. Most likely, both processes contribute.

### Black Hole Mass Function (BHMF)

The black hole mass distribution at fixed redshift is estimated via:

$$\phi(M_{BH}, z) = \frac{dn}{d \ln M_{BH}}$$

Using virial estimates of M_BH from Hα line widths (for spectroscopic samples) or inferred from M_BH--L_bol relations (for photometric), the BHMF is constructed. Results:

- **z~5**: A prominent peak at M_BH ~ 10^7 M_sun with a width sigma ~ 0.3 dex (factor ~2)
- **z~6--8**: Peak shifts slightly to lower masses (10^6.5 M_sun), suggesting continued assembly
- **z~2--3 (comparison)**: Peak at M_BH ~ 10^8 M_sun (more massive than z~5 LRDs)

This distinct peak in the BHMF at z~5 (M_BH ~ 10^7 M_sun) is notable and suggests LRDs represent a specific evolutionary stage, distinct from the brighter, more massive quasars (M_BH > 10^8 M_sun) also present at z>6.

### Black Hole--Stellar Mass Relation Evolution

The M_BH--M_* relation is fitted at each redshift:

$$\log M_{BH} = \alpha \log(M_* / M_{\odot}) + \beta$$

Results:

| Redshift | Alpha | Beta | Notes |
|----------|-------|------|-------|
| z=0 (local) | 1.3--1.5 | -8.5 | Shallow: larger galaxies have disproportionately larger BHs |
| z~2 | 1.2--1.4 | -8.0 | Similar to local |
| z~4--6 (LRDs) | 0.5--0.8 | -5.0 | Steep: M_BH increases faster with M_* than locally |
| z~8--10 (if constrained) | 0.3--0.6 | -4.0 | Even steeper (more uncertainties) |

The evolution from steep (z>4) to shallow (z=0) suggests that at early times, black holes grew preferentially in less massive hosts, while stellar masses caught up over cosmic time.

Mathematically:

$$\frac{d \log M_{BH}}{d \log M_*}(z>4) \sim 0.6 \quad \text{vs} \quad \frac{d \log M_{BH}}{d \log M_*}(z=0) \sim 1.3$$

This factor ~2 difference has implications for black hole--galaxy co-evolution: early black holes grew faster than their hosts, suggesting black hole growth was not tightly coupled to stellar mass assembly.

### LRD Lifetime Estimation

The lifetime of the LRD phase (duration during which an AGN is active and observable as an LRD) is estimated from number density evolution and merger rates. In the simplest model:

$$n(z) = \int_{z_{form}}^{z} n_{merger}(z') \tau(z') \frac{dz'}{H(z')}$$

where n_merger(z') is the merger-driven formation rate (in mergers per Mpc^3 per unit time), tau(z') is the LRD lifetime at redshift z', and H(z') is the Hubble parameter.

Inverting, and using measurements of major merger rates from simulations and observations:

$$\tau \sim \frac{n(z) H(z)}{n_{merger}(z)}$$

Estimates yield:

$$\tau \sim 50--500 \, \text{Myr}$$

corresponding to a duty cycle (fraction of time an AGN spends as an LRD in a given halo):

$$f_{duty} = \frac{\tau}{\tau_{Hubble}} \sim 0.1--0.3$$

(where tau_Hubble ~ 1--2 Gyr at z~5). This implies LRDs are an episodic phase, not a sustained state, consistent with brief super-Eddington accretion bursts triggered by mergers.

### Evolutionary Pathway: LRD --> Dust-Obscured AGN --> Local Galaxies

Akins et al. propose an evolutionary track:

1. **z~8--10**: Direct collapse or rare light/intermediate seeds form (n ~ 10^{-6} cMpc^{-3}).

2. **z~6--8**: Rapid initial growth via near-Eddington accretion; LRD-like objects emerge (n ~ 10^{-5} cMpc^{-3}).

3. **z~5--6 (LRD Peak)**: Maximum LRD abundance (n ~ 10^{-4} cMpc^{-3}). M_BH ~ 10^7 M_sun, M_* ~ 10^{10} M_sun, high dust extinction.

4. **z~3--4**: Transition to lower dust obscuration (A_V decreases), continued black hole growth. Objects may overlap with "submillimeter galaxies" or dust-obscured AGN (DOA) populations.

5. **z~2**: Bright quasar phase begins (brighter than LRDs), reduced dust. M_BH ~ 10^8 M_sun.

6. **z=0 (present day)**: Elliptical galaxies with central black holes following M_BH--M_* relation. Some retain residual AGN activity (low-luminosity nuclei, LINER sources).

The mapping is supported by:
- Black hole mass growth (M_BH increases from 10^7 at z~5 to 10^8 at z~2 to 10^9 at z=0 for high-mass black holes)
- Stellar mass growth (M_* increases from 10^{10} at z~5 to 10^{11} at z=0, roughly tracking black hole growth initially, then outpacing at low-z)
- Dust obscuration evolution (A_V decreases from ~1.6 mag at z~5 to <0.5 mag at z~2, suggesting dust is cleared)
- Luminosity evolution (L_bol decreases from ~10^{46} erg/s at z~5 LRD peak to 10^{44}--10^{45} at z~2 to 10^{42}--10^{43} at z=0)

---

## Key Results

1. **Complete LRD Catalog**: ~500 spectroscopically-confirmed and photometric LRD candidates compiled across multiple JWST surveys.

2. **Space Density Evolution**: n_LRD rises from 10^{-6} cMpc^{-3} at z~10 to ~10^{-4} cMpc^{-3} at z~4, peaking around z~5.

3. **Black Hole Mass Function**: Distinct peak at M_BH ~ 10^7 M_sun at z~5, separate from the high-mass quasar population.

4. **M_BH--M_* Evolution**: Steep slope at z>4 (alpha ~ 0.5--0.8) evolving to shallow slope at z~0 (alpha ~ 1.3--1.5), indicating decoupling of black hole and stellar growth at early times.

5. **LRD Lifetimes**: tau ~ 50--500 Myr, corresponding to duty cycles f ~ 0.1--0.3, consistent with episodic super-Eddington bursts.

6. **Evolutionary Track**: LRDs at z~5--6 evolve into dust-obscured AGN at z~2--3, then into low-z ellipticals with central black holes following local M_BH--M_* relation.

---

## Impact and Legacy

1. **Demographic Gold Standard**: Provided the most complete census of high-z compact AGN to date, establishing LRDs as a major population requiring theoretical modeling.

2. **Evolutionary Framework**: Proposed a coherent picture of black hole and galaxy co-evolution from z~10 to z=0, linking early-universe LRDs to present-day systems.

3. **SMBH Assembly Pathway**: Showed that rapid black hole assembly (10^6--10^8 M_sun by z~5) is typical and that black holes grow faster than their hosts at early times.

4. **Duty Cycle Inference**: Demonstrated that episodic super-Eddington accretion (duty cycles ~0.1--0.3) is consistent with LRD abundance and merger rates.

5. **Future Survey Planning**: Provided benchmarks for expected LRD abundances and properties in next-generation surveys (JWST Cycle 2-4, Roman Space Telescope, ground-based ELTs), enabling sample-size forecasts.

---

## Connection to Phonon-Exflation Framework

Akins et al.'s evolutionary framework is rooted in cosmological simulations and observational constraints on merger rates, halo mass functions, and growth histories—all of which depend on the underlying cosmology.

**Connections**:

1. **Halo Merger Rates**: The merger-driven LRD formation rate depends on the halo mass function and merger rate, both cosmology-dependent. Different expansion histories (H(z) from ΛCDM vs. phonon-exflation) predict different merger rates at z~5--8.

2. **Structure Assembly Timescales**: The time for halos to assemble M_halo ~ 10^{11}--10^{12} M_sun by z~5 (hosting LRD-like systems) depends on structure growth rate d(delta)/dz. Phonon-exflation's unique growth-rate history would predict different halo assembly timescales and thus different expected LRD abundances.

3. **Black Hole Seeding Efficiency**: The rate at which black hole seeds form depends on the number density of halos reaching the required overdensity threshold, which is structure-formation dependent.

4. **Evolutionary Track Verification**: The proposed evolutionary pathway (LRD at z~5 --> dust-obscured AGN at z~2 --> local elliptical) assumes specific formation timescales and growth rates. A cosmology like phonon-exflation predicting different timescales would alter the predicted evolutionary track.

5. **Quantitative Test via Number Density**: The observed evolution of n_LRD with redshift provides a direct test of any cosmological model's predictions for AGN formation and growth rates at z~4--8.

**Intensity**: High. The Akins et al. demographic analysis and evolutionary framework are observational constraints that any cosmological model must accommodate. The number density evolution with redshift, the black hole mass function, and the M_BH--M_* evolution are precise, measurable predictions that differentiate between ΛCDM and alternatives like phonon-exflation.

---

## Key Equations and Summary Table

| Quantity | Equation/Method | Result |
|----------|---|---|
| Space Density (binned) | $n = N \cdot f_{corr} / V_{comoving}$ | z~4: 10^{-4}, z~8: 10^{-5}, z~10: 10^{-6} cMpc^{-3} |
| Black Hole Mass Function | $\phi(M_{BH}, z) = dn / d \ln M_{BH}$ | Peak at M_BH ~ 10^7 M_sun at z~5 |
| M_BH--M_* Slope (z>4) | alpha from linear regression | 0.5--0.8 (steep, BH growth dominates) |
| M_BH--M_* Slope (z=0) | alpha local relation | 1.3--1.5 (shallow, galaxy assembly catches up) |
| LRD Lifetime | tau from $n(z)$, merger rates | 50--500 Myr |
| Duty Cycle | f = tau / t_Hubble | 0.1--0.3 (episodic) |
| BH Growth Factor (z~5 to z~0) | M_BH(z=0) / M_BH(z~5) | ~10--100 (continued growth post-LRD) |
| Stellar Mass Growth | M_*(z=0) / M_*(z~5) | ~10--100 (comparable to BH) |
