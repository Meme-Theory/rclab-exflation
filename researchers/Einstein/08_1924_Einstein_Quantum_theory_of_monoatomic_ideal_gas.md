# Quantum Theory of the Monoatomic Ideal Gas

**Author:** Albert Einstein
**Year:** 1924--1925
**Journal:** *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 261--267 (1924); 3--14 (1925)

---

## Abstract

In a series of papers in 1924--1925, Einstein extends Satyendra Nath Bose's revolutionary counting method for photon statistics to massive particles, creating what is now called Bose-Einstein statistics. By treating identical particles as genuinely indistinguishable -- counting only the number of particles in each quantum state, not which particle is in which state -- Einstein derives a new equation of state for an ideal gas of massive bosons. He discovers that below a critical temperature, the gas undergoes a phase transition: a macroscopic fraction of particles condenses into the ground state. This Bose-Einstein condensation (BEC) was experimentally realized seventy years later (Cornell, Wieman, and Ketterle, 1995) and represents the first prediction of a purely quantum-mechanical phase transition in a system of non-interacting particles.

---

## Historical Context

### Bose's Letter and Paper (1924)

In June 1924, Satyendra Nath Bose, a young Indian physicist, sent Einstein a short paper in which he derived Planck's blackbody radiation formula using a novel statistical method. Rather than treating photons as distinguishable particles and applying Boltzmann statistics (which gives the incorrect Rayleigh-Jeans law), Bose counted the number of ways to distribute indistinguishable photons among phase-space cells of volume $h^3$.

Bose's key insight: the correct counting is not "which photon is in which cell" but "how many photons are in each cell." This treats photons as fundamentally indistinguishable entities, eliminating the Boltzmann overcounting factor.

Einstein immediately recognized the profound implications. He translated Bose's paper into German and arranged its publication in *Zeitschrift fur Physik*. He then applied Bose's method to massive particles -- something Bose had not done.

### The Old Quantum Theory

By 1924, quantum mechanics as we know it did not yet exist (the Schrodinger equation came in 1926, matrix mechanics in 1925). The "old quantum theory" consisted of Bohr-Sommerfeld quantization rules applied to classical orbits, plus Einstein's own light-quantum hypothesis and various semi-classical results. The statistical mechanics of quantum systems was largely unexplored.

The key question was: does the new counting method apply only to photons (which are massless and have no conservation law for particle number) or also to massive particles (which are conserved)? Einstein argued for the latter.

### The Puzzle of Identical Particles

Classical statistical mechanics treats particles as distinguishable in principle -- even if they are physically identical, one imagines labeling them (particle #1, particle #2, etc.) and counting permutations. Gibbs had already recognized that this overcounting by $N!$ led to the Gibbs paradox (the entropy of mixing for identical gases should be zero), and corrected it ad hoc by dividing by $N!$.

Bose's method went further: not merely dividing by $N!$ but changing the counting entirely. The question was whether this was a mathematical trick for photons or a fundamental feature of quantum mechanics.

---

## Key Arguments and Derivations

### I. Bose's Counting for Photons (Recap)

Consider photons distributed among $Z_s$ cells (quantum states) with energy $\epsilon_s$. If there are $N_s$ photons in this energy level, the number of distinct arrangements of $N_s$ indistinguishable photons in $Z_s$ cells is:

$$W_s = \binom{N_s + Z_s - 1}{N_s} = \frac{(N_s + Z_s - 1)!}{N_s!(Z_s - 1)!}$$

This is the "stars and bars" combinatorial formula for distributing indistinguishable objects into distinguishable boxes. The total number of microstates is $W = \prod_s W_s$.

Using Stirling's approximation and maximizing $\ln W$ subject to the constraint of fixed total energy (but NOT fixed total photon number, since photons can be created and destroyed):

$$\bar{n}_s = \frac{1}{e^{\epsilon_s/k_BT} - 1}$$

This is the Bose-Einstein distribution for photons ($\mu = 0$, where $\mu$ is the chemical potential). Combined with the photon density of states $g(\epsilon) = 8\pi\epsilon^2/(h^3c^3)$, it gives Planck's law exactly.

### II. Extension to Massive Particles

Einstein applies the same counting to a gas of $N$ identical massive particles with single-particle energy:

$$\epsilon = \frac{p^2}{2m}$$

The crucial difference from photons: the total particle number $N$ is conserved. This introduces an additional constraint, handled by a Lagrange multiplier that becomes the chemical potential $\mu$ (or equivalently, the fugacity $z = e^{\mu/k_BT}$).

The density of states for massive particles in volume $V$ is:

$$g(\epsilon)\,d\epsilon = \frac{2\pi V (2m)^{3/2}}{h^3}\epsilon^{1/2}\,d\epsilon$$

The average occupation of a state with energy $\epsilon$ is:

$$\bar{n}(\epsilon) = \frac{1}{z^{-1}e^{\epsilon/k_BT} - 1}$$

where $z = e^{\mu/k_BT} \leq 1$ (since $\bar{n}$ must be non-negative, requiring $z \leq e^{\epsilon/k_BT}$ for all $\epsilon$; for the ground state $\epsilon = 0$, this gives $z \leq 1$).

The total particle number and energy are:

$$N = \sum_{\text{states}} \bar{n}(\epsilon) \approx \frac{2\pi V(2m)^{3/2}}{h^3}\int_0^\infty \frac{\epsilon^{1/2}\,d\epsilon}{z^{-1}e^{\epsilon/k_BT} - 1}$$

$$E = \frac{2\pi V(2m)^{3/2}}{h^3}\int_0^\infty \frac{\epsilon^{3/2}\,d\epsilon}{z^{-1}e^{\epsilon/k_BT} - 1}$$

### III. The Bose-Einstein Integrals

Defining the thermal de Broglie wavelength:

$$\lambda_{dB} = \frac{h}{\sqrt{2\pi mk_BT}}$$

the particle number equation becomes:

$$\frac{N}{V} = \frac{1}{\lambda_{dB}^3}g_{3/2}(z)$$

where:

$$g_n(z) = \frac{1}{\Gamma(n)}\int_0^\infty \frac{x^{n-1}\,dx}{z^{-1}e^x - 1} = \sum_{k=1}^{\infty}\frac{z^k}{k^n}$$

is the polylogarithm (Bose function). The series converges for $z \leq 1$.

The maximum value of $g_{3/2}(z)$ occurs at $z = 1$:

$$g_{3/2}(1) = \zeta(3/2) \approx 2.612$$

where $\zeta$ is the Riemann zeta function.

### IV. Bose-Einstein Condensation

The particle number equation:

$$\frac{N}{V} = \frac{g_{3/2}(z)}{\lambda_{dB}^3}$$

can accommodate the given density $N/V$ only if $g_{3/2}(z)$ is large enough. Since $g_{3/2}(z) \leq \zeta(3/2) \approx 2.612$, there is a maximum density that the integral can describe:

$$n_{max}(T) = \frac{\zeta(3/2)}{\lambda_{dB}^3} = \zeta(3/2)\left(\frac{2\pi mk_BT}{h^2}\right)^{3/2}$$

Equivalently, for a given density $n = N/V$, there is a critical temperature:

$$T_c = \frac{h^2}{2\pi mk_B}\left(\frac{n}{\zeta(3/2)}\right)^{2/3}$$

**Below $T_c$, the integral cannot account for all $N$ particles.** The "missing" particles must be in the ground state ($\epsilon = 0$), which contributes zero to the integral (since the density of states vanishes at $\epsilon = 0$). Einstein concludes that a macroscopic number of particles accumulates in the single-particle ground state:

$$N_0 = N\left[1 - \left(\frac{T}{T_c}\right)^{3/2}\right] \qquad \text{for } T < T_c$$

This is **Bose-Einstein condensation** -- a phase transition driven purely by quantum statistics, requiring no interactions.

### V. Equation of State

The pressure of the Bose gas is:

$$P = \frac{k_BT}{\lambda_{dB}^3}g_{5/2}(z)$$

For $T > T_c$: $z < 1$ is determined by the density equation, and the equation of state smoothly interpolates between classical ($z \ll 1$: $PV = Nk_BT$) and quantum behavior.

For $T < T_c$: $z = 1$ and:

$$P = \frac{k_BT}{\lambda_{dB}^3}\zeta(5/2)$$

The pressure depends only on temperature, not on density -- analogous to the vapor pressure of a liquid-gas coexistence. The condensate (ground-state particles) contributes zero pressure.

### VI. Einstein's Analogy to Light Quanta

Einstein explicitly draws the parallel between the condensation phenomenon and his earlier work on light quanta and the photoelectric effect. He notes that the new statistics imply a fundamental indistinguishability of identical particles that goes beyond classical physics. He also connects the work to de Broglie's hypothesis (1923) of matter waves: particles with wavelength $\lambda = h/p$ exhibit wave-like behavior, and the condensation occurs when the thermal de Broglie wavelength becomes comparable to the interparticle spacing.

---

## Physical Interpretation

### Quantum Degeneracy

BEC occurs when the interparticle spacing $n^{-1/3}$ becomes comparable to the thermal de Broglie wavelength $\lambda_{dB}$. At this point, the quantum-mechanical wave packets of individual particles overlap significantly, and the indistinguishability of identical particles becomes physically manifest. The classical notion of particles as distinguishable objects breaks down.

### A Phase Transition Without Interactions

BEC is remarkable because it is a phase transition in a non-interacting system. All other known phase transitions (liquid-gas, ferromagnetism, superconductivity) require interactions. BEC is driven purely by quantum statistics -- the tendency of bosons to "bunch" into the same quantum state. The condensate is a macroscopic quantum state: a single quantum-mechanical wave function $\psi(\mathbf{r})$ describes a macroscopic number of particles.

### Connection to Superfluidity

Einstein speculated that BEC might be related to the unusual properties of liquid helium at low temperatures (the lambda transition at 2.17 K). Fritz London (1938) developed this connection, arguing that the superfluid phase of helium-4 is a form of BEC, modified by the strong interatomic interactions. This identification, while approximate (the condensate fraction in superfluid He-4 is only about 8%, compared to 100% for the ideal gas), is now the standard understanding.

---

## Impact and Legacy

### Initial Skepticism

The prediction was met with considerable skepticism. Many physicists, including Einstein himself at times, were uncertain whether the condensation was a genuine physical effect or an artifact of the approximations (particularly the treatment of the ground state). The fact that the prediction involved an ideal gas -- while real gases liquefy before reaching $T_c$ -- made it seem academic.

### Experimental Realization (1995)

BEC was finally achieved experimentally in dilute atomic gases by three groups in 1995:
- **Eric Cornell and Carl Wieman** (JILA, Boulder): rubidium-87 atoms cooled to $\sim 170$ nK.
- **Wolfgang Ketterle** (MIT): sodium-23 atoms.

The key enabling technologies were laser cooling (Chu, Cohen-Tannoudji, Phillips; Nobel 1997) and evaporative cooling in magnetic traps. Cornell, Wieman, and Ketterle received the 2001 Nobel Prize.

The observed condensates matched Einstein's predictions quantitatively: the condensate fraction scales as $1 - (T/T_c)^{3/2}$, and the critical temperature is given by the ideal-gas formula with corrections for finite size and interactions.

### Superfluid Helium

London's application of BEC to superfluid He-4 (1938) opened the field of quantum fluids. Landau's phenomenological theory (1941), the Bogoliubov theory of the weakly interacting Bose gas (1947), and the Gross-Pitaevskii equation (1961) all build on Einstein's foundation.

---

## Connections to Modern Physics

### The Gross-Pitaevskii Equation

For a weakly interacting BEC, the condensate wave function $\Psi(\mathbf{r}, t)$ satisfies:

$$i\hbar\frac{\partial\Psi}{\partial t} = \left(-\frac{\hbar^2}{2m}\nabla^2 + V_{ext} + g|\Psi|^2\right)\Psi$$

where $g = 4\pi\hbar^2 a_s/m$ and $a_s$ is the s-wave scattering length. This nonlinear Schrodinger equation (GPE) describes vortices, solitons, and collective excitations of the condensate. The phononic excitation spectrum at long wavelengths follows the Bogoliubov dispersion:

$$E(k) = \sqrt{\frac{\hbar^2k^2}{2m}\left(\frac{\hbar^2k^2}{2m} + 2gn\right)}$$

which is linear (acoustic) at small $k$: $E \approx \hbar c_s k$ with $c_s = \sqrt{gn/m}$.

### Analog Cosmology

BEC systems with tunable interactions and time-dependent traps provide laboratory analogs for cosmological phenomena. Expanding BEC clouds mimic aspects of cosmic expansion; phonons in the condensate propagate on an effective metric determined by the condensate density and velocity. Vortex-antivortex pairs produced by rapid quenches (the Kibble-Zurek mechanism) are analogs of cosmic string formation. The nucleosynthesis of "atomic" bound states from vortex pairs in expanding condensates provides a testing ground for mechanisms of primordial element formation in alternative cosmological frameworks.

### Ultracold Atoms as Quantum Simulators

Modern BEC experiments serve as quantum simulators for condensed matter and high-energy physics. Optical lattices loaded with ultracold atoms realize the Bose-Hubbard model, allowing direct observation of the superfluid-to-Mott insulator quantum phase transition. Multi-component BECs (spinor condensates) exhibit rich topological defect structures (skyrmions, monopoles, knots) with connections to gauge field theory.

### Fermions and the Pauli Principle

Einstein's work on bosonic statistics was complemented by Fermi (1926) and Dirac (1926), who developed the statistics of indistinguishable particles with half-integer spin (fermions). The Pauli exclusion principle -- no two fermions can occupy the same quantum state -- leads to the Fermi-Dirac distribution:

$$\bar{n}(\epsilon) = \frac{1}{e^{(\epsilon - \mu)/k_BT} + 1}$$

The distinction between bosons ($-1$ sign in denominator) and fermions ($+1$ sign) has no classical analog and is one of the foundational features of quantum mechanics. The spin-statistics theorem (Pauli, 1940) connects this to the transformation properties under particle exchange, and in general relativity, to the KO-dimension of the relevant spectral triple.
