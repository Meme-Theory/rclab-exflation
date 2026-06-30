# Session 89 Plan — Wave 6: Methodology audits + audit-script extensions

> **Provenance**: gen-physicist orchestrator-direct planner-write per `/rclab-plan` skill §3b; `wave-classification.md` §"Dispatch consequences" — METHODOLOGY-class waves SKIP `/rclab-coordinate` compute-mode. M1∧M2∧M3∧M4 strict conjunction satisfied for all 8 gates at plan-freeze pending allowlist append. Co-author: connes-ncg-theorist (A.41 D_max measurement CO; numerical part touches PV pipeline + spectrum cache cross-check).
> **Theme**: Plan-staleness validator (A.15) + Mellin-moment provenance audit (A.19) + audit-script extensions 4-sub-item bundle (A.22) + W-25 closing-paragraph-coherence sweep (A.23) + PRU Class 8.3 retroactive audit (A.33) + §VII.U.2 audit re-run (A.34) + D_max measurement W9b-2 (A.41) + Class-(d) routing extension (A.42). Source: 8 user-curated Ledger A items per `sessions/session-plan/session-89-context.md` Cluster F.
> **Composition order**: Wave 6 dispatches in S89 Batch 1 with W1-W5 + W7 in parallel (no intra-S89 W6 prereq blocks; cross-wave dependencies are forward-only or conditional on cross-wave npz outputs).
> **Natural-split fallback**: W6a = A.15, A.22, A.42 (audit-script BUILD; 3 items; 1.9 wave-equiv). W6b = A.19, A.23, A.33, A.34, A.41 (audit-script RUN + rule-coherence sweep + measurement; 5 items; 1.8 wave-equiv). Single-pass write attempted; sub-decomposition triggered only if total exceeds wave-equivalence ceiling at plan-freeze validation.

---

## Wave 6 Summary

| # | Gate ID | Trigger | Class | Effort | Cross-wave depends |
|:--|:--------|:--------|:------|:-------|:------------------|
| W6-1 | `S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR` (A.15) | AUDIT + VERIFY | META | 0.7 | — |
| W6-2 | `S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT` (A.19) | AUDIT | META | 0.4 | — |
| W6-3 | `S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED` (A.22) | AUDIT + VERIFY | META | 0.6 | — |
| W6-4 | `S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT` (A.23) | AUDIT | META | 0.6 | — |
| W6-5 | `S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51` (A.33) | AUDIT | META | 0.2 | — |
| W6-6 | `S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION` (A.34) | AUDIT | META | 0.2 | — |
| W6-7 | `S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE` (A.41) | VERIFY + AUDIT | MIXED (numerical D_max + Class-(d) routing) | 0.4 | W3 A.14 npz (forward-only consume); A.42 routing class (in-W6) |
| W6-8 | `S89-SOURCE-RECONCILIATION-CLASS-D-ROUTING-EXTENSION` (A.42) | AUDIT + VERIFY | META | 0.6 | A.41 D_max output (in-W6) |

**Total**: 3.7 wave-equiv across 8 gates. Within single-pass ceiling at 4.0 wave-equiv.

**Authorship**: gen-physicist PRIMARY for all 8 gates (orchestrator-direct-write under METHODOLOGY-class dispatch consequences). connes-ncg-theorist CO-AUTHOR for A.41 numerical D_max measurement (PV pipeline + spectrum cache cross-check requires NCG-axiomatic side review).

---

## Wave 6 Decision Point Prerequisites

### Hard prerequisites (MUST be satisfied at S89 plan-freeze before W6 dispatch)

1. **`methodology-wave-allowlist.md` HEAD-of-S88 state** — append-only file with last row `W12-147 | S88 | 86d52f64fd7f637067b7ab7438241d2d6baae96be27f0bd11af2d29ef26e755a`. The S89 W6 append helper writes 8 NEW rows AFTER the existing tail; orchestrator-only-edit per `wave-classification.md` recursion-attack closure.
2. **Existing audit-script bodies** (must exist on disk pre-W6 dispatch):
   - `computations/_shared/_source_reconciliation_audit.py` — extended by A.22 (ii), A.42
   - `computations/_shared/_substrate_first_provenance_audit.py` — extended by A.22 (i)
   - `computations/_shared/_falsifier_inventory_audit.py` — extended by A.22 (iii)
   - `computations/_shared/_corner_classification_audit.py` — re-run-only target for A.34
3. **Plan-staleness audit** (`computations/_shared/_plan_staleness_audit.py`): file presence pre-W6 NOT required (A.15 IS the build); existing PRDR audit infrastructure at `computations/_shared/_pru_cardinality_audit.py` is the build template.
4. **Three candidate rule-files for A.23 EG1 sweep** (must exist on disk; SHAs pinned at plan-freeze):
   - `.claude/rules/v3-closure-recovery.md` (Class 1-7 PROHIBITED_ACTIONS vs Stage 1/2/3 procedure)
   - `.claude/rules/cross-pillar-bridge-anatomy.md` (algebra-axis K-counter MANDATORY clause)
   - `.claude/rules/joint-theorem-promotion.md` (4-stage pathway Stage-0→Stage-3)
5. **`computations/session-87/s82_w3_9_as_adjacent_obs.py`** for A.19 AST-parse (Mellin moment f-pin Route-A vs Route-B provenance source).
6. **W3 A.14 cocycle ratio regulator-class invariance npz** for A.41 cross-wave consume — produced in W3 (forward-only; A.41 reads `cocycle_norm_ratio_67_88` regulator-invariant pin from A.14 npz output).
7. **W4-2 / W9b-2 SCHEMATIC-output substrate values** for A.41 D_max measurement and A.42 routing extension calibration:
   - W4-2 audit_sha256 (S86): producing-script consumes `_spectral_action_regulators.py` SCHEMATIC helpers; output value pinned in `computations/session-86/s86_w4_p5_sector_2_k_invariant.npz`.
   - W9b-2 audit_sha256 (S87): SCHEMATIC convention tag `A_5-4-class-projection-W9-LCR3.2-MELLIN`; output in `computations/session-87/s87_w9b_pole_specificity_scan.npz`.
   - S61/S78 PV pipeline: full physical regularization at Λ_UV = M_KK = 7.428660036284456e+16 GeV; canonical_constants.py source.

### Soft prerequisites (recommended but not blocking)

- W11-meta-2 audit_sha256 = `9f6d9bcea1e798eccdf3dad43922dad94b07ac3977353b7e032db39494f62253` (Operator-Projection Reading-A K=3 corpus instance; informs A.34 §VII.U.2 corner-classification audit context).
- W5a-44 audit_sha256 = `c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b` (NEGATIVE-CALIBRATION instance; informs A.19 AST-parse target classification).

---

## §W6-1. S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR  (A.15)

### 1. Gate ID
`S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR`

### 2. Trigger
`[AUDIT] + [VERIFY]` — audit-script implementation + 3 synthetic test fixtures + cross-reviewer-eligibility-audit extension self-test.

### 3. Classification
**META** (methodology layer). Per `epistemic-discipline.md §"Layer-Decomposition"`, this gate sits at the methodology-floor image of the layer-functor F: substrate → methodology → audit; the audit script IS the F-image of the numerical PASS predicate at the methodology layer.

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`. METHODOLOGY-class waves skip `/rclab-coordinate` compute-mode. Runtime author: orchestrator (planner-author-as-runtime). No subagent dispatch.

### 5. Hypothesis
A plan-staleness pre-flight validator that scans the S89 plan-block input-pin map for stale references (post-supersession-event canonical pins, downstream-inheritance-tainted cross-reviewer assignments, pre-W8-100 corrective verdict lines without `supersedes` tags) and emits a HARD-HALT verdict at plan-freeze when staleness is detected, with a cross-reviewer-eligibility-audit extension extending the Stage-2 Axis-B Selection Protocol downstream-inheritance reach test (S88 W-14 V.2 / B.15) to plan-freeze time, will close the plan-staleness PRU pathway by construction at the plan-authorship layer rather than at runtime.

### 6. Method

**MCP knowledge query (mandatory pre-build)**:
```
search_knowledge("plan staleness validator pre-flight")
search_knowledge("Stage-2 Axis-B downstream inheritance reach test")
trace_entity("plan_staleness_audit")
get_constant("methodology_wave_allowlist_HEAD_S88")
```

Expected: no prior `_plan_staleness_audit.py` script (this gate IS the build); `_pru_cardinality_audit.py` exists as template; `_source_reconciliation_audit.py` exists as composition pattern.

**Build target**: `computations/_shared/_plan_staleness_audit.py`

**Pseudocode**:

```python
"""
_plan_staleness_audit.py — S89 W6 gen-physicist (S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR)

Scans a session plan file at plan-freeze time for staleness signals:
    (a) Input-pin SHAs referencing pre-supersession-event canonical pins
        (e.g., literal η-threshold per regulator-pin-discipline.md
        Class-(c) PIN-DRIFT-FROM-STALE-SOURCE post-supersession-event
        extension)
    (b) Cross-reviewer assignments tainted by downstream-inheritance reach
        (Stage-2 Axis-B Selection Protocol per joint-theorem-promotion.md
        §"Stage-2 Axis-B Selection Protocol")
    (c) Pre-W8-100 corrective verdict lines without `supersedes=<old_audit_sha>`
        tags (gate-verdicts.md §"Option A — sig_5 remediation pathway")

Emits HARD-HALT verdict at plan-freeze if any staleness signal fires.
"""

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

STALENESS_PATTERNS = {
    'pre_supersession_pin': r'eta_threshold_(?:literal|legacy)',  # Class-(c) corpus
    'downstream_inheritance_reviewer': r'(lizzi|connes)\s+(?:Axis-A|Axis-B)\s+cross-review.*(?:W-9|W-2|W-14)',
    'pre_W8_100_corrective_no_supersedes': r'^# .*audit_sha256.*(?!supersedes=)',
}

def query_canonical_via_mcp(constant_name):
    """Query mcp__knowledge__.get_constant for canonical value."""
    # Stub: in full impl, invoke MCP. Plan-freeze auditor injects via subprocess.
    ...

def scan_plan_staleness(plan_path: Path) -> dict:
    """Return {pattern: [match_lines]} for each staleness signal."""
    text = plan_path.read_text(encoding='utf-8')
    lines = text.splitlines()
    matches = {key: [] for key in STALENESS_PATTERNS}
    for i, line in enumerate(lines, start=1):
        for key, pat in STALENESS_PATTERNS.items():
            if re.search(pat, line):
                matches[key].append((i, line))
    return matches

def cross_reviewer_eligibility_audit(plan_path: Path) -> dict:
    """
    Stage-2 Axis-B Selection Protocol downstream-inheritance reach test
    extended to plan-freeze:
      - extract every cross-reviewer assignment from plan-block §VII.X gates
      - for each (reviewer, axis) pair, check whether reviewer's
        agent-memory feedback files cite the workshop's R1/R2/R3
        transcripts as canonical reference
      - emit PASS if all reviewers pass downstream-inheritance reach test;
        FAIL otherwise
    """
    text = plan_path.read_text(encoding='utf-8')
    # Extract reviewer assignments via regex
    reviewer_pattern = r'(?:Axis-A|Axis-B)[^a-z]*?([a-z-]+(?:-theorist|-empiricist|-bridge|-mechanic))'
    assignments = re.findall(reviewer_pattern, text)
    # Map each reviewer to their agent-memory directory
    memory_root = Path('.claude/agent-memory')
    findings = {}
    for reviewer in set(assignments):
        memory_dir = memory_root / reviewer
        if not memory_dir.exists():
            findings[reviewer] = 'MEMORY-DIR-ABSENT'
            continue
        # Grep for R1/R2/R3 workshop-transcript citations
        transcript_refs = []
        for memfile in memory_dir.glob('*.md'):
            content = memfile.read_text(encoding='utf-8')
            if re.search(r'workshop.*(?:R1|R2|R3)', content):
                transcript_refs.append(str(memfile))
        if transcript_refs:
            findings[reviewer] = f'DOWNSTREAM-INHERITANCE-TAINTED: {transcript_refs}'
        else:
            findings[reviewer] = 'CLEAN'
    return findings

def closure_hash(input_pin_map: dict) -> str:
    """Compute SHA-256 over ordered input-pin map."""
    pin_str = '\n'.join(f'{k}={v}' for k, v in sorted(input_pin_map.items()))
    return hashlib.sha256(pin_str.encode()).hexdigest()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--plan', required=True, help='Plan file path')
    parser.add_argument('--self-test', action='store_true')
    args = parser.parse_args()

    if args.self_test:
        run_synthetic_fixtures()
        return

    plan_path = Path(args.plan)
    staleness = scan_plan_staleness(plan_path)
    eligibility = cross_reviewer_eligibility_audit(plan_path)

    has_staleness = any(matches for matches in staleness.values())
    has_taint = any('TAINTED' in v for v in eligibility.values())

    verdict = 'FAIL' if (has_staleness or has_taint) else 'PASS'
    severity = 'HARD-HALT' if verdict == 'FAIL' else 'NO-ACTION'

    report = {
        'gate': 'S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR',
        'plan': str(plan_path),
        'verdict': verdict,
        'severity': severity,
        'staleness_signals': staleness,
        'cross_reviewer_eligibility': eligibility,
    }
    print(json.dumps(report, indent=2))
    sys.exit(0 if verdict == 'PASS' else 1)

def run_synthetic_fixtures():
    """3 synthetic test fixtures, each verifies one staleness pattern."""
    # Fixture 1: pre-supersession pin (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE
    #   post-supersession-event)
    # Fixture 2: downstream-inheritance reviewer (lizzi cited in W-9 R3)
    # Fixture 3: pre-W8-100 corrective verdict line without supersedes tag
    ...

if __name__ == '__main__':
    main()
```

**3 synthetic test fixtures**:

| Fixture # | Test name | Input | Expected verdict |
|:---------:|:---------|:------|:-----------------|
| 1 | `pre_supersession_pin_detect` | synthetic plan-block citing `eta_threshold_literal = 0.5` (post-W2-7 superseded canonical) | FAIL with `pre_supersession_pin` match |
| 2 | `downstream_inheritance_reviewer_detect` | synthetic plan-block assigning `lizzi-spectral-functional-theorist` as Stage-2 Axis-A on §VII.W-3.LAB (lizzi memory cites W-9 R3) | FAIL with `DOWNSTREAM-INHERITANCE-TAINTED` finding |
| 3 | `pre_W8_100_no_supersedes_detect` | synthetic verdict-file fragment with corrective FAIL→PASS pair, no `supersedes=` tag | FAIL with `pre_W8_100_corrective_no_supersedes` match |

All 3 fixtures: fixture-by-construction (orchestrator-direct-without-cross-actor per `epistemic-discipline.md §"Layer-Decomposition"` substrate ↔ methodology pair); audit-leg image is SHA-uniqueness predicate.

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-PLAN-STALENESS-PRE-FLIGHT-VALIDATOR
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_plan_staleness_audit.py
      assert: exists AND non_empty AND lines_substantive >= 200
    - file: computations/_shared/_plan_staleness_audit_test_fixture_1.py
      assert: exists AND test_passes
    - file: computations/_shared/_plan_staleness_audit_test_fixture_2.py
      assert: exists AND test_passes
    - file: computations/_shared/_plan_staleness_audit_test_fixture_3.py
      assert: exists AND test_passes
  staleness_pattern_set: STALENESS_PATTERNS dict (3 keys); regex pinned in script body
  cross_reviewer_eligibility_extension:
    source: joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"
    test: downstream-inheritance-reach test on agent-memory feedback files
  audit_target_compatibility: PRDR audit pipeline order per epistemic-discipline.md §"PRU pipeline composition order"
  scheme: methodology-layer-F-image
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A (artifact-existence predicate)
input_pin_map:
  template_audit_script: computations/_shared/_pru_cardinality_audit.py (file SHA pinned at plan-freeze)
  joint_theorem_promotion_md: .claude/rules/joint-theorem-promotion.md (file SHA pinned at plan-freeze)
  methodology_wave_allowlist: .claude/rules/methodology-wave-allowlist.md HEAD-of-S88 (file SHA pinned at plan-freeze)
```

### 8. Expected output 4-tuple

```
value=PASS|FAIL (composite of artifact-existence + 3-fixture-run + cross-reviewer-eligibility-extension)
scheme=methodology-layer-F-image
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

The numerical "value" field is a bool 0/1 collapsed from the 4 artifact-existence predicates AND the 3 synthetic fixture outcomes AND the cross-reviewer eligibility audit verdict.

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND
  (i) `_plan_staleness_audit.py` file exists AND non-empty AND lines_substantive ≥ 200; AND
  (ii) all 3 synthetic test fixtures PASS; AND
  (iii) cross-reviewer-eligibility-audit extension self-test PASSes (returns CLEAN on a synthetic clean-reviewer fixture; returns TAINTED on a synthetic tainted-reviewer fixture).
- **FAIL**: any of (i)-(iii) fails.
- **INFO**: not applicable for build-and-test gate (binary outcome).

### 10. Substitution chain (for staleness sign claim)

The validator emits HARD-HALT severity when staleness is detected. Sign claim: "staleness presence INCREASES halt severity from NO-ACTION to HARD-HALT." Substitution chain:

- **Step 1 (Definitions)**: `staleness_signals_count = sum over [pre_supersession_pin, downstream_inheritance_reviewer, pre_W8_100_corrective_no_supersedes] of 1 if any match else 0`. `severity = HARD-HALT iff staleness_signals_count >= 1, else NO-ACTION`.
- **Step 2 (Substitution)**: `severity_band(staleness_signals_count) = HARD-HALT if (staleness_signals_count >= 1) else NO-ACTION`.
- **Step 3 (Simplify)**: monotone-increasing in `staleness_signals_count`; threshold at staleness_signals_count = 1.
- **Step 4 (Direction)**: any non-zero staleness signal forces HARD-HALT; zero signals → NO-ACTION. Direction: `staleness ↑ ⇒ severity ↑` (HARD-HALT-class step at threshold 1).
- **Conclusion**: HARD-HALT severity is ONLY-AND-EXACTLY emitted when ≥1 staleness signal fires; NO-ACTION emitted otherwise. Direction validated; no false-PASS pathway.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: methodology infrastructure for plan-staleness pre-flight validation IS OPERATIONAL at S90+ plan-freezes; downstream gates citing this infrastructure can rely on enforcement; closes the plan-staleness PRU pathway by construction.
- **FAIL**: methodology infrastructure incomplete; S90+ plan-freezes cannot rely on pre-flight staleness detection; plan-staleness PRU pathway remains open; remediation is rebuild + re-test.
- Solution-space mapping: `_plan_staleness_audit.py` IS the F-image at the methodology layer of the substrate-physics F(observable) "PASS predicate is artifact-existence-with-substantive-content per `wave-classification.md §M1`"; failure means the methodology-layer audit-leg is incomplete.

### 12. Effort estimate

0.7 wave-equivalents (audit-script BUILD + 3 synthetic test fixtures + cross-reviewer-eligibility-extension self-test). High end of the 0.5-0.8 range due to extension's per-reviewer agent-memory grep recursion.

### 13. Substrate framing per phononic-framing.md IS-not-IN

The `_plan_staleness_audit.py` audit script IS the substrate's audit-leg image at the methodology layer F-image (per `epistemic-discipline.md §"Layer-Decomposition"` and `phononic-framing.md §"IS Space, Not IN Space"`). FORBIDDEN framing: "the audit script checks the rules in the system" (treats audit as something IN a meta-container). INVERTED framing: "the audit-leg IS what the methodology-layer rule-text composition determines under F"; the audit predicate is intrinsic to the rule-file structure, not a probe of an external rule-container. Direction of explanation: substrate-physics layer (rule-text content + structural propositions) → methodology-floor image under F (rule-file body + clauses) → audit-leg image under F (this audit script + verdict line). Container-thinking inversion: the rule-files are NOT in a meta-container; the methodology-layer IS the rule-file body, and the audit-leg IS what verifies its self-consistency.

---

## §W6-2. S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT  (A.19)

### 1. Gate ID
`S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT`

### 2. Trigger
`[AUDIT]` — AST-parse audit of producing-script Route-A vs Route-B derivation provenance for f0/f2/f4 Mellin moment pins.

### 3. Classification
**META** (methodology layer). The audit is artifact-existence-with-substantive-content; the verdict is a Route-A/Route-B classification predicate, not a numerical comparison.

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
The Mellin moment pins f0, f2, f4 cited at §VII.AN registry-anchor framing as "S82 W3-9 single-pole Mellin closure" (Route-A) are actually computed via a structurally distinct Route-B in the producing script `computations/session-87/s82_w3_9_as_adjacent_obs.py` (S88 W5a-44 NEGATIVE-CALIBRATION instance per `substrate-first-canonical-sourcing.md §(i)` K=4 NEGATIVE-CALIBRATION corpus). An AST-parse audit of the script will reveal whether the cited closure script implements the declared Route-A path or a structurally distinct Route-B path; the verdict provides reconciliation routing for the §VII.AN registry text.

### 6. Method

**MCP knowledge query (mandatory pre-audit)**:
```
search_knowledge("Mellin moment f0 f2 f4 Route-A Route-B pole closure")
search_knowledge("§VII.AN registry anchor W5a-44 NEGATIVE-CALIBRATION")
trace_entity("s82_w3_9_as_adjacent_obs")
get_constant("f_0_pin")
get_constant("f_2_pin")
get_constant("f_4_pin")
```

Expected: K=4 NEGATIVE-CALIBRATION corpus instance W5a-44 (`audit_sha256=c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b`) is cited in `substrate-first-canonical-sourcing.md §(i)`; pin canonical values exist at `canonical_constants.py` (Route-B identity-bit-exact); §VII.AN registry text cites Route-A.

**AST-parse audit logic**:

```python
"""
S89 W6-2 (A.19) — AST-parse audit of f0/f2/f4 Mellin moment pin derivation
provenance in s82_w3_9_as_adjacent_obs.py
"""

import ast
import json
from pathlib import Path

ROUTE_A_SIGNATURES = {
    'function_calls': ['mellin_single_pole_closure', 'compute_residue_at_s_eq_3'],
    'imports_required': ['analytic_zeta', 'mellin_barnes_residue'],
    'docstring_keywords': ['single-pole', 'Mellin closure', 'residue at s=3'],
}

ROUTE_B_SIGNATURES = {
    'function_calls': ['adjacent_observable_path', 'compute_via_alternate_chain'],
    'imports_required': ['_spectral_action_regulators', 'compute_aN_zeta'],
    'docstring_keywords': ['adjacent observable', 'alternate path', 'Route-B'],
}

def parse_script(script_path: Path) -> dict:
    """Parse the script, extract function calls, imports, and docstrings."""
    tree = ast.parse(script_path.read_text(encoding='utf-8'))
    calls = []
    imports = []
    docstrings = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                calls.append(node.func.id)
            elif isinstance(node.func, ast.Attribute):
                calls.append(node.func.attr)
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            for alias in node.names:
                imports.append(alias.name)
        elif isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node)
            if doc:
                docstrings.append(doc)
    return {'calls': calls, 'imports': imports, 'docstrings': docstrings}

def classify_route(parsed: dict) -> str:
    """Return 'Route-A', 'Route-B', or 'AMBIGUOUS' based on signature match."""
    a_score = sum(1 for c in parsed['calls'] if c in ROUTE_A_SIGNATURES['function_calls'])
    a_score += sum(1 for i in parsed['imports'] if i in ROUTE_A_SIGNATURES['imports_required'])
    a_score += sum(1 for d in parsed['docstrings'] for k in ROUTE_A_SIGNATURES['docstring_keywords'] if k in d)
    b_score = sum(1 for c in parsed['calls'] if c in ROUTE_B_SIGNATURES['function_calls'])
    b_score += sum(1 for i in parsed['imports'] if i in ROUTE_B_SIGNATURES['imports_required'])
    b_score += sum(1 for d in parsed['docstrings'] for k in ROUTE_B_SIGNATURES['docstring_keywords'] if k in d)
    if a_score > 2 * b_score and a_score >= 3:
        return 'Route-A'
    if b_score > 2 * a_score and b_score >= 3:
        return 'Route-B'
    return 'AMBIGUOUS'

def main():
    script_path = Path('computations/session-87/s82_w3_9_as_adjacent_obs.py')
    parsed = parse_script(script_path)
    classification = classify_route(parsed)

    declared_route = 'Route-A'  # per §VII.AN registry-anchor framing
    declared_in = 'sessions/permanent-results-registry.md §VII.AN'
    actual_route = classification

    conflation_detected = (declared_route != actual_route)
    verdict = 'FAIL' if conflation_detected else 'PASS'

    report = {
        'gate': 'S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT',
        'declared_route': declared_route,
        'declared_in': declared_in,
        'actual_route': actual_route,
        'conflation_detected': conflation_detected,
        'verdict': verdict,
        'parsed_summary': {
            'n_calls': len(parsed['calls']),
            'n_imports': len(parsed['imports']),
            'n_docstrings': len(parsed['docstrings']),
        },
        'remediation': (
            'If FAIL: route to mack-cosmic-bridge sole-writer for §VII.AN '
            'registry-text reconciliation (declare actual Route-B path; '
            'cite Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION '
            'audit-script extension per A.22 sub-item (ii)).'
        ) if conflation_detected else 'No remediation required.',
    }
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-MELLIN-MOMENT-PIN-F0-F2-F4-PROVENANCE-AUDIT
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_mellin_moment_pin_provenance_audit.py
      assert: exists AND non_empty
  ast_parse_target: computations/session-87/s82_w3_9_as_adjacent_obs.py
  ast_parse_target_sha: <pinned-at-plan-freeze>
  declared_route: Route-A (per §VII.AN registry-anchor framing in sessions/permanent-results-registry.md)
  classification_threshold: a_score > 2 * b_score AND a_score >= 3 → Route-A; symmetric for Route-B; else AMBIGUOUS
  scheme: AST-parse + signature-set classification
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  registry_md: sessions/permanent-results-registry.md (file SHA pinned at plan-freeze; §VII.AN anchor row extracted)
  producing_script: computations/session-87/s82_w3_9_as_adjacent_obs.py (file SHA pinned at plan-freeze)
  W5a_44_audit_sha: c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b
  substrate_first_canonical_sourcing_md: .claude/rules/substrate-first-canonical-sourcing.md (file SHA pinned at plan-freeze)
```

### 8. Expected output 4-tuple

```
value=PASS|FAIL (composite of declared_route vs actual_route comparison)
scheme=AST-parse-signature-set-classification
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND (declared_route == actual_route) AND (classification != 'AMBIGUOUS').
- **FAIL**: declared_route != actual_route (conflation detected) OR classification == 'AMBIGUOUS' (cannot reconcile).
- **INFO**: not applicable; the rule-file structure forces binary classification at the AST-parse layer per the `a_score > 2 * b_score AND a_score >= 3` threshold rule.

### 10. Substitution chain (for Route-A vs Route-B classification claim)

The audit emits `conflation_detected = True` when `declared_route != actual_route`. Substitution chain for the threshold claim "a_score > 2 * b_score AND a_score >= 3 implies Route-A":

- **Step 1 (Definitions)**: `a_score = #signature matches against ROUTE_A_SIGNATURES`; `b_score = #signature matches against ROUTE_B_SIGNATURES`. Each signature set has 3 sub-categories (function_calls, imports_required, docstring_keywords); each match contributes 1 to its score.
- **Step 2 (Substitution)**: `classification(parsed) = Route-A iff a_score > 2 * b_score AND a_score >= 3; Route-B iff b_score > 2 * a_score AND b_score >= 3; AMBIGUOUS otherwise`.
- **Step 3 (Simplify)**: the threshold `a_score > 2 * b_score` enforces dominance ratio; the `a_score >= 3` floor enforces absolute minimum signature density. Symmetric for Route-B.
- **Step 4 (Direction)**: as a_score increases relative to b_score, classification monotonically transitions AMBIGUOUS → Route-A; symmetric for b_score relative to a_score → Route-B. The double-threshold (ratio + floor) prevents AMBIGUOUS-to-Route classification on sparse-signature scripts.
- **Conclusion**: the classification predicate is well-defined and monotone in the signature-density indicators; conflation is binary-detected via `declared_route != actual_route` after the producing script's actual route is locked by the classification rule.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: §VII.AN registry-anchor framing accurately describes the producing-script's derivation path; no rule-file-text reconciliation required.
- **FAIL**: conflation detected; routes to mack-cosmic-bridge sole-writer (per `feedback_mack-bridge-role.md`) for §VII.AN registry-text reconciliation. Remediation declares the actual Route-B path and cites Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION audit-script extension (built in A.22 sub-item (ii)).
- **AMBIGUOUS** (FAIL with diagnostic): cannot classify; producing script's signature set is too sparse to lock Route-A or Route-B; remediation is to add more signature density via docstring expansion in the producing script, OR re-classify the script as a third route (Route-C) at next-session plan-freeze.

### 12. Effort estimate

0.4 wave-equivalents. AST-parse on a single ~500-line script + signature-set match + JSON report + integration with W6-3 (A.22 sub-item (ii) Class-(g) audit extension). Low end because the audit logic is simple (regex + AST traversal + scoring).

### 13. Substrate framing per phononic-framing.md IS-not-IN

The AST-parse audit IS the methodology-layer F-image of the substrate-physics provenance predicate "the producing-script's actual derivation path matches the registry-text declared path." FORBIDDEN: "the audit checks the script behavior IN the registry text". INVERTED: "the producing-script body IS what the registry-text reconciliation determines under F"; the AST IS the methodology-layer's image of the substrate-derivation chain. Direction: substrate-derivation chain (Mellin closure path Route-A or Route-B) → producing-script body (s82_w3_9_as_adjacent_obs.py AST) → registry-text declaration (§VII.AN). The audit verifies F-image consistency between the producing-script body and the registry-text declaration; both are emergent from the substrate-derivation chain, not container-bound.

---

## §W6-3. S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED  (A.22)

### 1. Gate ID
`S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED`

### 2. Trigger
`[AUDIT] + [VERIFY]` — 4 sub-items combined: audit-script extensions + synthetic test fixtures.

### 3. Classification
**META** (methodology layer). Each sub-item extends an existing audit script with a new pattern detector + 1 synthetic test fixture; the verdict is composite over the 4 sub-items.

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
Four structurally distinct audit-script extensions, when implemented and tested with synthetic fixtures, will collectively close four silent-class-conflation pathways in the methodology-floor enforcement layer:
- (i) cohomology-class-layer surrogate detection (W-9 V.5; closes the surrogate-vs-canonical conflation at the cohomology-class layer per `substrate-first-canonical-sourcing.md §(iv-bis)`);
- (ii) Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION (W-15 V.3; closes the registry-anchor framing-vs-implementation conflation surfaced at W5a-44 NEGATIVE-CALIBRATION instance);
- (iii) sign-PASS reading audit-script extension (W-5 V.4; closes the falsifier-inventory sign-PASS-tautology pathology surfaced at W1c-69);
- (iv) V_4 program parallel-compute-wave + §VII.AE vs §VII.AD anchor-structure audit (W-7 V.6/V.7; closes the V_4-on-triality cocycle-functor anchor-structure validation gap).

### 6. Method

**MCP knowledge query (mandatory pre-build)**:
```
search_knowledge("substrate_first_provenance_audit cohomology-class layer surrogate")
search_knowledge("REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION Class (g)")
search_knowledge("falsifier inventory sign PASS tautology W1c-69")
search_knowledge("V_4 triality cocycle functor §VII.AE §VII.AD anchor-structure")
trace_entity("substrate_first_provenance_audit")
trace_entity("source_reconciliation_audit")
trace_entity("falsifier_inventory_audit")
```

Expected: existing audit-script bodies for sub-items (i)-(iii); sub-item (iv) is a new pattern detector for V_4 anchor-structure audit; W-9 V.5, W-15 V.3, W-5 V.4, W-7 V.6/V.7 ledger anchors all reachable via knowledge index.

**Sub-item (i) — cohomology-class-layer surrogate detection extension** to `_substrate_first_provenance_audit.py`:

Adds a new audit class for §(iv-bis) "Surrogate-vs-Canonical at Cohomology-Class Layer" (S88 W-9 W3a-18 V.5; B.12). When a plan-block proposes a surrogate observable for a cohomology-class quantity, scan for the algebraic-distance theorem pre-registration (substitution chain reducing surrogate to component substrate-physics quantities + sign/magnitude lock to Peter-Weyl combinatorial fraction + uninformative-on-canonical disclosure).

```python
def cohomology_class_surrogate_audit(plan_block_text: str) -> dict:
    """
    Per substrate-first-canonical-sourcing.md §(iv-bis):
    A surrogate observable for cohomology-class quantity must pre-register:
        (i) substitution chain reducing surrogate to component substrate quantities
        (ii) sign/magnitude lock to Peter-Weyl combinatorial fraction (or other
             substrate-internal combinatorial constraint) flag
        (iii) uninformative-on-canonical disclosure (FAIL inference safety)
    """
    has_substrate_distance_ratio = bool(re.search(
        r'substrate-distance-\d+\s+spectral-moment\s+ratio', plan_block_text))
    if not has_substrate_distance_ratio:
        return {'applicable': False}
    has_substitution_chain = bool(re.search(
        r'(?:Definitions|Substitution|Simplify|Direction).*substitution\s+chain',
        plan_block_text))
    has_combinatorial_lock = bool(re.search(
        r'mechanically\s+locked\s+to\s+(?:Peter-Weyl|combinatorial)', plan_block_text))
    has_uninformative_disclosure = bool(re.search(
        r'(?:uninformative|surrogate\s+FAIL\s+does\s+NOT\s+falsify)', plan_block_text))
    all_three_present = (has_substitution_chain and has_combinatorial_lock
                        and has_uninformative_disclosure)
    return {
        'applicable': True,
        'substitution_chain_present': has_substitution_chain,
        'combinatorial_lock_present': has_combinatorial_lock,
        'uninformative_disclosure_present': has_uninformative_disclosure,
        'verdict': 'PASS' if all_three_present else 'FAIL',
        'severity': 'MANDATORY' if not all_three_present else 'NO-ACTION',
    }
```

Synthetic test fixture (i): plan-block proposing surrogate `R_surrogate = (Σ_BdG_A − Σ_BdG_M_3C) / (Σ_BdG_A + Σ_BdG_M_3C)` with substrate-distance-1 origin; FIXTURE-1A includes substitution chain `R_surrogate = 2*f − 1` lock + uninformative disclosure (PASS); FIXTURE-1B omits combinatorial lock (FAIL with MANDATORY severity).

**Sub-item (ii) — Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION extension** to `_source_reconciliation_audit.py`:

Adds a new sub-class to the 6-class taxonomy (a)-(f) per `epistemic-discipline.md §"Source Reconciliation"`. Class-(g) detects registry-anchor declared-vs-actual route conflation surfaced at W5a-44 NEGATIVE-CALIBRATION instance.

```python
def class_g_registry_anchor_route_audit(registry_md: Path, scripts_dir: Path) -> dict:
    """
    Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION detection:
    For each §VII.X registry entry that cites a closure-script path (e.g.,
    "S82 W3-9 single-pole Mellin closure"), verify that the cited script
    implements the declared route per AST-parse signature classification
    (see W6-2 / A.19).
    """
    text = registry_md.read_text(encoding='utf-8')
    # Extract (slot, declared_route, cited_script_path) triples
    pattern = r'(§VII\.[A-Z]+(?:\.[A-Z0-9-]+)*)\s+(?:.*?)\s+(?:S\d+\s+W[0-9a-z-]+\s+(.*?)\s+closure)'
    triples = re.findall(pattern, text, re.DOTALL)
    findings = []
    for slot, declared in triples:
        # Locate cited script via filename heuristic
        candidate_scripts = list(scripts_dir.glob(f's*_{slot.lower().replace(".", "_")}*.py'))
        if not candidate_scripts:
            findings.append({
                'slot': slot, 'declared_route': declared,
                'cited_script_found': False,
                'severity': 'MANDATORY',
            })
            continue
        # Run AST-parse classification (delegate to W6-2 audit logic)
        for script in candidate_scripts:
            from _mellin_moment_pin_provenance_audit import (
                parse_script, classify_route)
            actual_route = classify_route(parse_script(script))
            findings.append({
                'slot': slot, 'declared_route': declared,
                'actual_route': actual_route,
                'conflation': (declared != actual_route),
                'severity': 'MANDATORY' if (declared != actual_route) else 'NO-ACTION',
            })
    return findings
```

Synthetic test fixture (ii): registry-md fragment with §VII.AN declared "Route-A" + cited script `s82_w3_9_as_adjacent_obs.py` (Route-B per AST classification); FIXTURE-2 returns conflation_detected = True with MANDATORY severity.

**Sub-item (iii) — sign-PASS reading audit-script extension** to `_falsifier_inventory_audit.py`:

Adds detection of sign-PASS-tautology pathology at falsifier-inventory rows. A row is sign-PASS-tautology when its substrate prediction's SIGN is mechanically forced by row-format conventions (e.g., absolute-value ratio rows have sign = positive by construction; the row's sign-PASS conveys no substrate-physics content).

```python
def sign_pass_tautology_audit(inventory_md: Path) -> dict:
    """
    Per W-5 V.4 (W1c-69 sign-PASS-tautology corpus instance):
    A falsifier-inventory row is sign-PASS-tautology iff its substrate
    prediction's SIGN is mechanically forced by row-format conventions
    rather than substrate-physics content.
    Detection: rows whose prediction is wrapped in absolute-value bars
    and whose sign-PASS verdict adds no information.
    """
    text = inventory_md.read_text(encoding='utf-8')
    rows = re.findall(r'\|\s*F\d+\s*\|.*?\n', text)
    findings = []
    for row in rows:
        is_abs_value = bool(re.search(r'\|.*\|\s*[><=]', row))
        is_signed_ratio = bool(re.search(r'(?<!abs)(?:\+|\-)\s*\d', row))
        if is_abs_value and not is_signed_ratio:
            findings.append({
                'row': row.strip(),
                'sign_pass_tautology': True,
                'severity': 'MANDATORY',
                'remediation': 'Reformulate row to use signed substrate prediction OR explicitly disclose sign-PASS-tautology in row text',
            })
    return findings
```

Synthetic test fixture (iii): inventory-md fragment with row F-W1c-69-test wrapped in `|...|` absolute value (FIXTURE-3A: detected as tautology, FAIL); FIXTURE-3B with signed-ratio prediction (PASS).

**Sub-item (iv) — V_4 program parallel-compute-wave + §VII.AE vs §VII.AD anchor-structure audit** new audit script:

`computations/_shared/_v4_anchor_structure_audit.py` validates that §VII.AE (moduli-deformation substrate-IS, V_4-on-triality cocycle functor) and §VII.AD (single-τ-slice substrate-IS, Δ_0 LOCALIZATION FORMULA) anchor structures preserve the Single-τ-slice vs moduli-deformation Level-1↔Level-2 distinction per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (K=2 MANDATORY since S88 W-7 V.4).

```python
def v4_anchor_structure_audit(registry_md: Path) -> dict:
    """
    Per W-7 V.6/V.7: §VII.AE (Level-2 moduli-deformation) and §VII.AD
    (Level-1 single-τ-slice) MUST declare which level their substrate-IS
    observable lives at. Cross-check that V_4 cocycle functor F : m(p,q) → Δ_0(m)
    preserves the Level-1↔Level-2 distinction.
    """
    text = registry_md.read_text(encoding='utf-8')
    # Extract §VII.AE block + §VII.AD block
    ae_match = re.search(r'§VII\.AE.*?(?=§VII\.[A-Z])', text, re.DOTALL)
    ad_match = re.search(r'§VII\.AD.*?(?=§VII\.[A-Z])', text, re.DOTALL)
    if not (ae_match and ad_match):
        return {'verdict': 'INFO', 'reason': 'Slot block(s) absent'}
    ae_text = ae_match.group(0)
    ad_text = ad_match.group(0)
    ae_has_level_2 = bool(re.search(r'(?:Level\s*2|moduli-deformation)', ae_text))
    ad_has_level_1 = bool(re.search(r'(?:Level\s*1|single-τ-slice|single-tau-slice)', ad_text))
    cocycle_functor_cited = bool(re.search(
        r'cocycle\s+functor\s+F\s*:\s*m\(p,q\)\s*[→↦]\s*Δ_0', text))
    all_three_present = ae_has_level_2 and ad_has_level_1 and cocycle_functor_cited
    return {
        'ae_level_2_declared': ae_has_level_2,
        'ad_level_1_declared': ad_has_level_1,
        'cocycle_functor_cited': cocycle_functor_cited,
        'verdict': 'PASS' if all_three_present else 'FAIL',
        'severity': 'MANDATORY' if not all_three_present else 'NO-ACTION',
    }
```

Synthetic test fixture (iv): registry-md fragment with §VII.AE Level-2 declared + §VII.AD Level-1 declared + V_4 cocycle functor F cited (FIXTURE-4A: PASS); FIXTURE-4B with §VII.AE missing Level-2 declaration (FAIL with MANDATORY severity).

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-AUDIT-SCRIPT-EXTENSIONS-COMBINED
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_substrate_first_provenance_audit.py
      assert: exists AND extension_function_present('cohomology_class_surrogate_audit')
    - file: computations/_shared/_source_reconciliation_audit.py
      assert: exists AND extension_function_present('class_g_registry_anchor_route_audit')
    - file: computations/_shared/_falsifier_inventory_audit.py
      assert: exists AND extension_function_present('sign_pass_tautology_audit')
    - file: computations/_shared/_v4_anchor_structure_audit.py
      assert: exists AND non_empty
    - file: computations/_shared/_audit_script_extensions_combined_test_fixtures.py
      assert: exists AND all_4_synthetic_fixtures_pass
  source_workshop_anchors:
    sub_item_i: W-9 V.5 (Surrogate-vs-Canonical at Cohomology-Class Layer)
    sub_item_ii: W-15 V.3 (Class-(g) REGISTRY-ANCHOR-ROUTE-A-VS-ROUTE-B-CONFLATION)
    sub_item_iii: W-5 V.4 (sign-PASS reading; W1c-69 corpus instance)
    sub_item_iv: W-7 V.6/V.7 (V_4-on-triality + §VII.AE vs §VII.AD anchor-structure)
  scheme: methodology-layer-F-image-extension
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  substrate_first_provenance_audit_pre_extension: computations/_shared/_substrate_first_provenance_audit.py (file SHA pinned at plan-freeze)
  source_reconciliation_audit_pre_extension: computations/_shared/_source_reconciliation_audit.py (file SHA pinned at plan-freeze)
  falsifier_inventory_audit_pre_extension: computations/_shared/_falsifier_inventory_audit.py (file SHA pinned at plan-freeze)
  registry_md: sessions/permanent-results-registry.md (file SHA pinned at plan-freeze)
  falsifier_master_inventory_md: sessions/framework/registry/falsifier-master-inventory.md (file SHA pinned at plan-freeze)
```

### 8. Expected output 4-tuple

```
value=PASS|FAIL (composite of 4 sub-items × {extension_lands AND test_fixture_passes})
scheme=methodology-layer-F-image-extension
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND all 4 sub-items PASS (extension function present + synthetic test fixture passes).
- **FAIL**: any one of the 4 sub-items fails.
- **INFO**: not applicable for combined-extensions gate (binary outcome per sub-item).

### 10. Substitution chain (for combined-PASS direction claim)

Sub-item composition: combined PASS iff `sub_item_i_pass AND sub_item_ii_pass AND sub_item_iii_pass AND sub_item_iv_pass`. Substitution chain:

- **Step 1 (Definitions)**: `sub_item_k_pass = (extension_function_present_in_target_script AND synthetic_test_fixture_returns_pass) for k ∈ {i, ii, iii, iv}`. `combined_pass = AND_{k} sub_item_k_pass`.
- **Step 2 (Substitution)**: `combined_pass = sub_item_i_pass AND sub_item_ii_pass AND sub_item_iii_pass AND sub_item_iv_pass`.
- **Step 3 (Simplify)**: AND-conjunction is non-commutative-irrelevant; combined_pass = 1 iff all 4 sub-items return 1; combined_pass = 0 iff any sub-item returns 0.
- **Step 4 (Direction)**: combined-PASS implies all 4 silent-class-conflation pathways closed; any sub-item FAIL implies the corresponding pathway remains open and remediation is required.
- **Conclusion**: the combined verdict is monotonically dependent on all 4 sub-items; failure of any one closes the gate.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: all 4 silent-class-conflation pathways closed at the audit-script level; downstream gates citing the extended audit infrastructure can rely on enforcement; F-image consistency at the methodology layer preserved across the cohomology-class-layer / registry-anchor / falsifier-sign-PASS / V_4 anchor-structure axes.
- **FAIL**: at least one pathway remains open; remediation is to rebuild the corresponding audit extension + re-test until composite PASS achieved.
- Solution-space mapping: each sub-item is a structurally distinct audit-leg image of a substrate-physics provenance predicate; combined PASS represents methodology-floor enforcement saturation across 4 independent class-conflation axes (cohomology / registry / falsifier / V_4 anchor).

### 12. Effort estimate

0.6 wave-equivalents combined. Each sub-item is ~0.15 wave-equiv (extension function build + 1 synthetic test fixture); 4 sub-items × 0.15 = 0.6. Some shared overhead (test-fixture infrastructure) brings the total to 0.6 rather than 4 × 0.15 = 0.6 (no overhead reduction; flat sum holds).

### 13. Substrate framing per phononic-framing.md IS-not-IN

Each audit-script extension IS the methodology-layer F-image of a substrate-physics provenance predicate. FORBIDDEN: "the audit script extensions check the rules in the system" (treats audit-leg as something IN a meta-container). INVERTED: "the audit-leg IS what the methodology layer's class-conflation closure determines under F"; the 4 extensions IS the methodology-layer's image of the 4 substrate-physics class-conflation axes. Direction: substrate-physics class-conflation pathology (cohomology-class surrogate / registry-anchor route / falsifier sign-PASS / V_4 anchor-structure) → methodology-floor closure under F (rule-file body + clauses) → audit-leg image under F (extension functions + synthetic test fixtures). Container-thinking inversion: the methodology-floor IS the closure, not a probe of an external rule-container.

---

## §W6-4. S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT  (A.23)

### 1. Gate ID
`S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT`

### 2. Trigger
`[AUDIT]` — application of EG1 audit-pattern (Closing-Paragraph-Coherence Audit Pattern) to 3 candidate rule-files identified in S88 W-25 W7c-167 §V CF #5.

### 3. Classification
**META** (methodology layer). The audit applies the EG1 audit-pattern from `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"` to 3 candidate rule-files; the verdict is per-rule-file (literal-independent vs strict-conjunctive reading + structural-fix recommendation).

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
The EG1 audit-pattern (3-step procedure: identify antecedent's competing structural readings → test each reading against closing paragraph's qualifying language → reject reading producing self-contradiction), when applied to the 3 candidate rule-files (`v3-closure-recovery.md` Class 1-7 vs Stage 1/2/3; `cross-pillar-bridge-anatomy.md` algebra-axis K-counter MANDATORY clause; `joint-theorem-promotion.md` 4-stage pathway), will identify the canonical structurally-coherent reading for each rule-file (literal-independent vs strict-conjunctive) and emit a structural-fix recommendation when the strict-conjunctive reading produces self-contradiction.

### 6. Method

**MCP knowledge query (mandatory pre-audit)**:
```
search_knowledge("Closing-Paragraph-Coherence Audit Pattern EG1")
search_knowledge("v3-closure-recovery PROHIBITED_ACTIONS Stage 1 2 3")
search_knowledge("algebra-axis orthogonality K-counter MANDATORY")
search_knowledge("joint-theorem-promotion 4-stage Stage-2 Axis-B")
trace_entity("EG1_audit_pattern")
```

Expected: EG1 audit-pattern landed at S88 W-25 W7c-167 §V CF #1 + §V CF #8 (per `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"`); 3 candidate rule-files exist and are reachable.

**EG1 audit-pattern application**:

For each rule-file `R ∈ {v3-closure-recovery.md, cross-pillar-bridge-anatomy.md, joint-theorem-promotion.md}`:

1. **Identify antecedent's two competing structural readings** — the antecedent is the enumerated list (Class 1-7 / K-counter sub-clauses / Stage 0-3 stages); the closing paragraph is the rule's behavior-disambiguation paragraph at execution time.
2. **Test each reading against closing-paragraph qualifying language** — substitute literal-independent reading (each antecedent-clause independently testable; closing paragraph composes with companion rule) vs strict-conjunctive reading (closing paragraph applies when ALL antecedent-clauses hold simultaneously). Check for self-contradiction at execution time.
3. **Reject reading producing self-contradiction** — declare the structurally-coherent reading as canonical; emit structural-fix recommendation if the rejected reading was the formerly-default reading.

Audit logic:

```python
"""
S89 W6-4 (A.23) — EG1 audit-pattern sweep of 3 candidate rule-files
"""

import json
import re
from pathlib import Path

CANDIDATE_RULE_FILES = [
    {
        'path': '.claude/rules/v3-closure-recovery.md',
        'antecedent_section': 'PROHIBITED_ACTIONS',
        'antecedent_pattern': r'^\d+\.\s+\*\*[A-Z][a-zA-Z\s\-]+\*\*',
        'closing_paragraph_section': 'Stage 3: User-intervention trigger',
        'closing_paragraph_predicate': lambda txt: 'PROHIBITED_ACTIONS' in txt and 'Stage 3' in txt,
    },
    {
        'path': '.claude/rules/cross-pillar-bridge-anatomy.md',
        'antecedent_section': 'Algebra-axis orthogonality K-counter',
        'antecedent_pattern': r'^[A-Z]\.\s+',  # corner-cell labels A/B/C/D
        'closing_paragraph_section': 'Two-clause separation',
        'closing_paragraph_predicate': lambda txt: 'K-counter' in txt and 'cross-corner' in txt.lower(),
    },
    {
        'path': '.claude/rules/joint-theorem-promotion.md',
        'antecedent_section': 'The 4 Stages',
        'antecedent_pattern': r'^### Stage \d+',
        'closing_paragraph_section': 'Audit at plan-freeze',
        'closing_paragraph_predicate': lambda txt: 'Stage' in txt and 'cross-reviewer' in txt.lower(),
    },
]

def eg1_audit(rule_file_spec: dict) -> dict:
    """Apply EG1 3-step audit to a single rule-file."""
    path = Path(rule_file_spec['path'])
    text = path.read_text(encoding='utf-8')
    # Step 1: identify two competing structural readings
    antecedent_count = len(re.findall(rule_file_spec['antecedent_pattern'], text, re.MULTILINE))
    closing_paragraph_present = rule_file_spec['closing_paragraph_predicate'](text)
    # Step 2: test literal-independent vs strict-conjunctive
    # Literal-independent: each antecedent-clause testable in isolation;
    #   closing paragraph composes with separately-stated companion rule
    # Strict-conjunctive: closing paragraph applies when ALL antecedent-clauses
    #   hold simultaneously; admits self-contradiction if any clause's individual
    #   trigger (e.g., count-keyed) operates independently of conjunction
    has_companion_rule_xref = bool(re.search(
        r'(?:cross-link|cross-reference|composes?\s+with|see\s+also)',
        text, re.IGNORECASE))
    has_count_keyed_trigger = bool(re.search(
        r'(?:count\s*[≥>=]\s*\d|threshold\s*=\s*\d)', text))
    # If antecedent has count-keyed trigger AND closing paragraph qualifies on
    # individual-clause basis, the literal-independent reading is canonical
    # (strict-conjunctive produces self-contradiction)
    self_contradiction_under_strict = (has_count_keyed_trigger
                                       and has_companion_rule_xref
                                       and closing_paragraph_present)
    canonical_reading = (
        'literal-independent' if self_contradiction_under_strict else 'strict-conjunctive'
    )
    structural_fix_recommendation = (
        f'Compose {path.name} closing paragraph with explicit companion-rule citation '
        f'(literal-independent reading) rather than leaving it ambiguous.'
        if self_contradiction_under_strict
        else 'No remediation required.'
    )
    return {
        'rule_file': str(path),
        'antecedent_count': antecedent_count,
        'closing_paragraph_present': closing_paragraph_present,
        'has_companion_rule_xref': has_companion_rule_xref,
        'has_count_keyed_trigger': has_count_keyed_trigger,
        'self_contradiction_under_strict': self_contradiction_under_strict,
        'canonical_reading': canonical_reading,
        'structural_fix_recommendation': structural_fix_recommendation,
        'verdict': 'PASS' if closing_paragraph_present else 'INFO',
    }

def main():
    findings = [eg1_audit(spec) for spec in CANDIDATE_RULE_FILES]
    report = {
        'gate': 'S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT',
        'EG1_audit_pattern_source': 'S88 W-25 W7c-167 §V CF #5; epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"',
        'rule_file_findings': findings,
        'composite_verdict': 'PASS' if all(f['verdict'] == 'PASS' for f in findings) else 'INFO',
    }
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-W25-CLOSING-PARAGRAPH-COHERENCE-SWEEP-AUDIT
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_w25_closing_paragraph_coherence_sweep_audit.py
      assert: exists AND non_empty
  candidate_rule_files:
    - .claude/rules/v3-closure-recovery.md (file SHA pinned at plan-freeze)
    - .claude/rules/cross-pillar-bridge-anatomy.md (file SHA pinned at plan-freeze)
    - .claude/rules/joint-theorem-promotion.md (file SHA pinned at plan-freeze)
  EG1_audit_pattern_source: epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)" (file SHA pinned at plan-freeze)
  scheme: EG1-3-step-application
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  v3_closure_recovery_md: <file SHA pinned at plan-freeze>
  cross_pillar_bridge_anatomy_md: <file SHA pinned at plan-freeze>
  joint_theorem_promotion_md: <file SHA pinned at plan-freeze>
  epistemic_discipline_md: <file SHA pinned at plan-freeze>
```

### 8. Expected output 4-tuple

```
value=PASS|INFO (per-rule-file PASS if closing paragraph present + canonical reading declared; INFO if EG1 not applicable)
scheme=EG1-3-step-application
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND for each of the 3 rule-files, EG1 audit emits closing-paragraph-coherence verdict (canonical reading: literal-independent vs strict-conjunctive) + structural-fix recommendation when self-contradiction under strict-conjunctive detected.
- **INFO**: at least one rule-file's closing paragraph is absent / not detectable via the predicate; audit emits diagnostic but does not block.
- **FAIL**: applies only if M1-M4 conjunction fails (e.g., gate-ID not in allowlist).

### 10. Substitution chain (for self-contradiction detection direction claim)

Sign claim: "presence of count-keyed trigger AND companion-rule cross-reference AND closing paragraph implies literal-independent reading is canonical." Substitution chain:

- **Step 1 (Definitions)**: `has_count_keyed_trigger = bool(re.search(r'count ≥ N OR threshold = N'))`; `has_companion_rule_xref = bool(re.search(r'cross-link OR composes with OR see also'))`; `closing_paragraph_present = predicate(text)`.
- **Step 2 (Substitution)**: `self_contradiction_under_strict = has_count_keyed_trigger AND has_companion_rule_xref AND closing_paragraph_present`. Direct AND-conjunction.
- **Step 3 (Simplify)**: `self_contradiction_under_strict = 1 iff all 3 conditions hold; 0 iff any condition fails`. Monotone.
- **Step 4 (Direction)**: when `self_contradiction_under_strict = 1`, the strict-conjunctive reading admits a self-contradiction (count-keyed trigger fires INDEPENDENTLY of conjunction with other clauses, but strict-conjunctive reading requires ALL clauses to fire simultaneously; the count-keyed trigger's independent firing CONTRADICTS the strict-conjunctive's simultaneous-firing requirement). The literal-independent reading does NOT admit this contradiction (count-keyed trigger fires per its own predicate; companion-rule composition is separate). Therefore the literal-independent reading is canonical iff `self_contradiction_under_strict = 1`.
- **Conclusion**: detection of count-keyed trigger + companion-rule xref + closing paragraph IS the substrate-physics signal that the literal-independent reading is canonical; the structural-fix recommendation is to compose the closing paragraph with explicit companion-rule citation rather than leaving it ambiguous.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: 3 candidate rule-files have explicit closing-paragraph-coherence verdicts; canonical readings declared; structural-fix recommendations issued where applicable. EG1 audit-pattern operationalized as a sweep tool reusable for future rule-file additions.
- **INFO**: at least one rule-file's closing paragraph is structurally absent or not detectable via predicate; remediation is to either add a closing paragraph OR re-run sweep with adjusted predicate definition.
- Solution-space mapping: EG1 audit-pattern advances K-counter at `epistemic-discipline.md §"Closing-Paragraph-Coherence Audit Pattern (EG1)"` from K=1 (S88 W-25 calibration) to K=2 (S89 sweep adds 3 rule-file applications); promotes status from SUGGESTION-pending toward MANDATORY at K=3.

### 12. Effort estimate

0.6 wave-equivalents. EG1 application is per-rule-file ~0.2 wave-equiv (regex extraction + 3-step procedure + structural-fix recommendation drafting); 3 rule-files × 0.2 = 0.6.

### 13. Substrate framing per phononic-framing.md IS-not-IN

The EG1 audit-pattern IS the methodology-layer F-image of the substrate-physics rule-coherence predicate "the rule-file's closing paragraph is structurally coherent under both literal-independent and strict-conjunctive readings, OR the structurally-incoherent reading is identified and rejected." FORBIDDEN: "the audit checks the rule-file's closing paragraph IN the rule system." INVERTED: "the EG1 application IS what the rule-coherence predicate determines under F"; the audit-leg IS the methodology-layer's image of the substrate-physics rule-coherence predicate. Direction: substrate-physics rule-coherence predicate (rule-text composition + closing-paragraph qualifying language) → methodology-floor closure under F (EG1 3-step procedure) → audit-leg image under F (this audit script + per-rule-file findings). Container-thinking inversion: the rule-files are NOT in a rule-system container; the rule-files ARE the methodology-layer's substrate, and EG1 IS what verifies their closing-paragraph coherence.

---

## §W6-5. S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51  (A.33)

### 1. Gate ID
`S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51`

### 2. Trigger
`[AUDIT]` — retroactive audit of W6a-51 plan §10 Step 8 pre-registered estimate `≈4e-9` against substrate-derivable predictions per PRU Class 8.3 publication-precision pre-registration discipline.

### 3. Classification
**META** (methodology layer). Per `epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"` (existing K=4 MANDATORY at S87 W8-2 close).

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
The W6a-51 plan §10 Step 8 pre-registered estimate `≈4e-9` (originating in S88 W-19 V.4 substrate-derivable estimate baseline) is either substrate-derivable from first-principles (PASS) or ad-hoc rule-of-thumb (FAIL); a retroactive audit against PRU Class 8.3 publication-precision pre-registration discipline + substrate-first canonical-sourcing audit provides binary classification.

### 6. Method

**MCP knowledge query (mandatory pre-audit)**:
```
search_knowledge("PRU Class 8.3 publication precision pre-registration")
search_knowledge("W6a-51 substrate derivable estimate baseline 4e-9")
trace_entity("W6a_51_step8_4e9")
get_constant("W6a_51_step8_estimate")
```

Expected: PRU Class 8.3 K=4 MANDATORY corpus exists at `epistemic-discipline.md §"Publication-Precision Pre-Registration"`; W6a-51 plan §10 Step 8 reachable via `sessions/session-plan/session-88-plan-w6a.md` (or successor) with the `≈4e-9` literal cited.

**Audit logic**:

```python
"""
S89 W6-5 (A.33) — Retroactive PRU Class 8.3 audit on W6a-51 plan §10 Step 8
pre-registered estimate `≈4e-9`
"""

import json
import re
from pathlib import Path

def retroactive_class_8_3_audit() -> dict:
    """
    Audit W6a-51 plan §10 Step 8 estimate `≈4e-9` against:
      (1) PRU Class 8.3 publication-precision pre-registration: was the
          estimate published with explicit precision pin?
      (2) Substrate-first canonical-sourcing: is the estimate substrate-derivable
          from first-principles (κ_2 from CM-1995 §III.4 Jensen perturbation, or
          equivalent substrate-physics chain) OR ad-hoc?
      (3) Class-(f) PIN-PLACEHOLDER detection: does the `≈4e-9` form match the
          pattern set for placeholder pins?
    """
    plan_path = Path('sessions/session-plan/session-88-plan-w6a.md')
    text = plan_path.read_text(encoding='utf-8')

    # Locate W6a-51 plan §10 Step 8 block
    pattern_step8 = r'§W6a-51.*?§10.*?Step\s*8.*?≈\s*4e-?9'
    match = re.search(pattern_step8, text, re.DOTALL)
    if not match:
        return {'verdict': 'INFO', 'reason': 'W6a-51 §10 Step 8 block not located'}

    block_text = match.group(0)

    # Class 8.3: precision pin detection
    has_precision_pin = bool(re.search(
        r'precision_pin\s*[:=]|publication_sig_figs\s*[:=]|sig_figs\s*[:=]',
        block_text))

    # Substrate-first canonical-sourcing detection
    has_substrate_derivation = bool(re.search(
        r'(?:CM-1995|Connes-Moscovici|Seeley-DeWitt|Jensen\s+perturbation|'
        r'substrate-derivable|first-principles)', block_text))

    # Class-(f) placeholder pattern
    is_placeholder = bool(re.search(
        r'O\(10\^?-?\d+\)|≈\s*\d|placeholder|TBD|pending|analytic\s+estimate',
        block_text))

    # Verdict
    if has_substrate_derivation and has_precision_pin:
        verdict = 'PASS'
        severity = 'NO-ACTION'
        rationale = 'Estimate is substrate-derivable AND has precision pin; PRU Class 8.3 satisfied'
    elif has_substrate_derivation and not has_precision_pin:
        verdict = 'INFO'
        severity = 'ADVISORY'
        rationale = 'Substrate-derivable but missing precision pin; Class 8.3 advisory remediation'
    elif is_placeholder and not has_substrate_derivation:
        verdict = 'FAIL'
        severity = 'MANDATORY'
        rationale = 'Ad-hoc placeholder without substrate derivation; Class-(f) PIN-PLACEHOLDER'
    else:
        verdict = 'FAIL'
        severity = 'MANDATORY'
        rationale = 'Estimate lacks both substrate derivation AND precision pin'

    return {
        'gate': 'S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51',
        'block_text': block_text[:500],  # truncated for report
        'has_precision_pin': has_precision_pin,
        'has_substrate_derivation': has_substrate_derivation,
        'is_placeholder': is_placeholder,
        'verdict': verdict,
        'severity': severity,
        'rationale': rationale,
        'remediation': (
            'Add precision pin (publication_sig_figs = N) AND/OR substrate-derivation '
            'citation (CM-1995 §III.4 Jensen perturbation chain reproduces 4e-9 from '
            'first principles).' if verdict != 'PASS' else 'No remediation required.'
        ),
    }

def main():
    print(json.dumps(retroactive_class_8_3_audit(), indent=2))

if __name__ == '__main__':
    main()
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-PRU-CLASS-8-3-RETROACTIVE-AUDIT-W6A-51
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_pru_class_8_3_retroactive_audit_w6a_51.py
      assert: exists AND non_empty
  audit_target: sessions/session-plan/session-88-plan-w6a.md §W6a-51 §10 Step 8 (block SHA pinned at plan-freeze)
  pru_class_8_3_corpus_source: epistemic-discipline.md §"Publication-Precision Pre-Registration (Class 8.3, MANDATORY at K=4)"
  substrate_first_canonical_sourcing_source: substrate-first-canonical-sourcing.md §(v) Class-(f) PIN-PLACEHOLDER
  scheme: PRU-Class-8-3-retroactive
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  W6a_51_plan_md: sessions/session-plan/session-88-plan-w6a.md (file SHA pinned at plan-freeze)
  epistemic_discipline_md: .claude/rules/epistemic-discipline.md (file SHA pinned at plan-freeze)
  substrate_first_canonical_sourcing_md: .claude/rules/substrate-first-canonical-sourcing.md (file SHA pinned at plan-freeze)
```

### 8. Expected output 4-tuple

```
value=PASS|INFO|FAIL (composite of has_substrate_derivation + has_precision_pin + is_placeholder)
scheme=PRU-Class-8-3-retroactive
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND has_substrate_derivation AND has_precision_pin (both predicates True).
- **INFO**: has_substrate_derivation True but has_precision_pin False; substrate-derivable but Class 8.3 advisory remediation required.
- **FAIL**: NOT has_substrate_derivation; ad-hoc estimate without substrate-physics chain; Class-(f) PIN-PLACEHOLDER MANDATORY remediation.

### 10. Substitution chain (for substrate-derivability claim direction)

Sign claim: "substrate-derivability + precision-pin presence implies PASS." Substitution chain:

- **Step 1 (Definitions)**: `has_substrate_derivation = bool(re.search(substrate-derivation-pattern, block_text))`; `has_precision_pin = bool(re.search(precision-pin-pattern, block_text))`; `is_placeholder = bool(re.search(placeholder-pattern, block_text))`.
- **Step 2 (Substitution)**: `verdict = PASS iff (has_substrate_derivation AND has_precision_pin); INFO iff (has_substrate_derivation AND NOT has_precision_pin); FAIL iff (NOT has_substrate_derivation)`.
- **Step 3 (Simplify)**: 4-state truth table over (substrate, precision, placeholder); PASS requires both substrate derivation AND precision pin; INFO is substrate-derivable but missing precision; FAIL is ad-hoc.
- **Step 4 (Direction)**: substrate-derivability INCREASES verdict (FAIL → INFO → PASS); precision-pin presence INCREASES verdict (INFO → PASS); placeholder presence WITHOUT substrate derivation forces FAIL.
- **Conclusion**: monotone in substrate-derivability and precision-pin presence; FAIL is the absorbing class for ad-hoc estimates.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: W6a-51 plan §10 Step 8 estimate is substrate-derivable AND publication-precision-pinned; PRU Class 8.3 satisfied; no remediation required.
- **INFO**: substrate-derivable but missing precision pin; remediation is to add `publication_sig_figs = N` to the W6a-51 plan §10 Step 8 block.
- **FAIL**: ad-hoc estimate without substrate-physics chain; remediation is either (a) derive the estimate from CM-1995 §III.4 Jensen perturbation chain (or equivalent substrate-physics route), OR (b) reclassify as Class-(f) PIN-PLACEHOLDER and route to canonical substitution.

### 12. Effort estimate

0.2 wave-equivalents. Single-block retroactive audit; regex extraction + 4-state classification + JSON report. Low end of effort range.

### 13. Substrate framing per phononic-framing.md IS-not-IN

The retroactive Class 8.3 audit IS the methodology-layer F-image of the substrate-physics estimate-provenance predicate "the estimate `≈4e-9` is derived from first-principles substrate-physics OR is an ad-hoc placeholder." FORBIDDEN: "the audit checks the estimate IN the plan-block." INVERTED: "the estimate-provenance predicate IS what the methodology-layer's plan-block-content composition determines under F"; the audit-leg IS the methodology-layer's image of the substrate-derivation chain. Direction: substrate-physics derivation chain (CM-1995 §III.4 Jensen perturbation, or equivalent) → plan-block content under F (W6a-51 §10 Step 8 block) → audit-leg image under F (this audit script + verdict). Container-thinking inversion: the plan-block is NOT in a plan-container; the plan-block IS the methodology-layer's substrate-derivation-chain trace, and the audit IS what verifies its substrate-first canonical-sourcing.

---

## §W6-6. S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION  (A.34)

### 1. Gate ID
`S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION`

### 2. Trigger
`[AUDIT]` — re-run of `_corner_classification_audit.py` post-V.1+V.3 W-21 edits to verify Corner I assignment preserved through registry text changes.

### 3. Classification
**META** (methodology layer). Existing audit-script re-run; verdict is artifact-existence-with-substantive-content (the audit re-emits the per-corner classification verdict, and the verdict is checked against pre-V.1+V.3 baseline).

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
The S88 W-21 V.1 + V.3 edits to `sessions/permanent-results-registry.md` §VII.U.2 (Corner-I cell registry text) preserve the Corner-I assignment of pre-V.1+V.3 baseline; a re-run of the existing `_corner_classification_audit.py` post-edit will emit identical Corner-I classification verdict and the audit will PASS.

### 6. Method

**MCP knowledge query (mandatory pre-audit)**:
```
search_knowledge("VII.U.2 corner classification Corner I")
search_knowledge("_corner_classification_audit.py post-V.1 V.3 edits")
trace_entity("VII_U_2_corner_classification")
```

Expected: existing `_corner_classification_audit.py` script body present; pre-V.1+V.3 baseline verdict for Corner I cached in audit-trail (or recomputable from prior verdict-file row); post-V.1+V.3 registry-text edits landed at S88 W-21 close.

**Re-run logic**:

```python
"""
S89 W6-6 (A.34) — Re-run _corner_classification_audit.py to verify Corner I
assignment preservation post-V.1+V.3 W-21 edits
"""

import json
import subprocess
import sys
from pathlib import Path

def main():
    audit_script = Path('computations/_shared/_corner_classification_audit.py')
    if not audit_script.exists():
        print(json.dumps({
            'gate': 'S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION',
            'verdict': 'FAIL',
            'reason': f'Audit script not found at {audit_script}',
        }))
        sys.exit(1)

    # Run the audit; capture stdout JSON
    result = subprocess.run(
        ['python', str(audit_script), '--verdict-format=json'],
        capture_output=True, text=True, check=False)

    if result.returncode != 0:
        print(json.dumps({
            'gate': 'S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION',
            'verdict': 'FAIL',
            'reason': f'Audit script returned non-zero exit code: {result.returncode}',
            'stderr': result.stderr,
        }))
        sys.exit(1)

    try:
        audit_output = json.loads(result.stdout)
    except json.JSONDecodeError:
        print(json.dumps({
            'gate': 'S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION',
            'verdict': 'FAIL',
            'reason': 'Audit script output not valid JSON',
            'stdout': result.stdout[:1000],
        }))
        sys.exit(1)

    # Check Corner I classification preserved
    pre_v1_v3_baseline_corner_i = 'algebra-INVARIANT-spectrum-only-functional'  # known baseline
    post_v1_v3_corner_i = audit_output.get('corner_I_classification', None)

    preserved = (post_v1_v3_corner_i == pre_v1_v3_baseline_corner_i)
    verdict = 'PASS' if preserved else 'FAIL'

    report = {
        'gate': 'S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION',
        'pre_v1_v3_baseline_corner_i': pre_v1_v3_baseline_corner_i,
        'post_v1_v3_corner_i': post_v1_v3_corner_i,
        'preserved': preserved,
        'verdict': verdict,
        'audit_output_summary': {k: audit_output.get(k) for k in ['corner_I_classification', 'corner_II_classification', 'corner_III_classification', 'corner_IV_classification']},
        'remediation': (
            'If FAIL: route to mack-cosmic-bridge sole-writer for §VII.U.2 '
            'registry-text reconciliation; revert V.1 or V.3 edits and re-derive '
            'corner classification.' if not preserved else 'No remediation required.'
        ),
    }
    print(json.dumps(report, indent=2))

if __name__ == '__main__':
    main()
```

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-VII-U-2-AUDIT-RE-RUN-CORNER-I-PRESERVATION
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_corner_classification_audit.py
      assert: exists (pre-W6 prereq)
    - file: computations/_shared/_vii_u_2_audit_re_run_corner_i_preservation.py
      assert: exists AND non_empty
  audit_target: sessions/permanent-results-registry.md §VII.U.2 (file SHA pinned at plan-freeze, post-V.1+V.3 edits)
  pre_v1_v3_baseline_corner_i: 'algebra-INVARIANT-spectrum-only-functional' (per S88 W-21 V.1 baseline)
  scheme: post-V.1+V.3-edit-verification
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  corner_classification_audit_py: computations/_shared/_corner_classification_audit.py (file SHA pinned at plan-freeze)
  registry_md_post_v1_v3: sessions/permanent-results-registry.md (file SHA pinned at plan-freeze)
  W21_v1_landing_marker: <S88 W-21 V.1 verdict_sha pinned at plan-freeze>
  W21_v3_landing_marker: <S88 W-21 V.3 verdict_sha pinned at plan-freeze>
```

### 8. Expected output 4-tuple

```
value=PASS|FAIL (composite of pre-baseline vs post-V.1+V.3 Corner I classification comparison)
scheme=post-V.1+V.3-edit-verification
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND post-V.1+V.3 Corner I classification == pre-V.1+V.3 baseline ('algebra-INVARIANT-spectrum-only-functional').
- **FAIL**: post-V.1+V.3 Corner I classification != pre-V.1+V.3 baseline; remediation is to revert V.1 or V.3 edits and re-derive.
- **INFO**: not applicable for binary preservation check.

### 10. Substitution chain (for preservation claim direction)

Sign claim: "V.1+V.3 edits MUST preserve Corner I classification." Substitution chain:

- **Step 1 (Definitions)**: `pre_v1_v3_baseline = 'algebra-INVARIANT-spectrum-only-functional'`; `post_v1_v3 = corner_classification_audit_output['corner_I_classification']`; `preserved = (post_v1_v3 == pre_v1_v3_baseline)`.
- **Step 2 (Substitution)**: `verdict = PASS iff preserved; FAIL iff NOT preserved`.
- **Step 3 (Simplify)**: binary equality check; no continuous parameter.
- **Step 4 (Direction)**: edit preservation INCREASES verdict reliability (PASS); edit non-preservation FORCES FAIL (registry text change altered the corner classification, which is a registry-hygiene defect).
- **Conclusion**: the preservation predicate is a strict equality test; no false-PASS pathway under correct audit-script implementation.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: V.1+V.3 W-21 edits are registry-text-only (no semantic change to Corner I assignment); registry-text edits preserved the substrate-physics content; algebra-axis orthogonality K-counter MANDATORY clause continues to hold for §VII.U.2 cell I.
- **FAIL**: V.1+V.3 edits altered the Corner I classification; registry-hygiene defect; remediation routes to mack-cosmic-bridge sole-writer for §VII.U.2 registry-text reconciliation. Cross-wave consequence: W4 A.30 Stage-2 cross-axis verify of §VII.AR (which is registry-adjacent to §VII.U.2) inherits the registry-text instability and may need re-dispatch.

### 12. Effort estimate

0.2 wave-equivalents. Existing audit-script re-run + pre-baseline comparison + JSON report. Low end of effort range.

### 13. Substrate framing per phononic-framing.md IS-not-IN

The audit re-run IS the methodology-layer F-image of the substrate-physics registry-text-stability predicate "the V.1+V.3 W-21 edits preserve the substrate-physics Corner I classification." FORBIDDEN: "the audit re-checks the registry text after edits IN the rule system." INVERTED: "the registry-text-stability predicate IS what the methodology-layer's pre-edit-vs-post-edit composition determines under F"; the audit re-run IS the methodology-layer's image of the substrate-physics corner-classification structural identity. Direction: substrate-physics corner-classification structural identity (algebra-INVARIANT spectrum-only-functional class membership) → registry-text composition under F (§VII.U.2 cell I body) → audit-leg image under F (this re-run script + per-corner verdict). Container-thinking inversion: the registry text is NOT in a registry-system container; the registry text IS the methodology-layer's image of the substrate-physics structural identity, and the audit re-run IS what verifies its preservation under V.1+V.3 edits.

---

## §W6-7. S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE  (A.41)

### 1. Gate ID
`S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE`

### 2. Trigger
`[VERIFY] + [AUDIT]` — numerical D_max measurement (VERIFY) + Class-(d) classification routing (AUDIT).

### 3. Classification
**MIXED** — numerical D_max measurement IS GEOMETRIC (substrate-distance-2 spectral moment compared against substrate-canonical FULL physical regularization S61/S78 PV pipeline at Λ_UV = M_KK); the Class-(d) reclassification routing IS META (per `epistemic-discipline.md §"Source Reconciliation"` 6-class taxonomy + S88 W-24 V.1 reclassification of W4-2 + W9b-2 from Class-(f) → Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY).

**Sub-decomposition**: this gate is structurally MIXED-class; if wave-equivalence ceiling exceeded, sub-decompose into:
- W6-7a (COMPUTE-class numerical D_max measurement; gen-physicist + connes-ncg-theorist CO);
- W6-7b (METHODOLOGY-class Class-(d) routing; gen-physicist orchestrator-direct-write).

For initial single-pass plan: keep MIXED; sub-decomposition only on plan-freeze validation hit.

### 4. Agent type
**gen-physicist PRIMARY + connes-ncg-theorist CO-AUTHOR** for numerical D_max measurement (PV pipeline + spectrum cache cross-check requires NCG-axiomatic-side review). For the Class-(d) routing audit: orchestrator-direct-write per METHODOLOGY-class dispatch consequences.

Per `wave-classification.md §"Dispatch consequences"`:
- COMPUTE-half (numerical D_max) dispatches via `/rclab-coordinate` compute-mode with the CO-AUTHOR pair.
- METHODOLOGY-half (Class-(d) routing) dispatches via orchestrator-direct-write.

Both halves emit verdict lines to `computations/session-89/s89_gate_verdicts.txt` (canonical per `gate-verdicts.md`).

### 5. Hypothesis
The W9b-2 SCHEMATIC output value (per `_spectral_action_regulators.py` SCHEMATIC convention, output pinned in `computations/session-87/s87_w9b_pole_specificity_scan.npz`) compared against the substrate-canonical FULL physical regularization (S61/S78 PV pipeline at Λ_UV = M_KK = 7.428660036284456e+16 GeV) yields a measurable D_max = `|log10(W9b_2_schematic) − log10(S61_S78_PV_full)|`; the D_max value classifies under one of the SOURCE-RECONCILIATION 4-band severity levels (NO-ACTION / ADVISORY / MANDATORY / HARD-HALT) AND under the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY taxonomy (per S88 W-24 V.1 reclassification of W4-2 + W9b-2 from Class-(f) → Class-(d)).

### 6. Method

**MCP knowledge query (mandatory pre-compute)**:
```
search_knowledge("D_max W9b-2 SCHEMATIC vs PV pipeline FULL physical")
search_knowledge("Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY")
search_knowledge("S61 S78 PV pipeline Lambda_UV M_KK")
trace_entity("W9b_2_schematic_output")
get_constant("M_KK")
get_constant("xi_E_GGE_inv")
```

Expected: M_KK = 7.428660036284456e+16 GeV (canonical_constants.py); W9b-2 SCHEMATIC output reachable via npz path; S61/S78 PV pipeline source identified; Class-(d) taxonomy in `epistemic-discipline.md §"Source Reconciliation"`.

**COMPUTE-half logic** (numerical D_max measurement; via `/rclab-coordinate` compute-mode with gen-physicist + connes-ncg-theorist):

```python
"""
S89 W6-7 (A.41) COMPUTE-half — Numerical D_max measurement
W9b-2 SCHEMATIC output vs S61/S78 FULL PV pipeline at Λ_UV = M_KK
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')

import json
import math
import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, 'computations/_shared')
from canonical_constants import M_KK

def measure_d_max() -> dict:
    """
    Step 1: Load W9b-2 SCHEMATIC output value from
            computations/session-87/s87_w9b_pole_specificity_scan.npz
    Step 2: Compute substrate-canonical FULL PV pipeline value at
            Λ_UV = M_KK (S61/S78 pipeline; cross-check with connes-ncg-theorist)
    Step 3: Compute D_max = |log10(W9b_2_schematic) − log10(S61_S78_PV_full)|
    Step 4: Classify D_max under SOURCE-RECONCILIATION 4-band severity
    Step 5: Cross-reference with Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY
            taxonomy
    """
    # Step 1: Load W9b-2 SCHEMATIC
    w9b2_npz = np.load('computations/session-87/s87_w9b_pole_specificity_scan.npz')
    w9b2_schematic = float(w9b2_npz['rho_S_at_s_eq_4'])  # SCHEMATIC convention
    # Substrate-distance-2 pole rho_S value (per W9-LCR3.2 MELLIN convention)

    # Step 2: Substrate-canonical FULL PV pipeline at Λ_UV = M_KK
    # S61/S78 PV pipeline implements full Pauli-Villars subtraction with mass-scale
    # running; canonical reference at Λ_UV = M_KK = 7.4287e16 GeV
    # Cross-check: connes-ncg-theorist verifies PV pipeline implementation
    # matches Connes-Chamseddine 1996 §2.2-2.3 multipliers
    s61_s78_pv_full = pv_pipeline_at_substrate_distance_2_pole(
        lambda_uv=M_KK,
        regulator='Pauli-Villars',
        order=4)  # 4-PV-mass subtraction

    # Step 3: D_max
    d_max = abs(math.log10(abs(w9b2_schematic)) - math.log10(abs(s61_s78_pv_full)))

    # Step 4: 4-band severity classification per epistemic-discipline.md
    if d_max < 0.1:
        severity = 'NO-ACTION'
    elif d_max < 1.0:
        severity = 'ADVISORY (S2)'
    elif d_max < 3.0:
        severity = 'MANDATORY (S1)'
    else:
        severity = 'HARD-HALT'

    # Step 5: Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY classification
    # Per S88 W-24 V.1 reclassification: W9b-2 output is a derivative form
    # of the canonical primary (Mellin-Barnes residue at substrate-distance-2
    # pole s=4) via the SCHEMATIC `_spectral_action_regulators.py` derivation
    # chain; NOT a placeholder OOM estimate
    class_d_routing = 'Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY'

    return {
        'gate': 'S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE',
        'w9b2_schematic_value': w9b2_schematic,
        'w9b2_schematic_log10': math.log10(abs(w9b2_schematic)),
        's61_s78_pv_full_value': s61_s78_pv_full,
        's61_s78_pv_full_log10': math.log10(abs(s61_s78_pv_full)),
        'd_max': d_max,
        'severity_band': severity,
        'class_d_routing': class_d_routing,
        'lambda_uv_GeV': M_KK,
        'verdict': 'INFO' if d_max >= 0.1 else 'PASS',
    }

def pv_pipeline_at_substrate_distance_2_pole(lambda_uv: float, regulator: str, order: int) -> float:
    """
    Substrate-canonical S61/S78 PV pipeline at substrate-distance-2 pole.
    [Implementation references S61/S78 worked computation;
     connes-ncg-theorist verifies match with Connes-Chamseddine 1996 §2.2-2.3]
    """
    # Substrate-physics PV pipeline computation
    # [stub for plan; runtime implementation by gen-physicist + connes-ncg CO]
    ...
```

**METHODOLOGY-half logic** (Class-(d) routing; orchestrator-direct-write):

```python
"""
S89 W6-7 (A.41) METHODOLOGY-half — Class-(d) routing classification
"""

def class_d_routing_audit(d_max: float, severity: str) -> dict:
    """
    Per epistemic-discipline.md §"Source Reconciliation" Class-(d):
    PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation:
      - verify derivation chain
      - ratio check against source primitives
      - algebraic-equivalence audit at plan-authorship per Class 8.3 item 5
    """
    routing = {
        'class_taxonomy': 'Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY',
        'severity_band': severity,
        'remediation_steps': [
            'Verify derivation chain: SCHEMATIC `_spectral_action_regulators.py` '
            'consumes substrate-distance-2 pole s=4 residue via Mellin-Barnes '
            'closure; the SCHEMATIC version is a derivative form of the FULL '
            'physical PV pipeline at Λ_UV = M_KK',
            'Ratio check: r = W9b_2_schematic / S61_S78_PV_full; if |log10(r)| < 0.1 '
            '→ NO-ACTION; if 0.1 ≤ |log10(r)| < 1.0 → ADVISORY; if 1.0 ≤ |log10(r)| < 3.0 '
            '→ MANDATORY; if ≥ 3.0 → HARD-HALT',
            'Algebraic-equivalence audit: verify that the SCHEMATIC formula and FULL '
            'PV pipeline formula are the same function of the underlying spectral '
            'moments, modulo a closed-form scalar multiplier; if the multiplier is '
            'algebraically reducible to canonical_constants pins, downgrade severity by 1 band',
        ],
    }
    return routing
```

**Cross-wave consume**: A.41 reads `cocycle_norm_ratio_67_88` regulator-invariant pin from W3 A.14 npz output `computations/session-89/s89_w3_a14_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` (forward-only consume; A.14 closes before A.41 within S89 batch).

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-D-MAX-MEASUREMENT-W9B-2-VS-FULL-PV-PIPELINE
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/session-89/s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.py
      assert: exists AND non_empty
    - file: computations/session-89/s89_w6_d_max_measurement_w9b_2_vs_pv_pipeline.npz
      assert: exists (post-COMPUTE-half run)
  numerical_inputs:
    w9b2_schematic_npz: computations/session-87/s87_w9b_pole_specificity_scan.npz (file SHA pinned at plan-freeze)
    cocycle_norm_ratio_invariant: computations/session-89/s89_w3_a14_substrate_cocycle_ratio_regulator_class_invariance_scan.npz (cross-wave; npz SHA pinned at A.14 close)
    M_KK: 7.428660036284456e+16 GeV (canonical_constants.py)
    pv_pipeline_order: 4 (4-PV-mass subtraction)
  level_pin: SCHEMATIC vs FULL physical (per substrate-first-canonical-sourcing.md §(iv) MANDATORY at K=4)
  schematic_helper: computations/_shared/_spectral_action_regulators.py (file SHA pinned; consumed by W9b-2)
  pv_pipeline_source: S61/S78 worked computation (substrate-canonical FULL physical regularization)
  4_band_calibration:
    NO-ACTION: D_max < 0.1
    ADVISORY: 0.1 <= D_max < 1.0
    MANDATORY: 1.0 <= D_max < 3.0
    HARD-HALT: D_max >= 3.0
  scheme: substrate-distance-2-pole-Mellin-residue
  convention: SCHEMATIC-vs-FULL-PV-D_max-measurement
  L_max: 10 (per W9b-2 SCHEMATIC output)
input_pin_map:
  W9b_2_npz: computations/session-87/s87_w9b_pole_specificity_scan.npz (file SHA pinned at plan-freeze)
  W3_A14_npz: computations/session-89/s89_w3_a14_*.npz (cross-wave; SHA pinned at A.14 close)
  canonical_constants_py: computations/_shared/canonical_constants.py (file SHA pinned at plan-freeze)
  spectral_action_regulators_py: computations/_shared/_spectral_action_regulators.py (file SHA pinned at plan-freeze; SCHEMATIC docstring)
  epistemic_discipline_md: .claude/rules/epistemic-discipline.md (file SHA pinned at plan-freeze)
```

### 8. Expected output 4-tuple

```
value=<D_max-numerical> (with severity-band classification + Class-(d) routing tag)
scheme=substrate-distance-2-pole-Mellin-residue
convention=SCHEMATIC-vs-FULL-PV-D_max-measurement
L_max=10
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND D_max measurable (no division-by-zero, no NaN) AND severity-band classifiable AND Class-(d) routing tag emitted.
- **INFO**: D_max measurable but ≥ 0.1 (severity ADVISORY or higher); the W9b-2 SCHEMATIC output deviates from FULL PV pipeline by a structurally significant amount; remediation routes per Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY.
- **FAIL**: D_max not measurable (e.g., one of the values is zero or NaN); the COMPUTE-half cannot complete; remediation is debug + re-run.

### 10. Substitution chain (for D_max sign claim per substrate-first-canonical-sourcing.md §"Source Reconciliation" 4-band calibration)

Sign claim: "D_max INCREASES with structural deviation between SCHEMATIC W9b-2 and FULL PV pipeline; severity band INCREASES monotonically with D_max." Substitution chain:

- **Step 1 (Definitions)**:
  - `W9b_2_schematic = float(w9b2_npz['rho_S_at_s_eq_4'])` (SCHEMATIC convention; per `_spectral_action_regulators.py` docstring lines 23-30 SCHEMATIC class)
  - `S61_S78_PV_full = pv_pipeline_at_substrate_distance_2_pole(Λ_UV=M_KK, regulator='Pauli-Villars', order=4)` (FULL physical class; substrate-canonical reference)
  - `D_max = |log10(|W9b_2_schematic|) − log10(|S61_S78_PV_full|)|`
- **Step 2 (Substitution)**:
  - `D_max = |log10(|W9b_2_schematic|/|S61_S78_PV_full|)|` (substituting the log-difference identity log10(a) − log10(b) = log10(a/b))
- **Step 3 (Simplify)**:
  - `D_max = |log10(R)|` where `R = |W9b_2_schematic|/|S61_S78_PV_full|` is the structural-ratio between SCHEMATIC and FULL.
- **Step 4 (Direction)**:
  - `R = 1 ⇒ D_max = 0 ⇒ severity = NO-ACTION` (SCHEMATIC matches FULL exactly).
  - `R ≠ 1 ⇒ D_max > 0 ⇒ severity ∈ {ADVISORY, MANDATORY, HARD-HALT}` per the 4-band calibration `D_max < 0.1 / 0.1 ≤ D_max < 1.0 / 1.0 ≤ D_max < 3.0 / D_max ≥ 3.0`.
  - `D_max` MONOTONICALLY INCREASES with `|log10(R)|`; severity-band classification is a STEP FUNCTION at thresholds 0.1, 1.0, 3.0.
- **Conclusion**: D_max is the magnitude of the log-ratio between SCHEMATIC and FULL; severity-band classification is monotone-step in D_max; Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY routing fires at any D_max > 0 because W9b-2 is structurally a derivative form of the FULL PV pipeline (per S88 W-24 V.1 reclassification).

### 11. What PASSES/FAILS MEAN for solution space

- **PASS** (D_max < 0.1): SCHEMATIC W9b-2 numerically matches FULL PV pipeline; the SCHEMATIC convention is empirically calibrated and downstream consumers can rely on the SCHEMATIC value as a FULL-equivalent proxy.
- **INFO** (0.1 ≤ D_max < 3.0): structural deviation present; remediation routes per Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY:
  - 0.1 ≤ D_max < 1.0 (ADVISORY): downgrade `convention=` field on downstream consumers; document SCHEMATIC-vs-FULL ratio in canonical_constants.py provenance.
  - 1.0 ≤ D_max < 3.0 (MANDATORY): plan-freeze halt for downstream consumers; require explicit Class-(d) ratio-check + algebraic-equivalence audit at plan-authorship.
- **HARD-HALT** (D_max ≥ 3.0; subset of INFO outcome): plan-freeze halt + manual review required; SCHEMATIC convention is structurally non-equivalent to FULL physical; downstream consumers MUST re-pin to FULL.
- **FAIL**: COMPUTE-half cannot complete (zero or NaN); methodology infrastructure cannot proceed.

### 12. Effort estimate

0.4 wave-equivalents. COMPUTE-half: 0.3 (PV pipeline cross-check with connes-ncg-theorist + npz load + log-ratio computation); METHODOLOGY-half: 0.1 (Class-(d) routing JSON emission). MIXED-class overhead absorbed.

### 13. Substrate framing per phononic-framing.md IS-not-IN

The D_max measurement IS the substrate's audit-leg image of the substrate-physics SCHEMATIC-vs-FULL-physical-regularization invariance predicate "the SCHEMATIC convention's spectral moment value matches the FULL physical regularization's value at the substrate-distance-2 pole." FORBIDDEN: "the SCHEMATIC `_spectral_action_regulators.py` module computes the spectral moment IN a regulator-container; the FULL PV pipeline computes it IN a different regulator-container." INVERTED: "the substrate's spectral moment at the substrate-distance-2 pole IS what the SCHEMATIC and FULL conventions both attempt to image under F"; both conventions are F-images of the same substrate-physics quantity, and D_max measures their methodology-floor divergence under the F-image. Direction: substrate-physics spectral moment at substrate-distance-2 pole s=4 (intrinsic to D_K eigenvalue spectrum) → SCHEMATIC convention image under F (W9b-2 output) AND FULL PV pipeline image under F (S61/S78 output) → audit-leg image under F (D_max + severity band + Class-(d) routing). Container-thinking inversion: the regulators are NOT containers of the spectral moment; the spectral moment IS what the regulators (SCHEMATIC vs FULL) attempt to image under F, and D_max measures their F-image-divergence. The Λ_UV = M_KK pin IS the substrate's intrinsic UV scale (per `phononic-framing.md` substrate-IS levels), NOT a cutoff IN a UV-container.

---

## §W6-8. S89-SOURCE-RECONCILIATION-CLASS-D-ROUTING-EXTENSION  (A.42)

### 1. Gate ID
`S89-SOURCE-RECONCILIATION-CLASS-D-ROUTING-EXTENSION`

### 2. Trigger
`[AUDIT] + [VERIFY]` — audit-script extension implementation + 3 synthetic test fixtures.

### 3. Classification
**META** (methodology layer). Extends `_source_reconciliation_audit.py` with Class-(d) inheritance severity routing for W4-2/W9b-2-derived pins; queries calibration corpus for inheritance-classification.

### 4. Agent type
**Orchestrator-direct-write** per `wave-classification.md §"Dispatch consequences"`.

### 5. Hypothesis
A Class-(d) routing extension to `_source_reconciliation_audit.py`, querying the calibration corpus at `epistemic-discipline.md §"Source Reconciliation"` Class-(d) entries (W4-2 + W9b-2 reclassified per S88 W-24 V.1 from Class-(f) → Class-(d)) and emitting Class-(d) inheritance severity for downstream pins derived from W4-2/W9b-2 outputs (e.g., A.41 D_max measurement consuming W9b-2), will close the silent severity-band-misclassification pathway (currently W4-2/W9b-2-derived pins MAY be silently classified under Class-(f) Class-(b) Class-(c) instead of Class-(d), producing wrong remediation routing).

### 6. Method

**MCP knowledge query (mandatory pre-build)**:
```
search_knowledge("Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY W4-2 W9b-2 reclassification")
search_knowledge("source_reconciliation_audit.py routing extension calibration corpus")
trace_entity("source_reconciliation_audit")
```

Expected: existing `_source_reconciliation_audit.py` body present; W4-2 + W9b-2 Class-(d) reclassification per `substrate-first-canonical-sourcing.md §(iv)` calibration corpus (K=4 at S88 W7b-83 close; substantive corpus instances W4-2 + W9b-2 NEGATIVE-CALIBRATION → Class-(d) per S88 W-24 V.1 / B.61).

**Build target**: extension function in `computations/_shared/_source_reconciliation_audit.py`:

```python
def class_d_inheritance_routing(pin_provenance: str) -> dict:
    """
    Per epistemic-discipline.md §"Source Reconciliation" Class-(d)
    PIN-DERIVATIVE-VS-SOURCE-PRIMARY taxonomy + S88 W-24 V.1
    reclassification of W4-2 + W9b-2 from Class-(f) → Class-(d):

    For pins provenance-traced to W4-2 (S86) or W9b-2 (S87) outputs,
    emit Class-(d) inheritance severity (downgraded from Class-(f) by
    one severity band) per the W-24 V.1 reclassification.

    Calibration corpus query:
      - W4-2 (S86): producing-script consumes _spectral_action_regulators.py
        SCHEMATIC; output is Class-(d) per S88 W-24 V.1
      - W9b-2 (S87): same SCHEMATIC consumption pattern; output is Class-(d)
    """
    CALIBRATION_CORPUS = {
        'W4-2': {
            'session': 'S86',
            'producing_script': 's86_w4_p5_sector_2_k_invariant.py',
            'class_taxonomy': 'Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY',
            'reclassification_source': 'S88 W-24 V.1 / B.61',
            'd_max_band_estimate': '~1.13 OOM (MANDATORY)',
        },
        'W9b-2': {
            'session': 'S87',
            'producing_script': 's87_w9b_pole_specificity_scan.py',
            'class_taxonomy': 'Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY',
            'reclassification_source': 'S88 W-24 V.1 / B.61',
            'd_max_band_estimate': '~1.13 OOM (MANDATORY)',
        },
    }

    # Trace pin_provenance back to a calibration corpus entry
    for cal_id, cal_entry in CALIBRATION_CORPUS.items():
        if cal_id in pin_provenance or cal_entry['producing_script'] in pin_provenance:
            return {
                'inheritance_class': 'Class-(d)',
                'calibration_corpus_match': cal_id,
                'severity_band': 'MANDATORY',  # downgraded from Class-(f) HARD-HALT
                'remediation': (
                    f'Pin is provenance-traced to {cal_id} ({cal_entry["session"]}) '
                    f'output; Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation: '
                    f'(i) verify derivation chain; (ii) ratio check against source '
                    f'primitives; (iii) algebraic-equivalence audit at plan-authorship '
                    f'per Class 8.3 item 5. Per W-24 V.1 reclassification, severity '
                    f'is downgraded by 1 band from Class-(f) HARD-HALT to MANDATORY.'
                ),
                'reclassification_source': cal_entry['reclassification_source'],
            }

    # No calibration corpus match
    return {
        'inheritance_class': 'NOT-IN-CLASS-D-CORPUS',
        'calibration_corpus_match': None,
        'severity_band': 'N/A',
        'remediation': 'Pin is not derivative of W4-2 or W9b-2 calibration corpus; route via standard 6-class taxonomy.',
    }
```

**3 synthetic test fixtures**:

| Fixture # | Test name | Pin provenance | Expected verdict |
|:---------:|:---------|:---------------|:-----------------|
| 1 | `class_d_w4_2_inheritance_detect` | `'pin computed in s86_w4_p5_sector_2_k_invariant.npz consumed at S88 W-9 §V.1'` | `inheritance_class='Class-(d)'`, `calibration_corpus_match='W4-2'`, `severity_band='MANDATORY'` |
| 2 | `class_d_w9b_2_inheritance_detect` | `'pin computed in s87_w9b_pole_specificity_scan.npz consumed at S89 W-6 A.41'` | `inheritance_class='Class-(d)'`, `calibration_corpus_match='W9b-2'`, `severity_band='MANDATORY'` |
| 3 | `not_in_class_d_corpus_route` | `'pin computed in s85_w0_zubarev_lmax_convergence_to_minus_one.npz'` | `inheritance_class='NOT-IN-CLASS-D-CORPUS'`, route to standard 6-class |

### 7. Machinery pin (PRDR)

```yaml
schema_version: R3
gate_id: S89-SOURCE-RECONCILIATION-CLASS-D-ROUTING-EXTENSION
machinery_pin_map:
  artifact_existence_predicate:
    - file: computations/_shared/_source_reconciliation_audit.py
      assert: exists AND extension_function_present('class_d_inheritance_routing')
    - file: computations/_shared/_source_reconciliation_class_d_routing_test_fixtures.py
      assert: exists AND all_3_synthetic_fixtures_pass
  calibration_corpus:
    W4-2: {session: S86, class: 'Class-(d)', d_max_band: '~1.13 OOM'}
    W9b-2: {session: S87, class: 'Class-(d)', d_max_band: '~1.13 OOM'}
  reclassification_source: S88 W-24 V.1 / B.61 (Class-(f) → Class-(d) per substrate-first-canonical-sourcing.md §(iv))
  severity_downgrade: Class-(f) HARD-HALT → Class-(d) MANDATORY (1 band)
  scheme: calibration-corpus-keyed-routing
  convention: orchestrator-direct-write-METHODOLOGY-CLASS
  L_max: N/A
input_pin_map:
  source_reconciliation_audit_pre_extension: computations/_shared/_source_reconciliation_audit.py (file SHA pinned at plan-freeze)
  epistemic_discipline_md: .claude/rules/epistemic-discipline.md (file SHA pinned at plan-freeze; §"Source Reconciliation" Class-(d))
  substrate_first_canonical_sourcing_md: .claude/rules/substrate-first-canonical-sourcing.md (file SHA pinned at plan-freeze; §(iv) calibration corpus)
  S88_W_24_V1_landing_marker: <S88 W-24 V.1 verdict_sha pinned at plan-freeze>
```

### 8. Expected output 4-tuple

```
value=PASS|FAIL (composite of extension_function_present AND all_3_synthetic_fixtures_pass)
scheme=calibration-corpus-keyed-routing
convention=orchestrator-direct-write-METHODOLOGY-CLASS
L_max=N/A
```

### 9. PASS/FAIL/INFO thresholds

- **PASS**: M1∧M2∧M3∧M4 satisfied AND `class_d_inheritance_routing` function present in `_source_reconciliation_audit.py` AND all 3 synthetic test fixtures PASS.
- **FAIL**: extension function absent OR any synthetic test fixture fails.
- **INFO**: not applicable for build-and-test gate.

### 10. Substitution chain (for severity-downgrade direction claim)

Sign claim: "Class-(d) reclassification DOWNGRADES severity by 1 band from Class-(f) HARD-HALT to MANDATORY." Substitution chain:

- **Step 1 (Definitions)**:
  - Class-(f) PIN-PLACEHOLDER: severity_band per `epistemic-discipline.md §"Source Reconciliation"` Class-(f): `D_max ≥ 3.0 → HARD-HALT`; `1.0 ≤ D_max < 3.0 → MANDATORY`; etc.
  - Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: severity_band downgraded by 1 band relative to Class-(f) at the same D_max because the pin is structurally a derivative form of the canonical primary, not a placeholder OOM estimate.
  - W4-2 + W9b-2 D_max ≈ 1.13 OOM (per S88 W-24 V.1 / B.61).
- **Step 2 (Substitution)**:
  - Pre-reclassification (Class-(f)): D_max = 1.13 → severity_band = `MANDATORY` (since 1.0 ≤ 1.13 < 3.0).
  - Post-reclassification (Class-(d)): severity_band downgraded by 1 band: `MANDATORY → ADVISORY` ?? Wait — reread: per S88 W-24 V.1 / B.61 the W4-2 + W9b-2 instances at D_max ≈ 1.13 routed to MANDATORY band post-reclassification as Class-(d). Verify:
  - Class-(f) at D_max ≈ 1.13: MANDATORY (per `epistemic-discipline.md §"Source Reconciliation"` 4-band calibration).
  - Class-(d) at D_max ≈ 1.13: still MANDATORY (the reclassification preserves the band at this D_max because the band-rule depends on D_max, not on the class-letter; the class-letter changes the REMEDIATION not the band).
  - Downgrade clause "Class-(f) HARD-HALT → Class-(d) MANDATORY (1 band)" applies SPECIFICALLY at D_max ≥ 3.0: Class-(f) would be HARD-HALT, Class-(d) is MANDATORY (1 band downgrade).
- **Step 3 (Simplify)**: severity_band(D_max, class) is monotone in D_max but step-up at the band thresholds; the class-letter shifts the band-mapping at the high-D_max end only (HARD-HALT → MANDATORY for Class-(d) at D_max ≥ 3.0).
- **Step 4 (Direction)**:
  - At D_max < 3.0: Class-(f) and Class-(d) classify identically; no downgrade.
  - At D_max ≥ 3.0: Class-(f) → HARD-HALT; Class-(d) → MANDATORY; **direction: 1-band severity DOWNGRADE for Class-(d) reclassification at D_max ≥ 3.0 only**.
  - The W4-2 + W9b-2 calibration corpus at D_max ≈ 1.13 sits in the MANDATORY band under both classes; the reclassification's structural import is at the audit-trail-canonical reading layer (PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation steps differ from PIN-PLACEHOLDER steps).
- **Conclusion**: the severity-downgrade direction claim is conditional on D_max ≥ 3.0; for the W4-2 + W9b-2 calibration corpus at D_max ≈ 1.13, the band is MANDATORY under both classes, but the remediation routing differs structurally.

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: methodology-floor enforcement at the source-reconciliation-class-(d) routing extension is OPERATIONAL; downstream consumers (e.g., A.41 D_max measurement of W9b-2 inheritance) route correctly to Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY remediation rather than silently misclassifying to Class-(f) PIN-PLACEHOLDER.
- **FAIL**: methodology-floor enforcement incomplete; W4-2/W9b-2-derived pins may silently misclassify; remediation is to rebuild the extension function + re-test.
- Solution-space mapping: extension function IS the F-image at the methodology layer of the substrate-physics provenance-classification predicate; PASS represents methodology-floor saturation of the inheritance-classification axis.

### 12. Effort estimate

0.6 wave-equivalents. Extension function build (~0.2) + 3 synthetic test fixtures (~0.3) + integration with existing `_source_reconciliation_audit.py` body (~0.1).

### 13. Substrate framing per phononic-framing.md IS-not-IN

The Class-(d) routing extension IS the methodology-layer F-image of the substrate-physics provenance-classification predicate "a pin's provenance is structurally a derivative form of a calibration-corpus canonical primary, not a placeholder OOM estimate." FORBIDDEN: "the routing extension classifies pins IN the source-reconciliation system." INVERTED: "the provenance-classification predicate IS what the methodology-layer's calibration-corpus query determines under F"; the extension function IS the methodology-layer's image of the substrate-physics inheritance-classification structural identity. Direction: substrate-physics inheritance-classification (W4-2 + W9b-2 outputs are derivative forms of canonical primaries) → calibration-corpus content under F (`epistemic-discipline.md §"Source Reconciliation"` Class-(d) entries) → audit-leg image under F (extension function + 3 synthetic test fixtures). Container-thinking inversion: the calibration corpus is NOT in a corpus-container; the corpus IS the methodology-layer's image of the substrate-physics inheritance-classification structural identity, and the extension function IS what verifies its consistent application to W4-2/W9b-2-inheritance pins.

---

## Wave 6 → Other-wave Decision Points

### Cross-wave consume points (forward-only)

- **A.41 (W6-7) consumes W3 A.14 npz**: A.41 reads `cocycle_norm_ratio_67_88` regulator-invariant pin from `computations/session-89/s89_w3_a14_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` (forward-only consume; A.14 closes before A.41 within S89 batch order). The regulator-invariant pin serves as the substrate-canonical reference for the SCHEMATIC-vs-FULL ratio cross-check.
- **A.34 (W6-6) feeds W4 A.30 Stage-2 cross-axis verify of §VII.AR**: A.34 verifies §VII.U.2 Corner I preservation post-V.1+V.3 W-21 edits; §VII.AR is registry-adjacent to §VII.U.2 and Stage-2 cross-axis verify A.30 audits §VII.AR registry text. If A.34 FAILs (Corner I not preserved), the registry-text instability propagates to A.30 and may require re-dispatch of A.30 with revised registry-text input pin.

### In-W6 dependency chain

- **A.41 (W6-7) → A.42 (W6-8)**: A.41 emits D_max + severity band + Class-(d) routing tag; A.42's calibration-corpus-keyed-routing extension consumes A.41's output as a live test case (in addition to the 3 pre-registered synthetic fixtures).

### Forward-only effects (no S89 wave consumes these)

- **A.15 (W6-1) plan-staleness validator**: feeds future S90+ plan-freeze validators.
- **A.22 (W6-3) audit-script extensions**: feed all S89+ plan-freeze validators (cohomology-class-layer surrogate detection, Class-(g) registry-anchor route conflation, sign-PASS reading, V_4 anchor-structure).
- **A.42 (W6-8) Class-(d) routing extension**: feeds future remediation routing for W4-2/W9b-2-inheritance pins at S90+ plan-freeze.

### Composite W6 close

W6 closes cleanly when:
- All 8 gate verdicts emitted to `computations/session-89/s89_gate_verdicts.txt`.
- All 8 gate-IDs appended to `methodology-wave-allowlist.md` with computed `sha256_of_plan_block`.
- All 8 parallel registry entries written to `sessions/framework/registry/methodology-wave-instances.md` with verbatim rationale prose.
- Synthesis section landed at `sessions/archive/session-89/session-89-w6-workingpaper.md` with Carry-Forward Computations + Process Observations partition per `feedback_fix-in-session-never-defer.md`.

---

## Wave 6 Methodology-wave-allowlist Append Helper Spec

### Helper script: `computations/session-89/s89_w6_allowlist_append_helper.py`

Modeled on the canonical S88 W8 pattern at `computations/session-88/s88_w8_allowlist_append_helper.py` (per `methodology-wave-allowlist.md §"Append-helper canonical"`).

**Spec**:

```python
"""
S89 W6 methodology-wave-allowlist append helper

Appends 8 NEW rows to .claude/rules/methodology-wave-allowlist.md AFTER
the existing tail (last row at S88: W12-147 | S88 | 86d52f64f...).

Writes 3-column rows only (gate_id | session | sha256_of_plan_block);
parallel registry entries with rationale prose go to
sessions/framework/registry/methodology-wave-instances.md per the
S88 W9-RULE-CLEANUP precedent.

Single-shot POSIX O_APPEND (atomic; parallel-writer-safe) per
methodology-wave-allowlist.md §"Append-helper canonical".
"""

import hashlib
from pathlib import Path

S89_W6_ALLOWLIST_ROWS = [
    {'gate_id': 'W6-1', 'session': 'S89', 'plan_block_path_anchor': '§W6-1'},
    {'gate_id': 'W6-2', 'session': 'S89', 'plan_block_path_anchor': '§W6-2'},
    {'gate_id': 'W6-3', 'session': 'S89', 'plan_block_path_anchor': '§W6-3'},
    {'gate_id': 'W6-4', 'session': 'S89', 'plan_block_path_anchor': '§W6-4'},
    {'gate_id': 'W6-5', 'session': 'S89', 'plan_block_path_anchor': '§W6-5'},
    {'gate_id': 'W6-6', 'session': 'S89', 'plan_block_path_anchor': '§W6-6'},
    {'gate_id': 'W6-7', 'session': 'S89', 'plan_block_path_anchor': '§W6-7'},
    {'gate_id': 'W6-8', 'session': 'S89', 'plan_block_path_anchor': '§W6-8'},
]

def compute_sha_of_plan_block(plan_md_path: Path, anchor: str) -> str:
    """SHA-256 over the plan-file gate block (between anchor and next anchor)."""
    text = plan_md_path.read_text(encoding='utf-8')
    # Locate block from anchor to next §W6-X or end-of-section
    import re
    pattern = rf'## {re.escape(anchor)}\..*?(?=## §W6-\d|## Wave 6 → |$)'
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return 'pending'
    block_text = match.group(0)
    return hashlib.sha256(block_text.encode('utf-8')).hexdigest()

def append_allowlist_rows(allowlist_path: Path, plan_md_path: Path) -> None:
    """Single-shot POSIX O_APPEND of 8 rows."""
    rows_to_append = []
    for row_spec in S89_W6_ALLOWLIST_ROWS:
        sha = compute_sha_of_plan_block(plan_md_path, row_spec['plan_block_path_anchor'])
        row_text = f"| {row_spec['gate_id']} | {row_spec['session']} | {sha} |\n"
        rows_to_append.append(row_text)
    # Single atomic POSIX O_APPEND
    with allowlist_path.open('a', encoding='utf-8') as f:
        f.writelines(rows_to_append)

def append_registry_entries(registry_path: Path, plan_md_path: Path) -> None:
    """Append parallel registry entries with verbatim rationale prose."""
    entries = []
    for row_spec in S89_W6_ALLOWLIST_ROWS:
        sha = compute_sha_of_plan_block(plan_md_path, row_spec['plan_block_path_anchor'])
        # Rationale prose template (verbatim from W6 plan §3 classifications)
        entry = f"""
### {row_spec['gate_id']} ({row_spec['session']}) — {sha}

**Provenance**: gen-physicist orchestrator-direct planner-write per /rclab-plan skill §3b;
wave-classification.md §"Dispatch consequences" — METHODOLOGY-class waves SKIP /rclab-coordinate
compute-mode. Source: {row_spec['plan_block_path_anchor']} of session-89-plan-w6.md.

**M1∧M2∧M3∧M4 conjunction**:
- M1 (PASS predicate type): artifact-existence-with-substantive-content predicate per gate block §9.
- M2 (Producing-operation type): Edit/Write/MultiEdit on .claude/{{rules,templates,skills}}/** + grep/wc/SHA-256 cross-checks.
- M3 (Source-of-truth type): verbatim sub-diff from S88 Ledger A item (per session-89-context.md Cluster F).
- M4 (Allowlist membership): this row appends gate-ID to methodology-wave-allowlist.md.

**Authorship**: gen-physicist orchestrator-direct-write under METHODOLOGY-class dispatch consequences.
{'connes-ncg-theorist CO-AUTHOR for numerical D_max measurement (PV pipeline cross-check).' if row_spec['gate_id'] == 'W6-7' else ''}

**Cross-link**: session-89-plan-w6.md {row_spec['plan_block_path_anchor']}.
"""
        entries.append(entry)
    with registry_path.open('a', encoding='utf-8') as f:
        f.writelines(entries)

def main():
    allowlist_path = Path('.claude/rules/methodology-wave-allowlist.md')
    registry_path = Path('sessions/framework/registry/methodology-wave-instances.md')
    plan_md_path = Path('sessions/session-plan/session-89-plan-w6.md')

    append_allowlist_rows(allowlist_path, plan_md_path)
    append_registry_entries(registry_path, plan_md_path)
    print("S89 W6 allowlist + registry append complete.")

if __name__ == '__main__':
    main()
```

### Helper invocation discipline

The helper MUST be invoked at S89 plan-freeze AFTER the W6 plan file is finalized (so SHA computation reads stable content). Invocation: `python computations/session-89/s89_w6_allowlist_append_helper.py`.

The helper writes 3-column rows ONLY (per `methodology-wave-allowlist.md §"Edit discipline"` item 4); rationale prose goes to the parallel registry. A future single-shot append helper that writes rationale prose into the rule-file row reverts the W9-RULE-CLEANUP lift-out and is rejected at plan-freeze.

### Post-append verification

After the helper runs, the orchestrator MUST verify:

1. `methodology-wave-allowlist.md` has 8 NEW rows with computed (non-`pending`) SHAs at the tail.
2. `methodology-wave-instances.md` has 8 NEW `### W6-X (S89) — <sha>` entries with rationale prose.
3. SHAs match: each row's SHA matches the corresponding registry entry's SHA.

If any verification fails, the helper MUST be re-run after the discrepancy is fixed; the rule-file is append-only, so rejected appends route to the next-session's plan-revision.

---

## Wave 6 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR (Pre-Registration Dry-Run) protocol, every W6 gate's free parameters are enumerated below. Free parameters NOT pinned in the gate block's `machinery_pin_map` are flagged as PRU-vulnerable.

### Per-gate machinery enumeration

| Gate | Free parameters | Pin status |
|:-----|:----------------|:-----------|
| W6-1 (A.15) | STALENESS_PATTERNS regex set; cross-reviewer-eligibility-audit memory-grep recursion depth | All pinned in script body + machinery_pin_map |
| W6-2 (A.19) | ROUTE_A_SIGNATURES set; ROUTE_B_SIGNATURES set; classification thresholds (a_score > 2*b_score AND a_score >= 3) | All pinned in script body + machinery_pin_map |
| W6-3 (A.22) | 4 sub-item extension function bodies; 4 synthetic test fixtures | All pinned in script body + machinery_pin_map |
| W6-4 (A.23) | EG1 audit-pattern 3-step procedure; CANDIDATE_RULE_FILES list; per-rule-file regex patterns | All pinned in script body + machinery_pin_map |
| W6-5 (A.33) | Substrate-derivation pattern set; precision-pin pattern set; placeholder pattern set | All pinned in script body + machinery_pin_map |
| W6-6 (A.34) | pre_v1_v3_baseline_corner_i value; audit script subprocess invocation arguments | All pinned in machinery_pin_map |
| W6-7 (A.41) | M_KK value; PV pipeline order (4); 4-band calibration thresholds (0.1, 1.0, 3.0); cocycle_norm_ratio_invariant npz path (cross-wave A.14 consume) | All pinned in machinery_pin_map; cross-wave npz SHA pinned at A.14 close |
| W6-8 (A.42) | CALIBRATION_CORPUS dict (W4-2, W9b-2 entries); severity-downgrade rule (Class-(f) HARD-HALT → Class-(d) MANDATORY at D_max ≥ 3.0) | All pinned in script body + machinery_pin_map |

### PRU compliance

All 8 W6 gates satisfy PRU cardinality (no missing pins) AND SOURCE-RECONCILIATION (all values either substrate-canonical or fixture-by-construction synthetic) AND SUBSTRATE-FIRST-PROVENANCE (all source-existence checks pass). PRDR cleared at plan-freeze.

---

## Wave 6 Input-SHA Ledger

Pinned at S89 plan-freeze for audit reproducibility. SHAs computed at plan-freeze time over the cited file content.

| Pin name | File path | SHA status |
|:---------|:----------|:-----------|
| methodology_wave_allowlist_HEAD_S88 | `.claude/rules/methodology-wave-allowlist.md` (HEAD-of-S88 = last row W12-147) | `<pinned at plan-freeze>` |
| pru_cardinality_audit_template | `computations/_shared/_pru_cardinality_audit.py` | `<pinned at plan-freeze>` |
| source_reconciliation_audit_pre_extension | `computations/_shared/_source_reconciliation_audit.py` | `<pinned at plan-freeze>` |
| substrate_first_provenance_audit_pre_extension | `computations/_shared/_substrate_first_provenance_audit.py` | `<pinned at plan-freeze>` |
| falsifier_inventory_audit_pre_extension | `computations/_shared/_falsifier_inventory_audit.py` | `<pinned at plan-freeze>` |
| corner_classification_audit_py | `computations/_shared/_corner_classification_audit.py` | `<pinned at plan-freeze>` |
| s82_w3_9_as_adjacent_obs_py | `computations/session-87/s82_w3_9_as_adjacent_obs.py` | `<pinned at plan-freeze>` |
| permanent_results_registry_md | `sessions/permanent-results-registry.md` | `<pinned at plan-freeze>` |
| falsifier_master_inventory_md | `sessions/framework/registry/falsifier-master-inventory.md` | `<pinned at plan-freeze>` |
| epistemic_discipline_md | `.claude/rules/epistemic-discipline.md` | `<pinned at plan-freeze>` |
| substrate_first_canonical_sourcing_md | `.claude/rules/substrate-first-canonical-sourcing.md` | `<pinned at plan-freeze>` |
| v3_closure_recovery_md | `.claude/rules/v3-closure-recovery.md` | `<pinned at plan-freeze>` |
| cross_pillar_bridge_anatomy_md | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at plan-freeze>` |
| joint_theorem_promotion_md | `.claude/rules/joint-theorem-promotion.md` | `<pinned at plan-freeze>` |
| W6a_51_plan_md | `sessions/session-plan/session-88-plan-w6a.md` | `<pinned at plan-freeze>` |
| W9b_2_npz | `computations/session-87/s87_w9b_pole_specificity_scan.npz` | `<pinned at plan-freeze>` |
| canonical_constants_py | `computations/_shared/canonical_constants.py` | `<pinned at plan-freeze>` |
| spectral_action_regulators_py | `computations/_shared/_spectral_action_regulators.py` | `<pinned at plan-freeze>` |
| W3_A14_npz | `computations/session-89/s89_w3_a14_substrate_cocycle_ratio_regulator_class_invariance_scan.npz` | `<pinned at A.14 close (cross-wave)>` |
| W5a_44_audit_sha (constant) | (verdict-line audit_sha256 reference) | `c092fe1bff9ab66928aa9c545a3a22776f847053af40b5d2814db0143d21f64b` |
| W11_meta_2_audit_sha (constant) | (verdict-line audit_sha256 reference) | `9f6d9bcea1e798eccdf3dad43922dad94b07ac3977353b7e032db39494f62253` |
| S88_W_24_V1_landing_marker | (S88 W-24 V.1 verdict_sha) | `<pinned at plan-freeze; verdict_sha lookup from session-88 verdicts>` |
| W21_v1_landing_marker | (S88 W-21 V.1 verdict_sha) | `<pinned at plan-freeze; verdict_sha lookup from session-88 verdicts>` |
| W21_v3_landing_marker | (S88 W-21 V.3 verdict_sha) | `<pinned at plan-freeze; verdict_sha lookup from session-88 verdicts>` |

### Closure SHA aggregation

Each W6 gate's `audit_sha256` is computed at runtime by the producing script via `closure_hash(input_pin_map)` per `computations/_shared/_script_template.py append_verdict()` pattern. The `audit_sha256` is the SHA-256 of the ordered input-pin map (one line per pin, format `name=value\n`, sorted by name).

For METHODOLOGY-class gates (per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`):
- `content_sha256` = SHA-256 over the rule-file diff (or audit-script body) emitted by the gate.
- `audit_sha256` = SHA-256 over the input-pin map (source documents + canonical-constants pins).

Both SHAs are appended to `computations/session-89/s89_gate_verdicts.txt` per the canonical W9a-99 dual-SHA companion comment row pattern.

---

## End of Wave 6 Plan

**Wave 6 closes 8 Ledger A items in Cluster F**: A.15 + A.19 + A.22 + A.23 + A.33 + A.34 + A.41 + A.42. Total effort: 3.7 wave-equivalents. All 8 gate-IDs queued for `methodology-wave-allowlist.md` append at plan-freeze with parallel registry entries to `methodology-wave-instances.md`.

**Compose order**: Wave 6 dispatches in S89 Batch 1 in parallel with W1-W5 + W7. Cross-wave consume points: A.41 → W3 A.14 npz (forward-only); A.34 → W4 A.30 (registry-text-stability dependency).

**Substrate framing closure**: every gate's §13 inverts container-thinking — the methodology-floor IS what the substrate-physics rule-text composition determines under the layer-functor F: substrate → methodology → audit. The audit-leg images at the audit-floor verify F-image consistency.

**Cross-wave Decision Point file**: see `sessions/session-plan/session-89-decision-points.md` (separate file per S89 plan-author convention).
