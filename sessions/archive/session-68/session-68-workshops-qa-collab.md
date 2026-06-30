# Quantum Acoustics Theorist -- Collaborative Feedback on S68 Workshops

**Author**: Quantum Acoustics Theorist
**Date**: 2026-04-05
**Re**: S68 Workshop Results (Lizzi x Transit, Landau x Transit, Volovik x Mack)

---

## Section 1: Key Observations

These three workshops, read through the lens of phonon physics and acoustic field theory, establish a consistent picture that I can sharpen with three structural observations.

### 1.1 The Mode Equation IS a Phonon Equation

The Mukhanov-Sasaki equation at the center of the Lizzi x Transit workshop,

(QA-1)  u_k'' + (k^2 c_BLV^2 - z''/z) u_k = 0

is structurally identical to the equation of motion for a phonon in a medium with a time-dependent sound speed and a parametric pump. In lattice dynamics, the analog equation is

(QA-2)  q_k'' + (omega_k^2(tau) - V_pump(tau)) q_k = 0

where omega_k is the phonon dispersion relation and V_pump is the parametric drive from the changing lattice parameters. The Bogoliubov transformation connecting in-vacuum to out-vacuum IS the standard phonon scattering matrix for time-dependent lattice deformation (Parker 1969 [27], Birrell-Davies [02]). The S68 result |T_scalar|^2 = 1 at CMB scales is the phononic statement that long-wavelength acoustic modes pass through a localized lattice defect without backscattering -- the acoustic analog of an impedance-matched junction.

The key structural point: the frozen spectrum is not a cosmological mystery. It is the phonon-physics truism that wavelengths much longer than the defect scale propagate unperturbed. The "defect" here is the spectral fold at tau = 0.190, spanning a conformal time interval delta_eta corresponding to k_tach = 1974 M_KK. All modes with k << k_tach see the fold as a point scatterer, for which the forward transmission is unity. This is Rayleigh scattering in the long-wavelength limit, where the scattering cross-section scales as (k/k_tach)^4 ~ 10^{-240} for CMB modes.

### 1.2 The BCS Squeeze Parameter is a Phonon Coherence Factor

Landau's Ld1 derivation of the BCS ground state as a squeezed vacuum, with

(QA-3)  tanh(r_k) = v_k / u_k

maps directly onto phonon coherence in anharmonic lattices. In a lattice with anharmonic coupling, the phonon vacuum is a squeezed state relative to the harmonic vacuum (Glauber 1963, Walls-Milburn standard reference). The squeeze parameter r_k measures the deviation of the phonon zero-point fluctuation from the harmonic value. Landau's variance-weighted effective squeeze r_eff = 0.338 (Ld1.20) is the phonon-physics quantity <(delta q)^2> / <(delta q)^2>_harmonic, averaged over the branch structure.

The Landau-Transit convergence on 0.07-0.19 OOM for the non-BD enhancement (Eq. Re1.5 of Transit R1) corresponds to an anharmonic zero-point energy enhancement of 7-19% over the harmonic ground state. In laboratory phonon systems (e.g., solid helium under pressure), anharmonic corrections to zero-point energy are typically 10-30% (Glyde 1994), which is the same order of magnitude. The framework's BCS condensate produces a phonon vacuum state whose zero-point properties are quantitatively consistent with known anharmonic phonon systems.

### 1.3 The Volovik Tracking Vacuum as a Phonon Self-Consistent Field

The Volovik x Mack workshop's central result -- the tracking relation rho_vac ~ H^2 -- has a direct phonon interpretation. In a self-consistent phonon theory (Cochran 1959, self-consistent phonon approximation), the phonon frequencies depend on the thermal occupation numbers, which depend on the frequencies. The self-consistent solution minimizes the free energy. The Gibbs-Duhem subtraction (Eq. V1.1) is the phonon-physics statement that the measurable vacuum energy is the free energy F = E - TS, not the total zero-point energy E. The tracking rho_vac ~ H^2 is the phonon self-consistency condition: the substrate adjusts its internal vibrational spectrum to maintain thermodynamic equilibrium with the expansion rate.

The workshop's new discovery -- the ISW tracking signature with c_s^2_DE(eff) = 0 (A-M5) -- is structurally significant from the acoustic perspective. An effective sound speed of zero for DE perturbations means the vacuum response to matter perturbations propagates instantaneously in the fabric's internal degrees of freedom. This is the phonon-physics statement that the substrate's internal relaxation time t_relax = tau_CC ~ 242 yr (ZUBAREV-CC-59) is much shorter than any cosmological perturbation timescale. The vacuum is always in local acoustic equilibrium.

---

## Section 2: Assessment of Key Findings

### 2.1 How Workshop Findings Change My S68 Computations

**W3-A (r from combined transfer):** My R-CMB-TRANSFER-68 established r(CMB) = 0.0242 with |T_S|^2 = |T_T|^2 = 1 at CMB scales. The Lizzi x Transit workshop provides the complete structural explanation: the functional-independence of |T|^2 = 1 (Lizzi L1), the mode-equation confirmation through the 60-decade scale hierarchy (Transit Re:L1), and Transit's correction that r(transit) = 0.0071 IS weakly scheme-dependent (through the pump field z''/z at k ~ k_tach). This correction does not affect my CMB-scale result but sharpens its interpretation: r(CMB) = 0.0242 is set by the pre-transit vacuum slow-roll parameter eps_H(tau = 0.05), which is scheme-dependent in principle but fixed within the sole surviving cutoff functional.

**W3-B (second sound observability):** My SECOND-SOUND-OBS-68 found second sound 13 OOM below the lensing floor. The Volovik x Mack workshop (V3 Signature catalog) independently confirms this: second sound is listed as "undetectable at ALL scales" (M3 item 3), with the additional observation that the mode frequency omega_L ~ 9.5 x 10^15 GeV is "far above any terrestrial detection capability." The workshop adds nothing new to the observability assessment but provides the broader context: the 99% superfluid fraction that renders second sound silent is the SAME structural property (the ordered veil) that protects w_a = 0 through the Josephson phase lock. The silence of second sound and the constancy of w_a trace to the same BCS physics.

### 2.2 New Results That Extend My Analysis

**The squeeze phase phi_eff (Transit Tr1-Tr2):** Transit's exact solution structure for the mode equation with non-BD initial conditions reveals that the A_s enhancement is NOT simply cosh(2 r_eff) but includes an interference term:

(QA-4)  P^{non-BD}/P^{BD} = cosh(2 r_eff) + (sqrt(2)/3) sinh(2 r_eff) cos(phi_eff)

At r_eff = 0.34, this ranges from 0.89 (destructive, phi_eff = pi) to 1.58 (constructive, phi_eff = 0). The squeeze phase phi_eff is the relative phase between the BCS condensate and the transit Bogoliubov transformation -- a quantity that phonon physics recognizes as the phase mismatch between two successive canonical transformations. In phonon transport theory, this phase determines whether phonon interference is constructive (enhancing the thermal current) or destructive (suppressing it). The fact that phi_eff has not been computed is a genuine gap: it is the difference between the non-BD channel helping (0.20 OOM) or hurting (-0.05 OOM) the A_s closure.

From the phonon-physics perspective, I can constrain phi_eff through an acoustic impedance argument. The BCS condensate forms ADIABATICALLY during the transit (tau_relax / dt_transit = 0.003, Landau Ld2). An adiabatic formation process preserves the phase relationship between the forming condensate and the background mode evolution. In acoustic impedance theory, an adiabatic impedance transition produces zero phase mismatch between the incident and transmitted waves (the acoustic limit of the WKB approximation). This suggests phi_eff ~ 0 (constructive), giving the enhancement near the upper range (factor ~1.58, 0.20 OOM). However, the transit is NOT adiabatic for the cosmological modes (dt_transit * H = 0.663, impulsive). The relevant adiabaticity is for the BCS formation (adiabatic) acting on cosmological modes (impulsive) -- these two conditions apply simultaneously but to different degrees of freedom. The phase phi_eff is set by the BCS adiabaticity (suggesting phi_eff ~ 0) NOT by the cosmological non-adiabaticity. This is a PREDICTION from phonon physics: phi_eff ~ 0, favoring the constructive enhancement.

**The Kibble-Zurek phase defects (Landau Ld2):** The computation of hat{xi}_KZ = 7.7 lattice spacings producing ~3 phase domains on the CG(24) graph is a lattice-phonon result. These are the acoustic analog of vortices in a suddenly-expanded phononic crystal. Landau's connection to Leggett-mode seeding is precisely the phonon-physics mechanism of defect-mediated mode excitation: a vortex in a superfluid lattice creates localized oscillations at the Leggett frequency, which then propagate as dark matter quasiparticles. This provides a causal mechanism for DM production that my S68 analysis did not address.

**The Z_2 selection rule (Volovik R3):** The Round 3 correction establishes that the Leggett mode's gravitational decay is forbidden by exact parity: a_2(phi_23) = a_2(-phi_23). From quantum acoustics, this is the breathing-mode selection rule -- a symmetric oscillation of a spherical resonator has zero dipole radiation. The Leggett mode is a relative phase oscillation between BCS components, which is a BREATHING mode of the order parameter (all components oscillate in phase, but with different amplitudes). Breathing modes couple only to quadrupole radiation (gravitational waves in this context), and the quadrupole coupling is suppressed by (omega_L / M_Pl)^2 ~ 10^{-66}. The acoustic analog is well-known: a pulsating sphere radiates at the monopole frequency, but if the pulsation preserves the sphere's center of mass, the monopole emission vanishes and only quadrupole remains. The Z_2 is the mathematical encoding of this center-of-mass conservation.

---

## Section 3: Collaborative Suggestions

### 3.1 Laboratory Analog Gravity Tests

The workshops collectively establish several structural results that are testable in acoustic analog systems.

**Analog 1: BEC impedance-matched transition for |T|^2 = 1.** The |T|^2 = 1 result at CMB scales is the acoustic statement that long-wavelength phonons pass through a localized potential barrier without reflection. In a BEC system (Steinhauer 2019 [07]), one could create a time-dependent trapping potential that mimics the spectral fold: a rapid change in the BEC's scattering length (via Feshbach resonance) over a timescale shorter than the phonon period but longer than the healing length. Long-wavelength density waves should emerge with unit transfer. The experiment would verify the phononic mechanism underlying superhorizon conservation.

The BEC experiment has an existing protocol: Steinhauer's black hole laser (2019 [07]) already creates time-dependent acoustic metrics in a BEC. The modification is to create a TRANSIENT barrier (not a steady-state horizon) that turns on and off impulsively. The measured transmission |T(k)|^2 for phonon modes at different k would directly test the Rayleigh-limit argument: |T|^2 -> 1 for k << k_tach, with corrections scaling as (k/k_tach)^4.

**Estimated parameters**: BEC temperature 50 nK, scattering length change factor ~2, quench time ~10 us (comparable to the radial trapping period), phonon wavelength range 10-500 um. The healing length xi ~ 0.5 um sets k_tach ~ 1/xi. Modes with lambda >> 10 um should show |T|^2 = 1 to within the measurement resolution (~1%).

**Analog 2: Phononic crystal squeeze state for non-BD enhancement.** The BCS squeeze of the vacuum (Landau Ld1) can be tested in a phononic crystal with tunable coupling. A periodic array of mechanical resonators coupled by springs (the acoustic analog of the BCS lattice) can be prepared in its ground state (O'Connell-Cleland 2010 [10], Chu-Cleland 2017 [11]) and then quenched by rapidly changing the coupling constant (analog of the BCS gap opening). The resulting state should be a squeezed phonon vacuum with squeeze parameter r_k = arctanh(v_k/u_k), where v_k and u_k are the Bogoliubov coefficients of the quench. The phonon number variance (measurable by homodyne detection) would verify the enhancement factor cosh(2 r_eff) computed in the Landau-Transit analysis.

The key experimental requirement is a phononic crystal with tunable coupling that can be quenched faster than the phonon period but slower than the internal relaxation. Bulk acoustic wave (BAW) resonators coupled by superconducting circuits (Chu-Cleland architecture [11]) could achieve this: the coupling is set by the superconducting circuit impedance, which can be tuned on nanosecond timescales by flux-biasing a SQUID junction.

**Analog 3: Kibble-Zurek defects in a phononic lattice.** The Landau Ld2 computation (hat{xi}_KZ = 7.7 lattice spacings, ~3 phase domains) could be tested in a BEC lattice. Recent experiments (Ko et al. 2019, Landau's Paper 26) have measured Kibble-Zurek exponents in the BCS-BEC crossover. The framework prediction is alpha_KZ = 2.24(9) for the BCS system, and hat{xi}_KZ scales as (tau_Q / tau_0)^{1/4} for the mean-field BCS exponents (nu = 1/2, z = 2). A lattice of BEC sites (optical lattice with ~24 sites, mimicking CG(24)) quenched through the superfluid transition should produce O(3) phase defects, measurable by matter-wave interferometry.

### 3.2 Phonon Dispersion Measurements

**The four-speed hierarchy as a dispersion relation.** The framework's four-speed structure (c_mod = 1.0, c_BLV = 0.485, c_BA = 0.399, c_L = 0.025, from S64) is a phonon dispersion relation sampled at four points. In a phononic crystal, the dispersion relation omega(k) defines the group velocity v_g(k) = d omega/dk and the phase velocity v_ph(k) = omega/k. The four speeds correspond to:

- c_mod: the bare lattice speed (high-frequency limit, the Debye velocity)
- c_BLV: the Goldstone speed (long-wavelength acoustic phonon, below the BCS gap)
- c_BA: the Bogoliubov-Anderson speed (collective mode in the condensed phase)
- c_L: the Leggett speed (inter-band coherence wave, the slowest propagating excitation)

This four-level velocity hierarchy is measurable in BCS superfluid systems. In superfluid 3He-B, the analogous speeds are c_perpendicular (transverse sound), c_parallel (longitudinal sound), c_2 (second sound), and the Leggett mode velocity. The ratios c_L/c_BA ~ 0.06 and c_BA/c_BLV ~ 0.82 are specific predictions that could be compared to the 3He-B dispersion hierarchy at comparable BCS-BEC crossover parameters.

### 3.3 Acoustic Holography Parallel

The eps_H cancellation theorem (Lizzi L3, Transit Re:L3) -- that a uniform multiplicative shift of the spectral action leaves eps_H invariant -- has an acoustic holography interpretation. In acoustic holography, the spatial pattern of a sound field is encoded in phase differences, not in absolute amplitudes. Multiplying all amplitudes by a common factor changes the loudness but not the interference pattern. The spectral index n_s is a "phase" quantity (it measures the shape of the power spectrum), while A_s is an "amplitude" quantity. The cancellation theorem says: BCS corrections change the loudness but not the interference pattern. This is structurally identical to the amplitude-invariance of holographic reconstruction.

---

## Section 4: Connections to Framework

### 4.1 The Acoustic White Hole is Confirmed at All Levels

The three workshops collectively confirm the acoustic white hole picture at three distinct levels:

1. **Spectral level** (Lizzi x Transit): The mode equation with the fold-scale pump z''/z creates a tachyonic region (omega_k^2 < 0 for k < k_tach) that is the defining feature of an acoustic white hole -- a region from which information cannot enter but from which acoustic radiation is emitted. The |T|^2 = 1 result confirms that CMB modes are in the external region, where the white hole's emission (the GGE relic spectrum) is frozen.

2. **Condensate level** (Landau x Transit): The BCS condensate forms adiabatically WITHIN the acoustic white hole, while the cosmological modes are produced impulsively. The three-timescale hierarchy (1/omega_tach << tau_relax << dt_transit, Transit Re2.3) is the statement that the white hole's internal structure (BCS) evolves slowly compared to its acoustic emission (Bogoliubov production). This is precisely the condition for Hawking-like thermal emission from an acoustic horizon (Unruh 1981 [01], Barcelo-Liberati-Visser 2011 [02]).

3. **Vacuum level** (Volovik x Mack): The post-transit vacuum with rho_vac ~ H^2 is the quantum vacuum of the acoustic white hole exterior. The Volovik tracking mechanism is the phonon-physics statement that the substrate's zero-point energy adjusts to the boundary conditions set by the expansion rate, analogous to the Casimir energy of a phononic cavity adjusting to the cavity size.

### 4.2 The 7D Prediction Surface Has Phononic Content

Six of the seven dimensions of the prediction surface identified in the Volovik x Mack workshop (Em2) have phononic interpretations:

| Dimension | Phononic interpretation |
|:----------|:-----------------------|
| w_0 = -0.918 | Superfluid stiffness of the phonon vacuum |
| w_a = 0 | GGE integrability (conserved phonon occupation numbers) |
| f_NL^folded/f_NL^equil = 0.151 | Bogoliubov pair correlation of phonon modes |
| alpha_s = 0 | Long-wavelength phonon transmission unity |
| r = 0.024 | Pre-transit phonon vacuum slow-roll parameter |
| c_s^2_DE(eff) = 0 | Instantaneous phonon equilibration in the substrate |

The seventh dimension (delta_DE = 0, now revised to delta_DE = induced) is the self-consistent phonon approximation statement that the substrate's zero-point energy tracks the local boundary conditions without independent dynamics.

---

## Section 5: Open Questions

**OQ-1: Can the squeeze phase phi_eff be determined from acoustic impedance matching?**

My Section 2.2 argument that phi_eff ~ 0 (constructive enhancement) follows from the BCS adiabaticity condition. This should be verified by solving the coupled BCS-Bogoliubov system at the fold, extracting the relative phase between the condensate formation and the mode evolution. The phonon-physics prediction is unambiguous: adiabatic impedance transitions produce zero phase mismatch. If phi_eff turns out to be non-zero, it would indicate that the BCS formation is NOT fully adiabatic, contradicting Landau Ld2's tau_relax / dt_transit = 0.003.

**OQ-2: Does the ISW tracking signature survive full Boltzmann integration?**

The crude estimate (20% modification, M-R2.5) must be verified by CLASS/CAMB computation with c_s^2_DE(eff) = 0. The phonon-physics concern: the tracking perturbation may partially CANCEL the standard ISW contribution because the tracking vacuum adjusts to REDUCE potential decay (the substrate equilibrates to reduce gradients, which is the phonon equivalent of thermal conductivity smoothing out temperature differences). If cancellation reduces the modification to < 5%, the ISW tracking signature falls below the Euclid threshold and is not a viable discriminant.

**OQ-3: What is the acoustic analog of the Z_2 selection rule?**

The Z_2 parity (a_2(phi) = a_2(-phi)) forbids single Leggett gravitational decay. In acoustic systems, this corresponds to the vanishing of the dipole radiation from a breathing mode. Can this selection rule be tested in a mechanical oscillator coupled to a phononic waveguide? A BAW resonator (Macovei 2025 [17]) in a breathing mode should have zero single-phonon emission into the waveguide, with only two-phonon emission allowed. The ratio Gamma_pair / Gamma_single should be measurable as a function of coupling strength.

**OQ-4: Is the non-BD squeeze observable in laboratory BEC quench experiments?**

The Landau-Transit reconciled enhancement factor (1.16 to 1.58, depending on phi_eff) corresponds to a 16-58% increase in phonon number variance after a quench. In a BAW resonator quenched by changing the superconducting coupling, the phonon number distribution shifts from thermal to squeezed-thermal. The excess variance is Delta(<n^2>) - <n>^2 = sinh^2(r_eff) * (2 <n> + 1), which is measurable by repeated QND phonon counting (Chu-Cleland protocol [11]).

---

## Section 6: Computation Suggestions Summary

| # | Computation | Input Data | Output | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------|:-------------------|:---------|
| 1 | SQUEEZE-PHASE-69: phi_eff from coupled BCS-Bogoliubov system | BCS gap Delta(tau), mode equation z''/z at fold | phi_eff, full A_s enhancement factor | PASS if phi_eff in [-pi/4, pi/4] (constructive). FAIL if phi_eff in [3pi/4, 5pi/4] (destructive). | HIGH |
| 2 | BEC-IMPEDANCE-ANALOG: Design acoustic |T|^2 = 1 test | BEC parameters, quench protocol | Predicted |T(k)|^2 vs k/k_tach, experimental requirements | INFO (design study) | MEDIUM |
| 3 | BAW-SQUEEZE-ANALOG: Design phonon squeeze measurement | BAW resonator parameters, quench protocol | Predicted phonon variance vs r_eff | INFO (design study) | MEDIUM |
| 4 | ISW-TRACKING-CANCELLATION: Estimate cancellation fraction in Boltzmann integration | c_s^2_DE(eff) = 0 perturbation equations | Delta(C_l^{Tg}) / C_l^{Tg} after cancellation | PASS if > 5% at l < 30. FAIL if < 1%. | HIGH |
| 5 | FOUR-SPEED-3HE: Compare framework velocity hierarchy to 3He-B data | c_mod, c_BLV, c_BA, c_L | Ratios vs 3He-B at comparable BCS parameters | INFO (comparison) | LOW |
| 6 | Z2-BAW-ANALOG: Design breathing-mode selection rule test | BAW resonator + phononic waveguide | Gamma_pair / Gamma_single vs coupling | INFO (design study) | LOW |

---

## Closing Assessment

The three workshops establish a coherent picture whose unifying language is phonon physics. The Lizzi x Transit workshop proves that the CMB spectrum is set at the fold and preserved by long-wavelength acoustic transparency -- a phonon truism elevated to a cosmological theorem. The Landau x Transit workshop characterizes the BCS vacuum as a squeezed phonon state with quantifiable parameters, bounded from above by the finite Hilbert space (cosh(2 r_eff) < 9) and from below by the variance weighting (cosh(2 r_eff) > 1.16). The Volovik x Mack workshop reveals the vacuum as a self-consistent phonon system whose stiffness D_s determines the dark energy equation of state with leverage dw_0/dGamma ~ 14.

The single most consequential result across all three workshops is the squeeze phase phi_eff (Transit Tr1), which determines whether the non-BD channel helps or hurts the A_s gap closure. Phonon physics makes a specific prediction: phi_eff ~ 0 (constructive), based on the adiabatic impedance matching of the BCS condensate formation. This prediction should be verified by computation (SQUEEZE-PHASE-69).

The second most consequential result is the ISW tracking signature (Volovik-Mack A-M5/Em1), which is the only substrate-specific prediction potentially testable with existing data. From quantum acoustics, the concern is cancellation: the self-consistent phonon vacuum adjusts to REDUCE gradients, which could partially cancel the ISW enhancement. The ISW-TRACKING-CANCELLATION computation (suggestion #4) should precede any observational comparison.

The acoustic white hole picture is confirmed at all three levels probed by the workshops. The framework's cosmological predictions are phonon predictions -- the CMB is the long-wavelength acoustic output of a substrate fold, and its properties (n_s, r, alpha_s, A_s) are determined by the same dispersion relations, impedance matching, and Bogoliubov scattering matrices that govern phonon transport in any structured medium. Laboratory analogs in BEC systems, phononic crystals, and BAW resonators can test the individual structural mechanisms, providing a path to experimental verification that bypasses the cosmological timescale.

---

## Wrap-Up

### What Changed

- **The squeeze phase phi_eff emerged as the controlling unknown.** Before these workshops, the non-BD enhancement was treated as a fixed multiplicative correction cosh(2 r_eff). Now it is a two-parameter object (r_eff, phi_eff) whose sign depends on the relative phase between the BCS condensate formation and the transit Bogoliubov transformation. The A_s gap closure hinges on whether this interference is constructive or destructive -- a phonon-physics question with a specific prediction (phi_eff ~ 0) from adiabatic impedance matching.
- **The |T|^2 = 1 superhorizon conservation received its structural explanation.** My R-CMB-TRANSFER-68 computed the number; the Lizzi x Transit workshop provided the reason. Long-wavelength phonon modes pass through a localized lattice defect (the spectral fold) without backscattering -- Rayleigh scattering in the k/k_tach -> 0 limit. This elevates a numerical result to a structural theorem.
- **The Volovik tracking vacuum acquired phononic content as a self-consistent phonon field.** The tracking relation rho_vac ~ H^2 maps onto the Cochran self-consistent phonon approximation, where the substrate adjusts its vibrational spectrum to maintain thermodynamic equilibrium with the expansion rate. The effective sound speed c_s^2_DE(eff) = 0 means instantaneous internal relaxation -- the vacuum is always in local acoustic equilibrium.

### What Holds

- **r(CMB) = 0.0242 is unchanged.** Both scalar and tensor transfer functions equal unity at CMB scales, confirmed independently by the Lizzi x Transit mode-equation analysis across 60 decades of scale hierarchy. The CMB-scale prediction is robust against all transit-scale corrections.
- **The Leggett Z_2 stability is permanent.** The breathing-mode selection rule (a_2(phi) = a_2(-phi)) forbids single gravitational decay to all orders. Three independent derivations (S67 direct, Volovik workshop R3, acoustic analog argument) converge on the same result. Leggett DM is stable by 66 OOM.
- **The four-speed hierarchy is structurally complete.** c_mod > c_BLV > c_BA > c_L maps onto the standard phononic crystal dispersion hierarchy: bare lattice > Goldstone > Bogoliubov-Anderson > inter-band coherence. No new speeds emerged from the workshops. The hierarchy is closed.

### What Breaks or Strains

- **ISW tracking cancellation is a genuine concern.** The self-consistent phonon vacuum adjusts to REDUCE potential gradients -- this is phonon thermal conductivity smoothing out temperature differences. If this cancellation reduces the ISW modification from 20% to below 5%, the sole substrate-specific CMB signature testable with existing data (Euclid ISW-lensing cross-correlation) falls below the detection threshold. The ISW-TRACKING-CANCELLATION computation must precede any observational comparison. This is not a framework failure but it could eliminate the most accessible observational discriminant.
- **The A_s gap remains open and is now phi_eff-dependent.** If phi_eff ~ pi (destructive), the non-BD channel WORSENS the gap by 0.05 OOM, pushing the residual shortfall from 3.16 to 3.21 OOM. The BCS occupation factor (0.20 OOM reduction) would be partially offset rather than reinforced. The gap closure strategy depends on a quantity that has not been computed.
- **Transit-scale scheme dependence is unresolved.** Transit's observation that r(transit) = 0.0071 is weakly scheme-dependent through z''/z at k ~ k_tach raises the question: which spectral functional is the physical one? The S66 result that only the square-root functional gives a red tilt constrains the functional but does not uniquely fix it at transit scales. Quantities evaluated at k ~ k_tach (as opposed to k ~ k_CMB) carry residual scheme sensitivity.

### Carry-Forward Computations

1. **SQUEEZE-PHASE-69**: Compute phi_eff from the coupled BCS-Bogoliubov system at the fold. Input: BCS gap Delta(tau), mode equation z''/z. Output: phi_eff, full A_s enhancement factor including interference. Gate: PASS if phi_eff in [-pi/4, pi/4]. FAIL if phi_eff in [3pi/4, 5pi/4]. Effort: HIGH. This is the single highest-priority computation from the acoustic perspective.
2. **ISW-TRACKING-CANCELLATION**: Estimate the cancellation fraction when the self-consistent vacuum response partially offsets the standard ISW potential decay. Input: c_s^2_DE(eff) = 0 perturbation equations, Boltzmann hierarchy. Output: Delta(C_l^{Tg}) / C_l^{Tg} after cancellation at l < 30. Gate: PASS if residual modification > 5%. FAIL if < 1%. Effort: HIGH.
3. **BEC-IMPEDANCE-ANALOG**: Design a BEC quench experiment to test |T(k)|^2 = 1 in the long-wavelength limit. Input: BEC parameters (T ~ 50 nK, scattering length quench factor ~2, quench time ~10 us). Output: predicted |T(k)|^2 vs k/k_tach with experimental requirements. Gate: INFO (design study). Effort: MEDIUM.
4. **BAW-SQUEEZE-ANALOG**: Design a BAW resonator measurement of phonon squeeze variance after a coupling quench. Input: BAW resonator parameters, Chu-Cleland protocol. Output: predicted phonon variance vs r_eff. Gate: INFO (design study). Effort: MEDIUM.
5. **FOUR-SPEED-3HE**: Compare the framework four-speed hierarchy (c_mod, c_BLV, c_BA, c_L) to measured velocity ratios in superfluid 3He-B at comparable BCS-BEC crossover parameters. Input: c ratios from S64. Output: quantitative comparison of ratios. Gate: INFO (comparison). Effort: LOW.
6. **Z2-BAW-ANALOG**: Design a breathing-mode selection rule test in a BAW resonator coupled to a phononic waveguide. Input: BAW + waveguide parameters. Output: predicted Gamma_pair / Gamma_single vs coupling. Gate: INFO (design study). Effort: LOW.

### Closing Line

The workshops confirm that the framework's cosmological predictions are phonon-transport predictions, and the single result that most urgently needs computation -- the squeeze phase phi_eff -- is a quantity whose value phonon physics predicts (constructive, phi_eff ~ 0) but whose verification requires solving the coupled BCS-Bogoliubov system at the fold.
