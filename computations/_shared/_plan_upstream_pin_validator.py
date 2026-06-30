#!/usr/bin/env python3
"""
_plan_upstream_pin_validator.py — upstream-reference pin validation for wave plans (S86+)

Purpose
-------
Detect systematic plan-authoring pin drift BEFORE dispatch. For each gate
block in a wave plan that cites an upstream `.npz` artifact, cross-check
the plan-stated machinery pins (`L_max`, `n_tau`, `scheme`, `convention`)
against the actual npz payload. Flag mismatches.

Origin
------
S85 W9 observed 7 plan-authoring documentation bugs clustering
systematically across two gate blocks:
  - W9-1 pinned L_max=10 and n_tau=61 while the actual W10-121 npz was
    at L_max=5 and n_tau=301.
  - W9-2 pinned L_max=10 while the actual W6-69 and W6-70 npz files
    were at L_max=3.
  - W9-1 pinned artifact slug `s84_w10_121_borel_floor.npz` while the
    actual file was `s84_w10a_121_saddle_inventory.npz`.
  - W9-1 and W9-2 both pinned the registry at
    `sessions/framework/permanent-results-registry.md` while the
    canonical path is `sessions/permanent-results-registry.md`.

Runtime canonical-path rule (`.claude/rules/gate-verdicts.md`) rescued
each case, but prevention at plan-write time is cheaper than rescue at
dispatch time. This validator runs after per-wave planner agents
complete in `/rclab-plan` Phase 3d, before the Phase 4 user checkpoint.

Scope
-----
This validator does NOT replace the R3 YAML gate validator
(`_yaml_gate_validator.py`, which checks schema_version and PRDR
machinery-enumeration checklist completeness). The two validators are
orthogonal:
  - `_yaml_gate_validator.py`     : gate-block structural completeness
  - `_plan_upstream_pin_validator.py` : upstream-reference consistency

Both should run per wave before dispatch.

Cross-checked pins (PIN MAP)
----------------------------
    CHECKED_KEYS       = ("L_max", "n_tau", "scheme", "convention")
    PARSED_PLAN_TABLES = (machinery-pin, input-SHA-ledger)
    SEARCH_DIRS        = ("computations/_shared/",
                          "sessions/session-*/computation-artifacts/")
    NPZ_KEY_ALIASES    = (see NPZ_KEY_ALIAS_MAP below)

Usage
-----
    python _plan_upstream_pin_validator.py <plan_file.md> [<plan_file.md> ...]
    python _plan_upstream_pin_validator.py --json <plan_file.md>
    python _plan_upstream_pin_validator.py --strict <plan_file.md>  # exit 1 on any warning

Exit codes
----------
    0 — all cited upstream npz files exist AND all cross-checked pins
        match payload (within alias normalization).
    1 — at least one mismatch OR at least one cited npz missing from
        disk.
    2 — plan file parse error (malformed tables, no gate blocks,
        file not found, etc.).

No framework constants imported (NON-PHONONIC methodology tool).
Local intermediates tagged `# (local)` per .claude/rules/math-scripts.md.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")  # (local) CPU cap

import argparse
import glob
import json
import re
import sys
from pathlib import Path
from typing import Any

import numpy as np

# ------------------------------------------------------------------
# Self-PRDR pin block (W9 documentation-bug-cluster origin)
# ------------------------------------------------------------------
CHECKED_KEYS: tuple[str, ...] = ("L_max", "n_tau", "scheme", "convention")
SEARCH_DIRS: tuple[str, ...] = (
    "computations",
    "sessions",  # descended recursively for computation-artifacts/ subdirs
)

# Plan-form parameter name → npz payload key (some npz files use different casing)
NPZ_KEY_ALIAS_MAP: dict[str, tuple[str, ...]] = {
    "L_max":      ("L_max", "L_MAX", "l_max"),
    "n_tau":      ("n_tau", "N_tau", "ntau"),
    "scheme":     ("scheme", "tuple_scheme"),
    "convention": ("convention", "tuple_convention"),
}

# Regex patterns
RE_GATE_HEADER = re.compile(r"^##\s+§(W[\w-]+-\d+)\.\s+([A-Z][\w-]+)", re.M)  # (local)
# Gate body terminates at ANY next `##` header (either another gate or a wave-close section)
RE_ANY_H2 = re.compile(r"^##\s+", re.M)  # (local)
RE_TABLE_ROW = re.compile(r"^\|(.+)\|\s*$", re.M)  # (local)
# Bare `.npz` tokens (preserves the extension in the captured group)
RE_NPZ_BARE = re.compile(r"`([a-zA-Z0-9_\-/\\.]+\.npz)`")  # (local)
# Brace-expanded forms like `foo.{npz,py}` or `foo.{py,npz}` (reconstructed to `foo.npz`)
RE_NPZ_BRACE = re.compile(r"`([a-zA-Z0-9_\-/\\.]+?)\.\{[^}]*\bnpz\b[^}]*\}`")  # (local)
# R3-YAML structured pins: `path: "computations/.../foo.npz"` inside machinery_pin_map /
# input_files / output_artifacts blocks. The backtick forms above are the legacy
# markdown-prose pin style; R3 gate blocks pin upstream npz as double-quoted `path:` values,
# which the backtick regexes never matched (silent 0-extraction false-PASS on every R3 gate).
RE_NPZ_PATH_PIN = re.compile(r'path:\s*"([^"]+\.npz)"')  # (local)
# Plan-filename pattern to extract session N and wave index i (for output-artifact suppression)
RE_PLAN_FILENAME = re.compile(
    r"session-(?P<N>\d+)-plan-w(?P<w>[\w]+)\.md$", re.I
)  # (local)


# ------------------------------------------------------------------
# Plan parsing
# ------------------------------------------------------------------

def _parse_table_rows(md_block: str) -> list[list[str]]:
    """Extract rows from markdown tables in an arbitrary md_block.

    Returns list of row-lists (each row a list of stripped cell strings).
    Skips header separator rows (containing only `---`, `:---`, etc.).
    """
    rows = []  # (local)
    for m in RE_TABLE_ROW.finditer(md_block):
        cells = [c.strip() for c in m.group(1).split("|")]  # (local)
        # Skip separator rows
        if all(re.fullmatch(r":?-+:?", c) for c in cells if c):
            continue
        rows.append(cells)
    return rows


def _extract_gate_blocks(plan_text: str) -> list[dict[str, Any]]:
    """Split plan file into per-gate blocks.

    Returns list of {gate_header, gate_id, body} dicts, one per gate
    section `## §W{i}-{n}. {GATE_ID}`.

    Gate body ends at the NEXT `##` H2 header (another gate OR a
    wave-close section like `## Wave W9 → Wave W10 Decision Point`).
    This prevents the last gate from capturing wave-level trailing
    sections that may reference other gates' artifacts.
    """
    headers = list(RE_GATE_HEADER.finditer(plan_text))  # (local)
    all_h2 = list(RE_ANY_H2.finditer(plan_text))  # (local) every ## header start
    blocks = []  # (local)
    for i, h in enumerate(headers):
        start = h.end()  # (local)
        # Next H2 of ANY kind after this gate header's start
        next_h2_starts = [m.start() for m in all_h2 if m.start() > h.start()]  # (local)
        end = next_h2_starts[0] if next_h2_starts else len(plan_text)  # (local)
        blocks.append({
            "gate_anchor": h.group(1),                       # e.g., W9-1
            "gate_id_candidate": h.group(2),                  # e.g., S85
            "header_line": h.group(0),
            "body": plan_text[start:end],
        })
    return blocks


def _extract_gate_machinery_pins(body: str) -> dict[str, str]:
    """Find the gate's machinery-pin table and return pinned values.

    Searches for a table following a "Machinery pin" or "PRDR" heading in
    the gate body. Returns a dict of {parameter_name: pinned_value_str}.
    """
    pins: dict[str, str] = {}  # (local)
    # Try to locate the machinery-pin sub-block
    m = re.search(
        r"(?:Machinery pin|PRDR|\*\*7\.?\s+Machinery pin.*?\*\*)"
        r"(.*?)(?:^\*\*\d+\.|^##|\Z)",
        body, re.S | re.M | re.I,
    )  # (local)
    if not m:
        return pins
    sub_block = m.group(1)  # (local)
    rows = _parse_table_rows(sub_block)  # (local)
    if not rows:
        # Bullet-list form — supports 3 backtick placements (all observed in
        # S85 W9 plan):
        #   - `tau_step = 0.005` (comment)      [form A: whole-expr backticks]
        #   - `L_max` = 10                      [form B: key-only backticks]
        #   - tau_step = 0.005                  [form C: no backticks]
        bullet_re = re.compile(
            r"^\s*-\s*"
            r"`?(\w+)`?"           # key (optional backticks)
            r"\s*=\s*"             # equals
            r"`?([^`\n]+?)`?"      # value — greedy-lazy, inside-or-no backticks
            r"(?:\s*\(.*)?$",      # optional parenthetical comment to EOL
            re.M,
        )  # (local)
        for line in sub_block.splitlines():
            bm = bullet_re.match(line)  # (local)
            if bm:
                key = bm.group(1).strip()  # (local)
                val = bm.group(2).strip().rstrip(",")  # (local)
                if key:
                    pins[key] = val
        return pins
    # Table form: expect header row + data rows
    if len(rows) < 2:
        return pins
    header_row = rows[0]  # (local) e.g., ["Parameter", "Pinned value"] or ["Parameter", "Value", ...]
    # Find "Parameter" column index
    try:
        col_param = next(i for i, c in enumerate(header_row) if "param" in c.lower())  # (local)
    except StopIteration:
        col_param = 0  # (local) default: first column is parameter name
    try:
        col_value = next(
            i for i, c in enumerate(header_row)
            if "value" in c.lower() or "pinned" in c.lower()
        )  # (local)
    except StopIteration:
        col_value = 1  # (local) default: second column is pinned value
    for r in rows[1:]:
        if col_param < len(r) and col_value < len(r):
            key = r[col_param].strip().strip("`")  # (local)
            val = r[col_value].strip().strip("`")  # (local)
            if key:
                pins[key] = val
    return pins


def _extract_gate_upstream_npz(body: str, own_prefix: str | None = None) -> list[str]:
    """Find all `foo.npz` tokens referenced in the gate body.

    Supports both bare `foo.npz` and brace-expanded `foo.{npz,py}` forms.
    Brace forms are reconstructed to `foo.npz` for downstream resolution.

    If `own_prefix` is given (e.g., "s85_w9"), references whose basename
    starts with that prefix are treated as OUTPUT artifacts of the plan
    being validated (which don't exist at plan-write time) and are
    suppressed from the returned list. This prevents false-positive
    "missing" reports on every gate's own emitted npz file.
    """
    raw_tokens: list[str] = []  # (local)
    raw_tokens.extend(RE_NPZ_BARE.findall(body))
    # Brace form: reconstruct ".npz" extension onto the captured stem
    raw_tokens.extend(f"{stem}.npz" for stem in RE_NPZ_BRACE.findall(body))
    # R3-YAML structured `path: "...npz"` pins (machinery_pin_map / input_files /
    # output_artifacts). Without this, R3 gate blocks extract 0 upstream npz and the
    # validator silently PASSes (no-op) on every gate.
    raw_tokens.extend(RE_NPZ_PATH_PIN.findall(body))

    # Deduplicate while preserving order; suppress own-prefix outputs
    seen: set[str] = set()  # (local)
    result: list[str] = []  # (local)
    for t in raw_tokens:
        if t in seen:
            continue
        seen.add(t)
        # Output-artifact suppression: references to the plan's own output
        # namespace are not "upstream" inputs and would not exist pre-dispatch.
        # Extended to suppress sibling-wave outputs of the SAME session: a wave
        # plan citing `s{N}_wX_*.npz` for X != current wave is a legitimate
        # cross-wave intra-session dependency that won't exist at plan-freeze
        # but WILL at dispatch (sibling waves run per declared dependency order).
        if own_prefix:
            # Suppress the WHOLE own-session namespace `s{N}_` (not only `s{N}_w*`):
            # R3 plans name outputs `s{N}_cf_*`, `s{N}_<descriptor>`, etc., which the
            # old `s{N}_w` prefix missed -> false-positive MISSING on every own-output.
            # Legacy `s{N}_w{i}_*` outputs still start with `s{N}_`, so no regression.
            session_prefix = own_prefix.split("_w", 1)[0] + "_"  # (local) e.g., "s111_" from "s111_w1"
            basename = t.rsplit("/", 1)[-1].rsplit("\\", 1)[-1]  # (local)
            if basename.startswith(session_prefix):
                continue
        result.append(t)
    return result


def _infer_own_prefix(plan_path: Path) -> str | None:
    """Parse `session-{N}-plan-w{i}.md` filename → own-output prefix `s{N}_w{i}`.

    Returns None if the filename doesn't match the expected pattern.
    """
    m = RE_PLAN_FILENAME.search(plan_path.name)  # (local)
    if not m:
        return None
    N = m.group("N")  # (local)
    w = m.group("w").lower()  # (local)
    return f"s{N}_w{w}"


def _resolve_npz_path(npz_ref: str, project_root: Path) -> Path | None:
    """Given a plan-stated npz filename/path, try to resolve it on disk.

    Search strategy:
      1. If it's an absolute or relative path that exists → return it.
      2. Strip directory prefix, search in SEARCH_DIRS.
      3. Fuzzy match: try basename matching within glob patterns.
    """
    p = Path(npz_ref)  # (local)
    # 1. Direct path
    if p.is_absolute() and p.exists():
        return p
    abs_p = project_root / npz_ref  # (local)
    if abs_p.exists():
        return abs_p
    # 2. Basename search
    basename = p.name  # (local)
    for sd in SEARCH_DIRS:
        for candidate in (project_root / sd).rglob(basename):
            if candidate.is_file():
                return candidate
    return None


# ------------------------------------------------------------------
# Npz payload inspection
# ------------------------------------------------------------------

def _extract_npz_value(npz_path: Path, plan_key: str) -> Any:
    """Load npz and return the payload value for plan_key (trying aliases).

    Returns the scalar value if key found, else returns a sentinel dict
    {"__MISSING__": True, "aliases_tried": [...]}.
    """
    try:
        d = np.load(npz_path, allow_pickle=True)
    except Exception as e:
        return {"__LOAD_ERROR__": True, "error": repr(e)}
    aliases = NPZ_KEY_ALIAS_MAP.get(plan_key, (plan_key,))  # (local)
    for key in aliases:
        if key in d.files:
            v = d[key]
            # Try to coerce to native Python
            try:
                if hasattr(v, "shape") and v.shape == ():
                    val = v.item()
                else:
                    val = v.tolist() if hasattr(v, "tolist") else v
            except Exception:
                val = str(v)
            return val
    return {
        "__MISSING__": True,
        "aliases_tried": list(aliases),
        "npz_keys_available": list(d.files),
    }


# ------------------------------------------------------------------
# Value normalization & comparison
# ------------------------------------------------------------------

def _normalize_value(v: Any) -> Any:
    """Coerce plan/npz values to a common form for comparison.

    Integers as `int`; numeric strings as `float` or `int`; string labels
    stripped. Strings containing parenthetical comments are reduced to
    the leading token.
    """
    if isinstance(v, (int, float, bool)):
        return v
    # Single-element list/tuple from npz payload (e.g., `np.array([12]).tolist() == [12]`)
    # Recursively normalize the scalar element so plan_value '12' matches npz_value [12].
    if isinstance(v, (list, tuple)) and len(v) == 1:
        return _normalize_value(v[0])
    if isinstance(v, bytes):
        v = v.decode("utf-8", errors="replace")
    if isinstance(v, str):
        v = v.strip().strip("`'\"")
        # Strip trailing comments like "10 (S83 Branch-B baseline)"
        v = re.split(r"\s*[\(#]", v, maxsplit=1)[0].strip()
        # Try int then float
        try:
            return int(v)
        except ValueError:
            pass
        try:
            return float(v)
        except ValueError:
            pass
        return v
    return v


def _values_match(plan_v: Any, npz_v: Any) -> bool:
    """Compare plan pin vs npz payload value under tolerant normalization."""
    if isinstance(npz_v, dict) and npz_v.get("__MISSING__"):
        # Key absent from npz — not a mismatch, a separate 'KEY_MISSING' case
        return False
    if isinstance(npz_v, dict) and npz_v.get("__LOAD_ERROR__"):
        return False
    pn = _normalize_value(plan_v)  # (local)
    nn = _normalize_value(npz_v)   # (local)
    # Exact match
    if pn == nn:
        return True
    # Int vs float tolerance
    if isinstance(pn, (int, float)) and isinstance(nn, (int, float)):
        return abs(float(pn) - float(nn)) < 1e-9
    # String inclusion (npz label is "W10-121-original" while plan says
    # "W10-121-original" might include a trailing parenthetical)
    if isinstance(pn, str) and isinstance(nn, str):
        return pn.lower() in nn.lower() or nn.lower() in pn.lower()
    return False


# ------------------------------------------------------------------
# Validation core
# ------------------------------------------------------------------

def validate_plan_file(plan_path: Path, project_root: Path) -> dict[str, Any]:
    """Validate one wave plan file.

    Returns a report dict with overall verdict and per-gate diagnostics.
    """
    if not plan_path.exists():
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": f"Plan file not found: {plan_path}",
        }
    try:
        plan_text = plan_path.read_text(encoding="utf-8")
    except OSError as e:
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": f"Plan file read failure: {e!r}",
        }

    blocks = _extract_gate_blocks(plan_text)  # (local)
    if not blocks:
        return {
            "plan_file": str(plan_path),
            "verdict": "PARSE-ERROR",
            "error": "No gate blocks (## §W{i}-{n}) found in plan file.",
        }

    own_prefix = _infer_own_prefix(plan_path)  # (local) e.g., "s85_w9" for session-85-plan-w9.md

    gate_reports: list[dict[str, Any]] = []  # (local)
    n_gates = len(blocks)  # (local)
    n_gates_checked = 0  # (local) counter for gates with upstream npz references
    n_mismatches_total = 0  # (local) aggregate mismatch count across all gates
    n_missing_npz_total = 0  # (local) aggregate missing-artifact count

    for blk in blocks:
        gate_anchor = blk["gate_anchor"]  # (local) e.g., W9-1
        body = blk["body"]  # (local)

        pins = _extract_gate_machinery_pins(body)  # (local)
        upstream_npzs = _extract_gate_upstream_npz(body, own_prefix=own_prefix)  # (local)

        if not upstream_npzs:
            gate_reports.append({
                "gate_anchor": gate_anchor,
                "status": "NO-UPSTREAM-NPZ",
                "note": "Gate has no .npz artifact references; nothing to cross-check.",
                "pins_extracted": len(pins),
            })
            continue

        n_gates_checked += 1
        resolved_artifacts: list[dict[str, Any]] = []  # (local)
        mismatches: list[dict[str, Any]] = []  # (local) hard FAIL: value disagrees
        warnings_key_absent: list[dict[str, Any]] = []  # (local) soft WARN: key not in npz

        for npz_ref in upstream_npzs:
            resolved = _resolve_npz_path(npz_ref, project_root)  # (local)
            artifact_report = {
                "npz_ref": npz_ref,
                "resolved_path": str(resolved) if resolved else None,
                "found": resolved is not None,
                "key_checks": {},
            }
            if resolved is None:
                n_missing_npz_total += 1
                artifact_report["note"] = (
                    f"Plan cites `{npz_ref}` but no matching file found "
                    f"under {SEARCH_DIRS}."
                )
                resolved_artifacts.append(artifact_report)
                continue
            # Cross-check each CHECKED_KEYS pin
            for key in CHECKED_KEYS:
                if key not in pins:
                    continue  # Not pinned for this gate; nothing to check
                plan_value = pins[key]  # (local)
                npz_value = _extract_npz_value(resolved, key)  # (local)
                key_absent = (
                    isinstance(npz_value, dict) and npz_value.get("__MISSING__")
                )  # (local)
                match = _values_match(plan_value, npz_value)  # (local)
                artifact_report["key_checks"][key] = {
                    "plan_value": plan_value,
                    "npz_value": npz_value,
                    "match": match,
                    "key_absent_from_npz": bool(key_absent),
                }
                if not match:
                    if key_absent:
                        # Soft warning: upstream just didn't save this label.
                        # Not a pin-drift bug.
                        warnings_key_absent.append({
                            "gate_anchor": gate_anchor,
                            "npz_ref": npz_ref,
                            "resolved_path": str(resolved),
                            "parameter": key,
                            "plan_value": plan_value,
                            "npz_keys_available": npz_value.get(
                                "npz_keys_available", []
                            ),
                        })
                    else:
                        # Hard mismatch: real pin drift or value disagreement
                        mismatches.append({
                            "gate_anchor": gate_anchor,
                            "npz_ref": npz_ref,
                            "resolved_path": str(resolved),
                            "parameter": key,
                            "plan_value": plan_value,
                            "npz_value": npz_value,
                        })
            resolved_artifacts.append(artifact_report)

        n_mismatches_total += len(mismatches)
        gate_reports.append({
            "gate_anchor": gate_anchor,
            "status": "FAIL" if (mismatches or any(not a["found"] for a in resolved_artifacts)) else ("WARN" if warnings_key_absent else "PASS"),
            "artifacts": resolved_artifacts,
            "mismatches": mismatches,
            "warnings_key_absent": warnings_key_absent,
        })

    verdict = "PASS" if (n_mismatches_total == 0 and n_missing_npz_total == 0) else "FAIL"
    return {
        "plan_file": str(plan_path),
        "verdict": verdict,
        "n_gates_total": n_gates,
        "n_gates_checked": n_gates_checked,
        "n_gates_no_upstream": n_gates - n_gates_checked,
        "n_mismatches": n_mismatches_total,
        "n_missing_npz": n_missing_npz_total,
        "gate_reports": gate_reports,
    }


# ------------------------------------------------------------------
# Reporting
# ------------------------------------------------------------------

def _report_human(report: dict[str, Any]) -> None:
    print(f"=== {report['plan_file']} ===")
    if report["verdict"] == "PARSE-ERROR":
        print(f"  PARSE-ERROR: {report.get('error', 'unknown')}")
        return
    # Count warnings and mismatches separately
    n_warn = sum(  # (local)
        len(gr.get("warnings_key_absent", []))
        for gr in report.get("gate_reports", [])
    )
    print(f"  verdict: {report['verdict']}")
    print(f"  gates total          : {report['n_gates_total']}")
    print(f"  gates cross-checked  : {report['n_gates_checked']} "
          f"({report['n_gates_no_upstream']} had no upstream npz)")
    print(f"  mismatches (hard)    : {report['n_mismatches']}")
    print(f"  key-absent (soft)    : {n_warn}")
    print(f"  missing npz artifacts: {report['n_missing_npz']}")
    # Print hard issues first, then soft warnings
    hard_gates = [gr for gr in report["gate_reports"]
                  if gr.get("status") == "FAIL"]  # (local)
    warn_gates = [gr for gr in report["gate_reports"]
                  if gr.get("status") == "WARN"]  # (local)
    if hard_gates:
        print("\n  HARD ISSUES:")
        for gr in hard_gates:
            print(f"  {gr['gate_anchor']}:")
            for a in gr.get("artifacts", []):
                if not a["found"]:
                    print(f"    [MISSING] {a['npz_ref']} — {a.get('note', '')}")
                    continue
                for key, kc in a.get("key_checks", {}).items():
                    if not kc["match"] and not kc.get("key_absent_from_npz"):
                        print(f"    [MISMATCH] {a['npz_ref']} / {key}: "
                              f"plan={kc['plan_value']!r}  "
                              f"npz={kc['npz_value']!r}")
    if warn_gates:
        print("\n  SOFT WARNINGS (key not saved in upstream npz):")
        for gr in warn_gates:
            for w in gr.get("warnings_key_absent", []):
                print(f"  {gr['gate_anchor']}: [KEY-ABSENT] "
                      f"{w['npz_ref']} / {w['parameter']}: "
                      f"plan={w['plan_value']!r} (npz has no key; "
                      f"upstream didn't save it)")
    print()


def _exit_code(reports: list[dict[str, Any]], strict: bool = False) -> int:
    if any(r["verdict"] == "PARSE-ERROR" for r in reports):
        return 2
    if any(r["verdict"] == "FAIL" for r in reports):
        return 1
    if strict:
        # In strict mode, WARN also exits non-zero
        any_warn = any(  # (local)
            any(gr.get("status") == "WARN"
                for gr in r.get("gate_reports", []))
            for r in reports
        )
        if any_warn:
            return 1
    return 0


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Upstream-reference pin validator for wave plans."
    )
    parser.add_argument("plan_files", nargs="+", help="Wave plan markdown file(s).")
    parser.add_argument("--json", action="store_true",
                        help="Emit JSON reports instead of human-readable text.")
    parser.add_argument("--strict", action="store_true",
                        help="Exit non-zero even if only missing-npz (not mismatch) was found.")
    args = parser.parse_args(argv)

    # Project root: one level up from this script (computations/_shared/ → project root)
    project_root = Path(__file__).resolve().parent.parent.parent  # (local)  # validator at computations/_shared/<file>; project root is two levels up from _shared, three from <file>

    reports: list[dict[str, Any]] = []  # (local)
    for pf in args.plan_files:
        pf_path = Path(pf)
        if not pf_path.is_absolute():
            pf_path = project_root / pf
        report = validate_plan_file(pf_path, project_root)  # (local)
        reports.append(report)

    if args.json:
        print(json.dumps(reports, indent=2, default=str))
    else:
        for r in reports:
            _report_human(r)

    return _exit_code(reports, strict=args.strict)


if __name__ == "__main__":
    sys.exit(main())
