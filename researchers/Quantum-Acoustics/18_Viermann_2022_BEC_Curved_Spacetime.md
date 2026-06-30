# Quantum Field Simulator for Dynamics in Curved Spacetime

**Author(s):** Celia Viermann, Marius Sparn, Nikolas Liebster, Maurus Hans, Elinor Kath, Alvaro Parra-Lopez, Mireia Tolosa-Simeon, Natalia Sanchez-Kuntz, Tobias Haas, Helmut Strobel, Stefan Floerchinger, Markus K. Oberthaler
**Year:** 2022
**Journal:** Nature (2022)
**arXiv:** 2202.10399
**Relevance:** CRITICAL

---

## Abstract

The observed large-scale structure in our Universe is seen as a result of quantum fluctuations amplified by spacetime evolution. This, and related problems in cosmology, asks for an understanding of the quantum fields of the standard model and dark matter in curved spacetime. Even the reduced problem of a scalar quantum field in an explicitly time-dependent spacetime metric is a theoretical challenge and thus a quantum field simulator can lead to new insights. Here, we demonstrate such a quantum field simulator in a two-dimensional Bose-Einstein condensate with a configurable trap and adjustable interaction strength to implement this model system. We explicitly show the realisation of spacetimes with positive and negative spatial curvature by wave packet propagation and confirm particle pair production in controlled power-law expansion of space. We find quantitative agreement with new analytical predictions for different curvatures in time and space. This benchmarks and thereby establishes a quantum field simulator of a new class. In the future, straightforward upgrades offer the possibility to enter new, so far unexplored, regimes that give further insight into relativistic quantum field dynamics.

---

## Key Arguments and Derivations

### 1. Acoustic Metric from BEC Density

Building on Unruh's 1980 insight that sound waves in a convergent fluid flow are analogous to quantum fields in a gravitational field, the authors show that a static but spatially inhomogeneous superfluid provides a curved spacetime metric for phononic excitations. The acoustic metric in a BEC is:

$$ds^2 = -dt^2 + \frac{1}{c_s^2}(dr^2 + r^2 d\varphi^2)$$

where $c_s$ is the time- and space-dependent speed of sound. Spatial curvature is controlled by the density distribution; temporal metric evolution is controlled by tuning the s-wave scattering length $a_s(t)$.

### 2. FLRW Metric Implementation

The experiment implements a (2+1)-dimensional FLRW metric:

$$ds^2 = -dt^2 + a^2(t)\left(\frac{du^2}{1 - \kappa u^2} + u^2 d\varphi^2\right)$$

with independently adjustable spatial curvature $\kappa$ and scale factor $a(t)$. This is achieved in a two-dimensional potassium-39 BEC with $\sim$23,000 atoms.

### 3. Hyperbolic Geometry ($\kappa < 0$)

A harmonically trapped BEC with parabolic Thomas-Fermi density profile naturally implements negative spatial curvature $\kappa = -2/R_{TF}^2$ in its central region. The density profile $n_0(r) = \bar{n}_0[1 - r^2/R^2]^2$ yields a hyperbolic metric. Through the Poincare transformation, the infinite hyperbolic space is mapped to a finite disc, well-suited for finite-size ultracold gases.

Wave packet propagation along geodesics of this metric is observed, with quantitative agreement between theory and experiment. The speed of sound and Thomas-Fermi radius ($R_{TF} = 25\,\mu$m, $c_s = 1.5\,\mu$m/ms) completely determine the metric.

### 4. Spherical Geometry ($\kappa > 0$)

Positive curvature is implemented using a digital micromirror device (DMD) to configure a density profile $n_0(r) = \bar{n}_0[1 + r^2/R^2]^2$ with maximal density at the rim. Wave packets exhibit fundamentally different evolution (straightening) compared to hyperbolic case, confirming successful implementation.

### 5. Expanding Space via Scattering Length

Time-dependence of the metric (extrinsic curvature) is implemented by dynamically controlling the s-wave scattering length $a_s(t)$ via a Feshbach resonance at 562.2(1.5) G in potassium-39. The scale factor relates to scattering length via:

$$a^2(t) = \sqrt{\frac{m^3}{8\pi \omega_z \hbar^3 \bar{n}_0^2}} \frac{1}{a_s(t)}$$

Decreasing $a_s$ is equivalent to expanding space (decreasing causal speed at fixed coordinates). The radial trap frequency is adjusted simultaneously to keep the density distribution constant.

### 6. Cosmological Particle Production

Power-law ramps $a(t) \propto t^\gamma$ are performed:
- $\gamma = 0.5$: decelerating universe
- $\gamma = 1.0$: uniformly expanding universe
- $\gamma = 1.5$: accelerating universe

After the ramp, enhanced density fluctuations appear -- the signature of particle pair production from the expanding metric. The phononic scalar field $\phi$ obeys the effective action:

$$\Gamma = -\frac{\hbar^2}{2}\int dt\, du\, d\varphi\, \sqrt{g}\, g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi$$

This is the minimal model for cosmological particle pair production (Parker-type creation).

### 7. Density Contrast and Correlation Functions

The experimentally accessible density contrast is defined as:

$$\delta_c(x,y) = \sqrt{\frac{n_0(x,y)}{\bar{n}_0^3}}\,[n(x,y) - n_0(x,y)]$$

This is proportional to $\dot{\phi}$ (time derivative of the scalar field). The $\delta_c$-$\delta_c$ correlation function, averaged over many realizations, shows clear anti-correlation at a length scale of $\sim$5 $\mu$m after decelerated expansion, with correlations propagating at $v = 2.5(1)\,\mu$m/ms = $2c_s$ (twice the speed of sound), as expected for pair-produced excitations.

### 8. Sakharov Oscillations and Expansion History

The spectral decomposition via Hankel transform reveals Sakharov oscillations in individual $k$-modes:

$$f_k(t_h) = A_k \cos(2\omega_k t_h + \vartheta_k) + \text{const}$$

with $\omega_k = c_s k$. The amplitude $A_k$ and phase $\vartheta_k$ encode the expansion history. The power spectrum at non-zero temperature is:

$$S_k(t) = \left[\frac{1}{2} + |\beta_k|^2 + |\alpha_k\beta_k|\cos(\theta_k + 2\omega_k t)\right](1 + 2N_k^{\text{in}})$$

where $\alpha_k$, $\beta_k$ are Bogoliubov coefficients determined by the expansion history, $1/2$ is vacuum fluctuations, $|\beta_k|^2$ is particle production, and $N_k^{\text{in}}$ is the initial thermal distribution.

A phase jump exists for $\gamma = 1.0$ (uniform) and $\gamma = 1.5$ (accelerated) expansion but NOT for $\gamma = 0.5$ (decelerated). This feature is temperature-independent and thus an ideal indicator for expansion history.

### 9. Quantitative Agreement

The analytical predictions use a final sound speed $c_s = 1.2\,\mu$m/ms at $a_s = 50\,a_B$, initial $a_s = 350\,a_B$, and initial temperature $T = 40\,$nK (experimental: $T = 60(10)\,$nK; deviation attributed to thermal excitations being expelled from the condensate center). Both amplitude and phase of Sakharov oscillations show quantitative agreement with theory for all three expansion histories, confirming particle pair production from the expanding metric.

---

## Key Results

1. First successful implementation of a quantum field simulator for a relativistic scalar field in curved spacetime.
2. Explicit demonstration of both positive ($\kappa > 0$, spherical) and negative ($\kappa < 0$, hyperbolic) spatial curvature via BEC density engineering.
3. Confirmed cosmological particle pair production from controlled power-law expansion $a(t) \propto t^\gamma$ for three different expansion histories ($\gamma = 0.5, 1.0, 1.5$).
4. Quantitative agreement between experiment and analytical predictions for both amplitude and phase of Sakharov oscillations.
5. Phase jump in Sakharov oscillations distinguishes accelerated/uniform from decelerated expansion, independent of temperature.
6. Correlation propagation at $2c_s$ confirmed as signature of pair-produced quasiparticles.
7. Expansion history is encoded in the produced quantum state and can be extracted via heterodyne detection of individual $k$-modes.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FLRW metric | $ds^2 = -dt^2 + a^2(t)\left(\frac{du^2}{1-\kappa u^2} + u^2 d\varphi^2\right)$ | Eq. (1) |
| Scale factor from $a_s$ | $a^2(t) = \sqrt{\frac{m^3}{8\pi\omega_z\hbar^3\bar{n}_0^2}}\frac{1}{a_s(t)}$ | Eq. (2) |
| Density contrast | $\delta_c(x,y) = \sqrt{\frac{n_0(x,y)}{\bar{n}_0^3}}[n(x,y) - n_0(x,y)]$ | Eq. (3) |
| Effective action | $\Gamma = -\frac{\hbar^2}{2}\int dt\,du\,d\varphi\,\sqrt{g}\,g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi$ | Eq. (4) |
| Acoustic metric | $ds^2 = -dt^2 + \frac{1}{c_s^2}(dr^2 + r^2 d\varphi^2)$ | Eq. (5) |
| Speed of sound | $c_s^2 = \lambda(t)n_0(r)/m$, $\lambda(t) = \sqrt{8\pi\omega_z\hbar^3/m}\,a_s(t)$ | Eq. (6) |
| Metric (lab coords) | $ds^2 = -dt^2 + a^2(t)(1 - r^2/R^2)^{-2}(dr^2 + r^2 d\varphi^2)$ | Eq. (7) |
| Coordinate transform | $u(r) = \frac{r}{1 - r^2/R^2}$ | Eq. (8) |
| Hyperbolic distance | $L(u,\varphi,u',\varphi') = \frac{1}{\sqrt{|\kappa|}}\cosh^{-1}[\sqrt{|\kappa|u^2+1}\sqrt{|\kappa|u'^2+1} - |\kappa|uu'\cos(\varphi-\varphi')]$ | Eq. (9) |
| Hankel spectrum | $S_k = \frac{\bar{n}_0 m}{\hbar a(t_f)}\frac{1}{k}\int dL\,L\,J_0(kL)\,\langle\delta_c\delta_c\rangle(L)$ | Eq. (10) |
| Power spectrum | $S_k(t) = [\frac{1}{2} + |\beta_k|^2 + |\alpha_k\beta_k|\cos(\theta_k + 2\omega_k t)](1 + 2N_k^{\text{in}})$ | Eq. (11) |
| Thermal distribution | $N_k^{\text{in}}(T) = \frac{1}{e^{\hbar\omega_k/(k_BT)} - 1}$ | Eq. (12) |
| Spatial curvature | $\kappa = -2/R_{TF}^2$ (harmonic trap) | Methods |

---

## Relevance to Phonon-Exflation

This is the most directly relevant paper in the Quantum-Acoustics corpus. The phonon-exflation framework claims that particles are phononic excitations of $M^4 \times SU(3)$ and that expansion is driven by internal compactification. This paper provides the first **experimental confirmation** of cosmological particle pair production (Parker-type creation) in a phononic system -- precisely the mechanism identified in Session 38 as the framework's particle creation channel ("Transit = Parker-type cosmological particle creation, NOT Hawking. No horizon = no thermal spectrum").

Key parallels:
- The BEC phonon field $\phi$ on an FLRW metric is the exact (2+1)D analog of the framework's phononic excitations on the evolving $M^4 \times SU(3)$ geometry.
- The scale factor $a(t)$ controlled by scattering length $a_s(t)$ parallels the tau-dependent coupling constants in the framework.
- The Bogoliubov coefficient structure $S_k \propto [1/2 + |\beta_k|^2 + |\alpha_k\beta_k|\cos\theta]$ is identical to the framework's particle production formalism.
- The phase jump distinguishing accelerated vs decelerated expansion could constrain the expansion history encoded in the framework's transit.
- The GGE (generalized Gibbs ensemble) prediction from Session 38 -- that the post-transit state never thermalizes due to integrability -- could in principle be tested in an extended version of this experiment by checking whether the produced quasiparticle distribution relaxes to thermal equilibrium.
- The experimental temperature $T = 40-60\,$nK and the finding that thermal excitations are expelled from the condensate center both parallel the framework's "cold big bang" vacuum floor scenario.
