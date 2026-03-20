# Fifty Years of Cosmological Particle Creation

**Author(s):** Leonard Parker and Jose Navarro-Salas

**Year:** 2017

**Journal:** arXiv preprint (conference review from ERE2014)

**arXiv:** 1702.07132

---

## Abstract

This paper is a comprehensive historical and technical review of cosmological particle creation, covering the full development from Parker's 1966 thesis through 2017. Formatted as a detailed interview conducted during the ERE2014 (Spanish Relativity Meeting) in Valencia, September 2014, the review traces the mechanisms of particle creation for all spin fields (scalar, vector, spinor, graviton), discusses the connection to Hawking radiation and black hole thermodynamics, reviews applications to inflation and the early universe, and examines modern developments in quantum cosmology. The paper emphasizes that particle creation is not a small or exotic effect but a fundamental consequence of quantum field theory in curved spacetime, with implications for cosmology from the Planck scale through late-time acceleration.

---

## Historical Context

Leonard Parker's discovery of cosmological particle creation in his 1966 dissertation (published as the landmark 1969 paper) opened a new era in theoretical cosmology and quantum gravity. The fifty years between 1966 and 2016 saw the development of a mature field with dozens of applications and extensions.

The 2017 review is strategically timed: the field has matured enough to assess the impact on modern cosmology (inflation, preheating, reheating, dark matter candidates), and enough time has passed to write a genuine historical account. Parker himself, one of the pioneers, provides authoritative perspective on what was known, what was speculative, and what has been confirmed.

Key milestones in the field's development:

- **1966-1969**: Parker's original work on scalar and vector fields in expanding universes
- **1974**: Hawking's discovery of radiation near black hole horizons, recognized as a parallel phenomenon
- **1980s**: Application to inflation (Guth, Albrecht-Steinhardt, Linde)
- **1990s-2000s**: Preheating, reheating, and parametric resonance (Kofman, Linde, Riotto)
- **2000s-2010s**: Precision cosmology tests (WMAP, Planck) confirming predictions of inflation-driven particle creation
- **2010s+**: Modern developments in quantum gravity, holography, and black hole thermodynamics

The review by Parker and Navarro-Salas synthesizes this entire trajectory.

---

## Key Arguments and Derivations

### Part I: Scalar Field Particle Creation

The scalar field in an FRW universe:

$$\partial_\mu \left(\sqrt{-g} g^{\mu\nu} \partial_\nu \phi \right) - \sqrt{-g} m^2 \phi = 0$$

In conformal time $\eta$:

$$\phi''(\eta) + \nabla^2 \phi + a(\eta)^2 m^2 \phi = 0$$

Expanding in eigenmodes:

$$\phi(\eta, \mathbf{x}) = \sum_k \left[ a_k u_k(\eta) + \text{h.c.} \right]$$

Each mode satisfies:

$$u_k''(\eta) + \omega_k^2(\eta) u_k(\eta) = 0$$

where $\omega_k^2(\eta) = k^2 + a(\eta)^2 m^2$.

For a universe with scale factor $a(t) = t^p$ (power-law expansion), the mode equation becomes:

$$\frac{d^2 u_k}{d\eta^2} + \left( k^2 + \frac{\nu^2 - 1/4}{\eta^2} \right) u_k = 0$$

where $\nu = m/Hp$ depends on the mass and expansion rate. This is a **Bessel equation** with solutions in terms of Hankel functions $H_\nu^{(1,2)}(k\eta)$.

In the adiabatic limit (early times, $k\eta \to \infty$):

$$u_k \to \frac{1}{\sqrt{2k}} e^{-ik\eta}$$

In the long-wavelength limit (late times, $k\eta \to 0$):

$$u_k \to \eta^\nu$$

The Bogoliubov coefficients are:

$$\alpha_k = \langle \text{out} | \text{in} \rangle, \quad \beta_k = \langle \text{out} | \text{in}^* \rangle$$

For the power-law case:

$$|\beta_k|^2 \approx \exp\left( -\frac{2\pi\nu}{|p|} \right)$$

This **exponential suppression** of particle creation is fundamental: the creation rate depends on the nonadiabaticity of the expansion.

### Part II: Massless Conformal Fields

For $m = 0$ in a conformal metric $ds^2 = a(\eta)^2 (-d\eta^2 + d\mathbf{x}^2)$, the conformal transformation:

$$\tilde{\phi} = a(\eta) \phi$$

reduces the equation to:

$$\tilde{\phi}'' + \nabla^2 \tilde{\phi} = 0$$

which is the flat-spacetime wave equation. **No particle creation occurs**. This is conformal invariance: massless fields are "invisible" to the metric expansion at the classical level.

However, quantum corrections (one-loop diagrams) and anomalies can induce effective masses, allowing creation.

### Part III: Vector (Massive Photon-like) Fields

For a massive vector field:

$$\partial_\mu F^{\mu\nu} + m^2 A^\nu = 0$$

where $A^\nu$ is the four-potential. In an expanding universe:

$$A_i'' + \omega_k^2(\eta) A_i = 0$$

with longitudinal and transverse modes mixing due to the expansion. The scalar (Coulomb-like) mode does not couple to the expansion (protected by gauge invariance in the massless limit), while the vector (transverse) modes create particles similar to the scalar case.

Particle creation in massive vector fields was analyzed by Parker in his 1969-1971 papers, establishing that creation occurs for all components with rates comparable to (or sometimes exceeding) scalar fields.

### Part IV: Fermionic (Spinor) Field Creation

For a Dirac spinor $\psi$ in curved spacetime:

$$(i\gamma^\mu \nabla_\mu - m) \psi = 0$$

where $\gamma^\mu$ are curved-space gamma matrices. In an FRW metric:

$$\psi(\eta, \mathbf{x}) = \sum_k \sum_s \left[ a_{k,s}(t) u_{k,s}(\eta, \mathbf{x}) + b_{k,s}^\dagger(t) v_{k,s}(\eta, \mathbf{x}) \right] |0\rangle$$

where $s$ labels helicity and $a, b$ are fermion creation/annihilation operators (anticommutation relations).

For fermionic fields, particle creation is subtle: fermions obey exclusion statistics (Pauli principle), so the vacuum cannot accommodate infinite numbers of them. However, for expanding universes with infinitely many spatial modes, particle-antiparticle pair creation is still possible.

The creation of electron-positron pairs in the early universe proceeds via the same Bogoliubov mechanism, with additional complications from the spinor structure. Parker and subsequent authors showed that fermionic particle creation is suppressed (relative to scalars) by the Pauli exclusion principle but remains significant in the ultra-relativistic early universe.

### Part V: Graviton Creation

Gravitational waves (spin-2 massless fields) are described by the propagating components of the metric perturbation:

$$h_{ij}'' + \nabla^2 h_{ij} + \left( \frac{a''}{a} \right) h_{ij} = 0$$

For a conformal metric, the term $a''/a$ is a pure number. The conformal invariance of massless spin-2 fields means:

**No gravitons are created in a conformal universe**.

However, non-conformal expansions (most realistic cosmologies) do create gravitons. The creation rate is proportional to:

$$|\beta_k|^2 \sim \left( \frac{H}{\text{scale}} \right)^2$$

For inflation, this leads to a stochastic background of gravitational waves that are potentially observable by future detectors like LISA.

### Part VI: Hawking Radiation as a Special Case

In 1974, Stephen Hawking applied the particle creation formalism to a black hole spacetime and discovered that quantum fields near the event horizon radiate with a thermal spectrum at temperature:

$$T_H = \frac{\hbar \kappa}{2\pi k_B c}$$

where $\kappa$ is the surface gravity of the black hole. Hawking radiation is now understood as a special case of Parker's general mechanism: the event horizon is a one-way surface (like a time-dependent boundary condition), which causes Bogoliubov mixing and particle creation.

Key differences from cosmological creation:
- **Thermal spectrum**: The created particles have a thermal distribution at $T_H$
- **Negative energy flux**: The ingoing flux has negative energy (inside the horizon), leading to black hole evaporation
- **Horizon causality**: The horizon structure constrains which modes can be created

The recognition that Hawking and Parker are dual aspects of the same phenomenon unified quantum field theory in curved spacetime.

---

## Key Results and Modern Implications

### 1. Inflation-Driven Density Perturbations

The most successful application of Parker's mechanism is to the origin of density perturbations in inflation. During exponential expansion $a(t) \propto e^{Ht}$:

- Quantum vacuum fluctuations in the inflaton field are stretched to superhorizon scales
- The wavelength $\lambda = 2\pi a(t) k^{-1}$ grows faster than the Hubble radius $H^{-1}$
- Modes exit the horizon and freeze as classical perturbations
- After inflation ends, these perturbations re-enter and source density fluctuations

The spectral index (scale dependence) of density perturbations is:

$$n_s = 1 - 2\epsilon - \delta$$

where $\epsilon = -\dot{H}/H^2$ (slow-roll parameter) and $\delta$ are geometric properties of the inflaton potential. Precise measurements by Planck (2018) yield $n_s = 0.965 \pm 0.004$, consistent with single-field inflation driven by Parker-type particle creation.

### 2. Preheating and Parametric Resonance

At the end of inflation, the inflaton oscillates about the minimum of its potential. The oscillating inflaton field couples to other fields (e.g., standard model fermions, scalar fields) via:

$$\mathcal{L}_{\text{int}} = g \phi \chi^2$$

where $\phi$ is the inflaton and $\chi$ is a light field. The time-dependent amplitude of the inflaton acts like an oscillating pump, leading to **parametric resonance**: certain modes of $\chi$ grow exponentially (narrow-band resonance) or broadly (broad-band resonance).

This preheating process, driven by Parker-type particle creation in the time-dependent inflaton background, produces a large population of created particles in a very short time, eventually thermalizing into the radiation-dominated universe we observe. Without preheating, the universe would remain cold and matter-dominated.

### 3. Cosmological Graviton Background

Gravitational waves created during inflation produce a stochastic background:

$$\Omega_{\text{GW}}(f) \propto f^2 \quad \text{(spectral shape)}$$

This background is completely determined by the inflationary expansion history (via Parker's mechanism) and is essentially independent of particle physics details. Future experiments (LISA, Einstein Telescope, Cosmic Explorer) will measure this background and constrain inflation.

### 4. Dark Matter Candidates from Particle Creation

In beyond-standard-model cosmologies, particle creation can generate relics of superheavy particles or axionic dark matter. The axion production via the Peccei-Quinn mechanism has axion-like particles created by Parker-type mechanisms in the early universe, contributing to the dark matter density.

### 5. Quantum Coherence and Entanglement

Modern research emphasizes that the created particle pairs are **quantum-entangled**. The creation process is coherent, not thermal (except for special cases like Hawking radiation). This entanglement is crucial for:

- Explaining the emergence of classicality in cosmology
- Understanding the arrow of time in cosmology
- Quantum teleportation tests using cosmological observables (speculative)

---

## Connection to Phonon-Exflation Framework

**DIRECT AND UNCONDITIONAL**: The Parker-Navarro-Salas review establishes the theoretical foundation for understanding the BCS transit in phonon-exflation as a finite-dimensional Parker-type creation mechanism.

### Framework-Specific Connections

1. **Pair Creation in Finite Dimensions**: Parker's formalism typically applies to infinite-dimensional field theory (infinitely many modes). The phonon-exflation framework applies it to the finite Dirac spectrum of the SU(3) geometry (16 fermionic modes after color quantization). The review discusses how finite-dimensional systems exhibit the same Bogoliubov mixing.

2. **Adiabatic Invariance and Time-Dependence**: The review emphasizes that particle creation depends crucially on the nonadiabaticity of the background geometry. In the framework, the parameter $\tau$ (related to the radius of compactification) evolves during exflation. This $\tau(t)$ is the analog of $a(t)$ in cosmology.

3. **Spectral Gaps and Resonance**: The review discusses how spectral gaps (forbidden frequencies) in expanding spacetimes create resonances and particle creation. In the framework, the Dirac gap Delta(tau) and the chemical potential mu(tau) play the role of spectral gaps. The van Hove singularity at M_max=1.674 (Session 35) is a finite-dimensional resonance.

4. **Quantum Entanglement of Pairs**: The review notes that created particle pairs are entangled (coherent state, not thermal). The BCS pairs in the framework carry K_7 charge and are entangled across the SU(3) sectors. The GGE permanence (Session 38) reflects the integrability-protected coherence predicted by the review.

5. **No Thermal Spectrum**: The review distinguishes Hawking thermal creation (black hole) from Parker coherent creation (cosmology). The phonon-exflation transit is identified as Parker-type: coherent, non-thermal, kinematic (driven by geometry alone). The review's emphasis on this distinction validates the framework's classification.

6. **Backreaction**: The review discusses how particle creation backreacts on the spacetime metric via the stress-energy tensor. In the framework, the instanton gas backreaction (3.7% perturbative correction) is an underdamped oscillation in the geometry, analogous to the cosmological backreaction.

7. **Connection to Schwinger's Pair Production**: The review mentions Schwinger's classical result on electron-positron pair production in strong electric fields. Session 38 of the framework discovered **Schwinger-instanton duality**: the WKB integral for instanton tunneling equals Schwinger's integral for pair production. The review provides the broader context for this duality.

### Quantitative Framework Tests

The review's discussion of preheating (broad-band parametric resonance) predicts exponential growth of created particles over timescales $\sim 100/\Gamma$ where $\Gamma$ is the decay width. In the framework:

- BCS instability: exponential growth of pairing amplitude with $\lambda_L / E_F \sim 10^{-3}$
- Timescale: $\tau_{\text{pairing}} \sim 0.1 \hbar / E_{\text{gap}}$
- Feshbach doorway resonance: detuning 2.9%, strong mixing (Session 38)

These map directly onto the preheating scenario, making the framework a finite-dimensional analog of parametric resonance.

### Open Question Flagged in Review

The review emphasizes an outstanding challenge: **how does macroscopic coherence arise from microscopic particle creation?** In inflation, quantum fluctuations (tiny, $\sim 10^{-5}$) are amplified to seed galaxies. The review notes this is not yet fully understood at the quantum-to-classical transition.

In phonon-exflation, the analogous question is: how do 59.8 created Cooper pairs (S38 result) drive a macroscopic geometric deformation of the SU(3) compactification? The framework's answer: integrability. The 8 Richardson-Gaudin conserved quantities prevent thermalization and dissipation, preserving the coherence of the pair vibration across cosmological timescales. This is a new answer to the review's century-old challenge.

---

## Supplementary: Timeline of Major Papers (1960s-2017)

- Parker (1966): Original thesis
- Parker (1969): Scalar fields in expanding universes
- Parker (1971): Massive vector fields
- Hawking (1974): Black hole radiation
- Guth (1981): Inflation proposal
- Parker (1985): Quantum Field Theory in Curved Spacetime (monograph)
- Albrecht-Steinhardt (1982): New inflationary model
- Linde (1983): Chaotic inflation
- Kofman, Linde, Riotto (1994): Preheating
- Boyle, Steinhardt, Turok (2006): Alternative to inflation (Ekpyrotic)
- Planck Collaboration (2018): CMB constraints on inflation
- Agullo, Singh (2016): Quantum corrections to cosmological particle creation
- Navarro-Salas, Alonso-Serrano (2017): Hawking effect as Unruh effect near black holes

---

## Notes on the 2014 Interview Format

The review is formatted as a detailed interview between Leonard Parker and the conference organizers, recorded during ERE2014 in Valencia. This format captures:

- Parker's own recollection of why he pursued the problem
- Unexpected discoveries during the derivation (e.g., conformal invariance of massless fields)
- Historical context: what problems were "hot" in 1966, what were speculative
- Personal perspective on the impact of the discovery
- Critique of early misunderstandings (e.g., initial confusion about Hawking radiation)
- Commentary on modern developments he finds most promising

The 2017 publication (arXiv submission) preserves this informal, authoritative voice while adding references to post-2014 developments.

