---
name: pipeline-status-aware-registry-audit
description: Design pattern for extending a registry-completeness audit to be status-aware (pending vs defective) without false-FAILing legitimately-pending entries; header-scoped status read + PASS-first precedence + self-non-bridge/superseded rescue.
metadata:
  type: feedback
---

When extending a registry-completeness audit (e.g. `_cross_pillar_bridge_audit.py`) from blanket PASS/FAIL to a status-aware verdict (PASS / PASS-WITH-N-PENDING / FAIL), four design rules avoid mis-classification.

**Why:** The S94 W6-17 `S94-CPB-AUDIT-PENDING-VS-DEFECTIVE` gate. The audit had blanket-FAILed the §VII registry because 12/35 sections were non-PASS — but most were STAGE-0/1-CANDIDATE / deferred-pending (substrate-IS-LEGITIMATE per the Level-3 annotation discipline: Level-1 holds while Level-2/3 empirical realization is pending). A blanket-FAIL is the audit-floor F-image of a methodology veto over a substrate-IS structural PASS (forbidden). Only 4 of the 12 were genuinely-defective (anatomy/OE-form gap on a `settled` entry).

**How to apply:**

1. **Read a section's status from the HEADER line + the FIRST `**Status**:` body line ONLY — never a whole-body substring scan.** Cross-reference prose deep in a section body routinely names `STAGE-3-PERMANENT per joint-theorem-promotion.md` / `STAGE-1-CANDIDATE` about OTHER slots. A whole-body scan made every section look like it carried every status tag. Scope the status read via a `_status_scope_text()` helper (header + through the first `**Status**:` line, capped at ~30 lines).

2. **Check literal-PASS FIRST in the classification precedence.** A section that passes the full literal audit (3/3 tier, 5/5 anatomy, OE-form) is unambiguously complete; record it as PASS regardless of any "NOT a cross-pillar bridge" prose it carries. A precedence bug (self-non-bridge checked before PASS) demoted a genuine literal-PASS (§VII.AQ.STATE-PROJ) — the self-non-bridge skip is a RESCUE for false-FAILs only, never a demotion of genuine PASSes. Order: PASS → self-non-bridge → superseded → pending → inherits-completion → genuinely-defective.

3. **Two scoping-rescue classes beyond the literal trichotomy, both surfaced by live data (not the plan):** (a) **self-non-bridge** — an intra-pillar identity that self-declares `Element 2: N/A — Pillar-N-internal` / `NOT a cross-pillar bridge` gets caught by a `"laboratory-in observable"` substring guard in the NEGATING context; SKIP it (extend the existing non-bridge guard with the negating-context regex). (b) **superseded** — an Option-A `supersedes`-tagged successor is EXCLUDED from defect-scoring (canonical reading = latest non-superseded line per `gate-verdicts.md §"Option A"`).

4. **Parent/sub-section anatomy inheritance:** a `§VII.X.SUFFIX` sub-section parses its parent by dropping ONE trailing dotted segment; grant inheritance ONLY from a parent that itself literal-PASSes (an incomplete sub-section cannot inherit completion from an equally-incomplete parent). Verify the resolver fires in the self-test on a known OP-PROJ inheritor.

**Verdict discipline on a live un-retrofitted registry:** the gate verdict TRACKS live registry state (FAIL while genuinely_defective > 0, defective set NAMED + routed to the sole registry writer), and the self-test proves the classifier emits PASS-WITH-N-PENDING with genuinely_defective == 0 AFTER a synthetic retrofit fixture. Do NOT self-loosen to PASS — FAIL is the honest pre-registered `FAIL_meaning` outcome. Partition-completeness SUM check (n_pass + pending + defective + self-non-bridge + superseded == n_sections) is a cheap, decisive correctness gate.

Related: [[plan-authoring-r3-yaml]].
