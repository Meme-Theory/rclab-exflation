# The Field Equations of Gravitation

**Author:** Albert Einstein
**Year:** 1915
**Journal:** *Sitzungsberichte der Preussischen Akademie der Wissenschaften*, 844--847 (25 November 1915)

---

## Abstract

This paper presents the final, correct form of the gravitational field equations of general relativity, culminating a decade of effort (1907--1915) and a frantic November 1915 competition with David Hilbert. Einstein arrives at the equations $R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \kappa T_{\mu\nu}$ (equivalently, $G_{\mu\nu} = \kappa T_{\mu\nu}$), which relate the curvature of spacetime to the distribution of matter and energy. As immediate confirmation, Einstein demonstrates that these equations correctly predict the anomalous precession of Mercury's perihelion -- 43 arcseconds per century -- a discrepancy that had resisted explanation within Newtonian gravity for over half a century. The paper represents one of the greatest intellectual achievements in the history of physics.

---

## Historical Context

### From Special to General Relativity (1907--1912)

Einstein's journey from special relativity to general relativity began in 1907 with what he later called "the happiest thought of my life": the recognition that a person in free fall does not feel their own weight. This observation -- the **equivalence principle** -- implies that gravitational and inertial effects are locally indistinguishable.

The equivalence principle has a precise formulation: in a sufficiently small region of spacetime, the laws of physics reduce to those of special relativity. Gravity is not a force in the Newtonian sense but a manifestation of spacetime curvature. A freely falling particle follows the straightest possible path (geodesic) through curved spacetime.

By 1912, Einstein recognized that the gravitational field must be described by the metric tensor $g_{\mu\nu}$, a symmetric $4 \times 4$ matrix that encodes the geometry of spacetime. The metric determines distances:

$$ds^2 = g_{\mu\nu}\,dx^\mu\,dx^\nu$$

and the geodesic equation:

$$\frac{d^2x^\alpha}{d\tau^2} + \Gamma^\alpha_{\mu\nu}\frac{dx^\mu}{d\tau}\frac{dx^\nu}{d\tau} = 0$$

where $\Gamma^\alpha_{\mu\nu}$ are the Christoffel symbols (the gravitational "force" terms).

### The Zurich Notebook and the Entwurf Theory (1912--1913)

In collaboration with his mathematician friend Marcel Grossmann, Einstein searched for field equations that would determine $g_{\mu\nu}$ from the matter distribution. The "Zurich notebook" (1912-1913) records Einstein's exploration of various candidates, including equations based on the Ricci tensor $R_{\mu\nu}$. However, Einstein mistakenly convinced himself that Ricci-based equations could not reduce to the Newtonian limit and abandoned them.

Instead, Einstein and Grossmann published the "Entwurf" (outline) theory in 1913, with field equations that were not generally covariant -- they held only in restricted coordinate systems. Einstein spent two years defending this theory, constructing increasingly tortured arguments for why general covariance was not required (the "hole argument").

### The November Revolution (1915)

In the fall of 1915, Einstein recognized fatal flaws in the Entwurf theory and returned to generally covariant field equations. What followed was an extraordinary four-week sprint, documented in four papers presented to the Prussian Academy on November 4, 11, 18, and 25.

- **November 4:** Einstein proposes field equations based on the Ricci tensor: $R_{\mu\nu} = \kappa T_{\mu\nu}$, but restricted to unimodular coordinates ($\sqrt{-g} = 1$).
- **November 11:** Einstein extends the theory and corrects some errors.
- **November 18:** Einstein calculates Mercury's perihelion precession from the November 4 equations and obtains the correct value of 43"/century. He is reportedly so excited that he has heart palpitations.
- **November 25:** Einstein presents the final, fully generally covariant field equations with the trace term.

### The Race with Hilbert

David Hilbert, working independently from an axiomatic approach, submitted a paper on November 20, 1915, that also contained the correct field equations (derived from a variational principle). The priority question has generated extensive historical scholarship. The consensus is that Einstein and Hilbert arrived at the equations independently and nearly simultaneously, with Einstein having the physical insight and Hilbert the mathematical elegance. Hilbert's published paper (revised in proof) explicitly credits Einstein with the physical theory.

---

## Key Arguments and Derivations

### I. The Equivalence Principle and Curved Spacetime

The equivalence principle states that at any point in spacetime, one can choose a locally inertial coordinate system (a freely falling frame) in which the metric is Minkowski and the Christoffel symbols vanish:

$$g_{\mu\nu}(P) = \eta_{\mu\nu}, \qquad \Gamma^\alpha_{\mu\nu}(P) = 0$$

This is the mathematical expression of the idea that gravity is locally undetectable. The global effect of gravity is encoded in the curvature -- the fact that one cannot make $\Gamma^\alpha_{\mu\nu} = 0$ everywhere simultaneously.

### II. Riemann Curvature

The failure of parallel transport to be path-independent in curved spacetime is measured by the Riemann curvature tensor:

$$R^\rho_{\ \sigma\mu\nu} = \partial_\mu\Gamma^\rho_{\nu\sigma} - \partial_\nu\Gamma^\rho_{\mu\sigma} + \Gamma^\rho_{\mu\lambda}\Gamma^\lambda_{\nu\sigma} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\mu\sigma}$$

The Riemann tensor has 20 independent components in four dimensions. For the field equations, Einstein needs a rank-2 tensor (to match the rank-2 stress-energy tensor). The unique contraction is the Ricci tensor:

$$R_{\mu\nu} = R^\rho_{\ \mu\rho\nu} = \partial_\rho\Gamma^\rho_{\nu\mu} - \partial_\nu\Gamma^\rho_{\rho\mu} + \Gamma^\rho_{\rho\lambda}\Gamma^\lambda_{\nu\mu} - \Gamma^\rho_{\nu\lambda}\Gamma^\lambda_{\rho\mu}$$

and the Ricci scalar:

$$R = g^{\mu\nu}R_{\mu\nu}$$

### III. The Einstein Tensor

The field equations must satisfy a crucial consistency condition. The stress-energy tensor obeys local conservation:

$$\nabla_\mu T^{\mu\nu} = 0$$

(This follows from the equations of motion of matter.) Therefore, the geometric side of the field equations must be automatically divergence-free.

The Ricci tensor alone does not satisfy this: $\nabla_\mu R^{\mu\nu} \neq 0$ in general. However, the **contracted Bianchi identity** states:

$$\nabla_\mu\left(R^{\mu\nu} - \frac{1}{2}g^{\mu\nu}R\right) = 0$$

This identity is purely geometric -- it follows from the symmetries of the Riemann tensor and holds on any (pseudo-)Riemannian manifold. It defines the **Einstein tensor**:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R$$

which is automatically divergence-free: $\nabla_\mu G^{\mu\nu} = 0$.

### IV. The Field Equations

Einstein's field equations are:

$$G_{\mu\nu} = R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R = \frac{8\pi G}{c^4}T_{\mu\nu}$$

or equivalently (taking the trace and substituting back):

$$R_{\mu\nu} = \frac{8\pi G}{c^4}\left(T_{\mu\nu} - \frac{1}{2}g_{\mu\nu}T\right)$$

where $T = g^{\mu\nu}T_{\mu\nu}$ is the trace of the stress-energy tensor.

The coupling constant $\kappa = 8\pi G/c^4$ is fixed by requiring that the equations reduce to Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ in the Newtonian limit.

In vacuum ($T_{\mu\nu} = 0$), the equations simplify to:

$$R_{\mu\nu} = 0$$

This does NOT mean spacetime is flat -- the Riemann tensor can be nonzero even when the Ricci tensor vanishes. The vacuum equations have 10 components constraining 10 metric components, minus 4 for coordinate freedom, leaving 6 independent equations for 6 independent metric functions -- consistent with 2 physical degrees of freedom (the two polarizations of gravitational waves).

### V. The Newtonian Limit

For weak gravitational fields and slow motions, write $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$. The dominant component is:

$$g_{00} \approx -(1 + 2\Phi/c^2)$$

where $\Phi$ is the Newtonian gravitational potential. The geodesic equation reduces to:

$$\frac{d^2x^i}{dt^2} = -\partial_i\Phi$$

which is Newton's second law with the gravitational force. The $00$ component of the field equations becomes:

$$\nabla^2\Phi = 4\pi G\rho$$

which is Poisson's equation.

### VI. Mercury's Perihelion Precession

The most celebrated result of the November 18 paper (which uses equations equivalent to the final ones for this calculation) is the precession of Mercury's orbit.

For a spherically symmetric mass $M$, the vacuum field equations ($R_{\mu\nu} = 0$) yield the Schwarzschild metric (found by Karl Schwarzschild in January 1916):

$$ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 + r^2 d\Omega^2$$

where $r_s = 2GM/c^2$ is the Schwarzschild radius.

The orbit equation (derived from geodesics) is:

$$\frac{d^2u}{d\phi^2} + u = \frac{GM}{L^2} + \frac{3GM}{c^2}u^2$$

where $u = 1/r$ and $L$ is the specific angular momentum. The first term gives Keplerian orbits. The second term, proportional to $1/c^2$, is the general-relativistic correction.

For a nearly circular orbit, the perturbation causes the orbit to precess. The precession per orbit is:

$$\Delta\phi = \frac{6\pi G M}{c^2 a(1-e^2)}$$

where $a$ is the semi-major axis and $e$ is the eccentricity. For Mercury:

$$\Delta\phi = \frac{6\pi \times 6.674\times10^{-11} \times 1.989\times10^{30}}{(3\times10^8)^2 \times 5.79\times10^{10} \times (1 - 0.2056^2)} \approx 5.02 \times 10^{-7}\;\text{rad/orbit}$$

Over one century (415 orbits):

$$\Delta\phi_{century} \approx 42.98'' \approx 43''$$

This matched the observed anomaly of $43'' \pm 0.1''$ per century, which had been known since Le Verrier (1859) and had resisted all Newtonian explanations (including a hypothetical planet Vulcan).

---

## Physical Interpretation

### Geometry IS Gravity

The field equations express a revolutionary idea: gravity is not a force acting in a fixed spacetime background but is the curvature of spacetime itself. Matter tells spacetime how to curve ($G_{\mu\nu} = \kappa T_{\mu\nu}$), and spacetime tells matter how to move (the geodesic equation). This mutual, nonlinear interaction is encoded in ten coupled, nonlinear partial differential equations for the metric components.

### The Nonlinearity of Gravity

Unlike Maxwell's equations (which are linear), Einstein's equations are profoundly nonlinear. Gravitational energy itself gravitates. This self-interaction is responsible for many of the most dramatic predictions of GR: black holes, gravitational waves that carry energy, and the instability of static cosmological models.

### Background Independence

General relativity is the prototypical background-independent theory: the geometry of spacetime is not specified a priori but is determined dynamically by the field equations. This feature -- considered by many to be essential for any theory of quantum gravity -- has profoundly shaped the research programs of loop quantum gravity, causal dynamical triangulations, and other approaches.

---

## Impact and Legacy

### Schwarzschild Solution (1916)

Karl Schwarzschild found the first exact solution within weeks, describing the spacetime outside a spherically symmetric mass. The Schwarzschild solution predicts black holes (the term coined by Wheeler in 1967), which were long regarded as mathematical curiosities but are now confirmed through gravitational wave detections and the Event Horizon Telescope image of M87*.

### Gravitational Waves

The linearized field equations predict propagating perturbations of the metric -- gravitational waves -- traveling at the speed of light with two polarizations. These were detected by LIGO on September 14, 2015, exactly 100 years after the field equations were written down, confirming GR's most dramatic prediction.

### Cosmology

The field equations, applied to a homogeneous, isotropic universe, yield the Friedmann equations governing cosmic expansion. This application, pioneered by Friedmann (1922) and Lemaitre (1927), created physical cosmology as a science and predicted the expansion of the universe, confirmed by Hubble (1929).

### Tests of General Relativity

Beyond Mercury's precession, GR has been confirmed by:
- Light deflection by the Sun (Eddington, 1919; see Paper 11)
- Gravitational redshift (Pound-Rebka, 1959; see Paper 14)
- Shapiro time delay (1964)
- Orbital decay of the Hulse-Taylor binary pulsar (1979, matching GR's prediction for gravitational wave emission to 0.2%)
- Frame-dragging (Gravity Probe B, 2011)
- Black hole mergers (LIGO/Virgo, 2015-present)

---

## Connections to Modern Physics

### The Cosmological Constant

Einstein would modify his own equations in 1917 by adding $\Lambda g_{\mu\nu}$ (see Paper 07). The cosmological constant has returned as the leading description of dark energy, with $\Lambda \sim 10^{-52}$ m$^{-2}$.

### Quantum Gravity

The field equations are classical. Quantizing them -- constructing a consistent quantum theory of the gravitational field -- remains the central open problem in theoretical physics. The nonrenormalizability of perturbative quantum gravity (shown by 't Hooft and Veltman, 1974) indicates that GR cannot be the final theory at the Planck scale.

### The Action Principle

Hilbert showed that the field equations follow from the Einstein-Hilbert action:

$$S = \frac{c^4}{16\pi G}\int R\sqrt{-g}\,d^4x + S_{matter}$$

Varying with respect to $g^{\mu\nu}$ yields $G_{\mu\nu} = \kappa T_{\mu\nu}$. This variational formulation is the starting point for all modern extensions (supergravity, string theory, $f(R)$ gravity).

### Kaluza-Klein and Extra Dimensions

Kaluza (1921) and Klein (1926) showed that if spacetime is extended to five dimensions, with the fifth dimension compactified on a circle, then the five-dimensional Einstein equations contain both four-dimensional gravity and Maxwell's electrodynamics. This is the ancestor of all extra-dimensional theories and directly relevant to frameworks that unify gravity and gauge theory through internal geometry.
