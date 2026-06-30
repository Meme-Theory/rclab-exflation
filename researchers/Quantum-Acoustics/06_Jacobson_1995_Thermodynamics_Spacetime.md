# Thermodynamics of Spacetime: The Einstein Equation of State

**Author(s):** Ted Jacobson
**Year:** 1995
**Journal:** Physical Review Letters 75, 1260 (1995)
**arXiv:** gr-qc/9504004
**Relevance:** CRITICAL

---

## Abstract

The Einstein equation is derived from the proportionality of entropy and horizon area together with the fundamental relation $\delta Q = T\, dS$ connecting heat, entropy, and temperature. The key idea is to demand that this relation hold for all the local Rindler causal horizons through each spacetime point, with $\delta Q$ and $T$ interpreted as the energy flux and Unruh temperature seen by an accelerated observer just inside the horizon. This requires that gravitational lensing by matter energy distorts the causal structure of spacetime in just such a way that the Einstein equation holds. Viewed in this way, the Einstein equation is an equation of state. This perspective suggests that it may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air.

---

## Key Arguments and Derivations

### Motivation: Thermodynamic Origin of Gravity

Jacobson begins by noting that the four laws of black hole mechanics were originally derived from the classical Einstein equation. The discovery of quantum Hawking radiation revealed that this analogy is an identity -- horizon area is entropy and surface gravity is temperature. Jacobson asks: how did classical GR already "know" this? His answer reverses the logic: he derives the Einstein equation from thermodynamics.

### Defining Heat and Temperature

In thermodynamics, heat is energy flowing between degrees of freedom that are not macroscopically observable. Jacobson defines heat in the spacetime context as energy that flows across a causal horizon -- it can be felt via the gravitational field it generates, but its particular form or nature is unobservable from outside. The horizon need not be a black hole event horizon; it can be the boundary of the past of any set $\mathcal{O}$ (observer). The system is the degrees of freedom beyond the horizon, separated from the outside not by a diathermic wall but by a causality barrier.

Entropy is associated with causal horizons because they hide information. The dominant contribution is entanglement entropy from vacuum fluctuations straddling the horizon, which is proportional to the horizon area when a fundamental cutoff $l_c$ exists. The temperature is the Unruh temperature $T = \hbar\kappa/2\pi$ seen by a uniformly accelerated observer just inside the horizon.

### Local Rindler Horizons and Equilibrium

To apply equilibrium thermodynamics, Jacobson introduces the concept of a "local Rindler horizon." Through any spacetime point $p$, one considers a small spacelike 2-surface element $\mathcal{P}$ whose past-directed null normal congruence has vanishing expansion and shear at $p$ (instantaneously stationary, hence "local equilibrium"). The system beyond this horizon is the thermodynamic system.

### The Derivation

**Step 1 -- Heat flux.** Let $\chi^a$ be the approximate local boost Killing field generating the horizon, chosen future-pointing to the inside past of $\mathcal{P}$. The heat flux across the horizon is:

$$\delta Q = \int_{\mathcal{H}} T_{ab}\chi^a d\Sigma^b$$

With $k^a$ the tangent vector to the null generators (affine parameter $\lambda$ vanishing at $\mathcal{P}$, negative to the past), $\chi^a = -\kappa\lambda k^a$ and $d\Sigma^a = k^a d\lambda\, d\mathcal{A}$:

$$\delta Q = -\kappa \int_{\mathcal{H}} \lambda\, T_{ab} k^a k^b\, d\lambda\, d\mathcal{A}$$

**Step 2 -- Entropy change.** Assuming entropy proportional to area, $dS = \eta\, \delta\mathcal{A}$:

$$\delta\mathcal{A} = \int_{\mathcal{H}} \theta\, d\lambda\, d\mathcal{A}$$

where $\theta$ is the expansion of the null generators.

**Step 3 -- Raychaudhuri equation.** The null geodesic congruence obeys:

$$\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{ab}k^a k^b$$

Since $\theta$ and $\sigma$ vanish at $\mathcal{P}$ (by construction), integration gives $\theta = -\lambda R_{ab}k^a k^b$ for small $\lambda$, and therefore:

$$\delta\mathcal{A} = -\int_{\mathcal{H}} \lambda\, R_{ab} k^a k^b\, d\lambda\, d\mathcal{A}$$

**Step 4 -- Clausius relation.** The requirement $\delta Q = T\, dS = (\hbar\kappa/2\pi)\eta\, \delta\mathcal{A}$ is satisfied if and only if $T_{ab}k^a k^b = (\hbar\eta/2\pi) R_{ab}k^a k^b$ for all null $k^a$. This implies:

$$\frac{2\pi}{\hbar\eta} T_{ab} = R_{ab} + f\, g_{ab}$$

for some function $f$. Local energy-momentum conservation ($\nabla^a T_{ab} = 0$) and the contracted Bianchi identity then fix $f = -R/2 + \Lambda$ for some constant $\Lambda$, yielding the Einstein equation:

$$R_{ab} - \frac{1}{2}R\, g_{ab} + \Lambda\, g_{ab} = \frac{2\pi}{\hbar\eta}\, T_{ab}$$

The proportionality constant $\eta$ determines Newton's constant: $G = (4\hbar\eta)^{-1}$, identifying $\eta^{-1/2}$ as twice the Planck length.

### Implications

1. **Einstein equation as equation of state:** Gravity is not a fundamental interaction but an equation of state describing the thermodynamic limit of unknown microscopic degrees of freedom, valid under local equilibrium conditions.

2. **Against canonical quantization of gravity:** Since the Einstein equation is an equation of state (like the ideal gas law), canonically quantizing it is as inappropriate as quantizing the wave equation for sound in air. The sound field is a statistically defined observable, not a fundamental field.

3. **Breakdown at high frequency:** At sufficiently high frequency or large amplitude, local equilibrium fails and the Einstein equation breaks down -- not because the metric becomes a quantum operator, but because equilibrium conditions are violated. This is analogous to how sound ceases to propagate as an adiabatic wave at sufficiently high frequency.

4. **Modified entropy functionals:** If the entropy density is polynomial in the Ricci scalar ($\alpha_0 + \alpha_1 R + \ldots$), then $\delta Q = T\, dS$ implies field equations arising from a Lagrangian polynomial in $R$. The entropy density must likely arise from the variation of a generally covariant action, linking it to black hole entropy.

---

## Key Results

1. **Einstein equation derived from $\delta Q = T\,dS$:** The Einstein field equation follows uniquely from requiring the Clausius relation to hold for all local Rindler horizons at every spacetime point.
2. **Newton's constant from entropy-area proportionality:** $G = (4\hbar\eta)^{-1}$, where $\eta$ is the entropy per unit area, identifying the cutoff scale as the Planck length.
3. **Cosmological constant undetermined:** $\Lambda$ enters as an integration constant -- "as enigmatic as ever."
4. **Gravity as emergent thermodynamics:** The Einstein equation is an equation of state, not a fundamental law, born in the thermodynamic limit and depending on local equilibrium.
5. **Generalization to higher-curvature gravity:** Modified entropy-area relations imply modified gravitational field equations from corresponding Lagrangians.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Heat flux (boost energy) | $\delta Q = \int_{\mathcal{H}} T_{ab}\chi^a d\Sigma^b$ | Eq. (1) |
| Heat flux (affine form) | $\delta Q = -\kappa \int_{\mathcal{H}} \lambda\, T_{ab}k^a k^b\, d\lambda\, d\mathcal{A}$ | Eq. (2) |
| Area variation | $\delta\mathcal{A} = \int_{\mathcal{H}} \theta\, d\lambda\, d\mathcal{A}$ | Eq. (3) |
| Raychaudhuri equation | $\frac{d\theta}{d\lambda} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{ab}k^a k^b$ | Eq. (4) |
| Area change from curvature | $\delta\mathcal{A} = -\int_{\mathcal{H}} \lambda\, R_{ab}k^a k^b\, d\lambda\, d\mathcal{A}$ | Eq. (5) |
| Einstein equation | $R_{ab} - \frac{1}{2}Rg_{ab} + \Lambda g_{ab} = \frac{2\pi}{\hbar\eta}T_{ab}$ | Eq. (6) |
| Newton's constant | $G = (4\hbar\eta)^{-1}$ | After Eq. (6) |
| Unruh temperature | $T = \hbar\kappa / 2\pi$ | Sec. derivation |

---

## Relevance to Phonon-Exflation

Jacobson's result is one of the theoretical pillars of phonon-exflation cosmology. His derivation shows that the Einstein equation is an emergent thermodynamic equation of state, not a fundamental law -- precisely the ontological status gravity has in the M4 x SU(3) framework where spacetime geometry emerges from the spectral properties of the internal fiber. The explicit analogy Jacobson draws between gravity and sound in air ("it may be no more appropriate to canonically quantize the Einstein equation than it would be to quantize the wave equation for sound in air") directly supports the framework's treatment of particles as phononic excitations. The derivation also shows that Newton's constant is determined by the entropy-area proportionality constant, which in the framework corresponds to the UV scale of the SU(3) compactification. The result that modified entropy functionals yield modified gravitational field equations connects to the project's spectral action approach, where the gravitational action emerges from the spectral geometry of the Dirac operator rather than being postulated.
