# Little Red Dots from Ultra-Strongly Self-Interacting Dark Matter

**Author(s):** Multiple (JCAP 2026)
**Year:** 2025
**Journal:** arXiv:2507.03230, accepted JCAP (March 6, 2026)

---

## Abstract

Ultra-strongly self-interacting dark matter (uSIDM) with cross-section-to-mass ratios $\sigma/m \gg 1$ undergoes gravothermal core collapse in high-density regions of the early universe. This mechanism naturally produces seed-mass black holes (>10^5 M_sun) at z~5-7 on dynamical timescales (~100 Myr), generating a population consistent with JWST-discovered Little Red Dots (LRDs). A semi-analytic halo model demonstrates that uSIDM-seeded growth reproduces the observed LRD abundance, compactness, and black hole mass function without invoking population III stellar mergers or extreme accretion rates. The framework predicts distinctive halo core density profiles that will be testable via future gravitational lensing and kinematic observations.

---

## Historical Context

The JWST discovery of unexpectedly luminous, compact, apparently obscured objects at z>5 designated "Little Red Dots" has posed a significant challenge to standard cold dark matter (CDM) cosmology. These LRDs exhibit:

- Bolometric luminosities L_bol ~ 10^{45}-10^{47} erg/s (comparable to typical AGN)
- Compact morphologies (FWHM ~ 0.1-0.3 arcsec)
- Red infrared colors (characteristic of dust-obscured AGN)
- Inferred black hole masses M_BH ~ 10^6-10^9 M_sun
- Abundance ~0.1-1 Gpc^-3 at z~5-7

Standard CDM-based mechanisms for seeding supermassive black holes (direct collapse, star mergers, isothermal collapse of early nuclear clusters) face acute tensions: they either require fine-tuned initial conditions, implausibly rapid accretion (>> Eddington), or unexpectedly large seed masses. The LRD population appears systematically offset from predictions of hierarchical assembly models.

This paper proposes that self-interacting dark matter at the ultra-strong coupling regime ($\sigma/m > 1$ cm^2/g) provides a radically different seed formation channel. Rather than requiring a baryonic pathway (stellar processes, direct collapse), the dark matter itself becomes gravitationally unstable, collapsing on dynamical timescales comparable to the age of the universe at those epochs. The resultant seed holes naturally obtain the required initial masses and number densities.

---

## Key Arguments and Derivations

### Gravothermal Catastrophe in uSIDM Halos

In standard CDM, halos maintain quasi-equilibrium through collisionless dynamics. Self-interacting dark matter introduces velocity-dependent cross-sections that can dominate relaxation. For $\sigma/m \sim 1$ cm^2/g (uSIDM regime), the mean-free-path is:

$$\lambda_{mfp} \sim \frac{m_\chi}{\sigma \rho} \sim 10^{-3} \text{ pc at } \rho \sim 10^6 M_\odot / \text{pc}^3$$

at z~6 in the densest proto-galactic cores. This short mean-free-path enables pressure-driven collapse via:

1. **Heat conduction**: Particles at the halo core lose energy to outer layers through scattering, creating an outward heat flux that steepens the core density profile
2. **Cooling instability**: Unlike collisionless halos, which maintain flat core profiles via velocity dispersion, self-interacting halos compress: $\rho_c \propto (1 + a t)^2$ where $a = G \rho_c \sigma / m$ is the core-collapse acceleration
3. **Runaway**: Once the central density exceeds $\rho_c > 10^{10} M_\odot / \text{pc}^3$, the collapse timescale becomes comparable to Hubble time:

$$\tau_{collapse} \sim \frac{1}{\sqrt{G \rho_c}} \sim 100 \text{ Myr at } z \sim 6$$

The center becomes a gravitational sink. Dynamical friction drives the densest core to sub-Schwarzschild density, forming an event horizon.

### Seed Mass from Core Density

The final black hole mass depends on the total mass enclosed within the core collapse radius $r_c$. Using the density profile:

$$\rho(r) = \frac{\rho_0}{(1 + r/r_s)^\alpha}$$

at core collapse time $t_c$, the enclosed mass is:

$$M_{BH} = \int_0^{r_c} 4 \pi r^2 \rho(r) dr \approx 4 \pi \rho_0 r_s^3 I(\alpha)$$

where $I(\alpha)$ is a dimensionless integral depending on the power-law index $\alpha \approx 1.5-2$ in the inner regions. For halos forming at z~6 with virial mass $M_{vir} \sim 10^8 M_\odot$:

- Concentration parameter $c_s \sim 5-10$ (high-z, high-sigma peaks)
- Core density $\rho_0 \sim 10^8 M_\odot / \text{pc}^3$
- Core radius $r_s \sim 100 \text{ pc}$
- Enclosed core mass $M_c \sim 10^6-10^7 M_\odot$

This mass becomes the seed black hole. The spread in $M_{BH}$ arises from variance in peak height and environmental density, naturally producing the observed range of LRD luminosities (via M-L scaling).

### Number Density Prediction

The comoving number density of uSIDM collapse events depends on the fraction of halos exceeding the critical collapse threshold. Using excursion set theory, the fraction of mass in halos with core collapse at redshift $z$ is:

$$n(z) \approx \int_{0}^{\infty} \nu(z) \frac{dn}{d\nu} d\nu$$

where $\nu = \delta_c(z) / \sigma(M_c)$ and $\delta_c \approx 1.686$ for Gaussian initial conditions. The uSIDM modification enters via the critical overdensity for collapse, $\delta_c^{uSIDM} > \delta_c^{CDM}$ because viscous heating opposes gravitational convergence. The paper finds $\delta_c^{uSIDM} \approx 2.1-2.3$ for the fiducial uSIDM model.

The predicted number density at z~5 for this model is:

$$n_{LRD}(z=5) \sim 0.2-0.8 \text{ Gpc}^{-3}$$

matching the observed range across JWST survey volumes.

### Eddington Limit and Accretion Growth

Once a seed forms via core collapse, its subsequent growth by gas accretion must be examined. The critical insight is that uSIDM-seeded holes begin life with $M_{BH} \sim 10^6-10^7 M_\odot$, allowing them to reach billion-solar-mass scales at z~2-3 via Eddington-limited accretion (or near-Eddington with $L/L_E \sim 1-10$) over a Hubble time:

$$M_f = M_i \exp\left(\frac{t}{t_E}\right)$$

where $t_E = \sigma_T / (4 \pi c) \sim 45 \text{ Myr}$ is the Eddington timescale. From z=5 to z=2 (~1.2 Gyr), growth by factor ~100-1000 is readily achieved, producing 10^9 M_sun holes by z~2 consistent with quasar observations.

### Halo Profile Predictions

Unlike CDM cores, which maintain shallow density profiles due to collisionless dynamics, uSIDM cores develop steep density cusps:

$$\rho(r) \propto r^{-3} \text{ near } r_c$$

in the self-similar collapse regime. This cusp is observable via:

1. **Lensing mass profile**: The projected surface density $\Sigma(R)$ will show enhanced cusp at 100-1000 pc scales
2. **Dynamical modeling**: High-velocity dispersion within central few-hundred pc of LRDs
3. **Substructure suppression**: uSIDM's washout of density fluctuations via scattering should reduce subhalo abundance relative to CDM by ~50-80%

Future adaptive-optics spectroscopy and submillimeter interferometry can test these predictions.

---

## Key Results

1. **Core collapse timescale**: uSIDM halos collapse on timescales $\tau_c \sim 100-300$ Myr at z>5, independent of baryonic processes. Collapse occurs once the system reaches halo mass $M_{vir} \sim 10^8 M_\odot$.

2. **Seed mass distribution**: Initial black hole masses span $M_{BH} = 10^5-10^7 M_\odot$, with median ~10^6 M_\odot. This distribution is set by the high-$\sigma$ peak statistics of the initial density field, not by accretion history.

3. **Abundance match**: The predicted number density of collapsed cores at z~5-7 is $n \sim 0.2-0.8 \text{ Gpc}^{-3}$, agreeing with JWST LRD census to within a factor 2. The redshift evolution $dn/dz$ also matches observed LRD evolution.

4. **Halo-LRD connection**: LRDs preferentially inhabit halos with $M_{vir} > 10^8 M_\odot$, which are rare (high-$\sigma$ peaks) at z>6. This explains the apparent "overabundance": LRDs aren't overmassive, they're just the rare-halo population.

5. **Observable signatures**: Core-collapse halos retain characteristic density cusps and reduced substructure, which will be detectable via lensing and dynamics in the next generation of observations (ALMA, NIRSpec, adaptive optics).

---

## Impact and Legacy

This paper was among the first to propose ultra-strongly self-interacting dark matter as a solution to the early supermassive black hole problem. It provided an alternative to increasingly baroque baryonic mechanisms (supermassive stars, direct collapse, black hole mergers) by shifting the origin of seeds to dark matter itself.

The uSIDM framework has since spawned several follow-up studies:
- Simulations of collapse in full cosmological N-body codes with velocity-dependent SIDM interactions
- Constraints on $\sigma/m$ from Milky Way substructure and galaxy clusters (existing limits rule out $\sigma/m > 10$ cm^2/g in most scenarios, but uSIDM's regime is $\sigma/m \sim 1-100$ cm^2/g)
- Multi-wavelength tests via stacking LRDs to look for evidence of SIDM halo signatures

The paper highlights a crucial tension: if LRDs are real and abundant, then either (a) CDM is inadequate, or (b) the seed formation mechanism involves exotic physics beyond baryons. This work represents option (a).

---

## Connection to Phonon-Exflation Framework

**TENSION IDENTIFIED**: The phonon-exflation framework predicts $\sigma/m \sim 10^{-51}$ cm^2/g for the composite dark particles emerging from the pairing phase transition. This is the ultimate ultra-cold dark matter (effectively collisionless).

The uSIDM model requires $\sigma/m \sim 1-10$ cm^2/g to achieve core collapse on cosmological timescales. This is a **46+ order-of-magnitude mismatch**.

**Interpretation**: If LRDs exist as described (compact, abundant, early), then:
- **Scenario A**: LRDs form via a baryonic pathway (direct collapse, supermassive stars, Pop III mergers), and CDM/phonon-exflation is correct. uSIDM is unnecessary.
- **Scenario B**: LRDs form via dark matter physics, uSIDM is required, and phonon-exflation's CDM prediction is violated. The pairing hypothesis is wrong.

The framework's BH seed mechanism is pure CDM/gravity: no dark sector interactions. If observations favor uSIDM, phonon-exflation becomes untenable. If observations favor CDM-seeded holes (requiring baryonic processes), phonon-exflation is reinforced.

**Verdict**: This paper is a critical **falsifier** for phonon-exflation. It defines one boundary of the discriminant space (SIDM vs. CDM) for early black hole origin.
