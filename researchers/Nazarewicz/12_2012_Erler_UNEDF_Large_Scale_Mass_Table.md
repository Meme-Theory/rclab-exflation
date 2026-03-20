# Large-Scale Mass Table Calculations in the Nuclear Density Functional Theory Framework: UNEDF Project

**Author(s):** J. Erler, N. Birge, M. Kortelainen, W. Nazarewicz, W. Olsen, A.M. Sexton, F. Stoitsov, Y. Xu

**Year:** 2012

**Journal:** Nature, Vol. 486, pp. 509-512

---

## Abstract

An ambitious computational effort using state-of-the-art density functional theory calculates nuclear masses for ~9,400 nuclei spanning the entire nuclear chart from the proton to the neutron drip line. The UNEDF (Universal Nuclear Energy Density Functional) collaboration employs sophisticated Skyrme effective interactions optimized through high-performance computing on leadership-class supercomputers (Jaguar, etc.). The resulting mass predictions achieve root-mean-square deviation (rms) from experiment of ~600 keV across the chart, a standard error that enables extrapolation to unstable nuclei with quantifiable precision. The work establishes nuclear density functional theory as a predictive tool for comprehensive nuclear structure mapping and identifies systematic deficiencies in current parametrizations.

---

## Historical Context

Throughout the 20th century, nuclear mass tables were compiled empirically from a combination of experimental measurements (most sparse for unstable nuclei) and theoretical extrapolations using semi-empirical mass formulas (SEMF) or dedicated parametrizations (FRDM, HFM). Each approach traded accuracy for coverage: measurements were precise but sparse; global models were comprehensive but with theoretical uncertainties often exceeding 1 MeV.

By the 2000s, rare isotope beam facilities and computational advances enabled a new paradigm: calculate masses self-consistently from an effective nuclear Hamiltonian across the entire nuclear landscape. The UNEDF project, initiated in 2009 as a SciDAC collaboration, represented the first comprehensive implementation of this vision. Using some of the world's most powerful supercomputers, the UNEDF effort produced the most accurate global nuclear mass predictions available, fundamentally changing how nuclear structure theorists address properties of exotic nuclei.

---

## Key Arguments and Derivations

### Skyrme Energy Density Functional

The UNEDF calculations employ the Skyrme effective interaction, which expresses the nuclear energy as a functional of the nucleon density:

$$E[\rho_n, \rho_p, \boldsymbol{\tau}_n, \boldsymbol{\tau}_p, \ldots] = \int d\mathbf{r} \, \epsilon[\rho_n(\mathbf{r}), \rho_p(\mathbf{r}), \ldots]$$

The energy density $\epsilon$ is parametrized as:

$$\epsilon = \epsilon_{\text{kinetic}} + \epsilon_{\text{central}} + \epsilon_{\text{spin}} + \epsilon_{\text{tensor}} + \epsilon_{\text{Coulomb}} + \ldots$$

where:
- Kinetic: $\epsilon_{\text{kinetic}} = \frac{\hbar^2}{2m} \tau$, with kinetic density $\tau = \nabla^2 \rho$
- Central: Contact terms $\sim \rho^2$ and $\sim \rho \tau$ capture bulk properties
- Spin-orbit: $\sim (\nabla \rho \times \boldsymbol{\sigma}) \cdot \nabla \rho$ produces spin-orbit splittings (magic numbers)
- Tensor: Optional, captures some aspects of tensor-force physics
- Coulomb: $\epsilon_{\text{Coulomb}} = \frac{e^2}{2} \rho_p \left[ \int d\mathbf{r}' \frac{\rho_p(\mathbf{r}')}{|\mathbf{r} - \mathbf{r}'|} + \ldots \right]$

The functional is parametrized by ~20 constants (coupling strengths and ranges) fitted to binding energies, charge radii, and other nuclear data.

### Self-Consistent Hartree-Fock-Bogoliubov Calculations

For each nucleus, the wave function and energy are determined by solving the HFB equations:

$$\begin{pmatrix} h - \lambda & \Delta \\ -\Delta^\dagger & -h^* + \lambda \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = E \begin{pmatrix} u \\ v \end{pmatrix}$$

where the mean-field Hamiltonian $h$ is derived from functional variation:

$$h_{ij} = \delta E / \delta \rho_{ij}$$

and the pairing field is:

$$\Delta_{ij} = \delta E / \delta \kappa_{ij}$$

The computation requires diagonalization of a ~1000 x 1000 matrix for each nucleus, repeated until self-consistency (density and pairing field converge).

### Treatment of Deformation

For deformed nuclei, constrained calculations fix the quadrupole moment $Q_2 = \langle r^2 P_2(\cos\theta) \rangle$ and solve HFB with Lagrange multiplier:

$$H_{\text{eff}} = H - \lambda_2 Q_2$$

The total energy is then $E(Q_2)$, traced over a range of deformations to map the PES. The ground state is the lowest point on this surface.

For approximately spherical nuclei, deformation effects are small and the calculation simplifies; for deformed nuclei (much of the chart), explicit deformation treatment is essential for accuracy.

### Pairing Treatment

Two approaches are employed:
1. **Zero-range pairing**: Contact interaction with strength G(q)—simple but divergent in large model spaces
2. **Density-dependent pairing**: $G = G_0 [1 - \eta \rho(\mathbf{r})]$—partially absorbs effects of omitted physics

The pairing strength is either fixed empirically or optimized simultaneously with the Skyrme parameters during the fitting procedure.

### Computational Infrastructure

The UNEDF project employed:
- **Jaguar supercomputer** (Oak Ridge): ~10$^{15}$ floating-point operations for comprehensive calculations
- **Parallel MPI code** (HFODD): Parallel-domain decomposition HFB solver
- **Iterative refinement**: Multiple fitting cycles with improved parametrizations

Computing time per nucleus ranged from 10 seconds (light, spherical) to 10 minutes (heavy, deformed), necessitating distributed computing across thousands of processors.

---

## Key Results

1. **Comprehensive Coverage**: Mass predictions for ~9,400 nuclei from Z=1 to Z=120, N=1 to N=184, spanning from the proton to neutron drip line.

2. **Global Accuracy**: Root-mean-square deviation from experimental masses is ~600 keV across the entire chart. For nuclei near stability, accuracy improves to ~200-300 keV. For drip-line nuclei far from experiment, systematic errors are typically ~500 keV.

3. **Deformation Effects Captured**: The UNEDF calculation correctly predicts ground-state deformations, with prolate/oblate configurations properly identified and relative energies accurate to ~100 keV.

4. **Shell Effects**: Magic numbers and shell closures are reproduced, including exotic closures in neutron-rich systems (e.g., N=50 in Sn isotopes, N=82 persistence in Pb region).

5. **Beta-Decay Q-Values**: Second-difference masses (which determine beta-decay Q-values) are reproduced with accuracy of ~200 keV, enabling prediction of beta-decay chains relevant to r-process.

6. **Neutron Drip Line**: The two-neutron drip line is correctly predicted for Z > 20 (position within 2 nucleons in most regions), enabling astrophysical applications.

7. **Charge Radii Trends**: Charge radius predictions from the optimized functional show systematic improvement compared to earlier parameterizations, capturing the isotope-shift anomalies in some chain

s.

---

## Key Equations

| Quantity | Expression |
|:---------|:-----------|
| Skyrme energy | $E = \int d\mathbf{r} \epsilon(\rho, \tau, s, \ldots)$ |
| Kinetic energy density | $\epsilon_{\text{kin}} = \frac{\hbar^2}{2m} \tau(\mathbf{r})$ |
| Pairing interaction | $V_{\text{pair}} = -G(1 - \eta \rho(\mathbf{r})) \delta(\mathbf{r} - \mathbf{r}')$ |
| Self-consistency condition | $\rho_{ij} = \sum_k v_{ik}^* v_{jk}$ (from HFB wave function) |
| Binding energy | $B = -E(A,Z)$ (negative of ground-state energy) |
| Mass excess | $\Delta M = [M(A,Z) - M_u] c^2$ where $M_u$ is unified atomic mass unit |

---

## Connection to Phonon-Exflation Framework

The UNEDF project represents the current state-of-the-art density functional theory (DFT) approach to nuclear structure. In the phonon-exflation framework, the effective Skyrme interaction emerges as a low-energy effective theory of phononic modes on the internal SU(3) manifold.

Key implications:

1. **Effective Interaction from Geometry**: The Skyrme parameters (~20 constants) in UNEDF could be understood, in the framework, as arising from the spectral properties and coupling constants of the internal manifold. The fitting procedure (optimizing parameters to experimental data) then effectively maps out the geometry.

2. **Systematic Errors as Geometric Corrections**: The observed ~600 keV rms error in UNEDF masses might reflect physics missing from the Skyrme parametrization—specifically, corrections from the phonon spectrum of the internal geometry that are not captured by a simple contact interaction.

3. **Deformation Energy from Phonons**: The calculated deformation energies (difference between prolate and spherical configurations) arise in UNEDF from changes in the single-particle spectrum and pairing energy. In the framework, deformation would explicitly represent excitation of the internal manifold's geometric modes.

4. **Pairing Strength Evolution**: The successful density-dependent pairing in UNEDF (where $G$ decreases with density) reflects the framework's prediction that pairing strength should depend on the local phonon density of states, which decreases at high density.

5. **Predictive Power for Exotic Nuclei**: If the phonon-exflation framework is correct, UNEDF's success in predicting properties of unstable nuclei far from stability suggests that the internal geometry's phonon spectrum is remarkably robust—changing minimally with neutron/proton imbalance. Conversely, any systematic deviations of future measurements from UNEDF predictions would signal regions where the framework's assumptions break down.

---

## References

- Kortelainen, M., Lesinski, T.,Moreaux, J., et al. (2010). Nuclear energy density optimization. Phys. Rev. C 82, 024313.
- Erler, J., Birge, N., Kortelainen, M., Nazarewicz, W., et al. (2012). The limits of the nuclear landscape. Nature 486, 509-512.
- Bender, M., Heenen, P.H., Reinhard, P.-G. (2003). Self-consistent mean-field models for nuclear structure and dynamics. Rev. Mod. Phys. 75, 121-180.

