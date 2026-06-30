# Self-consistent graviton spectral function in Lorentzian quantum gravity

**Author(s):** Jan M. Pawlowski, Manuel Reichert, Jonas Wessely
**Year:** 2025 (Jul 2025)
**Journal:** arXiv preprint (hep-th)
**arXiv/DOI:** arXiv:2507.22169v1
**Relevance:** MEDIUM (graviton unitarity in asymptotically safe QG)

---

## Abstract

We present the first fully self-consistent computation of the graviton spectral function in quantum gravity, using the spectral renormalisation group for gravity put forward in [1] within a physical mass-shell renormalisation scheme. Here, self-consistency refers to the fact that the full non-perturbative spectral function is used in the diagrams, including the scattering continuum. We find a positive graviton spectral function with a massless one-graviton peak and a multi-graviton continuum with a close-to-quadratic spectral decay in the ultraviolet. Within the physical on-shell renormalisation scheme, the graviton satisfies the sum rule of an asymptotic state and features a unit total spectral weight. We briefly discuss the implications of the physical formulation for the computation of scattering processes and investigations of unitarity in asymptotically safe quantum gravity.

---

## Key Arguments and Derivations

**Section I: Introduction.** Asymptotic safety program needs unitarity/causality tests. Extension of Euclidean fRG to Lorentzian via spectral renormalisation group (SRG) with on-shell renormalisation. First self-consistent computation feeding full spectral function (including scattering continuum) into the flow.

**Section II: Renormalised spectral flows.**

**Field content.** Metric split $g_{\mu\nu} = \eta_{\mu\nu} + \sqrt{32\pi G_N}\sqrt{Z_h}h_{\mu\nu}$ (Eq. 1). Fields $\Phi = (h_{\mu\nu}, c_\mu, \bar{c}_\mu)$ (Eq. 2).

**Callan-Symanzik flow (Eq. 3):** $\partial_t\Gamma[\Phi] = (1/2)\text{Tr}[\mathcal{G}[\Phi]\partial_t R_{CS}] - \partial_t S_{ct}$, with momentum-independent regulators $R_{hh} = Z_h k^2$, $R_{\bar{c}c} = Z_c k^2$ (Eq. 5).

Momentum independence preserves analytic properties in the complex plane (linked to unitarity/causality) at the price of flowing counterterm $\partial_t S_{ct}$.

**RG-invariant vertex expansion (Eq. 6):**
$\bar\Gamma^{(\Phi_{i_1}\cdots\Phi_{i_n})} = \Gamma^{(\Phi_{i_1}\cdots\Phi_{i_n})}/(Z^{1/2}_{\Phi_{i_1}}\cdots Z^{1/2}_{\Phi_{i_n}})$, $\bar\Phi_i = Z^{1/2}_{\Phi_i}\Phi_i$.

**Approximation (Eq. 7):** full cutoff-dependent graviton 2-point function + Einstein-Hilbert vertices with running $G_{N,k}$ and $\Lambda_k$. Harmonic gauge $\alpha = \beta = 1$ (Eq. 9) singled out by spectral considerations; physical $\Lambda_{k=0} = 0$ (extended to $\Lambda_k = 0$ for computational convenience).

**Section II.B: Spectral flows.** Graviton propagator TT component
$\mathcal{G}^{\mu\nu\rho\sigma}_{hh}(p) = G_{hh}(p)\Pi^{\mu\nu\rho\sigma}_{TT}(p) + \ldots$ (Eq. 11).

**Källén-Lehmann representation (Eq. 12):** $G_{hh}(p^2) = \int_\lambda \rho_h(\lambda)/(\lambda^2 + p^2)$, $\int_\lambda \equiv \int_0^\infty d\lambda\,\lambda/\pi$.

Spectral function (Eq. 13): $\rho_h(\omega) = 2\,\text{Im}\,G_{hh}(p^2 \to -(\omega+)^2)$.

**Parametrisation (Eq. 14):** $\rho_h(\lambda) = (1/Z_h)[2\pi\delta(\lambda^2 - m_h^2) + \theta(\lambda^2 - 4m_h^2)f_h(\lambda)]$ — massless one-graviton peak plus multi-graviton continuum.

**Spectral sum rule (Eq. 15):** $\int_\lambda \rho(\lambda) = 1$ related to probability conservation and canonical commutation relations.

**Section II.C: On-shell renormalisation.** Running pole mass identified with RG scale: $m_h^2 = k^2$, $Z_h = 1$ (Eq. 16) implemented as $\Gamma^{(2)}(p^2 = -k^2) = 0$, $\partial_{p^2}\Gamma^{(2)}(p^2 = -k^2) = 1$ (Eq. 17). Flowing renormalisation conditions Eq. 20; anomalous dimension $\eta_h(p^2 = -k^2) = 0$ (Eq. 21).

**Section II.D: Computational setup.** Flow equation (Eq. 22) with three contributions: tadpole, 3-point graviton, and ghost loop. Newton-coupling beta function in harmonic gauge (Eq. 23):
$\partial_t g = 2g - (2499/380\pi)g^2$,
UV fixed point $g^* = 760\pi/2499 \approx 0.955$ (Eq. 24). Trajectory $g(k) = g^* k^2/(k^2 + g^* M_{pl}^2)$ (Eq. 25).

**Imaginary part of flow (Eq. 26):** $\text{Im}\,\Gamma^{(hh)}_{TT}(k,\omega) = \int_k^{\omega/2}(dk'/k')\int_{\lambda_1,\lambda_2}\rho^{(2)}_h(k',\lambda_1)\rho_h(k',\lambda_2)\text{Im}\,D(k',\omega,\lambda_1,\lambda_2)$ — flow from $k$ to $\omega/2$ (imaginary part proportional to $\theta(\omega - 2k)$).

Squared propagator spectral representation (Eq. 27) reduces spectral integral dimensionality.

Tail reconstruction via Kramers-Kronig relations (Eq. 28): $f_h(k,\omega) = -2\text{Im}\,\Gamma^{(hh)}_{TT}/[(\text{Im})^2 + (\text{Re})^2]$.

**Section III: Results.**

**UV tail decay (Eq. 29):** $f_h(\lambda \to \infty) = c^{UV}_h/[\lambda^2\log^3(\lambda^2)]$ — leads to finite spectral weight.

**Sum rule (Eq. 30):** $z_{spec} = 1 + \int_\lambda \lambda f_h(\lambda) \approx 1.486$.

**Physical spectral function (Eq. 31):** $\rho^{(ph)}_h = \rho_h/z_{spec}$, $h^{(ph)}_{\mu\nu} = h_{\mu\nu}/z^{1/2}_{spec}$. Satisfies sum rule $\int_\lambda \rho^{(ph)}_h(\lambda) = 1$ (Eq. 32).

**IR limit (Eq. 33):** $G^{(ph)}_{hh} = (1/z_{spec})(1/p^2 - A_h\log p^2 + \text{sub-leading})$, with gauge-dependent coefficient $A_h = 61/(60\pi) \approx 0.32$. Constant onset of scattering tail at $\rho_h = z_{spec}\rho^{(ph)}$ with $61/30 \approx 2.033$ prefactor.

## Key Results

1. First fully self-consistent Lorentzian graviton spectral function in quantum gravity, feeding full spectral function (including scattering tail) into diagrams.
2. Positive spectral function with massless one-graviton peak + multi-graviton continuum.
3. UV decay $f_h(\lambda) \sim 1/[\lambda^2\log^3\lambda^2]$ (Eq. 29) — integrable, finite spectral weight.
4. On-shell renormalisation enforces unit total spectral weight (Eq. 32); fluctuation graviton exhibits asymptotic-state properties.
5. Newton coupling UV fixed point $g^* \approx 0.955$ in harmonic gauge.
6. IR limit reproduces analytic coefficient $A_h = 61/(60\pi)$ (gauge-dependent but scheme-independent).
7. On-shell RG scheme implements momentum-dependent rescaling giving close-to-physical building blocks for asymptotically safe gravity.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Metric split | $g_{\mu\nu} = \eta_{\mu\nu} + \sqrt{32\pi G_N}\sqrt{Z_h}h_{\mu\nu}$ | Eq. 1 |
| Fields | $\Phi = (h_{\mu\nu}, c_\mu, \bar{c}_\mu)$ | Eq. 2 |
| CS flow | $\partial_t\Gamma[\Phi] = (1/2)\text{Tr}[\mathcal{G}[\Phi]\partial_t R_{CS}] - \partial_t S_{ct}$ | Eq. 3 |
| CS regulators | $R_{hh} = Z_h k^2$, $R_{\bar{c}c} = Z_c k^2$ | Eq. 5 |
| **KL representation** | $G_{hh}(p^2) = \int_\lambda \rho_h(\lambda)/(\lambda^2 + p^2)$ | **Eq. 12** |
| Spectral function | $\rho_h(\omega) = 2\,\text{Im}\,G_{hh}(p^2 \to -(\omega^+)^2)$ | Eq. 13 |
| Parametrisation | $\rho_h(\lambda) = (1/Z_h)[2\pi\delta(\lambda^2 - m_h^2) + \theta(\lambda^2 - 4m_h^2)f_h(\lambda)]$ | Eq. 14 |
| **Sum rule** | $\int_\lambda \rho(\lambda) = 1$ | **Eq. 15** |
| On-shell conditions | $m_h^2 = k^2$, $Z_h = 1$ | Eq. 16 |
| Renormalisation conds | $\Gamma^{(2)}(p^2 = -k^2) = 0$, $\partial_{p^2}\Gamma^{(2)}(p^2 = -k^2) = 1$ | Eq. 17 |
| Flowing conds | $\partial_t\Gamma^{(2)}_{TT}(p^2 = -k^2) = 2k^2$, $\partial_{p^2}\partial_t\Gamma^{(2)}_{TT}(p^2 = -k^2) = 0$ | Eq. 20 |
| Newton beta function | $\partial_t g = 2g - (2499/380\pi)g^2$, $g = G_{N,k}k^2$ | Eq. 23 |
| UV fixed point | $g^* = 760\pi/2499 \approx 0.955$ | Eq. 24 |
| Trajectory | $g(k) = g^* k^2/(k^2 + g^* M_{pl}^2)$ | Eq. 25 |
| Flow integrand | $\text{Im}\,\Gamma^{(hh)}_{TT}(k,\omega) = \int_k^{\omega/2}(dk'/k')\int_{\lambda_1\lambda_2}\rho^{(2)}_h\rho_h\text{Im}\,D$ | Eq. 26 |
| Squared propagator | $G^2_{hh}(q) = \int_\lambda \rho^{(2)}_h(\lambda)/(q^2 + \lambda^2)^2$ | Eq. 27a |
| Tail reconstruction | $f_h(k,\omega) = -2\text{Im}\,\Gamma/[(\text{Im})^2 + (\text{Re})^2]$ | Eq. 28 |
| **UV decay** | $f_h(\lambda \to \infty) = c^{UV}_h/[\lambda^2\log^3(\lambda^2)]$ | **Eq. 29** |
| Total spectral weight | $z_{spec} = 1 + \int_\lambda \lambda f_h(\lambda) \approx 1.486$ | Eq. 30 |
| Physical norm | $\rho^{(ph)}_h = \rho_h/z_{spec}$, $h^{(ph)}_{\mu\nu} = h_{\mu\nu}/z^{1/2}_{spec}$ | Eq. 31 |
| Unit sum rule | $\int_\lambda \rho^{(ph)}_h(\lambda) = 1$ | Eq. 32 |
| IR limit | $G^{(ph)}_{hh} = (1/z_{spec})(1/p^2 - A_h\log p^2 + \text{sub-leading})$, $A_h = 61/(60\pi)$ | Eq. 33 |

## Relevance to Phonon-Exflation

Directly relevant to Feynman Test Step 6 (unitarity) as applied to the emergent graviton of the spectral-action construction. Provides a Lorentzian, self-consistent benchmark for graviton spectral properties in a competing UV-completion (asymptotic safety). The KL representation (Eq. 12) and sum rule (Eq. 15) are the standard unitarity tests any emergent graviton in the phonon-exflation framework must satisfy.

Key benchmark numbers: UV fixed point $g^* \approx 0.955$; total spectral weight $z_{spec} \approx 1.486$; IR coefficient $A_h = 61/(60\pi) \approx 0.32$. Any graviton extracted from the project's $a_2$ Seeley-DeWitt coefficient must reproduce these Lorentzian properties or else provide a reason (e.g., substrate-induced modifications) for the deviation.

Positive, normalisable spectral function with massless peak + UV-decaying continuum is a template for what the project must demonstrate for the emergent graviton derived from $D_K$ eigenvalues. Direct adversarial comparison to spectral-action gravity.
