r"""Scrub `gates` table in tools/knowledge-index.json per user policy 2026-05-19.

Blacklist rules (DELETE the row):
  R1a — id contains parenthetical text   \(.+\)
  R1b — name EXACTLY matches one of 13 listed strings (narrowed from prior
        regex per user direction — broad paren-name match killed valid
        framework gates like fw_gates_17 / "Ω_DM h² (Leggett-only)")
  R2a — id starts with "NO-GO"
  R2b — name starts with "NO-GO"
  R2c — id starts with "STAGE"
  R2d — name starts with "STAGE"
  R3  — name matches /^W\d+:/
  R4a — result starts with "value=MIGRATED"
  R5  — id contains "PASS" or "FAIL"
  R6  — name is exactly "—" (em-dash) or "–" / "-" placeholder

Scrub rule (KEEP the row, edit result column):
  R4b — result starts with "value=" (not MIGRATED) → strip "value=" prefix

Defaults to --dry-run: emits a report without touching the JSON.
Pass --apply to actually modify (writes a timestamped .bak first).

Same safety model as _scrub_equations_prose.py:
  - dry-run default
  - backup before write
  - atomic rename via .tmp
  - idempotent
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "knowledge-index.json"
REPORT_PATH = ROOT / "_scrub_gates_report.json"

# R1a still: any parenthetical with at least one character inside the id.
_PAREN_RE = re.compile(r"\([^()]+\)")
_W_COLON_RE = re.compile(r"^W\d+:")

# R1b: user-supplied exact-name blacklist (2026-05-19). Replaces the broader
# regex that was killing legitimate framework gates like fw_gates_17 / "Ω_DM
# h² (Leggett-only)". Compare with .strip() applied to row name.
EXACT_NAME_BLACKLIST = frozenset({
    "R1 (lizzi FI/RD spectrum-only)",
    "Gate",
    "Wave",
    "PENDING-EVENT",
    "PROVEN",
    "ZERO (structural)",
    "INFO",
    "I (substrate side intact)",
    "III (3HeB-inheritance)",
    "I (if dispatched)",
    "STAGE-3",
    "Berry",
    "Euclidean",
})

# R6: name-only placeholders (em-dash / en-dash / hyphen) indicating the
# extractor lost the gate's real name.
NAME_PLACEHOLDER_BLACKLIST = frozenset({"—", "–", "-"})

VALUE_PREFIX = "value="
VALUE_MIGRATED_PREFIX = "value=MIGRATED"


def classify(row: dict) -> tuple[str | None, str | None]:
    """Return (action, rule) for a row.

    action ∈ {"DELETE", "SCRUB_VALUE_PREFIX", None}
    rule = identifier of which blacklist/scrub rule fired
    """
    gid = (row.get("id") or "").strip()
    name = (row.get("name") or "").strip()
    result = (row.get("result") or "").strip()

    # R1a — parenthetical in id (unchanged)
    if _PAREN_RE.search(gid):
        return ("DELETE", "R1a_paren_in_id")

    # R1b — exact-string match on name (narrowed from regex per user policy)
    if name in EXACT_NAME_BLACKLIST:
        return ("DELETE", "R1b_name_exact_match")

    # R2 — NO-GO or STAGE prefix
    if gid.startswith("NO-GO"):
        return ("DELETE", "R2a_id_NO-GO")
    if name.startswith("NO-GO"):
        return ("DELETE", "R2b_name_NO-GO")
    if gid.startswith("STAGE"):
        return ("DELETE", "R2c_id_STAGE")
    if name.startswith("STAGE"):
        return ("DELETE", "R2d_name_STAGE")

    # R3 — name matches W#:
    if _W_COLON_RE.match(name):
        return ("DELETE", "R3_name_W_colon")

    # R5 — id contains "PASS" or "FAIL" (substring match)
    if "PASS" in gid or "FAIL" in gid:
        return ("DELETE", "R5_id_PASS_or_FAIL")

    # R6 — name is just an em-dash / en-dash / hyphen placeholder
    if name in NAME_PLACEHOLDER_BLACKLIST:
        return ("DELETE", "R6_name_placeholder")

    # R4a — value=MIGRATED result
    if result.startswith(VALUE_MIGRATED_PREFIX):
        return ("DELETE", "R4a_value_MIGRATED")

    # R4b — other value= prefix → scrub
    if result.startswith(VALUE_PREFIX):
        return ("SCRUB_VALUE_PREFIX", "R4b_value_other")

    return (None, None)


def scrub_row(row: dict) -> tuple[dict | None, str | None]:
    """Apply scrub for a SCRUB_VALUE_PREFIX row. Returns (new_row, rule)."""
    new = dict(row)
    new["result"] = new["result"][len(VALUE_PREFIX):].lstrip()
    return new, "R4b_value_other"


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Actually modify the JSON (default: dry-run)",
    )
    ap.add_argument(
        "--sample-size",
        type=int,
        default=10,
        help="Per-rule sample count in report (default: 10)",
    )
    args = ap.parse_args()

    print(f"Loading {INDEX_PATH} ...")
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        idx = json.load(f)

    gates = idx.get("gates", [])
    print(f"  loaded {len(gates):,} gate rows")

    new_gates: list = []
    rule_counts: dict[str, int] = {}
    rule_samples: dict[str, list[dict]] = {}
    n_deleted = 0
    n_scrubbed = 0
    n_unchanged = 0

    for row in gates:
        if not isinstance(row, dict):
            new_gates.append(row)
            n_unchanged += 1
            continue

        action, rule = classify(row)
        if rule:
            rule_counts[rule] = rule_counts.get(rule, 0) + 1

        if action == "DELETE":
            n_deleted += 1
            sample = {
                "id": row.get("id"),
                "name": row.get("name"),
                "result_head": (row.get("result") or "")[:120],
            }
            rule_samples.setdefault(rule, [])
            if len(rule_samples[rule]) < args.sample_size:
                rule_samples[rule].append(sample)
            # Do NOT add to new_gates → effectively deleted
        elif action == "SCRUB_VALUE_PREFIX":
            n_scrubbed += 1
            new_row, _ = scrub_row(row)
            sample = {
                "id": row.get("id"),
                "result_before": (row.get("result") or "")[:120],
                "result_after": new_row["result"][:120],
            }
            rule_samples.setdefault(rule, [])
            if len(rule_samples[rule]) < args.sample_size:
                rule_samples[rule].append(sample)
            new_gates.append(new_row)
        else:
            n_unchanged += 1
            new_gates.append(row)

    report = {
        "dry_run": not args.apply,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "input_path": str(INDEX_PATH),
        "totals": {
            "input_rows": len(gates),
            "rows_deleted": n_deleted,
            "rows_scrubbed": n_scrubbed,
            "rows_unchanged": n_unchanged,
            "output_rows": len(new_gates),
        },
        "rule_counts": dict(sorted(rule_counts.items(), key=lambda x: -x[1])),
        "rule_samples": rule_samples,
    }

    with REPORT_PATH.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print()
    print("=" * 60)
    print(f"{'DRY-RUN — NO CHANGES WRITTEN' if not args.apply else 'APPLY MODE'}")
    print("=" * 60)
    print(f"Input rows:        {len(gates):>6,}")
    print(f"Rows deleted:      {n_deleted:>6,}")
    print(f"Rows scrubbed:     {n_scrubbed:>6,}  (value= prefix removed)")
    print(f"Rows unchanged:    {n_unchanged:>6,}")
    print(f"Output rows:       {len(new_gates):>6,}")
    print()
    print("Per-rule counts:")
    for r, n in sorted(rule_counts.items(), key=lambda x: -x[1]):
        print(f"  {r:<26} {n:>6,}")

    print(f"\nFull report: {REPORT_PATH}")

    if not args.apply:
        print("\nThis was a DRY RUN — no files were modified.")
        print("Re-run with --apply to actually scrub the gates table.")
        return

    # APPLY
    backup_path = INDEX_PATH.with_suffix(
        f".bak.gates.{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    )
    print(f"\nBacking up index to {backup_path} ...")
    shutil.copy2(INDEX_PATH, backup_path)

    new_idx = dict(idx)
    new_idx["gates"] = new_gates

    tmp_path = INDEX_PATH.with_suffix(".tmp")
    print(f"Writing scrubbed index to temp file {tmp_path} ...")
    with tmp_path.open("w", encoding="utf-8") as f:
        json.dump(new_idx, f, ensure_ascii=False, indent=2)

    print(f"Atomically renaming {tmp_path} -> {INDEX_PATH} ...")
    tmp_path.replace(INDEX_PATH)
    print("Done.")
    print(f"\nBackup retained at: {backup_path}")
    print(f"Regenerate markdown dumps with: python tools/_dump_kb_to_markdown.py")


if __name__ == "__main__":
    main()
