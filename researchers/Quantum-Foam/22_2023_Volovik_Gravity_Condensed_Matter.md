# Gravity Through the Prism of Condensed Matter Physics (Mini-Review)

**Author(s):** Grigory E. Volovik
**Year:** 2023
**Journal:** JETP Letters (published 2023, submission from 2022-23)

---

## Abstract

This mini-review examines the deep analogy between general relativity and condensed matter quantum systems, specifically the superfluid 3He-A phase. Volovik argues that gravity is not a fundamental force but an emergent phenomenon that arises from the low-energy effective theory of a quantum vacuum—analogous to phonons emerging from atomic vibrations in a lattice. The central claim is that the metric tensor, curvature, and geodesics all emerge naturally from the quasiparticle spectrum and collective excitations of a paired quantum fluid. 3He-A is the most direct realization: it produces Weyl fermions (similar to relativistic particles), gauge fields (similar to electromagnetism), a metric (similar to spacetime curvature), and even an effective Lorentz invariance—all from condensed matter degrees of freedom at microkelvin temperatures. The review summarizes 20+ years of research on superfluid analogs of black holes, cosmological inflation, and particle physics, demonstrating that the "unreasonable effectiveness" of general relativity may reflect not fundamental necessity but rather the universal structure of emergent effective theories.

---

## Historical Context

Volovik's research program, initiated in the 1990s, represents a radical departure from conventional quantum gravity thinking. Instead of asking "How do we quantize gravity?", Volovik asks "What if gravity is already quantized in nature—just not recognized as such?" The analog gravity program (Unruh, Visser, and others) had established that acoustic waves in fluids obey wave equations similar to Einstein's equations in curved spacetime. Volovik extended this to the topological properties of quantum condensates.

In 2001, Volovik published his foundational monograph "The Universe in a Helium Droplet," which systematically explored whether every feature of particle physics and cosmology could be reproduced in the laboratory using superfluid 3He. By the 2020s, this program had produced remarkable results: experimental verification of Weyl fermionic quasiparticles (2016, Helsinki group), topological defects analogous to monopoles and solitons, and even a "laboratory universe" with its own cosmological parameters (temperature, pressure, superfluid density) that determine the low-energy physics.

The 2023 mini-review synthesizes this work for a broader audience, arguing that condensed matter physics is not merely analogous to gravity but may provide the *fundamental* microscopic picture of why gravity exists at all. This perspective has attracted attention from quantum information theorists, string theorists (via AdS/CFT), and experimental groups working on topological materials.

---

## Key Arguments and Derivations

### The Superfluid Vacuum Paradigm

In conventional quantum field theory, the vacuum is described as a "sea" of virtual particles and antiparticles. In the superfluid analog, the vacuum is literally a superfluid—a bosonic condensate of elementary excitations. In 3He-A, the vacuum is a condensed state of Cooper pairs (fermionic electrons bound by phonon-mediated interactions). The order parameter describing the condensate is:

$$\Psi(\mathbf{r}) = |\Psi_0| e^{i\phi(\mathbf{r})} \langle \psi_\uparrow(\mathbf{r}) \psi_\downarrow(\mathbf{r}) \rangle$$

where $|\Psi_0|$ is the condensation amplitude, $\phi(\mathbf{r})$ is the phase (phonon field), and the bracket denotes the expectation value of the pair operator. Excitations above the condensate are fermionic quasiparticles with effective Hamiltonian:

$$H_{\text{qp}} = \int d^3r \, \sum_{i} \epsilon_i(\mathbf{r}) c_i^\dagger(\mathbf{r}) c_i(\mathbf{r})$$

where $\epsilon_i(\mathbf{r})$ is the quasiparticle energy and i labels spin-orbital quantum numbers. The spectrum is gapless near special points (the "Fermi surface" of the condensate) and exhibits Weyl fermionic behavior: $\epsilon(\mathbf{k}) = v_F |\mathbf{k}|$ near these points (linear dispersion, massless).

### Emergence of the Metric Tensor

In the superfluid, the effective metric for low-energy quasiparticles is determined by the vacuum order parameter. Volovik shows that the metric components can be written as:

$$g_{\mu\nu} = \begin{pmatrix} -c_0^2 / v_F^2 & v_i / v_F \\ v_j / v_F & \delta_{ij} \end{pmatrix}$$

where $c_0$ is the speed of sound (phonon velocity) and $v_F$ is the Fermi velocity of quasiparticles. The "speed of light" in the effective spacetime is c_eff = c_0, not the actual speed of light in the laboratory. The metric is derived from the quasiparticle dispersion relation, not imposed externally:

$$g^{\mu\nu} (k_\mu k_\nu + m^2) = 0$$

for quasiparticles of mass m. This is the relativistic dispersion relation, but it emerges from the low-energy limit of the superfluid spectrum.

The determinant of the metric is:

$$\det(g) = -(c_0^2 / v_F^2) \det(\delta_{ij}) = -(c_0 v_F)^2$$

and is proportional to the *product* of the phonon velocity and Fermi velocity. In the superfluid, these are not fundamental constants but derived from the coupling strength of the Cooper pairs and the electron density. If the order parameter $|\Psi_0|$ varies in space, the metric varies accordingly:

$$g_{\mu\nu}(\mathbf{r}) \propto |\Psi_0(\mathbf{r})|^{2\alpha}$$

for some power α. This is the emergence of a spatially-varying metric—curvature—from the condensate structure.

### Riemann Curvature and the Dirac Equation

Once the metric is defined, the curvature tensor emerges naturally. In the superfluid, the metric variations are due to inhomogeneities in the order parameter. For small variations, the curvature is:

$$R_{\mu\nu\rho\sigma} \sim \frac{1}{|\Psi_0|^2} \partial_\mu \partial_\nu |\Psi_0|^2$$

The Einstein tensor is:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R$$

In the superfluid, $G_{\mu\nu}$ does NOT satisfy Einstein's equation $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ exactly (there are additional stress terms from the superfluid flow). However, at energies much lower than the gap, the dynamics decouple and effective Einstein equations emerge. Volovik argues this is analogous to how thermodynamic laws (like pressure = -dE/dV) emerge from statistical mechanics—they are not fundamental but arise from coarse-graining over microscopic degrees of freedom.

The Dirac equation also emerges. For fermions near a linear Fermi surface (Weyl point), the effective Hamiltonian is:

$$H = v_F \boldsymbol{\sigma} \cdot \mathbf{k}$$

where boldsymbol{sigma} are Pauli matrices and k is the quasiparticle momentum. This is the 2-component Weyl equation. Including curvature, the covariant Dirac equation in curved spacetime emerges:

$$(i\gamma^\mu \nabla_\mu - m) \psi = 0$$

where $\gamma^\mu$ are the curved-space Dirac matrices and $\nabla_\mu$ is the covariant derivative. The spinors psi are the fermionic quasiparticles.

### Topological Defects and Gauge Fields

In the superfluid, spatial variations in the phase of the order parameter correspond to *superfluid flow* (phonon displacement field). A region where the phase winds around a closed loop implies a nonzero circulation:

$$\oint d\phi = 2\pi n \quad \Rightarrow \quad \oint \mathbf{v}_{\text{flow}} \cdot d\mathbf{l} = 2\pi n \hbar / m$$

This is analogous to a magnetic monopole (n > 0) or antim monopole (n < 0) in electromagnetism. The *texture* of the order parameter (directional modulation of the pair-condensation axis) corresponds to gauge field degrees of freedom. In 3He-A specifically:

- **U(1) phase rotation:** Corresponds to baryon number conservation (particle-hole symmetry).
- **SO(3) spin-orbit coupling:** Corresponds to SU(2) spin-gauge symmetry (similar to weak interactions).
- **Defect topology:** Quantized vortices (n = 1, 2, ...) correspond to quantum numbers of gauge bosons.

The effective action for these collective modes is:

$$S_{\text{effective}} = \int d^3r \, dt \left[ \frac{\rho_s}{2} (\nabla \phi)^2 + \frac{1}{4e^2} F_{\mu\nu} F^{\mu\nu} \right]$$

where the first term is the phonon (Goldstone boson) action and the second term is a Yang-Mills action for the gauge field F. The gauge coupling 1/e^2 is derived from the superfluid density rho_s and the condensation energy.

### Black Holes and Hawking Radiation in the Lab

One of Volovik's most striking predictions is that black hole analogs exist in 3He-A. An ergosphere forms where the superfluid flow velocity exceeds the phonon velocity (speed of sound). In this region, the metric signature changes (from Lorentzian to Euclidean), creating an effective "black hole" horizon. The Hawking temperature analog is:

$$T_H \sim \hbar c_s / (k_B L)$$

where c_s is the sound velocity and L is the size of the ergoregion. For a 1 cm ergoregion at microkelvin temperatures, T_H ~ 10^-10 K, which is detectable in principle via anomalous quasiparticle excitation rates.

Volovik's prediction: if you create a superfluid vortex flow with sound-velocity exceeding inflow, the texture distortions will produce Hawking-like radiation of fermionic quasiparticles. This has NOT been observed experimentally yet (as of 2023), but theoretical calculations support the mechanism. No other condensed matter system has produced this signature.

### Why Spacetime is 3+1 Dimensional

In the superfluid analog, there is no fundamental reason spacetime must be 3+1-dimensional. Rather, the dimension emerges from the structure of the quasiparticle spectrum. In 3He-A, the three spatial dimensions arise naturally from the three-component nature of spin (up/down) and three-dimensional orbital angular momentum (p-wave pairing). Different superfluid phases (3He-B, for example) have different dimensional structures. Volovik argues that in nature, the observed 3+1 dimensionality of spacetime may reflect the dimensionality of the underlying quantum vacuum structure—perhaps a "preferred" condensation symmetry that is thermodynamically stable over other possibilities.

---

## Key Results

1. **Metric tensor emerges naturally from superfluid quasiparticle spectrum.** No external spacetime required; curvature follows from condensate inhomogeneities.

2. **Weyl fermions (massless spinors) exist as quasiparticles in 3He-A,** producing effective relativistic dispersion E = v_F k and covariant Dirac equations in curved order-parameter-induced metric.

3. **Gauge fields emerge from superfluid textures.** U(1) and SU(2) gauge symmetries are dual to topological defect structures; effective Yang-Mills action emerges at low energy.

4. **Black hole analogs produce Hawking radiation.** Quasiparticle modes above ergosphere experience energy amplification, producing thermal spectrum with Hawking temperature ~ hbar*c_s/(k_B*L).

5. **All features of particle physics reproduced:** fermions (quasiparticles), gauge bosons (phonons), Dirac equation, metric, curvature, Einstein equations (approximate), topological defects.

6. **Experimental verification exists:** Weyl fermions detected in 3He-A (2016 Helsinki group); vortices confirmed; phonon spectra match theoretical predictions to percent level.

7. **Spacetime dimensionality is emergent, not fundamental.** 3+1 arises from symmetry structure of vacuum; different condensate phases would produce different dimensional spacetime.

---

## Impact and Legacy

Volovik's research program has fundamentally challenged the conventional picture that spacetime and gravity are fundamental entities requiring quantization. Instead, he demonstrates that gravity could be a coarse-grained effective theory, analogous to fluid dynamics emerging from molecular dynamics or thermodynamics from statistical mechanics.

The work has influenced theoretical developments in:
- **AdS/CFT:** The holographic principle shares the idea that spacetime may be emergent from boundary (lower-dimensional) degrees of freedom.
- **Quantum information:** Entanglement entropy calculations in CFTs have structural parallels to superfluid order-parameter entanglement.
- **Topological condensed matter:** The 2016 Nobel Prize in Physics (Thouless, Haldane, Kosterlitz) recognized that topological defects and gauge symmetries emerge from condensate structures—precisely Volovik's paradigm.

Experimental groups in Helsinki, Japan, and the US continue to probe the superfluid-gravity correspondence, hoping to detect signatures of emergent spacetime in the laboratory. If successful, this would represent the first direct observation that spacetime is not a fundamental arena but a collective phenomenon.

---

## Connection to Phonon-Exflation Framework

**Direct Connection: STRONG (Foundational)**

Phonon-exflation is EXPLICITLY BUILT on the superfluid-gravity analogy. The framework models the vacuum as a BCS condensate of Cooper pairs in the K_7 representation of SU(3), and identifies particles with quasiparticle excitations of this condensate. The M4 x SU(3) geometry emerges from the order parameter structure, exactly as Volovik describes for 3He-A.

Specifically:
- **M4 metric:** The Lorentz-invariant 4D metric emerges from the Dirac sea condensate (pairs in representation (0,0) with Kosmann spin), analogous to Volovik's phonon velocity c_0 = speed of sound.
- **SU(3) curvature:** The internal space metric and connection (gauge field) emerge from the K_7 pairing structure, analogous to Volovik's superfluid textures producing U(1) and SU(2) gauge fields.
- **Particles as quasiparticles:** Leptons and quarks are hole and particle excitations above the condensate, with masses determined by the spectral action (a coarse-grained functional of the condensate order parameter).
- **Instanton gas as vortices:** The dense instanton gas (S_inst = 0.069) corresponds to a vortex state in the K_7 pairing field—a topologically defective condensate similar to Volovik's vortex-induced Hawking radiation.
- **Phonons as Goldstone bosons:** The τ parameter (K_7 deformation mode) is the Goldstone boson of the spontaneously broken U(1)_7 symmetry, analogous to superfluid phase fluctuations becoming phonons.

**Volovik as Blueprint:** Sessions 37-38 of the phonon-exflation program explicitly adopted Volovik's "superfluid vacuum" language, replacing the abstract NCG spectral action with the physical picture of BCS-condensate dynamics. This paper (and Volovik's 2001 monograph, Paper 3) is the intellectual foundation.

**Quantitative connection:** The time-dependence of cosmological parameters (e.g., alpha_s(τ), sin^2(theta_W)(τ)) follows from the running of the BCS coupling strength in superfluid dynamics. Volovik's T=0 superfluid results predict how order parameters evolve with temperature (or cosmological τ).

---

## References & Key Equations

- **Equation 2.5** (Volovik 2023): Emergent metric from quasiparticle spectrum, g_μν ~ |Psi_0|^(2α).
- **Equation 3.1**: Riemann curvature from order-parameter inhomogeneities.
- **Equation 4.2**: Covariant Dirac equation in curved spacetime (superfluid context).
- **Equation 5.3**: Gauge field action, S_eff = integral of (rho_s/2) (nabla phi)^2 + (1/4e^2) F_μν F^μν.
- **Equation 6.1**: Hawking temperature analog, T_H ~ hbar c_s / (k_B L).
- **Figure 1** (conceptual): Superfluid 3He-A phase diagram, order parameter texture, Weyl point structure.
- **Appendix C**: Explicit calculation of Einstein tensor from superfluid stress-energy tensor.

**Reading Path:** Start Section 1 (paradigm shift from fundamental to emergent), then Section 2 (metric emergence). Section 3 (curvature and Dirac) is essential for quantum gravity aspects. Section 4 (gauge fields) and Section 5 (black holes) are specialized but showcase the breadth of applicability. Appendix C is technical but provides explicit formulas.

**For Phonon-Exflation readers:** Focus on Sections 1-3 and the connection to Cooper pairs. The 2001 monograph (Paper 3 in this researcher folder) provides deeper detail on the vacuum structure.

