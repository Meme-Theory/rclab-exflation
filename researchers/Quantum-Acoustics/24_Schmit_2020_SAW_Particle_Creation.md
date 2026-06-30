# Quantum Simulation of Particle Creation in Curved Space-Time

**Author(s):** R. P. Schmit, B. G. Taketani, F. K. Wilhelm
**Year:** 2020
**Journal:** [preprint, v3]
**arXiv:** 1804.04092
**Relevance:** MEDIUM

---

## Abstract

Conversion of vacuum fluctuations into real particles was first predicted by L. Parker considering an expanding universe, followed in S. Hawking's work on black hole radiation. Since their experimental observation is challenging, analogue systems have gained attention in the verification of this concept. Here we propose an experimental set-up consisting of two adjacent piezoelectric semiconducting layers, one of them carrying dynamic quantum dots (DQDs), and the other being p-doped with an attached gate on top, which introduces a space-dependent layer conductivity. The propagation of surface acoustic waves (SAWs) on the latter layer is governed by a wave equation with an effective metric. In the frame of the DQDs, this space- and time-dependent metric possesses a sonic horizon for SAWs and resembles that of a two dimensional non-rotating and uncharged black hole to some extent. The non-thermal steady state of the DQD spin indicates particle creation in form of piezophonons.

---

## Key Arguments and Derivations

### I. Introduction

The paper situates itself at the intersection of analogue gravity and solid-state quantum simulation. Vacuum fluctuations can be converted into real particles under three conditions: the dynamical Casimir effect (experimentally verified), expansion of the universe (Parker, 1968), and black hole event horizons (Hawking, 1975). Since direct observation of cosmological and black hole particle creation is impractical, analogue systems provide accessible substitutes. Prior analogue systems include: liquid helium, dc-SQUID transmission lines, electromagnetic waveguides, water waves, microcavity polaritons, optical setups, and Bose-Einstein condensates.

The proposed system combines features of both black hole and expanding universe analogues using surface acoustic waves (SAWs) on piezoelectric semiconducting substrates with a space-dependent 2DEG density modulation.

### II. Building Blocks

**Effective metric:** Starting from the 1D wave equation for SAWs with space-dependent speed of sound $c(x)$:
$$\frac{\partial^2 u}{\partial t^2} = \frac{\partial}{\partial x}\left(c^2(x)\frac{\partial u}{\partial x}\right)$$
this describes wave propagation in a spacetime with line element $ds^2 = -c^2(x)dt^2 + dx^2$. A Galilean transformation to the frame of an observer moving at speed $v$ yields:
$$ds^2 = -[c^2(x - vt) - v^2]dt^2 + 2v\,dt\,dx + dx^2$$
A sonic horizon appears where $c^2 - v^2 = 0$. This effective metric shares features with both the Painleve-Gullstrand metric (black hole analogue) and the Friedmann-Lemaitre-Robertson-Walker metric (expanding universe analogue).

**SAW dynamics:** The interaction between SAWs and a 2DEG in the piezoelectric substrate is derived following Hutson and White (1962), extended to the inhomogeneous case. The piezoelectric effect introduces an effective permittivity:
$$\epsilon_{\text{eff}} = \frac{\mu q}{\omega}\left[\frac{\partial_x n_{\text{2DEG}}}{\partial_x k + in_{\text{2DEG}}}\right]$$
and effective elastic constant $d_{\text{eff}} = d\left[1 + \frac{e^2}{\epsilon d}\left(1 - \frac{\epsilon_{\text{eff}}}{\epsilon}\right)^{-1}\right]$, where $e$ is the piezoelectric constant. The SAW speed is:
$$c(x) = \text{Re}\sqrt{\frac{d_{\text{eff}}}{\rho}}$$
The speed transitions from $c_0 = \sqrt{d/\rho}$ (inside the gate, high 2DEG density) to $c_0(1 + K^2/2)$ (outside, no 2DEG), where $K^2 = e^2/(\epsilon d) \ll 1$ is the piezoelectric coupling constant.

**2DEG density modulation:** The 2DEG density induced by a biased gate ($V_G \sim 10$ V) is smoothed near the gate edge by screening:
$$n_{\text{2DEG}}(x) = \frac{n_{\max}}{2}[1 - \text{erf}(\kappa_s x)]$$
where $\kappa_s^{-1} \sim 10^{-8}$ m is the screening length. The SAW speed changes over a region of width $\sim 4\kappa_s^{-1}$ around the gate edge, approximately linearly in this transition region.

### III. Particle Creation and Detection

Moving electrons trapped in SAW lateral piezoelectric potentials serve as dynamic quantum dots (DQDs) -- the moving particle detectors. The DQD electron spin in a magnetic field $B \sim 1$ T along [001] has Zeeman splitting $E_0 = g\mu_B B$. The Hamiltonian is decomposed as $H = H_S + H_{SB} + H_B$:

- Spin Hamiltonian: $H_S = E_0\sigma_z + \Delta E\sigma_y$
- Bath: $H_B = \sum_q \hbar\omega_q(b^\dagger_q b_q + 1/2)$
- Interaction (Dresselhaus spin-orbit): $H_{SB} = \sigma_x\sum_q M_q e^{iqvt}(b^\dagger_{-q} + b_q)$

Using Bloch-Redfield equations, the steady-state populations are $\rho_{11}/\rho_{00} = \Gamma_{12}/\Gamma_{21}$, defining an effective temperature $T'$ via $\rho_{11}/\rho_{00} = \exp(-\hbar\omega_{10}/k_B T')$.

**Subsonic case ($v < c$):** The absorption and emission rates involve Doppler-shifted frequencies $\omega^\pm = \omega_{21}/(1 \pm v/c)$. At zero bath temperature, $\Gamma_{12} = 0$ (no phonons to absorb), so the DQD equilibrates at zero effective temperature.

**Supersonic case ($v > c$):** At zero bath temperature, the absorption rate is nonzero:
$$\Gamma_{12} = \frac{\pi M_{1221}}{v/c - 1}J(\omega^-_{21})$$
$$\Gamma_{21} = \frac{\pi M_{1221}}{v/c + 1}J(\omega^+_{21})$$
Even with a zero-temperature phonon bath, the DQD reaches a non-thermal steady state ($T' \neq 0$). This is attributed to particle creation in the form of piezophonons -- excess phonons in the moving frame due to the observer-dependent notion of particles.

Detection uses Stern-Gerlach gates that convert spin into current paths. Equilibration time is estimated at $\sim 1$ s. A storage ring arrangement of interdigitated transducers (IDTs) provides sufficient interaction time.

### IV. Conclusion

The authors note that the origin of excess phonons in the moving frame requires further work to determine their cosmological nature. The Bogoliubov transformation approach (computing mixing of positive and negative frequency modes between reference frames) is deferred to future work.

---

## Key Results

1. A piezoelectric semiconductor with spatially modulated 2DEG produces a space-dependent SAW speed, creating a sonic horizon for a moving observer
2. The effective metric in the moving frame $ds^2 = -[c^2(x-vt) - v^2]dt^2 + 2v\,dt\,dx + dx^2$ shares features with both Painleve-Gullstrand (black hole) and FLRW (expanding universe) metrics
3. A DQD moving supersonically through the modulated substrate reaches a non-thermal steady state even when coupled to a zero-temperature phonon bath
4. The non-thermality is attributed to particle creation in the form of piezophonons, analogous to cosmological/Hawking particle creation
5. The SAW speed modulation occurs over $\sim 4\kappa_s^{-1} \approx 40$ nm near the gate edge, controlled by the screening length
6. Equilibration time for the DQD spin detector is estimated at $\sim 1$ s, achievable in SAW storage ring geometry
7. The subsonic-supersonic transition is the solid-state analogue of the observer crossing a sonic horizon

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| SAW wave equation | $\frac{\partial^2 u}{\partial t^2} = \frac{\partial}{\partial x}\left(c^2(x)\frac{\partial u}{\partial x}\right)$ | Eq. 1 |
| Static effective metric | $ds^2 = -c^2(x)dt^2 + dx^2$ | Eq. 2 |
| Moving-frame metric | $ds^2 = -[c^2(x-vt) - v^2]dt^2 + 2v\,dt\,dx + dx^2$ | Eq. 3 |
| Effective permittivity | $\epsilon_{\text{eff}} = \frac{\mu q}{\omega}\left[\frac{\partial_x n_{\text{2DEG}}}{\partial_x k + in_{\text{2DEG}}}\right]$ | Eq. 4 |
| Effective elastic constant | $d_{\text{eff}} = d\left[1 + \frac{e^2}{\epsilon d}\left(1 - \frac{\epsilon_{\text{eff}}}{\epsilon}\right)^{-1}\right]$ | Eq. 5 |
| SAW speed | $c(x) = \text{Re}\sqrt{d_{\text{eff}}/\rho}$ | Eq. 6 |
| 2DEG density profile | $n_{\text{2DEG}}(x) = \frac{n_{\max}}{2}[1 - \text{erf}(\kappa_s x)]$ | Eq. 7 |
| Redfield tensor | $R_{\mu\nu\kappa\lambda} = \Gamma^+_{\lambda\nu\mu\kappa} + \Gamma^-_{\lambda\nu\mu\kappa} - \delta_{\nu\lambda}\sum_\alpha\Gamma^+_{\mu\alpha\alpha\kappa} - \delta_{\mu\kappa}\sum_\alpha\Gamma^-_{\lambda\alpha\alpha\nu}$ | Eq. 8 |
| Steady-state population ratio | $\rho_{11}/\rho_{00} = \Gamma_{12}/\Gamma_{21}$ | Eq. 9 |
| Effective temperature | $\rho_{11}/\rho_{00} = \exp(-\hbar\omega_{10}/k_B T')$ | Eq. 10 |

---

## Relevance to Phonon-Exflation

This paper proposes a concrete solid-state analogue of cosmological particle creation using surface acoustic waves and piezoelectric phonons, directly connecting to the phonon-exflation framework's identification of the tau-transit as a Parker-type cosmological particle creation process. The key parallel is that the space-dependent modulation of the SAW speed creates an effective curved-spacetime metric for phononic excitations -- analogous to how the framework's evolving tau parameter creates an effective time-dependent geometry for quasiparticle excitations on $SU(3)$. The observer-dependent notion of particles (subsonic vs supersonic) mirrors the framework's result that the transit produces quasiparticle excitations ($P_{\text{exc}} = 1.000$) whose character depends on the reference frame. The non-thermal steady state of the DQD detector provides an experimental paradigm for the framework's GGE relic state that never thermalizes due to integrability protection.
