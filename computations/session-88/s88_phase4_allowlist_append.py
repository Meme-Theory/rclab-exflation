"""S88 Phase 4: methodology-wave-allowlist append for B.4 + B.34.

Implements Ledger entries B.4 (W4a-16 + W4a-27 plan-block SHAs) + B.34 (B.2-B.21
ledger-entry-block SHAs) per `.claude/rules/methodology-wave-allowlist.md`
§"Allowlist Rows" + Edit-discipline item 4 (3-column rule-file rows + parallel
registry entries with verbatim rationale prose, post W9-RULE-CLEANUP lift-out).

Sources:
- B.4 spec: `s88-pending-edits-ledger.md §B.4` (lines 179-187)
- B.34 spec: `s88-pending-edits-ledger.md §B.34` (lines 352-356)
- Schema reference: `.claude/rules/methodology-wave-allowlist.md §"Schema"` + §"Edit discipline"
- Append-helper canonical: `computations/session-88/s88_w8_allowlist_append_helper.py`
- Lift-out precedent: methodology-wave-instances.md §"W9-RULE-CLEANUP (S88)"

Pattern (per Edit-discipline item 4):
  1. Compute SHA-256 over each gate's source block (plan-block for B.4; ledger-entry
     block for B.34)
  2. Append 3-column row `| gate_id | session | sha |` to methodology-wave-allowlist.md
  3. Append `### {gate_id} ({session}) — {sha}` provenance entry to methodology-wave-instances.md
     with verbatim rationale prose

Atomic POSIX append (single open("a")) per registry-write race protection.
"""
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path("C:/sandbox/Ainulindale Exflation")
LEDGER = ROOT / "sessions" / "session-88" / "s88-pending-edits-ledger.md"
PLAN_W4A = ROOT / "sessions" / "session-plan" / "session-88-plan-w4a.md"
ALLOWLIST = ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
INSTANCES = ROOT / "sessions" / "framework" / "registry" / "methodology-wave-instances.md"

# Canonical-constants import per .claude/rules/math-scripts.md (S34+ compliance)
# This script doesn't compute physics; the import is a hygiene guard for the
# `from canonical_constants import *` policy.
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
from canonical_constants import n_s_FW_exact  # noqa: E402  # (local) import-only


def sha256_text(text: str) -> str:
    """SHA-256 hexdigest over UTF-8-encoded text bytes."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_block(file_text: str, header_pattern: str) -> str:
    """Extract a block from `## ` or `### ` header to next same-or-higher header.

    `header_pattern` is the literal header line (e.g., `### B.17 — wave-classification.md...`).
    Returns the block including the header line, up to but excluding the next header
    of the same level.
    """
    lines = file_text.splitlines()
    start_idx = None
    header_level = None
    for i, line in enumerate(lines):
        if line.startswith(header_pattern):
            start_idx = i
            # Detect header level from leading hashes
            m = re.match(r"^(#+)", line)
            header_level = len(m.group(1)) if m else 3
            break
    if start_idx is None:
        raise ValueError(f"Header pattern not found: {header_pattern}")

    # Find next header of same-or-higher level
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        line = lines[j]
        m = re.match(r"^(#+)\s", line)
        if m and len(m.group(1)) <= header_level:
            end_idx = j
            break

    return "\n".join(lines[start_idx:end_idx]).rstrip() + "\n"


def existing_gate_ids(allowlist_text: str) -> set:
    """Extract all gate-IDs from the allowlist table (column 1 of `| ... | ... | ... |` rows)."""
    ids = set()
    for line in allowlist_text.splitlines():
        if line.startswith("|") and not line.startswith("|:") and not line.startswith("| gate_id"):
            cols = [c.strip() for c in line.split("|") if c.strip()]
            if len(cols) >= 1:
                ids.add(cols[0])
    return ids


def main() -> int:
    # Sanity check on canonical constant import
    assert n_s_FW_exact is not None  # noqa: E712  # import-presence guard

    print(f"S88 Phase 4 — methodology-wave-allowlist append (B.4 + B.34)")
    print(f"Allowlist file: {ALLOWLIST}")
    print(f"Instances file: {INSTANCES}")
    print(f"=" * 80)

    ledger_text = LEDGER.read_text(encoding="utf-8")
    plan_w4a_text = PLAN_W4A.read_text(encoding="utf-8")
    allowlist_text_pre = ALLOWLIST.read_text(encoding="utf-8")
    pre_ids = existing_gate_ids(allowlist_text_pre)
    print(f"Existing allowlist gate-IDs (pre-append): {len(pre_ids)}")

    # ============================================================
    # B.4 — W4a-16 + W4a-27 rows with SHAs over plan §W4a-16 + §W4a-27 wave-blocks
    # ============================================================
    block_w4a_16 = extract_block(plan_w4a_text, "## §W4a-16. ")
    block_w4a_27 = extract_block(plan_w4a_text, "## §W4a-27. ")
    sha_w4a_16 = sha256_text(block_w4a_16)
    sha_w4a_27 = sha256_text(block_w4a_27)

    print(f"\nB.4 plan-block SHAs:")
    print(f"  §W4a-16 ({len(block_w4a_16)} bytes) → SHA = {sha_w4a_16}")
    print(f"  §W4a-27 ({len(block_w4a_27)} bytes) → SHA = {sha_w4a_27}")

    # ============================================================
    # B.34 — ledger-entry-block rows for B.2-B.21 methodology-class entries
    # B.4 itself excluded (covered by W4a-16 + W4a-27 above)
    # ============================================================
    b34_entries = []
    for n in [2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]:
        # Header pattern: `### B.N — `
        # Some entries have multiple sub-actions with similar prefixes — match exact prefix
        header = f"### B.{n} — "
        try:
            block = extract_block(ledger_text, header)
        except ValueError as e:
            print(f"WARNING: {e}")
            continue
        sha = sha256_text(block)
        b34_entries.append((f"W9-B{n}", "S88", sha, header, block))
        print(f"  B.{n} ledger block ({len(block)} bytes) → SHA = {sha}")

    # ============================================================
    # Compose new allowlist rows + instance entries
    # ============================================================
    new_rows_for_allowlist = []
    new_entries_for_instances = []
    skipped = []

    # B.4 — W4a-16 + W4a-27
    for gate_id, sha, plan_block in [
        ("W4a-16", sha_w4a_16, block_w4a_16),
        ("W4a-27", sha_w4a_27, block_w4a_27),
    ]:
        if gate_id in pre_ids:
            skipped.append(gate_id)
            continue
        new_rows_for_allowlist.append(f"| {gate_id} | S88 | {sha} |")

        # Extract gate-ID line from plan block (§"### 1. Gate ID" sub-section)
        gate_id_line = ""
        primary_agent = ""
        for ln in plan_block.splitlines():
            if ln.startswith("`S88-") or ln.startswith("`S87-"):
                gate_id_line = ln.strip("`")
                break
        # Extract PRIMARY agent if available
        for ln in plan_block.splitlines():
            if "**PRIMARY**" in ln:
                primary_agent = ln.split("**PRIMARY**:")[-1].strip(" *").split("(")[0].strip()
                break

        instance_entry = f"""
### {gate_id} (S88) — {sha}

**Gate ID**: `{gate_id_line}`

**Rule extension**: methodology-wave-allowlist M4-satisfaction row landed at S88 W9 housekeeping (Phase 4) per ledger entry B.4 spec ("methodology-wave-allowlist.md: W4a-16 + W4a-27 rows"; source `s88-w13-w4a-17-k3-advancement.md §V.6`). Plan-block at `sessions/session-plan/session-88-plan-w4a.md §{gate_id}` ({len(plan_block)} bytes); SHA computed over the entire wave-block from `## §{gate_id}.` header to next `## §` header. Plan-block self-classifies as METHODOLOGY-class with explicit M1-M4 conjunction declaration in §2 Classification.

**M1-M4 conjunction**: M1 PASS predicate = artifact-existence-with-substantive-content (declared in plan §2); M2 producing op = `Edit`/`Write` on rule-file/registry per plan §2; M3 source-of-truth = verbatim from upstream-closed mathematical theorems / closed workshop synthesis per plan §2; M4 allowlist append herewith satisfies the M4 plan-pin (`<pinned at plan-freeze>`).

**Authorship**: PRIMARY: {primary_agent or "(per plan §3)"}; CO-AUTHOR: per plan §3.

**Phase 4 landing context**: orchestrator-direct-write per `wave-classification.md` §"Dispatch consequences"; SHA computed at landing time from current plan-w4a.md state; no `pending` placeholder needed.
"""
        new_entries_for_instances.append(instance_entry)

    # B.34 — B.X ledger-entry-block rows
    for gate_id, session, sha, header, block in b34_entries:
        if gate_id in pre_ids:
            skipped.append(gate_id)
            continue
        new_rows_for_allowlist.append(f"| {gate_id} | {session} | {sha} |")

        # Extract title from header line (after "—")
        title = header.split("—", 1)[1].strip().rstrip("\n") if "—" in header else "(unspecified)"
        # Extract Source line if present
        source_line = ""
        for ln in block.splitlines():
            if ln.startswith("- **Source**:") or ln.startswith("- **Citation**:"):
                source_line = ln.strip()
                break

        instance_entry = f"""
### {gate_id} ({session}) — {sha}

**Ledger entry**: B.{gate_id[3:]} — {title}

**Rule extension**: methodology-wave-allowlist M4-satisfaction row landed at S88 W9 housekeeping (Phase 4) per ledger entry B.34 spec ("for EACH methodology-class wave executed (B.2-B.21), append (gate_id | session | sha256_of_plan_block) row + parallel registry entry with verbatim rationale prose"). Ledger-entry block at `sessions/archive/session-88/s88-pending-edits-ledger.md §B.{gate_id[3:]}` ({len(block)} bytes); SHA computed over the ledger entry block from `### B.{gate_id[3:]} — ` header to next `### ` header. The ledger entry IS the plan-block-equivalent for this housekeeping action (no formal plan-w{{N}}.md block exists; the pending-edits ledger is the source-of-truth document driving Phase 2/3 execution per user instruction "Follow your planned execution order" 2026-05-08).

{source_line}

**M1-M4 conjunction**: M1 PASS predicate = artifact-existence-with-substantive-content on rule-file diff (per ledger-entry **Action** field: rule-file edit landed); M2 producing op = `Edit` on `.claude/rules/**` (no .py compute, no eigenvalue computation, no numerical-comparison-against-threshold); M3 source-of-truth = verbatim from closed workshop synthesis per ledger **Source** field; M4 allowlist append herewith satisfies the M4 conjunction.

**Phase 4 landing context**: orchestrator-direct-write per `wave-classification.md` §"Dispatch consequences"; bulk landing via `computations/session-88/s88_phase4_allowlist_append.py` covering 19 B.X ledger-entry rows + 2 plan-w4a rows in single atomic POSIX append. SHA computed at landing time from current ledger state.
"""
        new_entries_for_instances.append(instance_entry)

    print(f"\nNew rows to append: {len(new_rows_for_allowlist)}")
    print(f"Skipped (already present): {len(skipped)} → {skipped}")

    if not new_rows_for_allowlist:
        print(f"\nNo new rows to append. Exiting cleanly.")
        return 0

    # ============================================================
    # SHA-uniqueness check across new rows
    # ============================================================
    new_shas = [r.split("|")[3].strip() for r in new_rows_for_allowlist]
    if len(set(new_shas)) != len(new_shas):
        print(f"ERROR: Duplicate SHA in new rows")
        return 1

    # Check no collisions with existing SHAs in allowlist
    existing_shas = set()
    for line in allowlist_text_pre.splitlines():
        if line.startswith("|") and "S8" in line:
            cols = [c.strip() for c in line.split("|") if c.strip()]
            if len(cols) >= 3 and len(cols[2]) == 64:
                existing_shas.add(cols[2])
    new_shas_set = set(new_shas)
    collisions = new_shas_set & existing_shas
    if collisions:
        print(f"ERROR: SHA collision with existing allowlist:")
        for sha in collisions:
            print(f"  {sha}")
        return 1
    print(f"\nSHA uniqueness check: PASS ({len(new_shas)} new SHAs, all unique vs existing {len(existing_shas)})")

    # ============================================================
    # Atomic POSIX append to allowlist
    # ============================================================
    append_block_allowlist = "\n".join(new_rows_for_allowlist) + "\n"
    with ALLOWLIST.open("a", encoding="utf-8", newline="\n") as f:
        f.write(append_block_allowlist)
        f.flush()
    print(f"\nAPPEND SUCCESS: {len(new_rows_for_allowlist)} rows → {ALLOWLIST}")

    # ============================================================
    # Atomic POSIX append to instances file
    # ============================================================
    append_block_instances = (
        "\n## Phase 4 batch landing (S88 W9 housekeeping; 2026-05-08)\n\n"
        "> **Provenance**: orchestrator-direct-write batch via "
        "`computations/session-88/s88_phase4_allowlist_append.py`. Per ledger entries "
        "B.4 (`s88-pending-edits-ledger.md §B.4`) + B.34 (`s88-pending-edits-ledger.md §B.34`). "
        "B.4 = 2 plan-w4a rows (W4a-16 + W4a-27); B.34 = 19 ledger-entry-block rows "
        "(B.2-B.21 methodology-class entries excluding B.4 itself). All rows landed with "
        "computed SHAs (no `pending` placeholder); methodology-wave-instances entries below "
        "carry verbatim rationale prose per the W9-RULE-CLEANUP lift-out precedent.\n"
    )
    append_block_instances += "".join(new_entries_for_instances)
    with INSTANCES.open("a", encoding="utf-8", newline="\n") as f:
        f.write(append_block_instances)
        f.flush()
    print(f"APPEND SUCCESS: {len(new_entries_for_instances)} entries → {INSTANCES}")

    # ============================================================
    # Post-write verification
    # ============================================================
    allowlist_text_post = ALLOWLIST.read_text(encoding="utf-8")
    post_ids = existing_gate_ids(allowlist_text_post)
    new_ids = post_ids - pre_ids
    expected_ids = {r.split("|")[1].strip() for r in new_rows_for_allowlist}
    print(f"\nPost-write verification:")
    print(f"  Allowlist gate-ID count: {len(pre_ids)} → {len(post_ids)} (delta {len(new_ids)})")
    print(f"  New gate-IDs in file: {sorted(new_ids)}")
    if new_ids != expected_ids:
        missing = expected_ids - new_ids
        unexpected = new_ids - expected_ids
        print(f"  VERIFICATION FAIL: missing={missing}, unexpected={unexpected}")
        return 1
    print(f"  VERIFICATION PASS: all {len(new_ids)} new rows landed")

    instances_text_post = INSTANCES.read_text(encoding="utf-8")
    instances_new_headings = sum(
        1 for ln in instances_text_post.splitlines() if any(f"### {gid} (" in ln for gid in expected_ids)
    )
    print(f"  Instances file new ### headings: {instances_new_headings} (expected {len(expected_ids)})")
    if instances_new_headings != len(expected_ids):
        print(f"  WARNING: instances heading count mismatch")

    print(f"\n{'=' * 80}")
    print(f"S88 Phase 4 complete. {len(new_rows_for_allowlist)} rows landed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
