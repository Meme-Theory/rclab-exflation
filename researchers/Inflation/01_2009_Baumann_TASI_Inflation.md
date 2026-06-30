# TASI Lectures on Inflation

**Author(s):** Daniel Baumann
**Year:** 2009 (revised 2012)
**Journal:** Delivered at TASI 2009; arXiv preprint
**arXiv:** 0907.5424
**Relevance:** CRITICAL -- canonical pedagogical reference for the inflationary formalism; defines the slow-roll framework, derives primordial scalar and tensor power spectra from first principles, and establishes the observational pipeline from quantum fluctuations to CMB anisotropies

---

## Abstract

In a series of five lectures I review inflationary cosmology. I begin with a description of the initial conditions problems of the Friedmann-Robertson-Walker (FRW) cosmology and then explain how inflation, an early period of accelerated expansion, solves these problems. Next, I describe how inflation transforms microscopic quantum fluctuations into macroscopic seeds for cosmological structure formation. I present in full detail the famous calculation for the primordial spectra of scalar and tensor fluctuations. I then define the inverse problem of extracting information on the inflationary era from observations of cosmic microwave background fluctuations. The current observational evidence for inflation and opportunities for future tests of inflation are discussed. Finally, I review the challenge of relating inflation to fundamental physics by giving an account of inflation in string theory.

---

## Key Arguments and Derivations

### Lecture 1: Classical Dynamics of Inflation (pp. 15-40)

**FRW Review.** The homogeneous universe is described by the FRW metric with scale factor $a(t)$, Hubble parameter $H = \dot{a}/a$, and Friedmann equations $H^2 = \frac{1}{3}\rho - k/a^2$ and $\dot{H} + H^2 = -\frac{1}{6}(\rho + 3p)$. The concordance model has $\Omega_b = 0.04$, $\Omega_{dm} = 0.23$, $\Omega_\Lambda = 0.72$.

**Big Bang Puzzles.** The horizon problem arises because the comoving Hubble radius $(aH)^{-1}$ grows monotonically in standard cosmology, so the CMB last-scattering surface consists of $\sim 10^5$ causally disconnected regions. The flatness problem follows from $|1 - \Omega(a)| = 1/(aH)^2$: since $(aH)^{-1}$ grows, $\Omega = 1$ is an unstable fixed point requiring $|\Omega(a_{\rm pl}) - 1| \leq \mathcal{O}(10^{-61})$.

**Inflation as Shrinking Hubble Sphere.** The central insight: require $d(aH)^{-1}/dt < 0$. This is equivalent to accelerated expansion $\ddot{a} > 0$ and to violation of the strong energy condition $\rho + 3p < 0$. Inflation drives $\Omega \to 1$ (attractor) and extends conformal time to $\tau_i \to -\infty$, resolving the horizon problem by allowing past light cones to intersect.

**Scalar Field Dynamics.** A minimally coupled scalar field $\phi$ with action $S = \int d^4x \sqrt{-g}[\frac{1}{2}R + \frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - V(\phi)]$ has energy density $\rho_\phi = \frac{1}{2}\dot\phi^2 + V$ and pressure $p_\phi = \frac{1}{2}\dot\phi^2 - V$. When $\dot\phi^2 \ll V$, the equation of state $w_\phi \approx -1$ and inflation occurs.

**Slow-Roll Conditions.** The potential slow-roll parameters $\epsilon_v \equiv \frac{M_{\rm pl}^2}{2}\left(\frac{V_{,\phi}}{V}\right)^2$ and $\eta_v \equiv M_{\rm pl}^2 \frac{V_{,\phi\phi}}{V}$ must satisfy $\epsilon_v, |\eta_v| \ll 1$. Inflation ends when $\epsilon(\phi_{\rm end}) \equiv 1$. The number of e-folds is $N(\phi) = \int_{\phi_{\rm end}}^{\phi} \frac{d\phi}{\sqrt{2\epsilon_v}}$, requiring $N_{\rm tot} \gtrsim 60$.

**Models.** Large-field models ($V = \lambda_p \phi^p$, including $m^2\phi^2$) require super-Planckian field excursions. Small-field models arise from spontaneous symmetry breaking. Natural inflation uses an axion-like cosine potential.

### Lecture 2: Quantum Fluctuations during Inflation (pp. 43-67)

**Cosmological Perturbation Theory.** Perturbations decompose into scalar, vector, and tensor modes (SVT decomposition). Key gauge-invariant scalars: the curvature perturbation on uniform-density hypersurfaces $-\zeta \equiv \Psi + \frac{H}{\dot{\bar\rho}}\delta\rho$ and the comoving curvature perturbation $\mathcal{R} \equiv \Psi + \frac{H}{\dot{\bar\phi}}\delta\phi$. Both are conserved on superhorizon scales ($k \ll aH$) for adiabatic perturbations.

**Mukhanov Variable and Mode Equation.** Expanding the action to second order in $\mathcal{R}$ gives $S_{(2)} = \frac{1}{2}\int d^4x\, a^3 \frac{\dot\phi^2}{H^2}[\dot{\mathcal{R}}^2 - a^{-2}(\partial_i\mathcal{R})^2]$. Defining $v \equiv z\mathcal{R}$ with $z^2 = 2a^2\epsilon$ and switching to conformal time yields the Mukhanov equation: $v_k'' + (k^2 - z''/z)v_k = 0$.

**Quantization and Bunch-Davies Vacuum.** The field $v$ is promoted to a quantum operator with standard commutation relations. The vacuum is fixed by demanding the mode functions match the Minkowski vacuum on subhorizon scales: $\lim_{\tau \to -\infty} v_k = \frac{e^{-ik\tau}}{\sqrt{2k}}$. In de Sitter ($z''/z = 2/\tau^2$), the exact solution is $v_k = \frac{e^{-ik\tau}}{\sqrt{2k}}\left(1 - \frac{i}{k\tau}\right)$.

**Scalar Power Spectrum.** On superhorizon scales ($|k\tau| \ll 1$), the power spectrum of $\mathcal{R}$ at horizon crossing ($k = aH$) is $\Delta_s^2(k) = \frac{H_\star^2}{(2\pi)^2}\frac{H_\star^2}{\dot\phi_\star^2} = \frac{1}{8\pi^2}\frac{H^2}{M_{\rm pl}^2}\frac{1}{\epsilon}\big|_{k=aH}$.

**Tensor Power Spectrum.** Each gravitational wave polarization satisfies the same mode equation as a massless scalar. The total tensor spectrum is $\Delta_t^2(k) = \frac{2}{\pi^2}\frac{H_\star^2}{M_{\rm pl}^2}$.

**Spectral Indices.** $n_s - 1 = 2\eta_\star - 4\epsilon_\star$ (scalars), $n_t = -2\epsilon_\star$ (tensors). The tensor-to-scalar ratio $r = 16\epsilon_\star$ satisfies the consistency relation $r = -8n_t$. The Lyth bound relates $r$ to field excursion: $\Delta\phi/M_{\rm pl} \sim (r/0.01)^{1/2}$.

### Lecture 3: Contact with Observations (pp. 68-89)

**Transfer Functions.** The primordial spectra are related to observables via $\mathcal{Q}_k(\tau) = T_{\mathcal{Q}}(k, \tau, \tau_\star)\mathcal{R}_k(\tau_\star)$. The CMB angular power spectra are $C_\ell^{XY} = \frac{2}{\pi}\int k^2 dk\, P(k)\, \Delta_{X\ell}(k)\Delta_{Y\ell}(k)$ where $\Delta_{X\ell}$ are line-of-sight integrals over source terms and projection factors.

**LSS.** The matter power spectrum $P_\delta(k,\tau) = \frac{4}{25}(k/aH)^4 T_\delta^2(k,\tau)P_{\mathcal{R}}(k)$.

**Observational Evidence.** Flatness ($\Omega_k \sim 0$), coherent superhorizon fluctuations (acoustic peaks, TE anti-correlation at $\ell < 100$), nearly scale-invariant, Gaussian, adiabatic perturbations all consistent with simplest inflationary predictions.

### Lecture 4: Primordial Non-Gaussianity (pp. 90-100)

**Bispectrum.** The three-point function defines $\langle\mathcal{R}_{k_1}\mathcal{R}_{k_2}\mathcal{R}_{k_3}\rangle = (2\pi)^3\delta(\sum k_i)B_\mathcal{R}(k_1,k_2,k_3)$. Different momentum configurations (local, equilateral, folded) diagnose different physical mechanisms. The Maldacena theorem: for single-field slow-roll, $f_{\rm NL} \sim \mathcal{O}(\epsilon, \eta)$, unobservably small. Large non-Gaussianity requires higher-derivative interactions, multiple fields, or non-standard vacua.

### Lecture 5: Inflation in String Theory (pp. 101-122)

**UV Sensitivity.** The eta problem: Planck-suppressed dimension-six operators $\Delta V \sim V\phi^2/M_{\rm pl}^2$ generically give $\Delta\eta_v \sim 1$, spoiling slow-roll. The Lyth bound demands super-Planckian field ranges for observable tensors, requiring shift symmetry protection.

**Case Studies.** Warped D-brane inflation (inflaton = D3-brane position in a warped throat; small-field, computable eta problem). Axion monodromy inflation (inflaton = axion with broken discrete shift symmetry; large-field, $V \propto \phi^{2/3}$, observable $r$).

---

## Key Results

1. Inflation is defined by a shrinking comoving Hubble radius: $d(aH)^{-1}/dt < 0$, equivalent to $\ddot{a} > 0$ and $\rho + 3p < 0$.
2. The slow-roll conditions $\epsilon_v, |\eta_v| \ll 1$ ensure sustained accelerated expansion; inflation ends when $\epsilon(\phi_{\rm end}) = 1$.
3. The scalar power spectrum from quantum fluctuations: $\Delta_s^2 = \frac{1}{8\pi^2}\frac{H^2}{M_{\rm pl}^2\epsilon}\big|_{k=aH}$.
4. The tensor power spectrum: $\Delta_t^2 = \frac{2}{\pi^2}\frac{H^2}{M_{\rm pl}^2}\big|_{k=aH}$.
5. Spectral tilt: $n_s - 1 = 2\eta_v - 6\epsilon_v$; tensor tilt: $n_t = -2\epsilon_v$; tensor-to-scalar ratio: $r = 16\epsilon_v$.
6. Consistency relation for single-field slow-roll: $r = -8n_t$.
7. Lyth bound: $\Delta\phi/M_{\rm pl} \sim (r/0.01)^{1/2}$; observable gravitational waves require super-Planckian field excursion.
8. Energy scale of inflation: $V^{1/4} \sim (r/0.01)^{1/4} \times 10^{16}$ GeV.
9. For $m^2\phi^2$ inflation: $n_s = 1 - 2/N_{\rm cmb} \approx 0.96$, $r = 8/N_{\rm cmb} \approx 0.13$.
10. The Maldacena theorem: single-field slow-roll inflation predicts $f_{\rm NL} \sim \mathcal{O}(\epsilon, \eta)$, undetectably small.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FRW metric | $ds^2 = -dt^2 + a^2(t)\left[\frac{dr^2}{1-kr^2} + r^2 d\Omega^2\right]$ | Eq. (1) |
| Friedmann equation | $H^2 = \frac{1}{3}\rho - \frac{k}{a^2}$ | Eq. (21) |
| Acceleration equation | $\frac{\ddot{a}}{a} = -\frac{1}{6}(\rho + 3p)$ | Eq. (22) |
| Continuity equation | $\dot\rho + 3H(\rho + p) = 0$ | Eq. (23) |
| Conformal time | $\tau = \int \frac{dt}{a(t)}$ | Eq. (5) |
| Comoving horizon | $\tau = \int_0^a d\ln a' \frac{1}{a'H(a')}$ | Eq. (36) |
| Inflation condition | $\frac{d}{dt}\left(\frac{1}{aH}\right) < 0 \;\Rightarrow\; \ddot{a} > 0 \;\Rightarrow\; \rho + 3p < 0$ | Eq. (50) |
| Inflaton action | $S = \int d^4x\sqrt{-g}\left[\frac{1}{2}R + \frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - V(\phi)\right]$ | Eq. (61) |
| Inflaton energy/pressure | $\rho_\phi = \frac{1}{2}\dot\phi^2 + V,\quad p_\phi = \frac{1}{2}\dot\phi^2 - V$ | Eqs. (64)-(65) |
| Slow-roll parameter $\epsilon$ | $\epsilon \equiv -\frac{\dot H}{H^2} = \frac{1}{2}\frac{\dot\phi^2}{H^2}$ | Eq. (70) |
| Potential slow-roll $\epsilon_v$ | $\epsilon_v \equiv \frac{M_{\rm pl}^2}{2}\left(\frac{V_{,\phi}}{V}\right)^2$ | Eq. (74) |
| Potential slow-roll $\eta_v$ | $\eta_v \equiv M_{\rm pl}^2 \frac{V_{,\phi\phi}}{V}$ | Eq. (75) |
| Number of e-folds | $N(\phi) = \int_{\phi_{\rm end}}^{\phi}\frac{d\phi}{\sqrt{2\epsilon_v}}$ | Eq. (83) |
| Comoving curvature perturbation | $\mathcal{R} = \Psi + \frac{H}{\dot{\bar\phi}}\delta\phi$ | Eq. (140) |
| Mukhanov variable | $v \equiv z\mathcal{R},\quad z^2 = 2a^2\epsilon$ | Eq. (182) |
| Mukhanov equation | $v_k'' + \left(k^2 - \frac{z''}{z}\right)v_k = 0$ | Eq. (185) |
| Bunch-Davies vacuum | $\lim_{\tau\to-\infty} v_k = \frac{e^{-ik\tau}}{\sqrt{2k}}$ | Eq. (192) |
| de Sitter mode function | $v_k = \frac{e^{-ik\tau}}{\sqrt{2k}}\left(1 - \frac{i}{k\tau}\right)$ | Eq. (196) |
| Scalar power spectrum | $\Delta_s^2(k) = \frac{1}{8\pi^2}\frac{H^2}{M_{\rm pl}^2}\frac{1}{\epsilon}\bigg|_{k=aH}$ | Eq. (222) |
| Tensor power spectrum | $\Delta_t^2(k) = \frac{2}{\pi^2}\frac{H^2}{M_{\rm pl}^2}\bigg|_{k=aH}$ | Eq. (223) |
| Tensor-to-scalar ratio | $r \equiv \frac{\Delta_t^2}{\Delta_s^2} = 16\epsilon_\star$ | Eq. (225) |
| Scalar spectral index | $n_s - 1 = 2\eta_v^\star - 6\epsilon_v^\star$ | Eq. (236) |
| Tensor spectral index | $n_t = -2\epsilon_v^\star$ | Eq. (237) |
| Consistency relation | $r = -8n_t$ | Eq. (239) |
| Lyth bound | $\frac{\Delta\phi}{M_{\rm pl}} \sim \left(\frac{r}{0.01}\right)^{1/2}$ | Eq. (221) |
| Energy scale of inflation | $V^{1/4} \sim \left(\frac{r}{0.01}\right)^{1/4} 10^{16}\;\text{GeV}$ | Eq. (218) |

---

## Relevance to Phonon-Exflation

Baumann's lectures provide the complete standard-inflation formalism that the phonon-exflation framework must either reproduce or replace. Several specific contact points: (1) The Mukhanov equation $v_k'' + (k^2 - z''/z)v_k = 0$ is the direct analog of the mode equation for spectral perturbations in the exflation transit -- the exflation framework must show that its own mode equation yields $n_s \approx 0.9561$ from the spectral geometry rather than from a slow-roll potential. (2) The consistency relation $r = -8n_t$ is a falsifiable prediction of single-field slow-roll models; exflation's acoustic white-hole transit predicts this relation is INAPPLICABLE (established via 5 independent arguments in the VdD-Hawking workshop). (3) The vacuum energy problem is sidestepped here -- inflation requires $V \sim (10^{16}\;\text{GeV})^4$ but says nothing about why the late-time cosmological constant is $\sim 120$ orders of magnitude smaller. This is precisely the CC overshoot problem that is the central open question of the exflation program. (4) The Lyth bound's requirement of super-Planckian field excursions for large $r$ has no analog in exflation, where the spectral action gradient $dS/d\tau$ drives the transit without a fundamental scalar field.
