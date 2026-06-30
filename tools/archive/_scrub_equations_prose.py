"""Scrub prose contamination from `equations[*].raw` in tools/knowledge-index.json.

Policy (per user direction 2026-05-19):
  - type=code rows         → DELETE (covered elsewhere in the KB pipeline)
  - type=comment rows      → SKIP unchanged (comments are descriptive by nature)
  - BRACKET_ANNOT (>=1 word) → strip from raw, append to context
  - CROSS_REF_TAG          → strip from raw, populate `tag` column
  - PROVENANCE_REF         → strip from raw, append to context
  - PAREN_PROSE (>=2 words) → strip from raw, append to context
  - TRAILING_PROSE         → split at sentence verb, append to context

Defaults to --dry-run: emits a report without touching the JSON.
Pass --apply to actually modify the index (writes a timestamped .bak first).

Idempotent: detectors only fire on prose that is still in raw, so running twice
leaves the second run with nothing to do.

Order of detector application:
  1. CROSS_REF_TAG  (anchored at end-of-string; cheap to remove first)
  2. PROVENANCE_REF (file:line / PDG year refs in parens)
  3. BRACKET_ANNOT  ([descriptive content])
  4. PAREN_PROSE    ((multi-word prose))
  5. TRAILING_PROSE (sentence-fragment after the equation)
  6. whitespace normalization (collapse runs of spaces)

Usage:
  python tools/_scrub_equations_prose.py            # dry-run, report only
  python tools/_scrub_equations_prose.py --apply    # backup + scrub + write
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
INDEX_PATH = ROOT / "knowledge-index.json"
REPORT_PATH = ROOT / "_scrub_equations_report.json"

# Reuse detection primitives from the scanner — single source of truth.
sys.path.insert(0, str(ROOT))
from _scan_equations_prose import (  # noqa: E402
    SAFE_LC,
    mask_math,
    _word_tokens_lowercase,
    _CROSS_REF_RE,
    _PROVENANCE_RE,
    _PROVENANCE_NUMERIC_RE,
    _BRACKET_ANNOT_RE,
    _PAREN_RE,
    _TRAILING_PROSE_RE,
)

# ---------------------------------------------------------------------------
# Scrubber — pure-function transforms on a row.
# ---------------------------------------------------------------------------

# Bracket-annot threshold: user direction lowered from >=2 to >=1.
BRACKET_ANNOT_MIN_WORDS = 1

# Paren-prose threshold: kept at >=2 (single-word parentheticals are often
# legitimate math grouping; we are not stripping those).
PAREN_PROSE_MIN_WORDS = 2


def _append_to_context(existing: str, addition: str) -> str:
    """Append `addition` to `existing` with ' | ' separator, dedupe."""
    addition = addition.strip()
    if not addition:
        return existing
    if not existing:
        return addition
    if addition in existing:
        return existing
    return f"{existing} | {addition}"


def _append_to_tag(existing: str, addition: str) -> str:
    """Append a cross-ref tag to the tag column with '; ' separator, dedupe."""
    addition = addition.strip()
    if not addition:
        return existing
    if not existing:
        return addition
    if addition in existing:
        return existing
    return f"{existing}; {addition}"


def scrub_row(row: dict) -> tuple[dict | None, list[tuple[str, str]]]:
    """Scrub a single equation row.

    Returns:
      (new_row, actions) where new_row is the modified dict, or None to delete
      the row, and actions is a list of (action_label, extracted_span) tuples
      for the report.
    """
    actions: list[tuple[str, str]] = []
    type_ = row.get("type", "") or ""

    # Type-based pre-policy
    if type_ == "code":
        actions.append(("DELETE_ROW", "<type=code>"))
        return None, actions
    if type_ == "comment":
        actions.append(("SKIP_ROW", "<type=comment>"))
        return row, actions

    raw = row.get("raw", "") or ""
    if not raw.strip():
        return row, actions

    new_raw = raw
    new_context = row.get("context", "") or ""
    new_tag = row.get("tag", "") or ""

    # ---------------- 1. CROSS_REF_TAG (trailing) ----------------
    while True:
        m = _CROSS_REF_RE.search(new_raw.rstrip())
        if not m:
            break
        span = m.group(0)
        new_tag = _append_to_tag(new_tag, span)
        new_raw = new_raw.rstrip()[:m.start()].rstrip()
        actions.append(("STRIP_CROSS_REF_TAG", span))

    # ---------------- 2. PROVENANCE_REF (any position) ----------------
    # Iterate over matches in reverse so we can strip without reindexing.
    for pattern in (_PROVENANCE_RE, _PROVENANCE_NUMERIC_RE):
        while True:
            ms = list(pattern.finditer(new_raw))
            if not ms:
                break
            m = ms[-1]  # rightmost; strip and reloop
            span = m.group(0)
            new_context = _append_to_context(new_context, span)
            new_raw = new_raw[:m.start()] + new_raw[m.end():]
            actions.append(("STRIP_PROVENANCE_REF", span))

    # ---------------- 3. BRACKET_ANNOT ([descriptive content]) ----------------
    while True:
        masked = mask_math(new_raw)
        ms = list(_BRACKET_ANNOT_RE.finditer(masked))
        if not ms:
            break
        # process rightmost first
        m = ms[-1]
        inner_raw = new_raw[m.start():m.end()]
        words = _word_tokens_lowercase(inner_raw)
        non_safe = [w for w in words if w not in SAFE_LC]
        if len(non_safe) < BRACKET_ANNOT_MIN_WORDS:
            # Not a prose bracket; stop scanning (further-left brackets are
            # not bigger; conservative)
            # Note: we could continue with earlier brackets but this is rare.
            break
        new_context = _append_to_context(new_context, inner_raw)
        new_raw = new_raw[:m.start()] + new_raw[m.end():]
        actions.append(("STRIP_BRACKET_ANNOT", inner_raw))

    # ---------------- 4. PAREN_PROSE ((multi-word prose)) ----------------
    while True:
        masked = mask_math(new_raw)
        ms = list(_PAREN_RE.finditer(masked))
        if not ms:
            break
        stripped_any = False
        for m in reversed(ms):
            inner_masked = m.group(1)
            inner_raw = new_raw[m.start() + 1:m.end() - 1]
            # Skip cross-ref tags (already handled, but might be mid-string)
            if re.fullmatch(r"\s*[A-Z]{1,4}-?\d{1,4}\s*", inner_masked):
                continue
            # Skip provenance refs (already handled)
            if re.search(r"\.[a-z]{2,5}\b|\bPDG\s*\d{4}", inner_raw):
                continue
            words = _word_tokens_lowercase(inner_masked)
            non_safe = [w for w in words if w not in SAFE_LC]
            if len(non_safe) < PAREN_PROSE_MIN_WORDS:
                continue
            span = "(" + inner_raw + ")"
            new_context = _append_to_context(new_context, span)
            new_raw = new_raw[:m.start()] + new_raw[m.end():]
            actions.append(("STRIP_PAREN_PROSE", span))
            stripped_any = True
            break  # restart from scratch since indices shifted
        if not stripped_any:
            break

    # ---------------- 5. TRAILING_PROSE (sentence verb -> end) ----------------
    masked = mask_math(new_raw)
    m = _TRAILING_PROSE_RE.search(masked)
    if m:
        # Split at the matched verb's start. Back up over any whitespace.
        split_idx = m.start()
        while split_idx > 0 and new_raw[split_idx - 1] == " ":
            split_idx -= 1
        prose_tail = new_raw[split_idx:].strip()
        if prose_tail:
            new_context = _append_to_context(new_context, prose_tail)
            new_raw = new_raw[:split_idx].rstrip()
            actions.append(("STRIP_TRAILING_PROSE", prose_tail))

    # ---------------- 6. Whitespace normalization (only if a strip happened) ----------------
    # Rationale: rows with no prose-strip should not be modified just because
    # their raw has multi-space alignment. Whitespace normalization is residue
    # cleanup downstream of a strip, not a standalone operation.
    cleaned = new_raw
    had_strip = any(a[0].startswith("STRIP_") for a in actions)
    if had_strip:
        cleaned = re.sub(r" {2,}", " ", new_raw).strip()
        # Normalize trailing punctuation residue (e.g., `... = a_n ,` after
        # stripping a parenthetical mid-string)
        cleaned = re.sub(r"\s+,", ",", cleaned)
        cleaned = re.sub(r",\s*$", "", cleaned)
        cleaned = cleaned.strip()
        if cleaned != new_raw:
            actions.append((
                "NORMALIZED_WHITESPACE",
                f"len {len(new_raw)}->{len(cleaned)}",
            ))

    # Write back
    row = dict(row)
    row["raw"] = cleaned
    row["context"] = new_context
    row["tag"] = new_tag
    return row, actions


# ---------------------------------------------------------------------------
# Driver.
# ---------------------------------------------------------------------------

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--apply",
        action="store_true",
        help="Actually modify tools/knowledge-index.json (default: dry-run, report only)",
    )
    ap.add_argument(
        "--sample-size",
        type=int,
        default=10,
        help="Per-action samples to include in the report (default: 10)",
    )
    args = ap.parse_args()

    print(f"Loading {INDEX_PATH} ...")
    with INDEX_PATH.open("r", encoding="utf-8") as f:
        idx = json.load(f)

    equations = idx.get("equations", [])
    print(f"  loaded {len(equations):,} equation rows")

    action_counts: dict[str, int] = {}
    action_samples: dict[str, list[dict]] = {}
    new_equations: list[dict] = []
    n_modified = 0
    n_deleted = 0
    n_unchanged = 0

    for row in equations:
        if not isinstance(row, dict):
            new_equations.append(row)
            n_unchanged += 1
            continue

        original_raw = row.get("raw", "") or ""
        new_row, actions = scrub_row(row)

        if new_row is None:
            n_deleted += 1
            for label, span in actions:
                action_counts[label] = action_counts.get(label, 0) + 1
                if label not in action_samples:
                    action_samples[label] = []
                if len(action_samples[label]) < args.sample_size:
                    action_samples[label].append({
                        "id": row.get("id"),
                        "type": row.get("type"),
                        "raw_before": original_raw[:200],
                        "span": span[:200] if isinstance(span, str) else str(span),
                    })
            continue

        # Row kept
        new_equations.append(new_row)
        if actions:
            modified = any(
                a[0] not in {"SKIP_ROW", "NORMALIZED_WHITESPACE"}
                for a in actions
            ) or new_row.get("raw", "") != original_raw
            if modified:
                n_modified += 1
            else:
                n_unchanged += 1
            for label, span in actions:
                action_counts[label] = action_counts.get(label, 0) + 1
                if label not in action_samples:
                    action_samples[label] = []
                if len(action_samples[label]) < args.sample_size:
                    action_samples[label].append({
                        "id": row.get("id"),
                        "type": row.get("type"),
                        "raw_before": original_raw[:200],
                        "raw_after": new_row.get("raw", "")[:200],
                        "span": span[:200] if isinstance(span, str) else str(span),
                    })
        else:
            n_unchanged += 1

    # ---- Report ----
    report = {
        "dry_run": not args.apply,
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "input_path": str(INDEX_PATH),
        "totals": {
            "input_rows": len(equations),
            "rows_modified": n_modified,
            "rows_deleted": n_deleted,
            "rows_unchanged": n_unchanged,
            "output_rows": len(new_equations),
        },
        "action_counts": dict(sorted(action_counts.items(), key=lambda x: -x[1])),
        "action_samples": action_samples,
    }

    with REPORT_PATH.open("w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)

    print("\n" + "=" * 60)
    print(f"{'DRY-RUN — NO CHANGES WRITTEN' if not args.apply else 'APPLY MODE'}")
    print("=" * 60)
    print(f"Input rows:        {len(equations):>8,}")
    print(f"Rows modified:     {n_modified:>8,}")
    print(f"Rows deleted:      {n_deleted:>8,}  (type=code)")
    print(f"Rows unchanged:    {n_unchanged:>8,}")
    print(f"Output rows:       {len(new_equations):>8,}")
    print(f"\nActions performed:")
    for label, n in sorted(action_counts.items(), key=lambda x: -x[1]):
        print(f"  {label:<26} {n:>8,}")

    print(f"\nFull report: {REPORT_PATH}")

    if not args.apply:
        print("\nThis was a DRY RUN — no files were modified.")
        print("Re-run with --apply to actually scrub the index.")
        return

    # ---- APPLY ----
    backup_path = INDEX_PATH.with_suffix(
        f".bak.{datetime.now().strftime('%Y%m%d-%H%M%S')}.json"
    )
    print(f"\nBacking up index to {backup_path} ...")
    shutil.copy2(INDEX_PATH, backup_path)

    # Build new index with replaced equations table
    new_idx = dict(idx)
    new_idx["equations"] = new_equations

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
