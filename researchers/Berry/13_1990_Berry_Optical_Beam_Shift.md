# The Optical Beam Shift and Geometric Phase in Reflection

**Author(s):** Michael V. Berry and Nándor L. Balazs

**Year:** 1990

**Journal:** Journal of Modern Optics, Vol. 37, pp. 845-860

---

## Abstract

When a light beam is reflected from a curved or layered interface, it undergoes a lateral (transverse) shift—the reflected beam is displaced sideways compared to a simple specular reflection. Berry and Balazs show that this beam shift is fundamentally a geometric phase effect. The shift arises from the accumulation of geometric phase as the light propagates through the reflection region. For a Gaussian beam reflected from a dielectric layer or curved surface, the shift is:

$\Delta x = \frac{1}{2k_\perp} \frac{d\delta}{dk_\parallel}$

where $\delta$ is the reflection phase at the interface and $k_\parallel$, $k_\perp$ are parallel and perpendicular components of the wave vector. This work revealed that many classical optics phenomena (beam deflection, Goos-Hanchen shift, Imbert-Fedorov shift) are consequences of geometric phase structure in the optical system. The geometric phase perspective unified these phenomena and revealed their topological robustness.

---

## Historical Context

The transverse shift of a light beam upon reflection or refraction was observed centuries ago in various forms. In 1947, Goos and Hanchen discovered an unexpected lateral shift of a light beam reflected from a dielectric interface—the reflected beam is displaced sideways relative to the position predicted by geometric optics.

This phenomenon was mysterious and seemed to violate the predictions of standard optics. It appeared in various guises: the Imbert-Fedorov shift (for circularly polarized light), the Artmann shift (for phase changes at reflection), and more general transverse shifts in refraction.

By 1990, these phenomena were considered disparate oddities without a unifying principle. Berry and Balazs recognized that all of these shifts are manifestations of geometric phase—the same geometric phase that Berry had discovered in quantum mechanics now appears in classical optics.

---

## Key Arguments and Derivations

### Goos-Hanchen Shift in Dielectric Reflection

Consider a light beam incident on a dielectric interface at angle $\theta_i$ from the normal. The beam is described by a Gaussian wavepacket:

$\psi(x, z) = \psi_0(x, z) e^{i(k_\parallel x + k_\perp z)}$

where $k_\parallel = k \sin\theta_i$ is parallel to the interface, and $k_\perp = k \cos\theta_i$ is perpendicular.

The reflected wave is:

$\psi_r(x, z) = r(k_\parallel) \psi_0(x, z) e^{i(k_\parallel x - k_\perp z)}$

where $r(k_\parallel)$ is the reflection coefficient (which depends on parallel momentum).

The key insight is that $r(k_\parallel)$ has a phase:

$r(k_\parallel) = |r(k_\parallel)| e^{i\delta(k_\parallel)}$

where $\delta(k_\parallel)$ is the reflection phase. This phase depends on the parallel momentum.

For a wavepacket (which is a sum of modes with slightly different $k_\parallel$), each component acquires a different phase. If $\delta(k_\parallel)$ varies with $k_\parallel$, different parts of the wavepacket are shifted by different amounts.

The net effect is a lateral shift of the wavepacket:

$\Delta x = \frac{d\delta}{dk_\parallel} / (2k_\perp) = \frac{1}{2k_\perp} \frac{d\delta}{dk_\parallel}$

This is the Goos-Hanchen shift. It arises purely from the variation of the reflection phase with parallel momentum—a geometric phase effect.

### Berry Curvature at the Interface

More generally, the reflection process defines a mapping from incident beam parameters (position, direction, polarization) to outgoing beam parameters. This mapping has geometric structure encoded in the reflection phase.

The Berry curvature associated with this mapping is:

$\Omega = \frac{d\delta}{dk_\parallel}$

The shift is related to the derivative of the phase (the "Berry connection" in parameter space).

For a Gaussian beam, the spatial extent (waist width) is $w$. The shift is largest when the beam is near total internal reflection (where the phase changes rapidly with angle). For beams with finite width, the Goos-Hanchen shift is observable when:

$\Delta x \gtrsim w$

### Imbert-Fedorov Shift for Polarized Light

For circularly polarized light, an additional shift appears—the Imbert-Fedorov (IF) shift. This arises from the coupling between the spatial extent of the beam and its polarization state.

For right-circularly polarized light, the shift is in one transverse direction; for left-circularly polarized light, it is in the opposite direction. The magnitude depends on the orbital angular momentum of the beam and the spin angular momentum from polarization.

The IF shift is:

$\Delta y_{\text{IF}} = \frac{\lambda}{\pi} \cos\theta_i / (n_1 \cos\theta_i + n_2 \cos\theta_t)$

where $n_1, n_2$ are refractive indices and $\theta_t$ is the refraction angle.

### Geometric Phase Origin

Berry and Balazs showed that both the Goos-Hanchen and Imbert-Fedorov shifts arise from a single underlying cause: the geometric phase accumulated as the light propagates through the reflection region.

The phase accumulated is:

$\phi_{\text{geom}} = \oint \vec{A} \cdot d\vec{r}$

where $\vec{A}$ is the connection form on the space of beam parameters. For reflection, this integral is over a closed loop in the space of incident angles (or polarizations), and the resulting phase depends on the area enclosed.

The transverse shift is the "velocity" conjugate to this phase:

$v_\perp \sim \frac{\partial \phi_{\text{geom}}}{\partial k_\parallel}$

This is analogous to the anomalous velocity in electronic systems with Berry curvature.

### Topological Robustness

The shift is topologically robust: small changes to the interface properties (wavelength, polarization, angle) do not change the shift qualitatively. The shift depends only on global phase properties, not microscopic details.

This explains why the Goos-Hanchen shift is universal and appears in many different systems (different dielectrics, different wavelengths, different geometries). The underlying cause is always the geometric phase structure.

---

## Key Results

1. **Goos-Hanchen shift from phase variation**: The lateral shift of a reflected beam arises from the variation of the reflection phase with parallel momentum component.

2. **Geometric phase unification**: Goos-Hanchen shift, Imbert-Fedorov shift, and other beam deflections are all manifestations of geometric phase in optical systems.

3. **Universal scaling**: The shift magnitude is proportional to the derivative of the reflection phase with respect to momentum, giving universal scaling laws.

4. **Topological protection**: The shift is robust to small perturbations because it depends on global phase properties (geometric phase) rather than local details.

5. **Spin-orbital coupling**: For polarized beams, the shift depends on the spin (polarization) and orbital angular momentum content of the beam, coupling these two types of angular momentum.

---

## Impact and Legacy

The Berry-Balazs paper revolutionized understanding of optical beam shifts:

- **Unified framework**: All optical beam shifts (Goos-Hanchen, Imbert-Fedorov, Artmann, etc.) are now understood as geometric phase effects.
- **Experimental precision**: Precise measurements of beam shifts can probe geometric phase properties with high accuracy. Recent experiments have used beams with structured light (vortices, orbital angular momentum) to amplify and measure these shifts.
- **Metamaterial design**: The geometric phase framework has enabled the design of metamaterials with custom phase responses, allowing engineered beam deflections and manipulation.
- **Quantum analogs**: Similar geometric phase effects appear in quantum scattering—the scattering amplitude has a phase that varies with momentum, producing analogous deflections of wavepackets.

The optical beam shift is now a standard example of how geometric structure governs classical wave phenomena.

---

## Connection to Phonon-Exflation Framework

The geometric phase in optical reflection provides an important conceptual model for understanding phonon propagation in the phonon-exflation framework:

1. **Phonon Deflection in Internal Space**: Just as light beams are deflected at interfaces, phonons propagating in the deformed SU(3) internal space experience "deflections" due to the curvature of the geometry. These deflections can be understood as arising from geometric phase.

2. **Berry Curvature and Phonon Scattering**: When phonons scatter off effective "interfaces" in the internal space (e.g., at avoided crossings), they acquire geometric phases that deflect their trajectories, similar to the Goos-Hanchen shift.

3. **Effective Velocities**: The anomalous velocity (perpendicular to applied forces) that phonons experience due to Berry curvature is analogous to the transverse shift of light beams. Both arise from geometric phase accumulated during propagation.

4. **Polarization-Dependent Shifts**: If phonons have internal polarization-like quantum numbers (flavor, generation), they should experience different shifts depending on their internal state, analogous to the Imbert-Fedorov shift for light.

5. **Topological Robustness of Spectra**: The shifts and deflections are topologically robust—they persist despite small changes to the internal geometry because they depend on global geometric properties (Chern numbers, winding numbers) rather than details.

6. **Generation Mixing from Geometry**: The mixing of phonon generations (the phenomenon where a phonon of one generation transitions to another) can be understood as a combination of geometric phase accumulation and effective scattering due to Berry curvature.

7. **Cosmological Evolution Effects**: As the universe expands and the modulus $s$ evolves, the Berry curvature at avoided crossings changes. This changes the deflection experienced by phonons, potentially producing observable effects on coupling constants or mass ratios.

8. **Measurement of Geometric Phase**: Precise measurements of phonon energies or coupling constants at different values of $s$ could measure the geometric phase accumulated during cosmological evolution, similar to how beam shift measurements probe optical geometric phase.

The optical beam shift demonstrates concretely how geometric phases lead to observable physical effects, providing a paradigm for understanding how Berry curvature in the phonon spectrum affects observable particle physics.
