# Mean-Field Description of Ground-State Properties of Drip-Line Nuclei: Pairing and Continuum Effects

**Author(s):** J. Dobaczewski, W. Nazarewicz, T.R. Werner, J.F. Berger, C.R. Chinn, J. Dechargé

**Year:** 1996

**Journal:** Physical Review C, Vol. 53, pp. 2809-2840

---

## Abstract

Ground-state properties of exotic even-even nuclei with extreme neutron-to-proton ratios are studied with self-consistent mean-field theory with pairing formulated in coordinate space, which properly accounts for the influence of the particle continuum—particularly important for weakly bound systems. Pairing properties of nuclei far from stability are studied with several interactions, emphasizing different aspects such as the range and density dependence of the effective interaction. Measurable consequences of spatially extended pairing fields are presented, and the sensitivity to model variation is evaluated. The results demonstrate that accurate treatment of the continuum is mandatory for understanding binding and pairing in drip-line nuclei.

---

## Historical Context

The 1990s witnessed a revolution in rare isotope physics enabled by radioactive beam facilities. Nuclei could now be produced with neutron separation energies of only a few MeV—barely bound to the nuclear continuum. Traditional nuclear structure theory, developed for stable nuclei in deep potential wells, failed catastrophically for these systems. The key innovation of Dobaczewski and Nazarewicz was to reformulate Hartree-Fock-Bogoliubov (HFB) theory in coordinate space, allowing explicit treatment of the continuum.

Prior work using harmonic oscillator bases implicitly suppressed continuum effects. The continuum Hartree-Fock-Bogoliubov approach opened a new chapter, enabling quantitatively accurate predictions for halo nuclei and drip-line systems. This paper became foundational for the subsequent two decades of density functional theory applied to exotic nuclei.

---

## Key Arguments and Derivations

### Hartree-Fock-Bogoliubov Theory in Coordinate Space

The HFB wave function for a system of fermions in coordinate representation reads:

$$|\Psi \rangle = \exp\left( \frac{1}{2} \int d\mathbf{r} d\mathbf{r}' \, \kappa(\mathbf{r}, \mathbf{r}') c^\dagger(\mathbf{r}) c^\dagger(\mathbf{r}') \right) |\text{vac}\rangle$$

where $\kappa(\mathbf{r}, \mathbf{r}')$ is the pair amplitude (off-diagonal density matrix). The quasiparticle operator is:

$$\gamma_k = \int d\mathbf{r} \left[ u_k(\mathbf{r}) c(\mathbf{r}) + v_k(\mathbf{r}) c^\dagger(\mathbf{r}) \right]$$

with $u_k$ and $v_k$ the Bogoliubov amplitudes satisfying $\int d\mathbf{r} (|u_k|^2 + |v_k|^2) = 1$.

The self-consistent HFB equations in coordinate space are:

$$\begin{pmatrix} h - \lambda & \Delta \\ -\Delta^* & -h^* + \lambda \end{pmatrix} \begin{pmatrix} u \\ v \end{pmatrix} = E \begin{pmatrix} u \\ v \end{pmatrix}$$

where $h$ is the mean-field Hamiltonian, $\Delta$ is the pair potential (pairing field), $\lambda$ is the chemical potential, and $E$ are quasiparticle energies.

### Continuum Boundary Conditions

A critical innovation is the proper treatment of boundary conditions at large radii $r \to \infty$. For bound states, wave functions decay exponentially. For continuum scattering states, waves must exhibit the correct asymptotic form:

$$u_k(r \to \infty) \sim A_u \sin(kr + \delta_u)$$
$$v_k(r \to \infty) \sim A_v \sin(kr + \delta_v)$$

The Berggren contour approach integrates the equation of motion over a complex energy path in the complex k-plane, naturally including both bound states (negative energy poles) and continuum resonances (Gamow poles). This procedure provides completeness for the quasiparticle basis.

### Pairing Functional and Density Dependence

The pairing field is defined from the pair potential:

$$\Delta(\mathbf{r}) = \sum_{\text{pairs}} V_{\text{pair}} \kappa(\mathbf{r}, \mathbf{r})|_{\text{contact}}$$

Commonly used pairing interactions include:
- **Zero-range (contact) force**: $V_{\text{pair}} = -G_0 \delta(\mathbf{r} - \mathbf{r}')$ (simplest, but divergent in large model spaces)
- **Finite-range Gogny force**: $V_{\text{pair}} = -G e^{-(|\mathbf{r} - \mathbf{r}'|/\mu)^2}$ (reduces ultraviolet divergence)
- **Density-dependent contact force**: $V_{\text{pair}} = -G(1 - \eta \rho(\mathbf{r})) \delta(\mathbf{r} - \mathbf{r}')$ (treats saturation effects)

The paper systematically varies these interactions to assess robustness of predictions.

### Extended Pairing Fields in Drip-Line Nuclei

For a nucleus near the neutron drip line with separation energy $S_n \approx 1$ MeV, the pairing field:

$$\Delta(\mathbf{r}) = \int d\mathbf{r}' \, V(\mathbf{r}, \mathbf{r}') \kappa(\mathbf{r}, \mathbf{r}')$$

extends far beyond the nuclear surface. The spatial extent of the pair amplitude:

$$\xi_{\text{pair}} \sim \hbar / \sqrt{2 m_n |E_F|}$$

where $E_F$ is the Fermi energy (typically $E_F \approx -S_n/2$), becomes macroscopic—several femtometers. This extended structure fundamentally alters the pairing correlations compared to stable nuclei.

### Coupling to the Continuum

The crucial insight is that loosely bound cooper pairs couple resonantly to particle-emission channels. The pairing field couples the bound region to the continuum through:

$$V_{\text{eff}}(\mathbf{r}) = U_0(\mathbf{r}) + \Delta(\mathbf{r}) \sigma_x - \lambda$$

The pair potential $\Delta(\mathbf{r})$ does not vanish as $r \to \infty$ but instead approaches the asymptotic limit determined by the continuum coupling. This boundary condition differs qualitatively from traditional calculations where $\Delta(r \to \infty) = 0$.

---

## Key Results

1. **Continuum Importance**: Neglecting continuum effects overestimates binding energies by 1-3 MeV in drip-line nuclei, comparable to the total binding energy itself.

2. **Pairing Correlations Persist at Drip Line**: Despite extremely low density, significant pairing correlations survive in weakly bound systems. For $^{32}$Ne (extreme neutron drip line), the pairing gap remains $\Delta \approx 0.7$ MeV.

3. **Extended Pairing Fields**: Neutron halo nuclei like $^{11}$Li exhibit pair amplitudes extending to 8-10 fm, compared to typical 3-4 fm in stable nuclei.

4. **Density-Dependent Pairing**: Interactions with explicit density dependence better reproduce experimental halo sizes, suggesting the pairing strength depends on local nucleon density.

5. **Quadrupole Deformation**: Several nuclei near the drip line exhibit spontaneous quadrupole deformation due to the interplay of pairing and mean-field effects. For instance, $^{30}$Ne is predicted deformed despite low binding.

6. **Neutron Separation Energies**: Calculated two-neutron separation energies $S_{2n}$ agree with experiment to within 0.3 MeV, validating the theoretical approach.

---

## Key Equations

| Equation | Meaning |
|:---------|:--------|
| $E = \int d\mathbf{r} \epsilon_{\text{sp}}(\mathbf{r}) \rho(\mathbf{r})$ | Single-particle energy density |
| $\Delta(\mathbf{r}) = -G \sum_k u_k(\mathbf{r}) v_k(\mathbf{r})$ | Pairing field definition |
| $\kappa(\mathbf{r}) = \sum_k u_k(\mathbf{r}) v_k(\mathbf{r})$ | Pair amplitude (off-diagonal density) |
| $S_n = E(N-1) - E(N)$ | Neutron separation energy |
| $E_F = -\mu = -(E(N) - E(N-1))$ | Fermi energy (negative of $S_n/2$ approx.) |

---

## Connection to Phonon-Exflation Framework

Pairing in drip-line nuclei exemplifies how collective correlations emerge at the edge of stability. In the phonon-exflation model, nuclear pairing is reinterpreted as a phononic excitation of the internal SU(3) compactification. The extended pairing fields observed by Dobaczewski and Nazarewicz—spanning many femtometers in halo systems—would correspond to collective modes of the deformed SU(3) metric that couple resonantly to the unbound continuum.

The BCS mechanism in weakly bound systems bears direct analogy to the framework's treatment of Cooper pairing in the spectral triple. When binding weakens, pairing correlations remain robust because they tap into the collective degree of freedom of the underlying geometry. The framework predicts that the pairing strength (analogous to G in the contact interaction) should depend on the spectral density of the Dirac operator on the deformed 3-manifold at threshold—a prediction that Dobaczewski's density-dependent interactions partially capture empirically.

Furthermore, the cusp-like structure of the continuum density of states near threshold would be reflected in the phonon density of states of the internal manifold, with implications for the energy-dependence of pairing interactions predicted by the phonon-exflation model.

---

## References

- Dobaczewski, J., Nazarewicz, W., Werner, T.R., et al. (1994). Mean-field description of ground-state properties of drip-line nuclei: Shell-correction method. Phys. Rev. C 50, 2860-2889.
- Flocard, H., Heenen, P.H., Vautherin, D. (1973). Generator coordinate method. Nucl. Phys. A 231, 176-208.
- Bender, M., Heenen, P.H., Reinhard, P.-G. (2003). Self-consistent mean-field models for nuclear structure. Rev. Mod. Phys. 75, 121-180.

