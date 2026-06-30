"""S93 methodology-wave-allowlist append helper (orchestrator-only edit).

Reusable across all S93 METHODOLOGY-class gates. Computes `sha256_of_plan_block`
over the gate's plan-file block (raw UTF-8 bytes, plain hashlib.sha256, from the
gate's `## §` header through the line preceding the next `## ` header), then:

  1. appends the 3-column ledger row `| {gate_id} | {session} | {sha} |` to
     sessions/framework/registry/methodology-wave-allowlist-ledger.md
  2. appends the parallel rationale entry to
     sessions/framework/registry/methodology-wave-instances.md

POSIX O_APPEND (open("a")) per `epistemic-discipline.md §"Registry-Write Hygiene"`;
idempotent (skips append if the (gate_id, session) row / entry already present).
Ledger carries 3-column rows ONLY (W9-RULE-CLEANUP lift-out); rationale prose
lives in the instances file (Edit-discipline item 4 of methodology-wave-allowlist.md).

Usage:
  python s93_allowlist_append_helper.py \
      --gate-id S93-W0-1-... --plan-file sessions/session-plan/session-93-plan-w0.md \
      --section "## §W0-1." --session S93 --rationale-file <path-to-rationale.txt>
"""
import argparse
import datetime
import hashlib
from pathlib import Path

from canonical_constants import *  # noqa: F401,F403 — project convention (computations/_shared/CLAUDE.md); this registry-append utility consumes no framework constants

ROOT = Path(__file__).resolve().parents[2]
LEDGER = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-allowlist-ledger.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"


def extract_block(plan_file: Path, section_marker: str):
    """Return (block_text, start_1indexed, end_exclusive) for the gate block."""
    lines = plan_file.read_text(encoding="utf-8").splitlines(keepends=True)
    start = None
    for i, ln in enumerate(lines):
        if ln.startswith(section_marker):
            start = i
            break
    if start is None:
        raise SystemExit(f"ERR: section '{section_marker}' not found in {plan_file}")
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return "".join(lines[start:end]), start + 1, end


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--gate-id", required=True)
    ap.add_argument("--plan-file", required=True)
    ap.add_argument("--section", required=True, help='e.g. "## §W0-1."')
    ap.add_argument("--session", default="S93")
    ap.add_argument("--rationale-file", required=True)
    a = ap.parse_args()

    plan_file = ROOT / a.plan_file
    block, s, e = extract_block(plan_file, a.section)
    sha = hashlib.sha256(block.encode("utf-8")).hexdigest()

    # (1) ledger 3-column row
    led = LEDGER.read_text(encoding="utf-8")
    if f"| {a.gate_id} | {a.session} |" in led:
        print(f"LEDGER: row for {a.gate_id} {a.session} already present; no-op")
    else:
        with LEDGER.open("a", encoding="utf-8") as f:
            f.write(f"| {a.gate_id} | {a.session} | {sha} |\n")
        print(f"LEDGER: appended {a.gate_id} {a.session} sha={sha[:16]} (block lines {s}-{e})")

    # (2) instances rationale entry
    inst = INSTANCES.read_text(encoding="utf-8")
    rationale = (ROOT / a.rationale_file).read_text(encoding="utf-8").strip()
    today = datetime.date.today().isoformat()
    entry = (
        f"\n### {a.gate_id} ({a.session}) — {sha[:16]}\n\n"
        f"**Full plan-block SHA**: `{sha}`\n"
        f"**Plan-file block range**: lines {s}-{e} of `{a.plan_file}` "
        f"(from `{a.section}` header through the line preceding the next `## ` header; "
        f"raw UTF-8 bytes, plain `hashlib.sha256`)\n"
        f"**Landing date**: {today}\n\n"
        f"{rationale}\n"
    )
    if f"### {a.gate_id} ({a.session})" in inst:
        print(f"INSTANCES: entry for {a.gate_id} already present; no-op")
    else:
        with INSTANCES.open("a", encoding="utf-8") as f:
            f.write(entry)
        print(f"INSTANCES: appended rationale for {a.gate_id}")

    print(f"SHA={sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
