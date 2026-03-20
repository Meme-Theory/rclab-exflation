# Fifty Years of Cosmological Particle Creation

**Author(s):** Leonard Parker, Jose Navarro-Salas

**Year:** 2017

**Journal:** Journal of Physics: Conference Series (ERE2014 proceedings)

**arXiv:** 1702.07132 [physics.hist-ph]

---

## Abstract

This historical interview documents Leonard Parker's foundational discovery that the expansion of the universe creates particles out of the quantum vacuum. The paper reviews five decades of developments in the theory of quantum particle creation in curved spacetime, from Parker's original 1966 analysis through modern applications to inflation, Hawking radiation, and analog gravity. The authors discuss the trans-Planckian problem—the question of whether modes at scales smaller than the Planck length have physical meaning in inflationary cosmology—and trace the connections between Parker's work and contemporary approaches to quantum gravity.

---

## Historical Context

In 1966, Leonard Parker made a revolutionary discovery: **the expansion of spacetime itself can create particles**. Before Parker, it was believed that the quantum vacuum was truly empty (except for virtual fluctuations); only matter fields could interact with the expanding background. Parker showed that this is incorrect. A quantum field in a time-dependent (expanding) spacetime is not in a definite particle eigenstate. What appears as "vacuum" at early times evolves into a state containing real, on-shell particles at late times.

This phenomenon arises because the notion of "particle" is observer-dependent in curved spacetime. Unlike in flat Minkowski space where the definition of particle is universal (via Fourier modes), in an expanding universe the "in" vacuum (early times) and "out" vacuum (late times) are orthogonal Fock states. The overlap between them is less than 1, indicating particle creation.

The discovery opened a new field of research with profound implications:

- **Inflation**: Primordial density perturbations responsible for CMB anisotropies arise from quantum fluctuations amplified by Parker particle creation.
- **Hawking Radiation**: Particle creation near black hole horizons is a specific case of Parker's general mechanism.
- **Analog Gravity**: Laboratory systems (BEC, Casimir effect, metamaterials) realize Parker particle creation in controlled settings.
- **Trans-Planckian Modes**: The question of whether high-frequency modes (above Planck scale) contribute to observable effects remains unresolved after 50 years.

For the phonon-exflation framework, Parker's work is **directly applicable**: the instanton-mediated particle creation (S38) is a realization of Parker's mechanism in the internal SU(3) geometry.

---

## Key Arguments and Derivations

### The Bogoliubov Transformation

The central mathematical tool in Parker's analysis is the **Bogoliubov transformation** relating creation/annihilation operators in different coordinate systems. For a scalar field $\phi$ in an expanding universe with scale factor $a(t)$:

In comoving coordinates, the field is decomposed as:
$$\phi(t, \vec{x}) = \sum_k \left[ a_k u_k(t) e^{i\vec{k} \cdot \vec{x}} + a^\dagger_k u_k^*(t) e^{-i\vec{k} \cdot \vec{x}} \right]$$

where $u_k(t)$ is the mode function satisfying the Klein-Gordon equation in curved spacetime. At early times (in-vacuum, $t \to -\infty$), the in-vacuum state satisfies $a_k^{\text{in}} |\Omega^{\text{in}} \rangle = 0$. At late times (out-vacuum, $t \to +\infty$), the out-vacuum state satisfies $b_k^{\text{out}} |\Omega^{\text{out}} \rangle = 0$.

The crucial point is that $a_k^{\text{in}}$ and $b_k^{\text{out}}$ are **different operators**. The relationship between them is given by the Bogoliubov transformation:

$$b_k^{\text{out}} = \alpha_k a_k^{\text{in}} + \beta_k a_{-k}^{\text{in} \dagger}$$

where $\alpha_k$ and $\beta_k$ are Bogoliubov coefficients depending on the mode functions. The coefficients satisfy $|\alpha_k|^2 - |\beta_k|^2 = 1$ (normalization) and $|\beta_k|^2 = 0$ if and only if the in and out vacua coincide.

### Particle Creation Rate

The number of particles created in mode $k$ is:

$$N_k = \langle \Omega^{\text{out}} | b_k^{\text{out} \dagger} b_k^{\text{out}} | \Omega^{\text{out}} \rangle = |\beta_k|^2$$

The total particle number is:

$$N_{\text{total}} = \sum_k |\beta_k|^2 = \int_0^\infty \frac{dk}{(2\pi)^2} k^2 |\beta_k(t_f)|^2$$

For an adiabatic (slowly varying) background, $|\beta_k|^2 \sim e^{-2\pi k/\omega}$ where $\omega$ is the adiabatic parameter (related to the time scale of variation of $a(t)$). Particles are suppressed when $k$ is small (long wavelengths, easily adjust to expansion) and enhanced for $k$ near $\omega$ (resonant modes).

### Applications to FRW Cosmology

For a Friedmann-Robertson-Walker universe with scale factor $a(t)$, the Klein-Gordon equation becomes:

$$u''_k + \left[ \frac{k^2}{a^2} + m^2 + \xi R \right] u_k = 0$$

where $\xi$ is the coupling to curvature scalar $R$, and primes denote derivatives with respect to conformal time. In the early universe (inflation), $a(t) \sim e^{Ht}$ with $H$ (Hubble parameter) nearly constant. The solution splits into:

1. **Short-wavelength modes** ($k \gg aH$): Follow their flat-space oscillation, essentially no creation.
2. **Long-wavelength modes** ($k \ll aH$): Freeze out during inflation due to Hubble friction, then oscillate classically after inflation ends.

The number of particles created is related to the ratio:

$$\mathcal{N} \sim \int d^3 k \, |\beta_k|^2 \propto \left( \frac{H}{\text{cutoff}} \right)^3 \times (\text{duration of expansion})$$

where $H$ is the Hubble scale during the epoch of particle creation.

### The Trans-Planckian Problem

A critical unresolved issue is: **What is the high-frequency cutoff?** During inflation, modes are continuously redshifted by the expansion. A mode that is presently observed (with wavelength $\lambda \sim 10^{27}$ m) had a much shorter wavelength at earlier times. If we extrapolate back to the Planck epoch, the wavelength becomes $\lambda_P \sim 10^{-35}$ m.

The question is: **Do modes with wavelength shorter than Planck length have physical meaning?** If not, the natural cutoff is $k_{\max} \sim 1/\ell_P$. But then the ultra-high-frequency fluctuations are artificially suppressed, and the predicted CMB power spectrum may differ from observation.

Parker's resolution (developed with collaborators) is that the particle creation is **robust to the trans-Planckian cutoff**. Different choices of cutoff (whether at Planck scale, some higher scale, or no cutoff at all) yield CMB predictions that agree to within percent levels—indicating that the measurable physics is independent of trans-Planckian modes.

### Analog Gravity Connection

Parker's mechanism can be realized in laboratory systems:

1. **Hawking Radiation in BEC** (Steinhauer et al., Paper #26): A sonic horizon in a flowing Bose-Einstein condensate mimics the event horizon of a black hole. Particles created near the horizon have the thermal spectrum predicted by Hawking (and by Parker's general mechanism).

2. **Dynamical Casimir Effect** (Wilson et al.): A moving mirror in a cavity creates real photons from vacuum, precisely as Parker's formalism predicts.

3. **Cosmological Particle Creation in Metamaterials** (Shvarts et al.): Engineered materials with time-varying refractive index can create photons, analog to cosmological expansion creating particles.

The success of these analogs strongly supports Parker's theoretical predictions.

---

## Key Results

1. **Expansion Creates Particles**: The expansion of spacetime itself, through its effect on the definition of "particle state," creates real, on-shell quanta from the vacuum. This is NOT virtual pair creation (Dirac sea picture) but genuine particle production.

2. **Bogoliubov Mechanism is Universal**: The creation mechanism is described by Bogoliubov transformations in ANY expanding spacetime geometry, whether FRW, inflation, scalar field collapse, or other scenarios.

3. **Trans-Planckian Modes are Benign**: The high-frequency trans-Planckian modes that formally appear in the loop integrals do NOT dominate the particle creation rate. Physical observables (CMB power, relic particle densities) are stable under trans-Planckian cutoff changes.

4. **Adiabatic Modes Survive**: Modes that vary slowly (adiabatically) with the background avoid particle creation. In inflation, modes with $k < aH$ are non-adiabatic and create particles; modes with $k > aH$ remain in ground state.

5. **Hawking Radiation is a Special Case**: Particle creation near black hole horizons (Hawking radiation) is a special case of Parker's mechanism where the Bogoliubov coefficient $|\beta_k|^2$ leads to thermal spectrum $\propto 1/(e^{\hbar \omega / k_B T} - 1)$.

6. **Analog Gravity Experiments Confirm Predictions**: Laboratory realizations (BEC sonic horizons, Casimir cavities, metamaterials) produce particle spectra matching Parker's theoretical predictions to within measurement precision.

---

## Impact and Legacy

Parker's discovery reshaped modern cosmology and quantum gravity:

- **Inflation Theory Foundation** (Guth 1981, Linde 1986, Starobinsky 1980): Inflationary perturbations are Parker-created particles, explaining the near-scale-invariance of density perturbations.

- **Hawking Radiation Unified** (Hawking 1974): Hawking's radiation is understood as Parker's mechanism applied to the geometrically singular region near a black hole.

- **Quantum Field Theory in Curved Spacetime** (Wald 1994 textbook): Became a core subject, with Parker's work foundational.

- **Analog Gravity Programs** (Unruh 1981 onwards): Vindicated Parker by showing his predictions are robust enough to appear in laboratory systems.

- **Cosmological Relics** (Kolb, Wolfram 1985 onwards): Particle creation produces dark matter candidates (axions, sterile neutrinos, others).

- **Black Hole Evaporation** (Hawking 1974, Page 1976, modern island formula): The total evaporation time and information content depend on Parker's creation rate.

---

## Framework Relevance

**Direct Connection to Instanton-Mediated Particle Creation (S38)**

The phonon-exflation framework's mechanism (S38) is a realization of Parker's general principle applied to internal geometry:

$$\text{Expansion of SU(3) fiber} \rightarrow \text{Particle creation in internal space} \rightarrow \text{External observer sees 4D particles}$$

Specifically:

1. **Order Parameter Evolution as Expansion**: The $\tau$ coordinate evolves from $\tau=0$ (flat SU(3), maximum symmetry) to $\tau \sim 0.28$ (curved SU(3), broken symmetries). This is analogous to the expansion of M^4, but in the internal space.

2. **Bogoliubov Transformation in K_7 Sector**: The Cooper pair creation (S35) via Schwinger instantons is governed by Bogoliubov coefficients. The "in" vacuum is the free-electron state; the "out" vacuum is the paired BCS state. The overlap $|\beta|^2$ measures pair creation probability:
$$|\beta|^2 = \left| \langle \text{BCS} | \text{free electron} \rangle \right|^2 \propto e^{-S_{\text{inst}}}$$
where $S_{\text{inst}} = 0.069$ (S38 result).

3. **Trans-Planckian Problem is Irrelevant**: The framework operates at scales much larger than Planck length (order parameter $\tau \sim 0.28$ is geometric, not stringy). Parker's robustness to trans-Planckian cutoffs is automatically satisfied—the framework's "high-energy" modes are still far below Planck scale.

4. **GGE as Out-Vacuum**: The post-transit state (S38) is a generalized Gibbs ensemble (GGE) with 8 Richardson-Gaudin conserved integrals. This is the "out-vacuum" analog: it is NOT thermal (not Boltzmann distributed), just as the Hawking radiation vacuum is not thermal in the usual sense (it is a thermal distribution as seen by infalling observers, but a squeezed state as seen by asymptotic observers).

5. **Instanton Worldlines as Parker Expansion Trajectory**: The worldlines of instantons in Euclidean time trace out the expansion of the internal geometry. The density of instantons ($n_{\text{inst}} \sim e^{-S_{\text{inst}}}$) controls the particle creation rate:
$$N_{\text{pairs}} = n_{\text{inst}} \times V_{\text{internal}} \times (\text{duration}) \propto e^{-0.069} \approx 93\%$$
(S38 gave $\approx 59$ pairs in a small volume, consistent with dense gas)

**Connection to Paper #23 (Islands in Cosmology)**

Parker's creation mechanism generates entanglement between the "in" and "out" vacua (the Bogoliubov coefficients encode this). In modern language (Hartman et al. 2020), this entanglement is encoded in an island. The framework's instanton gas may admit a similar island structure:
$$S_{\text{gen}}(\text{island in } SU(3)) = \frac{\text{Area}_{\text{SU(3)}}}{4 G_N} + S_{\text{vN}}(\text{paired electrons})$$

**Connection to Paper #25 (This Paper)**

Parker's formalism applies directly to the framework's particle creation. The framework is a concrete realization of cosmological (not black hole) particle creation in an internal-space geometry.

**Connection to Paper #26 (Steinhauer et al., Analog Hawking Radiation)**

The framework's mechanism is an "inverse analog": while Steinhauer et al. create Hawking radiation in a BEC with sonic horizon, the framework creates particles via internal-geometry expansion in a system that otherwise looks like flat spacetime. Both validate Parker's theory.

**Current Framework Status**

S38 confirmed Parker's mechanism in the framework's internal geometry. A natural follow-up (S44+) is to:
- Compute the full Bogoliubov transformation $\alpha_k, \beta_k$ as functions of $\tau$
- Verify trans-Planckian robustness (show that UV cutoff choices don't affect the GGE relic)
- Calculate the entanglement spectrum of the post-transit state (islands, if they form)
- Test analog gravity predictions: does a dual "acoustic" system (e.g., phonons in the SU(3) lattice) produce the same spectrum?
