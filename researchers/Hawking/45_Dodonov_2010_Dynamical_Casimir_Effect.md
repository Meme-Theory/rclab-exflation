# Current Status of the Dynamical Casimir Effect

**Author(s):** V. V. Dodonov
**Year:** 2010
**Journal:** Physica Scripta 82, 038105 (2010)
**arXiv:** 1004.3301
**Relevance:** MEDIUM

---

## Abstract

This is a brief review of different aspects of the so-called Dynamical Casimir Effect and the proposals aimed at its possible experimental realizations. A rough classification of these proposals is given and important theoretical problems are pointed out.

---

## Key Arguments and Derivations

### 1. Introduction and Classification

The Dynamical Casimir Effect (DCE), named by Yablonovitch and Schwinger, refers to photon generation from vacuum due to fast changes in the geometry or material properties of electrically neutral macroscopic or mesoscopic objects. The qualitative mechanism is parametric amplification of quantum vacuum fluctuations of the electromagnetic field in systems with time-dependent parameters.

Dodonov classifies DCE phenomena into two categories:
- **MI-DCE** (Mirror-Induced DCE): Photons created by movement of mirrors or changes in their material properties.
- **PA-DCE** (Parametric DCE): Photon creation via parametric amplification of vacuum fluctuations in media without moving boundaries.

The static Casimir effect has two ingredients: quantum fluctuations and boundaries. The DCE adds time-dependence to either the boundaries or the medium properties.

### 2. Single-Mode Theory

For a single harmonic oscillator with time-dependent frequency $\omega(t)$, the classical equation of motion:

$$\ddot{\varepsilon} + \omega^2(t)\varepsilon = 0$$

determines all quantum dynamical properties. For frequency changing from $\omega_i$ to $\omega_f$, the mean number of quanta created from an initial thermal state at temperature $\Theta$:

$$\langle N \rangle = G \left(\frac{|\dot{\varepsilon}|^2 + \omega_f^2|\varepsilon|^2}{4\omega_f} - \frac{1}{2}\right) = G \cdot R_T$$

where $G = \coth[\hbar\omega_i/(2k_B\Theta)]$, and $R \equiv |\rho_+/\rho_-|^2$ and $T \equiv 1-R \equiv |\rho_-|^{-2}$ are energy reflection and transmission coefficients from the effective "potential barrier" $\omega^2(t)$.

**Key constraints on single-mode DCE:**
- For monotonic frequency change: $R \leq (\omega_i - \omega_f)^2/(\omega_i + \omega_f)^2$ (Fresnel formula bound).
- Maximum photons in a single mode: $N_{\max} \sim (\Delta L/L)^2 \sim (v/c)^2$.
- The DCE is a second-order relativistic effect -- very few photons for non-relativistic motion.
- This rules out sonoluminescence as DCE: hydrodynamic timescales are adiabatic compared to optical frequencies.

**Parametric resonance.** For harmonic frequency variation $\omega(t) = \omega_0[1 + 2\kappa\cos(2\omega_0 t)]$ with $|\kappa| \ll 1$:

$$\langle N \rangle = \sinh^2(\omega_0 \kappa t)$$

With dissipation (quality factor $Q = \omega_0/(2\gamma)$), exponential growth requires $2Q\kappa > 1$.

### 3. Multi-Mode Theory: Effective Hamiltonian

For a cavity with time-dependent parameters, the field expands over instantaneous eigenfunctions. The effective Hamiltonian:

$$H = \frac{1}{2}\sum_\alpha \left[p_\alpha^2 + \omega_\alpha^2(\{L(t)\})q_\alpha^2\right] + \sum_{k=1}^n \frac{\dot{L}_k(t)}{L_k(t)} \sum_{\alpha \neq \beta} p_\alpha m_{\alpha\beta}^{(k)} q_\beta$$

where $m_{\alpha\beta}^{(k)} = -m_{\beta\alpha}^{(k)} = L_k \int dV \frac{\partial F_\alpha}{\partial L_k} F_\beta$ are antisymmetric coupling coefficients. This reduces the field problem to coupled oscillators with time-dependent frequencies and bilinear coupling.

**Key result for equidistant spectrum** ($\omega_n = c\pi n/L$, e.g. 1D cavity): Intermode coupling is "destructive" -- the number of photons in the $n$-th mode grows linearly, while the total number grows quadratically:

$$N_n \approx 8\kappa\omega_1 t/(\pi^2 n), \quad N_{\text{tot}} \approx 2(\kappa\omega_1 t)^2$$

The total energy grows exponentially: $E = (\hbar\omega_1/4)\sinh^2(2\kappa\omega_1 t)$.

### 4. Experimental Proposals

**4.1 Difficulties with Real Moving Boundaries.** For mechanical mirror oscillation: the maximum boundary velocity achievable is $v_{\max} \sim \delta_{\max} v_s \sim 50$ m/s (independent of frequency), giving $\Delta\omega < 10^3$ s$^{-1}$ in the microwave band. The quality factor must exceed $Q_{\min} \approx (L/\lambda) \cdot 4\pi c/(v_s\delta) \sim 10^8(L/\lambda)$.

**4.2 Semiconductor Schemes.** Yablonovitch proposed using laser pulses to create electron-hole plasma in a semiconductor slab inside a cavity, rapidly changing the effective cavity length. Short laser pulses can change the reflectivity on a femtosecond timescale, creating an "effective moving mirror" without mechanical motion. The photon rate depends on the plasma density and the rate of change of the dielectric constant.

**4.3 Thin Plasma Sheets (Lambrecht-Jaekel-Reynaud, 1996).** A thin plasma sheet inside a cavity, with time-varying number of free carriers, changes the effective boundary condition. This approach avoids the need for bulk material changes.

**4.4 Superconducting Circuits.** SQUID-based approaches: a superconducting transmission line terminated by a SQUID whose effective length is modulated by an external magnetic flux at GHz frequencies. This is the most promising experimental approach (and was subsequently confirmed experimentally by Wilson et al. 2011).

**4.5 Laser-Based Approaches for "Casimir Light."** Creating photons in the optical regime requires effective mirror velocities comparable to $c$, achievable through ultrafast changes in material properties. Proposals include using metamaterials or nonlinear crystals with time-varying refractive index.

### 5. Theoretical Problems

**Squeezing.** The DCE produces squeezed vacuum states. The variance of one quadrature can be reduced below the vacuum level while the other increases, a signature distinguishable from thermal noise.

**Finite Temperature.** At finite temperature, the vacuum contribution must be separated from the thermal contribution. The "stimulated" DCE (photon creation from thermal rather than vacuum fluctuations) could be much larger but must be distinguished from classical parametric amplification.

**Connection to Unruh and Hawking Effects.** The DCE, Unruh effect, and Hawking radiation are three manifestations of the same underlying physics: particle creation by time-dependent or observer-dependent backgrounds. The moving mirror model (Fulling-Davies 1976) provides the precise map: a mirror following a specific trajectory in flat spacetime produces radiation identical to Hawking radiation from a black hole.

**Decoherence and Backreaction.** The created photons can modify the boundary conditions (backreaction), and environmental coupling introduces decoherence of the squeezed state. Both effects limit the observability of quantum signatures.

---

## Key Results

1. The DCE is a second-order relativistic effect: $N \sim (v/c)^2$ for monotonic non-relativistic mirror motion, ruling out sonoluminescence as a DCE phenomenon.
2. Parametric resonance at frequency $2\omega_0$ can exponentially amplify vacuum fluctuations when $2Q\kappa > 1$, producing macroscopic photon numbers.
3. Intermode coupling in cavities with equidistant spectra is "destructive" -- photon production per mode is linear in time, but total photon number grows quadratically and total energy exponentially.
4. The effective Hamiltonian formulation reduces the field problem to coupled parametric oscillators, providing a unified theoretical framework.
5. Superconducting circuit approaches (SQUID-terminated transmission lines) are identified as the most promising experimental platform -- subsequently confirmed by Wilson et al. (2011).
6. The DCE, Unruh effect, and Hawking radiation are unified through the moving mirror / particle creation in curved spacetime framework.
7. The quantum signature of DCE is squeezed vacuum: sub-vacuum fluctuations in one quadrature, distinguishable from thermal radiation.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Classical oscillator equation | $\ddot{\varepsilon} + \omega^2(t)\varepsilon = 0$ | Eq. (2) |
| Mean photon number (thermal) | $\langle N \rangle = G \cdot R_T$ with $G = \coth[\hbar\omega_i/(2k_B\Theta)]$ | Eq. (3) |
| Parametric resonance | $\langle N \rangle = \sinh^2(\omega_0\kappa t)$ | Eq. (4) |
| Effective Hamiltonian | $H = \frac{1}{2}\sum_\alpha[p_\alpha^2 + \omega_\alpha^2 q_\alpha^2] + \sum_k \frac{\dot{L}_k}{L_k}\sum_{\alpha\neq\beta} p_\alpha m_{\alpha\beta}^{(k)} q_\beta$ | Eq. (5) |
| Coupling coefficients | $m_{\alpha\beta}^{(k)} = L_k \int dV \frac{\partial F_\alpha}{\partial L_k} F_\beta$ | Eq. (6) |
| Equidistant spectrum: per mode | $N_n \approx 8\kappa\omega_1 t/(\pi^2 n)$ | Eq. (7) |
| Equidistant spectrum: total | $N_{\text{tot}} \approx 2(\kappa\omega_1 t)^2$ | Eq. (7) |
| Total energy (exponential) | $E = (\hbar\omega_1/4)\sinh^2(2\kappa\omega_1 t)$ | Sec. 2 |
| DCE velocity bound | $N_{\max} \sim (v/c)^2$ | Sec. 2 |
| Dissipative threshold | $2Q\kappa > 1$ for exponential growth | Sec. 2 |

---

## Relevance to Phonon-Exflation

The dynamical Casimir effect provides a direct physical analog to the framework's tau-evolution mechanism. In the framework, the time-dependent internal modulus $\tau$ acts as a "moving mirror" in $K_7$ charge space: as $\tau$ evolves through the fold, the effective boundary conditions for fermion modes on the $SU(3)$ fiber change, producing particle creation from the vacuum. The framework's Schwinger-instanton duality ($S_{\text{Schwinger}} = 0.070 \approx S_{\text{inst}} = 0.069$, Session 38) identifies the same WKB integral underlying both pair creation mechanisms. The DCE's parametric amplification formula $\langle N \rangle = \sinh^2(\omega_0\kappa t)$ has structural parallels to the framework's quasiparticle excitation during transit ($P_{\text{exc}} = 1.000$, 59.8 pairs). The distinction between MI-DCE (boundary motion) and PA-DCE (medium parameter changes) maps onto the framework distinction between geometric evolution (tau-transit, analogous to moving boundaries) and spectral changes (eigenvalue rearrangement, analogous to parameter variation). The effective Hamiltonian's bilinear intermode coupling is structurally analogous to the framework's inter-sector coupling mediated by the Dirac operator $D_K$.
