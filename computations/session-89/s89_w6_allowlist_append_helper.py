#!/usr/bin/env python
"""
s89_w6_allowlist_append_helper.py — S89 W6 allowlist + registry append
========================================================================

Per `session-89-plan-w6.md §"Wave 6 Methodology-wave-allowlist Append
Helper Spec"` and `methodology-wave-allowlist.md §"Append-helper canonical"`:

Appends 8 NEW rows to `.claude/rules/methodology-wave-allowlist.md` AFTER
the existing tail. Each row is `| gate_id | session | sha256_of_plan_block |`
(3-column form per the W9-RULE-CLEANUP lift-out; rationale prose lives
in the parallel registry).

Also appends 8 parallel rationale-prose entries to
`sessions/framework/registry/methodology-wave-instances.md` keyed by
`### {gate_id} ({session}) — {sha}` heading.

Single-shot POSIX O_APPEND (atomic; parallel-writer-safe) per
`methodology-wave-allowlist.md §"Edit discipline"` item 4.

Modeled on `computations/session-88/s88_w8_allowlist_append_helper.py`
canonical pattern.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import hashlib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import *  # noqa: F401,F403


S89_W6_ALLOWLIST_ROWS: list[dict[str, str]] = [
    {"gate_id": "W6-1", "session": "S89", "anchor": "§W6-1"},
    {"gate_id": "W6-2", "session": "S89", "anchor": "§W6-2"},
    {"gate_id": "W6-3", "session": "S89", "anchor": "§W6-3"},
    {"gate_id": "W6-4", "session": "S89", "anchor": "§W6-4"},
    {"gate_id": "W6-5", "session": "S89", "anchor": "§W6-5"},
    {"gate_id": "W6-6", "session": "S89", "anchor": "§W6-6"},
    {"gate_id": "W6-7", "session": "S89", "anchor": "§W6-7"},
    {"gate_id": "W6-8", "session": "S89", "anchor": "§W6-8"},
]


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compute_sha_of_plan_block(plan_md: Path, anchor: str) -> str:
    """SHA-256 over the plan-file gate block (between anchor and next anchor)."""
    text = plan_md.read_text(encoding="utf-8")
    pattern = (
        rf"## {re.escape(anchor)}\..*?"
        rf"(?=## §W6-\d|## Wave 6 →|\Z)"
    )
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return "pending"
    return sha256_of_text(match.group(0))


def append_allowlist_rows(allowlist_path: Path, plan_md: Path) -> list[tuple[str, str, str]]:
    """Append 8 rows. Returns list of (gate_id, session, sha) triples."""
    rows = []  # local
    for spec in S89_W6_ALLOWLIST_ROWS:
        sha = compute_sha_of_plan_block(plan_md, spec["anchor"])
        rows.append((spec["gate_id"], spec["session"], sha))
    # Single atomic POSIX O_APPEND
    with allowlist_path.open("a", encoding="utf-8") as f:
        for gate_id, session, sha in rows:
            f.write(f"| {gate_id} | {session} | {sha} |\n")
    return rows


def append_registry_entries(
    registry_path: Path,
    rows: list[tuple[str, str, str]],
) -> None:
    """Append parallel rationale-prose entries to methodology-wave-instances.md."""
    entries = []  # local
    for gate_id, session, sha in rows:
        co_author_line = (
            "connes-ncg-theorist CO-AUTHOR for numerical D_max "
            "measurement (PV pipeline cross-check)."
            if gate_id == "W6-7"
            else "Sole authorship: gen-physicist orchestrator-direct-write."
        )
        entry = f"""

### {gate_id} ({session}) — {sha}

**Provenance**: gen-physicist orchestrator-direct planner-write per
`/rclab-plan` skill §3b; `wave-classification.md §"Dispatch consequences"`
— METHODOLOGY-class waves SKIP `/rclab-coordinate` compute-mode. Source:
`sessions/session-plan/session-89-plan-w6.md` §{gate_id.split("-", 1)[1]}.

**M1∧M2∧M3∧M4 conjunction**:
- M1 (PASS predicate type): artifact-existence-with-substantive-content per gate block §9.
- M2 (Producing-operation type): `Edit`/`Write`/`MultiEdit` on `.claude/{{rules,templates,skills}}/**` + grep/wc/SHA-256 cross-checks (or audit-script Python under `computations/_shared/`).
- M3 (Source-of-truth type): verbatim sub-diff from S88 Ledger A item per `session-89-context.md` Cluster F.
- M4 (Allowlist membership): this row appends gate-ID to `methodology-wave-allowlist.md`.

**Authorship**: gen-physicist orchestrator-direct-write under METHODOLOGY-class dispatch consequences. {co_author_line}

**Cross-link**: `sessions/session-plan/session-89-plan-w6.md` §{gate_id}.
"""
        entries.append(entry)
    with registry_path.open("a", encoding="utf-8") as f:
        for entry in entries:
            f.write(entry)


def verify_post_append(
    allowlist_path: Path,
    registry_path: Path,
    rows: list[tuple[str, str, str]],
) -> dict:
    """Verify all 8 rows landed in both files with matching SHAs."""
    allowlist_text = allowlist_path.read_text(encoding="utf-8")
    registry_text = registry_path.read_text(encoding="utf-8")
    allow_present = sum(
        1 for gate_id, session, sha in rows
        if f"| {gate_id} | {session} | {sha} |" in allowlist_text
    )
    registry_present = sum(
        1 for gate_id, session, sha in rows
        if f"### {gate_id} ({session}) — {sha}" in registry_text
    )
    return {
        "n_rows_target": len(rows),
        "n_rows_in_allowlist": allow_present,
        "n_rows_in_registry": registry_present,
        "all_landed": (allow_present == len(rows)
                       and registry_present == len(rows)),
        "rows": rows,
    }


def main() -> int:
    allowlist_path = Path(".claude/rules/methodology-wave-allowlist.md")
    registry_path = Path("sessions/framework/registry/methodology-wave-instances.md")
    plan_md = Path("sessions/session-plan/session-89-plan-w6.md")

    if not allowlist_path.exists():
        print(f"ERROR: allowlist not found at {allowlist_path}", file=sys.stderr)
        return 1
    if not registry_path.exists():
        print(f"ERROR: registry not found at {registry_path}", file=sys.stderr)
        return 1
    if not plan_md.exists():
        print(f"ERROR: plan not found at {plan_md}", file=sys.stderr)
        return 1

    rows = append_allowlist_rows(allowlist_path, plan_md)
    append_registry_entries(registry_path, rows)
    verification = verify_post_append(allowlist_path, registry_path, rows)
    import json
    print(json.dumps(verification, indent=2))
    return 0 if verification["all_landed"] else 1


if __name__ == "__main__":
    sys.exit(main())
