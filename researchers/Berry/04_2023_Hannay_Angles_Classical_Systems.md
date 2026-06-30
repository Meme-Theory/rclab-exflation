# Adiabatic driving and geometric phases in classical systems

**Author(s):** A. D. Bermudez Manjarres
**Year:** 2023
**Journal:** [not stated in PDF; preprint]
**arXiv:** 2305.14511
**Relevance:** MEDIUM

---

## Abstract

We study the concepts of adiabatic driving and geometric phases of classical integrable systems under the Koopman-von Neumann formalism. In close relation to what happens to a quantum state, a classical Koopman-von Neumann eigenstate will acquire a geometric phase factor exp{i*Phi} after a closed variation of the parameters lambda in its associated Hamiltonian. The explicit form of Phi is then derived for integrable systems, and its relation with the Hannay angles is shown. Additionally, we use quantum formulas to write a classical adiabatic gauge potential that generates adiabatic unitary flow between classical eigenstates, and we explicitly show the relationship between the potential and the classical geometric phase.

---

## Key Arguments and Derivations

### Koopman-von Neumann (KvN) Formalism

The paper reformulates classical mechanics in the same Hilbert space language as quantum mechanics. Starting from Liouville's equation for probability density rho in phase space, KvN wavefunctions are defined by psi*psi = rho. These wavefunctions satisfy a Schrodinger-like equation i partial_t psi = L_hat psi, where the Liouvillian L_hat = -i{., H(p,q)} plays the role of the Hamiltonian operator. The Hilbert space H_c consists of all square-integrable functions on phase space with inner product <phi, psi> = integral phi* psi d^n q d^n p.

### Integrable Systems: Action-Angle Variables

For integrable Hamiltonians H = H(I) in action-angle variables (phi, I), the Liouvillian simplifies to L_hat = -i omega partial/partial_phi where omega = partial H/partial I. The eigenfunctions are psi_n = (1/sqrt(2pi)) delta(I - I') e^{in phi} with eigenvalues l_n = n omega. The spectrum is uncountably degenerate (continuous in I). To handle this, the author discretizes I using eigendifferentials f(I)_k localized on individual Liouville-Arnold tori.

### Geometric Phases via Wilczek-Zee Formula

For parameter-dependent Hamiltonians H(I(lambda), lambda), the Wilczek-Zee non-Abelian potential is computed for the KvN eigenfunctions. The key computation shows:

A^(n)_{kk'} = -n delta_{kk'} <d_lambda phi(lambda)>

where <.> denotes the torus average. The potential is diagonal -- each wavefunction remains on the same torus, consistent with the classical adiabatic theorem. After a complete circuit in parameter space:

psi_n(lambda(t)) = e^{in Phi} psi_n(lambda(t_0))

where Phi = -Delta phi_{Hannay} = -oint_C <d_lambda phi>. The geometric phase factor acquired by KvN waves is proportional to the Hannay angle.

### Adiabatic Gauge Potential

Using quantum formulas, the author defines a classical adiabatic gauge potential A_hat that generates unitary flow between KvN eigenstates. The components satisfy A_hat = -i{., W(I, theta, lambda)} where the generating function W = (1/omega) integral d phi (<d_lambda H> - d_lambda H) corresponds to the first-order generating function in Lie-Deprit perturbation theory of Hamiltonian mechanics.

The Yang-Mills curvature F_hat of the adiabatic gauge potential encodes the geometric phase. The curvature's diagonal matrix elements yield the Hannay curvature, as verified for the generalized oscillator example.

### Example: Generalized Oscillator

For H = (1/2)(Xq^2 + 2Yqp + Zp^2) with frequency omega = sqrt(XZ - Y^2), the generating functions W_X, W_Y, W_Z are computed explicitly. The Poisson brackets {W_Y, W_X} = -ZI/(4 omega^3) etc. yield the curvature 2-form:

<psi_n, F_hat psi_n> = n/(4 omega^3) (X dY wedge dZ + Y dZ wedge dX + Z dX wedge dY)

This matches the known Hannay curvature of the system.

## Key Results

1. Classical KvN eigenstates acquire a geometric phase factor exp(in*Phi) after a closed adiabatic parameter variation, where Phi equals the negative Hannay angle.
2. The Wilczek-Zee potential for KvN states is diagonal, reflecting that each wavefunction stays on its torus (classical adiabatic theorem).
3. The classical adiabatic gauge potential A_hat = -i{., W} maps to the Lie-Deprit generating function of Hamiltonian perturbation theory.
4. The Yang-Mills curvature of the adiabatic potential reproduces the Hannay curvature.
5. The formalism unifies quantum Berry phases and classical Hannay angles in a single Hilbert space framework.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Liouville equation | $\frac{\partial\rho}{\partial t} = -\{\rho, H(p,q)\}$ | Eq. (1) |
| KvN Schrodinger equation | $i\frac{\partial\psi}{\partial t} = \hat{L}\psi$ | Eq. (3) |
| Liouvillian | $\hat{L} = -i\{\cdot, H(p,q)\}$ | Eq. (4) |
| Liouvillian (integrable) | $\hat{L} = -i\omega\frac{\partial}{\partial\phi}$ | Eq. (8) |
| KvN eigenfunctions | $\psi_n = \frac{1}{\sqrt{2\pi}}\delta(I-I')e^{in\phi}$ | Eq. (11) |
| KvN eigenvalues | $l_n = n\omega$ | Eq. (12) |
| Wilczek-Zee potential (KvN) | $A^{(n)}_{kk'}(\lambda) = -n\delta_{kk'}\langle d_\lambda\phi(\lambda)\rangle$ | Eq. (23) |
| Classical geometric phase | $\Phi = -\Delta\phi_{\text{Hannay}} = -\oint_C\langle d_\lambda\phi\rangle$ | Eq. (25) |
| Adiabatic gauge potential | $\hat{\mathcal{A}}(\lambda) = -i\{\cdot, W(I,\theta,\lambda)\}$ | Eq. (33) |
| Generating function | $W(I,\theta,\lambda) = \frac{1}{\omega}\int d\phi\;(\langle d_\lambda H\rangle - d_\lambda H)$ | Eq. (37) |
| Yang-Mills curvature | $\hat{F}_{\mu\nu}(\lambda) = \partial_\mu\hat{\mathcal{A}}_\nu - \partial_\nu\hat{\mathcal{A}}_\mu - i[\hat{\mathcal{A}}_\mu, \hat{\mathcal{A}}_\nu]$ | Eq. (40) |
| Hannay curvature (oscillator) | $\langle\psi_n, \hat{F}\psi_n\rangle = \frac{n}{4\omega^3}(XdY\wedge dZ + YdZ\wedge dX + ZdX\wedge dY)$ | Eq. (48) |

## Relevance to Phonon-Exflation

This paper provides the bridge between quantum geometric phases (Berry) and classical geometric phases (Hannay) through the Koopman-von Neumann formalism. For the phonon-exflation framework, where transit physics operates in a regime that is neither fully quantum nor fully classical (the phononic excitations are collective, semiclassical modes on the M4 x SU(3) substrate), the KvN unification is directly relevant. The adiabatic gauge potential A_hat = -i{., W} generating classical transit between eigenstates mirrors the gauge connection on the KK fiber, and the explicit link between the Yang-Mills curvature and the Hannay curvature validates computing spectral action corrections using classical phase-space methods. The Lie-Deprit perturbation theory connection provides a practical computational tool for perturbative corrections to the transit generating function.
