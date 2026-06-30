# Geometric magnetism in open quantum systems

**Author(s):** Michele Campisi, Sergey Denisov, Peter Hanggi
**Year:** 2012
**Journal:** [not stated in PDF; preprint]
**arXiv:** 1206.0671
**Relevance:** HIGH

---

## Abstract

An isolated classical chaotic system, when driven by the slow change of several parameters, responds with two reaction forces: geometric friction and geometric magnetism. By using the theory of quantum fluctuation relations we show that this holds true also for open quantum systems, and provide explicit expressions for those forces in this case. This extends the concept of Berry curvature to the realm of open quantum systems. We illustrate our findings by calculating the geometric magnetism of a damped charged quantum harmonic oscillator transported along a path in physical space in presence of a magnetic field and a thermal environment. We find that in this case the geometric magnetism is unaffected by the presence of the heat bath.

---

## Key Arguments and Derivations

### Background: Berry Phase in Isolated vs. Open Systems

The paper begins by reviewing Berry's 1984 result for isolated systems and the classical analogue: Hannay's angle (1985) for integrable systems, extended by Robbins and Berry (1992) to chaotic classical systems. Berry and Robbins (1993) showed that a slowly-driven classical chaotic system experiences two reaction forces from slow parameter change: geometric friction (from the symmetric part of the conductance matrix) and geometric magnetism (from the antisymmetric part, i.e., the Berry curvature two-form).

The key gap: no prior work extended this statistical mechanical approach to open quantum systems coupled to a thermal bath. This paper fills that gap using quantum work fluctuation relations.

### Canonical Adiabatic Linear Response Theory

The system+bath total Hamiltonian is H(R_t) = H_B + H_SB + H(R_t), where the system Hamiltonian is H(R_t) = H_0 - R_t . Q with time-dependent parameters R_t and conjugate force observables Q. Starting from the Gibbs equilibrium at t=0, the authors derive a nonequilibrium identity (Eq. 7) using the inclusive viewpoint of fluctuation relations, which generalizes the quantum Jarzynski equality.

Expanding to first order in the dissipated work W_dis (valid for slow/quasi-adiabatic driving), they obtain the adiabatic linear response formula relating the deviation of an observable from equilibrium to integrated equilibrium correlation functions (relaxation functions).

### Geometric Friction and Geometric Magnetism

Setting the observable O to the force Q^i, the response becomes <Delta Q_tau> = -K(R_tau) . R_dot_tau, where K is the N x N conductance matrix of integrated force-force correlation functions. Decomposing K into symmetric and antisymmetric parts:

- **Geometric friction**: from K^S, the symmetric part
- **Geometric magnetism**: from K^A, the antisymmetric part, giving a Lorentz-like force B(R) x R_dot

The field of geometric magnetism for open quantum systems is the central result (Eq. 21):
B(R) = (1/2) integral_0^infty dt integral_0^beta du <nabla H_{-ihbar u} x nabla H_t>^eq_R

This generalizes the Berry-Robbins expression (Eq. 1) for isolated classical chaotic systems.

### Application: Damped Charged Harmonic Oscillator

For a quantum harmonic oscillator of charge q in a magnetic field B coupled to a Caldeira-Leggett bath, the generalized Langevin equation is derived. Using the antisymmetric relaxation function and its Laplace transform, the geometric magnetism is computed exactly: B = qB, regardless of bath spectral density. The thermal environment does not alter the geometric magnetism in this linear case.

### Comparison with Kubo Theory

The paper clarifies the distinction between this Canonical Adiabatic Linear Response (linear in R_dot, response relative to instantaneous equilibrium) and Kubo's Linear Response Theory (linear in R, response relative to initial equilibrium). Both follow from exact fluctuation relations but from complementary "inclusive" vs. "exclusive" viewpoints.

## Key Results

1. Geometric magnetism extends to open quantum systems, even with strong system-bath coupling.
2. The geometric magnetism field B(R) is given by Eq. (21), a Kubo-type formula involving equilibrium correlation functions of the Hamiltonian gradient.
3. For a charged harmonic oscillator in a magnetic field + thermal bath, B = qB -- the geometric magnetism equals the physical magnetic field, unaffected by the bath.
4. The Berry phase of an open quantum system is defined as gamma = integral of B . dSigma (surface integral of geometric magnetism).
5. Geometric magnetism vanishes when time-reversal invariance holds (via Onsager-Casimir relations).
6. No assumption of chaotic dynamics is needed for the driven system; the bath provides the necessary relaxation.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Classical Berry curvature (chaotic) | $\mathcal{B}^c = \frac{1}{2\omega(E)}\frac{\partial}{\partial E}\left[\omega(E)\int_0^\infty dt\langle\nabla H_{t=0}\times\nabla H_t\rangle_E\right]$ | Eq. (1) |
| Total Hamiltonian | $\mathcal{H}(\mathbf{R}_t) = H_B + H_{SB} + H(\mathbf{R}_t)$ | Eq. (2) |
| System Hamiltonian | $H(\mathbf{R}_t) = H_0 - \mathbf{R}_t \cdot \mathbf{Q}$ | Eq. (3) |
| Nonequilibrium identity | $\langle O_\tau e^{-\beta\mathcal{H}_\tau(\mathbf{R}_\tau)}e^{\beta\mathcal{H}(\mathbf{R}_0)}\rangle^{\rm eq}_{\mathbf{R}_0} = e^{-\beta\Delta F}\langle O\rangle^{\rm eq}_{\mathbf{R}_\tau}$ | Eq. (7) |
| Adiabatic linear response | $\langle\Delta O_\tau\rangle = -\sum_i \int_0^\tau dt\,\Phi^{\mathbf{R}_\tau}_{i,O}(t-\tau)\dot{R}^i_\tau$ | Eq. (14) |
| Relaxation function | $\Phi^{\mathbf{R}_\tau}_{i,O}(t) = \int_0^\beta du\,\langle\Delta O_{-i\hbar u}\Delta Q^i_t\rangle^{\rm eq}_{\mathbf{R}_\tau}$ | Eq. (15) |
| Force response (matrix form) | $\langle\Delta\mathbf{Q}_\tau\rangle = -\mathbf{K}^S(\mathbf{R}_\tau)\dot{\mathbf{R}}_\tau - \mathcal{B}(\mathbf{R}_\tau)\times\dot{\mathbf{R}}_\tau$ | Eq. (19) |
| Geometric magnetism (open QS) | $\mathcal{B}(\mathbf{R}) = \frac{1}{2}\int_0^\infty dt\int_0^\beta du\,\langle\nabla H_{-i\hbar u}\times\nabla H_t\rangle^{\rm eq}_{\mathbf{R}}$ | Eq. (21) |
| Symmetrized correlation function | $\Psi^{\mathbf{R}}_{jk}(t) = \frac{1}{2}\langle\{\partial_k H,\,\partial_j H_t\}\rangle^{\rm eq}_{\mathbf{R}}$ | Eq. (22) |
| Classical geometric magnetism | $\mathcal{B}^{\rm cl}(\mathbf{R}) = \frac{\beta}{2}\int_0^\infty dt\,\langle\nabla H\times\nabla H_t\rangle^{\rm eq}_{\mathbf{R}}$ | Eq. (29) |
| Geometric magnetism via reduced density matrix | $\mathcal{B}_i(\mathbf{R}_\tau) = \frac{1}{2}\sum_{jk}\varepsilon_{ijk}\left[\mathrm{Tr}_S\rho^{S,j}_\tau Q_k - \langle Q_k\rangle^{\rm eq,S}_{\mathbf{R}_\tau}\right]/V_j$ | Eq. (34) |
| Damped oscillator result | $\mathcal{B} = qB$ | Eq. (40) |
| Berry phase (open system) | $\gamma = \int\mathcal{B}\cdot d\mathbf{\Sigma}$ | Eq. (43) |

## Relevance to Phonon-Exflation

This paper is directly relevant to the spectral action formulation on the M4 x SU(3) fiber. The phonon-exflation framework operates in a non-equilibrium, open-system regime where the internal fiber degrees of freedom couple to the expanding M4 "bath." The geometric magnetism formalism provides the precise mathematical tool for computing Berry curvature corrections to the spectral action when the compactification parameter tau evolves slowly -- the Canonical Adiabatic Linear Response is the natural framework for transit physics. The key result that geometric magnetism survives coupling to a thermal bath (B = qB for harmonic oscillators) suggests that topological invariants of the fiber connection may be robust against thermal decoherence during transit, supporting the Ordered Veil hypothesis.
