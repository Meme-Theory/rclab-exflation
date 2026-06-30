# Capstone-Hygiene Gate (standing 5-question status-synchronization discipline)

This rule is a **DIRECTIVE document**. It carries the standing checklist and routing directives only. Calibration corpus, per-instance drift records, K-counter advancement events, dated promotion histories, and session-event provenance belong in `sessions/framework/registry/capstone-hygiene-corpus.md`, NOT here (`feedback_rules-directive-only-no-session-info.md`). Bare enforcement-status ("SUGGESTION, K=1") is permitted; per-instance narrative is not.

## Scope

The living capstone `sessions/framework/phonic-exflation-equation.md` is a CURATED framework document whose narrative confidence on every status-bearing claim MUST equal that claim's status in the repo-wide register (Atlas D04 assumptions `sessions/framework/Atlas/atlas-04-assumptions.md`, the Atlas D09 retraction log `sessions/framework/Atlas/atlas-09-retractions.md`, `sessions/permanent-results-registry.md`, and the knowledge MCP). The recurring failure mode this rule closes BY CONSTRUCTION: a capstone section narrates a claim at a confidence the register marks **BROKEN / CONDITIONAL / RETRACTED / INFO** — version-synchronization drifting from a cosmetic issue into a substantive scholarly one.

The rule applies to any session whose wave-synthesis touches EITHER the capstone OR a capstone-governing register (Atlas D04, the retraction log, the permanent-results registry, the `§7` falsifier-anchor surface, or `canonical_constants.py` values the capstone cites).

## Rule

Any session whose wave-synthesis answers **YES** to any of the five questions below MUST run the capstone-hygiene gate before the session closes: the YES answer routes a capstone-update action into that session's housekeeping ledger (`sessions/session-{N}/session-{N}-housekeeping.md`) §A (in-session designated-writer fix) or §B (compute carry-forward), per `.claude/templates/session-housekeeping.md`.

A session that touches a capstone-governing register WITHOUT running the 5-question gate is a process-discipline FAIL detectable at the next session's plan-freeze (audit hook below).

## The 5-question checklist (pre-registered process discipline)

Run at session-close, one question at a time. Each YES carries a mandatory routing action.

- **Q1 — a(t) / effective-Friedmann gap.** Does this session's work alter the §6.3 `a(t)` / effective-Friedmann (substrate→FRW) gap status? If YES → update capstone §6.3 + reconcile Atlas D04 C1/C2 (the assumed-vs-broken effective-Friedmann pathway tags).

- **Q2 — §7 falsifier-anchor row.** Does this session's work alter a capstone §7 falsifier-anchor row (an observable value, a σ-distance, a detector horizon, or a status tag)? If YES → the §7 falsifier/observable surface is the `mack-cosmic-bridge` sole-writer's domain (`feedback_mack-bridge-role.md`): route the §7.1/§7.2 update + the `sessions/framework/registry/falsifier-master-inventory.md` row to `mack-cosmic-bridge`.

- **Q3 — PROVEN / CONDITIONAL / BROKEN / INFO status change.** Does this session's work change the PROVEN / CONDITIONAL / BROKEN / INFO status of any capstone claim? If YES → reconcile the capstone PROSE status tag AGAINST Atlas D04 + the retraction log (the prose tag MUST equal the register tag; no section narrates a claim above its register status).

- **Q4 — PROSE claim vs ledger row.** Is the change to a PROSE claim, not merely a ledger / registry row? If YES → the curated-doc designated-writer patch discipline applies (a reviewed patch, NOT a bulk install-agents append, per `feedback_framework-hygiene.md`). Prose changes land via the designated writer; ledger-only changes append to the register without touching the curated prose.

- **Q5 — citation add / invalidate.** Does this session's work add or invalidate a citation in the capstone? If YES → update the relevant §-citation anchor per the capstone's primary-literature citation-anchoring discipline (each numerical/structural claim carries an explicit anchor; an invalidated source is retracted, not silently left in place).

## Routing directive (housekeeping ledger)

A YES on any Qi routes the capstone-update action by lifecycle, per `.claude/templates/session-housekeeping.md`:

- **In-session designated-writer fix** (a prose down-tag, a §7 status-cell update, a citation-anchor repair effected this session) → housekeeping ledger **§A** (record of the completed fix). Per `feedback_fix-in-session-never-defer.md`, a status-tag edit on an already-derived claim is fixed in-session, not deferred.
- **Compute carry-forward** (the reconciliation requires a substrate-physics compute that an orchestrator-direct edit cannot perform — e.g. a Stage-2 cross-axis verify, a numerical re-run feeding the reconciled value) → housekeeping ledger **§B** with a 4-field spec, MIRRORED to the originating wave's WP `## Carry-Forward Computations` block.
- **Genuinely-unreconciled math/physics tension** (a dissonance whose resolution is a math/physics adjudication, Q1-YES per `.claude/rules/Investigating-Workshops.md`) → the capstone carries an explicit `STATUS: unreconciled — see <forward gate>` pointer on the affected cross-reference; the dissonance is forward-routed as a compute item, NOT silently down-tagged.

The designated writer is the capstone's prose owner for §-prose reconciliation; the §7 falsifier-TABLE status cells are `mack-cosmic-bridge` (sole writer per `feedback_mack-bridge-role.md`). The gate produces the reconciliation; the writer applies it as a reviewed patch — never a bulk append.

## Substrate-first framing preservation (load-bearing)

A status down-tag NEVER inverts an explanation direction. Reconciliation lowers over-confident wording to its register status while preserving the substrate-IS frame (`phononic-framing.md`): the substrate IS the observable; the register tag scopes the confidence; the arrow `D_K eigenvalues → spectral moments → emergent physics → measurement` is unchanged. Q3 keys on the substrate-physics status ladder (PROVEN/CONDITIONAL/BROKEN/INFO); Q4 distinguishes a PROSE claim (curated-doc discipline) from a ledger row (registry append). The rule institutionalizes F-consistency (capstone prose tag == register tag) every session — the methodology-floor analog of a substrate-IS conserved quantity (no capstone claim exceeds its register status), per `epistemic-discipline.md §"Layer-Decomposition"`.

## Audit

`computations/_shared/_capstone_hygiene_gate_audit.py` greps a session's working-paper / housekeeping-ledger text for the 5-question checklist block (regex on the Q1–Q5 markers + the routing-to-housekeeping marker). When a capstone-touching session lacks the block, the detector emits **S2 advisory** (under SUGGESTION status) / **S1 MANDATORY** (after K=3 promotion). The detector ships with a `--self-test` covering a synthetic POSITIVE case (a WP carrying the Q1–Q5 block → no flag) and a synthetic NEGATIVE case (a capstone-touching WP lacking the block → flag fires).

## Status

**MANDATORY at K=3.** Promoted from SUGGESTION (K=2) on the third distinct catching-session per `feedback_rules-compensate-missing-structure.md` — the K-counter advances by one on each distinct session that runs the gate and catches a real capstone-status drift (an over-confident-narration or version-synchronization reconciliation, not a no-op pass). The audit hook now emits **S1 HARD-HALT** at the next capstone-touching session's plan-freeze (a capstone-touching session that omits the 5-question block blocks, no longer merely warns). K-counter advancement records + the per-drift calibration corpus live at `sessions/framework/registry/capstone-hygiene-corpus.md` (append-only, forward-only per `feedback_rules-compensate-missing-structure.md`).

## Cross-references

- `.claude/templates/session-housekeeping.md` — the §A/§B routing target for every YES answer (canonical Q2 ledger).
- `sessions/framework/phonic-exflation-equation.md §0` — the prefatory note cross-links this gate as the standing hygiene discipline.
- `feedback_framework-hygiene.md` — curated-doc discipline (no bulk dumps; designated-writer reviewed patch).
- `feedback_mack-bridge-role.md` — `mack-cosmic-bridge` is the sole writer of the §7 falsifier/observable surface + `falsifier-master-inventory.md`.
- `phononic-framing.md` — substrate-first / IS-not-IN framing the reconciliation preserves.
- `epistemic-discipline.md §"Layer-Decomposition"` — the layer-functor F (capstone prose tag is the methodology-floor F-image of the substrate-physics register status).
- `.claude/rules/Investigating-Workshops.md §"Q1/Q2"` — a genuinely-unreconciled tension is a Q1 workshop, not a Q2 down-tag.
- `feedback_rules-compensate-missing-structure.md` — the SUGGESTION-K=1 → MANDATORY-K=3 promotion contract.
- `feedback_rules-directive-only-no-session-info.md` — this rule body carries directives only; corpus → `sessions/framework/registry/capstone-hygiene-corpus.md`.
