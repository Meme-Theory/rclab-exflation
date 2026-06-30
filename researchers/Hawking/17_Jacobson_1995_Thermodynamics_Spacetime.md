# Thermodynamics of Spacetime: The Einstein Equation of State

**Author(s):** Ted Jacobson
**Year:** 1995
**Journal:** Physical Review Letters 75, 1260-1263 (1995)
**arXiv:** gr-qc/9504004
**Relevance:** CRITICAL

---

## Abstract

The Einstein equation is derived from the proportionality of entropy and horizon area together with the fundamental relation $\delta Q = T \, dS$ connecting heat, entropy, and temperature. The key idea is to demand that this relation hold for all the local Rindler causal horizons through each spacetime point, with $\delta Q$ and $T$ interpreted as the energy flux and Unruh temperature seen by an accelerated observer just inside the horizon. This requires that gravitational lensing by matter energy distorts the causal structure of spacetime in just such a way that the Einstein equation holds. Viewed in this way, the Einstein equation is an equation of state. This perspective suggests that it may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air.

---

## Key Arguments and Derivations

### Thermodynamic Analogy for Spacetime

Jacobson inverts the logic of black hole thermodynamics. Instead of deriving thermodynamic laws from the Einstein equation, he derives the Einstein equation from thermodynamics. The key ingredients:

1. **Heat** is defined as energy flux across a causal horizon.
2. **Entropy** is proportional to horizon area: $dS = \eta \, \delta\mathcal{A}$.
3. **Temperature** is the Unruh temperature of an accelerated observer: $T = \hbar\kappa / 2\pi$.

### Local Rindler Horizons

At each spacetime point $p$, consider a small spacelike 2-surface element $\mathcal{P}$ whose past-directed null normal congruence has vanishing expansion and shear at $p$. The past horizon of such a $\mathcal{P}$ is the "local Rindler horizon" -- an instantaneously stationary system in local equilibrium.

### Heat Flux

Let $\chi^a$ be an approximate local boost Killing field generating the horizon. The heat flux across the horizon is:

$$\delta Q = \int_{\mathcal{H}} T_{ab} \chi^a \, d\Sigma^b$$

With $\chi^a = -\kappa\lambda k^a$ and $d\Sigma^a = k^a \, d\lambda \, d\mathcal{A}$:

$$\delta Q = -\kappa \int_{\mathcal{H}} \lambda \, T_{ab} k^a k^b \, d\lambda \, d\mathcal{A}$$

### Area Variation via Raychaudhuri Equation

The Raychaudhuri equation for the null generators:

$$\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{ab} k^a k^b$$

Since $\theta$ and $\sigma$ vanish at $\mathcal{P}$ (local equilibrium), integrating gives $\theta = -\lambda R_{ab} k^a k^b$, and:

$$\delta\mathcal{A} = -\int_{\mathcal{H}} \lambda \, R_{ab} k^a k^b \, d\lambda \, d\mathcal{A}$$

### Deriving the Einstein Equation

Imposing $\delta Q = T \, dS = (\hbar\kappa/2\pi) \eta \, \delta\mathcal{A}$ requires:

$$T_{ab} k^a k^b = \frac{\hbar\eta}{2\pi} R_{ab} k^a k^b$$

for all null $k^a$. This implies:

$$\frac{2\pi}{\hbar\eta} T_{ab} = R_{ab} + f g_{ab}$$

for some function $f$. Conservation $\nabla^a T_{ab} = 0$ plus the contracted Bianchi identity fixes $f = -R/2 + \Lambda$, yielding:

$$R_{ab} - \frac{1}{2}R g_{ab} + \Lambda g_{ab} = \frac{2\pi}{\hbar\eta} T_{ab}$$

Newton's constant is determined: $G = (4\hbar\eta)^{-1}$, identifying $\eta^{-1/2}$ as twice the Planck length.

### Implications for Quantization

Jacobson argues that the Einstein equation is an **equation of state** -- a macroscopic thermodynamic relation. Just as one should not canonically quantize the wave equation for sound in air, it may be inappropriate to canonically quantize the Einstein equation. Non-equilibrium spacetime would be the analog of non-adiabatic fluid dynamics.

---

## Key Results

1. The Einstein equation (with cosmological constant) is derived purely from $\delta Q = T \, dS$ applied to local Rindler horizons, with $S \propto A$ and $T = \hbar\kappa/2\pi$.
2. Newton's constant emerges from the proportionality constant between entropy and area: $G = (4\hbar\eta)^{-1}$.
3. The cosmological constant $\Lambda$ appears as an undetermined integration constant.
4. Changing the entropy functional changes the field equations: if entropy density is a polynomial in $R$, the field equations arise from a polynomial Lagrangian.
5. The Einstein equation is an equation of state, suggesting canonical quantization of gravity may be as inappropriate as quantizing sound waves.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Fundamental relation | $\delta Q = T \, dS$ | Central thesis |
| Heat flux | $\delta Q = \int_{\mathcal{H}} T_{ab}\chi^a \, d\Sigma^b$ | Eq. (1) |
| Heat flux (affine) | $\delta Q = -\kappa \int_{\mathcal{H}} \lambda \, T_{ab} k^a k^b \, d\lambda \, d\mathcal{A}$ | Eq. (2) |
| Area variation | $\delta\mathcal{A} = \int_{\mathcal{H}} \theta \, d\lambda \, d\mathcal{A}$ | Eq. (3) |
| Raychaudhuri equation | $\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{ab}k^a k^b$ | Eq. (4) |
| Focussed area variation | $\delta\mathcal{A} = -\int_{\mathcal{H}} \lambda \, R_{ab} k^a k^b \, d\lambda \, d\mathcal{A}$ | Eq. (5) |
| Einstein equation (derived) | $R_{ab} - \frac{1}{2}Rg_{ab} + \Lambda g_{ab} = \frac{2\pi}{\hbar\eta}T_{ab}$ | Eq. (6) |
| Unruh temperature | $T = \hbar\kappa / 2\pi$ | Page 4 |
| Newton's constant | $G = (4\hbar\eta)^{-1}$ | Page 6 |
| Entropy-area | $dS = \eta \, \delta\mathcal{A}$ | Page 5 |
| Higher-curvature extension | $(2\pi/\hbar\eta)T_{ab} = R_{ab} - \nabla_a\nabla_b\rho + fg_{ab}$ | Ref. [9] |

## Relevance to Phonon-Exflation

Jacobson's vision -- gravity as thermodynamics of spacetime microstructure -- is realized in the phonon-exflation framework where the spectral action IS the free energy of the internal geometry. The spectral action $\text{Tr}(f(D^2/\Lambda^2))$ = von Neumann entropy (Paper 20, CCS 2018) provides the microscopic underpinning Jacobson envisioned. The framework gives $\delta Q = T \, dS$ a concrete realization: heat is the energy flux of Bogoliubov-created quasiparticles across the transit horizon (the fold in $\tau$-space), and entropy is the spectral action evaluated on the evolving Dirac spectrum. Jacobson's warning against quantizing the Einstein equation aligns with the framework's bottom-up emergence: gravity emerges from the substrate, not the reverse.
