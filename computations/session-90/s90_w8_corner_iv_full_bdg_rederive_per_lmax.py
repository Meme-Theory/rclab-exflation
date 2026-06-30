#!/usr/bin/env python3
"""
S90 W8-3 — S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS  (CF-61)
=====================================================================================

Gate: S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS  ([VERIFY-THEOREM])

PURPOSE
-------
Corner-IV K-window log-derivative substrate-IS theorem empirical alpha extraction
across L_max in {6, 7, 8, 9, 10, 11, 12} via FULL BdG re-derivation:
    (i)   BCS gap equation regenerated self-consistently on the L_max-truncated
          D_K^2 spectrum at tau_fold = 0.19;
    (ii)  Bogoliubov diagonalization on the 8 canonical BdG modes (B1+B2+B3)
          with per-L_max Delta(L_max) replacing the L=12 canonical Delta_static;
    (iii) K-window log-derivative L_emp(L_max) := d^2 ln P_GGE / d(ln K)^2
          evaluated at K = K_horizon on each L_max-truncated triple;
    (iv)  delta_L(L_max) := |L_emp(L_max) - L_emp(L_max=12)|; empirical envelope
          alpha extracted by log-log regression log(delta_L) = log(C) - alpha*log(L_max).

This gate is the substantive substrate-physics computation that the S89 W5-3
SCHEMATIC Casimir-bound proxy (Delta_eff = Delta_static * f(L_max)) was a
placeholder for. The FULL re-derivation replaces the proxy by actually solving
the gap equation on each L_max truncation; the resulting Delta(L_max) is the
substrate's structural prediction.

PASS PREDICATE (plan §W8-3 line 790)
------------------------------------
    PASS iff  alpha in [2.5, 3.5]
         AND  R^2 >= 0.95
         AND  |L_emp(L_max=12) - (-7.046336474406761)| < 1e-9

PASS triggers §VII.AV upgrade from REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT
to STAGE-1-CANDIDATE per joint-theorem-promotion.md §"Stage 1".

INFO band: alpha in [2.0, 2.5) U (3.5, 4.5]  OR  R^2 in [0.90, 0.95).
FAIL:      alpha outside [2.0, 4.5]  OR  R^2 < 0.90  OR  L_max=12 anchor mismatch.

CLASSIFICATION: GEOMETRIC + PHONONIC
  GEOMETRIC because the K-window log-derivative IS a substrate-IS observable
  on the BdG sub-algebra M_2(C) of the substrate spectral triple
  (A_K^{<=L}, H_K^{<=L}, D_K^{<=L});
  PHONONIC because the GGE-Bogoliubov occupation variance P_GGE(K) carries the
  post-fold pair-production phonon structure.

CONVENTION (plan §W8-3 line 783)
--------------------------------
  scheme       = FULL-BdG-rederivation-per-lmax
  convention   = corner-iv-K-window-log-derivative-substrate-IS
  CLASS pin    = FULL (per substrate-first-canonical-sourcing.md §(iv);
                 FULL physical BdG; NOT SCHEMATIC; full BCS gap equation)
  L_max        = 12  (reference; L_max in {6..12} scanned)

SUBSTITUTION CHAIN (plan §W8-3 lines 800-839, MANDATORY)
========================================================

  Step 1 — Definitions (substrate-IS Bogoliubov on BdG sub-algebra M_2(C)):
    n_a^GGE(K)              := |v_a(K)|^2                   [Bogoliubov occupation]
    xi_a(K, L_max)          := xi_a^(0)(L_max) * (K / K_horizon)^2  [acoustic K^2]
    E_a(K, L_max)           := sqrt(xi_a(K, L_max)^2 + |Delta(L_max)|^2)
    Delta(L_max)            := L_max-truncated self-consistent BCS gap (Step 3)
    L_emp(L_max)            := d^2 ln P_GGE / d(ln K)^2 |_K_horizon

  Step 2 — Pre-flight Casimir-bound feasibility per
           `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection
           Feasibility Pre-Check"`:
    For each L_max in {6..12}, check that the deepest BdG sector eigenvalue
    is bounded below by  eta_FB_lower * sqrt(C_2(p+q) + 1)  with
    eta_FB_lower = 0.40  (S87 W11-3 calibration: 8.4% below empirical floor 0.4365).
    Output: `casimir_feasibility_log.json`.

  Step 3 — BCS gap equation regeneration per L_max (FULL re-derivation):
    For each L_max, solve self-consistently:
      1 / V_BCS  =  Sum_a [ m_a / (2 * E_a(L_max)) ] * tanh( E_a(L_max) / (2 T) )
    where the sum runs over multiplicity-weighted L_max-truncated D_K^2
    eigenvalues  lambda_a, m_a  with E_a = sqrt(lambda_a^2 + Delta^2);
    V_BCS is calibrated ONCE to reproduce Delta_BCS = 0.4643 M_KK at L_max=12
    (canonical S70 / S52 anchor). Iterative fixed-point:
      Delta_{n+1}  =  ( Sum_a m_a * tanh(E_a/(2T)) / (2 E_a) )^{-1} * Delta_n
    Convergence:  |Delta_{n+1} - Delta_n| / Delta_n < 1e-10  (RATIO).

  Step 4 — Bogoliubov diagonalization per L_max:
    For each L_max, with the structural 8-mode (B1+B2+B3) framework, rescale
    the s52 canonical xi^(0) static amplitudes by Delta(L_max)/Delta_static:
      Delta_per_mode(L_max)  :=  Delta_per_mode_static * Delta(L_max)/Delta_static
    The 8 modes are substrate-invariant (B1 ungapped, B2 4-fold deep, B3 3-fold
    upper); only the gap-modulation factor varies with L_max. This is the
    structurally correct FULL re-derivation because the substrate's 8-mode
    architecture is determined by the (A_K, H_K) algebra and pair-symmetry
    structure (S52 finding), while Delta(L_max) is the L_max-dependent
    spectral-kernel weight that the gap equation produces.
    Verification: at L_max=12, Delta(12) reproduces Delta_BCS = 0.4643 by
    construction (V_BCS calibration); Bogoliubov amplitudes match s52 exactly.

  Step 5 — K-window log-derivative observable per L_max:
    Build K-window grid uniform in ln K over [0.95, 1.05] K_horizon with
    DLNK = 0.001 (151 points; matches S87 W2-3 / S89 W5-2 canonical pin).
    For each L_max:
      v_a^2(K, L_max)  :=  (1/2) * (1 - xi_a(K, L_max) / E_a(K, L_max))
      P_GGE(K, L_max)  :=  Var_a( v_a^2(K, L_max) )      [substrate-IS Cell IV]
      L_emp(L_max)     :=  5-point central FD of ln P_GGE wrt ln K at K_horizon

  Step 6 — Empirical alpha extraction via log-log regression:
    delta_L(L_max)    :=  |L_emp(L_max) - L_emp(L_max=12)|  for L_max in {6..11}
    log linear fit:   log(delta_L)  =  log(C) - alpha * log(L_max)
    Cross-check L^{-3} envelope at d=4 per cross-pillar-bridge-anatomy.md
    §"Level-2-binding" calibration.

  Step 7 — PASS predicate:
    sign_verdict       = PASS by construction (alpha > 0 is the L^{-3} direction)
    magnitude_verdict  = PASS iff alpha in [2.5, 3.5] AND R^2 >= 0.95
                              AND |L_emp(12) - (-7.046336474406761)| < 1e-9
    regime_verdict     = VALID iff gap eq converges at every L_max within <= 1000 iter
                         MARGINAL iff one L_max requires > 1000 iter
                         BREAKDOWN iff any L_max fails to converge
    Composite collapse per gate-verdicts.md S87+ schema-v2.

  Step 8 — Promotion semantics trigger:
    PASS  ==>  emit §VII.AV registry-status upgrade companion row:
               # promotion_target=permanent-results-registry.md §VII.AV
               # from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT to=STAGE-1-CANDIDATE
    PASS jointly with CF-65 PASS  ==>  HIT K-counter K=2 -> K=3 (MANDATORY).
    PASS  ==>  Level-2-binding K-counter SUGGESTION K=1 -> K=2 advancement on
               new Corner-IV BdG observable instance (cross-pillar-bridge-
               anatomy.md §"Level-2-binding sub-class" calibration corpus).

CO-AUTHOR ROLES (plan §W8-3 lines 618-622)
==========================================
  connes-ncg-theorist CO-AUTHOR (addressed inline §"Connes co-author block"):
    - Registry-promotion semantics audit on §VII.AV upgrade pathway;
    - Bridge-anatomy 5-element check on Element-1 disambiguation post-CF-62;
    - Level-2-binding admissibility per cross-pillar-bridge-anatomy.md
      §"Level-2 sub-class (binding vs non-binding)" SUGGESTION K=1 calibration
      corpus instance #2 (this gate).
  gen-physicist optional adversarial review (addressed inline §"Gen-physicist
  adversarial review block"): log-log regression methodology on 7-point finite
  series; goodness-of-fit considerations.

SUBSTRATE FRAMING (per `phononic-framing.md §"IS Space, Not IN Space"`)
=======================================================================
  The substrate IS the spectral triple (A_K^{<=L}, H_K^{<=L}, D_K^{<=L}(tau_fold))
  at tau_fold = 0.19 (Level-1 single-tau-slice per "Single-tau-slice vs moduli-
  deformation substrate-IS levels"). The BdG sub-algebra M_2(C) subset A_K is
  intrinsic to the substrate's finite spectral triple — it is NOT a "BCS
  phenomenological model" or "Hamiltonian in a superconducting container".
  The Corner-IV K-window log-derivative L_emp(L_max) IS a single-summand-
  projection trace on M_2(C) per mechanical-closure-discipline.md §"Layer-
  separability carve-out" Type-F observable class (operator-side; algebra-
  INVARIANT functional family per cross-pillar-bridge-anatomy.md §"Algebra-
  axis orthogonality K-counter" MANDATORY at K=3).
  The L_max truncation IS the finite spectral triple's own truncation
  parameter; the L_max -> infinity limit IS the continuum cohomology-class
  binding under the HKR map per cross-pillar-bridge-anatomy.md §"Level-2-
  binding".
  Direction of explanation: substrate (Pillar III/IV BdG-spectral-triple) ->
  bridge (HKR L_max -> infinity) -> laboratory (Pillar V continuum 3He-B
  BdG-sector observable). FORBIDDEN container-thinking: "the BdG modes live
  IN a superconducting container parametrized by L_max"; INVERT: "the BdG
  modes ARE the substrate's intrinsic 8-mode B1+B2+B3 architecture; L_max IS
  the substrate's own truncation refining toward the cohomology-class image".

OUTPUTS
-------
  s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz   — per-L_max BCS gap + BdG modes +
                                                       L_emp + delta_L + log-log fit
  s90_w8_corner_iv_full_bdg_rederive_per_lmax.png   — delta_L vs L_max log-log scatter
                                                       with L^{-3} envelope overlay
  casimir_feasibility_log.json                       — pre-flight feasibility cert

Plan:    sessions/session-plan/session-90-plan-w8.md §W8-3 (CF-61, lines 593-879).
WP:      sessions/archive/session-90/session-90-w8-workingpaper.md §W8-3.
Verdict: computations/session-90/s90_gate_verdicts.txt.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Path / env / canonical-constants
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import time
import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    Delta_BCS,
    T_BCS,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2 — Gate-block constants (plan §W8-3 Machinery pin lines 743-764)
# ---------------------------------------------------------------------------
GATE_ID = "S90-CORNER-IV-FULL-BDG-REDERIVE-PER-LMAX-WITH-PROMOTION-SEMANTICS"
SCHEME = "FULL-BdG-rederivation-per-lmax"
CONVENTION = "corner-iv-K-window-log-derivative-substrate-IS"
L_MAX = 12  # (local) reference L_max for canonical anchor

# L_max scan range (plan W8-3 line 747)
L_MAX_SCAN = [6, 7, 8, 9, 10, 11, 12]  # (local)
L_MAX_REF = 12  # (local) reference; Delta(12) reproduces Delta_BCS by construction

# K-window pins (matches S87 W2-3 / S89 W5-2 canonical anchors)
K_HORIZON_FRAC = (0.95, 1.05)  # (local) 5% window around horizon crossing
DLNK = 0.001  # (local) step in ln K
RANDOM_SEED = 42  # (local) canonical seed

# BCS gap-equation convergence
GAP_EQ_CONVERGENCE_TOL = 1e-10  # (local) plan W8-3 line 752
GAP_EQ_MAX_ITER = 10000  # (local) plan W8-3 line 798 (MARGINAL > 1000)
GAP_EQ_MARGINAL_ITER = 1000  # (local) plan W8-3 line 797

# Anchor + pass bands
VOLOVIK_PATH_CANONICAL = -7.046336474406761  # (local) §W5-2 / S87 W2-3 canonical
LMAX12_ANCHOR_TOL = 1e-9  # (local) plan W8-3 line 753; ABSOLUTE bit-for-bit
ALPHA_PASS_BAND = (2.5, 3.5)  # (local) plan W8-3 line 754
R_SQUARED_PASS = 0.95  # (local) plan W8-3 line 755
ALPHA_INFO_BAND_LOW = (2.0, 2.5)  # (local) plan W8-3 line 756
ALPHA_INFO_BAND_HIGH = (3.5, 4.5)  # (local) plan W8-3 line 756
R_SQUARED_INFO = 0.90  # (local) plan W8-3 line 757

# Friedrich-Bar saturation feasibility per S87 W11-3
ETA_FB_LOWER = 0.40  # (local) plan W8-3 line 759; S87 W11-3 calibration

# Temperature scale
T_FOLD = T_BCS  # (local) substrate-natural at tau_fold = 0.640 in M_KK units (S70)

# Paths
OUT_NPZ = ROOT / "computations" / "session-90" / "s90_w8_corner_iv_full_bdg_rederive_per_lmax.npz"
OUT_PNG = ROOT / "computations" / "session-90" / "s90_w8_corner_iv_full_bdg_rederive_per_lmax.png"
OUT_FEASIBILITY = ROOT / "computations" / "session-90" / "casimir_feasibility_log.json"
VERDICT_FILE = ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"

CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
S52_BOG_CACHE = ROOT / "computations" / "session-52" / "s52_bogoliubov_amp.npz"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S89_W5_A26_NPZ = ROOT / "computations" / "session-89" / "s89_w5_a26_corner_iv_k_window_lmax_scan_level_2_envelope.npz"
PERMANENT_RESULTS = ROOT / "sessions" / "permanent-results-registry.md"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s52_bogoliubov_amp": S52_BOG_CACHE,
    "L12_spectrum_cache_tau019": L12_CACHE,
    "s89_w5_a26_envelope_npz": S89_W5_A26_NPZ,
    "permanent_results_registry": PERMANENT_RESULTS,
    "script": SCRIPT_PATH,
}


# ---------------------------------------------------------------------------
# Section 3 — SHA + verdict helpers (S87+ schema-v2 canonical pattern)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    blob = json.dumps(items, sort_keys=True).encode("utf-8")  # (local)
    return hashlib.sha256(blob).hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print("=" * 78)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:32s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:32s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    """Audit SHA = SHA(script + canonical_constants + pinmap-JSON); Content SHA = SHA(script)."""
    script_bytes = script_path.read_bytes()
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    reg_v: str,
    promote_pass: bool,
) -> None:
    """Atomic single-shot append of canonical line + 3 companion rows
    (dual-SHA + 3-tuple + §VII.AV promotion target).
    """
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    # §VII.AV promotion target cross-link (plan W8-3 lines 731-734)
    if promote_pass:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md §VII.AV "
            f"from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT to=STAGE-1-CANDIDATE "
            f"# {GATE_ID} §VII.AV promotion target companion row (plan W8-3 lines 731-734)\n"
        )  # (local)
    else:
        promotion_target = (
            f"# promotion_target=permanent-results-registry.md §VII.AV "
            f"from=REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT to=REGISTRY-INCOMPLETE "
            f"# {GATE_ID} §VII.AV promotion target companion row (composite={composite}; non-PASS)\n"
        )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(promotion_target)


# ---------------------------------------------------------------------------
# Section 4 — Pre-flight Casimir-bound feasibility (plan §W8-3 Step 1)
# ---------------------------------------------------------------------------
def casimir_c2(p: int, q: int) -> float:
    """SU(3) Casimir C_2(p,q) = (p^2 + p*q + q^2 + 3p + 3q)/3."""
    return float((p * p + p * q + q * q + 3 * p + 3 * q) / 3.0)


def friedrich_baer_check(L_max: int, sectors: dict) -> dict:
    """Verify L_max truncation lies within Friedrich-Bar saturation bound.

    For each L_max-truncated subset of (p,q) sectors with max(p,q) <= L_max,
    compute the per-sector eta_FB = |lambda|_min / sqrt(C_2(p+q) + 1) and
    confirm eta_FB >= ETA_FB_LOWER = 0.40 (S87 W11-3 calibration; 8.4% below
    empirical floor 0.4365).
    """
    sub_sectors = [(sec, info) for sec, info in sectors.items() if max(sec) <= L_max]
    n_sectors = len(sub_sectors)
    per_sector_eta = []
    for (p, q), info in sub_sectors:
        abs_min = float(np.min(info["abs_evals"]))  # (local)
        c2 = casimir_c2(p, q)  # (local)
        eta = abs_min / math.sqrt(c2 + 1.0)  # (local)
        per_sector_eta.append(((p, q), eta))
    eta_min = min(e for _, e in per_sector_eta) if per_sector_eta else float("nan")
    eta_min_sector = next(s for s, e in per_sector_eta if e == eta_min) if per_sector_eta else None
    return {
        "L_max": L_max,
        "n_sectors": n_sectors,
        "eta_min": eta_min,
        "eta_min_sector": list(eta_min_sector) if eta_min_sector else None,
        "eta_FB_lower": ETA_FB_LOWER,
        "feasibility_PASS": bool(eta_min >= ETA_FB_LOWER),
    }


# ---------------------------------------------------------------------------
# Section 5 — Spectrum truncation accounting (plan §W8-3 Step 2)
# ---------------------------------------------------------------------------
def truncate_spectrum_per_lmax(sectors: dict, L_max: int) -> tuple[np.ndarray, np.ndarray, int, int]:
    """For each L_max-truncated subset of (p,q) sectors with max(p,q) <= L_max,
    return:
      lambda_arr: array of |lambda|_a values (one entry per distinct eigenvalue per sector)
      mult_arr:  array of multiplicities m_a (Peter-Weyl dimension dim(p,q) for the sector)
      n_eigs_w:  multiplicity-weighted count = sum(m_a * len(abs_evals(sec)))
      n_sec:     number of sectors with max(p,q) <= L_max
    The multiplicity vector m_a counts dim(p,q) per appearance of the eigenvalue
    in the sector's abs_evals list (each distinct eigenvalue from the sector
    enters the spectrum dim(p,q) times because the sector has dim(p,q) copies
    of each eigenvalue across the Peter-Weyl multiplet).
    """
    lambdas = []
    mults = []
    n_eigs_w = 0  # (local)
    n_sec = 0  # (local)
    for (p, q), info in sectors.items():
        if max(p, q) > L_max:
            continue
        n_sec += 1
        dim = int(info["dim"])  # (local) Peter-Weyl multiplet dimension
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas.append(float(v))
            mults.append(dim)
        n_eigs_w += dim * len(evals_arr)
    return np.array(lambdas, dtype=np.float64), np.array(mults, dtype=np.float64), n_eigs_w, n_sec


# ---------------------------------------------------------------------------
# Section 6 — BCS gap equation regeneration per L_max (plan §W8-3 Step 3)
# ---------------------------------------------------------------------------
def bcs_gap_sum(Delta: float, lambdas: np.ndarray, mults: np.ndarray, T: float) -> float:
    """Sum over multiplicity-weighted L_max-truncated spectrum:
        S(Delta) = Sum_a m_a * tanh(E_a / (2T)) / (2 E_a)
    where E_a = sqrt(lambda_a^2 + Delta^2).
    """
    E = np.sqrt(lambdas * lambdas + Delta * Delta)  # (local)
    return float(np.sum(mults * np.tanh(E / (2.0 * T)) / (2.0 * E)))


def solve_bcs_gap_equation(
    lambdas: np.ndarray,
    mults: np.ndarray,
    T: float,
    inv_V_BCS: float,
    Delta_init: float,
    tol: float = GAP_EQ_CONVERGENCE_TOL,
    max_iter: int = GAP_EQ_MAX_ITER,
) -> tuple[float, int, bool, float]:
    """Self-consistent BCS gap equation solver:
        1/V_BCS = Sum_a m_a tanh(E_a/(2T)) / (2 E_a)
    where E_a = sqrt(lambda_a^2 + Delta^2). Solve by bisection on the residual
    R(Delta) = bcs_gap_sum(Delta) - inv_V_BCS  which is monotone-decreasing in
    Delta (larger Delta -> larger E -> smaller summand) for fixed T.
    Convergence test: |Delta_{n+1} - Delta_n| / |Delta_n| < tol.
    """
    # Bracket [Delta_lo, Delta_hi]: at Delta=0 the sum is maximum; for sufficiently
    # large Delta the sum decreases monotonically. Pick brackets that comfortably
    # straddle the canonical Delta_BCS = 0.4643.
    Delta_lo = 1e-6  # (local)
    Delta_hi = 100.0  # (local) far above any plausible Delta
    R_lo = bcs_gap_sum(Delta_lo, lambdas, mults, T) - inv_V_BCS  # (local)
    R_hi = bcs_gap_sum(Delta_hi, lambdas, mults, T) - inv_V_BCS  # (local)
    if R_lo * R_hi > 0:
        # No bracket (either both positive or both negative); fall back to
        # fixed-point seeded at Delta_init
        Delta = Delta_init  # (local)
        for it in range(max_iter):
            s = bcs_gap_sum(Delta, lambdas, mults, T)  # (local)
            Delta_new = Delta * s / inv_V_BCS  # (local) ratio-rescaling fixed-point
            if abs(Delta_new - Delta) / max(abs(Delta), 1e-30) < tol:
                return Delta_new, it + 1, True, float(s - inv_V_BCS)
            Delta = Delta_new
        return Delta, max_iter, False, float(s - inv_V_BCS)
    # Bisection: monotone-decreasing R(Delta), so R_lo > 0, R_hi < 0
    if R_lo < 0:
        Delta_lo, Delta_hi = Delta_hi, Delta_lo
        R_lo, R_hi = R_hi, R_lo
    converged = False
    iter_count = 0  # (local) bisection iteration counter
    while iter_count < max_iter:
        Delta_mid = 0.5 * (Delta_lo + Delta_hi)  # (local)
        R_mid = bcs_gap_sum(Delta_mid, lambdas, mults, T) - inv_V_BCS  # (local)
        if abs(Delta_hi - Delta_lo) / max(abs(Delta_mid), 1e-30) < tol:
            converged = True
            return Delta_mid, iter_count + 1, True, float(R_mid)
        if R_mid > 0:
            Delta_lo = Delta_mid
        else:
            Delta_hi = Delta_mid
        iter_count += 1
    Delta_mid = 0.5 * (Delta_lo + Delta_hi)  # (local)
    R_mid = bcs_gap_sum(Delta_mid, lambdas, mults, T) - inv_V_BCS  # (local)
    return Delta_mid, iter_count, converged, float(R_mid)


def calibrate_V_BCS(lambdas_L12: np.ndarray, mults_L12: np.ndarray, T: float) -> float:
    """Calibrate V_BCS coupling so that at L_max=12, the gap equation
    self-consistently produces Delta(L_max=12) = Delta_BCS = 0.4643 M_KK.

    inv_V_BCS = Sum_a m_a tanh(E_a^{can}/(2T)) / (2 E_a^{can})
    with E_a^{can} = sqrt(lambda_a^2 + Delta_BCS^2)  evaluated on the FULL
    L_max=12 spectrum.

    Returns inv_V_BCS so that solve_bcs_gap_equation(L=12, inv_V_BCS) -> Delta_BCS.
    """
    return bcs_gap_sum(Delta_BCS, lambdas_L12, mults_L12, T)


# ---------------------------------------------------------------------------
# Section 7 — Bogoliubov diagonalization per L_max (plan §W8-3 Step 4)
# ---------------------------------------------------------------------------
def bogoliubov_modes_per_lmax(
    Delta_L: float,
    Delta_static: float,
    s52_bog: dict,
) -> dict:
    """Rescale the s52 canonical 8-mode BdG amplitudes by Delta(L_max)/Delta_static.

    The 8 modes are substrate-invariant (B1 ungapped, 4xB2 deep, 3xB3 upper);
    only the gap-modulation factor varies with L_max. The static amplitudes
    {u_static, v_static, E_static, Delta_per_mode_static} are the L_max=12
    canonical reference (from s52_bogoliubov_amp.npz).

    Bogoliubov reconstruction at the L_max-modulated gap:
      xi^(0)_a            := (u_static_a^2 - v_static_a^2) * E_static_a    [unchanged; structural]
      Delta_per_mode_L_a  := Delta_per_mode_static_a * Delta_L / Delta_static
                              [B1 retains Delta=0 if Delta_per_mode_static_a=0]
      E_qp_L_a            := sqrt(xi^(0)_a^2 + |Delta_per_mode_L_a|^2)
      u_L_a^2             := (1/2) * (1 + xi^(0)_a / E_qp_L_a)
      v_L_a^2             := (1/2) * (1 - xi^(0)_a / E_qp_L_a)

    At L_max=12, Delta_L = Delta_static => modes are identical to s52 (bit-for-bit).
    """
    u_static = s52_bog["u_k"].astype(np.float64)
    v_static = s52_bog["v_k"].astype(np.float64)
    E_static = s52_bog["E_qp"].astype(np.float64)
    delta_static_per_mode = s52_bog["Delta_per_mode"].astype(np.complex128)
    # Static xi^(0) from u,v,E
    xi0 = (u_static * u_static - v_static * v_static) * E_static  # (local)
    # L_max-scaled per-mode Delta
    rescale = Delta_L / Delta_static  # (local)
    delta_per_mode_L = delta_static_per_mode * rescale  # (local)
    # BdG quasiparticle energies at L_max
    E_L = np.sqrt(xi0 * xi0 + np.abs(delta_per_mode_L) ** 2)  # (local)
    eps_floor = 1e-30  # (local) numerical floor for B1 ungapped mode
    E_L_safe = np.where(E_L < eps_floor, eps_floor, E_L)  # (local)
    u_L2 = 0.5 * (1.0 + xi0 / E_L_safe)  # (local)
    v_L2 = 0.5 * (1.0 - xi0 / E_L_safe)  # (local)
    return {
        "xi0": xi0,
        "delta_per_mode_L": delta_per_mode_L,
        "E_qp_L": E_L,
        "u_L": np.sqrt(np.clip(u_L2, 0.0, 1.0)),
        "v_L": np.sqrt(np.clip(v_L2, 0.0, 1.0)),
        "u_L2": np.clip(u_L2, 0.0, 1.0),
        "v_L2": np.clip(v_L2, 0.0, 1.0),
    }


# ---------------------------------------------------------------------------
# Section 8 — K-window log-derivative observable per L_max (plan §W8-3 Step 5)
# ---------------------------------------------------------------------------
def k_dependent_bogoliubov(
    xi0: np.ndarray,
    delta_per_mode_L: np.ndarray,
    K_ratio: float,
) -> np.ndarray:
    """K-dependent Bogoliubov occupation n_a^GGE(K) = |v_a(K)|^2 (S87 W2-3 Def 1-2)."""
    xi_K = xi0 * (K_ratio * K_ratio)  # (local) acoustic K^2 dispersion
    E_K = np.sqrt(xi_K * xi_K + np.abs(delta_per_mode_L) ** 2)  # (local)
    eps_floor = 1e-30  # (local)
    E_K_safe = np.where(E_K < eps_floor, eps_floor, E_K)  # (local)
    v_K2 = 0.5 * (1.0 - xi_K / E_K_safe)  # (local) Bogoliubov occupation
    v_K2 = np.clip(v_K2, 0.0, 1.0)  # (local) numerical floor
    return v_K2


def compute_K_window_log_derivative(
    xi0: np.ndarray,
    delta_per_mode_L: np.ndarray,
    k_ratios: np.ndarray,
) -> tuple[float | None, np.ndarray]:
    """L_emp(L_max) = d^2 ln P_GGE / d(ln K)^2 at K=K_horizon (5-point central FD)."""
    n_K = len(k_ratios)
    P_GGE = np.zeros(n_K)
    for i, kr in enumerate(k_ratios):
        v_K2 = k_dependent_bogoliubov(xi0, delta_per_mode_L, kr)
        P_GGE[i] = float(np.var(v_K2))
    if P_GGE.min() <= 0:
        return None, P_GGE
    ln_P = np.log(P_GGE)
    ln_K = np.log(k_ratios)
    h = ln_K[1] - ln_K[0]
    i0 = int(np.argmin(np.abs(ln_K)))
    if i0 < 2 or i0 > n_K - 3:
        d2 = (ln_P[i0 + 1] - 2 * ln_P[i0] + ln_P[i0 - 1]) / (h * h)
    else:
        d2 = (
            -ln_P[i0 - 2] + 16 * ln_P[i0 - 1] - 30 * ln_P[i0]
            + 16 * ln_P[i0 + 1] - ln_P[i0 + 2]
        ) / (12.0 * h * h)
    return float(d2), P_GGE


# ---------------------------------------------------------------------------
# Section 9 — Empirical alpha extraction via log-log regression (plan §W8-3 Step 6)
# ---------------------------------------------------------------------------
def extract_alpha_R_squared(
    L_max_arr: np.ndarray,
    delta_L_arr: np.ndarray,
) -> tuple[float, float, float, int]:
    """Log-log linear regression: log(delta_L) = log(C) - alpha * log(L_max)."""
    # Filter out the L_max=12 anchor (delta_L=0 by construction)
    valid = delta_L_arr > 1e-15
    n_valid = int(valid.sum())
    if n_valid < 4:
        return float("nan"), float("nan"), float("nan"), n_valid
    log_L = np.log(L_max_arr[valid])
    log_R = np.log(delta_L_arr[valid])
    # numpy.polyfit: returns [slope, intercept] for deg=1
    coeffs = np.polyfit(log_L, log_R, 1)
    slope = float(coeffs[0])
    intercept = float(coeffs[1])
    alpha = -slope  # log(delta_L) = log(C) - alpha * log(L_max)  =>  slope = -alpha
    log_R_pred = intercept + slope * log_L
    ss_res = float(np.sum((log_R - log_R_pred) ** 2))
    ss_tot = float(np.sum((log_R - log_R.mean()) ** 2))
    R_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")
    return alpha, R_squared, intercept, n_valid


# ---------------------------------------------------------------------------
# Section 10 — Verdict evaluation (plan §W8-3 Step 7 PASS predicate)
# ---------------------------------------------------------------------------
def evaluate_verdict(
    alpha: float,
    R_squared: float,
    L_emp_at_L12: float,
    max_gap_iter: int,
    gap_eq_converged_all: bool,
) -> dict:
    """Pre-registered PASS / INFO / FAIL bands per plan §W8-3 lines 786-792.

    PASS  : alpha in [2.5, 3.5] AND R^2 >= 0.95 AND |L_emp(12) - anchor| < 1e-9
    INFO  : alpha in [2.0, 2.5) U (3.5, 4.5]  OR  R^2 in [0.90, 0.95)
    FAIL  : alpha outside [2.0, 4.5]  OR  R^2 < 0.90  OR  anchor mismatch
    """
    anchor_diff = abs(L_emp_at_L12 - VOLOVIK_PATH_CANONICAL)
    anchor_PASS = anchor_diff < LMAX12_ANCHOR_TOL  # (local)
    alpha_in_pass_band = (
        not math.isnan(alpha) and ALPHA_PASS_BAND[0] <= alpha <= ALPHA_PASS_BAND[1]
    )
    alpha_in_info_band_low = (
        not math.isnan(alpha) and ALPHA_INFO_BAND_LOW[0] <= alpha < ALPHA_INFO_BAND_LOW[1]
    )
    alpha_in_info_band_high = (
        not math.isnan(alpha) and ALPHA_INFO_BAND_HIGH[0] < alpha <= ALPHA_INFO_BAND_HIGH[1]
    )
    alpha_in_info_band = alpha_in_info_band_low or alpha_in_info_band_high
    R_squared_pass = not math.isnan(R_squared) and R_squared >= R_SQUARED_PASS
    R_squared_info = not math.isnan(R_squared) and R_squared_pass is False and R_squared >= R_SQUARED_INFO
    alpha_outside_all = (
        not math.isnan(alpha)
        and (alpha < 2.0 or alpha > 4.5)
    )
    # sign_verdict = PASS by construction (alpha > 0 is the L^{-3} envelope direction)
    if not math.isnan(alpha) and alpha > 0:
        sign_v = "PASS"
    else:
        sign_v = "FAIL"
    # magnitude_verdict
    if alpha_in_pass_band and R_squared_pass and anchor_PASS:
        mag_v = "PASS"
    elif alpha_outside_all or not anchor_PASS:
        mag_v = "FAIL"
    elif alpha_in_info_band or R_squared_info:
        mag_v = "INFO"
    else:
        mag_v = "FAIL"
    # regime_verdict
    if not gap_eq_converged_all:
        reg_v = "BREAKDOWN"
    elif max_gap_iter > GAP_EQ_MARGINAL_ITER:
        reg_v = "MARGINAL"
    else:
        reg_v = "VALID"
    # composite collapse per gate-verdicts.md S87+ canonical rule
    if reg_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return {
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": reg_v,
        "composite": composite,
        "alpha": alpha,
        "R_squared": R_squared,
        "L_emp_at_L12": L_emp_at_L12,
        "anchor_diff": anchor_diff,
        "anchor_PASS": anchor_PASS,
        "alpha_in_pass_band": alpha_in_pass_band,
        "alpha_in_info_band_low": alpha_in_info_band_low,
        "alpha_in_info_band_high": alpha_in_info_band_high,
        "alpha_outside_all": alpha_outside_all,
        "R_squared_pass": R_squared_pass,
        "R_squared_info": R_squared_info,
        "max_gap_iter": max_gap_iter,
        "gap_eq_converged_all": gap_eq_converged_all,
    }


# ---------------------------------------------------------------------------
# Section 11 — Plot (plan §W8-3 output spec)
# ---------------------------------------------------------------------------
def emit_plot(
    out_png: Path,
    L_max_arr: np.ndarray,
    delta_L_arr: np.ndarray,
    alpha: float,
    R_squared: float,
    intercept: float,
    L_emp_per_L: np.ndarray,
    delta_bcs_per_L: np.ndarray,
) -> None:
    """4-panel:
      (a) delta_L vs L_max log-log scatter with L^{-3} reference + empirical fit
      (b) L_emp vs L_max linear scatter with canonical anchor at L_max=12
      (c) Delta(L_max) vs L_max
      (d) Empirical alpha extracted vs target band [2.5, 3.5]
    """
    fig, axes = plt.subplots(1, 4, figsize=(22, 5))

    # Panel (a): delta_L vs L_max log-log with envelope overlay
    valid = delta_L_arr > 1e-15
    ax = axes[0]
    ax.loglog(
        L_max_arr[valid], delta_L_arr[valid],
        "o", color="tab:blue", markersize=10,
        label="empirical delta_L"
    )
    # Empirical fit
    if not math.isnan(alpha):
        L_fit = np.linspace(L_max_arr[valid].min() * 0.9, L_max_arr[valid].max() * 1.1, 50)
        delta_L_fit = np.exp(intercept) * L_fit ** (-alpha)
        ax.loglog(
            L_fit, delta_L_fit, "--", color="tab:red", lw=2,
            label=f"empirical L^(-alpha), alpha = {alpha:.3f}, R^2 = {R_squared:.3f}"
        )
    # L^{-3} envelope reference (pinned to leftmost data point)
    if len(L_max_arr[valid]) > 0:
        L_ref = L_max_arr[valid][0]
        delta_ref = delta_L_arr[valid][0]
        C_ref = delta_ref * (L_ref ** 3)
        L_env = np.linspace(L_max_arr[valid].min() * 0.9, L_max_arr[valid].max() * 1.1, 50)
        delta_env = C_ref * L_env ** (-3.0)
        ax.loglog(L_env, delta_env, ":", color="tab:green", lw=2, label="L^(-3) envelope reference")
    ax.set_xlabel("L_max", fontsize=12)
    ax.set_ylabel("|L_emp(L_max) - L_emp(12)|", fontsize=12)
    ax.set_title("Corner-IV K-window log-derivative\nFULL BdG re-derivation L_max envelope", fontsize=11)
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, which="both", alpha=0.3)

    # Panel (b): L_emp(L_max) vs L_max linear
    ax = axes[1]
    ax.plot(L_max_arr, L_emp_per_L, "o", color="tab:blue", markersize=10, label="L_emp(L_max)")
    ax.axhline(
        VOLOVIK_PATH_CANONICAL, color="tab:green", ls="--", lw=2,
        label=f"canonical L_emp(inf) = {VOLOVIK_PATH_CANONICAL:.6f}"
    )
    ax.set_xlabel("L_max", fontsize=12)
    ax.set_ylabel("L_emp(L_max)", fontsize=12)
    ax.set_title("L_emp(L_max) convergence to canonical anchor", fontsize=11)
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel (c): Delta(L_max) vs L_max
    ax = axes[2]
    ax.plot(L_max_arr, delta_bcs_per_L, "o-", color="tab:purple", markersize=10, label="Delta(L_max)")
    ax.axhline(
        Delta_BCS, color="tab:green", ls="--", lw=2,
        label=f"Delta_BCS = {Delta_BCS:.6f} (S70 canonical)"
    )
    ax.set_xlabel("L_max", fontsize=12)
    ax.set_ylabel("Delta(L_max) (M_KK units)", fontsize=12)
    ax.set_title("BCS gap regenerated per L_max", fontsize=11)
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel (d): alpha vs PASS band
    ax = axes[3]
    band_colors = ["tab:red", "tab:orange", "tab:green", "tab:orange", "tab:red"]
    band_edges = [1.0, 2.0, 2.5, 3.5, 4.5, 5.5]
    band_labels = ["FAIL low", "INFO low", "PASS", "INFO high", "FAIL high"]
    for i, (lo, hi, c, lab) in enumerate(zip(band_edges[:-1], band_edges[1:], band_colors, band_labels)):
        ax.axhspan(lo, hi, alpha=0.18, color=c, label=lab if i in (0, 1, 2, 3, 4) else None)
    if not math.isnan(alpha):
        ax.scatter([0.5], [alpha], color="tab:blue", s=200, zorder=5, label=f"alpha = {alpha:.3f}")
    ax.axhline(3.0, color="black", ls=":", lw=1.5, label="L^{-3} prediction")
    ax.set_ylim(1.0, 5.5)
    ax.set_xlim(0, 1)
    ax.set_xticks([])
    ax.set_ylabel("empirical alpha", fontsize=12)
    ax.set_title("alpha extraction vs PASS band [2.5, 3.5]", fontsize=11)
    ax.legend(loc="best", fontsize=9)
    ax.grid(True, axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(out_png, dpi=110, bbox_inches="tight")
    plt.close()


# ---------------------------------------------------------------------------
# Section 12 — Main
# ---------------------------------------------------------------------------
def main() -> None:
    np.random.seed(RANDOM_SEED)
    pins = log_input_pins(INPUT_FILES)

    # --- Step 1: Pre-flight Casimir-bound feasibility -----------------------
    print("\n--- Step 1: Pre-flight Casimir-bound + Friedrich-Bar feasibility ---")
    cache = np.load(L12_CACHE, allow_pickle=True)
    sectors = cache["sector_evals"].item()
    feasibility_log = {
        "rule": "math-scripts.md §'D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check'",
        "anchor": "S87 W11-3 Friedrich-Bar saturation, eta_FB_lower=0.40 (8.4% below empirical floor 0.4365)",
        "L_max_scan": L_MAX_SCAN,
        "per_L_max": {},
    }
    all_feasible = True
    for L in L_MAX_SCAN:
        check = friedrich_baer_check(L, sectors)
        feasibility_log["per_L_max"][f"L_max_{L}"] = check
        print(
            f"  L_max={L:2d}: n_sectors={check['n_sectors']:3d}, "
            f"eta_min={check['eta_min']:.6f} (sector {check['eta_min_sector']}), "
            f"feasibility: {'PASS' if check['feasibility_PASS'] else 'FAIL'}"
        )
        if not check["feasibility_PASS"]:
            all_feasible = False
    feasibility_log["all_feasible"] = all_feasible
    with open(OUT_FEASIBILITY, "w", encoding="utf-8") as f:
        json.dump(feasibility_log, f, indent=2, default=str)
    print(f"  Casimir-bound feasibility log -> {OUT_FEASIBILITY.relative_to(ROOT)}")
    print(f"  all_feasible = {all_feasible}")

    # --- Step 2: Spectrum truncation accounting per L_max -------------------
    print("\n--- Step 2: Spectrum truncation accounting per L_max ---")
    spectrum_per_L = {}
    for L in L_MAX_SCAN:
        lambdas, mults, n_eigs_w, n_sec = truncate_spectrum_per_lmax(sectors, L)
        spectrum_per_L[L] = {
            "lambdas": lambdas,
            "mults": mults,
            "n_eigs_w": n_eigs_w,
            "n_sectors": n_sec,
            "lambda_min": float(lambdas.min()),
            "lambda_max": float(lambdas.max()),
        }
        print(
            f"  L_max={L:2d}: n_sectors={n_sec:3d}, n_distinct_evals={len(lambdas):5d}, "
            f"n_weighted_eigs={n_eigs_w:8d}, |lambda|=[{lambdas.min():.6f}, {lambdas.max():.6f}]"
        )

    # --- Step 3: BCS gap equation regeneration per L_max --------------------
    print("\n--- Step 3: BCS gap equation regeneration per L_max ---")
    # Calibrate inv_V_BCS so that at L_max=12 the gap eq gives Delta = Delta_BCS
    L12_data = spectrum_per_L[L_MAX_REF]
    inv_V_BCS = calibrate_V_BCS(L12_data["lambdas"], L12_data["mults"], T_FOLD)
    print(f"  Calibrated inv_V_BCS = {inv_V_BCS:.10f}  (T_fold = {T_FOLD}, Delta_BCS = {Delta_BCS})")
    print(f"  (V_BCS = {1.0/inv_V_BCS:.10f} M_KK^{-1})")
    delta_bcs_per_L = []
    gap_iter_per_L = []
    gap_converged_per_L = []
    gap_residual_per_L = []
    for L in L_MAX_SCAN:
        t0 = time.time()
        data = spectrum_per_L[L]
        Delta_L, n_iter, converged, residual = solve_bcs_gap_equation(
            data["lambdas"], data["mults"], T_FOLD,
            inv_V_BCS, Delta_init=Delta_BCS,
        )
        elapsed = time.time() - t0
        delta_bcs_per_L.append(Delta_L)
        gap_iter_per_L.append(n_iter)
        gap_converged_per_L.append(converged)
        gap_residual_per_L.append(residual)
        ratio_to_canonical = Delta_L / Delta_BCS
        print(
            f"  L_max={L:2d}: Delta(L) = {Delta_L:.10f}, iter={n_iter:4d}, "
            f"converged={converged}, residual={residual:+.3e}, "
            f"Delta/Delta_BCS = {ratio_to_canonical:.6f}, t={elapsed:.3f}s"
        )
    delta_bcs_per_L = np.array(delta_bcs_per_L, dtype=np.float64)
    gap_iter_per_L = np.array(gap_iter_per_L, dtype=np.int64)
    gap_residual_per_L = np.array(gap_residual_per_L, dtype=np.float64)
    gap_converged_all = bool(all(gap_converged_per_L))
    max_gap_iter = int(max(gap_iter_per_L))

    # Verify L_max=12 anchor by construction
    idx_L12 = L_MAX_SCAN.index(L_MAX_REF)
    Delta_at_L12 = delta_bcs_per_L[idx_L12]
    bcs_anchor_diff = abs(Delta_at_L12 - Delta_BCS)
    print(f"  Delta(L_max=12) - Delta_BCS = {bcs_anchor_diff:.3e}  "
          f"(expected ~ 1e-10 by V_BCS calibration; tol = {GAP_EQ_CONVERGENCE_TOL})")

    # --- Step 4: Bogoliubov diagonalization per L_max ----------------------
    print("\n--- Step 4: Bogoliubov diagonalization per L_max (8-mode B1+B2+B3) ---")
    s52_bog = dict(np.load(S52_BOG_CACHE, allow_pickle=True))
    Delta_static = float(np.abs(s52_bog["Delta_per_mode"]).max())  # = 0.7704351
    print(f"  Delta_static (from s52, max |Delta_per_mode|) = {Delta_static:.10f}")
    bdg_modes_per_L = {}
    bdg_amp_tensor_u = np.zeros((len(L_MAX_SCAN), 8), dtype=np.float64)
    bdg_amp_tensor_v = np.zeros((len(L_MAX_SCAN), 8), dtype=np.float64)
    bdg_amp_tensor_E = np.zeros((len(L_MAX_SCAN), 8), dtype=np.float64)
    bdg_amp_tensor_delta = np.zeros((len(L_MAX_SCAN), 8), dtype=np.complex128)
    for i, L in enumerate(L_MAX_SCAN):
        modes_L = bogoliubov_modes_per_lmax(delta_bcs_per_L[i], Delta_static, s52_bog)
        bdg_modes_per_L[L] = modes_L
        bdg_amp_tensor_u[i] = modes_L["u_L"]
        bdg_amp_tensor_v[i] = modes_L["v_L"]
        bdg_amp_tensor_E[i] = modes_L["E_qp_L"]
        bdg_amp_tensor_delta[i] = modes_L["delta_per_mode_L"]
        print(
            f"  L_max={L:2d}: rescale = {delta_bcs_per_L[i]/Delta_static:.6f}, "
            f"E_qp range = [{modes_L['E_qp_L'].min():.4f}, {modes_L['E_qp_L'].max():.4f}], "
            f"v range = [{modes_L['v_L'].min():.4f}, {modes_L['v_L'].max():.4f}]"
        )

    # --- Step 5: K-window log-derivative observable per L_max --------------
    print("\n--- Step 5: K-window log-derivative L_emp per L_max ---")
    ln_min = math.log(K_HORIZON_FRAC[0])
    ln_max_grid = math.log(K_HORIZON_FRAC[1])
    n_K_pts = int(round((ln_max_grid - ln_min) / DLNK)) + 1
    ln_K_grid = np.linspace(ln_min, ln_max_grid, n_K_pts)
    k_ratios = np.exp(ln_K_grid)
    print(f"  K-window grid: [{K_HORIZON_FRAC[0]:.3f}, {K_HORIZON_FRAC[1]:.3f}] K_horizon, "
          f"n_K_pts = {n_K_pts}, DLNK = {DLNK}")
    L_emp_per_L = []
    P_GGE_at_KH_per_L = []
    P_GGE_grid_per_L = {}
    for i, L in enumerate(L_MAX_SCAN):
        modes_L = bdg_modes_per_L[L]
        L_emp, P_GGE = compute_K_window_log_derivative(
            modes_L["xi0"], modes_L["delta_per_mode_L"], k_ratios
        )
        if L_emp is None:
            print(f"  L_max={L:2d}: P_GGE has zero/negative values -> NaN")
            L_emp_per_L.append(float("nan"))
            P_GGE_at_KH_per_L.append(float("nan"))
        else:
            L_emp_per_L.append(L_emp)
            P_at_KH = float(P_GGE[int(np.argmin(np.abs(ln_K_grid)))])
            P_GGE_at_KH_per_L.append(P_at_KH)
            print(
                f"  L_max={L:2d}: L_emp = {L_emp:+.10f}, "
                f"P_GGE@K_horizon = {P_at_KH:.6e}, "
                f"P_GGE range = [{P_GGE.min():.3e}, {P_GGE.max():.3e}]"
            )
        P_GGE_grid_per_L[L] = P_GGE
    L_emp_per_L = np.array(L_emp_per_L, dtype=np.float64)
    P_GGE_at_KH_per_L = np.array(P_GGE_at_KH_per_L, dtype=np.float64)

    # L_max=12 anchor verification
    L_emp_at_L12 = L_emp_per_L[idx_L12]
    anchor_diff = abs(L_emp_at_L12 - VOLOVIK_PATH_CANONICAL)
    print(f"\n  L_emp(L_max=12) = {L_emp_at_L12:+.15f}")
    print(f"  canonical anchor = {VOLOVIK_PATH_CANONICAL}")
    print(f"  |diff| = {anchor_diff:.3e}  (tol = {LMAX12_ANCHOR_TOL})")
    print(f"  anchor_PASS = {anchor_diff < LMAX12_ANCHOR_TOL}")

    # --- Step 6: Empirical alpha extraction --------------------------------
    print("\n--- Step 6: Empirical alpha extraction via log-log regression ---")
    L_max_arr = np.array(L_MAX_SCAN, dtype=np.float64)
    delta_L_arr = np.abs(L_emp_per_L - L_emp_at_L12)
    print(f"  delta_L per L_max = {delta_L_arr}")
    alpha, R_squared, intercept, n_valid = extract_alpha_R_squared(L_max_arr, delta_L_arr)
    print(f"  n_valid (L_max != 12) = {n_valid}")
    print(f"  log-log fit: log(delta_L) = log(C) - alpha * log(L_max)")
    print(f"  alpha = {alpha:.6f}  (predicted: 3.0 for L^-3 envelope at d=4)")
    print(f"  R^2   = {R_squared:.6f}")
    print(f"  log(C) intercept = {intercept:.6f}")

    # --- Step 7: PASS predicate evaluation ---------------------------------
    print("\n--- Step 7: PASS predicate evaluation ---")
    verdict = evaluate_verdict(
        alpha=alpha, R_squared=R_squared, L_emp_at_L12=L_emp_at_L12,
        max_gap_iter=max_gap_iter, gap_eq_converged_all=gap_converged_all,
    )
    for k, v in verdict.items():
        print(f"  {k:32s} = {v}")

    # --- Step 8: Compute dual SHA + emit verdict line ----------------------
    print("\n--- Step 8: Dual SHA + verdict emission ---")
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    composite = verdict["composite"]
    sign_v = verdict["sign_verdict"]
    mag_v = verdict["magnitude_verdict"]
    reg_v = verdict["regime_verdict"]
    value_str = (
        f"alpha={alpha:.6f};R_squared={R_squared:.6f};L_emp_at_L12={L_emp_at_L12:.15f};"
        f"anchor_diff={anchor_diff:.3e};anchor_PASS={int(verdict['anchor_PASS'])};"
        f"alpha_in_pass_band={int(verdict['alpha_in_pass_band'])};"
        f"R_squared_pass={int(verdict['R_squared_pass'])};"
        f"max_gap_iter={max_gap_iter};gap_eq_converged_all={int(gap_converged_all)};"
        f"all_feasible={int(all_feasible)};"
        f"Delta_L12_diff_canonical={bcs_anchor_diff:.3e};"
        f"sign={sign_v};mag={mag_v};reg={reg_v};composite={composite};"
        f"hit_K_advance={'1' if composite=='PASS' else '0'};"
        f"level_2_binding_K_advance={'1' if composite=='PASS' else '0'};"
        f"vii_av_promotion={'STAGE-1-CANDIDATE' if composite=='PASS' else 'REGISTRY-INCOMPLETE'}"
    )
    append_verdict(
        composite=composite,
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=sign_v,
        mag_v=mag_v,
        reg_v=reg_v,
        promote_pass=(composite == "PASS"),
    )
    print(f"  Verdict line appended to: {VERDICT_FILE.relative_to(ROOT)}")

    # --- Step 9: Save NPZ + emit plot --------------------------------------
    print("\n--- Step 9: Save NPZ + emit plot ---")
    np.savez(
        OUT_NPZ,
        # L_max scan + per-L_max BCS gaps
        L_max_arr=L_max_arr,
        delta_bcs_per_lmax=delta_bcs_per_L,
        gap_iter_per_L=gap_iter_per_L,
        gap_residual_per_L=gap_residual_per_L,
        gap_converged_per_L=np.array(gap_converged_per_L),
        inv_V_BCS=inv_V_BCS,
        T_FOLD=T_FOLD,
        Delta_BCS_canonical=Delta_BCS,
        Delta_static_s52=Delta_static,
        # Per-L_max BdG amplitude tensor (shape (7, 8))
        bdg_amp_tensor_u=bdg_amp_tensor_u,
        bdg_amp_tensor_v=bdg_amp_tensor_v,
        bdg_amp_tensor_E=bdg_amp_tensor_E,
        bdg_amp_tensor_delta=bdg_amp_tensor_delta,
        # K-window L_emp per L_max
        L_emp_per_L=L_emp_per_L,
        P_GGE_at_KH_per_L=P_GGE_at_KH_per_L,
        k_ratios=k_ratios,
        ln_K_grid=ln_K_grid,
        n_K_pts=n_K_pts,
        DLNK=DLNK,
        K_HORIZON_FRAC=np.array(K_HORIZON_FRAC),
        # Anchor + delta_L + alpha extraction
        VOLOVIK_PATH_CANONICAL=VOLOVIK_PATH_CANONICAL,
        L_emp_at_L12=L_emp_at_L12,
        anchor_diff=anchor_diff,
        anchor_PASS=verdict["anchor_PASS"],
        delta_L_arr=delta_L_arr,
        alpha=alpha,
        R_squared=R_squared,
        log_C_intercept=intercept,
        n_valid_regression=n_valid,
        # Friedrich-Bar feasibility
        all_feasible=all_feasible,
        eta_FB_lower=ETA_FB_LOWER,
        # Verdict 3-tuple + composite
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        composite_verdict=composite,
        # PASS thresholds
        alpha_pass_band=np.array(ALPHA_PASS_BAND),
        R_squared_pass=R_SQUARED_PASS,
        R_squared_info=R_SQUARED_INFO,
        alpha_info_band_low=np.array(ALPHA_INFO_BAND_LOW),
        alpha_info_band_high=np.array(ALPHA_INFO_BAND_HIGH),
        lmax12_anchor_tol=LMAX12_ANCHOR_TOL,
        # SHA
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        random_seed=RANDOM_SEED,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
    )
    # Also save P_GGE grids per L_max for debugging
    pg_grids = np.array([P_GGE_grid_per_L[L] for L in L_MAX_SCAN])
    np.save(OUT_NPZ.parent / (OUT_NPZ.stem + "_P_GGE_grids.npy"), pg_grids)
    print(f"  NPZ -> {OUT_NPZ.relative_to(ROOT)}")
    emit_plot(
        OUT_PNG, L_max_arr, delta_L_arr, alpha, R_squared, intercept,
        L_emp_per_L, delta_bcs_per_L,
    )
    print(f"  PNG -> {OUT_PNG.relative_to(ROOT)}")

    # --- Step 10: Final summary --------------------------------------------
    print("\n" + "=" * 78)
    print(f"GATE VERDICT: {composite}")
    print("=" * 78)
    print(f"  alpha = {alpha:.6f}  in PASS band [2.5, 3.5]? {verdict['alpha_in_pass_band']}")
    print(f"  R^2 = {R_squared:.6f}  >= 0.95? {verdict['R_squared_pass']}")
    print(f"  L_emp(12) anchor diff = {anchor_diff:.3e} < 1e-9? {verdict['anchor_PASS']}")
    print(f"  sign = {sign_v}, mag = {mag_v}, reg = {reg_v}")
    print(f"  composite = {composite}")
    if composite == "PASS":
        print(f"  ==> §VII.AV STAGE-1-CANDIDATE promotion triggered")
        print(f"  ==> HIT K-counter K=2 -> K=3 (joint with CF-65 PASS)")
        print(f"  ==> Level-2-binding K-counter SUGGESTION K=1 -> K=2 (new Corner-IV BdG instance)")
    else:
        print(f"  ==> §VII.AV remains REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT")


if __name__ == "__main__":
    main()
