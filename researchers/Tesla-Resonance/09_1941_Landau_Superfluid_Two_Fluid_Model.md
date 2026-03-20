# Superfluid Helium-4: Landau's Two-Fluid Model and Phonon Excitations (1941)

**Author:** Lev Davidovich Landau
**Year:** 1941 (first papers); 1947 (comprehensive treatment)
**Source:** Landau, L.D. (1941) "Theory of Superfluidity of Helium II." Journal of Physics (USSR) 5: 71-90; Landau & Lifshitz (1980) "Statistical Physics" (Part 1)

---

## Abstract

In 1941, Lev Landau proposed a revolutionary model of superfluid helium-4 (He-II), explaining how a single liquid can exhibit two distinct fluid components simultaneously: a normal fluid (with viscosity and entropy) and a superfluid (zero viscosity, zero entropy). The key insight was that superfluid He-II is not a static state but a dynamic system of quantized excitations (phonons, rotons, and vortices). The superfluid is the ground state; excitations are phonons (acoustic quanta) and rotons (rotation-like excitations). Landau's two-fluid hydrodynamics provided the first microscopic theory of superfluidity and revealed that superfluids are fundamentally phononic systems—oscillations in the ground-state medium.

---

## Historical Context

Superfluid helium was discovered experimentally in 1938 by Kapitza and Allen. The phenomenon was extraordinary: below a critical temperature (2.17 K), liquid helium-4 loses all measurable viscosity. A rotating cylinder of He-II maintains rotation indefinitely. Thin capillaries are filled by He-II against gravity.

The physical mechanism was mysterious. Traditional physics predicted viscosity from atomic collisions—how could collisions vanish? Some proposed superfluidity was a phase transition to a new state of matter entirely.

Landau's 1941 paper revolutionized understanding. He proposed that superfluidity arises from the quantum ground state, which supports quantized excitations (phonons). The superfluid component is the ground state itself; the normal component is the ensemble of thermally excited phonons.

This was a stunning conceptual shift: a "fluid" is not a collection of particles but a vibrational medium. The "particles" we experience (as heat, viscosity, entropy) are quantized excitations—phonons.

---

## Two-Fluid Hydrodynamics

### Experimental Observations Explained

He-II exhibits paradoxical properties:

1. **Viscosity**: He-II flows without viscosity through narrow channels
2. **Entropy**: At $T > 0$, He-II has thermodynamic entropy, implying excited states
3. **Heat transport**: He-II conducts heat anomalously (faster than diffusion)
4. **Vortices**: Rotating He-II can form quantized vortex rings

Landau's two-fluid model explains all of these.

### The Two-Fluid Picture

He-II consists of two interpenetrating fluids:

1. **Superfluid component**: At $T = 0$, all atoms are in the ground state (Bose-Einstein condensate). This component has zero viscosity, zero entropy, and flows without resistance.

2. **Normal component**: At $T > 0$, some atoms are excited into phonon states. These excited atoms act as a normal fluid with finite viscosity and entropy.

The densities are:

$$\rho = \rho_s + \rho_n$$

(total density = superfluid + normal densities)

At $T = 0$: $\rho_n = 0$, $\rho_s = \rho$ (pure superfluid)
At $T = T_c$: $\rho_s = 0$, $\rho_n = \rho$ (pure normal fluid)

The densities vary with temperature:

$$\rho_s(T) = \rho \left(1 - (T/T_c)^{\alpha}\right)$$

(approximately, for various values of $\alpha$ near the lambda point)

### Two-Fluid Equations of Motion

For a superfluid, Landau derived equations of motion:

$$\rho_s \frac{\partial \vec{v}_s}{\partial t} + \rho_n \frac{\partial \vec{v}_n}{\partial t} = -\nabla p$$

$$\rho_s (\vec{v}_s - \vec{v}_n) \times \vec{\omega} = \text{(momentum balance for counterflow)}$$

where $\vec{v}_s$ and $\vec{v}_n$ are superfluid and normal fluid velocities, and $p$ is pressure.

Crucially, the two fluids can move relative to each other—superfluid and normal fluid can have different velocities. This counterflow is the key to understanding heat transport and viscosity.

### Entropy and Heat Transport

Entropy is associated only with the normal component (excited atoms):

$$S = S_n = \text{constant} \times (T / T_c)^{\alpha}$$

(at low temperatures)

Heat transport is by normal fluid motion:

$$\vec{q} = \rho_s T \frac{\partial \vec{v}_n}{\partial t}$$

The thermal conductivity diverges at the lambda point, explaining He-II's anomalous heat transport.

---

## Excitation Spectrum: Phonons and Rotons

### Phonon Dispersion

Landau proposed that He-II excitations are phonons (acoustic waves) at low energy:

$$\epsilon(p) = c |p|$$

(linear dispersion, like sound in a normal liquid)

where $p$ is momentum and $c \approx 240$ m/s is the sound velocity in He-II.

### Roton Minimum

Experimental measurements (by Bijl, Feynman, and Cohen) revealed a surprise: the excitation spectrum is NOT simply linear. At higher momenta ($p > p_0 \approx 2\hbar/\lambda$, where $\lambda$ is the inter-atom spacing), the spectrum has a minimum:

$$\epsilon(p) = \Delta + \frac{(p - p_0)^2}{2\mu_r}$$

where $\Delta$ is the "roton gap" (~8.6 K or 0.86 meV) and $\mu_r$ is an effective roton mass (~0.17 $m_{\text{He}}$).

The roton minimum is a striking feature: excitations have a minimum energy, not at $p = 0$ (phonons), but at $p = p_0$. This means creating excitations requires overcoming an energy barrier, explaining He-II's extraordinary stability.

### Feynman's Quantum Hydrodynamics

Richard Feynman developed a deeper theory, showing that rotons can be understood as collective excitations—clusters of atoms oscillating against each other. A roton is not a single-particle excitation but a correlated, many-body mode.

Feynman also introduced the concept of vortex rings: circular vortices in the superfluid, each carrying quantized circulation $h/m_{\text{He}}$. Vortex rings are another type of excitation, with energy ~1 K.

---

## Heat Capacity and Thermal Properties

### Heat Capacity from Phonon Gas

The heat capacity of He-II is determined by the density of phonon states. For a 3D phonon gas:

$$g(\epsilon) \propto \epsilon^2$$

The total energy is:

$$U = \int_0^\infty \epsilon g(\epsilon) \frac{1}{e^{\epsilon/k_B T} - 1} d\epsilon$$

At low temperatures, this gives:

$$C_V \propto T^3$$

(Debye's $T^3$ law, same as solids!)

This is in remarkable agreement with He-II measurements. The superfluid is phononic—its heat capacity is that of a phonon gas.

### Specific Heat Jump at Lambda Point

At the lambda point ($T_c = 2.17$ K), the specific heat has a characteristic shape: a discontinuity or sharp peak. The "lambda point" gets its name from the shape of the $C_V$ vs $T$ curve, which resembles the Greek letter lambda.

Landau's theory naturally explains this: as $T$ approaches $T_c$ from below, the normal fluid density increases, and excitation modes become accessible. At $T = T_c$, all phonon states become thermally populated—a phase transition.

---

## Quantized Vortices and Circulation

### Quantum Circulation Condition

In a superfluid, the circulation around a vortex is quantized:

$$\oint \vec{v}_s \cdot d\vec{l} = \frac{nh}{m} \quad (n = 0, \pm 1, \pm 2, ...)$$

where $m$ is the mass of a He-4 atom and $h$ is Planck's constant.

Each quantum of circulation corresponds to a vortex. The superfluid cannot sustain arbitrary circulation; only quantized values are allowed. This is a purely quantum effect, arising from the coherence of the ground state (Bose-Einstein condensate).

### Vortex Ring Dynamics

A vortex ring (a circular loop of circulation) in He-II moves with velocity:

$$\vec{v}_{\text{ring}} = \frac{\hbar}{2m a} \ln\left(\frac{8R}{\xi}\right) \hat{z}$$

where $R$ is the ring radius, $\xi$ is the coherence length (core radius of the vortex), and $a$ is the inter-atomic spacing.

Vortex rings are excitations—they carry energy and momentum. Their dynamics are rich: rings can interact, merge, annihilate, and decay into phonons.

---

## Connection to Phonon-Exflation Framework

Landau's superfluid theory provides the deepest model for the phonon-exflation framework:

1. **Superfluid as ground state**: He-II is a Bose-Einstein condensate—all atoms in the ground state at $T = 0$. Phonon-exflation proposes that the universe itself is in a ground state: M4 x SU(3) acts as a "superfluid" at cosmological scales. The vacuum is the condensed phase; particles (phonons, fermions) are excitations above it.

2. **Phonons as particles**: In He-II, what we call "particles" (in thermodynamics and transport) are actually phonon excitations—quantized vibrations of the condensate. In phonon-exflation, elementary particles (electrons, quarks, photons, etc.) are phonons in the SU(3) geometry. The electron is a 1-phonon excitation of the M4 x SU(3) medium; the photon is another branch of the phonon spectrum.

3. **Two-component hydrodynamics**: He-II's two-fluid behavior (superfluid + normal) is a signature of excitations above a ground state. In cosmology, we observe a universe with both radiation (massless modes, behaving like an ideal gas) and matter (massive particles, moving slower). This is precisely the two-fluid structure: superfluid (vacuum, the coherent ground state) and normal fluid (excitations, thermally populated at early times).

4. **Heat capacity and entropy**: He-II's heat capacity scales as $T^3$ (phonon gas), matching the radiation-era universe. As the universe expands and cools, the thermal population of phonons decreases, and entropy decreases relative to energy. This is not a violation of thermodynamics but a consequence of adiabatic expansion—exactly as observed cosmologically (entropy per baryon is nearly constant).

5. **Quantized circulation and gauge fields**: Vortices in He-II carry quantized circulation. In the Standard Model, gauge fields (photon, gluons) have quantized topological properties (charge quantization, flux quantization). A vortex in a superfluid is topologically analogous to a monopole in a gauge field—a pointlike singularity carrying topological charge. In phonon-exflation, gauge bosons (photon, W, Z, gluons) might be vortex-like excitations of the SU(3) geometry.

6. **Roton minimum and particle mass**: The roton minimum in the He-II spectrum is striking: the lowest-energy excitations are at finite momentum, not at $p = 0$. This is like particles having minimum mass even when created with $p = 0$—rest mass. In fact, the roton minimum is a classic example of how the ground-state structure (the superfluid order parameter) creates an energy gap. In phonon-exflation, particle masses are analogous to roton gaps: they arise from the geometric structure of SU(3), which creates energy minima in the phonon spectrum at non-zero frequencies.

7. **Soundwave vs normal fluid**: In He-II, sound waves (phonons) propagate through the superfluid medium. In phonon-exflation, gravitational waves and other excitations propagate through the M4 x SU(3) medium. The speed of sound (first and second sound in He-II) is analogous to the speed of light—both are fundamental wave speeds in their respective media.

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Two-fluid density | $\rho = \rho_s + \rho_n$ | Superfluid + normal components |
| Superfluid fraction | $\rho_s(T) = \rho(1 - (T/T_c)^\alpha)$ | Temperature dependence of superfluid density |
| Phonon dispersion | $\epsilon(p) = c \|p\|$ | Linear acoustic excitation |
| Roton spectrum | $\epsilon(p) = \Delta + (p-p_0)^2/(2\mu_r)$ | Minimum-energy excitation at finite $p$ |
| Heat capacity (phonon) | $C_V = \frac{12\pi^4 N k_B}{5}(T/\theta_D)^3$ | Debye law (phonon gas) |
| Quantized circulation | $\oint \vec{v}_s \cdot d\vec{l} = \frac{nh}{m}$ | Circulation around vortex is quantized |
| Vortex ring velocity | $v_{\text{ring}} = \frac{\hbar}{2ma} \ln(8R/\xi)$ | Velocity of quantized vortex loop |
| Entropy (low T) | $S \propto T^3$ | From phonon gas entropy |

---

## Critical Assessment

**What holds up**:
- Two-fluid model explains all macroscopic properties of He-II accurately
- Phonon picture correctly predicts heat capacity, thermal conductivity
- Quantized vortices are observed and behave as predicted
- Temperature dependence of superfluid fraction matches experiments

**What was refined**:
- Roton minimum was not originally in Landau's theory; discovered experimentally and explained by Feynman
- Detailed structure of the roton (single-particle vs collective excitation) required deeper analysis
- Interaction effects (phonon-phonon scattering, thermal conductivity) need higher-order corrections

**Ahead of its time**:
- Recognition that a macroscopic fluid is fundamentally a system of excitations
- Insight that ground state and excited states are continuous (no particle-like boundary)
- Understanding that quantum effects (quantized vortices, Bose-Einstein condensation) can have macroscopic consequences

---

## Legacy and Modern Significance

Landau's theory of superfluidity is foundational to:

1. **Condensed-matter physics**: Model for all quantum phase transitions and excitation spectra
2. **Quantum field theory**: The vacuum in QFT is understood as a condensate, with particles as excitations (similar to He-II)
3. **Cosmology**: The cosmic microwave background and early universe thermodynamics follow similar principles
4. **Analog gravity**: Superfluids are used as experimental platforms to study black holes, Hawking radiation, and other gravitational phenomena

---

## References

1. Landau, L.D. (1941). "Theory of superfluidity of helium II." Journal of Physics (USSR) 5: 71-90.
2. Landau, L.D. & Lifshitz, E.M. (1980). "Statistical physics." Part 1, 3rd edn. Pergamon Press.
3. Feynman, R.P. (1955). "Application of quantum mechanics to liquid helium." Progress in Low Temperature Physics 1: 17-53.
4. Pines, D. & Nozieres, P. (1966). "The theory of quantum liquids." Benjamin, New York.
5. Donnelly, R.J. (1991). "Quantized vortices in helium II." Cambridge University Press.
6. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press.
