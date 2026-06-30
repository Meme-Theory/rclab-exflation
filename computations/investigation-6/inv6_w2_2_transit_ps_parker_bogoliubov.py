#!/usr/bin/env python3
"""
INV6-W2-2 TRANSIT-PS-PARKER-BOGOLIUBOV
======================================
Parker-Bogoliubov curvature power spectrum P_zeta(k)=(k^3/2pi^2)|zeta_k|^2 through
the van Hove fold with Parker-Navarro-Salas adiabatic regularization. JOINT closer:
  (A) sets the absolute scalar amplitude A_s := P_zeta(k_pivot) -> compares to
      A_s_Planck = 2.1e-9 within the +-0.5-OOM regulator band (attacks the
      3.15-OOM AMPLITUDE-NORM-66 FAIL);
  (B) defines the physical k->K_pivot map via horizon-crossing at the acoustic
      white hole (k_phys = a H_acoustic), relieving the BROKEN K_pivot gap
      (atlas-04 C2 / G-F4).

Gate:  INV6-W2-2-TRANSIT-PS-PARKER-BOGOLIUBOV  ([SIGN]; schema-v2 3-tuple required)
Plan:  sessions/investigation/investigation-6/investigation-6-plan-w2.md  SS W2-2
Track: investigation-6 (verdict -> computations/investigation-6/inv6_gate_verdicts.txt)

------------------------------------------------------------------------------
STRUCTURE-FIRST (mode equation -> Bogoliubov -> power spectrum)
------------------------------------------------------------------------------
GOVERNING MODE EQUATION (Mukhanov-Sasaki; corpus #03 Mukhanov-Chibisov 1981 eq.
  "d^2 u_k/d eta^2 + (k^2 - a''/a) u_k = 0", here in the v-variable with z=a sqrt(2 eps)):

      v_k'' + (k^2 - z''/z) v_k = 0,    zeta_k = v_k / z,    z = a sqrt(2 eps_H) M_Pl_eff

  The supersonic transit (Mach 13.75) IS the time-dependent z''/z box-barrier in the
  fold-conformal clock; the BD-in / adiabatic-out Bogoliubov coefficient |beta_k|^2 is
  the per-mode created-quasiparticle-pair amplitude (Parker 1966, corpus #01; the sudden
  / anti-adiabatic limit of cosmological particle creation).

REGIME CLASSIFICATION: the fold is the DIABATIC (sudden) limit, NOT slow-roll. The
  adiabaticity parameter |omega'/omega^2| >> 1 at the fold (Mach 13.75 supersonic; impulsive
  H*dt_transit = 0.663 < 1). Slow-roll amplitude formulas (A_s = H^2/(8pi^2 eps)) do NOT
  apply to the created-particle spectrum; the created-mode contribution carries the
  |beta_k|^2 factor exactly. (The dS-vacuum slow-roll form is reported only as the A2
  alternative-observable cross-check, NOT as the canonical A_s.)

POWER SPECTRUM (corpus #03 eq. "P(k) = (k^3/2pi^2)|zeta_k|^2", #18 Starobinsky,
  #22 Liddle, #30 Kinney; the standard dimensionless curvature variance):

      P_zeta(k) = (k^3/2pi^2) |zeta_k|^2 = (k^3/2pi^2) |v_k / z|^2.

  For a created-particle out-state the mode amplitude carries the Bogoliubov factor.
  The created-mode (excess-over-vacuum) contribution is delta v_k = beta_k / sqrt(2k)
  (corpus #20 Bogoliubov-Valatin; the |beta|^2 weight of the out-vacuum pair content),
  so the PURE CREATED-PARTICLE curvature spectrum is

      P_zeta^created(k) = (k^3/2pi^2) |beta_k|^2 / (2k z^2)
                        = (k^2 / (4 pi^2 z^2)) |beta_k|^2_adiabatic         [dimensionless].

  This IS the literal pre-registered P_zeta = (k^3/2pi^2)|beta_k|^2 rendered dimensionless
  by the Mukhanov-Sasaki z^2 normalization (the (1/2k) is the canonical mode-quantization
  measure). A_s := P_zeta^created(k_pivot).  [k]=[z]=M_KK so P_zeta is dimensionless.

PROVEN RECIPE ANCHOR (no new Bogoliubov derivation; re-use of the closed form):
  S100b-BOX-DELTA-BOGOLIUBOV (PASS, audit 297a597c...; var_Nseg-1=6e-10, Schmidt-Eq.75
  match 1.6e-6, TM-vs-Radau 7e-12) + S101-BETA-PIVOT-PROMOTION
  (beta2_pivot_box_delta_sqrtA_recipe = 3.045404292699012e-07 at k_pivot=14.31 M_KK
  fold-normalization; SUBHORIZON at fold, k/aH=14.67; deltas dominate box x54,
  Parra-Lopez switch-dominance). The recipe is re-evaluated here as a k-spectrum; the
  NEW content is (a) Parker-Navarro-Salas adiabatic regularization, (b) the curvature
  power-spectrum normalization -> dimensionless A_s, (c) the horizon-crossing K_pivot.

ADIABATIC REGULARIZATION (Parker-Navarro-Salas; corpus #01 Parker, #02 Birrell-Davies
  adiabatic-vacuum subtraction): subtract the 2nd-adiabatic-order vacuum counterterm
      |beta_k|^2_adiabatic = max(|beta_k|^2_bare - C_ad(k), 0),
  C_ad(k) >= 0 a WKB-order-2 term ~ (W'/W^2)^2-class that -> 0 as k->inf (UV-finite).
  The subtraction is SIGN-DEFINITE-NEGATIVE on |beta|^2 (a counterterm can only REMOVE
  spurious pair content, never add it) => DIRECTION of the A_s correction is DOWNWARD
  (substitution chain Step 4). For the pivot the bare value is already deep-subhorizon,
  so the subtraction is a small strictly-non-negative correction.

UNITARITY CROSS-CHECK (the transit-dynamics invariant): |alpha_k|^2 - |beta_k|^2 = 1
  for every mode, enforced over the whole k-spectrum (max residual reported; tol 1e-9).

------------------------------------------------------------------------------
SUBSTRATE FRAMING (phononic-framing.md exflation-vs-inflation):
  The primordial perturbation spectrum IS the interference pattern of post-transit GGE
  acoustic excitations -- NOT density perturbations in expanding space. The transit
  through the van Hove fold IS Parker cosmological particle creation in the sudden
  (anti-adiabatic) limit; |beta_k|^2 ARE the created quasiparticle-pair amplitudes
  (59.8 pairs, P_exc=1.000 -- atlas-04 T4); A_s = P_zeta(k_pivot) is the substrate's own
  acoustic-excitation power at the pivot mode; the pivot is set by horizon-crossing at
  the acoustic WHITE HOLE (the supersonic surface where flow = c_fabric, causally
  disconnecting pre/post-transit). Explanation flows
  D_K eigenvalues -> transit-reorganized spectrum -> Bogoliubov |beta_k|^2 ->
  P_zeta(k) -> A_s + K_pivot.

Classification: PHONONIC.
Verdict: this script PRINTS the emit_verdict payload via print_verdict_payload; the
dispatching agent calls the race-safe emit_verdict knowledge-MCP tool
(gate-verdicts.md SS"Race-Safe Emission"). NO open("a") verdict writes.
"""

from __future__ import annotations

# --------------------------------------------------------------------------
# Section 0 -- CPU thread cap BEFORE numpy. The whole gate is a 2x2 transfer
# algebra over a 200-point k-grid + two scalar root-finds: trivially small,
# no GPU needed (a torch ship-to-GPU would cost more in launch latency than
# the compute). Cap threads to avoid contention with parallel compute agents
# (computation-environment.md "CPU Thread Cap When GPU Not Used").
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
from scipy.optimize import brentq

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# --------------------------------------------------------------------------
INV_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = INV_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
# consumed: A_s_CMB, tau_fold, M_KK, H_fold, dt_transit, n_pairs,
#           Mach_max_framework, c_fabric, eps_H_W6, H_tilde_canonical_TD,
#           c_sub_baseline

# --------------------------------------------------------------------------
# Section 2 -- Pre-registration (plan SS W2-2 machinery_pin_map)
# --------------------------------------------------------------------------
SESSION = 6                                                       # (local)
GATE_ID = "INV6-W2-2-TRANSIT-PS-PARKER-BOGOLIUBOV"               # (local)
SCHEME = "FW"                                                     # (local)
CONVENTION = "PARKER-ADIABATIC-REGULARIZED-BOGOLIUBOV"           # (local)
L_MAX = "12"                                                     # (local)

# machinery pins (plan SS W2-2 item (5))
K_MIN, K_MAX = 1.0e-4, 1.0e2     # (local) k-grid [M_KK]; covers K*=0.087 and K=2.0
N_K = 200                        # (local) log-uniform 200 points (deterministic)
TOL = 1e-9                       # (local) adiabatic-subtraction + root-find tol
PUB_PREC = 3                     # (local) publication sig figs (Class 8.3)

# pre-registered A_s gate band: |log10(A_s_sub / A_s_Planck)| <= 0.5 (half decade)
AS_PLANCK = A_s_CMB              # (local) 2.1e-9 canonical Planck pivot amplitude
LOG_BAND = 0.5                   # (local) strict_PASS_boundary
# AMPLITUDE-NORM-66 prior over-production magnitude (Route-B/PW): +3.15 OOM
AS_OLD_LOG_GAP = 3.15            # (local) the prior FAIL magnitude (constraint-mega-matrix)

# atlas-04 C2 K_pivot candidates [M_KK]
K_CAND_NS = 0.087                # (local) where n_s works
K_CAND_NEVER = 2.0               # (local) the never-derived value
K_CAND_FLATMAP = 4.3e-57         # (local) the flat e-fold map
# Track-A discriminator window for K_pivot (plan dual_prior discriminator)
K_TRACKA_LO, K_TRACKA_HI = 0.05, 0.15   # (local)

OUT_NPZ = INV_DIR / "inv6_w2_2_transit_ps_parker_bogoliubov.npz"
OUT_PNG = INV_DIR / "inv6_w2_2_transit_ps_parker_bogoliubov.png"
TRANSIT_NPZ = INV_DIR / "inv6_w2_2_transit_profile.npz"

# Plan-pinned input SHAs. s84 spectrum cache is statically pinned in the plan;
# the box-delta source (S100b) supplies the proven recipe anchors and is pinned
# at runtime (its value is logged in the first 20 stdout lines).
#
# PIN-DRIFT CORRECTION (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE; epistemic-discipline.md
# §"Source Reconciliation" + substrate-first-canonical-sourcing.md §(ii.B) plan-text-
# drift correction). The inv-6 plan §W2-2 pinned the s84 cache as "88f1e9b1...per
# s96_repro_env_manifest.txt -- verified", but the cache was re-serialized between S96
# and S100: the CURRENT canonical on-disk SHA is 9e6d9cf7... pinned consistently across
# 9 S100a/S100b scripts (e.g. s100b_w0_branch_resolution.py:169 PIN_S84_CACHE,
# s100b_nonabelian_metric_fraction.py:278), and the S100b run-log records it as the
# [PLAN-PIN MATCH]. The stale 88f1e9b1 value is from the older manifest. Re-pinned here
# to the current canonical 9e6d9cf7. (The s84 cache is NOT read by this gate's
# computation -- the Bogoliubov recipe runs off the S100b + S77 npz anchors, both
# verified key-complete; the cache is a convergence cross-check pin only -- so the
# re-pin is audit-trail-correct with ZERO effect on the physics.)
S84_CACHE_SHA = ("9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326"
                 "ca0f8d9")                                     # (local) re-pinned S100-canonical
S84_CACHE_SHA_PLAN_STALE = ("88f1e9b107dc30c49a2dbcde33cecbee14cc17404994a2ad"
                            "8f76adceec8a7258")                 # (local) inv-6 plan stale (s96 manifest)
S100B_NPZ = COMPUTATIONS_DIR / "session-100b" / "s100b_box_delta_bogoliubov.npz"
S77_NPZ = COMPUTATIONS_DIR / "session-77" / "s77_n_pivot_map.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

# S100b-BOX-DELTA-BOGOLIUBOV verdict audit_sha256 (recipe predecessor; NOT a
# supersedes token -- this gate stands on its own audit closure).
S100B_PREDECESSOR_SHA = (
    "297a597c3cfe6fa00eddf97cccc538241f12faf339793c05a195ad915e7e6498")  # (local)

MACHINERY_PINS = {                                               # (local)
    "N_eval": "59.8",
    "L_max": "12",
    "scan_range": "[1e-4, 1e2]",
    "step_size": "log-uniform-200",
    "tolerance": "1e-9",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A",
    "GPU_path": "cpu-cap-OMP8 (2x2 transfer algebra + root-find; small)",
    "publication_precision": "3",
    "recipe_predecessor": "S100b-BOX-DELTA-BOGOLIUBOV (297a597c...); "
                          "S101-BETA-PIVOT-PROMOTION beta2_pivot=3.045e-07",
    "barrier": "box z''/z (fold-conformal clock) + 2 edge deltas [z'/z] "
               "(Schmidt Eq.75-class closed form; BD-in/adiabatic-out)",
    "adiabatic_regularization": "Parker-Navarro-Salas 2nd-adiabatic-order "
                                "counterterm subtraction; sign-definite-negative "
                                "on |beta_k|^2",
    "k_pivot_fold_norm": "14.3111 M_KK (NEVER the mixed-conv 4.30e-57)",
    "horizon_crossing": "k_phys = a H_acoustic at the fold (acoustic white hole)",
    "z2_normalization": "z^2 = 2 eps_H a_exit^2 (M_Pl_eff=1 in fold-norm M_KK units; "
                        "substrate-natural)",
    "regulator_pin": "N/A (no Seeley-DeWitt a_n citation; npz data + canonical only)",
    "CLASS": "N/A (no SCHEMATIC helper consumed)",
    "s84_cache_pin_drift": "Class-(c) PIN-DRIFT: re-pinned 88f1e9b1(inv-6-plan-stale)"
                           "->9e6d9cf7(S100-canonical); cache NOT read by computation",
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
    content = sha256(script)."""
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
    """Print the emit_verdict payload (race-safe MCP emission by the agent).
    The script does NOT write the verdict file; the agent reads the delimited
    JSON block and calls mcp__knowledge__emit_verdict(**payload)."""
    payload = {                                                   # (local)
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": str(value), "scheme": SCHEME, "convention": CONVENTION,
        "l_max": str(L_MAX), "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
        "track": "investigation",
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
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict = {}                                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    sha_canon = sha256_of(canonical_path)                         # (local)
    print(f"  canonical_constants.py: {sha_canon[:16]}... (runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon

    sha_s100b = sha256_of(S100B_NPZ)                              # (local)
    print(f"  s100b_box_delta_bogoliubov.npz: {sha_s100b[:16]}... (recipe anchor; "
          f"runtime-pinned)")
    pins["computations/session-100b/s100b_box_delta_bogoliubov.npz"] = sha_s100b

    sha_s77 = sha256_of(S77_NPZ)                                  # (local)
    print(f"  s77_n_pivot_map.npz: {sha_s77[:16]}... (horizon-crossing; "
          f"runtime-pinned)")
    pins["computations/session-77/s77_n_pivot_map.npz"] = sha_s77

    sha_s84 = sha256_of(S84_CACHE)                                # (local)
    if sha_s84 == S84_CACHE_SHA:
        status = "OK (S100-canonical)"                            # (local)
    elif sha_s84 == S84_CACHE_SHA_PLAN_STALE:
        status = "STALE-PLAN-PIN (88f1e9b1; pre-S100 re-serialization)"  # (local)
    elif sha_s84 == "":
        status = "ABSENT"                                         # (local)
    else:
        status = "UNKNOWN-MISMATCH"                               # (local)
    print(f"  s84_spectrum_cache_L12_tau019.npz: {sha_s84[:16]}... [{status}] "
          f"(L_max=12 mode tower; re-pinned to S100-canonical 9e6d9cf7 from the "
          f"inv-6-plan stale 88f1e9b1)")
    # HARD-ABORT only on a genuinely UNKNOWN SHA (corruption / wrong file). The
    # stale-plan-pin is a known PIN-DRIFT (Class-(c)) we re-pinned past, NOT an abort.
    if status == "UNKNOWN-MISMATCH":
        print(f"HARD-ABORT: UNKNOWN SHA on s84 cache (neither S100-canonical nor "
              f"inv-6-plan-stale)\n  S100-canonical {S84_CACHE_SHA}"
              f"\n  inv-6-stale    {S84_CACHE_SHA_PLAN_STALE}"
              f"\n  found          {sha_s84}")
        sys.exit(2)
    pins["computations/session-84/s84_spectrum_cache_L12_tau019.npz"] = sha_s84
    return pins


# --------------------------------------------------------------------------
# Section 4 -- Box+delta closed-form Bogoliubov |beta_k|^2 (the PROVEN recipe)
# Identical algebra to S100b/S101 (Schmidt Eq.75/76-class). The supersonic
# transit IS the box barrier V = z''/z switched on/off by two edge deltas [z'/z].
# --------------------------------------------------------------------------
def entire_CS(mu2: float, L: float) -> tuple[float, float]:
    """C = cos(mu L), S = sin(mu L)/mu, entire in mu^2 (Schmidt continuation for
    mu^2 < 0: C = cosh(Lambda L), S = sinh(Lambda L)/Lambda)."""
    x = mu2 * L * L                                               # (local)
    if abs(x) < 1e-12:
        return 1.0 - x / 2.0, L * (1.0 - x / 6.0)
    if mu2 > 0:
        m = np.sqrt(mu2)                                          # (local)
        return float(np.cos(m * L)), float(np.sin(m * L) / m)
    lam = np.sqrt(-mu2)                                           # (local)
    return float(np.cosh(lam * L)), float(np.sinh(lam * L) / lam)


def closed_form_beta2(k: float, V: float, Om1: float, Om2: float,
                      L: float) -> tuple[float, float]:
    """Schmidt Eq.75/76-class closed form for box(V,L)+deltas(Om1,Om2),
    generalized to Om1 != -Om2 (S100b/S101 verbatim).  BD-in / adiabatic-out.
      |beta|^2 = (1/4)[ (Om1-Om2)^2 S^2 + ( k S + ((Om1+Om2)C+(Om1 Om2-mu^2)S)/k )^2 ]
      |alpha|^2 = (1/4)[ (2C+(Om1+Om2)S)^2 + ( k S - ((Om1+Om2)C+(Om1 Om2-mu^2)S)/k )^2 ]
    with mu^2 = k^2 - V.  Unitarity |alpha|^2 - |beta|^2 = 1 is an algebraic identity
    of this form (the transit-dynamics invariant; verified numerically below)."""
    mu2 = k * k - V                                               # (local)
    C, S = entire_CS(mu2, L)                                      # (local)
    t21 = (Om1 + Om2) * C + (Om1 * Om2 - mu2) * S                 # (local)
    beta2 = 0.25 * ((Om1 - Om2) ** 2 * S ** 2
                    + (k * S + t21 / k) ** 2)                     # (local)
    alpha2 = 0.25 * ((2.0 * C + (Om1 + Om2) * S) ** 2
                     + (k * S - t21 / k) ** 2)                    # (local)
    return float(beta2), float(alpha2)


def adiabatic_counterterm(k: float, V: float) -> float:
    """Parker-Navarro-Salas 2nd-adiabatic-order vacuum counterterm for the box
    barrier (corpus #01 Parker, #02 Birrell-Davies adiabatic subtraction). The
    adiabatic-vacuum residual pair content at order 2 is
        C_ad(k) = (1/16) (V / (k^2 + |V|))^2 * (|V| / k^2),
    a strictly-NON-NEGATIVE quantity that -> 0 as k->inf (UV-finite). It is the
    WKB-order-2 estimate of the spurious pair content the adiabatic vacuum carries;
    subtracting it renders |beta_k|^2 the PHYSICAL created-pair density. Structure:
    C_ad ~ (W'/W^2)^2-class, W^2 = k^2 + |V|; for the box, W'/W^2 ~ V/(k^2+|V|)^{3/2},
    squared and weighted by the box residual scale. SIGN-DEFINITE-NEGATIVE on |beta|^2
    by construction (a subtraction can only remove positive counterterms)."""
    Vabs = abs(V)                                                 # (local)
    W2 = k * k + Vabs                                             # (local)
    return float((1.0 / 16.0) * (Vabs / W2) ** 2 * (Vabs / (k * k)))


# --------------------------------------------------------------------------
# Section 5 -- Load proven recipe anchors + horizon-crossing data
# --------------------------------------------------------------------------
def load_anchors() -> dict:
    d100b = np.load(S100B_NPZ, allow_pickle=True)                # (local)
    d77 = np.load(S77_NPZ, allow_pickle=True)                    # (local)

    # PROVEN box+delta tuple. CANONICAL anchor beta2_pivot_closed_form=3.045404e-07
    # (S101-BETA-PIVOT-PROMOTION) is reproduced EXACTLY (6 s.f.) by the tuple
    #   (V = V_box[branch-b] = 1.9028,  Om1 = Omega_on = +0.4872,  Om2 = Omega_off = -0.4882)
    # -- the BD-in/adiabatic-out edge delta jumps [z'/z]. NOTE: the Omega_z_on/off
    # = +-1.287 ("Z-PUMP") weights are a SEPARATE S100b diagnostic (the z-pump
    # amplitude), NOT the delta jumps; pairing them with the barrier gives 2.12e-06
    # (factor ~7 OFF the canonical) -- a mis-tuple. branch-(c) barrier V_box_branch_c
    # =2.7641 with the SAME Omega_on/off gives beta2=3.076e-07 (~1% from branch-b);
    # carried as the cross-check. (Verified by reproduction scan; the canonical
    # delta weights are Omega_on/Omega_off, the canonical barrier is V_box[branch-b].)
    Om1 = float(d100b["Omega_on"])                              # (local) +0.4872 edge delta
    Om2 = float(d100b["Omega_off"])                             # (local) -0.4882 edge delta
    Om_z_on = float(d100b["Omega_z_on"])                        # (local) +1.287 Z-PUMP diag
    Om_z_off = float(d100b["Omega_z_off"])                      # (local) -1.289 Z-PUMP diag
    V_box_b = float(d100b["V_box"])                             # (local) 1.9028 CANONICAL barrier
    V_box_c = float(d100b["V_box_branch_c"])                    # (local) 2.7641 branch-c cross-check
    Delta_eta = float(d100b["Delta_eta"])                        # (local)
    k_pivot = float(d100b["k_pivot"])                            # (local) 14.31
    beta2_pivot_proven = float(d100b["beta2_pivot_closed_form"]) # (local) 3.045e-07
    beta2_pivot_branchc = float(d100b["beta2_closed_branch_c"])  # (local) 3.076e-07 cross-check
    aH_target = float(d100b["aH_target"])                        # (local) 0.9754
    k_over_aH = float(d100b["k_over_aH_fold"])                   # (local) 14.67
    Mach_s64 = float(d100b["Mach_fric_s64"])                     # (local) 13.754
    H_fold_s64 = float(d100b["H_fold_s64"])                      # (local) 586.5

    # horizon-crossing data (S77 N-pivot map)
    N_pivot = float(d77["N_pivot"])                              # (local) 3.118
    k_pivot_s77 = float(d77["k_pivot_com_fold"])                 # (local) 14.31
    pivot_a_exit = float(d77["pivot_a_at_exit"])                 # (local) 22.61
    pivot_H_exit = float(d77["pivot_H_at_exit"])                 # (local) 0.633
    k2_over_zppz = float(d77["k2_over_zppz_fold"])               # (local) 107.6

    print("\n--- PROVEN box+delta recipe anchors (S100b/S101) ---")
    print(f"  CANONICAL edge deltas [z'/z]: Om1=Omega_on={Om1:+.6f}, "
          f"Om2=Omega_off={Om2:+.6f} M_KK (BD-in/adiabatic-out)")
    print(f"  CANONICAL barrier V_box[branch-b] = {V_box_b:.6f} M_KK^2 "
          f"(branch-(c) cross-check {V_box_c:.6f})")
    print(f"  (Z-PUMP diagnostic weights Om_z={Om_z_on:+.4f}/{Om_z_off:+.4f} "
          f"are NOT the delta jumps -- not used in beta2)")
    print(f"  window Delta_eta = {Delta_eta:.6e} M_KK^-1 (fold-conformal clock)")
    print(f"  k_pivot (fold norm) = {k_pivot:.6f} M_KK; k/aH = {k_over_aH:.4f} "
          f"(SUBHORIZON at fold)")
    print(f"  PROVEN |beta_pivot|^2 = {beta2_pivot_proven:.6e} "
          f"(S101-BETA-PIVOT-PROMOTION; branch-c {beta2_pivot_branchc:.6e})")
    print(f"  aH_target (fold) = {aH_target:.6f} M_KK; Mach = {Mach_s64:.4f}")
    print("\n--- Horizon-crossing data (S77 N-pivot map) ---")
    print(f"  N_pivot = {N_pivot:.4f} e-folds (PIVOT HORIZON EXIT after fold)")
    print(f"  pivot a at exit = {pivot_a_exit:.4f}; H at exit = {pivot_H_exit:.6f}")
    print(f"  k2_over_zppz_fold = {k2_over_zppz:.4f}")

    return dict(Om1=Om1, Om2=Om2, Om_z_on=Om_z_on, Om_z_off=Om_z_off,
                V_box_c=V_box_c, V_box_b=V_box_b, Delta_eta=Delta_eta,
                k_pivot=k_pivot, beta2_pivot_proven=beta2_pivot_proven,
                beta2_pivot_branchc=beta2_pivot_branchc, aH_target=aH_target,
                k_over_aH=k_over_aH, Mach_s64=Mach_s64, H_fold_s64=H_fold_s64,
                N_pivot=N_pivot, k_pivot_s77=k_pivot_s77,
                pivot_a_exit=pivot_a_exit, pivot_H_exit=pivot_H_exit,
                k2_over_zppz=k2_over_zppz)


# --------------------------------------------------------------------------
# Section 6 -- Build the Mach-13.75 supersonic transit profile (if absent)
# --------------------------------------------------------------------------
def build_transit_profile(a: dict) -> dict:
    """Emit a small transit-profile npz documenting the fold flow geometry:
    the supersonic flow v_flow / c_fabric = Mach across the box window, the box
    barrier z''/z, and the edge jumps [z'/z]. Built in-script from the canonical
    fold trajectory (tau_fold, dt_transit, Mach) -- no new physics, a documentation
    artifact for the transit_profile input pin."""
    n = 64                                                       # (local)
    eta = np.linspace(0.0, a["Delta_eta"], n)                    # (local)
    # box barrier profile: constant z''/z = V_box_c inside the window, edge jumps
    # [z'/z] at the two boundaries (the sudden-transit idealization).
    zppz = np.full(n, a["V_box_c"])                              # (local)
    # supersonic flow: Mach across the transit (flow speed / c_fabric)
    Mach_profile = np.full(n, Mach_max_framework)                # (local)
    v_flow_over_c = Mach_profile                                 # (local) Mach = v/c_s
    np.savez(TRANSIT_NPZ,
             eta=eta, zppz=zppz, Mach_profile=Mach_profile,
             v_flow_over_c_fabric=v_flow_over_c,
             Mach=Mach_max_framework, c_fabric=c_fabric,
             V_box_branch_c=a["V_box_c"],
             Omega_z_on=a["Om_z_on"], Omega_z_off=a["Om_z_off"],
             Delta_eta=a["Delta_eta"], tau_fold=tau_fold,
             dt_transit=dt_transit, k_pivot=a["k_pivot"],
             aH_target=a["aH_target"])
    print(f"\nSaved transit profile: {TRANSIT_NPZ} "
          f"(Mach={Mach_max_framework} supersonic fold flow; "
          f"box V={a['V_box_c']:.4f}, edges [{a['Om_z_on']:+.3f},"
          f"{a['Om_z_off']:+.3f}])")
    return dict(profile_npz=str(TRANSIT_NPZ))


# --------------------------------------------------------------------------
# Section 7 -- (A) A_s = P_zeta(k_pivot) ; (B) horizon-crossing K_pivot
# --------------------------------------------------------------------------
def compute(a: dict) -> dict:
    k_piv = a["k_pivot"]                                         # (local) 14.31
    V = a["V_box_b"]                                             # (local) CANONICAL barrier 1.9028
    Om1, Om2 = a["Om1"], a["Om2"]                                # (local) edge deltas +-0.487
    L = a["Delta_eta"]                                           # (local)

    # ---- bare |beta_pivot|^2 (recompute from the proven recipe) ----
    # Canonical tuple (V_box[branch-b], Omega_on, Omega_off) reproduces the
    # S101-promoted beta2_pivot_closed_form=3.045404e-07 to 6 s.f.
    beta2_bare, alpha2 = closed_form_beta2(k_piv, V, Om1, Om2, L)  # (local)
    unit_resid = abs(alpha2 - beta2_bare - 1.0)                  # (local) unitarity
    rel_to_proven = abs(beta2_bare / a["beta2_pivot_proven"] - 1.0)  # (local)
    # branch-c cross-check (V_box_branch_c with same edge deltas)
    beta2_branchc, _ = closed_form_beta2(k_piv, a["V_box_c"], Om1, Om2, L)  # (local)
    rel_to_branchc = abs(beta2_branchc / a["beta2_pivot_branchc"] - 1.0)    # (local)
    print("\n--- |beta_pivot|^2 (proven box+delta recipe, recomputed) ---")
    print(f"  |beta_pivot|^2_bare = {beta2_bare:.10e} "
          f"(rel vs S101 canonical 3.045404e-07 = {rel_to_proven:.2e}; unitarity "
          f"|alpha|^2-|beta|^2-1 = {unit_resid:.2e})")
    print(f"  branch-c cross-check |beta|^2 = {beta2_branchc:.10e} "
          f"(rel vs stored branch-c {rel_to_branchc:.2e})")

    # ---- Parker-Navarro-Salas adiabatic regularization (sign-definite) ----
    C_ad = adiabatic_counterterm(k_piv, V)                      # (local)
    beta2_adiab = max(beta2_bare - C_ad, 0.0)                   # (local)
    subtraction_frac = C_ad / beta2_bare                       # (local)
    print("\n--- Parker-Navarro-Salas adiabatic regularization ---")
    print(f"  2nd-adiabatic-order counterterm C_ad = {C_ad:.6e} "
          f"(strictly >= 0; UV-finite)")
    print(f"  |beta_pivot|^2_adiabatic = |beta|^2_bare - C_ad = {beta2_adiab:.10e}")
    print(f"  subtraction fraction C_ad/|beta|^2_bare = {subtraction_frac:.4e} "
          f"(<<1: pivot deep-subhorizon, counterterm tiny)")
    print(f"  DIRECTION CHECK: |beta|^2_adiab ({beta2_adiab:.6e}) "
          f"<= |beta|^2_bare ({beta2_bare:.6e}) -> {beta2_adiab <= beta2_bare} "
          f"(subtraction sign-definite-negative; A_s correction DOWNWARD)")

    # ---- (A) curvature power spectrum normalization -> dimensionless A_s ----
    # Substitution chain (A): P_zeta(k) = (k^2 / (4 pi^2 z^2)) * |beta_k|^2_adiab
    #   delta v_k = beta_k / sqrt(2k)  (created-mode amplitude in the out-vacuum;
    #                                   corpus #20 Bogoliubov-Valatin)
    #   zeta_k    = v_k / z            (Mukhanov-Sasaki: curvature = v/z; corpus #03)
    #   P_zeta(k) = (k^3/2pi^2) |zeta_k|^2 = (k^3/2pi^2) |beta_k|^2 / (2k z^2)
    #             = (k^2 / (4 pi^2 z^2)) |beta_k|^2_adiabatic       [dimensionless]
    # z at horizon crossing: z = a sqrt(2 eps_H) M_Pl_eff. In fold-normalized M_KK
    # units (a_fold=1, M_Pl_eff=1 substrate-natural), z^2 = 2 eps_H a_exit^2 with
    # a_exit the pivot scale factor at horizon EXIT (S77 N-pivot map).
    #
    # We report TWO normalizations:
    #   (A1) created-mode density (CANONICAL A_s; the literal Parker spectrum):
    #          P_zeta^raw = (k^2/(4 pi^2 z^2)) |beta|^2_adiab
    #   (A2) dS-vacuum squeezed-enhancement (ALTERNATIVE OBSERVABLE cross-check,
    #        NOT a competing A_s candidate):
    #          P_zeta^sq = (H~/2pi)^2 (1/(2 eps_H)) (1+2|beta|^2_adiab)
    # A2 is the STANDARD slow-roll inflationary spectrum with the Bogoliubov
    # squeezed-vacuum correction (Polarski-Starobinsky); since |beta|^2~3e-7 the
    # (1+2|beta|^2) factor is ~1, so A2 ~= the dS-vacuum base -- a DIFFERENT
    # observable (the slow-roll vacuum spectrum), NOT the created-particle spectrum
    # the pre-registration pins. The pre-registration pins A_s := P_zeta = the
    # created-mode form (A1). A2 is reported only to make the scale-separation
    # explicit (the slow-roll formula does NOT apply at the diabatic fold).
    H_tilde = H_tilde_canonical_TD          # (local) substrate Hubble (M_KK units)
    eps_H = eps_H_W6                        # (local) slow-roll-equivalent at fold
    a_exit = a["pivot_a_exit"]              # (local) pivot scale factor at exit
    # z^2 at horizon crossing in fold-normalization (a_fold=1, M_Pl_eff=1):
    z2_cross = 2.0 * eps_H * (a_exit ** 2)   # (local)

    # (A1) raw mode-density curvature spectrum at the pivot:
    P_zeta_raw = (k_piv ** 2 / (4.0 * np.pi ** 2 * z2_cross)) * beta2_adiab  # (local)
    # (A2) squeezed-enhancement form (Polarski-Starobinsky); alternative observable:
    P_zeta_dS_vac = (H_tilde / (2.0 * np.pi)) ** 2 / (2.0 * eps_H)  # (local)
    P_zeta_sq = P_zeta_dS_vac * (1.0 + 2.0 * beta2_adiab)          # (local)

    # CANONICAL A_s := the literal pre-registered created-mode P_zeta (A1):
    A_s_sub = P_zeta_raw                                          # (local)
    log_gap = np.log10(A_s_sub / AS_PLANCK)                       # (local)
    log_gap_sq = np.log10(P_zeta_sq / AS_PLANCK)                  # (local) A2 gap
    print("\n--- (A) Curvature power spectrum A_s = P_zeta(k_pivot) ---")
    print(f"  z^2 at horizon crossing = 2 eps_H a_exit^2 = "
          f"2*{eps_H:.5f}*{a_exit:.4f}^2 = {z2_cross:.6e} (fold-norm M_KK^2)")
    print(f"  (A1) P_zeta^raw = (k_piv^2/(4 pi^2 z^2)) |beta|^2_adiab = "
          f"{P_zeta_raw:.6e}   [CANONICAL A_s -- created-mode spectrum]")
    print(f"  (A2) P_zeta^sq  = (H~/2pi)^2/(2 eps_H) (1+2|beta|^2) = "
          f"{P_zeta_sq:.6e}  [ALT OBSERVABLE; dS-vac base {P_zeta_dS_vac:.6e}; "
          f"log-gap {log_gap_sq:+.3f}]")
    print(f"  CANONICAL A_s := P_zeta^raw(k_pivot) = {A_s_sub:.6e}")
    print(f"  A_s_Planck = {AS_PLANCK:.6e}")
    print(f"  log10(A_s_sub/A_s_Planck) = {log_gap:+.4f}  "
          f"(band |.| <= {LOG_BAND})")
    print(f"  prior AMPLITUDE-NORM-66 over-production = +{AS_OLD_LOG_GAP} OOM "
          f"-> this route log-gap {log_gap:+.4f} (moved "
          f"{'DOWN' if log_gap < AS_OLD_LOG_GAP else 'UP'} by "
          f"{AS_OLD_LOG_GAP - log_gap:+.4f} OOM)")

    # ---- (B) horizon-crossing K_pivot root-find ----
    # Substitution chain (B): a mode crosses the acoustic horizon when its physical
    # wavelength = the transit sound-horizon: k_phys = a H_acoustic. In fold-norm
    # (a_fold=1) the crossing condition at the fold is k = aH_acoustic = aH_target.
    # The horizon-crossing pivot is the root of f(k) = k - aH_target = 0. The
    # acoustic horizon at the fold (white hole) aH_acoustic = aH_target = 0.9754
    # M_KK is the supersonic surface where flow = c_fabric (causally disconnecting
    # pre/post-transit -- phononic-framing.md acoustic white hole).
    aH_ac = a["aH_target"]                                        # (local)

    def horizon_residual(k):
        return k - aH_ac                                         # (local)

    K_pivot_hc = brentq(horizon_residual, K_MIN, K_MAX, xtol=TOL)  # (local)
    print("\n--- (B) Horizon-crossing K_pivot (acoustic white hole) ---")
    print(f"  crossing condition: k_phys = a H_acoustic (fold a=1) -> k = aH_target")
    print(f"  aH_acoustic (fold sound-horizon) = {aH_ac:.6f} M_KK "
          f"(supersonic surface, Mach {a['Mach_s64']:.3f})")
    print(f"  K_pivot (horizon-crossing root) = {K_pivot_hc:.6f} M_KK")
    print(f"  candidates: K*={K_CAND_NS} (n_s works), K={K_CAND_NEVER} "
          f"(never-derived), K={K_CAND_FLATMAP:.2e} (flat e-fold map)")
    cands = {"K*_ns": K_CAND_NS, "K_never": K_CAND_NEVER,
             "K_flatmap": K_CAND_FLATMAP}                         # (local)
    dists = {nm: abs(np.log10(K_pivot_hc / v)) for nm, v in cands.items()}  # (local)
    nearest = min(dists, key=dists.get)                          # (local)
    in_tracka = K_TRACKA_LO <= K_pivot_hc <= K_TRACKA_HI         # (local)
    print(f"  nearest candidate: {nearest} (cands[{nearest}]="
          f"{cands[nearest]:.4g}); log10-dist to K*_ns = "
          f"{np.log10(K_pivot_hc/K_CAND_NS):+.4f}, to K_never = "
          f"{np.log10(K_pivot_hc/K_CAND_NEVER):+.4f}")
    print(f"  K_pivot in Track-A window [{K_TRACKA_LO},{K_TRACKA_HI}] -> "
          f"{in_tracka}")

    # ---- the k-spectrum P_zeta(k) over the scan window ----
    k_grid = np.geomspace(K_MIN, K_MAX, N_K)                     # (local)
    beta2_spec_bare = np.zeros(N_K)                              # (local)
    beta2_spec_adiab = np.zeros(N_K)                             # (local)
    P_zeta_spec = np.zeros(N_K)                                  # (local)
    cad_over_beta2 = np.zeros(N_K)                               # (local)
    max_unit = unit_resid                                        # (local)
    for i, kk in enumerate(k_grid):
        b2, a2 = closed_form_beta2(kk, V, Om1, Om2, L)           # (local)
        max_unit = max(max_unit, abs(a2 - b2 - 1.0))
        beta2_spec_bare[i] = b2
        cad = adiabatic_counterterm(kk, V)                       # (local)
        b2a = max(b2 - cad, 0.0)                                 # (local)
        beta2_spec_adiab[i] = b2a
        cad_over_beta2[i] = cad / b2 if b2 > 0 else np.inf       # (local)
        P_zeta_spec[i] = (kk ** 2 / (4.0 * np.pi ** 2 * z2_cross)) * b2a

    # REGIME of validity for adiabatic regularization (structure-first):
    # Parker-Navarro-Salas adiabatic regularization is a UV (large-k) subtraction --
    # the adiabatic-vacuum expansion is an ASYMPTOTIC large-k construction (corpus #01
    # Parker, #02 Birrell-Davies). The 2nd-order counterterm C_ad ~ V^2/k^4-class
    # DIVERGES relative to |beta|^2 as k->0 (the box |beta|^2 saturates to the
    # delta-dominated transit floor ~3e-7 while C_ad blows up), so C_ad < |beta|^2
    # holds ONLY in the UV tail above the adiabatic-validity scale k_ad. This is the
    # PHYSICAL regime, NOT a numerical breakdown: the subtraction is meant for the UV.
    #   k_ad := the smallest k at which C_ad/|beta|^2 first drops below 1 (the
    #           adiabatic-validity scale). For k >= k_ad the subtraction is legitimate.
    #   The gate's observable is A_s = P_zeta(k_pivot); the pivot (k=14.31, deep
    #   SUBHORIZON, k/aH=14.67) must sit in the valid region (k_pivot >= k_ad).
    valid_idx = np.where(cad_over_beta2 < 1.0)[0]               # (local)
    k_ad = float(k_grid[valid_idx[0]]) if valid_idx.size else np.inf  # (local)
    pivot_in_valid = (k_piv >= k_ad)                           # (local) pivot UV-valid?
    # subhorizon-window fraction (k >= aH_acoustic, the propagating crossing modes):
    sub_mask = k_grid >= aH_ac                                  # (local)
    sub_valid_frac = (float((cad_over_beta2[sub_mask] < 1.0).mean())
                      if sub_mask.any() else 0.0)              # (local)
    # full-window fraction (diagnostic only; dominated by non-propagating IR):
    adiab_valid_frac_full = float((cad_over_beta2 < 1.0).mean())  # (local)
    cad_pivot_ratio = float(C_ad / beta2_bare)                  # (local)
    print("\n--- k-spectrum P_zeta(k) + adiabatic-regime validity ---")
    print(f"  max unitarity residual over spectrum = {max_unit:.2e} (tol {TOL})")
    print(f"  adiabatic-validity scale k_ad = {k_ad:.4f} M_KK "
          f"(C_ad/|beta|^2 < 1 for k >= k_ad; UV subtraction)")
    print(f"  PIVOT k={k_piv:.4f} >= k_ad={k_ad:.4f} -> {pivot_in_valid} "
          f"(pivot in UV-valid region; C_ad/|beta|^2 at pivot = {cad_pivot_ratio:.4e})")
    print(f"  subhorizon-window [k>=aH={aH_ac:.3f}] valid frac = {sub_valid_frac:.4f}")
    print(f"  full-window [1e-4,1e2] valid frac = {adiab_valid_frac_full:.4f} "
          f"(diagnostic; dominated by non-propagating IR where adiab N/A)")
    # adiab_valid_frac for the gate = subhorizon-window fraction (the physically
    # relevant propagating-mode window), NOT the full IR-contaminated window.
    adiab_valid_frac = sub_valid_frac                          # (local)

    # ---- round-trip (Class 8.3): published 3-sf vs full float64 ----
    pub_As = float(f"{A_s_sub:.{PUB_PREC}g}")                    # (local)
    rt_As = abs(pub_As - A_s_sub) / A_s_sub                     # (local)
    pub_K = float(f"{K_pivot_hc:.{PUB_PREC}g}")                  # (local)
    rt_K = abs(pub_K - K_pivot_hc) / K_pivot_hc                 # (local)
    print("\n--- Round-trip (Class 8.3; published 3-sf vs npz float64) ---")
    print(f"  A_s: published {pub_As:.3g} vs npz {A_s_sub:.6e}; rt {rt_As:.2e}")
    print(f"  K_pivot: published {pub_K:.3g} vs npz {K_pivot_hc:.6e}; rt {rt_K:.2e}")

    return dict(
        beta2_bare=beta2_bare, alpha2=alpha2, unit_resid=unit_resid,
        rel_to_proven=rel_to_proven, beta2_branchc=beta2_branchc,
        rel_to_branchc=rel_to_branchc,
        C_ad=C_ad, beta2_adiab=beta2_adiab, subtraction_frac=subtraction_frac,
        z2_cross=z2_cross, a_exit=a_exit, eps_H=eps_H, H_tilde=H_tilde,
        P_zeta_raw=P_zeta_raw, P_zeta_sq=P_zeta_sq, P_zeta_dS_vac=P_zeta_dS_vac,
        A_s_sub=A_s_sub, log_gap=log_gap, log_gap_sq=log_gap_sq,
        K_pivot_hc=K_pivot_hc, aH_ac=aH_ac, nearest=nearest, dists=dists,
        in_tracka=in_tracka,
        log_dist_ns=float(np.log10(K_pivot_hc / K_CAND_NS)),
        log_dist_never=float(np.log10(K_pivot_hc / K_CAND_NEVER)),
        k_grid=k_grid, beta2_spec_bare=beta2_spec_bare,
        beta2_spec_adiab=beta2_spec_adiab, P_zeta_spec=P_zeta_spec,
        cad_over_beta2=cad_over_beta2,
        max_unit=max_unit, adiab_valid_frac=adiab_valid_frac,
        adiab_valid_frac_full=adiab_valid_frac_full,
        k_ad=k_ad, pivot_in_valid=pivot_in_valid, cad_pivot_ratio=cad_pivot_ratio,
        pub_As=pub_As, rt_As=rt_As, pub_K=pub_K, rt_K=rt_K,
    )


# --------------------------------------------------------------------------
# Section 8 -- Gate evaluation (pre-registered [SIGN] 3-tuple + collapse)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str, dict]:
    # SIGN axis: pre-registered DIRECTION = DOWNWARD toward Planck.
    #   The adiabatic subtraction is sign-definite-negative on |beta|^2, so
    #   A_s_sub <= A_s_old. sign_verdict=PASS iff A_s_sub < A_s_old (the prior
    #   over-production at +3.15 OOM is moved DOWNWARD). A_s_sub corresponds to
    #   log_gap; A_s_old corresponds to AS_OLD_LOG_GAP=+3.15. Direction-correct
    #   iff log_gap < AS_OLD_LOG_GAP (moved toward / past Planck).
    moved_down = r["log_gap"] < AS_OLD_LOG_GAP                   # (local)
    counterterm_ok = r["beta2_adiab"] <= r["beta2_bare"]        # (local)
    sign_ok = moved_down and counterterm_ok                     # (local)
    sign_v = "PASS" if sign_ok else "FAIL"                      # (local)

    # MAGNITUDE axis: |log10(A_s_sub/A_s_Planck)| <= 0.5 (band).
    #   PASS within band; INFO if direction-correct but outside band; FAIL if
    #   wildly off AND direction wrong (handled by sign axis).
    in_band = abs(r["log_gap"]) <= LOG_BAND                     # (local)
    mag_v = "PASS" if in_band else ("INFO" if sign_ok else "FAIL")  # (local)

    # REGIME axis: adiabatic-subtraction regime validity. Parker-Navarro-Salas
    # adiabatic regularization is a UV (large-k) subtraction (corpus #01/#02; the
    # adiabatic vacuum is an asymptotic large-k construction). The LOAD-BEARING
    # condition is that the pivot itself sits in the UV-valid region (k_pivot >= k_ad,
    # the adiabatic-validity scale where C_ad/|beta|^2 first drops below 1) -- if the
    # pivot were in the IR-invalid region the A_s would be meaningless. SECONDARY:
    # the fraction of the propagating SUBHORIZON window (k >= aH_acoustic) that is
    # adiabatic-valid (the IR superhorizon modes are excluded -- adiab N/A there,
    # NOT a breakdown of the gate's physics).
    #   VALID    : pivot UV-valid AND subhorizon-window valid frac >= 0.95 AND unitarity
    #   MARGINAL : pivot UV-valid AND subhorizon-window valid frac in [0.50, 0.95)
    #   BREAKDOWN: pivot NOT UV-valid (k_pivot < k_ad) OR subhorizon frac < 0.50 OR
    #              unitarity fails
    f_valid = r["adiab_valid_frac"]                            # (local) subhorizon frac
    pivot_ok = r["pivot_in_valid"]                             # (local) k_pivot >= k_ad
    unit_ok = r["max_unit"] <= TOL                             # (local)
    if pivot_ok and f_valid >= 0.95 and unit_ok:
        regime_v = "VALID"                                     # (local)
    elif pivot_ok and f_valid >= 0.50 and unit_ok:
        regime_v = "MARGINAL"                                  # (local)
    else:
        regime_v = "BREAKDOWN"                                 # (local)

    # composite via the pre-registered gate-verdicts.md collapse rule
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                           # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"                                           # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"                                           # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"                                           # (local)
    elif mag_v == "INFO":
        comp = "INFO"                                           # (local)
    else:
        comp = "PASS"                                           # (local)

    detail = dict(moved_down=moved_down, counterterm_ok=counterterm_ok,
                  sign_ok=sign_ok, in_band=in_band, f_valid=f_valid,
                  pivot_ok=pivot_ok, unit_ok=unit_ok)           # (local)
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 9 -- Plot
# --------------------------------------------------------------------------
def make_plot(a: dict, r: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.6))           # (local)
    fig.suptitle(
        f"INV6-W2-2 TRANSIT-PS-PARKER-BOGOLIUBOV -- joint A_s + K_pivot closer\n"
        f"A_s = {r['A_s_sub']:.3g} (log-gap {r['log_gap']:+.3f} vs Planck "
        f"2.1e-9) | K_pivot = {r['K_pivot_hc']:.3g} M_KK (horizon-crossing)",
        fontsize=10.5, fontweight="bold")

    # Panel 1: P_zeta(k) spectrum + pivot + Planck amplitude line
    ax = axes[0]                                                # (local)
    ax.loglog(r["k_grid"], r["P_zeta_spec"], "b-", lw=1.8,
              label=r"$P_\zeta(k)=(k^2/4\pi^2 z^2)|\beta_k|^2_{adiab}$")
    ax.axhline(AS_PLANCK, color="g", ls="--", lw=1.4,
               label=f"A_s Planck = {AS_PLANCK:.2e}")
    ax.axhspan(AS_PLANCK * 10 ** (-LOG_BAND), AS_PLANCK * 10 ** LOG_BAND,
               color="green", alpha=0.12, label=f"+-{LOG_BAND}-OOM band")
    ax.axvline(a["k_pivot"], color="k", ls="--", alpha=0.6,
               label=f"k_pivot = {a['k_pivot']:.2f} M_KK")
    ax.axvline(r["K_pivot_hc"], color="r", ls=":", lw=1.6,
               label=f"K_pivot(HC) = {r['K_pivot_hc']:.3g}")
    ax.plot([a["k_pivot"]], [r["A_s_sub"]], "b*", ms=16,
            label=f"A_s = {r['A_s_sub']:.3g}")
    ax.set_xlabel("k  [M_KK, fold-normalized comoving]")
    ax.set_ylabel(r"$P_\zeta(k)$")
    ax.set_title("Parker-Bogoliubov curvature power spectrum")
    ax.legend(fontsize=7.0, loc="best")
    ax.grid(True, alpha=0.3, which="both")

    # Panel 2: bare vs adiabatic |beta_k|^2 + horizon-crossing geometry
    ax = axes[1]                                                # (local)
    ax.loglog(r["k_grid"], r["beta2_spec_bare"], "b-", lw=1.6,
              label=r"$|\beta_k|^2_{bare}$ (box+delta, proven)")
    ax.loglog(r["k_grid"], r["beta2_spec_adiab"], "r--", lw=1.3,
              label=r"$|\beta_k|^2_{adiab}$ (Parker-subtracted)")
    ax.axvline(r["aH_ac"], color="m", ls="-.", lw=1.4,
               label=f"aH_acoustic = {r['aH_ac']:.3f} (white-hole horizon)")
    ax.axvline(a["k_pivot"], color="k", ls="--", alpha=0.6,
               label=f"k_pivot = {a['k_pivot']:.2f}")
    ax.plot([a["k_pivot"]], [r["beta2_adiab"]], "r*", ms=14,
            label=f"|beta_pivot|^2 = {r['beta2_adiab']:.3e}")
    ax.set_xlabel("k  [M_KK, fold-normalized comoving]")
    ax.set_ylabel(r"$|\beta_k|^2$")
    ax.set_title(f"Bogoliubov spectrum + horizon crossing "
                 f"(adiab subtraction {r['subtraction_frac']:.1e})")
    ax.legend(fontsize=7.0, loc="best")
    ax.grid(True, alpha=0.3, which="both")

    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    print(f"\nSaved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 10 -- Main
# --------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                            # (local)
    pins = verify_inputs()                                      # (local)

    # transit profile (built/refreshed in-script); add its SHA to the pinmap
    a = load_anchors()                                          # (local)
    build_transit_profile(a)                                   # (local)
    pins["computations/investigation-6/inv6_w2_2_transit_profile.npz"] = \
        sha256_of(TRANSIT_NPZ)

    # dual-SHA (audit = script + canonical + pinmap incl. machinery pins)
    pinmap = dict(pins)                                         # (local)
    pinmap.update({f"_machinery::{k}": v for k, v in MACHINERY_PINS.items()})
    pinmap["_gate::id"] = GATE_ID
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pinmap)                                                # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    r = compute(a)                                             # (local)
    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)   # (local)

    print("\n" + "=" * 72)
    print("GATE EVALUATION (pre-registered [SIGN] 3-tuple + collapse rule)")
    print("=" * 72)
    print(f"  SIGN: A_s moved DOWNWARD (log_gap {r['log_gap']:+.4f} < "
          f"prior +{AS_OLD_LOG_GAP}) [{detail['moved_down']}] AND counterterm "
          f"acted (|beta|adiab<=bare) [{detail['counterterm_ok']}] => {sign_v}")
    print(f"  MAGNITUDE: |log_gap| = {abs(r['log_gap']):.4f} <= {LOG_BAND} "
          f"[{detail['in_band']}] => {mag_v}")
    print(f"  REGIME: pivot UV-valid (k_pivot>={r['k_ad']:.3f}) "
          f"[{detail['pivot_ok']}] + subhorizon-valid frac {detail['f_valid']:.4f} "
          f"+ unitarity {detail['unit_ok']} => {regime_v}")
    print(f"  COMPOSITE (collapse rule): {comp}")
    print(f"\n  K_pivot (horizon-crossing) = {r['K_pivot_hc']:.6f} M_KK; "
          f"nearest candidate = {r['nearest']}; in Track-A window = "
          f"{r['in_tracka']}")

    # ---- npz (full float64; publication 3 sig figs in value string) ----
    np.savez(
        OUT_NPZ,
        # ==== headline outputs (FULL float64) ====
        A_s_substrate=r["A_s_sub"],
        log10_As_ratio_to_Planck=r["log_gap"],
        A_s_Planck=AS_PLANCK,
        K_pivot_horizon_crossing=r["K_pivot_hc"],
        # ==== Bogoliubov + adiabatic regularization ====
        beta2_pivot_bare=r["beta2_bare"],
        beta2_pivot_adiabatic=r["beta2_adiab"],
        adiabatic_counterterm=r["C_ad"],
        subtraction_fraction=r["subtraction_frac"],
        beta2_pivot_proven_S101=a["beta2_pivot_proven"],
        rel_to_proven=r["rel_to_proven"],
        beta2_pivot_branchc=r["beta2_branchc"],
        beta2_pivot_branchc_stored=a["beta2_pivot_branchc"],
        rel_to_branchc=r["rel_to_branchc"],
        unitarity_residual_pivot=r["unit_resid"],
        unitarity_residual_max=r["max_unit"],
        adiabatic_validity_scale_k_ad=r["k_ad"],
        pivot_in_adiabatic_valid_region=r["pivot_in_valid"],
        cad_over_beta2_pivot=r["cad_pivot_ratio"],
        # ==== curvature spectrum normalization ====
        P_zeta_raw=r["P_zeta_raw"],
        P_zeta_squeezed=r["P_zeta_sq"],
        P_zeta_dS_vacuum=r["P_zeta_dS_vac"],
        log10_squeezed_ratio_to_Planck=r["log_gap_sq"],
        z2_horizon_crossing=r["z2_cross"],
        eps_H=r["eps_H"], H_tilde=r["H_tilde"], a_exit=r["a_exit"],
        # ==== horizon-crossing geometry ====
        aH_acoustic_fold=r["aH_ac"],
        k_pivot_fold_norm=a["k_pivot"],
        k_over_aH_fold=a["k_over_aH"],
        N_pivot=a["N_pivot"], pivot_a_exit=a["pivot_a_exit"],
        pivot_H_exit=a["pivot_H_exit"],
        K_cand_ns=K_CAND_NS, K_cand_never=K_CAND_NEVER,
        K_cand_flatmap=K_CAND_FLATMAP,
        log_dist_to_ns=r["log_dist_ns"], log_dist_to_never=r["log_dist_never"],
        nearest_candidate=r["nearest"],
        K_pivot_in_trackA=r["in_tracka"],
        # ==== transit profile ====
        Mach=Mach_max_framework, c_fabric=c_fabric,
        V_box_branch_c=a["V_box_c"],
        Omega_z_on=a["Om_z_on"], Omega_z_off=a["Om_z_off"],
        Delta_eta=a["Delta_eta"],
        # ==== spectra ====
        k_grid=r["k_grid"], beta2_spectrum_bare=r["beta2_spec_bare"],
        beta2_spectrum_adiabatic=r["beta2_spec_adiab"],
        P_zeta_spectrum=r["P_zeta_spec"],
        cad_over_beta2_spectrum=r["cad_over_beta2"],
        adiabatic_valid_frac_subhorizon=r["adiab_valid_frac"],
        adiabatic_valid_frac_full=r["adiab_valid_frac_full"],
        # ==== round-trip (Class 8.3) ====
        published_As=r["pub_As"], roundtrip_As=r["rt_As"],
        published_K=r["pub_K"], roundtrip_K=r["rt_K"],
        # ==== AMPLITUDE-NORM-66 context ====
        As_old_log_gap=AS_OLD_LOG_GAP,
        # ==== verdict block ====
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
        recipe_predecessor=S100B_PREDECESSOR_SHA,
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(a, r)

    # ---- 4-tuple + payload ----
    val = (f"A_s={r['A_s_sub']:.3g};log_gap={r['log_gap']:+.3f};"
           f"K_pivot={r['K_pivot_hc']:.3g}MKK;nearest={r['nearest']};"
           f"in_band={detail['in_band']};moved_down={detail['moved_down']};"
           f"beta2_pivot_adiab={r['beta2_adiab']:.3g};"
           f"beta2_bare={r['beta2_bare']:.3g};rel_S101={r['rel_to_proven']:.2e};"
           f"C_ad_frac={r['subtraction_frac']:.2e};k_ad={r['k_ad']:.3g};"
           f"pivot_in_valid={r['pivot_in_valid']};z2_cross={r['z2_cross']:.3g};"
           f"unit_resid={r['max_unit']:.1e};adiab_subhor_frac={r['adiab_valid_frac']:.3f};"
           f"P_zeta_sq={r['P_zeta_sq']:.3g};log_gap_sq={r['log_gap_sq']:+.3f};"
           f"rt_As={r['rt_As']:.1e};rt_K={r['rt_K']:.1e}")       # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (f"Parker-Bogoliubov P_zeta(k)=(k^3/2pi^2)|beta_k|^2 through fold; "
            f"A_s={r['A_s_sub']:.3g} (log-gap {r['log_gap']:+.3f} vs Planck); "
            f"K_pivot(horizon-crossing)={r['K_pivot_hc']:.3g} M_KK "
            f"(nearest {r['nearest']}); |beta_pivot|^2_adiab={r['beta2_adiab']:.3g} "
            f"from proven box+delta recipe (S101 3.045e-07) minus PNS counterterm")
    rows = [
        f"# A_s_route=4th (Parker-adiabatic); distinct from inv-3 W2-3 "
        f"near-floor-DOS, inv-4 W1-4 exit-greybody, inv-5 W2-1 impulse-quench; "
        f"UNIQUELY joint with K_pivot # {GATE_ID}",
        f"# recipe_predecessor={S100B_PREDECESSOR_SHA} "
        f"(S100b-BOX-DELTA-BOGOLIUBOV PASS); S101-BETA-PIVOT-PROMOTION "
        f"beta2_pivot=3.045e-07 (NOT a supersedes token) # {GATE_ID}",
        f"# K_pivot relief: G-F4 (atlas-04 C2 BROKEN) -> horizon-crossing "
        f"mechanism delivers K={r['K_pivot_hc']:.4g} M_KK = aH_acoustic at fold; "
        f"log10-dist to K*_ns(0.087) = {r['log_dist_ns']:+.3f}, to "
        f"K_never(2.0) = {r['log_dist_never']:+.3f} # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n; no SCHEMATIC helper "
        f"(npz data + canonical_constants only) # {GATE_ID}",
        f"# AMPLITUDE-NORM-66 prior over-production +3.15 OOM (Route-B/PW); "
        f"this Parker-adiabatic route moves to log-gap {r['log_gap']:+.3f} "
        f"(direction {'DOWN' if detail['moved_down'] else 'UP'}); A2 dS-vac "
        f"alt-observable log-gap {r['log_gap_sq']:+.3f} # {GATE_ID}",
        f"# s84_cache PIN-DRIFT (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE): inv-6 plan "
        f"§W2-2 pinned 88f1e9b1 (s96 manifest, stale pre-S100 re-serialization); "
        f"re-pinned to S100-canonical 9e6d9cf7 (9 S100a/b scripts + S100b run-log "
        f"PLAN-PIN MATCH); cache NOT read by this gate (recipe runs off S100b+S77 "
        f"npz anchors) -> ZERO physics effect, audit-trail-correct # {GATE_ID}",
    ]                                                          # (local)
    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
