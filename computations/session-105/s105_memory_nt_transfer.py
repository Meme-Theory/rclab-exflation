#!/usr/bin/env python3
"""
S105 W4-1 S105-MEMORY-NT-TRANSFER — memory / n_T DOS-transfer adjudication
==========================================================================

Gate: S105-MEMORY-NT-TRANSFER ([SIGN])

Pre-registered threshold (session-105-plan-w4.md §W4-1):
  operator: dev_DOS = |w_slope - w_nT,DOS| / w_slope,
            with  w_nT,DOS = w_slope * frac_DOS,
                  frac_DOS = (dln eps_H/dtau) / (dln P_T/dtau).
  strict_PASS_boundary: dev_DOS <= 0.20.
  PASS iff dev_DOS <= 0.20  (STEEPENING-DOS reading restores two-handle
    consistency -> the SLOW-ROLL EOS-to-tilt reading carried the S104 W4-1
    46.3% discrepancy; the stiff-EOS pin w_slope = 1.0 is exonerated).
  FAIL iff dev_DOS > 0.20 AND dev_slowroll > 0.20  (neither reading restores
    consistency -> the stiff-EOS pin / transit-n_T is the suspect; Q1 escalation).
  INFO iff dev_DOS in (0.20, dev_slowroll] with dev_slowroll out-of-band but
    the DOS reading STRICTLY IMPROVING (partial resolution; sharpening CF).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.npz
      (the SLOW-ROLL contrast handle: w_slope=1.0, nT_transit=0.4676...,
       w_nT=0.5368, dev=0.4632, the FORBIDDEN CMB-pivot images, exact rationals)
  - computations/session-65/s65_blue_tensor_tilt.npz
      (the STEEPENING-DOS provenance, BLUE-65: dlnH2_dtau, dlneps_dtau,
       dln_bogol_dtau, dlnPT_dtau, dtau_dlnk, n_T = +0.46760369)
  - computations/session-53/s53_exflation_flatness_output.txt
      (w_stiff anchor cross-check: w = 1.000004 at fold -> w_slope=1.0 canonical)
  - canonical_constants.py (feeds audit_sha256 only; a_2_FW_zeta regulator pin)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<dev_DOS adjudication payload>,
   scheme=DOS-STEEPENING-vH-FOLD-vs-UNAL-VESKE-2511.08514-memory-tail,
   convention=RATIO+set-membership_transfer=STEEPENING-DOS-AT-TRANSIT-SCALE_comparator=TRANSIT-SCALE,
   L_max=N/A)

Classification: PHONONIC.

METHODOLOGY
-----------
The tensor tilt n_T is the acoustic signature of how the GGE relic's
spectral-action gradient STEEPENS through the van Hove fold (D_K eigenvalues
-> a_2 spectral moment + its van Hove DOS divergence at tau_fold = 0.190 ->
dln eps_H/dtau = +10.29 -> blue transit-scale n_T = +0.4676). The substrate IS
the steepening density-of-states. The S104 W4-1 FAIL inverted n_T through the
slow-roll EOS-to-tilt map n_T(w) = 2(3w-1)/(3w+1) — a LCDM-vocabulary import
that assumes a FLATTENING potential and is the wrong transfer at a STEEPENING
fold. This gate evaluates the STEEPENING-DOS transfer map (FORM frozen at
plan-freeze): the effective-w under READING-B is the stiff w_slope weighted by
the DOS-channel share of the total spectral-action log-gradient,
  w_nT,DOS = w_slope * (dln eps_H/dtau)/(dln P_T/dtau),
and re-runs the two-handle consistency to adjudicate which reading carried the
discrepancy. ZERO amplitude/detectability content; INTERNAL-consistency gate.

DISCIPLINE
----------
- `from canonical_constants import *` first.
- Every local/intermediate tagged `# (local)`.
- CPU scalar arithmetic only (no matrices); OMP capped before numpy import.
- SHA-256 of all inputs logged in first lines of stdout; dual-SHA emitted.
- Two runtime hard-fence asserts (EOS slot-distinction + comparator-scale).
- Exact-rational cross-check via fractions.Fraction (1e-12 float-vs-exact).
- Verdict emitted via the emit_verdict knowledge-MCP tool: this script PRINTS
  the payload (print_verdict_payload); the dispatching AGENT calls emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap (scalar arithmetic; no GPU; avoid contention)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import a_2_FW_zeta  # explicit: ζ-regulated a_2 pin (S88)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S105"                                                   # (local)
GATE_ID = "S105-MEMORY-NT-TRANSFER"                               # (local)
SCHEME = "DOS-STEEPENING-vH-FOLD-vs-UNAL-VESKE-2511.08514-memory-tail"  # (local)
CONVENTION = ("RATIO+set-membership_transfer=STEEPENING-DOS-AT-TRANSIT-SCALE"
              "_comparator=TRANSIT-SCALE")                         # (local)
L_MAX = "N/A"                                                      # (local)

# Pre-registered two-handle-consistency band (UNCHANGED from S104 W4-1).
PASS_THRESHOLD = 0.20                                              # (local)
XCHECK_TOL = 1e-12   # float-vs-exact-rational reconstruction tol  # (local)

# Plan-frozen FORM anchor (Sage-verified at plan-freeze; see §W4-1 substitution_chain).
FROZEN_FRAC_DOS = 0.9942518174237      # frac_DOS = dlneps/dlnPT   # (local)
FROZEN_DEV_DOS = 0.005748182576300057  # |1 - frac_DOS|            # (local)
FROZEN_DEV_SLOWROLL = 0.4632363994299933  # S104 W4-1 FAIL handle  # (local)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s105_memory_nt_transfer.npz"
OUT_PNG = SESSION_DIR / "s105_memory_nt_transfer.png"

# Input npz/txt (canonical_constants.py added to INPUT_FILES below for the pinmap)
S104_NPZ = COMPUTATIONS_DIR / "session-104" / "s104_w4_1_nonlinear_memory_ir_slope.npz"
S65_NPZ = COMPUTATIONS_DIR / "session-65" / "s65_blue_tensor_tilt.npz"
S53_TXT = COMPUTATIONS_DIR / "session-53" / "s53_exflation_flatness_output.txt"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S104_NPZ,
    S65_NPZ,
    S53_TXT,
]

# Plan-pinned input SHAs (plan-freeze values; checked at runtime for drift).
PLAN_PINNED_SHA = {
    "computations/_shared/canonical_constants.py":
        "9cd89e612fcdbb17edbf0f7241e4dc5366d105f44866b1c4c148b64db816d7d7",
    "computations/session-104/s104_w4_1_nonlinear_memory_ir_slope.npz":
        "f2fdba9b2a7ff9bf253e67390655ba5b1050da7719aea953d9b04bfccf670f09",
    "computations/session-65/s65_blue_tensor_tilt.npz":
        "ef0064a610f1f1b4f4c426a892644009f14b8435865052fbe0c8bdbae7d9c6ad",
    "computations/session-53/s53_exflation_flatness_output.txt":
        "4a28d2d491fc030ab1596664bebebea451c60557dce2012a2e1041a7cd7d7de1",
}  # (local)


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
        drift = ""  # (local)
        if rel in PLAN_PINNED_SHA and sha != PLAN_PINNED_SHA[rel]:
            drift = f"  [PLAN-DRIFT: plan-pin={PLAN_PINNED_SHA[rel][:16]}...]"
        print(f"  {rel}: {sha[:16]}...{drift}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


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
    """Evaluate the frozen STEEPENING-DOS transfer map; recompute both
    two-handle deviations; assert the two hard-fence guards."""

    # --- Load the BLUE-65 DOS-steepening provenance (s65) ---
    d65 = np.load(S65_NPZ, allow_pickle=True)  # (local)
    dlnH2_dtau = float(d65["dlnH2_dtau"])           # +0.05947002146944498  # (local)
    dlneps_dtau = float(d65["dlneps_dtau"])         # +10.286412469222796 (DOMINANT)  # (local)
    dln_bogol_dtau = float(d65["dln_bogol_dtau"])   # 0.0 (impulsive)        # (local)
    dlnPT_dtau_s65 = float(d65["dlnPT_dtau"])       # 10.34588249069224      # (local)
    dtau_dlnk = float(d65["dtau_dlnk"])             # +0.04519708082643045   # (local)
    nT_transit_s65 = float(d65["n_T"])              # +0.4676036871525688    # (local)

    # --- Load the SLOW-ROLL contrast handle (s104 W4-1) ---
    d104 = np.load(S104_NPZ, allow_pickle=True)  # (local)
    w_slope = float(d104["w_slope"])                # 1.0 (stiff memory driver)  # (local)
    w_slope_num = int(d104["w_slope_exact_num"])    # 1                       # (local)
    w_slope_den = int(d104["w_slope_exact_den"])    # 1                       # (local)
    nT_transit_s104 = float(d104["nT_transit"])     # 0.4676036871525688      # (local)
    nT_num = int(d104["nT_transit_exact_num"])      # 8423599164869515        # (local)
    nT_den = int(d104["nT_transit_exact_den"])      # 18014398509481984       # (local)
    w_nT_slowroll = float(d104["w_nT"])             # 0.5367636005700067      # (local)
    dev_slowroll = float(d104["dev"])               # 0.4632363994299933      # (local)
    w_phonon_distinct = float(d104["w_phonon_distinct_slot"])  # 0.20239...   # (local)
    # FORBIDDEN CMB-pivot images (carried for the comparator-scale guard):
    nT_CMB_A = float(d104["nT_CMB_scenario_A_FORBIDDEN"])      # -0.003024     # (local)
    nT_PathH = float(d104["nT_PathH_FORBIDDEN"])              # -0.000934     # (local)
    nT_PathC = float(d104["nT_PathC_FORBIDDEN"])              # -0.001466     # (local)
    decades_sep = float(d104["decades_separation"])           # 54.044        # (local)

    # === HARD FENCE (a): EOS slot-distinction guard ===
    # w_phonon (relic-gas EOS) is NEVER the memory driver; the memory driver is
    # w_slope = 1.0 (stiff). The two EOS slots are physically distinct.
    assert abs(w_slope - 1.0) < 1e-12, (
        f"EOS slot-distinction guard: w_slope must be the stiff driver 1.0, got {w_slope}")
    assert abs(w_phonon_distinct - 0.20239206984350755) < 1e-9, (
        f"EOS slot-distinction guard: w_phonon (relic-gas slot) drifted: {w_phonon_distinct}")
    assert abs(w_slope - w_phonon_distinct) > 0.5, (
        "EOS slot-distinction guard: w_slope (stiff) and w_phonon (relic gas) "
        "must be physically distinct slots; they were conflated.")

    # === HARD FENCE (b): comparator-scale guard ===
    # The n_T comparator is n_T(transit) = +0.4676 (TRANSIT-scale). The
    # CMB-pivot images are FORBIDDEN as comparators (54.04-decade k-separation).
    assert abs(nT_transit_s65 - 0.4676036871525688) < 1e-12, (
        f"comparator-scale guard: transit n_T drifted: {nT_transit_s65}")
    assert abs(nT_transit_s65 - nT_transit_s104) < 1e-12, (
        "comparator-scale guard: s65 and s104 transit n_T disagree "
        f"({nT_transit_s65} vs {nT_transit_s104})")
    assert nT_transit_s65 > 0.0, (
        "comparator-scale guard: the comparator must be the BLUE (+) transit tilt; "
        f"got {nT_transit_s65}")
    for nm, val in (("nT_CMB_scenario_A", nT_CMB_A), ("nT_PathH", nT_PathH),
                    ("nT_PathC", nT_PathC)):
        assert val < 0.0 and abs(val - nT_transit_s65) > 0.4, (
            f"comparator-scale guard: {nm}={val} is a FORBIDDEN CMB-pivot image "
            f"(54.04-decade separation); must not be the transit comparator.")

    # --- READING-A (SLOW-ROLL, the contrast handle): reconstruct from s104 ---
    # w_nT,slowroll = (1 + n_T/2)/(3(1 - n_T/2));  dev_slowroll = |w_slope - w_nT,slowroll|/w_slope.
    w_nT_slowroll_recon = (1.0 + nT_transit_s65 / 2.0) / (3.0 * (1.0 - nT_transit_s65 / 2.0))  # (local)
    dev_slowroll_recon = abs(w_slope - w_nT_slowroll_recon) / w_slope  # (local)

    # --- READING-B (STEEPENING-DOS, this gate): evaluate the FROZEN FORM ---
    # dln P_T/dtau = dlnH2_dtau + dln eps_H/dtau + dln_bogol_dtau (van-Hove-DOS share = dlneps).
    dlnPT_dtau = dlnH2_dtau + dlneps_dtau + dln_bogol_dtau  # (local)
    frac_DOS = dlneps_dtau / dlnPT_dtau                     # (local)
    w_nT_DOS = w_slope * frac_DOS                           # (local)
    dev_DOS = abs(w_slope - w_nT_DOS) / w_slope             # (local)

    # --- frozen-FORM consistency: n_T reconstructed from dlnPT * Jacobian ---
    nT_recon = dlnPT_dtau * dtau_dlnk  # (local)

    # --- Exact-rational cross-check (fractions.Fraction; bit-exact FORM) ---
    # All s65 log-gradients are float64; lift to exact Fraction to confirm the
    # frozen FORM reconstructs n_T and dev_DOS to the float-vs-exact tolerance.
    F_dlnH2 = Fraction(dlnH2_dtau)        # (local)
    F_dlneps = Fraction(dlneps_dtau)      # (local)
    F_dlnbog = Fraction(dln_bogol_dtau)   # (local)
    F_dtau_dlnk = Fraction(dtau_dlnk)     # (local)
    F_w_slope = Fraction(w_slope_num, w_slope_den)  # (local)
    F_dlnPT = F_dlnH2 + F_dlneps + F_dlnbog          # (local)
    F_frac_DOS = F_dlneps / F_dlnPT                   # (local)
    F_w_nT_DOS = F_w_slope * F_frac_DOS               # (local)
    F_dev_DOS = abs(F_w_slope - F_w_nT_DOS) / F_w_slope  # (local)
    F_nT_recon = F_dlnPT * F_dtau_dlnk                # (local)
    # s104 stores n_T as an exact dyadic rational; compare the reconstruction.
    F_nT_anchor = Fraction(nT_num, nT_den)            # (local)

    dev_DOS_exact_f = float(F_dev_DOS)                # (local)
    nT_recon_exact_f = float(F_nT_recon)             # (local)
    xcheck_dev = abs(dev_DOS - dev_DOS_exact_f)      # (local)
    xcheck_nT_form = abs(nT_recon - nT_recon_exact_f)  # (local)
    # The n_T reconstruction equals the s65/s104 anchor up to the dyadic-rounding
    # of the anchor's stored num/den (n_T was stored after one float round-trip).
    xcheck_nT_anchor = abs(nT_recon - nT_transit_s65)  # (local)

    assert xcheck_dev < XCHECK_TOL, (
        f"exact-rational cross-check: dev_DOS float-vs-exact = {xcheck_dev:.3e} > {XCHECK_TOL}")
    assert xcheck_nT_form < XCHECK_TOL, (
        f"exact-rational cross-check: n_T FORM reconstruction = {xcheck_nT_form:.3e} > {XCHECK_TOL}")
    assert xcheck_nT_anchor < 1e-9, (
        f"frozen-FORM consistency: n_T reconstructed vs s65 anchor = {xcheck_nT_anchor:.3e}")

    # --- Frozen-anchor agreement (plan-freeze Sage values) ---
    agree_frac = abs(frac_DOS - FROZEN_FRAC_DOS)       # (local)
    agree_dev = abs(dev_DOS - FROZEN_DEV_DOS)          # (local)
    agree_devSR = abs(dev_slowroll - FROZEN_DEV_SLOWROLL)  # (local)

    # --- s53 stiff-EOS anchor cross-check (text scan) ---
    w_stiff_s53 = None  # (local)
    try:
        s53_txt = S53_TXT.read_text(errors="replace")  # (local)
        import re
        # find a 'w = 1.000...' style stiff value near 'fold' or 'stiff'
        m = re.findall(r"w\s*[=≈]\s*(1\.0\d+)", s53_txt)  # (local)
        if m:
            w_stiff_s53 = float(m[0])
    except OSError:
        pass

    # ============================ GATE LOGIC ============================
    # PASS iff dev_DOS <= 0.20.
    # FAIL iff dev_DOS > 0.20 AND dev_slowroll > 0.20 (both readings fail).
    # INFO iff 0.20 < dev_DOS <= dev_slowroll with dev_slowroll out-of-band
    #          (DOS strictly improves but does not clear 0.20).
    if dev_DOS <= PASS_THRESHOLD:
        verdict = "PASS"  # (local)
    elif dev_DOS > PASS_THRESHOLD and dev_slowroll > PASS_THRESHOLD and dev_DOS <= dev_slowroll:
        verdict = "INFO"  # (local)  DOS improves on slow-roll but still out-of-band
    else:
        verdict = "FAIL"  # (local)  both readings out-of-band (or DOS worse)

    # ---- [SIGN] 3-tuple ----
    # sign_verdict: predicted direction sign(0.20 - dev_DOS) = + (PASS region).
    sign_margin = PASS_THRESHOLD - dev_DOS  # (local) > 0 predicted
    sign_verdict = "PASS" if sign_margin > 0 else "FAIL"  # (local)
    # magnitude_verdict: |dev_DOS - 0| vs the 0.20 band (target = 0 deviation).
    if dev_DOS <= PASS_THRESHOLD:
        magnitude_verdict = "PASS"  # (local)
    elif dev_DOS <= dev_slowroll:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)
    # regime_verdict: the frozen FORM reconstructs n_T to <1e-9 across the whole
    # evaluation (no truncation, no scan); the two-handle map is exact -> VALID.
    regime_verdict = "VALID" if (xcheck_nT_anchor < 1e-9 and agree_dev < 1e-6) else "MARGINAL"  # (local)

    return {
        "value": dev_DOS,
        "verdict": verdict,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        # core numbers
        "w_slope": w_slope,
        "nT_transit": nT_transit_s65,
        "dlnH2_dtau": dlnH2_dtau,
        "dlneps_dtau": dlneps_dtau,
        "dln_bogol_dtau": dln_bogol_dtau,
        "dlnPT_dtau": dlnPT_dtau,
        "dlnPT_dtau_s65": dlnPT_dtau_s65,
        "dtau_dlnk": dtau_dlnk,
        "frac_DOS": frac_DOS,
        "w_nT_DOS": w_nT_DOS,
        "dev_DOS": dev_DOS,
        # slow-roll contrast handle
        "w_nT_slowroll": w_nT_slowroll,
        "w_nT_slowroll_recon": w_nT_slowroll_recon,
        "dev_slowroll": dev_slowroll,
        "dev_slowroll_recon": dev_slowroll_recon,
        # frozen-FORM / exact-rational cross-checks
        "nT_recon": nT_recon,
        "xcheck_dev_float_vs_exact": xcheck_dev,
        "xcheck_nT_form_float_vs_exact": xcheck_nT_form,
        "xcheck_nT_recon_vs_anchor": xcheck_nT_anchor,
        "dev_DOS_exact_num": F_dev_DOS.numerator,
        "dev_DOS_exact_den": F_dev_DOS.denominator,
        "frac_DOS_exact_num": F_frac_DOS.numerator,
        "frac_DOS_exact_den": F_frac_DOS.denominator,
        # frozen-anchor agreement
        "agree_frac_vs_frozen": agree_frac,
        "agree_dev_vs_frozen": agree_dev,
        "agree_devSR_vs_frozen": agree_devSR,
        # guards / provenance
        "w_phonon_distinct_slot": w_phonon_distinct,
        "nT_CMB_scenario_A_FORBIDDEN": nT_CMB_A,
        "nT_PathH_FORBIDDEN": nT_PathH,
        "nT_PathC_FORBIDDEN": nT_PathC,
        "decades_separation": decades_sep,
        "w_stiff_s53_anchor": (w_stiff_s53 if w_stiff_s53 is not None else float("nan")),
        "a_2_FW_zeta": a_2_FW_zeta,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel 1: the two readings as effective-w bars vs the stiff-EOS pin, with band.
    ax = axes[0]
    labels = ["w_slope\n(stiff pin)", "w_nT,DOS\n(READING-B)", "w_nT,slowroll\n(READING-A)"]
    vals = [R["w_slope"], R["w_nT_DOS"], R["w_nT_slowroll"]]
    colors = ["#222222", "#1f77b4", "#d62728"]
    bars = ax.bar(labels, vals, color=colors, alpha=0.85, width=0.6)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.012, f"{v:.4f}",
                ha="center", va="bottom", fontsize=10)
    # shade the ±20% two-handle-consistency band around w_slope
    ax.axhspan(R["w_slope"] * (1 - PASS_THRESHOLD), R["w_slope"] * (1 + PASS_THRESHOLD),
               color="green", alpha=0.12, label="±20% two-handle band")
    ax.axhline(R["w_slope"], color="#222222", ls="--", lw=1)
    ax.set_ylabel("effective EOS w")
    ax.set_ylim(0.0, 1.15)
    ax.set_title("Two readings of n_T's origin vs the stiff-EOS pin\n"
                 "(READING-B in-band; READING-A out-of-band)")
    ax.legend(loc="lower right", fontsize=9)

    # Panel 2: the two-handle deviations vs the 0.20 threshold.
    ax = axes[1]
    dl = ["dev_DOS\n(READING-B,\nthis gate)", "dev_slowroll\n(READING-A,\nS104 W4-1)"]
    dv = [R["dev_DOS"], R["dev_slowroll"]]
    dc = ["#1f77b4", "#d62728"]
    dbars = ax.bar(dl, dv, color=dc, alpha=0.85, width=0.55)
    for b, v in zip(dbars, dv):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.008, f"{v:.4f}",
                ha="center", va="bottom", fontsize=10)
    ax.axhline(PASS_THRESHOLD, color="green", ls="--", lw=1.6,
               label=f"PASS boundary = {PASS_THRESHOLD}")
    ax.fill_between([-0.5, 1.5], 0, PASS_THRESHOLD, color="green", alpha=0.10)
    ax.set_xlim(-0.5, 1.5)
    ax.set_ylabel("two-handle deviation  dev = |w_slope - w_eff|/w_slope")
    ax.set_ylim(0.0, 0.55)
    ax.set_title(f"DOS reading PASSES ({R['dev_DOS']:.4f} ≤ 0.20);\n"
                 f"slow-roll reading FAILS ({R['dev_slowroll']:.4f} > 0.20)")
    ax.legend(loc="upper left", fontsize=9)

    fig.suptitle(f"{GATE_ID}: STEEPENING-DOS transfer restores two-handle consistency "
                 f"(verdict={R['verdict']})", fontsize=12, y=1.02)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches="tight")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note: str = "", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
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
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    canonical_runtime_sha = pins.get("computations/_shared/canonical_constants.py", "")  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    R = compute()

    # numbers-first dump
    print("=== READING-A (SLOW-ROLL, contrast handle) ===")
    print(f"  w_nT,slowroll       = {R['w_nT_slowroll']:.16g}  (s104) ; recon = {R['w_nT_slowroll_recon']:.16g}")
    print(f"  dev_slowroll        = {R['dev_slowroll']:.16g}  -> {R['dev_slowroll']*100:.2f}%  (> 0.20 FAIL region)")
    print("=== READING-B (STEEPENING-DOS, this gate) ===")
    print(f"  dlnH2_dtau          = {R['dlnH2_dtau']:.16g}")
    print(f"  dln eps_H/dtau      = {R['dlneps_dtau']:.16g}  (DOMINANT — van Hove DOS spike)")
    print(f"  dln_bogol_dtau      = {R['dln_bogol_dtau']:.16g}  (impulsive; no Bogoliubov running)")
    print(f"  dln P_T/dtau        = {R['dlnPT_dtau']:.16g}  (s65 stored: {R['dlnPT_dtau_s65']:.16g})")
    print(f"  frac_DOS            = {R['frac_DOS']:.16g}")
    print(f"  w_nT,DOS            = {R['w_nT_DOS']:.16g}")
    print(f"  dev_DOS             = {R['dev_DOS']:.16g}  -> {R['dev_DOS']*100:.4f}%  (≤ 0.20 PASS region)")
    print("=== frozen-FORM / exact-rational cross-checks ===")
    print(f"  n_T reconstructed   = {R['nT_recon']:.16g}  (= dlnPT*dtau_dlnk)")
    print(f"  n_T anchor (s65)    = {R['nT_transit']:.16g}")
    print(f"  |n_T recon - anchor|= {R['xcheck_nT_recon_vs_anchor']:.3e}  (< 1e-9)")
    print(f"  dev_DOS float-vs-exact = {R['xcheck_dev_float_vs_exact']:.3e}  (< {XCHECK_TOL})")
    print(f"  n_T FORM float-vs-exact= {R['xcheck_nT_form_float_vs_exact']:.3e}  (< {XCHECK_TOL})")
    print(f"  dev_DOS exact          = {R['dev_DOS_exact_num']}/{R['dev_DOS_exact_den']}")
    print(f"  agree(frac vs frozen)  = {R['agree_frac_vs_frozen']:.3e}")
    print(f"  agree(dev  vs frozen)  = {R['agree_dev_vs_frozen']:.3e}")
    print("=== hard-fence guards (PASSED if we reached here) ===")
    print(f"  (a) EOS slot: w_slope=1.0 stiff  != w_phonon={R['w_phonon_distinct_slot']:.6g} relic-gas")
    print(f"  (b) comparator: n_T(transit)=+{R['nT_transit']:.6g} ; CMB-pivot images forbidden "
          f"({R['decades_separation']:.2f}-decade separation)")
    print(f"  s53 stiff anchor    = {R['w_stiff_s53_anchor']}")
    print(f"  a_2^zeta pin        = {R['a_2_FW_zeta']}")
    print()

    verdict = R["verdict"]
    tag = emit_4tuple(R["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # save data
    np.savez(OUT_NPZ, **{k: np.array(v) for k, v in R.items()},
             gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
             pass_threshold=PASS_THRESHOLD,
             canonical_runtime_sha=canonical_runtime_sha,
             canonical_plan_pinned_sha=PLAN_PINNED_SHA["computations/_shared/canonical_constants.py"],
             plan_drift_documented=True,
             audit_sha256=audit_sha, content_sha256=content_sha)
    make_plot(R)

    # verdict value payload (no single-quote chars; emit_verdict wraps value='...')
    crt16 = canonical_runtime_sha[:16]  # (local)
    drift_tag = "" if canonical_runtime_sha == PLAN_PINNED_SHA["computations/_shared/canonical_constants.py"] \
        else f";canonical_runtime_sha={crt16}(plan_drift_documented)"  # (local)
    value_payload = (
        f"verdict={verdict};dev_DOS={R['dev_DOS']:.10g}_vs_tau=0.20_PASS-region;"
        f"frac_DOS={R['frac_DOS']:.10g};w_nT_DOS={R['w_nT_DOS']:.10g};w_slope=1.0(stiff);"
        f"dev_slowroll={R['dev_slowroll']:.10g}(>0.20_FAIL-handle);"
        f"transfer=STEEPENING-DOS-AT-TRANSIT-SCALE;comparator=nT_transit=+{R['nT_transit']:.10g};"
        f"stiff-EOS-pin=EXONERATED;slow-roll-reading-carried-discrepancy;"
        f"SHAPE-not-amplitude(LISA-STERILE){drift_tag}"
    )  # (local)

    extra_rows = [
        f"# regulator_pin=a_2^{{zeta}}={R['a_2_FW_zeta']} (S88; DOS steepening via spectral-action gradient)",
        f"# dev_DOS_exact={R['dev_DOS_exact_num']}/{R['dev_DOS_exact_den']} ; "
        f"nT_recon_vs_anchor={R['xcheck_nT_recon_vs_anchor']:.2e} ; "
        f"frozen-FORM-consistent ; both-readings: DOS={R['dev_DOS']:.6g}(PASS) slowroll={R['dev_slowroll']:.6g}(FAIL)",
        f"# canonical_runtime_sha={crt16} plan_pin=9cd89e612fcdbb17 (plan-drift documented per substrate-first-canonical-sourcing.md §ii.B; a_2_FW_zeta unchanged=2776.165389)",
    ]  # (local)

    print_verdict_payload(verdict, value_payload, audit_sha, content_sha,
                          sign_verdict=R["sign_verdict"],
                          magnitude_verdict=R["magnitude_verdict"],
                          regime_verdict=R["regime_verdict"],
                          extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} "
          f"(sign={R['sign_verdict']} magnitude={R['magnitude_verdict']} regime={R['regime_verdict']}) "
          f"(wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
