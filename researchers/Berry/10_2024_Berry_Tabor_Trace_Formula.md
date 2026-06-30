# Periodic orbit theory of Bethe-integrable quantum systems: an N-particle Berry-Tabor trace formula

**Author(s):** Juan Diego Urbina, Michael Kelly, and Klaus Richter
**Year:** 2024
**Journal:** [not stated in PDF]
**arXiv:** 2401.17891
**Relevance:** HIGH

---

## Abstract

One of the fundamental results of semiclassical theory is the existence of trace formulae showing how spectra of quantum mechanical systems emerge from massive interference among amplitudes related with time-periodic structures of the corresponding classical limit. If it displays the properties of Hamiltonian integrability, this connection is given by the celebrated Berry-Tabor trace formula, and the periodic structures it is built on are KAM tori supporting closed trajectories in phase space. Here we show how to extend this connection into the domain of quantum many-body systems displaying integrability in the sense of the Bethe ansatz, where a classical limit cannot be rigorously defined due to the presence of singular potentials. Formally following the original derivation of Berry and Tabor [1, 2], but applied to the Bethe equations without underlying classical structure, we obtain a many-particle trace formula for the density of states of N interacting bosons on a ring, the Lieb-Liniger model. Our semiclassical expressions are in excellent agreement with quantum mechanical results for N = 2, 3 and 4 particles. For N = 2 we relate our results to the quantization of billiards with mixed boundary conditions. Our work paves the way towards the treatment of the important class of integrable many-body systems by means of semiclassical trace formulae pioneered by Michael Berry in the single-particle context.

---

## Key Arguments and Derivations

### Section I: Introduction

The density of states of a quantum system decomposes into a smooth part (Thomas-Fermi / Weyl term) and an oscillatory part expressible as a sum over classical periodic orbits. For chaotic systems, the Gutzwiller trace formula provides this decomposition. For integrable systems with a well-defined classical limit, the Berry-Tabor trace formula (1976, 1977) achieves the same via Poisson summation of the EBK (Einstein-Brillouin-Keller) quantization conditions, followed by stationary phase evaluation. The resulting trace formula sums over winding numbers of periodic orbits on KAM tori.

The key question addressed is whether the Berry-Tabor approach can be extended to quantum integrable systems (Bethe-ansatz solvable) that lack a classical limit due to singular contact potentials. The authors show this is possible for the Lieb-Liniger model.

### Section II: The Lieb-Liniger Model

The Lieb-Liniger model describes N bosons on a ring of length L = 2*pi with contact interaction of strength g > 0. The Bethe ansatz gives eigenenergies E = sum k_j^2 where rapidities k_j satisfy the coupled Bethe equations. The Bethe quantum numbers I_j (half-integers or integers depending on N) label the many-body eigenstates, with the fermionic exclusion property that all I_j must be distinct.

### Section III: Many-Body Berry-Tabor Trace Formula

The density of states is written as an ordered sum over Bethe quantum numbers. The ordering constraint is overcome by a combinatorial identity involving integer partitions of N, with coefficients C_a that include inclusion-exclusion corrections for coinciding quantum numbers. For N=2: sum_{I_1<I_2} -> (1/2!)(sum_{I_1,I_2} - sum_{I_1=I_2}). Each partition term has an effective dimension d(a) with modified Bethe equations where multiplicity factors a_i track degenerate quantum numbers.

After this decomposition, Poisson summation is applied to each unordered sum term. The M=0 terms give the smooth Weyl contribution; the M != 0 terms give the oscillatory part. Switching from Bethe quantum numbers to rapidities introduces Jacobians related to the normalization of Bethe states. The oscillatory integrals are evaluated by stationary phase approximation, yielding the periodic orbit condition M parallel to dE/dI (winding numbers characterize topological families of periodic orbits).

The final many-body trace formula expresses the oscillatory density of states as a sum of cosine terms with semiclassical amplitudes A_M and actions R_M involving scaled free-particle actions S_M, scattering phases Phi_M, and the Bethe Jacobians.

### Section IV: Results and Connections

Comparison with exact quantum mechanical solutions for N = 2, 3, 4 particles at strong coupling (g = 10, 100) shows excellent agreement. The phenomenon of "resurgence" (Berry, 1989) is demonstrated for N = 2: the oscillatory contribution progressively cancels the smooth Weyl background, forming delta-peak structure. For N = 2, the LL model maps to a 2D square billiard with periodic boundary conditions and a mixed (Robin) boundary condition along x = y, equivalent to a delta-function potential V(x,y) = g*delta(x-y) with kappa = g/2.

## Key Results

1. **N-particle Berry-Tabor trace formula** for the Lieb-Liniger model (Eqs. 25-28), extending the single-particle Berry-Tabor approach to Bethe-integrable many-body systems
2. **Combinatorial identity** (Eqs. 11-12) for converting ordered sums over fermionic Bethe quantum numbers to unordered sums amenable to Poisson summation
3. **Smooth density of states** (Eq. 20) expressed via Jacobian of the Bethe equations, equivalent to thermodynamic Bethe ansatz
4. **Semiclassical resurgence** demonstrated in the few-body spectrum, where oscillatory periodic orbit contributions cancel the smooth Weyl background
5. **Billiard correspondence**: N=2 Lieb-Liniger maps to a 2D billiard with mixed boundary conditions (Robin type)
6. **Excellent agreement** with exact quantum results for N = 2, 3, 4 particles at strong coupling

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Density of states | $\rho(E) = \sum_n \delta(E - E_n) = \bar{\rho}(E) + \tilde{\rho}(E)$ | Eqs. (1)-(2) |
| Thomas-Fermi (smooth) | $\bar{\rho}(E) = \frac{1}{(2\pi\hbar)^f}\int dp\,dq\,\delta(E - H(p,q))$ | Eq. (3) |
| EBK quantization | $\mathbf{J}(\mathbf{c}) = \hbar\left(\mathbf{m} + \frac{\boldsymbol{\alpha}}{4}\right)$ | Eq. (4) |
| Action variable | $J_i = \frac{1}{2\pi}\oint_{\gamma_i(\mathbf{c})} \mathbf{p}\cdot d\mathbf{q}$ | Eq. (5) |
| LL Hamiltonian | $\hat{\mathcal{H}} = -\sum_{j=1}^N \partial_{x_j}^2 + 2g\sum_{k<j}\delta(x_j - x_k)$ | Eq. (6) |
| LL eigenenergies | $E(\vec{k}) = \sum_{j=1}^N k_j^2$ | Eq. (7) |
| Bethe equations | $2\pi I_j = Lk_j + 2\sum_{i=1}^N \arctan\left(\frac{k_j - k_i}{g}\right)$ | Eq. (8) |
| Partition coefficients | $C_{\vec{a}} = \prod_{m=1}^N \frac{(-1)^{d(\vec{a})-N}}{m^{s_m} s_m!}$ | Eq. (12) |
| Decomposed density | $\rho(E) = \sum_{\vec{a}\in\Pi(N)} C_{\vec{a}}\rho_{\vec{a}}(E)$ | Eq. (18) |
| Smooth part (Weyl) | $\bar{\rho}(E) = \sum_{\vec{a}} C_{\vec{a}}\int d^{d(\vec{a})}k\,\left\lvert\frac{\partial\vec{I}}{\partial\vec{k}}\right\rvert\delta(E - E(\vec{k}))$ | Eq. (20) |
| Oscillatory part | $\tilde{\rho}_{\vec{a}}(E) = \sum'_{M_1,\ldots,M_d} A_{\vec{M}}(E,\vec{a})\cos(R_{\vec{M}}(E,\vec{a}))$ | Eq. (25) |
| Actions | $R_{\vec{M}}(E,\vec{a}) = 2\sqrt{S_{\vec{M}}E} - \frac{\pi}{4}(d(\vec{a})-1) + \vec{M}\cdot\vec{\Phi}_{\vec{M}} + \pi\delta\lvert M\rvert$ | Eq. (27) |
| Scattering phases | $(\vec{\Phi}_{\vec{M}})_i = 2\sum_{j=1}^d a_j\arctan\left(\frac{(\vec{k}_{\vec{M}})_i - (\vec{k}_{\vec{M}})_j}{g}\right)$ | Eq. (28) |
| Robin boundary condition | $\partial_q\psi^+_n\big\rvert_{q=0} = \kappa\psi^+_n(X,X)$ | Eq. (31) |

## Relevance to Phonon-Exflation

This paper is directly relevant because the phonon-exflation BCS Fock space is integrable (the Ordered Veil, established in S36-38). The Berry-Tabor trace formula provides the spectral density decomposition for integrable systems, predicting Poisson-class level statistics. The extension to Bethe-integrable many-body systems without a classical limit is particularly significant: the M4 x SU(3) fiber phonon modes are quantum excitations that may likewise lack a strict classical limit but still admit Bethe-ansatz-type solutions. The resurgence phenomenon (oscillatory terms cancelling the smooth Weyl background) connects to our heat kernel computations (s61_heat_kernel_a2.py) and spectral action framework where the smooth term encodes the macroscopic geometry while oscillatory corrections carry the particle physics content.
