# Elasticity Tetrads, Gravitational Tetrads, and Emergent Gravity

**Authors:** J. Nissinen, G.E. Volovik

**Year:** 2019

**Journal:** Physical Review D 99, 016009 (2019)

**arXiv:** 1811.09236

---

## Abstract

We analyze the tetrad fields that emerge from elastic deformations in topological matter and compare them to the gravitational tetrads of general relativity. In crystalline solids and topological insulators, lattice vibrations (phonons) couple to fermions through elasticity-induced tetrad fields that are structurally identical to the tetrad formulation of gravity. We demonstrate that the effective gravity emerging from phononic excitations in solids can be described using the same mathematical framework as Einstein's tetrad gravity. The connection between elasticity tetrads and gravitational tetrads provides a concrete condensed-matter realization of emergent gravity, where curvature and torsion arise naturally from lattice deformations.

---

## Historical Context

The concept that gravity could emerge from a more fundamental substrate has deep roots in quantum gravity research. Wheeler's "it from bit" and recent developments in holography suggest that spacetime geometry is not fundamental but emergent from quantum entanglement. Volovik's program, spanning decades, demonstrates that analogue gravity systems—particularly superfluids and solids—can reproduce gravitational phenomena in a controlled laboratory setting.

The tetrad (or vielbein) formulation of gravity, developed by Einstein, Cartan, and others, expresses spacetime geometry in terms of orthonormal frame fields rather than metric tensors. Remarkably, Nissinen and Volovik discovered that the *identical mathematical structure* arises naturally when phonons couple to elastic deformations in condensed matter. This is not merely an analogy—it is structural isomorphism: the elasticity tensor generates tetrad transformations indistinguishable from gravitational gauge transformations.

In the framework of topological insulators and Weyl semimetals, fermions couple to lattice deformations through Berry-phase mechanisms. These couplings produce effective gauge fields and, as Nissinen and Volovik show, emergent tetrads. The lattice acts as the *vacuum* (in the relativity sense), and phonons are the *excitations of the vacuum*—precisely the structure expected if gravity is emergent.

For phonon-exflation, this work is foundational: the Jensen deformation at the fold is *geometrically* a tetrad transformation. The internal SU(3) coordinates undergo a volume-preserving deformation that, from the 4D external perspective, appears as a metric rescaling and Weyl transform. Nissinen-Volovik shows that such transformations are mathematically identical to those produced by elastic strain in a crystal.

---

## Key Arguments and Derivations

### Tetrad Formalism in Gravity

In Einstein's formulation, spacetime is described by a metric $g_{\mu\nu}$ or equivalently by a tetrad (vielbein) field $e_a^\mu$ that satisfies:

$$g_{\mu\nu} = \eta_{ab} e_a^\mu e_b^\nu$$

where $\eta_{ab} = \text{diag}(+,-,-,-)$ is the Minkowski metric in tangent space. The tetrad is not unique—it can be rotated by local Lorentz transformations:

$$e_a^\mu \to \Lambda_a^{\phantom{a}b} e_b^\mu$$

The spin connection $\omega_\mu^{\phantom{\mu}ab}$ couples the tetrad to fermions via the covariant derivative:

$$D_\mu \psi = \partial_\mu \psi + \frac{1}{4} \omega_\mu^{\phantom{\mu}ab} \gamma_{ab} \psi$$

where $\gamma_{ab} = \frac{1}{2}[\gamma_a, \gamma_b]$ are the generators of Lorentz transformations.

### Elasticity Tetrads in Solids

In a crystalline solid with elastic deformations parameterized by a strain tensor $u_{ij} = \frac{1}{2}(\partial_i u_j + \partial_j u_i)$, lattice vibrations couple to Bloch electrons. The key insight is that elastic strain induces a *metric deformation* in the band structure:

$$g_{ij}^{\text{eff}} = \delta_{ij} + \text{(elastic coupling terms)}$$

This effective metric can be precisely written in tetrad form. Define the elasticity tetrad:

$$e^{\text{elast}}_a{}^i = \delta_a^i + \partial_a u^i$$

Then the deformed metric becomes:

$$g_{ij} = \delta_{ab} e_a^{\text{elast},i} e_b^{\text{elast},j}$$

This is *structurally identical* to the gravitational tetrad formula. The phonon energy-momentum tensor couples to this effective metric just as matter couples to gravity in general relativity.

### Berry Phase Mechanism

Fermions in topological insulators and Weyl semimetals couple to phonons through Berry phase terms. The effective low-energy Hamiltonian becomes:

$$H = v_F \sigma \cdot (\mathbf{p} + \mathbf{A}_{\text{Berry}}) + V_{\text{deform}}$$

where $\mathbf{A}_{\text{Berry}}$ is a Berry gauge field and $V_{\text{deform}}$ encodes the coupling to lattice deformation. In the adiabatic limit, integrating out the band structure produces an effective action for the emergent gravitational field:

$$S_{\text{eff}} = \int d^4x \sqrt{-g} \left[ \frac{1}{16\pi G} R + L_{\text{matter}} \right]$$

where $g$ is the determinant of the effective metric induced by the elasticity tetrad, and $R$ is the Ricci scalar. This is the Einstein-Hilbert action for emergent gravity.

### Curvature from Strain

A key result is that lattice curvature (dislocations and disclinations in the crystal) maps directly to spacetime curvature in the effective description. A screw dislocation with Burgers vector $\mathbf{b}$ produces a torsion:

$$T^a = db^a + \omega^a{}_b \wedge e^b$$

where $\omega$ is the spin connection. In terms of the strain tensor:

$$\text{Riemann} \sim \nabla \otimes \nabla u = \text{(lattice curvature)}$$

This means that the topological defects of the crystal (which have definite, measurable spatial extent) become identified with curvature singularities of the emergent metric.

### Mixed Axial-Gravitational Anomaly

In Weyl semimetals, fermions at different Weyl nodes carry opposite chirality. Lattice deformations couple preferentially to one chirality, producing a mixed axial-gravitational anomaly:

$$\partial_\mu j_5^\mu = \frac{N_W}{24\pi^2} R \wedge R$$

where $N_W$ is the number of Weyl nodes (weighted by charge). This anomaly, which appears in high-energy physics only in gravitational contexts, emerges naturally from the phonon-fermion coupling in condensed matter. It validates the identification of elasticity tetrads with gravitational tetrads.

---

## Key Results

1. **Structural Identity**: Elasticity tensors and gravitational tetrads are mathematically isomorphic. Phonon coupling to strain produces an effective Einstein-Hilbert action.

2. **Metric Emergence**: Lattice deformations generate effective metrics that govern fermion dynamics. The metric is not imposed—it emerges from microscopic elasticity.

3. **Curvature from Defects**: Topological defects in the crystal (dislocations, disclinations) map to spacetime curvature singularities in the effective description.

4. **Anomaly Realization**: The mixed axial-gravitational anomaly, which in standard particle physics requires coupling to gravity, appears naturally in the phonon-fermion system.

5. **Emergent Einstein Equations**: Backreaction of fermions on the phonon field produces effective Einstein equations relating the energy-momentum tensor to the emergent curvature.

6. **Lorentz Invariance at Low Energy**: Despite the discrete lattice structure, the long-wavelength effective theory exhibits full Lorentz and general coordinate invariance.

---

## Impact and Legacy

This work unified two seemingly disparate areas: condensed matter elasticity and gravitational physics. It demonstrated that Einstein's tetrad formalism—long viewed as a mathematical tool in gravity—is actually the *natural* language for describing how fermions couple to deformations in solids.

The paper has profound implications for quantum gravity phenomenology. If gravity emerges from a microscopic substrate, then:
- The Planck length may be related to lattice spacing
- Quantization of geometry emerges naturally from the discrete substrate
- Violations of Lorentz invariance at trans-Planckian scales are testable

Nissinen and Volovik's framework provided a proof-of-principle that emergent gravity is not speculative—it occurs in real materials. Subsequent work has explored these connections in topological insulators, Weyl semimetals, and graphene-like systems.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The Jensen deformation at the fold (Session 20-24 computations) is precisely the tetrad transformation that Nissinen-Volovik describe. At $\tau = \tau_{\text{fold}}$, the internal SU(3) metric $G_{IJ}$ undergoes a volume-preserving distortion:

$$G_{IJ}(\tau) = \text{diag}(1, e^{-2\tau}, e^{-2\tau}) \to \text{diag}(1 + \delta, e^{-2(\tau+\epsilon)}, e^{-2(\tau+\epsilon)} - \delta)$$

This is an *elasticity tetrad transformation* in the internal space. From the external 4D perspective, this appears as a metric rescaling:

$$g_{00} \sim 1 - V_{\text{eff}}(\tau)$$

The instanton gas in Session 37-38 corresponds to *phonon excitations in the fabric* during the transit. The 992 Dirac eigenvalues comprise the phonon "density of states" of the deforming geometry.

Nissinen-Volovik shows that phonon coupling to strain generates effective gravity. In the framework, the *phonons ARE the particles* (quarks, leptons). They couple to the deforming fabric geometry through the very mechanism described in this paper.

**Testable Prediction**: The Weyl rescaling $g_{\mu\nu} \to e^{-2\phi} g_{\mu\nu}$ observed at the fold (Papers Baptista-24) should exhibit the same mixed axial-gravitational anomaly as in Weyl semimetals. The chiral asymmetry in the Dirac spectrum would manifest as a non-zero $\partial_\mu j_5^\mu \neq 0$ during transit.

**Lattice Defects as K.O. Dimension**: In the framework, topological defects in the internal-space lattice (e.g., dislocations in the 10 sectors' relative orientation) would generate curvature in the 4D external space—explaining why K.O. dimension = 6 (Session 7) rather than 8 or 10.

