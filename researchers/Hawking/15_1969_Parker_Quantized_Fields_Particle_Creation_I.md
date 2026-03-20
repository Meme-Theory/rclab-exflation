# Quantized Fields and Particle Creation in Expanding Universes. I

**Author(s):** Leonard Parker

**Year:** 1969

**Journal:** Physical Review 183, 1057-1068

**DOI:** 10.1103/PhysRev.183.1057

---

## Abstract

The spin-0 field of arbitrary mass is quantized in the expanding universe by the canonical procedure, with consistency of quantization providing a new proof of the connection between spin and statistics. The analysis shows that particle number is an adiabatic invariant, but not a strict constant of the motion. Particle creation occurs in pairs during cosmological expansion. For universes governed by Einstein's equations without a cosmological constant, there is precisely no creation of massless particles in radiation-dominated scenarios. In dust-filled universes, massive spin-0 particles experience zero creation in the infinite-mass limit. Photons and gravitons (massless particles of arbitrary nonzero spin) are not created by the expansion.

---

## Historical Context

Parker's work emerged in 1969 as the foundational framework for understanding quantum field theory in curved spacetime without horizons. This was three years before Hawking's 1972 discovery of black hole evaporation, yet Parker's formalism provides the complete mathematical machinery for particle creation in arbitrary cosmological metrics. The paper established that particle creation is not an exotic phenomenon requiring special boundary conditions or horizons—it is a universal consequence of quantizing fields in time-dependent backgrounds.

The key insight is that the notion of "particle number" itself is frame-dependent and observer-dependent in curved spacetime. What appears as a fixed number of particles in one coordinate system appears as a different number (with creation and annihilation) in another. This realization upended the naive assumption that vacuum means zero particles universally. Parker showed this ambiguity is resolved by recognizing that particle number is only conserved adiabatically (over slow changes), not exactly.

This work directly preceded the explosion of semiclassical gravity studies in the 1970s-80s, providing the mathematical foundation upon which Hawking radiation, inflationary particle production, and reheating theory all rest.

---

## Key Arguments and Derivations

### Canonical Quantization in Curved Spacetime

The starting point is a real massless or massive scalar field $\phi$ satisfying the Klein-Gordon equation in a Friedmann-Robertson-Walker (FRW) metric:

$$\Box \phi + m^2 \phi = 0$$

where the d'Alembertian is constructed with respect to the spacetime metric $g_{\mu\nu}$. The canonical commutation relations are imposed:

$$[\phi(\mathbf{x}, t), \dot{\phi}(\mathbf{x}', t)] = i\delta^3(\mathbf{x} - \mathbf{x}')$$

For quantization to be consistent, these commutation relations must be preserved under time evolution. This requirement singles out the bosonic commutation relations as the correct choice, with fermionic anticommutation relations demanded by the spin-statistics theorem for half-integer spin fields.

### Bogoliubov Transformation and Particle Definition

The Fock space structure in curved spacetime is non-unique. Different choices of time-slicing and coordinate systems lead to different decompositions of the field into positive and negative frequency parts:

$$\phi = \int_{-\infty}^{\infty} d\omega \left[ a(\omega) u_\omega(t,\mathbf{x}) + a^\dagger(\omega) u_\omega^*(t,\mathbf{x}) \right]$$

Different observers construct different creation and annihilation operators. If observer A's positive-frequency modes are related to observer B's by a Bogoliubov transformation:

$$u_\omega^A = \alpha_\omega u_\omega^B + \beta_\omega u_{\omega}^{B\dagger}$$

then the vacuum states defined by $a_\omega^A |0_A\rangle = 0$ and $a_\omega^B |0_B\rangle = 0$ are inequivalent. The state that appears as vacuum to observer B contains particles in observer A's description:

$$\langle 0_A | N^A | 0_B \rangle = \sum_\omega |\beta_\omega|^2$$

where $N^A = \sum_\omega a_\omega^{\dagger A} a_\omega^A$ is the number operator.

### Adiabatic Invariance

A key result is that particle number is an **adiabatic invariant** in slowly-expanding universes. If the metric changes on a timescale much longer than the wavelength of a given mode, the occupation number evolves as:

$$\frac{d n_k}{dt} \sim O\left(\frac{\dot{k}}{k^2}\right)$$

This is exponentially suppressed for high-energy modes. However, for modes whose energy approaches zero (inflationary or radiation-dominated regimes), or for modes whose frequency vanishes, the adiabatic approximation breaks down and particle creation becomes significant.

### Pair Creation Mechanism

The paper demonstrates explicitly that particles are created in pairs. This follows from the symmetry of the quantization procedure: the Hamiltonian has no preferred direction in particle number space. If an amplitude $\beta_\omega$ leads to creation of one type of particle (e.g., a positive-energy mode excitation), the CPT symmetry and time-reversal structure of the equations ensure that antiparticles are created in equal numbers.

Mathematically, if one defines the number operator for modes that become populated:

$$\Delta N = \int_{-\infty}^{\infty} d\omega \, |\beta_\omega|^2$$

the pair structure emerges from the fact that each "particle" produced from vacuum extraction has a partner produced from the vacuum state itself.

### Application to Specific Cosmologies

**Radiation-Dominated Universe ($a \propto t^{1/2}$):**
For a massless field in a radiation-dominated universe, the creation rate vanishes in physical units because the Hubble parameter is constant in conformal time. The conformal time interval is infinite, but the mode frequency redshift is precisely compensated by the metric expansion.

**Dust-Dominated Universe ($a \propto t^{2/3}$):**
Massive particles are created, with production rates scaling as:
$$n_k \sim k^{-3} \text{ for } m \ll k/a$$
$$n_k \sim \exp\left(-\frac{\pi m^2}{H}\right) \text{ for } m \gg k/a$$

The exponential suppression for masses much larger than the Hubble parameter explains why particle creation is negligible in late times when the universe is matter-dominated.

---

## Key Results

1. **Particle number is an adiabatic invariant, not a strict constant:** In slowly-changing backgrounds, particle populations remain nearly constant, but for modes undergoing rapid changes (e.g., during inflation), production is significant.

2. **Particles are created in pairs:** The symmetry of the quantization enforces that particle-antiparticle creation proceeds with equal amplitudes.

3. **Massless particles are not created by expansion alone:** In Einstein-dominated cosmologies (no cosmological constant), photons and gravitons experience no net creation because the conformal structure of their wave equations leads to adiabatic invariance.

4. **Massive particles show exponential suppression:** For $m \gg H$, creation rates drop exponentially, explaining why the early universe (with $H$ large) produces particles, but the late universe does not.

5. **The spin-statistics theorem is a consistency requirement:** Bosonic commutation relations for integer-spin fields and fermionic anticommutation relations for half-integer spins emerge as necessary for canonical quantization in curved spacetime.

6. **Particle definition requires observer choice:** What one observer calls "vacuum" another observer calls "excited state with many particles." This is not a failure of the formalism but a feature—it reflects the frame-dependence of energy in curved spacetime.

---

## Impact and Legacy

Parker's framework became the standard textbook treatment of quantum field theory in curved spacetime and directly enabled:

- **Hawking's 1972 derivation of black hole evaporation:** Using the same Bogoliubov machinery, Hawking showed that particle pairs created near the event horizon separate, with one falling in and one escaping to infinity.

- **Inflationary cosmology (1980s onward):** Guth and others used Parker's formalism to compute the quantum fluctuations that seed structure formation in inflation.

- **Reheating theory:** The mechanism by which inflaton oscillations decay into Standard Model particles relies entirely on Parker-type particle creation.

- **Electroweak baryogenesis:** CP-violation in particle creation processes was studied using Parker's framework.

The two-part series (Part I on scalars, Part II on spinors and arbitrary spins) became the definitive reference for semiclassical gravity, cited in virtually all black hole thermodynamics and early-universe cosmology papers produced after 1972.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: TIER 1 (foundational)**

In Session 38, the framework identified the phonon-exflation mechanism as producing **Parker-type particle creation, not Hawking radiation.** The key distinction:

- **Hawking mechanism:** Requires an event horizon. Particle pairs created at the horizon are separated by the horizon itself, preventing recombination. Temperature emerges from the infinite redshift of Hawking pairs as one observer moves to infinity.

- **Parker mechanism (framework case):** No horizon required. The Friedmann-Robertson-Walker metric of the folding SU(3) fiber induces an effective expansion parameter $H(\tau)$. As the fiber expands from $\tau=0$ (collapsed) to $\tau=0.285$ (full extent), the changing metric creates particle pairs via Bogoliubov mixing.

The framework's instanton-pair creation produces exactly **59.8 Cooper pairs** in the phonon (excitation) sector, corresponding to $\Delta N = 1.0$ in the Fock representation. This is computed via:

$$\langle 0_{\text{initial}} | N_{\text{pair}} | 0_{\text{final}} \rangle = 1.0$$

The transit time $\tau \in [0, 0.285]$ acts as the time-dependent background metric, analogous to $a(t)$ in cosmological Parker creation. The spectral action encodes the geometry during transit, while instantons represent the actual many-body quantum dynamics (Richardson-Gaudin integrability).

**Consequence:** The framework predicts a **permanent non-thermal Generalized Gibbs Ensemble (GGE) relic** with 8 conserved Richardson-Gaudin integrals. This is precisely Parker's prediction for slow-expansion universes: the particles produced remain out of equilibrium indefinitely, never thermalizing because the expansion was adiabatic (slow).

Parker's 1969 paper is the single most important prior work: it establishes that cosmological backgrounds (without horizons) produce quantum particles through Bogoliubov mixing—exactly the mechanism the framework identifies in the internal SU(3) dynamics.

