# Hartree-Fock-Bogoliubov Solution of the Pairing Hamiltonian in Finite Nuclei

**Author(s):** J. Dobaczewski, W. Nazarewicz

**Year:** 2013

**Journal:** 50 Years of Nuclear BCS, Ed. R.A. Broglia & V. Zelevinsky

---

## Abstract

A comprehensive treatment of the Hartree-Fock-Bogoliubov (HFB) framework for nucleonic superfluidity in finite systems is presented. The work explains how correlated pairs are incorporated into the HFB wave function and derives the fundamental HFB equations used in nuclear density functional theory. Key topics include the unitarity of the Bogoliubov transformation in truncated spaces, pairing functional forms, HFB continuum structure, regularization and renormalization of pairing fields, and treatment of systems with odd particle numbers. This review provides the theoretical foundation for modern applications of nuclear pairing theory to exotic nuclei and extreme conditions.

---

## Historical Context

The Bardeen-Cooper-Schrieffer (BCS) theory of nuclear pairing, formulated in 1958-1960, revolutionized nuclear physics by explaining the universal occurrence of even-odd mass staggering and nuclear superfluidity. However, BCS theory rests on several approximations: (1) it assumes a filling fraction (number of bound pairs) remains approximately constant, and (2) it utilizes a sharp cutoff in energy space. These assumptions fail for finite nuclei, where the number of nucleons is fixed and energy cutoffs introduce unphysical artifacts.

The Hartree-Fock-Bogoliubov theory, developed by Valatin and others in the 1960s-1970s, generalized BCS by allowing arbitrary quasiparticle configurations. In the 1990s, Dobaczewski and collaborators reformulated HFB in coordinate space to handle the continuum explicitly. By the 2010s, HFB had become the standard framework for nuclear density functional theory applied to unstable isotopes.

This pedagogical review distills three decades of theoretical development into a coherent exposition.

---

## Key Arguments and Derivations

### The HFB Wave Function

The fundamental ansatz is:

$$|\Psi_{\text{HFB}} \rangle = \prod_{k=1}^{M} \left( u_k + v_k c^\dagger_k c^\dagger_{\overline{k}} \right) |\text{vac}\rangle$$

where $k$ indexes a single-particle basis (bound and continuum), $\overline{k}$ denotes the time-reversed state, and $|u_k|^2 + |v_k|^2 = 1$. The coefficients $u_k$ and $v_k$ are called Bogoliubov amplitudes. The state $|\Psi_{\text{HFB}} \rangle$ is an eigenstate of a general two-body Hamiltonian within the restricted space of quasiparticle configurations.

### Bogoliubov Transformation

The fundamental operation that defines HFB is the Bogoliubov transformation, which relates creation and annihilation operators in the original basis to quasiparticle operators:

$$a_k = u_k \gamma_k + v_k^\dagger \gamma_{\overline{k}}^\dagger$$
$$a^\dagger_k = u_k^\dagger \gamma_k^\dagger + v_k^\dagger \gamma_{\overline{k}}$$

where $\gamma_k$ are quasiparticle operators satisfying canonical anticommutation relations $\{\gamma_k, \gamma^\dagger_{k'}\} = \delta_{kk'}$. The transformation is unitary if both sets of operators satisfy the canonical algebra, which imposes the constraint:

$$|u_k|^2 + |v_k|^2 = 1$$

This unitarity ensures that the Fock vacuum $|\text{vac}\rangle$ transforms into the quasiparticle vacuum $|\Phi\rangle = \prod_k \gamma^\dagger_k \gamma_{\overline{k}} |\text{vac}\rangle$.

### Truncation and Non-Orthogonality

In practice, computations truncate the single-particle space to a finite model space of M orbitals (M ~ 1000 for modern calculations). The Bogoliubov transformation remains unitary within this truncated space, but the HFB equations themselves are approximate because:

1. **Basis truncation**: Continuum and scattering states at high energy are omitted.
2. **Effective interaction**: The bare nucleon-nucleon force is replaced by an effective interaction fitted to nuclear properties.
3. **Hartree-Fock approximation**: The mean-field potential is computed self-consistently but ignores many-body correlations beyond pairing.

These limitations are inherent and can only be assessed through comparison with experiment and benchmark calculations.

### The HFB Equations

The canonical HFB equations arise from the variational principle $\delta E / \delta \rho = 0$ applied to the energy functional:

$$E[\rho, \kappa] = \text{Tr}[h \rho] + \frac{1}{2} \text{Tr}[V \rho \rho] + \text{Tr}[\Delta \kappa^*]$$

where $\rho(\mathbf{r}, \mathbf{r}') = \langle c^\dagger(\mathbf{r}') c(\mathbf{r}) \rangle$ is the density matrix and $\kappa(\mathbf{r}, \mathbf{r}') = \langle c(\mathbf{r}) c(\mathbf{r}') \rangle$ is the pair amplitude. The resulting equations read:

$$\begin{pmatrix} h - \lambda & \Delta \\ -\Delta^\dagger & -h^* + \lambda \end{pmatrix} \begin{pmatrix} u_k \\ v_k \end{pmatrix} = E_k \begin{pmatrix} u_k \\ v_k \end{pmatrix}$$

The mean-field potential includes both direct (Hartree) and exchange (Fock) terms:

$$h = \frac{\mathbf{p}^2}{2m} + U_{\text{ext}} + U_0[\rho]$$

The pairing field is:

$$\Delta(\mathbf{r}, \mathbf{r}') = -\frac{1}{2} \langle \mathbf{r}, \mathbf{r}' | V | \psi_k, \psi_{\overline{k}} \rangle \kappa^*(\mathbf{r}, \mathbf{r}')$$

summed over all bound and continuum quasiparticle pairs.

### Pairing Functional Form

Several functional forms are commonly employed:

1. **Contact (zero-range) pairing**: $\Delta(\mathbf{r}) = -G_0 \rho_c(\mathbf{r})$ where $\rho_c$ is the pair density. Simple but divergent in large spaces.

2. **Gogny-type pairing**: Separable expansion of the finite-range Gogny force allowing efficient computation.

3. **Density-dependent**: $\Delta(\mathbf{r}) = -G_0 [1 - \eta \rho(\mathbf{r})] \rho_c(\mathbf{r})$, which partially compensates for the divergence of the contact interaction.

The choice of pairing functional affects predictions for drip-line nuclei and deformed systems.

### Continuum Hartree-Fock-Bogoliubov (CHFB)

For weakly bound nuclei near particle emission thresholds, the continuum cannot be truncated. The **Berggren contour** method solves this by deforming the integration path into the complex k-plane:

$$\int_{\text{contour}} \frac{dk}{2\pi i} \, (\cdots)$$

This contour encircles the real k-axis (bound states at k=i\kappa) and includes resonance poles in the fourth quadrant (Gamow poles with decay width). The completeness relation:

$$\sum_{k \in \text{bound}} |\phi_k\rangle\langle\phi_k| + \int_{\text{contour}} \frac{dk}{2\pi i} |\phi_k\rangle\langle\phi_k| = 1$$

is recovered to arbitrary precision by choosing the contour appropriately.

### Odd-Particle Systems

For nuclei with an unpaired nucleon (odd-A systems), the HFB formalism extends naturally. The unpaired particle occupies one orbital (with $v_k = 0, u_k = 1$ for that orbital), while the remaining A-1 nucleons form pairs via the standard HFB wave function. This leads to a modified mean-field potential with blocking effects—the presence of an unpaired particle alters the pairing correlations of the remaining nucleons.

---

## Key Results

1. **Universal Applicability**: The HFB framework correctly describes both weakly bound halos ($^{11}$Li) and strongly bound magic nuclei ($^{208}$Pb) with a single unified theory.

2. **Pairing Gap Predictions**: HFB calculations predict odd-even mass staggering $\Delta_{odd-even} = E(A) - E(A-1) - E(A+1) + E(A-2)$ to within 0.1 MeV across the nuclear chart.

3. **Superfluid Transition**: HFB predicts a gradual transition to superfluidity—pairing gaps increase from zero at closed shells to maximum near the middle of a shell (filling fraction f~0.5).

4. **Deformed Superfluids**: HFB correctly describes superfluid nuclei with spontaneous breaking of rotational symmetry (deformed paired nuclei), explaining the observation of identical bands in physically distinct configurations.

5. **Separable Pair Approximation**: The HFB solution can be approximated by a two-body effective Hamiltonian under certain conditions, recovering a generalized BCS theory with finite number of nucleons.

---

## Key Equations

| Quantity | Definition |
|:---------|:-----------|
| Bogoliubov transformation | $a_k = u_k \gamma_k + v^\dagger_k \gamma^\dagger_{\bar{k}}$ |
| Normalization | $\|u_k\|^2 + \|v_k\|^2 = 1$ |
| HFB eigenvalue equation | $(h - \lambda) u_k + \Delta v_k = E_k u_k$ |
| HFB eigenvalue equation | $-\Delta^\dagger u_k - (h^* - \lambda) v_k = E_k v_k$ |
| Density matrix | $\rho(\mathbf{r}, \mathbf{r}') = \sum_k u_k(\mathbf{r}) v_k^*(\mathbf{r}')$ |
| Pair amplitude | $\kappa(\mathbf{r}, \mathbf{r}') = \sum_k u_k(\mathbf{r}) u_k(\mathbf{r}')$ |
| Pairing field | $\Delta(\mathbf{r}) = -G(1 - \eta \rho(\mathbf{r})) \kappa(\mathbf{r})$ |

---

## Connection to Phonon-Exflation Framework

The HFB theory represents the most sophisticated mean-field approach to nuclear pairing currently employed. In the phonon-exflation framework, the BCS pairing mechanism occurs at the level of the spectral triple (M4 x SU(3), D_K, spectral action). The framework proposes that what HFB treats as an effective two-body pairing interaction is actually a manifestation of collective phononic excitations of the internal compactification.

Key correspondences:

1. **Pairing functional**: The density-dependent pairing strength $G(\rho)$ in HFB would correspond to the spectral density of the Dirac operator on the deformed SU(3) manifold, modulated by the local metric structure.

2. **Continuum coupling**: The explicit treatment of continuum effects in the Berggren contour formalism parallels the framework's handling of resonance modes that couple to the uncompactified dimensions.

3. **Spontaneous symmetry breaking**: The HFB description of superfluid symmetry breaking (pairing condensate forming) mirrors the framework's treatment of gauge symmetry breaking through condensation on the SU(3) fiber.

4. **Mean-field self-consistency**: The self-consistent HFB equations reflect the framework's principle that collective modes generate their own mean-field potential through the spectral action.

The phonon-exflation perspective suggests that anomalies in pairing predictions (e.g., the density-dependent interaction required to match experiment) may hint at a deeper structure where pairing emerges from the internal geometry's phonon spectrum.

---

## References

- Broglia, R.A., Zelevinsky, V. (Eds.) (2013). 50 Years of Nuclear BCS. World Scientific.
- Bardeen, J., Cooper, L.N., Schrieffer, J.R. (1957). Theory of superconductivity. Phys. Rev. 108, 1175-1204.
- Valatin, J.G. (1961). Comments on the theory of superconductivity. Nuovo Cimento 7, 843-857.
- Marshalek, E.R., Weneser, J. (1969). The pairing interaction in nuclei. Ann. Phys. (N.Y.) 53, 569-635.

