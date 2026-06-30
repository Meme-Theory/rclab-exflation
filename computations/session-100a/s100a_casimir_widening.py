#!/usr/bin/env python3
"""
S100a W2-3 S100a-CASIMIR-WIDENING -- envelope widening W vs the
consecutive-Casimir-gap ratio 9/5 on the triality tower
=============================================================================

Gate: S100a-CASIMIR-WIDENING ([SIGN])
Plan: sessions/session-plan/session-100a-plan-w2.md SS W2-3
Classification: GEOMETRIC

Pre-registered discriminator bands (plan tolerance pin, FROZEN at plan-freeze
2026-06-03, BEFORE any computation):
    PASS : W in [1.80, 1.89]      (Casimir-ladder band centred on 9/5 = 1.800)
    INFO : |W - 4/3| <= 0.05      (fundamental (k,0) tower selected -- wrong
                                   sector assignment; C2 ladder real, wrong rungs)
    FAIL : otherwise              (named onset W >= 2.5; generic equal-Dlog ~ 3.0)

Method (plan SS W2-3, executed exactly):
  (1) Confirm the tower assignment (1,0)/(1,1)/(3,0) with exact-rational
      C2 = (4/3, 3, 6)  [Fraction arithmetic in-script; Sage-QQ cross-check
      recorded agent-side: C2 tower [4/3,3,6], g_lo=5/3, g_hi=3, W=9/5,
      W_fund=4/3, dims (3,8,10), trialities (1,0,0) -- all True].
  (2) From the Item-6 diagonal overlaps {d_i} (s100a_yukawa_overlap_offdiag.npz),
      form g_lo = ln(d_(1,1)/d_(1,0)), g_hi = ln(d_(3,0)/d_(1,1)), W = g_hi/g_lo.
  (3) Structural anchor: pure-Casimir-gap ratio
      (C2(3,0)-C2(1,1))/(C2(1,1)-C2(1,0)) = 3/(5/3) = 9/5 (exact).
  (4) Compare the integral-derived W against the three discriminator bands.

Substitution chain (math-scripts.md, sign/direction claim):
  Def 1: C2(p,q) = (p^2 + q^2 + p*q + 3p + 3q)/3        [SU(3) quadratic Casimir]
  Def 2: tower = {(1,0),(1,1),(3,0)} => C2 = {4/3, 3, 6}
  Def 3: g_lo = ln(d_(1,1)/d_(1,0)) ; g_hi = ln(d_(3,0)/d_(1,1))
  Def 4: W = g_hi / g_lo
  Casimir anchor: g_lo^cas = 3 - 4/3 = 5/3 ; g_hi^cas = 6 - 3 = 3
                  W_cas = 3/(5/3) = 9/5 = 1.800 exact  (predicted: positive,
                  both gaps same-sign, ratio in PASS band)
  Realised (Item-6 d_i): substituted numerically at runtime, printed below.
  Direction read-off: sign(W_computed) vs sign(W_cas = +9/5).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py            (runtime SHA)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
        plan-freeze pin 9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9
  - computations/session-100a/s100a_yukawa_overlap_offdiag.npz  (Item-6 output;
        runtime SHA; 4th audit ingredient per plan audit_discriminators)

Output 4-tuple:
  (value=<W + cross-checks>, scheme=CASIMIR-LADDER-WIDENING, convention=RATIO,
   L_max=12)

Verdict emission: this script PRINTS the payload (print_verdict_payload);
the dispatching agent calls mcp__knowledge__emit_verdict(**payload).
NO open("a") verdict write (Windows cross-process race, S98 lost 5/8 lines).

Casimir eigenvalues here are group-theoretic (C2(p,q)), NOT Seeley-DeWitt
heat-kernel coefficients -> no a_n regulator pin. No SCHEMATIC helper -> no
CLASS pin. The widening is a scheme-invariant RATIO (lizzi functional-
independence pin).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 -- CPU thread cap (machinery pin GPU_path: numpy.linalg, OMP 8)
# MUST precede every numpy import, including the one inside canonical_constants.
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED = Path(__file__).resolve().parent.parent / "_shared"   # (local)
sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403  (tau_fold, m_e, m_mu, R_cross_yukawa_t1_t2)

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from fractions import Fraction as Fr
from math import log

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration (ALL pinned before compute)
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                    # (local)
GATE_ID = "S100a-CASIMIR-WIDENING"                                  # (local)
SCHEME = "CASIMIR-LADDER-WIDENING"                                  # (local)
CONVENTION = "RATIO"                                                # (local)
L_MAX = "12"                                                        # (local)

# Pre-registered discriminator bands (plan SS W2-3 tolerance pin; closed bands)
PASS_BAND_LO = 1.80          # Casimir-ladder band, lower edge (9/5)   # (local)
PASS_BAND_HI = 1.89          # upper edge (PDG 1.8894 context)         # (local)
INFO_CENTER = 4.0 / 3.0      # fundamental (k,0) tower target          # (local)
INFO_HALFWIDTH = 0.05        # plan: INFO at 1.333 +- 0.05             # (local)
FAIL_GENERIC_ONSET = 2.5     # plan: FAIL at >= 2.5 (generic ~3.0)     # (local)

# Pre-registered regime / cross-check tolerances
GLO_COND_TOL = 1e-6          # |g_lo| conditioning floor (BREAKDOWN below)  # (local)
RECON_TOL = 1e-12            # reconstruction cross-check tolerance         # (local)
PDG_TOL = 1e-9               # publication-precision-tolerant default       # (local)

# The two towers (plan-pinned)
TOWER = [(1, 0), (1, 1), (3, 0)]       # triality tower (gate target)
FUND_TOWER = [(1, 0), (2, 0), (3, 0)]  # fundamental (k,0) alternative (INFO)

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # plan-freeze pin
ITEM6_NPZ = SESSION_DIR / "s100a_yukawa_overlap_offdiag.npz"

OUT_NPZ = SESSION_DIR / "s100a_casimir_widening.npz"
OUT_PNG = SESSION_DIR / "s100a_casimir_widening.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
    ITEM6_NPZ,
]

MACHINERY_PIN_MAP = {                                               # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-100a-w2-workingpaper.md#W2-3",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "N_eval": "3 tower sectors (1,0),(1,1),(3,0) -> 2 log-gaps -> 1 widening ratio",
    "L_max": "12",
    "scan_range": "N/A -- fixed tower, fixed tau_fold",
    "step_size": "N/A -- discrete",
    "tolerance": ("Casimir anchor exact (9/5); integral-W PASS band [1.80, 1.89]; "
                  "INFO at 1.333 +- 0.05; FAIL at >= 2.5"),
    "random_seed": "N/A -- deterministic",
    "GPU_path": "numpy.linalg (inherits Item-6 sector arrays; CPU adequate, OMP-capped 8)",
    "publication_precision": "6 sig figs (widening cited downstream in SS IV layer-separation ledger)",
    "spectrum_cache_sha": CACHE_SHA_PIN,
}


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA; Item-6-consistent)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict, item6_sha: str) -> tuple:
    """audit_sha256 = sha256(script || canonical || pinmap_json || item6_npz_sha);
    content_sha256 = sha256(script). Pinmap embeds per-gate identity keys
    (_gate_id/_scheme/...) so audit_sha256 is gate-unique. The Item-6 npz SHA
    is the 4th audit ingredient per the plan audit_discriminators block
    (["script", "canonical", "pinmap", "item6_npz_sha"])."""
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    full_pinmap = dict(pins)                                        # (local)
    full_pinmap.update(MACHINERY_PIN_MAP)
    pinmap_json = json.dumps(dict(sorted(full_pinmap.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(item6_sha.encode("ascii"))
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Exact SU(3) Casimir algebra (integer/Fraction arithmetic;
#              independent in-script engine, Sage-QQ cross-checked agent-side)
# ---------------------------------------------------------------------------

def C2_frac(p: int, q: int) -> Fr:
    """SU(3) quadratic Casimir, exact: C2(p,q) = (p^2+q^2+pq+3p+3q)/3."""
    return Fr(p * p + q * q + p * q + 3 * p + 3 * q, 3)


def dim_pq(p: int, q: int) -> int:
    """dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def triality(p: int, q: int) -> int:
    """t(p,q) = (p-q) mod 3."""
    return (p - q) % 3


# ---------------------------------------------------------------------------
# Section 6 -- Compute
# ---------------------------------------------------------------------------

def compute(pins: dict) -> dict:
    z = np.load(ITEM6_NPZ)                                          # (local)

    # ---- (1) Exact anchors: tower confirmation -----------------------------
    C2_tower = [C2_frac(p, q) for (p, q) in TOWER]                  # (local)
    g_lo_cas = C2_tower[1] - C2_tower[0]                            # (local) 5/3
    g_hi_cas = C2_tower[2] - C2_tower[1]                            # (local) 3
    W_cas = g_hi_cas / g_lo_cas                                     # (local) 9/5
    dims = [dim_pq(p, q) for (p, q) in TOWER]                       # (local)
    trial = [triality(p, q) for (p, q) in TOWER]                    # (local)

    C2_fund = [C2_frac(p, q) for (p, q) in FUND_TOWER]              # (local)
    W_fund = (C2_fund[2] - C2_fund[1]) / (C2_fund[1] - C2_fund[0])  # (local) 4/3

    assert C2_tower == [Fr(4, 3), Fr(3), Fr(6)], "C2 tower mismatch"
    assert (g_lo_cas, g_hi_cas) == (Fr(5, 3), Fr(3)), "Casimir gaps mismatch"
    assert W_cas == Fr(9, 5), "Casimir anchor != 9/5"
    assert C2_fund[1] == Fr(10, 3) and W_fund == Fr(4, 3), "fundamental tower mismatch"
    assert dims == [3, 8, 10], "dims mismatch"

    # vs Item-6 stored exact ints
    npz_pq = z["tower_pq"]                                          # (local)
    assert [tuple(r) for r in npz_pq] == TOWER, "tower_pq mismatch vs Item-6"
    npz_num = list(z["tower_C2_num"])                               # (local)
    npz_den = list(z["tower_C2_den"])                               # (local)
    exact_nd = [(f.numerator, f.denominator) for f in C2_tower]     # (local)
    assert exact_nd == list(zip(npz_num, npz_den)), "tower C2 num/den mismatch vs Item-6"
    assert int(z["W_casimir_num"]) == 9 and int(z["W_casimir_den"]) == 5, \
        "Item-6 W_casimir num/den != 9/5"
    assert list(z["dims"]) == dims, "Item-6 dims mismatch"

    print("(1) tower confirmed: (1,0)/(1,1)/(3,0)  C2 = (4/3, 3, 6) exact;")
    print(f"    dims = {dims} (fund/adjoint/decuplet), trialities = {trial}")
    print(f"    Casimir gaps: g_lo^cas = 5/3, g_hi^cas = 3, W_cas = 9/5 = {float(W_cas):.6f}")
    print(f"    fundamental-tower alternative: C2(2,0) = 10/3, W_fund = 4/3 = {float(W_fund):.6f}")

    # ---- (2) The gate quantity: W from the Item-6 diagonal overlaps --------
    O_g = np.asarray(z["O_g"], dtype=float)                         # (local)
    d_npz = np.asarray(z["d_i"], dtype=float)                       # (local)
    d_recon = O_g / O_g.max()                                       # (local)
    dev_d = float(np.max(np.abs(d_recon - d_npz)))                  # (local)

    g_lo = log(d_npz[1] / d_npz[0])                                 # (local)
    g_hi = log(d_npz[2] / d_npz[1])                                 # (local)
    W = g_hi / g_lo                                                 # (local)  THE gate value

    dev_glo = abs(g_lo - float(z["g_lo"]))                          # (local)
    dev_ghi = abs(g_hi - float(z["g_hi"]))                          # (local)
    dev_W = abs(W - float(z["widening_W"]))                         # (local)
    monotone = bool(d_npz[0] > d_npz[1] > d_npz[2])                 # (local)

    print()
    print("(2) integral-derived widening (Item-6 |s(h)|^2-weighted overlap diagonal):")
    print(f"    d_i = [{d_npz[0]:.6f}, {d_npz[1]:.6f}, {d_npz[2]:.6f}]  "
          f"on (1,0)/(1,1)/(3,0)   [recon from O_g: max dev {dev_d:.2e}]")
    print(f"    g_lo = ln(d_(1,1)/d_(1,0)) = ln({d_npz[1]:.6f}/{d_npz[0]:.6f}) = {g_lo:+.6f}")
    print(f"    g_hi = ln(d_(3,0)/d_(1,1)) = ln({d_npz[2]:.6f}/{d_npz[1]:.6f}) = {g_hi:+.6f}")
    print(f"    W = g_hi/g_lo = {g_hi:+.6f}/{g_lo:+.6f} = {W:+.6f}")
    print(f"    [vs Item-6 npz: dev(g_lo)={dev_glo:.2e}, dev(g_hi)={dev_ghi:.2e}, dev(W)={dev_W:.2e}]")
    print(f"    monotone Casimir ladder (d_(1,0)>d_(1,1)>d_(3,0))? {monotone}"
          f"   [d_(1,1) is the MAXIMUM -> ladder sign-inverted on first rung]")

    # ---- substitution chain, substituted ------------------------------------
    print()
    print("Substitution chain (realised numbers):")
    print(f"  Step 1-2: C2 = (4/3, 3, 6) exact on (1,0)/(1,1)/(3,0)")
    print(f"  Step 3:   g_lo = {g_lo:+.6f}, g_hi = {g_hi:+.6f}   [defs 3]")
    print(f"  Step 4:   W = {W:+.6f}   [def 4]")
    print(f"  Step 5:   predicted W_cas = +9/5 = +1.800000 (positive, PASS band)")
    print(f"            computed  W     = {W:+.6f}  -> sign({W:+.3f}) != sign(+1.8)"
          if W <= 0 else
          f"            computed  W     = {W:+.6f}  -> sign matches +9/5")

    # ---- (3) per-sector floor consistency + block structure ----------------
    floors = np.asarray(z["floors_lambda_min"], dtype=float)        # (local)
    mu_H = float(z["mu_H"])                                         # (local)
    ev = {"00": np.asarray(z["evals_00"], dtype=float),
          "10": np.asarray(z["evals_10"], dtype=float),
          "11": np.asarray(z["evals_11"], dtype=float),
          "30": np.asarray(z["evals_30"], dtype=float)}             # (local)
    floor_dev = max(abs(ev["10"].min() - floors[0]),
                    abs(ev["11"].min() - floors[1]),
                    abs(ev["30"].min() - floors[2]))                # (local)
    mu_dev = abs(ev["00"].min() - mu_H)                             # (local)
    block_counts_ok = (len(ev["00"]) == 16 and
                       [len(ev["10"]), len(ev["11"]), len(ev["30"])] ==
                       [16 * d for d in dims])                      # (local)
    print()
    print("(3) per-sector floors + Peter-Weyl block structure (D_K block-diagonal):")
    print(f"    lambda_min = [{floors[0]:.6f}, {floors[1]:.6f}, {floors[2]:.6f}],"
          f"  mu_H(0,0) = {mu_H:.6f}")
    print(f"    floor consistency dev = {floor_dev:.2e}; mu_H dev = {mu_dev:.2e}; "
          f"block counts 16*dim ok = {block_counts_ok}")

    # ---- (4) WHERE the Casimir grading breaks: lambda^2 vs C2 linearity ----
    lam2 = floors ** 2                                              # (local)
    slope_lo = (lam2[1] - lam2[0]) / float(g_lo_cas)                # (local)
    slope_hi = (lam2[2] - lam2[1]) / float(g_hi_cas)                # (local)
    slope_ratio = slope_hi / slope_lo                               # (local)
    W_floor = float(z["W_floor_only"])                              # (local)
    W_floor_recon = (lam2[2] - lam2[1]) / (lam2[1] - lam2[0])       # (local)
    dev_wfloor = abs(W_floor_recon - W_floor)                       # (local)
    print()
    print("(4) floor-route linearity check (bi-invariant metric would give lambda^2")
    print("    linear in C2 -> W_floor = 9/5 exactly; Jensen deformation at tau_fold")
    print(f"    = {float(tau_fold):.2f} breaks it):")
    print(f"    lambda^2 floors = [{lam2[0]:.6f}, {lam2[1]:.6f}, {lam2[2]:.6f}]")
    print(f"    chord slopes d(lambda^2)/d(C2): lo = {slope_lo:.6f}, hi = {slope_hi:.6f}; "
          f"ratio = {slope_ratio:.6f}  (Casimir-linear would be 1.0)")
    print(f"    W_floor_only = {W_floor_recon:.6f} = (9/5)*slope_ratio "
          f"[vs Item-6 {W_floor:.6f}, dev {dev_wfloor:.2e}]")

    # ---- (5) diagnostics + external cross-checks ---------------------------
    W_permode = float(z["W_permode"])                               # (local)
    pdg_lngap_recon = log(float(m_mu) / float(m_e))                 # (local)
    pdg_dev = abs(pdg_lngap_recon - float(z["pdg_lngap_mu_e"]))     # (local)
    tau_ok = abs(float(z["tau_fold_used"]) - float(tau_fold)) < RECON_TOL  # (local)
    rx_dev = abs(float(z["r_cross_canonical"]) - float(R_cross_yukawa_t1_t2))  # (local)

    cache_rel = str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    cache_sha_disk = pins[cache_rel]                                # (local)
    cache_sha_npz = str(z["spectrum_cache_sha"])                    # (local)
    cache_triple_ok = (cache_sha_disk == CACHE_SHA_PIN == cache_sha_npz)  # (local)

    print()
    print("(5) diagnostics + cross-checks:")
    print(f"    W_permode (Gaussian per-mode sum, no channel weight) = {W_permode:.6f}"
          f"  [{100.0 * (W_permode / float(W_cas) - 1.0):+.2f}% vs 9/5; NOT gating]")
    print(f"    W_floor_only (floor-only Gaussian)                   = {W_floor:.6f}")
    print(f"    PDG ln(m_mu/m_e) recomputed from canonical = {pdg_lngap_recon:.6f} "
          f"[dev vs Item-6 {pdg_dev:.2e}]")
    print(f"    tau_fold_used == tau_fold canonical ({float(tau_fold):.2f}): {tau_ok}")
    print(f"    R_cross canonical consistency dev = {rx_dev:.2e}")
    print(f"    spectrum-cache SHA triple-match (disk == plan pin == Item-6 npz): "
          f"{cache_triple_ok}")

    recon_all_ok = (dev_d < RECON_TOL and dev_glo < RECON_TOL and
                    dev_ghi < RECON_TOL and dev_W < RECON_TOL and
                    floor_dev < RECON_TOL and mu_dev < RECON_TOL and
                    dev_wfloor < RECON_TOL and pdg_dev < PDG_TOL and
                    tau_ok and rx_dev < PDG_TOL and block_counts_ok)  # (local)

    return {
        "W": W, "g_lo": g_lo, "g_hi": g_hi, "d": d_npz, "O_g": O_g,
        "monotone": monotone,
        "W_cas": W_cas, "g_lo_cas": g_lo_cas, "g_hi_cas": g_hi_cas,
        "W_fund": W_fund, "C2_tower": C2_tower, "C2_fund": C2_fund,
        "dims": dims, "trialities": trial,
        "floors": floors, "lam2": lam2, "mu_H": mu_H,
        "slope_lo": slope_lo, "slope_hi": slope_hi, "slope_ratio": slope_ratio,
        "W_floor": W_floor, "W_permode": W_permode,
        "pdg_lngap": pdg_lngap_recon, "pdg_dev": pdg_dev,
        "dev_d": dev_d, "dev_glo": dev_glo, "dev_ghi": dev_ghi, "dev_W": dev_W,
        "floor_dev": floor_dev, "mu_dev": mu_dev, "dev_wfloor": dev_wfloor,
        "rx_dev": rx_dev, "tau_ok": tau_ok,
        "cache_triple_ok": cache_triple_ok, "recon_all_ok": recon_all_ok,
        "item6_verdict": str(z["verdict"]), "item6_W": float(z["widening_W"]),
    }


# ---------------------------------------------------------------------------
# Section 7 -- Gate evaluation (pre-registered; [SIGN] 3-tuple + pinned
#              composite-collapse rule from gate-verdicts.md)
# ---------------------------------------------------------------------------

def evaluate_gate(r: dict) -> tuple:
    W = r["W"]                                                      # (local)

    # sign_verdict: substitution-chain direction is W_cas = +9/5 > 0
    sign_v = "PASS" if W > 0 else "FAIL"                            # (local)

    # magnitude_verdict: pre-registered band membership
    if PASS_BAND_LO <= W <= PASS_BAND_HI:
        mag_v = "PASS"                                              # (local)
    elif abs(W - INFO_CENTER) <= INFO_HALFWIDTH:
        mag_v = "INFO"                                              # (local)
    else:
        mag_v = "FAIL"                                              # (local)

    # regime_verdict: machinery in-regime?
    #   BREAKDOWN: log/ratio undefined or ill-conditioned
    #   MARGINAL : value computable but provenance/consistency impaired
    #   VALID    : all integrity checks pass
    if (not np.all(r["d"] > 0.0)) or abs(r["g_lo"]) <= GLO_COND_TOL:
        regime_v = "BREAKDOWN"                                      # (local)
    elif (not r["cache_triple_ok"]) or (not r["recon_all_ok"]):
        regime_v = "MARGINAL"                                       # (local)
    else:
        regime_v = "VALID"                                          # (local)

    # composite collapse (gate-verdicts.md, PRE-REGISTERED rule)
    if regime_v == "BREAKDOWN":
        composite = "FAIL"                                          # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"                                          # (local)
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"                                          # (local)
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"                                          # (local)
    elif mag_v == "INFO":
        composite = "INFO"                                          # (local)
    else:
        composite = "PASS"                                          # (local)

    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 8 -- Plot + npz
# ---------------------------------------------------------------------------

def make_plot(r: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.2))             # (local)
    C2f = [float(c) for c in r["C2_tower"]]                         # (local)
    labels = ["(1,0)", "(1,1)", "(3,0)"]                            # (local)

    # Panel A: ln d_i vs C2 (the gate ladder)
    ax = axes[0]                                                    # (local)
    lnd = np.log(r["d"])                                            # (local)
    ax.plot(C2f, lnd, "o-", color="crimson", lw=2, ms=9, label="ln d_i (Item-6 overlap diag)")
    A = np.vstack([np.ones(3), np.asarray(C2f)]).T                  # (local)
    coef, *_ = np.linalg.lstsq(A, lnd, rcond=None)                  # (local)
    xx = np.linspace(1.0, 6.3, 50)                                  # (local)
    ax.plot(xx, coef[0] + coef[1] * xx, "--", color="gray", lw=1.5,
            label=f"Casimir-linear LSQ (slope {coef[1]:+.3f})")
    for x, y, lab in zip(C2f, lnd, labels):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(8, 6), fontsize=10)
    ax.set_xlabel("C2(p,q)")
    ax.set_ylabel("ln d_i")
    ax.set_title("A: overlap-diagonal ladder vs C2\n(d_(1,1) is MAX -> sign-inverted rung)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: lambda_min^2 floors vs C2 (where Casimir-linearity breaks)
    ax = axes[1]                                                    # (local)
    ax.plot(C2f, r["lam2"], "s-", color="navy", lw=2, ms=8, label="lambda_min^2 (L=12 cache)")
    lin = r["lam2"][0] + (np.asarray(C2f) - C2f[0]) * r["slope_lo"]  # (local)
    ax.plot(C2f, lin, ":", color="darkorange", lw=2,
            label="Casimir-linear continuation (slope_lo)")
    for x, y, lab in zip(C2f, r["lam2"], labels):
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=(8, -12), fontsize=10)
    ax.set_xlabel("C2(p,q)")
    ax.set_ylabel("lambda_min^2  [M_KK^2]")
    ax.set_title(f"B: spectral floors at tau_fold={float(tau_fold):.2f}\n"
                 f"slope ratio hi/lo = {r['slope_ratio']:.3f} (bi-invariant: 1.0)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: W candidates vs discriminator bands
    ax = axes[2]                                                    # (local)
    ax.axvspan(PASS_BAND_LO, PASS_BAND_HI, color="green", alpha=0.25,
               label="PASS [1.80, 1.89] (9/5 ladder)")
    ax.axvspan(INFO_CENTER - INFO_HALFWIDTH, INFO_CENTER + INFO_HALFWIDTH,
               color="goldenrod", alpha=0.30, label="INFO 4/3 +- 0.05 (fund. tower)")
    ax.axvspan(FAIL_GENERIC_ONSET, 13.6, color="red", alpha=0.12,
               label="FAIL >= 2.5 (generic)")
    cands = [("W (gate: overlap diag)", r["W"], "crimson", "*", 290),
             ("W_permode (diagnostic)", r["W_permode"], "navy", "o", 90),
             ("W_floor_only (diagnostic)", r["W_floor"], "purple", "o", 90),
             ("W_cas = 9/5 exact", float(r["W_cas"]), "green", "D", 90),
             ("W_fund = 4/3 exact", float(r["W_fund"]), "goldenrod", "D", 90),
             ("W_generic ~ 3.0", 3.0, "red", "v", 90)]              # (local)
    for i, (lab, x, c, m, s) in enumerate(cands):
        ax.scatter([x], [len(cands) - i], c=c, marker=m, s=s, zorder=5)
        ax.annotate(f"{lab}: {x:+.4f}", (x, len(cands) - i),
                    textcoords="offset points", xytext=(0, 10), fontsize=8, ha="center")
    ax.axvline(0.0, color="k", lw=0.8)
    ax.set_xlim(-5.6, 13.6)
    ax.set_ylim(0.2, len(cands) + 1.2)
    ax.set_yticks([])
    ax.set_xlabel("widening W = g_hi / g_lo")
    ax.set_title(f"C: discriminator bands -> composite {verdict}\n"
                 f"W = {r['W']:+.6f} outside ALL bands (sign-inverted)")
    ax.legend(fontsize=7, loc="lower right")
    ax.grid(alpha=0.3, axis="x")

    fig.suptitle(f"{GATE_ID}: envelope widening vs consecutive-Casimir-gap ratio 9/5 "
                 f"on (1,0)/(1,1)/(3,0)  [tau_fold={float(tau_fold):.2f}, L_max=12]",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"plot -> {OUT_PNG.name}")


def save_npz(r: dict, verdict: str, tup: tuple, audit_sha: str,
             content_sha: str) -> None:
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        l_max=int(L_MAX), schema_version="S84+",
        # gate quantity + route
        widening_W=r["W"], g_lo=r["g_lo"], g_hi=r["g_hi"],
        d_i=r["d"], O_g=r["O_g"], monotone_ladder=r["monotone"],
        # exact anchors (num/den int pairs)
        W_casimir_num=9, W_casimir_den=5,
        W_fund_num=4, W_fund_den=3,
        g_lo_cas_num=5, g_lo_cas_den=3, g_hi_cas_num=3, g_hi_cas_den=1,
        tower_pq=np.array(TOWER), fund_tower_pq=np.array(FUND_TOWER),
        tower_C2_num=np.array([c.numerator for c in r["C2_tower"]]),
        tower_C2_den=np.array([c.denominator for c in r["C2_tower"]]),
        fund_C2_num=np.array([c.numerator for c in r["C2_fund"]]),
        fund_C2_den=np.array([c.denominator for c in r["C2_fund"]]),
        dims=np.array(r["dims"]), trialities=np.array(r["trialities"]),
        # bands (pre-registered)
        pass_band=np.array([PASS_BAND_LO, PASS_BAND_HI]),
        info_center=INFO_CENTER, info_halfwidth=INFO_HALFWIDTH,
        fail_generic_onset=FAIL_GENERIC_ONSET,
        # floors + linearity
        floors_lambda_min=r["floors"], lam2_floors=r["lam2"], mu_H=r["mu_H"],
        slope_lo=r["slope_lo"], slope_hi=r["slope_hi"], slope_ratio=r["slope_ratio"],
        W_floor_only=r["W_floor"], W_permode=r["W_permode"],
        # cross-checks
        dev_d_recon=r["dev_d"], dev_g_lo=r["dev_glo"], dev_g_hi=r["dev_ghi"],
        dev_W=r["dev_W"], floor_dev=r["floor_dev"], mu_dev=r["mu_dev"],
        dev_wfloor=r["dev_wfloor"], pdg_lngap_mu_e=r["pdg_lngap"],
        pdg_dev=r["pdg_dev"], rx_dev=r["rx_dev"], tau_ok=r["tau_ok"],
        cache_triple_ok=r["cache_triple_ok"], recon_all_ok=r["recon_all_ok"],
        item6_verdict=r["item6_verdict"], item6_W=r["item6_W"],
        tau_fold_used=float(tau_fold),
        # verdicts + SHAs
        verdict=verdict, sign_verdict=tup[0], magnitude_verdict=tup[1],
        regime_verdict=tup[2],
        spectrum_cache_sha=CACHE_SHA_PIN,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"data -> {OUT_NPZ.name}")


# ---------------------------------------------------------------------------
# Section 9 -- Verdict payload + main
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note: str = "",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission; the script does
    NOT write the verdict file). Session is the letter-suffixed string 100a."""
    payload = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }                                                               # (local)
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


def main() -> int:
    t0 = time.time()                                                # (local)
    pins = log_input_pins(INPUT_FILES)                              # (local)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"          # (local)
    item6_rel = str(ITEM6_NPZ.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, canonical_path, pins, pins[item6_rel])
    print(f"  audit_sha256:   {audit_sha} (script+canonical+pinmap+item6_npz_sha)")
    print(f"  content_sha256: {content_sha} (script only)")
    print()

    r = compute(pins)                                               # (local)
    verdict, sign_v, mag_v, regime_v = evaluate_gate(r)             # (local)

    print()
    print(f"Bands: PASS [{PASS_BAND_LO}, {PASS_BAND_HI}] | "
          f"INFO {INFO_CENTER:.4f} +- {INFO_HALFWIDTH} | FAIL >= {FAIL_GENERIC_ONSET}")
    print(f"3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v} "
          f"-> composite {verdict}")

    value = (f"W={r['W']:+.6f}_OUTSIDE-ALL-BANDS{{PASS[1.80,1.89],"
             f"INFO1.333+-0.05,FAILgeq2.5}};g_lo={r['g_lo']:+.6f};"
             f"g_hi={r['g_hi']:+.6f};ladder-SIGN-INVERTED_d11=max_nonmono;"
             f"d=[{r['d'][0]:.6f},{r['d'][1]:.6f},{r['d'][2]:.6f}];"
             f"W_cas=9/5=1.800000exact;W_fund=4/3exact;"
             f"W_permode={r['W_permode']:.6f}_diag;"
             f"W_floor={r['W_floor']:.6f}_diag;"
             f"slope_ratio_lam2_vs_C2={r['slope_ratio']:.6f};"
             f"NOT-generic-3.0;item6_repro_dev={r['dev_W']:.1e}")   # (local)

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, regime_v), audit_sha, content_sha)

    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note=("adjudicates the W2->W3 INFO row from Item 6 "
                        "(S100a-YUKAWA-OVERLAP-OFFDIAG INFO): widening on the "
                        "plan-pinned overlap-diagonal route; Sage-QQ + Fraction "
                        "exact anchors W_cas=9/5, W_fund=4/3, C2=(4/3,3,6); "
                        f"d_i/g/W reproduce Item-6 npz to {r['dev_W']:.1e}"),
        extra_rows=[
            (f"# bands(plan-frozen): PASS=[1.80,1.89] centred 9/5 triality tower "
             f"(1,0)/(1,1)/(3,0) C2=(4/3,3,6); INFO=4/3+-0.05 fundamental (k,0) "
             f"tower C2(2,0)=10/3; FAIL>=2.5 generic ~3.0 # {GATE_ID}"),
            (f"# structural: realised W={r['W']:+.6f} matches NONE of the three "
             f"discriminators -- ladder SIGN-INVERTED (adjoint (1,1) overlap-"
             f"enhanced, d=1.0 max); floors lam^2 NOT Casimir-linear at tau_fold "
             f"(slope_hi/slope_lo={r['slope_ratio']:.4f} vs bi-invariant 1.0); "
             f"per-mode Gaussian diagnostic W_permode={r['W_permode']:.4f} lands "
             f"{100.0 * (r['W_permode'] / 1.8 - 1.0):+.2f}pct below 9/5 (non-gating) "
             f"# {GATE_ID}"),
        ],
    )

    print(f"\n=== {GATE_ID}: {verdict} (sign={sign_v} magnitude={mag_v} "
          f"regime={regime_v}; wall {time.time() - t0:.1f}s) ===")
    return 0   # exit 0 on script success regardless of scientific verdict


if __name__ == "__main__":
    sys.exit(main())
