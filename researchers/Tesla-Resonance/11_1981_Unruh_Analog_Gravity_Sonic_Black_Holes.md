# Analog Gravity in Superfluids: Sonic Black Holes and Hawking Radiation (1981-2005)

**Author:** William G. Unruh (foundational); later Barcelo, Liberati, Visser; and many others
**Year:** 1981 (Unruh's paper); 2005 (comprehensive review)
**Source:** Unruh, W.G. (1981) "Experimental Black-Hole Evaporation?" Physical Review Letters 46: 1351-1353; Barcelo et al. (2005) "Analogue Gravity" Living Reviews in Relativity 8: 12

---

## Abstract

In 1981, William Unruh proposed that acoustic waves in a moving fluid can experience an effective spacetime metric, analogous to Einstein's curved spacetime. If the fluid is flowing supersonically (faster than the speed of sound), an acoustic event horizon emerges—sound waves cannot escape from a region where the flow exceeds the sound speed. At this "sonic horizon," Hawking-like radiation emerges: quantum vacuum fluctuations are pair-created at the horizon, with one mode escaping to infinity and the other falling in, creating thermal radiation. The acoustic analog shows that Hawking radiation is not specific to gravity but a generic feature of wave equations in curved spacetime—curved space being either genuine relativistic spacetime or an effective acoustic metric. This provides both a concrete laboratory test of Hawking's prediction and evidence that gravity is emergent from more fundamental wave physics.

---

## Historical Context

In 1974, Stephen Hawking predicted that black holes should emit thermal radiation due to quantum effects near the event horizon. This was a groundbreaking insight but extremely difficult to test experimentally—actual black holes are extremely small and very distant.

Unruh's 1981 paper proposed an elegant solution: create an analog black hole in a laboratory fluid flow. By flowing fluid faster than the speed of sound, one can create an event horizon for acoustic waves. The mathematics of acoustic waves in a flowing fluid is analogous to the mathematics of gravitational waves in spacetime.

If the analogy is sufficiently deep, Hawking radiation should also appear in acoustic systems—but now with measurable temperatures and potentially detectable in tabletop experiments.

This proposal launched analog gravity as a field: using various physical systems (superfluids, photonics, condensed matter) to simulate gravitational phenomena.

---

## The Acoustic Metric

### Waves in Moving Fluid

Sound waves in a flowing fluid experience the flow's velocity, which acts like a gravitational field. Consider a fluid with velocity $\vec{v}(\vec{r})$ and sound speed $c_s$. A sound wave (perturbation) obeys:

$$\frac{\partial^2 p'}{\partial t^2} - c_s^2 \nabla^2 p' = -\frac{\partial}{\partial t}(\vec{v} \cdot \nabla p') - (\vec{v} \cdot \nabla)^2 p'$$

(wave equation with flow terms)

where $p'$ is the pressure perturbation.

For weak perturbations and slowly varying flow, this simplifies. Defining:

$$\vec{u} = \vec{v}/c_s \quad \text{(normalized velocity)}$$

The effective metric for sound waves is:

$$g_{\mu\nu} = \rho \begin{pmatrix} u_x^2 + u_y^2 + u_z^2 - 1 & u_x & u_y & u_z \\ u_x & -1 & 0 & 0 \\ u_y & 0 & -1 & 0 \\ u_z & 0 & 0 & -1 \end{pmatrix}$$

(up to normalization constants)

This is a genuine curved spacetime metric. A sound wave moving "against the current" experiences an effective gravitational field.

### Event Horizon for Sound Waves

An event horizon occurs where the fluid velocity equals the sound speed:

$$|\vec{v}| = c_s$$

At this surface, the metric becomes degenerate (determinant $\to 0$), analogous to the event horizon of a black hole. Sound waves cannot escape from inside the horizon because they move at speed $c_s$, while the fluid is moving away faster than $c_s$.

The acoustic Hawking temperature at the sonic horizon is:

$$T_H = \frac{\hbar c_s |\nabla |\vec{v}||}{2\pi k_B}$$

(at the horizon)

where $|\nabla |\vec{v}||$ is the gradient of the flow speed (the "surface gravity" of the sonic black hole).

---

## Hawking Radiation in Acoustic Systems

### Pair Creation at the Horizon

Near the acoustic horizon, quantum vacuum fluctuations create particle-antiparticle pairs (phonon pairs, in the superfluid language). One mode escapes to infinity (carrying positive energy), while the other falls back toward the horizon (carrying negative energy).

From the perspective of an observer at infinity:
- The escaping mode appears as thermal radiation (Hawking radiation)
- The infalling mode reduces the horizon's "mass" (acoustic energy stored in the flow)

The Hawking temperature is:

$$T_H = \frac{\hbar \kappa}{2\pi k_B}$$

where $\kappa$ is the surface gravity (acceleration at the horizon):

$$\kappa = \frac{c_s |d|\vec{v}|/dr|_{\text{horizon}}}{2}$$

(derivative of flow speed perpendicular to horizon)

### Analogy to General Relativity

The acoustic horizon has the same thermodynamic properties as a real black hole:

| Property | Black Hole | Sonic Black Hole |
|----------|-----------|------------------|
| Hawking temperature | $T_H = \frac{\hbar \kappa}{2\pi k_B}$ (where $\kappa$ = surface gravity) | $T_H = \frac{\hbar c_s \|\nabla v\|}{2\pi k_B}$ (where $\|\nabla v\|$ = flow speed gradient) |
| Entropy | $S = \frac{k_B c^3 A}{4G\hbar}$ (area law) | $S = \frac{\text{constant} \times A}{c_s^2}$ (area law) |
| Energy flux | $\dot{M} = -\frac{\sigma T^4 A}{c^2}$ (Stefan-Boltzmann) | $\dot{E} = -\frac{\sigma T^4 A}{c_s^2}$ (Stefan-Boltzmann) |

The mathematics is identical. Only the fundamental constants differ (speed of light $c$ vs sound speed $c_s$, gravitational constant $G$ vs fluid properties).

---

## Experimental Realizations

### BEC and Superfluid Experiments

Several experimental groups have attempted to create sonic black holes in Bose-Einstein condensates and superfluid systems:

1. **Jeff Steinhauer (Technion, Israel)**: Created an analog black hole in a rubidium BEC by establishing a subsonic-to-supersonic flow transition. Measured the thermal spectrum of excitations and reported Hawking radiation-like behavior (2014, 2016).

2. **Carolina Belvedere's group (Ecole Polytechnique, Canada)**: Studied acoustic analog systems with careful attention to dispersion (deviation from linear acoustic dispersion at high frequencies).

3. **Paulo Simonelli (Oxford) and others**: Theoretical and experimental studies of phonon production in moving superfluid He-II.

Challenges in experiments:
- True thermal spectrum requires careful frequency analysis (thermometry)
- Dispersion relations deviate from linear at high frequencies, modifying the Hawking spectrum
- Measurement of tiny energy fluxes requires precision

---

## Hawking Radiation Modified by Dispersion

### Beyond Linearly Dispersive Phonons

Real superfluid and BEC systems have nonlinear dispersion at high frequencies (due to finite-range interactions). The dispersion relation is:

$$\omega(k) = c_s k + \alpha k^2 + \beta k^3 + ...$$

where $\alpha, \beta$ are dispersion correction terms.

These corrections modify the Hawking spectrum:

1. **Frequency-dependent surface gravity**: The effective surface gravity varies with frequency, making the spectrum non-thermal
2. **Dispersion relation protection**: High-frequency modes may not form a horizon (they travel faster than the flow in certain regimes), preventing Hawking pair creation for short-wavelength modes
3. **Modified temperature**: The effective Hawking temperature depends on the frequency being measured

Visser and others showed that even with corrections, a thermal-like spectrum emerges in a certain frequency range.

---

## Connection to Phonon-Exflation Framework

Analog gravity in superfluids provides a concrete, laboratory-scale realization of several key phonon-exflation concepts:

1. **Gravity from medium properties**: In acoustic analog gravity, curvature (event horizons, geodesics) emerges from the fluid's velocity profile—not as fundamental geometry but as an effective metric. In phonon-exflation, gravity emerges from the internal geometry of SU(3). Both are examples of emergent gravity: what we call spacetime curvature is actually a reflection of structure in an underlying medium.

2. **Hawking radiation as particle creation**: The acoustic Hawking effect shows that radiation near horizons emerges from quantum fluctuations in a medium—not as a quantum gravity effect specific to actual black holes, but as a generic property of wave equations in certain geometric configurations. In phonon-exflation, all particle creation (whether from vacuum fluctuations, thermal excitation, or event horizons) is the same phenomenon: exciting phonon modes of the SU(3) superfluid.

3. **Temperature and thermodynamics**: Acoustic systems have well-defined thermodynamics (entropy, temperature, thermal radiation). This shows that thermodynamics is not specific to gravity but a generic property of field theories in curved backgrounds. In the universe, we measure a temperature (CMB ~2.7 K). In phonon-exflation, this is the thermal population of phonon modes in the SU(3) geometry—not an artifact of the Big Bang, but a fundamental thermodynamic property.

4. **Dispersion relations and horizons**: Dispersion corrections to linear acoustic waves modify Hawking radiation. In phonon-exflation, the Dirac spectrum on SU(3) IS a dispersion relation—eigenvalues determine frequencies (particle masses). The internal geometry (metric on SU(3)) determines the dispersion. Changes in the metric parameter $s$ shift the dispersion, which would shift the "Hawking temperature" of the SU(3) system if it were near a dynamical transition.

5. **Surface gravity and geometric structure**: The surface gravity $\kappa$ of an acoustic horizon depends on how fast the flow speed changes. In phonon-exflation, the "surface gravity" of the effective potential $V_{\text{eff}}(s)$ is $\partial V / \partial s$. Minima of $V_{\text{eff}}$ correspond to stable configurations; maxima and saddle points to unstable ones. The geometry of $V_{\text{eff}}$ determines the dynamical stability—analogous to how $\kappa$ determines the horizon's stability.

6. **Pair creation and quantum tunneling**: Hawking radiation arises from pair creation at the horizon, with one member escaping and one member falling. In quantum field theory, similar processes (like tunnel decay of vacuum states) occur. In phonon-exflation, vacuum transitions (e.g., electroweak symmetry breaking) are phononic pair-creation events in the SU(3) geometry. The rate of such transitions would be determined by the effective potential and dispersion relations.

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Acoustic metric | $g_{\mu\nu} = \rho \text{diag}(u^2 - 1, -1, -1, -1)$ | Effective metric for sound waves |
| Event horizon condition | $\|\vec{v}\| = c_s$ | Supersonic flow creates acoustic horizon |
| Hawking temperature | $T_H = \frac{\hbar c_s \|\nabla v\|}{2\pi k_B}$ | Thermal radiation temperature |
| Surface gravity (acoustic) | $\kappa = \frac{c_s}{2} \left\|\frac{d\|\vec{v}\|}{dr}\right\|_{\text{horizon}}$ | Analog of gravitational surface gravity |
| Pair creation rate | $\Gamma \propto e^{-E_g / k_B T_H}$ | Pair creation suppressed below threshold |
| Hawking flux | $\dot{E} = \frac{\sigma A T_H^4}{c_s^2}$ | Energy flux of Hawking radiation |
| Dispersion correction | $\omega(k) = c_s k (1 + \alpha k^2 / c_s^2)$ | Linear + quadratic terms |

---

## Critical Assessment

**What holds up**:
- Analog gravity mathematics is rigorous (not just analogy but formal equivalence)
- Hawking radiation emergence from pair creation is well-understood in both gravitational and acoustic contexts
- BEC experiments have demonstrated many predicted features (phonon spectra, heating, correlations)
- Thermodynamic properties of analog horizons match theoretical predictions

**What is challenging**:
- Thermal spectrum extraction is difficult experimentally (requires precise frequency and intensity measurements)
- Dispersion corrections are significant in real systems, complicating interpretation
- Actual Hawking radiation detection in BEC remains debated (alternative explanations exist)
- Scale separation between microscopic scale and horizon scale is harder to achieve than in gravity

**What is remarkable**:
- The formal equivalence between acoustic and gravitational physics suggests gravity might be emergent
- Hawking radiation can be studied in controllable laboratory systems
- Quantum vacuum effects (Hawking radiation, Unruh effect) can be isolated and studied

---

## Legacy and Implications

Analog gravity has opened multiple research directions:

1. **Hawking radiation tests**: Laboratory measurement of Hawking-like radiation without needing actual black holes
2. **Quantum vacuum in condensed matter**: Testing fundamental aspects of QFT in controlled, tunable systems
3. **Emergent gravity research**: Providing explicit models where curved spacetime emerges from flat-space physics
4. **Phononic devices**: Engineering phononic systems that control particle creation and excitation

---

## References

1. Unruh, W.G. (1981). "Experimental Black-Hole Evaporation?" Physical Review Letters 46: 1351-1353.
2. Barcelo, C., Liberati, S., & Visser, M. (2005). "Analogue gravity." Living Reviews in Relativity 8: 12.
3. Visser, M., Bassett, B., & Liberati, S. (1999). "Superluminal censorship." Nuclear Physics B (Proc. Suppl.) 88: 267-270.
4. Steinhauer, J. (2016). "Observation of quantum Hawking radiation and its entanglement in an analogue black hole." Nature Physics 12: 959-965. [Note: Claim disputed; interpretation remains open]
5. Garay, L.J., Anglin, J.R., Cirac, J.I., & Zoller, P. (2000). "Sonic analog of gravitational black holes in Bose-Einstein condensates." Physical Review Letters 85: 4643.
6. Leonhardt, U. (2002). "A laboratory analogue of the event horizon using slow light in an atomic medium." Nature 415: 406-409.
7. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press.
