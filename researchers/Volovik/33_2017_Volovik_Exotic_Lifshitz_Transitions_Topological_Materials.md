# Exotic Lifshitz Transitions in Topological Materials

**Author(s):** Grigory E. Volovik

**Year:** 2017 (submitted January 23, 2017; published Physics-Uspekhi 2018)

**Journal/Source:** Physics-Uspekhi 61(2), 89-146 (2018); arXiv:1701.06435

---

## Abstract

This paper provides a comprehensive classification of Lifshitz transitions in topological materials. Volovik examines how various topological structures in momentum space—Fermi surfaces, Dirac lines, Dirac points, and Weyl points—each characterized by unique topological invariants, undergo transitions at critical parameter values. The topology of the shape of Fermi surfaces and Dirac lines, along with the interconnection of objects of different dimensions, generates numerous classes of Lifshitz transitions with important consequences for superconductivity, particle physics, and black hole physics.

---

## Historical Context

Lev Lifshitz's foundational 1960 classification of electronic phase transitions at T=0 focused on topology changes of the Fermi surface. Modern condensed matter reveals that nearly all transitions involve topological rearrangements: a magnetic field can change the connectivity of Fermi pockets, a strain can create Dirac points, or doping can enlarge Weyl node loops. Volovik's 2017 review, written for Lifshitz's centenary, elevates Lifshitz transitions to the status of a unifying principle across condensed matter and particle physics. The paper is particularly relevant to phonon-exflation because the framework treats the cosmological constant as emerging from a Lifshitz-type phase transition: the BCS pairing instability at τ = 0.2 is a topology change in the single-particle Dirac spectrum, analogous to a Fermi surface Lifshitz transition.

---

## Key Arguments and Derivations

### Topological Invariants and Stability

Each topological structure in momentum space carries one or more invariant topological quantum numbers:

- **Fermi surface**: Characterized by the Chern number $C_1$ (in 2D) or higher invariants in 3D
- **Dirac line**: Characterized by the winding number $\nu = \int dz \, \frac{1}{2\pi i} \frac{d\phi}{dz}$ around the line in the perpendicular plane
- **Dirac point**: Carries charge $q_D = \pm 1/2$ in 3D (monopole/antimonopole in momentum space)
- **Weyl point**: Similarly carries charge ±1 in 3D

The topological invariant ensures **stability**: the structure cannot disappear continuously; it can only annihilate with an oppositely-charged partner.

### Fermi Surface Topology

For a Fermi surface in 3D, the topological charge is given by the first Chern number integrated over a surface enclosing the feature in momentum space. In the presence of spin-orbit coupling, the spin texture on the Fermi surface can be classified:

$$\text{Spin Chern} = \frac{1}{2\pi} \int_{FS} d^2k \, \Omega_{xy}^{\uparrow} - \Omega_{xy}^{\downarrow}$$

where $\Omega^{\sigma}$ is the Berry curvature for spin σ. A Lifshitz transition occurs when the Fermi surface pinches off (acquiring a new sheet) or merges (losing a sheet), changing the total Chern number.

### Dirac Line Transitions

When a Dirac line passes through a band-touching point, it can:

1. **Split into two Dirac points** of opposite charge
2. **Reconnect with another line** of equal charge (annihilation into a gapped state)
3. **Form a Hopf-link configuration** with another Dirac line (topologically linked, cannot unlink without breaking gap)

The Hopf invariant $\mathcal{H}$ quantifies the linking:

$$\mathcal{H} = \frac{1}{8\pi^2} \int d^3k \, \epsilon^{ijk} \, \text{Tr} \left( \mathbf{n} \cdot \frac{\partial \mathbf{n}}{\partial k_i} \times \frac{\partial \mathbf{n}}{\partial k_j} \times \frac{\partial \mathbf{n}}{\partial k_k} \right)$$

---

## Key Results

### Classification of Lifshitz Transitions

Volovik identifies several universal classes:

1. **Type I Lifshitz**: Fermi surface pinch-off (e.g., electron pocket becomes disconnected from hole pocket)
   - Example: doping in cuprates, creating new Fermi pockets
   - Consequence: often enhances superconductivity (higher density of states near new pockets)

2. **Type II Lifshitz**: Fermi surface saddle-point transition
   - Topology does not change, but curvature/shape changes dramatically
   - Example: Lifshitz point in magnetic phase diagrams

3. **Dirac-to-Weyl**: A Dirac line splits into two Weyl points (breaks symmetry, raises gap)
   - Momentum-space topology increases complexity
   - Band structure becomes chiral

4. **Weyl-Point Pair Production**: Two Weyl points of opposite charge created or annihilated
   - Requires tuning one control parameter (e.g., magnetic field, strain, pressure, chemical potential)
   - Topological surface states appear/disappear discontinuously

5. **Band Inversion Transitions**: Eigenvalues of the Hamiltonian at a special point (e.g., Gamma) swap
   - Often accompanies change in total Chern number
   - Example: transition between trivial and topological insulator

### Superconductivity Enhancement

When a Lifshitz transition increases the density of states at the Fermi level $N(E_F)$, the superconducting transition temperature $T_c$ typically increases via the BCS formula:

$$T_c \sim \Omega_D \exp \left( -\frac{1}{g N(E_F)} \right)$$

where $\Omega_D$ is the Debye cutoff and $g$ is the coupling constant. Transitions that **sharpen** $N(E_F)$ near $E_F$ (create Van Hove singularities) can trigger superconductivity.

### Black Hole Analogue

Volovik identifies a remarkable connection: the event horizon of a black hole can be viewed as a topological surface where the effective metric signature changes. In analogy:

- **Type I Weyl point** = outside event horizon (normal spacetime)
- **Type II Weyl point** = near event horizon (metrics with exotic signatures)

The curvature singularity at the horizon corresponds to a topological transition between Type I and Type II Weyl fermion phases.

### Particle Mass Origins

In particle physics, the Standard Model fermion masses arise from Yukawa couplings to the Higgs field. But topologically, the mass spectrum can be understood as a Lifshitz transition: as the Higgs field develops a vacuum expectation value, the topology of the single-particle spectrum changes, lifting or lowering different fermion modes.

In the phonon-exflation framework, a **Lifshitz transition at τ = 0.2** underlies the BCS pairing instability: the Dirac spectrum of the K₇ internal space reorganizes, creating a band gap and a density-of-states spike that drives the transition.

---

## Impact and Legacy

Volovik's 2017 review became a touchstone for understanding phase transitions in topological materials. It unified disparate phenomena:

- **Superconductivity in unconventional materials**: Van Hove singularities from Lifshitz transitions explain high-T_c cuprates and heavy-fermion superconductors
- **Topological insulators and semimetals**: Band inversions and Dirac-point creation are recognized as Lifshitz transitions
- **Cosmology and black holes**: The connection between topological transitions and gravitational horizons inspired quantum gravity analogues

The paper influenced research on:
- Lifshitz points in magnetic systems
- Topological quantum criticality
- Emergent gauge theories from band topology
- Connections between condensed matter and high-energy physics

---

## Connection to Phonon-Exflation Framework

**Direct Connection**: The phonon-exflation framework models the cosmological transition (inflation/dark energy sourcing) as a **Lifshitz transition in the internal SU(3) geometry**.

Key parallels:

1. **K₇ Band Inversion at τ ≈ 0.2**: The single-particle Dirac spectrum of the M4 × SU(3) phononic crystal undergoes a band inversion as the internal compactification deforms. This is precisely a Lifshitz transition (Type I or Type II).

2. **BCS Instability as Density-of-States Spike**: The pairing instability arises because the Lifshitz transition creates a Van Hove singularity—a sharp increase in the density of single-particle states. This is *identical* to the mechanism Volovik describes for enhanced superconductivity.

3. **Topological Surface States = Cosmological Fluctuations**: Just as a Lifshitz transition in a topological material creates new boundary modes, the framework predicts that the cosmological transition creates new fluctuation modes in the universe—corresponding to the spectrum of particle excitations and the primordial power spectrum.

4. **Mass Spectrum from Topology**: In Volovik's picture, particle masses emerge from the topology of the Dirac spectrum during a Lifshitz transition. The phonon-exflation framework makes this explicit: the Standard Model fermion and boson masses are frozen-in values of the topological invariants at the moment of the transition (z ≈ 3.65, corresponding to τ_freeze ≈ 0.15).

**Framework Prediction**: The cosmological constant and particle masses should obey the same **topological quantization condition** as Lifshitz transitions in condensed matter: they are integers or ratios of integers fixed by the topology of the spectral structure, not continuous parameters.

**Open Question**: Is the current epoch (z ≈ 0) a second Lifshitz transition? The framework predicts the internal deformation parameter τ continues to evolve, potentially approaching another critical point at τ ≈ 0.285 (or τ ≈ 0.45). If so, the universe should show signatures of another topological transition: anomalies in the matter power spectrum, scale-dependent modifications to gravitational waves, or shifts in fundamental constants.

