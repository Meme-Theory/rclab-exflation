# The 2024 Phononic Crystals Roadmap

**Authors:** Yong Jin, Robert Shen, Osamu Sakai, Ying Wu, Bahram Djafari-Rouhani, Evgeny Tsitsas, and 35+ international contributors
**Year:** 2024
**Journal:** Journal of Physics D: Applied Physics, Vol. 58, No. 11, Art. 113001

---

## Abstract

This comprehensive roadmap synthesizes three decades of phononic crystal research, integrating contributions from physics, materials science, engineering, and applied mathematics. Phononic crystals are periodic structures engineered to manipulate acoustic and elastic wave propagation via Bragg scattering and local resonance mechanisms, enabling complete bandgaps where wave transmission is prohibited. The 2024 roadmap covers: (1) Fundamental properties—bandgap engineering, dispersion curves, transmission spectra; (2) Homogenization theory and effective medium descriptions; (3) Machine learning-assisted design and inverse design; (4) Topological phononic crystals with quantum Hall and valley Hall effects; (5) Non-Hermitian and nonreciprocal systems; (6) Nanoscale to macroscale implementations; (7) Chiral, nonlocal, active, and spatiotemporal metamaterials; (8) Applications in vibration control, noise reduction, thermal management, sensing, structural health monitoring, seismic protection, and underwater acoustics. The roadmap identifies key challenges: manufacturing precision at nanoscale, integration with electronics, reliability for commercialization, and computational design of tunable devices. It synthesizes current knowledge and charts future research directions across multiple scales and disciplines.

---

## Historical Context

Phononic crystals emerged in the 1990s as the acoustic/elastic analog of photonic crystals (pioneered by Yablonovitch 1987, John 1987). The first major results were:

1. **Complete bandgaps by Bragg scattering** (Sigalas & Economou 1993, Kushwaha et al. 1994): Periodic structures of high-impedance inclusions in a low-impedance host medium scatter acoustic waves destructively, creating frequency ranges where all waves are evanescent.

2. **Local resonance mechanism** (Liu et al. 2000): Periodic placement of local oscillators (masses on springs, resonant cavities) produces bandgaps at frequencies determined by the resonance, not just Bragg wavelength matching. This enabled bandgaps much smaller than the wavelength (deeply subwavelength).

3. **Early applications** (2000s): Vibration isolation, noise control, and acoustic waveguides were demonstrated.

By 2010s, the field rapidly expanded to include:

- **Topological phononic systems** (2015+): applying topological insulator concepts to phononic bands
- **Non-Hermitian phononics**: gain/loss in active metamaterials
- **Machine learning design**: using neural networks and genetic algorithms to optimize phononic structures
- **Nanoscale phononics**: GHz-frequency phononic crystals for quantum devices

By 2024, phononic crystals have matured into a central platform for applied physics, with interdisciplinary applications and theoretical depth rivaling photonics. This roadmap consolidates 30 years of knowledge and identifies next-generation challenges.

---

## Key Arguments and Derivations

### Bandgap Mechanism: Bragg Scattering

Phononic crystals with periodic structure exhibit bandgaps via the Bragg scattering mechanism. For a 1D crystal with lattice constant $a$, elastic waves satisfy:

$$\omega(k) = c_s |k|$$

for free propagation (linear dispersion, $c_s$ is sound speed). With periodicity, Bragg diffraction occurs when the wavelength matches:

$$\lambda = 2a / n, \quad k = n\pi/a$$

where $n = 1, 2, 3, \ldots$ indexes the Bragg orders. At these wavevectors, waves scattered from successive planes interfere constructively, creating a reflective barrier.

The band structure near the Brillouin zone boundary ($k = \pi/a$) exhibits avoided crossings: bands repel each other, creating gaps. The bandwidth $\Delta \omega$ of the gap depends on the scattering contrast (acoustic impedance mismatch between materials):

$$\Delta \omega \approx \omega_c \Delta Z / Z$$

where $Z = \rho c$ is the acoustic impedance, $\Delta Z$ is the impedance difference, and $\omega_c$ is the center frequency.

### Local Resonance Mechanism

A more efficient bandgap mechanism uses **local resonators**—subwavelength structures with internal oscillation modes. The simplest example is a mass $m$ attached to a spring ($k_s$) at each lattice site:

$$\omega_{\text{res}} = \sqrt{k_s / m}$$

In the dispersion relation, this introduces a new frequency scale independent of Bragg scattering. At $\omega \approx \omega_{\text{res}}$, the masses resonantly oscillate, storing energy locally rather than propagating it. This creates a bandgap with width:

$$\Delta \omega_{\text{res}} \propto \sqrt{k_s / m}$$

The gap can be tuned by varying $m$ or $k_s$ independently of the lattice constant $a$. This allows subwavelength gaps—gaps much smaller than the operating wavelength—crucial for practical applications.

### Effective Medium Theory

At frequencies well below the Bragg scattering threshold or far from resonances, a phononic crystal can be homogenized into an effective medium with renormalized density $\rho_{\text{eff}}$ and bulk/shear moduli. The effective density can be **negative** near a local resonance:

$$\rho_{\text{eff}}(\omega) = \rho_0 + \frac{\rho_r \omega_r^2}{\omega_r^2 - \omega^2 - i\Gamma\omega}$$

where $\rho_r$ is the resonator mass, $\omega_r$ is the resonance frequency, and $\Gamma$ is damping. For $\omega < \omega_r$, the second term is negative (at low frequencies and loss), making $\rho_{\text{eff}} < 0$.

Similarly, the bulk modulus can become negative. When both $\rho_{\text{eff}} < 0$ and $K_{\text{eff}} < 0$, the sound speed $c = \sqrt{K_{\text{eff}} / \rho_{\text{eff}}}$ becomes negative (phase velocity and group velocity have opposite signs), an exotic wave phenomenon enabling cloaking and negative refraction.

### Topological Phononic Crystals

Topological phononic crystals exhibit band topology characterized by topological invariants (Chern numbers, winding numbers) that protect edge states. A 2D phononic topological insulator has:

$$C = \frac{1}{2\pi} \int_{\text{BZ}} d^2k \, F(\mathbf{k})$$

where $F(\mathbf{k})$ is the Berry curvature. If $C \neq 0$, the boundary hosts edge states with frequencies in the bulk gap, robust against disorder.

The roadmap reviews how topological protection applies to:

- **Quantum Hall-like phononic insulators**: breaking time-reversal symmetry (e.g., with gyroscopic elements)
- **Valley Hall phononic insulators**: breaking inversion symmetry, protecting valley-selective modes
- **Higher-order topological phononic insulators**: corner and hinge states

### Machine Learning for Design

Modern phononic crystal design leverages **inverse design** and machine learning:

1. **Generative models** (neural networks, diffusion models): given desired frequency response (e.g., a specific bandgap width and location), generate a phononic crystal topology.

2. **Topological optimization** (grad-based): start with a material domain, iteratively refine the structure using gradients of an objective function (minimize loss in target band, maximize attenuation in stopband).

3. **Surrogate models** (reduced-order): train a fast neural network on expensive finite-element simulations, enabling rapid evaluation of design variants.

These methods reduce design time from months (hand-tuning parameters) to days or hours, enabling exploration of vast design spaces.

---

## Key Results

1. **Complete bandgaps demonstrated**: In 1D and 2D phononic crystals, complete bandgaps (where all waves are evanescent) are routinely achieved. Examples include:
   - 1D multilayers: bandgaps spanning 10-100% fractional width
   - 2D triangular/honeycomb lattices: complete bandgaps up to 50% fractional width
   - 3D photonic-like structures: complete bandgaps in all directions

2. **Subwavelength bandgaps via local resonance**: Bandgaps at frequencies where the wavelength is 10-100× larger than the unit cell, enabling compact structures. Example: MHz-scale vibration isolation using millimeter-scale resonators.

3. **Topological edge states experimentally confirmed**: Multiple groups have demonstrated unidirectional, disorder-robust edge state propagation in 2D phononic topological insulators, with edge state attenuation << bulk band attenuation.

4. **Negative refraction and focusing**: Phononic metamaterials with negative refractive index focus acoustic waves using flat (negative-curvature) lenses, defying Snell's law. Focusing to subwavelength scales has been observed.

5. **Active and non-Hermitian control**: Phononic crystals with gain (active speaker elements, parametric drive) or loss exhibit non-Hermitian topological effects (skin effect, exceptional points), enabling new control mechanisms for acoustic waves.

6. **Acoustic tweezers and manipulation**: Phononic metamaterials designed with topological or resonant features can stably trap and manipulate particles (cells, colloids) in acoustic potential wells, with applications to biomedical separation.

7. **Thermal transport control**: Phononic bandgaps suppress phonon propagation in the thermal bandwidth, reducing thermal conductivity by factors of 10-100 without reducing electrical conductivity—enabling thermoelectric applications.

8. **GHz-scale phononic crystals**: Nanoscale phononic structures with periods 10-100 nm produce phononic bandgaps at GHz frequencies, bridging quantum phononic effects (relevant to quantum computing) and classical metamaterials.

9. **Seismic metamaterials**: Large-scale implementations with periods 10-100 meters or engineered seismic metamaterial barriers have been proposed to protect buildings and infrastructure from seismic waves. Laboratory prototypes show attenuation in the Hz-kHz range.

10. **Machine learning design optimization**: Neural network-based inverse design has rapidly generated novel phononic structures with tailored frequency responses, reducing design iteration time by 10-100×.

---

## Impact and Legacy

The 2024 roadmap confirms that phononic crystals have transformed from a niche academic topic to a mature, multidisciplinary field with broad applicability:

1. **Engineering and industry**: Commercial interest in vibration isolation, noise control, thermal management, and acoustic devices has grown. Companies are integrating phononic concepts into consumer and industrial products.

2. **Fundamental physics**: Phononic crystals serve as classical platforms for studying topological, non-Hermitian, and nonlinear wave physics without quantum complications, clarifying fundamental concepts.

3. **Quantum information and metrology**: GHz-scale phononic crystals are now integrated with superconducting qubits (Chu et al. 2017, paper 11) and optomechanical systems, becoming essential to quantum transduction and quantum computing.

4. **Interdisciplinary cross-pollination**: Concepts and methods from condensed matter physics (topology, Bloch bands), quantum optics (squeezing, entanglement), and machine learning (neural networks, inverse design) all now inform phononic crystal research.

5. **Sustainability and energy**: Phononic metamaterials for thermoelectric enhancement and energy harvesting could improve efficiency of thermal-to-electric conversion, relevant to decarbonization.

---

## Connection to Phonon-Exflation Framework

**Relevance: METAMATERIAL BLUEPRINT FOR SPACETIME COMPACTIFICATION**

The phononic crystals roadmap provides deep structural insights for the phonon-exflation framework's geometry and dynamics:

1. **Periodic compactification as phononic crystal**: The M4 x SU(3) spacetime can be understood as a "phononic crystal" on a higher-dimensional background. The periodicity of the SU(3) lattice (with lattice constant set by the compactification radius) produces Bragg-like scattering of particle waves (phonons). The SM particle spectrum (masses, couplings) emerges as the "phononic bandgap structure" of this compactified geometry.

2. **Bandgap engineering through metric deformation**: As the compactification metric $\tau$ evolves (Sessions 35-38), the effective "impedance" of the K_7 channel changes, modifying the "bandgap structure" of the spectral triple. Topological properties of the Dirac spectrum shift, allowing particle states to emerge or disappear. This is directly analogous to tuning the phononic bandgap by varying the lattice constant or material contrast.

3. **Local resonance as BCS gap formation**: The local resonance mechanism (mass on spring) that creates subwavelength bandgaps is structurally identical to BCS pairing: a localized interaction (pairing on K_7) creates a macroscopic energy gap in the spectrum. The gap width is independent of the "wavelength" (fine structure of the geometry) and depends only on the pairing strength. Sessions 35-38 showed that the BCS gap $\Delta(\tau) = 0.115$ is such a resonance-generated feature.

4. **Effective medium and renormalized couplings**: The homogenization theory that derives $\rho_{\text{eff}}$ and $K_{\text{eff}}$ from a complex periodic structure is analogous to the renormalization group (RG) flow in the framework. Both compress microscopic complexity into effective macroscopic parameters. The spectral action itself can be viewed as the "effective action" of the phononic crystal, homogenized to 4D spacetime.

5. **Topological edge states as SM particles**: The robust, disorder-proof edge states in topological phononic crystals are analogous to SM particles in phonon-exflation. Both are localized to boundaries (the K_7 Fermi surface edge in the framework, the physical boundary in phononic crystals) and protected topologically. Both cannot backscatter into the bulk (no coupling to bulk states with different quantum numbers).

6. **Non-Hermitian dynamics during transit**: The Sessions 37-38 instanton physics involves loss (decay of the condensate during geometric transit). Non-Hermitian topological phononics (with gain/loss) provides a theoretical framework for understanding how topological protection persists during dissipation. The "skin effect" in non-Hermitian systems (bulk states accumulating at boundary) describes how phonon excitations concentrate at the transition region during BCS formation.

7. **Machine learning design and framework discovery**: Just as inverse design in phononic crystals rapidly generates structures with desired frequency response, machine learning could be used to explore the vast space of possible compactification metrics $\tau(t)$ and find those that yield physical SM properties and stable cosmological evolution. This is an untapped application area: ML-guided exploration of the $\tau$ landscape.

8. **Spatiotemporal modulation and cosmological evolution**: The roadmap's discussion of spatiotemporal phononic metamaterials (structures with time-dependent modulation) is directly relevant to phonon-exflation, where the compactification metric $\tau(t)$ is time-dependent. Phononic crystal physics with temporal modulation (Floquet systems) provides a natural language for describing cosmological evolution as a "driven" phononic system.

**Specific connection**: The local resonance formula $\omega_{\text{res}} = \sqrt{k_s / m}$ is dimensionally identical to the BCS gap $\Delta = v_F \sqrt{(m^* - m_0) / m_0}$ derived in Sessions 35-38. Both represent emergent energy scales arising from the interplay of a stiffness (spring constant $k_s$; Fermi velocity $v_F$) and an inertia (mass $m$; effective mass difference). This dimensional analogy suggests that the K_7 compactification geometry has an effective "spring constant" and "resonant mass" that determine the BCS gap magnitude—potentially a new avenue for computing the gap from first-principles geometry (currently a free parameter fit to Standard Model masses).

