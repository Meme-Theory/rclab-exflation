#!/usr/bin/env python3
"""
S100a W4-12 -- S100a-M0-FUNCTIONAL-SENSITIVITY
==============================================

Gate: S100a-M0-FUNCTIONAL-SENSITIVITY ([SIGN])
Classification: GEOMETRIC
Agent: lizzi-spectral-functional-theorist

DUAL-scheme functional-sensitivity test: the per-sector overall SCALE
M0^{sector} (and the m_H channel) MOVES between the cutoff action
Tr f(D_K^2/Lambda^2) and the zeta action S_zeta = zeta_{D_K}(0) = a_4^{zeta},
while the fermion mass RATIOS r_ij from |s(h)|^2-weighted eigenvalue overlaps
are bit-identical across the two schemes -- the empirical face of the
Spectral-Moment Decoupling Theorem (S75 W2-E, PERMANENT: a_0, a_2, a_4
algebraically independent, Wronskian nonzero).

Pre-registered thresholds (plan session-100a-plan-w4.md SS W4-12):
  PASS-side (RATIO invariance):
      max_ij |r_ij^{zeta} - r_ij^{cutoff}| / |r_ij^{zeta}| <= ratio_tol = 1e-12
  FAIL: ratio deviation > info_band = 1e-9 (falsifies decoupling)
  INFO band (1e-12, 1e-9]: sub-machine-epsilon kernel-scale leak flag
  INFO content (reported, NOT gated):
      D_scale = |M0^{cutoff} - M0^{zeta}| / M0^{zeta}  (the SCALE moves)
  Composite: INFO-BY-DESIGN whenever the SCALE characterization is the
  primary deliverable and the RATIO assertion is not FAIL (plan INFO_meaning).

DUAL LEVEL-PIN (substrate-first-canonical-sourcing.md SS(iv), MANDATORY K=4):
  ZETA LEG   = FULL physical. Bosonic scale moment-ratio a_4^{zeta}/a_2^{zeta}
               from the canonical zeta-regulated Seeley-DeWitt coefficients
               (a_4_FW_zeta = 1350.7216, a_2_FW_zeta = 2776.165389,
               a_0_FW_zeta = 6440.0; npz-sourced canonical, S88
               A-N-FW-CANONICALIZATION). Substrate-first; NO SCHEMATIC helper.
  CUTOFF LEG = SCHEMATIC. Tr f(D_K^2/Lambda^2) via (i) the Chamseddine-Connes
               1996 SS2.2-2.3 cutoff-function Mellin moments f_2, f_4 of f*
               restricted to [0, inf) -- canonical pins mellin_f_star_f2 =
               214.97335676 / mellin_f_star_f4 = 6446.63942272 at X_MAX=50
               (S78 W2-D), re-derived in-script by closed form + quadrature --
               AND (ii) the SCHEMATIC helper _spectral_action_regulators.py
               (hard_cutoff_a_n vs zeta_a_n; helper self-identifies SCHEMATIC
               per its docstring lines 23-30, verified S88 W7b-83).
  The verdict-line convention carries the pre-registered -SCHEMATIC suffix
  (RATIO-INVARIANCE-vs-SCALE-DEPENDENCE-LAYER-PINNED-SCHEMATIC) and the
  emit_verdict extra_rows carry the `# tier_pin=TIER-2` companion row.

SUBSTITUTION CHAIN (plan SS W4-12 item 7; [SIGN] trigger -- both claims):
  Claim A (INFO): "the bosonic SCALE M0 MOVES between schemes (D_scale != 0)."
    Step 1: M0^{sector} := (bosonic-scale moment ratio) x (per-sector |s(h)|^2
            envelope O_g)                                    [plan Definition 1]
    Step 2: scale_zeta   = a_4^{zeta}/a_2^{zeta}             [Definition 3]
            scale_cutoff = f_4/f_2 (Mellin moments of f*)    [Definition 4]
    Step 3: substitute  -> 1350.7216/2776.165389  vs  6446.63942272/214.97335676
    Step 4: simplify    -> 0.486542...            vs  29.98809...
            ratio of moment-ratios = 61.635 (native normalizations; the SAME
            per-branch Vol-normalization applies to both leg's M0, so the
            common envelope cancels in D_scale and the raw factor magnitude is
            a normalization artifact -- the PHYSICAL content is D_scale > 0).
    Step 5: direction   -> D_scale > 0 strictly => SIGN of Delta(M0) != 0.
  Claim B (PASS-side): "the fermion mass RATIOS do NOT move between schemes."
    Step 1: O_g = sum_{lambda in sector g} exp(-lambda^2/mu_H^2) with the
            exact-Haar unit-normalized |s(h)|^2 kernel mean (<|s_hat|^2> = 1,
            Item-6 P1/P2 construction); O_g depends ONLY on the D_K spectrum
            + kernel, NOT on any a_n moment                  [Definition 2]
    Step 2: r_ij^{scheme} = M_i^{scheme}/M_j^{scheme}
                          = (scale_scheme x O_i)/(scale_scheme x O_j)
    Step 3: substitute   -> r_ij^{zeta} = O_i/O_j ; r_ij^{cutoff} = O_i/O_j
    Step 4: simplify     -> r_ij^{zeta} - r_ij^{cutoff} = 0 exactly (exact
            arithmetic); <= 1e-12 in float64 (round-off only).
    Step 5: direction    -> ratio deviation = 0 => sign_verdict = PASS.
  Cross-check: R_1 = a_0^{zeta} a_4^{zeta}/(a_2^{zeta})^2 = 1.1286546
               (canonical R1_lizzi = 1.128655 at 7 sf) -- moment pins correct.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py        (audit_sha leg)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (plan input 2)
  - computations/_shared/_spectral_action_regulators.py (plan input 3, SCHEMATIC)
  - computations/session-100a/s100a_yukawa_overlap_offdiag.npz (4th pinned
    input, OPERATIONAL ENRICHMENT: Item-6 O_g reproduction cross-check ONLY;
    primary O_g is recomputed from the s84 cache. Plan input_files listed 3;
    honest disclosure per math-scripts.md plan-authorship item 4.)

Output 4-tuple:
  (value=<payload>, scheme=DUAL-ZETA-VS-CUTOFF-FSTAR,
   convention=RATIO-INVARIANCE-vs-SCALE-DEPENDENCE-LAYER-PINNED-SCHEMATIC,
   L_max=12)

DISCIPLINE
----------
- from canonical_constants import *   (no hardcoded framework constants)
- every intermediate tagged # (local)
- CPU-cap-OMP8 BEFORE numpy import (machinery pin GPU_path; arrays < 100x100)
- verdict emitted via the emit_verdict knowledge-MCP tool: this script PRINTS
  the payload (print_verdict_payload) and does NOT write the verdict file.
- exit 0 regardless of scientific verdict (math-scripts.md exit-code rule).
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (machinery pin: CPU-cap-OMP8) ---
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
from canonical_constants import *  # noqa: F401,F403
# pulls: a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta, mellin_f_star_f0,
#        mellin_f_star_f2, mellin_f_star_f4, R1_lizzi, R_cross_yukawa_t1_t2,
#        Vol_SU3_Haar, tau_fold, a0_fold, a2_fold, a4_fold

# SCHEMATIC helper (cutoff leg; self-identifies SCHEMATIC, docstring L23-30)
from _spectral_action_regulators import zeta_a_n, hard_cutoff_a_n  # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from math import exp, sqrt

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import quad

# ---------------------------------------------------------------------------
# Section 3 -- Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "100a"                                                    # (local)
GATE_ID = "S100a-M0-FUNCTIONAL-SENSITIVITY"                         # (local)
SCHEME = "DUAL-ZETA-VS-CUTOFF-FSTAR"                                # (local)
CONVENTION = ("RATIO-INVARIANCE-vs-SCALE-DEPENDENCE"
              "-LAYER-PINNED-SCHEMATIC")                            # (local)
L_MAX = "12"                                                        # (local)

# Pre-registered thresholds (plan SS W4-12 operator / machinery pin)
RATIO_TOL = 1e-12        # (local) strict PASS boundary (RATIO bit-identity)
INFO_BAND = 1e-9         # (local) RATIO drift INFO ceiling; > => FAIL
X_MAX = 50.0             # (local) X_MAX=50 regulator per mellin_f_star_f2/f4
#                          PROVENANCE (S78 W2-D, s78_f_conv_anomaly.npz)
CUTOFF_FRAC = 0.7        # (local) hard_cutoff_a_n helper default (plan cites
#                          the helper's hard_cutoff_a_n as pinned)
F_MOM_XCHECK_TOL = 1e-6  # (local) f-moment closed-form vs canonical pin
R1_XCHECK_TOL = 1e-6     # (local) R1_lizzi published at 7 sf (Class 8.3)
O_G_REPRO_TOL = 1e-12    # (local) Item-6 O_g reproduction consistency
R_CROSS_TOL = 1e-5       # (local) S97 floor-ratio wall reproduction (Item-6 pin)
LEAK_CONTROL_EPS = 1e-6  # (local) sensitivity-control kernel perturbation

TOWER = [(1, 0), (1, 1), (3, 0)]   # triality-distinct generation tower (plan)
HIGGS_SECTOR = (0, 0)              # fiber-singlet m_H channel (Item-6 P2 pin)
PAIRS = [(0, 1), (0, 2), (1, 2)]   # ratio index pairs over TOWER

CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # plan-freeze pin (Item-6 verified)
HELPER_PATH = SHARED_DIR / "_spectral_action_regulators.py"
ITEM6_NPZ = SESSION_DIR / "s100a_yukawa_overlap_offdiag.npz"

OUT_NPZ = SESSION_DIR / "s100a_m0_functional_sensitivity.npz"
OUT_PNG = SESSION_DIR / "s100a_m0_functional_sensitivity.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_PATH,
    HELPER_PATH,
    ITEM6_NPZ,    # operational enrichment: O_g reproduction cross-check ONLY
]

MACHINERY_PIN_MAP = {                                               # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "session-100a-w4-workingpaper.md#W4-12",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "N_eval": ("all bottom-sector overlaps at L_max=12, p+q<=4 "
               "triality-distinct tower (1,0)/(1,1)/(3,0)"),
    "L_max": "12",
    "scan_range": "N/A -- two-scheme point comparison (zeta vs cutoff)",
    "step_size": "N/A -- deterministic two-point comparison",
    "tolerance": "ratio_tol=1e-12 (PASS); info_band=1e-9 (INFO ceiling)",
    "scheme": "DUAL: zeta (S_zeta=zeta_{D_K}(0)=a_4^{zeta}) vs cutoff "
              "(Tr f(D_K^2/Lambda^2), f*-branch)",
    "convention": CONVENTION,
    "random_seed": "N/A -- deterministic",
    "GPU_path": "numpy.linalg (sub-100x100 sums -- CPU-cap-OMP8)",
    "regulator_pin": ("DUAL -- zeta leg a_0^{zeta}/a_2^{zeta}/a_4^{zeta} "
                      "(FULL canonical); cutoff leg a_2^{cutoff}=f_2 / "
                      "a_4^{cutoff}=f_4 (Mellin f-moments of f*, X_MAX=50); "
                      "bare a_n FORBIDDEN"),
    "CLASS": "SCHEMATIC (cutoff leg); FULL (zeta leg, level-pinned SEPARATELY)",
    "publication_precision": ("RATIO dev full float64 (npz) + 3 sf (WP); "
                              "D_scale 4 sf; downstream rel_tol >= 1e-12"),
    "spectrum_cache_sha": CACHE_SHA_PIN,
}


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """S84+ dual-SHA: audit = H(script||canonical||pinmap); content = H(script)."""
    script_bytes = script_path.read_bytes()                         # (local)
    canonical_bytes = canonical_path.read_bytes()                   # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")        # (local)
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Compute
# ---------------------------------------------------------------------------
def f_star(x: float) -> float:
    """f*(x) = (1 - f_0) sqrt(x) + f_0 exp(-x); f_0 = f*(0) = mellin_f_star_f0.

    The exp-branch weight IS the canonical f_0 Mellin moment (f_0 = f*(0));
    the sqrt-branch weight is its complement (S72/S78 f* functional).
    """
    return (1.0 - mellin_f_star_f0) * sqrt(x) + mellin_f_star_f0 * exp(-x)


def compute(pins: dict) -> dict:
    res: dict = {}                                                  # (local)

    # ---- (1) Load + verify spectrum cache (HARD SHA assert) ----
    cache_rel = str(CACHE_PATH.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
    assert pins[cache_rel] == CACHE_SHA_PIN, (
        f"spectrum cache SHA mismatch: {pins[cache_rel]} != {CACHE_SHA_PIN}")
    cache = np.load(CACHE_PATH, allow_pickle=True)                  # (local)
    se = cache["sector_evals"].item()                               # (local)
    print(f"\nSpectrum cache: {len(se)} sectors; SHA matches plan-freeze pin.")

    # ENVELOPE (scheme-independent by construction; Item-6 P1/P2 machinery):
    # mu_H = global Dirac floor = lambda_min(0,0); O_g = sum exp(-l^2/mu^2).
    global_floor = min(float(np.min(np.asarray(d["abs_evals"])))
                       for d in se.values())                        # (local)
    floor_00 = float(np.min(np.asarray(se[HIGGS_SECTOR]["abs_evals"])))  # (local)
    assert abs(global_floor - floor_00) < 1e-15, "P2 pin violated"
    mu2 = global_floor ** 2                                         # (local)
    print(f"  mu_H pin (P2): global floor = {global_floor:.9f} "
          f"== lambda_min(0,0); mu2 = {mu2:.9f}")

    sectors = {}                                                    # (local)
    blocks_complete = True                                          # (local)
    for pq in TOWER + [HIGGS_SECTOR]:
        d = se[pq]                                                  # (local)
        ev = np.sort(np.asarray(d["abs_evals"], dtype=np.float64))  # (local)
        ok = (ev.size == 16 * int(d["dim"]))                        # (local)
        blocks_complete = blocks_complete and ok
        sectors[pq] = ev
        print(f"  sector {pq}: dim={d['dim']} n_evals={ev.size} "
              f"(=16*dim: {ok}) lam_min={ev[0]:.6f}")
    assert blocks_complete, "cache block incomplete (n_evals != 16*dim)"

    # S97 wall reproduction (regime sanity; canonical R_cross_yukawa_t1_t2)
    r_cross_repro = float(sectors[(1, 0)][0]) / floor_00            # (local)
    r_cross_dev = abs(r_cross_repro - R_cross_yukawa_t1_t2)         # (local)
    print(f"  S97 cross-check: floor(1,0)/floor(0,0) = {r_cross_repro:.6f} "
          f"vs R_cross_yukawa_t1_t2 (|dev| = {r_cross_dev:.2e} < {R_CROSS_TOL})")
    assert r_cross_dev < R_CROSS_TOL, "S97 R_cross reproduction failed"

    O_arr = np.array([float(np.sum(np.exp(-(sectors[pq] ** 2) / mu2)))
                      for pq in TOWER])                             # (local)
    O_00 = float(np.sum(np.exp(-(sectors[HIGGS_SECTOR] ** 2) / mu2)))  # (local)
    print(f"\nEnvelope O_g (kernel <|s_hat|^2>_Haar = 1, Item-6 P1 block sums):")
    for k, pq in enumerate(TOWER):
        print(f"  O_{pq} = {O_arr[k]:.12f}")
    print(f"  O_(0,0) [m_H channel] = {O_00:.12f}")

    # Item-6 O_g reproduction cross-check (4th pinned input; enrichment)
    it6 = np.load(ITEM6_NPZ, allow_pickle=True)                     # (local)
    assert [tuple(t) for t in it6["tower_pq"].tolist()] == TOWER, \
        "Item-6 tower mismatch"
    O_it6 = np.asarray(it6["O_g"], dtype=np.float64)                # (local)
    o_repro_dev = float(np.max(np.abs(O_arr - O_it6) / O_it6))      # (local)
    assert str(it6["spectrum_cache_sha"]) == CACHE_SHA_PIN, \
        "Item-6 consumed a different spectrum cache"
    print(f"  Item-6 O_g reproduction: max rel dev = {o_repro_dev:.2e} "
          f"(< {O_G_REPRO_TOL}: {o_repro_dev < O_G_REPRO_TOL})")
    assert o_repro_dev < O_G_REPRO_TOL, "Item-6 O_g reproduction failed"

    # ---- (2) ZETA LEG (FULL physical; canonical npz-sourced a_n^{zeta}) ----
    scale_zeta = a_4_FW_zeta / a_2_FW_zeta                          # (local)
    R1_zeta = a_0_FW_zeta * a_4_FW_zeta / a_2_FW_zeta ** 2          # (local)
    R1_dev = abs(R1_zeta - R1_lizzi) / R1_lizzi                     # (local)
    # full-precision variant (a*_fold, same quantities at full float64)
    scale_zeta_fullprec = a4_fold / a2_fold                         # (local)
    scale_zeta_pubdev = abs(scale_zeta - scale_zeta_fullprec) / scale_zeta  # (local)
    print(f"\nZETA LEG (FULL): scale_zeta = a_4^{{zeta}}/a_2^{{zeta}} "
          f"= {a_4_FW_zeta}/{a_2_FW_zeta} = {scale_zeta:.9f}")
    print(f"  R_1^{{zeta}} = a_0 a_4/a_2^2 = {R1_zeta:.7f} vs R1_lizzi "
          f"= {R1_lizzi} (rel dev {R1_dev:.2e} < {R1_XCHECK_TOL}: "
          f"{R1_dev < R1_XCHECK_TOL})")
    print(f"  full-precision a4_fold/a2_fold cross-check: "
          f"{scale_zeta_fullprec:.12f} (pub-precision rel dev "
          f"{scale_zeta_pubdev:.1e})")
    assert R1_dev < R1_XCHECK_TOL, "R_1 protected-ratio cross-check failed"

    # ---- (3) CUTOFF LEG (SCHEMATIC; f* Mellin moments + helper) ----
    # Primary: canonical pins (plan Definition 4)
    scale_cutoff = mellin_f_star_f4 / mellin_f_star_f2              # (local)
    # closed-form re-derivation at X_MAX (w_sqrt = 1 - f_0; w_exp = f_0):
    w_exp = mellin_f_star_f0                                        # (local)
    w_sqrt = 1.0 - mellin_f_star_f0                                 # (local)
    f2_cf = (w_sqrt * (2.0 / 3.0) * X_MAX ** 1.5
             + w_exp * (1.0 - exp(-X_MAX)))                         # (local)
    f4_cf = (w_sqrt * (2.0 / 5.0) * X_MAX ** 2.5
             + w_exp * (1.0 - (X_MAX + 1.0) * exp(-X_MAX)))         # (local)
    f2_cf_dev = abs(f2_cf - mellin_f_star_f2) / mellin_f_star_f2    # (local)
    f4_cf_dev = abs(f4_cf - mellin_f_star_f4) / mellin_f_star_f4    # (local)
    # quadrature cross-check
    f2_q = quad(f_star, 0.0, X_MAX, limit=200)[0]                   # (local)
    f4_q = quad(lambda x: x * f_star(x), 0.0, X_MAX, limit=200)[0]  # (local)
    f2_q_dev = abs(f2_q - mellin_f_star_f2) / mellin_f_star_f2      # (local)
    f4_q_dev = abs(f4_q - mellin_f_star_f4) / mellin_f_star_f4      # (local)
    R1_cutoff_fmom = (mellin_f_star_f0 * mellin_f_star_f4
                      / mellin_f_star_f2 ** 2)                      # (local)
    print(f"\nCUTOFF LEG (SCHEMATIC): scale_cutoff = f_4/f_2 "
          f"= {mellin_f_star_f4}/{mellin_f_star_f2} = {scale_cutoff:.9f}")
    print(f"  closed-form at X_MAX={X_MAX:.0f}: f_2 = {f2_cf:.8f} "
          f"(rel dev {f2_cf_dev:.2e}), f_4 = {f4_cf:.8f} "
          f"(rel dev {f4_cf_dev:.2e})")
    print(f"  quadrature:                f_2 = {f2_q:.8f} "
          f"(rel dev {f2_q_dev:.2e}), f_4 = {f4_q:.8f} "
          f"(rel dev {f4_q_dev:.2e})")
    print(f"  R_1 f-moment combo: f_0 f_4/f_2^2 = {R1_cutoff_fmom:.7f} "
          f"(recorded; per-branch R-protection -- NOT a cross-scheme "
          f"conversion factor, R1_lizzi provenance note)")
    assert f2_cf_dev < F_MOM_XCHECK_TOL and f4_cf_dev < F_MOM_XCHECK_TOL, \
        "f* Mellin-moment closed-form cross-check failed (wrong f* form?)"

    # SCHEMATIC helper consumption (hard_cutoff_a_n vs zeta_a_n, L_max=12):
    # same schematic Casimir spectrum + same normalization on both helper
    # legs => the helper-internal a_4/a_2 shift is normalization-artifact-FREE
    # (the cleanest Claim-A direction confirmation).
    lmax_helper = int(L_MAX)                                        # (local)
    a0_hz = zeta_a_n(0, lmax_helper, Vol_SU3_Haar)                  # (local)
    a2_hz = zeta_a_n(1, lmax_helper, Vol_SU3_Haar)                  # (local)
    a4_hz = zeta_a_n(2, lmax_helper, Vol_SU3_Haar)                  # (local)
    a0_hc = hard_cutoff_a_n(0, lmax_helper, Vol_SU3_Haar, CUTOFF_FRAC)  # (local)
    a2_hc = hard_cutoff_a_n(1, lmax_helper, Vol_SU3_Haar, CUTOFF_FRAC)  # (local)
    a4_hc = hard_cutoff_a_n(2, lmax_helper, Vol_SU3_Haar, CUTOFF_FRAC)  # (local)
    helper_ratio_zeta = a4_hz / a2_hz                               # (local)
    helper_ratio_hc = a4_hc / a2_hc                                 # (local)
    helper_shift = abs(helper_ratio_hc / helper_ratio_zeta - 1.0)   # (local)
    R1_helper_zeta = a0_hz * a4_hz / a2_hz ** 2                     # (local)
    R1_helper_hc = a0_hc * a4_hc / a2_hc ** 2                       # (local)
    print(f"\nSCHEMATIC helper (L_max={lmax_helper}, cutoff_frac={CUTOFF_FRAC}):")
    print(f"  zeta_a_n:        a_0^{{zeta-hel}} = {a0_hz:.6f}, "
          f"a_2^{{zeta-hel}} = {a2_hz:.6f}, a_4^{{zeta-hel}} = {a4_hz:.6f}")
    print(f"  hard_cutoff_a_n: a_0^{{cutoff-hel}} = {a0_hc:.6f}, "
          f"a_2^{{cutoff-hel}} = {a2_hc:.6f}, a_4^{{cutoff-hel}} = {a4_hc:.6f}")
    print(f"  helper moment-ratio a_4/a_2: zeta = {helper_ratio_zeta:.6f}, "
          f"hard-cutoff = {helper_ratio_hc:.6f} "
          f"=> same-normalization shift = {helper_shift:.6f} (> 0)")
    print(f"  helper R_1 analogs (schematic spectrum, diagnostic only): "
          f"zeta = {R1_helper_zeta:.6f}, hard-cutoff = {R1_helper_hc:.6f}")

    # ---- (4) Per-scheme masses + Claim A (SCALE moves) ----
    M_zeta = scale_zeta * O_arr                                     # (local)
    M_cutoff = scale_cutoff * O_arr                                 # (local)
    M_H_zeta = scale_zeta * O_00                                    # (local)
    M_H_cutoff = scale_cutoff * O_00                                # (local)
    scale_ratio = scale_cutoff / scale_zeta                         # (local)
    D_scale_per_sector = np.abs(M_cutoff - M_zeta) / M_zeta         # (local)
    D_scale = float(D_scale_per_sector[0])                          # (local)
    D_scale_spread = float(np.max(D_scale_per_sector)
                           - np.min(D_scale_per_sector))            # (local)
    D_mH = abs(M_H_cutoff - M_H_zeta) / M_H_zeta                    # (local)
    D_mH_sqrt_reading = sqrt(scale_ratio) - 1.0                     # (local)
    print(f"\nClaim A (INFO content -- the SCALE moves):")
    print(f"  ratio of moment-ratios (native norms) = "
          f"{scale_ratio:.6f}  [plan chain: 61.635]")
    print(f"  D_scale = |M0^cutoff - M0^zeta|/M0^zeta = {D_scale:.6f} "
          f"(per-sector spread {D_scale_spread:.2e}; common envelope cancels)")
    print(f"  Delta(m_H)/m_H [linear riding, Definition 1] = {D_mH:.6f}")
    print(f"  Delta(m_H)/m_H [sqrt/quartic reading, diagnostic] = "
          f"{D_mH_sqrt_reading:.6f}")
    print(f"  NOTE: magnitude is native-normalization-dependent (the plan "
          f"flags the raw factor as a normalization artifact); the PHYSICAL "
          f"claim is D_scale > 0 strictly: {D_scale > 0}")

    # ---- (5) Claim B (PASS-side -- RATIOS bit-identical) ----
    r_zeta = np.array([M_zeta[i] / M_zeta[j] for i, j in PAIRS])    # (local)
    r_cutoff = np.array([M_cutoff[i] / M_cutoff[j] for i, j in PAIRS])  # (local)
    ratio_dev = np.abs(r_zeta - r_cutoff) / np.abs(r_zeta)          # (local)
    ratio_dev_max = float(np.max(ratio_dev))                        # (local)
    d_zeta = M_zeta / M_zeta.max()                                  # (local)
    d_cutoff = M_cutoff / M_cutoff.max()                            # (local)
    d_dev_max = float(np.max(np.abs(d_zeta - d_cutoff) / d_zeta))   # (local)
    print(f"\nClaim B (PASS-side -- RATIO invariance):")
    for k, (i, j) in enumerate(PAIRS):
        print(f"  r_{TOWER[i]}/{TOWER[j]}: zeta = {r_zeta[k]:.15f}  "
              f"cutoff = {r_cutoff[k]:.15f}  rel dev = {ratio_dev[k]:.3e}")
    print(f"  max cross-scheme RATIO deviation = {ratio_dev_max:.3e} "
          f"(ratio_tol = {RATIO_TOL:.0e}; info_band = {INFO_BAND:.0e})")
    print(f"  normalized d_i deviation (max) = {d_dev_max:.3e}")

    # Controls (pre-registered as controls, not gates):
    # (a) degenerate control: same scale on both legs => EXACT bit-zero dev.
    M_ctrl = scale_zeta * O_arr                                     # (local)
    r_ctrl = np.array([M_ctrl[i] / M_ctrl[j] for i, j in PAIRS])    # (local)
    ctrl_zero = float(np.max(np.abs(r_zeta - r_ctrl)))              # (local)
    # (b) sensitivity control: perturb the ENVELOPE (a fake kernel-scale
    #     leak, per-sector-varying) => the test MUST see ~LEAK_CONTROL_EPS.
    leak_fac = 1.0 + LEAK_CONTROL_EPS * np.arange(len(TOWER))       # (local)
    M_leak = scale_cutoff * (O_arr * leak_fac)                      # (local)
    r_leak = np.array([M_leak[i] / M_leak[j] for i, j in PAIRS])    # (local)
    leak_seen = float(np.max(np.abs(r_zeta - r_leak)
                             / np.abs(r_zeta)))                     # (local)
    print(f"  control (a) same-scale degenerate: max |dev| = {ctrl_zero:.1e} "
          f"(exact 0 expected: {ctrl_zero == 0.0})")
    print(f"  control (b) injected envelope leak {LEAK_CONTROL_EPS:.0e}: "
          f"test sees {leak_seen:.3e} (>> ratio_tol => test is sensitive)")
    assert ctrl_zero == 0.0, "degenerate control non-zero -- machinery broken"
    assert leak_seen > 100 * RATIO_TOL, "sensitivity control failed"

    res.update(
        mu_H=global_floor, mu2=mu2, O_arr=O_arr, O_00=O_00,
        o_repro_dev=o_repro_dev, r_cross_repro=r_cross_repro,
        r_cross_dev=r_cross_dev,
        scale_zeta=scale_zeta, scale_cutoff=scale_cutoff,
        scale_zeta_fullprec=scale_zeta_fullprec,
        scale_zeta_pubdev=scale_zeta_pubdev,
        R1_zeta=R1_zeta, R1_dev=R1_dev, R1_cutoff_fmom=R1_cutoff_fmom,
        f2_cf=f2_cf, f4_cf=f4_cf, f2_cf_dev=f2_cf_dev, f4_cf_dev=f4_cf_dev,
        f2_q=f2_q, f4_q=f4_q, f2_q_dev=f2_q_dev, f4_q_dev=f4_q_dev,
        a0_hz=a0_hz, a2_hz=a2_hz, a4_hz=a4_hz,
        a0_hc=a0_hc, a2_hc=a2_hc, a4_hc=a4_hc,
        helper_ratio_zeta=helper_ratio_zeta, helper_ratio_hc=helper_ratio_hc,
        helper_shift=helper_shift, R1_helper_zeta=R1_helper_zeta,
        R1_helper_hc=R1_helper_hc,
        M_zeta=M_zeta, M_cutoff=M_cutoff,
        M_H_zeta=M_H_zeta, M_H_cutoff=M_H_cutoff,
        scale_ratio=scale_ratio, D_scale=D_scale,
        D_scale_spread=D_scale_spread, D_mH=D_mH,
        D_mH_sqrt_reading=D_mH_sqrt_reading,
        r_zeta=r_zeta, r_cutoff=r_cutoff, ratio_dev=ratio_dev,
        ratio_dev_max=ratio_dev_max, d_zeta=d_zeta, d_cutoff=d_cutoff,
        d_dev_max=d_dev_max, ctrl_zero=ctrl_zero, leak_seen=leak_seen,
    )
    return res


# ---------------------------------------------------------------------------
# Section 6 -- Gate evaluation ([SIGN] 3-tuple + pre-registered collapse)
# ---------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple[str, str, str, str, bool]:
    """Return (composite, sign, magnitude, regime, kernel_leak_flag).

    Pre-registered rule (plan SS W4-12 rubric + gate-verdicts.md collapse):
      ratio_dev_max > INFO_BAND          -> sign=FAIL, magnitude=FAIL -> FAIL
      ratio_dev_max <= RATIO_TOL         -> sign=PASS (both claim directions
        hold: D_scale > 0 AND ratio dev at float64 zero), magnitude=INFO
        (D_scale is reported-not-gated; INFO-by-design) -> composite INFO
      RATIO_TOL < dev <= INFO_BAND       -> same but kernel_leak_flag=True
      D_scale == 0 (Claim A direction violated) -> sign=FAIL -> FAIL
      regime=VALID: full domain (no auto-shortening; domain_used_frac=1.0),
        cache blocks complete + all input cross-checks asserted upstream.
    """
    dev = r["ratio_dev_max"]                                        # (local)
    regime = "VALID"                                                # (local)
    if dev > INFO_BAND:
        return "FAIL", "FAIL", "FAIL", regime, False
    if r["D_scale"] <= 0.0:
        return "FAIL", "FAIL", "INFO", regime, False
    sign = "PASS"                                                   # (local)
    magnitude = "INFO"                                              # (local)
    leak = bool(dev > RATIO_TOL)                                    # (local)
    # collapse rule: regime VALID + sign PASS + magnitude INFO => INFO
    return "INFO", sign, magnitude, regime, leak


# ---------------------------------------------------------------------------
# Section 7 -- Plot + npz + payload
# ---------------------------------------------------------------------------
def make_plot(r: dict, verdict: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(16.5, 5.2))             # (local)
    ax1, ax2, ax3 = axes                                            # (local)
    labels = [str(pq) for pq in TOWER] + ["(0,0) m_H"]              # (local)
    x = np.arange(4)                                                # (local)
    mz = list(r["M_zeta"]) + [r["M_H_zeta"]]                        # (local)
    mc = list(r["M_cutoff"]) + [r["M_H_cutoff"]]                    # (local)
    ax1.bar(x - 0.18, mz, width=0.36,
            label=r"zeta leg (FULL): $a_4^{\zeta}/a_2^{\zeta}\cdot O_g$",
            color="#2c5f8a")
    ax1.bar(x + 0.18, mc, width=0.36,
            label=r"cutoff leg (SCHEMATIC): $f_4/f_2\cdot O_g$",
            color="#c25b2a")
    ax1.set_yscale("log")
    ax1.set_xticks(x, labels)
    ax1.set_ylabel(r"$M^{sector}$ (envelope units, native norms)")
    ax1.set_title(f"Claim A: the SCALE moves\n"
                  f"ratio of moment-ratios = {r['scale_ratio']:.3f} "
                  f"(D_scale = {r['D_scale']:.4g})")
    ax1.legend(fontsize=8)
    ax1.grid(alpha=0.3, which="both")

    pair_labels = [f"{TOWER[i]}/{TOWER[j]}" for i, j in PAIRS]      # (local)
    xp = np.arange(len(PAIRS))                                      # (local)
    dev_plot = np.maximum(r["ratio_dev"], 1e-18)                    # (local)
    ax2.bar(xp, dev_plot, width=0.5, color="#3a7d44")
    ax2.axhline(RATIO_TOL, color="k", ls="--", lw=1.2,
                label=f"ratio_tol = {RATIO_TOL:.0e} (PASS)")
    ax2.axhline(INFO_BAND, color="r", ls=":", lw=1.2,
                label=f"info_band = {INFO_BAND:.0e} (FAIL above)")
    ax2.axhline(max(r["leak_seen"], 1e-18), color="#c25b2a", ls="-.",
                lw=1.0, label=f"injected-leak control ({r['leak_seen']:.1e})")
    ax2.set_yscale("log")
    ax2.set_ylim(1e-18, 1e-4)
    ax2.set_xticks(xp, pair_labels, fontsize=8)
    ax2.set_ylabel("|r_zeta - r_cutoff| / r_zeta")
    ax2.set_title(f"Claim B: RATIOS bit-identical\n"
                  f"max dev = {r['ratio_dev_max']:.2e} <= 1e-12")
    ax2.legend(fontsize=8)
    ax2.grid(alpha=0.3, which="both")

    cats = ["zeta\n(canonical)", "cutoff\n(f* moments)",
            "helper zeta\n(SCHEMATIC)", "helper hard-cutoff\n(SCHEMATIC)"]  # (local)
    vals = [r["scale_zeta"], r["scale_cutoff"],
            r["helper_ratio_zeta"], r["helper_ratio_hc"]]           # (local)
    cols = ["#2c5f8a", "#c25b2a", "#7a9cc6", "#d99a77"]             # (local)
    ax3.bar(np.arange(4), vals, color=cols, width=0.55)
    ax3.set_yscale("log")
    ax3.set_xticks(np.arange(4), cats, fontsize=7)
    ax3.set_ylabel(r"$a_4/a_2$ moment ratio (native norms)")
    ax3.set_title(f"Bosonic-scale moment ratio by functional\n"
                  f"helper same-norm shift = {r['helper_shift']:.4f} > 0")
    ax3.grid(alpha=0.3, which="both")
    for xi, v in enumerate(vals):
        ax3.text(xi, v * 1.15, f"{v:.4g}", ha="center", fontsize=8)

    fig.suptitle(f"{GATE_ID}: {verdict} -- SCALE is scheme-DEPENDENT, "
                 f"RATIOS are scheme-INDEPENDENT (S75 W2-E empirical face)",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"\nPlot saved: {OUT_PNG.name}")


def save_npz(r: dict, verdict: str, tup3: tuple, leak_flag: bool,
             pins: dict, audit_sha: str, content_sha: str) -> None:
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        verdict=verdict, sign_verdict=tup3[0], magnitude_verdict=tup3[1],
        regime_verdict=tup3[2], kernel_leak_flag=leak_flag,
        # thresholds (pre-registered)
        ratio_tol=RATIO_TOL, info_band=INFO_BAND, x_max=X_MAX,
        cutoff_frac=CUTOFF_FRAC,
        # envelope (scheme-independent)
        tower_pq=np.array(TOWER), mu_H=r["mu_H"], mu2=r["mu2"],
        O_g=r["O_arr"], O_00=r["O_00"], o_repro_dev=r["o_repro_dev"],
        r_cross_repro=r["r_cross_repro"], r_cross_dev=r["r_cross_dev"],
        # zeta leg (FULL)
        a_0_zeta=a_0_FW_zeta, a_2_zeta=a_2_FW_zeta, a_4_zeta=a_4_FW_zeta,
        scale_zeta=r["scale_zeta"],
        scale_zeta_fullprec=r["scale_zeta_fullprec"],
        scale_zeta_pubdev=r["scale_zeta_pubdev"],
        R1_zeta=r["R1_zeta"], R1_dev=r["R1_dev"], R1_canonical=R1_lizzi,
        # cutoff leg (SCHEMATIC)
        f_0_star=mellin_f_star_f0, f_2_star=mellin_f_star_f2,
        f_4_star=mellin_f_star_f4, scale_cutoff=r["scale_cutoff"],
        f2_closed_form=r["f2_cf"], f4_closed_form=r["f4_cf"],
        f2_cf_dev=r["f2_cf_dev"], f4_cf_dev=r["f4_cf_dev"],
        f2_quad=r["f2_q"], f4_quad=r["f4_q"],
        f2_q_dev=r["f2_q_dev"], f4_q_dev=r["f4_q_dev"],
        R1_cutoff_fmom=r["R1_cutoff_fmom"],
        helper_a0_zeta=r["a0_hz"], helper_a2_zeta=r["a2_hz"],
        helper_a4_zeta=r["a4_hz"], helper_a0_hc=r["a0_hc"],
        helper_a2_hc=r["a2_hc"], helper_a4_hc=r["a4_hc"],
        helper_ratio_zeta=r["helper_ratio_zeta"],
        helper_ratio_hc=r["helper_ratio_hc"],
        helper_shift=r["helper_shift"],
        R1_helper_zeta=r["R1_helper_zeta"], R1_helper_hc=r["R1_helper_hc"],
        # Claim A
        M_zeta=r["M_zeta"], M_cutoff=r["M_cutoff"],
        M_H_zeta=r["M_H_zeta"], M_H_cutoff=r["M_H_cutoff"],
        scale_ratio=r["scale_ratio"], D_scale=r["D_scale"],
        D_scale_spread=r["D_scale_spread"], D_mH=r["D_mH"],
        D_mH_sqrt_reading=r["D_mH_sqrt_reading"],
        # Claim B (full float64 per publication-precision pin)
        pairs=np.array(PAIRS), r_zeta=r["r_zeta"], r_cutoff=r["r_cutoff"],
        ratio_dev=r["ratio_dev"], ratio_dev_max=r["ratio_dev_max"],
        d_zeta=r["d_zeta"], d_cutoff=r["d_cutoff"], d_dev_max=r["d_dev_max"],
        ctrl_zero=r["ctrl_zero"], leak_seen=r["leak_seen"],
        leak_control_eps=LEAK_CONTROL_EPS,
        # provenance
        tau_fold_used=tau_fold, vol_su3_haar=Vol_SU3_Haar,
        spectrum_cache_sha=CACHE_SHA_PIN,
        input_pin_map=json.dumps(dict(sorted(pins.items()))),
        machinery_pin_map=json.dumps(MACHINERY_PIN_MAP, sort_keys=True),
        domain_used_frac=1.0,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"Data saved: {OUT_NPZ.name}")


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (agent calls mcp__knowledge__emit_verdict)."""
    payload: dict = {                                               # (local)
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
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


# ---------------------------------------------------------------------------
# Section 8 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)                              # (local)
    script_path = Path(__file__).resolve()                          # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path,
                                              pins)                 # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    r = compute(pins)                                               # (local)
    verdict, sign_v, mag_v, reg_v, leak_flag = evaluate_gate(r)     # (local)

    print(f"\n=== gate evaluation (pre-registered collapse) ===")
    print(f"  sign_verdict      = {sign_v}  (Claim A D_scale > 0 AND "
          f"Claim B ratio-dev at float64 zero)")
    print(f"  magnitude_verdict = {mag_v}  (D_scale reported-not-gated; "
          f"INFO-by-design)")
    print(f"  regime_verdict    = {reg_v}  (full domain; blocks complete; "
          f"domain_used_frac=1.0)")
    print(f"  kernel_leak_flag  = {leak_flag}")
    print(f"  composite         = {verdict}")

    make_plot(r, verdict)
    save_npz(r, verdict, (sign_v, mag_v, reg_v), leak_flag, pins,
             audit_sha, content_sha)

    value = (                                                       # (local)
        f"D_scale={r['D_scale']:.4g}_native-norm(claimA-sign>0);"
        f"ratio_dev_max={r['ratio_dev_max']:.3e}<=1e-12;"
        f"scale_zeta=a4z/a2z={r['scale_zeta']:.7f};"
        f"scale_cutoff=f4/f2={r['scale_cutoff']:.6f};"
        f"ratio-of-ratios={r['scale_ratio']:.4f};"
        f"dmH_lin={r['D_mH']:.4g}_sqrt-read={r['D_mH_sqrt_reading']:.4g};"
        f"R1_zeta={r['R1_zeta']:.7f}_vs_canon_rel={r['R1_dev']:.1e};"
        f"R1_fmom={r['R1_cutoff_fmom']:.7f}(per-branch;not-cross-scheme);"
        f"helper_hc/zeta_a4a2_shift={r['helper_shift']:.4f};"
        f"O_g_repro_dev={r['o_repro_dev']:.1e};"
        f"leak_ctrl_seen={r['leak_seen']:.2e};"
        f"kernel_leak={'FLAGGED' if leak_flag else 'none'}"
    )
    companion = (                                                   # (local)
        "DUAL-scheme empirical face of S75 W2-E decoupling: SCALE moves "
        f"{r['scale_ratio']:.1f}x (native norms; physical content = sign), "
        f"RATIOS bit-identical to {r['ratio_dev_max']:.1e}; zeta leg FULL "
        "(canonical a_n_FW_zeta), cutoff leg SCHEMATIC (f* Mellin moments "
        "X_MAX=50 + _spectral_action_regulators.py helper)"
    )
    extra = [                                                       # (local)
        ("# regulator_pin: DUAL -- zeta leg a_0^{zeta}=6440.0 "
         "a_2^{zeta}=2776.165389 a_4^{zeta}=1350.7216 (FULL npz-sourced "
         "canonical, S88-A-N-FW-CANONICALIZATION); cutoff leg "
         "a_2^{cutoff}=f_2=214.97335676 a_4^{cutoff}=f_4=6446.63942272 "
         "(Mellin f-moments of f*, X_MAX=50, S78 W2-D); bare a_n FORBIDDEN "
         "per regulator-pin-discipline.md # " + GATE_ID),
        ("# tier_pin=TIER-2 # " + GATE_ID + " cutoff leg consumes "
         "_spectral_action_regulators.py (SCHEMATIC per docstring L23-30, "
         "S88 W7b-83 verified); zeta leg level-pinned SEPARATELY as FULL "
         "(canonical npz-sourced a_n_FW_zeta) per "
         "substrate-first-canonical-sourcing.md (iv)"),
        ("# operational_enrichment: s100a_yukawa_overlap_offdiag.npz "
         "consumed as 4th pinned input (Item-6 O_g reproduction cross-check "
         "ONLY; primary O_g recomputed from s84 cache, max rel dev "
         f"{r['o_repro_dev']:.1e}); plan input_files listed 3; "
         "honest-disclosure per math-scripts.md plan-authorship item 4 # "
         + GATE_ID),
        ("# masses(envelope-units): M_zeta=("
         + ",".join(f"{v:.6f}" for v in r["M_zeta"]) + ") M_cutoff=("
         + ",".join(f"{v:.6f}" for v in r["M_cutoff"]) + ") mH-channel "
         f"O_00={r['O_00']:.6f}; r_pairs=("
         + ",".join(f"{v:.9f}" for v in r["r_zeta"])
         + ") identical both schemes; controls: degenerate=0.0 exact, "
         f"injected-leak 1e-6 seen at {r['leak_seen']:.2e} # " + GATE_ID),
    ]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)             # (local)
    print(f"\n{tag}")
    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=reg_v, companion_note=companion,
                          extra_rows=extra)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0   # exit 0 regardless of scientific verdict (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
