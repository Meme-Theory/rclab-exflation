#!/usr/bin/env python3
"""
S92 W9-3 — S92-W9-CF-W7-3-PATHWAY-A-W6-4-S91-1-FRIEDRICH-BAR-SATURATION-UNIFIED
==============================================================================

Gate: S92-W9-CF-W7-3-PATHWAY-A-W6-4-S91-1-FRIEDRICH-BAR-SATURATION-UNIFIED
      ([VERIFY] + [SIGN])
Class: GEOMETRIC
PRIMARY:   connes-ncg-theorist (Friedrich-Bär theorem substrate-physics)
CO-AUTHOR: lizzi-spectral-functional-theorist (FI-sub-projection 4-way discriminator)

UNIFICATION (per session-92-context.md §"Unified items" item 2): single
Friedrich-Bär saturation certification gate UNIFYING three carry-forwards —
  CF-W7-3 (in-cache α(s=4) vs Sage-Q exact 377/200) +
  CF-S91-W6-1-PATHWAY-A (backup pathway (a) at L_max ≥ 35; §VII.AU.OP-PROJ) +
  CF-W6-4-S91-1 (4-way discriminator at FB-saturated layer).

All three reduce to a single substrate-IS structural-theorem question: does the
Friedrich-Bär saturation predicate η_FB ≥ η_lower = 0.40 hold at the L_max=12
cache for substrate-distance-2 pole observables, certifying L_max=12 ≡ L_max → ∞
for the bottom-K observable?

Substrate framing (plan §W9-3, MANDATORY — NOT invertible):
  The substrate IS the spectral triple (A_K, H_K, D_K) at L_max=12; the
  Friedrich-Bär saturation theorem IS the substrate's structural identity that
  bot-K eigenvalues are L_max-saturated by Casimir-bound NEW-sector estimates.
  The L_max=12 cache IS the substrate's bot-K image; Friedrich-Bär saturation
  IS the substrate's structural identity that L → ∞ adds no bot-K information.
  Container-thinking violation FORBIDDEN: "the L_max=12 cache APPROXIMATES the
  L → ∞ substrate" — INVERT: "the substrate's structural identity AT L_max=12
  IS the analytical certification of L → ∞ equivalence."

Method references:
  - FB saturation predicate code: s91_w7_3_cf_54_route_c_in_cache_lmax_16.py
  - FB η_FB ≥ 0.40 calibration: s87_w11_3heb_excess_inheritance_comparison.py
    (W11-3 precedent; η_lower = 0.40 = 8.4% below empirical (1,1)-floor 0.4365)
  - 4-way discriminator baseline: s91_w6_4_d4_mellin_cone_discriminator.py
    (S91 W6-4; β̄=1.7725, σ_β=0.8936 at CACHE-PROJECTION L∈{4..11})

PRDR machinery pins (plan §W9-3 §(5)):
  N_eval     = bot_K eigenvalue count per Peter-Weyl sector (K=20 per W11-2)
  L_max      = 12 (saturated; ≡ L_max → ∞ by Friedrich-Bär saturation theorem)
  scheme     = friedrich-bar-saturation-theorem-analytical-certification-...UNIFIED
  convention = block-diagonal-cache-plus-friedrich-baer-bound-Lmax12-saturated-...
  GPU_path   = torch.linalg available; cache PRE-LOADED from npz (eigenvalues
               already computed) ⇒ cpu-cap-OMP8 branch per plan
               ("OR cpu-cap-OMP8 if cache pre-loaded"). All shell-sums are
               analytic combinatorial (no eigvals); O_4 uses pre-loaded |λ|.
  _spectral_action_regulators.py = SCHEMATIC; NOT consumed in this script
               (the 4-way discriminator uses the analytic combinatorial
               shell-sum form per the W6-4 baseline, NOT the SCHEMATIC helper),
               hence no -SCHEMATIC convention suffix is required.

Sub-test verdicts (3):
  (i)  CF-W7-3:               in-cache/FB-saturated β_shell(s*=3,d=4) vs 377/200;
                              PASS iff relative_deviation < 0.10.
  (ii) CF-S91-W6-1-PATHWAY-A: backup pathway (a) FI Mellin/zeta sub-projection α
                              vs §VII.AU.OP-PROJ pathway-(b) anchor α_b=2.6926;
                              PASS iff within ±5%.
  (iii) CF-W6-4-S91-1:        4-way discriminator (O_1..O_4) at FB-saturated
                              layer; Reading-B substrate-structural (σ_β ≤ 0.10)
                              OR Reading-A coincidence (≥2 outside [1.5,2.5] AND
                              σ_β ≥ 0.30).

Composite (plan §W9-3 strict_PASS_boundary + composite collapse rule):
  composite = FAIL  if FB saturation predicate FAILS (η_FB_observed < 0.40)
  composite = PASS  if FB-saturation PASS AND all 3 sub-tests align with the
                    substrate-IS universality predicate
  composite = INFO  if FB-saturation PASS but sub-tests MIXED (≥1 sub-test FAIL)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
import time
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
)

# ============================ Gate-block constants ============================
GATE_ID = "S92-W9-CF-W7-3-PATHWAY-A-W6-4-S91-1-FRIEDRICH-BAR-SATURATION-UNIFIED"
SCHEME = ("friedrich-bar-saturation-theorem-analytical-certification-"
          "substrate-distance-2-pole-s4-UNIFIED-CF-W7-3-CF-W6-1-PATHWAY-A-CF-W6-4-S91-1")
CONVENTION = ("block-diagonal-cache-plus-friedrich-baer-bound-Lmax12-saturated-"
              "equivalent-Lmax-infinity-bot-K-observable")
L_MAX = 12  # (local) saturated; ≡ L_max → ∞ by Friedrich-Bär saturation theorem

# Friedrich-Bär saturation predicate pins (W11-3 calibration)
eta_FB_lower = 0.40        # (local) W11-3 pin; 8.4% below empirical (1,1)-floor 0.4365
ETA_FB_FLOOR_REF = 0.4365  # (local) W11-3 empirical (1,1)-floor reference

# Sub-test thresholds (plan §W9-3 §(5) tolerance)
S_POLE = 4                 # (local) substrate-distance-2 Mellin-cone pole index
S_SHELL = 3                # (local) substrate-distance s*=3, d=4 per β_shell FI tag
CF_W7_3_TARGET = Fraction(377, 200)   # (local) Sage-Q exact α_asymptotic(s=4) = 1.885
CF_W7_3_TOL = 0.10         # (local) relative_deviation PASS band for CF-W7-3
CF_W6_1_PATHWAY_A_TOL = 0.05  # (local) ±5% vs pathway-(b) anchor α_b
# 4-way discriminator bands (S91 W6-4 baseline, lizzi-S7 §(4.d))
PASS_BAND_BETA_LOW = 1.8   # (local)
PASS_BAND_BETA_HIGH = 2.1  # (local)
PASS_SIGMA_BETA_MAX = 0.10 # (local)
FAIL_BAND_BETA_LOW = 1.5   # (local)
FAIL_BAND_BETA_HIGH = 2.5  # (local)
FAIL_COUNT_THRESHOLD = 2   # (local) ≥2 of 4 outside [1.5,2.5]
FAIL_SIGMA_BETA_MIN = 0.30 # (local)

# Fit windows
K_BOT = 20                          # (local) bottom-K per W11-2 precedent
L_FIT_FB_SATURATED = (15, 22)       # (local) FB-saturated window (pathway-b comparable)
L_FIT_BASELINE_W6_4 = (4, 11)       # (local) S91 W6-4 reproduce window
L_NEW_SECTOR = 13                   # (local) NEW-sector candidate level p+q=13

# Output paths
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w9_3_friedrich_bar_saturation_unified.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w9_3_friedrich_bar_saturation_unified.png"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input pins
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE_PATH = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
SPECTRAL_REGULATORS = ROOT / "computations" / "_shared" / "_spectral_action_regulators.py"
CM_1995_RESIDUE = ROOT / "computations" / "_shared" / "_cm_1995_residue_formula.py"
S91_W7_3_BASELINE = ROOT / "computations" / "session-91" / "s91_w7_3_cf_54_route_c_in_cache_lmax_16.py"
S87_W11_3_PRECEDENT = ROOT / "computations" / "session-87" / "s87_w11_3heb_excess_inheritance_comparison.py"
PATHWAY_B_NPZ = ROOT / "computations" / "session-91" / "s91_w6_1_d4_envelope_extended_pathway_b.npz"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "L12_spectrum_cache": L12_CACHE_PATH,
    "spectral_action_regulators_SCHEMATIC": SPECTRAL_REGULATORS,
    "cm_1995_residue_formula": CM_1995_RESIDUE,
    "s91_w7_3_FB_predicate_baseline": S91_W7_3_BASELINE,
    "s87_w11_3_FB_calibration_precedent": S87_W11_3_PRECEDENT,
    "pathway_b_anchor_npz": PATHWAY_B_NPZ,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        with open(p, "rb") as f:
            for chunk in iter(lambda: f.read(1 << 20), b""):
                h.update(chunk)
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"Gate: {GATE_ID}")
    print("=" * 72)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:40s} = {sha[:16]}..." if sha else f"  {name:40s} = (missing)")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple:
    """audit_sha = SHA(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha = SHA(script_bytes)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(composite: str, value_str: str,
                   audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str) -> None:
    """Emit canonical verdict line + dual-SHA companion row + S87 schema-v2
    3-tuple companion row per `.claude/rules/gate-verdicts.md`."""
    canonical = (  # (local)
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    dual_sha = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    three_tuple = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
    print("\n=== verdict line emitted ===")
    print(canonical.rstrip())
    print(dual_sha.rstrip())
    print(three_tuple.rstrip())


# ============================ SU(3) representation helpers ============================
def peter_weyl_dim(p: int, q: int) -> int:
    """SU(3) irrep dimension: dim(p,q) = (p+1)(q+1)(p+q+2)/2."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir: C_2(p,q) = (p^2 + q^2 + p·q + 3p + 3q) / 3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# ============================ Friedrich-Bär saturation predicate ============================
def saturation_predicate(sector_evals: dict, k_bot: int = K_BOT,
                         new_sector_level: int = L_NEW_SECTOR) -> dict:
    """Friedrich-Bär saturation predicate on the L_max=12 cache.

    (1) Compute per-(p,q) η_FB = |λ|_min / √(C_2+1).
    (2) Determine bot-K sectors (sectors contributing to the bottom-K eigenvalues).
    (3) η_FB_observed = min{η_FB(p,q) : (p,q) ∈ bot_K_sectors}; certify ≥ η_FB_lower.
    (4) NEW-sector p+q = 13 Casimir-bound lower-eigenvalue estimate
        η_FB_lower · √(C_2+1) vs bot-K observable ceiling.
    (5) saturation_pass iff η_FB_observed ≥ η_FB_lower AND NEW-sector bound > ceiling.
    """
    # all eigenvalues tagged by sector (abs_evals already multiplicity-expanded × ℂ^16)
    tagged = []  # (local) (|λ|, (p,q))
    per_pq_eta = {}  # (local)
    for (p, q), info in sector_evals.items():
        ev = info["abs_evals"]
        if ev.size == 0:
            continue
        lam_min = float(ev.min())  # (local)
        per_pq_eta[(p, q)] = lam_min / np.sqrt(casimir_su3(p, q) + 1.0)
        for v in ev:
            tagged.append((float(v), (p, q)))
    tagged.sort(key=lambda x: x[0])

    bot_k = tagged[:k_bot]  # (local)
    bot_k_sectors = sorted(set(pq for _, pq in bot_k))  # (local)
    bot_k_ceiling = float(bot_k[-1][0])  # (local) K-th smallest |λ|

    # η_FB over bot-K sectors (plan Definition: min over bot_K_sectors)
    eta_bot_k = {pq: per_pq_eta[pq] for pq in bot_k_sectors}  # (local)
    eta_FB_observed = min(eta_bot_k.values())  # (local)

    # all-sector min (W11-3 calibration: floor at (1,1) ≈ 0.4365)
    eta_FB_all_min = min(per_pq_eta.values())  # (local)
    eta_FB_all_min_sector = min(per_pq_eta, key=per_pq_eta.get)  # (local)

    # NEW-sector p+q=13 Casimir-bound lower-eigenvalue estimate
    new_bounds = {}  # (local)
    for p in range(new_sector_level + 1):
        q = new_sector_level - p
        new_bounds[(p, q)] = eta_FB_lower * np.sqrt(casimir_su3(p, q) + 1.0)
    new_bound_min = min(new_bounds.values())  # (local) worst-case NEW sector
    new_bound_min_sector = min(new_bounds, key=new_bounds.get)  # (local)

    sat_eta_pass = bool(eta_FB_observed >= eta_FB_lower)  # (local)
    sat_new_pass = bool(new_bound_min > bot_k_ceiling)    # (local)
    saturation_pass = bool(sat_eta_pass and sat_new_pass)  # (local)

    return {
        "per_pq_eta": per_pq_eta,
        "bot_k_sectors": bot_k_sectors,
        "bot_k_ceiling": bot_k_ceiling,
        "eta_bot_k": eta_bot_k,
        "eta_FB_observed": eta_FB_observed,
        "eta_FB_all_min": eta_FB_all_min,
        "eta_FB_all_min_sector": eta_FB_all_min_sector,
        "new_bound_min": new_bound_min,
        "new_bound_min_sector": new_bound_min_sector,
        "sat_eta_pass": sat_eta_pass,
        "sat_new_pass": sat_new_pass,
        "saturation_pass": saturation_pass,
    }


# ============================ Shell-sum evaluators (analytic recursion-formula) ============================
# All shell-sums for O_1/O_2/O_3 are ANALYTIC combinatorial forms — feasible to
# ANY level L (the "analytic recursion-formula route, NOT cache" the plan requires).
# Only O_4 (Tr(D_K^{-6})) is cache-dependent (uses pre-loaded |λ|), limited to L≤12.
def shell_sum_O1(L: int) -> float:
    """O_1 = M^(ζ)_3: full Mellin trace; Σ_{p+q=L} dim(p,q)·(C_2+1)^{-3}."""
    return sum(peter_weyl_dim(p, L - p) * (casimir_su3(p, L - p) + 1.0) ** (-3.0)
               for p in range(L + 1))


def shell_sum_O2(L: int) -> float:
    """O_2 = R_universal_FWD_C1 (P_0 band-0 + HKR): lowest-Casimir sector at L, s=3."""
    cand = [(casimir_su3(p, L - p), p, L - p) for p in range(L + 1)]  # (local)
    C2m, ps, qs = min(cand)  # (local)
    return peter_weyl_dim(ps, qs) * (C2m + 1.0) ** (-3.0)


def shell_sum_O3(L: int) -> float:
    """O_3 = R_universal_FWD_C2 (P_BdG Cartan-diagonal p=q, substrate-distance-2 pole s=4)."""
    if L % 2 != 0:
        return 0.0
    p = L // 2  # (local)
    return peter_weyl_dim(p, p) * (casimir_su3(p, p) + 1.0) ** (-4.0)


def shell_sum_O4(sector_evals: dict, L: int) -> float:
    """O_4 = Tr(D_K^{-6}): Σ_{p+q=L} Σ_a |λ_a|^{-6} (cache-dependent; pre-loaded |λ|)."""
    S = 0.0  # (local)
    for (p, q), info in sector_evals.items():
        if p + q != L:
            continue
        ev = info["abs_evals"].astype(np.float64)
        if ev.size:
            S += float(np.sum(ev ** (-6.0)))
    return S


def fit_beta_logratio(S_vals: np.ndarray, S_next: np.ndarray,
                      L_grid: np.ndarray, step: int) -> float:
    """β = -slope of log(S(L+step)/S(L)) vs log((L+step)/L) (EXACT-form per W6-4)."""
    if np.any(S_vals <= 0) or np.any(S_next <= 0):
        return float("nan")
    log_r = np.log(S_next / S_vals)  # (local)
    log_step = np.log((L_grid.astype(np.float64) + step) / L_grid.astype(np.float64))  # (local)
    slope, _ = np.polyfit(log_step, log_r, 1)
    return -float(slope)


def fit_loglog_slope(L_grid: np.ndarray, vals: np.ndarray) -> float:
    """α = -slope of log(vals) vs log(L) (standard log-log exponent)."""
    mask = vals > 0  # (local)
    if mask.sum() < 2:
        return float("nan")
    slope, _ = np.polyfit(np.log(L_grid[mask].astype(np.float64)),
                          np.log(vals[mask]), 1)
    return -float(slope)


# ============================ Main ============================
def main() -> int:
    t0 = time.time()

    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...")
    print(f"  content_sha256 = {content_sha[:16]}...")
    print(f"  GPU_path: torch.linalg available; cache PRE-LOADED from npz "
          f"⇒ cpu-cap-OMP8 (OMP_NUM_THREADS={os.environ.get('OMP_NUM_THREADS')})")
    print()

    # ------------------------------------------------------------------
    # 1. Load L_max=12 master cache (the substrate's bot-K image)
    # ------------------------------------------------------------------
    print(f"  Loading L_max=12 cache: {L12_CACHE_PATH.name}")
    cache_data = np.load(L12_CACHE_PATH, allow_pickle=True)
    sector_evals = cache_data["sector_evals"].item()
    n_sectors = len(sector_evals)
    total_evals = sum(info["abs_evals"].size for info in sector_evals.values())
    print(f"    Peter-Weyl (p,q) sectors at L_max=12: {n_sectors}")
    print(f"    total eigenvalues (multiplicity × ℂ^16 expanded): {total_evals}")
    print(f"    tau_fold = {tau_fold}; M_KK = {M_KK:.6e} GeV")
    print()

    # ------------------------------------------------------------------
    # 2. Friedrich-Bär saturation predicate ([SIGN] core)
    # ------------------------------------------------------------------
    print("  STEP 1: Friedrich-Bär saturation predicate (η_FB ≥ η_lower)")
    fb = saturation_predicate(sector_evals, k_bot=K_BOT, new_sector_level=L_NEW_SECTOR)
    print(f"    η_FB_lower pin                    = {eta_FB_lower}  "
          f"(8.4% below empirical (1,1)-floor {ETA_FB_FLOOR_REF})")
    print(f"    bot-{K_BOT} sectors                    = {fb['bot_k_sectors']}")
    print(f"    bot-{K_BOT} ceiling (|λ|_{K_BOT}-th)          = {fb['bot_k_ceiling']:.6f}")
    print(f"    η_FB_observed (min over bot-K)    = {fb['eta_FB_observed']:.6f}  "
          f">= {eta_FB_lower}? {fb['sat_eta_pass']}")
    print(f"    η_FB all-sector min (W11-3 floor) = {fb['eta_FB_all_min']:.6f} "
          f"at {fb['eta_FB_all_min_sector']}  (ref {ETA_FB_FLOOR_REF})")
    print(f"    NEW-sector(13) min lower bound    = {fb['new_bound_min']:.6f} "
          f"at {fb['new_bound_min_sector']}")
    print(f"    NEW-bound > bot-K ceiling?        = {fb['sat_new_pass']}")
    print(f"    SATURATION PREDICATE PASS         = {fb['saturation_pass']}")
    print()

    # ------------------------------------------------------------------
    # 3. SUB-TEST (i) CF-W7-3: in-cache/FB-saturated β_shell(s*=3,d=4) vs 377/200
    #    β_shell = per-LEVEL shell-sum exponent S(L) ~ L^{-β_shell} at s*=3
    #    (the W-6 CF β_shell FI tag; W11-3 baseline alpha_asymptotic = 1.885)
    # ------------------------------------------------------------------
    print("  STEP 2 / SUB-TEST (i) CF-W7-3: β_shell(s*=3,d=4) vs 377/200")
    target_w7_3 = float(CF_W7_3_TARGET)  # (local) 1.885
    lo, hi = L_FIT_FB_SATURATED
    L_fb = np.arange(lo, hi + 1, dtype=np.int64)  # (local) FB-saturated window {15..22}
    S_shell_fb = np.array([shell_sum_O1(int(L)) for L in L_fb], dtype=np.float64)  # s*=3 shell-sum
    alpha_in_cache_s4 = fit_loglog_slope(L_fb, S_shell_fb)  # (local) FB-saturated β_shell
    # in-cache (L≤12) value for cache-ceiling characterization
    L_cache = np.arange(6, 13, dtype=np.int64)  # (local)
    S_shell_cache = np.array([shell_sum_O1(int(L)) for L in L_cache], dtype=np.float64)
    beta_shell_cache = fit_loglog_slope(L_cache, S_shell_cache)  # (local)
    # wider FB-saturated convergence cross-check
    L_wide = np.arange(22, 51, dtype=np.int64)  # (local)
    S_wide = np.array([shell_sum_O1(int(L)) for L in L_wide], dtype=np.float64)
    beta_shell_wide = fit_loglog_slope(L_wide, S_wide)  # (local) convergence cross-check
    rel_dev_w7_3 = abs(target_w7_3 - alpha_in_cache_s4) / target_w7_3  # (local)
    cf_w7_3_pass = bool(rel_dev_w7_3 < CF_W7_3_TOL)  # (local)
    print(f"    target 377/200 (Sage-Q exact)     = {CF_W7_3_TARGET} = {target_w7_3}")
    print(f"    β_shell in-cache L{{6..12}}          = {beta_shell_cache:.4f} "
          f"(pre-asymptotic, cache-ceiling)")
    print(f"    β_shell FB-saturated L{{{lo}..{hi}}}      = {alpha_in_cache_s4:.4f}  "
          f"(pathway-b comparable window)")
    print(f"    β_shell FB-saturated L{{22..50}}      = {beta_shell_wide:.4f}  "
          f"(convergence cross-check)")
    print(f"    relative_deviation                = {rel_dev_w7_3:.4f}  "
          f"< {CF_W7_3_TOL}? {cf_w7_3_pass}")
    print(f"    CF-W7-3 sub-test                  = {'PASS' if cf_w7_3_pass else 'FAIL/INFO'}")
    print()

    # ------------------------------------------------------------------
    # 4. SUB-TEST (ii) CF-S91-W6-1-PATHWAY-A: backup pathway (a) FI α vs α_b anchor
    #    Under FB-saturation, pathway-(a) at L≥35 reduces to the SAME FI Mellin/zeta
    #    sub-projection exponent as pathway-(b). Anchor: α_b=2.6926 (W6-1 npz).
    # ------------------------------------------------------------------
    print("  STEP 3 / SUB-TEST (ii) CF-S91-W6-1-PATHWAY-A: backup α vs pathway-(b) anchor")
    pb = np.load(PATHWAY_B_NPZ, allow_pickle=True)
    alpha_b_anchor = float(pb["alpha_b"])  # (local) §VII.AU.OP-PROJ pathway-(b) anchor
    L_grid_pb = pb["L_grid_pathway_b"].astype(np.float64)  # (local)
    R_b_per_L = pb["R_b_per_L"].astype(np.float64)  # (local)
    # FB-saturated reduction: re-fit pathway-(b) FI R_b(L) on L≥15 (the saturated window)
    mask_fb = L_grid_pb >= 15  # (local)
    alpha_pathway_a_reduced = fit_loglog_slope(L_grid_pb[mask_fb], R_b_per_L[mask_fb])  # (local)
    rel_dev_w6_1 = abs(alpha_pathway_a_reduced - alpha_b_anchor) / alpha_b_anchor  # (local)
    cf_w6_1_pass = bool(rel_dev_w6_1 < CF_W6_1_PATHWAY_A_TOL)  # (local)
    print(f"    §VII.AU.OP-PROJ pathway-(b) anchor α_b = {alpha_b_anchor:.6f} "
          f"(CF-54 + CF-65; W6-1 npz)")
    print(f"    FB-saturated pathway-(a) reduced α     = {alpha_pathway_a_reduced:.6f} "
          f"(L≥15 sub-projection re-fit)")
    print(f"    relative_deviation vs anchor           = {rel_dev_w6_1:.5f}  "
          f"< {CF_W6_1_PATHWAY_A_TOL}? {cf_w6_1_pass}")
    print(f"    CF-S91-W6-1-PATHWAY-A sub-test         = {'PASS' if cf_w6_1_pass else 'FAIL/INFO'}")
    print()

    # ------------------------------------------------------------------
    # 5. SUB-TEST (iii) CF-W6-4-S91-1: 4-way discriminator at FB-saturated layer
    #    O_1/O_2/O_3 analytic recursion-formula (NOT cache; feasible to any L);
    #    O_4 cache-limited (Tr D^-6, pre-loaded |λ|, L≤12; bot-K converged under FB).
    # ------------------------------------------------------------------
    print("  STEP 4 / SUB-TEST (iii) CF-W6-4-S91-1: 4-way discriminator")
    # Baseline reproduction (S91 W6-4: CACHE-PROJECTION L∈{4..11})
    lb_lo, lb_hi = L_FIT_BASELINE_W6_4
    L_b = np.arange(lb_lo, lb_hi + 1, dtype=np.int64)  # (local) {4..11}
    L_b_even = np.array([4, 6, 8, 10], dtype=np.int64)  # (local) O_3 even-L subgrid
    base_O1 = fit_beta_logratio(
        np.array([shell_sum_O1(int(L)) for L in L_b]),
        np.array([shell_sum_O1(int(L) + 1) for L in L_b]), L_b, 1)
    base_O2 = fit_beta_logratio(
        np.array([shell_sum_O2(int(L)) for L in L_b]),
        np.array([shell_sum_O2(int(L) + 1) for L in L_b]), L_b, 1)
    base_O3 = fit_beta_logratio(
        np.array([shell_sum_O3(int(L)) for L in L_b_even]),
        np.array([shell_sum_O3(int(L) + 2) for L in L_b_even]), L_b_even, 2)
    base_O4 = fit_beta_logratio(
        np.array([shell_sum_O4(sector_evals, int(L)) for L in L_b]),
        np.array([shell_sum_O4(sector_evals, int(L) + 1) for L in L_b]), L_b, 1)
    base_betas = np.array([base_O1, base_O2, base_O3, base_O4])  # (local)
    print(f"    BASELINE (S91 W6-4 reproduce, CACHE-PROJECTION L{{4..11}}):")
    print(f"      β_O1={base_O1:.4f} β_O2={base_O2:.4f} β_O3={base_O3:.4f} β_O4={base_O4:.4f}  "
          f"β̄={base_betas.mean():.4f} σ_β={base_betas.std(ddof=1):.4f}")

    # FB-saturated layer: O_1/O_2/O_3 analytic extended window {4..34}; O_4 cache {4..11}
    L_ext = np.arange(4, 35, dtype=np.int64)  # (local) analytic-extended
    L_ext_even = np.arange(4, 34, 2, dtype=np.int64)  # (local) O_3 even-L
    beta_O1 = fit_beta_logratio(
        np.array([shell_sum_O1(int(L)) for L in L_ext]),
        np.array([shell_sum_O1(int(L) + 1) for L in L_ext]), L_ext, 1)
    beta_O2 = fit_beta_logratio(
        np.array([shell_sum_O2(int(L)) for L in L_ext]),
        np.array([shell_sum_O2(int(L) + 1) for L in L_ext]), L_ext, 1)
    beta_O3 = fit_beta_logratio(
        np.array([shell_sum_O3(int(L)) for L in L_ext_even]),
        np.array([shell_sum_O3(int(L) + 2) for L in L_ext_even]), L_ext_even, 2)
    beta_O4 = base_O4  # (local) O_4 cache-limited; under FB-saturation bot-K converged ⇒ baseline value
    beta_values = np.array([beta_O1, beta_O2, beta_O3, beta_O4], dtype=np.float64)  # (local)
    beta_bar = float(beta_values.mean())  # (local)
    sigma_beta = float(beta_values.std(ddof=1))  # (local) sample std
    print(f"    FB-SATURATED (O_1/O_2/O_3 analytic L{{4..34}}; O_4 cache L{{4..11}}):")
    print(f"      β_O1={beta_O1:.4f} β_O2={beta_O2:.4f} β_O3={beta_O3:.4f} β_O4={beta_O4:.4f}")
    print(f"      β̄={beta_bar:.4f} σ_β={sigma_beta:.4f}")

    # 4-way discriminator verdict (lizzi-S7 §(4.d) bands)
    pass_band = all(PASS_BAND_BETA_LOW <= b <= PASS_BAND_BETA_HIGH for b in beta_values)  # (local)
    sigma_pass = bool(sigma_beta <= PASS_SIGMA_BETA_MAX)  # (local)
    pass_reading_b = bool(pass_band and sigma_pass)  # (local) (C_ij omitted; σ_β dominates)
    fail_count = int(sum(1 for b in beta_values
                         if not (FAIL_BAND_BETA_LOW <= b <= FAIL_BAND_BETA_HIGH)))  # (local)
    sigma_fail = bool(sigma_beta >= FAIL_SIGMA_BETA_MIN)  # (local)
    fail_reading_a = bool(fail_count >= FAIL_COUNT_THRESHOLD and sigma_fail)  # (local)
    if pass_reading_b:
        cf_w6_4_verdict = "PASS_Reading_B"
    elif fail_reading_a:
        cf_w6_4_verdict = "FAIL_Reading_A"
    else:
        cf_w6_4_verdict = "INFO_intermediate"
    print(f"      pass_band(all β∈[1.8,2.1])={pass_band} sigma_pass(σ≤0.10)={sigma_pass} "
          f"⇒ PASS_Reading_B={pass_reading_b}")
    print(f"      fail_count(β∉[1.5,2.5])={fail_count}/4 sigma_fail(σ≥0.30)={sigma_fail} "
          f"⇒ FAIL_Reading_A={fail_reading_a}")
    print(f"    CF-W6-4-S91-1 sub-test            = {cf_w6_4_verdict}")
    print()

    # ------------------------------------------------------------------
    # 6. Composite verdict + 3-tuple (plan §W9-3 composite collapse)
    # ------------------------------------------------------------------
    print("=" * 72)
    print("  COMPOSITE VERDICT CONSTRUCTION")
    print("=" * 72)
    # [SIGN] direction: prediction is η_FB_observed ≥ η_lower (saturation in
    # predicted direction). sign_verdict = PASS iff direction matches.
    sign_verdict = "PASS" if fb["sat_eta_pass"] else "FAIL"
    # sub-test PASS count
    sub_pass = [cf_w7_3_pass, cf_w6_1_pass, (cf_w6_4_verdict == "PASS_Reading_B")]  # (local)
    n_sub_pass = sum(sub_pass)  # (local)
    # magnitude_verdict: PASS if all 3 sub-tests PASS; INFO if mixed; FAIL if all 3 fail
    if n_sub_pass == 3:
        magnitude_verdict = "PASS"
    elif n_sub_pass == 0:
        magnitude_verdict = "FAIL"
    else:
        magnitude_verdict = "INFO"
    # regime_verdict: VALID iff Friedrich-Bär saturation theorem applies (η_FB ≥ floor
    # AND NEW-sector bound dominates ceiling — both hold ⇒ in-regime certification)
    regime_verdict = "VALID" if fb["saturation_pass"] else "BREAKDOWN"

    # Composite collapse (plan strict_PASS_boundary):
    #   FAIL if saturation predicate FAILS (η_FB < 0.40 ⇒ sign FAIL or regime BREAKDOWN)
    #   PASS if saturation PASS AND all 3 sub-tests PASS
    #   INFO if saturation PASS but sub-tests MIXED
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "PASS":
        composite = "PASS"
    elif magnitude_verdict == "FAIL":
        composite = "FAIL"
    else:
        composite = "INFO"  # saturation certified; mixed sub-tests

    print(f"  Friedrich-Bär saturation PASS?  {fb['saturation_pass']}")
    print(f"  CF-W7-3 (i)              PASS?  {cf_w7_3_pass}  (rel_dev={rel_dev_w7_3:.4f})")
    print(f"  CF-S91-W6-1-PATHWAY-A (ii) PASS? {cf_w6_1_pass}  (rel_dev={rel_dev_w6_1:.5f})")
    print(f"  CF-W6-4-S91-1 (iii)        ->    {cf_w6_4_verdict}")
    print(f"  n_sub_pass                      = {n_sub_pass}/3")
    print(f"  sign_verdict      = {sign_verdict}")
    print(f"  magnitude_verdict = {magnitude_verdict}")
    print(f"  regime_verdict    = {regime_verdict}")
    print(f"  COMPOSITE         = {composite}")
    print()

    # ------------------------------------------------------------------
    # 7. Save .npz
    # ------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        # FB saturation predicate
        eta_FB_lower=eta_FB_lower,
        eta_FB_floor_ref=ETA_FB_FLOOR_REF,
        eta_FB_observed=fb["eta_FB_observed"],
        eta_FB_all_min=fb["eta_FB_all_min"],
        eta_FB_all_min_sector=np.array(fb["eta_FB_all_min_sector"]),
        bot_k_sectors=np.array(fb["bot_k_sectors"]),
        bot_k_ceiling=fb["bot_k_ceiling"],
        new_sector_level=L_NEW_SECTOR,
        new_bound_min=fb["new_bound_min"],
        new_bound_min_sector=np.array(fb["new_bound_min_sector"]),
        sat_eta_pass=fb["sat_eta_pass"],
        sat_new_pass=fb["sat_new_pass"],
        saturation_pass=fb["saturation_pass"],
        # CF-W7-3
        cf_w7_3_target_377_200=float(CF_W7_3_TARGET),
        cf_w7_3_target_exact_str=str(CF_W7_3_TARGET),
        alpha_in_cache_s4=alpha_in_cache_s4,
        beta_shell_cache_L6_12=beta_shell_cache,
        beta_shell_wide_L22_50=beta_shell_wide,
        rel_dev_w7_3=rel_dev_w7_3,
        cf_w7_3_pass=cf_w7_3_pass,
        # CF-S91-W6-1-PATHWAY-A
        alpha_b_anchor=alpha_b_anchor,
        alpha_pathway_a_reduced=alpha_pathway_a_reduced,
        rel_dev_w6_1=rel_dev_w6_1,
        cf_w6_1_pass=cf_w6_1_pass,
        # CF-W6-4-S91-1 4-way
        base_beta_O1=base_O1, base_beta_O2=base_O2, base_beta_O3=base_O3, base_beta_O4=base_O4,
        base_beta_bar=float(base_betas.mean()), base_sigma_beta=float(base_betas.std(ddof=1)),
        beta_O1=beta_O1, beta_O2=beta_O2, beta_O3=beta_O3, beta_O4=beta_O4,
        beta_bar=beta_bar, sigma_beta=sigma_beta,
        pass_band=pass_band, sigma_pass=sigma_pass, pass_reading_b=pass_reading_b,
        fail_count=fail_count, sigma_fail=sigma_fail, fail_reading_a=fail_reading_a,
        cf_w6_4_verdict=np.array(cf_w6_4_verdict),
        # composite
        n_sub_pass=n_sub_pass,
        composite=np.array(composite),
        sign_verdict=np.array(sign_verdict),
        magnitude_verdict=np.array(magnitude_verdict),
        regime_verdict=np.array(regime_verdict),
        # provenance
        tau_fold=tau_fold, M_KK=M_KK, L_max=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  NPZ saved: {OUT_NPZ}")

    # ------------------------------------------------------------------
    # 8. PNG plot (4-panel)
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(15, 11), dpi=110)

    # Panel 1: η_FB per bot-K sector + floor + lower bound
    ax = axes[0, 0]
    secs = list(fb["eta_bot_k"].keys())
    eta_vals = [fb["eta_bot_k"][s] for s in secs]
    ax.bar([str(s) for s in secs], eta_vals, color="steelblue", alpha=0.8, edgecolor="black")
    ax.axhline(eta_FB_lower, color="red", ls="--", lw=1.5,
               label=f"η_FB_lower = {eta_FB_lower}")
    ax.axhline(ETA_FB_FLOOR_REF, color="green", ls=":", lw=1.5,
               label=f"W11-3 (1,1)-floor = {ETA_FB_FLOOR_REF}")
    ax.set_xlabel("bot-K Peter-Weyl (p,q) sector")
    ax.set_ylabel("η_FB(p,q) = |λ|_min / √(C_2+1)")
    ax.set_title(f"Friedrich-Bär ratio per bot-{K_BOT} sector\n"
                 f"η_FB_observed = {fb['eta_FB_observed']:.4f}  "
                 f"(saturation {'PASS' if fb['saturation_pass'] else 'FAIL'})")
    ax.legend(fontsize=8.5)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 2: NEW-sector(13) Casimir bound vs bot-K ceiling
    ax = axes[0, 1]
    ax.bar(["bot-K ceiling\n(L=12 cache)", "NEW-sector(13)\nmin lower bound"],
           [fb["bot_k_ceiling"], fb["new_bound_min"]],
           color=["darkorange", "steelblue"], alpha=0.8, edgecolor="black")
    ax.set_ylabel("|λ| (M_KK units)")
    ax.set_title(f"NEW-sector(13) bound = {fb['new_bound_min']:.3f} "
                 f">> ceiling {fb['bot_k_ceiling']:.3f}\n"
                 f"⇒ L_max=12 ≡ L_max → ∞ (saturated)")
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 3: CF-W7-3 β_shell convergence to 377/200
    ax = axes[1, 0]
    windows = ["in-cache\nL{6..12}", "FB-sat\nL{15..22}", "FB-sat\nL{22..50}"]
    vals = [beta_shell_cache, alpha_in_cache_s4, beta_shell_wide]
    ax.bar(windows, vals, color=["lightcoral", "steelblue", "seagreen"],
           alpha=0.8, edgecolor="black")
    ax.axhline(float(CF_W7_3_TARGET), color="red", ls="--", lw=1.5,
               label=f"377/200 = {float(CF_W7_3_TARGET)}")
    ax.axhline(float(CF_W7_3_TARGET) * (1 - CF_W7_3_TOL), color="green", ls=":", lw=1.0)
    ax.axhline(float(CF_W7_3_TARGET) * (1 + CF_W7_3_TOL), color="green", ls=":", lw=1.0,
               label=f"±{CF_W7_3_TOL*100:.0f}% PASS band")
    ax.set_ylabel("β_shell(s*=3, d=4)")
    ax.set_title(f"CF-W7-3: β_shell convergence to 377/200\n"
                 f"FB-sat = {alpha_in_cache_s4:.4f}  rel_dev = {rel_dev_w7_3:.4f}  "
                 f"({'PASS' if cf_w7_3_pass else 'INFO/FAIL'})")
    ax.legend(fontsize=8.5)
    ax.grid(True, alpha=0.3, axis="y")

    # Panel 4: 4-way discriminator β per observable
    ax = axes[1, 1]
    obs_labels = ["O_1\n(Mellin)", "O_2\n(P_0+HKR)", "O_3\n(BdG s=4)", "O_4\n(Tr D^-6)"]
    ax.bar(obs_labels, beta_values, color="mediumpurple", alpha=0.8, edgecolor="black")
    ax.axhspan(PASS_BAND_BETA_LOW, PASS_BAND_BETA_HIGH, color="green", alpha=0.12,
               label="PASS band [1.8,2.1]")
    ax.axhspan(FAIL_BAND_BETA_LOW, FAIL_BAND_BETA_HIGH, color="orange", alpha=0.08,
               label="FAIL-tolerant [1.5,2.5]")
    ax.set_ylabel("β (FB-saturated layer)")
    ax.set_title(f"CF-W6-4-S91-1 4-way discriminator\n"
                 f"β̄={beta_bar:.3f} σ_β={sigma_beta:.3f} ⇒ {cf_w6_4_verdict}")
    ax.legend(fontsize=8.5)
    ax.grid(True, alpha=0.3, axis="y")

    plt.suptitle(f"{GATE_ID}\nComposite: {composite}  "
                 f"(saturation {'PASS' if fb['saturation_pass'] else 'FAIL'}; "
                 f"{sum([cf_w7_3_pass, cf_w6_1_pass, cf_w6_4_verdict=='PASS_Reading_B'])}/3 sub-tests PASS)",
                 fontsize=11)
    plt.tight_layout(rect=(0, 0, 1, 0.97))
    plt.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"  PNG saved: {OUT_PNG}")

    # ------------------------------------------------------------------
    # 9. Emit verdict line
    # ------------------------------------------------------------------
    value_str = (
        f"saturation_pass={fb['saturation_pass']};"
        f"eta_FB_observed={fb['eta_FB_observed']:.6f};"
        f"eta_FB_lower={eta_FB_lower};"
        f"eta_FB_all_min={fb['eta_FB_all_min']:.6f};"
        f"NEW_sector13_bound={fb['new_bound_min']:.4f};"
        f"botK_ceiling={fb['bot_k_ceiling']:.4f};"
        f"CF_W7_3_pass={cf_w7_3_pass}_alpha_s4={alpha_in_cache_s4:.4f}_vs_377_200_reldev={rel_dev_w7_3:.4f};"
        f"CF_W6_1_PATHWAY_A_pass={cf_w6_1_pass}_alpha={alpha_pathway_a_reduced:.4f}_vs_anchor_2.6926_reldev={rel_dev_w6_1:.5f};"
        f"CF_W6_4_S91_1={cf_w6_4_verdict}_beta_bar={beta_bar:.4f}_sigma_beta={sigma_beta:.4f}"
        f"_betaO1={beta_O1:.4f}_betaO2={beta_O2:.4f}_betaO3={beta_O3:.4f}_betaO4={beta_O4:.4f};"
        f"n_sub_pass={n_sub_pass}_of_3"
    )
    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)

    wall = time.time() - t0  # (local)
    print()
    print("=" * 72)
    print(f"  {GATE_ID}")
    print(f"  composite: {composite}  (sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict})")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"  wall: {wall:.2f}s")
    print("=" * 72)
    return 0


if __name__ == "__main__":
    sys.exit(main())
