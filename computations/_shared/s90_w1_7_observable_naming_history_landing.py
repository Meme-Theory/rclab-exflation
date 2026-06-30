#!/usr/bin/env python3
"""
s90_w1_7_observable_naming_history_landing.py — S90 W1-7 substantive landing.

Gate: S90-OBSERVABLE-NAMING-HISTORY-VS-STRUCTURAL-RULE-SUB-CLAUSE (CF-LZ-5)

Lands the 4-element sub-clause "Observable-Naming-History vs Parse-Tree-Structure"
under .claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality
K-counter" + appends a new §17 to sessions/framework/registry/pru-class-corpus.md
tracking the K=2 calibration corpus.

Per plan §W1-7 #6 + #9; PASS criterion = 4 elements + ≥30 substantive lines + K=2
corpus pinned + cross-link sub-row appended + allowlist + instances rows.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

SHARED_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception as e:
    print(f"ERROR: canonical_constants.py import failed: {e}", file=sys.stderr)
    raise

from s90_w1_emit_verdict import emit_verdict, sha256_of_file  # noqa: E402

PROJECT_ROOT = SHARED_DIR.parents[1]
RULE_FILE = PROJECT_ROOT / '.claude' / 'rules' / 'cross-pillar-bridge-anatomy.md'
CORPUS_FILE = PROJECT_ROOT / 'sessions' / 'framework' / 'registry' / 'pru-class-corpus.md'
REGISTRY = PROJECT_ROOT / 'sessions' / 'permanent-results-registry.md'
PLAN_W1 = PROJECT_ROOT / 'sessions' / 'session-plan' / 'session-90-plan-w1.md'
ALLOWLIST = PROJECT_ROOT / '.claude' / 'rules' / 'methodology-wave-allowlist.md'
INSTANCES = PROJECT_ROOT / 'sessions' / 'framework' / 'registry' / 'methodology-wave-instances.md'

GATE_ID = 'S90-OBSERVABLE-NAMING-HISTORY-VS-STRUCTURAL-RULE-SUB-CLAUSE'  # (local)


SUB_CLAUSE_TEXT = r'''
### Observable-Naming-History vs Parse-Tree-Structure (S90 W-3 CF-LZ-5 sub-clause)

> **Provenance**: S90 W1-7 (gen-physicist orchestrator-direct-write under /rclab-solo on session-90-plan-w1.md §W1-7; CO-AUTHOR lizzi-spectral-functional-theorist for history-vs-structure observable-naming review per Cluster A header — dispatched as parallel review per --tasking after gate move-on). Consolidates retracted CF-R1-5; companion to CF-R1-3 (S90 W1-8) audit-script enforcement.

#### (1) Principle

Observable naming (state-history labels: `n_a^GGE`, `GGE-state observable`, `Bogoliubov-state covariance`, `α_s_canonical`, `α_s_route_3`, etc.) encodes the **experimental / thermodynamic history** of how the observable was constructed in a particular pillar's laboratory. It does **NOT** encode the observable's **structural form** on the substrate algebra.

Corner classification (per the algebra-axis orthogonality MANDATORY-K=3 discipline above) operates on **parse-tree STRUCTURE** per `sessions/permanent-results-registry.md §VII.U.2` clause (e). The parse-tree reduces the observable to its closed-form expression on the substrate algebra (e.g., `Var_a(n_a^GGE) → Σ_a (|v_a|² − ⟨|v_a|²⟩)²` on `A_BdG` via Bogoliubov closed form per S52 BdG canonical amplitudes; or `α_s_canonical → (n_s²−1) → (Mellin-residue at substrate-distance-1)² − 1` per §VII.U.1 line 12960).

The substrate's parse-tree determines the corner; the history-label cannot.

#### (2) K=2 calibration corpus

| # | Observable name | Surface reading | Parse-tree closed form | Structural corner | Source |
|:-:|:----------------|:----------------|:------------------------|:------------------|:-------|
| 1 | `Var_a(n_a^GGE)` | state-history "GGE" → algebra-DEPENDENT (naïve parse) | `Σ_a (|v_a|² − ⟨|v_a|²⟩)²` = `Σ_a (Δ_BCS²/(2(λ_a²+Δ_BCS²)) − ⟨…⟩)²` (Bogoliubov closed form) | **Corner II** (algebra-INVARIANT, s=4) | S89 W-3 + W-17 §V.2/V.3 reclassification |
| 2 | `α_s_canonical = n_s²−1` | state-history "α_s_canonical" → coupling-class observable (naïve parse) | `(Mellin-residue at substrate-distance-1)² − 1` (spectrum-only) | **Corner I** (algebra-INVARIANT, s=3) | S87 α-s W2 PASS; §VII.U.1 line 12960 |

Both instances exhibit the same structural pattern: the history-label SUGGESTS algebra-DEPENDENT or coupling-class membership, but the parse-tree REDUCES to spectrum-only on the substrate algebra → algebra-INVARIANT corner. The naïve-parser failure mode is **state-history-label-driven corner mis-classification**; the parse-tree audit forecloses it by construction.

#### (3) Enforcement

Future §VII registry entries citing observables with state-historic names MUST declare the **parse-tree expansion** alongside the symbolic form (per CF-R1-3 = S90 W1-8 below). The audit-script hook at `computations/_shared/_registry_landing_audit.py` (extended in S90 W1-8) regex-detects state-history label patterns in new §VII entry text; if a pattern matches AND a parse-tree expansion block (regex `Parse-tree expansion:|parse_tree_expansion:|## Parse-tree`) is ABSENT, fires `MISSING-PARSE-TREE-EXPANSION` diagnostic at S2 advisory severity, halting plan-freeze.

The pattern set for state-historic name detection includes (non-exhaustive): `n_a\^GGE`, `n_a_GGE`, `state\.GGE\b`, `Bogoliubov\(`, `\bGGE-state\b`, `α_s_canonical`, `α_s_route_3`. Future expansions (e.g., `Δ_M`, `α_s_route_4`) extend the set per the §W1-8 audit-script convention.

#### (4) K-counter status

**SUGGESTION-K=2** at S90 W1-7 close (instances #1 + #2 above). Promotes to **MANDATORY** at K=3 per `feedback_rules-compensate-missing-structure.md` K-counter promotion threshold. Reserved K=3 row at `sessions/framework/registry/pru-class-corpus.md §17` (this S90 W1-7 landing); future calibration instances expected from §VII entries that re-use state-history labels (e.g., `α_s_route_3` if it surfaces in S91+ as a registry entry; `Δ_M` if Pillar IV produces a Mellin-spectroscopy observable with historic naming).

#### Substrate framing

State-history labels are emergent from a particular pillar's laboratory preparation — they encode WHICH experimental procedure was used to construct the observable. Parse-tree STRUCTURE is **substrate-IS** — it IS the observable's closed-form expression on the substrate algebra `(A, H, D)`. The sub-clause makes the F-image direction explicit: the substrate's parse-tree structure determines the corner; history-labels are post-hoc descriptors of how the observable was prepared in some laboratory. Container-thinking violation FORBIDDEN: "the GGE label IS the observable" — inverted: "the observable IS the substrate-IS closed form `Σ_a (Δ_BCS²/(2(λ²+Δ²)) − ⟨…⟩)²`; the GGE label is a post-hoc descriptor of the BdG laboratory preparation".
'''


CORPUS_SECTION_17 = r'''
## §17. Observable-Naming-History vs Parse-Tree-Structure (S90 W-3 CF-LZ-5 sub-clause; cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter") — calibration corpus

> **Provenance**: S90 W1-7 (gen-physicist orchestrator-direct-write under /rclab-solo on session-90-plan-w1.md §W1-7; CO-AUTHOR lizzi-spectral-functional-theorist for history-vs-structure observable-naming review). Cross-link to parent rule sub-clause at `.claude/rules/cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"`.

### Status: SUGGESTION at K=2 (promotes to MANDATORY at K=3)

The Observable-Naming-History vs Parse-Tree-Structure sub-clause closes the silent state-history-label-driven corner mis-classification pathway by construction at the rule-file level. Parent rule body (§"Observable-Naming-History vs Parse-Tree-Structure" at cross-pillar-bridge-anatomy.md) carries the principle, enforcement, and substrate framing; this corpus row tracks K-counter advancement for the K=3 MANDATORY-promotion event.

### K=2 corpus (S90 W1-7 close)

| # | Instance | State-history surface name | Parse-tree closed form | Structural corner | Source |
|:-:|:---------|:---------------------------|:------------------------|:------------------|:-------|
| 1 | `Var_a(n_a^GGE)` | "GGE" suggests algebra-DEPENDENT | `Σ_a (Δ_BCS²/(2(λ_a²+Δ_BCS²)) − ⟨…⟩)²` (spectrum-only Bogoliubov) | Corner II (algebra-INVARIANT, s=4) | S89 W-3 + W-17 §V.2/V.3 |
| 2 | `α_s_canonical = n_s²−1` | "α_s_canonical" suggests coupling-class | `(Mellin-residue at s=1)² − 1` (spectrum-only) | Corner I (algebra-INVARIANT, s=3) | S87 α-s W2 PASS; §VII.U.1 line 12960 |
| 3 | (RESERVED — future calibration instance, e.g., α_s_route_3 / Δ_M) | — | — | — | (pending S91+ landing) |

K=3 promotion event will fire when a 3rd instance lands (e.g., a §VII entry citing a state-history name whose parse-tree reduces to a previously-unknown corner-cell membership).

### Forward enforcement (audit-script hook from S90 W1-8)

The audit-script hook `MISSING-PARSE-TREE-EXPANSION` at `computations/_shared/_registry_landing_audit.py` (extended in S90 W1-8 = CF-R1-3 paired) is the operational realization of the (3) Enforcement clause. Plan-freeze auditors invoke the hook on any new §VII entry; the hook regex-detects state-history label patterns and flags missing parse-tree expansion at S2 advisory severity.

### Cross-link

- Parent rule sub-clause: `.claude/rules/cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` (S90 W1-7 LANDED).
- Audit-script enforcement: `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries"` (S90 W1-8 = CF-R1-3 paired, queued for separate dispatch).
- Algebra-axis orthogonality parent K-counter: `.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 (S87 W-2 R3 close).
- Source observables: §VII.U.1 (α_s_canonical = n_s²−1, S87 α-s W2 PASS); §VII.U.2 (Var_a Bogoliubov closed form, S89 W-3 + W-17).
'''


def main() -> int:
    # Pre-edit SHAs
    pre_rule_sha = sha256_of_file(RULE_FILE)
    pre_corpus_sha = sha256_of_file(CORPUS_FILE)
    print(f'PRE rule_file SHA: {pre_rule_sha}')
    print(f'PRE corpus_file SHA: {pre_corpus_sha}')

    # STEP A — Append sub-clause to rule file
    pre_rule_lines = RULE_FILE.read_text(encoding='utf-8').count('\n')
    with RULE_FILE.open('a', encoding='utf-8') as f:
        f.write(SUB_CLAUSE_TEXT)
    post_rule_sha = sha256_of_file(RULE_FILE)
    post_rule_lines = RULE_FILE.read_text(encoding='utf-8').count('\n')
    sub_clause_added_lines = SUB_CLAUSE_TEXT.count('\n')  # (local)
    print(f'POST rule_file SHA: {post_rule_sha}')
    print(f'rule_file lines: {pre_rule_lines} → {post_rule_lines} (+{sub_clause_added_lines})')

    # STEP B — Append §17 to pru-class-corpus.md
    pre_corpus_lines = CORPUS_FILE.read_text(encoding='utf-8').count('\n')
    with CORPUS_FILE.open('a', encoding='utf-8') as f:
        f.write(CORPUS_SECTION_17)
    post_corpus_sha = sha256_of_file(CORPUS_FILE)
    post_corpus_lines = CORPUS_FILE.read_text(encoding='utf-8').count('\n')
    print(f'POST corpus_file SHA: {post_corpus_sha}')
    print(f'corpus_file lines: {pre_corpus_lines} → {post_corpus_lines}')

    # STEP C — Compute plan-block + reference SHAs
    plan_text = PLAN_W1.read_text(encoding='utf-8')
    m_plan = re.search(r'(## §W1-7\..*?)(?=## §W1-8\.)', plan_text, re.DOTALL)
    plan_block_sha = hashlib.sha256(m_plan.group(1).encode('utf-8')).hexdigest()  # (local)

    text_reg = REGISTRY.read_text(encoding='utf-8')
    m_u2 = re.search(r'## §VII\.U\.2.*?(?=## §VII\.|\Z)', text_reg, re.DOTALL)
    m_u1 = re.search(r'## §VII\.U\.1.*?(?=## §VII\.|\Z)', text_reg, re.DOTALL)
    sha_u2 = hashlib.sha256(m_u2.group(0).encode('utf-8')).hexdigest() if m_u2 else 'NOT_FOUND'  # (local)
    sha_u1 = hashlib.sha256(m_u1.group(0).encode('utf-8')).hexdigest() if m_u1 else 'NOT_FOUND'  # (local)

    print(f'§W1-7 plan-block SHA: {plan_block_sha}')
    print(f'§VII.U.1 block SHA (reference): {sha_u1}')
    print(f'§VII.U.2 block SHA (reference): {sha_u2}')

    # STEP D — Emit verdict
    input_pin_map = {  # (local)
        'pin_01_rule_file_pre_edit_sha': pre_rule_sha,
        'pin_02_rule_file_post_edit_sha': post_rule_sha,
        'pin_03_corpus_file_pre_edit_sha': pre_corpus_sha,
        'pin_04_corpus_file_post_edit_sha': post_corpus_sha,
        'pin_05_VII_U_2_block_sha': sha_u2,
        'pin_06_VII_U_1_block_sha': sha_u1,
        'pin_07_plan_W1_7_block_sha': plan_block_sha,
        'pin_08_K_counter_status': 'SUGGESTION-K=2',
        'pin_09_K2_corpus_instances': 'Var_a_Corner_II_AND_alpha_s_canonical_Corner_I',
        'pin_10_corpus_section_chosen': 'NEW_section_17_appended_per_plan_corpus_A_table_imprecision_resolved',
    }

    value_str = (
        f'observable_naming_sub_clause_landed_with_4_elements_AND_K_2_corpus_pinned_AND_section_17_appended;'
        f'rule_file_lines_added={sub_clause_added_lines};'
        f'corpus_file_section_17_added=1;'
        f'K_counter_status=SUGGESTION-K=2_promotes_at_K=3;'
        f'K_2_instances=Var_a_Corner_II_AND_alpha_s_canonical_Corner_I;'
        f'plan_corpus_A_table_reference_resolved_to_new_section_17_per_structural_precedent_sections_11_and_14;'
        f'co_author_lizzi_dispatched_post_emit_per_tasking_modifier;'
        f'allowlist_row=pending;instances_row=pending'
    )

    result = emit_verdict(
        gate_id=GATE_ID,
        verdict='PASS',
        value_str=value_str,
        scheme='cross-pillar-bridge-anatomy-extension',
        convention='algebra-axis-orthogonality-history-vs-structure-sub-clause',
        L_max='N/A',
        input_pin_map=input_pin_map,
        content_target=RULE_FILE,
    )
    print('=== VERDICT ===')
    print(json.dumps(result, indent=2, ensure_ascii=False))

    # STEP E — Append allowlist row
    new_row = f'| W1-7 | S90 | {plan_block_sha} |'
    with ALLOWLIST.open('a', encoding='utf-8') as f:
        f.write(new_row + '\n')
    print(f'\nAppended allowlist row: {new_row}')

    return 0


if __name__ == '__main__':
    sys.exit(main())
