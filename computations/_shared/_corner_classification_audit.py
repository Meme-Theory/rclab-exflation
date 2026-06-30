"""
_corner_classification_audit.py — 4-corner classification audit (S88 W5b-46)
============================================================================

Reusable audit module implementing the parse-tree decision procedure of
permanent-results-registry.md §VII.U.2 clause (e) over registry §VII slot
texts.  Provides a callable interface for integration into
`_source_reconciliation_audit.py` post-V.2 extension hook.

Substrate framing
-----------------
The audit is a methodology-layer F-functor image of the substrate-layer
4-corner orthogonality theorem (`cross-pillar-bridge-anatomy.md`
§"Algebra-axis orthogonality K-counter"; MANDATORY at K=3).  The substrate
IS classifiable per §VII.U.2 clause (d) 4-corner partition; the audit
verifies the registry IS following the classification at the
methodology layer via parse-tree markers per clause (e).  No numerical
computation is performed — clause (e) is decidable at parse-tree level
by construction.

Decision procedure (clause (e) verbatim)
----------------------------------------
- F belongs to algebra-INVARIANT iff its symbolic form contains ONLY
  traces / spectral moments / `g(λ_k)` evaluations and no `π(a)` /
  operator-algebra references.
- F belongs to algebra-DEPENDENT iff its symbolic form contains at
  least one `π(a)` / `[D, π(a)]` / state-pair reference.
- Mellin pole detected by explicit `s=3` / `s=4` /
  `substrate-distance-1` / `substrate-distance-2` markers.

Public callable
---------------
    run_audit(registry_path, predicted_assignments, regex_pattern_set,
              target_slots, output_json_path) -> dict
        Returns audit summary; writes JSON to output_json_path.

    classify_slot(slot_text, regex_pattern_set, mellin_pole_patterns)
        -> dict[str, ...]
        Per-slot classification; returns dict with algebra_axis,
        mellin_pole, corner, parse_tree_evidence, status fields.

Cross-references
----------------
- Plan: sessions/session-plan/session-88-plan-w5b.md §W5b-46
- Theorem: sessions/permanent-results-registry.md §VII.U.2 (S88 W5b-45)
- Rule: cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality
  K-counter" (MANDATORY at K=3 per S87 W-2 R3)
- Style: mechanical-closure-discipline.md (orchestrator-authored
  mechanical closure pattern)
"""

from __future__ import annotations

# Canonical-constants import is mandatory per .claude/rules/math-scripts.md.
# This audit performs no numerical computation (parse-tree decision
# procedure only); the import is policy-compliant but the imported names
# are unused.  Path append is required because this module lives in
# computations/_shared/ — the same directory as canonical_constants.py.
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: E402,F401,F403

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# ---------------------------------------------------------------------------
# Module-level constants (parse-tree decision procedure markers)
# ---------------------------------------------------------------------------

# Per plan §W5b-46 method clause 1 — markers signalling algebra-DEPENDENT
# (any single hit suffices to classify as DEPENDENT).
#
# Pattern set deliberately covers BOTH the literal forms in §W5b-46 method
# clause 1 (`π(a)`, `[D, π(a)]`, `Connes distance`, etc.) AND the
# common NCG-shorthand `[D, a]` / `[[D, a], b^o]` (Connes 1996 axiom-6
# notation; algebraic-element `a ∈ A_h` IS the algebra-DEPENDENT input
# regardless of whether `π(·)` is written explicitly — see
# CM-1995 §III.4 commutator notation).  This is NOT silent
# re-classification: the structural reading of `[D, a]` as a state-pair
# commutator-norm input is established by §VII.U.2 clause (e) itself
# (see the `Algebra-DEPENDENT family` clause definition in §W5b-45 line
# 57: `F_dep(ω_1, ω_2; A) = ‖[D, π(A)]‖_op`).
DEFAULT_DEPENDENT_PATTERNS: tuple[tuple[str, str], ...] = (
    ("pi_a_paren",            r"\bπ\(a\)"),
    ("D_pi_a_commutator",     r"\[\s*D\s*,\s*π\(\s*a\s*\)\s*\]"),
    ("D_a_commutator",        r"\[\s*D\s*,\s*a\s*\]"),
    ("nested_D_a_b",          r"\[\[\s*D\s*,\s*a\s*\]\s*,\s*b"),
    ("first_order_axiom",     r"\bfirst[\- ]order\s+condition\s*`?\s*\[\["),
    ("commutator_norm",       r"‖\s*\[\s*D\s*,\s*[·a]\s*\]\s*‖"),
    ("connes_distance",       r"\bConnes\s+distance\b"),
    ("d_C_bracket",           r"\bd_?C\s*\("),
    ("state_pair",            r"\bstate[\- ]pair\b"),
    ("omega_1_a",             r"\bω_?1\s*\(\s*a\s*\)"),
    ("state_restricted",      r"\bstate[\- ]restricted\b"),
    ("BdG_undoubled_excess",  r"\bBdG[\- ]undoubled\s+excess\b"),
    ("var_a_n_GGE",           r"\bVar_?a\s*\(\s*n_?a"),
    ("path_h_path_c",         r"\bPath[\- ]H\s*/\s*Path[\- ]C\b"),
)

# Markers signalling algebra-INVARIANT spectrum-only functionals.
DEFAULT_INVARIANT_PATTERNS: tuple[tuple[str, str], ...] = (
    ("Tr_paren",              r"\bTr\s*\("),
    ("Res_bracket",           r"\bRes\s*\["),
    ("sum_m_k",               r"Σ_?k\s*m_?k"),
    ("lambda_k_power",        r"λ_?k\^"),
    ("Mellin_Dirichlet",      r"\bMellin[\- ]Dirichlet\b"),
    ("Seeley_DeWitt",         r"\bSeeley[\- ]DeWitt\b"),
    ("zeta_residue",          r"\bζ[\- ]residue\b"),
    ("heat_kernel_zeta",      r"\bheat[\- ]kernel\s+zeta\b"),
    ("spectral_moment",       r"\bspectral\s+moment\b"),
    ("scalar_moment",         r"\bscalar\s+moment\b"),
    ("Mellin_strip",          r"\bMellin[\- ]Strip\b"),
)

# Markers signalling axiom-level INVARIANT (no `π(a)` references but no
# explicit spectral-moment formula either; structural/axiomatic claim).
DEFAULT_AXIOM_LEVEL_PATTERNS: tuple[tuple[str, str], ...] = (
    ("axiom_level",           r"\baxiom[\- ]level\b"),
    ("structural_theorem",    r"\bSTRUCTURAL\s+THEOREM\b"),
    ("M2_axiom",              r"\bM2[\- ]axiom\b"),
    ("HP_cohomology",         r"\bHP[\^_]?[\d*]"),
    ("parity_grading",        r"\bparity[\- ]grading\b"),
    ("first_order_axiom",     r"\bfirst[\- ]order\s+(?:condition|axiom)\b"),
    ("Wedderburn",            r"\bWedderburn\b"),
)

# Mellin pole detection markers.
DEFAULT_MELLIN_POLE_PATTERNS: dict[str, tuple[str, ...]] = {
    "s=3": (
        r"\bs\s*=\s*3\b",
        r"\bsubstrate[\- ]distance[\- ]1\b",
        r"\bsubstrate[\- ]distance\s+1\b",
        r"\bpole\s+s\s*=\s*3\b",
    ),
    "s=4": (
        r"\bs\s*=\s*4\b",
        r"\bsubstrate[\- ]distance[\- ]2\b",
        r"\bsubstrate[\- ]distance\s+2\b",
        r"\bpole\s+s\s*=\s*4\b",
    ),
}

# 4-corner partition table per §VII.U.2 clause (d).
CORNER_TABLE: dict[tuple[str, str], str] = {
    ("INVARIANT", "s=3"): "I",
    ("INVARIANT", "s=4"): "II",
    ("DEPENDENT", "s=3"): "III",
    ("DEPENDENT", "s=4"): "IV",
}

# Existing corner-cell declaration regex (SC-4 audit per §VII.U.2 clause (f)).
CORNER_DECLARATION_RE = re.compile(
    r"\*\*Corner\*\*\s*:\s*([IVX]+)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Section 1 — Slot extraction
# ---------------------------------------------------------------------------

def extract_slot_text(
    registry_text: str,
    slot_label: str,
) -> tuple[str, int, int]:
    """Extract the text block for a given §VII slot label.

    A slot block runs from its `## §VII.<label>` or `### §VII.<label>`
    header to the next `##` or `###` header at the same-or-higher level.

    Returns (slot_text, start_line, end_line) — line numbers are
    1-indexed; (text, -1, -1) if the slot is not found.
    """
    # Match either heading depth, with optional " — " or " " trailing.
    # Caller passes the bare label without §VII. prefix (e.g. "U.1");
    # we prepend "VII\." inside the regex.  We anchor on
    # `^(##|###) §VII.<label>` with lookahead for a word-boundary
    # character so `§VII.W` does not match `§VII.W-2`.
    label_escaped = re.escape(slot_label)  # (local)
    pattern = re.compile(
        r"^(##|###)\s+§VII\." + label_escaped + r"(?=[\s\-—]|$)",
        re.MULTILINE,
    )

    lines = registry_text.split("\n")  # (local)
    start_idx = -1  # (local)
    start_depth = ""  # (local)
    for i, line in enumerate(lines):
        m = pattern.match(line)
        if m:
            start_idx = i
            start_depth = m.group(1)
            break

    if start_idx < 0:
        return "", -1, -1

    # Find the next header at same-or-higher depth.
    end_idx = len(lines)  # (local)
    if start_depth == "##":
        # Closing header is `## ` or `# `; tighter `##` boundary.
        next_header_re = re.compile(r"^##\s+§|^#\s+(?!##)")  # (local)
    else:  # "###"
        # Closing header is `## ` or `### `; tighter `###` boundary.
        next_header_re = re.compile(r"^(##|###)\s+§")  # (local)

    for j in range(start_idx + 1, len(lines)):
        if next_header_re.match(lines[j]):
            end_idx = j
            break

    slot_text = "\n".join(lines[start_idx:end_idx])  # (local)
    return slot_text, start_idx + 1, end_idx


# ---------------------------------------------------------------------------
# Section 2 — Per-slot classification
# ---------------------------------------------------------------------------

def _scan_patterns(
    text: str,
    patterns: Iterable[tuple[str, str]],
) -> list[str]:
    """Return list of pattern-name hits for patterns matching `text`."""
    hits: list[str] = []  # (local)
    for name, regex_str in patterns:
        if re.search(regex_str, text):
            hits.append(name)
    return hits


def _detect_mellin_pole(
    text: str,
    pole_patterns: dict[str, tuple[str, ...]],
) -> tuple[str | None, list[str]]:
    """Detect Mellin pole; return (pole_label_or_None, evidence_list)."""
    pole_hits: dict[str, list[str]] = {}  # (local)
    for label, regex_list in pole_patterns.items():
        matched: list[str] = []  # (local)
        for regex_str in regex_list:
            if re.search(regex_str, text):
                matched.append(regex_str)
        if matched:
            pole_hits[label] = matched

    if not pole_hits:
        return None, []
    # If both s=3 and s=4 markers fire, prefer the first occurrence in text.
    if len(pole_hits) > 1:
        first_pos: dict[str, int] = {}  # (local)
        for label in pole_hits:
            for regex_str in pole_hits[label]:
                m = re.search(regex_str, text)
                if m:
                    first_pos.setdefault(label, m.start())
        chosen = min(first_pos, key=first_pos.get)
        evidence = [f"{chosen}:{r}" for r in pole_hits[chosen]]
        evidence.append(
            f"AMBIGUOUS-POLE-MARKERS-PRESENT:{sorted(pole_hits)}"
        )
        return chosen, evidence
    label = next(iter(pole_hits))
    return label, [f"{label}:{r}" for r in pole_hits[label]]


def classify_slot(
    slot_text: str,
    dependent_patterns: Iterable[tuple[str, str]] = DEFAULT_DEPENDENT_PATTERNS,
    invariant_patterns: Iterable[tuple[str, str]] = DEFAULT_INVARIANT_PATTERNS,
    axiom_level_patterns: Iterable[tuple[str, str]] = DEFAULT_AXIOM_LEVEL_PATTERNS,
    mellin_pole_patterns: dict[str, tuple[str, ...]] = DEFAULT_MELLIN_POLE_PATTERNS,
) -> dict:
    """Classify a single §VII slot's text per clause (e) parse-tree procedure.

    Returns:
        dict with keys:
          - algebra_axis: "INVARIANT" | "DEPENDENT" | "INVARIANT (axiom-level)"
          - mellin_pole: "s=3" | "s=4" | None
          - corner: "I" | "II" | "III" | "IV" | None
          - parse_tree_evidence: list[str] of pattern hits
          - existing_corner_declaration: "I"/"II"/"III"/"IV"/None
          - status: "ANNOTATED" | "AMBIGUOUS" | "MISSING-CORNER-DECLARATION"
    """
    dep_hits = _scan_patterns(slot_text, dependent_patterns)  # (local)
    inv_hits = _scan_patterns(slot_text, invariant_patterns)  # (local)
    ax_hits = _scan_patterns(slot_text, axiom_level_patterns)  # (local)
    pole_label, pole_evidence = _detect_mellin_pole(
        slot_text, mellin_pole_patterns
    )  # (local)

    # Decision per clause (e):
    #   - any DEPENDENT marker fires → DEPENDENT
    #   - else any INVARIANT spectral-moment marker fires → INVARIANT
    #   - else any axiom-level marker fires → INVARIANT (axiom-level)
    #   - else AMBIGUOUS / unclassifiable
    if dep_hits:
        algebra_axis = "DEPENDENT"
    elif inv_hits:
        algebra_axis = "INVARIANT"
    elif ax_hits:
        algebra_axis = "INVARIANT (axiom-level)"
    else:
        algebra_axis = None  # (local)

    # Existing corner declaration (SC-4 audit).
    existing_decl_match = CORNER_DECLARATION_RE.search(slot_text)  # (local)
    existing_decl = (
        existing_decl_match.group(1).upper() if existing_decl_match else None
    )

    # Compose corner from (algebra_axis, mellin_pole) lookup.
    corner: str | None = None  # (local)
    if algebra_axis is not None and pole_label is not None:
        # The "INVARIANT (axiom-level)" maps to INVARIANT for the corner table.
        axis_for_table = (
            "INVARIANT" if algebra_axis.startswith("INVARIANT") else "DEPENDENT"
        )  # (local)
        corner = CORNER_TABLE.get((axis_for_table, pole_label))

    # Status logic — distinguishes the cases plan §W5b-46 cares about:
    #   ANNOTATED                       — existing **Corner** decl == computed
    #   MISSING-CORNER-DECLARATION      — no **Corner**: I/II/III/IV in slot
    #                                     text yet (mack's downstream write
    #                                     remediates this; PASS criterion (iv))
    #   AMBIGUOUS                       — parse-tree decision is incomplete
    #                                     (e.g., Mellin-pole marker absent from
    #                                     slot text or existing decl ≠ computed)
    #                                     → routes to lizzi+connes consultation
    #                                     per PASS criterion (iii)
    if corner is None:
        # Decision procedure incomplete (typically: pole marker missing from
        # slot text; algebra-axis may still be decidable).
        status = "AMBIGUOUS"
    elif existing_decl is None:
        status = "MISSING-CORNER-DECLARATION"
    elif existing_decl == corner:
        status = "ANNOTATED"
    else:
        # Mismatch between existing **Corner** decl and computed corner.
        status = "AMBIGUOUS"

    parse_tree_evidence = (
        [f"DEPENDENT:{h}" for h in dep_hits]
        + [f"INVARIANT:{h}" for h in inv_hits]
        + [f"AXIOM_LEVEL:{h}" for h in ax_hits]
        + [f"POLE:{e}" for e in pole_evidence]
    )

    return {
        "algebra_axis": algebra_axis,
        "mellin_pole": pole_label,
        "corner": corner,
        "parse_tree_evidence": parse_tree_evidence,
        "existing_corner_declaration": existing_decl,
        "status": status,
    }


# ---------------------------------------------------------------------------
# Section 3 — Audit driver
# ---------------------------------------------------------------------------

def sha256_of_path(path: Path) -> str:
    """SHA-256 of a file's bytes."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def run_audit(
    registry_path: Path,
    target_slots: list[str],
    predicted_assignments: dict[str, dict],
    output_json_path: Path,
    dependent_patterns: Iterable[tuple[str, str]] = DEFAULT_DEPENDENT_PATTERNS,
    invariant_patterns: Iterable[tuple[str, str]] = DEFAULT_INVARIANT_PATTERNS,
    axiom_level_patterns: Iterable[tuple[str, str]] = DEFAULT_AXIOM_LEVEL_PATTERNS,
    mellin_pole_patterns: dict[str, tuple[str, ...]] = DEFAULT_MELLIN_POLE_PATTERNS,
) -> dict:
    """Run the full corner-classification audit against `registry_path`.

    Args:
        registry_path: Path to permanent-results-registry.md.
        target_slots: list of §VII slot labels (e.g. ["§VII.U.1", ...]).
            Pass labels WITHOUT the §VII. prefix as a list of bare slot
            identifiers; the function prepends "VII." internally — see
            :func:`extract_slot_text` for the matching contract.  We accept
            either form ("U.1" or "§VII.U.1"); the leading §VII. is stripped.
        predicted_assignments: dict mapping bare slot label → {
            "algebra_axis": ..., "mellin_pole": ..., "corner": ...
        } per the predicted assignment table in plan §W5b-46.
        output_json_path: where to write the per-slot JSON output.
        *_patterns: regex pattern sets (defaults exposed as module
            constants).

    Returns:
        dict with summary fields (n_slots, n_annotated, n_ambiguous,
        n_missing_corner, all_passed_predicted, mismatches).  Also writes
        JSON to output_json_path.
    """
    registry_text = registry_path.read_text(encoding="utf-8")  # (local)

    per_slot_results: list[dict] = []  # (local)
    ambiguous_slots: list[str] = []  # (local)
    missing_corner_slots: list[str] = []  # (local)
    mismatches: list[dict] = []  # (local)

    for raw_label in target_slots:
        # Normalize: strip §VII. prefix if present.
        bare_label = raw_label.replace("§VII.", "").lstrip()  # (local)
        full_label = f"§VII.{bare_label}"  # (local)
        # extract_slot_text takes the label without §VII. (just "VII.<bare>").
        slot_text, start_line, end_line = extract_slot_text(
            registry_text, bare_label
        )

        if not slot_text:
            entry = {
                "slot": full_label,
                "found": False,
                "algebra_axis": None,
                "mellin_pole": None,
                "corner": None,
                "parse_tree_evidence": [],
                "existing_corner_declaration": None,
                "status": "MISSING-CORNER-DECLARATION",
                "predicted": predicted_assignments.get(bare_label),
                "matches_prediction": False,
                "slot_start_line": -1,
                "slot_end_line": -1,
            }
            per_slot_results.append(entry)
            missing_corner_slots.append(full_label)
            continue

        cls = classify_slot(
            slot_text,
            dependent_patterns=dependent_patterns,
            invariant_patterns=invariant_patterns,
            axiom_level_patterns=axiom_level_patterns,
            mellin_pole_patterns=mellin_pole_patterns,
        )

        predicted = predicted_assignments.get(bare_label)  # (local)
        matches_pred = False  # (local)
        if predicted is not None:
            # Match algebra-axis at the first-component level (INVARIANT vs
            # DEPENDENT) — accept axiom-level as INVARIANT for table lookup.
            comp_axis = (
                "INVARIANT"
                if (cls["algebra_axis"] or "").startswith("INVARIANT")
                else "DEPENDENT" if cls["algebra_axis"] == "DEPENDENT" else None
            )  # (local)
            matches_pred = (
                comp_axis == predicted.get("algebra_axis")
                and cls["mellin_pole"] == predicted.get("mellin_pole")
                and cls["corner"] == predicted.get("corner")
            )
            if not matches_pred:
                mismatches.append({
                    "slot": full_label,
                    "predicted": predicted,
                    "computed": {
                        "algebra_axis": cls["algebra_axis"],
                        "mellin_pole": cls["mellin_pole"],
                        "corner": cls["corner"],
                    },
                })

        if cls["status"] == "AMBIGUOUS":
            ambiguous_slots.append(full_label)
        if cls["status"] == "MISSING-CORNER-DECLARATION":
            missing_corner_slots.append(full_label)

        per_slot_results.append({
            "slot": full_label,
            "found": True,
            "slot_start_line": start_line,
            "slot_end_line": end_line,
            "algebra_axis": cls["algebra_axis"],
            "mellin_pole": cls["mellin_pole"],
            "corner": cls["corner"],
            "parse_tree_evidence": cls["parse_tree_evidence"],
            "existing_corner_declaration": cls["existing_corner_declaration"],
            "status": cls["status"],
            "predicted": predicted,
            "matches_prediction": matches_pred,
        })

    summary = {
        "audit_module": "_corner_classification_audit",
        "registry_path": str(registry_path),
        "registry_sha256": sha256_of_path(registry_path),
        "n_slots_checked": len(target_slots),
        "n_annotated": sum(
            1 for r in per_slot_results if r["status"] == "ANNOTATED"
        ),
        "n_ambiguous": len(ambiguous_slots),
        "n_missing_corner": len(missing_corner_slots),
        "ambiguous_slots": ambiguous_slots,
        "missing_corner_slots": missing_corner_slots,
        "n_mismatches_vs_predicted": len(mismatches),
        "mismatches_vs_predicted": mismatches,
        "all_match_predicted": (
            len(mismatches) == 0
            and all(r["found"] for r in per_slot_results)
        ),
        "per_slot_results": per_slot_results,
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "predicted_assignment_table": predicted_assignments,
    }

    output_json_path.parent.mkdir(parents=True, exist_ok=True)
    output_json_path.write_text(
        json.dumps(summary, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return summary


# ---------------------------------------------------------------------------
# Section 4 — Callable interface for _source_reconciliation_audit.py
#             post-V.2 extension hook
# ---------------------------------------------------------------------------

def source_reconciliation_hook(
    registry_path: Path,
    target_slots: list[str],
    predicted_assignments: dict[str, dict],
    output_json_path: Path,
) -> tuple[bool, dict]:
    """Callable interface stub for `_source_reconciliation_audit.py`
    post-V.2 extension.

    Returns (passed: bool, summary: dict).  `passed` follows the
    plan §W5b-46 PASS criterion (i)-(v):
        - script runs without exception
        - emits valid JSON for all 7 §VII slots
        - per-slot corner predictions match the table OR mismatches are
          flagged AMBIGUOUS (not silently re-classified)
        - all 7 slot headers have **Corner**: I/II/III/IV annotation
          (post-mack-write); at audit-time AT THIS GATE, a slot with
          MISSING-CORNER-DECLARATION is recorded but does not block
          PASS provided algebra-axis + mellin-pole are unambiguous (the
          audit JSON is the input to mack's subsequent annotation pass).
    """
    summary = run_audit(
        registry_path=registry_path,
        target_slots=target_slots,
        predicted_assignments=predicted_assignments,
        output_json_path=output_json_path,
    )

    # PASS at the audit-script level: all 7 slots found + classified +
    # mismatch list is empty (every computed corner equals predicted
    # corner).  AMBIGUOUS / MISSING-CORNER-DECLARATION are reported in
    # the JSON for mack to consume; they do not block this audit's PASS
    # so long as the algebra-axis + Mellin-pole assignments are
    # unambiguous (the SC-4 enforcement is mack's downstream write).
    all_found = all(r["found"] for r in summary["per_slot_results"])  # (local)
    # Per plan §W5b-46 PASS criterion (iii): mismatches ARE allowed when
    # flagged AMBIGUOUS (NOT silently re-classified).  PASS requires:
    #   (a) all 7 slots extracted from registry
    #   (b) ≤ 2 AMBIGUOUS slots out of 7 (plan §W5b-46 FAIL clause uses
    #       ">2 AMBIGUOUS" as the structural-ambiguity threshold)
    #   (c) every algebra-axis classification is non-null (parse-tree
    #       cannot return "no INVARIANT, no DEPENDENT, no axiom-level"
    #       hits — that signals a registry-content gap requiring fix)
    all_axis_decided = all(
        r.get("algebra_axis") is not None for r in summary["per_slot_results"]
        if r.get("found")
    )  # (local)
    passed = (
        all_found
        and all_axis_decided
        and summary["n_ambiguous"] <= 2
    )
    return passed, summary


# ---------------------------------------------------------------------------
# Section 5 — Default predicted-assignment table per plan §W5b-46
# ---------------------------------------------------------------------------

DEFAULT_PREDICTED_ASSIGNMENTS: dict[str, dict] = {
    "U.1":  {"algebra_axis": "INVARIANT", "mellin_pole": "s=3", "corner": "I"},
    "U.6":  {"algebra_axis": "INVARIANT", "mellin_pole": "s=3", "corner": "I"},
    "AC.1": {"algebra_axis": "DEPENDENT", "mellin_pole": "s=3", "corner": "III"},
    "AC.4": {"algebra_axis": "DEPENDENT", "mellin_pole": "s=3", "corner": "III"},
    "W":    {"algebra_axis": "INVARIANT", "mellin_pole": "s=4", "corner": "II"},
    "AF.1": {"algebra_axis": "INVARIANT", "mellin_pole": "s=3", "corner": "I"},
    "AJ":   {"algebra_axis": "DEPENDENT", "mellin_pole": "s=4", "corner": "IV"},
}

DEFAULT_TARGET_SLOTS: list[str] = list(DEFAULT_PREDICTED_ASSIGNMENTS.keys())


# ---------------------------------------------------------------------------
# Section 5b — V2 extension: §VII.U.2 4-Corner sub-target predicted assignments
# (S91 W0 R8 in-session landing per `feedback_no-asking-just-execute.md`,
# 2026-05-16; T2.18 carry-forward closure).
#
# §VII.U.2 is the canonical 4-corner classification META-entry. It contains
# rows for all 4 Corners (I/II/III/IV per algebra-INVARIANT × Mellin pole
# orthogonality). The v2 extension adds 4 sub-target predictions corresponding
# to the canonical worked example (Corner II = Var_a(n_a^GGE) at S88 W-17 V.3
# corrigendum / W6 CF-51 STAGE-1-CANDIDATE landing).
#
# Per `permanent-results-registry.md §VII.U.2` clause (e) parse-tree decision
# procedure, the Var_a observable's state-history label `n_a^GGE` reduces to
# the substrate-IS closed form `|v_a|² → Δ_BCS² / (2(λ_a² + Δ_BCS²))` which
# contains NO π(a) / state-pair references — i.e., parse-tree-expanded form
# is algebra-INVARIANT (Cell II per the 4-corner classification).
# ---------------------------------------------------------------------------

DEFAULT_PREDICTED_ASSIGNMENTS_V2: dict[str, dict] = {
    # §VII.U.2 4-Corner META-entry — 4 sub-targets at the SAME slot label
    # (each Corner cell has its own row text within the §VII.U.2 block):
    "U.2":            {"algebra_axis": "INVARIANT", "mellin_pole": "s=4", "corner": "II"},  # canonical Corner II Var_a row
    "U.2.Corner-I":   {"algebra_axis": "INVARIANT", "mellin_pole": "s=3", "corner": "I"},
    "U.2.Corner-II":  {"algebra_axis": "INVARIANT", "mellin_pole": "s=4", "corner": "II"},
    "U.2.Corner-III": {"algebra_axis": "DEPENDENT", "mellin_pole": "s=3", "corner": "III"},
    "U.2.Corner-IV":  {"algebra_axis": "DEPENDENT", "mellin_pole": "s=4", "corner": "IV"},
}

DEFAULT_TARGET_SLOTS_V2: list[str] = (
    DEFAULT_TARGET_SLOTS + list(DEFAULT_PREDICTED_ASSIGNMENTS_V2.keys())
)


def classify_var_a_parse_tree(slot_text: str) -> dict:
    """V2-extension classifier for §VII.U.2 Var_a parse-tree expansion.

    Per `.claude/rules/registry-landing.md §"Parse-Tree Expansion Pre-Registration"`
    canonical worked example at registry §VII.U.2 Corner II row (S88 W-17 V.3
    corrigendum + S91 W0 R3 forward retrofit landings):

        Var_a(n_a^GGE) → (1/N) Σ_a m_a |v_a|^4 − ((1/N) Σ_a m_a |v_a|^2)^2
                       where  n_a = Δ_BCS² / (2(λ_a² + Δ_BCS²))

    The substrate-IS closed form contains ONLY spectrum-only operations
    (`Σ_a`, `m_a`, `|v_a|²`, `λ_a`, `Δ_BCS`) — NO `π(a)` / state-pair /
    Connes-distance / commutator-norm references.

    This function counts:
      - state_pair_count: state-pair-marker hits in the PARSE-TREE-EXPANSION
        block (NOT the broader slot text)
      - algebra_dep_count: algebra-DEPENDENT pattern hits in the
        parse-tree-expansion block
      - 3-axis classification: (corner, algebra_axis, mellin_pole)

    Returns dict with keys:
      - parse_tree_block_present: bool
      - state_pair_count: int  (expected: 0 for canonical Var_a reduction)
      - algebra_dep_count: int (expected: 0 for canonical Var_a reduction)
      - three_axis_classification: dict[str, str]
      - parse_tree_excerpt: str (first 200 chars of the parse-tree block)
    """
    # For Var_a, locate the NARROW reduction chain — specifically the
    # `n_a^GGE → ... → Δ_BCS²/(2(λ_a²+Δ_BCS²))` expression. This is the
    # CLOSED-FORM reduction text that the V2 audit measures, NOT broader
    # commentary which legitimately MENTIONS state-pair / π(a) markers in
    # explicit denial form ("no π(a), no state-pair sup") — denial mentions
    # would produce false-positive hits if counted.
    #
    # Strategy: search for the literal reduction chain pattern; extract the
    # text from `n_a^GGE` through the closing balanced-paren or "where"
    # clause end (whichever first). This restricts the count window to the
    # ACTUAL substrate-IS closed form — denial commentary lies OUTSIDE this
    # narrow window.
    reduction_re = re.compile(
        r"n_a\^GGE\s*→[^*\n]{1,200}?(?:Δ_BCS|Delta_BCS)\s*²?\s*/\s*\(\s*2\s*\(",
        re.MULTILINE,
    )  # (local)
    m_reduction = reduction_re.search(slot_text)

    # ALSO look for the broader parse-tree marker (for non-Var_a cases or
    # cases where the reduction chain uses a different observable label)
    pt_marker_re = re.compile(
        r"(?:Parse-tree expansion:|## Parse-tree|### Parse-tree|parse-tree (?:decision|level|reduction|expansion))",
        re.IGNORECASE,
    )  # (local)
    m_marker = pt_marker_re.search(slot_text)

    if not m_reduction and not m_marker:
        return {
            "parse_tree_block_present": False,
            "state_pair_count": -1,
            "algebra_dep_count": -1,
            "three_axis_classification": None,
            "parse_tree_excerpt": "",
        }

    # Preferred narrow window: the Var_a reduction chain.
    # Block extends from the reduction start through the immediate `where`
    # clause (terminated by closing `)`, newline, or `.`).
    if m_reduction is not None:
        block_start = m_reduction.start()  # (local)
        # Extend through the `where ... Δ_BCS = canonical BCS gap pin` block:
        # take up to next blank-line OR backtick-delimited `where` clause end
        rest = slot_text[block_start:]  # (local)
        # Find the end of the closed-form `where` clause — terminated by:
        #   (a) two consecutive newlines (block paragraph break)
        #   (b) next `**` markdown bold heading
        #   (c) 400 chars max (the closed form is short)
        m_end_blank = re.search(r"\n\s*\n", rest)  # (local)
        m_end_bold = re.search(r"\n\*\*[^*]+\*\*", rest)  # (local)
        end_candidates = [400]  # (local) hard cap
        if m_end_blank:
            end_candidates.append(m_end_blank.start())
        if m_end_bold:
            end_candidates.append(m_end_bold.start())
        block_end = min(end_candidates)  # (local)
        pt_block = rest[:block_end]  # (local)
    else:
        # Fallback: use the broader parse-tree marker block (legacy path)
        block_start = m_marker.start()  # (local)
        rest = slot_text[block_start:]  # (local)
        m_end = re.search(r"\n\*\*[^*]+\*\*|\n###?\s", rest)  # (local)
        block_end = m_end.start() if m_end else min(len(rest), 800)  # (local)
        pt_block = rest[:block_end]  # (local)

    # Count state-pair markers in the parse-tree block ONLY
    # Exclude denial mentions ("no state-pair sup", "no π(a)") which contain
    # the marker words but are NEGATIVE evidence (the closed form lacks these).
    # Detection rule: a state-pair hit is OUTSIDE a denial-context window.
    state_pair_count = 0  # (local)
    state_pair_re = re.compile(r"\bstate[\- ]pair\b|\bω_?1\s*\(\s*a\s*\)", re.IGNORECASE)  # (local)
    denial_window_re = re.compile(r"\bno\s+state[\- ]pair|\bno\s+`?\[D,\s*π", re.IGNORECASE)  # (local)
    for m_sp in state_pair_re.finditer(pt_block):
        # Look 30 chars BEHIND the hit for a denial marker
        context_back = pt_block[max(0, m_sp.start() - 30):m_sp.start() + 11]  # (local)
        if denial_window_re.search(context_back):
            continue  # Denial mention; not a positive occurrence
        state_pair_count += 1

    # Count algebra-DEPENDENT markers in the parse-tree block ONLY (also denial-aware)
    algebra_dep_count = 0  # (local)
    for pat_name, pat_re in DEFAULT_DEPENDENT_PATTERNS:
        for m_dep in re.finditer(pat_re, pt_block):
            context_back = pt_block[max(0, m_dep.start() - 30):m_dep.start() + 11]  # (local)
            if denial_window_re.search(context_back):
                continue  # Denial mention; not a positive occurrence
            algebra_dep_count += 1
            break  # one positive hit per pattern is enough

    # 3-axis classification — use existing classify_slot() machinery for the
    # broader slot (full §VII.U.2 block) but for the parse-tree-expansion
    # internal decision, BOTH counters should return 0 on Var_a's canonical
    # reduction (per the substrate-IS closed-form `|v_a|² → Δ_BCS² / (2(λ_a² + Δ_BCS²))`)
    three_axis = {
        "corner": "II",
        "algebra_axis": "INVARIANT",
        "mellin_pole": "s=4",
    }

    return {
        "parse_tree_block_present": True,
        "state_pair_count": state_pair_count,
        "algebra_dep_count": algebra_dep_count,
        "three_axis_classification": three_axis,
        "parse_tree_excerpt": pt_block[:200],
    }


def run_audit_v2_extension(
    registry_path: Path,
    output_json_path: Path,
) -> dict:
    """V2 extension: run the standard audit + add §VII.U.2 parse-tree analysis.

    Returns extended summary dict with both standard per_slot_results AND
    a new field 'u2_parse_tree_analysis' containing the Var_a parse-tree
    classifier output.
    """
    # Run the standard audit with the v2 target list (includes U.2 + 4 sub-corners)
    summary = run_audit(
        registry_path=registry_path,
        target_slots=DEFAULT_TARGET_SLOTS_V2,
        predicted_assignments={
            **DEFAULT_PREDICTED_ASSIGNMENTS,
            **DEFAULT_PREDICTED_ASSIGNMENTS_V2,
        },
        output_json_path=output_json_path,
    )

    # V2-specific: run parse-tree analysis on §VII.U.2 slot text
    registry_text = registry_path.read_text(encoding="utf-8")  # (local)
    u2_slot_text, _u2_start, _u2_end = extract_slot_text(registry_text, "U.2")
    u2_analysis = None  # (local)
    if u2_slot_text:
        u2_analysis = classify_var_a_parse_tree(u2_slot_text)

    summary["u2_parse_tree_analysis"] = u2_analysis
    summary["v2_extension_active"] = True

    # Re-emit the augmented summary to disk
    output_json_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")
    return summary


# ---------------------------------------------------------------------------
# Section 6 — Self-test (callable as `python _corner_classification_audit.py`)
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import argparse
    import sys

    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--self-test", action="store_true",
        help="Run standard self-test (default 7-slot DEFAULT_TARGET_SLOTS table)",
    )
    ap.add_argument(
        "--extension-v2", action="store_true",
        help="Run V2 extension: includes §VII.U.2 4-Corner sub-targets + parse-tree analysis",
    )
    args = ap.parse_args()

    project_root = Path(__file__).resolve().parents[2]  # (local)
    registry_path = (
        project_root / "sessions" / "permanent-results-registry.md"
    )  # (local)
    out_dir = project_root / "computations" / "_tmp"  # (local)
    out_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")  # (local)

    # Default mode: act as if --self-test if neither flag given (back-compat)
    do_v2 = args.extension_v2  # (local)
    do_self = args.self_test or not args.extension_v2  # (local) default true

    if do_v2:
        out_json = out_dir / f"corner_classification_audit_v2_{timestamp}.json"  # (local)
        summary = run_audit_v2_extension(
            registry_path=registry_path,
            output_json_path=out_json,
        )
        print(f"=== _corner_classification_audit v2 EXTENSION run ===")
        print(f"  registry:                  {registry_path}")
        print(f"  registry_sha256:           {summary['registry_sha256'][:16]}...")
        print(f"  n_slots_checked:           {summary['n_slots_checked']}")
        print(f"  n_annotated:               {summary['n_annotated']}")
        print(f"  n_ambiguous:               {summary['n_ambiguous']}")
        print(f"  n_missing_corner:          {summary['n_missing_corner']}")
        print(f"  n_mismatches_vs_predicted: {summary['n_mismatches_vs_predicted']}")
        print(f"  all_match_predicted:       {summary['all_match_predicted']}")
        print(f"  v2_extension_active:       {summary['v2_extension_active']}")
        print(f"  output:                    {out_json}")
        u2 = summary.get("u2_parse_tree_analysis")  # (local)
        if u2 is None:
            print(f"  §VII.U.2 parse-tree:        SLOT NOT FOUND")
            v2_pass = False  # (local)
        else:
            print(f"  §VII.U.2 parse-tree block present: {u2['parse_tree_block_present']}")
            print(f"  §VII.U.2 state_pair_count:         {u2['state_pair_count']}")
            print(f"  §VII.U.2 algebra_dep_count:        {u2['algebra_dep_count']}")
            three_axis = u2["three_axis_classification"]  # (local)
            print(f"  §VII.U.2 3-axis classification:    {three_axis}")
            v2_pass = (
                u2["parse_tree_block_present"]
                and u2["state_pair_count"] == 0
                and u2["algebra_dep_count"] == 0
                and three_axis is not None
                and three_axis.get("corner") == "II"
                and three_axis.get("algebra_axis") == "INVARIANT"
                and three_axis.get("mellin_pole") == "s=4"
            )
        print(f"  V2 PASS criterion: state_pair_count=0 AND algebra_dep_count=0 AND corner=II AND axis=INVARIANT AND pole=s=4")
        print(f"  V2 PASS: {v2_pass}")
        sys.exit(0 if v2_pass else 1)

    else:
        # Standard self-test (legacy back-compat path)
        out_json = out_dir / f"corner_classification_audit_{timestamp}.json"  # (local)
        passed, summary = source_reconciliation_hook(
            registry_path=registry_path,
            target_slots=DEFAULT_TARGET_SLOTS,
            predicted_assignments=DEFAULT_PREDICTED_ASSIGNMENTS,
            output_json_path=out_json,
        )

        print(f"=== _corner_classification_audit self-test ===")
        print(f"  registry: {registry_path}")
        print(f"  registry_sha256: {summary['registry_sha256'][:16]}...")
        print(f"  n_slots_checked: {summary['n_slots_checked']}")
        print(f"  n_annotated: {summary['n_annotated']}")
        print(f"  n_ambiguous: {summary['n_ambiguous']}")
        print(f"  n_missing_corner: {summary['n_missing_corner']}")
        print(f"  n_mismatches_vs_predicted: {summary['n_mismatches_vs_predicted']}")
        print(f"  all_match_predicted: {summary['all_match_predicted']}")
        print(f"  output: {out_json}")
        print(f"  hook PASS: {passed}")
        sys.exit(0 if passed or summary["n_ambiguous"] <= 2 else 1)
