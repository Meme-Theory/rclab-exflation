"""S101 plan-freeze allowlist append helper (orchestrator-effected).

Appends the three W8b METHODOLOGY-class gate-ID rows to the allowlist ledger
(3-column rows ONLY, per methodology-wave-allowlist.md Edit-discipline item 4)
and the paired rationale entries to methodology-wave-instances.md.

Pattern: single-shot open('a') append per the canonical
computations/session-88/s88_w8_allowlist_append_helper.py precedent.
SHA convention per the S98-HK-SIGMA8-CHANNEL-KEYED-PINS instances entry:
block = from the '## §' header line through the line preceding the next '## '
header; raw UTF-8 bytes; plain hashlib.sha256.

Source of the row prescription: sessions/session-plan/session-101-plan-w8.md
lines 34-42 (ALLOWLIST APPEND REQUIRED block).

canonical_constants exemption: registry append-helper, zero framework constants
consumed (paths + gate-ID strings only) — same shape as the canonical
s88_w8_allowlist_append_helper.py, which carries no canonical_constants import.
"""
import hashlib
import io
import sys

PLAN = r"sessions/session-plan/session-101-plan-w8.md"
LEDGER = r"sessions/framework/registry/methodology-wave-allowlist-ledger.md"
INSTANCES = r"sessions/framework/registry/methodology-wave-instances.md"

GATES = [
    ("S101-HK-SELECTION-RULE-PREFLIGHT-RULE", "## §W8b-1."),
    ("S101-HK-SUFFIX-DISCIPLINE", "## §W8b-2."),
    ("S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION", "## §W8b-3."),
]

RATIONALE = {
    "S101-HK-SELECTION-RULE-PREFLIGHT-RULE": (
        "S101 W8b-1 — METHODOLOGY-class rule-file extension: math-scripts.md "
        "Double-Check-Logic gains the center-character/triality CG-admissibility "
        "pre-flight directive (directive-only; calibration instance = the S100a W2-2 "
        "selection-rule finding, audit 871573da..., routed to the corpus). "
        "M1 artifact-existence (rule section + corpus section + content-SHA); "
        "M2 Edit + corpus append-helper + grep/SHA cross-checks (no threshold .py); "
        "M3 verbatim-extract from housekeeping-100a SD CF-W2-1 (no new derivation); "
        "M4 allowlist row herewith (orchestrator-only append). Plan block: "
        "session-101-plan-w8.md SW8b-1."
    ),
    "S101-HK-SUFFIX-DISCIPLINE": (
        "S101 W8b-2 — METHODOLOGY-class register-citation rule: channel-scope "
        "suffix discipline lands directive-only in the regulator-pin-discipline.md "
        "genre; K=1 calibration instance (S100a W-4 five-surface census) routes to "
        "the corpus. M1 artifact-existence; M2 Edit + corpus append-helper; "
        "M3 VERBATIM transcription of the FINAL drafted directive at "
        "session-100a-housekeeping.md:114 (strongest M3 form); M4 herewith. "
        "Status SUGGESTION K=1. Plan block: session-101-plan-w8.md SW8b-2."
    ),
    "S101-COMPOSITE-PRECEDENCE-RULE-EXTENSION": (
        "S101 W8b-3 — METHODOLOGY-class gate-verdicts.md clarification: a "
        "plan-frozen gate-block operator takes precedence over the generic "
        "schema-v2 composite-collapse rule on conflict (mandatory pre-declared "
        "disclosure extra-row); closes the applicability-GUARD gap. Calibration "
        "instance = S100b W4-1 (PASS, PASS, MARGINAL) -> plan-frozen INFO "
        "(verdict line 56, audit 273a0dc4...), routed to the corpus. "
        "M1 artifact-existence; M2 Edit + corpus append-helper; M3 verbatim "
        "assembly of housekeeping-100b SD CF-W4-2 + closeout SV.14; M4 herewith. "
        "Plan block: session-101-plan-w8.md SW8b-3."
    ),
}


def main() -> int:
    with io.open(PLAN, "r", encoding="utf-8") as fh:
        lines = fh.readlines()

    # All top-level '## ' header line indices (0-based).
    header_idx = [i for i, ln in enumerate(lines) if ln.startswith("## ")]

    rows = []
    for gate_id, header_prefix in GATES:
        starts = [i for i in header_idx if lines[i].startswith(header_prefix)]
        if len(starts) != 1:
            print(f"FATAL: header {header_prefix} matched {len(starts)} times")
            return 1
        start = starts[0]
        later = [i for i in header_idx if i > start]
        end = later[0] if later else len(lines)  # exclusive
        block = "".join(lines[start:end])
        sha = hashlib.sha256(block.encode("utf-8")).hexdigest()
        rows.append((gate_id, sha, start + 1, end))  # 1-based inclusive-exclusive
        print(f"{gate_id}: lines {start + 1}-{end} sha256={sha}")

    # Ledger rows (3-column ONLY).
    with io.open(LEDGER, "a", encoding="utf-8", newline="\n") as fh:
        for gate_id, sha, _, _ in rows:
            fh.write(f"| {gate_id} | S101 | {sha} |\n")
    print(f"APPENDED {len(rows)} rows -> {LEDGER}")

    # Paired rationale entries.
    with io.open(INSTANCES, "a", encoding="utf-8", newline="\n") as fh:
        for gate_id, sha, start, end in rows:
            fh.write(f"\n### {gate_id} (S101) — {sha[:16]}\n\n")
            fh.write(f"**Full plan-block SHA**: `{sha}`\n")
            fh.write(
                f"**Plan-file block range**: lines {start}-{end - 1} of "
                f"`sessions/session-plan/session-101-plan-w8.md` (from the "
                f"`## §W8b-` header through the line preceding the next `## ` "
                f"header; raw UTF-8 bytes, plain `hashlib.sha256`)\n"
            )
            fh.write("**Landing date**: 2026-06-07 (S101 plan-freeze)\n\n")
            fh.write(RATIONALE[gate_id] + "\n")
    print(f"APPENDED {len(rows)} rationale entries -> {INSTANCES}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
