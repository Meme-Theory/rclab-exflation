# Cosmological Experiments and the Theory of Phase Transitions

**Author(s):** Wojciech H. Zurek
**Year:** 1985
**Journal:** Nature, Physical Review Letters

---

## Abstract

Zurek extended Kibble's work on cosmological phase transitions by connecting the number of topological defects formed to the critical exponents and quench rate of the phase transition. He derived the universal scaling law: the density of defects is inversely proportional to the correlation length at the critical moment, which in turn depends on the rate at which the system is driven through the transition. This quantifies Kibble's intuition and provides testable predictions for defect abundance in the early universe and condensed matter systems.

---

## Historical Context

Kibble's 1976-1980 work established that topological defects form when phase transitions occur too rapidly for the system to maintain equilibrium. However, his work lacked quantitative predictions for defect density as a function of physical parameters. Zurek remedied this by applying critical-phenomena theory, showing that the scaling laws for defect formation are determined by the critical exponents of the phase transition itself. This connection made the Kibble mechanism quantitatively predictive and experimentally testable.

Zurek's insight also extended beyond cosmology: the same mechanism should be observable in the laboratory when superfluids, superconductors, and quantum systems undergo rapid phase transitions. This prediction has since been validated in numerous experiments.

---

## Key Arguments and Derivations

### The Kibble-Zurek Mechanism (KZM) Scaling

During a phase transition, the system's dynamics are governed by the correlation time τ_corr and correlation length ξ. Near the critical point T_c:

τ_corr ~ |T - T_c|^{-νz}

ξ ~ |T - T_c|^{-ν}

where ν is the correlation-length critical exponent and z is the dynamic critical exponent. For a quench where temperature decreases as T(t) = T_c - t/τ_Q (τ_Q is the quench timescale), the system remains adiabatic (follows the equilibrium path) until the relaxation time matches the cooling timescale:

τ_corr ~ τ_Q

This occurs at a "freeze-out" temperature:

|T_freeze - T_c| ~ (τ_Q)^{1/(νz + 1)}

### Freeze-Out Correlation Length

At the freeze-out moment, the correlation length is:

ξ_freeze ~ (τ_Q)^{ν/(νz + 1)}

This is the size of causally-connected regions that independently choose their symmetry-breaking direction. The density of topological defects is:

n_defects ~ ξ_freeze^{-d} ~ (τ_Q)^{-dν/(νz + 1)}

### Universality

The scaling exponents (ν, z) depend only on the symmetry-breaking pattern and spacetime dimension, not on the microscopic details. Thus:

- Different materials undergoing similar phase transitions produce the same scaling.
- Cosmological defect abundance can be predicted from knowledge of critical exponents.

### Application to Cosmology: The Quench Rate

In cosmology, the "quench" is the expansion of the universe cooling the plasma. The cooling rate is set by the expansion rate H:

dT/dt = -H T

For a transition at temperature T_c with duration Δt ~ 1/H, the quench rate is:

τ_Q ~ 1/H_c ~ T_c^{-1} × (some function of G_N)

Thus, defect density depends on the GUT scale energy density: higher-temperature transitions produce more abundant defects.

### Example: Electroweak Phase Transition (T_c ~ 100 GeV)

- Critical exponents: ν ~ 0.6, z ~ 2 (approximately)
- Quench rate: τ_Q ~ 1 GeV (set by Hubble rate at T = 100 GeV)
- Freeze-out length: ξ ~ (1 GeV)^{-1} ~ 10⁻³ fm
- Domain density: n_domains ~ (0.1 GeV)³ ~ 10²⁷ m⁻³

### Deviations and Scaling Violations

For very fast quenches (τ_Q → 0), or far from the critical point, the scaling law can break down. Zurek showed that deviations occur when:

1. The system enters the "impulse regime" where no relaxation occurs.
2. Finite-size effects become important.
3. Higher-order critical phenomena (tricritical points, etc.) modify scaling.

---

## Key Results

1. **Universal Scaling Law**: The scaling law n ~ (τ_Q)^{-dν/(νz+1)} is universal across different systems and different critical phenomena.

2. **Defect Density Prediction**: For a given phase transition characterized by known critical exponents, the defect abundance is predicted from the quench rate alone.

3. **Robustness**: The mechanism is robust—deviations from slow-roll or other approximations do not destroy the scaling, which depends only on critical exponents.

4. **Experimental Tests**: Laboratory tests of the mechanism in cold atoms, superfluids, and superconductors have confirmed the scaling predictions to high precision.

---

## Impact and Legacy

Zurek's work enabled quantitative predictions for early-universe defect production:

- **Monopole Problem Redux**: Applying KZM to GUT-scale transitions predicts monopole over-abundance, confirming that inflation (or other mechanisms) must suppress them.

- **Cosmic String Constraints**: CMB observations constrain cosmic string tension and abundance, which directly test KZM predictions.

- **Condensed Matter Analog**: The Kibble-Zurek mechanism is now routinely observed in laboratory systems, from BEC quenches to ion traps to superconductor transitions, validating the theory.

- **Extensions to Quantum Domains**: Zurek's formalism extends to quantum phase transitions (where T_c → 0 and quantum fluctuations dominate), with z → ∞ and different exponent values.

Follow-up work includes studies of defect dynamics, interactions, and annihilation (Long, 1994), applications to axion cosmology (Sikivie, 2008), and quantum simulations (Kibble-Zurek in cold atoms).

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: HIGH**

The Kibble-Zurek mechanism describes **universal defect-formation scaling** at **rapid phase transitions**. In phonon-exflation, the transit through the fold is a **first-order** phase transition (not continuous), so KZM strictly applies only in modified form. However, the framework claims the **structure** of GGE pair formation parallels KZM:

1. **Quench Rate in the Framework**: The Jensen deformation parameter τ changes from 0.190 → 0.191 over a timescale Δt ~ 10⁻³⁸ s. The effective "quench rate" is:

   τ_Q ~ Δt ~ 10⁻³⁸ s

   This is **hyper-fast** (Planck-scale timescales). According to KZM, defect density diverges in this limit:

   n_defects ~ (τ_Q)^{-α} → ∞

   Framework resolves this by claiming the first-order transition (not continuous) modifies the scaling. **Test**: Measure whether GGE pair density diverges or saturates at the fold.

2. **Freeze-Out Length as Fiber Width**: The causally-connected horizon during the transit is:

   ξ_freeze ~ c_s × Δt ~ (0.1 c) × 10⁻³⁸ s ~ 10⁻³⁹ m

   This is smaller than the fiber correlation length ξ_fiber ~ 10⁻³⁵ m (Planck scale). **Result**: Different parts of the fiber cannot causally communicate; each "decides" independently whether to form a pair. This is Kibble-Zurek in spectral geometry.

3. **Defect Count Matches Prediction**: Framework predicts 59.8 pairs ~ 120 degrees of freedom (including boson/fermion doubling). KZM with first-order scaling predicts:

   n_defects ~ (spectral_energy_scale) / (symmetry_breaking_scale)

   If spectral energy ~ 10¹⁶ GeV and symmetry breaking ~ E_fold ~ 10¹⁵ GeV, then n ~ 10. Framework gets ~120 because of multiple channels (scalar, vector, fermion). **Test**: Count defects in exact spectral geometry; compare to experiment.

4. **Observable Imprint**: If GGE pairs are topological defects (which they are, in the sense of Hilbert-space winding), they should produce characteristic signatures in CMB and large-scale structure, analogous to cosmic string observables. **Current status**: No such signatures detected at >99% CL, suggesting framework must explain why GGE defects are "invisible" to classical topology (perhaps because they are defects in **entanglement**, not in real-space fields).

**Quantitative test**: Apply Zurek scaling to the spectral-action first-order transition and compute n_GGE_pairs. Compare to 59.8 (framework prediction). If they match, KZM universality extends to spectral geometry.
