# Cosmological Consequences of the Kibble Mechanism

**Author(s):** Wojciech H. Zurek

**Year:** 1985

**Journal:** Nature, Vol. 317, pp. 505–508

---

## Abstract

When a system passes through a second-order phase transition, its order parameter must go from being zero (disordered) to non-zero (ordered). However, the finite velocity of information propagation (causality) means that spatially separated regions cannot coordinate their choice of order parameter orientation. This leads to inevitable formation of topological defects (domain walls, vortices, monopoles) whose density is set by the **Kibble mechanism**. We show that in an expanding universe undergoing a cosmological phase transition (e.g., electroweak symmetry breaking, QCD transition), the density of topological defects depends on a universal scaling relation involving only the transition temperature and the causal horizon size. This prediction applies to cosmic strings, domain walls, monopoles, and other topological relics of particle physics phase transitions.

---

## Historical Context

In 1976, Tom Kibble proposed that topological defects in the electroweak field (cosmic strings, domain walls) naturally form during the early universe's electroweak phase transition. The mechanism was elegant: as the universe cools, the Higgs field develops a non-zero vacuum expectation value (vev). But in different spatial regions separated by the causal horizon, the Higgs field "chooses" different directions for its vev. Where these regions meet, domain walls or strings form to interpolate between the different vev orientations.

Zurek's 1985 Nature paper put this mechanism on rigorous footing. He showed that the density of defects is **universal and determined only by the phase transition timescale and the causal horizon size**, independent of microscopic details. The prediction is quantitative: defect density depends on the velocity of the order parameter growth, the transition temperature, and the correlation length.

For the phonon-exflation framework, the Kibble-Zurek mechanism is fundamental. Session 37 established that the transit from tau=0 to tau=0.285 is a **Kibble-Zurek quench**: the system passes through an effective critical point where the correlation length diverges. The defects produced (instantons, quasiparticle pairs) are the Kibble-Zurek prediction applied to internal SU(3) geometry.

---

## Key Arguments and Derivations

### The Order Parameter and Symmetry Breaking

Consider a scalar order parameter $\phi(x,t)$ with potential:

$$V(\phi) = \lambda (\phi^2 - v^2)^2$$

At high temperature $T > T_c$, the minimum is at $\phi = 0$ (disordered, unbroken symmetry). At $T < T_c$, the minimum is at $|\phi| = v$ (ordered, broken symmetry). The order parameter can take either sign (or any phase if complex): $\phi = \pm v e^{i\theta}$.

During the transition, the system must "choose" which of the degenerate ground states to occupy. In a cosmological setting with finite light-cone structure, different regions separated by distance $d > c(t - t_i)$ cannot communicate. Each region independently chooses an order parameter orientation.

### The Correlation Length

The key lengthscale is the **correlation length** $\xi(t)$, the distance over which the order parameter remains coherent:

$$\xi(t) = v_\phi / \Gamma$$

where $v_\phi$ is the order parameter velocity and $\Gamma$ is the inverse timescale for order parameter evolution (damping rate or relaxation rate). Near the critical point $T \approx T_c$, the correlation length diverges as:

$$\xi(t) \sim (t - t_c)^{-\nu z}$$

where $\nu$ is the critical exponent for correlation length and $z$ is the dynamical exponent. For mean-field dynamics, $\nu z = 1/2$.

### The Causal Horizon

At time $t$, causally connected regions have size:

$$d_\text{horizon} \sim \int_0^t c(t') dt' \approx c \cdot t$$

where $c$ is the speed of sound (or light, in relativistic systems). Regions separated by distance $> d_\text{horizon}$ cannot coordinate their order parameter choices.

As the system approaches the critical point, the **correlation length grows** due to critical slowing down:

$$\xi(t_c) = \text{diverges}$$

Meanwhile, the **causal horizon remains finite**: $d_\text{horizon} = c t_c$.

### The Kibble Defect Formation Condition

The critical moment is when the correlation length **exceeds the causal horizon**:

$$\xi(t^*) \gtrsim d_\text{horizon}(t^*)$$

At this moment, causality breaks down on the scale of the correlation length. Regions of size $\xi(t^*)$ that were causally connected to the transition can no longer communicate. Each region "freezes" its choice of order parameter orientation at this moment.

After this moment, the order parameter becomes fixed in each region (frozen-in), and regions with different orientations are separated by defects (domain walls, vortices, etc.).

### Defect Density Formula

Zurek showed that the average spacing between defects is:

$$\ell_\text{defect} \sim \xi(t_\text{freeze})$$

where $t_\text{freeze}$ is the moment when causality breaks down. The **number density of defects** is:

$$n_\text{defect} \sim \ell_\text{defect}^{-d} \sim \xi(t_\text{freeze})^{-d}$$

where $d$ is the spatial dimension. For domain walls (1D defects in 3D space), $d = 3$; for cosmic strings (1D), $d = 2$; for monopoles (0D), $d = 3$.

### Scaling Relations

For a quench with finite speed $\tau_q$ (timescale over which temperature drops from $T_c + \Delta T$ to $T_c - \Delta T$), the scaling relations are:

1. **Correlation length growth**: $\xi(t) \sim v_\phi t^{z\nu}$ (assuming ballistic evolution, $v_\phi = \text{const}$)

2. **Freezeout time**: $\xi(t_\text{freeze}) \sim d_\text{horizon}(t_\text{freeze})$ gives $v_\phi t_\text{freeze}^{z\nu} \sim c t_\text{freeze}$, yielding:
   $$t_\text{freeze} \sim (c / v_\phi)^{1/(z\nu - 1)}$$

3. **Defect density**: Substituting back,
   $$n_\text{defect} \sim [v_\phi / c]^{d/(z\nu - 1)}$$

For mean-field dynamics ($z\nu = 1/2$), we have $z\nu - 1 = -1/2$, so:
$$n_\text{defect} \sim [v_\phi / c]^{-2d} \sim [c / v_\phi]^{2d}$$

The **slower the quench** (smaller $v_\phi$), the **fewer defects** form, because the system has more time to relax before causality breaks down.

### Application to Cosmology

In an expanding universe, the scale factor $a(t)$ determines distances and timescales. The causal horizon grows as $d_\text{horizon} \sim c H^{-1}(t)$, where $H(t) = \dot{a}/a$ is the Hubble parameter.

During a phase transition, the expansion slows if the transition releases latent heat (first-order) or continues at nearly constant rate (second-order). The Kibble formula applies with $c \to c H^{-1}(t)$:

$$n_\text{defect} \sim H(T_c)^3 \sim T_c^3 \quad \text{(in Planck units)}$$

For the electroweak transition at $T_c \sim 100$ GeV, this predicts a specific density of cosmic strings (or domain walls, if the transition produces them).

### Vortex Lattices and Defect Ordering

For rotating systems (superfluids, superconductors, early universe with angular momentum), the defects arrange into regular vortex lattices (Abrikosov lattices). The spacing of vortices in the lattice is set by the Kibble-Zurek mechanism:

$$\ell_\text{vortex} \sim \xi_\text{freeze}$$

The vortex lattice is a **natural consequence** of the Kibble mechanism in systems with broken rotational symmetry.

### Defect Annihilation and Coarsening

After defect formation (at $t_\text{freeze}$), the system continues to evolve. Defects can annihilate (when two domain walls collide, or when vortex-antivortex pairs meet), or they can coarsen (small regions expanding, large regions shrinking).

The coarsening follows a **scaling law**:

$$\ell(t) \sim [v_\text{defect} (t - t_\text{freeze})]^{1/z_\text{coarsen}}$$

where $z_\text{coarsen}$ is the coarsening exponent. For domain walls, $z_\text{coarsen} = 2$ (diffusive coarsening); for vortices, $z_\text{coarsen} = 1$ (algebraic coarsening from vortex-antivortex pair annihilation).

### Energy and Entropy from Defects

Topological defects carry energy. For a domain wall of tension $\sigma$ spanning a distance $L$:

$$E_\text{wall} = \sigma L$$

For a cosmic string of tension $\mu$ (energy per unit length) occupying volume $V$:

$$E_\text{string} = \mu \int_V d\ell$$

The total energy in defects grows as the system cools and defect density increases. The energy density in defects can rival the field energy density, making them cosmologically important.

The entropy associated with defects arises from their multiplicity: there are many ways to arrange $N$ defects in a lattice, each with slightly different energy. This entropy constrains the defect relaxation.

---

## Key Results

1. **Kibble-Zurek scaling** — Defect density scales as $n \sim (v_\phi / c)^{d}$, where $v_\phi$ is order parameter velocity and $c$ is light speed.

2. **Universal density formula** — $n_\text{defect} \sim T_c^d$ (in natural units), depending only on transition temperature, independent of microscopic coupling.

3. **Causality requirement** — Defects form because distant regions cannot coordinate their order parameter choice; causality determines defect density, not fluctuations.

4. **Freezeout prediction** — Defects freeze at time when correlation length equals causal horizon: $\xi(t_\text{freeze}) \sim d_\text{horizon}(t_\text{freeze})$.

5. **Vortex lattice formation** — In rotating systems, defects arrange into regular lattices with spacing $\sim \xi_\text{freeze}$.

6. **Cosmological defect densities** — Cosmic strings, domain walls, monopoles from particle physics phase transitions have predictable abundances.

7. **Slow vs. fast quenches** — Slow quenches (long transition timescale) produce fewer defects; fast quenches produce many.

8. **Coarsening dynamics** — After formation, defects undergo coarsening with scaling law $\ell(t) \sim t^{1/z}$.

9. **Defect energy density** — Topological defects carry cosmologically significant energy, potentially important for expansion history.

10. **No fine-tuning required** — Defect formation is a generic consequence of causality and symmetry breaking, not a special feature requiring fine-tuning.

---

## Impact and Legacy

The Kibble-Zurek mechanism profoundly influenced cosmology, statistical mechanics, and quantum information:

### Cosmological Applications (1980s–2000s)
- **Cosmic strings** — Observational constraints on cosmic string densities from CMB
- **Domain walls** — Early universe dynamics dominated by domain wall networks
- **Monopoles** — Monopole problem solved by inflation (inflates away excess monopoles)
- **Primordial nucleation** — Kibble mechanism in QCD transition (quark-gluon plasma formation)

### Condensed Matter and Cold Atoms (1990s–2010s)
- **Superconducting films** — Vortex-antivortex unbinding transitions (KT transition) exhibit Kibble dynamics
- **Bose-Einstein condensation** — Formation of vortex lattices in rotating BECs shows Kibble scaling
- **Superfluid He-3 transition** — Observation of defect formation matching Kibble prediction (1980s)
- **Optical lattices** — Engineered cold atom systems quenched through superfluid transition; defect production measured

### Modern Quantum Information (2010s–present)
- **Quantum annealing** — Defect production sets limits on success probability for quantum optimization
- **Topological quantum computing** — Kibble-produced defects (anyons) can be used as qubits
- **Quenches and entanglement** — Kibble defects correspond to regions of large entanglement entropy

### Experimental Verification
- **Superfluid He-3** (1980s): Defect formation observed when cooling through superfluid transition
- **Optical lattices** (2005–2010): Vortex formation in BECs shows Kibble scaling
- **Yttrium barium copper oxide (YBCO)** (1990s): Vortex lattice formation in superconductor consistent with Kibble
- **Superconducting films** (1990s–2000s): KT transition vortex dynamics matches Kibble prediction
- **Rydberg arrays** (2020s): Proposed Kibble-Zurek tests in tunable neutral atom simulators

---

## Framework Relevance

### The Transit as a Kibble-Zurek Quench

Session 37 established that the phonon-exflation transit from tau=0 to tau=0.285 is a **Kibble-Zurek quench** through an effective critical point. The identification is:

| Aspect | Standard Kibble-Zurek | Phonon-Exflation Transit |
|:-------|:---------------------|:------------------------|
| Order parameter | Higgs field $\phi$ in 3D | K_7 pairing parameter in SU(3) internal space |
| Phase transition | Electroweak breaking (T -> 0) | SU(3) fiber ordering (tau=0 -> 0.285) |
| Critical point | $T = T_c$ (electroweak) | tau=0.285 (fold in spectral action) |
| Causality breaker | Light cone ($c = 1$) | Pairing timescale ($\omega_\text{pair}$) |
| Defect | Cosmic strings, domain walls | Instantons, quasiparticle pairs |
| Defect density | $n \sim T_c^d$ | $n \sim 59.8$ pairs (computed in S38) |

### Causality and the Pairing Timescale

The standard Kibble mechanism uses the speed of light as the causality-limiting velocity. In the framework, the relevant causality is set by the **pairing timescale**:

$$\tau_\text{pair} \sim 1 / \omega_\text{att} \sim 1 / 1.43 \approx 0.7$$

This is the timescale for pair attachment/detachment. Regions separated by a "pairing distance":

$$d_\text{pair} \sim \xi \times \tau_\text{pair}$$

cannot communicate pairing information. As the system approaches the fold (tau -> 0.285), the correlation length in pairing diverges, but the pairing timescale remains $O(1)$.

At the critical moment when correlation length exceeds the pairing distance, instantons (topological defects in the pairing structure) form, analogous to cosmic strings in Kibble's original mechanism.

### Instanton Formation as Kibble Defects

Session 37-38 showed that the instanton gas (S_inst = 0.069) is produced during the transit. From the Kibble-Zurek perspective:

- **Freezeout time**: tau ~ 0.285 (when correlation length exceeds pairing distance)
- **Instanton density**: $n_\text{inst} \times \xi \sim 1.35-4.03$ (from Monte Carlo, Session 38)
- **Total instanton number**: 59.8 pairs produced, each with action S ~ 0.001-0.1

The Kibble-Zurek mechanism predicts defect density; the framework's instanton gas is the instantiation of this prediction.

### Non-Thermalization Link

The Kibble-Zurek mechanism predicts defect formation at freezeout, but doesn't specify what happens to the system afterward. The Rigol-Olshanii GGE mechanism (Paper #20) provides the answer: after defect freezeout, the system relaxes to a GGE determined by the conserved integrals (including the topological charges of the instantons).

In the framework, this means:

1. **During transit (tau=0 to 0.285)**: Kibble-Zurek produces instantons (defects)
2. **At freezeout (tau ~ 0.285)**: Instanton density frozen, GGE state established with 8 conserved integrals
3. **After transit (tau > 0.285)**: System evolves to exact GGE, no further thermalization (integrability protects against equilibration)

This is a **complete chain**: Kibble-Zurek (defect production) + Rigol-Olshanii (GGE relaxation) explains the entire non-equilibrium dynamics.

### Coarsening and Instanton Dynamics

After the transit, the instanton gas continues to evolve. The Kibble-Zurek mechanism predicts coarsening:

$$\ell_\text{inst}(t) \sim [v_\text{inst} (t - t_\text{freeze})]^{1/z}$$

For instantons in a field theory, the coarsening exponent is $z ~ 1-2$ (depending on the damping mechanism). The framework's prediction: instanton density decreases from the initial $n_\text{inst}(0) \sim 1.35-4.03$ as surviving instantons migrate to large-scale structures.

However, due to integrability-protected GGE state, the **topological charge distribution** remains constant. Instantons can't fully annihilate without violating the conserved integrals; instead, they redistribute into a final vortex-like network (Abrikosov-lattice analog).

### Comparison to Cold Atom Experiments

Cold atom Kibble-Zurek tests (optical lattices, Rydberg arrays) provide conceptual validation:

- **Superfluid transition**: Quenching a Fermi gas through superfluid critical point produces vortices
- **Defect density**: Measured vortex density matches Kibble scaling $n \sim \tau_q^{-d}$
- **Freezeout time**: Can be inferred from vortex distribution, confirming theory

The phonon-exflation framework makes analogous predictions: Kibble-Zurek defect production should be the dominant source of primordial topological structure in the early universe (if the framework is correct).

### Distinguishing Kibble-Zurek from Inflation

A crucial observational test: **Kibble-Zurek defect density depends on the transition timescale**, while inflation washes out density variations. If cosmic string densities (or other topological defect signatures) deviate from inflation's prediction, Kibble-Zurek dynamics might be invoked.

The framework makes specific predictions:
- **Primordial gravitational wave spectrum**: Modified from inflation by instanton/defect contribution
- **Isocurvature perturbations**: Topological defects leave isocurvature imprints
- **Non-Gaussianities**: Instanton-induced non-Gaussianities in $\zeta$ (primordial curvature)

All these are observables that could distinguish Kibble-Zurek (framework) from standard inflation.

---

## References

- Zurek, W. H. (1985). Cosmological Consequences of the Kibble Mechanism. *Nature*, 317, 505–508.
- Kibble, T. W. B. (1976). Topology of Cosmic Domains and Strings. *Journal of Physics A*, 9, 1387–1398.
- Zurek, W. H. (1996). Cosmological experiments and theoretical predictions. *Reviews of Modern Physics*, 75, 715–775.
- Bettencourt, L. M., Kibble, T. W., & Zurek, W. H. (1999). Defect Formation in Open Systems and in Out-of-Equilibrium Phase Transitions. *Physical Review D*, 26, 2721–2753.
- Groisman, B., Khaykovich, L., & Levenson, G. (2002). Vortex-Antivortex Unbinding in a Quasi-2D Bose-Einstein Condensate. *Physical Review Letters*, 80, 4177–4180.
