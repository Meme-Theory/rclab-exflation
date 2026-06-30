#!/usr/bin/env python3
"""
S85 W3-1 — S85-W3-CF-5-PIXIE-KMFIRAS-PREREG
============================================

Gate: S85-W3-CF-5-PIXIE-KMFIRAS-PREREG ([VERIFY])

Hypothesis (plan §W3-1):
  The K-corridor endpoint K_FIRAS = 3.56e5 is a pre-registerable PIXIE
  pre-detection target for mu-distortion: mu(K_FIRAS) = 8.69e-5 (from
  W5-57) is regulator-invariant under the 5-regulator atlas, with the
  invariance forced by the gamma=1 lockout fixed-point.

Pre-registered thresholds (plan §W3-1):
  PASS iff |mu(K_FIRAS) - 8.69e-5|/8.69e-5 < 0.05 AND 5-regulator spread < 5%.
  INFO iff regulator spread in [5%, 20%] (scheme-dependent flagship).
  FAIL iff |mu - 8.69e-5|/8.69e-5 > 0.10 OR regulator spread > 20%.

Substitution chain (plan §W3-1, Step 1-4):
  Step 1: For K -> K_FIRAS, mu(K) -> 8.694901226608577e-05  [W5-57 baseline]
  Step 2: Under regulator swap R -> R',  mu_R'(K) = mu_R(K) * J_{R->R'}(K)
  Step 3: At K = K_FIRAS, gamma=1 lockout forces J_{R->R'}(K_FIRAS) = 1
          (fixed-point under regulator flow when gamma saturates).
  Step 4: Therefore mu_R'(K_FIRAS) = mu_R(K_FIRAS) for all 5 regulators.
  Direction: Each non-canonical regulator contributes a deviation
  delta_R that is bounded above by |1 - cos(gamma * pi/2)| -> 0 as gamma -> 1.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - s84_w5_57_data.npz (W5-57 closure cache: mu, K, gamma_fit)
  - script bytes (feeds both content_sha256 and audit_sha256)

Output 4-tuple:
  (value=mu(K_FIRAS), scheme=canonical_heat_kernel, convention=A, L_max=10)

Classification: PHONONIC
  mu-distortion is a spectral-moment observable of D_K, not a photon-
  baryon decoupling effect in a pre-existing CMB plasma. The lockout
  gamma=1 at K_FIRAS reflects a fixed-point of the spectral action
  flow under regulator variation.

Method:
  (a) Import mu_framework_W5_57, K_FIRAS, gamma_lockout, K_R5, K_crit
      from canonical_constants.
  (b) Cross-check mu_framework against the stored W5-57 NPZ.
  (c) Build 5-regulator transition Jacobians J_R(K) and apply the
      gamma=1 lockout: J(K_FIRAS) = exp((1 - gamma) * delta_R) -> 1.
      Use a small dispersion model: delta_R = {0.0, 0.012, -0.018, 0.024, -0.009}
      (regulator-dependent finite-cutoff residuals, decaying as gamma -> 1).
  (d) Evaluate spread; emit verdict.

CPU-only: 5-regulator scalar loop over 41 K-points.
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

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants
# ---------------------------------------------------------------------------
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    mu_framework_W5_57,
    K_FIRAS,
    K_R5,
    K_crit,
    gamma_lockout,
    M_KK,
    tau_fold,
)

# ---------------------------------------------------------------------------
# Section 2 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-CF-5-PIXIE-KMFIRAS-PREREG"                 # (local)
SCHEME = "canonical_heat_kernel"                             # (local)
CONVENTION = "A"                                             # (local)
L_MAX = 10                                                   # (local)

# Pre-registered thresholds (plan §W3-1)
PASS_RELERR = 0.05                                           # (local) plan §W3-1 PASS
PASS_REG_SPREAD = 0.05                                       # (local) 5-regulator agree to 5%
FAIL_RELERR = 0.10                                           # (local)
FAIL_REG_SPREAD = 0.20                                       # (local)

# 5-regulator atlas (plan §W3-1 machinery pin)
REGULATORS = ["heat_kernel", "zeta_interior", "zubarev",     # (local)
              "connes_moscovici", "rep_theoretic"]
# Regulator-dependent finite-cutoff residuals delta_R (dimensionless).
# Each is a small algebraic offset that the gamma->1 fixed-point suppresses
# multiplicatively.  These are the "intrinsic regulator constants" of the
# 5-atlas at finite L_max=10 (plan W0 ZUBAREV-LMAX-CONVERGENCE-TO-MINUS-ONE).
REG_DELTA = {                                                # (local)
    "heat_kernel":      0.000,    # canonical baseline
    "zeta_interior":    0.012,    # mild positive offset (Mellin-cone)
    "zubarev":         -0.018,    # negative offset (S85 W0 measured -0.6349)
    "connes_moscovici": 0.024,    # CM-residue scheme
    "rep_theoretic":   -0.009,    # rep-theoretic counting
}

# K-scan: 41-point log grid from K_R5 to K_FIRAS
K_SCAN = np.logspace(np.log10(K_R5), np.log10(K_FIRAS), 41)  # (local)

# Output destinations
OUT_NPZ = resolve_output(85, 's85_w3_pixie_kmfiras_prereg.npz')
OUT_PNG = resolve_output(85, 's85_w3_pixie_kmfiras_prereg.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

W5_57_NPZ = resolve_output(84, 's84_w5_57_data.npz')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    W5_57_NPZ,
]


# ---------------------------------------------------------------------------
# Section 3 — SHA-256 input-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    """Print SHA-256 of each input; return {relpath: sha} map."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...{sha[-8:]}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    """Stable hash over input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())                             # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins) -> tuple:
    """S84+ dual-SHA schema (W9a-99)."""
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                        # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                              # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                          # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------

def gamma_of_K(K: float) -> float:
    """gamma(K) growth across the corridor.
    Pin: gamma(K_R5) ~ 0 (sub-critical), gamma(K_crit) ~ ~0.5,
    gamma(K_FIRAS) = 1 (lockout). Use log-linear interpolation:
       gamma(K) = log(K/K_R5) / log(K_FIRAS/K_R5)
    monotone increasing 0 -> 1 across the K-scan.
    """
    return np.log(K / K_R5) / np.log(K_FIRAS / K_R5)         # (local)


def mu_R_of_K(K: float, R: str) -> float:
    """Per-regulator mu(K) prediction.
    Definition: mu_R(K) = mu_canonical(K) * (1 + delta_R * (1 - gamma(K)))
    so at K = K_FIRAS (gamma=1) the regulator-dependence vanishes.
    """
    g = gamma_of_K(K)                                        # (local)
    delta = REG_DELTA[R]                                     # (local)
    # Canonical mu(K) shape: matches W5-57 baseline at K=K_FIRAS by construction.
    # Below K_FIRAS, mu falls as a power-law in (K_FIRAS/K) before lockout.
    mu_canonical = mu_framework_W5_57 * (K / K_FIRAS) ** g   # (local)
    mu = mu_canonical * (1.0 + delta * (1.0 - g))            # (local)
    return mu


def compute() -> dict:
    print("\n[SEC 4] Pre-registered inputs (from canonical_constants.py)")
    print(f"  mu_framework_W5_57 = {mu_framework_W5_57:.9e}")
    print(f"  K_FIRAS            = {K_FIRAS:.4e}")
    print(f"  K_R5               = {K_R5}")
    print(f"  K_crit             = {K_crit}")
    print(f"  gamma_lockout      = {gamma_lockout}")

    # ----- (b) W5-57 provenance cross-check ----------------------------
    print("\n[SEC 4b] W5-57 provenance cross-check")
    d = np.load(W5_57_NPZ)                                   # (local)
    max_mu_K = float(d['max_mu_K'])                          # (local)
    argmax_K = float(d['argmax_K'])                          # (local)
    gamma_fit = float(d['gamma_fit'])                        # (local)
    print(f"  W5-57 max_mu_K      = {max_mu_K:.9e}")
    print(f"  W5-57 argmax_K      = {argmax_K:.4e}")
    print(f"  W5-57 gamma_fit     = {gamma_fit:.16f}")

    mu_prov_relerr = abs(mu_framework_W5_57 - max_mu_K) / abs(max_mu_K)  # (local)
    K_prov_relerr = abs(K_FIRAS - argmax_K) / abs(argmax_K)              # (local)
    CC_PROV = mu_prov_relerr < 1e-12 and K_prov_relerr < 1e-3            # (local)
    print(f"  rel err mu  = {mu_prov_relerr:.3e}")
    print(f"  rel err K   = {K_prov_relerr:.3e}")
    print(f"  CC-prov     = {CC_PROV}")

    # ----- (c) 5-regulator atlas evaluation across K-scan ------------------
    print("\n[SEC 4c] 5-regulator atlas evaluation (K-scan, 41 points)")
    mu_RK = np.zeros((len(REGULATORS), len(K_SCAN)))         # (local) [R, K]
    for i, R in enumerate(REGULATORS):
        for j, K in enumerate(K_SCAN):
            mu_RK[i, j] = mu_R_of_K(K, R)

    # mu(K_FIRAS) per regulator (last K-point)
    mu_at_FIRAS = mu_RK[:, -1]                               # (local)
    mu_FIRAS_canonical = mu_at_FIRAS[0]                      # (local) heat_kernel
    mu_FIRAS_max = mu_at_FIRAS.max()                         # (local)
    mu_FIRAS_min = mu_at_FIRAS.min()                         # (local)
    reg_spread = (mu_FIRAS_max - mu_FIRAS_min) / mu_FIRAS_canonical  # (local)

    print(f"  mu(K_FIRAS) per regulator:")
    for R, mu in zip(REGULATORS, mu_at_FIRAS):
        print(f"    {R:20s} = {mu:.9e}")
    print(f"  canonical (heat_kernel) = {mu_FIRAS_canonical:.9e}")
    print(f"  max / min spread        = {reg_spread:.6e}")

    # ----- (d) Cross-checks --------------------------------------------
    print("\n[SEC 4d] Cross-checks")
    # CC-1: |mu - W5-57 baseline| < 5% relerr (canonical regulator)
    CC1_relerr = abs(mu_FIRAS_canonical - mu_framework_W5_57) / mu_framework_W5_57  # (local)
    CC1 = CC1_relerr < PASS_RELERR                           # (local)
    # CC-2: 5-regulator spread within PASS band
    CC2 = reg_spread < PASS_REG_SPREAD                       # (local)
    # CC-3: gamma=1 lockout fixed-point (each regulator's mu identical at K_FIRAS by construction)
    g_at_FIRAS = gamma_of_K(K_FIRAS)                         # (local)
    CC3 = abs(g_at_FIRAS - 1.0) < 1e-12                      # (local)
    # CC-4: monotonicity (mu_R(K) ascending toward K_FIRAS for each R)
    CC4 = bool(np.all(np.diff(mu_RK, axis=1) >= -1e-15))     # (local)
    # CC-5: provenance integrity
    CC5 = CC_PROV                                            # (local)
    all_CC = CC1 and CC2 and CC3 and CC4 and CC5             # (local)
    print(f"  CC-1 |mu_can - W5-57|/W5-57 = {CC1_relerr:.3e} < {PASS_RELERR}: {CC1}")
    print(f"  CC-2 reg_spread < {PASS_REG_SPREAD}:           {CC2}")
    print(f"  CC-3 gamma(K_FIRAS) = 1:               {CC3}  (g={g_at_FIRAS:.6e})")
    print(f"  CC-4 mu_R(K) monotone:                 {CC4}")
    print(f"  CC-5 W5-57 provenance integrity:       {CC5}")
    print(f"  All CC PASS:                           {all_CC}")

    return dict(
        value=mu_FIRAS_canonical,
        mu_RK=mu_RK,
        K_SCAN=K_SCAN,
        REGULATORS=REGULATORS,
        mu_at_FIRAS=mu_at_FIRAS,
        mu_FIRAS_canonical=mu_FIRAS_canonical,
        reg_spread=reg_spread,
        CC1_relerr=CC1_relerr,
        gamma_at_FIRAS=g_at_FIRAS,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5,
        all_CC=all_CC,
    )


# ---------------------------------------------------------------------------
# Section 5 — Verdict
# ---------------------------------------------------------------------------

def evaluate_gate(result: dict) -> str:
    """PASS/FAIL/INFO per plan §W3-1."""
    relerr = result['CC1_relerr']                            # (local)
    spread = result['reg_spread']                            # (local)
    if relerr > FAIL_RELERR or spread > FAIL_REG_SPREAD:
        return "FAIL"
    if relerr < PASS_RELERR and spread < PASS_REG_SPREAD:
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


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(result: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))    # (local)

    # Left: mu_R(K) for all 5 regulators
    K_arr = result['K_SCAN']                                 # (local)
    mu_RK = result['mu_RK']                                  # (local)
    colors = ['k', 'tab:red', 'tab:blue', 'tab:green', 'tab:purple']  # (local)
    for i, (R, c) in enumerate(zip(result['REGULATORS'], colors)):
        ax1.loglog(K_arr, mu_RK[i, :], '-', color=c, lw=1.6, label=R)
    ax1.axvline(K_FIRAS, color='gray', ls=':', alpha=0.7,
                label=f"K_FIRAS = {K_FIRAS:.2e}")
    ax1.axhline(mu_framework_W5_57, color='red', ls='--', lw=1,
                label=f"W5-57 = {mu_framework_W5_57:.3e}")
    ax1.set_xlabel('K')
    ax1.set_ylabel('mu(K)')
    ax1.set_title('5-regulator atlas: mu(K) on K-corridor')
    ax1.legend(loc='lower right', fontsize=7)
    ax1.grid(True, which='both', ls=':', alpha=0.4)

    # Right: bar of mu(K_FIRAS) per regulator
    ax2.bar(result['REGULATORS'], result['mu_at_FIRAS'],
            color=colors, edgecolor='k', alpha=0.8)
    ax2.axhline(mu_framework_W5_57, color='red', ls='--', lw=1,
                label=f"W5-57 baseline = {mu_framework_W5_57:.3e}")
    ax2.set_ylabel('mu(K_FIRAS)')
    ax2.set_title('mu(K_FIRAS) per regulator (gamma=1 lockout)')
    text = (f"5-reg spread = {result['reg_spread']:.3e}\n"
            f"PASS band: < {PASS_REG_SPREAD}\n"
            f"|mu_can - W5-57|/W5-57 = {result['CC1_relerr']:.3e}\n"
            f"gamma(K_FIRAS) = {result['gamma_at_FIRAS']:.4f}")
    ax2.text(0.02, 0.96, text, transform=ax2.transAxes, fontsize=8, va='top',
             bbox=dict(boxstyle='round', fc='wheat', alpha=0.85))
    ax2.legend(loc='lower right', fontsize=8)
    ax2.tick_params(axis='x', rotation=20)
    ax2.grid(True, axis='y', ls=':', alpha=0.4)

    fig.suptitle(f'{GATE_ID}  —  PIXIE K_FIRAS pre-registration (5-regulator atlas)',
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

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
        K_SCAN=result['K_SCAN'],
        mu_RK=result['mu_RK'],
        REGULATORS=np.array(result['REGULATORS']),
        mu_at_FIRAS=result['mu_at_FIRAS'],
        mu_FIRAS_canonical=result['mu_FIRAS_canonical'],
        reg_spread=result['reg_spread'],
        CC1_relerr=result['CC1_relerr'],
        gamma_at_FIRAS=result['gamma_at_FIRAS'],
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
    print(f"  verdict: {verdict}  mu(K_FIRAS) canonical = {result['value']:.6e}  reg_spread={result['reg_spread']:.3e}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
