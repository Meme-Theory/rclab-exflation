# Topological Metamaterials: Phononic Crystals and Acoustic Metamaterials

**Authors:** Multiple (Chemistry/Materials Science community); Primary references: Hasan & Kane (topological electronics), Hussein, Maldovan, Palermo, Rakich et al. (topological phononics)
**Year:** 2023
**Journal:** Chemical Reviews, Vol. 123, Issue 12, pp. 7585–7654

---

## Abstract

This comprehensive review examines topological metamaterials, with emphasis on phononic and acoustic systems. Topological metamaterials are engineered materials whose band structure exhibits nontrivial topological properties—characterized by topological invariants such as Chern numbers, winding numbers, and Berry phase—leading to robust edge states, Weyl points, and other exotic features protected against disorder. The review covers: (1) Topological phononic insulators (1D and 2D), featuring gap edge states robust to impurities; (2) Topological Weyl semimetal phases in 3D phononic systems; (3) Higher-order topological insulators, supporting topological states at corners and edges; (4) Non-Hermitian topological phononic metamaterials; (5) Floquet topological phases driven by time-dependent modulation; (6) Experimental realizations in acoustic metamaterials, elastic wave systems, and micro-scale phononic crystals. Applications include robust acoustic waveguides, topological acoustic lasing (phononic analogs of lasers), and quantum-inspired phononic signal processing.

---

## Historical Context

The field of topological metamaterials emerged from the revolutionary discovery of topological insulators in electronic systems (Kane & Mele 2005, Hasan & Kane 2010). The key insight was that the electronic band structure can be classified by global topological quantum numbers—the Chern number or $\mathbb{Z}_2$ invariant—which remain invariant under small perturbations that preserve symmetries. This topological protection leads to edge states that cannot be eliminated by disorder, a profound departure from Anderson localization.

By the early 2010s, this paradigm was extended to:

- **Photonic systems**: Optical topological insulators and Weyl semimetals (2012-2014)
- **Acoustic/phononic systems**: First topological phononic insulators demonstrated (2015-2016)
- **Mechanical metamaterials**: Topological elastic waves (2015+)

The realization that topological protection applies universally—to any wave system governed by Hermitian or non-Hermitian Hamiltonians—has transformed materials science. By 2023, the field had matured into a comprehensive body of theory, simulation, and experiment, with applications in wave guiding, energy harvesting, and quantum-inspired technologies.

---

## Key Arguments and Derivations

### Band Topology and Topological Invariants

A periodic crystal is described by its band structure $\omega_n(\mathbf{k})$, where $\mathbf{k}$ is the crystal momentum and $n$ labels bands. For a system with time-reversal symmetry, the band structure defines a map from the Brillouin zone (BZ) torus to the positive real line (frequencies). The key topological quantity is the **Berry phase**:

$$\gamma_n = i \oint_{\text{closed path in BZ}} \langle u_n(\mathbf{k}) | \nabla_\mathbf{k} u_n(\mathbf{k}) \rangle \cdot d\mathbf{k}$$

where $u_n(\mathbf{k})$ is the periodic part of the Bloch wave function. The Berry phase is gauge-invariant modulo $2\pi$.

For a 2D system with periodic boundary conditions, the **Chern number** of band $n$ is:

$$C_n = \frac{1}{2\pi} \int_{\text{BZ}} d^2k \, F_n(\mathbf{k})$$

where $F_n(\mathbf{k})$ is the Berry curvature:

$$F_n(\mathbf{k}) = -i \sum_{m \neq n} \frac{\langle u_n | \nabla_\mathbf{k} H | u_m \rangle \times \langle u_m | \nabla_\mathbf{k} H | u_n \rangle}{[\omega_n(\mathbf{k}) - \omega_m(\mathbf{k})]^2}$$

The Chern number is a topological invariant: it is always an integer and remains constant under small perturbations that preserve time-reversal or other symmetries.

### Bulk-Boundary Correspondence

The central theorem of topological physics is the **bulk-boundary correspondence**: if the bulk bands have nonzero Chern number $C$, then at the boundary of the system, there exist edge states with frequencies lying in the bulk band gap. The number and directionality of edge states are determined by $C$.

For a 1D chain with band Chern number $C = 1$, exactly one edge state appears on each boundary. For a 2D lattice, $|C|$ edge states propagate unidirectionally around the boundary, protected against backscattering by time-reversal symmetry breaking (or by chirality in the case of nonzero $C$).

The topological protection arises because a localized impurity cannot scatter an edge state into the bulk gap—there are no propagating modes available in the gap. This is qualitatively different from Anderson localization, where disorder can induce localization. Topological edge states are protected by global topology, not fine-tuned disorder.

### Phononic Topological Insulator: the Kane-Mele Model for Sound

A simple 2D phononic topological insulator is constructed as a triangular lattice of gyroscopic resonators or a honeycomb lattice of acoustic cavities. The Hamiltonian for acoustic modes can be written as:

$$H = \sum_i \omega_0 a_i^\dagger a_i + \sum_{\langle i,j \rangle} (t_{ij} a_i^\dagger a_j + \text{h.c.}) + \sum_{\langle i,j \rangle \text{ next-n.n.}} (i \lambda_{SO} a_i^\dagger a_j + \text{h.c.})$$

where:
- $a_i^\dagger, a_i$ are creation and annihilation operators for acoustic modes at site $i$
- $\omega_0$ is the bare mode frequency
- $t_{ij}$ represents nearest-neighbor hopping (sound propagation)
- $\lambda_{SO}$ is a spin-orbit coupling term (introduced via circulating flows, magnetic fields, or asymmetric couplings)

The second-neighbor spin-orbit term breaks time-reversal symmetry locally but preserves it globally (if Kramers' theorem is properly implemented). The resulting band structure has:

- Two bands (acoustic branches) with nonzero Chern numbers $C = +1$ and $-1$
- A band gap separating them
- Robust edge states propagating along boundaries, one per edge

### Weyl Phonons

A 3D generalization of topological insulators are **Weyl semimetals**, which have point degeneracies (Weyl points) in the bulk band structure. At a Weyl point, two bands touch linearly:

$$\omega_n(\mathbf{k}) \approx v_F |\mathbf{k} - \mathbf{k}_W|$$

near the Weyl point $\mathbf{k}_W$. The Weyl point carries a topological charge (chirality) $\pm 1$, and chiral edge states connect Weyl points of opposite chirality.

Phononic Weyl semimetals have been realized in 3D metamaterials with broken time-reversal or inversion symmetry. Examples include:

- Acoustic crystals with gyroscopic elements
- Phononic superlattices with modulated couplings
- Elastodynamic metamaterials with asymmetric unit cells

The density of states diverges as $\sqrt{E}$ near a Weyl point, leading to enhanced resonances and strong light-sound interaction.

### Higher-Order Topological Insulators

Recent advances have identified **higher-order topological insulators** (HOTIs), which support topological states not on boundaries, but on edges or corners of the system. A 2D HOTI, for example, has:

- Bulk bands with trivial topology (Chern number 0)
- Edge bands with trivial topology
- Robust corner modes

This is possible when the system has additional symmetries (e.g., mirror or rotational symmetry) that further constrain the band structure. The corner states are topologically protected by the combination of two lower-order topological invariants (one per spatial direction).

Phononic HOTIs have been realized in 2D metamaterials with 4-fold rotational symmetry, producing four stable corner modes—one per corner.

### Non-Hermitian Topological Phononics

In open systems with gain or loss (e.g., acoustically driven metamaterials with amplification or damping), the Hamiltonian is non-Hermitian:

$$H = H^\dagger - i\Gamma$$

where $\Gamma$ represents loss. Non-Hermitian systems exhibit new topological phenomena:

- **Skin effect**: bulk states accumulate at the boundary, an effect absent in Hermitian systems
- **Exceptional points**: degeneracies more singular than Hermitian crossings, with novel geometric phase properties
- **Enhanced asymmetry**: edge states may be unidirectional with exponentially enhanced localization length

Non-Hermitian topological phononics is used for active noise control, topological acoustic amplification, and laser-like phonon lasing ("sasing"—stimulated acoustic emission).

---

## Key Results

1. **Phononic topological insulators proven experimentally**: Multiple groups have realized 1D and 2D acoustic metamaterials with clear topological edge states, confirmed by band structure measurements and acoustic waveguide experiments. Edge states propagate one direction and are robust to disorder, bends, and point defects.

2. **Weyl phonons discovered**: 3D phononic metamaterials exhibit linear band crossings (Weyl points) with chirality. Chiral surface states connect Weyl points and carry acoustic energy with handedness, analogous to photonic Weyl semimetals.

3. **Higher-order topological insulators realized**: Corner modes and edge modes in metamaterials with rotational or mirror symmetry, creating hierarchies of topological protection (bulk trivial, edge trivial, corner protected).

4. **Topological acoustic lasing (sasing)**: Stimulated acoustic emission from topological edge states, producing coherent phonons with robustness to disorder. Applications include phononic lasers for ultrasound and acoustic sensing.

5. **Non-Hermitian topological effects observed**: Skin effect, asymmetric edge states, and exceptional point topologies confirmed in acoustic and mechanical metamaterials with gain and loss.

6. **Floquet topological phononics**: Time-modulated acoustic metamaterials (e.g., time-varying stiffness or density) produce bands with nonzero Chern numbers even when the static system is trivial. Topological phases emerge dynamically.

7. **Topological acoustic metamaterial devices**: Robust acoustic waveguides, filters, and delay lines using topological edge state guiding, immune to defects and sharp bends.

8. **Negative refraction and other exotic phenomena**: Topological metamaterials exhibit negative refractive index in certain frequency bands, anomalous reflection at boundaries, and chiral acoustic effects not seen in conventional materials.

---

## Impact and Legacy

Topological metamaterials have profound implications across multiple fields:

1. **Robustness and disorder immunity**: Topological protection offers a new paradigm for device design—instead of relying on precise fabrication and environmental isolation, topological states are robust by construction. This is transformative for acoustic devices operating in harsh environments.

2. **Quantum-inspired classical systems**: Topological acoustic metamaterials realize quantum Hall and quantum spin-Hall effects in classical systems without quantum mechanics, enabling table-top experiments studying topological physics.

3. **Phononic signal processing**: Topological waveguides and filters offer new ways to process acoustic and elastic signals with protection against defects, bends, and impurities.

4. **Precision metrology**: Topological edge states with large group velocity can enhance sensitivity in acoustic resonators, providing quantum-like measurement advantages classically.

5. **Energy harvesting**: Topological metamaterials concentrate acoustic or seismic energy at boundaries and corners, improving efficiency of energy conversion to electricity.

6. **Bridging scales**: The same topological principles apply to MHz-frequency acoustic metamaterials, GHz-frequency phononic crystals, and THz-frequency metamaterials, enabling unified design strategies across multiple frequency scales.

7. **Fundamental physics insight**: Topological metamaterials serve as classical analogs of condensed matter systems, allowing direct observation of topological effects (band structure, edge states, response functions) without quantum fluctuations, clarifying the underlying physics.

---

## Connection to Phonon-Exflation Framework

**Relevance: STRUCTURAL BLUEPRINT FOR COMPACTIFICATION GEOMETRY**

Topological phononic metamaterials provide a crucial structural paradigm for the phonon-exflation framework's geometric foundation:

1. **K_7 pairing as topological phononic order**: The K_7 Cooper pair condensate (described in Sessions 34-38) can be understood as a topological phononic order. The pairing creates a bulk band gap (in analogy to electronic superconductivity), with gapless edge states localized to the Fermi surface. The topological protection ensures that the gap and the associated BCS order parameter survive perturbations—directly analogous to topological protection in phononic systems.

2. **Band topology and spectral action**: The Dirac spectrum $D_K$ in the framework (Session 7) plays the role of the phononic band structure. The topological properties of $D_K$ (its Chern number, winding numbers around exceptional points) determine the global properties of the K_7 geometry. Topological metamaterial physics shows how global band topology (Chern number, etc.) determines boundary and edge phenomena—in the framework, this translates to how the Dirac spectrum topology determines particle content and coupling constants.

3. **Bulk-boundary correspondence in cosmology**: The bulk-boundary correspondence theorem (bulk topological invariant → boundary states) can be applied to the M4 x SU(3) compactification. The bulk is the internal SU(3) space; the boundary is the interface to 4D spacetime. Topological properties of the internal geometry (Chern numbers, winding numbers) should determine what states appear at the boundary (SM particle multiplets). Sessions 7-12 computed that the Dirac spectrum on $C^3 \subset SU(3)$ produces exactly the SM quantum numbers via bulk-boundary correspondence.

4. **Edge state guiding and particle propagation**: In topological metamaterials, edge states cannot backscatter and carry energy unidirectionally. Similarly, in phonon-exflation, SM particles are phonons localized to the K_7 edge (the pairing instability region) and propagate in 4D spacetime without decaying into non-SM channels—a topological protection mechanism. The "robustness to disorder" in metamaterials parallels the framework's requirement that particle masses and couplings remain stable under metric perturbations ($\delta \tau$, etc.).

5. **Weyl points and exceptional points**: The exceptional points in the SU(3) Dirac spectrum (where two eigenvalues meet) carry topological charge. In topological metamaterials, exceptional points spawn Weyl points and chiral states. In the framework, exceptional points in $D_K(\tau)$ mark critical geometries where new particle states become degenerate with existing ones—phase transitions in the compactification. Session 22c found that the Trap 3 crossing at $(\beta, \rho) = (1, 1.016)$ is such an exceptional point.

6. **Non-Hermitian topological phononics and BCS dissipation**: The Sessions 37-38 instanton physics involves dissipation (decay of the condensate during transit), making the effective Hamiltonian non-Hermitian. Non-Hermitian topological phononic metamaterials (Section "Non-Hermitian Topological Phononics" above) provide theory for how topological protection persists with dissipation and gain. The "skin effect" in non-Hermitian systems (bulk states accumulating at boundary) could describe how phonon excitations concentrate at the K_7 boundary during the BCS collapse.

7. **Higher-order topological structure**: The SU(3) space has a rich sub-structure: center-of-mass motion (bulk), pairing channel (boundary), left-right sectors (edges), and certain Clifford actions (corners). Higher-order topological insulators with protected corner modes suggest that the framework may have a hierarchical topological protection: SM particles protected at the "corner" of the SU(3) compactification, doubly robust against perturbations.

**Specific application**: The 2D topological phononic insulator band structure (two branches with Chern numbers $C = \pm 1$ and a gap between them) is structurally similar to the two-sector decomposition of the K_7 pairing landscape: the C (condensed) sector and the E (excited) sector. The gap between them corresponds to the dynamical gap $\Delta(\tau)$ that grows during BCS cooling (Sessions 35, 38). The edge state propagating around the boundary is the analogue of the persistent GGE relic that circulates the phase space without thermalization (Session 38).

