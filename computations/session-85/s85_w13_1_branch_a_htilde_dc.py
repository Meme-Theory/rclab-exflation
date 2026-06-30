#!/usr/bin/env python3
"""
S85 W13-1 — BRANCH-A-HTILDE-DC (Branch-A H_tilde DC tightening)
===============================================================

Gate: S85-W13-1-BRANCH-A-HTILDE-DC ([VERIFY])
  PASS  iff  |Delta_OOM'| <= 0.20  AND  |H_tilde_A' - H_tilde_A_S82|/H_tilde_A_S82 <= 0.05
  FAIL  iff  |Delta_OOM'| > 0.20
  INFO  iff  0.20 < |Delta_OOM'| <= 0.40  AND  |H_tilde_A' - H_tilde_A_S82|/H_tilde_A_S82 > 0.05

Output 4-tuple:
  (value=(H_tilde_A', A_s_A', Delta_OOM'),
   scheme=zeta, convention=TD-framework-a_0-tightened, L_max=10)

Classification: PHONONIC (H_tilde is the fundamental-mode amplitude of the
Mukhanov-Sasaki acoustic cavity at horizon exit; the DC component is the
zero-mode of this cavity).

METHODOLOGY
-----------
Per plan §W13-1 (sessions/session-plan/session-85-plan-w13.md lines 91-214):

1. Load S82 W1-1 Branch-A adjudicated artifact s82_w1_1_h_tilde_td.npz:
     H_tilde_A_S82 = 5.907613e-03 (dimensionless, = field H_tilde_adjudicated_dimless).

2. Compute DC zero-mode via spectral-action a_0 (zeta-scheme):
     rho_fold = (2/pi^2) * a_0_fold * M_KK_gravity^4           [GeV^4]
     H_DC_a0_GeV = sqrt(rho_fold / (3 * M_Pl_reduced^2))        [GeV]
     H_DC_a0_dimless = H_DC_a0_GeV / M_Pl_reduced               [dimensionless]
   This IS H_tilde_B from S82 under the substrate-native Friedmann convention.

3. Apply Path-A framework-forward dS decay (S82 adjudicated branch):
     H_tilde_A_tight(eps) = H_DC_a0_dimless * exp(-eps * N_pivot), N_pivot = 55.

4. Compute A_s via UNIFIED-AS-79 at a_0-tightened H_tilde_A:
     A_s_A'(eps) = (H_tilde_A_tight^2 / (8 pi^2)) * (1/eps)
                   * F_amp_slot * (1/c_sub) * f_conv
     with F_amp_slot = F_amp * k_a2 = 1.0166 * 0.3822,
          c_sub = 2.238, f_conv = 9.30e-4 (S82 pins).

5. Scan eps in [0.010, 0.050] at 41 grid points (plan machinery pin),
   central eps_pivot = 0.020 pinned.

6. Delta_OOM'(eps) = log10(A_s_A'(eps) / A_s_Planck).

7. Primary verdict at eps_pivot = 0.020:
     PASS if |Delta_OOM'| <= 0.20 AND |Delta_H| <= 0.05;
     FAIL if |Delta_OOM'| > 0.20;
     INFO if 0.20 < |Delta_OOM'| <= 0.40 AND |Delta_H| > 0.05.

SUBSTRATE FRAMING
-----------------
H_tilde is the fundamental-mode amplitude of the post-fold GGE's acoustic
B1-band excitation at horizon exit. Its DC component is the zeroth spectral
moment of D_K (a_0 Seeley-DeWitt coefficient) — the spectral weight of the
"ground-state" (non-oscillatory) projection of the fiber's eigenvalue
problem. This gate is the RESONANCE-AMPLITUDE pinning: the cavity's
zero-mode is NOT free; it is structurally locked to a_0. Direction: FROM the
spectral triple's zeroth moment a_0_fold=6440 TOWARD the observed A_s
amplitude in the CMB, via substrate-native Friedmann at the fold epoch and
Path-A dS decay to horizon exit. (IS space, not IN space — H_tilde is a
substrate-spectral datum, not an "amplitude in an expanding universe".)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per CLAUDE.md)
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
from computation_root import resolve_script, resolve_output, resolve_glob, resolve_dynamic, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                     # (local)
GATE_ID = "S85-W13-1-BRANCH-A-HTILDE-DC"                            # (local)
SCHEME = "zeta"                                                     # (local)
CONVENTION = "TD-framework-a_0-tightened"                           # (local)
L_MAX = 10                                                          # (local)

# Pre-registered machinery pins (plan §W13-1 lines 131-143)
N_PIVOT = 55.0                                                      # (local) canonical Planck e-folds (S82 pin)
EPS_H_S82 = 0.02163                                                 # (local) S82 canonical one-loop eps_H
EPS_PIVOT_CENTRAL = 0.020                                           # (local) plan pin
EPS_SCAN_LO = 0.010                                                 # (local) plan pin
EPS_SCAN_HI = 0.050                                                 # (local) plan pin
EPS_SCAN_N = 41                                                     # (local) plan pin

# UNIFIED-AS-79 pinned factors (from S82 W1-1-TD canonical)
F_AMP = 1.0166                                                      # (local) S80 W1-B-REMED PASS
K_A2 = 0.3822                                                       # (local) W0-5 slot factor
F_AMP_SLOT = F_AMP * K_A2                                           # (local) slot-adjusted F_amp
C_SUB = 2.238                                                       # (local) S78 W2-E central
F_CONV = 9.30e-4                                                    # (local) = (M_KK/M_Pl_red)^2

# Pre-registered thresholds (plan §W13-1 lines 156-167)
PASS_OOM_BOUND = 0.20                                               # (local) RATIO
PASS_H_TIGHT_TOL = 0.05                                             # (local) 5% tightening drift
INFO_OOM_UPPER = 0.40                                               # (local) INFO band upper

# S82 reference for comparison (from s82_w1_1_h_tilde_td.npz)
H_TILDE_S82_EXPECTED = 5.907613e-03                                 # (local) Branch-A adjudicated

# Input/output paths
INPUT_FILES = [                                                     # (local)
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(82, 's82_w1_1_h_tilde_td.npz'),
]

VERDICT_TXT = resolve_output(SESSION[1:], f's{SESSION[1:]}_gate_verdicts.txt')
OUT_NPZ = resolve_output(85, 's85_w13_1_branch_a_htilde_dc.npz')
OUT_PNG = resolve_output(85, 's85_w13_1_branch_a_htilde_dc.png')
OUT_JSON = resolve_output(85, 's85_w13_1_branch_a_htilde_dc.json')


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin logging + dual-SHA
# ---------------------------------------------------------------------------
def sha256_of(path):
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    """Dual-SHA per S84+ schema: audit = script+canonical+pinmap, content = script only."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""      # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")                      # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                     # (local)
    content = hashlib.sha256(script_bytes).hexdigest()              # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Physics: a_0-tightened H_DC and UNIFIED-AS-79
# ---------------------------------------------------------------------------
def rho_substrate_zeta(a0_val, M_KK_val):
    """rho_substrate(tau) = (2 / pi^2) * a_0(tau) * M_KK^4  [GeV^4]"""
    return (2.0 / np.pi**2) * a0_val * M_KK_val**4                  # (local) GeV^4


def H_friedmann(rho_val, M_Pl_val):
    """H = sqrt(rho / (3 * M_Pl^2))  [returns GeV]"""
    return np.sqrt(rho_val / (3.0 * M_Pl_val**2))                   # (local) GeV


def unified_as_79(H_tilde_dimless, eps_val, F_amp_val, c_sub_val, f_conv_val):
    """A_s = (H_tilde^2 / 8 pi^2) * (1/eps) * F_amp * (1/c_sub) * f_conv.

    H_tilde input is DIMENSIONLESS (units of M_Pl_reduced).
    """
    term_1 = H_tilde_dimless**2 / (8.0 * np.pi**2)                  # (local)
    term_2 = 1.0 / eps_val                                          # (local)
    term_3 = F_amp_val                                              # (local)
    term_4 = 1.0 / c_sub_val                                        # (local)
    term_5 = f_conv_val                                             # (local)
    return term_1 * term_2 * term_3 * term_4 * term_5               # (local) dimensionless A_s


def verdict_label(delta_oom, delta_h_rel):
    """Pre-registered threshold rule (plan §W13-1 lines 156-167)."""
    a = abs(delta_oom)                                              # (local)
    h = abs(delta_h_rel)                                            # (local)
    if a <= PASS_OOM_BOUND and h <= PASS_H_TIGHT_TOL:
        return "PASS"
    if a <= INFO_OOM_UPPER and h > PASS_H_TIGHT_TOL:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)

    # -----------------------------------------------------------------------
    # 6A. Input pinning (dual-SHA, S84+ schema)
    # -----------------------------------------------------------------------
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')           # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()
    print(f"S85 W13-1: BRANCH-A-HTILDE-DC (a_0 tightening of sole-surviving A_s pathway)")
    print(f"  Gate: {GATE_ID}")
    print(f"  Classification: PHONONIC")
    print()

    # -----------------------------------------------------------------------
    # 6B. Load S82 Branch-A adjudicated reference
    # -----------------------------------------------------------------------
    s82_npz_path = resolve_output(82, 's82_w1_1_h_tilde_td.npz')            # (local)
    if s82_npz_path.exists():
        s82 = np.load(s82_npz_path, allow_pickle=True)
        H_tilde_S82 = float(s82["H_tilde_adjudicated_dimless"])     # (local)
        A_s_S82_branch_a = float(s82["A_s_A_fw"])                   # (local) Path-A framework-forward
        delta_OOM_S82 = float(s82["delta_OOM_A_fw"])                # (local)
    else:
        print(f"WARN: S82 artifact missing — using plan-pinned fallback values")
        H_tilde_S82 = H_TILDE_S82_EXPECTED                          # (local)
        A_s_S82_branch_a = 3.299e-9                                 # (local) plan line 183
        delta_OOM_S82 = 0.1962                                      # (local) plan line 184

    print("=" * 78)
    print("STEP 1 — S82 Branch-A reference (s82_w1_1_h_tilde_td.npz)")
    print("=" * 78)
    print(f"  H_tilde_A_S82 (adjudicated, dimless)  = {H_tilde_S82:.6e}")
    print(f"  A_s_A_fw  (S82 Path-A framework-fw)   = {A_s_S82_branch_a:.4e}")
    print(f"  Delta_OOM_S82                         = {delta_OOM_S82:+.4f}")
    print(f"  Match to plan line 183-184 claim      = "
          f"{'YES' if abs(H_tilde_S82 - H_TILDE_S82_EXPECTED)/H_TILDE_S82_EXPECTED < 1e-4 else 'DRIFTED'}")
    print()

    # -----------------------------------------------------------------------
    # 6C. a_0-tightened DC zero-mode (substrate-native Friedmann, zeta)
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 2 — a_0-tightened DC zero-mode (substrate-native Friedmann, zeta)")
    print("=" * 78)

    # SUBSTITUTION CHAIN — direction of a_0 → H_DC
    # Definition: rho_fold = (2/pi^2) * a_0 * M_KK^4
    #             H_DC = sqrt(rho_fold / (3 * M_Pl^2))
    # Substitute: a_0_fold = 6440, M_KK_gravity, M_Pl_reduced
    # Simplify in Python below (no narrative shortcut).

    rho_fold = rho_substrate_zeta(a0_fold, M_KK_gravity)            # (local) GeV^4
    H_DC_a0_GeV = H_friedmann(rho_fold, M_Pl_reduced)               # (local) GeV
    H_DC_a0_dimless = H_DC_a0_GeV / M_Pl_reduced                    # (local)

    print(f"  a_0_fold                              = {a0_fold:.4f}")
    print(f"  M_KK_gravity                          = {M_KK_gravity:.6e} GeV")
    print(f"  M_Pl_reduced                          = {M_Pl_reduced:.6e} GeV")
    print(f"  rho_fold (zeta)                       = {rho_fold:.4e} GeV^4")
    print(f"  H_DC_a0 (GeV)                         = {H_DC_a0_GeV:.4e} GeV")
    print(f"  H_DC_a0 (dimless, = H_tilde_B_S82)    = {H_DC_a0_dimless:.6e}")
    print()

    # -----------------------------------------------------------------------
    # 6D. Apply Path-A framework-forward dS decay + UNIFIED-AS-79 scan
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 3 — Scan eps in [0.010, 0.050] (41 pts); central eps_pivot = 0.020")
    print("=" * 78)

    eps_grid = np.linspace(EPS_SCAN_LO, EPS_SCAN_HI, EPS_SCAN_N)    # (local)

    # SUBSTITUTION CHAIN — direction of eps on H_tilde_A and A_s
    # Definition: H_tilde_A_tight(eps) = H_DC_a0 * exp(-eps * N_pivot)
    # Substitute: N_pivot = 55 > 0, eps > 0 on scan
    # Simplify: factor exp(-eps*55) is monotone DECREASING in eps
    # Direction: H_tilde_A_tight DECREASES as eps grows
    #
    # Definition: A_s = (H_tilde^2 / 8pi^2) * (1/eps) * F_amp_slot * (1/c_sub) * f_conv
    # Substitute: H_tilde = H_DC_a0 * exp(-eps*N)
    # Simplify: A_s ∝ exp(-2 eps N) / eps
    #           dln(A_s)/dln(eps) = -2*N*eps - 1  (since dln(A_s)/deps = -2N - 1/eps)
    # Direction at eps=0.020, N=55: -2*55*0.020 - 1 = -3.20 ⇒ A_s rapidly decreases in eps

    H_tilde_A_tight = H_DC_a0_dimless * np.exp(-eps_grid * N_PIVOT)  # (local)
    A_s_A_tight = np.array([
        unified_as_79(H, eps, F_AMP_SLOT, C_SUB, F_CONV)
        for H, eps in zip(H_tilde_A_tight, eps_grid)
    ])                                                              # (local)
    Delta_OOM_tight = np.log10(A_s_A_tight / A_s_Planck)            # (local)

    # Central-pin evaluation (eps = 0.020)
    idx_central = int(np.argmin(np.abs(eps_grid - EPS_PIVOT_CENTRAL)))  # (local)
    H_tilde_A_prime = H_tilde_A_tight[idx_central]                  # (local)
    A_s_A_prime = A_s_A_tight[idx_central]                          # (local)
    Delta_OOM_prime = Delta_OOM_tight[idx_central]                  # (local)

    # S82-aligned cross-check at eps_H = 0.02163 (diagnostic)
    idx_s82_eps = int(np.argmin(np.abs(eps_grid - EPS_H_S82)))      # (local)
    H_tilde_A_s82_eps = H_tilde_A_tight[idx_s82_eps]                # (local)
    A_s_A_s82_eps = A_s_A_tight[idx_s82_eps]                        # (local)
    Delta_OOM_s82_eps = Delta_OOM_tight[idx_s82_eps]                # (local)

    # Tightening drift at central pin
    delta_H_rel_central = (H_tilde_A_prime - H_tilde_S82) / H_tilde_S82  # (local)

    print(f"  eps_grid: {EPS_SCAN_N} pts in [{EPS_SCAN_LO}, {EPS_SCAN_HI}]")
    print()
    print(f"  AT eps = {eps_grid[idx_central]:.4f} (central W13 pin):")
    print(f"    H_tilde_A'(0.020)           = {H_tilde_A_prime:.6e}")
    print(f"    A_s_A'(0.020)                = {A_s_A_prime:.4e}")
    print(f"    Delta_OOM'(0.020)            = {Delta_OOM_prime:+.4f}")
    print(f"    |Delta_H|/H_S82 (tightening) = {delta_H_rel_central:+.4f}  ({100*delta_H_rel_central:+.2f}%)")
    print()
    print(f"  AT eps = {eps_grid[idx_s82_eps]:.4f} (S82-aligned diagnostic):")
    print(f"    H_tilde_A'(0.02163)          = {H_tilde_A_s82_eps:.6e}")
    print(f"    A_s_A'(0.02163)              = {A_s_A_s82_eps:.4e}")
    print(f"    Delta_OOM'(0.02163)          = {Delta_OOM_s82_eps:+.4f}")
    print(f"    ratio to S82 A_s_A_fw        = {A_s_A_s82_eps/A_s_S82_branch_a:+.4f}")
    print()

    # -----------------------------------------------------------------------
    # 6E. Verdict
    # -----------------------------------------------------------------------
    print("=" * 78)
    print("STEP 4 — Verdict (pre-registered thresholds)")
    print("=" * 78)

    verdict = verdict_label(Delta_OOM_prime, delta_H_rel_central)   # (local)

    print(f"  Pre-registered:")
    print(f"    PASS iff |Delta_OOM'| <= {PASS_OOM_BOUND} AND |Delta_H|/H_S82 <= {PASS_H_TIGHT_TOL}")
    print(f"    FAIL iff |Delta_OOM'| >  {PASS_OOM_BOUND}")
    print(f"    INFO iff {PASS_OOM_BOUND} < |Delta_OOM'| <= {INFO_OOM_UPPER} AND |Delta_H| > {PASS_H_TIGHT_TOL}")
    print()
    print(f"  Computed:")
    print(f"    |Delta_OOM'|                 = {abs(Delta_OOM_prime):.4f}")
    print(f"    |Delta_H|/H_S82              = {abs(delta_H_rel_central):.4f}")
    print(f"    Verdict:                     = {verdict}")
    print()

    # -----------------------------------------------------------------------
    # 6F. Plot (3-panel): eps-scan of H_tilde / A_s / Delta_OOM
    # -----------------------------------------------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 4.8))

    ax1 = axes[0]
    ax1.plot(eps_grid, H_tilde_A_tight, "b-", lw=1.7,
             label=r"$\tilde H_A^{\mathrm{tight}}(\epsilon) = H_{DC}^{a_0}e^{-\epsilon N_\mathrm{pivot}}$")
    ax1.axhline(H_tilde_S82, color="k", ls="--", lw=1.2,
                label=f"S82 adjudicated = {H_tilde_S82:.2e}")
    ax1.axvline(EPS_PIVOT_CENTRAL, color="r", ls=":", lw=1.1, label=f"eps_pivot = {EPS_PIVOT_CENTRAL}")
    ax1.axvline(EPS_H_S82, color="g", ls=":", lw=1.1, label=f"S82 eps_H = {EPS_H_S82}")
    ax1.set_xlabel(r"$\epsilon$")
    ax1.set_ylabel(r"$\tilde H_A^{\prime}$ (dimless)")
    ax1.set_title("H_tilde_A (a_0-tightened)")
    ax1.set_yscale("log")
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=8)

    ax2 = axes[1]
    ax2.plot(eps_grid, A_s_A_tight, "m-", lw=1.7)
    ax2.axhline(A_s_Planck, color="k", ls="--", lw=1.2, label=f"Planck A_s = {A_s_Planck:.2e}")
    ax2.axhline(A_s_Planck * 10**PASS_OOM_BOUND, color="gray", ls=":", lw=1.0,
                label=f"+0.20 OOM bound")
    ax2.axhline(A_s_Planck * 10**(-PASS_OOM_BOUND), color="gray", ls=":", lw=1.0)
    ax2.axvline(EPS_PIVOT_CENTRAL, color="r", ls=":", lw=1.1)
    ax2.axvline(EPS_H_S82, color="g", ls=":", lw=1.1)
    ax2.set_xlabel(r"$\epsilon$")
    ax2.set_ylabel(r"$A_s^\prime$")
    ax2.set_title("A_s (UAS79, a_0-tightened)")
    ax2.set_yscale("log")
    ax2.grid(True, alpha=0.3, which="both")
    ax2.legend(fontsize=8)

    ax3 = axes[2]
    ax3.plot(eps_grid, Delta_OOM_tight, "r-", lw=1.7)
    ax3.axhline( PASS_OOM_BOUND, color="gray", ls="--", lw=1.1, label=f"PASS band |x|<{PASS_OOM_BOUND}")
    ax3.axhline(-PASS_OOM_BOUND, color="gray", ls="--", lw=1.1)
    ax3.axhline( INFO_OOM_UPPER, color="k",    ls=":",  lw=0.9, label=f"INFO band |x|<{INFO_OOM_UPPER}")
    ax3.axhline(-INFO_OOM_UPPER, color="k",    ls=":",  lw=0.9)
    ax3.axvline(EPS_PIVOT_CENTRAL, color="r", ls=":", lw=1.1)
    ax3.axvline(EPS_H_S82, color="g", ls=":", lw=1.1)
    ax3.set_xlabel(r"$\epsilon$")
    ax3.set_ylabel(r"$\Delta_\mathrm{OOM}^\prime = \log_{10}(A_s^\prime / A_s^{\mathrm{Planck}})$")
    ax3.set_title("Delta_OOM' vs eps")
    ax3.grid(True, alpha=0.3, axis="y")
    ax3.legend(fontsize=8)

    fig.suptitle(
        f"S85 W13-1: Branch-A H_tilde DC tightening (a_0 → H_DC); verdict = {verdict}",
        y=1.00, fontsize=11)
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)

    # -----------------------------------------------------------------------
    # 6G. Save npz + json
    # -----------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # Primary verdict tuple
        H_tilde_A_prime=H_tilde_A_prime,
        A_s_A_prime=A_s_A_prime,
        Delta_OOM_prime=Delta_OOM_prime,
        delta_H_rel_central=delta_H_rel_central,
        verdict=verdict,
        # Scan
        eps_grid=eps_grid,
        H_tilde_A_tight=H_tilde_A_tight,
        A_s_A_tight=A_s_A_tight,
        Delta_OOM_tight=Delta_OOM_tight,
        idx_central=idx_central,
        idx_s82_eps=idx_s82_eps,
        # Reference
        H_tilde_S82=H_tilde_S82,
        A_s_S82_branch_a=A_s_S82_branch_a,
        delta_OOM_S82=delta_OOM_S82,
        # a_0-tightened DC
        H_DC_a0_dimless=H_DC_a0_dimless,
        H_DC_a0_GeV=H_DC_a0_GeV,
        rho_fold=rho_fold,
        a0_fold=a0_fold,
        M_KK_gravity=M_KK_gravity,
        M_Pl_reduced=M_Pl_reduced,
        A_s_Planck=A_s_Planck,
        # Machinery pins
        N_PIVOT=N_PIVOT,
        EPS_H_S82=EPS_H_S82,
        EPS_PIVOT_CENTRAL=EPS_PIVOT_CENTRAL,
        F_AMP_SLOT=F_AMP_SLOT,
        C_SUB=C_SUB,
        F_CONV=F_CONV,
        PASS_OOM_BOUND=PASS_OOM_BOUND,
        PASS_H_TIGHT_TOL=PASS_H_TIGHT_TOL,
        # Metadata
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    with OUT_JSON.open("w", encoding="utf-8") as fp:
        json.dump({
            "gate_id": GATE_ID,
            "verdict": verdict,
            "value": {
                "H_tilde_A_prime": float(H_tilde_A_prime),
                "A_s_A_prime": float(A_s_A_prime),
                "Delta_OOM_prime": float(Delta_OOM_prime),
            },
            "delta_H_rel_central": float(delta_H_rel_central),
            "scheme": SCHEME,
            "convention": CONVENTION,
            "L_max": L_MAX,
            "audit_sha256": audit_sha,
            "content_sha256": content_sha,
            "pins": pins,
        }, fp, indent=2)

    # -----------------------------------------------------------------------
    # 6H. Verdict line (S84+ dual-SHA format) + companion row
    # -----------------------------------------------------------------------
    value_str = (f"(H_tilde={H_tilde_A_prime:.6e},"
                 f"A_s={A_s_A_prime:.4e},"
                 f"Delta_OOM={Delta_OOM_prime:+.4f})")                # (local)
    verdict_line = (
        f"{GATE_ID}: {verdict} -- value={value_str} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )                                                               # (local)
    companion = (f"# audit_sha256 companion row: {GATE_ID} "
                 f"audit={audit_sha[:16]} content={content_sha[:16]}\n")  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)
        fp.write(companion)

    # -----------------------------------------------------------------------
    # 6I. Diagnostic summary
    # -----------------------------------------------------------------------
    wall = time.time() - t0                                         # (local)
    print("=" * 78)
    print("OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script  : {__file__}")
    print(f"  Data    : {OUT_NPZ}")
    print(f"  Plot    : {OUT_PNG}")
    print(f"  JSON    : {OUT_JSON}")
    print(f"  Verdict : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print(f"  {companion.strip()}")
    print()
    print(f"4-tuple: (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0  # exit 0 regardless of verdict (math-scripts.md §Exit Codes)


if __name__ == "__main__":
    sys.exit(main())
