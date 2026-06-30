#!/usr/bin/env python3
"""
S86 W2 C10 — S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE ([VERIFY])

Verification driver for the new analytic_zeta(s, L_max) API
(see computations/_shared/_analytic_zeta.py).

PASS criteria (plan §W2-2 §9, both must hold):
  (a) analytic_zeta(s=3, L_max=10) finite (no NaN, no overflow, |result| < 1e10)
  (b) chi^2/dof <= 5 against direct subtraction across the 5-point sweep
      s in {2.5, 2.75, 3.0, 3.25, 3.5}, dof = 5 - 1 = 4

INFO: finite at s=3 but chi^2/dof in (5, 20] OR L_max=8 unstable >5% vs L_max=10
FAIL: non-finite OR chi^2/dof > 20

Cross-checks (plan §6 step 6):
  (i)   L_max=8 within 5% of L_max=10 value (truncation-stability)
  (ii)  s=3+0.001i continuous w/ s=3+0i (analyticity)
  (iii) self-test: analytic_zeta(s = 4 - 0.01, L_max=10) does NOT diverge
        but is large (near-pole asymptote of the SD residue at s=4)

Classification: GEOMETRIC (the analytic continuation is intrinsic to the
spectral triple's heat-kernel / zeta-function correspondence; off-pole
evaluation is a property of D_K's spectral measure).
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
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ─── W6-71 Mellin discipline markers (S86 W0c-6 retrofit) ───
# MELLIN-CONVERGENCE-STRIP: 2 < Re(s) < 4   # off-pole strip around s*=3
# MELLIN-RESIDUE-EXTRACTION: not_applicable_at_off_pole   # s*=3 is off-pole
# MELLIN-COUNTERTERM-SUBTRACTION: not_applicable_at_off_pole
# MELLIN-ANALYTIC-CONTINUATION-PATH: real-axis_Re(s)=3
# MELLIN-CLOSURE-VERIFICATION: identity_with_direct_Dirichlet_at_finite_L_max
# ─────────────────────────────────────────────────────────────

import hashlib
import json
import sys
import time
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# canonical_constants is a hard requirement for all S34+ computation scripts.
from canonical_constants import d_spec, tau_fold  # noqa: F401

# Local infrastructure module.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from _analytic_zeta import analytic_zeta, zeta_D_direct, load_spectrum

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE"
SCHEME = "analytic-continuation"
CONVENTION = "off-pole-Hankel"
L_MAX = 10  # (local) canonical evaluation L_max (plan §7 PRDR)
L_MAX_XCHECK = 8  # (local) cross-check L_max for truncation-stability (plan §7)

S_STAR = 3.0  # (local) primary off-pole evaluation point (plan §7 s_evaluation)
S_SWEEP = [2.5, 2.75, 3.0, 3.25, 3.5]  # (local) 5-point off-pole sweep
DOF = len(S_SWEEP) - 1  # (local) 5 - 1 = 4

PASS_CHI2_DOF = 5.0  # (local) PASS threshold from plan §9
INFO_CHI2_DOF = 20.0  # (local) INFO upper bound from plan §9
PASS_FINITE_MAX = 1e10  # (local) finiteness bound from plan §9
PASS_TRUNC_STABILITY = 0.05  # (local) 5% L_max=8 vs L_max=10 from plan §6
PASS_ANALYTIC_TOL = 1e-3  # (local) analyticity 1e-3 at s=3+0.001i

OUT_NPZ = resolve_output(86, 's86_w2_c10_zeta_sweep.npz')
OUT_PNG = resolve_output(86, 's86_w2_c10_compare.png')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_script(None, '_analytic_zeta.py'),
    resolve_output(84, 's84_spectrum_cache_L12_tau019.npz'),
]

# Soft prerequisite: C9 PASS (plan §6). If absent, dispatch C10 anyway and
# flag the dependency state in the cross-check section.
C9_RESIDUES_PATH = resolve_output(86, 's86_w2_c9_residues.npz')


def sha256_of(p: Path) -> str:
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


def compute_dual_sha(script: Path, canonical: Path, pins: dict):
    sb = script.read_bytes()
    cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())),
                    separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def run_sweep():
    """5-point off-pole sweep at L_max=10."""
    print("--- Section 5a: 5-point off-pole sweep at L_max=10 ---")
    rows = []
    for s in S_SWEEP:
        sc = complex(s, 0.0)
        t0 = time.time()
        zeta_an = analytic_zeta(sc, L_MAX)
        zeta_dr = zeta_D_direct(sc, L_MAX)
        wall = time.time() - t0
        diff_abs = abs(zeta_an - zeta_dr)
        diff_rel = diff_abs / max(abs(zeta_dr), 1e-30)
        rows.append((s, zeta_an, zeta_dr, diff_abs, diff_rel, wall))
        print(f"  s={s:.3f}: an={zeta_an.real:+.6e}  dr={zeta_dr.real:+.6e}  "
              f"|delta|={diff_abs:.3e}  rel={diff_rel:.3e}  wall={wall:.1f}s")
    return rows


def run_truncation_stability():
    """L_max=8 vs L_max=10 cross-check at s=3."""
    print("--- Section 5b: truncation-stability L_max=8 vs L_max=10 at s=3 ---")
    z10 = analytic_zeta(complex(S_STAR, 0.0), L_MAX)
    z8 = analytic_zeta(complex(S_STAR, 0.0), L_MAX_XCHECK)
    rel = abs(z10 - z8) / max(abs(z10), 1e-30)
    print(f"  analytic_zeta(3, 10) = {z10}")
    print(f"  analytic_zeta(3,  8) = {z8}")
    print(f"  relative shift       = {rel:.6e}  (threshold 5%)")
    return z10, z8, rel


def run_analyticity_check():
    """s=3+0.001i continuous w/ s=3+0i."""
    print("--- Section 5c: analyticity check at s=3 vs s=3+0.001i ---")
    z_real = analytic_zeta(complex(S_STAR, 0.0), L_MAX)
    z_eps = analytic_zeta(complex(S_STAR, 1e-3), L_MAX)
    rel = abs(z_real - z_eps) / max(abs(z_real), 1e-30)
    print(f"  analytic_zeta(3+0i)     = {z_real}")
    print(f"  analytic_zeta(3+0.001i) = {z_eps}")
    print(f"  relative shift          = {rel:.6e}  (tol 1e-3)")
    return z_real, z_eps, rel


def run_pole_self_test():
    """Self-test: analytic_zeta near s=4 (SD pole) should be large but finite
    via the Hankel deformation (1e-6 imaginary epsilon)."""
    print("--- Section 5d: near-pole self-test at s = 4 - 0.01 ---")
    s_near = complex(4.0 - 0.01, 0.0)
    z_near = analytic_zeta(s_near, L_MAX)
    z_at_3 = analytic_zeta(complex(S_STAR, 0.0), L_MAX)
    ratio = abs(z_near) / max(abs(z_at_3), 1e-30)
    print(f"  analytic_zeta(3.99, 10)    = {z_near}")
    print(f"  ratio |z(3.99)|/|z(3)|    = {ratio:.3e}")
    return z_near, ratio


def chi2_dof(rows, sigma_floor):
    """chi^2/dof against direct subtraction.

    sigma(s) = max( |an(s, 8) - an(s, 10)|, 1e-12 ) per plan §10.
    """
    print("--- Section 5e: chi^2/dof against direct subtraction ---")
    chi2 = 0.0  # (local) chi-squared accumulator
    for (s, zeta_an, zeta_dr, diff_abs, diff_rel, _wall), sigma in zip(rows, sigma_floor):
        # Cast to real residual since the off-pole sweep is on the real axis.
        resid = float((zeta_an - zeta_dr).real)
        norm_resid = resid / max(sigma, 1e-12)
        chi2 += norm_resid * norm_resid
        print(f"  s={s:.3f}: resid={resid:+.3e}  sigma={sigma:.3e}  "
              f"normalized={norm_resid:+.3e}")
    chi2_per_dof = chi2 / DOF
    print(f"  chi^2 = {chi2:.6e}, dof = {DOF}, chi^2/dof = {chi2_per_dof:.6e}")
    return chi2, chi2_per_dof


def compute_truncation_sigmas():
    """sigma(s) = |an(s, 8) - an(s, 10)| for each sweep point (plan §10)."""
    print("--- Section 5f: truncation-noise sigma per sweep point ---")
    sigmas = []
    z10_per_s = []
    z8_per_s = []
    for s in S_SWEEP:
        sc = complex(s, 0.0)
        z10 = analytic_zeta(sc, L_MAX)
        z8 = analytic_zeta(sc, L_MAX_XCHECK)
        z10_per_s.append(z10)
        z8_per_s.append(z8)
        sigma = max(abs(z10 - z8), 1e-12)
        sigmas.append(sigma)
        print(f"  s={s:.3f}: |an(s,8)-an(s,10)| = {sigma:.3e}")
    return sigmas, z10_per_s, z8_per_s


def make_plot(rows, sigmas, z10_per_s, z8_per_s, chi2_per_dof, verdict):
    fig, ax = plt.subplots(2, 1, figsize=(8, 8))

    s_arr = np.array([r[0] for r in rows])
    an_arr = np.array([float(r[1].real) for r in rows])
    dr_arr = np.array([float(r[2].real) for r in rows])
    rel_arr = np.array([float(r[4]) for r in rows])
    sigma_arr = np.array(sigmas)

    ax[0].semilogy(s_arr, np.abs(an_arr), "o-", label="analytic_zeta (Mellin)")
    ax[0].semilogy(s_arr, np.abs(dr_arr), "s--", label="zeta_D_direct (Dirichlet)")
    ax[0].axvspan(1.95, 2.05, alpha=0.15, color="red", label="grav pole s=2")
    ax[0].axvspan(3.95, 4.05, alpha=0.15, color="red", label="SD pole s=4")
    ax[0].axvline(S_STAR, color="green", ls=":", label=f"off-pole s={S_STAR}")
    ax[0].set_xlabel("s")
    ax[0].set_ylabel("|zeta_D(s)|")
    ax[0].set_title(f"S86 C10: analytic_zeta vs direct truncation (L_max={L_MAX})")
    ax[0].legend(loc="best", fontsize=9)
    ax[0].grid(True, which="both", alpha=0.3)

    ax[1].semilogy(s_arr, rel_arr + 1e-300, "o-", color="darkblue",
                   label="relative deviation (an vs direct)")
    ax[1].semilogy(s_arr, sigma_arr / np.abs(an_arr), "s--", color="darkred",
                   label="truncation noise sigma / |an|")
    ax[1].axvline(S_STAR, color="green", ls=":")
    ax[1].set_xlabel("s")
    ax[1].set_ylabel("relative magnitude")
    ax[1].set_title(f"chi^2/dof = {chi2_per_dof:.3e}  -->  verdict: {verdict}")
    ax[1].legend(loc="best", fontsize=9)
    ax[1].grid(True, which="both", alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close()
    print(f"  plot written: {OUT_PNG.relative_to(PROJECT_ROOT)}")


def evaluate_gate(z10_at_3, chi2_per_dof, trunc_rel, analytic_rel, near_pole_finite):
    """PASS / INFO / FAIL per plan §9."""
    finite = (np.isfinite(z10_at_3.real)
              and np.isfinite(z10_at_3.imag)
              and abs(z10_at_3) < PASS_FINITE_MAX)
    chi_pass = chi2_per_dof <= PASS_CHI2_DOF
    chi_info = (PASS_CHI2_DOF < chi2_per_dof <= INFO_CHI2_DOF)
    trunc_pass = trunc_rel <= PASS_TRUNC_STABILITY
    analytic_pass = analytic_rel <= PASS_ANALYTIC_TOL

    if not finite:
        return "FAIL", "non-finite at s=3"
    if chi2_per_dof > INFO_CHI2_DOF:
        return "FAIL", f"chi^2/dof={chi2_per_dof:.3e} > {INFO_CHI2_DOF}"
    if not near_pole_finite:
        return "FAIL", "near-pole self-test diverged unphysically"
    if chi_info or not trunc_pass or not analytic_pass:
        return "INFO", (
            f"chi^2/dof={chi2_per_dof:.3e} (PASS<=5, INFO<=20); "
            f"trunc={trunc_rel:.3e} (PASS<=5%); "
            f"analytic={analytic_rel:.3e} (PASS<=1e-3)"
        )
    return "PASS", (
        f"chi^2/dof={chi2_per_dof:.3e}<=5; finite |z(3,10)|={abs(z10_at_3):.3e}<1e10; "
        f"trunc={trunc_rel:.3e}; analytic={analytic_rel:.3e}"
    )


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} sha256={audit_sha}\n"
    )
    comment = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256={content_sha} "
        f"audit_sha256={audit_sha}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(comment)


def save_npz(rows, z10_at_3, z8_at_3, trunc_rel, z_eps, analytic_rel,
             z_near, near_pole_ratio, sigmas, chi2, chi2_per_dof,
             c9_pin, audit_sha, content_sha):
    s_arr = np.array([r[0] for r in rows])
    an_arr = np.array([complex(r[1]) for r in rows])
    dr_arr = np.array([complex(r[2]) for r in rows])
    diff_abs = np.array([float(r[3]) for r in rows])
    diff_rel = np.array([float(r[4]) for r in rows])
    sigma_arr = np.array(sigmas)
    np.savez_compressed(
        OUT_NPZ,
        s_sweep=s_arr,
        analytic_zeta_sweep=an_arr,
        direct_zeta_sweep=dr_arr,
        diff_abs=diff_abs,
        diff_rel=diff_rel,
        sigma_truncation=sigma_arr,
        chi2=chi2,
        chi2_per_dof=chi2_per_dof,
        z10_at_3=complex(z10_at_3),
        z8_at_3=complex(z8_at_3),
        truncation_rel_shift=trunc_rel,
        z_at_3_eps=complex(z_eps),
        analytic_rel_shift=analytic_rel,
        z_near_pole=complex(z_near),
        near_pole_ratio=near_pole_ratio,
        c9_dependency_status=c9_pin,
        L_max=L_MAX,
        L_max_xcheck=L_MAX_XCHECK,
        s_star=S_STAR,
        d_spec_NCG_cone_apex=8,
        d_spec_classical_canonical=int(d_spec),
        scheme=SCHEME,
        convention=CONVENTION,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  data written: {OUT_NPZ.relative_to(PROJECT_ROOT)}")


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(),
        resolve_script(None, 'canonical_constants.py'), pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    # Soft prerequisite: C9 PASS — flag in cross-check if absent.
    c9_pin = "absent_at_dispatch_time"
    if C9_RESIDUES_PATH.exists():
        c9_sha = sha256_of(C9_RESIDUES_PATH)
        c9_pin = f"present_sha={c9_sha[:16]}"
        print(f"  C9 prerequisite: {c9_pin}")
    else:
        print(f"  C9 prerequisite: NOT FOUND (concurrent dispatch; flagged in cross-check)")
    print()

    # 1. 5-point off-pole sweep
    rows = run_sweep()

    # 2. Truncation-stability (L_max=8 vs L_max=10)
    z10_at_3, z8_at_3, trunc_rel = run_truncation_stability()

    # 3. Analyticity check (s = 3+0.001i)
    _z_real, z_eps, analytic_rel = run_analyticity_check()

    # 4. Near-pole self-test at s = 4 - 0.01
    z_near, near_pole_ratio = run_pole_self_test()
    near_pole_finite = bool(np.isfinite(abs(z_near)))

    # 5. Truncation-noise sigma per sweep point (plan §10)
    sigmas, z10_sweep, z8_sweep = compute_truncation_sigmas()

    # 6. chi^2/dof against direct subtraction
    chi2, chi2_per_dof = chi2_dof(rows, sigmas)

    # 7. Gate verdict
    verdict, reason = evaluate_gate(z10_at_3, chi2_per_dof, trunc_rel,
                                    analytic_rel, near_pole_finite)

    # 8. Plot + persist
    make_plot(rows, sigmas, z10_sweep, z8_sweep, chi2_per_dof, verdict)
    save_npz(rows, z10_at_3, z8_at_3, trunc_rel, z_eps, analytic_rel,
             z_near, near_pole_ratio, sigmas, chi2, chi2_per_dof,
             c9_pin, audit_sha, content_sha)

    # 9. 4-tuple + verdict line
    tag = (f"(value={complex(z10_at_3)}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print()
    print(f"  4-tuple: {tag}")
    print(f"  verdict reason: {reason}")
    append_verdict(verdict, complex(z10_at_3), audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {time.time()-t0:.1f}s) ===")
    return 0  # all verdicts (PASS / INFO / FAIL) are valid scientific results


if __name__ == "__main__":
    sys.exit(main())
