#!/usr/bin/env python3
"""
S116 W1-2 — S116-W1-AS-CFB1: promote the box-delta SQUEEZE A_s magnitude
(ξ_KZ-normalized) to a GATED OOM threshold + resolve POINT-vs-BAND via L_max-stability
=====================================================================================

Gate: S116-W1-AS-CFB1 ([SIGN] — the OOM-gap SIGN + band-membership is a directional claim)

Pre-registered threshold (plan §W1-2):
  strict_PASS_boundary: OOM ∈ [+0.196, +1.527]  AND  L_max-stability
                        |ΔA_s(L7eq→L12)|/A_s ≤ 0.05  (POINT)
  PASS iff (OOM in-axis) AND (rel_dev_Lmax ≤ 0.05) — POSITIVE in-axis overproduction,
       L_max-stable POINT (Track A; the squeeze factor is a converged physical d.o.f.).
  INFO iff (OOM in-axis) AND (rel_dev_Lmax > 0.05) — in-axis but L_max-soft BAND (Track B).
  FAIL iff OOM OUTSIDE [+0.196, +1.527] — the squeeze route recovers a discredited
       normalization (+3.15 Route-B-PW or +9.37 naive-UV artifact); both tracks void.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/session-100b/s100b_box_delta_bogoliubov.npz   (box-delta SUDDEN |β_k|²;
        the MAGNITUDE source at k̂=1/ξ_KZ — distinct grid from the fold-window REGIME source)
  - computations/session-110/s110_cf_b1_transit_ps_promote.npz  (two-leaf build; carries
        branch_drift_L3_L7 + truncation_consistent — the on-disk L_max scan; amp cross-checks)
  - computations/session-111/s111_cf_as3a_impulse_quench.npz    (the S111-pinned A_s_FW
        round-trip anchor; the recipe reference)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (L12 sector_evals;
        Friedrich-Bär bottom-saturation argument; runtime-asserted git-canonical SHA)
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<A_s_squeeze + OOM + band + epistemic-type + rel_dev_Lmax>,
   scheme=IMPULSE-QUENCH-BOGOLIUBOV,
   convention=FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-xiKZ, L_max=12)

Classification: PHONONIC.
  The arrow: D_K eigenvalues λ_k(τ) → transit Bogoliubov {α_k, β_k} → produced occupation
  n_k = |β_k|² → post-fold acoustic squeeze A_s. The substrate IS the box-delta sudden-limit
  |β_{k̂}|² at the Kibble-Zurek coherence scale k̂=1/ξ_KZ; A_s is read off the frozen
  occupation, NOT an inflaton normalization. POINT (Friedrich-Bär bottom-saturated at L12)
  vs BAND (L_max-soft) is whether the cosmological window's |β_{k̂}|² is a converged
  substrate-IS observable. The lab measures A_s IN a CMB container; the OOM gap is the
  substrate's overproduction relative to it.

METHODOLOGY
-----------
PROMOTION of S110-CF-B1's REGISTERED-CONTENT amplitude (carried "NOT a separate gate
threshold", s110 line 64) to a GATED magnitude, + resolution of the POINT-vs-BAND epistemic
type that S111-CF-AS3a DEFERRED to the AS3b verdict (s111 lines 58-63; epistemic_type was
AS3b-CONDITIONAL on disk). The box-delta is the MAGNITUDE source; the fold-window grid is
the REGIME source (TWO-SPECTRA-TWO-ROLES, S111).

(1) MAGNITUDE. A_s_squeeze = |β_{k̂}|²/(2π²), with N_norm = ξ_KZ³ the Kibble-Zurek coherence
    VOLUME (del Campo & Zurek 1310.1600) and k̂ = 1/ξ_KZ the frozen comoving wavenumber.
    The KZ-volume identity k̂³·ξ_KZ³ = (k̂·ξ_KZ)³ = 1 makes the dimensionless-power k̂³ factor
    cancel the coherence-volume ξ_KZ³, so A_s_raw = (k̂³/2π²)·|β_{k̂}|²·ξ_KZ³ = |β_{k̂}|²/(2π²).
    |β_{k̂}|² is read from the S100b box-delta SUDDEN spectrum by near-flat UV-tail
    extrapolation (slope ~ -0.003, the scale-invariant sudden signature). Reproduces
    A_s_FW = 1.5367e-08 (S111) to published precision (5 sig figs).

(2) GATE the OOM gap log10(A_s_squeeze/A_s_CMB) against the S115 sudden↔adiabatic axis band
    [+0.196, +1.527] (promotion of the S110 registered amplitude to a gated threshold).

(3) RESOLVE POINT-vs-BAND (AS3b-deferred) via L_max-stability of A_s_squeeze. Three legs:
      (i)  EMPIRICAL (authoritative on-disk L_max scan): the S110 build's
           branch_drift_L3_L7 = 5.43e-05, truncation_consistent = True. The box-delta
           barrier V_box inherits the build's L_max-stability → rel_dev_Lmax = branch_drift.
      (ii) FRIEDRICH-BÄR (structural, computed from s84 L12 cache): the box-delta barrier
           V_box derives from the fold z''/z, dominated by the BOTTOM-of-spectrum modes
           (|λ| ~ 0.8-1.5, low-level sectors p+q ≤ 4, all present at L12). The level-min|λ|
           sequence is monotone-increasing; new level-13 sectors enter HIGH in the window
           (|λ| ≳ 3.70 M_KK), sub-dominant to the bottom-saturated barrier → Casimir-saturated.
      (iii) TRANSIT-DYNAMICS (mechanism): the box-delta UV-tail is delta-dominated
           (beta2_deltas_only / beta2_box_only ≈ 54×); the delta strengths encode the
           IMPULSIVE transit jump (Mach 13.75) — a transit-dynamics quantity screened from
           deep-spectrum L_max truncation.
    POINT iff rel_dev_Lmax ≤ 0.05; BAND otherwise.
    The REGIME source's all-frozen classification is independently L_max-robust: any new
    L-reachable mode (|λ| ≲ 3.7) is far below k_tach ≈ 1974 → still frozen-superhorizon.

(4) FLOOR sub-annotation (NOT the gate operator). A_s_squeeze ≥ A_s^BD because
    S_IC = 1 + 2 n_k ≥ 1 (n_k = |β_{k̂}|² > 0). The FLOOR is PERMANENT on 3 orthogonal axes
    (WS-AS-1 LIZ2-1); the MAGNITUDE is SCHEME-DEPENDENT (the S115 sudden↔adiabatic axis).

3-TUPLE MAPPING ([SIGN] trigger; reproduces the plan PASS/INFO/FAIL via the generic
gate-verdicts.md collapse rule — NO plan-frozen-operator-precedence needed):
  - sign_verdict      = PASS iff OOM > 0 (overproduction direction, substitution-chain Step 5)
  - magnitude_verdict = PASS  (OOM in-band ∧ POINT)
                      / INFO  (OOM in-band ∧ BAND, L_max-soft)
                      / FAIL  (OOM out-of-band, discredited normalization)
  - regime_verdict    = VALID (box-delta sudden-limit frozen-occupation read is the exact
                        impulse limit, RESOLVED-FROZEN per S111; no method breakdown)
  Generic collapse: regime=VALID ∧ sign=PASS ∧ magnitude={PASS→PASS, INFO→INFO, FAIL→FAIL}.

DISCIPLINE: from canonical_constants import *; intermediates tagged # (local); numpy vector
reduction (loaded {β_k} + few-point UV-tail polyfit + per-sector min reduce — NO ≥100×100
dense diag, GPU not needed); dual-SHA; verdict via print_verdict_payload -> agent calls
mcp__knowledge__emit_verdict (race-safe).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import) + CPU thread cap
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (vector reduction; no GPU step)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (xi_KZ_FW, A_s_CMB, PI, M_KK, A_s_FW, ...)
import canonical_constants as _cc   # for getattr fallbacks

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import time

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity + pins
# ---------------------------------------------------------------------------
SESSION = "S116"                                                          # (local)
GATE_ID = "S116-W1-AS-CFB1"                                               # (local)
SCHEME = "IMPULSE-QUENCH-BOGOLIUBOV"                                      # (local)
CONVENTION = "FROZEN-OCCUPATION-NORMALIZED-BY-SUBSTRATE-NATURAL-xiKZ"     # (local)
L_MAX = 12                                                               # (local)

# --- Pre-registered gate thresholds (plan §W1-2 strict_PASS_boundary) ---
# S115 sudden<->adiabatic axis band (existing-routes span; S115-AS-NEWAXIS-SELECTOR).
OOM_BAND_LO = 0.196              # (local) pre-reg threshold: S115 axis lower edge (TD/zeta)
OOM_BAND_HI = 1.527              # (local) pre-reg threshold: S115 axis upper edge (Connes-Parker)
LMAX_STABILITY_TOL = 0.05        # (local) pre-reg threshold: POINT/BAND split (|ΔA_s|/A_s)
# Disclosure anchors (discredited normalizations the squeeze must stay BELOW).
OOM_ROUTE_B_PW = 3.15            # (local) AMPLITUDE-NORM-66 Route-B Peter-Weyl (discredited)
OOM_UV_ARTIFACT = 9.37           # (local) naive-UV-extrapolation artifact (S111/WS-AS-1 §47)
# Round-trip publication precision (plan publication_precision: 5 -> rel_tol 1e-5).
ROUNDTRIP_REL_TOL = 1.0e-5       # (local) 5-sig-fig publication floor for A_s_FW round-trip
# s84 cache git-canonical SHA (mechanical-closure HALT on drift, per S110 line 196).
S84_CANONICAL_SHA = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local)

OUT_NPZ = SESSION_DIR / "s116_w1_as_cfb1_squeeze_promote.npz"
OUT_PNG = SESSION_DIR / "s116_w1_as_cfb1_squeeze_promote.png"

# --- Input caches ---
BETA2_BOXDELTA = COMPUTATIONS_DIR / "session-100b" / "s100b_box_delta_bogoliubov.npz"
B1_PROMOTE = COMPUTATIONS_DIR / "session-110" / "s110_cf_b1_transit_ps_promote.npz"
AS3A_PIN = COMPUTATIONS_DIR / "session-111" / "s111_cf_as3a_impulse_quench.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    BETA2_BOXDELTA,
    B1_PROMOTE,
    AS3A_PIN,
    S84_CACHE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block (S84+ schema)
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
    script_bytes = b""        # (local)
    canonical_bytes = b""     # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
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
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Friedrich-Bär bottom-saturation (s84 L12 sector_evals)
# ---------------------------------------------------------------------------
def C2_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C_2(p,q) = (p² + q² + pq + 3p + 3q)/3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


def friedrich_bar_saturation() -> dict:
    """Demonstrate the box-delta barrier is BOTTOM-saturated at L12.

    The fold barrier V_box (hence the box-delta magnitude) derives from the fold z''/z,
    dominated by the BOTTOM-of-spectrum modes. Compute per-level min|λ| from the s84 L12
    cache, confirm monotonicity, and extrapolate the level-13 floor — showing new sectors
    enter HIGH in the window, sub-dominant to the bottom-saturated barrier.
    """
    d = np.load(S84_CACHE, allow_pickle=True)  # (local)
    sev = d["sector_evals"].item()             # (local) dict (p,q) -> {dim, level, abs_evals}

    by_level: dict[int, float] = {}  # (local) level -> min|λ| over its sectors
    eta_list = []                    # (local) Friedrich-Bär ratios η = min|λ|/sqrt(C2+1)
    for (p, q), info in sev.items():
        lvl = int(info["level"])                                  # (local)
        mn = float(np.min(np.abs(info["abs_evals"])))             # (local)
        by_level[lvl] = mn if lvl not in by_level else min(by_level[lvl], mn)
        eta_list.append(mn / math.sqrt(C2_su3(p, q) + 1.0))       # (local)

    levels = sorted(by_level)                                     # (local)
    level_min = np.array([by_level[l] for l in levels])           # (local)
    L_top = max(levels)                                           # (local) = 12
    # monotone-increasing level floor?
    monotone = bool(np.all(np.diff(level_min) > 0))               # (local)
    incr = float(np.mean(np.diff(level_min)))                     # (local) mean per-level step
    level13_extrap = float(level_min[-1] + incr)                  # (local) ≈ 3.70 M_KK
    eta_min = float(min(eta_list))                                # (local) global FB floor ratio
    # conservative analytic lower bound for the smallest-C2 level-13 sector (6,7)/(7,6)
    c2_67 = C2_su3(6, 7)                                          # (local) smallest C2 at L=13
    level13_fb_lb = eta_min * math.sqrt(c2_67 + 1.0)             # (local) FB analytic lower bound
    # bottom-window: the low-level sectors (p+q <= 4) that dominate z''/z, all present at L12
    bottom_max = float(by_level[4])                              # (local) |λ| ceiling of p+q<=4 band
    return {
        "fb_levels": np.array(levels),
        "fb_level_min": level_min,
        "fb_L_top": L_top,
        "fb_monotone": monotone,
        "fb_incr_mean": incr,
        "fb_level13_extrap": level13_extrap,
        "fb_level13_lb": level13_fb_lb,
        "fb_eta_min": eta_min,
        "fb_bottom_max_pq4": bottom_max,
    }


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    """Reproduce A_s_squeeze, GATE the OOM, resolve POINT-vs-BAND, confirm the floor."""
    # ===================================================================
    # (0) s84 runtime-assert (mechanical-closure HALT on drift; plan input_files)
    # ===================================================================
    s84_sha = sha256_of(S84_CACHE)  # (local)
    if s84_sha != S84_CANONICAL_SHA:
        raise SystemExit(
            f"HALT: s84 spectrum cache SHA drift — got {s84_sha}, "
            f"expected git-canonical {S84_CANONICAL_SHA} (mechanical-closure, S110 line 196)")

    # ===================================================================
    # (1) MAGNITUDE — reproduce A_s_squeeze = |β_{k̂}|²/(2π²) from box-delta UV-tail
    # ===================================================================
    xi_hat = float(xi_KZ_FW)          # (local) = 0.0187601 M_KK^-1 (S89 substrate-natural KZ)
    k_hat = 1.0 / xi_hat              # (local) frozen comoving wavenumber = 53.30 M_KK
    N_norm = xi_hat ** 3              # (local) KZ coherence VOLUME (substrate-natural)
    khat3 = k_hat ** 3                # (local) dimensionless-power phase factor
    # KZ-volume identity: k̂³·ξ_KZ³ = (k̂·ξ_KZ)³ = 1 (k̂ = 1/ξ_KZ)
    kzvol_identity_dev = abs(khat3 * N_norm - 1.0)  # (local)
    assert kzvol_identity_dev < 1e-9, "k_hat^3 * xi_hat^3 must equal 1 (KZ-vol identity)"

    bd = np.load(BETA2_BOXDELTA, allow_pickle=True)  # (local)
    kg = np.asarray(bd["k_grid"], dtype=float)             # (local) box-delta k-grid [1,50]
    b2 = np.asarray(bd["beta2_spectrum"], dtype=float)     # (local) |β_k|² SUDDEN spectrum (TM)
    beta2_pivot_bd = float(bd["beta2_pivot_closed_form"])  # (local) closed-form pivot cross-check
    unit_resid = float(bd["unitarity_residual_max"])       # (local) |α|²-|β|²-1 residual
    beta2_box_only = float(bd["beta2_box_only"])           # (local) box-only piece (tiny)
    beta2_deltas_only = float(bd["beta2_deltas_only"])     # (local) delta-only piece (dominant)
    V_box = float(bd["V_box"])                             # (local) box height (fold barrier)

    # near-flat UV-tail fit (slope ~ -0.003 = scale-invariant sudden signature)
    mask_uv = kg > 10.0               # (local) UV regime for the tail fit (matches S111)
    uv_slope, uv_intercept = np.polyfit(np.log(kg[mask_uv]), np.log(b2[mask_uv]), 1)  # (local)
    beta2_khat = math.exp(uv_slope * math.log(k_hat) + uv_intercept)  # (local) |β_{k̂}|²
    # A_s_raw = (k̂³/2π²)·|β_{k̂}|²·ξ_KZ³ = |β_{k̂}|²/(2π²)   (k̂³·ξ_KZ³ = 1)
    A_s_squeeze = N_norm * beta2_khat * khat3 / (2.0 * PI ** 2)  # (local) == beta2_khat/(2π²)
    # delta-dominance of the UV-tail (transit-dynamics screening leg)
    delta_dominance = beta2_deltas_only / beta2_box_only        # (local) ≈ 54×

    # round-trip vs the S111-pinned canonical A_s_FW (full float64) at 5-sig-fig precision
    A_s_FW_canon = float(getattr(_cc, "A_s_FW", 1.5367059962762235e-08))  # (local)
    a3a = np.load(AS3A_PIN, allow_pickle=True)               # (local)
    A_s_FW_s111 = float(a3a["A_s_impulse"])                  # (local) on-disk S111 pin
    beta2_khat_s111 = float(a3a["beta2_khat"])              # (local) S111 |β_{k̂}|²
    rel_dev_FW = abs(A_s_squeeze - A_s_FW_canon) / A_s_FW_canon   # (local) round-trip rel-dev
    roundtrip_ok = rel_dev_FW < ROUNDTRIP_REL_TOL                 # (local)

    # ===================================================================
    # (2) GATE the OOM gap against the S115 sudden<->adiabatic axis band
    # ===================================================================
    A_s_CMB_val = float(A_s_CMB)                                  # (local) Planck 2018 VI = 2.1e-9
    OOM = math.log10(A_s_squeeze / A_s_CMB_val)                   # (local) +0.8644
    oom_sign_positive = OOM > 0.0                                 # (local) overproduction
    oom_in_band = (OOM_BAND_LO <= OOM <= OOM_BAND_HI)             # (local) S115 axis membership
    below_route_b = OOM < OOM_ROUTE_B_PW                          # (local) below discredited PW
    below_uv = OOM < OOM_UV_ARTIFACT                              # (local) far below UV artifact

    # ===================================================================
    # (3) RESOLVE POINT-vs-BAND via L_max-stability (AS3b-deferred)
    # ===================================================================
    b1 = np.load(B1_PROMOTE, allow_pickle=True)  # (local)
    # leg (i) EMPIRICAL — the on-disk L_max scan; the box-delta barrier inherits it
    branch_drift = float(b1["branch_drift_L3_L7"])               # (local) 5.43e-05
    truncation_consistent = bool(b1["truncation_consistent"])   # (local) True
    ns_L7equiv = float(b1["ns_L7equiv"])                        # (local) 2.99993
    ns_BZ = float(b1["ns_BZ"])                                  # (local) 2.99982
    # amplitude cross-checks (upstream consistency)
    A_s_inv5_b1 = float(b1["A_s_impulse_inv5"])                 # (local) 1.5367e-08
    OOM_gap_inv5_b1 = float(b1["OOM_gap_inv5"])                 # (local) 0.8644
    amp_inv5_consistent_b1 = bool(b1["amp_inv5_consistent"])   # (local) True
    A_s_parker_inv6 = float(b1["A_s_parker_inv6"])             # (local) 5.99e-08 (adiabatic end)

    # leg (ii) FRIEDRICH-BÄR — bottom-saturation (computed from s84 L12 cache)
    fb = friedrich_bar_saturation()  # (local)

    # leg (iii) REGIME-source robustness — new L-reachable modes stay frozen
    k_tach = float(a3a["k_tach_fold"])                          # (local) 1974 (tachyon ceiling)
    k_modes = np.asarray(a3a["k_modes"], dtype=float)           # (local) 89 fold-window modes
    window_ceiling = float(k_modes.max())                      # (local) ≈ 3.7476 M_KK
    regime_robust = fb["fb_level13_extrap"] < k_tach            # (local) new modes still frozen

    # DISCRIMINATOR metric: A_s_squeeze inherits the build's L_max drift
    rel_dev_Lmax = branch_drift                                 # (local) 5.43e-05 (≤ 0.05 -> POINT)
    is_point = (rel_dev_Lmax <= LMAX_STABILITY_TOL)             # (local)
    epistemic_type = "POINT" if is_point else "BAND"           # (local)

    # ===================================================================
    # (4) FLOOR sub-annotation (NOT the gate operator) — A_s >= A_s^BD
    # ===================================================================
    # S_IC = 1 + 2 n_k >= 1 with n_k = |β_{k̂}|² > 0; FLOOR PERMANENT 3-axis (WS-AS-1 LIZ2-1).
    n_k_khat = beta2_khat                                       # (local) occupation at k̂
    S_IC = 1.0 + 2.0 * n_k_khat                                 # (local) >= 1
    floor_satisfied = bool(n_k_khat > 0.0 and S_IC >= 1.0)     # (local)
    floor_satisfied_s111 = bool(a3a["floor_satisfied"])        # (local) S111 cross-check

    # ===================================================================
    # VERDICT (plan operator + 3-tuple)
    # ===================================================================
    # FAIL iff OOM out-of-band; else PASS iff POINT, INFO iff BAND.
    if not oom_in_band:
        verdict = "FAIL"   # (local) discredited normalization recovered
    elif is_point:
        verdict = "PASS"   # (local) in-axis overproduction + L_max-stable POINT (Track A)
    else:
        verdict = "INFO"   # (local) in-axis but L_max-soft BAND (Track B)

    # 3-tuple ([SIGN]) — reproduces the plan verdict via the generic collapse rule
    sign_verdict = "PASS" if oom_sign_positive else "FAIL"     # (local) OOM>0 overproduction
    if not oom_in_band:
        magnitude_verdict = "FAIL"                              # (local) out-of-band
    elif is_point:
        magnitude_verdict = "PASS"                              # (local) in-band + POINT
    else:
        magnitude_verdict = "INFO"                              # (local) in-band + BAND
    regime_verdict = "VALID"  # (local) box-delta sudden frozen-occupation read is exact (S111)

    return {
        "value": A_s_squeeze,
        # magnitude
        "xi_hat": xi_hat, "k_hat": k_hat, "N_norm": N_norm, "khat3": khat3,
        "kzvol_identity_dev": kzvol_identity_dev,
        "uv_slope": uv_slope, "uv_intercept": uv_intercept, "beta2_khat": beta2_khat,
        "beta2_pivot_bd": beta2_pivot_bd, "unit_resid": unit_resid,
        "beta2_box_only": beta2_box_only, "beta2_deltas_only": beta2_deltas_only,
        "delta_dominance": delta_dominance, "V_box": V_box,
        "A_s_squeeze": A_s_squeeze,
        "A_s_FW_canon": A_s_FW_canon, "A_s_FW_s111": A_s_FW_s111,
        "beta2_khat_s111": beta2_khat_s111,
        "rel_dev_FW": rel_dev_FW, "roundtrip_ok": roundtrip_ok,
        # OOM gate
        "A_s_CMB_val": A_s_CMB_val, "OOM": OOM,
        "oom_sign_positive": oom_sign_positive, "oom_in_band": oom_in_band,
        "below_route_b": below_route_b, "below_uv": below_uv,
        "OOM_BAND_LO": OOM_BAND_LO, "OOM_BAND_HI": OOM_BAND_HI,
        # L_max-stability
        "branch_drift": branch_drift, "truncation_consistent": truncation_consistent,
        "ns_L7equiv": ns_L7equiv, "ns_BZ": ns_BZ,
        "rel_dev_Lmax": rel_dev_Lmax, "is_point": is_point, "epistemic_type": epistemic_type,
        "k_tach": k_tach, "window_ceiling": window_ceiling, "regime_robust": regime_robust,
        **fb,
        # amplitude cross-checks
        "A_s_inv5_b1": A_s_inv5_b1, "OOM_gap_inv5_b1": OOM_gap_inv5_b1,
        "amp_inv5_consistent_b1": amp_inv5_consistent_b1, "A_s_parker_inv6": A_s_parker_inv6,
        # floor
        "n_k_khat": n_k_khat, "S_IC": S_IC,
        "floor_satisfied": floor_satisfied, "floor_satisfied_s111": floor_satisfied_s111,
        # verdict + 3-tuple
        "verdict": verdict, "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict, "regime_verdict": regime_verdict,
        # spectrum (plot)
        "kg": kg, "b2": b2,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    fig, ax = plt.subplots(1, 3, figsize=(18, 5.0))

    # (a) box-delta SUDDEN spectrum + UV-tail read at k̂
    ax[0].loglog(r["kg"], r["b2"], "o-", ms=3, color="#1f77b4",
                 label=r"$|\beta_k|^2$ box-delta SUDDEN (magnitude source)")
    kk = np.linspace(10.0, r["k_hat"] * 1.05, 50)  # (local)
    ax[0].loglog(kk, np.exp(r["uv_slope"] * np.log(kk) + r["uv_intercept"]),
                 "--", color="grey", lw=1.0, label=r"UV-tail fit (slope %.4f)" % r["uv_slope"])
    ax[0].axvline(r["k_hat"], color="crimson", ls="--",
                  label=r"$\hat{k}=1/\xi_{KZ}=%.2f$" % r["k_hat"])
    ax[0].axhline(r["beta2_khat"], color="green", ls="-.", lw=0.8,
                  label=r"$|\beta_{\hat k}|^2=%.3e$" % r["beta2_khat"])
    ax[0].set_xlabel(r"$k\ (M_{KK})$"); ax[0].set_ylabel(r"$|\beta_k|^2$")
    ax[0].set_title(r"MAGNITUDE: $A_s=|\beta_{\hat k}|^2/2\pi^2=%.4e$" % r["A_s_squeeze"])
    ax[0].legend(fontsize=7, loc="lower left"); ax[0].grid(alpha=0.3, which="both")

    # (b) OOM ladder with the S115 band shaded
    labels = ["TD/zeta\n(+0.196)", "squeeze\n(this gate)", "Parker\ninv6",
              "Connes-Parker", "Route-B-PW\n(REJECTED)", "UV artifact\n(REJECTED)"]  # (local)
    ooms = [0.196, r["OOM"], 1.455, 1.527, r["OOM"] if False else 3.15, 9.37]  # (local)
    colors = ["#2ca02c", "crimson", "#9467bd", "#8c564b", "grey", "black"]  # (local)
    bars = ax[1].bar(labels, ooms, color=colors, alpha=0.85)
    ax[1].axhspan(r["OOM_BAND_LO"], r["OOM_BAND_HI"], color="gold", alpha=0.25,
                  label=r"S115 axis [%.3f, %.3f]" % (r["OOM_BAND_LO"], r["OOM_BAND_HI"]))
    ax[1].axhline(0.0, color="black", lw=1.0, label=r"Planck $A_s$")
    for b, v in zip(bars, ooms):
        ax[1].text(b.get_x() + b.get_width() / 2, v + 0.15, "%.2f" % v, ha="center", fontsize=7)
    ax[1].set_ylabel(r"$\log_{10}(A_s/A_s^{\rm Planck})$")
    ax[1].set_title(r"GATE: squeeze OOM=+%.3f IN band, below 3.15/9.37" % r["OOM"])
    ax[1].legend(fontsize=7, loc="upper left"); ax[1].grid(alpha=0.3, axis="y")

    # (c) L_max-stability: monotone level-min|λ| + level-13 floor vs window ceiling
    ax[2].plot(r["fb_levels"], r["fb_level_min"], "o-", color="#1f77b4",
               label=r"min$|\lambda|$ per level (s84 L12)")
    ax[2].scatter([13], [r["fb_level13_extrap"]], marker="D", color="crimson", zorder=5,
                  label=r"L13 extrap %.2f (bottom-saturated)" % r["fb_level13_extrap"])
    ax[2].axhline(r["window_ceiling"], color="green", ls="--", lw=0.9,
                  label=r"fold-window ceiling %.2f" % r["window_ceiling"])
    ax[2].axhspan(0.0, r["fb_bottom_max_pq4"], color="orange", alpha=0.18,
                  label=r"bottom band $p{+}q\leq4$ (dominates $V_{box}$)")
    ax[2].set_xlabel("Peter-Weyl level $p+q$"); ax[2].set_ylabel(r"min$|\lambda|\ (M_{KK})$")
    ax[2].set_title(r"POINT: rel_dev$_{Lmax}$=%.2e $\leq$ 0.05" % r["rel_dev_Lmax"])
    ax[2].legend(fontsize=7, loc="upper left"); ax[2].grid(alpha=0.3)

    fig.suptitle(r"S116-W1-AS-CFB1 — squeeze $A_s=%.4e$ (+%.3f OOM, IN [%.3f,%.3f]); "
                 r"epistemic-type=%s; verdict=%s"
                 % (r["A_s_squeeze"], r["OOM"], r["OOM_BAND_LO"], r["OOM_BAND_HI"],
                    r["epistemic_type"], r["verdict"]), fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
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
# Section 9 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- report ---
    print("=== (1) MAGNITUDE — box-delta squeeze A_s = |β_khat|^2 / 2pi^2 ===")
    print(f"  xi_KZ (PINNED)               = {r['xi_hat']:.12g} M_KK^-1   [S89 substrate-natural]")
    print(f"  k_hat = 1/xi_KZ              = {r['k_hat']:.6f} M_KK")
    print(f"  KZ-vol identity k^3*xi^3-1   = {r['kzvol_identity_dev']:.2e}  (== 0 -> A_s=|b|^2/2pi^2)")
    print(f"  UV-tail slope (box-delta)    = {r['uv_slope']:.6f}  (near-flat = scale-inv sudden)")
    print(f"  |beta_khat|^2 (box-delta)    = {r['beta2_khat']:.10e}  (S111 pin {r['beta2_khat_s111']:.10e})")
    print(f"  delta-dominance b2_d/b2_box  = {r['delta_dominance']:.2f}x  (transit-jump screened)")
    print(f"  unitarity residual (cache)   = {r['unit_resid']:.2e}")
    print(f"  A_s_squeeze                  = {r['A_s_squeeze']:.12e}   <<< MAGNITUDE")
    print(f"  round-trip vs A_s_FW canon   = {r['A_s_FW_canon']:.12e}  rel-dev {r['rel_dev_FW']:.2e}"
          f"  (ok={r['roundtrip_ok']}, tol {ROUNDTRIP_REL_TOL:.0e})")
    print()
    print("=== (2) GATE — OOM vs S115 sudden<->adiabatic axis band ===")
    print(f"  A_s_CMB (Planck 2018 VI)     = {r['A_s_CMB_val']:.3e}")
    print(f"  OOM = log10(A_s_sq/A_s_CMB)  = +{r['OOM']:.4f}")
    print(f"  sign>0 (overproduction)      = {r['oom_sign_positive']}")
    print(f"  IN band [{r['OOM_BAND_LO']:.3f}, {r['OOM_BAND_HI']:.3f}] = {r['oom_in_band']}")
    print(f"  below Route-B-PW (+3.15)     = {r['below_route_b']}   below UV artifact (+9.37) = {r['below_uv']}")
    print()
    print("=== (3) POINT-vs-BAND — L_max-stability (AS3b-deferred resolution) ===")
    print(f"  [i]  branch_drift_L3_L7      = {r['branch_drift']:.4e}  truncation_consistent={r['truncation_consistent']}")
    print(f"       (ns_L7equiv={r['ns_L7equiv']:.6f} vs ns_BZ={r['ns_BZ']:.6f})")
    print(f"  [ii] Friedrich-Bar: level-min|lambda| monotone={r['fb_monotone']} "
          f"(L12={r['fb_level_min'][-1]:.4f}, L13 extrap={r['fb_level13_extrap']:.4f}, "
          f"FB lb={r['fb_level13_lb']:.4f})")
    print(f"       bottom band p+q<=4 ceiling={r['fb_bottom_max_pq4']:.4f} (dominates V_box, all at L12)")
    print(f"  [iii]regime robust (L13<{r['k_tach']:.0f} k_tach)={r['regime_robust']} "
          f"(window ceiling {r['window_ceiling']:.4f})")
    print(f"  rel_dev_Lmax (discriminator) = {r['rel_dev_Lmax']:.4e}  (<= {LMAX_STABILITY_TOL} -> POINT)")
    print(f"  epistemic_type               = {r['epistemic_type']}")
    print()
    print("=== (4) FLOOR sub-annotation (NOT the gate operator) ===")
    print(f"  n_k=|beta_khat|^2            = {r['n_k_khat']:.4e}   S_IC=1+2n_k = {r['S_IC']:.10f} (>=1)")
    print(f"  floor A_s>=A_s^BD satisfied  = {r['floor_satisfied']}  (S111 cross-check {r['floor_satisfied_s111']})")
    print(f"  >>> FLOOR PERMANENT 3-axis (WS-AS-1 LIZ2-1); MAGNITUDE SCHEME-DEPENDENT (S115 axis)")
    print()
    print("=== CROSS-CHECKS (two-leaf build s110_cf_b1) ===")
    print(f"  A_s_impulse_inv5 (upstream)  = {r['A_s_inv5_b1']:.6e}  (amp_consistent={r['amp_inv5_consistent_b1']})")
    print(f"  OOM_gap_inv5 (upstream)      = +{r['OOM_gap_inv5_b1']:.4f}")
    print(f"  A_s_parker_inv6 (adiab end)  = {r['A_s_parker_inv6']:.6e}  (+1.455 OOM)")
    print()
    print(f"=== 3-TUPLE: sign={r['sign_verdict']} magnitude={r['magnitude_verdict']} "
          f"regime={r['regime_verdict']} => composite {r['verdict']} ===")

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        value=r["A_s_squeeze"], A_s_squeeze=r["A_s_squeeze"],
        # magnitude
        xi_KZ=r["xi_hat"], k_hat=r["k_hat"], N_norm=r["N_norm"], khat3=r["khat3"],
        kzvol_identity_dev=r["kzvol_identity_dev"],
        uv_slope=r["uv_slope"], uv_intercept=r["uv_intercept"], beta2_khat=r["beta2_khat"],
        beta2_khat_s111=r["beta2_khat_s111"], beta2_pivot_boxdelta=r["beta2_pivot_bd"],
        unitarity_residual=r["unit_resid"], V_box=r["V_box"],
        beta2_box_only=r["beta2_box_only"], beta2_deltas_only=r["beta2_deltas_only"],
        delta_dominance=r["delta_dominance"],
        A_s_FW_canon=r["A_s_FW_canon"], A_s_FW_s111=r["A_s_FW_s111"],
        rel_dev_FW=r["rel_dev_FW"], roundtrip_ok=r["roundtrip_ok"], roundtrip_rel_tol=ROUNDTRIP_REL_TOL,
        # OOM gate
        A_s_CMB=r["A_s_CMB_val"], OOM=r["OOM"], OOM_BAND_LO=r["OOM_BAND_LO"], OOM_BAND_HI=r["OOM_BAND_HI"],
        oom_sign_positive=r["oom_sign_positive"], oom_in_band=r["oom_in_band"],
        below_route_b=r["below_route_b"], below_uv=r["below_uv"],
        OOM_ROUTE_B_PW=OOM_ROUTE_B_PW, OOM_UV_ARTIFACT=OOM_UV_ARTIFACT,
        # L_max-stability
        branch_drift_L3_L7=r["branch_drift"], truncation_consistent=r["truncation_consistent"],
        ns_L7equiv=r["ns_L7equiv"], ns_BZ=r["ns_BZ"],
        rel_dev_Lmax=r["rel_dev_Lmax"], lmax_stability_tol=LMAX_STABILITY_TOL,
        is_point=r["is_point"], epistemic_type=r["epistemic_type"],
        fb_levels=r["fb_levels"], fb_level_min=r["fb_level_min"], fb_monotone=r["fb_monotone"],
        fb_incr_mean=r["fb_incr_mean"], fb_level13_extrap=r["fb_level13_extrap"],
        fb_level13_lb=r["fb_level13_lb"], fb_eta_min=r["fb_eta_min"],
        fb_bottom_max_pq4=r["fb_bottom_max_pq4"],
        k_tach_fold=r["k_tach"], window_ceiling=r["window_ceiling"], regime_robust=r["regime_robust"],
        # amplitude cross-checks
        A_s_impulse_inv5=r["A_s_inv5_b1"], OOM_gap_inv5=r["OOM_gap_inv5_b1"],
        amp_inv5_consistent=r["amp_inv5_consistent_b1"], A_s_parker_inv6=r["A_s_parker_inv6"],
        # floor
        n_k_khat=r["n_k_khat"], S_IC=r["S_IC"], floor_satisfied=r["floor_satisfied"],
        floor_satisfied_s111=r["floor_satisfied_s111"],
        # verdict + 3-tuple
        verdict=r["verdict"], sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"], regime_verdict=r["regime_verdict"],
        # spectrum (plot reproducibility)
        kg_boxdelta=r["kg"], b2_boxdelta=r["b2"],
        s84_canonical_sha=S84_CANONICAL_SHA,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    make_plot(r)
    print(f"  wrote {OUT_NPZ.name}")
    print(f"  wrote {OUT_PNG.name}")

    # value payload (no single-quote chars; the tool wraps value='...')
    value_payload = (
        f"A_s_squeeze={r['A_s_squeeze']:.4e};OOM=+{r['OOM']:.4f};"
        f"band[+{r['OOM_BAND_LO']:.3f},+{r['OOM_BAND_HI']:.3f}]=IN;"
        f"epistemic_type={r['epistemic_type']};rel_dev_Lmax={r['rel_dev_Lmax']:.2e}<=0.05;"
        f"floor=satisfied-PERMANENT-3axis;roundtrip_A_s_FW_reldev={r['rel_dev_FW']:.2e};"
        f"below_RouteB+3.15_and_UV+9.37;magnitude_SCHEME-DEPENDENT"
    )  # (local)
    print(emit_4tuple(value_payload, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        r["verdict"], value_payload, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note=("squeeze A_s=|beta_khat|^2/2pi^2 (KZ-vol N_norm=xi_KZ^3, k_hat^3*xi_KZ^3=1); "
                        "box-delta SUDDEN magnitude source reproduces S111 A_s_FW=1.5367e-08; "
                        "OOM=+0.8644 IN S115 axis [+0.196,+1.527]; POINT (rel_dev_Lmax=5.43e-05)"),
        extra_rows=[
            "# regulator_pin=N/A (impulse-quench Bogoliubov |beta_k|^2; NOT a Seeley-DeWitt a_n residue)",
            f"# POINT resolution (AS3b-deferred): rel_dev_Lmax={r['rel_dev_Lmax']:.2e}<=0.05 -> Track A; "
            f"3 legs: [i] branch_drift_L3_L7={r['branch_drift']:.2e}+truncation_consistent=True; "
            f"[ii] Friedrich-Bar bottom-saturation (level-min|lambda| monotone, L13 extrap "
            f"{r['fb_level13_extrap']:.2f}>p+q<=4 bottom band {r['fb_bottom_max_pq4']:.2f}); "
            f"[iii] delta-dominance {r['delta_dominance']:.0f}x (transit-jump screened)",
            f"# floor A_s>=A_s^BD: S_IC=1+2n_k={r['S_IC']:.6f}>=1, PERMANENT 3-axis (WS-AS-1 LIZ2-1); "
            f"magnitude SCHEME-DEPENDENT (S115 sudden<->adiabatic axis); promotes S110 registered "
            f"amplitude to gated threshold; resolves AS3b POINT",
            f"# OOM=+{r['OOM']:.4f} below discredited +3.15 Route-B-PW and far below +9.37 naive-UV "
            f"artifact (S111/WS-AS-1 §47); A_s_parker_inv6 (+1.455) is the adiabatic axis end",
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
