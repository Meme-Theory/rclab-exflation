#!/usr/bin/env python3
"""
Classify theorem-registry rows with section-aware 4-tuple tags.

Reads `sessions/permanent-results-registry.md` section by section.
Each section has a canonical (scheme, convention) pair based on its
heading. The value comes from the row's Precision column; L_max from
the row description or defaults.

Unlike the earlier placeholder retrofit, this script uses actual
section context to produce 4-tuples that reflect the physics class:

- Section I. Publishable Standalone Mathematics →
    (scheme=STRUCTURAL-THEOREM, convention=publishable-math)
- Section II. Machine-Epsilon Verified Infrastructure →
    (scheme=NUMERICAL-VERIFICATION, convention=machine-epsilon)
- Section III. Four Curvature Invariants →
    (scheme=CURVATURE-INVARIANT, convention=exact-analytic)
- Section IV. Structural Walls →
    (scheme=CONSTRAINT-WALL, convention=solution-space-boundary)
- Section V. Closed Mechanisms →
    (scheme=CLOSURE-DECLARATION, convention=constraint-eliminated)
- Section VI. Gate Verdicts →
    (scheme=GATE-VERDICT, convention=pre-registered-threshold)
- Section VII. Structural Identities & Constants →
    (scheme=STRUCTURAL-IDENTITY, convention=exact-algebraic)
- Section VIII. Selection Rules →
    (scheme=SELECTION-RULE, convention=representation-theoretic)

The value is populated from the row's precision column when present;
otherwise from the row description.

Appended tag format:
  `(value=<precision>, scheme=<section-class>, convention=<section-conv>, L_max=<from-desc-or-NA>)`

Gate: S81-REGISTRY-CLASSIFY (NON-PHONONIC).

Usage:
    python _classify_registry_4tuples.py --dry
    python _classify_registry_4tuples.py
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_MD = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

RE_FOUR_TUPLE = re.compile(
    r"\(\s*value\s*=.*?,\s*scheme\s*=.*?,\s*convention\s*=.*?,\s*L_max\s*=",
    re.IGNORECASE,
)
RE_FOUR_TUPLE_LITERAL = re.compile(r"4-tuple", re.IGNORECASE)
RE_HEADER_SEP = re.compile(r"^\|[\s:\-|]+\|?\s*$")
RE_H2 = re.compile(r"^##\s+(?P<n>[IVX]+)\.\s+(?P<title>.+?)\s*$")

# Map roman-numeral section number → (scheme, convention)
SECTION_CLASS: dict[str, tuple[str, str]] = {
    "I":    ("STRUCTURAL-THEOREM",    "publishable-math"),
    "II":   ("NUMERICAL-VERIFICATION", "machine-epsilon"),
    "III":  ("CURVATURE-INVARIANT",   "exact-analytic"),
    "IV":   ("CONSTRAINT-WALL",       "solution-space-boundary"),
    "V":    ("CLOSURE-DECLARATION",   "constraint-eliminated"),
    "VI":   ("GATE-VERDICT",          "pre-registered-threshold"),
    "VII":  ("STRUCTURAL-IDENTITY",   "exact-algebraic"),
    "VIII": ("SELECTION-RULE",        "representation-theoretic"),
    "IX":   ("TRAJECTORY-POINT",      "effort-based-probability"),
    "X":    ("CORRECTION",            "retraction-record"),
    "XI":   ("META-STATISTIC",        "session-productivity"),
    "XII":  ("INDEX-GAP",             "knowledge-completeness"),
    "XIII": ("CHAIN-STATUS",          "mechanism-chain-position"),
    "XIV":  ("OBSERVATIONAL-SCORE",   "data-comparison"),
}
DEFAULT_CLASS = ("REGISTRY-ROW", "section-unclassified")

# Extract L_max hint from description/precision. Look for "L_max=N",
# "max_pq_sum=N", "machine epsilon" -> "NA", etc.
RE_LMAX_HINT = re.compile(
    r"L_max\s*=\s*(\d+)|max_pq(?:_sum)?\s*=\s*(\d+)"
)


def _extract_lmax(description: str, precision: str) -> str:
    for src in (precision, description):
        if not src:
            continue
        m = RE_LMAX_HINT.search(src)
        if m:
            return m.group(1) or m.group(2)
    return "NA"


def _clean_precision(p: str) -> str:
    """Normalize precision value for use as `value=...`."""
    if not p or p.strip() in ("—", "-", ""):
        return "structural"
    # Strip markdown emphasis and collapse spaces
    p = re.sub(r"[*`]", "", p).strip()
    # Long precision strings: truncate to first 40 chars
    if len(p) > 40:
        p = p[:40] + "..."
    # Replace commas and spaces with underscores for single-token value
    p = re.sub(r"[,\s]+", "_", p)
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true")
    args = ap.parse_args()

    if not REGISTRY_MD.exists():
        print(f"ERROR: {REGISTRY_MD} missing.")
        return 2

    text = REGISTRY_MD.read_text(encoding="utf-8")
    lines = text.splitlines()

    current_section = None
    in_table = False
    header_passed = False
    seen = 0  # (local) data rows scanned
    tagged = 0  # (local) retrofitted
    skipped_already = 0  # (local)

    out: list[str] = []
    for raw in lines:
        stripped = raw.strip()
        # Track section
        m_h2 = RE_H2.match(stripped)
        if m_h2:
            current_section = m_h2.group("n")
            out.append(raw)
            continue
        if not stripped:
            in_table = False
            header_passed = False
            out.append(raw)
            continue
        if stripped.startswith("|"):
            if RE_HEADER_SEP.match(stripped):
                header_passed = True
                in_table = True
                out.append(raw)
                continue
            if not in_table:
                in_table = True
                header_passed = False
                out.append(raw)
                continue
            if not header_passed:
                out.append(raw)
                continue
            # Data row
            seen += 1
            if RE_FOUR_TUPLE.search(raw) or RE_FOUR_TUPLE_LITERAL.search(raw):
                skipped_already += 1
                out.append(raw)
                continue
            cells = [c.strip() for c in raw.split("|")]
            # cells[0] is '' (pre-first-pipe), cells[1]..cells[-2] are data,
            # cells[-1] is '' (post-last-pipe).
            # Number of data cells = len(cells) - 2 (variable by section).
            if len(cells) < 3:
                out.append(raw)
                continue
            data_cells = cells[1:-1]  # actual data columns
            description = data_cells[1] if len(data_cells) > 1 else ""
            # Precision is column 3 in the 5-col `# | Result | Session | Precision | Target` format,
            # column 2 in the 4-col `# | Theorem | Statement | Source` format.
            # Heuristic: last column = target/source; second-to-last = precision/statement.
            precision = (
                data_cells[-2] if len(data_cells) >= 3 else (
                    data_cells[-1] if data_cells else ""
                )
            )
            scheme, convention = SECTION_CLASS.get(
                current_section or "", DEFAULT_CLASS)
            lmax = _extract_lmax(description, precision)
            value = _clean_precision(precision)
            tag = (
                f"(value={value}, scheme={scheme}, "
                f"convention={convention}, L_max={lmax})"
            )
            # Append to the LAST data cell (cells[-2] in split form).
            cells[-2] = (cells[-2] + " " + tag).strip()
            new = "| " + " | ".join(data_cells[:-1] + [cells[-2]]) + " |"
            out.append(new)
            tagged += 1
        else:
            in_table = False
            header_passed = False
            out.append(raw)

    print(f"Registry rows scanned: {seen}")
    print(f"  already 4-tuple tagged: {skipped_already}")
    print(f"  retrofitted this run:   {tagged}")

    if args.dry:
        print("(dry run: no changes written)")
        return 0

    if tagged > 0:
        REGISTRY_MD.write_text("\n".join(out) + "\n", encoding="utf-8")
        print(f"Wrote {REGISTRY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
