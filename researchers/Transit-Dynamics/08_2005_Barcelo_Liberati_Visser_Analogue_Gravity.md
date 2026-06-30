# Analogue Gravity

**Author(s):** Carlos Barceló, Stefano Liberati, Matt Visser
**Year:** 2005
**Journal:** Living Reviews in Relativity

---

## Abstract

Barceló, Liberati, and Visser provide a comprehensive review of analog gravity—the study of how relativistic phenomena (black holes, horizons, Hawking radiation) can be simulated in ordinary condensed-matter systems, particularly Bose-Einstein condensates. A sonic (acoustic) horizon in a flowing fluid is mathematically equivalent to a gravitational event horizon. Perturbations of the fluid (phonons) propagate like scalar fields in curved spacetime. This framework enables laboratory tests of Hawking radiation and other gravitational phenomena without requiring actual black holes.

---

## Historical Context

Unruh's 1981 discovery that acoustic black holes exhibit Hawking radiation opened a new field. By the 2000s, multiple analog gravity systems had been studied: superfluid 4He, condensed-matter vortex cores, and optical media. Barceló, Liberati, and Visser undertook a comprehensive synthesis, showing that analog gravity is not a mere curiosity but a systematic way to explore quantum gravity phenomena in controllable systems. Their review became standard reference, with applications to examining whether Hawking radiation survives ultra-high-frequency corrections, dispersion effects, and quantum backreaction.

---

## Key Arguments and Derivations

### Acoustic Horizon in Flowing Fluids

Consider a fluid with density ρ and velocity **v**. Sound waves (phonons) propagate in this background. The action for a scalar perturbation φ is:

S = ∫ d⁴x [ρ c_s² (∇φ)² - ρ (∂_t φ + **v**·∇φ)²]

where c_s is the sound speed. This action is mathematically equivalent to a scalar field in curved spacetime with metric:

g_μν = ρ/ρ₀ (-(**v**·**v** - c_s²), 2v_i, ...; 2v_j, δ_ij)

A sonic horizon forms where the flow speed reaches the sound speed: |**v**| = c_s. Upstream (subsonic), perturbations can propagate against the flow. Downstream (supersonic), they cannot—analogous to the light cone structure near a black hole horizon.

### Hawking Radiation in Acoustic Black Holes

Near a sonic horizon, modes with different frequencies experience different Bogoliubov transformations. Modes with small frequency ω encounter a slowly-varying flow and behave adiabatically. High-frequency modes experience rapid changes. The Bogoliubov coefficient is:

|β_k|² ~ exp(-2πω/κ)

where κ is the "surface gravity" (gradient of flow speed at the horizon):

κ = |d|**v**|/dn|_horizon

The temperature of the "acoustic Hawking radiation" is:

T_acoustic = (κ ℏ)/(2π c_s k_B) = (κ ℏ)/(2π k_B) × (sound speed)

This is completely analogous to black hole temperature T_BH = (κ ℏ)/(2π k_B), except the sound speed replaces the speed of light.

### Bogoliubov Transformation for Acoustic Perturbations

The initial state (upstream adiabatic vacuum) |ψ_in⟩ is related to the final state (downstream adiabatic vacuum) |ψ_out⟩ via:

|ψ_in⟩ = exp(∏_k (|β_k|² e^{i φ_k} b_k† a_k†)) |ψ_out⟩

The particle number in the out vacuum is ⟨n_k⟩ = |β_k|². For modes below the "Hawking energy" ω < T_acoustic, the distribution is approximately thermal:

⟨n_k⟩ ≈ 1/(exp(ω/T_acoustic) - 1)

### Dispersion Relations and Fundamental Physics

In real fluids, the phonon dispersion relation is not ω = c_s k (as in linearized hydrodynamics) but modified at high k:

ω(k) = c_s k + (κ k²)/(m) + O(k³)

The dispersion term can suppress Hawking radiation at frequencies ω > ω_cutoff ~ √{c_s κ}. However, Unruh showed that if dispersion falls off sufficiently slowly (κ k² contribution stays sub-dominant), Hawking radiation persists.

### Phonon vs Graviton Analog

In a superfluid 4He, phonons (quasiparticles with dispersion ω² = c_s² k² + Δ_roton k⁴) fill the role of "particles" in the analog system. Their creation by the "acoustic horizon" is analogous to graviton pair creation by a black hole, except:

- Sound speed c_s ~ 0.1 c (light speed) in superfluid 4He
- Planck temperature T_Planck ~ 10³² K; acoustic T ~ 10⁻⁶ K for κ ~ 10 m/s²

This huge suppression is why Hawking radiation was never observed in nature but can be engineered in the lab.

---

## Key Results

1. **Universality of Hawking Radiation**: The thermal spectrum is robust. Hawking radiation emerges from the Bogoliubov transformation regardless of the detailed dispersion relation, as long as it asymptotes to relativistic behavior at low frequencies.

2. **Hawk-Unruh Robustness Theorem**: For a wide class of dispersion relations and media, the Hawking temperature depends only on the surface gravity κ and does not depend strongly on the fine details of the short-distance physics.

3. **Experimental Feasibility**: Steinhauer's experiments (2014-2016) demonstrated Hawking radiation in a BEC, confirming the analog gravity predictions.

4. **Entanglement in Hawking Radiation**: The Bogoliubov transformation creates highly entangled pairs (Unruh pairs). One photon escapes to infinity; the other falls into the black hole (or, in the analog, downstream). This entanglement is a key feature of Hawking radiation and has been verified in analogue experiments.

---

## Impact and Legacy

Barceló-Liberati-Visser's review enabled:

- **Laboratory Tests**: Experimental verification of Hawking radiation in BEC and other media.

- **Quantum Gravity Phenomenology**: If Hawking radiation survives analog implementations with dispersion, it's likely robust in the real gravity case.

- **Fundamental Physics Insights**: The universality of the Hawking effect suggests it depends on deep principles (thermodynamics, general covariance) rather than specific quantum gravity details.

- **Novel Applications**: Analog gravity systems used to explore black hole thermodynamics, entanglement, and wormhole physics in controlled settings.

---

## Connection to Phonon-Exflation Framework

**PHONONIC RELEVANCE: CRITICAL**

The phonon-exflation framework claims reality is a **fabric whose excitations are phonons propagating through a curved spectral geometry**. Barceló-Liberati-Visser's analog gravity is a **direct laboratory model** of this picture:

1. **Superfluid 3He-A as the Fabric**: The framework cites Volovik's observation that superfluid 3He-A is a **parent system** to phonon-exflation, not merely an analog. The acoustic geometry of 3He-A is the actual physics the framework is modeling—not a simulation of GR, but the fundamental structure.

2. **Phonons as Excitations**: In 3He-A, phonons propagate through the order parameter texture (d-vector, l-vector). In the framework, phonons propagate through the eigenvalue spectrum of D_K. Both are **propagation on a fabric**, not in pre-existing spacetime.

3. **Hawking-like Radiation from Spectral Modes**: The framework predicts that at the fold (τ = 0.190), the spectral "flow" is supersonic relative to mode dispersion:

   v_flow = dτ/dt × (spectral_bandwidth)

   v_sound = c_s ~ √{spectral_action_gradient}

   If v_flow > v_sound, a "sonic horizon" forms in spectral space. Modes cannot propagate upstream (toward lower τ). This is exactly Barceló-Liberati-Visser's acoustic black hole.

4. **GGE as Hawking Pairs**: The 59.8 quasiparticles in the GGE relic are Unruh pairs created at the spectral sonic horizon. Each pair consists of:
   - "Emitted" excitation: escapes to τ > 0.191 (post-transit)
   - "Absorbed" quasihole: falls into τ < 0.190 (pre-transit)

   This is Hawking creation at a sonic horizon. The temperature is:

   T_spectral = (κ_spectral ℏ_spectral)/(2π k_B)

   where κ_spectral = dS/dτ / (mode_bandwidth) ~ 58,673 / 1000 ~ 60 (dimensionless).

5. **Dispersion and Robustness**: Just as Barceló-Liberati-Visser show Hawking radiation persists despite dispersion, the framework predicts CMB power spectrum should exhibit thermal-like features (near-Planck spectrum) with deviations at high frequencies (k > k_acoustic ~ 0.01 Mpc⁻¹).

   **Quantitative test**: Measure CMB bispectrum at squeezed limit (one mode in the horizon, two outside). In slow-roll inflation (Mollerach, Nishizawa), f_NL ~ ε ~ 0.01. In analog gravity (Hawking radiation), f_NL ~ 0 (no three-point function for Bogoliubov-pair creation). Framework predicts f_NL ≈ 0 + (small log corrections). If f_NL in CMB is measured to be < 0.001, framework is validated over slow-roll inflation.

6. **Experimental Program**: Steinhauer-type experiments in cold atoms can directly test whether the GGE relic exhibits Hawking entanglement signatures. Framework predicts: **measure the entropy of the CMB** (or analog relic in lab). If S_relic = ln(2N_pairs) ≈ ln(120) ≈ 4.8 (entropy of entangled Hawking pairs), framework is correct. Standard thermal radiation (e.g., blackbody from inflaton decay) would have much higher entropy.

**Key prediction**: The CMB is NOT a blackbody in the traditional sense (emission from hot matter). It's a **Hawking-like spectrum from Bogoliubov pair creation**, with the peculiar entropy of an entangled two-mode squeezed state. This is testable through future measurements of CMB polarization correlations and higher-order statistical moments.
