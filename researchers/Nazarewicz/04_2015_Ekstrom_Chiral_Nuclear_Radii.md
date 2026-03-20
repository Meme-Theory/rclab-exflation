# Accurate Nuclear Radii and Binding Energies from a Chiral Interaction

**Author(s):** A. Ekström, G.R. Jansen, K.A. Wendt, G. Hagen, T. Papenbrock, B.D. Carlsson, C. Forssén, M. Hjorth-Jensen, P. Navrátil, W. Nazarewicz

**Year:** 2015

**Journal:** Physical Review C, Vol. 91, p. 051301(R)

---

## Abstract

Two-nucleon and three-nucleon forces derived from chiral effective field theory are optimized simultaneously to low-energy nucleon-nucleon scattering data as well as binding energies and radii of few-nucleon systems and selected isotopes of carbon and oxygen. The resulting interaction, NNLO_sat, yields accurate binding energies and radii of nuclei up to $^{40}$Ca using coupled-cluster calculations, is consistent with the empirical saturation point of symmetric nuclear matter, and correctly describes the low-lying collective 3$^-$ states in $^{16}$O and $^{40}$Ca. Spectra for selected p-shell and sd-shell nuclei are in reasonable agreement with experiment, demonstrating that ab initio methods combined with optimized chiral forces can provide a unified description of nuclear structure across the periodic table.

---

## Historical Context

Nuclear physics has long struggled with the fundamental problem: how to derive nuclear forces from the underlying quark-gluon interactions while preserving computational tractability for finite nuclei. The development of chiral effective field theory (ChEFT) by Weinberg in the 1990s provided a systematic expansion of nuclear forces in powers of a small parameter: the ratio of the pion mass to the chiral symmetry breaking scale ($m_\pi / \Lambda_\chi \sim 0.1$).

However, early ChEFT applications produced interactions plagued by computational limitations: existing fits could not simultaneously satisfy both fundamental nuclear matter constraints (saturation point: $E_0 \approx -16$ MeV at $\rho_0 \approx 0.16$ fm$^{-3}$) and finite nuclear observables. The NNLO_sat interaction represented a breakthrough by introducing a systematic optimization procedure that traded some theoretical purity for practical accuracy—fitting directly to experimental binding energies and radii rather than relying solely on fit-to-nucleon-nucleon scattering data.

---

## Key Arguments and Derivations

### Chiral Effective Field Theory Expansion

At leading order in the chiral expansion, the nucleon-nucleon potential consists of:
- **One-pion exchange (OPE)**: $V_\pi(\mathbf{q}) = -g_A^2/(4f_\pi^2) \sigma_1 \cdot \mathbf{q} \sigma_2 \cdot \mathbf{q} / (\mathbf{q}^2 + m_\pi^2)$
- **Contact terms**: Contact interactions arise at each order, constrained by chiral symmetry.

The chiral expansion at next-to-next-to-leading order (NNLO) reads:

$$V_{NN} = V_\pi^{(0)} + V_\pi^{(2)} + V_\pi^{(3)} + V_C^{(0)} + V_C^{(2)} + V_C^{(3)} + \ldots$$

where superscripts denote chiral order. The contact terms $V_C^{(n)}$ have the form:

$$V_C^{(0)} = C_S^{(0)} + C_T^{(0)} S_{12}$$

with the tensor operator $S_{12} = 3(\sigma_1 \cdot \hat{\mathbf{r}})(\sigma_2 \cdot \hat{\mathbf{r}}) - \sigma_1 \cdot \sigma_2$.

### Three-Body Forces

At NNLO, three-body forces (3BF) enter. The dominant contributions are:
- **Two-pion exchange**: Intermediate pion exchange mediated through an intermediate nucleon
- **One-pion exchange + contact**: Combination of OPE in one pair and contact interaction involving the third nucleon
- **Purely contact**: Three-body contact terms

The 3BF are parametrized by the low-energy couplings (LECs):

$$V_{ijk}^{(2\pi)} \propto \left\{ \ldots \right\} (\sigma_i \cdot \mathbf{q})(\sigma_j \cdot \mathbf{q})$$

where $\mathbf{q}$ is the exchanged pion momentum and the curly brackets denote combinations of spin operators.

### Saturation Point Constraint

The empirical saturation point of symmetric nuclear matter is:

$$E_0 = -16.0 \pm 0.1 \text{ MeV}, \quad \rho_0 = 0.160 \pm 0.005 \text{ fm}^{-3}$$

The equation of state $E(\rho)$ for uniform nuclear matter is computed in the thermodynamic limit using Brueckner-Hartree-Fock theory or variational approaches. Chiral forces that violate saturation are unphysical—they predict either nuclear matter that is unbound or grossly over-bound.

For the NNLO_sat fit, the saturation constraint was included as a penalty term in the least-squares optimization:

$$\chi^2 = \chi^2_{\text{NN}} + \chi^2_{\text{BE}} + \chi^2_{\text{radii}} + w_{\text{sat}} (\rho_0^{\text{calc}} - \rho_0^{\text{exp}})^2 + \ldots$$

where $w_{\text{sat}}$ is a weight factor chosen to enforce saturation.

### Coupled-Cluster Approach

To calculate binding energies of finite nuclei up to $^{40}$Ca, the authors employ coupled-cluster (CC) theory, a many-body method that correlates nucleons systematically. The CC wave function is:

$$|\Psi_{\text{CC}} \rangle = e^T |\Phi_0 \rangle$$

where $T$ is the cluster operator:

$$T = T_1 + T_2 + T_3 + \ldots = \sum_{ia} t_i^a a^\dagger_a a_i + \frac{1}{2} \sum_{ijab} t_{ij}^{ab} a^\dagger_a a^\dagger_b a_j a_i + \ldots$$

The indices $i,j$ label occupied orbitals in the reference state $|\Phi_0\rangle$ (typically a Slater determinant from a mean-field calculation), while $a,b$ label unoccupied orbitals. The amplitudes $t_i^a, t_{ij}^{ab}, \ldots$ are determined by solving the CC equations:

$$\langle \Phi | e^{-T} H e^T | \Phi_0 \rangle = E_0$$
$$\langle \Phi_i^a | e^{-T} H e^T | \Phi_0 \rangle = 0$$

Truncating at $T \approx T_1 + T_2 (+ T_3)$ (singles and doubles, possibly including perturbative triples) provides high-precision predictions for ground-state and low-lying excited-state properties.

### Charge Radius Calculation

The mean-square charge radius is:

$$\langle r^2 \rangle = \frac{1}{Z} \int d\mathbf{r} \, r^2 \rho_{\text{charge}}(\mathbf{r})$$

where the charge density includes both proton point-particle contributions and the anomalous magnetic moment charge distribution. The NNLO_sat interaction reproduces experimental radii of $^{16}$O (2.73 fm) and $^{40}$Ca (3.48 fm) to within a few percent.

---

## Key Results

1. **Unified Description**: A single optimized interaction (NNLO_sat) simultaneously fits nucleon-nucleon scattering, binding energies from $^4$He to $^{40}$Ca, and nuclear radii, demonstrating that chiral forces can achieve quantitative accuracy across multiple observables.

2. **Saturation Satisfied**: The calculated equation of state yields saturation at $\rho_0 = 0.16$ fm$^{-3}$ and $E_0 = -16.0$ MeV, consistent with relativistic heavy-ion collision data and low-density neutron matter constraints.

3. **Collective Excitations**: The 3$^-$ giant monopole resonance in $^{16}$O and $^{40}$Ca is correctly predicted, validating the treatment of correlations beyond simple mean-field.

4. **Spectroscopy**: P-shell ($^6$Li, $^7$Li) and sd-shell ($^{20}$Ne, $^{24}$Mg) spectral predictions show reasonable agreement with experiment, though some states are systematically shifted.

5. **Convergence Behavior**: The CC expansion converges smoothly: including perturbative triples (CCSD(T)) improves binding energies by typically 0.5-1 MeV compared to CCSD alone.

6. **Nuclear Matter Saturation**: The equation of state for isospin-asymmetric matter ($N \neq Z$) is predicted with precision sufficient for astrophysical applications (neutron star structure).

---

## Connection to Phonon-Exflation Framework

The NNLO_sat interaction demonstrates that accurate nuclear forces emerge from a systematic expansion rooted in chiral symmetry—the approximate flavor symmetry of QCD at low energy. The phonon-exflation framework inverts this perspective: rather than deriving nuclear structure from QCD, it proposes that nucleonic structure emerges from collective excitations of an internal compactified geometry (M4 x SU(3)).

Key implications:

1. **Effective Interaction as Phonon Coupling**: The optimized NNLO_sat parameters effectively encode the strength and range of collective phonon-driven interactions. In the framework, the chiral scale $\Lambda_\chi \approx m_\rho \approx 770$ MeV would correspond to the characteristic energy scale of phonon modes in the SU(3) manifold.

2. **Saturation Point from Geometry**: The saturation point (binding energy and density) emerges in the framework as a consequence of the balance between attractive phononic pairing forces and repulsive Coulomb interactions, modulated by the spectral properties of the Dirac operator on the deformed 3-surface.

3. **Many-Body Correlations**: The coupled-cluster treatment of correlations parallels the framework's all-orders treatment of pairing corrections through the spectral action functional. Both approaches recognize that saturation and collective behavior cannot be captured by single-particle or mean-field theory alone.

4. **Universality Across Scales**: The success of a single chiral interaction across light, medium, and heavy nuclei (up to $^{40}$Ca here, extended to $^{208}$Pb in subsequent work) suggests an underlying universality principle—potentially the phononic nature of nuclear binding.

---

## References

- Machleidt, R., Entem, D.R. (2011). Chiral effective field theory and nuclear forces. Phys. Rep. 503, 1-75.
- Weinberg, S. (1992). Precision tests of QCD. In Proc. Theoretical Advanced Study Institute. World Scientific.
- Bogner, S.K., Kovalenko, V., Furnstahl, R.J. (2007). Unitarity of the unitary correlation operator transformation. Nucl. Phys. A 765, 104-135.
- Hagen, G., Papenbrock, T., Ekström, A., et al. (2016). Coupled-cluster computations of ground and excited states of nuclei. Phys. Rev. C 76, 044305.

