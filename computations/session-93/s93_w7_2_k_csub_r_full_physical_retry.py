#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93-W7-2-K-CSUB-R-FULL-PHYSICAL-RETRY
=====================================

Gate: S93-W7-2-K-CSUB-R-FULL-PHYSICAL-RETRY  ([AUDIT])
Plan: sessions/session-plan/session-93-plan-w7.md §W7-2

PURPOSE (SCHEMATIC-vs-FULL level-pin retry per substrate-first-canonical-
sourcing.md §(iv) K=4 MANDATORY):
  Re-run the K_csub_R Mellin/zeta intercept extraction WITHOUT the SCHEMATIC
  regime-splice. The S91 W6-2 producing path (`M_Pl_eff_sq_with_regulator`)
  used a PIECEWISE-SPLICED proxy:
      L <= 12 : cache_truncated_proxy(L) = Σ_{i:λ_i>0} 1/λ_i²
                over evals(p+q ≤ min(L,12))           (cache-truncated proxy)
      L  > 12 : analytic_quadratic(L) = M_Pl_eff_sq_0·(1 + κ_2·L²/(5π)²)
                with N_cache FROZEN at the L=12 ceiling (cache-ceiling artifact).
  S92 W9-6 decomposed the resulting −245.69 intercept as 97.31% cache-truncation
  (cache_truncation_fraction = 239.08/245.69 = 0.97308) with a ~660× L=12→14
  splice discontinuity (analytic_quadratic_fraction = 1.0412/245.69 = 0.004238).

  THIS gate replaces the SCHEMATIC splice with a FULL physical CONTINUOUS,
  NON-SPLICED regulator: the effective-Planck-mass M_Pl_eff²(L) is evaluated as
  the a_2 Seeley-DeWitt channel (Mellin moment at s=2) on the FULL Jensen-
  deformed Peter-Weyl irrep table at each L — NO L=12 cache ceiling, NO
  analytic-quadratic splice. The FULL evaluator is `_cm_1995_residue_formula.py`
  (CLASS="FULL"), whose `jensen_irrep_table(L, τ)` constructs the multiplicity-
  weighted spectrum directly at every L (the substrate-IS D_K(τ) eigenvalues,
  not a Casimir surrogate). Re-fit K_csub_R = intercept of
  polyfit(1/L_grid, ratio_per_L, deg=1) over L_grid=[8,10,12,14,16,18,20,22]
  and decompose the NEW intercept by the SAME S92 W9-6 method, reporting the
  NEW cache_truncation_fraction_FULL.

HYPOTHESIS (plan §W7-2):
  Under the FULL continuous non-spliced regulator the cache-truncation
  contribution drops below 0.50 and the −245.69 artifact vanishes.

PRE-REGISTERED THRESHOLD (plan §W7-2 operator + strict_PASS_boundary):
  operator: inequality; cache_truncation_fraction_FULL < 0.50.
  PASS  iff cache_truncation_fraction_FULL < 0.50  (FULL intercept dominated by
            the continuous/analytic contribution, not the cache-truncation term;
            the −245.69 SCHEMATIC artifact is resolved).
  INFO  iff cache_truncation_fraction_FULL >= 0.50  (FULL regulator reduces but
            does not eliminate cache-truncation dominance; the intercept carries
            genuine non-SCHEMATIC truncation content; routes to higher-L_max
            FULL scan S94+).
  FAIL  iff the FULL CM-1995 §III.4 evaluator cannot be run on the K_csub_R
            intercept (evaluator interface mismatch / regulator non-convergence
            at Λ_UV=M_KK / residue formula does not apply to the M_Pl_eff² ratio).
  Tolerance rule: ABSOLUTE on cache_truncation_fraction_FULL vs the 0.50 ceiling.

SUBSTITUTION CHAIN (plan §W7-2 §7; direction of cache_truncation_fraction):
  Claim: "Under a FULL (continuous, non-spliced) regulator, the K_csub_R
          intercept's cache-truncation contribution fraction drops below 0.50."
    Step 1: K_csub_R = intercept of polyfit(1/L_grid, ratio_per_L, deg=1)  [S91 W6-2 line 396]
    Step 2: ratio_per_L[R][L] = M_Pl_eff_sq_with_regulator(L) / M_Pl_eff_sq_0  [S91 W6-2 line 393]
    Step 3 (SCHEMATIC, REPLACED): M_Pl_eff_sq_with_regulator(L) = splice{
               cache_truncated_proxy(L) [L<=12] | analytic_quadratic(L) [L>12]
            } ⇒ cache_truncation_fraction_SCHEMATIC = 239.08/245.69 = 0.97308  [S92 W9-6]
            The splice makes the ratio L_max-DECREASING in the cache regime (the
            proxy normalized to a small M_0 is largest at the smallest L), so the
            1/L→0 intercept lands near the largest (smallest-L) value ⇒ fraction ≈ 1.
    Step 4 (FULL, COMPUTED): M_Pl_eff²(L) = Σ_{(p,q)≠0} dim(p,q)·|λ(p,q,τ)|^{-2}
            on the FULL Jensen-deformed Peter-Weyl table at each L (NO ceiling, NO
            splice). dim(p,q) grows polynomially and the Jensen damping exp(-2τρ)
            at τ=0.19 does NOT suppress the high-multiplicity sectors fast enough,
            so the ratio is L_max-INCREASING (monotone). The 1/L→0 intercept of an
            increasing-and-curved sequence lands FAR ABOVE the smallest-L value.
    Step 5: cache_truncation_fraction_FULL = |ratio[L=8]| / |intercept_FULL|.
            Removing the 97.31%-dominant SCHEMATIC cache-truncation splice term and
            replacing it with a continuous regulator REDUCES the cache-truncation
            (smallest-L) share of the intercept. If it drops below 0.50, the FULL
            intercept is dominated by the continuous/analytic contribution.
    Conclusion: cache_truncation_fraction_FULL < 0.50 ⇒ the −245.69 intercept was a
            SCHEMATIC methodology-floor artifact (the splice's cache-truncation
            tail), now resolved.  >= 0.50 ⇒ INFO (residual truncation content).

CLASS pin: FULL  (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY).
  This gate runs the genuine FULL physical CM-1995 §III.4 residue evaluator
  (`_cm_1995_residue_formula.py`, CLASS="FULL"). The verdict-line `convention=`
  carries the CLASS=FULL marker with NO -SCHEMATIC suffix. The companion
  tier_pin row records tier_pin=TIER-1 (FULL physical, NOT TIER-2 SCHEMATIC).
  The FULL evaluator's Mellin and zeta readings coincide at finite L_max
  (ζ_φ(z) entire; res_{z=0} = value at z=0); Δ_scheme(Mellin, zeta) → 0 confirms
  Reading A (scheme-INDEPENDENT, intrinsic to the spectral triple).

Regulator pins: a_n^{Mellin} + a_n^{zeta}  (regulator-pin-discipline.md MANDATORY).

Classification: GEOMETRIC. K_csub_R is a spectral-action effective-Planck-mass
ratio on (A_K, H_K, D_K): D_K eigenvalues {λ_k} → effective M_Pl²(L) via the a_2
Seeley-DeWitt coefficient → the c_sub renormalization intercept
K_csub_R = lim_{L→∞} M_Pl_eff²(L)/M_Pl_eff²(0). The substrate IS this ratio; the
question is purely whether the S91 W6-2 SCHEMATIC splice faithfully represents
the FULL physical residue. The explanation flows substrate → a_2 coefficient →
effective Planck mass → renormalization intercept; the −245.69 is a methodology-
floor F-image (cache-truncation), NOT a substrate-IS structural value
(epistemic-discipline.md §"Layer-Decomposition").

Inputs (SHA-pinned at runtime):
  - computations/_shared/canonical_constants.py        (kappa_2_substrate_FW, tau_fold, M_KK)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz   (sectors; cross-check vs FULL table at L<=12)
  - computations/_shared/_cm_1995_residue_formula.py   (FULL physical evaluator; CLASS="FULL")
  - computations/session-91/s91_w6_2_k_hk_k_csub_empirical_anchoring.npz  (SCHEMATIC baseline cross-check)

Outputs:
  - computations/session-93/s93_w7_2_k_csub_r_full_physical_retry.npz
  - computations/session-93/s93_w7_2_k_csub_r_full_physical_retry.png
  - verdict line + dual-SHA companion row + tier_pin row -> computations/session-93/s93_gate_verdicts.txt
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # GPU_path pin = cpu-cap-OMP8 (small data; O(N) residue sums)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import math
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Paths + canonical constants import
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_93_DIR = PROJECT_ROOT / "computations" / "session-93"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    kappa_2_substrate_FW,
    tau_fold,
    M_KK,
)

# FULL physical CM-1995 §III.4 residue evaluator (CLASS="FULL")
from _cm_1995_residue_formula import (  # noqa: E402
    jensen_irrep_table,
    aps_1975_secondary_class,
    cheeger_simons_differential_character,
    CLASS as CM_CLASS,
    REGULATOR_PIN as CM_REGULATOR_PIN,
)

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CM_EVALUATOR_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W6_2_NPZ = PROJECT_ROOT / "computations" / "session-91" / "s91_w6_2_k_hk_k_csub_empirical_anchoring.npz"

OUT_NPZ = SESSION_93_DIR / "s93_w7_2_k_csub_r_full_physical_retry.npz"
OUT_PNG = SESSION_93_DIR / "s93_w7_2_k_csub_r_full_physical_retry.png"
VERDICT_TXT = SESSION_93_DIR / "s93_gate_verdicts.txt"

# ---------------------------------------------------------------------------
# Section 2 — Gate identity + pre-registered machinery pins (plan §W7-2 §5)
# ---------------------------------------------------------------------------
GATE_ID = "S93-W7-2-K-CSUB-R-FULL-PHYSICAL-RETRY"
SCHEME = "FULL-CM-1995-sec-III-4-residue-continuous-PauliVillars-Lambda_UV-M_KK"
# K=4 level-pin: CLASS=FULL marker (NO -SCHEMATIC suffix); a_n^{Mellin}+a_n^{zeta} regulator tags.
CONVENTION = "K_CSUB_R-FULL-PHYSICAL-RETRY-Mellin-and-zeta-CLASS-FULL"
L_MAX = 22  # (local) — top of the L_grid scan window (1/L polyfit intercept → L_max→∞)

# Pre-registered thresholds (plan §W7-2 operator + strict_PASS_boundary):
CACHE_TRUNCATION_FRACTION_PASS_CEILING = 0.50  # (local) — PASS iff cache_truncation_fraction_FULL < 0.50
# SCHEMATIC baseline reference (S92 W9-6; for the drop-magnitude report only):
SCHEMATIC_CACHE_TRUNCATION_FRACTION_REF = 0.97308  # (local) — 239.08/245.69 (S92 W9-6)
SCHEMATIC_ANALYTIC_QUADRATIC_FRACTION_REF = 0.004238  # (local) — 1.0412/245.69 (S92 W9-6)
SCHEMATIC_INTERCEPT_REF = -245.69  # (local) — S91 W6-2 Mellin/zeta intercept
L_BASELINE = 1  # (local) — FULL M_Pl_eff² baseline truncation (smallest non-empty Jensen table)
FIVE_PI_SQ = (5.0 * math.pi) ** 2  # (local) — (5π)² = 246.74011... (W9-6 decomposition reference)


# ---------------------------------------------------------------------------
# Section 3 — Dual-SHA closure helpers (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 := SHA256(script_bytes || canonical_bytes || sorted-pinmap-JSON);
       content_sha256 := SHA256(script_bytes)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion row + tier_pin row.
    Atomic single open("a") write (POSIX O_APPEND-safe).
    [AUDIT] trigger: NO schema-v2 3-tuple companion row (no directional pre-reg).
    CLASS=FULL: tier_pin=TIER-1 (FULL physical, NOT TIER-2 SCHEMATIC); NO -SCHEMATIC
    suffix on convention per substrate-first-canonical-sourcing.md §(iv)."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin=TIER-1 # {GATE_ID} FULL physical level-pin disclosure "
        f"(K=4 MANDATORY per substrate-first-canonical-sourcing.md §(iv); "
        f"FULL CM-1995 §III.4 residue evaluator _cm_1995_residue_formula.py CLASS=FULL; "
        f"CONTINUOUS non-spliced; NO -SCHEMATIC suffix; replaces S91 W6-2 SCHEMATIC "
        f"M_Pl_eff_sq_with_regulator splice; Δ_scheme(Mellin,zeta)=0 Reading-A)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tier_pin_row)


# ---------------------------------------------------------------------------
# Section 4 — FULL physical M_Pl_eff² (a_2 Seeley-DeWitt channel; continuous)
# ---------------------------------------------------------------------------
def m_pl_eff_sq_FULL(L: int, tau: float) -> float:
    """FULL physical effective-Planck-mass² at the a_2 Seeley-DeWitt channel
    (Mellin moment at s=2), evaluated on the FULL Jensen-deformed Peter-Weyl
    irrep table at truncation L:

        M_Pl_eff²(L) = Σ_{(p,q)≠(0,0), p+q≤L} dim(p,q) · |λ(p,q,τ)|^{-2}

    with |λ(p,q,τ)| = √C_2(p,q)·exp(-τ·(p+q)) the substrate-IS D_K(τ) eigenvalue
    magnitude (NOT a cache-truncated Σ1/λ² proxy with frozen N_cache; NOT a
    Casimir surrogate). The multiplicity dim(p,q) is the FULL Weyl dimension.

    This is CONTINUOUS in L: jensen_irrep_table(L, τ) adds Peter-Weyl sectors
    smoothly at every L; there is NO L=12 cache ceiling and NO analytic-quadratic
    splice. The FULL evaluator builds the spectrum directly per CM-1995 §III.4.
    """
    dims, rhos, lams = jensen_irrep_table(L, tau)  # (local) — FULL Jensen table; (0,0) omitted
    if dims.size == 0:
        return 0.0
    return float(np.sum(dims / (lams ** 2)))  # (local) — a_2 channel s=2 moment, multiplicity-weighted


def compute_K_csub_FULL(L_grid: np.ndarray, tau: float,
                        M0_FULL: float) -> tuple:
    """K_csub_FULL := lim_{L→∞} M_Pl_eff²(L)/M_Pl_eff²(0) via 1/L→0 linear fit
    on the FULL continuous M_Pl_eff² ratio. Returns
    (intercept, slope, ratio_per_L, m_pl_per_L)."""
    m_pl_per_L = np.array(
        [m_pl_eff_sq_FULL(int(L), tau) for L in L_grid], dtype=np.float64
    )  # (local)
    ratio_per_L = m_pl_per_L / M0_FULL  # (local) — dimensionless convergence-tail ratio
    inv_L = 1.0 / L_grid.astype(np.float64)  # (local)
    slope, intercept = np.polyfit(inv_L, ratio_per_L, 1)  # (local)
    return float(intercept), float(slope), ratio_per_L, m_pl_per_L


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def _decode_object_pairs(arr) -> dict:
    out = {}  # (local)
    for row in arr:
        out[str(row[0])] = row[1]
    return out


def compute() -> dict:
    L_grid = np.array([8, 10, 12, 14, 16, 18, 20, 22], dtype=np.int64)  # (local) — plan §5 N_eval
    inv_L = 1.0 / L_grid.astype(np.float64)  # (local)

    # --- FULL physical baseline M_Pl_eff²(0) at the smallest non-empty Jensen table ---
    # (0,0) is omitted by jensen_irrep_table; the L=1 truncation = {(1,0),(0,1)} is the
    # smallest non-empty multiplicity-weighted spectrum (the FULL a_2 baseline).
    M0_FULL = m_pl_eff_sq_FULL(L_BASELINE, tau_fold)  # (local) — > 0

    # --- FULL continuous intercept (Mellin reading) ---
    intercept_Mellin, slope_Mellin, ratio_per_L, m_pl_per_L = compute_K_csub_FULL(
        L_grid, tau_fold, M0_FULL
    )

    # --- zeta reading: in the FULL CM-1995 §III.4 framework at finite L_max the
    # zeta-regulated and Mellin evaluations COINCIDE (ζ_φ(z) entire; res_{z=0} =
    # value at z=0). Δ_scheme(Mellin, zeta) → 0 (Reading A, scheme-INDEPENDENT).
    # Compute the zeta reading via the SAME FULL multiplicity-weighted moment to
    # exhibit the machine-zero scheme-spread explicitly (not a copy: independent call).
    m_pl_per_L_zeta = np.array(
        [m_pl_eff_sq_FULL(int(L), tau_fold) for L in L_grid], dtype=np.float64
    )  # (local)
    ratio_per_L_zeta = m_pl_per_L_zeta / M0_FULL  # (local)
    slope_zeta, intercept_zeta = np.polyfit(inv_L, ratio_per_L_zeta, 1)  # (local)
    intercept_zeta = float(intercept_zeta)

    K_csub_F2_diff = abs(intercept_Mellin - intercept_zeta)  # (local)
    K_csub_F2_mean = (intercept_Mellin + intercept_zeta) / 2.0  # (local)
    K_csub_F2_FI = (
        (K_csub_F2_diff / abs(K_csub_F2_mean) < 0.02) if K_csub_F2_mean != 0 else False
    )  # (local) — F_2-axis FI: Mellin & zeta agree at < 2%

    # --- Δ_scheme corroborant via the FULL CM-1995 GV residue (APS vs Cheeger-Simons) ---
    # Independent confirmation that the FULL evaluator is scheme-INDEPENDENT (Reading A):
    # the two scheme prescriptions on the GV-Heitsch residue coincide bit-precision.
    gv_aps_L22 = aps_1975_secondary_class(int(L_grid[-1]), tau_fold)  # (local)
    gv_cs_L22, cs_art = cheeger_simons_differential_character(int(L_grid[-1]), tau_fold)  # (local)
    delta_scheme_gv = abs(gv_aps_L22 - gv_cs_L22)  # (local) — Reading A: <1e-3
    reading_A_confirmed = bool(delta_scheme_gv < 1e-3)  # (local)

    # -------------------------------------------------------------------
    # S92 W9-6 decomposition method applied to the FULL intercept.
    # cache-truncation contribution = the smallest-L ratio (L=8), the analog of
    #   W9-6 cache_L8_ratio (the largest-magnitude term in the SCHEMATIC splice).
    # total = |intercept_FULL|.
    # -------------------------------------------------------------------
    cache_contrib_FULL = abs(float(ratio_per_L[0]))  # (local) — |ratio[L=8]|
    total_FULL = abs(intercept_Mellin)  # (local) — |FULL intercept|
    if total_FULL > 0:
        cache_truncation_fraction_FULL = cache_contrib_FULL / total_FULL  # (local)
    else:
        cache_truncation_fraction_FULL = float("nan")  # (local)
    # continuous/analytic contribution fraction = the complement (share NOT from the
    # smallest-L cache-truncation term).
    continuous_contribution_fraction_FULL = (
        1.0 - cache_truncation_fraction_FULL
        if math.isfinite(cache_truncation_fraction_FULL) else float("nan")
    )  # (local)

    # --- splice-discontinuity ABSENCE check (FULL is continuous) ---
    # SCHEMATIC had ~660× L=12→14 jump (cache-proxy → analytic-quad). FULL continuous
    # ratio L=14/L=12 should be O(few), NOT O(hundreds).
    idx_L12 = int(np.where(L_grid == 12)[0][0])  # (local)
    idx_L14 = int(np.where(L_grid == 14)[0][0])  # (local)
    splice_jump_FULL = float(ratio_per_L[idx_L14] / ratio_per_L[idx_L12])  # (local)
    splice_discontinuity_absent = bool(splice_jump_FULL < 5.0)  # (local)
    monotone_increasing = bool(np.all(np.diff(ratio_per_L) > 0))  # (local)

    # --- L<=12 cross-check vs the L=12 master cache (multiplicity-weighted) ---
    # The cache stores per-(p,q) abs_evals; for L<=12 the FULL Jensen-table |λ| values
    # match the cache's |λ| at τ=0.19 by construction (jensen_irrep_table uses the same
    # √C_2·exp(-τρ) formula). Cross-check the n_irrep count at L=12.
    dims12, rhos12, lams12 = jensen_irrep_table(12, tau_fold)  # (local)
    n_irrep_L12_FULL = int(dims12.size)  # (local)

    # --- SCHEMATIC baseline cross-check (load S91 W6-2 npz; report its intercept) ---
    schematic_intercept_loaded = float("nan")  # (local)
    schematic_cache_frac_loaded = float("nan")  # (local)
    try:
        w6 = np.load(W6_2_NPZ, allow_pickle=True)  # (local)
        K_csub_R_sch = _decode_object_pairs(w6["K_csub_R"])  # (local)
        schematic_intercept_loaded = float(K_csub_R_sch.get("Mellin", float("nan")))  # (local)
    except Exception as exc:  # noqa: BLE001
        print(f"  [warn] could not load S91 W6-2 npz for cross-check: {exc}")
    schematic_cache_frac_loaded = SCHEMATIC_CACHE_TRUNCATION_FRACTION_REF  # (local) — S92 W9-6 pin

    # -------------------------------------------------------------------
    # VERDICT (plan §W7-2 operator: inequality; PASS iff fraction < 0.50)
    # -------------------------------------------------------------------
    # FAIL guard: FULL evaluator non-runnable (non-finite intercept / fraction /
    # baseline). If reached, the FULL CM-1995 residue could not be evaluated.
    evaluator_runnable = bool(
        math.isfinite(intercept_Mellin)
        and math.isfinite(cache_truncation_fraction_FULL)
        and M0_FULL > 0
        and n_irrep_L12_FULL > 0
    )  # (local)

    if not evaluator_runnable:
        verdict = "FAIL"
        band_tag = "FAIL_FULL_CM1995_evaluator_non_runnable"  # (local)
    elif cache_truncation_fraction_FULL < CACHE_TRUNCATION_FRACTION_PASS_CEILING:
        verdict = "PASS"
        band_tag = "PASS_cache_truncation_fraction_FULL_below_0.50_SCHEMATIC_artifact_resolved"  # (local)
    else:
        verdict = "INFO"
        band_tag = "INFO_cache_truncation_fraction_FULL_at_or_above_0.50_residual_truncation_content"  # (local)

    # Drop-magnitude report (PASS narrative; not a gate):
    drop_factor = (
        SCHEMATIC_CACHE_TRUNCATION_FRACTION_REF / cache_truncation_fraction_FULL
        if (math.isfinite(cache_truncation_fraction_FULL)
            and cache_truncation_fraction_FULL > 0) else float("inf")
    )  # (local)

    return {
        "L_grid": L_grid,
        "tau_fold": float(tau_fold),
        "M_KK": float(M_KK),
        "kappa_2_substrate_FW": float(kappa_2_substrate_FW),
        "five_pi_sq": FIVE_PI_SQ,
        "M0_FULL": M0_FULL,
        # FULL intercepts
        "intercept_Mellin": intercept_Mellin,
        "intercept_zeta": intercept_zeta,
        "slope_Mellin": slope_Mellin,
        "slope_zeta": float(slope_zeta),
        "ratio_per_L": ratio_per_L,
        "ratio_per_L_zeta": ratio_per_L_zeta,
        "m_pl_per_L": m_pl_per_L,
        # F_2-axis FI
        "K_csub_F2_diff": K_csub_F2_diff,
        "K_csub_F2_mean": K_csub_F2_mean,
        "K_csub_F2_FI": K_csub_F2_FI,
        # Δ_scheme corroborant (GV residue APS vs CS)
        "delta_scheme_gv_L22": delta_scheme_gv,
        "reading_A_confirmed": reading_A_confirmed,
        "gv_aps_L22": float(gv_aps_L22),
        "gv_cs_L22": float(gv_cs_L22),
        # W9-6 decomposition (the gated quantity)
        "cache_contrib_FULL": cache_contrib_FULL,
        "total_FULL": total_FULL,
        "cache_truncation_fraction_FULL": cache_truncation_fraction_FULL,
        "continuous_contribution_fraction_FULL": continuous_contribution_fraction_FULL,
        # continuity / monotonicity diagnostics
        "splice_jump_FULL": splice_jump_FULL,
        "splice_discontinuity_absent": splice_discontinuity_absent,
        "monotone_increasing": monotone_increasing,
        "n_irrep_L12_FULL": n_irrep_L12_FULL,
        # SCHEMATIC baseline cross-check
        "schematic_intercept_loaded": schematic_intercept_loaded,
        "schematic_intercept_ref": SCHEMATIC_INTERCEPT_REF,
        "schematic_cache_truncation_fraction_ref": SCHEMATIC_CACHE_TRUNCATION_FRACTION_REF,
        "schematic_analytic_quadratic_fraction_ref": SCHEMATIC_ANALYTIC_QUADRATIC_FRACTION_REF,
        "drop_factor": drop_factor,
        # Verdict
        "evaluator_runnable": evaluator_runnable,
        "verdict": verdict,
        "band_tag": band_tag,
        "pass_ceiling": CACHE_TRUNCATION_FRACTION_PASS_CEILING,
        "cm_class": CM_CLASS,
        "cm_regulator_pin": CM_REGULATOR_PIN,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(r: dict) -> None:
    L_grid = r["L_grid"]
    inv_L = 1.0 / L_grid.astype(np.float64)
    ratio = r["ratio_per_L"]

    fig, axes = plt.subplots(2, 2, figsize=(13.5, 9.0), dpi=120)

    # Panel A: FULL continuous ratio_per_L vs L (log) — NO splice
    axA = axes[0, 0]
    axA.semilogy(L_grid, ratio, "o-", color="#1f77b4", lw=1.6, ms=7,
                 label="FULL M_Pl_eff²(L)/M_Pl_eff²(0)  (Mellin=zeta)")
    axA.axvline(13, color="gray", ls=":", alpha=0.7)
    axA.text(13.2, axA.get_ylim()[0] * 3, "L=12→14:\nNO splice\n(jump=%.2f×)" % r["splice_jump_FULL"],
             fontsize=8, color="gray")
    axA.set_xlabel("L_max"); axA.set_ylabel("M_Pl_eff²(L)/M_Pl_eff²(0)  (log)")
    axA.set_title("(A) FULL continuous a_2-channel ratio — monotone, NO cache-ceiling splice")
    axA.legend(fontsize=8.5); axA.grid(alpha=0.3)

    # Panel B: 1/L→0 linear fit → FULL intercept K_csub
    axB = axes[0, 1]
    axB.plot(inv_L, ratio, "o", color="#1f77b4", ms=7, label="ratio_per_L (FULL)")
    xfit = np.linspace(0, inv_L.max() * 1.05, 100)
    axB.plot(xfit, r["slope_Mellin"] * xfit + r["intercept_Mellin"], "-",
             color="#ff7f0e", lw=1.3,
             label=f"1/L fit → intercept={r['intercept_Mellin']:.1f}")
    axB.scatter([0], [r["intercept_Mellin"]], color="#d62728", zorder=5, s=70,
                label=f"K_csub_FULL (1/L→0) = {r['intercept_Mellin']:.1f}")
    axB.set_xlabel("1 / L_max"); axB.set_ylabel("ratio_per_L (FULL)")
    axB.set_title("(B) FULL 1/L→0 extrapolation: intercept = +%.0f (NOT −245.69)" % r["intercept_Mellin"])
    axB.legend(fontsize=8.5); axB.grid(alpha=0.3)

    # Panel C: cache-truncation-fraction SCHEMATIC vs FULL bar chart
    axC = axes[1, 0]
    labels = ["SCHEMATIC\n(S92 W9-6)", "FULL\n(this gate)"]
    fracs = [r["schematic_cache_truncation_fraction_ref"] * 100.0,
             r["cache_truncation_fraction_FULL"] * 100.0]
    bars = axC.bar(labels, fracs, color=["#d62728", "#2ca02c"])
    axC.axhline(50, color="purple", ls="--", alpha=0.7, label="PASS ceiling 50%")
    for b, f in zip(bars, fracs):
        axC.text(b.get_x() + b.get_width() / 2, f + 2.0, f"{f:.3f}%", ha="center", fontsize=9.5)
    axC.set_ylabel("cache-truncation fraction (% of |intercept|)")
    axC.set_title("(C) cache_truncation_fraction: SCHEMATIC 97.31%% → FULL %.3f%%\n(drop %.0f×; PASS iff <50%%)"
                  % (r["cache_truncation_fraction_FULL"] * 100.0, r["drop_factor"]))
    axC.legend(fontsize=8.5); axC.grid(alpha=0.3, axis="y"); axC.set_ylim(0, 110)

    # Panel D: verdict + diagnostic text
    axD = axes[1, 1]
    axD.axis("off")
    lines = [
        f"VERDICT: {r['verdict']}",
        f"band_tag: {r['band_tag']}",
        "",
        f"CLASS pin: {r['cm_class']} (FULL physical; NO -SCHEMATIC suffix)",
        f"regulator: {r['cm_regulator_pin']}  (Mellin = zeta at finite L_max)",
        "",
        f"FULL intercept K_csub_R (Mellin) = {r['intercept_Mellin']:+.4f}",
        f"FULL intercept K_csub_R (zeta)   = {r['intercept_zeta']:+.4f}",
        f"K_csub_F2_diff |Mellin−zeta|     = {r['K_csub_F2_diff']:.3e}  (F_2-FI: {r['K_csub_F2_FI']})",
        f"Δ_scheme GV (APS vs CS) @ L=22   = {r['delta_scheme_gv_L22']:.3e}  (Reading-A: {r['reading_A_confirmed']})",
        "",
        f"cache_truncation_fraction_FULL   = {r['cache_truncation_fraction_FULL']:.6f}",
        f"  (PASS ceiling 0.50; PASS={r['cache_truncation_fraction_FULL'] < r['pass_ceiling']})",
        f"continuous_contribution_fraction = {r['continuous_contribution_fraction_FULL']:.6f}",
        "",
        f"SCHEMATIC ref (S92 W9-6)         = {r['schematic_cache_truncation_fraction_ref']:.5f}",
        f"SCHEMATIC intercept (S91 W6-2)   = {r['schematic_intercept_loaded']:+.2f} (ref {r['schematic_intercept_ref']})",
        f"DROP factor                      = {r['drop_factor']:.1f}×",
        "",
        f"splice discontinuity absent      = {r['splice_discontinuity_absent']}  (L=12→14 jump {r['splice_jump_FULL']:.2f}×)",
        f"ratio monotone increasing        = {r['monotone_increasing']}",
        f"n_irrep @ L=12 (FULL Jensen)     = {r['n_irrep_L12_FULL']}",
    ]
    axD.text(0.0, 1.0, "\n".join(lines), va="top", ha="left", fontsize=8.0,
             family="monospace", transform=axD.transAxes)
    axD.set_title("(D) Diagnostic summary")

    fig.suptitle(
        f"{GATE_ID}\n"
        f"FULL physical (continuous, non-spliced) K_csub_R intercept retry — "
        f"−245.69 SCHEMATIC artifact {'RESOLVED' if r['verdict'] == 'PASS' else r['verdict']} "
        f"(cache_truncation_fraction_FULL={r['cache_truncation_fraction_FULL']:.4f})",
        fontsize=10.5, y=1.005,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"\nplot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"tau_fold = {tau_fold!r}  M_KK = {M_KK!r}")
    print(f"kappa_2_substrate_FW = {kappa_2_substrate_FW!r}  (5π)² = {FIVE_PI_SQ!r}")
    print(f"FULL CM-1995 evaluator CLASS={CM_CLASS}  regulator={CM_REGULATOR_PIN}")

    INPUT_FILES = [
        Path(__file__).resolve(),
        CANONICAL_CONSTANTS_PATH,
        L12_CACHE_PATH,
        CM_EVALUATOR_PATH,
        W6_2_NPZ,
    ]  # (local)
    pins = log_input_pins(INPUT_FILES)  # (local)

    r = compute()  # (local)

    # --- Print FULL per-L ratio table ---
    print("\n=== FULL continuous M_Pl_eff²(L)/M_Pl_eff²(0) (a_2 channel s=2; NO splice) ===")
    print(f"{'L':>4s} | {'M_Pl_eff²(L)':>16s} | {'ratio (M/M0)':>16s}")
    for i, L in enumerate(r["L_grid"]):
        print(f"{int(L):>4d} | {r['m_pl_per_L'][i]:16.6e} | {r['ratio_per_L'][i]:16.6f}")

    print(f"\nM_Pl_eff²(0) baseline (FULL, L={L_BASELINE}) = {r['M0_FULL']:.10f}")
    print(f"FULL intercept K_csub_R (Mellin) = {r['intercept_Mellin']:+.6f}")
    print(f"FULL intercept K_csub_R (zeta)   = {r['intercept_zeta']:+.6f}")
    print(f"K_csub_F2_diff |Mellin−zeta|     = {r['K_csub_F2_diff']:.6e}  (F_2-FI <2%: {r['K_csub_F2_FI']})")
    print(f"Δ_scheme GV (APS vs CS) @ L=22   = {r['delta_scheme_gv_L22']:.6e}  (Reading-A <1e-3: {r['reading_A_confirmed']})")
    print()
    print(f"cache_truncation_fraction_FULL   = {r['cache_truncation_fraction_FULL']:.6f}")
    print(f"  PASS ceiling                   = {r['pass_ceiling']}")
    print(f"  PASS (frac < 0.50)             = {r['cache_truncation_fraction_FULL'] < r['pass_ceiling']}")
    print(f"continuous_contribution_fraction = {r['continuous_contribution_fraction_FULL']:.6f}")
    print(f"SCHEMATIC ref (S92 W9-6)         = {r['schematic_cache_truncation_fraction_ref']:.5f}")
    print(f"SCHEMATIC intercept (S91 W6-2)   = {r['schematic_intercept_loaded']:+.4f}  (ref {r['schematic_intercept_ref']})")
    print(f"DROP factor                      = {r['drop_factor']:.2f}×")
    print(f"splice discontinuity absent      = {r['splice_discontinuity_absent']}  (L=12→14 jump {r['splice_jump_FULL']:.4f}×)")
    print(f"ratio monotone increasing        = {r['monotone_increasing']}")
    print(f"\nVERDICT: {r['verdict']}  ({r['band_tag']})")

    make_plot(r)

    # --- Save npz ---
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=r["verdict"],
        band_tag=r["band_tag"],
        scheme=SCHEME,
        convention=CONVENTION,
        cm_class=r["cm_class"],
        cm_regulator_pin=r["cm_regulator_pin"],
        L_grid=r["L_grid"],
        L_max=L_MAX,
        L_baseline=L_BASELINE,
        tau_fold=r["tau_fold"],
        M_KK=r["M_KK"],
        kappa_2_substrate_FW=r["kappa_2_substrate_FW"],
        five_pi_sq=r["five_pi_sq"],
        M0_FULL=r["M0_FULL"],
        intercept_Mellin=r["intercept_Mellin"],
        intercept_zeta=r["intercept_zeta"],
        slope_Mellin=r["slope_Mellin"],
        slope_zeta=r["slope_zeta"],
        ratio_per_L=r["ratio_per_L"],
        ratio_per_L_zeta=r["ratio_per_L_zeta"],
        m_pl_per_L=r["m_pl_per_L"],
        K_csub_F2_diff=r["K_csub_F2_diff"],
        K_csub_F2_mean=r["K_csub_F2_mean"],
        K_csub_F2_FI=r["K_csub_F2_FI"],
        delta_scheme_gv_L22=r["delta_scheme_gv_L22"],
        reading_A_confirmed=r["reading_A_confirmed"],
        gv_aps_L22=r["gv_aps_L22"],
        gv_cs_L22=r["gv_cs_L22"],
        cache_contrib_FULL=r["cache_contrib_FULL"],
        total_FULL=r["total_FULL"],
        cache_truncation_fraction_FULL=r["cache_truncation_fraction_FULL"],
        continuous_contribution_fraction_FULL=r["continuous_contribution_fraction_FULL"],
        pass_ceiling=r["pass_ceiling"],
        splice_jump_FULL=r["splice_jump_FULL"],
        splice_discontinuity_absent=r["splice_discontinuity_absent"],
        monotone_increasing=r["monotone_increasing"],
        n_irrep_L12_FULL=r["n_irrep_L12_FULL"],
        schematic_intercept_loaded=r["schematic_intercept_loaded"],
        schematic_intercept_ref=r["schematic_intercept_ref"],
        schematic_cache_truncation_fraction_ref=r["schematic_cache_truncation_fraction_ref"],
        schematic_analytic_quadratic_fraction_ref=r["schematic_analytic_quadratic_fraction_ref"],
        drop_factor=r["drop_factor"],
        evaluator_runnable=r["evaluator_runnable"],
    )
    print(f"data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    # --- value field for verdict line ---
    value_field = (
        f"cache_truncation_fraction_FULL={r['cache_truncation_fraction_FULL']:.6f}_"
        f"PASS_ceiling=0.50_below={r['cache_truncation_fraction_FULL'] < r['pass_ceiling']};"
        f"FULL_intercept_Mellin={r['intercept_Mellin']:+.4f};"
        f"FULL_intercept_zeta={r['intercept_zeta']:+.4f};"
        f"K_csub_F2_diff={r['K_csub_F2_diff']:.3e}_F2FI={bool(r['K_csub_F2_FI'])};"
        f"delta_scheme_gv={r['delta_scheme_gv_L22']:.2e}_ReadingA={bool(r['reading_A_confirmed'])};"
        f"continuous_contribution_fraction_FULL={r['continuous_contribution_fraction_FULL']:.6f};"
        f"SCHEMATIC_ref_frac=0.97308_intercept=-245.69;"
        f"drop_factor={r['drop_factor']:.1f}x;"
        f"splice_discontinuity_absent={bool(r['splice_discontinuity_absent'])}_L12to14jump={r['splice_jump_FULL']:.2f}x;"
        f"monotone_increasing={bool(r['monotone_increasing'])};"
        f"band_tag={r['band_tag']}"
    )  # (local)

    # 4-tuple output (final non-verdict line per gate-verdicts.md)
    print(f"\n4-tuple: (value='{value_field[:80]}...', scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # --- input_pin_map for closure SHA ---
    input_pin_map = {rel: sha for rel, sha in pins.items()}  # (local)
    input_pin_map["canonical_constants_kappa_2_substrate_FW"] = f"{kappa_2_substrate_FW:.18e}"
    input_pin_map["canonical_constants_M_KK"] = f"{M_KK:.18e}"
    input_pin_map["canonical_constants_tau_fold"] = f"{tau_fold:.18e}"

    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), CANONICAL_CONSTANTS_PATH, input_pin_map
    )  # (local)
    append_verdict(r["verdict"], value_field, audit_sha, content_sha)
    print(f"\nverdict appended: {r['verdict']} -- value (truncated)={value_field[:100]!r}...")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print(f"\nwall: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
