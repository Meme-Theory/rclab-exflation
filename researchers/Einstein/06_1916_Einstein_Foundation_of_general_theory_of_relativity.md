# The Foundation of the General Theory of Relativity

**Author:** Albert Einstein
**Year:** 1916
**Journal:** *Annalen der Physik*, **49**, 769--822

---

## Abstract

This paper is the definitive exposition of general relativity, presented as a self-contained treatise running to over fifty pages. Einstein systematically develops the mathematical apparatus (tensor calculus on curved manifolds), states the physical principles (general covariance, equivalence principle, Mach's principle), derives the geodesic equation for free particle motion, constructs the Einstein field equations from the Riemann curvature tensor, and applies the theory to compute the perihelion advance of Mercury, the deflection of light by the Sun, and the gravitational redshift. The paper represents not only the completion of a physical theory but the introduction of differential geometry as the language of fundamental physics -- a paradigm shift whose influence extends through gauge theory, string theory, and all of modern theoretical physics.

---

## Historical Context

### The Need for a Definitive Account

The November 1915 papers had been brief communications to the Prussian Academy -- compressed, technical, and incomplete in their exposition. The physics community needed a comprehensive, pedagogical presentation. Einstein wrote this paper in late 1915 and early 1916, and it was published in March 1916. It remains the canonical reference for understanding Einstein's own formulation of the theory.

### Mathematical Preparation

Einstein's struggle with the mathematics of curved spaces is well documented. He relied heavily on his friend Marcel Grossmann, a mathematician, and on the work of Ricci and Levi-Civita on absolute differential calculus (tensor analysis). By 1916, Einstein had fully mastered the formalism and could present it with clarity.

### Physical Motivations

Einstein frames the paper around three physical principles:

1. **The Principle of Relativity** (generalized): The laws of physics should take the same form in all coordinate systems, not just inertial ones. This is the principle of general covariance.

2. **The Equivalence Principle**: Inertial and gravitational mass are identical; gravity and acceleration are locally indistinguishable.

3. **Mach's Principle**: The inertial properties of matter are determined by the distribution of all other matter in the universe. (This principle is partially realized in GR but not completely -- the theory admits solutions with no matter, like Minkowski space.)

---

## Key Arguments and Derivations

### Part A: Fundamental Considerations on the Postulate of Relativity

#### The Critique of Privileged Frames

Einstein begins by arguing against the privileged status of inertial frames. In Newtonian mechanics and special relativity, inertial frames are distinguished by the absence of fictitious forces. But this distinction relies on the concept of absolute space (or at least a preferred class of frames), which Einstein finds unsatisfactory.

The thought experiment: two fluid bodies $S_1$ and $S_2$ floating in empty space, rotating relative to each other. $S_1$ is a sphere (no centrifugal bulging) while $S_2$ is an oblate ellipsoid. Newtonian mechanics explains this by saying $S_2$ is "truly rotating" relative to absolute space. But absolute space is unobservable. Mach argued that the difference should be attributed to rotation relative to the distant masses of the universe.

#### General Covariance

Einstein proposes that the laws of physics must be expressed in a form that is valid in all coordinate systems -- not just Cartesian or inertial coordinates. Mathematically, this means the laws must be written as tensor equations:

$$\text{If } A^{\mu\nu\ldots}_{\phantom{\mu\nu}\rho\sigma\ldots} = 0 \text{ in one coordinate system, then } A'^{\mu\nu\ldots}_{\phantom{\mu\nu}\rho\sigma\ldots} = 0 \text{ in all.}$$

This is the principle of general covariance. It is not merely a mathematical convenience; Einstein argues it has physical content because it entails that the gravitational field (represented by the metric) is not a fixed background but a dynamical entity.

### Part B: Mathematical Tools

#### The Metric Tensor

The fundamental object is the metric tensor $g_{\mu\nu}(x)$, which determines the infinitesimal spacetime interval:

$$ds^2 = g_{\mu\nu}\,dx^\mu\,dx^\nu$$

(Einstein uses the summation convention, introduced in this paper: repeated upper and lower indices are summed from 0 to 3.)

The metric tensor:
- Is symmetric: $g_{\mu\nu} = g_{\nu\mu}$ (10 independent components).
- Has Lorentzian signature $(-,+,+,+)$.
- Determines the causal structure: $ds^2 < 0$ for timelike, $ds^2 = 0$ for null, $ds^2 > 0$ for spacelike separations.
- Has an inverse $g^{\mu\nu}$ satisfying $g^{\mu\alpha}g_{\alpha\nu} = \delta^\mu_\nu$.

#### Coordinate Transformations and Tensors

Under a coordinate transformation $x^\mu \to x'^\mu(x)$, tensors transform according to their index structure:

**Contravariant vector:** $A'^\mu = \frac{\partial x'^\mu}{\partial x^\nu}A^\nu$

**Covariant vector:** $A'_\mu = \frac{\partial x^\nu}{\partial x'^\mu}A_\nu$

**General tensor:** Each upper index transforms with $\partial x'/\partial x$ and each lower index with $\partial x/\partial x'$.

The metric can raise and lower indices: $A_\mu = g_{\mu\nu}A^\nu$, $A^\mu = g^{\mu\nu}A_\nu$.

#### Covariant Derivative

Partial derivatives of tensors are not tensors (they do not transform correctly). Einstein introduces the covariant derivative:

$$\nabla_\mu A^\nu = \partial_\mu A^\nu + \Gamma^\nu_{\mu\alpha}A^\alpha$$

$$\nabla_\mu A_\nu = \partial_\mu A_\nu - \Gamma^\alpha_{\mu\nu}A_\alpha$$

where the Christoffel symbols (Levi-Civita connection) are:

$$\Gamma^\alpha_{\mu\nu} = \frac{1}{2}g^{\alpha\beta}\left(\partial_\mu g_{\nu\beta} + \partial_\nu g_{\mu\beta} - \partial_\beta g_{\mu\nu}\right)$$

The Christoffel symbols are symmetric ($\Gamma^\alpha_{\mu\nu} = \Gamma^\alpha_{\nu\mu}$) and are NOT tensors -- they transform inhomogeneously, which is precisely what cancels the non-tensorial part of the partial derivative.

The covariant derivative of the metric vanishes identically:

$$\nabla_\alpha g_{\mu\nu} = 0$$

This is the metricity condition, which says that parallel transport preserves inner products.

#### The Riemann Curvature Tensor

The failure of covariant derivatives to commute measures curvature:

$$[\nabla_\mu, \nabla_\nu]A^\rho = R^\rho_{\ \sigma\mu\nu}A^\sigma$$

where:

$$R^\rho_{\ \sigma\mu\nu} = \partial_\mu\Gamma^\rho_{\nu\sigma} - \partial_\nu\Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}$$

The Riemann tensor has 20 independent components (in 4D) and satisfies the symmetries:

$$R_{\rho\sigma\mu\nu} = -R_{\sigma\rho\mu\nu} = -R_{\rho\sigma\nu\mu} = R_{\mu\nu\rho\sigma}$$

$$R_{\rho[\sigma\mu\nu]} = 0 \qquad \text{(first Bianchi identity)}$$

$$\nabla_{[\alpha}R_{\rho\sigma]\mu\nu} = 0 \qquad \text{(second Bianchi identity)}$$

### Part C: The Geodesic Equation

A freely falling particle follows the path that extremizes proper time:

$$\delta\int ds = 0$$

The Euler-Lagrange equation for this variational problem is the geodesic equation:

$$\frac{d^2x^\alpha}{d\tau^2} + \Gamma^\alpha_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau} = 0$$

This replaces Newton's second law with gravitational force. The Christoffel symbols play the role of the gravitational "force" -- but they are geometric, not physical forces. A freely falling observer experiences no force; the geodesic equation simply says they follow the straightest possible path in curved spacetime.

For light (massless particles), the path satisfies $ds = 0$ (null geodesic), and the parameter $\tau$ is replaced by an affine parameter $\lambda$:

$$\frac{d^2x^\alpha}{d\lambda^2} + \Gamma^\alpha_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda} = 0, \qquad g_{\mu\nu}\frac{dx^\mu}{d\lambda}\frac{dx^\nu}{d\lambda} = 0$$

### Part D: The Field Equations

#### Construction

Einstein requires:
1. A second-rank, symmetric tensor equation (to match $T_{\mu\nu}$).
2. Second-order in derivatives of $g_{\mu\nu}$ (by analogy with Poisson's equation).
3. Divergence-free left-hand side (to be compatible with $\nabla_\mu T^{\mu\nu} = 0$).
4. Reduction to Poisson's equation in the Newtonian limit.

The contracted Bianchi identity provides the unique answer:

$$G_{\mu\nu} \equiv R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$$

satisfies $\nabla_\mu G^{\mu\nu} = 0$ identically. The field equations are:

$$R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4}T_{\mu\nu}$$

#### The Stress-Energy Tensor

The right-hand side is the stress-energy tensor $T_{\mu\nu}$, which encodes the density, flux, and stress of matter and energy:

- $T^{00}$: energy density
- $T^{0i}$: energy flux / momentum density
- $T^{ij}$: stress tensor (pressure on diagonal, shear off-diagonal)

For a perfect fluid:

$$T^{\mu\nu} = \left(\rho + \frac{p}{c^2}\right)u^\mu u^\nu + pg^{\mu\nu}$$

where $\rho$ is the energy density, $p$ is the pressure, and $u^\mu$ is the four-velocity.

### Part E: Applications

#### Perihelion Advance (Revisited)

Einstein reproduces the Mercury calculation from the November 18 paper, now within the systematic framework. The result:

$$\Delta\phi = \frac{6\pi GM}{c^2 a(1-e^2)} = 43.0''/\text{century}$$

#### Deflection of Light

A light ray passing the Sun at impact parameter $b$ is deflected by:

$$\delta = \frac{4GM}{c^2 b}$$

For a ray grazing the Sun ($b = R_\odot$):

$$\delta = \frac{4 \times 6.674\times10^{-11} \times 1.989\times10^{30}}{(3\times10^8)^2 \times 6.96\times10^8} \approx 1.75''$$

This is exactly twice the prediction from the equivalence principle alone (which gives $0.87''$), because the spatial curvature contributes equally to the deflection. The factor of 2 became a critical test -- see Paper 11 on Eddington's eclipse expedition.

#### Gravitational Redshift

A photon climbing out of a gravitational potential well loses energy. For a static field:

$$\frac{\Delta\nu}{\nu} = \frac{\Phi}{c^2}$$

This was confirmed by Pound and Rebka in 1959 (see Paper 14).

---

## Physical Interpretation

### Geometry as Physics

The paper establishes the paradigm that physical interactions can be encoded in the geometry of spacetime. The metric $g_{\mu\nu}$ is not a background stage but a dynamical participant -- it is both the arena in which physics occurs and the gravitational field itself. This identification of geometry with physics was revolutionary and remains the guiding principle of theoretical physics.

### The Nonlinearity and Self-Coupling

The Einstein equations are nonlinear: the metric appears on both sides (through the energy of the gravitational field itself, which is not captured by $T_{\mu\nu}$ but is implicit in the nonlinear structure of $G_{\mu\nu}$). This self-coupling is responsible for black holes, gravitational wave nonlinear interactions, and the absence of a well-defined local gravitational energy density.

### Conservation Laws

In GR, the covariant conservation law $\nabla_\mu T^{\mu\nu} = 0$ replaces the ordinary conservation laws of special relativity. In curved spacetime, this does not imply a globally conserved energy -- there is no time-translation symmetry in a general spacetime. Global conservation laws require asymptotic flatness or other special structure (Killing vectors).

---

## Impact and Legacy

### The Language of Modern Physics

This paper introduced differential geometry as the language of fundamental physics. The same mathematical framework -- connections on fiber bundles, curvature tensors, covariant derivatives -- was later adopted for gauge theories:
- Yang-Mills theory (1954): gauge fields as connections on principal bundles
- The Standard Model: $SU(3) \times SU(2) \times U(1)$ gauge theory
- Kaluza-Klein theory: unifying gravity and gauge theory through extra dimensions

### Exact Solutions

The field equations have yielded a rich family of exact solutions:
- Schwarzschild (1916): static, spherically symmetric vacuum
- Reissner-Nordstrom (1916-18): charged black hole
- Kerr (1963): rotating black hole
- Friedmann-Lemaitre-Robertson-Walker (1922-35): homogeneous cosmology
- de Sitter (1917): vacuum with cosmological constant

### Observational Cosmology

Applied to the universe as a whole, the field equations predict either expansion or contraction -- a static universe is unstable. This prediction, initially resisted by Einstein (who introduced the cosmological constant to avoid it), was confirmed by Hubble's observations.

---

## Connections to Modern Physics

### ADM Formalism and Canonical Gravity

Arnowitt, Deser, and Misner (1962) reformulated GR as a Hamiltonian system by decomposing the metric into spatial and temporal parts. The ADM formalism is the starting point for canonical quantum gravity and loop quantum gravity.

### Spectral Geometry

The Dirac operator on a curved manifold encodes the geometry through its spectrum (Connes' spectral triples). This connection between differential geometry and spectral theory is the mathematical bridge between GR and approaches to quantum gravity based on noncommutative geometry.

### Gravitational Waves as a Precision Tool

GR's prediction of gravitational waves, derived from the linearized field equations, has opened a new observational window onto the universe. The LIGO/Virgo detections (2015-present) test GR in the strong-field regime and have observed black hole and neutron star mergers.

### The Information Paradox

The combination of GR (black holes) and quantum mechanics (Hawking radiation) produces the black hole information paradox, which remains unresolved. The field equations of this paper, applied to collapsing matter (Oppenheimer-Snyder, Paper 12), produce event horizons that challenge the unitarity of quantum mechanics.
