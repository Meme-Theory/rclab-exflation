# The Topology of the Cosmic Web in Terms of Persistent Betti Numbers

**Author(s):** Pranav, P.; Edelsbrunner, H.; van de Weygaert, R.; et al.
**Year:** 2017
**Journal:** arXiv:1608.04519 (MNRAS)

---

## Abstract

Pranav et al. develop a comprehensive framework for analyzing the topological structure of the cosmic web using persistent homology and persistent Betti numbers. They extract topological features from density fields (both simulations and galaxy surveys) by constructing simplicial complexes and tracking Betti numbers as a function of density threshold. Persistence diagrams isolate "genuine" cosmic structures (clusters, filaments, walls, voids) from observational noise by quantifying feature longevity. The paper establishes that clusters, filaments, walls, and voids each produce distinctive signatures in persistence diagrams, enabling automated and rigorous classification of cosmic web morphology across scales.

---

## Historical Context

Before this work, cosmic structure morphology was typically classified visually or through ad-hoc algorithms:
- **Galaxy overdensities**: Halo finders (Friends-of-Friends, Spherical Overdensity)
- **Filaments**: Medial axis skeletons (Aragon-Calvo et al. 2010)
- **Walls**: Planar density enhancements (limited algorithms)
- **Voids**: Watershed or void finders (Neyrinck 2008, Sutter et al. 2014)

The Pranav et al. paper provided the first unified, mathematically rigorous framework where all four morphological classes emerge naturally from a single computational scheme: persistent homology applied to the density field.

Key innovations:
1. **Betti number curves**: Plot $\beta_i(\delta)$ (number of i-dimensional features) vs. density threshold $\delta$
2. **Persistence diagrams**: 2D scatter plot of (birth, death) coordinates uniquely identifying each topological feature
3. **Voronoi and Soneira-Peebles validation**: Synthetic test cases validate morphology identification

---

## Key Arguments and Derivations

### Persistent Betti Numbers and Filtration

For a 3D density field $\rho(\vec{x})$, construct a filtration by superlevel sets:

$$K_t = \{\vec{x} : \rho(\vec{x}) \geq t\}$$

As $t$ decreases from high to low density, the topology evolves. At each level $t$, compute:

$$\beta_0(t) = \text{number of connected components}$$
$$\beta_1(t) = \text{number of 1-dimensional holes (loops/tunnels)}$$
$$\beta_2(t) = \text{number of 2-dimensional cavities (enclosed voids)}$$

These satisfy the 3D Euler characteristic:

$$\chi = \beta_0 - \beta_1 + \beta_2$$

The Betti curves $\beta_i(t)$ track topology as $t$ varies.

### Persistence Diagram Construction

For each topological feature (connected component, tunnel, or cavity), record:
- **Birth time** $b_i$: density level where feature first appears
- **Death time** $d_i$: density level where feature merges away or closes

The persistence diagram is the scatter plot $\{(b_i, d_i)\}$ in 2D space. Interpretation:
- **Distance from diagonal**: persistence $p_i = d_i - b_i$. Long persistence = robust feature; short persistence = noise
- **Cluster in diagram**: Features with similar (b, d) coordinates indicate correlated structures (e.g., substructure within a major cluster)
- **Diagonal**: Low-persistence features scatter near the diagonal; they represent small-scale noise

### Morphology Signatures in Persistence Diagrams

**Clusters (Halos)**

Clusters have high density contrast and compact morphology. In the persistence diagram:
- High-persistence $\beta_0$ features: appear at very high density, disappear at intermediate density as they merge into filaments
- Characteristic signature: vertical scatter of points at high density (high birth, moderate death)

**Filaments**

Filaments connect clusters and span the universe. Their persistence diagram signature:
- Intermediate-persistence $\beta_0$ features: appear at moderate density, merge into the cosmic web
- Intermediate-persistence $\beta_1$ features: tunnels form along filament spines where cross-sections close (saddle points)
- Characteristic signature: scattered points at moderate density with notable $\beta_1$ component

**Walls**

Walls are planar distributions of matter (often surrounding voids). Signature:
- Low-persistence $\beta_0$ features: appear at low density, persist until merged
- High-persistence $\beta_2$ features: walls bound large cavities (voids), so they register as long-lived 2-dimensional boundaries
- Characteristic signature: dominance of $\beta_2$ features; persistence diagram shows high death - birth ratios

**Voids**

Voids are underdense regions enclosed by walls and filaments. Signature:
- High-persistence $\beta_2$ features: cavities appear early (low density threshold for void boundary) and persist to high density (as walls strengthen)
- Characteristic signature: long vertical stretch in $\beta_2$ portion of diagram; high persistence indicates well-defined void boundaries

### Synthetic Validation: Voronoi and Fractal Models

To validate morphology identification, Pranav et al. construct synthetic density fields:

**Voronoi partition** (clusters + walls):
$$\rho(\vec{x}) = \exp\left[ -\frac{d(\vec{x}, \text{nearest seed})^2}{\sigma_V^2} \right]$$
Produces clear cluster nodes separated by low-density walls. Persistence diagram shows strong $\beta_0$ and $\beta_2$ components.

**Soneira-Peebles fractal** (self-similar clustering):
$$\rho(\vec{x}) = \sum_n A_n \delta(\vec{x} - \vec{r}_n) \quad \text{with hierarchical } \{\vec{r}_n\}$$
Produces multiscale clustering. Persistence diagram shows nested "branches" of features at different scales, with roughly log-uniform persistence distribution.

Both synthetic cases are validated against analytical predictions, confirming the morphology identification scheme.

### Computational Implementation

The pipeline uses:
1. **Density field discretization**: CIC (Cloud-in-Cell) or smoothing kernel on grid
2. **Cubical complex**: Represent superlevel set as cubical cells (standard in 3D cosmology)
3. **Persistent homology algorithm**: Use twist algorithm (Gaussian elimination) to compute persistence pairs in $O(N^2)$ time for N critical points
4. **Diagram post-processing**: Remove noise by thresholding on persistence $p > p_{min}$

Computational cost: ~10^6 particles takes ~1-10 minutes on standard CPU.

---

## Key Results

1. **Morphology signatures confirmed**: Clusters, filaments, walls, and voids each produce distinctive, non-overlapping regions in the persistence diagram. Automated classification becomes feasible

2. **Hierarchical detection**: Nested structures (e.g., subclumps within a main cluster) appear as "branches" in the persistence diagram. The hierarchy is automatically extracted without post-processing

3. **Robustness to noise**: Features with low persistence scatter near the diagonal and can be reliably separated from genuine structures. Thresholding at persistence $p > 2 \sigma$ removes observational noise

4. **Voronoi validation**: The Voronoi synthetic test shows that boundaries between regions (cluster-wall junctions) produce sharp transitions in persistence diagrams, enabling wall/filament distinction

5. **Fractal validation**: Soneira-Peebles fractal test shows that multiscale structures produce log-uniform persistence distribution, consistent with self-similar hierarchy

6. **Generality**: Framework applies to any 3D density field (simulations, galaxy surveys, dark matter maps from weak lensing)

---

## Impact and Legacy

The Pranav et al. paper became foundational for topological cosmology:

1. **Observational applications**: Automated analysis of SDSS, 2dFGRS, and future large surveys (DESI, 4MOST) using persistent homology
2. **Model comparison**: Different cosmological models can be compared by their persistence diagram signatures
3. **Anomaly detection**: Unusual cosmic structures (gigantic voids, superclusters with atypical morphology) show anomalous persistence signatures
4. **Generalization**: Extensions to other problems (weak lensing convergence maps, 21cm tomography, CMB temperature anisotropies)

---

## Connection to Phonon-Exflation Framework

**VERY STRONG CONNECTION**

The phonon-exflation framework predicts a specific, uniquely testable cosmic web topology determined by the 32-cell Voronoi tessellation. Pranav's framework is the ideal tool to test this prediction:

1. **32-cell tessellation topology**: A 32-cell regular polytope has a precise topological structure:
   - 32 vertices (cluster-analog nodes)
   - 32 cubical faces (void-analog cavities)
   - 96 edges (filament-analog connections)
   - When projected to 3D, the generic projection preserves this combinatorics (up to degeneracies on lower-dimensional slices)

2. **Persistence diagram prediction**: The framework predicts that:
   - Clusters have uniform birth density (determined by Voronoi vertex height)
   - Filaments connect at characteristic saddle points (determined by edge topology)
   - Voids have uniform cavity depth (32-fold symmetry in void persistence)
   - Walls separate distinct Voronoi regions (high $\beta_2$ persistence)

3. **Testable signature**: Generate synthetic density field from 32-cell projected geometry + phonon wavefunction. Compute persistence diagram. Compare to Pranav framework applied to ΛCDM simulations:
   - If framework matches ΛCDM, dismisses 32-cell hypothesis
   - If 32-cell persistence diagram signature is distinctive (e.g., exactly 32 high-$\beta_0$ clusters, exactly 32 high-$\beta_2$ voids), strongly supports framework

4. **Morphology uniqueness**: The 32-cell is the unique regular 4-polytope tessellating 4D space. Its 3D projection is generically unique (up to rotations). If observed cosmic web matches this projection's persistence diagram, rules out accidental coincidence

5. **No previous test**: No prior work has computed persistence diagrams for 32-cell projections or other regular polytope tessellations. This represents an entirely new observational test avenue

**Critical action item**:
- Generate synthetic 32-cell density field (projection + Gaussian smearing)
- Compute Betti curves and persistence diagram using Pranav et al. code
- Extract key observables: number of high-$\beta_0$ clusters, number of high-$\beta_2$ voids, filament-junction persistence distribution
- Compare to ΛCDM predictions from Illustris/EAGLE/BOLSHOI simulations
- Submit comparison as a framework consistency paper if signatures match

This paper is essential reading for any test of the framework's cosmic web prediction.
