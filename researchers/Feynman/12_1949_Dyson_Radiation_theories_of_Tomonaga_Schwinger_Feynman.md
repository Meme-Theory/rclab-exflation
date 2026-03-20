# The Radiation Theories of Tomonaga, Schwinger, and Feynman

**Author:** Freeman J. Dyson
**Year:** 1949
**Journal:** *Physical Review*, 75(3), 486--502

---

## Abstract

Dyson proves the mathematical equivalence of the three independently developed approaches to quantum electrodynamics: Tomonaga's covariant perturbation theory based on the spacelike surface formalism, Schwinger's systematic operator-based renormalization program using the interaction representation, and Feynman's spacetime diagrammatic method based on the propagator formalism. By showing that all three yield identical S-matrix elements to every order of perturbation theory, Dyson establishes that the apparent differences are matters of computational technique rather than physical content. Beyond the equivalence proof, Dyson provides a systematic procedure for extracting finite, renormalized predictions from the perturbation series to all orders, introduces the concept of overlapping divergences and their treatment, and establishes the power-counting criteria for renormalizability. The paper is a masterpiece of mathematical physics that unified the field, resolved lingering doubts about the consistency of QED, and established the framework for perturbative quantum field theory that remains in use today.

---

## Historical Context

### The Three Methods

By late 1948, three apparently different methods for computing QED predictions had been developed:

**Tomonaga** (1943-46): Working in wartime Japan, Tomonaga generalized Dirac's many-time formalism to a covariant theory. The state vector depends on an arbitrary spacelike surface $\sigma$, and the Tomonaga-Schwinger equation governs its evolution:

$$i\hbar c \frac{\delta|\Phi[\sigma]\rangle}{\delta\sigma(x)} = \mathcal{H}_{\text{int}}(x)|\Phi[\sigma]\rangle$$

Tomonaga's students (Koba, Tomonaga, Kanesawa) applied this to compute radiative corrections, independently discovering the need for mass and charge renormalization.

**Schwinger** (1948): Working at Harvard, Schwinger developed a comprehensive operator-based approach using the interaction representation, proper-time methods, and systematic renormalization. His calculations were rigorous but extraordinarily laborious -- a single radiative correction could fill dozens of pages.

**Feynman** (1948-49): Working at Cornell, Feynman developed the propagator/diagrammatic approach. His calculations were intuitive and efficient but lacked a systematic derivation from quantum field theory principles.

### The Need for Unification

The coexistence of three methods created confusion. Were they really equivalent? Did they give the same answers to all orders? Were there hidden inconsistencies? Were the renormalization subtractions legitimate? These questions were particularly pressing because Feynman's approach, while producing correct answers, was derived from heuristic arguments (the path integral, the backward-in-time positron) that many physicists found unconvincing.

### Dyson's Unique Position

Freeman Dyson, a young British mathematician who had studied with both Schwinger (at Harvard) and Feynman (at Cornell), was ideally positioned to bridge the gap. His background in mathematics (he had worked with Hardy and Besicovitch at Cambridge) gave him the technical tools to handle the formal manipulations, while his exposure to both approaches gave him the physical insight to see the connections.

---

## Key Arguments and Derivations

### 1. The Interaction Representation and the S-Matrix

Dyson begins by establishing a common framework. In the interaction representation, the S-matrix is:

$$S = T\exp\left(-i\int_{-\infty}^{\infty} H_I(t) \, dt\right)$$

where $H_I(t) = \int \mathcal{H}_I(\mathbf{x}, t) \, d^3\mathbf{x}$ is the interaction Hamiltonian in the interaction picture, and $T$ is the time-ordering operator.

For QED, $\mathcal{H}_I(x) = -e:\bar{\psi}(x)\gamma^\mu\psi(x):A_\mu(x) + \text{counterterms}$, where the normal ordering $:\cdot:$ removes the infinite self-contractions.

Expanding the time-ordered exponential:

$$S = \sum_{n=0}^{\infty} \frac{(-i)^n}{n!}\int d^4x_1 \cdots d^4x_n \, T[\mathcal{H}_I(x_1)\cdots\mathcal{H}_I(x_n)]$$

### 2. From Operators to Propagators: The Equivalence

Dyson's central achievement is showing that the time-ordered products of field operators, when evaluated using Wick's theorem, produce exactly the Feynman propagators and vertex factors.

**Wick's theorem** (which Dyson essentially derives, though Wick published the complete version in 1950):

$$T[\phi(x_1)\phi(x_2)\cdots\phi(x_n)] = :\phi(x_1)\phi(x_2)\cdots\phi(x_n): + \text{all contractions}$$

where a contraction of two fields is:

$$\overline{\phi(x)\phi(y)} \equiv T[\phi(x)\phi(y)] - :\phi(x)\phi(y): = \begin{cases} iS_F(x-y) & \text{(electron)} \\ iD_F(x-y) & \text{(photon)} \end{cases}$$

The key identification:
- Each electron contraction $\overline{\psi(x)\bar{\psi}(y)} = iS_F(x - y)$ corresponds to a Feynman electron propagator (internal line)
- Each photon contraction $\overline{A_\mu(x)A_\nu(y)} = ig_{\mu\nu}D_F(x - y)$ corresponds to a Feynman photon propagator
- Each uncontracted $\psi$ or $\bar{\psi}$ corresponds to an external electron line
- Each uncontracted $A_\mu$ corresponds to an external photon line
- Each vertex where three fields meet (two fermion, one photon) contributes $-ie\gamma^\mu$

This is precisely the content of the Feynman rules, derived here from the operator formalism of Tomonaga and Schwinger.

### 3. The Feynman Graph Expansion

Dyson introduces a systematic graphical notation for the terms in the perturbation expansion. Each term corresponds to a graph (Feynman diagram) with:
- Vertices (interaction points) at the spacetime points $x_1, \ldots, x_n$
- Internal lines (propagators) connecting contracted field pairs
- External lines (wave functions) for uncontracted fields

The $n$-th order contribution to the S-matrix is:

$$S^{(n)} = \frac{(-ie)^n}{n!}\int d^4x_1 \cdots d^4x_n \sum_{\text{contractions}} (\text{propagators}) \times (\text{vertex factors}) \times (\text{external wave functions})$$

The sum over contractions is the sum over all topologically distinct Feynman diagrams. The combinatorial factor $1/n!$ from the exponential expansion is partially cancelled by the $n!$ ways of assigning vertices to spacetime points, leaving a symmetry factor specific to each diagram.

### 4. Connected and Disconnected Diagrams

Dyson proves the linked-cluster theorem: the S-matrix exponentiates in terms of connected diagrams:

$$S = \exp\left(\sum_{\text{connected}} iM_c\right)$$

Equivalently, the vacuum-to-vacuum amplitude factorizes:

$$\langle 0 | S | 0 \rangle = \exp\left(\sum_{\text{vacuum bubbles}} i\Delta E \cdot T\right)$$

and physical scattering amplitudes involve only connected diagrams with the vacuum-bubble factor divided out. This is crucial for the renormalization program: vacuum energy divergences can be ignored (they cancel in all physical observables).

### 5. Renormalization to All Orders

Dyson's most important result beyond the equivalence proof is the demonstration that QED can be renormalized to all orders of perturbation theory. His argument proceeds in several steps:

**Step 1: Classification of divergences.** A Feynman diagram with $E_e$ external electron lines, $E_\gamma$ external photon lines, $L$ loops, and $V$ vertices has a superficial degree of divergence:

$$D = 4L - I_e - 2I_\gamma = 4 - \frac{3}{2}E_e - E_\gamma$$

where $I_e$ and $I_\gamma$ are the numbers of internal electron and photon lines. This depends only on the external lines, not on the internal structure. The divergent diagrams have:
- $D = 2$: electron self-energy ($E_e = 2, E_\gamma = 0$)
- $D = 0$: vacuum polarization ($E_e = 0, E_\gamma = 2$)
- $D = 0$: vertex correction ($E_e = 2, E_\gamma = 1$)

No other configurations have $D \geq 0$. This means QED has only three types of primitive divergences.

**Step 2: Subtractive renormalization.** Each primitive divergence is absorbed into a redefinition of a physical parameter:
- Electron self-energy $\to$ mass renormalization $\delta m$ and wave-function renormalization $Z_2$
- Vacuum polarization $\to$ charge renormalization $Z_3$
- Vertex correction $\to$ vertex renormalization $Z_1$ (but $Z_1 = Z_2$ by the Ward identity)

**Step 3: Overlapping divergences.** At higher orders, diagrams contain multiple divergent subdiagrams that share internal lines -- "overlapping divergences." Dyson provides a procedure (later made fully rigorous by Bogoliubov and Parasiuk, 1957, and Hepp, 1966) for subtracting these nested and overlapping divergences consistently.

**Step 4: Finiteness of renormalized amplitudes.** After performing all subtractions, the renormalized amplitudes are finite in the limit where the regularization is removed. This holds to every order of perturbation theory.

### 6. The Ward Identity

Dyson provides a clear derivation of the Ward identity, which is the crucial consistency condition ensuring that the renormalization of the vertex and the electron propagator are related:

$$q_\mu \Gamma^\mu(p + q, p) = S_F^{-1}(p + q) - S_F^{-1}(p)$$

In the limit $q \to 0$:

$$\Gamma^\mu(p, p) = \frac{\partial S_F^{-1}(p)}{\partial p_\mu}$$

This identity, a consequence of gauge invariance ($U(1)$ charge conservation), ensures $Z_1 = Z_2$ and hence that the physical electric charge is renormalized only by vacuum polarization ($Z_3$).

### 7. The Dyson Series and Unitarity

Dyson shows that the perturbation series is consistent with unitarity ($S^\dagger S = I$) order by order. This requires:
- The optical theorem: $\text{Im}(M_{ii}) = \frac{1}{2}\sum_f |M_{fi}|^2 \cdot \text{(phase space)}$
- The Cutkosky rules: the imaginary part of a Feynman diagram is obtained by cutting internal lines (putting them on shell)
- Proper treatment of the $i\epsilon$ prescription in all propagators

---

## Physical Interpretation

### Unity of QED

Dyson's proof showed that Tomonaga, Schwinger, and Feynman had discovered the same theory expressed in different mathematical languages. This was immensely reassuring: the renormalization procedure was not an artifact of a particular computational scheme but a robust feature of the theory itself.

The three approaches have complementary strengths:
- **Tomonaga:** Manifestly covariant, closest to the fundamental axioms of QFT
- **Schwinger:** Most powerful for deriving general results (Ward identity, effective action, anomalies)
- **Feynman:** Most efficient for computing specific scattering amplitudes

### Perturbative QFT as a Framework

Dyson established perturbative quantum field theory as a general framework, not just a set of ad hoc tricks for QED. The procedure -- write down the Lagrangian, derive the Feynman rules, compute diagrams, renormalize -- applies to any local quantum field theory. This framework was subsequently applied to:
- Meson theories (Yukawa coupling)
- Weak interactions (Fermi theory, then electroweak theory)
- Non-Abelian gauge theories (Yang-Mills, QCD)
- The Standard Model as a whole

### The Divergence of the Perturbation Series

In a remarkable follow-up paper (1952), Dyson argued that the QED perturbation series is likely divergent (asymptotic rather than convergent). His argument: if the series converged for $e^2 > 0$, it would converge for $e^2 < 0$ (by analytic continuation). But QED with $e^2 < 0$ (like charges attract) is unstable -- the vacuum would decay by producing particle-antiparticle pairs without limit. Therefore, the series must diverge.

This does not invalidate the perturbative approach: an asymptotic series can provide excellent approximations to the true answer when truncated at the optimal order ($n_{\text{opt}} \sim 1/\alpha \approx 137$ for QED), far beyond current computational capabilities.

---

## Impact and Legacy

### The Standard Model

Dyson's framework is the template for the entire Standard Model. The Glashow-Weinberg-Salam electroweak theory, QCD, and the Higgs mechanism are all formulated, computed, and tested using the same perturbative QFT methods that Dyson established.

### Renormalizability as a Principle

Dyson's power-counting classification of divergences became the criterion for "good" quantum field theories. For decades, renormalizability was regarded as a necessary condition for a fundamental theory. This criterion guided the construction of the Standard Model: the requirement that the electroweak theory be renormalizable (despite the massive gauge bosons) was a key motivation for the Higgs mechanism.

### The BPHZ Theorem

Dyson's treatment of overlapping divergences was made fully rigorous by Bogoliubov and Parasiuk (1957), Hepp (1966), and Zimmermann (1969). The BPHZ theorem states that the renormalized perturbation series of a renormalizable QFT is finite to all orders, providing a complete mathematical proof of what Dyson had outlined.

### 't Hooft and Veltman: Non-Abelian Theories

The extension of Dyson's framework to non-Abelian gauge theories required two additional ingredients: the Faddeev-Popov ghosts (to maintain unitarity in loops) and dimensional regularization (to maintain gauge invariance while regulating divergences). 't Hooft's proof that spontaneously broken Yang-Mills theories are renormalizable (1971) -- following Dyson's template -- was the theoretical breakthrough that made the Standard Model viable.

---

## Connections to Modern Physics

1. **Precision QED tests:** The perturbative framework Dyson established has been pushed to extraordinary precision. The electron anomalous magnetic moment is computed to $O(\alpha^5)$ (five-loop level), involving 12672 Feynman diagrams, with agreement to 12 significant figures.

2. **Lattice QFT:** The lattice provides a non-perturbative regularization that avoids the divergences entirely (at the cost of discretizing spacetime). Lattice calculations confirm the perturbative predictions in regimes where both are applicable, validating Dyson's renormalization program non-perturbatively.

3. **Effective field theories:** The modern perspective (Weinberg 1979, Wilson-Polchinski) reinterprets Dyson's renormalizability criterion: a non-renormalizable theory is not "bad" but simply an effective theory valid below some cutoff scale. The non-renormalizable operators are suppressed by powers of $E/\Lambda$, where $\Lambda$ is the cutoff. This encompasses gravity, chiral perturbation theory, and the Standard Model itself.

4. **Asymptotic series and resurgence:** Dyson's observation about the divergence of the perturbation series has led to the modern theory of resurgence, which seeks to extract non-perturbative information (instantons, renormalons) from the large-order behavior of the perturbation series. The transseries approach combines perturbative and non-perturbative contributions into a complete (resurgent) asymptotic expansion.

5. **Amplitude methods:** Modern amplitude methods (on-shell recursion, unitarity cuts, the amplituhedron) can be seen as efficient implementations of Dyson's S-matrix program, computing the same perturbative amplitudes with dramatically reduced computational effort by exploiting symmetries and analytic properties that are obscured in the diagram-by-diagram approach.

6. **Quantum gravity:** Dyson's power-counting analysis, applied to general relativity, gives $D = 2L + 2$, indicating that new divergences appear at every loop order. This is the technical statement of non-renormalizability and motivates the search for UV completions (string theory, asymptotic safety) or reformulations (loop quantum gravity) of quantum gravity.
