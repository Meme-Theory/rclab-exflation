# Dissipative Effects in the Effective Field Theory of Inflation

**Author(s):** Diana Lopez Nacir, Rafael A. Porto, Leonardo Senatore, Matias Zaldarriaga
**Year:** 2012
**Journal:** [not specified in PDF]
**arXiv:** 1109.4192
**Relevance:** CRITICAL

---

## Abstract

We generalize the effective field theory of single clock inflation to include dissipative effects. Working in unitary gauge we couple a set of composite operators, $\mathcal{O}_{\mu\nu\ldots}$, in the effective action which is constrained solely by invariance under time-dependent spatial diffeomorphisms. We restrict ourselves to situations where the degrees of freedom responsible for dissipation do not contribute to the density perturbations at late time. The dynamics of the perturbations is then modified by the appearance of 'friction' and noise terms, and assuming certain locality properties for the Green's functions of these composite operators, we show that there is a regime characterized by a large friction term $\gamma \gg H$ in which the $\zeta$-correlators are dominated by the noise and the power spectrum can be significantly enhanced. We also compute the three point function $\langle\zeta\zeta\zeta\rangle$ for a wide class of models and discuss under which circumstances large friction leads to an increased level of non-Gaussianities. In particular, under our assumptions, we show that strong dissipation together with the required non-linear realization of the symmetries implies $|f_{\rm NL}| \sim \frac{\gamma}{c_s^2 H} \gg 1$. As a paradigmatic example we work out a variation of the 'trapped inflation' scenario with local response functions and perform the matching with our effective theory. A detection of the generic type of signatures that result from incorporating dissipative effects during inflation, as we describe here, would teach us about the dynamics of the early universe and also extend the parameter space of inflationary models.

---

## Key Arguments and Derivations

### Section 1: Introduction and Main Results

The paper extends the EFT of inflation to incorporate dissipative effects -- friction and noise from additional degrees of freedom (ADOF) that couple to the inflaton clock but do not directly contribute to late-time density perturbations. The key paradigmatic example is "trapped inflation" where particle production modifies the inflaton evolution while the produced particles dilute away.

**1.1 Preliminaries:** The dissipative harmonic oscillator $\ddot\pi + \gamma\dot\pi + \omega_0^2\pi = J$ (eq. 2) does not derive from a Lagrangian because energy is not conserved: $dE/dt = -\gamma\dot\pi^2$ (eq. 3). The general non-local (Langevin) equation involves a memory kernel $\tilde\gamma(t-t')$, but simplifies to local form when "Ohmic" behavior holds: $\mathrm{Im}\,\tilde\gamma(\omega) \simeq \gamma\omega$ (eq. 5). The Fluctuation-Dissipation (FD) theorem relates noise amplitude to dissipation: $\nu_J \simeq \gamma T$ (eq. 10).

**1.2 The Story of $\mathcal{O}$:** Dissipation is incorporated by coupling $\pi$ to a composite operator $\mathcal{O}$: $S_{\rm int} = -\int d^4x\,\mathcal{O}(x)\pi(x)$ (eq. 11). The operator $\delta\mathcal{O}$ splits into stochastic noise $\delta\mathcal{O}_S$ and response $\delta\mathcal{O}_R$ (eq. 13). Linear response gives $\delta\mathcal{O}_R(x) = -\int d^4y\,G^{\mathcal{O}}_{\rm ret}(x,y)\pi(y)$ (eq. 14), with the retarded Green's function $G^{\mathcal{O}}_{\rm ret}(x,y) = i\langle[\delta\mathcal{O}(x),\delta\mathcal{O}(y)]\rangle\theta(t_x - t_y)$ (eq. 15). Local dissipation requires $\mathrm{Im}\,G^{\mathcal{O}}_{\rm ret}(\omega,\mathbf{0}) \simeq \gamma\omega$ (eq. 19). An "emergent shift symmetry" requires the real part of the Green's function to vanish as $\omega \to 0$, preventing a mass for $\pi$ (and thus for $\zeta$).

**1.3 The Two-Point Function:**

*Homogeneous solution:* With $\gamma \gg H$, the homogeneous solution acquires an exponential suppression factor $e^{-\gamma|t_0|/2} \ll 1$ (eq. 30), making it negligible at late times.

*Noise:* In the overdamped limit ($\omega_0 \ll \gamma$), the Green's function $G^k_\gamma(t-t') = \gamma^{-1}\exp(-\omega_0^2(t-t')/\gamma)\,\theta(t-t')$ (eq. 34) defines an equilibration time $\tau_{\rm eq}^{-1} \sim \omega_0^2/\gamma$ (eq. 35). The noise-dominated power spectrum at late times gives $\langle\pi_k\pi_q\rangle \to \nu_{\mathcal{O}}(2\pi)^3/(N_c^2\gamma\omega_0^2)\,\delta^{(3)}(\mathbf{k}+\mathbf{q})$ (eq. 39). In the expanding universe, modes freeze when $\omega_0^2/\gamma \sim H$, giving $k_\star \sim \sqrt{\gamma H/c_s^2}$ (eq. 42) and a power spectrum (eq. 43-44) that can be significantly enhanced relative to Bunch-Davies.

**1.4 Non-Linear Effects:**

*Shift symmetry (Sec. 1.4.1):* The coupling $\tilde{\mathcal{O}}\dot\pi$ together with the non-linear realization of time diffs forces a term $-\frac{1}{2}\tilde{\mathcal{O}}(\partial_i\pi)^2$ (eq. 45). This gives the EOM (eq. 46) with a $\gamma(\partial_i\pi)^2$ non-linearity. The resulting non-Gaussianity is $|f_{\rm NL}| \sim \gamma/(c_s^2 H)$ (eq. 51), verified by comparing the ratio of interaction to free terms at freezing (eq. 53).

*Approximate shift symmetry (Sec. 1.4.2):* When shift symmetry is softly broken by slow-roll parameter $\epsilon$, the coupling $-\dot{f}(t)\delta\mathcal{O}\pi$ gives $f_{\rm NL} \sim -\ddot{f}/(\dot{f}H) \sim O(\epsilon)$ (eq. 55) -- very small.

*Non-linear response (Sec. 1.4.3):* When $\bar{\mathcal{O}} = F(\dot{\bar\phi})$, general covariance forces $\partial_t\phi \to n^\mu\partial_\mu\phi = \sqrt{-({\partial\phi})^2}$ (eq. 60), giving $\dot{f}\delta\mathcal{O}_R \simeq N_c\gamma(\dot\pi + \frac{\alpha}{2}\dot\pi^2 - \frac{1}{2}(\partial_i\pi)^2 + \ldots)$ (eq. 59). The $\gamma(\partial_i\pi)^2$ term in the EOM again yields $|f_{\rm NL}| \sim \gamma/(c_s^2 H)$ (eq. 61).

*Non-Gaussian noise (Sec. 1.4.4):* If the noise three-point function is local, $f_{\rm NL} \sim \gamma\nu_{\mathcal{O}^3}N_c/(\dot{f}\nu_{\mathcal{O}}^2)$ (eq. 64), which can also be large.

### Sections 2-3: EFT Setup and Adding New Degrees of Freedom

The EFT unitary gauge action (eq. 65) is the standard Cheung et al. construction. The Stuckelberg trick introduces $\pi$ via $t \to t - \pi$ (eq. 71). The quadratic action (eq. 76) involves normalization $N_c$ and speed of sound $c_s$ (eq. 77). When ADOF contribute to the background stress-energy, the authors use a modified unitary gauge where the physical clock controlling the end of inflation is uniform (not the total Goldstone boson), preserving $\zeta \simeq -H\pi$.

### Section 4: Interaction Terms in Unitary Gauge

Composite operators $\mathcal{O}$ (scalar), $\mathcal{O}_\mu$ (vector), and $\mathcal{O}_{\mu\nu}$ (tensor) are coupled to metric perturbations in unitary gauge. For scalars, the leading couplings are $\mathcal{O}\delta g^{00}$ and $f(t)\mathcal{O}$.

### Sections 5-7: Modified Dynamics, Power Spectrum, and Non-Gaussianities

The detailed computation confirms all the heuristic results from Section 1. The power spectrum is noise-dominated for $\gamma \gg H$. Non-Gaussianities from $\mathcal{O}\delta g^{00}$ coupling (Sec. 7.1), linear response of $f(t)\mathcal{O}$ (Sec. 7.2), and non-linear response (Sec. 7.3) are all computed, confirming $|f_{\rm NL}| \sim \gamma/(c_s^2 H)$ for the generic case with a preferred clock.

### Section 8: Matching -- Local Trapped Inflation

The trapped inflation scenario $f(t)\mathcal{O} \to \sum_i(\phi - \phi_i)^2\chi_i^2 + \mathcal{L}(\chi_i)$ is matched to the EFT. Particles $\chi_i$ are produced when the adiabaticity condition is violated as $\phi$ crosses thresholds $\phi_i$. The dissipation coefficient is $\gamma \sim g^2\dot\phi/\Delta$, where $\Delta$ is the spacing between thresholds. The matching confirms the EFT predictions.

---

## Key Results

1. The EFT of inflation can be extended to include dissipative effects by coupling composite operators $\mathcal{O}_{\mu\nu\ldots}$ to the metric in unitary gauge, constrained only by spatial diffeomorphism invariance.

2. In the strong dissipation regime ($\gamma \gg H$), the homogeneous (Bunch-Davies) contribution to the power spectrum is exponentially suppressed; the noise from ADOF dominates.

3. The noise-dominated power spectrum can be significantly enhanced relative to standard inflation, with modes freezing at $c_s k_\star \simeq \sqrt{\gamma H}$ rather than $H$.

4. The non-linear realization of time diffeomorphisms forces a connection between dissipation and non-Gaussianity: $|f_{\rm NL}| \sim \gamma/(c_s^2 H) \gg 1$ for $\gamma \gg H$.

5. Three sources of non-Gaussianity are identified: (a) non-linear couplings forced by symmetry, (b) non-linear response of the composite operators, (c) intrinsic non-Gaussianity of the noise.

6. The formalism is matched to a local version of trapped inflation, confirming the generic predictions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Dissipative EOM | $\ddot\pi + \gamma\dot\pi + \omega_0^2\pi = J$ | Eq. (2) |
| Energy dissipation | $dE/dt = -\gamma\dot\pi^2$ | Eq. (3) |
| Langevin equation | $\ddot\pi + \omega_0^2\pi + \int dt'\tilde\gamma(t-t')\pi(t') = J(t)$ | Eq. (4) |
| Ohmic condition | $\mathrm{Im}\,\tilde\gamma(\omega) \simeq \gamma\omega$ | Eq. (5) |
| Dissipative coupling | $S_{\rm int} = -\int d^4x\,\mathcal{O}(x)\pi(x)$ | Eq. (11) |
| Linear response | $\delta\mathcal{O}_R(x) = -\int d^4y\,G^{\mathcal{O}}_{\rm ret}(x,y)\pi(y)$ | Eq. (14) |
| Retarded Green's function | $G^{\mathcal{O}}_{\rm ret}(x,y) = i\langle[\delta\mathcal{O}(x),\delta\mathcal{O}(y)]\rangle\theta(t_x-t_y)$ | Eq. (15) |
| Local dissipation condition | $\mathrm{Im}\,G^{\mathcal{O}}_{\rm ret}(\omega,\mathbf{0}) \simeq \gamma\omega$ | Eq. (19) |
| White noise | $\langle\delta\mathcal{O}_S(\mathbf{k},t')\delta\mathcal{O}_S(\mathbf{q},t)\rangle = (2\pi)^3\nu_{\mathcal{O}}\delta(t-t')\delta^{(3)}(\mathbf{k}+\mathbf{q})$ | Eq. (22) |
| FD theorem | $\gamma = \nu_{\mathcal{O}}/T$ | Eq. (23) |
| Standard power spectrum | $\langle\zeta_k\zeta_q\rangle_{\rm BD} = (2\pi)^3\frac{H_\star^2}{4c_s^\star\epsilon_\star M_p^2 k^3}\delta^{(3)}(\mathbf{q}+\mathbf{k})$ | Eq. (25) |
| Overdamped Green's function | $G^k_\gamma(t-t') = \frac{1}{\gamma}e^{-\frac{\omega_0^2}{\gamma}(t-t')}\theta(t-t')$ | Eq. (34) |
| Equilibration time | $\tau_{\rm eq}^{-1} \sim \omega_0^2/\gamma$ | Eq. (35) |
| Noise power spectrum | $\langle\pi_k\pi_q\rangle \to \frac{\nu_{\mathcal{O}}(2\pi)^3}{N_c^2\gamma\omega_0^2}\delta^{(3)}(\mathbf{k}+\mathbf{q})$ | Eq. (39) |
| Freezing condition | $k_\star \sim \sqrt{\gamma H/c_s^2}$ | Eq. (42) |
| Symmetry-forced non-linearity | $-\frac{1}{2}\tilde{\mathcal{O}}(\partial_i\pi)^2$ | Eq. (45) |
| Non-Gaussianity (main result) | $\|f_{\rm NL}\| \sim \frac{\gamma}{c_s^2 H}$ | Eq. (51) |
| Non-linear response | $\dot{f}\delta\mathcal{O}_R \simeq N_c\gamma\left(\dot\pi + \frac{\alpha}{2}\dot\pi^2 - \frac{1}{2}(\partial_i\pi)^2 + \ldots\right)$ | Eq. (59) |
| Covariant derivative | $\partial_t\phi \to n^\mu\partial_\mu\phi = \sqrt{-(\partial\phi)^2}$ | Eq. (60) |

---

## Relevance to Phonon-Exflation

This paper is directly relevant to the phonon-exflation framework's GGE relic formation mechanism. The exflation transit is a strongly dissipative event: the Mach 13.75 supersonic passage through the van Hove fold produces 59.8 quasiparticle pairs (Parker pair production, $P_{\rm exc} = 1.000$), which is precisely the kind of particle production that creates ADOF in the trapped inflation paradigm. The friction coefficient $\gamma$ maps onto the acoustic impedance mismatch at the fold ($\Gamma = 0.99970$), and the noise term maps onto the stochastic force from the produced GGE excitations. The paper's central result -- $|f_{\rm NL}| \sim \gamma/(c_s^2 H)$ -- provides a concrete prediction framework for the non-Gaussianity of the GGE relic's contribution to curvature perturbations. The connection between dissipation and non-Gaussianity through the non-linear realization of time diffs is structurally identical to how the spectral action's non-linear structure forces correlations between the transit dynamics and the resulting perturbation spectrum.
