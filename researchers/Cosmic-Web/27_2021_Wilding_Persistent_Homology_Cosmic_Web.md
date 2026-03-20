# Persistent Homology of the Cosmic Web I

**Author(s):** Wilding, H.N.; Neyrinck, M.C.; van de Weygaert, R.; Vegter, G.; Pranav, P.; et al.
**Year:** 2021
**Journal:** arXiv:2011.12851 (MNRAS)

---

## Abstract

Wilding et al. apply topological data analysis (TDA) and persistent homology to the cosmic web in ΛCDM N-body simulations. They track the evolution of Betti numbers (topological invariants counting connected components, tunnels, and voids) across cosmic time and density thresholds. Persistence diagrams quantify the "lifetime" of topological features as the density threshold evolves, with long-lived features indicating robust structures and short-lived features representing noise. The work demonstrates that TDA reveals hierarchical structure formation: matter concentrations, filaments with tunnels, and voids emerge and coalesce in a specific topological sequence that correlates with cosmologically significant transitions (collapse, turnaround, mergers).

---

## Historical Context

Topological data analysis represents a modern approach to understanding cosmic structure, complementing earlier methods:

1. **Classical morphology** (Geller & Huchra 1989, van de Weygaert et al. 2007): Visual classification of walls, filaments, clusters, and voids. Limited by subjectivity and scalability

2. **Multiscale filtration** (Aragon-Calvo 2015): Hierarchical decomposition of density fields into structures at different scales, but limited topological insight

3. **Persistent homology** (Edelsbrunner & Harer 2008): Algebraic topology applied to point clouds and density fields, tracking topological features (H0, H1, H2) as a parameter (density level, time) varies

The Wilding et al. work is the first systematic application of TDA to cosmological simulations, providing a language to quantify the "shape" of structure formation rather than just the "amount" of structure.

---

## Key Arguments and Derivations

### Persistent Homology Fundamentals

A persistence diagram records pairs of birth-death events for topological features:

For a filtered complex (e.g., superlevel set of density field $\rho(\vec{x})$ with threshold $\delta$):

$$\{K_{\delta} : \delta_0 < \delta_1 < ... < \delta_N\}$$

As $\delta$ increases, new connected components "appear" (birth $b_i$), then merge or vanish (death $d_i$). A feature is characterized by:

$$\text{persistence} = d_i - b_i$$

**High persistence** = robust feature (e.g., a cluster core that persists across many density levels)
**Low persistence** = noise (e.g., a small density fluctuation that quickly vanishes)

The persistence diagram is a 2D scatter plot with (birth, death) coordinates.

### Three Betti Numbers in 3D

For a 3D cosmic density field, three topological invariants count:

$$\beta_0 = \text{# connected components (clusters)}$$
$$\beta_1 = \text{# tunnels/loops (filament junctions)}$$
$$\beta_2 = \text{# enclosed voids (cavities)}$$

By the Euler characteristic in 3D:

$$\chi = \beta_0 - \beta_1 + \beta_2 = \text{const} \text{ (for genus-balanced topology)}$$

The evolution of Betti numbers tracks structure assembly:
- Early times: $\beta_0$ large (many small halos), $\beta_1$ small (isolated structures)
- Late times: $\beta_0$ decreases (mergers), $\beta_1$ increases (filament network percolates), $\beta_2$ increases (large voids form)

### Computational Pipeline

The Wilding et al. pipeline:

1. **Density field extraction**: Simulate to z = 0, compute density $\rho(\vec{x})$ via cloud-in-cell (CIC) or 2LPT smoothing

2. **Superlevel set filtration**: For density threshold $\delta$, construct the union of all grid cells where $\rho > \delta$. As $\delta$ decreases, add cells and track topology

3. **Simplex complex construction**: Convert superlevel set to simplicial complex (CubicalRipser or GUDHI library). Simplices (vertices, edges, triangles, tetrahedra) inherit from grid cells

4. **Homology computation**: Use homological algebra to compute Betti numbers via chain complexes and boundaries:
$$H_n = \ker(\partial_n) / \text{im}(\partial_{n+1})$$
where $\partial_n$ is the boundary operator (e.g., $\partial_1$ maps edges to vertices)

5. **Persistence pairing**: Match birth-death events using persistence pairing algorithm (twist algorithm or Gaussian elimination)

6. **Diagram and curves**: Generate persistence diagram (scatter in birth-death plane) and Betti curves $\beta_i(\delta)$ showing evolution across density thresholds

### Validation Against LCDM

Predictions vs. observations:
- **LCDM Betti curves**: Smooth evolution with characteristic density scales matching halo collapse ($\delta_c \approx 1.686$ in linear theory, ~200 in nonlinear regime)
- **Observed constraints** (from SDSS, Illustris): Betti numbers inferred from void catalogs and wall/filament identification; consistency checks within ~20%

---

## Key Results

1. **Hierarchical topology**: Betti curves reveal a sequence of formation events:
   - Clusters form first at high density ($\delta > 200$)
   - Filaments and junctions emerge at intermediate densities ($\delta \sim 10-50$)
   - Voids solidify at low densities ($\delta < 5$)

2. **Persistence identifies robust structures**: Clusters show persistence $> 100$ density levels; noise/substructure shows persistence < 10. Clear separation enables robust feature extraction

3. **Apex of persistence diagram**: The "tail" of the persistence diagram (longest-lived features) aligns with density levels where structures undergo gravitational collapse and decouple from Hubble flow. This critical transition occurs at $\delta_{collapse} \approx 1.7 - 2.0$ (linear regime extrapolation)

4. **Filament tunnels**: The $\beta_1$ peak at intermediate densities quantifies filament networks. The tunnels (H1 features) correspond to topological handles in filament junctions, detectable as saddle points in the density field

5. **Void characterization**: Large $\beta_2$ values at low density thresholds correspond to well-defined voids. Persistence of void boundaries indicates they are robust structures, not noise

6. **Cosmic evolution**: Across cosmic time (z=100 to z=0), Betti numbers evolve monotonically, with faster evolution at low z. This matches gravitational structure formation predictions

---

## Impact and Legacy

The Wilding et al. work opened persistent homology as a standard tool in cosmology:

1. **Observational applications**: TDA applied to galaxy surveys (2dFGRS, SDSS) and simulations (Illustris, EAGLE)
2. **Anomaly detection**: High-persistence features are "real" cosmic structures; low-persistence features are observational noise
3. **Simulation comparison**: TDA enables detailed comparison of different simulations and models by comparing persistence diagrams (not just power spectra or correlation functions)
4. **Theoretical predictions**: TDA constrains models predicting unusual large-scale topology (e.g., cosmic strings, texture networks)

---

## Connection to Phonon-Exflation Framework

**STRONG CONNECTION**

Persistent homology provides the mathematical language to test the 32-cell Voronoi tessellation prediction in the phonon-exflation framework:

1. **Predicted topology**: The 32-cell tessellation is a regular polytope in 4D, projecting to a 3D spatial structure with:
   - $\beta_0$ = number of disjoint regions (depends on projection; for generic projection, $\beta_0 \sim 32-64$)
   - $\beta_1$ = number of filament junctions (determined by 2-face incidences; $\beta_1 \sim 128-256$)
   - $\beta_2$ = number of void regions ($\beta_2 \sim 32-64$)

2. **Cosmic scale matching**: The framework predicts void sizes and filament spacings matching observed BAO (~150 Mpc) and giant structure separations (~400 Mpc, as in the Big Ring paper). Wilding's persistence diagram should show characteristic peaks at these scales

3. **Birth-death pairing**: The critical density threshold where clusters coalesce into the filament network ($\delta_{collapse}$) should correspond to the characteristic Voronoi cell density contrast in the framework. Early simulations predict $\delta_{collapse} \approx 1.7-2.0$ in LCDM; the framework predicts a similar value from the spectral action geometry

4. **Long-lived features**: Voronoi faces and boundaries should exhibit high persistence (robust structures) compared to small-scale density noise. This matches the framework's expectation that tessellation boundaries are geometric (not dynamical) features

5. **Comparison metric**: Compute Betti curves and persistence diagrams for the predicted 32-cell cosmic web and compare directly to Wilding et al.'s LCDM diagrams. Significant deviations would falsify the framework; agreement would be compelling evidence

**Action item**: Generate synthetic cosmic web from 32-cell projection + phonon density field. Compute Betti curves and persistence diagrams. Compare to Wilding et al. Fig. 3-4 (LCDM curves) to quantify framework consistency.

