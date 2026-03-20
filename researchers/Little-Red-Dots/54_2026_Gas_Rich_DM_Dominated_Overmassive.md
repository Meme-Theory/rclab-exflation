# Overmassive Black Holes in the Early Universe Can Be Explained by Gas-Rich, Dark Matter-Dominated Galaxies

**Author(s):** William McClymont, Sandro Tacchella, Xihan Ji, Rahul Kannan, Roberto Maiolino, and 9 co-authors

**Year:** 2026

**Journal:** arXiv:2506.13852

---

## Abstract

Little Red Dots are characterized by black hole masses that appear "overmassive" relative to their stellar masses (M_BH/M_* ~ 0.1 to 1, compared to local relation M_BH/M_* ~ 0.001). A common interpretation is that this ratio represents a violation of the black hole-galaxy scaling relations and indicates exotic black hole physics. This work argues that the apparent overmassiveness is not exotic but rather a natural consequence of the demographics of high-redshift galaxies: young galaxies at z > 5 are typically gas-rich (gas fraction f_gas ~ 0.5-0.8 of baryons) and dark-matter-dominated (M_DM >> M_*). In such systems, the dynamical mass (total mass determining the gravitational potential) is dominated by dark matter, not stars. The black hole mass scales naturally with dynamical mass (M_BH ~ 0.001 M_dyn), not with stellar mass. Thus, a galaxy with M_* ~ 1e7 solar masses but M_dyn ~ 1e10 solar masses (due to dark matter) naturally hosts a black hole with M_BH ~ 1e7 solar masses, appearing "overmassive" if one ignores the dark matter and uses M_* as the denominator. Using the THESAN-ZOOM cosmological simulations, we demonstrate that LRDs emerge naturally as a population of gas-rich, dark-matter-dominated young galaxies. The M_BH/M_* vs. M_* relation in simulations matches JWST observations, without invoking exotic physics. The apparent overmassiveness is thus not a crisis, but a demographic artifact of incomplete census of galaxy masses.

---

## Historical Context

The observation that LRDs host black holes with M_BH/M_* ~ 0.1-1 (compared to local relation M_BH/M_* ~ 1/500) has been widely interpreted as a major puzzle requiring exotic explanation. Proposed solutions included:

1. **Primordial black holes**: Cosmological relics from the early universe with different formation physics than stellar-mass seeds
2. **Direct collapse black holes**: Massive collapsing gas clouds bypassing stellar evolution
3. **Rapid accretion at super-Eddington rates**: Enhanced growth beyond standard accretion
4. **Modified gravity**: Non-standard cosmology or gravitational physics

McClymont et al. 2026 proposes a simpler explanation: the "overmassive" characterization is based on an incomplete census of galaxy mass. The standard local M_BH-M_* relation applies to present-day massive elliptical galaxies that are essentially "all stars" (M_* ~ M_dyn, dark matter halo has been tidally stripped or is negligible). At high redshift, young galaxies are fundamentally different: they are gas-rich and dark-matter-dominated (M_dyn >> M_*).

If black holes scale with dynamical mass (M_BH ~ alpha M_dyn, where alpha ~ 0.001 is universal), then the ratio M_BH/M_* naturally becomes large in dark-matter-dominated systems.

---

## Key Arguments and Derivations

### Dynamical Mass and Stellar Mass in Young Galaxies

The total (dynamical) mass within a radius R of a galaxy includes:

1. **Stellar mass**: M_* = total integrated stellar mass
2. **Gas mass**: M_gas (neutral, ionized, molecular)
3. **Dark matter mass**: M_DM

The dynamical mass is determined from the rotation curve (in disk galaxies) or velocity dispersion (in early-type galaxies):

$$M_{\text{dyn}}(<r) = \frac{v_c^2(r) r}{G} \quad (\text{or}) \quad M_{\text{dyn}}(<r) = \frac{\sigma_v^2(r) r}{G}$$

For a galaxy at z ~ 6 with mass estimates:
- **Stellar mass** (from SED fitting): M_* ~ 1e7-1e8 solar masses
- **Gas mass** (from ALMA CO observations or dynamical modeling): M_gas ~ 1e7-1e8 solar masses (comparable to stellar mass, high gas fraction)
- **Dark matter mass** (from kinematics or halo mass function): M_DM ~ 1e9-1e10 solar masses

The total dynamical mass is:

$$M_{\text{dyn}} = M_* + M_{\text{gas}} + M_{\text{DM}} \sim M_{\text{DM}} \sim 1e10 M_\odot$$

Thus, M_* ~ 1e7 M_sun represents only ~0.1-1% of the dynamical mass.

### Black Hole-Dynamical Mass Relation

Observations of nearby galaxies reveal that black hole masses correlate with the dynamical properties of the galaxy:

1. **M_BH - M_* relation** (local): $M_{\text{BH}} \sim 0.001 M_*$ (Kormendy & Ho 2013, others)
2. **M_BH - sigma_v relation**: $M_{\text{BH}} \sim 0.002 \times (\sigma_v / 200 \text{ km/s})^4 M_*$ (applies to early-type galaxies)
3. **M_BH - M_dyn (halo) relation** (possibly more fundamental): $M_{\text{BH}} \sim 0.0001 - 0.001 \times M_{\text{halo}}$

The halo mass-dynamical mass relation is:

$$M_{\text{halo}} = \frac{M_*}{f_{\text{star}}}$$

where $f_{\text{star}} \sim 0.1$ is the cosmic baryon fraction condensed into stars. Thus:

$$M_{\text{halo}} = \frac{1e7 M_\odot}{0.01} = 1e9 M_\odot$$

(if only 1% of baryons are in stars, typical at high z). The black hole mass is then:

$$M_{\text{BH}} \sim 0.001 \times M_{\text{halo}} = 0.001 \times 1e9 = 1e6 M_\odot$$

This matches observations of LRD black hole masses without requiring exotic physics. The apparent overmassiveness is an artifact of computing M_BH/M_* instead of M_BH/M_dyn.

### THESAN-ZOOM Simulation Results

Cosmological simulations (THESAN-ZOOM, Illustris TNG, EAGLE, etc.) include dark matter, baryons (gas and stars), and black hole physics. The simulations predict:

1. **Black hole mass scaling**: M_BH grows via accretion, following a relation M_BH ~ alpha M_dyn where alpha depends on feedback and accretion efficiency. In THESAN-ZOOM, alpha ~ 0.001, consistent with observations.

2. **Gas fraction evolution**: The gas fraction f_gas = M_gas / (M_* + M_gas) decreases from f_gas ~ 0.9 at z ~ 10 to f_gas ~ 0.2 at z ~ 0 (present day). This evolution is driven by star formation converting gas to stars, and by supernova/AGN feedback ejecting gas.

3. **Stellar mass assembly**: The stellar mass fraction f_* = M_* / M_dyn at z ~ 5-6 is f_* ~ 0.01-0.1 (i.e., only 1-10% of the dynamical mass is in stars). At z ~ 0, f_* increases to f_* ~ 0.01-1 (depending on halo mass).

4. **Black hole demographics**: The simulations produce a population of high-z black holes that naturally spans a wide range of M_BH/M_* ratios: objects with f_* ~ 0.01 have M_BH/M_* ~ 0.1, while objects with f_* ~ 0.1 have M_BH/M_* ~ 0.01.

The predicted M_BH/M_* vs. M_* relation in THESAN-ZOOM at z ~ 6 is:

$$\log(M_{\text{BH}} / M_*) = -0.5 + 0.1 \log(M_* / 10^8 M_\odot)$$

(approximate slope; variations depending on simulation details). This means:
- At M_* ~ 1e7 M_sun: M_BH/M_* ~ 0.3 (appears overmassive)
- At M_* ~ 1e8 M_sun: M_BH/M_* ~ 0.03 (more normal)
- At M_* ~ 1e9 M_sun: M_BH/M_* ~ 0.003 (normal-mass)

This diversity of M_BH/M_* ratios as a function of stellar mass emerges naturally from the varying gas fractions and dark matter dominance at different stellar masses.

### Validation Against JADES Observations

The JADES survey provides 48,022 galaxies at z > 4 with photometric redshifts and stellar masses (from SED fitting). The black hole masses can be inferred for AGN-host galaxies via X-ray/UV-to-infrared flux ratios or emission-line diagnostics. McClymont et al. 2026 compare the simulated M_BH/M_* distribution to the observed distribution and find strong agreement (within the uncertainties of the observational measurements).

---

## Key Results

1. **LRD black hole masses can be explained naturally by the M_BH-dynamical-mass relation if one accounts for the fact that high-z galaxies are gas-rich and dark-matter-dominated, not just stellar-mass-dominated.**

2. **The apparent "overmassiveness" of LRD black holes (M_BH/M_* ~ 0.1-1) is an artifact of an incomplete mass census: the dynamical mass M_dyn >> M_* due to dark matter, and the M_BH/M_dyn ratio is normal (~0.001).**

3. **THESAN-ZOOM simulations naturally produce a population of young galaxies with high M_BH/M_* ratios without invoking exotic black hole physics or modified gravity.**

4. **The predicted M_BH/M_* vs. M_* relation in simulations matches JWST JADES observations at z > 4, validating the dark-matter-dominated interpretation.**

5. **The result implies that black hole formation in the early universe does not require special mechanisms beyond standard accretion-dominated growth: high-z black holes are not anomalously large, but rather the host galaxies are anomalously small (in stellar content).**

6. **The gas-rich, dark-matter-dominated nature of high-z galaxies has implications for AGN feedback and galaxy evolution: feedback processes must operate in systems where dark matter provides most of the gravitational potential, affecting the efficiency of feedback.**

7. **The simulated evolution of M_BH/M_* from z ~ 6 to z ~ 0 (declining as galaxies assemble more stars and less dark matter relative to their black hole masses) is testable via observations of intermediate-z galaxies (z ~ 2-4).**

---

## Impact and Legacy

This paper has been influential for reframing the "overmassive black hole problem". Its impacts include:

- **Shifting perspective on early black holes**: By arguing that the black hole masses themselves are not anomalous, but rather the host galaxy compositions are, the paper offers a simpler explanation for LRD demographics.
- **Validating LCDM for high-z black holes**: The success of simulations in reproducing observed M_BH/M_* ratios without exotic physics argues that LCDM remains viable for early black hole formation.
- **Motivating dynamical mass measurements**: The importance of knowing M_dyn (not just M_*) for understanding black hole demographics drives future kinematic follow-up of high-z galaxies.
- **Constraining black hole seed formation**: If all black holes follow the M_BH ~ 0.001 M_dyn relation from early times, this constrains seed mass and formation mechanisms.

---

## Connection to Phonon-Exflation Framework

**Indirect connection via black hole growth in cosmological context.**

In the phonon-exflation framework, if the expansion history or matter power spectrum differs from LCDM at high redshift, this would affect the assembly of halo masses and the subsequent growth of black holes.

Specifically:

1. **Modified halo mass assembly**: If phonon-exflation produces different halo growth rates at z > 6, this would change M_DM and thus (via the M_BH ~ 0.001 M_dyn relation) change predicted black hole masses.

2. **Modified gas physics**: If the instanton relic affects gas cooling, ionization, or accretion at high z, this would change the gas fraction and thus the stellar mass assembly, altering the predicted M_BH/M_* ratios.

3. **Degeneracy with LCDM**: Since McClymont et al. demonstrate that LCDM simulations naturally reproduce observed M_BH/M_* ratios, a phonon-exflation model would need to produce *different* ratios to be distinguished from LCDM. Currently, both frameworks are degenerate at z < 7.

**Closest thematic link**: The M_BH/M_* demographics of LRDs serve as a benchmark for cosmological models. If future high-z black hole mass measurements (via direct kinematics) show that the M_BH-M_dyn relation differs from the assumed universal value, or if the evolution of M_BH/M_* from z ~ 6 to z ~ 0 deviates from LCDM predictions, this could distinguish phonon-exflation. The McClymont et al. framework provides tools for making such predictions in alternative cosmologies.
