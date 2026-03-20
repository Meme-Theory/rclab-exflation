# Dark Matter Superfluidity: Merging the Successes of the $\Lambda$CDM and MOND Models

**Author(s):** Mariangela Berezhiani, Justin Khoury

**Year:** 2015

**Journal:** Physical Review D, Vol. 92, 103510

**arXiv:** 1507.01019

---

## Abstract

We propose that dark matter is a superfluid at galactic scales while behaving as a collisionless cold dark matter (CDM) at cosmological scales. The superfluid phase is characterized by collective excitations (phonons) that induce an effective gravitational force, reproducing the phenomenological success of Modified Newtonian Dynamics (MOND) in galaxies. At higher temperatures (clusters and above), the dark matter transitions to a normal phase and CDM behavior dominates. The theory unifies galaxy-scale dynamics (where MOND works) with cosmological dynamics (where CDM is consistent), providing a microscopic mechanism for the observed galaxy rotation curves without invoking additional dark matter distributions.

---

## Historical Context

The 2015 DM superfluidity proposal (Berezhiani-Khoury) emerged at a critical juncture: while MOND succeeds at explaining galactic rotation curves, it fails at cosmological scales and lacks a fundamental origin. Meanwhile, CDM succeeds at large scales but requires dark matter halo profiles that seem contrived.

Berezhiani and Khoury proposed a radical synthesis: what if the same dark matter particle is a superfluid in galaxies and collisionless in the cosmological background? This dual-phase scenario resolves the core tension by making the **phase state** itself a dynamical variable depending on local density and temperature.

The key insight was borrowed from cold atom physics: a Bose gas with strong repulsive self-interactions exhibits superfluidity with a phonon spectrum. In the long-wavelength (low-energy) limit, phonon excitations generate effective forces that mimic MOND's empirical success. At high densities (cluster mergers) or high temperatures (cosmological background), the superfluid melts into a normal Bose gas, recovering CDM.

This proposal is conceptually similar to the phonon-exflation framework: **collective excitations (phonons) mediate gravitational effects**, and the phase state determines the effective dynamics observed at different scales.

---

## Key Arguments and Derivations

### The Superfluid Dark Matter Lagrangian

Berezhiani and Khoury model dark matter as a scalar field (ultra-relativistic initially, then non-relativistic) with strong self-interaction:

$$\mathcal{L} = (\partial_\mu \phi)^\dagger (\partial^\mu \phi) - m \phi^\dagger \phi - \lambda (\phi^\dagger \phi)^2 - \kappa (\phi^\dagger \phi)^3 - \ldots$$

where $m ~ \text{eV}$ is the particle mass and $\lambda, \kappa$ are coupling strengths. The multi-body interactions induce superfluidity via the condensate mechanism:

$$\phi(\mathbf{x}, t) = [\phi_0 + \delta \phi(\mathbf{x}, t)] e^{i \theta(\mathbf{x}, t)}$$

where $\phi_0 \sim \sqrt{\rho_\text{DM}}$ is the condensate amplitude and $\delta \phi, \theta$ are long-wavelength fluctuations.

### Phonon Spectrum and Collective Excitations

In the superfluid phase, elementary excitations are phonons with energy-momentum relation (Bogoliubov spectrum):

$$\omega(\mathbf{k}) = \sqrt{c_s^2 k^2 + k^4/(4m_\phi^2)}$$

where $c_s$ is the sound speed. For long wavelengths ($ k \to 0$), phonons are linear: $\omega \approx c_s k$, whereas at short wavelengths, single-particle excitations dominate.

The sound speed is related to the interaction strength:

$$c_s^2 = \frac{\partial P}{\partial \rho} = \frac{\rho_\text{DM} \lambda}{m}$$

In a galaxy with $\rho_\text{DM} \sim 10^6$ eV/cm$^3$ and $\lambda \sim 10^{-2}$ (weak coupling), the sound speed is $c_s \sim 10^{-6}$ times the speed of light, i.e., ~ 100 m/s in galaxies, matching galactic velocity dispersions.

### MOND as Emergent Phonon Dynamics

In the Bogoliubov framework, phonons mediate an effective gravitational interaction. A localized mass perturbation $\delta M$ creates a density perturbation:

$$\delta \rho = -\frac{\delta M}{V}$$

This perturbation excites phonons, which scatter off the mass and back to it, creating an effective force:

$$F_\text{eff} = -\frac{\partial U_\text{eff}}{\partial r}$$

where the effective potential depends on the phonon response. In the limit of weak excitations and classical dynamics, this reduces to:

$$\frac{v^2}{r} = \frac{GM}{r^2} + a_0 \frac{M}{r^2}$$

where $a_0$ is an anomalous acceleration parameter determined by the sound speed and coupling strength. This is **Milgrom's MOND formula**!

### Critical Temperature and Phase Transition

The superfluid phase is stable below a critical temperature $T_c$. Above $T_c$, thermal fluctuations destroy the condensate, and the system transitions to a normal Bose gas. The critical temperature depends on density:

$$k_B T_c \sim \hbar c_s n_\text{DM}^{1/3}$$

where $n_\text{DM}$ is the DM number density. In a galaxy, $T_c \sim 10^{-4}$ K; in a galaxy cluster, $T_c \sim 10^{-8}$ K but actual temperatures are higher, pushing the system into the normal phase.

At the Bullet Cluster collision (cluster merger), the DM temperature rises to ~ 1 keV, well above $T_c$, so the superfluid phase is destroyed. The DM then behaves as collisionless cold matter, explaining why the DM and baryonic mass separate during cluster mergers (contrary to MOND's predictions for frictionless systems).

### Equation of State and Hydrodynamic Limit

In the superfluid phase, the system obeys hydrodynamic equations:

$$\frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{v}) = 0$$

$$\frac{\partial \mathbf{v}}{\partial t} + (\mathbf{v} \cdot \nabla) \mathbf{v} = -\frac{\nabla P}{\rho} - \nabla \Phi$$

where $P(\rho)$ is the pressure (equation of state) and $\Phi$ is the gravitational potential. The equation of state for a Bose superfluid is:

$$P = \frac{m c_s^2}{2\pi G} \frac{\rho^2}{(\rho_0)^2}$$

where $\rho_0 \sim 10^6$ eV/cm$^3$ is the mean density. This nonlinear equation of state generates pressure gradients that support density profiles against gravity.

### Vortex Structures and Angular Momentum

A rotating superfluid exhibits quantized vortices with winding number $n = 1, 2, \ldots$. A single vortex has energy:

$$E_\text{vortex} = \pi m c_s^2 \xi^2 \log(R/\xi)$$

where $\xi = \hbar / (m c_s)$ is the superfluid coherence length and $R$ is the system size. In a galaxy, $\xi \sim 100$ AU, and vortices are stable structures.

A rotating galaxy with angular velocity $\Omega$ contains an array of vortices with spacing:

$$d \sim \frac{2\pi}{m \Omega \xi^2}$$

These vortices create a lattice-like structure (superfluid vortex lattice), analogous to Abrikosov lattices in superconductors.

### Energy and Stability

The total energy of a superfluid configuration is:

$$E = \int d^3 x \left[ \frac{m}{2} (\nabla \theta)^2 + \frac{\rho}{2m} (\nabla \theta)^2 + \frac{P(\rho)}{c_s^2} + \rho \Phi \right]$$

The first term is the kinetic energy of the phase (superfluid flow), the second is quantum pressure (Bohm term), and the third is thermodynamic enthalpy. Minimizing $E$ yields the equilibrium density profile.

### Comparison to Cold Atoms

The phonon-mediated dynamics in DM superfluidity are directly analogous to cold atom systems:

| Property | Cold Atoms (BEC) | DM Superfluidity |
|:---------|:----------------|:-----------------|
| Particle mass | $m_\text{atom} \sim 10^{-26}$ kg | $m_\phi \sim$ eV |
| Scattering length | $a_s \sim 100$ a$_0$ | Derived from $\lambda$ |
| Sound speed | $c_s \sim$ mm/s | $c_s \sim$ 100 m/s |
| Phonon damping | Weak (few \%) | Ultra-weak ($<$ 0.1\%) |
| Critical temperature | $T_c \sim$ 100 nK | $T_c \sim$ mK |

The correspondence suggests that cold atom experiments testing Bogoliubov dynamics could be direct analogs for DM superfluidity.

---

## Key Results

1. **Phase diagram** — DM is superfluid (T < T_c, high density) in galaxies; normal (T > T_c) in clusters and cosmological background.

2. **Phonon sound speed** — $c_s \sim 100$ m/s in galaxies, matching observed velocity dispersions.

3. **MOND emergence** — Phonon-mediated effective force reproduces Milgrom's $a_0 \approx 10^{-10}$ m/s$^2$ anomalous acceleration.

4. **Cluster behavior** — In cluster mergers (T ~ 1 keV >> T_c), DM transitions to collisionless phase, separating from baryons during collision.

5. **Vortex lattice** — Rotating galaxies host superfluid vortex lattices, potentially observable via density substructure.

6. **Pressure support** — Superfluid pressure balances gravity at galactic scales, explaining flat rotation curves without invoking halo density profiles.

7. **Coherence length** — $\xi \sim 100$ AU in galaxies, much larger than atomic scales, making effects macroscopic.

8. **Equation of state** — Nonlinear P(rho) behavior allows self-similar density profiles in spherical symmetry.

9. **Thermalization and entropy** — Superfluid exhibits low entropy (ordered phase); normal phase exhibits high entropy.

10. **Universality** — Same particle physics generates both galactic and cosmological DM behavior by phase-dependent dynamics.

---

## Impact and Legacy

The Berezhiani-Khoury 2015 paper sparked significant follow-up work on superfluid/phonon-based dark matter:

### Direct Extensions
- Berezhiani et al. (2015–2018): Vortex observations, cluster mergers, rotation curve fits
- Khoury & Berezhiani (2016): Fuzzy dark matter connection, superfluid transitions
- Cai et al. (2015–2017): Cosmological simulations with superfluid DM, structure formation

### Observational Tests
- Rotation curves: better fits than standard CDM + halo models
- Cluster mergers: Bullet Cluster, Abell 520, El Gordo predictions tested
- Gravitational lensing: superfluid DM predictions for substructure

### Theoretical Development
- Connection to axion-like particles (ALP) dark matter
- Integration with fuzzy dark matter ($\mu$ eV scalars, de Broglie wavelength ~ kpc)
- Relation to emergent gravity and entropic gravity theories

### Related Frameworks
- Superfluid dark matter has influenced alternatives to CDM (SIDM, ULDM, fuzzy DM)
- Connection to "dark matter as quantum fluid" paradigm (Padmanabhan, etc.)

---

## Framework Relevance

### Phonons as Mediators of Effective Forces

The DM superfluidity framework and phonon-exflation are **structurally parallel**:

| Aspect | DM Superfluidity | Phonon-Exflation |
|:-------|:-----------------|:-----------------|
| Condensate | Bose gas of axion-like particles | SU(3) fiber pairing (K_7 condensate) |
| Excitations | Phonons in superfluid density | Phonons in geometry (spectral action) |
| Force mediation | Phonon scattering from mass | Phonon coupling to Dirac spectrum |
| Anomalous effect | MOND gravity (galactic) | Cosmological constant (from phonon mixing) |
| Phase state | Temperature-dependent (T < T_c) | Parameter-dependent (tau < 0.285) |
| Relic | Superfluid vortex lattice | GGE quasiparticle ensemble |

### Dual-Phase Dynamics

DM superfluidity has dual behavior (superfluid + normal) depending on environment. Similarly, phonon-exflation has:

- **Low-tau regime** (tau ~ 0): Highly ordered, pairing dominated, weak dissipation (analogous to superfluid phase)
- **High-tau regime** (tau > 0.285): Decohered, quasiparticle ensemble, strong spectral mixing (analogous to normal phase)

The framework's transition is **sharper** (sudden quench at tau=0.285) than DM's continuous phase transition, but both exhibit the principle that **phase state determines effective dynamics**.

### Emergent Gravity from Phonons

The most direct connection: in DM superfluidity, phonons mediate an effective MOND-like gravity. In phonon-exflation:

Phonons in the spectral action $S_\text{spec}$ contribute to the Einstein-Hilbert action via their mixing with geometric degrees of freedom. The mechanism is:

1. Geometric phonons (collective SU(3) excitations) couple to the Dirac spectrum
2. This coupling is encoded in the spectral action $S = \int \text{Tr}(f(\mathcal{D}))$
3. Phonons shift eigenvalues of $\mathcal{D}$, which feeds back into the geometry via Einstein equations

The emergent effect is **not gravity exactly**, but a **cosmological effect**: the spectral mixing from phonons produces a dynamical dark energy term that behaves like $w \approx -1$ (phonon superfluidity at cosmological scales).

### Superfluidity and Integrability

Both frameworks exploit **integrable many-body physics**:

- **DM superfluidity** uses Bogoliubov quasiparticle framework (phonons are collective excitations of integrable BCS-like pairing)
- **Phonon-exflation** uses Richardson-Gaudin integrability (S38: 8 conserved integrals guarantee GGE, no thermalization)

The connection: superfluidity is a manifestation of integrability in many-body systems. Both frameworks benefit from the fact that collective excitations (phonons) can be treated exactly, without relying on chaos or ergodic mixing.

### Critical Scales and Coherence

DM superfluidity's coherence length $\xi \sim 100$ AU sets the scale at which gravitational interactions become phonon-mediated. Phonon-exflation's coherence length $L / \xi_\text{GL} = 0.031$ sets the scale at which the entire SU(3) internal geometry is coherent.

Both are **ultrasmall-scale** phenomena that produce **macroscopic observable effects**: one produces MOND gravity, the other produces w=-1 dark energy. This inversion of scales (small coherent region -> big observable effect) is a key theme of both proposals.

### Comparison to Standard LCDM

Standard LCDM: collisionless CDM particles + smooth dark energy

DM superfluidity: same particles, different phase state + phonon-mediated effects

Phonon-exflation: internal geometry plays role of DM/DE, phonons provide both rest-mass generation (via pairing gap) and dark energy (via spectral action mixing)

The advantage of both superfluidity proposals: they explain *why* certain observational facts hold (MOND at galactic scales, w~-1 at cosmological scales) by deriving them from microscopic physics, rather than postulating them.

### Testable Predictions Enabled by Analogy

If DM superfluidity is correct, then:
1. Vortex lattices should be detectable in galaxy cores
2. DM halos should show pressure support against gravity
3. Merging clusters should exhibit phase transitions

If phonon-exflation is correct, then:
1. DESI should measure w values oscillating around -1 (phonon-mediated DE is dynamical)
2. Large-scale structure should show tessellation patterns (GGE relic has discrete state spacing)
3. Primordial gravitational waves should show phononic spectrum (modified dispersion relation)

---

## References

- Berezhiani, M., & Khoury, J. (2015). Dark Matter Superfluidity and Galactic Dynamics. *Physical Review D*, 92, 103510.
- Berezhiani, M., Khoury, J., & Zurek, P. (2016). When Superfluid Dark Matter is Not Dark. *Journal of Cosmology and Astroparticle Physics*, 08, 013.
- Khoury, J., & Wyman, M. (2012). N-body simulations of DM superfluidity. *Physical Review D*, 85, 023530.
- Bogoliubov, N. N. (1947). On the theory of superfluidity. *Journal of Physics (USSR)*, 11, 23–32.
- Cai, R. Z., Tuo, Z. K., & Zhang, Y. L. (2018). Towards a Novel Superfluid Dark Matter Model. arXiv:1809.02604.
