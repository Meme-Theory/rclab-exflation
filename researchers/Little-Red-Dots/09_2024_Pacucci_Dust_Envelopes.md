# Little Red Dots: Rapidly Growing Black Holes Reddened by Extended Dusty Flows

**Author(s):** Fabio Pacucci, Avi Loeb, Priyamvada Natarajan, and collaborators

**Year:** 2024

**Journal:** The Astrophysical Journal (arXiv:2407.17341)

---

## Abstract

This theoretical paper proposes that Little Red Dots arise from rapidly accreting black holes surrounded by extended dusty gaseous envelopes, rather than dusty star-forming hosts. Pacucci and collaborators develop models in which accretion-powered radiation from a central supermassive black hole (M_BH ~ 10^6--10^8 M_sun) photoionizes and heats surrounding gas, driving outflows that inflate a dusty envelope. The dust distribution is far more extended than traditional obscuring tori, reaching scales of ~kpc. Radiation from the black hole scattered by this extended dust produces the observed V-shaped SED characteristic of LRDs: blue UV (direct light from the black hole), red optical (scattered light and dust reradiation), and compact morphology (the black hole itself is point-like). The model naturally explains several observational puzzles: (1) X-ray weakness (dust absorption), (2) unusually compact morphologies (true size is black hole, not host galaxy), (3) high equivalent-width broad emission lines (dense gas in outflow funnel), and (4) the apparent disconnect between inferred black hole masses and host galaxy masses (the host is not the true stellar host, but rather the extended outflow remnant). The paper provides a unified physical picture of LRD structure and evolution, distinct from AGN in large dust tori or compact starbursts.

---

## Historical Context

Traditional AGN unification models (Antonucci 1993, others) posit a dusty torus around the black hole, obscuring it when viewed edge-on. The torus has scale ~pc--sub-kpc, is maintained by radiation pressure, and has a covering fraction that determines whether the AGN appears as Type I (unobscured) or Type II (obscured).

However, LRDs present challenges to this canonical picture:
1. Extremely compact morphologies (r_e ~ 100--200 pc) even accounting for the torus are difficult to reconcile with massive host galaxies.
2. X-ray weakness suggests heavy obscuration, yet some models predict X-ray leakage from tori.
3. The broad-line equivalent widths are exceptionally high (EW ~ 500--1000 Angstrom), suggesting the BLR gas is in an unusual geometry or density state.

Pacucci et al. proposed an alternative: the "dusty envelope" model. Rather than dust concentrated in a torus, dust is distributed over kpc scales in an outflow-driven wind. This envelope surrounds a compact black hole and accreting disk but extends much farther.

The model is motivated by observations of nearby AGN-driven winds (Mrk 231, Mrk 1014, others) and by hydrodynamic simulations showing that AGN radiation pressure can accelerate gas to ~10% escape velocity, creating large-scale outflows.

---

## Key Arguments and Derivations

### Black Hole Radiation and Dust Opacity

A black hole with bolometric luminosity L_bol radiates across a broad spectrum, with a fraction in the UV (shortward of 1216 Angstrom):

$$L_{UV} = f_{UV} \cdot L_{bol}$$

where f_UV ~ 0.1--0.3 for typical AGN. This UV light photoionizes hydrogen in surrounding gas:

$$\gamma = \frac{N_{ion}}{N_H} \approx \frac{L_{UV}}{4\pi d^2 h \nu_{ion} c}$$

where N_ion is the ionizing photon rate, h nu_ion ~ 13.6 eV is the ionization energy of hydrogen, and d is the distance from the black hole.

Gas ionized by the black hole's UV radiation experiences radiation pressure:

$$F_{rad} = \frac{\sigma_T}{c} L_{bol} \rho$$

where sigma_T is the Thomson cross-section for electron scattering. For a fully ionized gas cloud of density rho and size R:

$$F_{rad,total} = \frac{\sigma_T L_{bol}}{c} \cdot M_{gas} / R^2$$

If F_rad exceeds the gravitational binding force:

$$F_{grav} = \frac{GM_{BH} M_{gas}}{R^2}$$

the gas is accelerated outward. The condition for outflow is:

$$\frac{\sigma_T L_{bol}}{c} > \frac{GM_{BH}}{R^2}$$

Rearranging:

$$L_{bol} > \frac{GM_{BH} c}{\sigma_T} \equiv L_{Edd}$$

(the Eddington luminosity). For L_bol ~ L_Edd (near-Eddington accretion), radiation pressure becomes significant, and outflows develop.

### Outflow Velocity and Dust Envelope Extent

The outflow velocity is determined by energy balance. A parcel of gas at distance r from the black hole experiences radiation acceleration a_rad ~ sigma_T L_bol / (m_e c r^2) (per electron, scaled to gas by density). Integrating the equation of motion from r_0 (initial radius, ~AU) to large r:

$$\frac{1}{2} v_{out}^2 = \int_{r_0}^{r} a_{rad} \, dr' + \text{(wind energy)}$$

For a steady wind, the outflow velocity scales as:

$$v_{out} \sim \sqrt{\frac{2 G M_{BH}}{r_0}} \sim 0.01\text{--}0.1 \, c$$

where $r_0$ is the launch radius (AU-scale for radiation-driven winds). For near-Eddington luminosities, radiation pressure significantly accelerates the outflow, reaching v ~ 1,000--30,000 km/s depending on geometry and optical depth.

The extent of the dust envelope is limited by the distance at which gas cools and dust forms. In a radiatively-accelerated wind, the temperature drops as:

$$T(r) \propto r^{-1}$$

(under specific conditions). Dust forms at T ~ 1000--1500 K, which corresponds to:

$$r_{dust} \sim 1 - 10 \, \text{kpc}$$

for L_bol ~ 10^{45}--10^{46} erg/s. Thus, the dust envelope extends to kpc scales, far larger than traditional tori.

### SED Modeling

The observed SED is the superposition of:

1. **Direct AGN Light**: UV/optical continuum from accretion disk, blue component at lambda_rest ~ 1000--5000 Angstrom.

2. **Scattered Light**: AGN photons scattered by electrons in the outflowing ionized gas. This scattered component appears in all wavelengths but is enhanced in UV/optical due to high scattering cross-section.

3. **Dust Reradiation**: Dust grains absorb UV/optical photons from the AGN and reradiate in the infrared. The reradiated flux depends on dust temperature and optical depth:

$$f_{\nu}^{IR} = \epsilon(\nu) \, B_\nu(T_{dust}) \, \tau_{dust}(\nu)$$

where epsilon is dust emissivity and tau_dust is optical depth. For moderately optically-thick dust (tau ~ 1), the reradiated flux peaks in the near-IR and mid-IR.

The combined SED has:
- **Blue UV**: Direct AGN light unobscured.
- **Red Optical**: Scatter-dominated (Rayleigh scattering, enhanced at short wavelengths, suppressed at long wavelengths) plus dust reradiation.
- **Steep Optical-to-Near-IR Rise**: Characteristic of dust-dominated continuum, producing the "V-shape".

Quantitatively, the optical-to-near-IR ratio is:

$$f_\nu(1000 \text{ nm}) / f_\nu(10000 \text{ nm}) \sim 0.01--0.1$$

producing the strong color contrast observed in LRDs.

### Dust Envelope Extinction and Equivalent Width

The X-ray weakness is naturally explained if the dusty envelope has high optical depth to X-rays. X-ray absorption by dust and gas is governed by:

$$\tau_X \sim \sigma_X \, N_H$$

where sigma_X is the X-ray cross-section and N_H is the hydrogen column density. For an envelope with N_H ~ 10^{23}--10^{24} cm^{-2} (moderate-to-high column density), the soft X-ray (0.5--2 keV) optical depth is tau_X ~ 1--10, causing significant absorption. Hard X-rays (2--8 keV) penetrate more easily but are still suppressed by factors of 2--10.

The broad emission lines have high equivalent width because they form in the dense, highly ionized wind just outside the black hole, where column densities are high and the continuum source (the black hole) is partially obscured. The line-to-continuum ratio is thus:

$$\text{EW} = \frac{F_{line}}{F_{cont}} = \frac{F_{line}}{f_{cont,observed}}$$

If f_cont is reduced by dust obscuration (factor 2--10) while F_line is largely unaffected (forming close to black hole, outflowing along preferred directions), the EW is naturally enhanced by the same factor, reaching EW ~ 500 Angstrom or higher.

---

## Key Results

1. **Dusty Envelope Model**: Proposes LRDs as black holes surrounded by kpc-scale dusty outflow-driven envelopes, distinct from traditional tori.

2. **Unified SED Explanation**: The V-shaped SED naturally emerges from superposition of direct AGN light, scattering, and dust reradiation.

3. **X-ray Weakness Resolved**: Heavy dust and gas in envelope absorb X-rays; no need for exotic accretion physics (super-Eddington, advection-dominated flows) to explain X-ray weakness.

4. **Compact Morphology Explained**: The true source is point-like (black hole + accretion disk ~ AU scale); observed morphology at r_e ~ 100--200 pc reflects the dust envelope surface, not the stellar host galaxy.

5. **High Equivalent Width Natural**: High EW results from reduced continuum (due to obscuration) combined with line emission from dense, outflowing gas.

6. **M_BH/M_* Ratio Reinterpreted**: The apparent overmassive black hole (M_BH/M_* >> 0.001) may reflect confusion about what M_* means: if the "host" is not a true bulge but rather a dust-envelope remnant, the ratio is less anomalous.

7. **Outflow-Driven AGN Feedback**: LRDs provide direct observational evidence for AGN-driven winds and feedback in the early universe.

---

## Impact and Legacy

1. **Alternative Interpretation**: Offered an unconventional but physically grounded alternative to treating LRDs as dusty starbursts with AGN or as standard obscured AGN.

2. **AGN Feedback at High-z**: Emphasized importance of AGN-driven winds and outflows in early-universe AGN populations, with potential implications for galaxy quenching.

3. **Multi-Wavelength Interpretation**: Motivated coordinated observations across UV, optical, X-ray, and infrared to test the dusty-envelope hypothesis.

4. **Outflow Geometry**: Highlighted the role of outflow geometry and dust distribution in setting AGN observational signatures.

5. **Radiative Transfer Modeling**: Spurred development of detailed radiative transfer models of dusty AGN outflows, including scattering.

---

## Connection to Phonon-Exflation Framework

The dusty-envelope model is fundamentally about AGN feedback and gas dynamics in the early universe. The phonon-exflation framework predicts early-universe parameters (H(z), rho(z), T(z), structure growth) that would affect AGN feedback efficiency and outflow properties.

**Connections**:

1. **Outflow Efficiency**: The ratio of outflow kinetic energy to AGN luminosity depends on the ambient gas density and sound speed, both sensitive to H(z) and T(z).

2. **Dust Formation and Evolution**: The dust abundance and grain properties in the early universe depend on star formation history and metallicity evolution, which are cosmology-dependent.

3. **Gas Dynamics**: The ability of AGN to launch kpc-scale winds depends on the density structure and cooling properties of early-universe gas, which couple to H(z) and reionization.

4. **Envelope Extent**: The scale to which dust envelopes extend (set by dust-formation temperature and outflow velocity) depends on AGN luminosity and ambient gas properties, themselves cosmology-dependent.

**Intensity**: Medium. The dusty-envelope model provides physical insights into LRD structure and AGN feedback, but the connection to phonon-exflation is indirect (through AGN demographics and feedback efficiency rather than fundamental NCG physics).

---

## Key Equations Summary

| Quantity | Equation | Value |
|----------|----------|-------|
| UV Luminosity Fraction | L_UV = f_UV * L_bol | f_UV ~ 0.1--0.3 |
| Radiation Pressure Force | F_rad = (sigma_T/c) * L_bol * rho | Exceeds gravity for L ~ L_Edd |
| Outflow Velocity (radiation-driven) | v_out ~ sqrt(2*G*M_BH/r_0), boosted by radiation pressure | ~ 1,000--30,000 km/s for L_bol ~ L_Edd |
| Dust Envelope Extent | r_dust (where T ~ 1000 K) | 1--10 kpc |
| X-ray Optical Depth | tau_X = sigma_X * N_H | N_H ~ 10^{23}--10^{24} cm^{-2} gives tau ~ 1--10 (soft X) |
| Dust Temperature | T_dust (from L_bol, r) | 1000--1500 K at dust-formation radius |
| Broad Line Equivalent Width | EW = F_line / f_cont,obs | 500--1000 Angstrom (enhanced by obscuration) |
