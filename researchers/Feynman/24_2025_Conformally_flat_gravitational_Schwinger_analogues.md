# Conformally-flat gravitational analogues to the Schwinger effect

**Author(s):** S. A. Franchino-Viñas, F. D. Mazzitelli, S. Pla
**Year:** 2026 (submitted Feb 2026)
**Journal:** arXiv preprint (hep-th)
**arXiv/DOI:** arXiv:2602.18578v1
**Relevance:** MEDIUM

---

## Abstract

We study particle creation for scalar fields in conformally flat spacetimes using resummed heat-kernel techniques. We make use of an analogy between quantum scalar fields in conformally flat spacetimes and scalar field theories with a Yukawa coupling in Minkowski space. The correspondence holds exactly at the level of the effective action and includes nonconformal curvature couplings. This framework provides access to particle creation at strong curvature. In a radiation dominated universe, the particle production rates in arbitrary dimensions are independently confirmed through explicit calculations of the Bogoliubov coefficients. We also find new exact gravitational analogues of the Schwinger effect in quantum field theory in curved spacetime.

---

## Key Arguments and Derivations

**I. Introduction.** Strong-field pair creation is an archetype of quantum vacuum instability, with applications to cosmology and black hole evaporation. Previous heat-kernel resummations of the effective action for Yukawa/electromagnetic backgrounds (Refs. [3,4]) are here shown to extend to gravitational scenarios. The effective action $\Gamma$ controls the vacuum persistence probability via $|\langle\text{out}|\text{in}\rangle|^2 = e^{-P}$ with $P = 2\,\text{Im}\,\Gamma$.

**II. Quantum scalar field in conformally flat metrics.** Starting from a $d$-dimensional scalar with nonminimal coupling $\xi R$ and mass $m$ in a conformally flat metric $ds^2 = \Omega^2(\tau,\mathbf{x})(d\tau^2 - d\mathbf{x}^2)$, a Weyl rescaling $\varphi := \Omega^{(d-2)/2}\phi$ maps the problem to a scalar in Minkowski with Yukawa-type potential $V(\tau,\mathbf{x}) = m^2\Omega^2 + (\xi-\xi_d)R\Omega^2$, where $\xi_d = (d-2)/[4(d-1)]$ is the conformal value.

**II.A. Resummed heat-kernel.** The diagonal of the heat kernel for operator $Q = \partial^2 + \Omega^2[m^2 + (\xi-\xi_d)R]$ admits a closed resummed form involving $\gamma^2_{\alpha\beta} := 2V_{,\alpha\beta}$, resumming all invariants of $V$, $V_{,\alpha}$, $V_{,\alpha\beta}$. For radiation-dominated cosmology ($m^2 a^2 = b_0^2\tau^2$) with $\xi=\xi_d$, the heat kernel takes an explicit form and the effective action integral develops poles at $s = \pi n/b_0$ whose imaginary contributions yield the pair creation probability.

**II.B. Bogoliubov coefficients.** The modes obey $\varphi_k'' + \omega_k^2\varphi_k = 0$ with $\omega_k^2 = k^2 + m^2 a^2 + (\xi-\xi_d)Ra^2$, solved by parabolic cylinder functions $D_\nu(z)$. In/out vacua at $\tau\to\pm\infty$ give Bogoliubov coefficients $\alpha_k, \beta_k$ with $|\alpha_k|^2 = 1 + e^{-4\pi\kappa}$ ($\kappa = k^2/(4b_0)$). Result matches heat-kernel computation in all dimensions $d$, confirming the resummation.

**III. Other gravitational analogues.** For massless fields with nonconformal coupling the condition $Ra^2 \propto \tau^2 + c$ generates Schwinger-like scale factors. Case I ($c=0$, $d=4$) gives bouncing universes with scale factors built from $D_{-1/2}$ parabolic cylinder functions. Case II (Gaussian scale factor $a(\tau)=a_0\exp(-\alpha\tau^2/2)$) yields an effective mass $\tilde{m}^2 = 2(d-1)(\xi-\xi_d)|\alpha|$ and Schwinger-like exponential suppression in pair production.

**IV. Discussion.** The method extends to static universes only via classical instabilities (space-dependent gauge, tachyonic instabilities). Future directions: Euler–Heisenberg-like spinor heat kernel for axial anomaly; large-curvature expansion connecting to Hawking radiation.

## Key Results

1. Exact equivalence, at effective-action level, between scalar QFT in conformally flat spacetime and scalar QED/Yukawa with time-dependent mass (Eqs. 4, 6).
2. Closed-form pair creation probability in radiation-dominated universe in arbitrary $d$: $P/2 = -V_0/[2(2\pi)^{d-1}] \, b_0^{(d-1)/2}\,(1-2^{(1-d)/2})\,\zeta_R((d+1)/2)$ (Eq. 15).
3. Heat-kernel result matches Bogoliubov coefficient calculation for radiation-dominated universe.
4. New Schwinger-like gravitational analogues with Gaussian scale factor, featuring mass-like exponential suppression $e^{-\tilde{m}^2 n\pi/\tilde{a}}$ (Eq. 37).
5. Pair creation probability in radiation-dominated cosmology does NOT exhibit exponential mass suppression (contrast with SQED).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Vacuum persistence | $\|\langle\text{out}\|\text{in}\rangle\|^2 = e^{-P}$, $P = 2\text{Im}\,\Gamma$ | Eq. 1 |
| Weyl action | $S[\varphi] = \frac{1}{2}\int d\tau\,d^{d-1}x\,[(\partial\varphi)^2 - \Omega^2(m^2+(\xi-\xi_d)R)\varphi^2]$ | Eq. 4 |
| Yukawa potential | $V(\tau,\mathbf{x}) = m^2\Omega^2 + (\xi-\xi_d)R\Omega^2$ | Eq. 6 |
| Fluctuation operator | $Q = \partial^2 + \Omega^2[m^2 + (\xi-\xi_d)R]$ | Eq. 8 |
| Resummed heat kernel | $K(x,x;s) = \frac{1}{(4\pi s)^{d/2}}\frac{e^{-sV + \partial V[\gamma^{-3}(\gamma s - 2\tanh(\gamma s/2))]\partial V}}{\det^{1/2}((\gamma s)^{-1}\sinh(\gamma s))}\,W(x,x;s)$ | Eq. 10 |
| Rad-dom heat kernel | $K(x,x;s) = \frac{1}{(4\pi s)^{d/2}}\sqrt{\frac{b_0 s}{\cos(b_0 s)\sin(b_0 s)}}\,e^{-b_0\tau^2\tan(b_0 s)}$ | Eq. 12 |
| Pair prob (series) | $P/2 = \frac{V_0}{2(2\pi)^{d-1}}\,b_0^{(d-1)/2}\sum_{n=1}^\infty (-1)^{n+1}/n^{(d+1)/2}$ | Eq. 14 |
| Closed form | $P/2 = -\frac{V_0}{2(2\pi)^{d-1}}b_0^{(d-1)/2}(1-2^{(1-d)/2})\zeta_R((d+1)/2)$ | Eq. 15 |
| Modes equation | $\varphi_k'' + \omega_k^2\varphi_k = 0$, $\omega_k^2 = k^2 + m^2 a^2 + (\xi-\xi_d)Ra^2$ | Eq. 17 |
| Bogoliubov $\|\alpha_k\|^2$ | $\|\alpha_k\|^2 = 1 + e^{-4\pi\kappa}$, $\kappa = k^2/(4b_0)$ | (derived Eq. 26) |
| Schwinger (SQED comparison) | $P_{\text{SQED}}/V_0 = 2\pi T_0 (eE/4\pi^2)^{d/2}\sum_n (-1)^{n+1}n^{-d/2}e^{-n\pi m^2/(eE)}$ | Eq. 28 |
| Gaussian-scale-factor Ricci | $Ra^2(\tau) = 2(d-1)\alpha[(d-2)\alpha\tau^2/2 - 1]$ | (derived Eq. 32) |
| Case II pair prob | $P/2 = \frac{V_0}{2(2\pi)^{d-1}}\tilde{a}^{(d-1)/2}\sum_n(-1)^{n+1}n^{-(d+1)/2}e^{-\tilde{m}^2 n\pi/\tilde{a}}$ | Eq. 37 |

## Relevance to Phonon-Exflation

Connects to S38 Schwinger-instanton duality ($S_{\text{Schwinger}} = S_{\text{inst}} = 0.069$ in project results). The paper's gravitational-analogue framework is directly relevant to the transit-cosmogenesis picture where Parker-type pair creation at the van Hove fold generates the GGE relic (59.8 quasiparticle pairs). The Bogoliubov/heat-kernel equivalence provides a second computational route for verifying pair-creation rates in the exflation substrate description. The absence of mass-exponential suppression in radiation-dominated cosmology (vs SQED) maps onto the phononic substrate's weak dispersion in the post-transit regime.
