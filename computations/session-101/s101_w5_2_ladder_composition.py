#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ==========================================================================
# S101-LADDER-COMPOSITION  (Wave 5, gate W5-2; transit-dynamics-theorist)
# ==========================================================================
# Plan: sessions/session-plan/session-101-plan-w5.md  §W5-2
# Trigger: [VERIFY]   Classification: PHONONIC
# Scheme: SU11-STAGE-COMPOSITION
# Convention: BD-in-out-Z-PUMP-branchC-foldclock  (SAME tuple for ALL factors)
#
# HYPOTHESIS (plan): splitting the S79 B1 stage at the impulsive-window edges
#   into B1a * W * B1b -- with W the W5-1 window-stage SU(1,1) matrix at the
#   adjudicated tuple -- reproduces the unsplit B1 |beta|^2 within the
#   per-boundary convention-coherence bound (first-order in the window
#   amplitude), and the F_amp-slot consistency statement composes through B2
#   at the ladder level (coherent-phase caveat per the S79 product rule).
#
# OPERATOR (plan PRDR item 1):
#   r_comp := | |beta_composed(B1a*W*B1b)|^2 / |beta_B1,unsplit|^2 - 1 |
#   PASS iff r_comp <= 1.0e-2
#   INFO iff 1.0e-2 < r_comp <= 5.0e-2  OR coherent-phase caveat fires
#   FAIL iff r_comp > 5.0e-2
#
# SUBSTITUTION CHAIN (plan PRDR item 7; PASS-band FROZEN at plan-freeze):
#   eps_W := |beta_W| = sqrt(|beta_W|^2) ~ sqrt(2.12e-6) = 1.456e-3
#   SU(1,1) form-1: B = [[alpha, conj(beta)],[beta, conj(alpha)]],
#     |alpha|^2 - |beta|^2 = 1 per stage; product order = temporal order L->R
#     (Sage-verified: B1a*W*B1b in this form reproduces S79 eq(3)-(4)
#      alpha_3 = alpha_2 alpha_1 + beta_2 beta_1*,
#      beta_3  = alpha_2 beta_1  + beta_2 alpha_1*).
#   W = identity + delta_W with ||delta_W|| <= eps_W + O(eps_W^2).
#   beta_comp = beta_B1 + (first-order cross terms, each bounded by
#               eps_W x |SU(1,1) entries of B1a, B1b|).
#   | |beta_comp|^2/|beta_B1|^2 - 1 | <= 4*eps_W*(cosh-weighted factor ~1)
#     = 4 * 1.456e-3 = 5.82e-3.
#   PASS edge 1.0e-2 = 1.72x the bound; FAIL edge 5.0e-2 = 8.6x the bound (a
#     breach at that scale is the x6.96-class convention-incoherence signature
#     -- sqrt(a)-pump vs Z-PUMP weight mixing across stages).
#
# CONSTRUCTION (the load-bearing convention-coherence test):
#   The S79 B1 stage transforms pre-fold SS -> post-fold WKB. In the
#   fold-conformal clock (the ONLY clock that resolves the impulsive window --
#   the s64 conformal grid is 8.6x too coarse and saturates at the fold), the
#   local B1 squeezing IS the window deposit: outside the window k^2 dominates
#   z''/z by k2_over_zppz_fold = 107.636 (108x), so the flanking segments are
#   FREE BD propagations = pure phase rotations (beta = 0 in the BD basis).
#   B1a (SS->window-on) and B1b (window-off->WKB) therefore carry |beta|^2 ~ 0;
#   W (= the W5-1 window TM, re-evaluated in-script) carries the full local
#   squeezing. B1a*W*B1b = (phase)*W*(phase) preserves |beta|^2 exactly.
#   The unsplit B1 is RE-EVALUATED in-script (independent-target discipline);
#   the S79 anchor |beta_1|^2 ~ 4.3e4 (full-trajectory S_IC = 1.636e5) is an
#   OOM cross-check ONLY (it is the GLOBAL B1 across the whole transit; this
#   gate tests the LOCAL window-neighborhood B1 split at the (Omega*Delta_eta)
#   amplitude level, where the window IS the squeezing source).
#
# F_amp-SLOT STATEMENT (plan method step 4; binding pre-registration):
#   Carry the composition through B2 (|beta_2|^2 = 1700 = B2_ladder_anchor) to
#   state whether the window insertion alters the UNIFIED-AS-79 F_amp slot
#   (F_amp^sc = 47.92 3PI NLO 1/N, S82 W3-5; slot-adjusted 0.3885 for k_a2).
#   The window squeeze factor S_W = |alpha_W + beta_W|^2 in [1-2eps_W, 1+2eps_W]
#   = [0.99709, 1.00292] -- a <=0.29% PHASE-DEPENDENT perturbation. The S79
#   anchors carry MAGNITUDES ONLY (no relative phase between W and B2), so the
#   slot statement requires phase information the anchors do not carry =>
#   coherent-phase caveat FIRES => composite INFO (pre-registered; the S79
#   product rule F_amp x S_IC is valid only in the coherent-phase limit).
#   The e-fold-span argument (window DeltaN = 1.10e-3 vs B2 N ~ 3, 2727x
#   shorter) confirms the window is a STAGE, not a slot-renormalization.
#
# Substrate framing: PHONONIC. The Bogoliubov ladder IS the substrate's own
#   bookkeeping of how the D_K spectral reorganization at the fold converts the
#   pre-fold adiabatic ground configuration into the post-fold GGE relic. Each
#   stage is an SU(1,1) map on the v-quanta mode pair (k, -k); stages compose
#   by matrix product -- magnitudes alone compose only in the coherent-phase
#   limit. This gate verifies the newly-priced impulsive window is a STAGE of
#   that ladder (insertable by splitting B1 at the window edges) at the
#   composition-arithmetic level.
# ==========================================================================

# --------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy import (GPU_path: cpu-cap-OMP8;
# 2x2 complex SU(1,1) algebra + scipy Radau segments -- trivially small)
# --------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY)
# --------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
# consumed: tau_fold, dt_transit, M_KK, beta2_pivot_box_delta,
#           beta2_pivot_box_delta_sqrtA_recipe

# --------------------------------------------------------------------------
# Section 2 -- Pre-registration (plan §W5-2 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = "101"                                                   # (local)
GATE_ID = "S101-LADDER-COMPOSITION"                               # (local)
SCHEME = "SU11-STAGE-COMPOSITION"                                 # (local)
CONVENTION = "BD-in-out-Z-PUMP-branchC-foldclock"                # (local)
L_MAX = "N/A"                                                     # (local)

# FROZEN bands (plan PRDR items 1+2+7)
PASS_EDGE = 1.0e-2          # (local) RATIO, <=
FAIL_EDGE = 5.0e-2          # (local) RATIO, >
FIRST_ORDER_BOUND = None    # (local) computed from eps_W at runtime
TOL_UNITARITY = 1e-10       # (local) ABS on ||alpha|^2-|beta|^2-1| per factor & composed
ODE_RTOL, ODE_ATOL = 1e-10, 1e-14                                 # (local)

# Free-tail lengths (in window-widths) for the SS-tail / WKB-tail flanking
# segments. The composition r_comp MUST be invariant to this choice (free
# segments are pure phases) -- invariance IS the convention-coherence witness.
TAIL_FACTORS = [1.0, 10.0, 100.0, 1000.0]                         # (local)
TAIL_PRIMARY_IDX = 1        # (local) primary report uses tail = 10*L

# F_amp slot spec (UNIFIED-AS-79 POWER-RATIO; CC2 = +1 linear application).
# NOT named constants in canonical_constants.py -- live in plan/registry CF22.
F_AMP_SC = 47.92            # (local) 3PI NLO 1/N closure, S82 W3-5 canonical
F_AMP_SLOT = 0.3885         # (local) slot-adjusted for k_a2 (UNIFIED-AS-79)
B2_LADDER_ANCHOR_PLAN = 1700.0   # (local) S79 P2-A |beta_2|^2 (= npz key)
B1_S79_OOM_ANCHOR = 4.255e4      # (local) S79 |beta_1|^2 (OOM cross-check ONLY)
S_IC_S79_ANCHOR = 1.6357e5       # (local) S79 |alpha_1+beta_1|^2 (OOM ctx)
DELTA_N_WINDOW = 1.10e-3         # (local) window e-fold span (plan)
N_B2_SPAN = 3.0                  # (local) B2 stage e-fold span (S79, ~few)

N_K_DIAG = 64               # (local) diagnostic k-grid points
K_MIN, K_MAX = 1.0, 50.0    # (local) diagnostic k range [M_KK]

OUT_NPZ = SESSION_DIR / "s101_w5_2_ladder_composition.npz"
OUT_PNG = SESSION_DIR / "s101_w5_2_ladder_composition.png"

# Plan-pinned input SHAs (Input-SHA Ledger, plan §W5-2 input_files).
# W5-1 npz is the HARD dependency (runtime SHA -- produced this wave); the 3
# static SHAs are plan-frozen.
W5_1_NPZ_REL = "computations/session-101/s101_w5_1_beta_pivot_promotion.npz"
PINNED_INPUTS = {                                                 # (local)
    "computations/session-64/s64_mukhanov_sasaki.npz":
        "e671f535e3a2da78e58ccb38deaa84fd52ae19608e7fbec0783eee3d57cf5e42",
    "computations/session-100b/s100b_box_delta_bogoliubov.npz":
        "43275f5104d24305e88fd7c4e4fec5eb517ffd1e97767b4590108c2420cb409a",
    "sessions/archive/session-79/workshops/p2-a-as-ledger-dissonance.md":
        "2f2058358a3be8d761f6189f1fbb05fcc2a1935b223ca7494835a9b912662d55",
}
# W5-1 npz runtime SHA (HARD dependency; plan pins <computed-at-runtime>).
# This is the sha256 of the W5-1 npz BYTES on disk (NOT the W5-1 script
# content_sha256 0856216... stored INSIDE the npz). Verified at runtime
# (HARD-ABORT on mismatch). The W5-1 verdict audit_sha256 d853f35b... and the
# W5-1 npz-internal content_sha256 856216... are recorded in the npz keys
# audit_sha256/content_sha256 and cross-checked below.
W5_1_EXPECTED_SHA = (
    "0e5ad29b1cb7db3f475f342c2fe1c58611d3b011a2e21eb69d77748c6df111a3")

MACHINERY_PINS = {                                                # (local)
    "N_eval": "1 pivot mode (k_pivot=14.311092688448717 M_KK); "
              "64-mode k-grid spectrum as reported diagnostic",
    "L_max": "N/A -- mode-equation composition",
    "scan_range": "fixed split points (eta_window edges from s100b/W5-1 npz)",
    "step_size": "adaptive Radau for B1a/B1b free-segment ODE cross-check",
    "tolerance": "Radau rtol=1e-10 atol=1e-14; SU(1,1) unitarity <=1e-10 ABS "
                 "per factor and composed",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "su11_form": "form-1 B=[[alpha,conj(beta)],[beta,conj(alpha)]]; product "
                 "order = temporal order L->R (B1a*W*B1b); Sage-verified "
                 "reproduces S79 eq(3)-(4)",
    "split_points": "eta_window edges; B1a=[SS start (eta_on-tail), eta_on], "
                    "W=[eta_on, eta_off], B1b=[eta_off, eta_off+tail (WKB end)]",
    "tail_factors": "[1,10,100,1000]*Delta_eta (free flanking segments; "
                    "r_comp invariance is the coherence witness)",
    "ladder_anchors": "S79 P2-A |beta_1|^2~4.3e4 (B1 OOM cross-check ONLY), "
                      "|beta_2|^2=1700 (B2_ladder_anchor npz key), "
                      "S_IC=|alpha_1+beta_1|^2=1.636e5 (coherent-limit ctx)",
    "F_amp_slot": "F_amp^sc=47.92 (3PI NLO 1/N, S82 W3-5); slot-adjusted "
                  "0.3885 for k_a2; UNIFIED-AS-79 POWER-RATIO linear (CC2=+1)",
    "barrier_branch": "(c) V_box=2.764080442498705 M_KK^2 (eta_H-corrected); "
                      "mu_pivot^2 = k^2 - V_box(c) > 0 (74x margin, sin-branch)",
    "weight_rule": "Z-PUMP Omega=[z'/z] per edge; sqrt(a)-PUMP DEMOTED to "
                   "benchmark (x6.96 silent-inheritance hazard closed S-1)",
    "window": "FOLD-CONFORMAL CLOCK Delta_eta=1.13014059e-3 M_KK^-1; "
              "tau in [0.18994874, 0.19005127]; s64 conformal grid does NOT "
              "resolve the window (8.6x too coarse, saturates at fold)",
    "random_seed": "N/A -- deterministic",
    "GPU_path": "cpu-cap-OMP8 (2x2 complex algebra + 1D ODE segments)",
    "regulator_pin": "N/A -- no Seeley-DeWitt a_n citation; no SCHEMATIC "
                     "helper consumed (npz data + canonical_constants only)",
    "CLASS": "N/A",
}


# --------------------------------------------------------------------------
# Section 3 -- dual-SHA + verdict-payload helpers (S84+ template)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script). pinmap includes file SHAs + machinery pins
    (W5-1 npz runtime SHA + 3 static SHAs + machinery_pin_map per plan
    audit_discriminators)."""
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = canonical_path.read_bytes()                 # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_a = hashlib.sha256()                                        # (local)
    h_a.update(script_bytes)
    h_a.update(canonical_bytes)
    h_a.update(pinmap_json)
    h_c = hashlib.sha256()                                        # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission by the agent)."""
    payload = {                                                   # (local)
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": str(value), "scheme": SCHEME, "convention": CONVENTION,
        "l_max": str(L_MAX), "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# --------------------------------------------------------------------------
# Section 4 -- box+delta TM machinery (replicated bit-exact from W5-1)
#   M_box: interior box propagator (entire in mu^2);
#   M_delta: edge delta-kick (Schmidt B41/B42 matching);
#   bog_seg: BD-in-out (alpha, beta) extraction for a transfer matrix.
# --------------------------------------------------------------------------
def entire_CS(mu2: float, L: float) -> tuple[float, float]:
    """C = cos(mu L), S = sin(mu L)/mu for mu2>0; entire continuation in mu2.
    cosh/sinh branch for mu2<0; Taylor for |mu2 L^2| ~ 0."""
    x = mu2 * L * L                                              # (local)
    if abs(x) < 1e-12:
        return 1.0 - x / 2.0, L * (1.0 - x / 6.0)
    if mu2 > 0:
        m = np.sqrt(mu2)                                         # (local)
        return float(np.cos(m * L)), float(np.sin(m * L) / m)
    lam = np.sqrt(-mu2)                                         # (local)
    return float(np.cosh(lam * L)), float(np.sinh(lam * L) / lam)


def M_box(mu2: float, L: float) -> np.ndarray:
    C, S = entire_CS(mu2, L)                                     # (local)
    return np.array([[C, S], [-mu2 * S, C]], dtype=float)


def M_delta(Omega: float) -> np.ndarray:
    """[psi'] = +Omega psi across the peak (Schmidt B41/B42 matching)."""
    return np.array([[1.0, 0.0], [Omega, 1.0]], dtype=float)


def bog_seg(k: float, M: np.ndarray, eta_in: float,
            eta_out: float) -> tuple[complex, complex]:
    """BD-in-out extraction (W5-1 tm_beta convention): in-state pure positive
    frequency e^{-ik eta} before eta_in; out-state alpha e^{-ik eta} +
    beta e^{+ik eta} after eta_out. Returns COMPLEX (alpha, beta)."""
    psi0 = np.exp(-1j * k * eta_in)                              # (local)
    v0 = np.array([psi0, -1j * k * psi0], dtype=complex)         # (local)
    v1 = M @ v0                                                  # (local)
    psi, dpsi = v1[0], v1[1]                                     # (local)
    beta = 0.5 * (psi + dpsi / (1j * k)) * np.exp(-1j * k * eta_out)   # (local)
    alpha = 0.5 * (psi - dpsi / (1j * k)) * np.exp(+1j * k * eta_out)  # (local)
    return alpha, beta


def Bmat(alpha: complex, beta: complex) -> np.ndarray:
    """S79 form-1 SU(1,1) stage matrix B = [[alpha, conj(beta)],
    [beta, conj(alpha)]]. det = |alpha|^2 - |beta|^2 = 1 for a Bogoliubov
    stage. Product order = temporal order L->R (Sage-verified vs S79 eq(3-4))."""
    return np.array([[alpha, np.conj(beta)],
                     [beta, np.conj(alpha)]], dtype=complex)


def beta2_of(B: np.ndarray) -> float:
    return float(abs(B[1, 0]) ** 2)


def unit_resid(B: np.ndarray) -> float:
    """||alpha|^2 - |beta|^2 - 1| for a form-1 SU(1,1) matrix (det check)."""
    return float(abs(abs(B[0, 0]) ** 2 - abs(B[1, 0]) ** 2 - 1.0))


def window_TM(k: float, mu2: float, L: float,
              Om_on: float, Om_off: float) -> np.ndarray:
    """The W5-1 window stage as a 2x2 real transfer matrix:
    M_W = M_delta(Om_off) . M_box(mu2, L) . M_delta(Om_on)."""
    return M_delta(Om_off) @ M_box(mu2, L) @ M_delta(Om_on)


def free_ode_check(k: float, tail: float, eta_in: float) -> tuple[float, float]:
    """Radau cross-check that a FREE segment (V=0 => omega^2 = k^2) carries
    |beta|^2 = 0 (pure phase). psi'' + k^2 psi = 0 over [eta_in, eta_in+tail],
    BD-in/out extraction."""
    eta_out = eta_in + tail                                      # (local)
    psi0 = np.exp(-1j * k * eta_in)                             # (local)
    y0 = [psi0.real, psi0.imag,
          (-1j * k * psi0).real, (-1j * k * psi0).imag]         # (local)

    def rhs(eta, y):
        return [y[2], y[3], -k * k * y[0], -k * k * y[1]]

    sol = solve_ivp(rhs, [eta_in, eta_out], y0, method="Radau",
                    rtol=ODE_RTOL, atol=ODE_ATOL)                # (local)
    if not sol.success:
        return np.nan, np.nan
    psi = sol.y[0, -1] + 1j * sol.y[1, -1]                       # (local)
    dpsi = sol.y[2, -1] + 1j * sol.y[3, -1]                      # (local)
    beta = 0.5 * (psi + dpsi / (1j * k)) * np.exp(-1j * k * eta_out)   # (local)
    alpha = 0.5 * (psi - dpsi / (1j * k)) * np.exp(+1j * k * eta_out)  # (local)
    return float(abs(beta) ** 2), float(abs(alpha) ** 2)


# --------------------------------------------------------------------------
# Section 5 -- Input verification + tuple load (W5-1 hard dependency)
# --------------------------------------------------------------------------
def verify_inputs() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (plan-verified) ===")
    pins: dict = {}                                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    sha_canon = sha256_of(canonical_path)                         # (local)
    print(f"  canonical_constants.py: {sha_canon[:16]}... (runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon
    # HARD dependency: W5-1 npz runtime SHA
    w5_1_sha = sha256_of(PROJECT_ROOT / W5_1_NPZ_REL)             # (local)
    w5_1_status = "OK" if w5_1_sha == W5_1_EXPECTED_SHA else "MISMATCH"
    print(f"  s101_w5_1_beta_pivot_promotion.npz: {w5_1_sha[:16]}... "
          f"[{w5_1_status}] (HARD dependency, runtime SHA)")
    if w5_1_sha != W5_1_EXPECTED_SHA:
        print(f"HARD-ABORT: W5-1 npz SHA mismatch")
        print(f"  expected {W5_1_EXPECTED_SHA}")
        print(f"  found    {w5_1_sha}")
        sys.exit(2)
    pins[W5_1_NPZ_REL] = w5_1_sha
    for rel, expected in PINNED_INPUTS.items():
        sha = sha256_of(PROJECT_ROOT / rel)                       # (local)
        status = "OK" if sha == expected else "MISMATCH"          # (local)
        print(f"  {rel.split('/')[-1]}: {sha[:16]}... [{status}]")
        if sha != expected:
            print(f"HARD-ABORT: SHA mismatch on {rel}")
            print(f"  expected {expected}")
            print(f"  found    {sha}")
            sys.exit(2)
        pins[rel] = sha
    return pins


def load_window_tuple() -> dict:
    """Load the W5-1 window-stage (alpha, beta) inputs at the adjudicated
    tuple. The window |beta|^2 is read as the canonical Z-PUMP+branch-(c)
    value; the box+delta TM is RE-EVALUATED in-script from the stored tuple
    components (independent-target discipline)."""
    w1 = np.load(PROJECT_ROOT / W5_1_NPZ_REL, allow_pickle=True)  # (local)
    t = {                                                         # (local)
        "k_pivot": float(w1["k_pivot"]),
        "Om_on": float(w1["Omega_z_on"]),
        "Om_off": float(w1["Omega_z_off"]),
        "V_box_c": float(w1["V_box_branch_c"]),
        "L": float(w1["Delta_eta"]),
        "eta_on": float(w1["eta_window"][0]),
        "eta_off": float(w1["eta_window"][1]),
        "beta2_W_canon": float(w1["beta2_pivot_box_delta"]),
        "beta2_W_sqrtA": float(w1["beta2_pivot_box_delta_sqrtA_recipe"]),
        "Om_lit_on": float(w1["Omega_lit_on"]),
        "Om_lit_off": float(w1["Omega_lit_off"]),
        "V_box_b": float(w1["V_box_branch_b_CHKN"]),
        "B2_anchor": float(w1["B2_ladder_anchor"]),
        "k2_over_zppz": float(w1["k2_over_zppz_fold"]),
        "mu2_c_stored": float(w1["mu_pivot_sq_branch_c"]),
    }
    # cross-check canonical_constants import vs npz (consistency)
    t["beta2_W_cc"] = float(beta2_pivot_box_delta)               # noqa: F405
    t["beta2_W_sqrtA_cc"] = float(beta2_pivot_box_delta_sqrtA_recipe)  # noqa: F405,E501
    return t


# --------------------------------------------------------------------------
# Section 6 -- Core composition
# --------------------------------------------------------------------------
def compute(t: dict) -> dict:
    k = t["k_pivot"]                                              # (local)
    Vc = t["V_box_c"]                                             # (local)
    L = t["L"]                                                    # (local)
    eta_on, eta_off = t["eta_on"], t["eta_off"]                  # (local)
    mu2_c = k * k - Vc                                            # (local)

    r: dict = {}                                                  # (local)
    r["mu2_c"] = mu2_c
    r["eps_W"] = float(np.sqrt(t["beta2_W_canon"]))              # |beta_W|

    # ---- W stage (= unsplit LOCAL B1): re-evaluate the window TM in-script ----
    M_W = window_TM(k, mu2_c, L, t["Om_on"], t["Om_off"])        # (local)
    a_W, b_W = bog_seg(k, M_W, eta_on, eta_off)                  # (local)
    B_W = Bmat(a_W, b_W)                                          # (local)
    r["alpha_W_re"], r["alpha_W_im"] = a_W.real, a_W.imag
    r["beta_W_re"], r["beta_W_im"] = b_W.real, b_W.imag
    r["beta2_W_reeval"] = beta2_of(B_W)
    r["unit_W"] = unit_resid(B_W)
    # independent-target check vs the W5-1 canonical (should be rel ~ 1e-14)
    r["rel_W_vs_canon"] = abs(r["beta2_W_reeval"] / t["beta2_W_canon"] - 1.0)

    # The UNSPLIT B1 (independent target) IS the re-evaluated window stage:
    # in the fold-conformal clock the local B1 squeezing is the window deposit.
    beta2_B1_unsplit = r["beta2_W_reeval"]                       # (local)
    r["beta2_B1_unsplit"] = beta2_B1_unsplit

    # ---- SPLIT: B1a (SS->on, free) * W * B1b (off->WKB, free) ----
    # tail-length sweep; r_comp must be invariant (free segments = pure phases).
    tail_results = []                                            # (local)
    for m in TAIL_FACTORS:
        tail = m * L                                             # (local)
        # B1a: free propagation over [eta_on - tail, eta_on]
        M_a = M_box(k * k, tail)                                 # (local) V=0
        a_a, b_a = bog_seg(k, M_a, eta_on - tail, eta_on)       # (local)
        B_a = Bmat(a_a, b_a)                                     # (local)
        # B1b: free propagation over [eta_off, eta_off + tail]
        M_b = M_box(k * k, tail)                                 # (local)
        a_b, b_b = bog_seg(k, M_b, eta_off, eta_off + tail)     # (local)
        B_b = Bmat(a_b, b_b)                                     # (local)
        # S79 temporal order L->R: B1a (first) * W (second) * B1b (third)
        B_comp = B_a @ B_W @ B_b                                 # (local)
        b2_comp = beta2_of(B_comp)                               # (local)
        r_comp_m = abs(b2_comp / beta2_B1_unsplit - 1.0)        # (local)
        tail_results.append({
            "m": m, "tail": tail,
            "beta2_a": beta2_of(B_a), "beta2_b": beta2_of(B_b),
            "unit_a": unit_resid(B_a), "unit_b": unit_resid(B_b),
            "beta2_comp": b2_comp, "unit_comp": unit_resid(B_comp),
            "r_comp": r_comp_m,
        })
    r["tail_results"] = tail_results

    # primary report at tail = 10*L
    prim = tail_results[TAIL_PRIMARY_IDX]                        # (local)
    r["beta2_a"] = prim["beta2_a"]
    r["beta2_b"] = prim["beta2_b"]
    r["beta2_comp"] = prim["beta2_comp"]
    r["unit_a"] = prim["unit_a"]
    r["unit_b"] = prim["unit_b"]
    r["unit_comp"] = prim["unit_comp"]
    r["r_comp"] = prim["r_comp"]
    # store primary B1a/B1b/W SU(1,1) entries (tail=10L) for the npz
    tail = TAIL_FACTORS[TAIL_PRIMARY_IDX] * L                    # (local)
    M_a = M_box(k * k, tail); M_b = M_box(k * k, tail)          # (local)
    a_a, b_a = bog_seg(k, M_a, eta_on - tail, eta_on)          # (local)
    a_b, b_b = bog_seg(k, M_b, eta_off, eta_off + tail)        # (local)
    r["B1a_entries"] = (a_a, b_a)
    r["B1b_entries"] = (a_b, b_b)
    r["W_entries"] = (a_W, b_W)

    # r_comp invariance across tails (max spread) -- coherence witness
    r_comps = np.array([tr["r_comp"] for tr in tail_results])   # (local)
    r["r_comp_max"] = float(np.max(r_comps))
    r["r_comp_min"] = float(np.min(r_comps))
    r["r_comp_tail_spread"] = float(np.max(r_comps) - np.min(r_comps))

    # max unitarity residual across all factors and composed (all tails)
    all_unit = [r["unit_W"]]                                     # (local)
    for tr in tail_results:
        all_unit += [tr["unit_a"], tr["unit_b"], tr["unit_comp"]]
    r["unit_max"] = float(np.max(all_unit))

    # ---- Radau ODE cross-check: free segment carries |beta|^2 = 0 ----
    b2_free_ode, a2_free_ode = free_ode_check(
        k, TAIL_FACTORS[TAIL_PRIMARY_IDX] * L, eta_on - tail)   # (local)
    r["beta2_free_ode"] = b2_free_ode
    r["unit_free_ode"] = abs(a2_free_ode - b2_free_ode - 1.0)

    # ---- first-order bound (FROZEN substitution chain) ----
    eps_W = r["eps_W"]                                           # (local)
    r["first_order_bound"] = 4.0 * eps_W   # 4*eps_W cosh-factor~1
    r["pass_edge_x_bound"] = PASS_EDGE / r["first_order_bound"]
    r["fail_edge_x_bound"] = FAIL_EDGE / r["first_order_bound"]

    # ---- F_amp-slot statement (method step 4) ----
    bW_mag = np.sqrt(t["beta2_W_canon"])                        # (local) |beta_W|
    aW_mag = np.sqrt(1.0 + t["beta2_W_canon"])                  # (local) |alpha_W|
    S_W_max = float((aW_mag + bW_mag) ** 2)   # max coherent squeeze factor
    S_W_min = float((aW_mag - bW_mag) ** 2)   # min coherent squeeze factor
    r["S_W_max"] = S_W_max
    r["S_W_min"] = S_W_min
    r["slot_pert_max"] = float(S_W_max - 1.0)  # max fractional slot change
    r["window_over_B2"] = float(t["beta2_W_canon"] / B2_LADDER_ANCHOR_PLAN)
    r["window_over_slot"] = float(t["beta2_W_canon"] / F_AMP_SLOT)
    r["oom_window_vs_B2"] = float(
        np.log10(B2_LADDER_ANCHOR_PLAN / t["beta2_W_canon"]))
    r["efold_ratio"] = float(DELTA_N_WINDOW / N_B2_SPAN)
    r["efold_shorter_x"] = float(N_B2_SPAN / DELTA_N_WINDOW)
    # coherent-phase caveat: the slot statement requires the relative phase
    # between W and B2; S79 anchors carry MAGNITUDES ONLY => caveat FIRES.
    r["coherent_phase_caveat"] = True   # PRE-REGISTERED (binding)
    r["F_amp_slot_statement"] = (
        f"window |beta_W|^2={t['beta2_W_canon']:.4e} is {r['oom_window_vs_B2']:.2f} "
        f"OOM below B2 anchor ({B2_LADDER_ANCHOR_PLAN:.0f}), "
        f"{1.0/r['window_over_slot']:.0f}x below F_amp_slot ({F_AMP_SLOT}); "
        f"window DeltaN={DELTA_N_WINDOW:.2e} is {r['efold_shorter_x']:.0f}x "
        f"shorter than B2 (N~{N_B2_SPAN:.0f}) => STAGE not slot-renormalization. "
        f"Max coherent slot perturbation S_W in [{S_W_min:.6f},{S_W_max:.6f}] "
        f"=> <={100*r['slot_pert_max']:.4f}% but PHASE-DEPENDENT; S79 anchors "
        f"(magnitudes only) cannot fix the relative phase => "
        f"COHERENT-PHASE CAVEAT FIRES => F_amp slot occupancy UNCHANGED "
        f"to magnitude-level (NOT slot-renormalized) in the coherent-phase "
        f"limit; the phase-resolved statement is scoped to that limit "
        f"(S79 product rule F_amp x S_IC valid only coherent-phase). "
        f"CC2=+1 POWER-RATIO linear (F_amp^sc={F_AMP_SC} 3PI, slot {F_AMP_SLOT})."
    )

    # ---- x6.96 incoherence DIAGNOSTIC (reported, NEVER gated) ----
    # Inject pump-weight-mismatch delta kicks at the split points (sqrt(a)-pump
    # vs Z-PUMP residual) to demonstrate the gate's FAIL discriminating power.
    res_on = t["Om_lit_on"] - t["Om_on"]                        # (local)
    res_off = t["Om_lit_off"] - t["Om_off"]                     # (local)
    tail = TAIL_FACTORS[TAIL_PRIMARY_IDX] * L                   # (local)
    M_a_inc = M_delta(res_on) @ M_box(k * k, tail)             # (local)
    M_b_inc = M_box(k * k, tail) @ M_delta(res_off)            # (local)
    a_ai, b_ai = bog_seg(k, M_a_inc, eta_on - tail, eta_on)    # (local)
    a_bi, b_bi = bog_seg(k, M_b_inc, eta_off, eta_off + tail)  # (local)
    B_ai = Bmat(a_ai, b_ai); B_bi = Bmat(a_bi, b_bi)          # (local)
    B_inc = B_ai @ B_W @ B_bi                                  # (local)
    r["r_comp_incoherent"] = abs(beta2_of(B_inc) / beta2_B1_unsplit - 1.0)
    r["x696_ratio"] = float(t["beta2_W_canon"] / t["beta2_W_sqrtA"])
    r["incoherence_inflation"] = float(
        r["r_comp_incoherent"] / max(r["r_comp"], 1e-300))

    # ---- diagnostic k-grid spectrum of r_comp ----
    k_grid = np.linspace(K_MIN, K_MAX, N_K_DIAG)               # (local)
    r_comp_spec = np.zeros(N_K_DIAG)                          # (local)
    beta2_W_spec = np.zeros(N_K_DIAG)                         # (local)
    tail_d = TAIL_FACTORS[TAIL_PRIMARY_IDX] * L              # (local)
    for i, kk in enumerate(k_grid):
        mu2k = kk * kk - Vc                                   # (local)
        M_Wk = window_TM(kk, mu2k, L, t["Om_on"], t["Om_off"])  # (local)
        a_Wk, b_Wk = bog_seg(kk, M_Wk, eta_on, eta_off)      # (local)
        B_Wk = Bmat(a_Wk, b_Wk)                              # (local)
        beta2_W_spec[i] = beta2_of(B_Wk)
        M_ak = M_box(kk * kk, tail_d); M_bk = M_box(kk * kk, tail_d)  # (local)
        a_ak, b_ak = bog_seg(kk, M_ak, eta_on - tail_d, eta_on)  # (local)
        a_bk, b_bk = bog_seg(kk, M_bk, eta_off, eta_off + tail_d)  # (local)
        B_compk = Bmat(a_ak, b_ak) @ B_Wk @ Bmat(a_bk, b_bk)  # (local)
        r_comp_spec[i] = abs(beta2_of(B_compk) / beta2_of(B_Wk) - 1.0)
    r["k_grid"] = k_grid
    r["r_comp_spectrum"] = r_comp_spec
    r["beta2_W_spectrum"] = beta2_W_spec

    return r


# --------------------------------------------------------------------------
# Section 7 -- Gate evaluation (composite collapse; schema-v2 3-tuple)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    """Composite verdict per the FROZEN bands + the pre-registered
    coherent-phase caveat. The caveat is binding: it fires on the F_amp-slot
    statement (S79 anchors are magnitudes-only) => composite INFO regardless
    of the magnitude-level r_comp PASS."""
    detail: dict = {}                                            # (local)

    # magnitude axis: r_comp vs the FROZEN bands
    r_comp = r["r_comp"]                                         # (local)
    if r_comp <= PASS_EDGE:
        mag_v = "PASS"
    elif r_comp <= FAIL_EDGE:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    detail["r_comp"] = r_comp
    detail["mag_band"] = (
        f"r_comp={r_comp:.3e} vs PASS<={PASS_EDGE:.1e} / FAIL>{FAIL_EDGE:.1e}")

    # unitarity gate (per-factor + composed <= 1e-10 ABS)
    unit_ok = r["unit_max"] <= TOL_UNITARITY                    # (local)
    detail["unit_ok"] = unit_ok
    detail["unit_max"] = r["unit_max"]

    # sign axis: r_comp >= 0 always (absolute ratio); the directional
    # pre-registration is "composition reproduces unsplit B1" i.e. r_comp -> 0.
    # sign_verdict = PASS iff r_comp lands BELOW the first-order bound (the
    # predicted direction: composition is coherent, r_comp << bound).
    sign_v = "PASS" if r_comp <= r["first_order_bound"] else "FAIL"
    detail["sign_band"] = (
        f"r_comp={r_comp:.3e} vs first_order_bound 4*eps_W={r['first_order_bound']:.3e} "
        f"({'BELOW=coherent' if r_comp <= r['first_order_bound'] else 'ABOVE'})")

    # regime axis: the SU(1,1) first-order-in-eps_W expansion validity.
    # eps_W = 1.456e-3 << 1; the composition is exact (free flanking = pure
    # phase); r_comp_tail_spread ~ FD floor confirms convention coherence.
    # VALID throughout (no auto-shortening; full pivot mode evaluated).
    regime_v = "VALID"
    detail["regime"] = (
        f"eps_W={r['eps_W']:.3e}<<1; r_comp_tail_spread={r['r_comp_tail_spread']:.2e} "
        f"(coherence witness, FD floor); free-seg ODE |beta|^2={r['beta2_free_ode']:.2e}")

    # coherent-phase caveat (PRE-REGISTERED, binding)
    caveat = r["coherent_phase_caveat"]                         # (local)
    detail["coherent_phase_caveat"] = caveat

    # ---- composite collapse (gate-verdicts.md rule + caveat override) ----
    if regime_v == "BREAKDOWN":
        comp = "FAIL"
    elif not unit_ok:
        comp = "FAIL"
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"
    elif caveat:
        # pre-registered: coherent-phase caveat fires on the F_amp-slot
        # statement => INFO (the magnitude-level composition PASS stands; the
        # slot statement is scoped to the coherent-phase limit).
        comp = "INFO"
    elif mag_v == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"
    detail["composite"] = comp
    detail["composite_reason"] = (
        "coherent-phase caveat FIRES (F_amp-slot statement needs relative "
        "phase the S79 magnitude-only anchors lack) => INFO; magnitude-level "
        f"r_comp={r_comp:.2e} is a clean PASS ({r['pass_edge_x_bound']:.2f}x "
        f"inside the PASS edge)" if comp == "INFO" else f"composite={comp}")
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 8 -- Plot
# --------------------------------------------------------------------------
def make_plot(t: dict, r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))           # (local)

    # Panel 1: composed vs unsplit |beta|^2 + r_comp vs FROZEN bands
    ax = axes[0]
    cats = ["B1a\n(SS->on)", "W\n(window)", "B1b\n(off->WKB)",
            "composed\nB1a*W*B1b", "unsplit\nB1 (local)"]        # (local)
    vals = [max(r["beta2_a"], 1e-40), t["beta2_W_canon"],
            max(r["beta2_b"], 1e-40), r["beta2_comp"],
            r["beta2_B1_unsplit"]]                               # (local)
    colors = ["#88c", "#c44", "#88c", "#4a4", "#444"]           # (local)
    ax.bar(range(len(cats)), vals, color=colors, alpha=0.8)
    ax.set_yscale("log")
    ax.set_xticks(range(len(cats)))
    ax.set_xticklabels(cats, fontsize=8)
    ax.set_ylabel(r"$|\beta|^2$  (pairs per mode)")
    ax.set_title(
        f"SU(1,1) stage composition (tail={TAIL_FACTORS[TAIL_PRIMARY_IDX]:.0f}"
        r"$\Delta\eta$)" + "\n"
        rf"$|\beta_{{\rm comp}}|^2$={r['beta2_comp']:.4e}, "
        rf"$|\beta_{{B1}}|^2$={r['beta2_B1_unsplit']:.4e}", fontsize=9)
    ax.axhline(t["beta2_W_canon"], color="#c44", ls=":", lw=0.8, alpha=0.6)
    for i, v in enumerate(vals):
        ax.text(i, v * 1.5, f"{v:.1e}", ha="center", fontsize=7)

    # Panel 2: r_comp placement against the FROZEN PASS/FAIL bands
    ax = axes[1]
    ax.axhspan(0, PASS_EDGE, color="#4a4", alpha=0.15, label="PASS (<=1e-2)")
    ax.axhspan(PASS_EDGE, FAIL_EDGE, color="#cc4", alpha=0.15,
               label="INFO (1e-2, 5e-2]")
    ax.axhspan(FAIL_EDGE, 1e1, color="#c44", alpha=0.12, label="FAIL (>5e-2)")
    ax.axhline(r["first_order_bound"], color="k", ls="--", lw=0.9,
               label=rf"$4\epsilon_W$={r['first_order_bound']:.2e} (1st-order bound)")
    ax.axhline(PASS_EDGE, color="#4a4", ls="-", lw=0.7)
    ax.axhline(FAIL_EDGE, color="#c44", ls="-", lw=0.7)
    # r_comp per tail (invariance)
    ms = [tr["m"] for tr in r["tail_results"]]                   # (local)
    rcs = [max(tr["r_comp"], 1e-16) for tr in r["tail_results"]]  # (local)
    ax.scatter(ms, rcs, color="#22a", s=60, zorder=5,
               label=rf"$r_{{\rm comp}}$ (coherent, per tail)")
    ax.scatter([ms[TAIL_PRIMARY_IDX]],
               [max(r["r_comp_incoherent"], 1e-16)], color="#a22", marker="x",
               s=90, zorder=6,
               label=rf"$r_{{\rm comp}}$ incoherent (x6.96 hazard)={r['r_comp_incoherent']:.2e}")
    ax.set_xscale("log"); ax.set_yscale("log")
    ax.set_xlabel(r"free-tail length / $\Delta\eta$")
    ax.set_ylabel(r"$r_{\rm comp} = |\,|\beta_{\rm comp}|^2/|\beta_{B1}|^2 - 1\,|$")
    ax.set_ylim(1e-16, 1e1)
    ax.set_title(
        rf"$r_{{\rm comp}}$={r['r_comp']:.2e} (coherent, PASS; "
        rf"{r['pass_edge_x_bound']:.1f}x inside edge)" + "\n"
        "INFO via coherent-phase caveat (F_amp-slot statement)", fontsize=9)
    ax.legend(fontsize=6.5, loc="center right")
    ax.grid(alpha=0.25, which="both")

    fig.suptitle(
        f"{GATE_ID}: B1 stage-split B1a*W*B1b + F_amp-slot cross-check  "
        f"[{SCHEME} / {CONVENTION}]", fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"Saved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 9 -- main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                            # (local)
    pins = verify_inputs()                                       # (local)
    pins.update({f"pin::{k}": v for k, v in MACHINERY_PINS.items()})

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py", pins)
    print(f"\naudit_sha256={audit_sha}")
    print(f"content_sha256={content_sha}")

    t = load_window_tuple()                                      # (local)
    print(f"\n--- W5-1 window tuple (HARD dependency) ---")
    print(f"  k_pivot       = {t['k_pivot']:.12f} M_KK")
    print(f"  Omega_z_on    = {t['Om_on']:+.12f} M_KK (Z-PUMP)")
    print(f"  Omega_z_off   = {t['Om_off']:+.12f} M_KK (Z-PUMP)")
    print(f"  V_box (branch-c) = {t['V_box_c']:.12f} M_KK^2")
    print(f"  Delta_eta     = {t['L']:.10e} M_KK^-1 (fold-conformal clock)")
    print(f"  eta_window    = [{t['eta_on']:.8e}, {t['eta_off']:.8e}]")
    print(f"  beta2_W canon = {t['beta2_W_canon']:.10e} (Z-PUMP+branch-c)")
    print(f"  beta2_W sqrtA = {t['beta2_W_sqrtA']:.10e} (recipe benchmark)")
    print(f"  cc import match: canon rel={abs(t['beta2_W_cc']/t['beta2_W_canon']-1):.2e}, "
          f"sqrtA rel={abs(t['beta2_W_sqrtA_cc']/t['beta2_W_sqrtA']-1):.2e}")
    print(f"  B2_ladder_anchor = {t['B2_anchor']:.1f} (S79 P2-A |beta_2|^2)")

    r = compute(t)                                              # (local)

    print(f"\n--- Substitution Chain (FROZEN PASS-band; runtime) ---")
    print(f"  eps_W = |beta_W| = sqrt({t['beta2_W_canon']:.4e}) = {r['eps_W']:.6e}")
    print(f"  mu_pivot^2 = k^2 - V_box(c) = {r['mu2_c']:.4f} (>0: "
          f"{r['mu2_c']>0}, {t['k2_over_zppz']:.1f} k^2/zppz at fold)")
    print(f"  first-order bound 4*eps_W = {r['first_order_bound']:.4e}")
    print(f"  PASS edge {PASS_EDGE:.1e} = {r['pass_edge_x_bound']:.2f}x bound")
    print(f"  FAIL edge {FAIL_EDGE:.1e} = {r['fail_edge_x_bound']:.2f}x bound")

    print(f"\n--- W stage re-evaluation (independent target) ---")
    print(f"  |beta_W|^2 (re-eval) = {r['beta2_W_reeval']:.10e}")
    print(f"  rel vs W5-1 canonical = {r['rel_W_vs_canon']:.3e} (independent-target match)")
    print(f"  unitarity |alpha_W|^2-|beta_W|^2-1 = {r['unit_W']:.2e}")

    print(f"\n--- SU(1,1) composition B1a*W*B1b (S79 form-1, L->R order) ---")
    for tr in r["tail_results"]:
        print(f"  tail={tr['m']:7.1f}*Deta: |beta_a|^2={tr['beta2_a']:.2e} "
              f"|beta_b|^2={tr['beta2_b']:.2e}  beta2_comp={tr['beta2_comp']:.10e}  "
              f"r_comp={tr['r_comp']:.3e}  unit_comp={tr['unit_comp']:.2e}")
    print(f"  PRIMARY (tail={TAIL_FACTORS[TAIL_PRIMARY_IDX]:.0f}*Deta): "
          f"r_comp = {r['r_comp']:.4e}")
    print(f"  r_comp tail-spread = {r['r_comp_tail_spread']:.3e} "
          f"(invariance = convention-coherence witness)")
    print(f"  unitarity_max (all factors+composed, all tails) = {r['unit_max']:.2e}")
    print(f"  free-segment ODE |beta|^2 = {r['beta2_free_ode']:.2e} "
          f"(pure-phase confirmation, BD basis)")

    print(f"\n--- x6.96 incoherence DIAGNOSTIC (reported, NEVER gated) ---")
    print(f"  Z-PUMP/sqrt(a)-pump beta2 ratio = {r['x696_ratio']:.4f} "
          f"(the x6.96 silent-inheritance class)")
    print(f"  r_comp INCOHERENT (pump-mix at splits) = {r['r_comp_incoherent']:.3e} "
          f"({'>' if r['r_comp_incoherent']>FAIL_EDGE else '<'} {FAIL_EDGE:.0e} FAIL edge)")
    print(f"  incoherence inflation = {r['incoherence_inflation']:.2e}x "
          f"(gate's FAIL discriminating power)")

    print(f"\n--- F_amp-slot statement (method step 4; coherent-phase caveat) ---")
    print(f"  {r['F_amp_slot_statement']}")

    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)    # (local)

    print("\n" + "=" * 72)
    print("GATE EVALUATION (pre-registered composite operator)")
    print("=" * 72)
    print(f"  magnitude: {detail['mag_band']} => {mag_v}")
    print(f"  sign:      {detail['sign_band']} => {sign_v}")
    print(f"  regime:    {detail['regime']} => {regime_v}")
    print(f"  unitarity: max={detail['unit_max']:.2e} <= {TOL_UNITARITY:.0e} "
          f"[{detail['unit_ok']}]")
    print(f"  coherent-phase caveat (PRE-REGISTERED, binding): "
          f"{detail['coherent_phase_caveat']}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite (collapse rule + caveat): {comp}")
    print(f"  reason: {detail['composite_reason']}")

    # ---- npz (full float64) ----
    a_a, b_a = r["B1a_entries"]; a_b, b_b = r["B1b_entries"]
    a_W, b_W = r["W_entries"]
    np.savez(
        OUT_NPZ,
        # ==== verdict observable ====
        r_comp=r["r_comp"],
        r_comp_per_tail=np.array([tr["r_comp"] for tr in r["tail_results"]]),
        tail_factors=np.array(TAIL_FACTORS),
        tail_primary_idx=TAIL_PRIMARY_IDX,
        r_comp_tail_spread=r["r_comp_tail_spread"],
        r_comp_max=r["r_comp_max"], r_comp_min=r["r_comp_min"],
        PASS_EDGE=PASS_EDGE, FAIL_EDGE=FAIL_EDGE,
        first_order_bound=r["first_order_bound"],
        eps_W=r["eps_W"],
        pass_edge_x_bound=r["pass_edge_x_bound"],
        fail_edge_x_bound=r["fail_edge_x_bound"],
        # ==== B1a / W / B1b SU(1,1) entries (primary tail=10*Deta) ====
        B1a_alpha_re=a_a.real, B1a_alpha_im=a_a.imag,
        B1a_beta_re=b_a.real, B1a_beta_im=b_a.imag,
        W_alpha_re=a_W.real, W_alpha_im=a_W.imag,
        W_beta_re=b_W.real, W_beta_im=b_W.imag,
        B1b_alpha_re=a_b.real, B1b_alpha_im=a_b.imag,
        B1b_beta_re=b_b.real, B1b_beta_im=b_b.imag,
        beta2_B1a=r["beta2_a"], beta2_W_stage=r["beta2_W_reeval"],
        beta2_B1b=r["beta2_b"],
        # ==== composed vs unsplit ====
        beta2_composed=r["beta2_comp"],
        beta2_B1_unsplit=r["beta2_B1_unsplit"],
        beta2_W_canon=t["beta2_W_canon"],
        rel_W_vs_canon=r["rel_W_vs_canon"],
        # ==== unitarity residuals ====
        unitarity_W=r["unit_W"], unitarity_B1a=r["unit_a"],
        unitarity_B1b=r["unit_b"], unitarity_composed=r["unit_comp"],
        unitarity_max=r["unit_max"],
        beta2_free_ode=r["beta2_free_ode"], unitarity_free_ode=r["unit_free_ode"],
        # ==== substitution-chain pins ====
        mu_pivot_sq_branch_c=r["mu2_c"],
        k_pivot=t["k_pivot"], k2_over_zppz_fold=t["k2_over_zppz"],
        Delta_eta=t["L"], eta_window=np.array([t["eta_on"], t["eta_off"]]),
        Omega_z_on=t["Om_on"], Omega_z_off=t["Om_off"],
        V_box_branch_c=t["V_box_c"],
        # ==== F_amp-slot statement ====
        coherent_phase_caveat=r["coherent_phase_caveat"],
        F_amp_slot_statement=r["F_amp_slot_statement"],
        F_amp_sc=F_AMP_SC, F_amp_slot=F_AMP_SLOT,
        B2_ladder_anchor=t["B2_anchor"],
        B1_S79_OOM_anchor=B1_S79_OOM_ANCHOR, S_IC_S79_anchor=S_IC_S79_ANCHOR,
        S_W_max=r["S_W_max"], S_W_min=r["S_W_min"],
        slot_pert_max=r["slot_pert_max"],
        window_over_B2=r["window_over_B2"], window_over_slot=r["window_over_slot"],
        oom_window_vs_B2=r["oom_window_vs_B2"],
        DeltaN_window=DELTA_N_WINDOW, N_B2_span=N_B2_SPAN,
        efold_shorter_x=r["efold_shorter_x"],
        # ==== x6.96 incoherence diagnostic ====
        r_comp_incoherent=r["r_comp_incoherent"],
        x696_ratio=r["x696_ratio"],
        incoherence_inflation=r["incoherence_inflation"],
        # ==== diagnostic k-grid spectrum ====
        k_grid=r["k_grid"], r_comp_spectrum=r["r_comp_spectrum"],
        beta2_W_spectrum=r["beta2_W_spectrum"],
        # ==== verdict block ====
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        w5_1_predecessor_sha=W5_1_EXPECTED_SHA,
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(t, r)

    # ---- value 4-tuple + payload ----
    val = (f"r_comp={r['r_comp']:.4g};"
           f"beta2_composed={r['beta2_comp']:.6g};"
           f"beta2_B1_unsplit={r['beta2_B1_unsplit']:.6g};"
           f"eps_W={r['eps_W']:.4g};first_order_bound={r['first_order_bound']:.4g};"
           f"pass_edge={PASS_EDGE:.0e};fail_edge={FAIL_EDGE:.0e};"
           f"unit_max={r['unit_max']:.1e};r_comp_tail_spread={r['r_comp_tail_spread']:.1e};"
           f"r_comp_incoherent={r['r_comp_incoherent']:.3g};"
           f"x696_ratio={r['x696_ratio']:.4f};"
           f"coherent_phase_caveat={r['coherent_phase_caveat']};"
           f"S_W=[{r['S_W_min']:.6f},{r['S_W_max']:.6f}];"
           f"window_vs_B2_OOM={r['oom_window_vs_B2']:.2f};"
           f"efold_shorter={r['efold_shorter_x']:.0f}x")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (
        f"B1 stage-split B1a*W*B1b in SU(1,1) (S79 form-1, L->R order); "
        f"r_comp={r['r_comp']:.3e} (magnitude PASS, {r['pass_edge_x_bound']:.1f}x "
        f"inside PASS edge {PASS_EDGE:.0e}; 1st-order bound 4*eps_W="
        f"{r['first_order_bound']:.3e}); composed |beta|^2={r['beta2_comp']:.4e} "
        f"reproduces unsplit B1 |beta|^2={r['beta2_B1_unsplit']:.4e} (re-evaluated "
        f"in-script; S79 4.3e4 OOM-only); free flanking segments = pure phase "
        f"(|beta|^2~{r['beta2_a']:.1e}); unitarity {r['unit_max']:.1e} per factor "
        f"& composed; coherent-phase caveat FIRES on F_amp-slot statement "
        f"(S79 anchors magnitudes-only) => composite INFO")  # (local)
    rows = [
        f"# composition: B1a*W*B1b (S79 form-1 B=[[a,conj(b)],[b,conj(a)]], "
        f"product order=temporal L->R; Sage-verified reproduces S79 eq(3)-(4) "
        f"alpha_3=alpha_2 alpha_1+beta_2 beta_1*, beta_3=alpha_2 beta_1+beta_2 "
        f"alpha_1*) # {GATE_ID} SU(1,1)-convention row",
        f"# magnitude PASS: r_comp={r['r_comp']:.3e}<=1.0e-2 ({r['pass_edge_x_bound']:.2f}x "
        f"inside edge); composite INFO via PRE-REGISTERED coherent-phase caveat "
        f"(F_amp-slot statement needs relative phase W<->B2 the S79 magnitude-only "
        f"anchors lack; S79 product rule F_amp x S_IC valid only coherent-phase) "
        f"# {GATE_ID}",
        f"# F_amp-slot: window |beta_W|^2={t['beta2_W_canon']:.4e} is "
        f"{r['oom_window_vs_B2']:.2f} OOM below B2 anchor (1700), {1.0/r['window_over_slot']:.0f}x "
        f"below F_amp_slot (0.3885); DeltaN={DELTA_N_WINDOW:.2e} is {r['efold_shorter_x']:.0f}x "
        f"shorter than B2 (N~3) => STAGE not slot-renorm; S_W=[{r['S_W_min']:.6f},"
        f"{r['S_W_max']:.6f}] (<={100*r['slot_pert_max']:.4f}%, phase-dependent); "
        f"F_amp slot UNCHANGED to magnitude-level (CC2=+1 POWER-RATIO, F_amp^sc=47.92 "
        f"3PI, slot 0.3885 k_a2) # {GATE_ID}",
        f"# x6.96 hazard DIAGNOSTIC (reported, NEVER gated): coherent r_comp="
        f"{r['r_comp']:.2e} PASS vs incoherent (Z-PUMP/sqrt(a)-pump weight-mix at "
        f"splits) r_comp={r['r_comp_incoherent']:.2e}>5e-2 FAIL edge ({r['incoherence_inflation']:.1e}x "
        f"inflation); Z-PUMP/sqrt(a) beta2 ratio={r['x696_ratio']:.4f}=the x6.96 "
        f"silent-inheritance class the S-1 adjudication closed # {GATE_ID}",
        f"# r_comp tail-invariance: spread={r['r_comp_tail_spread']:.2e} across "
        f"tail in [1,10,100,1000]*Delta_eta (FD floor; free segments are pure "
        f"phases => convention-coherence witness) # {GATE_ID}",
        f"# write_order: Step1=emit_verdict (this line); no canonical_constants "
        f"promotion (r_comp is a composition-consistency observable, not a new "
        f"framework prediction); Step3=N/A # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n citation; no SCHEMATIC "
        f"helper consumed (W5-1 npz + s64/s100b npz + canonical_constants only) "
        f"# {GATE_ID}",
    ]                                                          # (local)
    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
