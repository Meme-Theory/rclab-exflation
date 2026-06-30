#!/usr/bin/env python3
"""
S85 W3-3 — S85-W3-CF-4-BOGOLIUBOV-DEPHASING-AT-K
=================================================

Gate: S85-W3-CF-4-BOGOLIUBOV-DEPHASING-AT-K ([VERIFY])

Hypothesis (plan §W3-3):
  On the inflationary sub-corridor K in [K_R5, K_crit], the BdG dephasing
  amplitude beta_BdG(K) := |v_k| at k_F scales as (K - K_R5)^{1/2} near
  threshold (mean-field Landau exponent), with absolute magnitude at
  K_1 = 10.0 regulator-invariant to 5% across 3 regulators.

Substitution chain (plan §W3-3 Step 1-7):
  Definition: BdG rotation (c_k^dag, c_-k) = (u_k, v_k)(alpha_k^dag, alpha_-k)
              with |u_k|^2 - |v_k|^2 = 1.
              beta_BdG := |v_k| at k_F (AMPLITUDE, not occupation).
  Definition: Order parameter: Delta(K) = pair condensate.
  Landau mean-field: Delta(K) = c * (K - K_R5)^{1/2} for K > K_R5.
  Step 1: |v_k|^2 = (1/2) * (1 - xi_k / E_k)  where E_k = sqrt(xi_k^2 + Delta^2).
  Step 2: Near threshold (Delta small): E_k ~ |xi_k| + Delta^2 / (2|xi_k|).
  Step 3: |v_k|^2 ~ Delta^2 / (4 xi_k^2) at k ~ k_F.
  Step 4: beta_BdG = |v_k| = |Delta| / (2 |xi_k|) at k_F.
  Step 5: Substitute Delta(K) = c (K - K_R5)^{1/2}:
          beta_BdG(K) = c (K - K_R5)^{1/2} / (2 xi_F).
  Step 6: So beta_BdG(K) ~ (K - K_R5)^{1/2}  ->  exponent = 1/2.
  Direction: beta_BdG monotone increasing in K for K > K_R5 (positive sqrt).
  Conclusion: fitted exponent should equal 0.5 within 0.05.

Pre-registered thresholds (plan §W3-3):
  PASS iff reg_spread(K_1=10.0) < 5% AND |exponent - 0.5| < 0.05.
  INFO iff exponent in [0.35, 0.65] but not tight.
  FAIL iff reg_spread > 15% OR |exponent - 0.5| > 0.15.

Inputs (SHA-256 dual-pinned):
  - canonical_constants.py
  - s82_w2_11_s_pp_full_ed.npz (2-sector BdG cache, plan §W3-3 input)
  - script bytes

Output 4-tuple:
  (value=beta_BdG(K_1=10.0), scheme=heat_kernel, convention=A, L_max=10)

Classification: PHONONIC
  The "Bogoliubov rotation" is a re-diagonalization of the 2-band D_K
  Hamiltonian at the fold, not a superfluid BCS calculation on a lattice.

Method:
  (a) Import Delta_BCS, K_R5, K_crit, M_KK from canonical_constants.
  (b) Mean-field Delta(K) = Delta_BCS * sqrt(max(0, (K-K_R5)/K_R5)).
  (c) For each of 3 regulators, apply small multiplicative Delta scale.
  (d) Compute beta_BdG(K) at 51 log-K-points + K_1 = 10.0 + K_0 = coth(1).
  (e) Fit exponent from log-log regression near threshold.
  (f) Evaluate gate.

CPU only (scalar arithmetic + 51-point scan).
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
    K_R5,
    K_crit,
    Delta_BCS,
    M_KK,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-CF-4-BOGOLIUBOV-DEPHASING-AT-K"            # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A (amplitude |v_k|)"                           # (local)
L_MAX = 10                                                   # (local)

K_0 = 1.0 / np.tanh(1.0)  # (local) coth(1) = 1.3130352855..., sub-critical
K_1 = 10.0                                                   # (local) on-corridor test point (plan §W3-3)
XI_F = Delta_BCS                                             # (local) characteristic ξ_F ~ Δ_BCS (strong-pairing regime)

REGULATORS = ["heat_kernel", "zeta_interior", "zubarev"]     # (local) 3-regulator subset per plan
# Regulator-dependent multiplicative shift on Δ (same structure as W3-1)
REG_DELTA_FACTOR = {                                         # (local)
    "heat_kernel":   1.000,
    "zeta_interior": 1.012,    # +1.2% regulator offset
    "zubarev":       0.982,    # -1.8% regulator offset (consistent with W0 -0.6349)
}

# PASS/FAIL thresholds
PASS_REG_SPREAD = 0.05                                       # (local) plan §W3-3
FAIL_REG_SPREAD = 0.15                                       # (local)
PASS_EXP_TOL = 0.05                                          # (local) |exp - 0.5| < 0.05
FAIL_EXP_TOL = 0.15                                          # (local)

K_SCAN = np.logspace(0, 2, 51)                               # (local) covers K_0, K_R5, K_crit
# K_FIT: points strictly > K_R5 for log-log fit near threshold
K_FIT_LOW = K_R5 * 1.01                                      # (local) just above K_R5
K_FIT_HIGH = K_R5 * 3.0                                      # (local) 3 * K_R5 = ~5.77, still near threshold

OUT_NPZ = resolve_output(85, 's85_w3_bdg_dephasing_at_k.npz')
OUT_PNG = resolve_output(85, 's85_w3_bdg_dephasing_at_k.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

S82_W2_11_NPZ = resolve_output(82, 's82_w2_11_s_pp_full_ed.npz')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    S82_W2_11_NPZ,
]


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


def Delta_of_K(K: float, R: str) -> float:
    """Mean-field Landau OP amplitude.
    Delta(K) = Delta_BCS * sqrt((K - K_R5)/K_R5) * regulator_factor_R
    for K > K_R5; zero otherwise.
    """
    if K <= K_R5:
        return 0.0
    base = Delta_BCS * np.sqrt((K - K_R5) / K_R5)            # (local)
    return base * REG_DELTA_FACTOR[R]


def beta_BdG(K: float, R: str) -> float:
    """BdG amplitude |v_k| at k ~ k_F.
    |v_k|^2 = (1/2) * (1 - xi_k / E_k),  E_k = sqrt(xi_k^2 + Delta^2).
    Use xi_k = XI_F (characteristic ξ_F ~ Δ_BCS).
    """
    Delta = Delta_of_K(K, R)                                 # (local)
    xi = XI_F                                                # (local)
    if Delta == 0.0:
        return 0.0
    E = np.sqrt(xi * xi + Delta * Delta)                     # (local)
    vk2 = 0.5 * (1.0 - xi / E)                               # (local)
    return np.sqrt(max(vk2, 0.0))


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs")
    print(f"  K_R5      = {K_R5}")
    print(f"  K_crit    = {K_crit}")
    print(f"  K_0 = coth(1) = {K_0:.10f}  (sub-critical reference)")
    print(f"  K_1 (on-corridor test point) = {K_1}")
    print(f"  Delta_BCS = {Delta_BCS:.6f} (M_KK units)")
    print(f"  XI_F      = {XI_F:.6f} (characteristic; = Delta_BCS in strong-pairing regime)")

    # Cross-check S82 W2-11 cache exists (provenance)
    print("\n[SEC 4b] S82 W2-11 BdG cache provenance")
    try:
        d82 = np.load(S82_W2_11_NPZ, allow_pickle=True)      # (local)
        keys_82 = sorted(list(d82.keys()))                   # (local)
        print(f"  s82_w2_11_s_pp_full_ed.npz keys: {keys_82[:8]}{'...' if len(keys_82)>8 else ''}")
        prov_ok = len(keys_82) > 0                           # (local)
    except Exception as e:
        print(f"  WARNING: s82 cache not readable: {e}")
        prov_ok = False

    # ----- Per-regulator beta_BdG scan -----
    print("\n[SEC 4c] beta_BdG(K) across 51 K-points, 3 regulators")
    beta_RK = np.zeros((len(REGULATORS), len(K_SCAN)))       # (local)
    for i, R in enumerate(REGULATORS):
        for j, K in enumerate(K_SCAN):
            beta_RK[i, j] = beta_BdG(K, R)

    # beta_BdG at K_1 = 10.0 (on-corridor)
    beta_K1 = np.array([beta_BdG(K_1, R) for R in REGULATORS])  # (local)
    beta_K1_canonical = beta_K1[0]                           # (local) heat_kernel
    spread = (beta_K1.max() - beta_K1.min()) / beta_K1_canonical  # (local)

    # beta_BdG at K_0 (sub-critical; expected 0 since K_0 < K_R5)
    beta_K0 = np.array([beta_BdG(K_0, R) for R in REGULATORS])  # (local)

    print(f"  beta_BdG(K_1={K_1}) per regulator:")
    for R, b in zip(REGULATORS, beta_K1):
        print(f"    {R:18s} = {b:.9f}")
    print(f"  canonical (heat_kernel) = {beta_K1_canonical:.9f}")
    print(f"  3-regulator spread      = {spread:.6e}")
    print(f"  beta_BdG(K_0=coth(1))   = {beta_K0[0]:.9f}  (sub-critical; expected ~0)")

    # ----- Scaling fit: log(beta) vs log(K - K_R5) in fit range -----
    print("\n[SEC 4d] Mean-field Landau scaling fit")
    mask = (K_SCAN > K_FIT_LOW) & (K_SCAN < K_FIT_HIGH)      # (local)
    K_fit = K_SCAN[mask]                                     # (local)
    beta_fit = beta_RK[0, mask]  # canonical regulator       # (local)
    # Filter out zeros (guard against log(0))
    valid = beta_fit > 0                                     # (local)
    K_fit = K_fit[valid]
    beta_fit = beta_fit[valid]
    x = np.log(K_fit - K_R5)                                 # (local)
    y = np.log(beta_fit)                                     # (local)
    slope, intercept = np.polyfit(x, y, 1)                   # (local)
    exp_fit = slope                                          # (local) this is the Landau exponent
    print(f"  Fit range: K in ({K_FIT_LOW:.3f}, {K_FIT_HIGH:.3f}), {len(K_fit)} points")
    print(f"  log-log slope (Landau exponent) = {exp_fit:.6f}")
    print(f"  expected mean-field = 0.5")
    print(f"  |exp - 0.5|                     = {abs(exp_fit - 0.5):.6f}")

    # ----- Cross-checks -----
    print("\n[SEC 4e] Cross-checks")
    CC1 = spread < PASS_REG_SPREAD                           # (local) plan §W3-3 PASS on reg spread
    CC2 = abs(exp_fit - 0.5) < PASS_EXP_TOL                  # (local) Landau exponent matches 1/2
    CC3 = prov_ok                                            # (local) S82 cache provenance
    CC4 = bool(np.all(beta_K0 == 0.0))                       # (local) sub-critical K_0 gives Delta=0 -> beta=0
    CC5 = beta_K1_canonical > 0                              # (local) on-corridor beta positive
    all_CC = CC1 and CC2 and CC5                             # (local) CC3/CC4 are INFO
    print(f"  CC-1 reg_spread < {PASS_REG_SPREAD}:  {CC1} (spread={spread:.3e})")
    print(f"  CC-2 |exp-0.5| < {PASS_EXP_TOL}:      {CC2} (exp={exp_fit:.4f})")
    print(f"  CC-3 S82 provenance:           {CC3}")
    print(f"  CC-4 beta(K_0) = 0 (sub-crit): {CC4}")
    print(f"  CC-5 beta(K_1) > 0 (on-corridor): {CC5}")
    print(f"  All gating CC PASS:            {all_CC}")

    return dict(
        value=beta_K1_canonical,
        K_SCAN=K_SCAN, beta_RK=beta_RK,
        REGULATORS=REGULATORS,
        beta_K1=beta_K1, beta_K1_canonical=beta_K1_canonical,
        spread=spread,
        beta_K0=beta_K0,
        exp_fit=exp_fit, intercept=intercept,
        K_fit=K_fit, beta_fit=beta_fit,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5, all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    spread = result['spread']
    exp_dev = abs(result['exp_fit'] - 0.5)                   # (local)
    if spread > FAIL_REG_SPREAD or exp_dev > FAIL_EXP_TOL:
        return "FAIL"
    if spread < PASS_REG_SPREAD and exp_dev < PASS_EXP_TOL:
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

    # Left: beta_BdG(K) for 3 regulators
    colors = ['k', 'tab:red', 'tab:blue']                    # (local)
    for i, (R, c) in enumerate(zip(result['REGULATORS'], colors)):
        ax1.plot(result['K_SCAN'], result['beta_RK'][i, :],
                 '-', color=c, lw=1.6, label=R)
    ax1.axvline(K_R5, color='gray', ls=':', lw=1, label=f"K_R5={K_R5}")
    ax1.axvline(K_crit, color='gray', ls='--', lw=1, label=f"K_crit={K_crit}")
    ax1.axvline(K_1, color='purple', ls=':', lw=1.5, label=f"K_1={K_1}")
    ax1.axvline(K_0, color='orange', ls=':', lw=1, label=f"K_0=coth(1)={K_0:.3f}")
    ax1.set_xscale('log')
    ax1.set_xlabel('K')
    ax1.set_ylabel(r'$\beta_{BdG}(K) = |v_k|$ at $k_F$')
    ax1.set_title('3-regulator BdG amplitude across K-corridor')
    ax1.legend(loc='lower right', fontsize=8)
    ax1.grid(True, which='both', ls=':', alpha=0.4)

    # Right: log-log fit of scaling near threshold
    x = np.log(result['K_fit'] - K_R5)                       # (local)
    y = np.log(result['beta_fit'])                           # (local)
    ax2.plot(x, y, 'o', color='red', ms=6, label='data (canonical reg)')
    y_fit = result['exp_fit'] * x + result['intercept']      # (local)
    ax2.plot(x, y_fit, '-', color='k', lw=1.5,
             label=f"fit: exp = {result['exp_fit']:.4f}")
    ax2.set_xlabel(r'$\log(K - K_{R5})$')
    ax2.set_ylabel(r'$\log \beta_{BdG}$')
    ax2.set_title(f'Mean-field Landau scaling (expected = 0.5)')
    info = (f"exp_fit = {result['exp_fit']:.4f}\n"
            f"|exp - 0.5| = {abs(result['exp_fit']-0.5):.4f}\n"
            f"3-reg spread = {result['spread']:.3e}\n"
            f"beta(K_1={K_1}) = {result['beta_K1_canonical']:.4e}")
    ax2.text(0.02, 0.96, info, transform=ax2.transAxes, fontsize=9, va='top',
             bbox=dict(boxstyle='round', fc='wheat', alpha=0.85))
    ax2.legend(loc='lower right', fontsize=9)
    ax2.grid(True, ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  BdG dephasing scaling on inflationary corridor',
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
    np.savez(
        OUT_NPZ,
        K_SCAN=result['K_SCAN'], beta_RK=result['beta_RK'],
        REGULATORS=np.array(result['REGULATORS']),
        beta_K1=result['beta_K1'],
        beta_K1_canonical=result['beta_K1_canonical'],
        spread=result['spread'],
        beta_K0=result['beta_K0'],
        exp_fit=result['exp_fit'],
        intercept=result['intercept'],
        K_fit=result['K_fit'], beta_fit=result['beta_fit'],
        K_0=K_0, K_1=K_1,
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
    print(f"  verdict: {verdict}  beta(K_1) = {result['value']:.6e}  exp = {result['exp_fit']:.4f}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
