# Analogue Gravity: How Condensed-Matter Systems Simulate Spacetime and Gravity (2005)

**Author:** Carlos Barcelo, Stefano Liberati, Matt Visser
**Year:** 2005 (comprehensive review); foundational work 1998-2005
**Source:** Barcelo, C., Liberati, S., & Visser, M. (2005) "Analogue Gravity." Living Reviews in Relativity 8: 12

---

## Abstract

Barcelo, Liberati, and Visser's 2005 review comprehensively documents how gravitational phenomena (curved spacetime, event horizons, Hawking radiation, Unruh effects) emerge from condensed-matter systems. Acoustic waves in flowing fluids experience curved-spacetime geometry; photons in metamaterials exhibit negative refraction analogous to gravitational lensing; Bose-Einstein condensates generate Hawking-like radiation at their sonic horizons. The review systematically maps every aspect of general relativity into analogous condensed-matter physics, showing that gravity is not special—it is one realization of generic emergence principles that apply to any wave system in an inhomogeneous medium. This review is the foundational reference for understanding how quantum field theory and gravity can emerge from more fundamental, discrete constituents, and is essential background for the phonon-exflation framework.

---

## Historical Context

By 2005, multiple researchers had proposed analogue gravity systems:

1. **Unruh (1981)**: Sonic black holes in flowing fluids
2. **Visser (1998)**: Comprehensive framework relating wave equations to gravitational metrics
3. **Various BEC groups (2000-2005)**: Experimental realizations in ultracold atoms
4. **Metamaterials group (2000-2005)**: Analogues in photonic and phononic systems

The 2005 Living Reviews article by Barcelo, Liberati, and Visser synthesized the field, providing the first comprehensive reference documentation. It established analogue gravity as a serious research program with implications for fundamental physics.

---

## Core Principles: From Gravity to Effective Metrics

### The Master Equation: Wave in Inhomogeneous Medium

Any wave equation in an inhomogeneous medium can be written in a form resembling the wave equation in curved spacetime:

$$\Box_g \Psi = \frac{1}{\sqrt{-g}} \partial_\mu (\sqrt{-g} g^{\mu\nu} \partial_\nu \Psi) = 0$$

For a wave (scalar, vector, or spinor) in a material with varying density, velocity, or refractive index, the effective metric is:

$$g_{\mu\nu}^{\text{eff}} \propto \rho(\vec{r}) / c(\vec{r}) \times (\text{metric tensor constructed from medium properties})$$

where $\rho$ is the medium density and $c$ is the wave speed (sound, light, etc.).

### Equivalence Principle in Analogue Systems

Einstein's equivalence principle states: local physics is indistinguishable from free-fall in a gravitational field. In analogue systems, the principle maps to: local wave physics is indistinguishable from waves in an effective curved metric.

A water wave doesn't "know" whether it's in a inhomogeneous fluid or in curved spacetime geometry—both produce the same wave equation and the same effective metric.

---

## Specific Implementations

### Acoustic Analogue: Flowing Fluids

Waves in a fluid with velocity $\vec{v}$ experience an effective metric:

$$g_{\mu\nu}^{\text{eff}} = \rho c^2 \begin{pmatrix} v^2/c^2 - 1 & -v_x/c & -v_y/c & -v_z/c \\ -v_x/c & 1 & 0 & 0 \\ -v_y/c & 0 & 1 & 0 \\ -v_z/c & 0 & 0 & 1 \end{pmatrix}$$

where $c$ is sound speed and $\vec{v}$ is fluid velocity.

An acoustic horizon forms where $v = c$ (fluid moving at sound speed). Hawking radiation emerges from pair production at the horizon.

### Electromagnetic Analogue: Metamaterials

In a photonic metamaterial with spatially-varying refractive index $n(\vec{r})$ and permeability $\mu(\vec{r})$, the effective metric for light is:

$$g_{\mu\nu}^{\text{eff}} \propto \begin{pmatrix} \mu/n & \text{...} \\ ... & -n/\mu \end{pmatrix}$$

By engineering $n(\vec{r})$ and $\mu(\vec{r})$, one can create optical black holes, lensing, and other gravitational effects for light.

### Bose-Einstein Condensate Analogue

In a BEC, the order parameter $\Psi(\vec{r})$ creates an effective metric for excitations:

$$g_{\mu\nu}^{\text{eff}} \propto |\Psi(\vec{r})|^2 \times (\text{metric from condensate dynamics})$$

Regions of high condensate density correspond to strong "gravitational" fields; vortices correspond to black holes.

---

## Horizons, Thermodynamics, and Hawking Radiation

### Event Horizons in Analogue Systems

A sonic horizon forms where wave speed equals medium velocity. This is not a gravitational event horizon but exhibits analogous properties:

1. **One-way membrane**: Waves cannot propagate outward past the horizon
2. **Thermodynamic properties**: The horizon has temperature and entropy
3. **Pair creation**: Quantum fluctuations produce particle-antiparticle pairs at the horizon

### Hawking Radiation Analog

At an acoustic horizon, phonons are pair-created:
- One phonon escapes to infinity (carrying positive energy)
- One phonon falls inward (carrying negative energy)

The escaping phonons appear as thermal radiation with Hawking temperature:

$$T_H = \frac{\hbar \kappa}{2\pi k_B}$$

where $\kappa$ is the "surface gravity" (gradient of fluid velocity at the horizon).

### Entropy and Black Hole Thermodynamics

The entropy of an acoustic horizon scales with area (analogous to Bekenstein entropy):

$$S = \text{constant} \times \frac{\text{Horizon Area}}{\ell_{\text{Planck}}^2}$$

In analogue systems, this is not mysterious—entropy counts the degrees of freedom in the underlying medium (atoms, phonons) near the horizon.

This suggests that in actual black holes, the entropy-area law arises from counting microscopic degrees of freedom in the underlying quantum geometry (whether discrete lattice, superfluid, or other structure).

---

## Universality: Gravity as Emergent Phenomenon

### Generic Emergence

The key insight of analogue gravity: every wave system in an inhomogeneous medium exhibits effective gravitational phenomena. Gravity is not special—it is a generic emergent feature of any wave equation.

This suggests that in nature:
- Spacetime (curvature) is an effective metric emerging from microscopic structure
- Gravitons are excitations in the underlying medium, not fundamental particles
- General relativity is a low-energy effective theory, valid at scales much larger than the microscopic lattice

### Lorentz Invariance as Emergent Symmetry

In any fluid or condensed-matter system, at long wavelengths and low frequencies, the wave equations exhibit Lorentz invariance approximately:

$$\omega(k) \approx c_s |\vec{k}|$$

(linear dispersion, speed of light = sound speed)

Deviations from Lorentz invariance appear at short wavelengths (high frequencies), where the discrete nature of the medium becomes important.

This explains why Lorentz invariance appears to be fundamental: it is a low-energy effective symmetry of the microscopic discrete system.

---

## Cosmological Implications

### Inflationary Expansion as Effective Metric

In an expanding cosmology, the metric $g_{\mu\nu}$ encodes expansion:

$$ds^2 = -dt^2 + a(t)^2 d\vec{x}^2$$

Analogue gravity suggests: expansion is an effective metric emerging from changing medium properties. As the universe expands, the density and other properties of the underlying medium change, causing the effective metric to evolve.

### Cosmological Constant as Vacuum Energy

The cosmological constant (dark energy) is:

$$\rho_\Lambda = \frac{\Lambda}{8\pi G}$$

In analogue gravity, this is understood as zero-point energy of the underlying medium:

$$\rho_\Lambda = \sum_{\text{modes}} \frac{1}{2} \hbar \omega_i$$

where the sum runs over all excitation modes of the medium.

### Early Universe and QFT Vacuum

The early hot universe is understood as a thermal distribution of excitations (particles) in the medium:

$$\langle N_i \rangle = \frac{1}{e^{\hbar\omega_i/k_B T} - 1}$$

(Bose-Einstein or Fermi-Dirac distribution)

As the universe expands and cools, fewer modes are thermally excited. The particles we observe (photons, electrons, quarks) are the few excitations that remain at low temperatures.

---

## Quantum-to-Classical Transition

### Why Classical Spacetime?

The theory predicts that at low energies (long wavelengths), smooth classical spacetime emerges. At Planck scales, the structure is quantum (discrete, noncommutative, probabilistic).

The emergence of classical geometry from quantum geometry parallels the emergence of classical thermodynamics from quantum statistical mechanics—a well-understood phenomenon.

### Decoherence and Thermodynamic Limit

In the thermodynamic limit (many particles, large system), quantum effects average out and classical behavior emerges. Similarly, in the cosmological/macroscopic limit, quantum geometry averages to smooth spacetime.

This is not a novel principle but a generic feature of many-body quantum systems.

---

## Connection to Phonon-Exflation Framework

Barcelo, Liberati, and Visser's 2005 review is the single most important reference for understanding phonon-exflation:

1. **Emergence principle**: The review systematically demonstrates that gravity (spacetime curvature) emerges from microscopic wave dynamics. Phonon-exflation applies this principle specifically: particles and gravity emerge from phonons in the SU(3) geometry.

2. **No fundamental particles**: Analogue gravity shows that "particles" (excitations) are emergent—they are not fundamental constituents but collective modes of a medium. In phonon-exflation, electrons, quarks, photons are precisely this: phonons of the SU(3) superfluid.

3. **Metric from medium properties**: The effective metric in analogue systems depends on local properties (density, velocity, refractive index). In phonon-exflation, the spacetime metric emerges from the order parameter of the SU(3) superfluid—a specific "medium property."

4. **Hawking radiation as generic phenomenon**: The review explains Hawking radiation as quantum pair creation at horizons—a feature of any wave system with an effective horizon. In phonon-exflation, particle creation (whether Hawking, thermal, or vacuum fluctuation) is the same process: exciting phonon modes.

5. **Lorentz invariance as low-energy effective symmetry**: The review documents how Lorentz invariance emerges at long wavelengths but is broken at Planck scales. Phonon-exflation is built on this insight: the Dirac spectrum on SU(3) exhibits Lorentz-like dispersion at low energies (high wavelengths in internal space), but is discrete and deformed at high energies (short wavelengths, near Planck scale).

6. **Universality of emergent gravity**: The review's key message is that gravity is generic—any wave system produces it. Phonon-exflation universalizes this further: any quantum system with a ground state, excitations, and a geometric structure will exhibit emergent gravity, particle physics, and cosmology.

7. **Cosmological constant from zero-point energy**: The review explains dark energy as sum of zero-point energies of all modes. Phonon-exflation calculates this explicitly: the spectral action $S = \int d^4x \sqrt{-g} \text{Tr}(f(D_K^2/\Lambda^2))$ is precisely this sum, weighted by a smooth function $f$.

8. **Foundational reference**: The review provides comprehensive coverage of:
   - Wave equations in curved spacetime
   - Effective metrics from condensed-matter systems
   - Hawking radiation mechanisms
   - Thermodynamic properties of horizons
   - Observational signatures

All of these are foundational to phonon-exflation.

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Wave in curved spacetime | $\Box_g \Psi = 0$ | General wave equation |
| Effective metric (general) | $g_{\mu\nu}^{\text{eff}} = f(\text{medium props})$ | Metric from medium properties |
| Acoustic metric (flowing fluid) | $g_{\mu\nu} = \rho c^2 \text{diag}(v^2/c^2 - 1, ...)$ | Metric from flow velocity |
| Hawking temperature | $T_H = \frac{\hbar \kappa}{2\pi k_B}$ | Black hole/horizon temperature |
| Bekenstein entropy | $S = \frac{k_B c^3 A}{4G\hbar}$ | Entropy proportional to area |
| Lorentz dispersion (emergent) | $\omega(k) \approx c_s \|\vec{k}\|$ | Linear dispersion at low $k$ |
| Zero-point energy (cosmological constant) | $\rho_\Lambda = \sum_i \frac{1}{2}\hbar\omega_i$ | Sum of vacuum fluctuations |

---

## Critical Assessment

**Strengths**:
- Comprehensive review covering all aspects of analogue gravity
- Rigorous mathematical development
- Experimental implementations verified
- Clear demonstration of universality of emergence principles
- Foundational for understanding emergent gravity

**Scope and Limitations**:
- Does not attempt to unify particle physics with gravity (that is beyond the scope)
- Remains agnostic about the true microscopic structure (what is the underlying medium?)
- Does not provide quantitative predictions for specific cosmologies
- Analogue systems model aspects of gravity, not complete gravity theory

**Impact**:
- Changed how physicists think about gravity (emergent rather than fundamental)
- Opened new experimental avenues for studying quantum gravity
- Connected condensed-matter physics and general relativity
- Inspired numerous follow-up theoretical and experimental programs

---

## Legacy and Future Directions

This review has been cited ~10,000 times and remains the standard reference:

1. **Analog gravity experiments**: BEC, superfluid, metamaterial platforms for studying gravitational phenomena
2. **Emergent gravity theories**: Multiple approaches building on Barcelo-Liberati-Visser framework
3. **Quantum gravity alternatives**: LQG, string theory, and other approaches informed by analogue gravity insights
4. **Foundational physics**: Deep questions about the nature of spacetime, emergence, and reductionism

---

## References

1. Barcelo, C., Liberati, S., & Visser, M. (2005). "Analogue gravity." Living Reviews in Relativity 8: 12.
2. Visser, M., Bassett, B., & Liberati, S. (1999). "Perturbative superluminal propagation: A general power-counting argument." Classical and Quantum Gravity 16: 1169-1198.
3. Unruh, W.G. (1981). "Experimental Black-Hole Evaporation?" Physical Review Letters 46: 1351-1353.
4. Jacobson, T. (1995). "Thermodynamics of spacetime: The Einstein equation of state." Physical Review Letters 75: 1260-1263.
5. Hawking, S.W. (1974). "Black hole explosions?" Nature 248: 30-31.
6. Garay, L.J., Anglin, J.R., Cirac, J.I., & Zoller, P. (2000). "Sonic analog of gravitational black holes in Bose-Einstein condensates." Physical Review Letters 85: 4643-4647.
7. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press.
8. Connes, A. (1994). "Noncommutative geometry." Academic Press.
