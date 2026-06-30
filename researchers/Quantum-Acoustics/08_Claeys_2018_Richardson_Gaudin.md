# Richardson-Gaudin Models and Broken Integrability

**Author(s):** Pieter W. Claeys
**Year:** 2018
**Journal:** Ph.D. Thesis, Ghent University; Academic Year 2017-2018
**arXiv:** 1809.04447
**Supervisors:** Prof. Dr. Dimitri Van Neck, Dr. Stijn De Baerdemacker
**Relevance:** CRITICAL

---

## Abstract

[The thesis does not contain a single abstract. The following is synthesized from the introduction (Chapter 1).]

This thesis provides a comprehensive treatment of Richardson-Gaudin (RG) integrable models, their Bethe ansatz solutions, and extensions to integrability-breaking perturbations. Part I develops the theoretical framework: the Generalized Gaudin Algebra (GGA), Bethe ansatz eigenstates, eigenvalue-based numerical methods, inner products, and form factors. Part II applies this framework to three physical problems: Read-Green resonances in topological superconductors coupled to a bath (Chapter 6), variational Bethe ansatz methods for integrability-breaking Hamiltonians (Chapter 7), and Floquet dynamics from integrability in periodically driven systems (Chapter 8). The central theme is that integrable models and their Bethe ansatz provide a powerful toolbox extending beyond exactly solvable systems.

---

## Key Arguments and Derivations

### Part I: Richardson-Gaudin Models

#### Chapter 2: Richardson-Gaudin Integrability

**Classical integrability.** A system with $L$ degrees of freedom is Liouville-integrable if it possesses $L$ independent integrals of motion in involution: $\{Q_i, Q_j\} = 0$. This reduces dynamics to the algebraic problem of finding canonical conjugate variables (Liouville-Arnol'd theorem). The simplest example is the diagonalization of the mass-weighted interaction matrix in a coupled oscillator system, reducing to normal modes.

**Quantum integrability.** No straightforward extension exists. Demanding $[\hat{Q}_i, \hat{H}] = [\hat{Q}_i, \hat{Q}_j] = 0$ is too weak (the spectral theorem provides projectors as trivial conserved charges for any Hamiltonian). The key additional requirement is that conserved charges lead to loss of ergodicity in the infinite system limit, excluding trivial projectors but including Yang-Baxter integrable and many-body localized systems. Berry-Tabor conjecture: integrable spectra follow Poisson statistics; non-integrable spectra follow Wigner-Dyson (GOE).

**RG models from the GGA.** Starting from $L$ copies of $\text{su}(2)$ with generators $\{S^+_i, S^-_i, S^z_i\}$, non-interacting conserved charges $Q_i = S^z_i$ are extended to interacting ones:

$$Q_i = S^z_i + g\sum_{j \neq i}\left[X_{ij}\frac{1}{2}(S^+_i S^-_j + S^-_i S^+_j) + Z_{ij} S^z_i S^z_j\right]$$

Commutativity $[Q_i, Q_j] = 0$ requires $X_{ij}$ and $Z_{ij}$ to satisfy the Gaudin equations:

$$X_{ij}X_{jk} - X_{ik}(Z_{ij} + Z_{jk}) = 0$$

Three solution classes: **rational** ($X = Z = 1/(\epsilon_i - \epsilon_j)$, XXX model), **trigonometric** ($X = 1/\sin(\epsilon_i - \epsilon_j)$, $Z = \cot(\epsilon_i - \epsilon_j)$), **hyperbolic** ($X = 1/\sinh(\epsilon_i - \epsilon_j)$, $Z = \coth(\epsilon_i - \epsilon_j)$).

**Generalized Gaudin Algebra.** An infinite-dimensional Lie algebra with operators $S^{x,y,z}(u)$ parametrized by spectral parameter $u \in \mathbb{C}$, satisfying:

$$[S^\alpha(u), S^\alpha(v)] = 0, \quad \alpha = x, y, z$$

and mixed commutators involving structure functions $X(u,v)$, $Y(u,v)$, $Z(u,v)$. The Casimir-like operators $S^2(u) = S^x(u)^2 + S^y(u)^2 + S^z(u)^2$ generate a continuous family of mutually commuting operators: $[S^2(u), S^2(v)] = 0$.

**Bethe ansatz.** Eigenstates are product wave functions:

$$|v_1 \cdots v_N\rangle = \prod_{a=1}^N S^+(v_a)|0\rangle$$

with rapidities $\{v_a\}$ satisfying the Richardson-Gaudin (Bethe) equations:

$$F^z(v_a) + \sum_{b \neq a} Z(v_b, v_a) = 0, \quad a = 1, \ldots, N$$

This scales linearly in excitation number $N$ rather than exponentially in system size $L$.

#### The Reduced BCS Model (Section 2.7.2)

Richardson's exact solution describes fermion pair scattering with level-independent pairing:

$$H_{\text{BCS}} = \sum_i 2\epsilon_i\left(S^z_i + \frac{\Omega_i}{4}\right) + g\sum_{i,j} S^+_i S^-_j$$

where $S^+_i = \sum_{m_i > 0} a^\dagger_{m_i} a^\dagger_{\bar{m}_i}$ creates a Cooper pair via quasi-spin algebra. The eigenstates are Bethe ansatz states with rapidities $v_a$ interpreted as half the pair energy ($E = 2\sum_a v_a + \sum_i \epsilon_i\Omega_i$). The Bethe equations in the thermodynamic limit reproduce the BCS mean-field gap equation; Richardson's exact solution handles ultrasmall grains where number fluctuations cannot be neglected.

#### The $p_x + ip_y$-Wave Pairing Hamiltonian (Section 2.7.3)

Describes chiral interaction between 2D fermions supporting a topological phase transition between weak-pairing (topologically non-trivial) and strong-pairing (trivial) phases:

$$H_{p+ip} = \sum_k \frac{|k|^2}{2m} a^\dagger_k a_k + \frac{G}{4m}\sum_{k,k'} (k_x + ik_y)(k'_x - ik'_y) a^\dagger_k a^\dagger_{-k} a_{-k'} a_{k'}$$

The conserved charges correspond to an XXZ Gaudin algebra with $X(u,v) = 2\sqrt{uv}/(u-v)$ and $Z(u,v) = (u+v)/(u-v)$.

#### Chapter 3: Eigenvalue-Based Framework

The key innovation: instead of solving for rapidities (which exhibit singularities at "singular points"), define eigenvalue-based variables $\Lambda_i = \sum_a Z(\epsilon_i, v_a)$. These satisfy quadratic equations:

$$\Lambda_i^2 = \frac{2}{g}\Lambda_i + \sum_{j \neq i} Z(\epsilon_i, \epsilon_j)(\Lambda_i - \Lambda_j) + N(L - N)$$

supplemented by $-\frac{g}{2}\sum_i \Lambda_i = N$. Advantages: (1) no singular behavior, (2) variables are necessarily real (eigenvalues of Hermitian operators), (3) completeness guaranteed by construction, (4) physical interpretation via Hellmann-Feynman theorem: $\langle S^z_i \rangle = -\frac{1}{2} + \frac{g}{2}\frac{\partial\Lambda_i}{\partial g}$.

#### Chapter 4: Inner Products

Determinant expressions for inner products (Slavnov determinant) and form factors derived via dual states and Domain Wall Partition Functions (DWPFs), connecting to the Izergin-Borchardt determinant through properties of Cauchy matrices.

### Part II: Applications

#### Chapter 6: Read-Green Resonances

A topological $p_x + ip_y$ superconductor coupled to an environment (bath) that permits particle exchange. At each Read-Green point (where a zero-energy excitation exists), the topological phase transition becomes an avoided level crossing between states with different particle numbers. The system absorbs Cooper pairs from the bath, remaining in the topologically non-trivial phase. Mean-field theory completely fails to capture these finite-size resonances. The exact Bethe ansatz solution reveals a clear separation of rapidity scales: rapidities with $|v^2_a| \ll |\mu|$ are dormant zero modes that activate at Read-Green points.

#### Chapter 7: Variational Bethe Ansatz

For integrability-breaking perturbations, Bethe ansatz states serve as variational wave functions. The method: (1) use the Bethe ansatz structure with rapidities as variational parameters, (2) minimize energy using gradient descent on the Bethe equations. Applied to central spin models with inhomogeneous couplings (breaking integrability), the variational Bethe ansatz accurately captures the ground state and low-lying spectrum. A Richardson-Gaudin Configuration Interaction (RGCI) method is also developed for nuclear pairing problems, using Bethe ansatz states as a many-body basis for diagonalization.

#### Chapter 8: Floquet Dynamics from Integrability

**Floquet theory.** For periodically driven systems $H(t + T) = H(t)$, the Floquet theorem gives $U(T) = P(T)e^{-iH_F T}$ with $H_F$ the Floquet Hamiltonian and $P(t)$ periodic. The Floquet-Magnus expansion:

$$H_F^{(0)} = H_{\text{Avg}}, \quad H_F^{(1)} = \frac{iT}{4}[H_{\text{Avg}}, V], \quad H_F^{(2)} = \frac{T^2}{24}[[H_{\text{Avg}}, V], V]$$

where $H_{\text{Avg}} = \delta H_1 + (1-\delta)H_2$ and $V = \delta H_1 - (1-\delta)H_2$.

**Many-body resonances.** At driving periods where $E_f - E_0 = 2\pi/T$, eigenstates of $H_{\text{Avg}}$ become quasi-degenerate in the Floquet spectrum, hybridize, and form superpositions --- many-body resonances. These dominate the Floquet spectrum in the crossover regime and lead to adiabatic transitions: slowly sweeping the driving frequency across a resonance transfers the system from the ground state to a highly excited state of $H_{\text{Avg}}$.

**Application to driven central spin model.** Periodically switching $B_z$ between two values, the Floquet operator is constructed in a 2D basis of quasi-degenerate Bethe states. This exploits the integrability of the static Hamiltonians (efficient construction of eigenstates and overlaps) to model the non-integrable Floquet dynamics. Remarkably, Floquet resonances produce near-complete spin polarization of the central spin ($\langle S^z_0 \rangle \to 1/2$) at the second-order resonance.

**Floquet phases.** Each Floquet phase $\phi_n$ has two contributions: a dynamical phase $\langle n|H_{\text{Avg}}|n\rangle$ (average energy during one cycle) and a nonadiabatic Berry phase $\langle n|H_F - H_{\text{Avg}}|n\rangle$ (from higher-order Magnus terms). Two energy measures: $\phi_n/T = \langle n|H_F|n\rangle$ (quasi-energy) and $\partial_T \phi_n = \langle n|H_{\text{Avg}}|n\rangle$ (dynamical energy).

## Key Results

1. Richardson-Gaudin models are exactly solvable via Bethe ansatz, with eigenstates scaling linearly in excitation number $N$ rather than exponentially in system size $L$.
2. The eigenvalue-based framework eliminates singular behavior in the Bethe equations, providing a numerically stable and complete description with real-valued variables.
3. The reduced BCS Hamiltonian is a Richardson-Gaudin integrable model; its exact solution recovers BCS mean-field in the thermodynamic limit but handles ultrasmall grains where mean-field breaks down.
4. Read-Green resonances in topological superconductors coupled to a bath: the topological phase transition becomes an avoided crossing; zero-energy excitations are absorbed from the environment.
5. The variational Bethe ansatz captures ground states and low-lying spectra of integrability-broken models, demonstrating that integrable structure persists approximately under perturbation.
6. Floquet many-body resonances in driven integrable systems are modeled by constructing the Floquet operator in a restricted Bethe-state basis; this enables study of large systems inaccessible to exact diagonalization.
7. Adiabatic transitions through Floquet resonances achieve near-complete spin polarization of a central spin.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Conserved charges | $Q_i = S^z_i + g\sum_{j\neq i}[X_{ij}\frac{1}{2}(S^+_i S^-_j + S^-_i S^+_j) + Z_{ij}S^z_i S^z_j]$ | Eq. (2.12) |
| Gaudin equations | $X_{ij}X_{jk} - X_{ik}(Z_{ij} + Z_{jk}) = 0$ | Eq. (2.14) |
| GGA Casimir | $S^2(u) = S^x(u)^2 + S^y(u)^2 + S^z(u)^2$, $[S^2(u), S^2(v)] = 0$ | Eqs. (2.22)-(2.23) |
| Bethe ansatz state | $\|v_1\cdots v_N\rangle = \prod_{a=1}^N S^+(v_a)\|0\rangle$ | Eq. (2.32) |
| Bethe equations | $F^z(v_a) + \sum_{b\neq a} Z(v_b, v_a) = 0$ | Eq. (2.36) |
| BCS Hamiltonian | $H_{\text{BCS}} = \sum_i 2\epsilon_i(S^z_i + \Omega_i/4) + g\sum_{ij} S^+_i S^-_j$ | Eq. (2.53) |
| BCS energy | $E = 2\sum_a v_a + \sum_i \epsilon_i\Omega_i$ | Eq. (2.58) |
| BCS Bethe eqns | $1/g + \sum_j d_j/(\epsilon_j - v_a) - \sum_{b\neq a} 1/(v_b - v_a) = 0$ | Eq. (2.57) |
| Eigenvalue-based eqns | $\Lambda_i^2 = (2/g)\Lambda_i + \sum_{j\neq i}Z(\epsilon_i,\epsilon_j)(\Lambda_i - \Lambda_j) + N(L-N)$ | Eq. (3.8) |
| Constraint | $-(g/2)\sum_i \Lambda_i = N$ | Eq. (3.10) |
| Occupation from $\Lambda$ | $\langle S^z_i\rangle = -1/2 + (g/2)\partial\Lambda_i/\partial g$ | Eq. (3.18) |
| Floquet theorem | $U(T) = P(T)e^{-iH_F T}$ | Eq. (8.1) |
| Floquet-Magnus $H_F^{(0)}$ | $H_F^{(0)} = H_{\text{Avg}} = \delta H_1 + (1-\delta)H_2$ | Eq. (8.7) |
| Floquet phase | $\phi_n = \int_0^T \langle n(t)\|H(t)\|n(t)\rangle dt - i\int_0^T \langle n(t)\|\partial_t\|n(t)\rangle dt$ | Eq. (8.9) |
| Resonance condition | $E_f - E_0 = 2\pi n/T$ | Sec. 8.1.2 |
| Floquet 2-level model | $U_F \approx \begin{pmatrix}e^{-iE_0T} & i\epsilon e^{-i(E_0+E_f)T/2}\\i\epsilon e^{-i(E_0+E_f)T/2} & e^{-iE_fT}\end{pmatrix}$ | Eq. (8.13) |
| $p+ip$ conserved charges | $X(u,v) = 2\sqrt{uv}/(u-v)$, $Z(u,v) = (u+v)/(u-v)$ | Eq. (2.63) |

## Relevance to Phonon-Exflation

This thesis is the mathematical backbone of the phonon-exflation framework's BCS/integrability program. Specifically: (1) The Richardson-Gaudin exact solution of the reduced BCS model is the formalism used in Sessions 35-38 to analyze the pairing instability on SU(3), where the 8 Richardson-Gaudin conserved integrals are the quantities protecting the GGE relic from thermalization. (2) The eigenvalue-based framework (Chapter 3) is the computational method applied to solve the Bethe equations for the framework's BCS condensate at arbitrary coupling. (3) The Floquet dynamics chapter directly informs the transit physics: the periodic quench protocol is analogous to the instanton gas dynamics, and the Floquet many-body resonances parallel the avoided crossings in the framework's spectral landscape. (4) The Berry-Tabor conjecture and the Poisson level statistics of integrable models are precisely what was verified in Session 38 (CHAOS-1: $\langle r \rangle = 0.321$, sub-Poisson), confirming that the Dirac spectrum on SU(3) is integrable.
