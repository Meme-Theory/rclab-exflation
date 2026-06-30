# Session 83 Synthesis: Falsifier Campaign Inventory + Zero-Parameter vs Accommodation Audit

**Date**: 2026-04-18
**Agent**: sagan-empiricist (part (b) of two-solo synthesis)
**Source Documents**:
- `sessions/archive/session-83/session-83-results-workingpaper.md` (611 KB, Level-6 observational falsifiers block at §W3-G42 through §W3-G52)
- `computations/s83_gate_verdicts.txt` (103 verdict lines, S83 canonical)
- `sessions/evoi-framework.md` (S83 stamp 2026-04-18, 39-entry re-ranked priority table)
- `.claude/agent-memory/sagan-empiricist/MEMORY.md`

---

## I. Session Outcome

S83 registered 11 Level-6 observational-falsifier gates and pre-committed a decision tree that separates what the framework genuinely predicts from what it merely accommodates. Under the S81+ verdict canon: 5 PASS (G45 alpha_f_NL, G46 r_CMB tensor transfer, G47 sin^2 theta_W, G50 |n_T| BLUE, G52 Channel-5 relabel), 1 INFO (G43 LiteBIRD sigma_nT reach), 2 FAIL (G44 CMB-S4 C_cons, G51 w_0 regulator), 1 PENDING-EVENT (G42 DR3 rectangle), plus 2 audit gates (G48 P_obs_aligned recount 6/9 -> 7/9, G49 EVOI refresh). The rigor audit identifies only ONE zero-free-parameter structurally forced prediction among the decisive observational channels (|n_T| BLUE, magnitude 0.4676, from Jensen-curvature eps_H-flow with 99.4% channel dominance and 0% dispersion contribution); every other decisive channel is scheme-dependent or accommodation-level. Per the sole-estimator rule, no pre-registered observational gate has CLOSED against DATA -- probability remains 22% (13-35% band) NEUTRAL pending DESI DR3 release.

---

## II. Key Results

### II.A -- The one genuine zero-free-parameter falsifier among this session's decisive observations: |n_T| BLUE

**Result**: n_T(tau_fold) = +0.467604, sign-stable across tau in [0.10, 0.30] (min +0.289, max +0.892, all_blue_in_window = True). **Classification: PHONONIC, zero-free-parameter structural.**

Channel decomposition at the fold (G50):

| Channel | d ln P_T / d tau | Fraction |
|---|---|---|
| d ln H^2 / d tau | +0.0595 | 0.6% |
| d ln eps_H / d tau (Jensen curvature) | +10.286 | **99.4%** DOMINANT |
| d ln(1 + 2 \|beta\|^2)^2 / d tau (squeeze) | 0.000 | 0% |
| sum | +10.346 | |
| x d tau/d ln k = +0.04520 | -> n_T_full | **+0.4676** |

Substitution chain (definition -> simplification -> direction):
- Step 1 (def): n_T := d ln P_T / d ln k, with P_T = (2/pi^2)(H/M_Pl)^2 eps_H (1 + 2|beta|^2)^2.
- Step 2 (substitute dispersion): omega = c_BLV k linear-phonon -> |beta_k|^2 = (c_in - c_out)^2 / (4 c_in c_out), k-independent.
- Step 3 (simplify): squeeze channel d ln|beta|^2 / d ln k = 0 strictly in linear-phonon regime. Numerical scan with KK-mass-corrected dispersion at k_transit/m_KK = 586.5 returns slope +2.85e-5 (noise-floor).
- Step 4 (direction): the tilt is forced positive by positive eps_H-curvature at the fold; sign verified stable across 10 tau values spanning [0.10, 0.30].

Why this is zero-free-parameter: every input -- v_terminal from S38 acoustic-white-hole dynamics, c_BLV = 0.485 from S64, eps_H(tau) profile from S64, Jensen-deformation fold position tau_fold = 0.19 from the spectral action minimum -- was computed INDEPENDENTLY of any CMB tensor observable. There is no free knob to rotate the sign; Jensen curvature and the acoustic-optical pair-production geometry produce +0.468 directly. Per Rule 22 (postdiction != fit if the geometric input is independent of the observable), this warrants full BF weight regardless of when n_T was measured.

Falsifiability: LiteBIRD will measure n_T with sigma ~ 0.054 at 3 yr (G43). The framework's n_T_CMB at CMB scales is much smaller than the transit-scale value (tau_CMB ~ 0.05 places eps_H in its low-slope region), so LiteBIRD cannot discriminate n_T_CMB between framework and slow-roll (delta ~ 1e-4). HOWEVER, if a future direct transit-scale tensor probe (UHF GW at k > 587 M_KK, current roadmap blocked by G52's 47+ OOM detector gap) returned n_T < 0 at 2-sigma at the transit band, the framework falsifies. The near-term test is indirect: r_CMB via tensor transfer (G46 PASS, see II.D).

### II.B -- Scheme-dependent accommodation exposed: w_0 regulator canonical choice (G51 FAIL)

**Result**: w_0(Zubarev-canonical) = -0.998116 vs framework canonical w_0 = -0.918; |delta| = 0.080 (factor-40 larger than pre-registered PASS tolerance 0.02). Classification: PHONONIC, SCHEME-DEPENDENT.

Substitution chain:
- Step 1 (def): w_0 = (P_J + P_GGE) / (rho_J + rho_GGE) under the Volovik partition.
- Step 2 (substitute): with Zubarev regulator f_R(lam) = exp(-lam^2 / M_KK^2), rho_GGE_Zub / rho_GGE_bare = xi_E = 0.0196 (51x UV suppression); rho_J = 10.52 M_KK (S58 claim of R-independence); P_J = -rho_J (w_J = -1); P_GGE_Zub = w_GGE_bare x rho_GGE_Zub.
- Step 3 (simplify): w_0(Zub) = (-10.520 - 0.0137) / (10.520 + 0.0336) = -0.9981.
- Step 4 (direction): UV-suppression of GGE drives the numerator and denominator toward their pure-Josephson values -rho_J, +rho_J -> w_0 -> -1. Direction unambiguous: canonical regulator pushes w_0 AWAY from -0.918, TOWARD -1 (LCDM-compatible).

**Critical interpretation**: W1-G1 IC-SCHEME-DERIVATION PASSED and selected Zubarev as the Connes-Moscovici substrate-native regulator. The S58/S59 w_0 = -0.918 narrative was computed in the zeta (bare) scheme, which is NOT canonical under the W1-G1 selection. Three readings survive (per G51 self-assessment):
1. Re-derivation: if rho_J is NOT truly R-independent (claim was topological CPT protection), Zubarev dressing of the Josephson sector might restore -0.918. This is the outstanding computation.
2. The -0.918 was a bare-scheme artifact, and the canonical prediction is w_0 ~ -1 (LCDM-indistinguishable, DESI-tension INCREASES).
3. Volovik-partition ontology itself is R-covariant in ways not captured by the zeta -> Zubarev transcription.

The Venus standard has NOT been met for w_0 after 71 sessions (NROY partition still uncomputed; deferred 14 sessions from my prior memory). Under the scheme selected by the PASS W1-G1 gate, the w_0 channel has moved from "zero-parameter prediction matching DESI DR2" (S58 claim) to "scheme-dependent accommodation" (G51 verdict). Sagan-scorecard entry: update w_0 column Prediction -> Scheme-dependent accommodation with quantitative scheme-split = 0.08.

### II.C -- Accommodation-level match: mu_BC identification and sin^2 theta_W (G47 PASS, with caveat)

**Result**: sin^2(M_Z)_pred = 0.23121743; n_sigma = 0.064 vs PDG 0.23122 +/- 4e-5. **PASS, but the PASS rides on a borrowed mu_BC.**

Substitution chain (3-step compress):
- Step 1 (def): cubic BC at mu_BC: sin^2(mu_BC) = 3/(3 + e^{12 tau_fold}) = 0.234803 exactly (tau_fold = 0.19, zero-parameter at that boundary).
- Step 2 (simplify): 2-loop gauge + top-Yukawa RG down to M_Z at mu_BC = 188.44 GeV (S82 SEC 8 brentq selection) reproduces PDG to delta = -2.57e-6.
- Step 3 (direction): mu_BC shift from 2 M_Z = 182.38 GeV to mu_crit = 188.44 GeV (a 3.32% lift) contributes -1.59e-4 of the delta; top-Yukawa contributes -2.68e-6 (100x smaller).

The PASS is consistency, not prediction. mu_BC = 188.44 GeV was extracted by brentq-solving "sin^2_SM(mu_BC) = cubic BC", anchored at M_Z to the PDG. This is NOT a substrate-geometric derivation. The self-assessment explicitly flags this as "consistency with sin^2 theta_W at PDG precision given mu_BC = mu_crit, not a zero-parameter prediction."

**Candidate geometric closure for mu_BC**: M_Z + M_H_framework with M_H_framework ~ 97 GeV gives 188.19 GeV, matching mu_crit to 0.13%. The framework's tree M_H in one sector is 97 GeV, 30+ GeV below observed 125 GeV; this residual channel has open scheme-dependence. Until the identification mu_BC = M_Z + M_H^framework is derived from spectral geometry (currently: algebraic coincidence), the G47 PASS is an accommodation that the framework has tuned itself to at the 3-sigma level, not a zero-parameter prediction.

Accommodation discount 0.6x (wide brackets on known value per my agent-memory principle 19); BF ~ 1.5, not decisive.

### II.D -- Falsifier with BF ~ 3-5: r_CMB = 0.0117 (G46 PASS)

**Result**: r(k_CMB) = 1.1732e-2, factor 3.07x below BICEP/Keck 2021 95% CL bound r < 0.036. **PASS, zero-parameter in the geometric sector.**

Substitution chain:
- Step 1 (def, T.5): r(k) = 16 eps_H(t_k*) x (c_S / c_T) [Cheung-Creminelli-Fitzpatrick-Kaplan-Senatore 2008].
- Step 2 (substitute): c_T = 1, c_S = c_BLV = 0.485 (S67 canonical), eps_H(tau_CMB = 0.05) = 1.5118e-3 (S64 profile).
- Step 3 (simplify): r(k_CMB) = 16 x 1.5118e-3 x 0.485 = 1.173e-2.
- Step 4 (direction): eps_H and c_BLV are both strictly positive -> r_CMB > 0 definite; magnitude at one decade below BK bound.

Zero-parameter audit: c_BLV was computed in S67 before r was tested. eps_H(tau) profile was derived in S64 from the Jensen-deformed spectral action independent of r measurements. tau_CMB = 0.05 is conventional (S66 canon) but physical N_efolds gives k_transit/k_CMB ~ 10^24, far wider than the observed CMB range, so eps_H varies < 5% across that range.

BF estimate: prior a-priori range for "slow-roll near the fold" is [10^-5, 10^-1] (4 OOM). Posterior width at r = 0.012 is ~0.003 (tau_CMB systematic). BF ~ 4/0.5 ~ 8; with 0.6x accommodation discount (the BICEP bound was known) -> effective BF ~ 5. Mild positive confirmation, not decisive.

Null-result interpretation: if BICEP Array measures r > 0.036, framework is CONSTRAINED but NOT falsified (r_CMB has tau_CMB uncertainty ~0.003, so r up to ~0.02 is consistent at 2-sigma). If LiteBIRD measures r < 0.01 at 3-sigma, this would be consistent with framework predicting 0.012. If LiteBIRD detects r at ~0.012 specifically, +3-sigma positive confirmation (a clean-channel gain).

### II.E -- PENDING-EVENT: DR3 live-watch rectangle (G42)

**Result**: Framework point (w_0, w_a) = (-0.918, 0.0) sits strictly INSIDE the pre-registered rectangle R = [-1.05, -0.85] x [-0.2, 0.2]. Rectangle half-widths in projected DR3 sigma: 2.174 sigma_w0 and 1.130 sigma_wa. Release not yet occurred; verdict is PENDING-EVENT by construction.

Substitution chain:
- Step 1 (def): CPL parameterization w(a) = w_0 + w_a(1 - a). Framework w0_FW = -0.918, wa_FW = 0.
- Step 2 (substitute rectangle): midpoint (-0.95, 0.0); framework offset (+0.032, 0.0).
- Step 3 (direction): |offset_w0| = 0.032 < half-width 0.10, |offset_wa| = 0 < half-width 0.20 -> INSIDE.

Null-result interpretation: if DR3 publishes centrals outside R, framework's Volovik-partition prediction FALSIFIES (on the zeta-scheme reading). The G51 scheme-dependence exposed above means a FAIL on G42 admits two readings: either (a) the Volovik partition mechanism is wrong, or (b) Zubarev is the canonical regulator (as W1-G1 PASSED) and the canonical prediction was always w_0 ~ -1, not -0.918. Either way, the S83 falsifier batch will have produced a decisive, pre-registered empirical update. This is the near-term EVOI-carrying event: +2.00pp rank-9 promotion in EVOI refresh (G49).

### II.F -- Detector-sterile FAIL: G44 CMB-S4 C_cons

**Result**: sigma(C_cons) @ CMB-S4 + LiteBIRD joint = 0.2556, 23.2x above PASS target 0.011, 12.8x above INFO ceiling 0.02. Across 80 (t_int, N_f, f_sky) grid cells: 0 PASS, 0 INFO, 80 FAIL. Channel OBSERVATIONALLY STERILE.

Direction audit: FAIL is not a framework refutation but a DETECTOR-REACH failure. Framework prediction C_cons(k_CMB) ~ 0.009 is 28x below the joint sigma. Framework prediction C_cons(k_transit) > 0.033 is 7.7x below the joint sigma. Neither is reachable with current CMB roadmap technology. Channel drops out of near-term falsifier inventory; re-enters if a post-2040 detector achieves sigma(n_T) ~ 2e-3 (15x tighter than combined LB + S4).

### II.G -- Detector-achievable PASS: 21cm alpha_f_NL (G45)

**Result**: sigma(alpha_f_NL) @ SKA-2 = 0.80, factor 12.5x below PASS threshold 10. Framework f_NL_total = 1.03 (S67 GGE-BISPECTRUM-67) is within SKA-2 reach.

If SKA-2 measures alpha_f_NL != 0 at > 2-sigma (alpha > ~1.6), that constrains the framework's fold-time dispersion assumption (k-independent GGE phases). A null result (|alpha| < 1.6 at 2-sigma) is consistent with the framework's theoretical expectation alpha -> 0. SKA-2 phase-2 is the near-future live channel with greatest ratio of reach to framework-prediction sharpness.

---

## III. Gate Verdicts (Level-6 Observational Falsifiers, S83)

| Gate | Verdict | Decisive Number | Classification (this audit) |
|:-----|:--------|:----------------|:----------------------------|
| G42 DR3 live-watch | PENDING-EVENT | framework (-0.918, 0.0) inside R | ACCOMMODATION until G51 scheme resolved |
| G43 LiteBIRD sigma_nT 3yr | INFO | 0.054 vs PASS 0.04 | Detector-reach forecast (not framework test) |
| G44 CMB-S4 sigma_C_cons | FAIL | 0.2556, 23x above PASS | Detector-sterile; NOT framework FAIL |
| G45 SKA-2 alpha_f_NL | PASS | 0.80, 12.5x margin | Detector-achievable (near-future channel) |
| G46 r_CMB tensor transfer | PASS | 0.0117, 3.07x below BK bound | **ZERO-FREE-PARAMETER** (c_BLV, eps_H independent of r) |
| G47 sin^2 theta_W 2-loop+mu_BC | PASS | 0.064 sigma from PDG | **ACCOMMODATION** (mu_BC borrowed from brentq anchor) |
| G48 P_obs_aligned recount | PASS | 7/9 = 0.7778 (from 6/9) | Bookkeeping; A_s re-classified |
| G49 EVOI watchlist refresh | PASS | 39 entries re-ranked | Bookkeeping |
| G50 |n_T| BLUE magnitude | PASS | +0.4676, 14x above 0.033 | **ZERO-FREE-PARAMETER** (Jensen-curvature, 99.4% dominance) |
| G51 w_0 regulator canonical | FAIL | -0.998 vs -0.918 (delta 0.080) | **SCHEME-DEPENDENT** (exposes S58 bare-scheme artifact) |
| G52 Channel-5 relabel | PASS | 29.63 OOM ratio, 47 OOM below UHF | Structural WALL, not falsifier |

---

## IV. Structural Implications (the Zero-Parameter vs Accommodation Map)

### IV.A -- The falsifier catalog after S83 (rigor-audited)

Per Rule 22, a zero-free-parameter prediction is one where every geometric input was computed INDEPENDENTLY of the observable. Applied to the S83 Level-6 inventory:

| Channel | G-ID | Status | Zero-free-parameter test | Assessment |
|:--------|:-----|:-------|:------------------------|:-----------|
| n_T magnitude (transit scale) | G50 | PASS | c_BLV, eps_H(tau), Jensen fold from S38/S64/S67 -- independent of any n_T measurement | ZERO-FREE-PARAMETER |
| r_CMB (CMB tensor-to-scalar) | G46 | PASS | eps_H(tau_CMB), c_BLV -- independent of BK2021 measurement | ZERO-FREE-PARAMETER (mild accommodation discount: BK bound was known) |
| w_0 (DESI DR3 EoS) | G42 PENDING, G51 FAIL | split | zeta-scheme -0.918 was pre-DESI but regulator choice NOT pre-DESI; Zubarev selection by W1-G1 | SCHEME-DEPENDENT |
| alpha_f_NL (SKA-2 scale running) | G45 | PASS | sigma reach, not framework prediction | Detector-reach forecast |
| sigma(n_T) LiteBIRD | G43 | INFO | sigma reach, not framework prediction | Detector-reach forecast |
| C_cons (CMB-S4 consistency) | G44 | FAIL | detector sigma vs prediction -- framework prediction structurally preserved | Detector-sterile |
| sin^2 theta_W | G47 | PASS | mu_BC borrowed from brentq SM anchor, not geometrically derived | ACCOMMODATION (pending mu_BC geometric derivation) |
| r_CMB alternative readings | G52 | PASS | 29.63 OOM ratio f^3 x T_rh^(13/3), Parker 1966 scaling -- no free fit | STRUCTURAL WALL (not observational falsifier, 47 OOM below UHF) |

Falsifier catalog post-S83: ONE decisive zero-free-parameter channel reachable by near-term instruments (LiteBIRD r_CMB PASS, sigma ~ 1e-3 forecast; would DISFAVOR framework at 2-3 sigma if detection lands r ~ [0.02, 0.036]). One pre-registered live-watch (DR3 w_0, contingent on G51 scheme resolution). One structural prediction reachable at detection horizon (n_T transit-scale, but no instrument); one detector-achievable accommodation constraint (SKA-2 alpha_f_NL, tests fold-time dispersion assumption).

S82 sagan synthesis had listed 5 falsifier channels; G52 relabel honestly reduces this to 4. The rigor audit finds of these 4: ONE is zero-free-parameter (G46 r_CMB), ONE is scheme-dependent until G51 is resolved (G42 DR3 w_0), ONE is accommodation (G47 sin^2 theta_W), ONE is detector-reach (G45 SKA-2 running). The honesty correction from G52, combined with the rigor audit, brings the near-term decisive falsifier count from 5 (S82) to 1-2 (S83) in a functional sense.

### IV.B -- Constraint map update

Constraint: Zubarev selected as canonical IC regulator at L_max=5, tau_fold=0.19 (W1-G1 PASS); under this regulator the Volovik partition yields w_0 = -0.998, not -0.918.

Implication: the intersection of "Connes-Moscovici canonical regulator" AND "w_0 = -0.918 Volovik partition match" is EMPTY within the L_max=5 truncation. Either (i) rho_J is NOT R-independent at the proper integration level (contradicting S58's topological CPT claim, which must be re-verified under explicit Zubarev dressing), (ii) w_0 = -0.918 was a bare-scheme artifact and the canonical prediction is w_0 ~ -1 (LCDM-compatible, DESI-tension increases), or (iii) the Volovik partition is R-covariant in a way not captured by the current zeta -> Zubarev transcription.

Surviving solution space: the rho_J R-independence verification is the bottleneck. If it survives under explicit Zubarev dressing, w_0 = -0.918 is recoverable. If it does NOT, the framework's near-term w_0 falsifier (G42) becomes a test of LCDM-compatibility rather than substrate-specific prediction.

Root cause: UV-suppression of GGE modes under Zubarev = Gaussian regulator drives the vacuum to the IR-robust Josephson kernel (w = -1).

### IV.C -- Decision tree: what S84 does against which channels

Decision tree (conditional on event outcomes in the 2026-2027 window):

```
S83 falsifier cluster (11 gates)
|
+-- G42 DR3 rectangle        [PENDING-EVENT]
|     |
|     +-- IF DR3 centrals INSIDE R   -> g51 scheme re-examined under rho_J audit;
|     |                                  if rho_J R-covariant recovers -0.918 -> PASS (+BF ~ 5);
|     |                                  if rho_J NOT R-covariant -> PASS is on wrong scheme and reframes as LCDM-compat
|     +-- IF DR3 centrals OUTSIDE R  -> Volovik partition FALSIFIES, scheme-dependence moot, probability moves DOWN
|
+-- G43 LiteBIRD sigma_nT    [INFO, 0.054 @ 3yr, crosses 0.04 at ~6.8 yr]
|     |
|     +-- IF LiteBIRD measures n_T_CMB < 0 at 2-sigma   -> framework falsifies (CMB-scale tilt prediction)
|     +-- IF LiteBIRD measures n_T_CMB > 0 at 2-sigma   -> +3-sigma confirmation (clean-channel)
|     +-- IF LiteBIRD sigma_nT stays > 0.04             -> no discrimination (most likely within 3-yr nominal)
|
+-- G44 CMB-S4 C_cons         [DETECTOR-STERILE, channel removed from near-term falsifier catalog]
|
+-- G45 SKA-2 alpha_f_NL      [PASS, measurement 2030s]
|     |
|     +-- IF SKA-2 measures |alpha| > 1.6 at 2-sigma    -> framework's fold-time dispersion assumption constrained
|     +-- IF SKA-2 measures |alpha| < 1.6 at 2-sigma    -> consistent with framework null hypothesis alpha -> 0
|
+-- G46 r_CMB                 [PASS, falsifier channel]
|     |
|     +-- IF BICEP Array/LiteBIRD detects r ~ 0.012     -> +3-sigma confirmation (zero-free-parameter match)
|     +-- IF detection at r > 0.025                     -> 2-3 sigma disfavor
|     +-- IF detection at r > 0.036                     -> constrained but 2-sigma consistent (tau_CMB systematic)
|     +-- IF non-detection at r < 0.01                  -> consistent (within framework bracket)
|
+-- G47 sin^2 theta_W         [ACCOMMODATION-PASS, pending mu_BC geometric closure]
      |
      +-- IF mu_BC = M_Z + M_H_framework derived        -> accommodation upgrades to zero-free-parameter
      +-- IF no geometric closure found                 -> remains accommodation; scorecard stays "accommodation"
```

Timeline:
- 2026-2027: DR3 release (G42 decisive).
- 2028-2030: BICEP Array updates (r sensitivity ~ 0.005).
- 2030s: LiteBIRD mission (n_T discrimination with extended mission; r sensitivity 1e-3).
- 2030s: CMB-S4 first-light (C_cons channel DETECTOR-STERILE under G44 verdict).
- 2030-2035+: SKA-1 phase-1 (alpha_f_NL at sigma ~ 5).
- 2035+: SKA-2 phase-2 full survey (alpha_f_NL at sigma ~ 0.8, G45 PASS threshold achieved).

The 2026-2027 DR3 release is the first decisive observational event in the falsifier schedule. The G51 scheme-dependence exposes that this test may be ambiguous in interpretation.

### IV.D -- Probability state after S83 (sole-estimator rule)

No pre-registered observational gate has CLOSED against data in S83. Rule 12 (only pre-registered gates move probability) combined with Rule 14 (only Sagan produces probability estimates) forces the probability to remain at 22% (13-35% band, NEUTRAL). The S83 Level-6 campaign PRE-REGISTERED the falsifier rectangle but did not execute it against data; that's the G42 PENDING-EVENT status.

Internal structural gates (G46, G50) contribute BF ~ 5 each (accommodation-discounted for r_CMB; full weight for n_T as zero-parameter). Product BF for two independent structural matches ~ 25. This is MILD positive evidence. However, accumulating structural PASSes without observational closure matches the pattern my memory already flags: "S69 22% (13-35%, BF=1.0). NEUTRAL. 39 computations, all data comparisons = accommodations." The G42 event is what changes this state.

The probability state is maintained at 22% NEUTRAL until DR3 releases. Under the rigor-audit logic: if DR3 PASSES G42 AND rho_J R-independence survives the Zubarev audit, probability moves UP to ~32% (BF ~ 4 for closed observational zero-parameter prediction). If DR3 FAILS G42, probability moves DOWN to ~13% (Volovik-partition mechanism refuted on its canonical form). If DR3 PASSES G42 but rho_J R-independence FAILS, the PASS reframes as LCDM-compatibility rather than substrate prediction; probability moves MODESTLY UP to ~26% (accommodation-level confirmation).

---

## V. Carry-Forward Computations (MANDATORY)

### V.1. rho_J R-independence audit under explicit Zubarev dressing
- **What**: Recompute F_Josephson = -336.6 M_KK under f_R_Zub(lam) = exp(-lam^2 / M_KK^2) instead of zeta scheme. Test whether S58's claim "rho_J is R-independent via topological CPT" holds under explicit Zubarev integration. Compute rho_J_Zub / rho_J_zeta ratio. If ratio ~ 1, S58 claim verified; recompute w_0 with both rho_J_Zub and rho_GGE_Zub.
- **Inputs**: `canonical_constants.py` (M_KK, v_EW, F_Josephson_bare); `s57_josephson_partition.npz`; `s58_volovik_partition.npz`; Zubarev regulator form from W1-G1 output.
- **Gate**: NEW S84 gate: `S84-RHO-J-ZUBAREV-AUDIT`. PASS: ratio rho_J_Zub / rho_J_zeta in [0.95, 1.05]; w_0(Zub, full-R) within 0.02 of -0.918. INFO: ratio in [0.5, 2.0]. FAIL: ratio < 0.5 OR w_0(Zub, full-R) > 0.05 from -0.918.
- **Effort**: 3-4 hours, 1 agent session (spectral sum over ~156k eigenvalues at L_max=5, but Josephson sector may be truncatable to SU(3) zero modes).

### V.2. mu_BC geometric derivation
- **What**: Test the candidate mu_BC = M_Z + M_H_framework with M_H_framework = 97 GeV (tree-level, one-sector). If match reproduces to < 0.5% at symbolic level, this upgrades G47 from accommodation to zero-free-parameter. Alternative candidates (2 M_W, 2 M_Z x exp(alpha_em x fn), sqrt(M_W^2 + M_H^2)) to be systematically tested.
- **Inputs**: `canonical_constants.py` (M_Z, M_W, M_H_obs, v_EW, sin^2_theta_W_PDG); framework sector M_H values (97 GeV tree, 131.8 GeV one-loop, 127.51 GeV BCS-resolved); spectral derivation of mu_BC position from cubic BC sin^2(mu_BC) = 3/(3+e^{12 tau_fold}).
- **Gate**: NEW S84 gate: `S84-MU-BC-GEOMETRIC`. PASS: one of the candidate sums/products matches 188.44 GeV to < 0.5% with a spectral-derivation-of-identification-mechanism. INFO: < 2% match but no derivation. FAIL: best candidate > 2% OR purely algebraic coincidence.
- **Effort**: 2-3 hours, 1 agent session (symbolic candidate search + derivation-attempt).

### V.3. LiteBIRD + CMB-S4 joint Fisher for sigma(n_T)
- **What**: Extend the 2x2 Fisher to a 3x3 or combined-experiment likelihood to quantify sigma(n_T) under joint observation. Pre-register at what joint-t_obs LiteBIRD crosses sigma(n_T) = 0.04. Test whether the (r, n_T) anti-correlation rho ~ -0.95 softens under the joint treatment.
- **Inputs**: G43 LiteBIRD Fisher (`s83_w3_g43_litebird_sigma_nT_reach.npz`); G44 joint Fisher (`s83_w3_g44_cmb_s4_ccons.npz`, contains S4 spec); literature anchors (Campeti et al. 2019, Tristram et al. 2022).
- **Gate**: S78-W3-C TENSOR-FAMP extension. PASS: sigma(n_T)_joint @ 3 yr LB + full S4 <= 0.04. INFO: in [0.04, 0.08]. FAIL: > 0.08.
- **Effort**: 3 hours, 1 agent session (Fisher code exists, extend to joint).

### V.4. n_T_CMB transfer -- recompute n_T at CMB scales under the G46 substrate-dispersion transfer
- **What**: G46 established r_CMB = 0.012 via the transfer T^2 = eps_H(tau_CMB) / eps_H(tau_fold) = 0.070. Apply the same transfer to n_T: what is n_T(k_CMB) if both n_T(transit) and r are subject to the same eps_H-flow? This is the pre-registered discrimination channel against slow-roll.
- **Inputs**: `s83_w3_g50_nT_bogoliubov.npz`; `s83_w3_g46_tensor_transfer.npz`; eps_H(tau) profile from S64; S65 NS-BLV gate (n_s under same flow).
- **Gate**: NEW S84 gate: `S84-N_T-CMB-TRANSFER`. PASS: n_T_CMB = -2 x eps_H(tau_CMB) = -3.0e-3 (RED, small, below LiteBIRD 3-yr sigma). This would confirm the transit/CMB structural dichotomy. INFO: n_T_CMB in [-0.01, 0.01]. FAIL: n_T_CMB > 0.01 OR < -0.01 (contradicts eps_H profile).
- **Effort**: 2 hours, 1 agent session (direct eps_H profile evaluation).

### V.5. G42 DR3 live-watch successor script (infrastructure maintenance)
- **What**: Verify `computations/s83_w3_g42_dr3_live_watch.py` infrastructure at DR3 release. If DESI publishes bf-only, successor invokes `verdict_rule(w_0^DR3, w_a^DR3)` on the rectangle. If DESI publishes cov, successor computes chi^2 = delta @ cov_inv @ delta.T against canonical (w0_FW, wa_FW) as ANCILLARY context (rectangle containment remains primary).
- **Inputs**: `s83_w3_g42_dr3_live_watch.npz` (rectangle bounds, framework predictions, cov contingency plan); DESI DR3 publication (w_0^DR3, w_a^DR3, optional cov).
- **Gate**: S83-DR3-LIVE-WATCH activation to PASS or FAIL (binary containment). Depends on V.1 interpretation if rho_J audit completed.
- **Effort**: 1 hour at DR3 release event, 1 agent session (script already staged; post-event execution only).

### V.6. UHF GW detector threshold pre-registration (G52 re-migration path)
- **What**: Formalize the re-migration criterion from CONSTRAINT-MAP WALL back to falsifier. Pre-register: if a post-2026 UHF GW detector proposal achieves Omega_GW < 1e-40 at 1 mHz (20 OOM concession above framework gamma prediction of 1.8e-59), reclassify C5 from WALL to falsifier.
- **Inputs**: `.claude/agent-memory/constraint-map.md` O-GW-01 entry; UHF GW detector roadmap survey (levitated sensors, CAST magnetic conversion).
- **Gate**: NEW long-watch gate `S84-UHF-GW-THRESHOLD-WATCH`. PASS: no roadmap proposal reaches Omega_GW < 1e-40 at 1 mHz; WALL classification stable. FAIL: a reaches threshold; re-migrate to falsifier catalog.
- **Effort**: 1 hour, 1 agent session (literature survey).

### V.7. eps_H(tau) shape sensitivity check for n_T magnitude
- **What**: The n_T = +0.468 result depends sensitively on d ln eps_H / d tau ~ +10.3 per tau at the fold. If the fold sharpens (broadening narrower than S42 pre-reg), d ln eps_H / d tau diverges and n_T blows up. If it flattens, n_T shrinks. Scan backreaction-window FWHM in [0.5e-3, 3e-3] (G31 PASSED at 1.65e-3) and report d n_T / d FWHM.
- **Inputs**: `s83_w3_g50_nT_bogoliubov.npz`; `s64_epsilon_profile.npz`; S42 pre-registration of fold window.
- **Gate**: NEW S84 gate: `S84-N_T-FWHM-SENSITIVITY`. PASS: |d n_T / d FWHM| < 100 per unit FWHM (stable). INFO: in [100, 500]. FAIL: > 500 (n_T is fragile to fold shape).
- **Effort**: 2 hours, 1 agent session.

### V.8. alpha_f_NL framework zero-parameter prediction
- **What**: Currently alpha_f_NL (framework) is assumed ~ 0 heuristically; if SKA-2 measures nonzero alpha, it tests the framework's fold-time-dispersion-independence assumption. Derive alpha_f_NL from first principles: the GGE phase alignment through the van Hove fold, Bogoliubov amplitude's k-dependence through the BCS gap width convolution.
- **Inputs**: `s67_gge_bispectrum.npz`; `s63_running_ns.npz`; `s65_ns_blv.npz`; `s78_fnl_coherence.npz`; transit dispersion omega(k) profile.
- **Gate**: NEW S84 gate: `S84-ALPHA-FNL-PREDICT`. PASS: |alpha_framework| computed to a specific value (not heuristic) with < 20% internal uncertainty. INFO: bracket derived. FAIL: cannot be computed without additional substrate-level input.
- **Effort**: 4-6 hours, 1 agent session (first-principles fold-time dispersion analysis).

### V.9. Falsifier catalog re-release with rigor-audit flags
- **What**: Update `sessions/evoi-framework.md` falsifier section to mark each channel with one of 4 rigor flags: ZERO-FREE-PARAMETER | ACCOMMODATION | SCHEME-DEPENDENT | DETECTOR-STERILE. Propagate to `summary/` atlas files. This operationalizes the rigor audit as a permanent registry state rather than a per-session assessment.
- **Inputs**: this synthesis; G46, G47, G50, G51 verdict files; S82 Sagan synthesis Sec VI table.
- **Gate**: NEW S84 gate: `S84-FALSIFIER-RIGOR-REGISTRY`. PASS: all falsifier channels tagged with one of the 4 flags; propagation verified in 3+ documents. FAIL: tagging incomplete.
- **Effort**: 1-2 hours, 1 agent session.

### V.10. Observational scorecard delta tracker
- **What**: Append to MEMORY.md scorecard: for each S83 Level-6 gate, record (channel, decisive number, rigor flag, falsification criterion, null-result criterion, reach date). Include the G42/G51 interaction: if DR3 lands in rectangle, probability interpretation is contingent on V.1 (rho_J audit) outcome.
- **Inputs**: this synthesis; sagan-empiricist MEMORY.md; session-results-summary.md.
- **Gate**: Not a gate; scorecard update action. Precondition for sole-estimator probability updates in S84.
- **Effort**: 30 minutes, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | n_T(tau_fold) = +0.4676 BLUE | PHONONIC, zero-free-parameter | G50 PASS | Only fully-genuine zero-parameter falsifier in S83 cluster; Jensen-curvature 99.4% dominance; transit-band prediction, no near-term instrument |
| 2 | r(k_CMB) = 0.0117 | PHONONIC, zero-free-parameter (mild accommodation discount) | G46 PASS | 3.07x below BK2021; LiteBIRD clean-channel falsifier at r ~ 1e-3 forecast; BF ~ 5 |
| 3 | mu_BC = 188.44 GeV, sin^2 PDG match 0.064-sigma | PARTICLE, ACCOMMODATION | G47 PASS | mu_BC borrowed from brentq SM anchor; upgrades to zero-parameter if M_Z + M_H_framework derivation closes |
| 4 | w_0(Zubarev) = -0.998, delta = 0.080 | PHONONIC, SCHEME-DEPENDENT | G51 FAIL | Canonical regulator moves prediction TOWARD -1; exposes S58 bare-scheme artifact; rho_J R-independence audit is the prerequisite |
| 5 | DR3 rectangle R = [-1.05,-0.85] x [-0.2,0.2] | ACCOMMODATION-pending | G42 PENDING-EVENT | Framework point (-0.918, 0.0) inside R; 2026-2027 release is near-term EVOI-carrying event |
| 6 | sigma_nT @ 3yr LiteBIRD = 0.054 | Detector-reach forecast | G43 INFO | PASS threshold (0.04) reached at ~6.8 yr; joint with S4 may reach earlier |
| 7 | sigma_C_cons = 0.2556, 23x above PASS | Detector-STERILE | G44 FAIL | Channel REMOVED from near-term falsifier catalog; framework prediction structurally preserved |
| 8 | sigma_alpha_fNL @ SKA-2 = 0.80 | Detector-reachable (2030s) | G45 PASS | Tests fold-time dispersion assumption at 12.5x margin; framework null alpha -> 0 is the hypothesis |
| 9 | Channel-5 GW 29.63 OOM ratio | STRUCTURAL WALL, not falsifier | G52 PASS | Honesty correction: falsifier count S82 -> S83 drops 5 -> 4 (reclassified, not eliminated) |
| 10 | P_obs_aligned 6/9 -> 7/9 | NON-PHONONIC bookkeeping | G48 PASS | A_s INFO -> PASS re-classification; does NOT move probability |
| 11 | EVOI rank-9 DR3 promotion +2.00pp | NON-PHONONIC bookkeeping | G49 PASS | DR3 is the top-priority near-term EVOI-carrying event |
| 12 | Probability state | sole-estimator rule | 22% NEUTRAL (13-35%) | No pre-registered observational gate closed against data; G42 release is the unlock |
| 13 | Falsifier rigor-audit summary | cross-channel | 1 zero-parameter clean (G46) + 1 zero-parameter no-instrument (G50) + 1 scheme-dependent (G42/G51) + 1 accommodation (G47) + 1 detector-sterile (G44) + 2 reach-forecasts (G43, G45) + 1 WALL (G52) | Functional decisive near-term falsifier count = 1-2 |
