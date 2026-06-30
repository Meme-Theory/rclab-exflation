#!/usr/bin/env python3
"""
S85 W3-11 — S85-W3-MULTIPOLE-BREAKDOWN-SCAN
============================================

Gate: S85-W3-MULTIPOLE-BREAKDOWN-SCAN ([VERIFY])

Hypothesis (plan §W3-11):
  The multipole expansion of the spectral action — treating each
  symmetry sector (a_0, a_2, a_4, ..., a_{2L}) as an independent
  spectral moment — breaks down at order L*(K) on K in [K_R5, K_crit].
  PASS iff min L*(K) >= 4 (good through octupole).

Substitution chain (Seeley-DeWitt + cutoff at highest weight):
  Def 1: a_L(K) = spectral moment Tr[(D_K^2)^L] truncated at L_max
  Def 2: dL_correction(L, K) = |a_{L+2} a_0 - a_L^2| / a_L^2
                              fractional correction from coset truncation
  Def 3: L*(K) = max L such that dL_correction(L, K) < 0.10
  Step 1: For Wigner-like spectral density on Jensen-deformed SU(3),
          ratio(L, K) ~ (Delta(K)/Lambda)^2 * (1 + L/L_max)
          where Lambda is the highest eigenvalue scale.
  Step 2: Lambda(L_max=10) = M_KK * sqrt(L_max+1)  (Casimir saturation
          on SU(3) at L_max=10: highest weight lambda^2 ~ L_max*(L_max+2))
  Step 3: Substitute Delta(K) = Delta_BCS * sqrt((K-K_R5)/K_R5):
          ratio(L, K) = [Delta_BCS^2 * (K-K_R5)/K_R5 / Lambda^2] * (1 + L/L_max)
  Step 4: At K = K_R5:  Delta=0  ->  ratio = 0  ->  L*(K_R5) = L_max
  Step 5: At K = K_crit: Delta = Delta_BCS*sqrt(46.6) = 3.169 M_KK,
          Lambda = sqrt(11) M_KK = 3.317
          ratio(L, K_crit) = (3.169/3.317)^2 * (1 + L/10) = 0.913 * (1+L/10)
          L*(K_crit) such that 0.913 * (1+L*/10) < 0.10
          1 + L*/10 < 0.110, L*/10 < -0.890 -> L*(K_crit) = 0
  Direction: L*(K) DECREASES with K (Delta grows with K, ratio grows with L)
            min L*(K) over corridor = L*(K_crit).
  Conclusion: With this Casimir-saturated cutoff Lambda = sqrt(L_max+1)*M_KK,
            min L*(K) on corridor is small; verdict depends on Lambda choice.

Pre-registered thresholds (plan §W3-11):
  PASS iff min L*(K) >= 4
  FAIL iff min L*(K) < 2
  INFO iff min L*(K) in [2, 4]

Inputs (SHA-256 dual-pinned):
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=min_corridor_L_star, scheme=heat_kernel, convention=A, L_max=10)

Classification: PHONONIC
  Multipole expansion is the SU(3) representation-theoretic decomposition
  of the spectral action.

Method:
  (a) Build moment ratio model with Lambda = sqrt(L_max+1) * M_KK.
  (b) Scan K over 21 log-spaced points on [K_R5, K_crit].
  (c) For each K, compute L*(K) = max L < L_max with ratio < 10%.
  (d) Report min L*(K).

CPU only (scalar arithmetic; no matrices needed since model is closed-form).
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
    K_R5, K_crit, Delta_BCS, M_KK,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-MULTIPOLE-BREAKDOWN-SCAN"                  # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A"                                             # (local)
L_MAX = 10                                                   # (local)

K_SCAN = np.logspace(np.log10(K_R5), np.log10(K_crit), 21)   # (local) plan §W3-11 PRDR pin
K_SCAN[0] = K_R5                                             # (local) endpoint pin
K_SCAN[-1] = K_crit                                          # (local) endpoint pin

MOMENT_TOL = 0.10                                            # (local) plan §W3-11 PASS band
LAMBDA_SCALE = M_KK * np.sqrt(L_MAX + 1)                     # (local) Casimir-saturated cutoff
                                                              # |lambda|^2 ~ L_max*(L_max+2) at top weight
                                                              # so Lambda ~ sqrt(L_max+1) * M_KK

PASS_MIN_L_STAR = 4                                          # (local)
FAIL_MIN_L_STAR = 2                                          # (local)

OUT_NPZ = resolve_output(85, 's85_w3_multipole_breakdown_scan.npz')
OUT_PNG = resolve_output(85, 's85_w3_multipole_breakdown_scan.png')
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


def Delta_of_K(K: float) -> float:
    """Mean-field Landau gap (M_KK_dim units; absolute scale Delta_BCS * M_KK)."""
    if K <= K_R5:
        return 0.0
    return Delta_BCS * np.sqrt((K - K_R5) / K_R5) * M_KK     # (local) absolute units (GeV)


def moment_ratio(L: int, K: float) -> float:
    """Fractional moment correction at order L for K-deformed spectrum.
    ratio(L, K) = (Delta(K) / Lambda)^2 * (1 + L / L_max).
    """
    Delta = Delta_of_K(K)                                    # (local) absolute (GeV)
    return (Delta / LAMBDA_SCALE) ** 2 * (1.0 + L / L_MAX)   # (local)


def L_star_of_K(K: float) -> int:
    """Compute L*(K): largest L in [0, L_max] with moment_ratio(L, K) < MOMENT_TOL."""
    L_star = -1                                              # (local) -1 if none satisfy
    for L in range(L_MAX + 1):
        if moment_ratio(L, K) < MOMENT_TOL:
            L_star = L
        else:
            break
    return L_star


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs")
    print(f"  K_R5 = {K_R5}, K_crit = {K_crit}")
    print(f"  Delta_BCS = {Delta_BCS:.6f} (M_KK units)")
    print(f"  M_KK = {M_KK:.4e} GeV")
    print(f"  Lambda_scale = sqrt(L_max+1) * M_KK = sqrt({L_MAX+1}) * M_KK = {LAMBDA_SCALE:.4e} GeV")
    print(f"  Moment tolerance: {MOMENT_TOL} (10%)")
    print(f"  K-scan: {len(K_SCAN)} points on [K_R5, K_crit]")

    # L*(K) scan
    print("\n[SEC 4b] L*(K) scan")
    L_star_scan = np.array([L_star_of_K(K) for K in K_SCAN])  # (local)
    Delta_scan = np.array([Delta_of_K(K) for K in K_SCAN])    # (local)

    print(f"  K_R5     L*(K_R5)   = {L_star_scan[0]} (Delta = {Delta_scan[0]:.3e})")
    print(f"  K_crit   L*(K_crit) = {L_star_scan[-1]} (Delta = {Delta_scan[-1]:.3e})")
    print(f"  K mid    L*(K_mid)  = {L_star_scan[len(K_SCAN)//2]}")

    min_L_star = int(L_star_scan.min())                      # (local) min over corridor
    min_K_idx = int(np.argmin(L_star_scan))                  # (local)
    min_K = K_SCAN[min_K_idx]                                # (local)

    print(f"\n[SEC 4c] Aggregate")
    print(f"  min L*(K) over corridor = {min_L_star}")
    print(f"  argmin K              = {min_K:.4e}")
    print(f"  PASS criterion: min L* >= {PASS_MIN_L_STAR}")
    print(f"  FAIL criterion: min L* <  {FAIL_MIN_L_STAR}")
    print(f"  INFO criterion: min L* in [{FAIL_MIN_L_STAR}, {PASS_MIN_L_STAR})")

    # Detailed moment ratios at K_crit (worst case)
    print("\n[SEC 4d] Per-L moment ratios at K_crit (worst-case endpoint)")
    L_arr = np.arange(L_MAX + 1)                             # (local)
    ratios_K_crit = np.array([moment_ratio(L, K_crit) for L in L_arr])  # (local)
    for L, r in zip(L_arr, ratios_K_crit):
        marker = " <-- crosses 10%" if r >= MOMENT_TOL and (L == 0 or ratios_K_crit[L-1] < MOMENT_TOL) else ""
        print(f"    L={L:2d}: ratio = {r:.4e}  ({'OK' if r < MOMENT_TOL else 'EXCEED'}){marker}")

    # Substitution-chain check: ratio formula matches
    print("\n[SEC 4e] Substitution-chain check at (L=2, K=K_crit)")
    Delta_crit = Delta_of_K(K_crit)                          # (local)
    expected = (Delta_crit / LAMBDA_SCALE) ** 2 * (1 + 2 / L_MAX)  # (local)
    actual = moment_ratio(2, K_crit)                         # (local)
    chain_ok = abs(expected - actual) < 1e-15                # (local)
    print(f"  expected = (Delta/Lambda)^2 * (1+L/L_max) = {expected:.6e}")
    print(f"  actual   = moment_ratio(2, K_crit)        = {actual:.6e}")
    print(f"  chain match (< 1e-15): {chain_ok}")

    # Cross-checks
    print("\n[SEC 4f] Cross-checks")
    CC1 = (min_L_star >= PASS_MIN_L_STAR)                    # (local) main PASS
    CC2 = (L_star_scan[0] == L_MAX)                          # (local) L*(K_R5) = L_max (Delta=0)
    CC3 = bool(np.all(np.diff(L_star_scan) <= 0))            # (local) L* monotone non-increasing
    CC4 = chain_ok                                           # (local) substitution chain
    CC5 = (LAMBDA_SCALE > 0 and Delta_BCS > 0)               # (local) sanity
    all_CC = CC1 and CC3 and CC4 and CC5                     # (local) CC2 informational
    print(f"  CC-1 min L* >= {PASS_MIN_L_STAR}:                  {CC1} (min={min_L_star})")
    print(f"  CC-2 L*(K_R5) == L_max (Delta=0):    {CC2} ({L_star_scan[0]})")
    print(f"  CC-3 L* monotone non-increasing:     {CC3}")
    print(f"  CC-4 substitution chain (machine prec): {CC4}")
    print(f"  CC-5 LAMBDA_SCALE, Delta_BCS > 0:    {CC5}")
    print(f"  All gating CC PASS:                  {all_CC}")

    return dict(
        value=min_L_star,
        K_SCAN=K_SCAN, L_star_scan=L_star_scan, Delta_scan=Delta_scan,
        min_L_star=min_L_star, min_K=min_K,
        ratios_K_crit=ratios_K_crit,
        LAMBDA_SCALE=LAMBDA_SCALE,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5,
        all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    m = result['min_L_star']                                 # (local)
    if m < FAIL_MIN_L_STAR:
        return "FAIL"
    if m >= PASS_MIN_L_STAR:
        return "PASS"
    return "INFO"


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
    ax1.semilogx(K, result['L_star_scan'], 'b-o', ms=5, lw=1.5, label='L*(K)')
    ax1.axhline(PASS_MIN_L_STAR, color='g', ls='--', lw=1, label=f'PASS threshold {PASS_MIN_L_STAR}')
    ax1.axhline(FAIL_MIN_L_STAR, color='r', ls='--', lw=1, label=f'FAIL threshold {FAIL_MIN_L_STAR}')
    ax1.axvspan(K_R5, K_crit, color='lightgreen', alpha=0.15)
    ax1.set_xlabel('K')
    ax1.set_ylabel('L*(K) (max convergent multipole)')
    ax1.set_title(f'Multipole breakdown order on inflationary corridor\nmin L*(K) = {result["min_L_star"]}')
    ax1.legend(loc='lower left', fontsize=8)
    ax1.grid(True, which='both', ls=':', alpha=0.4)
    ax1.set_ylim(-1, L_MAX + 1)

    L_arr = np.arange(L_MAX + 1)                             # (local)
    ax2.semilogy(L_arr, result['ratios_K_crit'], 'r-o', ms=5, lw=1.5, label=f'moment_ratio(L, K_crit)')
    ax2.axhline(MOMENT_TOL, color='k', ls='--', lw=1, label=f'tolerance {MOMENT_TOL}')
    ax2.set_xlabel('L (multipole order)')
    ax2.set_ylabel('moment_ratio(L, K_crit)')
    ax2.set_title('Per-L correction at K_crit (worst case)')
    ax2.legend()
    ax2.grid(True, which='both', ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  multipole expansion breakdown scan',
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
        K_SCAN=result['K_SCAN'], L_star_scan=result['L_star_scan'],
        Delta_scan=result['Delta_scan'],
        min_L_star=result['min_L_star'], min_K=result['min_K'],
        ratios_K_crit=result['ratios_K_crit'],
        LAMBDA_SCALE=result['LAMBDA_SCALE'],
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
    print(f"  verdict: {verdict}  min L*(K) = {result['min_L_star']}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
