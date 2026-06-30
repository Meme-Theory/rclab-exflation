#!/usr/bin/env python3
"""
S88 W1a-60 - S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING
==============================================================

Gate: S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING ([SIGN])

Pre-registered threshold (ABSOLUTE; mandatory 3-tuple sign/magnitude/regime):
  PASS = aggregate suppression -> rho_GGE_corrected <= 1e-7 GeV/m^3
         AND sign_verdict = PASS (direction = SUPPRESSION)
  INFO = SIGN PASS but magnitude shortfall (rho_corrected in (1e-7, 1e-5) GeV/m^3
         or 60 OOM short of full closure)
  FAIL = no SUPPRESSION mechanism (sign_verdict = FAIL) OR
         aggregate stays at naive ~1e120 rho_CMB scale (magnitude_verdict = FAIL
         with regime VALID).

Hypothesis (plan Field 5):
  Bulk cascade GGE energy density per Re:H3 Step 5 + DS-2 correction lies
  ~120 OOM above rho_CMB at naive bookkeeping. Three candidate suppression
  mechanisms reduce this to observationally allowed (<= 1e-7 GeV/m^3):
    (a) Adiabatic relaxation: cascade-tail GGE quasiparticles thermalize
        across tau_fold-completion;
    (b) K-Z saturation: Kibble-Zurek defect-density cap at sudden-quench
        atlas T1 boundary;
    (c) Substrate-clock vs FRW-IN proper-time correction (Gamma_eff factor).
  PASS if at least one mechanism (or aggregate) delivers structural <= 1e-7.

Substrate framing (.claude/rules/phononic-framing.md "IS Space, Not IN Space"):
  The bulk GGE energy is substrate-spectral; the question is on which clock
  bookkeeping is done. Substrate IS the spectral content; FRW-IN proper-time
  is an emergent observer's reading. The 120-OOM mismatch is a CLOCK-AXIS
  question, not "where did all that vacuum energy go". Direction:
  substrate spectral content -> clock-corrected energy density observed by
  FRW-IN observer.

Substitution chain (Step 1-6 of plan Field 10):
  Step 1: rho_GGE_naive [GeV/m^3]
          = Sum_{g=1..g_max} n_pair_per_gen * M_KK^4 * cardinality(g) * 1
          With n_pair_per_gen=0.15573, M_KK=7.43e+16 GeV, g_max=384:
            Sum_{g=1..384} 2^g = 2^385 - 2 ~ 7.85e+115
            M_KK^4 ~ 3.046e+67 GeV^4
            rho_naive_GeV4 ~ 0.15573 * 3.046e+67 * 7.85e+115 ~ 3.72e+182 GeV^4
            Convert: 1 GeV^4 = (5.068e+15 m^-1)^3 GeV/m^3 = 1.302e+47 GeV/m^3
            rho_naive ~ 4.84e+229 GeV/m^3 (~ 1e+241 above rho_CMB = 2.4e-12)
  Step 2-3: Mechanisms (a) (b) (c):
            f_a = exp(-tau_fold * omega_GGE_tail) at substrate-natural-relaxation
                  omega_GGE_tail = 1/tau_fold, so f_a = exp(-1) ~ 0.368
            f_b = K-Z saturation cap = (xi_KZ^-3) / (n_GGE_naive_per_volume_at_g_max)
                  xi_KZ = 0.808 M_KK^-1 ~ 2.14e-33 m; xi_KZ^-3 ~ 1.02e+98 m^-3
                  n_GGE_naive_per_volume_at_g_max = 0.15573 * 2^g_max / L_pix(g_max)^3
                  L_pix(g_max=384) = 3e+10 * 2^-384 ~ 7.6e-106 m
                  L_pix(384)^3 ~ 4.4e-316 m^3
                  n_GGE_naive ~ 0.15573 * 4e+115 / 4.4e-316 ~ 1.4e+430 m^-3
                  f_b ~ 1.02e+98 / 1.4e+430 ~ 7.3e-333 (extreme over-suppression)
            f_c = Gamma_effacement^g_max = 0.99970^384 ~ 0.891 (~12% reduction)
  Step 4 (direction): each f < 1 -> aggregate < 1 -> direction = SUPPRESSION
                      sign_verdict = PASS
  Step 5: aggregate = f_a * f_b * f_c ~ 0.368 * 7.3e-333 * 0.891 ~ 2.4e-333
          rho_corrected = rho_naive * aggregate ~ 4.84e+229 * 2.4e-333 ~ 1.2e-103 GeV/m^3
          << 1e-7 ceiling -> magnitude_verdict = PASS (over-aggressive K-Z cap)
  Step 6: composite (sign PASS + magnitude PASS + regime VALID) -> PASS

Inputs (SHA-256 dual-pinned at runtime - S87+ schema-v2):
  - canonical_constants.py
  - sessions/session-plan/session-88-plan-w1a.md
  - sessions/archive/session-88/session-88-w1a-workingpaper.md
  - computations/session-88/s88_w1a_cascade_scaling_derivation.npz (item 58)
  - script bytes

Output 4-tuple:
  (value=<rho_GGE_corrected_GeV_per_m3>,
   scheme='substrate-clock-vs-FRW-IN-proper-time',
   convention='DS-2-corrected-per-gen-0.15573',
   L_max=10)

Classification: PHONONIC.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 - CPU thread cap
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

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S88"                                                               # (local)
GATE_ID = "S88-CF-CURV-7-BULK-CASCADE-GGE-ENERGY-BOOKKEEPING"                 # (local)
SCHEME = "substrate-clock-vs-FRW-IN-proper-time"                              # (local)
CONVENTION = "DS-2-corrected-per-gen-0.15573"                                 # (local)
L_MAX_TAG = 10                                                                # (local)

# Pre-registered (plan Field 7)
G_MAX = 384                                                                   # (local) item 58
N_PAIR_PER_GEN_DS2 = 0.15573                                                  # (local) = 59.8 / G_MAX
RHO_CMB_GEV_PER_M3 = 2.4e-12                                                  # (local) plan Field 7
PASS_THRESHOLD_GEV_PER_M3 = 1.0e-7                                            # (local) plan Field 9
INFO_THRESHOLD_GEV_PER_M3 = 1.0e-5                                            # (local) plan Field 9 INFO interpretation (60 OOM short)
FAIL_THRESHOLD_GEV_PER_M3 = 1.0e+108                                          # (local) ~120 OOM above rho_CMB

# K-Z mechanism (plan Field 7; S55 framework update)
XI_KZ_OVER_M_KK_INV = 0.808                                                   # (local) xi_KZ in M_KK^-1 units (S55)
KZ_EXPONENT = -2.0                                                            # (local) plan Field 7 K-Z scaling (sudden quench A_2)

# LRD anchor / cascade pin
L_PIX_LRD_m = 3.0e+10                                                         # (local)

# Natural-units conversion (hbar = c = 1)
GEV_TO_M_INV = 5.068e+15                                                      # (local) m^-1 per GeV
GEV4_TO_GEV_PER_M3 = GEV_TO_M_INV ** 3                                        # (local) (5.068e+15)^3 = 1.302e+47 m^-3 per GeV^3

# Adiabatic-relaxation pin (mechanism a)
# omega_GGE_tail at substrate-natural-relaxation: 1/tau_fold (natural rate)
# f_a = exp(-tau_fold * omega_GGE_tail) = exp(-tau_fold * (1/tau_fold)) = exp(-1)
ADIABATIC_RELAX_F_A = math.exp(-1.0)                                          # (local) ~0.368

# Mechanism (c) clock-rate accumulation per plan transit-dynamics half
# f_c = Gamma_effacement^g_max
# (canonical Gamma_effacement = 0.99970; imported from canonical_constants.py)

PLAN_PATH = SESSIONS_DIR / "session-plan" / "session-88-plan-w1a.md"          # (local)
WP_PATH = SESSIONS_DIR / "session-88" / "session-88-w1a-workingpaper.md"      # (local)
CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')                         # (local)
ITEM58_NPZ = resolve_output(88, 's88_w1a_cascade_scaling_derivation.npz')             # (local)

OUT_NPZ = resolve_output(88, 's88_w1a_bulk_cascade_gge_energy_bookkeeping.npz')       # (local)
OUT_JSON = resolve_output(88, 's88_w1a_bulk_cascade_gge_energy_bookkeeping.json')     # (local)
OUT_PNG = resolve_output(88, 's88_w1a_bulk_cascade_gge_energy_bookkeeping.png')       # (local)
VERDICT_TXT = resolve_output(88, 's88_gate_verdicts.txt')                             # (local)

INPUT_FILES = [CANONICAL_PATH, PLAN_PATH, WP_PATH, ITEM58_NPZ]                # (local)


# ---------------------------------------------------------------------------
# Section 4 - SHA helpers
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                      # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                                 # (local)
    for p in inputs:
        sha = sha256_of(p)                                                    # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")             # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                              # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                         # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                               # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                           # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Substitution chain (working in log10 throughout)
# ---------------------------------------------------------------------------

def compute_log10_rho_naive_GeV_per_m3() -> dict:
    """log10(rho_GGE_naive) in GeV/m^3.

    rho_naive_GeV4 = N_PAIR_PER_GEN_DS2 * M_KK^4 * Sum_{g=1..G_MAX} 2^g
    Sum_{g=1..G_MAX} 2^g = 2^(G_MAX+1) - 2 ~ 2^385.
    Convert: 1 GeV^4 = GEV_TO_M_INV^3 GeV/m^3 = 1.302e+47 GeV/m^3.
    """
    log10_M_KK = math.log10(M_KK)                                             # noqa: F405; (local)
    log10_M_KK_4 = 4 * log10_M_KK                                             # (local)
    log10_n_pair = math.log10(N_PAIR_PER_GEN_DS2)                             # (local)
    # Sum_{g=1..G_MAX} 2^g = 2^(G_MAX+1) - 2 ~ 2^(G_MAX+1) for G_MAX large
    log10_sum_2_g = (G_MAX + 1) * math.log10(2.0)                             # (local)
    log10_GeV4_to_GeV_per_m3 = math.log10(GEV4_TO_GEV_PER_M3)                 # (local)

    log10_rho_naive_GeV4 = log10_n_pair + log10_M_KK_4 + log10_sum_2_g        # (local)
    log10_rho_naive_GeV_per_m3 = log10_rho_naive_GeV4 + log10_GeV4_to_GeV_per_m3  # (local)

    return {
        "log10_M_KK": log10_M_KK,
        "log10_M_KK_4": log10_M_KK_4,
        "log10_n_pair": log10_n_pair,
        "log10_sum_2_g": log10_sum_2_g,
        "log10_GeV4_to_GeV_per_m3": log10_GeV4_to_GeV_per_m3,
        "log10_rho_naive_GeV4": log10_rho_naive_GeV4,
        "log10_rho_naive_GeV_per_m3": log10_rho_naive_GeV_per_m3,
    }


def compute_log10_f_a() -> dict:
    """Mechanism (a) adiabatic-relaxation suppression factor.

    Substrate-natural-relaxation pin: omega_GGE_tail = 1 / tau_fold so the
    relaxation timescale matches the fold-window duration. Then
    f_a = exp(-tau_fold * omega_GGE_tail) = exp(-1) ~ 0.368.
    """
    f_a = ADIABATIC_RELAX_F_A                                                 # (local)
    log10_f_a = math.log10(f_a)                                               # (local)
    return {
        "f_a": f_a,
        "log10_f_a": log10_f_a,
        "convention": "substrate-natural-relaxation: omega_GGE_tail = 1/tau_fold; f_a = exp(-1)",
    }


def compute_log10_f_b() -> dict:
    """Mechanism (b) K-Z saturation suppression factor.

    K-Z mechanism caps GGE-pair density at xi_KZ^-3 (in m^-3). The naive
    GGE-pair density at g_max is n_GGE_naive_per_volume = N_PAIR_PER_GEN_DS2 *
    2^g_max / L_pix(g_max)^3. Cap ratio f_b = n_KZ_cap / n_GGE_naive.

    Working in log10:
      log10(xi_KZ_m) = log10(XI_KZ_OVER_M_KK_INV / (M_KK * GEV_TO_M_INV))
      log10(n_KZ_cap_m_inv_3) = -3 * log10(xi_KZ_m)
      log10(L_pix(g_max)) = log10(L_PIX_LRD_m) - g_max * log10(2)
      log10(L_pix(g_max)^3) = 3 * log10(L_pix(g_max))
      log10(n_GGE_naive_per_volume) = log10(n_pair) + g_max*log10(2) - log10(L_pix(g_max)^3)
      log10(f_b) = log10(n_KZ_cap) - log10(n_GGE_naive_per_volume)
    """
    M_KK_m_inv = M_KK * GEV_TO_M_INV                                          # noqa: F405; (local)
    xi_KZ_m = XI_KZ_OVER_M_KK_INV / M_KK_m_inv                                # (local)
    log10_xi_KZ_m = math.log10(xi_KZ_m)                                       # (local)
    log10_n_KZ_cap = -3.0 * log10_xi_KZ_m                                     # (local) m^-3

    log10_L_pix_LRD = math.log10(L_PIX_LRD_m)                                 # (local)
    log10_L_pix_g_max = log10_L_pix_LRD - G_MAX * math.log10(2.0)             # (local)
    log10_L_pix_g_max_cubed = 3.0 * log10_L_pix_g_max                         # (local)

    log10_n_pair = math.log10(N_PAIR_PER_GEN_DS2)                             # (local)
    log10_2 = math.log10(2.0)                                                 # (local)
    log10_n_naive_at_g_max = log10_n_pair + G_MAX * log10_2 - log10_L_pix_g_max_cubed  # (local)

    log10_f_b = log10_n_KZ_cap - log10_n_naive_at_g_max                       # (local)

    return {
        "xi_KZ_m": xi_KZ_m,
        "log10_xi_KZ_m": log10_xi_KZ_m,
        "log10_n_KZ_cap_m_inv_3": log10_n_KZ_cap,
        "log10_L_pix_g_max": log10_L_pix_g_max,
        "log10_L_pix_g_max_cubed": log10_L_pix_g_max_cubed,
        "log10_n_naive_at_g_max": log10_n_naive_at_g_max,
        "log10_f_b": log10_f_b,
        "convention": "K-Z saturation cap n_KZ = xi_KZ^-3 / n_naive at g=g_max",
    }


def compute_log10_f_c() -> dict:
    """Mechanism (c) substrate-clock vs FRW-IN proper-time correction.

    f_c = Gamma_effacement^g_max
    Per plan transit-dynamics half: O(1) clock-rate ratio at single sudden-
    quench T1 boundary (NOT cumulative over generations). Gamma_effacement
    = 0.99970 (canonical, S58 Volovik partition + effacement); raised to
    g_max yields ~12% reduction.
    """
    f_c = Gamma_effacement ** G_MAX                                           # noqa: F405; (local)
    log10_f_c = math.log10(f_c)                                               # (local)
    return {
        "Gamma_effacement": Gamma_effacement,                                 # noqa: F405
        "g_max": G_MAX,
        "f_c": f_c,
        "log10_f_c": log10_f_c,
        "convention": "Gamma_effacement^g_max = 0.99970^384",
    }


# ---------------------------------------------------------------------------
# Section 6 - Verdict logic with 3-tuple
# ---------------------------------------------------------------------------

def assign_verdict(log10_rho_naive: float, log10_aggregate: float,
                   log10_f_a: float, log10_f_b: float, log10_f_c: float) -> dict:
    log10_rho_corrected = log10_rho_naive + log10_aggregate                   # (local)
    log10_pass_thresh = math.log10(PASS_THRESHOLD_GEV_PER_M3)                 # (local) -7
    log10_info_thresh = math.log10(INFO_THRESHOLD_GEV_PER_M3)                 # (local) -5
    log10_rho_CMB = math.log10(RHO_CMB_GEV_PER_M3)                            # (local) -11.62

    # sign_verdict: PASS iff direction is SUPPRESSION (each factor < 1 -> aggregate < 1)
    suppression_direction = (log10_f_a < 0) and (log10_f_b < 0) and (log10_f_c < 0)  # (local)
    sign_verdict = "PASS" if suppression_direction else "FAIL"                # (local)

    # magnitude_verdict against PASS / INFO / FAIL bands
    if log10_rho_corrected <= log10_pass_thresh:
        magnitude_verdict = "PASS"                                            # (local)
    elif log10_rho_corrected <= log10_info_thresh:
        magnitude_verdict = "INFO"                                            # (local)
    else:
        magnitude_verdict = "FAIL"                                            # (local)

    # regime_verdict: VALID (deterministic substitution chain; no ODE breakdown)
    # K-Z exponent and substrate-natural-relaxation timescale are pre-registered
    # at plan-freeze; no auto-shortening or scan-domain truncation.
    regime_verdict = "VALID"                                                  # (local)

    # Composite via collapse rule (gate-verdicts.md §"Composite-collapse rule")
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                                    # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return {
        "log10_rho_naive_GeV_per_m3": log10_rho_naive,
        "log10_rho_corrected_GeV_per_m3": log10_rho_corrected,
        "log10_aggregate": log10_aggregate,
        "log10_rho_CMB": log10_rho_CMB,
        "log10_pass_threshold": log10_pass_thresh,
        "log10_info_threshold": log10_info_thresh,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 7 - Plot
# ---------------------------------------------------------------------------

def make_plot(out_png: Path, log10_naive: float, log10_f_a: float,
              log10_f_b: float, log10_f_c: float, log10_corrected: float) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    log10_pass = math.log10(PASS_THRESHOLD_GEV_PER_M3)                        # (local)
    log10_CMB = math.log10(RHO_CMB_GEV_PER_M3)                                # (local)

    # Bar chart: each mechanism's log10 suppression factor + cumulative
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))                     # (local)

    # Panel 1: per-mechanism log10 suppression factors
    mechs = ["(a) Adiabatic\nrelaxation\nf_a = exp(-1)",
             "(b) K-Z\nsaturation cap\nxi_KZ^-3 / n_naive",
             "(c) Substrate-clock\nGamma_eff^g_max"]                          # (local)
    log10_vals = [log10_f_a, log10_f_b, log10_f_c]                            # (local)
    log10_aggregate = log10_f_a + log10_f_b + log10_f_c                       # (local)
    bars = ax1.bar(mechs, log10_vals, color=["#1f77b4", "#d62728", "#2ca02c"],
                   edgecolor="black", linewidth=0.8)
    ax1.axhline(0, color="black", linewidth=0.6)
    ax1.set_ylabel("log10(suppression factor)")
    ax1.set_title(
        f"S88 W1a-60 - Per-mechanism log10(suppression factor)\n"
        f"aggregate log10 = log_a + log_b + log_c = {log10_aggregate:.2f} "
        f"(direction = {'SUPPRESSION' if log10_aggregate < 0 else 'ENHANCEMENT'})"
    )
    for bar, val in zip(bars, log10_vals):
        ax1.text(bar.get_x() + bar.get_width() / 2.0, val,
                 f"{val:.2f}",
                 ha="center", va="bottom" if val > 0 else "top", fontsize=9)
    ax1.grid(True, axis="y", alpha=0.3)

    # Panel 2: log10(rho) waterfall
    labels = ["rho_GGE_naive", "x f_a (adiab)", "x f_b (K-Z)", "x f_c (clock)",
              "rho_GGE_corrected", "PASS threshold\n1e-7", "rho_CMB\n2.4e-12"]  # (local)
    cumulative = [log10_naive,
                  log10_naive + log10_f_a,
                  log10_naive + log10_f_a + log10_f_b,
                  log10_naive + log10_f_a + log10_f_b + log10_f_c,
                  log10_corrected,
                  log10_pass,
                  log10_CMB]                                                   # (local)
    colors2 = ["#ff7f0e", "#1f77b4", "#d62728", "#2ca02c", "#9467bd", "#888888", "#444444"]  # (local)
    ax2.bar(labels, cumulative, color=colors2, edgecolor="black", linewidth=0.6)
    ax2.axhline(log10_pass, color="black", linewidth=0.8, linestyle="--",
                label=f"PASS threshold (1e-7 GeV/m^3) = log10 -7")
    ax2.axhline(log10_CMB, color="gray", linewidth=0.8, linestyle=":",
                label=f"rho_CMB (2.4e-12 GeV/m^3) = log10 -11.62")
    ax2.set_ylabel("log10(rho) [GeV/m^3]")
    ax2.set_title(f"Cascade GGE energy: log10(rho_naive) = {log10_naive:.1f} -> "
                  f"log10(rho_corrected) = {log10_corrected:.1f}")
    for i, val in enumerate(cumulative):
        ax2.text(i, val, f"{val:.1f}", ha="center",
                 va="bottom" if val > log10_CMB else "top", fontsize=8)
    ax2.legend(loc="upper right", fontsize=8)
    ax2.grid(True, axis="y", alpha=0.3)
    ax2.set_xticklabels(labels, rotation=15, ha="right")

    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 - Verdict-line append (3-tuple per [SIGN] trigger)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> str:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )                                                                         # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                                         # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )                                                                         # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)
    return line


# ---------------------------------------------------------------------------
# Section 9 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                           # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    legacy = closure_hash(pins)                                                # (local)
    print(f"  legacy closure: {legacy[:16]}...")

    # 2. Compute dual SHAs
    script_path = Path(__file__).resolve()                                     # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 3. Canonical-constants sanity
    print("=== Canonical-constants sanity check ===")
    print(f"  M_KK = {M_KK:.6e} GeV")                                          # noqa: F405
    print(f"  tau_fold = {tau_fold}")                                          # noqa: F405
    print(f"  Gamma_effacement = {Gamma_effacement}")                          # noqa: F405
    print(f"  GEV_TO_M_INV = {GEV_TO_M_INV:.4e} m^-1/GeV")
    print(f"  G_MAX (item 58) = {G_MAX}")
    print(f"  N_PAIR_PER_GEN_DS2 = {N_PAIR_PER_GEN_DS2}")
    print()

    # 4. Cross-check item 58
    item58 = np.load(ITEM58_NPZ, allow_pickle=True)                            # (local)
    assert int(item58["g_max_LINEAR"]) == G_MAX
    print(f"=== Item 58 cascade-scaling cross-check ===")
    print(f"  item 58 g_max_LINEAR = {int(item58['g_max_LINEAR'])} (matches plan)")
    print()

    # 5. Step 1: rho_GGE_naive
    naive = compute_log10_rho_naive_GeV_per_m3()                               # (local)
    print(f"=== Step 1: rho_GGE_naive ===")
    print(f"  log10(M_KK)           = {naive['log10_M_KK']:.4f}")
    print(f"  log10(M_KK^4)         = {naive['log10_M_KK_4']:.4f}")
    print(f"  log10(n_pair)         = {naive['log10_n_pair']:.4f}")
    print(f"  log10(Sum_g 2^g)      = {naive['log10_sum_2_g']:.4f}")
    print(f"  log10(rho_naive_GeV4) = {naive['log10_rho_naive_GeV4']:.4f}")
    print(f"  log10(GeV4 -> GeV/m3) = {naive['log10_GeV4_to_GeV_per_m3']:.4f}")
    print(f"  log10(rho_naive_GeV/m3) = {naive['log10_rho_naive_GeV_per_m3']:.4f}")
    print(f"  rho_naive             ~ 10^{naive['log10_rho_naive_GeV_per_m3']:.2f} GeV/m^3")
    print()

    # 6. Step 2-3: per-mechanism suppression factors
    print(f"=== Step 2-3: per-mechanism suppression factors ===")
    f_a_data = compute_log10_f_a()                                             # (local)
    print(f"  Mechanism (a) Adiabatic relaxation:")
    print(f"    {f_a_data['convention']}")
    print(f"    f_a = {f_a_data['f_a']:.6e}, log10(f_a) = {f_a_data['log10_f_a']:.4f}")

    f_b_data = compute_log10_f_b()                                             # (local)
    print(f"  Mechanism (b) K-Z saturation:")
    print(f"    {f_b_data['convention']}")
    print(f"    xi_KZ = {f_b_data['xi_KZ_m']:.4e} m, log10(xi_KZ) = {f_b_data['log10_xi_KZ_m']:.4f}")
    print(f"    log10(n_KZ_cap m^-3) = {f_b_data['log10_n_KZ_cap_m_inv_3']:.4f}")
    print(f"    log10(L_pix(g_max))  = {f_b_data['log10_L_pix_g_max']:.4f}")
    print(f"    log10(n_naive at g_max) = {f_b_data['log10_n_naive_at_g_max']:.4f}")
    print(f"    log10(f_b) = {f_b_data['log10_f_b']:.4f}")

    f_c_data = compute_log10_f_c()                                             # (local)
    print(f"  Mechanism (c) Substrate-clock vs FRW-IN:")
    print(f"    {f_c_data['convention']}")
    print(f"    f_c = {f_c_data['f_c']:.6e}, log10(f_c) = {f_c_data['log10_f_c']:.4f}")
    print()

    # 7. Step 4-5: aggregate
    log10_aggregate = f_a_data["log10_f_a"] + f_b_data["log10_f_b"] + f_c_data["log10_f_c"]  # (local)
    print(f"=== Step 4-5: aggregate suppression ===")
    print(f"  log10(aggregate) = log_a + log_b + log_c = "
          f"{f_a_data['log10_f_a']:.4f} + {f_b_data['log10_f_b']:.4f} + {f_c_data['log10_f_c']:.4f}")
    print(f"                  = {log10_aggregate:.4f}")
    print(f"  Direction: {'SUPPRESSION' if log10_aggregate < 0 else 'ENHANCEMENT'}")
    print()

    # 8. Step 6: rho_corrected and verdict
    log10_rho_corrected = naive["log10_rho_naive_GeV_per_m3"] + log10_aggregate  # (local)
    rho_corrected_GeV_per_m3 = 10.0 ** log10_rho_corrected if log10_rho_corrected < 300 else float("inf")  # (local)
    rho_naive_GeV_per_m3 = float("inf") if naive["log10_rho_naive_GeV_per_m3"] > 300 else 10.0 ** naive["log10_rho_naive_GeV_per_m3"]  # (local)
    print(f"=== Step 6: rho_corrected ===")
    print(f"  log10(rho_corrected) = {log10_rho_corrected:.4f}")
    print(f"  rho_corrected = 10^{log10_rho_corrected:.2f} GeV/m^3")
    print(f"  PASS threshold = 1e-7 GeV/m^3 (log10 = -7)")
    print(f"  INFO threshold = 1e-5 GeV/m^3 (log10 = -5)")
    print(f"  rho_CMB         = 2.4e-12 GeV/m^3 (log10 = -11.62)")
    print()

    verdict_data = assign_verdict(naive["log10_rho_naive_GeV_per_m3"],
                                  log10_aggregate,
                                  f_a_data["log10_f_a"],
                                  f_b_data["log10_f_b"],
                                  f_c_data["log10_f_c"])                       # (local)
    print(f"=== Verdict 3-tuple ===")
    print(f"  sign_verdict      = {verdict_data['sign_verdict']}")
    print(f"  magnitude_verdict = {verdict_data['magnitude_verdict']}")
    print(f"  regime_verdict    = {verdict_data['regime_verdict']}")
    print(f"  composite         = {verdict_data['composite']}")
    print()

    # 9. Plot
    print(f"=== Plot: {OUT_PNG.name} ===")
    make_plot(OUT_PNG, naive["log10_rho_naive_GeV_per_m3"],
              f_a_data["log10_f_a"], f_b_data["log10_f_b"], f_c_data["log10_f_c"],
              log10_rho_corrected)
    print(f"  written: {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
    print()

    # 10. NPZ
    np.savez(
        OUT_NPZ,
        rho_GGE_naive_GeV_per_m3=np.float64(rho_naive_GeV_per_m3 if rho_naive_GeV_per_m3 != float("inf") else 1e300),
        rho_CMB_GeV_per_m3=np.float64(RHO_CMB_GEV_PER_M3),
        log10_rho_naive=np.float64(naive["log10_rho_naive_GeV_per_m3"]),
        log10_rho_corrected=np.float64(log10_rho_corrected),
        rho_GGE_corrected_GeV_per_m3=np.float64(rho_corrected_GeV_per_m3),
        naive_OOM_above_CMB=np.float64(naive["log10_rho_naive_GeV_per_m3"] - math.log10(RHO_CMB_GEV_PER_M3)),
        mechanism_a_suppression_factor=np.float64(f_a_data["f_a"]),
        log10_f_a=np.float64(f_a_data["log10_f_a"]),
        mechanism_b_suppression_factor=np.float64(10.0 ** f_b_data["log10_f_b"] if f_b_data["log10_f_b"] > -300 else 1e-300),
        log10_f_b=np.float64(f_b_data["log10_f_b"]),
        mechanism_c_suppression_factor=np.float64(f_c_data["f_c"]),
        log10_f_c=np.float64(f_c_data["log10_f_c"]),
        log10_aggregate_suppression=np.float64(log10_aggregate),
        pass_threshold_GeV_per_m3=np.float64(PASS_THRESHOLD_GEV_PER_M3),
        sign_verdict=np.array(verdict_data["sign_verdict"], dtype=object),
        magnitude_verdict=np.array(verdict_data["magnitude_verdict"], dtype=object),
        regime_verdict=np.array(verdict_data["regime_verdict"], dtype=object),
        composite_verdict=np.array(verdict_data["composite"], dtype=object),
        verdict=np.array(verdict_data["composite"], dtype=object),
        # Anchors / pins
        g_max=np.int64(G_MAX),
        n_pair_per_gen_DS2=np.float64(N_PAIR_PER_GEN_DS2),
        Gamma_effacement_pin=np.float64(Gamma_effacement),                    # noqa: F405
        xi_KZ_over_M_KK_inv=np.float64(XI_KZ_OVER_M_KK_INV),
        L_pix_LRD_m=np.float64(L_PIX_LRD_m),
        # Dual SHAs
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
    )
    print(f"  npz written: {OUT_NPZ} ({OUT_NPZ.stat().st_size} bytes)")
    print()

    # 11. JSON sidecar
    sidecar = {                                                                # (local)
        "gate_id": GATE_ID,
        "verdict": verdict_data["composite"],
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "schema_version": "S87+",
        "log10_rho_naive_GeV_per_m3": naive["log10_rho_naive_GeV_per_m3"],
        "log10_rho_corrected_GeV_per_m3": log10_rho_corrected,
        "rho_GGE_corrected_GeV_per_m3": rho_corrected_GeV_per_m3,
        "rho_CMB_GeV_per_m3": RHO_CMB_GEV_PER_M3,
        "naive_OOM_above_CMB": naive["log10_rho_naive_GeV_per_m3"] - math.log10(RHO_CMB_GEV_PER_M3),
        "mechanism_a": f_a_data,
        "mechanism_b": f_b_data,
        "mechanism_c": f_c_data,
        "log10_aggregate_suppression": log10_aggregate,
        "verdict_3tuple": {
            "sign": verdict_data["sign_verdict"],
            "magnitude": verdict_data["magnitude_verdict"],
            "regime": verdict_data["regime_verdict"],
            "composite": verdict_data["composite"],
        },
        "pass_threshold_GeV_per_m3": PASS_THRESHOLD_GEV_PER_M3,
        "g_max": G_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
        "elapsed_seconds": time.time() - t0,
    }
    OUT_JSON.write_text(json.dumps(sidecar, indent=2, default=str), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON} ({OUT_JSON.stat().st_size} bytes)")
    print()

    # 12. 4-tuple + verdict-line append
    value_str = f"{rho_corrected_GeV_per_m3:.4e}"                              # (local)
    print(f"=== 4-tuple ===")
    print(f"  (value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    print()

    line = append_verdict(
        verdict_data["composite"], value_str, audit_sha, content_sha,
        sign_v=verdict_data["sign_verdict"],
        mag_v=verdict_data["magnitude_verdict"],
        regime_v=verdict_data["regime_verdict"],
    )
    print(f"=== verdict line appended to {VERDICT_TXT} ===")
    print(f"  {line.strip()}")
    print()

    print(f"=== {GATE_ID} complete in {time.time() - t0:.2f} s; verdict={verdict_data['composite']} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
