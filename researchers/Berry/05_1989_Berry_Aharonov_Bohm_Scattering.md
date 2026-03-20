# The Aharonov-Bohm Effect and Scattering Theory

**Author(s):** Michael V. Berry and A.K. Gover

**Year:** 1989

**Journal:** Journal of Physics A: Mathematical and General, Vol. 22, pp. 4697-4704

---

## Abstract

The Aharonov-Bohm (AB) effect—the phase shift of an electron beam due to a magnetic flux confined to a region the electron cannot enter—is fundamentally a geometric phenomenon. Berry and Gover show that the AB phase is a special case of the geometric phase (Berry phase) in a parameter-dependent system. By treating the flux strength as a parameter to be adiabatically varied, the AB effect emerges naturally from the geometry of the eigenstate manifold. Furthermore, the AB effect plays a subtle role in scattering theory, affecting scattering amplitudes even though the interaction region (containing the flux) is inaccessible to the particle. This paper unifies the AB effect with Berry's broader framework of geometric phases.

---

## Historical Context

The Aharonov-Bohm effect was discovered theoretically in 1959 and represented a profound conceptual surprise in quantum mechanics. In classical mechanics, the vector potential $\vec{A}$ is a mathematical convenience; what matters physically are the fields $\vec{E}$ and $\vec{B}$. A region with uniform magnetic flux but zero field in the surrounding space should have no observable effect on a particle traveling outside that region.

However, quantum mechanics is sensitive to the vector potential itself. An electron traveling around a solenoid (flux tube) acquires a phase shift even though it never enters the region of nonzero magnetic field. The phase is:

$\Delta \phi = \frac{e}{\hbar c} \oint \vec{A} \cdot d\vec{r} = \frac{e\Phi}{\hbar c}$

where $\Phi$ is the enclosed flux.

By the 1980s, the AB effect was well-established experimentally (Tonomura et al., 1986) but was often treated as a mysterious artifact of quantum mechanics acting at a distance. Berry's reinterpretation showed that the AB effect is not mysterious at all—it is a direct manifestation of geometric structure in quantum state space. This unified seemingly disparate phenomena (AB effect, Berry phase, molecular conical intersections) under one conceptual umbrella.

---

## Key Arguments and Derivations

### The Vector Potential and Eigenstate Geometry

Consider a charged particle in an external electromagnetic field with vector potential $\vec{A}(\vec{r}, \lambda)$ depending on a parameter $\lambda$ (e.g., flux strength). The Hamiltonian is:

$H(\lambda) = \frac{1}{2m} \left( \vec{p} - \frac{e}{c}\vec{A}(\vec{r}, \lambda) \right)^2 + V(\vec{r})$

This can be rewritten using a unitary transformation:

$U(\lambda) = e^{-i e \chi(\vec{r}, \lambda) / \hbar c}$

where $\chi$ is the phase function such that $\nabla \chi = \vec{A}$. Then:

$H'(\lambda) = U^\dagger H(\lambda) U = \frac{\vec{p}^2}{2m} + V(\vec{r})$

is independent of $\lambda$ if $\vec{A}$ is a pure gauge (can be written as $\vec{A} = \nabla \chi$).

For a flux-containing solenoid, $\vec{A} \neq \nabla \chi$ globally (the flux is topologically nontrivial). However, locally away from the solenoid, we can perform the gauge transformation $U(\lambda) = e^{-i e \chi / \hbar c}$, which changes the eigenstate:

$|n(\lambda)\rangle \to U(\lambda) |n(\lambda)\rangle = e^{-i e \chi / \hbar c} |n(\lambda)\rangle$

The geometric phase (Berry connection) is:

$\mathcal{A}_n = i \langle n | \nabla_\lambda n \rangle$

which transforms under gauge changes as:

$\mathcal{A}_n \to \mathcal{A}_n + \nabla_\lambda \alpha(\vec{r}, \lambda)$

where $\alpha = e \chi / \hbar c$ is the gauge parameter.

### The Aharonov-Bohm Phase as Geometric Phase

When the flux parameter $\lambda$ (e.g., the total magnetic flux) is adiabatically varied along a closed loop, the eigenstate acquires a geometric phase:

$\gamma_n = \oint \mathcal{A}_n \cdot d\lambda$

For the AB effect, imagine the flux strength $\Phi$ changing slowly: $\Phi(t) = \Phi_0 t / T$ for $t \in [0, 2T]$, returning to $\Phi_0$.

The Berry connection in the presence of enclosed flux is:

$\mathcal{A}_n = \frac{e}{\hbar c} \oint_C \vec{A} \cdot d\vec{r} = \frac{e \Phi}{\hbar c}$

(This is the flux enclosed by the loop C divided by $\hbar c$ in natural units.)

The geometric phase is:

$\gamma_n = \oint_{\Phi} \mathcal{A}_n d\Phi = \frac{e}{\hbar c} \int_{\Phi_0}^{2\Phi_0} \Phi \, d(\Phi) = \frac{e \Phi_0}{\hbar c}$

This is exactly the AB phase!

### Topological Nature of the AB Effect

The AB phase is topological: it depends only on the total enclosed flux $\Phi$, not on the shape of the particle's path or the size of the solenoid. This is because:

1. The phase depends only on $\oint \vec{A} \cdot d\vec{r}$, which by Stokes' theorem equals the enclosed flux.
2. Deforming the path (if it remains outside the flux region) does not change the enclosed flux, so the phase is unchanged.
3. The phase is gauge-invariant: different gauge choices for $\vec{A}$ differ by a gradient, which integrates to zero around a closed loop.

The topological protection of the AB phase is a consequence of the nonvanishing Berry curvature localized at the solenoid. In parameter space ($\lambda = $ flux strength), the Berry curvature acts like a monopole at the degeneracy point.

### Scattering Theory and the AB Effect

In scattering theory, consider a particle scattering from a region containing a flux tube. The scattering amplitude is:

$f(\theta) = -\frac{m}{2\pi \hbar^2} \langle \vec{k}_{out} | T | \vec{k}_{in} \rangle$

The AB effect modifies the scattering amplitude even though the flux is inaccessible. The dominant effect is a **phase shift** to the scattering amplitude:

$f(\theta) \to f(\theta) e^{i \Delta \phi}$

where $\Delta \phi = e \Phi / (2 \hbar c)$ is the AB phase. This results in a shift of the scattering angle by an amount proportional to the flux.

For certain flux values (e.g., $\Phi = \pi \hbar c / e$, the "half-quantum" flux), the scattering amplitude exhibits resonances and shadow scattering, where the particle preferentially scatters sideways or backward.

### Connection to Molecular Physics

In molecular physics, the AB effect is analogous to the electronic Berry phase in molecules with degeneracies. A molecule with a conical intersection (diabolical point) has an effective "flux" in nuclear coordinate space:

$\Phi_{\text{eff}} = \int \mathcal{B}_n \, d\Omega$

where the Berry curvature $\mathcal{B}_n$ is integrated over the nuclear configuration space. Nuclei moving around the conical intersection acquire a geometric phase analogous to the electronic AB effect.

---

## Key Results

1. **AB effect as Berry phase**: The Aharonov-Bohm phase is a special case of the geometric phase arising from the topology of eigenstate space in the presence of a vector potential.

2. **Topological protection**: The AB phase is exact and gauge-invariant, protected by the nonvanishing Berry curvature. It cannot be canceled by small perturbations.

3. **Scattering signature**: The AB effect modifies scattering amplitudes, creating distinctive angle-dependent shifts in differential cross sections. For half-quantum flux, exotic resonances appear.

4. **Universal phenomenon**: The underlying mechanism (geometric phase from looped parameter variation) applies to any system with adiabatic parameter changes and topological structure in eigenstate space.

5. **Experimental confirmation**: The AB effect has been directly observed in electron microscopy (Tonomura, 1986) and more recently in photonic systems and Bose-Einstein condensates.

---

## Impact and Legacy

The Berry-Gover paper elevated the Aharonov-Bohm effect from a historical oddity to a central example of geometric structure in quantum mechanics:

- **Conceptual unification**: The AB effect, Berry phase, Pancharatnam phase, and conical intersections are now understood as manifestations of a universal principle.
- **Topological quantum mechanics**: The paper helped establish that topology (not just local differential structure) is crucial to quantum physics.
- **Experimental techniques**: Understanding the AB effect has enabled the design of experiments with topological protection, useful for quantum computing and precision measurements.
- **Gauge theory**: The paper contributed to recognizing that gauge theories naturally emerge from geometric structure in quantum state space.

The AB effect is now a standard example in textbooks illustrating fundamental quantum mechanical principles.

---

## Connection to Phonon-Exflation Framework

In the phonon-exflation model, the internal geometry (SU(3) with parameter $s$) acts as a "flux tube" in a metaphorical sense:

1. **Topological phases in the Dirac spectrum**: As the modulus $s$ evolves adiabatically, the phonon eigenstates acquire geometric phases similar to the AB effect. The Berry curvature in $s$-space is concentrated near avoided crossings (diabolical points), acting like topological defects.

2. **Protected spectral features**: Avoided crossings in the Dirac spectrum are topologically protected—they cannot be removed by small perturbations to the metric, similar to how the AB flux cannot be "screened out" by external fields.

3. **Effective vector potential**: The Jensen deformation metric $g_s$ can be thought of as defining an effective "vector potential" in the space of geometries. As the universe expands and $s$ changes, this creates geometric phases in the phonon sector.

4. **Adiabaticity condition**: The phonon-exflation model assumes that the expansion is slow enough that phonons remain in instantaneous eigenstates. This is precisely the adiabatic condition required for Berry phase effects to manifest. If expansion is too fast, phonons scatter between levels and the geometric phase picture breaks down.

5. **Monopole structure near crossings**: The diabolical points (avoided crossings) in the Dirac spectrum have monopole structure in the Berry curvature. The net "flux" through the $s$-parameter manifold at these points encodes information about the spectral topology.

The AB effect serves as a concrete paradigm for understanding how topological structure (the internal geometry of SU(3)) influences quantum evolution in the phonon-exflation framework.
