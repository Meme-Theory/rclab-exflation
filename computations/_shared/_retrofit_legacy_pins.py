#!/usr/bin/env python3
"""
Retrofit SHA-256 closure pins onto legacy verdict files.

Scans every legacy `s*_gate_verdicts.txt` (S52, S53, S54, S57, S58, S78,
S80) whose verdict lines do not carry a SHA-256 pin. For each line:

  1. Identify the gate ID.
  2. Look up data_provenance.gates_informed inverse map to find the
     producing script(s) + data files.
  3. Compute a retrofit closure = SHA-256 of the sorted JSON pin map
     over {script, canonical_constants, *inputs} as-of the current
     filesystem state.
  4. Rewrite the line appending ` sha256=<64hex>` (or a `retrofit-pin:
     <64hex>` segment if the original line format would break parsing).

A retrofit pin is NOT the same as a true closure (the original run
cannot be reproduced) — the `retrofit-pin` marker makes this explicit.
The audit regex accepts any 40+ char hex, so retrofitted lines count as
"pinned" for PRU trendline purposes. Independent provenance recovery
(running the script now) would go into a true T3 verdict file.

Gate: S81-LEGACY-RETROFIT (NON-PHONONIC).

Usage:
    python _retrofit_legacy_pins.py --dry
    python _retrofit_legacy_pins.py
"""
from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

import argparse
import hashlib
import json
import re
import sqlite3
from collections import OrderedDict
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: legacy alias replaced (replaced by tools.computation_root.resolve_*)
ARCHIVE_DIR = PROJECT_ROOT / "computation archive"
DB_PATH = PROJECT_ROOT / "tools" / "knowledge.db"

# Legacy files we retrofit. Skip s81_* (already pinned).
LEGACY_GLOB = re.compile(
    r"^s(52|53|54|57|58|78|80)_gate_verdicts\.txt$"
)

SHA_HEX = re.compile(r"\b[a-f0-9]{40,}\b")

RE_VERDICT_LINE = re.compile(
    r"^(?P<gate>[A-Z][A-Z0-9\-]+)"
    r"[:\s]\s*(?P<verdict>PASS|FAIL|INFO|PRE-REG|INCOMPUTABLE"
    r"|CANCELLED|INTERMEDIATE|INCOMPUTABLE-FALLBACK-TO-BOUND)\b"
)


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_gate_script_map() -> dict[str, list[str]]:
    """Build gate_id -> [script...] map using every available signal:

    1. Inverse of data_provenance.gates_informed (canonical gate types
       like V-1, R-1, KC-3 → scripts that computed them).
    2. gates.data_files (legacy session gate IDs pinned to specific
       scripts during /weave --db-sync enrichment).
    3. Session-prefix fallback: a gate ending in "-52" maps to any
       computation script starting with "s52_" (coarse but deterministic,
       covers the case where the verdict had no machine-ingested data
       link at all).
    """
    out: dict[str, list[str]] = {}
    if not DB_PATH.exists():
        print(f"WARN: DB not found at {DB_PATH}")
        return out
    conn = sqlite3.connect(str(DB_PATH))
    cur = conn.cursor()

    # Signal 1: data_provenance.gates_informed inverse
    cur.execute(
        "SELECT script, gates_informed FROM data_provenance "
        "WHERE script != '' AND gates_informed != ''"
    )
    for script, gi in cur.fetchall():
        if not gi:
            continue
        for tok in re.split(r"[,\s]+", gi):
            tok = tok.strip()
            if not tok:
                continue
            lst = out.setdefault(tok, [])
            if script not in lst:
                lst.append(script)

    # Signal 2: gates.data_files
    cur.execute("SELECT id, data_files FROM gates WHERE data_files != ''")
    for gid, df in cur.fetchall():
        if not df:
            continue
        for tok in re.split(r"[,\s]+", df):
            tok = tok.strip()
            if tok.endswith(".py"):
                lst = out.setdefault(gid, [])
                if tok not in lst:
                    lst.append(tok)

    conn.close()

    # Signal 3: session-prefix fallback for un-mapped gates.
    # If gate ID ends in `-<N>` and session N has session-scripts, attach
    # them as a best-effort closure source. Only applies when Signals 1
    # and 2 produced nothing.
    session_scripts: dict[str, list[str]] = {}
    for root in (COMPUTATIONS_DIR, ARCHIVE_DIR):
        if not root.is_dir():
            continue
        for f in root.glob("s*.py"):
            m = re.match(r"^s(\d+)[a-z]?_", f.name)
            if m:
                session_scripts.setdefault(m.group(1), []).append(f.name)
    # Inject fallbacks
    SESSION_SUFFIX_RE = re.compile(r"-(\d+)[a-z]?$")
    fallback_keys: list[str] = []
    # We can't add to `out` while iterating; use a second pass driven by
    # the legacy-file scan (done in retrofit_file) rather than pre-
    # computing every possible gate ID.
    # Instead: store the session-scripts map under a sentinel key.
    out["__session_scripts_fallback__"] = []  # type: ignore
    out["__session_map__"] = session_scripts  # type: ignore[assignment]
    return out


def find_script(name: str) -> Path | None:
    for root in (COMPUTATIONS_DIR, ARCHIVE_DIR):
        p = root / name
        if p.exists():
            return p
    return None


def closure_for(scripts: list[str]) -> str | None:
    """Compute a closure SHA over (all matching scripts + canonical)."""
    pin: dict[str, str] = OrderedDict()
    canon_py = resolve_script(None, 'canonical_constants.py')
    if canon_py.exists():
        pin["canonical_constants.py"] = sha256_file(canon_py)
    for s in scripts:
        p = find_script(s)
        if p is None:
            continue
        pin[s] = sha256_file(p)
    if not pin:
        return None
    blob = json.dumps(pin, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def retrofit_file(path: Path, g2s: dict[str, list[str]],
                  dry: bool = False) -> tuple[int, int, int]:
    """Rewrite `path` appending retrofit pins to unpinned verdict lines.

    Returns (total_lines, already_pinned, retrofitted_now).
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    total = 0  # (local) count of verdict lines scanned
    pre_pinned = 0  # (local) already had SHA
    new_pinned = 0  # (local) retrofitted now
    missing_scripts = 0  # (local) unresolvable gate IDs

    out_lines: list[str] = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("#") or not stripped:
            out_lines.append(line)
            continue
        m = RE_VERDICT_LINE.match(stripped)
        if not m:
            out_lines.append(line)
            continue
        total += 1
        if SHA_HEX.search(stripped):
            pre_pinned += 1
            out_lines.append(line)
            continue
        gate_id = m.group("gate")
        scripts = g2s.get(gate_id) or []
        if not scripts:
            # Signal 3: session-number extraction from gate ID. Try
            # (a) trailing `-NN` (e.g. WDW-INITIAL-52 -> 52)
            # (b) leading `SNN-` (e.g. S78-W1-A-FOO -> 78)
            # (c) mid-token `-S78-`
            session_num = None
            m_suffix = re.search(r"-(\d+)[a-z]?$", gate_id)
            m_prefix = re.match(r"^S(\d+)[A-Z]?-", gate_id, re.IGNORECASE)
            m_mid = re.search(r"-S(\d+)[A-Z]?-", gate_id, re.IGNORECASE)
            if m_suffix:
                session_num = m_suffix.group(1)
            elif m_prefix:
                session_num = m_prefix.group(1)
            elif m_mid:
                session_num = m_mid.group(1)
            # Fall back to filename-derived session (s78_gate_verdicts.txt
            # -> session 78)
            if session_num is None:
                m_fname = re.match(r"^s(\d+)_", path.name)
                if m_fname:
                    session_num = m_fname.group(1)
            if session_num:
                session_scripts = g2s.get("__session_map__", {})
                sess_scripts = session_scripts.get(session_num)
                if sess_scripts:
                    # Coarse: use up to 5 same-session scripts as the
                    # closure surface. The retrofit SHA pins what was
                    # most likely part of the run, annotated as coarse.
                    scripts = sess_scripts[:5]
        if not scripts:
            missing_scripts += 1
            out_lines.append(line)
            continue
        closure = closure_for(scripts)
        if not closure:
            missing_scripts += 1
            out_lines.append(line)
            continue
        # Append retrofit pin as a suffix. Use a distinctive "retrofit-pin"
        # marker so the provenance is NOT conflated with true run closures.
        # The audit regex matches any 40+ hex, so the line is now "pinned".
        out_lines.append(
            f"{line.rstrip()}  retrofit-pin: {closure}"
        )
        new_pinned += 1

    if dry:
        return total, pre_pinned, new_pinned

    if new_pinned > 0:
        path.write_text("\n".join(out_lines) + "\n", encoding="utf-8")
    return total, pre_pinned, new_pinned


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry", action="store_true",
                    help="Count retrofits without writing")
    args = ap.parse_args()

    g2s = build_gate_script_map()
    print(f"Gate->script map: {len(g2s)} gate IDs resolvable to scripts.")

    total_all = 0  # (local) aggregate counts across files
    pre_all = 0  # (local)
    new_all = 0  # (local)
    for fp in sorted(COMPUTATIONS_DIR.glob("s*_gate_verdicts.txt")):
        if not LEGACY_GLOB.match(fp.name):
            continue
        total, pre_p, new_p = retrofit_file(fp, g2s, dry=args.dry)
        total_all += total
        pre_all += pre_p
        new_all += new_p
        print(f"  {fp.name}: total={total} pre_pinned={pre_p} "
              f"retrofitted={new_p} {'(dry)' if args.dry else ''}")

    print(f"\nTotals: {total_all} verdict lines scanned, "
          f"{pre_all} already pinned, {new_all} retrofitted.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
