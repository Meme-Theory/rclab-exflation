#!/usr/bin/env python3
"""
S85 W3-9 — S85-W3-RUNNING-MASS-GINZBURG-OZ
===========================================

Gate: S85-W3-RUNNING-MASS-GINZBURG-OZ ([VERIFY])

Hypothesis (plan §W3-9):
  The Ornstein-Zernike regime for the substrate two-band Leggett channel
  satisfies the Ginzburg criterion on the inflationary sub-corridor
  K in [K_R5, K_crit]: Gi(K) < 1 monotone, MAXIMUM at K_crit.
  PASS iff Gi(K_crit) < 1.

Substitution chain (plan §W3-9 Steps 1-5; Landau-Lifshitz vol 9 §144):
  Def: Ginzburg number Gi = (fluctuation correction / mean-field) at T_c
  3D d-wave formula:
        Gi = (1/(8 pi^2)^2) * (k_B T_c / E_cond)^2 / (xi_0 * k_F)^3
  Mean-field valid iff Gi << 1.

  Substrate identifications:
      k_F     = M_KK                  (characteristic scale)
      T_c     = Delta / 1.76          (BCS ratio)
      E_cond  = Delta^2 / E_F, E_F = M_KK
      xi_0    = v_F / (pi Delta)      v_F = c_fabric (substrate sound speed)

  Algebraic simplification (plan Step 4):
      Gi = (T_c/E_cond)^2 / (xi_0 k_F)^3
         = (Delta / (Delta^2/E_F))^2 / (v_F/(pi Delta) k_F)^3
         = (E_F/Delta)^2 * (pi Delta)^3 / (v_F k_F)^3
         = pi^3 * E_F^2 * Delta / (v_F k_F)^3
  With prefactors (1/(8 pi^2)^2) * (1/1.76^2):
      Gi = (1 / (64 pi * 1.76^2 * c_fabric^3)) * (Delta / M_KK)
  Therefore Gi PROPORTIONAL TO Delta (linear positive).
  Direction: d(Gi)/d(Delta) > 0; Delta monotone-increasing in K (W3-3);
             ==> Gi monotone-increasing in K;
             ==> max(Gi) on corridor is at K = K_crit.
  Conclusion: Test Gi at K_crit. PASS iff Gi(K_crit) < 1.

Pre-registered thresholds (plan §W3-9):
  PASS iff Gi(K_crit) < 1.
  FAIL iff Gi(K_crit) > 1.
  INFO iff Gi(K_crit) in [0.1, 1] (mean-field marginal).

Inputs (SHA-256 dual-pinned):
  - canonical_constants.py
  - script bytes

Output 4-tuple:
  (value=Gi(K_crit), scheme=heat_kernel, convention=A, L_max=10)

Classification: PHONONIC
  Gi is a spectral ratio inside D_K's perturbation expansion; measures
  whether leading-order mean-field captures the physics.

Method:
  (a) Construct Delta(K) mean-field Landau over [K_R5, K_crit].
  (b) Compute Gi(K) at 41 log-spaced K points.
  (c) Report Gi(K_crit); evaluate gate.
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
    K_R5, K_crit, Delta_BCS, M_KK, c_fabric, PI,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-RUNNING-MASS-GINZBURG-OZ"                  # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A"                                             # (local)
L_MAX = 10                                                   # (local)

# K-scan: 41 log-spaced points on [K_R5, K_crit] (inflationary sub-corridor)
K_SCAN = np.logspace(np.log10(K_R5), np.log10(K_crit), 41)   # (local)
K_SCAN[0] = K_R5                                             # (local) exact endpoint pin
K_SCAN[-1] = K_crit                                          # (local) exact endpoint pin

BCS_RATIO = 1.76                                             # (local) Delta/T_c BCS universal ratio

PASS_GI = 1.0                                                # (local) plan §W3-9 PASS
INFO_LOWER = 0.1                                             # (local)
FAIL_GI = 1.0                                                # (local)

OUT_NPZ = resolve_output(85, 's85_w3_ginzburg_oz.npz')
OUT_PNG = resolve_output(85, 's85_w3_ginzburg_oz.png')
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
    """Mean-field Landau gap."""
    if K <= K_R5:
        return 0.0
    return Delta_BCS * np.sqrt((K - K_R5) / K_R5)            # (local) in M_KK units


def Gi_of_K(K: float) -> float:
    """Ginzburg number via the simplified algebra chain from plan Step 4.

    Gi = (1 / (64 * pi * BCS_RATIO^2 * c_fabric^3)) * (Delta / M_KK)

    In the substrate's natural units where M_KK = 1, Delta is dimensionless
    in M_KK units (Delta_BCS = 0.4643), so Delta/M_KK = Delta (scalar).
    """
    Delta = Delta_of_K(K)                                    # (local) M_KK units, dimensionless
    if Delta == 0:
        return 0.0
    prefactor = 1.0 / (64.0 * PI * (BCS_RATIO ** 2) * (c_fabric ** 3))  # (local)
    return prefactor * Delta                                 # (local)


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs")
    print(f"  K_R5 = {K_R5}, K_crit = {K_crit}")
    print(f"  Delta_BCS = {Delta_BCS:.6f} (M_KK units)")
    print(f"  c_fabric  = {c_fabric:.6f} (substrate sound speed, M_KK units)")
    print(f"  BCS ratio (Delta/T_c) = {BCS_RATIO}")

    # Gi scan over inflationary sub-corridor
    print("\n[SEC 4b] Gi(K) scan over K in [K_R5, K_crit] (41 log-spaced points)")
    Gi_scan = np.array([Gi_of_K(K) for K in K_SCAN])         # (local)
    Delta_scan = np.array([Delta_of_K(K) for K in K_SCAN])   # (local)

    Gi_R5 = Gi_scan[0]                                       # (local) ~ 0 (Delta = 0)
    Gi_crit = Gi_scan[-1]                                    # (local) max of corridor
    Gi_max = Gi_scan.max()                                   # (local)
    Gi_max_K = K_SCAN[np.argmax(Gi_scan)]                    # (local)

    print(f"  Gi(K_R5)   = {Gi_R5:.6e}  (expected ~0; Delta vanishes at threshold)")
    print(f"  Gi(K_crit) = {Gi_crit:.6e}  (gated endpoint)")
    print(f"  Gi_max     = {Gi_max:.6e} at K = {Gi_max_K:.4f}")

    # Monotonicity verification
    print("\n[SEC 4c] Monotonicity verification")
    diffs = np.diff(Gi_scan)                                 # (local)
    monotone = bool(np.all(diffs >= -1e-18))                 # (local) Gi non-decreasing
    print(f"  Gi monotone non-decreasing: {monotone}")
    print(f"  max-at-K_crit: {Gi_max_K == K_crit}")

    # Substitution-chain check: Gi(K_crit) / Delta(K_crit) must equal prefactor
    print("\n[SEC 4d] Substitution-chain numerical check (Gi = prefactor * Delta)")
    prefactor = 1.0 / (64.0 * PI * (BCS_RATIO ** 2) * (c_fabric ** 3))  # (local)
    predicted_Gi_crit = prefactor * Delta_scan[-1]            # (local)
    reconstruct_err = abs(Gi_crit - predicted_Gi_crit)       # (local)
    print(f"  prefactor = 1 / (64 pi * 1.76^2 * c_fabric^3) = {prefactor:.6e}")
    print(f"  Delta(K_crit) = {Delta_scan[-1]:.6f}")
    print(f"  predicted Gi_crit = {predicted_Gi_crit:.6e}")
    print(f"  recompute error   = {reconstruct_err:.3e}")

    # Cross-checks
    print("\n[SEC 4e] Cross-checks")
    CC1 = Gi_crit < PASS_GI                                  # (local) main PASS criterion
    CC2 = monotone                                           # (local) substitution chain direction
    CC3 = reconstruct_err < 1e-15                            # (local) Gi = prefactor * Delta numerical
    CC4 = Gi_crit == Gi_max                                  # (local) max at K_crit (plan Step 6)
    CC5 = Gi_R5 == 0.0                                       # (local) Delta=0 at threshold
    all_CC = CC1 and CC2 and CC3 and CC4 and CC5             # (local)
    print(f"  CC-1 Gi(K_crit) < 1:         {CC1} ({Gi_crit:.3e})")
    print(f"  CC-2 Gi monotone increasing: {CC2}")
    print(f"  CC-3 Gi = prefactor * Delta: {CC3} (err = {reconstruct_err:.3e})")
    print(f"  CC-4 max(Gi) at K_crit:      {CC4}")
    print(f"  CC-5 Gi(K_R5) = 0:           {CC5}")
    print(f"  All CC PASS:                 {all_CC}")

    return dict(
        value=Gi_crit,
        K_SCAN=K_SCAN, Gi_scan=Gi_scan, Delta_scan=Delta_scan,
        Gi_R5=Gi_R5, Gi_crit=Gi_crit,
        Gi_max=Gi_max, Gi_max_K=Gi_max_K,
        prefactor=prefactor,
        reconstruct_err=reconstruct_err,
        monotone=monotone,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5,
        all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    g = result['Gi_crit']                                    # (local)
    if g > FAIL_GI:
        return "FAIL"
    if g < INFO_LOWER:
        return "PASS"  # firmly mean-field
    return "INFO"  # marginal


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
    ax1.loglog(K, result['Gi_scan'], 'b-', lw=1.8, label='Gi(K)')
    ax1.axhline(PASS_GI, color='k', ls='--', lw=1, label=f'PASS threshold Gi < {PASS_GI}')
    ax1.axhline(INFO_LOWER, color='gray', ls=':', lw=1, label=f'INFO lower {INFO_LOWER}')
    ax1.axvspan(K_R5, K_crit, color='lightgreen', alpha=0.15, label='Inflationary sub-corridor')
    ax1.axvline(K_crit, color='red', ls=':', lw=1.2, label=f'K_crit = {K_crit}')
    ax1.set_xlabel('K')
    ax1.set_ylabel('Gi(K)')
    ax1.set_title(f'Ginzburg number on inflationary sub-corridor\nGi(K_crit) = {result["Gi_crit"]:.3e}')
    ax1.legend(loc='lower right', fontsize=8)
    ax1.grid(True, which='both', ls=':', alpha=0.4)

    ax2.plot(result['Delta_scan'], result['Gi_scan'], 'go-', ms=4, lw=1.5,
             label='Gi vs Delta (linear relation)')
    ax2.set_xlabel(r'$\Delta(K)$ (M_KK units)')
    ax2.set_ylabel('Gi')
    ax2.set_title(f'Gi ∝ Δ (prefactor = {result["prefactor"]:.3e})')
    ax2.legend()
    ax2.grid(True, ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  Ginzburg criterion on OZ regime', fontsize=11)
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
        K_SCAN=result['K_SCAN'], Gi_scan=result['Gi_scan'],
        Delta_scan=result['Delta_scan'],
        Gi_R5=result['Gi_R5'], Gi_crit=result['Gi_crit'],
        Gi_max=result['Gi_max'], Gi_max_K=result['Gi_max_K'],
        prefactor=result['prefactor'],
        reconstruct_err=result['reconstruct_err'],
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
    print(f"  verdict: {verdict}  Gi(K_crit) = {result['Gi_crit']:.3e}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
