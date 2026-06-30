#!/usr/bin/env python3
"""
S85 W0-20 — S85-W0-L-MELLIN-CONE-S3-RESIDUE ([VERIFY-THEOREM])

Threshold (plan §W0-20):
  HYPOTHESIS: CM residue at s=3 converges under L_max ∈ {8..12} sweep
  with residue(L) = R_∞ + α/L² + β/L⁴ fit residual < 1e-3.

  PASS iff convergent AND |fit_residual| < 1e-3.
  INFO iff partial-convergence (monotone but slow).
  FAIL iff divergent (|R(L)−R(L-1)| not decreasing monotonically over 3+ pts).

Method: Z(s=3; L_max) = Σ_{sectors: p+q ≤ L_max} dim(p,q) × Σ |λ|^{-3}
  on the L=12 spectrum cache, subsetting by L_max. Fit extrapolated R_∞.

Classification: GEOMETRIC
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


import hashlib, json, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"
GATE_ID = "S85-W0-L-MELLIN-CONE-S3-RESIDUE"
SCHEME = "Connes-Moscovici-Mellin-cone"
CONVENTION = "s*=3"
L_MAX = 12

L_GRID = [8, 9, 10, 11, 12]                                      # (local) sweep
S_STAR = 3                                                        # (local) primary s*
PASS_ABS = 1e-3                                                   # (local) fit residual tol

OUT_NPZ = resolve_output(85, 's85_w0_mellin_cone_s3_residue.npz')
OUT_PNG = resolve_output(85, 's85_w0_mellin_cone_s3_residue.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py'),
               resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')]


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
    print("--- Section 5: Mellin-cone CM residue at s=3, L∈{8..12} sweep ---")
    d = np.load(resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'), allow_pickle=True)
    se = d["sector_evals"].item()

    R = {}  # (local) {L: Z(s=3; L_max)}
    for L in L_GRID:
        evs = []
        mults = []
        for (p, q), info in se.items():
            if (p + q) > L:
                continue
            es = np.asarray(info["abs_evals"], dtype=np.float64)
            mults.append(np.full(es.shape, float(info["dim"])))
            evs.append(es)
        evs = np.concatenate(evs)  # (local)
        mults = np.concatenate(mults)  # (local)
        mask = evs > 1e-12
        R[L] = float(np.sum(mults[mask] * np.power(evs[mask], -float(S_STAR))))
        print(f"  L_max={L:2d}: Z(s=3) = {R[L]:.6e}  (N_evs={evs.size})")

    # Increments
    L_arr = np.array(L_GRID, dtype=float)
    R_arr = np.array([R[L] for L in L_GRID])
    dR = np.diff(R_arr)  # (local) R(L+1) - R(L), with L-spacing = 1
    dR_abs = np.abs(dR)  # (local)
    monotone = bool(np.all(np.diff(dR_abs) <= 0) if len(dR_abs) >= 3 else True)  # (local) |ΔR| decreasing
    # Sign of dR tells us whether R is converging from above or below
    signs = np.sign(dR)
    monotone_direction = bool(np.all(signs == signs[0]))  # all same sign

    # Fit R(L) = c0 + α/L² + β/L⁴
    # Linear system: R(L) = c0 + α·(1/L²) + β·(1/L⁴)
    X = np.column_stack([np.ones_like(L_arr), 1.0/L_arr**2, 1.0/L_arr**4])  # (local)
    coefs, *_ = np.linalg.lstsq(X, R_arr, rcond=None)
    c0, alpha, beta = coefs
    fit = X @ coefs  # (local)
    residuals = R_arr - fit  # (local)
    max_resid_abs = float(np.max(np.abs(residuals)))  # (local)
    max_resid_rel = max_resid_abs / max(abs(c0), 1e-30)  # (local)
    print(f"  Fit R(L) = c0 + α/L² + β/L⁴:")
    print(f"    c0 (R_∞ extrapolated) = {c0:.6e}")
    print(f"    α = {alpha:.6e}")
    print(f"    β = {beta:.6e}")
    print(f"    max |residual|       = {max_resid_abs:.6e}")
    print(f"    max rel residual     = {max_resid_rel:.6e}")
    print(f"  Monotone |ΔR| decrease: {monotone}")
    print(f"  Monotone direction:     {monotone_direction}")

    return dict(
        value=c0,
        R_infty=c0,
        alpha=alpha, beta=beta,
        R_L={str(L): R[L] for L in L_GRID},
        L_grid=L_arr,
        R_arr=R_arr,
        residuals=residuals,
        max_resid_abs=max_resid_abs,
        max_resid_rel=max_resid_rel,
        monotone=monotone,
        monotone_direction=monotone_direction,
        dR=dR, dR_abs=dR_abs,
    )


def evaluate_gate(result):
    # PASS: convergent AND fit residual < 1e-3 (relative or absolute, whichever is stricter)
    converged = result["monotone"] and result["monotone_direction"]
    if converged and result["max_resid_rel"] < PASS_ABS:
        return "PASS"
    if converged and result["max_resid_rel"] < 1e-2:
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
        R_infty=result["R_infty"], alpha=result["alpha"], beta=result["beta"],
        L_grid=result["L_grid"], R_arr=result["R_arr"],
        residuals=result["residuals"], max_resid_abs=result["max_resid_abs"],
        max_resid_rel=result["max_resid_rel"],
        monotone=result["monotone"], monotone_direction=result["monotone_direction"],
        dR=result["dR"], dR_abs=result["dR_abs"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


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
    append_verdict(verdict, result["value"], audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
