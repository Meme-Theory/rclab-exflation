# Exactly solvable Richardson-Gaudin models for many-body quantum systems

**Author(s):** J. Dukelsky, S. Pittel, G. Sierra
**Year:** 2004
**Journal:** Reviews of Modern Physics 76, 643 (2004)
**arXiv:** nucl-th/0405011
**Relevance:** CRITICAL — backbone of Sessions 33-38 BCS on SU(3)

---

## Abstract

The use of exactly-solvable Richardson-Gaudin (R-G) models to describe the physics of systems with strong pair correlations is reviewed. We begin with a brief discussion of Richardson's early work, which demonstrated the exact solvability of the pure pairing model, and then show how that work has evolved recently into a much richer class of exactly-solvable models. We then show how the Richardson solution leads naturally to an exact analogy between such quantum models and classical electrostatic problems in two dimensions. This is then used to demonstrate formally how BCS theory emerges as the large-N limit of the pure pairing Hamiltonian and is followed by several applications to problems of relevance to condensed matter physics, nuclear physics and the physics of confined systems. Some of the interesting effects that are discussed in the context of these exactly-solvable models include: (1) the crossover from superconductivity to a fluctuation-dominated regime in small metallic grains, (2) the role of the nucleon Pauli principle in suppressing the effects of high spin bosons in interacting boson models of nuclei, and (3) the possibility of fragmentation in confined boson systems. Interesting insight is also provided into the origin of the superconducting phase transition both in two-dimensional electronic systems and in atomic nuclei, based on the electrostatic image of the corresponding exactly-solvable quantum pairing models.

---

## Key Arguments and Derivations

### I. Richardson's Exact Solution of the Pairing Model (Section II.A)

The pairing Hamiltonian is written in terms of pair creation/annihilation operators and number operators satisfying SU(2) algebra. The pure pairing model (PM) is:

$$H_P = \sum_l \varepsilon_l \hat{n}_l + \frac{g}{2} \sum_{ll'} A_l^\dagger A_{l'}$$

where $A_l^\dagger$ creates a pair in time-reversed states of level $l$ with degeneracy $\Omega_l$, and $g$ is the pairing strength. Richardson showed that exact unnormalized eigenstates have the product form $|\Psi\rangle = B_1^\dagger B_2^\dagger \cdots B_M^\dagger |\nu\rangle$ where collective pair operators are $B_\alpha^\dagger = \sum_l \frac{1}{2\varepsilon_l - E_\alpha} A_l^\dagger$.

The $M$ pair energies $E_\alpha$ satisfy the Richardson equations — a set of $M$ coupled nonlinear equations. The energy eigenvalue is $E = \sum_l \varepsilon_l \nu_l + \sum_\alpha E_\alpha$. This reduces the exponentially hard diagonalization problem to solving nonlinear equations, enabling exact solutions for systems as large as $L=1000$, $M=500$ ($2.7 \times 10^{299}$ dimensional Hilbert space).

### II. The Gaudin Magnet (Section II.B)

Gaudin proposed a family of integrable spin models based on SU(2) spin operators. The integrability condition requires $L$ commuting Hermitian operators (quantum invariants). Three families of solutions emerge:

- **Rational model**: $X_{ij} = Y_{ij} = 1/(\eta_i - \eta_j)$ — gives XXX spin models
- **Trigonometric model**: $X_{ij} = 1/\sin(\eta_i - \eta_j)$, $Y_{ij} = \cot(\eta_i - \eta_j)$ — gives XXZ models
- **Hyperbolic model**: $X_{ij} = 1/\sinh(\eta_i - \eta_j)$, $Y_{ij} = \coth(\eta_i - \eta_j)$ — gives XXZ models

### III. Integrability of the Pairing Model (Section II.C)

Cambiaggio, Rivas and Saraceno (CRS) established the missing link between Richardson and Gaudin models by introducing pseudo-spin representation and finding the complete set of commuting operators (quantum invariants):

$$R_l = K_l^0 + 2g \sum_{l'(\neq l)} \frac{1}{\varepsilon_l - \varepsilon_{l'}} \left[\frac{1}{2}(K_l^+ K_{l'}^- + K_l^- K_{l'}^+) + K_l^0 K_{l'}^0\right]$$

The PM Hamiltonian is a linear combination: $H_P = 2\sum_l \varepsilon_l R_l + C$. These are the rational Gaudin invariants plus a one-body (linear) term.

### IV. Generalized Richardson-Gaudin Models (Section II.D)

Extension proceeds along two lines: (1) all three families (rational, trigonometric, hyperbolic), and (2) both fermion (SU(2)) and boson (SU(1,1)) systems. The generalized quantum invariants are:

$$R_l = K_l^0 + 2g \sum_{l'(\neq l)} \left[\frac{X_{ll'}}{2}(K_l^+ K_{l'}^- + K_l^- K_{l'}^+) \mp Y_{ll'} K_l^0 K_{l'}^0\right]$$

where upper sign is for bosons, lower for fermions. The generalized Richardson equations for the rational model are:

$$1 \pm 4g \sum_j \frac{d_j}{2\eta_j - E_\alpha} \mp 4g \sum_{\beta(\neq\alpha)} \frac{1}{E_\alpha - E_\beta} = 0$$

with $d_l = \nu_l/2 \pm \Omega_l/4$.

### V. Electrostatic Mapping (Section III)

Richardson and Gaudin established an exact mapping between the quantum pairing problem and a 2D classical electrostatic system. The Richardson equations coincide with equilibrium conditions for free "pairon" charges (positions $z_\alpha = E_\alpha$, charges $q_\alpha = 1$) in the presence of fixed "orbiton" charges (positions $z_i = 2\eta_i$, charges $q_i = d_i$) and an external electric field of strength $e = \pm 1/(4g)$. Solving Richardson equations is equivalent to finding stationary pairon positions in the electrostatic problem.

### VI. The Large-N Limit (Section IV)

Using the electrostatic analogy in the continuum limit, the Richardson equations yield the BCS gap equation, the equation for chemical potential, and the BCS ground-state energy. This formally demonstrates that BCS theory is the exact large-$N$ limit of the pairing model.

### VII. Elementary Excitations (Section V)

Elementary excitations are classified by the number $N_G$ of pair energies that remain finite in the $g \to \infty$ limit. These "trapped" pair energies satisfy a Gaudin equation and exhibit a dispersion relation similar to Bogoliubov quasiparticles. They are called "gaudinos." The degeneracies in the superconducting limit are $d_{L,M,N_G} = C_L^{N_G} - C_L^{N_G - 1}$.

### VIII. Applications (Section VI)

**Ultrasmall superconducting grains**: The exact solution reveals a completely smooth crossover from superconducting to fluctuation-dominated regimes, in contrast to the abrupt BCS transition. For Aluminum grains ($g = 0.224$), exact results show pairing correlations never vanish, no matter how large $d/\tilde{\Delta}$.

**2D lattice pairing**: The electrostatic mapping reveals the superconducting phase transition as a delocalization transition from isolated "artificial atoms" to a collective "cluster" of pairons.

**Interacting Boson Model**: A repulsive boson pairing interaction can only correlate the two lowest boson degrees of freedom ($s$ and $d$), providing insight into why the IBM1 works with just $s$- and $d$-bosons.

**Confined bosons**: A new fragmented condensate phase is found at critical repulsive pairing strength $x_c = 1$, where the $l=0$ condensate splits into macroscopic occupation of both $l=0$ and $l=1$ levels.

---

## Key Results

1. The pairing model is exactly solvable via Richardson's ansatz of collective pair operators, reducing Hilbert space diagonalization to $M$ coupled nonlinear equations
2. Three families of integrable R-G models (rational, trigonometric, hyperbolic) exist for both fermion (SU(2)) and boson (SU(1,1)) systems
3. The CRS quantum invariants establish the precise connection between Richardson and Gaudin models; the PM Hamiltonian is a linear combination of these invariants
4. An exact 2D electrostatic analogy maps pair energies to pairon positions and single-particle energies to orbiton positions
5. BCS theory emerges rigorously as the large-$N$ limit via the electrostatic mapping
6. The superconducting phase transition in finite systems is a completely smooth crossover, not an abrupt transition
7. Elementary excitations (gaudinos) satisfy Gaudin equations in the strong-coupling limit
8. Generalized R-G models have $2L+1$ free parameters, providing enormous flexibility for modeling diverse physical systems
9. Fragmentation in confined boson systems occurs at a critical repulsive pairing strength

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| PM Hamiltonian | $H_P = \sum_l \varepsilon_l \hat{n}_l + \frac{g}{2} \sum_{ll'} A_l^\dagger A_{l'}$ | Eq. (4) |
| Pair algebra | $[A_l, A_{l'}^\dagger] = 2\delta_{ll'}(\Omega_l - 2\hat{n}_l)$ | Eq. (2) |
| Richardson ansatz | $\lvert\Psi\rangle = B_1^\dagger \cdots B_M^\dagger \lvert\nu\rangle$, $B_\alpha^\dagger = \sum_l \frac{1}{2\varepsilon_l - E_\alpha} A_l^\dagger$ | Eqs. (7-8) |
| Richardson equations | $1 - 4g\sum_l \frac{d_l}{2\varepsilon_l - E_\alpha} + 4g\sum_{\beta \neq \alpha} \frac{1}{E_\alpha - E_\beta} = 0$ | Eq. (9) |
| Energy eigenvalue | $E = \sum_l \varepsilon_l \nu_l + \sum_\alpha E_\alpha$ | Eq. (10) |
| Pseudo-spin algebra | $[K_l^0, K_{l'}^\pm] = \pm\delta_{ll'} K_l^\pm$, $[K_l^+, K_{l'}^-] = 2\delta_{ll'} K_l^0$ | Eq. (22) |
| CRS quantum invariants | $R_l = K_l^0 + 2g\sum_{l'\neq l} \frac{1}{\varepsilon_l - \varepsilon_{l'}} [\frac{1}{2}(K_l^+ K_{l'}^- + K_l^- K_{l'}^+) + K_l^0 K_{l'}^0]$ | Eq. (24) |
| PM as linear combo | $H_P = 2\sum_l \varepsilon_l R_l + C$ | Eq. (25) |
| Generalized R eqs (rational) | $1 \pm 4g\sum_j \frac{d_j}{2\eta_j - E_\alpha} \mp 4g\sum_{\beta\neq\alpha} \frac{1}{E_\alpha - E_\beta} = 0$ | Eq. (34) |
| BCS gap equation | $\int_\Omega \frac{\rho(\varepsilon)\,d\varepsilon}{\sqrt{(\varepsilon/2 - \lambda)^2 + \Delta^2}} = \frac{1}{G}$ | Eq. (51) |
| Chemical potential | $M = \int_\Omega \left(1 - \frac{\varepsilon/2 - \lambda}{\sqrt{(\varepsilon/2-\lambda)^2 + \Delta^2}}\right) \rho(\varepsilon)\,d\varepsilon$ | Eq. (52) |
| BCS ground-state energy | $E = -\frac{\Delta^2}{G} + \int_\Omega \left(1 - \frac{\varepsilon/2-\lambda}{\sqrt{(\varepsilon/2-\lambda)^2+\Delta^2}}\right) \rho(\varepsilon)\varepsilon\,d\varepsilon$ | Eq. (53) |
| Gaudin eq (strong coupling) | $\sum_{j=1}^L \frac{1}{\varepsilon_j - E_\nu^f} - \sum_{\mu=1(\neq\nu)}^{N_G} \frac{2}{E_\mu^f - E_\nu^f} = 0$ | Eq. (54) |
| Excitation degeneracies | $d_{L,M,N_G} = C_L^{N_G} - C_L^{N_G-1}$ | Eq. (56) |
| Condensation energy | $E_b^C = E_b^{GS} - \langle FS \lvert H_{BCS} \rvert FS\rangle$ | Eq. (57) |
| Matveev-Larkin gap | $\Delta_{ML} = E_1(N) - \frac{1}{2}(E_0(N+1) + E_0(N-1))$ | Eq. (58) |
| Renormalized boson Hamiltonian | $H = C + \sum_l \bar{\varepsilon}_l n_l + \sum_{l\neq l'} V_{ll'}[A_l^\dagger A_{l'} - n_l n_{l'}]$ | Eq. (61) |
| Occupation numbers | $\langle\hat{n}_l\rangle = \sum_p \frac{\partial E_p}{\partial \varepsilon_l}$ | Eq. (60) |

---

## Relevance to Phonon-Exflation

This paper is the primary reference for the Richardson-Gaudin framework used throughout Sessions 33-38 of the phonon-exflation project. The BCS pairing on SU(3) computed in the project uses Richardson's exact solution: the pair energies $E_\alpha$ satisfying Eq. (9) are the foundation of the BCS instability theorem (RG-BCS-35) showing any $g > 0$ flows to strong coupling. The electrostatic mapping provides the geometric picture underlying the instanton gas interpretation (S37-S38). The CRS quantum invariants $R_l$ are the 8 conserved integrals protecting the GGE relic post-transit (S38: integrability-protected permanence). The gaudino excitations at strong coupling connect directly to the quasiparticle spectrum computed in Sessions 34-35, and the smooth crossover from SC to fluctuation-dominated regimes is the finite-size physics controlling the framework's 0D limit ($L/\xi_{GL} = 0.031$).
