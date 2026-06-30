#!/usr/bin/env python3
"""S91 W0 R3 — Parse-tree expansion batch retrofit for 9 pre-S90 §VII entries.

Per `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration
for new §VII entries (S90 W-3 CF-R1-3)"`: pre-S90 §VII entries citing observables
with state-historic labels per `_registry_landing_audit.py STATE_HISTORY_LABEL_PATTERNS`
(11 patterns post-W1-8) MUST be retrofitted with parse-tree expansion blocks at
next-session plan-freeze.

This retrofit:
  1. Identifies 9 retrofit candidates from `s91_w0_r3_class_h_scan.json`
  2. For each, inserts a parse-tree expansion block at a stable tail-of-block
     position (BEFORE the next §VII slot heading; or BEFORE the next-section
     boundary if the slot is the last one)
  3. Uses the canonical template from §VII.AU.OP-PROJ landing-confirmation row
     at registry line 18022 (which already PASSes Class-(h))

Canonical templates:
  α_s_canonical observable:
    α_s_canonical → (n_s_FW_exact² − 1) → (Mellin-residue at substrate-distance-1 pole s=3)² − 1
                  where  n_s_FW_exact = Fraction(9561, 10000)  [canonical_constants.py]
                  and    Mellin-residue at substrate-distance-1 pole s=3 IS the substrate-IS
                         spectrum-only functional Tr(D_K^{−2s})|_{s→3} on (A_K, H_K, D_K)

  n_a^GGE observable:
    n_a^GGE → ⟨ψ_GGE | n_a | ψ_GGE⟩ → |v_a|² → Δ_BCS² / (2(λ_a² + Δ_BCS²))
            where  ψ_GGE  = post-transit Generalized Gibbs Ensemble state
            and    n_a    = a-th occupation operator on substrate Bogoliubov algebra
            and    v_a    = a-th Bogoliubov v-amplitude per S52 BdG canonical form
            and    λ_a    = a-th eigenvalue of D_K
            and    Δ_BCS  = canonical BCS gap pin (canonical_constants.py:Delta_BCS)

Cross-link: `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration"`
canonical worked example at §VII.U.2 Corner II registry line 12961.
"""
import json
import re
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY discipline.
_SHARED_DIR = Path(__file__).resolve().parent  # (local)
sys.path.insert(0, str(_SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as _e:
    print(f"WARNING: canonical_constants.py import failed: {_e}", file=sys.stderr)

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) project root
REGISTRY_FILE = REPO_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
SCAN_JSON = REPO_ROOT / "computations" / "_shared" / "s91_w0_r3_class_h_scan.json"  # (local)


# Parse-tree expansion templates (S91 W0 R3 in-session retrofit canonical forms)
# These match the canonical pattern at §VII.AU.OP-PROJ line 18022 (already-PASS instance).

ALPHA_S_PARSE_TREE = """
**Parse-tree expansion** (S91 W0 R3 in-session retrofit per `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"` SUGGESTION-K=1 grandfather retrofit; closes Class-(h) MISSING-PARSE-TREE-EXPANSION at audit `_registry_landing_audit.py detect_class_h_missing_parse_tree_expansion`):

```
α_s_canonical → (n_s_FW_exact² − 1) → (Mellin-residue at substrate-distance-1 pole s=3)² − 1
              where  n_s_FW_exact = Fraction(9561, 10000)  [canonical_constants.py]
              and    Mellin-residue at substrate-distance-1 pole s=3 IS the substrate-IS
                     spectrum-only functional Tr(D_K^{−2s})|_{s→3} on (A_K, H_K, D_K)
```

The parse-tree reduction lifts the state-history label `α_s_canonical` (post-hoc descriptor of the CMB-running observable's experimental preparation history at Pillar II) to its substrate-IS closed-form expression on the spectral triple algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The reduction shows the observable IS algebra-INVARIANT (spectrum-only) at the parse-tree decision layer per `permanent-results-registry.md §VII.U.2` clause (e) parse-tree decision procedure; the Cell I classification (algebra-INVARIANT × Mellin pole s=3) follows by structural property of the substrate's spectral closure at substrate-distance-1 pole `s=3` per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3.

"""

N_A_GGE_PARSE_TREE = """
**Parse-tree expansion** (S91 W0 R3 in-session retrofit per `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration for new §VII entries (S90 W-3 CF-R1-3)"` SUGGESTION-K=1 grandfather retrofit; closes Class-(h) MISSING-PARSE-TREE-EXPANSION at audit `_registry_landing_audit.py detect_class_h_missing_parse_tree_expansion`):

```
n_a^GGE → ⟨ψ_GGE | n_a | ψ_GGE⟩ → |v_a|² → Δ_BCS² / (2(λ_a² + Δ_BCS²))
        where  ψ_GGE  = post-transit Generalized Gibbs Ensemble state
        and    n_a    = a-th occupation operator on the substrate Bogoliubov algebra
        and    v_a    = a-th Bogoliubov v-amplitude per S52 BdG canonical form
        and    λ_a    = a-th eigenvalue of D_K
        and    Δ_BCS  = canonical BCS gap pin (canonical_constants.py: Delta_BCS)
```

The parse-tree reduction lifts the state-history label `n_a^GGE` (post-hoc descriptor of the GGE-state preparation history at the post-transit BdG laboratory) to its substrate-IS closed-form expression on the spectral triple `(A_K, H_K, D_K)` via the S52 Bogoliubov canonical amplitudes. The closed form `Δ_BCS² / (2(λ_a² + Δ_BCS²))` is spectrum-only (depends only on `{λ_a, Δ_BCS}`), making the observable algebra-INVARIANT at the parse-tree decision layer per `permanent-results-registry.md §VII.U.2` clause (e). The Cell II classification (algebra-INVARIANT × Mellin pole s=4) for moment-aggregated observables like `Var_a(n_a^GGE)` follows by structural property of the substrate Bogoliubov algebra per `permanent-results-registry.md §VII.U.2` Corner II canonical worked example at registry line 12961.

"""

BOTH_PARSE_TREE = ALPHA_S_PARSE_TREE + N_A_GGE_PARSE_TREE


def find_next_slot_heading(lines: list[str], start_idx: int) -> int:
    """Return line index of next `## §` or `### §` slot heading after start_idx; or len(lines) if none."""
    slot_re = re.compile(r"^(##|###) §VII\.")  # (local)
    for k in range(start_idx + 1, len(lines)):
        if slot_re.match(lines[k]):
            return k
    return len(lines)


def main():
    if not SCAN_JSON.exists():
        print(f"ERROR: scan JSON not found at {SCAN_JSON}", file=sys.stderr)
        sys.exit(1)

    scan_data = json.loads(SCAN_JSON.read_text(encoding="utf-8"))
    retrofit_candidates = [
        r for r in scan_data
        if r["diagnostic"] == "MISSING-PARSE-TREE-EXPANSION"
    ]
    print(f"Retrofit candidates: {len(retrofit_candidates)}")
    for r in retrofit_candidates:
        print(f"  {r['slot_label']:<35} line {r['line_start']:<6} labels={r['state_history_label_matches']}")

    # Load registry
    text = REGISTRY_FILE.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    pre_len = len(text)  # (local)

    # Determine template per slot — based on state-history labels detected
    inserts = []  # (local) list[(insert_at_line_idx, template_text)]
    for r in retrofit_candidates:
        line_start = r["line_start"]  # 1-indexed
        labels = set(r["state_history_label_matches"])
        has_alpha_s = "α_s_canonical" in labels
        has_n_a_gge = "n_a^GGE" in labels

        if has_alpha_s and has_n_a_gge:
            template = BOTH_PARSE_TREE
            kind = "BOTH"
        elif has_alpha_s:
            template = ALPHA_S_PARSE_TREE
            kind = "α_s"
        elif has_n_a_gge:
            template = N_A_GGE_PARSE_TREE
            kind = "n_a^GGE"
        else:
            print(f"WARNING: unrecognized state-history labels {labels} at {r['slot_label']}; skipping", file=sys.stderr)
            continue

        # Insert at tail of slot block (just before next slot heading)
        heading_idx = line_start - 1  # 0-indexed
        next_slot_idx = find_next_slot_heading(lines, heading_idx)
        # Insert position: at next_slot_idx (i.e., right BEFORE the next slot heading)
        inserts.append((next_slot_idx, template, r["slot_label"], r["line_start"], kind))

    # Apply inserts in REVERSE order so earlier line indices don't shift later inserts
    inserts.sort(key=lambda x: -x[0])
    print(f"\nApplying {len(inserts)} inserts (reverse order):")
    for insert_idx, template, slot_label, line_start_1idx, kind in inserts:
        # Insert template at lines[insert_idx]
        lines.insert(insert_idx, template)
        print(f"  Inserted {kind:<10} parse-tree expansion at line {insert_idx+1} (slot {slot_label} starts at line {line_start_1idx})")

    # Write back
    new_text = "".join(lines)
    post_len = len(new_text)  # (local)
    REGISTRY_FILE.write_text(new_text, encoding="utf-8")
    print(f"\nRegistry update complete: {post_len - pre_len} bytes added.")

    # Re-run scan to verify
    print(f"\nRe-running Class-(h) scan to verify retrofit completion...")
    import importlib
    import s91_w0_r3_class_h_scan as scan_mod
    importlib.reload(scan_mod)
    # Re-execute the scan logic
    text2 = REGISTRY_FILE.read_text(encoding="utf-8")
    slots2 = scan_mod.extract_all_slots(text2)
    from _registry_landing_audit import detect_class_h_missing_parse_tree_expansion
    missing_after = []  # (local)
    for slot in slots2:
        diag = detect_class_h_missing_parse_tree_expansion(slot["block_text"], slot["slot_label"])
        if diag["diagnostic"] == "MISSING-PARSE-TREE-EXPANSION":
            missing_after.append((slot["slot_label"], slot["line_start"]))
    print(f"Post-retrofit MISSING-PARSE-TREE-EXPANSION count: {len(missing_after)}")
    if missing_after:
        for label, line_start in missing_after:
            print(f"  STILL MISSING: {label} line {line_start}")
    else:
        print(f"  ALL 9 retrofit candidates now PASS Class-(h).")


if __name__ == "__main__":
    main()
