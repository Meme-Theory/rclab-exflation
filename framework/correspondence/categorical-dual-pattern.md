# CategoricalDual Authoring/Enumeration Ordering Pattern

**Status**: READY-TO-INSTALL → INSTALLED 2026-04-27 (S86 Level-10 housekeeping T10-41).
**Source**: S86 W-13 workshop `_housekeeping-extract-w13.md` FW-2 (line 202) + workshop §lines 2080-2113 + Verdict row 13 (line 2140) + line 2175 (M_meta-instance #1 framing).
**Recommending agent**: gen-physicist (extract); connes + lizzi (workshop sponsors).
**Cross-references**: `sessions/framework/registry/permanence-map.md` (T10-40 install; FW-1 parent registry; this file is sub-row of FW-1 OR companion file per FW-2 line 202).

This entry is the standalone pattern for the CategoricalDual authoring/enumeration ordering — the dual ordering convention where Author_seq (the order in which the workshop writes deliverables) follows the Phi-image order (structural weight, load-bearing first), while Enum_order (the order in which deliverables appear in the workshop's pre-registered header) follows traceability.

---

## §1 — Pattern statement

**CategoricalDual Authoring/Enumeration Ordering Pattern** (FW-2 line 202):

```
Author_seq follows Phi-image order (structural weight, load-bearing first).
Enum_order follows pre-registered header order (traceability).

Future multi-deliverable workshops adopt the dual ordering.
M_meta-instance #1 at N_instances = 1.
```

The pattern decouples the WORKSHOP'S INTERNAL AUTHORING ORDER (driven by structural weight; load-bearing deliverables authored first to establish anchors for downstream dependent deliverables) from the WORKSHOP'S EXTERNAL ENUMERATION ORDER (driven by pre-registered header sequence; ensures traceability to the spawn prompt's task list).

---

## §2 — Phi correspondence (graded ring isomorphism)

The Phi correspondence (CANON-4 of W-13 housekeeping extract; workshop §lines 2027-2034 C3-CONN-EM-1) is the structural mapping that defines the Phi-image order:

**Phi-correspondence statement**: Phi sends weight-`n` object to weight-`n` object; canonical grading at substrate (mass-dimension of curvature scalar) ↔ methodology (enforcement-strength).

```
Phi : Substrate × Methodology → Substrate × Methodology
Phi(weight_n object) = weight_n object   (graded-ring-isomorphism preserving)

Substrate grading:    n = mass-dimension of curvature scalar
Methodology grading:  n = enforcement-strength of methodology rule
```

The Phi-image order at substrate side (mass-dimension descending: `R^4 → R^2 → R → 1`) corresponds at methodology side to enforcement-strength descending (`hook-enforced → rule-file → memorized-norm → suggestion`).

**Author_seq follows Phi-image order**: load-bearing methodology deliverables (highest enforcement-strength, e.g., hook-enforced rules) are authored FIRST, providing anchor points for downstream lower-enforcement deliverables (rule-file rules, memorized norms, suggestions).

---

## §3 — Why the dual ordering

The dual ordering emerges naturally from two structurally orthogonal requirements:

### Author_seq requirement (Phi-image order)

When a workshop produces multiple deliverables, the deliverables form a DEPENDENCY DAG:

```
Definition 1: deliverable D_i has structural weight w_i = Phi-image grade
Definition 2: D_i depends on D_j iff D_j is load-bearing for D_i (e.g.,
             D_j defines a structural anchor cited by D_i)
Definition 3: dependency DAG = (deliverables, dependency edges)

Step 1 (sub):  authoring D_i before D_j when D_i has higher Phi-image grade
              (load-bearing first) eliminates forward-references in the
              authoring chain — every deliverable cites only previously-authored
              anchors.
Step 2 (sub):  authoring in REVERSE order (lower-weight first) creates
              forward-references; downstream-edits when load-bearing anchors
              are eventually authored cause re-write churn.
Direction:    Author_seq follows Phi-image order MINIMIZES authoring chain
              forward-references.
```

### Enum_order requirement (pre-registered header order)

When the workshop's spawn prompt pre-registers the deliverable list as a numbered header sequence, the Enum_order (the order in which deliverables appear in workshop output) MUST follow the spawn-prompt sequence to maintain TRACEABILITY:

```
Definition 4: Enum_order = order deliverables appear in workshop output
Definition 5: spawn_prompt_seq = order deliverables enumerated in spawn prompt

Step 1 (sub):  Enum_order ≠ spawn_prompt_seq breaks traceability — auditor
              cannot align workshop output deliverables with spawn-prompt
              task numbers.
Step 2 (sub):  Enum_order = spawn_prompt_seq preserves traceability.
Direction:    Enum_order follows pre-registered header order PRESERVES
              spawn-prompt-to-output traceability.
```

### The dual ordering reconciles both requirements

When `Phi-image_order ≠ spawn_prompt_seq`, a single ordering choice violates ONE of the two requirements. The CategoricalDual pattern resolves this by:

```
Author_seq = Phi-image order  (load-bearing first; for chain-build efficiency)
Enum_order = spawn_prompt_seq  (traceability; for audit-trail integrity)
```

The two orderings are STRUCTURALLY DUAL — both must be tracked, both must be honored, but they need not coincide.

---

## §4 — S86 W-13 calibration corpus (M_meta-instance #1)

The S86 W-13 workshop is M_meta-instance #1 of the CategoricalDual pattern at `N_instances = 1`. The workshop produced six structural emergences (per `permanence-map.md` T10-40 §2):

| Author_seq position | Emergence | Phi-image grade | Enum_order position |
|:---------------------|:-----------|:------------------|:----------------------|
| 1st (load-bearing) | (1) Read-Edit commutator (Theorem 1; Layer_A) | high (axiomatic) | 1 |
| 2nd | (4) 2D Scope × Layer permanence map (Layer_C; M_meta candidate) | high (categorical, methodology-meta) | 4 |
| 3rd | (2) Basis-completeness theorem (Theorem 2; Layer_C) | medium (categorical) | 2 |
| 4th | (3) Layer-functor F (Theorem 3; Layer_C) | medium (categorical) | 3 |
| 5th | (5) Prompt-encoded-vs-memorized (Layer_I) | medium (inductive, methodology-rule) | 5 |
| 6th | (6) M_meta meta-rule (Layer_I) | medium (inductive, meta-rule) | 6 |

**Author_seq** in the workshop output: 1, 4, 2, 3, 5, 6 (load-bearing emergences #1 and #4 authored first to establish axiomatic + meta-categorical anchors).

**Enum_order** in the workshop output: 1, 2, 3, 4, 5, 6 (verbatim spawn-prompt sequence).

The two orderings differ: position #4 (2D map) is authored 2nd but enumerated 4th. The workshop output traces both orderings explicitly to maintain audit-trail integrity.

---

## §5 — M_meta promotion path

**M_meta-instance #1 at `N_instances = 1`**: S86 W-13 workshop. The pattern is authored as an OBSERVATION-ONLY registry row (FW-2 line 202; READY-TO-INSTALL).

**Promotion criterion** (per workshop COMPUTE-CF-9 informal carry-forward, line 258):

> Track future multi-deliverable workshops for adoption of Phi-image authoring + header enumeration order; promote to rule-file at K=3 distinct invocations per M_meta criterion.

The promotion path (per `permanence-map.md` T10-40 §5 M_meta criterion):

1. **N_instances = 1** at S86 close (W-13 workshop is M_meta-instance #1).
2. **N_instances = 2** target at S87+ workshop adoption (next multi-deliverable workshop applying the CategoricalDual ordering).
3. **N_instances = 3 = K_meta** triggers M_meta promotion to Scope_S; CategoricalDual pattern registered as a rule-file across `.claude/rules/`.
4. **N_instances ≥ 4 + Scope_S corroboration** triggers M_meta promotion to Scope_C; canonical knowledge.db registration.

---

## §6 — Instrumentation for tracking (S87+ planner)

Per workshop COMPUTE-CF-9 (informal carry-forward), the S87 planner instruments tracking of the CategoricalDual pattern adoption:

```
For each S87+ multi-deliverable workshop:
  1. Identify Author_seq (order workshop output sections appear in the file)
  2. Identify Enum_order (order workshop section headers were pre-registered in spawn prompt)
  3. Identify Phi-image grading of each deliverable (substrate Phi-image)
  4. Verify Author_seq follows Phi-image order
  5. Verify Enum_order follows spawn_prompt_seq
  6. If both verified: increment N_instances counter for CategoricalDual pattern
  7. Log invocation with workshop ID + emergence-list

Promotion trigger: N_instances >= 3 → promote to rule-file
```

The tracking activity is observation-only at S86 close; no separate compute-cf is allocated. The tracking rides with `S87-WAVE-CLASSIFICATION-RULE-VALIDATION` (CF-72) as a sub-observation.

---

## §7 — Cross-references

- **Parent registry**: `sessions/framework/registry/permanence-map.md` (T10-40 install; FW-1; the CategoricalDual pattern is M_meta-instance #1 candidate within the 2D map's `Scope_W × Layer_C` cell #4).
- **Phi correspondence (CANON-4)**: knowledge.db registration deferred (W-13 workshop §lines 2027-2034 C3-CONN-EM-1); workshop-only at `N_instances = 1`; Scope_W candidate currently; promotion to Scope_S via M_meta K=3 path.
- **Read-Edit commutator (CANON-2)**: knowledge.db registration deferred to S87+ NCG-Axiom-5 cross-reference verification; the load-bearing emergence #1 in W-13 workshop's Author_seq.
- **Layer-functor F (CANON-3)**: knowledge.db registration deferred to `S87-LAYER-FUNCTOR-AUDIT-LEG-VERIFICATION` (CF-76) PASS; pair-verified status with audit-leg empirical corroboration pending; emergence #3 in Enum_order, #4 in Author_seq.
- **`S87-WAVE-CLASSIFICATION-RULE-VALIDATION`** (CF-72): empirical validation of M1-M4 conjunction on S87 first 5-wave methodology corpus; rides with CategoricalDual pattern adoption tracking.
- **CategoricalDual pattern propagation tracking** (COMPUTE-CF-9 informal): observation-only tracking; promote to rule-file at K=3 distinct invocations per M_meta criterion.
- **HIGH-DENSITY WORKSHOP TEMPLATE** (S86 W-12 RULE-W12-2): related multi-layer output-slot decomposition methodology for high-density workshops; specifies workshop verdict should NOT force a single PASS/FAIL/INFO at literal pre-reg, but rather decompose into INDEPENDENT OUTPUT slots with own promotion paths. CategoricalDual is the AUTHORING/ENUMERATION layer of the HIGH-DENSITY methodology.

---

## §8 — Closing

The CategoricalDual authoring/enumeration ordering pattern is the structural pattern under which Author_seq (workshop's internal authoring chain) follows Phi-image order (load-bearing first), while Enum_order (workshop's external enumeration in output) follows pre-registered header sequence (traceability). The two orderings are STRUCTURALLY DUAL — both must be tracked, both must be honored, and they need NOT coincide. The pattern is M_meta-instance #1 at S86 W-13 (`N_instances = 1`); promotion to rule-file requires K=3 distinct invocations per M_meta criterion. The S87 planner instruments tracking via `S87-WAVE-CLASSIFICATION-RULE-VALIDATION` (CF-72) as a sub-observation; no separate compute-cf is allocated.
