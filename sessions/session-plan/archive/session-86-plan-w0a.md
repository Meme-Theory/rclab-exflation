# Session 86 Plan — Wave W0a: Methodology rule-file landing — core rule-file v3 union

**Generated**: 2026-04-25
**Owner**: gen-physicist (planner) — runtime gates routed to per-item specialists below
**Output destination (verdict file)**: `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`)
**Item count**: 5 (R1, R2, R3, R5, R6 — verbatim from `session-86-partition.md` §1 Wave W0a)

---

## §0. Wave W0a Summary

Wave W0a is the first of three W0 sub-waves (W0a / W0b / W0c). Per the `--extra` "smaller chunks" instruction (agent-death-when-overwhelmed observation in S85 closeout §6.1), the original closeout-proposed monolithic W0 (16+ items) is partitioned into three thematically-cohesive sub-waves: W0a = core rule-file v3 union (5 items), W0b = methodology entries + audit infrastructure (5 items), W0c = canonical-constants consolidation + bulletins (9 items). W0a's specific scope is the FULL S85 v3 union of W-3 v2 (11 plan-layer methodology debt clauses) + 5A v2 (3 sub-diffs / 7 NEW debt classes) per context §2.5 + closeout §3.5 + §6.5; together these produce the consolidated v3 rule-file landing PLUS three discrete planner-template fixes (cutoff_axis YAML, PRDR-K disambiguation, plan-gen discipline) that close pre-registration vulnerabilities at the planner level rather than at script-rerun level.

**Scope (5 items)**: R1 monolithic v3 rule-file consolidation (MODERATE 3-4h); R2 `_source_reconciliation_audit.py` infrastructure with 13-site retrospective fixture and 5-class taxonomy (0.5 wave); R3 cutoff_axis YAML schema field (30 min); R5 8-key PRDR-K disambiguation in classifier vocabulary (0.3 wave); R6 `/rclab-plan` skill update for canonical-path verdict-state reading (1-2h). Total wave-equivalent ≈ 0.5-0.6, comfortably within the 16-agent-hour single-wave envelope (per context §7).

**Owner rationale**: per partition manifest §1 Wave W0a the wave-author is `gen-physicist` because the items are cross-reviewer methodology rules originating from BOTH lizzi 9A §7 (W-3 v2 + 5A v2 + sub-diff C) AND gen-physicist 9A §4.9 + §11 + §13 + S-7 §V.9 + §V.24 — no single specialist owns the full carry-forward set. The plan is authored here; runtime test-case design is delegated to specialists per `.claude/skills/rclab-plan/skill.md` §3b (gen-physicist is blacklisted from runtime test-case design).

**Sequencing justification (smaller-chunks)**: W0a is split off W0 because (a) R1 is the heaviest single item in the W0 family (3-4h, file-edit + cross-reference annotation work) and benefits from a single dedicated agent session; (b) R2 ships a NEW infrastructure script with a 13-site fixture that must close to floating-point tolerance — running it in the same wave as R4-R10 risks fixture-vs-other-script contention; (c) R3 / R5 / R6 are discrete planner-template / classifier / skill edits that share the "rule-pinning" methodology theme with R1 + R2 and fit naturally as the same wave. R4 (canonical-phrasing audit), R7 (single-name-conflation entry), R8 (three-layer methodology), R9 (W7 dual-SHA regen), R10 (dual-SHA infra) are all assigned to W0b — they share methodology-entry / dual-SHA infra theme and decouple cleanly from W0a's rule-file v3 scope.

---

## §0.5. Wave W0a Decision-Point Prerequisites

Verbatim from `session-86-partition.md` §1 Wave W0a Sequencing entry:

- **Inbound prerequisites**: NONE. W0a is foundation; sits at the root of the S86 dependency graph (context §3.1).
- **Outbound dependencies (W0a → downstream waves)**:
  - W0a R5 (K-disambiguation) → W1a T1 (W2-12 entry references K_crit_BdG distinct from K_crit per context §3 sequencing table row 5).
  - W0a R3 (cutoff_axis YAML pin) → W4 C28 (cutoff_sqrt resolution requires the YAML schema field to exist before the connes × lizzi 3-round workshop closes per context §3 + §3.1).
  - W0a R1 + R2 (PRU v3 SOURCE-RECONCILIATION sub-audit) → ALL S86 waves at plan-freeze (sequencing table row 1: "SOURCE-RECONCILIATION sub-audit must be operative at S86 plan-freeze for every subsequent wave").
  - W0a R8 (three-layer methodology) is OUT OF SCOPE for W0a — it lives in W0b. W0a's bridging-rule landing is R1 + R2 + R5 only.

- **Natural split candidates** (if W0a stalls per partition §1): W0a-i = (R1, R2 — heavy methodology unification) and W0a-ii = (R3, R5, R6 — discrete YAML / disambig / skill edits). DO NOT pre-emptively split; dispatch as one wave first.

---

## §I. Carry-Forward Items Mapping

| # | Gate ID | Source synthesis cite (context §2.5 + partition §1 Wave W0a) | Effort |
|:--|:--------|:---------------------------|:-------|
| R1 | `S86-RULE-FILE-V3-LANDING` | lizzi 9A §7 + 5A workshop; partition §1 W0a item 1 | MODERATE 3-4h |
| R2 | `S86-PRU-EXTENSION-RULE-V2-LANDING` | gen-physicist 9A §4.9 + 5A workshop; partition §1 W0a item 2 | 0.5 wave |
| R3 | `S86-CUTOFF-AXIS-YAML-PIN` | gen-physicist S-7 §V.9; partition §1 W0a item 3 | 30 min |
| R5 | `S86-CANON-PRDR-K-DISAMBIGUATION` | gen-physicist 9A §13 + W12-2 + lizzi 9A §7.4 sub-diff C; partition §1 W0a item 4 | 0.3 wave |
| R6 | `S86-PLAN-GEN-DISCIPLINE-UPDATE` | gen-physicist S-7 §V.24; partition §1 W0a item 5 | 1-2h |

---

## §W0a-1. S86-RULE-FILE-V3-LANDING

**1. Gate ID**: `S86-RULE-FILE-V3-LANDING`

**2. Trigger**: `[VERIFY]` — quantitative verification (clause-count enumeration + cross-reference link check) via Python before commit. No physical sign/direction claim; the verification target is structural completeness of the v3 changelog header.

**3. Classification**: META (methodology rule-file landing — keeps subsequent physics-gates honest; not a phononic / geometric / particle gate; explicitly NON-PHONONIC).

**4. Agent type**: `lizzi-spectral-functional-theorist`. Rationale: the W-3 v2 11-clause set and the 5A v2 3-sub-diff set both originated as lizzi-track outputs (lizzi 9A §7 + lizzi S-7 §V — see context §2.5 verbatim citation). The 2 PARENT/CHILD cross-references are lizzi-authored (lizzi 9A §7.5). Lizzi is the canonical owner of this consolidation; gen-physicist co-authored some clauses but is blacklisted from runtime test-case design per `.claude/skills/rclab-plan/skill.md` §3b. `connes-ncg-theorist` is a fallback if lizzi is saturated, since the rule-file edits are NCG-adjacent.

**5. Hypothesis**: The S85 Rule-File v3 = W-3 v2 (11 clauses) ∪ 5A v2 (3 sub-diffs / 7 NEW debt classes) + 2 PARENT/CHILD cross-reference annotations is landable as a single consolidated diff to four target files (`.claude/rules/epistemic-discipline.md`, `.claude/rules/math-scripts.md`, `.claude/templates/pru-pre-registration-template.md`, `.claude/skills/rclab-plan/skill.md`) with a v3 changelog header documenting the W-3 + 5A consolidation provenance.

**6. Method (complete dispatch prompt for runtime agent)**:

```
You are lizzi-spectral-functional-theorist. Land the FULL S85 Rule-File v3 per context §2.5 + closeout §6.5 + §3.5 R1.

Source rule-file diff specifications (READ FIRST):
- W-3 v2: 11 plan-layer methodology debt clauses across the 4 target files (lizzi 9A §7.1-§7.4)
- 5A v2 sub-diff A: SOURCE-RECONCILIATION sub-audit (PRU Class 8.1) → .claude/rules/epistemic-discipline.md
- 5A v2 sub-diff B: Machinery-feasibility audit (GPU-pin envelope + root-count S1 flag) → .claude/rules/math-scripts.md
- 5A v2 sub-diff C: PRDR keyword-window granularity (8-K-atom enumeration) + sig_2 scope-correction + 5B-class scan-as-robustness INFO-mode → .claude/templates/pru-pre-registration-template.md
- 2 PARENT/CHILD cross-references:
  (i) W-3 §G2 (g) keyword-context-audit ↔ 5A G4a PRDR bare-K window
  (ii) W-3 §G2 (c) GPU-pin selectivity ↔ 5A G3 GPU-pin feasibility envelope

Target files (4):
1. .claude/rules/epistemic-discipline.md
2. .claude/rules/math-scripts.md
3. .claude/templates/pru-pre-registration-template.md
4. .claude/skills/rclab-plan/skill.md

Procedure:
1. For each of the 11 W-3 v2 clauses, append the clause text to its target file under a new "## Rule-File v3 (S85 W-3 v2 union)" section. Each clause carries its origin tag `[W-3 v2 clause N]`.
2. For each of the 3 5A v2 sub-diffs (A/B/C), append the sub-diff body to its target file under a new "## Rule-File v3 (S85 5A v2 sub-diff X)" section. Each sub-diff carries its origin tag `[5A v2 sub-diff X]`.
3. Add the 2 PARENT/CHILD cross-references as bidirectional `<!-- xref: ... -->` HTML comments in BOTH the W-3 and 5A sections of the affected files.
4. Insert a top-of-file v3 changelog header in EACH of the 4 files:
   ```
   ## Changelog v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)
   - W-3 v2: <list of clause IDs landed in this file>
   - 5A v2: <list of sub-diff IDs landed in this file>
   - PARENT/CHILD cross-references: <list of xref pairs touching this file>
   - Source: lizzi 9A §7 + 5A workshop, consolidated per S85 closeout §3.5 R1 + §6.5 + S86 plan W0a-1
   ```

5. Verification (Python): write a tiny script `computations/_rule_file_v3_landing_verify.py` that:
   (a) greps each of the 4 files for the v3 changelog header presence;
   (b) counts `[W-3 v2 clause N]` tags (target = 11 across all 4 files);
   (c) counts `[5A v2 sub-diff X]` tags (target = 3 across all 4 files);
   (d) counts `<!-- xref: -->` comments (target = 4 = 2 cross-references × 2 directions);
   (e) emits one verdict line in canonical 4-tuple form.

6. Output: append ONE verdict line to computations/s86_gate_verdicts.txt:
   `S86-RULE-FILE-V3-LANDING: PASS|FAIL -- value=<W3_count+5A_count+xref_count> scheme=v3-changelog convention=W-3+5A-union L_max=N/A sha256=<closure>`

   Companion comment row (per W9a-99 dual-SHA template):
   `# audit_sha256_short=<first-16-hex> content_sha256=<64-hex> audit_sha256=<64-hex>`

Imports: NONE (file-edit only, no canonical_constants needed; verifier script has no numpy/torch).
GPU: N/A (text-edit + grep).
```

**7. Machinery pin (PRDR — rule-pinning)**:
- `clause_count_target`: 11 (W-3 v2 clauses)
- `sub_diff_count_target`: 3 (5A v2 sub-diffs A/B/C)
- `xref_count_target`: 4 (= 2 PARENT/CHILD pairs × 2 bidirectional comment rows)
- `target_file_count`: 4 (epistemic-discipline.md / math-scripts.md / pru-pre-registration-template.md / rclab-plan/skill.md)
- `changelog_header_format`: `## Changelog v3 (S85 W-3 v2 + 5A v2 union, landed S86 W0a-1)`
- `source_rule_file_pins`:
  - `lizzi_9A_§7_sha256`: `<computed-at-runtime>` (input: sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md)
  - `S85_5A_workshop_sha256`: `<computed-at-runtime>` (input: sessions/archive/session-85/workshops/s85-5A-workshop.md or analogous path)
  - `gen-physicist_9A_§7.5_sha256`: `<computed-at-runtime>` (input: sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md)
- `verifier_script`: `computations/_rule_file_v3_landing_verify.py` (NEW)

**8. Expected output 4-tuple**: `(value=11+3+4=18, scheme=v3-changelog, convention=W-3+5A-union, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: 11 W-3 v2 clauses + 3 5A v2 sub-diffs + 4 PARENT/CHILD cross-reference comment rows ALL present across the 4 target files; v3 changelog header present in EACH of the 4 files. Tolerance rule: THEOREM (exact equality on count; structural completeness has no tolerance band).
- **FAIL**: ANY clause / sub-diff / cross-reference / changelog header missing.
- **INFO**: NOT applicable (rule-file landing is binary present/absent).

**10. Substitution chain**: not required — this gate is a count-equality check (`landed_count == target_count`), no sign / direction / threshold-band claim. The 4-tuple verification is exact-equality enumeration via grep, structurally identical to a checksum match. No physical quantities involved.

**11. What PASSES / FAILS / INFO MEAN for the solution space**:
- **PASS**: the S86 plan-design configuration space is reduced to the subset that respects the v3 union of methodology rules. All subsequent S86 gates (W0b through W15) operate under the v3 epistemic floor; PRU Class 8.1 SOURCE-RECONCILIATION sub-audit is now mandatory at every plan-freeze. The W-3 v2 + 5A v2 debt classes are formally closed at the rule-file level.
- **FAIL**: at least one W-3 / 5A clause is unlanded; the v3 floor is not in force; downstream waves run under v2 (or hybrid v2/v3) — methodology debt persists into S87.
- The "solution space" for this METHODOLOGY-class gate is the set of plan-design configurations that survive PRU-audit at S86+ plan-freeze. PASS contracts that space to the v3-compliant subset.

**12. Effort estimate**: MODERATE 3-4h (file-edit + verifier script + dual-SHA verdict-line append).

**13. Substrate-framing reminder**: This gate is METHODOLOGY-class. It is NOT phononic. It is a rule-file landing that pins the scaffolding within which every subsequent physics-gate (PHONONIC, GEOMETRIC, PARTICLE) is evaluated. The framing is "this rule keeps subsequent physics-gates honest"; the gate itself does not derive substrate observables, does not invoke D_K eigenvalues, and does not produce spectral-action moments.

---

## §W0a-2. S86-PRU-EXTENSION-RULE-V2-LANDING

**1. Gate ID**: `S86-PRU-EXTENSION-RULE-V2-LANDING`

**2. Trigger**: `[VERIFY]` — quantitative verification of fixture replay accuracy (`D_max = 5.6726` reproduction within 1e-10) via Python.

**3. Classification**: META (NON-PHONONIC; new audit-script infrastructure that polices subsequent gates).

**4. Agent type**: `lizzi-spectral-functional-theorist`. Rationale: the 5A workshop sub-diff A (SOURCE-RECONCILIATION sub-audit) is a lizzi-track output (context §4 + §2.5); the 5-class taxonomy and 13-site retrospective fixture were derived by lizzi in 9A §C-1 / §7.4 with gen-physicist co-author on 9A §4.9. Lizzi is the natural runtime agent. `gen-physicist` is blacklisted from runtime test-case design.

**5. Hypothesis**: The PRU Extension Rule v2 (Diff 1+2+3 from 5A workshop) — comprising (i) a new audit script `computations/_source_reconciliation_audit.py` that detects PINNED-BUT-DRIFT source-reconciliation defects, (ii) a 5-class taxonomy canonicalized in `.claude/templates/pru-pre-registration-template.md`, and (iii) a 13-site retrospective fixture that replays the historical D_max = 5.6726 measurement — can be landed as a single coherent infrastructure addition that reproduces the historical D_max value to within 1e-10 absolute tolerance.

**6. Method (complete dispatch prompt for runtime agent)**:

```
You are lizzi-spectral-functional-theorist. Build and land the PRU Extension Rule v2 per context §2.5 R2 + closeout §3.5 + 5A workshop sub-diff A.

Output files:
1. computations/_source_reconciliation_audit.py (NEW infrastructure script)
2. .claude/templates/pru-pre-registration-template.md (EDIT — add 5-class taxonomy)

Script specification (`_source_reconciliation_audit.py`):
- No `s86_` prefix (infrastructure script, not per-gate verification — same convention as `_pru_cardinality_audit.py`, `_yaml_gate_validator.py`, `_dual_sha_uniqueness_audit.py`).
- Imports: `from canonical_constants import *` (even if no canonical constant is read here, the import enforces the audit-pipeline's compliance check; the import is harmless at runtime).
- CLI signature: `python computations/_source_reconciliation_audit.py [--session N] [--json] [--fixture FIXTURE_DIR]`
- Default: scan all `computations/s{N}_*.py` for the current session N (auto-detected from cwd or via --session); replay the 13-site retrospective fixture if --fixture is set.
- Detect logic (sub-diff A spec): for each script, parse its input-pin map; for each pin, compare the pin's declared SHA against the on-disk SHA of the referenced file. Flag any DRIFT (pin SHA differs from on-disk SHA) as a Class-8.1 PRU defect.

5-class taxonomy (canonical in `pru-pre-registration-template.md` + classifier-pipeline in the script):
- Class A — PINNED-AND-MATCHED (declared pin SHA == on-disk SHA; no defect)
- Class B — PINNED-BUT-DRIFTED (declared pin SHA != on-disk SHA; on-disk file modified after pin)
- Class C — UNPINNED-BUT-REFERENCED (script reads file with no SHA pin in input map; PRU Class 8.1 defect)
- Class D — PINNED-BUT-MISSING (declared pin SHA references nonexistent file; broken pin)
- Class E — PINNED-MULTIPLE-DIVERGENT (same logical input pinned with two different SHAs across two scripts; cross-script source contradiction)

13-site retrospective fixture: replay the historical 13-site source-reconciliation measurement that produced D_max = 5.6726 (the maximum SHA-divergence distance across the 13 detected sites). Fixture data layout: `computations/_source_reconciliation_fixture/{site_1, site_2, ..., site_13}/` each containing `pin_declared.sha256` + `on_disk.sha256` + `expected_class.txt` + `expected_distance.float`.

PASS criterion: replayed `D_max` across 13 fixture sites equals 5.6726 within abs(error) ≤ 1e-10.

Imports / numerics: only hashlib + os + json + (optional) numpy for the max-reduce. NO matrix ops, NO eigvals — CPU-only is fine. Set `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy` per `.claude/rules/computation-environment.md` cap.

Template edit (`pru-pre-registration-template.md`):
- Append a new section "## PRU Class 8.1 — SOURCE-RECONCILIATION (5A v2 sub-diff A)" containing the 5-class taxonomy (A/B/C/D/E) with definition + example for each class.
- Cross-reference the audit-script path `computations/_source_reconciliation_audit.py`.

Output: append ONE verdict line to computations/s86_gate_verdicts.txt:
`S86-PRU-EXTENSION-RULE-V2-LANDING: PASS|FAIL -- value=<D_max_replayed> scheme=source-reconciliation convention=5-class-taxonomy L_max=N/A sha256=<closure>`

Plus dual-SHA companion comment row per W9a-99 template.
```

**7. Machinery pin (PRDR — script + fixture pinning)**:
- `script_path`: `computations/_source_reconciliation_audit.py` (NEW)
- `template_path`: `.claude/templates/pru-pre-registration-template.md` (EDIT)
- `fixture_dir`: `computations/_source_reconciliation_fixture/`
- `fixture_site_count`: 13
- `D_max_target`: 5.6726
- `D_max_tolerance_abs`: 1e-10 (RATIO/ABSOLUTE/THEOREM = ABSOLUTE)
- `taxonomy_class_count`: 5 (Class A through Class E)
- `cli_signature`: `[--session N] [--json] [--fixture FIXTURE_DIR]`
- `random_seed`: N/A (deterministic SHA replay, no stochastic component)
- `GPU_path`: N/A (CPU-only; SHA + max-reduce; no matmul; thread-cap `OMP_NUM_THREADS=8`)
- `source_workshop_sha256`: `<computed-at-runtime>` (input: sessions/archive/session-85/workshops/s85-5A-workshop.md)

**8. Expected output 4-tuple**: `(value=5.6726, scheme=source-reconciliation, convention=5-class-taxonomy, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: `_source_reconciliation_audit.py` exists; 13-site fixture replays `D_max = 5.6726` within abs-error ≤ 1e-10; 5-class taxonomy section present in `pru-pre-registration-template.md`. Tolerance rule: ABSOLUTE 1e-10 on D_max replay.
- **FAIL**: any of: script missing; fixture replay disagrees by > 1e-10; taxonomy section missing.
- **INFO**: NOT applicable (binary infrastructure landing).

**10. Substitution chain** (required for the `D_max ≤ 1e-10` tolerance claim):

```
Step 1 (definitions):
  D_target            = 5.6726                              [historical 5A workshop measurement]
  D_replayed          = max_{i=1..13} dist(pin_SHA_i, on_disk_SHA_i)  [fixture replay]
                      = max_{i=1..13} hamming_or_difference_metric_over_13_sites
  abs_error           = |D_replayed - D_target|             [definition of replay accuracy]
  tolerance_threshold = 1e-10                                [pre-registered ABSOLUTE bound]

Step 2 (substitute):
  PASS_predicate = (abs_error <= tolerance_threshold)
                 = (|D_replayed - D_target| <= 1e-10)
                 = (|D_replayed - 5.6726| <= 1e-10)

Step 3 (simplify):
  PASS iff D_replayed ∈ [5.6726 - 1e-10, 5.6726 + 1e-10]
       iff D_replayed ∈ [5.67259999999, 5.67260000001]    (to display precision)

Step 4 (direction):
  Larger abs_error => greater divergence from historical measurement => fixture not faithfully reproducing the 5A workshop's D_max calculation => PRU defect detector is mis-calibrated => methodology floor is unsafe to land. Therefore the threshold direction is "PASS iff abs_error is SMALL (≤ 1e-10)".

Conclusion: the threshold direction is monotone-decreasing in abs_error; smaller error == better fidelity == PASS.
```

Python verification (the runtime agent runs this BEFORE appending the verdict line):
```python
import json, sys
result = json.load(open("computations/_source_reconciliation_audit.out.json"))
abs_error = abs(result["D_max_replayed"] - 5.6726)
assert abs_error <= 1e-10, f"FAIL: abs_error={abs_error} > 1e-10"
print(f"PASS: abs_error={abs_error}")
```

**11. What PASSES / FAILS / INFO MEAN for the solution space**:
- **PASS**: the SOURCE-RECONCILIATION sub-audit is operational; PRU Class 8.1 PINNED-BUT-DRIFT defects are now machine-detectable at every S86+ plan-freeze. The plan-design configuration space contracts to the subset that respects pin-fidelity. Subsequent waves (W0b onward) cannot pass plan-freeze with a drift defect.
- **FAIL**: the audit cannot reliably detect the historical defect class; PRU Class 8.1 remains a dark corner; all S86+ plans risk shipping with undetected pin drift.
- The plan-design configuration space is the set of plan documents that survive `_source_reconciliation_audit.py` exit-0 + `_pru_cardinality_audit.py` exit-0 simultaneously.

**12. Effort estimate**: 0.5 wave (~6-8 agent-hours: script + template edit + fixture build + 1e-10 closure + dual-SHA verdict + working-paper section).

**13. Substrate-framing reminder**: METHODOLOGY-class. NON-PHONONIC. The audit-script polices source-reconciliation hygiene of plan documents; it does not derive any substrate observable. No D_K eigenvalues, no spectral moments, no Jensen deformation involved. The framing is "this audit keeps subsequent physics-gates honest at plan-freeze".

---

## §W0a-3. S86-CUTOFF-AXIS-YAML-PIN

**1. Gate ID**: `S86-CUTOFF-AXIS-YAML-PIN`

**2. Trigger**: `[VERIFY]` — schema-validator round-trip + retrofit-count enumeration.

**3. Classification**: META (NON-PHONONIC; YAML schema field for planner-template).

**4. Agent type**: `connes-ncg-theorist`. Rationale: the cutoff convention being disambiguated (`spectral` vs `coherence`) is an NCG-spectral-action question — `spectral` cutoffs (Λ on D_K eigenvalues) versus `coherence` cutoffs (K on substrate dispersion / corridor length) are distinct NCG concepts that the W3-9 vs W3-11 PRU defect collapsed into a single `cutoff` field. connes-ncg-theorist is the canonical authority on NCG cutoff semantics. Lizzi is a fallback (also competent on Mellin-cone cutoffs); gen-physicist is blacklisted.

**5. Hypothesis**: Adding a `cutoff_axis: spectral | coherence | both` enumerated YAML field to the gate-block schema (validated by `computations/_yaml_gate_validator.py`) and retrofitting all S85 plan blocks that invoke a cutoff produces a planner-template-level closure of the W3-9 vs W3-11 PRU defect. PASS = validator accepts new field + at least N_retrofit_target gate blocks updated.

**6. Method (complete dispatch prompt for runtime agent)**:

```
You are connes-ncg-theorist. Land the cutoff_axis YAML field per context §2.5 R3 + gen-physicist S-7 §V.9.

Schema specification:
- Field name: `cutoff_axis`
- Field type: enumerated string
- Allowed values: `spectral`, `coherence`, `both`
- Required for: every gate block whose machinery pin invokes a cutoff (Λ_cut, K_cut, K_R5, K_crit, K_FIRAS, etc.)
- Default: NONE (must be explicit; absence triggers PRDR Class 8 PRE-REG-INC)

Files to edit:
1. `computations/_yaml_gate_validator.py` — add validation rule for `cutoff_axis ∈ {spectral, coherence, both}`; emit PRE-REG-INC if missing on a cutoff-invoking gate.
2. `.claude/templates/pru-pre-registration-template.md` — add `cutoff_axis` to the canonical machinery-pin checklist with a 3-line description: "spectral = Λ on D_K eigenvalues; coherence = K on substrate dispersion / corridor length; both = gate references both axes (must justify)."
3. Retrofit S85 gate blocks: scan `sessions/session-plan/session-85-plan-w*.md` for any gate block referencing a cutoff (regex pattern: `Λ_cut|K_cut|K_R5|K_crit|K_FIRAS|K_floor|K_wall|cutoff_sqrt`); for each, add `cutoff_axis: <appropriate-value>` to its machinery pin block. Track retrofit count.

Procedure:
1. Edit `_yaml_gate_validator.py` to add the new validation rule.
2. Edit `pru-pre-registration-template.md` to canonicalize the field.
3. Run a static scan of S85 plan files; produce a CSV `computations/_cutoff_axis_retrofit.csv` with columns `[plan_file, gate_id, current_cutoff_keyword, proposed_cutoff_axis_value, status]`.
4. Apply retrofit edits in-place to each affected S85 plan file (adding the YAML field to each gate block; this is a documentation-only edit that does NOT change verdict semantics, per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS clause 3 "Post-hoc pre-registration editing" — to comply, log each retrofit with a `# post-hoc-cutoff-axis-pin: landed S86 W0a-3` comment so it is documentation-only, not a verdict-affecting edit).
5. Re-run `_yaml_gate_validator.py` on all 16 S85 plan files (W0, W1a-c, W2, W3, W4, W5, W6-13, …); validator must exit 0 on each.

Output: append ONE verdict line to computations/s86_gate_verdicts.txt:
`S86-CUTOFF-AXIS-YAML-PIN: PASS|FAIL -- value=<retrofit_count> scheme=yaml-schema convention=v3-cutoff-axis-enum L_max=N/A sha256=<closure>`

Plus dual-SHA companion comment row.

Imports: NONE for YAML edit; the validator already imports its own deps. NO numpy/torch (text + YAML only).
GPU: N/A.
```

**7. Machinery pin (PRDR — schema field pinning)**:
- `field_name`: `cutoff_axis`
- `field_type`: enumerated string ∈ {`spectral`, `coherence`, `both`}
- `field_required_when`: machinery pin block contains any of `{Λ_cut, K_cut, K_R5, K_crit, K_FIRAS, K_floor, K_wall, cutoff_sqrt}` (8 keyword triggers — the same K-family keywords R5 disambiguates)
- `validator_path`: `computations/_yaml_gate_validator.py` (EDIT)
- `template_path`: `.claude/templates/pru-pre-registration-template.md` (EDIT)
- `retrofit_csv_path`: `computations/_cutoff_axis_retrofit.csv` (NEW)
- `S85_plan_file_count`: 16 (W0, W1a, W1b, W1c, W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W12, W13)
- `retrofit_target_count_lower_bound`: ≥ 1 (at minimum the W3-9 + W3-11 pair must retrofit; realistically 5-15 gate blocks across the 16 plans)

**8. Expected output 4-tuple**: `(value=<retrofit_count>, scheme=yaml-schema, convention=v3-cutoff-axis-enum, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: `_yaml_gate_validator.py` exits 0 on each of the 16 S85 plan files after retrofit; `cutoff_axis` field present in `pru-pre-registration-template.md`; retrofit_count ≥ 1 (i.e., at least the W3-9/W3-11 pair retrofitted, the minimum closure of the originating PRU defect). Tolerance rule: THEOREM (binary validator pass + presence check).
- **FAIL**: validator rejects ≥ 1 plan file; OR template missing the field; OR retrofit_count = 0.
- **INFO**: NOT applicable (binary schema landing).

**10. Substitution chain**: not required — this gate is a binary present/absent check on a YAML schema field plus a non-negative retrofit count. No sign / direction / threshold-band claim. The "≥ 1" minimum is structural (the W3-9/W3-11 pair MUST be retrofitted to close the originating PRU defect; not retrofitting them re-introduces the defect).

**11. What PASSES / FAILS / INFO MEAN for the solution space**:
- **PASS**: the planner-template configuration space is reduced to the subset where every cutoff-invoking gate explicitly declares which axis (spectral / coherence / both) it cuts off. The W3-9 vs W3-11 PRU defect is closed at the planner-template level — no script-level rerun is required for closure. Subsequent S86+ gates that invoke cutoffs cannot pass plan-freeze without the field set.
- **FAIL**: the cutoff ambiguity persists; W3-9 / W3-11-class PRU defects remain possible in S86+ plans; downstream W4 C28 cutoff_sqrt adjudication runs without schema support.

**12. Effort estimate**: 30 min (small validator edit + template edit + scan + retrofit script + dual-SHA verdict + working-paper section).

**13. Substrate-framing reminder**: METHODOLOGY-class. NON-PHONONIC. The YAML schema field disambiguates two distinct NCG concepts (spectral cutoff on D_K eigenvalues vs coherence cutoff on substrate corridor length) at the planner-template level; it does not itself compute any spectral moment or substrate observable. The framing is "this schema field forces every cutoff-invoking gate to declare its axis explicitly, eliminating an entire class of PRU defects".

---

## §W0a-4. S86-CANON-PRDR-K-DISAMBIGUATION

**1. Gate ID**: `S86-CANON-PRDR-K-DISAMBIGUATION`

**2. Trigger**: `[VERIFY]` — exact-equality check on classifier false-positive count (target = 0 from baseline = 14).

**3. Classification**: META (NON-PHONONIC; classifier-vocabulary expansion in PRDR audit pipeline).

**4. Agent type**: `lizzi-spectral-functional-theorist`. Rationale: the 8-key K-disambiguation is a lizzi 9A §7.4 sub-diff C output (context §2.5 R5 verbatim citation: "lizzi 9A §7.4 sub-diff C"); gen-physicist 9A §13 + W12-2 are co-authors on the false-positive enumeration but lizzi owns the keyword-window granularity rule. `connes-ncg-theorist` is a fallback (the K-family keywords are NCG-corridor concepts).

**5. Hypothesis**: Splitting the bare `K` observable in the `_pru_*` classifier vocabulary into 8 explicit sub-keys (`K_base / K_corridor / K_R5 / K_crit / K_substrate / K_R3 / K_FIRAS / K_pivot`) and re-running the classifier on the historical W12-2 corpus reduces the false-positive CONTRADICTS count from 14 to 0.

**6. Method (complete dispatch prompt for runtime agent)**:

```
You are lizzi-spectral-functional-theorist. Land the canonical PRDR-K disambiguation per context §2.5 R5 + gen-physicist 9A §13 + W12-2 + lizzi 9A §7.4 sub-diff C.

Source baseline: W12-2 W6-W13 closeout — bare-K classifier produced 14 false-positive CONTRADICTS on K-family pairs (e.g., K_crit vs K_FIRAS flagged as contradiction when they refer to distinct K observables).

8-key disambiguation table (canonical):
| Sub-key | Definition (one-line) | Canonical source |
|:--------|:----------------------|:-----------------|
| `K_base` | Substrate base coherence wavenumber (canonical_constants reference) | canonical_constants.py |
| `K_corridor` | Corridor-extension wavenumber for K ∈ [K_R5, K_crit] | gen-physicist S-7 §V.4 |
| `K_R5` | Inflationary-corridor lower edge (regulator family R5) | S85 W5 D.4 |
| `K_crit` | Inflationary critical wavenumber (= 91.5 per canonical_constants) | canonical_constants.py |
| `K_substrate` | Substrate intrinsic K (substrate-distance-1 quantity per P5) | gen-physicist 9A §4.5b |
| `K_R3` | R3 schema-validator K (regulator family R3) | gen-physicist S-7 §V.15 |
| `K_FIRAS` | FIRAS-anchored K (post-fold Riemann cover upper edge) | gen-physicist S-7 §V.4 |
| `K_pivot` | Pivot K at N_pivot for SR-flow integration | mack 9A §VI.3 |

Files to edit:
1. `computations/_pru_keyword_classifier.py` (or whichever `_pru_*` script holds the bare-K classifier vocabulary; identify by grep for `"K"` as a vocabulary entry in any computations/_pru_*.py file).
2. `.claude/templates/pru-pre-registration-template.md` — append the 8-key table to the canonical vocabulary section.

Classifier-pipeline edit:
- Replace the single-token `K` vocabulary entry with the 8 sub-keys above.
- Add a regex preprocessor that maps bare `K` in scanned text to the appropriate sub-key based on surrounding context (e.g., `K_FIRAS` if the same line mentions FIRAS, PIXIE, or μ; `K_R5` if R5 or 5-atlas; `K_crit` if 91.5 or critical; etc.). When context is ambiguous, the preprocessor leaves bare `K` flagged as `K_UNRESOLVED` rather than guessing.
- Re-run the classifier on the historical W12-2 corpus and emit a CSV `computations/_pru_k_disambiguation_rerun.csv` with columns `[pair_id, before_class, after_class, false_positive_resolved]`.

PASS criterion: post-disambiguation classifier returns ZERO false-positive CONTRADICTS on the 14 historical pairs (each of the 14 must reclassify to TRUE-POSITIVE-AGREEMENT or TRUE-DISTINCT-OBSERVABLES, both of which are not CONTRADICTS).

Output: append ONE verdict line to computations/s86_gate_verdicts.txt:
`S86-CANON-PRDR-K-DISAMBIGUATION: PASS|FAIL -- value=<post_fp_count> scheme=8-key-K-disambig convention=PRDR-G4a L_max=N/A sha256=<closure>`

Plus dual-SHA companion comment row.

Imports: only what `_pru_keyword_classifier.py` already needs (likely re + json + csv). NO numpy/torch.
GPU: N/A.
```

**7. Machinery pin (PRDR — classifier vocabulary pinning)**:
- `disambiguation_key_count`: 8 (`K_base / K_corridor / K_R5 / K_crit / K_substrate / K_R3 / K_FIRAS / K_pivot`)
- `historical_baseline_fp_count`: 14 (from W12-2)
- `target_post_fp_count`: 0
- `classifier_path`: `computations/_pru_keyword_classifier.py` (EDIT — exact filename to be confirmed by runtime grep)
- `template_path`: `.claude/templates/pru-pre-registration-template.md` (EDIT)
- `rerun_csv_path`: `computations/_pru_k_disambiguation_rerun.csv` (NEW)
- `historical_corpus_pin_sha256`: `<computed-at-runtime>` (input: the W12-2 result file containing the 14 pairs)
- `random_seed`: N/A (deterministic regex classifier)
- `GPU_path`: N/A
- `K_crit_canonical_value_pin`: `91.5` (per canonical_constants — context §1.4 + W12-2)
- `K_crit_BdG_canonical_value_pin`: `2.035` (per W0c C17 future-landing — separate from K_crit, must remain disambiguable; this gate's 8-key split treats them as distinct sub-keys)

**8. Expected output 4-tuple**: `(value=0, scheme=8-key-K-disambig, convention=PRDR-G4a, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: post-disambiguation classifier returns false-positive CONTRADICTS count = 0 on the 14 historical pairs; AND 8-key vocabulary present in `pru-pre-registration-template.md`. Tolerance rule: THEOREM (exact integer equality; no tolerance band).
- **FAIL**: post-disambiguation false-positive count > 0 (ANY remaining false-positive indicates the 8-key split is incomplete or the regex preprocessor mis-resolves at least one pair).
- **INFO**: NOT applicable (the count is exact-integer; binary).

**10. Substitution chain** (required for the false-positive count = 0 claim):

```
Step 1 (definitions):
  N_fp_baseline = 14                                    [W12-2 historical false-positive count, bare-K classifier]
  N_fp_post     = count of pairs (i ∈ {1..14}) such that
                   classifier_after(pair_i, vocab_8key) == "CONTRADICTS"
                                                       [post-disambiguation count]
  PASS_target   = 0                                     [pre-registered]
  delta_fp      = N_fp_baseline - N_fp_post             [false-positives resolved]

Step 2 (substitute):
  PASS_predicate = (N_fp_post == 0)
                 = (count_of_remaining_CONTRADICTS == 0)
                 = (∀ i ∈ {1..14}: classifier_after(pair_i, vocab_8key) ≠ "CONTRADICTS")

Step 3 (simplify):
  PASS iff every one of the 14 historical pairs reclassifies to a non-CONTRADICTS class
       (either TRUE-POSITIVE-AGREEMENT, TRUE-DISTINCT-OBSERVABLES, or K_UNRESOLVED)
  In terms of delta: PASS iff delta_fp == 14 (all 14 false-positives resolved by the 8-key split)

Step 4 (direction):
  Larger N_fp_post => more residual false-positives => the 8-key vocabulary is insufficient
                       to distinguish all K-family observables in the historical corpus
                    => disambiguation incomplete => K-disambiguation PRU defect persists.
  Therefore the threshold direction is "PASS iff N_fp_post is SMALL (= 0)";
  monotone-decreasing in N_fp_post.

Conclusion: PASS condition is "exact zero residual false-positives", equivalent to
"all 14 historical pairs successfully disambiguated by the 8-key vocabulary".
```

Python verification (the runtime agent runs this BEFORE appending the verdict line):
```python
import pandas as pd
df = pd.read_csv("computations/_pru_k_disambiguation_rerun.csv")
post_fp = (df["after_class"] == "CONTRADICTS").sum()
assert post_fp == 0, f"FAIL: {post_fp} residual false-positive CONTRADICTS"
print(f"PASS: 0 residual false-positives (was 14)")
```

**11. What PASSES / FAILS / INFO MEAN for the solution space**:
- **PASS**: the PRDR classifier vocabulary contracts to the subset that respects 8-way K disambiguation; no S86+ plan can ship a bare-K reference without the classifier flagging it for explicit sub-key resolution. The W12-2 false-positive class is closed at the classifier-vocabulary level. The plan-design configuration space contracts to plans that use disambiguated K-family keywords throughout.
- **FAIL**: residual false-positives > 0 means the 8-key split is incomplete; the classifier still produces spurious cross-pair contradictions; downstream PRDR audits in S86+ produce noise that obscures real defects.

**12. Effort estimate**: 0.3 wave (~3-5 agent-hours: classifier edit + regex preprocessor + template update + 14-pair fixture rerun + CSV emission + dual-SHA verdict + working-paper section).

**13. Substrate-framing reminder**: METHODOLOGY-class. NON-PHONONIC. The 8-key K disambiguation operates on the classifier vocabulary that polices PRDR audits of plan documents; it does not derive any K-corridor observable, does not invoke D_K eigenvalues, does not compute spectral moments. The 8 sub-keys themselves NAME substrate observables (K_substrate, K_corridor, K_pivot, etc.), but the gate's task is purely lexical/vocabulary disambiguation, not numerical computation of any of those K values. The framing is "this disambiguation lets the classifier distinguish 8 distinct substrate K observables that previously collapsed to one bare-K token, eliminating false-positive cross-observable contradictions in the PRDR audit pipeline".

---

## §W0a-5. S86-PLAN-GEN-DISCIPLINE-UPDATE

**1. Gate ID**: `S86-PLAN-GEN-DISCIPLINE-UPDATE`

**2. Trigger**: `[VERIFY]` — schema check that updated `/rclab-plan` skill produces template plans that read live verdict-state from canonical paths rather than carrying hardcoded `expected_verdicts` lists.

**3. Classification**: META (NON-PHONONIC; skill-file + plan-template update for plan-authoring discipline).

**4. Agent type**: `connes-ncg-theorist`. Rationale: this is a tooling gate not tied to physics — it edits the `/rclab-plan` skill file and plan-authoring templates. Per partition manifest §1 Wave W0a item 5 dispatch instruction: "for tooling gates not tied to physics, consider `connes-ncg-theorist` or `lizzi-spectral-functional-theorist`". connes-ncg-theorist owns the skill-update task because lizzi is already saturated on R1 + R2 + R5 in this wave (3 of the 5 W0a items). gen-physicist is the originating-synthesis author (gen-physicist S-7 §V.24) but is blacklisted from runtime test-case design.

**5. Hypothesis**: Updating `.claude/skills/rclab-plan/skill.md` (and the plan-authoring templates it references) so that template-generated plans dynamically read the latest-observed verdict state from canonical file paths (`computations/s{N}_gate_verdicts.txt`) rather than hardcoding `expected_verdicts: [...]` lists in plan documents eliminates a class of PRU drift defects (the `expected_verdicts` list goes stale the moment any verdict line is appended after plan-write).

**6. Method (complete dispatch prompt for runtime agent)**:

```
You are connes-ncg-theorist. Land the plan-gen discipline update per context §2.5 R6 + gen-physicist S-7 §V.24.

Files to edit:
1. `.claude/skills/rclab-plan/skill.md` — the primary skill file.
2. `.claude/templates/synthesis-template.md`, `.claude/templates/workingpaper-template.md`, `.claude/templates/agent-roster-template.md` (any plan-authoring template that currently embeds `expected_verdicts` references).
3. `.claude/templates/pru-pre-registration-template.md` — add a clause forbidding hardcoded `expected_verdicts` blocks.

Discipline update content:
- Replace any pattern like `expected_verdicts: [PASS, PASS, FAIL, ...]` (which freezes a snapshot of verdicts at plan-write time) with a CANONICAL FILE PATH reference: `verdict_source: computations/s{N}_gate_verdicts.txt` (which the orchestrator reads at compute time to get the latest-observed verdict state).
- Document the new pattern in the skill's §3b template specification.
- Explicitly forbid hardcoded paths to `sessions/session-{N}/s{N}_gate_verdicts.txt` or `sessions/session-plan/s{N}_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md` "Canonical Verdict-File Path" rule (only `computations/s{N}_gate_verdicts.txt` is canonical).
- Add a templated plan example using the new pattern to verify the skill update produces compliant plans.

Procedure:
1. Identify all hardcoded `expected_verdicts: [...]` references across `.claude/templates/*.md` and `.claude/skills/rclab-plan/skill.md`.
2. For each, replace with `verdict_source: computations/s{N}_gate_verdicts.txt` + a 2-line procedural comment "Read at compute time; do NOT freeze at plan-write".
3. Generate ONE example plan (a minimal 2-gate test plan) using the updated skill; verify the example's machinery-pin block has no hardcoded `expected_verdicts` and the verdict_source path resolves to the canonical `computations/` location.
4. Run a static-grep audit for any residual hardcoded paths matching `sessions/session-{N}/s{N}_gate_verdicts.txt` or `sessions/session-plan/s{N}_gate_verdicts.txt` in any `.claude/templates/*.md` or `.claude/skills/rclab-plan/skill.md`; if any remain, fix them or fail the gate.

Output: append ONE verdict line to computations/s86_gate_verdicts.txt:
`S86-PLAN-GEN-DISCIPLINE-UPDATE: PASS|FAIL -- value=<hardcoded_paths_remaining=0?1:0> scheme=plan-gen-skill-v3 convention=canonical-paths L_max=N/A sha256=<closure>`

Plus dual-SHA companion comment row.

Imports: NONE (text edits + grep only). NO numpy/torch.
GPU: N/A.
```

**7. Machinery pin (PRDR — skill-update pinning)**:
- `skill_path`: `.claude/skills/rclab-plan/skill.md` (EDIT)
- `template_paths`: list of `.claude/templates/*.md` files containing plan-authoring scaffolds (enumerated at runtime via grep for `expected_verdicts` token)
- `canonical_verdict_path`: `computations/s{N}_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md`)
- `forbidden_path_patterns`: 2 patterns —
  - `sessions/session-{N}/s{N}_gate_verdicts.txt`
  - `sessions/session-plan/s{N}_gate_verdicts.txt`
- `hardcoded_paths_target_count`: 0 (post-update; no hardcoded path may remain anywhere in the skill or templates)
- `example_plan_required`: 1 (a minimal templated plan using the updated skill, demonstrating the new pattern)
- `source_synthesis_pin_sha256`: `<computed-at-runtime>` (input: gen-physicist S-7 §V.24 — sessions/archive/session-85/session-85-s7-combined-landscape-gen-physicist.md)

**8. Expected output 4-tuple**: `(value=0, scheme=plan-gen-skill-v3, convention=canonical-paths, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: zero hardcoded `expected_verdicts: [...]` references remain in `.claude/skills/rclab-plan/skill.md` or `.claude/templates/*.md`; AND zero hardcoded forbidden-pattern paths remain; AND at least one templated example plan reads from canonical `computations/s{N}_gate_verdicts.txt`. Tolerance rule: THEOREM (exact integer count == 0).
- **FAIL**: any hardcoded `expected_verdicts` list remains; OR any forbidden path pattern remains; OR no example plan demonstrates the new pattern.
- **INFO**: NOT applicable (binary skill-update landing).

**10. Substitution chain**: not required — this gate is a structural grep-count check on text patterns (`hardcoded_paths_remaining == 0`). No sign / direction / threshold-band claim, no physical quantities, no monotone variable. The "0" is a hard structural target equivalent to a checksum match.

**11. What PASSES / FAILS / INFO MEAN for the solution space**:
- **PASS**: the plan-authoring configuration space contracts to plans that read live verdict state at compute time. The expected-verdicts-go-stale defect class is closed at the skill level; no future S86+ plan can ship with a frozen verdict-snapshot. The verdict-file-path-ambiguity class (canonical vs forbidden variants) is closed at the same time, eliminating the documentation-bug pathway that `.claude/rules/gate-verdicts.md` "Canonical Verdict-File Path" rule warns about.
- **FAIL**: planned plans continue to risk hardcoded snapshots; PRU drift via stale `expected_verdicts` lists remains possible in S86+; verdict-file-path documentation bugs continue to mislead agents.

**12. Effort estimate**: 1-2h (skill file edit + 2-4 template edits + grep audit + 1 example plan + dual-SHA verdict + working-paper section).

**13. Substrate-framing reminder**: METHODOLOGY-class. NON-PHONONIC. The skill update edits plan-authoring scaffolds; it does not derive any substrate observable, does not compute any spectral moment, does not invoke D_K. The framing is "this skill update keeps subsequent plan-write activities honest by forcing live verdict-state reads from the single canonical verdict-file path".

---

## §X. Wave W0a → Downstream Decision Point

W0a outputs are consumed by downstream waves as follows (verbatim from partition §1 Wave W0a Sequencing + context §3 sequencing table):

| W0a output | Downstream consumer | Mechanism |
|:-----------|:--------------------|:----------|
| R5 (8-key K disambiguation) | W1a T1 | T1 W2-12 entry references `K_crit_BdG = 2.035` distinct from `K_crit = 91.5`; the 8-key vocabulary lets T1's permanent-results-registry write distinguish the two without classifier ambiguity (sequencing table row 5). |
| R3 (cutoff_axis YAML pin) | W4 C28 | C28 W-4 cutoff_sqrt 3-round connes × lizzi adjudication needs the YAML schema field to declare whether `cutoff_sqrt` is a spectral cutoff or a coherence cutoff; without R3 the adjudication cannot produce a structurally-distinct verdict. |
| R2 (`_source_reconciliation_audit.py`) | ALL S86 waves at plan-freeze | Sequencing table row 1: "SOURCE-RECONCILIATION sub-audit must be operative at S86 plan-freeze for every subsequent wave"; each wave's plan-freeze (Phase 3e validator) calls `_source_reconciliation_audit.py` as a precondition. PRU Class 8.1 PINNED-BUT-DRIFT defects are blocked at plan-freeze rather than caught at script-rerun. |
| R1 (rule-file v3 union) | ALL S86 waves at plan-freeze + every working-paper section | The v3 rule-file union is the methodology floor under which every S86 gate executes; each agent dispatch reads the v3 rules at spawn time. |
| R6 (plan-gen discipline) | ALL future plan-write sessions (S87+) | The updated `/rclab-plan` skill produces compliant plans by construction; legacy plans (S86 plans authored BEFORE R6 lands are exempt — but S86 plans authored AFTER must pass the new check). |

**Sequencing note**: W0a is dispatched in Batch 1 (parallel with W0b, W0c, W1a, W1b, W1c, W2, W4 per partition §4). All 5 W0a items can run concurrently on a single specialist (4 lizzi assignments + 2 connes-ncg assignments — but most plausibly two specialists in sequence, since lizzi is over-saturated). If W0a stalls per natural-split candidates: split into W0a-i (R1, R2 — heavy) + W0a-ii (R3, R5, R6 — light) per partition §1.

---

## §0.10. Wave W0a Machinery-Enumeration Pin (PRDR §0.11)

| Gate ID | rule_file_target(s) | clause_count_or_field_count | schema_version | tolerance |
|:--------|:--------------------|:----------------------------|:---------------|:----------|
| `S86-RULE-FILE-V3-LANDING` | `.claude/rules/epistemic-discipline.md` + `.claude/rules/math-scripts.md` + `.claude/templates/pru-pre-registration-template.md` + `.claude/skills/rclab-plan/skill.md` | 11 W-3 clauses + 3 5A sub-diffs + 4 xref comments = 18 | v3 | THEOREM (exact count) |
| `S86-PRU-EXTENSION-RULE-V2-LANDING` | `computations/_source_reconciliation_audit.py` (NEW) + `.claude/templates/pru-pre-registration-template.md` (EDIT) | 5-class taxonomy + 13-site fixture + D_max=5.6726 replay | v2 (PRU Extension Rule) | ABSOLUTE 1e-10 |
| `S86-CUTOFF-AXIS-YAML-PIN` | `computations/_yaml_gate_validator.py` (EDIT) + `.claude/templates/pru-pre-registration-template.md` (EDIT) + 16 S85 plan files (RETROFIT) | 1 enumerated YAML field + 16 plan-file scans + ≥1 retrofit | v3-cutoff-axis-enum | THEOREM (binary validator + ≥1 retrofit) |
| `S86-CANON-PRDR-K-DISAMBIGUATION` | `computations/_pru_keyword_classifier.py` (EDIT) + `.claude/templates/pru-pre-registration-template.md` (EDIT) | 8 sub-keys (K_base/K_corridor/K_R5/K_crit/K_substrate/K_R3/K_FIRAS/K_pivot) + 14-pair historical fixture | PRDR-G4a | THEOREM (exact integer count = 0) |
| `S86-PLAN-GEN-DISCIPLINE-UPDATE` | `.claude/skills/rclab-plan/skill.md` (EDIT) + 2-4 `.claude/templates/*.md` (EDIT) | 0 hardcoded `expected_verdicts` + 0 forbidden-pattern paths + ≥1 example plan | plan-gen-skill-v3 | THEOREM (exact integer count = 0) |

All five gates are computation-METHODOLOGY: no GPU path required, no matrix ops, no random_seed (deterministic by construction). All tolerances are either THEOREM (exact equality) or ABSOLUTE 1e-10 (R2 only).

---

## §0.11. Wave W0a Input-SHA Ledger

| Gate ID | Input file | SHA-256 |
|:--------|:-----------|:--------|
| R1 | `sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md` (lizzi 9A §7) | `<computed-at-runtime>` |
| R1 | `sessions/archive/session-85/workshops/s85-w-3-workshop.md` (W-3 v2 source — exact filename TBD by runtime grep) | `<computed-at-runtime>` |
| R1 | `sessions/archive/session-85/workshops/s85-5A-workshop.md` (5A v2 source — exact filename TBD by runtime grep) | `<computed-at-runtime>` |
| R1 | `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` (gen-physicist 9A §7.5 cross-references) | `<computed-at-runtime>` |
| R1 | `sessions/archive/session-85/session-85-full-s85-closeout.md` §3.5 R1 + §6.5 (target-file enumeration) | `<computed-at-runtime>` |
| R2 | `sessions/archive/session-85/workshops/s85-5A-workshop.md` (sub-diff A spec) | `<computed-at-runtime>` |
| R2 | `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` §4.9 (D_max=5.6726 historical measurement) | `<computed-at-runtime>` |
| R2 | `computations/_source_reconciliation_fixture/site_{1..13}/` (NEW; 13-site fixture data) | `<computed-at-runtime>` |
| R3 | `sessions/archive/session-85/session-85-s7-combined-landscape-gen-physicist.md` §V.9 | `<computed-at-runtime>` |
| R3 | All 16 S85 plan files: `sessions/session-plan/session-85-plan-w{0,1a,1b,1c,2,3,4,5,6,7,8,9,10,11,12,13}.md` | `<computed-at-runtime>` |
| R3 | `computations/_yaml_gate_validator.py` (current state, pre-edit) | `<computed-at-runtime>` |
| R5 | `sessions/archive/session-85/session-85-gen-physicist-synthesis-w6-13.md` §13 (W12-2 14-pair enumeration) | `<computed-at-runtime>` |
| R5 | `sessions/archive/session-85/session-85-lizzi-synthesis-w6-13.md` §7.4 sub-diff C | `<computed-at-runtime>` |
| R5 | `computations/_pru_keyword_classifier.py` (current state, pre-edit; exact filename via runtime grep) | `<computed-at-runtime>` |
| R5 | `computations/canonical_constants.py` (K_crit = 91.5; K_crit_BdG = 2.035 will land in W0c C17) | `<computed-at-runtime>` |
| R6 | `sessions/archive/session-85/session-85-s7-combined-landscape-gen-physicist.md` §V.24 | `<computed-at-runtime>` |
| R6 | `.claude/skills/rclab-plan/skill.md` (current state, pre-edit) | `<computed-at-runtime>` |
| R6 | `.claude/templates/*.md` (full enumeration via runtime grep for `expected_verdicts`) | `<computed-at-runtime>` |
| R6 | `.claude/rules/gate-verdicts.md` (canonical-path rule reference) | `<computed-at-runtime>` |

**SHA pinning protocol**: each runtime agent computes SHA-256 of every input file at script start, logs them in the first 20 lines of stdout, and includes them in the closure hash that becomes the `audit_sha256` field of the verdict line (per `.claude/rules/gate-verdicts.md` S81+ rule + W9a-99 dual-SHA template).

---

**End of Session 86 Plan Wave W0a.** Five full gate blocks with the 13-field spec + structural sections (Summary, Decision-Point Prerequisites, Carry-Forward Mapping, Downstream Decision Point, Machinery-Enumeration Pin, Input-SHA Ledger) per `.claude/skills/rclab-plan/skill.md` §3b. All 5 gates are METHODOLOGY-class (NON-PHONONIC); all dispatch to specialists (4 × lizzi-spectral-functional-theorist, 2 × connes-ncg-theorist; 0 × gen-physicist runtime per blacklist); all use the canonical verdict-file path `computations/s86_gate_verdicts.txt`; all use full 64-char dual-SHA per W9a-99; none require GPU or matrix ops.
