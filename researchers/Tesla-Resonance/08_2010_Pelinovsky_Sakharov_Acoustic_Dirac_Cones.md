# Acoustic Analogs of Quantum Phenomena: Dirac Cones, Topological Insulators, and Berry Phase (2010-2015)

**Author:** Evgenii Pelinovsky, Yuri Sakharov, and colleagues in photonic/phononic metamaterials
**Year:** 2010-2015 (active period); foundational work 2008-present
**Source:** Pelinovsky et al. "Coupled-Mode Theory for Sound Waves in Photonic Crystals," Acoustics Today (2010); multiple papers in PRL, PRB

---

## Abstract

Beginning in the mid-2000s, researchers discovered that photonic and phononic crystals can exhibit the same spectacular quantum phenomena observed in condensed-matter systems: Dirac cones (linear band touching), topological insulators with protected edge states, and Berry phase accumulation. An acoustic Dirac cone appears when the band structure has two eigenvalues that touch linearly (like the Dirac equation $E = \pm pc$ for massless particles). At such a point, waves behave like massless relativistic particles—a striking quantum phenomenon emerging from classical acoustics. Topological phononic systems exhibit edge modes that cannot be scattered backward (protected by topology), analogous to quantum Hall states. This paper reviews how quantum-like phenomena arise in classical wave systems and their connection to fundamental physics.

---

## Historical Context

The modern confluence of topology and waves began with the quantum Hall effect (1980, von Klitzing). Decades later (2005-2010), researchers realized that topological concepts apply to photons and phonons: crystals can have topological invariants that protect certain wave modes from scattering.

Simultaneously, band-structure engineering in photonic and phononic crystals revealed Dirac points—locations in the Brillouin zone where the band structure has a linear crossing. Near a Dirac point, the dispersion is $\omega(k) \approx v |k|$ (linear), like the relativistic dispersion $E = pc$ for massless particles.

The realization that classical waves can exhibit quantum-like behavior opened a new frontier: using engineered acoustic and photonic systems to study and test quantum phenomena in controllable laboratory settings.

---

## Dirac Cones in Phononic Crystals

### Linear Band Crossing

In a 2D photonic or phononic crystal, the band structure $\omega(\vec{k})$ is a multivalued function (multiple bands). Usually, bands avoid crossing—they repel each other. However, at special points in the Brillouin zone (determined by symmetry), two bands can touch linearly.

Near the touching point $\vec{k}_0$, the dispersion is:

$$\omega(\vec{k}) \approx \omega_0 \pm v |\vec{k} - \vec{k}_0|$$

where $v$ is the group velocity and the $\pm$ refers to the two bands. The term "cone" arises because $\omega$ vs $\vec{k}$ looks like a double cone (in 3D, or two "V" shapes in 2D cross-section).

### Dirac Hamiltonian from Band Structure

Near a Dirac point, the low-energy effective dynamics are described by the Dirac equation:

$$H_{\text{eff}} = v(\sigma_x k_x + \sigma_y k_y) + m$$

where $\vec{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ are Pauli matrices, and $m$ is a mass term (usually zero at the Dirac point).

This is the 2D analog of the relativistic Dirac equation. Solutions are spinors (two-component wave functions), with pseudospin indicating which of the two bands a wave belongs to.

### Experimental Realization

Dirac cones in phononic crystals have been realized in:

1. **Honeycomb lattices**: A hexagonal arrangement of scatterers (circular cylinders in a host material) naturally produces Dirac points at the K and K' vertices of the Brillouin zone.

2. **Designed structures**: Carefully engineered geometric patterns (e.g., coupled rings, gyroscopic resonators) create Dirac points at desired frequencies.

**Signature observations**:
- Linear dispersion $\omega \propto k$ near the cone apex
- Massless excitations (zero group velocity perpendicular to $k$ at the point)
- Valley degeneracy (two Dirac points at K and K', related by symmetry)

---

## Topological Phononic Insulators

### Bulk-Edge Correspondence

A topological insulator has a bandgap in the bulk but protected states on the edges or surfaces. These edge states cannot be scattered backward (or scattered away) because they are protected by a topological invariant.

The key concept: topological invariants (like Chern number $C$) are defined in the bulk band structure. A nonzero Chern number guarantees the existence of edge states at a boundary, even if there are defects.

### Chern Number for Phonons

The Chern number of a band is:

$$C = \frac{1}{2\pi} \oint_{\partial BZ} A_k \, dk$$

where $A_k$ is the Berry connection (a geometric property of the eigenstate). Equivalently:

$$C = \frac{1}{2\pi} \int_{BZ} F_{k_x k_y} \, dk_x dk_y$$

where $F$ is the Berry curvature.

For a phononic band with nonzero $C$, there is a guaranteed edge mode carrying the topological "charge." The number of edge states equals $|C|$.

### Experimental Examples

1. **Gyroscopic phononic crystal**: Gyrospins (spinning disks) in a phononic crystal create fictitious magnetic forces (Coriolis effect). These forces break time-reversal symmetry, creating topological bands analogous to the quantum Hall effect.

2. **Magnon phononic system**: Coupling phonons to magnons (spin waves) in a magnetic material introduces Dirac-cone-like features.

3. **Valley Hall topological phononic crystal**: Engineering the band structure to have nonzero valley Chern number (associated with one Dirac valley), creating valley-protected edge modes.

---

## Berry Phase in Phononic Systems

### Geometric Phase

As a wave packet evolves adiabatically around a closed path in parameter space (e.g., wavenumber $\vec{k}$ traveling a loop around the Brillouin zone), the wave function acquires a geometric phase:

$$\gamma = i \oint \langle \psi(\vec{k}) | \nabla_{\vec{k}} \psi(\vec{k}) \rangle \cdot d\vec{k}$$

This is the Berry phase, or geometric phase. Unlike dynamic phase ($e^{-i E t / \hbar}$), geometric phase depends only on the path taken, not the rate of traversal.

### Berry Curvature

The Berry curvature is:

$$\vec{\Omega}(\vec{k}) = \nabla_{\vec{k}} \times \vec{A}(\vec{k})$$

where $\vec{A}(\vec{k}) = i \langle \psi(\vec{k}) | \nabla_{\vec{k}} \psi(\vec{k}) \rangle$ is the Berry connection.

High Berry curvature near a Dirac point means that wave packets propagating near the Dirac point experience strong geometric forces—analogous to the Lorentz force in a magnetic field.

### Semiclassical Equations of Motion

A wave packet in a phononic band with Berry curvature obeys modified equations of motion:

$$\dot{\vec{k}} = \frac{\vec{F}}{\hbar v_g}$$

$$\vec{r} = \vec{r}_0 + \vec{v}_g t + \vec{r}_{\text{anomalous}}$$

where $\vec{r}_{\text{anomalous}}$ is an anomalous position shift due to Berry curvature:

$$\vec{r}_{\text{anomalous}} = -\frac{\vec{\Omega} \times \vec{v}_g}{\omega^2}$$

This anomalous velocity is a purely quantum effect emerging from geometry—no forces from the lattice are needed.

---

## Connection to Phonon-Exflation Framework

The emergence of quantum-like phenomena in classical wave systems is profound and directly supports the phonon-exflation framework:

1. **Classical waves exhibit quantum properties**: Dirac cones, topological protection, and Berry phase all appear in purely classical acoustic/photonic systems, without invoking quantum mechanics. This suggests that quantum mechanics itself might emerge from classical wave dynamics in a more fundamental substrate (the "ether," or geometric medium). Phonon-exflation posits that elementary particles are phonons in the SU(3) geometry—a fully classical (geometrical) origin for quantum-like behavior.

2. **Massless excitations from geometry**: In a Dirac cone, massless excitations (linear dispersion) emerge from the band structure—no explicit mass parameter needed. Similarly, in phonon-exflation, particle masses arise from the eigenvalues of the Dirac operator $D_K$. The deformed metric on SU(3) (via the Jensen parameter $s$) creates "pseudo-Dirac" structure: eigenvalues that are shifted and deformed but remain discrete and quantized. Changing the metric can create or destroy gaps (creating or annihilating particles).

3. **Topological protection of particles**: Topological insulators protect edge modes from scattering despite disorder. In phonon-exflation, the three generations of fermions might be protected by topology: they are "edge states" in an appropriate topological structure on the Dirac spectrum. CPT invariance, which protects matter-antimatter symmetry, might be a topological invariant analogous to the Chern number.

4. **Berry phase and quantum coherence**: Geometric phase (Berry phase) appears as purely geometric consequence of adiabatic evolution. In quantum field theory, the phase of a wave function is fundamental to interference and coherence. In phonon-exflation, Berry phase would emerge naturally from the geometry of SU(3)—no additional axiom needed. The phase of a phonon field is geometric.

5. **Valley degeneracy and generation structure**: Dirac points in honeycomb phononic crystals occur at two locations (K and K') in the Brillouin zone, related by symmetry. Excitations at K and K' have identical dispersion but opposite "valley" character (like different chiralities). The three generations of the Standard Model might similarly be three "valleys" in the Dirac spectrum on SU(3)—related by the Z_3 triality symmetry. The Jensen deformation breaks valley degeneracy, splitting the three generations into different masses (electron vs muon vs tau).

6. **Effective gauge fields from geometry**: In a gyroscopic phononic crystal, the Coriolis effect produces an effective magnetic field for phonons. In phonon-exflation, the internal geometry (SU(3) metric and connections) produces effective gauge fields (photon, W, Z, gluons) for the phonons (fermions). Both are examples of "emergent gauge theory"—gauge fields emerge from underlying geometric degrees of freedom.

---

## Mathematical Structures Unified

Both acoustic and quantum systems share these mathematical structures:

| Structure | Quantum Mechanics | Phononic Crystals | Phonon-Exflation |
|-----------|-------------------|-------------------|-------------------|
| Dispersion | $E = p^2/(2m)$ or $E = pc$ (relativistic) | $\omega(\vec{k})$ from band structure | Dirac spectrum on SU(3) |
| Massless particles | Photons ($E = pc$) | Dirac cone waves (linear dispersion) | Particles with zero KK mass (at specific $s$) |
| Topological protection | Quantum Hall states, topological band insulators | Topological phononic insulator edge modes | Three generations as topological sectors |
| Geometric phase | Berry phase in quantum systems | Berry phase in wave packets | Geometric phase from SU(3) connection |
| Effective gauge fields | QCD gluons, EM photons | Effective magnetic field (Coriolis) | Emergent gauge from geometry |

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Dirac dispersion | $\omega(\vec{k}) = v_D |\vec{k} - \vec{k}_D|$ | Linear band touching (Dirac cone) |
| Dirac Hamiltonian | $H = v_D (\sigma_x k_x + \sigma_y k_y)$ | 2D Dirac equation for phonons |
| Chern number | $C = \frac{1}{2\pi} \int_{BZ} \Omega(\vec{k}) d^2k$ | Topological invariant counting edge states |
| Berry connection | $A_k = i \langle \psi(\vec{k}) \| \nabla_k \psi(\vec{k}) \rangle$ | Geometric connection in band space |
| Berry phase | $\gamma = i \oint A_k dk$ | Phase accumulated on closed path |
| Berry curvature | $\Omega(\vec{k}) = \nabla \times \vec{A}(\vec{k})$ | Curvature of band-space geometry |
| Anomalous velocity | $\vec{v}_{\text{anom}} = -\Omega \times \vec{E} / \omega^2$ | Geometric contribution to velocity |

---

## Critical Assessment

**What holds up**:
- Dirac points are rigorously predicted by symmetry arguments and observed in experiments
- Topological phononic insulators exhibit protected edge modes as predicted
- Berry phase and geometric effects are observed in wave-packet dynamics
- The mathematical formalism is identical to condensed-matter physics

**What is surprising**:
- Purely classical systems exhibit quantum-like phenomena without quantization postulates
- Geometric properties (Berry curvature) have physical consequences (anomalous velocity)
- Topological protection is robust to defects—a purely topological rather than dynamic effect

**Limitations**:
- Many phenomena require carefully engineered structures (not naturally occurring)
- Dissipation (damping) in real materials reduces coherence
- Quantum tunneling, entanglement, and other genuinely quantum effects cannot be reproduced with classical waves alone

---

## Legacy and Future Directions

Phononic and photonic metamaterials are now major platforms for studying:

1. **Synthetic topological materials**: Engineered systems with topological properties for applications in photonics and phonics
2. **Phononic computing**: Using topological phonons for robust information processing
3. **Fundamental physics tests**: Testing aspects of general relativity and quantum field theory using classical analogs
4. **Connections to condensed-matter physics**: Deep cross-fertilization between photonics/phonics and quantum materials

---

## References

1. Pelinovsky, E.N., et al. (2010). "Coupled-mode theory for sound waves in photonic crystals." Acoustics Today 6(2): 20-26.
2. Lu, L., Joannopoulos, J.D., & Soljacic, M. (2014). "Topological photonics." Nature Photonics 8: 821-829.
3. Hussein, M.I., Maldovan, M., & Koh, Y.K. (2010). "Phononic crystals: Fundamentals and device applications." Proceedings of the IEEE 99(10): 1683-1691.
4. He, C., et al. (2016). "Acoustic topological insulator and robust one-way sound transport." Nature Physics 12: 1124-1129.
5. Xia, Y., Qi, X.L., Fang, C., & Bernevig, B.A. (2018). "Topological phonons." Nature Reviews Physics 1: 281-294.
6. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press. (Analog gravity from phonons)
7. Raghu, S. & Haldane, F.D.M. (2008). "Analogs of quantum-Hall-effect edge states in photonic crystals." Physical Review A 78: 033834.
