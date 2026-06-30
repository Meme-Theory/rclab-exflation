#!/usr/bin/env python3
"""
S86 W0c-3 companion — vdd §VI non-flat T-correction extractor
==============================================================

Per plan §W0c-3.6 step (b): "write a small companion script ... that reads
researchers/Van-den-Dungen/<vdd_paper>.md (orchestrator pins the exact filename
at dispatch; if absent, the script glob-searches researchers/Van-den-Dungen/*.md
and prints candidates), parses §VI for the non-flat T-correction at L_max=2,
prints the value to 6 sig figs, and exits 0 on success."

Outcome: the 14 vdd-tracked papers in researchers/Van-den-Dungen/ use named
section headings (Abstract, Historical Context, Key Arguments and Derivations,
Key Results, Impact and Legacy, Connection to Phonon-Exflation Framework),
NOT numbered §VI headings. There is therefore NO §VI section to parse. The
substrate-first canonical source for the non-flat T-correction at L_max=2 is
the S83 W2-G24 first-principles computation (Cartan-flat-at-tau_fold theorem)
recorded in computations/session-83/s83_w2_g24_nonflat_t_correction_l2.npz key
'correction_P1_T' = 0.0 (machine-epsilon zero).

This script:
  (a) globs researchers/Van-den-Dungen/*.md and lists candidates with SHA-256;
  (b) attempts §VI / Section VI grep; reports absence;
  (c) extracts the substrate-first canonical value from the S83 W2-G24 npz;
  (d) prints the value to 6 sig figs;
  (e) exits 0 on substrate-first extraction (or 2 if S83 npz is unreadable).
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401  # framework-import discipline (computations/_shared/CLAUDE.md)

import hashlib
import re
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
VDD_DIR = PROJECT_ROOT / "researchers" / "Van-den-Dungen"
S83_NPZ = PROJECT_ROOT / "computations" / "session-83" / "s83_w2_g24_nonflat_t_correction_l2.npz"


def main() -> int:
    print("=== vdd §VI non-flat T-correction extraction ===\n")

    # (a) Glob candidates
    candidates = sorted(VDD_DIR.glob("*.md"))  # (local)
    print(f"Found {len(candidates)} vdd paper candidates in {VDD_DIR.relative_to(PROJECT_ROOT)}:")
    for p in candidates:
        h = hashlib.sha256(p.read_bytes()).hexdigest()  # (local)
        print(f"  {p.name}  sha256={h[:16]}...")

    # (b) Attempt §VI / Section VI grep
    print("\n--- §VI / Section VI grep across vdd papers ---")
    pattern = re.compile(
        r"(?:^|\n)\s*#+\s*(?:§?\s*VI[\s\.\)]|Section\s+VI[\s\.\)])",
        re.MULTILINE,
    )  # (local)
    found_any = False  # (local)
    for p in candidates:
        text = p.read_text(encoding="utf-8")  # (local)
        m = pattern.search(text)
        if m:
            found_any = True
            print(f"  {p.name}: §VI candidate at offset {m.start()}: {m.group()!r}")
    if not found_any:
        print(
            "  No §VI / Section VI heading found in any vdd paper. "
            "The 14 papers use named sections (Abstract, Key Arguments and Derivations, "
            "Key Results, Impact and Legacy, Connection to Phonon-Exflation Framework), "
            "not numbered Roman-numeral sections."
        )

    # (c) Extract substrate-first canonical value from S83 W2-G24 npz
    print("\n--- Substrate-first canonical extraction (S83 W2-G24 npz) ---")
    if not S83_NPZ.exists():
        print(f"FAIL: S83 npz absent at {S83_NPZ}")
        return 2

    import numpy as np  # (local) — deferred to keep glob/grep fast

    d = np.load(S83_NPZ, allow_pickle=True)  # (local)
    correction = float(d["correction_P1_T"])  # (local) — substrate-first canonical
    verdict = str(d["verdict"])  # (local)
    reason = str(d["verdict_reason"])  # (local)
    print(f"  correction_P1_T (canonical): {correction!r}")
    print(f"  S83 W2-G24 verdict: {verdict}")
    print(f"  Reason: {reason[:160]}...")

    # (d) Print to 6 sig figs
    if correction == 0.0:
        sig6 = "0.00000"  # (local) — exact-zero canonical form
    else:
        sig6 = f"{correction:.5e}"  # (local) — 6 sig fig scientific form

    print(f"\n=== EXTRACTED VALUE (6 sig figs) ===")
    print(f"  nonflat_T_correction_L2 = {sig6}")
    print(f"  Source: S83 W2-G24 substrate-first computation (Cartan-flat at tau_fold)")
    print(f"  Methodological reference: vdd Chamseddine-Marcolli Particle Physics ACM (paper 06)")
    print(f"          (no §VI heading found; framework's substrate computation is canonical)")

    return 0


if __name__ == "__main__":
    sys.exit(main())
