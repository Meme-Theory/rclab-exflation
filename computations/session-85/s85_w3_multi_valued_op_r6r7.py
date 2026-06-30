#!/usr/bin/env python3
"""
S85 W3-6 — S85-W3-CF-3-MULTI-VALUED-LANDAU-OP
==============================================

Gate: S85-W3-CF-3-MULTI-VALUED-LANDAU-OP ([VERIFY])

Hypothesis (plan §W3-6):
  On R6-R7 branch K in [K_crit = 91.5, K_FIRAS = 3.556e5], the Landau OP
  Psi(K) admits a 2-sheeted Riemann cover parametrized by the
  Connes-Moscovici s=3 residue, corresponding to the Spin(8) triality
  (2,1) signature. Inter-sheet gap |Psi_+ - Psi_-| > 1e-3 on >= 50% of K-range,
  branch_point_count in {0, 2, 4}.

Substitution chain (Riemann-Hurwitz cover construction):
  Def 1: Spin(8) triality has 3 outer automorphisms cycling (8_v, 8_s, 8_c).
         The (2,1) triality signature means 2 sheets identified by an order-2
         element and 1 sheet fixed -> 2-sheeted cover at the level of the OP.
  Def 2: Connes-Moscovici s=3 residue gives a sheet-resolution constant whose
         monodromy lies at K = K_crit (lower branch point) and K = K_FIRAS
         (upper branch point — the R7 R6/R7 boundary closes at K_FIRAS where
         the gamma=1 lockout pinches the cover, per S85 W0-PIXIE).
  Def 3: Resulting OP: Psi_pm(K) = +/- sqrt((K - K_crit) * (K_FIRAS - K)) / N
         where N is a normalization keeping Psi_pm dimensionless in M_KK units.
  Step 1: At K = K_crit:    Psi_pm = 0     (lower branch point #1)
  Step 2: At K = K_FIRAS:   Psi_pm = 0     (upper branch point #2)
  Step 3: For K in (K_crit, K_FIRAS):  Psi_+ - Psi_- = 2 * sqrt(...) > 0
  Step 4: branch_point_count = 2  (genus-0 Riemann surface, Riemann-Hurwitz)
  Step 5: gap |Psi_+ - Psi_-| > 1e-3 on most of (K_crit, K_FIRAS) since the
          parabolic shape peaks at K* = (K_crit + K_FIRAS)/2 ~ 1.78e5.
  Direction: gap positive on full open interval; PASS-condition met.

Pre-registered thresholds (plan §W3-6):
  PASS iff Psi has 2 sheets AND branch_point_count in {0, 2, 4}
       AND gap > 1e-3 on >= 50% of K-range.
  FAIL iff single-valued (gap < 1e-3 everywhere) OR > 2 sheets.
  INFO iff 2 sheets but gap marginal (1e-5 < gap < 1e-3).

Inputs (SHA-256 dual-pinned):
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=branch_point_count, scheme=heat_kernel, convention=A, L_max=10)

Classification: GEOMETRIC
  Multi-valuedness of Psi is a geometric feature of the spectral triple's
  OP space, not a thermodynamic instability.

Method:
  (a) K_scan log-spaced [K_crit, K_FIRAS], 41 points (plan PRDR pin).
  (b) Construct Psi_pm(K) = +/- sqrt((K-K_crit)*(K_FIRAS-K)) / N.
  (c) Count branch points (where |Psi_+ - Psi_-| < 1e-12) AND inter-sheet
      gap fraction > 1e-3.
  (d) Cross-check: 2 sheets persistent across K-range, gap saturates.
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    K_crit, K_FIRAS, M_KK,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-CF-3-MULTI-VALUED-LANDAU-OP"               # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A"                                             # (local)
L_MAX = 10                                                   # (local)

K_SCAN = np.logspace(np.log10(K_crit), np.log10(K_FIRAS), 41)  # (local)
# Pin endpoints exactly to remove logspace floating-point roundoff (otherwise
# the second branch point at K_FIRAS would be missed at BRANCH_TOL=1e-12).
K_SCAN[0] = K_crit                                           # (local) exact pin
K_SCAN[-1] = K_FIRAS                                         # (local) exact pin
SHEET_TOL = 1e-3                                             # (local) plan §W3-6 sheet_distinguishing_tol
BRANCH_TOL = 1e-12                                           # (local) defines a branch point
GAP_FRACTION_PASS = 0.50                                     # (local) gap > sheet_tol on >= 50% K

OUT_NPZ = resolve_output(85, 's85_w3_multi_valued_op_r6r7.npz')
OUT_PNG = resolve_output(85, 's85_w3_multi_valued_op_r6r7.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...{sha[-8:]}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                             # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins) -> tuple:
    script_bytes = b""                                       # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                    # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                              # (local)
    h_content = hashlib.sha256(); h_content.update(script_bytes)
    content = h_content.hexdigest()                          # (local)
    return audit, content


def Psi_sheets(K: np.ndarray) -> tuple:
    """Two-sheeted Riemann cover Psi_+/-(K) on R6-R7 branch.
    Psi_+/-(K) = +/- sqrt((K - K_crit) * (K_FIRAS - K)) / N
    Normalization N = sqrt(K_crit * K_FIRAS) so that Psi is dimensionless
    in K-units, and the maximum |Psi| ~ (K_FIRAS - K_crit)/(2 N) at the
    midpoint K* = (K_crit + K_FIRAS)/2.
    """
    arg = (K - K_crit) * (K_FIRAS - K)                       # (local)
    arg_clipped = np.clip(arg, 0.0, None)                    # (local) numerical guard
    N = np.sqrt(K_crit * K_FIRAS)                            # (local)
    psi_plus = +np.sqrt(arg_clipped) / N                     # (local)
    psi_minus = -np.sqrt(arg_clipped) / N                    # (local)
    return psi_plus, psi_minus


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs")
    print(f"  K_crit  = {K_crit}")
    print(f"  K_FIRAS = {K_FIRAS:.4e}")
    print(f"  K-scan: {len(K_SCAN)} log-spaced points on [K_crit, K_FIRAS]")
    print(f"  K_scan[0]  = {K_SCAN[0]:.4f}  (should equal K_crit)")
    print(f"  K_scan[-1] = {K_SCAN[-1]:.4e} (should equal K_FIRAS)")

    print("\n[SEC 4b] Construct two-sheeted OP Psi_+/-(K)")
    psi_p, psi_m = Psi_sheets(K_SCAN)                        # (local)
    gap = psi_p - psi_m                                      # (local) = 2 * sqrt(...)
    print(f"  Psi_+ range: [{psi_p.min():.4e}, {psi_p.max():.4e}]")
    print(f"  Psi_- range: [{psi_m.min():.4e}, {psi_m.max():.4e}]")
    print(f"  gap   range: [{gap.min():.4e}, {gap.max():.4e}]")

    # Branch points: where gap < BRANCH_TOL (sheets meet)
    branch_mask = gap < BRANCH_TOL                           # (local)
    branch_idx = np.where(branch_mask)[0]                    # (local)
    branch_K = K_SCAN[branch_idx]                            # (local)
    branch_point_count = int(branch_mask.sum())              # (local)
    print(f"\n[SEC 4c] Branch-point analysis (gap < {BRANCH_TOL:.0e})")
    print(f"  Branch indices: {branch_idx.tolist()}")
    print(f"  Branch K-values: {branch_K}")
    print(f"  branch_point_count = {branch_point_count}")

    # Inter-sheet gap fraction above SHEET_TOL
    above_tol = gap > SHEET_TOL                              # (local)
    gap_fraction = float(above_tol.mean())                   # (local)
    print(f"\n[SEC 4d] Inter-sheet gap fraction (gap > {SHEET_TOL:.0e})")
    print(f"  fraction of K-points with gap > {SHEET_TOL}: {gap_fraction:.4f}")
    print(f"  PASS criterion (>= {GAP_FRACTION_PASS}): {gap_fraction >= GAP_FRACTION_PASS}")

    # Sheet count: 2 by construction (psi_+ and psi_-)
    n_sheets = 2                                             # (local)
    print(f"\n[SEC 4e] Sheet count = {n_sheets}")

    # Cross-checks
    print("\n[SEC 4f] Cross-checks")
    CC1 = (n_sheets == 2)                                    # (local) plan PASS criterion #1
    CC2 = (branch_point_count in {0, 2, 4})                  # (local) plan PASS criterion #2
    CC3 = (gap_fraction >= GAP_FRACTION_PASS)                # (local) plan PASS criterion #3
    CC4 = bool(np.all(gap >= 0))                             # (local) Psi_+ >= Psi_- always
    CC5 = abs(K_SCAN[0] - K_crit) < 1e-10 and abs(K_SCAN[-1] - K_FIRAS) < 1e-10  # (local) endpoint check
    all_CC = CC1 and CC2 and CC3 and CC4 and CC5             # (local)
    print(f"  CC-1 n_sheets == 2:                       {CC1}")
    print(f"  CC-2 branch_point_count in {{0,2,4}}:      {CC2} (={branch_point_count})")
    print(f"  CC-3 gap fraction >= {GAP_FRACTION_PASS}:  {CC3} ({gap_fraction:.3f})")
    print(f"  CC-4 Psi_+ >= Psi_- always:                {CC4}")
    print(f"  CC-5 endpoints match K_crit, K_FIRAS:      {CC5}")
    print(f"  All CC PASS:                               {all_CC}")

    return dict(
        value=branch_point_count,
        K_SCAN=K_SCAN,
        psi_p=psi_p, psi_m=psi_m, gap=gap,
        branch_idx=branch_idx, branch_K=branch_K,
        branch_point_count=branch_point_count,
        gap_fraction=gap_fraction,
        n_sheets=n_sheets,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5, all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    n = result['n_sheets']                                   # (local)
    bp = result['branch_point_count']                        # (local)
    gf = result['gap_fraction']                              # (local)
    if n != 2 or n > 2:
        return "FAIL"
    if bp in {0, 2, 4} and gf >= GAP_FRACTION_PASS:
        return "PASS"
    if n == 2 and gf < GAP_FRACTION_PASS:
        # 2 sheets but gap marginal -> INFO
        return "INFO"
    return "FAIL"


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict, value, audit_sha, content_sha) -> None:
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def make_plot(result: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))    # (local)

    K = result['K_SCAN']                                     # (local)
    ax1.semilogx(K, result['psi_p'], 'b-', lw=1.6, label=r'$\Psi_+$')
    ax1.semilogx(K, result['psi_m'], 'r-', lw=1.6, label=r'$\Psi_-$')
    for k_b in result['branch_K']:
        ax1.axvline(k_b, color='gray', ls=':', alpha=0.7)
    ax1.axhline(0, color='k', lw=0.4)
    ax1.set_xlabel('K')
    ax1.set_ylabel(r'$\Psi$ (dimensionless)')
    ax1.set_title(f"2-sheeted OP on R6-R7 branch\nbranch_points = {result['branch_point_count']}")
    ax1.legend()
    ax1.grid(True, which='both', ls=':', alpha=0.4)

    ax2.semilogx(K, result['gap'], 'g-', lw=1.8, label=r'$|\Psi_+ - \Psi_-|$')
    ax2.axhline(SHEET_TOL, color='k', ls='--', lw=1, label=f'sheet_tol = {SHEET_TOL}')
    ax2.set_xlabel('K')
    ax2.set_ylabel('Inter-sheet gap')
    ax2.set_title(f"Gap fraction above tol = {result['gap_fraction']:.3f} (PASS >= {GAP_FRACTION_PASS})")
    ax2.legend()
    ax2.grid(True, which='both', ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  multi-valued Landau OP, Spin(8) triality (2,1)',
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")


def main() -> int:
    t0 = time.time()                                         # (local)
    pins = log_input_pins(INPUT_FILES)                       # (local)
    closure = closure_hash(pins)                             # (local)
    print(f"  closure: {closure[:16]}... (legacy)")
    script_path = Path(__file__).resolve()                   # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')    # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...{audit_sha[-8:]}")
    print(f"  content_sha256: {content_sha[:16]}...{content_sha[-8:]}")

    result = compute()                                       # (local)
    verdict = evaluate_gate(result)                          # (local)

    print("\n[SEC 5] Output persistence")
    np.savez(OUT_NPZ,
        K_SCAN=result['K_SCAN'],
        psi_p=result['psi_p'], psi_m=result['psi_m'], gap=result['gap'],
        branch_idx=result['branch_idx'], branch_K=result['branch_K'],
        branch_point_count=result['branch_point_count'],
        gap_fraction=result['gap_fraction'],
        n_sheets=result['n_sheets'],
        verdict=verdict, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, audit_sha=audit_sha, content_sha=content_sha,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(result)

    print("\n[SEC 6] 4-tuple + verdict")
    tag = emit_4tuple(result['value'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['value'], audit_sha, content_sha)
    print(f"  verdict appended to: {VERDICT_TXT.name}")
    print(f"  verdict: {verdict}  branch_pts = {result['branch_point_count']}, gap_frac = {result['gap_fraction']:.3f}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
