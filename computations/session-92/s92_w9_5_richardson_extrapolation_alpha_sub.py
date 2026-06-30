#!/usr/bin/env python3
"""
S92 W9-5: S92-W9-CF-W6-3-NEXT-1-RICHARDSON-EXTRAPOLATION-ALPHA-SUB
==================================================================

Gate: S92-W9-CF-W6-3-NEXT-1-RICHARDSON-EXTRAPOLATION-ALPHA-SUB  ([VERIFY]+[SIGN])

Post-hoc analysis on EXISTING S90 W8 FWD-C1 L_max-scan npz
(`computations/session-90/s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz`
— the SAME file consumed by S91 W6-3). No new spectrum compute.

PURPOSE (plan §W9-5): extend the S91 W6-3 sub-window regression (L in {6..9},
alpha_sub = 2.4291, R2 = 0.9074) to L in {6..10} (5-pt), {6..11} (6-pt),
{6..12} (7-pt), then Richardson-extrapolate alpha_inf from the sequence
{alpha_sub(9), alpha_sub(10), alpha_sub(11), alpha_sub(12)} to discriminate:
  PASS-A (Reading A pre-asymptotic steepening):  alpha_inf > 2.7 AND
                                                 R2(6-or-7-pt) >= 0.95 AND
                                                 |Delta alpha_inf| -> 0
  INFO  (intermediate / hybrid):                 alpha_inf in [2.3, 2.7]
  FAIL-Reading-B (persistent finite-L truncation): alpha_inf <= 2.0

SUBSTRATE-IS STRUCTURE (read directly from npz, NOT hardcoded):
  delta_n_s(L) = | n_s_recomputed(L) - n_s_FW_exact |   (npz: delta_n_s_per_L)
  with n_s_FW_exact = 0.9561 (npz: n_s_FW_exact_float; the L -> infinity
  continuum anchor). The substrate-IS finding (confirmed at runtime) is that
  delta_n_s descends to EXACTLY 0 at L=10 (n_s_recomputed(L=10) hits the
  anchor) and RE-ASCENDS for L>10. log(delta_n_s) is therefore -infinity at
  L=10, and the |delta_n_s| magnitude over [6,12] is NOT a single power-law
  decay: the post-anchor re-ascent is the "c_sub_corrected M_Pl_eff^2
  anti-symmetry artifact" the S91 plan already named (W8 WP §W8-7(l)).

  Consequence: the sub-window alpha_sub DECREASES as the window grows past
  the L=10 zero-crossing (2.43 -> 1.93 -> 0.88), the OPPOSITE of Reading A
  pre-asymptotic steepening. The Richardson sequence is divergent (error-step
  ratio > 1), so no convergent Richardson limit toward the Reading-A
  asymptote alpha=3 exists.

SUBSTRATE FRAMING (MANDATORY, plan §substrate_framing):
  The substrate IS the L_max-truncated spectral triple at L_max in {6..12};
  alpha_sub IS the substrate-IS Mellin-cone asymptotic exponent at
  substrate-distance-1 pole s=3 evaluated on the sub-window {L : L <= L_max};
  Richardson alpha_inf IS the substrate-IS asymptotic-limit predictor for
  L -> infinity. Container-thinking FORBIDDEN: "the cache is too short to see
  the asymptote." INVERTED reading: the substrate's sub-window alpha_sub IS a
  finite-L substrate-IS observable; Richardson alpha_inf IS the substrate's
  own asymptotic predictor; the n_s_FW curve crossing the continuum anchor at
  L=10 IS a substrate-IS structural fact about the FWD-C1 trajectory, not an
  artifact of a too-small enveloping container.

Sage-Q exact rational cross-check of all regressions + the Richardson
arithmetic per math-scripts.md §"Mnemonic-vs-exact ratio discipline" RULE-3.

GPU path: cpu-cap-OMP8 (small data; CPU-only) per plan §machinery_pin_map.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    kappa_2_substrate_FW,
    tau_fold,
    M_KK_gravity,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ============================ Gate-block constants ============================
GATE_ID = "S92-W9-CF-W6-3-NEXT-1-RICHARDSON-EXTRAPOLATION-ALPHA-SUB"
SCHEME = ("richardson-extrapolation-against-asymptotic-alpha-3-"
          "substrate-distance-1-pole-s3-FULL")
CONVENTION = ("lizzi-W6-3-NEXT-1-richardson-3-window-regression-"
              "CPU-only-post-hoc")
L_MAX_TAG = 12  # (local) — operational L_max output tag (consumes FWD-C1 npz at L<=12)

# Pre-registered band thresholds (plan §operator / §machinery_pin_map.tolerance)
ALPHA_PASS_A = 2.7       # (local) — alpha_inf > 2.7 -> PASS-A (Reading A)
ALPHA_INFO_LO = 2.3      # (local) — alpha_inf in [2.3, 2.7] -> INFO
ALPHA_FAIL_B = 2.0       # (local) — alpha_inf <= 2.0 -> FAIL-Reading-B
R2_FLOOR = 0.95          # (local) — R^2 goodness-of-fit floor for PASS-A
ALPHA_READING_A = 3.0    # (local) — Reading A substrate-IS asymptotic exponent
ALPHA_READING_B = 1.929  # (local) — Reading B persistent finite-L exponent (CF-65 anchor)

PROJECT_ROOT = ROOT
SHARED_DIR = ROOT / "computations" / "_shared"
SESSION_92_DIR = ROOT / "computations" / "session-92"
SESSION_90_DIR = ROOT / "computations" / "session-90"
SESSION_91_DIR = ROOT / "computations" / "session-91"
VERDICT_TXT = SESSION_92_DIR / "s92_gate_verdicts.txt"
OUT_NPZ = SESSION_92_DIR / "s92_w9_5_richardson_extrapolation_alpha_sub.npz"
OUT_PNG = SESSION_92_DIR / "s92_w9_5_richardson_extrapolation_alpha_sub.png"

FWD_C1_NPZ = (SESSION_90_DIR
              / "s90_w8_fwd_c1_lmax_scan_parameterized_slope_a_canonical.npz")

# Pinned input files (per plan §input_files)
INPUT_FILES = [
    FWD_C1_NPZ,
    SHARED_DIR / "canonical_constants.py",
    ROOT / "sessions" / "session-91" / "session-91-w6-workingpaper.md",
]


# ============================ SHA helpers ============================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """audit_sha = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha = SHA(script_bytes)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = canonical_path.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


# ============================ Section 5a — log-log regression (numpy) ============================
def regress_loglog_np(L_window: np.ndarray, delta_window: np.ndarray) -> dict:
    """Log-log linear regression alpha_sub = -slope on the POSITIVE-delta
    subset of {(L, delta_n_s(L)) : L in window}.

    delta_n_s == 0 (exact anchor crossing at L=10) has log(delta) = -inf and
    carries NO finite log-magnitude information; it is EXCLUDED from the fit
    with explicit accounting (n_used vs n_window). This exclusion is honest:
    the substrate-IS observable delta_n_s IS exactly 0 at L=10 (the FWD-C1
    n_s curve hits the continuum anchor); a zero magnitude is not a power-law
    sample point. Whether L>=10 (post-anchor RE-ASCENT) points are kept is
    governed by the window itself; their inclusion is what drives alpha_sub
    DOWN as the window grows (the post-anchor anti-symmetry artifact).
    """
    mask = delta_window > 0.0                                          # (local)
    Lk = L_window[mask].astype(np.float64)                            # (local)
    dk = delta_window[mask].astype(np.float64)                        # (local)
    n_used = int(mask.sum())                                          # (local)
    n_window = int(len(L_window))                                     # (local)
    if n_used < 2:
        return {"alpha_sub": float("nan"), "r_squared": float("nan"),
                "slope": float("nan"), "intercept": float("nan"),
                "n_used": n_used, "n_window": n_window,
                "L_used": Lk, "delta_used": dk}
    x = np.log(Lk)                                                    # (local)
    y = np.log(dk)                                                    # (local)
    slope, intercept = np.polyfit(x, y, 1)
    yhat = slope * x + intercept                                      # (local)
    ss_res = float(np.sum((y - yhat) ** 2))                          # (local)
    ss_tot = float(np.sum((y - y.mean()) ** 2))                      # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")       # (local)
    return {"alpha_sub": -float(slope), "r_squared": r2,
            "slope": float(slope), "intercept": float(intercept),
            "n_used": n_used, "n_window": n_window,
            "L_used": Lk, "delta_used": dk}


# ============================ Section 5b — log-log regression (Sage-Q exact) ============================
def regress_loglog_QQ(L_window: list, delta_window: list
                      ) -> tuple[Fraction, Fraction, int]:
    """Exact rational log-log regression on float64-quantized logs.
    Mnemonic-vs-exact discipline cross-check (RULE-3). Returns
    (alpha_sub_Q, r_sq_Q, n_used). Zeros excluded (log undefined)."""
    pts = [(L, d) for L, d in zip(L_window, delta_window) if d > 0.0]  # (local)
    n_used = len(pts)                                                  # (local)
    if n_used < 2:
        return Fraction(0), Fraction(0), n_used
    xs = [Fraction.from_float(math.log(float(L))) for (L, _) in pts]  # (local)
    ys = [Fraction.from_float(math.log(float(d))) for (_, d) in pts]  # (local)
    n_Q = Fraction(n_used)                                            # (local)
    sx = sum(xs, Fraction(0)); sy = sum(ys, Fraction(0))              # (local)
    sxy = sum((x * y for x, y in zip(xs, ys)), Fraction(0))           # (local)
    sxx = sum((x * x for x in xs), Fraction(0))                       # (local)
    denom = n_Q * sxx - sx * sx                                       # (local)
    slope_Q = (n_Q * sxy - sx * sy) / denom                           # (local)
    icpt_Q = (sy - slope_Q * sx) / n_Q                                # (local)
    mean_y = sy / n_Q                                                 # (local)
    ss_res = sum(((y - (slope_Q * x + icpt_Q)) ** 2
                  for x, y in zip(xs, ys)), Fraction(0))              # (local)
    ss_tot = sum(((y - mean_y) ** 2 for y in ys), Fraction(0))        # (local)
    r_sq_Q = Fraction(1) - ss_res / ss_tot if ss_tot != 0 else Fraction(0)  # (local)
    return -slope_Q, r_sq_Q, n_used


# ============================ Section 5c — Richardson / Aitken extrapolation ============================
def richardson(alpha_L: float, alpha_Lm1: float, r: float) -> float:
    """Plan §substitution_chain Def 4 Richardson extrapolation:

        alpha_inf ~ alpha(L) + (alpha(L) - alpha(L-1)) / (r^{-1} - 1)

    where r is the truncation-error decay ratio (assumed power-law in 1/L).
    For a CONVERGENT power-law error model with step DL=1 at the largest pair
    (L, L-1), r = ((L-1)/L)^p (p the power-law exponent). A convergent sequence
    has 0 < r < 1; the (r^{-1} - 1) > 0 denominator then accelerates toward the
    limit. This function is purely arithmetic; convergence is a PROPERTY OF THE
    INPUT SEQUENCE, diagnosed separately by `richardson_convergence_diagnostic`.
    """
    if not (r > 0.0) or abs(1.0 / r - 1.0) < 1e-30:
        return float("nan")
    return alpha_L + (alpha_L - alpha_Lm1) / (1.0 / r - 1.0)


def aitken_delta2(s0: float, s1: float, s2: float) -> float:
    """Aitken Delta^2 accelerator (assumption-free Richardson for sequences
    with geometric error). s_inf ~ s2 - (s2-s1)^2 / (s2 - 2 s1 + s0).
    Returns NaN if the second difference vanishes (no acceleration possible).

    NOTE: Aitken is only meaningful for a sequence that is actually converging
    geometrically. On a DIVERGENT sequence (growing step magnitude), the Aitken
    value is a numerical artifact with no physical meaning; the convergence
    diagnostic flags this case explicitly.
    """
    denom = s2 - 2.0 * s1 + s0                                        # (local)
    if abs(denom) < 1e-30:
        return float("nan")
    return s2 - (s2 - s1) ** 2 / denom


def richardson_convergence_diagnostic(seq: list[float]) -> dict:
    """Diagnose whether the alpha_sub sequence is CONVERGING (admits a
    Richardson limit) or DIVERGING (no convergent limit exists).

    A power-law-decaying error sequence has |alpha(L) - alpha(L-1)| DECREASING
    geometrically: the step ratio |d_{k+1}/d_k| < 1. A step ratio >= 1 means
    the error is GROWING -> the sequence does NOT converge to the asymptote, and
    any Richardson/Aitken extrapolation is ill-conditioned (the discriminating
    signal IS the non-convergence).
    """
    diffs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]        # (local)
    # step ratios over consecutive NON-ZERO diffs
    ratios = []                                                       # (local)
    for i in range(len(diffs) - 1):
        if abs(diffs[i]) > 1e-30:
            ratios.append(diffs[i + 1] / diffs[i])
    last_ratio = ratios[-1] if ratios else float("nan")              # (local)
    converging = (abs(last_ratio) < 1.0) if ratios else False        # (local)
    return {"diffs": diffs, "step_ratios": ratios,
            "last_step_ratio": last_ratio, "converging": bool(converging)}


# ============================ Section 6 — Compute ============================
def compute() -> dict:
    # ------------------------------------------------------------------
    # Step 0: load EXISTING S90 W8 FWD-C1 npz; read delta_n_s directly
    # (substrate-first sourcing — NOT hardcoded). n_s_FW_exact_float is the
    # L -> infinity continuum anchor; delta_n_s_per_L = |n_s_recomp - anchor|.
    # ------------------------------------------------------------------
    npz = np.load(FWD_C1_NPZ, allow_pickle=True)
    L_all = npz["L_max_range"].astype(np.int64)                      # (local) [6..12]
    delta_all = npz["delta_n_s_per_L"].astype(np.float64)            # (local)
    n_s_FW_exact = float(npz["n_s_FW_exact_float"])                  # (local) 0.9561 anchor
    n_s_recomp = npz["n_s_recomputed_per_L"].astype(np.float64)      # (local)
    tau_fold_npz = float(npz["tau_fold"])                            # (local)
    mellin_s = int(npz["mellin_s"])                                  # (local) substrate-distance-1 pole s=3
    fwd_c1_audit = str(npz["audit_sha256"])                          # (local)

    print(f"FWD-C1 npz L_max_range:     {list(L_all)}")
    print(f"FWD-C1 npz delta_n_s_per_L: {list(np.round(delta_all, 8))}")
    print(f"FWD-C1 npz n_s_FW_exact:    {n_s_FW_exact}")
    print(f"FWD-C1 npz n_s_recomp:      {list(np.round(n_s_recomp, 6))}")
    print(f"FWD-C1 npz mellin_s:        {mellin_s}  (substrate-distance-1 pole)")
    print(f"FWD-C1 npz tau_fold:        {tau_fold_npz}  "
          f"(canonical tau_fold={tau_fold})")

    # Sanity: tau_fold consistency (substrate-IS, single-tau-slice level)
    tau_consistent = abs(tau_fold_npz - float(tau_fold)) < 1e-9      # (local)

    # Structural fact: locate the anchor zero-crossing (delta == 0)
    zero_idx = np.where(delta_all == 0.0)[0]                          # (local)
    anchor_crossing_L = int(L_all[zero_idx[0]]) if len(zero_idx) else None  # (local)
    print(f"\nSUBSTRATE-IS structural fact: delta_n_s == 0 (anchor crossing) "
          f"at L={anchor_crossing_L} (n_s_recomp hits continuum anchor).")
    # post-anchor re-ascent check
    post_anchor_reascent = (anchor_crossing_L is not None
                            and anchor_crossing_L < int(L_all.max())
                            and delta_all[zero_idx[0] + 1] > 0.0)    # (local)
    print(f"Post-anchor RE-ASCENT (delta increases for L > {anchor_crossing_L}): "
          f"{post_anchor_reascent}")

    # ------------------------------------------------------------------
    # Step 1+2: sub-window regressions L in {6..10}, {6..11}, {6..12}
    # plus the S91 baseline {6..9} for the Richardson sequence anchor.
    # ------------------------------------------------------------------
    windows = [9, 10, 11, 12]                                        # (local) hi-edges
    reg = {}                                                         # (local)
    reg_QQ = {}                                                      # (local)
    for hi in windows:
        sel = L_all <= hi                                            # (local)
        Lw = L_all[sel]; dw = delta_all[sel]                        # (local)
        r_np = regress_loglog_np(Lw, dw)
        a_Q, r2_Q, nused_Q = regress_loglog_QQ(Lw.tolist(), dw.tolist())
        reg[hi] = r_np
        reg_QQ[hi] = {"alpha_sub_Q": float(a_Q), "r_squared_Q": float(r2_Q),
                      "n_used_Q": nused_Q}
        print(f"  window L in 6..{hi:>2}: alpha_sub={r_np['alpha_sub']:.6f} "
              f"R2={r_np['r_squared']:.6f} (np)  |  "
              f"alpha_sub_Q={float(a_Q):.6f} R2_Q={float(r2_Q):.6f} (Sage-Q)  "
              f"pts_used={r_np['n_used']}/{r_np['n_window']}")

    # Machine-epsilon cross-check Sage-Q vs numpy (per window)
    max_alpha_dev = 0.0                                              # (local)
    max_r2_dev = 0.0                                                 # (local)
    for hi in windows:
        ad = abs(reg_QQ[hi]["alpha_sub_Q"] - reg[hi]["alpha_sub"])  # (local)
        rd = abs(reg_QQ[hi]["r_squared_Q"] - reg[hi]["r_squared"])  # (local)
        max_alpha_dev = max(max_alpha_dev, ad)
        max_r2_dev = max(max_r2_dev, rd)
    sageQ_numpy_machine_eps = (max_alpha_dev < 1e-12
                               and max_r2_dev < 1e-12)              # (local)
    print(f"\nSage-Q vs numpy max deviation: |Dalpha|={max_alpha_dev:.3e} "
          f"|DR2|={max_r2_dev:.3e}  machine_eps={sageQ_numpy_machine_eps}")

    # ------------------------------------------------------------------
    # Step 3: Richardson extrapolation on {alpha_sub(9..12)}
    # ------------------------------------------------------------------
    alpha_seq = [reg[9]["alpha_sub"], reg[10]["alpha_sub"],
                 reg[11]["alpha_sub"], reg[12]["alpha_sub"]]         # (local)
    print(f"\nRichardson alpha_sub sequence (L=9,10,11,12): "
          f"{[round(a, 4) for a in alpha_seq]}")

    conv = richardson_convergence_diagnostic(alpha_seq)
    print(f"  consecutive diffs:   {[round(d, 6) for d in conv['diffs']]}")
    print(f"  step ratios:         {[round(r, 6) for r in conv['step_ratios']]}")
    print(f"  last step ratio:     {conv['last_step_ratio']:.6f}  "
          f"(>=1 => DIVERGENT / error growing)")
    print(f"  converging:          {conv['converging']}")

    # Canonical Richardson alpha_inf: standard 1/L^p power-law decay ratio
    # at the most-converged pair (L=12, L=11): r = ((L-1)/L)^p with p=1
    # (CM-1995 §III.4 leading L^{-3} finite-L correction -> p=1 in the
    # subleading-coefficient expansion of the log-log slope).
    a12 = alpha_seq[3]; a11 = alpha_seq[2]                           # (local)
    r_powerlaw = ((12.0 - 1.0) / 12.0) ** 1.0                       # (local) = 11/12
    alpha_inf = richardson(a12, a11, r_powerlaw)                    # (local) CANONICAL alpha_inf
    print(f"\nCANONICAL Richardson alpha_inf "
          f"(r=(L-1)/L=11/12, p=1 power-law): {alpha_inf:.6f}")

    # Sensitivity band: alternative r conventions + Aitken Delta^2
    a_inf_r_half = richardson(a12, a11, 0.5)                        # (local)
    a_inf_r_quarter = richardson(a12, a11, 0.25)                    # (local)
    aitken_top = aitken_delta2(alpha_seq[1], alpha_seq[2], alpha_seq[3])  # (local) {a10,a11,a12}
    aitken_low = aitken_delta2(alpha_seq[0], alpha_seq[1], alpha_seq[2])  # (local) {a9,a10,a11}
    print(f"  sensitivity: r=1/2 -> {a_inf_r_half:.4f}; "
          f"r=1/4 -> {a_inf_r_quarter:.4f}; "
          f"Aitken{{a10,a11,a12}} -> {aitken_top:.4f}; "
          f"Aitken{{a9,a10,a11}} -> {aitken_low:.4f}")
    band_vals = [v for v in [alpha_inf, a_inf_r_half, a_inf_r_quarter,
                             aitken_top, aitken_low]
                 if not math.isnan(v)]                              # (local)
    alpha_inf_band_max = max(band_vals)                             # (local)
    alpha_inf_band_min = min(band_vals)                            # (local)
    print(f"  alpha_inf sensitivity band: [{alpha_inf_band_min:.4f}, "
          f"{alpha_inf_band_max:.4f}]")

    # |Delta alpha_inf| -> 0 test: the consecutive-window step magnitudes.
    # PASS-A requires these to SHRINK toward 0 (convergence). Here they GROW.
    delta_alpha_shrinking = (abs(conv["diffs"][2]) < abs(conv["diffs"][1])
                             if len(conv["diffs"]) >= 3 else False)  # (local)
    print(f"  |Delta alpha_sub| shrinking (|d12| < |d11|)? "
          f"{delta_alpha_shrinking}  "
          f"(|d11|={abs(conv['diffs'][1]):.4f}, "
          f"|d12|={abs(conv['diffs'][2]):.4f})")

    # ------------------------------------------------------------------
    # R^2 on the 6-point and 7-point fits (PASS-A goodness-of-fit gate)
    # ------------------------------------------------------------------
    r2_6pt = reg[11]["r_squared"]                                   # (local) L in {6..11}
    r2_7pt = reg[12]["r_squared"]                                   # (local) L in {6..12}
    r2_best_6or7 = max(r2_6pt, r2_7pt)                              # (local)
    print(f"\nR2(6-pt, L in 6..11) = {r2_6pt:.4f}; "
          f"R2(7-pt, L in 6..12) = {r2_7pt:.4f}; "
          f"best = {r2_best_6or7:.4f} (floor {R2_FLOOR})")

    # ------------------------------------------------------------------
    # Step 5: verdict per PASS-A-Richardson rubric (plan §operator)
    # ------------------------------------------------------------------
    pass_a = (alpha_inf > ALPHA_PASS_A
              and r2_best_6or7 >= R2_FLOOR
              and delta_alpha_shrinking)                            # (local)
    if pass_a:
        verdict = "PASS"
        band_tag = "PASS_A_Richardson"
    elif ALPHA_INFO_LO <= alpha_inf <= ALPHA_PASS_A:
        verdict = "INFO"
        band_tag = "INFO_intermediate_band"
    elif alpha_inf <= ALPHA_FAIL_B:
        verdict = "FAIL"
        band_tag = "FAIL_Reading_B_persistent"
    else:
        # alpha_inf in (2.0, 2.3): below INFO band lower edge but above FAIL-B
        # ceiling -> treat as INFO-adjacent (intermediate); pre-registered
        # rubric has no band here, default to INFO with explicit tag.
        verdict = "INFO"
        band_tag = "INFO_below_2p3_above_2p0"

    # ------------------------------------------------------------------
    # 3-tuple companion (S87 schema-v2) — [SIGN] trigger
    # SIGN: direction of Richardson alpha_inf — toward Reading A (alpha=3) is
    # PASS direction; toward Reading B (alpha=1.929) / below is FAIL direction.
    # The pre-registered PASS direction is "alpha_sub INCREASES toward 3 as the
    # window grows". Computed: alpha_sub DECREASES (2.43 -> 1.93 -> 0.88) and
    # alpha_inf lands far below 1.929. => direction MISMATCH => sign FAIL.
    # ------------------------------------------------------------------
    # distance of alpha_inf to each reading
    dist_to_A = abs(alpha_inf - ALPHA_READING_A)                    # (local)
    dist_to_B = abs(alpha_inf - ALPHA_READING_B)                    # (local)
    toward_reading_A = dist_to_A < dist_to_B                        # (local)
    sign_v = "PASS" if toward_reading_A else "FAIL"                 # (local)
    # magnitude vs Reading A target alpha=3
    mag_v = ("PASS" if dist_to_A < 0.5
             else "INFO" if dist_to_A < 1.0
             else "FAIL")                                          # (local)
    # regime: the Richardson extrapolation regime of validity requires a
    # CONVERGENT input sequence; a divergent sequence (step ratio>=1) is
    # OUT OF the power-law-convergence regime -> BREAKDOWN.
    regime_v = "VALID" if conv["converging"] else "BREAKDOWN"       # (local)

    return {
        # inputs (substrate-first, from npz)
        "L_all": L_all, "delta_all": delta_all,
        "n_s_FW_exact": n_s_FW_exact, "n_s_recomp": n_s_recomp,
        "mellin_s": mellin_s, "tau_fold_npz": tau_fold_npz,
        "tau_consistent": tau_consistent,
        "fwd_c1_audit_sha": fwd_c1_audit,
        "anchor_crossing_L": anchor_crossing_L,
        "post_anchor_reascent": post_anchor_reascent,
        # per-window regression
        "reg": reg, "reg_QQ": reg_QQ,
        "alpha_seq": alpha_seq,
        "alpha_sub_9": alpha_seq[0], "alpha_sub_10": alpha_seq[1],
        "alpha_sub_11": alpha_seq[2], "alpha_sub_12": alpha_seq[3],
        "r2_5pt": reg[10]["r_squared"], "r2_6pt": r2_6pt, "r2_7pt": r2_7pt,
        "r2_best_6or7": r2_best_6or7,
        # Sage-Q cross-check
        "max_alpha_dev_Q_vs_np": max_alpha_dev,
        "max_r2_dev_Q_vs_np": max_r2_dev,
        "sageQ_numpy_machine_eps": sageQ_numpy_machine_eps,
        # Richardson
        "alpha_inf": alpha_inf,
        "r_powerlaw": r_powerlaw,
        "alpha_inf_r_half": a_inf_r_half,
        "alpha_inf_r_quarter": a_inf_r_quarter,
        "aitken_top": aitken_top, "aitken_low": aitken_low,
        "alpha_inf_band_min": alpha_inf_band_min,
        "alpha_inf_band_max": alpha_inf_band_max,
        "conv_diffs": conv["diffs"], "conv_step_ratios": conv["step_ratios"],
        "conv_last_step_ratio": conv["last_step_ratio"],
        "conv_converging": conv["converging"],
        "delta_alpha_shrinking": delta_alpha_shrinking,
        # verdict
        "verdict": verdict, "band_tag": band_tag,
        "sign_verdict": sign_v, "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "toward_reading_A": toward_reading_A,
        "dist_to_A": dist_to_A, "dist_to_B": dist_to_B,
        # provenance
        "kappa_2_substrate_FW": float(kappa_2_substrate_FW),
        "alpha_reading_A": ALPHA_READING_A,
        "alpha_reading_B": ALPHA_READING_B,
        "s91_baseline_alpha_sub_9": 2.4291,
        "s91_baseline_r2": 0.9074,
    }


# ============================ Section 7 — Plot ============================
def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14.0, 6.0), dpi=110)

    L_all = r["L_all"].astype(float)                                # (local)
    delta_all = r["delta_all"]                                      # (local)

    # ---- Left panel: log-log delta_n_s vs L with the per-window fits ----
    pos = delta_all > 0.0                                           # (local)
    ax1.scatter(np.log(L_all[pos]), np.log(delta_all[pos]), s=80,
                color="C0", zorder=4,
                label="delta_n_s(L) > 0 (log-log)")
    if (~pos).any():
        # mark the L=10 anchor crossing (delta==0) at the panel floor
        floor_y = np.log(delta_all[pos]).min() - 0.8                # (local)
        ax1.scatter(np.log(L_all[~pos]),
                    np.full((~pos).sum(), floor_y), s=120,
                    marker="v", color="red", zorder=5,
                    label=f"delta_n_s == 0 at L={r['anchor_crossing_L']} "
                          f"(anchor crossing; log undefined)")

    colors = {9: "C1", 10: "C2", 11: "C3", 12: "C4"}                # (local)
    x_line = np.linspace(np.log(6) - 0.05, np.log(12) + 0.05, 50)   # (local)
    for hi in [9, 10, 11, 12]:
        rr = r["reg"][hi]                                          # (local)
        if math.isnan(rr["alpha_sub"]):
            continue
        y_line = rr["slope"] * x_line + rr["intercept"]            # (local)
        ax1.plot(x_line, y_line, "-", color=colors[hi], lw=1.6,
                 label=f"fit L in 6..{hi}: alpha_sub={rr['alpha_sub']:.3f} "
                       f"(R2={rr['r_squared']:.3f})")
    ax1.set_xlabel("log(L_max)", fontsize=11)
    ax1.set_ylabel("log(delta_n_s)", fontsize=11)
    ax1.set_title("Sub-window log-log fits (FWD-C1 delta_n_s)\n"
                  "alpha_sub DECREASES as window grows past L=10 crossing",
                  fontsize=10)
    ax1.legend(loc="lower left", fontsize=8.0, framealpha=0.92)
    ax1.grid(True, alpha=0.32)

    # ---- Right panel: alpha_sub(L_max) sequence + Richardson alpha_inf ----
    Lseq = np.array([9, 10, 11, 12])                                # (local)
    ax2.plot(Lseq, r["alpha_seq"], "o-", color="C0", lw=1.8, ms=9,
             label="alpha_sub(L_max) sequence")
    ax2.axhline(r["alpha_reading_A"], ls=":", color="C2", lw=1.5,
                label=f"Reading A asymptotic alpha={r['alpha_reading_A']:.0f}")
    ax2.axhline(r["alpha_reading_B"], ls="--", color="C3", lw=1.5,
                label=f"Reading B persistent alpha={r['alpha_reading_B']:.3f}")
    ax2.axhline(ALPHA_PASS_A, ls="-.", color="C4", lw=1.2,
                label=f"PASS-A threshold alpha_inf>{ALPHA_PASS_A}")
    ax2.axhline(ALPHA_FAIL_B, ls="-.", color="C5", lw=1.2,
                label=f"FAIL-B ceiling alpha_inf<={ALPHA_FAIL_B}")
    # Richardson alpha_inf marker (canonical) — clipped to a readable y if extreme
    a_inf = r["alpha_inf"]                                          # (local)
    a_inf_disp = max(min(a_inf, 4.0), -2.0)                        # (local) display clip
    ax2.scatter([12.6], [a_inf_disp], marker="*", s=260, color="black",
                zorder=6,
                label=f"Richardson alpha_inf = {a_inf:.3f} "
                      f"({'clipped' if a_inf != a_inf_disp else 'shown'})")
    ax2.annotate(f"alpha_inf = {a_inf:.2f}\n"
                 f"step ratio = {r['conv_last_step_ratio']:.2f} "
                 f"({'DIVERGENT' if not r['conv_converging'] else 'conv'})",
                 xy=(12.6, a_inf_disp), xytext=(10.0, -1.4),
                 fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", color="black", lw=1.0))
    ax2.set_xlabel("L_max (upper window edge)", fontsize=11)
    ax2.set_ylabel("alpha_sub", fontsize=11)
    ax2.set_ylim(-2.3, 4.2)
    ax2.set_title(f"{GATE_ID}\n"
                  f"verdict = {r['verdict']} ({r['band_tag']}); "
                  f"sign={r['sign_verdict']} regime={r['regime_verdict']}",
                  fontsize=9.5)
    ax2.legend(loc="lower left", fontsize=7.8, framealpha=0.92)
    ax2.grid(True, alpha=0.32)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"plot written: {OUT_PNG}")


# ============================ Section 8 — Verdict emission ============================
def append_verdict(gate_id: str, verdict: str, value: str,
                   scheme: str, convention: str, L_max,
                   input_pin_map: dict,
                   schema_v2_annotation: dict,
                   script_path: Path, canonical_path: Path) -> tuple[str, str]:
    """Emit the canonical dual-SHA verdict line + dual-SHA companion comment
    row + REQUIRED schema-v2 3-tuple companion row per gate-verdicts.md
    §"S87+ canonical form". audit_sha256 = closure over
    script_bytes || canonical_bytes || sorted(input_pin_map)JSON."""
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, input_pin_map)

    canonical_line = (
        f"{gate_id}: {verdict} -- value='{value}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha_row = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple_row = (
        f"# sign_verdict={schema_v2_annotation['sign_verdict']} "
        f"magnitude_verdict={schema_v2_annotation['magnitude_verdict']} "
        f"regime_verdict={schema_v2_annotation['regime_verdict']} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_sha_row)
        fp.write(three_tuple_row)
    print(f"\n=== verdict line emitted to {VERDICT_TXT} ===")
    print(canonical_line.rstrip())
    print(dual_sha_row.rstrip())
    print(three_tuple_row.rstrip())
    return audit_sha, content_sha


# ============================ Section 9 — main ============================
def main() -> int:
    pins = log_input_pins(INPUT_FILES)
    r = compute()
    make_plot(r)

    # ---- Save .npz (per plan §output_artifacts.data) ----
    save_dict = {
        # substrate-first inputs
        "L_all": r["L_all"],
        "delta_all": r["delta_all"],
        "n_s_FW_exact": np.array(r["n_s_FW_exact"]),
        "n_s_recomp": r["n_s_recomp"],
        "mellin_s": np.array(r["mellin_s"]),
        "tau_fold_npz": np.array(r["tau_fold_npz"]),
        "anchor_crossing_L": np.array(r["anchor_crossing_L"]),
        "post_anchor_reascent": np.array(r["post_anchor_reascent"]),
        "fwd_c1_audit_sha": np.array(r["fwd_c1_audit_sha"]),
        # per-window regressions
        "alpha_sub_seq_L": np.array([9, 10, 11, 12]),
        "alpha_sub_seq": np.array(r["alpha_seq"]),
        "alpha_sub_9": np.array(r["alpha_sub_9"]),
        "alpha_sub_10": np.array(r["alpha_sub_10"]),
        "alpha_sub_11": np.array(r["alpha_sub_11"]),
        "alpha_sub_12": np.array(r["alpha_sub_12"]),
        "r2_5pt": np.array(r["r2_5pt"]),
        "r2_6pt": np.array(r["r2_6pt"]),
        "r2_7pt": np.array(r["r2_7pt"]),
        "r2_best_6or7": np.array(r["r2_best_6or7"]),
        # Sage-Q cross-check
        "max_alpha_dev_Q_vs_np": np.array(r["max_alpha_dev_Q_vs_np"]),
        "max_r2_dev_Q_vs_np": np.array(r["max_r2_dev_Q_vs_np"]),
        "sageQ_numpy_machine_eps": np.array(r["sageQ_numpy_machine_eps"]),
        # Richardson
        "alpha_inf": np.array(r["alpha_inf"]),
        "r_powerlaw": np.array(r["r_powerlaw"]),
        "alpha_inf_r_half": np.array(r["alpha_inf_r_half"]),
        "alpha_inf_r_quarter": np.array(r["alpha_inf_r_quarter"]),
        "aitken_top": np.array(r["aitken_top"]),
        "aitken_low": np.array(r["aitken_low"]),
        "alpha_inf_band_min": np.array(r["alpha_inf_band_min"]),
        "alpha_inf_band_max": np.array(r["alpha_inf_band_max"]),
        "conv_diffs": np.array(r["conv_diffs"]),
        "conv_step_ratios": np.array(r["conv_step_ratios"]),
        "conv_last_step_ratio": np.array(r["conv_last_step_ratio"]),
        "conv_converging": np.array(r["conv_converging"]),
        "delta_alpha_shrinking": np.array(r["delta_alpha_shrinking"]),
        # verdict
        "verdict": np.array(r["verdict"]),
        "band_tag": np.array(r["band_tag"]),
        "sign_verdict": np.array(r["sign_verdict"]),
        "magnitude_verdict": np.array(r["magnitude_verdict"]),
        "regime_verdict": np.array(r["regime_verdict"]),
        "toward_reading_A": np.array(r["toward_reading_A"]),
        "dist_to_A": np.array(r["dist_to_A"]),
        "dist_to_B": np.array(r["dist_to_B"]),
        # provenance
        "kappa_2_substrate_FW": np.array(r["kappa_2_substrate_FW"]),
        "alpha_reading_A": np.array(r["alpha_reading_A"]),
        "alpha_reading_B": np.array(r["alpha_reading_B"]),
        "s91_baseline_alpha_sub_9": np.array(r["s91_baseline_alpha_sub_9"]),
        "s91_baseline_r2": np.array(r["s91_baseline_r2"]),
    }
    np.savez(OUT_NPZ, **save_dict)
    print(f"npz written: {OUT_NPZ}")

    # ---- value field (plan §8 expected output 4-tuple) ----
    value_field = (
        f"alpha_inf={r['alpha_inf']:.4f};"
        f"band_tag={r['band_tag']};"
        f"alpha_sub_seq=[{r['alpha_sub_9']:.4f},{r['alpha_sub_10']:.4f},"
        f"{r['alpha_sub_11']:.4f},{r['alpha_sub_12']:.4f}];"
        f"r2_6pt={r['r2_6pt']:.4f};r2_7pt={r['r2_7pt']:.4f};"
        f"r2_best={r['r2_best_6or7']:.4f};"
        f"step_ratio={r['conv_last_step_ratio']:.4f};"
        f"converging={bool(r['conv_converging'])};"
        f"delta_alpha_shrinking={bool(r['delta_alpha_shrinking'])};"
        f"alpha_inf_band=[{r['alpha_inf_band_min']:.4f},{r['alpha_inf_band_max']:.4f}];"
        f"toward_reading_A={bool(r['toward_reading_A'])};"
        f"anchor_crossing_L={r['anchor_crossing_L']};"
        f"sageQ_numpy_machine_eps={bool(r['sageQ_numpy_machine_eps'])}"
    )

    print(f"\n4-tuple: (value='{value_field[:80]}...', scheme={SCHEME[:50]}..., "
          f"convention={CONVENTION[:50]}..., L_max={L_MAX_TAG})")

    # ---- input_pin_map for closure SHA ----
    input_pin_map = {rel: sha for rel, sha in pins.items()}
    input_pin_map["canonical_constants_kappa_2_substrate_FW"] = (
        f"{kappa_2_substrate_FW:.18e}")
    input_pin_map["canonical_constants_tau_fold"] = f"{float(tau_fold):.18e}"
    input_pin_map["canonical_constants_M_KK_gravity"] = (
        f"{float(M_KK_gravity):.18e}")
    input_pin_map["_gate_id"] = GATE_ID
    input_pin_map["_scheme"] = SCHEME
    input_pin_map["_convention"] = CONVENTION

    schema_v2_annotation = {
        "sign_verdict": r["sign_verdict"],
        "magnitude_verdict": r["magnitude_verdict"],
        "regime_verdict": r["regime_verdict"],
    }

    audit_sha, content_sha = append_verdict(
        gate_id=GATE_ID,
        verdict=r["verdict"],
        value=value_field,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_TAG,
        input_pin_map=input_pin_map,
        schema_v2_annotation=schema_v2_annotation,
        script_path=Path(__file__),
        canonical_path=SHARED_DIR / "canonical_constants.py",
    )

    # ---- diagnostic summary ----
    print(f"\n=== {GATE_ID} summary ===")
    print(f"  anchor crossing L:        {r['anchor_crossing_L']} "
          f"(delta_n_s==0; post-anchor re-ascent={r['post_anchor_reascent']})")
    print(f"  alpha_sub sequence:       "
          f"[{r['alpha_sub_9']:.4f}, {r['alpha_sub_10']:.4f}, "
          f"{r['alpha_sub_11']:.4f}, {r['alpha_sub_12']:.4f}]")
    print(f"  R2 5/6/7-pt:              "
          f"{r['r2_5pt']:.4f} / {r['r2_6pt']:.4f} / {r['r2_7pt']:.4f}")
    print(f"  step ratio (last):        {r['conv_last_step_ratio']:.4f} "
          f"(converging={r['conv_converging']})")
    print(f"  Richardson alpha_inf:     {r['alpha_inf']:.4f}  "
          f"(band [{r['alpha_inf_band_min']:.4f}, "
          f"{r['alpha_inf_band_max']:.4f}])")
    print(f"  toward Reading A?:        {r['toward_reading_A']} "
          f"(dist_A={r['dist_to_A']:.4f}, dist_B={r['dist_to_B']:.4f})")
    print(f"  Sage-Q machine eps:       {r['sageQ_numpy_machine_eps']} "
          f"(|Dalpha|={r['max_alpha_dev_Q_vs_np']:.2e}, "
          f"|DR2|={r['max_r2_dev_Q_vs_np']:.2e})")
    print(f"  VERDICT:                  {r['verdict']}  ({r['band_tag']})")
    print(f"  3-tuple:                  sign={r['sign_verdict']} "
          f"mag={r['magnitude_verdict']} regime={r['regime_verdict']}")
    print(f"  audit_sha256:             {audit_sha}")
    print(f"  content_sha256:           {content_sha}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
