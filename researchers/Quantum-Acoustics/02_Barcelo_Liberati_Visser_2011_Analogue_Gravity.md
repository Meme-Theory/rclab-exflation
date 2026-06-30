# Analogue Gravity

**Author(s):** Carlos Barcelo, Stefano Liberati, Matt Visser
**Year:** 2011 (Living Reviews in Relativity; major revision updated through 2024)
**Journal:** Living Reviews in Relativity 14, 3 (2011); revised version arXiv:gr-qc/0505065v4 (2024)
**arXiv:** gr-qc/0505065
**Relevance:** CRITICAL

---

## Abstract

Analogue gravity is a research programme that explores analogues of general relativistic gravitational fields within other physical systems, particularly but not exclusively in condensed matter systems, with the aim of gaining new insights into related problems. Analogue models of gravity boast a long and distinguished history, dating back to the early years of general relativity. This review article delves into the history, aims, results, and future prospects of various analogue models. We begin by presenting a particularly simple example of an analogue model, then traverse the rich history and complex array of models discussed in the literature. The last decade has witnessed significant and sustained advances in analogue gravity, resulting in hundreds of published articles, workshops, and books. The future of the analogue gravity programme looks promising, with rapid technological advances on the experimental front and the potential for analogue models to inspire innovative approaches to the problem of quantum gravity on the theoretical front. Most of all, these recent years have seen the rise of an unprecedented collaboration and interplay between different communities that we believe will set a new standard for interdisciplinary research in the years to come.

---

## Key Arguments and Derivations

### 1. Introduction and Motivation (Section 1)

The review establishes that analogue gravity investigates how analogues of general relativistic gravitational fields arise within other physical systems. The programme has multiple motivations: (i) probing aspects of general relativity (Hawking radiation, cosmological particle production) in laboratory settings where one has full control of the underlying microphysics, (ii) understanding trans-Planckian physics by studying how emergent Lorentzian geometry arises from non-relativistic substrates, and (iii) informing approaches to quantum gravity by providing concrete examples of emergent spacetime.

### 2. Acoustics: The Simplest Analogue Spacetime (Section 2)

#### 2.2 Geometrical Acoustics

The authors first show that in the eikonal (ray-tracing) limit, sound rays in a moving fluid behave exactly like null geodesics in a curved spacetime. The sound cones are tilted and distorted by the background flow, and if the flow speed exceeds the speed of sound, an acoustic horizon forms.

#### 2.3 Physical Acoustics -- The Central Derivation

The paper proves the following theorem:

**Theorem 1:** If a fluid is barotropic and inviscid, and the flow is irrotational (though possibly time dependent), then the equation of motion for the velocity potential describing a linearized acoustic disturbance $\varphi_1$ around some assumed background flow $\varphi_0$ is identical to the d'Alembertian equation of motion for a minimally-coupled massless scalar field propagating in a (3+1)-dimensional Lorentzian geometry specified by the background flow:

$$\Delta \varphi_1 \equiv \frac{1}{\sqrt{-g_0}} \partial_\mu \left( \sqrt{-g_0} \, [g_0]^{\mu\nu} \partial_\nu \varphi_1 \right) = 0$$

The proof proceeds by: (i) starting from the continuity equation $\partial_t \rho + \nabla \cdot (\rho \mathbf{v}) = 0$ and the Euler equation; (ii) assuming irrotational flow so $\mathbf{v} = -\nabla \varphi$; (iii) assuming a barotropic equation of state; (iv) linearizing all quantities around a background ($\rho_0, p_0, \varphi_0$) as $\rho = \rho_0 + \epsilon \rho_1 + O(\epsilon^2)$, etc.; (v) combining the linearized continuity and Euler equations to obtain a wave equation for $\varphi_1$ whose coefficients depend on the background fields.

The resulting wave equation can be recast as propagation in a Lorentzian geometry with acoustic metric:

$$[g_0]_{\mu\nu} = \frac{\rho_0}{c_s} \begin{pmatrix} -(c_s^2 - v_0^2) & -\mathbf{v}_0^T \\ -\mathbf{v}_0 & \mathbf{I} \end{pmatrix}$$

This is a remarkable result: even though the underlying fluid dynamics is Newtonian, nonrelativistic, and takes place in flat space-plus-time, the fluctuations (sound waves) are governed by a curved (3+1)-dimensional Lorentzian pseudo-Riemannian spacetime geometry.

#### 2.4 Horizons and Ergo-regions

The paper demonstrates that acoustic horizons form where the normal component of flow velocity equals the local speed of sound. The acoustic surface gravity is derived in analogy with the standard GR result, providing a definition for the Hawking temperature of an acoustic black hole.

#### 2.6--2.10 Worked Examples

The review works out several explicit acoustic spacetimes: vortex geometry (draining bathtub), slab geometry, conformal Schwarzschild geometry, the canonical acoustic black hole, and cosmological metrics (both expanding flows and time-varying speed of sound).

### 3. History (Section 3)

The historical survey spans: the pre-1981 period (Gordon's optical metric from 1923, early acoustic analogies), the classical period initiated by Unruh's 1981 paper, and the modern period featuring BEC experiments, optical analogues, surface-wave experiments, and the flourishing experimental programme.

### 4. Other Analogue Models (Section 4)

The review covers a comprehensive zoo of analogue models beyond acoustics:
- **Bose-Einstein condensates (BECs):** Phonons in BECs provide a particularly clean analogue due to the well-understood quantum microphysics (Gross-Pitaevskii equation).
- **Superfluid helium:** Both $^4$He (phonon-roton spectrum) and $^3$He-A (Fermi points giving emergent Weyl fermions and gauge fields).
- **Surface waves in shallow water:** Gravity waves in flowing water.
- **Electromagnetic analogues:** Dielectric media, nonlinear electrodynamics, meta-materials.
- **Normal mode meta-models:** Multi-field Lagrangian analysis showing how multi-refringence arises.
- **Slow light:** Light propagation in electromagnetically-induced transparency media.

### 5. Experimental Results (Section 5)

The review documents experimental confirmations:
- Steinhauer's observation of stimulated and spontaneous Hawking radiation analogues in BECs.
- Surface-wave analogues of horizons and Hawking radiation in water-tank experiments.
- Optical-fibre analogues.
- Phonon laser experiments.

### 6. Lessons for Quantum Gravity

A central theme is that the existence of Lorentz-violating trans-Planckian physics does not destroy the Hawking effect -- the thermal spectrum is robust against modifications at the UV cutoff scale. This is a key finding for quantum gravity: the Hawking effect does not depend on unknown trans-Planckian physics, as long as there is a sufficient separation of scales.

---

## Key Results

1. **Acoustic Metric Theorem:** Linearized sound in a barotropic, inviscid, irrotational fluid propagates on a (3+1)-dimensional Lorentzian geometry determined by the background density, velocity, and speed of sound.
2. **Acoustic Horizons:** Sonic horizons form where flow speed equals sound speed; they have well-defined surface gravity and Hawking temperature $T_H = \hbar \kappa / 2\pi$.
3. **Robustness of Hawking Radiation:** Trans-Planckian modifications (superluminal dispersion) do not destroy the thermal Hawking spectrum at leading order, as demonstrated in multiple analogue models.
4. **Emergent Lorentz Symmetry:** Even though the underlying physics is non-relativistic, the low-energy effective theory exhibits exact local Lorentz invariance for the acoustic fluctuations.
5. **Universality of Analogue Mechanism:** The acoustic metric construction generalizes to any Lagrangian system linearized about a background -- the causal structure of the fluctuation PDEs defines the analogue spacetime.
6. **Cosmological Analogue Metrics:** Expanding BECs and time-varying speed-of-sound systems reproduce FLRW-like cosmological spacetimes, enabling laboratory study of cosmological particle creation.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Acoustic wave equation | $\Delta \varphi_1 = \frac{1}{\sqrt{-g_0}} \partial_\mu(\sqrt{-g_0} [g_0]^{\mu\nu} \partial_\nu \varphi_1) = 0$ | Eq. (6) |
| Acoustic metric | $[g_0]_{\mu\nu} = \frac{\rho_0}{c_s} \begin{pmatrix} -(c_s^2 - v_0^2) & -\mathbf{v}_0^T \\ -\mathbf{v}_0 & \mathbf{I} \end{pmatrix}$ | Eq. (7) |
| Continuity equation | $\partial_t \rho + \nabla \cdot (\rho \mathbf{v}) = 0$ | Eq. (8) |
| Euler equation | $\rho \frac{d\mathbf{v}}{dt} = -\nabla p$ | Eqs. (9)--(10) |
| Bernoulli equation | $-\partial_t \varphi + h + \frac{1}{2}(\nabla \varphi)^2 = 0$ | Eq. (13) |
| Speed of sound | $c_s^{-2} = \partial \rho / \partial p$ | Eq. (25) |
| Densitised inverse metric | $f^{\mu\nu} = \frac{\rho_0}{c_s^2} \begin{pmatrix} -1 & -v_0^j \\ -v_0^i & c_s^2 \delta^{ij} - v_0^i v_0^j \end{pmatrix}$ | Eq. (26) |
| Covariant acoustic metric | $g_{\mu\nu} = \frac{\rho_0}{c_s} \begin{pmatrix} -(c_s^2 - v_0^2) & -v_{0j} \\ -v_{0i} & \delta_{ij} \end{pmatrix}$ | Eq. (28) |
| Acoustic interval | $ds^2 = \frac{\rho_0}{c_s}\left[ -c_s^2 dt^2 + (dx^i - v_0^i dt)\delta_{ij}(dx^j - v_0^j dt) \right]$ | Eq. (29) |
| Surface gravity (general) | $\kappa_H = \left. \frac{\partial}{\partial n}(c_s - v_\perp) \right|_{\text{horizon}}$ | Sec. 2.4.2 |
| Hawking temperature | $T_H = \frac{\hbar \kappa}{2\pi}$ | Sec. 2.4.2 |
| Multi-field densitised metric | $f^{\mu\nu}_{AB} = \frac{1}{2}\left(\frac{\partial^2 \mathcal{L}}{\partial(\partial_\mu \phi^A)\partial(\partial_\nu \phi^B)} + (A \leftrightarrow B)\right)$ | Eq. (213) |
| Gordon optical metric | $g^{\mu\nu} = \eta^{\mu\nu} + (1 - 1/n^2) V^\mu V^\nu$ | Eq. (190) |

---

## Relevance to Phonon-Exflation

This is one of the most directly relevant papers for the phonon-exflation programme. The central theorem -- that linearized fluctuations in a fluid propagate on an emergent Lorentzian geometry determined by the background state -- is the precise mathematical structure underlying the claim that particles are phononic excitations of M4 x SU(3). The acoustic metric construction shows explicitly how (3+1)-dimensional pseudo-Riemannian geometry emerges from a non-relativistic substrate, providing the template for how the exflation framework's internal SU(3) fiber dynamics could generate effective 4D gravity. The robustness of Hawking radiation against trans-Planckian modifications supports the framework's use of BCS-type microphysics at the Planck scale. The cosmological analogue metrics (Section 2.10) directly model the mechanism by which time-varying internal geometry (tau evolution) could produce cosmological particle creation (Parker-type) in the framework.
