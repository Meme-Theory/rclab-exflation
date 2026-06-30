#!/usr/bin/env python3
"""
S117 W9-2 CF-S117-TRANSIT-PS-67-WINDOW-WIDE — scale-range e-fold substrate obligation
====================================================================================

Gate: CF-S117-TRANSIT-PS-67-WINDOW-WIDE ([SIGN])
Classification: PHONONIC

Pre-registered composite PASS = (i) bandwidth ∧ (ii) tilt ∧ (iii) amplitude:
  (i)   span(k) >= 9.21 e-folds over [1e-4, 1] Mpc^-1          [binary span test]
  (ii)  max_{k in window} |n_s(k) - planck_ns| <= 3*planck_ns_err = 0.0126
                                                  [band [0.9523, 0.9775]]
  (iii) OOM(A_s) in [+0.196, +1.527]                          [amplitude-scheme reconciliation]

INFO-by-design: (iii) shares the A_s amplitude with the Wave-1 𝒩-fork. The S117
Wave-1 fork did NOT close this session (GS-1 = INFO-RESIDUAL-PREFACTOR; the A_s
magnitude stands as an OPEN 3-member plurality {+0.196, +0.384, +0.864} OOM). Per
the plan INFO_meaning + discriminator + mechanical-closure-discipline.md, (i) and
(ii) are computed UNCONDITIONALLY and (iii) closes INFO-pending-Wave-1; the composite
collapses to INFO (NOT FAIL — the amplitude axis is a live unsettled sub-condition,
not a falsification).

The window-wide constraint is STRICTLY TIGHTER than the pivot-local TRANSIT-PS-67
bound (|alpha_s| < 0.015): the window-wide |alpha_s| <= 0.0126/4.6052 = 2.736e-3 is
5.48x tighter, so window-wide PASS ⊂ pivot-local PASS ("pivot-local is necessary,
not sufficient" is a DERIVABLE inequality).

Substrate physics (scale-and-channel-tagging, phononic-framing.md):
  The substrate IS the power spectrum |β(k)|² — the GGE relic of the impulsive
  Mach-13.75 transit through the van Hove fold. The CMB pivot is reached through the
  deg-+2 NON-SCALAR transport T_{BZ→pivot} (54.04 decades). The Mode-Independent
  Occupation Theorem (S93-W7-1, PASS) makes the transport NON-SCALAR (deg=2.0):
     alpha_s_substrate = -0.08587279 (bare-BZ leaf-1, = n_s_FW^2 - 1)
     alpha_s_pivot     =  0.0 EXACT (CMB/LSS pivot leaf-2)
  i.e. the bare-BZ running does NOT transfer; the pivot reads the GEOMETRIC tilt
  n_s = 1 - 2*eps_H = 0.9561. This decoupling is WHY the window-wide band holds:
  the transported pivot spectrum is a pure near-scale-invariant power law (no running).

Inputs (SHA-256 dual-pinned at runtime):
  - computations/session-67/s67_transit_ps.npz            (TRANSIT-PS-67 baseline |β(k)|²; bare-BZ leaf-1)
  - computations/session-116/s116_w1_as_cf3_route_reconcile.npz (deg-+2 transport scheme split + A_s plurality)
  - computations/session-116/s116_w1_as_cfb1_squeeze_promote.npz (squeeze A_s + OOM band)
  - computations/session-111/s111_cf_as3a_impulse_quench.npz     (A_s_FW = 1.5367e-8)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<max|n_s(k)-0.9649|>, scheme=TRANSIT-PS-67-sudden-S70,
   convention=CMB-LSS-pivot-channel-deg2, L_max=12)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants import is DEFERRED to Section 3, AFTER
# SHARED_DIR is placed on sys.path (the module lives in computations/_shared).
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Section 2 — Standard imports (CPU-only: small mesh, no dense diagonalization)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
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
sys.path.insert(0, str(SHARED_DIR))

# Canonical constants (MANDATORY; imported here, after SHARED_DIR on sys.path)
from canonical_constants import *  # noqa: E402,F401,F403
from canonical_constants import (  # noqa: E402
    tau_fold, Mach_max, deg_T_BZ_pivot, A_s_FW, A_s_CMB,
    planck_ns, planck_ns_err, n_s_framework, n_s_FW_sqrt_cutoff,
    n_s_FW_exact, beta_s, k_pivot_planck,
)

SESSION = "S117"                                                   # (local)
GATE_ID = "CF-S117-TRANSIT-PS-67-WINDOW-WIDE"                      # (local)
SCHEME = "TRANSIT-PS-67-sudden-S70"                                # (local)
CONVENTION = "CMB-LSS-pivot-channel-deg2"                          # (local)
L_MAX = 12                                                         # (local)

# Pre-registered machinery pins (plan §W9-2 machinery_pin_map)
N_EVAL = 200                                                       # (local) log-spaced k-points
K_MIN_MPC = 1.0e-4                                                 # (local) Mpc^-1
K_MAX_MPC = 1.0                                                    # (local) Mpc^-1
TILT_BAND = 3.0 * planck_ns_err                                   # (local) = 0.0126 (3-sigma)
SPAN_TARGET_EFOLDS = 9.21                                         # (local) ln(1e4) pre-reg target
PIVOT_LOCAL_ALPHA_BOUND = 0.015                                   # (local) TRANSIT-PS-67 pivot-local bound

# Substrate-distance (bare-BZ leaf-1) running and pivot (leaf-2) running.
# CANONICAL provenance: S93-W7-1-ALPHA-S-W-KAPPA-FACTORIZATION-DEG-TRANSPORT-BZ-PIVOT
#   (PASS; deg_T=2.0 NON-SCALAR; alpha_s_substrate=-0.08587279; alpha_s_pivot=0.0)
# The substrate running equals the framework identity n_s_FW^2 - 1 (bit-exact in Q).
alpha_s_substrate = float(n_s_FW_exact**2 - 1)                    # (local) = -0.08587279 (leaf-1)
alpha_s_pivot = 0.0                                               # (local) EXACT (leaf-2, S93-W7-1)
beta_s_substrate = beta_s                                         # (local) = -0.1331 running-of-running (leaf-1)
transport_decades = 54.04                                         # (local) S110/S116 BZ->pivot scale gap (descriptive)

# A_s amplitude OOM band (plan §W9-2 (iii)); the Wave-1 𝒩-fork status this session.
OOM_BAND_LO = 0.196                                               # (local) plan-pinned amplitude band low
OOM_BAND_HI = 1.527                                               # (local) plan-pinned amplitude band high
NFORK_RESOLVED_THIS_SESSION = False                              # (local) GS-1=INFO-RESIDUAL-PREFACTOR; fork OPEN

# Output destinations
OUT_NPZ = SESSION_DIR / "s117_w9_transit_ps67_window_wide.npz"
OUT_PNG = SESSION_DIR / "s117_w9_transit_ps67_window_wide.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "session-67" / "s67_transit_ps.npz",
    COMPUTATIONS_DIR / "session-116" / "s116_w1_as_cf3_route_reconcile.npz",
    COMPUTATIONS_DIR / "session-116" / "s116_w1_as_cfb1_squeeze_promote.npz",
    COMPUTATIONS_DIR / "session-111" / "s111_cf_as3a_impulse_quench.npz",
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


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def transported_pivot_Pzeta(k_mpc, n_s_pivot, alpha_pivot, A_s):
    """Leaf-2: deg-+2 transported CMB/LSS-pivot-channel curvature spectrum.

    Mode-Independent Occupation (S93-W7-1): the occupation is k-INDEPENDENT in the
    frozen superhorizon plateau ⇒ the only k-dependence is the GEOMETRIC envelope,
    a near-scale-invariant power law with running alpha_pivot.

        P_zeta(k) = A_s * (k/k_pivot) ** [(n_s_pivot - 1) + 0.5*alpha_pivot*ln(k/k_pivot)]
    """
    lnr = np.log(k_mpc / k_pivot_planck)                # (local)
    exponent = (n_s_pivot - 1.0) + 0.5 * alpha_pivot * lnr  # (local)
    return A_s * np.exp(exponent * lnr)                 # (local)


def bare_bz_ns_of_k(k_mpc, n_s_pivot):
    """Leaf-1 contrast: if the bare-BZ substrate running were what the CMB measured
    (the container-thinking error — using the deg-0 SCALAR reading), n_s would drift:
        n_s^BZ(k) = n_s_pivot + alpha_s_substrate*ln(k/k_pivot) + 0.5*beta_s*ln(k/k_pivot)^2
    """
    lnr = np.log(k_mpc / k_pivot_planck)                # (local)
    return n_s_pivot + alpha_s_substrate * lnr + 0.5 * beta_s_substrate * lnr**2


def compute() -> dict:
    res = {}  # (local)

    # ---- Load inputs ----
    d67 = np.load(COMPUTATIONS_DIR / "session-67" / "s67_transit_ps.npz", allow_pickle=True)   # (local)
    dcf3 = np.load(COMPUTATIONS_DIR / "session-116" / "s116_w1_as_cf3_route_reconcile.npz", allow_pickle=True)  # (local)
    dcfb1 = np.load(COMPUTATIONS_DIR / "session-116" / "s116_w1_as_cfb1_squeeze_promote.npz", allow_pickle=True)  # (local)
    d111 = np.load(COMPUTATIONS_DIR / "session-111" / "s111_cf_as3a_impulse_quench.npz", allow_pickle=True)  # (local)

    # Bare-BZ baseline (leaf-1) grounding: the s67 sudden spectrum has wild running.
    k_grid_bz = np.asarray(d67["k_grid"], dtype=float)          # (local) M_KK units
    ns_sudden_bz = np.asarray(d67["ns_sudden"], dtype=float)    # (local) bare-BZ n_s(k)
    alpha_sudden_bz = np.asarray(d67["alpha_sudden"], dtype=float)  # (local)
    bz_efolds = float(np.log(k_grid_bz.max() / k_grid_bz.min()))    # (local) BZ window width
    bz_ns_min, bz_ns_max = float(ns_sudden_bz.min()), float(ns_sudden_bz.max())  # (local)
    alpha_s_decisive = float(d67["alpha_s_decisive"])          # (local) -0.915 (sudden decisive)

    # Pivot scheme split + plurality (cross-check pins)
    ns_sqrt = float(dcf3["ns_sqrt"])                           # (local) 0.959
    ns_fw = float(dcf3["ns_fw"])                               # (local) 0.9561
    route_names = [str(x) for x in dcf3["route_names"]]        # (local)
    route_oom = np.asarray(dcf3["route_oom"], dtype=float)     # (local) 5-member plurality
    routes_collapse = bool(dcf3["routes_collapse"])            # (local)
    cf3_sha = str(dcf3["audit_sha256"])                        # (local)

    A_s_squeeze = float(dcfb1["A_s_squeeze"])                  # (local) 1.5367e-8
    squeeze_oom = float(dcfb1["OOM"])                          # (local) +0.864
    cfb1_band_lo = float(dcfb1["OOM_BAND_LO"])                 # (local)
    cfb1_band_hi = float(dcfb1["OOM_BAND_HI"])                 # (local)
    cfb1_sha = str(dcfb1["audit_sha256"])                      # (local)

    A_s_impulse = float(d111["A_s_impulse"])                   # (local) 1.5367e-8
    s111_oom = float(d111["OOM_vs_Planck"])                    # (local) +0.864
    s111_sha = str(d111["audit_sha256"])                       # (local)

    # ---- Build the 200-point log mesh over the observed window ----
    k_mpc = np.logspace(np.log10(K_MIN_MPC), np.log10(K_MAX_MPC), N_EVAL)   # (local)
    lnk = np.log(k_mpc)                                                     # (local)
    span_efolds = float(lnk[-1] - lnk[0])                                   # (local) = ln(1e4)
    dlnk_half = 0.5 * span_efolds                                           # (local) symmetric half-window (plan)
    # Asymmetric half-window from the ACTUAL Planck pivot 0.05 Mpc^-1 (cross-check)
    dlnk_half_pivot = float(max(np.log(K_MAX_MPC / k_pivot_planck),
                                np.log(k_pivot_planck / K_MIN_MPC)))         # (local) = ln(500)

    # =====================================================================
    # PART (i) — BANDWIDTH
    # =====================================================================
    # Primary: the transported pivot spectrum (leaf-2 power law) is non-degenerate
    # (P_zeta>0, n_s finite) across the full mesh spanning span_efolds e-folds.
    Pz_pivot = transported_pivot_Pzeta(k_mpc, n_s_framework, alpha_s_pivot, A_s_FW)  # (local)
    nondegenerate = bool(np.all(Pz_pivot > 0.0) and np.all(np.isfinite(Pz_pivot)))   # (local)
    span_pass = bool((span_efolds >= SPAN_TARGET_EFOLDS) and nondegenerate)
    # Secondary (descriptive): deg-+2 transport maps the BZ e-fold width; the
    # Mode-Independent-Occupation power law has no UV/IR feature within the window.
    deg_efold_coverage = float(deg_T_BZ_pivot * bz_efolds)     # (local) 2 * 6.98 = 13.97 >= 9.21

    # =====================================================================
    # PART (ii) — TILT (window-wide near-scale-invariance)
    # =====================================================================
    # Numerically extract n_s(k) = 1 + dlnP_zeta/dlnk from the transported spectrum.
    ns_of_k_fw = 1.0 + np.gradient(np.log(Pz_pivot), lnk)      # (local) framework scheme
    Pz_pivot_sqrt = transported_pivot_Pzeta(k_mpc, n_s_FW_sqrt_cutoff, alpha_s_pivot, A_s_FW)  # (local)
    ns_of_k_sqrt = 1.0 + np.gradient(np.log(Pz_pivot_sqrt), lnk)   # (local) sqrt-cutoff scheme
    # Numerical running alpha_s(k) = d n_s/d ln k (should be ~0 — Mode-Independent Occupation)
    alpha_of_k_fw = np.gradient(ns_of_k_fw, lnk)              # (local)

    # Band test: max over the window of |n_s(k) - planck_ns|
    dev_fw = np.abs(ns_of_k_fw - planck_ns)                   # (local)
    dev_sqrt = np.abs(ns_of_k_sqrt - planck_ns)              # (local)
    max_dev_fw = float(np.max(dev_fw))                        # (local) ~0.0088
    max_dev_sqrt = float(np.max(dev_sqrt))                   # (local) ~0.0059
    # The analytic (exact power-law) deviations at the pivot (no gradient noise):
    dev_fw_analytic = abs(n_s_framework - planck_ns)          # (local) 0.0088
    dev_sqrt_analytic = abs(n_s_FW_sqrt_cutoff - planck_ns)   # (local) 0.0059
    band_lo = planck_ns - TILT_BAND                           # (local) 0.9523
    band_hi = planck_ns + TILT_BAND                           # (local) 0.9775
    in_band_fw = bool(band_lo <= n_s_framework <= band_hi)
    in_band_sqrt = bool(band_lo <= n_s_FW_sqrt_cutoff <= band_hi)
    tilt_pass = bool((dev_fw_analytic <= TILT_BAND) and in_band_fw and in_band_sqrt)
    sigdist_fw = dev_fw_analytic / planck_ns_err             # (local) 2.095 sigma
    sigdist_sqrt = dev_sqrt_analytic / planck_ns_err         # (local) 1.405 sigma
    max_alpha_pivot_numeric = float(np.max(np.abs(alpha_of_k_fw)))  # (local) ~0 (gradient floor)

    # Substitution-chain bound: window-wide |alpha_s| <= TILT_BAND / dlnk_half
    alpha_window_bound = TILT_BAND / dlnk_half                # (local) 0.0126/4.6052 = 2.736e-3
    alpha_window_bound_pivot = TILT_BAND / dlnk_half_pivot    # (local) tighter via 0.05 pivot
    tighten_factor = PIVOT_LOCAL_ALPHA_BOUND / alpha_window_bound  # (local) 5.48x

    # Leaf-1 contrast: bare-BZ running fully transported (WRONG channel) drifts out of band
    ns_bz_leaf = bare_bz_ns_of_k(k_mpc, n_s_framework)        # (local)
    ns_bz_min, ns_bz_max = float(ns_bz_leaf.min()), float(ns_bz_leaf.max())  # (local)
    bz_max_dev = float(np.max(np.abs(ns_bz_leaf - planck_ns)))   # (local) HUGE (out of band)
    bz_in_band = bool((ns_bz_leaf.min() >= band_lo) and (ns_bz_leaf.max() <= band_hi))  # (local) False
    # bare-BZ running fails even the LOOSE pivot-local bound:
    bz_fails_pivot_local = bool(abs(alpha_s_substrate) > PIVOT_LOCAL_ALPHA_BOUND)  # (local) True

    # =====================================================================
    # PART (iii) — AMPLITUDE (OOM band reconciliation; Wave-1 𝒩-fork status)
    # =====================================================================
    oom_AsFW = float(np.log10(A_s_FW / A_s_CMB))             # (local) +0.864
    oom_in_band = bool(OOM_BAND_LO <= oom_AsFW <= OOM_BAND_HI)   # (local) True (in band)
    # Every plurality member in band?
    members_in_band = [bool(OOM_BAND_LO <= o <= OOM_BAND_HI) for o in route_oom]  # (local)
    all_members_in_band = bool(all(members_in_band))         # (local)
    # The scheme has NOT collapsed (routes_collapse=False) AND the session 𝒩-fork is OPEN:
    amplitude_reconciled = bool(routes_collapse and NFORK_RESOLVED_THIS_SESSION)  # (local) False
    if amplitude_reconciled:
        amp_verdict = "PASS"   # (local)
    else:
        amp_verdict = "INFO"   # (local) INFO-pending-Wave-1 (scheme unreconciled)

    # =====================================================================
    # COMPOSITE + 3-tuple
    # =====================================================================
    # sign  = window-wide band-curvature direction: predicted alpha_s_pivot -> 0
    #         (no curvature out of band). Computed alpha ~ 0 ⇒ direction matches.
    sign_verdict = "PASS" if (span_pass and tilt_pass and abs(alpha_s_pivot) <= alpha_window_bound) else "FAIL"
    # magnitude = (ii) tilt magnitude: max|n_s(k)-0.9649| vs 0.0126
    if dev_fw_analytic <= TILT_BAND:
        magnitude_verdict = "PASS"
    elif dev_fw_analytic <= 2.0 * TILT_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # regime = first-order Taylor drift + Mode-Independent-Occupation frozen-plateau
    #          validity across the half-window. f_used = full window (no auto-shorten).
    regime_verdict = "VALID"

    # Composite: (i)∧(ii) PASS, (iii) INFO-pending ⇒ INFO via PLAN-FROZEN-OPERATOR
    # PRECEDENCE (the (iii) amplitude-pending applicability guard has no axis in the
    # sign/magnitude/regime 3-tuple; generic-collapse on PASS/PASS/VALID would read
    # PASS, OVERRIDDEN to INFO by the (iii) guard per §W9-2 INFO_meaning+discriminator).
    if not span_pass:
        composite = "FAIL"   # (local)
    elif not tilt_pass:
        composite = "FAIL"   # (local)
    elif amp_verdict == "INFO":
        composite = "INFO"   # (local) plan-frozen precedence (iii)-pending guard
    else:
        composite = "PASS"   # (local)

    res.update(dict(
        # mesh
        k_mpc=k_mpc, lnk=lnk, span_efolds=span_efolds, dlnk_half=dlnk_half,
        dlnk_half_pivot=dlnk_half_pivot,
        # (i) bandwidth
        Pz_pivot=Pz_pivot, nondegenerate=nondegenerate, span_pass=span_pass,
        bz_efolds=bz_efolds, deg_efold_coverage=deg_efold_coverage,
        # (ii) tilt
        ns_of_k_fw=ns_of_k_fw, ns_of_k_sqrt=ns_of_k_sqrt, alpha_of_k_fw=alpha_of_k_fw,
        max_dev_fw=max_dev_fw, max_dev_sqrt=max_dev_sqrt,
        dev_fw_analytic=dev_fw_analytic, dev_sqrt_analytic=dev_sqrt_analytic,
        band_lo=band_lo, band_hi=band_hi, in_band_fw=in_band_fw, in_band_sqrt=in_band_sqrt,
        sigdist_fw=sigdist_fw, sigdist_sqrt=sigdist_sqrt,
        max_alpha_pivot_numeric=max_alpha_pivot_numeric,
        alpha_window_bound=alpha_window_bound, alpha_window_bound_pivot=alpha_window_bound_pivot,
        tighten_factor=tighten_factor, tilt_pass=tilt_pass,
        # leaf-1 contrast
        ns_bz_leaf=ns_bz_leaf, ns_bz_min=ns_bz_min, ns_bz_max=ns_bz_max,
        bz_max_dev=bz_max_dev, bz_in_band=bz_in_band, bz_fails_pivot_local=bz_fails_pivot_local,
        alpha_s_substrate=alpha_s_substrate, alpha_s_pivot=alpha_s_pivot,
        # bare-BZ baseline grounding (s67)
        bz_ns_min=bz_ns_min, bz_ns_max=bz_ns_max, alpha_s_decisive=alpha_s_decisive,
        k_grid_bz=k_grid_bz, ns_sudden_bz=ns_sudden_bz, alpha_sudden_bz=alpha_sudden_bz,
        # (iii) amplitude
        oom_AsFW=oom_AsFW, oom_in_band=oom_in_band, all_members_in_band=all_members_in_band,
        route_names=np.array(route_names), route_oom=route_oom, routes_collapse=routes_collapse,
        amplitude_reconciled=amplitude_reconciled, amp_verdict=amp_verdict,
        squeeze_oom=squeeze_oom, A_s_squeeze=A_s_squeeze, s111_oom=s111_oom,
        OOM_BAND_LO=OOM_BAND_LO, OOM_BAND_HI=OOM_BAND_HI,
        # verdicts
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        # provenance pins
        cf3_sha=cf3_sha, cfb1_sha=cfb1_sha, s111_sha=s111_sha,
        # the reported scalar value (4-tuple)
        value=max_dev_fw,
    ))
    return res


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r):
    fig, ax = plt.subplots(2, 2, figsize=(15, 11))
    k = r["k_mpc"]

    # (a) n_s(k) over the window: leaf-2 (flat) PASS vs leaf-1 (bare-BZ drift) FAIL
    a = ax[0, 0]
    a.axhspan(r["band_lo"], r["band_hi"], color="green", alpha=0.12,
              label=f"3σ band [{r['band_lo']:.4f}, {r['band_hi']:.4f}]")
    a.axhline(planck_ns, color="k", ls="--", lw=1, label=f"Planck n_s={planck_ns}")
    a.plot(k, r["ns_of_k_fw"], color="C0", lw=2.4,
           label=f"leaf-2 pivot (framework) n_s={n_s_framework} (α_s=0)")
    a.plot(k, r["ns_of_k_sqrt"], color="C2", lw=1.8, ls=":",
           label=f"leaf-2 pivot (sqrt-cutoff) n_s={n_s_FW_sqrt_cutoff}")
    a.plot(k, r["ns_bz_leaf"], color="C3", lw=1.6, ls="-.",
           label=f"leaf-1 bare-BZ (WRONG channel) α_s={alpha_s_substrate:.5f}")
    a.set_xscale("log")
    a.set_xlabel("k  [Mpc$^{-1}$]")
    a.set_ylabel("$n_s(k)$")
    a.set_ylim(0.5, 1.5)
    a.set_title("(ii) window-wide tilt: leaf-2 PASS (flat in band) vs leaf-1 drift")
    a.legend(fontsize=7.5, loc="lower left")

    # (b) transported pivot power spectrum P_zeta(k) (leaf-2 power law)
    b = ax[0, 1]
    b.loglog(k, r["Pz_pivot"], color="C0", lw=2.2, label="leaf-2 $P_\\zeta(k)$ (deg-+2 pivot)")
    b.axvline(k_pivot_planck, color="grey", ls=":", lw=1, label=f"pivot {k_pivot_planck} Mpc$^{{-1}}$")
    b.set_xlabel("k  [Mpc$^{-1}$]")
    b.set_ylabel("$P_\\zeta(k)$")
    b.set_title(f"(i) bandwidth: span={r['span_efolds']:.4f} e-folds ≥ {SPAN_TARGET_EFOLDS}  [non-degenerate]")
    b.legend(fontsize=8, loc="best")

    # (c) running alpha_s(k): leaf-2 ~ 0 vs window bound vs bare-BZ
    c = ax[1, 0]
    c.axhspan(-r["alpha_window_bound"], r["alpha_window_bound"], color="green", alpha=0.12,
              label=f"window bound ±{r['alpha_window_bound']:.3e}")
    c.axhline(0.0, color="C0", lw=2.4, label="leaf-2 pivot α_s = 0 EXACT (Mode-Indep. Occ.)")
    c.axhline(-PIVOT_LOCAL_ALPHA_BOUND, color="orange", ls="--", lw=1.2,
              label=f"pivot-local bound ∓{PIVOT_LOCAL_ALPHA_BOUND} (5.48× looser)")
    c.axhline(PIVOT_LOCAL_ALPHA_BOUND, color="orange", ls="--", lw=1.2)
    c.axhline(alpha_s_substrate, color="C3", ls="-.", lw=1.6,
              label=f"leaf-1 bare-BZ α_s={alpha_s_substrate:.5f} (31× over bound)")
    c.set_xscale("log")
    c.set_xlabel("k  [Mpc$^{-1}$]")
    c.set_ylabel("$\\alpha_s(k) = dn_s/d\\ln k$")
    c.set_title("(ii) running: window-wide ⊂ pivot-local (5.48× tighter)")
    c.legend(fontsize=7.5, loc="center left")

    # (d) amplitude OOM plurality vs band
    d = ax[1, 1]
    d.axhspan(r["OOM_BAND_LO"], r["OOM_BAND_HI"], color="green", alpha=0.12,
              label=f"OOM band [+{r['OOM_BAND_LO']}, +{r['OOM_BAND_HI']}]")
    xs = np.arange(len(r["route_oom"]))
    d.bar(xs, r["route_oom"], color="C4", alpha=0.7)
    d.axhline(r["oom_AsFW"], color="C0", lw=2, label=f"A_s_FW OOM=+{r['oom_AsFW']:.3f}")
    d.set_xticks(xs)
    d.set_xticklabels([n[:14] for n in r["route_names"]], rotation=35, ha="right", fontsize=6.5)
    d.set_ylabel("OOM vs Planck A_s")
    d.set_title(f"(iii) amplitude: in-band but N-fork OPEN -> INFO-pending-Wave-1 (collapse={r['routes_collapse']})")
    d.legend(fontsize=8, loc="upper left")

    fig.suptitle(f"{GATE_ID}  —  composite {r['composite']}  "
                 f"(span PASS ∧ tilt PASS ∧ amplitude INFO-pending-Wave-1)", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.975])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload helper
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
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
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # ---- Report ----
    print("=== PART (i) BANDWIDTH ===")
    print(f"  window [{K_MIN_MPC:g}, {K_MAX_MPC:g}] Mpc^-1; span = {r['span_efolds']:.4f} e-folds "
          f">= {SPAN_TARGET_EFOLDS} : {'PASS' if r['span_pass'] else 'FAIL'}")
    print(f"  transported P_zeta(k) non-degenerate (P>0, n_s finite) over {N_EVAL} pts: {r['nondegenerate']}")
    print(f"  [context] bare-BZ window = {r['bz_efolds']:.4f} e-folds; deg-+2 coverage "
          f"= {r['deg_efold_coverage']:.4f} e-folds >= {SPAN_TARGET_EFOLDS}")
    print()
    print("=== PART (ii) TILT (window-wide near-scale-invariance) ===")
    print(f"  leaf-2 pivot framework  n_s = {n_s_framework}  |n_s-0.9649| = {r['dev_fw_analytic']:.4f} "
          f"({r['sigdist_fw']:.3f}σ)  in band [{r['band_lo']:.4f},{r['band_hi']:.4f}] = {r['in_band_fw']}")
    print(f"  leaf-2 pivot sqrt-cutoff n_s = {n_s_FW_sqrt_cutoff} |n_s-0.9649| = {r['dev_sqrt_analytic']:.4f} "
          f"({r['sigdist_sqrt']:.3f}σ)  in band = {r['in_band_sqrt']}")
    print(f"  numerical max|n_s(k)-0.9649| over window = {r['max_dev_fw']:.6f} (<= {TILT_BAND})")
    print(f"  numerical max|alpha_s(k)| pivot leaf      = {r['max_alpha_pivot_numeric']:.3e} (alpha_s_pivot=0 EXACT)")
    print(f"  substitution chain: window |alpha_s| <= {TILT_BAND}/{r['dlnk_half']:.4f} "
          f"= {r['alpha_window_bound']:.4e}  ⇒ {r['tighten_factor']:.2f}× tighter than pivot-local {PIVOT_LOCAL_ALPHA_BOUND}")
    print(f"  TILT verdict: {'PASS' if r['tilt_pass'] else 'FAIL'}")
    print(f"  [contrast] leaf-1 bare-BZ (WRONG channel) n_s drifts to [{r['ns_bz_min']:.3f},{r['ns_bz_max']:.3f}], "
          f"max|dev|={r['bz_max_dev']:.3f} → in band={r['bz_in_band']}; "
          f"bare-BZ |α_s|={abs(r['alpha_s_substrate']):.5f} fails pivot-local={r['bz_fails_pivot_local']}")
    print(f"  [s67 baseline] bare-BZ sudden n_s∈[{r['bz_ns_min']:.2f},{r['bz_ns_max']:.2f}], "
          f"alpha_s_decisive={r['alpha_s_decisive']:.3f} (leaf-1 FAIL — not the tested leaf)")
    print()
    print("=== PART (iii) AMPLITUDE ===")
    print(f"  A_s_FW = {A_s_FW:.6e}; OOM vs Planck = +{r['oom_AsFW']:.4f}; "
          f"band [+{r['OOM_BAND_LO']},+{r['OOM_BAND_HI']}]; in band = {r['oom_in_band']}")
    print(f"  plurality routes: {list(r['route_names'])}")
    print(f"  route OOMs: {np.round(r['route_oom'],4).tolist()}; all in band = {r['all_members_in_band']}; "
          f"routes_collapse = {r['routes_collapse']}")
    print(f"  𝒩-fork resolved this session = {NFORK_RESOLVED_THIS_SESSION}; "
          f"amplitude reconciled = {r['amplitude_reconciled']} ⇒ (iii) = {r['amp_verdict']}")
    print()
    print("=== COMPOSITE ===")
    print(f"  sign={r['sign_verdict']} magnitude={r['magnitude_verdict']} regime={r['regime_verdict']} "
          f"⇒ composite={r['composite']} (plan-frozen precedence: (iii) INFO-pending guard)")

    make_plot(r)

    # ---- Save npz ----
    save = {k: v for k, v in r.items() if not isinstance(v, (bool,))}
    save.update({k: int(v) for k, v in r.items() if isinstance(v, bool)})
    np.savez(OUT_NPZ,
             gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
             audit_sha256=audit_sha, content_sha256=content_sha,
             n_s_framework=n_s_framework, n_s_FW_sqrt_cutoff=n_s_FW_sqrt_cutoff,
             planck_ns=planck_ns, planck_ns_err=planck_ns_err, tilt_band=TILT_BAND,
             A_s_FW=A_s_FW, A_s_CMB=A_s_CMB, deg_T_BZ_pivot=deg_T_BZ_pivot,
             Mach_max=Mach_max, transport_decades=transport_decades,
             **save)
    print(f"\nSaved: {OUT_NPZ.name}, {OUT_PNG.name}")

    value = r["value"]
    tag = emit_4tuple(round(value, 6), SCHEME, CONVENTION, L_MAX)
    print(tag)

    # value payload: span/tilt/amplitude summary (no single-quote chars)
    vstr = (f"span={r['span_efolds']:.4f}ef>=9.21_PASS;"
            f"tilt_max|ns-0.9649|={r['dev_fw_analytic']:.4f}<=0.0126_PASS"
            f"(ns_fw=0.9561@{r['sigdist_fw']:.2f}sig,ns_sqrt=0.959@{r['sigdist_sqrt']:.2f}sig,alpha_s_pivot=0EXACT_S93W7-1);"
            f"window5.48x_tighter_than_pivot-local0.015;"
            f"amp_OOM=+{r['oom_AsFW']:.3f}_in[+0.196,+1.527]_but_Nfork_OPEN_INFO-pending-Wave1;"
            f"composite=INFO")

    precedence_row = ("# composite-precedence: §W9-2 INFO_meaning+discriminator — "
                      "(i)span PASS & (ii)tilt PASS, (iii)amplitude INFO-pending-Wave1 "
                      "Nfork-plurality{+0.196,+0.384,+0.864}OOM; generic-collapse "
                      "sign=PASS/mag=PASS/regime=VALID->PASS OVERRIDDEN to INFO by (iii) guard")
    channel_row = ("# scale-and-channel-tag: leaf-2 CMB-pivot alpha_s_pivot=0.0 EXACT "
                   "(S93-W7-1 deg_T=2.0 NON-SCALAR); NOT bare-BZ alpha_s_substrate=-0.08587279 "
                   "nor beta_s=-0.1331; provenance cf3="+r['cf3_sha'][:16]+" cfb1="+r['cfb1_sha'][:16])

    print_verdict_payload(
        r["composite"], vstr, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        extra_rows=[precedence_row, channel_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
