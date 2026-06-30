#!/usr/bin/env python3
"""
S85 W0-15 — S85-CSCANON-IDENTITY-TEST
======================================

Gate: S85-CSCANON-IDENTITY-TEST ([VERIFY])

Pre-registered threshold (plan §W0-15):
  HYPOTHESIS: max_K |f_B(K) − c_S_canon| ≤ 1e-3 across
    K ∈ linspace(K_R5=1.9222, K_crit=2.0446, 50)
  at L_max=8.

  PASS iff max_dev ≤ 1e-3.
  INFO iff 1e-3 < max_dev ≤ 1e-2.
  FAIL iff > 1e-2.

Status note: plan §W0-15 cites "W5-64 f_B table" as input, but no
f_B(K) table exists in canonical_constants.py or as a standalone
W5-64 NPZ (grep confirms absent). We implement an analytic f_B(K)
based on the Leggett-Bogoliubov dispersion: for a substrate with
canonical speed c_S_canon = 1 and Bogoliubov amplitude in the
Leggett channel, the mixing coefficient in the framework's
dimensionless convention (W5-D.5) is

  f_B(K) = c_S_canon × (1 − K_R5/K)^{1/2}                       (*)

for K ≥ K_R5, which is the standard Leggett dispersion for a
quasi-1D corridor between K_R5 (corridor floor) and K_crit (wall).
Plan W5-D.5 conjectures the IDENTITY f_B(K) ≡ c_S_canon — which
under (*) holds only at K → ∞. On the plan's finite K range
[K_R5, K_crit=2.0446], (*) gives f_B(K) < c_S_canon in all K, so
a strict interpretation FAILS the 1e-3 tolerance.

We evaluate both interpretations:
  (i) strict: f_B(K) via (*); max_dev = c_S_canon − f_B(K_R5) ≈ 1
  (ii) canonical: f_B(K) ≡ c_S_canon by W5-D.5 definition (identity
       conjecture as structural statement): max_dev = 0

And report both. Primary verdict uses (i) — strict dispersion —
since the purpose of the identity test is to check whether the
dispersion COLLAPSES to c_S_canon, not to assume it.

Classification: PHONONIC
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

import hashlib, json, sys, time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-CSCANON-IDENTITY-TEST"                        # (local)
SCHEME = "Leggett-Bogoliubov"                                # (local)
CONVENTION = "W5-D.5"                                        # (local)
L_MAX = 8                                                    # (local)

# Plan pins (NOTE plan K_crit=2.0446 differs from canonical K_crit=91.5; use plan value)
K_CRIT_PLAN = 2.0446                                         # (local) plan §W0-15
N_K = 50                                                     # (local)

PASS_ABS = 1e-3                                              # (local)
INFO_ABS = 1e-2                                              # (local)

OUT_NPZ = resolve_output(85, 's85_w0_fB_cScanon_identity.npz')
OUT_PNG = resolve_output(85, 's85_w0_fB_cScanon_identity.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


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


def compute():
    print("--- Section 5: f_B = c_S_canon identity test ---")
    K_grid = np.linspace(K_R5, K_CRIT_PLAN, N_K)  # (local)
    # Interpretation (i) strict: f_B(K) = c_S_canon × sqrt(1 - K_R5/K)
    # Note: at K = K_R5, 1 - K_R5/K_R5 = 0 → f_B = 0 (corridor floor)
    # At K → ∞, f_B → c_S_canon
    f_B_strict = c_S_canon * np.sqrt(np.maximum(1.0 - K_R5 / K_grid, 0.0))  # (local)
    dev_strict = np.abs(f_B_strict - c_S_canon)  # (local)
    max_dev_strict = float(np.max(dev_strict))  # (local)

    # Interpretation (ii) W5-D.5 canonical identity: f_B(K) ≡ c_S_canon
    f_B_identity = np.full_like(K_grid, c_S_canon)  # (local)
    max_dev_identity = float(np.max(np.abs(f_B_identity - c_S_canon)))  # (local) = 0

    print(f"  K_grid: linspace({K_R5}, {K_CRIT_PLAN}, {N_K})")
    print(f"  c_S_canon = {c_S_canon}")
    print(f"  K_R5 = {K_R5}")
    print(f"  K_crit (plan §W0-15) = {K_CRIT_PLAN}")
    print(f"  NOTE: canonical_constants.py K_crit = 91.5 (different from plan)")
    print()
    print(f"  Interpretation (i) strict dispersion f_B = sqrt(1 - K_R5/K):")
    print(f"    f_B range: [{float(f_B_strict[0]):.6f}, {float(f_B_strict[-1]):.6f}]")
    print(f"    max|f_B - c_S_canon|: {max_dev_strict:.6f}  (vs PASS tol 1e-3)")
    print(f"  Interpretation (ii) W5-D.5 identity conjecture f_B ≡ c_S_canon:")
    print(f"    max|f_B - c_S_canon|: {max_dev_identity:.6e}")

    return dict(
        value=max_dev_strict,  # strict interpretation is the primary test
        K_grid=K_grid,
        f_B_strict=f_B_strict,
        f_B_identity=f_B_identity,
        dev_strict=dev_strict,
        max_dev_strict=max_dev_strict,
        max_dev_identity=max_dev_identity,
        c_S_canon=c_S_canon,
        K_R5=K_R5,
        K_CRIT_PLAN=K_CRIT_PLAN,
    )


def evaluate_gate(result):
    d = result["max_dev_strict"]
    if d <= PASS_ABS:
        return "PASS"
    if d <= INFO_ABS:
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
        K_grid=result["K_grid"],
        f_B_strict=result["f_B_strict"],
        f_B_identity=result["f_B_identity"],
        dev_strict=result["dev_strict"],
        max_dev_strict=result["max_dev_strict"],
        max_dev_identity=result["max_dev_identity"],
        c_S_canon=result["c_S_canon"],
        K_R5=result["K_R5"],
        K_CRIT_PLAN=result["K_CRIT_PLAN"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def save_png(result):
    fig, ax = plt.subplots(figsize=(8, 5))
    K = result["K_grid"]
    ax.plot(K, result["f_B_strict"], "-o", ms=3, label="f_B(K) strict (Leggett-Bogoliubov dispersion)")
    ax.axhline(result["c_S_canon"], color="red", ls="--",
               label=f"c_S_canon = {result['c_S_canon']}")
    ax.axhline(result["c_S_canon"] + PASS_ABS, color="green", ls=":",
               alpha=0.5, label=f"PASS band ±{PASS_ABS}")
    ax.axhline(result["c_S_canon"] - PASS_ABS, color="green", ls=":", alpha=0.5)
    ax.set_xlabel("K (corridor parameter)")
    ax.set_ylabel("f_B(K)")
    ax.set_title(f"S85 W0-15: f_B = c_S_canon identity (max_dev = {result['max_dev_strict']:.4f})")
    ax.legend(loc="best")
    ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
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
    save_png(result)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    wall = time.time() - t0
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
