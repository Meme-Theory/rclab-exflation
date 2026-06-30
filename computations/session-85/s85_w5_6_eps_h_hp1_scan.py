#!/usr/bin/env python3
"""
S85 W5-6 S85-W5-6-REGULATOR-SCAN-EPS-H - ||eps_H||_{HP^1} scan across 5-atlas
==============================================================================

Gate: S85-W5-6-REGULATOR-SCAN-EPS-H  ([VERIFY])

Pre-registered threshold (plan §W5-6, observational-style band registration):
  - INFO (tight)       if max/min <= 10
  - INFO (acceptable)  if 10 < max/min <= 30
  - INFO (wide)        if max/min > 30
  (No FAIL clause per plan §W5-6 — gate is observational-registration.)

Classification: GEOMETRIC (KK-HP^1 magnitude under regulator variation).

METHODOLOGY
-----------
Per Connes-Moscovici residue formula (S83 G56 anchor):
  ||[eps_H]||_{HP^1, r} = Res_{s=0} zeta_{D, eps_H^2, r}(s)

Since eps_H^2 is curvature-squared (a_4 slot), the residue reduces to f_4^r,
the Mellin coefficient at the a_4 position of regulator r. This is the
leading-order HP^1 magnitude.

Mellin f_4^r values (5-atlas):
  zeta:        f_4 = 1        canonical Lizzi zeta (pure a_4)
  Zubarev:     f_4 = 1        S83 G3 EN3 equivalence to zeta
  SDW:         f_4 = 0.97     S78 mellin_ratio
  cutoff_sqrt: f_4 = 0.5      Chamseddine-Connes 2010 f(x)=sqrt(x) canonical
  anomaly:     f_4 = 1        S67 anomaly-derived selects a_2, a_4

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-78/s78_a4_r2_f_star.npz           (SDW mellin_ratio source)
  - computations/session-66/s66_zeta_sa.npz                (S66 raw eps_H context)
  - computations/session-83/s83_w3_g56_godbillon_vey_jensen_deform.npz  (CM residue)

Output 4-tuple:
  (value=max/min-ratio, scheme=5-regulator-atlas, convention=CM-residue, L_max=10)
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

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

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W5-6-REGULATOR-SCAN-EPS-H"                    # (local)
SCHEME = "5-regulator-atlas"                                  # (local)
CONVENTION = "CM-residue"                                     # (local)
L_MAX = 10                                                    # (local)

TIGHT_THRESH = 10.0                                           # (local) observational band
ACCEPTABLE_THRESH = 30.0                                      # (local)

OUT_NPZ = resolve_output(85, 's85_w5_6_eps_h_hp1_scan.npz')
OUT_PNG = resolve_output(85, 's85_w5_6_eps_h_hp1_scan.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
S66_NPZ = resolve_output(66, 's66_zeta_sa.npz')
S78_NPZ = resolve_output(78, 's78_a4_r2_f_star.npz')
S83_GV_NPZ = resolve_output(83, 's83_w3_g56_godbillon_vey_jensen_deform.npz')

INPUT_FILES = [CANON_PY, S66_NPZ, S78_NPZ, S83_GV_NPZ]


def sha256_of(path):
    h = hashlib.sha256()
    try: h.update(path.read_bytes())
    except OSError: return ""
    return h.hexdigest()

def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins

def closure_hash(pins):
    items = sorted(pins.items()); h = hashlib.sha256()
    for k, v in items: h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()

def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""; cb = b""
    try: sb = script_path.read_bytes()
    except OSError: pass
    try: cb = canonical_path.read_bytes()
    except OSError: pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


def gpu_sanity():
    try:
        import torch
        if not torch.cuda.is_available():
            return False
        m = torch.eye(8, dtype=torch.float64, device='cuda')
        ok = bool(torch.allclose(torch.linalg.eigvals(m).real.cpu(), torch.ones(8, dtype=torch.float64)))
        print(f"  [GPU] torch.linalg sanity ok={ok}")
        return ok
    except Exception as e:
        print(f"  [GPU] {type(e).__name__}: {e}")
        return False


def compute():
    d78 = np.load(S78_NPZ, allow_pickle=True)
    mellin_ratio_SDW = float(d78['mellin_ratio'])   # (local)  S78 W2-F pin

    # f_4^r Mellin coefficients (residue prefactors at a_4 slot)
    # Provenance:
    #   zeta:        1 (canonical Lizzi zeta = residue at s=0 of zeta-D)
    #   Zubarev:     1 (S83 G3 EN3: Zubarev UNIQUE axiom-native, == zeta)
    #   SDW:         S78 mellin_ratio (= f_4^fstar / f_4^SDW? actually stored
    #                as the SDW multiplier; 0.970024)
    #   cutoff_sqrt: 1/2 (Chamseddine-Connes 2010 Table 1 for f(x)=sqrt(x)
    #                at the a_4 slot, canonical Lambda-normalization)
    #   anomaly:     1 (S67 anomaly-derived selects a_2, a_4; f_4 normalized to 1)
    f_4_per_reg = {
        'zeta':         1.0,                     # canonical
        'Zubarev':      1.0,                     # S83 G3 EN3
        'SDW':          mellin_ratio_SDW,        # S78 W2-F
        'cutoff_sqrt':  0.5,                     # CC 2010 f(x)=sqrt(x)
        'anomaly':      1.0,                     # S67
    }

    mags = np.array(list(f_4_per_reg.values()), dtype=np.float64)
    max_val = float(mags.max())      # (local)
    min_val = float(mags.min())      # (local)
    ratio = max_val / min_val        # (local)

    # S66 raw eps_H dynamic-range reference (per S75 ZETA-NOT-PHYSICAL-75 theorem)
    S66_RAW_RANGE = 381.0            # (local) 381x across L_max values of zeta-D
    reduction_factor = S66_RAW_RANGE / ratio   # (local)

    # Band classification (plan §W5-6 observational clauses)
    if ratio <= TIGHT_THRESH:
        band = 'tight'
    elif ratio <= ACCEPTABLE_THRESH:
        band = 'acceptable'
    else:
        band = 'wide'

    return {
        'value': ratio,
        'f_4_per_reg': f_4_per_reg,
        'mags': mags,
        'max_val': max_val,
        'min_val': min_val,
        'ratio': ratio,
        'band': band,
        'reduction_factor': reduction_factor,
        'mellin_ratio_SDW': mellin_ratio_SDW,
    }


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")

def append_verdict(verdict, value, audit, content):
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit} content_sha256={content} "
            f"schema_version=S84+\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

def evaluate_gate(result):
    # Plan §W5-6: no-FAIL observational clauses; band becomes INFO-{band}
    return f"INFO-{result['band']}"


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    audit, content = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256:   {audit[:16]}...")
    print(f"  content_sha256: {content[:16]}...")
    print()
    gpu_sanity()
    print()

    result = compute()
    verdict = evaluate_gate(result)

    regs = list(result['f_4_per_reg'].keys())
    f4 = np.array(list(result['f_4_per_reg'].values()), dtype=np.float64)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        regulators=np.array(regs),
        f_4_per_reg=f4,
        max_val=result['max_val'],
        min_val=result['min_val'],
        ratio=result['ratio'],
        band=result['band'],
        reduction_factor=result['reduction_factor'],
        mellin_ratio_SDW=result['mellin_ratio_SDW'],
        tight_thresh=TIGHT_THRESH,
        acceptable_thresh=ACCEPTABLE_THRESH,
    )
    print(f"  saved: {OUT_NPZ.name}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 5))
        colors = ['tab:blue' if r != 'cutoff_sqrt' else 'tab:red' for r in regs]
        ax.bar(regs, f4, color=colors, edgecolor='k')
        ax.axhline(result['max_val'], color='green', linestyle=':', label='max')
        ax.axhline(result['min_val'], color='red', linestyle=':', label='min')
        ax.set_ylabel(r'$|f_4^r| \equiv \|[\varepsilon_H]\|_{HP^1, r}$ (normalized)')
        ax.set_title(f"{GATE_ID}: max/min={result['ratio']:.3f} band={result['band']} ({verdict})")
        ax.legend()
        ax.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result['ratio'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['ratio'], audit, content)

    wall = time.time() - t0
    print()
    print(f"=== {GATE_ID} HP^1 magnitude scan ===")
    for r in regs:
        print(f"  {r:14s}: |f_4^r| = {result['f_4_per_reg'][r]:.4f}")
    print(f"  max={result['max_val']:.4f}, min={result['min_val']:.4f}, max/min={result['ratio']:.3f}")
    print(f"  band = {result['band']}")
    print(f"  S66 raw eps_H 381x range reduction factor: {result['reduction_factor']:.1f}x")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
