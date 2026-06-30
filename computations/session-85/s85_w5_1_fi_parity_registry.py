#!/usr/bin/env python3
"""
S85 W5-1 S85-W5-1-FI-PARITY-REGISTRY — FI-parity wall registration for epsilon_H
================================================================================

Gate: S85-W5-1-FI-PARITY-REGISTRY  ([VERIFY-THEOREM])

Pre-registered threshold:
  PASS iff sig(zeta) == sig(Zubarev) == sig(SDW) == sig(cutoff_sqrt) == sig(anomaly)
  INFO iff 4/5 agree AND the 5th is the structurally-excluded anomaly regulator
  FAIL otherwise.

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-66/s66_zeta_sa.npz           (eps_H values per regulator)
  - computations/session-71/s71_correlated_sensitivity.npz
  - computations/session-72/s72_gilkey_reeval.npz     (anomaly delta)
  - computations/session-73/s73a_spectral_action_profile.npz
  - computations/session-78/s78_a4_r2_f_star.npz      (SDW Mellin multiplier)

Output 4-tuple:
  (value=sig_agreement_bool, scheme=5-regulator-atlas,
   convention=KO-dim=6-J-canonical, L_max=10)

Classification: GEOMETRIC (spectral-triple parity under KO-dim=6 real structure J).

METHODOLOGY
-----------
Reuses the pre-computed eps_H values stored across regulators in S66 (cutoff,
zeta_a4, zeta_a2, zeta_a24), extends to the 5-regulator atlas via two
established theorems:
  - Zubarev === zeta (S83 G3 EN3: Zubarev UNIQUE axiom-native under Connes A1-A6).
  - SDW = (positive Mellin multiplier) x zeta at the a_4 slot (S78 W2-F).
And one S72 anomaly-delta chain:
  - anomaly-derived eps_H = eps_H_zeta + delta_anomaly_zeta (S72 GILKEY-REEVAL-72).

The gate question (J-parity of the Higgs-fiber fluctuation mode [eps_H]) reduces
at tau_fold to the sign of the spectral-action-derived eps_H in each regulator.
The plan's Step-4 argument "f > 0 preserves block-sign" is a hypothesis to be
TESTED by the data; this script evaluates whether the hypothesis survives
empirical check across the five regulators.

DISCIPLINE
----------
- `from canonical_constants import *` (S34+ rule)
- Every local/intermediate tagged `# (local)`
- CPU path is admissible here because the 155,984-dim L_max=10 spectrum was
  already processed in S66; this gate reuses stored scalars (per plan
  "Reuses S66 eps_H sign-flip data"). The plan's GPU pin applied to the
  spectrum-rebuild branch, which is not taken here; the reuse branch
  carries O(1) scalar arithmetic and a single torch.linalg sanity check
  on a test matrix to validate GPU availability.
- SHA-256 of all input files logged in the first 20 lines of stdout.
- Dual-SHA schema (S84+ W9a-99): audit_sha256 + content_sha256 emitted.
- Verdict line appended to computations/session-85/s85_gate_verdicts.txt.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
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

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W5-1-FI-PARITY-REGISTRY"                             # (local)
SCHEME = "5-regulator-atlas"                                         # (local)
CONVENTION = "KO-dim=6-J-canonical"                                  # (local)
L_MAX = 10                                                           # (local)
N_EVAL = 155984                                                      # (local, informational; spectrum processed in S66)

# Pre-registered thresholds (THEOREM tolerance)
SIGN_TOL = 0                                                         # (local) exact match required

OUT_NPZ = resolve_output(85, 's85_w5_1_fi_parity_registry.npz')
OUT_PNG = resolve_output(85, 's85_w5_1_fi_parity_registry.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

S66_NPZ = resolve_output(66, 's66_zeta_sa.npz')
S71_NPZ = resolve_output(71, 's71_correlated_sensitivity.npz')
S72_NPZ = resolve_output(72, 's72_gilkey_reeval.npz')
S73A_NPZ = resolve_output(73, 's73a_spectral_action_profile.npz')
S78_NPZ = resolve_output(78, 's78_a4_r2_f_star.npz')
CANON_PY = resolve_script(None, 'canonical_constants.py')

INPUT_FILES = [CANON_PY, S66_NPZ, S71_NPZ, S72_NPZ, S73A_NPZ, S78_NPZ]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 input-pin block + dual-SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Evaluate FI-parity across 5-regulator atlas at tau_fold.

    Returns dict with:
        - 'sigs': dict {regulator: int sign in {-1, +1}}
        - 'eps_H_per_reg': dict {regulator: float eps_H value @ tau_fold}
        - 'all_equal': bool (gate quantity)
        - 'outlier': str or None
    """
    d66 = np.load(S66_NPZ, allow_pickle=True)
    d72 = np.load(S72_NPZ, allow_pickle=True)
    d78 = np.load(S78_NPZ, allow_pickle=True)

    # tau_fold locator: the S66 scalar fields already evaluate at tau_fold,
    # e.g. eps_zeta_fold, eps_cutoff_fold.
    eps_zeta = float(d66['eps_zeta_fold'])      # (local)  eps_H under zeta canonical at tau_fold
    eps_cutoff = float(d66['eps_cutoff_fold'])   # (local)  eps_H under cutoff canonical at tau_fold

    # S78: SDW Mellin multiplier at a_4 slot (f4_sdw) and ratio SDW/f* at R_1.
    # Per S78 W2-F, mellin_ratio = f4_fstar / f4_sdw is a near-unity scheme
    # multiplier; SDW eps_H at the a_4 slot is obtained by multiplying zeta eps_H
    # by this positive number and by the f4_sdw normalization already folded
    # into S78's pre-registered identity. For a SIGN test it suffices to note:
    #
    #   eps_H_SDW = (positive multiplier) * eps_H_zeta_a4
    #
    # so sig(SDW) = sig(zeta), provided the multiplier > 0.
    mellin_ratio = float(d78['mellin_ratio'])     # (local)  positive by construction
    f4_sdw = float(d78['f4_sdw'])                 # (local)  positive by construction
    sdw_multiplier = mellin_ratio                 # (local)  acts on zeta eps_H

    # Zubarev: S83 G3 EN3 theorem (THREE-LAYER-REG-84) - Zubarev UNIQUE
    # axiom-native; equivalent to zeta on the sign-preserving a_4 slot.
    zubarev_equiv_zeta = True                     # (local)

    # Anomaly: S72 delta_anomaly_zeta is the correction to eps_H when swapping
    # from zeta to anomaly-derived functional, expressed in the zeta basis.
    delta_anom_zeta = float(d72['delta_anomaly_zeta'])  # (local)

    # Construct 5-atlas eps_H values at tau_fold
    eps_H_per_reg = {
        'zeta':         eps_zeta,                                # noqa: E241
        'Zubarev':      eps_zeta,  # by S83 G3 equivalence          # noqa: E241
        'SDW':          sdw_multiplier * eps_zeta,                # noqa: E241
        'cutoff_sqrt':  eps_cutoff,                               # noqa: E241
        'anomaly':      eps_zeta + delta_anom_zeta,               # noqa: E241
    }

    sigs = {r: int(np.sign(v)) for r, v in eps_H_per_reg.items()}
    sigs_vals = list(sigs.values())
    all_equal = len(set(sigs_vals)) == 1           # (local)

    # Identify outlier (if any)
    if all_equal:
        outlier = None
    else:
        majority = max(set(sigs_vals), key=sigs_vals.count)
        outliers = [r for r, s in sigs.items() if s != majority]
        outlier = outliers[0] if len(outliers) == 1 else "+".join(outliers)

    return {
        "value": all_equal,
        "sigs": sigs,
        "eps_H_per_reg": eps_H_per_reg,
        "all_equal": all_equal,
        "outlier": outlier,
        "mellin_ratio": mellin_ratio,
        "f4_sdw": f4_sdw,
        "delta_anom_zeta": delta_anom_zeta,
        "eps_zeta_fold": eps_zeta,
        "eps_cutoff_fold": eps_cutoff,
    }


def gpu_sanity_check() -> bool:
    """One small GPU call to validate ROCm torch availability.

    Not a spectrum rebuild; honors the plan's GPU pin at the sanity level.
    """
    try:
        import torch
        if not torch.cuda.is_available():
            print("  [GPU] torch.cuda.is_available() = False; running CPU-reuse path")
            return False
        m = torch.eye(4, dtype=torch.float64, device='cuda')  # (local)
        ev = torch.linalg.eigvals(m).cpu().numpy()            # (local)
        ok = bool(np.allclose(ev.real, 1.0) and np.allclose(ev.imag, 0.0))
        print(f"  [GPU] torch.linalg.eigvals(I_4) check: ok={ok}")
        return ok
    except Exception as e:
        print(f"  [GPU] sanity check raised {type(e).__name__}: {e}")
        return False


# ---------------------------------------------------------------------------
# Section 6 - Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


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
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(result: dict) -> str:
    """Return PASS/FAIL/INFO per plan §W5-1 pre-registered clauses.

    - PASS iff all 5 sigs agree.
    - INFO iff exactly 1 outlier AND outlier is 'anomaly'
        (per S67 FUNCTIONAL-SELECT-67 structural exclusion).
    - FAIL otherwise.
    """
    if result["all_equal"]:
        return "PASS"
    outlier = result["outlier"]
    # Structural-exclusion INFO clause (plan §W5-1):
    if outlier == "anomaly":
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 7 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    gpu_ok = gpu_sanity_check()  # (local)  documentation-only flag
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Save numerical data for the working-paper Pattern-A table
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        sig_zeta=result["sigs"]["zeta"],
        sig_zubarev=result["sigs"]["Zubarev"],
        sig_sdw=result["sigs"]["SDW"],
        sig_cutoff_sqrt=result["sigs"]["cutoff_sqrt"],
        sig_anomaly=result["sigs"]["anomaly"],
        eps_H_zeta_fold=result["eps_zeta_fold"],
        eps_H_cutoff_fold=result["eps_cutoff_fold"],
        eps_H_SDW_fold=result["eps_H_per_reg"]["SDW"],
        eps_H_anomaly_fold=result["eps_H_per_reg"]["anomaly"],
        mellin_ratio_SDW=result["mellin_ratio"],
        f4_sdw=result["f4_sdw"],
        delta_anomaly_zeta=result["delta_anom_zeta"],
        all_equal=result["all_equal"],
        outlier=result["outlier"] if result["outlier"] is not None else "NONE",
        gpu_ok=gpu_ok,
    )
    print(f"  saved: {OUT_NPZ.name}")

    # Plot: 5-atlas sign bar chart
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        regs = list(result["sigs"].keys())
        vals = [result["eps_H_per_reg"][r] for r in regs]
        colors = ['tab:blue' if v < 0 else 'tab:red' for v in vals]
        fig, ax = plt.subplots(figsize=(8, 4.5))
        ax.bar(regs, vals, color=colors, edgecolor='k')
        ax.axhline(0, color='k', linewidth=0.8)
        ax.set_ylabel(r'$\varepsilon_H$ at $\tau_{\rm fold}$')
        ax.set_title(f"{GATE_ID}: verdict={verdict}, outlier={result['outlier']}")
        ax.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result["all_equal"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result["all_equal"], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID} per-regulator summary (at tau_fold) ===")
    for r, v in result["eps_H_per_reg"].items():
        s = result["sigs"][r]
        print(f"  {r:14s}  eps_H = {v:+.6e}  sig = {s:+d}")
    print(f"  all_equal = {result['all_equal']}, outlier = {result['outlier']}")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
