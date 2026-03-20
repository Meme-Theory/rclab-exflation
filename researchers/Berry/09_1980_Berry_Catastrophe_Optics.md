# Catastrophe Optics and Optical Caustics

**Author(s):** Michael V. Berry and C. Upstill

**Year:** 1980

**Journal:** Progress in Optics, Vol. 18, pp. 257-346

---

## Abstract

When light propagates through an inhomogeneous medium or is reflected from a curved surface, caustics form—surfaces where the light intensity is unbounded (formally infinite in the geometric optics approximation). Caustics have complex topological structures that can be classified using catastrophe theory (singularity theory). Berry's groundbreaking review showed that optical caustics and their evolution as parameters change are examples of catastrophes—singularities of mappings described by Thom's catastrophe theory. Fold caustics, cusp caustics, and higher-order caustics correspond to fold, cusp, and hyperbolic umbilic catastrophes. This unification reveals universal scaling laws near caustics and explains the topological transitions that occur when caustics bifurcate. The theory predicts the detailed intensity patterns near caustics, including the "glory" and "rainbow" effects observed in atmospheric optics.

---

## Historical Context

Caustics are ancient objects of study—they appear in everyday life (light patterns in water glasses, the bright ring in a wet rope). Newton studied them, and they were formalized in the 19th century via the envelope construction in geometric optics.

However, caustics are subtle: the geometric optics intensity diverges at caustics, requiring the addition of wave effects (diffraction) for a complete description. The diffraction patterns near caustics were mysterious until the 1970s, when Thom's catastrophe theory was being applied to physical phenomena.

Berry's insight was to recognize that caustics, as topological singularities of the ray mapping, fall naturally into Thom's classification of elementary catastrophes. This explained why diffraction patterns near different types of caustics have universal forms and why caustic evolution follows predictable topological rules.

The paper became foundational for understanding optical phenomena in the atmosphere (rainbows, mirages, glories) and sparked extensive research into topological optics.

---

## Key Arguments and Derivations

### Geometric Optics and Ray Mapping

In geometric optics, light propagates along rays (characteristics) of the wave equation. For a ray in a stratified medium with refractive index $n(\vec{r})$, the ray path satisfies Fermat's principle:

$\delta \int n(\vec{r}) \, ds = 0$

A ray bundle emanating from a point source will converge (focusing) or diverge (defocusing) depending on the medium's structure. At a point of convergence, the rays touch—this is a caustic surface.

The mapping from the source point to the receiving point defines a function:

$\vec{r} = \vec{r}(\vec{\xi}, \lambda)$

where $\vec{\xi}$ parametrizes the initial rays and $\lambda$ is a control parameter (e.g., impact parameter in scattering, viewing angle).

A caustic occurs where the Jacobian determinant vanishes:

$\det \frac{\partial \vec{r}}{\partial \vec{\xi}} = 0$

This is a singular point of the mapping—the image of multiple rays overlaps.

### Thom's Catastrophe Theory

Catastrophe theory classifies singularities of smooth mappings. The elementary catastrophes (for systems with up to 4 control parameters) are:

1. **Fold** ($A_2$): A smooth minimum that disappears as a control parameter varies
   - Equation: $x^3 + \lambda x = 0$
   - Caustic type: Fold surface

2. **Cusp** ($A_3$): Two folds merge and annihilate
   - Equation: $x^4 + \lambda x^2 + \mu x = 0$
   - Caustic type: Cusp edge

3. **Swallowtail** ($A_4$): More complex bifurcation
   - Equation: $x^5 + \lambda x^3 + \mu x^2 + \nu x = 0$

4. **Hyperbolic umbilic** ($D_4^+$): Two-parameter family
   - Three surfaces of folds meeting at a point

### The Fold Caustic

The simplest caustic is a fold, where rays from two neighboring directions converge. Near a fold, the ray amplitude varies as:

$A(\vec{r}) \sim \text{const} / |\det(\partial \vec{r}/\partial \vec{\xi})|^{1/4}$

Near the caustic, the intensity diverges as:

$I \sim |x|^{-1/2}$

where $x$ measures distance from the caustic surface. When diffraction is included, the intensity near a fold is given by the Airy function:

$I_{\text{wave}} \sim |\text{Ai}(k^{2/3} x)|^2$

This creates the characteristic bright fringe at the caustic, surrounded by oscillations (diffraction fringes) that decay away from the caustic.

### The Cusp Caustic

At a cusp caustic, three ray directions converge, and two fold surfaces meet. The cusp has a two-parameter unfolding:

$r = x^3 + \lambda x^2 + \mu x + c$

The cusp surface in $(x, \lambda, \mu)$ space divides the parameter space into regions with different numbers of real solutions (different numbers of rays).

The diffraction pattern near a cusp is given by a uniform asymptotic expansion involving the Pearcey function $\text{Pe}(x, y)$, defined by:

$\text{Pe}(x, y) = \int_{-\infty}^{\infty} e^{i(t^4 + xt^2 + yt)} dt$

The intensity pattern shows a distinctive X-shape at the cusp, with bright lobes and an oscillating interior structure.

### Rainbow and Glory Effects

The rainbow is a fold caustic formed when sunlight is refracted and internally reflected in water droplets. The rainbow angle is determined by the condition that the Jacobian vanishes, which occurs at an impact parameter where the refractive index creates a focusing condition.

For water droplets with refractive index $n = 1.33$, the rainbow primary appears at approximately $42°$ from the antisolar point.

The glory is a higher-order rainbow appearing at the backward-scattering direction. It is a cusp caustic formed by interference of rays with multiple internal reflections.

Berry showed that both the rainbow and glory can be understood as catastrophes, with predictable scaling laws for intensity and angular width:

- Rainbow intensity: $I \propto k^{-1/3}$ where $k$ is the wavenumber
- Glory oscillation period: Related to the Airy function oscillation scale

### Topological Transitions

As a control parameter varies (e.g., refractive index or droplet size), caustics undergo topological transitions. A fold can split into two folds, merge with another fold, or annihilate. These transitions correspond to bifurcation points in catastrophe theory.

For example, in the rainbow, if the refractive index changes, the fold caustic unfolds or refolds. The transition from a visible rainbow to an invisible one (as n decreases) corresponds to a fold bifurcation.

---

## Key Results

1. **Universal caustic classification**: All optical caustics fall into Thom's elementary catastrophes. Only fold, cusp, swallowtail, and hyperbolic umbilic caustics appear generically in 3D.

2. **Diffraction patterns**: The intensity distributions near caustics are given by universal functions (Airy, Pearcey, etc.) that depend only on the catastrophe type, not on microscopic details of the medium.

3. **Scaling laws**: The intensity and oscillation patterns near caustics obey universal scaling laws:
   - Fold: $I \sim |x|^{-1/2}$, fringe spacing $\sim k^{-1/3}$
   - Cusp: Pearcey function asymptotics
   - Glory: Double exponential decay far from the peak

4. **Topological transitions**: As parameters vary, caustics undergo bifurcations according to catastrophe theory rules. The bifurcation points are universal and parameter-independent.

5. **Experimental predictions**: The theory predicts the detailed structure of optical phenomena like rainbows, mirages, halos, and glories, including intensity ratios, angular separations, and fine structure.

---

## Impact and Legacy

Berry's catastrophe optics became a paradigm for understanding complex optical phenomena:

- **Atmospheric optics**: Explained rainbows, supernumerary rainbows, glories, and other sky phenomena from first principles.
- **Caustic topology**: Established that caustic structures are universal and can be predicted without detailed knowledge of the ray paths.
- **Diffraction theory**: Unified geometric optics with wave effects via catastrophe theory, showing how diffraction patterns encode caustic singularities.
- **Singularity physics**: Showed that catastrophe theory is not just mathematical abstraction but describes real physical phenomena.
- **Experimental verification**: Predictions of caustic structure and scaling laws have been confirmed in laboratory experiments and atmospheric observations.

Catastrophe optics is now standard in geophysical optics and atmospheric physics.

---

## Connection to Phonon-Exflation Framework

Caustic theory provides important insights into the phonon-exflation spectrum:

1. **Avoided crossings as caustics**: The avoided crossings in the Dirac spectrum can be understood as caustics in the "ray optics" of eigenvalue flow. As the parameter $s$ varies, eigenvalue trajectories (analogs of light rays) undergo bifurcations.

2. **Cusp catastrophe in spectrum**: If the Dirac spectrum exhibits a cusp caustic (e.g., three levels approaching near the same energy at a specific $s$ value), the spectrum near that point has the characteristic Pearcey function structure.

3. **Unfolding and level statistics**: The unfolding of eigenvalues (removing the smooth density-of-states background) can be understood as removing the "macroscopic" geometric structure, leaving the fine structure analogous to diffraction near a caustic.

4. **Scaling of level repulsion**: Near avoided crossings (analogous to fold caustics), the level spacing obeys universal scaling laws that depend only on the local geometry of the crossing, not on global properties of the spectrum.

5. **Topological transitions in $s$-parameter**: If the cosmological modulus $s$ varies, the Dirac spectrum may undergo bifurcations—new avoided crossings may appear or existing ones may annihilate. These are topological transitions analogous to fold bifurcations in catastrophe theory.

6. **Effective diffraction in spectral space**: The spectral action calculation involves summing or integrating over eigenmodes. Near avoided crossings, "diffraction" effects (interference between nearby modes) create oscillations analogous to diffraction fringes near optical caustics.

7. **Observable implications**: If catastrophe theory applies to the phonon spectrum, then observable quantities (particle masses, coupling constants) should show universal scaling behaviors near critical values of $s$, similar to how rainbow intensity shows universal scaling near the rainbow angle.

Catastrophe optics is particularly relevant for understanding topological transitions in the spectrum and the detailed structure of level crossings.
