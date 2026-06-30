# Investigation 2 Housekeeping Ledger

**Date**: 2026-06-14
**Investigation**: 2 (single-wave guinea-pig run; Wave 1 terminal)
**Authoritative scope**: `.claude/rules/Investigating-Workshops.md §"Q2"`
**Track adaptation**: INVESTIGATION track. Per `gate-verdicts.md §"Investigation-Track Canonical Path"`, an investigation result enters the permanent record ONLY when promoted into a session; the orchestrator MUST NOT directly mutate curated session-track registers (atlas-*, permanent-results-registry.md) from this track. Consequence: register-annotation Q2 items that a SESSION-track orchestrator would effect in §A are instead ROUTED to **session-promotion** in §B (the "why-not-§A" being the track-local boundary, not a compute requirement).

## Q2 marker (citation)

A candidate is Q2 iff its resolution is a status-tag edit / mechanical promotion / rule-file diff / audit-script extension / mechanical re-run, rather than a derivation that produces a new structural claim. See `Investigating-Workshops.md §"Q2"`.

---

## §A. In-session resolutions (already effected; ledger only)

Per `feedback_fix-in-session-never-defer.md`: items FIXED during the Investigation-2 Wave-1 run, within the orchestrator's investigation-track write authority (project tooling + investigation-local docs — NOT session-track curated registers).

| # | Source | Item | Resolution (file:lines) | Verified |
|:--|:-------|:-----|:------------------------|:---------|
| A1 | INV2-W1-1..3 (hook WARN surfaced by INV2-W1-3) | python-validate hook false-positive: `FILENAME_RE` rejected the investigation-track `inv{n}_*.py` convention (was `s{N}_*.py`-only), warning on every investigation script | `.claude/hooks/python-validate.py:40` (regex) + `:12` (docstring) + `:157-159` (WARN msg); `.claude/hooks/python-validate.sh:16` (comment) | regex tested on disk: all 3 `inv2_*` + `s84_`/`s100a_` MATCH; `_helper`/random excluded |
| A2 | INV2-W1-4 workshop | Workshop doc had 4 orphan blank duplicate headers (Re:V-b / Re:V-c / C-b / C-Q) from R1 editing — removed (orchestrator-direct presentation patch, `/rclab-coordinate` Hard Rule 2) | `sessions/investigation/investigation-2/workshops/n3-chi-rescue-kasparov-faithfulness.md` | post-clean grep: single header each; 0 `*[NOT STARTED]*` |
| A3 | INV2-W1-4 workshop | WP §W1-4 stub (`Status: NOT STARTED`) → COMPLETED + structural verdict + workshop-md pointer (workshop gate closes by artifact-existence; no verdict line) | `sessions/investigation/investigation-2/investigation-2-w1-workingpaper.md` §W1-4 | on disk |
| A4 | INV2-W1-1 (gate agent) | WP §W1-1 classification GEOMETRIC→PARTICLE — self-corrected by the gate agent (plan YAML authoritative; skeleton transcription drift) | `sessions/investigation/investigation-2/investigation-2-w1-workingpaper.md:14` | on disk |

---

## §B. Session-promotion register items (Q2-class; ROUTED — investigation track-local boundary)

**Track-adapted §B.** These are Q2 register-annotation items (status-tag edits / registry annotations). On the SESSION track an orchestrator would effect them in §A; on the INVESTIGATION track they are NOT orchestrator-editable (curated, capstone-governing session-track registers — `gate-verdicts.md §"Investigation-Track Canonical Path"`). They carry NO compute spec (no 4-field What/Inputs/Gate/Effort — no substrate-physics re-run is needed); instead each carries the precise **target file:anchor + recommended edit** for turnkey application by the promoting session. **Mirror**: the WP `## Wave 1 Synthesis → Effected In-Session → "Routed to session-promotion"` paragraph + the workshop md's `Effected In-Session` rows (items 1-5). They are NOT in the WP `## Carry-Forward Computations` section (that section is MATH-only).

> **Why not §A (effect-in-session)** — uniform for B1–B5: the investigation track-local boundary forbids an investigation agent/orchestrator from mutating curated session-track registers; the change is a PROMOTION (requires session adoption), not a deferral. The promoting session applies each via its designated writer (e.g. `mack-cosmic-bridge` for falsifier-surface rows; the curated-doc designated writer for atlas prose) under the session hygiene gates.

### B1 — atlas-04 N7 two-leg split annotation [Q2-status-tag · session-promotion]
- **What**: annotate the N7 `STAGE-3-PERMANENT` tag as a TWO-LEG split: **(i)** algebraic-singleton `ℂ⊕ℍ⊕M₃(ℂ)` (§VII.O d-singleton; M₃ the only killable matrix block) = STAGE-3-PERMANENT **UNCONDITIONAL**; **(ii)** spectral-triple-for-D_total upgrade = **CONDITIONAL-on-χ-admissibility (LBA-5)**. "PERMANENT" attaches to (i) only.
- **Target**: `sessions/framework/Atlas/atlas-04-assumptions.md` (N7 cell, ~line 105).
- **Promotion gate**: session adoption + **capstone-hygiene 5-question gate** (atlas-04 D04 is capstone-governing per `.claude/rules/capstone-hygiene-gate.md` — Q3 status-change fires; the promoting session MUST run the 5Q block).
- **Source**: INV2-W1-4 workshop Effected-In-Session item 1.

### B2 — atlas-08 Q10 narration scope-fix [Q2-status-tag · session-promotion]
- **What**: annotate the Q10 "RESCUED → PROVEN STAGE-3-PERMANENT" narration so STAGE-3-PERMANENT attaches to N7-(i) [algebraic singleton + CLAIM-χ], NOT the FULL spectral-triple claim for D_total; N7-(ii) carries the explicit LBA-5 conditional. (Status-precision annotation — does not down-tag a proven theorem; scopes which sub-claim "PERMANENT" covers.)
- **Target**: `sessions/framework/Atlas/atlas-08-open-questions.md` (Q10 / S97 freshness, ~line 94).
- **Promotion gate**: session adoption; capstone-hygiene Q3 (status-scope change).
- **Source**: INV2-W1-4 workshop Effected-In-Session item 2.

### B3 — permanent-results-registry §VII.W-3 verdict-name + LBA-5 record [Q2-registry · session-promotion]
- **What**: record the INV2-W1-4 verdict-name "EXTRINSIC RESTRICTION WITH AXIOM-FORCED KERNEL" + the Step-A(extrinsic)/Step-B(axiom-forced) decomposition + LBA-5 PROMOTED to a named undischarged assumption (discharge condition = CF-INV2-W1-4-M1); cross-link the **EM-1** reconciliation of the line-287/13208 (forced) vs line-17004 (chosen) register contradiction (generic-Wedderburn-vs-singleton-specific level distinction).
- **Target**: `sessions/permanent-results-registry.md §VII.W-3.SUBSTRATE` (~line 17044) + `§VII.W-3.ALGEBRAIC` (~line 16975).
- **Promotion gate**: session adoption (registry-landing discipline; designated writer).
- **Source**: INV2-W1-4 workshop Effected-In-Session item 3.

### B4 — LBA-5 named-assumption registration [Q2-registry · session-promotion]
- **What**: register **LBA-5** = "M₃ χ-killing / Step-A restriction-to-BdG-sub-sector is admissible as an intrinsic (geometry-forced) operation" as a named load-bearing assumption, status PROMOTED-UNDISCHARGED; discharge gate = CF-INV2-W1-4-M1 (expected FAIL per the Q10 zero-map).
- **Target**: `sessions/framework/Atlas/atlas-04-assumptions.md` (assumptions ledger).
- **Promotion gate**: session adoption; capstone-hygiene Q3/Q4 (new named assumption on a capstone-governing register).
- **Source**: INV2-W1-4 workshop Effected-In-Session item 4.

### B5 — Q9 CLOSED→PARTIAL down-correction (NS-3) [Q2-status-tag · session-promotion]
- **What**: down-correct the Q9 status tag CLOSED → PARTIAL (NS-3).
- **Target**: `sessions/framework/Atlas/atlas-08-open-questions.md` (Q9).
- **Promotion gate**: session adoption; capstone-hygiene Q3.
- **Source**: `investigation-2-plan-index.md §"Routed out (not a gate)"`. **Reclassification note**: the plan-index tagged this "orchestrator effects in-session"; it is reclassified to session-promotion here for consistency with the investigation track-local boundary (an investigation must not mutate curated session-track registers — the same reason the workshop routed its own atlas edits to promotion). This is the consistent reading, not a deferral of an in-authority fix.

---

## §C. Parallel-compute-wave carry-forwards (Q3 wave-together)

(none — no Q3 N-axis parallel-compute-wave structures surfaced this investigation.)

---

## §D. Methodology-rule extensions (M1-M4 + allowlist)

(none — the only audit-tooling change this run, the python-validate hook investigation-naming fix, was EFFECTED in-session → recorded in §A1, not deferred as a §D rule-extension.)

---

## §E. Pre-compute shell waves (upstream escalation; NOT a CF)

(none — all 4 Wave-1 gates executed and closed: INV2-W1-1/2/3 emitted verdict lines to `computations/investigation-2/inv2_gate_verdicts.txt`; INV2-W1-4 closed by artifact-existence on its workshop md.)

---

## §F. Structural counts (artifact shape; not length)

| Category | Count |
|:---------|------:|
| §A In-session resolutions | 4 |
| §B Session-promotion register items (ROUTED; investigation track-local) | 5 |
| §C Q3 parallel-wave CFs | 0 |
| §D Methodology rule extensions | 0 |
| §E Pre-compute shell waves | 0 |
| **Total Q2-class items surfaced** | 9 |

Separately (NOT Q2; NOT in this ledger): **4 MATH carry-forwards** (CF-INV2-W1-1-C2COSET, CF-INV2-W1-3-DYNSOLITON, CF-INV2-W1-4-M1, CF-INV2-W1-4-TYPEBRIDGE) live in the WP `## Carry-Forward Computations` section — genuine future computation, propagated via `/rclab-investigate --investigation 2`.

---

## Consumption pointers

- **`/rclab-investigate --investigation 2`**: read this file BEFORE producing candidates. Every §A/§B entry is structurally a non-workshop (Q2). The genuine workshop of this investigation (INV2-W1-4) is already CLOSED with its verdict landed — it is NOT a candidate. The 4 MATH carry-forwards (WP CF section) are compute carry-forwards, NOT workshops.
- **Session promotion (when Investigation-2 results are lifted into a session via `/rclab-plan`)**: apply §B1–B5 register edits via the appropriate designated writers; **run the capstone-hygiene 5-question gate** for the atlas-04 (D04, capstone-governing) edits B1/B4 and the atlas-08 edits B2/B5 (status-scope changes); the math CFs become pre-registered session gates.
- **`/rclab-coordinate`**: §E empty — no shell-wave re-dispatch needed.

---

*End of Investigation 2 housekeeping ledger.*
