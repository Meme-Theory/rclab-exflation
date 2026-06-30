# Kaluza-Klein Schwinger Effect

**Author(s):** Yusuke Yamada
**Year:** 2024
**Journal:** Progress of Theoretical and Experimental Physics (preprint: arXiv:2403.13451)
**arXiv:** 2403.13451
**Relevance:** HIGH

---

## Abstract

We show that electric fields in compactified spaces may produce Kaluza-Klein (KK) particles even when the energy of electric fields is smaller than KK scale. As an illustrating example, we consider a charged massless complex scalar coupled to U(1) gauge theory in $\mathbb{R}^{1,3} \times S^1$ and discuss the effect of background gauge potential along a compact direction. The electric field produces the charged Kaluza-Klein particle non-perturbatively, which we call KK Schwinger effect. We quantitatively show that KK modes can be produced even when the electric field energy is much below the KK scale. The mechanism is rather general and similar phenomena would occur in any compactification models when a gauge potential along compact direction evolves in time and experiences large enough field excursion. We also discuss the subtlety of four dimensional effective theory truncated by KK modes at an initial time, when the electric field is turned on.

---

## Key Arguments and Derivations

### Setup (Sec. 2)

A massless complex scalar $\Phi$ charged under U(1) in (4+1)D with the extra space compactified to $S^1$: $ds^2 = \eta_{\mu\nu}dx^\mu dx^\nu + (2\pi R)^2 dy^2$. A background electric field along the compact direction: $A_y = \zeta(t) \to E_y = \dot{\zeta}$.

KK decomposition gives time-dependent masses:
$$M_n^2(t) = \frac{1}{(2\pi R)^2}(n + q\zeta(t))^2$$

where $n$ is the KK number, $q$ is the U(1) charge, and $\zeta(t)$ is the dimensionless gauge potential.

### Quantization and Particle Production (Sec. 2)

The mode function $f_{n,k}$ satisfies:
$$\ddot{f}_{n,k}(t) + (k^2 + M_n^2(t))f_{n,k}(t) = 0$$

Using adiabatic expansion with Bogoliubov coefficients $\alpha_{n,k}(t)$ and $\beta_{n,k}(t)$:
$$|\alpha_{n,k}|^2 - |\beta_{n,k}|^2 = 1$$

The particle number density is:
$$\langle \hat{N}_{n,k}(t) \rangle = |\beta_{n,k}(t)|^2$$

### KK Schwinger Effect (Sec. 3)

**Key mechanism:** The electric field "decelerates" KK momentum. A mode with KK number $n$ becomes effectively massless ($M_n^2 \to 0$) when $n + q\zeta(t) = 0$, at which point it is non-perturbatively produced via the Schwinger mechanism.

**Model (i): Constant electric field** $\zeta_c(t) = Et\Theta(t)\Theta(t_f - t)$

The production rate for each KK mode that crosses zero mass:
$$\langle \hat{N}_{n,k} \rangle = \exp\left(-\frac{\pi k^2}{qE}\right) \quad \text{for } n \leq -\lfloor qEt_f \rfloor$$

Production is independent of KK number $n$ -- each mode that crosses zero is produced with the same Schwinger rate. Multiple KK particles can be produced however small $E$ is, as long as the integrated deceleration $\Delta\zeta$ is large enough.

**Model (ii): Damped oscillation** $\zeta_c(t) = (E/m)e^{-\gamma t}\cos(mt)$

Resonant (parametric) particle production occurs -- burst production like preheating after inflation. The $n = 1$ mode experiences resonant amplification. Modes with $n > |\Delta\zeta_c|/M_{\text{KK}}$ are not created.

### Backreaction (Sec. 4)

The produced KK pairs induce an electric current along the compact direction that shields the electric field:
$$\ddot{\zeta}_c + \sum_{n \in \mathbb{Z}} 2q(nM_{\text{KK}} + q\zeta_c)\langle|\hat{\phi}_n|^2\rangle_{\text{ren}} = 0$$

Numerical solution shows backreaction eventually traps $\zeta_c$ at a fixed point in field space, stopping KK particle production. This is the modulus trapping mechanism.

### Implications (Sec. 3.3 & 5)

- The KK Schwinger effect occurs when $|\Delta\zeta_c| > M_{\text{KK}}$, even if $|\dot{\zeta}_c| \ll M_{\text{KK}}^2$
- This is NOT the distance conjecture (no infinite tower of light states; just a single mode crosses zero)
- 4D EFT truncated at the KK scale FAILS when the KK Schwinger effect operates
- Produced KK particles have conserved KK momentum (translational invariance) so lightest KK particles can only co-annihilate in pairs
- Mechanism is general: applies to any compactification with gauge fields along compact directions

---

## Key Results

1. Electric fields in compact spaces produce KK particles non-perturbatively, even when $E \ll M_{\text{KK}}^2$
2. The production condition is $|\Delta\zeta_c| > M_{\text{KK}}$ (total field excursion, not instantaneous strength)
3. Each KK mode that crosses zero mass is produced with the standard Schwinger rate $\sim e^{-\pi k^2/(qE)}$
4. Resonant production (parametric amplification) can dramatically enhance production in oscillatory models
5. Backreaction traps the gauge potential, eventually halting production (modulus trapping)
6. 4D effective theory truncated at the KK scale becomes invalid during the KK Schwinger effect
7. Produced KK particles carry conserved KK momentum and can only co-annihilate

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| KK mass | $M_n^2(t) = \frac{(n + q\zeta(t))^2}{(2\pi R)^2}$ | Eq. (5) |
| Mode equation | $\ddot{f}_{n,k} + (k^2 + M_n^2(t))f_{n,k} = 0$ | Eq. (8) |
| Particle number | $\langle\hat{N}_{n,k}\rangle = \|\beta_{n,k}(t)\|^2$ | Eq. (12) |
| Schwinger rate | $\langle\hat{N}_{n,k}\rangle = e^{-\pi k^2/(qE)}$ | Eq. (15) |
| Electric field energy | $\rho_E = \dot{\zeta}^2/(4\pi R g^2)$ | Eq. (14) |
| Backreaction equation | $\ddot{\zeta}_c + \sum_n 2q(nM_{\text{KK}} + q\zeta_c)\langle\|\hat{\phi}_n\|^2\rangle_{\text{ren}} = 0$ | Eq. (16) |

## Relevance to Phonon-Exflation

This paper is directly relevant to the Schwinger-instanton duality discovered in Session 38: $S_{\text{Schwinger}}(0.070) \approx S_{\text{inst}}(0.069)$. The KK Schwinger effect shows that gauge fields evolving along compact dimensions produce KK particles non-perturbatively -- exactly the mechanism operating during the tau transit in M4 x SU(3). The time-dependent KK mass formula $M_n^2(t) = (n + q\zeta(t))^2/(2\pi R)^2$ is the direct analog of the framework's tau-dependent Dirac spectrum. The backreaction-driven modulus trapping parallels the framework's finding that produced quasiparticles backreact on the geometry (3.7% backreaction, perturbative). The failure of 4D EFT during the KK Schwinger effect validates the framework's approach of retaining the full KK spectrum rather than truncating to zero modes.
