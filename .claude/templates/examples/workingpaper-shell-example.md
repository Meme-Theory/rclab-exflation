<!-- CANONICAL SHELL EXAMPLE — DO NOT MODIFY — NOT A SESSION ARTIFACT

This file is a frozen snapshot of a correct working-paper dispatch shell. It is
referenced by:
- `.claude/templates/workingpaper.md` (the mechanical template)
- `.claude/skills/rclab-plan/skill.md` Phase 5c (the prompter prompt)

Purpose: shows the correct shape at dispatch time — 7-line context header +
2 compact pending blocks per gate — before any runtime agent has filled it in.

Do NOT treat this as a session artifact. Do NOT edit to reflect filled content.
If the shell shape changes in the future, update this file + both pointers.

Origin: `sessions/archive/session-85/session-85-w1a-workingpaper.md` as written at
S85 Wave 1 retask, 2026-04-23, before runtime dispatch. Frozen here so the
live session file can be filled without invalidating the canonical reference.

Retrofit 2026-04-25: added `**MCP Pre-Compute Audit**` pending block to every
gate to match `.claude/templates/workingpaper.md` line 27-28 (Rule 3, the
mandatory MCP-query block per `.claude/rules/knowledge-index-usage.md`). The
original 2026-04-23 freeze pre-dated that template provision; this retrofit
makes example + template + rule consistent. No other content changed.
-->

# Session 85 Wave W1a — mack-origin reviewer wave (split 1/2) (Results Working Paper)

**Session**: 85 | **Wave**: W1a | **Plan**: session-85-plan-w1a.md | **Theme**: mack-origin single-reviewer carry-forwards — observational pre-registration, detector forecasts, regulator-conditional live-watches, registry landings.

## Gate Sections

### §W1a-1. S85-W1a-SCHEME-DEP (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-SCHEME-DEP`
**Trigger**: `[VERIFY]`
**Classification**: **META** (scheme-invariance audit of f_conv)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: 2-loop Z_R correction either closes the S84 f_conv scheme-variance floor (4.65% → ≤1%) or permanently books the variance into §VII.M.2.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-1 (machinery pin, thresholds, substitution chain source).

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: Z_R_2loop_variance value, 4-tuple (scheme=MS-bar, convention=CONVENTION-I, L_max=10), CC1 perturbative-convergence, CC2 heat-kernel residue at s=3, substitution chain with substituted numbers, dual-SHA, artifacts `s85_w1a_scheme_dep.py/.npz/.png`)*

---

### §W1a-2. S85-W1a-ALPHA-S-REGISTRY-UPGRADE (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-ALPHA-S-REGISTRY-UPGRADE`
**Trigger**: `[AUDIT]`
**Classification**: **META** (permanent-results-registry maintenance under partition-invariance criterion)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: α_s registry row promotable to partition-invariant iff α_s = n_s²−1 holds across ≥2 independent partition schemes with residual ≤1%.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-2.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: partition-scheme residuals (topological vs spectral), 4-tuple, CCs, registry patch, knowledge-MCP cross-check against `get_constant('alpha_s_MZ_obs')` + `trace_entity('alpha_s')`, dual-SHA, artifacts)*

---

### §W1a-3. S85-W1a-ALT-D-SPEC-PROBE (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-ALT-D-SPEC-PROBE`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (alternative pathway to d_spec = 12 at fiber-transition scale)
**Agent**: `mack-cosmic-bridge` (optional consult: connes-ncg-theorist)
**Hypothesis**: d_spec = 12 derivable from three convergent routes — Seeley-DeWitt a_{12/2}, zeta residue at interior-s* critical strip, SU(3) Casimir ratio — all within ±0.1.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-3.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: three-route d_spec values, convergence spread, 4-tuple, CCs, substitution chain, dual-SHA, artifacts)*

---

### §W1a-4. S85-W1a-BK-ARRAY-2026-LIVEWATCH (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-BK-ARRAY-2026-LIVEWATCH`
**Trigger**: `[AUDIT]` (event-driven; CF-M9)
**Classification**: **META** (pre-registration + live-watch protocol)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: r = 0.01173 prediction (S84 W4-42) tested by BICEP Array + Keck 2026 release; four-branch decision tree already registered at SHA `e2ca24d6…882d3` covers outcome space.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-4.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: event-watch registration artifact, branch-tree SHA echo-check, 4-tuple, dual-SHA, no compute until trigger fires)*

---

### §W1a-5. S85-W1a-DR3-LIVEWATCH (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-DR3-LIVEWATCH`
**Trigger**: `[AUDIT]` (event-driven, 2026-04-23 DR3 window open; CF-M1)
**Classification**: **META** (binary R_842 containment check)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: S84-W1b-9 DR3 response protocol (R_842 = [−0.942, −0.742] × [−0.2, 0.2] at `content_sha=9cc7f47e…79d9f`) resolves to (i) R_842-contained → w_0 ratified, or (ii) R_842-excluded → cascade S85-R_842-PHYSICAL-ANCHOR-REAUDIT + S85-W0-L-INVERTED-BRANCH-ENUMERATION.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-5.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: DR3 central (w_0, w_a) values, binary containment verdict, cascade-trigger state, 4-tuple, dual-SHA)*

---

### §W1a-6. S85-W1a-LISA-CGWB-FLAGSHIP-FIX-K (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-LISA-CGWB-FLAGSHIP-FIX-K`
**Trigger**: `[VERIFY]`
**Classification**: **META** (pre-registration fix-k vs fix-f disambiguation; CF-M4)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: S84 W6-50 CGWB-ABSOLUTE-PT prediction (h_c^(A) 11 OOM above LISA noise floor) requires both fix-k and fix-f formulations documented with deterministic map — ρ_AC(fix-f) = 2.38 vs ρ_AC(fix-k) = 2.10.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-6.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: ρ_AC values both conventions, deterministic-map verification, 4-tuple, CCs, dual-SHA, artifacts)*

---

### §W1a-7. S85-W1a-LISA-FLAGSHIP-FIX-TIGHTENING (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-LISA-FLAGSHIP-FIX-TIGHTENING`
**Trigger**: `[VERIFY]`
**Classification**: **META** (tightens pre-registration boundaries; W6 D.2)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: LISA falsification window tightens from [h_c/10, 10·h_c] to [h_c/3, 3·h_c] using W1a-6 fix-k/fix-f consistency as internal error budget — LISA becomes DECISIVE rather than merely consistent.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-7.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: tightened-window edges, error-budget derivation, 4-tuple, CCs with W1a-6 anchor, dual-SHA, artifacts)*

---

### §W1a-8. S85-W1a-LITEBIRD-NT-REGISTRY-LANDING (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-LITEBIRD-NT-REGISTRY-LANDING`
**Trigger**: `[AUDIT]`
**Classification**: **META** (registry landing; CF-M5)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: S84 W4-41 result (LiteBIRD n_T 540–654× below 1-sigma; EVOI=0 for 2030–2040) lands in permanent-results-registry as STRUCTURAL-FLOOR — 54-decade separation is geometric, not statistical.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-8.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: registry patch, STRUCTURAL-FLOOR classification justification, SHA pinning to S84 W4-41, no-renumbering CC, dual-SHA, artifacts)*

---

### §W1a-9. S85-W1a-MULTID-FISHER-FRAMEWORK (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-MULTID-FISHER-FRAMEWORK`
**Trigger**: `[VERIFY]`
**Classification**: **META** (multi-channel Fisher-information framework; W6 D.3)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: 7D discriminant surface (w_0, w_a, n_T, r, β_s, α_s, f_NL) collapses to N-channel Fisher framework returning joint BF_FW/LCDM with explicit correlation matrix (CMB-S4 + DESI DR3 + LiteBIRD + LISA + 21cm).
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-9.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: 7D Fisher matrix, correlation matrix, BF_FW/LCDM joint value, 4-tuple, CCs, substitution chain, dual-SHA, artifacts)*

---

### §W1a-10. S85-W1a-FALSIFIER-MONITOR-RANK-UNIVERSALITY (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S85-W1a-FALSIFIER-MONITOR-RANK-UNIVERSALITY`
**Trigger**: `[AUDIT]`
**Classification**: **META** (falsifier-watchlist monitoring; R_N scan via R3 YAML template)
**Agent**: `mack-cosmic-bridge` (coordinates with van-den-dungen-bridge, tesla-resonance)
**Hypothesis**: Alternative fiber groups (G_2, F_4, A_3, C_3 from S84 W13) with R_N deviating >10% from SU(3) baseline trigger a counterexample registration against S84 W10-111 rank-universality claim.
**Plan reference**: `sessions/session-plan/session-85-plan-w1a.md` §W1a-10.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: per-group R_N scan values, deviation %, counterexample trigger verdicts, 4-tuple, dual-SHA, artifacts)*

---

## Wave W1a Synthesis (team-lead)

(Written after all 10 gates complete. Structure: `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`.)

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)
