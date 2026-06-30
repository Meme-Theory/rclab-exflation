# Non-Fermi-Liquid/Marginal-Fermi-Liquid Signatures Induced by Van Hove Singularity

**Author(s):** Yi-Hui Xing, Wu-Ming Liu
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2401.10707
**Relevance:** MEDIUM

---

## Abstract

We theoretically study the two-dimensional metal that is coupled to critical magnons and features van Hove singularities on the Fermi surface. When there is only translationally invariant SYK-liked Yukawa interaction, van Hove points suppress the contribution from the part of the Fermi surface away from them, dominating and exhibiting non-Fermi-liquid behavior. When introducing disordered Yukawa coupling, it leads to a crossover from non-Fermi-liquid to marginal-Fermi-liquid, and the marginal-Fermi-liquid region exhibits the T ln(1/T) specific heat and temperature-linear resistivity of strange metal. By solving the gap equation, we provide the critical temperature for superconductor induced by van Hove singularities and point out the possible emergence of pair-density-wave superconductor. Our theory may become a new mechanism for understanding non-Fermi-liquid or marginal-Fermi-liquid phenomenons.

---

## Key Arguments and Derivations

### Model setup

A two-dimensional normal metal (NM) coupled to a ferromagnetic insulator (FMI) via exchange coupling. The interface Hamiltonian includes:
- Electron hopping H = -sum_{i,j,sigma} t_{ij} c^dag_{i,sigma} c_{j,sigma}
- Magnon spectrum omega_k = k^2 + Delta (tunable via anisotropy K and out-of-plane momentum k_z)
- Two types of Yukawa coupling: translationally invariant (SYK-like, variance |J|^2) and spatially disordered (variance |J'|^2)

Near the VHS, the electron dispersion is epsilon_k = k_x^2 + a k_y^2 with a < 0 (saddle point).

### NFL from translationally invariant coupling

With only the space-independent SYK Yukawa coupling (J' = 0):
- Magnon self-energy: Pi(i Omega_m, q) - Pi(0,0) ~ |J|^2 (N/N') f(q_x, q_y, -a) |Omega_m|
- Electron self-energy: Sigma(i omega_n, 0) - Sigma(0,0) ~ -i|J| sqrt(N'/N) sgn(omega_n) |omega_n|^{1/2}

The |omega|^{1/2} quasiparticle decay rate is NFL behavior, dominated by VHS scattering (suppresses the |omega|^{2/3} from hot-spot scattering on circular Fermi surface).

### MFL from disordered coupling

With only the spatially dependent coupling (J = 0):
- Magnon self-energy: Pi(i Omega_m) - Pi(0) ~ -|J'|^2 (N/N') |Omega_m|
- Electron self-energy: Sigma(i omega_n) - Sigma(0) ~ -i|J'|^2 omega_n ln(N'/N |omega_n|)

This gives MFL scaling with T ln(1/T) specific heat and T-linear resistivity.

### Crossover

When both couplings are present:
- N >> N': MFL dominates
- N << N': NFL (|omega|^{1/2}) dominates
- The crossover depends on the ratio |J'|/|J| (see Fig. 2)

### Superconductivity and PDW

The SC critical temperature depends on the coupling type:
- Translational invariant: T_C ~ (|J|/sqrt(N))^3
- Disordered: T_C ~ exp(-sqrt(N)/|J'|)
- With multiple VHPs on the Fermi surface, pair-density-wave (PDW) order with condensed momentum K_1 + K_2 competes with conventional SC.

---

## Key Results

1. VHS suppresses Fermi surface contributions away from Van Hove points, making VHS the dominant source of NFL behavior
2. Translationally invariant Yukawa coupling gives NFL with Im Sigma ~ |omega|^{1/2} (dynamic critical exponent z = 4)
3. Disordered Yukawa coupling gives MFL with Im Sigma ~ omega ln|omega| (z = 2), yielding strange metal T-linear resistivity
4. Crossover between NFL and MFL controlled by N/N' ratio or |J'|/|J|
5. SC critical temperature has power-law (T_C ~ |J|^3) or exponential (T_C ~ exp(-1/|J'|)) dependence on coupling strength
6. Multiple VHPs enable PDW superconductivity competing with conventional SC

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Effective Lagrangian | $\mathcal{L} = \psi^\dagger[\partial_\tau - \partial_x^2 - a\partial_y^2]\psi + (\partial\phi)^2 + H_{\text{int}}$ | Eq. (6) |
| NFL self-energy | $\Sigma(i\omega_n, 0) \sim -i|J|\sqrt{N'/N}\,\text{sgn}(\omega_n)|\omega_n|^{1/2}$ | Eq. (3) |
| MFL self-energy | $\Sigma(i\omega_n) \sim -i|J'|^2 \omega_n \ln(N'/N|\omega_n|)$ | Eq. (4) |
| MFL resistivity | $\text{Re}[1/\sigma(\Omega \gg T)] = \frac{16\pi^4(-a)|\Omega|}{|J'|^2 N \Lambda_U^2 \ln\Lambda}$ | Eq. (5) |
| Magnon spectrum | $\omega_k = k^2 + \Delta$, $\Delta = k_z^2 + 4K/\bar{J}a^2$ | Text |
| VHS dispersion | $\varepsilon_k = k_x^2 + ak_y^2$ with $a < 0$ | Text |
| SC T_C (clean) | $T_C \sim (|J|/\sqrt{N})^3$ | Supp. Mat. |
| SC T_C (disordered) | $T_C \sim e^{-\sqrt{N}/|J'|}$ | Supp. Mat. |

## Relevance to Phonon-Exflation

The NFL/MFL behavior from VHS scattering is relevant to the framework's post-transit quasiparticle dynamics. The GGE relic state (Session 38) contains quasiparticle excitations near the Van Hove singularity at M_max = 1.674; the NFL self-energy Im Sigma ~ |omega|^{1/2} would modify their decay rates and transport properties. The PDW instability at multiple VHPs maps onto the framework's inter-sector pairing possibility: the three M-points of the kagome BZ correspond to inequivalent sectors of the SU(3) representation space, and PDW order between them would produce the finite-momentum condensate that PMNS mixing requires.
