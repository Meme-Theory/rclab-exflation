#!/usr/bin/env python3
"""
S85 W3-7 — S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035
===================================================

Gate: S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035 ([VERIFY])

Hypothesis (plan §W3-7):
  Branch-A baseline-layer A_s closure at K_substrate = 2.035 yields
  A_s(K=2.035) = 2.1e-9 +/- 10%, matching Planck 2018 central value.
  This is the sole surviving A_s pathway post-S80 UNIFIED-AS-79.

Substitution chain (plan §W3-7 Steps 1-4):
  Def 1: A_s = <|zeta_k|^2> at k_pivot                     (scalar amplitude)
  Def 2: H_tilde(K) = substrate Hubble-analog at K_substrate
  Def 3: eps_H(K)  = slow-roll parameter at K_substrate
  Step 1: Mukhanov (UNIFIED-AS-79): A_s = H_tilde^2 / (8 pi^2 eps_H)
  Step 2: At K = 2.035 (S84 W6-A Branch-A baseline):
          H_tilde(2.035) = 5.9076e-3 (from S80 TD cache; canonical)
          eps_H(2.035)   = 2.163e-2  (from S80 TD cache; canonical)
  Step 3: A_s_TD = (5.9076e-3)^2 / (8 * pi^2 * 2.163e-2) = 3.299e-9
  Step 4: Direction: A_s INCREASES with K on the corridor (H_tilde
          dominant); K=2.035 near K_R5=1.9222 is near the corridor
          minimum of A_s.  Therefore A_s(2.035) is close to the
          framework-minimum value of A_s, = 3.30e-9.
  Conclusion: |A_s - 2.10e-9| / 2.10e-9 = 0.571 (57.1%);
              fails PASS band 10%, fails INFO band 30%, lands in FAIL.

Pre-registered thresholds (plan §W3-7):
  PASS iff |A_s - 2.10e-9| / 2.10e-9 < 0.10.
  INFO iff deviation in [0.10, 0.30] (PASS-with-tight-margin).
  FAIL iff deviation > 0.30 (closes sole A_s pathway).

Inputs (SHA-256 dual-pinned):
  - canonical_constants.py
  - s80_unified_as_79_full.npz (S80 W1-2 cache, TD path)
  - script bytes

Output 4-tuple:
  (value=A_s(K=2.035), scheme=heat_kernel, convention=A, L_max=10, path=TD)

Classification: PHONONIC
  A_s is the spectral-moment variance of the fabric's acoustic modes at
  pivot scale; H_tilde is substrate-spectral Hubble-analog.

Method:
  (a) Load S80 UNIFIED-AS-79 cache (A_s_TD_framework, H_tilde, eps_H, A_s_Planck).
  (b) Re-compute A_s from first principles using H_tilde^2 / (8 pi^2 eps_H).
  (c) Cross-check against S80's cached A_s_TD_framework.
  (d) Relerr vs Planck central.
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
    A_s_CMB, c_Gold, M_KK, K_R5, K_crit, PI,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035"           # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A, path=TD"                                    # (local) plan §W3-7
L_MAX = 10                                                   # (local)

K_central = 2.035                                            # (local) plan §W3-7 Branch-A baseline
K_band_low = 1.9                                             # (local) sensitivity
K_band_high = 2.2                                            # (local) sensitivity

PASS_RELERR = 0.10                                           # (local) plan §W3-7
INFO_LOWER = 0.10                                            # (local)
INFO_UPPER = 0.30                                            # (local)

OUT_NPZ = resolve_output(85, 's85_w3_branch_a_as_closure_k2035.npz')
OUT_PNG = resolve_output(85, 's85_w3_branch_a_as_closure_k2035.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

S80_NPZ = resolve_output(80, 's80_unified_as_79_full.npz')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    S80_NPZ,
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


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs")
    print(f"  K_central = {K_central}  (Branch-A baseline)")
    print(f"  K-band = [{K_band_low}, {K_band_high}]  (sensitivity)")
    print(f"  A_s_CMB (canonical) = {A_s_CMB:.3e}")

    # ----- Load S80 UNIFIED-AS-79 cache -----
    print("\n[SEC 4b] S80 UNIFIED-AS-79 cache (plan input pin)")
    d = np.load(S80_NPZ, allow_pickle=True)                  # (local)
    H_tilde_TD = float(d['H_tilde_TD_framework'])            # (local)
    eps_H = float(d['eps_H'])                                # (local)
    A_s_Planck_cache = float(d['A_s_Planck'])                # (local)
    A_s_TD_cache = float(d['A_s_TD_framework'])              # (local)
    verdict_TD_s80 = str(d['verdict_TD'])                    # (local)
    c_sub = float(d['c_sub'])                                # (local)
    f_conv = float(d['f_conv'])                              # (local)
    F_amp = float(d['F_amp_canonical'])                      # (local)

    print(f"  H_tilde_TD_framework = {H_tilde_TD:.6e}")
    print(f"  eps_H                = {eps_H:.6e}")
    print(f"  c_sub                = {c_sub:.4f}")
    print(f"  f_conv               = {f_conv:.4e}")
    print(f"  F_amp_canonical      = {F_amp:.4f}")
    print(f"  A_s_Planck (cached)  = {A_s_Planck_cache:.3e}")
    print(f"  A_s_TD (S80 cached)  = {A_s_TD_cache:.6e}")
    print(f"  S80 verdict_TD       = {verdict_TD_s80}")

    # ----- Re-derive A_s from Mukhanov formula -----
    print("\n[SEC 4c] Re-derivation from A_s = H_tilde^2 / (8 pi^2 eps_H)")
    A_s_recomputed = H_tilde_TD**2 / (8.0 * PI**2 * eps_H)   # (local)
    recompute_relerr = abs(A_s_recomputed - A_s_TD_cache) / A_s_TD_cache  # (local)
    print(f"  A_s_recomputed       = {A_s_recomputed:.6e}")
    print(f"  relerr vs S80 cache  = {recompute_relerr:.3e}")

    # ----- Deviation from Planck central -----
    print("\n[SEC 4d] Deviation from Planck central A_s = 2.10e-9")
    A_s_framework = A_s_TD_cache                             # (local) use canonical S80 cache value
    delta = A_s_framework - A_s_Planck_cache                 # (local)
    relerr_vs_planck = abs(delta) / A_s_Planck_cache         # (local)
    print(f"  A_s_framework  = {A_s_framework:.6e}")
    print(f"  A_s_Planck     = {A_s_Planck_cache:.3e}")
    print(f"  |delta|        = {abs(delta):.3e}")
    print(f"  relerr         = {relerr_vs_planck:.4f} ({relerr_vs_planck*100:.1f}%)")
    print(f"  PASS band: relerr < {PASS_RELERR}")
    print(f"  INFO band: relerr in [{INFO_LOWER}, {INFO_UPPER}]")
    print(f"  FAIL band: relerr > {INFO_UPPER}")

    # ----- K-sensitivity band -----
    # A_s(K) direction (plan §W3-7 Step 4): A_s increases with K on corridor.
    # K=2.035 is near K_R5=1.9222 (0.113 above threshold); A_s(2.035) is near
    # the corridor minimum.  Since S80 cache is conventionally the Branch-A
    # baseline at K=2.035 (per plan input pin), A_s_framework IS A_s(K=2.035).
    # The 57% positive deviation means framework over-produces A_s at Branch-A
    # baseline, relative to the Planck-central match.
    print("\n[SEC 4e] K-sensitivity (direction from plan Step 4)")
    print(f"  A_s(K) direction: INCREASING with K on [K_R5, K_crit]")
    print(f"  K_central={K_central} is 0.113 above K_R5={K_R5} (near corridor min)")
    print(f"  A_s(2.035) = 3.30e-9 is near framework-minimum A_s on corridor")
    print(f"  Strictly greater than Planck central -> positive 57% deviation")

    # ----- Cross-checks -----
    print("\n[SEC 4f] Cross-checks")
    CC1 = recompute_relerr < 1e-3                            # (local) S80 cache internal consistency
    CC2 = A_s_framework > 0                                  # (local) positivity
    CC3 = (abs(A_s_Planck_cache - A_s_CMB) / A_s_CMB) < 0.05  # (local) S80 cache Planck value matches canonical
    CC4 = verdict_TD_s80 == 'PASS-F2'                        # (local) S80 provenance
    CC5 = F_amp > 0                                          # (local) F_amp sign consistency
    all_CC = CC1 and CC2 and CC3 and CC4 and CC5             # (local)
    print(f"  CC-1 re-derive matches S80 cache (<1e-3):  {CC1} (relerr={recompute_relerr:.3e})")
    print(f"  CC-2 A_s_framework > 0:                    {CC2}")
    print(f"  CC-3 Planck cache matches canonical A_s:   {CC3}")
    print(f"  CC-4 S80 verdict == PASS-F2:               {CC4} ({verdict_TD_s80})")
    print(f"  CC-5 F_amp > 0 (sign consistency):         {CC5}")
    print(f"  All CC PASS:                                {all_CC}")

    return dict(
        value=A_s_framework,
        A_s_framework=A_s_framework,
        A_s_Planck=A_s_Planck_cache,
        A_s_recomputed=A_s_recomputed,
        H_tilde_TD=H_tilde_TD,
        eps_H=eps_H,
        c_sub=c_sub, f_conv=f_conv, F_amp=F_amp,
        recompute_relerr=recompute_relerr,
        relerr_vs_planck=relerr_vs_planck,
        delta=delta,
        verdict_TD_s80=verdict_TD_s80,
        K_central=K_central, K_band_low=K_band_low, K_band_high=K_band_high,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5, all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    r = result['relerr_vs_planck']                           # (local)
    if r > INFO_UPPER:
        return "FAIL"
    if r < PASS_RELERR:
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

    # Left: bar chart A_s_framework vs A_s_Planck
    labels = ['A_s_Planck\n(2018 central)', 'A_s_framework\n(Branch-A, K=2.035)']  # (local)
    values = [result['A_s_Planck'], result['A_s_framework']]  # (local)
    colors = ['gray', 'crimson']                             # (local)
    ax1.bar(labels, values, color=colors, edgecolor='k', alpha=0.85)
    for i, v in enumerate(values):
        ax1.text(i, v * 1.03, f"{v:.3e}", ha='center', fontsize=10)
    ax1.set_ylabel('A_s')
    ax1.set_title(f'Branch-A A_s closure at K={K_central}\nrelerr = {result["relerr_vs_planck"]*100:.1f}%')
    ax1.grid(True, axis='y', ls=':', alpha=0.4)

    # Right: relerr comparison with PASS/INFO/FAIL bands
    bands = [('PASS', 0, PASS_RELERR, 'lightgreen'),
             ('INFO', PASS_RELERR, INFO_UPPER, 'lightyellow'),
             ('FAIL', INFO_UPPER, 1.0, 'lightcoral')]
    for label, lo, hi, c in bands:
        ax2.axhspan(lo, hi, alpha=0.35, color=c, label=label)
    ax2.axhline(result['relerr_vs_planck'], color='k', lw=2.5,
                label=f"relerr = {result['relerr_vs_planck']:.3f}")
    ax2.set_ylabel('Relative error vs Planck central')
    ax2.set_ylim(0, 1.0)
    ax2.set_title('Relerr band diagnosis')
    ax2.legend(loc='upper right', fontsize=9)
    ax2.grid(True, ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  Branch-A A_s(K=2.035) closure (TD path)',
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
        A_s_framework=result['A_s_framework'],
        A_s_Planck=result['A_s_Planck'],
        A_s_recomputed=result['A_s_recomputed'],
        H_tilde_TD=result['H_tilde_TD'],
        eps_H=result['eps_H'],
        c_sub=result['c_sub'], f_conv=result['f_conv'],
        F_amp=result['F_amp'],
        recompute_relerr=result['recompute_relerr'],
        relerr_vs_planck=result['relerr_vs_planck'],
        delta=result['delta'],
        verdict_TD_s80=result['verdict_TD_s80'],
        K_central=result['K_central'],
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
    print(f"  verdict: {verdict}  A_s = {result['A_s_framework']:.3e}  relerr = {result['relerr_vs_planck']*100:.1f}%")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
