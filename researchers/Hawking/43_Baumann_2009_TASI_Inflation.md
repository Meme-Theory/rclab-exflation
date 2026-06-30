# TASI Lectures on Inflation

**Author(s):** Daniel Baumann
**Year:** 2009
**Journal:** Published in TASI 2009 proceedings; arXiv preprint
**arXiv:** 0907.5424
**Relevance:** MEDIUM

---

## Abstract

In a series of five lectures I review inflationary cosmology. I begin with a description of the initial conditions problems of the Friedmann-Robertson-Walker (FRW) cosmology and then explain how inflation, an early period of accelerated expansion, solves these problems. Next, I describe how inflation transforms microscopic quantum fluctuations into macroscopic seeds for cosmological structure formation. I present in full detail the famous calculation for the primordial spectra of scalar and tensor fluctuations. I then define the inverse problem of extracting information on the inflationary era from observations of cosmic microwave background fluctuations. The current observational evidence for inflation and opportunities for future tests of inflation are discussed. Finally, I review the challenge of relating inflation to fundamental physics by giving an account of inflation in string theory.

---

## Key Arguments and Derivations

### Lecture 1: Classical Dynamics of Inflation

**FRW Cosmology.** The homogeneous, isotropic universe is described by the FRW metric:

$$ds^2 = -dt^2 + a^2(t)\left[\frac{dr^2}{1-kr^2} + r^2(d\theta^2 + \sin^2\theta \, d\phi^2)\right]$$

The Hubble parameter $H \equiv \dot{a}/a$ sets the fundamental scale. Conformal time $\tau = \int dt/a(t)$ simplifies the causal structure: null geodesics are straight lines at $\pm 45^\circ$ in the $(\tau, \chi)$ plane. The comoving particle horizon is $\chi_p(\tau) = \tau - \tau_i$.

**Friedmann Equations.** From the Einstein equations with a perfect fluid ($T^{\mu\nu} = (\rho+p)u^\mu u^\nu + p g^{\mu\nu}$):

$$H^2 = \frac{\rho}{3} - \frac{k}{a^2}$$

$$\dot{H} + H^2 = -\frac{1}{6}(\rho + 3p)$$

The continuity equation: $\dot{\rho} + 3H(\rho + p) = 0$, giving $\rho \propto a^{-3(1+w)}$ for equation of state $w = p/\rho$. Scale factor evolution: $a(t) \propto t^{2/3(1+w)}$ for $w \neq -1$, and $a(t) \propto e^{Ht}$ for $w = -1$.

**Big Bang Puzzles.** The horizon problem: the CMB is uniform to $10^{-5}$ across $\sim 10^4$ causally disconnected patches. The flatness problem: $|\Omega - 1|$ must be tuned to $\lesssim 10^{-60}$ at the Planck epoch.

**Inflation as Solution.** Inflation is defined by a shrinking comoving Hubble sphere: $d(aH)^{-1}/dt < 0$, equivalent to $\ddot{a} > 0$ (accelerated expansion) and $w < -1/3$. During inflation, the comoving Hubble radius shrinks, allowing the entire observable universe to emerge from a single causal patch.

**Slow-Roll Inflation.** A scalar field $\phi$ (the inflaton) with potential $V(\phi)$ drives inflation when the slow-roll conditions hold:

$$\epsilon \equiv -\frac{\dot{H}}{H^2} = \frac{1}{2}\left(\frac{V'}{V}\right)^2 \ll 1, \quad \eta \equiv \frac{V''}{V} \ll 1$$

where $'$ denotes $d/d\phi$ (in Planck units $M_{pl} = 1$). The number of e-folds: $N = \int H \, dt \approx \int \frac{V}{V'} d\phi$.

### Lecture 2: Quantum Fluctuations during Inflation

**Cosmological Perturbation Theory.** Metric perturbations decompose into scalars, vectors, and tensors. The gauge-invariant comoving curvature perturbation $\mathcal{R}$ is conserved on superhorizon scales. The Mukhanov-Sasaki variable $v = z\mathcal{R}$ (with $z = a\dot{\phi}/H$) satisfies:

$$v'' + \left(k^2 - \frac{z''}{z}\right)v = 0$$

In de Sitter ($z''/z \approx 2/\tau^2$), the Bunch-Davies vacuum mode function is:

$$v_k = \frac{e^{-ik\tau}}{\sqrt{2k}}\left(1 - \frac{i}{k\tau}\right)$$

**Scalar Power Spectrum.** On superhorizon scales ($|k\tau| \ll 1$):

$$\Delta_s^2(k) = \frac{k^3}{2\pi^2}|\mathcal{R}_k|^2 = \frac{1}{8\pi^2}\frac{H^2}{\epsilon M_{pl}^2}\bigg|_{k=aH}$$

**Tensor Power Spectrum.** Gravitational waves $h_{ij}$ satisfy a similar equation. Two polarizations give:

$$\Delta_t^2(k) = \frac{2}{\pi^2}\frac{H^2}{M_{pl}^2}\bigg|_{k=aH}$$

**Tensor-to-Scalar Ratio.** $r \equiv \Delta_t^2/\Delta_s^2 = 16\epsilon$.

**Spectral Indices.** The scale dependence is parametrized by:

$$n_s - 1 \equiv \frac{d\ln\Delta_s^2}{d\ln k} = -6\epsilon + 2\eta$$

$$n_t \equiv \frac{d\ln\Delta_t^2}{d\ln k} = -2\epsilon$$

The consistency relation $r = -8n_t$ is a hallmark prediction of single-field slow-roll inflation.

**Lyth Bound.** The field excursion during inflation is related to $r$:

$$\frac{\Delta\phi}{M_{pl}} \geq \left(\frac{r}{0.01}\right)^{1/2}$$

Detectable tensors ($r > 0.01$) require super-Planckian field excursions.

### Lecture 3: Contact with Observations

The primordial spectra are related to CMB observables via transfer functions. The scalar spectrum determines the CMB temperature anisotropy power spectrum $C_\ell^{TT}$. The tensor spectrum produces B-mode polarization. Observational constraints (circa 2009): $n_s = 0.960 \pm 0.013$ (WMAP5), consistent with slow-roll prediction $n_s < 1$; no detection of $r$, with $r < 0.22$ (95% CL).

### Lecture 4: Primordial Non-Gaussianity

The bispectrum $B(k_1, k_2, k_3)$ parametrizes non-Gaussian correlations. The amplitude $f_{NL}$ characterizes the departure from Gaussianity. The Maldacena theorem: for single-field slow-roll inflation, $f_{NL} \sim \mathcal{O}(\epsilon, \eta) \ll 1$ -- unobservably small. Large non-Gaussianity requires higher-derivative interactions, multiple fields, or non-standard initial states.

### Lecture 5: Inflation in String Theory

The eta problem: generic Planck-suppressed corrections to the inflaton potential $\Delta V \sim V \cdot \phi^2/M_{pl}^2$ give $\eta \sim 1$, spoiling slow-roll. String theory models (warped D-brane inflation, axion monodromy) attempt to address this but face significant challenges. The UV sensitivity of inflation makes it a probe of Planck-scale physics.

---

## Key Results

1. Pedagogical derivation of the full primordial perturbation spectra (scalar and tensor) from first principles, including quantization in de Sitter space.
2. Slow-roll parameters $\epsilon$ and $\eta$ control both the dynamics and the observational predictions: $n_s - 1 = -6\epsilon + 2\eta$, $r = 16\epsilon$.
3. The consistency relation $r = -8n_t$ uniquely identifies single-field slow-roll inflation.
4. The Lyth bound connects the tensor-to-scalar ratio to super-Planckian field excursions: detectable $r$ requires $\Delta\phi > M_{pl}$.
5. The Maldacena theorem: single-field slow-roll inflation produces negligible non-Gaussianity, $f_{NL} \sim \mathcal{O}(\epsilon, \eta)$.
6. The eta problem: UV-sensitive corrections generically spoil slow-roll, making inflation sensitive to Planck-scale physics.
7. Comprehensive presentation of the connection between primordial spectra and CMB/LSS observables via transfer functions.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| FRW metric | $ds^2 = -dt^2 + a^2(t)\left[\frac{dr^2}{1-kr^2} + r^2 d\Omega^2\right]$ | Eq. (1) |
| Hubble parameter | $H \equiv \dot{a}/a$ | Eq. (4) |
| Conformal time | $\tau = \int dt/a(t)$ | Eq. (5) |
| Friedmann equation | $H^2 = \rho/3 - k/a^2$ | Eq. (21) |
| Acceleration equation | $\dot{H} + H^2 = -(\rho + 3p)/6$ | Eq. (22) |
| Continuity equation | $\dot{\rho} + 3H(\rho + p) = 0$ | Eq. (23) |
| Slow-roll parameter $\epsilon$ | $\epsilon = -\dot{H}/H^2 = \frac{1}{2}(V'/V)^2$ | Lecture 1, Sec. 6.2 |
| Slow-roll parameter $\eta$ | $\eta = V''/V$ | Lecture 1, Sec. 6.2 |
| Mukhanov-Sasaki equation | $v'' + (k^2 - z''/z)v = 0$ | Lecture 2, Sec. 12.2 |
| Scalar power spectrum | $\Delta_s^2 = \frac{1}{8\pi^2}\frac{H^2}{\epsilon M_{pl}^2}\big|_{k=aH}$ | Lecture 2, Sec. 12.2 |
| Tensor power spectrum | $\Delta_t^2 = \frac{2}{\pi^2}\frac{H^2}{M_{pl}^2}\big|_{k=aH}$ | Lecture 2, Sec. 12.3 |
| Tensor-to-scalar ratio | $r = 16\epsilon$ | Lecture 2, Sec. 12.4 |
| Scalar spectral index | $n_s - 1 = -6\epsilon + 2\eta$ | Lecture 2, Sec. 13.2 |
| Consistency relation | $r = -8n_t$ | Lecture 2, Sec. 13.2 |
| Lyth bound | $\Delta\phi/M_{pl} \geq (r/0.01)^{1/2}$ | Lecture 2, Sec. 12.5 |

---

## Relevance to Phonon-Exflation

The standard inflationary perturbation theory presented here provides the benchmark against which the phonon-exflation framework must be compared. The framework's NS-TILT-42 test yielded $n_s = 0.746$ versus the Planck measurement $n_s = 0.9649 \pm 0.0042$, a decisive FAIL confirming that the framework does not produce standard slow-roll inflation. The Mukhanov-Sasaki equation and its quantization are structurally analogous to the framework's treatment of fluctuations on the $M_4 \times SU(3)$ background, but the tau-evolution (internal modulus dynamics) replaces the inflaton potential. The eta problem highlighted in Lecture 5 is relevant: Planck-suppressed corrections to the effective potential are precisely the kind of UV sensitivity that the spectral action formulation of the framework is designed to avoid. The Friedmann equations and energy conditions connect directly to the Hawking-Penrose singularity theorem context of paper 01.
