#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93 W3-6 in-session CORNER-CELL REMEDIATION: §VII.AV.OP-PROJ  Cell I -> Cell II
==============================================================================

Confirmed in-session classification-defect fix (orchestrator adjudication, objective).
The W3-1/W3-5 landing mislabeled §VII.AV.OP-PROJ as **Cell I**. Per the §VII.U.2
4-corner partition (`permanent-results-registry.md:12998/12999`):

    Cell I  = algebra-INVARIANT × Mellin pole s=3
    Cell II = algebra-INVARIANT × Mellin pole s=4
    Cell IV = algebra-DEPENDENT × Mellin pole s=4

§VII.AV.OP-PROJ is the trace-residue Tr_{A_K}(P_a·|D_K|^{-2s}) at substrate-distance-2
pole **s=4**, algebra-INVARIANT  =>  **Cell II**, NOT Cell I. Direct precedent:
the Var_a Cell I -> Cell II retraction (CF-25 S90 W2, registry:13043) for exactly
this reason (algebra-INVARIANT × s=4 is Cell II).

This is NOT convention-shopping: the corner-cell is FORCED by the source-pinned
4-corner partition definition (algebra-axis × Mellin-pole), not a free choice.
vdd's Axis-A OP-PROJ corner-cell FAIL CAUGHT this defect — that is the Stage-2
verify's PURPOSE.

SCOPE DISCIPLINE (load-bearing): remediate ONLY the §VII.AV.OP-PROJ cell markers.
Do NOT touch the GENERIC "Cell I (algebra-INVARIANT ... × substrate-distance-1)"
boilerplate in the cross-corner-co-primary-FORBIDDEN rule citations (registry
lines ~18634/18682) — those correctly cite the canonical Cell I = INVARIANT × s=3
definition and are NOT §VII.AV.OP-PROJ references. Each replacement below carries
full surrounding context so it matches EXACTLY ONE site.

Single-shot AFTER pattern per `registry-landing.md §"Bridge-Landing Script
Architecture"`: build_full_text_in_memory -> write_atomic_with_fsync ->
re_read + verify_all_markers_flipped -> report ONCE. This script emits NO verdict
line of its own (it is the registry-edit half of W3-6; the W3-6 verdict line is
emitted by s93_w3_6_vii_av_stage_2_cross_axis_verify.py --emit). Re-runs are
idempotent (already-Cell-II text is detected and the no-op is reported).

mack-cosmic-bridge is the SOLE registry writer per `feedback_mack-bridge-role.md`.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
# Pure registry-text remediation: consumes NO framework constants. Import kept for
# math-scripts.md S34+ compliance; the cell markers (Cell I/II, s=3/s=4) are sourced
# from the §VII.U.2 4-corner partition at permanent-results-registry.md:12998-12999,
# NOT from canonical_constants.py.
from canonical_constants import tau_fold as _tau_fold  # noqa: E402,F401  # (local) compliance-only

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

# ---------------------------------------------------------------------------
# Targeted replacements. Each (old, new) pair is UNIQUE in the file by context.
# These touch ONLY §VII.AV.OP-PROJ cell markers (index row, sub-slot body,
# three-object map, STATE-PROJ cross-refs to OP-PROJ's cell, parent host body).
# The generic "Cell I (algebra-INVARIANT ... substrate-distance-1)" boilerplate
# is NOT in this list.
# ---------------------------------------------------------------------------
REPLACEMENTS = [  # (local)
    # --- index row 143 (parent §VII.AV split row) ---
    (
        "SPLIT (S93 W3-1) into §VII.AV.OP-PROJ (Cell I; algebra-INVARIANT spectrum-only trace-residue",
        "SPLIT (S93 W3-1) into §VII.AV.OP-PROJ (Cell II; algebra-INVARIANT spectrum-only trace-residue",
    ),
    # --- sub-slot heading (18445) ---
    (
        "### §VII.AV.OP-PROJ — Cell-I OP-PROJ Trace-Residue Sub-Slot (S93 W3-1",
        "### §VII.AV.OP-PROJ — Cell-II OP-PROJ Trace-Residue Sub-Slot (S93 W3-1",
    ),
    # --- Corner-cell line (18451): the cell marker + pole are now CONSISTENT (II=INVARIANT×s=4) ---
    (
        "**Corner-cell**: **Cell I** (algebra-INVARIANT spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification. The trace-residue `B_LAYER_A` is a spectrum-only functional of `D_K` with NO state-pair dependence; its parse-tree terminus is `Tr`, which FORCES the Cell-I classification",
        "**Corner-cell**: **Cell II** (algebra-INVARIANT spectrum-only functional `F({λ_k, m_k}) = Σ_k m_k g(λ_k)` × substrate-distance-2 pole `s=4`) per `permanent-results-registry.md §VII.U.2` 4-corner classification (Cell II = INVARIANT × s=4 per registry:12999; CORRECTED from Cell I in-session at S93 W3-6 per the §VII.U.2 partition — Cell I is INVARIANT × s=3; direct precedent: Var_a Cell I→Cell II retraction CF-25 S90 W2 at registry:13043). The trace-residue `B_LAYER_A` is a spectrum-only functional of `D_K` with NO state-pair dependence; its parse-tree terminus is `Tr` (algebra-INVARIANT), and the substrate-distance-2 pole is `s=4`, which together FORCE the Cell-II classification",
    ),
    # --- parse-tree terminus line (18453) ---
    (
        "The closed form is a spectrum-only sum `Σ_k m_k |λ_k|^{-2s}` — Cell-I terminus by `Tr`.",
        "The closed form is a spectrum-only sum `Σ_k m_k |λ_k|^{-2s}` — algebra-INVARIANT by `Tr` terminus; at substrate-distance-2 pole `s=4` this is the Cell-II corner (INVARIANT × s=4).",
    ),
    # --- OP-PROJ orthogonal-companion declaration (18471): 4 sites in one line ---
    (
        "§VII.AV.OP-PROJ (Cell I) and §VII.AV.STATE-PROJ (Cell IV) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: criterion (4) requires both co-primary anchors to be on the SAME algebra-axis cell, but `corner_cell(OP-PROJ) = Cell I ≠ Cell IV = corner_cell(STATE-PROJ)`. Cell I (algebra-INVARIANT spectrum-only) and Cell IV (algebra-DEPENDENT state-pair) live on ORTHOGONAL algebra-axes; when both projection-side readings are independently registry-eligible the correct anchor structure is structural-orthogonal-companion. Cross-corner cross-pole magnitude comparison of `B_LAYER_A` (Cell I × s=4) against `L_emp` (Cell IV × s=4)",
        "§VII.AV.OP-PROJ (Cell II) and §VII.AV.STATE-PROJ (Cell IV) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: criterion (4) requires both co-primary anchors to be on the SAME algebra-axis cell, but `corner_cell(OP-PROJ) = Cell II ≠ Cell IV = corner_cell(STATE-PROJ)`. Cell II (algebra-INVARIANT spectrum-only × s=4) and Cell IV (algebra-DEPENDENT state-pair × s=4) live on ORTHOGONAL algebra-axes (same Mellin pole `s=4`, orthogonal algebra-axis); when both projection-side readings are independently registry-eligible the correct anchor structure is structural-orthogonal-companion. Cross-corner cross-pole magnitude comparison of `B_LAYER_A` (Cell II × s=4) against `L_emp` (Cell IV × s=4)",
    ),
    # --- split-source line (18473): "(LAYER-A, Cell I)" ---
    (
        "The W3-9 disambiguation found `B_LAYER_A=3.752271e+02` (LAYER-A, Cell I) and `B_LAYER_B=-7.046336` (LAYER-B, Cell IV)",
        "The W3-9 disambiguation found `B_LAYER_A=3.752271e+02` (LAYER-A, Cell II) and `B_LAYER_B=-7.046336` (LAYER-B, Cell IV)",
    ),
    # --- substrate-framing line (18475) ---
    (
        "the OP-PROJ trace-residue `B_LAYER_A` IS the algebra-INVARIANT spectrum-only image at Cell I × substrate-distance-2 pole `s=4`. Direction of explanation:",
        "the OP-PROJ trace-residue `B_LAYER_A` IS the algebra-INVARIANT spectrum-only image at Cell II × substrate-distance-2 pole `s=4`. Direction of explanation:",
    ),
    # --- cross-references line (18488) ---
    (
        '`.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell I (algebra-INVARIANT) classification + cross-corner co-primary FORBIDDEN.',
        '`.claude/rules/cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 — Cell II (algebra-INVARIANT × s=4) classification + cross-corner co-primary FORBIDDEN.',
    ),
    # --- STATE-PROJ orthogonal-companion declaration (18525): refs OP-PROJ's cell ---
    (
        "§VII.AV.STATE-PROJ (Cell IV) and §VII.AV.OP-PROJ (Cell I) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: `corner_cell(STATE-PROJ) = Cell IV ≠ Cell I = corner_cell(OP-PROJ)`. The K-window log-derivative is a state-pair functional on the BdG sub-algebra, NOT a spectrum-only-functional image — period. Cross-corner cross-pole magnitude comparison of `L_emp` (Cell IV × s=4) against `B_LAYER_A` (Cell I × s=4)",
        "§VII.AV.STATE-PROJ (Cell IV) and §VII.AV.OP-PROJ (Cell II) are **STRUCTURAL-ORTHOGONAL-COMPANIONS, NOT SOURCE-DOUBLE-CITE-CO-PRIMARY**. Cross-corner co-primary is STRUCTURALLY FORBIDDEN: `corner_cell(STATE-PROJ) = Cell IV ≠ Cell II = corner_cell(OP-PROJ)`. The K-window log-derivative is a state-pair functional on the BdG sub-algebra, NOT a spectrum-only-functional image — period. Cross-corner cross-pole magnitude comparison of `L_emp` (Cell IV × s=4) against `B_LAYER_A` (Cell II × s=4)",
    ),
    # --- STATE-PROJ cross-reference (18548) ---
    (
        "- §VII.AV.OP-PROJ (the structural-orthogonal-companion sub-slot; Cell I).",
        "- §VII.AV.OP-PROJ (the structural-orthogonal-companion sub-slot; Cell II).",
    ),
    # --- parent host body sub-slot list (18562) ---
    (
        "- **§VII.AV.OP-PROJ** (Cell I; algebra-INVARIANT spectrum-only trace-residue `B_LAYER_A = 3.752271e+02 M_KK²` over PW sectors `{(0,2),(1,1),(2,0)}`; substrate-distance-2 pole `s=4`)",
        "- **§VII.AV.OP-PROJ** (Cell II; algebra-INVARIANT spectrum-only trace-residue `B_LAYER_A = 3.752271e+02 M_KK²` over PW sectors `{(0,2),(1,1),(2,0)}`; substrate-distance-2 pole `s=4`)",
    ),
    # --- parent host body anchor-structure (18565) ---
    (
        "`corner_cell(OP-PROJ) = Cell I ≠ Cell IV = corner_cell(STATE-PROJ)`; cross-corner co-primary is STRUCTURALLY FORBIDDEN (criterion (4): both co-primary anchors MUST be on the SAME algebra-axis cell).",
        "`corner_cell(OP-PROJ) = Cell II ≠ Cell IV = corner_cell(STATE-PROJ)`; cross-corner co-primary is STRUCTURALLY FORBIDDEN (criterion (4): both co-primary anchors MUST be on the SAME algebra-axis cell).",
    ),
    # --- parent host body disambiguation (18567) ---
    (
        "it separates **Cell I OP-PROJ `B_LAYER_A`** (algebra-INVARIANT) from **Cell IV STATE-PROJ `L_emp`** (algebra-DEPENDENT)",
        "it separates **Cell II OP-PROJ `B_LAYER_A`** (algebra-INVARIANT × s=4) from **Cell IV STATE-PROJ `L_emp`** (algebra-DEPENDENT × s=4)",
    ),
    # --- three-object-map preamble (18577): "the parse-tree fixes the corner (Cell IV vs Cell I)" ---
    (
        "eigenvalues first — the gap sets the curvature (the single anchor), the cutoff dresses it (the diagnostic sub-row), the parse-tree fixes the corner (Cell IV vs Cell I).",
        "eigenvalues first — the gap sets the curvature (the single anchor), the cutoff dresses it (the diagnostic sub-row), the parse-tree fixes the corner (Cell IV vs Cell II).",
    ),
    # --- three-object-map table row (iii) (18585): two cell markers in one row ---
    (
        "| **(iii)** | Cell-I OP-PROJ trace-residue `Tr_{A_K}(P_a · \\|D_K\\|^{-2s})` at `s=4` over PW sectors `{(0,2),(1,1),(2,0)}` | Cell I · §VII.AV.OP-PROJ |",
        "| **(iii)** | Cell-II OP-PROJ trace-residue `Tr_{A_K}(P_a · \\|D_K\\|^{-2s})` at `s=4` over PW sectors `{(0,2),(1,1),(2,0)}` | Cell II · §VII.AV.OP-PROJ |",
    ),
    # --- within-Cell-IV re-scope (18591): "separates Cell I from Cell IV" ---
    (
        "This within-Cell-IV regulator-class divergence is STRUCTURALLY DISTINCT from the cross-corner OP-PROJ/STATE-PROJ split (object (iii) vs object (i)), which separates Cell I from Cell IV per the S92 §W3-9 disambiguation",
        "This within-Cell-IV regulator-class divergence is STRUCTURALLY DISTINCT from the cross-corner OP-PROJ/STATE-PROJ split (object (iii) vs object (i)), which separates Cell II from Cell IV per the S92 §W3-9 disambiguation",
    ),
    # --- object (iii) detail block (18593): "(... Cell I)" ---
    (
        "**Object (iii) — OP-PROJ trace-residue** (`B_LAYER_A = 3.752271e+02 M_KK²`, Cell I): **LANDED as a Level-3 anchor**",
        "**Object (iii) — OP-PROJ trace-residue** (`B_LAYER_A = 3.752271e+02 M_KK²`, Cell II): **LANDED as a Level-3 anchor**",
    ),
    # --- ASCII three-object map (18605) ---
    (
        "  (iii) Cell I  OP-PROJ     B_LAYER_A = 3.752271e+02     -> OP-PROJ Level-3 anchor (W3-3-gated; PASS => landed)",
        "  (iii) Cell II OP-PROJ     B_LAYER_A = 3.752271e+02     -> OP-PROJ Level-3 anchor (W3-3-gated; PASS => landed)",
    ),
    # --- ASCII cross-corner split label (18608) ---
    (
        "  cross-corner split:      (iii) vs (i) is Cell I vs Cell IV (S92 W3-9 MANDATORY split)",
        "  cross-corner split:      (iii) vs (i) is Cell II vs Cell IV (S92 W3-9 MANDATORY split)",
    ),
]


def build_full_text(text: str) -> tuple[str, list[str]]:
    """Apply all replacements in memory. Return (new_text, applied_log)."""
    applied: list[str] = []  # (local)
    out = text  # (local)
    for old, new in REPLACEMENTS:
        n = out.count(old)  # (local)
        if n == 1:
            out = out.replace(old, new)
            applied.append(f"OK   (1 site): {old[:70]}...")
        elif n == 0:
            # idempotent: maybe already Cell II (re-run) — check the new form exists
            if out.count(new) >= 1:
                applied.append(f"SKIP (already Cell II): {new[:60]}...")
            else:
                applied.append(f"MISS (0 sites; NOT already-Cell-II): {old[:70]}...")
        else:
            applied.append(f"AMBIGUOUS ({n} sites — REFUSED): {old[:60]}...")
    return out, applied


def main() -> int:
    print("=== §VII.AV.OP-PROJ Cell I -> Cell II in-session remediation (S93 W3-6) ===")
    text = REGISTRY.read_text(encoding="utf-8")  # (local)

    new_text, applied = build_full_text(text)  # (local) Step 1: build in memory
    for line in applied:
        print("  " + line)

    misses = [a for a in applied if a.startswith("MISS")]  # (local)
    ambiguous = [a for a in applied if a.startswith("AMBIGUOUS")]  # (local)
    if ambiguous:
        print("FATAL: ambiguous replacement(s) — REFUSED (would corrupt generic Cell I boilerplate).")
        for a in ambiguous:
            print("  " + a)
        return 2
    if misses:
        print("FATAL: replacement target(s) not found and not already-Cell-II.")
        for m in misses:
            print("  " + m)
        return 2

    if new_text == text:
        print("IDEMPOTENT: all markers already Cell II; no write.")
        return 0

    # Step 2: write atomically with fsync
    tmp = REGISTRY.with_name(REGISTRY.name + ".tmp_cellii")  # (local)
    with tmp.open("w", encoding="utf-8") as fp:
        fp.write(new_text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, REGISTRY)

    # Step 3: re-read + verify ALL §VII.AV.OP-PROJ Cell-I markers are flipped
    reread = REGISTRY.read_text(encoding="utf-8")  # (local)
    residual_bad: list[str] = []  # (local)
    for old, _new in REPLACEMENTS:
        if old in reread:
            residual_bad.append(old[:70])
    # also assert the generic substrate-distance-1 Cell I boilerplate is INTACT
    generic_boilerplate = (  # (local)
        "Cross-corner co-primary structures with Cell I (algebra-INVARIANT "
        "spectrum-only-functional × substrate-distance-1)"
    )
    boilerplate_intact = generic_boilerplate in reread  # (local)

    print()
    print(f"VERIFY: residual §VII.AV.OP-PROJ Cell-I markers = {len(residual_bad)} (expect 0)")
    for r in residual_bad:
        print(f"  RESIDUAL: {r}...")
    print(f"VERIFY: generic 'Cell I × substrate-distance-1' boilerplate INTACT = {boilerplate_intact} (expect True)")

    if residual_bad or not boilerplate_intact:
        print("REMEDIATION VERIFY FAILED.")
        return 2

    print("REMEDIATION OK: all §VII.AV.OP-PROJ markers Cell I -> Cell II; generic boilerplate intact.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
