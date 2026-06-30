# Exactly solvable Richardson-Gaudin models for many-body quantum systems

**Author(s):** J. Dukelsky, S. Pittel, G. Sierra
**Year:** 2004
**Journal:** Rev. Mod. Phys. (Colloquium)
**arXiv/DOI:** arXiv:nucl-th/0405011
**Relevance:** CRITICAL

---

## Abstract

The use of exactly-solvable Richardson-Gaudin (R-G) models to describe the physics of systems with strong pair correlations is reviewed. We begin with a brief discussion of Richardson's early work, which demonstrated the exact solvability of the pure pairing model, and then show how that work has evolved recently into a much richer class of exactly-solvable models. We then show how the Richardson solution leads naturally to an exact analogy between such quantum models and classical electrostatic problems in two dimensions. This is then used to demonstrate formally how BCS theory emerges as the large-N limit of the pure pairing Hamiltonian and is followed by several applications to problems of relevance to condensed matter physics, nuclear physics and the physics of confined systems. Some of the interesting effects that are discussed in the context of these exactly-solvable models include: (1) the crossover from superconductivity to a fluctuation-dominated regime in small metallic grains, (2) the role of the nucleon Pauli principle in suppressing the effects of high spin bosons in interacting boson models of nuclei, and (3) the possibility of fragmentation in confined boson systems. Interesting insight is also provided into the origin of the superconducting phase transition both in two-dimensional electronic systems and in atomic nuclei, based on the electrostatic image of the corresponding exactly-solvable quantum pairing models.

---

## Key Arguments and Derivations

**I. Introduction.** Exactly-solvable models have shaped understanding of strongly correlated quantum systems. In 1D: Bethe-ansatz family (Heisenberg model onward), Tomonaga-Luttinger bosonization family, and Calogero-Sutherland long-range family. In nuclear physics, dynamical-symmetry models like Elliott SU(3) and the three IBM limits. Superconductivity is common to both nuclear and condensed-matter systems; BCS approximation breaks down for $N \sim 100$ particles, motivating exact pairing solutions.

**II.A. Richardson's exact solution.** Pair operators $\hat{n}_l$, $A^\dagger_l = \sum_m a^\dagger_{lm}a^\dagger_{l\bar{m}}$ (Eq. 1) close SU(2) (Eq. 2). The pairing model Hamiltonian $H_P = \sum_l \epsilon_l\hat{n}_l + (g/2)\sum_{ll'}A^\dagger_l A_{l'}$ (Eq. 4).

Richardson's ansatz: $M$-pair unnormalized eigenstate $|\Psi\rangle = B^\dagger_1\cdots B^\dagger_M|\nu\rangle$ (Eq. 7) with collective pair operators $B^\dagger_\alpha = \sum_l (2\epsilon_l - E_\alpha)^{-1}A^\dagger_l$ (Eq. 8).

**Richardson equations:** $1 - 4g\sum_l d_l/(2\epsilon_l - E_\alpha) + 4g\sum_{\beta(\ne\alpha)}1/(E_\alpha - E_\beta) = 0$ (Eq. 9), where $d_l = \nu_l/2 - \Omega_l/4$. Energy: $E = \sum_l \epsilon_l\nu_l + \sum_\alpha E_\alpha$ (Eq. 10).

**II.B. Gaudin magnet.** Integrable spin model based on SU(2) with L independent commuting Hermitian operators $H_i = \sum_{j\ne i}\sum_\alpha w^\alpha_{ij}K^\alpha_i K^\alpha_j$ (Eq. 12). Integrability condition Eq. 13 reduces (with antisymmetry and $w^\alpha_{ij} = f_\alpha(\eta_i-\eta_j)$) to three solution families:
- Rational: $X_{ij} = Y_{ij} = 1/(\eta_i - \eta_j)$ (Eq. 17)
- Trigonometric: $X_{ij} = 1/\sin(\eta_i-\eta_j)$, $Y_{ij} = \cot(\eta_i-\eta_j)$ (Eq. 18)
- Hyperbolic: $X_{ij} = 1/\sinh(\eta_i-\eta_j)$, $Y_{ij} = \coth(\eta_i-\eta_j)$ (Eq. 19)

**II.C. Integrability of pairing model (Cambiaggio-Rivas-Saraceno).** Pseudo-spin operators $K^0_l$, $K^\pm_l$ (Eq. 21) close SU(2) (Eq. 22). The set $R_l = K^0_l + 2g\sum_{l'\ne l}(\epsilon_l - \epsilon_{l'})^{-1}[(K^+_l K^-_{l'} + K^-_l K^+_{l'})/2 + K^0_l K^0_{l'}]$ (Eq. 24) is Hermitian, global, independent, and mutually commuting. Pairing Hamiltonian: $H_P = 2\sum_l \epsilon_l R_l + C$ (Eq. 25). This equals Gaudin's rational model plus a linear term.

**II.D. Generalized Richardson-Gaudin models.** For both fermions (SU(2)) and bosons (SU(1,1)) with compact algebra Eq. 28, the general quantum invariants Eq. 29 satisfy Gaudin equations (Eq. 16) with solution families parametrized by $\gamma$:
$X_{ij} = \gamma/\sin[\gamma(\eta_i - \eta_j)]$, $Y_{ij} = \gamma\cot[\gamma(\eta_i - \eta_j)]$ (Eq. 30); $\gamma = 0$ rational, $\gamma = 1$ trigonometric, $\gamma = i$ hyperbolic.

Eigenstates $|\Psi\rangle = \prod_{\alpha=1}^M B^\dagger_\alpha|\nu\rangle$, $B^\dagger_\alpha = \sum_i u_i(E_\alpha)K^+_i$ (Eq. 32).

- Rational: $u_i(E_\alpha) = 1/(2\eta_i - E_\alpha)$ (Eq. 33), Richardson equations Eq. 34, eigenvalues Eq. 35.
- Trig/hyperbolic: $u_i(E_\alpha) = 1/\text{sn}(E_\alpha - 2\eta_i)$ (Eq. 36), equations Eq. 37, eigenvalues Eq. 38.

For boson/fermion unification: $d_l = \nu_l/2 \pm \Omega_l/4$ (Eq. 39, upper sign bosons).

**III. Electrostatic mapping.** Richardson equations = equilibrium equations for 2D classical charges. Orbiton positions $z_i = 2\eta_i$, charges $q_i = d_i$; pairon positions $z_\alpha = E_\alpha$, charges $q_\alpha = 1$; electric field $e = \pm 1/(4g)$ (Table I). Solving Richardson equations = finding 2D electrostatic equilibrium.

**IV. Large-N limit.** Electrostatic analogy used by Richardson and Gaudin to show thermodynamic limit reproduces BCS solution.

**V–VI. Elementary excitations and applications.** Applications to ultrasmall superconducting grains, 2D lattice pairing, interacting boson models, confined boson systems.

## Key Results

1. Exact solvability of the general pairing Hamiltonian via Richardson's Bethe-ansatz-like construction.
2. Unified framework for three families (rational, trigonometric, hyperbolic) of R-G integrable models.
3. Integrability proof: L commuting quantum invariants $R_l$ for the pairing model (Cambiaggio-Rivas-Saraceno).
4. Exact mapping between quantum pairing models and 2D classical electrostatics.
5. Extension to bosonic systems (SU(1,1) algebra).
6. BCS theory emerges as large-N limit of exact solution.
7. Applications: ultrasmall superconducting grains (superconductor-to-fluctuation crossover), boson condensation with fragmentation, pictorial view of pairing transitions.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Pair operators | $A^\dagger_l = \sum_m a^\dagger_{lm}a^\dagger_{l\bar{m}}$ | Eq. 1 |
| SU(2) pair algebra | $[A_l, A^\dagger_{l'}] = 2\delta_{ll'}(\Omega_l - 2\hat{n}_l)$ | Eq. 2 |
| Pairing Hamiltonian | $H_P = \sum_l \epsilon_l\hat{n}_l + (g/2)\sum_{ll'}A^\dagger_l A_{l'}$ | Eq. 4 |
| Richardson eigenstate | $\|\Psi\rangle = B^\dagger_1\cdots B^\dagger_M\|\nu\rangle$ | Eq. 7 |
| Collective pair | $B^\dagger_\alpha = \sum_l (2\epsilon_l - E_\alpha)^{-1}A^\dagger_l$ | Eq. 8 |
| Richardson equations | $1 - 4g\sum_l d_l/(2\epsilon_l - E_\alpha) + 4g\sum_{\beta\ne\alpha}1/(E_\alpha - E_\beta) = 0$ | Eq. 9 |
| Energy | $E = \sum_l \epsilon_l\nu_l + \sum_\alpha E_\alpha$ | Eq. 10 |
| Gaudin integrability | $Y_{ij}X_{jk} + Y_{ki}X_{jk} + X_{ki}X_{ij} = 0$ | Eq. 16 |
| Rational family | $X_{ij} = Y_{ij} = 1/(\eta_i - \eta_j)$ | Eq. 17 |
| CRS conserved charges | $R_l = K^0_l + 2g\sum_{l'\ne l}(\epsilon_l-\epsilon_{l'})^{-1}[(K^+_l K^-_{l'} + K^-_l K^+_{l'})/2 + K^0_l K^0_{l'}]$ | Eq. 24 |
| Generalized RG charges | $R_l = K^0_l + 2g\sum_{l'\ne l}[X_{ll'}(K^+_l K^-_{l'} + K^-_l K^+_{l'})/2 \mp Y_{ll'}K^0_l K^0_{l'}]$ | Eq. 29 |
| Three families unified | $X_{ij} = \gamma/\sin[\gamma(\eta_i-\eta_j)]$, $Y_{ij} = \gamma\cot[\gamma(\eta_i-\eta_j)]$ | Eq. 30 |
| Generalized eigenstate | $\|\Psi\rangle = \prod_\alpha B^\dagger_\alpha\|\nu\rangle$, $B^\dagger_\alpha = \sum_i u_i(E_\alpha)K^+_i$ | Eq. 32 |
| Degeneracy function | $d_l = \nu_l/2 \pm \Omega_l/4$ | Eq. 39 |
| Electrostatic analogy | Orbiton $z_i = 2\eta_i$, $q_i = d_i$; pairon $z_\alpha = E_\alpha$, $q_\alpha = 1$; $e = \pm 1/(4g)$ | Table I |
| Poisson 2D | $\nabla^2 V(\mathbf{r}) = -2\pi\delta(\mathbf{r})$, logarithmic potential | Eq. 40 |
| Electrostatic extremum | $e + \sum_j q_j/(z_j - z_\alpha) - \sum_{\beta\ne\alpha}q_\beta/(z_\alpha - z_\beta) = 0$ | Eq. 43 |

## Relevance to Phonon-Exflation

Central to S38 GGE permanence in the framework. The project's $N=8$ BCS pairing on the Dirac spectrum is an explicit realization of Richardson-Gaudin integrability — Bethe ansatz eigenstates, 8 conserved charges $R_l$, pairing-model Hamiltonian with $d_l = \nu_l/2 - \Omega_l/4$. The rational family (Eq. 17) corresponds to the S34–35 mechanism chain (I-1, RPA, Turing, WALL, BCS) as standard pairing. The electrostatic mapping provides a pictorial tool for the two-dimensional "compound nucleus" picture of transit dynamics. The integrability-protected non-thermal relic (GGE permanence) follows from the L commuting conserved charges $R_l$. Directly underpins the project's claim that the post-transit Ordered Veil is integrable/non-thermal.
