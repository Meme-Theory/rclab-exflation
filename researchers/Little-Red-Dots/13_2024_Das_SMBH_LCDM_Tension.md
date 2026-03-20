# Seeds of Supermassive Black Holes in General Relativistic and Alternative Cosmologies: Implications of Massive Seeds

**Author(s):** Nirmali Das, Sanjeev Kalita, Ankita Kakati, and collaborators

**Year:** 2024

**Journal:** Physics of the Dark Universe (volume 46, article 101631; arXiv ID needs verification -- listed as 2601.22991 but journal publication year 2024 is inconsistent with a January 2026 arXiv submission)

---

## Abstract

This theoretical paper systematically investigates the early supermassive black hole (SMBH) problem—the tension between observed SMBHs at z>6 (masses M_BH > 10^9 M_sun) and the difficulty of assembling such masses within the available cosmic time in standard ΛCDM—across multiple cosmological frameworks including General Relativity (GR) and alternative theories (modified gravity, quintessence, etc.). Das et al. parameterize SMBH growth via a "seed mass" m_seed and accretion efficiency, then solve the black hole mass evolution equations in different cosmological backgrounds. Key results: (1) Light seeds (m ~ 100 M_sun) require either extremely early seeding (z > 30) or sustained super-Eddington accretion (lambda_Edd >> 1) to reach 10^9 M_sun by z=6, challenging under ΛCDM assumptions of quiescence early in cosmic history. (2) Intermediate seeds (m ~ 10^3--10^4 M_sun) are more viable but still demand early formation. (3) Heavy seeds (m ~ 10^5 M_sun) from direct collapse nearly eliminate the growth timescale problem but require special conditions. (4) Most importantly, the paper shows that different cosmologies (ΛCDM vs. modified gravity) predict different structure formation histories and hence different rates at which black hole seeds form and are available for early accretion. (5) Little Red Dots, with their inferred masses 10^6--10^8 M_sun at z~4--8, directly constrain the seeding scenario and thus provide a test of cosmology-dependent structure formation. The paper concludes that the SMBH problem is fundamentally a structure-formation problem and thus a powerful probe of cosmological models.

---

## Historical Context

The "early SMBH problem" or "super-massive black hole crisis" emerged following the discovery of billion-solar-mass SMBHs at z>6. Notable examples include:

- SDSS J1148+5251 at z=6.4: M_BH ~ 3 × 10^9 M_sun (though recent work questions this estimate)
- ULAS J1342+0928 at z=7.5: M_BH ~ 8 × 10^9 M_sun
- More recently, JWST observations at z>10 confirming SMBHs at earlier times

In standard ΛCDM with Einstein-de Sitter early behavior (matter-dominated universe for z > z_eq ~ 3000), the growth of density perturbations follows the linear growth factor:

$$D(a) \propto a$$

for z >> 1. However, at z~6--10, the universe is still evolving from matter-domination to dark-energy-domination, and the structure growth rate slows compared to the Einstein-de Sitter case. The cumulative effect is that by z=6, density perturbations have only grown by a factor ~ 10^2--10^3 since primordial (z~10^3) times, not the 10^5--10^6 needed if the universe started with primordial black hole seeds of mass m_seed ~ 10^{-8} M_sun (from primordial density fluctuations).

Thus, seeds must be much heavier (10^2--10^5 M_sun) or must form via later-generation mechanisms (stellar collapse, runaway collisions, direct collapse). This realization catalyzed theoretical work on alternative seeding scenarios and also raised the question: **Does the SMBH problem indicate a failure of ΛCDM or merely require revision of seeding assumptions?**

Das et al. addressed this by examining the problem across multiple cosmologies.

---

## Key Arguments and Derivations

### SMBH Mass Evolution Equation

The fundamental equation governing black hole mass growth is:

$$\frac{dM_{BH}}{dt} = \epsilon \, \lambda_{Edd} \, \dot{M}_{Edd}$$

where epsilon is the radiative efficiency (epsilon ~ 0.1 for thin disks), lambda_Edd is the Eddington ratio (L/L_Edd), and dot{M}_{Edd} is the Eddington accretion rate:

$$\dot{M}_{Edd} = \frac{L_{Edd}}{c^2 \epsilon} \propto M_{BH}$$

Substituting:

$$\frac{dM_{BH}}{dt} = \lambda_{Edd} \times f(M_{BH})$$

For constant lambda_Edd, this integrates to:

$$M_{BH}(t) = m_{seed} \exp(\lambda_{Edd} \, t / t_{Edd})$$

where t_Edd ~ 0.5 Gyr is the Eddington timescale (time for a black hole to double in mass at L = L_Edd).

### Growth Timescale Calculation

To grow from m_seed to M_target in cosmic time t_cosmic requires:

$$t_{cosmic} = t_{Edd} \times \frac{\ln(M_{target} / m_{seed})}{\lambda_{Edd}}$$

Examples:

**Light Seed (m = 100 M_sun) to M_target = 10^9 M_sun by z=6 (t_cosmic ~ 1 Gyr)**:

$$1 \, \text{Gyr} = 0.5 \, \text{Gyr} \times \frac{\ln(10^9 / 10^2)}{\lambda_{Edd}} = 0.5 \times \frac{16}{lambda_{Edd}}$$

$$\lambda_{Edd} = 8$$

Required: continuous super-Eddington accretion (factor of 8x), very challenging for Eddington-limited flows.

**Intermediate Seed (m = 10^4 M_sun) to 10^9 M_sun by z=6**:

$$1 \, \text{Gyr} = 0.5 \, \text{Gyr} \times \frac{\ln(10^5)}{lambda_{Edd}} = 0.5 \times \frac{11.5}{\lambda_{Edd}}$$

$$\lambda_{Edd} \sim 5--6$$

Still requires super-Eddington, but less extreme.

**Heavy Seed (m = 10^5 M_sun) to 10^9 M_sun**:

$$1 \, \text{Gyr} = 0.5 \, \text{Gyr} \times \frac{\ln(10^4)}{\lambda_{Edd}} = 0.5 \times \frac{9.2}{\lambda_{Edd}}$$

$$\lambda_{Edd} \sim 4--5$$

Most viable under Eddington-limited accretion, though still challenging.

### Cosmology-Dependent Structure Formation

The rate at which halos collapse and reach densities sufficient for black hole seeding depends on the growth rate of density perturbations, described by the growth factor D(a) and linear growth rate f(a) = d ln D / d ln a.

In ΛCDM:

$$D(a) = \frac{1}{a} \frac{\int_0^a da'/a'^3 E(a')^{-3}}{\int_0^1 da'/a'^3 E(a')^{-3}}$$

where E(a) = H(a) / H_0 is the normalized Hubble parameter:

$$E(a)^2 = \Omega_m a^{-3} + \Omega_\Lambda$$

For a = 0.2 (z=4):

$$E(0.2)^2 \approx 0.3 \times (0.2)^{-3} + 0.7 \approx 4.3 \times 10^1 + 0.7 \approx 43$$

$$E(0.2) \approx 6.5$$

The growth rate at z=4 is:

$$f(z=4) \approx 0.37$$

This relatively slow growth rate at z~4--6 (compared to the z >> 1 regime) limits the availability of overdense regions capable of hosting rapidly-growing black holes.

In alternative cosmologies (modified gravity, quintessence), E(a) differs, leading to different D(a) and f(a). For instance:

- **Faster Early Growth** (some modified gravity models): D(z) increases more steeply at z > 5, allowing earlier black hole formation and more rapid initial growth.
- **Slower Early Growth** (models with higher dark energy at early times): D(z) increases more slowly, exacerbating the SMBH problem.

### Seeding Scenario Comparison

Das et al. compute the abundance of black hole seeds as a function of redshift and halo mass, accounting for cosmology-dependent structure formation. Results show:

1. **ΛCDM with Light Seeds**: Few seeds form at z > 15; those that do form undergo slow initial growth. By z=6, only ~1% of halos host black holes of M > 10^9 M_sun. **Inconsistent with observations showing abundant SMBHs.**

2. **ΛCDM with Intermediate Seeds**: More abundant at z~10--15. Growth to 10^9 M_sun by z=6 is marginal; ~10--20% of halos might achieve this. **Borderline consistency with observations.**

3. **ΛCDM with Heavy Seeds (10^5 M_sun)**: Few in number but grow efficiently. By z=6, ~50% could reach 10^9 M_sun. **Consistent with observations but requires special formation mechanism.**

4. **Modified Gravity (faster early growth)**: Slightly eases the problem; seeds form earlier and grow faster. Could make light-seed scenario more viable.

5. **Modified Gravity (slower early growth)**: Worsens the problem; requires even heavier seeds.

### Little Red Dots as Evolutionary Markers

Little Red Dots at z~4--8 with M_BH ~ 10^6--10^8 M_sun are intermediate in the black hole mass spectrum. Their abundance and properties constrain the seed population and growth history:

- High abundance of z~4 black holes (10^6--10^8 M_sun) requires either abundant seeds at z>10 or very efficient growth from lighter seeds.
- Compact morphologies and high Eddington ratios (lambda_Edd ~ 1--5) suggest rapid, super-Eddington-dominated growth.
- Dust-obscuration prevalence suggests rapid growth occurs in dusty, merger-driven environments.

The paper uses LRD demographics to constrain seeding models: the observed LRD abundance requires seed formation efficiency ~1--10% in halos M > 10^6--10^7 M_sun at z > 15, far higher than predicted for light seeds in standard scenarios but achievable with intermediate or heavy seeds.

---

## Key Results

1. **Light Seeds Disfavored**: Cannot easily produce observed SMBH abundances at z>6 without implausibly high Eddington ratios (lambda_Edd > 10) or non-standard physics.

2. **Intermediate Seeds Viable**: m ~ 10^3--10^4 M_sun seeds can produce observed SMBH population if seeding efficiency is high (~1--10%).

3. **Heavy Seeds Preferred**: m ~ 10^5 M_sun seeds most naturally explain both z>6 SMBHs and z~4 LRDs with minimal fine-tuning.

4. **Cosmology Matters**: Different cosmologies predict different structure growth rates and thus different black hole seeding and growth rates. SMBH observations can constrain cosmology.

5. **LRDs as Constraint**: The abundance of 10^6--10^8 M_sun black holes at z~4--8 directly constrains the seed population and growth history, ruling out some seeding scenarios.

6. **ΛCDM Viable but Requires Heavy Seeds**: Standard ΛCDM can accommodate observed SMBH population if seeds are massive (10^5 M_sun from direct collapse or primordial), but this is less economical than light seeds and requires special conditions.

---

## Impact and Legacy

1. **Seeding Scenario Taxonomy**: Provided systematic framework for comparing different SMBH formation pathways (light, intermediate, heavy seeds) in standard and alternative cosmologies.

2. **Observational Constraints**: Showed how SMBH abundance at different redshifts constrains seeding models, elevating SMBH observations to a cosmological test.

3. **LRD Significance**: Elevated Little Red Dots from a curiosity to a major constraint on black hole formation physics and cosmology.

4. **Alternative Cosmology Consideration**: Opened door to using SMBH observations to distinguish between ΛCDM and modified-gravity models.

---

## Connection to Phonon-Exflation Framework

The Das et al. framework directly applies to the phonon-exflation model by providing a method to extract cosmology-dependent predictions of black hole seeding and growth. The phonon-exflation framework predicts specific values of H(z) and growth rate f(z) that would yield distinct predictions for SMBH abundance at different redshifts.

**Connections**:

1. **Structure Growth Rate**: Phonon-exflation's predicted H(z) determines d(delta)/dz and f(z) via the growth rate equations. Different H(z) from phonon-exflation vs. ΛCDM would lead to different black hole seeding rates and abundances at z>10.

2. **SMBH Abundance Test**: The observed SMBH and LRD abundances at z~4--8 directly constrain the structure growth rate predicted by any cosmological model. Phonon-exflation's predictions can be tested against these observations.

3. **Halo Mass Function**: Phonon-exflation predicts a different halo mass function at z>10 due to modified growth rates. This directly affects the abundance of halos capable of hosting black hole seeds.

4. **Seed Formation Rate**: The rate at which sufficiently-dense regions form for direct collapse (or other seeding mechanisms) depends on the growth factor D(z), which is cosmology-dependent. Phonon-exflation's unique H(z) would lead to unique predictions for DCBH formation rates.

5. **Quantitative Test**: By computing D(z) and f(z) under phonon-exflation assumptions, one can predict the expected SMBH mass function at z~4--8, then compare to observations. Agreement or disagreement tests the framework.

**Intensity**: High. The Das et al. framework provides a direct method to test cosmological models (including phonon-exflation) against SMBH and LRD observations. This is one of the most powerful ways to constrain early-universe expansion and structure formation, fundamental to distinguishing between ΛCDM and alternatives.

---

## Key Equations Summary

| Quantity | Equation | Comment |
|----------|----------|---------|
| BH Mass Evolution | $M_{BH}(t) = m_{seed} \exp(t/t_{Eff})$ | t_Eff = t_Edd / lambda_Edd |
| Eddington Timescale | t_Edd ~ 0.5 Gyr | Time to double mass at L = L_Edd |
| Required Growth Time | $t_{cosmic} = t_{Edd} \ln(M_{target}/m_{seed})/\lambda_{Edd}$ | Constrains lambda_Edd for given timescale |
| Linear Growth Factor | $D(a) = f(a) \int_0^a E(a')^{-3} da'$ | Cosmology-dependent structure growth |
| Hubble Parameter (ΛCDM) | $E(a)^2 = \Omega_m a^{-3} + \Omega_\Lambda$ | Different for phonon-exflation |
| Growth Rate | $f(a) = d \ln D / d \ln a$ | Normalized to 1 at early times |
| Light Seed Requirement | lambda_Edd ~ 8 for 100 M_sun -> 10^9 M_sun by z=6 | Extreme super-Eddington |
| Intermediate Seed Requirement | lambda_Edd ~ 5--6 for 10^4 M_sun -> 10^9 M_sun | Still challenging |
| Heavy Seed Requirement | lambda_Edd ~ 4--5 for 10^5 M_sun -> 10^9 M_sun | Most viable under Eddington limit |
