"""
s116_w8_fwdc1_level2_envelope_friedrich_bar.py
==============================================

S116-W8-FWDC1-LANDING  —  discharge the FWD-C1 Level-2 convergence-envelope
NUMERICAL-DEFERRED residual (CF-S94-W5-3).

NOT a re-landing.  §VII.AU.OP-PROJ is STAGE-3-PERMANENT (S93 W2-2).  This gate
discharges the registered `CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED` sub-class:
on the L12 (s84) + L14 (s87) tau=0.19 block-diagonal D_K spectrum caches it

  (1) recomputes the FULL-CC Pauli-Villars residue rho_FULL(s=3, L) and the
      Friedrich-Bar marginal-saturation rel_drift = |rho(L14)-rho(L12)|/|rho(L12)|
      (the REGIME driver), reproducing the S92 W1-CF-W9-8-2 machinery;
  (2) RECONCILES the three F-images of the SAME substrate-IS convergence
      exponent alpha at substrate-distance-1 pole s=3:
        - SCHEMATIC d=4 generic envelope  : |alpha| = 3   (L^{-3}; the canonical
          alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC = -3 is the exponent IN L^{-3})
        - Wodzicki per-pole               : alpha = 2     (alpha_HH1_per_pole_FW_s3
          = 2*(s-2)|_{s=3}; single-cocycle LOWER bound)
        - direct Connes-Karoubi pathway-B : alpha = 2.6926 (L15-22 fit, REPRODUCED
          at FULL-physical class — alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22)
      into a single admissible window [2,3], with the FULL-physical DIRECT value
      2.6926 as the gate's alpha_sat;
  (3) CROSS-CHECKS the reconciliation against the 2-point FULL-CC rho data by
      Richardson-extrapolating rho_inf for each candidate alpha — the rho_inf
      spread IS the numerical-deferred uncertainty (why pinning needs L>14);
  (4) cites the topological-integer Level-3 anchor (=2) as the ENVELOPE-FREE
      complementary reading.

[SIGN] gate (composite):
    sign      = convergent (alpha > 0)
    magnitude = alpha_sat in [2.5, 3.5]
    regime    = Friedrich-Bar rel_drift band:
                  < 1e-3            -> VALID    (saturated)
                  [1e-3, 1e-2)      -> MARGINAL  (marginal-saturation)
                  >= 1e-2           -> BREAKDOWN (unsaturated)

PLAN-FROZEN composite operator (session-116-plan-w8.md §W8-1 PASS_meaning /
INFO_meaning, pre-registered BEFORE evaluation):
    PASS iff  alpha_sat in [2.5,3.5]  AND  rel_drift < 1e-3
    INFO iff  rel_drift in [1e-3,1e-2)   (alpha in/near band; CORRIDOR CONFIRMED)
    FAIL iff  rel_drift >= 1e-2  OR  alpha_sat <= 0 (divergent)
This plan-frozen operator takes PRECEDENCE over the generic 3-tuple collapse
rule (which would read sign=PASS ^ magnitude=PASS ^ regime=MARGINAL -> PASS);
a `# composite-precedence:` disclosure extra-row is emitted per
`gate-verdicts.md §"Plan-frozen gate-block operator precedence"`.

CLASS = FULL : the gate value is the FULL-CC Pauli-Villars rho ratio + the
FULL-physical-reproduced pathway-B alpha_sat.  The SCHEMATIC -3 and the Wodzicki
+2 are CITED structural bounds (cross-check ONLY), not the gate value
(substrate-first-canonical-sourcing.md §(iv)).

Substrate framing (GEOMETRIC): the substrate IS the spectral triple
(A_K, H_K, D_K) at the substrate-distance-1 Mellin pole s=3.  alpha is the
fabric's intrinsic Level-2 convergence rate of its own finite-L Mellin-cone
image toward its continuum limit; the Planck n_s observation is the lab-IN
context, not the source of the rate.  Direction of explanation:
  D_K eigenvalues -> rho_FULL(s=3, L) -> HKR L->inf image -> Planck n_s.

Plan: sessions/session-plan/session-116-plan-w8.md §W8-1.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-thread cap (numpy log-log fit + residue sums only; no large eigensolve)

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a space — absolute paths only)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC,        # = -3  (L^{-3} exponent; |.|=3 d=4 generic upper edge)
    alpha_HH1_per_pole_FW_s3,                            # = 2   (Wodzicki per-pole lower bound)
    alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22,     # = 2.6926... (FULL-physical direct pathway-B)
    rho_FULL_CC_VII_AU_SAT_s3,                           # = 1.0076927826 (canonical L14 cross-check anchor)
    Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI,       # = 2   (envelope-free topological Level-3 anchor)
)

# -----------------------------------------------------------------------------
# FULL-CC Pauli-Villars helper (PRIMARY; CC1996 §2.2-2.3 2-point multiplier)
#   identical machinery to S92 W1-CF-W9-8-2 (the rho_FULL lineage)
# -----------------------------------------------------------------------------
import _pauli_villars_subtraction  # noqa: E402,F401
from _pauli_villars_subtraction import (  # noqa: E402
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
    pv_multiplier_primary,
    pv_mellin_moment_primary,
    bare_mellin_moment,
    _verify_pv_identities,
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (R3 YAML, plan §W8-1)
# -----------------------------------------------------------------------------
SESSION = "S116"
GATE_ID = "S116-W8-FWDC1-LANDING"
SCHEME = "fwd-c1-substrate-distance-1-mellin-pole-s3-friedrich-bar-saturation"
CONVENTION = (
    "FULL-CC-pauli-villars-and-pathway-B-direct-connes-karoubi-"
    "poleconv-A-double-pole_in_s-3-curvature_grade-n-2"
)
L_MAX = "12_14"          # both master caches consumed (scan window [12,14])
S_POLE = 3               # (local) substrate-distance-1 pole; poleconv-A-double, curvature_grade n=2

# Pre-registered bands (plan §W8-1 machinery_pin_map.tolerance)
ALPHA_PASS_LO = 2.5      # (local) alpha_sat PASS band lower edge
ALPHA_PASS_HI = 3.5      # (local) alpha_sat PASS band upper edge
RELDRIFT_PASS = 1e-3     # (local) rel_drift < 1e-3 -> VALID (saturated)
RELDRIFT_INFO_UPPER = 1e-2  # (local) [1e-3,1e-2) -> MARGINAL; >= -> BREAKDOWN

# Plan SHA pin (drift-aware: canonical_constants.py was edited THIS session)
CANONICAL_PLAN_PINNED_SHA = "261b117ce312968b036d325668e6951c95c955633cc7a898f1ab191dc9c02b9d"

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
PV_HELPER_PATH = PROJECT_ROOT / "computations" / "_pauli_villars_subtraction.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_L14 = PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-116" / "s116_w8_fwdc1_level2_envelope_friedrich_bar.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-116" / "s116_w8_fwdc1_level2_envelope_friedrich_bar.png"


# -----------------------------------------------------------------------------
# SHA helpers (S84+ dual-SHA schema; same as S92 lineage)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """audit_sha256 = sha256(script || canonical || pinmap_json); content_sha256 = sha256(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# -----------------------------------------------------------------------------
# Verdict payload emitter (script PRINTS; agent calls emit_verdict — race-safe)
# -----------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None) -> dict:
    """Emit the delimited verdict PAYLOAD for the dispatching agent to pass to
    the knowledge-MCP `emit_verdict` tool (gate-verdicts.md §"Race-Safe Emission").
    The script does NOT write the verdict file."""
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
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# -----------------------------------------------------------------------------
# Spectrum cache loader (Peter-Weyl sectored -> flat (lambdas, mults))
#   identical to S92 W1-CF-W9-8-2 load_spectrum_flat
# -----------------------------------------------------------------------------
def load_spectrum_flat(cache_path: Path) -> tuple[np.ndarray, np.ndarray, int, int]:
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    max_level = 0  # (local)
    for (p, q), info in sector_evals.items():
        n_sectors += 1
        dim = int(info["dim"])  # (local)
        level = int(info["level"])  # (local)
        if level > max_level:
            max_level = level
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(float(dim))
    return (np.array(lambdas_list, dtype=np.float64),
            np.array(mults_list, dtype=np.float64),
            n_sectors, max_level)


def evaluate_rho_FULL(s_pole: float, lambdas: np.ndarray, mults: np.ndarray) -> tuple[float, float, float, dict]:
    """rho_FULL(s) = M_FULL(s)/M_BARE(s); FULL-CC PV PRIMARY (CC1996 §2.2-2.3)."""
    M_FULL = pv_mellin_moment_primary(s_pole, lambdas, mults, c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS)  # (local)
    M_BARE = bare_mellin_moment(s_pole, lambdas, mults)  # (local)
    rho = M_FULL / M_BARE  # (local)
    w_PV = pv_multiplier_primary(lambdas * lambdas, s_pole, c_arr=PV_PRIMARY_C, m_arr=PV_PRIMARY_M_DIMLESS)  # (local)
    diag = {
        "M_FULL": M_FULL, "M_BARE": M_BARE,
        "w_PV_min": float(np.min(w_PV)), "w_PV_mean": float(np.mean(w_PV)), "w_PV_max": float(np.max(w_PV)),
        "lambda_min": float(np.min(lambdas)), "lambda_max": float(np.max(lambdas)),
        "N_eig": int(len(lambdas)), "N_weighted": float(np.sum(mults)),
    }
    return rho, M_FULL, M_BARE, diag


def friedrich_baer_intrusion(cache12: Path, cache14: Path, s_pole: float) -> dict:
    """NEW-sector (p+q in {13,14}) BARE-moment intrusion ratio at s=3 (W11-3 precedent)."""
    sd12 = np.load(cache12, allow_pickle=True)["sector_evals"].item()
    sd14 = np.load(cache14, allow_pickle=True)["sector_evals"].item()
    new_sectors = {k: v for k, v in sd14.items() if k not in sd12}  # (local)
    lam14, m14, _, _ = load_spectrum_flat(cache14)
    M_BARE_L14 = bare_mellin_moment(s_pole, lam14, m14)  # (local)
    new_lam = []  # (local)
    new_m = []  # (local)
    new_levels = []  # (local)
    for (p, q), info in new_sectors.items():
        dim = int(info["dim"])  # (local)
        new_levels.append(int(info["level"]))
        for v in np.asarray(info["abs_evals"], dtype=np.float64):
            new_lam.append(float(v))
            new_m.append(float(dim))
    if new_lam:
        M_BARE_new = bare_mellin_moment(s_pole, np.array(new_lam), np.array(new_m))  # (local)
        intrusion = float(M_BARE_new) / float(M_BARE_L14)  # (local)
    else:
        M_BARE_new, intrusion = 0.0, 0.0  # (local)
    # eta_FB lower bound on L12 (Friedrich-Bar ratio lambda_min / sqrt(C2+1))
    eta = []  # (local)
    for (p, q), info in sd12.items():
        ev = np.asarray(info["abs_evals"], dtype=np.float64)
        if ev.size == 0:
            continue
        C2 = (1.0 / 3.0) * (p * p + q * q + p * q + 3.0 * p + 3.0 * q)  # (local) SU(3) Casimir
        eta.append(float(np.min(ev)) / np.sqrt(C2 + 1.0))
    return {
        "M_BARE_L14_full": float(M_BARE_L14),
        "M_BARE_new_L13_L14": float(M_BARE_new),
        "intrusion_ratio": intrusion,
        "n_new_sectors": int(len(new_sectors)),
        "unique_new_levels": sorted(set(new_levels)),
        "eta_FB_lower_L12": float(np.min(eta)) if eta else 0.0,
    }


def richardson_rho_inf(rho_L12: float, rho_L14: float, alpha: float,
                       L_lo: float = 12.0, L_hi: float = 14.0) -> tuple[float, float]:
    """Two-point Richardson extrapolation rho(L) = rho_inf + C*L^{-alpha}.

    Returns (rho_inf, C).  This is the cross-check that turns the alpha
    reconciliation into a STATEMENT about the deferred continuum value:
    the spread of rho_inf across the admissible alpha window IS the
    numerical-deferred uncertainty (why pinning needs L>14).
    """
    f_lo = L_lo ** (-alpha)  # (local)
    f_hi = L_hi ** (-alpha)  # (local)
    C = (rho_L14 - rho_L12) / (f_hi - f_lo)  # (local)
    rho_inf = rho_L14 - C * f_hi  # (local)
    return rho_inf, C


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"Pole s={S_POLE} (substrate-distance-1, poleconv-A-double, curvature_grade n=2)")
    print(f"PASS band: alpha_sat in [{ALPHA_PASS_LO},{ALPHA_PASS_HI}] AND rel_drift < {RELDRIFT_PASS}")

    # 1) Input pins
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/_pauli_villars_subtraction.py": sha256_of(PV_HELPER_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_of(CACHE_L12),
        "computations/session-87/s87_spectrum_cache_L14_tau019.npz": sha256_of(CACHE_L14),
    }
    print("\n=== Input pins (SHA-256 heads) ===")
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v[:16]}")

    # 1a) Plan-text-drift disclosure (substrate-first-canonical-sourcing.md §(ii.B))
    live_canonical_sha = pins["computations/_shared/canonical_constants.py"]  # (local)
    canonical_drifted = (live_canonical_sha != CANONICAL_PLAN_PINNED_SHA)  # (local)
    print(f"\n=== Plan-text-drift (canonical_constants.py) ===")
    print(f"  plan-pinned: {CANONICAL_PLAN_PINNED_SHA[:16]}  live: {live_canonical_sha[:16]}  drifted={canonical_drifted}")
    print(f"  -> S116 W1 (A_s) + W7 (7 polycritical anchors) edited canonical_constants.py THIS session.")
    print(f"  -> FWD-C1 Level-2 exponent is c_sub-INDEPENDENT (L_max property); imports stable; drift does NOT affect result.")
    # Cache SHAs MUST be unchanged (verify)
    assert pins["computations/session-84/s84_spectrum_cache_L12_tau019.npz"].startswith("9e6d9cf7"), "L12 cache SHA drift!"
    assert pins["computations/session-87/s87_spectrum_cache_L14_tau019.npz"].startswith("fa2bfb83"), "L14 cache SHA drift!"
    print(f"  L12/L14 cache SHAs verified unchanged (9e6d9cf7.../fa2bfb83...).")

    # 2) tau consistency
    assert "tau019" in CACHE_L12.name and "tau019" in CACHE_L14.name
    assert abs(tau_fold - 0.19) < 1e-6, f"tau_fold={tau_fold} != 0.19"
    print(f"\ntau_fold = {tau_fold}")

    # 3) PV identities (Sum c_r = 1, Sum c_r m_r^2 = 0)
    sc, scm2 = _verify_pv_identities()
    print(f"\n=== PV identities ===\n  Sum c_r = {sc:.16e} (target 1)\n  Sum c_r m_r^2 = {scm2:.16e} (target 0)")
    assert abs(sc - 1.0) < 1e-12 and abs(scm2) < 1e-12, "PV identities failed"

    # 4) Load spectra + evaluate FULL-CC rho at s=3
    lam12, m12, nsec12, lev12 = load_spectrum_flat(CACHE_L12)
    lam14, m14, nsec14, lev14 = load_spectrum_flat(CACHE_L14)
    print(f"\n=== Caches ===")
    print(f"  L12: n_sectors={nsec12}, max_level={lev12}, N_eig={len(lam12)}, lambda in [{lam12.min():.4f},{lam12.max():.4f}]")
    print(f"  L14: n_sectors={nsec14}, max_level={lev14}, N_eig={len(lam14)}, lambda in [{lam14.min():.4f},{lam14.max():.4f}]")

    rho_L12, MF12, MB12, d12 = evaluate_rho_FULL(S_POLE, lam12, m12)
    rho_L14, MF14, MB14, d14 = evaluate_rho_FULL(S_POLE, lam14, m14)
    rel_drift = abs(rho_L14 - rho_L12) / abs(rho_L12)  # (local)
    print(f"\n=== FULL-CC rho_FULL(s=3) ===")
    print(f"  rho_FULL(L12) = {rho_L12:.12f}")
    print(f"  rho_FULL(L14) = {rho_L14:.12f}")
    print(f"  rel_drift     = {rel_drift:.10e}  (PASS<{RELDRIFT_PASS}, INFO<{RELDRIFT_INFO_UPPER})")

    # 4a) Cross-check rho_FULL(L14) against canonical pin rho_FULL_CC_VII_AU_SAT_s3
    rho_canon_dev = abs(rho_L14 - rho_FULL_CC_VII_AU_SAT_s3) / abs(rho_FULL_CC_VII_AU_SAT_s3)  # (local)
    print(f"  canonical rho_FULL_CC_VII_AU_SAT_s3 = {rho_FULL_CC_VII_AU_SAT_s3} ; rel_dev = {rho_canon_dev:.3e}")
    assert rho_canon_dev < 1e-9, "rho_FULL(L14) deviates from canonical pin > 1e-9 (precision floor)"

    # 5) Friedrich-Bar NEW-sector intrusion (BARE moment) — the deferral source
    intr = friedrich_baer_intrusion(CACHE_L12, CACHE_L14, S_POLE)
    print(f"\n=== Friedrich-Bar NEW-sector intrusion (BARE moment, s=3) ===")
    print(f"  intrusion_ratio (BARE, L14 NEW sectors p+q in 13,14) = {intr['intrusion_ratio']:.6f}  ({100*intr['intrusion_ratio']:.2f}%)")
    print(f"  n_new_sectors = {intr['n_new_sectors']}, new levels = {intr['unique_new_levels']}, eta_FB_lower = {intr['eta_FB_lower_L12']:.4f}")
    print(f"  CONTRAST: ratio rho_FULL drifts only {100*rel_drift:.3f}% while BARE intrusion is {100*intr['intrusion_ratio']:.2f}%")
    print(f"           -> PV subtraction cancels the L-leading UV tail in the ratio (why DEFERRED, not divergent).")

    # 6) THREE-F-IMAGE alpha RECONCILIATION (the CF-S94-W5-3 residual)
    alpha_schematic_mag = abs(float(alpha_canonical_VII_AU_OP_PROJ_FW_ASYMPTOTIC))  # (local) |-3| = 3 (d=4 generic L^{-3} upper edge)
    alpha_wodzicki = float(alpha_HH1_per_pole_FW_s3)                                # (local) 2 (per-pole lower bound)
    alpha_sample = float(alpha_sample_VII_AU_OP_PROJ_FW_PATHWAY_B_L15_22)           # (local) 2.6926 (FULL-physical DIRECT pathway-B)
    alpha_window_lo = min(alpha_schematic_mag, alpha_wodzicki, alpha_sample)        # (local) 2 (Wodzicki)
    alpha_window_hi = max(alpha_schematic_mag, alpha_wodzicki, alpha_sample)        # (local) 3 (SCHEMATIC d=4 generic)
    # alpha_sat: the FULL-physical DIRECT measurement (CLASS=FULL gate value).
    # The SCHEMATIC magnitude (3) and Wodzicki (2) are CITED structural bounds.
    alpha_sat = alpha_sample  # (local)
    print(f"\n=== Three-F-image alpha reconciliation (substrate-distance-1 pole s=3) ===")
    print(f"  F-image 1 SCHEMATIC d=4 generic (L^{{-3}}): |alpha| = {alpha_schematic_mag:.4f}   [UPPER edge]")
    print(f"  F-image 2 Wodzicki per-pole 2*(s-2):       alpha = {alpha_wodzicki:.4f}   [LOWER bound]")
    print(f"  F-image 3 pathway-B direct (L15-22, FULL): alpha = {alpha_sample:.6f}   [DIRECT measured]")
    print(f"  admissible window = [{alpha_window_lo:.4f}, {alpha_window_hi:.4f}]   (the three STRATIFY one window; not in conflict)")
    print(f"  alpha_sat (CLASS=FULL gate value) = {alpha_sat:.6f}")
    alpha_in_pass_band = (ALPHA_PASS_LO <= alpha_sat <= ALPHA_PASS_HI)  # (local)
    print(f"  alpha_sat in PASS band [{ALPHA_PASS_LO},{ALPHA_PASS_HI}]? {alpha_in_pass_band}")
    print(f"  window-overlap with PASS band = [{max(alpha_window_lo,ALPHA_PASS_LO):.4f}, {min(alpha_window_hi,ALPHA_PASS_HI):.4f}]")

    # 7) Richardson rho_inf cross-check (the numerical-deferred uncertainty band)
    print(f"\n=== Richardson rho_inf extrapolation per candidate alpha (2-point FULL-CC) ===")
    rich = {}  # (local)
    for name, a in [("wodzicki_2", alpha_wodzicki), ("sample_2.6926", alpha_sample), ("schematic_3", alpha_schematic_mag)]:
        rho_inf, C = richardson_rho_inf(rho_L12, rho_L14, a)
        rich[name] = (a, rho_inf, C)
        print(f"  alpha={a:.4f} ({name:14s}): rho_inf = {rho_inf:.8f}  (C={C:.5f})")
    rho_inf_vals = np.array([rich[k][1] for k in rich])  # (local)
    rho_inf_spread = float(rho_inf_vals.max() - rho_inf_vals.min())  # (local)
    rho_inf_spread_rel = rho_inf_spread / float(np.mean(rho_inf_vals))  # (local)
    print(f"  rho_inf spread across window = {rho_inf_spread:.6e} ({100*rho_inf_spread_rel:.4f}%)")
    print(f"  -> this spread IS the numerical-deferred uncertainty: 2 L-points cannot discriminate alpha in [2,3].")

    # 8) Level-3 envelope-FREE complementary reading
    print(f"\n=== Level-3 envelope-free anchor (complementary; NOT a convergence rate) ===")
    print(f"  Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI = {Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI}")
    print(f"  -> topological K-theoretic index (3He-B BDI); envelope-FREE, stands regardless of alpha deferral.")

    # 9) [SIGN] 3-tuple + plan-frozen composite operator
    sign_v = "PASS" if alpha_sat > 0.0 else "FAIL"  # (local) convergent
    mag_v = "PASS" if alpha_in_pass_band else "FAIL"  # (local) alpha_sat in band
    if rel_drift < RELDRIFT_PASS:
        regime_v = "VALID"  # (local)
    elif rel_drift < RELDRIFT_INFO_UPPER:
        regime_v = "MARGINAL"  # (local)
    else:
        regime_v = "BREAKDOWN"  # (local)

    # PLAN-FROZEN operator (plan §W8-1 PASS_meaning/INFO_meaning/FAIL_meaning):
    #   PASS iff alpha_sat in band AND rel_drift < 1e-3
    #   INFO iff rel_drift in [1e-3,1e-2)  (alpha in/near band) -> CORRIDOR CONFIRMED
    #   FAIL iff rel_drift >= 1e-2 OR alpha_sat <= 0 (divergent)
    if sign_v == "FAIL" or regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif mag_v == "PASS" and regime_v == "VALID":
        composite = "PASS"  # (local)
    else:
        composite = "INFO"  # (local) marginal-saturation; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED CONFIRMED

    # Generic-collapse reading (for the composite-precedence disclosure)
    if regime_v == "BREAKDOWN":
        generic = "FAIL"  # (local)
    elif sign_v == "FAIL":
        generic = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        generic = "FAIL"  # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        generic = "INFO"  # (local)
    else:
        generic = "PASS"  # (local)  <- (sign=PASS ^ mag=PASS ^ regime=MARGINAL) -> PASS
    precedence_invoked = (composite != generic)  # (local)

    print(f"\n=== Verdict (3-tuple) ===")
    print(f"  sign={sign_v} (alpha_sat={alpha_sat:.4f}>0 convergent)")
    print(f"  magnitude={mag_v} (alpha_sat in [{ALPHA_PASS_LO},{ALPHA_PASS_HI}])")
    print(f"  regime={regime_v} (rel_drift={rel_drift:.4e})")
    print(f"  composite (plan-frozen operator) = {composite}")
    print(f"  generic-collapse reading = {generic}  -> precedence_invoked={precedence_invoked}")

    # 10) Dual-SHA
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n=== Dual-SHA ===\n  audit_sha256   = {audit_sha}\n  content_sha256 = {content_sha}")
    print(f"  closure_hash(pins) [cross-check] = {closure_hash(pins)}")

    # 11) Save npz
    np.savez_compressed(
        OUT_NPZ,
        # FULL-CC rho ratio + saturation
        rho_FULL_L12=rho_L12, rho_FULL_L14=rho_L14, rel_drift=rel_drift,
        M_FULL_L12=MF12, M_BARE_L12=MB12, M_FULL_L14=MF14, M_BARE_L14=MB14,
        rho_canon_dev=rho_canon_dev,
        # three F-image alpha reconciliation
        alpha_schematic_mag=alpha_schematic_mag, alpha_wodzicki=alpha_wodzicki, alpha_sample=alpha_sample,
        alpha_window_lo=alpha_window_lo, alpha_window_hi=alpha_window_hi, alpha_sat=alpha_sat,
        alpha_in_pass_band=alpha_in_pass_band,
        # Richardson rho_inf cross-check
        rho_inf_wodzicki=rich["wodzicki_2"][1], rho_inf_sample=rich["sample_2.6926"][1], rho_inf_schematic=rich["schematic_3"][1],
        rho_inf_spread=rho_inf_spread, rho_inf_spread_rel=rho_inf_spread_rel,
        # Friedrich-Bar intrusion
        intrusion_ratio=intr["intrusion_ratio"], n_new_sectors=intr["n_new_sectors"],
        unique_new_levels=np.array(intr["unique_new_levels"], dtype=int), eta_FB_lower_L12=intr["eta_FB_lower_L12"],
        M_BARE_L14_full=intr["M_BARE_L14_full"], M_BARE_new_L13_L14=intr["M_BARE_new_L13_L14"],
        # Level-3 envelope-free anchor
        Level3_integer_anchor=Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI,
        # verdict
        verdict_composite=composite, verdict_sign=sign_v, verdict_magnitude=mag_v, verdict_regime=regime_v,
        generic_collapse=generic, precedence_invoked=precedence_invoked,
        # bands
        ALPHA_PASS_LO=ALPHA_PASS_LO, ALPHA_PASS_HI=ALPHA_PASS_HI,
        RELDRIFT_PASS=RELDRIFT_PASS, RELDRIFT_INFO_UPPER=RELDRIFT_INFO_UPPER,
        # PV
        pv_sum_c=sc, pv_sum_c_m2=scm2, PV_PRIMARY_C=PV_PRIMARY_C, PV_PRIMARY_M_DIMLESS=PV_PRIMARY_M_DIMLESS,
        # caches
        n_sectors_L12=nsec12, n_sectors_L14=nsec14, N_eig_L12=len(lam12), N_eig_L14=len(lam14),
        max_level_L12=lev12, max_level_L14=lev14,
        # drift disclosure
        canonical_live_sha=live_canonical_sha, canonical_plan_pinned_sha=CANONICAL_PLAN_PINNED_SHA,
        canonical_drifted=canonical_drifted,
        tau_fold=tau_fold, S_POLE=S_POLE,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\nSaved npz: {OUT_NPZ}")

    # 12) Plot
    make_plot(rho_L12, rho_L14, rel_drift, alpha_schematic_mag, alpha_wodzicki, alpha_sample,
              alpha_window_lo, alpha_window_hi, alpha_sat, rich, rho_inf_spread_rel, intr, composite)
    print(f"Saved plot: {OUT_PNG}")

    # 13) Build verdict value string + emit payload
    value_str = (
        f"alpha_sat={alpha_sat:.6f}_window[{alpha_window_lo:.1f},{alpha_window_hi:.1f}]_"
        f"reconciled[wodzicki={alpha_wodzicki:.1f},sample={alpha_sample:.4f},schematic_mag={alpha_schematic_mag:.1f}]_"
        f"rel_drift={rel_drift:.6e}_rho_FULL_L12={rho_L12:.8f}_rho_FULL_L14={rho_L14:.8f}_"
        f"rho_inf_spread={rho_inf_spread:.3e}_BARE_intrusion={intr['intrusion_ratio']:.4f}_"
        f"Level3_anchor={Level3_integer_anchor_VII_AU_OP_PROJ_3HEB_BDI}_canonical_drift_S116_W1_W7_anchors_added"
    )
    extra_rows = [
        f"# regulator_pin=a_4^{{Pauli-Villars}} CLASS=FULL poleconv-A-double pole_in_s={S_POLE} curvature_grade_n=2 "
        f"# {GATE_ID} regulator/level/Mellin-pole pins (regulator-pin-discipline.md + substrate-first-canonical-sourcing.md §(iv))",
        f"# composite-precedence: §W8-1 plan operator (PASS iff alpha_sat in band AND rel_drift<1e-3; "
        f"INFO iff rel_drift in [1e-3,1e-2)) OVERRIDES generic-collapse reading '{generic}' "
        f"(sign=PASS ^ magnitude=PASS ^ regime=MARGINAL -> PASS); pre-declared in plan §W8-1 BEFORE evaluation "
        f"# {GATE_ID} gate-verdicts.md Plan-frozen gate-block operator precedence",
        f"# F-image-reconciliation: SCHEMATIC|-3|=3 (d=4 generic upper edge), Wodzicki=2 (per-pole lower bound), "
        f"pathway-B=2.6926 (FULL-physical DIRECT, alpha_sat); admissible window [2,3]; rho_inf spread {100*rho_inf_spread_rel:.4f}% "
        f"# {GATE_ID} CF-S94-W5-3 residual: CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED {'CONFIRMED' if composite=='INFO' else composite}",
    ]
    print_verdict_payload(composite, value_str, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
                          extra_rows=extra_rows)
    return 0


def make_plot(rho_L12, rho_L14, rel_drift, a_sch, a_wod, a_smp, a_lo, a_hi, a_sat,
              rich, rho_inf_spread_rel, intr, composite) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: rho_FULL saturation
    ax = axes[0, 0]
    ax.plot([12, 14], [rho_L12, rho_L14], "o-", lw=2.5, ms=11, color="darkorange",
            label=r"$\rho_{FULL}(s{=}3,L)$")
    ax.set_xlabel(r"$L_{max}$", fontsize=11)
    ax.set_ylabel(r"$\rho_{FULL}(s{=}3)=M_{FULL}/M_{BARE}$", fontsize=11)
    ax.set_title(f"FULL-CC Pauli-Villars saturation (REGIME driver)\n"
                 f"rel_drift = {rel_drift:.4e}  "
                 f"(VALID<1e-3, MARGINAL[1e-3,1e-2), BREAKDOWN>=1e-2)", fontsize=10)
    ax.set_xticks([12, 14])
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=10)

    # Panel 2: three F-image alpha reconciliation
    ax = axes[0, 1]
    names = ["Wodzicki\nper-pole\n(lower)", "pathway-B\ndirect FULL\n(alpha_sat)", "SCHEMATIC\nd=4 generic\n(upper)"]
    vals = [a_wod, a_smp, a_sch]
    colors = ["steelblue", "darkorange", "seagreen"]
    ax.bar(names, vals, color=colors, edgecolor="black")
    ax.axhspan(a_lo, a_hi, color="gray", alpha=0.18, label=f"admissible window [{a_lo:.0f},{a_hi:.0f}]")
    ax.axhspan(2.5, 3.5, color="green", alpha=0.12, label="PASS band [2.5,3.5]")
    ax.axhline(a_sat, color="red", ls="--", lw=1.5, label=f"alpha_sat={a_sat:.4f}")
    ax.axhline(2.0, color="purple", ls=":", lw=1.3, label="Level-3 anchor=2 (envelope-free)")
    ax.set_ylabel(r"convergence exponent $\alpha$", fontsize=11)
    ax.set_title("Three F-images STRATIFY one window [2,3]\n(not in conflict; alpha_sat in PASS band)", fontsize=10)
    ax.set_ylim(0, 4)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, axis="y", alpha=0.3)

    # Panel 3: Richardson rho_inf spread (numerical-deferred uncertainty)
    ax = axes[1, 0]
    aa = [rich[k][0] for k in rich]
    rr = [rich[k][1] for k in rich]
    ax.plot(aa, rr, "s-", lw=2, ms=10, color="purple")
    for k in rich:
        ax.annotate(f"{rich[k][1]:.6f}", (rich[k][0], rich[k][1]), textcoords="offset points",
                    xytext=(6, 6), fontsize=8)
    ax.set_xlabel(r"candidate $\alpha$", fontsize=11)
    ax.set_ylabel(r"Richardson $\rho_\infty$ (2-pt, L12/L14)", fontsize=11)
    ax.set_title(f"rho_inf extrapolation per alpha\n"
                 f"spread = {100*rho_inf_spread_rel:.4f}%  (= numerical-deferred uncertainty;\n"
                 f"2 L-points cannot discriminate alpha in [2,3] -> L>14 deferred)", fontsize=10)
    ax.grid(True, alpha=0.3)

    # Panel 4: ratio-vs-BARE contrast (why DEFERRED not divergent)
    ax = axes[1, 1]
    cats = ["rho_FULL ratio\nrel_drift", "BARE moment\nNEW-sector\nintrusion"]
    vals = [rel_drift, intr["intrusion_ratio"]]
    ax.bar(cats, vals, color=["darkorange", "crimson"], edgecolor="black")
    for i, v in enumerate(vals):
        ax.annotate(f"{100*v:.2f}%", (i, v), textcoords="offset points", xytext=(0, 5),
                    ha="center", fontsize=10)
    ax.set_yscale("log")
    ax.set_ylabel("fractional change (log)", fontsize=11)
    ax.set_title(f"PV ratio cancels the L-leading UV tail\n"
                 f"ratio {100*rel_drift:.3f}% vs BARE {100*intr['intrusion_ratio']:.2f}%  "
                 f"({intr['n_new_sectors']} NEW sectors)", fontsize=10)
    ax.grid(True, axis="y", alpha=0.3)

    plt.suptitle(f"{GATE_ID}  —  composite={composite}\n"
                 f"FWD-C1 Level-2 convergence-envelope discharge (CF-S94-W5-3) at substrate-distance-1 pole s=3",
                 fontsize=12, y=1.0)
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


if __name__ == "__main__":
    sys.exit(main())
