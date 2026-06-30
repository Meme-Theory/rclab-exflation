"""S92 W6 — orchestrator-direct allowlist append helper for §W6-1/§W6-2/§W6-4/§W6-6.

Computes sha256_of_plan_block over each gate's plan-file block (extracted by ##-section
header range) and appends 3-column rows per `methodology-wave-allowlist.md §"Schema"`
to `sessions/framework/registry/methodology-wave-allowlist-ledger.md`.

Per `methodology-wave-allowlist.md §"Edit discipline"` item 2: orchestrator-only edit;
subagents denied. This script is dispatched orchestrator-direct per the closure pattern
at `.claude/skills/rclab-coordinate/SKILL.md §"Effected In-Session"`.

Section boundaries verified against `sessions/session-plan/session-92-plan-w6.md`:
  §W6-1 starts at line 34;  §W6-2 starts at line 673 (i.e., §W6-1 = lines 34..672 inclusive)
  §W6-2 starts at line 673; §W6-3 starts at line 1121 (i.e., §W6-2 = lines 673..1120)
  §W6-4 starts at line 1760; §W6-5 starts at line 2509 (i.e., §W6-4 = lines 1760..2508)
  §W6-6 starts at line 3072; EOF or next section (§W6-6 = lines 3072..3825 per WP §"Plan reference")

Idempotency: skip append if (gate_id, session) row already present in ledger.
"""
from pathlib import Path
import hashlib
import sys

# Required by computations/_shared/CLAUDE.md (S34+ scripts MUST import canonical_constants).
# This script does not use framework constants (pure infrastructure: path manipulation + SHA),
# but the import satisfies the policy. The `_canonical_constants_imported` flag is # (local).
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403  (required by policy, unused here)
_canonical_constants_imported = True  # (local)

ROOT = Path(r"C:\sandbox\Ainulindale Exflation")
PLAN = ROOT / "sessions" / "session-plan" / "session-92-plan-w6.md"
LEDGER = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-allowlist-ledger.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

# Section boundaries (1-indexed line numbers; inclusive start, exclusive end)
SECTIONS = {
    "W6-1": (34, 673),
    "W6-2": (673, 1121),
    "W6-4": (1760, 2509),
    "W6-6": (3072, 3826),  # 3826 = past last line of file (EOF clamp)
}

INSTANCE_RATIONALE = {
    "W6-1": (
        "S92-W6-CF-W2-1-S91-W2-PASS-V-VII-AX-NEW-SLOT-MULTI-PIN-ATLAS-LANDING — "
        "METHODOLOGY-class registry-text landing of NEW §VII.AX.MULTI-PIN-ATLAS sub-slot "
        "as STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway. "
        "M1 PASS: artifact-existence-with-substantive-content (95 substantive lines + "
        "13-of-13 sub-blocks bit-exact content_sha256 match against pre-composed text; "
        "audit_sha256=`a006b8092e33e680c445676041d3fe38bc7cd46d8dab9e9a99e0d9904ff8b727`). "
        "M2 PASS: Edit on `sessions/permanent-results-registry.md` via atomic POSIX "
        "tmp+replace; sha256sum cross-check; canonical `append_registry_section()` helper. "
        "M3 PASS: verbatim sourcing from S91 §W2-1 PASS-V verdict (audit_sha256="
        "`58671312b0aee2e749836b8902273ab135073992736ddcc8f3362be2328dea14`) + §VII.AX "
        "mother slot pre-registration at registry line 18683 (S91 W0 R5) + S90 W-2 EV1 "
        "D1-Reading-B admission of option (v). M4 PASS: allowlist append herewith. "
        "Author: mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`."
    ),
    "W6-2": (
        "S92-W6-CF-W2-2-S91-W2-K-COUNTER-K2-ADVANCEMENT-REGULATOR-CLASS-PLURALISM — "
        "METHODOLOGY-class corpus-row landing of THREE K=2 corpus rows at "
        "`cross-pillar-bridge-corpus.md` §3 (Hybrid Independence Test) + §10 (Element 3 "
        "fiducial-anchor binding / Bridge-map-scheme suffix) + §17 (Within-cell "
        "discriminator axes; corrected from plan's §15 reference per runtime drift). "
        "M1 PASS: artifact-existence on three K=2 corpus rows (gen-physicist primary "
        "audit_sha256=`266f3bdd6ad2216969d99ef92e24b3c90f420f9178b3b0ea0630755babe2b742`) "
        "+ K-counter audit sub-section (connes co-author audit_sha256="
        "`fe3910552ca448667e8cb412821339ba852e4f36a1f9abe3b094570dd802edcf`). "
        "M2 PASS: atomic POSIX O_APPEND `atomic_append()` for corpus rows + Edit on WP. "
        "M3 PASS: verbatim K=2 instances derived from §W6-1 §VII.AX.MULTI-PIN-ATLAS "
        "landing; K_HIT 1→2; K_E3 1→2; K_WCD 1→2 (status SUGGESTION preserved at K=2). "
        "M4 PASS: allowlist append herewith. Composite (gen-physicist primary ∧ connes "
        "K-counter audit) = PASS. Author: gen-physicist + connes-ncg-theorist CO-AUTHOR."
    ),
    "W6-4": (
        "S92-W6-CF-S92-W5-4-VII-AX-STATE-PROJ-COMPANION-LANDING — METHODOLOGY-class "
        "registry-text edit landing the algebra-axis-orthogonal-companion to "
        "§VII.AX.OP-PROJ. CLOSED via mechanical-closure-discipline.md (`PRE-REG-INC` "
        "blocked by §W6-3 PASS-AND impossible per Axis-A E2 FAIL ∧ Axis-B JE5 FAIL); "
        "audit_sha256=`ac13c378cbba8061981da89c8abb90d40df94f8b12ea8afd68ad027bf73ae904`. "
        "M1 PASS: artifact-existence-with-substantive-content on closure-narrative WP "
        "section (50 lines) + verdict line on disk + per-gate-distinct audit_sha. "
        "M2 PASS: Edit on WP + atomic POSIX O_APPEND via canonical closure script "
        "`s92_w6_pre_reg_inc_closure.py`. M3 PASS: closure scenario PRE-REGISTERED at "
        "plan §\"Wave 6 Decision Point Prerequisites\" line 32; verbatim sourcing from "
        "§W6-3 Axis-A + Axis-B FAIL verdicts on disk. M4 PASS: allowlist append herewith. "
        "Author: mack-cosmic-bridge sole-writer (closure script covers §W6-4/§W6-5/§W6-6 "
        "with per-gate-distinct audit_sha256 in single producing script)."
    ),
    "W6-6": (
        "S92-W6-CF-S92-W5-4-CANONICAL-CONSTANTS-PROMOTION-N-PBH-FW-PENDING-STAGE-3 — "
        "METHODOLOGY-class orchestrator-direct write to `canonical_constants.py` per "
        "`math-scripts.md §\"Canonical Write-Order\"` Step 2. CLOSED via mechanical-"
        "closure-discipline.md (`PRE-REG-INC` blocked by §W6-3 PASS-AND impossible); "
        "audit_sha256=`c87ed3e304146cc289e18b17dcbc7be2de1b36682c81c396fb51de69951160ce`. "
        "M1 PASS: artifact-existence-with-substantive-content on closure-narrative WP "
        "section (54 lines) + verdict line on disk + per-gate-distinct audit_sha. "
        "M2 PASS: Edit on WP + atomic POSIX O_APPEND via same closure script as §W6-4. "
        "M3 PASS: closure scenario PRE-REGISTERED at plan line 32; Step 1 (verdict-file "
        "emission) already discharged at S91 W5-4 line 106; Step 2 (canonical_constants "
        "promotion) HALTED at prereq-block; Step 3 (mack inventory row) already discharged "
        "at S91 W5-4. M4 PASS: allowlist append herewith. Author: mack-cosmic-bridge "
        "(via closure script) — original plan-assigned to orchestrator-direct, executed "
        "as mechanical closure on prereq-block."
    ),
}


def extract_section(lines: list, start: int, end: int) -> str:
    """Return the joined plan-file block for the section (inclusive start, exclusive end)."""
    # lines is 0-indexed list; convert from 1-indexed plan line numbers
    return "".join(lines[start - 1:end - 1])


def sha256_hex(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> int:
    plan_text = PLAN.read_text(encoding="utf-8")
    lines = plan_text.splitlines(keepends=True)

    print(f"Plan file: {PLAN}")
    print(f"  Total lines: {len(lines)}")

    ledger_text = LEDGER.read_text(encoding="utf-8")
    instances_text = INSTANCES.read_text(encoding="utf-8") if INSTANCES.exists() else ""

    appends_ledger = []
    appends_instances = []
    SESSION = "S92"

    for gate_id_short, (start, end) in SECTIONS.items():
        # Idempotency check: if (gate_id, session) row exists, skip
        idempotency_key = f"| {gate_id_short:<7} | {SESSION}"
        if idempotency_key in ledger_text:
            print(f"  SKIP {gate_id_short} {SESSION}: idempotency key present in ledger")
            continue

        block = extract_section(lines, start, min(end, len(lines) + 1))
        sha = sha256_hex(block)

        # Ledger row (3-column form per S92-RULE-SPLIT)
        # Format matches existing rows in the ledger (gate_id padded to 7 chars).
        row = f"| {gate_id_short:<7} | {SESSION}     | {sha} |\n"
        appends_ledger.append(row)
        print(f"  APPEND {gate_id_short} {SESSION}: sha={sha[:16]}... block_lines={end - start} ({len(block)} bytes)")

        # Instances row (rationale prose; companion file)
        instance_anchor = f"### {gate_id_short} ({SESSION}) — {sha[:16]}"
        instance_body = (
            f"\n{instance_anchor}\n\n"
            f"**Full plan-block SHA**: `{sha}`\n"
            f"**Plan-file block range**: lines {start}-{end - 1} of `sessions/session-plan/session-92-plan-w6.md`\n"
            f"**Landing date**: 2026-05-23\n\n"
            f"{INSTANCE_RATIONALE[gate_id_short]}\n"
        )
        appends_instances.append(instance_body)

    if not appends_ledger:
        print("No new rows to append (all four gate-ids already in ledger).")
        return 0

    # Atomic POSIX O_APPEND on ledger (single write per file)
    with LEDGER.open("a", encoding="utf-8") as f:
        for row in appends_ledger:
            f.write(row)
    print(f"Appended {len(appends_ledger)} rows to {LEDGER.name}")

    # Atomic POSIX O_APPEND on instances file (single write per file)
    with INSTANCES.open("a", encoding="utf-8") as f:
        for body in appends_instances:
            f.write(body)
    print(f"Appended {len(appends_instances)} rationale entries to {INSTANCES.name}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
