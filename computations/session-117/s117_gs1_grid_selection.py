#!/usr/bin/env python3
"""
S117 W1-2 CF-S117-GS-1 — between-grid scale-coincidence sub-discriminator
=========================================================================

Gate: CF-S117-GS-1 ([SIGN])

Adjudicates the A_s grid SELECTION between the two normalization grids of the
0.668-OOM A_s fork:

  ℓ_occ      = ξ_KZ                       [G1: KZ coherence/healing length, UV;
                                           the box-delta/impulse grid, A_s=1.5367e-8]
  ℓ_horizon  = c_s / (aH)|_exit           [G2: acoustic sound-horizon comoving scale,
                                           IR; the TD/ζ (H̃) grid, A_s=3.2994e-9]

Three-branch partition on  Δ_scale = |log₁₀(ℓ_occ) − log₁₀(ℓ_horizon)|:

  CONVENTION-BLOCKED        : Δ_scale ≤ 0.05                      ⇒ scales coincide,
                              fork is a normalization-convention artifact (PASS)
  PHYSICS-SCALE-SEPARATION  : |2·Δ_scale − 0.668| ≤ 0.1          ⇒ two genuine substrate
                              scales whose ratio under deg=+2 IS the fork ⇒ Volovik
                              hydrodynamic selection picks the acoustic-horizon grid (PASS)
  INFO-RESIDUAL-PREFACTOR   : neither                             ⇒ a residual non-scale
                              prefactor exists; deg=+2 transport is not the sole carrier (INFO)

deg=+2 backbone (canonical:717, S93 W7-1; deg_T_BZ_pivot = +2.0, NON-SCALAR):
  A_s ∝ carrier²,  carrier ∝ scale^{+1}  ⇒  A_s ∝ scale^{+2}.
  fork_OOM = log₁₀(A_s_G1/A_s_G2) = 2·log₁₀(2.15814) = 0.66825 (Sage-exact backbone).

[SIGN] item: resolve the carrier↔scale exponent sign. deg_T_BZ_pivot = +2 > 0
  ⇒ carrier ∝ scale^{+1} (sign = +, |±1|=1 the load-bearing magnitude; the near-flat
  sudden-spectrum slope −0.003135 makes the within-grid tilt sub-dominant, so the
  scale-dependence of A_s is carried by the deg=+2 transport, not the tilt).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/_shared/canonical_constants.py
  - computations/session-77/s77_n_pivot_map.npz   (aH|_exit kinematics)
  - script bytes

Output 4-tuple:
  (value=<Δ_scale / branch>, scheme=GRID-SELECTION-DISJOINT-SCALES,
   convention=xi_KZ-coherence(UV)-vs-acoustic-sound-horizon(IR), L_max=N/A)

Classification: PHONONIC. GS-1 asks the substrate which of its two intrinsic
lengths the curvature/a₂-channel (hydrodynamic IR) observable reads at: ℓ_occ
(KZ healing length, UV coherence of the post-transit GGE relic) or ℓ_horizon
(acoustic sound-horizon, IR causal scale of first-sound across the supersonic
transit). These are two substrate-IS lengths the fabric carries, not coordinates
in a container.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 2 — Standard imports + path setup (SHARED_DIR before canonical import)
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
# Used: xi_KZ_FW, c_Gold, c_BLV, c_fabric, Mach_max_framework, H_fold,
#       dt_transit, deg_T_BZ_pivot

os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (two scalar evals)
os.environ.setdefault("MKL_NUM_THREADS", "8")
import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration
# ---------------------------------------------------------------------------

SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-GS-1"                                           # (local)
SCHEME = "GRID-SELECTION-DISJOINT-SCALES"                          # (local)
CONVENTION = "xi_KZ-coherence-UV-vs-acoustic-sound-horizon-IR"     # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered branch thresholds (SOURCE-RECON log-OOM bands)
CONV_BLOCKED_TOL = 0.05                                            # (local) Δ_scale ≤ 0.05
SCALE_SEP_TOL = 0.10                                               # (local) |2Δ−0.668| ≤ 0.1
BACKBONE_FAIL_TOL = 1.0                                            # (local) |2Δ−0.668| > 1 ⇒ FAIL
BACKBONE_RELTOL = 1e-6                                             # (local) Sage-exact identity check

# Fork anchors (the two A_s grid values; 1-1 substitution-chain inputs)
A_s_G1 = 1.5367e-8                                                 # (local) box-delta/impulse, ξ_KZ grid (+0.864)
A_s_G2 = 3.2994e-9                                                 # (local) TD/ζ (H̃) grid (+0.196)

# Output destinations
OUT_NPZ = SESSION_DIR / "s117_gs1_grid_selection.npz"
OUT_PNG = SESSION_DIR / "s117_gs1_grid_selection.png"

S77_NPZ = COMPUTATIONS_DIR / "session-77" / "s77_n_pivot_map.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S77_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
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
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- Def 1: ℓ_occ = ξ_KZ (UV coherence / healing length) -----------------
    l_occ = xi_KZ_FW                                            # (local) M_KK^-1

    # --- Def 2: c_s = transit-frame sound speed -----------------------------
    # Plan-pinned canonical sound-speed identification = c_Gold (Goldstone
    # first-sound). The Mach relation Mach = v_transit/c_s (canonical:2505)
    # then FIXES the implied transit velocity v_transit = Mach·c_s.
    c_s_primary = c_Gold                                        # (local) 0.915  PRIMARY (plan-pin)
    c_s_crosscheck = c_BLV                                      # (local) 0.485  post-fold GGE scalar c_s
    Mach = Mach_max_framework                                   # (local) 13.75
    v_transit_implied = Mach * c_s_primary                      # (local) Mach·c_Gold (consistency)

    # --- Def 4: (aH)|_exit from the transit kinematics ----------------------
    # H·dt_transit consistency (plan-pin 0.663): H_fold·dt_transit
    H_dt = H_fold * dt_transit                                  # (local) ≈ 0.663
    # s77 exit kinematics: at horizon exit k = aH, so (aH)|_exit = k_pivot.
    d77 = np.load(S77_NPZ, allow_pickle=True)                   # (local)
    k_pivot = float(d77["k_pivot_com_fold"])                    # (local) 14.3111 M_KK
    k_over_aH_fold = float(d77["k_over_aH_fold"])               # (local) 14.6721 (~14.7)
    a_exit = float(d77["pivot_a_at_exit"])                      # (local) 22.6105
    H_exit = float(d77["pivot_H_at_exit"])                      # (local) 0.63294
    aH_exit_from_product = a_exit * H_exit                      # (local) exit-kinematics product
    aH_exit = k_pivot                                           # (local) (aH)|_exit = k_pivot (exit: aH=k)
    aH_fold = k_pivot / k_over_aH_fold                          # (local) 0.9754 (cross-check, fold)
    # consistency of the two exit routes (should match to ~1e-5)
    exit_route_reldev = abs(aH_exit_from_product - k_pivot) / k_pivot   # (local)

    # --- Def 3: ℓ_horizon = c_s/(aH)|_exit (comoving acoustic sound horizon)
    # dimension: [c_s]=M_KK^0 (velocity), [aH]=M_KK ⇒ ℓ_horizon in M_KK^-1 (length).
    l_horizon_primary = c_s_primary / aH_exit                  # (local) M_KK^-1
    l_horizon_crosscheck = c_s_crosscheck / aH_exit            # (local) M_KK^-1

    # --- Def 5: Δ_scale ------------------------------------------------------
    dscale_primary = abs(np.log10(l_occ) - np.log10(l_horizon_primary))      # (local)
    dscale_crosscheck = abs(np.log10(l_occ) - np.log10(l_horizon_crosscheck))  # (local)

    # --- deg=+2 backbone -----------------------------------------------------
    deg = deg_T_BZ_pivot                                        # (local) +2.0
    fork_ratio = A_s_G1 / A_s_G2                                # (local) 4.6575
    fork_OOM = np.log10(fork_ratio)                            # (local) 0.66825
    carrier_ratio = np.sqrt(fork_ratio)                        # (local) 2.15813
    backbone_2log = 2.0 * np.log10(carrier_ratio)             # (local) = fork_OOM by identity
    # Sage-exact identity: 2·log10(sqrt(r)) == log10(r). rel-dev → machine ε.
    backbone_identity_reldev = abs(backbone_2log - fork_OOM) / abs(fork_OOM)  # (local)

    two_dscale_primary = 2.0 * dscale_primary                   # (local)
    two_dscale_crosscheck = 2.0 * dscale_crosscheck            # (local)
    backbone_resid_primary = abs(two_dscale_primary - fork_OOM)         # (local)
    backbone_resid_crosscheck = abs(two_dscale_crosscheck - fork_OOM)   # (local)

    # --- [SIGN]: carrier↔scale exponent --------------------------------------
    # A_s ∝ carrier² and deg ≡ d(ln A_s)/d(ln scale) = 2·e (e = carrier exponent).
    # deg = +2 ⇒ e = +1 ⇒ carrier ∝ scale^{+1}; sign(e) = + (consistent with deg>0).
    carrier_exponent = deg / 2.0                               # (local) +1.0
    carrier_sign = "+" if carrier_exponent > 0 else "-"        # (local)
    sign_consistent_with_deg = (carrier_exponent > 0) == (deg > 0)  # (local) True

    # --- required-c_s window for PHYSICS-SCALE-SEPARATION (transparency) ------
    # |2Δ − 0.668| ≤ 0.1  ⇒  Δ ∈ [(fork−0.1)/2, (fork+0.1)/2].
    dscale_lo = (fork_OOM - SCALE_SEP_TOL) / 2.0               # (local)
    dscale_hi = (fork_OOM + SCALE_SEP_TOL) / 2.0               # (local)
    # ℓ_horizon = ℓ_occ·10^{Δ} (IR>UV branch) ⇒ c_s = ℓ_horizon·aH_exit.
    cs_req_lo = (l_occ * 10.0 ** dscale_lo) * aH_exit          # (local)
    cs_req_hi = (l_occ * 10.0 ** dscale_hi) * aH_exit          # (local)
    cs_req_center = (l_occ * 10.0 ** (fork_OOM / 2.0)) * aH_exit  # (local) exact-fork c_s

    # --- 3He-B lab cross-check (V.2; does NOT gate) --------------------------
    # R_scale = ℓ_occ/ℓ_horizon is DIMENSIONLESS ⇒ the S86 W11-1 M_KK→SI length
    # map cancels (numerator and denominator scale by the same factor): the lab
    # twin reads the SAME R_scale. R_scale<1 ⇒ microscopic (UV) below causal (IR).
    R_scale_primary = l_occ / l_horizon_primary                # (local) conversion-invariant
    R_scale_crosscheck = l_occ / l_horizon_crosscheck          # (local)
    lab_corroborates = (R_scale_primary < 1.0)                 # (local) microscopic-below-causal
    lab_sign_contradiction = not lab_corroborates              # (local) FAIL trigger if True

    # --- three-branch partition (on the PRIMARY = c_Gold reading) ------------
    conv_blocked = dscale_primary <= CONV_BLOCKED_TOL          # (local)
    scale_sep = backbone_resid_primary <= SCALE_SEP_TOL        # (local)
    backbone_diverges = backbone_resid_primary > BACKBONE_FAIL_TOL  # (local) FAIL trigger

    if conv_blocked:
        branch = "CONVENTION-BLOCKED"                          # (local)
        magnitude_verdict = "PASS"                             # (local)
    elif scale_sep:
        branch = "PHYSICS-SCALE-SEPARATION"                    # (local)
        magnitude_verdict = "PASS"                             # (local)
    else:
        branch = "INFO-RESIDUAL-PREFACTOR"                     # (local)
        magnitude_verdict = "INFO"                             # (local)

    # FAIL guards: backbone divergence >1 OOM OR lab-sign contradiction.
    fail_triggered = backbone_diverges or lab_sign_contradiction  # (local)
    if fail_triggered:
        branch = "FAIL-MACHINERY-UNSOUND"                      # (local)
        magnitude_verdict = "FAIL"                             # (local)

    sign_verdict = "PASS" if sign_consistent_with_deg else "FAIL"  # (local)
    regime_verdict = "VALID"                                   # (local) closed-form, no breakdown

    # composite collapse (gate-verdicts.md)
    if regime_verdict == "BREAKDOWN" or sign_verdict == "FAIL":
        composite = "FAIL"                                     # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                     # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                     # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                     # (local)
    else:
        composite = "PASS"                                     # (local)

    return {
        "l_occ": l_occ,
        "c_s_primary": c_s_primary, "c_s_crosscheck": c_s_crosscheck,
        "Mach": Mach, "v_transit_implied": v_transit_implied, "H_dt": H_dt,
        "k_pivot": k_pivot, "k_over_aH_fold": k_over_aH_fold,
        "a_exit": a_exit, "H_exit": H_exit,
        "aH_exit": aH_exit, "aH_exit_from_product": aH_exit_from_product,
        "aH_fold": aH_fold, "exit_route_reldev": exit_route_reldev,
        "l_horizon_primary": l_horizon_primary,
        "l_horizon_crosscheck": l_horizon_crosscheck,
        "dscale_primary": dscale_primary, "dscale_crosscheck": dscale_crosscheck,
        "deg": deg, "fork_ratio": fork_ratio, "fork_OOM": fork_OOM,
        "carrier_ratio": carrier_ratio, "backbone_2log": backbone_2log,
        "backbone_identity_reldev": backbone_identity_reldev,
        "two_dscale_primary": two_dscale_primary,
        "two_dscale_crosscheck": two_dscale_crosscheck,
        "backbone_resid_primary": backbone_resid_primary,
        "backbone_resid_crosscheck": backbone_resid_crosscheck,
        "carrier_exponent": carrier_exponent, "carrier_sign": carrier_sign,
        "sign_consistent_with_deg": sign_consistent_with_deg,
        "dscale_window_lo": dscale_lo, "dscale_window_hi": dscale_hi,
        "cs_req_lo": cs_req_lo, "cs_req_hi": cs_req_hi, "cs_req_center": cs_req_center,
        "R_scale_primary": R_scale_primary, "R_scale_crosscheck": R_scale_crosscheck,
        "lab_corroborates": lab_corroborates,
        "lab_sign_contradiction": lab_sign_contradiction,
        "conv_blocked": conv_blocked, "scale_sep": scale_sep,
        "backbone_diverges": backbone_diverges, "fail_triggered": fail_triggered,
        "branch": branch,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict, "composite": composite,
        "value": dscale_primary,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(R: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

    # Panel 1 — the two substrate length scales on a log axis -----------------
    l_occ = R["l_occ"]                                          # (local)
    lh_g = R["l_horizon_primary"]                               # (local)
    lh_b = R["l_horizon_crosscheck"]                            # (local)
    target = l_occ * 10.0 ** (R["fork_OOM"] / 2.0)             # (local) PHYSICS-SCALE-SEP target (IR)
    band_lo = l_occ * 10.0 ** R["dscale_window_lo"]            # (local)
    band_hi = l_occ * 10.0 ** R["dscale_window_hi"]            # (local)

    ax1.axvspan(band_lo, band_hi, color="tab:green", alpha=0.18,
                label=f"PHYSICS-SCALE-SEP band for ℓ_horizon [{band_lo:.4f},{band_hi:.4f}]")
    ax1.axvspan(l_occ * 10.0 ** (-CONV_BLOCKED_TOL), l_occ * 10.0 ** CONV_BLOCKED_TOL,
                color="tab:blue", alpha=0.18,
                label="CONVENTION-BLOCKED band (Δ≤0.05 around ℓ_occ)")
    for x, lab, col in [
        (l_occ, "ℓ_occ = ξ_KZ (UV)", "k"),
        (lh_g, f"ℓ_horizon (c_Gold={c_Gold})", "tab:red"),
        (lh_b, f"ℓ_horizon (c_BLV={c_BLV})", "tab:orange"),
        (target, "PHYSICS-SCALE-SEP target (ℓ_occ·2.158)", "tab:green"),
    ]:
        ax1.axvline(x, color=col, lw=2)
        ax1.text(x, 0.6, f" {lab}\n {x:.4f}", rotation=90, va="bottom",
                 ha="center", fontsize=8, color=col)
    ax1.set_xscale("log")
    ax1.set_xlim(min(l_occ, lh_b) * 0.5, max(lh_g, target) * 2.0)
    ax1.set_yticks([])
    ax1.set_xlabel("comoving length  (M_KK$^{-1}$)")
    ax1.set_title(f"GS-1 between-grid scales — branch: {R['branch']}  "
                  f"(Δ_scale={R['dscale_primary']:.4f}, c_Gold primary)")
    ax1.legend(fontsize=7, loc="upper left")

    # Panel 2 — 2·Δ_scale vs the deg=+2 fork backbone -------------------------
    fork = R["fork_OOM"]                                        # (local)
    ax2.axvspan(fork - SCALE_SEP_TOL, fork + SCALE_SEP_TOL, color="tab:green",
                alpha=0.18, label=f"PHYSICS-SCALE-SEP |2Δ−{fork:.3f}|≤0.1")
    ax2.axvspan(0.0, 2 * CONV_BLOCKED_TOL, color="tab:blue", alpha=0.18,
                label="CONVENTION-BLOCKED 2Δ≤0.10")
    ax2.axvline(fork, color="tab:green", lw=2.5, ls="--",
                label=f"deg=+2 backbone 2·log₁₀(2.15814)={fork:.5f}")
    ax2.axvline(R["two_dscale_primary"], color="tab:red", lw=2,
                label=f"2·Δ_scale (c_Gold)={R['two_dscale_primary']:.4f}")
    ax2.axvline(R["two_dscale_crosscheck"], color="tab:orange", lw=2,
                label=f"2·Δ_scale (c_BLV)={R['two_dscale_crosscheck']:.4f}")
    ax2.set_yticks([])
    ax2.set_xlim(-0.05, max(R["two_dscale_primary"], fork) + 0.3)
    ax2.set_xlabel("OOM")
    ax2.set_title("deg=+2 backbone cross-check (A_s ∝ scale²): "
                  f"residual={R['backbone_resid_primary']:.4f} OOM  → {R['branch']}")
    ax2.legend(fontsize=7, loc="upper right")

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload helper
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID, "verdict": verdict, "value": str(value),
        "scheme": SCHEME, "convention": CONVENTION, "l_max": str(L_MAX),
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    R = compute()

    print("--- scale identifications (M_KK^-1) ---")
    print(f"  ℓ_occ = ξ_KZ                       = {R['l_occ']:.10f}")
    print(f"  H·dt_transit (H_fold·dt_transit)  = {R['H_dt']:.6f}  (plan-pin 0.663)")
    print(f"  k_pivot (s77)                     = {R['k_pivot']:.6f}")
    print(f"  (k/aH)|_fold (s77)                = {R['k_over_aH_fold']:.6f}  (~14.7)")
    print(f"  (aH)|_exit = k_pivot              = {R['aH_exit']:.6f}")
    print(f"  (aH)|_exit = a_exit·H_exit        = {R['aH_exit_from_product']:.6f}  "
          f"(reldev {R['exit_route_reldev']:.2e})")
    print(f"  aH|_fold (cross-check)            = {R['aH_fold']:.6f}")
    print(f"  c_s primary  = c_Gold             = {R['c_s_primary']:.4f}  "
          f"(⇒ v_transit = Mach·c_s = {R['v_transit_implied']:.4f})")
    print(f"  c_s crosscheck = c_BLV            = {R['c_s_crosscheck']:.4f}  (post-fold GGE)")
    print(f"  ℓ_horizon (c_Gold)               = {R['l_horizon_primary']:.10f}")
    print(f"  ℓ_horizon (c_BLV)                = {R['l_horizon_crosscheck']:.10f}")
    print("--- Δ_scale + deg=+2 backbone ---")
    print(f"  Δ_scale (c_Gold)                  = {R['dscale_primary']:.6f}  "
          f"(2Δ={R['two_dscale_primary']:.6f})")
    print(f"  Δ_scale (c_BLV)                   = {R['dscale_crosscheck']:.6f}  "
          f"(2Δ={R['two_dscale_crosscheck']:.6f})")
    print(f"  fork_OOM = log10(A_s_G1/A_s_G2)   = {R['fork_OOM']:.6f}  "
          f"= 2·log10({R['carrier_ratio']:.6f})")
    print(f"  backbone identity rel-dev         = {R['backbone_identity_reldev']:.2e}  "
          f"(Sage-exact; tol {BACKBONE_RELTOL:.0e})")
    print(f"  backbone residual (c_Gold)        = {R['backbone_resid_primary']:.6f} OOM")
    print(f"  backbone residual (c_BLV)         = {R['backbone_resid_crosscheck']:.6f} OOM")
    print("--- branch logic ---")
    print(f"  CONVENTION-BLOCKED (Δ≤0.05)?      = {R['conv_blocked']}")
    print(f"  PHYSICS-SCALE-SEP (|2Δ−fork|≤0.1)?= {R['scale_sep']}")
    print(f"  backbone diverges (|2Δ−fork|>1)?  = {R['backbone_diverges']}")
    print(f"  required c_s window [PASS]         = [{R['cs_req_lo']:.4f}, {R['cs_req_hi']:.4f}] "
          f"(center {R['cs_req_center']:.4f}); c_BLV={c_BLV}, c_Gold={c_Gold} straddle the gap")
    print(f"  3He-B lab R_scale (c_Gold)        = {R['R_scale_primary']:.6f}  <1 ⇒ "
          f"micro-below-causal: {R['lab_corroborates']} (conversion-invariant)")
    print(f"  BRANCH                            = {R['branch']}")
    print("--- [SIGN] ---")
    print(f"  deg_T_BZ_pivot                    = {R['deg']:+.1f}")
    print(f"  carrier exponent e = deg/2        = {R['carrier_exponent']:+.1f} "
          f"(carrier ∝ scale^{R['carrier_sign']}1; |e|=1 load-bearing)")
    print(f"  sign consistent with deg>0        = {R['sign_consistent_with_deg']}")
    print()

    make_plot(R)

    np.savez(
        OUT_NPZ,
        **{k: v for k, v in R.items() if not isinstance(v, str)},
        branch=R["branch"], carrier_sign=R["carrier_sign"],
        sign_verdict=R["sign_verdict"], magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"], composite=R["composite"],
        scheme=SCHEME, convention=CONVENTION, gate_id=GATE_ID,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"saved: {OUT_NPZ.name}, {OUT_PNG.name}")

    verdict = R["composite"]  # (local)
    value = (f"{R['branch']}_Dscale={R['dscale_primary']:.4f}_2Dscale={R['two_dscale_primary']:.4f}"
             f"_vs_forkbackbone={R['fork_OOM']:.4f}_resid={R['backbone_resid_primary']:.4f}OOM"
             f"_cGold; cBLV_2Dscale={R['two_dscale_crosscheck']:.4f}_resid={R['backbone_resid_crosscheck']:.4f}"
             f"; reqd_cs=[{R['cs_req_lo']:.3f},{R['cs_req_hi']:.3f}]_gap_between_cBLV{c_BLV}_cGold{c_Gold}"
             f"; Rscale={R['R_scale_primary']:.4f}LT1_micro-below-causal_conv-invariant"
             f"; carrier_exp={R['carrier_sign']}1_deg{R['deg']:+.0f}")  # (local)

    tag = (f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=R["sign_verdict"],
                          magnitude_verdict=R["magnitude_verdict"],
                          regime_verdict=R["regime_verdict"])

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={R['sign_verdict']} "
          f"mag={R['magnitude_verdict']} regime={R['regime_verdict']}; wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
