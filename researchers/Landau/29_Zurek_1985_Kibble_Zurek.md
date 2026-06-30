# Cosmological Experiments in Superfluids and Superconductors

**Author(s):** W. H. Zurek
**Year:** 1995 (based on 1985 original; this version: proceedings contribution, cond-mat/9502119)
**Journal:** Proceedings of NATO ASI/Euroconference "Formation and Interactions of Topological Defects", A. C. Davis and R. N. Brandenberger, eds. (Plenum, in press)
**arXiv:** cond-mat/9502119
**Relevance:** CRITICAL

---

## Abstract

Evolution of the order parameter in condensed matter analogues of cosmological phase transitions is discussed. It is shown that the density of the frozen-out topological defects is set by the competition between the quench rate -- the rate at which the phase transition is taking place -- and the relaxation rate of the order parameter. More specifically, the characteristic domain size which determines the typical distance separating topological defects in the new broken symmetry phase (and, therefore, their density) is determined by the correlation length at the instant at which the relaxation timescale of the order parameter is equal to the time from the phase transition. This scenario shares with the Kibble mechanism the idea that topological defects will appear "in between" domains with independently chosen broken symmetry vacuum. However, it differs from the original proposal in estimating the size of such domains through the non-equilibrium aspects of the transition (quench rate), rather than through the Ginzburg temperature at which thermally activated symmetry restoration can still occur in the correlation-length sized volumes of the broken symmetry phase. This scenario can be employed to analyze recent superfluid quench experiments carried out in bulk He4 to study the analogue of the "cosmological" prediction of significant vortex line production. It can be also applied to superfluid quenches in annular geometry, as well as to the rapid phase transition from the normal metal to superconductor, where the symmetry breaking occurs in the order parameter with the local (rather than a global) gauge. Cosmological implications of the revised defect formation scenario with the critical domain size set by the freeze-out time rather than by the Ginzburg temperature are also briefly considered.

---

## Key Arguments and Derivations

### 1. Symmetry Breaking in Superfluids, Superconductors, and the Early Universe (Section 2)

**Superfluid Helium.** The Landau-Ginzburg free energy density is:
$$F(\Psi) = \frac{\hbar^2}{2m}|\nabla\Psi|^2 + \alpha|\Psi|^2 + \frac{\beta}{2}|\Psi|^4$$
with $\alpha = \alpha'(T - T_C)/T_C$ ($\alpha' > 0$) and $\beta > 0$. Below $T_C$, the order parameter acquires amplitude $\sigma = \sqrt{-\alpha/\beta}$ and a random phase $\theta$. The correlation length is $\xi = \hbar/\sqrt{2m|\alpha|}$.

Vortex lines are axisymmetric solutions $\eta = \psi(\varrho)\exp(in\phi)$ of the rescaled equilibrium equation $\nabla^2\eta = (|\eta|^2 - 1)\eta$, with winding number $n$. The superfluid velocity is $v_S = (\hbar/m)(n/r)$. Vortex lines are the analogue of global cosmic strings; the homotopy group $\Pi_1(U(1)) = \mathbb{Z}$ ensures their topological stability.

**Superconductors.** The Landau-Ginzburg free energy includes gauge fields:
$$F = \frac{1}{4m}|(-i\hbar\nabla - \frac{2e}{c}\vec{A})\Psi|^2 + \alpha|\Psi|^2 + \frac{1}{2}\beta|\Psi|^4 + \frac{B^2}{8\pi} + E_0$$

The London penetration depth $\lambda^2 = mc^2/(8\pi e^2 n_C)$ and correlation length $\xi^2 = \hbar/(4m\alpha)$ define two characteristic scales. Vortices exist only in type II superconductors where $\kappa = \lambda/\xi > 1/\sqrt{2}$. These are analogues of local (Nielsen-Olesen) cosmic strings.

**Field Theory.** The global U(1) Lagrangian $\mathcal{L} = (\partial_\mu\phi^*)(\partial^\mu\phi) - \alpha\phi^*\phi - \frac{\beta}{2}(\phi^*\phi)^2$ yields, upon symmetry breaking, a massive Higgs mode (mass $\sqrt{-\alpha}$) and a massless Goldstone boson. The local gauge version (Abelian Higgs model) features the Higgs mechanism where the gauge boson acquires mass $e\sigma\sqrt{2}$.

### 2. The Freeze-Out Mechanism (Section 3) -- THE CORE CONTRIBUTION

Zurek's key insight is that the density of topological defects produced in a quench is NOT determined by the Ginzburg temperature $T_G$ (thermal activation), but by the **freeze-out** of order parameter dynamics near $T_C$.

**The Argument:** Near the critical temperature, the relaxation time diverges as:
$$\tau = \tau_0/|\epsilon|$$
where $\epsilon = (T - T_\lambda)/T_\lambda$, and the correlation length diverges as:
$$\xi = \xi_0|\epsilon|^{-\nu}$$

For a linear quench $\epsilon = t/\tau_Q$ (where $\tau_Q$ is the quench timescale), the order parameter initially adjusts adiabatically to changing thermodynamic conditions. But as $T \to T_C$, the relaxation time exceeds the rate of change, and the system freezes out.

**The freeze-out time** $\hat{t}$ is determined by $\tau(\hat{t}) = \hat{t}$, giving:
$$\hat{t} = \sqrt{\tau_0 \tau_Q}$$

**The frozen correlation length** determines the domain size:
$$d = \xi(\hat{t}) = \xi_0(\tau_Q/\tau_0)^{\nu/2}$$

**The vortex line density** is:
$$\ell = k/d^2 = (k/\xi_0^2)(\tau_0/\tau_Q)^\nu$$
where $k$ is a proportionality constant of order 1.

### 3. Why Ginzburg Temperature Does NOT Determine Defect Density

Zurek argues that thermally activated transitions at the Ginzburg temperature create only small vortex loops of radius $\sim \xi$ (the correlation length at $T_G$). These "doughnut" configurations are not topologically stable -- they can be unwound by local field reconfigurations within a $\xi$-sized region. They cannot produce the long vortex lines that constitute the dominant defect population after a quench.

The Ginzburg temperature estimate $T_\lambda - T_G \sim 0.5$ K for He4 has little bearing on vortex line production; the freeze-out mechanism at much closer proximity to $T_\lambda$ is decisive.

### 4. Comparison with He4 Experiment (Section 3)

The Lancaster experiment (McClintock and colleagues) performed pressure quenches through the $\lambda$-line with $\Delta\epsilon \sim 0.1$ over $\Delta t \sim 3$ ms, giving $\tau_Q \sim 30$ ms. The predicted vortex line densities are:

- Landau-Ginzburg ($\nu = 1/2$, $\xi_0 = 5.6$ A, $\tau_0 = 0.85 \times 10^{-11}$ s): $\ell_{LG} \approx 3(\tau_Q/100\text{ ms})^{-1/2} \times 10^{13}$ m$^{-2}$
- Renormalization group ($\nu = 2/3$): $\ell_{RG} \approx 1.2(\tau_Q/100\text{ ms})^{-2/3} \times 10^{12}$ m$^{-2}$

These bracket the experimental lower bound of $\ell \sim 10^{13}$ m$^{-2}$.

### 5. Superconducting Quench and Flux Trapping (Sections 4-5)

For superconductors, the freeze-out produces trapped magnetic flux (fluxons) rather than vortex lines. The predicted flux per unit area is $\Phi \sim \Phi_0/\hat{\xi}^2$, where $\hat{\xi}$ is the frozen correlation length. The annular geometry allows testing of the KZ mechanism through trapped flux quanta in a loop.

### 6. Cosmological Implications (Section 6)

The revised scenario impacts cosmic string density estimates. The freeze-out correlation length replaces the Ginzburg-temperature correlation length, potentially yielding different string densities depending on the quench rate of the cosmological phase transition. For GUT-scale transitions, the Hubble time provides the quench timescale.

## Key Results

1. **The Kibble-Zurek mechanism**: Topological defect density after a symmetry-breaking quench is determined by the freeze-out correlation length $\hat{\xi} = \xi_0(\tau_Q/\tau_0)^{\nu/2}$, not by the Ginzburg temperature.
2. Defect density scales as a power law of the quench rate: $\ell \propto \tau_Q^{-\nu}$.
3. The freeze-out time $\hat{t} = \sqrt{\tau_0\tau_Q}$ marks the crossover from adiabatic to impulse regime.
4. Predictions for He4 vortex line density bracket the experimental observation of $\ell \sim 10^{13}$ m$^{-2}$.
5. The mechanism applies to both global (superfluid) and local (superconductor) gauge symmetry breaking.
6. Thermally activated defect creation at $T_G$ produces only topologically unstable micro-loops, not the observed long vortex lines.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Landau-Ginzburg free energy | $F = \frac{\hbar^2}{2m}|\nabla\Psi|^2 + \alpha|\Psi|^2 + \frac{\beta}{2}|\Psi|^4$ | Eq. (1) |
| Order parameter amplitude | $\sigma = \sqrt{-\alpha/\beta}$ | Eq. (3) |
| Correlation length | $\xi = \hbar/\sqrt{2m|\alpha|}$ | Eq. (5) |
| Superfluid velocity | $v_S = (\hbar/m)(n/r)$ | Eq. (9) |
| Superconductor free energy | $F = \frac{1}{4m}|(-i\hbar\nabla - \frac{2e}{c}\vec{A})\Psi|^2 + \alpha|\Psi|^2 + \frac{\beta}{2}|\Psi|^4 + \frac{B^2}{8\pi}$ | Eq. (10) |
| London penetration depth | $\lambda^2 = mc^2/(8\pi e^2 n_C)$ | Eq. (17) |
| Type II condition | $\kappa = \lambda/\xi > 1/\sqrt{2}$ | Eq. (20) |
| Relaxation time | $\tau = \tau_0/|\epsilon|$ | Eq. (30)/(32) |
| Correlation length divergence | $\xi = \xi_0|\epsilon|^{-\nu}$ | Eq. (33) |
| Linear quench | $\epsilon = t/\tau_Q$ | Eq. (34) |
| Freeze-out condition | $\tau(\hat{t}) = \hat{t}$ | Eq. (35) |
| Freeze-out time | $\hat{t} = \sqrt{\tau_0\tau_Q}$ | Eq. (37) |
| Frozen correlation length | $d = \xi(\hat{t}) = \xi_0(\tau_Q/\tau_0)^{\nu/2}$ | Eq. (38) |
| Vortex line density | $\ell = (k/\xi_0^2)(\tau_0/\tau_Q)^\nu$ | Eq. (40) |
| RG exponent | $\nu = 2/3$ | Eq. (41) |
| LG prediction | $\ell_{LG} \approx 3(\tau_Q/100\text{ ms})^{-1/2} \times 10^{13}\text{ m}^{-2}$ | Eq. (50a) |
| RG prediction | $\ell_{RG} \approx 1.2(\tau_Q/100\text{ ms})^{-2/3} \times 10^{12}\text{ m}^{-2}$ | Eq. (50b) |
| Ginzburg barrier | $\xi^3\alpha^2/(2\beta) \sim k_B T$ | Eq. (45) |
| Ginzburg temperature (He4) | $T_\lambda - T_G \sim 0.5$ K | Eq. (46) |

## Relevance to Phonon-Exflation

This is a foundational paper for the phonon-exflation framework. The Kibble-Zurek mechanism is the direct analogue of the transit-induced particle creation identified in Sessions 37-38. The fold transit on the SU(3) fiber constitutes a symmetry-breaking quench where the BCS condensate forms and then is destroyed, with the "quench rate" set by the geometric evolution rate $\dot{\tau}$. The freeze-out correlation length $\hat{\xi}$ determines the domain structure of the post-transit GGE relic, and the scaling law $\ell \propto \tau_Q^{-\nu}$ governs the density of topological excitations (quasiparticle pairs) produced during transit. The key distinction between thermal activation (Ginzburg) and dynamical freeze-out (Zurek) maps directly onto the framework's distinction between equilibrium BCS and the non-equilibrium instanton gas: the relevant physics is the transit dynamics, not the static potential landscape.
