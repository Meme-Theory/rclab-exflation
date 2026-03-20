# The Weinberg No-Go Theorem for Cosmological Constant and Nonlocal Gravity

**Authors:** Salvatore Capozziello, Matteo De Bianchi, Anupam Mazumdar, Giuseppe Buoninfante

**Year:** 2025

**Journal:** arXiv:2502.07321

---

## Abstract

This paper addresses a foundational problem in theoretical cosmology: the Weinberg no-go theorem, which forbids any solution to the cosmological constant problem within local field theories. The authors demonstrate that nonlocal gravitational interactions can circumvent this no-go constraint. Infinite-derivative gravity theories, characterized by gravitational actions involving nonlocal operators (e.g., exponentials of d'Alembertian), provide a systematic framework for understanding cosmic acceleration without invoking a fundamental cosmological constant or dynamical scalar fields. The paper synthesizes recent developments in nonlocal gravity, emphasizing both theoretical consistency and observational compatibility with Type Ia supernovae, BAO, and CMB data.

---

## Historical Context

The cosmological constant problem has plagued theoretical physics since Einstein's 1917 introduction of Lambda. Weinberg's no-go theorem (1987-1989) states that in any local quantum field theory with a finite vacuum state, the cosmological constant must be either exactly zero (by symmetry) or fine-tuned. The problem deepens when one considers vacuum energy contributions from quantum loops: the observed Lambda is 120 orders of magnitude smaller than the natural quantum scale, the Planck mass.

By the 1990s, two dominant paradigms emerged:
1. **Dynamical Dark Energy** (quintessence, k-essence, scalar field potentials)
2. **Modified Gravity** (f(R) gravity, scalar-tensor theories)

Both face criticisms: quintessence requires a flat potential (why?), and f(R) modifications typically introduce fifth forces that are constrained by solar-system tests.

The revival of nonlocal gravity came from string theory (Siegel 1989, Areshenkov et al. 2000s) and quantum gravity (Wheeler-DeWitt equation, Hartle-Hawking). The key insight is that nonlocal operators naturally appear in quantum gravity:
- The graviton propagator in quantum gravity is not strictly local at the Planck scale
- String theory amplitudes contain nonanalytic kinetic factors
- The heat kernel of the Dirac operator (relevant to spectral action) is inherently nonlocal

Capozziello and collaborators have spent the last decade developing the theory and phenomenology of infinite-derivative gravity. This 2025 paper explicitly addresses Weinberg's no-go theorem as a motivation.

---

## Key Arguments and Derivations

### Weinberg's No-Go Theorem (Classical Statement)

In local effective field theory, the vacuum energy density is:

$$\rho_{\text{vac}} = \sum_i \hbar \omega_i / 2 + T(\text{loop corrections})$$

If we assume:
1. Lorentz invariance (vacuum is isotropic)
2. Locality (interactions vanish outside a light cone)
3. Unitarity (norm of states preserved)
4. Relativistic dispersion $\omega = \sqrt{p^2 + m^2}$

Then any renormalization scheme (including dimensional regularization, zeta-function regularization) produces:

$$\Lambda_{\text{eff}} = \Lambda_0 + \text{counter-terms}$$

where $\Lambda_0$ is a bare cosmological constant that must be fine-tuned order-by-order in perturbation theory to match observations. The theorem is essentially *no symmetry principle can enforce Lambda = 0 without additional structure*.

### Nonlocal Gravity Action

Nonlocal gravity generalizes Einstein-Hilbert to:

$$S = \frac{1}{16\pi G_N} \int d^4 x \sqrt{-g} \left[ R + f(R, \mathcal{G}, \Box) \right] + S_m[g_{\mu\nu}, \psi]$$

where $\Box = \nabla^\mu \nabla_\mu$ is the covariant d'Alembertian, and $f$ is a nonlocal function. The simplest form:

$$f(R, \mathcal{G}, \Box) = R + m^2 R \mathcal{G}(m^{-2}\Box) R + \lambda R \mathcal{G}(m^{-2}\Box) \mathcal{G}(m^{-2}\Box) \mathcal{G}_{\mu\nu}$$

where $\mathcal{G}(z)$ is a form factor (typically exponential: $\mathcal{G}(z) = e^{z}$), and $\mathcal{G}_{\mu\nu}$ is the Gauss-Bonnet tensor:

$$\mathcal{G}_{\mu\nu} = R R_{\mu\nu} - 4 R^\lambda_\mu R^\rho_\lambda g_{\nu\rho} + R^\lambda\rho_{\mu\nu} R_{\lambda\rho}$$

The Gauss-Bonnet invariant in 4D is:

$$\mathcal{G} = R^2 - 4 R_{\mu\nu}^2 + R_{\mu\nu\rho\sigma}^2 = \partial_\mu K^\mu$$

with $K^\mu$ a divergence. In the action, it vanishes on-shell (in flat 4D), but it contributes to equations of motion via the nonlocal coupling.

### How Nonlocality Circumvents Weinberg

The key is that nonlocal operators modify the dispersion relation:

$$\omega^2 = p^2 f(\Box) + m^2$$

where $f(\Box)$ depends on the field's self-interaction scale. For exponential form factors:

$$f(\Box) \sim e^{\Box/M^2}$$

The zero-point energy becomes:

$$\rho_{\text{vac}} = \int_0^\infty \frac{dp}{2\pi^2} p^2 \sqrt{p^2 f(\Box) + m^2}$$

with $\Box \to -p^2$ in momentum space. The exponential suppresses high-momentum contributions:

$$\rho_{\text{vac}} \sim \int_0^{M} dp \, p^2 \sqrt{p^2 e^{p^2/M^2} + m^2}$$

The UV cutoff becomes effective and finite. Loop corrections are also suppressed by the nonlocal kernel. This breaks the locality assumption of Weinberg's theorem without violating unitarity (at tree level; quantum properties require care).

**Why Weinberg's no-go no longer applies**: Weinberg's theorem assumes locality of both the kinetic operator and the vertex structure. Nonlocal gravity has non-local kinetic terms, making the assumptions invalid.

### Cosmological Solutions in Nonlocal Gravity

The modified Friedmann equation in the simplest nonlocal model is:

$$H^2 + \frac{k}{a^2} = \frac{8\pi G_N}{3} \rho_m + \rho_{\text{eff}}$$

where $\rho_{\text{eff}}$ arises from the nonlocal geometric term. For metric-Ricci models:

$$\rho_{\text{eff}} = -\frac{1}{8\pi G_N} \left[ f(R) - R f_R(R) + 3 H f_{RR}(R) \dot{R} + 3 H^2 f_{RR}(R) \right]$$

with $f_R = \partial f / \partial R$ and $f_{RR} = \partial^2 f / \partial R^2$. The nonlocal contribution modifies the effective dark energy equation of state:

$$w_{\text{eff}} = \frac{p_{\text{eff}}}{\rho_{\text{eff}}} \approx -1 + \frac{1}{3} \frac{d \ln \rho_{\text{eff}}}{d \ln a}$$

In exponential nonlocal models, as the universe expands ($a \to \infty$, $H \to 0$), the nonlocal kernel becomes sensitive to lower curvatures, and $w_{\text{eff}}$ evolves. The authors show that $w(a)$ can remain near -1 (mimicking a cosmological constant) while still being technically dynamical.

### Matter Coupling and Equivalence Principle

Nonlocal gravity couples to matter via:

$$S_m = \int d^4 x \sqrt{-g} \mathcal{L}_m[g_{\mu\nu}, \psi]$$

No explicit fifth force is introduced. The nonlocality is purely geometric (in the gravitational action), preserving the Equivalence Principle at the classical level. However, nonlocal effects modify geodesic equations at order-M^{-2} (M is the nonlocality mass scale):

$$\ddot{x}^\mu + \Gamma^\mu_{\nu\lambda} \dot{x}^\nu \dot{x}^\lambda + \frac{1}{M^2} (\text{nonlocal correction terms}) = 0$$

Solar system tests constrain M > 10^{18} GeV (or equivalently, the nonlocality scale is sub-millimeter for macroscopic objects), so Equivalence Principle violations are below current sensitivity.

---

## Key Results

1. **Circumvention of Weinberg's Theorem**: Nonlocal gravity provides a consistent gravitational theory that does not require a fine-tuned bare cosmological constant. The UV finiteness of nonlocal actions eliminates the worst ultraviolet divergences in vacuum energy.

2. **Observational Consistency**: Nonlocal models with exponential form factors and Gauss-Bonnet coupling match Type Ia supernovae, BAO, and CMB data as well as ΛCDM, with similar parameter bounds. The effective dark energy density today is $\Omega_\Lambda \sim 0.68$, consistent with observations.

3. **Dynamical Dark Energy Signature**: Unlike ΛCDM, nonlocal gravity predicts a time-evolving dark energy equation of state $w(a)$. Current constraints from DESI DR2 allow $w$ to vary by ±0.2 around -1, consistent with nonlocal predictions. Future observations may distinguish nonlocal gravity from ΛCDM.

4. **Modified Gravitational Wave Propagation**: Graviton dispersion in nonlocal gravity is:

$$v_{gw} = c \sqrt{1 + O(H^2/M^2)} \approx c$$

for M >> H (Hubble scale). Current LIGO/Virgo observations rule out large deviations, constraining the nonlocality mass scale to M > 10^8 GeV.

5. **Scalar-Tensor Equivalence**: Nonlocal metric-Ricci gravity can be reformulated as a scalar-tensor theory with a single extra scalar degree of freedom. This scalar, the "nonlocal mode," has mass proportional to M. Its coupling to matter is suppressed by M^{-1}, consistent with fifth-force constraints.

6. **Stability and Hyperbolicity**: The authors prove that the nonlocal Cauchy problem is well-posed (hyperbolicity) for exponential form factors with finite M. This ensures predictions are causally consistent.

---

## Impact and Legacy

Capozziello's 2025 paper represents the maturation of nonlocal gravity as a viable alternative to ΛCDM and quintessence. It has influenced recent work on:

- **Swampland Conjectures**: Nonlocal gravity as a UV completion of gravity that avoids de Sitter conjectures
- **Quantum Gravity Phenomenology**: Low-scale nonlocality (M ~ 10^{16} GeV) as a signal of quantum gravity
- **Dark Energy Observables**: Distinguishing nonlocal dark energy from ΛCDM via high-precision CMB and BAO measurements

The explicit connection to Weinberg's theorem is pedagogically important: it shows that "new physics" beyond local QFT is required to explain the observed cosmological constant, not just more scalar fields or modified gravity.

---

## Connection to Phonon-Exflation Framework

**STRONG STRUCTURAL ANALOGY.**

The phonon-exflation framework shares the nonlocal gravity structure in a crucial way:

**Spectral Action Nonlocality**: The spectral action in noncommutative geometry,

$$S_{\text{spec}} = \text{Tr}(\mathcal{A}(D_K))$$

where $D_K$ is the Dirac operator on M4 x SU(3) and $\mathcal{A}$ is a spectral profile function, is inherently **nonlocal in position space**. It depends on the full spectrum of $D_K$, not just its value at a point.

Expanding in eigenmodes:

$$S_{\text{spec}} = \sum_n \mathcal{A}(\lambda_n) = \int d^4 x \int_0^\infty dt \, f(t) \text{heat kernel trace}(e^{t D_K^2})$$

where the heat kernel $K(t; x, x)$ propagates information non-locally over distances $\sim \sqrt{t}$.

**Cosmological Implication**: Just as nonlocal gravity avoids a fine-tuned cosmological constant by modifying the UV behavior of gravity, the framework's spectral action (depending on the full Dirac spectrum including the gap edge and van Hove singularities) naturally reproduces the observed dark energy scale without fine-tuning a bare Lambda.

**Difference from ΛCDM**: In ΛCDM, $\Lambda$ is a fundamental constant chosen to match observations. In the framework (like nonlocal gravity), $\Lambda_{\text{eff}}(z)$ emerges dynamically from the geometry of the internal fiber (SU(3)) and evolves with cosmology.

**Quantitative prediction conflict**:
- Nonlocal gravity: allows $w = -1 \pm 0.2$ from DESI
- Framework: predicts $w = -1 + O(10^{-29})$ (exact ΛCDM-like)
- DESI DR2: observes $w_0 \sim -0.75$, $w_a \sim -1.05$ (2.5-3.7σ away from $w=-1$)

This tension suggests the framework's spectral action route (Paper #15, #17 discussions) is under stress. Either the framework's monotonicity theorem for spectral action is wrong, or the coupling between moduli dynamics (tau evolution) and the spectral action is non-trivial (as Session 37-38 instanton mechanism implies).

**Possible resolution**: The framework's dark energy is NOT driven by the spectral action potential (which is monotonic and has no minimum), but by the many-body instanton gas dynamics during transit (Kibble-Zurek). The observed "w != -1" from DESI would then reflect the time-dependent nature of the instanton gas, similar to how nonlocal gravity produces dynamical dark energy. This would require a quantum-kinetic equation for the instanton density during the tau evolution.

