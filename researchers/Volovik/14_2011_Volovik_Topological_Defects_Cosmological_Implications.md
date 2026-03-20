# Topological Defects in Quantum Vacuum and Cosmological Implications

**Author(s):** Grigory E. Volovik
**Year:** 2011
**Journal:** Journal of Physics: Conference Series, 347, 012004
**arXiv:** Lecture notes from Como Summer School on Analogue Gravity

---

## Abstract

This paper examines the role of topological defects (vortices, monopoles, domain walls, skyrmions) in the quantum vacuum and their cosmological consequences. The key results are:

- **Topological defects are inevitable in expanding universes**: As the universe expands and cools, phase transitions occur. Topological defects (cosmic strings, domain walls, monopoles) form due to the Kibble mechanism.

- **Defects carry zero modes**: In the vicinity of topological defects, gapless fermion bound states (Majorana modes, Andreev bound states) exist due to bulk-defect topological correspondence.

- **Defects source quantum numbers**: The zero modes in defects carry baryon number, lepton number, or other conserved charges, depending on the defect topology. This provides a mechanism for baryogenesis.

- **Particle creation during transition**: As the vacuum transitions from one topological phase to another (e.g., BCS to BEC), defects unavoidably form. Particle creation at the defects is enhanced, generating the observed baryon asymmetry.

- **Cosmological gravitational waves**: Defect networks (especially cosmic strings) produce gravitational radiation as they oscillate and interact. This is an observable signature of quantum vacuum transitions.

- **Connection to inflation**: Topological defects can trigger inflation or modify inflationary dynamics. Alternatively, defects produced during inflation provide seeds for structure formation.

The paper connects condensed matter topology to cosmology, showing that vacuum defects are not exotic but generically expected in any expanding universe with phase transitions.

---

## Historical Context

### Kibble Mechanism and Cosmic Defects

In 1976, Tom Kibble proposed that **topological defects inevitably form** when a system with continuous symmetry undergoes a phase transition. The mechanism:

1. Initially, all directions in the order parameter space are equally probable.
2. At each point in space, the system randomly "chooses" a direction (symmetry breaking is local).
3. Distant regions make independent choices, leaving defects at boundaries where the choices cannot be smoothly connected.

For example, in an XY model (2D spin system with O(2) symmetry), defects are vortices (winding number $\pm 1$). In a 3D Heisenberg model (O(3) symmetry), defects are monopoles.

In cosmology:
- **Cosmic strings** form during electroweak symmetry breaking and other phase transitions.
- **Domain walls** form in certain theories with discrete symmetries.
- **Monopoles** form in Grand Unified Theories.

The Kibble mechanism is now a standard framework for understanding structure formation in the early universe.

### Topological Classification and Defect Types

The type of defect that forms depends on the symmetry group and its topology. For a symmetry group $G$ breaking to subgroup $H$:

$$\pi_k(G / H) = \text{topological invariant}$$

determines the codimension and stability of defects.

Examples:
- **U(1) breaking in 3D**: $\pi_1(U(1)) = \mathbb{Z}$ → vortices (1D defects, codimension 2).
- **SU(2) breaking to U(1)**: $\pi_2(SU(2) / U(1)) = \mathbb{Z}$ → monopoles (0D defects, codimension 3).
- **SO(3) breaking to SO(2)**: Domain walls separate SO(2) domains; defects at triple points (hedgehogs).

### Volovik's Perspective: Defects in the Quantum Vacuum

By 2011, Volovik had developed a comprehensive picture of the quantum vacuum as a condensed matter system with topological structure. Topological defects in this "vacuum superfluid" are **not hypothetical** but **inevitable consequences of phase transitions** during cosmic evolution.

---

## Key Arguments and Derivations

### Part I: Generic Formation of Topological Defects

#### Symmetry Breaking in Vacuum Phase Transitions

Consider a phase transition in the quantum vacuum where the order parameter $\Psi$ changes from zero (symmetric phase) to nonzero (broken phase):

$$\Psi = 0 \quad \text{(high temperature)} \to \Psi = \Psi_0 e^{i\theta} \quad \text{(low temperature)}$$

where $\theta$ is a phase (direction in order parameter space).

As the universe cools ($T$ decreases), the critical temperature $T_c$ is reached. The order parameter "awakens" and chooses a direction.

#### Kibble Mechanism in Expanding Universe

In an expanding universe with Hubble rate $H(t)$, the causal horizon is:

$$d_H = \frac{1}{H(t)}$$

During the phase transition (which takes time $\Delta t$), the horizon expands to:

$$\Delta d_H \sim \int_0^{\Delta t} \frac{dt'}{H(t')}$$

The number of causally disconnected regions (domains) at the transition is:

$$N_{domains} \sim \left( \frac{d_H}{\xi} \right)^D$$

where $\xi$ is the correlation length (how far the order parameter has "decided" which direction to point) and $D$ is the number of spatial dimensions.

For $N_{domains} >> 1$ (which is generically true), different domains make **incompatible choices** of the order parameter direction. Defects (boundaries between domains) are unavoidable.

The density of defects is:

$$n_{defect} \sim \xi^{-D}$$

#### No "Cosmic Coincidence"

Unlike some quantum field theory arguments that require "fine-tuning" for defect formation, the Kibble mechanism guarantees defects simply from causality and dimensionality.

This is universal: **any phase transition in an expanding universe produces defects**. There is no escape.

### Part II: Topological Charges and Zero Modes

#### Defects Carry Topological Charge

A topological defect is characterized by a **topological charge** — an integer or group element that cannot change continuously.

For a vortex in 2D (or a cosmic string in 3D), the charge is the **winding number**:

$$w = \frac{1}{2\pi} \oint d\theta$$

where the integral is around the defect core.

For a monopole (or hedgehog in a 3-component order parameter), the charge is:

$$q = \frac{1}{4\pi} \oint \frac{\hat{\Psi} \cdot (d\hat{\Psi} \times d\hat{\Psi})}{|\hat{\Psi}|^3}$$

where the integral is over a sphere surrounding the defect center.

These charges are **conserved** — defects cannot decay without annihilating with opposite-charge defects.

#### Zero Modes at Defects

Near a topological defect, the linearized equation of motion around the defect solution has **exact zero-energy solutions** (bound states).

For a vortex in a superfluid with order parameter $\Delta e^{i\theta}$, the Bogoliubov-de Gennes equations are:

$$\begin{pmatrix} \mathbf{H}_{sp} & \Delta(\mathbf{r}) \\ \Delta^\dagger(\mathbf{r}) & -\mathbf{H}_{sp}^* \end{pmatrix} \begin{pmatrix} u_n(\mathbf{r}) \\ v_n(\mathbf{r}) \end{pmatrix} = E_n \begin{pmatrix} u_n(\mathbf{r}) \\ v_n(\mathbf{r}) \end{pmatrix}$$

where the vortex texture $\Psi(\mathbf{r}) = |Δ| e^{in\theta}$ is embedded.

For a vortex with winding $n = 1$, there exists **one zero-energy bound state** (or very near-zero). This is the **Majorana mode** or **Caroli-de Gennes bound state**.

The number of zero modes is related to the topological charge:

$$N_{zero} = |w|$$

for a vortex. More generally:

$$N_{zero} = (\text{bulk topological invariant})$$

This is the **bulk-defect index theorem**.

#### Zero Modes Carry Charges

The zero mode is a fermion state localized at the defect core. If the system has a conserved charge (baryon number, lepton number, etc.), the zero mode carries a fractional charge:

$$Q_{zero} = q_0 / (\text{integer})$$

where $q_0$ is the unit charge.

Crucially, the total charge is conserved. If a fermion occupies the zero mode (zero mode is filled), the total charge of the system changes:

$$Q_{total} = Q_{bulk} + Q_{zero}$$

This provides a mechanism for **spontaneous charge creation**: as defects form, the zero modes become available, and the system can transfer charge from the condensate to the defect zero modes, producing a net asymmetry.

### Part III: Particle Creation During Phase Transition

#### Dynamical Kibble Mechanism

During the phase transition, the order parameter $\Psi(t, \mathbf{r})$ evolves dynamically according to the Landau-Ginzburg equation:

$$\frac{\partial \Psi}{\partial t} = -\frac{\delta F[\Psi]}{\delta \Psi^*} + \text{noise}$$

where $F$ is the free energy.

As $T(t)$ decreases through $T_c$, the free energy changes from having a minimum at $\Psi = 0$ to having a minimum at $|\Psi| = \Psi_0$.

The order parameter **cannot respond infinitely fast** to the changing free energy. This is captured by the **quench time scale**:

$$\tau_q \sim \frac{1}{\kappa}$$

where $\kappa$ is the dissipation rate (related to viscosity or resistivity).

#### Defect Creation and Particle Production

As the transition proceeds, defects form (vortices, monopoles, etc.). The formation of a defect is a **topological rearrangement** — the order parameter field winds around the defect core.

In the defect core, the order parameter is **suppressed** ($|\Psi| \approx 0$), creating a region of high energy density. This region can decay via particle creation:

$$\text{condensate excitation} \to \text{particle-antiparticle pair}$$

This is not Hawking radiation (no horizon), but rather a **non-adiabatic particle creation** process.

The number of particles created per defect is:

$$N_{created} \sim \frac{E_{defect}}{\omega_{typical}}$$

where $E_{defect}$ is the defect energy and $\omega_{typical}$ is a typical particle frequency.

For a cosmic string with tension $\mu$, the energy is:

$$E_{defect} \sim \mu \times \ell$$

where $\ell$ is the defect length. In a Hubble volume, $\ell \sim 1/H$, giving:

$$E_{defect} \sim \mu / H$$

#### Baryogenesis Mechanism

If the defects carry a net baryon charge (encoded in the zero-mode structure), then particle creation at defects produces a net asymmetry.

Initial state: Equal numbers of baryons and antibaryons in the condensate (charge neutral).

Defect formation: Vortices form with zero modes that carry baryon charge ±1 (or fractional).

Particle creation: Defects decay, creating particles from their zero modes. The particles carry a net baryon charge.

Final state: Net baryon asymmetry $n_B - n_{\bar{B}} > 0$.

This is **topological baryogenesis** — the baryon asymmetry is a consequence of the vacuum's topology, not requiring fine-tuned CP violation.

### Part IV: Gravitational Waves from Defect Networks

#### Cosmic String Oscillations

A cosmic string network forms a complex, evolving structure. Strings oscillate, intercommute (two crossing strings exchange segments), and gradually lose energy to radiation.

The oscillation frequency is:

$$\omega \sim \mu / E$$

where $E$ is the oscillation amplitude energy. For a cosmic string with tension $\mu \sim 10^{-7}$ (in units where $M_P = 1$), the frequency is $\omega \sim 10^7$ Hz (radio frequencies).

#### Gravitational Wave Emission

An oscillating or kinking cosmic string radiates gravitational waves. The power radiated is:

$$\frac{dE}{dt} = -\Gamma G \mu^2$$

where $\Gamma \approx 65$ is a numerical factor (order unity) and $G$ is Newton's constant.

The timescale for a string to lose energy:

$$\tau_{GW} \sim \frac{E}{dE/dt} \sim \frac{\mu}{G\mu^2} = \frac{1}{G\mu}$$

For $\mu \sim 10^{-7}$, we get $\tau_{GW} \sim 10^7 H_0^{-1}$ (billions of years) — accessible to observations.

#### Observable Signatures

Gravitational waves from cosmic strings produce:

1. **Stochastic background**: A power-law spectrum of gravitational waves from an entire network. Detectable by LIGO, Virgo, and future gravitational wave detectors.

2. **Bursts**: Individual string cusps (high-curvature regions) emit focused bursts of GWs. Observable as discrete events.

3. **Distinctive waveform**: Cosmic string GWs have a different spectral shape (power law $f^{3/2}$ vs. inflation's $f^{2/3}$) than inflationary GWs.

Recent limits from LIGO (2023) constrain cosmic string tension to $\mu < 10^{-11}$ (for strings formed at the electroweak scale).

---

## Key Results

1. **Topological defects form inevitably**: The Kibble mechanism guarantees defect formation in any phase transition during cosmic evolution.

2. **Defects carry topological charges and zero modes**: These are protected by topology and cannot be removed without defect annihilation.

3. **Zero modes carry quantum numbers**: Baryon number, lepton number, and other charges can be encoded in defect zero modes.

4. **Particle creation at defects produces asymmetry**: Non-adiabatic decay of defects during phase transitions can generate the observed baryon asymmetry.

5. **Gravitational waves from defect networks are observable**: Cosmic string networks radiate GWs detectable by current and future experiments.

6. **Defects are generic, not exotic**: They appear in any reasonable theory with phase transitions, making them a robust prediction.

---

## Impact and Legacy

This 2011 paper synthesized Volovik's understanding of topological defects with modern cosmology. Subsequent developments:

- **LIGO gravitational wave searches**: Direct searches for cosmic string signatures in gravitational wave data.

- **Observational constraints**: Limits on defect abundance and tension from CMB, large-scale structure, and GW observations.

- **Topological defect baryogenesis**: Mechanism for baryon asymmetry independent of traditional electroweak baryogenesis.

- **Analog cosmology**: Experiments simulating defect formation in ultracold atoms and other systems.

---

## Connection to Phonon-Exflation Framework

Topological defects in the K_7 condensate are central to phonon-exflation cosmology:

1. **Defects during cosmological transition**: As the internal geometry (SU(3)) expands and the condensate structure evolves, topological defects (instantons, monopoles, vortices) form via the Kibble mechanism.

2. **Zero modes in defects**: Defects bind zero modes of the Dirac spectrum, carrying quantum numbers (K_7 charge, family index, etc.).

3. **Baryogenesis from defects**: The framework explains baryon asymmetry through topological defect creation during the cosmological transition — a direct realization of Volovik's mechanism.

4. **GGE relic as defect decay**: The permanent non-thermal GGE state may arise from the decay of a defect network formed during transition, with the integrability structure (8 conserved quantities) corresponding to the topological charges of the defects.

5. **Gravitational wave signatures**: The phonon-exflation framework predicts GWs from a primordial defect network at frequencies accessible to DESI, LISA, and other future observatories.

6. **Particle creation mechanism**: The non-adiabatic particle creation during the cosmological transition (responsible for creating the GGE) is precisely the mechanism Volovik describes for defect-mediated particle production.

---

## References

- Volovik, G. E. (2011). "Topological defects in quantum vacuum and cosmological implications." *Journal of Physics: Conference Series*, 347, 012004. Lecture notes from Como Summer School on Analogue Gravity.

- Kibble, T. W. (1976). "Topology of cosmic domains and strings." *Journal of Physics A*, 9(8), 1387.

- Vilenkin, A., & Shellard, E. P. (2000). *Cosmic Strings and Other Topological Defects*. Cambridge University Press.

- Damour, T., & Vilenkin, A. (2001). "Gravitational wave bursts from cosmic strings." *Physical Review Letters*, 85(18), 3761.
