# Phonon Dispersion Relations: Debye Model and Born-von Karman Theory (1912-1920s)

**Author:** Peter Debye, Max Born, Theodor von Karman, and colleagues
**Year:** 1912-1930 (foundational papers)
**Source:** Debye, P. "Zur Theorie der spezifischen Waermen" (1912); Born & von Karman, "On the Vibrations of Mono- and Polyatomic Lattices" (1912)

---

## Abstract

In the early 20th century, Peter Debye, Max Born, and Theodor von Karman developed the theory of lattice vibrations—a quantum-mechanical framework describing how atoms in a crystal lattice oscillate collectively, creating quasiparticles called phonons. Debye's model provided a simple yet powerful picture: a solid is treated as a continuous elastic medium supporting three acoustic branches (one longitudinal, two transverse), each with dispersion relation $\omega(k) = v_s |k|$ (linear at small $k$). Born and von Karman developed the full lattice dynamics approach using periodic boundary conditions and eigenvalue analysis of the dynamical matrix. These frameworks explained heat capacity, thermal conductivity, and elastic properties of solids from first principles. This paper reviews the foundational phonon theory essential to understanding the phonon-exflation framework.

---

## Historical Context

In the early 1900s, heat capacity of solids presented a puzzle. The Dulong-Petit law predicted constant heat capacity (3 per atom), but experiment showed heat capacity decreases at low temperatures. Einstein (1907) proposed that atoms oscillate as independent quantum harmonic oscillators, explaining the temperature dependence. However, this model predicted a Debye temperature (a characteristic temperature scale) that didn't match experiments.

Debye (1912) and Born-von Karman (1912) recognized the issue: atoms do not oscillate independently. They interact through elastic forces, creating collective modes—phonons. The spectrum of phonon frequencies is continuous (not discrete like Einstein's independent oscillators), and density-of-states calculations gave the correct heat capacity dependence.

This was a major conceptual shift: from independent particles to collective excitations. The phonon became the central object of condensed-matter physics.

---

## The Debye Model

### Core Concept

The Debye model treats a solid as a continuous elastic medium. Vibrations are acoustic waves with dispersion relation:

$$\omega(k) = v_s |k|$$

where $v_s$ is the sound velocity (assumed constant for simplicity). There are three acoustic branches: one longitudinal (velocity $v_L$) and two transverse (velocity $v_T$).

The phonon density of states is:

$$g(\omega) = \frac{V}{2\pi^2} \left[\frac{1}{v_L^3} + \frac{2}{v_T^3}\right] \omega^2$$

for $\omega$ below the Debye cutoff frequency $\omega_D$, and $g(\omega) = 0$ for $\omega > \omega_D$.

The Debye cutoff is determined by the constraint that the total number of modes equals $3N$ (where $N$ is the number of atoms):

$$\int_0^{\omega_D} g(\omega) \, d\omega = 3N$$

This gives:

$$\omega_D = v_s \left(6\pi^2 n\right)^{1/3}$$

where $n = N/V$ is the number density of atoms.

### Heat Capacity from Debye Model

The average energy of a phonon at frequency $\omega$ and temperature $T$ is:

$$\langle E_\omega \rangle = \frac{\hbar \omega}{e^{\hbar\omega/k_B T} - 1}$$

(Bose-Einstein distribution: phonons are bosons.)

The total internal energy is:

$$U = \int_0^{\omega_D} \hbar \omega g(\omega) \frac{1}{e^{\hbar\omega/k_B T} - 1} d\omega$$

The heat capacity is:

$$C_V = \frac{\partial U}{\partial T}$$

At low temperatures ($T \ll \theta_D$, where $\theta_D = \hbar\omega_D/k_B$ is the Debye temperature):

$$C_V \propto T^3$$

(Debye's $T^3$ law, matching experiments!)

At high temperatures ($T \gg \theta_D$):

$$C_V \to 3Nk_B$$

(Dulong-Petit limit.)

---

## Born-von Karman Lattice Dynamics

### Dynamical Matrix Approach

Born and von Karman developed a more complete theory treating atoms as discrete masses connected by springs. For a monoatomic lattice, atoms at positions $\vec{R}_n$ (labeled by lattice vector $\vec{n}$) oscillate with displacements $u_n(t)$.

The equations of motion are:

$$m \ddot{u}_n = -\sum_{n'} \Phi_{n-n'} u_{n'}$$

where $\Phi$ is the force-constant matrix (spring stiffness between atoms).

For lattice vibrations, assume traveling-wave solutions:

$$u_n = A e^{i(\vec{k} \cdot \vec{R}_n - \omega(k) t)}$$

This leads to the eigenvalue problem:

$$\omega^2 A = D(\vec{k}) A$$

where $D(\vec{k})$ is the dynamical matrix:

$$D_{\alpha\beta}(\vec{k}) = \frac{1}{m} \sum_n \Phi_{\alpha\beta}(n) e^{i\vec{k} \cdot \vec{R}_n}$$

(summation over neighboring atoms; $\alpha, \beta$ are Cartesian coordinates.)

Solving the eigenvalue problem yields three branches: $\omega_j(\vec{k})$ for $j = 1, 2, 3$.

### Brillouin Zone and Periodic Boundary Conditions

In an infinite crystal, $\vec{k}$ is continuous. To make the problem tractable, Born and von Karman applied periodic boundary conditions: the crystal is topologically a torus, so $\vec{k}$ takes discrete values in the first Brillouin zone (reciprocal-space cell of the lattice).

For a cubic lattice with lattice constant $a$, the first Brillouin zone extends from $-\pi/a$ to $+\pi/a$ in each direction. Each wavenumber $\vec{k}$ corresponds to one normal mode of the entire crystal.

The number of modes in the Brillouin zone equals the number of atoms (or degrees of freedom per atom times the number of atoms).

---

## Dispersion Relations: Key Features

### Acoustic Branches

For monoatomic lattices, the three phonon branches are acoustic. At small $\vec{k}$:

$$\omega(\vec{k}) \approx v_s |\vec{k}|$$

(linear dispersion, like Debye model)

As $\vec{k}$ increases toward the Brillouin zone boundary, $\omega(\vec{k})$ reaches a maximum and becomes horizontal (flat). This cutoff in frequency is crucial: it explains why heat capacity saturates at the Dulong-Petit value at high temperatures.

### Optical Branches

For polyatomic lattices (multiple atoms per primitive cell), additional optical branches appear. These have $\omega(\vec{k})$ that is nearly constant (flat, frequency doesn't depend strongly on $\vec{k}$), with energy gap $\omega_{\text{opt}}$ at $\vec{k} = 0$.

Optical phonons are important for ionic crystals and semiconductors. They carry strong electric dipole moments (because the charges oscillate), making them observable in infrared spectroscopy.

### Group and Phase Velocity

The group velocity (energy transport speed) is:

$$v_g(\vec{k}) = \frac{\partial \omega(\vec{k})}{\partial \vec{k}}$$

The phase velocity is:

$$v_p(\vec{k}) = \frac{\omega(\vec{k})}{|\vec{k}|}$$

In the Debye approximation, $v_g = v_p = v_s$ (constant). In real crystals, $v_g$ and $v_p$ differ, and both depend on $\vec{k}$.

---

## Connection to Phonon-Exflation Framework

The Born-von Karman and Debye theories are foundational to phonon-exflation because they establish phonons as the correct language for describing collective excitations in a medium:

1. **Discrete spectrum from continuous medium**: The remarkable insight of lattice dynamics is that a continuous elastic medium (or discrete atoms with interactions) can support a discrete spectrum of vibrational modes. The Brillouin zone construction shows that a finite crystal (with periodic boundary conditions) has a discrete set of $\vec{k}$ values, hence discrete eigenfrequencies $\omega_j(\vec{k})$. In phonon-exflation, the universe's particle spectrum arises from the discrete eigenvalues of the Dirac operator $D_K$ on the internal space (SU(3)). Both are examples of spectral discretization: continuous geometry yields discrete quanta.

2. **Density of states and thermodynamics**: The Debye density of states $g(\omega) \propto \omega^2$ (at low $\omega$) is the starting point for computing thermodynamic properties. In phonon-exflation, the spectral action is precisely:

$$S = \int d^4x \sqrt{-g} \left[a_0 f(D_K^2/\Lambda^2) + \text{matter}\right]$$

where $f$ is a smooth function that weights mode contributions. The expansion of $f$ in eigenvalues of $D_K$ yields the low-energy effective action. This is structurally identical to Debye's approach: sum over all modes with weight given by density-of-states.

3. **Temperature dependence of properties**: The Debye model predicts that heat capacity depends on temperature via the Bose-Einstein distribution. If the universe is a phononic condensate (as in Volovik's superfluid cosmology), then thermal excitations are phonons, and heat capacity scales as $T^3$ at low temperatures. The equation of state of the universe would match phonon thermodynamics, not a scalar field or cosmological constant.

4. **Dispersion relations and wave propagation**: The Debye and Born-von Karman theories show how geometric structure (lattice constant, force constants) determines dispersion relations $\omega(\vec{k})$. In phonon-exflation, the internal geometry (metric on SU(3), encoded in the Jensen parameter $s$) determines the particle mass spectrum. Changing the metric is analogous to changing the force constants—it renormalizes the dispersion relation, which renormalizes particle masses.

5. **Acoustic vs optical modes**: Lattice dynamics distinguish acoustic modes (gapless, $\omega \to 0$ as $\vec{k} \to 0$) from optical modes (gapped, $\omega > \omega_0$ always). In the Standard Model, photons are gapless (acoustic), while Higgs and other scalars are gapped (optical-like). This distinction arises naturally in NCG if the Dirac spectrum is partitioned by symmetry.

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Debye linear dispersion | $\omega(\vec{k}) = v_s |\vec{k}|$ | Sound wave relation |
| Debye density of states | $g(\omega) = \frac{V}{2\pi^2} \left[\frac{3}{v_s^3}\right] \omega^2$ | Number of modes in frequency interval |
| Debye cutoff | $\omega_D = v_s (6\pi^2 n)^{1/3}$ | Maximum phonon frequency |
| Debye temperature | $\theta_D = \hbar \omega_D / k_B$ | Characteristic temperature scale |
| Phonon energy (Bose-Einstein) | $\langle E_\omega \rangle = \frac{\hbar\omega}{e^{\hbar\omega/k_B T} - 1}$ | Average energy per mode |
| Heat capacity (Debye T^3 law) | $C_V = \frac{12\pi^4 N k_B}{5} (T/\theta_D)^3$ | Low-temperature heat capacity |
| Dynamical matrix | $D(\vec{k}) = \frac{1}{m} \sum_n \Phi(n) e^{i\vec{k} \cdot \vec{R}_n}$ | Eigenvalues give $\omega^2(\vec{k})$ |
| Group velocity | $v_g = \partial \omega / \partial k$ | Energy transport velocity |

---

## Critical Assessment

**What holds up**:
- Debye model correctly predicts heat capacity at low and high temperatures
- Born-von Karman lattice dynamics is exact (in principle; assumes pairwise force constants)
- Phonons are the correct quasiparticles for describing collective vibrations
- Dispersion relations from lattice dynamics match experiments
- The density-of-states approach generalizes to any system with discrete spectrum

**What was simplified**:
- Debye model assumes linear dispersion; real solids have curved dispersion
- Debye cutoff is artificial (density of states actually goes to zero at $\omega_D$); real solids have gradual cutoff
- Born-von Karman assumes pairwise interactions; real atoms interact via many-body forces
- Anharmonic effects (mode-mode interactions, nonlinear phonon dynamics) are neglected

**Ahead of its time**:
- Recognition that collective excitations (phonons) are the right language for solids
- Insight that discrete spectrum emerges from periodic boundary conditions
- Bose-Einstein statistics applied to phonons
- Connection between microscopic dynamics and macroscopic thermodynamics

---

## Legacy and Modern Applications

Phonon theory revolutionized solid-state physics and materials science:

1. **Thermal transport**: Heat capacity, thermal conductivity, and thermal expansion are all computed via phonon distributions
2. **Electron-phonon interaction**: Electrical conductivity, superconductivity, and semiconductor transport all involve phonon scattering
3. **Spectroscopy**: Phonon frequencies are probed via Raman and infrared spectroscopy
4. **Topological phonons**: Modern research explores topological properties of phonon bands (phononic topological insulators)

---

## References

1. Debye, P. (1912). "Zur Theorie der spezifischen Waerme." Annalen der Physik 39: 789-839.
2. Born, M. & von Karman, T. (1912). "Ueber Schwingungen in Raumgittern." Physikalische Zeitschrift 13: 297-309.
3. Born, M. & Huang, K. (1954). "Dynamical theory of crystal lattices." Oxford University Press.
4. Kittel, C. (2005). "Introduction to solid state physics." 8th edn. Wiley.
5. Ashcroft, N.W. & Mermin, N.D. (1976). "Solid state physics." Holt, Rinehart, Winston.
6. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press. (Phonons in quantum liquids)
