# Backreaction inclusive Schwinger effect in flat and de Sitter spacetimes via a self-consistent Maxwell-Schrödinger semiclassical dynamics

**Author(s):** Shagun Kaushal, Suprit Singh
**Year:** 2025 (v2, Sep 2025; v1 Dec 2024)
**Journal:** arXiv preprint (hep-th)
**arXiv/DOI:** arXiv:2412.09436v2
**Relevance:** MEDIUM

---

## Abstract

We employ a self-consistent framework to study the backreaction effects of particle creation in the coupled semiclassical dynamics of a quantum complex scalar field and a classical electric field in both (1 + 1)- and (1 + 3)-dimensional Minkowski and de Sitter spacetimes. Using a general Gaussian-state formalism in the Schrödinger picture, we solve the resulting nonlinear equations with Gaussian initial data, obtaining a self-consistent semiclassical evolution that incorporates nonperturbative backreaction. We compute the time-dependent instantaneous particle content, current density, and electric field, defined through instantaneous eigenstates of the field modes. Comparing scenarios with and without backreaction, we find that backreaction strongly modifies the electric field and current, producing immediate plasma-like oscillations and driving pronounced oscillations in the instantaneous mode occupations through nonadiabatic squeezing and quantum interference. These oscillations do not imply additional irreversible particle production—the time-averaged particle number remains essentially constant—but they reveal the rich nonperturbative real-time dynamics captured by our self-consistent semiclassical approach across dimensions and in both Minkowski and de Sitter backgrounds.

---

## Key Arguments and Derivations

**Motivation.** Standard Schwinger mechanism treats electric field as fixed background, neglecting feedback from produced pair currents. This paper develops a local canonical prescription where a quantum matter field and classical electric field evolve self-consistently.

**Framework.** System split: classical variable $C$ (electric field), quantum variable $Q$ (complex scalar). Quantum sector evolves via TDSE (Eq. 1) with $C$ as c-number; classical sector evolves via Poisson bracket with effective Hamiltonian $H_{\text{eff}} = H_1(C) + \langle\psi|\hat{H}_2(Q,C)|\psi\rangle$ (Eq. 2).

**Section 2: Canonical approach without backreaction.** Hamiltonian density Eq. 3 for complex scalar $\phi(t,x)$ coupled to $A_\mu = (0, A_1(t))$. Separation $H = H_1 + H_2$ with classical $H_1 = (1/2)\int dx\,E^2$. Fourier decomposition gives decoupled modes with Hamiltonians $\hat{h}_{k_1}$ (Eq. 14) and $\hat{h}_{-k_1}$ (Eq. 15).

Gaussian ansatz $\psi_{k_1} = \beta_{k_1}(t)\exp[-\alpha_{k_1}(t)|\phi_{k_1}|^2]$ (Eq. 18) yields $\dot{\alpha}_{k_1} = -i\alpha_{k_1}^2/2 + i\omega_{k_1}^2(t)/2$ (Eq. 20) with $\omega_{k_1}^2(t) = m^2 + (k_1 + qA_1(t))^2$. Particle number $\langle n_{k_1}\rangle = |z_{k_1}|^2/(1-|z_{k_1}|^2)$ (Eq. 26) with $z_{k_1} = (\omega_{k_1} - \alpha_{k_1})/(\omega_{k_1} + \alpha_{k_1})$ (Eq. 27). Initial condition: $\alpha_{k_1}(0) = \sqrt{m^2 + k_1^2}$ (Eq. 28).

**Section 3: Backreaction framework.** Semiclassical equation $-dE/dt = \langle \hat{J}^\mu_Q\rangle$ (Eq. 29). Current operator $\hat{J}^\mu_Q = \eta^{\mu\nu}[-iq(\phi^\dagger\partial_\nu\phi - \partial_\mu\phi^\dagger\phi) - 2q^2 A_\nu\phi^\dagger\phi]$ (Eq. 30). Zero-th component vanishes; spatial component in vacuum state gives $\langle\hat{J}^1_Q\rangle = 4q^2 A_1(t)\int_0^\infty (dk_1/2\pi)\langle|\phi_{k_1}|^2\rangle$ (Eq. 32).

Using Gaussian ansatz $\langle|\phi_{k_1}|^2\rangle = 1/(4\text{Re}\,\alpha_{k_1})$ (Eq. 34), coupled system: $\dot{E} = -q^2 A_1(t)\int_0^\infty (dk_1/2\pi) [\text{Re}\,\alpha_{k_1}(t)]^{-1}$ (Eq. 35). UV regulated by lattice with spacing $\ell$ (Eq. 36). Dimensionless variable $\tau = -\sqrt{q/E_0}A_1(t)$ gives coupled Eqs. 37, 38, 39.

**(1+3) extension.** Current $\langle\hat{J}^1_Q\rangle = (q^2 A_1/(4\pi\ell))\sum_n k_n^2/\text{Re}(\alpha_{k_n})$ (Eq. 44). Oscillation frequency $\omega_k^2 = |\mathbf{k}|^2 - 2q|k_1|A_1(t) + q^2 A_1^2(t)$.

**De Sitter extension (Sections 4–5).** Framework extended to cosmological backgrounds with expansion; formalism remains general. Backreaction generates plasma-like oscillations in both Minkowski and de Sitter.

## Key Results

1. Self-consistent semiclassical framework for Schwinger effect with full backreaction via TDSE + Poisson bracket evolution.
2. Without backreaction: $\langle n_k\rangle$ shows damped oscillations saturating to finite value (symmetric $|k|\leftrightarrow-|k|$).
3. With backreaction: immediate plasma-like oscillations in electric field and current (contrast with adiabatic methods producing transient plateau).
4. Framework handles (1+1) and (1+3) dimensions uniformly; transverse momentum acts as effective mass.
5. Time-averaged particle number remains essentially constant despite oscillations — oscillations reflect quantum interference, not net pair production.
6. No need for adiabatic regularization; normal-ordering subtraction handled by lattice UV cutoff.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| TDSE | $\hat{H}_2(Q,C)\psi(Q,t) = i\hbar\,\partial_t\psi(Q,t)$ | Eq. 1 |
| Classical evolution | $\dot{C} = \{C, H_{\text{eff}}\}$, $H_{\text{eff}} = H_1(C) + \langle\psi|\hat{H}_2|\psi\rangle$ | Eq. 2 |
| Hamiltonian density | $\mathcal{H} = E^2/2 + (1/2)[\Pi^\dagger\Pi + (\partial_1-iqA_1)\phi^\dagger(\partial_1+iqA_1)\phi + m^2\phi^\dagger\phi]$ | Eq. 3 |
| $\alpha$ EoM | $\dot{\alpha}_{k_1} = -i\alpha_{k_1}^2/2 + i\omega_{k_1}^2(t)/2$ | Eq. 20 |
| Particle number | $\langle n_{k_1}\rangle = \|z_{k_1}\|^2/(1-\|z_{k_1}\|^2)$ | Eq. 26 |
| $z$ definition | $z_{k_1}(t) = (\omega_{k_1} - \alpha_{k_1})/(\omega_{k_1} + \alpha_{k_1})$ | Eq. 27 |
| Initial condition | $\alpha_{k_1}(0) = \sqrt{m^2 + k_1^2}$ | Eq. 28 |
| Backreaction eq. | $-dE/dt = \langle\hat{J}^\mu_Q\rangle$ | Eq. 29 |
| Current | $\hat{J}^1_Q = iq(\phi^\dagger\partial_1\phi - \partial_1\phi^\dagger\phi) + 2q^2 A_1(t)(\phi^\dagger\phi)$ | Eq. 31 |
| Field EoM | $\dot{E} = -q^2 A_1(t)\int_0^\infty (dk_1/2\pi)/\text{Re}(\alpha_{k_1}(t))$ | Eq. 35 |
| (1+3) current | $\langle\hat{J}^1_Q\rangle = (q^2 A_1(t)/(4\pi\ell))\sum_n k_n^2/\text{Re}(\alpha_{k_n})$ | Eq. 44 |

## Relevance to Phonon-Exflation

Provides semiclassical backreaction framework directly applicable to the transit-cosmogenesis picture where pair creation (Parker-like, 59.8 quasiparticle pairs in project notation) back-reacts on the driving Jensen deformation gradient. The Gaussian state formalism and instantaneous mode occupation tracking are the analytic tools needed to compute GGE relic formation self-consistently, extending the S38 Schwinger-instanton duality ($S_{\text{Schwinger}} = S_{\text{inst}} = 0.069$) beyond the fixed-background approximation. Directly relevant to Feynman Test Step 6 (unitarity/backreaction consistency).
