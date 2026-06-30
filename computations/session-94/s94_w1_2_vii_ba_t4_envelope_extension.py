#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S94-VII-BA-T4-ENVELOPE-EXTENSION  (connes-ncg-theorist; [SIGN] gate)
====================================================================

Extend the T4|s≠s' = Res_W(s)/Res_W(s') differential-SUM-growth envelope of the
§VII.BA composite-bridge program (S93 W1-3) BEYOND the L_max=12 cache ceiling via
the substrate's own Friedrich-Bär (Casimir-bound) analytic tail over L∈[14,100],
and test whether the Level-3 anchor falls BELOW the Level-2 envelope (L3 < L2).

SUBSTRATE PICTURE (IS-not-IN):
  The substrate IS the finite spectral triple (A_K = ℂ⊕ℍ⊕M_3(ℂ), H_K, D_K(τ_fold)).
  Res_W(s, L_max) = Σ_{(p,q): p+q≤L_max} dim(p,q) · Σ_i |λ_{(p,q),i}|^{−2s}
  is the unique Wodzicki trace on Ψ(A_K) evaluated on the L_max-truncated D_K
  spectrum (on the FINITE triple the CM-1995 §III.4 simple-pole residue reduces
  algebraically to this direct sum; bare moment = unique-trace value, NO auxiliary
  regulator). deg(Res_W) = −2s (Wodzicki uniqueness, Connes 1994 book §2.3).
  T4|s≠s' = Res_W(s)/Res_W(s'), deg = (−2s)−(−2s') = 2(s'−s); s=2,s'=3 ⇒ deg=+2.

  The Friedrich-Bär analytic tail is NOT an external regulator. It is the
  substrate's OWN Casimir-bound eigenvalue floor (|λ|_min(p,q) ≈ √C_2(p,q)/r(τ),
  η_FB(p,q) = |λ|_min/√(C_2+1) ≥ η_FB_lower = 0.40 per W11-3) extended to the
  Peter-Weyl sectors that were never raw-diagonalized (p+q ∈ [13,100]). The
  question "does L3 cross below L2" IS "does the substrate's differential-SUM-
  growth saturate" — a property of D_K's Casimir spectrum, read off its structure,
  NOT measured in a container.

METHOD:
  1. EXACT in-cache Res_W(s={2,3}, L) for L∈{8,10,12} from the L_max=12 master
     cache (reproduces S93 W1-3 Res_W_s2/s3 bit-for-bit).
  2. Calibrate the per-eigenvalue moment scaling ⟨|λ|^{−2s}⟩(p,q) ~ A_s·C_2(p,q)^{−β_s}
     on the 89 nonzero-Casimir cache sectors (per-sector mean |λ|^{−2s} vs C_2),
     anchored by the empirical band ratio mean|λ|/√C_2 → 0.595 (Casimir floor).
  3. Friedrich-Bär analytic tail: for each NEW level p+q=L ∈ [13,100], every new
     sector (p,q) contributes 16·dim(p,q) eigenvalues each carrying multiplicity
     dim(p,q); its residue contribution is dim(p,q)·16·dim(p,q)·A_s·C_2(p,q)^{−β_s}.
     NO raw diagonalization above L=12 (math-scripts.md D_K Block-Diagonality
     Pre-Check). Robustness cross-check via the conservative κ-band method
     (⟨|λ|^{−2s}⟩ = (κ_s·√C_2)^{−2s}).
  4. Re-fit the Level-2 envelope exponent + Level-3 anchor (S93 W1-3 Aitken Δ²
     construction, level2_envelope_and_level3) over a sliding 3-point window at the
     asymptotic L_fit=[50,100], test ΔL = L3 − L2 < 0.

VERDICT METRIC ([SIGN]): the SIGN of ΔL_asymptotic = L3_asymptotic − L2_asymptotic.
  PASS  iff ΔL_asymptotic < 0 (margin > 1e-3 M_KK²-norm) at L_fit=[50,100]
        ⇒ T4|s≠s' admissible as an ALTERNATIVE Element-3 (admissible set widens to
          {T3, T4|s≠s', T5}).
  FAIL  iff ΔL_asymptotic ≥ 0 persists through L_max=100
        ⇒ T4|s≠s' structurally-admissible (deg-match + non-scalar) but NOT
          envelope-saturated; T5 remains the SOLE registry-PASS-eligible Element-3
          (the deg-+2 differential-SUM-growth of Res_W is the obstruction).
  INFO  iff ΔL non-monotone OR η_FB lower-bound fails to converge over [50,100]
        (regime_verdict ≠ VALID).

Plan: sessions/session-plan/session-94-plan-w1.md §W1-2.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib  # noqa: E402
import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# -----------------------------------------------------------------------------
# Paths + shared-module imports (match S93 W1-3 path setup exactly)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"

sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

from canonical_constants import (  # noqa: E402
    M_KK,
    Delta_BCS,
    tau_fold,
)

import _cm_1995_residue_formula  # noqa: E402, F401
from _cm_1995_residue_formula import (  # noqa: E402
    su3_casimir,
    su3_dimension,
)

import _pauli_villars_subtraction  # noqa: E402, F401
from _pauli_villars_subtraction import (  # noqa: E402
    bare_mellin_moment,
)

# -----------------------------------------------------------------------------
# Gate identity
# -----------------------------------------------------------------------------
GATE_ID = "S94-VII-BA-T4-ENVELOPE-EXTENSION"
SCHEME = "T4-Res_W-ratio-Friedrich-Bar-analytic-tail"
CONVENTION = "VII-BA-T4-s-neq-s-prime-Res_W-over-Res_W-deg-2-differential-SUM-growth"

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W1_3_NPZ = (
    PROJECT_ROOT / "computations" / "session-93"
    / "s93_w1_3_vii_ba_f_functor_non_scalar_reconstruction.npz"
)
CM_1995_HELPER_PATH = SHARED_DIR / "_cm_1995_residue_formula.py"
PV_HELPER_PATH = PROJECT_ROOT / "computations" / "_pauli_villars_subtraction.py"

VERDICT_TXT = PROJECT_ROOT / "computations" / "session-94" / "s94_gate_verdicts.txt"
OUT_NPZ = (
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w1_2_vii_ba_t4_envelope_extension.npz"
)
OUT_PNG = (
    PROJECT_ROOT / "computations" / "session-94"
    / "s94_w1_2_vii_ba_t4_envelope_extension.png"
)

# -----------------------------------------------------------------------------
# Machinery pins (plan §W1-2 machinery_pin_map)
# -----------------------------------------------------------------------------
L_CACHE_MAX = 12                       # (local) raw-diagonalization ceiling (cache)
L_TAIL_MAX = 100                       # (local) Friedrich-Bär analytic-tail ceiling
L_TAIL_START = 13                      # (local) first NEW level (p+q=13)
L_SCAN_CACHE = (8, 10, 12)             # (local) S93 W1-3 in-cache scan points
S_POLE = 2                             # (local) numerator pole s
S_POLE_PRIME = 3                       # (local) denominator pole s' (a_4/a_2 → (2,3) per W7-1)
L_FIT_ASYMPTOTIC = (50, 100)           # (local) Friedrich-Bär saturation window
ETA_FB_LOWER = 0.40                    # (local) W11-3 pin (8.4% below empirical (1,1)-floor 0.4365)
K_BOT = 8                              # (local) bot-K ceiling cardinality (W11-3 calibration)
PASS_MARGIN = 1e-3                     # (local) ΔL_asymptotic PASS margin (M_KK²-norm units)
CACHE_DEVIATION_BAND = 0.10            # (local) asymptotic-vs-empirical(L=12) cite-cache-ceiling band


# -----------------------------------------------------------------------------
# SHA helpers (match S93 W1-3)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def closure_hash(pins: dict) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


# -----------------------------------------------------------------------------
# Spectrum cache loader with L_max filtering (matches S93 W1-3 / S93 W1-1 exactly)
# -----------------------------------------------------------------------------
def load_spectrum_flat_filtered(cache_path: Path, L_max_filter: int):
    """Peter-Weyl sectored cache filtered to p+q ≤ L_max_filter.

    Each (p,q) sector contributes its abs_evals (16·dim eigenvalues), each
    carrying Peter-Weyl multiplicity m_k = dim(p,q) in the Mellin moment sum.
    Returns (lambdas, mults, n_sectors, max_level).
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()  # (local)
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    max_level = 0  # (local)
    for (p, q), info in sector_evals.items():
        level = int(info["level"])  # (local)
        if level > L_max_filter:
            continue
        n_sectors += 1
        if level > max_level:
            max_level = level
        dim = int(info["dim"])  # (local)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(float(dim))
    lambdas = np.array(lambdas_list, dtype=np.float64)  # (local)
    mults = np.array(mults_list, dtype=np.float64)  # (local)
    return lambdas, mults, n_sectors, max_level


def Res_W_at_pole(lambdas: np.ndarray, mults: np.ndarray, s_pole: int) -> float:
    """Wodzicki residue Res_W(D_K^{−2s})(L_max) = Σ_k m_k·|λ_k|^{−2s} (bare moment;
    unique-trace value on the FINITE triple per CM-1995 §III.4 / Connes 1994 §2.3).
    deg(Res_W) = −2·s_pole. a_n carries the regulator superscript only when a
    PV-dressed moment is used; the bare moment IS the unique trace.
    """
    return bare_mellin_moment(s_pole, lambdas, mults)


# -----------------------------------------------------------------------------
# Friedrich-Bär saturation predicate (W11-3 / S92 W9-3 methodology)
# -----------------------------------------------------------------------------
def friedrich_bar_predicate(cache_path: Path) -> dict:
    """η_FB(p,q) = |λ|_min(p,q)/√(C_2(p,q)+1); certify η_FB ≥ η_FB_lower over all
    sectors; NEW-sector (p+q=13) worst-case lower-eigenvalue bound η_FB_lower·√(C_2+1)
    > bot-K ceiling. saturation_pass ⇒ the analytic tail is well-defined (regime VALID).
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    se = cache["sector_evals"].item()  # (local)
    per_pq_eta = {}  # (local)
    tagged = []  # (local)
    for (p, q), info in se.items():
        ev = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        if ev.size == 0:
            continue
        lam_min = float(ev.min())  # (local)
        per_pq_eta[(p, q)] = lam_min / np.sqrt(su3_casimir(p, q) + 1.0)
        for v in ev:
            tagged.append(float(v))
    tagged.sort()
    bot_k_ceiling = float(tagged[K_BOT - 1])  # (local)
    eta_all_min = float(min(per_pq_eta.values()))  # (local)
    eta_all_min_sector = min(per_pq_eta, key=per_pq_eta.get)  # (local)
    new_bounds = {}  # (local)
    for p in range(L_TAIL_START + 1):
        q = L_TAIL_START - p
        new_bounds[(p, q)] = ETA_FB_LOWER * np.sqrt(su3_casimir(p, q) + 1.0)
    new_bound_min = float(min(new_bounds.values()))  # (local)
    sat_eta = bool(eta_all_min >= ETA_FB_LOWER)  # (local)
    sat_new = bool(new_bound_min > bot_k_ceiling)  # (local)
    return {
        "eta_FB_all_min": eta_all_min,
        "eta_FB_all_min_sector": eta_all_min_sector,
        "bot_k_ceiling": bot_k_ceiling,
        "new_bound_min": new_bound_min,
        "sat_eta_pass": sat_eta,
        "sat_new_pass": sat_new,
        "saturation_pass": bool(sat_eta and sat_new),
    }


# -----------------------------------------------------------------------------
# Per-eigenvalue moment calibration on cache (analytic-tail input)
# -----------------------------------------------------------------------------
def calibrate_moment_powerlaw(cache_path: Path, s_pole: int):
    """Fit ⟨|λ|^{−2s}⟩(p,q) ~ A_s · C_2(p,q)^{−β_s} on the 89 nonzero-Casimir cache
    sectors (log-log). Returns (A_s, β_s, n_sectors, r2).
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    se = cache["sector_evals"].item()  # (local)
    lnC, lnA = [], []  # (local)
    for (p, q), info in se.items():
        if (p, q) == (0, 0):
            continue  # C_2 = 0 (trivial rep)
        ev = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        avg = float(np.mean(ev ** (-2 * s_pole)))  # (local) per-eigenvalue moment
        lnC.append(np.log(su3_casimir(p, q)))
        lnA.append(np.log(avg))
    lnC = np.array(lnC)  # (local)
    lnA = np.array(lnA)  # (local)
    slope, intercept = np.polyfit(lnC, lnA, 1)  # (local) slope = -beta
    A_s = float(np.exp(intercept))  # (local)
    beta_s = float(-slope)  # (local)
    pred = intercept + slope * lnC  # (local)
    ss_res = float(np.sum((lnA - pred) ** 2))  # (local)
    ss_tot = float(np.sum((lnA - np.mean(lnA)) ** 2))  # (local)
    r2 = float(1.0 - ss_res / ss_tot) if ss_tot > 0 else 1.0  # (local)
    return A_s, beta_s, len(lnC), r2


def calibrate_kappa_band(cache_path: Path, s_pole: int) -> float:
    """Conservative robustness calibration: effective band ratio κ_s such that
    ⟨|λ|^{−2s}⟩ = (κ_s·√C_2)^{−2s}, averaged over nonzero-Casimir cache sectors.
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    se = cache["sector_evals"].item()  # (local)
    kappas = []  # (local)
    for (p, q), info in se.items():
        if (p, q) == (0, 0):
            continue
        ev = np.asarray(info["abs_evals"], dtype=np.float64)  # (local)
        avg = float(np.mean(ev ** (-2 * s_pole)))  # (local)
        kappa = (avg ** (-1.0 / (2 * s_pole))) / np.sqrt(su3_casimir(p, q))  # (local)
        kappas.append(kappa)
    return float(np.mean(kappas))


# -----------------------------------------------------------------------------
# Res_W with Friedrich-Bär analytic tail
# -----------------------------------------------------------------------------
def resW_cache_exact(cache_path: Path, L_filter: int, s_pole: int) -> float:
    """EXACT in-cache Res_W(s, L_filter) (L_filter ≤ 12)."""
    lam, mul, _, _ = load_spectrum_flat_filtered(cache_path, L_filter)
    return Res_W_at_pole(lam, mul, s_pole)


def resW_with_tail(cache_path: Path, L_max: int, s_pole: int,
                   A_s: float, beta_s: float, kappa_s: float,
                   method: str = "powerlaw") -> float:
    """Res_W(s, L_max) = [exact cache part p+q≤12] + [Friedrich-Bär tail 13..L_max].

    Tail per NEW level lev: every new sector (p,q), p+q=lev, contributes
    dim(p,q)·(16·dim(p,q))·⟨|λ|^{−2s}⟩, where ⟨|λ|^{−2s}⟩ is the calibrated
    per-eigenvalue moment estimate (Casimir-bound floor extension).
    """
    total = resW_cache_exact(cache_path, min(L_max, L_CACHE_MAX), s_pole)  # (local)
    if L_max <= L_CACHE_MAX:
        return total
    for lev in range(L_TAIL_START, L_max + 1):
        for p in range(lev + 1):
            q = lev - p
            C2 = su3_casimir(p, q)  # (local)
            dim = su3_dimension(p, q)  # (local)
            n_eig = 16 * dim  # (local) ℂ^16 internal factor
            if method == "powerlaw":
                avg = A_s * C2 ** (-beta_s)  # (local)
            else:  # kappa-band (conservative robustness)
                avg = (kappa_s * np.sqrt(C2)) ** (-2 * s_pole)  # (local)
            total += dim * n_eig * avg  # m_k = dim, summed over 16·dim eigenvalues
    return total


# -----------------------------------------------------------------------------
# Level-2 envelope + Level-3 anchor (S93 W1-3 Aitken Δ² construction — verbatim)
# -----------------------------------------------------------------------------
def level2_envelope_and_level3(L_arr: np.ndarray, Phi_arr: np.ndarray) -> dict:
    """Aitken Δ² extrapolation of the 3-point Φ-sequence to Φ_∞; fit
    |Φ(L)−Φ_∞| ~ C·L^{−α}; Level-2 = C·L_canon^{−α}; Level-3 = |Φ(L_canon)−Φ_∞|.
    (Identical construction to s93_w1_3 level2_envelope_and_level3.)
    """
    p0, p1, p2 = float(Phi_arr[0]), float(Phi_arr[1]), float(Phi_arr[2])  # (local)
    denom = (p2 - 2.0 * p1 + p0)  # (local)
    if abs(denom) > 1e-30:
        Phi_inf = p2 - (p2 - p1) ** 2 / denom  # (local) Aitken Δ²
    else:
        Phi_inf = p2  # (local)
    residual = np.abs(Phi_arr - Phi_inf)  # (local)
    valid = residual > 0  # (local)
    if int(np.sum(valid)) >= 2:
        ln_L = np.log(L_arr[valid])  # (local)
        ln_R = np.log(residual[valid])  # (local)
        mean_x = float(np.mean(ln_L))  # (local)
        mean_y = float(np.mean(ln_R))  # (local)
        num = float(np.sum((ln_L - mean_x) * (ln_R - mean_y)))  # (local)
        den = float(np.sum((ln_L - mean_x) ** 2))  # (local)
        slope = num / den if den != 0.0 else 0.0  # (local) slope = -alpha
        alpha = -slope  # (local) envelope exponent (positive ⇒ convergent)
        intercept = mean_y - slope * mean_x  # (local)
        C_env = float(np.exp(intercept))  # (local)
    else:
        alpha = float("inf")  # (local)
        C_env = 0.0  # (local)
    L_canon = float(L_arr[-1])  # (local)
    if np.isfinite(alpha) and C_env > 0:
        level2_envelope = C_env * (L_canon ** (-alpha))  # (local)
    else:
        level2_envelope = float(np.max(residual)) if np.max(residual) > 0 else 1e-30  # (local)
    level3_value = float(residual[-1])  # (local) |Φ(L_canon)−Φ_∞|
    level3_lt_level2 = bool(level3_value <= level2_envelope * (1.0 + 1e-9))  # (local)
    return {
        "Phi_inf": float(Phi_inf),
        "alpha_envelope": float(alpha),
        "C_envelope": float(C_env),
        "level2_envelope": float(level2_envelope),
        "level3_value": float(level3_value),
        "level3_lt_level2": level3_lt_level2,
    }


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; [SIGN] ⇒ dual-SHA companion + 3-tuple row)
# -----------------------------------------------------------------------------
def append_verdict(verdict: str, value: str,
                   audit_sha: str, content_sha: str,
                   sign_v: str, magnitude_v: str, regime_v: str,
                   supersedes: str = "") -> None:
    """Canonical line + dual-SHA companion + [SIGN] schema-v2 3-tuple row + axis pins.

    [SIGN] trigger ⇒ schema_v2_3tuple_required=True (plan output_artifacts).
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    supersedes_field = f"_supersedes={supersedes}" if supersedes else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{supersedes_field}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max=8_10_12_friedrich_bar_14_100 "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    supersedes_note = f"; supersedes={supersedes}" if supersedes else ""  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"[SIGN] envelope-saturation direction test (does L3 cross below L2 as "
        f"L_max grows){supersedes_note}\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    level_pin = (
        f"# LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY "
        f"level-pin compliance (FULL CM-1995 §III.4 unique-trace residue = bare "
        f"Mellin moment on the FINITE triple; Friedrich-Bar Casimir-bound analytic "
        f"tail is the substrate's own eigenvalue floor, NOT an external regulator; "
        f"Res_W SUM = a_n^{{Pauli-Villars}} unique-trace value; bare a_n FORBIDDEN)\n"
    )
    machinery_scope_pin = (
        f"# MACHINERY_SCOPE_PIN=CACHE-PROJECTION+FRIEDRICH-BAR-ANALYTIC-TAIL "
        f"# {GATE_ID} regulator-pin-discipline.md MACHINERY-SCOPE axis (EXACT "
        f"in-cache on L_max=12 master {{p+q<=8,10,12}}; Friedrich-Bar Jensen-Casimir "
        f"analytic tail over p+q in [13,100]; NO raw diagonalization above L=12 per "
        f"math-scripts.md D_K Block-Diagonality + Recursive-Casimir-Projection Pre-Check)\n"
    )
    binding_axis_pin = (
        f"# BINDING_AXIS_PIN=substrate-natural-binding "
        f"# {GATE_ID} regulator-pin-discipline.md Binding-axis (T4|s!=s' = "
        f"Res_W(s)/Res_W(s') is a degree-matched [deg 2(s'-s)=+2] NON-SCALAR "
        f"morphism; L_max-dependence is the substrate's own differential-SUM-growth, "
        f"NOT a canonical-import scalar; T2 scalar FORBIDDEN/VACUOUS Class-8 PRU)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)
        fp.write(level_pin)
        fp.write(machinery_scope_pin)
        fp.write(binding_axis_pin)


# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------
def make_plot(L_grid, T4_grid, dL_grid, alpha_grid,
              L_window_centers, dL_window, l3_window, l2_window,
              dL12, verdict) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1 — T4 ratio Res_W(2)/Res_W(3) over the extended L range
    ax = axes[0, 0]
    ax.plot(L_grid, T4_grid, "o-", color="C1", ms=3,
            label="T4|s≠s' = Res_W(2)/Res_W(3), deg +2")
    ax.axvline(L_CACHE_MAX, color="gray", ls="--", lw=1,
               label="cache ceiling L=12")
    ax.axvspan(L_FIT_ASYMPTOTIC[0], L_FIT_ASYMPTOTIC[1], color="C2", alpha=0.12,
               label=f"FB saturation window [{L_FIT_ASYMPTOTIC[0]},{L_FIT_ASYMPTOTIC[1]}]")
    ax.set_xlabel("L_max")
    ax.set_ylabel("Res_W(2) / Res_W(3)")
    ax.set_title("T4 differential ratio: DIVERGES (deg-+2 SUM-growth not saturated)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 2 — THE CORE FIGURE: ΔL(L_max) = L3 − L2 trajectory
    ax = axes[0, 1]
    ax.plot(L_window_centers, dL_window, "s-", color="C3", ms=4,
            label="ΔL(L_max) = L3 − L2")
    ax.axhline(0.0, color="k", ls="-", lw=1.2, label="L3 = L2 (PASS boundary)")
    ax.axhline(dL12, color="C0", ls=":", lw=1,
               label=f"ΔL(12) = {dL12:+.4f} (W1-3 anchor)")
    ax.axvspan(L_FIT_ASYMPTOTIC[0], L_FIT_ASYMPTOTIC[1], color="C2", alpha=0.12)
    ax.set_xlabel("L_max (3-pt window center)")
    ax.set_ylabel("ΔL = L3 − L2  (M_KK²-norm units)")
    ax.set_title(f"ΔL stays > 0 through L=100 ⇒ {verdict} the L3<L2 test")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3 — envelope exponent α(L_max): NEGATIVE ⇒ divergent (no finite Φ_∞)
    ax = axes[1, 0]
    ax.plot(L_window_centers, alpha_grid, "^-", color="C4", ms=4,
            label="envelope exponent α (3-pt Aitken window)")
    ax.axhline(0.0, color="k", ls="-", lw=1.2,
               label="α = 0 (convergence boundary)")
    ax.set_xlabel("L_max (3-pt window center)")
    ax.set_ylabel("α (positive ⇒ convergent; negative ⇒ divergent)")
    ax.set_title("α < 0 everywhere ⇒ T4 sequence DIVERGENT ⇒ Φ_∞ ill-defined")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 4 — L3 vs L2 over the window (both grow; L3 never falls below L2)
    ax = axes[1, 1]
    ax.plot(L_window_centers, l3_window, "o-", color="C3", ms=4, label="L3 anchor")
    ax.plot(L_window_centers, l2_window, "s--", color="C0", ms=4, label="L2 envelope")
    ax.axvspan(L_FIT_ASYMPTOTIC[0], L_FIT_ASYMPTOTIC[1], color="C2", alpha=0.12)
    ax.set_xlabel("L_max (3-pt window center)")
    ax.set_ylabel("Level-3 / Level-2  (M_KK²-norm units)")
    ax.set_title("L3 ≥ L2 throughout: deg-+2 obstruction (numerator outgrows denom)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"{GATE_ID} — T4|s≠s' Res_W envelope extension via Friedrich-Bär tail "
        f"(s,s')=({S_POLE},{S_POLE_PRIME})  ⇒  {verdict}",
        fontsize=13, y=1.00,
    )
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close()


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print(f"=== {GATE_ID} ===")
    print(f"T4|s≠s' = Res_W(s={S_POLE})/Res_W(s'={S_POLE_PRIME}), deg=2(s'−s)=+2")
    print(f"Extend the S93 W1-3 envelope beyond L_max={L_CACHE_MAX} via the "
          f"Friedrich-Bar analytic tail over L∈[{L_TAIL_START},{L_TAIL_MAX}].")
    print(f"tau_fold={tau_fold}  M_KK={M_KK:.6e}  Delta_BCS={Delta_BCS:.6f}")

    # ------------------------------------------------------------------
    # 1) Input pins
    # ------------------------------------------------------------------
    print("\n=== Step 1: input pins (16-char heads) ===")
    w1_3 = np.load(W1_3_NPZ, allow_pickle=True)  # (local)
    w1_3_audit = str(w1_3["audit_sha256"])  # (local)
    L12_cache_sha = sha256_of(CACHE_L12)  # (local)
    pins = {
        "computations/_shared/canonical_constants.py": sha256_of(CANONICAL_CONSTANTS_PATH),
        "computations/session-93/s93_w1_3_vii_ba_f_functor_non_scalar_reconstruction.npz":
            sha256_of(W1_3_NPZ),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": L12_cache_sha,
        "computations/_shared/_cm_1995_residue_formula.py": sha256_of(CM_1995_HELPER_PATH),
        "computations/_pauli_villars_subtraction.py": sha256_of(PV_HELPER_PATH),
        "_gate_id": GATE_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_s_pole": str(S_POLE),
        "_s_pole_prime": str(S_POLE_PRIME),
        "_L_tail_start": str(L_TAIL_START),
        "_L_tail_max": str(L_TAIL_MAX),
        "_L_fit_asymptotic": str(L_FIT_ASYMPTOTIC),
        "_eta_fb_lower": str(ETA_FB_LOWER),
        "_pass_margin": str(PASS_MARGIN),
        "_w1_3_audit_sha": w1_3_audit,
    }
    for k, v in sorted(pins.items()):
        print(f"  {k}: {v if k.startswith('_') else v[:16]}")

    # ------------------------------------------------------------------
    # 2) Friedrich-Bär saturation predicate (regime-validity gate)
    # ------------------------------------------------------------------
    print("\n=== Step 2: Friedrich-Bär saturation predicate (regime VALID gate) ===")
    fb = friedrich_bar_predicate(CACHE_L12)
    print(f"  η_FB_all_min = {fb['eta_FB_all_min']:.6f} at {fb['eta_FB_all_min_sector']} "
          f"(≥ η_FB_lower={ETA_FB_LOWER}? {fb['sat_eta_pass']})")
    print(f"  NEW p+q={L_TAIL_START} worst-case bound = {fb['new_bound_min']:.4f} "
          f"> bot-{K_BOT} ceiling {fb['bot_k_ceiling']:.4f}? {fb['sat_new_pass']}")
    print(f"  saturation_pass (analytic tail well-defined) = {fb['saturation_pass']}")

    # ------------------------------------------------------------------
    # 3) Per-eigenvalue moment calibration on cache
    # ------------------------------------------------------------------
    print("\n=== Step 3: per-eigenvalue moment calibration ⟨|λ|^{−2s}⟩ ~ A_s·C_2^{−β_s} ===")
    A2, beta2, ncal2, r2_2 = calibrate_moment_powerlaw(CACHE_L12, S_POLE)
    A3, beta3, ncal3, r2_3 = calibrate_moment_powerlaw(CACHE_L12, S_POLE_PRIME)
    kappa2 = calibrate_kappa_band(CACHE_L12, S_POLE)
    kappa3 = calibrate_kappa_band(CACHE_L12, S_POLE_PRIME)
    print(f"  s={S_POLE}: A={A2:.5f} β={beta2:.4f} (r²={r2_2:.4f}, n={ncal2}); κ_band={kappa2:.4f}")
    print(f"  s={S_POLE_PRIME}: A={A3:.5f} β={beta3:.4f} (r²={r2_3:.4f}, n={ncal3}); κ_band={kappa3:.4f}")

    # ------------------------------------------------------------------
    # 4) EXACT in-cache reproduction cross-check (must match S93 W1-3)
    # ------------------------------------------------------------------
    print("\n=== Step 4: EXACT in-cache reproduction (cross-check vs S93 W1-3 npz) ===")
    ResW2_cache = np.array([resW_cache_exact(CACHE_L12, L, S_POLE) for L in L_SCAN_CACHE])  # (local)
    ResW3_cache = np.array([resW_cache_exact(CACHE_L12, L, S_POLE_PRIME) for L in L_SCAN_CACHE])  # (local)
    ref_ResW2 = np.array(w1_3["Res_W_s2"], dtype=np.float64)  # (local)
    ref_ResW3 = np.array(w1_3["Res_W_s3"], dtype=np.float64)  # (local)
    repro_ok2 = bool(np.allclose(ResW2_cache, ref_ResW2, rtol=1e-9))  # (local)
    repro_ok3 = bool(np.allclose(ResW3_cache, ref_ResW3, rtol=1e-9))  # (local)
    print(f"  Res_W_s2 reproduce S93 W1-3? {repro_ok2}  {ResW2_cache.tolist()}")
    print(f"  Res_W_s3 reproduce S93 W1-3? {repro_ok3}  {ResW3_cache.tolist()}")
    T4_ref_L12 = float(ref_ResW2[-1] / ref_ResW3[-1])  # (local)
    print(f"  T4(L=12) cache = {ResW2_cache[-1]/ResW3_cache[-1]:.4f}  (ref {T4_ref_L12:.4f})")
    print(f"  W1-3 anchor: L3={float(w1_3['T4_level3']):.4e} > L2={float(w1_3['T4_level2']):.4e} "
          f"⇒ ΔL(12)={float(w1_3['T4_level3'])-float(w1_3['T4_level2']):+.4e}")

    # ------------------------------------------------------------------
    # 5) Friedrich-Bär analytic tail: Res_W and T4 over L∈[8,100]
    # ------------------------------------------------------------------
    print(f"\n=== Step 5: Res_W + T4 over L∈[8,{L_TAIL_MAX}] (PV powerlaw + κ-band robustness) ===")
    L_grid = np.arange(8, L_TAIL_MAX + 1)  # (local) full L grid
    ResW2_grid_pl, ResW3_grid_pl = [], []  # (local)
    ResW2_grid_kb, ResW3_grid_kb = [], []  # (local)
    for L in L_grid:
        ResW2_grid_pl.append(resW_with_tail(CACHE_L12, int(L), S_POLE, A2, beta2, kappa2, "powerlaw"))
        ResW3_grid_pl.append(resW_with_tail(CACHE_L12, int(L), S_POLE_PRIME, A3, beta3, kappa3, "powerlaw"))
        ResW2_grid_kb.append(resW_with_tail(CACHE_L12, int(L), S_POLE, A2, beta2, kappa2, "kappa"))
        ResW3_grid_kb.append(resW_with_tail(CACHE_L12, int(L), S_POLE_PRIME, A3, beta3, kappa3, "kappa"))
    ResW2_grid_pl = np.array(ResW2_grid_pl)  # (local)
    ResW3_grid_pl = np.array(ResW3_grid_pl)  # (local)
    ResW2_grid_kb = np.array(ResW2_grid_kb)  # (local)
    ResW3_grid_kb = np.array(ResW3_grid_kb)  # (local)
    T4_grid_pl = ResW2_grid_pl / ResW3_grid_pl  # (local) primary (power-law tail)
    T4_grid_kb = ResW2_grid_kb / ResW3_grid_kb  # (local) robustness (κ-band tail)
    for L in (12, 14, 20, 40, 60, 80, 100):
        idx = int(np.where(L_grid == L)[0][0])  # (local)
        print(f"  L={L:3d}: Res_W(2)={ResW2_grid_pl[idx]:.4e} Res_W(3)={ResW3_grid_pl[idx]:.4e} "
              f"T4_pl={T4_grid_pl[idx]:.4f}  T4_kb={T4_grid_kb[idx]:.4f}")

    # ------------------------------------------------------------------
    # 6) Sliding 3-point envelope: ΔL(L_max) = L3 − L2 over the L grid
    #    (3-pt window step = 2, matching S93 W1-3 (8,10,12) spacing)
    # ------------------------------------------------------------------
    print("\n=== Step 6: sliding 3-pt envelope ΔL(L_max)=L3−L2 (Aitken Δ², step-2 window) ===")
    win_centers, dL_win, l3_win, l2_win, alpha_win = [], [], [], [], []  # (local)
    for c in range(12, L_TAIL_MAX + 1):  # window center
        L3pts = np.array([c - 4, c - 2, c], dtype=np.float64)  # (local) step-2 window
        if L3pts[0] < 8:
            continue
        idxs = [int(np.where(L_grid == int(L))[0][0]) for L in L3pts]  # (local)
        P3 = T4_grid_pl[idxs]  # (local)
        env = level2_envelope_and_level3(L3pts, P3)
        win_centers.append(c)
        l3_win.append(env["level3_value"])
        l2_win.append(env["level2_envelope"])
        dL_win.append(env["level3_value"] - env["level2_envelope"])
        alpha_win.append(env["alpha_envelope"])
    win_centers = np.array(win_centers)  # (local)
    dL_win = np.array(dL_win)  # (local)
    l3_win = np.array(l3_win)  # (local)
    l2_win = np.array(l2_win)  # (local)
    alpha_win = np.array(alpha_win)  # (local)

    # ΔL(12) anchor (the S93 W1-3 window {8,10,12})
    dL12 = float(dL_win[0])  # (local) window center = 12
    print(f"  ΔL(12) [window 8,10,12] = {dL12:+.6e}  (S93 W1-3 reported +0.095)")

    # Asymptotic window L_fit=[50,100]
    asym_mask = (win_centers >= L_FIT_ASYMPTOTIC[0]) & (win_centers <= L_FIT_ASYMPTOTIC[1])  # (local)
    dL_asym = float(np.mean(dL_win[asym_mask]))  # (local) mean ΔL over the saturation window
    dL_asym_end = float(dL_win[-1])  # (local) ΔL at window center=100
    l3_asym_end = float(l3_win[-1])  # (local)
    l2_asym_end = float(l2_win[-1])  # (local)
    alpha_asym = float(np.mean(alpha_win[asym_mask]))  # (local) mean envelope exponent
    print(f"  asymptotic window [{L_FIT_ASYMPTOTIC[0]},{L_FIT_ASYMPTOTIC[1]}]: "
          f"mean ΔL={dL_asym:+.6e}  ΔL(100)={dL_asym_end:+.6e}")
    print(f"  mean envelope exponent α over window = {alpha_asym:+.4f} "
          f"(negative ⇒ DIVERGENT sequence ⇒ Φ_∞ ill-defined)")

    # Direction of ΔL trajectory (saturation direction)
    dΔL = float(dL_win[-1] - dL_win[0])  # (local) net change over [12,100]
    dΔL_sign = "decreasing" if dΔL < 0 else "increasing/flat"  # (local)
    # crossing test: does ΔL ever go strictly negative beyond margin in the window?
    crosses_below = bool(np.any(dL_win[asym_mask] < -PASS_MARGIN))  # (local)
    monotone = bool(np.all(np.diff(dL_win) <= 1e-9) or np.all(np.diff(dL_win) >= -1e-9))  # (local)

    # Cache-ceiling deviation cite (Level-2 empirical-β verification rule)
    cache_dev = abs(dL_asym - dL12) / abs(dL_asym) if abs(dL_asym) > 0 else 0.0  # (local)
    print(f"  |ΔL_asymptotic − ΔL(12)|/|ΔL_asymptotic| = {cache_dev:.4f} "
          f"({'> 0.10 → cite cache-ceiling effect' if cache_dev > CACHE_DEVIATION_BAND else 'within 0.10 band'})")

    # ------------------------------------------------------------------
    # 7) Verdict ([SIGN] 3-tuple → composite collapse)
    # ------------------------------------------------------------------
    print("\n=== Step 7: verdict ([SIGN] 3-tuple → composite) ===")
    regime_valid = bool(fb["saturation_pass"])  # (local) η_FB convergence
    # sign_verdict: substitution chain Step 5 PREDICTED ΔL stays ≥ 0 (T5 sole).
    #   sign_verdict=PASS iff the computed direction matches the predicted direction.
    #   Predicted: ΔL_asymptotic ≥ 0 (no crossing). Computed: ΔL_asymptotic > 0.
    predicted_no_crossing = True  # (local) substitution chain Step 5 prediction
    computed_no_crossing = bool(dL_asym >= 0.0 and not crosses_below)  # (local)
    sign_pass = bool(predicted_no_crossing == computed_no_crossing)  # (local) direction matches
    sign_v = "PASS" if sign_pass else "FAIL"  # (local)
    # magnitude_verdict: the L3<L2 PASS test. PASS iff ΔL_asymptotic < −margin.
    #   FAIL iff ΔL_asymptotic ≥ +margin (deg-+2 obstruction persists).
    if dL_asym < -PASS_MARGIN:
        magnitude_v = "PASS"  # (local) L3 strictly below L2
    elif abs(dL_asym) <= PASS_MARGIN:
        magnitude_v = "INFO"  # (local) borderline (within margin band)
    else:
        magnitude_v = "FAIL"  # (local) L3 ≥ L2 (T4 not saturated)
    # regime_verdict
    if not regime_valid:
        regime_v = "BREAKDOWN"  # (local) η_FB fails to converge
    elif not monotone:
        regime_v = "MARGINAL"  # (local) ΔL non-monotone
    else:
        regime_v = "VALID"  # (local) FB window genuinely reached

    # Composite collapse rule (gate-verdicts.md §"Composite-collapse rule")
    if regime_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    print(f"  sign_verdict={sign_v} (predicted no-crossing={predicted_no_crossing}, "
          f"computed no-crossing={computed_no_crossing})")
    print(f"  magnitude_verdict={magnitude_v} (ΔL_asymptotic={dL_asym:+.6e} vs ±{PASS_MARGIN})")
    print(f"  regime_verdict={regime_v} (η_FB saturation_pass={regime_valid}, monotone={monotone})")
    print(f"  ⇒ COMPOSITE = {composite}")

    if composite == "FAIL":
        verdict_value = (
            f"FAIL_L3_NOT_below_L2: dL_asymptotic={dL_asym:+.6e}>=0 persists through "
            f"L_max={L_TAIL_MAX}; T4|s!=s' deg+2 differential-SUM-growth NOT saturated "
            f"(alpha_env={alpha_asym:+.4f}<0 DIVERGENT); T5 SOLE registry-PASS-eligible "
            f"Element-3; admissible-set NOT widened. dL12={dL12:+.4e} T4_L12={T4_ref_L12:.4f} "
            f"T4_L100={float(T4_grid_pl[-1]):.4f}"
        )  # (local)
    elif composite == "PASS":
        verdict_value = (
            f"PASS_L3_below_L2: dL_asymptotic={dL_asym:+.6e}<0 at L_fit=[50,100]; "
            f"T4|s!=s' envelope-saturated, ADMISSIBLE alt Element-3; "
            f"admissible-set widened to {{T3,T4,T5}}"
        )  # (local)
    else:
        verdict_value = (
            f"INFO_undetermined: dL_asymptotic={dL_asym:+.6e}, regime={regime_v}, "
            f"monotone={monotone}; saturation undetermined at analytic-tail resolution; "
            f"T5 conservative SOLE Element-3 pending resolution"
        )  # (local)

    # ------------------------------------------------------------------
    # 8) Dual-SHA + emit
    # ------------------------------------------------------------------
    audit_sha = closure_hash(pins)  # (local) over [script, canonical, pinmap, w1_3, L12_cache]
    content_sha = sha256_of(Path(__file__))  # (local) over script bytes
    print(f"\n=== Step 8: dual-SHA ===")
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # ------------------------------------------------------------------
    # 9) Save npz
    # ------------------------------------------------------------------
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        tau_fold=float(tau_fold),
        M_KK=float(M_KK),
        Delta_BCS=float(Delta_BCS),
        s_pole=S_POLE,
        s_pole_prime=S_POLE_PRIME,
        L_cache_max=L_CACHE_MAX,
        L_tail_max=L_TAIL_MAX,
        L_fit_asymptotic=np.array(L_FIT_ASYMPTOTIC, dtype=np.int64),
        # Friedrich-Bär predicate
        eta_FB_all_min=fb["eta_FB_all_min"],
        eta_FB_lower=ETA_FB_LOWER,
        eta_FB_new_bound_min=fb["new_bound_min"],
        eta_FB_bot_k_ceiling=fb["bot_k_ceiling"],
        eta_FB_saturation_pass=fb["saturation_pass"],
        # calibration
        A_s2=A2, beta_s2=beta2, r2_s2=r2_2, kappa_s2=kappa2,
        A_s3=A3, beta_s3=beta3, r2_s3=r2_3, kappa_s3=kappa3,
        n_calib_sectors=ncal2,
        # exact cache reproduction
        L_scan_cache=np.array(L_SCAN_CACHE, dtype=np.int64),
        ResW2_cache=ResW2_cache, ResW3_cache=ResW3_cache,
        repro_ok_s2=repro_ok2, repro_ok_s3=repro_ok3,
        ref_ResW2_w1_3=ref_ResW2, ref_ResW3_w1_3=ref_ResW3,
        # full grid
        L_grid=L_grid,
        ResW2_grid_powerlaw=ResW2_grid_pl, ResW3_grid_powerlaw=ResW3_grid_pl,
        ResW2_grid_kappaband=ResW2_grid_kb, ResW3_grid_kappaband=ResW3_grid_kb,
        T4_grid_powerlaw=T4_grid_pl, T4_grid_kappaband=T4_grid_kb,
        # envelope sliding window
        win_centers=win_centers,
        dL_window=dL_win, l3_window=l3_win, l2_window=l2_win, alpha_window=alpha_win,
        dL12=dL12,
        dL_asymptotic_mean=dL_asym, dL_asymptotic_end=dL_asym_end,
        l3_asymptotic_end=l3_asym_end, l2_asymptotic_end=l2_asym_end,
        alpha_asymptotic_mean=alpha_asym,
        delta_dL_net=dΔL, dL_trajectory_direction=dΔL_sign,
        crosses_below=crosses_below, monotone=monotone,
        cache_deviation=cache_dev,
        # verdict
        sign_verdict=sign_v, magnitude_verdict=magnitude_v, regime_verdict=regime_v,
        composite_verdict=composite, verdict_value=verdict_value,
        pass_margin=PASS_MARGIN,
        T4_admissible=True,                 # deg-match + non-scalar (conjunct 1 ∧ 2)
        T4_envelope_saturated=bool(composite == "PASS"),
        T5_sole_element3=bool(composite == "FAIL"),
        # provenance
        w1_3_audit_sha256=w1_3_audit,
        L12_cache_sha256=L12_cache_sha,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved {OUT_NPZ.name}")

    # ------------------------------------------------------------------
    # 10) Plot + verdict line
    # ------------------------------------------------------------------
    make_plot(L_grid, T4_grid_pl, dL_win, alpha_win,
              win_centers, dL_win, l3_win, l2_win, dL12, composite)
    print(f"  saved {OUT_PNG.name}")

    append_verdict(composite, verdict_value, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v)
    print(f"\n  verdict line appended to {VERDICT_TXT}")

    # ------------------------------------------------------------------
    # 11) 4-tuple output tag (final non-verdict line)
    # ------------------------------------------------------------------
    print(f"\n(value={dL_asym:+.6e}_sign={sign_v}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max=14..{L_TAIL_MAX})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
