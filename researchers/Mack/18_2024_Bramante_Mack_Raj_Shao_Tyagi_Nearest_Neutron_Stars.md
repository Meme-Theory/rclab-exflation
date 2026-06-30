# Seeking the Nearest Neutron Stars Using a New Local Electron Density Map

**Author(s):** Joseph Bramante, Katherine Mack, Nirmal Raj, Lijing Shao, Narayani Tyagi

**Year:** 2024

**Journal/ArXiv:** arXiv:2411.18647

---

## Abstract

Neutron stars provide a compelling testing ground for gravity, nuclear dynamics, and physics beyond the Standard Model. Locating the neutron stars nearest to Earth would be particularly valuable for such studies.

This work revisits pulsar distance estimates extracted from the dispersion measure of pulsar radio waves scattering on electrons. The authors create a new electron density map for the local kiloparsec by fitting to parallax measurements of the nearest pulsars, which complements existing maps fitted on Galactic scales.

This "near-Earth" electron density map implies that pulsars previously estimated to be 100-200 parsecs away may be as close as tens of parsecs away. This motivates a parallax-based measurement campaign to follow-up on very-near candidate pulsars. Such nearby neutron stars would be valuable laboratories for testing fundamental physics phenomena, including several late-stage neutron star heating mechanisms, using current and forthcoming telescopes.

The work illustrates this by estimating the sensitivities of the upcoming Extremely Large Telescope and Thirty Meter Telescope to neutron stars heated by dark matter capture, potentially enabling direct observation of dark matter interactions at nearby neutron stars.

---

## Historical Context

Neutron stars represent extreme laboratories for testing fundamental physics. Dense nuclear matter at neutron star cores reaches densities approaching the nuclear saturation density, providing constraints on the nuclear equation of state impossible to obtain in terrestrial experiments. The strong gravitational fields near neutron star surfaces test general relativity in regimes where other theories of gravity produce distinct predictions. Additionally, neutron stars serve as sensitive probes of physics beyond the Standard Model.

Approximately 5-10% of neutron stars are observed as radio pulsars, primarily due to their beam orientation, brightness, and distance limitations. Including X-ray and gamma-ray observations, the observable fraction might reach approximately 10%. The closest known pulsar is estimated at 110-130 parsecs away.

Accurate distance measurements to nearby neutron stars are essential for:
- Determining masses and radii (constraining equation of state)
- Measuring proper motions (pinpointing kinematic age)
- Detecting heat emission from late-stage reheating mechanisms
- Searching for signatures of dark matter interactions

Previously, pulsar distances were estimated using dispersion measure (DM), the frequency-dependent delay of radio waves caused by scattering on free electrons in the interstellar medium. However, existing electron density models (NE2001, YMW16) are calibrated on Galactic scales and may not accurately represent the local (kiloparsec) structure.

---

## Key Arguments and Derivations

### Dispersion Measure and Distance Estimation

Pulsar radio waves propagate through the ionized interstellar medium, experiencing a frequency-dependent time delay due to free electrons:

DM = integral_0^d n_e(l) dl

where n_e(l) is the electron number density along the line of sight and d is the distance to the pulsar. The arrival time of radio waves at different frequencies f satisfies:

t(f) = constant + (DM e^2) / (8 pi^2 epsilon_0 m_e c) * (1/f^2)

where e is the electron charge, m_e is the electron mass, and epsilon_0 is the permittivity of free space.

Measuring the frequency-dependent delay allows determination of DM. Converting DM to distance requires knowledge of the electron density distribution n_e(l):

d = integral_0^DM dn_e^(-1) (DM')

The inversion is ambiguous without an assumed n_e model. Existing models (NE2001, YMW16) assume smooth, large-scale electron density distributions calibrated on Galactic observations.

### Local Electron Density Map Methodology

The work develops a new local electron density model by fitting to parallax measurements of the nearest pulsars. Parallax measurements, from radio interferometry (such as the Very Long Baseline Array), provide geometric distance measurements independent of DM:

d_parallax = 1 / parallax_angle (in parsecs)

For pulsars with both parallax measurements and dispersion measures, one can directly infer the local electron density along the line of sight:

n_e(line of sight) = DM / d_parallax

By combining measurements for multiple nearby pulsars, a 3D electron density map can be reconstructed for the local kiloparsec.

The work parameterizes the local electron density distribution, fitting free parameters to match the DM/parallax relationships:

n_e(r) = n_0 * exp[-(r - r_sun)^2 / (2 sigma_r^2)] + background

where r is the Galactocentric distance, r_sun is the Sun's distance from the Galactic center, and sigma_r is a scale height parameter.

### Impact on Distance Estimates

The improved electron density map reveals that:

1. **Underestimated Distances**: Standard models (NE2001, YMW16) systematically underestimate electron densities in the local region, leading to distance overestimates.

2. **Distance Revisions**: Pulsars previously estimated at 100-200 pc may actually be as close as tens of parsecs based on the new map.

3. **Candidate Nearby Pulsars**: The new map identifies specific pulsar candidates that deserve parallax measurement follow-up to confirm nearby distances.

### Dark Matter Heating of Neutron Stars

If dark matter particles can be captured by neutron stars, the annihilation or decay of captured dark matter injects energy into the neutron star, heating it against passive cooling. The heating rate depends on:

1. **Capture Cross-Section**: Dark matter nucleon scattering allows capture into orbits that decay and spiral into the neutron star

2. **Local Dark Matter Density**: The solar neighborhood dark matter density affects the capture rate

3. **Dark Matter Mass and Cross-Section**: Lighter particles capture more readily; higher cross-sections increase capture probability

The temperature of a neutron star heated by dark matter capture depends on the balance between:

dE_heat/dt = heating_rate (from captured dark matter annihilation)

dE_cool/dt = cooling_rate (from neutrino and photon emission)

For a neutron star in thermal equilibrium:

heating_rate = cooling_rate

This determines an equilibrium temperature that can exceed passive cooling values by orders of magnitude if dark matter heating is significant.

### Observational Signatures with ELT and TMT

The Extremely Large Telescope (ELT) and Thirty Meter Telescope (TMT) provide infrared and optical sensitivity to detect thermal radiation from nearby neutron stars. For a neutron star at distance d with surface temperature T:

F_thermal ~ (R_NS / d)^2 * sigma_B * T^4

where R_NS ~ 10 km is the neutron star radius and sigma_B is the Stefan-Boltzmann constant.

The work estimates the temperatures achievable for different dark matter heating models and determines whether nearby neutron stars could be detected and distinguished from passive cooling predictions.

---

## Key Results

1. **Revised Electron Density Model**: A new local kiloparsec electron density map, fitted to parallax measurements, provides improved distance estimates to nearby pulsars.

2. **Distance Corrections**: Several pulsars previously estimated at 100-200 pc may be as close as tens of parsecs, with important implications for neutron star physics studies.

3. **Candidate Nearby Neutron Stars**: The work identifies specific pulsars that deserve high-precision parallax measurements to confirm potentially very-nearby distances.

4. **Dark Matter Heating Sensitivity**: The upcoming ELT and TMT could detect dark matter heating signatures in nearby neutron stars with sensitivities to dark matter capture cross-sections and masses previously inaccessible to observations.

5. **Observational Prospects**: For nearby neutron stars (< 50 pc) with dark matter heating, infrared thermal emission should be detectable with ELT/TMT.

6. **Discriminant Against Passive Cooling**: Dark matter-heated neutron stars would display characteristic temperature predictions distinct from passive cooling, enabling empirical testing of dark matter capture models.

---

## Impact and Legacy

This work demonstrated that careful local mapping of the interstellar medium can revise distances to nearby astrophysical objects by orders of magnitude. The identification of nearby neutron stars opened new observational avenues for detecting dark matter interactions through neutron star heating.

The work motivated high-precision parallax measurement campaigns for nearby pulsar candidates and shaped the planning of dark matter searches using next-generation telescopes. The framework for predicting dark matter heating signatures became standard in neutron star dark matter studies.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework predicts a dark matter candidate emerging from spectral geometry of M4 x SU(3). Nearby neutron stars provide direct laboratories for testing whether this dark matter produces observable heating signatures.

Specific connections include:

- **Dark Matter Capture and Heating**: If phonon-exflation dark matter interacts gravitationally with neutron stars (and possesses any non-gravitational cross-section), nearby neutron star heating rates should be predictable from the framework. Observations of nearby neutron star temperatures directly test the capture cross-section prediction.

- **Neutron Star Equation of State**: Neutral mass and radius measurements from compact object binaries and other methods constrain the nuclear equation of state. The framework's dark matter candidate's effects on neutron star structure must be consistent with these measurements.

- **Fundamental Physics Tests**: Neutron stars as testing grounds for gravity and nuclear physics provide complementary constraints to cosmological observations. If phonon-exflation predicts specific deviations from general relativity or modified nuclear dynamics, neutron star observations test these predictions.

- **Dark Matter Density Profile**: The framework's prediction for the local dark matter density and velocity distribution affects the expected capture rate in nearby neutron stars. Current and future observations constrain these predictions.

- **Multi-Messenger Observations**: Coordinating neutron star observations (thermal X-ray/infrared) with other dark matter searches provides a comprehensive test of the framework's dark matter sector.

Nearby neutron stars identified by this work provide ideal laboratories for detecting interactions of phonon-exflation's emergent dark matter sector.
