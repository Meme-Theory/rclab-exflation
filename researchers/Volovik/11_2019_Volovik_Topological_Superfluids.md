# Topological Superfluids

**Author(s):** Grigory E. Volovik
**Year:** 2019
**Journal:** JETP (Zhurnal Eksperimental'noi i Teoreticheskoi Fiziki), 156(4), 700-706
**arXiv:** 1602.02595

---

## Abstract

This comprehensive review synthesizes Volovik's understanding of topological properties in superfluid 3He and other quantum liquids. The paper demonstrates that:

- Topological defects (quantized vortices, dislocations, domain walls, skyrmions) are fundamental to understanding superfluidity.
- The momentum-space topology (Fermi surface topology, Dirac points, Weyl points) determines the types of gapless fermions and their protection.
- Topologically protected Dirac, Weyl, and Majorana fermions exist in the bulk, on surfaces, and within topological defects.
- The topological structure gives rise to multiple types of quantum anomalies (axial, chiral, gravitational).
- Bulk-surface and bulk-vortex correspondences connect momentum-space topology to real-space properties.
- The framework extends beyond superfluid 3He to topological insulators, topological superconductors, and the Standard Model vacuum.

The review provides a unified perspective on how topology in momentum space and real space determines the low-energy physics of quantum systems and can be extended to fundamental particle physics.

---

## Historical Context

### Evolution of Topological Concepts in Condensed Matter (1980s-2010s)

The study of topology in condensed matter progressed through several stages:

1. **Quantum Hall Effect (1980)**: Von Klitzing discovered the integer quantum Hall effect — the Hall conductance is quantized in integer units. Laughlin (1983) explained this using a topological quantum number (Chern number) characterizing the filled Landau level wavefunction.

2. **Topological Insulators (2005-2010)**: Bernevig, Hughes, and Zhang proposed time-reversal-invariant topological insulators with insulating bulk but conducting surface states. Kane and Mele discovered the quantum spin Hall effect in graphene.

3. **Weyl Fermions (2003-2015)**: Volovik and Kopnin proposed Weyl fermions in the spectrum of certain superfluids and superconductors. Experimentally realized in solids (TaAs, WTe2, etc.) starting in 2015.

4. **Majorana Fermions (2010s)**: Proposal that topological superconductors host zero-energy Majorana modes at their surfaces or in vortex cores. Experimental searches continue.

5. **Topological Symmetry Protected Phases (2010s-2020s)**: Recognition that topological protection is possible with only discrete symmetries (time-reversal, particle-hole, or chiral), leading to the Altland-Zirnbauer classification.

Volovik's 2019 review integrates these developments into a coherent framework applicable to 3He and beyond.

### 3He as the Archetype Topological Superfluid

Superfluid 3He (discovered 1972) is the most complex quantum liquid known. Its two phases are:

- **3He-A**: Chiral p-wave superfluid with gap nodes and topologically nontrivial structure.
- **3He-B**: Isotropic p-wave superfluid with a fully gapped spectrum (topologically trivial).

By 2019, 3He was understood as the "quantum condensed matter analog of the Standard Model" — all the topological features observed in solid-state materials (Weyl points, Majorana modes, etc.) appear naturally in 3He, often with fully calculable microscopic theory.

---

## Key Arguments and Derivations

### Part I: Momentum-Space Topology

#### Fermi Surface as a Topological Manifold

For a normal (non-superconducting) metal, the Fermi surface is a 2D manifold in 3D momentum space. Its topological invariant is the **genus** $g$ (number of handles).

- Genus 0: Simply connected Fermi surface (sphere-like). Example: free electron model.
- Genus 1: Toroidal Fermi surface. Example: quasi-1D conductor with open bands.
- Genus > 1: More complex surfaces. Example: graphene with multiple sheets.

The genus is a topological invariant — it cannot change continuously as microscopic parameters vary. A topological phase transition occurs when the genus changes, mediated by a Lifshitz transition (Fermi surface touches a van Hove singularity).

#### Dirac and Weyl Points

In a superconductor or superfluid, gap nodes are special points or lines in momentum space where the energy vanishes.

For a **Dirac point** in 3D (codimension 2), the spectrum near the node is:

$$E(\mathbf{k}) = v_F |\mathbf{k} - \mathbf{k}_D|$$

where $\mathbf{k}_D$ is the location of the node. This linear spectrum is described by the Dirac equation.

The topological invariant is the **chirality** $\nu$:

$$\nu = \text{sign of } E / |\mathbf{k}|$$

For a simple node, $\nu = \pm 1$. The node cannot be gapped without closing or merging with another node of opposite chirality — this is topological protection.

A **Weyl point** is similar but has additional symmetries (e.g., a two-fold degeneracy that prevents gapping).

#### 3He-A Spectrum

In superfluid 3He-A, the quasiparticle spectrum is:

$$E(\mathbf{k}) = v_F \sqrt{(k_x^2 + k_y^2) + (A k_z)^2}$$

where $A$ is an anisotropy factor. The gap vanishes along a **line** where $k_z = 0$ (the equator of the Fermi sphere).

This is a codimension-1 defect in momentum space — a **Fermi surface** analog (but one-dimensional: a line rather than a 2D surface).

In 3He-B, the spectrum is fully gapped:

$$E(\mathbf{k}) = \sqrt{\xi_k^2 + \Delta^2}$$

where $\Delta$ is a constant. No nodes.

The topological character of 3He-A vs 3He-B reflects a difference in momentum-space topology.

### Part II: Topological Defects in Real Space

#### Vortex Core Bound States

A quantized vortex in 3He-A is a singular defect where the order parameter texture winds around the core. The singular structure creates **bound states** (zero modes or near-zero modes) within the vortex core.

For a vortex of circulation quantum $n = 1$ (one quantum of circulation), there is **one zero-energy bound state** per sector. This is a consequence of the bulk-vortex duality:

**Bulk winding number = Number of vortex zero modes**

In mathematical language:

$$N_{zero} = \nu$$

where $\nu$ is the winding (chirality) of the Dirac point and $N_{zero}$ is the number of zero modes bound to the vortex core.

#### Skyrmion Defects

A skyrmion is a continuous deformation of the order parameter (no singularity, unlike a vortex). In 3He-A, skyrmions are characterized by:

$$\mathbf{S} = \int d^3 r \, \frac{\partial^3 \ell_i}{\partial x \partial y \partial z}$$

The integral is the **skyrmion number** — an integer topological invariant.

Skyrmions carry:
- Angular momentum (linked to their topological structure)
- Chiral charge (if the skyrmion involves chiral rotations of the order parameter)
- Fermionic zero modes in the bulk (from the anomaly)

Experimentally, vortex-skyrmion configurations have been observed in NMR experiments on 3He.

#### Domain Walls and Hedgehogs

- **Domain walls**: Surfaces separating regions with different order parameter orientations. They carry surface charges and host Majorana-like modes.

- **Hedgehogs**: Solitonic defects where the order parameter points radially outward from a central point (like a hedgehog's spines). In 3He-A, hedgehogs are singular and unstable; in 3He-B, they are stable point defects.

### Part III: Surface States and Bulk-Surface Correspondence

#### Surface Andreev Bound States

When superfluid 3He-A is confined (e.g., in a container), the boundary breaks the translational symmetry. Andreev bound states form at the surface.

For a surface perpendicular to the order parameter $\ell_i$ (say, $\ell_i = \hat{z}$), the surface state spectrum is:

$$E_n(k_\parallel) = v_F \sqrt{k_\perp^2(n) + k_\parallel^2}$$

where $k_\perp(n)$ is a discretized perpendicular wavenumber depending on the boundary condition, and $k_\parallel$ is the parallel momentum.

The number of surface bands is determined by the **bulk topological invariant**:

$$N_{surface} = |\nu|$$

This is the **index theorem** in condensed matter form.

#### Bulk-Surface Duality

A remarkable theorem: **If the bulk has a nonzero topological invariant, the surface must have gapless states.**

Proof (sketch):
1. Smoothly deforming the bulk Hamiltonian while preserving the protecting symmetry does not change the bulk invariant.
2. At the boundary, the deformation must terminate (boundary breaks translational invariance).
3. This creates a "mismatch" — a gapless mode at the boundary is forced to exist to accommodate the topological change.

This explains:
- Why topological insulators have conducting surface states.
- Why topological superconductors have Majorana zero modes.
- Why 3He-A has Andreev bound states.

### Part IV: Anomalies and Topological Invariants

#### Chiral Anomaly

The divergence of the axial current (chiral current) is:

$$\partial_\mu j_A^\mu = \frac{1}{2\pi} \epsilon^{\mu\nu\rho\sigma} \text{Tr}(F_{\mu\nu} F_{\rho\sigma})$$

where $F_{\mu\nu}$ is the gauge field strength.

In a topological superfluid or superconductor, the "gauge field" is the effective spin-orbit coupling or electromagnetic field. The anomaly manifests as a non-conservation of fermionic number (baryon number violation, lepton number violation, etc.).

#### Anomalous Transport

Anomalies induce anomalous transport coefficients — responses that are independent of the microscopic scattering rate and depend only on topological invariants.

Examples:
- **Chiral magnetic effect**: A current proportional to the magnetic field, independent of disorder.
- **Anomalous Hall effect**: Hall conductivity quantized by the Chern number.
- **Gravitational anomalies**: Thermal transport coupled to curvature via a topological term.

In 3He-A, the chiral anomaly leads to:

$$j_A = \frac{e B}{2\pi} \text{Tr} [\gamma^5 Q]$$

where $Q$ is the spin operator, giving an anomalous spin current in the presence of a magnetic field.

### Part V: Universality and Classification

#### Topological Phase Diagram

A topological material is classified by:

1. **Symmetry class**: Time-reversal (T), particle-hole (C), or chiral (S) symmetries.
2. **Space dimension** $D$: 1D, 2D, 3D, etc.
3. **Topological invariant**: Integer (Z), mod 2 (Z_2), or other abelian group.

The **Altland-Zirnbauer classification** organizes all possibilities into a table:

| Class | $T^2$ | $C^2$ | D=1 | D=2 | D=3 |
|:-----:|:-----:|:-----:|:----:|:----:|:----:|
| A | 0 | 0 | 0 | Z | 0 |
| AIII | 0 | 0 | Z | 0 | Z |
| AI | + | - | Z | 0 | 0 |
| BDI | + | + | Z | Z | 0 |
| ... | ... | ... | ... | ... | ... |

Each entry is the topological invariant: Z means integer invariant (multiple phases); Z_2 means mod 2 (two phases); 0 means no topological distinction.

**3He-A is in class BDI** (has particle-hole, time-reversal, and chiral symmetries). It has one Dirac line in 3D, and the topological structure is robust against any symmetric perturbation.

**3He-B is in class D** (has particle-hole but not time-reversal symmetry). It is fully gapped, topologically trivial.

---

## Key Results

1. **Topological classification determines all phases of matter**: Discrete symmetries and dimension, not energy scales, define universality classes.

2. **Bulk-surface and bulk-vortex correspondences are universal laws**: Topological invariants predict the number of bound states at boundaries and in defects.

3. **Multiple types of anomalies appear**: Chiral, gravitational, and mixed anomalies are manifestations of topological structure.

4. **Topological defects (vortices, skyrmions, domain walls) host zero modes**: These modes are protected by topology and cannot be gapped without breaking symmetries.

5. **3He-A is topologically non-trivial; 3He-B is topologically trivial**: This explains their different spectroscopic and transport properties.

6. **The framework extends to all topological materials**: Graphene, topological insulators, Weyl semimetals, etc., all fit the unified picture.

---

## Impact and Legacy

This 2019 review synthesized Volovik's 30+ years of research on topological superfluids. Subsequent developments:

- **Topological quantum computing**: Majorana zero modes as non-abelian qubits.

- **Quantum anomalous Hall effect**: Experimental realizations of anomaly-induced transport in real materials.

- **Topological photonics and acoustics**: Extension of topological classification to photons and phonons.

- **High-temperature superconductivity**: Topological aspects of cuprate and iron-based superconductors.

- **Moiré materials**: Twisted bilayer graphene and other van der Waals materials as new platforms for topological phases.

---

## Connection to Phonon-Exflation Framework

The topological superfluid framework is the **theoretical foundation for phonon-exflation**:

1. **BCS condensate as topologically nontrivial state**: The K_7 condensate on SU(3) is a p-wave-like pairing state with nontrivial momentum-space topology (gap nodes, Dirac points).

2. **Particles as Dirac/Weyl fermions**: The phononic excitations of the condensate are Dirac fermions near the Fermi points, analogous to electrons in graphene or quasiparticles in 3He-A.

3. **Topological protection of gaplessness**: The masslessness of particles is protected by topological invariants of the condensate, not by symmetries. This explains why particles remain massless across cosmic evolution (until a topological transition).

4. **Defects and cosmological singularities**: Topological defects in the K_7 condensate (instantons, monopoles, vortices) are analogs of cosmic strings and domain walls. They carry zero modes and affect cosmological dynamics.

5. **Anomalies and baryon asymmetry**: The chiral anomaly mechanism (Volovik's 1998 paper) shows how baryon asymmetry can arise from topological defects in the condensate.

6. **Bulk-defect correspondence = CPT symmetry**: The topological bulk-vortex correspondence in 3He analogs to the [iK_7, D_K] = 0 symmetry that protects CPT in phonon-exflation.

7. **Classification table predicts particle spectrum**: Applying the Altland-Zirnbauer classification to the K_7 condensate should predict the number of fermion families and their topological properties.

---

## References

- Volovik, G. E. (2019). "Topological superfluids." *JETP*, 156(4), 700-706. arXiv:1602.02595.

- Altland, A., & Zirnbauer, M. R. (1997). "Nonstandard symmetry classes in mesoscopic normal-superconductor hybrid structures." *Physical Review B*, 55(3), 1142.

- Hasan, M. Z., & Kane, C. L. (2010). "Colloquium: Topological insulators." *Reviews of Modern Physics*, 82(4), 3045.

- Volovik, G. E. (2003). "Exotic properties of superfluid 3He." World Scientific, Singapore. (Monograph)
