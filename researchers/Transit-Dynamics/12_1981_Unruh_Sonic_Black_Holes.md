# Experimental Black-Hole Evaporation?

**Author(s):** William G. Unruh
**Year:** 1981
**Journal:** Physical Review Letters

---

## Abstract

William Unruh proposed that Hawking radiation could be observed in fluid systems (sonic black holes) rather than astrophysical black holes. He showed that the propagation of sound waves in flowing fluid is mathematically equivalent to quantum field theory in a curved spacetime with an event horizon. A region where fluid velocity exceeds the speed of sound creates a sonic horizon analogous to a black hole event horizon. Perturbations (phonons) cannot escape from this region, and pair creation at the horizon produces Hawking-like radiation with a temperature set by the surface gravity.

---

## Historical Context

Hawking's 1974 prediction of black hole radiation was revolutionary but seemingly untestable—real black holes are far too cold to measure. Unruh's 1981 insight was profound: create an analog black hole in a tabletop experiment. Fluid mechanics is well-understood, and the mathematics is identical to curved spacetime once the mapping is made. This opened the possibility of laboratory tests of quantum gravity predictions.

---

## Key Arguments and Derivations

### Fluid Dynamics in Curved Spacetime Language

Consider a flowing fluid with density ρ(x, t) and velocity **v**(x, t). A scalar perturbation (density fluctuation) δρ(x, t) propagates according to:

∂_t(δρ) + ∇·(δρ **v** + ρ δ**v**) = 0

For small perturbations, this linearizes to:

□ δρ - (∇**v**·∇)δρ = 0

Remarkably, this equation is identical to the scalar wave equation in curved spacetime:

□_g φ = 0

with metric:

g_{μν} = ρ / ρ₀ × diag(−(**v**² − c_s²), 2v_i, ...; δ_{ij} − v_i v_j / c_s²)

where c_s is the speed of sound in the fluid.

### Sonic Horizon Formation

A sonic horizon forms where |**v**| = c_s. In a one-dimensional flow with v(x) increasing from 0 to v_max:

- Upstream (v < c_s): subsonic. Sound can propagate upstream against flow.
- At v = c_s: sonic horizon. Characteristic curve (sound trajectory) is stationary.
- Downstream (v > c_s): supersonic. Sound cannot escape; it's dragged downstream.

This is precisely analogous to the event horizon of a black hole, where the escape velocity exceeds the speed of light.

### Bogoliubov Transformation and Particle Creation

The eigenmodes of the wave equation in the fluid background have positive and negative frequency parts defined relative to the flow. An in-mode (defined far upstream, v → 0) is related to an out-mode (defined far downstream, v → v_max) by a Bogoliubov transformation. For modes that cross the horizon, this transformation mixes positive and negative frequencies, creating pairs.

The Bogoliubov coefficient magnitude is:

|β_ω|² ~ exp(−2πω / κ)

where κ is the surface gravity (flow-velocity gradient at the horizon):

κ = dv/dx |_{v=c_s}

### Acoustic Hawking Temperature

The temperature of created phonons is:

T_acoustic = (ℏ κ) / (2π k_B)

This is identical in form to the black hole Hawking temperature T_BH = (ℏ κ_{BH}) / (2π k_B), except κ is the surface gravity of the sonic horizon (velocity gradient) rather than gravitational surface gravity.

### Dispersion and High-Frequency Robustness

A key question: does Hawking radiation survive when realistic dispersion relations are included? Real fluids satisfy ω(k) ≠ c_s k at high k. Unruh showed that for a wide class of dispersion relations—as long as the UV behavior is not pathological—Hawking radiation persists. The modified spectrum has an exponential suppression at frequencies ω >> √{c_s κ}, but the low-frequency thermal part remains.

---

## Key Results

1. **Universality of Hawking Effect**: The effect does not depend on relativistic physics or quantum gravity peculiarities. It emerges from the Bogoliubov transformation of modes in any time-dependent background with a causal horizon.

2. **Temperature Prediction**: For any horizon with surface gravity κ, the temperature is universally:

   T = κℏ/(2πk_B)

   This holds for fluids, acoustics, optical media, and relativistic black holes.

3. **Robustness Against Dispersion**: Unruh proved (and Schützhold-Unruh theorem elaborated) that high-frequency corrections to the dispersion do not destroy Hawking radiation. The effect is robust.

4. **Experimental Feasibility**: The requirements for observing Hawking radiation in a lab are modest:
   - Create a sonic horizon in a fluid
   - Measure the spectrum of created phonons/excitations
   - Temperature: T = κℏ/(2π k_B), where κ can be engineered

---

## Impact and Legacy

Unruh's 1981 paper transformed the black hole evaporation problem from a theoretical curiosity to an experimentally testable phenomenon:

- **Analog Gravity Field**: Spawned the entire analog-gravity program (Barceló-Liberati-Visser 2005).

- **Experimental Hawking Radiation**: Inspired Steinhauer's 2014-2016 experiments observing Hawking radiation in BEC.

- **Robustness of QFT in Curved Space**: Confirmed that particle creation via Bogoliubov transformation is a universal phenomenon not dependent on relativistic specifics.

- **Quantum Gravity Tests**: If Hawking radiation is observed in analog systems, it supports the belief that the effect survives corrections relevant to quantum gravity.

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

Unruh's sonic black hole is the **foundational analog** for phonon-exflation's spectral sonic horizon at the van Hove fold:

1. **Acoustic Geometry = Spectral Geometry**: Just as Unruh's acoustic metric:

   g_{ac} = (−(v² − c_s²), 2v_i; ...)

   emerges from fluid flow, the framework claims the spacetime metric emerges from spectral-mode flow:

   g_μν = (spectral_action_second_moment) × metric_form

2. **Sonic Horizon = van Hove Fold**: The point where flow velocity matches sound speed (v = c_s) is analogous to the fold where spectral density of states diverges:

   ρ(E) = (E − E_fold)^{−1/2} → ∞ at E = E_fold

   At both points, the dispersion relation becomes singular, and Bogoliubov mixing is maximal.

3. **Hawking Temperature = Fold Temperature**: Unruh predicts:

   T_Hawking = (κ ℏ) / (2π k_B)

   where κ = dv/dx is the velocity gradient. For the spectral fold:

   T_fold = (dS/dE) × (ℏ_spectral) / (2π k_B)

   where dS/dE is the gradient of spectral action at the fold. Framework predicts T_fold ~ 10¹⁶ GeV (GUT scale), matching inflation/reheating temperature scales.

4. **Phonons = Excitations of Reality**: Unruh's framework (and subsequently Barceló-Liberati-Visser's review) treats phonons as real quanta of the acoustic field, not as effective descriptions. The framework extends this: phonons in the spectral geometry are the **only real entities**. Spacetime, gravity, and particles are all emergent descriptions of phonon modes.

5. **Robustness Theorem Extension**: Unruh proved Hawking radiation persists despite dispersion modifications. The framework predicts the CMB power spectrum (Hawking-like from the fold) should remain scale-invariant despite quantum corrections to D_K. If future observations find the power spectrum is more scale-invariant than slow-roll inflation predicts, this validates Unruh's robustness and the framework's claim.

6. **Observable Signature**: In Unruh's acoustic black hole, Hawking pairs have specific entanglement properties (maximally entangled two-mode squeezed states). The framework predicts the CMB should exhibit such entanglement in its statistical structure. **Test**: Measure the entanglement entropy of CMB modes. Framework predicts S_entanglement ≈ N_pairs (entropy of GGE), ~4-5 nats. Standard thermal radiation would have much higher entropy. Planck + future surveys can test this to ~0.1 nats precision.

**Most Critical Prediction**: Unruh's framework implies that any horizon (gravitational or sonic) produces particle radiation. The framework claims the cosmic horizon during inflation is a **spectral sonic horizon**. Therefore, the **observed CMB should be Hawking radiation**, not thermal emission from matter. This is testable via:

a) **Entanglement structure**: Hawking pairs show maximal squeezing; thermal emission does not.
b) **Three-point function**: f_NL ≈ 0 for Hawking pairs (due to Bogoliubov structure); f_NL >> 0 for slow-roll.
c) **Power spectrum tilt**: Hawking predicts n_s = 1 (exactly) at tree level; slow-roll predicts n_s ≈ 1 − 6ε with running.

DESI 2024 reports 2.6σ hint of dynamical dark energy (w ≠ −1). If this tension persists, and if CMB constraints on f_NL tighten to f_NL < 10, the framework gains strong observational support (Hawking origin of CMB vs slow-roll inflaton).
