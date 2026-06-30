# Analogue Models for FRW Cosmologies

**Author(s):** Carlos Barcelo, Stefano Liberati, Matt Visser
**Year:** 2003
**Journal:** Gravity Research Foundation essay (honorable mention)
**arXiv:** gr-qc/0305061
**Relevance:** HIGH

---

## Abstract

It is by now well known that various condensed matter systems may be used to mimic many of the kinematic aspects of general relativity, and in particular of curved-spacetime quantum field theory. In this essay we will take a look at what would be needed to mimic a cosmological spacetime -- to be precise a spatially flat FRW cosmology -- in one of these analogue models. In order to do this one needs to build and control suitable time dependent systems. We discuss here two quite different ways to achieve this goal. One might rely on an explosion, physically mimicking the big bang by an outflow of whatever medium is being used to carry the excitations of the analogue model, but this idea appears to encounter dynamical problems in practice. More subtly, one can avoid the need for any actual physical motion (and avoid the dynamical problems) by instead adjusting the propagation speed of the excitations of the analogue model. We shall focus on this more promising route and discuss its practicality.

---

## Key Arguments and Derivations

### Two Routes to Analogue FRW

The paper begins with the generic analogue effective metric:
$$ds^2_{\mathrm{effective}} = \frac{\rho}{c_s}\left[-\left(c_s^2 - v^2\right)dt^2 - 2\mathbf{v}\cdot dt\,d\mathbf{x} + d\mathbf{x}^2\right]$$

and asks: how close can this come to reproducing a spatially flat FRW metric $ds^2_{\mathrm{FRW}} = -c^2\,dt^2 + a(t)^2\,d\mathbf{x}^2$?

**Route 1: Explosion.** Substituting $\mathbf{z} = b(t)\mathbf{x}$, introducing $H_b = \dot{b}/b$, the FRW metric transforms to a form matching the effective metric with $\mathbf{v} \leftrightarrow H_b\mathbf{z}$, $c_s \leftrightarrow (b/a)c$, $\rho/c_s \leftrightarrow a^2/b^2$. The continuity equation gives $\rho \propto 1/b^3$ and $c_s \propto 1/(a^2 b)$. Problem: the linearly rising velocity field guarantees an apparent horizon (a spherical surface where fluid speed exceeds sound speed), introducing dynamical complications not intrinsic to the FRW geometry.

**Route 2: Varying propagation speed (preferred).** With the medium at rest ($\mathbf{v} = 0$), constant $\rho$, and time-varying $c_s(t)$:
$$ds^2_{\mathrm{effective}} = \frac{c_0}{c_s(t)}\left[-c_s^2(t)\,dt^2 + d\mathbf{x}^2\right] = -c_0 c_s(t)\,dt^2 + \frac{c_0}{c_s(t)}\,d\mathbf{x}^2$$

Introducing pseudo-time $d\tau = dt\sqrt{c_s(t)/c_0}$ and scale factor $a(\tau)^2 = c_0/c_s(t)$:
$$ds^2_{\mathrm{effective}} = -c_0^2\,d\tau^2 + a(\tau)^2\,d\mathbf{x}^2$$

This is an exact spatially flat FRW cosmology. An expanding universe corresponds to decreasing $c_s$.

### Inflationary Solution

The analogue Hubble factor is $H = -\frac{1}{2}\sqrt{c_0/c_s}\,\dot{c}_s/c_s$. The inflationary (de Sitter) solution $a(\tau) = e^{H\tau}$ corresponds to a power law in physical time for the speed of sound: $c_s(t) = c_0/(H^2 t^2)$.

### Physical Mechanism: Feshbach Resonance in BEC

In a BEC, the speed of sound satisfies $c_s^2 \propto \sigma$ where $\sigma$ is the s-wave scattering length. Feshbach resonances allow $\sigma$ to be tuned at will via an external magnetic field. This provides a physical mechanism to control $c_s(t)$.

The key constraint is the Markovian approximation: timescales of external parameter changes must be longer than the two-body collisional duration. The authors estimate the interaction timescale as $t_i = \lambda_{\mathrm{vdW}} m R/h \approx 10^{-6}$ s (for a typical BEC with $\lambda_{\mathrm{vdW}} \sim 1$ nm, trap size $R \sim 10$ $\mu$m), so changes in $\sigma$ faster than $\sim 1$ $\mu$s violate the GP equation validity.

### Analogue Cosmological Particle Creation

The ratio $t_i/t_{\mathrm{size}} = 2\pi\lambda_{\mathrm{vdW}}/\xi \approx 10^{-2}$--$10^{-4}$ (where $\xi = \hbar/(mc_s)$ is the healing length) shows a viable window: timescales exist for which both the GP equation holds and quasi-particles are produced with wavelengths shorter than the condensate size. The peak frequency of created quasi-particles is $\nu_{\mathrm{peak}} \approx 1/t_{\mathrm{min}}$.

At short wavelengths (comparable to healing length), the Bogoliubov dispersion relation $\omega = \sqrt{c_s^2 k^2 + (\hbar k^2/2m)^2}$ replaces the linear phononic dispersion, providing a natural UV modification relevant to the trans-Planckian debate for inflationary perturbations.

---

## Key Results

1. A spatially flat FRW cosmology is exactly reproduced by a static medium with time-varying propagation speed, with no conformal factor mismatch.
2. The explosion route, while mathematically valid, is dynamically problematic due to the inevitable formation of an apparent horizon.
3. Feshbach resonances in BECs provide a practical mechanism for controlling $c_s(t)$ to simulate cosmological expansion.
4. A viable experimental window exists ($t_i/t_{\mathrm{size}} \sim 10^{-2}$--$10^{-4}$) for cosmological particle production in BECs.
5. Building an analogue FRW cosmology appears considerably less problematic than building an analogue black hole.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FRW metric | $ds^2_{\mathrm{FRW}} = -c^2\,dt^2 + a(t)^2\,d\mathbf{x}^2$ | Eq. (1) |
| Effective metric (generic) | $ds^2 = \frac{\rho}{c_s}[-(c_s^2 - v^2)dt^2 - 2\mathbf{v}\cdot dt\,d\mathbf{x} + d\mathbf{x}^2]$ | Eq. (2) |
| Explosion: Hubble-like parameter | $H_b(t) = \dot{b}(t)/b(t)$ | Eq. (4) |
| Varying $c_s$: effective metric | $ds^2 = -c_0 c_s(t)\,dt^2 + (c_0/c_s(t))\,d\mathbf{x}^2$ | Eq. (10) |
| Scale factor identification | $a(\tau)^2 = c_0/c_s(t)$ | Eq. (12) |
| Analogue Hubble factor | $H = -\frac{1}{2}\sqrt{c_0/c_s}\,\dot{c}_s/c_s$ | Eq. (14) |
| Inflationary $c_s$ | $c_s(t) = c_0/(H^2 t^2)$ | Eq. (16) |
| GP equation | $-i\hbar\partial_t\psi = (-\frac{\hbar^2}{2m}\nabla^2 + V_{\mathrm{ext}} + \kappa|\psi|^2)\psi$ | Eq. (17) |
| BEC speed of sound | $c_s^2 \propto \sigma$ (scattering length) | Eq. (18) |
| Interaction timescale | $t_i = \lambda_{\mathrm{vdW}} m R/h \approx 10^{-6}$ s | Eq. (19) |
| Timescale ratio | $t_i/t_{\mathrm{size}} = 2\pi\lambda_{\mathrm{vdW}}/\xi \approx 10^{-2}$--$10^{-4}$ | Eq. (21) |
| Bogoliubov dispersion | $\omega = \sqrt{c_s^2 k^2 + (\hbar k^2/(2m))^2}$ | Eq. (22) |

---

## Relevance to Phonon-Exflation

This paper provides the specific construction used by the phonon-exflation framework: an expanding FRW cosmology arises from decreasing the effective speed of sound in a static condensate. The framework's mechanism -- internal compactification of the SU(3) fiber changes the effective propagation speed of phononic excitations -- is a higher-dimensional realization of this exact analogue. The identification $a^2 \propto 1/c_s$ maps directly to the exflation picture where fiber compaction (increasing $\tau$) reduces the phonon speed and generates cosmological expansion. The Feshbach resonance mechanism demonstrates experimental controllability of the analogue, and the Bogoliubov dispersion provides the UV completion that the framework's BCS instanton physics extends to the full nonperturbative regime.
