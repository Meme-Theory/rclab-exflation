# The Effective Field Theory of Inflation

**Author(s):** Clifford Cheung, Paolo Creminelli, A. Liam Fitzpatrick, Jared Kaplan, Leonardo Senatore
**Year:** 2008
**Journal:** JHEP (IC/2007/032)
**arXiv:** 0709.0293
**Relevance:** CRITICAL

---

## Abstract

We study the effective field theory of inflation, i.e. the most general theory describing the fluctuations around a quasi de Sitter background, in the case of single field models. The scalar mode can be eaten by the metric by going to unitary gauge. In this gauge, the most general theory is built with the lowest dimension operators invariant under spatial diffeomorphisms, like $g^{00}$ and $K_{\mu\nu}$, the extrinsic curvature of constant time surfaces. This approach allows us to characterize all the possible high energy corrections to simple slow-roll inflation, whose sizes are constrained by experiments. Also, it describes in a common language all single field models, including those with a small speed of sound and Ghost Inflation, and it makes explicit the implications of having a quasi de Sitter background. The non-linear realization of time diffeomorphisms forces correlation among different observables, like a reduced speed of sound and an enhanced level of non-Gaussianity.

---

## Key Arguments and Derivations

### Section 1: Introduction

The paper's central insight is that perturbations during inflation can be described by an EFT built directly around the time-evolving vacuum, where time diffeomorphisms are non-linearly realized. The inflaton perturbation $\delta\phi$ transforms non-linearly under time diffs (eq. 1) and can be "eaten" by the metric in unitary gauge ($\phi(t,\vec{x}) = \phi_0(t)$), analogous to how a Goldstone boson is eaten by a gauge boson in a spontaneously broken gauge theory.

In unitary gauge, the most general Lagrangian is built from operators invariant under spatial diffeomorphisms only. The scalar mode re-emerges as a Goldstone boson $\pi$ via the Stuckelberg trick. The non-linear realization of time diffs forces correlations between different observables -- e.g., a reduced speed of sound is linked to enhanced non-Gaussianity.

Key advantages enumerated: (1) systematic parametrization of high-energy corrections to slow-roll; (2) explicit separation of what is forced by symmetry vs. what is free; (3) complete operator enumeration; (4) unification of all single-field models (DBI, Ghost Inflation, etc.); (5) removal of field-redefinition ambiguity present in the $\phi$ language; (6) transparent operator scaling for perturbation theory; (7) straightforward renormalization of loop corrections.

### Section 2: Construction of the Action in Unitary Gauge

The authors prove that the most general Lagrangian in unitary gauge can be written as:

$$S = \int d^4x \sqrt{-g} \left[ \tfrac{1}{2}M_{\rm Pl}^2 R - c(t)g^{00} - \Lambda(t) + \tfrac{1}{2!}M_2(t)^4(g^{00}+1)^2 + \tfrac{1}{3!}M_3(t)^4(g^{00}+1)^3 - \tfrac{\bar{M}_1(t)^3}{2}(g^{00}+1)\delta K^\mu{}_\mu - \tfrac{\bar{M}_2(t)^2}{2}(\delta K^\mu{}_\mu)^2 - \tfrac{\bar{M}_3(t)^2}{2}\delta K^\mu{}_\nu \delta K^\nu{}_\mu + \ldots \right]$$

The building blocks are: (a) polynomials of $g^{00}$ (the only terms without derivatives); (b) the extrinsic curvature $K_{\mu\nu}$ of constant-time surfaces; (c) the Riemann tensor and its derivatives; (d) arbitrary time-dependent coefficients.

Only the first three terms ($R$, $c(t)g^{00}$, $\Lambda(t)$) contain linear perturbations. The coefficients $c(t)$ and $\Lambda(t)$ are fixed by the Friedmann equations for a given $H(t)$:

$$H^2 = \frac{1}{3M_{\rm Pl}^2}[c(t)+\Lambda(t)], \quad \dot{H}+H^2 = -\frac{1}{3M_{\rm Pl}^2}[2c(t)-\Lambda(t)]$$

All remaining operators are free parameters encoding different theories of perturbations with the same background.

### Section 3: Action for the Goldstone Boson

The Goldstone $\pi$ is reintroduced via the Stuckelberg trick: performing a broken time diff $t \to t + \pi(t,\vec{x})$ on the unitary gauge action. The transformation rule is $\pi(x) \to \pi(x) - \xi^0(x)$.

At sufficiently high energies ($E \gg E_{\rm mix}$), the mixing of $\pi$ with metric perturbations can be neglected (the "equivalence theorem" for inflation). The mixing scale depends on which operators dominate:

- Standard slow-roll: $E_{\rm mix} \sim \epsilon^{1/2} H$
- Large $M_2$: $E_{\rm mix} \sim M_2^2/M_{\rm Pl}$

In the decoupling limit, the Goldstone action simplifies dramatically to eq. (28). The conserved quantity $\zeta = -H\pi$ is constant outside the horizon, reducing the problem to computing correlators at horizon crossing.

### Section 4: The Various Limits of Single Field Inflation

#### 4.1 Slow-Roll Inflation and High Energy Corrections

With all higher operators set to zero ($M_2 = M_3 = \bar{M}_1 = \bar{M}_2 = \ldots = 0$), one recovers standard slow-roll. The power spectrum of $\zeta$ is derived (eq. 32) and the spectral tilt at leading order in slow-roll (eq. 33). Radiative corrections generate higher operators with small coefficients: e.g., $M_2^4 \sim \dot{H}^2 \log\Lambda$ from graviton loops, giving speed-of-sound deviations $\gtrsim \epsilon^2 \cdot 10^{-10}$.

The gravity wave spectrum (eq. 34) and tensor-to-scalar ratio are discussed. Verification of the consistency relation $n_g = -2\epsilon_*$ constrains $M_2^4 \lesssim M_{\rm Pl}^2|\dot{H}|$ (eq. 35). The extrinsic curvature operator $\bar{M}_3^2 \delta K^\mu{}_\nu \delta K^\nu{}_\mu$ modifies the gravity wave dispersion relation (eq. 36).

#### 4.2 Small Speed of Sound and Large Non-Gaussianities

The spatial kinetic term $({\partial_i \pi})^2$ is fixed by $\dot{H}$, but the time kinetic term $\dot\pi^2$ receives a free contribution from $(g^{00}+1)^2$. This gives a speed of sound:

$$c_s^{-2} = 1 - \frac{2M_2^4}{M_{\rm Pl}^2 \dot{H}}$$

$M_2^4 > 0$ (for $\dot{H}<0$) is required to avoid superluminal propagation, which would prevent a Lorentz-invariant UV completion.

The same operator that reduces $c_s$ forces cubic couplings $\dot\pi(\nabla\pi)^2$ and $\dot\pi^3$, giving equilateral non-Gaussianity:

$$f_{\rm NL}^{\rm equil.} = \frac{85}{324} \cdot \frac{1}{c_s^2}$$

The experimental window $-256 < f_{\rm NL}^{\rm equil.} < 332$ (95% C.L.) translates to $c_s > 0.028$.

**Cutoff and naturalness** (Sec. 4.2.1): The strong-coupling scale is:

$$\Lambda^4 \simeq 16\pi^2 M_{\rm Pl}^2 |\dot{H}| \frac{c_s^5}{1-c_s^2}$$

Requiring $H \ll \Lambda$ gives $c_s \gg P_\zeta^{1/4} \simeq 0.003$. Small $c_s$ is natural: loop corrections to $({\nabla\pi})^2$ are bounded by the tree-level value at the unitarity cutoff.

#### 4.3 De Sitter Limit and the Ghost Condensate

In the limit $\dot{H} \to 0$ (exact de Sitter), the leading spatial kinetic term comes from the higher-derivative operators $(\delta K^\mu{}_\mu)^2$, giving a non-relativistic dispersion $\omega \propto k^2$ -- this is Ghost Inflation. The Goldstone has scaling dimension 1/4, making all operators besides the kinetic term irrelevant (the theory is a valid EFT). The spectrum (eq. 60) requires $(H/M)^{5/4} \simeq 10^{-5}$, and non-Gaussianity is parametrically $\sim P_\zeta^{1/5}$.

A new de Sitter limit (Sec. 4.3.1) exists when the operator $(g^{00}+1)\delta K^\mu{}_\mu$ dominates, giving $\omega^2 \propto k^2$ with small $c_s^2 = H/M$. Higher-order dispersion relations $\omega^2 \sim k^{2n}$ with $n \geq 3$ are excluded because the cubic operator $\dot\pi(\nabla\pi)^2$ becomes strong at low energy.

### Section 5: Conclusions

The formalism unifies all single-field models, makes symmetry constraints transparent, and provides a systematic parametrization analogous to BSM physics in the Standard Model. Extensions to quintessence, fluids, and multi-field models are suggested.

### Appendices

**Appendix A** proves that the most general unitary-gauge Lagrangian takes the form $S = \int d^4x \sqrt{-g}\, F(R_{\mu\nu\rho\sigma}, g^{00}, K_{\mu\nu}, \nabla_\mu, t)$. The building blocks are enumerated: (1) Riemann tensor terms; (2) generic time functions; (3) upper-0 index tensors from $\partial_\mu \tilde{t} \to \delta^0_\mu$; (4) induced metric and 3D Riemann tensor (redundant via Gauss-Codazzi); (5) extrinsic curvature from covariant derivatives of $n_\mu$.

**Appendix B** proves that the linear terms in the most general Lagrangian around a given FRW background reduce to $g^{00}$ and a cosmological constant term, whose coefficients are fixed by $H(t)$. All other operators start quadratic or higher in the fluctuations.

---

## Key Results

1. The most general single-field inflation EFT in unitary gauge is parametrized by a finite set of time-dependent coefficients ($M_2, M_3, \bar{M}_1, \bar{M}_2, \bar{M}_3, \ldots$) multiplying operators invariant under spatial diffeomorphisms.

2. The background evolution $H(t)$ fixes only two coefficients ($c(t)$ and $\Lambda(t)$); all differences between models are encoded in higher-order operators.

3. The Goldstone boson $\pi$ (related to $\zeta$ by $\zeta = -H\pi$) decouples from gravity at energies above the mixing scale $E_{\rm mix}$.

4. A reduced speed of sound ($c_s < 1$) is linked by the non-linear realization of time diffs to enhanced equilateral non-Gaussianity: $f_{\rm NL}^{\rm equil.} \sim 1/c_s^2$.

5. The strong-coupling cutoff for $c_s \ll 1$ scales as $\Lambda^4 \sim M_{\rm Pl}^2 |\dot{H}| c_s^5$; requiring perturbative control at $H$ gives $c_s \gg 0.003$.

6. In the exact de Sitter limit ($\dot{H}=0$), Ghost Inflation with $\omega \propto k^2$ emerges, and a second de Sitter limit with $\omega^2 \propto k^2$ (small $c_s^2 = H/M$) exists. Dispersion relations $\omega^2 \sim k^{2n}$ with $n \geq 3$ are excluded by EFT consistency.

7. Operators $(g^{00}+1)^n$ do not affect tensor modes; the extrinsic curvature operator $\bar{M}_3^2 \delta K^\mu{}_\nu \delta K^\nu{}_\mu$ modifies the graviton dispersion relation.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Unitary gauge action | $S = \int d^4x \sqrt{-g}\left[\tfrac{1}{2}M_{\rm Pl}^2 R + M_{\rm Pl}^2 \dot{H} g^{00} - M_{\rm Pl}^2(3H^2+\dot{H}) + \tfrac{M_2^4}{2!}(g^{00}+1)^2 + \tfrac{M_3^4}{3!}(g^{00}+1)^3 - \tfrac{\bar{M}_1^3}{2}(g^{00}+1)\delta K^\mu{}_\mu - \tfrac{\bar{M}_2^2}{2}(\delta K^\mu{}_\mu)^2 - \tfrac{\bar{M}_3^2}{2}\delta K^\mu{}_\nu \delta K^\nu{}_\mu + \ldots\right]$ | Eq. (10) |
| Goldstone action (decoupling) | $S_\pi = \int d^4x \sqrt{-g}\left[\tfrac{1}{2}M_{\rm Pl}^2 R - M_{\rm Pl}^2 \dot{H}(\dot\pi^2 - (\partial_i\pi)^2/a^2) + 2M_2^4(\dot\pi^2 + \dot\pi^3 - \dot\pi(\partial_i\pi)^2/a^2) - \tfrac{4}{3}M_3^4 \dot\pi^3 - \tfrac{\bar{M}^2}{2}\tfrac{1}{a^4}(\partial_i^2\pi)^2 + \ldots\right]$ | Eq. (28) |
| Speed of sound | $c_s^{-2} = 1 - \frac{2M_2^4}{M_{\rm Pl}^2 \dot{H}}$ | Eq. (38) |
| Goldstone action with $c_s$ | $S_\pi = \int d^4x \sqrt{-g}\left[-\frac{M_{\rm Pl}^2 \dot{H}}{c_s^2}\left(\dot\pi^2 - c_s^2 \frac{(\partial_i\pi)^2}{a^2}\right) + M_{\rm Pl}^2 \dot{H}\left(1-\frac{1}{c_s^2}\right)\left(\dot\pi^3 - \dot\pi\frac{(\partial_i\pi)^2}{a^2}\right) - \frac{4}{3}M_3^4 \dot\pi^3 \ldots\right]$ | Eq. (39) |
| Scalar power spectrum | $\langle\zeta(\vec{k}_1)\zeta(\vec{k}_2)\rangle = (2\pi)^3\delta(\vec{k}_1+\vec{k}_2)\frac{1}{c_{s*}}\cdot\frac{H_*^2}{4\epsilon_* M_{\rm Pl}^2}\frac{1}{k_1^3}$ | Eq. (40) |
| Spectral tilt (general) | $n_s - 1 = 4\frac{\dot{H}_*}{H_*^2} - \frac{\ddot{H}_*}{\dot{H}_* H_*} - \frac{\dot{c}_{s*}}{c_{s*} H_*}$ | Eq. (41) |
| Non-Gaussianity ($\dot\pi(\nabla\pi)^2$) | $f_{\rm NL}^{\rm equil.} = \frac{85}{324}\cdot\frac{1}{c_s^2}$ | Eq. (45) |
| Non-Gaussianity ($\dot\pi^3$) | $f_{\rm NL,\,\dot\pi^3}^{\rm equil.} \sim 1 - \frac{4}{3}\frac{M_3^4}{M_{\rm Pl}^2|\dot{H}|c_s^{-2}}$ | Eq. (44) |
| Strong-coupling cutoff | $\Lambda^4 \simeq 16\pi^2 M_{\rm Pl}^2 |\dot{H}|\frac{c_s^5}{1-c_s^2}$ | Eq. (50) |
| Perturbative control bound | $c_s \gg P_\zeta^{1/4} \simeq 0.003$ | Eq. (52) |
| Tensor spectrum | $\langle\gamma^s(\vec{k}_1)\gamma^{s'}(\vec{k}_2)\rangle = (2\pi)^3\delta(\vec{k}_1+\vec{k}_2)\frac{H_*^2}{M_{\rm Pl}^2}\frac{1}{k_1^3}\delta_{ss'}$ | Eq. (34) |
| Tensor action with $\bar{M}_3$ | $S_\gamma = \frac{M_{\rm Pl}^2}{8}\int d^4x \sqrt{-g}\left[\left(1-\frac{\bar{M}_3^2}{M_{\rm Pl}^2}\right)\dot\gamma_{ij}\dot\gamma_{ij} - \frac{1}{a^2}\partial_l\gamma_{ij}\partial_l\gamma_{ij}\right]$ | Eq. (36) |
| Ghost Inflation dispersion | $\omega^2 = \frac{\bar{M}^2}{M_2^4}\cdot k^4$ | Sec. 4.3 |
| Ghost spectrum | $\langle\zeta(\vec{k}_1)\zeta(\vec{k}_2)\rangle \sim (2\pi)^3\delta(\vec{k}_1+\vec{k}_2)\frac{H^2}{M^4}(HM^3)^{1/2}\frac{1}{k_1^3}$ | Eq. (60) |
| $\zeta$-$\pi$ relation | $\zeta(t,\vec{x}) = -H\pi(t,\vec{x})$ | Eq. (30) |
| Friedmann (unitary gauge) | $H^2 = \frac{1}{3M_{\rm Pl}^2}[c(t)+\Lambda(t)]$ | Eq. (8) |
| Most general UG action | $S = \int d^4x \sqrt{-g}\, F(R_{\mu\nu\rho\sigma}, g^{00}, K_{\mu\nu}, \nabla_\mu, t)$ | Eq. (75) |

---

## Relevance to Phonon-Exflation

This paper is foundational for connecting the phonon-exflation framework to the standard inflationary perturbation theory literature. The EFT of inflation organizes all single-field models by their operator content in unitary gauge -- this is precisely the language needed to compare the spectral action's effective operator hierarchy ($a_0$, $a_2$, $a_4$ Seeley-DeWitt coefficients) against the standard EFT parametrization ($M_2$, $M_3$, $\bar{M}_n$). The speed of sound $c_s$ derived here from the $(g^{00}+1)^2$ operator maps directly onto the acoustic impedance mismatch at the exflation fold: the framework's Mach 13.75 supersonic transit predicts a specific $c_s$ profile through the fold that this EFT language can diagnose. The strong-coupling cutoff $\Lambda \sim (M_{\rm Pl}^2 |\dot{H}| c_s^5)^{1/4}$ is directly relevant to whether the spectral action's $\Lambda$ cutoff introduces the same hierarchy problems Burgess later examines. The Goldstone boson $\pi$ of broken time diffs is the direct analog of the phononic excitations in the exflation picture -- both are the scalar mode that emerges from spontaneous breaking of a symmetry by the background evolution.
