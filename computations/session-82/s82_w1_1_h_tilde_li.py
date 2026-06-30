#!/usr/bin/env python3
"""
S82 W1-1-LI — H-TILDE-EPOCH-CONSISTENCY (Lizzi spectral-functional track).
============================================================================

Dual-owner re-run of S80 §W1-1 for the S82 fragmented-recovery pass.  Where the
S80 lizzi script treated Path B via three-Route enumeration (bare-CC vs
P4-D-cited vs substrate-native), this S82 run tightens the LIZZI-TRACK emphasis
to DIRECT SPECTRAL-MOMENT READING: the Seeley-DeWitt coefficients a_0, a_2 at
tau = tau_fold are substituted into Friedmann H^2 = (8 pi / 3) * rho /
M_Pl_eff^2 with NO dynamical integration.  The sister script
s80_h_tilde_epoch_td.py uses the Friedmann ODE chain; convergence of the
static-spectral and dynamical tracks is the Wave-2 unblock criterion.

Gate: S82-H-TILDE-EPOCH-LI  (CF-1 from S79 P4-D, inherited from S80).
  PASS Factor-2: |delta_OOM(best branch)| < 0.3
  INFO 2-10    : delta_OOM in [0.3, 1.0]
  FAIL > 10    : delta_OOM > 1.0 even under best branch

Trigger: [VERIFY]   (mandatory substitution chain below)
Classification: PHONONIC (per S82 task spec; spectral moments ARE the substrate,
  rho is a spectral-functional readout rather than an external fluid).

4-tuple schema:
  (H_tilde_value, scheme in {SDW, Zubarev},
   convention in {spectral-moment-direct, observational-inverse},
   L_max = 3)   -- L_max=3 is the canonical pin for a_n per S73b.

SUBSTITUTION CHAIN  (mandatory [VERIFY] trigger; DIRECT SPECTRAL-MOMENT route).
-----------------------------------------------------------------------------
Step 1. Definitions (Chamseddine-Connes 1996, CC96):
  - Bosonic spectral action S_SA = Tr f(D^2/Lambda^2) with Lambda = M_KK.
  - Heat-kernel expansion: S_SA = f_0 a_0 Lambda^4 + f_2 a_2 Lambda^2 + f_4 a_4.
  - Energy density (CC96 sec 2):  rho_SA(tau) = (2 / pi^2) * a_0(tau) * M_KK^4.
  - Newton coupling (CC96 sec 4): 1/(16 pi G_N) scales as a_2(tau) * M_KK^2.
      In Planck units with fold-pinned M_KK, set
        M_Pl_eff(tau)^2 = M_Pl_red^2 * [a_2(tau) / a_2(tau_fold)].
  - Dimensionless Hubble H_tilde(tau) := H(tau) / M_Pl_red.

Step 2. Substitute into Friedmann H^2 = (8 pi / 3) rho / M_Pl_eff^2:
    H(tau)^2
      = (8 pi / 3) * (2 / pi^2) a_0(tau) M_KK^4
        / [M_Pl_red^2 * (a_2(tau) / a_2_fold)]
      = (16 / 3 pi) * [a_0(tau) / a_2(tau)] * a_2_fold * M_KK^4 / M_Pl_red^2.
  Dividing by M_Pl_red^2:
    H_tilde(tau)^2
      = (16 / 3 pi) * [a_0(tau)/a_2(tau)] * a_2_fold * (M_KK / M_Pl_red)^4.

Step 3. At fold (tau = tau_fold): a_0(tau) = a0_fold, a_2(tau) = a2_fold.
  The factor a_2_fold * (1/a2_fold) = 1, so
    H_tilde_B^2 = (16 / 3 pi) * a0_fold * (M_KK / M_Pl_red)^4.
  Call this the "SDW direct" branch — it uses the *bare* zeroth moment a_0,
  which is the conformally-invariant volume term in the heat kernel.

Step 4. Zubarev (CC-subtracted) branch: the bare a_0 is a conserved Casimir
  of the Richardson-Gaudin integrable sector of the substrate (S59, S60);
  only the non-integrable Josephson piece sources gravity.  Operationally
  this is single-pin H_tilde_B^Zub = (M_KK / M_Pl_red)^2 / sqrt(3), the
  canonical P4-D convention.  Same pin for Path A (mode-equation output is
  scheme-invariant in the UV-clean pivot sector).

Step 5. Direction read-off.  The gate compares |delta_OOM| to 0.3.  Under
  both schemes, the spectral-moment-direct Path B gives delta_OOM > 1.0
  (SDW: 6.76; Zubarev: 2.24); Path A (horizon-exit, mode-equation output)
  gives delta_OOM = -0.4363 in both schemes.  Best branch = A.  |0.4363| is
  in [0.3, 1.0], so verdict is INFO-2-10.

FUNCTIONAL-INDEPENDENT vs SCHEME-DEPENDENT (Lizzi permanent classification).
-----------------------------------------------------------------------------
  * FUNCTIONAL-INDEPENDENT:
      - Path-A value H_tilde_A = sqrt(A_s_raw * 8 pi^2 * eps) is the SAME
        under SDW and Zubarev — the mode-equation A_s inherits no regulator
        coupling in the UV-clean pivot sector.
      - Gate verdict (best branch = A, INFO-2-10) is the SAME.
  * SCHEME-DEPENDENT:
      - H_tilde_B (absolute Path-B value) moves by 2.26 OOM (factor 181)
        between SDW and Zubarev.  This IS the CC problem expressed in H
        rather than in Lambda.
      - Ratio r_AB depends on the Path-B scheme.

Dual-owner convergence (vs s80_h_tilde_epoch_td.npz sister output):
  TD track uses zeta scheme (Kerner-route M_KK alt) + dynamical post-fold
  dS cascade at N_pivot = 55.  If the S82 LI (SDW or Zubarev) H_tilde_A
  agrees with TD H_tilde_A within 20%, Wave 2 proceeds with convergent.
  Observed at S80 close: LI-TD Path A rel_diff = 99.58% (DIVERGED); per
  S80 memo file, this triggered Wave-2 dual-branch dispatch.  We re-check.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path
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


sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import (                 # noqa: F401
    PI,
    M_Pl_reduced,
    M_KK_gravity,
    M_KK_kerner,
    tau_fold,
    a0_fold,
    a2_fold,
    a4_fold,
    H_fold,
    A_s_CMB,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S82"                                                    # (local)
GATE_ID = "S82-H-TILDE-EPOCH-LI"                                   # (local)
L_MAX = 3                                                          # (local) canonical L_max=3 for a_n (S73b)

# Observational pins
EPS_PIVOT = 0.01                                                   # (local) UNIFIED-AS-79 benchmark eps
A_s_OBS = A_s_CMB                                                  # (local) Planck 2018 pivot amplitude = 2.1e-9
UNIFIED_AS_79_RAW = 7.69e-10                                       # (local) P2-A raw mode-eq A_s

# Gate thresholds
PASS_F2_THRESHOLD = 0.3                                            # (local) delta_OOM Factor-2 cutoff
INFO_THRESHOLD = 1.0                                               # (local) delta_OOM 2-10 cutoff

# Output destinations
OUT_NPZ = resolve_output(82, 's82_w1_1_h_tilde_li.npz')
OUT_PNG = resolve_output(82, 's82_w1_1_h_tilde_li.png')
VERDICT_TXT = resolve_output(82, 's82_gate_verdicts.txt')

INPUT_FILES = [
    resolve_script(None, 'canonical_constants.py'),
    resolve_output(80, 's80_h_tilde_epoch_td.npz'),   # TD convergence cross-check sibling
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                           # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                      # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()                                           # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def verdict_label(delta_OOM: float) -> str:
    """Pre-registered threshold mapping per plan L788-L799."""
    a = abs(delta_OOM)                                             # (local)
    if a < PASS_F2_THRESHOLD:
        return "PASS-F2"
    if a < INFO_THRESHOLD:
        return "INFO-2-10"
    return "FAIL-GT10"


def compute_h_tilde_B_SDW(M_KK_val: float) -> float:
    """Direct spectral-moment Friedmann at fold, SDW scheme (bare a_0 sourcing)."""
    eps4 = (M_KK_val / M_Pl_reduced) ** 4                          # (local)
    H2 = (16.0 / (3.0 * PI)) * a0_fold * eps4                      # (local) dimensionless^2
    return float(np.sqrt(H2))


def compute_h_tilde_B_Zubarev(M_KK_val: float) -> float:
    """Single-pin CC-subtracted (Zubarev-analog) H_tilde at fold."""
    eps2 = (M_KK_val / M_Pl_reduced) ** 2                          # (local)
    return float(eps2 / np.sqrt(3.0))


def compute_h_tilde_A_from_As_raw(A_s_raw: float, eps_val: float) -> float:
    """Horizon-exit H_tilde from Mukhanov-Sasaki inverse identification."""
    return float(np.sqrt(A_s_raw * 8.0 * PI**2 * eps_val))


def A_s_from_h_tilde(H_tilde_val: float, eps_val: float) -> float:
    """Forward A_s(H_tilde) from mode-equation normalization."""
    return float(H_tilde_val**2 / (8.0 * PI**2 * eps_val))


def main() -> int:
    # --- 1. SHA-256 pins (first 20 stdout lines) -----------------------
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (full below)")
    print(f"  full closure sha256 = {closure}")
    print()

    # --- 2. Path B under each scheme (static spectral read) ------------
    M_KK = M_KK_gravity                                            # (local) gravity-route canonical
    eps_MKK2 = (M_KK / M_Pl_reduced) ** 2                          # (local)

    H_B_SDW = compute_h_tilde_B_SDW(M_KK)                          # (local)
    H_B_Zub = compute_h_tilde_B_Zubarev(M_KK)                      # (local)

    print("=" * 78)
    print("STEP 1-3: Direct spectral-moment Path B (H_tilde at fold)")
    print("=" * 78)
    print(f"  M_KK (gravity route) = {M_KK:.6e} GeV")
    print(f"  M_Pl_reduced         = {M_Pl_reduced:.6e} GeV")
    print(f"  (M_KK/M_Pl_red)^2    = {eps_MKK2:.6e}")
    print(f"  a_0_fold (L_max=3)   = {a0_fold:.4f}")
    print(f"  a_2_fold (L_max=3)   = {a2_fold:.4f}")
    print(f"  H_tilde_B^SDW      = sqrt((16/3pi)*a_0*(M_KK/M_Pl)^4) = {H_B_SDW:.6e}")
    print(f"  H_tilde_B^Zubarev  = (M_KK/M_Pl_red)^2 / sqrt(3)      = {H_B_Zub:.6e}")
    print(f"  Scheme ratio SDW/Zub = {H_B_SDW / H_B_Zub:.2f}  "
          f"({np.log10(H_B_SDW / H_B_Zub):.2f} OOM)")
    print()

    # --- 3. Path A from UNIFIED-AS-79 inverse identification -----------
    H_A_SDW = compute_h_tilde_A_from_As_raw(UNIFIED_AS_79_RAW, EPS_PIVOT)
    H_A_Zub = H_A_SDW                                              # mode-eq output scheme-invariant in UV-clean pivot
    H_tilde_obs = compute_h_tilde_A_from_As_raw(A_s_OBS, EPS_PIVOT)

    print("=" * 78)
    print("STEP 4: Path A (horizon-exit) from UNIFIED-AS-79 inverse ID")
    print("=" * 78)
    print(f"  UNIFIED-AS-79 raw A_s   = {UNIFIED_AS_79_RAW:.3e}")
    print(f"  eps_pivot (slow-roll)   = {EPS_PIVOT:.4f}")
    print(f"  H_tilde_A^SDW/Zubarev   = {H_A_SDW:.6e}  (scheme-invariant)")
    print(f"  H_tilde_obs (from Planck A_s) = {H_tilde_obs:.6e}")
    print()

    # --- 4. A_s under each branch / scheme, gate evaluation ------------
    branch_results = {}                                            # (local)
    for scheme_name, H_A_val, H_B_val in [
        ("SDW",     H_A_SDW, H_B_SDW),
        ("Zubarev", H_A_Zub, H_B_Zub),
    ]:
        A_s_A = A_s_from_h_tilde(H_A_val, EPS_PIVOT)               # (local)
        A_s_B = A_s_from_h_tilde(H_B_val, EPS_PIVOT)               # (local)
        d_A = np.log10(A_s_A / A_s_OBS)                            # (local)
        d_B = np.log10(A_s_B / A_s_OBS)                            # (local)
        best_tag = "A" if abs(d_A) < abs(d_B) else "B"             # (local)
        best_abs = min(abs(d_A), abs(d_B))                         # (local)
        verdict = verdict_label(best_abs)                          # (local)
        r_AB = H_A_val / H_B_val                                   # (local)
        branch_results[scheme_name] = dict(
            H_A=H_A_val, H_B=H_B_val,
            A_s_A=A_s_A, A_s_B=A_s_B,
            d_A=d_A, d_B=d_B, r_AB=r_AB,
            best_tag=best_tag, best_abs=best_abs,
            verdict=verdict,
        )

    print("=" * 78)
    print("STEP 5: Gate evaluation under each scheme")
    print("=" * 78)
    for name, r in branch_results.items():
        print(f"  [{name}]  "
              f"H_A={r['H_A']:.4e}  H_B={r['H_B']:.4e}  r_AB={r['r_AB']:.4e}")
        print(f"           A_s_A={r['A_s_A']:.4e}  A_s_B={r['A_s_B']:.4e}")
        print(f"           d_OOM(A)={r['d_A']:+.4f}  d_OOM(B)={r['d_B']:+.4f}")
        print(f"           best={r['best_tag']}({r['best_abs']:.4f})  "
              f"-> {r['verdict']}")
    print()

    # Canonical gate branch: use SDW (direct spectral-moment read, the lizzi-
    # track primary emphasis).  Zubarev is the companion for scheme-dependence.
    sdw = branch_results["SDW"]                                    # (local)
    canonical_verdict = sdw["verdict"]                             # (local)
    # The value we report in the 4-tuple is the BEST-BRANCH H_tilde under SDW.
    canonical_value = sdw["H_A"] if sdw["best_tag"] == "A" else sdw["H_B"]   # (local)

    # --- 5. Dual-owner convergence check vs TD sister ------------------
    td_convergence_note = "transit-TD NPZ unavailable"             # (local)
    converged_A = None                                             # (local)
    converged_B = None                                             # (local)
    td_npz_path = resolve_output(80, 's80_h_tilde_epoch_td.npz')
    if td_npz_path.exists():
        td = np.load(td_npz_path, allow_pickle=True)
        td_keys = list(td.keys())
        # Prefer *_framework_dimless* variants (zeta-scheme canonical TD).
        if "H_tilde_A_framework_dimless" in td_keys and "H_tilde_B_dimless" in td_keys:
            H_A_td = float(td["H_tilde_A_framework_dimless"])
            H_B_td = float(td["H_tilde_B_dimless"])
            rel_A = abs(H_A_SDW - H_A_td) / max(abs(H_A_td), 1e-30)   # (local)
            rel_B = abs(H_B_SDW - H_B_td) / max(abs(H_B_td), 1e-30)   # (local)
            converged_A = rel_A < 0.20                             # (local)
            converged_B = rel_B < 0.20                             # (local)
            td_convergence_note = (
                f"TD framework: H_A={H_A_td:.4e}  H_B={H_B_td:.4e}; "
                f"LI(SDW) vs TD -- A rel_diff={rel_A*100:.1f}% ({'CONVERGED' if converged_A else 'DIVERGED'}), "
                f"B rel_diff={rel_B*100:.1f}% ({'CONVERGED' if converged_B else 'DIVERGED'})"
            )
            print("Dual-owner TD cross-check:")
            print(f"  TD H_tilde_A (framework)  = {H_A_td:.4e}")
            print(f"  TD H_tilde_B              = {H_B_td:.4e}")
            print(f"  rel_diff A = {rel_A*100:.2f}%  -> "
                  f"{'CONVERGED (<20%)' if converged_A else 'DIVERGED (>20%)'}")
            print(f"  rel_diff B = {rel_B*100:.2f}%  -> "
                  f"{'CONVERGED (<20%)' if converged_B else 'DIVERGED (>20%)'}")
            # Also report obs-branch convergence (this is the TD zero-by-construction reference)
            if "H_tilde_A_obs_dimless" in td_keys:
                H_A_td_obs = float(td["H_tilde_A_obs_dimless"])
                rel_A_obs = abs(H_A_SDW - H_A_td_obs) / max(abs(H_A_td_obs), 1e-30)   # (local)
                print(f"  TD H_tilde_A (obs-inverse) = {H_A_td_obs:.4e}  "
                      f"(LI rel_diff = {rel_A_obs*100:.2f}%)")
        else:
            td_convergence_note = f"TD NPZ missing framework keys; have {td_keys}"

    print()

    # --- 6. Save NPZ ---------------------------------------------------
    np.savez(
        OUT_NPZ,
        # Canonical pins
        M_KK_used=M_KK,
        M_Pl_reduced=M_Pl_reduced,
        tau_fold=tau_fold,
        a0_fold=a0_fold,
        a2_fold=a2_fold,
        a4_fold=a4_fold,
        eps_pivot=EPS_PIVOT,
        A_s_obs=A_s_OBS,
        UNIFIED_AS_79_RAW=UNIFIED_AS_79_RAW,
        # SDW scheme results
        H_tilde_A_SDW=H_A_SDW,
        H_tilde_B_SDW=H_B_SDW,
        A_s_A_SDW=sdw["A_s_A"],
        A_s_B_SDW=sdw["A_s_B"],
        delta_OOM_A_SDW=sdw["d_A"],
        delta_OOM_B_SDW=sdw["d_B"],
        r_AB_SDW=sdw["r_AB"],
        best_branch_SDW=sdw["best_tag"],
        best_abs_SDW=sdw["best_abs"],
        verdict_SDW=sdw["verdict"],
        # Zubarev scheme results
        H_tilde_A_Zubarev=branch_results["Zubarev"]["H_A"],
        H_tilde_B_Zubarev=branch_results["Zubarev"]["H_B"],
        A_s_A_Zubarev=branch_results["Zubarev"]["A_s_A"],
        A_s_B_Zubarev=branch_results["Zubarev"]["A_s_B"],
        delta_OOM_A_Zubarev=branch_results["Zubarev"]["d_A"],
        delta_OOM_B_Zubarev=branch_results["Zubarev"]["d_B"],
        r_AB_Zubarev=branch_results["Zubarev"]["r_AB"],
        best_branch_Zubarev=branch_results["Zubarev"]["best_tag"],
        best_abs_Zubarev=branch_results["Zubarev"]["best_abs"],
        verdict_Zubarev=branch_results["Zubarev"]["verdict"],
        # Scheme comparison
        H_B_ratio_SDW_over_Zubarev=H_B_SDW / H_B_Zub,
        log10_scheme_ratio=np.log10(H_B_SDW / H_B_Zub),
        H_tilde_obs=H_tilde_obs,
        # Dual-owner convergence
        td_convergence_note=td_convergence_note,
        converged_A=converged_A if converged_A is not None else "unavailable",
        converged_B=converged_B if converged_B is not None else "unavailable",
        # 4-tuple tags
        scheme_primary="SDW",
        convention_primary="spectral-moment-direct",
        L_max=L_MAX,
        canonical_value=canonical_value,
        canonical_verdict=canonical_verdict,
        closure_sha256=closure,
    )
    print(f"Saved NPZ: {OUT_NPZ}")

    # --- 7. Plot -------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(12.5, 5.0))

    ax1 = axes[0]
    schemes = ["SDW", "Zubarev"]
    H_A_values = [branch_results[s]["H_A"] for s in schemes]       # (local)
    H_B_values = [branch_results[s]["H_B"] for s in schemes]       # (local)
    x = np.arange(len(schemes))                                    # (local)
    w = 0.32                                                       # (local)
    ax1.bar(x - w / 2, H_A_values, width=w, label="Path A (horizon-exit)",
            color="tab:green", alpha=0.8, edgecolor="k")
    ax1.bar(x + w / 2, H_B_values, width=w, label="Path B (fold, direct)",
            color="tab:red", alpha=0.8, edgecolor="k")
    ax1.axhline(H_tilde_obs, color="tab:purple", ls=":", lw=2,
                label=f"H_tilde_obs (Planck) = {H_tilde_obs:.2e}")
    ax1.set_xticks(x)
    ax1.set_xticklabels(schemes)
    ax1.set_ylabel("H_tilde = H / M_Pl_red (dimensionless)")
    ax1.set_yscale("log")
    ax1.set_title("H_tilde under SDW vs Zubarev (LI direct spectral read)")
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3, axis="y")
    for i, (a, b) in enumerate(zip(H_A_values, H_B_values)):
        ax1.text(i - w / 2, a * 1.4, f"{a:.2e}", ha="center", fontsize=8)
        ax1.text(i + w / 2, b * 1.4, f"{b:.2e}", ha="center", fontsize=8)

    ax2 = axes[1]
    bars_x = np.arange(4)                                          # (local)
    d_vals = [sdw["d_A"], sdw["d_B"],
              branch_results["Zubarev"]["d_A"],
              branch_results["Zubarev"]["d_B"]]                    # (local)
    bar_labels = ["SDW\nPath A", "SDW\nPath B",
                  "Zubarev\nPath A", "Zubarev\nPath B"]            # (local)
    bar_colors = ["tab:green", "tab:red", "tab:green", "tab:red"]  # (local)
    ax2.bar(bars_x, d_vals, color=bar_colors, alpha=0.75, edgecolor="k")
    ax2.axhline(PASS_F2_THRESHOLD, color="gray", ls="--", alpha=0.6,
                label=f"PASS F2 ({PASS_F2_THRESHOLD:.1f} OOM)")
    ax2.axhline(-PASS_F2_THRESHOLD, color="gray", ls="--", alpha=0.6)
    ax2.axhline(INFO_THRESHOLD, color="black", ls=":", alpha=0.6,
                label=f"INFO bound ({INFO_THRESHOLD:.1f} OOM)")
    ax2.axhline(-INFO_THRESHOLD, color="black", ls=":", alpha=0.6)
    ax2.set_xticks(bars_x)
    ax2.set_xticklabels(bar_labels, fontsize=9)
    ax2.set_ylabel("delta_OOM = log10(A_s(H_tilde) / Planck)")
    ax2.set_title("Gate verdict: A_s gap under each (scheme, branch)")
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3, axis="y")
    for i, v in enumerate(d_vals):
        offset = 0.2 if v >= 0 else -0.35                          # (local)
        ax2.text(i, v + offset, f"{v:+.3f}", ha="center", fontsize=8)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=135)
    print(f"Saved plot: {OUT_PNG}")
    plt.close(fig)

    # --- 8. Append verdict line to s82_gate_verdicts.txt ---------------
    verdict_line = (
        f"{GATE_ID}: {canonical_verdict} -- "
        f"value={canonical_value:.4e} scheme=SDW "
        f"convention=spectral-moment-direct L_max={L_MAX} sha256={closure}"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line + "\n")
    # Also append a companion Zubarev line for dual-scheme record.
    zub = branch_results["Zubarev"]
    zub_value = zub["H_A"] if zub["best_tag"] == "A" else zub["H_B"]   # (local)
    verdict_line_zub = (
        f"{GATE_ID}-ZUBAREV: {zub['verdict']} -- "
        f"value={zub_value:.4e} scheme=Zubarev "
        f"convention=single-pin-CC-subtracted L_max={L_MAX} sha256={closure}"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(verdict_line_zub + "\n")

    print()
    print("=" * 78)
    print("VERDICT LINE (canonical SDW):")
    print("=" * 78)
    print(verdict_line)
    print()
    print("VERDICT LINE (companion Zubarev):")
    print(verdict_line_zub)
    print()
    print(f"Appended to: {VERDICT_TXT}")

    # --- 9. 4-tuple final line -----------------------------------------
    four_tuple = (
        f"(value={canonical_value:.6e}, scheme=SDW, "
        f"convention=spectral-moment-direct, L_max={L_MAX})"
    )
    print()
    print(four_tuple)

    return 0 if canonical_verdict != "FAIL-GT10" else 1


if __name__ == "__main__":
    sys.exit(main())
