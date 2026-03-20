# Topological Metamaterials

**Author(s):** Xiang Ni, Simon Yves, Alex Krasnok, Andrea Alù

**Year:** 2023

**Identifier:** DOI: 10.1021/acs.chemrev.2c00800

**Published in:** Chemical Reviews, Vol. 123, No. 12, pp. 7585–7654 (2023)

---

## Abstract

Topological materials—matter whose physical properties are dictated by global topological invariants rather than local details—have revolutionized condensed-matter physics and inspired rapid innovation across photonics, phononics, and metamaterials. This comprehensive review by Ni, Yves, Krasnok, and Alù synthesizes the foundations and cutting-edge developments in **topological metamaterials**: engineered structures whose band structures exhibit non-trivial topology, granting them intrinsic robustness and novel functionalities.

The review covers:

1. **Topological Foundations:** Berry phase, Chern numbers, topological invariants, and their role in protecting gapless edge states and ensuring robustness to perturbations.

2. **Topological Photonic Metamaterials:** Engineering of photonic structures with non-trivial Chern numbers and topological edge modes.

3. **Topological Phononic Metamaterials:** Analogous constructions in acoustic and mechanical systems, yielding phononic edge states, topological insulation, and protected wave transport.

4. **Design Principles:** Methods for tuning topological properties, breaking symmetries to open band gaps, and controllably generating topological phase transitions.

5. **Recent Advances:** Non-Hermitian topological metamaterials, higher-order topological insulators, topological nonlinearities, and dynamic topological systems.

6. **Applications:** Robust waveguides, topologically protected lasers, phononic edge-state waveguides, and integrated topological optical and acoustic devices.

The review emphasizes that topological order is not restricted to exotic quantum systems but can be engineered into classical metamaterials, providing a versatile platform for fundamental physics, technology, and interdisciplinary applications spanning quantum chemistry, materials science, and engineering.

---

## Historical Context

Topological insulators emerged in the early 2000s as a predicted phase of matter, followed by experimental confirmation (Zhang et al. 2006, König et al. 2007). By 2010, the topological classification scheme (Altland-Zirnbauer) had unified understanding of topological phases in electronics, photonics, and phononics.

The leap to **engineered metamaterials** came in the 2010s: researchers realized that explicitly designed electromagnetic or mechanical structures could be engineered to exhibit non-trivial topological invariants without relying on quantum effects or exotic materials. Topological photonic crystals (Hafezi et al. 2011, Wang et al. 2009) and topological phononic metamaterials (Hussein & Maldovan) followed rapidly.

By 2023, the field had matured into a well-developed discipline with numerous experimental demonstrations, theoretical refinements, and emerging applications. The Ni et al. review represents a comprehensive synthesis of this rapid development, positioning topological metamaterials as one of the major paradigm shifts in materials science and engineering of the past two decades.

---

## Key Topics and Derivations

### Topological Invariants: Berry Phase and Chern Number

The foundation of topological metamaterials is the **topological invariant**—a global property of the system that cannot change continuously but only through singular events (band touching).

**Berry Phase:** For a cyclic adiabatic evolution of a quantum state $|\psi(t)\rangle$ through a closed loop in parameter space, the wavefunction acquires a phase beyond the dynamic phase:

$$|\psi(t)\rangle = e^{i\gamma(t)} e^{-i\phi_d(t)} |\psi_0\rangle$$

where $\phi_d(t) = \int_0^t dt' E(t') / \hbar$ is the dynamic phase, and $\gamma(t)$ is the **Berry phase**:

$$\gamma = i \oint \langle \psi(k) | \nabla_k | \psi(k) \rangle \cdot dk = \oint \mathbf{A}(k) \cdot dk$$

The Berry connection $\mathbf{A}(k) = i \langle \psi(k) | \nabla_k | \psi(k) \rangle$ encodes the geometric phase accumulated along the loop.

For a 2D system with periodic boundary conditions (torus), the Berry phase can be integrated over the entire Brillouin zone, yielding the **Chern number**:

$$C = \frac{1}{2\pi i} \int_{BZ} d^2k \, \mathbf{A}(k) \cdot (\nabla_k \times \mathbf{A}(k))$$

where $\nabla_k \times \mathbf{A}$ is the Berry curvature. The Chern number is quantized: $C \in \mathbb{Z}$.

In crystalline systems (electronic, photonic, or phononic), the Chern number classifies the topology of the band structure. A non-zero Chern number $C \neq 0$ indicates a topologically non-trivial insulator; it guarantees the existence of protected edge states.

**Topological Invariants in Metamaterials:**

In metamaterials, the band structure is engineered through structure (lattice geometry, resonance tuning, etc.) rather than relying on fundamental quantum properties. Yet the same topological invariants apply: if the metamaterial's lattice is designed such that the band structure has a non-zero Chern number, topologically protected edge states emerge.

### Bulk-Boundary Correspondence

The key theorem underlying topological metamaterials is the **bulk-boundary correspondence**: the number and properties of edge states are determined entirely by the bulk topological invariant.

For a 2D system with Chern number $C$:

**Number of edge states crossing the gap:** $|C|$

**Directionality of edge modes:** All edge states propagate in the same direction (chiral propagation).

**Robustness to disorder:** As long as the band gap remains open, edge states persist despite disorder and defects. This is because the topological charge cannot change continuously.

Mathematically, this follows from the Atiyah-Singer index theorem: the number of zero modes of a differential operator is related to its topological index.

### Engineering Topological Bands in Metamaterials

To create a topological metamaterial, one must:

1. **Design a periodic structure** with a band structure (via frequency dispersion, coupled resonators, etc.).

2. **Break a symmetry** (e.g., time-reversal symmetry, or a mirror symmetry) to open a band gap. Without gap-opening, the Chern number is ill-defined (states can mix across the gap).

3. **Tune parameters** to achieve a non-zero Chern number in the region of interest.

**Example: Topological Photonic Crystal**

A photonic crystal with a triangular lattice of dielectric pillars naturally has a band gap separating lower and upper bands. To make it topological, one can:

- **Break time-reversal symmetry** via the Faraday effect (applying a magnetic field perpendicular to the plane), causing the gyromagnetic response of the material to couple different polarizations asymmetrically.

The modified dispersion relation becomes:

$$\omega(k) = \omega_0(k) \pm \frac{g B}{2}$$

where $g$ is the gyromagnetic coupling strength and $B$ is the magnetic field. The $\pm$ corresponds to two opposite circular-polarization eigenmodes.

The band structure now exhibits a band inversion at certain points in the Brillouin zone (where the lower and upper bands would meet in the unmagnetized case). This inversion is the signature of a non-zero Chern number.

The resulting band structure has a gap containing chiral edge states: modes that propagate only in one direction along the boundary.

### Higher-Order Topological Insulators

Recent advances include **higher-order topological insulators**: systems whose topological properties are characterized by higher-order invariants (quadrupole moment, octupole moment, etc.), leading to **corner states** (localized at corners of a 2D sample) or **hinge states** (localized along edges of a 3D sample), rather than the usual edge states.

These are classified by a topological multipole expansion:

$$p_\text{dipole} = 0, \quad p_\text{quadrupole} \neq 0$$

A 2D higher-order topological insulator with zero dipole moment but non-zero quadrupole moment hosts zero-dimensional corner states.

### Non-Hermitian Topological Metamaterials

Metamaterials with gain and loss (active components) are non-Hermitian. They exhibit exotic topological phenomena:

- **Exceptional-point topologies:** Band touchings at exceptional points (not diabolical points) where eigenvalues and eigenvectors coalesce.

- **Non-Hermitian skin effect:** Boundary accumulation of eigenstates.

- **PT-symmetric topological metamaterials:** Balanced gain-loss systems maintaining PT symmetry while exhibiting topological properties.

For example, in a 1D PT-symmetric system:

$$H = \sum_n t_n (|n\rangle\langle n+1| + |n+1\rangle\langle n|) + i\gamma n$$

where the imaginary term alternates between $+i\gamma$ and $-i\gamma$, the system can exhibit topological phase transitions without band gaps closing—a phenomenon absent in Hermitian systems.

### Topological Nonlinearities

Recent work explores **nonlinear topological metamaterials**, where the topological properties depend on the amplitude of excitations. Examples include:

- **Nonlinear edge-state localization:** Edge modes are enhanced or suppressed depending on their intensity.

- **Topological solitons:** Nonlinear waves constrained to boundaries by topological protection, with no linear (small-amplitude) counterpart.

- **Frequency-dependent topology:** As the amplitude increases, the effective band structure changes, altering the Chern number dynamically.

---

## Key Results

1. **Universal Topological Classification:** Berry phase and Chern numbers classify the topology of metamaterial band structures, independent of specific material or frequency domain (photonic, phononic, electronic).

2. **Engineered Topological Bands:** Topological properties can be deliberately engineered into metamaterials via symmetry breaking and structure design, without relying on fundamental quantum properties.

3. **Protected Edge States Are Robust:** Non-zero Chern number guarantees existence of edge states and their immunity to back-scattering from defects, disorder, and impurities.

4. **Chiral Propagation:** Topological edge states propagate in a unique direction, determined by the Chern number sign and sample boundary.

5. **Higher-Order Topology:** Beyond edge states, metamaterials exhibit corner states and hinge states, expanding the space of topologically protected modes.

6. **Non-Hermitian Extensions:** Active metamaterials (with gain and loss) exhibit new topological phenomena, including exceptional-point topology and non-Hermitian skin effects.

7. **Nonlinear Topological Effects:** Amplitude-dependent topology enables nonlinear topological solitons and tunable edge-state properties.

8. **Practical Devices:** Topological photonic and phononic waveguides, topologically protected lasers, and integrated topological circuits have been demonstrated experimentally.

---

## Impact and Legacy

This review consolidates topological metamaterials as a mature, transformative field:

- **Paradigm Shift:** From viewing topology as exotic and restricted to quantum systems to recognizing it as a universal principle applicable to engineered classical materials.

- **Technological Applications:** The robustness of topological edge states enables new devices in communications, sensing, and computing.

- **Fundamental Physics:** Metamaterials serve as a platform for testing topological theories in controlled, observable settings.

- **Interdisciplinary Bridges:** Connects condensed-matter theory, photonics, phononics, materials science, and engineering.

---

## Connection to Phonon-Exflation Framework

**The BDI Classification as Topological Invariant:**

The phonon-exflation framework identifies its SU(3) spectral structure with the **BDI topological class** (time-reversal symmetry $T^2 = +1$, particle-hole symmetry, no chiral symmetry). The Pfaffian sign $\text{Pf}(D_K) = -1$ is analogous to a Chern number.

In the language of this topological-metamaterials review, the framework's spectral action defines a **band structure in internal space** (the SU(3) fiber), and this band structure has non-trivial topology—specifically, BDI classification.

**Topologically Protected Particle Spectrum:**

The Standard Model's particle spectrum (electron, muon, tau, quarks, bosons) can be reinterpreted as **edge states** (in internal-space) of a higher-dimensional topological structure. The fact that the spectrum is robust (unchanged by small perturbations to the coupling constants) mirrors the robustness of topological edge states to disorder.

**Corner States Analogy:**

The framework predicts precise mass hierarchies (e.g., $m_e / m_\mu \approx 1/200$) that are "exact" in some sense. These could be reinterpreted as **corner states** in a higher-order topological invariant structure: states localized at special points in a higher-dimensional parameter space, protected by topology beyond simple Chern numbers.

**Phonon-Electron Coupling and Non-Hermitian Topology:**

The coupling between the phononic excitations (BCS Cooper pairs) and the electronic degrees of freedom (Fermi surface) in the framework is non-Hermitian: gain (instanton-driven pair creation) balances loss (pairing interactions). This mirrors PT-symmetric topological metamaterials studied in this review.

**Dynamical Topology in the Transit:**

As the universe transits in $\tau$-space (from $\tau = 0$ to $\tau \approx 0.3$), the topological invariant—the Pfaffian sign—remains frozen ($\text{Pf} = -1$ throughout). However, the **effective** topology of the quasiparticle excitations changes: the density of states evolves, band structure deforms, but the topological index persists.

This is analogous to a **nonlinear topological metamaterial** where amplitude changes alter the local band structure but the global Chern number remains quantized.

**Experimental Opportunities:**

Topological metamaterials reviewed here provide a possible **laboratory platform** for testing aspects of the phonon-exflation framework:

- Engineer a phononic metamaterial with BDI-class topology (e.g., a 3D acoustic metamaterial with appropriate symmetry breaking).
- Measure the edge-state spectrum and verify robustness to disorder.
- Introduce phonon-electron coupling (via piezoelectric coupling, superconducting interfaces, etc.) and study the emergence of Cooper pairs and their non-thermal statistics (GGE).
- Test predictions of the framework (specific mass ratios, coupling constants) in the metamaterial analog.

---

## References and Further Reading

- Ni, X., Yves, S., Krasnok, A., & Alù, A. (2023). "Topological metamaterials." *Chemical Reviews*, 123(12), 7585–7654.
- Ozawa, T., Price, H. M., Amo, A., Goldman, N., Hafezi, M., Lu, L., ... & Zilberberg, O. (2019). "Topological photonics." *Reviews of Modern Physics*, 91(1), 015006.
- Lu, L., Joannopoulos, J. D., & Soljačić, M. (2014). "Topological photonics." *Nature Photonics*, 8(11), 821–829.
- Wang, Z., Chong, Y., Joannopoulos, J. D., & Soljačić, M. (2009). "Observation of unidirectional backscattering-immune topological electromagnetic states." *Nature*, 461(7265), 772–775.
- Hafezi, M., Demler, E. A., Lukin, M. D., & Chong, Y. (2011). "Robust optical delay lines with topological protection." *Nature Physics*, 7(12), 907–912.
