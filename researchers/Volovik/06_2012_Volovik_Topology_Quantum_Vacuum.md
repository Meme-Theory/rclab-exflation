# Topology of Quantum Vacuum

**Author(s):** Grigory E. Volovik
**Year:** 2012
**Journal:** Chapter in *Analogue Gravity Phenomenology* (Springer)
**arXiv:** 1111.4627

---

## Abstract

This comprehensive review expands Volovik's topological approach to the quantum vacuum, treating it as a topological material with gapless excitations protected by momentum-space topology. The paper demonstrates that:

- Topology in momentum space is the primary characteristic of ground states and quantum vacua
- Topological protection ensures that gaplessness of fermions is robust against microscopic deformations
- The Standard Model's vacuum is topologically equivalent to topological superfluids, superconductors, and insulators
- Topological invariants (winding numbers, Chern numbers, etc.) determine universality classes and emergent low-energy effective theories
- These invariants explain the emergence of Lorentz invariance, gauge fields, and gravitational fields
- Several scenarios of Lorentz violation are explored and constrained
- Bulk-surface and bulk-vortex correspondences provide dualities connecting momentum space to real space

The paper presents a unifying framework: **the quantum vacuum is topological matter**. This perspective resolves longstanding puzzles in quantum gravity and particle physics by showing that low-energy physics depends only on topological invariants, not on trans-Planckian details.

---

## Historical Context

The concept of topology in physics underwent a dramatic evolution in the 20th and 21st centuries:

### Early Topological Ideas (1950s-1980s)

- **Monopoles and topological defects** (Yang, Dirac, 't Hooft, Polyakov): Classical field configurations with nontrivial topology, stable by topological conservation laws.

- **Chern number** (Chern, 1946; rediscovered in physics by Thouless et al., 1982): A topological invariant quantifying the total "twisting" of a vector bundle. In condensed matter, the Chern number of the electron wavefunction determines the Hall conductivity.

- **Quantum Hall effect** (von Klitzing, 1980; Laughlin, 1983): Integer and fractional quantization of Hall conductance arise from the topology of the filled Landau level.

### Topological Phases (1990s-2000s)

- **Topological superconductivity** (Volovik, Salomaa, 1987): Superconductors with gap nodes are topologically nontrivial; gapless fermions exist at surfaces and in vortex cores.

- **Topological insulators** (Kane-Mele, 2005; Hasan-Kane, 2010): Insulators with insulating bulk but conducting surface states, protected by topology.

- **Weyl fermions** (Volovik, Kopnin, 2003; Wan, Turner, Vishwanath, 2011): Materials with point nodes in the electronic spectrum, protected by certain symmetries.

### Volovik's Unification (2000s-2010s)

Volovik realized that topological classification provides a **universal framework** for understanding gapless and gapped phases in any dimension. His 2012 review synthesizes this into a coherent program connecting condensed matter, high-energy physics, and gravity.

---

## Key Arguments and Derivations

### Part I: Classification of Topological Matter

#### Universality Classes and Symmetries

A topological material is classified by:

1. **Dimension** $D$ of the real space
2. **Dimension** $d$ of the gapless features in momentum space (co-dimension = $D - d$)
3. **Discrete symmetries** (time-reversal $T$, particle-hole $C$, chiral $S = CT$)
4. **Continuous symmetries** (gauge, global)

For each combination, there exists a **topological invariant** — an integer or topological number that cannot change smoothly.

**Example: Fermi Surface (d=3)**
- In 3D space with a gapless 3D Fermi surface, the invariant is the genus of the surface (a topological number counting "handles").
- The Fermi surface cannot be gapped without closing or merging with another surface (topology forbids smooth deformation).

**Example: Weyl Point (d=0)**
- In 3D space with a 0-dimensional Weyl fermion node, the invariant is the **chirality** $\nu = \pm 1$ (winding number).
- The point node cannot be gapped without a symmetry-breaking deformation.

#### Altland-Zirnbauer Classification

The Altland-Zirnbauer (AZ) classification organizes all topological insulators and superconductors by three discrete symmetries:

| $T^2$ | $C^2$ | $S^2$ | 1D | 2D | 3D |
|:-----:|:-----:|:-----:|:----:|:----:|:----:|
| 0 | 0 | 0 | Z | 0 | 0 |
| + | 0 | 0 | Z | Z | 0 |
| - | 0 | 0 | 0 | Z | Z |
| + | + | - | Z | 0 | Z |
| ... | ... | ... | ... | ... | ... |

Each entry denotes the **topological invariant** for the corresponding dimension. Z means the invariant is an integer (multiple types of topological phases); 0 means no topological distinction.

The AZ table was developed for condensed matter but applies universally: **The Standard Model vacuum can be placed on this table**.

### Part II: Topological Protection

#### Winding Number for Fermi Points

For a 3D system with a point node (Fermi point or Weyl point), the topological invariant is the **winding number**:

$$\nu = \frac{1}{2\pi i} \oint_{S^2} d^2 k \, \text{Tr} \left[ \hat{P}({\bf k}) \nabla_{\bf k} \hat{P}({\bf k}) \right]$$

where $\hat{P}({\bf k})$ is the projector onto the occupied (or unoccupied) states near the node, and the integral is over a small 2-sphere surrounding the node in momentum space.

For a simple Dirac point with two-fold degeneracy, $\nu = \pm 1$. This integer is **conserved under smooth deformations** of the Hamiltonian that preserve the protecting symmetry.

Consequence: A perturbation that respects the symmetry cannot gap out the node. The gaplessness is **topologically protected**.

#### Bulk-Surface Correspondence

One of the deepest results in topological matter: **If the bulk has a topological invariant $\nu \neq 0$, then the surface must have gapless (or special) states**.

This is the **index theorem** in condensed matter form. For Weyl fermions:

- A 3D bulk with Weyl point (chirality $\nu$) has a **Fermi arc** on the 2D surface — a gapless curve in the surface Brillouin zone.
- The arc is topologically forced: it cannot be gapped while preserving the surface periodicity.

#### Bulk-Vortex Correspondence

Similarly, inside a vortex defect in a topologically nontrivial superfluid, **zero modes (gapless states) exist**. The number of zero modes is determined by the bulk topological invariant.

**Example (3He-B superfluid)**:
- Bulk: Topologically nontrivial (chiral p-wave pairing), Weyl fermions in bulk spectrum.
- Vortex: Bound states (Majorana zero modes) form on the vortex core, protected by the bulk topology.

### Part III: Emergence of Lorentz Invariance

#### Near a Fermi Point

Consider fermions in a superfluid or condensed matter system. Near a point node in momentum space, expand the Hamiltonian:

$$H({\bf k}) = v_i \sigma^i k_i + \text{higher order terms}$$

where $v_i$ are the Fermi velocities (can be anisotropic in general). The spectrum is:

$$E({\bf k}) = \pm \sqrt{(v_x k_x)^2 + (v_y k_y)^2 + (v_z k_z)^2}$$

If the Fermi velocities are equal, $v_x = v_y = v_z = v_F$ (isotropy enforced by symmetry), the spectrum becomes:

$$E({\bf k}) = \pm v_F |\mathbf{k}|$$

This is exactly the **relativistic dispersion** $E = pc$ with $v_F \to c$. Lorentz invariance emerges from the isotropic Fermi point.

#### Robustness to Anisotropy

If microscopic physics is anisotropic, the Fermi velocities are generically unequal. However, if **symmetries enforce isotropy** (e.g., cubic symmetry in a lattice), the Fermi point is isotropic.

Even if anisotropy is present at high energy, renormalization group flow typically drives the Fermi velocities to a common value at low energy. Thus, **Lorentz invariance is an emergent consequence of symmetry and RG flow**, not a fundamental assumption.

### Part IV: Gauge and Gravitational Fields

#### Emergent Gauge Fields

Suppose the condensate order parameter varies spatially: $\Psi({\bf r}) = \rho({\bf r}) e^{i\theta({\bf r})}$. This induces an effective **gauge field**:

$$A_\mu({\bf r}) = \frac{\hbar}{2m} \partial_\mu \theta({\bf r})$$

Quasiparticles couple to this field through the Pauli covariant derivative:

$$\mathbf{p} \to \mathbf{p} - \frac{e}{c} \mathbf{A}$$

The gauge field is **emergent** — it arises from the condensate structure, not a fundamental symmetry.

#### Emergent Gravity

Now allow metric fluctuations. The effective spacetime metric seen by quasiparticles is:

$$g_{\mu\nu}({\bf r}) = \begin{pmatrix} -(v_F)^2 & 0 \\ 0 & \delta_{ij} \end{pmatrix} + h_{\mu\nu}({\bf r})$$

where $h_{\mu\nu}$ represents deformations of the condensate. The Riemann curvature tensor:

$$R_{\mu\nu\rho\sigma} \propto \frac{\partial^2 h}{\partial x \partial x}$$

Feynman path integrals over quasiparticles coupled to this metric generate an effective action for the metric, analogous to the Einstein-Hilbert action.

---

## Key Results

1. **Topological invariants classify all quantum vacua**: Discrete symmetries and dimensionality determine the universality class.

2. **Gaplessness is topologically protected**: Point nodes, lines, and surfaces in the spectrum cannot be gapped if they carry nonzero topological invariants.

3. **Lorentz invariance emerges near isotropic Fermi points**: No assumption of Lorentz symmetry needed a priori; it emerges from symmetry and RG flow.

4. **Gauge and gravitational fields are emergent**: They arise as composite degrees of freedom from the quasiparticle spectrum and condensate structure.

5. **Low-energy physics is universal**: The effective theory depends only on topological invariants, making it robust to trans-Planckian details.

6. **Einstein-Cartan theory is natural**: Torsion naturally appears in emergent gravity from fermions, suggesting that Einstein-Cartan (not GR) is the correct low-energy effective theory.

7. **Standard Model vacuum as topological matter**: The particle physics vacuum is topologically equivalent to a topological superfluid, with fermion families corresponding to different topological sectors.

---

## Impact and Legacy

This 2012 review synthesized decades of topological insights. Key subsequent developments:

- **Topological insulators and Weyl semimetals** in materials (molybdenum ditelluride, tungsten ditelluride, bismuth compounds) confirmed topological predictions experimentally.

- **Quantum simulation** of topological systems in ultracold atoms and photonics.

- **Topological quantum computing**: Majorana fermions as non-abelian quantum gates.

- **AdS/CFT and holography**: Bulk topological invariants correspond to boundary entanglement structures.

- **Swampland constraints**: String theory consistency conditions align with topological stability requirements.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework is built on the principle that particle physics emerges from the topology of the K_7 BCS condensate on SU(3):

1. **Fermi points = quasiparticles**: The gapless excitations of the BCS condensate are topologically protected Fermi points, analogous to Weyl nodes in topological materials.

2. **Standard Model from topological classification**: The 16 fermion families (per generation) may arise from the topological structure of the condensate's gap nodes, with different topological sectors corresponding to different fermion types.

3. **Gauge symmetries are emergent**: SU(2) x U(1) electroweak and SU(3) strong forces may be emergent gauge fields from the condensate's order parameter structure.

4. **Gravity from topology**: The spectral action on SU(3) is the effective action for the metric emerging from the condensate's topological structure.

5. **Dark energy and topological transitions**: Cosmological evolution (changing scale of the SU(3) compactification) induces topological transitions in the condensate, visible as dark energy in the 4D effective theory.

6. **Lorentz invariance is robust**: The emergent Lorentz symmetry is insensitive to trans-Planckian details of the condensate microscopy, explaining why no Lorentz violations have been detected.

---

## References

- Volovik, G. E. (2012). "Topology of quantum vacuum." Chapter in *Analogue Gravity Phenomenology: Analogue spacetimes and horizons, from theory to experiment* (Springer). arXiv:1111.4627.

- Altland, A., & Zirnbauer, M. R. (1997). "Nonstandard symmetry classes in mesoscopic normal-superconductor hybrid structures." *Physical Review B*, 55(3), 1142.

- Hasan, M. Z., & Kane, C. L. (2010). "Colloquium: Topological insulators." *Reviews of Modern Physics*, 82(4), 3045.

- Kane, C. L., & Mele, E. J. (2005). "Quantum spin Hall effect in graphene." *Physical Review Letters*, 95(22), 226801.
