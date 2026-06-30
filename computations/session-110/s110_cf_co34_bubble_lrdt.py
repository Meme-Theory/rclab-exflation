#!/usr/bin/env python3
"""
S110 W4a-3  S110-CF-CO34-BUBBLE-LRDT — KK-bubble maturation + LRD-T transport
==============================================================================

Gate: S110-CF-CO34-BUBBLE-LRDT ([SIGN])   — session track
Classification: PHONONIC
Agent: mack-cosmic-bridge

TWO structurally-orthogonal legs sharing one gate (triage CF-CO-3 + CF-CO-4),
combined via wave-AND for the composite verdict.

  LEG A (bubble maturation).  Lift the reduced (4+8) Gregory-Laflamme TRANSIENT
    instability (inv-4 W2-4: min omega^2_eff = -44.26 M_KK^2 at lambda_GL = 0.944
    M_KK^-1, k_GL = 6.653, TRACK-B-BUBBLE, tau_dot^2-gated) toward a maturation
    test: compute growth integral N_efold over the impulsive transit and compare
    to the 1-e-fold threshold (permanent localized structure vs sub-critical
    fluctuation).
      sign  : omega^2_eff < 0 => growth_rate = sqrt(|omega^2_eff|) > 0 => amplitude
              GROWS.  sign_verdict(A) = PASS by construction.
      magn  : does N_efold reach >= 1 e-fold within the transit?
      PASS(A) iff N_efold >= 1 ; INFO(A) iff N_efold < 1 (transient sub-critical).

  LEG B (LRD-T transport).  Test whether the LRD photosphere T reaches the ~5000 K
    band [3500, 6500] K through the substrate-natural NON-SCALAR deg(T_{BZ->pivot})
    transport (CONSUMED from W3 CF-CV6B, dedup flag iii; deg_T_BZ_pivot = 2.0,
    NON-SCALAR), retaining the inv-7 W2-2 fold-robustness (Claim B, T varies 0.69%).
    The bare projection T_bare = 3.55e29 K (deg=0, scalar / container thinking) is
    25.85 OOM too high.
      sign  : a NON-SCALAR kernel < 1 DECREASES T from 3.55e29 K toward eV scale.
              sign_verdict(B) = PASS (direction correct: kernel<1 => T decreases).
      magn  : does the substrate-natural deg=+2 transport land T in [3500,6500] K?
      PASS(B) iff T_pivot in band via substrate-natural transport ; INFO(B) iff the
              substrate-natural transport overshoots (no fitted scale supplies the
              required ratio) ; FAIL(B) iff no substrate-natural transport reaches
              eV scale at all.

Composite (wave-AND): PASS iff A AND B both PASS ; FAIL iff either leg hard-FAILs ;
  INFO otherwise (mixed; records which formation leg is substrate-derived and which
  is held).

SUBSTRATE-FIRST (the explanatory arrow held substrate -> emergent/lab):
  Leg A: a "KK bubble" is a LOCALIZED reorganization of the fiber's spectral weight
    during transit — a GL instability of the M^4 x SU(3) acoustic metric, gated by
    tau_dot^2 (only the impulsive fold drives it).  D_K eigenvalues -> omega^2_eff
    (tau, k) -> growth -> bubble amplitude.  The static tau_dot->0 limit reproduces
    GL-STABILITY-63 (omega^2 >= 0).
  Leg B: the LRD photosphere T IS a substrate excitation energy READ AT the pivot
    scale.  The bare E=k_BT projection treats the substrate scale AS the observed
    scale (container thinking, 25 OOM wrong).  The substrate-natural NON-SCALAR
    deg(T)=+2 transport is the 54.04-decade BZ->pivot scale separation; it carries
    the dimensionful amplitude with homogeneity degree d/2 = 2.

DEPENDENCY (dedup flag iii): deg_T_BZ_pivot = 2.0 is IMPORTED from
  canonical_constants.py:716 (W3 CF-CV6B-DS-M4) — NOT re-derived here.  Leg A is
  independent and proceeds regardless.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/investigation-4/inv4_w2_gregory_laflamme_dynamical.npz  (omega^2_eff)
  - computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.npz  (T_bare)
  - computations/session-110/s110_cf_cv6b_ds_m4.npz  (deg(T), W3 — cross-check the canonical pin)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz  (L12 cache — provenance pin)

Output 4-tuple:
  (value=<N_efold | T_pivot>, scheme=GL-dynamical-12D + emergent-scale-transport-NON-SCALAR,
   convention=SUBSTRATE-NATURAL-BINDING, L_max=12)

DISCIPLINE
----------
- from canonical_constants import *   (deg_T_BZ_pivot, dt_transit, Mach_max_framework,
  tau_fold, M_KK, k_B, ...)
- every local/intermediate tagged # (local)
- the heavy 12D leg-A spectrum is ALREADY in the inv-4 cache; this gate consumes the
  cached omega^2_eff(tau,k) trajectory (no re-diagonalization) + a scalar deg(T)
  transport -> CPU, OMP capped at 8 (no matrix op >= 100x100)
- dual-SHA emitted; agent calls emit_verdict(session=110, track="session").
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # explicit, for clarity
    deg_T_BZ_pivot,          # = 2.0 NON-SCALAR, W3 CF-CV6B (dedup flag iii) — IMPORTED
    dt_transit,              # impulsive transit duration (M_KK^-1, S38)
    Mach_max_framework,      # 13.75 (van Hove fold velocity ratio)
    tau_fold,                # 0.19
    M_KK, k_B,
)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Pre-registration pins
# ---------------------------------------------------------------------------
SESSION = 110                                                       # (local) session track
GATE_ID = "S110-CF-CO34-BUBBLE-LRDT"                               # (local)
SCHEME = "GL-dynamical-12D + emergent-scale-transport-NON-SCALAR"  # (local)
CONVENTION = "SUBSTRATE-NATURAL-BINDING"                           # (local)
L_MAX = 12                                                         # (local)

# ---- Leg A pre-registered threshold ----
N_EFOLD_THRESHOLD = 1.0          # (local) >= 1 e-fold => permanent localized structure

# ---- Leg B pre-registered band ----
T_BAND_LO = 3500.0               # (local) K — LRD photosphere band lower (inv-7 5000K +/- 30%)
T_BAND_HI = 6500.0               # (local) K — LRD photosphere band upper
T_TARGET_K = 5000.0              # (local) comparison target (LRD Balmer-break; NOT a pin source)
# 54.04-decade BZ->pivot k-separation (canonical scale-tag; alpha_s/n_s scale separation,
# canonical_constants.py:628/629/716). The deg=+2 transport raises the kernel to this power.
N_DECADES_BZ_PIVOT = 54.04       # (local) substrate-natural BZ->pivot k-separation [decades]

# Static-limit cross-check (the inv-4 [SIGN] payload, re-verified for provenance)
STATIC_LIMIT_TOL = 1e-6          # (local)

OUT_NPZ = SESSION_DIR / "s110_cf_co34_bubble_lrdt.npz"
OUT_PNG = SESSION_DIR / "s110_cf_co34_bubble_lrdt.png"

GL_DYNAMICAL = COMPUTATIONS_DIR / "investigation-4" / "inv4_w2_gregory_laflamme_dynamical.npz"
LRD_TEMPERATURE = COMPUTATIONS_DIR / "investigation-7" / "inv7_w2_2_substrate_photosphere_temperature.npz"
DEG_TRANSPORT_W3 = SESSION_DIR / "s110_cf_cv6b_ds_m4.npz"
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"

INPUT_FILES = [CANONICAL, GL_DYNAMICAL, LRD_TEMPERATURE, DEG_TRANSPORT_W3, L12_CACHE]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+; first lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...  exists={p.exists()}")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — LEG A: bubble maturation
# ---------------------------------------------------------------------------
def compute_leg_A(gl) -> dict:
    """Growth-integral e-fold count over the impulsive transit.

    The inv-4 cache stores omega^2_eff(tau, k) at tau in {0, 0.1, 0.19, 0.22, 0.35}
    plus the local tau_dot at each tau.  The tau_dot^2-gating is BUILT INTO
    omega^2_eff: the new destabilizing term is DeltaK ~ -tau_dot^2 * k^2 * P, so the
    growth rate Gamma(tau) = sqrt(|omega^2_eff|) tracks tau_dot.

    Proper-time e-fold count (PHYSICALLY CORRECT):
        N_efold = int Gamma dt = int (Gamma/tau_dot) dtau    over the transit window
    Plan-stated tau-integral (the pre-registration's literal form, disclosed too):
        N_efold_tau = int Gamma dtau                          over {tau_dot^2 > 0}
    Both are computed and reported; the proper-time form is the gate verdict number.
    """
    tau_samples = np.asarray(gl["tau_samples"], dtype=float)        # (local) [0,0.1,0.19,0.22,0.35]
    # build per-tau min(omega^2_eff) and tau_dot from the cached keys
    keys = ["om2_tau_0p000_eff", "om2_tau_0p100_eff", "om2_tau_0p190_eff",
            "om2_tau_0p220_eff", "om2_tau_0p350_eff"]                # (local)
    tdkeys = ["taudot_0p000", "taudot_0p100", "taudot_0p190",
              "taudot_0p220", "taudot_0p350"]                        # (local)

    min_om2_eff = np.array([float(np.min(gl[k])) for k in keys])     # (local) min over k at each tau
    taudot = np.array([float(gl[t]) for t in tdkeys])                # (local) dtau/dt at each tau
    # growth rate Gamma(tau) = sqrt(|omega^2_eff|) where omega^2_eff < 0, else 0 (stable, no growth)
    gamma = np.where(min_om2_eff < 0.0, np.sqrt(np.abs(min_om2_eff)), 0.0)  # (local) M_KK

    # integrand for proper-time e-folds: Gamma/tau_dot (= dt-weighted growth).
    # Guard tau_dot==0 (stable endpoints have gamma==0 anyway).
    safe_td = np.where(taudot > 1e-12, taudot, np.inf)               # (local)
    integrand_dt = gamma / safe_td                                   # (local) dimensionless dN/dtau (proper-time)

    # trapezoid integrals over the tau-window covered by the samples
    # (numpy 2.x renamed trapz -> trapezoid; use it directly)
    _trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))    # (local) numpy 2.x / 1.x compat
    N_efold_proper = float(_trapz(integrand_dt, tau_samples))        # (local) int (Gamma/tau_dot) dtau
    N_efold_tau = float(_trapz(gamma, tau_samples))                  # (local) plan-literal int Gamma dtau

    # --- impulsive-transit cross-check (single-scale upper bound) ---
    # Peak growth Gamma_max over the impulsive transit window dt_transit:
    gamma_max = float(np.max(gamma))                                 # (local) M_KK  (= sqrt|global_min_om2_eff|)
    global_min_om2_eff = float(gl["global_min_om2_eff"])             # (local)
    N_efold_impulsive_ub = gamma_max * float(dt_transit)             # (local) Gamma_max * dt_transit (single-scale UB)

    # static-limit provenance (the inv-4 [SIGN] payload): tau_dot->0 must reproduce GL-STABILITY-63
    static_resid = float(gl["static_resid"])                         # (local)
    static_limit_ok = bool(gl["static_limit_ok"])                    # (local)
    static_sign_ok = (static_resid <= STATIC_LIMIT_TOL) and static_limit_ok  # (local)

    lambda_GL = float(gl["lambda_GL_dyn"])                           # (local) 0.944 M_KK^-1
    k_GL = float(gl["k_GL_dyn"])                                     # (local) 6.653

    # leg-A verdicts
    sign_A = "PASS" if global_min_om2_eff < 0.0 else "N/A"           # (local) instability EXISTS => growth direction +
    # use the proper-time (physically correct) e-fold count as the verdict number
    N_efold = N_efold_proper                                         # (local) the gate number
    if N_efold >= N_EFOLD_THRESHOLD:
        magn_A = "PASS"                                              # (local) bubble matures (permanent)
    else:
        magn_A = "INFO"                                              # (local) transient sub-critical
    # regime: the static-limit reproduction is leg A's regime-of-validity (the operator is built right)
    regime_A = "VALID" if static_sign_ok else "BREAKDOWN"            # (local)

    return {
        "tau_samples": tau_samples,
        "min_om2_eff": min_om2_eff,
        "taudot": taudot,
        "gamma": gamma,
        "integrand_dt": np.where(np.isfinite(integrand_dt), integrand_dt, 0.0),
        "N_efold_proper": N_efold_proper,
        "N_efold_tau": N_efold_tau,
        "N_efold_impulsive_ub": N_efold_impulsive_ub,
        "N_efold": N_efold,
        "gamma_max": gamma_max,
        "global_min_om2_eff": global_min_om2_eff,
        "lambda_GL": lambda_GL,
        "k_GL": k_GL,
        "static_resid": static_resid,
        "static_limit_ok": static_limit_ok,
        "static_sign_ok": static_sign_ok,
        "sign_A": sign_A,
        "magn_A": magn_A,
        "regime_A": regime_A,
    }


# ---------------------------------------------------------------------------
# Section 6 — LEG B: LRD-T transport
# ---------------------------------------------------------------------------
def compute_leg_B(lrd, w3) -> dict:
    """Apply the substrate-natural NON-SCALAR deg(T)=+2 transport to T_bare.

    Substitution chain (the directional + magnitude logic):
      Def B1: T_bare = 3.55e29 K  [inv-7 W2-2; bare E=k_BT projection, deg=0 scalar /
              container thinking; treats the BZ-scale energy AS the observed energy].
      Def B2: deg_T_BZ_pivot = +2 NON-SCALAR  [W3 CF-CV6B; canonical import].
      Def B3: T2-VACUOUS (scalar) => T_pivot = T_bare EXACTLY (no relief).
      Substitute: T_pivot = T_bare * kernel^deg, kernel = (k_pivot/k_BZ) = 10^(-54.04)
                  is the substrate-natural BZ->pivot scale ratio (kernel < 1).
      Direction: kernel < 1, deg = +2 > 0 => kernel^deg < 1 => T_pivot < T_bare
                 (T DECREASES). sign_verdict(B) = PASS (direction correct).
      Magnitude: does the substrate-natural transport LAND T in [3500, 6500] K?
                 substrate-natural over the full 54.04-dec separation => 10^(-108.08)
                 suppression => overshoots BELOW the band by ~82 OOM.  To land in band
                 a deg=+2 transport would need a 12.93-decade ratio that the substrate
                 does NOT supply (would be a FITTED scale) => INFO (held magnitude),
                 NOT FAIL (the eV-scale T is NOT structurally empty — both the bare
                 deg=0 and substrate-natural deg=2 transports are well-defined, they
                 just bracket the target by 25.85 OOM up and 82.23 OOM down).
    """
    T_bare = float(lrd["T_substrate_K"])                             # (local) 3.55e29 K
    claim_B = bool(lrd["claim_B"])                                   # (local) fold-robust (T varies 0.69%)
    frac_var_window = float(lrd["frac_var_window"])                  # (local) 0.00687

    deg = float(deg_T_BZ_pivot)                                      # (local) 2.0 (IMPORTED, dedup iii)
    deg_is_scalar = (deg == 0.0)                                     # (local) NON-SCALAR => False

    # cross-check the canonical pin against the W3 npz (provenance integrity)
    w3_deg = float(w3["deg_T_BZ_pivot"])                             # (local) should be 2
    deg_matches_w3 = bool(abs(deg - w3_deg) < 1e-9)                  # (local)

    # substrate-natural kernel: the BZ->pivot scale ratio (k_pivot/k_BZ) = 10^(-N_decades)
    log10_kernel = -N_DECADES_BZ_PIVOT                               # (local) -54.04
    # transported T (substrate-natural, deg=+2): log10(T_pivot) = log10(T_bare) + deg*log10(kernel)
    log10_T_bare = float(np.log10(T_bare))                          # (local)
    log10_T_pivot_natural = log10_T_bare + deg * log10_kernel        # (local)
    T_pivot_natural = 10.0 ** log10_T_pivot_natural                  # (local) substrate-natural transported T

    # the scalar (deg=0) / bare path, for contrast: T_pivot = T_bare (no relief)
    T_pivot_scalar = T_bare                                          # (local) deg=0 => unchanged (25.85 OOM high)

    # OOM diagnostics
    log10_target = float(np.log10(T_TARGET_K))                       # (local)
    oom_bare_above = log10_T_bare - log10_target                     # (local) +25.85 (bare overshoots UP)
    oom_natural_below = log10_target - log10_T_pivot_natural          # (local) +82.23 (natural overshoots DOWN)

    # required decades for a deg=+2 transport to land exactly at T_TARGET:
    #   deg * log10(kernel_needed) = log10(T_target/T_bare)
    log10_kernel_needed = (log10_target - log10_T_bare) / deg        # (local) -12.925
    decades_needed = -log10_kernel_needed                            # (local) 12.925 (NOT 54.04)
    # is the required scale the substrate-natural one? (within 5% relative)
    natural_supplies_band = bool(abs(decades_needed - N_DECADES_BZ_PIVOT)
                                 / N_DECADES_BZ_PIVOT < 0.05)         # (local) False — 12.93 != 54.04

    # band membership of the substrate-natural transported T
    in_band_natural = bool(T_BAND_LO <= T_pivot_natural <= T_BAND_HI)  # (local) False

    # leg-B verdicts
    # sign: kernel<1 and deg>0 => T_pivot < T_bare (DECREASE). The pre-registered direction is
    # "NON-SCALAR transport DECREASES T toward eV scale" => sign PASS iff T_pivot < T_bare.
    sign_B = "PASS" if (T_pivot_natural < T_bare) else "FAIL"        # (local)
    # magnitude: PASS iff substrate-natural transport lands in band; INFO iff overshoots
    # (substrate-natural transport well-defined but misses by a fixed OOM — held); FAIL iff
    # the eV-scale T is structurally unreachable by ANY substrate transport (it is not — the
    # bare and natural transports BRACKET the band, so the channel is non-empty).
    if in_band_natural:
        magn_B = "PASS"                                             # (local) substrate-natural lands in band
    elif natural_supplies_band:
        magn_B = "PASS"                                             # (local) (unreached branch; kept for completeness)
    else:
        # substrate-natural transport overshoots; the required ratio is NOT substrate-natural
        # (would be a fitted 12.93-dec scale). Held magnitude => INFO (fitted/scalar reading).
        magn_B = "INFO"                                             # (local)
    # regime: leg B's regime-of-validity is the inv-7 fold-robustness (Claim B); VALID iff fold-robust
    regime_B = "VALID" if claim_B else "MARGINAL"                   # (local)

    return {
        "T_bare": T_bare,
        "claim_B": claim_B,
        "frac_var_window": frac_var_window,
        "deg": deg,
        "deg_is_scalar": deg_is_scalar,
        "w3_deg": w3_deg,
        "deg_matches_w3": deg_matches_w3,
        "N_decades_BZ_pivot": N_DECADES_BZ_PIVOT,
        "log10_kernel": log10_kernel,
        "log10_T_bare": log10_T_bare,
        "log10_T_pivot_natural": log10_T_pivot_natural,
        "T_pivot_natural": T_pivot_natural,
        "T_pivot_scalar": T_pivot_scalar,
        "oom_bare_above": oom_bare_above,
        "oom_natural_below": oom_natural_below,
        "log10_kernel_needed": log10_kernel_needed,
        "decades_needed": decades_needed,
        "natural_supplies_band": natural_supplies_band,
        "in_band_natural": in_band_natural,
        "T_target_K": T_TARGET_K,
        "T_band_lo": T_BAND_LO,
        "T_band_hi": T_BAND_HI,
        "sign_B": sign_B,
        "magn_B": magn_B,
        "regime_B": regime_B,
    }


# ---------------------------------------------------------------------------
# Section 7 — Composite (wave-AND over the two legs)
# ---------------------------------------------------------------------------
def combine_legs(A, B) -> dict:
    """wave-AND composite over leg A and leg B.

    Per-leg 3-tuple collapse (gate-verdicts.md collapse rule), then AND.
      leg composite L = collapse(sign_L, magn_L, regime_L)
      composite = FAIL if either leg composite == FAIL
                = PASS if both leg composites == PASS
                = INFO otherwise (mixed)
    The reported 3-tuple is the AND-aggregate:
      sign_verdict   = PASS iff both legs sign PASS (else the weaker)
      magnitude_verdict = the weaker of the two magnitudes (FAIL>INFO>PASS)
      regime_verdict = the weaker of the two regimes (BREAKDOWN>MARGINAL>VALID)
    """
    def leg_collapse(sign, magn, regime):  # (local) gate-verdicts.md collapse
        if regime == "BREAKDOWN":
            return "FAIL"
        if sign == "FAIL":
            return "FAIL"
        if magn == "FAIL" and regime == "VALID":
            return "FAIL"
        if magn == "FAIL" and regime == "MARGINAL":
            return "INFO"
        if magn == "INFO":
            return "INFO"
        return "PASS"

    comp_A = leg_collapse(A["sign_A"], A["magn_A"], A["regime_A"])   # (local)
    comp_B = leg_collapse(B["sign_B"], B["magn_B"], B["regime_B"])   # (local)

    if comp_A == "FAIL" or comp_B == "FAIL":
        composite = "FAIL"                                          # (local)
    elif comp_A == "PASS" and comp_B == "PASS":
        composite = "PASS"                                         # (local)
    else:
        composite = "INFO"                                        # (local) mixed

    # AND-aggregate 3-tuple (the weaker per axis; sign: FAIL>N/A>PASS ordering -> weaker)
    sign_rank = {"FAIL": 0, "N/A": 1, "PASS": 2}                    # (local)
    magn_rank = {"FAIL": 0, "INFO": 1, "PASS": 2}                   # (local)
    regime_rank = {"BREAKDOWN": 0, "MARGINAL": 1, "VALID": 2}       # (local)
    sign_agg = min([A["sign_A"], B["sign_B"]], key=lambda v: sign_rank[v])      # (local)
    magn_agg = min([A["magn_A"], B["magn_B"]], key=lambda v: magn_rank[v])      # (local)
    regime_agg = min([A["regime_A"], B["regime_B"]], key=lambda v: regime_rank[v])  # (local)

    return {
        "comp_A": comp_A, "comp_B": comp_B, "composite": composite,
        "sign_agg": sign_agg, "magn_agg": magn_agg, "regime_agg": regime_agg,
    }


# ---------------------------------------------------------------------------
# Section 8 — Plot
# ---------------------------------------------------------------------------
def make_plot(A, B, C) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # (a) leg A: growth rate Gamma(tau) and tau_dot(tau) over the transit window
    ax = axes[0, 0]
    tau = A["tau_samples"]                                          # (local)
    ax.plot(tau, A["gamma"], "o-", color="navy", lw=2, label=r"$\Gamma(\tau)=\sqrt{|\omega^2_{eff}|}$")
    ax.plot(tau, A["taudot"], "s--", color="teal", lw=1.5, label=r"$\dot\tau(\tau)$ (transit speed)")
    ax.axvline(tau_fold, color="k", ls=":", lw=1, label=f"$\\tau_{{fold}}$={tau_fold}")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"rate [$M_{KK}$]")
    ax.set_title(r"(a) Leg A: $\Gamma\approx\dot\tau$ ($\dot\tau^2$-gated growth)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) leg A: e-fold count vs threshold
    ax = axes[0, 1]
    bars = ax.bar(["N_efold\n(proper-time)", r"$\int\Gamma d\tau$" + "\n(plan-literal)", "impulsive\nUB"],
                  [A["N_efold_proper"], A["N_efold_tau"], A["N_efold_impulsive_ub"]],
                  color=["navy", "slategray", "lightsteelblue"])
    ax.axhline(N_EFOLD_THRESHOLD, color="crimson", ls="--", lw=1.5, label="1 e-fold threshold")
    ax.set_ylabel("N e-folds")
    ax.set_yscale("log")
    ax.set_title(f"(b) Leg A: bubble {'matures' if A['magn_A']=='PASS' else 'TRANSIENT (sub-critical)'}")
    for b, v in zip(bars, [A["N_efold_proper"], A["N_efold_tau"], A["N_efold_impulsive_ub"]]):
        ax.text(b.get_x() + b.get_width()/2, v, f"{v:.2e}", ha="center", va="bottom", fontsize=8)
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # (c) leg B: T ladder — bare / target band / substrate-natural transported
    ax = axes[1, 0]
    cats = ["T_bare\n(deg=0 scalar)", "TARGET\nband", "T_pivot\n(deg=+2 natural)"]  # (local)
    vals = [B["log10_T_bare"], np.log10(B["T_target_K"]), B["log10_T_pivot_natural"]]  # (local)
    colors = ["firebrick", "seagreen", "steelblue"]                # (local)
    ax.bar(cats, vals, color=colors)
    ax.axhspan(np.log10(B["T_band_lo"]), np.log10(B["T_band_hi"]), alpha=0.18, color="seagreen",
               label=f"band [{B['T_band_lo']:.0f},{B['T_band_hi']:.0f}] K")
    ax.set_ylabel(r"$\log_{10}(T\,[\mathrm{K}])$")
    ax.set_title(f"(c) Leg B: bare +{B['oom_bare_above']:.1f} OOM up;\n"
                 f"natural −{B['oom_natural_below']:.1f} OOM below band → INFO (held)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # (d) leg B: decades-needed vs substrate-natural separation
    ax = axes[1, 1]
    bars = ax.bar(["needed for band\n(deg=+2)", "substrate-natural\n(BZ→pivot)"],
                  [B["decades_needed"], B["N_decades_BZ_pivot"]],
                  color=["orange", "steelblue"])
    ax.set_ylabel("scale-ratio [decades]")
    ax.set_title(f"(d) Leg B: needed {B['decades_needed']:.2f} dec ≠ natural "
                 f"{B['N_decades_BZ_pivot']:.2f} dec\n(no fitted knob → magnitude held)")
    for b, v in zip(bars, [B["decades_needed"], B["N_decades_BZ_pivot"]]):
        ax.text(b.get_x() + b.get_width()/2, v, f"{v:.2f}", ha="center", va="bottom", fontsize=9, fontweight="bold")
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle(
        f"{GATE_ID}: leg A N_efold={A['N_efold']:.3e} ({C['comp_A']}) | "
        f"leg B T_pivot={B['T_pivot_natural']:.2e}K ({C['comp_B']}) | "
        f"composite {C['composite']} (sign={C['sign_agg']} mag={C['magn_agg']} regime={C['regime_agg']})",
        fontsize=11, fontweight="bold")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig(OUT_PNG, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  wrote {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 9 — Verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict, magnitude_verdict, regime_verdict,
                          extra_rows=None) -> dict:
    payload: dict = {
        "session": SESSION,
        "track": "session",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    gl = np.load(GL_DYNAMICAL, allow_pickle=True)                  # (local)
    lrd = np.load(LRD_TEMPERATURE, allow_pickle=True)              # (local)
    w3 = np.load(DEG_TRANSPORT_W3, allow_pickle=True)             # (local)

    A = compute_leg_A(gl)                                          # (local)
    B = compute_leg_B(lrd, w3)                                     # (local)
    C = combine_legs(A, B)                                         # (local)

    print("=" * 72)
    print(f"{GATE_ID}: KK-bubble maturation (leg A) + LRD-T transport (leg B)")
    print("=" * 72)
    print("\n--- LEG A: bubble maturation (tau_dot^2-gated dynamical GL) ---")
    print(f"  global_min_om2_eff   = {A['global_min_om2_eff']:.5f} M_KK^2  (k_GL={A['k_GL']:.4f}, lambda_GL={A['lambda_GL']:.4f} M_KK^-1)")
    print(f"  Gamma_max            = {A['gamma_max']:.5f} M_KK")
    print(f"  per-tau (tau, min_om2_eff, Gamma, tau_dot):")
    for i, ts in enumerate(A["tau_samples"]):
        print(f"      tau={ts:5.3f}  om2_eff={A['min_om2_eff'][i]:9.4f}  Gamma={A['gamma'][i]:8.5f}  tau_dot={A['taudot'][i]:8.5f}")
    print(f"  N_efold (proper-time int (Gamma/tau_dot) dtau) = {A['N_efold_proper']:.6e}   <-- VERDICT NUMBER")
    print(f"  N_efold (plan-literal int Gamma dtau)          = {A['N_efold_tau']:.6e}")
    print(f"  N_efold (impulsive Gamma_max*dt_transit UB)    = {A['N_efold_impulsive_ub']:.6e}")
    print(f"  threshold = {N_EFOLD_THRESHOLD} e-fold ; static-limit OK (GL-STABILITY-63 repro) = {A['static_sign_ok']} (resid={A['static_resid']:.2e})")
    print(f"  leg A: sign={A['sign_A']} magn={A['magn_A']} regime={A['regime_A']} -> {C['comp_A']}")

    print("\n--- LEG B: LRD-T transport (substrate-natural NON-SCALAR deg=+2) ---")
    print(f"  T_bare (inv-7, deg=0 scalar/container) = {B['T_bare']:.6e} K  (+{B['oom_bare_above']:.2f} OOM above 5000 K)")
    print(f"  deg_T_BZ_pivot (IMPORTED, W3 CF-CV6B)  = {B['deg']}  NON-SCALAR (scalar?={B['deg_is_scalar']}); matches W3 npz = {B['deg_matches_w3']}")
    print(f"  fold-robust (inv-7 Claim B)            = {B['claim_B']} (T varies {B['frac_var_window']*100:.3f}%)")
    print(f"  substrate-natural kernel = 10^({B['log10_kernel']:.2f})  (54.04-dec BZ->pivot k-separation)")
    print(f"  T_pivot (substrate-natural deg=+2)     = {B['T_pivot_natural']:.6e} K  (10^{B['log10_T_pivot_natural']:.4f})")
    print(f"     -> {B['oom_natural_below']:.2f} OOM BELOW the band [{B['T_band_lo']:.0f},{B['T_band_hi']:.0f}] K")
    print(f"  decades a deg=+2 transport NEEDS for band = {B['decades_needed']:.4f}  (substrate-natural = {B['N_decades_BZ_pivot']:.2f}; supplies band? {B['natural_supplies_band']})")
    print(f"  in_band_natural = {B['in_band_natural']}")
    print(f"  leg B: sign={B['sign_B']} magn={B['magn_B']} regime={B['regime_B']} -> {C['comp_B']}")

    print(f"\n--- COMPOSITE (wave-AND) ---")
    print(f"  leg A = {C['comp_A']} ; leg B = {C['comp_B']}")
    print(f"  >>> {C['composite']}  (sign={C['sign_agg']} magnitude={C['magn_agg']} regime={C['regime_agg']})")

    # persist
    np.savez(
        OUT_NPZ,
        # leg A
        tau_samples=A["tau_samples"], min_om2_eff=A["min_om2_eff"], taudot=A["taudot"],
        gamma=A["gamma"], integrand_dt=A["integrand_dt"],
        N_efold_proper=A["N_efold_proper"], N_efold_tau=A["N_efold_tau"],
        N_efold_impulsive_ub=A["N_efold_impulsive_ub"], N_efold=A["N_efold"],
        gamma_max=A["gamma_max"], global_min_om2_eff=A["global_min_om2_eff"],
        lambda_GL=A["lambda_GL"], k_GL=A["k_GL"],
        static_resid=A["static_resid"], static_limit_ok=A["static_limit_ok"],
        static_sign_ok=A["static_sign_ok"],
        N_efold_threshold=N_EFOLD_THRESHOLD,
        sign_A=A["sign_A"], magn_A=A["magn_A"], regime_A=A["regime_A"], comp_A=C["comp_A"],
        # leg B
        T_bare=B["T_bare"], claim_B=B["claim_B"], frac_var_window=B["frac_var_window"],
        deg_T_BZ_pivot=B["deg"], deg_is_scalar=B["deg_is_scalar"],
        w3_deg=B["w3_deg"], deg_matches_w3=B["deg_matches_w3"],
        N_decades_BZ_pivot=B["N_decades_BZ_pivot"], log10_kernel=B["log10_kernel"],
        log10_T_bare=B["log10_T_bare"], log10_T_pivot_natural=B["log10_T_pivot_natural"],
        T_pivot_natural=B["T_pivot_natural"], T_pivot_scalar=B["T_pivot_scalar"],
        oom_bare_above=B["oom_bare_above"], oom_natural_below=B["oom_natural_below"],
        log10_kernel_needed=B["log10_kernel_needed"], decades_needed=B["decades_needed"],
        natural_supplies_band=B["natural_supplies_band"], in_band_natural=B["in_band_natural"],
        T_target_K=B["T_target_K"], T_band_lo=B["T_band_lo"], T_band_hi=B["T_band_hi"],
        sign_B=B["sign_B"], magn_B=B["magn_B"], regime_B=B["regime_B"], comp_B=C["comp_B"],
        # composite
        composite=C["composite"], sign_agg=C["sign_agg"], magn_agg=C["magn_agg"], regime_agg=C["regime_agg"],
        # provenance
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"  wrote {OUT_NPZ.name}")
    make_plot(A, B, C)
    print()

    tag = (f"(value=N_efold={A['N_efold']:.4e}|T_pivot={B['T_pivot_natural']:.4e}K, "
           f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")  # (local)
    print(tag)

    # value payload: no single-quote chars (tool wraps value='...')
    value_payload = (
        f"legA_N_efold={A['N_efold']:.4e}(thr=1;{C['comp_A']}) "
        f"min_om2_eff={A['global_min_om2_eff']:.3f}M_KK2 lambda_GL={A['lambda_GL']:.4f} "
        f"legB_T_bare={B['T_bare']:.3e}K T_pivot_natural={B['T_pivot_natural']:.3e}K(band[3500,6500]K;{C['comp_B']}) "
        f"deg_T={B['deg']:.1f}_NONSCALAR oom_bare_up={B['oom_bare_above']:.2f} oom_natural_down={B['oom_natural_below']:.2f} "
        f"composite={C['composite']}"
    )  # (local)

    extra_rows = [
        f"# leg A: tau_dot^2-gated dynamical GL bubble; min omega^2_eff={A['global_min_om2_eff']:.4f} M_KK^2 (k_GL={A['k_GL']:.4f}, lambda_GL={A['lambda_GL']:.4f}); "
        f"N_efold_proper={A['N_efold_proper']:.4e} < 1 -> TRANSIENT sub-critical (sign PASS: omega^2_eff<0 grows; magnitude INFO); "
        f"static-limit GL-STABILITY-63 repro OK (resid={A['static_resid']:.1e}); Gamma~tau_dot (impulsive transit too brief, dt_transit={float(dt_transit):.3e} M_KK^-1)",
        f"# leg B: LRD-T deg(T)=+2 NON-SCALAR transport (IMPORTED canonical_constants.py:716 W3 CF-CV6B, dedup flag iii; matches W3 npz={B['deg_matches_w3']}); "
        f"T_bare={B['T_bare']:.3e}K (deg=0 scalar/container, +{B['oom_bare_above']:.2f} OOM up); T_pivot_natural={B['T_pivot_natural']:.3e}K over 54.04-dec sep (-{B['oom_natural_below']:.2f} OOM below band); "
        f"sign PASS (kernel<1=>T decreases); magnitude INFO (substrate-natural overshoots; band needs {B['decades_needed']:.2f}-dec ratio != 54.04-dec natural, no fitted knob)",
        f"# composite wave-AND: leg A={C['comp_A']} AND leg B={C['comp_B']} -> {C['composite']}; both legs sign-PASS, magnitude-held (the campaign sign-PASS/magnitude-FAIL pattern); "
        f"compact-object/LRD formation axis: GL-bubble structure REAL but transient, LRD-T eV-scale NOT substrate-natural-reachable (bracketed +25.85/-82.23 OOM)",
        f"# regulator_pin: leg A omega^2_eff from inv4_w2_gregory_laflamme_dynamical (Lichnerowicz TT + extrinsic-curvature DeltaK~-tau_dot^2 k^2); leg B deg=d/2=2 amplitude homogeneity (a_n^{{zeta}} heat-trace P_M4~sigma^-2)",
    ]  # (local)

    print_verdict_payload(C["composite"], value_payload, audit_sha, content_sha,
                          C["sign_agg"], C["magn_agg"], C["regime_agg"], extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {C['composite']} "
          f"(sign={C['sign_agg']} mag={C['magn_agg']} regime={C['regime_agg']}) (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
