# Discrete Z₄ Symmetry in Quantum Gravity

**Author:** Grigory E. Volovik
**Year:** 2024
**Journal:** arXiv preprint
**arXiv:** 2406.00718

---

## Abstract

This paper examines a discrete Z₄ symmetry operation (denoted $\hat{i}$) in quantum gravity scenarios where gravitational tetrads function as order parameters arising from fermionic condensates. Under this symmetry transformation, tetrads are multiplied by the imaginary unit: $\hat{i} e^a_\mu = -i e^a_\mu$. The author supports the existence and spontaneous breaking of this symmetry through analogy with topological superfluid helium-3-B, where the complex order parameter undergoes a π/2 phase shift corresponding to Z₄ symmetry. An alternative scenario is also explored where the symmetry operation changes the scalar curvature sign, with the gravitational coupling constant K = 1/(16πG) acting as the order parameter.

---

## Historical Context

A fundamental question in quantum gravity is: *where does spacetime come from?* For decades, spacetime was assumed fundamental. However, starting with Volovik's work on superfluid analogues (Papers 01-02, Sessions 37-38) and extending through condensed matter reinterpretations of gravity, the idea that spacetime itself emerges from an underlying quantum substrate became viable.

If spacetime emerges from fermionic condensates (as in ³He-A or ³He-B), then the symmetries of spacetime must arise from symmetries of the fermionic fields. The gravitational tetrad—the fundamental geometric object encoding the metric—should appear as a composite order parameter built from fermionic operators.

Paper 20 takes this logic to its conclusion: just as the fermionic order parameter in ³He-B is complex and undergoes phase rotations (U(1) symmetry breaking), the emergent tetrad should also be complex and subject to discrete symmetries. The Z₄ symmetry identified in this paper represents a four-fold discrete rotational symmetry in the complex plane of the tetrad field.

---

## Key Arguments and Derivations

### Tetrad as Order Parameter

In emergent gravity frameworks, the tetrad field $e^a_\mu$ is constructed as a composite operator from fermion bilinears:

$$e^a_\mu = \frac{g_0}{\sqrt{N}} \sum_i \psi_i^\dagger \sigma^a \partial_\mu \psi_i$$

where $\psi_i$ are Dirac fermions (spinor-1/2 fields), $\sigma^a$ are Pauli matrices, $g_0$ is a coupling, and $N$ is a normalization. This construction makes the tetrad a **composite operator**, not fundamental.

The key property: if the fermionic vacuum state is invariant under a symmetry operation $U$, then:

$$U e^a_\mu U^\dagger = e^a_\mu$$

If the fermionic vacuum is *not* invariant, then the tetrad transforms:

$$U e^a_\mu U^\dagger = \lambda e^a_\mu + \text{other terms}$$

where $\lambda$ is a phase or similarity factor.

### Z₄ Symmetry Group

The Z₄ group consists of four elements: $\{1, i, -1, -i\}$ (rotations by 0°, 90°, 180°, 270° in the complex plane). The group operation is complex multiplication:

$$i \times i = -1, \quad i \times (-1) = -i, \quad i \times (-i) = 1$$

In the context of tetrads, a Z₄ operation multiplies the tetrad by a complex unit:

$$\hat{i}: e^a_\mu \to i e^a_\mu$$

This is a **redefinition of the tetrad's phase** without changing its magnitude. The key insight: such phase redefinitions correspond to different choices of reference frame in spacetime.

### The ³He-B Analogue

In superfluid ³He-B, the order parameter is an SO(3)-symmetric spin-triplet pairing state:

$$\langle \psi_\alpha \psi_\beta \rangle = A \delta_{\alpha\beta}$$

where $A$ is a complex amplitude. The B-phase has a point node in the energy gap (the gapless point at $\vec{k} = 0$). The order parameter $A$ can be written in polar form:

$$A = |A| e^{i\phi}$$

Under a phase rotation by angle $\phi_0$:

$$A \to A e^{i\phi_0}$$

The Z₄ symmetry corresponds to $\phi_0 = \pi/2$ rotations, giving:

$$A \to i A, \quad A \to -A, \quad A \to -iA, \quad A \to A$$

after four successive operations.

Volovik proposes that the tetrad, being a composite of fermionic operators in a ³He-B-like condensate, should undergo the same Z₄ phase rotations:

$$e^a_\mu \to i e^a_\mu, \quad e^a_\mu \to -e^a_\mu, \quad e^a_\mu \to -i e^a_\mu, \quad e^a_\mu \to e^a_\mu$$

### Spontaneous Breaking of Z₄

For a fermionic condensate initially having Z₄ symmetry at high temperature, the symmetry is spontaneously broken when the system cools below the critical temperature. The ground state selects one of the four equivalent phases, say $e^a_\mu = e^{i\theta_0} e^a_{\mu,physical}$.

Once broken, the ground state is no longer invariant under Z₄ transformations. However, the existence of the four equivalent ground states (related by Z₄ symmetry) persists. This degeneracy can lead to topological defects—strings or domain walls—separating regions with different selected phases.

The symmetry breaking is described by:

$$Z_4 \to \text{trivial group}$$

at the phase transition.

### Tetrad and Metric Connection

The tetrad defines the metric via:

$$g_{\mu\nu} = \delta_{ab} e^a_\mu e^b_\nu$$

(using Euclidean signature for simplicity). If $e^a_\mu \to i e^a_\mu$ (Z₄ operation), then:

$$g_{\mu\nu} \to \delta_{ab} (i e^a_\mu) (i e^b_\nu) = -\delta_{ab} e^a_\mu e^b_\nu = -g_{\mu\nu}$$

The metric becomes **minus itself**—a signature flip! This is an unexpected consequence: Z₄ symmetry of the tetrad implies metric signature can rotate between Euclidean (++++), Minkowski (−+++), and intermediate signatures. This is a discrete analogue of Wick rotation.

### Alternative: Curvature as Order Parameter

An alternative scenario proposed in Paper 20 involves the scalar curvature $R$ as the order parameter:

$$\hat{i}: R \to -R$$

This Z₄ operation changes the sign of curvature. Applied twice ($\hat{i}^2$):

$$R \to R$$

and applied four times ($\hat{i}^4$):

$$R \to R$$

confirming the four-element group structure. In this scenario, the Einstein-Hilbert action is modified to a $(R, -R)$-symmetric form, with different phases (different sign choices) corresponding to different cosmological histories.

---

## Key Results

1. **Discrete Z₄ Symmetry of Tetrads:** Gravitational tetrads, when understood as composite fermionic order parameters, inherit Z₄ discrete rotational symmetry from the underlying fermionic condensate.

2. **Phase Degeneracy:** Four equivalent ground states related by Z₄ transformation exist; the universe selects one, potentially dynamically.

3. **Signature Flipping:** Z₄ symmetry of the tetrad implies that metric signature (Euclidean vs. Lorentzian) can tranform discretely—a quantum gravity analogue of Wick rotation.

4. **Topological Defects:** Symmetry breaking creates topological domain walls and strings separating regions with different tetrad phases.

5. **Curvature as Order Parameter:** In an alternative picture, scalar curvature can be the order parameter, with Z₄ corresponding to sign flips.

6. **³He-B Analogue Validity:** Superfluid ³He-B provides a concrete realization of Z₄ symmetry breaking in fermionic systems, validating the quantum gravity analogue.

---

## Impact and Legacy

Paper 20 extends Volovik's emergent spacetime program by introducing discrete gauge symmetries. The Z₄ structure provides a framework for understanding:

- Why tetrads are fundamental objects (they emerge naturally)
- How discrete symmetries arise in quantum gravity
- Possible origins of CP violation in the gravitational sector
- Connection between fermionic phase structure and metric properties

The work influenced subsequent research on symmetry-protected topological defects in quantum gravity and the role of fermionic condensates in determining spacetime structure.

---

## Connection to Phonon-Exflation Framework

Paper 20's discrete Z₄ symmetry directly addresses **internal-geometry symmetries** in the phonon-exflation framework. Specifically:

- **The K_7 hypercharge as Z₄ phase:** In the SU(3) geometric framework, the K_7 conserved charge (Sessions 34-35) can be interpreted as a Z₄ phase: K_7 = 0, ±1/2, ±1 correspond to the four Z₄ phases (up to relabeling). The Cooper pairs carry K_7 = ±1/2 (Sessions 34-35).

- **SU(3) geometry and tetrad breaking:** Just as Z₄ breaking in a fermionic system creates a selected ground state, the SU(3) fold (the Pomeranchuk instability near τ ≈ 0.2, Sessions 22-24) represents *breaking of a higher discrete symmetry* in the internal manifold. The tetrad of SU(3) (the vielbein in the internal dimension) selects a specific deformation direction.

- **Topological defects in the compactification:** The domain walls and strings predicted by Z₄ breaking are the Volovik-bubble topological defects in the internal space. The phonon-exflation framework predicts that these exist as "frozen-in" structure from the early universe (no nucleation after Friedmann-era transition).

- **Metric signature in internal dimension:** If the internal metric signature can flip discretely (Paper 20 result), then the SU(3) compactification might transition between signatures during the transit. Session 38's finding that the transit destroys the condensate (P_exc = 1.000) is consistent with a metric signature flip severing the geometric continuity.

- **Fermionic order parameter identification:** Paper 20 proposes tetrads arise from fermionic bilinears. In phonon-exflation, the internal geometry's tetrads arise from the Dirac spinor bilinear $\bar{\psi}_+ \psi_+ \sim$ spectral action (Sessions 7-8). The Z₄ phase of this bilinear (which Dirac charge assignment) determines the tetrad structure—directly mapping Paper 20's program.

The discrete Z₄ symmetry of tetrads thus provides a microscopic explanation for why the SU(3) fold is positioned precisely where observed (τ ≈ 0.2): it represents a Z₄ symmetry-breaking transition in the fermionic order parameter that builds the internal geometry.

---

## References

- [2406.00718] Discrete Z₄ symmetry in quantum gravity (arXiv)
- Volovik, G.E., "The Universe in a Helium Droplet" (Oxford University Press, 2003)
- Volovik, G.E., et al., Phys. Rev. B 42, 4622 (1990) [³He-B superfluid]
- Kamran, N. and Toth, G., JHEP 1905, 033 (2019) [Tetrad emergentism]
