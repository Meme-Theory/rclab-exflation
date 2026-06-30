# Analogue Gravity

**Author(s):** Carlos Barcelo, Stefano Liberati, Matt Visser
**Year:** 2005 (major revision 2024)
**Journal:** Living Reviews in Relativity
**arXiv:** gr-qc/0505065
**Relevance:** CRITICAL

---

## Abstract

Analogue gravity is a research programme that explores analogues of general relativistic gravitational fields within other physical systems, particularly but not exclusively in condensed matter systems, with the aim of gaining new insights into related problems. Analogue models of gravity boast a long and distinguished history, dating back to the early years of general relativity. This review article delves into the history, aims, results, and future prospects of various analogue models. We begin by presenting a particularly simple example of an analogue model, then traverse the rich history and complex array of models discussed in the literature. The last decade has witnessed significant and sustained advances in analogue gravity, resulting in hundreds of published articles, workshops, and books. The future of the analogue gravity programme looks promising, with rapid technological advances on the experimental front and the potential for analogue models to inspire innovative approaches to the problem of quantum gravity on the theoretical front. Most of all, these recent years have seen the rise of an unprecedented collaboration and interplay between different communities that we believe will set a new standard for interdisciplinary research in the years to come.

---

## Key Arguments and Derivations

### Section 2: Acoustics as the Simplest Analogue Spacetime

The central result of the review is the derivation that sound waves in a moving fluid propagate as though governed by a curved Lorentzian spacetime metric. The derivation proceeds at two levels:

**Geometrical acoustics:** Assuming only a well-defined speed of sound $c_s$ relative to the fluid and a well-defined fluid velocity $\mathbf{v}$, the sound cone condition $-c_s^2 dt^2 + (d\mathbf{x} - \mathbf{v}\,dt)^2 = 0$ defines a conformal class of Lorentzian metrics.

**Physical acoustics (Theorem 1):** For a barotropic, inviscid fluid with irrotational (but possibly time-dependent) flow, the linearized perturbation $\phi_1$ of the velocity potential satisfies $\Delta\phi_1 = 0$, where $\Delta$ is the d'Alembertian of a (3+1)-dimensional Lorentzian geometry specified by the acoustic metric. The proof proceeds by: (1) linearizing the continuity equation and Euler equation around background $(p_0, \rho_0, \phi_0)$; (2) combining the linearized equations to obtain a single wave equation for $\phi_1$; (3) identifying the resulting PDE with the covariant wave equation $\partial_\mu(\sqrt{-g}\,g^{\mu\nu}\partial_\nu \phi_1) = 0$ by matching the tensor density $f^{\mu\nu} = \sqrt{-g}\,g^{\mu\nu}$; (4) computing $\det(f^{\mu\nu}) = -\rho_0^4/c_s^2$ to extract the metric.

The acoustic metric is:
$$g_{\mu\nu} = \frac{\rho_0}{c_s}\begin{pmatrix} -(c_s^2 - v_0^2) & -\mathbf{v}_0^T \\ -\mathbf{v}_0 & \mathbf{I} \end{pmatrix}$$

Key properties: (a) Lorentzian signature $(-,+,+,+)$; (b) two distinct metrics exist -- the flat physical Minkowski metric seen by the fluid particles and the curved acoustic metric seen by phonons; (c) topology inherited from physical space; (d) stable causality inherited from Newtonian time; (e) at most 3 degrees of freedom per spacetime point (vs. 6 for general Lorentzian geometry), reduced to 2 by continuity.

### Horizons, Ergo-regions, and Surface Gravity (Section 2.4)

**Ergo-region:** The norm $g_{\mu\nu}(\partial/\partial t)^\mu(\partial/\partial t)^\nu = -[c_s^2 - v^2]$ changes sign when $\|\mathbf{v}\| > c_s$, so any region of supersonic flow is an ergo-region.

**Trapped surfaces:** Defined by closed 2-surfaces where the inward-pointing normal component of fluid velocity exceeds $c_s$ everywhere. The acoustic apparent horizon is the surface where the normal component equals $c_s$.

**Event horizon:** The boundary of the region from which null geodesics (phonons) cannot escape to infinity.

**Surface gravity** for static acoustic spacetimes:
$$g_H = \frac{1}{2}\frac{\partial(c_s^2 - v^2)}{\partial n}\bigg|_H = c_s\bigg|_H \frac{\partial|c_s - v|}{\partial n}\bigg|_H$$

This generalizes Unruh's original result to position-dependent speed of sound. The Hawking temperature is:
$$kT_H = \frac{\hbar g_H}{2\pi c_H}$$

For the general stationary (non-static) case, the surface gravity is computed via the horizon-generating null vector field $L^\mu = (1; v_\parallel^i)$ and the standard Killing horizon definition, yielding the same formula.

### Cosmological Metrics (Section 2.10)

Two routes to analogue FRW cosmologies:

**Explosion route:** Using a homogeneous system with radial velocity profile $\mathbf{v} = (\dot{b}/b)\mathbf{r}$ and a comoving coordinate $r_b = r/b$, the acoustic metric becomes a spatially flat FLRW geometry $ds^2 = -\mathcal{T}^2(t)\,dt^2 + a_s^2(t)(dr_b^2 + r_b^2 d\Omega^2)$ with $\mathcal{T} = \sqrt{\rho}\,c_s$ and $a_s = \sqrt{\rho/c_s}\,b$.

**Varying speed of sound route:** With the fluid at rest ($\mathbf{v}=0$), $\rho$ spatially constant, and $c_s$ time-varying, one obtains $ds^2 = -\rho c_s\,dt^2 + (\rho/c_s)\,d\mathbf{x}^2$. Introducing $a_s = \sqrt{\rho/c_s}$, this is FRW with expanding universe corresponding to decreasing $c_s$. De Sitter expansion requires $a_s(\tau) = a_0 e^{H_0\tau}$.

### BEC as Analogue Gravity (Section 4.2.1)

Starting from the Gross-Pitaevskii equation for a BEC:
$$i\hbar\frac{\partial}{\partial t}\hat{\Psi} = \left(-\frac{\hbar^2}{2m}\nabla^2 + V_{\mathrm{ext}} + \kappa(a)\hat{\Psi}^\dagger\hat{\Psi}\right)\hat{\Psi}$$

with $\kappa(a) = 4\pi a\hbar^2/m$, and using the Madelung representation $\psi = \sqrt{n_c}\,e^{-i\theta/\hbar}$ with $\mathbf{v} = \nabla\theta/m$, the GP equation reduces to a continuity equation plus an Euler equation with quantum potential $V_{\mathrm{quantum}} = -(\hbar^2/2m)(\nabla^2\sqrt{n_c}/\sqrt{n_c})$. In the hydrodynamic (long-wavelength) approximation where the quantum potential is negligible, the fluctuations of the phase $\hat{\theta}_1$ obey the curved-space d'Alembertian equation with effective metric identical in form to the acoustic metric, but with speed of sound $c_s^2 = \kappa(a)n_c/m$.

At shorter wavelengths (comparable to the healing length $\hbar/mc_s$), the Bogoliubov dispersion relation $\omega^2 = c_s^2 k^2 + (\hbar k^2/2m)^2$ introduces Lorentz-violating corrections -- this is the trans-Planckian regime of the analogue model.

### Hawking Radiation (Section 5.1)

The review establishes that Hawking radiation is a kinematic effect depending only on: (1) the existence of an effective Lorentzian geometry with an event horizon; (2) the quantum nature of the field propagating in that geometry. It does not depend on the Einstein equations. The trans-Planckian problem -- that traced-back outgoing modes had arbitrarily high frequencies -- is addressed by analogue models showing that modified (subluminal or superluminal) dispersion relations preserve the thermal Hawking spectrum under broad conditions, making the effect robust against UV physics.

### Cosmological Particle Production (Section 5.4)

In BEC-based FRW analogues, cosmological pair production of phonons occurs when the background (effective metric) changes with time. The theory predicts particle production with spectra sensitive to the expansion history. Experimental verification was reported by Steinhauer et al. (2022) using a quenched 3D quantum fluid of light.

### The Cosmological Constant Problem (Section 7.10)

In analogue gravity, the zero-point energy of phonons ($\sim E_P^4$) vastly exceeds the actual vacuum energy. However, liquid systems (as opposed to gases) can remain stable on their own without external pressure. At zero temperature, the total vacuum energy $\Lambda \propto \rho_V = -p_V$ is forced to be relatively small. The $E_P^4$ contribution from quasiparticle fluctuations is exactly balanced by "trans-Planckian" microphysics contributions. At nonzero temperature, the vacuum energy $\Lambda \propto p_M$ (pressure of the thermal quasiparticle "matter"), matching the order of magnitude of the observed cosmological constant.

### Emergent Gravity and Einstein Equations (Section 7)

The review discusses: (a) the Weinberg-Witten theorem and how analogue models evade it (the effective graviton is not a Lorentz-covariant massless spin-2 particle at the microscopic level); (b) diffeomorphism invariance as an emergent low-energy symmetry; (c) possible routes from analogue models to Einstein equations via Sakharov's induced gravity or Jacobson's thermodynamic derivation; (d) the information loss problem, where analogue models demonstrate that information is preserved in the full microscopic theory even when it appears lost in the effective low-energy (semiclassical) description.

---

## Key Results

1. Sound waves in a barotropic, inviscid, irrotational fluid propagate according to a (3+1)-dimensional curved Lorentzian spacetime metric determined algebraically by the fluid density, velocity, and local speed of sound (Theorem 1).
2. Supersonic flow regions define ergo-regions; trapped surfaces and event horizons are defined in direct analogy with general relativity.
3. The surface gravity of an acoustic horizon is $g_H = \frac{1}{2}\partial_n(c_s^2 - v_\perp^2)|_H$, generalizing Unruh's result.
4. Hawking radiation is a kinematic effect robust against trans-Planckian modifications of the dispersion relation.
5. FRW cosmologies can be mimicked either by explosive expansion or by time-varying speed of sound in a static medium; decreasing $c_s$ corresponds to expanding space.
6. BECs provide an ideal analogue system: the Gross-Pitaevskii equation yields an acoustic metric for phonons, with the healing length providing a natural trans-Planckian scale.
7. The cosmological constant problem has a natural resolution in liquid-like analogue systems: equilibrium vacuum energy is zero (or order $p_M$), regardless of the UV cutoff.
8. Cosmological particle production in expanding BECs is predicted and has been experimentally observed.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Sound cone | $-c_s^2\,dt^2 + (d\mathbf{x} - \mathbf{v}\,dt)^2 = 0$ | Eq. (2) |
| Conformal metric class | $g = \Omega^2\begin{pmatrix} -(c_s^2 - v^2) & -\mathbf{v}^T \\ -\mathbf{v} & \mathbf{I}\end{pmatrix}$ | Eq. (4) |
| Acoustic wave equation | $\partial_\mu(f^{\mu\nu}\partial_\nu\phi_1) = 0$ | Eq. (27) |
| Inverse metric density | $f^{\mu\nu} = \sqrt{-g}\,g^{\mu\nu}$ | Eq. (29) |
| Metric determinant | $g = -\rho_0^4/c_s^2$; $\sqrt{-g} = \rho_0^2/c_s$ | Eq. (32) |
| Acoustic metric (covariant) | $g_{\mu\nu} = \frac{\rho_0}{c_s}\begin{pmatrix} -(c_s^2 - v_0^2) & -v_0^j \\ -v_0^i & \delta_{ij}\end{pmatrix}$ | Eq. (34) |
| Acoustic line element | $ds^2 = \frac{\rho_0}{c_s}[-c_s^2\,dt^2 + (\delta_{ij})(dx^i - v_0^i\,dt)(dx^j - v_0^j\,dt)]$ | Eq. (35) |
| Ergo-region condition | $g_{tt} = -(c_s^2 - v^2)$; changes sign when $\|v\| > c_s$ | Eq. (48) |
| Surface gravity (static) | $g_H = \frac{1}{2}\frac{\partial(c_s^2 - v^2)}{\partial n}\bigg\|_H$ | Eq. (65) |
| Hawking temperature | $kT_H = \frac{\hbar g_H}{2\pi c_H}$ | Eq. (67) |
| FRW from explosion | $ds^2 = -\mathcal{T}^2(t)\,dt^2 + a_s^2(t)(dr_b^2 + r_b^2\,d\Omega^2)$ | Eq. (114) |
| FRW from varying $c_s$ | $ds^2 = -c_0 c_s(t)\,dt^2 + \frac{c_0}{c_s(t)}\,d\mathbf{x}^2$ | Eq. (122)/(124) |
| GP equation | $i\hbar\partial_t\hat{\Psi} = (-\frac{\hbar^2}{2m}\nabla^2 + V_{\mathrm{ext}} + \kappa\hat{\Psi}^\dagger\hat{\Psi})\hat{\Psi}$ | Eq. (233) |
| BEC speed of sound | $c_s^2 = \kappa(a)n_c/m$ | Eq. (263) |
| Quantum potential | $V_{\mathrm{quantum}} = -\frac{\hbar^2}{2m}\frac{\nabla^2\sqrt{n_c}}{\sqrt{n_c}}$ | Eq. (244) |
| Bogoliubov dispersion | $\omega^2 = c_s^2 k^2 + (\hbar k^2/2m)^2$ | Eq. (277) |
| Phonon vacuum energy | $\epsilon_{\mathrm{eff}} = \frac{1}{16\pi^2}\frac{\Theta^4}{\hbar^3 c^3}$ | Eq. (24) in Volovik sense |
| CC equilibrium condition | $\tilde{\epsilon}_{\mathrm{vac}} = -P_{\mathrm{vac}}$ | Sec. 7.10 |

---

## Relevance to Phonon-Exflation

This is the foundational reference for the entire analogue gravity programme and directly underpins the phonon-exflation framework. The acoustic metric formalism (Theorem 1) provides the mathematical backbone: phononic excitations of a substrate propagate on a curved Lorentzian geometry determined by the substrate's density, flow, and speed of sound. The FRW cosmology construction via time-varying $c_s$ (Section 2.10.2) maps directly onto the exflation mechanism: internal compactification of the SU(3) fiber changes the effective phonon propagation speed, generating an expanding effective spacetime. The BEC section establishes that the Gross-Pitaevskii/Madelung formalism -- which underlies the project's GPE solver -- produces an exact acoustic metric for phonon fluctuations. The cosmological constant discussion (Section 7.10) resonates with the framework's q-theory CC redirect: in liquid-like vacua, the vacuum energy is forced to be zero or of order the matter content, resolving the 120-order-of-magnitude discrepancy. The trans-Planckian robustness of Hawking radiation validates the framework's use of BCS instanton physics in regimes where the lattice-scale (healing length) physics is non-Lorentzian.
