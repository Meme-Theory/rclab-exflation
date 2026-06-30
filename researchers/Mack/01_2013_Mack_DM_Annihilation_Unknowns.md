# Known Unknowns of Dark Matter Annihilation Over Cosmic Time

**Author(s):** Katherine J. Mack
**Year:** 2013
**Journal/ArXiv:** arXiv:1309.7783v2

---

## Abstract

Dark matter self-annihilation holds promise as one of the most robust mechanisms for the identification of the particle responsible for the Universe's missing mass. In this work, Mack examines the evolution of the dark matter annihilation power produced by smooth and collapsed structures over cosmic time, taking into account uncertainties in the structure of dark matter halos. As observations search for signatures of annihilation, understanding this time evolution helps direct observational efforts, either with local measurements or investigation of effects on the intergalactic medium at high redshift. Several key sources of uncertainty significantly affect predictions: the density profile of dark matter halos; the small-scale cutoff in the halo mass function; the redshift-dependent mass-concentration relation for small halos; and the particle-velocity dependence of the annihilation process. Varying these quantities can result in annihilation power predictions that differ by several orders of magnitude.

---

## Historical Context

Dark matter identification efforts face a large set of inconclusive or contradictory results in indirect and direct detection experiments. This confusing state of affairs highlights the importance of seeking alternative probes of dark matter's properties. Mack explores one promising avenue: modeling the consequences of dark matter annihilation on the local baryonic medium in which dark matter halos reside. The form and ultimate impact of energy deposition when annihilation occurs depends strongly on density, temperature, ionization state, and redshift.

A key insight is that knowing the total annihilation power being produced by dark matter halos at a given redshift (per unit volume) is instructive for determining if there is a "sweet spot" in which to look for signs of local energy injection, where total annihilation power is higher than at other times in cosmic structure evolution. Understanding this evolution is a first step to understanding the overall impact of dark matter annihilation on baryonic structures and the evolution of stars and galaxies.

The structure of dark matter halos, especially at the lowest masses, is difficult to observe directly or to simulate at mass scales below those of galaxy clusters. Knowledge of low-mass structures is generally an extrapolation from properties of halos at higher masses. The choices made in these extrapolations over several orders of magnitude strongly affect predictions of annihilation power, making careful examination of these assumptions essential before robust predictions can be applied to future observations.

---

## Key Arguments and Derivations

The annihilation rate per unit volume of weakly interacting massive particle (WIMP) dark matter is proportional to the square of the local dark matter density, since annihilation is a two-particle process. Mack separates the dark matter annihilation rate density A(z) into two components:

**Smooth component (uncollapsed regions):**

$$A_{sm}(z) = \langle \sigma v \rangle^2 m_\chi^2 \rho_{DM,0}^2 (1+z)^6$$

**Structure component (within collapsed halos):**

$$A_{struct}(z) = \langle \sigma v \rangle^2 m_\chi^2 \int_{M_{min}}^{M_{max}} \left[ \frac{dn}{dM}(z,M)(1+z)^3 \int_{V_{vir}} \rho_{DM}^2(r,z,M) dV \right] dM$$

where $\langle \sigma v \rangle$ is the thermally averaged annihilation cross section, $m_\chi$ is the dark matter particle mass, $\rho_{DM,0}$ is the mean dark matter density at redshift 0, $\frac{dn}{dM}(z,M)$ is the comoving number density of halos of mass M, and $\rho_{DM}(r,z,M)$ represents the dark matter halo radial density profile. The volume integral extends over $V_{vir}$, the volume out to the virial radius.

The total annihilation rate is approximately:

$$A(z) \approx A_{sm}(z) + A_{struct}(z)$$

though this approximation double-counts dark matter in halos and overestimates void density. At volume-averaged power per unit volume:

$$P(z) = 2 m_\chi c^2 A(z)$$

For comparison with other studies, power per hydrogen nucleus is useful:

$$P_H(z) = P(z) / n_H(z)$$

where $n_H(z) = \Omega_{b,0} \rho_{crit,0} (1 - Y_p) (1+z)^3 / m_H$, with $\Omega_{b,0}$ the present baryon density, $\rho_{crit,0}$ the critical density, $Y_p = 0.2477$ the primordial helium fraction, and $m_H$ the proton mass.

### Dark Matter Halo Modeling

To calculate annihilation rate requires models for five key properties: (1) dark matter particle properties $\langle \sigma v \rangle$ and $m_\chi$; (2) halo mass function $\frac{dn}{dM}(z,M)$; (3) minimum and maximum mass cutoffs $M_{min}$ and $M_{max}$; (4) halo density profile $\rho_{DM}^2(r,z,M)$; (5) mass-concentration relation $c(z,M)$.

**Density Profiles:** Mack considers three forms commonly applied to dark matter halos:

NFW profile (Navarro, Frenk & White):
$$\rho_{NFW}(r) = \frac{\rho_s(z,M)}{(r/r_s)(1+r/r_s)^2}$$

Einasto profile:
$$\rho_{Ein}(r) = \rho_{E,0}(z,M) \exp\left[-\frac{2}{\alpha_E}\left(\left(\frac{r}{r_s}\right)^{\alpha_E} - 1\right)\right]$$

Burkert profile (cored):
$$\rho_{Burk}(r) = \frac{\rho_{B,0}(z,M)}{(1+r/r_0)(1+(r/r_0)^2)}$$

Since annihilation depends on density squared, the shape of the inner profile strongly influences total annihilation output. Baryonic feedback effects such as supernova feedback can alter inner density profiles, in some cases creating "cored" halos where density reaches a plateau.

**Mass-Concentration Relation:** The concentration parameter $c = r_{vir}/r_s$ determines central density concentration. While two halos with identical mean density can have different annihilation outputs if concentration differs, changes to the squared-density term affect power output through the $\rho_{DM}^2$ term in the structure integral. Four mass-concentration relations are considered: (1) Comerford & Natarajan (2007) from cluster observations; (2) Duffy et al. (2008) from simulations; (3) Ludlow et al. (2013a) from the Millennium Simulation; (4) a flat mass-concentration relation with no mass dependence.

### Minimum Mass Cutoff

The smallest halos at which collapsed structures persist and form depends on (1) primordial power spectrum; (2) dark matter particle species; (3) particle mass; (4) ability of microhalos to persist under tidal forces during hierarchical merging. Estimates vary widely, from $10^{-11} M_\odot$ to $10^{-4} M_\odot$ for cold dark matter, and significantly more restrictive for warm dark matter. The choice of minimum mass cutoff has a strong effect on annihilation power, especially at early times, because small-mass halos dominate halo populations at all redshifts.

---

## Key Results

1. **Fiducial model behavior**: Using standard parameters ($\langle \sigma v \rangle = 10^{-26}$ cm$^3$/s, $m_\chi = 100$ GeV, Reed et al. mass function, $M_{min} = 10^{-9} M_\odot$, NFW density profile, Duffy et al. mass-concentration relation), the structure component dominates over smooth component at late times as structure formation proceeds. Peak annihilation power occurs around redshift 10-40 (primordial star formation epoch), where structure component is almost four orders of magnitude stronger than smooth component.

2. **Mass function dependence**: Choice of halo mass function (Reed et al., Press-Schechter, Sheth-Tormen) can alter annihilation signal by factor of 3-4 around redshift 10-40 (early star formation). Differences are largest at very high redshift (z > 80) where smooth component dominates.

3. **Density profile effects**: NFW and Einasto profiles produce similar results (matched to high-mass halo observations). Cored Burkert profile produces dramatic (factor of 3) decrease in annihilation power at low redshifts. However, feedback model (cores only in halos above 1 solar mass) has negligible effect on total power, remaining nearly indistinguishable from fiducial model.

4. **Minimum mass cutoff dominance**: The lower-mass cutoff has strongest effect on total power, especially at early times. Varying $M_{min}$ from $10^{-9} M_\odot$ to $10^{-6} M_\odot$ shifts redshift at which collapsed halos dominate by $\Delta z \sim 35$. At z~35, difference between predictions is approximately two orders of magnitude. Warm dark matter cases with $M_{min} = 10^7 M_\odot$ delay structure dominance until redshift ~20 (already into star formation epoch).

5. **Mass-concentration relation dominance**: Using Comerford & Natarajan (2007) relation derived from cluster observations predicts annihilation power 2-4 orders of magnitude larger than fiducial case. Flat mass-concentration relation reduces power below fiducial case by approximately two orders of magnitude at early star formation epoch. These alterations also shift redshift at which structure component dominates: from z~110 (CN relation) to z~80 (fiducial) to z~50 (flat relation).

6. **Overall prediction range**: Plausible models produce predictions spanning multiple orders of magnitude across cosmic time. Full range illustrated in Figure 7, with red shaded region showing variability for cold dark matter models and thin dashed lines extending outside this range for warm dark matter cases.

---

## Impact and Legacy

This work demonstrates that robust estimation of cosmological annihilation signals requires resolving several key sources of model uncertainty through combination of observation and modeling. The identification of dark matter halos through their gravitational signatures, combined with improved simulations of halo structure at all mass scales, is essential. The framework provides a methodological foundation for assessing sensitivity of indirect detection strategies to assumptions about dark matter halo structure.

Key implications: (1) The dominant contribution to annihilation power comes from the smallest, most numerous halos, which are the least directly observable; (2) A "sweet spot" in cosmic history (z~20-40) provides peak annihilation signal, suggesting observational focus on high-redshift cosmic dawn and reionization epoch; (3) Annihilation effects on intergalactic medium at high redshift could be consequential for first star and galaxy formation; (4) Velocity-dependent annihilation (Sommerfeld enhancement, p-wave) would shift relative importance of smooth versus structure components.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation cosmology, dark matter arises as collective phononic excitations of the M4 x SU(3) geometric substrate undergoing internal compactification. The framework predicts dark matter density and structure fundamentally differ from CDM: particles are emergent quasiparticles with density-dependent interactions encoded in the spectral action of the compactified geometry, rather than relics from thermal freeze-out.

Mack's uncertainty quantification becomes reframed in phonon-exflation context: instead of uncertain halo density profiles, velocity-dependent cross-sections, and mass-concentration relations extrapolated over orders of magnitude, the framework provides deterministic geometric density profiles from KK reduction and spectral geometry. The annihilation power evolution would follow from the geometry's evolution, not from WIMP freeze-out assumptions. The "known unknowns" (halo structure, small-scale cutoff, mass-concentration) map to testable predictions about particle-field coupling derived from the geometry itself. The framework's prediction of w=-1 dark energy further differs from annihilation-based energy injection scenarios, suggesting alternative mechanisms for early-universe energy balance that do not rely on velocity-dependent cross-section enhancements (Sommerfeld, p-wave).

The density-squared dependence of annihilation ($\propto \rho^2$) highlighted by Mack maps directly to nonlinear spectral action terms in geometric dark matter models, where annihilation signatures would encode information about the underlying compactification fold and its stability properties.
