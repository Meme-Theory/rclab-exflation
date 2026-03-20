# The Pancharatnam-Berry Phase in Polarization Optics

**Author(s):** Michael V. Berry

**Year:** 1987

**Journal:** Journal of Modern Optics, Vol. 34, pp. 1401-1407

---

## Abstract

Light propagating through polarizing optical elements acquires a geometric phase determined by the path traced by the polarization state on the Poincare sphere. This phenomenon, originally discovered by Pancharatnam (1956) in classical optics, can be understood as a special case of Berry's general geometric phase theory. The Pancharatnam-Berry phase depends only on the solid angle subtended by the polarization path on the Poincare sphere, not on the rate of polarization change. For a closed path returning to the original polarization state, the phase is:

$\gamma = \pm \frac{\Omega}{2}$

where $\Omega$ is the solid angle enclosed. This provides a beautiful geometric interpretation of polarization phenomena and has enabled practical optical devices (geometric phase optical elements, depolarizers, etc.) that rely on topological rather than dynamic effects.

---

## Historical Context

In 1956, Sheshachary Pancharatnam discovered an interesting phenomenon in classical optics: when linearly polarized light passes through a series of polarizing filters at different angles and returns to the original polarization direction, the phase shift depends not on the filters' individual properties but on the geometric path traced on the Poincare sphere (a representation of polarization states).

This discovery lay dormant for decades until Berry's general theory of geometric phases provided the conceptual framework to understand it. Berry showed that Pancharatnam's observation is a special case of the geometric phase principle, and that the phase is determined by the solid angle (area) enclosed on the Poincare sphere, analogous to how the Aharonov-Bohm phase is determined by enclosed magnetic flux.

Berry's 1987 Nature paper made the connection explicit and sparked the modern field of geometric phase optics. The subsequent development of geometric phase optical elements (GPOEs) has had practical applications in laser technology and quantum optics.

---

## Key Arguments and Derivations

### The Poincare Sphere Representation

Polarization states of light can be represented as points on the Poincare sphere, a 2-sphere in abstract polarization space. Any polarization state can be described by the Stokes parameters $(S_0, S_1, S_2, S_3)$, where:

- $S_0$ = total intensity
- $(S_1, S_2, S_3)$ represent the degree of linear and circular polarization

The Poincare sphere has normalized coordinates:

$(s_1, s_2, s_3) = \frac{(S_1, S_2, S_3)}{S_0}$

with $s_1^2 + s_2^2 + s_3^2 = 1$ for pure (fully polarized) states.

Key points on the sphere:
- North pole $(0, 0, 1)$: right-handed circular polarization
- South pole $(0, 0, -1)$: left-handed circular polarization
- Equator: linear polarization at various angles

### Pancharatnam's Experiment

Consider light passing through three linear polarizers at angles $\theta_1$, $\theta_2$, $\theta_3$, each separated by small angle increments, returning to the initial angle $\theta_1$ (i.e., $\theta_3 - \theta_1 = 0$ mod $2\pi$, but $\theta_2$ is between them).

The intensity after passing through all three is proportional to:

$I \propto \cos^2(\theta_2 - \theta_1) \cos^2(\theta_3 - \theta_2) \cos^2(\theta_1 - \theta_3)$

This is zero if the angles are equally spaced (120 degrees apart), but for other configurations, there is measurable transmission. Remarkably, Pancharatnam discovered that the phase of the emerging light (relative to the incident light) is not the sum of individual phase shifts from each filter, but rather depends on the area enclosed on the Poincare sphere.

### Geometric Phase on the Poincare Sphere

As light passes through a sequence of polarizers, the polarization state traces a path on the Poincare sphere. For a slowly varying (adiabatic) sequence of polarizers, the light remains in the instantaneous eigenstate of the optical system.

The geometric phase acquired is:

$\gamma = \pm \oint d\vec{s} \cdot \vec{A}(\vec{s})$

where $\vec{A}(\vec{s})$ is the Berry connection on the Poincare sphere, and the integral is around the closed path.

By Stokes' theorem:

$\gamma = \pm \int_S (\nabla \times \vec{A}) \cdot d\vec{S} = \pm \int_S d\Omega$

where $d\Omega$ is the solid angle element and $S$ is the surface enclosed by the path on the sphere.

For a simply connected region on the Poincare sphere:

$\gamma = \pm \frac{\Omega}{2}$

where $\Omega$ is the solid angle subtended. The sign depends on the orientation of the path (clockwise vs. counterclockwise when viewed from the center of the sphere).

The factor of 1/2 is crucial: for a path that closes on itself, the phase shift is half the solid angle, not equal to it.

### Practical Realization: Jones Vectors

For light, the polarization state can be represented by the Jones vector:

$\vec{E} = \begin{pmatrix} E_x \\ E_y \end{pmatrix}$

An optical element (waveplate, rotator, etc.) is described by a $2 \times 2$ Jones matrix $J$. For a sequence of elements:

$\vec{E}_{\text{out}} = J_n \cdots J_2 J_1 \vec{E}_{\text{in}}$

The geometric phase arises from the path of the output polarization state as the input state is cycled around a closed loop on the Poincare sphere. The phase depends on which eigenvector (ordinary or extraordinary ray) is being tracked and on the solid angle traced.

### Geometric Phase Optical Elements

A geometric phase optical element is a device designed to impart a specific geometric phase without relying on traditional refractive optics. Such elements can be created using:

1. **Liquid crystal devices**: By varying the orientation of liquid crystals across the device, the local polarization state changes smoothly, creating a designed phase pattern.

2. **Metasurfaces**: Subwavelength structures that manipulate polarization locally, introducing a spatially varying geometric phase.

A geometric phase optical element can implement the same function as traditional optical elements (lenses, mirrors, etc.) but with different physical mechanisms and potentially greater efficiency.

### Connection to Berry Curvature

The geometric phase on the Poincare sphere is related to the Berry curvature on the polarization eigenstate manifold. The Berry curvature $\mathcal{B}$ is:

$\mathcal{B} = \nabla \times \vec{A}$

On the Poincare sphere, this curvature is uniform (the sphere has constant Gaussian curvature), so:

$\mathcal{B} \sim$ constant

The curvature is related to the metric on the Poincare sphere. The solid angle integral is equivalent to integrating the Gaussian curvature, which by the Gauss-Bonnet theorem gives:

$\int_S K \, dA = 2\pi \chi(S)$

where $\chi(S)$ is the Euler characteristic of the surface.

---

## Key Results

1. **Pancharatnam phase formula**: The phase acquired by light traversing a closed polarization path is $\gamma = \Omega/2$, where $\Omega$ is the solid angle enclosed on the Poincare sphere.

2. **Geometric phase is exact**: The Pancharatnam-Berry phase is independent of the rate of polarization change—it depends only on the geometric path and the enclosed area.

3. **Topological quantization**: For paths that wind around the Poincare sphere multiple times, the total phase is quantized in units of solid angle.

4. **Geometric phase optical elements**: Optical devices can be designed to impart a predetermined geometric phase, enabling lenses, mirrors, and other elements without using refractive optics.

5. **Universal phenomenon**: The Pancharatnam-Berry phase appears in any adiabatic evolution of a two-level system where the parameter space is a 2D surface (like the Poincare sphere).

---

## Impact and Legacy

The Pancharatnam-Berry phase unified classical and quantum optics under a single geometric principle:

- **Optical technology**: Geometric phase optical elements are now standard in laser systems, enabling efficient manipulation of light without material dispersion.
- **Quantum information**: The geometric phase is exploited in quantum state manipulation and in geometric quantum gates, which are more robust to certain types of noise.
- **Foundational physics**: The Pancharatnam-Berry phase demonstrates that quantum mechanics and classical wave optics share the same geometric structure.
- **Topological optics**: The geometric phase is foundational to understanding topological phases in photonic systems and has connections to topological insulators.

The Pancharatnam-Berry phase is now a standard concept in optics textbooks and essential for understanding modern optical devices.

---

## Connection to Phonon-Exflation Framework

The Pancharatnam-Berry phase provides a concrete paradigm for understanding geometric structure in the phonon-exflation framework:

1. **Effective two-level systems**: In the Dirac spectrum, pairs of closely spaced eigenstates (before avoided crossing) form effective two-level systems. As the modulus parameter $s$ varies, these "two-level systems" trace paths in the space of eigenstate parameters.

2. **Phonon polarization analogs**: Just as light has polarization states, phonons in the internal space SU(3) have internal quantum numbers (generation, flavor, etc.). As the geometry evolves, these internal states trace paths in the space of quantum numbers, acquiring geometric phases.

3. **Solid angle in modulus space**: The avoided crossings in the Dirac spectrum (e.g., (3,0)-(2,0)) define regions in $s$-parameter space. The solid angle enclosed by paths in this parameter space (analogous to the Poincare sphere) determines geometric phases acquired by adiabatically evolving phonons.

4. **Topological structure of the spectrum**: The Berry curvature at avoided crossings (acting as monopoles) creates a structured topological landscape in $s$-parameter space. Phonons traversing this landscape acquire quantized geometric phases.

5. **Geometric phase elements in the internal space**: The deformed SU(3) geometry with parameter $s$ can be thought of as a "geometric phase optical element" for phonons—it imparts phase structure without changing the phonon identities, analogous to how a GPOE manipulates light polarization.

6. **Parameter-dependent couplings**: As $s$ evolves, phonon couplings change. If this evolution is adiabatic, phonons acquire geometric phases that are topologically protected (cannot be removed by small perturbations to the metric).

The Pancharatnam-Berry phase is directly relevant to understanding how the expanding universe (changing $s$) imparts geometric phases on the phonon spectrum.
