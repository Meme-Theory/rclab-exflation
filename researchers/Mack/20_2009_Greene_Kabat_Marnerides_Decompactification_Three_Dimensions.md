# Dynamical Decompactification and Three Large Dimensions

**Author(s):** Brian Greene, Daniel Kabat, Stefanos Marnerides

**Year:** 2009

**Journal/ArXiv:** arXiv:0908.0955

---

## Abstract

The authors study string gas dynamics in the early universe seeking to realize the Brandenberger-Vafa mechanism, which aims to single out three or fewer spatial dimensions as the number that grow large cosmologically. This goal has eluded earlier works.

Considering wound string interactions in an impact parameter picture, the authors show that a strong exponential suppression occurs in interaction rates for d > 3 spatial dimensions. This reflects the classical argument that string worldsheets generically intersect in at most four spacetime dimensions. This description applies in the early universe if wound strings are heavy (wrapping long cycles) and diluted.

Considering the dynamics of a string gas coupled to dilaton-gravity, the authors find that: (a) for any number of dimensions the universe generically stays trapped in the Hagedorn regime, and (b) if the universe fluctuates to a radiation regime, any residual winding modes are diluted enough so that they freeze-out in d > 3 large dimensions while they generically annihilate for d = 3. In this sense, the Brandenberger-Vafa mechanism operates.

---

## Historical Context

The Brandenberger-Vafa (BV) mechanism was proposed two decades prior to this work as one of the few mechanisms within superstring theory aimed at explaining the hierarchy between three large and six small spatial dimensions. In this scenario, the early universe consists of a hot string gas in thermal equilibrium near the Hagedorn temperature (the transition temperature where string excitation modes become infinitely numerous).

The topology of space has non-trivial cycles supporting winding modes--strings wound around compact dimensions. The BV mechanism relied on a dimension-counting argument: wound strings generically intersect in at most three spatial dimensions, singling this out as the maximum number in which winding modes can track their equilibrium values and drop to zero, allowing those dimensions to grow large.

However, subsequent work encountered difficulties. Prior numerical simulations and analytic studies found "all-or-nothing" behavior: either all dimensions decompactify or none do, failing to single out three large dimensions dynamically. The problem appeared to be that string interaction rates fell off insufficiently rapidly with dimension number to suppress decompactification in d > 3.

This work re-examines these conclusions and suggests a mechanism where string dynamics favor three large dimensions through careful analysis of wound string collisions in dilute (non-equilibrium) regimes.

---

## Key Arguments and Derivations

### Dimension Counting and Intersection Probabilities

The classical BV argument is rooted in the observation that d-dimensional worldvolumes of one-dimensional objects (strings) generically intersect in at most d spacetime dimensions (or d-1 spatial dimensions). In 4D spacetime, two strings generically intersect at a point (0-dimensional intersection). In 5D spacetime (4 spatial dimensions), strings generically miss each other entirely.

This topological fact becomes manifest in the semiclassical (high-energy) limit where strings behave as nearly classical one-dimensional objects with small quantum thickness.

### Impact Parameter Representation

The authors develop an impact parameter representation for wound string scattering amplitudes, starting from the Virasoro-Shapiro amplitude for wound strings in d = D-1 large dimensions:

A(s,t) = Γ(-Λ² D-2) s² t(Λ'0 s/4) Λ'0 t/2 e^(-iπ Λ'0 t/4)

where s and t are Mandelstam variables. For wound strings with total energy E and wrapping radius R, the center-of-mass energy relates to R: s ~ R²/Λ'0.

The impact parameter amplitude A(s,b) is obtained by transforming in the transverse D-4 directions:

A(s,b) = Integral d^(D-4) q/(2π)^(D-4) e^(-iq·b) A(s,t)

For long wound strings (large R, large s), the imaginary part exhibits exponential suppression with dimension:

ImA(s,b) ~ (π Λ'0 ρ² 10 s)/(4(4π Y Λ'0)^(D/2-2)) * e^(-b²/4 Y Λ'0)

where Y = log(Λ'0 s/4) and b is the impact parameter in the D-4 transverse directions. The exponential factor e^(-b²/4 Y Λ'0) describes spreading of the wavefunction in transverse space.

Crucially, this amplitude is dimensionless for any D, but its physical interpretation changes:
- For D = 4 (3 spatial dimensions): amplitude is dimensionless and gives annihilation probability directly
- For D > 4: amplitude has units of (length)^(D-4), representing an effective cross-section in transverse directions

### String Interaction Rate in Dilute Regime

For a dilute gas of winding modes, the authors randomly select impact parameters on each re-collision time:

t_r ~ r / <v>

where r is the mean separation between winding modes and <v> is their mean velocity. This choice reflects the assumption that winding modes are distributed isotropically.

The interaction rate for winding mode annihilation is:

Γ_W = Γ_0 * (π Λ'0/4 ρ²_10 V^(1/2) [2π R/Λ'0]^2)² * (2π R/(π Δx²)^(1/2))^(D-4) * e^(-b²/Δx²)

where:
- Γ_0 is a baseline interaction rate
- V is the total spatial volume
- R = e^β is the radius of the wrapped dimension
- Δx² ~ 4 Y Λ'0 is the quantum thickness of the string

The key observation is the factor (2π R/(π Δx²)^(1/2))^(D-4), which produces a strong suppression when D > 4.

### Hagedorn and Radiation Phases

In the Hagedorn phase (high-density, near the critical temperature), equilibrium winding numbers are:

<W> = (1/12) sqrt(E/(π e^(-β)))
<K> = (1/12) sqrt(E/(π e^β))

where E is total energy and β is the scale factor (ln radius). As the universe expands and energy density drops, the equilibrium phase transitions to radiation-dominated when:

E / V_d ~ c_d T_H^(d+1)

In the radiation phase, equilibrium winding number vanishes (<W> = 0), but if the universe starts with residual winding modes, their subsequent evolution determines whether three or more dimensions grow.

### Coupled Dilaton-Gravity Equations

The evolution of the scale factors and dilaton couple through Einstein equations:

φ̈ = (1/2)(φ̇² + d β̇²)
β̈ = φ̇ β̇ + (1/8π²) e^φ P

where P is the pressure (times volume) in d dimensions. The Hamiltonian constraint enforces energy conservation:

E = (2π)² e^(-φ) (φ̇² - d β̇²)

The Boltzmann equations for winding (W) and Kaluza-Klein (K) modes are:

Ẇ = -Γ_W (W² - <W>²)
K̇ = -Γ_K (K² - <K>²)

---

## Key Results

1. **Exponential Suppression for d > 3**: The impact parameter analysis shows exponential suppression of wound string interaction rates for d > 3 spatial dimensions, with the suppression factor depending on the quantum thickness and dimension count:

   Rate(d=3) / Rate(d=4) ~ e^(Δx²/4)

   where Δx increases logarithmically with string length R.

2. **Hagedorn Trapping**: For large initial energy densities, the universe generically remains trapped in the Hagedorn phase with non-zero equilibrium winding numbers, preventing decompactification in any dimension count unless large fluctuations occur.

3. **Radiation Phase Decompactification**: When the universe fluctuates to the radiation phase (where equilibrium winding vanishes), residual winding modes either freeze out (for d > 3) or efficiently annihilate (for d = 3), directly realizing the BV mechanism.

4. **Dynamical Selection**: For d = 3, even in the radiation phase where winding has frozen out in higher dimensions, the enhanced interaction rates overcome coupling suppression, allowing winding mode annihilation. For d > 3, interactions freeze out at ~1% rates or lower.

5. **Phase Diagram**: The parameter space (initial scale β_0, initial dilaton φ_0) shows:
   - Upper left: All dimensions decompactify equally (no dimension selection)
   - Lower right (radiation regime): Only d = 3 decompactifies
   - Thin band: Transition region between Hagedorn and radiation phases

6. **Initial Conditions**: Decompactification requires large volume fluctuations from the self-dual radius (β_0 >> 0) plus energy distribution conducive to radiation phase entry, suggesting this mechanism operates only in a restricted parameter region.

---

## Impact and Legacy

This work provided the first convincing dynamical demonstration of the Brandenberger-Vafa mechanism within string theory, showing that three large dimensions can be singled out through string interaction physics rather than anthropic reasoning alone.

The impact parameter formalism became standard for analyzing high-energy string scattering in extra-dimensional contexts. The work motivated subsequent studies of brane gas cosmology and early-universe string dynamics in more realistic compactifications.

---

## Connection to Phonon-Exflation Framework

The phonon-exflation framework embeds the Standard Model in M4 x SU(3) compactified geometry. Greene-Kabat-Marnerides' work on why precisely three large dimensions emerge from string dynamics connects conceptually to phonon-exflation's prediction of dimensionality:

- **Dynamical Dimension Selection**: Just as the BV mechanism dynamically selects three large dimensions through string interactions, phonon-exflation's internal geometry dynamics may determine why M4 is large while SU(3) remains compact.

- **Winding and Topological Modes**: In phonon-exflation, the internal SU(3) compactification supports topological modes analogous to wound strings. These may play a role in stabilizing the internal structure against decompactification.

- **Early Universe Thermodynamics**: The framework's early universe behavior (Hagedorn-like density regimes, phase transitions) may exhibit similar dimension-selection dynamics to the string gas mechanism studied here.

- **Impact Parameter Dynamics**: If phonon-exflation involves scattering of internal modes (analogous to wound strings), the impact parameter analysis showing dimension-dependent suppression may apply to internal geometry interactions.

- **KK Mode Freezeout**: The freezeout of Kaluza-Klein modes in higher dimensions parallels the framework's KK tower structure. If phonon-exflation's dark matter and dark energy arise from KK mode dynamics, the suppression mechanisms here may constrain allowed KK spectra.

This work establishes that dynamical string interaction mechanisms can produce the observed four-dimensional spacetime structure from higher-dimensional theories—a principle directly relevant to phonon-exflation's compactification geometry.
