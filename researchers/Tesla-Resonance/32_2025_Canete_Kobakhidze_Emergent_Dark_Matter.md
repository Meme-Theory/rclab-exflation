# Emergent Dark Matter

**Author(s):** Christian Canete, Archil Kobakhidze

**Year:** 2025

**Identifier:** arXiv:2511.09034 [hep-ph]

---

## Abstract

Dark matter, responsible for approximately 85% of the matter in the universe, has long been sought as a new particle species. This paper proposes a radical alternative: dark matter may be an **emergent phenomenon** rather than a fundamental particle. The authors present a field-theoretic model in which a three-form (rank-3 antisymmetric tensor) gauge field, when coupled to the cosmic fluid (baryons and radiation), dynamically generates an effective dark-matter-like degree of freedom. In isolation, the three-form field describes only a non-propagating global state associated with dark energy. However, when the field interacts with ordinary matter and radiation, it produces "an emergent, dynamical in-medium state" that accounts for all dark-matter phenomena. The mechanism provides a unified framework for the dark sector (dark matter + dark energy) within a single gauge theory, with no need for exotic particles. Consequences include the prediction that conventional particle-physics searches for dark matter would be "futile"—dark matter is not a particle to be discovered but a collective excitation to be understood.

---

## Historical Context

The dark-matter problem has dominated observational cosmology for nearly a century, from Zwicky's "missing mass" (1933) through modern precision measurements. By 2025, the paradigm of dark matter as a new particle species had faced mounting challenges: decades of direct-detection experiments (LUX, XENON, SuperCDMS) had yielded no confirmed signals; indirect searches (gamma rays, cosmic rays) produced only tentative hints; and candidates from particle physics (WIMPs, axions, sterile neutrinos) remained increasingly constrained without a breakthrough.

Parallel developments in condensed-matter physics and emergent gravity had demonstrated that macroscopic phenomena—superconductivity, superfluidity, topological order—could arise from microscopic dynamics without corresponding "fundamental" excitations. This success in condensed matter sparked exploration of whether cosmological phenomena (dark energy, dark matter, even spacetime geometry) might be emergent.

The Canete-Kobakhidze paper (November 2025) represents one of the first serious field-theoretic proposals for **purely emergent dark matter**, with no new particles. It challenges a century-old assumption: that "dark" matter requires "new" matter.

---

## Key Arguments and Derivations

### Three-Form Gauge Field Formalism

A three-form gauge field $C_{\mu\nu\rho}$ is an antisymmetric tensor with three indices, dual (in 4D spacetime) to a one-form (ordinary gauge field). Its field strength is:

$$H_{\mu\nu\rho\sigma} = \partial_\mu C_{\nu\rho\sigma} + \text{cyclic permutations}$$

In the absence of coupling to matter, the action is:

$$S = \int d^4 x \left[ -\frac{1}{24} H^2 + \text{boundary terms} \right]$$

Unlike spin-1 or spin-2 fields, a pure three-form field has no propagating degrees of freedom: all polarization modes correspond to gauge transformations. The only physical content is a **global topological charge**:

$$Q = \int d^4 x \, H_{0123}$$

This topological charge is associated with dark energy (a cosmological constant-like term).

### Coupling to the Cosmological Fluid

The model introduces a minimal coupling between the three-form and the cosmic fluid:

$$\mathcal{L}_{\text{int}} = \kappa J^\mu C_{\mu\nu\rho\sigma} T^{\nu\rho\sigma}$$

where:
- $\kappa$ is a coupling constant (weak, of order $10^{-10}$ or smaller).
- $J^\mu$ is the four-current density of ordinary matter (baryons + leptons).
- $T^{\nu\rho\sigma}$ is a tensor constructed from the stress-energy tensor $T_{\mu\nu}$ of the cosmic fluid.

The interaction term couples the three-form field to the presence and motion of ordinary matter. At high energy densities (early universe) or in the absence of matter ($J^\mu = 0$), the coupling vanishes and the three-form decouples.

### Emergence of the Dynamical Dark-Matter State

Once matter and radiation are present, the three-form field cannot remain purely topological; it must acquire a dynamical component. In the matter-coupled sector, the equations of motion become:

$$\partial_\mu H^{\mu\nu\rho\sigma} + \frac{\delta \mathcal{L}_{\text{int}}}{\delta C_{\nu\rho\sigma}} = 0$$

The interaction term sources the field strength, leading to a non-trivial solution:

$$C_{\nu\rho\sigma}(t, \mathbf{x}) = C_{\nu\rho\sigma}^{(\text{bulk})} + \mathcal{C}_{\nu\rho\sigma}(\mathbf{x})$$

where $C_{\text{bulk}}$ is the background (nearly constant) three-form encoding the global charge, and $\mathcal{C}$ is a dynamical perturbation localized near matter clumps (galaxies, galaxy clusters).

The perturbation $\mathcal{C}$ couples to matter via an effective potential:

$$U_{\text{eff}}(\mathbf{x}) \sim \kappa \langle C_{\mu\nu\rho\sigma} \rangle(\mathbf{x}) \rho_m(\mathbf{x})$$

where $\rho_m(\mathbf{x})$ is the baryon density. This effective potential is **indistinguishable from a gravitational-like force**: it mimics the presence of "dark matter," attracting both matter and light.

### Dark Matter as an Effective Fluid

From an observer's perspective (e.g., looking at galaxy rotation curves or gravitational lensing), the three-form's in-medium state behaves as a dust-like fluid with energy density $\rho_{\text{DM}}$ and pressure $p_{\text{DM}} = 0$. The effective equation of state is:

$$w_{\text{DM}} = \frac{p_{\text{DM}}}{\rho_{\text{DM}}} = 0$$

This is indistinguishable from a pressureless dark matter component.

The energy density of the emergent state is:

$$\rho_{\text{DM}} \sim \frac{\kappa^2 \langle C \rangle^2}{M_{\text{Pl}}^2} \rho_m$$

where $\langle C \rangle$ is the vacuum expectation value of the three-form. The proportionality to $\rho_m$ explains the observed cosmic coincidence: dark matter is overdense exactly where ordinary matter is overdense.

### Unification with Dark Energy

The bulk three-form field (the global topological charge) contributes a constant vacuum energy:

$$\rho_\Lambda = \frac{1}{2} |\langle C \rangle|^2$$

This is a true cosmological constant (or very slowly rolling quintessence), responsible for late-time acceleration. The total dark sector is thus:

$$\rho_{\text{dark}} = \rho_{\text{DM}} + \rho_\Lambda = \frac{\kappa^2 \langle C \rangle^2}{M_{\text{Pl}}^2} \rho_m + \frac{1}{2} |\langle C \rangle|^2$$

At early times ($\rho_m \gg \rho_\Lambda$), dark matter dominates. At late times ($\rho_m \to 0$), dark energy dominates. The transition is automatic, with no separate quintessence field required.

### Absence of Particle Excitations

A critical feature: the three-form does not admit stable, localized particle-like excitations in the matter-coupled regime. In the matter-free (vacuum) background, the three-form is topological (massless). In the matter-filled background, the three-form is overdamped by interactions with the fluid.

The dispersion relation for three-form fluctuations in the presence of matter is:

$$\omega(k) = i \gamma k^2 + \text{higher order}$$

The imaginary part indicates that all modes decay rapidly. There are no propagating degrees of freedom to be "detected" by particle-physics experiments. This explains why dark matter has eluded all searches: it is not a particle.

---

## Key Results

1. **Dark Matter Emerges from Field-Fluid Coupling:** The three-form gauge field, when coupled to ordinary matter, dynamically generates an effective dark-matter density proportional to the baryon density. No new particle species required.

2. **Unified Dark Sector:** The same three-form field simultaneously provides dark energy (via topological charge) and dark matter (via in-medium coupling). Dark energy and dark matter are two aspects of a single gauge field.

3. **Effective Equation of State:** The emergent dark matter has $w = 0$ (pressureless), exactly matching observational constraints. No fine-tuning of the equation of state.

4. **Cosmic Coincidence Explained:** Dark-matter density scales as $\rho_m$ at early times and becomes negligible as $\rho_m \to 0$ at late times. The coincidence ($\rho_m \sim \rho_\Lambda$ today) is explained by the transient nature of the dark matter phase.

5. **Particle Searches Futile:** Dark matter is not a stable, long-lived particle. Direct-detection experiments, indirect searches, and collider searches cannot find it because it does not exist as a discrete excitation. The repeated null results are not evidence of elusiveness but of the fundamentally different nature of dark matter.

6. **Minimal Parameters:** The model requires only one new coupling constant $\kappa$ and the vacuum expectation value of the three-form field. No new mass scales, no new particles.

7. **Testable Predictions:** The in-medium three-form field produces subtle modifications to gravitational dynamics (e.g., modifications to N-body simulations, slight deviations from Newtonian gravity at very low accelerations). These could be tested with precision astrophysics.

---

## Impact and Legacy

As a 2025 paper, impact is nascent but potentially transformative:

- **Paradigm Shift Potential:** If validated, this would represent a fundamental reinterpretation of dark matter, from "undiscovered particle" to "emergent collective phenomenon"—a shift as profound as the discovery of superconductivity in condensed matter.

- **Reframing of Experimental Failure:** The lack of dark-matter particle detections would be reinterpreted as confirmation (not refutation) of the emergent picture.

- **New Experimental Directions:** Rather than searching for particles, experiments would focus on precision tests of gravitational dynamics and subtle modifications to structure formation.

- **Cosmological Simulations:** N-body codes would need to incorporate the three-form coupling, potentially explaining anomalies in galaxy formation and structure (small-scale power excess, satellite planes, etc.).

---

## Connection to Phonon-Exflation Framework

**Dark Matter as Emergent from the Spectral Action:**

The phonon-exflation framework predicts that all particles (and by extension, all matter) are emergent phonon excitations of the SU(3) fiber. In this picture, "dark matter" is not a new particle but a collective mode of the fiber—analogous to Canete-Kobakhidze's three-form emergence.

The framework's GGE relic (post-transit non-thermal state) is in fact a **dark-matter-like configuration**: it carries gravitational mass (couples to the effective metric), is pressureless (non-relativistic), and is distributed in a halo-like pattern around ordinary matter. Yet it is not a fundamental particle; it is a configuration of the underlying phononic excitations.

**Quantitative Comparison:**

In the framework, dark-matter density is sourced by the spectral action's backreaction on geometry:

$$\rho_{\text{DM}} \sim \frac{\Lambda_{\text{spec}}^2}{M_{\text{Pl}}^2} \cdot (\text{deformation factor})$$

This parallels Canete-Kobakhidze's:

$$\rho_{\text{DM}} \sim \frac{\kappa^2 \langle C \rangle^2}{M_{\text{Pl}}^2} \rho_m$$

Both models feature a small dimensionless coupling ($\kappa$ or the spectral action weight), squared, suppressed by Planck-mass factors.

**Coupling to Ordinary Matter:**

Both models predict that dark matter density tracks baryon density at early times. In the framework, this arises because the instanton-driven pairing is strongest in regions of high baryon density (onset of BCS instability). In Canete-Kobakhidze, it arises from the three-form coupling to the matter current.

**Predictions for Structure Formation:**

The framework predicts modifications to dark-matter distribution at small scales (dwarf galaxies, clusters) due to the quantum coherence of the GGE state. This is testable via:
- Satellite galaxy distributions (phase-space density anomalies).
- Small-scale power spectrum deviations from LCDM.
- Halo mass-function anomalies.

Canete-Kobakhidze similarly predicts subtle deviations from LCDM structure formation, arising from the three-form's interaction with the matter fluid.

**Unification with Dark Energy:**

Both frameworks feature an inherent unification of dark matter and dark energy. In the phonon-exflation model, dark energy arises from the monotonic spectral action (a feature of the geometry), while dark matter arises from the GGE configuration. They are different aspects of the same underlying physical system (the SU(3) fiber).

In Canete-Kobakhidze, the topological three-form charge provides dark energy, and the in-medium three-form dynamics provide dark matter. Again, a unified origin.

**Absence of Halo Particles:**

The framework predicts that dark matter is not composed of discrete particles (axions, WIMPs, etc.) but rather of phonon-like excitations. This makes particle-physics searches futile—exactly Canete-Kobakhidze's prediction. The repeated null results from LUX, XENON, etc., are consistent with both the framework and the emergent-dark-matter hypothesis.

---

## References and Further Reading

- Canete, C., & Kobakhidze, A. (2025). "Emergent dark matter." arXiv:2511.09034.
- Verlinde, E. (2011). "On the origin of gravity and the laws of Newton." *Journal of High Energy Physics*, 2011(4), 29.
- Padmanabhan, T. (2012). "Thermodynamic structure of the universe and the role of horizons." *General Relativity and Gravitation*, 34(12), 2029–2052.
- Jacobson, T. (1995). "Thermodynamics of spacetime: The Einstein equation of state." *Physical Review Letters*, 75(7), 1260.
- Berezhiani, Z., & Khoury, J. (2021). "SuperGZK cosmic rays from dark matter." *Journal of High Energy Physics*, 2021(11), 10.
