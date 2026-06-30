---
name: reviewed-annotation-frozen-immune-entry
description: Reviewed designated-writer SCOPE annotation on an EXISTING §VII entry whose frozen Stage-0 blockquote is byte-SHA-IMMUNE — annotation surfaces ONLY, frozen span located by literal anchor and HARD-asserted UNCHANGED, idempotent NO-OP re-run, distinct from a verbatim Stage-0 LANDING.
metadata:
  type: feedback
---

Applying a reviewed designated-writer ANNOTATION (scope-narrowing / out-of-frozen-block amendment) to an ALREADY-LANDED §VII registry entry — NOT a registry-landing (no new slot, no Stage-0 candidate consume). Distinct from [[verbatim_extraction_registry_landing]] (which lands a NEW frozen Stage-0 candidate). S103 W1-6 §VII.BS clause-(b) scope annotation (S-1 connes synthesis §IV.D verbatim).

**Why:** the frozen Stage-0 blockquote (theorem-tag span) is byte-SHA-pinned (W1-1 landing PASSed on byte-faithfulness). An annotation NEVER edits it — it lands on the OTHER register surfaces (header parenthetical / index-row parenthetical / clause-inline / a NEW out-of-frozen-block block, modeled on the §VII.BP BINDING AMENDMENT precedent). A frozen-span SHA mismatch is the MOST SERIOUS FAIL.

**How to apply:**

1. **Recover the FULL 64-char frozen-span SHA at a pre-flight probe.** The plan + registry store the head form (`e669ccd2…`). The span is the ENTIRE blockquote LINE *including* the `> ` marker (len 2514 for §VII.BS); stripping `> ` gives a DIFFERENT SHA. Locate by literal substring `> **<title>**` → end-of-line; confirm `hashlib.sha256(span).hexdigest() == pin`. This is the immutability anchor (PRE==POST==pin).

2. **Annotation surfaces ONLY; anchor each on FULL distinguishing context.** The bare parenthetical (`(N₃=0 corollary, rank-1)`) recurs in header AND the frozen blockquote — match header/index on their full prefixes (`### §VII.X — …`, `| §VII.X | THM | …`) so `txt.replace(old,new,1)` cannot touch the immune blockquote. Assert each OLD anchor count == 1 before replacing. The clause-inline surface is the clause-attribution TABLE row (a transcribed annotation surface), NOT the frozen blockquote's clause text.

3. **Insert the out-of-frozen-block block AFTER the clause-attribution table** (after the last clause row), on the line after its `\n`. Verbatim from the synthesis §IV.D recommendation text; wrapper-header adapted to the §VII.BP BINDING-AMENDMENT form ("authoritative grade for downstream consumers"). Optional dated cross-reference (e.g. a same-session W2-1 PASS that upgrades a standing premise → result) per the plan's coupling note — append, do NOT restructure; the upgrade itself is the next-session follow-up.

4. **Idempotency = detect-already-annotated, NO-OP write.** On re-run the OLD anchors are gone (replaced by NEW). `already_annotated = (HEADER_NEW in pre) and (HEADER_OLD not in pre)` → SKIP write, verify against on-disk state. The line-drift probe must anchor on `HEADER_OLD if present else HEADER_NEW`. Plan-cited line will have drifted (registry gains rows mid-session); anchor by substring, disclose `line_drift` per substrate-first §(ii.B).

5. **must_contain literal `print_verdict_payload`.** The plan's script must_contain wants the CANONICAL helper NAME, not an open-coded `<<<EMIT_VERDICT_PAYLOAD>>>` print. Define `def print_verdict_payload(payload): print("<<<EMIT_VERDICT_PAYLOAD>>>"+json+"<<<END…>>>"); return payload` (template line 226 contract) and CALL it. If you miss this on run-1, it is a script-COMPLIANCE defect (not a physics FAIL): refactor, re-run (idempotent NO-OP), emit a CORRECTIVE line with `supersedes=<old 64-hex audit>` (Option A; verdict permanence) — the SOLE change is content_sha (script bytes), verdict/value/booleans identical; disclose in the companion_note + WP.

6. **Verdict predicate (all RE-READ from disk):** `verify = frozen_unchanged(==pin, HARD) ∧ four_surfaces ∧ second-finding-present ∧ grade_unchanged(STAGE-3-PERMANENT count preserved) ∧ narrowed-wording-markers ∧ blockquote_count_preserved`. The annotation SCOPES wording (necessity vs sufficiency) — it does NOT down-tag the theorem (Q3 capstone-hygiene = NO). audit_sha inputs = [script, s1_ivd_text_sha, registry_pre_file_sha, frozen_span_sha_assertion, pinmap]; content_sha = script SHA.
