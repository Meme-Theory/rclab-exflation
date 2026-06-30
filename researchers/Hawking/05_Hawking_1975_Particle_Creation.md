# Particle Creation by Black Holes

**Author(s):** S.W. Hawking
**Year:** 1975
**Journal:** Commun. Math. Phys. 43, 199-220 (1975)
**arXiv:** N/A (pre-arXiv)
**Relevance:** CRITICAL

---

## Abstract

[INCOMPLETE - pre-arXiv, no PDF available]

---

## Key Arguments and Derivations

[INCOMPLETE - pre-arXiv, no PDF available]

## Key Results

1. Provided the complete derivation of black hole radiation using quantum field theory on curved spacetime. A scalar field propagating on a Schwarzschild background that undergoes gravitational collapse emits a thermal flux at late times with temperature $T_H = \hbar\kappa/(2\pi)$.
2. The derivation proceeds by tracing the positive-frequency modes defined at future null infinity ($\mathscr{I}^+$) back through the collapsing geometry to past null infinity ($\mathscr{I}^-$). The resulting Bogoliubov transformation mixes positive and negative frequency modes, producing particles.
3. The Bogoliubov coefficients satisfy $|\alpha_{\omega\omega'}|^2 = e^{2\pi\omega/\kappa} |\beta_{\omega\omega'}|^2$, yielding a Planck spectrum with temperature $T = \hbar\kappa/(2\pi)$.
4. The particle number expectation value is thermal: $\langle N_\omega \rangle = \frac{\Gamma_\omega}{e^{2\pi\omega/\kappa} - 1}$ where $\Gamma_\omega$ is the greybody factor (absorption probability).
5. The radiation carries energy, causing the black hole to lose mass and eventually evaporate (for sufficiently small black holes).
6. The back-reaction problem (how the metric evolves as the black hole loses mass) was identified but not solved.
7. For fermions, the Bogoliubov coefficients give a Fermi-Dirac distribution instead of Bose-Einstein.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Bogoliubov transformation | $\phi_\omega^{\text{out}} = \int d\omega' \left(\alpha_{\omega\omega'} \phi_{\omega'}^{\text{in}} + \beta_{\omega\omega'} \bar{\phi}_{\omega'}^{\text{in}}\right)$ | Mode decomposition |
| Bogoliubov coefficient relation | $\|\alpha_{\omega\omega'}\|^2 = e^{2\pi\omega/\kappa} \|\beta_{\omega\omega'}\|^2$ | Thermal spectrum condition |
| Hawking temperature | $T_H = \frac{\hbar\kappa}{2\pi}$ | Main result |
| Planck spectrum | $\langle N_\omega \rangle = \frac{\Gamma_\omega}{e^{2\pi\omega/\kappa} - 1}$ | Particle number (bosons) |
| Fermi-Dirac spectrum | $\langle N_\omega \rangle = \frac{\Gamma_\omega}{e^{2\pi\omega/\kappa} + 1}$ | Particle number (fermions) |
| Greybody factor | $\Gamma_\omega = 1 - |R_\omega|^2$ | Absorption probability |
| Surface gravity (Schwarzschild) | $\kappa = \frac{1}{4M}$ | ($G = c = 1$ units) |

## Relevance to Phonon-Exflation

This is the foundational paper for the Bogoliubov coefficient formalism that the phonon-exflation framework uses to analyze particle creation during the tau-transit. The framework's transit IS Parker-type cosmological particle creation -- the same Bogoliubov mechanism operating without a horizon. Hawking's derivation produces a thermal spectrum because the horizon provides a universal geometric origin for mode mixing ($|\alpha|^2/|\beta|^2 = e^{2\pi\omega/\kappa}$). The framework's transit instead produces a non-thermal GGE because the Richardson-Gaudin integrability constrains the Bogoliubov coefficients beyond what a thermal ansatz allows. The Schwinger-instanton duality ($S_{\text{Schwinger}} = 0.070 \approx S_{\text{inst}} = 0.069$) established in Session 38 connects the framework's pair creation to the same WKB integral underlying Hawking's calculation.
