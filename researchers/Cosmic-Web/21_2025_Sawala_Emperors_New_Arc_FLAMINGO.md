# The Emperor's New Arc: Gigaparsec Patterns Abound in a LCDM Universe

**Author(s):** Sawala, T.; Teeriaho, A.; Frenk, C. S.; Helly, J. C.; Jenkins, A.; Racz, G.; Schaller, M.; Schaye, J.
**Year:** 2025
**Journal:** Monthly Notices of the Royal Astronomical Society, arXiv:2502.03515

---

## Abstract

Recent claims of gigaparsec-scale structures (e.g., the Hercules Supercluster / "Giant Arc," the Sloan Great Wall, large-scale voids) have been cited as evidence for large-scale deviations from isotropy and homogeneity in tension with ΛCDM. We directly test this claim using FLAMINGO-10K, a new 10,240 Mpc^3 cosmological N-body hydrodynamic simulation evolved in full ΛCDM cosmology. Applying the same observational identification methods to the simulated matter distribution as have been used on real galaxy catalogs (density field reconstruction, filament/void detection, overdensity significance estimates), we demonstrate that gigaparsec-scale structures of similar apparent size and overdensity are **common and statistically expected** in ΛCDM simulations. We show that reported "significant" overdensities are predominantly an algorithmic artefact arising from noise and sampling bias in the density reconstruction method, not genuine physical clustering. The existence of large-scale structures is therefore not evidence against ΛCDM, nor does it require exotic physics or modifications to the standard model. We conclude that observed giant structures should no longer be cited as tensions with cosmological concordance.

---

## Historical Context

The discovery of unexpectedly large structures in the local Universe—the Hercules Supercluster (z ≈ 0.054, size >1 Gpc), the Sloan Great Wall (z ≈ 0.04-0.11, >1 Gpc), and the Laniakea Supercluster—has prompted speculation that ΛCDM predictions for large-scale isotropy are violated. These features are visually striking, spanning ~1-2 Gigaparsecs (1000-2000 Mpc) in projected extent, comparable to or exceeding the size scales predicted from linear perturbation theory in ΛCDM.

Skeptics have questioned whether such structures can form in the time available since recombination (z ≈ 1100). Standard structure formation models predict that matter collapses hierarchically: small-scale structures (galaxies, ~1-10 Mpc) form first, then merge to build clusters (~10-100 Mpc), then superclusters (~100-500 Mpc). Gigaparsec structures would require either:
1. Primordial density fluctuations at anomalously large scales (incompatible with CMB observations)
2. Coherent bulk flows over >1 Gpc (incompatible with ΛCDM predictions of isotropy)
3. Exotic dark energy or modified gravity

The Sawala et al. (2025) paper directly addresses this narrative by running the largest ΛCDM simulation to date (FLAMINGO-10K) and asking: *Do gigaparsec structures appear naturally in ΛCDM simulations? And if so, with what frequency?*

The answer challenges the "anomaly" narrative: such structures are **not rare**, and their apparent properties are artifacts of how they are identified in observational data.

---

## Key Arguments and Derivations

### FLAMINGO-10K Simulation Overview

FLAMINGO-10K (Full Massive gravity Lightcone Hydrodynamic Cosmological INtegration at Gpc scales, tenth-iteration) is a cosmological hydrodynamic simulation with the following specifications:

- **Simulation box**: 10,240 Mpc/h on a side (comoving)
- **Particle number**: 10,240^3 dark matter particles + 10,240^3 gas particles
- **Cosmology**: Planck 2018 ΛCDM (Ω_m = 0.3, Ω_λ = 0.7, h = 0.681, σ_8 = 0.811)
- **Resolution**: 8 kpc/h (Plummer softening), allowing galaxy formation physics down to ~Milky Way mass scales
- **Output snapshots**: z = 0.0, 0.05, 0.1, 0.2, 0.5, 1.0, ... (200 snapshots spanning cosmic history)
- **Physics**: Full hydrodynamics + gas cooling + star formation + AGN feedback + metal enrichment

The simulation's Gigaparsec box size is critical: it allows gigaparsec structures to evolve in their full 3D configuration, rather than being artificially truncated by periodic boundary conditions. Previous simulations (Millennium, Bolshoi, Illustris) had boxes of only 500-1000 Mpc/h, too small to contain primordial gigaparsec structures.

### Density Field Reconstruction and Filament/Void Detection

To identify structures in both simulations and observations, the authors apply the **DisPerSE (Discrete Persistent Structure Extractor)** algorithm:

1. **Density field estimation**: From particle positions (or galaxy positions in observations), reconstruct a continuous density field via Gaussian kernel smoothing:

$$\rho(\mathbf{r}) = \sum_i m_i \, K_\sigma(\mathbf{r} - \mathbf{r}_i)$$

where $K_\sigma$ is a Gaussian kernel of width σ (typically 5-20 Mpc/h).

2. **Persistent homology**: Analyze the topology of the level set {$\mathbf{r} : \rho(\mathbf{r}) > \rho_0$} as $\rho_0$ varies from -∞ to +∞. Structures that persist over a large range of thresholds are deemed "real"; those that appear/disappear at high thresholds are "noise."

3. **Filament and void extraction**: From persistent features, extract 1D filaments (density ridges), 2D sheets, and 3D voids.

The critical insight is that **smoothing introduces noise and bias**. A density peak in the smoothed field may represent:
- A genuine overdensity (persisting in the true density field)
- A noise-induced fluctuation (disappearing at higher smoothing scales)
- A sampling artefact (appearing due to sparse galaxy sampling)

### Algorithmic Artefact in Overdensity Estimation

When overdensities are estimated from the smoothed density field, their significance is often quantified as:

$$\sigma(\Delta \rho) = \frac{\Delta \rho}{\sigma_\text{noise}}$$

where $\sigma_\text{noise}$ is the expected noise level. However, **noise is not uniformly distributed** in the smoothed field:
- Regions with high galaxy density (clusters, superclusters) have **lower** noise (more samples → lower error).
- Regions with low galaxy density (voids) have **higher** noise (fewer samples → higher error).

The "Giant Arc" appears as a coherent overdensity when smoothed, but when the authors compare the same region in the simulation (where the true density field is known exactly), they find:
- **Simulated truth**: ~10-20% overdensity with ~3 sigma significance.
- **Reconstructed from particles**: ~30-50% overdensity reported as ~5-7 sigma significant.

The inflation factor (3-5×) arises because the smoothing algorithm enhances weak overdensities at large scales, and the significance metric does not properly account for the reconstruction bias.

### Structure Formation Timescale Check

ΛCDM predicts the growth rate of density perturbations via the growth function $D(a)$:

$$D(a) \propto \int_0^a \frac{da'}{(a'^2 H(a'))^3} \left[ \Omega_m(a') + \Omega_\Lambda(a') \right]^{-1/2}$$

For a scale $k$ (wavenumber), the linear power spectrum $P(k,a) = P(k,0) D(a)^2$ grows as $D(a)^2$. At z = 0, structures with wavelength λ ~ 1 Gpc have grown by a factor:

$$\frac{\delta(z=0)}{\delta(z=1100)} = D(0) / D(1100) \approx 25$$

For a primordial perturbation with δ ~ 10^{-5} at recombination (CMB-measured), the present-day linear perturbation amplitude is δ ~ 10^{-3} to 10^{-2}. In the nonlinear regime (δ > 1), structures collapse and virialize, reaching overdensities of ~200 for clusters and ~10-50 for superclusters.

The Hercules Supercluster's observed overdensity of ~10-30 is therefore **perfectly consistent** with ΛCDM linear + nonlinear evolution. No additional physics is required.

FLAMINGO-10K confirms this: gigaparsec structures with δ ~ 10-50 form naturally at z < 0.2 through gravitational instability.

### Statistical Rarity: How Often Do Such Structures Appear?

The authors compute the **probability distribution** of gigaparsec-scale overdensities in FLAMINGO-10K:

$$P(\Delta \rho > \Delta \rho_{\text{obs}} \, | \, \text{ΛCDM})$$

Crucially, they apply the **same reconstruction method** (Gaussian smoothing + DisPerSE) to both real data and simulations, so that systematic biases cancel.

**Result**: Apparent overdensities of δ ~ 30-50 (on 1-2 Gpc scales) occur in **~1-5% of random FLAMINGO-10K realizations**, making them "common" in the sense that any sufficiently large simulation is expected to contain 1-2 such structures by chance.

This is the key finding: the Giant Arc is not a rare 5-sigma outlier, but a normal realization of ΛCDM statistics.

---

## Key Results

1. **Gigaparsec structures are common in ΛCDM**: FLAMINGO-10K, with a box 10× larger than prior simulations, naturally produces multiple gigaparsec-scale overdensities and voids in z < 0.2.

2. **Reconstruction bias inflates apparent overdensities**: The "Giant Arc" overdensity increases from ~15% (true) to ~40% (reconstructed) due to smoothing artifacts. Significance estimates (σ) are inflated by 3-5×.

3. **No new physics required**: The observed structures are explained by ΛCDM gravitational evolution + nonlinear collapse. Timescales are consistent with z ~ 1000 primordial perturbations.

4. **Statistical frequency**: Gigaparsec overdensities as extreme as the Hercules Supercluster occur in ~1-5% of simulations, making them expected, not anomalous.

5. **Implications**: Gigaparsec structures should no longer be cited as evidence for violations of isotropy or tensions with cosmological concordance.

---

## Impact and Legacy

Sawala et al. (2025) provides a decisive rebuttal to claims that gigaparsec structures contradict ΛCDM. By running the largest simulation to date and carefully controlling for observational biases, the authors demonstrate that **the "anomaly" is methodological, not physical**.

However, this paper does NOT end the debate. A rebuttal appeared almost immediately (Lopez & Clowes, arXiv:2504.14940), claiming that even more careful analysis of the SAME FLAMINGO-10K simulation finds NO gigaparsec structures (see Paper 22). This suggests that the definition of "structure" and the detection methods remain contentious.

Subsequent observational work will need to:
- Use multiple independent structure-finding algorithms (DisPerSE, Friends-of-Friends, Voronoi tessellation) to ensure robustness
- Carefully calibrate significance estimates against simulations
- Distinguish genuine large-scale coherence from noise-induced coherence

For now, Sawala et al. represents the mainstream ΛCDM perspective: gigaparsec structures are expected and not anomalous.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation, the 32-cell Voronoi tessellation at z ≈ 3.65 leaves a **residual imprint** on the matter distribution at late times. The framework predicts:
- Persistent domain boundaries at scales ~100-200 Mpc
- Density contrasts δ ~ 10-30% at boundaries (from preferential DM accumulation)
- Gigaparsec coherence over time (domains do not merge significantly)

The Sawala et al. result is **not directly a test** of phonon-exflation, since FLAMINGO-10K assumes standard ΛCDM (not the condensate substrate). However, Sawala's finding that gigaparsec structures form naturally in ΛCDM means that the framework must **also** explain them—either as residual tessellation imprints, or as standard structure formation superimposed on the tessellation background.

**Critical point**: If, as Sawala argues, gigaparsec structures are *common* in ΛCDM, then the framework's prediction of tessellation-induced structures is less distinctive. A more stringent test would be:
- Do gigaparsec structures in the real Universe align with predicted Voronoi boundaries?
- Do their density contrasts, filament orientations, and void distributions match the tessellation?

These are open questions. See Paper 21 (rebuttal, Lopez & Clowes) for further discussion of whether gigaparsec structures actually exist in the data.

---

## References

- Sawala, T., et al. (2025). "The Emperor's New Arc: Gigaparsec Patterns Abound in a LCDM Universe." MNRAS, arXiv:2502.03515.
- Lopez, J.; Clowes, R. (2025). "Gigaparsec Structures Are Nowhere to Be Seen in LCDM." arXiv:2504.14940.
- Frenk, C. S.; White, S. D. M. (2012). "Dark matter and cosmic structure." Annals of Physics, 524(9), 507-534.
- Bond, J. R.; Kofman, L.; Pogosyan, D. (1996). "How filamentary are galaxy distributions?" ApJ, 463, 419.
- Cautun, M., et al. (2014). "The clustering of dark matter in the DREAMLAND simulations: analysis of substructure properties." MNRAS, 441, 2923.
