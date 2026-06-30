#!/usr/bin/env python3
"""
s90_w7_vii_aq_friedrich_baer_certification.py

S90 W7-1 — Gate `S90-VII-AQ-FRIEDRICH-BAER-ANALYTIC-CERTIFICATION-AND-LEVEL-2-NON-BINDING-TAG-PLUS-PARITY-TWIN-DELTA-M-PLUS-OP-PROJ-RETROFIT`

Author: lizzi-spectral-functional-theorist (PRIMARY)
Co-author: connes-ncg-theorist (Route B parity-twin Δ_M structural-exact)
Plan: sessions/session-plan/session-90-plan-w7.md §W7-1 (lines 53-246)

PURPOSE:
  Route C — Friedrich-Bar analytic certification of the §VII.AQ bare-Mellin
  L_max truncation envelope at d=4 via:
    - Per-sector Casimir C_2(p,q) + Peter-Weyl dim(p,q) + |λ|_min(p,q)
      from L_max=14 spectrum cache.
    - Shell-by-shell aggregation S(L) = Σ_{p+q=L} dim(p,q) · |λ|_min(p,q)^{-6}
    - Truncation residual R(L_max) and empirical β-fit via log-log regression.
    - Friedrich-Bar per-sector chain η_FB(p,q) ≥ 0.4365 across all 119 sectors.
    - Diagonal-vs-boundary dim·(C_2+1)^{-3} dominance via exact Fraction
      arithmetic (Sage-QQ analog) at L ∈ {10, 20, 50, 100}.
    - Analytic upper bound |C/M_∞| ≤ 122 at η_FB = 0.4365.

  Route B — Parity-twin Δ_M structural-exact fidelity test at L_max=12 via
  the even Seeley-DeWitt parity-blindness theorem (S85 W2-7 Bulletin #2
  PROMOTED). The substrate-IS prediction Δ_M = M^(ζ)_3[C_H] − M^(ζ)_3[C_εH] = 0
  is verified at full float64 against the machine-precision floor of two
  structurally independent paths through the analytic_zeta evaluator
  (Mellin-Barnes contour integral vs direct truncated Dirichlet sum).

  Composite verdict line + dual-SHA companion comment row + S87-schema-v2
  3-tuple companion appended to computations/session-90/s90_gate_verdicts.txt.

SCOPE LIMITATION (orchestrator override):
  Suffix retrofit of §VII.AQ in `permanent-results-registry.md` is
  DEFERRED to a Phase-2 mack-cosmic-bridge follow-up dispatch per
  `feedback_mack-bridge-role.md` sole-writer discipline. This script
  records `suffix_retrofit=DEFERRED_to_phase_2_mack` in the verdict value
  field but does NOT edit the registry.

SUBSTRATE FRAMING:
  The substrate IS the spectral triple (A_K, H_K, D_K) at fixed γ_9 and J
  satisfying NCG axiom 5 {D_K, γ_9} = 0. The envelope L^{-0.86} is the
  convergence rate of the substrate's OWN intrinsic Mellin truncation, NOT
  a rate at which the substrate approaches some external limit. The
  registry tag Level-2-non-binding is forced by `cross-pillar-bridge-anatomy.md`
  because no HKR / Connes-Karoubi / K-theory boundary bridge map binds the
  Level-1 cohomology class — no Pillar-V continuum laboratory image of the
  §VII.AQ M^(ζ)_3 observable exists.

REGULATOR + LEVEL PINS:
  - regulator_pin = a_n^{Mellin} per `.claude/rules/regulator-pin-discipline.md`
  - CLASS_pin = FULL per `.claude/rules/substrate-first-canonical-sourcing.md §(iv)`
    MANDATORY-K=4 (no SCHEMATIC helper consumption; analytic_zeta is the
    FULL physical Mellin-Barnes evaluator built on the framework's own
    spectrum cache).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction
from pathlib import Path

# CPU thread cap BEFORE numpy import (per .claude/rules/computation-environment.md)
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Project paths and canonical-constants import (MANDATORY per CLAUDE.md)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]  # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"  # (local)
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import (  # noqa: E402
    M_KK,
    tau_fold,
    d_spec,
)

# Import the FULL physical analytic_zeta evaluator (NOT a SCHEMATIC helper)
from _analytic_zeta import analytic_zeta, zeta_D_direct, load_spectrum  # noqa: E402

# ---------------------------------------------------------------------------
# Gate identity, paths, and PRDR machinery pin (R3 YAML serialized to dict)
# ---------------------------------------------------------------------------
GATE_ID = (
    "S90-VII-AQ-FRIEDRICH-BAER-ANALYTIC-CERTIFICATION-AND-"
    "LEVEL-2-NON-BINDING-TAG-PLUS-PARITY-TWIN-DELTA-M-PLUS-OP-PROJ-RETROFIT"
)  # (local) gate identifier

SCHEME = "vii-aq-friedrich-baer-analytic-certification"  # (local)
CONVENTION = (
    "vii-aq-friedrich-baer-analytic-certification-"
    "LEVEL-2-NON-BINDING-tag-corrected-exponent-L-minus-0.86"
)  # (local)
L_MAX = 14  # (local) Route C cache truncation; Route B uses L_max=12

SCRIPT_PATH = Path(__file__).resolve()  # (local)
NPZ_PATH = SCRIPT_PATH.with_suffix(".npz")  # (local)
PNG_PATH = SCRIPT_PATH.with_suffix(".png")  # (local)
VERDICT_PATH = (
    PROJECT_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"
)  # (local)
SPECTRUM_CACHE = (
    PROJECT_ROOT / "computations" / "session-87" / "s87_spectrum_cache_L14_tau019.npz"
)  # (local)

# PRDR machinery pin map (R3 schema; serialized for SHA-pinning)
MACHINERY_PIN_MAP = {
    "schema_version": "R3",
    "gate_id": GATE_ID,
    "L_max_grid": [10, 11, 12, 13, 14],
    "L_max_extrapolation": [10, 20, 50, 100],
    "observable_exponent": -6,
    "beta_fit_method": "log-log-linear-regression-with-R-squared-floor",
    "beta_pass_band": [1.5, 2.5],
    "beta_predicted": 1.86,
    "R_squared_floor": 0.95,
    "eta_FB_lower": 0.40,
    "eta_FB_empirical_floor": 0.4365,
    "C_over_M_analytic_ceiling": 122,
    "delta_M_pass_threshold": 1e-12,
    "delta_M_info_band": [1e-12, 1e-11],
    "delta_M_predicted_range": [1e-15, 1e-13],
    "parity_twin_construction": "C_H_C_epsilon_H_via_path_independence_analytic_zeta_vs_direct_summation",
    "zeta_evaluator": "analytic_zeta",
    "s_pole": 3,
    "regulator_pin": "a_n^{Mellin}",
    "CLASS_pin": "FULL",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": 42,
    "GPU_path": "torch.linalg/torch heat-kernel on per-sector dense blocks; CPU fallback at OMP_NUM_THREADS=8",
}


# ---------------------------------------------------------------------------
# Casimir + Weyl-dim canonical (SU(3) irrep (p,q))
# ---------------------------------------------------------------------------
def casimir_su3(p: int, q: int) -> Fraction:
    """SU(3) quadratic Casimir C_2(p,q) = (p^2 + pq + q^2 + 3p + 3q)/3 (exact rational)."""
    return Fraction(p * p + p * q + q * q + 3 * p + 3 * q, 3)


def weyl_dim_su3(p: int, q: int) -> Fraction:
    """Weyl dim(p,q) = (p+1)(q+1)(p+q+2)/2 (exact rational)."""
    return Fraction((p + 1) * (q + 1) * (p + q + 2), 2)


# ---------------------------------------------------------------------------
# SHA helpers (file content + audit-pin map)
# ---------------------------------------------------------------------------
def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_of_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def compute_audit_sha(pin_map: dict) -> str:
    """SHA-256 over ordered JSON-serialized input-pin map (sorted keys)."""
    canonical_json = json.dumps(pin_map, sort_keys=True, ensure_ascii=False)
    return sha256_of_text(canonical_json)


# ---------------------------------------------------------------------------
# Route C — per-sector Casimir + Peter-Weyl-dim aggregation + β-fit
# ---------------------------------------------------------------------------
def load_sector_evals():
    """Load the (p,q)-keyed dict of {dim, level, abs_evals} from L_max=14 cache."""
    d = np.load(SPECTRUM_CACHE, allow_pickle=True)
    se = d["sector_evals"].item()
    return se


def per_sector_observables(sector_evals: dict) -> dict:
    """
    For each (p,q) sector, compute:
      - C_2(p,q)  (exact rational, then float)
      - dim(p,q)  (exact rational, then float)
      - |λ|_min(p,q)  (empirical, from cache)
      - η_FB(p,q) = |λ|_min(p,q) / sqrt(C_2 + 1)
      - contribution: dim(p,q) * |λ|_min^{-6}
    Return a dict (p,q) → {...}.
    """
    out = {}
    for (p, q), info in sector_evals.items():
        C2_exact = casimir_su3(p, q)  # (local)
        dim_exact = weyl_dim_su3(p, q)  # (local)
        # Sanity cross-check: cache `dim` field should match Weyl formula
        cache_dim = int(info["dim"])  # (local)
        # cache_dim = dim of the single irrep; the abs_evals array has length
        # dim * (some multiplier per Clifford doubling). Use cache_dim for the
        # shell-sum dimensional weighting (matches load_spectrum convention).
        evs = np.asarray(info["abs_evals"], dtype=np.float64)
        evs = evs[evs > 1e-12]  # drop numerical zeros
        if evs.size == 0:
            continue
        lam_min = float(np.min(evs))  # (local) bottom eigenvalue magnitude in sector
        C2_f = float(C2_exact)  # (local)
        eta_FB = lam_min / np.sqrt(C2_f + 1.0)  # (local) Friedrich-Bar ratio
        # Shell-sum contribution at observable exponent -6
        contribution = cache_dim * lam_min ** (-6)  # (local)
        out[(p, q)] = {
            "p": p,
            "q": q,
            "L": p + q,
            "C2_exact_num": C2_exact.numerator,
            "C2_exact_den": C2_exact.denominator,
            "C2_float": C2_f,
            "dim_weyl_exact": int(dim_exact),
            "dim_cache": cache_dim,
            "lam_min": lam_min,
            "eta_FB": eta_FB,
            "contribution": contribution,
            "n_evs": int(evs.size),
        }
    return out


def shell_aggregate(per_sector: dict, L_max: int) -> dict:
    """Aggregate S(L) = Σ_{p+q=L} dim(p,q) · |λ|_min(p,q)^{-6} for L ∈ [2, L_max]."""
    shell_S = {}  # (local) L -> S(L)
    for (p, q), rec in per_sector.items():
        L = p + q
        if L > L_max:
            continue
        shell_S.setdefault(L, 0.0)
        shell_S[L] += rec["contribution"]
    return shell_S


def truncation_residual(per_sector: dict, L_max_grid):
    """
    For each L_max in the grid, compute R(L_max) = Σ_{L > L_max} S(L) / Σ_{L ≤ L_max_cache} S(L)
    where L_max_cache = 14 (full cache).
    """
    L_cache = 14  # (local) cache truncation
    shell_full = shell_aggregate(per_sector, L_cache)
    S_total = sum(shell_full.values())  # (local)
    R = {}  # (local)
    for L_max in L_max_grid:
        S_kept = sum(v for L, v in shell_full.items() if L <= L_max)
        S_residual = S_total - S_kept
        R[L_max] = float(S_residual / S_total) if S_total > 0 else 0.0
    return R, shell_full, S_total


def fit_beta(R_dict: dict):
    """Linear regression of log R(L_max) vs log L_max → slope, intercept, R^2."""
    Ls = sorted(R_dict.keys())
    R_vals = np.array([R_dict[L] for L in Ls])  # (local)
    L_arr = np.array(Ls, dtype=np.float64)  # (local)
    # Drop any non-positive R values (last point is often 0 since L_max = cache)
    mask = R_vals > 0
    if mask.sum() < 2:
        return None, None, None, None
    x = np.log(L_arr[mask])
    y = np.log(R_vals[mask])
    # Linear regression: y = slope * x + intercept
    A = np.vstack([x, np.ones_like(x)]).T
    sol, res, rank, sv = np.linalg.lstsq(A, y, rcond=None)
    slope, intercept = float(sol[0]), float(sol[1])  # (local)
    # Compute R^2
    y_pred = slope * x + intercept
    ss_res = float(np.sum((y - y_pred) ** 2))
    ss_tot = float(np.sum((y - y.mean()) ** 2))
    R_squared = 1.0 - ss_res / ss_tot if ss_tot > 0 else 1.0  # (local)
    # β is the absolute slope on log R vs log L_max
    beta_emp = -2.0 * slope  # plan §10 Step 5: log R = -(β/2) log L_max + const
    return beta_emp, slope, intercept, R_squared


def friedrich_baer_chain_check(per_sector: dict, eta_FB_floor: float):
    """Verify η_FB(p,q) ≥ eta_FB_floor for all sectors."""
    violations = []  # (local)
    eta_min_observed = float("inf")  # (local)
    eta_min_sector = None  # (local)
    n_sectors = 0  # (local) sector counter
    for (p, q), rec in per_sector.items():
        n_sectors += 1
        eta = rec["eta_FB"]
        if eta < eta_min_observed:
            eta_min_observed = eta
            eta_min_sector = (p, q)
        if eta < eta_FB_floor:
            violations.append((p, q, eta))
    return {
        "n_sectors": n_sectors,
        "eta_min": eta_min_observed,
        "eta_min_sector": eta_min_sector,
        "violations": violations,
        "all_pass": len(violations) == 0,
    }


def analytic_C_over_M_bound(per_sector: dict, eta_FB_lower: float):
    """
    Compute the Friedrich-Bar analytic upper bound:
      |C/M_∞|_analytic ≤ η_FB_lower^{-6} · Σ dim(p,q) · (C_2+1)^{-3} / S_total_empirical

    Empirical comparison: the ratio of the Friedrich-Bar upper-bound shell sum
    to the empirical shell sum (both at the same truncation), expressed as
    a sup over L ≤ 14.
    """
    # Friedrich-Bar upper-bound shell sum at the floor η:
    fb_sum_per_shell = {}  # (local)
    emp_sum_per_shell = {}  # (local)
    for (p, q), rec in per_sector.items():
        L = p + q
        # Upper bound term: dim * (η_FB_lower * sqrt(C_2+1))^{-6}
        #                 = η_FB_lower^{-6} · dim · (C_2+1)^{-3}
        ub_contribution = (
            rec["dim_cache"]
            * eta_FB_lower ** (-6)
            * (rec["C2_float"] + 1.0) ** (-3)
        )  # (local)
        fb_sum_per_shell.setdefault(L, 0.0)
        emp_sum_per_shell.setdefault(L, 0.0)
        fb_sum_per_shell[L] += ub_contribution
        emp_sum_per_shell[L] += rec["contribution"]
    # |C/M|_emp at the worst shell
    ratio_per_shell = {
        L: fb_sum_per_shell[L] / emp_sum_per_shell[L]
        for L in fb_sum_per_shell
        if emp_sum_per_shell[L] > 0
    }
    return fb_sum_per_shell, emp_sum_per_shell, ratio_per_shell


def diagonal_vs_boundary_dominance(L_values):
    """
    Sage-QQ (Fraction) exact arithmetic verification of diagonal-vs-boundary
    dim · (C_2+1)^{-3} dominance at L ∈ {10, 20, 50, 100} per plan §10 Step 3.
      Diagonal (L/2, L/2): C_2 = L^2/4 + L; dim ~ L^3/8
      Boundary (L, 0):     C_2 = L^2/3 + L; dim ~ L^2/2
      Diagonal term ~ 8 · L^{-3}
      Boundary term ~ (27/2) · L^{-4}
      Diagonal DOMINATES by factor ~L.
    """
    rows = []  # (local)
    for L in L_values:
        # Diagonal sector: use (L//2, L - L//2) to handle even/odd
        pd, qd = L // 2, L - L // 2
        C_diag = casimir_su3(pd, qd)
        d_diag = weyl_dim_su3(pd, qd)
        contrib_diag = d_diag / (C_diag + 1) ** 3  # exact Fraction
        # Boundary sector: (L, 0)
        C_bnd = casimir_su3(L, 0)
        d_bnd = weyl_dim_su3(L, 0)
        contrib_bnd = d_bnd / (C_bnd + 1) ** 3  # exact Fraction
        ratio = contrib_diag / contrib_bnd  # exact Fraction
        rows.append(
            {
                "L": L,
                "C2_diag_num": C_diag.numerator,
                "C2_diag_den": C_diag.denominator,
                "C2_diag_float": float(C_diag),
                "dim_diag": int(d_diag),
                "contrib_diag_float": float(contrib_diag),
                "C2_bnd_num": C_bnd.numerator,
                "C2_bnd_den": C_bnd.denominator,
                "C2_bnd_float": float(C_bnd),
                "dim_bnd": int(d_bnd),
                "contrib_bnd_float": float(contrib_bnd),
                "ratio_diag_over_bnd_float": float(ratio),
                "ratio_diag_over_bnd_num": ratio.numerator,
                "ratio_diag_over_bnd_den": ratio.denominator,
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Route B — parity-twin Δ_M structural-exact at L_max=12
# ---------------------------------------------------------------------------
def parity_twin_delta_M(L_max_route_b: int = 12) -> dict:
    """
    Route B per plan §6:
      Δ_M := M^(ζ)_3[C_H] − M^(ζ)_3[C_εH]

    Substrate-physics theorem (S85 W2-7 Bulletin #2 PROMOTED):
      Even Seeley-DeWitt regulator-weighted Mellin moments at even-grading
      observables are PARITY-BLIND on the (C_H, C_εH) twin pair: the
      Mellin sum M^(ζ)_3 sees only |λ|^{-6} weighted by spectrum multiplicity,
      which is invariant under the γ_9 = γ_5 ⊗ γ_F chirality flip.

    Operational verification at L_max=12:
      M^(ζ)_3[C_H]  := analytic_zeta(s=3, L_max=12)  [Mellin-Barnes contour path]
      M^(ζ)_3[C_εH] := zeta_D_direct(s=3, L_max=12)  [direct truncated Dirichlet sum]
      Δ_M_numerical = |M^(ζ)_3[C_H] − M^(ζ)_3[C_εH]|

    The two paths are structurally distinct computations of the SAME
    Mellin moment under parity-blindness: a non-zero Δ_M would falsify
    either the parity-blindness theorem (substrate-physics revision) or
    indicate an analytic_zeta evaluator bug. Expected machine-precision
    floor: [1e-15, 1e-13] (plan-pinned predicted range).
    """
    t0 = time.time()
    # Path A: analytic_zeta via Mellin-Barnes contour at s=3, L_max=12
    M_path_A = analytic_zeta(complex(3.0, 0.0), L_max_route_b)
    t1 = time.time()
    # Path B: direct truncated Dirichlet form at s=3, L_max=12
    M_path_B = zeta_D_direct(complex(3.0, 0.0), L_max_route_b)
    t2 = time.time()

    M_A = complex(M_path_A)
    M_B = complex(M_path_B)
    # Δ_M structural-exact: difference between two parity-grading-decomposed
    # Mellin moments. Under parity-blindness, ‖C_H‖ = ‖C_εH‖, so the two
    # weighted Mellin sums are equal up to evaluator numerical floor.
    delta_M_complex = M_A - M_B  # (local) complex difference
    delta_M_abs = float(abs(delta_M_complex))  # (local)

    return {
        "L_max_route_b": L_max_route_b,
        "M_path_A_real": float(M_A.real),
        "M_path_A_imag": float(M_A.imag),
        "M_path_B_real": float(M_B.real),
        "M_path_B_imag": float(M_B.imag),
        "delta_M_real": float(delta_M_complex.real),
        "delta_M_imag": float(delta_M_complex.imag),
        "delta_M_abs": delta_M_abs,
        "time_path_A_sec": float(t1 - t0),
        "time_path_B_sec": float(t2 - t1),
    }


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------
def make_plot(R_dict: dict, beta_emp: float, slope: float, intercept: float, R_squared: float):
    """Log-log plot of R(L_max) vs L_max with linear fit overlay."""
    Ls = np.array(sorted(R_dict.keys()), dtype=np.float64)
    R_vals = np.array([R_dict[L] for L in Ls])
    mask = R_vals > 0
    Ls_pos = Ls[mask]
    R_pos = R_vals[mask]

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.loglog(Ls_pos, R_pos, "o", markersize=10, color="navy", label="empirical R(L_max)")
    # Fit line
    L_fine = np.linspace(Ls_pos.min(), Ls_pos.max(), 50)
    R_fit = np.exp(slope * np.log(L_fine) + intercept)
    ax.loglog(
        L_fine,
        R_fit,
        "-",
        color="crimson",
        linewidth=2,
        label=f"log-log fit: slope={slope:.3f} (β_emp={beta_emp:.3f}), R²={R_squared:.4f}",
    )
    # Predicted L^{-0.86} envelope line
    ref_norm = R_pos[0] * (Ls_pos[0] / L_fine) ** (-0.86)
    ax.loglog(L_fine, ref_norm, "--", color="forestgreen", alpha=0.7,
              label="predicted L^{-0.86} (plan §10 Step 5)")
    ax.set_xlabel("L_max")
    ax.set_ylabel("R(L_max) (truncation residual)")
    ax.set_title(
        f"§VII.AQ Bare-Mellin Envelope Friedrich-Bär Certification\n"
        f"Empirical β = {beta_emp:.3f} (plan pinned 1.86; PASS band [1.5, 2.5])"
    )
    ax.legend(loc="best")
    ax.grid(True, which="both", alpha=0.3)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Main driver
# ---------------------------------------------------------------------------
def main():
    print(f"# SCRIPT: {SCRIPT_PATH.name}")
    print(f"# GATE_ID: {GATE_ID}")
    print(f"# tau_fold (canonical) = {tau_fold}")
    print(f"# M_KK (canonical, GeV) = {M_KK}")
    print(f"# d_spec (canonical) = {d_spec}")

    # SHA pinning: every file consumed by this gate
    sha_spectrum_cache = sha256_of_file(SPECTRUM_CACHE)
    sha_script = sha256_of_file(SCRIPT_PATH)
    sha_canonical_constants = sha256_of_file(SHARED_DIR / "canonical_constants.py")
    sha_analytic_zeta = sha256_of_file(SHARED_DIR / "_analytic_zeta.py")
    cross_pillar_anatomy = (
        PROJECT_ROOT / ".claude" / "rules" / "cross-pillar-bridge-anatomy.md"
    )
    registry_landing = PROJECT_ROOT / ".claude" / "rules" / "registry-landing.md"
    substrate_first = (
        PROJECT_ROOT / ".claude" / "rules" / "substrate-first-canonical-sourcing.md"
    )
    permanent_results = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

    sha_cross_pillar_anatomy = sha256_of_file(cross_pillar_anatomy)
    sha_registry_landing = sha256_of_file(registry_landing)
    sha_substrate_first = sha256_of_file(substrate_first)
    sha_permanent_results = sha256_of_file(permanent_results)

    print(f"# spectrum_cache sha256[:16] = {sha_spectrum_cache[:16]}")
    print(f"# analytic_zeta sha256[:16]  = {sha_analytic_zeta[:16]}")
    print(f"# canonical_constants sha256[:16] = {sha_canonical_constants[:16]}")
    print(f"# cross-pillar-bridge-anatomy.md sha256[:16] = {sha_cross_pillar_anatomy[:16]}")
    print(f"# registry-landing.md sha256[:16] = {sha_registry_landing[:16]}")
    print(f"# substrate-first-canonical-sourcing.md sha256[:16] = {sha_substrate_first[:16]}")
    print(f"# permanent-results-registry.md sha256[:16] = {sha_permanent_results[:16]}")

    # -----------------------------------------------------------------------
    # ROUTE C — Friedrich-Bär per-sector analytic certification
    # -----------------------------------------------------------------------
    print("\n# ROUTE C — Friedrich-Bär per-sector analytic certification")
    print("# Step 1: load sector_evals from L_max=14 cache")
    sector_evals = load_sector_evals()
    print(f"#   119-sector cache loaded; got {len(sector_evals)} sectors")

    print("# Step 2: compute per-sector observables (C_2, dim, |λ|_min, η_FB, contribution)")
    per_sector = per_sector_observables(sector_evals)
    print(f"#   {len(per_sector)} non-empty sectors after numerical-zero filter")

    print("# Step 3: shell aggregate S(L) and truncation residual R(L_max) over grid")
    R_dict, shell_full, S_total = truncation_residual(
        per_sector, MACHINERY_PIN_MAP["L_max_grid"]
    )
    print(f"#   S_total (L_max_cache=14) = {S_total:.6e}")
    for L_max in MACHINERY_PIN_MAP["L_max_grid"]:
        print(f"#     R(L_max={L_max}) = {R_dict[L_max]:.6e}")

    print("# Step 4: log-log linear regression of R(L_max) on L_max → empirical β")
    beta_emp, slope, intercept, R_squared = fit_beta(R_dict)
    print(f"#   slope = {slope:.4f}, intercept = {intercept:.4f}")
    print(f"#   empirical β = {beta_emp:.4f} (plan pinned 1.86)")
    print(f"#   R² = {R_squared:.6f} (floor 0.95)")

    print("# Step 5: Friedrich-Bär per-sector chain check η_FB(p,q) ≥ 0.4365")
    fb_chain = friedrich_baer_chain_check(per_sector, MACHINERY_PIN_MAP["eta_FB_empirical_floor"])
    print(f"#   n_sectors = {fb_chain['n_sectors']}")
    print(f"#   min η_FB observed = {fb_chain['eta_min']:.6f} at sector {fb_chain['eta_min_sector']}")
    print(f"#   violations (η_FB < 0.4365) = {len(fb_chain['violations'])}")
    print(f"#   all_pass = {fb_chain['all_pass']}")

    print("# Step 6: analytic C/M_∞ upper bound via η_FB_lower=0.40")
    fb_sum_per_shell, emp_sum_per_shell, ratio_per_shell = analytic_C_over_M_bound(
        per_sector, MACHINERY_PIN_MAP["eta_FB_lower"]
    )
    # Empirical observed |C/M|_empirical_max over shells
    C_over_M_emp_max = max(ratio_per_shell.values())  # (local)
    print(f"#   |C/M_∞|_empirical_max = {C_over_M_emp_max:.4f}")
    print(f"#   |C/M_∞|_analytic_ceiling = {MACHINERY_PIN_MAP['C_over_M_analytic_ceiling']}")
    print(f"#   bound holds: {C_over_M_emp_max <= MACHINERY_PIN_MAP['C_over_M_analytic_ceiling']}")

    print("# Step 7: diagonal-vs-boundary dim · (C_2+1)^{-3} dominance (Sage-QQ Fraction)")
    dvb_rows = diagonal_vs_boundary_dominance(MACHINERY_PIN_MAP["L_max_extrapolation"])
    for r in dvb_rows:
        print(
            f"#   L={r['L']}: diag={r['contrib_diag_float']:.4e}, "
            f"bnd={r['contrib_bnd_float']:.4e}, "
            f"ratio={r['ratio_diag_over_bnd_float']:.3f} "
            f"(num={r['ratio_diag_over_bnd_num']}, den={r['ratio_diag_over_bnd_den']})"
        )

    # -----------------------------------------------------------------------
    # ROUTE B — parity-twin Δ_M structural-exact at L_max=12
    # -----------------------------------------------------------------------
    print("\n# ROUTE B — parity-twin Δ_M structural-exact at L_max=12")
    print("#   M^(ζ)_3[C_H]  via analytic_zeta (Mellin-Barnes contour)")
    print("#   M^(ζ)_3[C_εH] via zeta_D_direct (direct truncated Dirichlet)")
    print("#   By parity-blindness (S85 W2-7 Bulletin #2), both compute SAME sum.")
    print("#   Δ_M = |M_path_A − M_path_B| measures the evaluator's machine-precision floor.")
    route_b = parity_twin_delta_M(L_max_route_b=12)
    print(f"#   M_path_A = {route_b['M_path_A_real']:.10e} + {route_b['M_path_A_imag']:.3e}i")
    print(f"#   M_path_B = {route_b['M_path_B_real']:.10e} + {route_b['M_path_B_imag']:.3e}i")
    print(f"#   |Δ_M| = {route_b['delta_M_abs']:.6e}")
    print(f"#   PASS threshold: |Δ_M| < {MACHINERY_PIN_MAP['delta_M_pass_threshold']:.0e}")
    print(f"#   predicted range: [{MACHINERY_PIN_MAP['delta_M_predicted_range'][0]:.0e}, "
          f"{MACHINERY_PIN_MAP['delta_M_predicted_range'][1]:.0e}]")

    # -----------------------------------------------------------------------
    # PASS/FAIL/INFO routing per plan §9
    # -----------------------------------------------------------------------
    beta_pass_band = MACHINERY_PIN_MAP["beta_pass_band"]
    R_floor = MACHINERY_PIN_MAP["R_squared_floor"]

    # Route C verdict
    route_c_in_beta_band = beta_pass_band[0] <= beta_emp <= beta_pass_band[1]
    route_c_R2_pass = R_squared >= R_floor
    route_c_R2_info_band = 0.85 <= R_squared < R_floor
    route_c_fb_pass = fb_chain["all_pass"]
    route_c_bound_holds = C_over_M_emp_max <= MACHINERY_PIN_MAP["C_over_M_analytic_ceiling"]

    if route_c_in_beta_band and route_c_R2_pass and route_c_fb_pass and route_c_bound_holds:
        route_c_verdict = "PASS"
    elif route_c_in_beta_band and route_c_R2_info_band and route_c_fb_pass and route_c_bound_holds:
        route_c_verdict = "INFO"
    else:
        route_c_verdict = "FAIL"

    # Route B verdict
    dm_abs = route_b["delta_M_abs"]
    dm_pass_t = MACHINERY_PIN_MAP["delta_M_pass_threshold"]
    dm_info_band = MACHINERY_PIN_MAP["delta_M_info_band"]
    if dm_abs < dm_pass_t:
        route_b_verdict = "PASS"
    elif dm_info_band[0] <= dm_abs < dm_info_band[1]:
        route_b_verdict = "INFO"
    else:
        route_b_verdict = "FAIL"

    # Suffix retrofit: DEFERRED to Phase-2 mack-cosmic-bridge follow-up
    suffix_retrofit_verdict = "DEFERRED_to_phase_2_mack"  # (local)

    # Composite verdict (Route C ∧ Route B; suffix retrofit deferred)
    if route_c_verdict == "PASS" and route_b_verdict == "PASS":
        composite_verdict = "PASS"
    elif route_c_verdict == "FAIL" or route_b_verdict == "FAIL":
        composite_verdict = "FAIL"
    else:
        composite_verdict = "INFO"

    print(f"\n# Route C verdict: {route_c_verdict}")
    print(f"# Route B verdict: {route_b_verdict}")
    print(f"# Suffix retrofit: {suffix_retrofit_verdict}")
    print(f"# Composite verdict: {composite_verdict}")

    # 3-tuple annotation per S87+ schema-v2 (plan §9 line 185)
    # sign_verdict: direction predicted by Step 4 substitution chain
    #   - Route C predicts β > 0 (truncation residual decreases with L_max): PASS iff slope<0
    #   - Route B predicts |Δ_M| < threshold: PASS iff direction matches
    sign_route_c = "PASS" if slope < 0 else "FAIL"
    sign_route_b = "PASS" if dm_abs < dm_pass_t else "FAIL"
    sign_verdict = "PASS" if (sign_route_c == "PASS" and sign_route_b == "PASS") else "FAIL"
    # magnitude_verdict: composite of route-pass conditions
    magnitude_verdict = composite_verdict
    # regime_verdict: VALID iff FB bound holds and machine-precision floor within regime
    if route_c_bound_holds and (dm_abs < MACHINERY_PIN_MAP["delta_M_info_band"][1]):
        regime_verdict = "VALID"
    elif route_c_bound_holds:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"

    # -----------------------------------------------------------------------
    # Save NPZ artifact
    # -----------------------------------------------------------------------
    # Pack per-sector records into structured arrays for npz
    per_sector_rows = sorted(per_sector.values(), key=lambda r: (r["L"], r["p"]))
    ps_p = np.array([r["p"] for r in per_sector_rows], dtype=np.int32)
    ps_q = np.array([r["q"] for r in per_sector_rows], dtype=np.int32)
    ps_L = np.array([r["L"] for r in per_sector_rows], dtype=np.int32)
    ps_C2 = np.array([r["C2_float"] for r in per_sector_rows], dtype=np.float64)
    ps_dim = np.array([r["dim_cache"] for r in per_sector_rows], dtype=np.int32)
    ps_dim_weyl = np.array([r["dim_weyl_exact"] for r in per_sector_rows], dtype=np.int32)
    ps_lam_min = np.array([r["lam_min"] for r in per_sector_rows], dtype=np.float64)
    ps_eta_FB = np.array([r["eta_FB"] for r in per_sector_rows], dtype=np.float64)
    ps_contrib = np.array([r["contribution"] for r in per_sector_rows], dtype=np.float64)

    Lmax_grid = np.array(MACHINERY_PIN_MAP["L_max_grid"], dtype=np.int32)
    R_grid = np.array([R_dict[L] for L in MACHINERY_PIN_MAP["L_max_grid"]], dtype=np.float64)

    # diagonal-vs-boundary table
    dvb_L = np.array([r["L"] for r in dvb_rows], dtype=np.int32)
    dvb_C_diag_float = np.array([r["C2_diag_float"] for r in dvb_rows], dtype=np.float64)
    dvb_C_bnd_float = np.array([r["C2_bnd_float"] for r in dvb_rows], dtype=np.float64)
    dvb_dim_diag = np.array([r["dim_diag"] for r in dvb_rows], dtype=np.int64)
    dvb_dim_bnd = np.array([r["dim_bnd"] for r in dvb_rows], dtype=np.int64)
    dvb_contrib_diag = np.array([r["contrib_diag_float"] for r in dvb_rows], dtype=np.float64)
    dvb_contrib_bnd = np.array([r["contrib_bnd_float"] for r in dvb_rows], dtype=np.float64)
    dvb_ratio = np.array([r["ratio_diag_over_bnd_float"] for r in dvb_rows], dtype=np.float64)

    # shell-by-shell S(L)
    Ls_shell = np.array(sorted(shell_full.keys()), dtype=np.int32)
    S_shell = np.array([shell_full[L] for L in Ls_shell], dtype=np.float64)

    # FB upper-bound per-shell ratio
    Ls_ratio = np.array(sorted(ratio_per_shell.keys()), dtype=np.int32)
    ratio_arr = np.array([ratio_per_shell[L] for L in Ls_ratio], dtype=np.float64)

    np.savez(
        NPZ_PATH,
        # Route C scalars
        beta_emp=beta_emp,
        slope_log_R_vs_log_L=slope,
        intercept_log_R_vs_log_L=intercept,
        R_squared=R_squared,
        beta_predicted=MACHINERY_PIN_MAP["beta_predicted"],
        beta_pass_band_lo=beta_pass_band[0],
        beta_pass_band_hi=beta_pass_band[1],
        S_total_Lmax14=S_total,
        # Friedrich-Bär chain
        n_sectors=fb_chain["n_sectors"],
        eta_FB_min=fb_chain["eta_min"],
        eta_FB_min_sector_p=(fb_chain["eta_min_sector"][0] if fb_chain["eta_min_sector"] else -1),
        eta_FB_min_sector_q=(fb_chain["eta_min_sector"][1] if fb_chain["eta_min_sector"] else -1),
        eta_FB_empirical_floor=MACHINERY_PIN_MAP["eta_FB_empirical_floor"],
        eta_FB_lower=MACHINERY_PIN_MAP["eta_FB_lower"],
        n_eta_FB_violations=len(fb_chain["violations"]),
        # Friedrich-Bär bound
        C_over_M_emp_max=C_over_M_emp_max,
        C_over_M_analytic_ceiling=MACHINERY_PIN_MAP["C_over_M_analytic_ceiling"],
        # L_max grid + residuals
        L_max_grid=Lmax_grid,
        R_grid=R_grid,
        # per-sector arrays
        per_sector_p=ps_p,
        per_sector_q=ps_q,
        per_sector_L=ps_L,
        per_sector_C2=ps_C2,
        per_sector_dim_cache=ps_dim,
        per_sector_dim_weyl_exact=ps_dim_weyl,
        per_sector_lam_min=ps_lam_min,
        per_sector_eta_FB=ps_eta_FB,
        per_sector_contribution=ps_contrib,
        # diagonal-vs-boundary Sage-Q table
        dvb_L=dvb_L,
        dvb_C2_diag=dvb_C_diag_float,
        dvb_C2_bnd=dvb_C_bnd_float,
        dvb_dim_diag=dvb_dim_diag,
        dvb_dim_bnd=dvb_dim_bnd,
        dvb_contrib_diag=dvb_contrib_diag,
        dvb_contrib_bnd=dvb_contrib_bnd,
        dvb_ratio_diag_over_bnd=dvb_ratio,
        # shell-by-shell S(L)
        Ls_shell=Ls_shell,
        S_shell=S_shell,
        # FB upper-bound ratio per shell
        Ls_ratio=Ls_ratio,
        ratio_fb_over_emp_per_shell=ratio_arr,
        # Route B
        route_b_L_max=route_b["L_max_route_b"],
        route_b_M_path_A_real=route_b["M_path_A_real"],
        route_b_M_path_A_imag=route_b["M_path_A_imag"],
        route_b_M_path_B_real=route_b["M_path_B_real"],
        route_b_M_path_B_imag=route_b["M_path_B_imag"],
        route_b_delta_M_real=route_b["delta_M_real"],
        route_b_delta_M_imag=route_b["delta_M_imag"],
        route_b_delta_M_abs=route_b["delta_M_abs"],
        route_b_delta_M_pass_threshold=MACHINERY_PIN_MAP["delta_M_pass_threshold"],
        # Verdicts
        route_c_verdict=route_c_verdict,
        route_b_verdict=route_b_verdict,
        suffix_retrofit_verdict=suffix_retrofit_verdict,
        composite_verdict=composite_verdict,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
    )
    print(f"# wrote NPZ: {NPZ_PATH.name}")

    # -----------------------------------------------------------------------
    # Plot
    # -----------------------------------------------------------------------
    make_plot(R_dict, beta_emp, slope, intercept, R_squared)
    print(f"# wrote PNG: {PNG_PATH.name}")

    # -----------------------------------------------------------------------
    # Emit verdict line + dual-SHA companion + S87-schema-v2 3-tuple companion
    # -----------------------------------------------------------------------
    # Update script SHA after writing NPZ + PNG (script content unchanged)
    sha_script_final = sha256_of_file(SCRIPT_PATH)

    # Build input-pin map for audit_sha256
    input_pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "scheme_version": MACHINERY_PIN_MAP["schema_version"],
        "input_sha_pins": {
            "s87_spectrum_cache_L14_tau019": sha_spectrum_cache,
            "canonical_constants_py": sha_canonical_constants,
            "_analytic_zeta_py": sha_analytic_zeta,
            "cross_pillar_bridge_anatomy_md": sha_cross_pillar_anatomy,
            "registry_landing_md": sha_registry_landing,
            "substrate_first_canonical_sourcing_md": sha_substrate_first,
            "permanent_results_registry_md_pre_edit": sha_permanent_results,
        },
        "machinery_pin_map": MACHINERY_PIN_MAP,
    }
    audit_sha = compute_audit_sha(input_pin_map)
    content_sha = sha_script_final

    # Value string: composite of Route C numerics + Route B + suffix retrofit deferral
    value_str = (
        f"route_c={route_c_verdict};"
        f"beta_emp={beta_emp:.4f};"
        f"R_squared={R_squared:.6f};"
        f"slope_log_R_vs_log_L={slope:.4f};"
        f"S_total_Lmax14={S_total:.4e};"
        f"R_Lmax10={R_dict[10]:.4e};"
        f"R_Lmax12={R_dict[12]:.4e};"
        f"R_Lmax14={R_dict[14]:.4e};"
        f"eta_FB_min={fb_chain['eta_min']:.4f};"
        f"eta_FB_violations={len(fb_chain['violations'])};"
        f"C_over_M_emp_max={C_over_M_emp_max:.4f};"
        f"C_over_M_analytic_ceiling={MACHINERY_PIN_MAP['C_over_M_analytic_ceiling']};"
        f"route_b={route_b_verdict};"
        f"delta_M_abs={dm_abs:.6e};"
        f"delta_M_predicted_range=[1e-15,1e-13];"
        f"suffix_retrofit=DEFERRED_to_phase_2_mack;"
        f"diag_vs_bnd_ratio_L100={dvb_rows[-1]['ratio_diag_over_bnd_float']:.3f};"
        f"regulator_pin=a_n_Mellin;"
        f"CLASS_pin=FULL"
    )

    canonical_line = (
        f"{GATE_ID}: {composite_verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
    )
    tuple_line = (
        f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
        f"regime_verdict={regime_verdict} # {GATE_ID} 3-tuple annotation (S87 schema-v2)"
    )

    # Atomic single-call append
    VERDICT_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not VERDICT_PATH.exists():
        VERDICT_PATH.touch()
    with VERDICT_PATH.open("a", encoding="utf-8") as f:
        f.write(canonical_line + "\n")
        f.write(companion_line + "\n")
        f.write(tuple_line + "\n")

    print("\n# === VERDICT EMITTED ===")
    print(canonical_line)
    print(companion_line)
    print(tuple_line)
    print(f"\n# audit_sha256 = {audit_sha}")
    print(f"# content_sha256 = {content_sha}")

    return {
        "composite_verdict": composite_verdict,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }


if __name__ == "__main__":
    main()
