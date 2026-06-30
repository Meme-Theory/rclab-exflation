# Acoustic Metric and Planck Constants

**Author(s):** G.E. Volovik
**Year:** 2023
**Journal:** arXiv:2302.08894v3 [cond-mat.other]
**arXiv:** 2302.08894
**Relevance:** CRITICAL

---

## Abstract

Based on Akama-Diakonov (AD) theory of emergent tetrads, it was suggested that one can introduce two Planck constants, $\hbar$ and $\not{h}$, which are the parameters of the corresponding components of Minkowski metric, $g^{\mu\nu}_{\text{Mink}} = \text{diag}(-\hbar^2, \not{h}^2, \not{h}^2, \not{h}^2)$. In the AD theory, the interval $ds$ is dimensionless, as a result the metric elements and thus the Planck constants have nonzero dimensions. The Planck constant $\hbar$ has dimension of time, and the Planck constant $\not{h}$ has dimension of length. It is natural to compare $\not{h}$ with the Planck length $l_P$. However, this connection remains an open question, because the microscopic (trans-Planckian) physics of the quantum vacuum is not known. Here we study this question using the effective gravity emerging for sound wave quanta (phonons) in superfluid Bose liquid, where the microscopic physics is known, and the elements of the effective acoustic metric are determined by the parameters of the Bose liquid. Since the acoustic interval is dimensionless, one may introduce the effective "acoustic Planck constants". The acoustic Planck constant $\not{h}_{\text{ac}}$ has dimension of length and is on the order of the interatomic distance. This supports the scenario in which $\not{h} \sim l_P$. We also use the acoustic metric for consideration of dependence of $\hbar$ on the Hubble parameter in expanding Universe.

---

## Key Arguments and Derivations

### I. Introduction: Dimensionless Physics

Volovik begins from the Akama-Diakonov (AD) theory of quantum gravity, where the fundamental microscopic objects are fermionic fields and the spin connection gauge field. Gravitational tetrads emerge as vacuum expectation values of bilinear combinations of fermionic field operators:

$$E^a_\mu = \langle \hat{E}^a_\mu \rangle, \quad \hat{E}^a_\mu = \frac{1}{2}\left(\Psi^\dagger \gamma^a \partial_\mu \Psi - \Psi^\dagger \overleftarrow{\partial}_\mu \gamma^a \Psi\right)$$

The metric arises as the bilinear combination of tetrads: $g_{\mu\nu} = \eta_{ab} E^a_\mu E^b_\nu$. A key property is that tetrads have dimensions of inverse time or inverse length: $[E^a_0] = 1/[t]$ and $[E^a_i] = 1/[L]$. Consequently, the metric elements have dimensions $[g_{00}] = 1/[t]^2$, $[g_{ik}] = 1/[L]^2$, and the interval $ds^2 = g_{\mu\nu} dx^\mu dx^\nu$ is dimensionless: $[ds] = 1$. All diffeomorphism-invariant quantities (cosmological constant $\Lambda$, scalar curvature $R$, particle masses $M$, etc.) are also dimensionless. This is "dimensionless physics."

### II. Two Planck Constants from Minkowski Metric

In the non-relativistic limit, the wave equation for massive particles takes the form of the Schrodinger equation with two separate Planck constants entering the time and space derivatives:

$$i\hbar \partial_t \psi = -\frac{\not{h}^2}{2M}\nabla^2 \psi$$

where

$$\sqrt{-g^{00}_{\text{Mink}}} = \hbar, \quad g^{ik}_{\text{Mink}} = \not{h}^2 \delta^{ik}$$

The time-like Planck constant $\hbar$ has dimension of time $[\hbar] = [t]$, while the space-like Planck constant $\not{h}$ has dimension of length $[\not{h}] = [L]$. The Newton constant has dimension of length $[G] = [L]$, so one can form the Planck mass $M_P = \sqrt{\not{h}/G}$ (dimensionless) and Planck length $l_P = \not{h}/M_P = \sqrt{\not{h} G}$ with $[l_P] = [L]$.

### III. Acoustic Planck Constants

In superfluid $^4$He at zero temperature and zero external pressure, the phonon action for the phase $\Phi$ of the Bose condensate is:

$$S_{\text{ph}} = \frac{S}{\hbar} = \frac{m}{2\hbar} \int d^3x\, dt\, n\left((\nabla\Phi)^2 - \frac{1}{s^2}(\dot{\Phi} - \mathbf{v}\cdot\nabla\Phi)^2\right) = \frac{1}{2}\int d^4x \sqrt{-g}\, g^{\mu\nu}\nabla_\mu\Phi\nabla_\nu\Phi$$

where $n$ is the particle density, $m$ is the atom mass, $s$ is the speed of sound, and $\mathbf{v}$ is the superfluid velocity. The acoustic interval is dimensionless: $[ds] = 1$.

Setting the shift function $\mathbf{v} = 0$, the effective acoustic Minkowski metric is:

$$g^{00} = \frac{\hbar n s}{m}, \quad g^{ik} = \frac{\hbar n}{ms}\delta^{ik}, \quad \sqrt{-g} = \frac{\hbar^2 n^2}{m^2 s}$$

The acoustic Planck constants are identified from the Schrodinger equation for massive phonons:

$$\hbar_{\text{ac}}^2 = g^{00} = \frac{m}{\hbar n s}, \quad \not{h}_{\text{ac}}^2 = \hbar_{\text{ac}}^2 s^2 = \frac{ms}{\hbar n}$$

For the idealized quantum liquid where $msa = \hbar$ (all three UV energy scales coincide), one obtains $\hbar_{\text{ac}} = a/s$ and $\not{h}_{\text{ac}} = a$, where $a = n^{-1/3}$ is the interatomic distance. The space-like acoustic Planck constant equals the UV length scale.

### IV. Tolman Temperature and Hawking Radiation

The thermal distribution of massless phonons in an inhomogeneous liquid follows the Tolman law $T(\mathbf{r}) = T_0/\sqrt{-g_{00}(\mathbf{r})}$, where $T_0$ is the Tolman temperature with dimension of frequency. The Tolman temperature for phonons coincides with the background liquid temperature expressed as frequency: $T_0 = T_{\text{liquid}}/\hbar$. For Hawking radiation from an acoustic horizon: $T_0 = v'/2\pi$, where $v'$ is the velocity gradient at the horizon.

### V. Variation of Planck Constants in Expanding Universe

In de Sitter expansion with shift function $v = Hr$, the Planck constants may acquire corrections proportional to the squared Hubble parameter:

$$\frac{\Delta \not{h}}{\not{h}} \sim \frac{\Delta \hbar}{\hbar} \sim \hbar^2 H^2 \sim T_{\text{GH}}^2 \ll 1$$

where $T_{\text{GH}} = \hbar H / 2\pi$ is the Gibbons-Hawking temperature. These corrections are typically negligibly small throughout cosmological history, so the Planck constants and speed of light $c = \not{h}/\hbar$ are practically constant.

---

## Key Results

1. **Two Planck constants from dimensionless physics:** In the AD theory, the Minkowski metric contains two independent Planck constants -- $\hbar$ (dimension of time) and $\not{h}$ (dimension of length) -- as metric components.
2. **Acoustic Planck constants:** In superfluid $^4$He, effective acoustic Planck constants $\hbar_{\text{ac}}$ and $\not{h}_{\text{ac}}$ are expressed in terms of liquid parameters ($m$, $n$, $s$).
3. **$\not{h}_{\text{ac}} \sim a$ (interatomic distance):** The space-like acoustic Planck constant equals the UV length scale, supporting the scenario $\not{h} \sim l_P$ in relativistic vacuum.
4. **Hawking temperature universal:** $T_0 = v'/2\pi$ applies identically in both acoustic and Schwarzschild geometries.
5. **Planck constants nearly constant:** Cosmological expansion induces corrections $\sim T_{\text{GH}}^2 \ll 1$, preserving constancy of $\hbar$, $\not{h}$, and $c$.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Emergent tetrad | $\hat{E}^a_\mu = \frac{1}{2}(\Psi^\dagger \gamma^a \partial_\mu \Psi - \Psi^\dagger \overleftarrow{\partial}_\mu \gamma^a \Psi)$ | Eq. (1) |
| Metric from tetrads | $g_{\mu\nu} = \eta_{ab} E^a_\mu E^b_\nu$ | Eq. (2) |
| Schrodinger with two $\hbar$ | $i\hbar \partial_t \psi = -\frac{\not{h}^2}{2M}\nabla^2 \psi$ | Eq. (4) |
| Two Planck constants | $\sqrt{-g^{00}_{\text{Mink}}} = \hbar$, $g^{ik}_{\text{Mink}} = \not{h}^2 \delta^{ik}$ | Eq. (5) |
| Planck length | $l_P = \not{h}/M_P = \sqrt{\not{h} G}$ | Eq. (6) |
| Phonon action | $S_{\text{ph}} = \frac{m}{2\hbar}\int d^3x\, dt\, n\left((\nabla\Phi)^2 - \frac{1}{s^2}(\dot{\Phi} - \mathbf{v}\cdot\nabla\Phi)^2\right)$ | Eq. (7) |
| Acoustic interval | $ds^2 = \frac{\hbar n}{ms}\left[-s^2 dt^2 + (dx^i - v^i dt)\delta_{ij}(dx^j - v^j dt)\right]$ | Eq. (8) |
| Acoustic Minkowski metric | $g^{00} = \frac{\hbar ns}{m}$, $g^{ik} = \frac{\hbar n}{ms}\delta^{ik}$ | Eq. (9) |
| Acoustic Planck constants | $\hbar_{\text{ac}}^2 = \frac{m}{\hbar ns}$, $\not{h}_{\text{ac}}^2 = \frac{ms}{\hbar n}$ | Eq. (15) |
| Tolman temperature | $T(\mathbf{r}) = T_0 / \sqrt{-g_{00}(\mathbf{r})}$ | Eq. (16) |
| Hawking temperature | $T_0 = v'/2\pi$ | Eq. (18) |
| UV energy scales | $E_{\text{UV1}} = ms^2$, $E_{\text{UV2}} = \hbar s/a$, $E_{\text{UV3}} = \hbar^2/ma^2$ | Eqs. (19)--(21) |
| Acoustic $\hbar_{\text{ac}}$ from UV | $\hbar_{\text{ac}}^2 = \hbar^2 / (E_{\text{UV2}} E_{\text{UV3}})$ | Eq. (22) |
| de Sitter interval | $ds^2 = -\frac{1}{\hbar^2}dt^2 + \frac{1}{\not{h}^2}\left((dr - Hrdt)^2 + r^2 d\Omega^2\right)$ | Eq. (23) |
| Pressure corrections | $\Delta\not{h}/\not{h} \sim \Delta\hbar/\hbar \sim P/(nms^2) \ll 1$ | Eq. (24) |
| Hubble corrections | $\Delta\not{h}/\not{h} \sim \Delta\hbar/\hbar \sim \hbar^2 H^2 \sim T_{\text{GH}}^2 \ll 1$ | Eq. (25) |

---

## Relevance to Phonon-Exflation

This paper is directly foundational for phonon-exflation cosmology. Volovik's demonstration that (i) the spacetime interval is dimensionless, (ii) Planck constants are metric components, and (iii) the space-like Planck constant equals the UV length scale (interatomic distance in the condensed-matter analogue) provides the precise mathematical template for the M4 x SU(3) framework. In phonon-exflation, the internal SU(3) fiber plays the role of the "quantum liquid" whose parameters determine the emergent 4D metric. The identification $\not{h}_{\text{ac}} \sim a$ supports the framework's use of the lattice/compactification scale as the fundamental length. The result that Planck constants acquire only $O(T_{\text{GH}}^2)$ corrections during expansion validates treating $\hbar$ as constant during the tau-transit. The Akama-Diakonov emergent tetrad construction directly parallels the project's use of Connes' spectral action where geometry emerges from fermionic degrees of freedom.
