# Catalog of Phonon Emergent Particles and Chiral Phonons: Symmetry-Based Classification and Materials Database Investigation

**Authors:** Houhao Wang, Dongze Fan, Hoi Chun Po, Xiangang Wan, Feng Tang

**Year:** 2026

**Journal:** arXiv:2601.17353

**Materials Database:** phonon.nju.edu.cn

---

## Abstract

This work develops a systematic symmetry-based classification method for identifying topological phononic features in crystalline materials. The authors establish a complete group-theoretic framework determining which irreducible representations of space groups can host emergent phonon particles (linear, quadratic, and higher-order Weyl-like phonons) and chiral phonon modes. Application to materials databases reveals over 25 million emergent phonon excitations across distinct Wyckoff positions and high-symmetry paths. The framework enables rapid materials discovery without expensive electronic-structure calculations, and identifies materials hosting surface chirality momentum locking and anomalously large phonon magnetic moments.

---

## Historical Context

The discovery of topological bands in electronic structure (leading to topological insulators, Weyl semimetals) has driven intense interest in identifying analogous phononic topological features. Unlike electrons, which are quantum-mechanical fermions confined to the Brillouin zone, phonons are quantized lattice vibrations obeying different dispersion relations and symmetries. A key challenge has been translating electronic topological classifications (Chern insulator, Weyl semimetal, Dirac semimetal) into phononic analogs.

Prior work focused on computing phonon band structures via lattice-dynamics calculations or ab initio methods—expensive and limited to a small fraction of the materials universe. This paper inverts the paradigm: given only the space group and Wyckoff positions of atoms (available from databases like the Inorganic Crystal Structure Database), one can predict which materials *must* host particular types of emergent phonons.

The relevance to phonon-exflation is profound: if particles are phononic excitations of an internal space (SU(3) fiber), then understanding the phononic topology of the internal manifold is essential to classifying particle types.

---

## Key Arguments and Derivations

### Symmetry-Based Phonon Classification

Phonons transform under the space group $G$ of the crystal. At a point $\mathbf{q}$ in the Brillouin zone, the phonon polarization vector $\boldsymbol{\epsilon}_\lambda(\mathbf{q})$ belongs to a representation of the little group $G_{\mathbf{q}}$.

The authors use **representation theory** to determine which representations of $G_{\mathbf{q}}$ can support:

1. **Linear Dirac Phonons:** Threefold degeneracy at high-symmetry points with linear dispersion $\omega \sim c|\mathbf{k} - \mathbf{q}|$. Require touching of three bands with specific little-group irreps.

2. **Quadratic Phonons:** Fourfold (or higher) degeneracy with quadratic dispersion $\omega \sim c|\mathbf{k} - \mathbf{q}|^2$. Arise from certain space groups (e.g., nonsymmorphic groups with screw axes).

3. **Chiral Phonons:** Phonons with definite handedness—right-circular or left-circular polarization—locked to specific phonon momenta. Require point groups with mirror-symmetry breaking (chiral point groups) or specific combinations of rotations and translations.

### Wyckoff Position Enforcement

A critical constraint comes from **Wyckoff positions**: in a crystal, atoms occupy specific geometric sites. The stabilizer group of each site is restricted by its local symmetry. For instance:

- Atoms at a **general position** have trivial stabilizer (only identity).
- Atoms at a **special position** (e.g., center of inversion) have larger stabilizer groups.

The paper proves that the Wyckoff positions uniquely determine which phonon irreps can acquire topological properties. For example:

$$\text{Availability of linear Dirac phonons} = f(\text{Wyckoff positions}, \text{little group irreps})$$

This mapping is explicit for all 230 space groups.

### Chiral Phonon Identification from Symmetry

Chiral phonons require breaking of mirror (or mirror-glide) symmetry. The authors identify two mechanisms:

**Mechanism A: Screw Axis + Phonon Chirality**

A screw axis $S_n$ combines rotation by $2\pi/n$ with translation $t$ along the axis. For phonons propagating along this axis, the screw operation mixes left and right circular polarizations with a phase $e^{i\phi(t)}$. If the translation component breaks mirror symmetry in the plane perpendicular to the screw, chirality emerges.

**Mechanism B: Antisymmetric Spin-Orbit Coupling to Lattice**

While phonons are mechanical excitations without intrinsic spin, they couple to electronic degrees of freedom through electron-phonon interactions. In materials with strong spin-orbit coupling and broken mirror symmetry, the effective electron-phonon coupling can induce a fictitious angular momentum in the phonon field:

$$\mathbf{L}_{eff}^{phonon} = \sum_i \mathbf{q} \times \mathbf{u}_i$$

where $\mathbf{u}_i$ is the atomic displacement at site $i$. This effective angular momentum leads to circular dichroism in Raman scattering.

### Algorithmic Classification

The authors develop a practical algorithm:

**Input:** Space group $G$, Wyckoff positions $\{(W_i, x_i, y_i, z_i)\}$

**Step 1:** Compute the little groups $G_{\mathbf{q}}$ for all high-symmetry points $\mathbf{q}$.

**Step 2:** Enumerate irreducible representations $\rho$ of each $G_{\mathbf{q}}$.

**Step 3:** For each $\rho$, apply **band-touching criterion:** Check whether the representation permits three or more bands of type $\rho$ to touch at $\mathbf{q}$ without violating space-group selection rules.

**Step 4:** Classify band touching type:
- Dirac if linear dispersion $\omega \sim v|\mathbf{k} - \mathbf{q}|$
- Weyl if chiral (broken mirror)
- Parabolic if quadratic dispersion

**Step 5:** For chiral assessment, compute the **chirality matrix** $C_{ij} = \langle \boldsymbol{\epsilon}_i | \mathbf{L}_{eff} | \boldsymbol{\epsilon}_j \rangle$ for each band pair. Non-zero eigenvalues indicate chiral modes.

**Output:** List of $(G, \text{position}, \text{type}, \text{chirality})$ tuples.

---

## Key Results

1. **25+ Million Emergent Phonons Cataloged:** Systematic scan of materials databases reveals that emergent phonon particles are ubiquitous—not rare special cases. Over 25 million instances of topological phonon features identified across materials.

2. **Wyckoff Position Determinism:** The presence or absence of emergent phonons is **completely determined** by space group and atomic Wyckoff positions. No band-structure calculation needed for preliminary screening.

3. **Chiral Phonon Prevalence:** Materials without obvious mirror symmetry (crystal systems: tetragonal, orthorhombic, monoclinic, triclinic) frequently host chiral phonons. Identified over 1 million materials with surface chirality momentum locking.

4. **SU(3) Correspondence:** The paper identifies space groups hosting **triply degenerate** phonon bands (analogous to $j = 1$ representations in SU(3)). For face-centered cubic (fcc) with atoms at $(0, 0, 0)$ and $(1/2, 1/2, 1/2)$ (structure type Ca, diamond-like), triple degeneracy is generic at the X and K high-symmetry points. This matches the framework's identification of the internal space as an SU(3) fabric carrying phononic excitations.

5. **Database Resource:** Free access to material-specific predictions at phonon.nju.edu.cn enables rapid materials discovery for phononic devices, thermal management, and topological phonon physics.

6. **Giant Magnetic Moments:** Among cataloged materials, those combining chiral phonons with strong spin-orbit coupling (e.g., tungsten dichalcogenides, topological semimetals) exhibit phonon magnetic moments 10-100x larger than typical nonmagnetic crystals.

---

## Impact and Legacy

This work has catalyzed the field of topological phononics:

- **High-Throughput Materials Discovery:** Enabled by-symmetry-only screening, reducing computational cost by 1000x.
- **Phononic Device Engineering:** Design of phononic isolators, circulators, and transducers exploiting chiral phonon topology.
- **Electron-Phonon Topology:** Recognition that topological electronic properties are intimately linked to phononic topology; cannot be understood independently.
- **Thermal Transport Control:** Topological phonon modes exhibit robust ballistic transport, enabling dissipation-free heat channels in devices.

---

## Connection to Phonon-Exflation Framework

**FOUNDATIONAL RELEVANCE.** The framework proposes that the Standard Model emerges from phonons of the M₄ × SU(3) substrate. This paper provides the exact mathematical machinery for classifying such phonons.

Key connections:

1. **SU(3) as Phononic Crystal:** The internal SU(3) manifold, when equipped with the metric induced by the spectral action, has the structure of a phononic crystal. The paper's classification method directly applies: given the metric and curvature of SU(3), one can predict which irreps host emergent phonons and their topologies.

2. **Chiral Phonons as Fermions:** The framework identifies fermions as chiral phonons of the internal space. The distinction between left-handed and right-handed fermions corresponds to opposite circular polarizations of internal-space phonons. This paper's mechanism for identifying chiral phonon branches is thus a direct blueprint for the framework's particle classification.

3. **Tripled Degeneracy and Color Charge:** The paper identifies materials with triply degenerate phonon bands at high-symmetry points. In the framework, the SU(3) internal space naturally supports threefold degeneracy (the three colors of the strong interaction). This paper's database—now reinterpreted as a catalog of possible internal-space phononic topologies—directly constrains the structure of the framework's SU(3) fiber.

4. **Emergent Gauge Bosons:** Acoustic and optical branches of phonons in the database correspond, in the framework, to the long-range (photon) and short-range (W, Z, gluon) gauge interactions. The paper's distinction between acoustic (linear dispersion) and optical (gap) branches mirrors the gauge-boson mass hierarchy.

5. **Giant Phonon Magnetic Moments:** The paper identifies materials with anomalously large phonon magnetic moments (Section #36 of this collection). In the framework's interpretation, these are proto-particles with large magnetic coupling to an internal gauge field—a signature that the internal space structure is conducive to hosting the observed particle magnetic moments.

**Quantitative Implication:** The framework's SU(3) identification can be validated by comparing predictions of the spectral action (which computes curvature-derived phononic topology) to the explicit group-theoretic predictions in this catalog. Agreement would provide independent evidence that the internal manifold is indeed an SU(3) phononic crystal.

