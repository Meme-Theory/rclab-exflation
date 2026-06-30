# Quantum Field Simulator for Dynamics in Curved Spacetime

**Author(s):** Celia Viermann, Marius Sparn, Nikolas Liebster, Maurus Hans, Elinor Kath, Alvaro Parra-Lopez, Mireia Tolosa-Simeon, Natalia Sanchez-Kuntz, Tobias Haas, Helmut Strobel, Stefan Floerchinger, Markus K. Oberthaler
**Year:** 2022
**Journal:** [INCOMPLETE - not extractable from PDF; appears to be a preprint/Nature Physics submission]
**arXiv:** 2202.10399
**Relevance:** HIGH

---

## Abstract

The observed large-scale structure in our Universe is seen as a result of quantum fluctuations amplified by spacetime evolution. This, and related problems in cosmology, asks for an understanding of the quantum fields of the standard model and dark matter in curved spacetime. Even the reduced problem of a scalar quantum field in an explicitly time-dependent spacetime metric is a theoretical challenge and thus a quantum field simulator can lead to new insights. Here, we demonstrate such a quantum field simulator in a two-dimensional Bose-Einstein condensate with a configurable trap and adjustable interaction strength to implement this model system. We explicitly show the realisation of spacetimes with positive and negative spatial curvature by wave packet propagation and confirm particle pair production in controlled power-law expansion of space. We find quantitative agreement with new analytical predictions for different curvatures in time and space. This benchmarks and thereby establishes a quantum field simulator of a new class. In the future, straightforward upgrades offer the possibility to enter new, so far unexplored, regimes that give further insight into relativistic quantum field dynamics.

---

## Key Arguments and Derivations

### Implementing Curved Spacetime in a BEC

The experiment realizes a 2D potassium-39 BEC ($\sim$23,000 atoms, $F=1$, $m_F=-1$) with configurable trap (digital micromirror device) and dynamically adjustable scattering length via Feshbach resonance at 562.2(1.5) G. The acoustic metric for phononic excitations takes the form:
$$ds^2 = -dt^2 + a^2(t)\left(\frac{du^2}{1 - \kappa u^2} + u^2\,d\varphi^2\right)$$

This is the standard (2+1)-dimensional FLRW metric in reduced circumference coordinates, parametrized by intrinsic spatial curvature $\kappa$ and a time-dependent scale factor $a(t)$.

### Spatial Curvature from Density Profiles

The acoustic metric on a 2D condensate with azimuthal symmetry is $ds^2 = -dt^2 + c_s^{-2}(dr^2 + r^2\,d\varphi^2)$ with $c_s^2 = \lambda(t)n_0(r)/m$. A hyperbolic geometry ($\kappa < 0$) is achieved with density profile $n_0(r) = \bar{n}_0[1 - r^2/R^2]^2$, giving $\kappa = -2/R_{\mathrm{TF}}^2$ (Thomas-Fermi radius). A parabolic Thomas-Fermi profile (harmonic trap) naturally approximates this in the central region with $R = \sqrt{2}R_{\mathrm{TF}}$.

Positive spatial curvature ($\kappa > 0$, spherical geometry) is implemented with density profile $n_0(r) = \bar{n}_0[1 + r^2/R^2]^2$, shaped by the DMD.

Wave packet propagation experiments confirm the geodesic structure: packets follow geodesics of the underlying metric, with quantitative agreement between predictions for the hyperbolic metric and the observed propagation (deviations only near $R_{\mathrm{TF}}$).

### Time-Dependent Metric: Expanding Space

The scale factor is related to the scattering length via:
$$a^2(t) = \sqrt{\frac{m^3}{8\pi\omega_z\hbar^3\bar{n}_0^2}}\frac{1}{a_s(t)}$$

where $\omega_z = 2\pi \times 1.6$ kHz is the tight-confinement trap frequency and $\bar{n}_0 = 1.3 \times 10^9$ cm$^{-2}$ is the central 2D density. Expanding space is implemented by decreasing $a_s(t)$ (via the Feshbach resonance magnetic field), with the radial trap frequency adjusted to maintain constant density.

### Particle Pair Production

Power-law ramps $a(t) \propto t^\gamma$ simulate different expansion histories:
- $\gamma = 0.5$: decelerating universe
- $\gamma = 1.0$: uniformly expanding universe
- $\gamma = 1.5$: accelerating universe

Ramps from $a_s = 400\,a_B$ to $50\,a_B$ produce enhanced density fluctuations visible in individual realizations. The density contrast:
$$\delta c(x,y) = \sqrt{\frac{n_0(x,y)}{\bar{n}_0^3}}[n(x,y) - n_0(x,y)]$$

is proportional to $\dot{\phi}$ for a massless relativistic scalar field $\phi$ in the curved spacetime governed by the effective action $\Gamma = -(\hbar^2/2)\int dt\,du\,d\varphi\,\sqrt{g}\,g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi$.

### Correlation Analysis and Sakharov Oscillations

The $\delta c$-$\delta c$ correlation function, averaged over all pixel pairs at given hyperbolic distance, reveals:
- Clear anti-correlation at $\sim$5 $\mu$m after expansion ($\gamma = 0.5$), absent before the ramp.
- Correlation features propagate outward at $v = 2.5(1)$ $\mu$m/ms = twice the speed of sound (consistent with paired excitations moving in opposite directions).
- These are real-space Sakharov oscillations.

**Heterodyne detection** (interference between phonon modes and background condensate) reveals mode-by-mode oscillations at frequency $2\omega_k = 2c_s k$ during hold time $t_h$ after the ramp. Fitting $f_k(t_h) = A_k\cos(2\omega_k t_h + \vartheta_k) + \mathrm{const}$:
- Amplitude $A_k$ and phase $\vartheta_k$ show quantitative agreement with analytical theory for a free massless relativistic scalar field in (2+1)-dimensional expanding spacetime.
- For $\gamma = 1.0$ and $\gamma = 1.5$, a phase jump is present that is absent for $\gamma = 0.5$. This feature is temperature-independent and thus an ideal indicator of expansion history.
- Theory uses final $c_s = 1.2$ $\mu$m/ms at $a_s = 50\,a_B$, initial $a_s = 350\,a_B$, initial temperature $T = 40$ nK (vs. independently measured 60(10) nK; discrepancy attributed to thermal excitation expulsion from condensate center).

---

## Key Results

1. First successful implementation of a relativistic scalar quantum field in curved spacetime as a quantum field simulator.
2. Both positive and negative spatial curvature realized in a BEC by configuring the density profile (harmonic trap for hyperbolic; DMD-shaped for spherical).
3. Particle pair production confirmed in power-law expanding spacetimes with quantitative agreement between experiment and analytical theory.
4. Sakharov oscillations observed in both real-space correlations and momentum-space heterodyne signals.
5. Phase jump in heterodyne signal distinguishes accelerating from decelerating expansion -- a temperature-independent probe of expansion history.
6. Correlation features propagate at twice the speed of sound, confirming paired excitation interpretation.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FLRW metric (2+1D) | $ds^2 = -dt^2 + a^2(t)[\frac{du^2}{1 - \kappa u^2} + u^2\,d\varphi^2]$ | Eq. (1) |
| Scale factor vs scattering length | $a^2(t) = \sqrt{m^3/(8\pi\omega_z\hbar^3\bar{n}_0^2)}\cdot 1/a_s(t)$ | Eq. (2) |
| Density contrast | $\delta c = \sqrt{n_0/\bar{n}_0^3}[n - n_0]$ | Eq. (3) |
| Effective action | $\Gamma = -(\hbar^2/2)\int dt\,du\,d\varphi\,\sqrt{g}\,g^{\mu\nu}\partial_\mu\phi\,\partial_\nu\phi$ | Eq. (4) |
| Acoustic metric (2D BEC) | $ds^2 = -dt^2 + c_s^{-2}(dr^2 + r^2\,d\varphi^2)$ | Eq. (5) |
| Speed of sound | $c_s^2 = \lambda(t)n_0(r)/m$ | Eq. (6) |
| Hyperbolic metric | $ds^2 = -dt^2 + a^2(t)(1 - r^2/R^2)^{-2}(dr^2 + r^2\,d\varphi^2)$ | Eq. (7) |
| Coordinate transform | $u(r) = r/(1 - r^2/R^2)$ | Eq. (8) |
| Hyperbolic distance | $L = \frac{1}{\sqrt{|\kappa|}}\cosh^{-1}[\sqrt{|\kappa|}u^2 + 1)\cdot(\sqrt{|\kappa|}u'^2 + 1) - |\kappa|uu'\cos(\varphi - \varphi')]$ | Eq. (9) |
| Sakharov oscillation fit | $f_k(t_h) = A_k\cos(2\omega_k t_h + \vartheta_k) + \mathrm{const}$ | Text |

---

## Relevance to Phonon-Exflation

This paper provides direct experimental evidence that phononic excitations in a BEC undergo cosmological particle pair production when the effective metric expands -- the same physical mechanism posited by the phonon-exflation framework. The key formula $a^2 \propto 1/a_s$ maps the BEC scattering length to cosmological scale factor, paralleling the framework's mapping of SU(3) fiber modulus $\tau$ to expansion. The observation of Sakharov oscillations and their quantitative agreement with QFT in curved spacetime validates the analogue gravity programme experimentally. The phase jump discriminant between accelerating and decelerating expansion demonstrates that expansion history is encoded in the quantum state of the phonon field -- relevant to the framework's prediction that the GGE (generalized Gibbs ensemble) relic from fiber transit carries permanent information about the transit dynamics.
