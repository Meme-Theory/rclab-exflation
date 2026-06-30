# 100 Years of Weyl's Law

**Author(s):** Victor Ivrii
**Year:** 2016 (revised 2017)
**Journal:** [INCOMPLETE - not extractable from source]
**arXiv:** 1608.03963
**Relevance:** HIGH

---

## Abstract

We discuss the asymptotics of the eigenvalue counting function for partial differential operators and related expressions paying the most attention to the sharp asymptotics. We consider Weyl asymptotics, asymptotics with Weyl principal parts and correction terms and asymptotics with non-Weyl principal parts. Semiclassical microlocal analysis, propagation of singularities and related dynamics play crucial role. We start from the general theory, then consider Schrodinger and Dirac operators with the strong magnetic field and, finally, applications to the asymptotics of the ground state energy of heavy atoms and molecules with or without a magnetic field.

---

## Key Arguments and Derivations

### 1. Weyl's Original Law (1911)

Hermann Weyl proved the asymptotic formula for eigenvalues of the Dirichlet Laplacian in a bounded domain X in R^d:

N(lambda) = (2pi)^{-d} omega_d vol(X) lambda^{d/2} (1 + o(1)) as lambda -> +infinity

where N(lambda) counts eigenvalues less than lambda, omega_d is the volume of the unit ball in R^d, and vol(X) is the volume of X. Weyl's conjecture (1912) added the next correction term involving the boundary volume.

### 2. Method of the Hyperbolic Operator

The paper describes Carleman's Tauberian method and the hyperbolic operator approach as the central tool. The propagator u(x, y, t) satisfies the wave equation u_{tt} + Delta u = 0 and the connection to spectral asymptotics comes through Fourier transform and Tauberian theorems. The sharp remainder o(lambda^{(d-1)/2}) was obtained by Duistermaat-Guillemin (1975) under the assumption that the set of periodic geodesics has measure zero.

### 3. Semiclassical Microlocal Analysis

The modern formulation uses semiclassical parameter h -> 0. The semiclassical wave front set WF^s(u) and propagation of singularities (Theorem 2.1.2) are the main technical tools. The microhyperbolicity condition on the principal symbol controls propagation:

<(l P_0)(x,xi) v, v> >= epsilon |v|^2 - C |P_0(x,xi) v|^2

### 4. Successive Approximation Method

For short times |t| <= T_* = h^{1-delta}, the propagator can be constructed by successive approximation, yielding asymptotic expansions for the spectral function. The key technical result (Proposition 2.1.5) gives:

T integral of chi-bar((lambda-tau)Th^{-1}) d_tau (Q_1x e Q_2y)(y, y, tau) ~ sum_{m>=0} h^{-d+m} ...

### 5. Global Asymptotics and Non-Weyl Cases

The paper surveys Weyl asymptotics for compact manifolds without boundary:

N(lambda) = c_0 lambda^{d/m} + c_1 lambda^{(d-1)/m} + o(lambda^{(d-1)/m})

under the non-periodicity condition on Hamiltonian trajectories. Non-Weyl cases arise from operators with degenerate principal symbols (e.g., sub-Riemannian geometry) or from magnetic Schrodinger operators.

### 6. Magnetic Schrodinger and Dirac Operators

Sections 5-6 discuss spectral asymptotics for magnetic Schrodinger operators h^2 Delta + V - mu h F_{jk} where F is the magnetic field tensor, and magnetic Dirac operators. Key phenomena include Landau levels in 2D, the role of magnetic field degeneracies, and applications to ground state energy of heavy atoms.

---

## Key Results

1. **Weyl's Law**: N(lambda) = (2pi)^{-d} omega_d vol(X) lambda^{d/2} (1 + o(1)) for the Dirichlet Laplacian on bounded domains.

2. **Weyl Conjecture**: N(lambda) ~ (2pi)^{-d} omega_d vol(X) lambda^{d/2} -/+ (1/4)(2pi)^{1-d} omega_{d-1} vol'(dX) lambda^{(d-1)/2} for Dirichlet/Neumann conditions.

3. **Duistermaat-Guillemin Theorem**: The remainder is o(lambda^{(d-1)/2}) when the set of periodic geodesics has measure zero.

4. **Ivrii's Theorem (1980)**: Weyl's conjecture holds under the assumption that the set of all periodic geodesic billiards has measure zero.

5. **Sharp remainder estimates** for magnetic Schrodinger operators including the 2D case with degenerating magnetic field.

6. **Applications to multiparticle quantum theory**: Asymptotics of the ground state energy of heavy atoms and molecules.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Weyl's Law | $N(\lambda) = (2\pi)^{-d}\omega_d \mathrm{vol}(X)\lambda^{d/2}(1+o(1))$ | Eq. (1.1.1) |
| Weyl's conjecture | $N(\lambda) = (2\pi)^{-d}\omega_d \mathrm{vol}(X)\lambda^{d/2} \mp \frac{1}{4}(2\pi)^{1-d}\omega_{d-1}\mathrm{vol}'(\partial X)\lambda^{(d-1)/2}$ | Eq. (1.1.2) |
| Wave equation propagator | $u_{tt} + \Delta u = 0,\; u|_{t=0} = \delta(x-y),\; u_t|_{t=0} = 0$ | Eqs. (1.2.2)-(1.2.3) |
| Spectral projector | $u(x,y,t) = \int_0^\infty \cos(\lambda t)\, d_\lambda e(x,y,\lambda^2)$ | Eq. (1.2.1) |
| Fourier-Tauberian | $F_{t\to\tau}[\bar{\chi}_T(t) u(x,x,t)] = c_0(x)\lambda^{d-1} + c_1(x)\lambda^{d-2} + O(\lambda^{d-3})$ | Eq. (1.2.4) |
| Microhyperbolicity | $\langle(\ell P_0)(x,\xi)v,v\rangle \geq \epsilon|v|^2 - C|P_0(x,\xi)v|^2$ | Eq. (2.1.2) |
| WF propagation | $\mathrm{WF}^s(u) \subset \mathrm{WF}^s(Pu) \cup \mathrm{Char}(P)$ | Eq. (2.1.1) |
| Finite speed bound | $\mathrm{WF}(u) \cap \{|t|\leq T_*\} \subset \{|x-y|^2 + |\xi+\eta|^2 \leq (C_0 t)^2\}$ | Eq. (2.1.7) |

---

## Relevance to Phonon-Exflation

Weyl's law governs the eigenvalue asymptotics of the Dirac operator on M4 x SU(3), and the constant-ratio trap (F/B = 0.55) identified in the project is a direct manifestation of Weyl's law applied to the bosonic vs fermionic spectral sums. The Seeley-DeWitt heat coefficients a_0, a_2, a_4 appearing in the spectral action Tr(f(D/Lambda)) are precisely the objects whose asymptotics this paper characterizes. The paper's treatment of Dirac operators specifically, and the role of periodic geodesics in controlling remainder estimates, is relevant to understanding spectral action precision on compact Lie groups.
