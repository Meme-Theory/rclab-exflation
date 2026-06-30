#!/usr/bin/env python3
"""
S85 W5-2 S85-W5-2-HP0-INTRA-CORRIDOR - HP^0(A_F) factorization test across 5-atlas
===================================================================================

Gate: S85-W5-2-HP0-INTRA-CORRIDOR  ([VERIFY])

Pre-registered threshold:
  PASS iff for all 5 regulators r, M(r, i) = <eps_H, nu_i>_r / <eps_H, nu_i>_zeta
    is basis-element-independent within 5% multiplicative tolerance across
    4 CCM-2008 basis elements nu_i of HP^0(A_F).
  INFO iff 4/5 regulators factorize AND the outlier is anomaly (per S67).
  FAIL otherwise.

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-78/s78_a4_r2_f_star.npz  (SDW Mellin multiplier at a_4)
  - computations/session-66/s66_zeta_sa.npz       (eps_H baseline context)
  - computations/session-72/s72_gilkey_reeval.npz (anomaly reference)

Output 4-tuple:
  (value=M_table_5x4, scheme=5-regulator-atlas, convention=CCM-2008-A_F-basis,
   L_max=3)

Classification: GEOMETRIC (KK-HP^0 cohomology intra-corridor).

METHODOLOGY
-----------
The pairing <[eps_H], nu_i>_r factorizes into a regulator-Mellin vector
(f_0^r, f_2^r, f_4^r, f_6^r) dotted with a basis-character vector
(m_0^i, m_2^i, m_4^i, m_6^i). Under the plan's Step-5 prediction (extension
of S78 W2-F Mellin-multiplier scheme-invariance theorem to HP^0), M(r, i)
should be i-independent IFF the regulator is "pure-a_4" in its Mellin
support. This script tabulates M for 5 regulators x 4 CCM-2008 basis
elements, computes max/min spread per regulator, compares to 5% tolerance.

Mellin vectors sourced from S83 G3 (Zubarev equivalent to zeta),
S78 W2-F (mellin_ratio = 0.970024 for SDW at a_4 slot),
Chamseddine-Connes 2010 (cutoff_sqrt f(x)=sqrt(x) heat-kernel moments
f_0=2, f_2=1, f_4=1/2, f_6=1/10 at canonical Lambda-normalization),
S67 FUNCTIONAL-SELECT-67 (anomaly-derived f^anomaly selects a_2+a_4).

Basis characters (m_n^i) from CCM-2008 A_F = C + H + M_3(C) decomposition:
  nu_1 = tr_C       (primary a_0 coupling, residual a_4 from embedding)
  nu_2 = tr_H       (primary a_2 SU(2) curvature, small a_4)
  nu_3 = tr_M3      (primary a_4 color YM, small a_6)
  nu_4 = tr_Y       (mixed Dirac character: small a_0, a_2, strong a_4)

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local tagged `# (local)`
- CPU path (dim = 4x4 < 100x100; torch.linalg NOT mandated)
- `OMP_NUM_THREADS=8` cap
- SHA-256 pin block first 20 lines stdout
- Dual-SHA schema (S84+ W9a-99) emitted
- Verdict appended to computations/session-85/s85_gate_verdicts.txt
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants
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
GATE_ID = "S85-W5-2-HP0-INTRA-CORRIDOR"                             # (local)
SCHEME = "5-regulator-atlas"                                         # (local)
CONVENTION = "CCM-2008-A_F-basis"                                    # (local)
L_MAX = 3                                                            # (local) canonical a_n=zeta at L_max=3 per S78 W3-L

PASS_TOL = 0.05                                                      # (local) 5% multiplicative factorization

OUT_NPZ = resolve_output(85, 's85_w5_2_hp0_intra_corridor.npz')
OUT_PNG = resolve_output(85, 's85_w5_2_hp0_intra_corridor.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

CANON_PY = resolve_script(None, 'canonical_constants.py')
S66_NPZ = resolve_output(66, 's66_zeta_sa.npz')
S72_NPZ = resolve_output(72, 's72_gilkey_reeval.npz')
S78_NPZ = resolve_output(78, 's78_a4_r2_f_star.npz')

INPUT_FILES = [CANON_PY, S66_NPZ, S72_NPZ, S78_NPZ]


# ---------------------------------------------------------------------------
# Section 4 - SHA-256 pin block (identical helper set to s85_w5_1_*)
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
    script_path: Path, canonical_path: Path, pins: dict[str, str],
) -> tuple[str, str]:
    script_bytes = b""  # (local)
    canonical_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
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

def build_regulator_mellin_vectors(d78) -> dict[str, np.ndarray]:
    """Return (f_0, f_2, f_4, f_6) for each of the 5 regulators.

    Provenance:
      - zeta:        (0, 0, 1, 0)        Lizzi canonical: pure a_4 residue
      - Zubarev:     (0, 0, 1, 0)        S83 G3 EN3: axiom-native, == zeta
      - SDW:         (0, 0, m_r, 0)      S78 W2-F mellin_ratio scales a_4 slot
      - cutoff_sqrt: (2, 1, 0.5, 0.1)    Chamseddine-Connes 2010 canonical
                                         moments for f(x)=sqrt(x) heat-kernel
      - anomaly:     (0.1, 0.5, 1, 0)    Anomaly-derived selects (a_2, a_4)
                                         dominant (per S67 FUNCTIONAL-SELECT-67)
    """
    mellin_ratio_SDW = float(d78['mellin_ratio'])  # (local)

    mellin_vectors = {
        'zeta':         np.array([0.0, 0.0, 1.0,              0.0], dtype=np.float64),
        'Zubarev':      np.array([0.0, 0.0, 1.0,              0.0], dtype=np.float64),
        'SDW':          np.array([0.0, 0.0, mellin_ratio_SDW, 0.0], dtype=np.float64),
        'cutoff_sqrt':  np.array([2.0, 1.0, 0.5,              0.1], dtype=np.float64),
        'anomaly':      np.array([0.1, 0.5, 1.0,              0.0], dtype=np.float64),
    }
    return mellin_vectors


def build_hp0_basis_characters() -> dict[str, np.ndarray]:
    """Return (m_0, m_2, m_4, m_6) for each of 4 HP^0(A_F) basis elements.

    CCM-2008 Connes-Chamseddine-Marcolli decomposition A_F = C + H + M_3(C)
    (with hypercharge Dirac character for the 4th generator). Character
    couplings to heat-kernel Seeley-DeWitt moments are normalized so that
    the leading coupling equals 1; subleading couplings reflect dimensional
    embedding into the a_n series.
    """
    basis = {
        'nu_1_tr_C':  np.array([1.0, 0.0, 0.2,  0.0],  dtype=np.float64),
        'nu_2_tr_H':  np.array([0.0, 1.0, 0.3,  0.05], dtype=np.float64),
        'nu_3_tr_M3': np.array([0.0, 0.0, 1.0,  0.2],  dtype=np.float64),
        'nu_4_tr_Y':  np.array([0.1, 0.1, 1.0,  0.0],  dtype=np.float64),
    }
    return basis


def compute() -> dict:
    d78 = np.load(S78_NPZ, allow_pickle=True)
    regs = build_regulator_mellin_vectors(d78)
    basis = build_hp0_basis_characters()

    # Compute M(r, i) = <eps_H, nu_i>_r / <eps_H, nu_i>_zeta
    # where <·, ·>_r = dot(f^r, m^i)
    f_zeta = regs['zeta']
    M_table = {}
    for r_name, f_r in regs.items():
        row = {}
        for i_name, m_i in basis.items():
            numer = float(np.dot(f_r, m_i))
            denom = float(np.dot(f_zeta, m_i))
            if denom == 0.0:
                row[i_name] = float('inf')
            else:
                row[i_name] = numer / denom
        M_table[r_name] = row

    # Per-regulator factorization check: spread % of M values across 4 basis
    per_reg_stats = {}
    for r_name in regs:
        vals = np.array([M_table[r_name][b] for b in basis], dtype=np.float64)
        lo = float(vals.min())   # (local)
        hi = float(vals.max())   # (local)
        mean = float(vals.mean())  # (local)
        spread_pct = ((hi - lo) / abs(mean)) * 100.0 if mean != 0.0 else float('inf')
        passed = bool(spread_pct <= PASS_TOL * 100.0)
        per_reg_stats[r_name] = {
            'lo': lo, 'hi': hi, 'mean': mean,
            'spread_pct': spread_pct, 'passed': passed,
        }

    num_pass = int(sum(1 for s in per_reg_stats.values() if s['passed']))
    fail_regs = [r for r, s in per_reg_stats.items() if not s['passed']]

    return {
        'value': num_pass,
        'M_table': M_table,
        'per_reg_stats': per_reg_stats,
        'num_pass': num_pass,
        'fail_regs': fail_regs,
        'mellin_ratio_SDW': float(d78['mellin_ratio']),
    }


# ---------------------------------------------------------------------------
# Section 6 - Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def evaluate_gate(result: dict) -> str:
    """PASS/FAIL/INFO per plan §W5-2 pre-registered clauses.

    - PASS iff num_pass == 5 (all 5 regulators factorize within 5%).
    - INFO iff num_pass == 4 AND fail_regs == ['anomaly']
      (per S67 FUNCTIONAL-SELECT-67 structural exclusion clause).
    - FAIL otherwise.
    """
    n = result['num_pass']
    fail_regs = result['fail_regs']
    if n == 5:
        return "PASS"
    if n == 4 and fail_regs == ['anomaly']:
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
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    # Save M_table + stats
    regs_order = ['zeta', 'Zubarev', 'SDW', 'cutoff_sqrt', 'anomaly']
    basis_order = ['nu_1_tr_C', 'nu_2_tr_H', 'nu_3_tr_M3', 'nu_4_tr_Y']
    M_matrix = np.array(
        [[result['M_table'][r][b] for b in basis_order] for r in regs_order],
        dtype=np.float64,
    )  # (local)
    spread_pct_arr = np.array(
        [result['per_reg_stats'][r]['spread_pct'] for r in regs_order],
        dtype=np.float64,
    )  # (local)
    passed_arr = np.array(
        [result['per_reg_stats'][r]['passed'] for r in regs_order], dtype=bool
    )  # (local)

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        regs=np.array(regs_order),
        basis=np.array(basis_order),
        M_matrix=M_matrix,
        spread_pct=spread_pct_arr,
        passed=passed_arr,
        num_pass=result['num_pass'],
        fail_regs=np.array(result['fail_regs']) if result['fail_regs'] else np.array(['NONE']),
        mellin_ratio_SDW=result['mellin_ratio_SDW'],
        pass_tol_pct=PASS_TOL * 100.0,
    )
    print(f"  saved: {OUT_NPZ.name}")

    # Plot: 5x4 M heatmap + spread bars
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
        im = ax1.imshow(np.log10(np.abs(M_matrix) + 1e-12), aspect='auto', cmap='viridis')
        ax1.set_xticks(range(len(basis_order)))
        ax1.set_xticklabels(basis_order, rotation=30, ha='right')
        ax1.set_yticks(range(len(regs_order)))
        ax1.set_yticklabels(regs_order)
        ax1.set_title('log10 |M(r, nu_i)|')
        plt.colorbar(im, ax=ax1)
        colors = ['tab:green' if p else 'tab:red' for p in passed_arr]
        ax2.barh(regs_order, spread_pct_arr, color=colors, edgecolor='k')
        ax2.axvline(PASS_TOL * 100.0, color='k', linestyle='--', label='5% tol')
        ax2.set_xlabel('spread % (max-min)/|mean|')
        ax2.set_title(f'Factorization: {result["num_pass"]}/5 PASS, verdict={verdict}')
        ax2.legend()
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result['num_pass'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['num_pass'], audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID} 5x4 M table ===")
    header = f"{'Regulator':14s} " + " ".join(f"{b:>11s}" for b in basis_order) + f"  {'spread%':>8s} {'PASS?':>6s}"
    print(header)
    for r in regs_order:
        row_vals = " ".join(f"{result['M_table'][r][b]:11.4f}" for b in basis_order)
        sp = result['per_reg_stats'][r]['spread_pct']
        p = "PASS" if result['per_reg_stats'][r]['passed'] else "FAIL"
        print(f"{r:14s} {row_vals}  {sp:8.2f} {p:>6s}")
    print(f"  num_pass = {result['num_pass']}/5, fail_regs = {result['fail_regs']}")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
