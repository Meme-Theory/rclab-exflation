# Session 86 Synthesis (Slot 1a, Entry S-6): INVENTORY-AS-CANONICAL-SOURCE Architectural Review

**Date**: 2026-04-27
**Agent**: gen-physicist (cross-domain workhorse)
**Slot/Entry**: S86 1a / S-6 (W14 Candidate-4 architectural review; r_PathH primary anchoring + canonical_constants registry sync)
**Source Documents**:
- `sessions/archive/session-86/session-86-w12-workingpaper.md`
- `sessions/archive/session-86/session-86-w14-workingpaper.md`
- `computations/canonical_constants.py`
- `sessions/framework/registry/falsifier-master-inventory.md`
- `.claude/rules/agent-standards.md`
- `.claude/rules/math-scripts.md`
- `.claude/rules/gate-verdicts.md`
- `.claude/rules/epistemic-discipline.md`
- `.claude/skills/weave/SKILL.md`
- `.claude/agent-memory/gen-physicist/MEMORY.md`

---

## I. Session Outcome

A registry-layer constraint surface has surfaced and was correctly mapped by the W14 wave: across W14-1 → W14-6, five consecutive META gates returned `Constant 'X_FW' not found` for the framework's headline observable family — `w0_FW` (no PROVENANCE entry), `alpha_s_FW` (not found), `Omega_GW_LISA` (not found), `f_NL_FW` (not found, with sub-pathway ambiguity), `A_s_FW` (not found, with ε_pivot ambiguity), plus `M_KK` (value present but no PROVENANCE entry). All five values DO exist in `sessions/framework/registry/falsifier-master-inventory.md` (P11 + W14-2..W14-6 audit-pin sub-rows). The architectural finding from the cross-domain review: the inventory has become the **de-facto canonical source** for the framework's headline observable set, while `computations/canonical_constants.py` (which all S34+ computation scripts import via `from canonical_constants import *`) has not been kept in sync. This is not a physics defect; it is a write-order-discipline gap and a missing `/weave --update` audit hook. The W14-6 in-session promotion of seven `dE_a` lab-falsifier constants WITH PROVENANCE entries is the correct in-session fix-now precedent (per `feedback_fix-in-session-never-defer.md`); the residual five families are queued under `S87-CANONICAL-CONSTANTS-W14-RESIDUAL`.

---

## II. Key Results

### II.1 Source-of-truth direction: which artifact held the up-to-date value when the gate fired?

**Result**: `falsifier-master-inventory.md` was the LIVE-UPDATED source for all five families at gate-fire time; `canonical_constants.py` was the STALE source. Evidence chain (substitution-style, walking the W14 §lines):

1. **`w0_FW = -0.918`** (W14-1, §line 23 of W14 WP):
   - `canonical_constants.py:1243` → `w0_FW = -0.918  # Framework w_0 from Volovik vacuum + effacement (S58)` — value present, BUT `PROVENANCE["w0_FW"]` does NOT exist (verified by grep against the PROVENANCE dict block at line 685+).
   - `falsifier-master-inventory.md` Row #1 (post-P11): carries the L=8/L=10/L=12 sub-pin table with branch-(iv) audit-pin SHA reference.
   - Direction: the inventory carries L_max-resolved (L=8: `0.0204`; L=10: `-0.918`; L=12 lower: `-0.998`; L=12 upper: `-0.842454`) AND the substrate-vs-Volovik-partition adjudication; `canonical_constants.py` carries only the single L=10 Volovik-partition canonical with no provenance.
   - **Inventory is the canonical source for the structured form; canonical_constants is a stale single-value snapshot.**

2. **`alpha_s_FW = -0.068968`** (W14-2, §line 119 of W14 WP):
   - `canonical_constants.py:1277` → `alpha_s_inflation_framework = n_s_canon**2 - 1` (computed = -0.068968 at `n_s_canon = 0.9649`).
   - The MCP `get_constant("alpha_s_FW")` returned `Constant 'alpha_s_FW' not found` because the canonical handle is `alpha_s_inflation_framework` (and its alias `alpha_s_framework_central`), NOT `alpha_s_FW`.
   - `falsifier-master-inventory.md` Row #3 + sub-row 3.audit: cite `alpha_s_inflation_framework = -0.068968 (n_s^2 - 1 identity, S50-51)` plus the W13-2 joint-Fisher full-64-hex audit pin.
   - **The inventory is consistent; the canonical_constants module names the same value under a different handle. This is a NAMING-MISMATCH inversion, not a value-drift inversion.** The fix is either (a) add `alpha_s_FW = alpha_s_inflation_framework` alias OR (b) standardize the inventory on the canonical handle.

3. **`Omega_GW_LISA = 8.299e-58`** (W14-3, §line 217 of W14 WP):
   - `canonical_constants.py`: NO entry. The value `8.299e-58` exists ONLY in (i) the W13-2 verdict line at `computations/s85_gate_verdicts.txt:201`, (ii) the `s85_w13_2_cgwb_alpha_s_joint.py` interpolator output, (iii) `falsifier-master-inventory.md` Row #7 + sub-row 7.audit.
   - **The inventory is the only documentation registry that carries this value; the canonical-constants module has no entry at all (neither value nor PROVENANCE).** Direction: inventory IS canonical here; canonical_constants is empty.

4. **`f_NL_FW`** (W14-4, §line 347 of W14 WP):
   - `canonical_constants.py`: ONE entry `FW_F_NL_FOLDED = 0.0547` (local, in `s85_w4_null_elim_map.py`) — Pathway A only, not in the central canonical_constants module's importable namespace.
   - `falsifier-master-inventory.md` Row #9 + sub-row 9.audit: carries all THREE pathway values (S82-equilateral 0.0547, S67-folded 0.129, S85-W9-3 0.7685) with full-64-hex per-pathway audit pins.
   - **The inventory carries the structured 3-pathway form; canonical_constants has at most one of three values, not in canonical scope.**

5. **`A_s_FW`** (W14-5, §line 475 of W14 WP):
   - `canonical_constants.py`: `A_s_CMB = 2.1e-9` (line 82, Planck 2018 OBSERVED), `A_s_Planck = A_s_CMB` (alias). NO framework-prediction entry.
   - `falsifier-master-inventory.md` Row #12 + sub-row 12.audit: carries the band `A_s_FW(eps=0.02163) = 3.11e-9` and `A_s_FW(eps=0.020) = 4.27e-9`, plus the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 binding to band-not-point reporting until W5a P3 closes ε_pivot.
   - **The inventory carries the band-not-point reporting contract; canonical_constants carries only the OBSERVED Planck value.** Inventory is the canonical source for the prediction; canonical_constants is the canonical source for the comparand.

**Cross-domain pattern (substitution chain, source-of-truth direction)**:

- *Definition*: "Canonical source for value X" = the artifact whose value (a) is derivation-frozen, (b) carries traceable provenance, (c) is queryable by downstream consumers via a stable interface.
- *Substitution* for the five families: (a) is satisfied by the inventory rows (P11 + audit-pin sub-rows landed by W13/W14 with content_sha256 + audit_sha256 closures); (b) is satisfied by both artifacts in principle, but in PRACTICE only the inventory carries the cross-references (P10/P11/PAIR-N/audit-pin sub-rows + W13-2 SHA pinning); (c) is the failing predicate — the inventory IS NOT directly importable by computation scripts, but `canonical_constants.py` IS (`from canonical_constants import *`).
- *Simplification*: the inventory is the WRITE-canonical (where new framework predictions land first, with full audit trail); `canonical_constants.py` is the IMPORT-canonical (what computation scripts actually consume). The two diverge when a new prediction lands in the inventory and is not promoted into the import-canonical module.
- *Direction*: the inventory is structurally the source of truth for derivation provenance; `canonical_constants.py` is structurally the source of truth for computation-script consumption. **Both are canonical, but for different consumers.** The architectural failure is not "wrong source of truth" — it is "no enforced sync between the two canonical layers".

**Classification**: META (registry-layer architecture, not a physics observable).

### II.2 Canonical write-order proposal: verdict → canonical_constants → inventory

**Result**: The structurally correct write-order for new framework predictions is **(1) verdict file → (2) canonical_constants.py → (3) falsifier-master-inventory.md**, NOT (1) → (3) → (2).

**Substitution chain (forward-rationale, applied to a hypothetical new prediction P)**:

1. *Definition*: "verdict file" = `computations/s{N}_gate_verdicts.txt` — the one-line append-only log of pre-registered gate outcomes per `.claude/rules/gate-verdicts.md`. "canonical_constants" = `computations/canonical_constants.py` — the import-source for computation scripts. "inventory" = `sessions/framework/registry/falsifier-master-inventory.md` — the registry of falsifiable observables with detector horizons.
2. *Substitution* (write-order (1)→(2)→(3)):
   - Step 1: producing script appends `S{N}-NEW-P-GATE: PASS -- value=<P_value> ... sha256=<closure>` to the verdict file. This emits the value in dual-SHA pinned form. Provenance (script SHA + canonical_constants SHA at write-time + input-pin map SHA) is now permanent.
   - Step 2: orchestrator (or producing-script's post-write hook) calls `update_constant("P", P_value, session="S{N}", source="S{N}-NEW-P-GATE", comment="...")` against `canonical_constants.py`, which adds a PROVENANCE entry citing the verdict-line SHA from Step 1. computation scripts can now import `P` from canonical_constants and pin it with provenance.
   - Step 3: mack-cosmic-bridge (sole writer per `feedback_mack-bridge-role.md`) appends a new row (or audit-pin sub-row) to the inventory, citing both the verdict-line SHA AND the canonical_constants entry. The inventory now carries the falsifier-side annotation (live-watch envelope, internal-consistency split, detector horizon) anchored to two upstream pins.
3. *Substitution* (write-order (1)→(3)→(2), the OBSERVED W14 pattern):
   - Step 1: identical to above.
   - Step 2': mack-cosmic-bridge appends a new row to the inventory. The row's audit-pin cites only the verdict-line SHA — no canonical_constants entry exists yet, so no second pin is available.
   - Step 3': eventually (next session, perhaps), an orchestrator notices the gap and dispatches a canonical-constants promotion gate. Between Steps 2' and 3', computation scripts that need `P` either (a) hardcode the value (violating `.claude/rules/math-scripts.md` "never hardcode framework constants") or (b) import a related constant and skip P entirely.
4. *Simplification*: under (1)→(2)→(3), computation scripts can begin consuming `P` from canonical_constants immediately after Step 2; the inventory citation (Step 3) adds falsifier-side annotation but is not a prerequisite for computation consumption. Under (1)→(3)→(2), computation scripts CANNOT consume `P` until Step 3' completes — which may be one or more sessions later, creating a window where the value is "canonical in inventory but invisible to computation import". This is exactly the W14-1..W14-5 condition the gates surfaced.
5. *Direction*: the (1)→(2)→(3) order is structurally cleaner because it preserves the dependency chain (verdict pins canonical_constants pins inventory), whereas (1)→(3)→(2) inverts it (verdict pins inventory; canonical_constants becomes a downstream consumer of the inventory's row identity). **Forward-canonical write-order is (1)→(2)→(3).**

**Caveat (one-shot vs streaming)**: when a single gate produces a STRUCTURED value (band, pathway-keyed, pivot-keyed) that the inventory captures with annotation but canonical_constants would have to flatten to multiple constants, the practical write-order is (1) → (2 with sub-keyed entries) → (3). W14-4's f_NL example: the inventory carries one row with three pathway columns; canonical_constants needs three sub-keyed entries `f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template` (per the W14-4 §lines 438-440 carry-forward spec). This is NOT a deviation from (1)→(2)→(3); it is the sub-keying expansion at Step 2.

**Classification**: META (write-order discipline; rule-file proposal lands as code-block in §VII).

### II.3 Hooks fired by `/weave --update` to enforce sync

**Result**: NO hook currently enforces inventory ↔ canonical_constants sync. The five existing `/weave --update` phases (per `.claude/skills/weave/SKILL.md` §`--update`, lines 60-80) do not include an inventory-vs-canonical-constants diff check.

The SKILL.md `--update` chain explicitly documents:
- Phase 1: `harvest_archive_edges.py` + `harvest_provenance_edges.py` — harvests fresh edges from filesystem sources.
- Phase 2: `extract_entities.py` — rebuilds `tools/knowledge-index.json` from sessions, computation, and harvested edges.
- Phase 3: `knowledge_db.py --sync` — syncs JSON into SQLite (`tools/knowledge.db`).
- Phase 4: `viz/console/build_data.py` — rebuilds the console's bundled `data.js` from SQLite.
- Phase 5: `build_topic_pages.py` — rebuilds `summary/topics/<class>.md` pages from SQLite.

Plus the `--audit-constants` invocation (per the SKILL's argument-hint line) which audits scripts against `canonical_constants.py` per `.claude/rules/math-scripts.md` "Audit Pipeline" — but this checks SCRIPTS for hardcodes, NOT the inventory for canonical_constants gaps.

What does NOT exist:
- A `--framework-diff` cross-check between inventory rows and `canonical_constants.PROVENANCE` keys — although `--framework-diff` IS in the SKILL.md argument-hint (line 4) as `Cross-check session entries vs framework-canonical entries`, it covers the session→framework direction, not the inventory→canonical-constants direction.
- A POST-HOOK on `update_constant(...)` calls that automatically appends to the inventory's audit-pin sub-row.
- A POST-HOOK on inventory edits (the `mack-cosmic-bridge` sole-writer) that automatically queues a corresponding canonical_constants promotion gate.

The existing pre-tool hooks (`.claude/hooks/math-is-hard.sh`, `.claude/hooks/PRIME-DIRECTIVE.sh`, etc.) are session-startup / tool-call directives, not registry-sync enforcers.

**The architectural inference**: the W14-1..W14-5 pattern (5/5 consecutive gates surfacing the same gap) is structurally guaranteed in the absence of a sync hook. Adding ONE audit script `_inventory_canonical_sync_audit.py` invoked under `/weave --update` Phase 2 (after `extract_entities.py` rebuilds the knowledge index) would catch the gap at index-rebuild time, well before the next META gate is dispatched.

**Classification**: META (infrastructure gap; remediation belongs in `/weave --update` Phase 2 plus a new audit script).

### II.4 Audit-pin sub-row pattern (3.audit/7.audit/9.audit/12.audit/21.audit-block): permanent vs scaffolding

**Result**: The audit-pin sub-row pattern is **PERMANENT inventory schema convention**, NOT one-time SHA-discipline scaffolding. Substitution chain establishing this:

1. *Definition*: "permanent schema convention" = a row class that future inventory rows will adopt by default; "one-time scaffolding" = a row class created to bridge a specific historical gap, slated for retirement once the gap is closed.
2. *Substitution* — three structural arguments:
   - (a) **Format-discipline persistence**: `.claude/rules/gate-verdicts.md` requires "the closure SHA MUST be the full 64-character hexdigest — never a head-truncated prefix" in canonical verdict lines, with the 16-char head form allowed ONLY in prose for human scan-readability. Inventory rows carry 16-hex prefix in the human-prose cells (audit_sha256 column); the audit-pin sub-row carries the full-64-hex form. This dual-form coexistence is structurally required by the rule and applies to ALL future framework predictions, not just the W14-1..W14-6 set.
   - (b) **Multi-source pin closure**: W14-4's 9.audit sub-row pins THREE per-pathway sources (S82 + S67 + S85 W9-3); W14-6's 21.audit-block pins FIVE upstream sources (W8-4 + W11 C5 + W11 C6 + W12 C30 + P11). The single-row primary cell cannot accommodate multi-source pinning without becoming unreadable; the sub-row pattern IS the schema solution to multi-source pinning.
   - (c) **Forward-extensibility**: the `feedback_research-corpus.md` precedent (collaboration documents have a Section 6 summary table read first, not whole doc) suggests the inventory's primary table + audit-pin sub-row pattern is the READ-FIRST/AUDIT-SECOND structural division. Future audit upgrades (e.g., post-DESI-DR3 W10-2 R_842 audit-pin re-emission, post-LiteBIRD r-window audit-pin re-emission) will follow the same sub-row pattern, not invent a new one.
3. *Simplification*: the W14-2/3/4/5/6 wave landed FIVE audit-pin sub-rows in one wave with consistent structural form. The pattern is instantiated, not provisional.
4. *Direction*: **PERMANENT schema convention**. Future framework predictions promoted to the inventory will follow the same `<N>.audit` sub-row pattern (or `<N>.audit-block` consolidated form when the upstream chain shares 4+ pins). The pattern is forward-canonical.

**One small caveat**: the sub-row pattern's INSERTION POINT (immediately after the primary row) is a layout convention, not a structural requirement. Future inventory schema upgrades may consolidate audit-pin sub-rows into a separate "## Audit-pin Sub-rows" section at the bottom of the inventory file, leaving the primary table cleaner. This would be a layout migration, not a pattern retirement.

**Classification**: META (inventory schema; no physics impact).

### II.5 r_PathH primary anchoring (W12 C32 OQ-2 surface)

**Result**: `r_PathH = 0.00745` is plan-pinned in W12-2 §7 (the BK-Array classifier) but is NOT in `canonical_constants.py`. The W12 OQ-2 (per `session-86-w12-workingpaper.md:619`) classifies this as `SOURCE-RECON class-(c) PIN-DRIFT-FROM-STALE-SOURCE` per `.claude/rules/epistemic-discipline.md` and queues `S87-R-PATH-H-PRIMARY-ANCHORING` as the remediation gate.

The high-precision form `r_CMB_framework = 0.011731522176014426` IS canonical (`canonical_constants.py:30`, S83 W3-G46 TENSOR-TRANSFER PASS, with PROVENANCE entry at line 869). This is the Path-C value (Volovik-type substrate-compaction tensor), NOT Path-H.

**Architectural placement**: `r_PathH` is the dual-pathway tensor-mode prediction's H-pathway value. Its absence from `canonical_constants.py` (vs `r_PathC = r_CMB_framework` already canonical) is exactly the W14-1..W14-5 gap pattern, observed one wave earlier in W12. The S87-R-PATH-H-PRIMARY-ANCHORING gate per `session-86-w12-workingpaper.md:619` is the W12-side analog of `S87-CANONICAL-CONSTANTS-W14-RESIDUAL`. Both should be discharged in the same S87 W0 cleanup wave.

The substitution chain for whether r_PathH should be promoted directly OR re-derived from primary substrate source first:

1. *Definition*: "primary substrate source" = the spectral-triple derivation that produces the value from D_K eigenvalues + spectral moments, NOT a downstream gate citing the value.
2. *Substitution*: r_PathH = 0.00745 traces (per W12 OQ-2) to "oral citation only via S85 W1b-6 (untraced in knowledge index)". The S85 W1a-4 substrate-eigenvalue-partition (B1/B2 modes) is the upstream derivation — but the mapping from B1/B2 partition fractions to the specific value 0.00745 is not currently a closed substitution chain on disk.
3. *Direction*: r_PathH should NOT be promoted to canonical_constants until either (a) a primary-source derivation is locked, OR (b) the S85 W1b-6 citation is recovered and pinned. Otherwise the canonical_constants entry becomes a citation-only stub (PIN-DRIFT-FROM-STALE-SOURCE class-(c)) — exactly the failure mode `.claude/rules/epistemic-discipline.md` Source-Reconciliation rule Class-(c) defines as MANDATORY remediation.

**Classification**: META (provenance gap; out-of-scope for direct in-session promotion until S87 primary-source recovery).

---

## III. Gate Verdicts

These verdicts are NOT re-adjudicated — they are inherited from the W12/W14 working papers and serve as the architectural-review anchor.

| Gate | Verdict | Decisive Number | Source |
|:-----|:--------|:----------------|:-------|
| `S86-WATCHLIST-W1-EDIT` | FAIL | "row-numbering-mismatch-route-b" | W14 §line 25 |
| `S86-WATCHLIST-W2-EDIT` (Row #3 α_s) | PASS | sha_citations_added=1 | W14 §line 129 |
| `S86-WATCHLIST-W3-EDIT` (Row #7 CGWB) | PASS | audit_subrow=1 + paragraphs=1 + column=0 | W14 §line 219 |
| `S86-WATCHLIST-W4-EDIT` (Row #9 f_NL) | PASS | pathway_audit_pins=3 | W14 §line 359 |
| `S86-WATCHLIST-W5-EDIT` (Row #12 A_s) | PASS | sub_note=1 + sub_row_12.audit=1 | W14 §line 487 |
| `S86-WATCHLIST-W6-NEW-CLASS` | PASS | new_rows=9 + audit-block + summary-section | W14 §line 636 |
| W12 OQ-2 (`S87-R-PATH-H-PRIMARY-ANCHORING`) | OPEN (carry-forward) | — | W12 §line 619 |
| `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` | OPEN (carry-forward) | — | W14 §lines 313, 437, 583 |

**Cross-checks** (independent of source-doc adjudication):
- The 5 PASS gates are structurally homogeneous: each lands an audit-pin sub-row with full-64-hex pins for the cited W13-2 / S82+S67+S85 / W13 P1 / W8-4+C5+C6+C30+P11 source chain. The pattern is internally consistent.
- The 1 FAIL gate (W14-1) is timing-induced (parallel-session race with W13 P11), not methodological. The carry-forward `S86-INVENTORY-W14-1-ROW-W_0-CREATION` is moot post-P11; W14-1 is re-dispatchable as a PASS-route-(a) follow-up if desired (LOW priority per W14 §line 789).
- `r_CMB_framework = 0.011731522176014426` IS in canonical_constants.py with PROVENANCE (S83 W3-G46 TENSOR-TRANSFER, line 869) — verified by direct grep. This is the Path-C value, confirming that ONE side of the dual-pathway is already canonical-anchored; only Path-H is not.

---

## IV. Structural Implications

The W14 wave's surfacing of the inventory↔canonical_constants divergence is an architectural-correction event, not a physics-correction event. Three structural implications:

**(IV.1) The inventory is a SHA-pinned audit-trail registry, not a value-import target.** computation scripts cannot import from a markdown file; the inventory's role is to anchor falsifier-side annotation (live-watch envelopes, internal-consistency splits, detector horizons, dual-pathway / band / pathway-keyed structure) to verdict-file-pinned values. The canonical_constants module's role is to expose individual scalar / array values for computation import. These two registries are STRUCTURALLY DISTINCT and should remain so. The architectural fix is NOT to merge them — it is to enforce sync between them.

**(IV.2) Sub-keying expansion at canonical_constants Step 2 is structurally required for ALL ambiguous predictions.** Three of the five families (`f_NL_FW`, `A_s_FW`, dual-pathway `r`) require sub-keys (pathway-keyed, pivot-keyed, pathway-keyed) because a single scalar would erase the structural ambiguity. The W14-4 + W14-5 carry-forward specs already enumerate the sub-keys (`f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template`, `A_s_FW_eps_02163`, `A_s_FW_eps_020`); these names are forward-canonical. For Path-H/Path-C r, the natural sub-key pattern is `r_PathH_FW` and `r_PathC_FW = r_CMB_framework` (alias to the existing canonical), once primary-source anchoring lands.

**(IV.3) The 5-gate convergent surface IS the constraint map for inventory-vs-canonical-constants discipline.** Per `feedback_reporting-framing.md`, the 5/5 PASS gates plus the 1/1 FAIL gate are NOT a session-success metric — they are a structural mapping of where the registry-layer constraint surface lies. The constraint surface boundary, post-W14, is: **the inventory carries 5 framework headline observables in fully audited form; canonical_constants.py carries 0 of the 5 with matching PROVENANCE entries (the `dE_a` lab-falsifier suite is the exception, promoted in W14-6 in-session per `feedback_fix-in-session-never-defer.md`).** This is the corridor S87 W0 closes.

**Substrate framing reminder (per `.claude/rules/phononic-framing.md`)**: all five families ARE substrate observables (PHONONIC for w_0 / α_s / Ω_GW / f_NL / A_s; LAB-FALSIFIER for dE_a) — they emerge from D_K eigenvalues + spectral moments under specific regulator conventions. The architectural review is META; the substrate physics is unchanged. The inventory's audit-pin sub-rows preserve the substrate-framing assessment per row (W14-2 §line 169-171; W14-3 §lines 289-295; W14-4 §lines 414-422; W14-5 §lines 562-568; W14-6 §lines 697-706); promoting the values to canonical_constants will inherit the same substrate framing via the PROVENANCE comment field.

---

## V. Carry-Forward Computations

Per `feedback_fix-in-session-never-defer.md`, every entry has 4 fields. The W14 wave already opened `S87-CANONICAL-CONSTANTS-W14-RESIDUAL`; this synthesis CONSOLIDATES it (no duplicates, per §V.4 below) and adds two architectural-rule entries.

### V.1 S87-CANONICAL-CONSTANTS-W14-RESIDUAL (consolidated, supersedes W14-3/4/5/6 individual carry-forwards)

- **What**: Promote the five framework headline observable families from `falsifier-master-inventory.md` into `computations/canonical_constants.py` with full PROVENANCE dict entries. Specifically: (a) add PROVENANCE entry for existing `w0_FW = -0.918` (currently missing); (b) add `w0_FW_R842 = -0.842454` constant + PROVENANCE (substrate-compaction branch-(iv)); (c) add `alpha_s_FW = alpha_s_inflation_framework` alias (or rename inventory cite to use canonical handle); (d) add `Omega_GW_LISA = 8.299e-58` constant + PROVENANCE; (e) add three sub-keyed `f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template` constants + PROVENANCE entries; (f) add two sub-keyed `A_s_FW_eps_02163 = 3.11e-9` and `A_s_FW_eps_020 = 4.27e-9` constants + PROVENANCE entries; (g) add PROVENANCE entry for existing `M_KK = 7.428660036284456e+16` (value present, provenance missing per W14-6 §line 621).
- **Inputs**: `computations/canonical_constants.py` (current state); `computations/s85_gate_verdicts.txt:201` (W13-2 audit pin `f514d642fe2a80ac…`); `computations/s86_gate_verdicts.txt:217` (W13 P1 FROZEN-COMMIT-LANDING `e774fc99cb1ea3d2…`); `computations/s82_gate_verdicts.txt:34` (S82 W3-4 GGE-FNL pin `fe8c7d0e6b96187d…`); `computations/s85_gate_verdicts.txt:161` (S85 W9-3 pin `2484b4a24419329…`); `summary/session-67-final.md:1393` (S67 GGE-folded prose anchor); `sessions/framework/registry/falsifier-master-inventory.md` (post-W14 SHA `7e0879a579dd6752…`).
- **Gate**: `S87-CANONICAL-CONSTANTS-W14-RESIDUAL`. PASS = all 11 entries (5 new constants × 1 each + 6 PROVENANCE-only entries) present in `canonical_constants.py` with `update_constant(...)` provenance; `mcp__knowledge__get_constant("X")` returns a populated record for each of `{w0_FW, w0_FW_R842, alpha_s_FW (or alias), Omega_GW_LISA, f_NL_FW_*, A_s_FW_*, M_KK}`; post-promotion `/weave --update` rebuild produces 0 inventory-vs-canonical-constants drift entries. FAIL = any entry missing OR any value disagrees with its citing inventory cell / verdict line. INFO = sub-keyed family naming differs from this spec but is internally consistent.
- **Effort**: ~45 min (11 `update_constant` calls + verdict-file grep verification + `/weave --update` rebuild + spot-check of MCP responses + S87 W0 verdict-line append). Single agent session (gen-physicist or sagan-empiricist).

### V.2 S87-R-PATH-H-PRIMARY-ANCHORING (open-canonical follow-up to W12 OQ-2)

- **What**: Re-derive `r_PathH = 0.00745` from primary substrate source (S85 W1a-4 substrate-eigenvalue-partition for B1/B2 modes) OR locate the S85 W1b-6 citation that originated the value. After primary source is locked, promote `r_PathH_FW` to `canonical_constants.py` with PROVENANCE. The dual-pathway companion `r_PathC_FW = r_CMB_framework = 0.011731522176014426` (already canonical at line 30 / PROVENANCE line 869) gets a parallel `r_PathC_FW` alias added so the dual-pathway naming convention is symmetric.
- **Inputs**: `canonical_constants.py` (`r_CMB_framework` line 30 + PROVENANCE line 869, S83 W3-G46); `sessions/archive/session-85/session-85-w1a-workingpaper.md` (substrate-eigenvalue-partition derivation if recoverable); `sessions/archive/session-86/session-86-w1c-workingpaper.md` (W1c-8 r-dual-function-promotion `S86-FALSIFIER-MASTER-INVENTORY-PROMOTION` with audit `32c60c2f69fe6150`); `sessions/archive/session-86/session-86-w12-workingpaper.md:619` (OQ-2 SOURCE-RECON class-(c) classification).
- **Gate**: `S87-R-PATH-H-PRIMARY-ANCHORING`. PASS = primary substrate source for r_PathH = 0.00745 is closed AND `update_constant("r_PathH_FW", 0.00745, ...)` lands AND alias `r_PathC_FW = r_CMB_framework` lands AND `mcp__knowledge__get_constant` returns populated records for both. INFO = primary source unrecoverable; r_PathH_FW is pinned-but-flagged with `provenance_status="ORAL_CITATION_S85_W1b_6_PENDING"` and a follow-up gate `S88-R-PATH-H-DERIVATION` is queued. FAIL = primary source contradicts 0.00745 by more than the W12-2 4-branch boundary tolerance (which would invalidate the BK-Array 2026 classifier).
- **Effort**: ~60 min (primary-source recovery is the main effort; if INFO route, ~20 min). Single agent session (volovik-superfluid-universe-theorist as the dual-pathway-derivation owner).

### V.3 S87-WEAVE-UPDATE-INVENTORY-CANONICAL-SYNC-AUDIT (NEW infrastructure gate)

- **What**: Add a new audit script `computations/_inventory_canonical_sync_audit.py` that reads `sessions/framework/registry/falsifier-master-inventory.md`, extracts the row-cited value names (currently w_0, alpha_s, rho_AC / Omega_GW_LISA, f_NL_folded, A_s, dE_a 9-row class), cross-references `computations/canonical_constants.py` PROVENANCE dict, and emits a report of missing PROVENANCE entries + missing constants. Wire the audit into `/weave --update` Phase 2 (after `extract_entities.py` rebuilds the knowledge index, before `knowledge_db.py --sync`). The audit emits INFO for each gap (NOT FAIL) so the audit does not block index rebuilds; ORCHESTRATOR consumes the report at session-start to dispatch in-session promotion gates.
- **Inputs**: `sessions/framework/registry/falsifier-master-inventory.md`; `computations/canonical_constants.py` (PROVENANCE dict at Section F, line 685+); `.claude/skills/weave/SKILL.md` (insertion point at Phase 2). The script uses Python's regex to extract value-name tokens from inventory rows + `ast.parse` on canonical_constants.py to extract the PROVENANCE dict literal.
- **Gate**: `S87-WEAVE-UPDATE-INVENTORY-CANONICAL-SYNC-AUDIT`. PASS = `_inventory_canonical_sync_audit.py` runs cleanly, emits a report at `tools/inventory_sync_audit.json` listing 0 missing entries (assuming S87-CANONICAL-CONSTANTS-W14-RESIDUAL has discharged); `/weave --update` Phase 2 invokes the audit and writes the report; SKILL.md `--update` documentation is updated to mention the new phase. INFO = report emitted with N>0 missing entries (the audit working but residual gaps remain). FAIL = audit script crashes OR produces malformed report OR `/weave --update` hook integration breaks.
- **Effort**: ~90 min (script authoring 45 min + SKILL.md doc update 15 min + integration test 20 min + verdict closure 10 min). Single agent session (gen-physicist or kitaev-instanton-theorist).

### V.4 Carry-forward consolidation note

This synthesis's V.1 SUPERSEDES the individual `S87-CANONICAL-ALPHA-S-FW-PROVENANCE-PROMOTION` (W14-2), `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` (W14-3 original opener), W14-4 contribution, W14-5 contribution, and W14-6 extension carry-forwards. The plan-author for S87 should treat V.1 as the canonical 4-field spec for the consolidated promotion gate; the individual W14-N entries are documentation-only references to the per-gate origin of each sub-family. No duplicate carry-forward is generated.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Inventory is the de-facto canonical write-source for 5 framework headline observables; canonical_constants.py has 0/5 PROVENANCE entries for them | META | OPEN (S87-CANONICAL-CONSTANTS-W14-RESIDUAL) | computation scripts cannot import these values today; inventory carries the audit trail but is not import-target for Python |
| 2 | Forward-canonical write-order for new framework predictions: verdict → canonical_constants → inventory | META | PROPOSED (rule-file diff in §VII) | Reverses the W14-observed (1)→(3)→(2) order; closes the canonical-import gap at write-time |
| 3 | `/weave --update` has no inventory↔canonical_constants sync hook | META | OPEN (S87-WEAVE-UPDATE-INVENTORY-CANONICAL-SYNC-AUDIT) | The W14-N pattern (5/5 gates surfacing same gap) was structurally guaranteed in absence of this hook |
| 4 | Audit-pin sub-row pattern (`<N>.audit` / `<N>.audit-block`) is permanent inventory schema convention | META | LANDED (W14-2/3/4/5/6 + P11) | Future framework-prediction promotions to inventory will follow the same sub-row pattern |
| 5 | r_PathH primary anchoring is the W12-side analog of the W14 gap | META | OPEN (S87-R-PATH-H-PRIMARY-ANCHORING) | Discharge in same S87 W0 cleanup wave as V.1 |
| 6 | r_CMB_framework = 0.011731522176014426 (= Path-C value) IS already canonical with PROVENANCE | META | LANDED (S83 W3-G46) | Confirms ONE side of dual-pathway is anchored; only Path-H is not |
| 7 | W14-1 FAIL is timing-honest (parallel-session race with W13 P11), not methodological | META | CLOSED-AT-LANDING (P11 created Row #1 = w_0 minutes after W14-1 dispatched) | Optional re-dispatch of W14-1 is LOW-priority |
| 8 | 7 lab `dE_a` constants promoted in-session per `feedback_fix-in-session-never-defer.md` (W14-6) | META | LANDED | Establishes the in-session promotion precedent for all future inventory→canonical_constants migrations |

---

## VII. Proposed Architectural-Decision Document (Code-Block — Orchestrator installs after review)

The orchestrator should install the following content as `sessions/framework/registry/canonical-source-architecture.md`:

```markdown
# Canonical Source Architecture (S86 W14 + W12 OQ-2 surface)

> **Provenance**: S86 1a Slot S-6 architectural review (gen-physicist, 2026-04-27).
> Promotion of the W14-1..W14-6 + W12 OQ-2 surface findings to permanent
> framework-level architecture document.
>
> **Sole writer**: gen-physicist (META scope; not a falsifier-inventory entry).
> **Cross-references**: `computations/canonical_constants.py` (Section F PROVENANCE dict);
> `sessions/framework/registry/falsifier-master-inventory.md` (audit-pin sub-row schema);
> `.claude/skills/weave/SKILL.md` (`--update` Phase pipeline);
> `.claude/rules/math-scripts.md` §"Canonical Constants (MANDATORY)" (write-order rule).

## Two-Layer Canonical Source Model

The framework uses TWO STRUCTURALLY DISTINCT canonical registries, each with a
different consumer:

| Layer | File | Consumer | What it canonicalizes |
|:------|:-----|:---------|:----------------------|
| Import-canonical | `computations/canonical_constants.py` | computation Python scripts (`from canonical_constants import *`) | Scalar/array values + PROVENANCE dict |
| Audit-trail-canonical | `sessions/framework/registry/falsifier-master-inventory.md` | mack-cosmic-bridge (sole writer); downstream falsifier consumers; reader-facing detector-horizon table | Falsifier annotation: live-watch envelope, internal-consistency split, detector horizon, dual-pathway / band / pathway-keyed structure, full-64-hex audit pins |

These two layers are NOT interchangeable. The inventory is markdown — computation
scripts cannot import from it. The canonical_constants module is Python — it
cannot carry the cross-reference structure (PAIR-N annotations, audit-pin
sub-rows, detector horizons) the inventory requires.

## Forward-Canonical Write-Order: (1) verdict → (2) canonical_constants → (3) inventory

When a computation gate produces a new framework prediction value `P`, the canonical
write-order for downstream consumption is:

**Step 1 — Verdict-file emission** (mandatory; producing script):
```
{GATE_ID}: PASS|FAIL|INFO -- value=<P_value> scheme=<s> convention=<c> L_max=<L>
audit_sha256=<full-64-hex> content_sha256=<full-64-hex> schema_version=R3
```
appended to `computations/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`.

**Step 2 — canonical_constants.py promotion** (mandatory; orchestrator OR
producing-script's post-write hook):
```python
update_constant("P_FW", P_value, session="S{N}",
                source="S{N}-{GATE_ID}", comment="<one-line provenance>")
```
which (a) adds `P_FW = P_value` to the appropriate Section (E for cosmological
observables; B for geometric; C for BCS; D for spectral action) and (b) adds
a PROVENANCE entry citing the verdict-line `audit_sha256`.

For STRUCTURED predictions (band, pathway-keyed, pivot-keyed), Step 2 expands
to multiple sub-keyed entries per the W14 precedents:
- Pathway-keyed: `P_FW_S{N}_<scheme>` per pathway (W14-4 f_NL family).
- Pivot-keyed: `P_FW_<param>_<value>` per pivot (W14-5 A_s family).
- Branch-keyed: `P_FW` (canonical) + `P_FW_<branch>` (alternative; W14-1 w_0
  Volovik-partition vs substrate-compaction R_842 dual).

**Step 3 — inventory row landing** (mandatory; mack-cosmic-bridge as sole writer
per `feedback_mack-bridge-role.md`):
- Append a new row to `sessions/framework/registry/falsifier-master-inventory.md` (or an
  audit-pin `<N>.audit` sub-row if the row already exists), citing BOTH the
  verdict-line audit_sha256 (full-64-hex) AND the canonical_constants entry
  name (e.g., "framework value = canonical_constants.P_FW").
- Carry the falsifier-side annotation (live-watch envelope, detector horizon,
  internal-consistency split, dual-pathway / band / pathway-keyed structure).

## Why this order

Under (1)→(2)→(3), computation scripts can begin consuming `P_FW` via
`from canonical_constants import P_FW` immediately after Step 2; the inventory
citation (Step 3) adds falsifier-side annotation but is not a prerequisite for
computation consumption.

Under the WRONG order (1)→(3)→(2) (the W14-1..W14-5 observed pattern), computation
scripts cannot consume `P_FW` until Step 3' completes — which may be one or
more sessions later, creating a window where the value is "canonical in
inventory but invisible to computation import". This is a registry-layer
constraint surface failure that consistently surfaces 5+ META gates in a
row before the gap is closed.

## Sync Enforcement

`/weave --update` Phase 2 (after `tools/extract_entities.py` rebuilds
`tools/knowledge-index.json`, before `tools/knowledge_db.py --sync`) invokes
`computations/_inventory_canonical_sync_audit.py` (S87+ infrastructure;
see `S87-WEAVE-UPDATE-INVENTORY-CANONICAL-SYNC-AUDIT`). The audit:
1. Parses `falsifier-master-inventory.md` and extracts the row-cited value
   names (e.g., w_0, α_s, ρ_AC / Ω_GW_LISA, f_NL_folded, A_s, dE_a).
2. Parses `canonical_constants.py` PROVENANCE dict via `ast.parse`.
3. Emits `tools/inventory_sync_audit.json` listing missing PROVENANCE
   entries + missing constants.
4. Returns INFO (not FAIL) so the audit does not block index rebuilds; the
   orchestrator consumes the report at session-start to dispatch in-session
   promotion gates.

## Audit-Pin Sub-Row Schema (PERMANENT)

The inventory's audit-pin sub-row pattern (rows `3.audit`, `7.audit`, `9.audit`,
`12.audit`, consolidated `21.audit-block`) is the canonical form for carrying
full-64-hex audit pins per `.claude/rules/gate-verdicts.md` while keeping the
primary-row cells human-prose-readable with 16-hex prefix form. This pattern
is PERMANENT, not one-time scaffolding. New inventory rows that cite multi-
source upstream chains (3+ pinned sources) should use the `<N>.audit-block`
consolidated form; single-source rows use `<N>.audit`.

## In-Session vs Carry-Forward Promotion

Per `feedback_fix-in-session-never-defer.md`: when an in-session gate
surfaces a missing canonical_constants entry that can be fixed with a single
`update_constant(...)` call, FIX-IN-SESSION (the W14-6 dE_a precedent).
When the gap requires primary-source recovery (W12 OQ-2 r_PathH PIN-DRIFT
class-(c)) or sub-keying decisions (W14-4 f_NL pathway sub-keying), generate
a 4-field carry-forward spec and queue for next session. The two routes are
the two halves of the no-technical-debt rule (CLAUDE.md §"No Technical Debt").

## Cross-References

- `feedback_fix-in-session-never-defer.md` — every synthesis must produce structured carry-forwards
- `feedback_fix-in-session-never-defer.md` — in-session promotion precedent
- `feedback_mack-bridge-role.md` — sole writer for inventory rows
- `.claude/rules/gate-verdicts.md` — full-64-hex audit-pin canonical form
- `.claude/rules/math-scripts.md` — canonical_constants import rule
- `.claude/rules/epistemic-discipline.md` — Source-Reconciliation 5-class taxonomy
- `computations/canonical_constants.py` Section F — PROVENANCE dict structure
- `sessions/framework/registry/falsifier-master-inventory.md` — audit-pin sub-row schema instances

## Provenance

- Architecture-document promotion: S86 1a Slot S-6 (gen-physicist, 2026-04-27).
- Surface-finding gates: W14-1 (FAIL, row-numbering-mismatch); W14-2 / W14-3 /
  W14-4 / W14-5 / W14-6 (5× PASS, audit-pin sub-row pattern); W12 OQ-2
  (r_PathH OPEN carry-forward); W14-6 (in-session dE_a promotion precedent).
- W14 working paper: `sessions/archive/session-86/session-86-w14-workingpaper.md`.
- W12 working paper: `sessions/archive/session-86/session-86-w12-workingpaper.md`.
```

---

## VIII. Proposed Rule-File Diff for `.claude/rules/math-scripts.md` (Code-Block — Orchestrator installs after review)

Insert AFTER the existing "## Canonical Constants (MANDATORY)" section, BEFORE the "## Local Variable Tagging" section, the following addition:

```markdown
## Canonical Write-Order for New Framework Predictions (S86 1a S-6 surface)

> **Provenance**: S86 1a Slot S-6 architectural review surfaced that the W14-1..W14-5
> META gates each returned `Constant 'X_FW' not found` for 5 framework headline
> observables present in `sessions/framework/registry/falsifier-master-inventory.md` but
> missing from `canonical_constants.py`. The structural cause was an inverted
> write-order. Promoted to permanent rule per the architectural decision document at
> `sessions/framework/registry/canonical-source-architecture.md`.

When a computation gate produces a new framework prediction value `P`, the producing
script (or its post-write orchestrator hook) MUST follow the canonical
write-order **(1) verdict file → (2) canonical_constants.py → (3) falsifier-
master-inventory.md**:

1. **Step 1 — Verdict-file emission**: append the canonical dual-SHA verdict
   line to `computations/s{N}_gate_verdicts.txt` per `.claude/rules/gate-
   verdicts.md`. This MUST happen first so the value is permanently pinned with
   audit_sha256 + content_sha256.

2. **Step 2 — canonical_constants.py promotion**: invoke
   `update_constant("P_FW", P_value, session="S{N}", source="S{N}-{GATE_ID}",
   comment="<provenance>")` to add the value AND its PROVENANCE entry. For
   STRUCTURED predictions (band, pathway-keyed, pivot-keyed), Step 2 expands
   to multiple sub-keyed entries — per the W14-4 / W14-5 precedents:
   - Pathway-keyed: `P_FW_<scheme>` per pathway (e.g., `f_NL_FW_S82_equilateral`,
     `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template`).
   - Pivot-keyed: `P_FW_<param>_<value>` per pivot (e.g., `A_s_FW_eps_02163`,
     `A_s_FW_eps_020`).
   - Branch-keyed: `P_FW` canonical + `P_FW_<branch>` alternative (e.g., `w0_FW`
     Volovik-partition + `w0_FW_R842` substrate-compaction).
   This step is mandatory BEFORE Step 3, because computation scripts CANNOT import
   from the inventory markdown file — only canonical_constants.py is import-target.

3. **Step 3 — Inventory row landing**: mack-cosmic-bridge (sole writer per
   `feedback_mack-bridge-role.md`) appends a new row OR audit-pin sub-row to
   `sessions/framework/registry/falsifier-master-inventory.md` citing BOTH the verdict-line
   audit_sha256 (full-64-hex per `.claude/rules/gate-verdicts.md`) AND the
   canonical_constants entry name. The inventory carries the falsifier-side
   annotation (live-watch envelope, detector horizon, internal-consistency
   split, dual-pathway / band / pathway-keyed structure).

### What goes wrong under the inverted order (1)→(3)→(2)

Under inverted order, computation scripts CANNOT consume `P_FW` via `from
canonical_constants import P_FW` until Step 3' completes — which may be one
or more sessions later. This creates a window where the value is "canonical
in the inventory but invisible to computation import". The W14-1..W14-5 wave
surfaced exactly this failure mode for 5 consecutive META gates.

### In-session promotion vs carry-forward (decision rule)

Per `feedback_fix-in-session-never-defer.md`:
- If Step 2 is a single `update_constant(...)` call with no derivation ambiguity
  (e.g., the W14-6 dE_a 7-constant promotion): **FIX-IN-SESSION**. Add the
  entries directly to `canonical_constants.py` before terminating the gate.
- If Step 2 requires sub-keying decisions (pathway/pivot/branch ambiguity)
  OR primary-source recovery (PIN-DRIFT class-(c) per `.claude/rules/epistemic-
  discipline.md` Source-Reconciliation): **CARRY-FORWARD with 4-field spec**.
  Queue for next session; do NOT promote a single-value stub.

### Sync enforcement (`/weave --update`)

`/weave --update` Phase 2 invokes `computations/_inventory_canonical_
sync_audit.py` (S87+) after `tools/extract_entities.py` rebuilds the knowledge
index. The audit emits `tools/inventory_sync_audit.json` listing missing
PROVENANCE entries + missing constants. The audit returns INFO (not FAIL),
so it does not block index rebuilds; the orchestrator consumes the report at
session-start to dispatch in-session promotion gates.
```

---

## IX. Substrate-Framing Assessment (per `.claude/rules/phononic-framing.md`)

This synthesis is a META architectural review of the registry-layer constraint
surface. The five framework headline observables it discusses (w_0, α_s, Ω_GW,
f_NL, A_s) are each substrate observables (PHONONIC) — they emerge from D_K
eigenvalues + spectral moments under specific regulator conventions per
`.claude/rules/regulator-pin-discipline.md` (Section F PROVENANCE entries
should carry the `regulator-tag` field per `.claude/rules/regulator-pin-
discipline.md` when promoted). The inventory's audit-pin sub-rows preserve
the substrate-framing assessment per row (W14-2 §lines 169-171; W14-3 §lines
289-295; W14-4 §lines 414-422; W14-5 §lines 562-568; W14-6 §lines 697-706);
promotion to canonical_constants will inherit the same substrate framing via
the PROVENANCE comment field.

The 9 lab-falsifier dE_a constants (W14-6 in-session promotion) are LAB-
FALSIFIER-A class observables — they probe substrate-direction asymmetric
coverage (3 platforms × 3 lambda directions, with λ_8 resolved only via
¹⁷³Yb sweet-spot SW3). The promotion preserves the substrate framing: the
constants are M_KK-normalized δE_a ratios; SI translation to laboratory units
remains W11 C5's domain and is preserved as the inventory row-cell SI value.
M_KK itself (`= 7.428660036284456e+16` GeV) IS the compactification scale
emergent from the spectral triple's a_2 Seeley-DeWitt coefficient projection,
NOT a Kaluza-Klein "internal extra dimension" container. The architectural
decision document IX.A above (canonical-source-architecture.md) preserves
this substrate framing explicitly.

There is NO container-thinking violation in this synthesis: every value is a
substrate-derived spectral moment, and the architectural review classifies
the inventory and canonical_constants as two registries SERVING the substrate
predictions, not as separate "container" layers. Direction of explanation
flows FROM the spectral triple (D_K eigenvalues + Seeley-DeWitt moments)
TOWARD the registries (canonical_constants is the import-canonical layer for
computation scripts; inventory is the audit-trail-canonical layer for falsifier
annotation), NOT in reverse.

---

## X. Artifacts on Disk (Verification)

This is a synthesis-only output. No computation script, .npz, .png, or verdict-line
append is owed by this dispatch. The single artifact is this working-paper
section at:

- `sessions/archive/session-86/session-86-1a-s6-gen-physicist.md` (THIS FILE; ~21 KB).

The two PROPOSED outputs (architectural decision document + rule-file diff)
are written as code blocks in §VII and §VIII of THIS file; the orchestrator
installs them after review per the spawn-prompt instructions.

The verdicts cited in §III are inherited from the source working papers and
NOT re-adjudicated by this synthesis.

---

## XI. Cross-Domain Sanity Checks (gen-physicist niche)

This synthesis touches three sub-fields the cross-domain workhorse must
verify together:

1. **Registry architecture (META)**: per `.claude/rules/agent-standards.md`
   §"Agent-Memory Registry Inversion (AMRI)", the inventory↔canonical_constants
   gap is ARMI-shaped — both registries are project-level, neither is agent-
   memory-private, and the gap is exactly the input-pin test failure case (a
   downstream gate cites the inventory but the inventory is not import-target,
   while canonical_constants is import-target but missing the entry). The §VII
   architectural decision document explicitly addresses this with the two-
   layer canonical source model.

2. **PRDR / PRU pre-registration discipline (per `.claude/rules/epistemic-
   discipline.md`)**: the W14-1 FAIL is a PRU-Class-8 surface (the plan
   pre-registered a row identity that did not exist on disk at gate-fire
   time), but it was correctly FLAGGED rather than PASS-forced — exactly the
   PRU rule's intent. The W14-2..6 PASS gates are NOT PRU-vulnerable (each
   landed an additive sub-row whose content was fully pre-determined by Field
   9 PASS criteria).

3. **Substrate framing (per `.claude/rules/phononic-framing.md`)**: §IX
   above confirms zero container-thinking violations. The architectural
   review preserves the direction-of-explanation: spectral triple →
   registries → computation consumers, NOT containers → emergent registries.

The synthesis passes all three cross-domain checks. No conflict-flagging
required.
