# Richardson-Gaudin models and broken integrability

**Author(s):** Pieter W. Claeys
**Year:** 2018
**Journal:** PhD Thesis, Ghent University
**arXiv:** 1809.04447
**Relevance:** HIGH — off-Jensen integrability breaking

---

## Abstract

[From thesis abstract, extracted from PDF]

This thesis presents a study of Richardson-Gaudin (RG) integrable models and their applications, with particular emphasis on what happens when integrability is broken. Part I develops the mathematical framework: RG integrability from the generalized Gaudin algebra, an eigenvalue-based numerical method avoiding singular Richardson equations, determinant expressions for inner products and form factors, and the contraction limit connecting to the Dicke and $p_x + ip_y$ models. Part II applies this framework to three physical problems: Read-Green resonances in topological superconductors coupled to a bath, variational methods using Bethe ansatz states for integrability-breaking Hamiltonians, and Floquet dynamics of periodically driven integrable systems. The thesis demonstrates that Richardson-Gaudin states provide a powerful variational basis even for non-integrable Hamiltonians, and that periodic driving of integrable systems produces rich many-body resonance structure.

---

## Key Arguments and Derivations

### Part I: Richardson-Gaudin Integrability

**Chapter 2: RG Integrability from Generalized Gaudin Algebra (GGA)**

The starting point is the su(2) algebra with generators $\{S_i^+, S_i^-, S_i^z\}$ for each spin-$s_i$ at site $i = 1, \ldots, L$. The GGA defines a set of commuting operators (conserved charges) through the requirement $[Q_i, Q_j] = 0$, where:

$$Q_i = S_i^z + g\sum_{j\neq i} \left[\frac{X_{ij}}{2}(S_i^+ S_j^- + S_i^- S_j^+) + Y_{ij}S_i^z S_j^z\right]$$

Three families of solutions exist (rational/XXX, trigonometric/XXZ, hyperbolic/XXZ), parameterized by free parameters $\{\epsilon_i\}$. The rational model has $X_{ij} = Y_{ij} = 1/(\epsilon_i - \epsilon_j)$.

**Physical Realizations (Section 2.7)**:

- **Central spin model**: One distinguished spin coupled uniformly to a bath of $L-1$ spins. Hamiltonian: $H_{CSM} = B_z S_0^z + \sum_{i=1}^{L-1} A_i(S_0^+ S_i^- + S_0^- S_i^+ + 2S_0^z S_i^z)$
- **Reduced BCS model**: Pairing Hamiltonian $H_{BCS} = \sum_i \epsilon_i \hat{n}_i + g\sum_{ij} S_i^+ S_j^-$. This is a linear combination of the rational RG conserved charges
- **$p_x + ip_y$ pairing**: Hyperbolic RG model with $H_{px+ipy} = \sum_i \epsilon_i \hat{n}_i + g\sum_{ij}\sqrt{\epsilon_i\epsilon_j}\,S_i^+ S_j^-$, relevant to topological superconductivity

**Chapter 3: Eigenvalue-Based Framework**

The traditional Richardson equations have singular points where pair energies collide. Claeys develops an eigenvalue-based method that circumvents these singularities by working directly with the eigenvalues $\Lambda_i$ of the conserved charges $Q_i$, which satisfy:

$$\Lambda_i^2 + (1 - 2s_i)\Lambda_i + g^2\sum_{j\neq i}\frac{s_i(2s_j + 1)\Lambda_i - s_j(2s_i + 1)\Lambda_j}{\epsilon_i - \epsilon_j} + g^2\sum_{j\neq i}\frac{\Lambda_i\Lambda_j - s_i s_j}{(\epsilon_i - \epsilon_j)^2}(2s_i + 1)(2s_j + 1) = 0$$

These equations are polynomial (no singularities) and can be solved by standard Newton methods. The pair energies can be recovered from the eigenvalues when needed.

**Chapter 4: Inner Products**

Determinant expressions for inner products between Bethe states are derived, connecting eigenvalue-based expressions to Slavnov's determinant formula through the concept of dual states. This enables efficient computation of correlation functions and form factors at polynomial cost.

**Chapter 5: Contraction Limit**

The Dicke model (atoms coupled to a single bosonic mode) is obtained as a contraction limit of the RG model when one spin representation is sent to infinity ($s_0 \to \infty$). Similarly, the extended $p_x + ip_y$ model with a bosonic mode is obtained from the hyperbolic family.

### Part II: Applications

**Chapter 6: Read-Green Resonances in Topological Superconductors**

The $p_x + ip_y$ pairing model undergoes a topological phase transition (Read-Green point) between a weak-pairing BCS phase and a strong-pairing BEC phase. When coupled to a bath (environment), the topological signatures survive: the Pfaffian sign changes at the Read-Green point, and this is detectable through the distribution of pair energies (rapidities). The bath coupling does not destroy the topological invariant but shifts the transition point.

**Chapter 7: Variational Method for Broken Integrability**

The central result for this project: RG Bethe states are used as variational ansatz for non-integrable Hamiltonians:

$$|\psi_{RG}\rangle = \prod_{\alpha=1}^{N}\left(\sum_{i=1}^{L}\frac{S_i^+}{\epsilon_i - v_\alpha}\right)|\downarrow\cdots\downarrow\rangle$$

The variational parameters are the inhomogeneity parameters $\{\epsilon_i\}$ and the rapidities $\{v_\alpha\}$ (or equivalently, the eigenvalues $\{\Lambda_i\}$). The energy functional $E[\psi] = \langle\psi_{RG}|H|\psi_{RG}\rangle/\langle\psi_{RG}|\psi_{RG}\rangle$ is minimized via gradient descent.

Key findings:
- For perturbations that do not change qualitative physics, the variational RG state accurately approximates the true ground state even beyond perturbative regimes
- When perturbations cause level crossings, variationally optimizing an excited RG state can capture the new ground state
- The method provides a guaranteed improvement over first-order perturbation theory
- Applied to the central spin model with integrability-breaking perturbations, the variational method gives excellent overlap with exact ground states for moderate perturbation strength

**Chapter 8: Floquet Dynamics from Integrability**

Periodically driving an integrable system breaks its integrability (since $[H(t_1), H(t_2)] \neq 0$ generically). However, integrability techniques can still be leveraged:

- The Floquet operator $U_F = \exp(-i(1-\delta)H_2 T)\exp(-iH_1 \delta T)$ connects states within the integrable Hilbert space
- Many-body resonances occur when the driving frequency matches energy differences between integrable eigenstates
- At resonance, the system transitions between ground and highest excited states of the time-averaged Hamiltonian
- For the central spin model with periodic magnetic field, resonances can decouple the central spin from its environment, achieving maximal polarization

---

## Key Results

1. The eigenvalue-based method eliminates singularities in Richardson equations, enabling reliable numerical solutions for all coupling strengths
2. Determinant expressions for inner products and form factors allow polynomial-cost computation of observables
3. Topological invariants (Pfaffian sign) survive coupling to a bath in the $p_x + ip_y$ model
4. RG Bethe states are effective variational ansatz for non-integrable systems close to RG integrability
5. The variational method is guaranteed to improve on first-order perturbation theory
6. Periodic driving creates many-body resonances that can selectively transfer population between integrable eigenstates
7. The Dicke model is the contraction limit of RG models (sending one spin to infinity)
8. Level crossings in non-integrable spectra can be captured by variationally optimizing excited RG states

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Conserved charges | $Q_i = S_i^z + g\sum_{j\neq i}[\frac{X_{ij}}{2}(S_i^+S_j^- + S_i^-S_j^+) + Y_{ij}S_i^zS_j^z]$ | Eq. (2.16) |
| Rational model | $X_{ij} = Y_{ij} = \frac{1}{\epsilon_i - \epsilon_j}$ | Sec. 2.4 |
| Bethe ansatz state | $\lvert\psi_{RG}\rangle = \prod_{\alpha=1}^{N}\left(\sum_{i=1}^{L}\frac{S_i^+}{\epsilon_i - v_\alpha}\right)\lvert\downarrow\cdots\downarrow\rangle$ | Eq. (2.56/7.2) |
| Richardson equations | $\frac{1}{g} + \sum_{j=1}^{L}\frac{s_j}{\epsilon_j - v_\alpha} - \sum_{\beta\neq\alpha}\frac{1}{v_\alpha - v_\beta} = 0$ | Eq. (2.59) |
| Eigenvalue equations | $\Lambda_i^2 + (1-2s_i)\Lambda_i + g^2\sum_{j\neq i}\frac{s_i(2s_j+1)\Lambda_i - s_j(2s_i+1)\Lambda_j}{\epsilon_i - \epsilon_j} + \cdots = 0$ | Eq. (3.14) |
| BCS Hamiltonian | $H_{BCS} = \sum_i \epsilon_i\hat{n}_i + g\sum_{ij}S_i^+S_j^-$ | Eq. (2.72) |
| Central spin model | $H_{CSM} = B_zS_0^z + \sum_{i=1}^{L-1}A_i(\mathbf{S}_0\cdot\mathbf{S}_i)$ | Sec. 2.7.1 |
| $p_x+ip_y$ Hamiltonian | $H = \sum_i\epsilon_i\hat{n}_i + g\sum_{ij}\sqrt{\epsilon_i\epsilon_j}\,S_i^+S_j^-$ | Eq. (2.80) |
| Variational energy | $E[\psi] = \langle\psi_{RG}\lvert H\rvert\psi_{RG}\rangle / \langle\psi_{RG}\lvert\psi_{RG}\rangle$ | Eq. (7.1) |
| Floquet operator | $U_F = e^{-i(1-\delta)H_2 T}\,e^{-iH_1\delta T}$ | Sec. 8.1 |

---

## Relevance to Phonon-Exflation

This thesis is directly relevant to the framework's use of Richardson-Gaudin models on SU(3). The eigenvalue-based method (Chapter 3) is the numerical technique underlying the BCS computations in Sessions 33-38 — it avoids the singularity problems that plagued earlier attempts to solve Richardson equations on the SU(3) Dirac spectrum. Chapter 7 on broken integrability is critical for the framework's open question: the Jensen breaking $[iK_7, D_K] = 0$ selects a $U(1)_7$ subsector, but physical perturbations (inner fluctuations) break integrability at the 5.2% level (Session 35). Claeys' variational method provides the tool to assess how much of the integrable BCS physics survives this breaking — directly relevant to the GGE permanence prediction. Chapter 6 on topological phase transitions in the $p_x + ip_y$ model parallels the framework's BDI classification (Session 17c), and the survival of topological invariants under bath coupling is encouraging for the framework's claim that $\text{sgn}(\text{Pf}) = -1$ persists at all $\tau$.
