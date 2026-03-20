# Quantum Theory of Gravitation

**Author:** Richard P. Feynman
**Year:** 1963
**Journal:** *Acta Physica Polonica*, 24, 697--722 (Conference on the Role of Gravitation in Physics, Chapel Hill, 1957; published in the proceedings of a 1962 Warsaw conference)

---

## Abstract

Feynman applies the methods of quantum field theory -- perturbative expansion, Feynman diagrams, and path integrals -- to general relativity, treating the gravitational field as a spin-2 quantum field (the graviton) propagating on a flat Minkowski background. He derives the graviton propagator, constructs the Feynman rules for gravitational interactions, and discovers that naive application of these rules to loop diagrams produces inconsistencies: gauge-dependent (unphysical) results in loop calculations that can be cured only by introducing fictitious particles (ghost fields) into internal loops. This discovery of ghost fields in non-Abelian gauge theories -- made independently and more systematically by Faddeev and Popov (1967) and by DeWitt (1967) -- is one of the paper's most important contributions. Feynman also discusses the one-loop structure of quantum gravity, finds divergences that presage the eventual proof of non-renormalizability, and reflects on whether the quantization of gravity requires fundamentally new ideas.

---

## Historical Context

### The State of Quantum Gravity in the 1950s-60s

By the early 1960s, the quantization of electromagnetism (QED) was a spectacular success, and gauge field theories for the strong and weak interactions were being explored. General relativity, however, resisted quantization. The difficulties were both conceptual (what does it mean to quantize spacetime itself?) and technical (the theory is non-polynomial in the metric, and the gauge invariance -- diffeomorphism invariance -- is far more complex than the $U(1)$ gauge invariance of electromagnetism).

Several approaches were being pursued:
- **Canonical quantization** (Dirac, Bergmann, Arnowitt-Deser-Misner): quantize the metric on a spacelike surface, treating the Hamiltonian constraint as an operator equation. This approach struggled with the "problem of time" and the constraint algebra.
- **Covariant quantization** (Gupta, DeWitt): expand $g_{\mu\nu} = \eta_{\mu\nu} + \kappa h_{\mu\nu}$ and quantize the perturbation $h_{\mu\nu}$. This is the approach Feynman takes.
- **Path integral** (Misner, Hawking, later): integrate over all metrics $g_{\mu\nu}$ weighted by $e^{iS_{\text{EH}}/\hbar}$.

### Feynman's Motivation

Feynman's interest in quantum gravity arose from his belief that all of physics should be describable in quantum mechanical terms. At the 1957 Chapel Hill conference, he presented arguments (including a thought experiment with a gravitational Stern-Gerlach apparatus) that gravity must be quantized: if a classical gravitational field could be used to measure the position of a quantum particle without disturbing it, quantum mechanics would be violated.

The paper is based on Feynman's Chapel Hill talk (1957) but was not formally published until the proceedings of a 1962 Warsaw conference. Despite the delayed publication, the ideas had circulated through the community and influenced DeWitt, Faddeev, Popov, and others.

---

## Key Arguments and Derivations

### 1. Linearized Gravity and the Graviton

Feynman expands the metric around flat spacetime:

$$g_{\mu\nu} = \eta_{\mu\nu} + \kappa h_{\mu\nu}$$

where $\kappa = \sqrt{32\pi G}$ and $h_{\mu\nu}$ is a symmetric tensor field. The Einstein-Hilbert action $S = \frac{1}{16\pi G}\int R\sqrt{-g} \, d^4x$, expanded to second order in $h$, gives the linearized action:

$$S^{(2)} = \int d^4x \left[\frac{1}{2}\partial_\alpha h_{\mu\nu}\partial^\alpha h^{\mu\nu} - \frac{1}{2}\partial_\alpha h \partial^\alpha h + \partial_\mu h^{\mu\nu}\partial_\nu h - \partial_\mu h^{\mu\nu}\partial^\alpha h_{\alpha\nu}\right]$$

where $h = h^\mu{}_\mu$ is the trace. This is invariant under the linearized diffeomorphism (gauge transformation):

$$h_{\mu\nu} \to h_{\mu\nu} + \partial_\mu \xi_\nu + \partial_\nu \xi_\mu$$

analogous to the electromagnetic gauge transformation $A_\mu \to A_\mu + \partial_\mu \Lambda$.

The field $h_{\mu\nu}$ represents the graviton: a massless spin-2 particle. The physical (transverse-traceless) degrees of freedom are 2, corresponding to the two helicity states $\pm 2$ of the graviton.

### 2. Gauge Fixing and the Graviton Propagator

To define the propagator, the gauge must be fixed. Feynman uses the harmonic (de Donder) gauge:

$$\partial^\mu \bar{h}_{\mu\nu} = 0, \quad \bar{h}_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu}h$$

Adding a gauge-fixing term $\frac{1}{2}(\partial^\mu \bar{h}_{\mu\nu})^2$ to the action, the propagator in momentum space becomes:

$$D_{\mu\nu;\alpha\beta}(k) = \frac{i}{k^2 + i\epsilon}\left[\frac{1}{2}(\eta_{\mu\alpha}\eta_{\nu\beta} + \eta_{\mu\beta}\eta_{\nu\alpha}) - \frac{1}{2}\eta_{\mu\nu}\eta_{\alpha\beta}\right]$$

This is the "Feynman gauge" graviton propagator, analogous to $-ig_{\mu\nu}/(k^2 + i\epsilon)$ for the photon. The tensor structure $\frac{1}{2}(\eta_{\mu\alpha}\eta_{\nu\beta} + \eta_{\mu\beta}\eta_{\nu\alpha}) - \frac{1}{2}\eta_{\mu\nu}\eta_{\alpha\beta}$ projects onto the symmetric traceless tensor representations, as appropriate for a spin-2 field.

### 3. Gravitational Vertices

Expanding the Einstein-Hilbert action to higher orders in $h$ produces graviton self-interaction vertices. Unlike QED, where the photon has no self-coupling (the theory is Abelian), gravity is inherently self-interacting: gravitons gravitate.

The cubic vertex (three-graviton coupling) comes from the $O(h^3)$ term in the expansion of $R\sqrt{-g}$. Schematically:

$$V^{(3)}_{\mu\nu;\alpha\beta;\rho\sigma}(k_1, k_2, k_3) \propto \kappa \cdot [\text{polynomial in } \eta_{\cdot\cdot} \text{ and } k_\cdot]$$

The explicit expression involves dozens of terms due to the index structure of a rank-2 symmetric tensor. There are also quartic ($O(\kappa^2)$), quintic ($O(\kappa^3)$), and higher-order vertices, making gravity a non-polynomial theory. This proliferation of vertices is one reason gravitational calculations are far more laborious than their QED counterparts.

The coupling to matter is through the energy-momentum tensor $T^{\mu\nu}$:

$$\mathcal{L}_{\text{int}} = -\frac{\kappa}{2}h_{\mu\nu}T^{\mu\nu}$$

For a scalar field $\phi$ with $T^{\mu\nu} = \partial^\mu\phi\partial^\nu\phi - \frac{1}{2}\eta^{\mu\nu}(\partial\phi)^2 + \frac{1}{2}\eta^{\mu\nu}m^2\phi^2$, this gives the graviton-scalar vertex.

### 4. Tree-Level Graviton Exchange

At tree level, the exchange of a single graviton between two massive particles gives Newton's law of gravitation. The amplitude for graviton exchange between particles with momenta $p_1, p_2$ and $p_3, p_4$ is:

$$\mathcal{M} = -\frac{\kappa^2}{4}\frac{T^{\mu\nu}(1,3) \left[\frac{1}{2}(\eta_{\mu\alpha}\eta_{\nu\beta} + \eta_{\mu\beta}\eta_{\nu\alpha}) - \frac{1}{2}\eta_{\mu\nu}\eta_{\alpha\beta}\right] T^{\alpha\beta}(2,4)}{q^2}$$

In the non-relativistic limit ($p^0 \gg |\mathbf{p}|$, $T^{00} \approx m$), this reduces to:

$$\mathcal{M} \approx \frac{\kappa^2 m_1 m_2}{4q^2} = \frac{8\pi G m_1 m_2}{q^2}$$

The Fourier transform gives $V(r) = -Gm_1m_2/r$: Newton's gravitational potential.

### 5. The Ghost Problem

This is the paper's most far-reaching contribution. Feynman discovers that loop calculations in quantum gravity (and in Yang-Mills theories generally) give results that depend on the gauge choice, violating unitarity. The problem can be illustrated with a one-loop graviton self-energy diagram.

Consider the one-loop correction to the graviton propagator. The loop involves two internal graviton lines connected by two cubic vertices. Computing the imaginary part of this diagram (via the optical theorem, related to the total cross section by unitarity) should give the sum over all physical intermediate states -- two transverse-traceless gravitons with helicities $\pm 2$. However, Feynman finds that the naive calculation gives contributions from unphysical polarizations (longitudinal and trace modes) that do not cancel.

The resolution, which Feynman discovers and states but does not fully systematize, is that additional "ghost" diagrams must be included. These involve fictitious scalar particles (or in the full theory, anti-commuting vector particles) that circulate in the loop and cancel the unphysical contributions. Feynman writes:

"I found the rule for trees...[but] for closed loops...the results were not gauge invariant...I found I had to subtract something...a contribution of a ghost going around the loop..."

The ghost field for gravity is a vector (spin-1) field $\eta^\mu$ with the wrong statistics (Fermi statistics for a vector field). Its propagator is:

$$D^{\text{ghost}}_{\mu\nu}(k) = \frac{-i\eta_{\mu\nu}}{k^2 + i\epsilon}$$

and its coupling to the graviton comes from the gauge-fixing procedure. The ghost contribution has a minus sign relative to real particle loops (due to the wrong statistics), which exactly cancels the unphysical polarization contributions.

### 6. Connection to Faddeev-Popov

Feynman's discovery was placed on a rigorous foundation by Faddeev and Popov (1967), who showed that the ghosts arise necessarily from the path integral when gauge-fixing a non-Abelian gauge theory. The correct path integral measure is:

$$Z = \int \mathcal{D}[h_{\mu\nu}] \mathcal{D}[\bar{c}^\mu] \mathcal{D}[c^\nu] \, \det\left(\frac{\delta F^\alpha}{\delta \xi^\beta}\right) \exp\left(iS_{\text{EH}} + iS_{\text{gf}} + iS_{\text{ghost}}\right)$$

where $F^\alpha = 0$ is the gauge condition, $\xi^\beta$ is the gauge parameter, and $c^\mu, \bar{c}^\mu$ are the ghost and anti-ghost fields. The functional determinant $\det(\delta F/\delta\xi)$ is precisely the ghost contribution. For an Abelian theory like QED, this determinant is field-independent and can be dropped -- which is why QED has no ghosts.

### 7. One-Loop Divergences

Feynman examines the divergence structure of one-loop graviton diagrams. By power counting, the superficial degree of divergence of a diagram with $E$ external graviton lines and $L$ loops is:

$$D = 2 + 2L - 0 \cdot E$$

(The graviton propagator goes as $1/k^2$ and each vertex brings two derivatives, hence two powers of momentum.) For one loop ($L = 1$), $D = 4$, indicating a quartic divergence. However, the gauge symmetry (diffeomorphism invariance) reduces this significantly: the on-shell divergences at one loop are proportional to:

$$\int d^4x \sqrt{-g}\left(aR^2 + bR_{\mu\nu}R^{\mu\nu} + cR_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}\right)$$

For pure gravity (no matter), 't Hooft and Veltman showed in 1974 that these one-loop divergences actually vanish on shell (due to the Gauss-Bonnet identity in four dimensions). However, this is an accident of one loop; at two loops, Goroff and Sagnotti (1986) showed that a non-vanishing, non-removable divergence proportional to $R_{\mu\nu}^{\ \ \rho\sigma}R_{\rho\sigma}^{\ \ \alpha\beta}R_{\alpha\beta}^{\ \ \mu\nu}$ appears, confirming that quantum gravity (treated perturbatively) is non-renormalizable.

---

## Physical Interpretation

### Gravity as a Gauge Theory

Feynman's approach treats general relativity as a gauge theory of a spin-2 field, with diffeomorphism invariance playing the role of gauge invariance. This perspective reveals deep structural parallels with Yang-Mills theories:
- Both have self-interacting gauge bosons (gravitons/gluons)
- Both require ghost fields for consistent quantization
- Both have gauge-invariant physical observables and gauge-dependent intermediate quantities

The difference is that gravity's gauge group (the diffeomorphism group) is infinite-dimensional and non-compact, and the coupling ($\kappa = \sqrt{32\pi G}$) has dimensions of $[\text{length}]$ in natural units, making the theory non-renormalizable by power counting.

### Gravitons and Classical Gravity

The tree-level graviton exchange reproduces Newton's law, and the resummation of tree diagrams reproduces the full nonlinear classical solutions of general relativity (including the Schwarzschild solution, gravitational waves, etc.). The quantum effects appear only in loops and are suppressed by powers of $E^2/M_{\text{Pl}}^2$, where $E$ is the characteristic energy and $M_{\text{Pl}} = 1/\sqrt{G} \approx 1.2 \times 10^{19}$ GeV is the Planck mass. This explains why quantum gravity effects are utterly negligible at accessible energies.

### The Non-Renormalizability Problem

Feynman's paper hints at what became the central problem of quantum gravity: the theory is non-renormalizable, meaning that new divergences appear at each loop order, requiring an infinite number of counterterms. This suggests either:
1. Gravity must be embedded in a larger, UV-complete theory (string theory, loop quantum gravity, etc.)
2. Gravity is asymptotically safe (has a non-trivial UV fixed point)
3. The perturbative approach is fundamentally inadequate

---

## Impact and Legacy

### Faddeev-Popov Ghosts

Feynman's discovery of ghosts was generalized by Faddeev and Popov to all non-Abelian gauge theories. The ghost fields are essential for:
- Maintaining unitarity in loop calculations
- Defining the BRST symmetry (Becchi, Rouet, Stora, Tyutin), which provides the most elegant formulation of gauge invariance in quantum field theory
- Proving the renormalizability of Yang-Mills theories ('t Hooft, 1971)

### DeWitt's Program

Bryce DeWitt extensively developed the covariant quantization of gravity, building on Feynman's work. His background field method, combined with the Faddeev-Popov procedure, became the standard approach for computing gravitational effective actions.

### Gravitational Effective Field Theory

The modern perspective (Donoghue, 1994) treats quantum gravity as an effective field theory, valid below the Planck scale. In this framework, the non-renormalizability is not a fundamental problem but a signal that new physics appears at $M_{\text{Pl}}$. The one-loop corrections are finite predictions:

$$V(r) = -\frac{Gm_1 m_2}{r}\left(1 + \frac{41}{10\pi}\frac{G}{r^2} + \cdots\right)$$

giving the leading quantum correction to Newton's law.

---

## Connections to Modern Physics

1. **String theory:** The graviton emerges as a massless spin-2 mode of the closed string. The tree-level graviton scattering amplitude in string theory reproduces Feynman's result at low energies and resolves the UV divergences at high energies through the extended nature of the string.

2. **Double copy:** The "double copy" relation (Bern, Carrasco, Johansson) states that graviton amplitudes can be obtained as the "square" of gluon amplitudes: $\mathcal{M}_{\text{gravity}} \sim \mathcal{M}_{\text{YM}} \otimes \mathcal{M}_{\text{YM}}$. This remarkable structural relation, whose origin is understood through string theory, makes multi-loop gravitational calculations feasible.

3. **Gravitational wave physics:** The post-Newtonian expansion used for LIGO/Virgo template generation is a systematic expansion in $v/c$ and $Gm/r$ that uses Feynman diagram techniques. The effective field theory approach (NRGR) treats the binary system using graviton exchange diagrams between the two bodies.

4. **Asymptotic safety:** Reuter's (1998) application of the functional renormalization group to gravity finds evidence for a non-trivial UV fixed point, suggesting that gravity might be non-perturbatively renormalizable despite its perturbative non-renormalizability. The fixed-point action involves the operators identified by Feynman's power-counting analysis.

5. **Kaluza-Klein gravitons:** In extra-dimensional theories, the graviton propagator is modified by the KK tower: $D(k) \to \sum_n D_n(k)$, where $n$ labels the KK modes with masses $m_n \sim n/R$. The summation over the tower modifies the UV behavior and can lead to enhanced gravitational effects at the compactification scale, with implications for both collider physics and cosmological evolution.
