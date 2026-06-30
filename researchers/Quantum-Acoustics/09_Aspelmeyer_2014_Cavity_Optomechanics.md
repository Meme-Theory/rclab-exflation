# Cavity Optomechanics

**Author(s):** Markus Aspelmeyer, Tobias J. Kippenberg, Florian Marquardt
**Year:** 2014
**Journal:** Reviews of Modern Physics 86, 1391-1452 (2014)
**arXiv:** 1303.0733
**Relevance:** HIGH

---

## Abstract

We review the field of cavity optomechanics, which explores the interaction between electromagnetic radiation and nano- or micromechanical motion. This review covers the basics of optical cavities and mechanical resonators, their mutual optomechanical interaction mediated by the radiation pressure force, the large variety of experimental systems which exhibit this interaction, optical measurements of mechanical motion, dynamical backaction amplification and cooling, nonlinear dynamics, multimode optomechanics, and proposals for future cavity quantum optomechanics experiments. In addition, we describe the perspectives for fundamental quantum physics and for possible applications of optomechanical devices.

---

## Key Arguments and Derivations

### 1. Optical Cavities (Section II.A)

A Fabry-Perot resonator with mirror separation $L$ has resonances at $\omega_m \approx m \cdot \pi c / L$ with free spectral range:

$$\Delta\omega_{\text{FSR}} = \frac{\pi c}{L}$$

The cavity decay rate $\kappa$ determines the finesse $\mathcal{F} = \Delta\omega_{\text{FSR}}/\kappa$ and quality factor $Q_{\text{opt}} = \omega_{\text{cav}} \tau$ with $\tau = \kappa^{-1}$. The total decay rate splits as $\kappa = \kappa_{\text{ex}} + \kappa_0$ (input coupling plus internal losses). Three regimes: overcoupled ($\kappa_{\text{ex}} \approx \kappa$), critically coupled ($\kappa_{\text{ex}} = \kappa_0$), and undercoupled ($\kappa_{\text{ex}} \ll \kappa_0$).

The input-output formalism gives the intracavity field equation:

$$\dot{\hat{a}} = -\frac{\kappa}{2}\hat{a} + i\Delta\hat{a} + \sqrt{\kappa_{\text{ex}}}\hat{a}_{\text{in}} + \sqrt{\kappa_0}\hat{f}_{\text{in}}$$

with output field $\hat{a}_{\text{out}} = \hat{a}_{\text{in}} - \sqrt{\kappa_{\text{ex}}}\hat{a}$, and steady-state photon number:

$$\bar{n}_{\text{cav}} = \frac{\kappa_{\text{ex}}}{\Delta^2 + (\kappa/2)^2} \frac{P}{\hbar\omega_L}$$

### 2. Mechanical Resonators (Section II.B)

The mechanical mode obeys:

$$m_{\text{eff}}\ddot{x} + m_{\text{eff}}\Gamma_m\dot{x} + m_{\text{eff}}\Omega_m^2 x = F_{\text{ext}}(t)$$

with susceptibility $\chi_{xx}(\omega) = [m_{\text{eff}}(\Omega_m^2 - \omega^2) - im_{\text{eff}}\Gamma_m\omega]^{-1}$.

Quantized: $\hat{H} = \hbar\Omega_m(\hat{b}^\dagger\hat{b} + 1/2)$ with $\hat{x} = x_{\text{ZPF}}(\hat{b} + \hat{b}^\dagger)$ where:

$$x_{\text{ZPF}} = \sqrt{\frac{\hbar}{2m_{\text{eff}}\Omega_m}}$$

The thermal decoherence rate $\bar{n}_{\text{th}} \cdot \Gamma_m \approx k_B T_{\text{bath}} / (\hbar Q_m)$ sets the rate at which the oscillator heats out of the ground state. The $Q \cdot f$ product quantifies decoupling from the thermal environment: $\Omega_m / (\bar{n}_{\text{th}} \cdot \Gamma_m) = Q_m \cdot f_m \times (h/k_B T)$.

### 3. Optomechanical Hamiltonian (Section III.B)

The uncoupled Hamiltonian: $\hat{H}_0 = \hbar\omega_{\text{cav}}\hat{a}^\dagger\hat{a} + \hbar\Omega_m\hat{b}^\dagger\hat{b}$.

The cavity frequency depends on displacement: $\omega_{\text{cav}}(x) \approx \omega_{\text{cav}} - Gx$ with $G = -\partial\omega_{\text{cav}}/\partial x$ (for simple cavity $G = \omega_{\text{cav}}/L$). The interaction Hamiltonian:

$$\hat{H}_{\text{int}} = -\hbar g_0 \hat{a}^\dagger\hat{a}(\hat{b} + \hat{b}^\dagger)$$

where $g_0 = G x_{\text{ZPF}}$ is the vacuum optomechanical coupling strength (single-photon/single-phonon coupling). The radiation pressure force: $\hat{F} = \hbar G \hat{a}^\dagger\hat{a}$.

In the rotating frame at laser frequency $\omega_L$:

$$\hat{H} = -\hbar\Delta\hat{a}^\dagger\hat{a} + \hbar\Omega_m\hat{b}^\dagger\hat{b} - \hbar g_0\hat{a}^\dagger\hat{a}(\hat{b} + \hat{b}^\dagger)$$

with $\Delta = \omega_L - \omega_{\text{cav}}$.

### 4. Linearized Regime (Section III.B)

Splitting $\hat{a} = \bar{\alpha} + \delta\hat{a}$ and keeping terms of order $|\bar{\alpha}|^1$:

$$\hat{H}_{\text{int}}^{(\text{lin})} = -\hbar g_0\sqrt{\bar{n}_{\text{cav}}}(\delta\hat{a}^\dagger + \delta\hat{a})(\hat{b} + \hat{b}^\dagger) = -\hbar g(\delta\hat{a}^\dagger + \delta\hat{a})(\hat{b} + \hat{b}^\dagger)$$

where $g = g_0\sqrt{\bar{n}_{\text{cav}}}$ is the light-enhanced coupling. Three regimes depending on detuning:

- **Red detuning** $\Delta \approx -\Omega_m$: beam-splitter interaction $-\hbar g(\delta\hat{a}^\dagger\hat{b} + \delta\hat{a}\hat{b}^\dagger)$ --- cooling, state transfer.
- **Blue detuning** $\Delta \approx +\Omega_m$: two-mode squeezing $-\hbar g(\delta\hat{a}^\dagger\hat{b}^\dagger + \delta\hat{a}\hat{b})$ --- amplification, entanglement.
- **On resonance** $\Delta = 0$: QND coupling to mechanical quadrature.

Strong coupling: $g > \kappa$ (normal-mode splitting). Single-photon strong coupling: $g_0 > \kappa$ (nonlinear quantum regime).

### 5. Dynamical Backaction (Section V.B)

Radiation pressure modifies the mechanical susceptibility. In the sideband-resolved regime ($\kappa \ll \Omega_m$):

- **Optical spring**: frequency shift $\delta\Omega_m \approx 2\bar{n}_{\text{cav}}g_0^2/\Delta$.
- **Optomechanical damping**: $\Gamma_{\text{opt}} = A_- - A_+$ with transition rates:

$$A_\pm = g_0^2 \bar{n}_{\text{cav}} \frac{\kappa}{(\kappa/2)^2 + (\Delta \pm \Omega_m)^2}$$

Maximum damping rate: $\Gamma_{\text{opt,max}} = 4\bar{n}_{\text{cav}}g_0^2/\kappa$ for $\kappa \ll \Omega_m$.

### 6. Standard Quantum Limit (Section VI.A)

For continuous displacement measurement, imprecision noise and backaction force noise satisfy:

$$\bar{S}_{xx}^{\text{imp}}(\omega) \cdot \bar{S}_{FF}(\omega) \geq \frac{\hbar^2}{4}$$

The imprecision noise: $\bar{S}_{xx}^{\text{imp}} = (\kappa/16\bar{n}_{\text{cav}}G^2)(1 + 4\omega^2/\kappa^2)$.
The backaction force noise: $\bar{S}_{FF} = \bar{n}_{\text{cav}}(4\hbar^2G^2/\kappa)(1 + 4\omega^2/\kappa^2)^{-1}$.

For an optomechanical cavity, the equality is saturated (quantum-limited detector). Minimizing total added noise:

$$\bar{S}_{xx}^{\text{add}}(\omega) \geq \bar{S}_{xx}^{\text{ZPF}}(\omega) = \hbar|\text{Im}\,\chi_{xx}(\omega)|$$

This is the **standard quantum limit** (SQL): the measurement adds at least the zero-point fluctuations. Reaching the SQL requires optimizing photon number such that imprecision equals backaction.

### 7. Ground-State Cooling (Section VII.A)

Quantum theory of radiation-pressure cooling via Raman scattering: red-detuned photons scatter upward by $\Omega_m$ (anti-Stokes), absorbing a phonon. The final phonon number:

$$\bar{n}_f = \frac{A_+ + \bar{n}_{\text{th}}\Gamma_m}{\Gamma_{\text{opt}} + \Gamma_m}$$

Minimum achievable:

$$\bar{n}_{\min} = \frac{A_+}{A_- - A_+}$$

In the sideband-resolved regime ($\kappa \ll \Omega_m$):

$$\bar{n}_{\min} = \left(\frac{\kappa}{4\Omega_m}\right)^2 < 1$$

which permits ground-state cooling. In the opposite limit ($\kappa \gg \Omega_m$): $\bar{n}_{\min} = \kappa/(4\Omega_m) \gg 1$.

### 8. Cooperativity

The optomechanical cooperativity is defined as:

$$C = \frac{g^2}{\kappa\Gamma_m} = \frac{4g_0^2\bar{n}_{\text{cav}}}{\kappa\Gamma_m}$$

The quantum cooperativity $C_{\text{qu}} = C/\bar{n}_{\text{th}}$ determines whether quantum effects dominate: ground-state cooling requires $C_{\text{qu}} > 1$, i.e., $\Gamma_{\text{opt}} > \bar{n}_{\text{th}}\Gamma_m$.

### 9. Multimode and Quantum Optomechanics (Sections IX-X)

The review covers: optomechanical normal-mode splitting, optomechanically induced transparency (OMIT), state transfer between optical and mechanical modes, entanglement generation via two-mode squeezing, hybrid quantum systems coupling mechanics to atomic ensembles or superconducting qubits, quantum protocols (state teleportation, quantum memories), and nonlinear quantum optomechanics (photon blockade, Schrödinger cat states).

## Key Results

1. The optomechanical interaction is fundamentally a three-wave mixing process ($\hat{a}^\dagger\hat{a}\hat{b}$), linearized to beam-splitter or two-mode squeezing depending on detuning.
2. Ground-state cooling is achievable in the sideband-resolved regime: $\bar{n}_{\min} = (\kappa/4\Omega_m)^2 < 1$.
3. The standard quantum limit for displacement measurement: added noise $\geq$ zero-point fluctuations.
4. The optomechanical cavity is a quantum-limited detector: imprecision-backaction product saturates the Heisenberg bound.
5. Dynamical backaction provides both optical spring (frequency shift) and optomechanical damping (cooling) from the same radiation pressure interaction.
6. Strong coupling ($g > \kappa$) enables normal-mode splitting and coherent state transfer between photons and phonons.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Optomechanical Hamiltonian | $\hat{H}_{\text{int}} = -\hbar g_0 \hat{a}^\dagger\hat{a}(\hat{b} + \hat{b}^\dagger)$ | Eq. (19) |
| Vacuum coupling | $g_0 = Gx_{\text{ZPF}}$ | Eq. (20) |
| Radiation pressure force | $\hat{F} = \hbar G\hat{a}^\dagger\hat{a}$ | Eq. (21) |
| Full Hamiltonian (rotating frame) | $\hat{H} = -\hbar\Delta\hat{a}^\dagger\hat{a} + \hbar\Omega_m\hat{b}^\dagger\hat{b} - \hbar g_0\hat{a}^\dagger\hat{a}(\hat{b}+\hat{b}^\dagger)$ | Eq. (22) |
| Linearized interaction | $\hat{H}_{\text{int}}^{(\text{lin})} = -\hbar g(\delta\hat{a}^\dagger + \delta\hat{a})(\hat{b} + \hat{b}^\dagger)$ | Eq. (28) |
| Enhanced coupling | $g = g_0\sqrt{\bar{n}_{\text{cav}}}$ | Eq. (29) |
| Beam-splitter (cooling) | $-\hbar g(\delta\hat{a}^\dagger\hat{b} + \delta\hat{a}\hat{b}^\dagger)$ | Eq. (30) |
| Two-mode squeezing | $-\hbar g(\delta\hat{a}^\dagger\hat{b}^\dagger + \delta\hat{a}\hat{b})$ | Eq. (31) |
| Mechanical susceptibility | $\chi_{xx}(\omega) = [m_{\text{eff}}(\Omega_m^2 - \omega^2) - im_{\text{eff}}\Gamma_m\omega]^{-1}$ | Eq. (10) |
| Zero-point fluctuations | $x_{\text{ZPF}} = \sqrt{\hbar/(2m_{\text{eff}}\Omega_m)}$ | Sec. II.B |
| Intracavity photon number | $\bar{n}_{\text{cav}} = \kappa_{\text{ex}}P/[\hbar\omega_L(\Delta^2 + (\kappa/2)^2)]$ | Eq. (7) |
| SQL inequality | $\bar{S}_{xx}^{\text{add}}(\omega) \geq \bar{S}_{xx}^{\text{ZPF}}(\omega)$ | Eq. (73) |
| Heisenberg bound | $\bar{S}_{xx}^{\text{imp}} \cdot \bar{S}_{FF} \geq \hbar^2/4$ | Eq. (71) |
| Final phonon number | $\bar{n}_f = (A_+ + \bar{n}_{\text{th}}\Gamma_m)/(\Gamma_{\text{opt}} + \Gamma_m)$ | Eq. (83) |
| Minimum phonon (resolved) | $\bar{n}_{\min} = (\kappa/4\Omega_m)^2$ | Eq. (88) |
| Transition rates | $A_\pm = g_0^2\bar{n}_{\text{cav}}\kappa/[(\kappa/2)^2 + (\Delta \pm \Omega_m)^2]$ | Eq. (85) |
| Optomechanical damping | $\Gamma_{\text{opt}} = A_- - A_+$ | Eq. (81) |

## Relevance to Phonon-Exflation

This review establishes the theoretical framework for phonon-photon coupling that underpins the framework's treatment of phonon excitations interacting with the radiation content of spacetime. Three connections are paramount: (1) The optomechanical Hamiltonian $-\hbar g_0 \hat{a}^\dagger\hat{a}(\hat{b} + \hat{b}^\dagger)$ is the phonon-coupling prototype for the framework's particle-geometry interaction, where geometry (the "cavity") couples parametrically to phononic excitations of the internal space. (2) Dynamical backaction --- where the cavity's retarded response damps or amplifies mechanical motion --- is the mechanism analog for how the spectral action modifies the instanton dynamics: the backreaction result of Session 38 (3.7%, perturbative, underdamped) follows the same perturbative structure. (3) The standard quantum limit and the zero-point fluctuation floor connect directly to the framework's vacuum floor analysis (Session 42) where the virtual/real distinction emerges from substrate complexity rather than an imposed boundary.
