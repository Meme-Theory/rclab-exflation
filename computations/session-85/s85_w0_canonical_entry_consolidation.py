#!/usr/bin/env python3
"""
S85 W0-14 — S85-CANONICAL-ENTRY-CONSOLIDATION
==============================================

Gate: S85-CANONICAL-ENTRY-CONSOLIDATION ([AUDIT])

Pre-registered threshold (plan §W0-14):
  Target entries (5): eps_H_HP1_norm, HP1_dim, FI_parity_exclusion,
                      rank_exclusion, nonflat_T_correction_L2
  PASS iff ≥ 5 present in canonical_constants.py, 0 collisions.
  INFO iff 3-4 present.
  FAIL iff < 3 OR any collision.

Presence-only audit: this script does NOT modify canonical_constants.py
(safe mid-session posture). If entries are absent, it reports them as
S86 carry-forward.

Known values from S84 syntheses:
  ‖[ε_H]‖_{HP^1} = 16.197719  (S84 W10-114, lizzi synthesis Result 1)
  dim HP^1(A_F) = 3           (van-den-dungen synthesis, CM-2008 anchor)
  FI parity exclusion: parity([ε_H]) = 1 mod 2; parity(ch(K_0)) = 0 mod 2
  rank exclusion: image(ch: K_0 → HP^0(A_F)) = rank-3 lattice
  nonflat_T correction at L=2: non-flat T connection scalar correction (vdd §VI)

Classification: META
"""

from __future__ import annotations
import os
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

os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

import hashlib, json, re, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                    # (local)
GATE_ID = "S85-CANONICAL-ENTRY-CONSOLIDATION"                      # (local)
SCHEME = "canonical-consolidation"                                 # (local)
CONVENTION = "provenance-tagged"                                   # (local)
L_MAX = "NA"                                                       # (local)

TARGET_ENTRIES = [                                                 # (local) names to check for
    "eps_H_HP1_norm",
    "HP1_dim",
    "FI_parity_exclusion",
    "rank_exclusion",
    "nonflat_T_correction_L2",
]

# Known canonical values from S84 cohomology syntheses
KNOWN_VALUES = {                                                   # (local)
    "eps_H_HP1_norm": 16.197719,
    "HP1_dim": 3,
    "FI_parity_exclusion": 1,  # parity([ε_H]) = 1 mod 2
    "rank_exclusion": 3,        # image(ch: K_0 → HP^0(A_F)) rank-3 lattice
    "nonflat_T_correction_L2": None,  # value not explicitly stated in syntheses
}

CC_PY = resolve_script(None, 'canonical_constants.py')
LIZZI = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s5-lizzi-cohomology-synthesis.md"
VDD = PROJECT_ROOT / "sessions" / "session-84" / "session-84-s5-vdd-cohomology-synthesis.md"

OUT_NPZ = resolve_output(85, 's85_w0_canonical_entry_consolidation.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [CC_PY, LIZZI, VDD]


def sha256_of(p):
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script, canonical, pins):
    sb = script.read_bytes()
    cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def audit_canonical_constants():
    cc_text = CC_PY.read_text(encoding="utf-8")
    present = {}  # (local)
    for entry in TARGET_ENTRIES:
        # Look for assignment "entry ="  at line start (loose match)
        pat = re.compile(rf"^\s*{re.escape(entry)}\s*=", re.MULTILINE)
        present[entry] = bool(pat.search(cc_text))
    # Collision check: any entry that appears > 1 time at line start?
    collisions = 0  # (local)
    for entry in TARGET_ENTRIES:
        pat = re.compile(rf"^\s*{re.escape(entry)}\s*=", re.MULTILINE)
        matches = pat.findall(cc_text)
        if len(matches) > 1:
            collisions += 1
    return present, collisions


def compute():
    print("--- Section 5: Canonical entry consolidation audit ---")
    present, collisions = audit_canonical_constants()
    n_present = sum(1 for v in present.values() if v)  # (local)
    print(f"  Target entries (5):")
    for entry, is_present in present.items():
        kv = KNOWN_VALUES.get(entry)
        status = "✓ present" if is_present else "✗ MISSING"
        print(f"    {entry:32s}  {status}  (S84 value: {kv!r})")
    print(f"  Total present: {n_present}/5")
    print(f"  Collision check: {collisions} duplicates detected")
    return dict(
        value=n_present,
        entries_present=present,
        n_present=n_present,
        collisions=collisions,
        known_values=KNOWN_VALUES,
    )


def evaluate_gate(result):
    if result["collisions"] > 0:
        return "FAIL"
    if result["n_present"] >= 5:
        return "PASS"
    if result["n_present"] >= 3:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        n_present=result["n_present"],
        collisions=result["collisions"],
        target_entries=np.array(TARGET_ENTRIES),
        entries_present_json=json.dumps(result["entries_present"]),
        known_values_json=json.dumps({k: v for k, v in result["known_values"].items()}),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CC_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    result = compute()
    verdict = evaluate_gate(result)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_npz(result, audit_sha, content_sha)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
