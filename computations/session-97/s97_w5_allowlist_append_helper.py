"""S97 W5-1 METHODOLOGY-class allowlist append helper (orchestrator-only).

Appends the `S97-DK-DF-STAGE2` COMPONENT-A registry-landing row to
methodology-wave-allowlist-ledger.md + the paired rationale to
methodology-wave-instances.md, per .claude/rules/methodology-wave-allowlist.md
§"Edit discipline" (3-column ledger row; parallel rationale entry; atomic
O_APPEND single-shot writes). Classification CONFIRMED METHODOLOGY-class by
the W5 plan §M1-M4 table (lines 321-326).

sha256_of_plan_block = SHA-256 over the §W5-1 plan-file gate block text
(from the `## §W5-1.` header to just before `## §W5-2.`).
"""
import hashlib
from pathlib import Path

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
PLAN = ROOT / "sessions" / "session-plan" / "session-97-plan-w5.md"
LEDGER = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-allowlist-ledger.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

GATE_ID = "S97-DK-DF-STAGE2"
SESSION = "S97"

# --- extract the §W5-1 gate block (header-delimited, not hardcoded lines) ---
text = PLAN.read_text(encoding="utf-8")
lines = text.splitlines(keepends=True)
start = next(i for i, l in enumerate(lines) if l.startswith("## §W5-1."))
end = next(i for i, l in enumerate(lines) if i > start and l.startswith("## §W5-2."))
block = "".join(lines[start:end])
sha = hashlib.sha256(block.encode("utf-8")).hexdigest()
print(f"§W5-1 block: lines {start+1}-{end} ({len(block)} bytes)")
print(f"sha256_of_plan_block = {sha}")

# --- idempotency guard: do not double-append ---
ledger_text = LEDGER.read_text(encoding="utf-8")
if GATE_ID in ledger_text:
    print(f"GUARD: {GATE_ID} already in ledger — no append (idempotent).")
else:
    row = f"| {GATE_ID} | {SESSION} | {sha} |\n"
    with open(LEDGER, "a", encoding="utf-8") as f:   # atomic O_APPEND
        f.write(row)
    print(f"APPENDED ledger row: {row.strip()}")

inst_text = INSTANCES.read_text(encoding="utf-8")
if GATE_ID in inst_text:
    print(f"GUARD: {GATE_ID} already in instances — no append (idempotent).")
else:
    rationale = (
        f"\n### {GATE_ID} ({SESSION}) — {sha}\n\n"
        "S97 W5-1 COMPONENT-A — METHODOLOGY-class registry-landing of the §VII.BH "
        "STAGE-1-CANDIDATE D_K≅D_F controlled-recovery theorem (verbatim from the "
        "closed W8-4 gate). M1 artifact-existence-with-content (§VII.BH entry exists "
        "with all required fields: clauses, joint-clause flags, author attribution, "
        "closure SHA pin); M2 registry Edit/Write on permanent-results-registry.md; "
        "M3 verbatim controlled-recovery theorem from the closed W8-4 gate (no new "
        "derivation); M4 herewith. The gate's COMPONENT B (Stage-2 two-agent cross-axis "
        "PASS-AND verify, connes + volovik) is COMPUTE-class and needs no allowlist row; "
        "the MIXED gate shares one gate-ID + one composite verdict line (Stage-2 PASS-AND "
        "outcome, with the landing as precondition).\n"
    )
    with open(INSTANCES, "a", encoding="utf-8") as f:   # atomic O_APPEND
        f.write(rationale)
    print(f"APPENDED instances rationale for {GATE_ID}.")
