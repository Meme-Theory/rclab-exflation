# Planck 2015 Results. XIII. Cosmological Parameters

**Authors**: Planck Collaboration (Ade P.A.R. et al.)
**Year**: 2015 (published 2016)
**Journal**: Astronomy & Astrophysics, vol. 594, A13
**arXiv**: 1502.01589
**DOI**: 10.1051/0004-6361/201525830
**Source**: https://arxiv.org/abs/1502.01589

---

## Abstract

The Planck Collaboration presents results based on full-mission Planck observations of
temperature and polarization anisotropies of the cosmic microwave background (CMB) radiation.
These data are consistent with the six-parameter inflationary LCDM cosmology. From the Planck
temperature and lensing data, for this cosmology they find a Hubble constant
$H_0 = (67.8 \pm 0.9)$ km/s/Mpc, a matter density parameter $\Omega_m = 0.308 \pm 0.012$,
and a scalar spectral index $n_s = 0.968 \pm 0.006$. Additional constraints include the
reionization optical depth $\tau = 0.066 \pm 0.016$, spatial curvature $|\Omega_K| < 0.005$,
dark energy equation of state $w = -1.006 \pm 0.045$, and the sum of neutrino masses
$\sum m_\nu < 0.23$ eV.

---

## Historical Context

The Planck satellite, launched by the European Space Agency in 2009, provided the most precise
all-sky map of the CMB ever obtained. The CMB is the relic radiation from the early universe,
emitted approximately 380,000 years after the Big Bang when the universe cooled enough for
neutral hydrogen to form (recombination).

The Planck 2015 data release represented the most comprehensive analysis of CMB temperature
and polarization anisotropies, delivering the tightest constraints on cosmological parameters.
This paper became the benchmark reference for the standard cosmological model (LCDM).

Paasch's Paper 03 cites this paper as [4] for the mass and age of the observable universe,
which he uses to validate his exponential model predictions for $m_U$ and $t_0$.

---

## Key Arguments and Derivations

### The Six-Parameter LCDM Model

The standard cosmological model fits the CMB power spectrum with just six free parameters:

1. **$\Omega_b h^2$** = baryon density = $0.02225 \pm 0.00016$
2. **$\Omega_c h^2$** = cold dark matter density = $0.1198 \pm 0.0015$
3. **$\tau$** = optical depth to reionization = $0.066 \pm 0.016$
4. **$n_s$** = scalar spectral index = $0.968 \pm 0.006$
5. **$\ln(10^{10} A_s)$** = amplitude of primordial perturbations = $3.064 \pm 0.023$
6. **$H_0$** = Hubble constant = $(67.8 \pm 0.9)$ km/s/Mpc
   (equivalently, $100\theta_{MC}$ = angular scale of sound horizon)

From these six parameters, all other cosmological quantities are DERIVED:

### Derived Cosmological Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| $\Omega_m$ | $0.308 \pm 0.012$ | Total matter density |
| $\Omega_\Lambda$ | $0.692 \pm 0.012$ | Dark energy density |
| $\Omega_b$ | $0.0484 \pm 0.0010$ | Baryon density |
| $\sigma_8$ | $0.815 \pm 0.009$ | RMS matter fluctuations at 8 Mpc/h |
| $t_0$ | $13.799 \pm 0.021$ Gyr | Age of the universe |
| $z_{re}$ | $8.8_{-1.2}^{+1.7}$ | Redshift of reionization |
| $r$ | $< 0.11$ | Tensor-to-scalar ratio (95% CL) |

### The CMB Power Spectrum

The CMB temperature anisotropies are characterized by the angular power spectrum $C_\ell$,
which shows a series of acoustic peaks:

$$C_\ell^{TT} = \frac{2\pi}{l(l+1)} \left\langle |a_{lm}|^2 \right\rangle$$

where $a_{lm}$ are the spherical harmonic coefficients of the temperature map:

$$\frac{\Delta T}{T}(\theta, \phi) = \sum_{l,m} a_{lm} Y_{lm}(\theta, \phi)$$

The positions and heights of the acoustic peaks encode:
- **Peak positions**: Sound horizon at recombination (depends on $\Omega_b$, $\Omega_m$, $H_0$)
- **Peak heights**: Baryon loading (ratio $\Omega_b/\Omega_\gamma$)
- **Peak damping**: Silk damping from photon diffusion
- **Low-$\ell$ plateau**: Sachs-Wolfe effect (gravitational redshift)

### Key Physical Quantities

**Age of the universe:**
$$t_0 = 13.799 \pm 0.021 \text{ Gyr} = (4.354 \pm 0.007) \times 10^{17} \text{ s}$$

**Mass of the observable universe** (derived from $\Omega_m$ and $H_0$):
$$M_U = \frac{4}{3}\pi R_H^3 \rho_c \Omega_m \approx 4.5 \times 10^{53} \text{ kg}$$

where $\rho_c = 3H_0^2/(8\pi G)$ is the critical density and $R_H = c/H_0$ is the Hubble
radius.

**Hubble time:**
$$t_H = 1/H_0 = 14.4 \text{ Gyr}$$

**Critical density:**
$$\rho_c = \frac{3H_0^2}{8\pi G} = 8.62 \times 10^{-27} \text{ kg/m}^3$$

### Extensions Beyond LCDM

The Planck data also constrain extensions to the standard model:

- **Spatial curvature**: $|\Omega_K| < 0.005$ (universe is flat to 0.5%)
- **Dark energy**: $w = -1.006 \pm 0.045$ (consistent with cosmological constant)
- **Neutrino masses**: $\sum m_\nu < 0.23$ eV (95% CL)
- **Effective neutrino species**: $N_{eff} = 3.15 \pm 0.23$ (consistent with 3 SM families)
- **Running spectral index**: $dn_s/d\ln k = -0.003 \pm 0.007$ (consistent with zero)

---

## Key Results

1. The six-parameter LCDM model provides an excellent fit to the Planck CMB data
2. $H_0 = 67.8 \pm 0.9$ km/s/Mpc (in tension with local measurements ~73 km/s/Mpc)
3. $\Omega_m = 0.308 \pm 0.012$ (30.8% matter, 69.2% dark energy)
4. $t_0 = 13.799 \pm 0.021$ Gyr (age of the universe to 0.15% precision)
5. The universe is spatially flat to 0.5% ($|\Omega_K| < 0.005$)
6. Dark energy is consistent with a cosmological constant ($w = -1.006 \pm 0.045$)
7. No evidence for physics beyond the standard LCDM model
8. The "Hubble tension" ($H_0^{Planck} \approx 67.8$ vs $H_0^{local} \approx 73$) remains
   unresolved

---

## Impact and Legacy

The Planck 2015 results paper is one of the most cited papers in all of physics (>10,000
citations). It established:

- The "concordance cosmology" with unprecedented precision
- Tight constraints on inflation models (via $n_s$ and $r$)
- The Hubble tension as a major open problem in cosmology
- Neutrino mass constraints competitive with laboratory experiments
- The benchmark values used by essentially ALL subsequent cosmological analyses

The Planck satellite ceased operations in 2013, and the final Planck 2018 data release
refined these parameters slightly but did not change the overall picture.

---

## Relevance to Paasch Framework

Paasch's Paper 03 cites this paper as [4] for two specific quantities:

1. **Age of the universe**: $t_0 = 13.799$ Gyr. Paasch uses this in his exponential mass
   formula via the LNH relation $G \propto 1/t$. He claims his model predicts $t_0$
   consistent with the Planck value.

2. **Mass of the observable universe**: Paasch derives $M_U$ from his mass formula and
   compares with the Planck-derived value $M_U \approx 4.5 \times 10^{53}$ kg.

**CRITICAL EVALUATION**: Paasch's model has MULTIPLE free parameters (mass numbers, the
reference mass $m_0$, the LNH time scale) that can be adjusted to match $t_0$ and $M_U$.
The match with Planck values is therefore a CONSISTENCY CHECK (verifying that reasonable
parameter choices exist) rather than a PREDICTION (deriving the values from fewer inputs).
Session 3 of the multi-agent review explicitly flagged this as a "fit not prediction"
situation: 4 parameters for 1 observable.

---

## Relevance to Phonon-Exflation Project

The Planck parameters provide the observational benchmarks that any cosmological framework
must match:

1. **Age and size**: $t_0 = 13.8$ Gyr and $R \sim 46$ Gly (comoving) are constraints on
   any expansion mechanism. The phonon-exflation framework parameterizes expansion through
   the deformation parameter $s(t)$, and the Planck values constrain the dynamics $s(t)$.

2. **Flatness**: $|\Omega_K| < 0.005$ is a strong constraint. In the phonon-exflation
   framework, spatial flatness follows from the product structure $M^4 \times K$ where
   $M^4$ is flat Minkowski space.

3. **Dark energy**: $w = -1.006 \pm 0.045$ is consistent with a cosmological constant. In
   the phonon-exflation framework, the effective cosmological constant would emerge from
   $V_{\text{eff}}(s_0)$ -- the spectral action evaluated at the physical minimum. This
   is a PREDICTION once $s_0$ is determined.

4. **Hubble tension**: The $\sim 5\sigma$ discrepancy between Planck and local $H_0$
   measurements COULD be a hint that the standard LCDM model is incomplete. The phonon-
   exflation framework offers a different expansion mechanism that might resolve this
   tension (though this is speculative at the current stage).
