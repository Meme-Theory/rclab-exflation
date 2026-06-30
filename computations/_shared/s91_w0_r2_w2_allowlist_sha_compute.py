#!/usr/bin/env python3
"""S91 W0 R2 — Compute plan-block SHAs for S90 W2-1..W2-15 allowlist batch.

Per `.claude/rules/methodology-wave-allowlist.md` schema (3-column form, post-S88
W9-RULE-CLEANUP lift-out): each row records `(gate_id, session, sha256_of_plan_block)`
where the SHA is computed via SHA-256 over the plan-file gate-block text
(from the `## §W{i}-{n}.` heading through but not including the next `## §`
heading or EOF).

Pairs with `sessions/framework/registry/methodology-wave-instances.md` rationale
prose entries (S88 W9-RULE-CLEANUP precedent — rationale lives in registry,
allowlist holds the 3-column audit tuples).

S90 W2 gate-block boundaries (from grep `^## §W2-` in
`sessions/session-plan/session-90-plan-w2.md`):
  §W2-1   at line 67   — CF-18 §VII.AAU/§VII.AV withdrawn-in-favor-of LANDING-CLEANUP
  §W2-2   at line 195  — CF-19 §VII.NEXT substrate-clock-uniqueness STAGE-1-CANDIDATE
  §W2-3   at line 336  — CF-20 §VII.AH STAGE-3-PERMANENT promotion
  §W2-4   at line 440  — CF-21 §VII.W-3.LAB Element-2 OE-form retrofit
  §W2-5   at line 553  — CF-22 §VII.AR Stage-2 PENDING A36 sub-claim advancement
  §W2-6   at line 663  — CF-23 §VII.AN registry-anchor reconciliation
  §W2-7   at line 763  — CF-24 §W6a plan-file-or-downstream anchor reconciliation
  §W2-8   at line 862  — CF-25 §VII.U.2 corner-reconciliation Reading-B lock-in
  §W2-9   at line 974  — CF-26 §VII.AF.1.OP-PROJ annotation clarification + W5 V4
  §W2-10  at line 1089 — CF-27 canonical_constants R_universal HP1 strict-F4 Class-(d)
  §W2-11  at line 1230 — CF-28 canonical_constants eps_H HP1 norm provenance addition
  §W2-12  at line 1354 — CF-29 falsifier-inventory row-3 alpha_s_canonical update
  §W2-13  at line 1487 — CF-30 DR3 binding-protocol readiness audit
  §W2-14  at line 1588 — CF-31 falsifier-inventory row-2 r dual-pathway update
  §W2-15  at line 1691 — CF-32 mack-observational-constraints S89 update (EOF at 1929)

Cross-link: `.claude/rules/methodology-wave-allowlist.md` §"Edit discipline"
item 4 (Append-helper writes 3-column rows only; parallel registry entry).
Canonical append-helper precedent: `computations/session-88/s88_w8_allowlist_append_helper.py`.

Output: `s91_w0_r2_w2_allowlist_shas.json` with per-gate SHA + line range.
"""
import hashlib
import json
import re
import sys
from pathlib import Path

# Canonical-constants import per `computations/_shared/CLAUDE.md` MANDATORY discipline.
SHARED_DIR = Path(__file__).resolve().parent  # (local) — script-dir resolver
sys.path.insert(0, str(SHARED_DIR))
try:
    from canonical_constants import *  # noqa: F401,F403,E402
except Exception as e:
    print(f"WARNING: canonical_constants.py import failed: {e}", file=sys.stderr)
    # Not fatal — this script computes SHAs, doesn't use framework constants.

REPO_ROOT = Path(__file__).resolve().parents[2]  # (local) project root (Ainulindale Exflation/)
PLAN_FILE = REPO_ROOT / "sessions" / "session-plan" / "session-90-plan-w2.md"  # (local)
OUTPUT_JSON = REPO_ROOT / "computations" / "_shared" / "s91_w0_r2_w2_allowlist_shas.json"  # (local)

GATE_HEADING_RE = re.compile(r"^## §W2-(\d+)\.\s+(.+?)$", re.MULTILINE)  # (local)


def extract_gate_blocks(plan_text: str) -> list[dict]:
    """Extract (gate_label, gate_title, block_text, line_start, line_end) tuples.

    A gate block spans from a `## §W2-N.` heading through but not including
    the next `## §` heading (any level) or EOF.
    """
    lines = plan_text.splitlines(keepends=True)
    # Find heading line numbers (0-indexed)
    heading_indices = []  # (local) list[(line_idx, gate_num, gate_title)]
    for i, line in enumerate(lines):
        m = GATE_HEADING_RE.match(line)
        if m:
            heading_indices.append((i, int(m.group(1)), m.group(2).strip()))

    # Build blocks
    blocks = []  # (local)
    for j, (start_line_idx, gate_num, gate_title) in enumerate(heading_indices):
        # End is start of NEXT W2-N heading, OR first `## §` heading after start, OR EOF
        if j + 1 < len(heading_indices):
            end_line_idx = heading_indices[j + 1][0]
        else:
            # Scan from start_line_idx onward for next `## §` heading; if none, EOF
            end_line_idx = len(lines)
            for k in range(start_line_idx + 1, len(lines)):
                if lines[k].startswith("## §") and not GATE_HEADING_RE.match(lines[k]):
                    end_line_idx = k
                    break
        block_text = "".join(lines[start_line_idx:end_line_idx])
        block_sha = hashlib.sha256(block_text.encode("utf-8")).hexdigest()  # (local)
        blocks.append({
            "gate_label": f"W2-{gate_num}",
            "gate_title": gate_title,
            "line_start": start_line_idx + 1,  # 1-indexed for display
            "line_end_exclusive": end_line_idx + 1,
            "byte_count": len(block_text.encode("utf-8")),
            "sha256_of_plan_block": block_sha,
        })
    return blocks


def main():
    if not PLAN_FILE.exists():
        print(f"ERROR: plan file not found at {PLAN_FILE}", file=sys.stderr)
        sys.exit(1)
    plan_text = PLAN_FILE.read_text(encoding="utf-8")
    blocks = extract_gate_blocks(plan_text)

    if len(blocks) != 15:
        print(f"WARNING: expected 15 W2 gate-blocks, found {len(blocks)}", file=sys.stderr)

    # Emit tabular summary to stdout for human inspection
    print(f"S90 W2 plan-block SHA computation ({PLAN_FILE.name})")
    print(f"=" * 100)
    print(f"{'gate':<8} {'lines':<14} {'bytes':<8} {'sha256_of_plan_block':<64} title")
    print(f"-" * 100)
    for b in blocks:
        lines_str = f"{b['line_start']}-{b['line_end_exclusive']-1}"
        title_short = b["gate_title"][:60]
        print(f"{b['gate_label']:<8} {lines_str:<14} {b['byte_count']:<8} {b['sha256_of_plan_block']:<64} {title_short}")
    print(f"-" * 100)
    print(f"Total: {len(blocks)} gate-blocks")
    print()

    # Emit JSON sidecar
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(blocks, indent=2, ensure_ascii=False))
    print(f"JSON sidecar: {OUTPUT_JSON}")

    # Emit allowlist-rows pre-formatted for paste into rule file
    print()
    print("=" * 100)
    print("Allowlist rows (for `.claude/rules/methodology-wave-allowlist.md` append):")
    print("-" * 100)
    for b in blocks:
        print(f"| {b['gate_label']:<7} | S90 | {b['sha256_of_plan_block']} |")


if __name__ == "__main__":
    main()
