# Field Theory of Relativistic Strings. I. Trees

**Authors:** Michio Kaku, Keiji Kikkawa
**Year:** 1974
**Journal:** Physical Review D, Vol. 10, pp. 1110–1133

---

## Abstract

We present a complete field theory formulation of relativistic strings in the light-cone gauge. Unlike traditional quantum field theory where quantization occurs at spacetime points, our approach performs canonical quantization along an extended set of multilocal points on a string. The theory naturally accommodates an infinite set of linearly rising Regge trajectories and derives the Veneziano amplitude as the sum of s- and t-channel pole contributions, demonstrating the equivalence between light-cone string dynamics and dual resonance model amplitudes. We introduce three-string interactions, four-string vertices, and resolve multiple-counting issues through systematic graph-theoretical analysis. In the zero-slope limit, the formalism yields Yang-Mills theory.

---

## Historical Context

Before 1974, string theory existed primarily as an S-matrix theory (dual resonance models) without a field-theoretic description. The standard approach treated strings as abstract external states summed over Feynman diagrams, but the underlying field equations and Lagrangian were unknown. Kaku and Kikkawa's breakthrough was recognizing that strings could be quantized as fields living not at points but along one-dimensional extended objects.

This resolved a fundamental conceptual gap: How does an infinite tower of mass levels (Regge trajectory) arise naturally in quantum field theory? The answer was that the infinite number of oscillator modes of a vibrating string generates all the mass levels, and canonical commutation relations among these modes encode the full dynamics.

The light-cone gauge simplification—fixing the coordinate $x^+ = p^+ \tau$ (where $\tau$ is worldsheet parameter, $p^+$ is light-cone momentum)—eliminated ghosts and reduced the Lorentz algebra to kinematical subgroups. This gauge choice, inspired by Weinberg's light-cone QED calculations, proved ideal for constructing a manifestly unitary field theory.

---

## Key Arguments and Derivations

### The Light-Cone String Coordinates

In light-cone gauge, spacetime coordinates split into light-cone pairs:

$$x^\pm = \frac{1}{\sqrt{2}}(x^0 \pm x^{d-1}), \quad x^i \quad (i=1,\ldots,d-2)$$

The worldsheet is parametrized by $(\tau, \sigma)$ (time and space), and the string field is a multilocal functional:

$$\Phi[\mathbf{x}(\sigma)]$$

where $\mathbf{x}(\sigma) = \{x^i(\sigma)\}$ denotes all transverse coordinates along the string.

### Canonical Quantization

The canonical momentum density is:

$$\pi^i(\sigma) = \frac{\partial \mathcal{L}}{\partial \dot{x}^i(\sigma)}$$

Commutation relations are imposed at equal times $\tau_1 = \tau_2$:

$$[x^i(\sigma_1), \pi^j(\sigma_2)] = i\hbar \delta^{ij} \delta(\sigma_1 - \sigma_2)$$

The Fourier expansion in oscillator modes:

$$x^i(\sigma) = x^i_0 + p^i \sigma + \sum_{n \neq 0} \frac{1}{n} a_n^i e^{-in\sigma}$$

introduces ladder operators $a_n^i, a_n^{i \dagger}$ with canonical commutators:

$$[a_m^i, a_n^{j \dagger}] = \delta^{ij} \delta_{m,n}$$

### String Interactions: Three-String Vertex

A key insight is the joining-splitting picture: three strings can interact by joining at a point. The three-string amplitude (without ghosts in light-cone gauge):

$$V_3 = \int d\tau_1 d\tau_2 d\sigma_1 d\sigma_2 d\sigma_3 \, \text{(contact term interaction)}$$

encodes the coupling strength $g_s$ and kinematical structure. The diagram:

```
   |String 1|
   |        |
   |===*===|---String 2
   |        |
   |String 3|
```

Here the vertex [*] is located at worldsheet coordinates $(\tau_*, \sigma_*)$.

### Four-String Interaction and Yang-Mills Limit

The four-string amplitude is:

$$\mathcal{A}_4 = g_s^2 \int d\Phi_4 \, \mathcal{M}(\Phi_4)$$

where the measure $d\Phi_4$ accounts for the phase space of four intersecting strings. In the zero-slope limit $\alpha' \to 0$ (while holding $g_s$ fixed), the kinetic poles from three-string channels vanish, leaving only the contact interaction:

$$\mathcal{A}_4^{YM} = \mathcal{Tr}(T^a T^b T^c T^d) k_1 \cdot k_2 \cdots$$

This is precisely the color-ordered Yang-Mills amplitude. The gauge group arises from the ordering structure of string joining.

### Veneziano Amplitude Recovery

For four-point scattering of open strings, summing tree diagrams in the s-channel and t-channel:

$$\mathcal{A}_{s}(s,t) + \mathcal{A}_{t}(s,t) = B(s, t)$$

where $B(s,t) = \frac{\Gamma(-\alpha s)\Gamma(-\alpha t)}{\Gamma(-\alpha s - \alpha t)}$ is the Veneziano beta-function amplitude. The dual-channel sum automatically dualizes s ↔ t, confirming that the Regge trajectory description and the string field tree amplitudes are equivalent.

### Multiple-Counting and Combinatorics

A subtle but critical issue: when summing Feynman diagrams over all topologies of string splitting and joining, one must avoid overcounting. Each diagram corresponds to a specific ordered sequence of join/split events. The authors resolve this through a graph-coloring argument on the worldsheet, assigning each segment between splitting events a unique color, with no two adjacent segments sharing the same color.

The number of distinct tree graphs grows as:

$$N_{\text{graphs}}(n) \sim \left(\frac{2n}{e}\right)^n$$

asymptotically for $n$ external strings.

---

## Key Results

1. **Equivalence of field and amplitude pictures**: Tree-level string field theory amplitudes exactly reproduce the Veneziano model and dual resonance amplitudes.

2. **Light-cone quantization is ghost-free**: The light-cone gauge eliminates negative-norm states. The Hilbert space has a positive-definite inner product.

3. **Infinite Regge trajectories emerge naturally**: Each oscillator excitation $n$ of the string adds to the invariant mass squared by $\approx \frac{2n}{\alpha'}$, generating the linear trajectory.

4. **Yang-Mills in the zero-slope limit**: When $\alpha' \to 0$, string field theory reduces to Yang-Mills, proving that Yang-Mills is an effective theory of massless string excitations.

5. **Lorentz covariance**: Despite fixing light-cone gauge, the theory is manifestly Lorentz covariant off-shell (by explicit verification of the transformation properties of all fields).

6. **Four-string vertex is necessary**: Unlike the three-string picture in some early formulations, a four-string contact term is essential to avoid spurious poles in certain kinematic limits.

---

## Impact and Legacy

This 1974 paper launched the field of string field theory. Within a decade, it inspired:

- **Siegel and Zwiebach's BRST quantization** (1985-1990): A covariant formulation including ghosts.
- **Witten's cubic open string field theory** (1986): An elegant reformulation using a Konishi operator (the *-product).
- **Berkovits' superstring extensions** (1995+): Covariant BRST string field theory for superstrings.
- **Modern gauge-fixed theories**: Endpoint gauge, midpoint gauge, and geometric string field theory all trace their conceptual origin to Kaku-Kikkawa.

The paper is cited 500+ times in the literature and remains the standard reference for light-cone string field theory. It demonstrated that strings could be treated as quantum fields—a paradigm shift that unified particle physics and string dynamics.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: MODERATE to HIGH**

The phonon-exflation model treats particles as phononic excitations of an internal M4 x SU(3) compact space. Kaku-Kikkawa string field theory provides a rigorous example of how extended objects (strings) with internal structure can be second-quantized into a field theory of massless and massive quanta.

**Key parallels**:

1. **Multi-local quantization**: Just as Kaku-Kikkawa quantize at positions $\sigma$ along the string, the phonon-exflation framework quantizes in the internal SU(3) coordinate space. The density-of-states in Fourier space on the torus $T^3$ (or SU(3) quotient) plays the role of the transverse oscillators.

2. **Regge trajectory structure**: The infinite mass-gap structure in strings (one oscillator per integer $n$) mirrors the Dirac spectrum structure in the finite-geometry approximation, where spectral gaps encode internal excitations.

3. **Zero-slope Yang-Mills limit**: The emergence of Yang-Mills from strings in the $\alpha' \to 0$ limit mirrors the emergence of the Standard Model gauge structure from the Dirac spectrum near criticality (small $\tau$).

4. **Unification via geometry**: Strings unify gravity and gauge forces via compactification and higher dimensions. Similarly, phonon-exflation proposes that all forces arise from the geometry and curvature of the M4 x SU(3) fiber, with particles being quantized fluctuations of the metric and connection.

**Gap**: Kaku-Kikkawa assumes spacetime as fundamental. Phonon-exflation reverses this: spacetime metrics emerge from pairing instabilities in the internal fiber. Nevertheless, the mathematical machinery—canonical quantization, field operators, Fock spaces—is directly applicable.

---

## References & Further Reading

- Kaku, M., & Kikkawa, K. (1974a). "Field theory of relativistic strings. I. Trees," *Phys. Rev. D*, 10(4), 1110–1133.
- Kaku, M., & Kikkawa, K. (1974b). "Field theory of relativistic strings. II. Loops and Pomerons," *Phys. Rev. D*, 10(12), 3814–3828.
- Siegel, W., & Zwiebach, B. (1987). "Gauge string field theory," *Nucl. Phys. B*, 282, 125–183.
- Witten, E. (1986). "Non-commutative geometry and string field theory," *Nucl. Phys. B*, 268(2), 253–294.
