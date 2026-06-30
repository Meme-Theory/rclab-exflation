# Self-tuning vacuum variable and cosmological constant

**Author(s):** F.R. Klinkhamer, G.E. Volovik
**Year:** 2008
**Journal:** Physical Review D 77, 085015 (2008)
**arXiv:** 0711.3170
**Relevance:** CRITICAL

---

## Abstract

A spacetime-independent variable is introduced which characterizes a Lorentz-invariant self-sustained quantum vacuum. For a perfect (Lorentz-invariant) quantum vacuum, the self-tuning of this variable nullifies the effective energy density which enters the low-energy gravitational field equations. The observed small but nonzero value of the cosmological constant may then be explained as corresponding to the effective energy density of an imperfect quantum vacuum (perturbed by, e.g., the presence of thermal matter).

---

## Key Arguments and Derivations

### I. Introduction
The paper begins from the emergent-gravity perspective: if gravitation is only a low-energy effective interaction, gravitons as quasiparticles do not feel all microscopic degrees of freedom. The gravitating effect of the total vacuum energy density would then be effectively tuned away by elementary thermodynamic arguments, even if the details of microscopic physics remain unknown.

### II. Vacuum Variable and Thermodynamics
A new Lorentz-invariant variable $q$ is introduced to characterize the quantum vacuum. The vacuum is treated as a self-sustained medium (analogous to a water droplet in empty space). The effective action is:

$$S_{\text{eff}}[g, q] = \int d^4x \sqrt{-g} \left( \frac{1}{16\pi G_N} R[g] + \epsilon(q) \right)$$

The vacuum variable $q$ is a conserved quantity with chemical potential $\mu = d\epsilon/dq$. The energy-momentum tensor takes the cosmological-constant form $T_{\mu\nu}(q) = \rho_{\text{vac}}(q) g_{\mu\nu}$ with:

$$\rho_{\text{vac}}(q) = \epsilon(q) - q \frac{d\epsilon(q)}{dq}$$

This structure is argued on thermodynamic grounds: the vacuum energy density that enters Einstein's equations is not $\epsilon(q)$ itself but includes the chemical-potential correction.

### III. Self-tuning Mechanism
The equation of motion for $q$ yields $d\epsilon/dq = \mu = \text{constant}$. The equilibrium vacuum satisfies:
- $\rho_{\text{vac}}(q_0) = 0$ (zero effective cosmological constant)
- Positive vacuum compressibility $\chi = (q^2 d^2\epsilon/dq^2)^{-1} > 0$

The nullification of the cosmological constant follows from thermodynamic equilibrium without fine-tuning: the Planck-scale quantity $\epsilon(q_0)$ is compensated by $q_0 \, d\epsilon/dq|_{q_0}$.

### IV. Perturbation by Matter
The presence of thermal matter shifts $q$ away from equilibrium ($q \neq q_0$), producing a nonzero $\rho_{\text{vac}}$. The matter-induced shift is calculated: $\delta\rho_{\text{vac}} \propto T^8/(\chi E_P^2)$ for a radiation-dominated universe at temperature $T$.

### V. Origin of the Vacuum Variable
Two specific realizations of $q$ are discussed:
1. A four-form field strength $F_{\kappa\lambda\mu\nu}$ from a three-form gauge potential (Hawking's construction)
2. A four-velocity field realization

Both give the same universal macroscopic equations at the classical level.

## Key Results

1. The vacuum energy density entering Einstein's equations is $\rho_{\text{vac}} = \epsilon - q \, d\epsilon/dq$, not $\epsilon$ alone
2. In perfect thermodynamic equilibrium, $\rho_{\text{vac}} = 0$ without fine-tuning
3. The nonzero observed $\Lambda$ arises from the imperfect (perturbed) vacuum in an expanding universe
4. The vacuum variable $q$ is conserved and has an associated chemical potential $\mu$
5. Vacuum compressibility $\chi > 0$ ensures thermodynamic stability

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Effective action | $S_{\text{eff}} = \int d^4x \sqrt{-g} \left( \frac{R}{16\pi G_N} + \epsilon(q) \right)$ | Eq. (1) |
| Vacuum energy density | $\rho_{\text{vac}}(q) = \epsilon(q) - q \frac{d\epsilon(q)}{dq}$ | Eq. (4) |
| Equilibrium condition | $d\epsilon/dq = \mu = \text{const}$ | Eq. (9) |
| Self-tuning | $\rho_{\text{vac}}(q_0) = 0$ | Eq. (12) |
| Vacuum compressibility | $\chi = \left(q^2 \frac{d^2\epsilon}{dq^2}\right)^{-1}$ | Eq. (14) |
| Matter perturbation | $\delta\rho_{\text{vac}} \sim \frac{T^8}{\chi E_P^2}$ | Eq. (24) |

## Relevance to Phonon-Exflation

This is the founding paper of q-theory, which is directly analogous to the phonon-exflation framework's treatment of the vacuum. Key connections:
- The vacuum variable $q$ and its thermodynamic properties parallel the framework's treatment of the SU(3) fiber as a self-sustained medium with internal degrees of freedom
- The Gibbs-Duhem relation $\rho_{\text{vac}} = \epsilon - q \, d\epsilon/dq = 0$ in equilibrium is structurally identical to the framework's mechanism for CC nullification
- The vacuum compressibility $\chi$ connects to the framework's instanton gas dynamics: the vacuum responds to perturbations with a characteristic stiffness
- The matter-induced shift from equilibrium connects to the framework's picture of CC as an out-of-equilibrium residual from the transit/crystallization process
- The four-form realization of $q$ connects to Hawking's cosmological constant mechanism, which the framework has independently engaged
