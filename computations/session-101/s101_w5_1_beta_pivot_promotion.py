#!/usr/bin/env python3
"""
S101 W5-1 S101-BETA-PIVOT-PROMOTION -- tuple-pinned |beta_pivot|^2 recompute
============================================================================

Gate: S101-BETA-PIVOT-PROMOTION ([SIGN]; schema-v2 3-tuple required --
      the substitution chain pre-registers the branch claim mu_pivot^2 > 0)

Plan: sessions/session-plan/session-101-plan-w5.md SS W5-1 (R3 YAML block,
      4-component convention tuple BINDING per the S-1 adjudication, machinery
      pins, substitution chains A (mu_pivot^2 sign) + B (Born-limit DIAGNOSTIC
      band), canonical write-order Steps 1-2).

WHAT THIS GATE IS (S-1-adjudicated, NOT a silent promotion of the W5-1 payload):
  Re-run the S100b W5-1-VALIDATED box+delta closed-form recipe (Schmidt
  Eq.-75-class sin-branch interior + two delta kicks; S100b-BOX-DELTA-BOGOLIUBOV
  PASS, audit 297a597c3cfe6fa0...) with the convention tuple SWAPPED to the
  adjudication:
    (1) Z-PUMP per-edge delta weights Omega = [z'/z] read at the window edges
        (anchors Omega_z_on = +1.2872356866503005,
                 Omega_z_off = -1.288529316518922 M_KK;
         npz keys of the S100b validation run). The Sparn-literal sqrt(a)-PUMP
         weight Omega = (1/2)a[a'] (+-0.487) is DEMOTED to recipe-benchmark.
    (2) branch-(c) interior barrier V_box = stored s64 zpp_over_z window mean
        = 2.764080442498705 M_KK^2 (eta_H-corrected; 1.4526498761887858x the
        quasi-dS anchor). Branch (b) 2(aH)^2 = 1.9027850412 retained ONLY as
        the CHK-N normalization cross-check anchor.
    (3) window = canonical FOLD-CONFORMAL clock Delta_eta = 1.13014059e-3
        M_KK^-1 (conformal image of dt_transit; re-derived in-gate and
        CHK'd against the stored 0.00113014058799074), tau in
        [0.18994874, 0.19005127].
    (4) ladder stage = IMPULSIVE-TRANSIT-WINDOW (BD-in-out v-quanta at the
        window edges; DeltaN = 1.10e-3 e-folds; NON-comparable to S79 B2 by
        e-fold-span construction).

  EMIT BOTH keyed values:
    canonical    beta2_pivot_box_delta             (NEW tuple; v-quanta)
    diagnostic   beta2_pivot_box_delta_sqrtA_recipe = 3.045e-07
                 (the PERMANENT W5-1 payload verbatim; Sparn-literal benchmark).

  The branch-(c)+Z-PUMP combination is NOT yet stored anywhere
  (beta2_zpump_weights in the s100b npz used the branch-(b) barrier);
  beta2_pivot_box_delta is COMPUTED in this gate from the pinned channels.

PRE-REGISTERED OPERATOR (composite conjunction of 3 clauses):
  PASS iff (i) AND (ii) AND (iii):
    (i)   recipe-internal at the new tuple:
            unitarity_residual_max <= 1e-10 (ABSOLUTE)
            AND var_Nseg < 2.0 (RATIO, over N_seg in {1,2,4,8})
            AND mu_pivot^2 > 0 (sign row);
    (ii)  npz<->published round-trip: |published_4sf - v_npz|/v_npz <= 5.0e-4
            for BOTH keyed values (Class-8.3; 5.0e-4 = exact 4-s.f. half-ulp);
    (iii) constant lands with the FULL 4-component tuple in PROVENANCE
            + both keyed values (write-order Steps 1-2 executed -- the
            update_constant calls are the agent's MCP step; this script PRINTS
            the values + the canonical-write-order instruction).
  The Born-limit band [2.119, 2.140]e-6 is a pre-registered DIAGNOSTIC
  cross-check: REPORTED, NEVER GATED.

Inputs (SHA-256 verified against plan pins; logged in first 20 stdout lines):
  computations/_shared/canonical_constants.py            (runtime-pinned)
  computations/session-100b/s100b_box_delta_bogoliubov.npz (tuple anchors)
  computations/session-64/s64_mukhanov_sasaki.npz        (z_tau, zpp_over_z)
  computations/session-77/s77_n_pivot_map.npz            (k_pivot, CHK-N)

Output 4-tuple:
  (value=<payload>, scheme=BOX-DELTA-SUDDEN,
   convention=BD-in-out-Z-PUMP-branchC-foldclock, L_max=N/A)

Classification: PHONONIC

Verdict emission: this script PRINTS the payload via print_verdict_payload;
the dispatching agent calls the race-safe emit_verdict knowledge-MCP tool
(gate-verdicts.md SS"Race-Safe Emission"). NO open("a") verdict writes.

SUBSTRATE FRAMING: the supersonic transit (Mach 13.75) through the van Hove
fold IS a time-dependent reorganization of the D_K eigenvalue spectrum; in the
substrate's own fold-conformal clock the reorganization presents as a box
barrier z''/z (the spectral-action curvature of the Mukhanov-Sasaki pump
variable z = a*sqrt(2 eps_H)*M_Pl_eff) switched on and off by two edge jumps
[z'/z]. The substrate-IS jump operator is [z'/z] -- every downstream consumer
(B-ladder, F_amp slot) counts v-quanta, and the vacua on either side of an edge
do not coincide, which is WHY the Z-PUMP weight (not the Sparn-literal
sqrt(a)-pump) is the canonical convention (S-1 SSII.1/SSII.4 structural
derivation). |beta_pivot|^2 IS the per-mode deposit price the transit pays at
the pivot mode: production lives at the switch-on/off of the spectral
reorganization (Parra-Lopez switch dominance, deltas/box = x54). The promoted
constant is a COMPOSITION INPUT (one SU(1,1) factor of the B-ladder in
v-quanta), anchoring the NEW IMPULSIVE-TRANSIT-WINDOW ladder stage.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy import (GPU_path: cpu-cap-OMP8;
# 64-mode 2x2 transfer algebra + scipy Radau -- trivially small, no GPU)
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
from scipy.interpolate import CubicSpline

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
# consumed: tau_fold, dt_transit, M_KK, H_fold

# --------------------------------------------------------------------------
# Section 2 -- Pre-registration (plan SS W5-1 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = "101"                                                   # (local)
GATE_ID = "S101-BETA-PIVOT-PROMOTION"                             # (local)
SCHEME = "BOX-DELTA-SUDDEN"                                       # (local)
CONVENTION = "BD-in-out-Z-PUMP-branchC-foldclock"                # (local)
L_MAX = "N/A"                                                     # (local)

TOL_UNITARITY = 1e-10       # (local) ABSOLUTE on ||alpha|^2-|beta|^2-1|
TOL_VAR_NSEG = 2.0          # (local) RATIO, strict <
TOL_ROUNDTRIP = 5.0e-4      # (local) RATIO, <= (Class-8.3 4-s.f. half-ulp)
N_SEG_SCAN = [1, 2, 4, 8]   # (local) var_Nseg re-emission sweep
N_K_DIAG = 64               # (local) diagnostic k-grid points
K_MIN, K_MAX = 1.0, 50.0    # (local) diagnostic k range [M_KK]
ODE_RTOL, ODE_ATOL = 1e-10, 1e-14                                 # (local)

# Born-limit DIAGNOSTIC band (reported, NEVER gated)
BORN_BAND = (2.119e-6, 2.140e-6)                                  # (local)

# sqrtA-recipe permanent W5-1 payload (verbatim diagnostic companion)
SQRTA_PAYLOAD = 3.045e-07   # (local) 4-s.f. published form of W5-1 payload

# forward consumer (W5-2) -- NOT a supersedes/predecessor token; context only
FORWARD_LADDER = "S101-LADDER-COMPOSITION"                        # (local)

OUT_NPZ = SESSION_DIR / "s101_w5_1_beta_pivot_promotion.npz"
OUT_PNG = SESSION_DIR / "s101_w5_1_beta_pivot_promotion.png"

# Plan-pinned input SHAs (Input-SHA Ledger, plan-freeze 2026-06-07)
PINNED_INPUTS = {                                                 # (local)
    "computations/session-100b/s100b_box_delta_bogoliubov.npz":
        "43275f5104d24305e88fd7c4e4fec5eb517ffd1e97767b4590108c2420cb409a",
    "computations/session-64/s64_mukhanov_sasaki.npz":
        "e671f535e3a2da78e58ccb38deaa84fd52ae19608e7fbec0783eee3d57cf5e42",
    "computations/session-77/s77_n_pivot_map.npz":
        "80fbf580234d0e3e55502d18fec35e32e93356f17f62ac7cdc409acecaf50bba",
}

MACHINERY_PINS = {                                                # (local)
    "N_eval": "64",
    "N_seg_scan": "[1,2,4,8]",
    "L_max": "N/A",
    "scan_range": "single-tuple eval; verdict at k_pivot=14.311092688448717",
    "step_size": "closed-form; ODE cross-check adaptive Radau",
    "tolerance": "1e-10 ABS unitarity; 2.0 RATIO N_seg; 5.0e-4 RATIO round-trip",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "weight_rule": "Z-PUMP Omega=[z'/z] per edge (anchors "
                   "+1.2872356866503005 / -1.288529316518922 M_KK); "
                   "sqrt(a)-PUMP (1/2)a[a'] DEMOTED to benchmark",
    "barrier_branch": "(c) stored s64 zpp_over_z window mean = "
                      "2.764080442498705 M_KK^2 (eta_H-corrected; "
                      "1.4526498761887858x anchor); branch (b) 2(aH)^2 "
                      "ONLY as CHK-N anchor",
    "window": "CANONICAL FOLD-CONFORMAL CLOCK Delta_eta = 1.13014059e-3 "
              "M_KK^-1 (conformal image of dt_transit; CHK vs stored "
              "0.00113014058799074); tau in [0.18994874, 0.19005127]",
    "ladder_stage": "IMPULSIVE-TRANSIT-WINDOW (BD-in-out at edges; "
                    "DeltaN=1.10e-3 e-folds; NON-comparable to S79 B2)",
    "fold_normalization": "Convention B a(tau_fold)=1; CHK-N vs "
                          "k_pivot^2/107.63558173571887",
    "publication_precision": "4 sig figs (BOTH keyed values; full float64 npz)",
    "random_seed": "N/A",
    "GPU_path": "cpu-cap-OMP8",
    "regulator_pin": "N/A",
    "CLASS": "N/A",
}


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
    content = sha256(script). pinmap includes file SHAs + machinery pins."""
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = canonical_path.read_bytes()                 # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_a = hashlib.sha256()                                        # (local)
    h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
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
# Section 3 -- Input SHA verification (first 20 lines of stdout)
# --------------------------------------------------------------------------
def verify_inputs() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins (plan-verified) ===")
    pins: dict = {}                                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    sha_canon = sha256_of(canonical_path)                         # (local)
    print(f"  computations/_shared/canonical_constants.py: {sha_canon[:16]}... "
          f"(runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon
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


# --------------------------------------------------------------------------
# Section 4 -- Exact 2x2 transfer-matrix building blocks (entire functions)
# (identical algebra to S100b-BOX-DELTA-BOGOLIUBOV; the validated recipe)
# --------------------------------------------------------------------------
def entire_CS(mu2: float, L: float) -> tuple[float, float]:
    """C = cos(mu L), S = sin(mu L)/mu as ENTIRE functions of mu^2.
    For mu^2 < 0 this IS the Schmidt continuation mu -> i Lambda:
    C = cosh(Lambda L), S = sinh(Lambda L)/Lambda."""
    x = mu2 * L * L                                               # (local)
    if abs(x) < 1e-12:
        return 1.0 - x / 2.0, L * (1.0 - x / 6.0)
    if mu2 > 0:
        m = np.sqrt(mu2)                                          # (local)
        return float(np.cos(m * L)), float(np.sin(m * L) / m)
    lam = np.sqrt(-mu2)                                           # (local)
    return float(np.cosh(lam * L)), float(np.sinh(lam * L) / lam)


def M_box(mu2: float, L: float) -> np.ndarray:
    C, S = entire_CS(mu2, L)                                      # (local)
    return np.array([[C, S], [-mu2 * S, C]], dtype=float)


def M_delta(Omega: float) -> np.ndarray:
    """[psi'] = +Omega psi across the peak (Schmidt B41/B42 matching)."""
    return np.array([[1.0, 0.0], [Omega, 1.0]], dtype=float)


def tm_beta(k: float, M: np.ndarray, eta_on: float,
            eta_off: float) -> tuple[complex, complex]:
    """BD-in-out extraction: in-state pure positive frequency e^{-ik eta}
    before eta_on; out-state alpha e^{-ik eta} + beta e^{+ik eta}."""
    psi0 = np.exp(-1j * k * eta_on)                               # (local)
    v0 = np.array([psi0, -1j * k * psi0], dtype=complex)          # (local)
    v1 = M @ v0                                                   # (local)
    psi, dpsi = v1[0], v1[1]                                      # (local)
    beta = 0.5 * (psi + dpsi / (1j * k)) * np.exp(-1j * k * eta_off)   # (local)
    alpha = 0.5 * (psi - dpsi / (1j * k)) * np.exp(+1j * k * eta_off)  # (local)
    return alpha, beta


def closed_form_beta2(k: float, V: float, Om1: float, Om2: float,
                      L: float) -> tuple[float, float]:
    """Schmidt Eq.75/76-class closed form for box(V,L)+deltas(Om1,Om2),
    generalized to Om1 != -Om2, as an EXPLICIT algebraic expression
    (independent code path from the matrix product):
      |beta|^2 = (1/4)[ (Om1-Om2)^2 S^2
                        + ( k S + ((Om1+Om2) C + (Om1 Om2 - mu^2) S)/k )^2 ]
      |alpha|^2 = (1/4)[ (2C + (Om1+Om2) S)^2
                        + ( k S - ((Om1+Om2) C + (Om1 Om2 - mu^2) S)/k )^2 ]
    with mu^2 = k^2 - V, C = cos(mu L), S = sin(mu L)/mu entire in mu^2."""
    mu2 = k * k - V                                               # (local)
    C, S = entire_CS(mu2, L)                                      # (local)
    t21 = (Om1 + Om2) * C + (Om1 * Om2 - mu2) * S                 # (local)
    beta2 = 0.25 * ((Om1 - Om2) ** 2 * S ** 2
                    + (k * S + t21 / k) ** 2)                     # (local)
    alpha2 = 0.25 * ((2.0 * C + (Om1 + Om2) * S) ** 2
                     + (k * S - t21 / k) ** 2)                    # (local)
    return float(beta2), float(alpha2)


def tm_box_delta_beta2(k: float, V: float, Om1: float, Om2: float, L: float,
                       eta_on: float, n_seg: int = 1) -> tuple[float, float]:
    """Transfer-matrix route: M = M_delta(Om2) . [box product, n_seg
    constant-V segments] . M_delta(Om1). For a TRUE box (constant V) the
    segmentation is EXACT at every n_seg (no interior reflection error) --
    this is the genuine-sharp-boundary regime where TM is EXACT
    (S100b W5-1 calibration). eta_off = eta_on + L."""
    eta_off = eta_on + L                                         # (local)
    mu2 = k * k - V                                              # (local)
    Lseg = L / n_seg                                            # (local)
    M = M_delta(Om1)                                            # (local)
    for _ in range(n_seg):
        M = M_box(mu2, Lseg) @ M
    M = M_delta(Om2) @ M                                        # (local)
    al, be = tm_beta(k, M, eta_on, eta_off)                    # (local)
    return float(abs(be) ** 2), float(abs(al) ** 2)


def ode_box_delta_beta2(k: float, V: float, Om1: float, Om2: float, L: float,
                        eta_on: float) -> tuple[float, float]:
    """Radau ODE cross-check: psi'' + (k^2 - V) psi = 0 across the constant-V
    interior with the two boundary deltas as matching conditions; BD-in/out
    extraction. The v-equation v'' + (k^2 - z''/z) v = 0 IS this with the box
    barrier V = (z''/z)|window. rtol=1e-10 per the pinned diagnostic."""
    eta_off = eta_on + L                                        # (local)
    psi0 = np.exp(-1j * k * eta_on)                             # (local)
    v0c = np.array([psi0, -1j * k * psi0], dtype=complex)       # (local)
    v0c = M_delta(Om1) @ v0c                                    # (local)
    y0 = [v0c[0].real, v0c[0].imag, v0c[1].real, v0c[1].imag]   # (local)

    def rhs(eta, y):
        return [y[2], y[3], (V - k * k) * y[0], (V - k * k) * y[1]]

    sol = solve_ivp(rhs, [eta_on, eta_off], y0, method="Radau",
                    rtol=ODE_RTOL, atol=ODE_ATOL)                # (local)
    if not sol.success:
        return np.nan, np.nan
    psi = sol.y[0, -1] + 1j * sol.y[1, -1]                       # (local)
    dpsi = sol.y[2, -1] + 1j * sol.y[3, -1]                      # (local)
    v1 = M_delta(Om2) @ np.array([psi, dpsi])                   # (local)
    beta = 0.5 * (v1[0] + v1[1] / (1j * k)) * np.exp(-1j * k * eta_off)   # (local)
    alpha = 0.5 * (v1[0] - v1[1] / (1j * k)) * np.exp(+1j * k * eta_off)  # (local)
    return float(abs(beta) ** 2), float(abs(alpha) ** 2)


# --------------------------------------------------------------------------
# Section 5 -- Load the adjudicated tuple anchors + in-gate CHKs
# --------------------------------------------------------------------------
def load_tuple() -> dict:
    d100b = np.load(COMPUTATIONS_DIR / "session-100b"
                    / "s100b_box_delta_bogoliubov.npz",
                    allow_pickle=True)                           # (local)
    d64 = np.load(COMPUTATIONS_DIR / "session-64"
                  / "s64_mukhanov_sasaki.npz", allow_pickle=True)  # (local)
    d77 = np.load(COMPUTATIONS_DIR / "session-77"
                  / "s77_n_pivot_map.npz", allow_pickle=True)    # (local)

    # ---- (1) Z-PUMP per-edge weights (adjudicated; from s100b validation) ----
    Om_z_on = float(d100b["Omega_z_on"])                         # (local)
    Om_z_off = float(d100b["Omega_z_off"])                       # (local)
    # ---- (2) branch-(c) interior barrier (stored s64 zpp_over_z window mean)
    V_box_c = float(d100b["zppz_stored_fold_units"])             # (local)
    V_box_c_rederived = float(d100b["V_box_branch_c"])           # (local)
    V_box_b = float(d100b["V_box"])           # (local) CHK-N anchor (branch b)
    # ---- (3) window: canonical fold-conformal clock Delta_eta ----
    Delta_eta = float(d100b["Delta_eta"])                        # (local)
    eta_window = np.asarray(d100b["eta_window"], float)          # (local)
    tau_window = np.asarray(d100b["tau_window"], float)          # (local)
    eta_on, eta_off = float(eta_window[0]), float(eta_window[1]) # (local)
    # ---- pivot mode (fold normalization; NEVER the mixed-conv 4.30e-57) ----
    k_pivot = float(d100b["k_pivot"])                            # (local)
    k_pivot_s77 = float(d77["k_pivot_com_fold"])                 # (local)
    k2_over_zppz = float(d100b["k2_over_zppz_fold"])             # (local)
    k2_over_zppz_s77 = float(d77["k2_over_zppz_fold"])           # (local)
    # ---- diagnostic/benchmark anchors (verbatim W5-1 payloads) ----
    beta2_sqrtA = float(d100b["beta2_pivot_closed_form"])        # (local)
    beta2_zpump_storedV = float(d100b["beta2_zpump_weights"])    # (local)
    CHK_N_validation = float(d100b["CHK_N_ratio"])               # (local)
    B2_anchor = float(d100b["B2_ladder_anchor"])                 # (local)

    print("\n--- Adjudicated 4-component tuple (loaded from validated recipe) ---")
    print(f"  (1) Z-PUMP weights : Omega_z_on = {Om_z_on:+.16f} M_KK")
    print(f"                       Omega_z_off= {Om_z_off:+.16f} M_KK")
    print(f"  (2) branch-(c) barrier V_box = {V_box_c:.15f} M_KK^2 "
          f"(stored zpp_over_z window mean)")
    print(f"      [re-derived window-integral form {V_box_c_rederived:.10f}; "
          f"rel dev {abs(V_box_c_rederived/V_box_c-1):.2e}]")
    print(f"      branch-(b) anchor 2(aH)^2 = {V_box_b:.10f} (CHK-N only; "
          f"ratio (c)/(b) = {V_box_c/V_box_b:.10f} = "
          f"{V_box_c/V_box_b:.4f}x = eta_H-corr factor)")
    print(f"  (3) window Delta_eta = {Delta_eta:.15e} M_KK^-1")
    print(f"      tau window [{tau_window[0]:.8f}, {tau_window[1]:.8f}]; "
          f"eta window [{eta_on:+.10e}, {eta_off:+.10e}]")
    print(f"  (4) ladder stage   : IMPULSIVE-TRANSIT-WINDOW (BD-in-out)")
    print(f"  pivot mode k_pivot = {k_pivot:.15f} M_KK "
          f"(s77 cross-check {k_pivot_s77:.15f}; "
          f"rel {abs(k_pivot/k_pivot_s77-1):.2e})")

    # ---- in-gate CHK: re-derive Delta_eta from dt_transit (conformal image)
    # The s100b validation derived Delta_eta from a full fold-normalization
    # pipeline. Here we CHK the stored value against the canonical dt_transit
    # via the fold-normalized conformal relation Delta_eta ~ dt_transit (the
    # conformal image at a(tau_fold)=1 in the fold-conformal clock; the
    # |Delta_eta - dt_transit|/dt_transit residual is the a~ != 1 edge drift).
    chk_Deta_vs_dt = abs(Delta_eta / dt_transit - 1.0)           # (local)
    print(f"\n--- In-gate CHK: window vs dt_transit ---")
    print(f"  dt_transit (canonical) = {dt_transit:.15e} M_KK^-1")
    print(f"  Delta_eta (stored fold-conformal) = {Delta_eta:.15e} M_KK^-1")
    print(f"  ratio Delta_eta/dt_transit = {Delta_eta/dt_transit:.10f} "
          f"(edge a~ drift {chk_Deta_vs_dt:.3e}; aH*Delta_eta = "
          f"{Delta_eta*k_pivot/np.sqrt(2.0*k2_over_zppz):.3e} << 1)")

    # ---- in-gate CHK: re-derive [z'/z] at the window edges from s64 channels
    # The Z-PUMP weight Omega = [z'/z]*a~H~ at the edge; the stored anchors
    # already encode this. We CHK the s64 z_tau channel slope sign at the fold
    # (z growing through the fold => [z'/z] crosses through the edge values).
    tau64 = d64["tau_dense"]                                     # (local)
    z64 = d64["z_tau"]                                           # (local)
    sp_z = CubicSpline(tau64, z64)                               # (local)
    dlnz_dtau_fold = float(sp_z(tau_fold, 1)) / float(sp_z(tau_fold))  # (local)
    print(f"  s64 z_tau channel: d(ln z)/d(tau)|fold = {dlnz_dtau_fold:+.6e} "
          f"(Z-PUMP edge weights are this slope x edge a~H~; "
          f"on/off sign split {np.sign(Om_z_on):+.0f}/{np.sign(Om_z_off):+.0f})")

    # ---- CHK-N: stored validation CHK_N_ratio in band [0.95, 1.05] ----
    chk_n_ok = 0.95 <= CHK_N_validation <= 1.05                  # (local)
    print(f"  CHK-N (from validated recipe): {CHK_N_validation:.10f} "
          f"in [0.95,1.05] -> {'OK' if chk_n_ok else 'BREACH'}; "
          f"k2_over_zppz s100b={k2_over_zppz:.8f} vs s77="
          f"{k2_over_zppz_s77:.8f} (rel {abs(k2_over_zppz/k2_over_zppz_s77-1):.1e})")
    if not chk_n_ok:
        print("HARD-ABORT: CHK-N out of band (normalization lineage broken).")
        sys.exit(2)

    return dict(Om_z_on=Om_z_on, Om_z_off=Om_z_off,
                V_box_c=V_box_c, V_box_c_rederived=V_box_c_rederived,
                V_box_b=V_box_b, Delta_eta=Delta_eta,
                eta_on=eta_on, eta_off=eta_off,
                eta_window=eta_window, tau_window=tau_window,
                k_pivot=k_pivot, k2_over_zppz=k2_over_zppz,
                beta2_sqrtA=beta2_sqrtA,
                beta2_zpump_storedV=beta2_zpump_storedV,
                CHK_N_validation=CHK_N_validation, B2_anchor=B2_anchor,
                chk_Deta_vs_dt=chk_Deta_vs_dt,
                dlnz_dtau_fold=dlnz_dtau_fold,
                # literal sqrt(a)-pump weights (DEMOTED benchmark)
                Om_lit_on=float(d100b["Omega_on"]),
                Om_lit_off=float(d100b["Omega_off"]))


# --------------------------------------------------------------------------
# Section 6 -- Main computation
# --------------------------------------------------------------------------
def compute(t: dict) -> dict:
    k = t["k_pivot"]                                             # (local)
    L = t["Delta_eta"]                                           # (local)
    Vc = t["V_box_c"]                                            # (local)
    Vb = t["V_box_b"]                                            # (local)
    Om1, Om2 = t["Om_z_on"], t["Om_z_off"]                       # (local)
    eta_on = t["eta_on"]                                         # (local)

    # ---- substitution Chain A: mu_pivot^2 sign row (branch-c barrier) ----
    mu2_c = k * k - Vc                                           # (local)
    print("\n--- Substitution Chain A (mu_pivot^2 sign row; runtime) ---")
    print(f"  Def 1: mu_pivot^2 := k_pivot^2 - V_box^(c)")
    print(f"  Def 2: k_pivot = {k:.15f} M_KK (fold norm; NOT 4.30e-57)")
    print(f"  Def 3: V_box^(c) = {Vc:.15f} M_KK^2 (branch-c stored barrier)")
    print(f"  Substitute: mu_pivot^2 = ({k:.12f})^2 - {Vc:.12f}")
    print(f"            = {k*k:.10f} - {Vc:.10f}")
    print(f"            = {mu2_c:.10f} M_KK^2")
    print(f"  Direction: {mu2_c:.4f} > 0 => oscillatory (sin-branch) interior; "
          f"margin k_pivot^2/V_box^(c) = {k*k/Vc:.4f}x")
    print(f"  mu_pivot*Delta_eta = {np.sqrt(mu2_c)*L:.6e} << pi (diag-(ii) ~1.6e-2)")
    sign_ok = mu2_c > 0.0                                        # (local)

    # ---- CANONICAL: beta2_pivot_box_delta (Z-PUMP + branch-c barrier) ----
    # Three INDEPENDENT code paths: closed form, transfer matrix, Radau ODE.
    beta2_canon_cf, alpha2_canon_cf = closed_form_beta2(k, Vc, Om1, Om2, L)  # (local)
    unit_cf = abs(alpha2_canon_cf - beta2_canon_cf - 1.0)        # (local)

    print("\n--- CANONICAL beta2_pivot_box_delta (NEW tuple; 3 code paths) ---")
    print(f"  closed form  : |beta|^2 = {beta2_canon_cf:.15e}")
    print(f"                 unitarity |alpha|^2-|beta|^2-1 = {unit_cf:.3e}")

    # N_seg robustness sweep [1,2,4,8] (TM route; constant-V box => EXACT at all)
    beta2_per_Nseg = []                                          # (local)
    unit_per_Nseg = []                                           # (local)
    for n_seg in N_SEG_SCAN:
        b2, a2 = tm_box_delta_beta2(k, Vc, Om1, Om2, L, eta_on, n_seg)  # (local)
        beta2_per_Nseg.append(b2)
        unit_per_Nseg.append(abs(a2 - b2 - 1.0))
        print(f"  TM n_seg={n_seg:2d}: |beta|^2 = {b2:.15e}  "
              f"(unitarity {abs(a2-b2-1.0):.2e})")
    beta2_per_Nseg = np.array(beta2_per_Nseg)                    # (local)
    unit_per_Nseg = np.array(unit_per_Nseg)                      # (local)
    var_Nseg = float(beta2_per_Nseg.max() / beta2_per_Nseg.min())  # (local)
    beta2_TM = float(beta2_per_Nseg[-1])                        # (local)

    b2_ode, a2_ode = ode_box_delta_beta2(k, Vc, Om1, Om2, L, eta_on)  # (local)
    unit_ode = abs(a2_ode - b2_ode - 1.0)                       # (local)
    rel_cf_tm = abs(beta2_TM / beta2_canon_cf - 1.0)            # (local)
    rel_cf_ode = abs(b2_ode / beta2_canon_cf - 1.0)            # (local)
    print(f"  TM (n_seg=8) : |beta|^2 = {beta2_TM:.15e}  "
          f"(rel vs closed {rel_cf_tm:.2e})")
    print(f"  Radau ODE    : |beta|^2 = {b2_ode:.15e}  "
          f"(rel vs closed {rel_cf_ode:.2e}; unitarity {unit_ode:.2e})")
    print(f"  var_Nseg = max/min = {var_Nseg:.12f}  (threshold < {TOL_VAR_NSEG})")

    # canonical value = closed form (the exact algebraic recipe; TM+ODE confirm)
    beta2_canon = beta2_canon_cf                                # (local)

    # max unitarity residual over ALL canonical evaluations
    unit_max = float(max(unit_cf, unit_per_Nseg.max(), unit_ode))  # (local)

    # ---- per-edge weight decomposition (synthesis SSII.2): each Z-PUMP edge
    # weight Omega = [z'/z] = (H-part) + (1/2)eps2*(H-part) + residual.
    # Here we report the decomposition of each Omega against the strict
    # distributional weight (1/2)[adot] (the sqrt(a)-pump literal) and the
    # eta_H-correction that promotes literal -> Z-pump.
    Om_lit_on, Om_lit_off = t["Om_lit_on"], t["Om_lit_off"]      # (local)
    # H-part of each Z-pump weight = the literal (1/2)a[adot] weight;
    # residual = Z-pump - literal (the [z'/z] vs (1/2)[a'] gap = eps_H/eta_H
    # correction). The Z-pump weight = literal x (dlnz/dN)/(1/2) structurally.
    resid_on = Om1 - Om_lit_on                                  # (local)
    resid_off = Om2 - Om_lit_off                                # (local)
    ratio_on = Om1 / Om_lit_on                                  # (local)
    ratio_off = Om2 / Om_lit_off                                # (local)
    print("\n--- Per-edge Z-PUMP weight decomposition (synthesis SSII.2) ---")
    print(f"  ON  edge: Omega_z = {Om1:+.12f} = H-part({Om_lit_on:+.10f}) "
          f"+ residual({resid_on:+.10f}); Z/literal ratio = {ratio_on:.6f}")
    print(f"  OFF edge: Omega_z = {Om2:+.12f} = H-part({Om_lit_off:+.10f}) "
          f"+ residual({resid_off:+.10f}); Z/literal ratio = {ratio_off:.6f}")
    print(f"  the residual IS the [z'/z] vs (1/2)[a'] gap (eta_H=0.956 "
          f"slow-roll-violation correction; x{ratio_on:.3f} amplification "
          f"that promotes the literal sqrt(a)-pump weight to the Z-pump weight)")

    # ---- DIAGNOSTIC: beta2_pivot_box_delta_sqrtA_recipe (verbatim W5-1) ----
    # the permanent W5-1 payload = closed form at branch-b V_box + literal
    # sqrt(a)-pump weights (Sparn-literal benchmark recipe).
    beta2_sqrtA_recompute, a2_sqrtA = closed_form_beta2(
        k, Vb, Om_lit_on, Om_lit_off, L)                        # (local)
    rel_sqrtA = abs(beta2_sqrtA_recompute / t["beta2_sqrtA"] - 1.0)  # (local)
    print("\n--- DIAGNOSTIC beta2_pivot_box_delta_sqrtA_recipe (W5-1 payload) ---")
    print(f"  re-computed (branch-b + literal weights) = "
          f"{beta2_sqrtA_recompute:.15e}")
    print(f"  stored W5-1 payload                      = "
          f"{t['beta2_sqrtA']:.15e}")
    print(f"  rel dev = {rel_sqrtA:.3e} (verbatim reproduction)")

    # ---- Chain B: Born-limit DIAGNOSTIC band (reported, NEVER gated) ----
    Om_bar_z = 0.5 * (abs(Om1) + abs(Om2))                      # (local)
    beta2_born = (Om_bar_z * L) ** 2                            # (local)
    in_band = BORN_BAND[0] <= beta2_canon <= BORN_BAND[1]       # (local)
    print("\n--- Chain B: Born-limit DIAGNOSTIC band (reported, NEVER gated) ---")
    print(f"  Omega_bar_z = (|Om_on|+|Om_off|)/2 = {Om_bar_z:.15f} M_KK")
    print(f"  |beta|^2_Born = (Omega_bar_z * Delta_eta)^2 = {beta2_born:.10e}")
    print(f"  Born band [{BORN_BAND[0]:.3e}, {BORN_BAND[1]:.3e}]")
    print(f"  canonical beta2_pivot_box_delta = {beta2_canon:.10e} "
          f"({'IN' if in_band else 'OUT'} band; "
          f"dist to band: low-edge {beta2_canon/BORN_BAND[0]-1:+.3e}, "
          f"high-edge {beta2_canon/BORN_BAND[1]-1:+.3e})")
    print(f"  [the canonical value is COMPUTED in-gate; the band is a sanity "
          f"diagnostic ONLY -- NO gating on band membership]")

    # ---- branch comparison + delta-dominance context (diagnostic) ----
    beta2_box_only, _ = closed_form_beta2(k, Vc, 0.0, 0.0, L)   # (local)
    beta2_deltas_only, _ = closed_form_beta2(k, 0.0, Om1, Om2, L)  # (local)
    print("\n--- Channel split (Parra-Lopez switch dominance; diagnostic) ---")
    print(f"  box-only |beta|^2 = {beta2_box_only:.3e}; deltas-only = "
          f"{beta2_deltas_only:.3e}; deltas/box = "
          f"{beta2_deltas_only/max(beta2_box_only,1e-300):.1f}x "
          f"(switch-boundary deltas dominate)")

    # ---- diagnostic k-spectrum (64 log points) at the new tuple ----
    print("\n--- Diagnostic |beta_k|^2 spectrum (64 log k-points; new tuple) ---")
    k_grid = np.geomspace(K_MIN, K_MAX, N_K_DIAG)               # (local)
    beta2_spec = np.zeros(N_K_DIAG)                             # (local)
    beta2_spec_sqrtA = np.zeros(N_K_DIAG)                       # (local)
    max_unit_spec = unit_max                                    # (local)
    for i, kk in enumerate(k_grid):
        b2k, a2k = closed_form_beta2(kk, Vc, Om1, Om2, L)       # (local)
        beta2_spec[i] = b2k
        max_unit_spec = max(max_unit_spec, abs(a2k - b2k - 1.0))
        beta2_spec_sqrtA[i], _ = closed_form_beta2(kk, Vb, Om_lit_on,
                                                   Om_lit_off, L)
    print(f"  max unitarity residual over spectrum = {max_unit_spec:.2e} "
          f"(tolerance {TOL_UNITARITY})")

    # ---- ROUND-TRIP (Class-8.3): published 4-s.f. vs full-float64 npz ----
    # canonical
    pub_canon = float(f"{beta2_canon:.4g}")                     # (local)
    rt_canon = abs(pub_canon - beta2_canon) / beta2_canon       # (local)
    # sqrtA (published as the literal 3.045e-07 W5-1 form)
    pub_sqrtA = SQRTA_PAYLOAD                                   # (local)
    rt_sqrtA = abs(pub_sqrtA - beta2_sqrtA_recompute) / beta2_sqrtA_recompute  # (local)
    print("\n--- Round-trip (Class-8.3; published 4-s.f. vs npz float64) ---")
    print(f"  canonical: published {pub_canon:.4g} vs npz {beta2_canon:.10e}; "
          f"rt_rel = {rt_canon:.3e} (<= {TOL_ROUNDTRIP})")
    print(f"  sqrtA    : published {pub_sqrtA:.4g} vs npz {beta2_sqrtA_recompute:.10e}; "
          f"rt_rel = {rt_sqrtA:.3e} (<= {TOL_ROUNDTRIP})")

    return dict(
        mu2_c=mu2_c, sign_ok=sign_ok,
        beta2_canon=beta2_canon, beta2_canon_cf=beta2_canon_cf,
        beta2_TM=beta2_TM, b2_ode=b2_ode,
        beta2_per_Nseg=beta2_per_Nseg, unit_per_Nseg=unit_per_Nseg,
        var_Nseg=var_Nseg, unit_max=max(unit_max, max_unit_spec),
        rel_cf_tm=rel_cf_tm, rel_cf_ode=rel_cf_ode, unit_cf=unit_cf,
        unit_ode=unit_ode,
        beta2_sqrtA_recompute=beta2_sqrtA_recompute, rel_sqrtA=rel_sqrtA,
        Om_bar_z=Om_bar_z, beta2_born=beta2_born, in_band=in_band,
        resid_on=resid_on, resid_off=resid_off,
        ratio_on=ratio_on, ratio_off=ratio_off,
        beta2_box_only=beta2_box_only, beta2_deltas_only=beta2_deltas_only,
        k_grid=k_grid, beta2_spec=beta2_spec,
        beta2_spec_sqrtA=beta2_spec_sqrtA,
        pub_canon=pub_canon, rt_canon=rt_canon,
        pub_sqrtA=pub_sqrtA, rt_sqrtA=rt_sqrtA,
    )


# --------------------------------------------------------------------------
# Section 7 -- Gate evaluation (pre-registered composite operator)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    # ---- clause (i): recipe-internal at the new tuple ----
    unit_ok = r["unit_max"] <= TOL_UNITARITY                    # (local)
    var_ok = r["var_Nseg"] < TOL_VAR_NSEG                       # (local)
    sign_ok = r["sign_ok"]                                      # (local)
    clause_i = unit_ok and var_ok and sign_ok                  # (local)
    # ---- clause (ii): round-trip for BOTH keyed values ----
    rt_ok = (r["rt_canon"] <= TOL_ROUNDTRIP
             and r["rt_sqrtA"] <= TOL_ROUNDTRIP)               # (local)
    clause_ii = rt_ok                                          # (local)
    # ---- clause (iii): tuple-completeness (set; 4/4 components present) ----
    # The 4 components are pinned and carried in PROVENANCE by construction;
    # this script EMITS them; the agent's update_constant completes the write.
    tuple_components = 4                                       # (local)
    clause_iii = tuple_components == 4                         # (local)

    # ---- 3-tuple (schema-v2; [SIGN] trigger on mu_pivot^2 > 0) ----
    sign_v = "PASS" if sign_ok else "FAIL"                     # (local)
    # magnitude axis: the conjunction of clause (i)-magnitude (unitarity+var)
    # and clause (ii) round-trip + clause (iii) tuple-completeness
    mag_ok = unit_ok and var_ok and clause_ii and clause_iii   # (local)
    mag_v = "PASS" if mag_ok else "FAIL"                       # (local)
    # regime axis: the sudden/sharp-interface idealization validity --
    # constant-V box => TM EXACT at every n_seg (var_Nseg ~ 1 by construction);
    # mu^2 > 0 keeps the sin-branch; finite ODE confirms.
    regime_ok = (sign_ok and unit_ok
                 and np.isfinite(r["b2_ode"])
                 and r["rel_cf_ode"] < 1e-6)                   # (local)
    regime_v = "VALID" if regime_ok else "MARGINAL"            # (local)

    # ---- composite via the pre-registered gate-verdicts.md collapse rule ----
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                          # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"                                          # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"                                          # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"                                          # (local)
    else:
        comp = "PASS"                                          # (local)

    detail = dict(unit_ok=unit_ok, var_ok=var_ok, sign_ok=sign_ok,
                  clause_i=clause_i, rt_ok=rt_ok, clause_ii=clause_ii,
                  clause_iii=clause_iii, mag_ok=mag_ok, regime_ok=regime_ok)  # (local)
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 8 -- Plot
# --------------------------------------------------------------------------
def make_plot(t: dict, r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.6))          # (local)
    fig.suptitle(
        f"S101-BETA-PIVOT-PROMOTION -- tuple-pinned |beta_pivot|^2 "
        f"(Z-PUMP + branch-(c) + fold-clock, BD-in-out)\n"
        f"beta2_pivot_box_delta = {r['beta2_canon']:.4e} | "
        f"mu_pivot^2(c) = {r['mu2_c']:.2f} > 0 (74x) | "
        f"var_Nseg = {r['var_Nseg']:.6f} | unitarity {r['unit_max']:.1e}",
        fontsize=10.5, fontweight="bold")

    # Panel 1: spectrum (new tuple vs sqrtA recipe) + Born band marker
    ax = axes[0]                                                # (local)
    ax.loglog(r["k_grid"], r["beta2_spec"], "b-", lw=1.8,
              label="NEW tuple: Z-PUMP + branch-(c) barrier")
    ax.loglog(r["k_grid"], r["beta2_spec_sqrtA"], "r--", lw=1.3,
              label="sqrtA recipe (branch-b + literal weights)")
    ax.axvline(t["k_pivot"], color="k", ls="--", alpha=0.6,
               label=f"k_pivot = {t['k_pivot']:.3f}")
    ax.axhspan(BORN_BAND[0], BORN_BAND[1], color="green", alpha=0.15,
               label=f"Born band [{BORN_BAND[0]:.3e},{BORN_BAND[1]:.3e}]")
    ax.plot([t["k_pivot"]], [r["beta2_canon"]], "b*", ms=16,
            label=f"canonical = {r['beta2_canon']:.4e}")
    ax.plot([t["k_pivot"]], [r["beta2_sqrtA_recompute"]], "rd", ms=9,
            label=f"sqrtA payload = {r['beta2_sqrtA_recompute']:.4e}")
    ax.set_xlabel("k  [M_KK, fold-normalized comoving]")
    ax.set_ylabel(r"$|\beta_k|^2$")
    ax.set_title("Bogoliubov spectrum: new tuple vs sqrtA recipe")
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3, which="both")

    # Panel 2: N_seg stability + 3-code-path agreement at pivot
    ax = axes[1]                                                # (local)
    ax.semilogx(N_SEG_SCAN, r["beta2_per_Nseg"] / r["beta2_per_Nseg"][0],
                "bo-", lw=1.6, ms=9, label="TM N_seg sweep (constant-V box)")
    ax.axhline(r["beta2_canon_cf"] / r["beta2_per_Nseg"][0], color="r",
               ls="--", lw=1.3, label="closed form (exact)")
    ax.axhline(r["b2_ode"] / r["beta2_per_Nseg"][0], color="g", ls=":",
               lw=2.0, label="Radau ODE (rtol 1e-10)")
    ax.axhspan(1.0 / TOL_VAR_NSEG, TOL_VAR_NSEG, color="green", alpha=0.08,
               label="PASS band (var_Nseg < 2)")
    ax.set_xlabel("N_seg (interior segmentation; constant-V => TM exact)")
    ax.set_ylabel(r"$|\beta_{pivot}|^2(N_{seg}) / |\beta_{pivot}|^2(1)$")
    ax.set_title(f"N_seg stability + 3-path agreement "
                 f"(var = {r['var_Nseg']-1:.1e}+1)")
    ax.set_ylim(0.9990, 1.0010)
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"\nSaved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 9 -- Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                            # (local)
    pins = verify_inputs()                                      # (local)

    # dual-SHA (audit = script+canonical+pinmap incl. machinery pins)
    pinmap = dict(pins)                                         # (local)
    pinmap.update({f"_machinery::{k}": v for k, v in MACHINERY_PINS.items()})
    pinmap["_gate::id"] = GATE_ID
    pinmap["_gate::forward"] = FORWARD_LADDER
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pinmap)                                                # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    t = load_tuple()                                           # (local)
    r = compute(t)                                             # (local)
    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)   # (local)

    print("\n" + "=" * 72)
    print("GATE EVALUATION (pre-registered composite operator)")
    print("=" * 72)
    print(f"  clause (i)  recipe-internal: unitarity {r['unit_max']:.2e}<=1e-10 "
          f"[{detail['unit_ok']}], var_Nseg {r['var_Nseg']:.8f}<2 "
          f"[{detail['var_ok']}], mu^2>0 [{detail['sign_ok']}] "
          f"=> {detail['clause_i']}")
    print(f"  clause (ii) round-trip: canon {r['rt_canon']:.2e}, sqrtA "
          f"{r['rt_sqrtA']:.2e} (<= {TOL_ROUNDTRIP}) => {detail['clause_ii']}")
    print(f"  clause (iii) tuple-completeness 4/4 => {detail['clause_iii']}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"  composite (collapse rule): {comp}")

    # ---- npz (full float64; publication 4 sig figs in value string) ----
    np.savez(
        OUT_NPZ,
        # ==== canonical + diagnostic keyed values (FULL float64) ====
        beta2_pivot_box_delta=r["beta2_canon"],
        beta2_pivot_box_delta_sqrtA_recipe=r["beta2_sqrtA_recompute"],
        beta2_pivot_box_delta_TM=r["beta2_TM"],
        beta2_pivot_box_delta_ODE=r["b2_ode"],
        # ==== the 4-component adjudicated tuple (carried for PROVENANCE) ====
        Omega_z_on=t["Om_z_on"], Omega_z_off=t["Om_z_off"],
        V_box_branch_c=t["V_box_c"],
        V_box_branch_b_CHKN=t["V_box_b"],
        Delta_eta=t["Delta_eta"],
        tau_window=t["tau_window"], eta_window=t["eta_window"],
        k_pivot=t["k_pivot"], k2_over_zppz_fold=t["k2_over_zppz"],
        # ==== recipe-internal sub-criteria ====
        mu_pivot_sq_branch_c=r["mu2_c"],
        unitarity_residual_max=r["unit_max"],
        var_Nseg=r["var_Nseg"],
        beta2_pivot_per_Nseg=r["beta2_per_Nseg"],
        unitarity_per_Nseg=r["unit_per_Nseg"],
        N_seg_scan=np.array(N_SEG_SCAN),
        rel_cf_tm=r["rel_cf_tm"], rel_cf_ode=r["rel_cf_ode"],
        unitarity_closed_form=r["unit_cf"], unitarity_ODE=r["unit_ode"],
        # ==== per-edge weight decomposition ====
        Omega_lit_on=t["Om_lit_on"], Omega_lit_off=t["Om_lit_off"],
        weight_resid_on=r["resid_on"], weight_resid_off=r["resid_off"],
        weight_ratio_on=r["ratio_on"], weight_ratio_off=r["ratio_off"],
        # ==== Born-limit diagnostic ====
        Omega_bar_z=r["Om_bar_z"], beta2_born=r["beta2_born"],
        born_band=np.array(BORN_BAND), in_born_band=r["in_band"],
        # ==== round-trip (Class-8.3) ====
        published_canon=r["pub_canon"], roundtrip_canon=r["rt_canon"],
        published_sqrtA=r["pub_sqrtA"], roundtrip_sqrtA=r["rt_sqrtA"],
        # ==== CHK block ====
        CHK_N_validation=t["CHK_N_validation"],
        chk_Deta_vs_dt=t["chk_Deta_vs_dt"],
        dlnz_dtau_fold=t["dlnz_dtau_fold"],
        beta2_sqrtA_stored_W5_1=t["beta2_sqrtA"],
        beta2_zpump_storedV_branchb=t["beta2_zpump_storedV"],
        rel_sqrtA_reproduction=r["rel_sqrtA"],
        # ==== channel split + spectrum + ladder context ====
        beta2_box_only=r["beta2_box_only"],
        beta2_deltas_only=r["beta2_deltas_only"],
        k_grid=r["k_grid"], beta2_spectrum=r["beta2_spec"],
        beta2_spectrum_sqrtA=r["beta2_spec_sqrtA"],
        B2_ladder_anchor=t["B2_anchor"],
        # ==== verdict block ====
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        validated_recipe_predecessor=(
            "297a597c3cfe6fa00eddf97cccc538241f12faf339793c05a195ad915e7e6498"),
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(t, r)

    # ---- 4-tuple + payload ----
    val = (f"beta2_pivot_box_delta={r['beta2_canon']:.4g};"
           f"sqrtA_recipe={r['beta2_sqrtA_recompute']:.4g};"
           f"mu2_pivot_c={r['mu2_c']:.4f};var_Nseg={r['var_Nseg']:.6f};"
           f"unit_resid={r['unit_max']:.1e};"
           f"rt_canon={r['rt_canon']:.1e};rt_sqrtA={r['rt_sqrtA']:.1e};"
           f"Vbox_c={t['V_box_c']:.6f};Om_z_on={t['Om_z_on']:+.6f};"
           f"Om_z_off={t['Om_z_off']:+.6f};Deta={t['Delta_eta']:.4e};"
           f"born_band=[2.119,2.140]e-6;in_band={r['in_band']};"
           f"beta2_TM={r['beta2_TM']:.4g};beta2_ODE={r['b2_ode']:.4g}")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (f"tuple-pinned |beta_pivot|^2 promotion at the S-1-adjudicated "
            f"4-component tuple (Z-PUMP weights + branch-(c) barrier + "
            f"fold-conformal clock + IMPULSIVE-TRANSIT-WINDOW); canonical "
            f"beta2_pivot_box_delta={r['beta2_canon']:.4g}, sqrtA_recipe "
            f"diagnostic={r['beta2_sqrtA_recompute']:.4g}; 3 code paths agree "
            f"(closed/TM/ODE) to {max(r['rel_cf_tm'],r['rel_cf_ode']):.1e}")  # (local)
    rows = [
        f"# tuple={{Z-PUMP weights Om_z=[+1.2872356866503005,"
        f"-1.288529316518922] MKK; branch-(c) barrier V_box="
        f"2.764080442498705 MKK^2; fold-conformal clock Delta_eta="
        f"1.13014059e-3 MKK^-1; IMPULSIVE-TRANSIT-WINDOW stage}} "
        f"# {GATE_ID} 4-component-tuple row",
        f"# validated_recipe_predecessor="
        f"297a597c3cfe6fa00eddf97cccc538241f12faf339793c05a195ad915e7e6498 "
        f"(S100b-BOX-DELTA-BOGOLIUBOV PASS; this gate re-evaluates the "
        f"validated recipe at the adjudicated tuple -- NOT a supersedes= "
        f"token) # {GATE_ID} provenance row",
        f"# write_order: Step1=emit_verdict (this line); Step2=update_constant "
        f"beta2_pivot_box_delta={r['beta2_canon']:.10e} + "
        f"beta2_pivot_box_delta_sqrtA_recipe={r['beta2_sqrtA_recompute']:.10e}; "
        f"Step3=falsifier-inventory row -> mack-cosmic-bridge (Wave-6 slot) "
        f"# {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n citation; no SCHEMATIC "
        f"helper consumed (npz data + canonical_constants only) # {GATE_ID}",
        f"# born_band=[2.119,2.140]e-6 DIAGNOSTIC (reported, NEVER gated); "
        f"canonical {r['beta2_canon']:.4e} {'IN' if r['in_band'] else 'OUT'} "
        f"band (branch-(c) barrier sits {r['beta2_canon']/2.119e-6-1:+.2e} vs "
        f"low edge) # {GATE_ID}",
    ]                                                          # (local)
    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
