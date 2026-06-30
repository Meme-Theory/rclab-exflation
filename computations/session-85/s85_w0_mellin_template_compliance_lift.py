#!/usr/bin/env python3
"""
S85 W0-19 — S85-MELLIN-TEMPLATE-COMPLIANCE-LIFT ([AUDIT])

Threshold (plan §W0-19):
  PASS iff 16/16 Mellin-balance scripts carry the W6-71 canonical boilerplate.
  INFO iff 13-15/16.
  FAIL iff < 13.

Method: scan computations/_shared/*.py for scripts with Mellin-balance
indicators (scheme=MS-bar + mellin-balance tag + canonical structure).
Count compliance.

Classification: GEOMETRIC (Mellin-balance is substrate-spectral-analysis convention)
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
# ─── W6-71 Mellin discipline markers (S86 W0c-6 retrofit) ───
# MELLIN-CONVERGENCE-STRIP: -1, +3   # (W6-71_default; per-script audit needed)
# MELLIN-RESIDUE-EXTRACTION: residue-at-pole_via_lhopital   # (W6-71_default; per-script audit needed)
# MELLIN-COUNTERTERM-SUBTRACTION: a_2_zeta-regulated   # (W6-71_default; per-script audit needed)
# MELLIN-ANALYTIC-CONTINUATION-PATH: vertical-line_Re(s)=1   # (W6-71_default; per-script audit needed)
# MELLIN-CLOSURE-VERIFICATION: self-consistent_at_residue   # (W6-71_default; per-script audit needed)
# ─────────────────────────────────────────────────────────────


import hashlib, json, re, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                  # (local)
GATE_ID = "S85-MELLIN-TEMPLATE-COMPLIANCE-LIFT"                  # (local)
SCHEME = "template-audit"                                        # (local)
CONVENTION = "Mellin-balance-W6-71"                              # (local)
L_MAX = "NA"                                                     # (local)

TARGET_COUNT = 16                                                # (local) plan expected
PASS_MIN = 16                                                    # (local)
INFO_MIN = 13                                                    # (local)

OUT_NPZ = resolve_output(85, 's85_w0_mellin_template_compliance_lift.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')


def sha256_of(p):
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def compute_dual_sha(script, canonical, pins):
    sb = script.read_bytes(); cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute():
    print("--- Section 5: Mellin-balance template compliance audit ---")
    # Find all computation .py files with Mellin indicators
    candidates = []  # (local)
    for p in sorted(SCRIPT_DIR.glob("*.py")):
        text = p.read_text(encoding="utf-8", errors="ignore")
        # Mellin-balance indicators
        has_mellin = bool(re.search(r"mellin|Mellin", text))
        has_msbar = bool(re.search(r"MS-bar|MS_BAR|ms-bar", text))
        if has_mellin and has_msbar:
            candidates.append(p)

    print(f"  Found {len(candidates)} Mellin-balance candidate scripts (target: {TARGET_COUNT})")

    # Canonical boilerplate compliance markers (W6-71):
    #  1. `from canonical_constants import *`
    #  2. SHA-256 dual-pin block
    #  3. scheme = "MS-bar" or similar canonical pin
    #  4. mellin-balance tag in method or docstring
    #  5. gate verdict append function
    compliant = []  # (local)
    non_compliant = []  # (local)
    for p in candidates:
        text = p.read_text(encoding="utf-8", errors="ignore")
        checks = {
            "canonical_import": bool(re.search(r"from canonical_constants import", text)),
            "dual_sha": bool(re.search(r"audit_sha256.*content_sha256|compute_dual_sha", text, re.DOTALL)),
            "mellin_balance_tag": bool(re.search(r"mellin.?balance|Mellin.?balance|mellin-balance", text)),
            "msbar_pin": bool(re.search(r'(scheme\s*=\s*["\']MS-bar["\'])|MS_BAR', text)),
            "verdict_append": bool(re.search(r"append_verdict|gate_verdicts\.txt", text)),
        }
        is_compliant = all(checks.values())
        if is_compliant:
            compliant.append(p.name)
        else:
            missing = [k for k, v in checks.items() if not v]
            non_compliant.append((p.name, missing))

    print(f"  Compliant scripts: {len(compliant)}/{len(candidates)}")
    for name in compliant[:5]:
        print(f"    ✓ {name}")
    if len(compliant) > 5:
        print(f"    ... ({len(compliant) - 5} more)")
    if non_compliant:
        print(f"  Non-compliant: {len(non_compliant)}")
        for name, missing in non_compliant[:5]:
            print(f"    ✗ {name} — missing: {missing}")

    return dict(
        value=len(compliant),
        compliant_count=len(compliant),
        candidate_count=len(candidates),
        compliant_names=[c.name if isinstance(c, Path) else c for c in compliant],
        non_compliant_count=len(non_compliant),
    )


def evaluate_gate(result):
    n = result["compliant_count"]
    if n >= PASS_MIN:
        return "PASS"
    if n >= INFO_MIN:
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
        compliant_count=result["compliant_count"],
        candidate_count=result["candidate_count"],
        non_compliant_count=result["non_compliant_count"],
        compliant_names=np.array(result["compliant_names"]),
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
