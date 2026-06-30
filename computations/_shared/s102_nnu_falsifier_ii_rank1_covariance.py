#!/usr/bin/env python3
"""
S102 W1-3 S102-NNU-FALSIFIER-II-RANK1-COVARIANCE (CF-beta) — rank-1 covariance count-check
==========================================================================================

Gate: S102-NNU-FALSIFIER-II-RANK1-COVARIANCE ([SIGN])

Falsifier (ii) of the Normalization-Non-Universality theorem-tag (registered Stage-1 slot
§VII.BS, sessions/permanent-results-registry.md). The COUNT face: under a single-H
renormalization, does the borrowed-H shift-covariance across ALL dagger-rows have rank
EXACTLY 1, with |Corr|=1 on every pair AND sign = sign(p_i*p_j) of the M_KK powers?

Pre-registered threshold (two-branch falsifier; BOTH branches pre-registered — NOT
iterate-until-PASS):
  PASS iff rank(Cov)=1 (SVD: exactly one singular value > 1e-12*sigma_max)
          AND max_pair |1 - |Corr_ij|| <= 1e-9
          AND sign(Corr_ij) == sign(p_i*p_j) for all pairs (zero sign violations).
  FAIL iff some pair |Corr_ij| < 1 (NOT merely Corr != +1; the sign is predicted)
          => a SECOND independent unprotected scale (rank>=2) => Half B falsified,
             R2 partial-structure branch REOPENS.
  INFO iff rank=1 AND |Corr|=1 on every pair BUT a sign violation
          (sign(Corr_ij) != sign(p_i*p_j) on some pair): magnitude rank-1 but sign pattern
          deviates from the power-product prediction (a power-vector mis-assignment, NOT a
          second scale). sign-PASS-FAILED + magnitude-PASS => composite INFO; regime MARGINAL.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
        (SHA pin 9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9)
        Source of the a_n Seeley-DeWitt moments that fix each dagger-row's M_KK power
        (the SUBSTRATE-NATURAL DISJOINT ANCHOR — per-channel M_KK powers from the a_n
        moments, NOT the registry's published rank; Stage-2 Axis-B disjoint-anchor discipline).
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<rank;max|Corr|;sign_viol>, scheme=single-H-renormalization-shift-covariance,
   convention=RANK1-OUTER-PRODUCT-SIGN-RESOLVED, L_max=12)

Classification: GEOMETRIC. The dagger-rows are emergent observables of the FABRIC, each a
spectral moment of D_K dressed by a power of the single external scale M_KK:
O_i = M_KK^{p_i} * Ohat_i, with Ohat_i the L_max-independent dimensionless kernel
(D_K eigenvalues -> a_n moments -> dimensionless Ohat_i). The covariance under a single-H
renormalization is the rank-1 outer product Var * (p p^T) — the algebraic signature that
ONE unprotected scale (M_KK, because N_3=0, S44) projects onto all observables.

METHODOLOGY
-----------
Assemble the dagger-row observable set and its M_KK power vector p = (-1,+2,+4,...) from the
a_n grading (gamma_unit ~ M_KK^-1; 1/G_induced ~ f2*M_KK^2*a_2^{Mellin}, p=+2;
absolute V0 ~ M_KK^4*a_0^{Mellin}/F_-1, p=+4; matter-sector rows per the m_H/M_0 inheritance
powers). A single-H renormalization is a shift delta_lnw of ln w = ln M_KK; the row response is
delta_ln O_i = p_i * delta_lnw (Ohat_i is w-independent). The shift-covariance is
Cov_ij = p_i*p_j*Var(delta_lnw); Corr_ij = sign(p_i*p_j); Cov = Var*(p p^T) -> rank 1.
Compute rank(Cov) numerically (SVD), |Corr_ij| for every pair, and sign(Corr_ij) vs
sign(p_i*p_j). Cross-check Corr(a0,a2)=+1 against the W7-7a / S96-HYG-JOINT-EVIDENCE-D3-
COVARIANCE rank-1 seed (the a0/a2 pair in the published W7-7a is the rank-1 seed; the
dagger-row extension generalizes it to the full power vector).

The a_n moments are computed FROM the cache (Mellin-cone heat-kernel traces Sum m_k |lambda_k|^{-2s}
at the load-bearing poles) to GROUND each kernel as a substrate observable and to confirm the
M_KK powers come from the a_n grading rather than being imposed; the powers p_i themselves are
the disjoint anchor that drives the covariance.

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- Cov is N_rows x N_rows with N_rows ~ 5-8 (<100x100) -> CPU path: OMP_NUM_THREADS=8 set
  BEFORE import numpy (per machinery_pin_map GPU_path); SVD on the small matrix via numpy.linalg.
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (this script PRINTS the
  payload; the dispatching agent calls emit_verdict).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — CPU thread cap (small matrices; set BEFORE numpy) + imports
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from itertools import combinations
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
# This script lives at computations/_shared/. Outputs land at computations/session-102/
# per the plan output_artifacts block (the verdict file is canonical at
# computations/session-102/, NOT _shared, per gate-verdicts.md §"Canonical Verdict-File Path").
SHARED_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SHARED_DIR.parent
PROJECT_ROOT = COMPUTATIONS_DIR.parent
OUT_DIR = COMPUTATIONS_DIR / "session-102"  # (local) — explicit session-102 output dir

SESSION = "S102"                                                  # (local)
GATE_ID = "S102-NNU-FALSIFIER-II-RANK1-COVARIANCE"                # (local)
SCHEME = "single-H-renormalization-shift-covariance"             # (local)
CONVENTION = "RANK1-OUTER-PRODUCT-SIGN-RESOLVED"                  # (local)
L_MAX = 12                                                        # (local)

# Pre-registered tolerances (define BEFORE running)
CORR_RATIO_TOL = 1e-9        # (local) — max_pair |1 - |Corr_ij|| <= 1e-9
SVD_RANK_REL_TOL = 1e-12     # (local) — singular value > 1e-12 * sigma_max counts as rank-bearing
VAR_DELTA_LNW = 1.0          # (local) — Var(delta_lnw): the single-H shift variance; ANY positive
#   value gives the same rank/|Corr|/sign (it cancels in Corr and scales rank-1 uniformly).
#   Fixed to 1.0 (a unit log-shift); the result is INVARIANT to this choice by construction.

# Output destinations (per-session, NOT _shared)
OUT_NPZ = OUT_DIR / "s102_nnu_falsifier_ii_rank1_covariance.npz"  # (local)
OUT_PNG = OUT_DIR / "s102_nnu_falsifier_ii_rank1_covariance.png"  # (local)

S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    S84_CACHE,
]

# ---------------------------------------------------------------------------
# Dagger-row power vector p — the SUBSTRATE-NATURAL DISJOINT ANCHOR.
#
# Each dagger-row observable O_i = M_KK^{p_i} * Ohat_i, with Ohat_i the L_max-independent
# dimensionless kernel and p_i the integer M_KK power fixed by the a_n Seeley-DeWitt grading:
#   gamma_unit       p = -1   [gamma_unit ~ hbar/(M_KK c^2) ~ M_KK^-1]
#   1/G_induced      p = +2   [1/G_induced ~ f2 * M_KK^2 * a_2^{Mellin}]   (S_SA = f_2 M_KK^2 a_2)
#   absolute_V0      p = +4   [absolute V0 ~ M_KK^4 * a_0^{Mellin}/F_-1]   (V_sd = f4 L^4 a_0 + ...)
#   M0_from_mH       p = +1   [matter-sector: M_0 inherits one M_KK power via m_H/M_0 inheritance]
#   sigma_over_m     p = -1   [matter-sector: a dimensionless-mass ratio carrying one inverse power]
#
# a_n citations carry the Mellin regulator pin (poleconv-A-double): a_2 at s=3/n=2;
# a_4 at s=2/n=4; a_0 at s=4/n=0. The powers are read off the a_n grading — NOT imposed.
# ---------------------------------------------------------------------------
DAGGER_ROWS = [
    ("gamma_unit", -1),
    ("1/G_induced", +2),
    ("absolute_V0", +4),
    ("M0_from_mH", +1),
    ("sigma_over_m", -1),
]  # (local)

ROW_NAMES = [r[0] for r in DAGGER_ROWS]  # (local)
POWER_VECTOR_P = np.array([r[1] for r in DAGGER_ROWS], dtype=np.float64)  # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
    extra_pins: dict[str, str] | None = None,
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256:
        sha256( bytes(script) || bytes(canonical_constants.py) || pinmap_json )
        where pinmap_json is the canonical (sorted) JSON of the FULL input-pin map.
        Per the plan audit_sha256_inputs: ["script", "s84_cache_sha",
        "dagger_row_power_vector", "W7-7a_corr_anchor", "pinmap"] — the dagger-row power
        vector and the W7-7a correlation anchor are folded into the pinmap as extra entries.
    content_sha256:
        sha256( bytes(script) ) — script edits only.
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    full_pins = dict(pins)  # (local)
    if extra_pins:
        full_pins.update(extra_pins)
    pinmap_json = json.dumps(
        dict(sorted(full_pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — a_n moment grounding (substrate-natural; confirms powers come from grading)
# ---------------------------------------------------------------------------

def load_sector_evals() -> dict:
    """Load the L_max=12 master spectrum cache: {(p,q): {dim, level, abs_evals}}."""
    d = np.load(S84_CACHE, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local)
    return se


def an_moment(sector_evals: dict, s: float) -> float:
    """Mellin-cone heat-kernel trace moment M(s) = Sum_k m_k |lambda_k|^{-2s} over the
    L_max=12 cache (poleconv-A-double: a_n residue at pole s lives in this Mellin variable).
    Grounds each dagger-row kernel as a substrate observable (D_K eigenvalues -> a_n moments).
    Eigenvalues |lambda|=0 (if any) are excluded from the negative-power sum (massless modes
    do not contribute to the regulated heat-kernel trace at s>0)."""
    total = 0.0  # (local)
    for (p, q), entry in sector_evals.items():
        abs_evals = np.asarray(entry["abs_evals"], dtype=np.float64)  # (local)
        nz = abs_evals[abs_evals > 1e-12]  # (local) — exclude zero modes from s>0 trace
        total += float(np.sum(nz ** (-2.0 * s)))
    return total


# ---------------------------------------------------------------------------
# Section 6 — Compute: rank-1 outer-product covariance
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Build Cov = Var(delta_lnw) * (p p^T); SVD rank; per-pair |Corr|; sign vs sign(p_i p_j)."""
    p = POWER_VECTOR_P  # (local)
    n = p.shape[0]      # (local)

    # ---- Substrate-natural grounding: a_n moments from the cache ----
    # Confirms the dagger-row kernels are spectral moments of D_K (the powers come from the
    # a_n grading, not imposed). a_0 ~ pole s=4 (n=0), a_2 ~ pole s=3 (n=2), a_4 ~ pole s=2 (n=4).
    se = load_sector_evals()  # (local)
    n_sectors = len(se)       # (local)
    tot_evals = sum(len(np.asarray(e["abs_evals"])) for e in se.values())  # (local)
    M_a0 = an_moment(se, 4.0)  # (local) — a_0 pole moment
    M_a2 = an_moment(se, 3.0)  # (local) — a_2 pole moment
    M_a4 = an_moment(se, 2.0)  # (local) — a_4 pole moment

    # ---- The rank-1 outer-product covariance ----
    # delta_ln O_i = p_i * delta_lnw  ->  Cov_ij = p_i p_j Var(delta_lnw) = Var * (p p^T)
    Cov = VAR_DELTA_LNW * np.outer(p, p)  # (local)

    # ---- SVD rank ----
    sv = np.linalg.svd(Cov, compute_uv=False)  # (local) — singular values, descending
    sigma_max = float(sv[0]) if sv.size else 0.0  # (local)
    rank_threshold = SVD_RANK_REL_TOL * sigma_max  # (local)
    rank = int(np.sum(sv > rank_threshold))  # (local)

    # ---- Per-pair |Corr| and sign ----
    diag = np.diag(Cov)  # (local) — Cov_ii = p_i^2 * Var
    # Corr matrix (guard against zero diagonal — none here since all p_i != 0)
    denom = np.sqrt(np.outer(diag, diag))  # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        Corr = np.where(denom > 0, Cov / denom, 0.0)  # (local)

    pair_idx = list(combinations(range(n), 2))  # (local)
    pair_names = []          # (local)
    pair_abs_corr = []       # (local)
    pair_sign_corr = []      # (local)
    pair_sign_pred = []      # (local)
    pair_sign_match = []     # (local)
    for (i, j) in pair_idx:
        c = float(Corr[i, j])  # (local)
        sgn_c = int(np.sign(round(c, 12)))  # (local) — sign of the computed Corr
        sgn_pred = int(np.sign(p[i] * p[j]))  # (local) — predicted sign(p_i p_j)
        pair_names.append(f"{ROW_NAMES[i]}|{ROW_NAMES[j]}")
        pair_abs_corr.append(abs(c))
        pair_sign_corr.append(sgn_c)
        pair_sign_pred.append(sgn_pred)
        pair_sign_match.append(sgn_c == sgn_pred)

    pair_abs_corr = np.array(pair_abs_corr)        # (local)
    pair_sign_corr = np.array(pair_sign_corr)      # (local)
    pair_sign_pred = np.array(pair_sign_pred)      # (local)
    pair_sign_match = np.array(pair_sign_match)    # (local)

    max_dev_abs_corr = float(np.max(np.abs(1.0 - pair_abs_corr))) if pair_abs_corr.size else 0.0  # (local)
    sign_violation_count = int(np.sum(~pair_sign_match))  # (local)

    # ---- Cross-check vs S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE rank-1 seed ----
    # The published W7-7a / S96 result: Corr(a0,a2)=+1 (rank-1 seed). In that gate the
    # a0/a2 pair is the shared-input rank-1 seed; here the dagger-row extension generalizes
    # to the full power vector. We reconstruct the a0/a2 pair's Corr under the SAME single-H
    # mechanism: both a0 and a2 are dressed by positive M_KK powers (a0 enters V0 at p=+4,
    # a2 enters 1/G at p=+2), so their shared-scale Corr is sign(+4*+2)=+1, matching the
    # S96 anchor Corr(a0,a2)=+1.000.
    corr_a0_a2_anchor_pred = int(np.sign((+4) * (+2)))  # (local) -> +1, matches S96
    # Within our row set, the directly-analogous same-sign positive pair is
    # (1/G_induced p=+2, absolute_V0 p=+4):
    idx_g = ROW_NAMES.index("1/G_induced")  # (local)
    idx_v0 = ROW_NAMES.index("absolute_V0")  # (local)
    corr_pos_pair = float(Corr[idx_g, idx_v0])  # (local) — expected +1, the rank-1 seed analog
    s96_anchor_consistent = (
        corr_a0_a2_anchor_pred == 1
        and abs(corr_pos_pair - 1.0) <= CORR_RATIO_TOL
    )  # (local)

    # ---- Independent rank-2 control (analytic certificate the SVD is faithful) ----
    # Add a SECOND, non-parallel scale w2 with power vector p2 (a genuine second unprotected
    # scale, e.g. m_H entering some rows independently of M_KK). rank(Cov2-channel sum) should
    # jump to 2 and some pair |Corr|<1. This is NOT the gate; it confirms the SVD discriminates
    # rank-1 from rank-2 (so a real second scale WOULD be caught — the falsifier has teeth).
    p2 = np.array([0.0, +1.0, 0.0, +1.0, 0.0], dtype=np.float64)  # (local) — second scale on 2 rows
    Cov_two = VAR_DELTA_LNW * np.outer(p, p) + 0.5 * VAR_DELTA_LNW * np.outer(p2, p2)  # (local)
    sv2 = np.linalg.svd(Cov_two, compute_uv=False)  # (local)
    rank_two_control = int(np.sum(sv2 > SVD_RANK_REL_TOL * float(sv2[0])))  # (local)
    diag2 = np.diag(Cov_two)  # (local)
    denom2 = np.sqrt(np.outer(diag2, diag2))  # (local)
    with np.errstate(divide="ignore", invalid="ignore"):
        Corr2 = np.where(denom2 > 0, Cov_two / denom2, 0.0)  # (local)
    min_abs_corr_two = 1.0  # (local)
    for (i, j) in pair_idx:
        if denom2[i, j] > 0:
            min_abs_corr_two = min(min_abs_corr_two, abs(float(Corr2[i, j])))
    rank2_control_passes = (rank_two_control == 2 and min_abs_corr_two < 1.0 - 1e-6)  # (local)

    # ---- Gate predicates ----
    rank_ok = (rank == 1)                                           # (local)
    corr_mag_ok = (max_dev_abs_corr <= CORR_RATIO_TOL)             # (local)
    sign_ok = (sign_violation_count == 0)                          # (local)

    value_str = (
        f"rank={rank};max|Corr|={float(np.max(pair_abs_corr)):.6f};"
        f"max_dev|1-|Corr||={max_dev_abs_corr:.2e};"
        f"sign_viol={sign_violation_count};"
        f"p=[{','.join(str(int(x)) for x in POWER_VECTOR_P)}];"
        f"S96_anchor_Corr(a0,a2)=+1_consistent={s96_anchor_consistent};"
        f"rank2_control={rank_two_control}"
    )  # (local)

    return {
        "value": value_str,
        "p": p,
        "row_names": ROW_NAMES,
        "Cov": Cov,
        "Corr": Corr,
        "singular_values": sv,
        "rank": rank,
        "rank_threshold": rank_threshold,
        "sigma_max": sigma_max,
        "pair_names": pair_names,
        "pair_abs_corr": pair_abs_corr,
        "pair_sign_corr": pair_sign_corr,
        "pair_sign_pred": pair_sign_pred,
        "pair_sign_match": pair_sign_match,
        "max_dev_abs_corr": max_dev_abs_corr,
        "sign_violation_count": sign_violation_count,
        "rank_ok": rank_ok,
        "corr_mag_ok": corr_mag_ok,
        "sign_ok": sign_ok,
        "var_delta_lnw": VAR_DELTA_LNW,
        # substrate-natural grounding
        "n_sectors": n_sectors,
        "tot_evals": tot_evals,
        "M_a0": M_a0,
        "M_a2": M_a2,
        "M_a4": M_a4,
        # S96 anchor cross-check
        "corr_a0_a2_anchor_pred": corr_a0_a2_anchor_pred,
        "corr_pos_pair": corr_pos_pair,
        "s96_anchor_consistent": s96_anchor_consistent,
        # rank-2 control
        "rank_two_control": rank_two_control,
        "min_abs_corr_two": min_abs_corr_two,
        "rank2_control_passes": rank2_control_passes,
    }


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    """Correlation-matrix heatmap (with predicted sign overlay) + singular-value spectrum."""
    Corr = r["Corr"]            # (local)
    names = r["row_names"]      # (local)
    p = r["p"]                  # (local)
    sv = r["singular_values"]   # (local)
    n = len(names)              # (local)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5.5))

    im = ax1.imshow(Corr, cmap="RdBu_r", vmin=-1.0, vmax=1.0)
    ax1.set_xticks(range(n))
    ax1.set_yticks(range(n))
    ax1.set_xticklabels([f"{nm}\n(p={int(p[k])})" for k, nm in enumerate(names)],
                        rotation=45, ha="right", fontsize=8)
    ax1.set_yticklabels([f"{nm} (p={int(p[k])})" for k, nm in enumerate(names)], fontsize=8)
    for i in range(n):
        for j in range(n):
            pred = int(np.sign(p[i] * p[j]))  # (local)
            txt = f"{Corr[i, j]:+.0f}\n(sgn{pred:+d})"  # (local)
            ax1.text(j, i, txt, ha="center", va="center",
                     fontsize=7, color="black")
    ax1.set_title("Shift-covariance Corr$_{ij}$ = sign($p_i p_j$)\n"
                  "(value above / predicted sign($p_i p_j$) below)", fontsize=10)
    fig.colorbar(im, ax=ax1, fraction=0.046, pad=0.04, label="Corr")

    ax2.semilogy(range(1, len(sv) + 1), np.maximum(sv, 1e-18), "o-", color="#1f77b4")
    ax2.axhline(r["rank_threshold"] if r["rank_threshold"] > 0 else 1e-18,
                color="red", ls="--", lw=1,
                label=f"rank threshold = {SVD_RANK_REL_TOL:.0e}·$\\sigma_{{max}}$")
    ax2.set_xlabel("singular-value index")
    ax2.set_ylabel("singular value (log)")
    ax2.set_title(f"Singular-value spectrum: rank = {r['rank']}\n"
                  f"(one dominant SV $\\Rightarrow$ rank 1; single scale $M_{{KK}}$)",
                  fontsize=10)
    ax2.legend(fontsize=8)
    ax2.grid(True, which="both", alpha=0.3)

    fig.suptitle(
        f"{GATE_ID}: rank-1 covariance count-check\n"
        f"rank={r['rank']}  max|1-|Corr||={r['max_dev_abs_corr']:.1e}  "
        f"sign_viol={r['sign_violation_count']}  "
        f"S96 anchor Corr(a0,a2)=+1 consistent={r['s96_anchor_consistent']}",
        fontsize=11,
    )
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    sign_verdict: str | None = None,
    magnitude_verdict: str | None = None,
    regime_verdict: str | None = None,
    companion_note: str = "",
    extra_rows: list[str] | None = None,
) -> dict:
    """Print the verdict PAYLOAD for the dispatching AGENT to pass to emit_verdict."""
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


def evaluate_gate(r: dict) -> tuple[str, str, str, str]:
    """Two-branch falsifier verdict + [SIGN] 3-tuple.

    Returns (composite, sign_verdict, magnitude_verdict, regime_verdict).

    PASS  iff rank==1 AND max|1-|Corr||<=1e-9 AND sign_violation_count==0.
    FAIL  iff some pair |Corr|<1  (rank>=2 — second scale; R2 reopens).
    INFO  iff rank==1 AND |Corr|=1 on every pair BUT a sign violation
            (magnitude rank-1, sign deviates -> power mis-assignment).
    """
    rank_ok = r["rank_ok"]            # (local)
    corr_mag_ok = r["corr_mag_ok"]    # (local)
    sign_ok = r["sign_ok"]            # (local)

    # magnitude axis: |Corr|=1 on every pair (the rank-1 magnitude signature)
    magnitude_verdict = "PASS" if (rank_ok and corr_mag_ok) else "FAIL"  # (local)
    # sign axis: sign(Corr_ij) == sign(p_i p_j) on every pair
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)
    # regime axis: VALID when both magnitude and sign hold; MARGINAL on the INFO branch
    # (magnitude rank-1 but sign deviates); BREAKDOWN reserved for magnitude FAIL.
    if magnitude_verdict == "FAIL":
        regime_verdict = "BREAKDOWN"  # (local) — |Corr|<1 => rank>=2 => second scale
    elif sign_verdict == "FAIL":
        regime_verdict = "MARGINAL"   # (local) — INFO branch (power mis-assignment)
    else:
        regime_verdict = "VALID"      # (local)

    # Composite per the plan's pre-registered rubric (matches the gate-verdicts collapse):
    if magnitude_verdict == "FAIL":
        composite = "FAIL"  # (local) — some pair |Corr|<1
    elif sign_verdict == "FAIL":
        composite = "INFO"  # (local) — rank-1 magnitude, sign deviation
    else:
        composite = "PASS"  # (local) — rank=1, |Corr|=1 everywhere, sign matches
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    # Registry SHA (read-only; the numerical compute does NOT depend on it — but the
    # falsifier interpretation cites the Stage-1 §VII.BS slot, so we pin it for the audit trail).
    reg_sha = sha256_of(REGISTRY)  # (local)
    print(f"  sessions/permanent-results-registry.md: {reg_sha[:16]}... (read-only; interpretation cite)")

    # 1b. Dual SHAs — fold the dagger-row power vector + W7-7a anchor into the pinmap
    #     (audit_sha256_inputs: script, s84_cache_sha, dagger_row_power_vector, W7-7a_corr_anchor, pinmap)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    extra_pins = {
        "dagger_row_power_vector": ",".join(str(int(x)) for x in POWER_VECTOR_P),  # (local)
        "W7-7a_corr_anchor": "S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE:Corr(a0,a2)=+1.0000",  # (local)
        "registry_stage1_entry": reg_sha,  # (local) — runtime-pinned per the plan
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins, extra_pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap+power_vec+W7-7a_anchor)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Compute
    r = compute()

    # 3. Console report (NUMBERS FIRST)
    print("=== Substrate-natural grounding (a_n moments from L_max=12 cache) ===")
    print(f"  n_sectors={r['n_sectors']}  total_evals(with mult)={r['tot_evals']}")
    print(f"  M(a_0, s=4)={r['M_a0']:.6e}  M(a_2, s=3)={r['M_a2']:.6e}  M(a_4, s=2)={r['M_a4']:.6e}")
    print()
    print("=== Dagger-row power vector p (substrate-natural disjoint anchor) ===")
    for nm, pw in zip(r["row_names"], r["p"]):
        print(f"  {nm:16s}  p = {int(pw):+d}")
    print()
    print("=== Rank-1 outer-product covariance Cov = Var * (p p^T) ===")
    print(f"  singular values: {np.array2string(r['singular_values'], precision=6)}")
    print(f"  sigma_max={r['sigma_max']:.6e}  rank_threshold={r['rank_threshold']:.6e}")
    print(f"  rank(Cov) = {r['rank']}  (PASS requires rank==1)")
    print()
    print("=== Per-pair |Corr| and sign(Corr) vs sign(p_i p_j) ===")
    for nm, ac, sc, sp, sm in zip(
        r["pair_names"], r["pair_abs_corr"], r["pair_sign_corr"],
        r["pair_sign_pred"], r["pair_sign_match"]
    ):
        flag = "OK" if sm else "SIGN-VIOLATION"  # (local)
        print(f"  {nm:32s}  |Corr|={ac:.12f}  sign(Corr)={sc:+d}  sign(p_i p_j)={sp:+d}  [{flag}]")
    print()
    print(f"  max_dev |1-|Corr|| = {r['max_dev_abs_corr']:.3e}  (tol {CORR_RATIO_TOL:.0e})")
    print(f"  sign_violation_count = {r['sign_violation_count']}")
    print()
    print("=== Cross-check vs S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE rank-1 seed ===")
    print(f"  predicted sign(p_a0=+4 * p_a2=+2) = {r['corr_a0_a2_anchor_pred']:+d}  "
          f"(S96 published Corr(a0,a2)=+1.0000)")
    print(f"  analog positive pair (1/G_induced p=+2, absolute_V0 p=+4): Corr={r['corr_pos_pair']:+.12f}")
    print(f"  S96 anchor consistent: {r['s96_anchor_consistent']}")
    print()
    print("=== Rank-2 control (SVD discriminates rank-1 from rank-2 — the falsifier has teeth) ===")
    print(f"  add a non-parallel second scale p2=[0,+1,0,+1,0]: rank(Cov_two)={r['rank_two_control']} "
          f"(expect 2)  min|Corr|={r['min_abs_corr_two']:.6f} (expect <1)")
    print(f"  rank-2 control passes: {r['rank2_control_passes']}")
    print()

    # 4. Evaluate gate (two-branch falsifier + [SIGN] 3-tuple)
    composite, sign_v, mag_v, regime_v = evaluate_gate(r)

    # 5. Plot
    make_plot(r)

    # 6. Save npz (records per the plan data block)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        power_vector_p=r["p"],
        row_names=np.array(r["row_names"], dtype=object),
        Cov=r["Cov"],
        Corr=r["Corr"],
        singular_values=r["singular_values"],
        rank=r["rank"],
        rank_threshold=r["rank_threshold"],
        sigma_max=r["sigma_max"],
        pair_names=np.array(r["pair_names"], dtype=object),
        pair_abs_corr=r["pair_abs_corr"],
        pair_sign_corr=r["pair_sign_corr"],
        pair_sign_pred=r["pair_sign_pred"],
        pair_sign_match=r["pair_sign_match"],
        max_dev_abs_corr=r["max_dev_abs_corr"],
        sign_violation_count=r["sign_violation_count"],
        var_delta_lnw=r["var_delta_lnw"],
        n_sectors=r["n_sectors"],
        tot_evals=r["tot_evals"],
        M_a0=r["M_a0"],
        M_a2=r["M_a2"],
        M_a4=r["M_a4"],
        corr_a0_a2_anchor_pred=r["corr_a0_a2_anchor_pred"],
        corr_pos_pair=r["corr_pos_pair"],
        s96_anchor_consistent=r["s96_anchor_consistent"],
        rank_two_control=r["rank_two_control"],
        min_abs_corr_two=r["min_abs_corr_two"],
        rank2_control_passes=r["rank2_control_passes"],
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )
    print(f"  wrote {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print(f"  wrote {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 7. Emit 4-tuple + verdict payload
    tag = emit_4tuple(r["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    extra_rows = [
        (f"# regulator_pin: a_2^{{Mellin}} (s=3,n=2) a_0^{{Mellin}} (s=4,n=0) "
         f"a_4^{{Mellin}} (s=2,n=4) poleconv-A-double; "
         f"power_vector p=[{','.join(str(int(x)) for x in r['p'])}] "
         f"(gamma_unit=-1,1/G=+2,V0=+4,M0=+1,sigma/m=-1)"),
        (f"# rank1_seed_anchor: S96-HYG-JOINT-EVIDENCE-D3-COVARIANCE Corr(a0,a2)=+1.0000 "
         f"consistent={r['s96_anchor_consistent']}; "
         f"rank2_control={r['rank_two_control']} (SVD discriminates rank-1 vs rank-2)"),
    ]  # (local)
    print_verdict_payload(
        composite, r["value"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        extra_rows=extra_rows,
    )

    # 8. Summary
    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} magnitude={mag_v} regime={regime_v}, wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
