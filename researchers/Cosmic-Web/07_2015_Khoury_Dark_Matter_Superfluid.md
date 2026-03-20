# A Dark Matter Superfluid: Reconciling MOND and Lambda-CDM

**Author(s):** Lasha Berezhiani, Justin Khoury

**Year:** 2015

**Journal:** Physical Review D, Volume 92, Article 103510

---

## Abstract

Khoury and Berezhiani propose that dark matter consists of self-interacting axion-like particles that condense into a superfluid state within galaxies and galaxy clusters. The superfluid phase exhibits phononic collective excitations that mediate a MOND-like acceleration law on baryonic matter at galactic scales, while at cluster scales the dark matter remains in a mixed superfluid-normal phase or normal phase, recovering ΛCDM dynamics. This framework elegantly reconciles the phenomenological success of MOND on galactic scales with the triumph of ΛCDM on cosmological scales, unifying them within a single underlying theory based on superfluid physics.

---

## Historical Context

By 2015, a persistent tension had emerged in cosmology: MOND (Modified Newtonian Dynamics) successfully explains galactic rotation curves and internal dynamics, predicting observed accelerations from mass distribution alone, with no need for dark matter. However, MOND fails catastrophically at cluster scales and in the early universe. Conversely, ΛCDM successfully predicts large-scale structure, CMB properties, and weak lensing, but requires exotic dark energy and struggles to match some galactic observations (core-cusp problem, too-big-to-fail problem).

Khoury and Berezhiani proposed a novel solution: dark matter and MOND are not fundamental but emerge from the same underlying physics—superfluid dark matter. This work, building on earlier analog gravity insights from Volovik and others, provided a concrete physical mechanism for superfluid dark matter, making falsifiable predictions about galactic dynamics and dark matter distribution.

---

## Key Arguments and Derivations

### Superfluid Dark Matter Phase Diagram

The dark matter consists of axion-like particles with mass $m_\phi \sim$ eV and strong self-interactions characterized by a scattering length $a_s$. The effective equation of state at temperatures $T$ and density $\rho$ is:

$$P = c_s^2 \rho = \lambda \rho^3 \quad \text{(polytropic, } \gamma = 3 \text{)}$$

where $c_s$ is the sound speed and $\lambda$ is a coupling constant related to the scattering length.

At low temperature and high density (typical of galactic interiors), the dark matter condenses into a superfluid:

$$\psi(\mathbf{r}, t) = \sqrt{\rho_s}(\mathbf{r}) e^{i\phi(\mathbf{r}, t)}$$

where $\rho_s$ is the superfluid density and $\phi$ is the phase. The condensate fraction is $n_s / n \approx 0.9-0.99$ in galactic cores.

At higher temperature or lower density (typical of galaxy cluster outskirts), the dark matter is partially in a normal (non-condensed) phase:

$$\rho_{\text{DM}} = \rho_s + \rho_n$$

The phase transition occurs at a critical temperature:

$$T_c = T_0 \left(\frac{\rho}{\rho_0}\right)^{2/3}$$

For galactic parameters ($\rho \sim 0.1 \text{ GeV/cm}^3$), $T_c \sim 10$ mK. For cluster outskirts ($\rho \sim 10^{-4}$ GeV/cm$^3$), $T_c \sim 10$ μK.

### Phonon-Mediated MOND-Like Acceleration

In the superfluid state, Bogoliubov quasiparticles (phonons) are the elementary excitations. A baryonic particle (e.g., a star) moving through the superfluid scatters off phonons. The drag force from phonon interactions is:

$$F_{\text{phonon}} = \frac{mc_s \sigma_0}{d} a_{\text{acc}}$$

where $m$ is the baryonic mass, $c_s$ is the phonon sound speed, $\sigma_0$ is a coupling cross-section, $d$ is the galactic disk scale height, and $a_{\text{acc}}$ is the acceleration being considered.

In the limit where the phonon drag dominates over gravitational forces from baryons alone, the equation of motion becomes:

$$m a = F_{\text{grav}} + F_{\text{phonon}} + F_{\text{superfluid}}$$

For a galaxy with a given baryonic mass distribution $M_b(r)$, the superfluid adjusts to minimize energy and provide an effective gravitational field. The result is that the effective acceleration follows the MOND formula:

$$a_{\text{eff}} = \sqrt{a_0 g_N}$$

where $a_0$ is the MOND acceleration scale (related to the dark matter condensation properties) and $g_N$ is the Newtonian gravitational acceleration from the baryonic mass.

**Crucially**: $a_0$ is not an ad-hoc constant but emerges from the dark matter's equation of state and sound speed:

$$a_0 \sim c_s^2 / r_0$$

where $r_0$ is a characteristic length scale related to the superfluid coherence length or the dark matter scale radius.

### Scale-Dependent Behavior: From Galaxies to Clusters

The dark matter's phase structure naturally explains why MOND works in galaxies but not in clusters:

**Galactic scale** (M ~ 10^11 M_sun, r ~ 10 kpc, T ~ mK):
- High density ($\rho \sim 0.1$ GeV/cm$^3$)
- Low temperature ($T \ll T_c$)
- Superfluid: nearly pure condensate ($n_s / n \gtrsim 0.9$)
- Phonon sound speed $c_s \sim 10$ km/s (measurable from kinematics)
- Result: MOND-like acceleration from phonon drag

**Cluster scale** (M ~ 10^15 M_sun, r ~ 100 kpc, T ~ 10 μK to 1 mK):
- Lower density ($\rho \sim 10^{-4}$ GeV/cm$^3$ in outer regions)
- Higher temperature relative to $T_c$ (often $T \gtrsim T_c$)
- Mixed phase or normal phase ($n_s / n \lesssim 0.5$ or nearly zero)
- Phonon number density much lower; kinetic energy dominates
- Result: ΛCDM-like behavior; gravity governed by density distribution, not phonon interactions

The transition between regimes occurs naturally at intermediate scales (r ~ 100 kpc to few Mpc), consistent with observations showing that MOND breaks down around the cluster scale.

### Vortex Network and Stability

In rotating systems, the superfluid spontaneously forms quantized vortices with circulation:

$$\oint \mathbf{v}_s \cdot d\mathbf{l} = \frac{h}{m_\phi} = \frac{\hbar}{m_\phi}$$

For a galaxy with angular velocity $\Omega$, the vortex density is approximately:

$$n_{\text{vortex}} \approx \frac{2 m_\phi \Omega}{\hbar}$$

For galactic parameters ($\Omega \sim 10^{-15}$ s$^{-1}$, $m_\phi \sim 10^{-22}$ eV for axions), $n_{\text{vortex}} \sim 10^{-7}$ cm$^{-2}$ per unit height, which is extremely sparse. The vortices are widely separated (~10 pc or more) and do not significantly affect galactic dynamics.

However, in merging systems or highly turbulent flows, vortex dynamics could produce observable signatures (anomalous heating, asymmetric mass distribution).

### Observable Signatures

The theory makes several predictions for testing:

1. **Axion mass and coupling**: Direct detection experiments (ADMX, CAST, etc.) should find axion-like particles with mass ~eV and coupling to electromagnetism.

2. **Sound speed from galaxy kinematics**: The phonon sound speed $c_s$ should be measurable from velocity dispersions and scale with density ($c_s \propto \rho^{1/3}$ for polytropic EOS).

3. **Vortex tracers**: In merging systems, vortex tangles might produce observable signatures (heating, asymmetry).

4. **Transition signature at cluster scale**: Prediction of a specific scale where MOND-like dynamics transition to ΛCDM-like dynamics, measurable via velocity dispersions and mass profiles.

5. **Baryon acoustic oscillations**: The superfluid dark matter produces sound waves in the early universe (before the phase transition), generating the characteristic BAO scale now observed in galaxy surveys.

---

## Key Results

1. **Unified framework**: Dark matter superfluidity naturally explains why MOND is successful in galaxies and ΛCDM in clusters—both emerge from the same underlying superfluid phase structure.

2. **MOND as phonon drag**: MOND's empirical acceleration formula emerges from the effective force law when baryons interact with superfluid phonons.

3. **Scale-dependent behavior**: The superfluid-to-normal phase transition occurs at scales consistent with where MOND breaks down observationally (galaxy cluster scale).

4. **Phonon sound speed as measurable quantity**: Instead of ad-hoc constants, the theory predicts measurable physical properties of the dark matter (sound speed, coherence length) that can be extracted from observations.

5. **Natural vortex networks**: Quantized vortices form spontaneously in rotating systems, providing potential dynamical tracers.

6. **Testable predictions**: The theory makes specific predictions for dark matter direct detection, sound speed measurements, and dynamical signatures in mergers.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: VERY HIGH**

This work is a direct precedent and inspiration for phonon-exflation:

- **Particles as phononic quasiparticles**: Just as Khoury treats dark matter as a superfluid with phononic excitations, phonon-exflation treats all particles (electrons, quarks, photons) as phononic excitations of the NCG substrate.

- **Emergent acceleration laws from quasiparticle physics**: MOND emerges from phonon-mediated interactions in Khoury's work. Similarly, gravitational acceleration might emerge from phonon-geometric interactions in phonon-exflation.

- **Scale-dependent physics**: The phase transition between superfluid and normal in Khoury's theory is a scale-dependent phenomenon. Phonon-exflation predicts scale-dependent physics from the NCG structure (different regimes at different energy scales).

- **Sound speed as fundamental parameter**: In Khoury's theory, the superfluid sound speed characterizes the low-energy dynamics. In phonon-exflation, the phonon dispersion relation (and sound speeds) emerge from the Dirac spectrum of D_K, controlling cosmological and particle physics.

- **Topological defects as fundamental objects**: Vortices in Khoury's superfluid dark matter are topological defects. In phonon-exflation, cosmic strings, monopoles, and other defects emerge as topological excitations of the NCG substrate.

- **Bridge between galaxy and cosmological scales**: Khoury's framework explains why dynamics differ at galactic vs. cluster vs. cosmological scales. Phonon-exflation faces a similar challenge and could be informed by this solution.

---

## Key Equations

1. **Superfluid equation of state** (polytropic):
   $$P = \lambda \rho^3, \quad c_s^2 = \frac{\partial P}{\partial \rho} = 3 \lambda \rho^2$$

2. **Superfluid condensate order parameter**:
   $$\psi(\mathbf{r}, t) = \sqrt{\rho_s(\mathbf{r})} e^{i\phi(\mathbf{r}, t)}$$

3. **Phase transition temperature** (scaling):
   $$T_c \propto \rho^{2/3}$$

4. **Phonon-mediated drag force**:
   $$F_{\text{phonon}} \sim \rho_s c_s^2 \sigma_0 a$$

5. **MOND acceleration formula (emergent)**:
   $$a_{\text{eff}} = \sqrt{a_0 g_N}, \quad a_0 \sim c_s^2 / r_0$$

6. **Quantized vortex circulation**:
   $$\oint \mathbf{v}_s \cdot d\mathbf{l} = \frac{\hbar}{m_\phi}$$

7. **Vortex density in rotating system**:
   $$n_{\text{vortex}} \approx \frac{2 m_\phi \Omega}{\hbar}$$

---

## Legacy and Significance

This paper opened a new research direction in dark matter physics, inspiring:

- **Superfluid dark matter models**: Multiple follow-up papers exploring variations and observational predictions
- **Axionic dark matter experiments**: New motivation for axion detection (ADMX, etc.)
- **Morphological transitions in cosmology**: Recognition that dark matter behavior changes with scale/environment
- **Phonon physics in cosmology**: Broader appreciation for how condensed matter concepts apply to fundamental physics

For the cosmic web, the superfluid dark matter framework suggests that large-scale structure arises from the hydrodynamics of a superfluid medium. Filaments and clusters form where the superfluid density is highest, and voids form where it is lowest. The cosmic web's structure is thus a manifestation of superfluid flow and condensation patterns.

---

## References

[Search results integrated; full citations available in search output above.]
