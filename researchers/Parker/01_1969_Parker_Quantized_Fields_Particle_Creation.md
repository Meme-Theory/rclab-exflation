# Quantized Fields and Particle Creation in Expanding Universes. I

**Author(s):** Leonard Parker

**Year:** 1969

**Journal:** Physical Review, Vol. 183, pp. 1057-1068

**arXiv:** None (published before arXiv)

---

## Abstract

The quantization of a spin-0 field (scalar boson) of arbitrary mass is carried out in an expanding Friedmann universe using canonical quantization procedures. The key finding is that particle creation occurs as an inevitable consequence of the time-dependent background metric: the expansion of spacetime itself induces the production of particles in pairs. For massless particles of arbitrary spin (photons, gravitons), no particle creation occurs regardless of the expansion history. The particle number is an adiabatic invariant but not a strict constant of motion, with creation proceeding via the Bogoliubov transformation connecting different particle bases at early and late times in the expansion.

---

## Historical Context

Leonard Parker's 1969 paper stands as the foundational work establishing quantum field theory in curved spacetime and the mechanism of cosmological particle creation. Prior to this work, the quantization of fields in curved spacetime was not well-developed; most attention focused on flat (Minkowski) spacetime or treated gravity as a perturbation. Parker's insight was that the expanding universe—a genuine curved spacetime geometry with time-dependent metric—induces mode mixing and particle creation through the mechanism of the Bogoliubov transformation.

This paper emerged during the late 1960s, following advances in gravitational physics post-Einstein and in quantum field theory post-Feynman/Schwinger. The motivation was partly cosmological: what happens to quantum fields during the hot big bang? And partly theoretical: does the expansion of spacetime have quantum mechanical consequences?

Parker's answer transformed the field. He showed that vacuum fluctuations in the early universe are stretched and amplified by expansion, causing mode functions to evolve nonlinearly. The out-vacuum state (late times) is not equivalent to the in-vacuum state (early times); they are related by a Bogoliubov transformation, implying creation of real particles. The mechanism is purely kinematic—no special potential or interaction is needed, only the time-dependence of the metric.

The paper established several key concepts:
- Particle creation in cosmology is real and inevitable for massive fields
- The Bogoliubov transformation is the mathematical tool connecting different particle bases
- Adiabatic invariants characterize the creation process
- Massless particles are protected (conformal invariance)

This work laid the groundwork for all subsequent developments in quantum cosmology, including Hawking radiation (1974, which Parker recognized as a related phenomenon) and inflation-era particle creation. Session 38 of the Ainulindale framework identifies the BCS transit mechanism as Parker-type creation (not Hawking), confirming Parker's mechanism as the parent physics.

---

## Key Arguments and Derivations

### Quantization in Expanding Universe

Consider a scalar field $\phi(\mathbf{x}, t)$ in a Friedmann-Robertson-Walker (FRW) universe with metric:

$$ds^2 = -dt^2 + a(t)^2 d\Omega_3^2$$

where $a(t)$ is the scale factor. The action is:

$$S = \int d^4x \, \sqrt{-g} \left[ \frac{1}{2}(\partial_\mu\phi)(\partial^\mu\phi) - \frac{1}{2}m^2\phi^2 \right]$$

In conformal coordinates $\eta = \int dt/a(t)$, the equation of motion becomes:

$$\frac{\partial^2\phi}{\partial\eta^2} + \nabla^2\phi + m^2 a(\eta)^2 \phi = 0$$

The field is expanded in eigenfunctions of the Laplacian on the spatial 3-sphere (or 3-torus for flat spatial slices):

$$\phi(\mathbf{x}, t) = \sum_k \left[ a_k(t) u_k(\mathbf{x}) + a_k^\dagger(t) u_k^*(\mathbf{x}) \right]$$

where $u_k$ are spatial eigenfunctions. Canonical quantization imposes:

$$[a_k, a_k^\dagger] = \delta_{kk'}, \quad [a_k, a_{k'}] = 0$$

### Mode Equation and Bogoliubov Transformation

Each mode satisfies a time-dependent oscillator equation:

$$\ddot{f}_k + \omega_k^2(t) f_k = 0$$

where $\omega_k^2(t) = k^2/a(t)^2 + m^2$. This is a generalized time-dependent harmonic oscillator (THO).

For a THO with time-dependent frequency, the standard solution decomposes as:

$$f_k(t) = A_k(t) e^{-i\Phi_k(t)} + B_k(t) e^{i\Phi_k(t)}$$

where $\Phi_k(t) = \int_0^t \omega_k(t') dt'$ is the phase integral. Early in the universe (adiabatic regime), $\omega_k$ changes slowly, and the mode is in the vacuum state of its instantaneous oscillator:

$$a_k^{\text{in}} |0_{\text{in}}\rangle = 0$$

Late in the universe (adiabatic regime), the mode is in a different vacuum:

$$a_k^{\text{out}} |0_{\text{out}}\rangle = 0$$

These states are related by a **Bogoliubov transformation**:

$$a_k^{\text{in}} = \alpha_k a_k^{\text{out}} + \beta_k (a_k^{\text{out}})^\dagger$$

where $|\alpha_k|^2 - |\beta_k|^2 = 1$ (unitarity). The particle creation number in mode $k$ is:

$$N_k = |\beta_k|^2$$

The total expected particle creation is:

$$\langle N \rangle = \sum_k |\beta_k|^2$$

### Adiabatic Invariant and WKB Expansion

For a slowly varying frequency, the WKB expansion applies:

$$f_k(t) \approx \frac{1}{\sqrt{2\omega_k(t)}} \exp\left(-i \int_0^t \omega_k(t') dt' \right)$$

This is the **adiabatic vacuum** state. The particle creation is suppressed by the adiabatic theorem: if $\omega_k$ changes negligibly over a period $\sim 1/\omega_k$, the state remains in the adiabatic ground state and no particles are created.

However, if $\omega_k$ changes rapidly (e.g., during reheating or horizon crossing), the adiabatic approximation breaks down, and $\beta_k \neq 0$, leading to particle creation.

### Conformal Invariance and Massless Fields

For massless fields ($m = 0$) in an expanding universe, the equation becomes:

$$\ddot{f}_k + \frac{k^2}{a(t)^2} f_k = 0$$

This can be rewritten by defining $\tilde{f}_k = a(t) f_k$:

$$\ddot{\tilde{f}}_k + \left(\frac{k^2}{a^2} - \frac{\ddot{a}}{a}\right) \tilde{f}_k = 0$$

For conformally flat metrics (e.g., $a(t) = t^\alpha$), the term $\ddot{a}/a$ is a pure number, and the mode equation is trivial in conformal coordinates. This is the **conformal invariance**: massless fields do not mix modes, and no particle creation occurs.

In contrast, for $m \neq 0$, the mass term $m^2 a^2$ grows with expansion, forcing the frequency to decrease and modes to cross, causing Bogoliubov mixing.

### Energy Density and Radiation Backreaction

The energy density of created particles is:

$$\rho_{\text{created}} = \frac{1}{a^4} \sum_k \left[ \omega_k(t) \langle (a_k^{\text{out}})^\dagger a_k^{\text{out}} \rangle + \frac{1}{2}\omega_k(t) \right]$$

For a radiation-dominated era, this backreacts on the metric via the Einstein equations:

$$\dot{H}^2 + H^2 = \frac{8\pi G}{3} \rho$$

Parker showed that for the case of a massive scalar field in a radiation-dominated universe, the creation rate is significant during certain epochs and can affect the expansion dynamics. This backreaction is small in most scenarios but becomes important in some quantum gravity contexts.

---

## Key Results

1. **Particle Creation Mechanism**: Massive scalar fields are created in pairs due to the time-dependence of the cosmic metric. The creation rate is quantified by the Bogoliubov coefficient $\beta_k$.

2. **Bogoliubov Transformation**: The particle creation is formalized via Bogoliubov transformations connecting early (in-vacuum) and late (out-vacuum) particle bases.

3. **Adiabatic Suppression**: Particle creation is suppressed if the metric varies adiabatically (slowly). Rapid metric changes (e.g., reheating) lead to particle creation.

4. **Conformal Protection**: Massless particles (photons, gravitons in some cases) are not created due to conformal invariance of the massless wave equation.

5. **Kinematic Origin**: Particle creation requires no special interaction—purely kinematic spacetime geometry causes it.

6. **Energy Backreaction**: Created particles contribute to the energy density and can feed back into the expansion dynamics, though the effect is usually perturbative.

---

## Impact and Legacy

Parker's 1969 paper revolutionized quantum cosmology and established a new branch of theoretical physics. Key impacts include:

- **Hawking Radiation (1974)**: Hawking applied Parker's mechanism to black hole horizons, showing that quantum fields near an event horizon create a thermal spectrum. Parker and Hawking both recognized the deep connection.

- **Inflation Theory (1980s+)**: Inflationary cosmology relies on Parker's mechanism to explain the origin of density perturbations. Quantum fluctuations in the inflaton field are stretched by exponential expansion, creating classical perturbations that seed large-scale structure.

- **Quantum Field Theory in Curved Spacetime**: The paper established the mathematical framework (Bogoliubov transformations, adiabatic vacua, mode mixing) that has become standard in theoretical physics.

- **Thermodynamics of Horizons**: Parker's work on cosmological particle creation connects to the thermodynamic properties of horizons, leading to the holographic principle and the black hole information problem.

- **Reheating and Preheating**: Modern studies of particle creation during the end of inflation (preheating) use Parker's formalism directly.

- **Experimental Interest**: Though cosmological particle creation is not directly observable, its effects on the CMB and large-scale structure are tested by experiments like WMAP, Planck, and DESI.

---

## Connection to Phonon-Exflation Framework

**CRITICAL RELEVANCE**: Session 38 identified the BCS transit during the phonon-exflation mechanism as Parker-type particle creation, NOT Hawking radiation. This is the direct parent mechanism for the framework.

### Specific Connections

1. **Pair Creation Mechanism**: In Parker's theory, particles are created in pairs due to mode mixing in expanding spacetime. In BCS phonon condensation during the exflation transit, Cooper pairs (two-fermion bound states) are created by the time-dependent deformation of the SU(3) spectral geometry. The mathematical structure is identical: Bogoliubov transformation on a time-varying geometric background.

2. **Adiabatic Invariant**: Parker identifies the particle number as an adiabatic invariant—it is not a conserved quantity but changes as the metric evolves. In the phonon-exflation framework, the pairing quantum number (K_7 charge in the B2 sector) evolves during the exflation transit, driven by the time-dependent geometry. The analogy is direct.

3. **Mode Mixing and Resonance**: Parker's particle creation is driven by frequency crossing (omega_k ~ k/a decreases as a increases). In the BCS regime, the pairing gap Delta and the Dirac spectrum modes interact via the time-dependent chemical potential mu(tau). The analogy extends to threshold crossings and van Hove singularities (M_max = 1.674 in Session 35).

4. **Kinematic vs. Dynamical**: Parker shows that expansion alone (without interaction) creates particles. This is purely geometric. Similarly, in phonon-exflation, the geometric deformation of SU(3) (parameterized by tau) drives the BCS instability without requiring external potentials or interactions beyond the spectral action. The mechanism is kinematic-geometric.

5. **GGE Permanence**: Parker's in-vacuum and out-vacuum states are related but distinct—particle creation breaks the vacuum state. In the framework (Session 38), the post-transit state is a **Generalized Gibbs Ensemble (GGE)** with 8 Richardson-Gaudin conserved integrals. This is a finite-dimensional analog of Parker's out-vacuum: the state that emerges after creation events have occurred, with a new set of constants of motion.

6. **No Hawking Connection**: Parker created in an expanding universe background without an event horizon. Hawking created near a black hole horizon with thermal spectrum. The phonon-exflation BCS transit is Parker-type: no horizon, no thermal spectrum, only coherent pair creation and conservation laws (integrability). Session 38 explicitly ruled out Hawking-type thermalization via the integrability theorem.

7. **Spectral Action as Geometric Stage**: Parker's metric g_mu_nu is the "stage" for particle creation. In the framework, the Dirac spectrum (or equivalently the spectral action S_spec) is the geometric stage for BCS pairing. Both are purely geometric, no extraneous forces needed.

### Quantitative Analogy

- Parker: $N_k = |\beta_k|^2$ (dimensionless creation number per mode)
- Framework: $n_inst = \langle N_+ \rangle = 59.8$ pair operators at the transit (Session 38). The instanton gas has S_inst = 0.069, and integrand matches the Schwinger instanton integral (Schwinger-instanton duality, Session 38 W3).

Both quantities measure the amount of coherent pair creation. Parker's creation is distributed over infinitely many cosmological modes; the framework's is localized to the finite Dirac spectrum of SU(3).

---

## Supplementary Notes

### Relation to Second Quantization

Parker's work assumes second-quantized fields (creation/annihilation operators). The vacuum state $|0_{\text{in}}\rangle$ is the state of no particles in the early universe. As the universe expands, the Bogoliubov transformation shows that this state, when expressed in the late-time basis, contains particles: $a_k^{\text{out}} |0_{\text{in}}\rangle \neq 0$. This is not due to any external source; the background geometry itself causes the creation.

### Conformal Anomaly

While massless fields are conformally invariant and do not create particles, quantum loop corrections (conformal anomaly) can induce effective mass and lead to particle creation even for massless fields. This is relevant to photons and gravitons in some cosmological scenarios.

### Modern Applications

Parker's formalism has been extended to:
- Fermionic fields (Dirac fields), where creation occurs in particle-antiparticle pairs
- Massive vector fields (with polarization complications)
- Nonminimally coupled fields
- Curved spacetime backgrounds beyond FRW (de Sitter, anti-de Sitter, black hole spacetimes)

The Ainulindale framework applies Parker's mechanism to a finite-dimensional Dirac spectrum (SU(3) geometry) undergoing rapid deformation, making it one of the most concrete implementations of Parker's abstract principle.

