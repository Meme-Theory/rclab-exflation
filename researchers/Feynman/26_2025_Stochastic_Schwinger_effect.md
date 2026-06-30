# The Stochastic Schwinger Effect

**Author(s):** Lucas Vicente García-Consuegra, Azadeh Maleknejad
**Year:** 2025 (v2 Feb 2026; v1 Oct 2025)
**Journal:** Submitted to JHEP (KCL-PH-TH/2025-41)
**arXiv/DOI:** arXiv:2510.14468v2
**Relevance:** MEDIUM

---

## Abstract

We formulate a stochastic generalisation of the Schwinger effect, extending pair production to statistically fluctuating gauge-field backgrounds. Our approach captures realistic field configurations that are transient, inhomogeneous, and stochastic, as commonly encountered in cosmological and high-energy astrophysical settings. Using the effective action formalism, we compute the vacuum decay rate and number density of charged particles, obtaining closed-form analytical expressions for both scalar and fermionic cases. To isolate the essential physics, the analysis is performed in flat spacetime and at zero temperature, providing a controlled setting in which curvature and thermal effects can be neglected. As a proof of concept, we present representative phenomenological examples relevant to astrophysical plasmas and early-Universe–motivated scenarios.

---

## Key Arguments and Derivations

**Classification of Schwinger-type mechanisms (Table 1).** Distinguishes deterministic (classical) backgrounds — static, inhomogeneous, dynamically assisted, thermally assisted — from quantum Breit–Wheeler and the new stochastic channel. Stochastic is perturbatively accessible like Breit–Wheeler but driven by classical stochastic backgrounds rather than real quanta or thermal baths.

**Motivation.** Static field configurations at Schwinger-scale magnitudes are unlikely in realistic cosmological/astrophysical settings. Lattice simulations of reheating and inflation produce highly stochastic gauge fields, necessitating a stochastic pair-production framework.

**Section 2: Setup.** Complex scalar $\phi$ or fermion $\psi$ coupled to $U(1)$ gauge field via $D_\mu = \partial_\mu + igQA_\mu$. Gauge sector can be Maxwell (Eq. 2.2) or Proca (dark photon, Eq. 2.3). Matter Lagrangians: $\mathcal{L}_\phi = -(D_\mu\phi)(D^\mu\phi)^* - m^2|\phi|^2$ (Eq. 2.4); $\mathcal{L}_\psi = i\bar\psi(D\!\!\!/ - m)\psi$ (Eq. 2.5).

Quantum effective action derived from partition function with external sources; vacuum persistence $\mathcal{P} = e^{-2\,\text{Im}\,\Gamma}$ (Eq. 2.9); decay probability $\mathcal{P}_{\text{decay}} = 1 - \mathcal{P} \simeq 2\,\text{Im}\,\Gamma = 2\int d^4x\,w(x)$ (Eq. 2.10).

One-loop effective actions (scalar Eq. 2.13, fermion Eq. 2.14) in proper-time representation (Eq. 2.15). Static Euler–Heisenberg results recalled (Eqs. 2.16–2.19).

**Section 3: Stochastic formalism.** Gauge field promoted to operator-valued Gaussian stochastic process with $\langle\hat{A}_\mu(x)\rangle_s = 0$, $\langle\hat{A}_\mu(x)\hat{A}_\nu(y)\rangle_s = G_{\mu\nu}(x-y)$ (Eq. 3.1). Mode decomposition Eq. 3.3 with polarization vectors and stochastic amplitudes $\alpha_{q,\sigma}$ satisfying $\langle\alpha_{q,\sigma}\alpha^*_{q',\sigma'}\rangle_s = \delta_{\sigma\sigma'}\delta^3(q-q')$ (Eq. 3.5).

Combined quantum+stochastic average $\langle\ldots\rangle = \int\mathcal{D}A\,P[A]\langle 0_{\text{in}}|\ldots|0_{\text{in}}\rangle_A$ (Eq. 3.6). Effective action (Eq. 3.11) expanded perturbatively in $g$; scalar decay probability Eq. 3.12, fermion Eq. 3.13.

**3.1 Stationary background.** Four-momentum Fourier expansion valid. Vacuum decay probability for scalars:
$\mathcal{P}^b_{\text{decay}} = (g^2 Q^2\pi/3)\int_q \Theta(-q^2-4m^2)(1+4m^2/q^2)^{3/2}\langle-\hat{F}_{\mu\nu}(q)\hat{F}^{\mu\nu}(-q)\rangle$ (Eq. 3.16).

Spectral number density for scalar particles (Eq. 3.17) and fermions (Eq. 3.18) feature kinematic threshold $\omega^2 > |\mathbf{q}|^2 + 4m^2$. Production rates scale as $g^2 Q^2$ and are proportional to the spectral intensity of field fluctuations.

**3.2 Non-stationary background.** Three-momentum decomposition (Eq. 3.19) with time-dependent mode functions; windowed/short-time Fourier transform used for transient backgrounds (preheating, magnetogenesis, phase transitions, magnetars, pulsar winds, turbulent plasmas).

**Sections 4–6.** Phenomenological applications: astrophysical plasmas (EM modes in cold medium, dark-photon DM background), axion–gauge field reheating, and comparative efficiency of static vs stochastic channels.

## Key Results

1. New pair-production mechanism: vacuum decay into charged pairs driven by stochastic classical Abelian backgrounds with $\langle A_\mu\rangle = 0$ but non-trivial correlator $G_{\mu\nu}$.
2. Closed-form analytic expressions for vacuum decay rate and number density for both scalar and fermionic charged matter.
3. Kinematic threshold $\omega^2 > |\mathbf{q}|^2 + 4m^2$: only background modes above twice rest mass contribute.
4. Perturbative contribution vanishes for strictly constant EM field, as expected.
5. Framework applies to stationary (Fourier-decomposable) and non-stationary (windowed Fourier) backgrounds.
6. Direct phenomenological applications: astrophysical plasmas, dark photon backgrounds, axion–gauge reheating.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Vacuum persistence | $\mathcal{P} = e^{-2\,\text{Im}\,\Gamma} = \exp[-2\int d^4x\,w(x)]$ | Eq. 2.9 |
| Decay probability | $\mathcal{P}_{\text{decay}} \simeq 2\,\text{Im}\,\Gamma$ | Eq. 2.10 |
| Pair density (weak field) | $n_{\text{pairs}} \simeq V^{-1}\mathcal{P}_{\text{decay}}$, $n_{\text{particles}} \simeq 2n_{\text{pairs}}$ | Eq. 2.11 |
| Scalar effective action | $\Gamma^b_{\text{1-loop}}[A_\mu] = i\ln\det[(D_\mu D^\mu - m^2)/(\Box - m^2)]$ | Eq. 2.13 |
| Fermion effective action | $\Gamma^f_{\text{1-loop}}[A_\mu] = -i\ln\det[(iD\!\!\!/-m)/(i\partial\!\!\!/-m)]$ | Eq. 2.14 |
| Euler–Heisenberg (bosonic) | $2\,\text{Im}\,\mathcal{L}_b = (g^2 Q^2 E^2/8\pi^3)\sum_n (-1)^{n+1}/n^2\,\exp[-n\pi m^2/(gQE)]$ | Eq. 2.16 |
| Euler–Heisenberg (fermionic) | $2\,\text{Im}\,\mathcal{L}_f = (g^2 Q^2 E^2/4\pi^3)\sum_n (1/n^2)\exp[-n\pi m^2/(gQE)]$ | Eq. 2.17 |
| Stochastic mean | $\langle\hat{A}_\mu(x)\rangle_s = 0$, $\langle\hat{A}_\mu(x)\hat{A}_\nu(y)\rangle_s = G_{\mu\nu}(x-y)$ | Eq. 3.1 |
| Stochastic amplitudes | $\langle\alpha_{q,\sigma}\alpha^*_{q',\sigma'}\rangle_s = \delta_{\sigma\sigma'}\delta^3(q-q')$ | Eq. 3.5 |
| Combined average | $\langle\ldots\rangle = \int\mathcal{D}A\,P[A]\langle 0_{\text{in}}\|\ldots\|0_{\text{in}}\rangle_A$ | Eq. 3.6 |
| Effective action (stochastic) | $\text{Im}\,\Gamma^b_{\text{1-loop}} = -\text{Tr}\ln[\hat{I} - \hat{O}(A)\hat{\delta}^+\hat{O}(A)\hat{\delta}^-]$ | Eq. 3.11 |
| Scalar decay (perturbative) | $\mathcal{P}^b_{\text{decay}} = -g^2 Q^2\,\text{Tr}[(2\hat{A}_\mu\partial^\mu+\partial_\mu\hat{A}^\mu)\hat{\delta}^+(2\hat{A}_\nu\partial^\nu+\partial_\nu\hat{A}^\nu)\hat{\delta}^-]$ | Eq. 3.12 |
| Stationary scalar prob | $\mathcal{P}^b_{\text{decay}} = (g^2 Q^2\pi/3)\int_q \Theta(-q^2-4m^2)(1+4m^2/q^2)^{3/2}\langle-\hat{F}_{\mu\nu}(q)\hat{F}^{\mu\nu}(-q)\rangle$ | Eq. 3.16 |
| Spectral scalar density | $\langle n^b(\omega)\rangle = (g^2 Q^2\pi/(3V))\int d^3q\,\Theta(\omega^2-\|\mathbf{q}\|^2-4m^2)(1-4m^2/(\omega^2-\|\mathbf{q}\|^2))^{3/2}\langle-F_{\mu\nu}F^{\mu\nu}\rangle$ | Eq. 3.17 |

## Relevance to Phonon-Exflation

Stochastic Schwinger framework is directly applicable to computing pair-production rates in the stochastic gauge-field environments of the phonon-exflation substrate. The S38 Schwinger-instanton duality in the project ($S_{\text{Schwinger}} = S_{\text{inst}} = 0.069$) assumes a coherent driving field; this paper's framework provides the extension to stochastic/fluctuating drivers, relevant for computing GGE relic formation under realistic non-uniform Jensen deformation gradients. Kinematic threshold $\omega^2 > |\mathbf{q}|^2 + 4m^2$ maps to the van Hove fold dispersion constraints. Feynman Test Step 6 (unitarity) preserved by optical-theorem relation.
