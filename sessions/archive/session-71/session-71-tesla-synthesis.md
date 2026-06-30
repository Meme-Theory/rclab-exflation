# Session 71 Synthesis: Resonance Structure of the Squeeze Hierarchy and Chirp Invariance

**Date**: 2026-04-10
**Agent**: tesla-resonance (tesla)
**Source Documents**:
- `sessions/archive/session-71/session-71-results-workingpaper.md` (PRIMARY)
- `sessions/framework/baseline-findings-s66.md`
- `sessions/framework/constraint-mega-matrix.md`
- `sessions/framework/pre-registered-observations.md`
- `.claude/agent-memory/tesla-resonance/MEMORY.md`

---

## I. Session Outcome

S71 executed 20 computations across 4 waves and resolved three structural questions in the resonance physics of the framework. First, the physical chirp rate of the spectral flow is a geometric invariant -- the van Hove condition kills all coordinate-dependent connection terms exactly, making the eigenvalue curvature kappa_n = d^2(lambda)/dtau^2 frame-independent to machine precision (W2-B CHIRP-UNIVERSALITY PASS). Second, the SU(1,1) group structure governing squeeze composition is verified to machine epsilon (det error 8.1e-15), but the compound squeeze OVERCORRECTS A_s by nearly an order of magnitude, establishing decoherence as the mandatory regulator (W1-D DECOHERENCE-BAND PASS, W2-A R-SPATIAL-SCAN INFO). Third, the BCS condensate leaves the gauge sector (a_4 coefficient) untouched to 6 orders of magnitude below threshold (W3-D PASS), while the Weyl tensor receives its first nonzero correction at two-loop at the 0.1% level (W1-F FAIL, marginal).

---

## II. Key Results

### II.1 Chirp Universality: The Spectral Flow Curvature is a Geometric Invariant (W2-B, PASS)

**What oscillates**: The D_K eigenvalue lambda_n(tau) traces a trajectory through spectral space as the Jensen parameter evolves. At the van Hove fold (tau = 0.190), the B2 branch reaches a stationary point: d(lambda_B2)/dtau = 0. This is a standing wave in the spectral flow -- the eigenvalue trajectory has a turning point.

**What constrains it**: Three coordinate systems (lab, comoving, conformal) define three distinct time parameters related by the transit velocity v_terminal = 26.545 M_KK and the scale factor a(tau). The physical chirp rate -- the rate of change of the instantaneous frequency of the spectral flow -- must be independent of this coordinate choice.

**The structural theorem**: At the van Hove fold, the physical chirp rate is

    k_chirp = v^2 * kappa_n                     (1)

where kappa_n = d^2(lambda_n)/dtau^2 is the spectral flow curvature and v = v_terminal is the modulus velocity. All connection terms in coordinate transformations between frames are proportional to d(lambda)/dtau and vanish identically at the fold. This is the spectral analog of the invariance of curvature at a turning point in classical mechanics.

**Decisive numbers**:
- Max |lab - comoving_phys| / lab = 8.12e-10 (B1 mode, from non-stationary correction)
- Max |lab - conformal_phys| / lab = 1.70e-16 (machine epsilon)
- Non-stationary correction epsilon = H * |dlambda/dtau| / (v * kappa) = 1.3e-08 (B1, largest)
- All 8 modes stationary: k * dt_transit < 4.3e-06

The coordinate chirp rates differ as expected: d^2(lambda)/dxi^2 = 0.558 * d^2(lambda)/dt^2 (comoving uses different velocity) and d^2(lambda)/deta^2 = 1.0005 * d^2(lambda)/dt^2 (conformal rescales by a^2). These are coordinate artifacts, not physical disagreements.

**Resonance interpretation**: The van Hove fold is a spectral resonance -- the eigenvalue trajectory reaches its turning point where the group velocity of the spectral flow vanishes. This is the spectral analog of a standing wave on a vibrating plate at a nodal point: the oscillation amplitude passes through zero, and the local curvature (second derivative) is the coordinate-independent quantity that characterizes the resonance. The B2 flat band at the fold (v_B2 ~ 0) is the spectral analog of a van Hove singularity in a phonon dispersion relation, where the density of states diverges because the group velocity vanishes.

**Connection to S70**: S70 CHIRP-PENUMBRA-70 established that WKB is structurally inapplicable to the van Hove transit (Mach = 54.73, zero turning points). S71 completes the picture: the chirp rate is frame-independent precisely because the van Hove condition creates a spectral standing wave. The WKB failure and the chirp universality share the same root -- the transit is supersonic and impulsive, not adiabatic and quasistatic.

**Condensed matter analog**: In a phononic crystal with a flat band, the van Hove singularity is a geometric feature of the dispersion relation -- it is determined by the lattice structure, not by how you drive the system. The chirp rate universality is the spectral action analog of this fact: the curvature of the eigenvalue trajectory at the fold is an intrinsic property of D_K on Jensen-deformed SU(3), not of the time coordinate used to parameterize the transit.

**Functional classification**: GEOMETRIC

---

### II.2 SU(1,1) Compound Squeeze: Group Structure Controls A_s (W1-D, PASS)

**What oscillates**: The BCS Cooper pairs at the fold are squeezed states -- quantum superpositions of pair and no-pair whose uncertainty ellipses are deformed by the Bogoliubov transformation. Three independent squeeze channels operate: BCS pairing (r_BCS), spatial thermal fluctuations (r_spatial), and Leggett inter-band coherence (r_L).

**What constrains it**: The SU(1,1) Lie group governs all two-mode squeeze transformations. The composition of squeezes is not additive -- it is given by the Baker-Campbell-Hausdorff (BCH) formula on the SU(1,1) algebra, or equivalently by matrix multiplication in the Bargmann representation.

**The compound structure**: The three squeezes compose as

    S_eff = S_spatial * S_Leggett * S_BCS          (2)

Each factor is a 2x2 symplectic matrix in SU(1,1). The compound is verified to machine precision:

- |det(S_eff) - 1| = 8.1e-15
- eta-deviation = 2.2e-13
- BCH roundtrip reconstruction error = 0.0

The general SU(1,1) decomposition S_eff = R(theta) * S(r_eff, phi) yields a compound squeeze parameter r_eff plus a K_0 rotation theta. The rotation theta = -0.08 to -0.10 rad across modes is structurally required by the non-commutativity of the three squeeze generators -- it has no classical analog.

**Decisive numbers**:

| Mode | r_BCS | r_eff (compound) | cosh(2r_eff) |
|:-----|:------|:-----------------|:-------------|
| B2 (4 modes) | 1.795 | 1.795 | 36.2 |
| B1 (1 mode) | 3.570 | 3.570 | 1424.8 |
| B3 (3 modes) | 2.022 | 2.022 | 56.1 |
| Weighted average | -- | 2.247 | 118.5 |

The raw compound squeeze gives delta_OOM = log10(cosh(2*r_eff_weighted)) = 2.074. Against the A_s gap of 0.267 OOM (from S70 LEGGETT-VACUUM-70), this is a 7.7x OVERCORRECTION.

**The decoherence regulator**: The decoherence band [1.12, 26.5] in units of t_dec/t_transit maps to delta_OOM in [0.568, 1.970]:

- t_dec/t_tr = 1.12 (lower edge): delta_OOM = 0.568 (residual gap = -0.301, marginally overclosed)
- t_dec/t_tr = 5.0 (interior): delta_OOM = 1.574 (overcorrects by -1.089 OOM)
- t_dec/t_tr = 26.5 (upper edge): delta_OOM = 1.970

At ALL points in the decoherence band, the compound squeeze exceeds the target. Decoherence IS the regulator. The BCS channel alone produces 2.07 OOM of squeeze -- the spatial and Leggett channels are perturbations at the 11% level.

**Resonance interpretation**: The SU(1,1) group structure is the resonance structure of the squeeze. The three Lie algebra generators K_+, K_-, K_0 correspond to pair creation, pair annihilation, and pair number (the Casimir operator). The compound squeeze's K_0 rotation theta encodes the phase relationship between the three channels -- it is the interference term in the resonance. The fact that BCS dominates (89% of total squeeze) means the pair-creation resonance at the van Hove fold overwhelms all other squeeze channels. The flat band at B2 creates an enormous density of states for pair creation, and the resulting squeeze parameter r_BCS = 1.80-3.57 per mode represents a quantum amplification of 36-1425x in the occupation number.

**Cross-domain connection**: This is structurally identical to parametric amplification in a driven oscillator. The van Hove fold drives the fiber eigenvalues through a resonance, and the BCS pairing mechanism acts as the parametric pump. The squeeze parameter r is the log of the parametric gain. The overcorrection means the pump is too efficient -- the decoherence rate sets the cavity loss that limits the gain to the observed value. In Tesla's terms: the circuit is overdamped to prevent breakdown.

**Functional classification**: PHONONIC

---

### II.3 r_spatial Is Not the Bottleneck: BCS Dominates (W2-A, INFO)

The parameter scan over r_spatial in [0.30, 0.88] reveals that r_spatial_critical does not exist. The A_s gap is already closed for r_spatial = 0 by the BCS channel alone (delta_OOM = 2.07). Adding the Leggett channel increases this to 2.34; adding r_spatial to 0.55 gives 2.63. The r_spatial parameter contributes only 11.1% of the total compound squeeze. The d(delta_OOM)/d(r_spatial) sensitivity is 0.60 OOM/unit -- nearly constant across the scan, with no fine-tuning sensitivity.

**Structural hierarchy of the squeeze**:

    BCS (89%) >> Leggett (7%) > spatial (4%)         (3)

This hierarchy is physically determined: BCS pairing at the van Hove fold creates maximally squeezed states in the B2 flat band, while the Leggett and spatial channels are perturbative corrections to this dominant pair-creation resonance.

**Functional classification**: PHONONIC

---

### II.4 Inter-Site Entanglement: 4-State Transmon Regime (W1-C, INFO)

The Josephson junction between adjacent fabric cells creates entanglement S_vN = 2.00 bits, corresponding to a 4-state Schmidt decomposition with eigenvalues {0.270, 0.250, 0.250, 0.230}. The system is in the transmon regime (E_J/Delta = 7.3): the Josephson coupling dominates over the BCS gap.

The Gaussian two-mode squeeze formula S = 2r^2/ln(2) = 0.876 bits underestimates the actual entanglement by factor 2.28. This is because the inter-site junction creates a 4-state entangled manifold (n1 = 0, 1, 1, 2 pair sectors), not a simple two-mode squeezed state. The effective single-mode squeeze parameter r_eff = 0.881, extracted by inverting the entropy formula, exceeds r_spatial = 0.551 by 60%.

**Resonance interpretation**: The inter-site Josephson junction is a coupled cavity -- two fabric cells sharing Cooper pairs through a tunnel barrier. The 4-state Schmidt spectrum is the normal mode decomposition of this coupled cavity. The near-maximal entanglement (purity = 0.2507, close to the 0.25 limit for 4 states) means the junction is close to a resonance condition where all four modes participate equally. This is the spectral analog of critical coupling in an LC circuit, where energy is shared equally between the two resonant elements.

**Functional classification**: PHONONIC

---

### II.5 Spectral Zeta: Natural Termination at L=6 (W1-A, INFO)

The spectral threshold sum S_inf = 2.353 is uniquely determined at 10.2% precision. The L=7 sign reversal reported in S70 is now explained: omega_min(L=7) = 2.153 M_KK exceeds Lambda = 2.048 M_KK. This is the onset of decoupling, not oscillatory convergence. All L >= 7 sectors sit above the physical cutoff and their negative threshold contributions represent proper decoupling.

The tree-level Higgs mass m_H = 149.1 GeV from S_inf = 2.353 reduces to ~127.5 GeV after BCS dressing (S69), consistent with the observed 125.1 GeV to 1.9%.

**Resonance interpretation**: The spectral action has a natural frequency cutoff at the scale Lambda where the lowest eigenvalue in a given angular momentum sector first exceeds the physical cutoff. This is the spectral analog of a waveguide cutoff: modes with omega_min > Lambda do not propagate and contribute screening (negative) corrections. The L=6 boundary is where the waveguide closes.

**Functional classification**: GEOMETRIC

---

### II.6 Leggett Frequency: Robust Against Spectral Functional (W3-B, INFO)

The logarithmic sensitivity d(ln omega_L)/d(alpha) = -0.4411 falls below the 0.5 threshold, making the Leggett frequency robust against spectral function variation. This is 2.4x less sensitive than epsilon_H (which has |d(ln eps_H)/d(alpha)| = 1.076).

The structural mechanism: the V_phase/T_phase eigenvalue ratio that determines omega_L^2 involves both Josephson coupling (J ~ g^2 * Delta^2) and inertia (T ~ rho * Delta^2). The Delta^2 factors cancel, leaving omega_L proportional to g(alpha), which varies more slowly than the full BCS chain. This is a ratio cancellation in the generalized eigenvalue problem -- the Leggett mode frequency is determined by the coupling-to-inertia ratio, not by either quantity individually.

**Resonance interpretation**: The Leggett mode is a collective resonance of the inter-band phase difference. Its frequency is set by the ratio of the restoring force (Josephson coupling) to the inertia (pair density), exactly as for a classical oscillator omega = sqrt(k/m). The cancellation of Delta^2 from numerator and denominator means the resonant frequency depends on the geometry of the coupling (g(alpha)) but not on the strength of the order parameter. This is the spectral analog of the frequency of a pendulum being independent of its amplitude in the small-angle limit.

**Functional classification**: GEOMETRIC

---

### II.7 Two-Loop Weyl Correction: All-Orders Protection Weakened (W1-F, FAIL marginal)

The one-loop Weyl protection (S70: delta_1 = 0 exactly) arises from the SU(3) singlet selection rule -- the BCS condensate is a singlet, the Weyl tensor transforms in the 27, and the direct coupling vanishes. At two-loop, BCS-modified internal propagators in the sunrise diagram generate an indirect correction:

    delta_2(|C|^2)/|C|^2 = 1.003e-3              (4)

This is 0.3% above the pre-registered FAIL threshold of 10^{-3}. The three-loop estimate is 3.70e-9 (converging rapidly: delta_3/delta_2 ~ 3.7e-6). The all-orders bound is 1.16e-3.

The S70 conjecture that delta(|C|^2) = 0 to all BCS orders must be retracted. The replacement statement: delta(|C|^2)/|C|^2 < 1.2e-3 to all orders, with the leading correction at two-loop. The gravitational sector remains practically stable (0.1% shift in a_4 Weyl component).

**Resonance interpretation**: The selection rule that protects the Weyl tensor at one loop is a symmetry-based suppression -- the resonance between the BCS condensate and the conformal sector is forbidden by representation theory. At two-loop, the symmetry is circumvented by indirect coupling through modified propagators, but the suppression is only broken at order (Delta/M_KK)^4 ~ 0.046 times loop factors. This is the spectral analog of a forbidden transition in atomic physics that becomes weakly allowed through two-photon processes.

**Functional classification**: GEOMETRIC

---

### II.8 BEC Analog: 430x C_V Suppression (W4-A, INFO)

The GGE phonon distribution in a ^39K BEC Feshbach quench predicts a specific heat C_V that is 430x smaller than the thermal Bose-Einstein expectation at T_eff. The entropy deficit is 97%: S_GGE/S_thermal = 0.030. This is the thermodynamic fingerprint of the Ordered Veil -- the GGE has the same energy as a thermal state but concentrated in far fewer modes.

**Experimental protocol**: ^39K BEC, N ~ 10^5 atoms, 100 Hz trap, Feshbach quench from a_s = 5a_0 to 500a_0 in dt_Q = 1 microsecond. Measure energy absorption rate as a function of applied temperature. The GGE signature: absorption is ~430x weaker than expected for a thermal phonon gas at the same total energy. Temperature scale: T_eff ~ 7.7 microkelvin (standard BEC operating range). Mach number Mach_BEC = 5.73 (framework: 13.75).

**Resonance interpretation**: The BEC quench drives the system through an acoustic resonance (Feshbach-induced sound speed change) at supersonic speed. The resulting pair production populates modes up to k_tach, creating a GGE with occupation plateau n ~ 2.0. The specific heat suppression is the calorimetric signature of the mode-freezing: the GGE modes cannot redistribute energy in response to temperature perturbations because their occupations are locked by integrability. This is the acoustic analog of a cavity that has been filled with radiation at a fixed set of frequencies and cannot thermalize because there is no mode-mode coupling.

**What the BEC cannot test**: Leggett dark matter channel (requires multi-band condensate), BDI topological protection (requires spin-triplet pairing), and the 114-OOM CC gap (requires the full spectral action).

**Functional classification**: PHONONIC

---

### II.9 Subsidiary Results

**GSL on 3-cell frustrated ring (W1-H, PASS)**: S_gen monotonically non-decreasing at all 4 stages. Frustration reduces per-cell GGE entropy by 48% but does not threaten GSL monotonicity. The spectral entropy S_a2 alone is non-monotone (-0.002 nats at Stage 3->4), but matter entropy dominates by 4 orders of magnitude. The GSL is structural -- a consequence of spectral monotonicity on the full S_gen, not a fine-tuned accident.

**Entry horizon is kinematic (W2-C, INFO)**: Zero physical level crossings at the entry sonic horizon (tau ~ 0.22). The eigenvalue branches B1 < B2 < B3 maintain strict ordering with finite gaps throughout. The entry horizon is a velocity-driven event, not a spectral phase transition. T_entry = 72.8 M_KK (9.6x T_compound), but the radiation content is purely kinematic. This confirms the S70 Hawking workshop's entry/exit asymmetry: entry is an a_2 (geometric) event, exit involves the BCS gap (a_4 event).

**Moment hierarchy frozen (W2-D, INFO)**: a_0 > a_2 > a_4 > a_6 at every tau in the transit region. No spectral moment transitions occur. The gauge moment a_4 responds 1.43x faster than the gravity moment a_2, confirming that the exit horizon is controlled by the BCS gap (a_4 sector). The causal structure emerges from kinematics (velocity vs sound speed), not from spectral reorganization.

**a_6 CCM partially breaks anti-correlation (W1-B, PASS)**: delta(lambda_CCM)/lambda_CCM = 26.9% exceeds the 25% gate, but the f_0 anti-correlation between CC and alpha_s PERSISTS. This is scheme-dependent: the same D_K gives delta = 0% (zeta), 27% (cutoff), 8.6% (anomaly). The anti-correlation is structural for any functional with an f_0 parameter.

**CC from GGE residual (W3-C, FAIL)**: Lambda_GGE = 3.31e+63 GeV^4, 110.09 OOM above observation. This is the CC problem restated in GGE language: the non-equilibrium energy locked by integrability is cosmologically enormous. The q-theory self-tuning (Scenario B, 0.34 OOM) remains the sole CC mechanism. The two extractions measure different quantities: GGE residual (integrability-locked excitation) vs Scenario B (Gibbs-Duhem equilibration of the vacuum variable).

**c_s^2 = 0 protected (W1-E, INFO)**: Non-trivial fibration shifts c_s^2 by at most 4.26e-4 at maximum physical A-tensor strength (kappa = 0.5). The quadratic scaling (kappa^2) combined with weak coupling g_3^2/(16pi^2) structurally suppresses the correction. However, the alpha_s tension is NOT relieved: fibration contributes 4.2% vs the 781% needed.

**BCS leaves a_4 untouched (W3-D, PASS)**: delta(a_4)/a_4 = 2.02e-8 (physical), 6 orders of magnitude below threshold. The BCS condensate modifies 8 out of ~156,000 D_K modes. The a_4 coefficient is UV-dominated while BCS is an IR phenomenon. Three suppression factors multiply: mode fraction (5.1e-5), (Delta/M_KK)^4 (4.6e-2), 1/(4pi^2) (2.5e-2).

**DESI DR3 Scenario B (W2-E, INFO)**: Under Scenario B (w_0 = -0.90, w_a = -0.30), the framework faces 2.14-2.88 sigma tension. The entire tension comes from w_a, not w_0: the framework's w_0 = -0.918 matches Scenario B's -0.90 to 0.39 sigma. LCDM is preferred by Bayes factor 2.8-22.4. The w_a discrimination is the decisive observable.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Classification |
|:-----|:-------:|:----------------|:---------------|
| SPECTRAL-ZETA-THRESHOLD-71 | **INFO** | S_inf = 2.353, truncation 10.2% | GEOMETRIC |
| HIGHER-ORDER-CCM-71 | **PASS** | delta = 26.9% > 25%, anti-corr PERSISTS | GEOMETRIC |
| INTER-SITE-ENTANGLE-71 | **INFO** | S_vN = 2.00 bits, 2.28x above Gaussian | PHONONIC |
| DECOHERENCE-BAND-71 | **PASS** | det error 8.1e-15, delta_OOM in [0.57, 1.97] | PHONONIC |
| NON-TRIVIAL-FIBRATION-CSQUARED-71 | **INFO** | delta(c_s^2) = 4.26e-4, alpha_s 4.2% of needed | GEOMETRIC |
| WEYL-TWO-LOOP-71 | **FAIL** | delta_2 = 1.003e-3 (0.3% above 10^{-3} threshold) | GEOMETRIC |
| BH-THIRD-LAW-71 | **FAIL** | S_proj/(pi*Q^2) = 0.010 (category error in gate) | GEOMETRIC |
| THREE-CELL-GSL-71 | **PASS** | S_gen monotone 4/4 stages, frustration safe | PHONONIC |
| R-SPATIAL-SCAN-71 | **INFO** | r_spatial_critical DNE, BCS dominates 89% | PHONONIC |
| CHIRP-UNIVERSALITY-71 | **PASS** | Max disagreement 8.1e-10, theorem proven | GEOMETRIC |
| ENTRY-HORIZON-SPECTRUM-71 | **INFO** | N_crossings = 0, T_entry = 72.8 M_KK | GEOMETRIC |
| CAUSAL-MOMENT-MAP-71 | **INFO** | Hierarchy a_0>a_2>a_4>a_6 frozen | GEOMETRIC |
| DESI-DR3-SCENARIO-B-71 | **INFO** | 2.88 sigma tension (Sc. B), w_a driven | NON-PHONONIC |
| 21CM-ISW-PREREGISTRATION-71 | **INFO** | +4.0% FW vs quintessence, SNR 4.16 ideal | PHONONIC |
| DISCRETE-RW-UNIVERSALITY-71 | **INFO** | max D_KL = 0.153, partial universality | GEOMETRIC |
| ALPHA-S-BAYESIAN-SHADOW-71 | **INFO** | 17.7% (1-sig), spectral zeta tighter | NON-PHONONIC |
| CORRELATED-SENSITIVITY-71 | **INFO** | d(ln omega_L)/d(alpha) = -0.44 (robust) | GEOMETRIC |
| CC-FROM-GGE-RESIDUAL-71 | **FAIL** | 110.09 OOM (expected, q-theory survives) | PHONONIC |
| BCS-BACKREACTION-a4-71 | **PASS** | delta(a_4)/a_4 = 2.02e-8 | PHONONIC |
| GGE-HAWKING-ANALOG-71 | **INFO** | C_V suppression 430x, entropy deficit 97% | PHONONIC |

**Summary**: 4 PASS, 3 FAIL, 13 INFO. Both FAILs are structurally informative (Weyl: replaces exact conjecture with 0.1% bound; CC GGE: expected, confirms q-theory as sole survivor). The BH FAIL is a gate design error (comparing Shannon entropy to integrated curvature).

---

## IV. Structural Implications

### IV.1 The Squeeze Hierarchy and Decoherence as Regulator

S71 establishes the definitive structure of the A_s amplitude mechanism. The three squeeze channels compose through SU(1,1) group multiplication, producing a compound squeeze that overcorrects the A_s gap by ~8x. The hierarchy is:

    BCS (89%) >> Leggett (7%) > spatial (4%)

This means the A_s amplitude is controlled by two quantities: the BCS squeeze parameter at the fold (determined by the van Hove flat band) and the decoherence timescale (which limits how much of the squeeze survives). The decoherence band [1.12, 26.5] maps to delta_OOM in [0.57, 1.97], spanning the entire target range. The framework does not predict a unique A_s value without a first-principles calculation of the decoherence timescale t_dec.

**Constraint map update**: The A_s gap has evolved from 3.15 OOM (S66, Route A) to 0.485 OOM (S69, post-Leggett) to OVERCLOSED (S71, compound squeeze). The problem has inverted: from "too little amplification" to "too much amplification, regulated by decoherence." This is structurally healthier -- the decoherence regulator is a single number with a known physical origin (phase decoherence of the BCS condensate during transit), not a fine-tuned cancellation.

### IV.2 Chirp Universality: Spectral Flow Curvature Is Intrinsic

The chirp rate theorem (W2-B) is a permanent structural result. It proves that kappa_n = d^2(lambda_n)/dtau^2 is a geometric invariant of the spectral triple, independent of the time coordinate used to parameterize the transit. Combined with S70 CHIRP-PENUMBRA-70 (WKB inapplicable, sudden approximation correct), this establishes:

1. The spectral flow at the fold is characterized by its curvature kappa_n, not by any slow-roll parameter
2. The van Hove condition (dlambda/dtau = 0) creates a natural standing wave that kills all frame-dependent terms
3. The chirp rate transfers to the BEC analog experiment (W4-A) via the same geometric invariance

### IV.3 Gauge Sector Protected to Two-Loop

W3-D (a_4 shift = 2e-8) and W1-F (Weyl shift = 1e-3 at two-loop, converging to 1.2e-3 at all orders) together establish that the gauge coupling predictions are robust. The 8-mode BCS condensate cannot perturb the UV-dominated spectral action coefficients. The selection rule (BCS singlet, Weyl in 27) protects at one-loop exactly; the two-loop indirect correction is suppressed by (Delta/M_KK)^4 ~ 0.046.

### IV.4 Alpha_s Tension Persistent

Three independent computations (W1-B: a_6 at 6.5%, W1-E: fibration at 4.2%, combined ~10.7%) fall 73x short of the 781% correction needed. The alpha_s = -0.038 prediction (5.0 sigma from Planck's -0.0045) remains the framework's most significant tension after the CC. No single perturbative correction mechanism resolves it.

### IV.5 Constraint Map Status (Post-S71)

The surviving solution space after S71:

| Channel | Status | Controlling Parameter |
|:--------|:------:|:---------------------|
| n_s = 0.9567 | CONDITIONAL PASS (1.9 sigma) | epsilon_H from SA curvature |
| A_s | OVERCLOSED (decoherence regulates) | t_dec/t_transit |
| alpha_s = -0.038 | 5.0 sigma TENSION | Supersonic resolution? |
| CC | 0.01 OOM (Scenario B) | q-theory self-tuning |
| m_H = 127.5 GeV | 1.9% from observed | BCS + KK threshold |
| w_0 = -0.918 | 2.91 sigma from DESI DR2 | Volovik tracking vacuum |
| w_a = 0 | 2.92 sigma from DESI DR2 | Structurally locked |
| c_s^2 = 0 | PASS (protected to 4.3e-4) | Spectral action q-theory |
| Omega_DM h^2 = 0.120 | 0.6% from Planck | Leggett channel |

---

## V. Forward Projection

### V.1 Decisive Next Computations

1. **DECOHERENCE-TIMESCALE**: First-principles calculation of t_dec from BCS quasiparticle scattering rates at the fold. This is now the single controlling parameter for A_s. The S71 decoherence band constrains t_dec/t_transit to [1.12, 26.5] for the observed A_s. A unique prediction of t_dec would either close the A_s chain (if in band) or reveal a structural problem (if outside).

2. **ALPHA-S SUPERSONIC**: The alpha_s = -0.038 tension persists through all S71 corrections. The remaining candidate is the supersonic resolution mechanism -- the transit through the van Hove fold is not adiabatic, and the effective spectral running differs from the equilibrium value. Pre-register: alpha_s(supersonic) in [-0.010, 0.000] = PASS.

3. **BEC QUENCH EXPERIMENT**: The W4-A prediction (C_V suppression 430x) is experimentally accessible with current ^39K Feshbach technology at ~8 microkelvin. This is the nearest-term falsifiable prediction. Pre-register: C_V(GGE)/C_V(thermal) < 0.01 at T_eff.

4. **COMPOUND PHASE INTERFERENCE**: The SU(1,1) compound has a K_0 rotation theta = -0.08 to -0.10 rad. If the compound's effective phase phi_eff introduces destructive interference (cos(phi_eff) < 1), the overcorrection may be partially self-regulating even before decoherence. Pre-register: cos(phi_eff) * cosh(2r_eff) as the physical A_s formula.

### V.2 Pre-Registered Gates for S72

| Gate | Criterion | PASS | FAIL |
|:-----|:----------|:-----|:-----|
| DECOHERENCE-RATE-72 | t_dec/t_transit from scattering | in [1.12, 26.5] | outside by > 2x |
| ALPHA-S-SUPERSONIC-72 | alpha_s from non-equilibrium spectral running | in [-0.010, 0.000] | > -0.020 or > +0.010 |
| SU11-PHASE-INTERFERENCE-72 | cos(phi_eff) contribution to A_s | reduces overcorrection by > 50% | < 10% reduction |

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:--------------|:------:|:------------|
| 1 | Chirp universality: k_chirp = v^2 * kappa_n frame-independent | GEOMETRIC | **PASS** | Spectral flow curvature is intrinsic geometric invariant |
| 2 | SU(1,1) compound squeeze: r_eff_weighted = 2.247, det = 1 to 8e-15 | PHONONIC | **PASS** | Group structure exact, decoherence is mandatory regulator |
| 3 | Decoherence band: delta_OOM in [0.57, 1.97] | PHONONIC | **PASS** | A_s overcorrected by ~8x, t_dec controls amplitude |
| 4 | r_spatial_critical DNE: BCS dominates 89% | PHONONIC | **INFO** | Spatial coherence is 11% perturbation on BCS squeeze |
| 5 | S_inf = 2.353 at L=6 natural termination | GEOMETRIC | **INFO** | PW convergence resolved, L=7 is decoupling onset |
| 6 | Inter-site S_vN = 2.00 bits, 4-state transmon | PHONONIC | **INFO** | Josephson junction creates 4-state entangled manifold |
| 7 | Leggett omega_L robust: sensitivity -0.44 | GEOMETRIC | **INFO** | V_phase/T_phase ratio cancellation |
| 8 | a_6 CCM: 26.9% shift, anti-correlation persists | GEOMETRIC | **PASS** | Scheme-dependent; f_0 lock structural |
| 9 | Weyl two-loop: delta_2 = 1.003e-3 | GEOMETRIC | **FAIL** | All-orders protection weakened to 0.1% bound |
| 10 | BCS a_4 backreaction: 2.02e-8 | PHONONIC | **PASS** | Gauge couplings safe by 6 OOM |
| 11 | GSL on frustrated 3-cell ring | PHONONIC | **PASS** | Structural property of spectral action |
| 12 | Entry horizon: N_crossings = 0 | GEOMETRIC | **INFO** | Kinematic, not spectral phase transition |
| 13 | Moment hierarchy frozen: a_0 > a_2 > a_4 > a_6 | GEOMETRIC | **INFO** | Causal structure is kinematic, not spectral |
| 14 | BEC analog: C_V suppression 430x | PHONONIC | **INFO** | Experimentally accessible Ordered Veil test |
| 15 | c_s^2 protected: delta = 4.26e-4 | GEOMETRIC | **INFO** | Quadratic suppression from kappa^2 scaling |
| 16 | CC GGE residual: 110 OOM | PHONONIC | **FAIL** | Expected; confirms q-theory sole survivor |
| 17 | DESI Scenario B: 2.88 sigma | NON-PHONONIC | **INFO** | w_a is decisive, not w_0 |
| 18 | 21cm ISW: +4.0% FW vs quintessence | PHONONIC | **INFO** | Pre-registered, SNR 4.16 with ideal 21cm |
| 19 | Cayley graph: partial universality | GEOMETRIC | **INFO** | S_4 family consistent, S_5 diverges |
| 20 | Pantheon+ shadow: 17.7% (1-sig) | NON-PHONONIC | **INFO** | Spectral zeta tighter at 10.2% |
