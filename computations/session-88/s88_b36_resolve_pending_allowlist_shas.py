"""S88 B.36 — Resolve `pending` SHAs in methodology-wave-allowlist.md.

Computes sha256_of_plan_block for each named pending row by extracting the
plan-block via the canonical extractor (mirrors
`s88_w12_147_methodology_t1_21_extension.py:71-93`), then atomically updates
the allowlist `pending` token in-place via Edit-tool-equivalent replacement.

Pending rows (from current allowlist state):
  W0a-1, W0a-3, W0a-5  → sessions/session-plan/archive/session-86-plan-w0a.md
  W0a-2b               → STAYS pending (sub-wave decomposition; no plan-block)
  W2-6, W2-8, W2-9, W2-10, W2-11, W2-12  → sessions/session-plan/session-88-plan-w2.md
  W8-92                → sessions/session-plan/session-88-plan-w8.md
  W9-ALLOWLIST-LIFT-OUT → STAYS pending (structurally undefined per ledger)

Total: 10 computable; 2 stay pending under the rule's one-time exception clause.

Provenance: S88 B.36 ledger entry (`sessions/archive/session-88/s88-pending-edits-ledger.md`
line 363-366). Phase 1.2 of dependency-aware execution order.
"""
from __future__ import annotations

import hashlib
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
ALLOWLIST = REPO / ".claude" / "rules" / "methodology-wave-allowlist.md"

PLAN_S86_W0A = REPO / "sessions" / "session-plan" / "archive" / "session-86-plan-w0a.md"
PLAN_S88_W2 = REPO / "sessions" / "session-plan" / "session-88-plan-w2.md"
PLAN_S88_W8 = REPO / "sessions" / "session-plan" / "session-88-plan-w8.md"


def compute_plan_block_sha(plan_path: Path, section_substr: str) -> tuple[str, int, int]:
    """Extract plan-block matching section_substr in a `## ` header line; compute SHA over the block.

    Block extends from header line through (but not including) the next `## ` or `---` separator.
    Mirrors compute_plan_block_sha from s88_w12_147_methodology_t1_21_extension.py:71-93.
    """
    text = plan_path.read_text(encoding="utf-8")
    lines = text.splitlines()
    start = None  # (local) header line index
    end = None  # (local) boundary line index
    for i, line in enumerate(lines):
        if start is None and section_substr in line and line.startswith("## "):
            start = i
            continue
        if start is not None and i > start and (line.startswith("## ") or line.startswith("---")):
            end = i
            break
    if start is None:
        raise RuntimeError(f"Section substring {section_substr!r} not found in {plan_path.name}")
    if end is None:
        end = len(lines)  # (local) EOF fallback
    block = "\n".join(lines[start:end])
    sha = hashlib.sha256(block.encode("utf-8")).hexdigest()
    return sha, start + 1, end + 1  # 1-indexed for human-readable reporting


# Gate-ID → (plan_path, section_substring) map
PENDING_TARGETS = [
    ("W0a-1", PLAN_S86_W0A, "§W0a-1."),
    ("W0a-3", PLAN_S86_W0A, "§W0a-3."),
    ("W0a-5", PLAN_S86_W0A, "§W0a-5."),
    ("W2-6", PLAN_S88_W2, "§W2-6."),
    ("W2-8", PLAN_S88_W2, "§W2-8."),
    ("W2-9", PLAN_S88_W2, "§W2-9."),
    ("W2-10", PLAN_S88_W2, "§W2-10."),
    ("W2-11", PLAN_S88_W2, "§W2-11."),
    ("W2-12", PLAN_S88_W2, "§W2-12."),
    ("W8-92", PLAN_S88_W8, "§W8-92 "),  # em-dash header, space anchor
]


def main() -> int:
    print("=" * 72)
    print("S88 B.36 — Pending SHA resolution for methodology-wave-allowlist.md")
    print("=" * 72)

    # Step 1: compute SHA for each pending gate
    computed = []  # (local) list of (gate_id, sha, lines_span)
    for gate_id, plan_path, section_substr in PENDING_TARGETS:
        try:
            sha, start_line, end_line = compute_plan_block_sha(plan_path, section_substr)
            computed.append((gate_id, sha, start_line, end_line, plan_path.name))
            print(f"[OK] {gate_id:8s} sha={sha}  (lines {start_line}-{end_line} of {plan_path.name})")
        except RuntimeError as e:
            print(f"[FAIL] {gate_id}: {e}")
            return 1

    # Step 2: update allowlist in-place — replace `| {gate_id} | {session} | pending |`
    # with `| {gate_id} | {session} | {sha} |` for each computed row.
    print()
    print("=" * 72)
    print("STEP 2: updating allowlist rows")
    print("=" * 72)

    allowlist_text = ALLOWLIST.read_text(encoding="utf-8")
    n_replaced = 0  # (local) replacement counter

    for gate_id, sha, start_line, end_line, plan_name in computed:
        # Determine session — W0a* are S86; W2-* and W8-* are S88
        if gate_id.startswith("W0a"):
            session = "S86"  # (local)
        else:
            session = "S88"  # (local)
        # Build padded row patterns: allowlist uses width-padded gate_id field.
        # Match permissively: any whitespace-padded form of `| W0a-1 | S86 | pending |`.
        # Use literal substring replace on the canonical patterns observed in the file.
        old_patterns = [
            f"| {gate_id}   | {session} | pending |",
            f"| {gate_id}  | {session} | pending |",
            f"| {gate_id} | {session} | pending |",
            f"| {gate_id}    | {session} | pending |",
            f"| {gate_id}     | {session} | pending |",
        ]
        replaced = False  # (local)
        for pat in old_patterns:
            if pat in allowlist_text:
                # Preserve column alignment: rebuild row with same gate_id padding
                new_row = pat.replace("pending", sha)
                allowlist_text = allowlist_text.replace(pat, new_row, 1)
                print(f"[OK] {gate_id:8s} replaced (pattern width={len(pat) - len(gate_id) - len(session) - len('pending')})")
                replaced = True
                n_replaced += 1
                break
        if not replaced:
            print(f"[WARN] {gate_id} pending row not found with standard padding patterns")

    # Step 3: write atomically (single open with mode='w', no fsync needed for markdown)
    ALLOWLIST.write_text(allowlist_text, encoding="utf-8")
    print()
    print(f"Wrote allowlist: {n_replaced} of {len(computed)} pending rows replaced")
    print()

    # Step 4: confirm post-write state
    post = ALLOWLIST.read_text(encoding="utf-8")
    for gate_id, sha, _, _, _ in computed:
        if sha in post:
            print(f"[VERIFIED] {gate_id} SHA present: {sha[:16]}...")
        else:
            print(f"[NOT VERIFIED] {gate_id}: SHA not in post-write file")
    print()
    print(f"Note: W0a-2b and W9-ALLOWLIST-LIFT-OUT remain `pending` per the rule's")
    print(f"      one-time exception clause (no plan-block exists for either).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
