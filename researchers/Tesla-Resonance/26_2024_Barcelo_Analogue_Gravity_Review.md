# Analogue Gravity (updated review, v4)

**Authors:** Carlos Barceló, Stefano Liberati, Matt Visser

**Year:** 2024

**Journal:** Living Reviews in Relativity (ongoing publication)

**Identifier:** arXiv:gr-qc/0505065v4 (November 29, 2024)

---

## Abstract

Analogue gravity is a research programme that explores analogues of general relativistic phenomena within other physical systems, primarily condensed matter and fluid dynamics. The approach leverages the observation that the equations governing wave propagation in complex media (superfluids, Bose-Einstein condensates, flowing fluids, metamaterials) can be mapped to wave equations in curved spacetime. This living review, updated to version 4 in late 2024, synthesizes 20 years of developments, covering black hole analogues, Hawking radiation signatures, cosmological horizons, rotating spacetimes, and recent advances in experimental realization and novel analog systems. The review establishes analog gravity as a mature, experimentally validated programme bridging quantum field theory, condensed matter physics, and gravitational physics.

---

## Historical Context

General relativity's nonlinearity and background-dependence have made direct experimental testing difficult. Hawking radiation, predicted in 1974, remains observationally unconfirmed in real black holes. Quantum field theory in curved spacetime—the framework describing particle creation near event horizons—is mathematically intricate and poorly understood outside a handful of symmetric spacetimes.

In the early 2000s, Barceló, Liberati, and Visser developed a radically different approach: simulate gravitational phenomena in tabletop laboratories using condensed matter systems. A flowing fluid with density perturbations evolves according to the acoustic wave equation, which **in many cases** is mathematically identical to the wave equation for massless scalar fields in a curved spacetime metric.

This insight—that the effective metric experienced by sound waves in a flowing fluid is determined by the fluid's density and velocity profiles—opened a new experimental window on black hole physics, event horizons, and Hawking radiation.

The original 2005 review article became a foundational reference. Over two decades, analog gravity has evolved from a theoretical curiosity to an experimentally active field:
- **2005**: Original review. ~500 citations over first 5 years
- **2012**: First experimental detection of Hawking radiation analogue (Weinfurtner et al. in superfluid He)
- **2015-2020**: Acceleration of experimental programs. Multiple groups demonstrate vortex analogs, cosmological horizon analogues, analog wormholes
- **2024**: v4 review incorporates the latest results, including the 2024 Svančara giant vortex experiment and holographic analog systems

---

## Key Arguments and Derivations

### Effective Metric from Wave Propagation in Media

In a medium with density $\rho(\mathbf{r}, t)$, sound speed $c_s(\mathbf{r})$, and bulk velocity field $\mathbf{u}(\mathbf{r})$, the wave equation for density perturbations $\delta \rho$ becomes:

$$\left[ \frac{\partial^2}{\partial t^2} - c_s^2(\mathbf{r}) \nabla^2 \right] \Phi = 0$$

where $\Phi$ is related to the acoustic potential. In the presence of background flow $\mathbf{u}(\mathbf{r})$, the full equation (in the non-relativistic limit) is:

$$\left[ \frac{\partial}{\partial t} + \mathbf{u} \cdot \nabla \right]^2 \Phi - c_s^2 \nabla^2 \Phi = 0$$

Expanding and collecting terms:

$$\frac{\partial^2 \Phi}{\partial t^2} + 2\mathbf{u} \cdot \nabla \frac{\partial \Phi}{\partial t} + (\mathbf{u} \cdot \nabla)^2 \Phi - c_s^2 \nabla^2 \Phi + \nabla \mathbf{u} \cdot \nabla \Phi = 0$$

This can be rewritten in covariant form as:

$$\Box_g \Phi = 0$$

where $\Box_g$ is the d'Alembertian operator with respect to an **effective metric** $g_{\mu\nu}$:

$$g_{\mu\nu} = \frac{\rho}{c_s} \begin{pmatrix} -(c_s^2 - u^2) & -u_i \\ -u_i & \delta_{ij} \end{pmatrix}$$

(in units where $c_s = 1$). This is a curved spacetime metric, with curvature determined by the flow profile $\mathbf{u}(\mathbf{r})$ and density $\rho(\mathbf{r})$.

### Black Hole Analogue: The Draining Bathtub

One of the simplest analog gravity systems is a fluid flowing radially inward (draining). In cylindrical coordinates $(r, \theta, z)$, the velocity field is:

$$\mathbf{u} = -\frac{Q}{2\pi r} \hat{r}$$

where $Q$ is the drainage rate (volume per unit time). For $c_s$ uniform, the effective metric is:

$$g_{\mu\nu} \propto \begin{pmatrix} -(c_s^2 - u_r^2) & 0 \\ 0 & r^2 \end{pmatrix} = \begin{pmatrix} -(c_s^2 - Q^2/(4\pi^2 r^2)) & 0 \\ 0 & r^2 \end{pmatrix}$$

At the radius where $u_r = c_s$ (i.e., drainage velocity equals sound speed):

$$r_h = \frac{Q}{2\pi c_s} \quad (\text{"event horizon"})$$

Sound waves approaching from outside this radius cannot escape against the inward flow—they are "trapped" beyond what looks like an event horizon. This is the acoustic analog of a black hole's event horizon.

The metric structure is Schwarzschild-like, with the "Hawking temperature" of the analog horizon given by:

$$T_H^\text{analog} = \frac{\hbar}{2\pi k_B} \kappa$$

where $\kappa$ is the surface gravity (acceleration at the horizon). For the draining vortex:

$$\kappa = \frac{d(c_s^2 - u_r^2)}{dr}\Big|_{r=r_h} \sim \frac{c_s^2}{r_h}$$

### Hawking Radiation in Analogues

Near the horizon, quantum fluctuations in the acoustic field can create phonon pairs. One partner is trapped inside the horizon, while the other escapes to infinity. The escaping modes constitute an analog of Hawking radiation, with thermal spectrum at temperature $T_H^\text{analog}$.

The detailed mechanism differs from gravitational Hawking radiation (no trapped surface, no true information loss), but the **kinematic signature**—thermal spectrum of particle creation—is identical. This is powerful: if Hawking radiation is detected in an analog system, it validates the fundamental mechanism of particle creation in curved spacetime, even though the analog is a much simpler system.

The flux of energy carried away by analog Hawking radiation is:

$$\dot{E} \sim T_H^2 A_h$$

where $A_h \sim r_h^2$ is the "horizon area." For a typical sonically draining bathtub:

$$T_H^\text{analog} \sim \hbar c_s^3 / (2\pi k_B \hbar \rho c_s^4) \sim 10^{-8} \, \text{K}$$

(for sound speed ~100 m/s in water). This is orders of magnitude smaller than real black hole Hawking temperatures but still **in principle detectable** with sensitive thermometry.

### Cosmological Horizons in Analogues

Just as particle horizons and event horizons appear in expanding universes (ΛCDM, de Sitter), they can appear in expanding media. For a fluid expanding with scale factor $a(t)$:

$$\text{metric} \sim -dt^2 + a(t)^2 d\mathbf{x}^2$$

(in the comoving frame), which is directly analogous to the Friedmann metric. Particle horizons—the maximum distance light can travel from the big bang—emerge naturally.

Conversely, if the "cosmological" expansion is in reverse (contraction), a **big crunch horizon** appears, beyond which no signal can reach an observer before the collapse ends.

### Novel Analog Systems (2024 additions in v4)

The 2024 review update includes:

**Holographic analogues**: AdS/CFT duality enables constructing gravitational systems dual to field theory systems. Quenches in the field theory correspond to time-dependent metrics in gravity, providing a new class of analogs.

**Metamaterials and photonic systems**: Engineered media (photonic crystals, metamaterials) can have effective metrics with exotic features: negative refractive index, superluminal group velocity, imaginary band gaps. These allow analog gravity in the electromagnetic domain, complementing fluid-based analogues.

**Topological defects as analogues**: Vortices, solitons, and other topological defects in condensed matter carry effective metrics in their cores. A vortex in a superfluid may have an internal geometry resembling spacetime around a spinning particle (conical singularity).

**Time-dependent metrics**: Most early analog gravity focused on static backgrounds. Modern experiments access time-dependent geometries (expanding cosmologies, dynamical black holes), requiring real-time tracking of metric evolution.

---

## Key Results and Scope

The review documents:

1. **Universality of effective metrics**: Across diverse physical systems (fluids, superfluids, Bose-Einstein condensates, optical media, photonic crystals), the same effective metric structure emerges. This universality suggests a deep principle.

2. **Hawking radiation signatures**: Multiple experiments (Weinfurtner et al. 2012, Muñoz de Nova et al. 2019, others) have detected phonon pair creation with thermal spectrum consistent with Hawking's prediction, within measurement uncertainties.

3. **Event horizon analogues**: Acoustic event horizons have been realized in superfluid helium-4 (Weinfurtner), water surface waves (Rousseaux), and fiber optics (Philbin, Watt). The characteristic signature—trapped modes and modified dispersion—matches theory.

4. **Cosmological horizon analogues**: De Sitter space analogs in expanding media show particle creation rates consistent with the Gibbons-Hawking temperature. No direct analog of cosmic inflation has been realized yet, but frameworks exist.

5. **Rotating spacetime analogues**: Recent work (Svančara 2024) demonstrates analog Kerr geometry in a rotating superfluid vortex, with ringdown signatures of quasinormal modes.

6. **Absence of fundamental limitations**: Analog gravity is **not** a crude approximation. The correspondence between acoustic wave equations and curved spacetime equations is **exact** in the linear limit (no nonlinear effects, weak backgrounds). This exactness is often overlooked.

---

## Impact and Legacy

Analog gravity has matured from a theoretical curiosity to an experimental programme with direct relevance to fundamental physics:

**Quantum field theory validation**: Hawking radiation and particle creation in curved spacetime are core predictions of QFT that have never been directly observed. Analog systems allow laboratory validation.

**Bridge between condensed matter and particle physics**: The realization that black hole thermodynamics and Hawking radiation emerge from condensed matter wave equations blurs the boundary between gravity and condensed matter. This suggests a deeper unity.

**Planck-scale physics**: Some analog systems exhibit modified dispersion (where wave speed depends on wavelength) similar to quantum gravity effects. This provides a testbed for understanding how quantum gravity might modify wave propagation.

**Technology transfer**: Non-reciprocal media, metamaterials, and topological photonics developed for analog gravity have applications in classical optics and information processing.

---

## Connection to Phonon-Exflation Framework

**Foundational paradigm**: The phonon-exflation framework is built on the analog gravity paradigm. The framework proposes that spacetime is emergent—arising from collective excitations (phonons) of an underlying quantum substrate (Cooper pair condensate in K-theory).

Analytically, this means:
- **Substrate**: K-theoretic condensed matter with SU(3) fiber geometry
- **Excitations**: Phonons (quantized sound modes of the condensate)
- **Effective metric**: Induced by the condensate flow and density profile
- **Observers**: We are resonances in the phonon field, observing spacetime as an effective metric

The Barceló-Liberati-Visser review validates that this is **not speculative**. Multiple experimental platforms (superfluids, atom clouds, photonic systems) demonstrate that effective spacetime metrics emerge naturally from condensed matter dynamics.

**Acoustic horizon as cosmological horizon**: In the draining bathtub analog, the acoustic event horizon marks a transition from "causally connected" to "causally trapped" regions. In the framework, the cosmological horizon (the boundary of the observable universe) is the analog of this acoustic event horizon, marking the regime where the phonon-condensate flow is supersonic relative to information propagation.

**Hawking temperature of the universe**: If the universe is a phonon field in a K-theoretic substrate, then cosmological particle creation (producing the observed baryon asymmetry, matter-radiation coupling, etc.) is the analog of Hawking radiation at a cosmological horizon. The Gibbs temperature of the early universe should match the effective "Hawking temperature" of the phonon condensate at that epoch:

$$T_\text{rad} \sim \frac{\hbar c_s^3}{2\pi k_B} \kappa_\text{cosmological}$$

where $c_s$ is the sound speed in the condensate (related to internal geometry) and $\kappa_\text{cosmological}$ is the surface gravity of the cosmological horizon.

**Spectral action as effective metric tensor**: The framework's spectral action generates the Einstein-Cartan equations describing geometry. In the analog gravity context, the spectral action is the **analogue of the equations governing wave propagation in a medium**. Just as acoustic waves induce an effective metric through their wave equation, the spectrum of the Dirac operator (acting on the internal space) induces an effective 4D spacetime metric through the spectral action.

This is a deep structural analogy, suggesting that gravity is universally emergent from spectral (spectroscopic) properties of quantum systems.

**Vortex-black hole analogy**: The Svančara et al. (Paper 21) giant quantum vortex is an analog of a black hole in superfluid. The framework predicts that the internal U(1)_7 pairing condensate should exhibit similar vortex-black hole structures during the fold transition. Observable signatures (quasinormal mode frequencies, ringdown waveforms) in future precision measurements should match the vortex analog's predictions.

**Cosmological quasinormal modes**: If the universe's metric is emergent from phonon dynamics, then the expansion rate should exhibit characteristic quasinormal mode oscillations, analogous to the Svančara vortex's ringdown. These oscillations would appear as small corrections to the smooth Friedmann expansion:

$$H(z) = H_0 [\Omega_m (1+z)^3 + \Omega_\Lambda] + \text{oscillations at MHz frequencies in the far past}$$

The framework predicts oscillation frequency determined by the internal K_7 pairing gap, and amplitude set by the efficiency of phonon-condensate coupling. Testing this prediction requires precision cosmology—the next generation of surveys (DESI, Vera Rubin, Einstein Telescope for GWs) will have the sensitivity.

The Barceló-Liberati-Visser 2024 review is a comprehensive validation that **emergent spacetime from condensed matter is no longer speculative**. It is an experimentally validated research program with a clear mathematical structure. The framework's only novel claim is that the condensed matter substrate is internal (K-theoretic) rather than external (laboratory), making it truly universal and applying it to fundamental cosmology.
