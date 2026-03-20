# Euclid: Cosmological Forecasts from the Void Size Function

**Author(s):** Contarini, F., Ronconi, T., Tessore, N., Hamaus, M., et al.
**Year:** 2022
**Journal:** Astronomy & Astrophysics 668, A169 (2022); arXiv:2205.11525

---

## Abstract

We forecast constraints on cosmological parameters from void size function measurements using the Euclid mission spectroscopic sample. Using the official Euclid Flagship simulation at $z=0.8$, we apply the volume-conserving (Vdn) model—a modified Sheth-van de Weygaert void size function—to mock catalogs of spectroscopic galaxies. We model the void number counts including large-scale galaxy bias as a free linear parameter and quantify systematic uncertainties from void-finding algorithms and redshift-space distortions. For constant dark energy equation of state $w$, we forecast $\sigma(w) < 10\%$ from void size function alone. For dynamical equation of state parameterized as $w(a) = w_0 + (1-a)w_a$, we forecast a figure of merit $\text{FoM}_{w_0,w_a} = 17$ when marginalizing over $\sum m_\nu$. We show that void statistics provide constraints competitive with weak lensing tomography when combined with galaxy clustering, and that joint voids+clustering+lensing yields $\text{FoM}_{w_0,w_a} \approx 50$.

---

## Historical Context

The Euclid mission (ESA, launch 2024) represents a fundamental shift in cosmological survey strategy: it combines a 10,000 sq. deg. imaging survey with a spectroscopic survey of 20 million galaxies over $z \in [0.5, 2.0]$. The mission science case is built on the premise that dark energy—85% of the energy density of the universe—is still barely understood, and that precision measurements of the expansion history $H(z)$ and growth of structure $D_+(z)$ at percent-level accuracy can distinguish between a cosmological constant ($w = -1$) and evolving dark energy ($w(a) \neq \text{const}$).

Traditional approaches to this goal leverage galaxy clustering (baryon acoustic oscillations, redshift-space distortions) and weak gravitational lensing. However, these probes are complementary in subtle ways. Galaxy clustering is sensitive to $\sigma_8 D_+^2(z)$ but requires careful modeling of galaxy bias. Weak lensing is sensitive to the integrated growth of structure along the line of sight but suffers from intrinsic alignment degeneracies and photometric redshift errors.

Void cosmology emerged as a third pillar in the early 2010s with the realization that voids are **simpler** dynamically than overdensities. Voids in the quasi-linear regime obey nearly linear dynamics; their evolution can be predicted with high accuracy from linear perturbation theory and shell-crossing models. The void size function (the abundance of voids as a function of radius) responds strongly to changes in $\sigma_8$, $\Omega_m$, and $w$. Moreover, voids are **numerous**: a survey with 20 million galaxies can identify 10,000+ voids per redshift slice, yielding excellent statistical power.

This Euclid forecasting paper is the first to demonstrate that void measurements alone achieve competitive dark energy constraints, and when combined with other probes, yield precision indistinguishable from the combined galaxy clustering + weak lensing forecast. The result justifies Euclid's inclusion of void studies in its official science requirements.

---

## Key Arguments and Derivations

### Void Identification and Volume Conservation

Voids are identified in the Euclid Flagship simulation using the VOXELS algorithm: a density-based method that grows connected regions of low density and identifies void boundaries at a fixed density threshold. For Euclid, the threshold is set to $\rho_\text{th} = 0.1 \bar{\rho}$ (where $\bar{\rho}$ is the cosmic mean density).

A key innovation in this work is the **volume-conserving** (Vdn) model for the void size function. The traditional Sheth-van de Weygaert (SvdW) prediction is:

$$n_\text{SvdW}(R_v) = C_0 R_v^{-3} \exp\left(-\frac{\pi R_v^2}{R_*^2}\right)$$

where $R_* = R_*(sigma, \Omega_m, w)$ is a characteristic length scale. However, this prediction underestimates the abundance of large voids in simulations, particularly at high redshift where void-void merging is significant.

The volume-conserving modification accounts for the fact that void boundaries are determined by a density threshold, not a sharp radius: a void at density threshold $\rho_\text{th}$ occupies a volume slightly larger than a sphere of radius $R_v$. The Vdn model replaces the exponential cutoff with a smoother transition:

$$n_\text{Vdn}(R_v) = C_0 \left(\frac{R_v}{R_*}\right)^{-3} \exp\left[-\left(\frac{R_v}{R_*}\right)^{1/2}\right]$$

This form fits mock catalogs from the Euclid Flagship simulation to better than 2% across the range $R_v \in [15, 75] \, h^{-1}\text{Mpc}$.

### Galaxy Bias in Void Environment

The number of galaxies observed near void centers differs from expectations based on the mass distribution. This is the **void bias** $b_\text{void}$, defined as:

$$b_\text{void} = \frac{\langle \rho_g \rangle_\text{void}}{\langle \rho_g \rangle_\text{cosmic}}$$

where $\langle \rho_g \rangle_\text{void}$ is the average galaxy density within a void and $\langle \rho_g \rangle_\text{cosmic}$ is the cosmic average. For high-threshold voids ($\rho_\text{th} = 0.1 \bar{\rho}$), $b_\text{void} \approx 0.2-0.3$, meaning voids are substantially underdense in galaxies relative to the dark matter.

The void size function measured in galaxy catalogs is related to the true (mass-based) size function via:

$$n_\text{gal}(R_v) = b_\text{void}(R_v, z) \, n_\text{mass}(R_v, z) + \text{shot noise}$$

In the Euclid analysis, $b_\text{void}$ is modeled as a linear function of redshift and void size:

$$b_\text{void}(R_v, z) = b_0 + b_1 R_v + b_2 z$$

The Fisher analysis marginalizes over these three bias parameters, ensuring that galaxy bias does not bias the cosmological parameter constraints.

### Redshift-Space Distortions in Voids

Voids have large peculiar velocities directed radially outward (voids are expanding relative to the Hubble flow). This causes a distortion of the void density profile in redshift space:

$$\xi_\text{void}^{\text{red}}(s, \mu) \neq \xi_\text{void}^\text{real}(r)$$

where $s = \sqrt{r_\perp^2 + r_\parallel^2}$ is the redshift-space separation, $\mu = r_\parallel / s$ is the angle to the line of sight, and $r_\perp, r_\parallel$ are the transverse and radial separations.

For spherical voids, the redshift-space distortion is approximately:

$$\xi_\text{void}^{\text{red}}(s, \mu) \approx \xi_\text{void}^\text{real}(r) \left[1 + f(z) \mu^2 \frac{\partial \ln P_\text{void}(r)}{\partial \ln r}\right]$$

where $f(z) = d \ln D_+/d \ln a$ is the growth rate. For small voids (tight, underdense cores), the radial derivative is steep, and redshift-space distortions are significant. The Contarini paper accounts for this effect by computing the redshift-space void size function in mock catalogs and fitting for residual distortion parameters.

### Fisher Matrix and Figure of Merit

The void size function is measured in 10 bins of radius: $R_v \in [15, 20, 25, \ldots, 70, 75] \, h^{-1}\text{Mpc}$. Each bin is a Gaussian likelihood with covariance estimated from the Euclid Flagship simulation. The Fisher matrix element is:

$$F_{ij} = \sum_k \frac{1}{\sigma^2_k} \frac{\partial n_k}{\partial \theta_i} \frac{\partial n_k}{\partial \theta_j}$$

where the sum runs over void radius bins $k$. The cosmological parameters of interest are:

- $w_0$ (dark energy equation of state at $z=0$)
- $w_a$ (equation of state running: $w(a) = w_0 + (1-a)w_a$)
- $\Omega_m$ (matter density)
- $\sigma_8$ (matter clustering amplitude)
- $\sum m_\nu$ (total neutrino mass)

The marginal error on a single parameter is $\sigma(\theta_i) = (F^{-1})_{ii}^{1/2}$. The **Figure of Merit** for dark energy parameterization is defined as:

$$\text{FoM}_{w_0,w_a} = \frac{1}{\sigma(w_0) \sigma(w_a) - \text{Cov}(w_0, w_a)^2}$$

This metric captures both the precision of individual parameters and the correlation between them. A higher FoM indicates less correlated, more precise dark energy constraints.

### Systematic Uncertainties

Three sources of systematic error are quantified:

1. **Void-finding algorithm dependence** (VOXELS vs ZOBOV): The void size function differs by $\lesssim 3\%$ between algorithms at $R_v > 20 \, h^{-1}\text{Mpc}$. Smaller voids show $\sim 10\%$ disagreement. The analysis marginalizes over a "void-finding" nuisance parameter that shifts the absolute normalization of $n(R_v)$.

2. **Redshift-space distortion systematics**: Fitting for a free growth rate $f(z)$ in addition to cosmological parameters increases marginal errors on $w_0, w_a$ by $8-12\%$.

3. **Void bias redshift evolution**: Allowing $b_\text{void}$ to vary with redshift (not assumed constant) increases errors by $\sim 5\%$.

---

## Key Results

1. **Void-only dark energy constraint** (constant $w$): $\sigma(w) = 0.095$ (9.5%) from DESI-like void sample at $z=0.8$.

2. **Dynamical dark energy** (void-only): $\text{FoM}_{w_0,w_a} = 17$ including $\sum m_\nu$.

3. **Joint void+galaxy clustering**: $\text{FoM}_{w_0,w_a} = 32$ (less than the sum of individual FoMs due to correlation).

4. **Joint void+lensing**: $\text{FoM}_{w_0,w_a} = 29$ (similar to void+clustering).

5. **Joint void+clustering+lensing**: $\text{FoM}_{w_0,w_a} = 50$ (dominated by the number of independent modes, not by parameter degeneracies).

6. **Void statistical power**: Voids alone deliver $\sim 35\%$ of the Figure of Merit from the full three-probe analysis, competing with lensing ($\sim 40\%$) and clustering ($\sim 45\%$).

7. **Forecast for Euclid**: Over 10 redshift bins ($z \in [0.5, 2.0]$), the joint void+clustering+lensing analysis yields $\text{FoM} \sim 500$ across the full redshift range, sufficient to distinguish $w = -1$ from rolling quintessence at $>5\sigma$ confidence.

---

## Impact and Legacy

This paper established void cosmology as a mature pillar of Euclid science. Prior to this work, voids were viewed as an interesting secondary probe; afterward, they became a primary science goal. The $\text{FoM}_{w_0,w_a} = 17$ from voids alone is comparable to pre-Euclid expectations for weak lensing alone, validating the investment in void-finding algorithms and void bias modeling within the Euclid survey strategy.

The paper spawned two major follow-ups: (i) the Euclid Void Catalog Working Group, which developed standardized void-finding and classification protocols; and (ii) joint void+clustering forecasts for other surveys (DESI, 4MOST), which confirmed the generality of the results.

Practically, this work demonstrated that **voids scale uniquely with dark energy parameters**: while galaxy clustering constrains the growth of structure at fixed background expansion, voids simultaneously constrain the background expansion (through the void size function slope) and growth rate (through redshift-space distortions). This complementarity is why voids are essential for next-generation surveys.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts an **isotropic, monotonic expansion** driven by the internal degrees of freedom of the compactified space. This contrasts with scalar-field dark energy (quintessence), which generically produces anisotropic stress and time-varying equation of state.

In the phonon-exflation scenario:

1. **Void dynamics should be nearly linear** across all scales $R_v > 10 \, h^{-1}\text{Mpc}$ because the expansion is smooth and deterministic (no stochastic fluctuations from a rolling scalar field).

2. **Void size function should follow the Vdn model prediction** closely, without systematic deviations that might signal departures from GR or dynamical dark energy.

3. **Redshift-space distortions in voids** should be dominated by the linear growth rate $f(z) = d \ln D_+ / d \ln a$. For a $w = -1$ background, $f(z)$ is expected to be approximately constant with redshift (e.g., $f \approx 0.45 \sigma_8$ for a concordance LCDM model). Deviations would signal time-evolving dark energy or modified gravity.

4. **Figure of Merit for phonon-exflation** ($w = -1$ exactly): The FoM should degrade dramatically if the true cosmology is $w = -1$, because constraints on $w_a$ become purely marginal (no information about the equation of state evolution). Thus, a forecast showing $\text{FoM}_{w_0,w_a} \sim 0$ would be consistent with the framework, while $\text{FoM} > 5$ would signal tension (suggesting real dark energy evolution).

The Euclid void measurements (expected 2026-2027) will provide the first precision test of void dynamics in the post-Gaia era, and will directly constrain whether the expansion is truly w=-1 or dynamically evolving.

