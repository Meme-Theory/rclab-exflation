# Superconductivity in Hyperbolic Spaces

**Author(s):** Multiple authors
**Year:** 2025
**Journal:** arXiv preprint
**arXiv:** 2510.26528

---

## Abstract

BCS superconductivity is analyzed on negatively curved geometries (Cayley trees, hyperbolic planes, horodisc regions). The key finding: the superconducting order parameter localizes at boundaries, with edge superconductivity occurring at higher critical temperature than bulk superconductivity. The Bogoliubov-de Gennes equations are solved on discrete tree geometries and hyperbolic continua. Boundary density-of-states enhancement macroscopically stabilizes edge pairing even in the thermodynamic limit — a phenomenon distinct from flat-space BCS.

---

## Historical Context

Superconductivity in condensed matter physics is traditionally studied on flat (Euclidean) or periodic (lattice) geometries. The BCS theory (Bardeen-Cooper-Schrieffer) assumes a constant density of states $N(E_F)$ at the Fermi level and a uniform interaction strength.

However, curved space introduces geometry-dependent modifications:

1. **Density of States Anomalies**: In hyperbolic space, the density-of-states grows near boundaries due to the divergence of geodesics. This is a fundamental feature of negative curvature.

2. **Edge Effects in Topological Materials**: Recent discoveries of topological superconductors show that pairing can be enhanced at boundaries (topological surface states). Hyperbolic geometry naturally models such edge-localized phenomena.

3. **Kaluza-Klein on Curved Compactifications**: Our framework computes BCS pairing on the Jensen-deformed SU(3) manifold, which is positively curved but non-Euclidean. Understanding how curvature enters the BCS equations is essential.

This paper provides the first systematic treatment of BCS on curved spaces using hyperbolic geometry as a tractable test case.

---

## Key Arguments and Derivations

### Bogoliubov-de Gennes Equations on Curved Spaces

The standard BCS gap equation on flat space is:

$$\Delta(\mathbf{k}) = -g \sum_{\mathbf{k}'} \frac{\Delta(\mathbf{k}')}{2E(\mathbf{k}')} \tanh\left(\frac{E(\mathbf{k}')}{2T}\right)$$

where $g > 0$ is the pairing coupling, $\Delta$ is the order parameter, and $E(\mathbf{k}) = \sqrt{\xi(\mathbf{k})^2 + \Delta(\mathbf{k})^2}$ is the quasiparticle energy with $\xi(\mathbf{k}) = \epsilon(\mathbf{k}) - \mu$ the kinetic energy relative to chemical potential.

On a curved manifold $(M, g_{ij})$, the kinetic energy is:

$$\epsilon(\mathbf{p}) = \frac{g^{ij} p_i p_j}{2m}$$

where $g^{ij}$ is the inverse metric tensor and $p_i$ are canonical momenta conjugate to coordinates $x^i$ on the manifold.

The density of states at energy $E$ is:

$$N(E) = \int_M \frac{d^d x \sqrt{g}}{(2\pi)^d} \, \delta(E - \epsilon(\mathbf{p}))$$

where $\sqrt{g} = \det(g_{ij})^{1/2}$ is the metric volume factor. For a curved manifold, $N(E)$ depends on position $\mathbf{x}$ and the local metric geometry.

The Bogoliubov-de Gennes Hamiltonian becomes:

$$\mathcal{H}_{BdG} = \begin{pmatrix} -\nabla^2 - \mu & \Delta(\mathbf{x}) \\ \Delta^*(\mathbf{x}) & \nabla^2 + \mu \end{pmatrix}$$

where $\nabla^2 = g^{-1/2} \partial_i (g^{1/2} g^{ij} \partial_j)$ is the Laplacian on the curved manifold, with metric-dependent coefficients.

Eigenvalues $E_n$ of $\mathcal{H}_{BdG}$ determine the density of states:

$$N(E) = \sum_n \delta(E - E_n)$$

On flat space, $E_n = \sqrt{\epsilon_n^2 + \Delta^2}$. On curved spaces, $\epsilon_n$ depends on the Laplacian spectrum.

### Hyperbolic Geometry: The Poincare Disk Model

The hyperbolic plane $\mathbb{H}^2$ in the Poincare disk model has metric:

$$ds^2 = \frac{4(dx^2 + dy^2)}{(1 - x^2 - y^2)^2}$$

with $x^2 + y^2 < 1$. The Ricci curvature is $\text{Ric} = -2 g$ (negative definite).

The Laplacian in Poincare coordinates is:

$$\Delta u = \frac{(1 - x^2 - y^2)^2}{4} \partial_x^2 u + \text{(similar for } y)$$

For a radial function $u(r)$ (where $r = \sqrt{x^2 + y^2}$ is the distance from the center), the Laplacian becomes:

$$\Delta u = \frac{d^2 u}{dr^2} + \frac{1 - r^2}{r} \frac{du}{dr}$$

The eigenvalue equation $-\Delta u = \lambda u$ on the disk has spectrum $\lambda_n = (n + 1/2)^2$ for $n = 0, 1, 2, \ldots$, with eigenfunctions localized near the boundary at $r \to 1$.

### Density of States in Hyperbolic Geometry

On the hyperbolic plane, the density of states near energy $E$ is:

$$N(E) = \int_{\mathbb{H}^2} \frac{d^2 x \sqrt{g(x)}}{(2\pi)^2} \int \frac{dp_x dp_y}{(2\pi)^2} \delta\left(E - \frac{|p|^2}{2m}\right)$$

Because of the diverging volume element near the boundary ($\sqrt{g(x)} \to \infty$ as $r \to 1$), the density of states is enhanced at the boundary. More precisely, for a disk of radius $R$ (in hyperbolic distance units), the total "volume" is:

$$V(\text{disk}) = \int_0^R dr \int_0^{2\pi} d\theta \, r \sinh(r) \approx 2\pi \sinh(R)$$

which grows exponentially in $R$. Most of this volume is concentrated near $r = R$ (the boundary).

For a band of states with Fermi level $E_F$, the density-of-states is approximately:

$$N(E) \propto \int_{\partial M} dS \, \rho(E)_{\text{boundary}} + \int_M dV \, \rho(E)_{\text{bulk}}$$

The boundary contribution scales as $e^{R}$ (exponential in the disk radius), while the bulk contribution is polynomial. Thus, for large $R$, boundary effects dominate: **pairing is enhanced at the boundary**.

### Cayley Tree Analysis

A Cayley tree $C_k$ of branching number $k$ is a discrete version of hyperbolic space. Each site has $k$ neighbors (except the root, which has $k-1$). The coordination number grows exponentially with distance from the root, mimicking the expanding volume of hyperbolic space.

For a finite tree with $N$ sites, the density of states at site $n$ is computed via the local Green function:

$$G_n(E) = \langle n | (E - \mathcal{H})^{-1} | n \rangle$$

On a Cayley tree with uniform nearest-neighbor hopping $t$ and pairing potential $\Delta$, the Green function satisfies a self-consistency equation:

$$G_n(E) = \frac{1}{E - \Delta - k \cdot t \cdot G_{n+1}(E)}$$

where $G_{n+1}$ is the Green function at a neighboring site. For a semi-infinite tree (extending to infinity from the root), a closed form can be obtained by iteration.

The paper solves this for the Cayley tree with $k=3$ (tree of coordination 3), obtaining:

$$G_{\text{bulk}}(E) = \frac{E + \sqrt{E^2 - 4t^2(k-1)^2}}{2t^2(k-1)^2}$$

The density of states is $N(E) = -\frac{1}{\pi} \text{Im}[G(E + i0^+)]$. For $|E| < 2t\sqrt{k-1}$, $N(E)$ is real and large (van Hove singularity from the tree bandwidth). For $|E| > 2t\sqrt{k-1}$, $N(E) = 0$ (outside the band).

At the boundary of the tree (leaves), the coordination is reduced, yielding a different Green function and enhanced $N(E)$.

### Gap Equation on Hyperbolic/Tree Geometries

With spatially varying density of states $N_n(E)$ at site $n$, the gap equation becomes:

$$\Delta_n = -g \sum_m V_{nm} \int dE \, N_m(E) \, \frac{\Delta_m}{2\sqrt{\xi_m^2 + \Delta_m^2}} \tanh\left(\frac{\sqrt{\xi_m^2 + \Delta_m^2}}{2T}\right)$$

where $V_{nm}$ is the pairing vertex (on-site pairing in simplest case: $V_{nm} = \delta_{nm}$, no off-site pairing).

For a uniform coupling $g$, the equation decouples by site:

$$\Delta_n = -g \int dE \, N_n(E) \, \frac{\Delta_n}{2\sqrt{\xi_n^2 + \Delta_n^2}} \tanh\left(\frac{\sqrt{\xi_n^2 + \Delta_n^2}}{2T}\right)$$

Define the pairing kernel:

$$K_n(T) = \int dE \, N_n(E) \, \frac{1}{2\sqrt{\xi_n^2 + \Delta_n^2}} \tanh\left(\frac{\sqrt{\xi_n^2 + \Delta_n^2}}{2T}\right)$$

Then:

$$1 = g \cdot K_n(T)$$

At the critical temperature, $K_n(T_c^{(n)}) = 1/g$. Sites with larger $N(E_F)$ have larger $K_n$, hence reach $T_c$ at higher temperatures.

The paper finds: **Boundary sites (with enhanced $N$) have higher $T_c$ than bulk sites**. For a Cayley tree, $T_c^{(\text{boundary})} \approx 2 \times T_c^{(\text{bulk})}$ (factor of 2 enhancement).

### Macroscopic Edge Pairing

In the thermodynamic limit, the boundary contribution scales as:

$$\Delta_{\text{boundary}} \sim e^{R/2} \quad (\text{length scale } R \text{ in hyperbolic distance})$$

$$\Delta_{\text{bulk}} \sim 1 \quad (\text{constant})$$

Thus, even as $R \to \infty$, the ratio $\Delta_{\text{boundary}} / \Delta_{\text{bulk}} \to \infty$. **The order parameter is fundamentally localized at the boundary**, and the bulk remains normal (or weakly paired) even below $T_c^{(\text{boundary})}$.

---

## Key Results

1. **Boundary-Enhanced Density of States**: In hyperbolic geometries, $N(E)$ diverges at boundaries due to exponentially expanding volume. Bulk density remains polynomial.

2. **Dual Transition Temperatures**: Edge superconductivity ($T_c^{(\text{edge})} \sim 2 \times T_c^{(\text{bulk})}$) and bulk superconductivity are separated. Edge transitions first.

3. **Edge-Localized Order Parameter**: The gap $\Delta(x)$ is concentrated at boundaries in the thermodynamic limit. Bulk pairing is suppressed by the geometry.

4. **Cayley Tree Solution**: Explicit gap equations solved for finite and semi-infinite trees. Multiplicity of solutions corresponding to different edge/bulk combinations.

5. **No Topological Protection Needed**: Unlike topological superconductors, edge pairing here is purely due to geometry (negative curvature), not topology.

6. **Hyperbolic Continuum Results**: Analytical solution on the Poincare disk and horodisc regions confirm tree results in the continuum limit.

---

## Impact and Legacy

This paper is the first systematic treatment of BCS theory on curved manifolds. It bridges superconductivity and differential geometry. The results have immediate applications to:

- **Topological Superconductors**: Understanding boundary pairing without invoking topological band structure.
- **Curved-Space Field Theory**: Superconducting phases in cosmological backgrounds (inflation, dark energy).
- **Kaluza-Klein Phenomenology**: Pairing on internal dimensions.

---

## Connection to Phonon-Exflation Framework

**Curved-space BCS on SU(3):**

The framework computes BCS pairing (Cooper condensate) on the Jensen-deformed SU(3) manifold, which is positively curved (not negatively curved like hyperbolic space). However, the principle is identical: **curvature enters the density of states, modifying the gap equation**.

This paper provides the rigorous formalism. The van Hove mechanism in our framework (Session 23a: $N(E) \to \infty$ at the fold) is a manifestation of this principle — a geometric singularity (critical point of the metric) producing a divergent density of states.

**Boundary vs. bulk pairing:**

On the deformed SU(3), the spectrum has structure: $\mathfrak{su}(3)$ decomposes into irreps $(p, q)$, each with different curvature. The paper's finding — that high-curvature regions have enhanced pairing — suggests: **the Jensen deformation preferentially stabilizes pairing in sectors with positive curvature**, which is precisely what Sessions 34-35 found (B2 singlet channel, sector with large Casimir).

**Thermalization in presence of geometry:**

The paper shows that in hyperbolic geometry, boundaries remain superconducting while the bulk thermalizes. By analogy, on SU(3), the geometry (curvature) determines which sectors condense. The "bulk" (low-Casimir sectors) may remain normal, while the "boundary" (high-Casimir, near-van Hove) condenses.

**Dark energy from boundary condensate:**

If the van Hove singularity (boundary of the spectrum) is where pairing condenses, then the energy density is localized at the edge of the density-of-states band. In cosmology, such edge-localized vacuum energy could produce the smooth, nearly-uniform dark energy we observe — a geometric origin rather than a cosmological constant.

