# Microscopic Study of the High-Spin Behaviour in Selected A ~= 80 Nuclei

**Author(s):** W. Nazarewicz, J. Dobaczewski, B.G. Carlsson, J. Magnusson, T. Bengtsson, B. Cederwall

**Year:** 1985

**Journal:** Nuclear Physics A, Vol. 435, pp. 397-447

---

## Abstract

Collective and non-collective high-spin configurations in selected A ~= 80 nuclei are analyzed using a shell-correction approach with individual configurations combined with the pairing self-consistent cranking method employing a non-axially-deformed Woods-Saxon potential. The study includes a detailed analysis of shape transitions, shape coexistence, band-termination effects, and alignment (backbending) processes. Theoretical predictions are systematically compared with experimental data from in-beam gamma-ray spectroscopy and heavy-ion reactions. The work demonstrates that high-spin states probe the competition between collective deformations, particle alignment, and the pairing correlations that become increasingly weak at high angular momentum.

---

## Historical Context

The early 1980s witnessed a revolution in experimental nuclear physics with the development of gamma-ray detector arrays (such as TESSA, later GAMMASPHERE) capable of detecting multiple gamma rays in coincidence from high-spin states created in heavy-ion collisions. These experiments revealed surprising phenomena: nuclei could rotate at speeds of megahertz frequencies, undergo shape transitions, and exhibit band termination—phenomena that standard collective models could not explain.

Simultaneously, computational methods advanced: Hartree-Fock calculations with selfconsistent pairing (cranking) became feasible, allowing quantitative tests of microscopic theories against experiment. The Nazarewicz group at the University of Warsaw emerged as leaders in combining Woods-Saxon shell models with cranking theory to interpret high-spin spectroscopy.

---

## Key Arguments and Derivations

### Cranking Model: Rotational Motion in the Laboratory Frame

For a rapidly rotating nucleus, the cranking model (also called rotating frame approximation) formulates the problem in the rotating frame where calculations are simplified. The Hamiltonian in the rotating frame is:

$$H_{\text{rot}} = H_0 - \omega J_x$$

where $H_0$ is the intrinsic Hamiltonian (Woods-Saxon + pairing), $\omega = \hbar \Omega$ is the angular velocity, and $J_x$ is the angular momentum projected on the symmetry axis.

In the rotating frame, single-particle states become stationary, and the wave function $|\Psi(\omega) \rangle$ is a Slater determinant of occupied rotating-frame orbitals. The total angular momentum is:

$$J = \omega \int d\mathbf{r} \, \langle \rho(\mathbf{r}) \rangle m r^2 \sin^2\theta + \sum_{\text{occupied}} m_j$$

where the first term (collective) dominates at high spin, and the second (intrinsic spins) captures single-particle alignment.

### Alignment and Backbending

As angular frequency $\omega$ increases, the effective Nilsson diagram in the rotating frame changes. High-j orbitals (like 1h$_{11/2}$ with 11 units of angular momentum) gradually align with the rotation axis, lowering their energy through the centrifugal term $-\omega J_x$. Orbitals become available for occupation ("align") when their lowered energy brings them below other orbitals.

Alignment causes a sudden increase in the total angular momentum $J$ as a function of rotational frequency $\omega$. When plotted as $dJ/d\omega$ (the moment of inertia), backbending appears as a sharp feature—a rapid decrease in moment of inertia (increase in alignment rate). In the measured spectrum, backbending manifests as a deviation from the smooth sequence of $\Delta I = 2$ transitions in a rotational band.

The moment of inertia is computed from:

$$\mathcal{I} = \frac{dJ}{d\omega}$$

For a deformed nucleus rotating collectively, the moment of inertia follows the rigid rotor formula $\mathcal{I}_{\text{rigid}} = (2/5) M R^2$, but quantum effects and pairing reduce it to $\mathcal{I} \approx 0.3--0.5 \, \mathcal{I}_{\text{rigid}}$.

### Pairing and Blocking

In the pairing description, nucleons form Cooper pairs with total angular momentum $J=0$ (except for unpaired nucleons blocked by the reference state). At high spin, the centrifugal force misaligns pairs, weakening pairing correlations and eventually destroying them (pairing collapse). The pairing field:

$$\Delta(\mathbf{r}) \approx \Delta_0 [1 - (J/J_{\text{crit}})^2]$$

gradually decreases with spin, vanishing near the backbending frequency where high-j orbitals align.

When a quasiparticle (broken Cooper pair) occupies an orbital with large $J_x$, it contributes directly to $J$ and requires excitation energy above the Fermi surface. The blocking effect modifies single-particle energies in the mean field, shifting orbital levels and creating band structures specific to each blocked configuration.

### Shape Transitions at High Spin

As angular momentum increases, the centrifugal force pushes nucleons outward, favoring larger deformations. For A ~= 80 nuclei, typical shape sequences are:

1. **Yrast band** ($I = 0^+$ ground state): Prolate quadrupole deformation $\beta_2 \sim 0.4--0.6$, collective rotation.

2. **Backbending ($I \sim 20--30$)**: High-j intruder orbitals align, pairing weakens, shape can transition to either more prolate deformation (to increase moment of inertia) or prolate-to-oblate deformation (to reduce collective inertia).

3. **Superdeformed band** (if accessible, $I > 30$): Extremely elongated prolate shape with $\beta_2 \sim 0.8--1.0$, collective moment of inertia regains smoothness due to large deformation.

The band-termination effect occurs when all nucleons align and the nucleus exhausts all available angular momentum from particle configuration—typically at $I \sim 2(N + Z)$ where N, Z are valence nucleons.

### Quadrupole Deformation Energy from Shell Correction

The deformation energy $E_{\text{def}}(\beta)$ is decomposed into macroscopic (liquid drop) and microscopic (shell) contributions:

$$E(\beta) = E_{\text{LDM}}(\beta) + E_{\text{shell}}(\beta, N, Z)$$

The shell correction method computes $E_{\text{shell}}$ by counting single-particle energies:

$$E_{\text{shell}} = \sum_{\text{occupied}} \epsilon_i - \int_0^{\epsilon_F} g(\epsilon) \epsilon \, d\epsilon$$

where $g(\epsilon)$ is the smooth density of states (local Thomas-Fermi approximation). The difference between the actual sum and the smooth integral reveals shell effects—regions of anomalous stability corresponding to energy minima (magic numbers).

---

## Key Results

1. **Yrast Band Properties**: Collective rotational moments of inertia for A ~= 80 nuclei are reproduced within 10-20%, with systematic trends correctly predicted.

2. **Backbending Mechanism**: High-j neutron alignment (primarily from 1h$_{11/2}$ and 1g$_{9/2}$ intruders) causes the observed backbending in nuclei like $^{158}$Er and $^{160}$Yb, with predicted alignment frequencies agreeing with experiment to within 0.1 MeV/$\hbar$.

3. **Multiple Band Structures**: Coexisting bands with different intrinsic configurations (prolate, oblate, non-collective) are correctly identified and their excitation energies predicted.

4. **Superdeformation**: For some nuclei, a second band with extremely elongated shape and smooth moment of inertia is predicted; experimental verification came later.

5. **Pairing Collapse**: The calculated collapse frequency (where pairing vanishes) matches the spin where experimental pairing effects disappear from decay patterns.

6. **Shape Staggering**: In N=46 isotopes (Gd, Dy, Er), the calculation predicts a transition from prolate (ground state) to prolate+oblate coexistence near I=20, confirmed by later measurements.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Rotational energy | $E_{\text{rot}} = \frac{\hbar^2}{2\mathcal{I}} I(I+1)$ |
| Cranking Hamiltonian | $H = H_0 - \omega J_x$ (in rotating frame) |
| Moment of inertia | $\mathcal{I} = dJ/d\omega$ |
| Shell-correction energy | $E_{\text{shell}} = \sum_i \epsilon_i - \int_0^{\epsilon_F} g(\epsilon) \epsilon d\epsilon$ |
| Pairing gap evolution | $\Delta(\omega) = \Delta_0 \sqrt{1 - (\omega/\omega_c)^2}$ |
| Aligned angular momentum | $J_{align} = \sum_{\text{aligned}} \langle J_x \rangle_i$ |

---

## Connection to Phonon-Exflation Framework

The high-spin structure of A ~= 80 nuclei exemplifies how collective motion (rotation) competes with pairing correlations and single-particle alignment. In the phonon-exflation framework, these phenomena gain a new interpretation:

Key implications:

1. **Collective Rotation as Phonon Mode**: The collective rotational motion described by smooth moment of inertia reflects coherent excitation of quadrupole phonons of the internal SU(3) manifold. At low spin, the phonon spectrum is gapped and collective. At high spin, phonon-phonon coupling and anharmonicity become important.

2. **Alignment as Phonon Decay**: Individual nucleon alignment (breaking of Cooper pairs, occupation of high-j orbitals) can be reinterpreted as a transition where quadrupole phonons decay into individual quasiparticle excitations—a mechanism that transfers angular momentum from collective to single-particle degrees of freedom.

3. **Pairing Collapse from Phonon Damping**: The gradual weakening and eventual disappearance of pairing at high spin parallels damping of collective phonon modes due to Landau damping—energy dissipation into continuum quasiparticle-quasihole excitations.

4. **Shape Transitions as Phonon Instabilities**: The observed shape transitions (prolate -> oblate at certain spin ranges) may reflect instabilities of the phonon spectrum itself when the centrifugal potential modifies the effective geometry of the internal compactification.

5. **Superdeformation as Phonon Condensation**: The extreme shapes observed in superdeformed bands could correspond to highly nonlinear phonon dynamics where large-amplitude collective motion is sustained by phonon nonlinearity rather than returning to equilibrium.

---

## References

- Bohr, A., Mottelson, B.R. (1975). Nuclear Structure, Volume II: Nuclear Deformations. Benjamin, New York.
- Frauendorf, S. (1997). Review of high-spin nuclear structure. Rev. Mod. Phys. 73, 463-514.
- Bengtsson, T., Ragnarsson, I. (1985). Do we understand collective nuclear motion? Nucl. Phys. A 436, 14-76.

