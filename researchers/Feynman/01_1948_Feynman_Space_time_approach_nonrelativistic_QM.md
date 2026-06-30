# Space-Time Approach to Non-Relativistic Quantum Mechanics

**Author(s):** R. P. Feynman (Cornell University, Ithaca, New York)
**Year:** 1948
**Journal:** Reviews of Modern Physics, Volume 20, Number 2, April 1948, pp. 367-387
**arXiv/DOI:** N/A (pre-arXiv); RMP reference
**Relevance:** CRITICAL

---

## Abstract

Non-relativistic quantum mechanics is formulated here in a different way. It is, however, mathematically equivalent to the familiar formulation. In quantum mechanics the probability of an event which can happen in several different ways is the absolute square of a sum of complex contributions, one from each alternative way. The probability that a particle will be found to have a path x(t) lying somewhere within a region of space time is the square of a sum of contributions, one from each path in the region. The contribution from a single path is postulated to be an exponential whose (imaginary) phase is the classical action (in units of hbar) for the path in question. The total contribution from all paths reaching x, t from the past is the wave function psi(x, t). This is shown to satisfy Schroedinger's equation. The relation to matrix and operator algebra is discussed. Applications are indicated, in particular to eliminate the coordinates of the field oscillators from the equations of quantum electrodynamics.

---

## Key Arguments and Derivations

**Section 1 — Introduction.** Feynman notes that modern QM grew from two formulations (Schrödinger's differential equation; Heisenberg's matrix algebra), proved equivalent and later unified by Dirac's transformation theory. He proposes a third formulation suggested by Dirac's remarks on the relation of classical action to quantum mechanics: a probability amplitude is associated with an entire *motion of a particle as a function of time*, rather than with a particle position at a given time. He motivates this by (i) new perspective on old results, (ii) problems for which a new viewpoint has advantage — in particular eliminating coordinates of interacting system B from the equations of A, by analogy with eliminating longitudinal and transverse field oscillators in QED.

**Section 2 — Superposition of probability amplitudes.** For three successive measurements A, B, C giving results a, b, c, the classical probability identity P_{abc} = P_{ab} P_{bc} and P_{ac} = sum_b P_{abc} holds in classical physics but fails in quantum mechanics. The quantum-mechanical replacement introduces complex amplitudes phi with P = |phi|^2 and phi_{ac} = sum_b phi_{ab} phi_{bc}. If B is not measured, the sum of amplitudes (not of probabilities) is taken — giving interference. If B is measured, classical addition of probabilities returns. Measurement necessarily disturbs the phase.

**Section 3 — Probability amplitude for a space-time path.** Feynman generalizes this to a particle sampled at times t_i = t_{i-1} + epsilon in 1D. A region R in space-time has probability amplitude phi(R) = lim_{epsilon to 0} int_R Phi(...x_i, x_{i+1}...) dx_i dx_{i+1}... Postulate I: *If an ideal measurement is performed to determine whether a particle has a path lying in a region of space-time, then the probability that the result will be affirmative is the absolute square of a sum of complex contributions, one from each path in the region.*

**Section 4 — Calculation of the probability amplitude.** Postulate II: *The paths contribute equally in magnitude, but the phase of their contribution is the classical action (in units of hbar); i.e., the time integral of the classical Lagrangian taken along the path.* Thus each path's contribution is proportional to exp((i/hbar) S[x(t)]) where S = int L dt. For small epsilon the action splits S = sum_i S(x_{i+1}, x_i). Combining with postulate I:

phi(R) = lim_{epsilon to 0} int_R exp((i/hbar) sum_i S(x_{i+1}, x_i)) prod_i dx_i / A,

with normalization 1/A per factor.

**Section 5 — Definition of the wave function.** Splitting R into past-region R' (before t) and future-region R'' (after t), the exponential factorizes and the integrals yield phi(R',R'') = int chi*(x,t) psi(x,t) dx. Here psi(x_k,t) depends only on the past region R', and chi* depends only on the future region R''. psi plays the role of wave function.

**Section 6 — The wave equation.** From the recursion psi(x_{k+1}, t+epsilon) = int exp((i/hbar) S(x_{k+1}, x_k)) psi(x_k, t) dx_k / A, for Lagrangian L = (m/2) xdot^2 - V(x), Taylor-expanding psi(x - xi, t) to second order in xi, doing Gaussian integrals, and requiring zero-order agreement, Feynman fixes A = (2 pi hbar i epsilon / m)^{1/2} and derives to first order in epsilon the Schrödinger equation:

-(hbar/i) d psi/dt = (1/2m) (hbar/i del)^2 psi + V(x) psi.

Thus the path integral IS equivalent to standard QM. The "paths" that dominate are continuous but nowhere differentiable (Brownian-like), with (x_{k+1} - x_k)/epsilon of order (hbar/(m epsilon))^{1/2} — diverging as epsilon → 0.

**Section 7 — Classical limit.** The formulation is Huygens' principle for matter waves: action replaces time. For hbar → 0 the phase sum exp(iS/hbar) oscillates rapidly except near stationary points, so the classical orbit satisfies dS/dx_i = 0, recovering Hamilton's principle and Lagrangian equations of motion.

**Sections 8-10 — Matrix elements, Newton's law, Hamiltonian.** Transition elements  are defined between two states psi (at t') and chi (at t''). Integration by parts in x_k yields the equivalence relation -(hbar/i) dF/dx_k <-> F dS/dx_k, which for simple choices reproduces [p,x] = hbar/i, Newton's equation m xddot = -V'(x) in matrix form, and identifies the kinetic-energy functional with (1/2)m((x_{k+1}-x_k)/epsilon)((x_k-x_{k-1})/epsilon). The Hamiltonian is defined through infinitesimal time translations: H_k = dS(x_{k+1}, t_{k+1}; x_k, t_k)/dt_k + hbar/(2i(t_{k+1}-t_k)). The momentum functional arises from spatial displacements.

**Section 11 — Inadequacies.** The subdivision of time is unnatural (could be improved by functional calculus). No direct procedure handles non-position measurements (momentum etc.) from within the formulation; invariance under canonical transformations is not manifest.

**Section 12 — Generalization.** The formulation admits actions that are NOT integrals of functions of position and velocity: actions involving acceleration, or non-instantaneous interactions S = int x(t) x(t+T) dt, for which no wave function exists but transition probabilities still do. This anticipates Wheeler-Feynman absorber theory and QED.

**Section 13 — Application: eliminating field oscillators.** A particle coordinate x(t) interacting with an oscillator q(t) (Lagrangian L_osc = (1/2)(qdot^2 - omega^2 q^2)) via a coupling gamma(x,t) q(t) gives, after Gaussian integration over oscillator q_i coordinates, an effective action for the particle alone times an oscillator-transition factor G_{mn}. The oscillator contribution reduces to classical forced-oscillator action Q(q_j, q_0). Applied to QED this eliminates the field oscillators — both longitudinal (giving instantaneous Coulomb) and, in principle, transverse — and yields a non-local action functional for charges alone, generalizing Wheeler-Feynman to quantum theory.

**Section 14 — Statistical mechanics, spin, relativity.** The density matrix generalizes directly. Spin and relativity can be added formally (Pauli equation from spin-1/2 path sum; Klein-Gordon from relativistic action m c^2 int dtau).

## Key Results

1. A third formulation of quantum mechanics: the wave function is a sum over all space-time paths weighted by exp(iS/hbar).
2. Postulate I (sum rule) + Postulate II (action as phase) are equivalent to Schrödinger's equation for quadratic Lagrangians.
3. The dominant paths are continuous, nowhere differentiable, Brownian-like; the classical path emerges as the stationary-phase limit when hbar → 0.
4. Matrix element relations <chi | dF/dx_k | psi> = -(i/hbar) <chi | F dS/dx_k | psi> give the commutation relation [p,x] = hbar/i and Newton's equation in matrix form.
5. Harmonic oscillators coupled linearly to a system can be integrated out exactly, producing a non-local effective action — the path-integral tool for eliminating QED field oscillators.
6. Generalization to non-Lagrangian actions (Wheeler-Feynman-type) is possible: transition amplitudes exist even when no wave function does.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Quantum composition | $\varphi_{ac} = \sum_b \varphi_{ab}\,\varphi_{bc}$ | Eq. (5) |
| Probability amplitude | $P = |\varphi|^2$ | Eq. (3) |
| Path amplitude postulate | $\Phi[x(t)] \propto \exp\!\left(\frac{i}{\hbar} S[x(t)]\right),\ \ S = \int L(\dot x, x)\,dt$ | Postulate II, §4 |
| Discretized path integral | $\varphi(R) = \lim_{\epsilon \to 0} \int_R \exp\!\left[\tfrac{i}{\hbar}\sum_i S(x_{i+1}, x_i)\right]\frac{dx_{i+1}}{A}\frac{dx_i}{A}\cdots$ | Eq. (12) |
| Normalization | $A = (2\pi \hbar i\,\epsilon/m)^{1/2}$ | Eq. (28) |
| Wave-function recursion | $\psi(x_{k+1}, t+\epsilon) = \int \exp\!\left[\tfrac{i}{\hbar}S(x_{k+1},x_k)\right]\psi(x_k,t)\,dx_k/A$ | Eq. (18) |
| Short-time action | $S(x_{i+1},x_i) = \tfrac{m\epsilon}{2}\!\left(\frac{x_{i+1}-x_i}{\epsilon}\right)^{\!2} - \epsilon V(x_{i+1})$ | Eq. (22) |
| Schrödinger equation | $-\frac{\hbar}{i}\frac{\partial\psi}{\partial t} = \frac{1}{2m}\!\left(\frac{\hbar}{i}\nabla\right)^{\!2}\!\psi + V(x)\psi$ | Eq. (30) |
| Bra-ket/transition factorization | $\varphi(R',R'') = \int \chi^*(x,t)\,\psi(x,t)\,dx$ | Eq. (14) |
| Transition element | $\langle\chi_{t''}|F|\psi_{t'}\rangle_S = \lim \int \chi^*(x'',t'')F(x_0,\ldots)\exp(iS/\hbar)\psi(x',t')\prod dx_i/A$ | Eq. (39) |
| Equivalence of functionals | $-\tfrac{\hbar}{i}\frac{\partial F}{\partial x_k} \leftrightarrow_S F\,\frac{\partial S}{\partial x_k}$ | Eq. (46) |
| Commutator from EOM | $(x_{k+1}-x_k)^2/\epsilon^2 \leftrightarrow_S \hbar/(im\epsilon)$, giving $[p,x]=\hbar/i$ | Eq. (50) |
| Newton's law (matrix form) | $m\!\left(\frac{x_{k+1}-x_k}{\epsilon}-\frac{x_k-x_{k-1}}{\epsilon}\right)/\epsilon \leftrightarrow_S -V'(x_k)$ | Eq. (48) |
| Oscillator elimination | $G_{mn}=(2\pi i\hbar \sin\omega T/\omega)^{-1/2}\iint \varphi_m^*(q_j)\exp(iQ(q_j,q_0)/\hbar)\varphi_n(q_0)\,dq_j dq_0$ | §13 |
| Forced-oscillator action | $Q(q_j,q_0)=\frac{\omega}{2\sin\omega T}[(\cos\omega T)(q_j^2+q_0^2)-2q_j q_0] + \text{driving terms}$ | §13 |

## Relevance to Phonon-Exflation

This paper is the foundational document for the framework's computational backbone. The phonon-exflation project represents the substrate by a spectral triple whose Dirac operator D_K defines the eigenmode content, and treats emergent cosmological dynamics (fold transit, Parker pair production, GGE relic formation) as sums over histories of the fabric. The GPE simulation computes the classical saddle point of a specific path integral — exactly the stationary-phase limit of Feynman's construction (§7). Integration-out of the field oscillators (§13) is the exact technique needed to eliminate the SU(3) fiber oscillators and derive the effective action on the emergent M4. Quantum corrections to the GPE (Bogoliubov theory) are fluctuations around the stationary path described here. Every Lagrangian Feynman-Theorist writes for this project inherits the path-integral semantics of Eqs. (12) and (18).
