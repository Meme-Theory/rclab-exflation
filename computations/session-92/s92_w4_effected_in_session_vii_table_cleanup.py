"""
S92 W4 Effected-In-Session §VII slot-table cleanup.

Surfaced by `_vii_slot_allocation_audit.py` after the path bug at line 522
was fixed this session. 32 E_REGISTRY_VS_TABLE_DRIFT findings (slots have
section headers in the registry body but no entry in the top-of-registry
§VII allocation table at lines 47-130) are mechanically fixable: parse each
slot's `### §VII.<slot> — <description>` body header to extract description +
owner + date, then append a properly-formatted row to the §VII table.

This script is METHODOLOGY-class housekeeping per `feedback_fix-in-session-never-defer.md`
+ `feedback_no-asking-just-execute.md` (pre-existing audit failures fixed
in-session when surfaced). NO substrate-physics content; pure mechanical
slot-table maintenance.

Outputs:
  - sessions/permanent-results-registry.md (modified: appends 32 rows to §VII table)
  - computations/session-92/s92_w4_effected_in_session_vii_table_cleanup.json (sidecar)

Per `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"`:
single-script POSIX-O_APPEND-equivalent (in-memory string replace + atomic write),
mtime-conflict-safe since this is orchestrator-direct in Effected-In-Session AFTER
all Wave 4 agents have closed.
"""
from __future__ import annotations
import hashlib
import json
import re
import sys
from pathlib import Path

# Project-rule requirement (computations/_shared/CLAUDE.md): all scripts MUST
# import canonical_constants. This script is METHODOLOGY-class housekeeping
# (no substrate-physics use), but the import satisfies the audit hook.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
SIDECAR = Path(__file__).with_suffix(".json")

# 32 E-class slots from the audit (S92 W4 Effected-In-Session surface)
MISSING_E_SLOTS = [
    "§VII.AO", "§VII.AX", "§VII.AZ.OP-PROJ", "§VII.AW.OP-PROJ", "§VII.AN",
    "§VII.AR", "§VII.BC.OP-PROJ", "§VII.AS", "§VII.K-PROP-W8-LAYERED",
    "§VII.U.2", "§VII.AJ.OP-PROJ", "§VII.BE", "§VII.AX.OP-PROJ",
    "§VII.AT.OP-PROJ", "§VII.AO-CORRIGENDUM", "§VII.U.6.k1-vs-k2",
    "§VII.AF.1.OP-PROJ", "§VII.AQ.STATE-PROJ", "§VII.AV", "§VII.AU.OP-PROJ",
    "§VII.BB", "§VII.AP", "§VII.AN-CORRIGENDUM", "§VII.AJ.STATE-PROJ",
    "§VII.AF.1.STATE-PROJ", "§VII.BA", "§VII.AY.OP-PROJ", "§VII.AV.OP-PROJ",
    "§VII.BD.OP-PROJ", "§VII.AAU.OP-PROJ", "§VII.AQ.OP-PROJ",
    "§VII.K-PROP-HK-2-WINDOWED-PV-AS-SD-REFINEMENT",
]

# Owner inference patterns (most-specific first)
OWNER_PATTERNS = [
    (r"mack-cosmic-bridge sole-writer", "mack-cosmic-bridge"),
    (r"mack-cosmic-bridge", "mack-cosmic-bridge"),
    (r"volovik-superfluid-universe-theorist", "volovik-superfluid-universe-theorist"),
    (r"lizzi-spectral-functional-theorist", "lizzi-spectral-functional-theorist"),
    (r"connes-ncg-theorist", "connes-ncg-theorist"),
    (r"van-den-dungen-bridge-theorist", "van-den-dungen-bridge-theorist"),
    (r"gen-physicist", "gen-physicist"),
    (r"hawking-theorist", "hawking-theorist"),
    (r"knowledge-weaver", "knowledge-weaver"),
    (r"transit-dynamics-theorist", "transit-dynamics-theorist"),
    (r"baptista-spacetime-analyst", "baptista-spacetime-analyst"),
    (r"sagan-empiricist", "sagan-empiricist"),
    (r"landau-condensed-matter-theorist", "landau-condensed-matter-theorist"),
]

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")

# Class inference patterns (most-specific first)
CLASS_PATTERNS = [
    (r"CORRIGENDUM", "META"),
    (r"K-PROP-", "THM"),
    (r"OP-PROJ", "THM"),
    (r"STATE-PROJ", "THM"),
    (r"Bridge Theorem|Structural Theorem|Cohomology|STAGE-1-CANDIDATE", "THM"),
    (r"Pre-Registration|methodology|META", "META"),
]


def slot_to_regex(slot: str) -> re.Pattern[str]:
    """Slot like §VII.AX.OP-PROJ → regex that matches the body header.
    Accepts both H2 (`## `) and H3 (`### `) headers per the audit script's parser."""
    escaped = re.escape(slot)
    return re.compile(rf"^#{{2,3}} {escaped}(?:[\s.—(].*)?$", re.MULTILINE)


def extract_metadata(body_text: str, slot: str) -> dict:
    """Find the body header for slot; extract description, owner, date, class."""
    pat = slot_to_regex(slot)
    m = pat.search(body_text)
    if not m:
        return {"slot": slot, "found": False}
    header_line = m.group(0)
    # Strip the leading '### §VII.<slot>' prefix
    after_slot = header_line.split(slot, 1)[1].lstrip(" —.")
    # Trim to about 90 chars for the Semantics column
    description = after_slot[:200].strip()
    # Owner inference
    owner = "(unknown)"
    for pat_str, owner_name in OWNER_PATTERNS:
        if re.search(pat_str, after_slot):
            owner = owner_name
            break
    # Date inference
    date_m = DATE_RE.search(after_slot)
    date = date_m.group(1) if date_m else "(undated)"
    # Class inference
    cls = "THM"  # default
    for pat_str, cls_name in CLASS_PATTERNS:
        if re.search(pat_str, slot + " " + after_slot):
            cls = cls_name
            break
    return {
        "slot": slot,
        "found": True,
        "description": description,
        "owner": owner,
        "date": date,
        "class": cls,
        "header_line_excerpt": header_line[:140],
    }


def build_row(meta: dict) -> str:
    """5-column table row matching the existing format at lines 47-130."""
    # Truncate description to keep table readable
    desc = meta["description"]
    if len(desc) > 160:
        desc = desc[:157] + "..."
    return f"| {meta['slot']} | {meta['class']} | {desc} | {meta['owner']} | {meta['date']} |"


def main() -> int:
    if not REGISTRY.exists():
        print(f"ERROR: registry not found at {REGISTRY}", file=sys.stderr)
        return 1
    body = REGISTRY.read_text(encoding="utf-8")
    pre_sha = hashlib.sha256(body.encode("utf-8")).hexdigest()
    pre_lines = body.split("\n")

    # Idempotency: identify slots that ALREADY have a §VII top-table row
    # (anywhere in lines 47-200 to safely cover prior cleanup-script appends)
    already_in_table = set()
    table_row_re = re.compile(r"^\| (§VII\.[A-Za-z0-9_.-]+(?:\.[A-Za-z0-9_.-]+)*) \|")
    for i, line in enumerate(pre_lines):
        if i + 1 < 47:
            continue
        if i + 1 > 250:
            break
        m = table_row_re.match(line)
        if m:
            already_in_table.add(m.group(1))

    # Extract metadata for missing slots (skip ones already in the table)
    extractions = []
    for slot in MISSING_E_SLOTS:
        if slot in already_in_table:
            extractions.append({"slot": slot, "found": False,
                                "skip_reason": "already_in_table_post_prior_cleanup_run"})
            continue
        meta = extract_metadata(body, slot)
        extractions.append(meta)

    rows = [build_row(m) for m in extractions if m.get("found")]
    missing_count = sum(1 for m in extractions if not m.get("found") and m.get("skip_reason") != "already_in_table_post_prior_cleanup_run")
    skipped_idempotent = sum(1 for m in extractions if m.get("skip_reason") == "already_in_table_post_prior_cleanup_run")

    # Find the §VII table's last row (lines 47-130 range; last row is the
    # last line matching `^| §VII\.` before a blank line)
    table_end_idx = None
    for i, line in enumerate(pre_lines):
        if i + 1 < 47:
            continue
        if i + 1 > 200:  # safety cap
            break
        if line.startswith("| §VII."):
            table_end_idx = i  # 0-indexed
    if table_end_idx is None:
        print("ERROR: §VII table not found", file=sys.stderr)
        return 1

    # Insert the 32 rows after the last existing row
    insertion_block = [
        "",
        "<!-- S92 W4 Effected-In-Session §VII slot-table cleanup (orchestrator-direct, "
        "per `feedback_fix-in-session-never-defer.md` + `feedback_no-asking-just-execute.md`; "
        f"32 E_REGISTRY_VS_TABLE_DRIFT findings surfaced by `_vii_slot_allocation_audit.py` "
        f"after path bug fix at line 522 in S92 W4) -->",
    ]
    new_lines = (
        pre_lines[:table_end_idx + 1]
        + rows
        + insertion_block
        + pre_lines[table_end_idx + 1:]
    )
    new_body = "\n".join(new_lines)
    post_sha = hashlib.sha256(new_body.encode("utf-8")).hexdigest()
    REGISTRY.write_text(new_body, encoding="utf-8")

    result = {
        "registry_path": str(REGISTRY),
        "pre_sha256": pre_sha,
        "post_sha256": post_sha,
        "missing_slot_count": len(MISSING_E_SLOTS),
        "found_count": len(rows),
        "not_found_count": missing_count,
        "skipped_idempotent": skipped_idempotent,
        "table_end_idx_0based": table_end_idx,
        "rows_inserted": rows,
        "extractions": extractions,
    }
    SIDECAR.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"Inserted {len(rows)} rows into §VII table.")
    print(f"  pre_sha: {pre_sha[:16]}...")
    print(f"  post_sha: {post_sha[:16]}...")
    print(f"  not found in body: {missing_count}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
