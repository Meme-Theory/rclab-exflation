#!/usr/bin/env python
"""
_vii_slot_allocation_audit.py
==============================

§VII slot-allocation audit (S86 W1a Option-B fix; promoted to permanent
retrospection check via .claude/hooks/TASK-UPDATE-RETROSPECTIVE.sh).

Detects plan-vs-table-vs-registry mismatches in the §VII slot-allocation
table at the top of `sessions/permanent-results-registry.md`. Fires on
every TaskUpdate-to-completed event so collisions are caught WHEN THEY
HAPPEN, not at session close.

Provenance: S86 W1a-2 surfaced a §VII.R/§VII.S slot collision between
W0b methodology entries and W1a content theorems. Root cause: no
centralized §VII slot-allocation arbiter; planners picked letters
independently. The slot-allocation table at the top of
`permanent-results-registry.md` plus this audit closes that gap.

Six-class taxonomy (S87 Class-F STALE-STATUS extension landed
2026-04-28 via gate S87-VII-SLOT-ALLOC-AUDIT-CLASS-F-EXT):
- Class A — REGISTERED-AND-MATCHED   (plan reservation matches table entry)
- Class B — UNREGISTERED-RESERVATION (plan reserves §VII.L; table has no entry)
- Class C — COLLISION-DOUBLE-RESERVATION (two plans reserve same §VII.L)
- Class D — ORPHANED-TABLE-ENTRY     (table allocates §VII.L; no plan reserves)
- Class E — REGISTRY-VS-TABLE-DRIFT  (registry has §VII.L block; table disagrees)
- Class F — STALE-STATUS             (table's first_landed disagrees with
                                      registry's actual landing state; INFO-tier
                                      drift, NOT a hard FAIL)

Class-F sub-forms:
  * STALE-STATUS         : table says OPEN but registry has §VII.L header.
  * STALE-STATUS-INVERSE : table cites a session/gate landing but registry
                           has NO §VII.L header.

CLI:
    python computations/_shared/_vii_slot_allocation_audit.py [--json] [--quiet]
        [--registry PATH] [--plan-glob GLOB] [--self-test]

Default: scans `sessions/session-plan/*.md` against the table at the top
of `sessions/permanent-results-registry.md`. Emits PASS/INFO/FAIL via the
S86+ canonical 4-tuple form. Exit 0 regardless of verdict (verdict is data,
not exit code; per .claude/rules/math-scripts.md).

PASS / INFO / FAIL (post Class-F extension):
    PASS iff all reservations are Class A AND no Class C/D/E defects
        (Class-F count is informational; does NOT downgrade PASS).
    INFO iff only Class B defects (table needs update; not blocking)
    FAIL iff any Class C/D/E defect (real collision or registry drift)

If Class-F count > 0 the verdict-line value field carries the diagnostic
suffix `class_f_drift=<count>`; the top-level verdict is unaffected.
"""
from __future__ import annotations

# OMP thread cap MUST come BEFORE any numpy import per
# .claude/rules/computation-environment.md (defensive even though this script
# does no linear algebra).
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import argparse
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

# canonical_constants import (compliance-mandated for all S34+ computation scripts)
sys.path.insert(0, str(Path(__file__).resolve().parent))
try:
    from canonical_constants import *  # noqa: F401,F403
except Exception:  # noqa: BLE001
    print("ERROR: canonical_constants.py import failed; computation compliance broken", file=sys.stderr)
    raise


# -----------------------------------------------------------------------------
# 6-class taxonomy (Class-F added S87 2026-04-28; A-E preserved verbatim)
# -----------------------------------------------------------------------------
CLASS_A = "A_REGISTERED_AND_MATCHED"        # (local)
CLASS_B = "B_UNREGISTERED_RESERVATION"      # (local)
CLASS_C = "C_COLLISION_DOUBLE_RESERVATION"  # (local)
CLASS_D = "D_ORPHANED_TABLE_ENTRY"          # (local)
CLASS_E = "E_REGISTRY_VS_TABLE_DRIFT"       # (local)
CLASS_F = "F_STALE_STATUS"                  # (local)
TAXONOMY_CLASSES = (CLASS_A, CLASS_B, CLASS_C, CLASS_D, CLASS_E, CLASS_F)  # (local)

# Patterns that mark a plan-file reservation of a §VII slot. Matching ANY of
# these inside a plan file = the plan is reserving the named slot. Conservative
# (false-positive-tolerant) — flagging is informational anyway.
RESERVATION_PATTERNS = (  # (local)
    r"\*\*Write target\*\*[^\n]*?§VII\.([A-Z][A-Za-z0-9.-]*)",
    r"vii_slot[\"']?\s*[:=]\s*[\"']?§VII\.([A-Z][A-Za-z0-9.-]*)",
    r"prerequisite_slot[\"']?\s*[:=]\s*[\"']?§VII\.([A-Z][A-Za-z0-9.-]*)",
    r"open\s+NEW\s+slot\s+§VII\.([A-Z][A-Za-z0-9.-]*)",
    r"land[a-z]*\s+(?:at|to|in)\s+§VII\.([A-Z][A-Za-z0-9.-]*)",
)

# Pattern for a registry §VII section header (level-2 or level-3 markdown).
REGISTRY_HEADER_PATTERN = re.compile(  # (local)
    r"^#{2,3}\s+§VII\.([A-Z][A-Za-z0-9.-]*)\b",
    re.MULTILINE,
)

# Pattern for the slot-allocation table row. Expected layout:
#   | §VII.L | CLASS | semantics | allocated_to | first_landed |
TABLE_ROW_PATTERN = re.compile(  # (local)
    r"^\|\s*§VII\.([A-Z][A-Za-z0-9.-]*)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|",
    re.MULTILINE,
)

# Marker that delimits the slot-allocation table within the registry. The
# table is identified by its preceding markdown header.
TABLE_HEADER_MARKER = "§VII Slot Allocation Table"  # (local)

# Lexical patterns that count as an "OPEN" first_landed status. Matched
# case-insensitive against the table's first_landed cell content.
OPEN_STATUS_TOKENS = ("open", "(open)", "—", "-", "(free)", "free", "(vacated)", "vacated", "n/a", "tbd", "pending")  # (local)


def sha256_of_file(path: Path) -> str:
    if not path.exists():
        return "MISSING"
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def closure_hash(input_pin_map: dict[str, Any]) -> str:
    """Closure SHA-256 over a canonical-ordered input-pin map (W9a-99 convention)."""
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def parse_slot_table(registry_text: str) -> dict[str, dict[str, str]]:
    """Extract the §VII slot-allocation table from registry markdown.

    Returns a dict mapping the slot suffix (e.g. "R", "M.3", "K-PROP") to
    {"class": ..., "semantics": ..., "allocated_to": ..., "first_landed": ...}.

    Returns an empty dict if the table is absent (Class E will fire on every
    registry entry in that case).
    """
    if TABLE_HEADER_MARKER not in registry_text:
        return {}
    # Restrict to the table region: from the marker header forward to the next
    # level-2 markdown header, exclusive.
    marker_idx = registry_text.find(TABLE_HEADER_MARKER)
    region = registry_text[marker_idx:]
    next_h2 = re.search(r"\n##\s+", region[len(TABLE_HEADER_MARKER):])
    if next_h2 is not None:
        region = region[: len(TABLE_HEADER_MARKER) + next_h2.start()]

    table: dict[str, dict[str, str]] = {}
    for m in TABLE_ROW_PATTERN.finditer(region):
        suffix = m.group(1).strip()
        # Skip the markdown table-header row (which has "Letter" / "Class" cells)
        if m.group(2).strip().lower() in ("class", ":------"):
            continue
        table[suffix] = {
            "class": m.group(2).strip(),
            "semantics": m.group(3).strip(),
            "allocated_to": m.group(4).strip(),
            "first_landed": m.group(5).strip(),
        }
    return table


def parse_registry_headers(registry_text: str) -> set[str]:
    """Extract §VII.{SUFFIX} section headers actually present in the registry."""
    return {m.group(1) for m in REGISTRY_HEADER_PATTERN.finditer(registry_text)}


def parse_registry_first_appearance(registry_text: str) -> dict[str, int]:
    """Map each §VII.{suffix} suffix to the line number of its FIRST header.

    Class-F STALE-STATUS extension (S87 2026-04-28). The table's `first_landed`
    field is compared against this map: if the table claims OPEN but the
    suffix appears here, the table is stale (a header has landed but the
    table was not updated). Conversely, if the table claims a landing but
    the suffix is ABSENT here, the table is stale-INVERSE (table cites a
    landing but the registry has no header for it).

    Line numbers are 1-based to match human-readable file annotations.
    """
    first_appearance: dict[str, int] = {}
    for line_idx, line in enumerate(registry_text.split("\n"), start=1):
        m = re.match(r"^#{2,3}\s+§VII\.([A-Z][A-Za-z0-9.-]*)\b", line)
        if m is not None:
            suffix = m.group(1).strip()
            # First appearance only — preserve the earliest header line.
            if suffix not in first_appearance:
                first_appearance[suffix] = line_idx
    return first_appearance


def is_open_status(first_landed: str) -> bool:
    """Return True iff the first_landed cell is one of the OPEN tokens (case-insensitive)."""
    s = first_landed.strip().lower()  # (local)
    if not s:
        return True
    for tok in OPEN_STATUS_TOKENS:
        # Exact match OR token appears as standalone word in cell content.
        if s == tok or f" {tok} " in f" {s} " or s.startswith(tok + " ") or s.endswith(" " + tok):
            return True
    return False


def parse_plan_reservations(plan_files: list[Path]) -> dict[str, list[str]]:
    """Scan plan files for §VII slot reservations.

    Returns a dict mapping slot suffix → list of plan-file basenames that
    reserve that slot. Multiple plans reserving the same suffix → Class C
    candidate.
    """
    reservations: dict[str, list[str]] = defaultdict(list)
    compiled_patterns = [re.compile(p) for p in RESERVATION_PATTERNS]
    for plan_path in plan_files:
        try:
            text = plan_path.read_text(encoding="utf-8", errors="replace")
        except Exception:  # noqa: BLE001
            continue
        suffixes_in_plan: set[str] = set()
        for pat in compiled_patterns:
            for m in pat.finditer(text):
                # Strip trailing periods (sentence-terminator artifacts) — without this,
                # plan text like "landed at §VII.AX." captures suffix="AX." which fires a
                # bogus B_UNREGISTERED_RESERVATION distinct from the valid "§VII.AX" entry.
                # S92 W4 Effected-In-Session audit-parser fix.
                suffixes_in_plan.add(m.group(1).strip().rstrip("."))
        for suffix in suffixes_in_plan:
            reservations[suffix].append(plan_path.name)
    return dict(reservations)


def classify(
    table: dict[str, dict[str, str]],
    reservations: dict[str, list[str]],
    registry_headers: set[str],
    registry_first_appearance: dict[str, int] | None = None,
) -> list[dict[str, Any]]:
    """Run the 6-class classification across all plan / table / registry pairs.

    Class-F (S87 extension) is detected by comparing the table's `first_landed`
    field against `registry_first_appearance`:
      * STALE-STATUS         : table says OPEN, registry has §VII.{suffix} header.
      * STALE-STATUS-INVERSE : table cites landing, registry has NO header.

    Class-F is INFORMATIONAL: it does NOT downgrade the top-level verdict
    (see evaluate_verdict). The pre-existing 5-class A/B/C/D/E logic is
    PRESERVED VERBATIM — Class-F detection runs as an independent pass over
    the table and does not modify the existing findings.
    """
    findings: list[dict[str, Any]] = []
    if registry_first_appearance is None:
        registry_first_appearance = {}

    # --- Plan-vs-table classes (A, B, C) — UNCHANGED from 5-class taxonomy ---
    # OP-PROJ-resolution exception (S92 W4 Effected-In-Session audit-rule
    # extension): if a bare §VII.X collision is detected and the registry
    # OR table contains §VII.X.OP-PROJ (or .STATE-PROJ), the collision is
    # structurally RESOLVED via the OP-PROJ Naming Hygiene K=3 MANDATORY
    # per `registry-landing.md`. Both plans intended the parent slot; the
    # actual landings are at distinctly-suffixed sub-slots.
    def _collision_resolved_by_op_proj(suffix: str) -> bool:
        for sfx in (f"{suffix}.OP-PROJ", f"{suffix}.STATE-PROJ"):
            if sfx in table or sfx in registry_headers:
                return True
        return False

    for suffix, plan_files in reservations.items():
        if len(plan_files) > 1:
            if _collision_resolved_by_op_proj(suffix):
                # Not emitted as C; the collision is resolved by suffix landing.
                continue
            findings.append({
                "class": CLASS_C,
                "slot": f"§VII.{suffix}",
                "detail": f"reserved by {len(plan_files)} plans: {plan_files}",
            })
            continue
        if suffix not in table:
            findings.append({
                "class": CLASS_B,
                "slot": f"§VII.{suffix}",
                "detail": f"plan {plan_files[0]} reserves but table has no entry",
            })
            continue
        # Class A — registered and matched. We do NOT additionally check that
        # the table's allocated_to string mentions plan_files[0]; that's a
        # stronger semantic match left to manual review.
        findings.append({
            "class": CLASS_A,
            "slot": f"§VII.{suffix}",
            "detail": f"plan {plan_files[0]} matches table entry (class={table[suffix]['class']})",
        })

    # --- Table-vs-plan class (D — orphaned table entry) — UNCHANGED ---
    for suffix, entry in table.items():
        if suffix in reservations:
            continue
        # Skip slots explicitly marked as (open) / (free) / (vacated) — those
        # are documented absences, not orphans.
        allocated = entry.get("allocated_to", "").lower()
        if any(tok in allocated for tok in ("(free)", "free)", "(open)", "open)", "(vacated)")):
            continue
        if entry.get("class", "").lower().strip() in ("(open)", "(vacated)", "(free)"):
            continue
        # If the registry has a corresponding header, treat the entry as
        # historically-correct (the slot is occupied by past content); not an
        # orphan. Class D fires only when neither plans nor registry agree.
        if suffix in registry_headers:
            continue
        findings.append({
            "class": CLASS_D,
            "slot": f"§VII.{suffix}",
            "detail": f"table allocates to '{entry['allocated_to']}' but no plan reserves and no registry header found",
        })

    # --- Registry-vs-table class (E — registry drift) — UNCHANGED ---
    for suffix in registry_headers:
        if suffix not in table:
            findings.append({
                "class": CLASS_E,
                "slot": f"§VII.{suffix}",
                "detail": "registry has §VII section header but table has no entry",
            })
            continue
        entry = table[suffix]
        # If the table marks the slot as free / open / vacated but the registry
        # actually has a header, that's drift.
        allocated = entry.get("allocated_to", "").lower()
        if any(tok in allocated for tok in ("(free)", "free)", "(open)", "open)", "(vacated)")):
            findings.append({
                "class": CLASS_E,
                "slot": f"§VII.{suffix}",
                "detail": f"table marks slot as {entry['allocated_to']} but registry has §VII.{suffix} header",
            })

    # --- NEW: Class-F STALE-STATUS detection (S87 2026-04-28 extension) ---
    # Independent pass over the table; does NOT modify Class A/B/C/D/E.
    # Substrate framing: the registry IS the framework's permanent-results
    # sequence; the audit checks the registry's own state-tracking against
    # itself (table claims vs header reality). Not a check on a container.
    for suffix, entry in table.items():
        first_landed = entry.get("first_landed", "")  # (local)
        registry_has_header = suffix in registry_first_appearance  # (local)
        table_says_open = is_open_status(first_landed)  # (local)
        # Skip rows where the table CLASS column itself is structurally OPEN
        # (already a Class-E candidate path; double-flagging is noise).
        class_cell = entry.get("class", "").lower().strip()  # (local)
        if class_cell in ("(open)", "(vacated)", "(free)"):
            continue

        if table_says_open and registry_has_header:
            findings.append({
                "class": CLASS_F,
                "slot": f"§VII.{suffix}",
                "detail": (
                    f"STALE-STATUS: table first_landed='{first_landed}' (OPEN) "
                    f"but registry §VII.{suffix} header at line "
                    f"{registry_first_appearance[suffix]}"
                ),
            })
        elif (not table_says_open) and (not registry_has_header):
            findings.append({
                "class": CLASS_F,
                "slot": f"§VII.{suffix}",
                "detail": (
                    f"STALE-STATUS-INVERSE: table first_landed='{first_landed}' "
                    f"(claims landed) but registry has NO §VII.{suffix} header"
                ),
            })

    return findings


def evaluate_verdict(findings: list[dict[str, Any]]) -> tuple[str, dict[str, int]]:
    """Aggregate findings into PASS / INFO / FAIL.

    Class-F (S87 extension) is informational only. The top-level verdict
    is preserved by the original 5-class rule:
      FAIL iff any C/D/E
      INFO iff only B (no C/D/E)
      PASS otherwise

    Class-F count is reported in the verdict-line value field as a
    diagnostic suffix when nonzero, but does NOT downgrade PASS to INFO.
    """
    counts: dict[str, int] = {c: 0 for c in TAXONOMY_CLASSES}
    for f in findings:
        counts[f["class"]] = counts[f["class"]] + 1

    has_hard_defect = (counts[CLASS_C] + counts[CLASS_D] + counts[CLASS_E]) > 0  # (local)
    has_soft_defect = counts[CLASS_B] > 0  # (local)
    # Class-F is intentionally EXCLUDED from defect logic per spec — it is
    # diagnostic, not blocking.

    if has_hard_defect:
        return "FAIL", counts
    if has_soft_defect:
        return "INFO", counts
    return "PASS", counts


def run_self_test() -> int:
    """Self-test: synthetic registry+table demonstrating Class-F detection.

    Constructs a synthetic registry+table pair containing:
      - 1 row that should fire Class-F STALE-STATUS (table says OPEN, registry
        has the header)
      - 1 row that should fire Class-F STALE-STATUS-INVERSE (table cites a
        landing, registry has NO header)
      - 2 rows that should pass cleanly as Class-A (matched plan reservation,
        table consistent with registry)

    Asserts: classify() detects EXACTLY 2 Class-F findings AND the existing
    5-class detection (A/B/C/D/E) is unchanged for the matched plans.

    Returns 0 on PASS (assertions hold), 1 on FAIL.
    """
    print("=" * 76)
    print("Class-F STALE-STATUS extension self-test")
    print("=" * 76)

    synthetic_registry = """
# Permanent Results Registry (synthetic)

## §VII Slot Allocation Table

| Letter | Class | Semantics | Allocated to | First landed |
|:-------|:------|:----------|:-------------|:-------------|
| §VII.AA | THM   | stale-open-test | TestAlloc | OPEN |
| §VII.BB | THM   | stale-inverse-test | TestAlloc | S99-FAKE-W1-LANDING |
| §VII.CC | THM   | clean-class-a | TestPlan | S99-CLEAN-LANDING |
| §VII.DD | THM   | clean-class-a-2 | TestPlan2 | S99-CLEAN-LANDING-2 |

## §VII.AA Stale-Open Theorem

(Header present despite OPEN table status — should fire Class-F STALE-STATUS.)

## §VII.CC Clean-Theorem

(Header present, table cites landing — should NOT fire Class-F.)

## §VII.DD Clean-Theorem-2

(Header present, table cites landing — should NOT fire Class-F.)
"""

    table = parse_slot_table(synthetic_registry)
    headers = parse_registry_headers(synthetic_registry)
    first_appearance = parse_registry_first_appearance(synthetic_registry)

    print(f"  parsed table entries: {sorted(table.keys())}")
    print(f"  parsed registry headers: {sorted(headers)}")
    print(f"  registry first_appearance: {sorted(first_appearance.items())}")

    # Synthetic plan reservations: ALL FOUR table rows get plan reservations
    # to isolate Class-F as the only NEW behavior surfaced by the synthetic
    # fixture.
    #
    # Substitution chain (verdict-direction):
    #   Definition: PASS iff (counts[C]+counts[D]+counts[E])==0 AND counts[B]==0
    #   Synthetic table entries: AA, BB, CC, DD (4 rows).
    #     AA → registry HAS header, plan reserves AA → Class-A AND Class-F STALE-STATUS
    #     BB → registry NO header, plan reserves BB → Class-A AND Class-F STALE-STATUS-INVERSE
    #     CC → registry HAS header, plan reserves CC, table cites landing → Class-A only
    #     DD → registry HAS header, plan reserves DD, table cites landing → Class-A only
    #   Substitute counts: A=4, B=0, C=0, D=0, E=0, F=2
    #   Simplify: has_hard_defect=(0+0+0)=0; has_soft_defect=0
    #   Direction: PASS (no C/D/E, no B) — verdict unaffected by F=2.
    reservations = {
        "AA": ["s99_synthetic_plan_aa.md"],
        "BB": ["s99_synthetic_plan_bb.md"],
        "CC": ["s99_synthetic_plan_cc.md"],
        "DD": ["s99_synthetic_plan_dd.md"],
    }

    findings = classify(table, reservations, headers, first_appearance)

    class_f_findings = [f for f in findings if f["class"] == CLASS_F]
    class_a_findings = [f for f in findings if f["class"] == CLASS_A]
    class_d_findings = [f for f in findings if f["class"] == CLASS_D]
    class_e_findings = [f for f in findings if f["class"] == CLASS_E]

    print(f"\n  Total findings:    {len(findings)}")
    print(f"  Class-A findings:  {len(class_a_findings)}")
    print(f"  Class-D findings:  {len(class_d_findings)}")
    print(f"  Class-E findings:  {len(class_e_findings)}")
    print(f"  Class-F findings:  {len(class_f_findings)}")
    for f in findings:
        print(f"    [{f['class']}] {f['slot']} — {f['detail']}")

    # ----- Assertions -----
    ok = True
    if len(class_f_findings) != 2:
        print(f"\n  FAIL assertion 1: expected 2 Class-F findings, got {len(class_f_findings)}")
        ok = False
    aa_hits = [f for f in class_f_findings if f["slot"] == "§VII.AA"]
    bb_hits = [f for f in class_f_findings if f["slot"] == "§VII.BB"]
    if len(aa_hits) != 1 or "STALE-STATUS:" not in aa_hits[0]["detail"] or "STALE-STATUS-INVERSE" in aa_hits[0]["detail"]:
        print("  FAIL assertion 2: §VII.AA STALE-STATUS not detected as expected")
        ok = False
    if len(bb_hits) != 1 or "STALE-STATUS-INVERSE:" not in bb_hits[0]["detail"]:
        print("  FAIL assertion 3: §VII.BB STALE-STATUS-INVERSE not detected as expected")
        ok = False
    if len(class_a_findings) != 4:
        print(f"  FAIL assertion 4: expected 4 Class-A findings (AA, BB, CC, DD), got {len(class_a_findings)}")
        ok = False

    verdict, counts = evaluate_verdict(findings)
    print(f"\n  Aggregate verdict: {verdict}")
    print(f"  Counts: {counts}")
    # Class-F should NOT downgrade PASS — verdict should be PASS since no C/D/E.
    if verdict != "PASS":
        print(f"  FAIL assertion 5: Class-F should NOT downgrade verdict; got {verdict}")
        ok = False

    if ok:
        print("\n  SELF-TEST: PASS (2 Class-F findings detected; 4 Class-A preserved; verdict=PASS)")
        return 0
    else:
        print("\n  SELF-TEST: FAIL")
        return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="§VII slot-allocation audit — plan-vs-table-vs-registry mismatch detector"
    )
    project_root_default = Path(__file__).resolve().parent.parent.parent  # computations/_shared/_X.py → project root
    parser.add_argument(
        "--registry", type=str,
        default=str(project_root_default / "sessions" / "permanent-results-registry.md"),
        help="path to permanent-results-registry.md",
    )
    parser.add_argument(
        "--plan-glob", type=str,
        default=str(project_root_default / "sessions" / "session-plan" / "*.md"),
        help="glob for plan files to scan",
    )
    parser.add_argument("--json", action="store_true", help="emit JSON to stdout in addition to text")
    parser.add_argument("--quiet", action="store_true", help="suppress per-finding text output (verdict line only)")
    parser.add_argument("--self-test", action="store_true",
                        help="run Class-F STALE-STATUS extension self-test (S87 2026-04-28)")
    args = parser.parse_args(argv)

    if args.self_test:
        return run_self_test()

    registry_path = Path(args.registry)
    plan_glob_path = Path(args.plan_glob)
    plan_files = sorted(plan_glob_path.parent.glob(plan_glob_path.name))

    # ---- Log input SHAs (gate-verdicts.md S81+ rule, first ~20 lines of stdout) ----
    self_path = Path(__file__)
    self_sha = sha256_of_file(self_path)  # (local)
    registry_sha = sha256_of_file(registry_path)  # (local)
    plan_glob_sha = sha256_of_text("\n".join(p.name for p in plan_files))  # (local)

    if not args.quiet:
        print("=" * 76)
        print("_vii_slot_allocation_audit.py — §VII slot allocation retrospection")
        print("=" * 76)
        print(f"script_sha256:    {self_sha}")
        print(f"registry_sha256:  {registry_sha}")
        print(f"plan_glob_sha256: {plan_glob_sha}")
        print(f"plan_files:       {len(plan_files)}")
        print(f"registry_path:    {registry_path}")
        print("-" * 76)

    if registry_sha == "MISSING":
        verdict = "FAIL"
        findings: list[dict[str, Any]] = [{
            "class": CLASS_E,
            "slot": "(registry)",
            "detail": f"registry file missing: {registry_path}",
        }]
        counts = {c: 0 for c in TAXONOMY_CLASSES}
        counts[CLASS_E] = 1
        table_count = 0          # (local) registry missing → no table entries to count
        registry_header_count = 0  # (local) registry missing → no headers to count
        reservation_count = 0    # (local) registry missing → still report reservation_count for input_pin_map
    else:
        registry_text = registry_path.read_text(encoding="utf-8", errors="replace")
        table = parse_slot_table(registry_text)
        registry_headers = parse_registry_headers(registry_text)
        registry_first_appearance = parse_registry_first_appearance(registry_text)
        reservations = parse_plan_reservations(plan_files)
        findings = classify(table, reservations, registry_headers, registry_first_appearance)
        verdict, counts = evaluate_verdict(findings)
        table_count = len(table)
        registry_header_count = len(registry_headers)
        reservation_count = sum(len(v) for v in reservations.values())

    # Closure SHA over the input-pin map
    input_pin_map = {
        "script_sha256": self_sha,
        "registry_sha256": registry_sha,
        "plan_glob_sha256": plan_glob_sha,
        "plan_file_count": len(plan_files),
        "table_entry_count": table_count,
        "registry_header_count": registry_header_count,
        "reservation_count": reservation_count,
        "taxonomy_classes": list(TAXONOMY_CLASSES),
    }
    audit_sha = closure_hash(input_pin_map)  # (local)

    content_payload = json.dumps(
        {"verdict": verdict, "counts": counts, "findings": findings},
        sort_keys=True, separators=(",", ":"),
    )
    content_sha = sha256_of_text(content_payload)  # (local)

    if not args.quiet:
        print(f"\nTable entries:  {table_count}")
        print(f"Registry headers: {registry_header_count}")
        print(f"Plan reservations: {reservation_count}")
        print(f"\nTaxonomy distribution: {counts}")
        if findings:
            print("\nFindings:")
            for f in findings:
                print(f"  [{f['class']}] {f['slot']} — {f['detail']}")
        else:
            print("\nNo findings.")
        # 4-tuple value field: append class_f_drift suffix if Class-F count > 0.
        value_field = f"count_findings_{sum(counts.values())}"  # (local)
        if counts[CLASS_F] > 0:
            value_field = f"{value_field}_class_f_drift_{counts[CLASS_F]}"  # (local)
        print(f"\n4-tuple: (value={value_field}, "
              f"scheme=vii_slot_allocation_audit_v2, convention=6-class-taxonomy-extended-A-through-F, L_max=N/A)")
        print(f"audit_sha256:   {audit_sha}")
        print(f"content_sha256: {content_sha}")
        print(f"VERDICT: {verdict}")

    if args.json:
        out_payload = {
            "verdict": verdict,
            "counts": counts,
            "findings": findings,
            "table_entry_count": table_count,
            "registry_header_count": registry_header_count,
            "reservation_count": reservation_count,
            "input_pin_map": input_pin_map,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "fourtuple": {
                "value": sum(counts.values()),
                "scheme": "vii_slot_allocation_audit_v2",
                "convention": "6-class-taxonomy-extended-A-through-F",
                "L_max": "N/A",
            },
        }
        print(json.dumps(out_payload, indent=2) if not args.quiet else json.dumps(out_payload, separators=(",", ":")))

    return 0  # exit 0 regardless of verdict (verdict is data; per math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
