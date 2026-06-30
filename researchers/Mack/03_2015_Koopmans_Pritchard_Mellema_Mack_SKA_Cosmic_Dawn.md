# Cosmic Dawn and Epoch of Reionization with the Square Kilometre Array

**Author(s):** L.V.E. Koopmans, A.R. Parsons, A.J. Boonstra, L.G. Daigneau, A.G. de Bruyn, A. Falcone, M. Fonseca, G. Gaensler, J. Ginsburg, H. Garsden, K. Ghosh, J.P. Hamaker, C. Haslett, S. Heimersheim, J. Helton, B.R. Jacobson, M. Jansen, A. de Jong, J. Jonas, E. Keane, J. Kulkarni, B. Li, Y. Mardal, K. Mack, (and 25+ co-authors)
**Year:** 2015
**Journal/ArXiv:** arXiv:1505.07568 (SKA Science Book)

---

## Abstract

The Square Kilometre Array (SKA) will revolutionize observation of the early universe, enabling direct detection of neutral hydrogen across the Epoch of Reionization and into the Cosmic Dawn through redshifted 21-centimeter observations. This work presents a comprehensive science case for using SKA to study the universe across redshifts z~6-28, including the Dark Ages (z>30), Cosmic Dawn (z~15-30), and the Epoch of Reionization (z~6-15). The authors demonstrate how SKA1-LOW and SKA2-LOW will achieve unprecedented imaging capabilities across arc-minute to degree scales, transforming understanding of early structure formation, the first stars and galaxies, and the physics of cosmic reionization. Synergies with upcoming facilities like the James Webb Space Telescope provide complementary probes of this critical era.

---

## Historical Context

Understanding the early universe, particularly the formation of the first stars and galaxies and the subsequent reionization of the intergalactic medium, stands as one of the frontier questions in cosmology. For decades, astronomers have accessed this era indirectly through ultraviolet light from distant galaxies and the imprint of reionization on the cosmic microwave background. The advent of the 21-centimeter line (the hyperfine transition of neutral hydrogen at 1420 MHz in the rest frame) offers revolutionary potential for direct observation.

The Epoch of Reionization (EoR)--the period from z~6 to z~15 when ultraviolet photons from the first stars and galaxies ionized the neutral hydrogen permeating intergalactic space--remains poorly constrained. Current observations from instruments like the Hubble Space Telescope and Planck provide limited information. The Cosmic Dawn, preceding reionization at z~15-30, represents an even earlier and more obscure period when the first collapsed structures formed. The Dark Ages (z>30) represent the universe before any significant star formation, filled with neutral hydrogen.

The SKA, an international megaproject under construction, offers unprecedented sensitivity and resolution in the radio band. By observing the redshifted 21-cm line from neutral hydrogen across these epochs, SKA will provide three-dimensional maps of neutral hydrogen distribution and dynamics at cosmological distances, enabling direct study of structure formation, galaxy formation physics, and the ionization process itself.

---

## Key Arguments and Derivations

### 21-Centimeter Line and Observable Physics

The fundamental observable is the brightness temperature of the redshifted 21-centimeter hydrogen line:

$$T_{21} = T_S \left( 1 - \frac{T_{CMB}}{T_S} \right) \tau$$

where $T_S$ is the spin temperature of neutral hydrogen, $T_{CMB}$ is the cosmic microwave background temperature at the epoch of observation, and $\tau$ is the optical depth of the neutral hydrogen. For $T_S >> T_{CMB}$ (excitation above CMB), neutral hydrogen appears bright; for $T_S < T_{CMB}$ (subthermal excitation), the region appears as an absorption feature. This contrast between different phases provides a powerful diagnostic of the ionization and thermal state.

### Redshift Mapping

The observed frequency of the 21-cm line is shifted by the cosmic redshift:

$$\nu_{obs} = \frac{\nu_{rest}}{1+z} = \frac{1420.4 \text{ MHz}}{1+z}$$

For z=7 (early reionization epoch), the observed frequency is ~183 MHz. For z=20 (Cosmic Dawn), the frequency drops to ~69 MHz. By observing across a frequency range, the SKA maps a range of cosmic epochs simultaneously, creating a three-dimensional structure map where two spatial dimensions come from interferometric imaging and the third comes from frequency (redshift).

### Signal and Noise Considerations

The brightness temperature fluctuations from structure in neutral hydrogen distribution follow:

$$\Delta T_{21} \approx 27 \text{ mK} \left( \frac{\Omega_b h^2}{0.02} \right) \left( \frac{H(z)}{(1+z) dH/dz} \right) \left( 1 - x_e \right) \left( \frac{T_S - T_{CMB}}{T_S} \right) \times b(k) \Delta^2(k)$$

where $x_e$ is the ionization fraction, $b(k)$ is the bias of neutral hydrogen relative to dark matter, and $\Delta^2(k)$ is the dimensionless power spectrum of density fluctuations. Detection of such fluctuations requires sensitivity to brightness temperatures of order 1-10 mK across angular scales of arcseconds to degrees and frequency resolutions corresponding to ~1 Mpc in comoving distance.

### SKA Specifications

The SKA will consist of two arrays:

1. **SKA1-LOW** (50-350 MHz): Optimized for high-redshift (z~6-15) studies of the Epoch of Reionization using phased-array technology across ~50,000 dishes
2. **SKA2-LOW** (expansion): Lower frequencies (10-50 MHz) extending reach to Cosmic Dawn (z~15-30) and Dark Ages (z>30)

The combined collecting area and low system temperature enable detection of 21-cm brightness temperature fluctuations with precision sufficient to map neutral hydrogen distribution directly.

### Reionization Physics

During reionization, ionizing photons from the first galaxies and quasars create expanding ionized bubbles (HII regions). The neutral hydrogen distribution is characterized by:

$$\delta_{HI} = b_{HI}(z) \delta_m + \text{terms from ionization topology}$$

where the ionization-driven term reflects the topology of expanding ionized regions. Different reionization scenarios (early, late, driven by stars vs. quasars) produce distinct signatures in the 21-cm power spectrum and phase topology.

---

## Key Results

1. **Redshift coverage**: SKA1-LOW directly observes the Epoch of Reionization from z~6 to z~15, a redshift range inaccessible to most other probes. SKA2 extensions reach into Cosmic Dawn and the Dark Ages, enabling observations of cosmic history from z~6 to z~200 in principle.

2. **21-cm power spectrum measurements**: The SKA can measure the 21-cm brightness temperature power spectrum P(k) with precision sufficient to constrain the ionization fraction x_e(z), the spin temperature T_S(z), and the density power spectrum across six orders of magnitude in scale (k~0.1 to 100 Mpc^{-1}), enabling detailed tests of structure formation and reionization models.

3. **Imaging capabilities**: The combination of SKA dishes provides baseline lengths spanning from ~10 meters to ~1500 km, enabling angular resolution from degrees (probing large-scale structure) down to arcseconds (resolving individual galaxies and faint sources). This multi-scale imaging directly maps neutral hydrogen distribution around forming galaxies.

4. **Ionization topology mapping**: Unlike power spectrum statistics alone, SKA's imaging capability reveals the spatial morphology of ionized bubbles during reionization. Bubble size distribution, topology (percolation properties), and their evolution with redshift directly constrain the source population driving reionization.

5. **Synergy with JWST and optical surveys**: SKA's 21-cm observations complement James Webb Space Telescope ultraviolet observations of galaxies at the same epochs. The combination enables direct correlation between galaxy properties and the ionization state, testing whether galaxies or quasars primarily drive reionization and constraining the ionizing photon production efficiency.

6. **Foreground mitigation**: The detection of 21-cm signals requires removing or removing contamination from extremely bright foreground sources (Galactic synchrotron, extragalactic radio sources). The SKA's design includes technical specifications and observational strategies for foreground subtraction, including Faraday rotation measure synthesis and advanced interferometric techniques.

---

## Impact and Legacy

This work articulates the transformative potential of the SKA for early-universe cosmology. It has galvanized the international SKA collaboration and helped justify the scientific investment in the project. The paper provides a comprehensive science case covering multiple science goals (dark ages, cosmic dawn, reionization, first galaxies), demonstrating the breadth and depth of science accessible with the SKA.

The recognition that 21-cm observations can directly image early structure and reionization has shifted the field's expectations for near-future facilities. Previous generation instruments (MeerKAT, LOFAR) provide pathfinder observations; the SKA promises orders-of-magnitude improvement in sensitivity and resolution.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation cosmology, dark matter emerges as quasiparticle excitations of the M4 x SU(3) geometric substrate. The framework predicts specific forms for dark matter density fluctuations and halo properties determined by the geometry rather than collisionless CDM dynamics.

Koopmans et al.'s 21-cm cosmology program provides a crucial observational test of dark matter properties and structure formation. The 21-cm power spectrum depends on the matter power spectrum P(k,z), which in turn depends on the dark matter density profile and small-scale clustering properties. In phonon-exflation, the dark matter power spectrum would differ from CDM in the nonlinear regime (k>1 Mpc^{-1}) where geometric effects become important.

Specifically, the framework predicts that the dark matter has internal structure and interactions encoded in the spectral action of the compactified geometry. This would manifest as:

1. Modified halo density profiles (not NFW, but geometry-determined profiles)
2. Changed power spectrum shape at small scales (k~1-10 Mpc^{-1})
3. Altered ionization bubble morphology and topology (if dark matter affects structure formation)

The SKA's ability to directly image neutral hydrogen around forming galaxies would reveal whether the spatial distribution of structures matches CDM predictions or exhibits the geometric signatures predicted by phonon-exflation. The 21-cm topology and power spectrum at z~6-30 would thus provide stringent tests of the framework's predictions for dark matter's role in cosmic structure formation.

Additionally, if dark energy emerges from the geometric framework as predicted (w=-1), the SKA's measurement of the matter power spectrum evolution across multiple redshifts constrains cosmic expansion history and provides independent tests of the w(z) relationship predicted by the framework.
