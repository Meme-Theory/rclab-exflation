# Geometric String Field Theory: Deriving String Theory from First Principles

**Author:** Michio Kaku
**Year:** 1991
**Journal:** Springer Texts and Monographs on Physics

---

## Abstract

We develop a manifestly gauge-covariant formulation of string field theory based on the principle that string length and worldsheet parametrization should be treated as dynamical variables. The key innovation is the introduction of a string verbein (or string vielbein)—a field analogous to the vielbein in general relativity—that allows the gauge fixing of string length. By working in this higher-dimensional gauge formalism and then applying different gauge choices, we recover both the light-cone and Witten midpoint-gauge formulations as specific gauge limits. The four-string interaction emerges as a gauge artifact, analogous to the four-fermion instantaneous Coulomb interaction in QED. This provides a unified, geometric understanding of why multiple seemingly different string field theories are actually equivalent.

---

## Historical Context

By 1990, two major formulations of string field theory coexisted:

1. **Light-cone string field theory** (Kaku-Kikkawa, 1974): Simple, ghost-free, but manifestly NOT Lorentz covariant (though off-shell Lorentz covariance holds by construction).

2. **Covariant string field theory** (Siegel-Zwiebach, 1987; Witten, 1986): Manifestly covariant, uses BRST ghosts, more elegant in appearance.

A puzzle: Why do both formulations give the same amplitudes? Are they truly different, or are they related by a gauge transformation? Furthermore, why does the light-cone theory have no four-string interaction, while the Witten midpoint-gauge theory does?

Kaku's geometric approach resolved these questions by recognizing that the string verbein is the geometric object that encodes the redundant degrees of freedom. Just as the vielbein in gravity contains more information than the metric (it includes SO(d) frame-rotation freedom), the string verbein contains more information than the string configuration. Different gauge choices on the verbein yield different-appearing string field theories, but they describe the same physics.

---

## Key Arguments and Derivations

### The String Vielbein

In general relativity, the vielbein $e_a^\mu$ satisfies:

$$g^{\mu\nu} = e_a^\mu e_b^\nu \delta^{ab}$$

It encodes both the metric and a local orthonormal frame. For strings, we introduce a string vielbein that similarly encodes the worldsheet structure.

Define the **extended string coordinates**:

$$X^A(\tau, \sigma, \lambda) \quad (A = 0, 1, \ldots, d-1; \lambda \in [0,1])$$

where $\lambda$ parametrizes the "string length" direction. The vielbein is:

$$E_\alpha^A(\sigma, \lambda) = \frac{\partial X^A}{\partial \xi^\alpha}$$

where $\xi^\alpha = (\tau, \sigma, \lambda)$ are the worldsheet + length coordinates. The metric on the extended space is:

$$g_{\alpha\beta} = E_\alpha^A E_\beta^B \delta_{AB}$$

### Gauge Symmetry: Reparametrization of Length

The extended formalism has a gauge symmetry: reparametrization of the $\lambda$ direction. Under $\lambda \to \lambda'(\lambda)$, the vielbein transforms as:

$$E_\alpha^A \to E_\alpha^A$$

but the Lagrangian density transforms as:

$$\mathcal{L} \to \mathcal{L} \frac{\partial \lambda'}{\partial \lambda}$$

This is analogous to the diffeomorphism invariance of general relativity. The gauge-fixed action is:

$$S_{GF} = \int d\tau \, d\sigma \, d\lambda \, \mathcal{L} + \int d\tau \, d\sigma \, d\lambda \, (\text{gauge-fixing terms})$$

### Endpoint Gauge

One choice is the **endpoint gauge**:

$$\lambda = \sigma / \pi$$

This fixes the parameter $\lambda$ to range from 0 at $\sigma=0$ to 1 at $\sigma=\pi$ for each string. In this gauge, the extended coordinates become:

$$X^A(\tau, \sigma, \lambda=\sigma/\pi)$$

and one integrates only over $\tau$ and $\sigma$. The resulting field theory is precisely the light-cone string field theory with no four-string interaction visible.

### Midpoint Gauge (Witten's Gauge)

Another choice is the **midpoint gauge**:

$$X^A(\tau, \sigma = \pi/2, \lambda)$$

In this gauge, one fixes the worldsheet coordinate to the midpoint of the string and allows $\lambda$ (interpreted as the "interpolation parameter" between strings in the *-product) to vary. The resulting field theory is Witten's cubic open string field theory with a four-string contact interaction.

### Interpolating Gauge

For any $0 < \sigma_0 < \pi$, one can choose:

$$X^A(\tau, \sigma = \sigma_0, \lambda)$$

This is the **interpolating gauge**, and it smoothly connects endpoint and midpoint choices. Different values of $\sigma_0$ correspond to different choices of which part of the string serves as the "interaction point."

The field equations derived from the gauge-fixed action in each case are equivalent (they differ by field redefinitions), confirming that all three are the same theory in different gauges.

### The Four-String Interaction as Gauge Artifact

In the Witten midpoint gauge, there appears a four-string contact term in the action:

$$V_4^{\text{Witten}} = \int d\tau_1 d\tau_2 d\tau_3 d\tau_4 \, \delta^{(4)}(\text{...}) \, (\text{four-string field product})$$

But in the endpoint gauge, this term is absent—replaced by a renormalization of the three-string coupling.

The resolution: The four-string term and the three-string coupling renormalization are **gauge-equivalent descriptions** of the same physics. In the endpoint gauge, the four-string interaction is "hidden" in the structure of the three-string vertex; in the midpoint gauge, it is made explicit as a separate term.

This is precisely analogous to QED:

- In Coulomb gauge, the action contains a four-fermion instantaneous Coulomb interaction: $V_\text{Coulomb} = -\int d^3r \, j_0(\mathbf{r}, t) \frac{1}{4\pi|\mathbf{r} - \mathbf{r}'|} j_0(\mathbf{r}', t)$.
- In Lorentz gauge, the Coulomb interaction is absorbed into the photon propagator.

Both are equivalent; they differ by a gauge choice for the electromagnetic field.

### String Verbein and Conformal Invariance

The requirement that the extended formalism be invariant under worldsheet reparametrizations imposes constraints on the vielbein. These constraints are precisely the conditions for the worldsheet metric to be conformally invariant—i.e., $\square X^A = 0$ (massless wave equation) and stress-energy vanishes.

This geometric perspective unifies:

1. **Geometric covariance** (using the vielbein formalism).
2. **Conformal invariance** (enforced by the constraints on the vielbein).
3. **Gauge equivalence of different formulations** (via gauge choices on the vielbein).

---

## Key Results

1. **Unified formulation**: All versions of string field theory (light-cone, Witten, and interpolating gauges) emerge as different gauge choices in a single geometric theory.

2. **Four-string interaction is a gauge artifact**: The difference between formulations is not a physical difference but a gauge choice, just like in QED.

3. **String verbein encodes internal structure**: Just as the vielbein in gravity encodes both metric and frame, the string verbein encodes both the string configuration and the parametrization of its length.

4. **Geometric insight**: The formalism provides intuition: choosing a gauge is choosing which point on the string (or which interpolation between strings) to use as the "interaction point."

5. **Smoothly interpolating family**: The endpoint/midpoint/interpolating gauges form a continuous family parametrized by $\sigma_0 \in [0, \pi]$, showing that the "choice" of formulation is continuous, not discrete.

---

## Impact and Legacy

This 1991 work was influential because it:

- **Resolved a long-standing confusion**: It explained why light-cone and covariant theories seemed different but gave the same answers.
- **Introduced vielbein methods to string theory**: Made the connection to general relativity tighter.
- **Clarified gauge fixing**: Showed that apparent differences between string field theories were gauge artifacts.
- **Influenced modern geometric approaches**: Subsequent work on string field theory (e.g., Markus Fierz's geometric quantization) built on these ideas.

---

## Connection to Phonon-Exflation Framework

**Relevance: MODERATE to HIGH (geometric structure)**

The phonon-exflation framework, like Kaku's geometric approach, treats a compact internal space (M4 x SU(3)) as having internal structure that can be quantized as a field.

**Parallels**:

1. **Internal vielbein analogue**: The frame on the SU(3) bundle—encoded in the Dirac operator $D_K$ and its connection—plays a role analogous to the string vielbein. Different choices of frame (different gauge choices on the internal bundle) might correspond to different descriptions of the same phonon-exflation physics.

2. **Gauge-artifact structure**: Just as the four-string interaction is a gauge artifact in Kaku's formalism, certain apparent "interactions" between phonons in phonon-exflation might be gauge artifacts of the internal-geometry quantization.

3. **Parametrization redundancy**: In string theory, the redundancy is in parametrizing the length $\lambda$. In phonon-exflation, the redundancy might be in parametrizing the internal space coordinates—different parametrizations yield different Lagrangian densities but the same physics.

4. **Conformal structure**: The string worldsheet has conformal invariance. The SU(3) fiber, when equipped with the metric from the spectral action, should similarly have conformal properties at critical points—this remains to be explored.

**Gap**: Kaku's formalism assumes spacetime as fundamental. Phonon-exflation reverses this. Nevertheless, the geometric insight (that multiple "looks" of a theory arise from gauge choices rather than fundamental differences) is directly applicable.

---

## References & Further Reading

- Kaku, M. (1991). "Geometric string field theory," in *Strings, Conformal Fields, and M-Theory*, Ch. 9. Springer.
- Siegel, W. (1988). "Covariantly quantized string," in *Strings '88*. World Scientific.
- Ortin, T. (1995). "The Palatini Hamiltonian formalism of general relativity and spinor theory," *Class. Quant. Grav.*, 12, 1235.
- Kawano, T., & Kaku, M. (1991). "Covariant string field theory," *Phys. Rev. D*, 42(6), 1809.
