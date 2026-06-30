# Dark Matter Annihilation in the Circumgalactic Medium at High Redshifts

**Author(s):** Sarah Schon, Katherine J. Mack, Stuart B. Wyithe
**Year:** 2017
**Journal/ArXiv:** arXiv:1706.04327

---

## Abstract

Dark matter annihilation has been proposed as a potential source of energy injection into the early universe, with the potential to affect galaxy formation and reionization. This work develops an energy deposition model to investigate how annihilating dark matter affects the circumgalactic medium (CGM)--the ionized/neutral hydrogen and metals surrounding galaxies--during the early universe. The authors model neutralino-like dark matter candidates and their annihilation products across various particle masses and decay channels, computing ionization and heating effects in the circumgalactic medium around dark matter halos of 10^5-10^7 solar masses at high redshifts (z=20 and z=40). The results indicate that dark matter annihilation significantly increases the minimum star-forming mass scale in the earliest galaxies by factors of 2-3 at z=20 and 4-5 at z=40 for some dark matter models, with profound implications for early structure formation.

---

## Historical Context

The early universe presents a unique laboratory for dark matter physics. In the first billion years (z>6), when galaxies were assembling for the first time from primordial density fluctuations, the ionization state of the intergalactic medium and circumgalactic medium was critical for galaxy formation. Any significant energy injection from exotic processes--such as dark matter annihilation, primordial black hole decay, or other beyond-Standard-Model physics--could fundamentally alter the thermodynamic state of gas and suppress or enhance star formation.

Dark matter annihilation signals have been searched for in the local universe and at high redshift through indirect detection experiments and astrophysical observations. However, a complementary approach is to ask: if dark matter annihilation is occurring at any significant level in the early universe, what observable consequences would result? Schon et al. address this question by computing how the energy deposition from annihilation products affects the circumgalactic medium around the earliest forming galaxies.

The circumgalactic medium--the halo of ionized and neutral gas surrounding and between galaxies--plays a crucial role in galaxy formation. It sets the gas temperature, ionization state, and metal enrichment, all of which affect star formation. Understanding CGM properties at high redshift is essential for interpreting observations from the James Webb Space Telescope and future 21-centimeter observations.

---

## Key Arguments and Derivations

### Dark Matter Annihilation Energy Deposition

Dark matter annihilation produces a reaction cross section times relative velocity $\langle \sigma v \rangle$ and results in the production of Standard Model particles (or other decay products, depending on the dark matter model). For neutralino-like candidates, common annihilation channels include:

$$\chi \bar{\chi} \to b \bar{b}, \quad W^+ W^-, \quad \tau^+ \tau^-, \quad ZZ, \quad hh$$

The annihilation power per unit volume scales with the square of local dark matter density:

$$\dot{E}(r) = \frac{1}{2} n_\chi(r)^2 \langle \sigma v \rangle m_\chi c^2$$

where $n_\chi(r)$ is the dark matter number density at radius $r$ from the halo center, and $m_\chi$ is the dark matter particle mass. The factor of 1/2 accounts for the fact that annihilation involves pairs.

### Energy Deposition in Circumgalactic Medium

The energy from annihilation products (after hadronization and decay) is deposited into the circumgalactic gas through ionization and heating. The primary processes are:

1. **Ionization**: Fast electrons from annihilation cascade ionize neutral hydrogen and helium
2. **Heating**: The residual energy heats the already-ionized gas, increasing temperature and thermal energy density

The ionization rate per hydrogen atom can be parameterized as:

$$\zeta(r) = A \times f_{ion} \times \dot{E}(r) / E_{ion}$$

where $A$ is a numerical factor accounting for cascade efficiency, $f_{ion}$ is the fraction of energy going into ionization (vs. heating), and $E_{ion} \approx 13.6$ eV is the typical ionization energy. The heating rate is similarly:

$$\Gamma(r) = f_{heat} \times \dot{E}(r) / n_b(r)$$

where $f_{heat}$ is the fractional energy in heating and $n_b(r)$ is the baryon number density.

### Circumgalactic Medium Model

The circumgalactic structure is modeled as a hydrostatic atmosphere in equilibrium with the gravitational potential of the dark matter halo. The density profile of the CGM follows:

$$n_b(r) = n_{b,0} \left( \frac{r}{r_0} \right)^{-\alpha}$$

where typical values are $\alpha \sim 1-2$. The temperature and ionization state adjust according to the energy balance between heating/ionization and radiative cooling.

### Jeans Mass and Star Formation

Star formation is suppressed in gas that is too hot or too ionized to cool efficiently on galaxy formation timescales. The Jeans mass--the minimum mass that can cool and collapse to form a star--is:

$$M_J = \left( \frac{\pi}{6G^3 \rho} \right)^{1/2} T^{3/2}$$

where $\rho$ is the gas density and $T$ is the temperature. If dark matter annihilation heats the circumgalactic gas to higher temperatures, the Jeans mass increases, suppressing star formation in low-mass systems.

### Model Parameters

The authors consider:

- **Dark matter mass range**: Neutralino candidates with $m_\chi$ = 10 GeV to 1 TeV
- **Annihilation cross section**: Thermal relic value $\langle \sigma v \rangle \sim 3 \times 10^{-26}$ cm$^3$/s (and variations)
- **Halo mass range**: $10^5$ to $10^7 M_\odot$ (minihalos and dwarf galaxy hosts)
- **Redshifts**: z=20 (early star formation) and z=40 (pre-reionization)

---

## Key Results

1. **Circumgalactic medium ionization and heating**: Dark matter annihilation produces significant ionization fractions in the circumgalactic medium surrounding small halos. At z=20 with m_chi = 100 GeV and thermal relic cross section, ionization extends to distances of 10-100 physical kpc from halo centers, depending on halo mass and dark matter density profile.

2. **Temperature elevation**: The thermal energy injection from annihilation products increases the circumgalactic gas temperature by factors of 2-10 relative to the primordial case, depending on model parameters. Higher-mass dark matter particles produce more energetic products and greater heating.

3. **Jeans mass suppression**: The increase in Jeans mass due to heating and ionization is most severe for smaller halos. For 10^5 solar mass halos at z=40:
   - Standard (no annihilation) Jeans mass: ~10^5 solar masses
   - With annihilation (m_chi = 100 GeV): Jeans mass increases by factor of 4-5 to ~5×10^5 solar masses
   - This suppresses star formation in the smallest systems by up to a factor of 10

4. **Redshift dependence**: The effect is more pronounced at higher redshifts (z=40 vs. z=20), where the circumgalactic gas density is higher and the annihilation power density scales as (1+z)^6 from structure formation increases.

5. **Dark matter mass dependence**: Heavier dark matter particles produce more ionization/heating per annihilation event, with a roughly logarithmic dependence on particle mass across the range studied. The thermal relic cross section value is near the lower end of parameters producing detectable CGM effects.

6. **Channel dependence**: Annihilation channels producing more energetic particles (e.g., W^+W^- vs. tau^+tau^-) produce more heating and ionization.

---

## Impact and Legacy

This work contributes to the nascent field of early-universe dark matter physics, exploring how beyond-Standard-Model dark matter might leave observable imprints on galaxy formation and reionization. The result that dark matter annihilation can suppress star formation in minihalos has implications for:

1. The Planck satellite's constraints on ionizing photon production
2. Reionization timescale and morphology
3. The abundance of the first galaxies
4. Future 21-centimeter and optical observations of the high-redshift universe

The paper establishes that dark matter annihilation could be a competitive energy source with stars and active galactic nuclei in the early universe, motivating further investigation of annihilation signatures in reionization-era observations.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation framework, dark matter is not a relic particle species but an emergent collective excitation (phonon) of the M4 x SU(3) geometric substrate. This fundamental difference has profound implications for Schon et al.'s study of dark matter annihilation effects.

In the framework:

1. **Dark matter "annihilation" is not a particle process** but rather a scattering or decay of phononic modes back into the substrate. The energy deposition mechanism differs fundamentally from WIMP annihilation.

2. **Density-squared coupling**: The framework predicts that dark matter-baryon coupling and energy transfer rates depend on the spectral action of the compactified geometry. The energy deposition rate would scale with dark matter density in a way determined by the geometry, not by a particle physics annihilation cross section.

3. **Circumgalactic medium effects**: If dark matter emerges from internal geometry, the circumgalactic medium's properties would be coupled to the local compactification state. Regions with stronger or weaker geometric effects would exhibit different dark matter densities and corresponding different heating/ionization rates.

4. **Alternative to suppressed star formation**: Rather than suppressing star formation through heating, the framework predicts that the spectral properties of the geometric dark matter could enhance or suppress structure formation through more subtle mechanisms involving the form of the power spectrum itself (which the framework predicts differs from CDM at small scales).

5. **Halo mass dependence**: The strong redshift and halo mass dependence of Schon et al.'s results could be reinterpreted as probing how the geometric dark matter density and coupling evolve across cosmic time and across halos of different sizes.

The framework's prediction of specific dark matter density profiles and interactions encoded in geometry could be tested by comparing predicted CGM ionization and heating profiles with future observations from JWST and 21-cm facilities. The pattern of star formation suppression as a function of halo mass and redshift would differ from WIMP predictions if dark matter emerges from the compactified geometry rather than existing as a particle species.
