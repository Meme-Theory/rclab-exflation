# Background and Emerging Applications of Acoustic Metamaterials: A Forum on Classical Waves

**Editor(s):** Hong Chen (Tongji University) (Forum organizer)

**Contributors:** Che Ting Chan (Hong Kong University of Science and Technology), Yan-Feng Chen (Nanjing University), Zhengyou Liu (Wuhan University), Jie Zhu (Tongji University), and others

**Year:** 2024

**Identifier:** DOI: 10.1093/nsr/nwae366

**Published in:** National Science Review, Vol. 12, No. 8, pp. nwae366 (2025, online 2024)

---

## Abstract

Acoustic metamaterials—engineered composite materials designed to control, guide, and manipulate sound waves in novel ways—have emerged as a transformative field bridging condensed-matter physics, materials science, and engineering. This comprehensive forum, organized by Hong Chen and featuring leading experts from leading research institutions, provides an updated overview of the field's current state and future directions. The review encompasses:

1. **Classical-Wave Foundations:** The design principles underlying acoustic metamaterials, from simple resonators and mass-spring chains to complex phononic crystals and topology-protected acoustic metamaterials.

2. **Non-Hermitian Phenomena:** The exploration of parity-time (PT) symmetry, gain-loss engineering, and non-Hermitian dynamics in acoustic systems, enabling phenomena like unidirectional invisibility and exceptional-point engineering.

3. **Phonon-Electron Coupling:** The interaction between acoustic excitations (phonons) and electronic systems, opening pathways to hybrid quantum systems and phononic-electronic devices.

4. **Exotic Phenomena:** Perfect acoustic imaging, cloaking, topological edge states, and negative refraction.

5. **Applications:** From noise control in transportation and architecture to quantum information processing, the metamaterials platform offers solutions across scales.

The forum positions acoustic metamaterials not merely as a technology for sound manipulation but as a conceptual and developmental platform for condensed-matter physics, allowing researchers to realize and test exotic phases of matter (topological order, non-Hermitian phases, time-crystal-like structures) in a controlled, accessible laboratory setting.

---

## Historical Context

Acoustic and photonic metamaterials arose in the late 1990s and early 2000s, following the pioneering work of Pendry on electromagnetic cloaking and Smith et al. on negative-refractive-index materials. By 2010-2015, the field had matured into a rich discipline exploring topological phonons, non-Hermitian systems, and analogues of condensed-matter phenomena.

By 2024, additive manufacturing (3D printing) had democratized metamaterial fabrication, enabling rapid prototyping of complex structures previously impossible to manufacture. Simultaneously, the field had absorbed insights from quantum information, topological materials, and non-Hermitian physics. The NSR forum represents a maturity milestone: the field has moved from proof-of-concept demonstrations to systematic engineering and applications.

The forum is particularly timely given the convergence of:
- **PT-symmetric photonics and acoustics:** Exceptional-point engineering and mode coalescence.
- **Topological phononics:** Berry phase, Chern numbers, topological edge states in acoustic systems.
- **Phonon-electron coupling:** Hybrid quantum devices combining acoustic excitations with superconductivity, magnetism, and quantum information.
- **Quantum-inspired acoustics:** Phononic analogs of quantum phenomena (Berry curvature, topological bands, non-Hermitian skin effect).

---

## Key Topics and Derivations

### Acoustic Metamaterial Design Principles

An acoustic metamaterial is characterized by an **effective acoustic impedance** $Z_{\text{eff}}$ and **refractive index** $n_{\text{eff}}$, both often frequency-dependent and potentially negative:

$$Z_{\text{eff}}(\omega) = Z_0 + Z_{\text{resonator}}(\omega)$$

where $Z_0$ is the background (e.g., air or water) impedance, and $Z_{\text{resonator}}$ is contributed by embedded resonators.

The resonators are typically:
- **Helmholtz cavities:** Hollow chambers with a narrow neck, resonating at a frequency $\omega_0 = c \sqrt{A/V\ell}$, where $A$ is the neck area, $V$ is the cavity volume, $c$ is sound speed.
- **Membrane resonators:** Thin plates vibrating at $\omega_0 \propto \sqrt{T/(\rho a^2)}$, with tension $T$, density $\rho$, and area $a$.
- **Coiled waveguides:** Long, narrow channels bent into compact spirals, introducing phase delays and resonances.

The collective response of many resonators engineered at different frequencies enables frequency-selective impedance shaping:

$$n_{\text{eff}}(\omega) = 1 + \frac{\omega_p^2}{\omega(\omega + i\gamma)}$$

where $\omega_p$ is a plasma-like frequency controlled by the resonator parameters, and $\gamma$ is damping.

### Phononic Crystals and Band Gaps

A phononic crystal is a periodic arrangement of scatterers (e.g., cylindrical holes in a solid, or periodic stiffness variations). The periodic structure creates a **photonic band structure** (in optics) or **phononic band structure** (in acoustics).

For a 1D periodic structure with period $\Lambda$, the dispersion relation exhibits **band gaps** (frequency ranges with no propagating modes):

$$\omega(k) \text{ is non-real (decaying) in band-gap regions}$$

The edges of the band gap are determined by Bragg resonance:

$$\Lambda = \frac{n \lambda}{2} = \frac{n \pi c}{2\omega}$$

where $n = 1, 2, \ldots$ is the mode order.

For 2D and 3D phononic crystals, the band structure becomes multidimensional. The density of states (DOS) vanishes within the gap:

$$g(\omega) = 0 \quad \text{for} \quad \omega \in [\omega_{\text{gap}}, \omega_{\text{gap}}']$$

This enables perfect absorption and reflection if the metamaterial is thick enough.

### PT-Symmetric Acoustic Systems

Parity-time (PT) symmetry refers to combined symmetry under spatial inversion ($\mathbf{r} \to -\mathbf{r}$, "parity") and time reversal ($t \to -t$, "time"). A Hamiltonian (or equation of motion) respects PT symmetry if:

$$PT H = H (PT)$$

In acoustic systems, PT symmetry is realized by balancing **gain** and **loss** regions:

$$n_{\text{eff}}(x) = n_R(x) + i n_I(x)$$

where $n_I(x) > 0$ represents loss (absorption) and $n_I(x) < 0$ represents gain (active amplification).

For a 1D waveguide with periodic alternating gain and loss:

$$n(x) = n_0 [1 + \epsilon \Theta(x)]$$

where $\Theta(x)$ alternates between $+1$ (gain) and $-1$ (loss), and $\epsilon$ controls the magnitude. PT symmetry requires equal gain and loss over a spatial period.

**Exceptional Points (EPs):** At special parameter values, two eigenvalues and corresponding eigenmodes coalesce:

$$E_1(\epsilon_0) = E_2(\epsilon_0)$$

Near an exceptional point, the system exhibits **extreme sensitivity** to perturbations—a feature exploited for sensitive detection.

### Non-Hermitian Skin Effect

In a non-Hermitian system (with gain and loss), the eigenmodes are typically **not orthogonal**. This leads to surprising phenomena, including the **non-Hermitian skin effect**: a macroscopic number of eigenmodes localize near the boundary, even though the bulk is extended in a Hermitian system.

For a 1D non-Hermitian tight-binding model:

$$H = \sum_n t_n (|n\rangle\langle n+1| + |n+1\rangle\langle n|) + i\gamma_n |n\rangle\langle n|$$

with non-Hermitian terms $i\gamma_n$ representing loss, the spectrum can exhibit a "point gap" (the spectrum lies on a curve in the complex plane, enclosing an empty region).

The number of boundary-localized states scales with the system size $N$, not exponentially (as for Hermitian boundary states) but polynomially or even linearly.

### Phonon-Electron Coupling: Hybrid Systems

Acoustic metamaterials can be coupled to electronic systems, creating **hybrid phonon-electron devices**. A key platform is the **surface acoustic wave (SAW)** on a piezoelectric substrate, which generates electric fields and couples to electrons.

The coupling Hamiltonian is:

$$H_{\text{int}} = g \sum_k (b_k^\dagger c_k + c_k^\dagger b_k)$$

where $b_k$ is the acoustic phonon (phonon annihilation operator), $c_k$ is the electronic mode, and $g$ is the phonon-electron coupling strength.

In the strong-coupling limit ($g \gg \Delta E$, where $\Delta E$ is the frequency mismatch), the system enters the **polariton regime**: hybrid quasi-particles (phonon-excitons or acousto-electronic polaritons) emerge, with properties intermediate between phonons and electrons.

This enables:
- **Phonon lasing:** Amplification of acoustic modes via stimulated emission.
- **Phonon-mediated superconductivity:** Enhancement of pairing via acoustic mediation.
- **Acoustic quantum computing:** Using phonons as quantum information carriers.

### Topological Phononic Metamaterials

Inspired by topological insulators in electronics, researchers engineered acoustic metamaterials with topologically non-trivial band structures. The key is the **topological invariant**, often the **Chern number**:

$$C = \frac{1}{2\pi i} \oint_{\partial BZ} \mathbf{A}(k) \cdot d\mathbf{k}$$

where $\mathbf{A}(k)$ is the Berry connection in momentum space.

A non-zero Chern number $C \neq 0$ guarantees the existence of **topologically protected edge states**—modes localized at boundaries that cannot be removed by adiabatic deformation. These are analogous to the edge states in the quantum Hall effect.

For example, in a 2D acoustic metamaterial with time-reversal symmetry breaking (via magnetic coupling or nonlinear effects), a Chern number can be defined. The bulk exhibits a phononic band gap, while the boundary hosts chiral edge states with:
- **Unidirectional propagation:** Modes travel only in one direction along the boundary.
- **Robustness to disorder:** Topological protection ensures the edge states survive scattering.
- **Back-scattering immunity:** A boundary defect cannot scatter a mode backward; it must propagate forward.

---

## Key Results

1. **Acoustic Control Beyond Traditional Materials:** Metamaterials enable impedance values and frequency responses impossible in natural materials, permitting perfect absorption, negative refraction, and acoustic cloaking.

2. **PT-Symmetric Dynamics in Acoustics:** Balanced gain-loss systems exhibit exceptional-point phenomena, extreme sensitivity to perturbations, and unidirectional transmission—features exploitable for detection and filtering.

3. **Non-Hermitian Skin Effect:** Loss introduces a macroscopic accumulation of energy near boundaries, a phenomenon absent in Hermitian systems and potentially useful for trapping and dissipating unwanted acoustic energy.

4. **Topological Phononic Edge States:** Acoustic metamaterials can be engineered to support topologically protected boundary modes, immune to defects and disorder, enabling robust acoustic communication channels.

5. **Phonon-Electron Hybrid Devices:** Acoustic-electronic coupling enables new functionalities: phonon lasing, phonon-enhanced superconductivity, acoustic quantum information processing.

6. **Phononic Simulation of Condensed-Matter Phases:** Acoustic metamaterials provide a versatile platform for testing exotic phases (topological order, non-Hermitian dynamics, time-crystal-like structures) in a controllable, observable setting.

7. **Practical Applications:** Noise suppression in vehicles and buildings, ultrasound generation and detection, acoustic metamaterial lenses for imaging, and phononic-photonic integrated circuits.

---

## Impact and Legacy

The NSR forum consolidates the maturity of acoustic metamaterials as a discipline:

- **Interdisciplinary Bridge:** Connects condensed-matter physics, materials science, engineering, and quantum information.
- **Accessibility:** Acoustic systems are easier to fabricate, measure, and visualize than photonic or electronic systems, making them ideal for education and fundamental research.
- **Technological Trajectory:** Moving from proof-of-concept demonstrations to engineered devices and systems integration.
- **Conceptual Platform:** Metamaterials serve as a "condensed-matter physics laboratory," enabling realization and measurement of exotic phases under controlled conditions.

---

## Connection to Phonon-Exflation Framework

**The Framework's D_K as a Non-Hermitian Acoustic Operator:**

The phonon-exflation framework's Dirac operator $D_K$ (acting on the SU(3) fiber) exhibits non-Hermiticity in the inner-fluctuation sector. The inner fluctuations are not physical gauge freedom but rather acoustic-like excitations (phonons) whose dynamics are non-Hermitian due to coupling to an external environment (the expanding 4D geometry).

In this interpretation, the framework's spectral action and the pairing dynamics constitute a **non-Hermitian phononic system**, precisely the type studied in this acoustic-metamaterials review.

**PT-Symmetry and Balanced Gain-Loss:**

The framework predicts that the effective "gain-loss" structure of the phononic system is balanced: the instanton rate (providing "gain" or source of particle creation) is matched by the dissipation rate (Landau damping, interaction with the thermal bath). This balance, in the PT sense, could explain the system's robustness and the persistence of the integrable structure (Richardson-Gaudin symmetry).

**Phonon-Electron Coupling in the GGE Relic:**

The post-transit GGE relic contains locked-in Richardson-Gaudin conserved charges—analogous to topological invariants in condensed-matter systems. The coupling between these "phononic" modes (the RG integrals) and the "fermionic" degrees of freedom (the Cooper pairs) is the phonon-electron interaction in acoustic-metamaterials language.

**Topological Edge States Analogy:**

The framework's prediction of mass hierarchy and the precise values of the Standard Model parameters (e.g., $\sin^2\theta_W = 3/8$) can be reinterpreted as **topological invariants** protected by the SU(3) symmetry. The "edge" of the framework is the 4D spacetime boundary, and the "edge states" are the observed particles and forces—protected not by random defects but by the fundamental topology of the internal fiber.

**Non-Hermitian Skin Effect and Condensate Localization:**

In acoustic metamaterials, the skin effect concentrates energy near boundaries. In the framework, the BCS condensate density is concentrated in regions of high pairing interaction (the K7-neutral sector). This could be reinterpreted as a phononic skin effect: the pairing "skin" in the non-Hermitian coupled dynamics.

---

## References and Further Reading

- Chen, H., Chan, C. T., Chen, Y.-F., Liu, Z., & Zhu, J. (2024). "Background and emerging applications of acoustic metamaterials: A forum on classical waves." *National Science Review*, 12(8), nwae366.
- Hussein, M. I., Maldovan, M., Branch, R., & Barajas-Solano, D. A. (2014). "Phononic crystals and metamaterials: Multiphysics and multiscale modeling." *Mechanical Engineering Magazine*, 136(09), 30–37.
- Christensen, J., Cummer, S. A., Koh, S., & Maldovan, M. (2016). "Designing phononic band-gap crystals and metamaterials." *Nature Reviews Materials*, 1(11), 16001.
- Maldovan, M. (2013). "Sound and heat revolutions in phononics." *Nature*, 503(7475), 209–217.
- Hussein, M. I., Frazier, M. J., El-Kady, I., & Ruzzene, M. (2018). "Recent advances in engineered structures and materials for enhanced vibration isolation." *Advances in Applied Mechanics*, 51, 361–412.
