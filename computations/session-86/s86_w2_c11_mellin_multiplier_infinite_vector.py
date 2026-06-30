#!/usr/bin/env python3
"""
S86 W2-C11 — Mellin Multiplier INFINITE-VECTOR Extension
========================================================

Gate: S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION ([VERIFY])

Pre-registered threshold:
  PASS iff max_rel_err <= 1e-12 across all 8 sample points
        s in {0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0}
        AND framework note exists with §1-§4 substantive content (>= 25 lines)
  FAIL iff any rel_err > 1e-12 OR framework note absent / stub
  NO INFO band (closed-form analytic identity).

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - script bytes
  (No D_K cache; no upstream .npz; closed-form symbolic verification.)

Output 4-tuple:
  (value=max_rel_err, scheme=analytic-Mellin, convention=closed-form-verification, L_max=NA)

Classification: GEOMETRIC

METHODOLOGY
-----------
Computes the analytic Mellin transform of the Zubarev kernel
f_Z(x) = exp(-x / Lambda_Z^2) at 8 sample points s in {0.5, 1.0, ..., 4.0}
via mp.quad at workdps=50, and compares against the closed-form identity
M[f_Z](s) = Lambda_Z^{2s} * Gamma(s) (Erdelyi 1953; substitution u = x/Lambda_Z^2).

Cross-checks:
  (i)   M[f_Z](1) = Lambda_Z^2
  (ii)  M[f_Z](2) = Lambda_Z^4
  (iii) Recurrence M[f_Z](s+1) / M[f_Z](s) = Lambda_Z^2 * s

Embeds Zubarev as the INFINITE-VECTOR class extending Lizzi S-1's finite-vector
F_4 formalism. The asymmetry is formalized in
sessions/framework/registry/lizzi-finite-infinite-vector-classification.md.

DISCIPLINE
----------
- from canonical_constants import * (M_KK as the Lambda_Z scale anchor)
- workdps = 50 (mpmath, deterministic)
- All intermediates tagged # (local)
- audit_sha256 + content_sha256 (S84+ dual-SHA schema)
- Lambda_Z = 1.0 in M_KK units (S83 G14 / G1 convention; checked also at
  Lambda_Z = 2.5 to verify the identity's dependence on the scale parameter)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants
# ---------------------------------------------------------------------------
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

os.environ.setdefault("OMP_NUM_THREADS", "8")  # defensive CPU pin
os.environ.setdefault("MKL_NUM_THREADS", "8")  # defensive CPU pin

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from mpmath import mp, mpf, mpc, gamma, quad, exp as mp_exp, power as mp_power

mp.dps = 50  # workdps = 50 throughout

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"                                                 # (local)
GATE_ID = "S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION"     # (local)
SCHEME = "analytic-Mellin"                                       # (local)
CONVENTION = "closed-form-verification"                          # (local)
L_MAX = "NA"                                                     # (local)

# Pre-registered: max_rel_err <= 1e-12 across all 8 sample points
PASS_THRESHOLD_REL_ERR = 1e-12                                   # (local)
N_EVAL = 50                                                      # (local) mpmath workdps
S_SAMPLES = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0)             # (local)

# Lambda_Z choice: 1.0 in M_KK units (S83 G14 / G1 convention);
# also verified at Lambda_Z = 2.5 to assert the identity's
# scale-parameter dependence (a 2nd anchor for the closed form).
LAMBDA_Z_PRIMARY = mpf("1.0")                                    # (local) M_KK units
LAMBDA_Z_SECONDARY = mpf("2.5")                                  # (local) cross-check anchor

# Output destinations
OUT_NPZ = resolve_output(86, 's86_w2_c11_mellin_table.npz')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""        # (local)
    canonical_bytes = b""     # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def mellin_zubarev_numerical(s_val: float, Lambda_Z) -> mpc:
    """Numerical Mellin transform of f_Z(x) = exp(-x / Lambda_Z^2).

    M[f_Z](s) = int_0^inf x^{s-1} exp(-x / Lambda_Z^2) dx
    Computed by mp.quad on a semi-infinite contour [0, inf].
    """
    s_mp = mpf(s_val)                                            # (local)
    Lz2 = Lambda_Z ** 2                                          # (local)
    integrand = lambda x: (x ** (s_mp - 1)) * mp_exp(-x / Lz2)   # (local)
    # mp.quad handles improper integrals on [0, inf] via tanh-sinh.
    val = quad(integrand, [0, mp.inf])                           # (local)
    return val


def mellin_zubarev_closed_form(s_val: float, Lambda_Z) -> mpc:
    """Closed form: Lambda_Z^{2s} * Gamma(s)."""
    s_mp = mpf(s_val)                                            # (local)
    return mp_power(Lambda_Z, 2 * s_mp) * gamma(s_mp)


def compute() -> dict:
    """Run 8-point sweep at LAMBDA_Z_PRIMARY; cross-check secondary anchor.

    Returns:
      dict with 'value' = max_rel_err over 8 samples (primary anchor),
      'samples_primary' / 'samples_secondary' table arrays,
      'cross_checks' dict.
    """
    # --- Primary sweep: Lambda_Z = 1.0 (M_KK units) ---
    rows_primary = []  # (local) list of (s, num_re, num_im, cf_re, cf_im, rel_err)
    print(f"\n=== Primary sweep: Lambda_Z = {LAMBDA_Z_PRIMARY} (M_KK units) ===")
    print(f"  workdps = {mp.dps}")
    print(f"  s in {S_SAMPLES}")
    print()
    print(f"  {'s':>5}  {'num':>30}  {'closed-form':>30}  {'rel_err':>14}")
    for s_val in S_SAMPLES:
        num_val = mellin_zubarev_numerical(s_val, LAMBDA_Z_PRIMARY)        # (local)
        cf_val = mellin_zubarev_closed_form(s_val, LAMBDA_Z_PRIMARY)       # (local)
        # Relative error |num - cf| / |cf|
        diff = abs(num_val - cf_val)                                       # (local)
        denom = abs(cf_val)                                                # (local)
        rel_err = float(diff / denom) if denom > 0 else float(diff)         # (local)
        rows_primary.append((
            float(s_val),
            float(mp.re(num_val)), float(mp.im(num_val)),
            float(mp.re(cf_val)), float(mp.im(cf_val)),
            rel_err,
        ))
        print(f"  {s_val:>5.2f}  {mp.nstr(num_val, 18):>30}  "
              f"{mp.nstr(cf_val, 18):>30}  {rel_err:>14.3e}")

    rel_errs_primary = [r[5] for r in rows_primary]                        # (local)
    max_rel_err_primary = max(rel_errs_primary)                            # (local)

    # --- Secondary anchor: Lambda_Z = 2.5 ---
    rows_secondary = []  # (local)
    print(f"\n=== Secondary anchor: Lambda_Z = {LAMBDA_Z_SECONDARY} ===")
    print(f"  {'s':>5}  {'num':>30}  {'closed-form':>30}  {'rel_err':>14}")
    for s_val in S_SAMPLES:
        num_val = mellin_zubarev_numerical(s_val, LAMBDA_Z_SECONDARY)      # (local)
        cf_val = mellin_zubarev_closed_form(s_val, LAMBDA_Z_SECONDARY)     # (local)
        diff = abs(num_val - cf_val)                                       # (local)
        denom = abs(cf_val)                                                # (local)
        rel_err = float(diff / denom) if denom > 0 else float(diff)         # (local)
        rows_secondary.append((
            float(s_val),
            float(mp.re(num_val)), float(mp.im(num_val)),
            float(mp.re(cf_val)), float(mp.im(cf_val)),
            rel_err,
        ))
        print(f"  {s_val:>5.2f}  {mp.nstr(num_val, 18):>30}  "
              f"{mp.nstr(cf_val, 18):>30}  {rel_err:>14.3e}")

    rel_errs_secondary = [r[5] for r in rows_secondary]                    # (local)
    max_rel_err_secondary = max(rel_errs_secondary)                        # (local)

    # --- Cross-checks ---
    print("\n=== Cross-checks ===")

    # (i) M[f_Z](s=1) = Lambda_Z^2 * Gamma(1) = Lambda_Z^2
    cc_i_primary_num = mellin_zubarev_numerical(1.0, LAMBDA_Z_PRIMARY)     # (local)
    cc_i_primary_target = LAMBDA_Z_PRIMARY ** 2                            # (local)
    cc_i_primary_err = float(abs(cc_i_primary_num - cc_i_primary_target) /
                              abs(cc_i_primary_target))                    # (local)
    cc_i_secondary_num = mellin_zubarev_numerical(1.0, LAMBDA_Z_SECONDARY) # (local)
    cc_i_secondary_target = LAMBDA_Z_SECONDARY ** 2                        # (local)
    cc_i_secondary_err = float(abs(cc_i_secondary_num - cc_i_secondary_target) /
                                abs(cc_i_secondary_target))                # (local)
    print(f"  (i) M[f_Z](1) = Lambda_Z^2:")
    print(f"      Lambda_Z=1.0:  num={mp.nstr(cc_i_primary_num, 18)}  "
          f"target={mp.nstr(cc_i_primary_target, 18)}  rel_err={cc_i_primary_err:.3e}")
    print(f"      Lambda_Z=2.5:  num={mp.nstr(cc_i_secondary_num, 18)}  "
          f"target={mp.nstr(cc_i_secondary_target, 18)}  rel_err={cc_i_secondary_err:.3e}")

    # (ii) M[f_Z](s=2) = Lambda_Z^4 * Gamma(2) = Lambda_Z^4
    cc_ii_primary_num = mellin_zubarev_numerical(2.0, LAMBDA_Z_PRIMARY)    # (local)
    cc_ii_primary_target = LAMBDA_Z_PRIMARY ** 4                           # (local)
    cc_ii_primary_err = float(abs(cc_ii_primary_num - cc_ii_primary_target) /
                               abs(cc_ii_primary_target))                  # (local)
    cc_ii_secondary_num = mellin_zubarev_numerical(2.0, LAMBDA_Z_SECONDARY)# (local)
    cc_ii_secondary_target = LAMBDA_Z_SECONDARY ** 4                       # (local)
    cc_ii_secondary_err = float(abs(cc_ii_secondary_num - cc_ii_secondary_target) /
                                 abs(cc_ii_secondary_target))              # (local)
    print(f"  (ii) M[f_Z](2) = Lambda_Z^4:")
    print(f"      Lambda_Z=1.0:  num={mp.nstr(cc_ii_primary_num, 18)}  "
          f"target={mp.nstr(cc_ii_primary_target, 18)}  rel_err={cc_ii_primary_err:.3e}")
    print(f"      Lambda_Z=2.5:  num={mp.nstr(cc_ii_secondary_num, 18)}  "
          f"target={mp.nstr(cc_ii_secondary_target, 18)}  rel_err={cc_ii_secondary_err:.3e}")

    # (iii) Recurrence: M[f_Z](s+1) / M[f_Z](s) = Lambda_Z^2 * s
    print(f"  (iii) Recurrence M[f_Z](s+1) / M[f_Z](s) = Lambda_Z^2 * s:")
    recurrence_errs = []  # (local)
    for s_val in (0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5):
        m_s = mellin_zubarev_closed_form(s_val, LAMBDA_Z_PRIMARY)          # (local)
        m_sp1 = mellin_zubarev_closed_form(s_val + 1.0, LAMBDA_Z_PRIMARY)  # (local)
        ratio = m_sp1 / m_s                                                # (local)
        target = (LAMBDA_Z_PRIMARY ** 2) * mpf(s_val)                      # (local)
        rec_err = float(abs(ratio - target) / abs(target))                 # (local)
        recurrence_errs.append((float(s_val), rec_err))
        print(f"      s={s_val:.2f}: ratio={mp.nstr(ratio, 18)}  "
              f"target={mp.nstr(target, 18)}  rel_err={rec_err:.3e}")
    max_rec_err = max(e for _, e in recurrence_errs)                       # (local)

    # Aggregate value: max_rel_err over PRIMARY 8-point sweep
    # (this is the registered output per plan §8 expected output 4-tuple)
    value = max_rel_err_primary

    return {
        "value": value,
        "samples_primary": np.array(rows_primary, dtype=float),
        "samples_secondary": np.array(rows_secondary, dtype=float),
        "max_rel_err_primary": max_rel_err_primary,
        "max_rel_err_secondary": max_rel_err_secondary,
        "cc_i_primary_err": cc_i_primary_err,
        "cc_i_secondary_err": cc_i_secondary_err,
        "cc_ii_primary_err": cc_ii_primary_err,
        "cc_ii_secondary_err": cc_ii_secondary_err,
        "recurrence_errs": recurrence_errs,
        "max_rec_err": max_rec_err,
        "Lambda_Z_primary": float(LAMBDA_Z_PRIMARY),
        "Lambda_Z_secondary": float(LAMBDA_Z_SECONDARY),
        "s_samples": np.array(S_SAMPLES, dtype=float),
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def evaluate_gate(value: float, framework_note_path: Path) -> str:
    """PASS iff max_rel_err <= 1e-12 AND framework note exists with >=25 substantive lines.
       FAIL otherwise. NO INFO band.
    """
    # Numerical reproducibility
    num_pass = value <= PASS_THRESHOLD_REL_ERR  # (local)

    # Framework note existence + content
    note_pass = False  # (local)
    note_lines = 0     # (local)
    if framework_note_path.exists():
        try:
            content = framework_note_path.read_text(encoding="utf-8")  # (local)
            # Count non-empty, non-pure-whitespace lines
            note_lines = sum(
                1 for ln in content.splitlines() if ln.strip()
            )
            note_pass = note_lines >= 25
        except OSError:
            note_pass = False

    print(f"\n=== Gate evaluation ===")
    print(f"  max_rel_err = {value:.6e}  threshold = {PASS_THRESHOLD_REL_ERR:.0e}  "
          f"=> {'PASS' if num_pass else 'FAIL'}")
    print(f"  framework note: {framework_note_path}")
    print(f"  note exists: {framework_note_path.exists()}  "
          f"substantive lines: {note_lines}  "
          f"=> {'PASS' if note_pass else 'FAIL'}")

    if num_pass and note_pass:
        return "PASS"
    return "FAIL"


def append_verdict(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    # Companion comment row with audit_sha (pre-S86 dual-row style)
    comment = (
        f"# {GATE_ID} audit_sha256={audit_sha} content_sha256={content_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # 1b. Dual-SHA
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    # 2. Compute
    result = compute()
    value = result["value"]

    # 3. Persist .npz table
    np.savez(
        OUT_NPZ,
        s_samples=result["s_samples"],
        samples_primary=result["samples_primary"],
        samples_secondary=result["samples_secondary"],
        Lambda_Z_primary=result["Lambda_Z_primary"],
        Lambda_Z_secondary=result["Lambda_Z_secondary"],
        max_rel_err_primary=result["max_rel_err_primary"],
        max_rel_err_secondary=result["max_rel_err_secondary"],
        max_rec_err=result["max_rec_err"],
    )
    print(f"\n  Saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # 4. Evaluate gate (requires framework note on disk)
    framework_note = (
        PROJECT_ROOT / "sessions" / "framework"
        / "lizzi-finite-infinite-vector-classification.md"
    )
    verdict = evaluate_gate(value, framework_note)

    # 5. Emit 4-tuple + append verdict
    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, value, audit_sha, content_sha)

    # 6. Summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
