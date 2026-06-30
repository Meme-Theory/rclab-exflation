# Magnon Bose-Einstein Condensates: From Time Crystals and Quantum Chromodynamics to Vortex Sensing and Cosmology

**Author(s):** J. T. Makinen, S. Autti, V. B. Eltsov
**Year:** 2023
**Journal:** Applied Physics Letters (Perspective)
**arXiv:** 2312.10119
**Relevance:** MEDIUM

---

## Abstract

Under suitable experimental conditions collective spin-wave excitations, magnons, form a Bose-Einstein condensate (BEC) where the spins precess with a globally coherent phase. Bose-Einstein condensation of magnons has been reported in a few systems, including superfluid phases of $^3$He, solid state systems such as Yttrium-iron-garnet (YIG) films, and cold atomic gases. Among these systems, the superfluid phases of $^3$He provide a nearly ideal test bench for coherent magnon physics owing to experimentally proven spin superfluidity, the long lifetime of the magnon condensate, and the versatility of the accessible phenomena. We first briefly recap the properties of the different magnon BEC systems, with focus on superfluid $^3$He. The main body of this review summarizes recent advances in application of magnon BEC as a laboratory to study basic physical phenomena connecting to diverse areas from particle physics and cosmology to new phases of condensed matter. This line of research complements the ongoing efforts to utilize magnon BECs as probes and components for potentially room-temperature quantum devices. In conclusion, we provide a roadmap for future directions in the field of applications of magnon BEC to fundamental research.

---

## Key Arguments and Derivations

### I. Introduction: Magnon BEC Systems

Magnons are spin-1 quasiparticles obeying bosonic statistics. At sufficiently large number density and low temperature, magnons form a BEC manifested as spontaneous coherence of spin precession across a macroscopic ensemble. Key distinction from atomic BECs: magnons are quasiparticles with non-conserved number. In thermodynamic equilibrium, $\mu_{\text{eq}} \equiv 0$, so no equilibrium BEC can exist. The BEC forms when the magnon lifetime $\tau_N \gg \tau_E$ (thermalization time), allowing a nonzero chemical potential.

Systems where magnon BEC has been reported:
- Superfluid phases of $^3$He (first observed 1984 as homogeneously precessing domain)
- Cold atomic gases ($^1$H, $^{87}$Rb spinor condensates)
- Solid-state systems (YIG films, at room temperature)
- Antiferromagnetic hematite ($\alpha$-Fe$_2$O$_3$) as candidate

The critical magnon density $n_c$ corresponds to when inter-magnon separation becomes comparable to the thermal de Broglie wavelength: $n_c^{-1/3} \sim \lambda_{\text{dB}}$.

### II. Coherent Precession and Spin Superfluidity

**ODLRO and magnon condensation:** The magnetic ODLRO is represented via Holstein-Primakoff transformation relating spin operators to magnon creation/annihilation operators. The ODLRO in magnon BEC is given by:
$$\langle \hat{a}_0 \rangle = N^{1/2} e^{i\omega t + i\alpha} = \sqrt{\frac{2S}{\hbar}} \sin\frac{\beta}{2} e^{i\omega t + i\alpha}$$
where $\beta$ is the tipping angle, $\mu \equiv \hbar\omega$ (chemical potential = precession frequency), and $\alpha$ is the condensate phase.

**Gross-Pitaevskii description:** The magnon BEC is described by a GP equation with free energy functional:
$$F - \mu N = \int d^3r \left[\frac{1}{2}g_{ik}\nabla_i\Psi^*\nabla_k\Psi + \hbar(\omega_L(\mathbf{r})-\omega)|\Psi|^2 + F_{\text{so}}(|\Psi|^2)\right]$$
The spin-orbit interaction provides both second-order (trapping) and fourth-order (interaction) terms, analogous to the standard Ginzburg-Landau form with external potential $U(\mathbf{r})$ and interaction term $b|\Psi|^4$.

### III. Magnon BEC as a Time Crystal

Time crystals in magnon BEC systems break time-translation symmetry. In $^3$He-B, continuous time crystals reach lifetimes longer than $10^7$ periods.

**Phonon in a time crystal:** Spontaneous breaking of continuous time-translation symmetry gives rise to a Nambu-Goldstone mode -- a phonon in the time crystal. Under RF drive with amplitude $H_{\text{rf}}$, this becomes a pseudo-NG mode with dispersion:
$$\omega_{\text{NG}}^2 = M_{\text{NG}}^2 + c_{\text{NG}}^2 k^2$$
where $M_{\text{NG}} \propto H_{\text{rf}}$. Extrapolation to $H_{\text{rf}} = 0$ gives a true massless NG mode.

**Interacting time crystals:** Two magnon BECs form a macroscopic two-level system with Hamiltonian:
$$H = \hbar \begin{pmatrix} \omega_B[N_B(t)] & -\Omega \\ -\Omega & \omega_S \end{pmatrix}$$
where coupling $\Omega$ is determined by spatial overlap of wave functions. This yields AC Josephson oscillations and Landau-Zener transitions.

### IV. Magnon BEC and Cosmology

**Q-balls:** The trapped magnon BEC in $^3$He-B provides a one-to-one implementation of the Q-ball Hamiltonian. The magnon number is the charge $Q$, BEC precession frequency corresponds to oscillation frequency of the relativistic field. Above a critical magnon number, the radial trapping potential changes from harmonic to "Mexican-hat." All essential features demonstrated: self-condensation, long lifetime, propagation across macroscopic distances (several mm).

**MIT Bag Model analog:** When the magnetic maximum is removed, the magnon BEC forms a self-trapping box analogous to the MIT bag model of quark confinement. Magnons dig a hole in the confining "vacuum," pushing the orbital field away. The flexible Cooper pair orbital momentum distribution $\hat{l}$ plays the role of the pion field or non-perturbative gluonic field.

### V. Light Higgs Bosons

Superfluid $^3$He-B has 18 bosonic degrees of freedom: 14 Higgs modes (gapped at $\Delta/h \sim 100$ MHz) and 4 Nambu-Goldstone modes. The order parameter:
$$A_{\alpha j} = \Delta e^{i\phi} R_{\alpha j}(\hat{n}, \theta)$$
The spin-orbit interaction lifts degeneracy with respect to $\theta$; one NG mode acquires a gap at the Leggett frequency $\Omega_L/h \sim 100$ kHz, becoming a **light Higgs mode**. Parametric decay of optical magnons into light Higgs quasiparticles has been observed -- directly analogous to Higgs production in the Standard Model.

### VI. Curved Space-Time: Event Horizons

Two magnon BECs connected by a narrow channel create an analog white-hole event horizon. Spin-precession waves propagating opposite to spin superflow are blocked when the phase difference is sufficiently large, analogous to a white-hole horizon.

### VII. Magnon BEC as Probe for Quantized Vortices

Vortex contribution to textural energy modifies the magnon trapping potential. The ground state frequency shift scales as:
$$\Delta f \approx -f_0 \sin^2\theta$$
where $f_0 \sim 100$ Hz scales linearly with vortex core size. This enables probing transient vortex dynamics and distinguishing vortex core structures.

### VIII. Outlook

Future directions include: dark matter axion detection via magnon-BEC coupling, probing topological surface states (Majorana states at $^3$He-B surface), magnon lattices for solid-state physics analogs, curved-spacetime simulation via acoustic metric experiments, and Minkowski-to-Euclidean signature transitions.

---

## Key Results

1. Magnon BEC in $^3$He-B forms the closest experimental realization of a time crystal, with coherence times reaching tens of minutes and lifetimes exceeding $10^7$ periods.
2. Phonon of a time crystal (NG mode of time-translation symmetry breaking) observed experimentally; becomes massless as $H_{\text{rf}} \to 0$.
3. Two interacting magnon-BEC time crystals realize a macroscopic two-level quantum system exhibiting Josephson oscillations and Landau-Zener transitions.
4. Magnonic Q-ball solitons demonstrated: self-condensation, long lifetime, macroscopic propagation -- first experimental implementation of Q-ball Hamiltonian.
5. MIT bag model analog realized: magnons self-trap by excavating the confining "vacuum."
6. Light Higgs mode observed at Leggett frequency $\Omega_L/h \sim 100$ kHz; parametric decay channel to Higgs modes demonstrated.
7. Analog white-hole event horizon realized using spin superflow blocking spin-precession waves.
8. Magnon BEC used as local probe of quantized vortex dynamics down to lowest temperatures, resolving vortex core structure.
9. Minkowski-to-Euclidean signature change achievable in polar $^3$He magnon BEC by adjusting magnetic field angle.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BEC ground state population | $n_0 = \frac{1}{e^{(\epsilon_0 - \mu)/k_B T} - 1}$ | Eq. (1) |
| ODLRO creation/annihilation | $\Psi = \langle\hat{\Psi}\rangle$, $\Psi^* = \langle\hat{\Psi}^\dagger\rangle$ | Eq. (2) |
| Holstein-Primakoff transformation | $\hat{a}_0\sqrt{1 - \frac{\hbar \hat{a}_0^\dagger \hat{a}_0}{2S}} = \frac{\hat{S}_+}{\sqrt{2S\hbar}}$ | Eq. (3) |
| Magnon number-spin relation | $\hat{N} = \hat{a}_0^\dagger \hat{a}_0 = \frac{S - \hat{S}_z}{\hbar}$ | Eq. (4) |
| ODLRO in magnon BEC | $\langle\hat{a}_0\rangle = N^{1/2}e^{i\omega t + i\alpha} = \sqrt{\frac{2S}{\hbar}}\sin\frac{\beta}{2}e^{i\omega t + i\alpha}$ | Eq. (5) |
| Magnon field and number | $\Psi(\mathbf{r},t) = \langle\hat{\Psi}(\mathbf{r},t)\rangle$, $n = |\Psi|^2$, $N = \int d^3r |\Psi|^2$ | Eq. (6) |
| Gross-Pitaevskii equation | $-i\hbar\frac{\partial\Psi}{\partial t} = \frac{\delta F}{\delta\Psi^*}$ | Eq. (7) |
| Ginzburg-Landau equation | $\frac{\delta F}{\delta\Psi^*} - \mu\Psi = 0$ | Eq. (9) |
| Free energy functional | $F - \mu N = \int d^3r\left[\frac{1}{2}g_{ik}\nabla_i\Psi^*\nabla_k\Psi + \hbar(\omega_L - \omega)|\Psi|^2 + F_{\text{so}}\right]$ | Eq. (10) |
| Pseudo-NG dispersion | $\omega_{\text{NG}}^2 = M_{\text{NG}}^2 + c_{\text{NG}}^2 k^2$ | Eq. (13) |
| Two-level Hamiltonian | $H = \hbar\begin{pmatrix}\omega_B[N_B(t)] & -\Omega \\ -\Omega & \omega_S\end{pmatrix}$ | Eq. (14) |
| $^3$He-B order parameter | $A_{\alpha j} = \Delta e^{i\phi} R_{\alpha j}(\hat{n},\theta)$ | Eq. (15) |
| Vortex textural energy | $F_v = \frac{2}{5}a_m H^2 \frac{\lambda}{\Omega}\int d^3r\frac{(\boldsymbol{\omega}_v \cdot \hat{l})^2}{\omega_v}$ | Eq. (16) |
| Vortex tilt frequency shift | $\Delta f \approx -f_0 \sin^2\theta$ | Eq. (18) |

---

## Relevance to Phonon-Exflation

The magnon BEC system demonstrates several phenomena directly relevant to the phonon-exflation framework: (1) Bose-Einstein condensation of non-conserved quasiparticles with emergent chemical potential parallels the instanton gas picture where quasiparticle excitations arise from a substrate with no conserved particle number. (2) The phonon-in-a-time-crystal (NG mode of broken time-translation symmetry) provides a condensed matter analog of how phononic excitations emerge from spontaneous symmetry breaking in the M4 x SU(3) setting. (3) The Q-ball self-trapping and MIT bag model analogy connect to how Cooper pair condensates in the framework create self-consistent potentials. (4) The Minkowski-to-Euclidean signature change in polar $^3$He magnon BEC is directly relevant to the framework's instanton physics and the Schwinger-instanton duality identified in Session 38.
