# ASTRA: Cosmic Web Classification through Stochastic Topological Ranking

**Author(s):** Authors: Various; Primary contact: N. Porqueres, D. Alonso
**Year:** 2024
**Journal:** RASTI (accepted); arXiv:2404.01124

---

## Abstract

We present ASTRA (stochastic topological ranking applied to the cosmic web), a novel algorithm for classifying the cosmic web into four environments: voids, sheets, filaments, and knots. The key innovation is the use of random tracers to identify underdense regions, enabling robust void detection even in sparsely sampled survey geometries. Unlike traditional density-based classifiers, ASTRA operates directly on galaxy positions without interpolation to a density field. We validate ASTRA on N-body simulations (Illustris, EAGLE, TNG), SDSS observational data, and DESI-like synthetic catalogs. Void catalogs from ASTRA follow the Sheth-van de Weygaert theoretical size function predictions to within 5% accuracy across scales $R_v \in [10, 100] \, h^{-1}\text{Mpc}$. We demonstrate application to DESI DR2 data, classifying 7 million galaxies into cosmic web environments. ASTRA is publicly available and scalable to next-generation surveys (Rubin LSST, Vera Rubin Observatory).

---

## Historical Context

The cosmic web—the large-scale structure of the universe consisting of voids, filaments, walls, and clusters—has fascinated cosmologists since computer simulations revealed its ubiquity in the 1980s. Early classifications used density-based methods: computing a smoothed density field via Gaussian kernel or Delaunay tessellation, then assigning each point to an environment based on density threshold. However, density-based classifiers suffer from three systematic problems.

First, **sampling bias**: spectroscopic surveys don't sample all matter, only high-mass halos and their galaxies. Voids are by definition underdense in galaxies, so void interiors are often poorly sampled. A density estimator trained on galaxy positions underestimates the void-interior density, making it difficult to distinguish true voids from low-density filament regions.

Second, **kernel dependence**: the choice of smoothing kernel (Gaussian vs. tophat) and kernel scale ($\sigma = 2, 5, 10 \, h^{-1}\text{Mpc}$) substantially affects classification. There is no principled way to choose these hyperparameters a priori, leading to survey-dependent and group-dependent variations in cosmic web classification.

Third, **boundary ambiguity**: environments are classified using fixed density thresholds (e.g., "filament if $0.5 < \rho/\bar{\rho} < 2$"), but these thresholds are somewhat arbitrary. Different papers use different values, making literature comparisons difficult.

ASTRA addresses these problems through a radically different approach: **stochastic topological ranking**. Instead of computing density at each point, ASTRA examines the local topology of the galaxy point set using random tracers. The method is inspired by the theory of cosmic void formation and the notion that voids are defined not by density alone, but by their topological properties (connectedness, isolation, size).

Prior cosmic web classifiers (NEXUS, COSMIC WEB CONSTRUCTION, ORIGAMI) used geometrical or topological methods but required density field interpolation or were sensitive to kernel choice. ASTRA is the first to use random tracers directly, achieving both robustness and speed.

---

## Key Arguments and Derivations

### Void Definition via Random Tracers

The classical definition of a void is a connected region of space where density is below threshold $\rho < \rho_\text{th}$. However, in a point sample (galaxy positions), density is poorly defined in sparse regions. ASTRA bypasses this by using **Voronoi cells** and **random point distributions**.

For a set of galaxy positions $\{\vec{r}_i\}$ in a survey, the Voronoi diagram partitions space into cells, one per galaxy. The Voronoi cell of galaxy $i$ is the set of all points closer to $\vec{r}_i$ than to any other galaxy:

$$V_i = \{\vec{r} : |\vec{r} - \vec{r}_i| < |\vec{r} - \vec{r}_j| \, \forall j \neq i\}$$

The **Delaunay triangulation** is the dual of the Voronoi diagram: it connects galaxies that have adjacent Voronoi cells. The Delaunay faces (triangles in 3D) represent topological neighborhoods.

ASTRA's key insight is to overlay a **random point set** (Poisson distribution with density $\bar{\rho}$) on top of the galaxy survey. For each random point, ASTRA computes which galaxy Voronoi cell it falls into. In dense regions (clusters, filaments), random points are distributed uniformly across many galaxy cells. In sparse regions (voids), few random points fall into any single galaxy cell, and the random points that do exist form a sparse, disconnected set.

This leads to the **topological ranking**: galaxies whose Voronoi cells contain many random points are classified as high-density (knots, filaments); galaxies with few random points are classified as low-density (voids, sheets).

### Stochastic Ranking Algorithm

Let $n_\text{rand}(i)$ be the number of random tracers in the Voronoi cell of galaxy $i$. The expected value is:

$$\langle n_\text{rand}(i) \rangle = \frac{\text{(volume of cell)} \times \rho_\text{random}}{\text{(number of cells)}}$$

For a uniform distribution, $\langle n_\text{rand}(i) \rangle \propto V_i \bar{\rho}$.

The **rank** of galaxy $i$ is defined as its percentile in the distribution of $n_\text{rand}$:

$$\text{rank}(i) = \frac{\#\{j : n_\text{rand}(j) \leq n_\text{rand}(i)\}}{N_\text{gal}}$$

Galaxies with rank $< 0.2$ are classified as void environment (low density). Those with $0.2 < \text{rank} < 0.6$ are sheets. Those with $0.6 < \text{rank} < 0.9$ are filaments. Those with rank $> 0.9$ are knots (clusters).

To improve robustness, ASTRA repeats this calculation with multiple random catalogs (typically 5-10 realizations) and takes the **mean rank** across realizations. This averaging (the "stochastic" part of the name) suppresses noise from individual random point realizations.

### Void Identification and Size Function

Once galaxies are ranked as void environments (rank $< 0.2$), ASTRA groups connected void galaxies (using Delaunay adjacency) into **void clusters**. Each void cluster is a connected component of the void-ranked galaxy subset.

For each void cluster, a representative **void center** and **void radius** are computed:

- **Center**: center of mass of the void-ranked galaxies in the cluster, weighted by random point count (to emphasize the void interior).
- **Radius**: effective radius encompassing 68% of the void cluster's Voronoi cell volume.

The void size function $n(R_v)$ is constructed by binning the void radii and counting voids per unit volume:

$$n(R_v) = \frac{\text{number of voids with radius in } [R_v, R_v + dR_v]}{\text{comoving volume surveyed}}$$

ASTRA validates this against the theoretical Sheth-van de Weygaert prediction:

$$n_\text{SvdW}(R_v) \propto R_v^{-3} \exp(-\pi R_v^2 / R_*^2)$$

---

### Robustness to Survey Geometry

A key challenge in cosmic web classification is handling **survey boundary effects** and **selection functions**. A galaxy near the survey boundary might appear to be in a void simply because the survey doesn't extend far enough to see the surrounding overdensity.

ASTRA handles this by computing random tracers **within the survey footprint**. The random point distribution respects the survey mask (boundaries, magnitude limits, fiber collisions, etc.). Thus, if a galaxy is near the boundary and the random tracers also fail to probe beyond the boundary, the galaxy's rank reflects its true local environment given the available data.

Furthermore, ASTRA allows for **variable random point density** to mimic differential selection effects (e.g., fainter galaxies sampled at lower density). This makes ASTRA particularly suitable for spectroscopic surveys with complex selection functions.

---

### Classification Validation on Simulations

ASTRA is validated on three suites of N-body simulations:

1. **Illustris**: Hydrodynamical simulation with baryon physics. ASTRA identifies 1,200 voids per snapshot, with void size function agreeing with theory to 3%.

2. **EAGLE**: Another hydrodynamical suite. Void abundance and spatial distribution match SvdW predictions to within 2-5% across scales.

3. **TNG (The Next Generation)**: High-resolution MHD simulation. Void catalogs show robust agreement with void bias estimates from clustering (void bias $b_\text{void} \approx 0.25$, consistent across simulations).

On SDSS observational data, ASTRA identifies 2,000+ voids, with size function parameters ($R_* \approx 32 \, h^{-1}\text{Mpc}$, amplitude) matching simulation predictions.

---

## Key Results

1. **Void detection sensitivity**: ASTRA identifies voids with mean radius $\langle R_v \rangle = 24 \, h^{-1}\text{Mpc}$ in SDSS, compared to $22 \pm 3 \, h^{-1}\text{Mpc}$ in Illustris simulations.

2. **Size function accuracy**: ASTRA void size functions agree with theoretical SvdW predictions to within 5% across $R_v \in [10, 100] \, h^{-1}\text{Mpc}$.

3. **Void bias**: Void galaxies (rank $< 0.2$) have bias $b_\text{void} = 0.26 \pm 0.03$, consistent with theory and prior void studies.

4. **Environmental statistics**: Galaxy properties (star formation rate, morphology, color) show clear stratification across ASTRA-classified environments: star formation is suppressed in void-ranked galaxies and enhanced in knot-ranked galaxies.

5. **Filament structure**: Filament-ranked galaxies (rank $0.6-0.9$) show coherent alignment with the large-scale matter distribution, consistent with hydrodynamical simulation filaments.

6. **Application to DESI DR2**: ASTRA classifies 7 million galaxies in the DESI footprint, identifying 8,500+ voids, 120,000+ filament segments, and 500+ knot clusters.

7. **Computational speed**: ASTRA runs in $\approx 1$ minute for 1 million galaxies on a single CPU core, making it practical for large surveys.

8. **Stochasticity robustness**: Using 5-10 random catalog realizations reduces classification variance by factor of $\approx 50$ compared to single realization.

---

## Impact and Legacy

ASTRA has become the de facto standard for cosmic web classification in spectroscopic surveys. Its adoption by the DESI collaboration (DR2 public data release) gives it immediate impact. Three follow-up developments have emerged:

1. **Void+filament+knot clustering**: Joint analysis of void and filament environments to constrain growth of structure (filament matter is biased differently than void matter).

2. **ASTRA+BAO**: Using ASTRA-classified voids and filaments to measure baryon acoustic oscillations with reduced systematic uncertainty (voids have higher BAO signal-to-noise than galaxies).

3. **Morphology-environment connection**: Using ASTRA environmental classification to study how galaxy morphology correlates with position in the cosmic web.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation model predicts a **tessellated, quasi-periodic matter distribution** arising from the 32-cell Voronoi partition of the compactified space. This would manifest observationally as:

1. **Regular void spacing**: If the phonon-exflation tessellation is real, voids should exhibit a characteristic length scale (the typical Voronoi cell size), leading to void sizes clustering around a modal radius $R_* \sim 30-40 \, h^{-1}\text{Mpc}$.

2. **Void uniformity**: Void environments classified by ASTRA should show unusual uniformity (void density profiles more symmetric and less disturbed by nearby structures) if they are rooted in the tessellation.

3. **Filament alignment**: Filament-ranked regions should align with Voronoi boundaries (edges of 3D Delaunay simplices). This would produce a characteristic **skeleton** of the cosmic web, distinct from the stochastic filament structure predicted by Gaussian initial conditions.

4. **Void correlation function**: Voids should show stronger correlation at specific separations (multiples of the Voronoi cell scale) if the tessellation is driving their positions.

ASTRA's void and filament catalogs (already public for DESI DR2) provide the first precision test of these predictions. A detailed statistical analysis of ASTRA void spacing and filament alignment against the phonon-exflation tessellation predictions would either **confirm the tessellation hypothesis or rule it out at high confidence**.

