# Cosmological Particle Production: A Review

**Author(s):** L. H. Ford
**Year:** 2021
**Journal:** arXiv preprint (review article)
**arXiv:** 2112.02444
**Relevance:** HIGH

---

## Abstract

This article will review quantum particle creation in expanding universes. The emphasis will be on the basic physical principles and on selected applications to cosmological models. The needed formalism of quantum field theory in curved spacetime will be summarized, and applied to the example of scalar particle creation in a spatially flat universe. Estimates for the creation rate will be given and applied to inflationary cosmology models. Analog models which illustrate the same physical principles and may be experimentally realizable are also discussed.

---

## Key Arguments and Derivations

### Quantum Field Theory in Curved Spacetime

Ford reviews the framework for QFT in curved spacetime, starting from the action for a scalar field $\phi$ in a general curved background:

$$S = \int d^4x \sqrt{-g} \left[ -\frac{1}{2} g^{\mu\nu} \partial_\mu \phi \, \partial_\nu \phi - \frac{1}{2}(m^2 + \xi R)\phi^2 \right]$$

where $\xi$ is the coupling to the Ricci scalar ($\xi = 0$ for minimal coupling, $\xi = 1/6$ for conformal coupling in 4D).

### Mode Equation in FRW Spacetime

In a spatially flat FRW spacetime with $ds^2 = a^2(\eta)(-d\eta^2 + d\mathbf{x}^2)$, the rescaled field $\chi_k = a \phi_k$ satisfies:

$$\chi_k'' + \omega_k^2(\eta) \chi_k = 0$$

where the effective frequency is:

$$\omega_k^2(\eta) = k^2 + m^2 a^2 - (1 - 6\xi)\frac{a''}{a}$$

This is a parametric oscillator equation -- the time-dependence of $\omega_k$ drives particle creation.

### Bogoliubov Transformation and Particle Number

The "in" and "out" mode functions are related by:

$$f_k^{\text{out}} = \alpha_k f_k^{\text{in}} + \beta_k f_k^{\text{in}*}$$

with $|\alpha_k|^2 - |\beta_k|^2 = 1$ (bosonic normalization). The particle number in mode $k$ is:

$$N_k = |\beta_k|^2$$

The total number density of created particles is:

$$n = \frac{1}{(2\pi)^3} \int d^3k \, |\beta_k|^2$$

### Adiabatic Particle Creation Rate Estimate

For slowly varying backgrounds (adiabatic regime, $\dot{\omega}/\omega^2 \ll 1$), particle creation is exponentially suppressed:

$$|\beta_k|^2 \sim \exp\left(-\frac{\pi \omega_k^2}{\dot{\omega}_k}\right)$$

For massive particles ($m \gg H$), this gives $N_k \sim e^{-\pi m/H}$, where $H$ is the Hubble parameter.

### Sudden Transition (Non-Adiabatic Limit)

For a sudden transition where $a(\eta)$ changes abruptly, the Bogoliubov coefficients can be computed by matching mode functions across the transition. In the sudden limit:

$$|\beta_k|^2 \approx \frac{(\omega_k^{\text{in}} - \omega_k^{\text{out}})^2}{4\omega_k^{\text{in}}\omega_k^{\text{out}}}$$

### Applications to Inflation

During de Sitter inflation ($a = e^{Ht}$), massless minimally coupled scalars have a scale-invariant spectrum of fluctuations:

$$\langle |\phi_k|^2 \rangle = \frac{H^2}{2k^3}$$

Ford discusses how particle creation during and after inflation can produce the observed density perturbations, dark matter candidates, and gravitational waves.

### Analog Models

The review discusses analog models for cosmological particle creation:
- **Dynamical Casimir effect**: accelerating mirrors produce photon pairs, analogous to particle creation by an expanding universe.
- **BEC analog models**: expanding Bose-Einstein condensates can simulate cosmological expansion, with phonon creation as the analog of particle creation.
- **Superconducting circuits**: time-varying boundary conditions in microwave cavities realize the dynamical Casimir effect.

---

## Key Results

1. Particle creation in expanding universes is controlled by the Bogoliubov coefficient $|\beta_k|^2$, which measures the mismatch between "in" and "out" vacuum states.
2. The creation rate is exponentially suppressed in the adiabatic regime ($m \gg H$) and enhanced in the non-adiabatic regime (sudden transitions).
3. Conformal coupling ($\xi = 1/6$) eliminates the gravitational coupling term for massless fields, preventing particle creation in conformally flat spacetimes.
4. Inflationary particle creation produces a nearly scale-invariant spectrum of perturbations.
5. Analog models (BEC, superconducting circuits, dynamical Casimir) can experimentally test the same physics in laboratory settings.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Scalar field action | $S = \int d^4x\sqrt{-g}\left[-\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi - \frac{1}{2}(m^2+\xi R)\phi^2\right]$ | Sec. I |
| Mode equation | $\chi_k'' + \left(k^2 + m^2 a^2 - (1-6\xi)\frac{a''}{a}\right)\chi_k = 0$ | Sec. II |
| Bogoliubov transformation | $f_k^{\text{out}} = \alpha_k f_k^{\text{in}} + \beta_k f_k^{\text{in}*}$ | Sec. II |
| Normalization | $\|\alpha_k\|^2 - \|\beta_k\|^2 = 1$ | Sec. II |
| Particle number | $N_k = \|\beta_k\|^2$ | Sec. II |
| Number density | $n = (2\pi)^{-3}\int d^3k \, \|\beta_k\|^2$ | Sec. II |
| Adiabatic suppression | $\|\beta_k\|^2 \sim \exp(-\pi\omega_k^2/\dot{\omega}_k)$ | Sec. III |
| De Sitter spectrum | $\langle\|\phi_k\|^2\rangle = H^2/(2k^3)$ | Sec. IV |
| Sudden transition | $\|\beta_k\|^2 \approx (\omega^{\text{in}}_k - \omega^{\text{out}}_k)^2/(4\omega^{\text{in}}_k\omega^{\text{out}}_k)$ | Sec. III |

## Relevance to Phonon-Exflation

Ford's comprehensive review of cosmological particle creation provides the theoretical backdrop for the transit mechanism. The phonon-exflation transit IS cosmological particle creation in the internal space: the time-dependent Dirac spectrum $D_K(\tau)$ acts as the parametric oscillator equation, and the Bogoliubov coefficients determine the quasiparticle spectrum. The framework's sudden quench ($P_{\text{exc}} = 1.000$, 59.8 pairs created) sits firmly in the non-adiabatic limit Ford describes. The analog model discussion is directly relevant: the BCS condensate on $SU(3)$ IS an analog model, with Cooper pair creation as the analog of cosmological particle creation, and the instanton gas providing the time-dependent "metric" of the internal space.
