# Thick Accretion Disks and Envelopes Around Rapidly-Growing Black Holes in the Early Universe

**Author(s):** Kohei Inayoshi, Zoltan Haiman, Shantanu Basu, and collaborators

**Year:** 2024

**Journal:** The Astrophysical Journal (volume 976, article 182; arXiv:2312.15387)

---

## Abstract

This theoretical paper investigates whether rapidly-growing black holes (M_BH ~ 10^6--10^8 M_sun at z~4--8) can maintain geometrically-thick, radiatively-inefficient accretion flows (RIAFs), analogous to those invoked to explain sub-Eddington accretion in nearby nuclei (e.g., M87, Sgr A*) but operating at super-Eddington rates in the early universe. Inayoshi and colleagues develop models of black hole accretion in gas-rich, turbulent environments characteristic of high-z mergers. They show that for lambda_Edd >> 1 (super-Eddington), the accretion disk becomes geometrically thick (H/R ~ 1) and radiatively inefficient, with most energy carried away in outflows rather than radiated. In such flows, the accretion rate far exceeds the standard Eddington rate because the radiation-pressure barrier is weakened by the low radiative efficiency and the outflow geometry. Critically, the models predict that super-Eddington flows produce only weak X-ray emission relative to the bolometric luminosity (explaining LRD X-ray weakness without invoking extreme dust obscuration), and can support broad-line-region gas at higher densities than thin disks (explaining high broad-line equivalent widths). The paper provides a self-consistent physical model of Little Red Dots as rapidly-growing black holes in thick, possibly outflow-fed accretion flows, distinct from both thin-disk AGN and standard Compton-thick-obscured scenarios.

---

## Historical Context

The standard thin-disk model of AGN accretion (Shakura-Sunyaev, 1973; subsequent work) assumes a geometrically-thin (H << R), optically-thick disk with thermal radiation. At the Eddington limit (lambda_Edd = L/L_Edd = 1), radiation pressure on electrons equals gravity:

$$\frac{\sigma_T L_{Edd}}{4\pi R^2 c} = \frac{GM}{R^2}$$

For lambda_Edd > 1, the radiation pressure exceeds gravity on electrons, driving a wind and limiting the accretion rate.

However, observations of nearby low-accretion sources (M87, NGC 3115, Sgr A*) show that sub-Eddington black holes can accrete via geometrically-thick, optically-thin (radiatively-inefficient) accretion flows (RIAFs). In RIAFs, much energy is advected into the black hole without being radiated. The effective "Eddington limit" in RIAFs is not a limit on accretion rate but rather on radiative luminosity, allowing very high accretion rates with modest radiated power.

Inayoshi et al. asked: can similar thick flows operate at super-Eddington rates in the early universe? If so, they would naturally explain LRD properties without invoking fine-tuned obscuration.

The key insight is that in a super-Eddington RIAF, radiation pressure is dynamically unimportant because the flow is optically thin and carries most energy in the form of bulk motion (outflows), not radiation. The accretion rate is limited only by the gas supply from the host galaxy, not by radiation pressure.

---

## Key Arguments and Derivations

### Thick Disk Structure and Stability

A geometrically-thick accretion disk has scale height H comparable to radius R. The vertical hydrostatic balance is:

$$\frac{dP}{dz} = -\rho \frac{GM}{R^3} z$$

for small z. The pressure scale height is H_p = (c_s^2 / (GM/R^3))^{1/2} = c_s sqrt(R^3 / GM), and the disk is "thick" if H_p >> H_thin, where H_thin ~ (c_s / v_K) R is the thin-disk scale height.

For a geometrically-thick RIAF, the scale height is:

$$H \sim \alpha R$$

where alpha ~ 0.1--1 is the viscosity parameter (Shakura-Sunyaev). With alpha ~ 0.3--1, H/R ~ 0.3--1 is achieved.

### Radiative Efficiency in Thick Flows

The radiative efficiency (fraction of rest-mass energy radiated) in a thin disk is epsilon ~ 0.1. In a thick RIAF, epsilon is much lower:

$$\epsilon_{RIAF} \sim 0.01 - 0.1 \times \epsilon_{thin}$$

In the extreme case of a high-accretion-rate RIAF (advection-dominated), epsilon ~ 0.001--0.01, meaning 99% of the accretion power goes into advection and outflow, not radiation.

The accretion luminosity is then:

$$L_{acc} = \epsilon \dot{M} c^2$$

For lambda_Edd >> 1, even if dot{M} >> dot{M}_{Edd}, the radiated luminosity can remain modest if epsilon is low. Specifically:

$$L_{bol} = \epsilon \, \lambda_{Edd} \, \dot{M}_{Edd} c^2 = \epsilon \, \lambda_{Edd} \, L_{Edd}$$

For epsilon ~ 0.01 and lambda_Edd ~ 10 (super-Eddington accretion):

$$L_{bol} \sim 0.1 \, L_{Edd}$$

which is sub-Eddington in terms of radiated power despite a 10x super-Eddington accretion rate. This naturally explains X-ray weakness (due to low epsilon) without invoking extreme dust obscuration.

### Outflow Morphology and Wind Power

In a super-Eddington RIAF, the outflow carries away the bulk of the accretion energy:

$$P_{wind} = (1 - \epsilon) \, \dot{M} c^2 = (0.99) \times (10 \, \dot{M}_{Edd}) c^2 \sim 10 \, L_{Edd}$$

The outflow velocity is set by the gravitational potential and the enthalpy of the gas:

$$\frac{1}{2} v_{out}^2 \sim h_{out} \sim \frac{c_p T}{1}$$

where h_out is the specific enthalpy and c_p is the specific heat. For radiation-dominated outflows:

$$h \sim c^2 (1 - \epsilon)$$

giving v_out ~ c (mildly relativistic). More typically, for gas-dominated outflows:

$$v_{out} \sim \sqrt{\frac{GM}{R}} \sim v_K$$

(comparable to the Keplerian velocity at that radius), yielding v_out ~ 1000--10,000 km/s.

The momentum flux in the outflow is:

$$\dot{P}_{wind} = \dot{M}_{out} \, v_{out}$$

This can drive significant feedback on host galaxies, suppressing star formation—a key mechanism for AGN feedback in the early universe.

### Broad-Line Region in Thick Flows

In a thin-disk AGN, the broad-line region is photoionized by the AGN continuum and typically has electron density n_e ~ 10^9--10^{10} cm^{-3}. The broad-line equivalent width is set by the ratio of line to continuum flux.

In a super-Eddington RIAF, the flow is denser and more opaque, with n_e ~ 10^{10}--10^{12} cm^{-3} in the inner regions. Additionally, the optically-thick portions of the flow can scatter and absorb the central AGN continuum, reducing the continuum observed in the line-of-sight while the lines (formed in ionized outflowing gas along preferential directions) remain visible.

The result is a naturally high equivalent width:

$$\text{EW} \sim \frac{F_{line}}{f_{continuum,obs}}$$

with the denominator reduced by scattering/absorption and the numerator unaffected (or enhanced by density), yielding EW ~ 100--1000 Angstrom, consistent with observations.

### X-Ray Emission

X-ray photons in a RIAF are produced primarily by Comptonization of the accretion-disk radiation by hot electrons in the ion-electron-couple. However, in a geometrically-thick, optically-thin RIAF, the electron temperature (keV) and optical depth (tau ~ 0.1--1) are set by the balance between heating (accretion viscosity) and cooling (Coulomb interactions, radiation).

For a super-Eddington RIAF with epsilon ~ 0.01--0.1, the hard X-ray luminosity is:

$$L_X \sim \epsilon \, L_{bol}$$

If L_bol ~ 10^{45} erg/s and epsilon ~ 0.01, then L_X ~ 10^{43} erg/s, consistent with the X-ray stacking results from Yue et al. (Paper 06), without requiring extreme dust obscuration.

---

## Key Results

1. **Thick RIAF Viability**: Super-Eddington accretion via geometrically-thick, radiatively-inefficient accretion flows is physically viable in the early universe.

2. **Low Radiative Efficiency**: Thick RIAFs at lambda_Edd >> 1 can have epsilon << 0.1, allowing high accretion rates with modest radiated luminosity.

3. **X-ray Weakness Natural**: Low epsilon (0.01--0.1) explains weak X-ray emission without invoking extreme dust. L_X is naturally a small fraction of L_bol.

4. **High Equivalent Width Natural**: Dense, thick flows with scattering and absorption of central continuum naturally produce high broad-line equivalent widths (EW ~ 100--1000 Angstrom).

5. **Outflow-Driven Feedback**: Super-Eddington RIAFs drive powerful outflows with P_wind ~ 10 L_Edd, significant for early-universe AGN feedback.

6. **Black Hole Growth**: Thick RIAFs permit rapid black hole growth (dot{M} >> dot{M}_{Edd}) while remaining radiatively sub-Eddington in output. Enables assembly of 10^6--10^8 M_sun black holes in <1 Gyr.

---

## Impact and Legacy

1. **Accretion Physics Alternative**: Provided a physically-grounded alternative to standard thin-disk AGN models that applies at high accretion rates.

2. **X-ray Weakness Explanation**: Offered a natural explanation for LRD X-ray weakness without invoking exotic obscuration scenarios.

3. **RIAF Applicability at High-z**: Extended RIAF models (previously applied to low-accretion systems) to high-accretion regimes, broadening the theoretical framework.

4. **Early-Universe AGN Feedback**: Showed that super-Eddington RIAFs drive powerful winds capable of significant AGN feedback, affecting galaxy evolution.

5. **Unified AGN Physics**: Suggested a unified description of AGN across accretion rates from sub-Eddington (local nuclei) to super-Eddington (LRDs).

---

## Connection to Phonon-Exflation Framework

Accretion disk physics is fundamental to AGN but does not directly depend on the large-scale cosmology or NCG structure. However, the prevalence of super-Eddington accretion at z~4--8 and the efficiency of AGN feedback do couple to cosmology.

**Connections**:

1. **Black Hole Growth Timescale**: The accretion rate and radiative efficiency determine how quickly black holes reach observed masses. Phonon-exflation's prediction of H(z) affects gas infall rates into black hole potential wells and thus accretion rates.

2. **AGN Feedback Efficiency**: The kinetic power in outflows (P_wind ~ 10 L_Edd for thick RIAFs) determines how effectively AGN suppresses star formation. This impacts the predicted star formation history and galaxy evolution, a key test of cosmological models.

3. **Merger Rates and Black Hole Binary Evolution**: Rapid black hole growth via high-accretion flows is most efficient in mergers. The merger rate depends on structure growth (d(delta)/dz), which differs between ΛCDM and phonon-exflation.

4. **Reheating and Ionization**: AGN-driven outflows affect the ionization and temperature state of early-universe gas, feeding back to the ionization fraction and thus structure formation. Phonon-exflation's prediction of reheating would interact with AGN feedback.

**Intensity**: Medium. The thick-RIAF model provides detailed accretion physics applicable to LRDs, with implications for AGN feedback and star formation in the early universe. The connection to phonon-exflation is primarily through AGN feedback effects on galaxy evolution, rather than fundamental physics.

---

## Key Equations Summary

| Quantity | Equation | Value |
|----------|----------|-------|
| Disk Scale Height (thick) | H ~ alpha * R | alpha ~ 0.3--1 (H/R ~ 0.3--1) |
| Radiative Efficiency (RIAF) | epsilon_RIAF | ~ 0.001--0.1 (vs. thin disk ~ 0.1) |
| Radiated Luminosity (super-Edd RIAF) | L_bol = epsilon * lambda_Edd * L_Edd | ~ 0.1--1.0 L_Edd for epsilon ~ 0.01--0.1, lambda_Edd ~ 10 |
| Outflow Power | P_wind = (1 - epsilon) * dot{M} c^2 | ~ 10 L_Edd (super-Edd regime) |
| Outflow Velocity | v_out ~ sqrt(GM/R) | ~ 1000--10,000 km/s |
| X-ray Luminosity (thick RIAF) | L_X ~ epsilon * L_bol | ~ 10^{43} erg/s for L_bol ~ 10^{45} and epsilon ~ 0.01 |
| Broad-Line Equivalent Width | EW from continuum obscuration | 100--1000 Angstrom (enhanced by thick flow) |
