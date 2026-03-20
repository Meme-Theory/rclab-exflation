# Multi-probe Cosmology Forecasts from HOD-Based Void and Galaxy Statistics

**Author(s):** Salcedo, Pisani, Hamaus, et al.
**Year:** 2025
**Journal:** arXiv:2504.08221 (PRD submitted)

---

## Abstract

We forecast constraints on cosmological parameters from the combination of void statistics and galaxy clustering in DESI Year 5 spectroscopic survey. Using forward modeling with N-body simulations across a grid of $(\Omega_m, \sigma_8)$ parameter space, we employ Halo Occupation Distribution (HOD) modeling to capture galaxy-halo assembly bias and void-void clustering. Multi-probe summary statistics—void size function, void-galaxy cross-correlation, galaxy auto-correlation—are combined via Fisher matrix analysis and mock catalog validation. We forecast 1.5% precision on $\Omega_m$ and 0.8% precision on $\sigma_8$ from void+galaxy combined analysis, with void statistics alone yielding $2.1\%$ and $1.2\%$ respectively. We demonstrate that void and galaxy clustering measurements break the $(\Omega_m, \sigma_8)$ degeneracy that persists in galaxy clustering alone, establishing voids as a complementary high-information probe.

---

## Historical Context

Cosmic voids—large underdense regions of the matter distribution—have undergone a renaissance in cosmological analysis over the past decade. Historically, void studies were limited to X-ray observations of galaxy clusters and low-redshift optical surveys. However, the spectroscopic revolution initiated by SDSS, extended by BOSS, and now transformed by DESI has made void cataloging and statistical analysis both feasible and essential.

The theoretical foundation for void cosmology rests on three pillars. First, voids are dynamically simpler than overdensities: their evolution is driven primarily by gravitational expansion, with minimal role for nonlinear vorticity or shell-crossing in their interiors. This linearity makes them amenable to perturbative analysis. Second, the void size function—the comoving number density of voids as a function of radius—responds sensitively to changes in the growth rate of structure, encoded in $\sigma_8$, and to the matter density parameter $\Omega_m$ through the background expansion. Third, voids populate the cosmic web hierarchically: their spatial clustering encodes information about long-wavelength modulations in the density field that are complementary to galaxy clustering.

Prior work by Hamaus, Pisani, and collaborators established that void-finding algorithms (e.g., VOXELS, ZOBOV) recover topological and metric properties robustly across simulations and real surveys. The void size function was shown to follow a universal scaling form consistent with excursion-set models, confirming that voids obey quasi-linear dynamics even at modest redshifts $z<1$. Simultaneously, the discovery of assembly bias in void populations—the fact that void occupancy depends not only on environment but on halo assembly history—created both a challenge and an opportunity. The challenge: assembly bias introduces additional parameters and covariance into the likelihood. The opportunity: assembly bias carries information about the baryon-halo connection that improves constraints when properly marginalized.

This paper represents a maturation of void cosmology: it combines void-only statistics, galaxy clustering, and their cross-correlation into a single joint likelihood, leveraging HOD modeling to account for assembly bias. The result is a forecast of unprecedented precision: voids alone contribute $\approx 30\%$ to the total $\sigma(\Omega_m)$ constraint and dominate $\sigma(\sigma_8)$.

---

## Key Arguments and Derivations

### Void Definition and Size Function

Voids are identified in simulations using the ZOBOV algorithm, which grows Voronoi cells from particles until density drops below a fixed threshold (typically $\rho < 0.1 \bar{\rho}$). The void center is defined as the Voronoi nucleus (lowest density particle), and the void radius $R_v$ is the radius of the maximum sphere centered on this point that remains within the underdense region.

The void size function $n(R_v)$ gives the comoving number density of voids with radius between $R_v$ and $R_v + dR_v$:

$$n(R_v) dR_v = \text{number of voids per unit volume in radius bin}$$

In the linear/quasi-linear regime ($R_v \gtrsim 10 \, h^{-1}\text{Mpc}$), the void size function follows a scaling collapse onto a universal form:

$$n(R_v) = \bar{n}(R_v) \left[1 + \frac{\partial \ln n}{\partial \ln \sigma_8}(\sigma_8 - \sigma_{8,\text{fid}}) + \frac{\partial \ln n}{\partial \ln \Omega_m}(\Omega_m - \Omega_{m,\text{fid}}) + \ldots \right]$$

where $\bar{n}(R_v)$ is the fiducial prediction and derivatives are computed via finite differences across simulation suites. The void size function exhibits strong sensitivity to $\sigma_8$ (slope $\approx 2-3$ in $\log n \text{ vs } \log R_v$) because void abundance decreases with the amplitude of density fluctuations—larger $\sigma_8$ suppresses voids. Sensitivity to $\Omega_m$ arises through the growth rate $D_+ \propto \Omega_m^{0.55}$ at late times and through the background expansion $H(z)$.

### Void-Galaxy Cross-Correlation

The void-galaxy cross-correlation function $\xi_{vg}(r)$ measures the excess probability of finding a galaxy at distance $r$ from a void center:

$$\xi_{vg}(r) = \frac{\langle \rho_g(r) \rangle}{\langle \rho_g \rangle} - 1$$

where $\langle \rho_g(r) \rangle$ is the average galaxy density in shells of radius $r$ around void centers. This quantity carries information about the galaxy-halo connection near void boundaries, where density transitions from void interior ($\rho \ll \bar{\rho}$) to the cosmic average. Assembly bias contributes to $\xi_{vg}$ through the HOD: voids in low-assembly-bias halos (recently formed) preferentially occupy low-density regions and thus have galaxy density profiles slightly different from voids in high-assembly-bias halos (old, viralized).

### Halo Occupation Distribution Modeling

The HOD framework parameterizes the galaxy-halo connection as a conditional probability distribution. For central galaxies:

$$\langle N_c \rangle = \begin{cases}
0 & M < M_{\min} \\
\frac{1}{2} \left[1 + \text{erf}\left(\frac{\ln M - \ln M_c}{\sigma_{\log M}}\right)\right] & M \geq M_{\min}
\end{cases}$$

For satellite galaxies:

$$\langle N_s \rangle = \left(\frac{M - M_0}{M_1}\right)^\alpha \quad \text{for} \quad M > M_0$$

where $M_{\min}, M_c, \sigma_{\log M}, M_0, M_1, \alpha$ are six HOD parameters constrained from galaxy clustering and group catalogs. Assembly bias enters through a seven-parameter extension:

$$\langle N_s \rangle = \langle N_s \rangle_0 \left[1 + b_{s,\text{AB}} \, f_\text{AB}(\eta)\right]$$

where $f_\text{AB}(\eta)$ is an assembly bias proxy computed from halo formation time $\eta$ and $b_{s,\text{AB}}$ is the assembly bias amplitude (typically $|b_{s,\text{AB}}| \lesssim 0.3$).

The combined HOD+assembly-bias model is applied to N-body simulation snapshots at $z=0.7$ (mean DESI-LRG redshift). For each simulation at cosmology $\boldsymbol{\theta} = (\Omega_m, \sigma_8, \ldots)$, galaxies are painted onto halos using the HOD likelihood, and mock catalogs are generated with realistic geometry and selection functions.

### Fisher Matrix and Forecasting

Parameter constraints are forecasted via Fisher matrix formalism. For a set of summary statistics $\vec{d}(\boldsymbol{\theta})$ with covariance $\mathbf{C}$, the Fisher matrix element is:

$$F_{ij} = \frac{\partial \vec{d}^T}{\partial \theta_i} \mathbf{C}^{-1} \frac{\partial \vec{d}}{\partial \theta_j}$$

The joint forecast combines three probes:

1. **Void size function** $n(R_v)$ in 5 radius bins ($15-45 \, h^{-1}\text{Mpc}$)
2. **Void-galaxy cross-correlation** $\xi_{vg}(r_\perp, r_\parallel)$ in 8 bins ($0.1-50 \, h^{-1}\text{Mpc}$)
3. **Galaxy clustering** $\xi_{gg}(r_\perp, r_\parallel)$ in 15 bins ($0.1-100 \, h^{-1}\text{Mpc}$)

The covariance matrix is estimated from 300 mock catalogs drawn from the N-body suite (10 realizations per cosmology, 10 cosmologies surrounding the fiducial point). Covariance includes sample variance, Poisson shot noise, and the galaxy count variance from HOD sampling.

The void size function alone yields constraints via:

$$\vec{F}_\text{void} = \sum_i \frac{1}{\sigma^2_i} \left(\frac{\partial \vec{n}}{\partial \Omega_m}, \frac{\partial \vec{n}}{\partial \sigma_8}, \ldots \right)^T \left(\frac{\partial \vec{n}}{\partial \Omega_m}, \frac{\partial \vec{n}}{\partial \sigma_8}, \ldots \right)$$

where the sum runs over radius bins. The galaxy clustering alone yields $\vec{F}_\text{gal}$. The cross-correlation contributes $\vec{F}_\text{cross}$. The total forecasted error on parameter $\theta_i$ is:

$$\sigma(\theta_i) = \left[(\mathbf{F}_\text{void} + \mathbf{F}_\text{gal} + \mathbf{F}_\text{cross})^{-1}\right]_{ii}^{1/2}$$

### Degeneracy Breaking

In galaxy clustering alone, the $(\Omega_m, \sigma_8)$ degeneracy arises because the clustering amplitude is sensitive to $\sigma_8 \, D_+(z) \, b(z)$ (the product of clustering amplitude, growth factor, and bias), and both $\Omega_m$ (through $D_+$) and $\sigma_8$ drive this product in similar directions at modest redshift. The void size function breaks this degeneracy because $n(R_v)$ depends differently on $\Omega_m$ and $\sigma_8$: the void abundance scales as $\propto \sigma_8^{-2}$ (approximately) due to the exponential sensitivity of the halo mass function, while the dependence on $\Omega_m$ is weaker and mediated through the growth rate. Additionally, the void-galaxy cross-correlation probes the density profile transition at void boundaries, providing leverage on the large-scale bias that complements small-scale clustering.

The Fisher matrix eigendecomposition reveals that the two largest eigenvectors of the joint $(F_\text{void} + F_\text{gal} + F_\text{cross})$ correspond to: (1) the total matter density-growth factor combination $\Omega_m D_+^2$, and (2) a "void-dominated" direction sensitive to $\sigma_8$ at fixed growth rate. Combined constraints on these eigendirections yield $\sigma(\Omega_m)/\Omega_m \approx 1.5\%$ and $\sigma(\sigma_8)/\sigma_8 \approx 0.8\%$.

---

## Key Results

1. **Void-only constraint**: $\sigma(\Omega_m) = 2.1\%$, $\sigma(\sigma_8) = 1.2\%$ from void size function + void clustering alone in DESI-Y5 footprint (14,000 sq. deg., 10 million galaxies).

2. **Galaxy clustering alone**: $\sigma(\Omega_m) = 2.4\%$, $\sigma(\sigma_8) = 1.5\%$ from galaxy clustering to $r_\parallel < 200 \, h^{-1}\text{Mpc}$.

3. **Combined constraint**: $\sigma(\Omega_m) = 1.5\%$, $\sigma(\sigma_8) = 0.8\%$ from the joint likelihood of voids + galaxies + cross-correlation.

4. **Void contribution**: Voids contribute $30\%$ of total Fisher information on $\Omega_m$ and $50\%$ on $\sigma_8$.

5. **Assembly bias impact**: Marginalizing over assembly bias amplitudes increases forecast errors by $8\%$ (on $\Omega_m$) to $12\%$ (on $\sigma_8$), but the joint analysis remains superior to galaxy clustering alone.

6. **Redshift evolution**: Forecasts improve by $\approx 15\%$ when extending analysis to full DESI redshift range ($z \in [0.5, 1.6]$) by using multiple void catalogs at different redshifts and fitting the growth of structure.

7. **Degeneracy reduction**: The void size function reduces the $(\Omega_m, \sigma_8)$ correlation coefficient from $r=0.87$ (galaxies alone) to $r=0.34$ (joint analysis).

---

## Impact and Legacy

This work establishes void statistics as a mature, precision probe complementary to galaxy clustering for DESI and future surveys. It demonstrates that voids—the "empty space" between galaxies—contain as much or more information about cosmology as the space occupied by matter itself. The 1.5% and 0.8% forecasts represent a fourfold improvement over pre-DESI void studies (which achieved $\sim 6-8\%$ constraints from BOSS voids at $z\sim 0.5$).

The paper will likely catalyze three follow-up directions: (i) joint void+galaxy analyses on actual DESI data, (ii) extension to redshift-space distortions in voids (void-void peculiar velocities), and (iii) void tomography at multiple redshift slices to map the evolution of $\Omega_m(z)$ and $\sigma_8(z)$ independently.

The assembly bias model introduced here provides a template for separating galaxy physics from cosmology in other large-scale structure probes (clusters, filaments), reinforcing the principle that **the cosmic web itself—voids, filaments, walls, and knots—is a precision cosmological tool**.

---

## Connection to Phonon-Exflation Framework

The framework predicts a tessellated matter distribution: a 32-cell Voronoi partition where vertices correspond to DM concentrations (quasiparticle loci) and void centers correspond to pairing nodes. The phonon-exflation model predicts that:

1. **Void density profiles** should be nearly spherical (no "pancaking" from anisotropic expansion) if the expansion is driven by isotropic phononic excitations of the compactified space, not by kinetic energy of a scalar field.

2. **Void size function scaling** ($\propto \sigma_8^{-2}$) depends on the amplitude of density fluctuations; in phonon-exflation, the spectrum of curvature fluctuations is modified by the spectral action, potentially altering the exponent.

3. **Assembly bias in voids** is suppressed in phonon-exflation if the BCS instability quenching is rapid (high coherence loss prevents halo clustering strongly with formation time).

4. **Redshift-space distortions in void peculiar velocities** would constrain the expansion rate $H(z)$ at precision $\approx 1.5\%$, sufficient to distinguish $w=-1$ from a rolling quintessence model ($w(z) = w_0 + (1-a)w_a$ with $w_a \neq 0$).

The DESI-Y5 void catalog (expected 2026) will be the first precision test of these predictions, providing a direct observational handle on the large-scale isotropy and spectral properties of the cosmic expansion.

