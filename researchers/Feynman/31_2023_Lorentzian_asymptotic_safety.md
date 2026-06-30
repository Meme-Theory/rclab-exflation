# Asymptotic safety in Lorentzian quantum gravity

**Author(s):** Edoardo D'Angelo
**Year:** 2024 (v2, Jan 2024; v1 Oct 2023)
**Journal:** Phys. Rev. D 109, 066012 (2024)
**arXiv/DOI:** arXiv:2310.20603v2
**Relevance:** MEDIUM (adversarial UV completion vs spectral action)

---

## Abstract

A recently introduced functional Renormalization Group (RG) provides a new tool to explore non-perturbative and covariant RG flows in Lorentzian spacetimes. We apply it for the first time to investigate the ultraviolet limit of quantum gravity. While the RG flow is state-dependent, it is possible to evaluate state and background independent contributions to the flow. Taking into account only these universal terms, the RG flow exhibits a non-trivial fixed point in the Einstein-Hilbert truncation, providing a mechanism for Asymptotic Safety in Lorentzian quantum gravity.

---

## Key Arguments and Derivations

**Setup: QG as locally covariant QFT.** Gravity quantized on fixed but arbitrary globally hyperbolic $(\mathcal{M}, \bar{g})$. Off-shell configurations $\hat{h} \in \Gamma(T^*(\mathcal{M})^{\otimes 2})$ extended by ghosts $\hat{c}, \bar{\hat{c}}$ and Nakanishi-Lautrup $\hat{b}$. Batalin-Vilkovisky (BV) formalism with antifields $\varphi^\ddagger = \delta/\delta\varphi$; classical action $I = I_{EH} + I_{af} + \gamma\Psi$ (Eq. 1) with $I_{EH} = 2\zeta^2\int_\mathcal{M}\sqrt{-\det\hat{g}}(R(\hat{g}) - 2\Lambda)$ and $\zeta^2 = (32\pi G)^{-1}$.

De-Donder gauge fermion $\Psi$; BRST differential $\gamma = \{\cdot, I_{af}\}$; master equation $\{I, I\} = sI = 0$.

**Regulator terms (Eq. 2):** local in position, preserving causality and Lorentz invariance, $Q_k = -(1/2)\int_\mathcal{M}\sqrt{-\det\bar{g}}[T(\hat{h}_{ab}q_k^{abcd}\hat{h}_{cd}) + 2T\bar{\hat{c}}_a\tilde{q}_k^{ab}\hat{c}_b]$.

**Extended BV symmetry:** $s_k I_{ext} = 0$ (Eq. 4) where $s_k = s + \int q_{kA}\delta/\delta\eta_A$.

**Regularized generating functional:** $Z_k(\bar{g}; j, \sigma, \eta) = \langle T\exp\{\Sigma + J + Q_k + H\}\rangle$ (Eq. 5) generalizing path-integral to globally hyperbolic spacetimes. Effective Average Action (EAA) $\Gamma_k = \tilde\Gamma_k - Q_k(\phi)$, satisfying extended Slavnov-Taylor identity (Eq. 6).

**Wetterich-type FRGE (Eq. 7):** $\partial_k\Gamma_k(\bar{g};\phi) = (i/2)\int_\mathcal{M}\text{Tr}\{\partial_k q_k(x):G_k:(x,x)\}$, written in terms of interacting Feynman propagator $(\Gamma_k + Q_k)^{(2)}G_k = -\delta\mathbb{I}$ (Eq. 8).

**UV finiteness via normal-ordering.** Point-splitting subtracts Hadamard parametrix counterterm $H_k$; ultra-violet and infrared finiteness by definition. Regulator acts as Callan-Symanzik-type cutoff.

**State dependence.** Lorentzian FRGE admits infinite family of propagator solutions; choice fixed by selecting Hadamard state for free theory. Feynman propagator has universal UV singular structure $h_k$ (Hadamard parametrix); smooth contribution $w_k = \Delta_{F,k} - h_k$ fixes quasi-free Hadamard state. Interacting propagator: $:G_k: = \sum_{n=0}^\infty (i\Delta_{F,k}U_k^{(2)})^n w_k$ (Eq. 9).

**Hadamard subtraction and local potential approximation.** In LPA, interacting propagator coincides with free one with effective mass from $U_k$. Hadamard parametrix (Eq. 10):
$G_k = i/(8\pi^2\zeta_k^2)(H_k + W)$ with
$H_k(x,y) = i/(8\pi^2\zeta_k^2)\lim_{\epsilon\to 0^+}[\Delta^{1/2}/\sigma_\epsilon(x,y)\mathbb{I} + V\log(\sigma_\epsilon(x,y)/\mu)]$.

Taylor expansion $V = \sum_n V_n\sigma^n$, $W = \sum_n W_n\sigma^n$. Zeroth term from $V_0 = -(1/2)\delta^2(\Gamma_k + Q_k)/\delta\phi\delta\phi\cdot\Delta^{1/2}\mathbb{I}$ (Eq. 11). FRGE becomes (Eq. 12):
$\partial_k\Gamma_k = -[1/(16\pi^2\zeta_k^2)]\int_\mathcal{M}\text{Tr}\partial_k q_k[S_0 + V_0\log(M^2/\mu^2)]$.

**Einstein-Hilbert truncation.** Ansatz Eq. 13 with running $G_{N,k}$ and $\Lambda_k$, harmonic gauge $\alpha = \beta = 1$, physical $\Lambda_{k=0} = 0$. Graviton propagator decomposed into tensor ($G_k^T$), scalar ($G_k^S$) and ghost ($\tilde{G}_k$) parts (Eqs. 15–17). Hadamard coefficients $V_0^T, V_0^S, \tilde{V}_0$ computed (Eqs. 21–23).

**Universal terms.** State-dependent $S_0$ vanishes in flat-space limit and can be absorbed by renormalization ambiguities; neglected. Running Hadamard mass $\mu = k^2$ chosen. Mass functions $M^2_S = V_0^S$, $M^2_T = V_0^T{}_{ab}^{cd}\mathbb{I}^{ab}_{cd}$, $\tilde{M}^2 = \tilde{V}_0^{ab}\bar{g}_{ab}$ (Eq. 24).

**Beta functions (Eqs. 25–27):** for dimensionless $g_k = k^{-2}G_k^{-1}(32\pi\zeta_k^2)^{-1}$ and $\lambda_k = \Lambda_k/k^2$,
$k\partial_k g_k = (\eta_N + 2)g_k$,
$k\partial_k\lambda_k = -(2-\eta_N)\lambda_k + (g_k/4\pi)(2-\eta_N)\{4\log 4 + (1-2\lambda_k)[8\log[4(1-2\lambda_k)] + \log[(1-2\lambda_k)/2]]\}$,
anomalous dimension $\eta_N(g_k, \lambda_k) = g_k/6\pi \cdot [27\log(1-2\lambda_k) + 7 + 37\log 2]/[1 + g_k/(12\pi)(37\log 2 + 27\log(1-2\lambda_k))]$.

**Non-trivial fixed point:** $g^* = 1.15$, $\lambda^* = 0.42$. Critical exponents $\theta_{1,2} = 5.11 \pm 11.59i$ (complex conjugate pair → two relevant directions). Compared to ADM-based Lorentzian $(g^{ADM}_*, \lambda^{ADM}_*) = (0.21, 0.3)$, $\theta^{ADM}_{1,2} = 0.94 \pm 3.1i$; Euclidean $(g^E_*, \lambda^E_*) = (0.34, 0.3)$, $\theta^E_{1,2} = 1.55 \pm 3.83i$.

## Key Results

1. First background-independent, non-trivial fixed point for quantum gravity in Lorentzian signature in Einstein-Hilbert truncation.
2. Novel Wetterich-type FRGE (Eq. 7) directly on globally hyperbolic spacetimes with covariant formalism and arbitrary Hadamard state.
3. Local (mass-type) regulator preserves Lorentz invariance and causality; UV finiteness via Hadamard subtraction.
4. Universal contributions (state and background independent) suffice to produce Reuter-type fixed point.
5. Complex-conjugate critical exponents ($\theta_{1,2} = 5.11 \pm 11.59i$) consistent with Euclidean results.
6. Different numerical values from ADM/Euclidean frameworks interpreted as state-dependent effects.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Classical action | $I = I_{EH} + I_{af} + \gamma\Psi$, $I_{EH} = 2\zeta^2\int\sqrt{-\det\hat{g}}(R - 2\Lambda)$ | Eq. 1 |
| Local regulator | $Q_k = -(1/2)\int\sqrt{-\bar{g}}[T(\hat{h}q_k\hat{h}) + 2T\bar{\hat{c}}\tilde{q}_k\hat{c}]$ | Eq. 2 |
| Extended BV | $s_k I_{ext} = 0$ | Eq. 4 |
| Generating functional | $Z_k(\bar{g}; j,\sigma,\eta) = \langle T\exp\{\Sigma + J + Q_k + H\}\rangle$ | Eq. 5 |
| **Lorentzian FRGE** | $\partial_k\Gamma_k = (i/2)\int\text{Tr}\{\partial_k q_k : G_k:\}$ | **Eq. 7** |
| Propagator eq | $(\delta^2/\delta\phi\delta\phi)(\Gamma_k + Q_k)G_k = -\delta\mathbb{I}$ | Eq. 8 |
| Interacting propagator | $:G_k: = \sum_n (i\Delta_{F,k}U_k^{(2)})^n w_k$ | Eq. 9 |
| Hadamard structure | $G_k = (i/8\pi^2\zeta_k^2)(H_k + W)$ | Eq. 10 |
| Coefficient $V_0$ | $V_0 = -(1/2)(\delta^2/\delta\phi\delta\phi)(\Gamma_k + Q_k)\Delta^{1/2}\mathbb{I}$ | Eq. 11 |
| FRGE after subtraction | $\partial_k\Gamma_k = -(1/16\pi^2\zeta_k^2)\int\text{Tr}\partial_k q_k[S_0 + V_0\log(M^2/\mu^2)]$ | Eq. 12 |
| Regulator kernels | $q_k{}_{ab}^{cd} = \zeta_k^2 k^2 K^{ab}_{cd}$, $\tilde{q}_{k,ab} = \zeta_k^2 k^2\bar{g}_{ab}$ | Eq. 14 |
| $V_0^S$ | $V_0^S = (1/2)(k^2 - 2\Lambda_k) - (1/12)\bar{R}$ | Eq. 21 |
| Mass functions | $M^2_S = V_0^S$, $M^2_T = V_0^T I$, $\tilde{M}^2 = \tilde{V}_0\bar{g}$ | Eq. 24 |
| Beta function $g$ | $k\partial_k g_k = (\eta_N + 2)g_k$ | Eq. 25 |
| Beta function $\lambda$ | $k\partial_k\lambda_k = -(2-\eta_N)\lambda_k + (g_k/4\pi)(2-\eta_N)\{4\log 4 + \ldots\}$ | Eq. 26 |
| Anomalous dim. | $\eta_N(g_k,\lambda_k) = (g_k/6\pi)[27\log(1-2\lambda_k) + 7 + 37\log 2]/[1 + (g_k/12\pi)(\ldots)]$ | Eq. 27 |
| Fixed point | $(g^*, \lambda^*) = (1.15, 0.42)$; $\theta_{1,2} = 5.11 \pm 11.59i$ | §Phase diagram |

## Relevance to Phonon-Exflation

Provides adversarial UV completion against the spectral-action (Connes) approach underlying the framework. Asymptotic Safety fixed point in the EH truncation claims gravity is non-perturbatively renormalizable as a metric theory — competing UV completion to the project's claim that gravity is the second spectral moment ($a_2$ Seeley-DeWitt) of $D_K$. The Lorentzian covariant FRGE (Eq. 7) is the closest QFT-based analog to the project's aspiration of a Lorentzian substrate dynamics. State-dependence of the flow parallels the Hadamard-state subtleties encountered when computing the project's effective action on the substrate. Directly relevant to Feynman Test Step 4 (power counting / renormalizability): if AS holds, metric gravity is complete without compactification; if not, compactification and KK physics (substrate) become necessary. The critical exponents $\theta_{1,2} = 5.11 \pm 11.59i$ provide concrete numbers to compare against any substrate-derived RG flow at the graviton level.
