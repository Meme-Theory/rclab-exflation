# String Field Theory

**Author:** Michio Kaku
**Year:** 1987
**Journal:** International Journal of Modern Physics A, Vol. 2, pp. 1–178

---

## Abstract

We present a comprehensive, pedagogical review of string field theory, unifying the light-cone and covariant approaches. This article covers the foundations of canonical quantization of strings, the structure of interactions (joining-splitting amplitudes), multi-loop calculations, and the relationship to dual resonance models and conformal field theory. We discuss both open and closed string field theories, address the ghost problem in covariant gauge fixing, and outline the path to understanding 26 dimensions for bosonic strings and 10 dimensions for superstrings. The paper includes detailed examples, exercises, and proofs, establishing string field theory as a complete, unitary framework for quantum strings.

---

## Historical Context

By the mid-1980s, string theory had achieved remarkable theoretical consistency: the 26-dimensional bosonic string was solved, and the anomaly-free 10-dimensional superstring had emerged. However, the conceptual status of strings remained somewhat unclear. Were they fundamental? How did interactions actually work?

The period 1974–1987 saw rapid developments:

- **Siegel and Zwiebach** (1985–1987) developed manifestly covariant BRST quantization, introducing ghosts and the nilpotent BRST charge.
- **Witten** (1986) proposed cubic open string field theory using a novel *-product structure, later recognized as a star algebra.
- **Kaku and Lykken** developed nonpolynomial closed string field theory, addressing anomalies in closed strings.

By 1987, the field had matured to the point where a comprehensive, unified review could be written. This paper by Kaku provided that service—it became a standard reference that synthesized light-cone and covariant approaches, made the theory accessible to graduate students, and clarified the relationship between string field theory and conventional string S-matrix theory.

---

## Key Arguments and Derivations

### Canonical Quantization in Light-Cone Gauge

The light-cone coordinates are:

$$x^\pm = \frac{1}{\sqrt{2}}(x^0 \pm x^{d-1}), \quad x^i \quad (i=1,\ldots,d-2)$$

In light-cone gauge, the worldsheet Hamiltonian simplifies to:

$$H = \frac{1}{2} \int_0^\pi d\sigma \left[ \left(\frac{\pi^i(\sigma)}{T}\right)^2 + T \left(\frac{\partial x^i}{\partial \sigma}\right)^2 \right]$$

where $T = 1/(2\pi \alpha')$ is the string tension and $\pi^i$ is the conjugate momentum. The oscillator expansion:

$$x^i(\tau, \sigma) = x^i_0 + p^i \tau + \sum_{n \neq 0} \frac{1}{n} a_n^i e^{-in\tau} \cos(n\sigma)$$

yields the mass formula:

$$M^2 = \frac{1}{\alpha'} \sum_{n=1}^\infty n(a_n^{i \dagger} a_n^i + a_n^{i \dagger}_R a_n^i_R) - a_0$$

where $a_0 = 1$ for the bosonic string (the normal-ordering constant arises from the vacuum energy of the oscillators).

### The Critical Dimension

For the spectrum to be unitary (positive norm) in the light-cone gauge, physical states must satisfy:

$$L_n^\perp | \psi \rangle = 0 \quad (n \geq 1)$$

where $L_n^\perp$ is the transverse Virasoro generator. The commutator algebra of these constraints closes only if the central charge vanishes:

$$c = d - 2 - 24 a_0 = 0$$

With $a_0 = 1$, this gives:

$$d = 26$$

for the bosonic string. For superstrings (combining fermions and bosons), the condition is $d = 10$.

The reason: Lorentz invariance of the S-matrix requires all Lorentz generators $M^{\mu\nu}$ to commute with the spectrum-defining constraints. In light-cone gauge, the transverse rotations and boosts must have consistent commutation relations, which over-constrains the system unless the dimension is exactly 26 (or 10 for superstrings).

### Three-String Vertex in Light-Cone Gauge

The three-string amplitude is encoded in the vertex operator:

$$V_3 = g_c \int_0^\infty d\tau \int_0^\pi d\sigma \, \delta(x^-_1(\sigma) - x^-_2(\sigma)) \, \delta(x^-_1(\sigma) - x^-_3(\sigma))$$

where $x^-_i$ is the "$x^-$" coordinate of string $i$. The delta functions enforce the condition that the three strings meet at a single worldsheet point $(\tau, \sigma)$. The coupling $g_c$ is related to the string length and the topology of the interaction.

### Covariant BRST Quantization

In a covariant approach, one introduces the Faddeev-Popov ghosts $c, b$ with anticommutation relations:

$$\{c_m, b_n\} = \delta_{m+n, 0}$$

The BRST charge is:

$$Q_{BRST} = \sum_{n=1}^\infty (c_{-n} L_n + c_n L_{-n}) - \frac{1}{2} \sum_{m,n} (m-n) c_{-m} c_{-n} b_{m+n}$$

Physical states satisfy:

$$Q_{BRST} | \psi \rangle = 0, \quad Q_{BRST}^2 = 0$$

The nilpotency $Q_{BRST}^2 = 0$ is a crucial consistency check—it ensures that ghost contributions cancel exactly in physical amplitudes, leaving an unitary S-matrix.

### Witten's Cubic Open String Field Theory

Witten's formulation uses the *-product (Konishi operator):

$$(A * B)(x) = \int dy \int dz \, \delta_{\text{OPE}}(y - z) A(y) B(z)$$

The action is:

$$S = \frac{1}{g_s^2} \left[ \frac{1}{2} \langle \Phi | \partial_t \Phi \rangle + \frac{1}{3} \langle \Phi | \Phi * \Phi \rangle \right]$$

where $\Phi$ is the string field and $\langle \cdot | \cdot \rangle$ is the inner product. The star algebra is associative:

$$(A * B) * C = A * (B * C)$$

This cubic form is remarkably compact—all interactions are captured in one term, and the action is manifestly gauge invariant.

### Multi-Loop String Amplitudes

The loop order is organized by powers of $g_s^2$:

$$\mathcal{A} = \mathcal{A}^{(0)} + g_s^2 \mathcal{A}^{(1)} + g_s^4 \mathcal{A}^{(2)} + \ldots$$

Each loop introduces:
- A worldsheet Riemann surface of genus $g_{\text{loop}}$.
- An integral over the moduli space of surfaces: $\int d\tau_i$ where $\tau_i$ are modular parameters.
- Exponential suppression by $e^{-S}$ where $S$ is the worldsheet action.

For a genus-$g$ surface, the moduli space dimension is $3g - 3$ (for genus $g \geq 2$). The integral:

$$\int_{\mathcal{M}_g} d\mu \, |\mathcal{Z}_g(\tau, \Phi)|^2$$

runs over all conformal metrics (up to diffeomorphisms and Weyl scalings) on the surface.

### Connection to Conformal Field Theory

A profound insight: A 26-dimensional bosonic string is equivalent to a two-dimensional conformal field theory (CFT) with central charge $c = 26$. Each oscillator mode $a_n^i$ represents the $n$-th Fourier mode of a free scalar field $X^i(\sigma)$ on the worldsheet.

The correlation function:

$$\langle \mathcal{O}_1(z_1) \mathcal{O}_2(z_2) \cdots \mathcal{O}_n(z_n) \rangle_{CFT}$$

for primary operators on the sphere can be computed via the free-field representation, and when integrated over the positions $z_i$, yields the string field theory amplitudes.

---

## Key Results

1. **Unified formalism**: Light-cone and covariant approaches are equivalent; they are related by a change of gauge fixing.

2. **Dimensional requirements**: Consistency of quantization forces $d=26$ (bosonic) or $d=10$ (superstring).

3. **Finiteness and unitarity**: All loop amplitudes are finite; unitarity is manifest (no ghosts propagate in physical states).

4. **Interaction structure**: Cubic vertices in light-cone gauge correspond to Witten's *-product in covariant form.

5. **String theory as 2D CFT + geometry**: Strings can be understood as a coupling of a 2D CFT (the worldsheet) to 2D gravity (the worldsheet metric).

6. **Multi-loop structure**: Loop integrals are organized by the moduli space of Riemann surfaces; they exhibit natural cutoffs at the string scale.

---

## Impact and Legacy

This 1987 review by Kaku served as the primary pedagogical reference for string field theory for over a decade. It unified scattered results and made the subject accessible to graduate students. Key impacts:

- **Graduate education**: Students used this paper (and later the textbook version) to learn string theory systematically.
- **Research direction**: It clarified which questions in string field theory were settled and which were open.
- **Cited by**: All subsequent papers on covariant string field theory, Witten's formulation, BRST quantization, and superstring field theory cite this work.
- **Pedagogical gold standard**: Even today, aspects of this review are clearer than some modern treatments.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH (conceptual structure)**

The phonon-exflation model is structured around a similar principle: quantize an extended object (the M4 x SU(3) compact fiber) as a quantum field theory, deriving particles as excitations of the geometry.

**Key parallels**:

1. **Extended-object quantization**: Strings are quantized at every point $\sigma \in [0, \pi]$ along their extent. Similarly, phonons are quantized at every point in the SU(3) Lie group space, with eigenfunctions of the Laplacian providing the basis.

2. **Oscillator formalism**: String oscillators $a_n^i$ generate the spectrum. Phonon-exflation uses analogous creation/annihilation operators on the SU(3) representations.

3. **Dimensional fixing**: The string theory is forced to be 26-dimensional (or 10 for superstrings) by consistency. Phonon-exflation is similarly forced to M4 x SU(3) by consistency with the Dirac spectrum and spectral action.

4. **Interaction vertices**: String interactions via joining-splitting have an analogue in phonon-exflation: the noncommutative-geometry product $*$ that encodes how internal fluctuations couple.

5. **Loop finiteness**: String loops are finite due to the extended nature. Phonon-exflation loops (spectral-action loop corrections) should similarly be finite due to the discrete internal spectrum.

**Kaku's formalism provides a rigorous template** for how to structure the phonon-exflation theory—canonical quantization of an internal geometry, interaction vertices, and loop expansion.

---

## References & Further Reading

- Kaku, M. (1987). "String field theory," *Int. J. Mod. Phys. A*, 2(1), 1–178.
- Kaku, M. (1998). *Introduction to Superstrings and M-Theory* (2nd ed.). Springer.
- Siegel, W., & Zwiebach, B. (1987). "Gauge string field theory," *Nucl. Phys. B*, 282, 125–183.
- Witten, E. (1986). "Non-commutative geometry and string field theory," *Nucl. Phys. B*, 268(2), 253–294.
- Kaku, M., & Lykken, J. (1990). "The structure of non-polynomial closed string field theory," *Nucl. Phys. B*, 341(2), 249–279.
