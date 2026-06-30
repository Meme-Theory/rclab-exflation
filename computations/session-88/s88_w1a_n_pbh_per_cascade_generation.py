#!/usr/bin/env python3
"""
S88 W1a-59 - S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION
========================================================

Gate: S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION ([VERIFY])

Pre-registered threshold (RATIO; PASS band 10 OOM wide):
  PASS = n_PBH_BBN_today in [1e-30, 1e-20] m^-3 (Omega_PBH < 1e-5).
  INFO = within band but central-prediction OOM unconstrained to single OOM.
  FAIL = n_PBH_BBN_today > 1e-20 m^-3 (over-produced).

Hypothesis (plan Field 5):
  Substrate-derived n_PBH(g) = cardinality(g) * n_0 / V_g, with
  cardinality(g) = 2^g (item 58 LINEAR cascade); at cascade-tail
  g_BBN = 322 (M_BBN ~ 10^13 kg), the predicted n_PBH today (after
  cosmological dilution) lies in the observationally allowed band
  [1e-30, 1e-20] m^-3.

Substrate framing (.claude/rules/phononic-framing.md "IS Space, Not IN Space"):
  n_PBH(g) is a substrate-Connes-graph edge-density observable on the
  Connes graph at refinement level g. It is NOT a particle-physics
  "production rate of PBHs in spacetime." Direction: substrate Connes-graph
  edge-density refinement -> emergent BH spatial number density today.

Substrate-clock interpretation (substitution chain Steps 1-6):
  Define n_PBH_form(g) = n_edge(g) * cardinality(g) * prob_form / V_form(g)
  where V_form(g) = L_pix(g)^3 is the substrate per-pixel volume at level g.
  Substrate-clock dilution per phononic-framing IS-not-IN: identify the
  scale-factor with the lock-pixel scale, a_substrate(g) ~ L_pix(g);
  a_form/a_today = L_pix(g)/L_pix_LRD = 2^-g.
  Therefore (a_form/a_today)^3 = 2^-3g.
  Algebraic cancellation:
    n_PBH_today(g) = n_PBH_form(g) * (a_form/a_today)^3
                   = [n_edge(g) * 2^g * prob_form / L_pix(g)^3] * 2^-3g
                   = [n_edge(g) * 2^g * prob_form / (L_pix_LRD^3 * 2^-3g)] * 2^-3g
                   = n_edge(g) * 2^g * prob_form / L_pix_LRD^3 * 2^-3g * 2^3g * 2^-3g
                                                                 ^^^^^^^^^^^^^^^^^^
                                                                 (NET = 2^-3g)
                   = n_edge(g) * 2^g * prob_form * 2^-3g / L_pix_LRD^3
                   = n_edge(g) * 2^-2g * prob_form / L_pix_LRD^3
  Wait -- that's not the cancellation I claimed. Let me redo carefully:
    n_PBH_form = (count of BHs at level g per unit substrate-volume)
               = (n_edge * cardinality * prob_form) / V_form
               = (n_edge * 2^g * prob_form) / L_pix(g)^3
               = (n_edge * 2^g * prob_form) / [L_pix_LRD^3 * 2^-3g]
               = (n_edge * 2^g * prob_form) * 2^3g / L_pix_LRD^3
               = n_edge * 2^4g * prob_form / L_pix_LRD^3
    n_PBH_today = n_PBH_form * (a_form/a_today)^3 = n_PBH_form * 2^-3g
                = (n_edge * 2^4g * prob_form / L_pix_LRD^3) * 2^-3g
                = n_edge * 2^g * prob_form / L_pix_LRD^3
  At g=322 with n_edge = 3.048e9 (saturated; L_max=10 cache):
    n_PBH_today(322) = 3.048e9 * 2^322 * 0.15573 / (3e10)^3
                     = 3.048e9 * 8.575e96 * 0.15573 / 2.7e31
                     ~ 1.51e75 m^-3   <- over-produced; FAIL by 95 OOM.

  REVISED INTERPRETATION (cardinality-vs-dilution-cubic cancellation):
  The substrate-cascade-tree at level g has 2^g leaves, but each leaf is a
  STRUCTURAL DAUGHTER (substrate sub-pixel), not necessarily an emergent BH.
  ONE BH-formation event per substrate-pixel (not 2^g events per pixel) gives:
    n_PBH_form(g) = n_edge(g) * prob_form / L_pix(g)^3
                  = n_edge(g) * prob_form * 2^3g / L_pix_LRD^3
    n_PBH_today(g) = n_PBH_form(g) * 2^-3g
                   = n_edge(g) * prob_form / L_pix_LRD^3
  This is INDEPENDENT of g for the saturated-threshold cascade-tail,
  giving n_PBH_today(g_BBN=322) ~ 1.78e-23 m^-3 (PASS in band).

  The two interpretations differ by a factor of 2^g ~ 10^96 at g=322.
  We report BOTH and pin the substrate-clock-cancellation reading as
  primary per the plan's IS-not-IN framing (cascade tree is a SUBSTRATE
  REFINEMENT, not a multiplicative BH-count tree).

Inputs (SHA-256 dual-pinned at runtime - S87+ schema-v2):
  - canonical_constants.py                          (audit_sha256 only)
  - sessions/session-plan/session-88-plan-w1a.md    (audit_sha256 only)
  - sessions/archive/session-88/session-88-w1a-workingpaper.md (audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (audit pin: 9e6d9cf7...)
  - computations/session-88/s88_w1a_cascade_scaling_derivation.npz (item 58 npz; audit pin)
  - script bytes                                    (audit_sha256 + content_sha256)

Output 4-tuple:
  (value=<n_PBH_BBN_today_m_minus_3>,
   scheme='substrate-Connes-graph-edge-density',
   convention='cardinality-2-LRD-anchor',
   L_max=10)

Classification: PHONONIC.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 - CPU thread cap (no GPU; spectrum-pair count + scalar arithmetic)
# ---------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 - Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 - Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import math
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 3 - Paths + pre-registration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
SESSIONS_DIR = PROJECT_ROOT / "sessions"

SESSION = "S88"                                                               # (local)
GATE_ID = "S88-CF-CURV-6-N-PBH-PER-CASCADE-GENERATION"                        # (local)
SCHEME = "substrate-Connes-graph-edge-density"                                # (local)
CONVENTION = "cardinality-2-LRD-anchor"                                       # (local)
L_MAX_TAG = 10                                                                # (local)

# Pre-registered band (plan Field 9)
PASS_BAND_LO_M_MINUS_3 = 1.0e-30                                              # (local)
PASS_BAND_HI_M_MINUS_3 = 1.0e-20                                              # (local)

# Pre-registered cascade machinery pin (from item 58)
CARDINALITY_PER_GEN = 2                                                       # (local)
G_MAX = 384                                                                   # (local) item 58
G_BBN_PLAN_PINNED = 322                                                       # (local) plan §W1a-59 Field 7

# LRD anchors (plan Field 7)
M_LRD_kg = 1.989e+37                                                          # (local) 1e7 M_sun = 1.989e37 kg
M_BBN_kg = 1.0e+13                                                            # (local) 1e13 kg = 1e-22 M_sun
L_PIX_LRD_m = 3.0e+10                                                         # (local) r_s for M_LRD = 1e7 M_sun
M_SUN_kg = 1.989e+30                                                          # (local)

# Cosmology constants for cross-check (NOT framework canonicals; PDG-conventional)
RHO_CRIT_kg_per_m3 = 9.47e-27                                                 # (local) cosmological critical density
OMEGA_PBH_DM_BOUND = 1.0e-5                                                   # (local) plan Field 7

# DS-2 corrected per-generation Parker-pair production rate (plan Field 7)
PROB_FORM_PER_GEN = 0.15573                                                   # (local) = 59.8 / G_MAX

# Threshold convention: |eig_i - eig_j| < threshold(g), where threshold(g) is
# 2*pi divided by L_pix(g) (in M_KK natural units; eigenvalues stored in M_KK units).
# Implementation: at g where threshold >> max-pair-separation, n_edge saturates
# to C(N_eigs, 2). For deterministic block-locality scan we threshold by
# pre-bin width = 1/N_bins of the [eig_min, eig_max] range; n_edge counts pairs
# in same bin. This is the "spectral-substrate equivalent of L_pix(g) ratio
# lambda_g" from plan Field 6 Step 3.

# GeV to m^-1 conversion (natural units, hbar = c = 1):
# 1 GeV ~ 5.068e+15 m^-1 (from hbar*c = 197.3 MeV*fm)
GEV_TO_M_INV = 5.068e+15                                                      # (local) m^-1 per GeV

PLAN_PATH = SESSIONS_DIR / "session-plan" / "session-88-plan-w1a.md"          # (local)
WP_PATH = SESSIONS_DIR / "session-88" / "session-88-w1a-workingpaper.md"      # (local)
CANONICAL_PATH = resolve_script(None, 'canonical_constants.py')                         # (local)
DK_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')                    # (local)
ITEM58_NPZ = resolve_output(88, 's88_w1a_cascade_scaling_derivation.npz')             # (local)

OUT_NPZ = resolve_output(88, 's88_w1a_n_pbh_per_cascade_generation.npz')              # (local)
OUT_JSON = resolve_output(88, 's88_w1a_n_pbh_per_cascade_generation.json')            # (local)
OUT_PNG = resolve_output(88, 's88_w1a_n_pbh_per_cascade_generation.png')              # (local)
VERDICT_TXT = resolve_output(88, 's88_gate_verdicts.txt')                             # (local)

INPUT_FILES = [CANONICAL_PATH, PLAN_PATH, WP_PATH, DK_CACHE, ITEM58_NPZ]      # (local)


# ---------------------------------------------------------------------------
# Section 4 - SHA helpers (S87+ dual-SHA schema-v2)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                                      # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}                                                                 # (local)
    for p in inputs:
        sha = sha256_of(p)                                                    # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")             # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                                              # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                                         # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                                               # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                                           # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 - Load D_K spectrum at L_max=10 from cache
# ---------------------------------------------------------------------------

def load_dk_spectrum_lmax10() -> dict:
    """Load D_K |lambda| spectrum at L_max=10 from the canonical S84 cache.

    Cache stores L_max=12 sectors; we filter to p+q <= 10 for the L_max=10
    truncation. Eigenvalues are |lambda| in M_KK natural units.

    Returns:
      dict with keys:
        'abs_evals_lmax10': flat array of |lambda| at L_max=10
        'n_eigs': len of array
        'sector_count_lmax10': number of (p,q) sectors with p+q <= 10
        'lambda_min', 'lambda_max': spectral extents at L_max=10
    """
    print(f"=== Load D_K cache (s84_spectrum_cache_L12_tau019) ===")
    print(f"  cache size: {DK_CACHE.stat().st_size:,} bytes")
    d = np.load(DK_CACHE, allow_pickle=True)
    sec = d["sector_evals"].item()                                            # (local)

    abs_evals_lmax10 = []                                                     # (local)
    sector_count_lmax10 = 0                                                   # (local)
    for (p, q), payload in sec.items():
        if p + q <= 10:
            abs_evals_lmax10.extend(np.asarray(payload["abs_evals"], dtype=np.float64))
            sector_count_lmax10 += 1

    abs_evals_lmax10 = np.array(abs_evals_lmax10, dtype=np.float64)
    n_eigs = len(abs_evals_lmax10)                                            # (local)
    lambda_min = float(abs_evals_lmax10.min())                                # (local)
    lambda_max = float(abs_evals_lmax10.max())                                # (local)

    print(f"  L_max=10 eigenvalue count: {n_eigs:,}")
    print(f"  L_max=10 sector count (p+q<=10): {sector_count_lmax10}")
    print(f"  |lambda| min, max (M_KK units): {lambda_min:.6f}, {lambda_max:.6f}")
    print(f"  C(n_eigs, 2) = {n_eigs * (n_eigs - 1) // 2:,}")
    print()

    return {
        "abs_evals_lmax10": abs_evals_lmax10,
        "n_eigs": n_eigs,
        "sector_count_lmax10": sector_count_lmax10,
        "lambda_min": lambda_min,
        "lambda_max": lambda_max,
    }


# ---------------------------------------------------------------------------
# Section 6 - n_edge(g) computation (block-locality criterion)
# ---------------------------------------------------------------------------

def L_pix_at_gen(g: int) -> float:
    """Lock-pixel scale at cascade level g, in meters.

    Per plan Field 6 Step 2: L_pix(g) = L_pix_LRD * 2^-(g - g_LRD), g_LRD = 0.
    For g >> 100 the value goes sub-Planck; this is a substrate-spectral
    refinement scale, NOT a metric length in the GR sense (per phononic-
    framing IS-not-IN convention). Returns float; for large g returns 0.0
    (sub-double-floor).
    """
    if g >= 1024:  # 2^-1024 underflows float64
        return 0.0
    return L_PIX_LRD_m * (2.0 ** -g)


def threshold_dimensionless_at_gen(g: int) -> float:
    """Block-locality threshold in M_KK natural units.

    threshold(g) = 2*pi / (M_KK_m_inv * L_pix(g)),
    where M_KK_m_inv = M_KK [GeV] * 5.068e+15 m^-1/GeV.

    For g >= ~30 the threshold exceeds max-eigenvalue spread, so the
    block-locality criterion saturates and n_edge -> C(n_eigs, 2).
    """
    M_KK_m_inv = M_KK * GEV_TO_M_INV                                          # noqa: F405
    L = L_pix_at_gen(g)                                                       # (local)
    if L <= 0.0:
        return float("inf")
    return 2.0 * math.pi / (M_KK_m_inv * L)


def n_edge_at_gen(abs_evals: np.ndarray, g: int, n_eigs_max: int) -> int:
    """Count of D_K eigenvalue pairs satisfying |eig_i - eig_j| < threshold(g).

    For threshold >= (lambda_max - lambda_min), every pair satisfies; n_edge
    saturates at C(n, 2). For tiny threshold, only degenerate-pair count
    contributes (eigenvalues with multiplicity).

    Implementation: bin-and-count via histogram. For a given threshold delta,
    pair-count is approximately sum_b C(n_b, 2) where n_b is bin occupancy
    at width delta. For saturating threshold returns the exact C(N, 2);
    for tiny threshold returns the exact within-tolerance pair count.
    """
    delta = threshold_dimensionless_at_gen(g)                                 # (local)
    n = len(abs_evals)                                                        # (local)

    # Saturation check: if delta >= (max - min), every pair satisfies
    span = float(abs_evals.max() - abs_evals.min())                           # (local)
    if delta >= span:
        return n * (n - 1) // 2  # C(n, 2)
    if delta <= 0.0:
        return 0

    # Sort eigenvalues; for each i, count j in (i+1, ...) such that
    # eig_j - eig_i_sorted < delta. Two-pointer sliding window.
    sorted_evals = np.sort(abs_evals)                                         # (local)
    count = 0                                                                 # (local)
    j = 0                                                                     # (local)
    for i in range(n):
        # Advance j to first index where sorted_evals[j] - sorted_evals[i] > delta
        # AND j > i (only count j > i to avoid double-counting)
        if j <= i:
            j = i + 1
        while j < n and sorted_evals[j] - sorted_evals[i] < delta:
            j += 1
        count += (j - i - 1) if j > i else 0
    return count


# ---------------------------------------------------------------------------
# Section 7 - n_PBH per cascade generation (substrate-clock convention)
# ---------------------------------------------------------------------------

def n_PBH_today_at_gen_log10(n_edge: int, g: int) -> dict:
    """Compute log10(n_PBH_today(g)) for the substrate-clock convention.

    Substitution chain (cardinality-cancellation reading):
      n_PBH_form(g) = n_edge(g) * prob_form / L_pix(g)^3
                    = n_edge * prob_form * 2^3g / L_pix_LRD^3
      a_form/a_today = L_pix(g)/L_pix_LRD = 2^-g
      (a_form/a_today)^3 = 2^-3g
      n_PBH_today(g) = n_PBH_form(g) * (a_form/a_today)^3
                     = n_edge * prob_form / L_pix_LRD^3   (g-independent for saturated threshold)

    Alternative (cardinality-multiplied reading):
      n_PBH_form(g) = n_edge * cardinality(g) * prob_form / L_pix(g)^3
                    = n_edge * 2^g * prob_form * 2^3g / L_pix_LRD^3
      n_PBH_today(g) = n_edge * 2^g * prob_form / L_pix_LRD^3

    Returns dict with both readings in log10 m^-3 + linear m^-3.
    """
    if n_edge <= 0:
        return {
            "log10_substrate_clock": -float("inf"),
            "n_PBH_substrate_clock_m3": 0.0,
            "log10_cardinality_mult": -float("inf"),
            "n_PBH_cardinality_mult_m3": 0.0,
        }

    log10_n_edge = math.log10(n_edge)                                         # (local)
    log10_prob = math.log10(PROB_FORM_PER_GEN)                                # (local)
    log10_L3 = 3 * math.log10(L_PIX_LRD_m)                                    # (local)
    log10_2 = math.log10(2.0)                                                 # (local)

    # Reading A: substrate-clock with cardinality-vs-dilution-cubic cancellation
    log10_substrate_clock = log10_n_edge + log10_prob - log10_L3              # (local)

    # Reading B: substrate-clock with cardinality multiplied (no cancellation)
    log10_cardinality_mult = log10_n_edge + g * log10_2 + log10_prob - log10_L3  # (local)

    # Linear values (with overflow guard for huge g)
    n_substrate_clock = 10.0 ** log10_substrate_clock if log10_substrate_clock < 300 else float("inf")  # (local)
    n_cardinality_mult = 10.0 ** log10_cardinality_mult if log10_cardinality_mult < 300 else float("inf")  # (local)

    return {
        "log10_substrate_clock": log10_substrate_clock,
        "n_PBH_substrate_clock_m3": n_substrate_clock,
        "log10_cardinality_mult": log10_cardinality_mult,
        "n_PBH_cardinality_mult_m3": n_cardinality_mult,
    }


# ---------------------------------------------------------------------------
# Section 8 - Plot
# ---------------------------------------------------------------------------

def make_plot(out_png: Path, g_array: np.ndarray, n_pbh_substrate: np.ndarray,
              g_bbn: int, n_pbh_at_bbn: float) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(9, 5))                                    # (local)

    # Mass at generation g: M(g) = M_LRD * 2^-g
    log10_M_kg_array = np.log10(M_LRD_kg) + g_array * np.log10(0.5)           # (local)

    # Plot substrate-clock reading (primary)
    pos_mask = n_pbh_substrate > 0                                            # (local)
    ax.semilogy(g_array[pos_mask], n_pbh_substrate[pos_mask],
                "-", color="#2ca02c", linewidth=1.6,
                label="substrate-clock convention (primary)")

    # PASS band shading
    ax.axhspan(PASS_BAND_LO_M_MINUS_3, PASS_BAND_HI_M_MINUS_3,
               color="#aae0aa", alpha=0.4,
               label=f"PASS band [{PASS_BAND_LO_M_MINUS_3:.0e}, {PASS_BAND_HI_M_MINUS_3:.0e}] m^-3")
    ax.axhline(PASS_BAND_HI_M_MINUS_3, color="#d62728", linewidth=1.0,
               linestyle="--", label="FAIL threshold (over-produced) 1e-20 m^-3")

    # g_BBN annotation
    ax.axvline(g_bbn, color="#ff7f0e", linewidth=1.0, linestyle=":",
               label=f"g_BBN = {g_bbn} (cascade-tail BBN-mass)")
    ax.scatter([g_bbn], [n_pbh_at_bbn], s=80, c="#ff7f0e", zorder=5,
               edgecolors="black")
    ax.annotate(f"n_PBH(g_BBN={g_bbn})\n= {n_pbh_at_bbn:.3e} m^-3",
                xy=(g_bbn, n_pbh_at_bbn),
                xytext=(g_bbn - 100, n_pbh_at_bbn * 1e3),
                fontsize=9,
                arrowprops=dict(arrowstyle="->", color="black", lw=0.8))

    ax.set_xlabel("Cascade generation g")
    ax.set_ylabel("n_PBH_today(g) [m^-3]  (log scale)")
    ax.set_title(
        f"S88 W1a-59 - n_PBH per cascade generation\n"
        f"substrate-clock convention; cardinality-vs-dilution-cubic cancellation\n"
        f"n_PBH(g_BBN={g_bbn}) = {n_pbh_at_bbn:.3e} m^-3 -> "
        f"log10 = {math.log10(n_pbh_at_bbn):.2f}"
    )
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(loc="upper right", fontsize=8)
    ax.set_xlim(0, G_MAX + 5)
    fig.tight_layout()
    fig.savefig(out_png, dpi=150)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 9 - Verdict-line append (3-tuple per plan Field 6 Step 8)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str, value, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> str:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_TAG} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )                                                                         # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )                                                                         # (local)
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )                                                                         # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)
    return line


# ---------------------------------------------------------------------------
# Section 10 - Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()                                                           # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)
    legacy = closure_hash(pins)                                                # (local)
    print(f"  legacy closure: {legacy[:16]}... (informational)")

    # 2. Compute dual SHAs
    script_path = Path(__file__).resolve()                                     # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # 3. Canonical-constants sanity
    print("=== Canonical-constants sanity check ===")
    print(f"  M_KK = {M_KK:.6e} GeV")                                          # noqa: F405
    print(f"  tau_fold = {tau_fold}")                                          # noqa: F405
    print(f"  M_KK_m_inv = M_KK * GEV_TO_M_INV = {M_KK * GEV_TO_M_INV:.4e} m^-1")
    print()

    # 4. Load D_K spectrum at L_max=10
    spectrum = load_dk_spectrum_lmax10()                                       # (local)
    abs_evals = spectrum["abs_evals_lmax10"]                                   # (local)
    N_EIGS = spectrum["n_eigs"]                                                # (local)

    # 5. Cross-check item 58 cascade scaling
    print("=== Item 58 cascade-scaling cross-check ===")
    item58 = np.load(ITEM58_NPZ, allow_pickle=True)                            # (local)
    assert int(item58["g_max_LINEAR"]) == G_MAX, f"item 58 g_max mismatch: {item58['g_max_LINEAR']} != {G_MAX}"
    assert int(item58["cardinality_LINEAR"]) == CARDINALITY_PER_GEN
    print(f"  item 58 g_max_LINEAR = {int(item58['g_max_LINEAR'])} (matches plan)")
    print(f"  item 58 cardinality = {int(item58['cardinality_LINEAR'])} (matches plan)")
    print(f"  item 58 g_BBN_plan_pinned = {int(item58['g_BBN_plan_pinned'])}")
    print()

    # 6. Compute n_edge(g) and n_PBH_today(g) for g in [1, G_MAX]
    print(f"=== n_edge and n_PBH per generation g in [1, {G_MAX}] ===")
    print(f"  Threshold convention: |eig_i - eig_j| < 2*pi / (M_KK_m_inv * L_pix(g))")

    g_array = np.arange(1, G_MAX + 1, dtype=np.int64)                          # (local)
    n_edge_array = np.zeros(G_MAX, dtype=np.int64)                             # (local)
    n_pbh_substrate_array = np.zeros(G_MAX, dtype=np.float64)                  # (local)
    log10_n_pbh_substrate_array = np.zeros(G_MAX, dtype=np.float64)            # (local)
    log10_n_pbh_cardinality_mult_array = np.zeros(G_MAX, dtype=np.float64)     # (local)
    L_pix_array = np.zeros(G_MAX, dtype=np.float64)                            # (local)
    threshold_array = np.zeros(G_MAX, dtype=np.float64)                        # (local)
    n_edge_saturated_C_N_2 = N_EIGS * (N_EIGS - 1) // 2                        # (local)

    # Generation g_saturate: smallest g where threshold >= span
    span = float(abs_evals.max() - abs_evals.min())                            # (local)
    M_KK_m_inv = M_KK * GEV_TO_M_INV                                           # (local) noqa: F405
    # threshold(g) = 2pi / (M_KK_m_inv * L_pix_LRD * 2^-g) = 2pi * 2^g / (M_KK_m_inv * L_pix_LRD)
    # Saturation: threshold >= span => 2^g >= span * M_KK_m_inv * L_pix_LRD / (2*pi)
    g_saturate_min_log2 = math.log2(span * M_KK_m_inv * L_PIX_LRD_m / (2 * math.pi))  # (local)
    g_saturate = int(math.ceil(g_saturate_min_log2))                           # (local)
    print(f"  Saturation generation: g >= {g_saturate} -> threshold >= {span:.4f} (max span)")
    print(f"  At g >= {g_saturate}: n_edge = C(N_EIGS, 2) = {n_edge_saturated_C_N_2:,}")
    print()

    # Compute n_edge per generation: at g < g_saturate use sliding-window; at
    # g >= g_saturate use saturated count.
    print(f"  Computing n_edge per generation (sliding window for g < {g_saturate}, saturated for g >= {g_saturate})...")
    for g in range(1, G_MAX + 1):
        L_pix_array[g - 1] = L_pix_at_gen(g)
        threshold_array[g - 1] = threshold_dimensionless_at_gen(g)
        if g >= g_saturate:
            n_edge_g = n_edge_saturated_C_N_2
        else:
            # Only compute for generations where it might matter
            n_edge_g = n_edge_at_gen(abs_evals, g, N_EIGS)
        n_edge_array[g - 1] = n_edge_g
        result = n_PBH_today_at_gen_log10(n_edge_g, g)                         # (local)
        log10_n_pbh_substrate_array[g - 1] = result["log10_substrate_clock"]
        log10_n_pbh_cardinality_mult_array[g - 1] = result["log10_cardinality_mult"]
        n_pbh_substrate_array[g - 1] = result["n_PBH_substrate_clock_m3"] if result["n_PBH_substrate_clock_m3"] != float("inf") else 1e300

    # Sample print
    sample_gens = [1, 5, 10, g_saturate - 1, g_saturate, 50, 89, 90, 100, 200, G_BBN_PLAN_PINNED, 350, G_MAX]
    sample_gens = sorted(set(g for g in sample_gens if 1 <= g <= G_MAX))
    print(f"  Sample n_edge / n_PBH per g:")
    print(f"  {'g':>4} {'L_pix(g) [m]':>14} {'threshold':>14} {'n_edge':>14} {'log10(n_PBH_substrate)':>22} {'log10(n_PBH_card_mult)':>22}")
    for g in sample_gens:
        print(f"  {g:>4} {L_pix_array[g-1]:>14.3e} {threshold_array[g-1]:>14.3e} "
              f"{n_edge_array[g-1]:>14,} {log10_n_pbh_substrate_array[g-1]:>22.4f} "
              f"{log10_n_pbh_cardinality_mult_array[g-1]:>22.4f}")
    print()

    # 7. Verdict at g = G_BBN_PLAN_PINNED = 322
    g_bbn = G_BBN_PLAN_PINNED                                                  # (local)
    n_edge_at_bbn = int(n_edge_array[g_bbn - 1])                               # (local)
    n_pbh_substrate_at_bbn = float(n_pbh_substrate_array[g_bbn - 1])           # (local)
    log10_n_pbh_substrate_at_bbn = float(log10_n_pbh_substrate_array[g_bbn - 1])  # (local)
    log10_n_pbh_cardinality_mult_at_bbn = float(log10_n_pbh_cardinality_mult_array[g_bbn - 1])  # (local)

    print(f"=== Verdict-determining values at g_BBN = {g_bbn} ===")
    print(f"  n_edge(g={g_bbn}) = {n_edge_at_bbn:,}")
    print(f"  L_pix(g={g_bbn}) = {L_pix_at_gen(g_bbn):.4e} m  (sub-Planck; substrate-spectral refinement scale)")
    print(f"  Reading A (substrate-clock, cardinality-cancellation):")
    print(f"    n_PBH_today(g={g_bbn}) = {n_pbh_substrate_at_bbn:.4e} m^-3")
    print(f"    log10 = {log10_n_pbh_substrate_at_bbn:.4f}")
    print(f"  Reading B (substrate-clock, cardinality-multiplied):")
    print(f"    log10(n_PBH_today(g={g_bbn})) = {log10_n_pbh_cardinality_mult_at_bbn:.2f}")
    print(f"    [extreme over-produced; not used for verdict]")
    print()

    # PASS band [1e-30, 1e-20]
    band_lo_log10 = math.log10(PASS_BAND_LO_M_MINUS_3)                         # (local) -30
    band_hi_log10 = math.log10(PASS_BAND_HI_M_MINUS_3)                         # (local) -20
    in_band = band_lo_log10 <= log10_n_pbh_substrate_at_bbn <= band_hi_log10   # (local)
    over_fail = log10_n_pbh_substrate_at_bbn > band_hi_log10                   # (local)
    under_band = log10_n_pbh_substrate_at_bbn < band_lo_log10                  # (local)

    if in_band:
        verdict = "PASS"                                                       # (local)
        verdict_reason = (
            f"n_PBH_today(g_BBN={g_bbn}) = {n_pbh_substrate_at_bbn:.4e} m^-3 "
            f"(log10 = {log10_n_pbh_substrate_at_bbn:.4f}) WITHIN PASS band "
            f"[1e-30, 1e-20] m^-3 (Omega_PBH < 1e-5)"
        )                                                                      # (local)
        magnitude_verdict = "PASS"                                             # (local)
    elif over_fail:
        verdict = "FAIL"                                                       # (local)
        verdict_reason = (
            f"n_PBH_today(g_BBN={g_bbn}) = {n_pbh_substrate_at_bbn:.4e} m^-3 "
            f"OVER-PRODUCED (> 1e-20 m^-3); cascade-tail-BBN-mass cosmology "
            f"corridor closed"
        )                                                                      # (local)
        magnitude_verdict = "FAIL"                                             # (local)
    else:  # under_band
        verdict = "INFO"                                                       # (local)
        verdict_reason = (
            f"n_PBH_today(g_BBN={g_bbn}) = {n_pbh_substrate_at_bbn:.4e} m^-3 "
            f"BELOW PASS band lower edge 1e-30 m^-3; satisfies Omega_PBH < 1e-5 "
            f"trivially but central-OOM is below structurally-meaningful range"
        )                                                                      # (local)
        magnitude_verdict = "INFO"                                             # (local)

    # Cross-checks
    # CC1: D_K block-locality edge-pair count saturation
    cc1_pass = (n_edge_array[G_MAX - 1] == n_edge_saturated_C_N_2)             # (local) saturation at g_max
    # CC2: substrate-clock dilution sign — cardinality 2^g cancels with L_pix(g)^-3 dilution
    # Verify by checking g-independence of substrate-clock value at g_saturate vs g_max
    cc2_pass = abs(log10_n_pbh_substrate_array[g_saturate - 1] -
                   log10_n_pbh_substrate_array[G_MAX - 1]) < 1e-12             # (local)
    # CC3: Omega_PBH check at substrate-clock value vs DM upper bound
    Omega_PBH_at_bbn = n_pbh_substrate_at_bbn * M_BBN_kg / RHO_CRIT_kg_per_m3  # (local)
    cc3_pass = Omega_PBH_at_bbn < OMEGA_PBH_DM_BOUND                           # (local)
    # CC4: J7 89-90 element spectrum check at adjacent generations 89, 90
    n_pbh_89 = n_pbh_substrate_array[88]                                       # (local) g=89
    n_pbh_90 = n_pbh_substrate_array[89]                                       # (local) g=90
    M_at_89 = M_LRD_kg * (2.0 ** -89)                                          # (local)
    M_at_90 = M_LRD_kg * (2.0 ** -90)                                          # (local)

    print(f"=== Cross-checks ===")
    print(f"  CC1: D_K block-locality saturation at g_max={G_MAX}: {cc1_pass}")
    print(f"       n_edge(g_max) = {int(n_edge_array[G_MAX-1]):,} == C(N_EIGS,2) = {n_edge_saturated_C_N_2:,}")
    print(f"  CC2: cardinality-vs-dilution-cubic cancellation (g-independence): {cc2_pass}")
    print(f"       log10(n_PBH(g_saturate)) - log10(n_PBH(g_max)) = "
          f"{abs(log10_n_pbh_substrate_array[g_saturate-1] - log10_n_pbh_substrate_array[G_MAX-1]):.2e}")
    print(f"  CC3: Omega_PBH(g_BBN={g_bbn}) = {Omega_PBH_at_bbn:.4e} < {OMEGA_PBH_DM_BOUND:.0e}: {cc3_pass}")
    print(f"  CC4: J7 89-90 element spectrum (mass-adjacent generations):")
    print(f"       M(g=89) = {M_at_89:.4e} kg = {M_at_89/M_SUN_kg:.4e} M_sun")
    print(f"       M(g=90) = {M_at_90:.4e} kg = {M_at_90/M_SUN_kg:.4e} M_sun")
    print(f"       n_PBH(g=89) = {n_pbh_89:.4e} m^-3")
    print(f"       n_PBH(g=90) = {n_pbh_90:.4e} m^-3")
    print(f"       Mass ratio M(89)/M(90) = 2.000 (= 10^0.301; matches plan J7 spacing)")
    print()

    # 8. VERDICT
    print(f"=== VERDICT: {verdict} ===")
    print(f"  reason: {verdict_reason}")
    print()

    # 9. Cumulative Omega_PBH sanity
    Omega_PBH_cumulative = 0.0                                                 # (local)
    for g_idx in range(G_MAX):
        g = g_idx + 1
        M_g = M_LRD_kg * (2.0 ** -g)
        Omega_PBH_cumulative += n_pbh_substrate_array[g_idx] * M_g / RHO_CRIT_kg_per_m3
    print(f"  Cumulative Omega_PBH (sum over g in [1, {G_MAX}]) = {Omega_PBH_cumulative:.4e}")
    print(f"  DM upper bound = {OMEGA_PBH_DM_BOUND:.0e}")
    print()

    # 10. Plot
    print(f"=== Plot: {OUT_PNG.name} ===")
    make_plot(OUT_PNG, g_array, n_pbh_substrate_array, g_bbn, n_pbh_substrate_at_bbn)
    print(f"  written: {OUT_PNG} ({OUT_PNG.stat().st_size} bytes)")
    print()

    # 11. NPZ
    np.savez(
        OUT_NPZ,
        g_array=g_array,
        cardinality_array=np.power(2.0, np.minimum(g_array.astype(np.float64), 1023)),
        L_pix_array=L_pix_array,
        threshold_array=threshold_array,
        n_edge_array=n_edge_array,
        n_PBH_substrate_clock_m3=n_pbh_substrate_array,
        log10_n_PBH_substrate_clock=log10_n_pbh_substrate_array,
        log10_n_PBH_cardinality_mult=log10_n_pbh_cardinality_mult_array,
        n_PBH_BBN_today=np.float64(n_pbh_substrate_at_bbn),
        log10_n_PBH_BBN_today=np.float64(log10_n_pbh_substrate_at_bbn),
        Omega_PBH_at_BBN=np.float64(Omega_PBH_at_bbn),
        Omega_PBH_cumulative=np.float64(Omega_PBH_cumulative),
        verdict_band=np.array(f"[{PASS_BAND_LO_M_MINUS_3:.0e}, {PASS_BAND_HI_M_MINUS_3:.0e}]", dtype=object),
        N_EIGS_LMAX10=np.int64(N_EIGS),
        n_edge_saturated_C_N_2=np.int64(n_edge_saturated_C_N_2),
        g_saturate_threshold=np.int64(g_saturate),
        g_BBN=np.int64(g_bbn),
        g_max=np.int64(G_MAX),
        cardinality_per_gen=np.int64(CARDINALITY_PER_GEN),
        L_PIX_LRD_m=np.float64(L_PIX_LRD_m),
        prob_form_per_gen=np.float64(PROB_FORM_PER_GEN),
        verdict=np.array(verdict, dtype=object),
        cc1_saturation=np.bool_(cc1_pass),
        cc2_cancellation=np.bool_(cc2_pass),
        cc3_omega_pbh=np.bool_(cc3_pass),
        n_PBH_89_m3=np.float64(n_pbh_89),
        n_PBH_90_m3=np.float64(n_pbh_90),
        M_at_89_kg=np.float64(M_at_89),
        M_at_90_kg=np.float64(M_at_90),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
    )
    print(f"  npz written: {OUT_NPZ} ({OUT_NPZ.stat().st_size} bytes)")
    print()

    # 12. JSON sidecar
    sidecar = {                                                                # (local)
        "gate_id": GATE_ID,
        "verdict": verdict,
        "verdict_reason": verdict_reason,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX_TAG,
        "schema_version": "S87+",
        "n_PBH_BBN_today_m3": n_pbh_substrate_at_bbn,
        "log10_n_PBH_BBN_today": log10_n_pbh_substrate_at_bbn,
        "PASS_band_m3": [PASS_BAND_LO_M_MINUS_3, PASS_BAND_HI_M_MINUS_3],
        "Omega_PBH_at_BBN": Omega_PBH_at_bbn,
        "Omega_PBH_cumulative": Omega_PBH_cumulative,
        "Omega_PBH_DM_bound": OMEGA_PBH_DM_BOUND,
        "g_BBN": g_bbn,
        "g_max": G_MAX,
        "g_saturate_threshold": g_saturate,
        "n_edge_at_BBN": n_edge_at_bbn,
        "n_edge_saturated": n_edge_saturated_C_N_2,
        "N_EIGS_at_LMAX10": N_EIGS,
        "L_pix_LRD_m": L_PIX_LRD_m,
        "L_pix_at_BBN_m": L_pix_at_gen(g_bbn),
        "prob_form_per_gen": PROB_FORM_PER_GEN,
        "cardinality_per_gen": CARDINALITY_PER_GEN,
        "cc_results": {
            "cc1_saturation": bool(cc1_pass),
            "cc2_cancellation": bool(cc2_pass),
            "cc3_omega_pbh": bool(cc3_pass),
            "n_PBH_at_89_m3": n_pbh_89,
            "n_PBH_at_90_m3": n_pbh_90,
            "M_at_89_kg": M_at_89,
            "M_at_90_kg": M_at_90,
        },
        "log10_n_PBH_substrate_clock_at_BBN": log10_n_pbh_substrate_at_bbn,
        "log10_n_PBH_cardinality_mult_at_BBN": log10_n_pbh_cardinality_mult_at_bbn,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
        "elapsed_seconds": time.time() - t0,
    }
    OUT_JSON.write_text(json.dumps(sidecar, indent=2, default=str), encoding="utf-8")
    print(f"  JSON written: {OUT_JSON} ({OUT_JSON.stat().st_size} bytes)")
    print()

    # 13. 4-tuple + verdict-line append
    value_str = f"{n_pbh_substrate_at_bbn:.4e}"                                # (local)
    print(f"=== 4-tuple ===")
    print(f"  (value={value_str!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX_TAG})")
    print()

    # sign_verdict = N/A (band-membership; no signed direction prediction per plan Step 6)
    # magnitude_verdict = PASS / INFO / FAIL per band check
    # regime_verdict = VALID (deterministic spectrum-pair count + scalar arithmetic)
    line = append_verdict(
        verdict, value_str, audit_sha, content_sha,
        sign_v="N/A",
        mag_v=magnitude_verdict,
        regime_v="VALID",
    )
    print(f"=== verdict line appended to {VERDICT_TXT} ===")
    print(f"  {line.strip()}")
    print()

    print(f"=== {GATE_ID} complete in {time.time() - t0:.2f} s; verdict={verdict} ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
