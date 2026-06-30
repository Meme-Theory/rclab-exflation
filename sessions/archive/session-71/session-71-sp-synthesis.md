# Session 71 Synthesis: Causal Rigidity and the Spectrally Inert Horizon

**Date**: 2026-04-10
**Agent**: schwarzschild-penrose-geometer (sp)
**Source Documents**:
- `sessions/archive/session-71/session-71-results-workingpaper.md` (primary, all 20 computations)
- `sessions/framework/baseline-findings-s66.md`
- `sessions/framework/constraint-mega-matrix.md`
- `sessions/framework/pre-registered-observations.md`
- `sessions/framework/Phononic-Penrose-Diagrams.md` (definitive, S53)
- Agent memory: S69 collab, S70 Penrose sequence, S70 near-extremal

---

## I. Session Outcome

Session 71 delivers 20 computations across 4 waves, with 4 PASS, 3 FAIL, and 13 INFO verdicts. The decisive result for causal structure is the **entry/exit horizon asymmetry confirmed**: the entry sonic horizon at tau ~ 0.22 has zero physical eigenvalue crossings (W2-C), while the exit horizon at tau ~ 0.16 sits below the van Hove fold where the BCS flat band creates the spectral reorganization that defines the condensate. The moment hierarchy a_0 > a_2 > a_4 > a_6 is frozen across transit (W2-D), establishing that the causal structure is painted by kinematic velocity onto a spectrally rigid backdrop. The GSL extends to frustrated topology (W1-H PASS), while the BH third law fails by category error (W1-G FAIL), sharpening the boundary between emergent thermodynamics and fiber-level spectral entropy.

---

## II. Key Results

### II.1 The Entry Horizon is Spectrally Featureless (W2-C)

The entry sonic horizon at tau = 0.2195 has N_crossings_physical = 0. All 85 raw crossings detected in the eigenvalue scan are conjugate-symmetry degeneracies (B2(0,1) = B2(1,0) to machine epsilon), which are representation-theoretic identities of D_K, not physical level crossings. The B1/B2/B3 branches maintain strict ordering with finite gaps throughout:

| Gap | Value at Entry | Behavior |
|:----|:---------------|:---------|
| B2 - B1 | 0.0146 M_KK | OPENS as tau decreases through entry |
| B3 - B2 | 0.0366 M_KK | Stable |
| B3 - B1 | 0.0517 M_KK | Stable |

The derivative structure at entry is: dB1/dtau = -0.018, dB2/dtau = +0.109, dB3/dtau = +0.103. B2 and B3 co-move; B1 separates. The B2-B1 gap OPENS at the entry horizon -- the opposite of what occurs at a BCS transition where gaps close.

**Causal interpretation**: The entry horizon is a pure geometric event. The spectral action gradient dS/dtau = 68,095 accelerates the modulus past the acoustic barrier. The substrate's eigenvalue topology is undisturbed -- no branch reconnection, no symmetry breaking, no mode transmutation. The analog Hawking temperature T_entry = kappa_v/(2pi) = 72.8 M_KK exists as a kinematic quantity (from the velocity gradient), but it carries zero spectral reorganization content.

This confirms the S70 Hawking workshop proposal (PC1): the entry horizon is an a_2 (geometric) event; the exit horizon is an a_4 (matter) event. The entry is where the modulus breaks the sound barrier. The exit is where the BCS gap opens. These are categorically different horizons.

**Updated horizon classification**:

```
    ENTRY SONIC HORIZON (tau ~ 0.22)         EXIT SONIC HORIZON (tau ~ 0.16)
    ├── Kinematic: Ma crosses 1              ├── Kinematic: Ma crosses 1
    ├── Spectral: NOTHING happens            ├── Spectral: Van Hove fold at 0.19
    │   N_crossings = 0                      │   dB2/dtau = 0 (flat band)
    │   All gaps stable/opening              │   BCS pairing enabled
    ├── Temperature: T_entry = 72.8 M_KK     ├── Temperature: T_compound = 7.578 M_KK
    │   (velocity gradient, no content)      │   (condensate thermodynamics)
    ├── Character: GEOMETRIC (a_2 event)     ├── Character: MATTER (a_4 event)
    └── Analog: Acoustic barrier crossing     └── Analog: Phase transition
```

### II.2 The Moment Hierarchy is Frozen (W2-D)

The spectral moment fractions f_k = a_k / sum(a_j) are:

| Moment | f(fold) | Range across [0.10, 0.30] | Variation |
|:-------|:--------|:--------------------------|:----------|
| f_0 (mode count) | 0.6094 | [0.604, 0.622] | 2.95% |
| f_2 (gravity) | 0.2627 | varies 3.69% | 3.69% |
| f_4 (gauge) | 0.1278 | varies 6.57% | 6.57% |

The hierarchy a_0 > a_2 > a_4 > a_6 holds at EVERY tau-slice in the transit region. No moment transitions occur. The PE1 proposal (S70) that absolute moment dominance switches across causal zones is NOT confirmed.

The physically significant result is the DIFFERENTIAL response: |d ln a_4 / d ln a_2| = 1.43 at the fold. The gauge moment responds 1.43x faster than the gravity moment to the Jensen deformation. This is consistent with the exit horizon being controlled by a_4 (through the Yang-Mills coupling that sets the BCS gap), while the entry horizon is controlled by a_2 (through the spectral action gradient that determines the modulus velocity).

The moment ratio a_2/a_4 = 2.055 at the fold varies by only 2.9% across transit. The gravity-to-gauge balance is approximately preserved -- the substrate's spectral weight shifts uniformly, not selectively.

**Causal structure implication**: The sonic horizons are kinematic events painted onto a spectrally rigid background. The substrate's spectral content does not reorganize to create horizons. The horizons exist because velocity exceeds sound speed, not because the spectral structure transitions. This is the substrate analog of a sonic boom in air: the medium does not change its equation of state at the Mach cone.

### II.3 The GSL Extends to Frustrated Topology (W1-H)

S_gen is monotonically non-decreasing at all 4 stages on the 3-cell frustrated ring:

```
    S_gen (nats):   0.752  -->  0.793  -->  4.294  -->  19.507
    Stage:          BCS        transit      GGE         Gibbs
    dS_gen:              +0.042      +3.500       +15.213
```

This extends the S64/S70 two-cell result to the simplest non-trivial graph topology on CG(24). The frustration (120-degree phase separation in ground state, E_frust = 5.985 M_KK) reduces per-cell GGE entropy by 48% but does not threaten GSL monotonicity.

The non-trivial content is the S_a2 behavior: the spectral entropy from the a_2 Seeley-DeWitt coefficient decreases by 0.002 nats from Stage 3 to Stage 4. This is the substrate analog of a black hole losing area to superradiance -- the generalized entropy (geometric + matter) still increases because the matter entropy gain (+15.2 nats) overwhelms the geometric decrease by 4 orders of magnitude.

The frustrated ring topology is significant because it is the minimal loop on CG(24). If the GSL held only on linear chains, one could argue it was an artifact of the chain topology. Its extension to the frustrated ring suggests the GSL is a STRUCTURAL property of the spectral action, a consequence of spectral monotonicity rather than topology-specific fine-tuning.

### II.4 BH Third Law: Category Error Exposed (W1-G)

S_projected / (pi * Q^2) = 0.01. FAIL by a factor of 100.

The D_K spectral entropy (Shannon entropy of the a_2-weighted eigenvalue distribution, S_projected = 6.945 nats across 1,232 distinct eigenvalues) measures the statistical uniformity of eigenvalue contributions to the gravitational moment. The denominator pi * Q^2 = a_2/4 = 694 measures the magnitude of integrated scalar curvature. These are categorically different quantities.

| Quantity | Value | What It Measures |
|:---------|:------|:-----------------|
| S_projected | 6.945 nats | How uniformly modes contribute to a_2 |
| pi * Q^2 | 694.0 | How much curvature the spectrum produces |
| Ratio | 0.010 | Statistical vs magnitude = category mismatch |

The information deficit Delta_S = S_full - S_projected = 0.082 nats (only 1.2% entropy loss from the a_2 projection vs the uniform a_0 projection). The participation ratio PR(a_2) = 943 (76.5% of modes contribute). The gravitational projection is broadly distributed, not concentrated.

**Implication**: The Bekenstein-Hawking entropy S_BH = A/(4G_N) is an emergent quantity requiring the fabric tessellation (N_cells copies of D_K) and the a_2 hierarchy (M_Pl >> M_KK) to reach its 4D value. The fiber-level spectral entropy cannot reproduce it because a single fiber's spectral content (order 7 nats) measures information capacity, while S_BH (order 10^{77} for a solar-mass object) measures the 4D spatial extent of the horizon in Planck units. The FAIL closes the direct fiber-to-BH-entropy identification but leaves intact the S70 projection-artifact interpretation of the information paradox: information loss arises from discarding the a_0 and a_4 spectral moments in the 4D reduction.

### II.5 Weyl Two-Loop: Protection Weakened but Survives (W1-F)

delta_2(|C|^2)/|C|^2 = 1.003e-3. Marginal FAIL (threshold was 10^{-6}).

The one-loop Weyl protection (S70 KRETSCHNER-BCS-70) is exact: delta_1 = 0. This follows from the SU(3) singlet selection rule -- the BCS condensate is a singlet; the Weyl tensor transforms in the 27 of SU(3). Direct coupling vanishes to all orders. At two-loop, BCS modifies internal propagators in the sunrise diagram, generating an indirect correction at order (Delta/M_KK)^4 * N^2/(16 pi^2) = 1.0e-3.

The series converges rapidly: delta_3 ~ 3.7e-9, all-orders bound 1.16e-3. The loop expansion parameter lambda = 0.137, minimal term at n ~ 7 (we are at n = 2, deep in convergence).

**Retraction and replacement**: The S70 conjecture that BCS protection of |C|^2 extends to all orders at the 10^{-6} level must be RETRACTED. Replaced by the proven statement: delta(|C|^2)/|C|^2 < 1.2e-3 to all orders, with the leading nonzero correction at two-loop. The Weyl tensor -- and with it the Petrov classification -- is practically stable (0.1% shift) but not absolutely protected.

**Causal structure impact**: The Penrose diagrams (Diagram A, F in Phononic-Penrose-Diagrams.md) remain valid. The Petrov type D classification at static tau, and the D -> G -> D transit sequence, are insensitive to a 0.1% shift in |C|^2. The curvature sign hierarchy K_sect(0.537) < lambda_Weyl(0.895) < Ric(1.382) is unperturbed at this level.

### II.6 Chirp Universality Confirmed (W2-B)

The physical chirp rate d^2(lambda)/dt^2 agrees to machine precision (max disagreement 8.1e-10) across lab, comoving, and conformal frames for all 8 BCS modes. This is an exact result, not approximate.

**Structural theorem**: At the van Hove fold, d(lambda)/dtau = 0 (standing wave in spectral flow). All connection terms in coordinate transformations are proportional to d(lambda)/dtau and vanish identically. The chirp rate kappa_n = d^2(lambda_n)/dtau^2 is a GEOMETRIC INVARIANT of the spectral flow, the analog of geodesic curvature at a turning point.

This result is relevant to causal structure because it confirms that the fold's spectral content is coordinate-independent. The spectral action gradient, the BCS pairing, and the sonic horizons are all described in terms of quantities that do not depend on the choice of time coordinate.

### II.7 Squeeze Overcorrection and Decoherence as Regulator (W1-D, W2-A)

The SU(1,1) compound squeeze is exact to machine epsilon (|det(S_eff) - 1| = 8.1e-15). The BCS squeeze parameters alone produce delta_OOM = 2.07, which is 7.7x the 0.267 OOM target gap. Adding Leggett and spatial channels brings this to 9.8x at r_spatial = 0.55.

The decoherence band [t_dec/t_tr in [1.12, 26.5]] produces delta_OOM in [0.568, 1.970]. At the physically favored interior point t_dec/t_tr = 5.0, the compound squeeze overcorrects A_s by 1.089 OOM.

**Causal structure interpretation**: The squeeze parameters are set at the van Hove fold (the white hole interior). The decoherence timescale determines how much of that squeeze survives the exit horizon crossing. This is the substrate analog of Hawking radiation filtering: the horizon determines what escapes, not what is produced. The white hole produces enormous squeeze; the exit horizon + decoherence regulates it down to the observed A_s.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Classification |
|:-----|:-------:|:----------------|:---------------|
| SPECTRAL-ZETA-THRESHOLD-71 | **INFO** | S_inf = 2.353, truncation 10.2% | GEOMETRIC |
| HIGHER-ORDER-CCM-71 | **PASS** | delta = 0.269 > 0.25 (but anti-correlation persists) | GEOMETRIC |
| INTER-SITE-ENTANGLE-71 | **INFO** | S_vN = 2.00 bits, 2.28x above squeeze prediction | PHONONIC |
| DECOHERENCE-BAND-71 | **PASS** | SU(1,1) exact, delta_OOM in [0.568, 1.970] | PHONONIC |
| NON-TRIVIAL-FIBRATION-CSQUARED-71 | **INFO** | delta(c_s^2) = 4.26e-4 < 10^{-3} (SAFE); alpha_s NOT relieved | GEOMETRIC |
| WEYL-TWO-LOOP-71 | **FAIL** | delta_2 = 1.003e-3 > 10^{-3} (marginal) | GEOMETRIC |
| BH-THIRD-LAW-71 | **FAIL** | S_proj/(pi Q^2) = 0.01 (category error) | GEOMETRIC |
| THREE-CELL-GSL-71 | **PASS** | S_gen monotone all 4 stages | PHONONIC |
| R-SPATIAL-SCAN-71 | **INFO** | r_spatial_critical DNE; BCS alone closes gap 7.7x | PHONONIC |
| CHIRP-UNIVERSALITY-71 | **PASS** | max disagreement 8.1e-10 (machine precision) | GEOMETRIC |
| ENTRY-HORIZON-SPECTRUM-71 | **INFO** | N_crossings = 0, T_entry = 72.8 M_KK | GEOMETRIC |
| CAUSAL-MOMENT-MAP-71 | **INFO** | Hierarchy a_0>a_2>a_4>a_6 FROZEN, no transitions | GEOMETRIC |
| DESI-DR3-SCENARIO-B-71 | **INFO** | 2.88-sigma tension (FW), 1.70-sigma (LCDM) | NON-PHONONIC |
| 21CM-ISW-PREREGISTRATION-71 | **INFO** | +4.0% ISW enhancement, SNR = 4.16 (ideal 21cm) | PHONONIC |
| DISCRETE-RW-UNIVERSALITY-71 | **INFO** | max D_KL = 0.153 (partial universality) | GEOMETRIC |
| ALPHA-S-BAYESIAN-SHADOW-71 | **INFO** | 17.7% max systematic (1-sig), zeta 10.2% tighter | NON-PHONONIC |
| CORRELATED-SENSITIVITY-71 | **INFO** | d(ln omega_L)/d(alpha) = -0.44 (ROBUST) | GEOMETRIC |
| CC-FROM-GGE-RESIDUAL-71 | **FAIL** | 110.09 OOM gap (expected; q-theory sole survivor) | PHONONIC |
| BCS-BACKREACTION-a4-71 | **PASS** | delta(a_4)/a_4 = 2.02e-8 (physical) | PHONONIC |
| GGE-HAWKING-ANALOG-71 | **INFO** | C_V(GGE)/C_V(thermal) = 0.0023 (430x suppression) | PHONONIC |

---

## IV. Structural Implications

### IV.1 Causal Architecture Update

The definitive Penrose diagram set (Phononic-Penrose-Diagrams.md, 9 diagrams) requires the following updates from S71:

**Entry/exit asymmetry confirmed quantitatively**. Diagram B (modulus space) should annotate the entry horizon at tau = 0.22 as "N_crossings = 0, purely kinematic" and the exit region at tau ~ 0.16-0.19 as "van Hove fold, BCS flat band, spectral reorganization." The S70 4-panel acoustic Penrose sequence (Penrose-Sequence-70) gains the spectral annotation that the entry panel (tau = 0.221, near-sonic) has undisturbed eigenvalue topology while the fold panel (tau = 0.190, white hole) has the van Hove singularity in the spectral flow.

**Moment hierarchy is structural background, not dynamical actor**. The spectral moments do not transition during transit. The causal zones (subsonic -> supersonic -> subsonic) are painted by modulus velocity onto a spectrally rigid fabric. This simplifies the Penrose diagram interpretation: all causal structure is kinematic. The spectral content provides the equation of state; the dynamics provides the horizons.

**Six-layer censorship updated**: The S62 six-layer censorship (energy, friction, no trapped surfaces, Josephson, fragmentation, one-loop stabilization) gains additional support from the frozen moment hierarchy. The spectral moments do not develop instabilities during transit that could breach the censorship layers.

### IV.2 The White Hole Interior Recharacterized

Diagram I-1 (white hole analogy) needs revision in light of W1-D and W2-A. The white hole interior (supersonic region, tau in [0.16, 0.22]) produces enormous squeeze (delta_OOM = 2.07 from BCS alone). The S39/S53 white hole comparison remains structurally sound, but the exit mechanism is now clearer: decoherence at the exit horizon regulates the squeeze amplitude. The white hole emits a regulated, anti-thermal, product-state signal -- not the thermal Hawking radiation of a Schwarzschild white hole.

```
    SCHWARZSCHILD WHITE HOLE              SUBSTRATE WHITE HOLE (revised S71)

    Past singularity (r = 0)              Round SU(3) (tau = 0, regular)
         |                                     |
         v                                     v
    INTERIOR (expanding)                  SUPERSONIC INTERIOR
    Pair creation (thermal)               Squeeze production (anti-thermal)
    T_Hawking = kappa/(2pi)               delta_OOM = 2.07 (BCS)
         |                                     |
         v                                     v
    EVENT HORIZON (null, r = 2M)          EXIT SONIC HORIZON (tau ~ 0.16)
    Thermal emission                      Decoherence-regulated squeeze
    S_BH = A / (4 G_N)                   S_GGE = 3.54 bits
         |                                     |
         v                                     v
    EXTERIOR (static)                     POST-TRANSIT GGE (w = 0.202)
    Asymptotically flat                   Decelerating FRW
```

The overcorrection (7.7x the target) means the white hole interior is far more productive than needed. The observed A_s = 2.1e-9 requires destructive interference or decoherence at the exit to tame the raw squeeze. The decoherence mechanism plays the role of the horizon: it determines what the exterior observer sees.

### IV.3 GSL as Structural Property

The extension of the GSL from 2-cell chains (S64, S70) to the 3-cell frustrated ring (W1-H) is the minimal step needed to argue universality on CG(24). The next test is the full 32-cell lattice, but the frustrated ring already contains the essential complication (topological frustration with circulating currents |I_J| = 0.808 M_KK).

The S_a2 non-monotonicity (decrease of 0.002 nats at Stage 3 -> 4) is structurally analogous to the black hole area decrease under superradiance: the geometric sector can lose entropy if the matter sector gains sufficiently. The ratio (4 orders of magnitude margin) means this is not a fine-tuning issue.

### IV.4 Constraint Map Updates

**Closures**:
- CC via direct GGE residual: CLOSED (110.09 OOM). Q-theory sole survivor.
- All-orders Weyl protection conjecture: RETRACTED. Replaced by delta < 1.2e-3 bound.
- Fiber-level BH entropy: CLOSED (category error). S_BH requires 4D tessellation.

**Confirmed protections**:
- c_s^2 = 0 robust against non-trivial fibration: delta(c_s^2) = 4.26e-4, quadratic suppression.
- a_4 gauge couplings safe from BCS: delta(a_4)/a_4 = 2.02e-8 (physical).
- Leggett frequency robust: |d(ln omega_L)/d(alpha)| = 0.44 (below 0.5 threshold).
- Chirp rate geometric invariant: frame-independent to machine precision.

**Persistent tensions**:
- alpha_s extraction: non-trivial fibration gives 4.2%, a_6 gives 26.9%, combined ~10.7%. Need 781%. Still 73x short.
- w_a: framework predicts 0; DESI DR2 gives -0.73. Even Scenario B (w_a = -0.30) gives 2.14-sigma tension. w_a is the decisive vulnerability.
- A_s: overcorrection by 7.7x (BCS alone). Decoherence is the necessary regulator.

---

## V. Forward Projection

### V.1 Next Decisive Computations for Causal Structure

1. **Exit horizon eigenvalue tracking**. W2-C established the entry horizon as spectrally featureless. The symmetric computation for the exit (tau in [0.14, 0.19]) would complete the entry/exit asymmetry characterization. The van Hove singularity (dB2/dtau = 0 at tau = 0.19) means N_crossings should be nonzero at the exit, confirming the a_4 character.

2. **Full 32-cell GSL**. The 3-cell frustrated ring (W1-H) passes. The 32-cell Voronoi tessellation of SU(3) is the physical system. Does the GSL hold on the full lattice? The computation is expensive (Hilbert space dimension grows exponentially with cell count) but could be attacked with DMRG or variational methods.

3. **Decoherence mechanism from first principles**. W1-D shows the decoherence band regulates A_s. But t_dec/t_tr is currently a free parameter in [1.12, 26.5]. Computing it from the substrate dynamics (e.g., from the B2 dephasing rate, or from the acoustic Hawking temperature) would reduce the A_s prediction to zero free parameters.

4. **c_s^2 direct measurement prospects**. W2-F establishes the pre-registered chain to 21cm ISW cross-correlation. The +4.0% substrate-specific signal requires ideal all-sky 21cm IM at z ~ 0.4-3 (SNR = 4.16, achievable post-2035). This is the unique discriminant between the substrate tracking vacuum (c_s^2 = 0) and quintessence (c_s^2 = 1).

### V.2 Causal Structure Open Questions (updated from Phononic-Penrose-Diagrams.md)

Questions 1 (8D BLV formula) and 2 (post-transit acoustic metric existence) from the definitive diagram document remain open and are now more urgent. The frozen moment hierarchy (W2-D) means the acoustic metric's equation of state is constant during transit, which constrains the 8D generalization. The decoherence-as-regulator finding (W1-D, W2-A) makes question 2 critical: if the post-transit GGE has no condensate, the BLV acoustic metric may not exist, and the decoherence mechanism would need to operate before condensate destruction.

Question 6 (acoustic horizon during c_s transition) is now PARTIALLY ANSWERED: the entry horizon has no spectral content (W2-C), so the c_s transition at the exit is where any transient acoustic horizon would form. The exit eigenvalue tracking computation (V.1 item 1 above) would resolve this.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:------:|:------------|
| 1 | Entry horizon spectrally featureless (N_crossings = 0) | GEOMETRIC | INFO | Entry/exit asymmetry confirmed: entry = kinematic, exit = spectral |
| 2 | Moment hierarchy frozen (a_0 > a_2 > a_4 > a_6 at all tau) | GEOMETRIC | INFO | Causal structure is kinematic, not spectral. Background spectrally rigid. |
| 3 | GSL on 3-cell frustrated ring (S_gen monotone 4/4) | PHONONIC | PASS | GSL is structural, survives minimal loop topology |
| 4 | BH third law (S_proj/pi Q^2 = 0.01) | GEOMETRIC | FAIL | Category error: fiber entropy != BH entropy. S_BH requires tessellation. |
| 5 | Weyl two-loop (delta_2 = 1.003e-3) | GEOMETRIC | FAIL | All-orders protection retracted. Replaced by delta < 1.2e-3. Practical stability. |
| 6 | Chirp universality (max disagreement 8.1e-10) | GEOMETRIC | PASS | Spectral flow curvature is geometric invariant. Coordinate-independent. |
| 7 | Decoherence band (delta_OOM in [0.568, 1.970]) | PHONONIC | PASS | Decoherence regulates A_s overcorrection. White hole overproduces by 7.7x. |
| 8 | r_spatial critical DNE (BCS alone 7.7x gap) | PHONONIC | INFO | BCS squeeze dominates; r_spatial is 11% perturbation |
| 9 | c_s^2 robust vs fibration (delta = 4.26e-4) | GEOMETRIC | INFO | c_s^2 = 0 prediction safe. alpha_s tension persists (73x short). |
| 10 | S_inf = 2.353 (spectral zeta, 10.2% truncation) | GEOMETRIC | INFO | L=7 sign reversal = decoupling onset. Physical sum terminates at L=6. |
| 11 | a_6 CCM shift = 26.9% (PASS but anti-correlation persists) | GEOMETRIC | PASS | a_6 shifts Higgs quartic but cannot break f_0 anti-correlation |
| 12 | Inter-site entanglement (S_vN = 2.00 bits, 4-state manifold) | PHONONIC | INFO | Josephson junction creates 4-state entangled manifold, not 2-mode squeeze |
| 13 | CC from GGE residual (110 OOM gap) | PHONONIC | FAIL | Direct GGE-residual CC closed. Q-theory sole survivor. |
| 14 | a_4 BCS backreaction (delta = 2.02e-8) | PHONONIC | PASS | Gauge couplings safe from BCS. IR/UV decoupling structural. |
| 15 | DESI DR3 Scenario B (2.88-sigma FW, 1.70-sigma LCDM) | NON-PHONONIC | INFO | w_a is decisive vulnerability. Framework survives Scenario B marginally. |
| 16 | 21cm ISW pre-registration (+4.0% enhancement) | PHONONIC | INFO | Substrate-specific signal detectable post-2035 with ideal 21cm IM |
| 17 | Cayley graph partial universality (D_KL = 0.153) | GEOMETRIC | INFO | S_4 family consistent; S_5 family deviates. d_s undefined on finite graphs. |
| 18 | Pantheon+ alpha_s shadow (17.7% at 1-sigma) | NON-PHONONIC | INFO | Spectral zeta (10.2%) is binding constraint, not Pantheon+ |
| 19 | Leggett frequency robust (sensitivity 0.44) | GEOMETRIC | INFO | omega_L survives spectral function variation. Ratio cancellation. |
| 20 | BEC analog C_V prediction (430x suppression) | PHONONIC | INFO | Experimentally accessible GGE fingerprint. ^39K Feshbach quench at 8 muK. |
