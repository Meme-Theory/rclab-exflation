# Hydrodynamic Quantum Analogs

**Authors:** John W. M. Bush, Anand U. Oza
**Year:** 2021
**Journal:** Reports on Progress in Physics, Vol. 84, No. 1, Art. 017001

---

## Abstract

This comprehensive review examines how classical hydrodynamic systems can exhibit quantum-like behavior through the interaction of particles (droplets) with their own wave fields, providing a macroscopic realization of de Broglie's 1920s pilot-wave proposal. The walking droplet system, discovered experimentally by Couder and Fort (2005), consists of a millimeter-scale droplet bouncing on the surface of a vibrating liquid bath. The droplet's bouncing motion generates capillary waves that guide the droplet's horizontal motion—a pilot-wave mechanism. This macroscopic pilot-wave system exhibits: (1) wavelike diffraction and interference patterns in a double-slit analog experiment; (2) quantized orbital motion and angular momentum in a rotating bath; (3) quantum-like statistical behavior in scattering experiments; (4) temporal nonlocality arising from the persistent wave field memory. The review synthesizes experimental observations, theoretical models (from simple force laws to hydrodynamic quantum field theory), and connections to foundational issues in quantum mechanics, suggesting that hydrodynamic analogs offer new perspectives on the quantum-classical boundary and the role of pilot-wave dynamics in nature.

---

## Historical Context

The history of quantum mechanics is intertwined with debates about interpretation and mechanism:

1. **de Broglie's pilot-wave proposal (1923)**: Louis de Broglie proposed that particles are guided by pilot waves, with the particle always located at a definite position in space (realist interpretation). The wave field determines the probability of where the particle will be found.

2. **Quantum mechanical orthodoxy (1920s-1960s)**: The Copenhagen interpretation (Bohr, Heisenberg) became dominant, treating quantum objects as purely probabilistic with no underlying mechanism. de Broglie's idea was largely abandoned.

3. **Bohmian mechanics revival (1950s-present)**: David Bohm independently recovered and developed de Broglie's idea into a fully consistent non-local realist theory. This interpretation remains mathematically equivalent to standard quantum mechanics but offers an explicit mechanism.

4. **The walking droplet breakthrough (2005)**: Couder and Fort discovered that macroscopic oil droplets bouncing on the surface of a vibrating liquid bath exhibit pilot-wave dynamics. The droplet bounces in resonance with the liquid's waves, generating capillary waves that guide subsequent bounces. This was the first classical macroscopic realization of de Broglie's 1920s vision.

5. **Quantum analog phenomena (2010s)**: Multiple groups demonstrated that walking droplets exhibit quantum-like behavior: double-slit interference, energy quantization, statistical correlations mimicking quantum phenomena. The system provided a testable classical mechanism for quantum effects.

The Bush-Oza review consolidates two decades of walking droplet research, showing how hydrodynamic systems can bridge classical and quantum physics.

---

## Key Arguments and Derivations

### The Walking Droplet System

A droplet of viscous liquid (silicone oil, mass $m$, diameter $d \sim 1$ mm) bounces vertically on the surface of a shallow liquid bath that is vibrated horizontally at frequency $f = 80$ Hz (typical parameters). The bath oscillation is:

$$z_{\text{bath}}(t) = A \sin(2\pi f t)$$

where $A$ is the amplitude. At a critical acceleration ($\Gamma = A(2\pi f)^2 > g$, where $g$ is gravity), the bath surface becomes unstable—this is the Faraday instability, where the surface oscillates in response to driving.

The droplet bounces vertically at the Faraday frequency $f$, but if the bath is slightly anharmonic or the droplet is given a horizontal velocity, the droplet's trajectory becomes periodic in space and time. Each impact creates a capillary wave (ripple) on the liquid surface. These waves propagate outward and guide the droplet's subsequent motion.

The key insight: the droplet interacts with the **memory** of its past wave field. If the droplet moves horizontally, it creates a trail of capillary waves that decay on a timescale $\tau_m \sim 1/\lambda \omega_c$ (the "memory depth"). This temporal nonlocality—the droplet's current motion depends on the location and time of all past impacts—creates quantum-like statistics.

### Force Balance and Pilot-Wave Coupling

The droplet's horizontal equation of motion is:

$$m \ddot{x} = F_{\text{wave}} - D \dot{x}$$

where:
- $F_{\text{wave}}$ is the force exerted by the capillary wave field at the droplet's current position
- $D$ is a drag coefficient (from fluid viscosity)

The wave field $h(\mathbf{r}, t)$ satisfies a wave equation (for surface waves):

$$\partial_t^2 h + \Omega^2 h = f_{\text{impact}}(\mathbf{r}, t)$$

where $\Omega^2 = gk + \sigma k^3 / \rho$ is the dispersion relation for surface waves (gravity + surface tension), $\sigma$ is surface tension, $\rho$ is density. The forcing $f_{\text{impact}}$ is the impulse from droplet impacts:

$$f_{\text{impact}}(\mathbf{r}, t) = \sum_{i} \delta(\mathbf{r} - \mathbf{x}_i(t)) I_i(t)$$

summing over all impacts at positions $\mathbf{x}_i(t)$ at times $t_i$.

The force on the droplet is then:

$$F_{\text{wave}}(\mathbf{x}, t) = \nabla h(\mathbf{x}, t^-) \times (\text{contact area}) \times \rho g$$

This creates a feedback loop: the droplet's trajectory determines the wave field, which determines the force back on the droplet—a pilot-wave mechanism.

### Quantum-Like Single-Slit Diffraction

When a walking droplet approaches a slit of width $w$ in a barrier, its trajectory curves due to the wave field diffracted by the slit. The diffraction pattern is described by the Fresnel-Kirchhoff diffraction integral. For typical parameters:

- Droplet wavelength (de Broglie): $\lambda = v / f$ where $v$ is droplet speed and $f$ is bounce frequency
- Slit width: $w \sim 1$ mm
- Fresnel number: $F = w^2 / (\lambda L)$ where $L$ is distance to screen

When $F \sim 1$ (intermediate diffraction regime), the droplet's trajectory exhibits quantum-like diffraction. Multiple experimental runs with identical initial conditions produce a distribution of final positions mimicking the quantum diffraction pattern for a particle with de Broglie wavelength $\lambda$.

### Energy Quantization in a Rotating Bath

When the bath rotates with angular velocity $\Omega$, a walking droplet in the rotating frame experiences a Coriolis force and confining potential. The droplet can execute circular orbits at discrete radii, analogous to electron orbits in a Bohr atom.

The quantization condition arises from the standing wave pattern on a circular orbit. For a closed circular path:

$$\oint p \cdot dr = n h$$

where $p$ is the effective momentum (related to the droplet's wave number $k = 2\pi / \lambda$) and $n$ is an integer. This gives:

$$2\pi r k = 2\pi n$$

$$r = n \lambda$$

Discrete stable orbits occur when the circumference is an integer multiple of the wavelength—the standing wave condition. This is formally identical to the Bohr quantization rule and arises classically from the pilot-wave mechanism.

### Memory Effect and Temporal Nonlocality

The wave field created by a droplet impact decays on a timescale $\tau_m$. The droplet's future motion depends on the entire past trajectory integrated over the memory depth:

$$\mathbf{F}_{\text{wave}}(t) = \int_{t - \tau_m}^{t} dt' \, K(t - t') h(\mathbf{x}(t'), t')$$

where $K$ is a memory kernel. This temporal nonlocality (the future depends on past states in a non-Markovian way) is fundamentally different from standard Newtonian mechanics, where only the present state matters.

The temporal nonlocality can produce behavior that **appears** spatially nonlocal (particle affecting distant regions), even though the system is entirely local in space. This offers a classical mechanism for the apparent "spookiness" of quantum mechanics—non-locality at the phenomenological level can arise from temporal correlations in a memory-dependent classical system.

---

## Key Results

1. **Double-slit diffraction in walking droplets**: Experiments show that walking droplets, when forced through a double slit, produce an interference pattern similar to quantum double-slit experiments. The distribution of landing positions exhibits diffraction maxima and minima determined by the droplet wavelength and slit spacing.

2. **Energy and angular momentum quantization**: Walking droplets confined in a rotating bath orbit at quantized radii and angular momenta, with quantum numbers $n = 1, 2, 3, \ldots$. The orbital energies are quantized as $E_n = \hbar n \Omega$ in direct analogy to quantum angular momentum.

3. **Wavelike scattering statistics**: In scattering experiments (droplet approaching a potential barrier), the probability of transmission and reflection reproduce quantum mechanical results. At low energy (long wavelength relative to barrier width), reflection is enhanced; at high energy, transmission dominates.

4. **Band structure and Bloch waves**: Walking droplets in a periodic potential (array of barriers) exhibit band structure analogous to electrons in crystal. Allowed energy bands are separated by bandgaps where propagation is forbidden.

5. **Quantum tunneling analog**: Droplets can "tunnel" through classically forbidden barriers with an exponentially suppressed probability, mimicking quantum tunneling. The tunneling rate depends on barrier height and droplet wavelength in the same functional form as quantum tunneling.

6. **Non-Markovian dynamics confirmed**: The droplet's motion exhibits memory effects and temporal correlations that cannot be captured by Markovian (memoryless) equations. The persistent wave field creates long-range temporal correlations.

7. **Pilot-wave trajectory reconstruction**: Using high-speed imaging, the droplet trajectory can be reconstructed in real time, revealing a definite path (no quantum indeterminacy). Yet, the statistical behavior of many trajectories matches quantum predictions. This provides the first experimental evidence that realist pilot-wave mechanics can quantitatively reproduce quantum phenomena.

---

## Impact and Legacy

The walking droplet system has profound implications for quantum mechanics and our understanding of the quantum-classical boundary:

1. **Realist interpretation validation**: Walking droplets provide concrete experimental evidence that a realist interpretation (de Broglie-Bohm mechanics) is classically feasible. This challenges the conventional wisdom that quantum indeterminacy is fundamental rather than emergent from a hidden-variable pilot-wave mechanism.

2. **Macroscopic quantum-like behavior**: The system demonstrates that quantum-like phenomena (diffraction, interference, quantization, tunneling) can arise in purely classical macroscopic systems without quantum mechanics. This suggests that the boundary between quantum and classical is less sharp than previously thought.

3. **Memory and nonlocality**: The Bush-Oza review identifies temporal nonlocality as a key mechanism for generating apparent spatial nonlocality. This offers a new perspective on how quantum entanglement and EPR correlations might emerge from classical memory effects.

4. **Pedagogical impact**: Walking droplets have become a powerful teaching tool. Students can visualize quantum phenomena directly in the lab, mapping droplet trajectories and measuring interference patterns. This demystifies quantum mechanics and makes it tangible.

5. **Fluid dynamics of quantum mechanics**: The review proposes that quantum mechanics itself might have a hydrodynamic substrate—that the quantum field might be a fluid of some kind, with particles as excitations. This echoes ideas from fluid mechanics in relativity (analogue gravity, hydrodynamic duality).

6. **Foundational physics**: Walking droplets provide new angles on old questions: the measurement problem, the origin of quantum randomness, the role of pilot-wave fields, and the possibility of deterministic hidden variable theories. The Bush-Oza framework offers concrete models to test these ideas experimentally.

---

## Connection to Phonon-Exflation Framework

**Relevance: FOUNDATIONAL MECHANISM FOR PARTICLE-PHONON DUALITY**

The Bush-Oza hydrodynamic quantum analogs are central to interpreting the phonon-exflation framework as a classical system generating quantum-like phenomena:

1. **Particles as droplets in the geometric fluid**: In phonon-exflation, SM particles are phonons (excitations of the K_7 compactification). The Bush-Oza walking droplet analogy suggests that particles can be understood as droplet-like entities bouncing/moving through the substrate geometry, guided by a pilot-wave field (the Dirac spectrum, or equivalently, the spectral action). Just as a droplet creates ripples that guide its motion, a SM particle's trajectory is determined by the curvature and topology of the compactified geometry.

2. **Temporal nonlocality and spectral action feedback**: The temporal nonlocality in walking droplets (where the droplet's future depends on past wave field) is directly analogous to the spectral action's role in phonon-exflation. The spectral action $S_{\text{spec}}[\tau]$ integrates over all Dirac eigenvalues, including contributions from distant (in $\tau$ space) configurations. The geometry's evolution $d\tau/dt$ depends on this "memory" of the spectral action landscape—a temporal nonlocality that constrains the evolution.

3. **Quantization without quantum mechanics**: Walking droplets achieve energy quantization (discrete orbital radii) through a classical pilot-wave mechanism, without any quantum mechanics postulate. Similarly, the framework aims to show that SM particles (with quantized masses and quantum numbers) emerge classically from the K_7 geometry, without importing quantum mechanics axiomatically. Both rely on standing wave conditions in confined geometries.

4. **Diffraction and interference as geometric properties**: When a droplet diffracts through a slit, its trajectory curves due to the wave field. In phonon-exflation, particles diffract and interfere because they are waves (phonons) in the K_7 lattice. Their wavelength $\lambda = 2\pi / k$ depends on the dispersion relation $\omega(k)$ of the compactified geometry. The interference patterns that emerge are topological properties of the geometry—bulk-boundary correspondence (as in topological phononic metamaterials, paper 12).

5. **Realist interpretation and emergence**: The Bush-Oza framework is explicitly realist (droplet positions are definite, trajectories exist) and deterministic (no randomness, only apparent randomness from averaging over many trajectories). Phonon-exflation adopts this realist stance: SM particles are real excitations with definite properties (masses, spins, quantum numbers), determined by the compactification geometry. Quantum indeterminacy is not fundamental but emergent from coarse-graining over many equivalent geometries.

6. **Memory effects and path dependence**: Walking droplets' motion depends on their past wave field—a memory effect. In phonon-exflation, particle properties (masses, coupling constants) depend on the history of the compactification metric $\tau(t)$. The "memory" of the metric's past configurations encodes in the current spectral action landscape. This explains why particle masses appear fine-tuned: they are path-dependent relics of the geometric transit (Sessions 37-38).

7. **Hydrodynamic substrate for spacetime**: The Bush-Oza review suggests that quantum mechanics emerges from a hydrodynamic substrate. Phonon-exflation proposes that spacetime itself is such a substrate—the M4 x SU(3) geometry is a "phononic fluid" where particle excitations (phonons) behave wave-like due to the substrate's structure. General relativity (geometry ↔ gravity) then emerges as the long-wavelength effective description of the hydrodynamic substrate.

**Specific parallel**: The droplet wavelength $\lambda = v / f$ (horizontal speed divided by bounce frequency) is the de Broglie wavelength. In phonon-exflation, the K_7 "phonon velocity" is set by the Fermi surface curvature, and the "bounce frequency" is set by the BCS energy scale $\Delta$. The resulting effective wavelength $\lambda_{\text{K7}} = v_F / \Delta$ determines particle interaction cross-sections and scattering lengths, which in turn determine coupling constants and running of the gauge theory. This is a prediction the framework could test numerically (Session 39+).

