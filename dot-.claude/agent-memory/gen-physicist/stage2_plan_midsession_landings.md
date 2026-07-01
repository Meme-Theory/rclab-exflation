---
name: stage2-plan-midsession-landings
description: Planning a Stage-2 verify wave whose Stage-1 entries land MID-SESSION (same-session W6 -> W7 edge) — boundary-check static leg, runtime slot resolution, AMRI trap, orthogonality two-branch
metadata:
  type: feedback
---

Rule: when authoring a Stage-2 verify wave whose Stage-1 registry entries land in an EARLIER wave of the SAME session (vs the S100a-plan-w6 precedent where entries pre-existed), four adaptations are mandatory:

1. **Static `--check-reviewers --strict` leg is NOT pre-clearable at plan-freeze** (the §VII slot doesn't exist yet; invocation returns `INFO_SLOT_NOT_FOUND`). Pin it as a MANDATORY W(N)→W(N+1) boundary check run by the dispatching orchestrator AFTER the landing, BEFORE reviewer dispatch. At plan-freeze, run `--self-test` (proves liveness) + the pre-landing demo (documents expected INFO behavior) and record both in the prerequisites section.
2. **Slot letters are runtime-resolved**: a multi-landing wave (6 entries, next-free-letter scan) makes "≥ §VII.BM" indicative only. Producing scripts parse the ACTUAL slot from the landing gate's verdict-line `value=` field (fallback: registry header grep on the suffix/title); drift documented per `substrate-first-canonical-sourcing.md §(ii.B)`.
3. **AMRI trap on inheritance evidence**: an agent-memory file cited as the downstream-inheritance-reach WITNESS (e.g. berry `s100b-band-selective-rigidity.md`) goes in the machinery_pin_map exclusion clause as a grep TARGET with an explicit "NOT an Input-SHA pin" note — listing it in `input_files` fires AMRI Test 1.
4. **Orthogonality clause has two legitimate branches; declare which**: axis-partitioned design (text-only Axis-A / npz-only Axis-B) → predicate SATISFIED-by-construction, no caveat; binding-text dual-verification (both reviewers load the same npz for the witness clause) → predicate FAILS BY DESIGN → pre-register the explicit `OVERLAP-CAVEAT` tag in verdict value + WP per `joint-theorem-promotion.md`. Do NOT re-engineer the binding spec to force branch 1.

**Why**: S101-plan-w7 (2026-06-07) hit all four; the binding-text rule forbids re-deriving thresholds, so the overlap-caveat branch is the honest treatment, not a defect. Witness re-check tolerances split VALUE-class (Class-8.3 rel_tol ≥ 10^(−published s.f.)) vs FLOOR-class (bound re-verification — floor digits are BLAS-order-sensitive; the registered criterion IS the bound).

**How to apply**: any future same-session Stage-1→Stage-2 chain (queued: S102 H-parity Stage-2 after the odd-floor gate; S102 Route-D Stage-2). Validator note: `_yaml_gate_validator.py` takes positional file args (no `--plan` flag).

Related: [[stage2-pass-and-aggregation-closeout]] (the closeout side of the same pipeline).
