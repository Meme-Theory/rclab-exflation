# The Unruh Effect and its Applications

**Author(s):** Luis C. B. Crispino, Atsushi Higuchi, George E. A. Matsas
**Year:** 2008
**Journal:** Reviews of Modern Physics 80 (2008) 787-838
**arXiv:** 0710.5373
**Relevance:** HIGH

---

## Abstract

It has been thirty years since the discovery of the Unruh effect. It has played a crucial role in our understanding that the particle content of a field theory is observer dependent. This effect is important in its own right and as a way to understand the phenomenon of particle emission from black holes and cosmological horizons. Here, we review the Unruh effect with particular emphasis to its applications. We also comment on a number of recent developments and discuss some controversies. Effort is also made to clarify what seems to be common misconceptions.

---

## Key Arguments and Derivations

### Section I: Introduction
Notes that the Unruh effect was on Feynman's blackboard as one of the things "to learn" at the time of his death in 1988. The effect expresses the fact that uniformly accelerated observers (Rindler observers) associate a thermal bath of Rindler particles to the no-particle state of inertial observers (Minkowski vacuum). Addresses two common misconceptions:
1. The heuristic expression of the Minkowski vacuum as a superposition of Rindler states makes sense in the whole of Minkowski spacetime, not just inside the Rindler wedges
2. The Unruh effect is NOT the equivalence of excitation rates between (i) a uniformly accelerated detector in vacuum and (ii) a static detector in a thermal bath of Minkowski particles --- this equivalence does not hold in general

Emphasizes that the Unruh effect is a quantum field theory result independent of detector models. The detailed balance relation for accelerated detectors is a *consequence* of the Unruh effect, not its definition.

### Section II: The Unruh Effect
**II.A - Free scalar field in curved spacetime** (reproduces Birrell & Davies 1982; Wald 1994):
- General framework of QFT in curved spacetimes with metric ds^2 = N(x)^2 dt^2 - G_{ab}(x) dx^a dx^b
- Klein-Gordon equation, inner product, Bogoliubov transformations
- Key result: <0^(2)| N^(1)_i |0^(2)> = sum_I |beta_{Ii}|^2 (particle number in one vacuum as seen by another)
- Static vacuum state is natural when the spacetime has a timelike Killing vector
- Fulling's observation (1973): the Rindler vacuum is distinct from the Minkowski vacuum restricted to the Rindler wedge

**II.B - Rindler wedges**:
- Boost Killing vector z(d/dt) + t(d/dz) divides Minkowski spacetime into four regions: right Rindler wedge (|t| < z), left Rindler wedge (|t| < -z), expanding and contracting degenerate Kasner universes
- Rindler coordinates: t = a^{-1} e^{a xi} sinh(a tau), z = a^{-1} e^{a xi} cosh(a tau)
- Metric: ds^2 = e^{2a xi}(d tau^2 - d xi^2) - dx^2 - dy^2
- World line at xi = 0 has constant proper acceleration a
- Killing horizons at t = +/- z where the boost Killing field becomes null

**II.C - Two-dimensional example** (massless scalar):
- Complete derivation of Bogoliubov coefficients between Minkowski and Rindler modes
- Derives the crucial relations: beta^L_{omega k} = -e^{-pi omega/a} alpha^{R*}_{omega k} and beta^R_{omega k} = -e^{-pi omega/a} alpha^{L*}_{omega k}
- Constructs the purely positive-frequency functions G_omega(V) and G-bar_omega(V) that are linear combinations of Rindler modes
- Derives the annihilation conditions on the Minkowski vacuum: (a^R_{+omega} - e^{-pi omega/a} a^{L dagger}_{+omega})|0_M> = 0
- Proves thermal occupation: <0_M| a^{R dagger}_{+omega_i} a^R_{+omega_i} |0_M> = (e^{2pi omega_i / a} - 1)^{-1}
- Derives the Minkowski vacuum as an entangled state over Rindler Fock spaces: |0_M> = prod_i C_i sum_{n_i} e^{-pi n_i omega_i / a} |n_i, R> tensor |n_i, L>
- Shows the reduced density matrix is exactly thermal: rho_R = prod_i C_i^2 sum_{n_i} e^{-2pi n_i omega_i / a} |n_i, R><n_i, R|

**II.D - Massive scalar field in Rindler wedges**:
- Full 4D calculation with transverse momenta k_perp
- Mode functions involve modified Bessel functions: g_{omega k_perp}(xi) proportional to K_{i omega/a}(kappa e^{a xi}/a)
- Same thermal result T = a/2pi

**II.E - Bogolubov coefficients and the Unruh effect**:
- Complete Bogoliubov coefficient calculation between Minkowski plane waves and Rindler modes
- Confirms the thermal spectrum for the massive case

**II.F - Completeness of Rindler modes in Minkowski spacetime**:
- Shows the Rindler mode expansion can be extended to the whole Minkowski spacetime
- Responds to criticisms by Narozhny et al. (2002, 2004) who questioned this completeness

**II.G - Unruh effect and Kasner universe**:
- Connection between the Unruh effect and QFT in the expanding degenerate Kasner universe

**II.H - Unruh effect and classical field theory**:
- Classical analogue: the Rindler vacuum has a nonzero Minkowski particle content even classically

**II.I - Unruh effect for interacting theories and other spacetimes**:
- Bisognano-Wichmann theorem: the Minkowski vacuum restricted to a Rindler wedge is a KMS (thermal) state for any Wightman QFT, not just free fields
- Connection to the Hartle-Hawking vacuum on bifurcate Killing horizons (Kay & Wald 1991)

### Section III: Applications
**III.A - Unruh-DeWitt detectors**:
- Two-level detector model coupled to the field via interaction Hamiltonian H_int = c m(tau) phi(x(tau))
- Inertial perspective: accelerated detector in vacuum has excitation rate proportional to the Wightman function
- Rindler perspective: static detector in a thermal bath of Rindler particles absorbs a Rindler quantum
- The detailed balance condition (ratio of excitation to de-excitation rates = e^{-omega/T}) is universal
- Circularly moving detectors: non-thermal but still show a modified Unruh-like effect

**III.B - Weak decay of non-inertial protons**:
- Accelerated protons can undergo beta decay (p -> n + e+ + nu_e) even when this is kinematically forbidden for inertial protons
- Inertial perspective: the external field causes the decay
- Rindler perspective: the proton absorbs a thermal fermion from the Rindler bath and decays
- Both perspectives give the same decay rate, providing a consistency check of the Unruh effect

**III.C - Bremsstrahlung**:
- Classical bremsstrahlung from an accelerated charge viewed in both inertial and Rindler frames
- Inertial frame: the charge radiates real photons (Larmor radiation)
- Rindler frame: the charge is static but absorbs and emits Rindler photons, with zero net radiation consistent with inertial observation

### Section IV: Experimental Proposals
- Electrons in particle accelerators (required acceleration ~ 10^{25} m/s^2 for T ~ 1 K, far beyond current technology)
- Electrons in Penning traps
- Atoms in microwave cavities
- Backreaction radiation in ultraintense lasers
- Thermal spectra in hadronic collisions (Hagedorn temperature connection)
- Dynamical Casimir effect (Moore effect) as a related phenomenon

### Section V: Recent Developments
- Entanglement degradation for accelerated observers: Rindler observers have reduced entanglement fidelity
- Decoherence of accelerated detectors
- Generalized second law of thermodynamics and the "self-accelerating box paradox"
- Einstein equations as an equation of state (Jacobson 1995 connection)

---

## Key Results

1. **Unruh temperature**: T = hbar a / (2 pi k_B c), where a is the proper acceleration. The Minkowski vacuum is a thermal state with this temperature for a uniformly accelerated observer.

2. **Minkowski vacuum as entangled thermal state**: |0_M> = prod_i C_i sum_{n_i} e^{-pi n_i omega_i / a} |n_i, R> tensor |n_i, L>, where C_i = sqrt(1 - e^{-2pi omega_i / a}).

3. **Reduced density matrix is exactly thermal**: rho_R = prod_i (1 - e^{-2pi omega_i / a}) sum_{n_i} e^{-2pi n_i omega_i / a} |n_i, R><n_i, R|.

4. **Bisognano-Wichmann theorem**: The thermal nature of the Unruh effect holds for arbitrary Wightman QFTs, not just free fields.

5. **Beta decay of accelerated protons**: Provides a physical application where the Unruh thermal bath has real physical consequences --- an accelerated proton can decay via processes forbidden for inertial protons.

6. **Detector independence**: The Unruh effect is a QFT result about the state structure, not about detector models. The detailed balance relation is a consequence, not a definition.

7. **No experimental detection yet**: The required acceleration (~10^{25} m/s^2) for T ~ 1 K makes direct detection extremely challenging with current technology.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Klein-Gordon inner product | $(f_A, f_B)_{\rm KG} = i \int d^D x \sqrt{G} N^{-1} (f_A^* \partial_t f_B - f_B \partial_t f_A^*)$ | Eq. 2.6 |
| Bogoliubov transformation | $\hat{a}^{(2)}_I = \sum_i (\alpha^*_{Ii} \hat{a}^{(1)}_i - \beta^*_{Ii} \hat{a}^{(1)\dagger}_i)$ | Eq. 2.27 |
| Particle production | $\langle 0^{(1)} | N^{(2)}_I | 0^{(1)} \rangle = \sum_i |\beta_{Ii}|^2$ | Eq. 2.29 |
| Rindler metric | $ds^2 = e^{2a\xi}(d\tau^2 - d\xi^2) - dx^2 - dy^2$ | Eq. 2.37 |
| Rindler coordinates | $t = a^{-1} e^{a\xi} \sinh(a\tau)$, $z = a^{-1} e^{a\xi} \cosh(a\tau)$ | Eq. 2.36 |
| Crucial Bogoliubov relation | $\beta^L_{\omega k} = -e^{-\pi\omega/a} \alpha^{R*}_{\omega k}$ | Eq. 2.60 |
| Vacuum annihilation condition | $(a^R_{+\omega} - e^{-\pi\omega/a} a^{L\dagger}_{+\omega})|0_M\rangle = 0$ | Eq. 2.66 |
| Thermal occupation number | $\langle 0_M | a^{R\dagger}_{+\omega} a^R_{+\omega} | 0_M \rangle = (e^{2\pi\omega/a} - 1)^{-1}$ | Eq. 2.70 |
| Minkowski vacuum state | $|0_M\rangle = \prod_i C_i \sum_{n_i} e^{-\pi n_i \omega_i/a} |n_i, R\rangle \otimes |n_i, L\rangle$ | Eq. 2.76 |
| Thermal density matrix | $\hat{\rho}_R = \prod_i C_i^2 \sum_{n_i} e^{-2\pi n_i \omega_i/a} |n_i, R\rangle \langle n_i, R|$ | Eq. 2.78 |
| Unruh temperature | $T = a / 2\pi$ (natural units) | Sec. II.C |
| Massive Rindler modes | $v^R_{\omega k_\perp} \propto K_{i\omega/a}(\kappa e^{a\xi}/a) e^{ik_\perp \cdot x_\perp - i\omega\tau}$ | Eq. 2.92 |

## Relevance to Phonon-Exflation

The Unruh effect is the flat-spacetime prototype for the observer-dependent particle content that is central to the phonon-exflation framework. The framework's T_ACOUSTIC-40 result (T_a/T_Gibbs = 1.40 Rindler ratio) directly uses the Unruh temperature formula. The entangled structure of the Minkowski vacuum across Rindler wedges (Eq. 2.76) is the same mathematical structure as the entanglement between the KK fiber and the 4D base during transit. The Bisognano-Wichmann theorem's generality to interacting theories is relevant because the framework's instanton gas is strongly interacting (g*N(E_F) = 2.18, BCS-BEC crossover regime). The absence of a horizon in the KK geometry means the framework's particle creation is cosmological (Parker-type) rather than Unruh/Hawking-type, but the Bogoliubov coefficient technology is identical.
