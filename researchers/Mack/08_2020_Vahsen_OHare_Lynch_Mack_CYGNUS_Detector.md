# CYGNUS: Nuclear Recoil Observatory for Dark Matter and Neutrinos

**Author(s):** S.E. Vahsen, O. O'Hare, L. Lynch, K. Mack, R. Seidel, J. Tiffenberg, M. Tlusty, C. Tote, R. Vilar, Y. Zhao, and collaborators
**Year:** 2020
**Journal/ArXiv:** arXiv:2008.12587, Instrumentation and Detectors

---

## Abstract

The direct detection of dark matter particles through their nuclear recoils in sensitive detectors remains one of the primary experimental strategies for identifying dark matter. However, current and near-future experiments face the "neutrino floor"--the irreducible background from coherent neutrino-nucleus scattering that ultimately limits sensitivity for non-directional detectors. The CYGNUS project proposes a novel solution: a modular, multi-site observatory of large-scale directional dark matter detectors based on time projection chamber (TPC) technology, operating with helium and SF_6 gases at atmospheric pressure. CYGNUS would identify dark matter through directional recoil signatures, distinguishing dark matter signals from the isotropic solar neutrino background. The detector aims to achieve sensitivity to WIMP-nucleus scattering for 10 GeV dark matter particles while simultaneously observing solar, supernova, reactor, and geological neutrinos. This white paper describes the scientific case, detector design, experimental challenges, and expected physics reach.

---

## Historical Context

Dark matter direct detection has pursued one primary strategy for decades: place sensitive detectors in shielded underground locations and look for WIMP-nucleus collisions that produce nuclear recoils observable as ionization, scintillation, or phonon signals. This approach has yielded increasingly stringent constraints on WIMP-nucleon cross sections, ruling out large regions of parameter space.

However, this strategy faces a fundamental limitation: the "neutrino floor." Solar neutrinos--which are constantly streaming through Earth--scatter coherently off nuclei in the detector medium at rates that exceed the expected dark matter signal for the most sensitive cross sections. Below a certain WIMP cross section (the "floor"), neutrino-induced recoils dominate and dark matter signals disappear in the background.

A solution emerges from recognizing that dark matter and neutrino signals have different directional properties. Dark matter particles, gravitationally bound to the galactic halo, produce recoils preferentially in the direction of galactic motion (~solar apex at 76 degrees galactic latitude). Solar neutrinos are isotropic (same direction from all sources as seen from Earth). Directional detectors sensitive to recoil directions can exploit this asymmetry to distinguish dark matter from neutrino backgrounds.

CYGNUS envisions a network of directional detectors at multiple sites globally, achieving the sensitivity needed to detect WIMP dark matter despite the neutrino floor and simultaneously observe neutrinos themselves--opening a new window on solar neutrino physics, supernovae, reactor antineutrinos, and geological neutrinos.

---

## Key Arguments and Derivations

### The Neutrino Floor and Directional Detection

The WIMP-nucleus scattering cross section is parameterized as:

$$\sigma_n = \sigma_0 A^2 [Z f_p + (A-Z) f_n]^2 / (Z f_p)^2$$

where $\sigma_0$ is the WIMP-nucleon cross section, $A$ is the mass number, $Z$ is the atomic number, and $f_p$, $f_n$ are the isoscalar coupling strengths to protons and neutrons. The recoil rate for a WIMP halo moving relative to Earth is:

$$\frac{dR}{dE_r} = \frac{\rho_\chi m_n}{2\pi m_\chi m_N v_\chi^2} \sigma_n(E_r) g(v_{min})$$

where $E_r$ is the recoil energy, $\rho_\chi$ is the local dark matter density, $v_\chi$ is the WIMP velocity, and $g(v_{min})$ is a velocity distribution integral accounting for the WIMP halo model.

Coherent neutrino-nucleus scattering (CNS) produces a similar recoil spectrum but with an isotropic directional distribution. The neutrino-nucleus cross section is:

$$\sigma_\nu N = \frac{G_F^2}{\pi} Q_w^2$$

where $G_F$ is Fermi's constant and $Q_w = Z + N - 4\sin^2\theta_w Z$ is the weak charge. Solar neutrino CNS rates scale with atomic mass and vastly exceed WIMP rates at cross sections below ~10^{-47} cm^2.

The directional recoil distribution for dark matter is anisotropic, preferentially pointing toward the galactic center or solar apex (depending on season and time of day). For a WIMP halo with velocity distribution $f(v)$ moving with velocity $v_{halo}$, the differential rate per unit solid angle is:

$$\frac{d^2R}{dE_r d\Omega} \propto v_\phi(\theta,\phi) f(v_\phi(\theta,\phi))$$

where $\theta,\phi$ are the recoil direction angles and $v_\phi$ is the relative velocity in that direction. For an isotropic background (solar neutrinos), $d^2R/d\Omega$ is constant.

By requiring recoils to point toward the galactic center, directional experiments can reject isotropic neutrino backgrounds with high efficiency while retaining dark matter signals.

### Time Projection Chamber Technology

A time projection chamber (TPC) uses an ionizing particle's track in a gas to measure the direction and energy of recoil. When a nucleus recoils through a gas volume (helium or SF_6), it ionizes gas atoms along its path:

$$N_{ion} = E_r / W$$

where $W$ is the average energy per ion pair (~20 eV for noble gases). The ionization electrons drift toward an anode under an electric field, and their collection provides:

1. **Energy measurement**: Total charge collected gives recoil energy with resolution $\Delta E_r / E_r \sim$ 10-20%
2. **Direction and track length**: 2D position of ionization clusters reveals track direction. For low-energy recoils (10-100 keVr), track lengths are 1-10 mm in atmospheric-pressure helium, requiring good spatial resolution.

The gas mixture in CYGNUS would employ:
- **Helium**: Low mass (better directional resolution for light recoils, lower ionization density)
- **SF_6**: Quenching agent (reduces diffusion, improves track imaging; also an excellent insulator for high-voltage operation)

At atmospheric pressure and room temperature, ionization charge is sufficient for detection, and electron drift distances reach 10-100 cm for 1000 m^3 detectors.

### Multi-site Observatory Design

Rather than a single mega-detector, CYGNUS envisions a network of regional 100-300 m^3 TPCs at sites globally:

**Scientific Motivation**:

1. **Seasonal modulation**: Dark matter wind direction and speed vary as Earth orbits the Sun and seasons change. Different sites (Northern/Southern hemisphere) observe complementary modulation patterns, breaking degeneracies in halo models.

2. **Directional sidereal modulation**: As Earth rotates, the galactic center's position relative to detector coordinates changes. This provides daily modulation in dark matter signal direction, distinguishing it from constant backgrounds.

3. **Redundancy and systematics**: Multiple independent sites reduce risks of individual systematic errors and allow cross-validation of results.

4. **Neutrino observatories**: Different sites' neutrino capabilities (solar, atmospheric, supernova sensitivity) create a geographically distributed neutrino observatory.

### Sensitivity Goals

For 10 GeV WIMPs (a benchmark mass), the expected spin-independent scattering rate on helium is:

$$R_{10 GeV} \approx 0.3 \text{ events/(kg-day)} \text{ at } \sigma = 10^{-45} \text{ cm}^2$$

with directional peak-to-isotropic contrast improving dark matter/neutrino discrimination. A 1000 m^3 detector with 0.1 efficiency for energy thresholds 6-20 keVr would collect:

$$N = 0.1 \times 10^3 \text{ kg} \times 0.3 \text{ events/(kg-day)} \times 365 \text{ days/year} \approx 10^4 \text{ events/year}$$

With neutrino background rates of order 1-10 events/year (isotropic), dark matter signal discovery requires only 10-20 directional events pointing toward the galactic center, easily achievable.

---

## Key Results

1. **Neutrino floor avoidance**: CYGNUS's directional capability fundamentally overcomes the neutrino floor. While non-directional detectors plateau in sensitivity around 10^{-47} cm^2 (for spin-independent WIMP-nucleon scattering), directional detectors can push sensitivity to 10^{-50} cm^2 and beyond, several orders of magnitude lower.

2. **10 GeV WIMP reach**: For light WIMPs (10-100 GeV mass), CYGNUS achieves sensitivity to spin-independent cross sections down to 10^{-45} - 10^{-47} cm^2, substantially below current best limits. This probes the "low-mass WIMP" parameter space increasingly favored by some direct detection hints.

3. **Annual modulation characterization**: Seasonal variations in dark matter wind direction and speed produce a modulating annual signal. CYGNUS can map this modulation to high precision, testing WIMP halo models and distinguishing dark matter from other backgrounds.

4. **Neutrino observation**: Simultaneous detection of solar neutrinos enables precision solar neutrino spectroscopy. CYGNUS's expected 10-40 solar neutrino events per year at various energy thresholds provides unique sensitivity to:
   - Solar mass hierarchy (matter vs. vacuum mixing)
   - Solar mass eigenstate fluxes
   - Neutrino flavor oscillation parameters

5. **Supernova sensitivity**: A nearby supernova's neutrino burst produces ~1 event per 10 second in CYGNUS, allowing real-time supernova neutrino spectroscopy and possibly directional information (supernova location relative to detector).

6. **Reactor and geological neutrino detection**: Reactor antineutrinos and geoneutrinos from radioactive decay in Earth's interior produce discrete, identifiable signals. CYGNUS can detect geoneutrinos, providing constraints on Earth's internal heat production.

7. **Requirements for signal identification**: The paper quantifies the minimum number of directional recoils required to identify a dark matter signal with specified confidence:
   - For 10-20 helium recoils above 6 keVr threshold: 5-sigma dark matter discovery
   - For 3-4 recoils above 20 keVr: still achievable, depending on isotope and background assumptions

---

## Impact and Legacy

CYGNUS represents a paradigm shift in dark matter detection: from single-site, non-directional experiments to a global directional observatory. The white paper has motivated R&D toward large-scale directional detectors and has expanded the discussion of how to overcome fundamental limitations (neutrino floor) through directional information.

The project exemplifies multi-messenger astronomy applied to dark matter: combining directional, energy, and temporal information from multiple sites to constrain particle physics and cosmic structure.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation framework, dark matter is not a free particle but a collective excitation of the geometric substrate M4 x SU(3). This fundamentally changes CYGNUS's interpretation and physics reach:

1. **No WIMP scattering**: Traditional WIMP-nucleus scattering is replaced by coupling between phononic dark matter modes and nuclear excitations. The interaction cross section is not a fundamental particle property but depends on the coupling between the phonon field and nuclear motion through the local geometry.

2. **Direction-dependent coupling**: Since dark matter emerges from the geometry, its local density and couplings vary with the local state of compactification. CYGNUS's directional information would probe not the galactic dark matter halo's motion but the geometry of the compactified space in different locations and directions.

3. **Coherence and collective behavior**: Dark matter phonons exhibit coherence and collective properties. Rather than detecting individual particle scattering, CYGNUS might observe collective excitations or domain structures related to the phononic nature of dark matter.

4. **Modified recoil spectrum**: The energy and directional distribution of nuclear recoils from phononic dark matter would differ from WIMP predictions. The framework predicts a specific density profile and interaction form determined by the KK reduction, which could yield measurably different directional patterns than isotropic (neutrino) or WIMP halo (directional) backgrounds.

5. **Neutrino background unchanged**: Solar and other neutrino backgrounds remain isotropic in the framework, providing the same clean distinction as in particle physics. However, dark matter "signals" would reflect the compactification geometry rather than WIMP kinematics.

CYGNUS would provide stringent tests of phonon-exflation through precise mapping of dark matter directional signatures. If dark matter emerges from geometry, the pattern of annual modulation, daily modulation, and directional anisotropy would encode information about the compactification's spatial structure and evolution--offering a new probe of the framework independent of precision cosmology or collider experiments.
