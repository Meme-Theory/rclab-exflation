# Iterative Solutions of the ATDHFB Equations to Determine the Nuclear Collective Inertia

**Author(s):** Xuwei Sun, Jacek Dobaczewski, Markus Kortelainen, David Muir, Jhilam Sadhukhan, Adrian Sanchez-Fernandez, Herlik Wibowo
**Year:** 2024
**Journal:** Acta Physica Polonica B (Proceedings of the 57th Zakopane Conference on Nuclear Physics)
**arXiv:** 2411.18404
**Relevance:** HIGH

---

## Abstract

An iterative adiabatic time-dependent Hartree-Fock-Bogoliubov (ATDHFB) method is developed within the framework of Skyrme density functional theory. The ATDHFB equation is solved iteratively to avoid explicitly calculating the stability matrix. The contribution of the time-odd mean fields to the ATDHF(B) moment of inertia is incorporated self-consistently, and the results are verified by comparing them with the dynamical cranking predictions. The inertia mass tensor is calculated with the density-derivative term evaluated by numerical differentiation.

---

## Key Arguments and Derivations

### Section 2: Formalism

The time-dependent density is decomposed as $\rho(t) = e^{(i/\hbar)\chi(t)} \rho_0(t) e^{(-i/\hbar)\chi(t)}$, where $\rho_0(t)$ and $\chi(t)$ are Hermitian, time-even operators serving as collective coordinates and momenta respectively. The first-order correction is $\rho_1 = [i\chi, \rho_0]$, and the ATDHF equation becomes $i\dot{\rho}_0 = [h_0, \rho_1] + [\Gamma_1, \rho_0]$, where $h_0$ is the static single-particle Hamiltonian and $\Gamma_1$ is the time-odd mean field.

The collective kinetic energy $K = \frac{1}{2}\mathrm{Tr}(\dot{\rho}_0 \chi) = -\frac{i}{2}\mathrm{Tr}(\dot{\rho}_0[\rho_1, \rho_0])$ yields the collective inertia $M = -i \mathrm{Tr}(\dot{\rho}_0[\rho_1, \rho_0]) / \dot{q}^2$.

The key innovation is the iterative solution. In the HF single-particle basis:
$$\rho^{(n+1)}_{1,ph} = \frac{1}{\epsilon_p - \epsilon_h}\left[i\dot{q}\frac{\partial\rho_{0,ph}}{\partial q} - \Gamma^{(n)}_{1,ph}\right]$$

Starting from $\Gamma^{(0)}_1 = 0$ (Inglis-Belyaev value), each iteration updates $\rho_1 \to \Gamma_1 \to \rho_1$ until the collective mass converges. The adiabatic basis of $\rho_1$ eigenstates consists of $2N$ "occupied" states with eigenvalues $\pm r$ (from SVD decomposition), analogous to the HF basis. This allows standard calculation of time-odd densities and currents.

The method avoids the full two-body stability matrix entirely, working only with one-body operators. This is a decisive computational advantage for deformed superfluid nuclei.

### Section 3.1: Rotational Inertia of $^{20}$Ne (Axial)

The ATDHF moment of inertia is compared with dynamical cranking (DC) at $\omega_y = 0.001$ MeV. Perfect agreement is achieved when all particle states are included (sensitive to single-particle energy cutoff). The dominant time-odd contributions come from the current density $\mathbf{j}(\mathbf{r})$ and spin density $\mathbf{s}(\mathbf{r})$.

### Section 3.2: Rotational Inertia of $^{126}$Ba (Triaxial)

For the triaxially deformed nucleus ($\beta = 0.18$, $\gamma = 40.13°$), ATDHF moments of inertia along all three principal axes agree perfectly with DC results. Example: $I^{\mathrm{ATDHF}}_y = 13.14124$ vs $I^{\mathrm{DC}}_y = 13.1417$ $\hbar^2$/MeV, both significantly larger than the Inglis-Belyaev value $I^{\mathrm{IB}}_y = 9.84689$ $\hbar^2$/MeV. The moments of inertia are invariant under spatial reorientation of the principal axes, validating self-consistency.

### Section 3.3: Vibrational Inertia of $^{74}$Ge (ATDHFB)

The quadrupole inertia mass tensor $B(a_0, a_2)$ is calculated using numerical differentiation of the density derivative. With SkM* interaction and volume pairing, diagonal components stabilize within 1% accuracy for $\Delta \leq 0.02$ b. Off-diagonal component $B(a_0 a_2)$ is more sensitive, with ~4% uncertainty from numerical differentiation.

## Key Results

1. Iterative ATDHF(B) method achieves exact agreement with dynamical cranking for rotational inertia
2. Time-odd mean fields increase rotational inertia by factor ~1.2-1.4 over Inglis-Belyaev values
3. Method involves only one-body operators, avoiding the prohibitive two-body stability matrix
4. Dominant time-odd contributions: current density $\mathbf{j}(\mathbf{r})$ and spin density $\mathbf{s}(\mathbf{r})$
5. Triaxial nuclei: inertia along all three principal axes correctly reproduced; invariant under reorientation
6. Vibrational mass tensor: diagonal components to 1% accuracy, off-diagonal to ~4%
7. Full single-particle space required for convergence (sensitive to energy cutoff)
8. Implemented in HFODD code for arbitrarily deformed superfluid nuclei

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Time-dependent density decomposition | $\rho(t) = e^{(i/\hbar)\chi(t)} \rho_0(t) e^{(-i/\hbar)\chi(t)}$ | Eq. (1) |
| First-order density correction | $\rho_1 = [i\chi, \rho_0]$ | Eq. (2) |
| ATDHF equation | $i\dot{\rho}_0 = [h_0, \rho_1] + [\Gamma_1, \rho_0]$ | Eq. (3) |
| Collective kinetic energy | $K = \frac{1}{2}\mathrm{Tr}(\dot{\rho}_0 \chi) = -\frac{i}{2}\mathrm{Tr}(\dot{\rho}_0[\rho_1, \rho_0])$ | Eq. (4) |
| Collective inertia | $M = -i\,\mathrm{Tr}(\dot{\rho}_0[\rho_1, \rho_0]) / \dot{q}^2$ | Eq. (5) |
| Iterative ph density | $\rho^{(n+1)}_{1,ph} = \frac{1}{\epsilon_p - \epsilon_h}\left[i\dot{q}\frac{\partial\rho_{0,ph}}{\partial q} - \Gamma^{(n)}_{1,ph}\right]$ | Eq. (6) |
| SVD of $\rho_1$ | $\rho_1 = \begin{pmatrix} 0 & UrV^+ \\ VrU^+ & 0 \end{pmatrix}$ | Eq. (7) |
| Adiabatic basis eigenstates | $\rho_1 \begin{pmatrix} U \\ \pm V \end{pmatrix} = \pm \begin{pmatrix} U \\ \pm V \end{pmatrix} r$ | Eq. (8) |
| Numerical density derivative | $\frac{\partial\rho}{\partial q}\big|_{q_0} = \lim_{\delta q \to 0} \frac{\rho[q_0 + \delta q] - \rho[q_0]}{\delta q}$ | Eq. (11) |
| Vibrational mass tensor | $M = \begin{pmatrix} B(a_0) & B(a_0 a_2) \\ B(a_2 a_0) & B(a_2) \end{pmatrix}$ | Eq. (12) |

## Relevance to Phonon-Exflation

This paper provides the precise nuclear physics methodology underlying the collective inertia $M_{\mathrm{ATDHFB}} = 1.695$ computed in S40 for the tau-transit. The iterative ATDHF(B) method directly parallels the framework's need to compute collective inertia for geometry changes on the SU(3) fiber: $\rho_0$ maps to the equilibrium density on the fiber, $\Gamma_1$ to the time-odd response from BCS pairing, and the iteration $\Gamma^{(0)}_1 = 0 \to$ Inglis-Belyaev $\to$ full ATDHFB mirrors the correction chain from naive perturbative to non-perturbative inertia. The 1.2-1.4x enhancement from time-odd fields over Inglis-Belyaev is the nuclear calibration for the inverted Born-Oppenheimer regime (S38: geometry fast, pairing slow). The adiabatic basis decomposition (Eq. 7-8) provides the SVD structure needed for the BdG spectral flow during transit.
