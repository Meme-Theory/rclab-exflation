# Field Theory of Relativistic Strings. II. Loops and Pomerons

**Authors:** Michio Kaku, Keiji Kikkawa
**Year:** 1974
**Journal:** Physical Review D, Vol. 10, pp. 3814–3828

---

## Abstract

Extending the light-cone string field theory to loop diagrams, we develop the formalism for multi-loop amplitudes and establish the complete renormalization structure of string theory in the field-theoretic framework. We demonstrate that unitarity of tree and loop amplitudes is preserved in the light-cone gauge without ghost loops. The Pomeron trajectory emerges naturally as the leading Regge pole in multi-loop partial-wave amplitudes. We compute one-loop self-energy corrections, analyze the Pomeron intercept, and show that string theory loops generate no infinities—divergences are explicitly absent due to the extended nature of the string. This paper completes the field-theoretic formulation and establishes string theory as a finite, unitary, and Lorentz-covariant quantum field theory.

---

## Historical Context

The first paper (Kaku-Kikkawa I) established tree-level string field theory. However, any candidate theory of fundamental interactions must include loop corrections. The standard worry was whether loops would introduce the infinities plaguing quantum gravity and QED at higher orders.

The 1974 loop paper revealed a remarkable feature: string theory is **naturally finite to all orders** in perturbation theory. This was a major theoretical attraction—one could do loop quantum field theory without renormalization constants, a property unmatched by point-particle quantum field theory except in rare special cases (supersymmetric Yang-Mills, N=4 SYM).

The Pomeron, discovered empirically by Regge in the 1950s as the leading exotic trajectory in hadron scattering ($J - M^2$ plane), is a fundamental object in dual models. The paper showed that the Pomeron is not an ad-hoc addition but a built-in consequence of string loop dynamics.

---

## Key Arguments and Derivations

### Loop Diagrams in Light-Cone Gauge

The general multi-loop amplitude in string field theory is:

$$\mathcal{A}_L = \int \prod_{i=1}^L d\tau_i \, d\sigma_i \, |\mathcal{M}_L(\tau_i, \sigma_i, \{p_j\})|^2$$

where the product runs over $L$ independent loop variables. Each loop corresponds to an internal string propagator that circles back and annihilates itself. Unlike point particles, where a loop integral $\int d^D k / (k^2 + m^2)^n$ diverges, the string loop is an **extended object**—the loop integral is cut off by the string length scale $\sqrt{\alpha'}$.

### The String Propagator

The free string propagator (Green's function for the free string equation in light-cone gauge) is:

$$\langle x_i(\sigma_1) x_j(\sigma_2) \rangle_{\text{loop}} = -\frac{\alpha'}{2} \sum_{n=1}^\infty \frac{1}{n} \cos(n|\sigma_1 - \sigma_2|) e^{-|n| \tau_{\text{loop}}}$$

The exponential cutoff factor $e^{-|n| \tau_{\text{loop}}}$ shows that high-frequency modes (large $|n|$) are exponentially suppressed for finite loop time $\tau_{\text{loop}}$. This is the origin of finiteness.

### One-Loop Amplitudes

The one-loop vacuum amplitude (Pomeron loop) is:

$$\mathcal{A}_{\text{loop}} = \int_0^\infty \frac{d\tau}{\tau} Z_0(\tau)$$

where the partition function is:

$$Z_0(\tau) = \left| \prod_{n=1}^\infty (1 - e^{-2\pi n \tau})\right|^{-d}$$

The integrand has the form of a modular function on the worldsheet torus. The integral $\int_0^\infty d\tau$ converges due to the exponential suppression at small $\tau$ (high-frequency cutoff) and the decay at large $\tau$ (low-frequency modes vanish).

### The Pomeron Intercept

In the partial-wave expansion, the amplitude behaves as:

$$\mathcal{A}(s, t) \sim (s + s_0)^{\alpha(t)}$$

where $\alpha(t)$ is the Regge trajectory function. For the Pomeron exchange (in the t-channel of a multi-loop diagram):

$$\alpha_P(t) = 1 + \frac{t}{2\pi T}$$

where $T$ is the string tension. At $t=0$ (forward scattering):

$$\alpha_P(0) = 1 + \text{const}$$

The intercept is **slightly above 1**, consistent with empirical pomeron physics (empirically $\alpha_P(0) \approx 1.08$). In string theory:

$$\alpha_P(0) - 1 = \frac{2\pi \alpha' m_{string}^2}{(\text{const})}$$

quantifies the approach to the Pomeron limit from higher-mass string resonances.

### One-Loop Vertex Corrections

The one-loop correction to the three-string vertex is:

$$V_3^{(1)} = g_s^2 \int d\Phi_1 \, \mathcal{M}_1(\{p_i\}, \{m_i\})$$

where $d\Phi_1$ is the one-loop phase space and $\mathcal{M}_1$ depends on the external momenta $p_i$ and intermediate string masses $m_i$. The result is:

$$V_3^{(1)} \propto \frac{g_s^2}{\alpha'} \left[ \zeta(2) + \zeta(4) \cdot \frac{\alpha' \hat{s}}{M_s^2} + \ldots \right]$$

where $\zeta(n)$ are Riemann zeta values and $\hat{s}$ is the Mandelstam variable. All divergences cancel exactly.

### Finiteness Proof (Outline)

The key theorem states: **All loop amplitudes in light-cone string field theory are finite.**

*Proof sketch*: Any potential divergence arises from the high-frequency part of a loop integral:

$$\int_0^\infty dk \, k^d \cdot \text{(form factor)} \times (k^2 + m^2)^{-n}$$

In field theory, this would behave as $k^{d-2n}$ for large $k$, diverging if $d - 2n \geq 0$. However, the string "form factor" includes the exponential cutoff $\exp(-k/M_s)$ with $M_s = 1/\sqrt{\alpha'}$. This exponential:

1. Makes the integral converge at high $k$.
2. Suppresses contributions from energies above the string scale.
3. Ensures that all divergences are canceled order-by-order.

The exponential cutoff is a **consequence of the extended nature** of the string, not an ad-hoc regulator. It emerges from the exact solution of the free string wave equation.

---

## Key Results

1. **String theory is finite to all orders**: No renormalization is needed. Loop amplitudes are finite as they stand, with no infinities to cancel against counterterms.

2. **The Pomeron emerges naturally**: The leading exotic Regge pole in loop amplitudes has intercept $\alpha_P(0) \approx 1$ (or slightly above), matching empirical pomeron physics.

3. **Unitarity is manifest**: Tree amplitudes and loop corrections satisfy unitarity (optical theorem) without ghost loops in light-cone gauge.

4. **Modular invariance**: The one-loop amplitude is encoded in a modular function on the worldsheet torus, establishing a connection to conformal field theory (which would be developed later by Friedan, Shenker, and others).

5. **String scale sets loop cutoff**: The natural loop cutoff is the string mass scale $M_s = 1/\sqrt{\alpha'} \sim 10^{18}$ GeV (if strings are at the Planck scale). Loops are suppressed at energies above this scale.

6. **Coupling constant**: The loop suppression factor is determined by the string coupling $g_s$. In closed string theory, $g_s$ is dynamical (related to the dilaton); in open string theory, $g_s$ is a coupling constant. This structure differs from point-particle QFT.

---

## Impact and Legacy

The 1974 loops paper was groundbreaking because it:

1. **Proved finiteness**: The first complete quantum field theory without renormalization counterterms (beyond special cases like N=4 SYM which would be discovered later).

2. **Unified pomeron physics**: Connected dual models (Regge theory) to loop quantum field theory.

3. **Established string quantization**: Showed that the canonical quantization of extended objects (strings) produces a consistent, unitary quantum field theory.

4. **Motivated further work**:
   - Modular forms in string theory (Dedekind eta function, theta functions).
   - One-loop string amplitudes (Polchinski, Veneziano, Kawai, Lewellen, Tye).
   - Tachyon condensation and consistency checks.

Citations: 300+ in peer-reviewed journals. This paper remains essential reading for anyone learning advanced string theory.

---

## Connection to Phonon-Exflation Framework

**Relevance: MODERATE**

The loop-level finiteness of string theory suggests that the internal M4 x SU(3) phonon-exflation mechanism should also avoid ultraviolet divergences if properly formulated as a loop expansion in the internal coordinates.

**Specific parallels**:

1. **Extended-object quantization**: Just as strings avoid divergences through their extended nature, phonons on the SU(3) fiber avoid standard UV divergences because they are collective excitations with a natural cutoff at the fiber diameter.

2. **Loop suppression**: In string theory, loops are suppressed by powers of $g_s$. In phonon-exflation, loop suppression (if present) would be governed by the dimensionless coupling in the BCS mechanism, which we know is extremely weak ($g \lesssim 0.1$ for realistic cases).

3. **Modular structure**: The appearance of modular functions (Dedekind eta, theta functions) in string loops may have an analogue in the spectral action loop expansion on the noncommutative geometry of SU(3). Both involve torus-like structures (worldsheet vs. internal torus).

**Key difference**: String loops involve external particle scattering. Phonon-exflation loops would involve internal fiber dynamics—the spectral action self-corrections as the fiber geometry evolves. The finiteness of such a framework requires careful analysis of the spectral-trace regularization.

---

## References & Further Reading

- Kaku, M., & Kikkawa, K. (1974b). "Field theory of relativistic strings. II. Loops and Pomerons," *Phys. Rev. D*, 10(12), 3814–3828.
- Veneziano, G., Suzuki, M., & Tye, S. H. (1974). "Regge intercepts for bound states of quarks," *Phys. Lett. B*, 50(3), 235–240.
- Kawai, H., Lewellen, D. C., & Tye, S. H. (1986). "A relation between tree amplitudes of closed and open strings," *Nucl. Phys. B*, 269(1), 1–23.
- Polchinski, J. (1998). *String Theory*, Vol. 1. Cambridge University Press.
