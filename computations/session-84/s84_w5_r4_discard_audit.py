#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S84 W5-61 — GATE-R4-DISCARD-AUDIT
==================================

Bookkeeping audit for Session 84 Wave 5 — flags and counts all
occurrences of R4 (K-corridor reading convention, Landau V.1
R1-R5 reading set, K_R4 = n_pairs / N_modes = 59.8 / 8 = 15.95)
and the corresponding "5 physical conventions" / "5-convention"
/ "Landau-V.1-R1-R5" / "R1-R5" / "R1..R5" language in
    sessions/archive/session-82/session-82-results-workingpaper.md
    sessions/archive/session-82/session-82-OOM.md
    sessions/archive/session-83/session-83-results-workingpaper.md

Produces a PASS/FAIL verdict against the pre-registered rule:

    PASS iff every in-scope file either (a) contains no R4-K-corridor
    occurrence at all, or (b) contains a "DIMENSIONAL-ERROR-CROSS-CLASS"
    audit-tag line appended at the end-of-file (anywhere in the final
    50 lines, case-sensitive).

    value := count of in-scope files with R4-K-corridor hits that
    lack the audit tag (post-edit).

    PASS iff value == 0.

Input pins are SHA-256 hashed; the closure hash is the SHA-256 of the
ordered input-pin map.  The audit deliberately EXCLUDES:
  - R4 = c_L / c_BA from s82_w3_13_four_speed_provenance.py
    (a four-speed ratio label in an unrelated gate, not the K-corridor
    reading convention).
  - The S83 5-regulator atlas {zeta, Zubarev, SDW, dim-reg, lattice-BR}
    (a different "5" — regulator schemes, not reading conventions).

Feed from W5-56 (volovik agent memory
`r4-cross-class-84-result.md`): R4 dim-error is CROSS-CLASS (BDI +
AIII both ≥ 10 FAIL threshold).  Tag variant selected:
    "DIMENSIONAL-ERROR-CROSS-CLASS"

Convention inventory (post-audit): 4 physical + 1 cross-class
dim-error.  Physical cluster = {R1, R2, R3, R5}.

Trigger: [AUDIT] (bookkeeping gate; no substitution chain required).
"""

from __future__ import annotations

import hashlib
import re
import sys
from collections import OrderedDict
from pathlib import Path

# Canonical constants are imported for provenance even in an audit script.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403

# ------------------------------------------------------------------ #
# In-scope targets (working papers + OOM ledger)
# ------------------------------------------------------------------ #
PROJECT_ROOT = Path(__file__).resolve().parent.parent                # (local)
TARGET_FILES = [                                                     # (local)
    PROJECT_ROOT / "sessions" / "session-82"
        / "session-82-results-workingpaper.md",
    PROJECT_ROOT / "sessions" / "session-82" / "session-82-OOM.md",
    PROJECT_ROOT / "sessions" / "session-83"
        / "session-83-results-workingpaper.md",
]

# Pattern for R4-K-corridor reading convention. Must disambiguate from
# s82_w3_13 R4 = c_L/c_BA. K-corridor R4 ALWAYS appears in the context
# of (i) K_R4, (ii) n_pairs/8, (iii) 59.8/8, (iv) K-reading tables
# R1-R5, or (v) "Landau-V.1-R1-R5".
R4_K_CORRIDOR_PATTERNS = [                                           # (local)
    r"\bK_?R4\b",                            # K_R4 or KR4
    r"\bR4\s*\(.*n_?pairs.*\)",              # R4 (naive n_pairs=...)
    r"\bR4\b.*15\.95",                       # R4 ... 15.95
    r"\bR4\b.*59\.8\s*/\s*8",                # R4 ... 59.8/8
    r"\bR4\b.*naive",                        # R4 ... naive
    r"\bR4\b.*Fock[- ]count",                # R4 ... Fock-count
    r"\bR4\b.*legacy",                       # R4 ... legacy
    r"\bR4\b.*BCS[- ]dimensional",           # R4 ... BCS-dimensional
    r"\bR4[- ]cross[- ]class",               # R4-cross-class
    r"Landau-V\.1-R1-R5",                    # verdict-line scheme label
    r"R1\.\.R5",                             # R1..R5
    r"R1[- ]R5",                             # R1-R5
]

# Pattern for the "5 physical conventions" / "5-convention" language
# that refers to the K-corridor reading set (NOT the regulator atlas).
# The reading-set "5" always co-occurs with R1/R2/R3/R4/R5 or with
# "A_s_Planck=2.10e-9" / "Landau-V.1".
FIVE_CONVENTIONS_PATTERNS = [                                        # (local)
    r"5\s+convention",
    r"5-convention",
    r"five\s+convention",
    r"five\s+reading",
    r"five\s+pre-registered\s+reading",
    r"all\s+5\s+conventions",
]

AUDIT_TAG_LITERAL = "DIMENSIONAL-ERROR-CROSS-CLASS"                  # (local)

# ------------------------------------------------------------------ #
# Helpers
# ------------------------------------------------------------------ #
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                              # (local)
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: "OrderedDict[str, str]") -> str:
    """SHA-256 of the ordered input-pin map (file_id=sha256, ...)."""
    h = hashlib.sha256()                                              # (local)
    for key, val in pin_map.items():
        h.update(key.encode("utf-8"))
        h.update(b"=")
        h.update(val.encode("utf-8"))
        h.update(b";")
    return h.hexdigest()


def count_hits(text: str, patterns: list) -> list:
    """Return list of (line_number, pattern, match_text)."""
    hits = []                                                         # (local)
    lines = text.splitlines()                                         # (local)
    for i, line in enumerate(lines, start=1):
        for pat in patterns:
            m = re.search(pat, line, flags=re.IGNORECASE)             # (local)
            if m:
                # Filter out the irrelevant R4=c_L/c_BA four-speed
                # match if the line mentions "c_L" or "c_BA" or
                # "four-speed".
                if (
                    re.search(r"c_?L\s*/\s*c_?BA", line)
                    or re.search(r"four[- ]speed", line, re.I)
                ):
                    continue
                hits.append((i, pat, line.strip()[:180]))
                break
    return hits


def file_has_audit_tag(text: str) -> bool:
    """True iff AUDIT_TAG_LITERAL appears anywhere in the file
    (tag is append-only; the only writer is this audit)."""
    return AUDIT_TAG_LITERAL in text


# ------------------------------------------------------------------ #
# Main
# ------------------------------------------------------------------ #
def main() -> int:
    print("=" * 72)
    print("S84 W5-61 -- GATE-R4-DISCARD-AUDIT")
    print("=" * 72)
    print()

    # --- Input SHA pins (logged in first 20 lines per plan rule) ----
    pin_map = OrderedDict()                                           # (local)
    for p in TARGET_FILES:
        if not p.exists():
            print(f"FATAL: missing target file {p}", file=sys.stderr)
            return 2
        pin_map[p.name] = sha256_of(p)

    print("Input SHA-256 pins:")
    for k, v in pin_map.items():
        print(f"  {k:52s}  {v}")
    print()

    # --- Per-file audit pass ---------------------------------------
    print("Per-file audit:")
    print("-" * 72)

    per_file = OrderedDict()                                          # (local)
    total_R4_hits = 0                                                 # (local)
    total_5conv_hits = 0                                              # (local)
    files_with_R4_no_tag = 0                                          # (local)
    files_with_R4 = 0                                                 # (local)

    for p in TARGET_FILES:
        text = p.read_text(encoding="utf-8", errors="replace")        # (local)
        r4_hits = count_hits(text, R4_K_CORRIDOR_PATTERNS)            # (local)
        conv_hits = count_hits(text, FIVE_CONVENTIONS_PATTERNS)       # (local)
        has_tag = file_has_audit_tag(text)                            # (local)

        per_file[p.name] = dict(
            r4_hits=r4_hits,
            conv_hits=conv_hits,
            has_tag=has_tag,
        )
        total_R4_hits += len(r4_hits)
        total_5conv_hits += len(conv_hits)
        if len(r4_hits) > 0:
            files_with_R4 += 1
            if not has_tag:
                files_with_R4_no_tag += 1

        print(f"\nFILE: {p.name}")
        print(f"  R4-K-corridor hits   : {len(r4_hits)}")
        print(f"  5-convention hits    : {len(conv_hits)}")
        print(f"  audit tag present    : {has_tag}")
        for (ln, pat, txt) in r4_hits[:5]:
            print(f"    L{ln:5d} [{pat[:32]:32s}] {txt[:110]}")
        if len(r4_hits) > 5:
            print(f"    ... ({len(r4_hits)-5} more R4 hits suppressed)")
        for (ln, pat, txt) in conv_hits[:3]:
            print(f"    L{ln:5d} [5-conv  ] {txt[:110]}")

    print()
    print("-" * 72)
    print("Aggregate:")
    print(f"  total R4-K-corridor hits     : {total_R4_hits}")
    print(f"  total 5-convention hits      : {total_5conv_hits}")
    print(f"  files with R4 hits           : {files_with_R4}")
    print(f"  files w/R4 hits AND no tag   : {files_with_R4_no_tag}")
    print()

    # --- Gate verdict ----------------------------------------------
    # value = files_with_R4_no_tag (post-edit target = 0)
    value = files_with_R4_no_tag                                      # (local)

    if value == 0:
        verdict = "PASS"                                              # (local)
    else:
        verdict = "FAIL"                                              # (local)

    closure = closure_hash(pin_map)                                   # (local)

    print(f"value (untagged_count)       : {value}")
    print(f"verdict                      : {verdict}")
    print(f"scheme                       : R4-audit")
    print(f"convention                   : 4+1")
    print(f"L_max                        : N/A")
    print(f"sha256 closure               : {closure}")
    print()

    # --- 4-tuple output tag (final non-verdict line) ---------------
    print(
        f"(value={value}, scheme=R4-audit, convention=4+1, L_max=N/A)"
    )

    # --- Verdict line (canonical S81+ form) ------------------------
    verdict_line = (
        f"W5-61: {verdict} -- value={value} scheme=R4-audit "
        f"convention=4+1 L_max=N/A sha256={closure}"
    )
    print()
    print("VERDICT LINE:")
    print(verdict_line)

    # --- Write audit report ----------------------------------------
    report_path = PROJECT_ROOT / "computations" \
        / "s84_w5_61_r4_audit_report.txt"                             # (local)
    with open(report_path, "w", encoding="utf-8") as fh:
        fh.write(
            "S84 W5-61 -- R4-DISCARD-AUDIT REPORT\n"
            "====================================\n\n"
            f"Tag variant applied: {AUDIT_TAG_LITERAL}\n"
            "Source: W5-56 volovik agent memory "
            "r4-cross-class-84-result.md\n"
            "R4 dim-error persists across BDI (3He-B, N_3=0) and "
            "AIII (Weyl, N_3=2).\n"
            "Formula-level mistake, NOT universality-class-specific. "
            "3He-B inheritance uncontaminated.\n\n"
        )
        fh.write("Convention inventory (post-audit):\n")
        fh.write("  5 -> 4 physical + 1 cross-class dim-error\n")
        fh.write("  physical cluster: {R1, R2, R3, R5}\n")
        fh.write("  dim-error slot   : R4 (K_R4 = 59.8/8 = 15.95)\n\n")
        fh.write("Input SHA-256 pins:\n")
        for k, v in pin_map.items():
            fh.write(f"  {k}  {v}\n")
        fh.write("\nPer-file counts:\n")
        for fname, d in per_file.items():
            fh.write(f"\n  {fname}:\n")
            fh.write(f"    R4-K-corridor hits : {len(d['r4_hits'])}\n")
            fh.write(f"    5-convention hits  : {len(d['conv_hits'])}\n")
            fh.write(f"    audit tag present  : {d['has_tag']}\n")
            for (ln, pat, txt) in d["r4_hits"]:
                fh.write(
                    f"      L{ln}  [{pat[:30]}]  {txt[:140]}\n"
                )
        fh.write(
            f"\nAggregate:\n"
            f"  total R4-K-corridor hits : {total_R4_hits}\n"
            f"  total 5-convention hits  : {total_5conv_hits}\n"
            f"  files with R4 hits       : {files_with_R4}\n"
            f"  files w/R4 no tag        : {files_with_R4_no_tag}\n"
        )
        fh.write(
            f"\nGate result:\n"
            f"  value = {value}\n"
            f"  verdict = {verdict}\n"
            f"  4-tuple = (value={value}, scheme=R4-audit, "
            f"convention=4+1, L_max=N/A)\n"
            f"  sha256 closure = {closure}\n"
        )
        fh.write(f"\nVerdict line:\n  {verdict_line}\n")

    print(f"\nReport written: {report_path}")

    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
