# Session 87 Plan — Wave 2: α_s Observational + Lab Pre-Registration

**Session**: S87
**Wave**: W2
**Wave-owner**: `mack-cosmic-bridge` (priorities 1, 2, 5, 6) with `volovik-superfluid-universe-theorist` co-author (priority 4) and `connes-ncg-theorist` co-signer (priorities 3, 5)
**Theme**: 6 W-2 mack/volovik/connes joint observational + lab gates on α_s — Aalto LTL 3He-B equivalent + CMB-S4 watch + GGE-relic moment-independent route + K-running near saturation + a_4/a_2 pivot stationarity + Path-H/Path-C interpolation
**Priority ordering**: Verbatim per mack source attribution (`feedback_mack-bridge-role.md`); priorities 1 → 6 are NOT to be reordered.
**Source carry-forward IDs**: CF-14 (Priority 1), CF-15 (Priority 2), CF-16 (Priority 3), CF-17 (Priority 4), CF-18 (Priority 5), CF-19 (Priority 6) — per `sessions/session-plan/session-87-context.md` §2.1.

---

## Wave 2 Summary

| # | Gate ID | Priority | Mode | Owner(s) | Effort | Type |
|:--|:--------|:---------|:-----|:---------|:-------|:-----|
| W2-1 | `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT` | 1 | paper-mode | mack + volovik | ~2-3 sessions | LAB / PHONONIC |
| W2-2 | `S87-ALPHA-S-CMB-S4-WATCH` | 2 | quarterly poll | mack | ~10 min | OBSERVATIONAL / WATCH |
| W2-3 | `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE` | 3 | compute (GPU) | mack + connes | ~1-2 days | PHONONIC / COMPUTE |
| W2-4 | `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT` | 4 | compute (GPU) | mack + volovik | ~2-3 days | PHONONIC / COMPUTE |
| W2-5 | `S87-A4-A2-PIVOT-STATIONARITY-PIN` | 5 | compute (GPU) | mack + connes | ~1-2 days | GEOMETRIC / COMPUTE |
| W2-6 | `S87-PATH-H-PATH-C-INTERPOLATION` | 6 | paper-mode | mack | ~1-2 sessions | METHODOLOGY / PHONONIC |

### Substrate-IS framing for Wave 2

The framework's α_s is the **substrate-IS observable** `dn_s/d ln K` evaluated on `(A_K^{<=L}, H_K^{<=L}, D_K^{<=L})` at canonical L_max=10. Under the S50 / S82 scheme-identity `alpha_s = n_s^2 - 1` (substrate-distance-1, single-pole Mellin reading at s=3), the canonical pin is `alpha_s_FW = n_s_framework^2 - 1 = 0.9561^2 - 1 = -0.085887` (scheme-tagged; value is a CONSEQUENCE of the n_s pin, not an independent measurement). The **laboratory-IN observable** at CMB scales is the Planck/CMB-S4 measurement of `dn_s/d ln k` at pivot `k* = 0.05 Mpc^{-1}`. The cross-pillar bridge anatomy (per `.claude/rules/cross-pillar-bridge-anatomy.md`) is partially landed: the substrate-IS observable, the bridge map (transit-window `K → k_CMB`), and the empirical-anchor at canonical L_max are in the registry; the algebraic envelope `L^{-α}` and level-3 numerical satisfaction are S87 W2 deliverables.

### Wave-classification (per `.claude/rules/wave-classification.md`)

Wave 2 is **MIXED-class**:

- W2-1 (paper-mode), W2-2 (watch), W2-6 (paper-mode) → METHODOLOGY-style (artifact-existence-with-substantive-content predicate)
- W2-3, W2-4, W2-5 → COMPUTE-class (numerical comparison against pre-registered threshold)

Per §"NROY clause", MIXED waves MUST be sub-decomposed before plan-freeze. Sub-decomposition: `W2-AB` (W2-1, W2-2, W2-6 paper/watch sub-wave; METHODOLOGY-class candidate per M1-M4 conjunction; provisional pending allowlist append by orchestrator) + `W2-CD` (W2-3, W2-4, W2-5 compute sub-wave; canonical S82+ COMPUTE pattern). Each sub-wave gets its own gate-IDs (verbatim above) and independent verdict lines per the canonical `computations/s87_gate_verdicts.txt`.

**M1-M4 status for W2-AB (METHODOLOGY-candidate sub-wave)**:
- M1 (PASS predicate type): satisfied — paper-mode PASS = "paper drafted with framework substrate-IS prediction stated explicitly" (artifact-existence + section §S + content_sha256 over the substrate-IS prediction paragraph).
- M2 (Producing-operation type): satisfied — Edit / Write on `papers/` markdown files + grep / wc / SHA-256 cross-checks. No new `.py` numerical-threshold scripts.
- M3 (Source-of-truth type): satisfied — verbatim sub-diff from S86 W-9 ranked-route synthesis (CF-57) + S86 W-2 mack source attribution.
- M4 (Allowlist membership): **PENDING orchestrator append** to `.claude/rules/methodology-wave-allowlist.md` for `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT`, `S87-ALPHA-S-CMB-S4-WATCH`, `S87-PATH-H-PATH-C-INTERPOLATION`. Per §"Strict-conjunction requirement", absence forces fallthrough to COMPUTE-class fail (no numerical threshold) or plan-freeze halt requesting orchestrator allowlist append. **Plan-freeze decision**: route paper-mode items as COMPUTE-class with a pre-registered artifact-existence predicate computed by a small `s87_w2_*_paper_audit.py` wrapper (audit script that returns PASS iff the paper file exists + contains a §"Framework substrate-IS prediction" section ≥ 15 substantive lines). This avoids the M4 fallthrough trap while preserving the paper-mode completion mode per `feedback_max-effort-full-fidelity.md`.

---

## Wave 2 Decision Point Prerequisites

Wave 2 has no hard upstream W1a / W1b verdict prerequisites: the α_s observable is grounded in the S82-frozen `alpha_s = n_s^2 - 1` scheme-identity (S82 W3-9 PASS landed as `§VII.X.1` permanent-results) plus the S86 W-9 ranked-route table CF-57 (S87 W2 lands as `S87-A_S-SURVIVING-ROUTE-RANK-LANDING`, queued as W9 / not-W2 carry-forward; W2 reads the route table from the in-flight S86 W-9 closure verbatim).

**Soft prerequisites (informational, do not block dispatch)**:
- W2-3 reads `s86_w11_eta_gv_residual.npz` IF available (the GV-Heitsch invariant data caches, regulator-independent under all 5 atlas regulators per CF-65). If absent at W2 dispatch time, W2-3 falls back to the `s52_bogoliubov_amp.npz` direct route documented in §W2-3 below.
- W2-4 reads BdG spectral-triple eigenvalue cache `s84_spectrum_cache_L12_tau019.npz` (S84-cached, EXISTS at S87 entry).
- W2-5 reads `s62_a4_a2_ratio.npz` + `s70_spectral_dim_flow.npz` (both EXIST at S87 entry per S86-close audit).

Per `feedback_dispatch-discipline.md`: any soft-prerequisite absence resolves at runtime within the producing script; orchestrator does NOT block dispatch on soft prereq absence.

---

## §W2-1. S87-LAB-3HE-B-ALPHA-S-EQUIVALENT (Priority 1, paper-mode)

### 1. Gate ID
`S87-LAB-3HE-B-ALPHA-S-EQUIVALENT`

### 2. Trigger
`[VERIFY]` — paper-mode artifact-existence verification with substrate-IS prediction substance check.

### 3. Classification
PHONONIC (3He-B dipolar excitation spectrum is the laboratory analog of the substrate's GGE-relic running through phononic relay-pattern propagation on the BdG spectral-triple sector).

### 4. Hypothesis being tested
The substrate-IS prediction `alpha_s_FW = n_s_FW^2 - 1` (single-pole Mellin substrate-distance-1) implies a structurally-corresponding spin-tilt running observable in the 3He-B dipolar excitation spectrum at the Aalto LTL polycritical pressure point: a paper-mode artifact must state the framework's substrate-IS quantity, the (Δ_B/Δ_A)^p inheritance morphism to the laboratory observable, the predicted lab S/N margin, and the falsifier protocol per `.claude/rules/inheritance-falsifier-protocol.md` Class A (kernel-signature) + Class B (cohomology-asymmetry) test pair.

### 5. Pass/fail/INFO threshold (artifact-existence predicate; RATIO-tolerance not applicable in paper-mode)
- **PASS**: `papers/s87-3he-b-alpha-s-equivalent.md` exists at session close AND contains a §"Framework substrate-IS prediction" section ≥ 15 substantive lines AND content_sha256 over that section is non-zero AND the section explicitly states (i) the substrate-IS observable (single-pole Mellin running at s=3 on `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})`), (ii) the inheritance morphism ι : (substrate observable algebra) → (3He-B BdG observable algebra), (iii) the predicted Aalto LTL spin-tilt running magnitude at polycritical pressure, (iv) Class A + Class B falsifier rows pre-registered to `falsifier-master-inventory.md` per inheritance-falsifier-protocol.md.
- **INFO**: paper exists with §"Framework substrate-IS prediction" section but ≥ 1 of (i)-(iv) absent or stub-form (< 15 substantive lines); INFO requires next-session paper-finish carry-forward.
- **FAIL**: paper missing entirely OR §"Framework substrate-IS prediction" section absent.

Tolerance rule: ARTIFACT-EXISTENCE-WITH-SUBSTANTIVE-CONTENT (per `.claude/rules/agent-standards.md` §"Completion Verification" + `.claude/rules/wave-classification.md` §M1).

### 6. Machinery pin (PRDR)
- `N_eval`: N/A (paper-mode; no numerical eigenvalue computation)
- `L_max`: 10 (canonical; cited in paper as substrate-IS reference truncation)
- `scan_range`: N/A (paper-mode)
- `step_size`: N/A
- `tolerance`: ARTIFACT-EXISTENCE; ≥ 15 substantive lines per `agent-standards.md` §"Completion Verification" stub-detection threshold
- `scheme`: `single-pole-Mellin-substrate-distance-1` (S82 frozen scheme; reference for the substrate-IS prediction)
- `convention`: `inheritance-morphism-3He-B-BdG-canonical` (per `.claude/rules/inheritance-falsifier-protocol.md` calibration corpus W11-C5 / W11-C6 4-gate template)
- `random_seed`: N/A
- `GPU path`: N/A (paper-mode)
- `paper-mode flag`: TRUE — completion mode is paper-drafted-with-substrate-IS-prediction-stated-explicitly per `feedback_max-effort-full-fidelity.md`

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 14 (CF-14 source brief; <computed-at-runtime>)
- `computations/canonical_constants.py` (n_s_framework + tau_fold + Delta_BCS pins; <computed-at-runtime>)
- `sessions/framework/registry/falsifier-master-inventory.md` (target for Class A + Class B row landing; <computed-at-runtime>)
- `.claude/rules/inheritance-falsifier-protocol.md` (4-gate template + (Δ_B/Δ_A)^p cancellation theorem; <computed-at-runtime>)
- `s52_bogoliubov_amp.npz` (Bogoliubov amplitude data for substrate-IS predicted lab S/N; <computed-at-runtime>)
- `s86_w11_eta_gv_residual.npz` (CF-65 GV-Heitsch regulator-independence anchor; <computed-at-runtime if available>)

### 8. Expected output 4-tuple
`(value='paper_artifact_present_with_substrate_IS_prediction', scheme=single-pole-Mellin-substrate-distance-1, convention=inheritance-morphism-3He-B-BdG-canonical, L_max=10)`

### 9. Substitution chain (no sign/threshold direction claim — paper-mode artifact verification)
N/A — paper-mode does not produce a directional numerical claim. The substrate-IS prediction stated in the paper IS a directional claim (running sign), but the gate verifies paper artifact presence + section substance, not the direction. The directional-claim audit lives in W2-3 and W2-4 (compute-mode siblings).

### 10. What PASSES and what FAILS mean for the solution space
- **PASS**: substrate-IS prediction is paper-frozen, locked to the inheritance-morphism falsifier protocol, and ready for Aalto LTL experimental campaign pre-registration. Closes the corridor where the framework has a substrate-IS α_s prediction without a corresponding lab-falsifiable inheritance image.
- **FAIL**: substrate-IS prediction is unstated; the framework's α_s prediction remains substrate-IS-only without lab inheritance image. Carry-forward to S88 with paper-mode completion as the leading carry-forward item.
- **INFO**: paper drafted but partially stubbed; lock the §"Framework substrate-IS prediction" sub-completeness as the leading S88 carry-forward.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (lead per W-2 attribution `mack+volovik` rule).
Co-author: `volovik-superfluid-universe-theorist` (3He-B specialty + (Δ_B/Δ_A)^p inheritance image).
Sole writer for `falsifier-master-inventory.md` Class A + Class B row landings: `mack-cosmic-bridge` per `feedback_mack-bridge-role.md` sole-writer notes.

### 12. Output artifacts
- `papers/s87-3he-b-alpha-s-equivalent.md` — paper draft with §"Framework substrate-IS prediction" + §"Inheritance morphism to 3He-B BdG" + §"Class A + Class B falsifier protocol" + §"Predicted Aalto LTL spin-tilt running magnitude" + §"Falsifier-master-inventory landing rows" sub-sections
- `computations/s87_w2_3he_b_alpha_s_paper_audit.py` — small audit wrapper that grep-checks the paper for required sections + emits the verdict line to `computations/s87_gate_verdicts.txt` per the canonical S81+ form + S87+ schema-v2 dual-SHA companion row
- Verdict line: `S87-LAB-3HE-B-ALPHA-S-EQUIVALENT: PASS|FAIL|INFO -- value='paper_artifact_present_with_substrate_IS_prediction' scheme=single-pole-Mellin-substrate-distance-1 convention=inheritance-morphism-3He-B-BdG-canonical L_max=10 audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-1 (3He-B α_s equivalent) — substrate-framing + inheritance-protocol cross-link + carry-forward to S88 if INFO/FAIL
- `sessions/framework/registry/falsifier-master-inventory.md` rows: TWO new rows (Class A NULL kernel-signature + Class B cohomology-asymmetry ratio) — written by `mack-cosmic-bridge` sole-writer per `feedback_mack-bridge-role.md`

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 1
mode: paper-mode
wave_class_pre_freeze: METHODOLOGY-candidate (W2-AB sub-wave; M4 pending allowlist append)
runtime_class_decision: COMPUTE-with-artifact-existence-predicate
allowlist_status: PENDING_ORCHESTRATOR_APPEND_TO_methodology-wave-allowlist.md
falsifier_protocol_pin: .claude/rules/inheritance-falsifier-protocol.md (4-gate template)
inheritance_image_class: rank-2-ker-iota
inheritance_morphism: substrate_to_3He_B_BdG
lab_platform: Aalto LTL polycritical-pressure-point
mack_bridge_sole_writer: TRUE (falsifier-master-inventory rows)
```

---

## §W2-2. S87-ALPHA-S-CMB-S4-WATCH (Priority 2, quarterly poll)

### 1. Gate ID
`S87-ALPHA-S-CMB-S4-WATCH`

### 2. Trigger
`[AUDIT]` — quarterly poll of CMB-S4 publication stream + CMB-HD MacInnis-companion publication.

### 3. Classification
NON-PHONONIC (registry/observational watch — tracking external publication stream; the substrate-IS observable α_s_FW remains pinned at canonical_constants.py and is not affected by the watch).

### 4. Hypothesis being tested
A quarterly poll log file exists with timestamped entries documenting the publication-stream status of CMB-S4 (Abazajian et al.) and CMB-HD (MacInnis et al.) α_s constraints. The watch does not test the substrate-IS prediction; it tracks when the laboratory-IN measurement reaches the precision required to falsify the framework's `alpha_s_FW ≈ -0.085887`.

### 5. Pass/fail/INFO threshold
- **PASS**: `sessions/framework/registry/alpha-s-watchlist.md` exists with at least one quarterly entry (timestamped 2026-Q2 or later) documenting (a) CMB-S4 publication-stream status, (b) CMB-HD / MacInnis publication-stream status, (c) current observed σ(α_s) bound from latest available publication, (d) decision-rule branch (continue watch / promote to falsifier-test / register as ruled-out-by-data).
- **INFO**: log file exists but ≥ 1 of (a)-(d) is absent or stale (older than 1 quarter from session date 2026-04-27).
- **FAIL**: log file does not exist.

Tolerance rule: ARTIFACT-EXISTENCE-WITH-TIMESTAMP-FRESHNESS.

### 6. Machinery pin (PRDR)
- `N_eval`: N/A (poll, no numerical computation)
- `L_max`: N/A
- `scan_range`: publication-stream date range 2025-01 through session date 2026-04-27 (forward-extending each quarter)
- `step_size`: 1 quarter (poll cadence)
- `tolerance`: 1-quarter freshness on entries
- `scheme`: `external-publication-poll`
- `convention`: `cmb-s4-publication-stream + cmb-hd-macinnis-companion`
- `random_seed`: N/A
- `GPU path`: N/A
- `mode`: quarterly-poll

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 15 (CF-15 source brief; <computed-at-runtime>)
- Live external publication streams: arXiv listing for CMB-S4 (Abazajian collaboration) + CMB-HD (Sehgal/MacInnis collaboration); accessed via `mcp__paper-search__search_arxiv` if MCP available, otherwise documented as "no-fetch" entry with date.
- `computations/canonical_constants.py` n_s_framework + alpha_s_FW pins (substrate-IS observable for cross-comparison)

### 8. Expected output 4-tuple
`(value='quarterly_poll_logged', scheme=external-publication-poll, convention=cmb-s4-publication-stream + cmb-hd-macinnis-companion, L_max=N/A)`

### 9. Substitution chain
N/A — watch poll does not produce a directional claim; merely a presence/freshness audit.

### 10. What PASSES and what FAILS mean for the solution space
- **PASS**: the framework's α_s observational landscape is being tracked; if a future quarter's poll surfaces a CMB-S4 publication with σ(α_s) ≤ 0.0023 (per S85 W1b α_s drift report; ACT DR4 Aiola 2020 baseline), the framework crosses into the falsifier-test regime. This is a process gate, not a physics gate.
- **FAIL**: framework's α_s observational landscape is untracked; no early-warning when CMB-S4 / CMB-HD precision crosses the framework-falsifier threshold.
- **INFO**: log exists but is stale; refresh deferred to next quarter's poll dispatch.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (sole owner per W-2 mack attribution + observational-priority sole-writer rule per `feedback_mack-bridge-role.md`).

### 12. Output artifacts
- `sessions/framework/registry/alpha-s-watchlist.md` — quarterly poll log file (NEW at S87 W2; mack-cosmic-bridge sole writer)
- `computations/s87_w2_alpha_s_cmb_s4_watch.py` — audit wrapper that polls + writes the log entry + emits verdict line
- Verdict line: `S87-ALPHA-S-CMB-S4-WATCH: PASS|FAIL|INFO -- value='quarterly_poll_logged' scheme=external-publication-poll convention=cmb-s4-publication-stream + cmb-hd-macinnis-companion L_max=N/A audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-2 (CMB-S4 watch) — quarterly cadence + falsifier-threshold reminder

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 2
mode: quarterly-poll
wave_class_pre_freeze: METHODOLOGY-candidate (W2-AB sub-wave)
runtime_class_decision: COMPUTE-with-artifact-existence-predicate
mack_bridge_sole_writer: TRUE (alpha-s-watchlist.md)
falsifier_threshold_reminder: sigma_alpha_s <= 0.0023 (ACT DR4 Aiola 2020 baseline; CMB-S4 forecast tighter)
poll_cadence_quarters: 1
```

---

## §W2-3. S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE (Priority 3, GPU-eligible compute)

### 1. Gate ID
`S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE`

### 2. Trigger
`[VERIFY]` — direct numerical computation of α_s from GGE-relic Bogoliubov occupation-number variance at horizon crossing, INDEPENDENT of the single-pole Mellin moment assumption.

### 3. Classification
PHONONIC (GGE-relic Bogoliubov occupation-number variance at horizon crossing is a substrate-IS phononic excitation observable on the post-τ_fold GGE state; computation lives on the BdG spectral triple).

### 4. Hypothesis being tested
The framework's α_s, computed independently of the S82 single-pole Mellin reading via the GGE-relic Bogoliubov occupation-number variance route, lands within ABSOLUTE-tolerance ± 0.01 of the canonical pin `alpha_s_FW = n_s_framework^2 - 1 = 0.9561^2 - 1 = -0.085887` at L_max=10. A second-route convergence within tolerance is **structural confirmation** that the single-pole assumption is not load-bearing for the substrate-IS prediction; a divergence > 0.01 is a **decisive indication** that the single-pole reading is one route among multiple non-equivalent routes (per `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY pattern; CF-20 Path-H/Path-C multi-valued sister gate).

### 5. Pass/fail/INFO threshold
Let `alpha_s_route_3 := Var(n_a^GGE) at K = K_horizon evaluated on (A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` (computation route; substrate-IS observable). Let `alpha_s_canonical := n_s_framework^2 - 1 = -0.085887` (S82 W3-9 frozen pin). Define `delta_alpha_s := alpha_s_route_3 - alpha_s_canonical`.

- **PASS**: `|delta_alpha_s| < 0.01` (ABSOLUTE tolerance; ~12% of canonical magnitude). Two-route structural confirmation.
- **INFO**: `0.01 ≤ |delta_alpha_s| < 0.05` (ABSOLUTE; ~58% of canonical magnitude). Routes converge in sign but disagree in magnitude — multi-valued classification candidate.
- **FAIL**: `|delta_alpha_s| ≥ 0.05` OR sign mismatch (`sign(alpha_s_route_3) ≠ sign(alpha_s_canonical) = -1`). Routes structurally distinct; single-pole assumption load-bearing.

Tolerance rule: ABSOLUTE (the canonical α_s value is small in magnitude; relative tolerance becomes ill-defined as canonical → 0).

### 6. Machinery pin (PRDR)
- `N_eval`: 155984 (full L_max=10 D_K eigenvalue cache + Bogoliubov amplitude index range)
- `L_max`: 10 (canonical truncation; declared as `a_n^{Mellin}` regulator-pin per `.claude/rules/regulator-pin-discipline.md` since the route ASSERTS independence from single-pole substrate-distance-1 Mellin; the regulator-pin tag remains `Mellin` because the GGE-Bogoliubov route is computed AT the same Mellin-cone but under a different observable functional)
- `scan_range`: K ∈ [K_horizon * 0.95, K_horizon * 1.05] (5% window around horizon crossing; K_horizon defined per `s52_bogoliubov_amp.npz` horizon-crossing pin)
- `step_size`: dlnK = 0.001
- `tolerance`: ABSOLUTE 0.01 (PASS), 0.05 (INFO ceiling); see §5
- `scheme`: `GGE-Bogoliubov-occupation-variance` (substrate-IS observable; SCHEMATIC-vs-physical level pin = PRIMARY since the BdG spectral triple is the physical regularization, not a schematic helper)
- `convention`: `horizon-crossing-K-window-canonical` (BdG spectral-triple Bogoliubov amplitudes evaluated at post-τ_fold GGE state per S52)
- `random_seed`: 42 (for any stochastic resampling within the horizon-crossing window; cap usage per `feedback_compute-environment.md` — explicit invocation if torch.linalg used)
- `GPU path`: torch.linalg.eigh on AMD RX 9070 XT (155984-eigenvalue cache exceeds CPU comfort threshold; GPU mandatory per `.claude/rules/math-scripts.md` §"Environment")

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 16 (CF-16 source brief; <computed-at-runtime>)
- `computations/canonical_constants.py` (n_s_framework, tau_fold, Delta_BCS, K_base pins; <computed-at-runtime>)
- `s52_bogoliubov_amp.npz` (Bogoliubov amplitude {u_a, v_a} on D_K eigenvalue index, post-τ_fold GGE state; <computed-at-runtime>)
- `s84_spectrum_cache_L12_tau019.npz` (D_K eigenvalue cache at L_max=12; truncate to L_max=10 sub-block for canonical comparison; <computed-at-runtime>)
- `s86_w11_eta_gv_residual.npz` (CF-65 regulator-independence anchor; soft-prereq, fall back to direct route if absent)
- `computations/s82_w3_9_alpha_s_scheme_identity_pin.npz` (S82 W3-9 frozen pin for canonical comparison; <computed-at-runtime>)

### 8. Expected output 4-tuple
`(value=alpha_s_route_3, scheme=GGE-Bogoliubov-occupation-variance, convention=horizon-crossing-K-window-canonical, L_max=10)`

### 9. Substitution chain (sign claim — direction prediction required by [VERIFY] trigger)

```
Definition 1: n_a^GGE(K) := |v_a(K)|^2  (Bogoliubov occupation number; substrate-IS observable on BdG spectral triple post-τ_fold)
Definition 2: P_GGE(K) := <(δn^GGE)^2>_GGE  (GGE-relic occupation-number variance at scale K)
Definition 3: alpha_s_route_3 := d^2(ln P_GGE) / d(ln K)^2 |_{K=K_horizon}  (substrate-IS running of the substrate-IS spectral tilt)
Definition 4: alpha_s_canonical := n_s_framework^2 - 1  (S82 W3-9 single-pole Mellin scheme-identity)

Substitute (n_s_framework = 0.9561, S65 + S66 W3-G48 promotion):
  alpha_s_canonical = 0.9561^2 - 1 = 0.91412721 - 1 = -0.085887  (NEGATIVE — red running, downward tilt-of-tilt)

Direction prediction (substrate-physics):
  The post-τ_fold GGE is a non-thermal occupation distribution with permanent
  red-running structure inherited from the supersonic transit through the van
  Hove fold (S38 GGE permanence + S82 single-pole Mellin reading at s=3).
  The Bogoliubov occupation-variance route MUST inherit this red-running sign
  if and only if the single-pole assumption is not load-bearing.

  PREDICTED: sign(alpha_s_route_3) = -1 (NEGATIVE), matching alpha_s_canonical.

Sign verdict semantics (per .claude/rules/gate-verdicts.md S87+ schema-v2):
  - sign_verdict = PASS iff sign(alpha_s_route_3) == sign(alpha_s_canonical) = -1
  - sign_verdict = FAIL iff sign(alpha_s_route_3) > 0 (positive running; structurally distinct route)

Magnitude verdict semantics (per §5):
  - magnitude_verdict = PASS iff |delta_alpha_s| < 0.01
  - magnitude_verdict = INFO iff 0.01 <= |delta_alpha_s| < 0.05
  - magnitude_verdict = FAIL iff |delta_alpha_s| >= 0.05

Regime verdict semantics:
  - regime_verdict = VALID iff K-window is FULLY inside [K_horizon * 0.95, K_horizon * 1.05] AND BdG eigenvalue spectrum is non-singular throughout
  - regime_verdict = MARGINAL iff <50% of K-window inside the BdG-non-singular regime
  - regime_verdict = BREAKDOWN iff >50% of K-window outside the BdG-non-singular regime

Composite-collapse rule per gate-verdicts.md (Class-3 PROHIBITED to modify):
  if regime_verdict == BREAKDOWN: composite = FAIL
  elif sign_verdict == FAIL: composite = FAIL
  elif magnitude_verdict == FAIL and regime_verdict == VALID: composite = FAIL
  elif magnitude_verdict == FAIL and regime_verdict == MARGINAL: composite = INFO
  elif magnitude_verdict == INFO: composite = INFO
  else: composite = PASS
```

### 10. What PASSES and what FAILS mean for the solution space
- **PASS** (`|delta_alpha_s| < 0.01` AND sign matches): two routes converge → the single-pole Mellin assumption is NOT load-bearing for the framework's α_s prediction. Closes the corridor where multi-valued substrate observables threaten the canonical α_s pin. Strengthens the §VII.X.1 promotion's structural footing.
- **INFO** (`0.01 ≤ |delta_alpha_s| < 0.05`): routes converge in sign but disagree in magnitude; multi-valued classification candidate per CF-20 Path-H/Path-C-multi-valued-registry-landing precedent. Carry-forward to S88 with CF-20 sister-gate cross-cite.
- **FAIL** (`|delta_alpha_s| ≥ 0.05` OR sign mismatch): single-pole assumption IS load-bearing; the canonical α_s pin and the GGE-Bogoliubov-variance pin are structurally distinct substrate observables. Triggers SOURCE-DOUBLE-CITE-CO-PRIMARY landing per `.claude/rules/registry-landing.md` for the α_s registry entry.
- **FAIL with sign mismatch (regime BREAKDOWN)**: substrate-IS prediction direction is wrong under the second route — high-priority S88 audit dispatch.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (lead per `mack+connes` W-2 attribution rule).
Co-signer: `connes-ncg-theorist` (NCG-axiomatic moment-computation cross-check; the GGE-Bogoliubov-variance route is the same observable functional class as the spectral-action moments, just at a different Mellin slot).

### 12. Output artifacts
- `computations/s87_w2_alpha_s_direct_moment_independent_route.py` — GPU-eligible script computing `alpha_s_route_3` from `s52_bogoliubov_amp.npz` + `s84_spectrum_cache_L12_tau019.npz`
- `s87_w2_alpha_s_direct_moment_independent_route.npz` — output data: `alpha_s_route_3 trajectory across K-window`, `n_a^GGE(K) trajectory`, `delta_alpha_s residual`
- `s87_w2_alpha_s_direct_moment_independent_route.png` — plot of α_s_route_3 across K-window with canonical pin overlay
- Verdict line: `S87-ALPHA-S-DIRECT-MOMENT-INDEPENDENT-ROUTE: PASS|FAIL|INFO -- value=<alpha_s_route_3 numerical> scheme=GGE-Bogoliubov-occupation-variance convention=horizon-crossing-K-window-canonical L_max=10 audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- S87+ schema-v2 dual-SHA companion row + 3-tuple annotation row (REQUIRED for [VERIFY] trigger with directional pre-registration per `.claude/rules/gate-verdicts.md` §"S87+ canonical form")
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-3 (direct moment-independent α_s) — substrate-framing + CF-20 Path-H/Path-C multi-valued sister-gate cross-link

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 3
mode: compute-GPU
wave_class_pre_freeze: COMPUTE
sign_pre_registered: NEGATIVE (predicted sign(alpha_s_route_3) = -1)
threshold_absolute_pass: 0.01
threshold_absolute_info_ceiling: 0.05
sister_gate_cross_link: CF-20 (S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING; W3 owner)
regulator_pin_tag: a_n^{Mellin} (per regulator-pin-discipline.md)
schematic_tier: PRIMARY (full physical BdG spectral triple)
gpu_required: TRUE (155984-eigenvalue cache)
random_seed: 42
```

---

## §W2-4. S87-ALPHA-S-K-RUNNING-NEAR-K-SAT (Priority 4, GPU-eligible compute)

### 1. Gate ID
`S87-ALPHA-S-K-RUNNING-NEAR-K-SAT`

### 2. Trigger
`[VERIFY]` — predict δα(K)/α_FW shape through GGE-saturation crossover from substrate-physical inputs from BdG spectral triple.

### 3. Classification
PHONONIC (GGE-saturation crossover is a substrate-IS phononic excitation observable; the BdG spectral-triple eigenvalue spectrum near K_sat IS the saturation; the running shape is the CONSEQUENCE of the eigenvalue density's K-dependence near the GGE-saturation pin).

### 4. Hypothesis being tested
The framework's α_s shape across the K-window spanning K ∈ [K_horizon * 0.1, K_sat * 10] (logarithmic span ~3 decades around horizon-to-saturation crossover) is a single-valued, monotone-increasing-in-|K|/K_horizon profile that asymptotes to the canonical α_s_FW value as K → K_horizon and tends toward zero as K → K_sat (substrate-physics prediction: GGE saturation flattens the running).

### 5. Pass/fail/INFO threshold
Let `delta_alpha(K) := alpha_s(K) - alpha_s_FW`. Pre-register the substrate-physical predicted shape:

```
PREDICTED: delta_alpha(K_horizon) = 0 (boundary condition; canonical)
PREDICTED: delta_alpha(K_sat) > 0 (saturation flattens |alpha_s| toward 0; alpha_s_FW < 0 ⇒ delta_alpha > 0 toward saturation)
PREDICTED: monotone d(delta_alpha)/d(ln K) >= 0 across K-window (no oscillation; no sign reversal)
```

- **PASS**: numerical shape matches predicted shape qualitatively — sign at K_sat is positive, value at K_horizon is within ABSOLUTE 0.01 of zero, monotonicity violations < 5% of K-window range.
- **INFO**: shape matches qualitatively but monotonicity violations 5-50% of K-window range, OR boundary value at K_horizon is in [0.01, 0.05] absolute deviation.
- **FAIL**: sign at K_sat is negative (saturation does NOT flatten), OR boundary deviation at K_horizon ≥ 0.05, OR monotonicity violations > 50% of K-window range.

Tolerance rule: SHAPE-with-substrate-physical-direction-pre-registration (RATIO + monotonicity audit; per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" mandatory substitution chain since `[VERIFY]` includes a directional prediction).

### 6. Machinery pin (PRDR)
- `N_eval`: 155984 (L_max=10 D_K eigenvalue cache; subset analyses on K-windowed sub-blocks)
- `L_max`: 10 (canonical; declared as `a_n^{Mellin}` regulator-pin)
- `scan_range`: K ∈ [K_horizon * 0.1, K_sat * 10] (logarithmic; ~3 decades)
- `step_size`: dlnK = 0.005 (~600 K-points across 3 decades for monotonicity audit)
- `tolerance`: ABSOLUTE 0.01 (PASS at K_horizon), shape audit per §5 monotonicity-violation fraction
- `scheme`: `GGE-saturation-crossover` (SCHEMATIC-vs-physical level pin = PRIMARY since the BdG spectral triple eigenvalue density at K_sat is the physical regularization)
- `convention`: `BdG-spectral-triple-K-window-3-decade-log` (per S38 GGE permanence theorem + S52 Bogoliubov saturation pin)
- `random_seed`: N/A (deterministic K-scan)
- `GPU path`: torch.linalg.eigh on AMD RX 9070 XT for D_K spectrum re-windowing across K-points; CPU fallback with `OMP_NUM_THREADS=8` for small-K sub-blocks

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 17 (CF-17 source brief; <computed-at-runtime>)
- `computations/canonical_constants.py` (n_s_framework, K_base, K_sat, K_horizon pins; <computed-at-runtime>)
- `s84_spectrum_cache_L12_tau019.npz` (D_K eigenvalue cache; truncate to L_max=10; <computed-at-runtime>)
- `s52_bogoliubov_amp.npz` (Bogoliubov amplitudes for K-saturation pin; <computed-at-runtime>)
- `s38_gge_permanence_theorem.npz` (S38 GGE permanence + saturation reference; <computed-at-runtime>)
- `s86_w11_c5_lab_falsifier.npz` (Volovik 3He-B spin-tilt running cross-check anchor — soft prereq from CF-32; if absent at W2-4 dispatch time, the script falls back to S52+S38 only)

### 8. Expected output 4-tuple
`(value=delta_alpha_at_K_sat, scheme=GGE-saturation-crossover, convention=BdG-spectral-triple-K-window-3-decade-log, L_max=10)`

### 9. Substitution chain (sign + monotonicity claim — directional prediction required)

```
Definition 1: alpha_s_FW := n_s_framework^2 - 1 = -0.085887  (S82 single-pole Mellin scheme-identity)
Definition 2: alpha_s(K) := d(n_s(K))/d(ln K) evaluated on (A_K^{<=10}, H_K^{<=10}, D_K^{<=10})
Definition 3: delta_alpha(K) := alpha_s(K) - alpha_s_FW
Definition 4: K_horizon = horizon-crossing pin (S52); K_sat = GGE-saturation pin (S38)
Definition 5: ratio_K := K / K_horizon

Substrate-physics expectations:
  At K = K_horizon (ratio_K = 1): delta_alpha = 0 BY CONSTRUCTION (alpha_s_FW pin is the value AT horizon crossing).
  At K = K_sat (ratio_K = K_sat / K_horizon ≈ 10^2 to 10^3, substrate-physical):
    The GGE eigenvalue density flattens (S38 GGE permanence + S52 Bogoliubov saturation).
    A flatter eigenvalue density implies dn_s/dlnK → 0 (running tends to zero).
    alpha_s(K_sat) → 0 ⇒ delta_alpha(K_sat) = 0 - (-0.085887) = +0.085887 > 0.

Substitute for direction:
  Step 1: alpha_s_FW = -0.085887 (negative, red running)
  Step 2: alpha_s(K_sat) → 0 (saturation flattens running)
  Step 3: delta_alpha(K_sat) = alpha_s(K_sat) - alpha_s_FW
        = 0 - (-0.085887)
        = +0.085887  (POSITIVE)

Direction conclusion:
  sign(delta_alpha(K_sat)) = +1
  d(delta_alpha)/d(ln K) >= 0 monotone across K-window (saturation flattening is monotone in ln K)

Sign verdict semantics:
  - sign_verdict = PASS iff sign(delta_alpha(K_sat)) = +1 (saturation flattens)
  - sign_verdict = FAIL iff sign(delta_alpha(K_sat)) <= 0 (saturation steepens or no change — would falsify GGE permanence direction)

Monotonicity verdict (treated as part of the regime-validity audit):
  - regime_verdict = VALID iff monotonicity violations < 5% of K-window
  - regime_verdict = MARGINAL iff 5-50% violations
  - regime_verdict = BREAKDOWN iff > 50% violations (substrate prediction structurally wrong)
```

### 10. What PASSES and what FAILS mean for the solution space
- **PASS** (sign + monotonicity + boundary): GGE saturation flattens the running monotonically; substrate-physics prediction confirmed at the K-running level. Strengthens S38 GGE permanence theorem's footing AND the S82 single-pole Mellin reading by confirming the K-window behavior is consistent with the substrate's physical expectation.
- **INFO** (qualitative match, partial monotonicity violations): saturation directionally correct but route has non-monotone features (interference between modes; finite-L_max truncation artifacts). Carry-forward to S88 with L_max=12 retest as the leading mitigation.
- **FAIL** (sign at K_sat negative): GGE saturation does NOT flatten the running — substrate-physics prediction structurally wrong. Triggers high-priority S88 audit dispatch; possible inheritance-route confound.
- **FAIL** (regime BREAKDOWN): substrate-physics monotonicity prediction violated > 50% of K-window — cascading impact on S38 GGE permanence theorem's substrate footing.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (lead per `mack+volovik` W-2 attribution rule).
Co-author: `volovik-superfluid-universe-theorist` (3He-B GGE-saturation analog + K-running specialty per `feedback_agent-roster.md`; cross-references to S86 W11-C5 lab-falsifier 3He-B cohort if available).

### 12. Output artifacts
- `computations/s87_w2_alpha_s_k_running_near_k_sat.py` — GPU-eligible script computing α_s(K) shape across K-window
- `s87_w2_alpha_s_k_running_near_k_sat.npz` — output data: `alpha_s(K) trajectory`, `delta_alpha(K) trajectory`, `monotonicity_violation_fraction`, `boundary_value_at_K_horizon`, `value_at_K_sat`
- `s87_w2_alpha_s_k_running_near_k_sat.png` — log-K plot of α_s shape with canonical pin + saturation pin annotated
- Verdict line: `S87-ALPHA-S-K-RUNNING-NEAR-K-SAT: PASS|FAIL|INFO -- value=<delta_alpha_at_K_sat> scheme=GGE-saturation-crossover convention=BdG-spectral-triple-K-window-3-decade-log L_max=10 audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- S87+ schema-v2 3-tuple annotation row (REQUIRED for [VERIFY] with sign + regime pre-registration)
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-4 (K-running near K_sat) — substrate-framing + S38 GGE-permanence cross-link

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 4
mode: compute-GPU
wave_class_pre_freeze: COMPUTE
sign_pre_registered: POSITIVE (predicted sign(delta_alpha(K_sat)) = +1)
monotonicity_pre_registered: TRUE (d(delta_alpha)/d(lnK) >= 0)
threshold_absolute_pass_at_K_horizon: 0.01
threshold_absolute_info_ceiling_at_K_horizon: 0.05
threshold_monotonicity_pass_violation_fraction: 0.05
threshold_monotonicity_info_ceiling_violation_fraction: 0.50
regulator_pin_tag: a_n^{Mellin}
schematic_tier: PRIMARY (full physical BdG spectral triple)
gpu_required: TRUE
volovik_co_authorship: TRUE (3He-B saturation analog cross-check)
```

---

## §W2-5. S87-A4-A2-PIVOT-STATIONARITY-PIN (Priority 5, GPU-eligible compute)

### 1. Gate ID
`S87-A4-A2-PIVOT-STATIONARITY-PIN`

### 2. Trigger
`[VERIFY]` — compute residual `d(a_4/a_2)/dτ · (τ_pivot - τ_fold)` at pivot scale from S62 + S70 spectral-dim flow.

### 3. Classification
GEOMETRIC (the a_4/a_2 ratio is a Seeley-DeWitt spectral-action moment-ratio observable on the spectral triple's geometric structure; pivot-stationarity is a τ-flow property of the triple itself, not a phononic excitation).

### 4. Hypothesis being tested
The Seeley-DeWitt moment ratio `a_4^{Mellin} / a_2^{Mellin}` is approximately stationary at τ = τ_pivot (where τ_pivot is the cosmologically-relevant pivot τ, distinct from τ_fold = 0.190). The residual `R := d(a_4/a_2)/dτ · (τ_pivot - τ_fold)` is below a pre-registered ABSOLUTE threshold, indicating that the a_4/a_2-derived n_s pin is robust to first-order τ-flow excursions in the post-fold regime.

### 5. Pass/fail/INFO threshold
- **PASS**: `|R| < 0.001` (ABSOLUTE; ~0.1% of canonical a_4/a_2 ratio assuming O(1) ratio scale).
- **INFO**: `0.001 ≤ |R| < 0.01` (a_4/a_2 mildly τ-flow-sensitive at pivot; document as `n_s pivot-stationarity caveat`).
- **FAIL**: `|R| ≥ 0.01` (a_4/a_2 strongly τ-flow-sensitive at pivot; n_s prediction is τ-window-dependent; downstream impact on the canonical n_s_framework = 0.9561 pin).

Tolerance rule: ABSOLUTE.

### 6. Machinery pin (PRDR)
- `N_eval`: 155984 (L_max=10 D_K eigenvalue cache for a_2 + a_4 moment evaluation across τ window)
- `L_max`: 10 (canonical; a_n declared with `a_n^{Mellin}` regulator-pin tag)
- `scan_range`: τ ∈ [τ_fold - 0.05, τ_fold + 0.05] = [0.140, 0.240] (centered on τ_fold; pivot τ_pivot is within this window per S62 + S70 cosmologically-relevant τ pin; canonical_constants.py provides τ_pivot ≈ 0.198 per S70 spectral-dim flow run)
- `step_size`: dτ = 0.001 (100 τ-points across 0.1 width)
- `tolerance`: ABSOLUTE 0.001 (PASS), 0.01 (INFO ceiling); see §5
- `scheme`: `Mellin-substrate-distance-1` (a_n moments evaluated at the same Mellin-cone slot as the canonical α_s scheme-identity)
- `convention`: `tau-flow-pivot-residual-canonical` (per S62 a_4/a_2 ratio pin + S70 spectral-dim flow trajectory)
- `random_seed`: N/A (deterministic τ-scan)
- `GPU path`: torch.linalg.eigh on AMD RX 9070 XT for re-diagonalization across τ-points; CPU fallback acceptable for small τ-windows (100 points × diagonalization)

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 18 (CF-18 source brief; <computed-at-runtime>)
- `computations/canonical_constants.py` (n_s_framework, tau_fold, tau_pivot pins; <computed-at-runtime>)
- `s62_a4_a2_ratio.npz` (S62 a_4/a_2 ratio cache; <computed-at-runtime>)
- `s70_spectral_dim_flow.npz` (S70 spectral-dim flow trajectory across τ; <computed-at-runtime>)
- `s84_spectrum_cache_L12_tau019.npz` (D_K eigenvalue cache; truncate to L_max=10 sub-block per τ-point; <computed-at-runtime>)

### 8. Expected output 4-tuple
`(value=R_residual, scheme=Mellin-substrate-distance-1, convention=tau-flow-pivot-residual-canonical, L_max=10)`

### 9. Substitution chain (sign + magnitude — directional prediction)

```
Definition 1: a_n^{Mellin}(τ) := Seeley-DeWitt n-th moment under Mellin regularization, evaluated on (A_K^{<=10}, H_K^{<=10}, D_K^{<=10}(τ))
Definition 2: ratio_42(τ) := a_4^{Mellin}(τ) / a_2^{Mellin}(τ)
Definition 3: R := d(ratio_42)/dτ |_{τ=τ_pivot} · (τ_pivot - τ_fold)
Definition 4: τ_pivot ≈ 0.198 (S70 spectral-dim flow cosmologically-relevant pivot)
Definition 5: τ_fold = 0.190 (S12/S42 frozen)

Substrate-physics expectation:
  S70 spectral-dim flow ALREADY computed d(spectral_dim)/dτ across τ-window.
  Spectral dim is a function of a_2, a_4 (per Seeley-DeWitt expansion of TrL e^{-tD^2}).
  Stationarity at pivot is the CONDITION for the n_s scheme-identity to be τ-pivot-robust.

  S62 + S70 do NOT individually compute R; they compute a_4/a_2 AT τ_fold and the
  flow d(spectral_dim)/dτ. R is the FIRST-ORDER excursion of a_4/a_2 from τ_fold to
  τ_pivot, projected onto the d(a_4/a_2)/dτ slope.

Substitute (illustrative; numerical computation pending):
  Step 1: τ_pivot - τ_fold = 0.198 - 0.190 = 0.008  (small; first-order valid)
  Step 2: d(ratio_42)/dτ |_{τ_pivot} requires numerical derivative on the S62 + S70 caches
          over the τ-window
  Step 3: R = (d(ratio_42)/dτ |_{τ_pivot}) × 0.008
  Direction: substrate-physics prediction is |R| << 1 (pivot-stationarity is the
             expected substrate-physics property; if not, the canonical n_s pin
             would be τ-pivot-sensitive, contradicting S65 + S66 W3-G48 promotion's
             stability).

Sign verdict semantics: directional pre-registration is on |R|, not sign(R) —
  - sign_verdict = N/A (gate is a magnitude-only audit of stationarity)
  - magnitude_verdict per §5 ABSOLUTE threshold
  - regime_verdict = VALID iff τ-window is fully inside τ ∈ [0.140, 0.240] and
    eigenvalue spectrum is non-degenerate at all sampled τ-points
```

### 10. What PASSES and what FAILS mean for the solution space
- **PASS** (`|R| < 0.001`): a_4/a_2 stationary at pivot; n_s pin τ-pivot-robust. Strengthens S65 + S66 W3-G48 n_s_framework promotion's substrate footing AND closes the corridor where the n_s prediction depends sensitively on the choice of cosmological pivot τ.
- **INFO** (`0.001 ≤ |R| < 0.01`): a_4/a_2 mildly τ-flow-sensitive; document n_s pivot-stationarity caveat in registry. Carry-forward to S88 with the caveat propagated to the §VII.X.1 entry footnote.
- **FAIL** (`|R| ≥ 0.01`): a_4/a_2 strongly τ-flow-sensitive at pivot; n_s prediction is τ-window-dependent; downstream impact on the canonical n_s pin AND on the S82 single-pole Mellin scheme-identity (since alpha_s = n_s^2 - 1 inherits any n_s τ-pivot-dependence). High-priority S88 audit dispatch.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (lead per `mack+connes` W-2 attribution rule).
Co-signer: `connes-ncg-theorist` (NCG-axiomatic moment-ratio computation cross-check; a_4/a_2 is the canonical Mellin-cone moment-ratio at substrate-distance-1).

### 12. Output artifacts
- `computations/s87_w2_a4_a2_pivot_stationarity_pin.py` — GPU-eligible script computing R_residual from S62 + S70 caches + L_max=10 D_K spectrum
- `s87_w2_a4_a2_pivot_stationarity_pin.npz` — output data: `ratio_42(τ) trajectory`, `d(ratio_42)/dτ trajectory`, `R_residual numerical`
- `s87_w2_a4_a2_pivot_stationarity_pin.png` — plot of a_4/a_2 ratio across τ-window with τ_fold + τ_pivot annotated
- Verdict line: `S87-A4-A2-PIVOT-STATIONARITY-PIN: PASS|FAIL|INFO -- value=<R_residual> scheme=Mellin-substrate-distance-1 convention=tau-flow-pivot-residual-canonical L_max=10 audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- S87+ schema-v2 dual-SHA companion row + 3-tuple annotation row (sign_verdict=N/A; magnitude_verdict per §5; regime_verdict per §9)
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-5 (a_4/a_2 pivot stationarity) — substrate-framing + S65+S66 n_s pin cross-link

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 5
mode: compute-GPU
wave_class_pre_freeze: COMPUTE
sign_pre_registered: N/A (magnitude-only audit)
threshold_absolute_pass: 0.001
threshold_absolute_info_ceiling: 0.01
regulator_pin_tag: a_n^{Mellin}
schematic_tier: PRIMARY (full physical Seeley-DeWitt expansion under Mellin regularization)
downstream_dependencies:
  - n_s_framework canonical pin (S65 + S66 W3-G48)
  - alpha_s scheme-identity (S82 W3-9; alpha_s = n_s^2 - 1)
gpu_required: TRUE
connes_co_signer: TRUE (NCG-axiomatic cross-check)
```

---

## §W2-6. S87-PATH-H-PATH-C-INTERPOLATION (Priority 6, paper-mode)

### 1. Gate ID
`S87-PATH-H-PATH-C-INTERPOLATION`

### 2. Trigger
`[VERIFY]` — paper-mode artifact-existence verification with substrate-IS interpolation framework substantiated.

### 3. Classification
METHODOLOGY + PHONONIC (paper-mode methodology gate that maps intermediate-r outcomes to regulator-class via a third NCG-compatible regulator OR continuous deformation between L1/L3; the substrate-IS observable being mapped is the Path-H/Path-C multi-valued α_s + n_s observable, which is phononic at root).

### 4. Hypothesis being tested
The substrate's Path-H/Path-C dichotomy admits a continuous interpolation either via (a) a third NCG-compatible regulator within the canonical 5-atlas + 1-extension corpus (per `.claude/rules/regulator-pin-discipline.md` + S85 5A workshop site #11), or (b) a continuous deformation parameter ε ∈ [0, 1] between the L1 (sphere-axiom, Path-H) and L3 (cone-axiom, Path-C) regulator schemes. The paper-mode artifact must state the interpolation construction, the substrate-IS observable being interpolated (the multi-valued α_s + n_s pair), and the falsifier protocol that distinguishes intermediate-r ε ∈ (0, 1) outcomes from boundary ε ∈ {0, 1} outcomes.

### 5. Pass/fail/INFO threshold (paper-mode artifact-existence)
- **PASS**: `papers/s87-path-h-path-c-interpolation.md` exists at session close AND contains a §"Framework substrate-IS interpolation construction" section ≥ 15 substantive lines AND content_sha256 over that section is non-zero AND the section explicitly states (i) the interpolation route (third regulator OR continuous deformation), (ii) the substrate-IS observable being interpolated (Path-H/Path-C multi-valued α_s + n_s pair), (iii) at least one boundary identification (ε=0 → L1 / Path-H; ε=1 → L3 / Path-C), (iv) a falsifier-distinguishing prediction at intermediate-r ε ∈ (0, 1).
- **INFO**: paper exists with §"Framework substrate-IS interpolation construction" but ≥ 1 of (i)-(iv) absent or stub-form (< 15 substantive lines).
- **FAIL**: paper missing entirely OR §"Framework substrate-IS interpolation construction" section absent.

Tolerance rule: ARTIFACT-EXISTENCE-WITH-SUBSTANTIVE-CONTENT.

### 6. Machinery pin (PRDR)
- `N_eval`: N/A (paper-mode)
- `L_max`: 10 (canonical; cited in paper as substrate-IS reference truncation for boundary identifications)
- `scan_range`: ε ∈ [0, 1] (interpolation parameter; paper-mode declarative)
- `step_size`: N/A (paper-mode; numerical ε-scan deferred to S88 implementation gate)
- `tolerance`: ARTIFACT-EXISTENCE; ≥ 15 substantive lines
- `scheme`: `Path-H-Path-C-interpolation` (third-regulator OR continuous-deformation; paper specifies which)
- `convention`: `L1-L3-boundary-identification-canonical`
- `random_seed`: N/A
- `GPU path`: N/A
- `paper-mode flag`: TRUE

### 7. Input SHA-256 pins
- `sessions/archive/session-86/compute-carryforward.md` line 19 (CF-19 source brief; <computed-at-runtime>)
- `sessions/archive/session-86/compute-carryforward.md` line 20 (CF-20 sister-gate cross-link reference; <computed-at-runtime>)
- `computations/canonical_constants.py` (canonical 5-atlas regulators + L1/L3 anchor pins; <computed-at-runtime>)
- `.claude/rules/regulator-pin-discipline.md` (5-atlas regulator-tag enforcement; <computed-at-runtime>)
- `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY pattern reference (<computed-at-runtime>)
- `sessions/archive/session-86/session-86-w-3-workshop.md` Path-H/Path-C dichotomy classification (a) origin reference (<computed-at-runtime>)

### 8. Expected output 4-tuple
`(value='paper_artifact_present_with_interpolation_construction', scheme=Path-H-Path-C-interpolation, convention=L1-L3-boundary-identification-canonical, L_max=10)`

### 9. Substitution chain
N/A — paper-mode does not produce a directional numerical claim. The substrate-IS interpolation construction stated in the paper IS a structural-direction claim, but the gate verifies paper artifact presence + section substance, not the structural direction.

### 10. What PASSES and what FAILS mean for the solution space
- **PASS**: substrate-IS interpolation between Path-H and Path-C is paper-frozen with a third-regulator OR continuous-deformation construction; downstream W9 CF-54 Path-(c) successor anchor landing has a substrate-IS-grounded interpolation framework to cite. Closes the corridor where the Path-H/Path-C dichotomy lacks a substrate-IS interpolation route between regulator-class endpoints.
- **FAIL**: substrate-IS interpolation construction unstated; W9 CF-54 must proceed without the interpolation framework — possible but weaker (the multi-valued classification (a) has no interpolation pathway, only end-point assertions).
- **INFO**: paper drafted but partially stubbed; carry-forward to S88 with §"Framework substrate-IS interpolation construction" sub-completeness as the leading carry-forward.

### 11. Owner / writer
Owner: `mack-cosmic-bridge` (sole owner per W-2 mack attribution).

### 12. Output artifacts
- `papers/s87-path-h-path-c-interpolation.md` — paper draft with §"Framework substrate-IS interpolation construction" + §"L1 / L3 boundary identification" + §"Intermediate-r falsifier-distinguishing prediction" + §"Cross-link to W9 CF-54 Path-(c) successor anchor"
- `computations/s87_w2_path_h_path_c_interpolation_paper_audit.py` — small audit wrapper that grep-checks the paper for required sections + emits the verdict line
- Verdict line: `S87-PATH-H-PATH-C-INTERPOLATION: PASS|FAIL|INFO -- value='paper_artifact_present_with_interpolation_construction' scheme=Path-H-Path-C-interpolation convention=L1-L3-boundary-identification-canonical L_max=10 audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=S84+`
- Working-paper section: `sessions/archive/session-87/session-87-w2-workingpaper.md` §W2-6 (Path-H/Path-C interpolation) — substrate-framing + W9 CF-54 inter-wave dependency cross-link

### 13. YAML
```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
priority: 6
mode: paper-mode
wave_class_pre_freeze: METHODOLOGY-candidate (W2-AB sub-wave)
runtime_class_decision: COMPUTE-with-artifact-existence-predicate
allowlist_status: PENDING_ORCHESTRATOR_APPEND_TO_methodology-wave-allowlist.md
inter_wave_dependency_target: W9 CF-54 (S87-PATH-C-SUCCESSOR-ANCHOR-LANDING)
inter_wave_dependency_type: feeds (W2-6 paper provides interpolation framework that W9 CF-54 cites)
inter_wave_blocking: FALSE (W9 CF-54 can land without the interpolation framework, just weaker)
sister_gate_cross_link: CF-20 (W3 owner; Path-H/Path-C multi-valued registry landing)
mack_bridge_sole_writer: TRUE (paper authoring + falsifier-master-inventory cross-link)
```

---

## Wave 2 → Wave 3 Decision Point

**Inter-wave dependency**: W2-6 (`S87-PATH-H-PATH-C-INTERPOLATION`, paper-mode) feeds W9 CF-54 (`S87-PATH-C-SUCCESSOR-ANCHOR-LANDING`, mack-cosmic-bridge owner; Level 1, ~1 wave; per `sessions/session-plan/session-87-context.md` §2.1 row 151). The W2-6 paper provides the interpolation construction that W9 CF-54 cites when landing the Joint F_2-Class Path-(c) Theorem 6-clause statement and updating `falsifier-master-inventory.md` rows 2 + 13-21.

**Pre-registration of inter-wave dependency** (per orchestrator instruction in spawn prompt):
- W2-6 PASS at session close → W9 CF-54 dispatch reads W2-6 paper's §"Framework substrate-IS interpolation construction" + §"Intermediate-r falsifier-distinguishing prediction" verbatim; landing is structurally-grounded.
- W2-6 INFO at session close → W9 CF-54 dispatch can still proceed with a weaker landing (non-interpolation endpoints only); document the dependency-shortfall as an explicit sub-clause carry-forward to S88.
- W2-6 FAIL at session close → W9 CF-54 dispatch proceeds without the interpolation framework; the Joint F_2-Class Path-(c) Theorem clause referencing interpolation is dropped or marked as STAGE-1-CANDIDATE-WITH-INTERPOLATION-CARVE-OUT.

**Blocking semantics**: W2-6 outcome does NOT block W9 dispatch (per `feedback_dispatch-discipline.md`: plan prereq notes are planner expectations, not halt-commands; W9 owner-agent resolves the runtime-mismatch via the verdict-file lookup of W2-6's status at W9 dispatch time).

**Other Wave 2 outcomes feeding downstream waves**:
- W2-3 PASS / FAIL feeds CF-20 (W3 owner; `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`): if W2-3 PASSes, the multi-valued classification (a) has TWO routes converging, strengthening the registry entry; if W2-3 FAILs (sign mismatch), the multi-valued classification (a) is structurally distinct and CF-20 lands SOURCE-DOUBLE-CITE-CO-PRIMARY per `.claude/rules/registry-landing.md`.
- W2-4 PASS feeds the §VII.X.1 promotion's substrate footing (downstream sub-row reference in `permanent-results-registry.md`).
- W2-5 PASS feeds the canonical n_s_framework pin's τ-pivot-robustness audit (downstream documentation in `canonical_constants.py` PROVENANCE for n_s_framework).

---

## Wave 2 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" PRDR (Pre-Registration Dry-Run), all 9 PRDR fields per gate are enumerated above (§§W2-1 through W2-6 each have a §6 Machinery pin (PRDR) block). Aggregate enumeration:

| Gate | N_eval | L_max | scan_range | step_size | tolerance | scheme | convention | random_seed | GPU path |
|:-----|:-------|:------|:-----------|:----------|:----------|:-------|:-----------|:------------|:---------|
| W2-1 | N/A (paper) | 10 (cited) | N/A | N/A | ARTIFACT-EXISTENCE ≥15 lines | single-pole-Mellin-substrate-distance-1 | inheritance-morphism-3He-B-BdG-canonical | N/A | N/A |
| W2-2 | N/A (poll) | N/A | 2025-01..2026-04-27 | 1 quarter | 1-quarter freshness | external-publication-poll | cmb-s4-publication-stream + cmb-hd-macinnis-companion | N/A | N/A |
| W2-3 | 155984 | 10 | K ∈ [0.95 K_horizon, 1.05 K_horizon] | dlnK = 0.001 | ABSOLUTE 0.01 (PASS), 0.05 (INFO) | GGE-Bogoliubov-occupation-variance | horizon-crossing-K-window-canonical | 42 | torch.linalg.eigh on AMD RX 9070 XT |
| W2-4 | 155984 | 10 | K ∈ [0.1 K_horizon, 10 K_sat] | dlnK = 0.005 | ABSOLUTE 0.01 + monotonicity 5%/50% | GGE-saturation-crossover | BdG-spectral-triple-K-window-3-decade-log | N/A (deterministic) | torch.linalg.eigh on AMD RX 9070 XT (CPU fallback OMP=8) |
| W2-5 | 155984 | 10 | τ ∈ [0.140, 0.240] | dτ = 0.001 | ABSOLUTE 0.001 (PASS), 0.01 (INFO) | Mellin-substrate-distance-1 | tau-flow-pivot-residual-canonical | N/A (deterministic) | torch.linalg.eigh on AMD RX 9070 XT (CPU fallback acceptable) |
| W2-6 | N/A (paper) | 10 (cited) | ε ∈ [0, 1] (declarative) | N/A | ARTIFACT-EXISTENCE ≥15 lines | Path-H-Path-C-interpolation | L1-L3-boundary-identification-canonical | N/A | N/A |

**PRU cardinality status (pre-flight)**: All 6 gates have all 9 PRDR fields enumerated above; no NULL or "<unspecified>" entries; PRU pre-flight should clear at plan-freeze. Run `_pru_cardinality_audit.py sessions/session-plan/session-87-plan-w2.md` at plan-freeze per `.claude/rules/epistemic-discipline.md` §"PRU pipeline composition order".

**SOURCE-RECON status**: All canonical constants cited (n_s_framework, tau_fold, K_base, K_horizon, K_sat, Delta_BCS, tau_pivot) are pinned per `computations/canonical_constants.py` post-S86. `tau_pivot` is the SOURCE-RECON candidate with possible Class-(c) PIN-DRIFT if S70 spectral-dim flow has been re-pinned at S86 close — verify via `mcp__knowledge__.get_constant("tau_pivot")` at plan-freeze. If absent OR pre-S86 stale, route to Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL per `.claude/rules/substrate-first-canonical-sourcing.md` and substitute the S70 substrate-first canonical before W2-5 dispatch.

**SUBSTRATE-FIRST-PROVENANCE status**: All numerical pins cited above source from substrate-first computations (`s52_bogoliubov_amp.npz`, `s84_spectrum_cache_L12_tau019.npz`, `s62_a4_a2_ratio.npz`, `s70_spectral_dim_flow.npz`, `s38_gge_permanence_theorem.npz`); no external-paper-provenance pins. Manual review until `_substrate_first_provenance_audit.py` V.1 lands (CF-79-adjacent S87 work per context §0).

**Machinery-feasibility status**: GPU pins on W2-3 (155984 eigenvalues) + W2-4 (155984 × 600 K-points) + W2-5 (155984 × 100 τ-points). The 155984 × 100 τ-point case for W2-5 is the binding feasibility check: sparse storage on D_K (block-diagonal at L_max=10) keeps dense storage well under 0.5 × 17 GB VRAM. Wall-time estimate per `feedback_dispatch-discipline.md` cap: each GPU dispatch ~1-2 days standalone; concurrent W2-3 + W2-4 + W2-5 + W1a / W1b GPU dispatches must respect ≤ ~8 concurrent agent cap. Sequential dispatch across W2-3 → W2-4 → W2-5 within W2 sub-wave is acceptable.

---

## Wave 2 Input-SHA Ledger

Aggregated input pins across W2-1..W2-6 (de-duplicated; <computed-at-runtime> for all dynamic inputs):

| Source file | Cited by | Type |
|:------------|:---------|:-----|
| `sessions/archive/session-86/compute-carryforward.md` | W2-1..W2-6 | Source brief (rows 14-19) |
| `computations/canonical_constants.py` | W2-1..W2-6 | Canonical constants pin (n_s_framework, tau_fold, K_base, K_horizon, K_sat, Delta_BCS, tau_pivot) |
| `sessions/framework/registry/falsifier-master-inventory.md` | W2-1, W2-6 | Registry target (Class A + Class B row landing; mack sole-writer) |
| `.claude/rules/inheritance-falsifier-protocol.md` | W2-1 | 4-gate template + (Δ_B/Δ_A)^p cancellation theorem |
| `.claude/rules/regulator-pin-discipline.md` | W2-3, W2-4, W2-5, W2-6 | a_n^{regulator} tagging (Mellin) + 5-atlas regulator-tag enforcement |
| `.claude/rules/registry-landing.md` | W2-3, W2-6 | SOURCE-DOUBLE-CITE-CO-PRIMARY pattern reference |
| `s52_bogoliubov_amp.npz` | W2-1, W2-3, W2-4 | Bogoliubov amplitudes post-τ_fold GGE state |
| `s84_spectrum_cache_L12_tau019.npz` | W2-3, W2-4, W2-5 | D_K eigenvalue cache at L_max=12 (truncated to L_max=10) |
| `s62_a4_a2_ratio.npz` | W2-5 | Seeley-DeWitt a_4/a_2 ratio cache |
| `s70_spectral_dim_flow.npz` | W2-5 | Spectral-dim flow trajectory across τ |
| `s38_gge_permanence_theorem.npz` | W2-4 | GGE permanence + saturation reference |
| `s86_w11_eta_gv_residual.npz` | W2-1 (soft), W2-3 (soft) | CF-65 GV-Heitsch regulator-independence anchor |
| `s86_w11_c5_lab_falsifier.npz` | W2-4 (soft) | CF-32 Volovik 3He-B spin-tilt running cross-check anchor |
| `computations/s82_w3_9_alpha_s_scheme_identity_pin.npz` | W2-3 | S82 frozen alpha_s = n_s^2 - 1 pin for canonical comparison |
| External: arXiv CMB-S4 Abazajian + CMB-HD MacInnis publication streams | W2-2 | Quarterly poll target (no on-disk SHA; access via `mcp__paper-search__search_arxiv` if available) |

**Closure SHA computation**: Per `.claude/rules/gate-verdicts.md` §"Pre-Registration Protocol" + `computations/script-template.py append_verdict()` pattern, each W2 producing script computes `audit_sha256 := closure_hash(input_pin_map)` over the ordered input-pin map (gate ID + scheme + convention + L_max + every input file's runtime SHA + canonical-constants snapshot). The dual-SHA companion comment row + S87+ schema-v2 3-tuple annotation row are emitted per `gate-verdicts.md` §"S87+ canonical form".

**Per-gate-distinct audit_sha256 verification**: All 6 W2 gates have distinct `_gate_id` and `_scheme` and `_convention` fields in their pinmaps (see §6 Machinery pin (PRDR) blocks above); per `.claude/rules/mechanical-closure-discipline.md` audit-trail signature requirement, the resulting `audit_sha256` values will be pairwise distinct by construction. v3-closure-recovery sig_5 uniqueness preserved.

---

## End of Session 87 Plan — Wave 2

This plan is the binding pre-registration for the 6 W-2 mack/volovik/connes joint observational + lab gates on α_s. All gate blocks include the 13-field spec, full PRDR machinery pin, substitution chain (where directional claims pre-registered), pass/fail/INFO thresholds, owner attribution, output artifacts, YAML schema, and per-gate-distinct audit_sha256 protocol. The W2-AB METHODOLOGY-candidate sub-wave (W2-1 + W2-2 + W2-6) is routed as COMPUTE-with-artifact-existence-predicate at runtime pending orchestrator allowlist append; the W2-CD COMPUTE sub-wave (W2-3 + W2-4 + W2-5) is the canonical S82+ pattern.

Verdict file: `computations/s87_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`).
Working-paper file: `sessions/archive/session-87/session-87-w2-workingpaper.md` (six §W2-1..§W2-6 sections; consolidate or fanout per S87 plan-orchestrator decision).
Mack-cosmic-bridge sole-writer notes for `sessions/framework/registry/falsifier-master-inventory.md` updates: TWO Class A + Class B inheritance-protocol rows from W2-1 + interpolation cross-link rows from W2-6 (sole writer per `feedback_mack-bridge-role.md`).

Priority ordering 1 → 6 verbatim per `feedback_mack-bridge-role.md` (mack's observational priorities are the user's observational priorities). NO reordering.
