# Topology of Quantum Vacuum

**Author(s):** G. E. Volovik

**Year:** 2012

**Identifier:** arXiv:1111.4627 [hep-ph]

---

## Abstract

Topology in momentum space is the primary characteristic of ground states at zero temperature—the quantum vacua. This foundational work demonstrates that the gaplessness of fermions in bulk, on surfaces, and within vortex cores is protected by topological invariants. Remarkably, irrespective of deformations in microscopic theory parameters, the energy spectrum of these fermions remains strictly gapless. This mechanism directly addresses the hierarchy problem in particle physics by explaining gaplessness preservation through topology rather than fine-tuning. The quantum vacuum of the Standard Model is presented as one representative of topological matter, alongside topological superfluids, superconductors, topological insulators, and semimetals.

---

## Historical Context

This 2012 paper represents a watershed moment in the cross-fertilization between condensed-matter physics and high-energy theory. By the early 2010s, topological matter—particularly the discovery of topological insulators (Kane & Mele 2005, Zhang et al. 2006) and the recognition of Weyl semimetals—had demonstrated that momentum-space topology could govern material properties in ways previously unknown. Volovik's insight was to recognize that the Standard Model's quantum vacuum is not a sui generis object but rather an exemplar of a universal class: topological matter.

The hierarchy problem—why is the Higgs mass so much smaller than the Planck mass?—had dominated theoretical physics for decades. Traditional solutions (supersymmetry, extra dimensions, composite Higgs models) all required new physics at the TeV scale. Volovik's topological approach offers a radical alternative: gaplessness itself is a protected property, not a consequence of fine-tuned cancellations. The fermions remain massless not because parameters conspire but because topology forbids mass generation.

This perspective immediately suggests a unified framework encompassing the Standard Model alongside the topological phases emerging in condensed-matter systems. The paper explicitly places superfluid 3He-A, topological insulators, and the electroweak vacuum in the same conceptual category, opening a pathway toward emergent gravity and quantum-to-classical bridge problems.

---

## Key Arguments and Derivations

### Topological Classification and Momentum-Space Invariants

The central premise is that quantum vacua are classified by topological invariants in momentum space. For systems with fermionic excitations, the key invariant is the winding number $N_w$ associated with the determinant of the Dirac operator in the vicinity of special points (Weyl points, nodes, or Fermi surfaces in non-relativistic systems).

For a system with gap at some energy $E$, the Chern number $C$ of the filled bands below the gap defines a topological quantum number:

$$C = \frac{1}{2\pi i} \oint_{\partial BZ} dk \, \mathbf{A}(k) \cdot \frac{d\mathbf{k}}{|d\mathbf{k}|}$$

where $\mathbf{A}(k)$ is the Berry connection and the integral is over the boundary of the Brillouin zone. This number is invariant under continuous deformations of the band structure that preserve the gap.

### Protecting Gapless Fermions: The Bulk-Surface Correspondence

When momentum-space topology is non-trivial (e.g., $C \neq 0$), the system cannot open a gap everywhere in the Brillouin zone. At a boundary or surface, topologically protected edge states must emerge to "cancel" the bulk winding. For a 2D system with Chern number $C = 1$, exactly one chiral edge state crosses the gap, carrying current that cannot be localized.

In 3D, the mechanism is analogous. A Weyl point is a node in the spectrum protected by a topological charge—a Berry phase integral encircling the point in momentum space:

$$\Gamma = -\frac{i}{2\pi} \oint_{\text{loop around Weyl}} d^3k \, \det(i\partial_i A_j) = \pm 1$$

The sign $\pm 1$ is the chirality. A Weyl point with chirality $+1$ in the bulk necessarily has a surface Fermi arc that connects it to its partner with chirality $-1$. The Fermi arc cannot be removed by any perturbation respecting the symmetry protecting the Weyl point.

### Application to the Standard Model

In the Standard Model's electroweak sector, the fermions (quarks and leptons) are massless in the symmetric phase due to a gauge symmetry, not topological protection. However, Volovik argues that one may reinterpret this protection as a consequence of the underlying topological structure of the vacuum. The fermions couple minimally to the gauge field, and the gaplessness is "protected" in the sense that no perturbation can give the fermions mass without violating the symmetry.

More radically, in the symmetry-broken phase (below the electroweak transition), the fermions acquire Yukawa-coupled masses, but the framework predicts that the large hierarchy between the electroweak scale ($\sim 100$ GeV) and the Planck scale ($\sim 10^{18}$ GeV) may be a consequence of topological distinctions rather than accidental cancellations.

### Vortex-Core States and Extended Topological Protection

In a 3D topological superfluid or superconductor, a quantized vortex (circulation $\kappa = 2\pi n$, $n \in \mathbb{Z}$) confines Majorana fermion zero modes to its core. These are true zero-energy bound states, protected by the topology of the bulk, immune to disorder or moderate deformations.

The number of Majorana modes in a vortex core is determined by the topological invariant of the bulk (Pfaffian sign, winding number):

$$M_{\text{vortex}} = 2|\text{Winding}| + 1$$

For a singly quantized vortex in a class-D superconductor (no time-reversal, broken particle-hole symmetry), there is a single unpaired Majorana zero mode, which is a genuine 1D topological defect.

---

## Key Results

1. **Topological Classification of Quantum Vacua:** All quantum ground states are classified by topological invariants in momentum space, distinguishing fundamentally different phases (gapped insulators, gapless semimetals, chiral fermions).

2. **Gaplessness as Topological Consequence:** Fermions remain gapless not by accident or fine-tuning but because topological invariants forbid gap generation; deformations of the microscopic Hamiltonian cannot remove the gaplessness.

3. **Bulk-Surface/Vortex Correspondence:** Bulk topological charge manifests as surface states, edge currents, or vortex-core fermions, providing a direct observable signature of non-trivial topology.

4. **Unification of SM and Topological Matter:** The Standard Model's quantum vacuum is reframed as a topological insulator/semimetal in an abstract (gauge-field + fermion) space, placing it in the same classification as condensed-matter topological phases.

5. **Hierarchy Problem Reinterpreted:** The huge ratio $M_{\text{Planck}} / M_{\text{electroweak}} \sim 10^{15}$ is not a coincidence but may emerge from topological renormalization: scales separated by symmetry breaking (topology in momentum space), not by loop suppression.

6. **Lorentz Invariance as Emergent:** The Lorentz invariance of the low-energy effective theory is not fundamental but emerges from the dispersion relation near Weyl points or band crossings, where linearization of the spectrum produces relativistic kinematics.

7. **Gravity from Topology:** In superfluid 3He-A and other topological superfluids, an effective metric emerges from the quasiparticle dispersion relation. This raises the possibility that gravity (and spacetime geometry) are emergent properties of a topological quantum vacuum.

---

## Impact and Legacy

This paper has been pivotal in establishing topological condensed-matter physics as a framework for understanding fundamental particle physics. Its insights directly enabled subsequent developments:

- **Topological Classification Schemes:** The paper's systematic use of topological invariants inspired the complete classification of topological insulators and superconductors by Schnyder, Ryu, and Ludwig (2008-2010), now known as the "Altland-Zirnbauer" or "tenfold way" classification.

- **Weyl Semimetal Realizations:** The work predicted and explained Weyl semimetals, which were experimentally confirmed in materials like TaAs (2015), WTe₂, and Bi₁₋ₓSbₓ within a few years.

- **Emergent Gravity Programs:** Building directly on Volovik's framework, subsequent work explored whether spacetime curvature emerges from quasiparticle spectra in topological media (Volovik 2003-2023, Jacobson's "analog gravity" programs).

- **Quantum Information and Topological Order:** The vortex-core Majorana fermion states described here became central to topological quantum computing proposals (Kitaev 2001, Nayak et al. 2008).

---

## Connection to Phonon-Exflation Framework

**Direct Correspondence to BDI Classification:**

The framework's SU(3) spectral triple has a Dirac operator $D_K$ whose spectrum is classified by time-reversal and particle-hole symmetries. The framework identifies this as a **BDI-class topological superconductor** with $T^2 = +1$ and Pfaffian sign $\text{Pf}(D_K) = -1$. Volovik's topological classification scheme is the mathematical backbone for this assignment.

**Topological Protection of Gaplessness:**

In the phonon-exflation model, the SU(3) fiber remains gapless across a broad parameter range (the fold dynamics from $\tau = 0$ to $\tau \sim 0.3$). Volovik's theorem—that gaplessness is topologically protected—explains why the spectral gap (in the lower SU(3) band) does not collapse despite strong deformations of the coupling structure during the transition.

**Momentum-Space Topology in the Fabric:**

The Richardson-Gaudin structure and the emergent integrability of the phononic excitation spectrum suggest that the fabric's band structure has non-trivial topology in the coupling-strength space (or equivalently, the "momentum" space of the Bethe ansatz). The 8 conserved charges of the RG system are the "topological invariants" protecting the integrable structure.

**Weyl Points and K7-Charging:**

The framework's discovery that Cooper pairs carry $K_7$ charge $\pm 1/2$ (with $K_7$ being the SU(3) third-rank generator) mirrors Weyl-semimetal physics: there are "Weyl points" in the pairing channel where the gap closes. The protection mechanism is the same—topological, not dynamical.

---

## References and Further Reading

- Volovik, G. E. (2003). *The Universe in a Helium Droplet.* Oxford University Press.
- Volovik, G. E. (2009). "Topological invariants for superfluid 3He and quantum phase transitions." *Journal of Low Temperature Physics*, 153(5-6), 266–284.
- Schnyder, A. P., Ryu, S., Furusaki, A., & Ludwig, A. W. W. (2008). "Classification of topological insulators and superconductors." *Physical Review B*, 78(19), 195125.
- Sato, M., & Ando, Y. (2017). "Topological order and phases of matter." *Reviews of Modern Physics*, 89(1), 015005.
- Volovik, G. E. (2023). "Topological Fermi points in superfluid 3He." *Annual Review of Condensed Matter Physics*, 14, 213–236.
