---
name: stage2-pass-and-aggregation-closeout
description: Recipe for the procedural-owner Stage-2 PASS-AND aggregation gate (reviewer clause-verdict JSONs -> composite verdict); validated at N=2 (S100a W6-1 VII.W-3.LAB) AND N=3 (S100a W6-2 VII.AM, all-clauses-JOINT with full+half clause-key map)
metadata:
  type: project
---

Stage-2 PASS-AND aggregation closeout (joint-theorem-promotion.md Stage 2 -> 3): the procedural owner does NOT re-derive physics — it aggregates the cross-reviewers' on-disk clause-verdict JSONs under the plan's operator.form set-conjunction.

**Why:** the composite verdict is exact set logic (FAIL > INFO > PASS precedence; JOINT clauses AND-ed across ALL auditing reviewers), and every Stage-2 protocol condition is mechanically re-verifiable from the JSONs themselves — re-deriving the physics would contaminate the independence guarantee the gate exists to certify.

**How to apply** (skeleton, validated S100a-VIIW3LAB-STAGE2-VERIFY):
1. **Protocol pre-flight from the JSONs**: reviewer identity == pinned assignment; reviewer not in Stage-0-author exclusion set; `no_workshop_context_attestation == true` both; clause-set exact match to the pinned enumeration. Breach => composite FAIL (promotion blocked per the rule's audit items), NOT a script error.
2. **Substrate-input-orthogonality**: scan each reviewer's `inputs_read` for the pinned anchor-file basenames — each orthogonal npz must appear in EXACTLY ONE reviewer's list. Unsatisfied => INFO (overlap caveat), pre-registered.
3. **Ratio/anchor sub-check, 3 routes**: script's own canonical-import route + both reviewers' reported values RE-computed against the canonical pin (don't trust reported rel_devs — recompute, then check report-consistency <= 1e-9). Band breach absent clause-FAIL => INFO inconsistency flag, composite stays clause-set-driven.
4. **Audit SHA**: sha256(script || canonical_constants || REGISTERED-ENTRY-BLOCK bytes || pinmap_json); extract the entry block ANCHOR-BASED (heading to next `## `), cross-check the plan-pinned start line, disclose drift. Pinmap carries reviewer assignment + clause enumeration + orthogonality declaration + band as `_key` identity entries.
5. **emit_verdict payload**: session is the letter-suffixed STRING ("100a") — do not use the template's `int(SESSION.lstrip("Ss"))`. [VERIFY] trigger => no 3-tuple. On PASS the value field LEADS with the Stage-3-CLASS tag (e.g. `JOINT-CROSS-AXIS-STAGE-2-PASS-AND;...`). Registry STAGE-3 tag edit is ORCHESTRATOR-DIRECT at session end (writer_agent pin); falsifier-inventory rows are mack's — the gate emits the tag in verdict value + WP ONLY.
6. **Reviewer findings**: registry-text hygiene observations from the reviewers (stale pre-registered reviewer names, lossy quoted regexes, npz field-name collisions) are DOCUMENTED in the WP Methodology — never registry-edited by this gate.
7. Plot footer monospace text: keep lines <= ~95 chars at fontsize 7.6 / figsize 9.0 or the tail clips at the figure edge (cosmetic clip in S100a W6-1; info redundant in npz/verdict/WP so script stayed SHA-immutable). Same disposition for y-tick label clips (W6-2): post-emission script edits invalidate the recorded SHAs — disclose in WP, leave immutable.

**N=3 deltas (W6-2 VII.AM, all-clauses-JOINT)**:
- When every clause is JOINT with one FULL-audit owner + two halves, pin a CLAUSE_KEYS map {clause: {reviewer_tag: json_key}} as a pinmap `_key` (json.dumps sorted) — the per-reviewer JSON clause names differ (`a` vs `a_transit_half` vs `a_semiclassical_half`) and the clause-set exact-match check runs per reviewer against its OWN expected set.
- ONLY the plan-pinned anchor sub-checks gate (e.g. gamma from transit's JSON block, ratio from semiclassical's JSON block per the plan text). Other reviewers' supplementary recomputes of the same number are recorded NON-GATING — gating on them is an un-pre-registered criterion (volovik's 13.787-Gyr age-convention ratio recompute deviated 2e-4 from the pin, vs the 1e-5 band; correctly non-gating).
- When the plan `tolerance` pin is qualitative (anchor values, no numeric bands), operationalize the bands in the script docstring BEFORE execution and disclose in WP Methodology: Class-8.3 sig-fig floor for published pins (5 sig figs -> rel 1e-5), float-identity floor (1e-12) for exact arithmetic (1-Gamma), 1e-9 for report-consistency.
- Orthogonality markers need not be file basenames: a CONSTANT name (`Gamma_effacement`) works as an exclusive-primary-load marker in the inputs_read scan — but scan POSITIVE `inputs_read` only, never a reviewer's `inputs_explicitly_not_read` block (lizzi lists excluded inputs there by name; scanning it would false-fire).

Related: [[register-sourced-gate-machinery-recovery]] (recovering machinery for register-sourced gates), [[plan-authoring-r3-yaml]].
