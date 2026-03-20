# Causal Dynamical Triangulations: Emergent de Sitter Spacetime from Discrete Geometry (2005)

**Author:** Jan Ambjorn, Jerzy Jurkiewicz, Renate Loll
**Year:** 2005-2015 (active period); foundational work 2000-2005
**Source:** Ambjorn, J., Jurkiewicz, J., & Loll, R. (2005) "Reconstructing the Universe." Physical Review D 72: 064014; Loll, R. (2019) "Quantum Gravity from Causal Dynamical Triangulations." Classical and Quantum Gravity 37: 013002

---

## Abstract

Causal Dynamical Triangulations (CDT) is a lattice-based approach to quantum gravity that directly formulates gravity in terms of discrete spacetime geometry. Spacetime is triangulated into simplicial elements (tetrahedra in 3+1D), with metric structure encoding geometry. By summing over all possible triangulations (weighted by the Einstein-Hilbert action), one obtains a path integral for quantum gravity without requiring a background spacetime. Remarkably, this approach produces emergent de Sitter spacetime: from purely discrete, combinatorial rules, spacetime with the observed 4D structure, cosmic expansion, and approximately smooth metric spontaneously emerges. CDT is one of the few frameworks that claims to reproduce general relativity in the semiclassical limit, demonstrating that spacetime itself may be emergent from discrete quantum geometry.

---

## Historical Context

The path integral formulation of quantum gravity involves summing over all possible spacetime metrics:

$$Z = \int D[g] e^{i S[g] / \hbar}$$

This integral is non-renormalizable: divergences plague the calculation, and no finite answer emerges.

CDT, developed by Ambjorn, Jurkiewicz, and Loll (2000-2005), proposed a solution: discretize spacetime into a lattice of simplices, then sum over all possible lattice configurations. This regularization is non-perturbative and has no background metric.

Strikingly, when they implemented this numerically, they found that spacetime with our observed 4D structure spontaneously emerged—it was not imposed but naturally selected.

---

## Simplicial Triangulation and Causal Structure

### Simplicial Complex

A simplicial complex is a partition of spacetime into simplices (building blocks):
- 0-simplices: vertices (points)
- 1-simplices: edges (lines connecting vertices)
- 2-simplices: triangles
- 3-simplices: tetrahedra (in 3+1D spacetime, also called 4-simplices)

A triangulation covers the entire spacetime: every point belongs to at least one simplex.

### Causal Structure

Standard lattice quantum gravity (Regge calculus, Euclidean dynamical triangulations) has trouble implementing causality: the distinction between timelike, spacelike, and null directions becomes unclear on a discrete lattice.

CDT solves this by encoding causality explicitly: each simplex is labeled either "spacelike" or "timelike," and the lattice is constructed to maintain a global time-ordering. Spacelike simplices connect to spacelike simplices, timelike to timelike, respecting causality.

This constraint dramatically reduces the number of allowed triangulations (makes the sum finite and computable).

### Metric from Simplicial Geometry

The metric is reconstructed from edge lengths. In a simplicial complex, each edge has an assigned length. For a triangle with vertices $A$, $B$, $C$, if edge lengths are $\ell_{AB}, \ell_{BC}, \ell_{CA}$, the triangle's geometric properties (angles, area) follow from Euclidean geometry.

The full metric $g_{\mu\nu}(x)$ is constructed by aggregating local geometric information from all adjacent simplices.

---

## Path Integral and Partition Function

### Discretized Action

The Einstein-Hilbert action in terms of simplicial geometry becomes:

$$S = \sum_i \delta_i R_i + \lambda \sum_j \epsilon_j$$

where:
- $\delta_i$ is the deficit angle at edge $i$ (how much angle is "missing" around the edge due to curvature)
- $R_i$ is curvature contribution
- $\epsilon_j$ are areas of simplices
- $\lambda$ is a cosmological constant term

The sum is over all edges (accounting for curvature) and all simplices (area/volume).

### Partition Function

The partition function is:

$$Z = \sum_{\text{triangulations}} e^{-S_{\text{eff}}}$$

where the sum is over all allowed causal triangulations with a fixed number of simplices.

In the continuum limit ($N \to \infty$ simplices, lattice spacing $a \to 0$), this sum reconstructs the path integral of gravity:

$$Z = \int D[g] e^{-S_{\text{EH}}}$$

Numerically, they evaluate the sum using Monte Carlo methods, sampling over random triangulations.

---

## Emergence of de Sitter Spacetime

### Numerical Results

The remarkable discovery: when CDT is implemented numerically, a preferred geometry spontaneously emerges.

The most striking result comes from measuring the "spectral dimension" $d_s$ (how dimension changes with scale):

$$d_s = 2 - \frac{d \log N(r)}{d \log r}$$

(where $N(r)$ is the number of simplices within "distance" $r$)

The results:
- **Small scales** ($r < \ell_{\text{Planck}}$): $d_s \approx 2$ (approximately 2D)
- **Intermediate scales**: $d_s$ transitions from 2 to 4
- **Large scales** ($r > \ell_{\text{Planck}} \times 10^2$): $d_s \approx 4$ (4D spacetime)

This is remarkable: a 4D universe emerges from a purely combinatorial lattice model!

### de Sitter Background

At large scales, the emergent metric is approximately:

$$ds^2 = -dt^2 + \left(\frac{H_0}{\sqrt{3}}\right)^{-2} \cosh^2\left(\sqrt{3} H_0 t\right) (dx^2 + dy^2 + dz^2)$$

(de Sitter metric, spatially flat with exponential expansion)

The Hubble parameter $H_0$ emerges naturally from the theory—no fine-tuning of a cosmological constant needed.

### Timeline Foliation

Remarkably, a preferred foliation of spacetime into time-slices emerges. Each time-slice is approximately 3D and nearly flat. The foliation evolves smoothly from past to future—exactly the structure we observe.

This emergence of time and space structure is profound: space and time are not fundamental in CDT, but emerge from the quantum geometry.

---

## Spectral Dimension and Scale-Dependent Geometry

### Fractal Structure

The transition of spectral dimension from 2 to 4 suggests that spacetime has a fractal-like structure at intermediate scales. Near the Planck scale, geometry is 2D (like a membrane); at human/cosmic scales, it's 4D.

This scale-dependent dimensionality is characteristic of fractal geometry (where Hausdorff dimension differs from topological dimension at different scales).

### Implication for Particle Physics

A 2D structure at Planck scales has profound implications: interactions and wave propagation are different in 2D vs 4D. This could explain:
- Why gravity is so weak (it "spreads out" in 4D but is confined in 2D core)
- Structure of particle spectrum (determined by 2D geometry near Planck scale)
- Fundamental symmetries (which emerge from discrete geometry)

---

## Connection to Phonon-Exflation Framework

CDT provides strong support for the phonon-exflation framework in several ways:

1. **Emergent spacetime**: CDT demonstrates that 4D spacetime with metric structure can emerge from discrete, combinatorial geometry without being imposed. Phonon-exflation similarly posits that 4D spacetime emerges from M4 x SU(3)—spacetime is not fundamental. Both frameworks take emergence seriously.

2. **No inflaton field**: CDT produces cosmic expansion (de Sitter geometry) without an inflaton field. The expansion emerges from the causal structure and path integral weights. Phonon-exflation similarly avoids the inflaton: expansion is driven by internal compactification geometry (Jensen deformation), not a scalar field. Both provide mechanistic alternatives to inflation.

3. **Discrete underlying structure**: CDT is fundamentally discrete (simplicial lattice). Phonon-exflation is based on compactified geometry (SU(3) is discrete at Planck scale due to quantum geometry). Both reject the classical continuum assumption and embrace discrete quantum geometry.

4. **Dimension flow**: CDT exhibits dimension flow—the effective dimensionality changes with scale. In phonon-exflation, the Dirac spectrum on SU(3) changes structure as the metric parameter $s$ varies. This is analogous: geometry changes with scale/parameter, causing the effective dimension to shift.

5. **Simplices as quantum of geometry**: In CDT, simplices are the building blocks—the quanta of spacetime. In phonon-exflation, phonons are the quanta—excitations of the SU(3) geometry. Both frameworks identify fundamental quantum units (simplices, phonons) as the basic constituents.

6. **Natural cosmological constant**: CDT yields the correct magnitude of the cosmological constant without fine-tuning. Phonon-exflation similarly derives the cosmological constant from zero-point energy of the phonon spectrum. Both explain why the universe accelerates without exotic fields.

7. **Causal structure as fundamental**: CDT encodes causality in the lattice structure (timelike vs spacelike edges). Phonon-exflation, via the Dirac operator on spacetime (acting on M4 x SU(3)), also encodes causality in the geometric structure. Causality is emergent from geometry.

**Key connection**: Both CDT and phonon-exflation suggest that the universe's expansion and large-scale structure emerge from discrete quantum geometry at Planck scales, without requiring:
- Inflaton fields
- Fine-tuned initial conditions
- Additional scalar degrees of freedom

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Simplicial action | $S = \sum_i \delta_i R_i + \lambda \sum_j \epsilon_j$ | Discrete Einstein-Hilbert action |
| Partition function | $Z = \sum_{\text{triangulations}} e^{-S_{\text{eff}}}$ | Path integral over geometries |
| Spectral dimension | $d_s = 2 - \frac{d \ln N(r)}{d \ln r}$ | Scale-dependent effective dimension |
| de Sitter metric | $ds^2 = -dt^2 + e^{2Ht} d\vec{x}^2$ | Emergent large-scale geometry |
| Deficit angle | $\delta = 2\pi - \sum_{\text{adjacent angles}}$ | Discrete curvature measure |
| Hubble parameter | $H = \frac{d a}{dt} / a$ | Expansion rate (emergent from CDT) |

---

## Critical Assessment

**What holds up**:
- Mathematical framework is rigorous and well-defined
- Numerical simulations are reproducible and robust
- Emergence of 4D spacetime is remarkable and consistent
- de Sitter geometry matches observations (accelerating expansion)
- No background metric required (truly background-independent)

**What is challenging**:
- Computational limits restrict to relatively small systems (~100,000 simplices)
- Continuum limit (infinite simplices) is still formal; convergence not fully proven
- Connection to Standard Model is unclear (CDT doesn't yet include matter coupled consistently)
- Some ambiguities in how to implement causality and measure observables

**What is promising**:
- First concrete demonstration of emergent spacetime
- No inflaton or fine-tuning required
- Testable predictions (dimension flow, CMB) being developed
- Recently extended to include matter and gauge fields

---

## Legacy and Current Directions

CDT remains actively researched:

1. **Extension to matter**: Coupling fermions and gauge fields to CDT geometry
2. **Observational predictions**: Dimension flow effects in CMB and structure formation
3. **Black hole thermodynamics**: Using CDT to study black hole interiors
4. **Quantum criticality**: Studying the phase transitions in CDT as analogs of critical phenomena

---

## References

1. Ambjorn, J., Jurkiewicz, J., & Loll, R. (2005). "Reconstructing the universe." Physical Review D 72: 064014.
2. Loll, R. (2019). "Quantum gravity from causal dynamical triangulations: a review." Classical and Quantum Gravity 37: 013002.
3. Ambjorn, J., Jurkiewicz, J., & Loll, R. (2008). "The self-organized de Sitter universe." Physical Review Letters 100: 091304.
4. Glaser, L. & Steinhaus, S. (2016). "Quantum gravity on the computer: the search for quantum spacetime." Symmetry 8: 145.
5. Horava, P. (2009). "Quantum gravity at a Lifshitz point." Physical Review D 79: 084008. (Alternative discrete approach)
6. Carlip, S. (2017). "Dimension and dimensional reduction in quantum gravity." Universe 3: 76.
