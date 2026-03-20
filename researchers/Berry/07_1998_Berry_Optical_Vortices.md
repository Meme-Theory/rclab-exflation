# Optical Vortices and Wavefront Dislocations

**Author(s):** Michael V. Berry

**Year:** 1998

**Journal:** Proc. SPIE 3487, International Conference on Singular Optics, pp. 1-5 (conference proceedings); see also Nye & Berry 1974 (Proc. R. Soc. A 336, 165-190) for foundational results

---

## Abstract

Optical vortices are phase singularities in light fields where the wavefront forms a dislocation (like a screw dislocation in a crystal). At the core of an optical vortex, the phase is undefined (singular), and the intensity vanishes. The vortex is characterized by a topological charge (winding number) determined by the circulation of phase around the vortex:

$m = \frac{1}{2\pi} \oint \nabla \phi \cdot d\vec{l}$

Optical vortices have profound implications: they carry orbital angular momentum, enable new approaches to optical manipulation and communication, and reveal fundamental topological structure in wave phenomena. Berry showed that optical vortices are generic—they appear naturally in random wave fields and at any point in parameter space where the phase has a singularity. This work opened a new subfield of singular optics.

---

## Historical Context

Phase singularities in waves were known in principle since the early 20th century, but their physical significance and ubiquity were not appreciated until the 1990s. Nye and Berry (1974) first discussed phase singularities in random wave fields, showing that singularities are generic features, not rare artifacts.

By the 1990s, experimental techniques (computer-generated holograms, liquid crystal spatial light modulators) made it possible to generate and manipulate optical vortices on demand. Berry's 1998 work synthesized the theory of wavefront dislocations and vortices, showing their topological nature and universal properties.

The paper marked the birth of "singular optics"—the study of structured light with vortices, knots, and more exotic topologies. This field has grown to become central in contemporary photonics and quantum optics.

---

## Key Arguments and Derivations

### Definition of Optical Vortices

For a monochromatic light field described by a complex amplitude:

$E(\vec{r}) = A(\vec{r}) e^{i\phi(\vec{r})}$

where $A(\vec{r})$ is the real amplitude and $\phi(\vec{r})$ is the phase. An optical vortex is a point (in 2D) or line (in 3D) where $A(\vec{r}) = 0$ and the phase is singular.

The topological charge (winding number) is:

$m = \frac{1}{2\pi} \oint \nabla \phi \cdot d\vec{l}$

where the circulation is around a closed loop encircling the vortex core. For a simple vortex, $m = \pm 1, \pm 2, \ldots$ is an integer.

The phase near a vortex of charge $m$ behaves as:

$\phi(\vec{r}) \approx m \theta + \text{smooth corrections}$

where $\theta$ is the azimuthal angle around the vortex core. The phase winds $m$ times around the core as $\theta$ goes from 0 to $2\pi$.

### Wavefront Dislocations

A wavefront dislocation is a line of discontinuity in the phase—analogous to a screw dislocation in a crystal lattice. Along the dislocation line, the phase jumps by $2\pi m$ (where $m$ is the charge), and the wavefronts (surfaces of constant phase) have a helical structure winding around the dislocation.

In 2D, a line of phase dislocation projects as a point—the vortex core. In 3D, vortex lines can be knotted or linked, creating rich topological structures.

The density of wavefront dislocations in a random wave field $E(\vec{r})$ of wavelength $\lambda$ is:

$n = \frac{1}{\pi^2 \lambda^2}$

This result, derived by Nye and Berry, shows that dislocations are generic—every random wave field has a finite density of vortices.

### Orbital Angular Momentum

A light field with an optical vortex of charge $m$ carries orbital angular momentum. The angular momentum density is:

$\vec{L} = \epsilon_0 c \, (\vec{r} \times (\vec{E} \times \vec{B}))$

For a paraxial beam with a vortex of charge $m$, the total orbital angular momentum per photon is:

$L_z = m \hbar$

This is in addition to the spin angular momentum from polarization. A vortex of charge $m=2$ carries twice the angular momentum of a circularly polarized photon.

### Orbital Angular Momentum Density

The z-component of angular momentum density (for light propagating in the z-direction) is:

$L_z = \epsilon_0 \, r^2 E^* \frac{\partial E}{\partial \phi} + \text{h.c.}$

where $\phi$ is the azimuthal coordinate. For a vortex of charge $m$:

$L_z \sim m |E|^2$

The angular momentum is distributed around the vortex core. The total angular momentum flux (integrated over a cross-section) is proportional to $m \hbar$, independent of the beam size or shape.

### Generic Appearance of Vortices

Berry showed that optical vortices are not anomalies but generic features of wave fields. In any 2D random field, vortices appear with characteristic density $\sim 1/\lambda^2$. They can be created by:

1. Interference of two plane waves at a small angle
2. Phase modulation by a spatial light modulator
3. Propagation of Laguerre-Gaussian beams
4. Any structured optical field

The key insight is that vortex formation is topological: wherever the phase has a singularity (a point where the real and imaginary parts of $E$ both vanish, with $\nabla \phi$ singular), a vortex exists. This is as generic as zeros of polynomials.

### Connection to Geometric Phase

Optical vortices are intimately related to the Berry phase. The phase accumulated by a wave circulating around a vortex core is determined by the topological charge:

$\gamma = \oint \nabla \phi \cdot d\vec{l} = 2\pi m$

where $m$ is the topological charge (winding number). This quantized phase is the optical analog of the Aharonov-Bohm phase accumulated by an electron encircling a magnetic flux tube.

---

## Key Results

1. **Optical vortices are generic**: Phase singularities appear naturally in random wave fields, with density $\sim 1/(\pi^2 \lambda^2)$ for wavelength $\lambda$.

2. **Topological charge conservation**: Vortices of opposite charge can annihilate, but the total topological charge is conserved in time-reversal symmetric processes. This is a topological conservation law.

3. **Orbital angular momentum quantization**: A vortex of charge $m$ carries orbital angular momentum $m \hbar$ per photon, which can be transferred to matter (mechanical systems, atoms, etc.).

4. **Wavefront structure**: The phase field around a vortex has helical wavefronts—surfaces of constant phase wind around the vortex core like a screw thread.

5. **Experimental generation**: Optical vortices can be easily generated using computer-generated holograms, spatial light modulators, or mode converters, enabling practical applications.

---

## Impact and Legacy

Berry's 1998 work catalyzed the field of singular optics:

- **Optical manipulation**: Vortex beams (Laguerre-Gaussian modes) can exert torque on microscopic objects, enabling optical spinning and rotation of biological cells and colloidal particles.
- **Quantum information**: Vortex beams are used in quantum communication protocols exploiting orbital angular momentum as an additional quantum number.
- **Fundamental physics**: Vortices in light illuminate the topological structure of wave phenomena and provide analogs to topological defects in condensed matter and cosmology.
- **Material structuring**: Vortex beams can be used to create structured light for direct laser writing and material manipulation.
- **Astronomy**: Vortex coronagraphs suppress starlight in exoplanet imaging by exploiting the zero intensity at the vortex core.

The recognition that phase singularities are generic and useful has become foundational in modern photonics.

---

## Connection to Phonon-Exflation Framework

Optical vortices provide an important conceptual analogy for understanding topological defects in the phonon-exflation framework:

1. **Phase singularities in the Dirac spectrum**: The avoided crossings in the Dirac spectrum (e.g., sector (3,0)-(2,0)) can be thought of as phase singularities in eigenvalue space. Just as optical vortices have a topological charge (winding number), the avoided crossings have a quantized Berry phase $\gamma = \pi$.

2. **Topological charge conservation**: In the phonon spectrum, the total topological charge (total Berry phase from all avoided crossings) is conserved under smooth deformations of the metric. This mirrors the conservation of total optical vorticity.

3. **Helical phase structure**: The phase of the phonon wavefunction around an avoided crossing has helical structure in modulus space, analogous to the helical wavefront of an optical vortex.

4. **Angular momentum analogs**: In the internal space SU(3), phonons near avoided crossings carry "internal angular momentum" analogous to the orbital angular momentum of optical vortices. This could be related to isospin and generation mixing.

5. **Generic appearance**: Just as optical vortices are generic in random wave fields, topological defects in the Dirac spectrum might be generic features of any curved internal geometry. Their density and charge distribution encode information about the curvature.

6. **Thermal effects**: Phonons in a thermal bath could interact with topological defects in the spectrum, analogous to how optical vortices can trap and rotate particles. This affects thermal properties and transport coefficients.

Optical vortices are a concrete, well-studied example of topological defects in wave phenomena, providing intuition for understanding topological structure in the phonon-exflation spectrum.
