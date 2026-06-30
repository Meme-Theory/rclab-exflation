# Non-Gaussian features of primordial fluctuations in single field inflationary models

**Author(s):** Juan Maldacena
**Year:** 2003 (revised 2005)
**Journal:** JHEP 0305:013 (2003)
**arXiv:** astro-ph/0210603
**Relevance:** CRITICAL -- first rigorous computation of the three-point correlation function (bispectrum) for primordial fluctuations in single-field inflation; establishes the Maldacena consistency relation $f_{\rm NL} \sim \mathcal{O}(\epsilon, \eta)$ that is the benchmark for all non-Gaussianity measurements; provides the cleanest derivation of the second-order action for $\zeta$

---

## Abstract

We compute the three point correlation functions for primordial scalar and tensor fluctuations in single field inflationary models. We obtain explicit expressions in the slow roll limit where the answer is given terms of the two usual slow roll parameters. In a particular limit the three point functions are determined completely by the tilt of the spectrum of the two point functions. We also make some remarks on the relation of this computation to dS/CFT and AdS/CFT. We emphasize that (A)dS/CFT can be viewed as a statement about the wavefunction of the universe.

---

## Key Arguments and Derivations

### Section 2: Review of the Quadratic Computation (pp. 4-11)

Starting from $S = \frac{1}{2}\int\sqrt{g}[R - (\nabla\phi)^2 - 2V(\phi)]$ with $M_{pl}^{-2} \equiv 8\pi G_N = 1$, Maldacena uses the ADM formalism ($ds^2 = -N^2 dt^2 + h_{ij}(dx^i + N^i dt)(dx^j + N^j dt)$) and works in the gauge $\delta\phi = 0$, $h_{ij} = e^{2\rho}[(1+2\zeta)\delta_{ij} + \gamma_{ij}]$ where $\zeta$ parameterizes scalar and $\gamma_{ij}$ tensor fluctuations. The lapse $N$ and shift $N^i$ are solved as constraint equations. The second-order action is $S_{(2)} = \frac{1}{2}\int dt\,d^3x\,\frac{\dot\phi^2}{\dot\rho^2}[e^{3\rho}\dot\zeta^2 - e^\rho(\partial\zeta)^2]$. This is suppressed by a slow-roll parameter because $\zeta$ would be pure gauge in exact de Sitter. The two-point function at late times is $\langle\zeta_{\vec{k}}\zeta_{\vec{k}'}\rangle \sim (2\pi)^3\delta^3(\vec{k}+\vec{k}')\frac{1}{2k^3}\frac{\dot\rho_*^2}{M_{pl}^2}\frac{\dot\rho_*^2}{\dot\phi_*^2}$.

### Section 3: Third-Order Action (pp. 11-18)

The action is expanded to third order in $\zeta$ and $\gamma$, yielding explicit cubic interaction terms. These are computed using the ADM constraint solutions to second order. The cubic action contains terms proportional to $\epsilon\dot\zeta^3$, $\epsilon\zeta(\partial\zeta)^2$, $\epsilon^2\zeta\dot\zeta^2$, and mixed scalar-tensor terms.

### Section 4: Three-Point Functions (pp. 18-30)

Using the in-in formalism, the three-point functions are computed. The key results in the slow-roll limit are schematically $\langle\zeta^3\rangle \sim \frac{H^4}{M_{pl}^4}\frac{1}{\epsilon}\mathcal{M}_1$, $\langle\zeta\zeta\gamma\rangle \sim \frac{H^4}{M_{pl}^4}\frac{1}{\epsilon}\mathcal{M}_2$, $\langle\zeta\gamma\gamma\rangle \sim \frac{H^4}{M_{pl}^4}\mathcal{M}_3$, $\langle\gamma\gamma\gamma\rangle \sim \frac{H^4}{M_{pl}^4}\mathcal{M}_4$, where $\mathcal{M}_i$ are homogeneous functions of momenta of degree $k^{-6}$.

The crucial **squeezed limit** result ($k_1 \ll k_2, k_3$): the bispectrum is proportional to the tilt of the power spectrum, $\langle\zeta_{k_1}\zeta_{k_2}\zeta_{k_3}\rangle \sim -n_s\langle\zeta_{k_2}\zeta_{k_3}\rangle\langle\zeta_{k_1}\zeta_{-k_1}\rangle$. This is the **Maldacena consistency relation**: the non-Gaussianity of single-field slow-roll inflation is completely determined by the spectral tilt and is unobservably small.

### Section 5: Relation to dS/CFT and AdS/CFT (pp. 30-39)

The computation is connected to holographic dualities. The wavefunction of the universe in de Sitter space has the structure of a generating functional of a conformal field theory. The three-point functions of $\zeta$ and $\gamma$ map to stress-tensor correlators in the dual CFT.

---

## Key Results

1. The Maldacena consistency relation: in the squeezed limit, $f_{\rm NL}^{\rm local} = \frac{5}{12}(1 - n_s)$ for single-field slow-roll inflation.
2. Non-Gaussianity from single-field slow-roll is of order $f_{\rm NL} \sim \mathcal{O}(\epsilon, \eta) \sim 10^{-2}$, undetectable by CMB experiments.
3. The second-order action for $\zeta$ is $S_{(2)} = \frac{1}{2}\int dt\,d^3x\,\frac{\dot\phi^2}{\dot\rho^2}[e^{3\rho}\dot\zeta^2 - e^\rho(\partial\zeta)^2]$, suppressed by slow-roll.
4. $\zeta$ is pure gauge in exact de Sitter; its dynamics arise only from the breaking of exact de Sitter symmetry.
5. All four three-point functions ($\zeta\zeta\zeta$, $\zeta\zeta\gamma$, $\zeta\gamma\gamma$, $\gamma\gamma\gamma$) are computed with exact momentum dependence.
6. The dS/CFT correspondence can be understood as a statement about the wavefunction of the universe.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Starting action | $S = \frac{1}{2}\int\sqrt{g}[R - (\nabla\phi)^2 - 2V(\phi)]$ | Eq. (2.1) |
| ADM metric | $ds^2 = -N^2 dt^2 + h_{ij}(dx^i + N^i dt)(dx^j + N^j dt)$ | Eq. (2.5) |
| Gauge choice | $\delta\phi = 0,\; h_{ij} = e^{2\rho}[(1+2\zeta)\delta_{ij} + \gamma_{ij}]$ | Eq. (2.8) |
| Constraint solutions | $N_1 = \dot\zeta/\dot\rho,\; N_T^i = 0$ | Eq. (2.10) |
| Second-order action | $S_{(2)} = \frac{1}{2}\int dt\,d^3x\,\frac{\dot\phi^2}{\dot\rho^2}[e^{3\rho}\dot\zeta^2 - e^\rho(\partial\zeta)^2]$ | Eq. (2.12) |
| Scalar two-point | $\langle\zeta_{\vec{k}}\zeta_{\vec{k}'}\rangle = (2\pi)^3\delta^3(\vec{k}+\vec{k}')\frac{1}{2k^3}\frac{\dot\rho_*^4}{\dot\phi_*^2 M_{pl}^2}$ | Eq. (2.20) |
| Spectral tilt | $n_s = 2(\eta - 3\epsilon)$ | Eq. (2.22) |
| Schematic three-point | $\langle\zeta^3\rangle = \frac{H^4}{M_{pl}^4\epsilon}\delta^3(\sum\vec{k}_i)\mathcal{M}_1$ | Eq. (1.1) |
| Squeezed limit | $\langle\zeta_{k_1}\zeta_{k_2}\zeta_{k_3}\rangle \sim -n_s\langle\zeta_{k_2}\zeta_{k_3}\rangle\langle\zeta_{k_1}\zeta_{-k_1}\rangle$ for $k_1 \ll k_2, k_3$ | Eq. (1.2) |

---

## Relevance to Phonon-Exflation

Maldacena's computation is directly relevant to the exflation framework in two ways. (1) The consistency relation $f_{\rm NL} = \frac{5}{12}(1-n_s)$ is a falsifiable prediction of single-field slow-roll models. The exflation transit is driven by a spectral action gradient ($dS/d\tau$), not a slowly rolling scalar field, and the non-linear dynamics of the van Hove fold transit at Mach 13.75 should produce a different bispectrum shape -- potentially detectable as a signature distinguishing exflation from standard inflation. (2) Maldacena's proof that $\zeta$ is pure gauge in exact de Sitter, gaining dynamics only from slow-roll breaking, has an analog in the spectral action framework: the curvature perturbation $\mathcal{R}$ would be sourced by the spectral reorganization at the fold, not by a slowly varying Hubble parameter. The GGE (generalized Gibbs ensemble) relic formation process during the transit produces excitations that are fundamentally non-thermal, which could leave non-Gaussian signatures distinct from any single-field prediction.
