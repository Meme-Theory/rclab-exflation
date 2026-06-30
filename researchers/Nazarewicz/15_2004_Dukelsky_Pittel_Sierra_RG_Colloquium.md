# Exactly Solvable Richardson-Gaudin Models for Many-Body Quantum Systems

**Author(s):** J. Dukelsky, S. Pittel, G. Sierra
**Year:** 2004
**Journal:** Reviews of Modern Physics (Colloquium)
**arXiv:** nucl-th/0405011
**Relevance:** CRITICAL

---

## Abstract

The use of exactly-solvable Richardson-Gaudin (R-G) models to describe the physics of systems with strong pair correlations is reviewed. We begin with a brief discussion of Richardson's early work, which demonstrated the exact solvability of the pure pairing model, and then show how that work has evolved recently into a much richer class of exactly-solvable models. We then show how the Richardson solution leads naturally to an exact analogy between such quantum models and classical electrostatic problems in two dimensions. This is then used to demonstrate formally how BCS theory emerges as the large-N limit of the pure pairing Hamiltonian and is followed by several applications to problems of relevance to condensed matter physics, nuclear physics and the physics of confined systems. Some of the interesting effects that are discussed in the context of these exactly-solvable models include: (1) the crossover from superconductivity to a fluctuation-dominated regime in small metallic grains, (2) the role of the nucleon Pauli principle in suppressing the effects of high spin bosons in interacting boson models of nuclei, and (3) the possibility of fragmentation in confined boson systems. Interesting insight is also provided into the origin of the superconducting phase transition both in two-dimensional electronic systems and in atomic nuclei, based on the electrostatic image of the corresponding exactly-solvable quantum pairing models.

---

## Key Arguments and Derivations

### Richardson's Exact Solution of the Pairing Model (Sec. II.A)

The pairing model (PM) Hamiltonian is:
$$H_P = \sum_l \varepsilon_l \hat{n}_l + \frac{g}{2} \sum_{ll'} A^\dagger_l A_{l'}$$
where $A^\dagger_l = \sum_m a^\dagger_{lm} a^\dagger_{l\bar{m}}$ creates a pair of fermions in time-reversed states, and $g$ is the pairing strength. Richardson showed the exact unnormalized eigenstates can be written as $|\Psi\rangle = B^\dagger_1 B^\dagger_2 \cdots B^\dagger_M |\nu\rangle$, where the collective pair operators are $B^\dagger_\alpha = \sum_l \frac{1}{2\varepsilon_l - E_\alpha} A^\dagger_l$. The $M$ pair energies $E_\alpha$ satisfy the Richardson equations:
$$1 - 4g \sum_l \frac{d_l}{2\varepsilon_l - E_\alpha} + 4g \sum_{\beta(\neq\alpha)} \frac{1}{E_\alpha - E_\beta} = 0$$
where $d_l = \nu_l/2 - \Omega_l/4$ is the effective pair degeneracy. The energy eigenvalue is $E = \sum_l \varepsilon_l \nu_l + \sum_\alpha E_\alpha$. This method can solve systems with $L = 1000$, $M = 500$ (dimension $2.7 \times 10^{299}$), far beyond any diagonalization.

### The Gaudin Magnet (Sec. II.B)

Gaudin proposed integrable spin models based on SU(2), with quantum invariants $H_i = \sum_{j(\neq i)} \sum_\alpha w^\alpha_{ij} K^\alpha_i K^\alpha_j$. Three families of solutions exist: rational ($X_{ij} = Y_{ij} = 1/(\eta_i - \eta_j)$), trigonometric ($X_{ij} = 1/\sin(\eta_i - \eta_j)$, $Y_{ij} = \cot(\eta_i - \eta_j)$), and hyperbolic (sinh/coth forms). Each yields an integrable spin chain with long-range interactions.

### Integrability of the Pairing Model (Sec. II.C)

Cambiaggio, Rivas and Saraceno (CRS) established the connection by introducing pseudo-spin operators $K^0_l, K^\pm_l$ satisfying SU(2) commutation relations. They found the complete set of commuting operators:
$$R_l = K^0_l + 2g \sum_{l'(\neq l)} \frac{1}{\varepsilon_l - \varepsilon_{l'}} \left[\frac{1}{2}(K^+_l K^-_{l'} + K^-_l K^+_{l'}) + K^0_l K^0_{l'}\right]$$
The PM Hamiltonian is a linear combination: $H_P = 2\sum_l \varepsilon_l R_l + C$.

### Generalized Richardson-Gaudin Models (Sec. II.D)

The generalization includes both fermion (SU(2)) and boson (SU(1,1)) systems. The most general quantum invariants are:
$$R_l = K^0_l + 2g \sum_{l'(\neq l)} \left[\frac{X_{ll'}}{2}(K^+_l K^-_{l'} + K^-_l K^+_{l'}) \mp Y_{ll'} K^0_l K^0_{l'}\right]$$
All three families (rational, trigonometric, hyperbolic) are exactly solvable via the ansatz $|\Psi\rangle = \prod_\alpha B^\dagger_\alpha |\nu\rangle$ with $B^\dagger_\alpha = \sum_i u_i(E_\alpha) K^+_i$. For the rational model, $u_i(E_\alpha) = 1/(2\eta_i - E_\alpha)$ and the generalized Richardson equations are:
$$1 \pm 4g \sum_j \frac{d_j}{2\eta_j - E_\alpha} \mp 4g \sum_{\beta(\neq\alpha)} \frac{1}{E_\alpha - E_\beta} = 0$$

### Electrostatic Mapping (Sec. III)

The Richardson equations are exactly equivalent to the equilibrium conditions for free charges (pairons) in a 2D electrostatic problem with fixed charges (orbitons), an external electric field $e = \pm 1/(4g)$, pairon positions $z_\alpha = E_\alpha$, orbiton positions $z_i = 2\eta_i$, orbiton charges $q_i = d_i$, and pairon charges $q_\alpha = 1$. This maps the quantum pairing problem onto a classical problem amenable to geometrical interpretation.

### Large-N Limit (Sec. IV)

Using the electrostatic analogy in the continuum limit ($L \to \infty$, $G = g/L$ fixed), the Richardson equations convert to integral equations whose solutions yield precisely the BCS gap equation:
$$\int_\Omega \frac{\rho(\varepsilon)\,d\varepsilon}{\sqrt{(\varepsilon/2 - \lambda)^2 + \Delta^2}} = \frac{1}{G}$$
the chemical potential equation, and the BCS ground-state energy. For finite $N$, the pair energies organize into an arc in the complex plane with endpoints $2\lambda \pm 2i\Delta$, directly visualizing the BCS gap.

### Elementary Excitations (Sec. V)

Excitations are characterized by the number $N_G$ of pair energies that remain finite in the $g \to \infty$ limit. These "trapped" pair energies satisfy the Gaudin equation. A clear phase transition from normal to superconducting is visible in the excitation spectrum. The degeneracies are $d_{L,M,N_G} = C^L_{N_G} - C^L_{N_G-1}$. The elementary excitations are called "gaudinos."

### Applications (Sec. VI)

**Ultrasmall superconducting grains**: The exact solution shows a completely smooth superconducting/fluctuation-dominated (SC/FD) transition, unlike BCS which predicts an abrupt crossover. Even-odd parity effects are reproduced: odd grains with a blocked level show reduced pairing. The Matveev-Larkin parameter $\Delta_{ML}$ exhibits a minimum as a function of $d/\tilde{\Delta}$, confirmed by DMRG calculations.

**2D lattice pairing**: The electrostatic analogy provides a pictorial representation of the normal-to-superconducting transition as a delocalization from isolated "artificial atoms" around orbitons to a collective "cluster" of pairons.

**Interacting Boson Model (IBM)**: A second-order quantum phase transition from U(5) vibrational to O(6) gamma-unstable symmetry is visualized as the balance between Coulomb repulsion and external electric field. Repulsive boson pairing can only correlate two boson degrees of freedom (s and d), explaining the success of IBM1.

**Confined bosons**: For bosons in a harmonic trap, the pure PM scatters pairs to high-energy states unphysically. By choosing $\eta_l = (\varepsilon_l)^3$, a physically meaningful exactly-solvable Hamiltonian is obtained. With repulsive pairing, a fragmented condensate with two macroscopically occupied states appears at a critical interaction strength.

---

## Key Results

1. Richardson's exact solution reduces the pairing model to solving $M$ coupled nonlinear equations for pair energies, tractable for systems of dimension $\sim 10^{299}$
2. The pairing model is integrable with $L$ commuting quantum invariants (CRS operators), expressible as a linear combination of Gaudin-type integrals of motion
3. Three families of generalized R-G models exist (rational, trigonometric, hyperbolic), all exactly solvable for both fermion and boson systems
4. An exact mapping exists between the quantum pairing problem and a 2D classical electrostatic system of fixed orbitons and free pairons
5. BCS theory emerges rigorously as the large-$N$ limit of the Richardson solution via the electrostatic analogy
6. The SC/FD crossover in ultrasmall grains is completely smooth in the exact solution, with pairing correlations never vanishing regardless of how large $d/\tilde{\Delta}$ becomes
7. Randomness in level spacings enhances pairing correlations, particularly in the fluctuation-dominated regime
8. The IBM phase transition from U(5) to O(6) is directly visualized in the electrostatic mapping
9. Repulsive boson pairing in IBM naturally selects only $s$ and $d$ bosons as the correlated degrees of freedom
10. Confined bosons with repulsive pairing can form a fragmented condensate — the first known example for scalar bosons

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Pairing Hamiltonian | $H_P = \sum_l \varepsilon_l \hat{n}_l + \frac{g}{2} \sum_{ll'} A^\dagger_l A_{l'}$ | Eq. 4 |
| Richardson ansatz | $\lvert\Psi\rangle = \prod_{\alpha=1}^M B^\dagger_\alpha \lvert\nu\rangle$, $B^\dagger_\alpha = \sum_l \frac{1}{2\varepsilon_l - E_\alpha} A^\dagger_l$ | Eqs. 7-8 |
| Richardson equations | $1 - 4g \sum_l \frac{d_l}{2\varepsilon_l - E_\alpha} + 4g \sum_{\beta \neq \alpha} \frac{1}{E_\alpha - E_\beta} = 0$ | Eq. 9 |
| Energy eigenvalue | $E = \sum_l \varepsilon_l \nu_l + \sum_\alpha E_\alpha$ | Eq. 10 |
| CRS quantum invariants | $R_l = K^0_l + 2g \sum_{l'(\neq l)} \frac{1}{\varepsilon_l - \varepsilon_{l'}} [\frac{1}{2}(K^+_l K^-_{l'} + K^-_l K^+_{l'}) + K^0_l K^0_{l'}]$ | Eq. 24 |
| PM as linear combination | $H_P = 2\sum_l \varepsilon_l R_l + C$ | Eq. 25 |
| Generalized RG invariants | $R_l = K^0_l + 2g \sum_{l'(\neq l)} [\frac{X_{ll'}}{2}(K^+_l K^-_{l'} + K^-_l K^+_{l'}) \mp Y_{ll'} K^0_l K^0_{l'}]$ | Eq. 29 |
| Rational model amplitudes | $u_i(E_\alpha) = 1/(2\eta_i - E_\alpha)$ | Eq. 33 |
| Electrostatic equilibrium | $e + \sum_j \frac{q_j}{z_j - z_\alpha} - \sum_{\beta(\neq\alpha)} \frac{q_\beta}{z_\alpha - z_\beta} = 0$ | Eq. 43 |
| BCS gap equation (large-N) | $\int_\Omega \frac{\rho(\varepsilon)\,d\varepsilon}{\sqrt{(\varepsilon/2 - \lambda)^2 + \Delta^2}} = \frac{1}{G}$ | Eq. 51 |
| BCS ground-state energy | $E = -\Delta^2/G + \int_\Omega [1 - \frac{\varepsilon/2 - \lambda}{\sqrt{(\varepsilon/2-\lambda)^2+\Delta^2}}] \rho(\varepsilon)\varepsilon\,d\varepsilon$ | Eq. 53 |
| Gaudin equation (excitations) | $\sum_{j=1}^L \frac{1}{\varepsilon_j - E^f_\nu} - \sum_{\mu=1(\neq\nu)}^{N_G} \frac{2}{E^f_\mu - E^f_\nu} = 0$ | Eq. 54 |
| Excitation degeneracies | $d_{L,M,N_G} = C^L_{N_G} - C^L_{N_G-1}$ | Eq. 56 |
| Condensation energy | $E^C_b = E^{GS}_b - \langle FS \lvert H_{BCS} \rvert FS\rangle$ | Eq. 57 |
| Matveev-Larkin parameter | $\Delta_{ML} = E_1(N) - \frac{1}{2}(E_0(N+1) + E_0(N-1))$ | Eq. 58 |
| Occupation numbers | $\langle \hat{n}_l \rangle = \sum_p \partial E_p / \partial \varepsilon_l$ | Eq. 60 |
| Modified Hamiltonian | $H = C + \sum_l \bar{\varepsilon}_l n_l + \sum_{l\neq l'} V_{ll'} [A^\dagger_l A_{l'} - n_l n_{l'}]$ with $\eta_l = (\varepsilon_l)^3$ | Eqs. 61-62 |

## Relevance to Phonon-Exflation

This paper is the foundational reference for Richardson-Gaudin integrability, which is the mathematical backbone of the framework's BCS sector on SU(3). The framework operates at $L/\xi_{GL} = 0.031$ (ultrasmall 0D limit, Sec. VI.A), has 8 conserved Richardson-Gaudin integrals that protect the post-transit GGE from thermalization, and produces a giant pair vibration with 85.5% strength concentration (the "pairing vibrations" discussed in Sec. V). The electrostatic mapping (Sec. III) provides the geometric picture for pair energy arcs in the complex plane that the framework's instanton gas explores. The smooth SC/FD crossover (no abrupt phase transition) is precisely what the framework finds: the condensate destruction during transit is a continuous process governed by the Richardson integrals.
