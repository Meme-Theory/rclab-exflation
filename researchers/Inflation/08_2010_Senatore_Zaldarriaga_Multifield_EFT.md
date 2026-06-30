# The Effective Field Theory of Multifield Inflation

**Author(s):** Leonardo Senatore, Matias Zaldarriaga
**Year:** 2012 (v2; originally 2010)
**Journal:** [not specified in PDF]
**arXiv:** 1009.2093
**Relevance:** HIGH

---

## Abstract

We generalize the Effective Field Theory of Inflation to include additional light scalar degrees of freedom that are in their vacuum at the time the modes of interest are crossing the horizon. In order to make the scalars light in a natural way we consider the case where they are the Goldstone bosons of a global symmetry group or are partially protected by an approximate supersymmetry. We write the most general Lagrangian that couples the scalar mode associated to the breaking of time translation during inflation to the additional light scalar fields. This Lagrangian is constrained by diffeomorphism invariance and the additional symmetries that keep the new scalars light. This Lagrangian describes the fluctuations around the time of horizon crossing and it is supplemented with a general parameterization describing how the additional fluctuating fields can affect cosmological perturbations. We find that multifield inflation can reproduce the non-Gaussianities that can be generated in single field inflation but can also give rise to new kinds of non-Gaussianities. We find several new three-point function shapes. We show that in multifield inflation it is possible to naturally suppress the three-point function making the four-point function the leading source of detectable non-Gaussianities. We find that under certain circumstances, ie. if specific shapes of non-Gaussianities are detected in the data, one could distinguish between single and multifield inflation and sometimes even among the various mechanisms that kept the additional fields light.

---

## Key Arguments and Derivations

### Section 1: Introduction and Summary of Signatures

The paper extends the single-field EFT of inflation (Cheung et al.) to include additional light scalar degrees of freedom $\sigma_I$ ($I = 1, \ldots, N$) present during inflation. The key challenge: making scalars naturally light requires either (1) them being Goldstone bosons of a spontaneously broken global symmetry, or (2) approximate supersymmetry.

The summary of signatures (Tables 1 and 2) catalogs all possible non-Gaussian signals from multifield inflation versus single-clock inflation, organized by operator, dispersion relation ($\omega = c_s k$ or $\omega \propto k^2$), type (adiabatic/isocurvature), and origin (Abelian, non-Abelian, SUSY, reheating).

### Section 2: Review of Single-Clock EFT

Reproduces the Cheung et al. unitary gauge action (eq. 1) and the Goldstone boson action (eq. 5). The speed of sound relation $M_2^4 = -(1-c_s^2)M_{\rm Pl}^2\dot{H}/(2c_s^2)$ connects the EFT coefficient to the observable $c_s$.

### Section 3: Additional Light Scalar Fields

**3.1 Abelian case ($U(1)^N$ shift symmetry):** The most general unitary-gauge Lagrangian for the $\sigma_I$ fields is constructed from two building blocks: $g^{0\mu}\partial_\mu\sigma_I$ and $g^{\mu\nu}\partial_\mu\sigma_I\partial_\nu\sigma_J$ (eq. 7). After Stuckelberg and decoupling from gravity, the quadratic Lagrangian (eq. 10) shows:
- Each $\sigma_I$ can have a different speed of sound via the operator $\tilde{e}_2^I (g^{0\mu}\partial_\mu\sigma_I)^2$ -- generalizing multifield DBI where all fields share the same $c_s$.
- A time-kinetic mixing $\dot\pi\dot\sigma_I$ (proportional to $\tilde{M}_1^{2\,I}$) is allowed, but spatial-kinetic mixing $\partial_i\pi\partial_i\sigma_I$ is forbidden by the non-linear realization of time diffs.
- Ghost-free condition requires $\epsilon_{\rm unmix} \equiv (1+e_2)(2M_2^4 - \dot{H}M_{\rm Pl}^2)/\tilde{M}_1^4 - 1 > 0$.
- Ghost-condensate-like dispersion $\omega^2 \sim k^4/\bar{\bar{M}}^2$ is possible for $\sigma$ fields.

The cubic Lagrangian (eq. 11) contains $(6 + 13N + 9N^2 + 2N^3)/3$ operators for $N$ additional scalars. Crucially, some cubic coefficients are fixed by the quadratic Lagrangian through the non-linear realization of time diffs (e.g., $\tilde{e}_2^I \dot\sigma_I^2 \to \tilde{e}_2^I (\partial_i\pi\partial_i\sigma_I/a^2)\dot\sigma_I$).

The quartic Lagrangian (eq. 20) has three independent operators: $\dot\sigma^4$, $\dot\sigma^2(\partial_i\sigma)^2$, and $(\partial_i\sigma)^4$, of which only the Lorentz-invariant combination $(\partial_\mu\sigma)^4$ survives if approximate Lorentz symmetry is imposed.

**Soft-breaking Lagrangian:** The $U(1)$ must be explicitly broken for $\sigma$ fluctuations to affect curvature perturbations. A cosine potential $V(\sigma) = -a_1\mu^4\cos(\sigma/M + \theta)$ gives mass $m^2 \sim \mu^4/M^2$, requiring $\mu^4 \ll H^2 M^2$ for light fields. The leading odd interaction is suppressed to order $\mu^8/M^7$ (eq. 25), with new operators like $\sigma(\partial\sigma)^2$ from the breaking (eq. 26).

**3.2 Non-Abelian case ($G \to H$):** The Goldstone bosons $\sigma_a$ parametrize the coset $G/H$ via $\gamma = \exp(i\sigma_a x_a)$. The Maurer-Cartan form $\gamma^{-1}\partial_\mu\gamma = ix_a D_{a\mu} + it_i E_{i\mu}$ defines the building block $D_{a\mu}$ (eq. 31-32). The Lagrangian is built from traces of products of $D_\mu$ and its covariant derivatives (eq. 38), coupled to the $\pi$ Goldstone through unitary gauge operators. Key novelty: for non-Abelian groups, operators like $\sigma\dot\sigma^2$ and $\sigma(\partial_i\sigma)^2$ can appear without soft breaking, and for some groups the cubic operators $\dot\sigma^3$ and $\dot\sigma(\partial_i\sigma)^2$ are forbidden by symmetry.

**3.3 Supersymmetric case:** SUSY breaking during inflation gives scalar masses $\sim H$, too heavy for scale-invariant fluctuations. An accidental tuning of $\sim 50$ is needed. The resulting EFT is less constrained than the Goldstone case since no shift symmetry protects the scalars.

### Section 4: Conversion of $\sigma$ Fluctuations to Observables

The curvature perturbation $\zeta$ is parametrized as a local Taylor expansion in the fluctuations at horizon crossing (eq. 61, analogous to $\delta N$ formalism):

$$\zeta(x) = -H\pi(x) + \frac{\partial\zeta}{\partial\sigma_I}\bigg|_0 \sigma_I(x) + \frac{1}{2}\frac{\partial^2\zeta}{\partial\sigma_I\partial\sigma_J}\bigg|_0 \sigma_I(x)\sigma_J(x) + \ldots$$

The coefficients involving $\pi\sigma_I$ are suppressed by shift-symmetry breaking. The number of free parameters is $N(N+3)/2$ (Abelian), with analogous counts for non-Abelian and SUSY cases (eq. 66). Isocurvature fluctuations are similarly parametrized (eq. 68).

### Section 5: Signatures

**Detectable four-point function:** In multifield inflation, approximate symmetries ($\pi \to -\pi$, $\sigma_I \to -\sigma_I$, or approximate Lorentz invariance) can suppress all cubic interactions while leaving the quartic $(\partial\sigma)^4$ large. This is the first case where large non-Gaussianities can arise without large Lorentz violation. The Lorentz-invariant operator $(\partial_\mu\sigma)^4/\tilde{\tilde{M}}^4$ gives $g_{NL} \sim 10^{10} H^4/\tilde{\tilde{M}}^4$ (eq. 80). The soft-breaking operator $\sigma^4$ gives a local $g_{NL} \sim (\mu^4/\Lambda_{U,S}^4)N_e$ (eq. 84).

**Three-point functions:** New shapes beyond single-field arise from $\sigma(\partial_\mu\sigma)^2$ (from soft breaking), with non-vanishing squeezed limits distinguishing them from equilateral shapes.

---

## Key Results

1. The multifield EFT is constructed for three cases of naturally light scalars: Abelian Goldstone bosons (shift symmetry), non-Abelian Goldstone bosons (coset $G/H$), and approximate SUSY.

2. Each additional scalar can have an independent speed of sound; time-kinetic mixing $\dot\pi\dot\sigma$ is allowed but spatial-kinetic mixing $\partial_i\pi\partial_i\sigma$ is forbidden by the non-linear realization of time diffs.

3. Multifield inflation can produce new non-Gaussian shapes beyond single-field, including shapes from $\sigma(\partial_\mu\sigma)^2$ with non-vanishing squeezed limits.

4. Approximate symmetries (Lorentz invariance, $\sigma \to -\sigma$ parity, or non-Abelian structure) can naturally suppress the three-point function, making the four-point function the leading non-Gaussianity -- a qualitatively new possibility absent in single-field models.

5. Detection of specific shapes can distinguish single vs. multifield inflation and even identify the symmetry mechanism (Abelian, non-Abelian, or SUSY).

6. The conversion of $\sigma$ fluctuations to curvature perturbations is parametrized by a local Taylor expansion (analogous to $\delta N$) with $N(N+3)/2$ free parameters.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Single-field EFT action | $S_{\rm EH+SF} = \int d^4x\sqrt{-g}\left[\tfrac{1}{2}M_{\rm Pl}^2 R + M_{\rm Pl}^2\dot{H}g^{00} - M_{\rm Pl}^2(3H^2+\dot{H}) + \tfrac{M_2^4}{2!}(g^{00}+1)^2 + \ldots\right]$ | Eq. (1) |
| Speed of sound relation | $M_2^4 = -\frac{1-c_s^2}{c_s^2}\frac{M_{\rm Pl}^2\dot{H}}{2}$ | Eq. (6) |
| Multifield unitary gauge action | $S_{\rm MF} = \int d^4x\sqrt{-g}\left[\tilde{M}_1^{2\,I}(g^{00}+1)(g^{0\mu}\partial_\mu\sigma_I) - e_1^{IJ}g^{\mu\nu}\partial_\mu\sigma_I\partial_\nu\sigma_J + e_2^{IJ}(g^{0\mu}\partial_\mu\sigma_I)(g^{0\mu}\partial_\mu\sigma_J) + \ldots\right]$ | Eq. (7) |
| Quadratic Lagrangian | $S^{(2)} = \int d^4x\sqrt{-g}\left[(2M_2^4-M_{\rm Pl}^2\dot{H})\dot\pi^2 + M_{\rm Pl}^2\dot{H}\frac{(\partial_i\pi)^2}{a^2} + 2\tilde{M}_1^{2\,I}\dot\pi\dot\sigma_I + (1+\tilde{e}_2^I)\dot\sigma_I^2 + \frac{(\partial_i\sigma_I)^2}{a^2}\right]$ | Eq. (10) |
| Ghost-free condition | $\epsilon_{\rm unmix} = (1+e_2)\frac{2M_2^4-\dot{H}M_{\rm Pl}^2}{\tilde{M}_1^4} - 1 > 0$ | Eq. (13) |
| Non-Abelian Maurer-Cartan | $\gamma^{-1}\partial_\mu\gamma = ix_a D_{a\mu} + it_i E_{i\mu}$ | Eq. (31) |
| Non-Abelian Lagrangian | $S_\sigma = \int d^4x\sqrt{-g}\,\mathrm{Tr}\left[F_1^2 D_\mu D^\mu + F_2^2 D^0 D^0 + F_3^3(g^{00}+1)D^0 + \ldots\right]$ | Eq. (38) |
| Soft-breaking potential | $V(\tilde\sigma) \simeq a_1\mu^4\left(1 - \frac{\tilde\sigma^2}{2M^2} + \frac{\tilde\sigma^4}{24M^4}\right)$ | Eq. (23) |
| Light field condition | $\mu^4 \ll H^2 M^2$ | Eq. (24) |
| $\zeta$-$\sigma$ conversion | $\zeta(x) = -H\pi + \frac{\partial\zeta}{\partial\sigma_I}\big|_0\sigma_I + \frac{1}{2}\frac{\partial^2\zeta}{\partial\sigma_I\partial\sigma_J}\big|_0\sigma_I\sigma_J + \ldots$ | Eq. (61) |
| Local $f_{NL}$ | $f_{\rm NL}^{\rm loc.} \sim \frac{\partial^2\zeta/\partial\sigma^2|_0}{(\partial\zeta/\partial\sigma|_0)^2}$ | Eq. (74) |
| Local $g_{NL}$ | $g_{\rm NL}^{\rm loc.} \sim \frac{\partial^3\zeta/\partial\sigma^3|_0}{(\partial\zeta/\partial\sigma|_0)^3}$ | Eq. (73) |
| Lorentz-invariant 4pt | $g_{NL} \sim 10^{10}\frac{H^4}{\tilde{\tilde{M}}^4}$ | Eq. (80) |
| $\sigma$ speed of sound | $c_s^2 \sim \frac{1}{1+\tilde{e}_2}$ | Eq. (88) |

---

## Relevance to Phonon-Exflation

The phonon-exflation framework has a rich internal structure (155,984 eigenvalues of $D_K$ at $L_{\rm max}=10$) that generically produces multiple light degrees of freedom during the exflation transit -- the GGE quasiparticle excitations are precisely the kind of additional scalar modes this paper treats. The Abelian and non-Abelian Goldstone constructions are directly relevant because the SU(3) fiber has both Abelian and non-Abelian subgroup structure, and the spectral action's symmetry breaking pattern ($G \to H$ at the fold) maps onto the coset construction of Section 3.2. The paper's finding that approximate Lorentz invariance can suppress 3-point functions while leaving 4-point functions large is relevant to the GGE relic's non-Gaussian predictions: the ordered veil (integrable, non-thermalizing) may impose exactly such symmetry constraints. The conversion mechanism (Section 4) parallels the exflation framework's need to convert GGE excitations into observable curvature perturbations through the impedance mismatch at the fold boundary.
