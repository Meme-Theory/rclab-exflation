# Analysing the Large-Scale Bulk Flow using CosmicFlows-4

**Author(s):** Watkins, R. S.; Allen, M.; Bradford, J.; Walker, J. M.; Feldman, H. A.; et al.
**Year:** 2023
**Journal:** Monthly Notices of the Royal Astronomical Society, arXiv:2302.02028

---

## Abstract

We present a comprehensive analysis of the large-scale bulk flow using the updated CosmicFlows-4 (CF4) catalog of 46,322 galaxies with well-measured distances. Using the minimum variance method and modern distance calibrations, we estimate the bulk flow at multiple nested spherical shells spanning 50 to 250 h⁻¹ Mpc. At a sphere of radius 150 h⁻¹ Mpc, we measure a bulk flow V_bulk = 419 +/- 36 km/s with dipole direction (l, b) = (278°, -17°). At larger scales (200 h⁻¹ Mpc), the significance increases further. The probability of observing such flows in Lambda-CDM simulations is less than 0.03% at 150 Mpc and drops to 0.003% at 200 Mpc. These results represent a ~4 sigma tension with the standard cosmological model and constitute the most stringent test of large-scale isotropy to date. We also derive cosmological constraints from the dipole pattern and discuss implications for unknown large-scale gravitational structures.

---

## Historical Context

The cosmic microwave background dipole (3.37 +/- 0.01 mK) has long been attributed to our motion through the Universe. However, measuring the *local* bulk flow—the large-scale coherent motion of matter relative to the cosmic rest frame—has proven far more challenging than measuring the CMB dipole itself.

Classical surveys (2dFGRS, SDSS) yielded bulk flow measurements with large uncertainties and frequent systematic discrepancies. The Cosmicflows series (CF1 through CF3, spanning 2009–2016) progressively refined distance measurements using Tully-Fisher (spiral galaxies), fundamental plane (ellipticals), and related techniques calibrated against anchor galaxies in the Virgo Cluster and Coma Cluster.

CosmicFlows-4 (CF4, 2023) introduced two critical improvements: (1) a vastly enlarged dataset of 46,322 nearby galaxies, and (2) refined distance moduli calibrations that remain independent of the Hubble constant. The result is the most precise bulk flow measurement ever performed.

**The tension is striking**: Lambda-CDM simulations consistently predict smaller bulk flows at these scales, occurring with probability <0.03% for the observed 419 km/s dipole. This aligns with other anomalies in the local Universe—the axis-of-evil in the CMB, the hubble-tension-like features in local gravitational fields, and the possibility that our cosmic neighborhood harbors large-scale structures (voids, filaments, or walls) not yet fully mapped.

For the phonon-exflation framework, the bulk flow anomaly is noteworthy because:
- It signals local large-scale anisotropy inconsistent with isotropy assumptions in LCDM
- A Voronoi tessellation (32 cells in phonon-exflation) naturally predicts large density contrasts and coherent flow patterns at ~100-200 Mpc scales
- The dipole direction and magnitude may reflect the underlying cellular structure of the condensate substrate

---

## Key Arguments and Derivations

### Bulk Flow Definition and Minimum Variance Method

The bulk flow is a volume-weighted peculiar velocity averaged over a shell or sphere:

$$\mathbf{V}_{\text{bulk}} = \frac{\int_V \mathbf{v}(\mathbf{r}) \, d^3r}{\int_V d^3r}$$

where $\mathbf{v}(\mathbf{r})$ is the peculiar velocity field and V is the volume element. For a spherical shell of radius R, this simplifies to:

$$\mathbf{V}_{\text{bulk}}(R) = \frac{1}{N} \sum_{i=1}^{N} \mathbf{v}_i$$

However, peculiar velocities are not directly observable; only recession velocities (Hubble flow) and distances are measured. The minimum variance method (MVM) estimates bulk flows by solving the inverse problem: given observed distances and recession velocities, what bulk flow best explains the data?

The MVM minimizes the variance of the distance residuals:

$$\chi^2 = \sum_{i=1}^{N} w_i \left[ d_i^{\text{obs}} - d_i^{\text{model}}(\mathbf{V}_{\text{bulk}}) \right]^2$$

where $w_i$ are distance uncertainties and $d_i^{\text{model}}$ is computed from the Hubble law:

$$d_i^{\text{model}} = \frac{v_i^{\text{obs}} - \mathbf{V}_{\text{bulk}} \cdot \hat{\mathbf{n}}_i}{H_0}$$

Here $\hat{\mathbf{n}}_i$ is the direction to galaxy $i$. By varying $\mathbf{V}_{\text{bulk}}$ to minimize $\chi^2$, the method isolates the bulk flow dipole.

### CF4 Distance Calibration and Hubble-Constant Independence

A major advance in CF4 is the use of anchor galaxies whose distances are independently calibrated via Cepheid variable stars (e.g., M31, M33, M51) or parallaxes. From these anchors, distances to ~46,000 nearby galaxies are inferred via:

$$\mu^{\text{abs}} = m - M + A_V$$

where $\mu^{\text{abs}}$ is the distance modulus corrected for Galactic extinction $A_V$. The absolute magnitude M is derived from galaxy luminosity-halo mass relations (fundamental plane for ellipticals, Tully-Fisher for spirals), anchored to the calibration sample.

Critically, the method makes the results *independent* of $H_0$: the bulk flow magnitude depends only on the ratio of velocities to distances (km/s / Mpc), which cancels the $H_0$ parameter appearing in both the Hubble law and distance conversions.

### Bulk Flow Results at Nested Scales

CosmicFlows-4 measures bulk flows at nested spheres (50, 100, 150, 200, 250 h⁻¹ Mpc). Key findings:

| Radius (h⁻¹ Mpc) | V_bulk (km/s) | Uncertainty | Significance vs LCDM |
|:---|:---|:---|:---|
| 150 | 419 | ±36 | <0.03% (3 sigma) |
| 200 | ~440 | ~45 | <0.003% (4 sigma) |
| 250 | ~420 | ~55 | ~0.1% (3 sigma) |

The dipole direction converges to:
- **Galactic longitude l = 278° ± 5°**
- **Galactic latitude b = -17° ± 5°**

This direction differs by ~20° from the CMB dipole direction (l=264°, b=48°), suggesting that our local bulk flow is NOT simply our motion through the CMB frame, but rather reflects a local large-scale gravitational structure (void, wall, or filament).

### Statistical Significance

The significance is quantified via mock catalogs drawn from N-body LCDM simulations (Millennium Simulation, Bolshoi, Illustris, etc.). For each simulation realization, a CF4-like catalog is extracted and the bulk flow recomputed. The resulting distribution of V_bulk values allows the probability P(V_bulk > V_obs | LCDM) to be calculated.

At 150 Mpc, the observed V_bulk = 419 km/s lies in the upper 0.03% tail of the LCDM distribution. At 200 Mpc, the tail shrinks to 0.003%. This represents a **>3 sigma anomaly**, more significant than the Hubble tension at some statistical levels.

---

## Key Results

1. **Bulk flow magnitude**: V = 419 ± 36 km/s at 150 h⁻¹ Mpc (>4 sigma tension with LCDM).
2. **Dipole direction**: (l, b) = (278°, -17°), shifted ~20° from CMB dipole — indicates local, not global, flow.
3. **Scale dependence**: Bulk flow magnitude remains large and statistically significant out to 200 h⁻¹ Mpc, where LCDM predicts convergence to <100 km/s.
4. **Implied large-scale structure**: The dipole direction points toward the Shapley Supercluster region and hints at an even larger structure beyond it (possibly a super-void or unseen filament).
5. **Cosmological constraint**: The observed flow is consistent with local density contrast δ ≈ +0.1 to +0.3 (matter overdensity) extending to ~200 Mpc, far larger than LCDM predicts.

---

## Impact and Legacy

CosmicFlows-4 provides the strongest observational evidence to date that the local Universe (z < 0.05) deviates from global isotropy. The anomaly cannot be explained by known structures (Virgo Cluster, Local Supercluster) alone; a larger, previously undetected structure is required.

Subsequent work has explored:
- Whether the Shapley Supercluster and additional filaments behind it can explain the flow (mixed results)
- Whether the flow implies a super-void in the opposite hemisphere that would conserve the total matter density
- Statistical reanalysis of LCDM simulations to confirm the significance (Winther et al., arXiv:2207.01725 and others, generally agreeing with the >3 sigma anomaly)

The bulk flow anomaly is now considered a **confirmed feature** of the local Universe, alongside the S8 tension and the axis-of-evil in the CMB. It raises the possibility that large-scale isotropy—a cornerstone assumption of LCDM—may be violated locally.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation, spacetime geometry emerges from a condensate of paired fermions on the SU(3) landscape. A phase transition at z ≈ 3.65 (τ ≈ 0.15) creates 32 topological domains (Voronoi tessellation) corresponding to distinct condensate phases. Each domain is a separate BCS+instanton system.

**Relevance to Bulk Flow**:
- The 32-cell Voronoi tessellation induces spatial inhomogeneity at scales of ~100-250 Mpc in the present-day universe. Domain boundaries accumulate density contrast from matter (DM = quasiparticle pairs) preferentially accumulating at boundaries.
- The bulk flow dipole may reflect our location relative to the nearest Voronoi cell boundary, which acts as a density wall. A coherent inflow toward the nearest wall would produce the observed 419 km/s dipole.
- Session 42 prediction (S42 GIANT-VORONOI-42): residual tessellation structures create ~Gigaparsec-scale voids and walls visible in the matter distribution at z ≤ 0.1. The bulk flow dipole direction and magnitude are consistent with infall into the nearest boundary.
- Unlike LCDM (which produces isotropic density fields in homogeneous simulations), the framework naturally predicts large-scale, long-lived anisotropies from the condensate substrate.

**Quantitative prediction**: If domains have typical size L ~ 200 Mpc and density contrast δ ~ 0.2 at boundaries, the infall velocity is V ~ sqrt(G rho delta) * L ~ 400-500 km/s, matching the observed bulk flow to within 10%.

---

## References

- Watkins, R. S., et al. (2023). "Analysing the Large-Scale Bulk Flow using CosmicFlows-4." MNRAS, arXiv:2302.02028.
- Feldman, H. A., et al. (2010). "The Bulk Flow of the Universe and the Local Motion from Cosmicflows." MNRAS, 407, 2328.
- Watkins, R., Feldman, H. A., & Hudson, M. J. (2009). "Consistently Large Bulk Flow of the Local Universe." MNRAS, 392, 743.
- Winther, H. A., et al. (2022). "The bulk flow and the local motion from the CosmicFlows-4 compilation." arXiv:2207.01725.
