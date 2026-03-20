# Theory of Dark Matter Superfluidity

**Author(s):** Lasha Berezhiani, Justin Khoury

**Year:** 2015

**Journal:** Physical Review D, Volume 92, Article 103510

---

## Abstract

Berezhiani and Khoury develop a comprehensive theoretical framework in which dark matter consists of self-interacting axion-like particles that undergo a phase transition to a superfluid state within galaxies. The superfluid's collective excitations (phonons) mediate an effective MOND-like acceleration law on baryonic matter at galactic scales, while cluster-scale physics remains governed by particle-like dark matter. This paper provides the theoretical foundation for superfluid dark matter, detailing the phase diagram, equation of state, order parameter dynamics, and observational predictions. The theory elegantly unifies MOND's success in galaxy dynamics with ΛCDM's success in cosmology.

---

## Historical Context

Building on their earlier papers (Khoury 2015, Berezhiani & Khoury 2015), the authors present a detailed theoretical treatment in Physical Review D. This work synthesizes condensed matter physics, quantum field theory, and cosmology into a coherent framework. The publication in a premier physics journal signaled the seriousness and rigor of the superfluid dark matter program.

---

## Key Arguments and Derivations

### Fundamental Theory: Self-Interacting Axion-Like Particles

The dark matter consists of a complex scalar field $\phi$ with Lagrangian:

$$\mathcal{L} = \partial_\mu \phi^* \partial^\mu \phi - m_\phi^2 |\phi|^2 - \lambda (|\phi|^2)^2 + \text{higher order}$$

The potential has a minimum at $|\phi| = v$ where:

$$v = \sqrt{\frac{m_\phi^2}{2\lambda}}$$

At low temperatures and high density, the field condenses:

$$\phi(\mathbf{r}, t) = \sqrt{\rho_s/m_\phi} e^{i\Theta(\mathbf{r}, t)}$$

where $\rho_s$ is the superfluid density (number of condensed particles).

### Equation of State and Thermodynamics

The pressure-density relation (equation of state) for the superfluid is derived from the effective action:

$$P = \lambda \rho^3 + \text{quantum corrections}$$

This is a **polytropic equation of state** with index $\gamma = 3$ (more accurately, $\gamma$ is slightly higher due to quantum corrections, but the polytropic form dominates at low energies).

The sound speed in the superfluid is:

$$c_s^2 = \frac{\partial P}{\partial \rho} = 3 \lambda \rho^2 + \text{quantum corrections}$$

For superfluid 3He and dilute BEC gases, observations and theory give $c_s \sim 1-100$ m/s (depending on density and temperature).

For dark matter, Berezhiani and Khoury estimate $c_s \sim 10$ km/s in galactic cores, yielding the observed MOND acceleration scale.

### Phase Diagram and Superfluid-Normal Transition

The critical temperature for the superfluid transition is:

$$T_c = T_0 \left( \frac{\rho}{\rho_0} \right)^{2/3}$$

This follows from general scaling arguments in superfluid systems. The superfluid density as a function of temperature and density is:

$$\rho_s(T, \rho) = \rho \left[ 1 - \left( \frac{T}{T_c} \right)^{\nu} \right]$$

where $\nu$ is a critical exponent (typically $\nu \approx 2/3$ for Bose systems).

The phase diagram has several regimes:

1. **Deep superfluid** (low T, high ρ): $\rho_s \approx \rho$ (nearly all particles condensed)
2. **Mixed phase** (intermediate): $0 < \rho_s < \rho$ (partial condensate)
3. **Normal phase** (high T or low ρ): $\rho_s \approx 0$ (no condensate)

**Galactic cores**: T ~ mK, ρ ~ 0.1 GeV/cm³ → deep superfluid
**Cluster outskirts**: T ~ μK, ρ ~ 10^{-4} GeV/cm³ → normal phase

### Phonon Dynamics and MOND-Like Acceleration

In the superfluid state, Bogoliubov quasiparticles (phonons) are the elementary excitations. A baryonic test particle (e.g., a star) interacts with the condensate via two mechanisms:

1. **Drag from phonon scattering**: As the particle moves through the condensate at velocity $\mathbf{v}$, it scatters off phonons, experiencing a drag force.

2. **Effective gravitational coupling**: The condensate's density distribution affects the gravitational field experienced by baryons.

The equation of motion for a baryonic mass in the galactic superfluid is:

$$m_b \mathbf{a} = -\nabla \Phi_g - m_b \nabla \Phi_{\text{eff}}$$

where $\Phi_g$ is the gravitational potential and $\Phi_{\text{eff}}$ is an effective potential arising from the superfluid's density distribution.

In the MOND regime, the effective potential dominates over the gravitational potential, yielding:

$$m_b a = F_{\text{eff}} \approx \sqrt{m_b c_s^2 g}$$

which reproduces the MOND formula $a_{\text{eff}} = \sqrt{a_0 g_N}$ with $a_0 \sim c_s^2 / \ell$ (where $\ell$ is a characteristic length scale).

### Quantized Vortices and Stability

In a rotating galaxy with angular velocity $\Omega$, the superfluid spontaneously forms a vortex lattice. The vortex density is:

$$n_v = \frac{2m_\phi \Omega}{\hbar}$$

For galactic parameters:
- $\Omega \sim 10^{-15}$ rad/s
- $m_\phi \sim 10^{-22}$ eV (axion mass)

This gives $n_v \sim 10^{-7}$ cm^{-2} per unit height, corresponding to vortex separation ~10 pc. The vortex lattice is so sparse that it does not significantly affect galactic dynamics but might leave observable signatures in merger events or in the structure of galactic halos.

### Hydrodynamic Instabilities and Structure Formation

The superfluid dark matter undergoes instabilities on certain scales, leading to structure formation. These instabilities are driven by:

1. **Kelvin-Helmholtz instability**: Velocity shear at the boundaries between superfluid and normal regions
2. **Rayleigh-Taylor instability**: Density inversion in the superfluid
3. **Jeans instability**: Gravity acting on density perturbations

The **Jeans length** in the superfluid is:

$$\lambda_J = c_s \sqrt{\frac{\pi}{G \rho}}$$

For dark matter with $c_s \sim 10$ km/s and $\rho \sim 0.1$ GeV/cm³:

$$\lambda_J \sim 100 \text{ kpc}$$

This is the minimum length scale at which the superfluid contracts under gravity, consistent with the size of galactic halos.

### Observational Predictions

The theory makes specific, falsifiable predictions:

1. **Axion mass and coupling**: Detectable in experiments like ADMX if $m_\phi \sim$ eV

2. **Sound speed**: Measurable from galactic dynamics; should be $\sim 10$ km/s in cores

3. **Vortex signatures**: In merging galaxies, vortex tangles might produce heating or asymmetric mass distributions

4. **Baryon acoustic oscillations**: The BAO peak in galaxy surveys reflects the sound speed in the early universe

5. **Transition scale**: MOND-to-ΛCDM transition should occur at a specific cluster-scale diameter, measurable via weak lensing

---

## Key Results

1. **Comprehensive theoretical framework**: A complete theory of superfluid dark matter with specified equation of state, thermodynamics, and dynamics.

2. **MOND emergence from first principles**: MOND's empirical law emerges from superfluid phonon physics, not requiring ad-hoc modifications.

3. **Natural phase structure**: The superfluid-to-normal transition naturally explains why dynamics differ at galactic vs. cluster scales.

4. **Detailed predictions**: Sound speed, critical scales, vortex properties—all are calculable from the theory.

5. **Consistency checks**: The theory's predictions for BAO, structure formation timescales, and galaxy kinematics are consistent with observations.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: VERY HIGH**

This paper is arguably the most important precedent for phonon-exflation:

- **Particles as phonons in condensate**: Berezhiani-Khoury treat dark matter as phonons. Phonon-exflation generalizes this: all particles (not just dark matter) are phonons in the NCG condensate.

- **Superfluid equation of state**: The polytropic EOS $P \propto \rho^3$ emerges from self-interactions. In phonon-exflation, the EOS might emerge from the spectral action of the NCG substrate.

- **Phase structure and scale-dependent physics**: The superfluid-normal phase transition explains why physics differs at different scales. Phonon-exflation predicts scale-dependent physics from the NCG geometry.

- **Phonon sound speed as fundamental**: In Berezhiani-Khoury, the sound speed $c_s$ is fundamental and constrains galactic dynamics. In phonon-exflation, the phonon dispersion relation (with its sound speeds at different energies) is fundamental and should constrain all physics.

- **Vortex networks as topological objects**: Quantized vortices are topological defects in superfluids. In phonon-exflation, cosmic strings, monopoles, and other defects are topological excitations of the NCG substrate.

- **Unification of scales**: Berezhiani-Khoury unifies galactic and cosmological physics via phase transitions. Phonon-exflation aims to unify quantum and gravitational scales via geometric emergence.

---

## Key Equations

1. **Self-interacting axion Lagrangian**:
   $$\mathcal{L} = \partial_\mu \phi^* \partial^\mu \phi - m_\phi^2 |\phi|^2 - \lambda (|\phi|^2)^2$$

2. **Condensate order parameter**:
   $$\phi(\mathbf{r}, t) = \sqrt{\rho_s / m_\phi} e^{i\Theta}$$

3. **Superfluid equation of state** (polytropic):
   $$P = \lambda \rho^3, \quad c_s = \sqrt{3\lambda \rho^2}$$

4. **Critical temperature scaling**:
   $$T_c = T_0 \left( \frac{\rho}{\rho_0} \right)^{2/3}$$

5. **Superfluid density (near T_c)**:
   $$\rho_s(T) = \rho \left[ 1 - \left( \frac{T}{T_c} \right)^{2/3} \right]$$

6. **Bogoliubov dispersion relation** (phonons):
   $$\omega(k) = c_s k \sqrt{1 + \frac{k^2 \ell_q^2}{4}}$$
   where $\ell_q$ is the quantum healing length

7. **Vortex density in rotating superfluid**:
   $$n_v = \frac{2m_\phi \Omega}{\hbar}$$

8. **Jeans length in superfluid**:
   $$\lambda_J = c_s \sqrt{\frac{\pi}{G \rho}}$$

9. **MOND acceleration formula** (emergent):
   $$a = \sqrt{a_0 g_N}, \quad a_0 \sim \frac{c_s^2}{r_0}$$

---

## Legacy and Significance

This paper has inspired numerous follow-up studies:

- Detailed observational predictions for axion detectors
- Simulations of superfluid dark matter galaxy formation
- Tests of MOND vs. superfluid dark matter vs. ΛCDM
- Theoretical work on hydrodynamic instabilities in superfluid dark matter
- Connections to condensed matter analogues of black holes and cosmology

For the cosmic web, the superfluid dark matter framework predicts that large-scale structure emerges from the hydrodynamics of a superfluid medium. Clusters, filaments, walls, and voids are manifestations of superfluid flow and condensation patterns. This conceptual framework directly informs and motivates the phonon-exflation hypothesis.

---

## References

[Search results integrated; full citations available in search output above.]
