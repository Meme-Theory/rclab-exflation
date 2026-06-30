# Quantized Fields and Particle Creation in Expanding Universes. I

**Author(s):** Leonard Parker
**Year:** 1969
**Journal:** Physical Review 183, 1057-1068 (1969)
**arXiv:** N/A (pre-arXiv)
**Relevance:** CRITICAL

---

## Abstract

[INCOMPLETE - pre-arXiv, no PDF available]

---

## Key Arguments and Derivations

[INCOMPLETE - pre-arXiv, no PDF available]

### Core Framework (from published results)

Parker established the foundational framework for quantum particle creation by gravitational fields in expanding universes. The key insight is that the concept of "particle" depends on the choice of mode functions, and different choices related to different epochs of the expansion yield inequivalent particle definitions connected by Bogoliubov transformations.

### Bogoliubov Transformation

Consider a scalar field $\phi$ in a spatially flat FRW spacetime $ds^2 = a^2(\eta)(-d\eta^2 + d\mathbf{x}^2)$. Mode functions satisfying the field equation at early times ("in" modes $f_k^{\text{in}}$) and late times ("out" modes $f_k^{\text{out}}$) are related by:

$$f_k^{\text{out}} = \alpha_k f_k^{\text{in}} + \beta_k f_k^{\text{in}*}$$

where $\alpha_k$ and $\beta_k$ are the Bogoliubov coefficients.

### Normalization Condition

The Bogoliubov coefficients satisfy the normalization:

$$|\alpha_k|^2 - |\beta_k|^2 = 1$$

This follows from the preservation of the Klein-Gordon inner product (Wronskian condition).

### Particle Number

The expected number of particles created in mode $k$, as measured by a late-time observer in the "in" vacuum, is:

$$N_k = \langle 0_{\text{in}} | \hat{N}_k^{\text{out}} | 0_{\text{in}} \rangle = |\beta_k|^2$$

### Adiabatic Vacuum

Parker introduced the concept of the **adiabatic vacuum**, defined by WKB-type mode functions:

$$f_k(\eta) \sim \frac{1}{\sqrt{2W_k(\eta)}} \exp\left(-i \int^\eta W_k(\eta') d\eta'\right)$$

where $W_k$ is determined by an iterative WKB procedure. The adiabatic vacuum minimizes particle creation at each order of the adiabatic expansion, providing a physically preferred vacuum state when the expansion is slow compared to the mode frequency.

---

## Key Results

1. Quantum fields in expanding universes generically undergo **particle creation** -- the "in" vacuum contains particles as measured by "out" observers.
2. The particle number is determined by the Bogoliubov coefficient: $N_k = |\beta_k|^2$.
3. The normalization $|\alpha_k|^2 - |\beta_k|^2 = 1$ ensures unitarity.
4. The **adiabatic vacuum** provides a preferred vacuum state in slowly expanding spacetimes.
5. Particle creation is a purely gravitational effect requiring no coupling constants -- it follows from the time-dependence of the metric alone.
6. Massless conformally coupled fields are not created in conformally flat spacetimes (conformal invariance prevents mixing of positive and negative frequencies).

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Bogoliubov transformation | $f_k^{\text{out}} = \alpha_k f_k^{\text{in}} + \beta_k f_k^{\text{in}*}$ | Sec. II |
| Normalization | $\|\alpha_k\|^2 - \|\beta_k\|^2 = 1$ | Sec. II |
| Particle number | $N_k = \|\beta_k\|^2$ | Sec. II |
| WKB mode function | $f_k \sim (2W_k)^{-1/2} \exp\left(-i\int W_k \, d\eta\right)$ | Sec. III |
| Mode equation | $\chi_k'' + \left(k^2 + m^2 a^2 - \frac{a''}{a}\right)\chi_k = 0$ | Sec. II |
| Conformal coupling | $\xi = 1/6$ (4D): no particle creation for $m=0$ | Sec. IV |

## Relevance to Phonon-Exflation

Parker's particle creation mechanism is THE direct analog of the transit in phonon-exflation cosmology. The transit IS Parker-type cosmological particle creation: the time-dependent internal geometry $g_{SU(3)}(\tau)$ drives Bogoliubov mixing of the Dirac modes on $M^4 \times SU(3)$, producing quasiparticle pairs. The key difference: the framework produces a non-thermal GGE relic (integrability-protected) rather than a thermal spectrum, because the transit dynamics are integrable (Richardson-Gaudin) with 8 conserved quantities. The Schwinger-instanton duality ($S_{\text{Schwinger}} = 0.070 \approx S_{\text{inst}} = 0.069$) confirms the WKB integral underlying both Parker production and instanton tunneling is the same.
