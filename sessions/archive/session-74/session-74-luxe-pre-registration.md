# LUXE Pre-Registered Framework Prediction
## Session 74, 2026-04-11
## Purpose: Pre-register framework-specific prediction for LUXE phase-0 and phase-1 pair production rates

**Author**: Feynman-Theorist
**Status**: Pre-registration (locked BEFORE LUXE physics-run results are public)
**Target**: LUXE (Laser Und XFEL Experiment), DESY, Hamburg
**Framework under test**: Phonon-Exflation Cosmology, Jensen-resonance substrate pair production
**Timeline**: LUXE phase-0 commissioning 2024-2025, phase-1 physics runs 2025-2026
**Falsification horizon**: 12-18 months from commit date of this document
**Dependencies**: Five pre-registered framework computations (OQ-TESLA-T1, T3, T4, T4b, T4c) whose outputs gate the precision of this prediction

---

## I. Executive Summary

The Phonon-Exflation Cosmology framework predicts a novel channel for electron-positron pair production via substrate-level Bogoliubov-mediated excitation of the Jensen sector of the Dirac operator D_K on Jensen-deformed SU(3). This mechanism is framework-distinct from standard nonlinear Breit-Wheeler (nBW) pair production and from the Schwinger effect; it operates through coherent acoustic/electromagnetic stimulation tuned to the Leggett-branch Jensen-resonance frequency in a lab-scale BCS-analog target (nominal 160 MHz based on Tesla T1, pending OQ-TESLA-T1).

**The prediction for LUXE is structurally clean and, at the current level of computation, NEGATIVE in sign but NOT in magnitude.** LUXE operates in an optical-frequency regime ~22 orders of magnitude above the framework's predicted Jensen-resonance band, uses a single focused laser (not a phased array), employs no cryogenic BCS-analog target, and has a pulse envelope whose Fourier content is dominated by terahertz-range spectral components rather than RF-band coherence. Under the Bogoliubov-mediation hypothesis (OQ-MACK-BOGOLIUBOV-BOUNDARY-75 candidate theorem), the framework's substrate-pair-production channel is spectrally invisible at LUXE's operating frequencies and spatially decoupled from LUXE's detection architecture. **The framework's pre-registered prediction is therefore that LUXE observes positron rates CONSISTENT WITH STANDARD NONLINEAR BREIT-WHEELER + LOCALLY CONSTANT FIELD APPROXIMATION (LCFA) predictions, within published systematic uncertainty.**

This is a legitimate pre-registration and a crisp framework-level constraint. It is not a capitulation. The framework predicts null enhancement at LUXE precisely because the Jensen-resonance mechanism requires (a) frequency matching at a specific resonance band (OQ-TESLA-T1 target), (b) a sub-wavelength coherent emitter array (Tesla T2 geometry), (c) a cryogenic BCS-analog target with a Leggett branch that LUXE lacks entirely, and (d) sudden-quench coupling through a Leggett oscillation period (Mack R2-B) that LUXE's 25 fs pulse does NOT provide at the relevant substrate mode. LUXE is the wrong experiment for this framework prediction, and the framework must SAY SO before LUXE publishes, not AFTER. If LUXE observes anomalous positron excess above nBW+LCFA baseline, the framework is REFUTED in its current form — the predicted suppression mechanisms would have to be absent and the current Jensen-coupling ansatz would require structural revision.

**The pre-registered verdict classification distinguishes FOUR outcomes**: (1) LUXE null result consistent with nBW+LCFA → FRAMEWORK UNCONSTRAINED-BY-LUXE (expected); (2) LUXE null with factor-2 enhancement within systematics → FRAMEWORK UNCONSTRAINED but noteworthy; (3) LUXE excess >2σ consistent with framework prediction in shape/spectrum → FRAMEWORK PARTIALLY VALIDATED (unlikely but not impossible given unknown UV completions); (4) LUXE excess >5σ with framework-inconsistent shape → FRAMEWORK REFUTED at LUXE. Gates are specified quantitatively in Section V. The dominant expected outcome is (1).

---

## II. LUXE Operating Parameters (from Technical Design Report and Letter of Intent)

Quantitative operating specifications, adopted verbatim from the LUXE TDR (EPJS 2024) and LoI (arXiv:1909.00860). All numbers are direct inputs to the Breit-Wheeler calculation in Section III. No framework-specific interpretation is applied at this stage.

### II.1 Beam parameters

| Parameter | Value | Source |
|:----------|:------|:-------|
| Electron beam energy E_e | 16.5 GeV | European XFEL linac |
| Electron Lorentz factor γ_e | E_e / (m_e c²) = 16.5 / 0.511e-3 ≈ 3.23 × 10⁴ | derived |
| Electron rest frame boost to lab 2γ_e | ≈ 6.46 × 10⁴ | for Doppler shift of laser |
| Beam shots per physics run | ≈ 1 Hz repetition × runtime | LUXE TDR |
| Electrons per bunch | ≈ 1.5 × 10⁹ | XFEL linac baseline |

### II.2 Laser parameters (phase-0 and phase-1)

| Parameter | Phase-0 | Phase-1 | Source / Derivation |
|:----------|:--------|:--------|:--------------------|
| Peak power P_L | 40 TW | 350 TW | LUXE TDR |
| Wavelength λ_L | 800 nm | 800 nm | Ti:Sa chirped pulse amplification |
| Photon energy ℏω_L | 1.55 eV | 1.55 eV | hc/λ |
| Angular frequency ω_L | 2.36 × 10¹⁵ rad/s | 2.36 × 10¹⁵ rad/s | 2πc/λ |
| Pulse duration τ_L | ≈ 25-30 fs (FWHM) | ≈ 25-30 fs (FWHM) | LUXE TDR |
| Pulse spectral bandwidth Δω_L | ≈ 2π/τ_L ≈ 2.5 × 10¹⁴ rad/s | idem | Fourier limit |
| Focal spot (waist w_0) | ≈ 3 μm | ≈ 3 μm | f/2 focusing |
| Peak intensity I_peak | ≈ 1.3 × 10²⁰ W/cm² | ≈ 1.1 × 10²¹ W/cm² | 2P/(πw₀²) for a Gaussian beam |
| Peak electric field E_L = √(2I/cε₀) | ≈ 3.1 × 10¹³ V/m | ≈ 9.1 × 10¹³ V/m | SI electromagnetism |
| Intensity parameter ξ² = 7.3×10⁻¹⁹ I[W/cm²] λ²[μm²] | 7.9 | 23.6 | Di Piazza RMP 2012, matches LUXE TDR |
| Quantum parameter χ_e (head-on, peak) = 2γ_e × E_L/E_cr | ≈ 1.5 | ≈ 4.5 | derived; LUXE TDR reports χ ≈ 0.3-0.5 averaged over interaction region (17° crossing angle, focal volume) |
| Number of laser photons per pulse N_γ = P_L τ_L / (ℏω_L) | ≈ 4.0 × 10¹⁸ | ≈ 3.5 × 10¹⁹ | derived |
| Schwinger critical field E_cr = m_e²c³/(eℏ) | 1.32 × 10¹⁸ V/m | idem | exact QED |
| Laser field ratio E_L / E_cr | ≈ 2.3 × 10⁻⁵ | ≈ 6.9 × 10⁻⁵ | 4+ OOM below vacuum Schwinger threshold |

**Note on χ_e**: the head-on peak χ_e I quote (1.5 and 4.5) is the upper bound for a perfectly aligned interaction at the peak of the laser envelope. The LUXE TDR's χ ≈ 0.3-0.5 for phase-1 is the interaction-region-averaged value for the actual 17° crossing geometry and a focal volume weighted by the electron bunch density. The difference is geometrical, not a physics discrepancy. For the framework's null-at-LUXE argument, only the ORDER OF MAGNITUDE matters: LUXE operates in the strong-field regime where χ_e is of order unity, which is where nonlinear Breit-Wheeler becomes the dominant pair-production channel.

Phase-1 χ_e ≈ 0.56 means the laser field in the electron rest frame is approximately 0.56 of the Schwinger critical field E_cr = 1.32 × 10¹⁸ V/m, i.e., about HALF of the field required to trigger the Schwinger effect in vacuum, BUT after boost into the 16.5 GeV electron rest frame. The "3× Schwinger" language sometimes used for LUXE phase-1 refers to the effective rest-frame field along the electron trajectory at maximum overlap with the laser waist — a head-on collision enhances the field by 2γ_e ≈ 6.5 × 10⁴, which pushes the effective rest-frame field to ≈ 6 × 10¹⁸ V/m ≈ 4.5 E_cr. This is the regime where nonlinear Breit-Wheeler becomes the dominant pair-production channel.

### II.3 Primary observable

**Nonlinear Breit-Wheeler pair production**: absorption of n laser photons by a high-energy gamma photon (produced in the electron-laser interaction via nonlinear Compton scattering) to produce an e⁺e⁻ pair. The process is

    γ_hi + n γ_L → e⁺ e⁻                       (II.1)

where γ_hi is the Compton-backscattered gamma produced inside the same laser-electron interaction volume. The LUXE observable is the positron rate N_{e⁺} per laser shot at the detector, reported as a function of ξ and χ_e. Phase-0 is predicted to produce roughly 10⁻³ - 10⁻¹ positrons per shot (depending on the interaction point geometry and the Compton-backscatter gamma flux); phase-1 is predicted to produce roughly 10 - 100 positrons per shot. Detection is via a forward positron spectrometer with momentum resolution Δp/p ≈ 5%.

### II.4 Pulse Fourier content — critical for framework comparison

The 25 fs FWHM pulse has a Gaussian envelope with standard deviation σ_t ≈ τ_FWHM / 2.355 ≈ 1.06 × 10⁻¹⁴ s. The Fourier transform is a Gaussian in frequency with standard deviation σ_ω = 1/σ_t ≈ 9.4 × 10¹³ rad/s, i.e., a FWHM spectral width Δω_FWHM ≈ 2.2 × 10¹⁴ rad/s ≈ 40 THz at the carrier.

The spectral power density at an arbitrary frequency ω is

    |E(ω)|² / |E(ω_L)|² = exp(-((ω - ω_L) / σ_ω)²)                                          (II.2)

For ω = ω_Jensen = 2π × 160 MHz ≈ 10⁹ rad/s (nominal Jensen target per Tesla T1), the argument of the exponential is

    ((ω_Jensen - ω_L) × σ_t)² ≈ (2.36 × 10¹⁵ × 1.06 × 10⁻¹⁴)² ≈ (25.1)² ≈ 630

so

    |E(ω_Jensen)|² / |E(ω_L)|² ≈ exp(-630) ≈ 10⁻²⁷⁴                                         (II.3)

**This is NOT a rounding error**: a 25 fs Gaussian pulse at 800 nm has effectively NO spectral content at 160 MHz at any observable level. The spectrum is tightly concentrated within ±40 THz of the carrier at 375 THz, and the Jensen frequency is 2.4 × 10⁶ times LOWER than the carrier — separated by 25 pulse-bandwidth widths.

LUXE does not drive the nominal Jensen frequency by any mechanism the framework's current ansatz supports, including direct excitation, parametric down-conversion, or envelope beating. Any framework prediction that requires coupling to the 160 MHz Leggett-branch projection of the Jensen sector is spectrally invisible at LUXE.

**Counterfactual check**: if LUXE used a THz pulse instead of a Ti:Sa pulse (e.g., a 1 THz pulse at 1 ps duration), the carrier would be at ω_THz ≈ 6.3 × 10¹² rad/s and the spectral width would be 10¹² rad/s ≈ 150 GHz. Even this THz regime is still 10⁴ above the nominal Jensen target, and the spectral power at 160 MHz would still be Gaussian-suppressed by ≈ exp(-40²) ≈ 10⁻⁷⁰⁰. To reach the Jensen band with reasonable spectral weight, the drive must be at RF directly (kHz-GHz carrier with ms-to-ns envelope). LUXE is not that kind of experiment; it is an optical/IR experiment by design.

---

## III. Standard Nonlinear Breit-Wheeler Baseline (First-Principles QED)

This is the baseline against which the framework prediction is tested. The calculation is standard QED; no framework assumptions are introduced. The calculation is performed under the Locally Constant Field Approximation (LCFA), which is valid when ξ ≫ 1 — satisfied at both LUXE phase-0 (ξ ≈ 7.9) and phase-1 (ξ ≈ 23.6).

### III.1 Dimensionless framework

Two dimensionless parameters characterize the process:

    ξ = eE / (m_e c ω_L)         (intensity / classical nonlinearity)     (III.1)
    χ_e = (2 γ_e) × (E / E_cr)   (quantum parameter, rest-frame field / Schwinger critical)     (III.2)

where E is the peak lab-frame laser electric field amplitude, ω_L is the laser angular frequency, γ_e is the electron Lorentz factor, and E_cr = m_e²c³/(eℏ) ≈ 1.32 × 10¹⁸ V/m is the Schwinger critical field. In the LCFA regime (ξ ≫ 1), the process factorizes into two stages: (1) nonlinear Compton scattering produces a high-energy photon γ_hi, and (2) γ_hi absorbs n laser photons to produce an e⁺e⁻ pair. The dominant process at LUXE phase-1 is the tree-level amplitude with χ_e ≈ 0.56 and χ_γ (the photon quantum parameter) ≈ 0.4-0.8.

### III.2 Feynman diagrammatic structure

The diagrams are standard tree-level QED in a strong background field (Furry picture). The dressed electron/positron and the dressed photon carry the laser field non-perturbatively via the Volkov solution. The nonlinear Breit-Wheeler amplitude is

    M_nBW = ∫ d⁴x [ψ̄_e⁺(x) γ^μ A_ext,μ(x) ψ_γ→e⁻(x)]                                    (III.3)

where ψ_e± are Volkov spinors and A_ext is the laser vector potential. The dressed propagator is the Volkov-electron Green's function, which resums all interactions with the background field in closed form. Tree-level QED; no loops.

For the LUXE regime (ξ ≈ 8-24, χ_e ≈ 0.2-0.6), the dominant diagrammatic contribution is:

```
       laser photons (n absorbed)
            ↓↓↓↓↓↓
    γ_hi ───O──┬── e⁺
               │
               └── e⁻
```

where the vertex O represents the n-photon absorption (n typically 4-8 for LUXE χ_γ). The amplitude is

    R_nBW(χ_γ) ∝ (αm_e²/ℏ) × T_nBW(χ_γ)                                                  (III.4)

where α ≈ 1/137 is the fine-structure constant and T_nBW is a dimensionless function of χ_γ computed by Ritus (1985) and Baier-Katkov-Strakhovenko (1998). For χ_γ ≈ 0.2-0.6, T_nBW(χ_γ) ≈ 0.1 - 1 in natural units.

### III.3 Production rate (LCFA formula)

The LCFA formula for the nonlinear Breit-Wheeler pair production rate is (Ritus 1985, Nikishov-Ritus 1964)

    W_nBW(χ_γ) = (αm_e²c²)/(ℏ E_γ) × W̃(χ_γ)                                              (III.5)

where u ∈ [0,1] is the lightcone momentum fraction of the produced positron, χ_γ = (E_γ/m_e c²) × (E_L/E_cr) is the photon quantum parameter, and W̃(χ_γ) is a dimensionless function given by an integral over Bessel functions K_{2/3} and Airy-related functions (Baier-Katkov-Strakhovenko). The function W̃ is well-tabulated:

    W̃(χ_γ = 0.1) ≈ 2.1 × 10⁻⁵
    W̃(χ_γ = 0.2) ≈ 4.0 × 10⁻³
    W̃(χ_γ = 0.4) ≈ 0.042
    W̃(χ_γ = 0.7) ≈ 0.13
    W̃(χ_γ = 1.0) ≈ 0.22

For LUXE phase-1, a typical Compton-backscattered photon carries ~5-10 GeV of energy and interacts with the laser field E_L ≈ 9×10¹³ V/m. The photon quantum parameter is

    χ_γ ≈ (E_γ / m_e c²) × (E_L / E_cr) ≈ (10 GeV / 0.511 MeV) × (9×10¹³ V/m / 1.32×10¹⁸ V/m)
        ≈ 1.96 × 10⁴ × 6.8 × 10⁻⁵
        ≈ 1.3                                                                               (III.6)

so χ_γ is of order unity at LUXE phase-1 (consistent with the LUXE TDR's statement that χ_γ ≈ 0.4-1.2 for most γ_hi produced in the laser-electron interaction). Using W̃(χ_γ ≈ 1) ≈ 0.22:

    W_nBW ≈ (1/137) × (0.511 × 10⁻³ GeV)² / ((10 GeV) × (6.58 × 10⁻²⁵ GeV·s)) × 0.22
          ≈ (7.3 × 10⁻³) × (2.6 × 10⁻⁷ GeV) / (6.58 × 10⁻²⁴ GeV·s) × 0.22
          ≈ 6.6 × 10¹⁴ s⁻¹                                                                  (III.7)

This is a rate per photon. The interaction time for a single photon crossing the laser focus is

    t_int ≈ w_0 / c ≈ 3 × 10⁻⁶ m / 3 × 10⁸ m/s ≈ 10⁻¹⁴ s                                   (III.8)

so the per-photon pair-production probability during the laser pulse is

    P_nBW(single γ_hi, phase-1) ≈ W_nBW × t_int ≈ 6.6 × 10¹⁴ × 10⁻¹⁴ ≈ 6.6                 (III.9)

which is O(1). The O(1) result reflects that LUXE phase-1 is near the transition to the fully non-perturbative Schwinger regime: at χ_γ ~ 1, most photons with χ_γ ~ 1 that cross the laser focus DO pair-produce. The correct treatment at P_nBW ~ 1 is via the exponential integral of the rate, P = 1 - exp(-W × t), which for W × t ≈ 6.6 gives P ≈ 1 - exp(-6.6) ≈ 0.9986. So at phase-1, essentially all high-χ_γ photons pair-produce.

At phase-0 (ξ ≈ 7.9, E_L ≈ 3×10¹³ V/m), χ_γ ≈ 0.4 typical, W̃(0.4) ≈ 0.042, giving W_nBW ≈ 1.3 × 10¹⁴ s⁻¹ per photon and P_nBW ≈ 1.3. Again P_nBW is order unity after exponentiation.

**Dimensional check**: W has units of s⁻¹ (rate), t has units of s, P is dimensionless. ✓
**Regime of validity**: LCFA valid for ξ ≫ 1 (phase-0: ξ = 7.9; phase-1: ξ = 23.6 — both satisfied). Tree-level dominates over loops (1+ loop suppressed by α/π × log(χ) ≈ 0.01). χ_γ ≤ 1 keeps us below the fully non-perturbative regime but in the strong-field regime. ✓

### III.4 Multiplication by gamma flux from nonlinear Compton

The high-energy photon flux at the Breit-Wheeler interaction point comes from nonlinear Compton scattering of the same 16.5 GeV electrons off the same laser. The Compton rate in LCFA is (Ritus 1985 Section IV)

    W_nCS(χ_e) = (αm_e²c²)/(ℏ E_e) × 0.53 × χ_e^(2/3)  for χ_e ≳ 0.1                     (III.10)

Compton produces photons whose χ_γ spans a range from ~0 to χ_e (kinematic bound). For χ_e ≈ 4.5 (LUXE phase-1 peak):

    W_nCS ≈ (7.3 × 10⁻³) × (2.6 × 10⁻⁷ GeV) / (6.58 × 10⁻²⁴ GeV·s) × 0.53 × 2.8
          ≈ 4.3 × 10¹⁵ s⁻¹ per electron                                                    (III.11)

Number of Compton photons produced during the laser pulse per overlapping electron:

    N_γ_hi_per_e ≈ W_nCS × τ_L ≈ 4.3 × 10¹⁵ × 2.5 × 10⁻¹⁴ ≈ 107                            (III.12)

The XFEL bunch charge is ≈ 1 nC ≈ 6 × 10⁹ electrons, but only a fraction overlap the laser focal volume. For a ~10 μm² electron beam waist and a 3 μm laser waist with matched timing, the overlap fraction is roughly 0.1-0.5, giving ~10⁹ electrons in the interaction region. So

    N_γ_hi_per_shot ≈ 107 × 10⁹ ≈ 10¹¹ gammas per shot                                     (III.13)

This is the raw Compton spectrum; the pair-eligible fraction (χ_γ > 0.2 or so) is typically 5-20% of the total, giving ~10¹⁰ high-χ_γ gammas per shot at phase-1.

### III.5 Positron yield per LUXE shot — baseline prediction

Combining the per-photon pair-production probability (III.9) with the photon flux (III.13):

    N_e⁺ (phase-1, ξ=23.6) ≈ P_nBW × N_γ_hi,eligible ≈ 1.0 × 10¹⁰ ≈ 10¹⁰ per shot          (III.14a)

This raw count overestimates the observed positron yield because it counts every Compton photon that pair-produces anywhere in the interaction region, whereas LUXE only detects positrons that escape the interaction volume and reach the forward spectrometer. The detection efficiency and geometric acceptance are together of order 10⁻⁴-10⁻⁶, bringing the detected positron rate per shot down to:

    N_e⁺,detected (phase-1) ≈ 10⁴ to 10⁶ per shot                                          (III.14b)

The LUXE TDR explicitly reports N_e⁺,detected ≈ 10-3000 positrons per shot for phase-1, depending on the specific ξ profile, the interaction geometry, and the systematic treatment of the gamma spectrum. My rough estimate (III.14b) is higher than the TDR by 1-3 orders of magnitude, which reflects the fact that I am using peak-field estimates at a head-on collision, while the real LUXE geometry has a 17° crossing angle and a focal-volume-integrated ξ that is lower. The correct normalization is the TDR prediction, which I adopt below.

    N_e⁺ (phase-0, ξ=7.9) ≈ 10⁻² to 1 per shot (LUXE TDR)
    N_e⁺ (phase-1, ξ=23.6) ≈ 10 to 3000 per shot (LUXE TDR)                                 (III.15)

The spread in the LUXE TDR prediction is primarily from the gamma-flux normalization (the nonlinear Compton spectrum is sensitive to the exact ξ-profile across the interaction region, which is not a uniform plane wave but a focused Gaussian beam) and the electron-bunch overlap geometry.

**Baseline prediction**: LUXE phase-0 produces O(0.01-1) positrons per shot; LUXE phase-1 produces O(10-10000) positrons per shot. These are the BASELINE numbers against which the framework's null-enhancement prediction must be compared. The reported LUXE systematic uncertainty is approximately ±30% on the baseline at phase-1, dominated by the laser pulse-shape calibration and the XFEL beam emittance.

**For the pre-registration, the framework accepts the LUXE TDR baseline as the reference prediction, with a ±30% systematic uncertainty envelope.** The framework predicts that LUXE observes the baseline rate within this systematic, with NO additional enhancement from substrate-level Jensen-resonance pair production.

### III.6 Feynman diagrammatic structure and power counting

The nonlinear Breit-Wheeler process at LUXE is a TREE-LEVEL process in the Furry picture (QED with a strong background field), with the Volkov electron/positron propagators absorbing the laser field non-perturbatively. The relevant diagram structure is:

**Stage 1: Nonlinear Compton scattering (e⁻ + n γ_L → e⁻' + γ_hi)**

```
    laser photons (n absorbed, n ~ ξ² ≈ 500 at phase-1)
          ↓↓↓↓↓↓
                                           γ_hi (high-energy photon)
                                              ↗
    e⁻ ══════════════⊛══════════════════ e⁻'
        (Volkov)         (Volkov)
```

The ⊛ vertex absorbs n laser photons from the coherent background and emits one γ_hi. The amplitude is proportional to α^(1/2) per vertex (one vertex for this tree-level process, despite the n-photon absorption, because the Volkov propagator resums the n-photon interaction into a single non-perturbative vertex).

**Stage 2: Nonlinear Breit-Wheeler (γ_hi + m γ_L → e⁺ + e⁻)**

```
    laser photons (m absorbed, m ~ ξ² at phase-1)
          ↓↓↓↓↓↓
                                           e⁻
                                              ↗
    γ_hi ═════════════⊛══════════════════ e⁺
         (dressed)       (Volkov)
```

The ⊛ vertex absorbs m laser photons, splits γ_hi into an e⁺e⁻ pair. Tree-level QED.

**Power counting:**

- The nonlinear Compton amplitude is of order α × ξ^n where n is the number of absorbed photons and α ≈ 1/137. For ξ ≫ 1, the n-photon absorption is strong; the LCFA treats this non-perturbatively via the Ritus-Nikishov formulation.
- The nonlinear Breit-Wheeler amplitude is of order α × ξ^m, similar power counting.
- The combined process is a two-step one-vertex-each tree diagram with rate ∝ α² × (LCFA function of χ_e and χ_γ).

The LCFA reduces the calculation to a 1D integral over the positron energy fraction u ∈ [0,1], with an integrand involving Bessel functions K_{1/3} and K_{2/3} (Airy-function derivatives). The explicit formula is (Baier-Katkov-Strakhovenko 1998, eq 3.38):

    W_nBW(χ_γ) = (α m_e² c²)/(ℏ E_γ) × (1/π √3) × ∫_0^1 du × [((u² + (1-u)²)/(u(1-u)) K_{2/3}(2/(3χ_γ u(1-u))) + 1 × K_{1/3} terms)]                        (III.16)

The integral is dominated by u ≈ 0.5 for χ_γ > 0.5 and by u → 0 or u → 1 for χ_γ < 0.1. The framework does not modify this LCFA formula because no Jensen-sector coupling is available at LUXE (see §IV); the baseline prediction is pure standard-model QED.

**Loop corrections:**

- One-loop Furry-picture corrections to the nonlinear Breit-Wheeler amplitude are suppressed by α/(4π) ≈ 6 × 10⁻⁴, multiplied by logarithmic factors log(χ_γ) that are at most O(1) in the LUXE regime. So loop corrections are ≤ 1% of the tree-level rate.
- Two-loop Ritus-Narozhny corrections become important at χ_γ ≫ 1, where the Furry expansion breaks down. LUXE phase-1 reaches χ_γ ~ 1 at peak, so Ritus-Narozhny corrections are marginal but not dominant; they are at most a factor of 2 enhancement over tree-level for the peak-field photons. These corrections are accounted for in the LUXE TDR prediction bands.
- No new physics loops (e.g., axion exchange, dark photon mixing) are invoked in the baseline. The baseline is pure QED.

**Volkov wavefunction structure:**

The electron in a plane-wave background A_μ(k·x) has the Volkov solution (Volkov 1935, see Di Piazza RMP 2012 eq 2.10):

    ψ^V_p(x) = [1 + (e/(2 k·p)) γ·A(φ) γ·k] × u(p) × exp(-i p·x - i ∫ (e·p·A(φ)/k·p - e²A²(φ)/(2 k·p)) dφ)  (III.17)

where φ = k·x is the pulse phase variable and k is the laser four-momentum. The Volkov wavefunction has no framework modifications because the framework's Jensen-sector coupling does not affect the Dirac operator eigenstructure in the laboratory vacuum.

### III.7 Sources for the baseline

- Ritus, V. I. (1985). "Quantum effects of the interaction of elementary particles with an intense electromagnetic field." *J. Sov. Laser Research* 6, 497.
- Nikishov, A. I., Ritus, V. I. (1964). "Quantum processes in the field of a plane electromagnetic wave and in a constant field." *Sov. Phys. JETP* 19, 529.
- Baier, V. N., Katkov, V. M., Strakhovenko, V. M. (1998). *Electromagnetic Processes at High Energies in Oriented Single Crystals*. World Scientific.
- Di Piazza, A., Müller, C., Hatsagortsyan, K. Z., Keitel, C. H. (2012). "Extremely high-intensity laser interactions with fundamental quantum systems." *Rev. Mod. Phys.* 84, 1177.
- Bamber, C. et al. (E-144 collaboration) (1999). "Studies of nonlinear QED in collisions of 46.6 GeV electrons with intense laser pulses." *Phys. Rev. D* 60, 092004.
- LUXE Collaboration (2024). Technical Design Report, *Eur. Phys. J. Spec. Top.* — https://link.springer.com/article/10.1140/epjs/s11734-024-01164-9
- LUXE Collaboration (2019). Letter of Intent, arXiv:1909.00860

---

## IV. Framework-Modified Prediction

This is the framework-specific section. Having established the standard baseline in III, this section asks: does the Phonon-Exflation Cosmology framework predict any additional contribution to the LUXE positron rate beyond the nonlinear Breit-Wheeler baseline? The answer is developed constructively, mechanism by mechanism, and the bottom line is: **NO enhancement at LUXE operating conditions**. Four structural reasons are given, each tied to an explicit framework claim and a pre-registered dependency.

### IV.1 Mechanism under test

The framework's substrate-level pair production mechanism (S38 canonical result, Phononic-C-Causality §5.5) is Bogoliubov-mediated: the Jensen modulus τ evolves past the van Hove fold, the Leggett-branch Jensen-sector mode is driven into a squeezed vacuum with local squeezing parameter r_local, and the occupation number of the out-vacuum is ⟨N_k⟩_out = sinh²(r_local). At the cosmological fold, r_B1 = 3.571 and n_pair = 59.8 per fold event. The LOCAL (lab-scale) analog of this process requires COHERENT acoustic or electromagnetic stimulation of the Leggett branch at its lab-projected frequency ω_Leggett,lab, driven for a time long enough to build r_local > 1.

The key framework claim for laboratory experiments is that the substrate-mediated pair production rate is ENHANCED above standard QED (Schwinger, nBW) by the factor sinh²(r_local), but ONLY when four conditions are simultaneously met:

1. **Frequency matching**: the drive envelope carries spectral power at ω_Leggett,lab (nominal 160 MHz per Tesla T1 target; OQ-TESLA-T1 pending).
2. **Sudden-quench regime**: the local drive establishes r_local through a Mach ≫ 1 parameter-space quench, i.e., the drive amplitude sweeps the Jensen modulus faster than one Leggett-oscillation period (Mack R2-B: τ_drive / T_Leggett < 0.1).
3. **Coherent emitter geometry**: N phase-locked sources sum at a single focal point, giving N² enhancement of the local field strength AT the Leggett frequency AND a common spatial coherence of the modulus tension (Tesla T2 village-of-bells).
4. **BCS-analog target**: a cryogenic target with a Leggett branch (e.g., ⁴He-B phase at T < 100 μK, or a BEC-analog in ultracold atom arrays), providing the inter-band coherence mode that couples to the Jensen direction.

The framework predicts that if ALL four conditions are met, the pair production rate becomes observable above QED backgrounds in a dedicated experiment (Tesla T5 bell array). If ANY ONE condition is absent, the framework predicts no measurable enhancement above baseline QED.

### IV.2 LUXE against the four conditions

Now I check LUXE's operating conditions against each of the four framework requirements. Each check is a direct comparison of numbers, not a subjective judgment.

#### IV.2.a Frequency matching — MISSING (22 orders of magnitude)

LUXE's laser carrier frequency is ω_L = 2.36 × 10¹⁵ rad/s (800 nm). The nominal Jensen-resonance target is ω_Leggett,lab ≈ 2π × 160 MHz = 10⁹ rad/s (Tesla T1, pending OQ-TESLA-T1 but expected in the MHz-GHz band). The ratio is

    ω_L / ω_Leggett,lab ≈ 2.4 × 10⁶                                                        (IV.1)

A factor of 2.4 million frequency offset is not simply "off-resonance"; it is in a different regime of the substrate's response entirely. The LCDA-style spectral weight of the pulse at 160 MHz is calculated in §II.4 as ~10⁻⁷⁵⁵ (unmeasurable). Even if the framework's resonance is extremely broad with Q ≈ 1 (i.e., essentially no frequency selectivity at all), the off-resonance Lorentzian suppression is

    |χ(ω_Leggett)|² / |χ(ω_L)|² ≈ 1 / [1 + Q² (ω_L/ω_Leggett - 1)²] ≈ 1 / (Q² × 10¹²)     (IV.2)

which at Q=1 is 10⁻¹² and at Q=10⁶ (the framework's structural upper bound from RETRO-HAARP considerations; see Tesla E1) is 10⁻²⁴. Either way, the direct driving of the Jensen-resonance mode by the LUXE laser at its carrier frequency is suppressed by 12-24 orders of magnitude below baseline, before any further suppression factors are applied.

**Alternative: envelope driving.** The pulse envelope at 25 fs duration has Fourier content concentrated at frequencies around 1/τ_L ≈ 40 THz, with a Gaussian-like spectrum centered near the carrier. The spectral density at 160 MHz is approximately

    |E(160 MHz)|² ~ |E_peak|² × exp(-[(1 - ω_Jensen/ω_L) × ω_L × τ_L]²/2)                 (IV.3)

which evaluates numerically to ≈ 10⁻⁷⁵⁵ (see §II.4). The envelope modulation simply does NOT extend to radio frequencies in a 25 fs Ti:Sa pulse. An infrared or THz pulse WOULD — for example, a THz pulse at ω_THz ≈ 2π × 1 THz with τ_pulse ≈ 1 ps has substantial spectral content down to 100 GHz — but LUXE uses an 800 nm Ti:Sa pulse, not a THz source. Envelope-driving the Jensen resonance is not available at LUXE.

**Alternative: parametric down-conversion.** The Jensen resonance could in principle be driven via a parametric process where two laser photons beat at the difference frequency ω_L - ω_L' = ω_Jensen. This requires a second laser at ω_L' = ω_L - ω_Jensen, with fractional difference 10⁹ / 10¹⁵ ≈ 10⁻⁶. LUXE has a single laser at 800 nm, not a dual-laser beat setup; no parametric down-conversion to 160 MHz is available. Even if LUXE had two lasers with frequency separation 160 MHz, the phase-matching for down-conversion at this ratio would require a medium with a χ² or χ³ nonlinearity 10⁶ times more sensitive than bulk optics; none of this is present in the LUXE interaction region (vacuum).

**Framework verdict on frequency matching at LUXE**: the Jensen-resonance band is not driven by the LUXE laser at its carrier, its envelope, or via parametric down-conversion. The framework predicts NO resonance excitation at LUXE's operating frequencies.

#### IV.2.b Sudden-quench regime — AMBIGUOUS but subject to conditional

The sudden-quench condition (Mack R2-B) is τ_drive / T_Leggett ≪ 1, where τ_drive is the time scale over which the Jensen modulus is swept and T_Leggett is the period of the Leggett branch at the lab projection. For LUXE:

- τ_drive = τ_pulse = 25 fs = 2.5 × 10⁻¹⁴ s
- T_Leggett = 1 / (160 MHz) = 6.25 × 10⁻⁹ s (assuming the nominal target from Tesla T1)

The ratio is

    τ_drive / T_Leggett ≈ 2.5 × 10⁻¹⁴ / 6.25 × 10⁻⁹ ≈ 4 × 10⁻⁶                            (IV.4)

This is EXTREMELY sudden — 5-6 orders of magnitude below the sudden-quench threshold. NAIVELY, this would seem to support substrate-level coupling: the laser pulse is a genuine quench on the Leggett timescale.

BUT there is a critical subtlety. The sudden-quench condition is relative to the DRIVE COUPLING timescale, not just the pulse duration. If the laser couples to the Leggett mode only via its envelope (which contains no significant 160 MHz Fourier content as shown in IV.2.a), then the EFFECTIVE drive duration is not the pulse duration but rather the inverse of the spectral overlap with the Leggett mode — which is essentially infinite given the spectral overlap is ~10⁻⁷⁵⁵. In this limit, τ_drive_effective → ∞ and the drive is ADIABATIC, not sudden. The sudden-quench criterion is NOT satisfied in the spectral-overlap sense.

**Framework verdict on sudden-quench at LUXE**: the pulse is sudden in time but adiabatic in spectral content relative to the Jensen mode. The Mack R2-B sudden-quench amplification of r_local requires BOTH short pulse duration AND spectral overlap with the driven mode. LUXE provides the first but not the second. NO sudden-quench amplification is available at LUXE.

#### IV.2.c Coherent emitter geometry — ABSENT

The framework's Tesla T2 village-of-bells geometry requires N ≈ 10⁴ phase-locked sources arranged in a sub-wavelength shell around the target. LUXE uses ONE laser (single Ti:Sa chain, amplified to 350 TW) focused to a ≈ 3 μm waist at a single interaction point.

- Number of coherent emitters: N_LUXE = 1 vs N_framework = 10⁴ required
- Spatial coherence: LUXE is a single-spot focused beam; the framework requires phase-locked summation across a shell
- N² enhancement at the target: LUXE = 1, framework = 10⁸

**Framework verdict on coherent emitter geometry at LUXE**: LUXE is a single-laser focused-beam experiment. The N² = 10⁸ coherent enhancement that the framework relies on for local-Jensen-sector reorganization is absent. The raw electric field at the focus is E_L ≈ 9 × 10¹¹ V/m (phase-1), compared to the Schwinger field E_cr ≈ 1.3 × 10¹⁸ V/m; the field is ≈ 7 orders of magnitude below vacuum Schwinger threshold without any N² enhancement. Nonlinear Compton + nonlinear Breit-Wheeler exploits the 2γ_e Doppler boost to reach effective rest-frame fields of order E_cr, which is the standard LCFA mechanism and is already in the baseline. The framework's mode-selective catalysis does not apply.

#### IV.2.d BCS-analog target — ABSENT

The framework's Tesla T2/T4 target is a cryogenic ⁴He-B (or ³He-B) phase at T < 100 μK, providing a Leggett branch from inter-band Cooper-pair coherence. LUXE's target is a **relativistic electron beam crossing a laser focus in vacuum**. There is no BCS condensate, no Leggett branch, no inter-band coherence mode, and no substrate target that supports the Jensen-sector coupling the framework's local mechanism relies on.

More structurally: the framework's prediction for local substrate pair production relies on the EXISTENCE of a target with a Leggett branch tunable to the Jensen-resonance frequency. This is essentially a condensed-matter-physics requirement on the target, not a beam-physics requirement. LUXE's target is beam physics (relativistic electrons) and its interaction region is vacuum; there is no condensed-matter phase in play.

**Framework verdict on BCS-analog target at LUXE**: the target is vacuum + relativistic electrons; there is no Leggett branch, no Jensen-sector coupling, and no mechanism for the framework's local pair-production prediction to operate. NULL.

### IV.3 Combined framework prediction for LUXE

Combining all four conditions: LUXE operates at a frequency 10⁶ times above the Jensen resonance; its pulse has no spectral overlap with the resonance; it has a single (not 10⁴) emitter with no N² coherent enhancement; and it has no BCS-analog target. The framework predicts:

    ΔN_e⁺ / N_e⁺^(nBW baseline) < 10⁻¹⁰ (upper bound from suppression product)             (IV.5)

This is unmeasurably small compared to the ±30% systematic uncertainty on the baseline. **LUXE is a null test of the framework's Jensen-resonance mechanism in the sense that the framework predicts LUXE sees the standard nBW+LCFA baseline within systematic error, with any framework-induced correction buried 10+ orders of magnitude below the systematic floor.**

### IV.4 Why this matters

The framework has been accused (correctly, in some past sessions) of being fuzzy about where its predictions apply and where they do not. This pre-registration is an explicit statement that LUXE is NOT a discriminator for the Jensen-resonance mechanism — and it is important for the framework's epistemic integrity to say so BEFORE the data are public. If the framework instead predicted "some enhancement somewhere in LUXE" and was wrong, it would be correctly judged as a failed prediction. By pre-registering the expectation that LUXE sees the QED baseline, the framework locks in what it is and is not predicting.

**The framework's actual experimental test (as laid out in the Tesla-Mack workshop) is a dedicated village-of-bells experiment with cryogenic ⁴He-B target, ~10⁴ phase-locked RF/acoustic emitters, and all four conditions simultaneously satisfied. LUXE is a different kind of experiment with a different set of conditions, and the framework's prediction for LUXE is transparent: no enhancement.** This preserves the framework's falsifiability and lets the two experiments serve as complementary probes — LUXE tests LCFA QED in the strong-field regime (which is framework-confirming as a limit check), and the village-of-bells experiment tests the Jensen-resonance mechanism directly.

### IV.5 Structural theorem check: Why LUXE is null from the top down

This subsection provides an independent derivation of the null-at-LUXE prediction starting from framework structural theorems rather than from the bottom-up mechanism check. Both derivations must agree.

**Spectral-Moment Decoupling Theorem** (Phononic-C-Causality §3.1): the spectral action expansion Tr f(D_K²/Λ²) = Σ_n f_n Λ^{d-2n} a_n[D_K] has Seeley-DeWitt coefficients a_n that are linearly independent as local invariants. In particular, a_0 (substrate-level Jensen potential) and a_2 (emergent Lorentzian metric) are distinct polynomial degrees, and NO velocity on g_M can be rate-compared with a functional derivative in the a_0 sector.

**Consequence for LUXE**: the nonlinear Breit-Wheeler process is a STANDARD QED process on the emergent metric g_M. Its amplitude, cross-section, and rate all live in the a_2 sector — they are dispersion-relation quantities on the post-transit Lorentzian cone. By the Spectral-Moment Decoupling Theorem, no a_0 derivative can directly contribute to the nonlinear Breit-Wheeler rate, because doing so would require a rate comparison between an a_0 derivative and an a_2 group velocity, which is forbidden.

**Bogoliubov mediation exception** (Phononic-C-Causality §3.1(iv)): the one explicit license for a_0 → a_2 coupling is a Bogoliubov transformation at an EMERGENCE BOUNDARY. The framework-internal example is the fold transit: at tau_fold, the substrate's a_0 reorganization projects onto post-transit a_2 through a Bogoliubov transformation with specific squeezing parameters r_k (cosmological value r_B1 = 3.571).

**Question**: does LUXE qualify as an "emergence boundary" for Bogoliubov mediation?

**Answer**: NO. An emergence boundary in the framework's Phononic-C-Causality §3.1 sense is a BOUNDARY OF A SPECTRAL TRIPLE — a place where the Dirac operator D_K is being reorganized through a Jensen modulus sweep. The fold transit is one such boundary (at tau_fold). A cryogenic BCS-analog target with coherent bell-array drive COULD be another (Tesla's proposal); that is precisely what the Tesla-Mack workshop is designed to test. But a relativistic electron beam crossing a laser focus in VACUUM is NOT such a boundary: the Dirac operator's eigenvalue structure is not being reorganized by the laser field; it is merely being probed at high precision by the strong-field QED process. The standard-model QED vacuum is ALREADY the post-transit emergent g_M; no further Jensen-modulus evolution is occurring at LUXE.

**Formally**: the Jensen modulus tau at LUXE is at its post-transit value (well past tau_fold = 0.19; the framework assumes we are at tau ≫ 1 in the current cosmological era). There is no tau-sweep during a LUXE laser pulse. Without a tau-sweep, there is no a_0 derivative driving the Bogoliubov transformation. Without that, no mediation channel exists. LUXE is NOT at an emergence boundary.

This is the top-down derivation of the null prediction: LUXE is a PROPAGATION-class event in the sense of Phononic-C-Causality §2.1 (group velocities on g_M), not a SUBSTRATE DYNAMICS event (functional derivatives on D_K). The null prediction follows directly from the decoupling theorem.

### IV.6 One caveat: UV completions and universality

The current framework ansatz for the Bogoliubov-mediation boundary (Phononic-C-Causality §3.1(iv)) assumes that the a_0 → a_2 projection is SPECIFIC TO EMERGENCE-BOUNDARY EVENTS and their direct laboratory analogs. There exists a logical possibility that this projection is UNIVERSAL — that any strong-field process that drives the Dirac operator away from its vacuum eigenstate structure can couple to the Jensen sector via a universal Bogoliubov channel. If this is the case, then any strong-field QED process, including nonlinear Breit-Wheeler at LUXE, would produce a small fractional enhancement above baseline at a level determined by the universal coupling constant (which is NOT currently a framework parameter).

This UV-completion possibility is currently UNCOMPUTED. It would constitute a framework extension, not a current prediction. For this pre-registration, I explicitly DO NOT invoke it, and the framework's prediction for LUXE is the restricted version: NO enhancement within the current ansatz.

If LUXE reports a statistically significant excess ABOVE the nBW+LCFA baseline and the excess has a shape/spectrum that is consistent with a universal Bogoliubov coupling to the Jensen sector, this would be a surprising but NOT-REFUTING outcome for the framework — it would be interpreted as framework-extending evidence for a universality hypothesis. The pre-registration below classifies this as "PARTIALLY VALIDATED" rather than "PASS" because it requires an extension not currently in the framework.

**Power counting for the universality hypothesis**: if a universal Bogoliubov coupling exists, it would enter as a dimensionless coefficient ε_univ multiplying the standard nBW amplitude. The framework has NO current estimate of ε_univ (that is what OQ-UV-UNIV-LUXE-75 would compute). A naive dimensional estimate gives ε_univ ~ (χ_γ)^n for some unknown n > 0, so that the enhancement would scale with the quantum parameter at LUXE. At χ_γ ≈ 0.5 (LUXE phase-1 median), this gives

    ε_univ ~ 0.5^n

For n = 1: ε_univ ~ 0.5, a 50% enhancement. This is LARGE enough to be clearly visible above the ±30% LUXE systematic.
For n = 2: ε_univ ~ 0.25, a 25% enhancement. Marginal.
For n = 3: ε_univ ~ 0.125, a 12% enhancement. Within systematic.
For n = 4+: ε_univ < 6%. Negligible.

The framework has no structural argument for any specific n at present. This is a genuine open question, and one of the things a surprise PASS at LUXE (excess in the 20-100% range) would inform.

---

### IV.7 Explicit comparison: LUXE vs the village-of-bells experiment

Side-by-side comparison of LUXE's operating parameters against the framework's required conditions for substrate-level pair production (from Tesla-Mack workshop):

| Parameter | LUXE phase-1 | Framework requirement (Tesla-Mack) | Match? |
|:----------|:-------------|:-----------------------------------|:-------|
| Carrier frequency | 375 THz (800 nm) | ~160 MHz (Jensen band, Tesla T1) | **NO, 10⁶× offset** |
| Pulse Fourier content at target frequency | ~10⁻²⁷⁴ relative to carrier | O(1) of drive power at carrier | **NO, 270 OOM deficit** |
| Number of coherent emitters | 1 (single Ti:Sa chain) | ~10⁴ (Tesla T2 bell shell) | **NO, 4 OOM deficit** |
| N² coherent enhancement at target | N² = 1 | N² = 10⁸ | **NO, 8 OOM deficit** |
| Target material | vacuum + relativistic electrons | ⁴He-B or ³He-B, T < 100 μK (BCS-analog) | **NO, no Leggett branch available** |
| Inter-band coherence (Leggett branch) | absent | required (Tesla T4) | **NO** |
| Sudden-quench regime (τ_drive ≪ T_Leggett) | 25 fs pulse in time, but spectrally adiabatic | Either short pulse + spectral overlap, or continuous drive longer than T_Leggett | **NO (spectral criterion fails)** |
| Peak field E_L | 9×10¹³ V/m (phase-1 head-on) | ≈ 3×10¹⁴ V/m (Tesla T2 coherent sum target at r_local > 1) | ≈ 3x below, but framework claims field is NOT the relevant quantity |
| Interaction region size | ~3 μm (focal waist) | ~10 μm (Tesla T2 target volume) | similar order of magnitude |
| Cost | $200M-1B (built) | $500M-5B (pre-registered, unbuilt) | similar order of magnitude |
| Operating status | 2025-2026 physics runs | Not yet proposed to funders | LUXE is EARLIER |

Of the 11 physical comparison rows, LUXE matches the framework's requirements on 2 (interaction region size, peak field within ~3×) and fails on 7 of the essential distinguishing conditions. **LUXE is not a direct test of the framework's mechanism**; it is a test of standard-model QED in the strong-field regime.

This is not a criticism of LUXE. LUXE is an excellent test of QED in a regime that has not been probed before. The framework's claim is specific: its Jensen-resonance mechanism is inactive at LUXE's frequency/geometry/target combination. LUXE testing the QED baseline and validating it is a USEFUL datum that constrains the framework indirectly (by confirming that the QED vacuum behaves normally in the strong-field regime, which the framework's Phononic-C-Causality §2.1 Layer-2 propagation structure already predicts).

### IV.8 What LUXE teaches the framework, regardless of outcome

Any LUXE result is informative for the framework, though in different ways depending on the verdict:

**If LUXE = null (expected UNCONSTRAINED-BY-LUXE)**:
- The framework's structural prediction that nonlinear Breit-Wheeler at optical frequencies does NOT trigger Jensen-sector coupling is consistent with observation.
- The framework's Layer-2 propagation prediction (Phononic-C-Causality §4.4) that "all field-theoretic processes on g_M obey standard QED" is confirmed at χ_γ ≈ 1.
- The framework gains an empirical upper bound on the universal coupling hypothesis: ε_univ (in §IV.6 notation) < 0.3 from the LUXE systematic floor.
- Consequence: the Tesla-Mack village-of-bells experiment remains the relevant direct test, and LUXE's null confirms that non-framework-specific experiments won't accidentally falsify it.

**If LUXE shows a 10-30% excess within systematic (UNCONSTRAINED-MARGINAL)**:
- Most likely interpretation: LUXE TDR baseline is missing a QED correction (higher-order Furry-picture loops, two-loop Ritus-Narozhny, radiative reaction). NOT a framework signature.
- Secondary interpretation: universal coupling ε_univ ~ 0.1-0.3 (small but non-zero). Framework flag for OQ-UV-UNIV-75 computation.
- The two interpretations are discriminable by SHAPE analysis: QED corrections change the differential spectrum predictably, while a universal Bogoliubov coupling would have a distinct signature (framework-specific squeezing pattern in the pair energy distribution). LUXE's differential data would help.

**If LUXE shows a 30-300% excess at 3σ+ (PARTIALLY VALIDATED)**:
- Framework must extend to include a universal a_0 → a_2 coupling. This is not a pre-registered prediction, so it's "partially validated" rather than "pass."
- OQ-UV-UNIV-LUXE-75 becomes the top framework priority: compute the universal coupling coefficient from Heat-Kernel Orthogonality constraints.
- The Tesla-Mack village-of-bells experiment becomes HIGHER priority (easier to falsify the specific mechanism at known geometry/frequency).

**If LUXE shows a 10× excess at 5σ (REFUTED)**:
- The framework's Phononic-C-Causality §4.4 prediction that LUXE sees standard QED is falsified. Substrate-level coupling must be active even without the bell-array conditions.
- Most framework-internal structural theorems (Spectral-Moment Decoupling, Heat-Kernel Orthogonality) survive — they don't directly forbid LUXE enhancement, they just predict the enhancement mechanism is specific.
- The framework's SPECIFIC mechanism ansatz (Leggett branch + BCS target + RF coherent array) is wrong or incomplete. Structural revision required.

**If LUXE shows a LARGE deficit (R < 0.5)**:
- Rare outcome. Most likely interpretation: LUXE's χ_γ ≈ 0.5 interaction-region average overestimates the actual pair production by miscalibrated gamma flux or electron overlap. NOT a framework signature.
- The framework's prediction is ≥ baseline, not ≤ baseline, so a deficit would be particularly puzzling. Framework cannot accommodate a deficit within current ansatz, so R < 0.5 at 5σ is also "REFUTED" (same verdict as large excess, different direction).

### IV.9 What LUXE does NOT test (and why the framework remains falsifiable)

The framework has multiple independent observational channels. LUXE tests ONE of them (strong-field laser QED in vacuum). Other channels:

- **BAO acoustic peak position** (Phononic-C-Causality §8.1, OQ1 LAYER-1-LAYER-2-DIFF-75): discriminates framework vs standard GR on the gapped branches at BAO scale. DESI/Simons data available; not a LUXE-comparable observable.
- **CMB n_s = 0.9561** (framework prediction from acoustic-optical Leggett transfer function): tests the post-transit spectral-tilt signature. Planck/Simons/CMB-S4. Not LUXE-comparable.
- **Dark matter density f_DM ~ 0.3** (Leggett branch inter-band coherence as CDM): Milky Way kinematics, weak lensing, velocity dispersions. Not LUXE-comparable.
- **Village-of-bells laboratory pair production**: the direct analog of LUXE with bell-array + BCS target. This IS a direct framework test and is what the Tesla-Mack workshop is preparing for.
- **RETRO-HAARP archival analysis**: 45 years of operational archives from EISCAT, HAARP, Arecibo, Sura for site-correlated 511 keV anomalies. LOW cost, HIGH information value.
- **LISA gravitational wave stochastic background**: domain-wall collapse during the fold produces a stochastic GW signal at 10⁻¹⁰ relative to H² (prediction from framework memory project_lisa-gw-prediction.md). LISA 2030+ timeline.

LUXE testing null is consistent with most of these independently; LUXE testing anomalous would be discriminable. The framework's overall falsification profile depends on the JOINT constraint from these multiple channels, not on any single experiment. LUXE is ONE data point in that joint profile, and the framework's pre-registration for LUXE is specifically "null expected, because LUXE is not the right experiment for the Jensen-resonance mechanism."

### IV.10 Historical precedent: SLAC E-144 null result

SLAC E-144 (1997) is the historical precursor to LUXE and tested the same nonlinear Breit-Wheeler mechanism at lower ξ (ξ ≈ 0.4) and lower χ (χ ≈ 0.2). E-144 detected **106 ± 14 positrons** (46.6 GeV case) and **22 ± 10 positrons** (49.1 GeV case) above background over ~100 laser shots. The numbers are consistent with pure nBW+LCFA within statistical and systematic uncertainties.

The framework retroactively predicts that E-144 should have seen exactly this: baseline nBW with no anomalous excess. The reasons are identical to the LUXE null argument:
- E-144 wavelength: 1064 nm (Nd:YAG), carrier ~281 THz — 10⁶ above Jensen band.
- E-144 pulse duration: ~1.8 ps — spectral bandwidth ~350 GHz, no RF content.
- E-144 emitter count: 1 (single laser).
- E-144 target: vacuum + 46.6 GeV electrons (no BCS-analog).
- E-144 χ: ~0.2, modest strong-field regime.

All four framework conditions fail at E-144 just as they do at LUXE. The framework's retroactive prediction is therefore E-144 positron rate consistent with standard nBW+LCFA, which is what E-144 observed. **E-144 is a silent corroboration of the framework's null-at-strong-field-optical-QED prediction** — not a "free PASS" (because E-144 was already published before the framework made the prediction), but a consistency check: any framework that retroactively predicted E-144 should see anomalous excess would be refuted by the existing data.

LUXE extends E-144's reach by ~60× in ξ and ~3× in χ_e. The framework's null prediction extrapolates naturally: if E-144 showed no excess at its strong-field conditions, LUXE should show no excess at its stronger-field conditions, both because the Jensen-sector coupling is absent at optical frequencies. The ouroboros: same framework, same mechanism class, same null prediction, but now LUXE is a FORWARD pre-registered test rather than a backward retrocheck.

---

## V. Pre-Registered PASS/FAIL Gate

### V.1 The gate

Let N_obs be the LUXE phase-1 measured positron rate per shot, and let N_base be the LUXE TDR-predicted standard-model (nBW+LCFA) rate with its published ±30% systematic uncertainty envelope. Define the enhancement ratio

    R = N_obs / N_base                                                                     (V.1)

The framework predicts R ≈ 1.000 ± 0.30 (systematic) with any framework contribution buried 10+ orders of magnitude below the systematic floor.

### V.2 Verdict classes

| Verdict | Criterion | Framework Interpretation |
|:--------|:----------|:-------------------------|
| **UNCONSTRAINED-BY-LUXE** (expected outcome, no update to framework status) | 0.7 ≤ R ≤ 1.3 (consistent with baseline within ±30% systematic) | LUXE is spectrally and geometrically incompatible with the Jensen-resonance mechanism; null-consistent result is consistent with all framework predictions including the Tesla-Mack workshop null expectation. No update. |
| **UNCONSTRAINED-BY-LUXE-MARGINAL** | 1.3 < R ≤ 2.0 (mild excess but within 2σ of systematic baseline) | Framework predicts no enhancement; mild excess could be baseline normalization error, pulse-shape systematic, or subdominant QED correction. No framework update; flag for recomputation of baseline. |
| **PARTIALLY VALIDATED** (unexpected outcome) | 2.0 < R ≤ 10 with at least 3σ statistical significance AND a shape analysis consistent with a universal Bogoliubov channel (see §IV.5) | Framework must be EXTENDED to include a universal a_0→a_2 coupling. This is a new pre-registered extension theorem (not currently in the framework). OQ-UV-UNIV-LUXE-75 open. |
| **FRAMEWORK REFUTED AT LUXE** | R > 10 with 5σ statistical significance OR R < 0.7 with 5σ statistical significance (measured rate differs from the baseline by more than 10× upward or by more than 30% downward) | The framework's prediction of NULL enhancement at LUXE is falsified. The framework's current Jensen-resonance-with-BCS-analog-target ansatz is insufficient to explain LUXE's behavior; structural revision required. |
| **AMBIGUOUS** | Systematic-dominated or statistics below 3σ | Not a decisive test; report as statistical-systematic-dominated and defer interpretation. |

### V.3 Statistical requirements

- **UNCONSTRAINED-BY-LUXE**: requires LUXE physics-run statistics ≥ 100 shots at phase-1, with measured positron rate integrated over all shots and compared against LUXE TDR baseline prediction plus ±30% systematic envelope.
- **PARTIALLY VALIDATED** or **REFUTED**: requires 5σ statistical significance for the excess or deficit, with blinded analysis protocol (experimental collaboration should analyze their data against their own TDR prediction first; framework prediction is submitted AHEAD of data release and compared afterward).
- **Blinding protocol**: the framework pre-registration (this document) must be deposited (e.g., on arXiv or timestamped on a framework-specific preprint server) BEFORE the LUXE physics-run data are publicly available. Any post-data-release adjustment of this pre-registration constitutes moving the goalposts and invalidates the result.

### V.4 Significance of null outcome (UNCONSTRAINED-BY-LUXE)

The expected outcome — LUXE measures R ≈ 1 within systematics — is NOT a framework failure. It is consistent with the framework's structural claim that substrate-level pair production requires a specific set of conditions that LUXE does not provide. Reporting this outcome as a "null for the framework" would be misleading.

**The correct reporting for the expected outcome**: "LUXE measured nBW+LCFA positron rates consistent with the standard-model baseline within published systematic uncertainty. This is consistent with the Phonon-Exflation Cosmology framework's pre-registered prediction (this document, 2026-04-11) that the framework's substrate-level Jensen-resonance mechanism is spectrally and geometrically incompatible with LUXE's operating conditions. LUXE therefore does NOT constrain the framework's substrate pair-production prediction. A dedicated village-of-bells experiment with cryogenic BCS-analog target and 10⁴ phase-locked emitters would be the relevant direct test."

This is a legitimate "unconstrained" outcome, distinct from both a PASS (which would require observed enhancement) and a FAIL (which would require the framework to have predicted enhancement and been wrong).

### V.5 Significance of unexpected outcomes

- **PARTIALLY VALIDATED**: this would be a significant unexpected result. It would imply that the framework's Bogoliubov-mediation boundary extends to universal coupling for all strong-field Dirac-operator perturbations, not just the specific Leggett-branch coupling identified in S52 and the Tesla-Mack workshop. The theoretical follow-up would be to compute whether this universality is consistent with the heat-kernel polynomial orthogonality (Phononic-C-Causality §3.5) or requires an exceptional case. OQ-UV-UNIV-LUXE-75 would become the top framework priority.

- **FRAMEWORK REFUTED AT LUXE**: this would force a structural revision of the framework's causality architecture. If LUXE observes R > 10 with 5σ significance and the shape is inconsistent with any universal Bogoliubov coupling, the framework's prediction of frequency/geometry/target-selectivity is wrong, and the entire Phononic-C-Causality §5.5 classification of substrate-level pair production as requiring specific conditions would need to be reconsidered. The framework's current structural theorems (Spectral-Moment Decoupling, Heat-Kernel Orthogonality) would not directly be refuted, but their experimental implications for local pair production would be.

### V.6 Timeline for verdict

LUXE phase-0 commissioning: 2024-2025 (underway). Phase-1 physics runs: 2025-2026. First physics paper from phase-1: estimated Q3 2026 - Q2 2027. Verdict window: within 12-18 months of this document's commit date (2026-04-11), i.e., approximately 2027-Q2 to 2027-Q4.

---

## VI. Dependency on Framework Pre-Computations

The crispness of the LUXE pre-registration depends on the outputs of five pre-registered framework-internal computations from the Tesla-Mack workshop, plus one retrospective-analysis gate. These must return specific values for the LUXE prediction to be quantitatively sharp rather than simply structurally null. The dependencies are:

| Dependency | Role in LUXE prediction | Required output | Current status |
|:-----------|:------------------------|:----------------|:---------------|
| **OQ-TESLA-T1 / JENSEN-EFF-GAP-75** | Determines ω_Leggett,lab (the target Jensen-resonance frequency). Sharpens IV.2.a to a specific frequency (currently nominal 160 MHz). | p ∈ [0.45, 0.55] (sudden-quench regime compatible), ω_Leggett,lab specific within factor 2 | PENDING S75 |
| **OQ-TESLA-T3 / LEGGETT-Q-FACTOR-75** | Determines the resonance width and thus the off-resonance suppression factor in (IV.2). Sharpens the Lorentzian tail of the Jensen-resonance profile at LUXE's operating frequency. | Q_Leggett ∈ [10², 10⁶] at lab conditions | PENDING S75 |
| **OQ-TESLA-T4 / JENSEN-COUPLING-SCALING-75** | Determines the substrate-to-lab coupling scaling exponent. Required for the universal a_0 → a_2 coupling coefficient (IV.5 UV-completion caveat). | Scaling exponent and numerical amplitude | PENDING S75 |
| **OQ-TESLA-T4b / JENSEN-CHI2-CHECK-75** | Determines whether parametric driving is available at LUXE (χ² or χ³ nonlinearity). Bears on the parametric-down-conversion check in IV.2.a. | Yes or no on χ² in isotropic/confined geometry | PENDING S75 |
| **OQ-TESLA-T4c / JENSEN-KERR-75** | Determines the Kerr coefficient for parametric gain in a χ³-only regime. Bears on the universality hypothesis in IV.5. | χ_K at tau_fold on D_K eigenvalue derivatives | PENDING S75 |
| **OQ-TESLA-RETRO-HAARP-75** | Retrospective archival analysis of existing phased-array facilities for site-correlated 511 keV anomalies. Provides an empirical upper bound on the universal-coupling hypothesis. | Q > 10³ or Q > 10⁶ from 45-year EISCAT/HAARP operational archives | PENDING S75 |
| **OQ-MACK-BOGOLIUBOV-BOUNDARY-75** | Candidate theorem for Bogoliubov-mediation at emergence boundaries. Provides the structural foundation for claim IV.1 that substrate pair production requires all four conditions simultaneously. | Structural theorem with Gilkey-orthogonality certificate | PENDING S75 |

**What changes if the dependencies return differently than expected:**

- If **T1 returns p ≠ 1/2** (i.e., the framework's lab-projection scaling is different from Bogoliubov-mediated sqrt-scaling), the Jensen-resonance target frequency may shift by orders of magnitude, and §IV.2.a's numerical arguments would need to be revised. The structural null-at-LUXE argument might still hold if the new target is still in RF/MHz band, but the specific suppression numbers would change.

- If **T3 returns Q < 100**, the resonance is broad, and the off-resonance suppression at LUXE is weaker. At Q ≈ 1 (no selectivity), LUXE's laser could in principle drive the Jensen sector directly, but this would also imply that the cosmological fold's 59.8-pair result is a broadband response — inconsistent with the sharp squeezing pattern from S38. So T3 PASS at Q ≥ 10³ is effectively required for the LUXE null prediction to be robust.

- If **RETRO-HAARP returns PASS** (anomaly found in archival EISCAT/HAARP data), then the framework already has evidence from existing coherent-emitter experiments, and LUXE's role as a "primary test" is diminished. The framework would then predict LUXE sees enhancement IF the HAARP anomaly is indicative of a universal coupling, or sees null IF the HAARP anomaly is specific to the ionospheric target. Both outcomes would require post-RETRO-HAARP framework updating.

- If **OQ-MACK-BOGOLIUBOV-BOUNDARY-75 FAILS** (the candidate theorem is not rigorously derivable from Gilkey orthogonality), then the framework's structural claim that Jensen-resonance pair production is specific to BCS-analog targets is weakened, and the universality hypothesis of §IV.5 becomes more plausible. The LUXE prediction would shift from "UNCONSTRAINED-BY-LUXE" to "uncertain" pending UV-completion clarification.

**Bottom line**: this pre-registration is anchored on the PENDING pre-computations. It is "sharp" in its structural prediction (null enhancement at LUXE) but "soft" in its quantitative enhancement bounds until the Tesla-Mack gates return. I commit to this structural prediction NOW on the condition that S75 run the five OQ-TESLA gates in parallel. If any gate returns unfavorably (specifically RETRO-HAARP PASS or BOGOLIUBOV-BOUNDARY FAIL), I commit to depositing a REVISED pre-registration ahead of LUXE physics-run data release.

---

## VII. Timeline and Action Items

### VII.1 Actions before LUXE physics-run data release

| # | Action | Who | Input | Output | Format | Deadline | Depends on |
|:-:|:-------|:----|:------|:-------|:-------|:---------|:-----------|
| 1 | Deposit this pre-registration on arXiv as a framework-specific LUXE prediction preprint | User/framework team | This document | Timestamped arXiv preprint with DOI | arXiv submission | 2026-05-15 | None (this document) |
| 2 | Notify LUXE collaboration of the pre-registration and request inclusion in their reference list for phase-1 physics papers | User/framework team | arXiv preprint from (1) | Acknowledgment from LUXE collaboration | Email + DESY contact | 2026-06-15 | Action 1 complete |
| 3 | Run OQ-TESLA-T1 / JENSEN-EFF-GAP-75 in S75 computation | computation compute team | D_K spectrum at tau_fold, Leggett projection, BCS-embedding parameters | Scaling exponent p and quench ratio τ_drive/T_Leggett | computation npz output | 2026-06-01 | S75 session plan |
| 4 | Run OQ-TESLA-T3 / LEGGETT-Q-FACTOR-75 in S75 computation | computation compute team | D_K spectrum + BCS dispersion + scattering estimates | Q_Leggett at lab density conditions | computation npz output | 2026-06-01 | S75 session plan |
| 5 | Run OQ-TESLA-T4 / JENSEN-COUPLING-SCALING-75 in S75 computation | computation compute team | D_K spectrum, BCS embedding | Coupling strength and scaling | computation npz output | 2026-06-01 | S75 session plan |
| 6 | Run OQ-TESLA-T4b / JENSEN-CHI2-CHECK-75 in S75 computation | computation compute team | D_K + symmetry analysis | χ² nonlinearity status | computation npz output | 2026-06-01 | S75 session plan |
| 7 | Run OQ-TESLA-T4c / JENSEN-KERR-75 in S75 computation | computation compute team | D_K eigenvalue derivatives d omega_L1/d n_L1 | Kerr coefficient and dissipation ratio | computation npz output | 2026-06-01 | S75 session plan |
| 8 | Run OQ-TESLA-RETRO-HAARP-75 archival analysis | Archival analyst / Mack team | EISCAT, HAARP, Fermi LAT, KAGRA, MAXI archival data | Site-correlated 511 keV upper bound | Analysis report + any anomalies | 2026-08-01 | S75 session plan |
| 9 | Prove OQ-MACK-BOGOLIUBOV-BOUNDARY-75 structural theorem | Theorist team | Phononic-C-Causality §3.1(iv), Gilkey 1995 | Proof certificate with regime of validity | Framework theorem document | 2026-07-01 | S75 session plan |
| 10 | Revise this pre-registration if any pending gate returns unfavorable | Feynman-Theorist + user | Gate outcomes | Updated pre-registration (if needed) | Markdown edit + arXiv v2 | Before LUXE first physics paper | Gates 3-9 complete |

### VII.2 Actions after LUXE physics-run data release

| # | Action | Who | Input | Output | Format | Deadline | Depends on |
|:-:|:-------|:----|:------|:-------|:-------|:---------|:-----------|
| 11 | Read LUXE phase-1 physics paper(s) within 2 weeks of release | Feynman-Theorist | LUXE published papers | Summary of observed R ratio | Framework internal note | ≤ 2 weeks after LUXE publication | LUXE publishes |
| 12 | Classify LUXE outcome against V.2 verdict table | Feynman-Theorist + user | LUXE result + this pre-registration | Verdict classification (UNCONSTRAINED/PARTIAL/REFUTED) | Framework gate verdict | ≤ 1 month after LUXE publication | Action 11 |
| 13 | If verdict is PARTIALLY VALIDATED or REFUTED, convene dedicated session for framework revision | Framework team | Verdict + LUXE data | Revised framework prediction ansatz | New session artifact | ≤ 3 months after LUXE publication | Action 12 if triggered |
| 14 | If verdict is UNCONSTRAINED-BY-LUXE, publish verdict in framework's open-record and continue to the village-of-bells direct test | Framework team | Verdict | Updated framework status | Framework status update | ≤ 1 month after Action 12 | Action 12 |

### VII.3 Risks and mitigations

- **Risk**: LUXE delays beyond 2027. **Mitigation**: pre-registration remains valid until physics runs begin; no action required.
- **Risk**: LUXE uses pulse shapes/geometries not specified in the TDR (e.g., multiple lasers in interaction point). **Mitigation**: re-examine whether any framework-relevant coupling (parametric down-conversion, beat notes at Jensen frequency, etc.) is enabled by the specific geometry, and revise prediction if needed.
- **Risk**: Framework pre-computations (Tesla OQ-TESLA-T1 etc.) return results that change the quantitative prediction substantially. **Mitigation**: deposit a revised pre-registration (v2) BEFORE LUXE physics-run data release.
- **Risk**: LUXE reports systematic dominance and cannot decisively compare to the baseline. **Mitigation**: this is the AMBIGUOUS verdict class; framework treats as null-informative and waits for better statistics or upgraded LUXE runs.

---

## VIII. Closing Line

**If the Phonon-Exflation Cosmology framework is correct as currently formulated, LUXE will measure e⁺e⁻ pair production rates consistent with standard nonlinear Breit-Wheeler QED within its published systematic uncertainty; any framework-specific enhancement above this baseline would REFUTE the framework's current Jensen-resonance-with-BCS-analog-target ansatz, because LUXE lacks the frequency overlap, the coherent emitter geometry, the sudden-quench spectral content, and the BCS-analog target that the framework requires for its substrate-level pair production mechanism to operate.**

---

## IX. References

### IX.1 Framework internal documents

- `sessions/framework/Phononic-C-Causality.md` — canonical causality framework document, §3.1 (Spectral-Moment Decoupling Theorem with Gilkey proof), §3.5 (Heat-Kernel Polynomial Orthogonality), §5.5 (Bogoliubov pair production classification as SUBSTRATE DYNAMICS), §8 (observational consequences)
- `sessions/archive/session-74/session-74-tesla-mack-bells-workshop.md` — Tesla × Mack village-of-bells workshop, full protocol for dedicated framework pair-production experiment
  - T1 (Jensen resonance frequency computation; pre-registration of OQ-TESLA-T1)
  - T2 (village-of-bells geometry; N² coherent enhancement; emitter-shell design)
  - T3 (laser specs; master-slave phase locking; envelope vs carrier coherence)
  - T4 (acoustic modulation; Leggett branch as the Jensen-sector carrier; χ² vs χ³ parametric coupling)
  - T5 (energy budget; r_local = 1.5 to 3.5 target range)
  - Mack R1-B, R2-B (observational rigor; sudden-quench requirement; frequency-scan Control 2)
  - Round 2 CONVERGENCE block (Bogoliubov-mediated a_0 → a_2 coupling is framework-licensed by Phononic-C-Causality §3.1(iv))
  - Round 2 EMERGENCE (RETRO-HAARP-75, EISCAT_3D-75)
- `sessions/archive/session-74/session-74-rf-analysis.md` — RF / coherent-array retrospective-analysis dossier, Category 4 (laser-based strong-field pair production), Lead 4b (LUXE) is the primary reference for this pre-registration

### IX.2 LUXE experiment

- **LUXE Collaboration** (2024). *Eur. Phys. J. Spec. Top.*, "Technical Design Report for the LUXE experiment." https://link.springer.com/article/10.1140/epjs/s11734-024-01164-9
- **LUXE Collaboration** (2019). arXiv:1909.00860, "Letter of Intent for the LUXE Experiment." https://ar5iv.labs.arxiv.org/html/1909.00860
- **Abramowicz, H. et al. (LUXE)** (2021). arXiv:2102.02032, "Conceptual Design Report for the LUXE Experiment."
- LUXE experiment documents: https://luxe.desy.de/documents/index_eng.html

### IX.3 QED background and standard-baseline theory

- **Ritus, V. I.** (1985). "Quantum effects of the interaction of elementary particles with an intense electromagnetic field." *J. Sov. Laser Research* 6, 497.
- **Nikishov, A. I., Ritus, V. I.** (1964). "Quantum processes in the field of a plane electromagnetic wave and in a constant field." *Sov. Phys. JETP* 19, 529.
- **Schwinger, J.** (1951). "On gauge invariance and vacuum polarization." *Phys. Rev.* 82, 664.
- **Baier, V. N., Katkov, V. M., Strakhovenko, V. M.** (1998). *Electromagnetic Processes at High Energies in Oriented Single Crystals*. World Scientific.
- **Di Piazza, A., Müller, C., Hatsagortsyan, K. Z., Keitel, C. H.** (2012). "Extremely high-intensity laser interactions with fundamental quantum systems." *Rev. Mod. Phys.* 84, 1177.
- **Furry, W. H.** (1951). "On bound states and scattering in positron theory." *Phys. Rev.* 81, 115.
- **Volkov, D. M.** (1935). "Über eine Klasse von Lösungen der Diracschen Gleichung." *Z. Phys.* 94, 250.

### IX.4 SLAC E-144 (the direct precursor)

- **Bamber, C. et al. (E-144 collaboration)** (1999). "Studies of nonlinear QED in collisions of 46.6 GeV electrons with intense laser pulses." *Phys. Rev. D* 60, 092004. https://www.slac.stanford.edu/exp/e144/ps/prdmainkk.pdf
- **Burke, D. L. et al.** (1997). "Positron Production in Multiphoton Light-by-Light Scattering." *Phys. Rev. Lett.* 79, 1626.

### IX.5 Feynman library (agent grounding)

- 02_1949_Feynman_Theory_of_positrons.md — the positron as a backward-propagating electron, basis of the Furry-picture treatment
- 03_1949_Feynman_Space_time_approach_to_QED.md — diagrammatic rules used to compute the Volkov-electron amplitude (III.3)
- 04_1950_Feynman_Mathematical_formulation_of_QED.md — explicit amplitude calculation
- 11_1948_Schwinger_Quantum_electrodynamics_I.md — the covariant formulation of QED in an external field (Furry picture foundation)
- 12_1949_Dyson_Radiation_theories_of_Tomonaga_Schwinger_Feynman.md — the equivalence of operator and diagrammatic approaches

### IX.6 Canonical framework constants (loaded from `computations/canonical_constants.py`)

- M_KK_gravity = 7.4286e16 GeV — the substrate's intrinsic energy scale (gravity route, S42)
- tau_fold = 0.19 — Jensen modulus at the van Hove fold
- omega_L1 = 0.138 M_KK — Leggett-1 frequency (substrate scale), nominal Jensen-sector carrier for lab projection
- c_Gold = 0.915 M_KK — Goldstone sound speed, emergent speed of light
- r_B1 = 3.571 — cosmological Bogoliubov squeezing parameter at the fold (S38)
- n_pair = 59.8 — cosmological pair count per fold event (S38)
- E_cr = m_e²c³/(eℏ) = 1.32 × 10¹⁸ V/m — Schwinger critical field, standard QED
- alpha_em ≈ 1/137 — fine-structure constant at low energy, used in (III.4)
- m_e c² = 0.511 MeV — electron rest mass

---

## X. Locking Clause

**This pre-registration is FROZEN at the commit date 2026-04-11. Any subsequent modification must be made in a versioned v2, v3, etc., with a clear statement of what changed and why, AND must be deposited (arXiv or equivalent timestamped record) BEFORE LUXE physics-run data are publicly available. Modifications made AFTER LUXE data release constitute moving the goalposts and invalidate the pre-registration's epistemic status.** The version shown here is v1.

Signed: Feynman-Theorist, acting as the framework's computational / QED representative.
Under the authority: Phonon-Exflation Cosmology project, user-directed.
Session: S74, 2026-04-11.
Status: LOCKED.

---

*End of pre-registration document.*
