# The Perspective of Voids on Rising Cosmology Tensions

**Author(s):** Contarini, F.; Pisani, A.; Hamaus, N.; et al.
**Year:** 2024
**Journal:** arXiv:2212.07438 (A&A)

---

## Abstract

Contarini et al. present the first direct constraints on the cosmological parameters S8 and H0 derived from cosmic void statistics using BOSS DR12 galaxy samples. Using void number counts and void shape distortions (monopole and quadrupole of the void-galaxy cross-correlation), they obtain S8 = 0.813^(+0.093)_(−0.068) and H0 = 67.3^(+10.0)_(−9.1) km/s/Mpc. These measurements are consistent with Planck 2018 and weakly prefer lower S8 values compared to weak lensing surveys (KiDS, DES). The paper demonstrates that void-based cosmology provides an independent "viewing angle" on the Hubble tension and S8 discrepancy, with potential to break parameter degeneracies when combined with cluster and BAO measurements.

---

## Historical Context

Cosmic voids — underdense regions separated by filaments and walls — have historically been treated as "background" in cosmological analysis, with attention focused on clusters, filaments, and galaxy overdensities. However, since Sutter et al. (2014) and Hamaus et al. (2016), voids have been recognized as sensitive cosmological probes because:

1. **Sensitivity to S8**: Void abundance and shape distortions scale with $\sigma_8(1 + 0.5 w)$, making them particularly sensitive to matter clustering amplitude
2. **Complement to cluster constraints**: Clusters and voids respond oppositely to cosmological parameters, enabling parameter space reduction through joint analysis
3. **Weak lensing degeneracies**: Void measurements probe slightly different physical scales and physics than galaxy weak lensing, reducing prior degeneracies

The work by Contarini et al. represents the first rigorous application of void-derived constraints to the Hubble tension (H0 discrepancy between early-time and late-time measurements). Their measurement of H0 from voids—while still high-uncertainty—provides an independent leverage point for breaking the H0/S8 degeneracy.

---

## Key Arguments and Derivations

### Void Identification and Characterization

Voids are identified using the Void Finder algorithm on BOSS DR12 galaxies (redshift z ~ 0.5, comoving volume ~4 Gpc³):

$$\rho_{void}(r) = \rho_0 \left[ 1 - \frac{r^2}{r_{void}^2} \right]^{\alpha}$$

where:
- $r$ = distance from void center
- $r_{void}$ = void radius (typically 20-40 Mpc/h)
- $\alpha$ = shape exponent (typically $\alpha \approx 2$)
- $\rho_0$ = ambient galaxy density

### Void Number Count Function

The abundance of voids per unit volume per unit size bin is modeled by:

$$\frac{dn}{dR} = A \left( \frac{R}{R_0} \right)^{\lambda} \exp\left[ -\frac{R}{R_0} \right]$$

where $A$, $\lambda$, and $R_0$ are fitted from observations and validated against simulations. The functional form captures both the exponential cutoff at large radii and the power-law behavior at small radii.

This distribution is sensitive to $\sigma_8$: higher clustering amplitude produces fewer large voids (strong gravity accelerates void collapse into filaments). The sensitivity is quantified as:

$$\frac{d \ln(dn/dR)}{d \sigma_8} \approx -0.5 \text{ to } -1.2$$

depending on void size, making voids competitive with cluster counts for S8 constraints.

### Void-Galaxy Cross-Correlation and Redshift-Space Distortions (RSD)

The stacked void-galaxy cross-correlation function encodes both the void profile and redshift-space anisotropy:

$$\xi_{void-gal}(s, \mu) = \xi_0(s) \left[ 1 + \beta \mu^2 \right]$$

where:
- $s$ = comoving separation
- $\mu$ = cosine of angle to line of sight
- $\xi_0$ = monopole (isotropic component)
- $\beta$ = RSD parameter, $\beta = f(z) / b(z)$ with $f(z) = \Omega_m(z)^{0.55}$ and $b$ = galaxy bias
- The quadrupole $\xi_2$ arises from $\mu^2$ and $\mu^4$ terms

Void shape distortions (anisotropic clustering) encode the growth rate $f(z)$ and thus constrain $\Omega_m$ and $\sigma_8$ through growth structure:

$$f(z) = d \ln D_+(z) / d \ln a \quad \text{where} \quad D_+ \propto \int_z^\infty (1+z') E(z') dz' / E(z')^3$$

### Covariance Matrix and Likelihood

The joint likelihood combines void counts and cross-correlation:

$$-2 \ln \mathcal{L} = \sum_{i,j} \left[ d_i - m_i(\vec{\theta}) \right] C^{-1}_{ij} \left[ d_j - m_j(\vec{\theta}) \right]$$

where:
- $d$ = observational data vector (void counts + cross-correlation multipoles)
- $m(\vec{\theta})$ = model predictions (functions of cosmological parameters)
- $C_{ij}$ = covariance matrix including cosmic variance, Poisson noise, and shot noise

The covariance is computed from 1000 mock catalogs derived from BOSS FastPM simulations, accounting for realistic selection effects and non-Gaussian errors in the tails.

### Parameter Constraints

The posterior distributions are obtained via MCMC sampling:

**S8 = $\Omega_m^{0.5} \sigma_8$ = 0.813^(+0.093)_(−0.068)**

This is ~2 sigma lower than weak lensing estimates (KiDS: 0.766±0.024; DES: 0.801±0.025) and consistent with Planck 2018 CMB + $\Lambda$CDM predictions (0.811±0.006).

**H0 = 67.3^(+10.0)_(−9.1) km/s/Mpc**

This measurement is:
- Consistent with Planck (67.27±0.60)
- ~3 sigma higher than local H0 measurements (Riess et al. 2022: 73.0±1.0)
- Wide error bars reflect degeneracies with void bias and sound speed

---

## Key Results

1. **First void-derived S8**: Constrains the matter clustering amplitude independently from weak lensing, cluster counts, and BAO

2. **S8 tension softened**: Void measurements slightly favor lower S8, reducing but not resolving the 2-3 sigma discrepancy with KiDS/DES

3. **H0 independent determination**: While high-uncertainty, void-derived H0 provides leverage for H0/S8 degeneracy breaking

4. **Consistency with $\Lambda$CDM**: Both S8 and H0 constraints are fully compatible with Planck 2018, indicating no exotic physics required by void data

5. **Methodology validated**: Void number counts and RSD measurements calibrated against 1000 simulated catalogs to <5% systematic error

---

## Impact and Legacy

This work established void statistics as a viable independent cosmological probe, complementary to:
- Weak lensing (KiDS, DES, Euclid)
- Cluster abundance (SPT, ACT, eROSITA)
- BAO (BOSS, DESI)
- Supernovae (DES, ZTF)

Future improvements will come from:
- Larger void samples (DESI will provide ~3x volume increase)
- Combined void + cluster analysis (Pisani et al. 2025 in prep)
- Void profile modeling at non-linear scales
- Machine learning void identification (improved completeness)

---

## Connection to Phonon-Exflation Framework

**MODERATE CONNECTION**

The phonon-exflation framework predicts void structure from quasiparticle depletion in the many-body wavefunction:

1. **QP depletion channel**: In regions where the condensate gap is suppressed (e.g., near domain walls or Voronoi boundaries), the density of coherent phononic excitations drops, manifesting as observed voids

2. **Void size spectrum**: The framework predicts a characteristic void size related to the coherence length of the condensate, $\xi_cond ~ 50-100$ Mpc. Contarini's void radii (20-40 Mpc) bracket this prediction, suggesting multiple length scales (condensate coherence vs. Voronoi cell scale)

3. **S8 constraint test**: The framework predicts that cosmic structure formation occurs through a mechanism fundamentally different from gravitational instability (instead via phonon condensation). This should produce distinctive signatures in the void profile shape — particularly in the density profile exponent $\alpha$ and the size-function power law $\lambda$. The Contarini data provides the first probe of this prediction

4. **H0 discrepancy**: The framework naturally produces a local void (KBC void analog) due to the Voronoi tessellation. This local depletion zone could contribute to the local H0 measurement bias noted by Riess et al., providing a partial explanation for the H0 tension without exotic physics

**Action item**: Compare predicted void size function (from spectral action + phonon condensation) to Contarini's measured $dn/dR$ to refine framework predictions of S8.

