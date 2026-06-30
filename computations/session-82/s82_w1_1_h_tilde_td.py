#!/usr/bin/env python3
"""
S82 W1-1-TD — H-TILDE-EPOCH-CONSISTENCY (transit-dynamics track)
================================================================

Gate: S82-H-TILDE-EPOCH-TD ([VERIFY], CF-1 inherited from S80)
  PASS-F2  : |delta_OOM(best branch)| < 0.30
  INFO-2-10: delta_OOM in [0.30, 1.00]
  FAIL-GT10: delta_OOM > 1.00 even under best branch

Inputs (SHA-256 pinned at runtime — logged in first 20 lines of stdout):
  - canonical_constants.py (closure hash anchor)

Output 4-tuple:
  (value=<H_tilde_adjudicated>, scheme=<zeta|zeta-inv>,
   convention=<substrate-native|obs-inverse>, L_max=3)

Classification: PHONONIC

METHODOLOGY
-----------
Task: adjudicate H̃ epoch conflation in UNIFIED-AS-79 per P4-D CF-1.
Two candidate epochs:
  Path A: horizon-exit H for k_pivot = 0.05 Mpc^{-1} (inflation-inherited).
  Path B: fold-epoch H at tau_fold = 0.190 (substrate-native).

Substrate-native Friedmann (Chamseddine-Connes zeta-scheme):
  rho_substrate(tau_fold) = (2/pi^2) * a_0_fold * M_KK^4
  H^2 = rho / (3 M_Pl_red^2)

Path A is computed two ways:
  (a) obs-inverse: invert UNIFIED-AS-79 with A_s = A_s_Planck to read
      H̃_A^obs = sqrt(A_s * 8 pi^2 * eps_H). This is the "calibration"
      value UNIFIED-AS-79 needs to land Planck exactly.
  (b) framework: evolve H forward on post-fold dS slow-roll,
      H(N) = H_fold * exp(-eps_H * N), with N_pivot = 55 e-folds.

A_s under each branch comes from SCALING at fixed (eps_H, F_amp, c_sub, f_conv):
  A_s(H̃) = A_s_ref * (H̃ / H̃_ref)^2, with H̃_ref = H̃_A^obs (calibration).

Adjudicated H̃ = branch with smaller |delta_OOM(A_s_branch, A_s_Planck)|.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- GPU path not required (scalar arithmetic + 1D scan)
- SHA-256 of all input files logged in first 20 lines of stdout
- 4-tuple printed as the final non-verdict line
- Gate verdict appended to s82_gate_verdicts.txt with 64-char SHA pin

PHONONIC FRAMING
----------------
H̃ is NOT an inflation-era "container-spacetime" Hubble parameter. It is a
spectral-moment quantity: H̃^2 emerges from a_0 * M_KK^4 (volume moment of
D_K spectrum) via Friedmann identification with a_2 (scalar-curvature
moment). Both epochs — fold and horizon-exit — live on the substrate
timeline; they differ by how far the post-fold spectral relaxation has
progressed. The "horizon" in Path A is the acoustic sound horizon of the
post-transit GGE spectrum, not a GR cosmological horizon.
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per CLAUDE.md)
# -----------------------------------------------------------------------------
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

os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) CPU cap per comp-env rule
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local)

import sys
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (  # noqa: F401
    PI, a0_fold, a2_fold, a4_fold, tau_fold,
    M_KK_gravity, M_KK_kerner, M_Pl_reduced,
    Mpc_to_m, hbar_c_GeV_m, A_s_CMB, H_fold,
)

# -----------------------------------------------------------------------------
# Section 2 — Standard imports
# -----------------------------------------------------------------------------
import hashlib
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths and pre-registration pins
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"                                     # (local)
GATE_ID = "S82-H-TILDE-EPOCH-TD"                    # (local)
SCHEME = "zeta"                                      # (local)
CONVENTION = "substrate-native"                      # (local)
L_MAX = 3                                            # (local)

# Pre-registered thresholds (from S80 plan L788-L799)
PASS_FACTOR_2 = 0.30                                 # (local) |delta_OOM| < 0.30
INFO_BOUND    = 1.00                                 # (local) 0.30 <= delta_OOM < 1.00
# (FAIL => delta_OOM > 1.00)

# Input/output paths
OUT_NPZ = resolve_output(82, 's82_w1_1_h_tilde_td.npz')
OUT_PNG = resolve_output(82, 's82_w1_1_h_tilde_td.png')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
]

# Machinery pins (per PRU discipline, S80 plan machinery-pin block)
k_pivot_Mpc_inv = 0.05                              # (local) Planck 2018 pivot, Mpc^{-1}
EPS_H_CANONICAL = 0.02163                           # (local) S75/S77 one-loop eps
N_pivot_canonical = 55.0                            # (local) canonical Planck e-folds

# Derived UNIFIED-AS-79 factors (to compute A_s^framework at each branch)
F_amp_canonical = 1.0166                            # (local) S80 W1-B-REMED PASS
k_a2            = 0.3822                            # (local) W0-5 slot factor
F_amp_slot      = F_amp_canonical * k_a2            # (local) slot-adjusted F_amp
c_sub           = 2.238                             # (local) S78 W2-E central
f_conv          = 9.30e-4                           # (local) (M_KK/M_Pl_red)^2

# -----------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin logging (first 20 lines of stdout)
# -----------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file; empty string on missing/unreadable."""
    h = hashlib.sha256()                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    """Print SHA-256 of each input; return dict {relpath: sha} for closure."""
    print(f"=== {GATE_ID} — input SHA-256 pins (S81-hardened) ===")
    pins = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    """Stable hash over ordered input SHAs — full 64-char hexdigest."""
    items = sorted(pins.items())                    # (local)
    h = hashlib.sha256()                            # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------------------
# Section 5 — Physics: Friedmann + epoch evaluation
# -----------------------------------------------------------------------------

def rho_substrate_zeta(a0_val, M_KK_val):
    """Substrate energy density from zeta-scheme a_0 moment.

    rho_substrate(tau) = (2 / pi^2) * a_0(tau) * M_KK^4        [GeV^4]
    """
    return (2.0 / PI**2) * a0_val * M_KK_val**4     # (local) GeV^4


def H_friedmann(rho_val, M_Pl_val):
    """Friedmann equation: H^2 = rho / (3 * M_Pl_red^2)        [returns GeV]"""
    H2 = rho_val / (3.0 * M_Pl_val**2)              # (local) GeV^2
    return np.sqrt(H2)                              # (local) GeV


def unified_as_79(H_tilde_dimless, eps_val, F_amp_val, c_sub_val, f_conv_val):
    """UNIFIED-AS-79 A_s formula (P2-A closer, S79).

    A_s = (H_tilde^2 / (8 pi^2)) * (1/eps) * F_amp * (1/c_sub) * f_conv

    H_tilde input is DIMENSIONLESS (units of M_Pl_reduced).
    """
    term_1 = H_tilde_dimless**2 / (8.0 * PI**2)     # (local)
    term_2 = 1.0 / eps_val                          # (local)
    term_3 = F_amp_val                              # (local)
    term_4 = 1.0 / c_sub_val                        # (local)
    term_5 = f_conv_val                             # (local)
    return term_1 * term_2 * term_3 * term_4 * term_5  # (local) dimensionless A_s


def verdict_label(delta_oom):
    """Pre-registered threshold rule (S80 plan L796-798)."""
    a = abs(delta_oom)                              # (local)
    if a < PASS_FACTOR_2:
        return "PASS-F2"
    if a < INFO_BOUND:
        return "INFO-2-10"
    return "FAIL-GT10"


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

def main() -> int:
    t0 = time.time()  # (local)

    # -------------------------------------------------------------------------
    # 4A. Input pinning (S81 hardening)
    # -------------------------------------------------------------------------
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure-64: {closure}")
    print()
    print(f"S82 W1-1-TD: H-TILDE-EPOCH-CONSISTENCY (transit-dynamics track)")
    print(f"  Gate: {GATE_ID}")
    print(f"  CF-1 inherited from S80 (plan L782-L867)")
    print(f"  Classification: PHONONIC")
    print()

    # -------------------------------------------------------------------------
    # 5A. Path B: H̃_B = H(tau_fold), substrate-native Friedmann
    # -------------------------------------------------------------------------
    print("=" * 78)
    print("STEP 1 — Path B: H̃_B from substrate-native Friedmann at tau_fold = 0.19")
    print("=" * 78)

    # Zeta-scheme rho at fold, using gravity-route M_KK (canonical)
    rho_fold_grav = rho_substrate_zeta(a0_fold, M_KK_gravity)     # (local) GeV^4
    H_tilde_B_GeV = H_friedmann(rho_fold_grav, M_Pl_reduced)      # (local) GeV
    H_tilde_B_dimless = H_tilde_B_GeV / M_Pl_reduced              # (local)

    # Kerner-route cross-check
    rho_fold_kern = rho_substrate_zeta(a0_fold, M_KK_kerner)      # (local) GeV^4
    H_tilde_B_kern_GeV = H_friedmann(rho_fold_kern, M_Pl_reduced) # (local) GeV
    H_tilde_B_kern_dimless = H_tilde_B_kern_GeV / M_Pl_reduced    # (local)

    # S38 H_fold (in M_KK units) cross-check
    H_fold_S38_GeV = H_fold * M_KK_gravity                        # (local) GeV
    H_fold_S38_dimless = H_fold_S38_GeV / M_Pl_reduced            # (local)

    print(f"Inputs (zeta-scheme, L_max=3):")
    print(f"  a_0_fold      = {a0_fold:.4f}")
    print(f"  a_2_fold      = {a2_fold:.4f}")
    print(f"  a_4_fold      = {a4_fold:.4f}")
    print(f"  M_KK_gravity  = {M_KK_gravity:.6e} GeV")
    print(f"  M_KK_kerner   = {M_KK_kerner:.6e} GeV")
    print(f"  M_Pl_reduced  = {M_Pl_reduced:.6e} GeV")
    print()
    print(f"rho_fold (zeta, M_KK_grav) = {rho_fold_grav:.4e} GeV^4")
    print(f"H̃_B (grav, Friedmann)     = {H_tilde_B_GeV:.4e} GeV")
    print(f"H̃_B / M_Pl_red             = {H_tilde_B_dimless:.4e}  (dimensionless)")
    print(f"H̃_B (kerner route)         = {H_tilde_B_kern_dimless:.4e} M_Pl_red")
    print(f"  (kerner/grav ratio)      = {H_tilde_B_kern_dimless/H_tilde_B_dimless:.4f}  "
          f"[log = {np.log10(H_tilde_B_kern_dimless/H_tilde_B_dimless):+.3f}, "
          f"expected OOM_diff_MKK=0.83]")
    print()
    print(f"Cross-check: S38 H_fold (M_KK units) = {H_fold:.3f} M_KK = "
          f"{H_fold_S38_GeV:.4e} GeV = {H_fold_S38_dimless:.4e} M_Pl_red")
    print(f"  Ratio H_fold_S38 / H̃_B(this)      = {H_fold_S38_dimless/H_tilde_B_dimless:.4e}")
    print()

    # -------------------------------------------------------------------------
    # 5B. Path A: H̃_A^obs (inverse UNIFIED-AS-79 with A_s = Planck) and
    #             H̃_A^framework (dS decay from fold, N_pivot e-folds)
    # -------------------------------------------------------------------------
    print("=" * 78)
    print("STEP 2 — Path A: H̃_A candidates (obs-inverse AND framework-forward)")
    print("=" * 78)

    # (a) Obs-inverse via Mukhanov-Sasaki bench form
    # A_s = H^2 / (8 pi^2 eps) ⇒ H = sqrt(A_s * 8 pi^2 * eps)
    H_tilde_A_obs_dimless = np.sqrt(A_s_CMB * 8.0 * PI**2 * EPS_H_CANONICAL)  # (local)
    H_tilde_A_obs_GeV = H_tilde_A_obs_dimless * M_Pl_reduced                  # (local) GeV

    # (b) Framework-forward: dS decay from fold by N_pivot e-folds
    H_tilde_A_fw_dimless = H_tilde_B_dimless * np.exp(-EPS_H_CANONICAL * N_pivot_canonical)  # (local)
    H_tilde_A_fw_GeV = H_tilde_A_fw_dimless * M_Pl_reduced                    # (local) GeV

    # SUBSTITUTION CHAIN — verify direction of dS decay
    # Definition: H(N) = H_fold * exp(-eps_H * N), eps_H = 0.02163 > 0, N_pivot = 55 > 0
    # Substitution: H(55) / H(0) = exp(-0.02163 * 55)
    # Simplify (in Python below): exp(-1.18965) ~ 0.304
    # Direction: factor < 1 ⇒ H̃_A^fw < H̃_B (monotone decrease under dS+slow-roll)
    decay_factor = np.exp(-EPS_H_CANONICAL * N_pivot_canonical)              # (local)
    print(f"dS decay factor: exp(-eps_H * N_pivot) = exp(-{EPS_H_CANONICAL:.5f}*{N_pivot_canonical:.1f}) "
          f"= {decay_factor:.6f}")
    # Verify direction: decay_factor should be < 1
    assert decay_factor < 1.0, "dS decay factor must be < 1 under positive eps_H"
    print(f"  (verified: decay_factor < 1 ⇒ H̃_A^fw < H̃_B, as expected from eps_H > 0)")
    print()

    print(f"H̃_A^obs [inverting Planck A_s, eps={EPS_H_CANONICAL}] = "
          f"{H_tilde_A_obs_dimless:.4e} M_Pl_red  ({H_tilde_A_obs_GeV:.4e} GeV)")
    print(f"H̃_A^framework [H̃_B * exp(-eps N_pivot), N=55]      = "
          f"{H_tilde_A_fw_dimless:.4e} M_Pl_red  ({H_tilde_A_fw_GeV:.4e} GeV)")
    print(f"H̃_B (fold-epoch, repeated for contrast)              = "
          f"{H_tilde_B_dimless:.4e} M_Pl_red  ({H_tilde_B_GeV:.4e} GeV)")
    print()

    # -------------------------------------------------------------------------
    # 5C. Ratios r_AB and A_s-gap scaling
    # -------------------------------------------------------------------------
    print("=" * 78)
    print("STEP 3 — r_AB = H̃_A / H̃_B ratios, and UNIFIED-AS-79 A_s per branch")
    print("=" * 78)

    r_AB_obs = H_tilde_A_obs_dimless / H_tilde_B_dimless          # (local)
    r_AB_fw  = H_tilde_A_fw_dimless  / H_tilde_B_dimless          # (local)

    # SUBSTITUTION CHAIN — A_s scaling
    # Definition: A_s(H̃) = (H̃^2 / 8 pi^2) * (1/eps) * F_amp * (1/c_sub) * f_conv
    # All factors (eps, F_amp, c_sub, f_conv) held fixed across branches.
    # Substitution: A_s_A / A_s_B = (H̃_A / H̃_B)^2 = r_AB^2
    # Simplify: A_s_branch = C * H̃_branch^2, where C is the shared prefactor.
    # Direction: A_s_A > A_s_B iff r_AB > 1; A_s_A < A_s_B iff r_AB < 1.

    A_s_A_obs = unified_as_79(H_tilde_A_obs_dimless, EPS_H_CANONICAL,
                              F_amp_slot, c_sub, f_conv)          # (local)
    A_s_A_fw  = unified_as_79(H_tilde_A_fw_dimless,  EPS_H_CANONICAL,
                              F_amp_slot, c_sub, f_conv)          # (local)
    A_s_B     = unified_as_79(H_tilde_B_dimless,     EPS_H_CANONICAL,
                              F_amp_slot, c_sub, f_conv)          # (local)

    delta_OOM_A_obs = np.log10(abs(A_s_A_obs / A_s_CMB))          # (local)
    delta_OOM_A_fw  = np.log10(abs(A_s_A_fw  / A_s_CMB))          # (local)
    delta_OOM_B     = np.log10(abs(A_s_B     / A_s_CMB))          # (local)

    print(f"r_AB (obs-inverse)       = H̃_A^obs / H̃_B = {r_AB_obs:.4e}  "
          f"(log = {np.log10(r_AB_obs):+.4f} OOM)")
    print(f"r_AB (framework, N=55)   = H̃_A^fw  / H̃_B = {r_AB_fw:.4e}  "
          f"(log = {np.log10(r_AB_fw):+.4f} OOM)")
    print()
    print(f"A_s under each branch vs Planck ({A_s_CMB:.2e}):")
    print(f"  Path A (obs-inverse):      A_s = {A_s_A_obs:.4e}  delta_OOM = {delta_OOM_A_obs:+.4f}  "
          f"=> {verdict_label(delta_OOM_A_obs)}")
    print(f"  Path A (framework, N=55):  A_s = {A_s_A_fw:.4e}  delta_OOM = {delta_OOM_A_fw:+.4f}  "
          f"=> {verdict_label(delta_OOM_A_fw)}")
    print(f"  Path B (fold-epoch):       A_s = {A_s_B:.4e}  delta_OOM = {delta_OOM_B:+.4f}  "
          f"=> {verdict_label(delta_OOM_B)}")
    print()

    # -------------------------------------------------------------------------
    # 5D. Adjudication
    # -------------------------------------------------------------------------
    branches = {
        "Path-A-obs-inverse":     (delta_OOM_A_obs, H_tilde_A_obs_dimless, "zeta-inv", "obs-inverse"),
        "Path-A-framework-N55":   (delta_OOM_A_fw,  H_tilde_A_fw_dimless,  "zeta",     "substrate-native"),
        "Path-B-fold-epoch":      (delta_OOM_B,     H_tilde_B_dimless,     "zeta",     "substrate-native"),
    }  # (local)
    best_branch_name = min(branches.keys(), key=lambda k: abs(branches[k][0]))  # (local)
    best_delta_oom = branches[best_branch_name][0]
    best_H_tilde   = branches[best_branch_name][1]
    best_scheme    = branches[best_branch_name][2]
    best_conv      = branches[best_branch_name][3]
    best_verdict   = verdict_label(best_delta_oom)

    print("=" * 78)
    print("STEP 4 — Adjudication: best branch = lowest |delta_OOM|")
    print("=" * 78)
    for name, (d, h, s, c) in branches.items():
        mark = " <-- BEST" if name == best_branch_name else ""
        print(f"  {name:<26s}  delta_OOM = {d:+.4f}  [{verdict_label(d)}]{mark}")
    print()
    print(f"ADJUDICATED H̃: {best_H_tilde:.6e} M_Pl_red  ({best_H_tilde*M_Pl_reduced:.4e} GeV)")
    print(f"  scheme     = {best_scheme}")
    print(f"  convention = {best_conv}")
    print(f"  L_max      = {L_MAX}")
    print(f"  verdict    = {best_verdict}")
    print()

    # -------------------------------------------------------------------------
    # 5E. H(N) trajectory and plot
    # -------------------------------------------------------------------------
    N_axis = np.linspace(0.0, 70.0, 701)                            # (local)
    H_of_N_dimless = H_tilde_B_dimless * np.exp(-EPS_H_CANONICAL * N_axis)  # (local)

    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    ax1 = axes[0]
    ax1.semilogy(N_axis, H_of_N_dimless, 'b-', lw=1.7,
                 label=r'$H(N) = H_B \, \exp(-\varepsilon_H N)$')
    ax1.axhline(H_tilde_B_dimless, color='k', ls='--', lw=1.3,
                label=f'$\\tilde H_B$ (fold) = {H_tilde_B_dimless:.2e}')
    ax1.axhline(H_tilde_A_fw_dimless, color='r', ls='--', lw=1.3,
                label=f'$\\tilde H_A^\\mathrm{{fw}}$ (N=55) = {H_tilde_A_fw_dimless:.2e}')
    ax1.axhline(H_tilde_A_obs_dimless, color='g', ls=':', lw=1.5,
                label=f'$\\tilde H_A^\\mathrm{{obs}}$ = {H_tilde_A_obs_dimless:.2e}')
    ax1.axvline(0.0, color='k', ls=':', lw=0.8, alpha=0.4, label='fold epoch (N=0)')
    ax1.axvline(N_pivot_canonical, color='gray', ls=':', lw=1.2, alpha=0.7,
                label=f'N_pivot = {N_pivot_canonical:.0f}')
    ax1.set_xlabel(r'e-folds $N$ after fold')
    ax1.set_ylabel(r'$\tilde H / M_{\mathrm{Pl,red}}$')
    ax1.set_title('Substrate Friedmann: $\\tilde H$ candidates for W1-1-TD')
    ax1.legend(fontsize=8, loc='lower left')
    ax1.grid(True, alpha=0.3, which='both')

    ax2 = axes[1]
    bn = ['A obs-inv', 'A framework\n(N=55)', 'B fold']
    bd = [delta_OOM_A_obs, delta_OOM_A_fw, delta_OOM_B]
    bc = ['g', 'orange', 'r']
    ax2.bar(range(3), bd, color=bc, alpha=0.72, edgecolor='k')
    ax2.axhline( PASS_FACTOR_2, color='gray', ls='--', alpha=0.6,
                 label=f'PASS-F2 boundary (|$\\Delta$OOM|<{PASS_FACTOR_2})')
    ax2.axhline(-PASS_FACTOR_2, color='gray', ls='--', alpha=0.6)
    ax2.axhline( INFO_BOUND, color='k', ls=':', alpha=0.6,
                 label=f'INFO boundary (|$\\Delta$OOM|<{INFO_BOUND})')
    ax2.axhline(-INFO_BOUND, color='k', ls=':', alpha=0.6)
    ax2.set_xticks(range(3))
    ax2.set_xticklabels(bn)
    ax2.set_ylabel(r'$\Delta_\mathrm{OOM} = \log_{10}(A_s^\mathrm{branch} / A_s^\mathrm{Planck})$')
    ax2.set_title(f'A$_s$ gap under UNIFIED-AS-79 per $\\tilde H$ branch')
    ax2.legend(fontsize=8, loc='best')
    ax2.grid(True, alpha=0.3, axis='y')
    for i, v in enumerate(bd):
        off = 0.35 if v >= 0 else -0.55                              # (local)
        ax2.text(i, v + off, f'{v:+.2f}', ha='center', fontsize=9, fontweight='bold')

    fig.suptitle(f'S82 W1-1-TD: H̃-EPOCH-CONSISTENCY — adjudicated branch: {best_branch_name}',
                 y=1.00, fontsize=11)
    plt.tight_layout()
    fig.savefig(OUT_PNG, dpi=140, bbox_inches='tight')
    plt.close(fig)

    # -------------------------------------------------------------------------
    # 5F. Save npz
    # -------------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # Adjudicated 4-tuple
        H_tilde_adjudicated_dimless = best_H_tilde,
        H_tilde_adjudicated_GeV     = best_H_tilde * M_Pl_reduced,
        best_branch                 = best_branch_name,
        best_scheme                 = best_scheme,
        best_convention             = best_conv,
        best_verdict                = best_verdict,
        best_delta_oom              = best_delta_oom,
        L_max                       = L_MAX,
        # Per-branch
        H_tilde_A_obs_dimless       = H_tilde_A_obs_dimless,
        H_tilde_A_obs_GeV           = H_tilde_A_obs_GeV,
        H_tilde_A_fw_dimless        = H_tilde_A_fw_dimless,
        H_tilde_A_fw_GeV            = H_tilde_A_fw_GeV,
        H_tilde_B_dimless           = H_tilde_B_dimless,
        H_tilde_B_GeV               = H_tilde_B_GeV,
        H_tilde_B_kern_dimless      = H_tilde_B_kern_dimless,
        r_AB_obs                    = r_AB_obs,
        r_AB_fw                     = r_AB_fw,
        # A_s per branch
        A_s_A_obs                   = A_s_A_obs,
        A_s_A_fw                    = A_s_A_fw,
        A_s_B                       = A_s_B,
        A_s_Planck                  = A_s_CMB,
        delta_OOM_A_obs             = delta_OOM_A_obs,
        delta_OOM_A_fw              = delta_OOM_A_fw,
        delta_OOM_B                 = delta_OOM_B,
        # H(N) trajectory
        N_axis                      = N_axis,
        H_of_N_dimless              = H_of_N_dimless,
        # Machinery pins
        tau_fold                    = tau_fold,
        a0_fold                     = a0_fold,
        a2_fold                     = a2_fold,
        a4_fold                     = a4_fold,
        M_KK_gravity                = M_KK_gravity,
        M_KK_kerner                 = M_KK_kerner,
        M_Pl_reduced                = M_Pl_reduced,
        EPS_H_CANONICAL             = EPS_H_CANONICAL,
        N_pivot_canonical           = N_pivot_canonical,
        F_amp_slot                  = F_amp_slot,
        c_sub                       = c_sub,
        f_conv                      = f_conv,
        # Scheme metadata
        scheme                      = SCHEME,
        convention                  = CONVENTION,
        closure_sha256_full         = closure,
    )

    # -------------------------------------------------------------------------
    # 5G. 4-tuple + verdict line (S81-canonical, 64-char SHA)
    # -------------------------------------------------------------------------
    # 4-tuple: the value is the ADJUDICATED H̃ in M_Pl_red units
    four_tuple = (
        f"(value={best_H_tilde:.6e}, scheme={best_scheme}, "
        f"convention={best_conv}, L_max={L_MAX})"
    )
    print(f"\n4-tuple: {four_tuple}")
    print()

    verdict_line = (
        f"{GATE_ID}: {best_verdict} -- "
        f"value={best_H_tilde:.6e} scheme={best_scheme} "
        f"convention={best_conv} L_max={L_MAX} sha256={closure}\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line)

    # -------------------------------------------------------------------------
    # 5H. Diagnostic summary
    # -------------------------------------------------------------------------
    wall = time.time() - t0                                         # (local)
    print("=" * 78)
    print(f"OUTPUTS SAVED")
    print("=" * 78)
    print(f"  Script  : {__file__}")
    print(f"  Data    : {OUT_NPZ}")
    print(f"  Plot    : {OUT_PNG}")
    print(f"  Verdict : appended to {VERDICT_TXT}")
    print()
    print(f"VERDICT LINE (appended):")
    print(f"  {verdict_line.strip()}")
    print()
    print(f"=== {GATE_ID}: {best_verdict} (wall {wall:.2f}s) ===")
    return 0 if "FAIL" not in best_verdict else 1


if __name__ == "__main__":
    sys.exit(main())
