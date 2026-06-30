# Phonon-Assisted Casimir Interactions between Piezoelectric Materials

**Author(s):** Dai-Nam Le, Pablo Rodriguez-Lopez, Lilia M. Woods
**Year:** 2024
**Journal:** arXiv preprint
**arXiv:** 2408.13368
**Relevance:** HIGH

---

## Abstract

The strong coupling between electromagnetic field and lattice oscillation in piezoelectric materials gives rise to phonon polariton excitations. Such quasiparticles open up new directions in modulating the ubiquitous Casimir force. Here by utilizing the generalized Born-Huang hydrodynamics model, three types of phonons in piezoelectrics are studied: longitudinal optical phonon, transverse optical phonon and phonon polariton. The phonon-electromagnetic coupling results in a complex set of Fresnel reflection matrices which prevents the utilization of the standard Lifshitz approach for calculating Casimir forces in the imaginary frequency domain. Our calculations are based on an approach within real frequency and finite temperatures, through which various regimes of the Casimir interaction are examined. Our study shows that piezoelectrics emerge as a set of materials where this ubiquitous force can be controlled via phonon properties for the first time. The Casimir interaction appears as a suitable means to distinguish between different types of surface phonon polaritons associated with different structural piezoelectric polytypes.

---

## Key Arguments and Derivations

### 1. Introduction

The Casimir force arises from electromagnetic fluctuations between objects separated by a gap. While the force depends strongly on material optical response (electronic structure), phonons are rarely considered in Casimir physics because weak phonon-photon coupling makes phonon participation negligible at separations exceeding the phonon mean free path. However, in polar/piezoelectric materials, hybridization between transverse optical phonon modes and photon excitations produces tunable phonon polariton resonances that can significantly affect the Casimir energy.

Piezoelectrics feature strong coupling between the macroscopic electric field $\mathbf{E}$ and mechanical deformation $\mathbf{u}$ induced by phonons, creating surface phonon polaritons (PhPs) that open additional channels of fluctuation-induced interactions.

### 2. Born-Huang Hydrodynamics Model

The generalized Born-Huang model governs the time evolution of the ionic mechanical displacement $\mathbf{u}$ as a driven harmonic oscillator:

$$\rho_i \left(\frac{\partial^2}{\partial t^2} + \gamma \frac{\partial}{\partial t} + \omega_{TO}^2\right) \mathbf{u} = e_i \mathbf{E} + \rho_i \left[\beta_{TO}^2 \nabla \times (\nabla \times \mathbf{u}) - \beta_{LO}^2 \nabla(\nabla \cdot \mathbf{u})\right]$$

where $\rho_i$, $e_i$ are ionic mass and charge densities, $\gamma$ is damping, $\beta_{TO}$, $\beta_{LO}$ are TO and LO phonon speeds, and $\omega_{TO}$ is the zone-center TO frequency. The Lyddane-Sachs-Teller relation $\omega_{LO}^2 - \omega_{TO}^2 = e_i^2/(\varepsilon_\infty \varepsilon_0 \rho_i)$ connects LO and TO frequencies.

The model distinguishes three phonon mode types:
- **LO phonons**: $\nabla \times \mathbf{u}_{LO} = 0$, dispersion $\omega^2 = \omega_{LO}^2 - \beta_{LO}^2 q^2$
- **TO phonons**: $\nabla \cdot \mathbf{u}_{TO} = 0$, purely mechanical (no EM field), dispersion $\omega^2 = \omega_{TO}^2 - \beta_{TO}^2 q^2$
- **PhP modes**: $\nabla \cdot \mathbf{u}_{PhP} = 0$, surface-confined, dispersion $\omega^2 = q^2 c^2 / \varepsilon_{PhP}(\omega, q)$

### 3. PhP Dielectric Function

The nonlocal PhP dielectric function from the Born-Huang model is:

$$\frac{\varepsilon_{PhP}(\omega)}{\varepsilon_\infty} \approx \frac{\omega_{LO}^2 - \omega(\omega + i\gamma) - \frac{\varepsilon_\infty \omega^2 \beta_{TO}^2}{c^2} \frac{\omega_{LO}^2 - \omega(\omega+i\gamma)}{\omega_{TO}^2 - \omega(\omega+i\gamma)}}{\omega_{TO}^2 - \omega(\omega + i\gamma) - \frac{\varepsilon_\infty \omega^2 \beta_{TO}^2}{c^2} \frac{\omega_{LO}^2 - \omega(\omega+i\gamma)}{\omega_{TO}^2 - \omega(\omega+i\gamma)}}$$

### 4. Surface PhP and Fresnel Coefficients

The coupled electromagnetic-elastic boundary conditions produce a surface PhP (SPhP) mode contribution:

$$\Omega(q_\parallel, \omega) = \frac{q_\parallel^2 (q_{PhP,z} - q_{TO,z})}{q_\parallel^2 + q_{TO,z} q_{LO,z}} (\varepsilon_{PhP}(\omega) - \varepsilon_\infty)$$

This affects only p-polarized modes. For SiC polytypes (4H, 6H, etc.), zone folding of LO phonon dispersions creates additional Bragg peaks, producing hybrid longitudinal-transverse SPhPs (LT-SPhPs) with mixed polarization.

### 5. Real-Frequency Casimir Formalism

The reflection coefficient $r_{pp}(q_\parallel, i\xi)$ is complex-valued for piezoelectrics, preventing standard Lifshitz (imaginary frequency) calculations. The authors use Rytov's real-frequency approach:

$$P(D,T) = \sum_{\alpha=s,p} \left[P_\alpha^{\text{prop}}(D,T) + P_\alpha^{\text{evan}}(D,T)\right]$$

with propagating and evanescent contributions integrated over real frequencies weighted by $\eta(\omega, T) = \coth(\hbar\omega / 2k_BT)$.

### 6. Semi-Infinite Plates

For semi-infinite SiC plates at $T = 0$, $P_s$ and $P_p$ follow $1/D^4$ scaling with a transition region at separations comparable to phonon wavelengths $\lambda_{TO} = c/\omega_{TO} \approx 2\,\mu\text{m}$ and $\lambda_{LO} \approx 1.6\,\mu\text{m}$. SPhPs and LT-SPhPs give identical Casimir interaction at small separations but differ at sub-micron and larger distances.

At finite temperature ($T = 100\,$K), a $1/D^4 \to 1/D^3$ transition signals onset of thermal fluctuations at separations comparable to $\lambda_{th} = \hbar c / k_B T$.

### 7. Finite Thickness Plates

For plates of thickness $L$ with separations $D \gg L$:
- **SPhP plates**: $P \sim 1/D^6$ (plates behave as dielectrics), analytically:
$$P(D \gg L) \approx -\frac{(\varepsilon_{st}-1)^2(9\varepsilon_{st}^2 + 10\varepsilon_{st} + 4) L^2 \hbar c}{32\pi^2 \varepsilon_{st}^2 D^6}$$
- **LT-SPhP plates**: $P \sim 1/D^4$ with resonant-like features controlled by $R(L) \propto \cot^2(q_{LO}L/2)$. Attractive resonances at $\cot(q_{LO}L/2) = 0$; repulsive resonances at specific cotangent values. The confined LO phonon in the cavity produces trapped LT-SPhP excitations.

At $T > 0$, scaling transitions shift: $1/D^6 \to 1/D^5$ for SPhPs and $1/D^4 \to 1/D^3$ for LT-SPhPs.

### 8. Role of Graphene Coating

Graphene layers covering the piezoelectric surfaces cause near-complete reflection of low-frequency p-modes, diminishing SPhP/LT-SPhP effects at separations $D > \lambda_{th}$ and pushing the quantum-to-thermal transition to smaller distances. At small separations ($D \lesssim L$), graphene has minimal effect.

---

## Key Results

1. Piezoelectric materials exhibit phonon-modulated Casimir interactions via surface phonon polaritons, demonstrated for the first time.
2. Three phonon types (LO, TO, PhP) are captured by the generalized Born-Huang hydrodynamic model.
3. The complex nature of Fresnel reflection coefficients necessitates real-frequency (not imaginary Matsubara) Casimir calculations.
4. SPhP vs LT-SPhP modes produce qualitatively different Casimir scaling laws at large separations ($1/D^6$ vs $1/D^4$ for finite plates).
5. LT-SPhP modes produce resonant-like Casimir force features (including repulsion) controlled by plate thickness via $\cot(q_{LO}L/2)$.
6. The Casimir force can distinguish between different SiC polytypes through their distinct phonon polariton modes.
7. Casimir pressures of $10^{-8}$ to $10^{-3}\,$mPa are predicted for separations under 10 microns, within experimental reach (CANNEX experiment).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Born-Huang equation | $\rho_i(\partial_t^2 + \gamma\partial_t + \omega_{TO}^2)\mathbf{u} = e_i\mathbf{E} + \rho_i[\beta_{TO}^2\nabla\times(\nabla\times\mathbf{u}) - \beta_{LO}^2\nabla(\nabla\cdot\mathbf{u})]$ | Eq. (1) |
| Fresnel $r_{pp}$ (semi-inf.) | $r_{pp} = \frac{\varepsilon_{PhP}q_z - (q_{PhP,z} + \Omega) + \mu_0 c\sigma_s \frac{q_z c}{\omega}(q_{PhP,z}+\Omega)}{\varepsilon_{PhP}q_z + (q_{PhP,z} + \Omega) + \mu_0 c\sigma_s \frac{q_z c}{\omega}(q_{PhP,z}+\Omega)}$ | Eq. (4) |
| SPhP coupling | $\Omega(q_\parallel, \omega) = \frac{q_\parallel^2(q_{PhP,z} - q_{TO,z})}{q_\parallel^2 + q_{TO,z}q_{LO,z}}(\varepsilon_{PhP} - \varepsilon_\infty)$ | Eq. (5) |
| PhP dielectric function | $\varepsilon_{PhP}/\varepsilon_\infty \approx \frac{\omega_{LO}^2 - \omega(\omega+i\gamma) - \varepsilon_\infty\omega^2\beta_{TO}^2[\omega_{LO}^2-\omega(\omega+i\gamma)]/[c^2(\omega_{TO}^2-\omega(\omega+i\gamma))]}{\omega_{TO}^2 - \omega(\omega+i\gamma) - \varepsilon_\infty\omega^2\beta_{TO}^2[\omega_{LO}^2-\omega(\omega+i\gamma)]/[c^2(\omega_{TO}^2-\omega(\omega+i\gamma))]}$ | Eq. (6) |
| Casimir pressure (real freq.) | $P(D,T) = \sum_\alpha [P_\alpha^{\text{prop}}(D,T) + P_\alpha^{\text{evan}}(D,T)]$ | Eq. (7) |
| Propagating contribution | $P_\alpha^{\text{prop}} = \frac{\hbar}{4\pi^3}\text{Re}\int_0^\infty d\omega\,\eta(\omega,T)\int_{q<\omega/c} d^2q_\parallel\, q_z \frac{r_{\alpha\alpha}^{(1)}r_{\alpha\alpha}^{(2)}e^{2iq_zD}}{1 - r_{\alpha\alpha}^{(1)}r_{\alpha\alpha}^{(2)}e^{2iq_zD}}$ | Eq. (8) |
| Matsubara form | $P_\alpha = -\frac{k_BT}{2\pi^2}\text{Re}\sum_{n=0}^{\prime\infty}\int_0^\infty d^2q_\parallel\,\kappa_z\frac{r_{\alpha\alpha}^{(1)}r_{\alpha\alpha}^{(2)}e^{-2\kappa_zD}}{1 - r_{\alpha\alpha}^{(1)}r_{\alpha\alpha}^{(2)}e^{-2\kappa_zD}}$ | Eq. (10) |
| SPhP asymptotic ($D\gg L$) | $P \approx -\frac{(\varepsilon_{st}-1)^2(9\varepsilon_{st}^2+10\varepsilon_{st}+4)L^2\hbar c}{32\pi^2\varepsilon_{st}^2 D^6}$ | Eq. (11) |
| LT-SPhP asymptotic | $P(D\gg L) \approx -\frac{\pi^2\hbar c}{240 D^4}R(L)$ | Eq. (12) |
| Resonance factor | $R(L) = \left[\frac{1 - (\frac{\pi\varepsilon_{st}q_{LO}}{2(\varepsilon_{st}-\varepsilon_\infty)q_{1,2}})^2\cot^2(q_{LO}L/2)}{(1 + (\frac{\pi\varepsilon_{st}q_{LO}}{2(\varepsilon_{st}-\varepsilon_\infty)q_{1,2}})^2\cot^2(q_{LO}L/2))}\right]^2$ | Eq. (13) |
| LO-TO relation | $\omega_{LO}^2 - \omega_{TO}^2 = e_i^2/(\varepsilon_\infty\varepsilon_0\rho_i)$ | Sec. II |

---

## Relevance to Phonon-Exflation

This paper demonstrates that phonons can directly modulate vacuum fluctuation forces (Casimir effect) through phonon polariton coupling in piezoelectric materials. For the phonon-exflation framework, this establishes a concrete physical mechanism by which phononic excitations on a structured substrate couple to electromagnetic vacuum modes and modify the effective vacuum energy. The resonant cavity behavior controlled by plate thickness $L$ via $\cot(q_{LO}L/2)$ provides a direct analog for how the compactification radius of the SU(3) fiber (playing the role of $L$) could modulate vacuum energy contributions. The distinction between SPhP ($1/D^6$) and LT-SPhP ($1/D^4$) scaling laws demonstrates that the polarization structure of phonon modes matters for vacuum energy, paralleling the framework's finding that vector (vs scalar) excitations on the internal space produce qualitatively different spectral action contributions.
