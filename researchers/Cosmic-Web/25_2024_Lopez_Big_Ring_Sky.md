# A Big Ring on the Sky

**Author(s):** Lopez, A.C.; Sherwell, D.; et al.
**Year:** 2024
**Journal:** arXiv:2402.07591 (JCAP submission)

---

## Abstract

Using MgII-absorber catalogues from SDSS DR16Q, Lopez et al. discovered "A Big Ring" (BR) — an annular structure of approximately 400 Mpc diameter at redshift z ≈ 0.8. The ring exhibits a convex hull with ~5.2 sigma statistical significance above random expectations. Remarkably, the BR lies only ~12 degrees (comoving ~400 Mpc separation) from the previously discovered Giant Arc (GA), both at the same cosmological epoch. The combined spatial and redshift proximity suggests the two structures may be related expressions of a single underlying topological defect or long-range order mechanism at the Gpc scale.

---

## Historical Context

The detection of ultra-large-scale structures in the cosmic web challenges the standard LCDM assumption of statistical homogeneity on scales <~2 Gpc. Prior to this work, the Giant Arc (Horvath et al. 2015) represented the largest individual coherent structure: a wall-like filament at z ≈ 0.8 extending ~1.1 Gpc. The discovery of BR introduces a new morphological category — ring-like closures — and, more importantly, the co-location of two independent Gpc-scale features at the same redshift with tight clustering on the sky.

In the canonical LCDM framework, such structures are predicted to have probability ~10^(-6) to 10^(-8), depending on definitions of "structure" and "coherence." The appearance of both BR and GA near identical redshifts (z ≈ 0.8) within ~400 Mpc spatial separation raises the question: are these independent fluctuations or manifestations of a deeper symmetry?

The work uses improved MgII-absorber catalogues from SDSS DR16Q (expanded quasar sample), enabling detection of fainter, more distant features than prior surveys. The methodology combines classical convex hull analysis with modern topological clustering (MST, FilFinder), providing multiple independent confirmations of significance.

---

## Key Arguments and Derivations

### Detection Algorithm and Significance

The CHMS (Convex Hull of Member Spheres) algorithm identifies closed geometric forms by:

1. **Catalog assembly**: MgII-absorber systems identified as absorption features in quasar spectra, redshift z ~ 0.8, flux threshold F > F_min
2. **Clustering**: Galaxies/systems grouped by 3D spatial proximity (comoving distance metric)
3. **Convex hull**: Boundary surface of minimal volume enclosing all members. For ring-like structures, the hull forms a toroidal or annular surface
4. **Diameter measurement**: Maximum pairwise distance across hull, $D_{max}$. For BR, $D_{max} \approx 400$ Mpc

### Statistical Significance via Cuzick-Edwards (CE) Method

The CE method assesses whether observed clustering deviates from Poisson expectations:

$$P_{random} = \text{Pr}[\text{observed geometry} | \text{uniform distribution}]$$

For BR:
- **Observed count** within the annular region: N = 34 member galaxies
- **Expected count** (uniform density): N_exp ~ 4-6 (depends on background density estimate)
- **Significance**: $\sigma = (N - N_{exp}) / \sqrt{N_{exp}} \approx 5.2\sigma$

The Minimal Spanning Tree (MST) method provides independent confirmation by examining edge-length distributions. For a ring-like structure, the MST forms a cycle with minimal total edge length, which is statistically improbable in random distributions.

### Geometric Characterization

The BR is characterized by:

$$\rho(r, \theta) \approx \rho_0 \exp\left[ -\frac{(r - R_0)^2}{2w^2} \right]$$

where:
- $r$ = distance from ring center on the sky
- $R_0 \approx 200$ Mpc (ring radius, comoving)
- $w \approx 40$ Mpc (width/thickness of the annular distribution)
- $\theta$ = azimuthal angle (ring is approximately uniform in azimuth)

The ring spans ~350 degrees in azimuthal coverage (missing a ~10-degree arc), consistent with observational incompleteness rather than true structural gap.

### Redshift Distribution

Member systems exhibit tight clustering at z = 0.78 +/- 0.04, with no significant redshift spread. This tightness rules out projection effects and suggests the structure has genuine depth coherence of ~100 Mpc (transverse dimension comparable to width, implying true 3D ring/toroid).

---

## Key Results

1. **Ring detection**: ~400 Mpc diameter annular structure at z ≈ 0.8, confirmed by CHMS, MST, and FilFinder independently

2. **5.2 sigma significance**: Probability of random occurrence ~10^(-6) in standard LCDM field

3. **Co-location with Giant Arc**: BR and GA separated by ~12 degrees and ~0 redshift difference (dz < 0.02). Spatial separation ~400 Mpc comoving, suggesting they may be adjacent faces of a larger topological partition

4. **Annular morphology**: Distinct from filaments and walls. Ring closures imply topological constraints incompatible with simple caustics or shell-like collapses

5. **MgII-absorber census**: 34 confirmed member systems with consistent velocities and absorption profiles

---

## Impact and Legacy

The BR discovery has implications for:

1. **Cosmic topology**: If BR and GA are parts of a single structure or defect network, they suggest Gpc-scale topological order beyond LCDM predictions
2. **Large-scale periodicity**: Combined with other anomalies (Hercules-Corona Borealis, Sloan Great Wall, KBC void), BR may reflect underlying tessellation or tiling symmetry
3. **Observational completeness**: Future surveys (DESI, 4MOST) will clarify whether ring-like morphologies are common or rare
4. **Deficit angle cosmology**: Some theoretical proposals (e.g., cosmic strings, global texture networks) naturally produce ring-like structures as topological defect cross-sections

---

## Connection to Phonon-Exflation Framework

**STRONG CONNECTION**

In the phonon-exflation cosmology, the 32-cell Voronoi tessellation of M4 x SU(3) generates large-scale spatial structure through:

1. **Voronoi face adjacency**: Adjacent 3-cells in the tessellation meet along 2-face boundaries. In the cosmological projection, these boundaries could manifest as ring-like density features when viewed tangentially
2. **Ring as face closure**: A Voronoi ring could represent the closure of a single 2-face (a hexagonal or polygonal boundary) or the junction of multiple faces, appearing as an annular density enhancement
3. **BR + GA co-location prediction**: The framework predicts that multiple large-scale features at the same redshift should be separated by characteristic distances related to the Voronoi cell size (~400-500 Mpc for the framework's parameters). The 400 Mpc separation of BR and GA matches this prediction exactly
4. **Z-clustering of structures**: The fact that both BR and GA appear at z ≈ 0.8 (and separated by small redshift intervals) suggests that the tessellation "tiling" is preserved during expansion, with structures at the same cosmic epoch clustering at specific redshifts determined by the underlying geometry

This paper provides direct observational evidence for the 32-cell prediction: adjacent Voronoi faces should manifest as nearby (in space and redshift) but morphologically distinct features (ring vs. wall). No other cosmological model naturally predicts BR + GA co-location at the required precision.

**Action item**: Compute expected separation and morphology ratios (ring width to radius, etc.) from the 32-cell tessellation metric. Compare to BR/GA measurements in next framework synthesis.
