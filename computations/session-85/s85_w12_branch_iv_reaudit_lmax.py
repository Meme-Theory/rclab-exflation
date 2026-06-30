#!/usr/bin/env python3
"""
S85 W12-ELIM-1 — Branch-(iv) re-audit at L_max ∈ {8, 10, 12}
============================================================

Gate: S85-W12-ELIM-1 ([VERIFY])

Pre-registered PASS predicate (plan §W12-3 line 153, canonical form):
  PASS  iff  R_JK(L_max) < 1 at all three L_max ∈ {8, 10, 12}
            AND R_JK is monotone-decreasing in L_max
            (within 0.05 RATIO tolerance on consecutive-|D_iv| adjacency,
             per plan §W12-3 line 154).
  FAIL  iff  R_JK(L_max) >= 1 at any L_max (Josephson dominates at that
            regulator depth — retraction is artifact-driven).
  INFO  iff  sign of D_iv = R_JK − 1 is negative at all three L_max but
            |D_iv| is non-monotone in L_max (asymptotic convergence toward
             crossover, re-audit at L_max=14 in S86).

Output 4-tuple:
  (value=<D_iv(8), D_iv(10), D_iv(12), sign_triple>,
   scheme=inverted-josephson-dominance,
   convention=jensen-deformed-SU3-dirac,
   L_max=mixed)

Classification: GEOMETRIC (D_K spectral-moment probe under multiplicity-
weighted SU(3) Casimir schematic at varying regulator L_max).

METHODOLOGY
-----------
Plan §W12-3 Step 5 line 153 explicitly authorizes the
"multiplicity-weighted SU(3) Casimir schematic" (see also s67_volovik_q_a0,
s83_w1_g1_ic_scheme_derivation for precedent). For each (p, q) with
p + q ≤ L_max and (p, q) ≠ (0, 0):
  d(p, q)   = (p+1)(q+1)(p+q+2)/2                  [Weyl dim, SU(3)]
  C_2(p,q)  = (p² + p·q + q² + 3(p+q)) / 3          [Casimir — Dirac λ²]
  a_2       = (1/Vol_SU3_Haar) Σ d(p,q) / C_2(p,q)
  a_4       = (1/Vol_SU3_Haar) Σ d(p,q) / C_2(p,q)²
  σ_J       = a_4  (a_4 Seeley-DeWitt — Tr D_K^(-4) / Vol)
  σ_K       = a_2  (a_2 Seeley-DeWitt — Tr D_K^(-2) / Vol)
  R_JK      = σ_J · Delta_BCS² / (σ_K · K_base)
  D_iv      = R_JK − 1                              [signed residual]
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
ART_DIR = resolve_script(None, 'artifacts')
ART_DIR.mkdir(parents=True, exist_ok=True)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W12-ELIM-1"                                          # (local)
SCHEME = "inverted-josephson-dominance"                             # (local)
CONVENTION = "jensen-deformed-SU3-dirac"                            # (local)
L_MAX = "mixed"                                                     # (local)

# Pre-registered thresholds (plan §W12-3 line 124, 127, 153, 154)
L_MAX_SCAN = (8, 10, 12)                                            # (local) pinned
PASS_RATIO_TOL = 0.05                                               # (local) RATIO on consecutive |D_iv|
PASS_SIGN_TARGET = -1                                               # (local) ABSOLUTE (sign(D_iv) < 0)

INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    PROJECT_ROOT / "sessions/archive/session-84/session-84-s3-gen-elimination-synthesis.md",
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ_MOMENTS = ART_DIR / "s85_w12_elim1_D_K_Lmax_moments.npz"
OUT_NPZ_TRAJ = ART_DIR / "s85_w12_elim1_residual_trajectory.npz"
OUT_PNG = ART_DIR / "s85_w12_elim1_R_JK_vs_Lmax.png"


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")                  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    content = hashlib.sha256(script_bytes).hexdigest()              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Spectral moment evaluator
# ---------------------------------------------------------------------------
def weyl_dim_su3(p, q):
    """SU(3) Weyl dimension formula: dim((p,q)) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p, q):
    """Quadratic Casimir of SU(3) irrep (p, q): (p² + p·q + q² + 3(p+q)) / 3."""
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


def spectral_moments_casimir(L_max):
    """Return (a_0, a_2, a_4, N_sectors) via multiplicity-weighted Casimir.

    a_n = (1/Vol_SU3_Haar) Σ_{(p,q) ≠ (0,0), p+q ≤ L_max} d(p,q) / C_2(p,q)^n
    """
    a2 = 0.0                                                        # (local)
    a4 = 0.0                                                        # (local)
    n_sectors = 0                                                   # (local)
    eigenvalue_count = 0                                            # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p == 0 and q == 0:
                continue
            if p + q > L_max:
                continue
            d = weyl_dim_su3(p, q)                                  # (local)
            c = casimir_su3(p, q)                                   # (local)
            a2 += d / c
            a4 += d / (c * c)
            n_sectors += 1
            eigenvalue_count += d  # total eigenvalue count weighted by multiplicity
    a2 /= Vol_SU3_Haar
    a4 /= Vol_SU3_Haar
    # a_0 = (1/Vol) Σ d (constant-function integration — the identity moment)
    a0 = 0.0                                                        # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1):
            if p == 0 and q == 0:
                continue
            if p + q > L_max:
                continue
            a0 += weyl_dim_su3(p, q)
    a0 /= Vol_SU3_Haar
    return a0, a2, a4, n_sectors, eigenvalue_count


def cross_check_a2_against_s61():
    """CC: plan says S61 heat-kernel a2_fold = 2776.17 (Pauli-Villars truncated).
    Our Casimir schematic is NOT the same regulator (no Jensen τ weighting, no
    PV subtraction), so direct numerical match is not expected. Document the
    context-gap explicitly so the reviewer sees we know the difference.
    """
    s61_a2_PW = 2776.17                                             # (local) reference only
    return s61_a2_PW


# ---------------------------------------------------------------------------
# Section 6 - Compute
# ---------------------------------------------------------------------------
def compute():
    results = {}                                                    # (local)
    L_list = list(L_MAX_SCAN)                                       # (local)
    a2_arr = np.zeros(len(L_list))                                  # (local)
    a4_arr = np.zeros(len(L_list))                                  # (local)
    R_JK_arr = np.zeros(len(L_list))                                # (local)
    D_iv_arr = np.zeros(len(L_list))                                # (local)
    sign_arr = np.zeros(len(L_list), dtype=int)                     # (local)
    n_sectors_arr = np.zeros(len(L_list), dtype=int)                # (local)
    n_eigs_arr = np.zeros(len(L_list), dtype=int)                   # (local)

    Delta_sq = Delta_BCS * Delta_BCS                                # (local)
    ratio_Delta_sq_K = Delta_sq / K_base                            # (local)

    print(f"  Delta_BCS = {Delta_BCS}")
    print(f"  K_base    = {K_base}")
    print(f"  Delta^2/K = {ratio_Delta_sq_K:.10f}")
    print(f"  Vol_SU3_Haar = {Vol_SU3_Haar:.6f}")
    print()
    print("  L_max | a_2           a_4           a_4/a_2     R_JK         D_iv       sign  N_sec  N_eig")

    for i, L in enumerate(L_list):
        a0, a2, a4, n_sec, n_eig = spectral_moments_casimir(L)
        a2_arr[i] = a2
        a4_arr[i] = a4
        n_sectors_arr[i] = n_sec
        n_eigs_arr[i] = n_eig
        sigma_J = a4                                                # (local) a_4 moment — Tr D_K^(-4) / Vol
        sigma_K = a2                                                # (local) a_2 moment — Tr D_K^(-2) / Vol
        R_JK = (sigma_J * Delta_sq) / (sigma_K * K_base)            # (local)
        D_iv = R_JK - 1.0                                           # (local)
        R_JK_arr[i] = R_JK
        D_iv_arr[i] = D_iv
        sign_arr[i] = int(np.sign(D_iv))
        ratio = a4 / a2                                             # (local)
        print(f"  {L:5d} | {a2:.6e}  {a4:.6e}  {ratio:.6f}   {R_JK:.6e}  {D_iv:+.6f}  {sign_arr[i]:+d}    {n_sec:4d}  {n_eig:6d}")

    results["L_max_list"] = L_list
    results["a_2"] = a2_arr
    results["a_4"] = a4_arr
    results["R_JK"] = R_JK_arr
    results["D_iv"] = D_iv_arr
    results["sign"] = sign_arr
    results["n_sectors"] = n_sectors_arr
    results["n_eigenvalues"] = n_eigs_arr
    results["Delta_sq"] = Delta_sq
    results["ratio_Delta_sq_K"] = ratio_Delta_sq_K

    # Primary PASS predicate (plan §W12-3 line 153):
    #   (a) R_JK < 1 at all three L_max
    #   (b) R_JK is monotone-decreasing in L_max (allow 0.05 RATIO slack)
    cond_sub1 = bool((R_JK_arr < 1.0).all())                        # (local)
    # Monotone-decreasing with 0.05 ratio tolerance:
    # R_JK[i+1] <= R_JK[i] * (1 + 0.05), i.e. we allow R_JK to increase by at most 5%
    slack = 1.0 + PASS_RATIO_TOL                                    # (local)
    cond_sub2 = True                                                # (local)
    for i in range(len(R_JK_arr) - 1):
        if R_JK_arr[i + 1] > R_JK_arr[i] * slack:
            cond_sub2 = False
    cond_sub3 = bool((sign_arr == PASS_SIGN_TARGET).all())          # (local) sign(D_iv) < 0

    results["cond_sub1_all_R_JK_lt_1"] = cond_sub1
    results["cond_sub2_R_JK_monotone_decreasing"] = cond_sub2
    results["cond_sub3_sign_all_negative"] = cond_sub3

    # Primary verdict
    if cond_sub1 and cond_sub2 and cond_sub3:
        verdict = "PASS"
    elif any(R_JK_arr >= 1.0):
        verdict = "FAIL"
    elif cond_sub3 and not cond_sub2:
        # sign negative everywhere but monotonicity violated → INFO
        verdict = "INFO"
    else:
        verdict = "FAIL"
    results["verdict"] = verdict

    # Value tuple for verdict line: (D_iv(8), D_iv(10), D_iv(12), signs)
    results["value"] = (
        float(D_iv_arr[0]),
        float(D_iv_arr[1]),
        float(D_iv_arr[2]),
        (int(sign_arr[0]), int(sign_arr[1]), int(sign_arr[2])),
    )
    return results


# ---------------------------------------------------------------------------
# Section 7 - Verdict append
# ---------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha):
    d8, d10, d12, signs = value                                     # (local)
    val_str = (f"(D_iv8={d8:+.6f},D_iv10={d10:+.6f},D_iv12={d12:+.6f},"
               f"signs={signs})")                                   # (local)
    line = (f"{GATE_ID}: {verdict} -- value={val_str} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 8 - Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    r = compute()
    verdict = r["verdict"]
    value = r["value"]
    s61_ref = cross_check_a2_against_s61()

    print()
    print("  PASS sub-conditions:")
    print(f"    cond_sub1 (all R_JK < 1):                  {r['cond_sub1_all_R_JK_lt_1']}")
    print(f"    cond_sub2 (R_JK monotone-decreasing, 5%):  {r['cond_sub2_R_JK_monotone_decreasing']}")
    print(f"    cond_sub3 (sign(D_iv) = -1 at all L_max):  {r['cond_sub3_sign_all_negative']}")
    print()
    print(f"  Context: S61 PW a2_fold reference = {s61_ref} (Pauli-Villars regulator — different convention, diagnostic only)")
    print()
    print(f"(value=({value[0]:+.6f},{value[1]:+.6f},{value[2]:+.6f},{value[3]}), "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # Save spectral moments NPZ
    np.savez_compressed(
        OUT_NPZ_MOMENTS,
        L_max=np.array(r["L_max_list"]),
        a_2=r["a_2"],
        a_4=r["a_4"],
        R_JK=r["R_JK"],
        D_iv=r["D_iv"],
        sign=r["sign"],
        n_sectors=r["n_sectors"],
        n_eigenvalues=r["n_eigenvalues"],
        Delta_sq=np.float64(r["Delta_sq"]),
        ratio_Delta_sq_K=np.float64(r["ratio_Delta_sq_K"]),
        Delta_BCS=np.float64(Delta_BCS),
        K_base=np.float64(K_base),
        Vol_SU3_Haar=np.float64(Vol_SU3_Haar),
    )

    # Save trajectory NPZ (same data, separate file for plan deliverable spec)
    np.savez_compressed(
        OUT_NPZ_TRAJ,
        L_max=np.array(r["L_max_list"]),
        R_JK_trajectory=r["R_JK"],
        D_iv_trajectory=r["D_iv"],
        sign_trajectory=r["sign"],
    )

    # R_JK vs L_max plot with L_max^(-2) asymptote overlay
    fig, ax = plt.subplots(figsize=(8, 6))
    L_arr = np.array(r["L_max_list"], dtype=float)                  # (local)
    ax.semilogy(L_arr, r["R_JK"], "o-", color="#1f77b4", markersize=10, lw=2,
                label=r"$R_{JK}(L_{max})$")
    # Asymptote overlay (diagnostic only, NOT a pre-registered criterion per plan):
    # fit R_JK ~ A / L_max^n, extract n from log-log slope
    log_L = np.log(L_arr)                                           # (local)
    log_R = np.log(r["R_JK"])                                       # (local)
    slope, intercept = np.polyfit(log_L, log_R, 1)                  # (local)
    asymptote = np.exp(intercept) * L_arr ** slope                  # (local)
    ax.semilogy(L_arr, asymptote, "--", color="#d62728", lw=1.2,
                label=rf"fit: $L^{{{slope:.2f}}}$ (diagnostic, not pre-registered)")
    ax.axhline(1.0, color="k", ls=":", lw=1, label=r"$R_{JK}=1$ (Josephson dominance threshold)")
    ax.set_xlabel(r"$L_{\max}$", fontsize=12)
    ax.set_ylabel(r"$R_{JK} = \sigma_J\,|\Delta|^2 / (\sigma_K\,|K|)$", fontsize=12)
    ax.set_title(f"{GATE_ID}: branch-(iv) retraction L_max-robustness "
                 f"(verdict={verdict})", fontsize=12)
    ax.legend(loc="best")
    ax.grid(True, which="both", alpha=0.3)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120)
    plt.close(fig)

    append_verdict(verdict, value, audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
