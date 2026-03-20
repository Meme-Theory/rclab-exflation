# Superfluid Analogies of Cosmological Phenomena

**Author(s):** Grigory E. Volovik
**Year:** 2001
**Journal:** Physics Reports, 351, 195-246
**DOI:** 10.1016/S0370-1573(00)00139-3
**arXiv:** gr-qc/0005091

---

## Abstract

This review demonstrates that superfluid 3He-A exhibits fundamental physics concepts — chirality, Weyl fermions, gauge fields, and gravity — emerging together with their associated symmetries, including Lorentz symmetry and local SU(N) gauge invariance. The work proposes that quantum field theory functions as an effective low-energy theory describing quasiparticles (excitations) in the quantum vacuum, analogous to how elementary excitations in a superfluid emerge from the condensed matter substrate.

The paper examines how key cosmological phenomena can be understood through the superfluid analogy:

- **Inflation**: Vacuum phase transitions and latent heat release
- **Cosmological constant**: Equilibrium vacuum energy and its apparent smallness
- **Topological defects**: Domain walls, strings, monopoles as textural features
- **Axial anomaly**: Charge generation via fermion pair creation
- **Baryon asymmetry**: Chiral anomalies and parity violation
- **Event horizons and Hawking radiation**: Effective metrics and thermodynamics

The superfluid paradigm offers a resolution to multiple cosmological puzzles by replacing exotic assumptions (inflation, dark energy, GUT monopoles) with physics directly observable in laboratory superfluids.

---

## Historical Context

By 2001, the experimental observation of Bose-Einstein condensation in dilute alkali gases (1995, Cornell & Wieman) had revived interest in superfluid physics. Simultaneously, cosmology faced escalating tensions:

1. **Inflation problem**: Guth's 1981 inflationary hypothesis had solved horizon and flatness problems, but the inflationary potential was ad hoc and unobserved.

2. **Monopole problem**: Grand unified theories naturally predict massive monopoles. Yet no monopoles were observed. Inflation was proposed as a solution (dilute them away), but this felt unsatisfying.

3. **Cosmological constant problem**: Particle physics predictions for vacuum energy (Casimir effect, zero-point fluctuations) exceeded observations by 120 orders of magnitude.

4. **Baryon asymmetry**: CP-violating processes in the early universe were required to explain matter-antimatter asymmetry, but the magnitude was insufficient in minimal scenarios.

5. **Vacuum structure**: The inflaton field (responsible for inflation) was purely theoretical; no connection to known physics was apparent.

Volovik's 2001 review reframed these problems: *they are not cosmological mysteries but features of effective field theory*. The superfluid analogy shows that:

- Phase transitions (directly observable in labs) drive expansion
- Topological defects are unavoidable consequences of symmetry breaking
- Vacuum energy is a relative quantity (equilibrium value is zero)
- Chiral anomalies are exact mathematical features, not approximate symmetries

This was revolutionary because it grounded cosmology in **observable condensed matter physics** rather than speculative high-energy theories.

---

## Key Arguments and Derivations

### Part I: Superfluid 3He-A as a Toy Universe

#### Order Parameter and Ground State

Superfluid 3He-A at low temperature undergoes a phase transition to a paired state. Two fermions form a Cooper pair in a spin-triplet, p-wave state:

$$\psi_{3He} = \Delta(\mathbf{k}) \mathbf{d} \cdot (\boldsymbol{\sigma} \times \mathbf{\hat{k}})$$

where $\Delta(\mathbf{k})$ is the gap function, $\mathbf{d}$ is the gap direction (order parameter), and $\boldsymbol{\sigma}$ are Pauli matrices.

The order parameter $\mathbf{d}(\mathbf{r})$ varies spatially. Smooth variations (textures) create effective gauge fields. Singular variations (vortices, hedgehogs) create topological defects.

#### Hamiltonian for Quasiparticles

The effective Hamiltonian for low-energy fermionic excitations is:

$$H = \sum_{\mathbf{k}, \alpha} \epsilon(\mathbf{k}, \alpha) c^\dagger_{\mathbf{k}, \alpha} c_{\mathbf{k}, \alpha}$$

where the dispersion relation, near the Fermi surface, is:

$$\epsilon(\mathbf{k}, \alpha) = \sqrt{\Delta^2(\mathbf{k}) + v_F^2 |\mathbf{k}|^2}$$

At low energies ($\epsilon << p_F c_s$, where $c_s$ is sound speed), the spectrum is **linear**:

$$\epsilon(\mathbf{k}) \approx v_F |\mathbf{k}| = p_F |\mathbf{k}|$$

This is the spectrum of a **relativistic particle** — identical to a Weyl fermion in high-energy physics.

The Lorentz symmetry is emergent: it emerges from the gap structure of the superfluid. Boosts in momentum space (Lorentz transformations) correspond to rotations in real space that preserve the gap texture.

#### Fermi Liquid Instability and Pairing

The key insight is that the paired (superfluid) state is not just lower in free energy than the normal Fermi liquid — it is *energetically inevitable* if the interaction is attractive.

The BCS free energy functional is:

$$F[T, V] = \int \frac{d^3k}{(2\pi)^3} \left[ 2\epsilon_k - 2\sqrt{\Delta^2 + \epsilon_k^2} + \frac{\Delta^2}{g(k)} \right]$$

where $g(k)$ is the attractive interaction strength and $\epsilon_k$ is the single-particle energy relative to chemical potential.

At the transition temperature $T_c$, the second derivative $\partial^2 F / \partial \Delta^2 = 0$. For $T < T_c$, the gapped state is a global minimum of the free energy.

**Cosmological interpretation**: Just as the Fermi liquid is unstable to BCS pairing in superfluid 3He, the high-temperature early universe is unstable to condensate formation. The instability is driven by the same mechanism: an attractive interaction in the quantum vacuum.

### Part II: Emergence of Gauge Fields and Symmetries

#### Berry Phase and Effective Gauge Fields

Consider a quasiparticle wavefunction $|\psi(\mathbf{r})\rangle$ that evolves slowly in a spatially varying order parameter $\mathbf{d}(\mathbf{r})$. The adiabatic evolution acquires a **Berry phase**:

$$\gamma = i \oint \langle \psi(\mathbf{r}) | \nabla \psi(\mathbf{r}) \rangle \cdot d\mathbf{r}$$

This is equivalent to coupling to an effective gauge potential:

$$\mathbf{A}_{\text{eff}} = i \langle \psi | \nabla \psi \rangle$$

For a spin-orbit coupled system (like 3He-A), the Berry connection comes in SU(2) form:

$$A_i^a = i \langle \psi | \nabla_i \sigma^a | \psi \rangle$$

where $\sigma^a$ are Pauli matrices. This is a **non-abelian gauge field** — identical in structure to weak-force gauge fields.

**Remarkable result**: Gauge fields are not imposed by hand. They are *necessities* arising from the texture of the order parameter. A smooth variation in $\mathbf{d}(\mathbf{r})$ automatically generates gauge fields.

#### Lorentz and Rotational Symmetries

The low-energy Hamiltonian in 3He-A has the form:

$$H = p_F v_F [\gamma^0 \partial_0 + \gamma^i (\partial_i - A_i)] + \ldots$$

where $\gamma$ matrices are the Dirac algebra. This is **Lorentz covariant**: it respects the symmetry group SO(3,1).

But Lorentz symmetry is not fundamental — it is an *emergent* symmetry of the low-energy effective theory. The microscopic theory (the fermionic Fermi liquid) has no such symmetry. The symmetry emerges because:

1. The superfluid gap has a preferred direction (breaking rotations)
2. Low-energy excitations live on the Fermi surface
3. For these excitations, the only relevant energy scale is the Fermi velocity $v_F$
4. At momenta $k << p_F$, the dispersion is precisely linear: $\epsilon \propto k$
5. Linear dispersion is Lorentz invariant

**Implication for cosmology**: The Lorentz symmetry observed in our universe is not a fundamental law but an emergent feature valid at low energies. Above some "Planck scale" energy (where the effective theory breaks down), Lorentz invariance is violated. Physics is fundamentally non-relativistic; we observe Lorentz symmetry because we are low-energy observers.

This has profound consequences:
- Tests of Lorentz symmetry (constraints on SME violations) are tests of the effective theory validity, not fundamental laws.
- Quantum gravity is not fundamentally Lorentz invariant; it is a UV completion of an effective theory.
- Planck-scale physics can violate Lorentz symmetry; this is not pathological but expected.

### Part III: Cosmological Phenomena in the Superfluid Analogy

#### Inflation from Phase Transitions

The universe begins at high temperature $T >> T_c$ in a **disordered phase**:
- No condensate, no gap
- Excitations are gapless (massless)
- Entropy density: $s \sim T^3$
- Radiation-dominated equation of state: $w = 1/3$

At $T = T_c$, a **phase transition** occurs. The order parameter $\mathbf{d}(\mathbf{r})$ acquires a non-zero value. The condensate forms rapidly (on timescales set by the critical dynamics, not arbitrarily fast).

The latent heat released is:

$$L = T_c \Delta s = T_c [s_+ - s_-]$$

where $s_\pm$ are entropies above and below $T_c$. For a weakly-coupled BCS transition:

$$\Delta s \sim N(0) T_c^2 \Delta^2$$

This heat goes into kinetic energy of the expansion. The universe inflates as the latent heat is converted to work:

$$H = \frac{\dot{a}}{a} \propto \sqrt{\rho_{\text{latent}} / M_{\text{Planck}}^2}$$

**Duration**: The transition completes on a timescale set by nucleation and growth of the condensate. In laboratory 3He, this timescale is microseconds. In the universe, it is set by the friction (damping) acting on the order parameter evolution.

**Key difference from Guth inflation**: There is no slow-roll scalar field with a potential. Instead, the "inflaton" is the order parameter itself, and the potential emerges from the many-body dynamics of the condensate formation process.

#### Texture-Generated Defects

As the universe cools through $T_c$, the order parameter $\mathbf{d}(\mathbf{r})$ forms a random pattern. In different spatial regions, $\mathbf{d}$ points in different directions. Where domains meet, **topological defects** form:

- **Monopoles**: Points where $\mathbf{d}$ winds around all directions (hedgehog texture)
- **Cosmic strings**: Vortex lines where $\mathbf{d}$ is undefined
- **Domain walls**: 2D surfaces separating regions with opposite $\mathbf{d}$

These are not separately generated objects — they are inevitable consequences of the symmetry-breaking transition.

**Calculation**: The defect density is determined by the Kibble-Zurek mechanism:

$$n_{\text{defect}} \propto \frac{1}{\xi^3}$$

where $\xi$ is the correlation length at the phase transition:

$$\xi \propto \left( \frac{d\Phi}{dt} \right)^{-1/2}$$

and $\Phi$ is the order parameter. For a slow transition (fast cooling, large $d\Phi/dt$), $\xi$ is small and defect density is high. For a fast transition (slow cooling), $\xi$ is large and defects are sparse.

**Observational constraint**: WMAP and Planck data constrain topological defect contributions to the CMB power spectrum. If cosmic strings existed, they would produce distinctive line-shaped temperature distortions. Current limits allow defect contributions of order 10% or less.

In the superfluid analogy, this is not a problem — the defect density is a dynamical quantity determined by the cooling rate, not a fixed prediction. A sufficiently fast phase transition produces sparse defects.

#### Cosmological Constant from Equilibrium

In the low-temperature (ordered) phase, the vacuum energy density is:

$$\rho_{\text{vac}} = \frac{F[T, V]}{V}$$

where $F$ is the Helmholtz free energy. At $T = 0$:

$$F = -\int \frac{d^3k}{(2\pi)^3} \sqrt{\Delta^2 + v_F^2 k^2}$$

This integral diverges (it is the zero-point energy of all occupied quasiparticles). However, this is the *absolute* vacuum energy. What we measure is the *relative* energy density:

$$\Delta \rho = \rho_{\text{vac}} - \rho_{\text{ref}}$$

where $\rho_{\text{ref}}$ is a reference value (e.g., the energy of the same system at very high temperature).

At equilibrium ($T = 0$, $\mu = \mu_0$), the relative vacuum energy is:

$$\Delta \rho = 0$$

by definition — we choose $\mu_0$ such that the system is in its ground state.

**Observable cosmological constant**: The observed CC corresponds to small deviations from equilibrium:
- Non-zero temperature: $T > 0$ → $\rho \sim T^4$
- Non-zero chemical potential shift: $\delta \mu \neq 0$ → $\rho \sim \delta \mu^4$

If the universe is close to its ground state, both deviations are small, explaining the observed small CC.

**No fine-tuning required**: The CC is small not because of miraculous cancellations but because equilibrium (ground state) has zero CC by definition.

#### Axial Anomaly and Baryon Production

In a superfluid with chiral fermions (like 3He-A), the axial current $j^5_\mu = \bar{\psi} \gamma^5 \gamma^\mu \psi$ is not conserved at the quantum level. Instead, it satisfies the Adler-Bell-Jackiw (ABJ) anomaly:

$$\partial_\mu j^5_\mu = \frac{N_f}{16\pi^2} F_{\mu\nu} \tilde{F}^{\mu\nu}$$

where $F_{\mu\nu}$ is the effective gauge field strength and $\tilde{F}^{\mu\nu}$ is its dual.

In 3He-A, this anomaly has been verified experimentally via measurements of spin and orbital angular momentum currents (Volovik and Khazan, 1987-1993).

**Cosmological application**: During the early-universe QCD phase transition or electroweak transition, the effective gauge fields (gluons, W/Z bosons) have non-zero $F \tilde{F}$. This drives the axial anomaly, generating excess baryons (or antibaryons, depending on the sign of the anomaly).

Sakharov's necessary conditions for baryogenesis (baryon number violation, C and CP violation, departure from equilibrium) are all satisfied:
- Baryon number violation: Anomaly
- CP violation: Possible from CKM matrix or other sources
- Departure from equilibrium: The phase transition takes finite time

The magnitude of baryogenesis can be estimated from the anomaly coefficient and the field strength:

$$n_B \propto \frac{N_c N_f}{16\pi^2} \int F \tilde{F}$$

---

## Key Results

1. **Superfluid universality**: Elementary particle physics is the low-energy effective theory of quasiparticles in a superfluid-like quantum vacuum. Weyl fermions, gauge fields, and Lorentz symmetry all emerge from the superfluid structure.

2. **Lorentz symmetry is emergent**: Linear dispersion $\epsilon \propto k$ at low energies produces Lorentz invariance. Above the Planck scale, Lorentz symmetry is violated. Tests of SME provide constraints on effective theory validity.

3. **Inflation without inflation**: Phase transitions in the vacuum release latent heat, driving expansion. No scalar inflaton field is required; the "inflaton" is the order parameter itself.

4. **Texture-generated defects**: Topological defects (monopoles, strings, domain walls) form inevitably during phase transitions via the Kibble-Zurek mechanism. Defect density depends on cooling rate, not fundamental parameters.

5. **CC resolved**: Vacuum energy is zero at equilibrium. Small deviations (temperature, chemical potential) produce the observed small CC. No 120-order-of-magnitude fine-tuning needed.

6. **Baryon asymmetry from anomalies**: The ABJ anomaly generates baryon number violation during phase transitions. The magnitude is calculable from field-strength integrals.

7. **Event horizons are universal**: Any system with an effective metric can have event horizons. Hawking radiation follows from vacuum thermodynamics, not specific to gravitational black holes.

---

## Impact and Legacy

The 2001 review established superfluid analogs as a central paradigm in quantum gravity research. Subsequent developments include:

1. **Experimental advances**: Hawking radiation simulated in sonic black holes (Garay et al. 2000, Schützhold et al. 2005), BEC analog systems for vortices and defects.

2. **Theoretical extensions**: The analog paradigm was extended to condensed matter realizations of curved spacetime, black hole thermodynamics, and entanglement entropy.

3. **Holography connection**: The anti-de Sitter/conformal field theory (AdS/CFT) correspondence (Maldacena 1997) shares deep structural similarities with the superfluid analogy: in both, a higher-dimensional bulk spacetime emerges from lower-dimensional quantum physics.

4. **Topological matter**: The discovery of topological insulators (Kane-Mele 2005, Hasan-Kane 2010) and topological superconductors (from Volovik's earlier work, 1990s) validated the topological classification of gapped fermionic systems — a core prediction of the superfluid analogy.

5. **Lattice gauge theory**: The connection between emergent gauge fields (from superfluid textures) and lattice QCD was made more concrete. The superfluid analogy suggests that continuum gauge theories emerge from discrete lattice models in the long-wavelength limit.

---

## Connection to Phonon-Exflation Framework

### Fundamental Mechanism

The superfluid analogy and phonon-exflation are structurally identical:

| Superfluid 3He-A | Phonon-Exflation on SU(3) |
|:---|:---|
| Fermi liquid substrate | NCG spectral triple |
| BCS Cooper pairing | K_7 flavor-pairing instability |
| Order parameter $\mathbf{d}(\mathbf{r})$ | Jensen deformation tensor |
| Gap $\Delta$ | Spectral action minimum |
| Quasiparticles | Phonon modes (Dirac eigenstates) |
| Emergent gauge fields | Yang-Mills from texture |
| Low-energy Weyl fermions | Quarks, leptons from Psi_+ |

The phonon-exflation mechanism is therefore a **superfluid analog of cosmological expansion**, where:
- The "superfluid" is the SU(3) geometry itself
- The "Cooper pairs" are phonon mode condensates
- The "expansion" is the cosmological evolution of the compactification radius

### BCS Instability and Cosmological Dynamics

In superfluid 3He-A, the transition from Fermi liquid to superfluid is *inevitable* if the interaction is attractive. Session 35 established that in the K_7 sector, the RG-BCS-35 theorem shows: *any g > 0 flows to strong coupling*. There is no critical threshold.

This directly parallels Volovik's finding that the phase transition is not optional — it is dynamically required. The expanding universe in phonon-exflation is thus not a separated process but a *necessary consequence* of the microscopic coupling structure.

### Textures and Cosmological Defects

As the phonon condensate forms (driven by the K_7 pairing instability), the order parameter (Jensen deformation) develops spatial variations. These variations produce:
- Emergent Yang-Mills fields (color charges)
- Topological defects (domain walls, vortex-like singularities)
- Effective metric curvature (from spectral action)

The defect network is a *relic* of the phase transition, analogous to cosmic strings in Volovik's scenario.

### Planck Scale and Transplanckian Physics

Volovik's crucial observation is that effective field theory breaks down above the Planck scale. In the superfluid, this scale is set by the gap and Fermi velocity:

$$E_{\text{Planck}} \sim v_F \Delta$$

Excitations with energy above this scale cannot be described as quasiparticles in the long-wavelength limit; the microscopic structure (the fermionic lattice) becomes relevant.

In phonon-exflation, the analog is:
- Planck scale = gap in the phonon spectrum $\Delta = \Delta_0$
- Below Planck scale: effective field theory (low-energy phonons)
- Above Planck scale: full SU(3) geometry and spectral structure (microscopic degrees of freedom)

This provides a *microscopic UV completion* of cosmology: we can in principle compute what happens beyond the Planck scale by studying the full spectral triple.

### Hawking Radiation and Particle Creation

Session 38 established that the phonon condensate undergoes **sudden quenching** during the expansion phase. This produces pair creation:

$$\psi_{\text{final}} = U(t) \psi_{\text{initial}}$$

The unitary evolution generates particle pairs via the instanton mechanism (Schwinger pair creation). The resulting state is a **GGE** (generalized Gibbs ensemble) characterized by Richardson-Gaudin integrals.

This is Volovik's prediction realized: particle creation at a "horizon" (the condensate formation boundary), producing a non-thermal spectrum of excitations.

### Vacuum Energy Saturation

Volovik's resolution of the CC problem applies directly to phonon-exflation:

The spectral action in the ground state (condensed phase) yields:

$$S_{\text{spec}} = \int d^4x \sqrt{g} \left[ \frac{C_0}{16\pi G} R + \ldots \right]$$

where $C_0$ is computed from the Dirac spectrum. This is the *absolute* action. But cosmologically, we measure the *change* in action as the universe expands:

$$\Delta S = S(t_f) - S(t_i)$$

If the initial and final states are both near equilibrium, $\Delta S \approx 0$. The observed expansion is driven by *kinetic* energy of the order parameter evolution, not by vacuum energy.

This naturally explains a small but non-zero cosmological constant without the infamous 120-order fine-tuning.

### The Missing Ingredient: Coupling to Gravity

Volovik's superfluid model exists in *flat space* (or with an imposed external metric). The order parameter evolves according to its own dynamics; spacetime curvature is not backreacting.

In phonon-exflation, the situation is more subtle: the phonon excitations *are* the fields of our universe, and they couple back to the metric via the Einstein equation:

$$G_{\mu\nu} = \frac{8\pi G}{M_{\text{Planck}}^2} T_{\mu\nu}$$

where $T_{\mu\nu}$ is the energy-momentum tensor of the phonon field. The full problem requires solving coupled Einstein-order-parameter equations, not just the order-parameter dynamics alone.

Session 38 touched on this (backreaction 3.7%, underdamped transit completes), but a full treatment of coupled dynamics remains open (FRIEDMANN-BCS-38 gate).

---

## References and Further Reading

- Volovik, G.E. (2001). "Superfluid analogies of cosmological phenomena". *Physics Reports* 351, 195-246. arXiv:gr-qc/0005091.
- Volovik, G.E. (2003). *The Universe in a Helium Droplet*. Oxford University Press.
- Volovik, G.E. & Khazan, M. (1989). "Magnetic vortices in superfluid 3He-A and in Yang-Mills theory". *JETP Lett.* 49, 201.
- Volovik, G.E. & Kopnin, N.B. (1997). "Topology of the order parameter and the defects in superfluid 3He". *Rep. Prog. Phys.* 58, 1517.
- Unruh, W.G. (1981). "Experimental Black-Hole Evaporation?" *Phys. Rev. Lett.* 46, 1351.
- Garay, L.J., Anglin, J.R., Cirac, J.I., & Zoller, P. (2000). "Sonic Black Holes in Dilute Bose-Einstein Condensates". *Phys. Rev. Lett.* 85, 4643.
- Schützhold, R., Uhlmann, M., Petri, Y., & Schaller, G. (2005). "Hawking radiation in ordinary laboratory systems". *Phys. Rev. Lett.* 97, 190405.
