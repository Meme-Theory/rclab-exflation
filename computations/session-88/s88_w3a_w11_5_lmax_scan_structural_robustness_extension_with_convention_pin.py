"""
S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN  (§W3a-19)
=================================================================================

L_max-scan robustness extension of the W11-5 multiplicity-weighted Mellin-pole-
window observable, with PRE-REGISTERED convention pin (Cβ unweighted-median OR
B multiplicity-weighted-median; Cα frozen-pole REJECTED at planner-w3a freeze
per W11-5 §6 finding "frozen-pole sweep is convention-shopping-equivalent" and
the demarcation-theorem analog at `regulator-convention-lockdown.md`).

Operational simplification (relative to plan §"Method" §1)
----------------------------------------------------------
The W11-5 multiplicity-weighted Mellin-pole-window observable
    R(L) = δN(L) / N_paired(L)
    δN(L) = N_unpaired(L) − 2·N_paired(L)
    N_pair(L) = sum_{(p,q): p+q ≤ L, paired_mask} d(p,q)
depends ONLY on closed-form (Weyl-dim, Casimir) per (p,q):
    d(p,q)   = (p+1)(q+1)(p+q+2)/2                          [closed form]
    C_2(p,q) = (p² + p·q + q² + 3(p+q))/3                    [closed form]
NO eigenvalue lookup is required. Therefore:
  * NO Friedrich-Bär extrapolation needed (the FB theorem is for
    eigenvalue-based observables; the W11-5 form does not use λ_min)
  * NO recursive Casimir-projection irrep construction needed
  * Wall-time per L_max is O(L²) trivial enumeration; L_max=20 is feasible
  * Verdict-line scheme tag remains the canonical
    'multiplicity-weighted-Mellin-pole-window-Lmax-scan' — NOT
    'friedrich-baer-extrapolated' (FB-extrapolation reserved for eigenvalue-
    based observables; not invoked here)

Convention pins (pre-registered at planner-w3a freeze)
------------------------------------------------------
  Cβ : unweighted-median pole-aggregation
       C_pole_Cβ(L) = numpy.median([C_2(p,q) : p+q ≤ L])
  B  : multiplicity-weighted-median pole-aggregation
       C_pole_B(L) = weighted-median with weights d(p,q)
  Cα : frozen-pole sweep — REJECTED at planner-w3a freeze
       (effacement-non-anchored ≡ outside admissibility class per
        regulator-convention-lockdown.md §"Demarcation theorem" analog)

W11-5 anchor reproduction
-------------------------
At (L_max=10, Cβ): R_substrate = −1.21222 (machine precision match expected)
W11-5 metric anchor: ratio_mismatch_W11_5 = 1.029
Plan-metric anchor at L_max=10: ratio_mismatch(L=10, Cβ; plan metric) =
  |R - R_lit| / |R_lit| = |−1.21222 − 0.03536| / 0.03536 ≈ 35.30

Saturation criterion (per plan §"Step 4-5")
-------------------------------------------
saturated_conv iff
  |ratio_mismatch(L=20, conv) − ratio_mismatch(L=18, conv)|
    < 0.05 · |ratio_mismatch(L=18, conv)|
  AND
  |ratio_mismatch(L=18, conv) − ratio_mismatch(L=16, conv)|
    < 0.05 · |ratio_mismatch(L=16, conv)|

Cross-convention check (per plan §"Step 7")
-------------------------------------------
cross_conv_deviation = |rm(L=20, Cβ) − rm(L=20, B)| / mean(...)
If > 0.5 → Conv-B canonical-metric advisory; convention pin structurally unstable.

Verdict (per plan §"PASS / FAIL / INFO thresholds")
---------------------------------------------------
PASS:  saturation_Cβ AND saturation_B AND rm(L=20, Cβ) ≤ 0.05 AND rm(L=20, B) ≤ 0.05
       AND cross_conv_deviation < 0.5
INFO-saturated-FAIL: saturation_Cβ AND saturation_B AND any rm(L=20) > 0.05
INFO-cross-conv-unstable: cross_conv_deviation ≥ 0.5
FAIL:  NOT saturation_Cβ OR NOT saturation_B at L_max=20
"""

import json
import hashlib
import os
import sys
from pathlib import Path

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent  # (local)
PROJECT_ROOT = HERE.parent  # (local)
sys.path.insert(0, str(HERE))

from canonical_constants import tau_fold, M_KK
from _spectral_action_regulators import _enumerate_sectors

# ----------------------------------------------------------------------------
# Gate identity
# ----------------------------------------------------------------------------
GATE_ID = "S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN"  # (local)
SCHEME = "multiplicity-weighted-Mellin-pole-window-Lmax-scan"  # (local) NOT friedrich-baer-extrapolated
SCHEMA_VERSION = "R3"  # (local)

# Pre-registered scan grid
L_MAX_SCAN = [10, 16, 18, 20]  # (local) per plan §"L_max_scan"
CONVENTIONS = ["Cβ", "B"]  # (local) Cα REJECTED

# Pre-registered thresholds per plan §"PASS / FAIL / INFO thresholds"
PASS_THRESH = 0.05  # (local) ratio_mismatch ceiling
SATURATION_THRESH = 0.05  # (local) relative L_max-step variation
CROSS_CONV_DEVIATION_THRESH = 0.50  # (local) cross-convention disagreement
MELLIN_WINDOW_FRAC = 0.5  # (local) match W11-5 anchor

# Friedrich-Bär lower bound (recorded but NOT used — FB-extrapolation not invoked)
FRIEDRICH_BAER_LOWER = 0.40  # (local) W11-3 calibration; recorded for plan-pin discharge

# ----------------------------------------------------------------------------
# 3He-B literature anchor (mirrored from W11-5 / §W3a-14 / §W3a-18)
# ----------------------------------------------------------------------------
DELTA_BCS_WEAK_RATIO = np.pi * np.exp(-np.euler_gamma)  # (local)
SC_CORR_A = 1.151  # (local)
SC_CORR_B = 1.111  # (local)
DELTA_A_OVER_KBT_C = DELTA_BCS_WEAK_RATIO * SC_CORR_A  # (local) ~ 2.030
DELTA_B_OVER_KBT_C = DELTA_BCS_WEAK_RATIO * SC_CORR_B  # (local) ~ 1.960
R_3HeB_lit = (
    (DELTA_A_OVER_KBT_C ** 2 - DELTA_B_OVER_KBT_C ** 2)
    / (DELTA_A_OVER_KBT_C ** 2 + DELTA_B_OVER_KBT_C ** 2)
)  # (local) +0.03536

# W11-5 anchor (under W11-5 max-denominator metric)
R_substrate_W11_5_anchor = -1.21222  # (local) W11-5 measured at (L=10, Cβ)
ratio_mismatch_W11_5_anchor = 1.029  # (local) W11-5 metric

# ----------------------------------------------------------------------------
# Input file pins
# ----------------------------------------------------------------------------
INPUT_PINS_PATHS = {  # (local)
    "canonical_constants.py": HERE / "canonical_constants.py",
    "_spectral_action_regulators.py": HERE / "_spectral_action_regulators.py",
    "s87_w11_3heb_excess_inheritance_comparison.py": (
        HERE / "s87_w11_3heb_excess_inheritance_comparison.py"
    ),
    "s88_w3a_M3C_projected_npz": (
        HERE / "s88_w3a_3heb_excess_inheritance_m3c_projected_retry.npz"
    ),
    "regulator-convention-lockdown.md": (
        PROJECT_ROOT / ".claude" / "rules" / "regulator-convention-lockdown.md"
    ),
    "math-scripts.md": (
        PROJECT_ROOT / ".claude" / "rules" / "math-scripts.md"
    ),
    "cross-pillar-bridge-anatomy.md": (
        PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
    ),
    "phononic-framing.md": (
        PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"
    ),
}


def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    payload = "\n".join(f"{k}={v}" for k, v in sorted(input_pin_map.items())).encode()  # (local)
    return hashlib.sha256(payload).hexdigest()


# ----------------------------------------------------------------------------
# Pole aggregation conventions
# ----------------------------------------------------------------------------
def C_pole_Cbeta(casimirs, weyl_dims):
    """Cβ: unweighted median of Casimirs (W11-5 anchor convention)."""
    return float(np.median(casimirs))  # (local)


def C_pole_B(casimirs, weyl_dims):
    """B: multiplicity-weighted median of Casimirs (Weyl-dim weights)."""
    # Sort by Casimir, then find weighted-median (cumulative weight = total/2)
    order = np.argsort(casimirs)  # (local)
    sorted_C = casimirs[order]  # (local)
    sorted_w = weyl_dims[order]  # (local)
    cumw = np.cumsum(sorted_w)  # (local)
    half = cumw[-1] / 2.0  # (local)
    idx = int(np.searchsorted(cumw, half))  # (local)
    if idx >= len(sorted_C):
        idx = len(sorted_C) - 1  # (local)
    return float(sorted_C[idx])  # (local)


CONV_FUNCS = {"Cβ": C_pole_Cbeta, "B": C_pole_B}  # (local)


def compute_R_at_Lmax_conv(L_max, conv_name):
    """W11-5 multiplicity-weighted Mellin-pole-window observable at (L_max, conv)."""
    sectors = _enumerate_sectors(L_max)  # (local)
    casimirs = np.array([s[3] for s in sectors], dtype=np.float64)  # (local)
    weyl_dims = np.array([s[2] for s in sectors], dtype=np.float64)  # (local)
    C_pole = CONV_FUNCS[conv_name](casimirs, weyl_dims)  # (local)
    paired_mask = np.abs(casimirs - C_pole) / C_pole <= MELLIN_WINDOW_FRAC  # (local)
    unpaired_mask = ~paired_mask  # (local)
    N_paired = float(np.sum(weyl_dims[paired_mask]))  # (local)
    N_unpaired = float(np.sum(weyl_dims[unpaired_mask]))  # (local)
    delta_N = N_unpaired - 2.0 * N_paired  # (local)
    if N_paired == 0.0:
        R = float("nan")  # (local)
    else:
        R = delta_N / N_paired  # (local)
    rm_plan_metric = abs(R - R_3HeB_lit) / abs(R_3HeB_lit) if R_3HeB_lit != 0 else float("inf")  # (local)
    rm_W11_5_metric = abs(R - R_3HeB_lit) / max(abs(R), abs(R_3HeB_lit)) if max(abs(R), abs(R_3HeB_lit)) > 0 else float("inf")  # (local)
    return {  # (local)
        "L_max": L_max,
        "convention": conv_name,
        "n_sectors": len(sectors),
        "C_pole": C_pole,
        "N_paired": N_paired,
        "N_unpaired": N_unpaired,
        "delta_N": delta_N,
        "R": R,
        "ratio_mismatch_plan_metric": rm_plan_metric,
        "ratio_mismatch_W11_5_metric": rm_W11_5_metric,
    }


def main():
    # ------------------------------------------------------------------------
    # 1. Stamp input SHAs
    # ------------------------------------------------------------------------
    input_pin_map = {}  # (local)
    for name, p in INPUT_PINS_PATHS.items():
        if p.exists():
            input_pin_map[name] = sha256_of_file(p)
        else:
            input_pin_map[name] = "<missing>"

    print("=" * 80)
    print(f"GATE  : {GATE_ID}")
    print(f"SCHEME: {SCHEME}")
    print(f"L_max scan: {L_MAX_SCAN};  Conventions: {CONVENTIONS}  (Cα REJECTED)")
    print(f"tau_fold = {tau_fold}; M_KK = {M_KK:.6e}")
    print(f"R_3HeB_lit = {R_3HeB_lit:.6e}")
    print("INPUT PIN SHA-256 (truncated to 16 hex):")
    for k, v in sorted(input_pin_map.items()):
        print(f"  {k:50s} {v[:16]}")
    print("=" * 80)

    # ------------------------------------------------------------------------
    # 2. 4 × 2 grid scan
    # ------------------------------------------------------------------------
    grid = {}  # (local)  (L, conv) → result dict
    for L in L_MAX_SCAN:
        for conv in CONVENTIONS:
            r = compute_R_at_Lmax_conv(L, conv)
            grid[(L, conv)] = r

    # Display grid
    print(f"\n{'L_max':>6} {'conv':>4} {'n_sec':>6} {'C_pole':>10} {'N_paired':>10} {'N_unpaired':>11} {'δN':>10} {'R':>12} {'rm_plan':>10} {'rm_W11_5':>10}")
    print("-" * 100)
    for L in L_MAX_SCAN:
        for conv in CONVENTIONS:
            r = grid[(L, conv)]
            print(f"{L:>6} {conv:>4} {r['n_sectors']:>6} {r['C_pole']:>10.4f} "
                  f"{r['N_paired']:>10.0f} {r['N_unpaired']:>11.0f} {r['delta_N']:>10.0f} "
                  f"{r['R']:>+12.4e} {r['ratio_mismatch_plan_metric']:>10.4e} {r['ratio_mismatch_W11_5_metric']:>10.4e}")

    # ------------------------------------------------------------------------
    # 3. W11-5 anchor reproduction check at (L=10, Cβ)
    # ------------------------------------------------------------------------
    R_anchor_check = grid[(10, "Cβ")]["R"]  # (local)
    anchor_dev = abs(R_anchor_check - R_substrate_W11_5_anchor)  # (local)
    print(f"\nW11-5 anchor reproduction at (L=10, Cβ):")
    print(f"  W11-5 measured R_substrate = {R_substrate_W11_5_anchor:.6e}")
    print(f"  this run R(L=10, Cβ)       = {R_anchor_check:.6e}")
    print(f"  deviation                   = {anchor_dev:.4e}  ({'✓' if anchor_dev < 1e-4 else '✗'})")

    # ------------------------------------------------------------------------
    # 4. Saturation check per plan §"Step 4-5"
    #    saturated iff |rm(L=20) - rm(L=18)| < 0.05 · |rm(L=18)| AND same for L=18 vs L=16
    # ------------------------------------------------------------------------
    def saturated_for_conv(conv):
        rm_16 = grid[(16, conv)]["ratio_mismatch_plan_metric"]  # (local)
        rm_18 = grid[(18, conv)]["ratio_mismatch_plan_metric"]  # (local)
        rm_20 = grid[(20, conv)]["ratio_mismatch_plan_metric"]  # (local)
        step_18_to_20 = abs(rm_20 - rm_18) / abs(rm_18) if rm_18 != 0 else float("inf")  # (local)
        step_16_to_18 = abs(rm_18 - rm_16) / abs(rm_16) if rm_16 != 0 else float("inf")  # (local)
        sat = (step_18_to_20 < SATURATION_THRESH) and (step_16_to_18 < SATURATION_THRESH)  # (local)
        return sat, step_16_to_18, step_18_to_20

    sat_Cbeta, step_Cb_16_18, step_Cb_18_20 = saturated_for_conv("Cβ")
    sat_B,     step_B_16_18,  step_B_18_20  = saturated_for_conv("B")

    print(f"\nSaturation check (Step 4-5; threshold = {SATURATION_THRESH} relative cross-step variation):")
    print(f"  Cβ: step(16→18) = {step_Cb_16_18:.4e}; step(18→20) = {step_Cb_18_20:.4e}; saturated = {sat_Cbeta}")
    print(f"  B:  step(16→18) = {step_B_16_18:.4e};  step(18→20) = {step_B_18_20:.4e}; saturated = {sat_B}")

    # ------------------------------------------------------------------------
    # 5. Cross-convention check at L_max=20
    # ------------------------------------------------------------------------
    rm_20_Cb = grid[(20, "Cβ")]["ratio_mismatch_plan_metric"]  # (local)
    rm_20_B = grid[(20, "B")]["ratio_mismatch_plan_metric"]  # (local)
    if (rm_20_Cb + rm_20_B) > 0:
        cross_conv_dev = 2.0 * abs(rm_20_Cb - rm_20_B) / (rm_20_Cb + rm_20_B)  # (local)
    else:
        cross_conv_dev = float("inf")  # (local)
    print(f"\nCross-convention check at L_max=20:")
    print(f"  rm(20, Cβ) = {rm_20_Cb:.4e}; rm(20, B) = {rm_20_B:.4e}")
    print(f"  cross_conv_deviation = {cross_conv_dev:.4e}  (threshold = {CROSS_CONV_DEVIATION_THRESH})")
    cross_conv_unstable = cross_conv_dev >= CROSS_CONV_DEVIATION_THRESH  # (local)

    # ------------------------------------------------------------------------
    # 6. Verdict per plan §"PASS / FAIL / INFO thresholds"
    # ------------------------------------------------------------------------
    rm_20_Cb_pass = rm_20_Cb <= PASS_THRESH  # (local)
    rm_20_B_pass = rm_20_B <= PASS_THRESH  # (local)

    if sat_Cbeta and sat_B and rm_20_Cb_pass and rm_20_B_pass and not cross_conv_unstable:
        verdict = "PASS"  # (local)
        verdict_label = "PASS"  # (local)
    elif cross_conv_unstable:
        verdict = "INFO"  # (local)
        verdict_label = "INFO-cross-conv-unstable"  # (local)
    elif sat_Cbeta and sat_B:
        # Saturation holds but ratio_mismatch > 0.05 at L_max=20 → INFO-saturated-FAIL
        verdict = "INFO"  # (local)
        verdict_label = "INFO-saturated-FAIL"  # (local)
    else:
        verdict = "FAIL"  # (local) NOT saturated at one or both conv
        verdict_label = "FAIL"  # (local)

    # 3-tuple per gate-verdicts.md S87+ schema-v2
    sign_R_lit = +1 if R_3HeB_lit > 0 else (-1 if R_3HeB_lit < 0 else 0)  # (local)
    sign_R_pred_Cb = +1 if grid[(20, "Cβ")]["R"] > 0 else (-1 if grid[(20, "Cβ")]["R"] < 0 else 0)  # (local)
    sign_match = (sign_R_pred_Cb == sign_R_lit)  # (local)
    sign_verdict = "PASS" if sign_match else "FAIL"  # (local)
    if rm_20_Cb_pass:
        magnitude_verdict = "PASS"  # (local)
    elif rm_20_Cb <= 0.25:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    regime_verdict = "VALID"  # (local) closed-form sector enumeration; no truncation breakdown

    print(f"\nVERDICT (composite): {verdict}  ({verdict_label})")
    print(f"  saturation_Cβ      = {sat_Cbeta}")
    print(f"  saturation_B       = {sat_B}")
    print(f"  rm(20, Cβ) ≤ {PASS_THRESH}  : {rm_20_Cb_pass}")
    print(f"  rm(20, B)  ≤ {PASS_THRESH}  : {rm_20_B_pass}")
    print(f"  cross_conv_unstable = {cross_conv_unstable}")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")

    # ------------------------------------------------------------------------
    # 7. Closure SHAs
    # ------------------------------------------------------------------------
    pinmap_for_audit = dict(input_pin_map)  # (local)
    pinmap_for_audit["_gate_id"] = GATE_ID
    pinmap_for_audit["_scheme"] = SCHEME
    pinmap_for_audit["_convention"] = "+".join(CONVENTIONS)
    pinmap_for_audit["_L_max_scan"] = "+".join(str(L) for L in L_MAX_SCAN)
    pinmap_for_audit["_mellin_window_frac"] = str(MELLIN_WINDOW_FRAC)
    pinmap_for_audit["_friedrich_baer_lower"] = str(FRIEDRICH_BAER_LOWER)
    pinmap_for_audit["_friedrich_baer_used"] = "False"  # (local) FB not invoked
    audit_sha = closure_hash(pinmap_for_audit)  # (local)

    content_payload = {  # (local)
        "value": rm_20_Cb,  # primary verdict-line value at (L=20, Cβ) plan metric
        "scheme": SCHEME,
        "convention_used": "Cβ-and-B",
        "L_max": 20,
        "schema_version": SCHEMA_VERSION,
        "verdict": verdict,
        "verdict_label": verdict_label,
        "saturation_Cbeta": sat_Cbeta,
        "saturation_B": sat_B,
        "cross_conv_deviation_at_Lmax20": cross_conv_dev,
        "cross_conv_unstable": cross_conv_unstable,
        "rm_20_Cbeta": rm_20_Cb,
        "rm_20_B": rm_20_B,
        "rm_18_Cbeta": grid[(18, "Cβ")]["ratio_mismatch_plan_metric"],
        "rm_18_B": grid[(18, "B")]["ratio_mismatch_plan_metric"],
        "rm_16_Cbeta": grid[(16, "Cβ")]["ratio_mismatch_plan_metric"],
        "rm_16_B": grid[(16, "B")]["ratio_mismatch_plan_metric"],
        "rm_10_Cbeta": grid[(10, "Cβ")]["ratio_mismatch_plan_metric"],
        "rm_10_B": grid[(10, "B")]["ratio_mismatch_plan_metric"],
        "R_anchor_check_dev": anchor_dev,
        "friedrich_baer_used": False,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    content_sha = hashlib.sha256(
        json.dumps(content_payload, sort_keys=True, default=str).encode()
    ).hexdigest()  # (local)

    # ------------------------------------------------------------------------
    # 8. Save .npz + .png artifacts
    # ------------------------------------------------------------------------
    npz_path = HERE / "s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.npz"  # (local)
    # Build grids for npz output
    R_grid = np.array([[grid[(L, conv)]["R"] for conv in CONVENTIONS] for L in L_MAX_SCAN])  # (local) shape (4, 2)
    rm_plan_grid = np.array([[grid[(L, conv)]["ratio_mismatch_plan_metric"] for conv in CONVENTIONS] for L in L_MAX_SCAN])  # (local)
    rm_W11_5_grid = np.array([[grid[(L, conv)]["ratio_mismatch_W11_5_metric"] for conv in CONVENTIONS] for L in L_MAX_SCAN])  # (local)
    Cpole_grid = np.array([[grid[(L, conv)]["C_pole"] for conv in CONVENTIONS] for L in L_MAX_SCAN])  # (local)
    np.savez(
        npz_path,
        L_max_scan=np.array(L_MAX_SCAN, dtype=np.int64),
        conv_scan=np.array(CONVENTIONS),
        R_grid=R_grid,
        ratio_mismatch_plan_grid=rm_plan_grid,
        ratio_mismatch_W11_5_grid=rm_W11_5_grid,
        C_pole_grid=Cpole_grid,
        saturation_Cbeta=np.array(sat_Cbeta),
        saturation_B=np.array(sat_B),
        cross_conv_deviation_at_Lmax20=np.float64(cross_conv_dev),
        friedrich_baer_used=np.array(False),
        friedrich_baer_lower=np.float64(FRIEDRICH_BAER_LOWER),
        R_substrate_W11_5_anchor=np.float64(R_substrate_W11_5_anchor),
        ratio_mismatch_W11_5_anchor=np.float64(ratio_mismatch_W11_5_anchor),
        R_anchor_check_dev=np.float64(anchor_dev),
        R_3HeB_lit=np.float64(R_3HeB_lit),
        verdict=np.array(verdict),
        verdict_label=np.array(verdict_label),
        sign_verdict=np.array(sign_verdict),
        magnitude_verdict=np.array(magnitude_verdict),
        regime_verdict=np.array(regime_verdict),
        audit_sha=np.array(audit_sha),
        content_sha=np.array(content_sha),
    )
    print(f"\nSaved data: {npz_path.name}")

    # 3-panel plot
    fig, axes = plt.subplots(3, 1, figsize=(10, 13))

    # Panel 1: ratio_mismatch vs L_max for both conventions, with Level-3 thresholds
    ax = axes[0]
    Ls = np.array(L_MAX_SCAN)  # (local)
    rm_Cb = np.array([grid[(L, "Cβ")]["ratio_mismatch_plan_metric"] for L in L_MAX_SCAN])  # (local)
    rm_B = np.array([grid[(L, "B")]["ratio_mismatch_plan_metric"] for L in L_MAX_SCAN])  # (local)
    ax.plot(Ls, rm_Cb, marker="o", color="#2a6fdb", linewidth=2, label=f"Cβ unweighted-median (saturated={sat_Cbeta})")
    ax.plot(Ls, rm_B, marker="s", color="#dd6b3a", linewidth=2, label=f"B multiplicity-weighted-median (saturated={sat_B})")
    ax.axhline(PASS_THRESH, color="green", linestyle="--", linewidth=1.5, label=f"PASS ≤ {PASS_THRESH}")
    ax.axhline(0.001, color="darkgreen", linestyle=":", linewidth=1.5, label=f"Level-3 strict ≤ 0.001")
    ax.set_xlabel("L_max")
    ax.set_ylabel("ratio_mismatch (plan metric: |R - R_lit| / |R_lit|)")
    ax.set_yscale("log")
    ax.set_title("S88 §W3a-19 — L_max scan ratio_mismatch (plan metric)")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3, which="both")

    # Panel 2: R_substrate convergence to R_3HeB_lit anchor
    ax = axes[1]
    R_Cb = np.array([grid[(L, "Cβ")]["R"] for L in L_MAX_SCAN])  # (local)
    R_B = np.array([grid[(L, "B")]["R"] for L in L_MAX_SCAN])  # (local)
    ax.plot(Ls, R_Cb, marker="o", color="#2a6fdb", linewidth=2, label="R(L, Cβ)")
    ax.plot(Ls, R_B,  marker="s", color="#dd6b3a", linewidth=2, label="R(L, B)")
    ax.axhline(R_3HeB_lit, color="#2a8c4a", linestyle="--", linewidth=2, label=f"R_3HeB_lit = {R_3HeB_lit:+.4e}")
    ax.axhline(R_substrate_W11_5_anchor, color="#aa2222", linestyle=":", linewidth=1.5, label=f"W11-5 anchor R = {R_substrate_W11_5_anchor:+.4e}")
    ax.axhline(0, color="black", linewidth=0.5)
    ax.set_xlabel("L_max")
    ax.set_ylabel("R_substrate")
    ax.set_title("R_substrate convergence vs L_max under Cβ + B conventions")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: cross-convention deviation vs L_max
    ax = axes[2]
    cross_devs = []  # (local)
    for L in L_MAX_SCAN:
        rm_Cb_L = grid[(L, "Cβ")]["ratio_mismatch_plan_metric"]
        rm_B_L = grid[(L, "B")]["ratio_mismatch_plan_metric"]
        if (rm_Cb_L + rm_B_L) > 0:
            cross_devs.append(2.0 * abs(rm_Cb_L - rm_B_L) / (rm_Cb_L + rm_B_L))
        else:
            cross_devs.append(float("nan"))
    ax.plot(Ls, cross_devs, marker="^", color="#888822", linewidth=2)
    ax.axhline(CROSS_CONV_DEVIATION_THRESH, color="red", linestyle="--", linewidth=1.5,
               label=f"unstable threshold ≥ {CROSS_CONV_DEVIATION_THRESH}")
    ax.set_xlabel("L_max")
    ax.set_ylabel("cross_conv_deviation = 2|rm_Cβ - rm_B| / (rm_Cβ + rm_B)")
    ax.set_title(f"§W3a-19 verdict = {verdict_label}")
    ax.legend(loc="best", fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    png_path = HERE / "s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.png"  # (local)
    fig.savefig(png_path, dpi=110)
    plt.close(fig)
    print(f"Saved plot: {png_path.name}")

    # ------------------------------------------------------------------------
    # 9. Append verdict line + dual-SHA + 3-tuple to s88_gate_verdicts.txt
    # ------------------------------------------------------------------------
    verdict_path = HERE / "s88_gate_verdicts.txt"  # (local)
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={rm_20_Cb:.6e} "
        f"scheme={SCHEME} convention=Cbeta-and-B-grid L_max=20 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}"
    )  # (local)
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); verdict_label={verdict_label}"
    )  # (local)
    tuple_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )  # (local)
    with open(verdict_path, "a", encoding="utf-8") as fh:
        fh.write(canonical_line + "\n")
        fh.write(companion_line + "\n")
        fh.write(tuple_line + "\n")
    print(f"\nVerdict appended to: {verdict_path.name}")
    print(f"  CANONICAL:  {canonical_line[:140]}...")
    print(f"  COMPANION:  {companion_line}")
    print(f"  3-TUPLE:    {tuple_line}")

    print(
        f"\n4-TUPLE: (value={rm_20_Cb:.6e}, scheme={SCHEME}, "
        f"convention=Cbeta-and-B-grid, L_max=20)  verdict={verdict_label}"
    )

    return verdict


if __name__ == "__main__":
    v = main()
    sys.exit(0)
