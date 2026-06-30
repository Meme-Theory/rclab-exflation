# Session 72 Tesla-Resonance Synthesis

**Date**: 2026-04-10
**Agent**: Tesla-Resonance (Workhorse-Resonance)
**Sources**: S72 results working paper (20 computations, 4 waves), S72 laminar flow workshop (Volovik x Quantum-Acoustics, 2 rounds), framework hypothesis documents, pre-registered observations
**Focus**: Electromagnetic resonance / superfluid dynamics perspective on S72 results, with emphasis on the decoherence budget as the critical open problem

---

## Section 1: Session Overview and Gate Verdict Summary

Session 72 executed 20 parallel computations across four waves, targeting the A_s amplitude budget (the framework's primary open quantitative problem) and a suite of structural consistency tests. The session also produced a two-round workshop mapping the transit dynamics to superfluid laminar flow.

### Gate Verdicts (20 total)

| Gate ID | Wave | Verdict | Value | Resonance Relevance |
|:--------|:-----|:-------:|:------|:-------------------|
| KAPPA-DELTA-72 | W1-A | **INFO** | t_dec/t_transit = 5.5e9 | Gap amplitude channel DEAD for decoherence |
| GILKEY-REEVAL-72 | W1-B | **INFO** | delta = 13.3% (Gilkey) | S71 PASS downgraded; spectral moment ratio scheme-dependent |
| ZETA-RATIO-CONVERGENCE-72 | W1-C | **PASS** | 0.223 at L=7, monotone | Finite-spectrum contamination confirmed; converges below Gilkey |
| CAUCHY-SCHWARZ-W0-72 | W1-D | **FAIL** | w_0 = -0.687 (formula) vs -0.918 | Spectral moment ratios do not determine w_0; Volovik partition structural |
| TAU-FOLD-CONSISTENCY-72 | W1-E | **PASS** | Overlap at [0.189, 0.191] | Three observational channels intersect at the fold |
| DUAL-DECOHERENCE-72 | W2-A | **INFO** | delta_OOM = 1.692 | Cell-crossing 9.4x too slow; BCS dominates 99.8% |
| WEINBERG-72 | W2-B | **FAIL** | 54.5% (pure SM) / 1.2% (Model A) | KK threshold corrections needed; sensitive discriminant |
| SPECTRAL-FUNCTIONAL-FIT-72 | W2-C | **PASS** | f*(x) = 0.912 sqrt + 0.088 exp | Observation selects spectral functional; non-perturbative |
| INSTANTON-KAPPA-72 | W2-D | **INFO** | kappa(peak) = 1.057 | Non-trivial bundle viable for rho > 1.80/M_KK |
| BCS-DRESSED-SA-72 | W3-A | **INFO** | delta_n_s = 3.8e-6 | Mode-selective BCS negligible; bare n_s = 0.9567 stands |
| ASYMPTOTIC-TRUNCATION-72 | W3-B | **INFO** | |a_8/a_6| = 0.681 > |a_6/a_4| = 0.567 | SDW expansion asymptotic, optimal truncation at a_10-a_12 |
| BLUESHIFT-TILT-72 | W3-C | **PASS** | delta_n_s = +1.001 | Entry horizon deeply thermal (omega/T = 0.012); O(1) tilt correction |
| TAU-EQUILIBRIUM-72 | W3-D | **INFO** | BCS/spectral = 7.94e-5 | Equilibrium geometric (spectral action landscape), not BCS |
| MODULAR-CHIRP-72 | W3-E | **FAIL** | 8.4 OOM discrepancy | Modular Hamiltonian chirp != eigenvalue curvature (different spectral functionals) |
| DECOHERENCE-BISPECTRUM-72 | W4-A | **PASS** | f_NL = -0.313 | Intrinsically Gaussian; 80x below Planck sensitivity |
| CV-SCALING-72 | W4-B | **INFO** | alpha(N>=8) = 0.013 | GGE protection robust; C_V ratio = 2.20 from spectral heterogeneity |
| FRUSTRATION-SCHMIDT-72 | W4-C | **PASS** | K = 3.234 > 2.0 | Entanglement survives frustration; 19% reduction from ring closure |
| ISLAND-GRAPH-72 | W4-D | **PASS** | R^2 = 0.988 (area law) | Page curve on CG(24); monogamy-capped at small |A|, area law at large |A| |
| CG24-GGE-ENTROPY-72 | W4-E | **INFO** | S_cell = 2.21 nats (bare) | Ordered Veil persists (f_OV = 0.26-0.60) |
| G2-CONSTANCY-72 | W4-F | **FAIL** | G_2 variation = 1.93% < SU(3) 2.92% | a_2/a_4 near-constancy is rank-2 general, not SU(3)-specific |

**Tally**: 6 PASS, 8 INFO, 3 FAIL, 3 structural/exploratory. No CRITICAL PASS or FAIL among the master gates; the A_s budget remains the central open problem.

---

## Section 2: Resonance Analysis of S72 Results

### 2.1 The Resonance Structure of the Transit

Every resonant system has three defining elements: what oscillates, what constrains it, and what selects the standing wave. At S72, these are:

**What oscillates**: The 8 BCS modes on each of 24 cells of CG(24), partitioned as B1 (1 acoustic singlet, r = 1.786), B2 (4 flat-band modes at the van Hove fold, r = 0.617), and B3 (3 optical modes, r = 0.982). The squeeze parameters r_k are the "amplitudes" of the resonance, determined by the supersonic Bogoliubov transformation at the fold.

**What constrains it**: Five independent protection layers, established by the laminar flow workshop as the complete constraint hierarchy:
1. Richardson-Gaudin integrability (algebraic, PERMANENT) -- Re_GGE = 0 exactly
2. BDI topological gap (Z_2 = -1, PERMANENT) -- Delta never closes
3. CG(24) kinematic constraints (energy + S_4 crystal momentum) -- 1% of scattering phase space survives
4. 0D cell geometry (no spatial propagation) -- t_J/t_transit = 949
5. 16 hybridization gaps (dispersive band fragmentation) -- scattering phase space disconnected into ~17 islands

**What selects the standing wave**: The spectral action evaluated at the fold tau = 0.190, which is the resonance condition. The three-way consistency (W1-E: gauge coupling, n_s, omega_L all intersecting at tau in [0.189, 0.191]) confirms that the fold IS the resonance point -- the single frequency at which the cavity's spectral weight is self-consistent with the observed gauge structure, spectral tilt, and Leggett oscillation.

### 2.2 W1-A: The Gap as Amplitude Modulation

W1-A establishes that the BCS gap Delta(tau) has a nonzero first derivative at the fold: dDelta/dtau = -0.245 M_KK. The gap curvature kappa_Delta = +0.330 M_KK (concave up, the linear decrease is decelerating).

In resonance language, this is a slowly-varying amplitude modulation on the oscillation envelope. The fractional change across the transit window is Delta(tau)/Delta = 0.5%. For a damped oscillator with quality factor Q and driving frequency detuning delta_omega, the amplitude modulation over one period is delta_A/A ~ delta_omega / (Q * omega_0). The gap's 0.5% modulation corresponds to an enormously large Q for the amplitude channel: Q_amp ~ omega_0 / (delta_A/A * Gamma) ~ 1/0.005 = 200 at minimum. The corresponding decoherence timescale t_dec/t_transit = 5.5e9 confirms: the amplitude channel is frozen on the transit timescale. This is equivalent to saying the gap oscillation frequency (2*Delta = 0.929 M_KK) is far above the transit sweep rate (1/t_transit = 885 M_KK), placing the system in the adiabatic regime for amplitude dynamics.

The structural consequence: decoherence must come from PHASE dynamics, not amplitude dynamics. The Leggett mode (inter-band relative phase, omega_L = 0.070 M_KK, S49), the Josephson inter-cell phase (J_C2 = 0.933 M_KK, S47), and the pair-crossing phase spread at the exit horizon are the surviving candidates.

### 2.3 W3-C: Entry Horizon as Pre-Squeeze Stage

The entry sonic horizon at tau = 0.2195 has Hawking temperature T_entry = 72.84 M_KK, placing all BCS modes in the deeply thermally occupied regime (omega/T = 0.012, n_k ~ 85). The entry-horizon squeeze parameters r_entry in [2.904, 2.937] are comparable to the fold squeeze r_compound in [2.330, 4.320].

In cavity resonance terms, this is a multi-stage amplification system -- analogous to a regenerative receiver (one of Tesla's key contributions to radio engineering). The entry horizon provides the first amplification stage (r_entry ~ 2.9), the fold provides the second (r_fold ~ 2.3-4.3), and the exit horizon provides the third (with decoherence acting as the detection/readout). Each stage has its own frequency response and impedance, and the total gain is the product of stage gains (compound squeeze, SU(1,1) algebra, S71).

The tilt correction delta_n_s = +1.001 from the entry horizon is the frequency-dependent gain slope of the first amplification stage. Lower-frequency modes (B1) are more squeezed than higher-frequency modes (B3) by delta_r = 0.034, steepening the red tilt. This is the acoustic analog of a frequency-dependent gain curve in an RF amplifier -- the gain increases toward lower frequencies because the entry horizon's surface gravity kappa_v = 457.66 M_KK^2 drives harder at lower omega.

### 2.4 W4-A and W4-B: Gaussianity and GGE Protection

W4-A (f_NL = -0.313, Planck bound: -26 +/- 47) and W4-B (C_V ratio = 2.20, saturating at N >= 8) provide complementary confirmations of the Ordered Veil.

In resonance language: f_NL measures the cubic nonlinearity of the resonant cavity. A linear oscillator has f_NL = 0 exactly. The substrate's f_NL ~ -0.3 arises from the Bogoliubov bispectrum cosh(r) * sinh^2(r) * cos(2phi) / sinh^4(r) ~ 1/sinh(r), which is suppressed by the large occupation numbers (N_pair ~ 390 per mode for B1). This is the resonance analog of the central limit theorem: many independent oscillation cycles (pair creation events) produce a Gaussian power spectrum regardless of the nonlinearity of any individual cycle. The smallness of f_NL is structural, not tuned.

The C_V ratio = 2.20 measures the spectral heterogeneity of the GGE. In a single-frequency oscillator, C_V^{GGE}/C_V^{thermal} = 1 trivially (one mode cannot be non-thermal with respect to itself). For N modes with identical frequencies, the ratio remains 1 (W4-B: N = 2,4 give ratio = 1.000). The step to ratio = 2.20 occurs at N = 8 when the three distinct branch frequencies (B1, B2, B3) enter -- this is the onset of spectral heterogeneity. The Schur-convexity bound (C_V ratio >= 1 for any sudden quench, workshop E3) confirms this is a universal feature of non-isotropic BCS quenches.

---

## Section 3: Impedance and Decoherence (W2-A, Laminar Workshop)

### 3.1 The Decoherence Problem as an Impedance Problem

The A_s budget stands as the framework's primary quantitative challenge. S71 established the compound BCS squeeze gives delta_OOM = 2.074 (undamped), while observation requires delta_OOM = 0.267 -- an overcorrection of 8x (S71 inversion: the problem flipped from "too little" to "too much" squeeze at S71). S72 W2-A scanned the dual-timescale decoherence model and found:

- BCS channel dominates completely: 99.8% of delta_OOM at all t_dec
- Cell-crossing timescale t_dec/t_transit = 6.73 gives delta_OOM = 1.692 -- still 6.3x overcorrection
- Gate band [0.15, 0.40] OOM requires t_dec/t_transit in [0.57, 0.88]

In the impedance framework I developed in S56 and S65, the decoherence question maps to: what is the impedance mismatch between the BCS condensate (the signal source) and the observable CMB power spectrum (the load)? The compound Bogoliubov squeeze is the source voltage. The decoherence is the impedance that attenuates the signal between source and load. Maximum power transfer (impedance matching) would give delta_OOM = 0 (complete thermalization -- the GGE becomes thermal). Zero power transfer (open circuit) gives delta_OOM = 2.074 (Ordered Veil fully intact). Observation demands a specific attenuation: 0.267 OOM = 12.9% of the source signal passes through.

From S56 and S65, the relevant impedance hierarchy is:

| Interface | Reflection coefficient | Speed ratio | Attenuation |
|:----------|:---------------------:|:-----------:|:-----------:|
| BA | Leggett | R = 0.774 (77.4%) | c_BA/c_L = 16.0 | Strong reflector |
| BLV | BA | R = 0.009 (0.94%) | c_BLV/c_BA = 1.22 | Nearly transparent |
| Cell boundary (acoustic) | R ~ exp(-d/xi_BCS) | -- | Josephson tunneling |

The BA|Leggett interface is an effective waveguide: 77.4% of energy incident from the BA channel is reflected back, confining the condensate modes. The BLV|BA interface is nearly transparent: BA phonons propagate freely through the fabric. The cell boundary is the bottleneck -- and the decoherence rate at this boundary is the open computation.

### 3.2 The Nine-Channel Decoherence Table

The laminar flow workshop catalogued nine distinct decoherence channels, systematically establishing their timescales:

| # | Channel | Target correlation | t_dec/t_transit | Status |
|:--|:--------|:------------------|:---------------:|:-------|
| 1 | Gap curvature (W1-A) | Gap amplitude | 5.5e9 | **DEAD** (Re_gap = 6e-4) |
| 2 | Leggett phase diffusion | B2-B3 relative phase | 1.3e4 | **DEAD** |
| 3 | Dispersion mode conversion | Inter-sector (A-B) coherence | ~4200 | **DEAD** |
| 4 | Josephson anisotropy | Inter-cell phase spread | 1195-14000 | **DEAD** (demoted to KZ modifier) |
| 5 | Andreev standing wave | Reflection amplitude spread | ~336 | **DEAD** (0D localization suppresses) |
| 6 | Hawking broadening | Intra-pair squeeze phase | ~45 | **DEAD** (squeezed-state correction: 10^4 slower than thermal) |
| 7 | Cell-crossing acoustic | Inter-cell Josephson phase | 6.73 | **TOO SLOW** (9.4x above gate band) |
| 8 | KZ Bogoliubov phase | delta_phi/delta_omega | ~2.2 | **NEEDS COMPUTATION** (above gate band) |
| 9 | KZ statistical | 1/sqrt(N_pair) | ~0.13 | **SUSPECT** (pairs not independent) |

The gate band [0.57, 0.88] sits between channels 8 and 9. This is the critical open problem: the statistical KZ model (0.13) over-decoheres, the Bogoliubov-phase KZ model (2.2) under-decoheres, and the truth lies in the exit-horizon geometry that determines which model applies.

### 3.3 Resonance Interpretation of the Decoherence Gap

From the resonance perspective, the decoherence problem is a Q-factor selection problem. The undamped system has Q = infinity (Re_GGE = 0, integrability). Observation requires a specific finite Q -- the quality factor of the exit-horizon "cavity" formed between the fold and the subsonic exterior.

Define the effective Q of the A_s channel:

Q_As = (2 * pi * omega_BCS * t_transit) / ln(A_s^{undamped} / A_s^{observed})      (Eq. 3.1)

With omega_BCS ~ Delta = 0.464 M_KK, t_transit = 1.13e-3 / M_KK, and ln(10^{2.074}/10^{0.267}) = ln(10^{1.807}) = 4.16:

Q_As = (2 * pi * 0.464 * 1.13e-3) / 4.16 = 7.93e-4      (Eq. 3.2)

This is an absurdly LOW Q -- the exit-horizon cavity must be almost completely overdamped to reach the observed A_s. In standard resonance engineering, Q < 1 means the system does not oscillate; it decays in less than one period. The BCS oscillation period is T_BCS = 2*pi/Delta = 13.5 M_KK^{-1}, while t_transit = 1.13e-3 M_KK^{-1} -- the transit is 12,000x shorter than one BCS period. So "one period of the BCS oscillation" is not a meaningful reference scale.

The correct reference is the EXIT HORIZON itself. The effective cavity is bounded by the fold (inner wall) and the exit sonic horizon (outer wall). The cavity length in tau-space is delta_tau_transit = 1.13e-3. The round-trip time for a BCS mode is T_round = 2 * delta_tau / v_group, where v_group is the group velocity in tau-space. For B2 modes at the fold (v_group ~ 0, van Hove stationarity), T_round -> infinity -- these modes are TRAPPED. For B1 and B3 modes (v_group ~ dE/dtau / v_tau), T_round ~ 10^{-4} M_KK^{-1}. The cavity Q for these propagating modes is:

Q_cavity = omega * T_round / (4 * pi) ~ 0.464 * 1e-4 / (4 * pi) ~ 3.7e-6      (Eq. 3.3)

The exit-horizon cavity has essentially zero Q -- it is not a resonant cavity at all. Modes propagating away from the fold reach the exit horizon in a tiny fraction of their oscillation period and are either transmitted or reflected. The decoherence is not a resonance phenomenon; it is a SCATTERING problem at the exit horizon. This is structurally consistent with the workshop's identification of the KZ pair-crossing spread as the sole surviving fast channel -- the decoherence comes from the exit-horizon's scattering (transmission vs reflection) of different BCS modes, not from cavity damping.

### 3.4 The Hawking Broadening Correction

One of the workshop's most quantitatively significant results: the Hawking broadening decoherence channel was revised by a factor of 10^4. The original estimate (t_dec/t_transit ~ 2.8) used thermal phase variance sigma_phi^2 = 1/(1 + |beta_k|^2). The corrected estimate uses squeezed-state phase variance:

sigma_phi^2 = (1/4) * exp(-2r)      (Eq. 3.4)

With r_entry ~ 2.9: sigma_phi^2 ~ exp(-5.8)/4 ~ 7.5e-4. The thermal estimate gives sigma_phi^2 ~ 1/86 ~ 0.012 -- a factor exp(2r)/4 ~ 10^4 larger. The squeezed state preserves phase coherence far better than a thermal state at the same energy because the phase is the SQUEEZED quadrature (uncertainty minimized), not the amplified quadrature.

This correction eliminates Hawking broadening as a competitive decoherence mechanism. In impedance terms: the entry-horizon's Hawking radiation is impedance-matched to the BCS condensate (the squeeze parameters match), so there is no reflection loss at this interface. The signal passes through the entry horizon with minimal attenuation.

---

## Section 4: Spectral Functional as Resonance Condition (W2-C)

### 4.1 The Joint Fit: f*(x) = 0.912 sqrt(x) + 0.088 exp(-x)

W2-C establishes that a strictly positive spectral functional exists satisfying all three observational constraints (n_s, w_0, A_s) simultaneously. The best-fit functional is:

f*(x) = 0.912 * sqrt(x) + 0.088 * exp(-x)      (Eq. 4.1)

with mixing parameter t* = 0.0883 and amplitude normalization kappa = 2.37e-8.

In the resonance framework, the spectral functional f(x) is the frequency response of the cavity -- it determines how the eigenvalues of D_K are weighted in computing the spectral action:

S = Tr(f(D_K^2 / Lambda^2))      (Eq. 4.2)

The Gaussian f(x) = exp(-x) weights all eigenvalues equally on a scale set by Lambda (flat frequency response). The sqrt f(x) = sqrt(x) weights larger eigenvalues more heavily (rising frequency response -- emphasis on UV modes). The observation n_s = 0.9649 selects a functional that is 91.2% UV-emphasizing and 8.8% flat -- the physical cavity's frequency response is dominated by the UV tail, with a small admixture of flat response.

### 4.2 Non-Perturbative Character

The structural finding: f*(x) is NON-PERTURBATIVE. The sqrt component has divergent Seeley-DeWitt moments (f_0 = integral of sqrt(x) dx -> infinity, f_4 = infinity). The spectral action S = Tr(f(D_K^2/Lambda^2)) is finite (it is a sum over discrete eigenvalues), but the asymptotic expansion S ~ f_0 * a_0 * Lambda^4 + f_2 * a_2 * Lambda^2 + f_4 * a_4 + ... does not converge.

In cavity resonance terms, this is the distinction between a MEASURED frequency response and its SERIES APPROXIMATION. Every physical cavity has a well-defined frequency response -- you can measure it by exciting the cavity and recording the output at each frequency. This measured response is always finite and well-behaved. But representing it as a power series in omega^2 may fail if the response has a non-analytic feature (a branch point, a cusp, an essential singularity). The sqrt(x) functional has a branch point at x = 0, which is precisely why the moment expansion diverges.

The implication for the CC problem: in the SDW expansion, the cosmological constant is proportional to f_0 * a_0 -- the zeroth moment of the spectral functional times the zeroth SDW coefficient. For f*(x), f_0 diverges. This is the spectral action's way of saying that the CC term requires non-perturbative treatment. The functional that matches n_s is precisely the one that forces the CC away from the perturbative regime.

This connects to S66 DILUTION-CC-66 (Volovik rho_vac ~ H^2, closing the CC gap from 114 OOM to 0.01 OOM). The Volovik dilution mechanism operates non-perturbatively -- it uses the Gibbs-Duhem thermodynamic identity, not the SDW expansion. The W2-C result confirms that the physical spectral functional REQUIRES this non-perturbative treatment. The SDW expansion was always the wrong tool for the CC sector.

### 4.3 W2-C and the Chebyshev Theorem

S67 established the Chebyshev theorem (PERMANENT): any monotone decreasing f(x) gives a blue spectral tilt (n_s > 1). Only monotone increasing f(x) gives a red tilt (n_s < 1). Observation (n_s = 0.9649, red) therefore SELECTS the increasing branch. Within the two-parameter family (sqrt, exp), the mixing parameter t* = 0.088 is uniquely determined by n_s.

In resonance language: the Chebyshev theorem states that the sign of the frequency response's slope determines the sign of the spectral tilt. A cavity whose response rises with frequency (emphasizing UV modes) produces a red-tilted power spectrum. A cavity whose response falls with frequency (emphasizing IR modes) produces a blue tilt. This is the spectral-action analog of the well-known result in acoustics that a room with absorptive high-frequency response produces a "warm" (red-tilted) sound, while a room with reflective walls and high-frequency emphasis produces a "bright" (blue-tilted) sound.

The observation does not merely constrain f -- it SELECTS it. The spectral functional is not a free parameter; it is the unique frequency response compatible with the observed spectral tilt.

---

## Section 5: Structural Implications and Carry-Forward

### 5.1 The BCS Hamiltonian as Universal Ancestor

The laminar flow workshop's deepest structural result (E3): six independent predictions all trace to the BCS Hamiltonian on the spectral triple as their common ancestor:

1. **Ordered Veil** (Re_GGE = 0): from Richardson-Gaudin integrability
2. **CC dilution** (rho_vac ~ H^2): from positive vacuum compressibility
3. **Non-thermal specific heat** (C_V = 2.20): from van Hove quench anisotropy
4. **Pair creation** (N_pair = 59.8): from Landau criterion v_tau > c_L
5. **DM stability** (Z_2 parity): from cos(phi_23) structure
6. **Five-layer laminar protection**: R-G + BDI + CG(24) kinematics + 0D + hybridization gaps

These are six consequences flowing through distinct channels (dynamical, thermodynamic, statistical, kinematic, symmetry, structural) from a single algebraic object. The BCS Hamiltonian is not one element of the model -- it IS the model's predictive engine for all post-transit physics. In resonance language: the BCS Hamiltonian is the wave equation, and everything observed is a mode of that equation.

### 5.2 Ma = 331 and Re = 0: Ballistic Supersonic Flow

The workshop converged on the definitive characterization of the transit: Mach number Ma_L = 331 (using the Leggett speed c_L = 0.025 M_KK as the Landau critical velocity) and Reynolds number Re_GGE = 0 (exact, from integrability). This is ballistic supersonic spectral flow -- the spectral flow passes through the phononic crystal of SU(3) without scattering, creating 59.8 Cooper pairs through the Landau mechanism, but the created pairs cannot scatter or thermalize because of the five protection layers.

The simultaneous Ma >> 1 and Re = 0 is the defining signature of the Ordered Veil. In standard fluid dynamics, supersonic flow (Ma > 1) typically transitions to turbulence above a critical Reynolds number. On the substrate, this transition is prevented absolutely by the five-layer protection. The condensed matter parent (3He-B) achieves Ma > 1 with finite but exponentially long thermalization (tau_th ~ exp(Delta/T)). The substrate strengthens this to exact non-thermalization (tau_th = infinity) through the 0D cell limit and algebraic integrability.

### 5.3 The Exit-Horizon Scattering Problem

The critical open computation, distilled from the workshop: the pair-crossing phase spread at the exit sonic horizon. Two models bracket the gate band:

**Statistical KZ model**: Each pair crosses independently with spread delta_t ~ t_transit / sqrt(N_pair). Result: t_dec/t_transit ~ 0.13 (over-decohered, delta_OOM ~ 0.07).

**Bogoliubov-phase KZ model**: Pairs are created coherently with phase spread delta_phi = 2.4e-4 rad (S64 PHASE-BOGOLIUBOV-64). The spread in crossing times is delta_t ~ delta_phi / (omega_max - omega_min). Result: t_dec/t_transit ~ 2.2 (under-decohered, delta_OOM ~ 1.1).

The gate band [0.57, 0.88] lies between these. The resolution requires the exit-horizon Bogoliubov coefficients -- the LOCAL transformation at the sonic point, not the GLOBAL transformation at the fold. The mode-dependent greybody factors at the exit horizon determine the actual phase spread, which may be larger than the global delta_phi = 2.4e-4 because the horizon is a caustic where different modes focus at different tau values.

This is the single most important computation for S73.

### 5.4 What W2-C Means for the Decoherence Budget

The spectral functional f*(x) = 0.912 sqrt + 0.088 exp enters the A_s budget through the amplitude normalization kappa = 2.37e-8. The raw A_s prediction (before decoherence) overshoots by 10^{7.6}. The compound BCS squeeze (delta_OOM = 2.074) partially closes this gap but overcorrects by 8x (S71). The remaining decoherence must close the 0.267 OOM residual.

The W2-C result means: once f* is fixed by n_s, the A_s amplitude is a zero-parameter prediction that depends ONLY on the decoherence rate. The decoherence rate is computable from the exit-horizon geometry. The A_s budget reduces to a SINGLE unknown -- t_dec/t_transit at the exit horizon.

### 5.5 Carry-Forward Computations

From the resonance perspective, the following computations are prioritized:

1. **RE-DECOHERENCE-73** (CRITICAL): Resolve statistical vs Bogoliubov KZ model at the exit horizon. Compute exit-horizon Bogoliubov coefficients beta_k(tau_exit), mode-dependent phase spread, CG(24) geometric weighting. Gate: t_dec/t_transit in [0.57, 0.88].

2. **EXIT-HORIZON-BOG-73** (HIGH): Compute the Bogoliubov transformation AT the exit horizon. Local surface gravity kappa_exit from W3-C, greybody factors, phase spread delta_phi(k). Input to RE-DECOHERENCE-73.

3. **DISPERSION-PROTECTION-73** (MEDIUM): Quantify how the 16 hybridization gaps (Layer 5) suppress effective decoherence by protecting inter-branch coherence.

4. **SPECTRAL-ACTION-PROFILE-73** (MEDIUM): Compute S(tau) for tau in [0, 2] to determine whether a post-transit stable equilibrium exists (W3-D: the equilibrium question reduces to the global shape of S(tau)).

5. **KZ-GEOMETRIC-73** (MEDIUM): Compute f_KZ on CG(24) with the physical E_J distribution. The Josephson anisotropy acts as a second-order modifier of the KZ pair-crossing window, not as an independent channel.

---

## Section 6: Summary Table

| # | Topic | Finding | Resonance Implication | Status |
|:--|:------|:--------|:---------------------|:-------|
| 1 | Gap monotonicity (W1-A) | dDelta/dtau = -0.245 M_KK; kappa_Delta = +0.330 | Amplitude channel FROZEN (Q_amp >> 1); decoherence must be PHASE dynamics | INFO |
| 2 | Spectral zeta convergence (W1-C) | a_6/a_4 = 0.223 at L=7, monotone decreasing | Finite-spectrum artifacts confirmed; Gilkey ratio (0.25) is the correct reference | PASS |
| 3 | Three-way tau consistency (W1-E) | Overlap at [0.189, 0.191] | The fold IS the resonance point; three independent channels select the same cavity shape | PASS |
| 4 | Dual decoherence (W2-A) | delta_OOM = 1.692 at physical t_dec; BCS = 99.8% | Cell-crossing 9.4x too slow; A_s budget IS the BCS decoherence budget | INFO |
| 5 | Spectral functional (W2-C) | f* = 0.912 sqrt + 0.088 exp; non-perturbative | Observation SELECTS the cavity frequency response; SDW expansion inapplicable | **PASS** |
| 6 | BCS-dressed n_s (W3-A v2) | delta_n_s = 3.8e-6 (16/155,984 modes) | Condensate back-reaction negligible; flow carries condensate without distortion | INFO |
| 7 | Entry horizon (W3-C) | T_entry = 72.8 M_KK; omega/T = 0.012; delta_n_s = +1.001 | First amplification stage in multi-stage squeeze chain; frequency-dependent gain | PASS |
| 8 | Bispectrum (W4-A) | f_NL = -0.313; 80x below Planck | Gaussian spectrum: laminar flow confirmed; 1/sqrt(N) CLT suppression | **PASS** |
| 9 | C_V scaling (W4-B) | Ratio = 2.20 at N >= 8; alpha = 0.013 | GGE protection from spectral heterogeneity (B1/B2/B3 anisotropy); non-universal, bounded >= 1 | INFO |
| 10 | Frustration Schmidt (W4-C) | K = 3.234; 19% reduction | Entanglement robust to geometric frustration; analog = theta-texture in 3He-B | PASS |
| 11 | Page curve (W4-D) | Area law R^2 = 0.988; monogamy-min R^2 = 0.996 | Monogamy-capped at small |A|, area law at large |A|; gapped BCS fabric, not black hole | PASS |
| 12 | Laminar flow (workshop) | Ma = 331, Re = 0; five-layer protection | Ballistic supersonic spectral flow; Ordered Veil protected by redundant mechanisms | **CONVERGED** |
| 13 | Hawking correction (workshop) | t_dec shifted from 2.8 to 45 (x16) | Squeezed-state phase variance 10^4 smaller than thermal; Hawking channel eliminated | **CONVERGED** |
| 14 | KZ bracket (workshop) | Statistical: 0.13; Bogoliubov: 2.2 | Gate band [0.57, 0.88] between models; exit-horizon geometry is the arbiter | **OPEN** |
| 15 | BCS unification (workshop E3) | Six predictions from one Hamiltonian | BCS on spectral triple = universal ancestor for post-transit physics | **STRUCTURAL** |
| 16 | Two-fluid retraction (workshop C5) | Volovik partition != Landau two-fluid | Correct mapping: BCS spectral function A(k,omega), not spatially separated fluids | **CORRECTED** |
| 17 | Weinberg angle (W2-B) | 54.5% discrepancy (pure SM) | KK threshold corrections required; sin^2(theta_W) is sensitive probe of spectral functional | FAIL |
| 18 | G_2 constancy (W4-F) | G_2 1.93% < SU(3) 2.92% | a_2/a_4 constancy is rank-2 general; MAGNITUDE (40x) may be distinguishing, not constancy | FAIL |
| 19 | Modular chirp (W3-E) | 8.4 OOM discrepancy | Bogoliubov rotation rate != eigenvalue curvature; different spectral functionals | FAIL |
| 20 | tau equilibrium (W3-D) | BCS/spectral = 7.94e-5 | Equilibrium is a GEOMETRIC question (spectral action landscape), not BCS | INFO |

---

**Bottom line from the resonance perspective**: S72 established that the transit is ballistic supersonic flow (Ma = 331) through a phononic crystal with five redundant laminar protection layers (Re = 0), observation selects the spectral functional (f* non-perturbative, dominated by sqrt), and the A_s budget reduces to a single unknown -- the exit-horizon pair-crossing phase spread. The decoherence problem is not a resonance problem (Q_cavity ~ 10^{-6}); it is a scattering problem at the exit sonic horizon. Nine decoherence channels have been catalogued and ranked; only the KZ pair-crossing spread survives as viable, but its timescale brackets the gate band from both sides. The exit-horizon Bogoliubov coefficients are the decisive computation.
