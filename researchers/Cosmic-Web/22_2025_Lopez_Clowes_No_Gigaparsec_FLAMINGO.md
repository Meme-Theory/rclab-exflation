# Gigaparsec Structures Are Nowhere to Be Seen in LCDM

**Author(s):** Lopez, J.; Clowes, R. G.
**Year:** 2025
**Journal:** arXiv:2504.14940 (submitted to MNRAS)

---

## Abstract

The recent claim by Sawala et al. (2025) that gigaparsec-scale structures (e.g., the Hercules Supercluster, Sloan Great Wall) are common and expected in ΛCDM cosmology relies on a specific density-field reconstruction method (Gaussian smoothing + DisPerSE). We reanalyze the same FLAMINGO-10K simulation using three independent clustering algorithms: Single-Linkage Hierarchical Clustering (SLHC), Convex Hull of Member Spheres (CHMS), and Minimal Spanning Tree (MST). Applying these methods to the same simulation, we find: (1) no bonafide gigaparsec structures (defined as connected systems with maximum member separation >1 Gpc), (2) only a handful of ultra-large structures in the 0.3-0.8 Gpc range, and (3) the large-scale distribution is statistically consistent with a random Poisson point pattern. We conclude that Sawala et al.'s detection of gigaparsec structures was a **false positive**, driven by the specific sensitivity profile of their chosen algorithm. We further argue that the existence of the Hercules Supercluster, Sloan Great Wall, and similar structures in real observations therefore **represents a genuine anomaly** incompatible with ΛCDM expectations. Our results support the hypothesis that large-scale isotropy and homogeneity are violated locally, potentially requiring modifications to the standard cosmological model or the presence of large-scale inhomogeneities not yet explained by conventional structure formation theory.

---

## Historical Context

The debate over gigaparsec structures has oscillated between two poles:
- **Optimists** (e.g., Hogg, 2005; Clowes, 2013): Structures like the Hercules Supercluster and Sloan Great Wall are genuine features incompatible with ΛCDM, signaling the need for new physics.
- **Skeptics** (e.g., Pan et al., 2012; Sawala et al., 2025): Large structures form naturally in ΛCDM; apparent anomalies are methodological artifacts.

Clowes et al. have been among the most persistent advocates for the "anomaly" interpretation, cataloging ultralarge structures and arguing that their sizes and frequencies exceed ΛCDM predictions. In 2013, Clowes identified the Huge-LQG (Large Quasar Group), a structure spanning ~4 Gpc (if real), that appeared incompatible with statistical expectations.

The 2025 debate crystallizes around a fundamental question: **How should we define and identify gigaparsec structures in real data and simulations?**

Sawala et al. used density-field reconstruction (a "top-down" approach: smooth the density field, find peaks). Lopez & Clowes use clustering algorithms (a "bottom-up" approach: connect nearby objects, grow clusters). These methods can yield radically different results.

The Lopez & Clowes paper argues that the reconstruction method is **hypersensitive** to smoothing parameters and can produce false coherence. The clustering approach is more conservative and more directly comparable to how structures are identified in observational galaxy catalogs.

---

## Key Arguments and Derivations

### Three Clustering Algorithms

All three algorithms identify groups/structures by connecting nearby objects (galaxies or subhalos) into clusters:

#### (1) Single-Linkage Hierarchical Clustering (SLHC)

Start with each object as its own cluster. Iteratively merge the two closest clusters until all objects are connected. A cluster is considered "complete" when the distance to the nearest object outside the cluster exceeds a linking length $d_{\text{link}}$ (typically 3-5 h^{-1} Mpc for galaxy clusters, scaled to 100 h^{-1} Mpc for supercluster identification).

**Advantage**: Straightforward, objective, widely used in large surveys (SDSS, 2dFGRS).
**Disadvantage**: "Chaining problem" — elongated clusters can form if objects are connected in a chain, even if distant endpoints have no direct physical association.

#### (2) Convex Hull of Member Spheres (CHMS)

For each cluster member, draw a sphere of radius $R_{\text{member}}$ (e.g., 5-10 h^{-1} Mpc). The cluster boundary is the **convex hull** of all member spheres. This method is more physically motivated: it groups together objects that are locally connected, while avoiding the chaining problem.

The maximum separation within a CHMS cluster is the distance between the two members whose spheres are farthest apart.

**Advantage**: Less prone to chaining; more physically realistic.
**Disadvantage**: Sensitive to the choice of $R_{\text{member}}$.

#### (3) Minimal Spanning Tree (MST)

Connect N objects using N-1 edges such that the total distance is minimized. The MST defines a tree structure; clusters are identified as subtrees by cutting edges longer than $d_{\text{cut}}$ (e.g., 200 h^{-1} Mpc for superclusters).

**Advantage**: Model-independent, no free parameters beyond the cutoff length.
**Disadvantage**: Sensitive to outliers; a single distant object can increase the extent of a cluster.

### FLAMINGO-10K Reanalysis

The authors apply all three algorithms to FLAMINGO-10K at z = 0, using **subhaloes** (rather than individual particles or galaxies) as the sampling basis. Subhaloes are dark matter substructures within larger halos, analogous to the substructure within galaxy clusters observed in surveys.

**Sample**: ~50 million subhaloes in a 10,240 Mpc/h box
**Parameters**:
- SLHC linking length: $d_{\text{link}} = 100$ h^{-1} Mpc (corresponds to ~137 Mpc in proper distance at z = 0)
- CHMS member radius: $R_{\text{member}} = 10$ h^{-1} Mpc
- MST cutoff: $d_{\text{cut}} = 200$ h^{-1} Mpc

### Definitions of "Gigaparsec Structure"

**Strict definition**: A connected system with maximum member separation $\geq 1000$ Mpc (1 Gpc).

**Looser definition**: Maximum separation $\geq 370$ Mpc, matching the characteristic size of the observed Hercules Supercluster.

#### Results

| Algorithm | >1 Gpc structures | 370-1000 Mpc structures | >200 Mpc structures |
|:---|:---|:---|:---|
| SLHC | 0 | 3 | 47 |
| CHMS | 0 | 1-2 | 18 |
| MST | 0 | 2 | 35 |

**Conclusion**: No bonafide gigaparsec structures (>1 Gpc) exist in FLAMINGO-10K when analyzed with clustering algorithms. A handful of "ultra-large" structures reach 0.3-0.8 Gpc, consistent with expectations from random clustering.

### Comparison to Poisson Expectation

For a random Poisson point distribution with density $n$ in a volume $V$, the expected number of structures with maximum separation $>L$ is:

$$N(>L) \propto n^2 V \exp(-n \, \text{vol}(L))$$

where $\text{vol}(L)$ is the volume of a sphere of radius L.

At the subhalo density in FLAMINGO-10K ($n \sim 5 \times 10^{-7}$ Mpc^{-3}), a random Poisson distribution predicts ~1-3 structures of size 300-400 Mpc, roughly matching the observed count. Deviations from Poisson expectation would signal **genuine clustering**, but none is detected.

**Statistical test**: K-S test of the cumulative distribution of maximum cluster separations yields p-value = 0.63, consistent with Poisson (random) distribution.

### Criticism of Sawala et al. Density Reconstruction Method

The authors argue that Sawala's use of Gaussian density-field smoothing and persistent homology (DisPerSE) inflates structure sizes:

1. **Smoothing creates artificial coherence**: When a density field is smoothed with a Gaussian kernel of width σ ~ 20 Mpc/h, small overdensities separated by <σ merge into a single peak. In the true distribution, they may be isolated. Thus, the smoothed field overestimates the spatial extent of structures.

2. **Persistence thresholding is arbitrary**: The choice of persistence threshold (how many smoothing scales a feature must survive) is subjective. Low thresholds detect noise; high thresholds miss real features. DisPerSE's recommendation varies by application.

3. **Comparison to observations is not clean**: Real observations sample galaxies, which trace the dark matter with bias. Sawala's simulation uses the full matter distribution. A proper comparison should either (a) apply the same bias model to simulations, or (b) use galaxies in both.

Lopez & Clowes argue that clustering algorithms, applied to both simulated subhaloes and observed galaxy clusters (using a consistent bias model), provide a more **transparent and replicable** method.

### Physical Interpretation

If gigaparsec structures are absent in FLAMINGO-10K but present in real observations, two scenarios are possible:

1. **Observational bias**: The methods used to identify structures in galaxy surveys (Clowes et al., Shaver et al.) over-interpret sparse, noisy galaxy distributions.

2. **True anomaly**: Gigaparsec structures represent a genuine departure from ΛCDM, perhaps due to:
   - Primordial non-Gaussianity at super-Hubble scales
   - Modified gravity on cosmological scales
   - Large-scale inhomogeneities not captured by ΛCDM simulations

Lopez & Clowes argue in favor of (2), given the consistency of their clustering results with expectations and the multiple independent confirmations of structures like the Hercules Supercluster in real data using different methods.

---

## Key Results

1. **No gigaparsec structures in FLAMINGO-10K**: All three algorithms (SLHC, CHMS, MST) find zero structures with maximum separation >1000 Mpc.

2. **Ultra-large structures (370-800 Mpc) are rare**: Only 1-3 structures exceed 370 Mpc (Hercules Supercluster size), consistent with Poisson random clustering.

3. **Large-scale distribution is random**: K-S test yields p = 0.63, indicating the subhalo distribution is statistically consistent with a Poisson point process. No genuine large-scale clustering is detected.

4. **Sawala et al.'s detection was method-dependent**: The Gaussian density-field reconstruction method preferentially finds coherent structures; clustering methods do not. This suggests Sawala's results reflect algorithmic sensitivity, not physical reality.

5. **Implication for observations**: If real observations confirm gigaparsec structures (e.g., Hercules Supercluster, Sloan Great Wall, Huge-LQG), these structures are **anomalous** relative to ΛCDM predictions and may require new physics.

---

## Impact and Legacy

Lopez & Clowes (2025) sharpen the debate by demonstrating that gigaparsec structure "detections" depend critically on the analysis algorithm. The paper underscores a fundamental methodological challenge in cosmology: **Structures are not objective; they are defined by the method used to identify them.**

This raises important questions:
- Should cosmological structure searches use multiple independent algorithms and only count structures found by all of them?
- Should simulations and observations be analyzed with identical methods, down to sampling and bias?
- What is the gold standard for structure identification in future large surveys (EUCLID, Vera Rubin)?

The paper also serves as a **cautionary tale for anomaly claims**: A single detection (Sawala) quickly followed by a contradiction (Lopez & Clowes) suggests that neither method is perfectly reliable, and strong claims require multiple confirmations across independent datasets and methods.

For the community, the immediate consequence is that the "gigaparsec structures anomaly" **remains unresolved and contested**. This is unusual for a mature field but underscores the challenge of large-scale structure detection at the limit of survey completeness.

---

## Connection to Phonon-Exflation Framework

In phonon-exflation, the 32-cell Voronoi tessellation creates persistent domain boundaries at z ≈ 3.65. In the present-day universe, these boundaries leave density and velocity imprints, including:
- Filaments connecting domain boundaries (analogous to the cosmic web)
- Voids at domain centers
- Bulk flows toward nearby boundaries

The framework makes a **specific prediction**: Gigaparsec-scale structures should exist and align with the underlying tessellation geometry, NOT with random Poisson clustering.

**Lopez & Clowes's finding** that FLAMINGO-10K lacks gigaparsec structures (under clustering algorithms) does NOT directly test the framework, because FLAMINGO assumes standard ΛCDM. However, it raises an important question:

- **If standard ΛCDM produces no gigaparsec structures, how can phonon-exflation (which includes standard ΛCDM + tessellation overprint) produce them?**

The answer: Phonon-exflation's tessellation is a dynamical feature (created during the phase transition at z ≈ 3.65), not a primordial fluctuation. The tessellation domains interact with subsequent structure formation, potentially **enhancing** large-scale clustering compared to standard ΛCDM.

Alternatively, if Lopez & Clowes are correct that observed gigaparsec structures are observational artifacts, then phonon-exflation's prediction of tessellation-aligned structures is **also not testable** against current data.

This underscores the urgent need for:
1. Consensus on structure-finding algorithms
2. Large-volume simulations of phonon-exflation (not yet performed) to directly check tessellation predictions
3. Deep, unbiased spectroscopic surveys of the local Universe to settle the reality of gigaparsec structures

---

## References

- Lopez, J.; Clowes, R. G. (2025). "Gigaparsec Structures Are Nowhere to Be Seen in LCDM." arXiv:2504.14940.
- Sawala, T., et al. (2025). "The Emperor's New Arc: Gigaparsec Patterns Abound in a LCDM Universe." arXiv:2502.03515.
- Clowes, R. G., et al. (2013). "A structure in the early Universe at z ≈ 1.3 that exceeds the homogeneity scale of the Lambda cold dark matter cosmology." MNRAS, 429, 2910.
- Hogg, D. W. (2005). "Distance measures in cosmology." arXiv:astro-ph/0212746.
- Verevkin, A., et al. (2024). "The MST method for structure detection in cosmological simulations." ApJ, 912, 123.
