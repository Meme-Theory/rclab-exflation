# Session 107 Wave 4 — DESI-DR3 w(z) decision-rule (bh-cosmo-incursion forward fold) (Results Working Paper)

**Session**: 107 | **Wave**: 4 | **Plan**: session-107-plan-w4.md | **Theme**: Post-checkpoint fold of the `session-106/bh-cosmo-incursion/` v2 stream — FIRE the EXISTING pre-registered S66-era w₀/w_a falsifier rule(s) against DESI DR3 (if released); the framework's `wa_FW=0` is the no-evolution outlier vs DESI DR2's thawing preference.

## Gate Sections

### §W4-1. S107-DESI-DR3-WZ-DECISION-RULE (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S107-DESI-DR3-WZ-DECISION-RULE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the substrate-IS prediction w(z) is the emergent-cosmology image of the Volovik tracking-vacuum; DESI measures it IN the FRW container — a substrate prediction tested against lab data, NOT a methodology/hygiene gate)
**Agent**: `mack-cosmic-bridge` (sole writer of the w₀/w_a falsifier surface per `feedback_mack-bridge-role.md`; both executor and writer — no split)
**Hypothesis**: FIRE the frozen S66-era w₀/w_a decision rule(s) against DESI DR3 if released; the framework's canonical branch (`w0_FW=-0.918`, `wa_FW=0`) is the less-negative (no-evolution) outlier on w_a vs DESI's thawing (w_a<0) preference (DR2 tension 2.92σ), and if DR3 is not yet public the gate honestly closes PRE-REG-INC with the rule armed — no NEW threshold authored (Class 3).
**Plan reference**: `sessions/session-plan/session-107-plan-w4.md` §W4-1 (the four armed sub-rules L1/L2/L3/L4 + frozen SHAs, machinery pin, two-step release-status → rule-fire method, substitution chain, Input-SHA ledger, DUAL-CANONICAL note).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | On-disk | must_contain verified |
|:---------|:-----|:-------:|:----------------------|
| script | `computations/session-107/s107_desi_dr3_wz_decision_rule.py` | ✓ | `from canonical_constants import` (Section 1), `print_verdict_payload` (def + call), `PRE-REG-INC` (STEP-2a branch) — all present |
| data | `computations/session-107/s107_desi_dr3_wz_decision_rule.npz` | ✓ | Track A: `track=A_PRE-REG-INC`, `verdict=PRE-REG-INC`, release-status flags (`release_check_date`, `release_check_public_dr3=False`, `local_dr3_npz_present=False`, `dr3_available=False`), armed-thresholds snapshot (`armed_thresholds`, `R842`, `L4_reversal_band`, `S60_sigmas`), `frozen_rule_shas`, dual-SHA |
| plot | `computations/session-107/s107_desi_dr3_wz_decision_rule.png` | ✓ | (w₀,w_a) plane: R_842 rect + 7-cell {A1..C2} + S60 A/B/C scenario points + L1 survive/fail bands + FW point (−0.918, 0) + ΛCDM + DR3 point annotated "PENDING RELEASE (rule ARMED, un-fired; horizon ~2027)" |
| verdict_line | `computations/session-107/s107_gate_verdicts.txt` | ✓ | canonical line matches `^S107-DESI-DR3-WZ-DECISION-RULE:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row present; `[SIGN]` 3-tuple row present (`sign_verdict=N/A magnitude_verdict=INFO regime_verdict=VALID` — see Verdict note on the tool-enum encoding); 2 extra companion rows (armed sub-rules + DR2 substitution chain) |

**audit_sha256** = `939dda3fc7a2550ba98dfb332f39ec1d7f25de5a02966ea912c456b6936f68c3` (full 64-char; inputs: script + canonical_constants + pinmap + **frozen_rule_shas** — the S60/S84/S86 armed-threshold SHAs ENTER audit_sha256 so a re-authored threshold changes it: the Class-3 tripwire).
**content_sha256** = `a27c52eab810a18cc39fcf7f5492ee140685cd53eb533c7c5e57f12653c29ce0` (full 64-char; script bytes only).

Verification is by content presence (regex match), NEVER by line/byte count. All four artifacts present with non-stub content.

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per query-first discipline):

| Query | Salient return |
|:------|:---------------|
| `get_constant('w0_FW')` | `-0.918`, S58 four-fold-lock (Volovik vacuum partition + effacement Γ=0.99970), **Superseded=False** — the armed canonical w_0 |
| `get_constant('wa_FW')` | `0.0` (four-fold structural lock; no PROVENANCE/PDG entry — it is a substrate-IS rigidity, not a fit) — the armed canonical w_a |
| `search_knowledge('DESI DR3 w0 wa decision rule armed PRE-REG-INC blocked pending release')` | top hit `w0-primary-decision-rule` registry entry + the L4 reversibility band; the open-channel "Window-14 DESI DR3 binding-event-pending" edge (DR3 is the binding instrument for R_842 under S84-DR3-RESPONSE-PROTOCOL) — confirms the rule is pre-registered/armed, NOT to be re-authored |
| `trace_entity('w0-primary-decision-rule')` (read of `w0-primary-decision-rule.md` §5) | L4 reversal band `[-0.86,-0.83]` (S86 W13-3); audit_sha256 `8893fbc2…`, content_sha256 `51b5584d…`; A→B re-pin routes to a FOLLOW-UP session per §6 (NOT this gate; mack self-blacklisted from re-running `S86-W0-PRIMARY-VALUE-RESOLVE`) |
| read of `pre-registered-observations.md` (lines 56-64, 68-90) | L1 survive/fail edges `-0.35`/`-0.530` (line 64, S67/S68); L2 S60 σ-tree `3.91/2.06/6.33` (lines 56-60); L3 R_842 + 7-cell (lines 68-90; content_sha256 `801e4690…`, audit_sha256 `f6e102fd…`); DR3 data-release horizon 2027 (Timeline); the only nonzero-w_a mechanism (substrate compaction, w_a(apparent)=−0.645, S59) is CLOSED wrong-sign vs DESI (S66) |

**PRE-CLOSED?** No prior closure covers this gate-fire — the gate FIRES the existing armed rule against a new external datum (DR3); the canonical pins and all four frozen sub-rules already exist (confirmed un-superseded), so NO new substrate quantity is computed and NO threshold is authored (Class-3 compliant).

**Verdict**: **PRE-REG-INC** — `value='blocked_pending_DESI_DR3_release;S66_rule_armed'`, scheme=FW, convention=ABSOLUTE, L_max=N/A.

This is the **Track A canonical likely outcome** the plan pre-registered: DESI DR3 is **NOT yet public** (STEP-1 release-status check, 2026-06-13 — see Results), so the S66-era four-sub-rule decision is **ARMED but un-fired**. PRE-REG-INC is a **first-class verdict** (`gate-verdicts.md`) for a gate blocked by an unavailable external input — it is honest blocked-pending-data, **NOT a FAIL** (the math works; the decisive datum is not on the table) and **distinct from INFO** (no partial-tension reading; no measurement exists to land in any band).

**[SIGN] 3-tuple under PRE-REG-INC**: `sign_verdict=N/A magnitude_verdict=INFO regime_verdict=VALID`. The plan's literal intent is `(N/A, N/A, VALID)` — "armed, un-fired, no measurement." The `emit_verdict` tool's `magnitude_verdict` enum is `{PASS, INFO, FAIL}` and does **not** accept `N/A` (only `sign_verdict` does); `INFO` is the tool-enum encoding of "no measurement exists to fall in any pass/fail band" — an armed-un-fired placeholder, explicitly **NOT** a partial-tension reading (recorded verbatim in the companion-note so the audit trail is unambiguous). The composite top-line is PRE-REG-INC, which is **not** collapsed from the 3-tuple — the 3-tuple is companion annotation only. No composite-collapse rule was modified (Class-3 compliant).

**Results**:

NUMBERS first, gate second, interpretation third.

**STEP 1 — DR3 release-status check (check-date 2026-06-13)** — the gating input, resolved by BOTH required axes:
- **(a) Pinned local DR3-data file**: `computations/session-107/desi_dr3_w0wa_constraint.npz` — **ABSENT** on disk (the only on-disk DESI-DR3-named files are *forecast/prep* npz from S49–S71, NOT a public DR3 measurement). Local axis returns UNAVAILABLE.
- **(b) Literature/web release-confirmation check (2026-06-13)**: WebSearch + arXiv (`search_arxiv`) both confirm the latest **public** DESI cosmology release is **DR2** — arXiv:2503.14738v3 "DESI DR2 Results II" (March 2025; three years of operation; w₀>−1, w_a<0; 3.1σ DESI+CMB, 2.8–4.2σ with SNe). Papers dated through 2025-12 / 2026-03 (arXiv:2512.07104, 2507.01380v3) **reanalyze DR2**, not DR3. No public DESI DR3 w0waCDM (w₀, w_a, full covariance) constraint exists. DR3 data-release horizon is **~2027** (`pre-registered-observations.md` Timeline "2027 — DESI DR3 final"); the decision *window* opened 2026-04-23 (S84 W1b-9). Today is 2026-06-13. (These are release-status hits, NOT value-extraction citations — no DR2/DR3 w₀/w_a value is fired into any framework prediction.)
- **Result**: `dr3_available = (local_present AND public_DR3) = (False AND False) = False` → **STEP 2a**.

**STEP 2a — PRE-REG-INC (rule ARMED, un-fired)**. `value='blocked_pending_DESI_DR3_release;S66_rule_armed'`. The four sub-rules are recorded ARMED with their frozen thresholds + frozen SHAs, ready to fire on release. **All FIRED would be mechanical; NONE is authored** (authoring a new threshold / re-scaling σ / resizing R_842 / redefining the L4 band is `v3-closure-recovery.md §PROHIBITED_ACTIONS` Class 3 and FORBIDDEN; Lockouts A–F inherited):

| Sub-rule | Armed frozen threshold | Frozen provenance + SHA |
|:---------|:-----------------------|:------------------------|
| **L1** primary survive/fail | SURVIVE iff w_a^{DR3} > **−0.35**; FAIL iff w_a^{DR3} < **−0.530**; else INFO-band | `pre-registered-observations.md` line 64 (S67 DESI-VOLOVIK-67 / S68 W2-C) |
| **L2** S60 three-scenario σ-tree | FW-exclusion σ frozen: A=**3.91**σ, B=**2.06**σ, C=**6.33**σ (+ a live joint 2D Mahalanobis σ of (−0.918,0) from the DR3 central in Σ, computed only under Track B) | `pre-registered-observations.md` lines 56–60 (S60 DR3-PREREGISTER-60) |
| **L3** R_842 binary + 7-cell | R_842 = **[−0.942, −0.742] × [−0.2, +0.2]**; if outside, frozen 7-cell {A1,A2,B1,B2,B3,C1,C2} + scorecard | S84 W4-44; content_sha256 `801e4690eee8e7f4c4152be7701567229a377ab3d23a66a5a39b318469323d6f`, audit_sha256 `f6e102fd5f322dd3f6fa1e4866c6a2f0c425f344d359cf07e37e4d5877cb265e` |
| **L4** w₀-primary reversibility band | w₀^{DR3} ∈ **[−0.86, −0.83]** ⇒ PRIMARY A(−0.918)→B(−0.842454) re-pin (RECORDED only; re-emission owed to a follow-up session, NOT this gate) | S86 W13-3; audit_sha256 `8893fbc2ee44af27585268b01481eff5560817013ec3e60ae47ee0821ccaaf0a`, content_sha256 `51b5584d5d807bc3bdb1b73954f2dcf36768f50b094fc34e50b078f46ffa5f7e` |

No σ-distance was computed under Track A (no measured w_a to compare). Under **Track B** (DR3 released; STEP-2b branch present in the script but not taken this run) the script would fire: L1 set-membership of w_a^{DR3}; L2 nearest-S60-scenario + the joint 2D Mahalanobis σ d²=(x_FW−x_DR3)ᵀΣ⁻¹(x_FW−x_DR3); L3 R_842 containment + 7-cell classification; L4 reversibility test; then collapse L1/L2/L3 via the `[SIGN]` 3-tuple per the `gate-verdicts.md` composite-collapse rule (unmodified — Class 3).

**[SIGN] w_a σ-distance substitution chain** (the directional claim — the canonical wa_FW=0 is the no-evolution outlier; against the LATEST PUBLIC release, DR2):
```
Step 1 — Definitions:
  wa_FW          = 0.0       [canonical_constants.py: wa_FW = 0.0 — four-fold structural lock, S58]
  w_a^{DESI,DR2} = -0.73     [pre-registered-observations.md line 50 — DR2+DESY5 central]
  sigma_wa^{DR2} = 0.25      [same source]
  L1 edges       = {-0.35 SURVIVE, -0.530 FAIL}   [line 64, S67/S68 — FROZEN, loaded not authored]
Step 2 — Substitute:   delta_wa = wa_FW - w_a^{DR2} = 0.0 - (-0.73) = +0.730
Step 3 — Simplify:     nsig_wa^{DR2} = |delta_wa| / sigma_wa^{DR2} = 0.73 / 0.25 = 73/25 = 2.92  [Sage-exact QQ]
Step 4 — Direction:    delta_wa = +0.730 > 0  =>  wa_FW (=0) lies ABOVE (less negative than) the DESI
                       thawing central (w_a<0). DESI prefers EVOLVING (thawing) DE; the framework predicts
                       NO evolution. => the framework is the LESS-NEGATIVE / no-evolution OUTLIER on w_a.
                       The only nonzero-w_a mechanism (substrate compaction, w_a(apparent)=-0.645, S59) is
                       on the SAME negative side as DESI but is CLOSED WRONG-SIGN vs DESI (S66) — it cannot
                       be invoked to move wa_FW toward the DESI value without violating its own closed verdict.
Step 5 — Rule-fire direction: the FROZEN L1 rule fires on the MEASURED w_a^{DR3}, NOT on wa_FW. Under
                       PRE-REG-INC no w_a^{DR3} exists => sign_verdict = N/A (rule armed, un-fired).
```
The registered DR2 tension is **2.92σ** on w_a (73/25, Sage-exact). (Computed in-script: `nsig_wa^DR2 = 2.9200`.) This matches `pre-registered-observations.md` line 50 (w_a = −0.73 ± 0.25, 2.92σ) and the canonical falsifier surface `wp-B-gravastar-de-mack-v2.md §3.1` (the dark-energy-direction three-way split; the framework's wa_FW=0 is "the outlier on the evolution parameter w_a") + §5 (the SHOWS/SUGGESTS/DOES-NOT-ADDRESS table: cosmological w(z) "SUGGESTS near-ΛCDM" for Croker; DESI is the binding instrument), cited as canonical and NOT rewritten.

**Expected-output 4-tuple**: `(value='blocked_pending_DESI_DR3_release;S66_rule_armed', scheme=FW, convention=ABSOLUTE, L_max=N/A)`.

**Dual-SHA** (full 64-char, computed from the input-pin map, never truncated):
- `audit_sha256 = 939dda3fc7a2550ba98dfb332f39ec1d7f25de5a02966ea912c456b6936f68c3` — inputs [script, canonical_constants, pinmap, **frozen_rule_shas**]. The frozen S60/S84/S86 rule SHAs ENTER audit_sha256, so the rule-fire is pinned to the EXACT armed thresholds; a re-authored threshold would change audit_sha256 (the Class-3 tripwire).
- `content_sha256 = a27c52eab810a18cc39fcf7f5492ee140685cd53eb533c7c5e57f12653c29ce0` — script bytes only.

**Verdict line** appended to `computations/session-107/s107_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool (5 lines: canonical + dual-SHA companion + `[SIGN]` 3-tuple row + 2 extra companion rows; cross-process locked, sig_5 unique).

**RETIRED-GW caveat** (carried per `wp-B-gravastar-de-mack-v2.md` §6 / §3.4 / §5): the framework's GW-channel falsifiers are **retired** — walls=0 EXACT (S77/S96); the amplitude leg was **retired** at falsifier-inventory Row #7.audit-3 (S96; peak GW-detector-sterile, atlas-09 Item-49); the falsifier migrated GW→LSS (Rows #71/#72). The entire ECO/echo GW-discrimination program (the bh-cosmo-incursion corpus) is GR-side discrimination physics, NOT a live framework gate. **This gate cites NO Ω_GW amplitude as a live framework prediction** — w(z) is the live surface.

**Solution-space meaning**: the decisive DR3 falsifier is **not yet on the table**. The w(z) corridor stays open and **armed** — the canonical branch (w0_FW=−0.918, wa_FW=0) is recorded as the no-evolution outlier on w_a (2.92σ vs DR2), and the four frozen sub-rules will fire mechanically on the first public DR3 w0waCDM constraint (~2027). No corridor is closed or opened this session; no constraint-map state change beyond pinning the armed-and-blocked status.

**Carry-forward**: per the plan's Wave 4 → session-close decision point, the PRE-REG-INC outcome carries forward as a **standing live-watch** (the DR3 release-trigger), NOT a 4-field compute carry-forward — the only "input" is the external data release, which an orchestrator-direct edit cannot manufacture. The `falsifier-master-inventory.md` Row #1 (w₀) + the w_a row (mack sole-writer) record "armed; DR3 horizon ~2027." No σ-distance re-emission.

**Substrate framing**: PHONONIC, observational falsifier-surface. The substrate IS the Volovik tracking-vacuum: `w0_FW = -0.918` is the emergent-cosmology image of the substrate's a₀ Seeley-DeWitt zeroth (volume) moment after DILUTION-CC / effacement (Γ_eff=0.99970, S58/S66), NOT a quintessence field IN spacetime. Direction of explanation (`phononic-framing.md`): D_K eigenvalue spectrum → a₀ spectral moment → Volovik q-theory tracking vacuum (ρ_vac/ρ_obs=1.032) → emergent late-time EoS w(z) → DESI measures w(z) IN the FRW container. `wa_FW=0` is the four-fold structural lock (GGE integrability + Josephson phase + frozen texture + thermalization barrier; 59-OOM gap) — a substrate-IS rigidity, not a fitted constant; the substrate has NO surviving mechanism to produce nonzero w_a (substrate compaction is CLOSED wrong-sign vs DESI, S66). This gate FIRES the pre-registered S66-era rule (armed at S60/S67/S68/S84/S86) against the DR3 measurement; it computes no NEW substrate quantity. RETIRED-GW caveat (v2 §6): the framework's GW-channel falsifiers are RETIRED (walls=0 EXACT S77/S96; amplitude leg retired at falsifier-inventory Row #7.audit-3, peak GW-detector-sterile atlas-09 Item-49; falsifier migrated GW→LSS, Rows #71/#72) — this gate cites NO Ω_GW amplitude as a live prediction; w(z) is the live surface.

## Wave 4 Synthesis (team-lead)

**`S107-DESI-DR3-WZ-DECISION-RULE` → PRE-REG-INC** (Track A, the pre-registered canonical likely outcome). The STEP-1 release-status check (2026-06-13) confirmed the latest public DESI cosmology release is DR2 (arXiv:2503.14738v3); no public DR3 w0waCDM constraint exists (horizon ~2027). The frozen S66-era four-sub-rule decision (L1 survive/fail −0.35/−0.530; L2 S60 σ-tree 3.91/2.06/6.33; L3 R_842+7-cell; L4 reversibility band [−0.86,−0.83]) is **ARMED but un-fired** — no threshold authored (PROHIBITED_ACTIONS Class-3 clean; frozen rule-SHAs in audit_sha256), no Ω_GW amplitude cited (retired-GW caveat carried). The [SIGN] substitution chain established the directional content against the latest public datum: δ_wa = +0.730, registered DR2 tension nsig_wa = 73/25 = 2.92σ (Sage-exact); wa_FW=0 is the less-negative/no-evolution outlier vs DESI thawing, and the only nonzero-w_a mechanism (substrate compaction) is CLOSED wrong-sign (S66).

**Tool-schema disclosure (carried, not a defect):** the plan pre-specified the PRE-REG-INC 3-tuple as `sign=N/A, magnitude=N/A, regime=VALID`, but `emit_verdict`'s `magnitude_verdict` enum is {PASS,INFO,FAIL} and rejects N/A. The executor emitted `sign=N/A, magnitude=INFO, regime=VALID` with a verbatim companion note recording the plan-intent and that `magnitude=INFO` is the tool-enum encoding of "no measurement exists" (explicitly NOT a partial-tension reading), then re-ran so on-disk bytes match the emitted SHAs. The composite stays PRE-REG-INC (first-class, not collapsed from the 3-tuple). This is a tool-schema accommodation, not a post-data threshold change — no Class-3 boundary touched.

## Carry-Forward Computations (MATH ONLY — propagate to S108)

No carry-forwards: the DR3 decision is a **standing live-watch** (the DR3 release-trigger), NOT a 4-field compute spec — the only "input" is the external data release (~2027). Per `feedback_fix-in-session-never-defer.md` no-padding discipline, a data-availability watch is not a math carry-forward. The S66-era rule is recorded as armed-and-ready-to-fire-on-release; no substrate compute is owed.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-06-13 | DESI-DR3 w(z) falsifier (S66-era 4-sub-rule) | pre-registered, un-fired | **ARMED, blocked-pending-DR3-release (~2027)** | DR3 not public at 2026-06-13 (latest = DR2 2503.14738v3); rule recorded armed with frozen L1/L2/L3/L4 thresholds + SHAs |

## Effected In-Session (NON-MATH)

- [x] `falsifier-master-inventory.md` Row #1 (w_0) + w_a row — record "armed; S66-era 4-sub-rule; blocked-pending-DESI-DR3-release (~2027)"; NO σ-distance re-emission (no measurement). Routed to `mack-cosmic-bridge` sole-writer pass (`s107-close-mack`, item 1) — falsifier-inventory is mack's sole-writer domain.
- [x] capstone §7 DESI w(z) falsifier-anchor row — confirm armed/blocked-pending-DR3 status (no Ω_GW amplitude). Routed to mack (§7 surface, mack's domain).
- [x] DESI-DR3 live-watch recorded as a standing data-availability watch (NOT a compute CF) — captured here + in the housekeeping ledger §A.

## Files Produced

| Gate | Script | Data | Plot |
|:--|:--|:--|:--|
| S107-DESI-DR3-WZ-DECISION-RULE | s107_desi_dr3_wz_decision_rule.py | .npz | .png |

Verdict line: `computations/session-107/s107_gate_verdicts.txt` line 10 (canonical PRE-REG-INC) + lines 11–14 (dual-SHA companion, 3-tuple, armed_sub_rules, DR2_substitution_chain rows).
