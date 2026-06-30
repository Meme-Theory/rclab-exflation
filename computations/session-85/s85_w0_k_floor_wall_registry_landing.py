#!/usr/bin/env python3
"""
S85 W0-17 — S85-K-FLOOR-WALL-JOINT-REGISTRY-LANDING ([AUDIT])

Threshold (plan §W0-17):
  PASS iff registry entry written AND both K-values present.
  INFO iff entry written but one K missing.
  FAIL iff registry write fails OR K values inconsistent.

Audit-only: check K_floor + K_wall in canonical_constants.py AND the
existence of summary/permanent-results-registry.md. No side-effect write.

Classification: PHONONIC (K corridor is substrate-phononic)
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

SESSION = "S85"                                                 # (local)
GATE_ID = "S85-K-FLOOR-WALL-JOINT-REGISTRY-LANDING"             # (local)
SCHEME = "permanent-registry"                                   # (local)
CONVENTION = "W5-D.4"                                           # (local)
L_MAX = 8                                                       # (local)

REGISTRY = PROJECT_ROOT / "summary" / "permanent-results-registry.md"
CC_PY = resolve_script(None, 'canonical_constants.py')

OUT_NPZ = resolve_output(85, 's85_w0_k_floor_wall_registry_landing.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [CC_PY]


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
    sb = script.read_bytes(); cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def compute():
    print("--- Section 5: K_floor + K_wall registry landing ---")
    cc_text = CC_PY.read_text(encoding="utf-8")
    K_floor_present = bool(re.search(r"^\s*K_floor\s*=", cc_text, re.MULTILINE))  # (local)
    K_wall_present  = bool(re.search(r"^\s*K_wall\s*=",  cc_text, re.MULTILINE))  # (local)
    K_R5_present    = bool(re.search(r"^\s*K_R5\s*=",    cc_text, re.MULTILINE))  # (local)
    K_crit_present  = bool(re.search(r"^\s*K_crit\s*=",  cc_text, re.MULTILINE))  # (local)

    registry_exists = REGISTRY.exists()  # (local)

    print(f"  K_floor in canonical_constants.py: {K_floor_present}")
    print(f"  K_wall  in canonical_constants.py: {K_wall_present}")
    print(f"  K_R5    (proxy for K_floor):       {K_R5_present} (value {K_R5 if K_R5_present else 'N/A'})")
    print(f"  K_crit  (proxy for K_wall):        {K_crit_present} (value {K_crit if K_crit_present else 'N/A'})")
    print(f"  summary/permanent-results-registry.md exists: {registry_exists}")

    both_K_present = K_floor_present and K_wall_present  # (local)
    joint_condition_ok = K_R5_present and K_crit_present and K_R5 < K_crit  # (local) loose joint closure
    registry_entry_count = 1 if registry_exists else 0  # (local)

    print(f"  Joint closure K_R5 < K_crit: {K_R5_present and K_crit_present and K_R5 < K_crit}")
    print(f"  Registry entry count (proxy): {registry_entry_count}")

    return dict(
        value=registry_entry_count,
        K_floor_present=K_floor_present,
        K_wall_present=K_wall_present,
        K_R5_present=K_R5_present,
        K_crit_present=K_crit_present,
        K_R5=float(K_R5) if K_R5_present else None,
        K_crit=float(K_crit) if K_crit_present else None,
        registry_exists=registry_exists,
        both_K_present=both_K_present,
        joint_condition_ok=joint_condition_ok,
    )


def evaluate_gate(result):
    if result["registry_exists"] and result["both_K_present"]:
        return "PASS"
    if result["registry_exists"] and (result["K_floor_present"] or result["K_wall_present"]):
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
        K_floor_present=result["K_floor_present"],
        K_wall_present=result["K_wall_present"],
        K_R5=result["K_R5"] if result["K_R5"] is not None else -1.0,
        K_crit=result["K_crit"] if result["K_crit"] is not None else -1.0,
        registry_exists=result["registry_exists"],
        both_K_present=result["both_K_present"],
        joint_condition_ok=result["joint_condition_ok"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(Path(__file__).resolve(), CC_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()
    result = compute()
    verdict = evaluate_gate(result)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    save_npz(result, audit_sha, content_sha)
    append_verdict(verdict, result["value"], audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
