#!/usr/bin/env python3
"""
S85 W0-24 — S85-HOOK-WIRING-R3-YAML-NORMALIZATION ([AUDIT])

Threshold (plan §W0-24):
  PASS iff hook_OK=True AND schema_pct=100%.
  INFO iff hook_OK=True AND 90% ≤ schema_pct < 100%.
  FAIL iff hook_OK=False OR schema_pct < 90%.

Audit-only: check settings.json for PostToolUse hook + scan S85 plan
files for schema_version: R3 declarations.

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
PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"
SETTINGS_JSON = PROJECT_ROOT / ".claude" / "settings.json"
LOCAL_SETTINGS_JSON = PROJECT_ROOT / ".claude" / "settings.local.json"

SESSION = "S85"
GATE_ID = "S85-HOOK-WIRING-R3-YAML-NORMALIZATION"
SCHEME = "R3-YAML-audit"
CONVENTION = "W9-carry-forward"
L_MAX = "NA"

R3_SCHEMA_PATTERN = re.compile(r"schema_version:\s*R3|schema_version=R3", re.IGNORECASE)

OUT_NPZ = resolve_output(85, 's85_w0_hook_wiring_r3_yaml.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')


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
    print("--- Section 5: Hook-wiring + R3 YAML audit ---")
    # Check settings.json for PostToolUse hook
    hook_ok = False  # (local)
    settings_sources = [SETTINGS_JSON, LOCAL_SETTINGS_JSON]
    for sp in settings_sources:
        if sp.exists():
            try:
                s = json.loads(sp.read_text(encoding="utf-8"))
                hooks = s.get("hooks", {})
                if "PostToolUse" in hooks:
                    hook_ok = True
                    print(f"  PostToolUse hook present in {sp.name}")
            except Exception as e:
                print(f"  Error parsing {sp.name}: {e}")
    if not hook_ok:
        print("  PostToolUse hook NOT found in any settings.json")

    # Scan S85 plan files for schema_version: R3
    plan_files = sorted(PLAN_DIR.glob("session-85-plan-w*.md"))
    schema_counts = {}  # (local)
    total_gates_found = 0  # (local)
    total_r3_gates = 0  # (local)
    for p in plan_files:
        text = p.read_text(encoding="utf-8")
        # Count gate blocks (loose: "## §" headers)
        gate_blocks = re.findall(r"^##\s+§W\d+-\d+", text, re.MULTILINE)
        n_gates = len(gate_blocks)
        # Count R3 schema declarations
        r3_hits = len(R3_SCHEMA_PATTERN.findall(text))
        schema_counts[p.name] = dict(n_gates=n_gates, r3_hits=r3_hits)
        total_gates_found += n_gates
        total_r3_gates += r3_hits
    schema_pct = (total_r3_gates / total_gates_found * 100.0) if total_gates_found > 0 else 0.0  # (local)

    print(f"  Scanned {len(plan_files)} S85 plan files")
    print(f"  Total gate blocks: {total_gates_found}")
    print(f"  R3 schema declarations: {total_r3_gates}")
    print(f"  schema_pct (R3 coverage): {schema_pct:.1f}%")

    return dict(
        value=(hook_ok, schema_pct),
        hook_ok=hook_ok,
        schema_pct=schema_pct,
        total_gates=total_gates_found,
        total_r3=total_r3_gates,
        schema_counts=schema_counts,
    )


def evaluate_gate(result):
    hook = result["hook_ok"]
    pct = result["schema_pct"]
    if not hook:
        return "FAIL"
    if pct >= 100.0:
        return "PASS"
    if pct >= 90.0:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    # value is (hook_ok, schema_pct) tuple
    v_repr = f"(hook={value[0]},schema={value[1]:.1f}%)"
    line = (
        f"{GATE_ID}: {verdict} -- value={v_repr} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        hook_ok=result["hook_ok"],
        schema_pct=result["schema_pct"],
        total_gates=result["total_gates"],
        total_r3=result["total_r3"],
        schema_counts_json=json.dumps(result["schema_counts"]),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins([resolve_script(None, 'canonical_constants.py')])
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(),
        resolve_script(None, 'canonical_constants.py'), pins)
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
