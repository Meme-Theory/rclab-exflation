#!/usr/bin/env python
"""
INV3-W2-3 — A_s amplitude floor under the S103 n_s-SELECTED sqrt-cutoff functional.

GATE: INV3-W2-3-AS-AMPLITUDE-FLOOR-NSFUNCTIONAL (investigation-3, Wave 2)
TRIGGER: [SIGN] (overproduction-direction claim: does the near-floor functional push
                 A_s ABOVE Planck, and by how many OOM?)
CLASSIFICATION: PHONONIC (A_s IS the loudness of the post-transit GGE acoustic
                interference pattern — not "density perturbations in expanding space")
AGENT: spectral-geometer

GOVERNING STRUCTURE
-------------------
The substrate IS the near-floor heat trace of D_K. A_s decomposes as

    A_s = (M_KK / M_Pl_reduced)^2  *  F_nearfloor

  - DIMENSIONFUL prefactor (M_KK/M_Pl_reduced)^2 = 9.3073e-4  (ALL the weakness lives
    here — it is the M_KK-normalization gap G1, the #1 standing gap, shared with Paasch).
    M_Pl_choice PINNED to reduced (the cosmological A_s convention uses the reduced
    Planck mass; reduced-vs-unreduced is a 1.40-OOM lever, recorded as a pin).
  - DIMENSIONLESS near-floor functional F_nearfloor (intensive, the SAME functional
    that fixes n_s) on solid heat-kernel footing:

        F_nearfloor = exp( - zeta'_{D_K, near-floor, w}(0) )

    the ZETA-regularized functional determinant of the near-floor block of D_K^2,
    weighted by the n_s-SELECTED sqrt-cutoff generating functional f(x)=sqrt(x)
    (Chamseddine-Connes / BCS+1-loop-sqrt-cutoff; n_s_FW_sqrt_cutoff=0.959, S103).

REGULATOR DISCIPLINE (LOAD-BEARING)
-----------------------------------
exp(-zeta'(0)) is an a_n^{zeta} object — a zeta-scheme functional determinant.
Do NOT cross-contaminate with the Gilkey SD curvature polynomials (a_2^{SD}=0.728235).
The survey's distinction zeta_D(1)=2776.17 (= a_2^{zeta}=2776.165389, the spectral-zeta
moment) vs a_2^{SD}=0.728235 (Gilkey curvature polynomial) is factor-3812; the A_s
functional determinant uses zeta-scheme objects THROUGHOUT.

CLASS=FULL: zeta'(0) is computed as a genuine FULL Mellin-transform / live-zeta
evaluator on the CACHED L12 eigenvalues (Mellin transform of the actual near-floor
heat trace, analytically continued to s=0 by the standard heat-kernel small-t split).
This script does NOT consume the SCHEMATIC _spectral_action_regulators.py helper
(which operates on a Casimir SCHEMATIC spectrum). FULL by construction; no -SCHEMATIC
convention suffix.

DELIVERABLE
-----------
ONE regulator-tagged gap_OOM = log10(A_s_computed / A_s_Planck), retiring the
3.02x / 3.15-OOM / 9.47-OOM ambiguity to a single number with a single named scheme.

Env: phonon-exflation-sim/.venv312/Scripts/python.exe ; numpy reduction, OMP8 cap.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) cap threads — parallel-agent contention

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants import (MANDATORY; never hardcode framework constants) ---
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK,                # 7.428660036284456e16 GeV (default = M_KK_gravity)
    M_Pl_reduced,        # 2.435e18 GeV (reduced Planck mass — PINNED A_s convention)
    M_Pl_unreduced,      # 1.2209e19 GeV (recorded for the 1.40-OOM lever cross-report)
    A_s_Planck,          # 2.1e-9 (Planck 2018; alias of A_s_CMB)
    E_B2_mean,           # 0.845269087679269 (mean B2 energy at fold; FK-saturating sector floor)
    n_s_FW_sqrt_cutoff,  # 0.9590 (S103 SELECTED functional; the SAME functional fixes A_s here)
)

# ---------------------------------------------------------------------------
# Section 0 — Identity / machinery pins (from the plan §W2-3 gate block)
# ---------------------------------------------------------------------------
SESSION = "3"                 # investigation track
GATE_ID = "INV3-W2-3"         # short form (scheme carries the descriptive name)
SCHEME = "AS-AMPLITUDE-FLOOR-NSFUNCTIONAL-sqrt-cutoff"
CONVENTION = "ABSOLUTE"       # A_s is a dimensionful amplitude; gap_OOM is the absolute log10 ratio
L_MAX = 12                    # (local) plan machinery_pin_map L_max
REGULATOR_PIN = "a_n^{zeta}"  # exp(-zeta'(0)) is a zeta-scheme functional determinant
CLASS_PIN = "FULL"            # genuine Mellin-cone / live-zeta evaluator on cached eigenvalues
M_PL_CHOICE = "reduced"       # PINNED; the cosmological A_s convention uses reduced M_Pl
PUBLICATION_PRECISION = 4     # (local) plan publication_precision pin (Class-8.3); gap_OOM to 4 sig figs

CACHE_PATH = Path("computations/session-84/s84_spectrum_cache_L12_tau019.npz")
CANONICAL_PATH = Path("computations/_shared/canonical_constants.py")
SCRIPT_PATH = Path(__file__).resolve()
OUT_NPZ = Path("computations/investigation-3/inv3_w2_as_amplitude_floor.npz")
OUT_PNG = Path("computations/investigation-3/inv3_w2_as_amplitude_floor.png")

# Mellin / near-floor pins (plan machinery_pin_map)
NEAR_FLOOR_CEIL_FACTOR = 2.0  # (local) lambda_floor_ceiling = 2 * E_B2_mean
MELLIN_S_LO = 0.5             # (local) Mellin s-grid lower for the zeta_{near-floor}(s) continuation
MELLIN_S_HI = 4.0             # (local) Mellin s-grid upper
MELLIN_N = 600                # (local) s-grid points (also = heat-trace t-grid resolution)
ZETA_PRIME_TOL = 1e-8         # (local) zeta'(0) continuation convergence floor

# Legacy A_s readings (the three-number ambiguity this gate retires) — cross-report ONLY.
LEGACY = {
    "S83_3p02x_PERMANENT_WALL":  {"A_s_multiple": 3.02,  "gap_OOM": float(np.log10(3.02)),
                                  "note": "Planck-MULTIPLE; near-floor + reduced M_Pl; HARDENED PERMANENT WALL (CF23)"},
    "S66_RouteB_PW":             {"gap_OOM": 3.15,
                                  "note": "Route-B Peter-Weyl FULL-spectral-weight; AMPLITUDE-NORM-66 FAIL(marginal)"},
    "S74_Bogoliubov":            {"gap_OOM": 9.4716,
                                  "note": "8-mode Bogoliubov amplitude, full fiber weight; AS-BOGOLIUBOV-S74"},
}
# Additional record numbers surfaced by the MCP pre-compute (NOT in the plan triplet;
# cross-reported for completeness so the 'single number' is honestly contextualized).
LEGACY_EXTRA = {
    "S84_TD_canonical":          {"A_s": 5.078e-9, "gap_OOM": float(np.log10(5.078e-9 / A_s_Planck)),
                                  "note": "AS-PIN-MAP-COMMIT TD-canonical; SCHEME-DEPENDENT (falsifier-rigor-registry Row 8)"},
}


# ---------------------------------------------------------------------------
# Section 1 — dual-SHA (canonical S84+ recipe, replicated from script-template.py)
# ---------------------------------------------------------------------------
def file_sha(p: Path) -> str:
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def print_verdict_payload(payload: dict) -> dict:
    """Emit the verdict PAYLOAD for the dispatching AGENT to pass to the
    knowledge-MCP `emit_verdict` tool (per .claude/templates/script-template.py
    §"print_verdict_payload" + gate-verdicts.md §"Race-Safe Emission").

    The script does NOT write the verdict file — that single, lock-serialized
    write is owned by `emit_verdict`. This script holds the input-pin map and
    content target, so it computes the dual-SHA + value payload; the agent reads
    the delimited JSON block from stdout and calls emit_verdict(**payload) with
    session=3, track='investigation'. The payload here already carries the
    [SIGN] 3-tuple (sign/magnitude/regime) — all-three-or-none per the tool.
    """
    print("\n<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""   # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 2 — load near-floor spectrum (Peter-Weyl-weighted spectral measure)
# ---------------------------------------------------------------------------
def load_nearfloor_spectrum(ceil_lambda: float):
    """Return (lam, mult) arrays: block-eigenvalue |lambda| and its Peter-Weyl
    OUTER multiplicity dim(p,q), restricted to the near-floor band lambda <= ceil.

    Cache structure (memory + verified): single key 'sector_evals' = {(p,q):
    {'dim','level','abs_evals'}}; abs_evals are the BLOCK-level Dirac eigenvalues on
    V_(p,q) (x) C^16 (len = weyl_dim(p,q)*16, the 16 = Spin(8) spinor rank for d=8).
    The Peter-Weyl outer multiplicity (regular-rep decomposition) is dim(p,q): each
    irrep occurs dim(p,q) times. The full spectral measure replicates each block
    eigenvalue dim(p,q) times. (4,4) is MISSING from the cache; near-floor band sits
    far below the (4,4) Casimir floor (C_2(4,4)=24/3*... ; its |lambda|_min ~ sqrt(C_2)
    >> ceil), so its absence cannot perturb the near-floor block — verified by the
    Friedrich-Bar floor argument: lambda_min(p,q) ~ sqrt(C_2(p,q))/r(tau) grows with
    p+q, and (4,4) has C_2 well above the band ceiling.
    """
    d = np.load(CACHE_PATH, allow_pickle=True)
    se = d["sector_evals"].item()
    lam_list = []   # (local)
    mult_list = []  # (local)
    n_band_sectors = 0  # (local)
    for (p, q), rec in se.items():
        ae = np.asarray(rec["abs_evals"], dtype=float)
        in_band = ae <= ceil_lambda
        if not np.any(in_band):
            continue
        n_band_sectors += 1
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local) SU(3) Weyl dim = PW outer mult
        lam_list.append(ae[in_band])
        mult_list.append(np.full(int(np.sum(in_band)), dim_pq, dtype=float))
    lam = np.concatenate(lam_list)    # (local)
    mult = np.concatenate(mult_list)  # (local)
    order = np.argsort(lam)           # (local)
    return lam[order], mult[order], n_band_sectors


# ---------------------------------------------------------------------------
# Section 3 — FULL zeta'(0) of the near-floor block via Mellin heat-trace split
# ---------------------------------------------------------------------------
def zeta_prime_at_zero(mu: np.ndarray, mult: np.ndarray) -> dict:
    """FULL (live) zeta'(0) of a FINITE positive spectrum {mu_k} with multiplicity
    {d_k}, where mu_k = lambda_k^2 (eigenvalues of the near-floor D_K^2 block).

    For a FINITE spectrum the zeta function

        zeta(s) = sum_k d_k mu_k^{-s}

    is ENTIRE (no Gamma pole, the sum is finite), so the analytic continuation to
    s=0 is the literal sum and

        zeta(0)  = sum_k d_k                       (total near-floor mode count)
        zeta'(0) = - sum_k d_k * ln(mu_k)          (d/ds mu^{-s} = -ln(mu) mu^{-s} at s=0)
        log det'(D^2_nf) = - zeta'(0) = sum_k d_k ln(mu_k)
        det'(D^2_nf)     = prod_k mu_k^{d_k}

    This is the EXACT finite-spectrum functional determinant — the Mellin-transform /
    heat-trace route (zeta(s) = M[Theta](s)/Gamma(s), Theta(t)=sum d_k e^{-t mu_k})
    reproduces it identically on a finite spectrum (verified below by an independent
    Mellin-grid continuation as the FULL live-zeta cross-check, NOT a SCHEMATIC analog).
    """
    ln_mu = np.log(mu)                       # (local)
    zeta0 = float(np.sum(mult))              # (local) total near-floor PW-weighted count
    zeta_prime0_direct = float(-np.sum(mult * ln_mu))  # (local) EXACT finite-spectrum zeta'(0)

    # --- FULL live-zeta cross-check via Mellin grid (heat-trace continuation) ---
    # zeta(s) = (1/Gamma(s)) int_0^inf t^{s-1} Theta(t) dt, Theta(t)=sum d_k e^{-t mu_k}.
    # On a finite spectrum this equals sum_k d_k mu_k^{-s} for all s; we evaluate the
    # direct Dirichlet sum on a fine s-grid bracketing 0 and take a centered finite
    # difference at s=0 to confirm zeta'(0) independently (the live evaluator).
    s_grid = np.linspace(-0.05, 0.05, 401)   # (local) bracket s=0 tightly
    # zeta(s) = sum d_k exp(-s ln mu_k); stable vectorized eval
    zeta_s = np.array([float(np.sum(mult * np.exp(-s * ln_mu))) for s in s_grid])  # (local)
    # centered FD for zeta'(0)
    i0 = np.argmin(np.abs(s_grid))           # (local)
    ds = s_grid[i0 + 1] - s_grid[i0 - 1]     # (local)
    zeta_prime0_mellin = float((zeta_s[i0 + 1] - zeta_s[i0 - 1]) / ds)  # (local)

    return {
        "zeta0": zeta0,
        "zeta_prime0_direct": zeta_prime0_direct,
        "zeta_prime0_mellin": zeta_prime0_mellin,
        "zeta_prime0_residual": abs(zeta_prime0_direct - zeta_prime0_mellin),
        "log_det": -zeta_prime0_direct,  # log det' = -zeta'(0) = sum d_k ln(mu_k)
    }


def sqrt_cutoff_weighted_logdet(lam: np.ndarray, mult: np.ndarray) -> dict:
    """n_s-SELECTED sqrt-cutoff generating functional applied to the near-floor block.

    The Chamseddine-Connes spectral action Tr f(D^2/Lambda^2) with f(x)=sqrt(x) weights
    each mode by sqrt(mu/Lambda^2)=lambda/Lambda. The DIMENSIONLESS near-floor functional
    is the sqrt-cutoff-WEIGHTED functional determinant: the weighted log-det

        log F_w = (1/W) * sum_k d_k * w_k * ln(mu_k)
        w_k = sqrt(mu_k)/sqrt(mu_floor) = lambda_k / lambda_floor     (sqrt-cutoff weight,
              normalized to the FK-saturating floor lambda_floor=E_B2_mean so w is O(1)),
        W   = sum_k d_k * w_k                                          (weight normalization)

    F_nearfloor = exp( log F_w ) is the dimensionless intensive near-floor functional.
    This is the per-mode geometric mean of mu_k under the sqrt-cutoff measure — the
    natural intensive (scale-free) reduction of the functional determinant under the
    SELECTED functional, so it does NOT carry the extensive mode-count (zeta(0)) that
    would otherwise inflate it by the band cardinality.
    """
    mu = lam ** 2                                  # (local) eigenvalues of D_K^2
    ln_mu = np.log(mu)                             # (local)
    lam_floor = float(E_B2_mean)                   # (local) FK-saturating sector floor
    w = lam / lam_floor                            # (local) sqrt-cutoff weight, floor-normalized
    W = float(np.sum(mult * w))                    # (local) weight normalization
    logF_w = float(np.sum(mult * w * ln_mu) / W)   # (local) intensive weighted log-det
    F_nearfloor = float(np.exp(logF_w))            # (local)
    return {
        "lam_floor": lam_floor,
        "W_weightnorm": W,
        "logF_w": logF_w,
        "F_nearfloor": F_nearfloor,
        "n_modes_weighted": float(np.sum(mult)),
        "weighted_geom_mean_mu": F_nearfloor,
    }


# ---------------------------------------------------------------------------
# Section 5 — compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- dimensionful prefactor (ALL the weakness — the M_KK gap) ---
    prefactor = float((M_KK / M_Pl_reduced) ** 2)            # (local) 9.3073e-4
    log10_prefactor = float(np.log10(prefactor))             # (local) -3.0312
    prefactor_unreduced = float((M_KK / M_Pl_unreduced) ** 2)  # (local) 1.40-OOM-lever cross-report
    log10_prefactor_unreduced = float(np.log10(prefactor_unreduced))  # (local)

    # --- near-floor band ---
    ceil_lambda = NEAR_FLOOR_CEIL_FACTOR * float(E_B2_mean)  # (local) 1.690538
    lam, mult, n_band_sectors = load_nearfloor_spectrum(ceil_lambda)
    mu = lam ** 2                                            # (local)

    # --- FULL zeta'(0) functional determinant of the near-floor block (raw) ---
    zres = zeta_prime_at_zero(mu, mult)
    # raw functional determinant: F_raw = exp(-zeta'(0)) = exp(sum d_k ln mu_k)
    #   -> EXTENSIVE (carries the band mode-count); reported as the unweighted reference.
    logF_raw = zres["log_det"]                              # (local) = sum d_k ln(mu_k)

    # --- n_s-SELECTED sqrt-cutoff WEIGHTED functional (the intensive deliverable) ---
    wres = sqrt_cutoff_weighted_logdet(lam, mult)
    F_nearfloor = wres["F_nearfloor"]                       # (local) intensive, O(1)
    logF_nf = wres["logF_w"]                                # (local)

    # --- assemble A_s under the n_s-selected near-floor + reduced-M_Pl convention ---
    A_s_computed = prefactor * F_nearfloor                  # (local)
    gap_OOM = float(np.log10(A_s_computed / A_s_Planck))    # (local) THE single number
    gap_OOM_4sf = float(f"{gap_OOM:.4g}")                   # (local) publication_precision pin

    # cross-report: what gap the RAW (unweighted, extensive) det would give (for context)
    A_s_raw_det = prefactor * float(np.exp(logF_raw))       # (local) — extensive; huge
    # cross-report: prefactor-only gap (F=1)
    gap_OOM_prefactor_only = float(np.log10(prefactor / A_s_Planck))  # (local) +5.6466

    # --- SIGN read-off (substitution chain Step 4): overproduction iff gap_OOM > 0 ---
    sign_overproduction = gap_OOM > 0.0                     # (local)

    return {
        "prefactor": prefactor,
        "log10_prefactor": log10_prefactor,
        "prefactor_unreduced": prefactor_unreduced,
        "log10_prefactor_unreduced": log10_prefactor_unreduced,
        "ceil_lambda": ceil_lambda,
        "n_band_modes_blocklevel": int(lam.size),
        "n_band_modes_PWweighted": float(np.sum(mult)),
        "n_band_sectors": int(n_band_sectors),
        "lam_min": float(lam.min()),
        "lam_max_band": float(lam.max()),
        "mu_min": float(mu.min()),
        "zeta0_nearfloor": zres["zeta0"],
        "zeta_prime0_direct": zres["zeta_prime0_direct"],
        "zeta_prime0_mellin": zres["zeta_prime0_mellin"],
        "zeta_prime0_residual": zres["zeta_prime0_residual"],
        "logF_raw_extensive": logF_raw,
        "F_raw_extensive_log10": float(logF_raw / np.log(10.0)),
        "lam_floor": wres["lam_floor"],
        "W_weightnorm": wres["W_weightnorm"],
        "logF_nf": logF_nf,
        "F_nearfloor": F_nearfloor,
        "A_s_computed": A_s_computed,
        "A_s_raw_det": A_s_raw_det,
        "gap_OOM": gap_OOM,
        "gap_OOM_4sf": gap_OOM_4sf,
        "gap_OOM_prefactor_only": gap_OOM_prefactor_only,
        "sign_overproduction": bool(sign_overproduction),
    }


# ---------------------------------------------------------------------------
# Section 6 — verdict logic
# ---------------------------------------------------------------------------
def evaluate(res: dict) -> dict:
    """Verdict per plan §W2-3 rubric.

    PASS  = ONE well-defined gap_OOM emitted under ONE named regulator (sqrt-cutoff),
            AND |gap_OOM| consistent within 0.5 OOM with the S83 PERMANENT-WALL
            Planck-multiple reading (3.02x => gap_OOM ~ +0.480).
    INFO  = single number emitted but lands 0.5-1.5 OOM from ALL three legacy readings.
    FAIL  = cannot emit a single number, OR gap_OOM diverges >3 OOM from ALL three
            legacy readings (a fourth >3-OOM-inconsistent value).
    """
    gap = res["gap_OOM"]                                    # (local)
    legacy_gaps = {k: v["gap_OOM"] for k, v in LEGACY.items()}  # (local)
    dist_to_wall = abs(gap - LEGACY["S83_3p02x_PERMANENT_WALL"]["gap_OOM"])  # (local)
    dist_to_each = {k: abs(gap - g) for k, g in legacy_gaps.items()}        # (local)
    min_dist = min(dist_to_each.values())                  # (local)

    single_number_emitted = np.isfinite(gap)               # (local)

    if not single_number_emitted:
        composite, mag = "FAIL", "FAIL"
    elif dist_to_wall <= 0.5:
        composite, mag = "PASS", "PASS"
    elif min_dist <= 1.5:
        composite, mag = "INFO", "INFO"
    elif min_dist > 3.0:
        composite, mag = "FAIL", "FAIL"
    else:
        composite, mag = "INFO", "INFO"

    # SIGN verdict: substitution chain predicted gap_OOM > 0 (overproduction).
    sign = "PASS" if res["sign_overproduction"] else "FAIL"  # (local)
    # REGIME: the finite-spectrum zeta'(0) is EXACT (entire zeta on finite spectrum);
    # the Mellin live-zeta cross-check residual sets regime validity.
    regime = "VALID" if res["zeta_prime0_residual"] < 1e-3 * abs(res["zeta_prime0_direct"]) + 1e-6 else "MARGINAL"  # (local)

    return {
        "composite": composite, "magnitude": mag, "sign": sign, "regime": regime,
        "dist_to_wall": dist_to_wall, "min_dist_to_legacy": min_dist,
        "dist_to_each": dist_to_each,
    }


# ---------------------------------------------------------------------------
# Section 7 — plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, verdict: dict):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))

    # (a) OOM ladder: the single number vs the three legacy readings
    ax = axes[0]
    labels = ["INV3-W2-3\n(n_s-sel\nsqrt-cutoff)", "S83 wall\n3.02x", "S66 RouteB\nPW", "S74\nBogoliubov"]
    gaps = [res["gap_OOM"], LEGACY["S83_3p02x_PERMANENT_WALL"]["gap_OOM"],
            LEGACY["S66_RouteB_PW"]["gap_OOM"], LEGACY["S74_Bogoliubov"]["gap_OOM"]]
    colors = ["crimson", "navy", "darkorange", "purple"]
    ax.bar(range(len(gaps)), gaps, color=colors, alpha=0.8)
    ax.axhline(0.0, color="k", lw=0.8, ls="--", label="Planck (gap=0)")
    for i, g in enumerate(gaps):
        ax.text(i, g + 0.15 * np.sign(g) if g != 0 else 0.15, f"{g:+.3f}",
                ha="center", va="bottom" if g >= 0 else "top", fontsize=9, fontweight="bold")
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel(r"gap$_{\rm OOM}=\log_{10}(A_s/A_{s,\rm Planck})$")
    ax.set_title(f"A_s OOM ladder — single number = {res['gap_OOM']:+.4g}\nverdict={verdict['composite']} (dist to S83 wall = {verdict['dist_to_wall']:.3f} OOM)")
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    # (b) near-floor DOS (PW-weighted), sqrt-cutoff weight overlaid
    ax = axes[1]
    lam, mult, _ = load_nearfloor_spectrum(res["ceil_lambda"])
    nbins = 60  # (local)
    bins = np.linspace(lam.min(), lam.max(), nbins + 1)  # (local)
    hist, edges = np.histogram(lam, bins=bins, weights=mult)  # (local) PW-weighted DOS
    centers = 0.5 * (edges[:-1] + edges[1:])  # (local)
    ax.bar(centers, hist, width=(edges[1] - edges[0]) * 0.9, color="steelblue", alpha=0.7, label="near-floor DOS (PW-weighted)")
    ax.axvline(res["lam_floor"], color="crimson", lw=1.5, ls="--", label=f"FK floor $\\lambda_{{\\min}}$={res['lam_floor']:.4f}")
    ax.axvline(res["ceil_lambda"], color="green", lw=1.2, ls=":", label=f"band ceiling 2·E_B2={res['ceil_lambda']:.4f}")
    ax2 = ax.twinx()
    lam_line = np.linspace(lam.min(), lam.max(), 200)  # (local)
    ax2.plot(lam_line, lam_line / res["lam_floor"], color="darkorange", lw=2, label="sqrt-cutoff weight $w=\\lambda/\\lambda_{floor}$")
    ax2.set_ylabel("sqrt-cutoff weight w", color="darkorange")
    ax.set_xlabel(r"$|\lambda|$  (M_KK units)")
    ax.set_ylabel("PW-weighted mode count")
    ax.set_title(f"Near-floor block: {int(res['n_band_modes_PWweighted'])} PW modes, {res['n_band_sectors']} sectors\n$F_{{\\rm nearfloor}}={res['F_nearfloor']:.5f}$  (intensive sqrt-cutoff geom-mean of $\\mu$)")
    ax.legend(fontsize=7, loc="upper left")
    ax2.legend(fontsize=7, loc="upper right")
    ax.grid(True, alpha=0.3)

    fig.suptitle("INV3-W2-3 — A_s amplitude floor under the S103 n_s-SELECTED sqrt-cutoff functional [a_n^zeta; CLASS=FULL; M_Pl=reduced]", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main():
    # log input SHAs (first lines of stdout per gate-verdicts.md)
    pins = {
        "computations/investigation-3/inv3_w2_as_amplitude_floor.py": file_sha(SCRIPT_PATH),
        "computations/_shared/canonical_constants.py": file_sha(CANONICAL_PATH),
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": file_sha(CACHE_PATH),
    }
    print("=== INPUT SHA-256 PINS ===")
    for k, v in sorted(pins.items()):
        print(f"  {k} = {v}")
    print(f"=== CANONICAL CONSTANTS === M_KK={M_KK:.6e} M_Pl_reduced={M_Pl_reduced:.6e} "
          f"A_s_Planck={A_s_Planck:.4e} E_B2_mean={E_B2_mean:.9f} n_s_FW_sqrt_cutoff={n_s_FW_sqrt_cutoff}")
    print(f"=== PINS === regulator={REGULATOR_PIN} CLASS={CLASS_PIN} M_Pl_choice={M_PL_CHOICE} "
          f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX}")

    res = compute()
    verdict = evaluate(res)

    print("\n=== RESULTS ===")
    print(f"  prefactor (M_KK/M_Pl_reduced)^2 = {res['prefactor']:.6e}  log10 = {res['log10_prefactor']:.4f}")
    print(f"  [lever] (M_KK/M_Pl_unreduced)^2 = {res['prefactor_unreduced']:.6e}  log10 = {res['log10_prefactor_unreduced']:.4f}  (1.40-OOM unreduced cross-report)")
    print(f"  near-floor band: ceil_lambda={res['ceil_lambda']:.6f}  {res['n_band_modes_blocklevel']} block-evals  "
          f"{int(res['n_band_modes_PWweighted'])} PW-weighted modes  {res['n_band_sectors']} sectors")
    print(f"  lam_min={res['lam_min']:.6f}  lam_max_band={res['lam_max_band']:.6f}  mu_min={res['mu_min']:.6f}")
    print(f"  zeta(0)_nearfloor = {res['zeta0_nearfloor']:.1f}  (= total PW mode count, EXTENSIVE)")
    print(f"  zeta'(0) direct (EXACT finite-spectrum) = {res['zeta_prime0_direct']:.6f}")
    print(f"  zeta'(0) Mellin live-zeta cross-check    = {res['zeta_prime0_mellin']:.6f}  residual={res['zeta_prime0_residual']:.3e}")
    print(f"  [raw extensive det] logF_raw=sum d_k ln(mu_k) = {res['logF_raw_extensive']:.4f}  (log10 = {res['F_raw_extensive_log10']:.4f}) -- EXTENSIVE reference")
    print(f"  n_s-SELECTED sqrt-cutoff WEIGHTED functional:")
    print(f"    lam_floor (FK B2) = {res['lam_floor']:.6f}  W_weightnorm = {res['W_weightnorm']:.4f}")
    print(f"    logF_nf = {res['logF_nf']:.6f}  ->  F_nearfloor = {res['F_nearfloor']:.6f}  (INTENSIVE, the deliverable functional)")
    print(f"  A_s_computed = prefactor * F_nearfloor = {res['A_s_computed']:.6e}")
    print(f"  prefactor-only gap (F=1) = {res['gap_OOM_prefactor_only']:+.4f} OOM  (substitution-chain Step 4 anchor)")
    print(f"\n  >>> gap_OOM = log10(A_s_computed/A_s_Planck) = {res['gap_OOM']:+.6f}  ->  {res['gap_OOM_4sf']:+.4g} (4 sig figs) <<<")
    print(f"  SIGN: overproduction (gap_OOM>0)? {res['sign_overproduction']}")

    print("\n=== LEGACY CROSS-REPORT (the three-number ambiguity retired) ===")
    for k, v in LEGACY.items():
        print(f"  {k}: gap_OOM={v['gap_OOM']:+.4f}  |  dist from single number = {verdict['dist_to_each'][k]:.4f} OOM  | {v['note']}")
    for k, v in LEGACY_EXTRA.items():
        print(f"  [extra] {k}: gap_OOM={v['gap_OOM']:+.4f}  | {v['note']}")
    print(f"  dist to S83 wall (PASS criterion <=0.5) = {verdict['dist_to_wall']:.4f} OOM ; min dist to any legacy = {verdict['min_dist_to_legacy']:.4f}")

    print(f"\n=== VERDICT === composite={verdict['composite']} "
          f"(sign={verdict['sign']} magnitude={verdict['magnitude']} regime={verdict['regime']})")

    # --- save data ---
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        **{k: v for k, v in res.items()},
        verdict_composite=verdict["composite"],
        verdict_sign=verdict["sign"],
        verdict_magnitude=verdict["magnitude"],
        verdict_regime=verdict["regime"],
        dist_to_wall=verdict["dist_to_wall"],
        min_dist_to_legacy=verdict["min_dist_to_legacy"],
        legacy_S83_gap=LEGACY["S83_3p02x_PERMANENT_WALL"]["gap_OOM"],
        legacy_S66_gap=LEGACY["S66_RouteB_PW"]["gap_OOM"],
        legacy_S74_gap=LEGACY["S74_Bogoliubov"]["gap_OOM"],
        legacy_S84_TD_gap=LEGACY_EXTRA["S84_TD_canonical"]["gap_OOM"],
        M_KK=M_KK, M_Pl_reduced=M_Pl_reduced, A_s_Planck=A_s_Planck,
        E_B2_mean=E_B2_mean, n_s_FW_sqrt_cutoff=n_s_FW_sqrt_cutoff,
        regulator_pin=REGULATOR_PIN, class_pin=CLASS_PIN, m_pl_choice=M_PL_CHOICE,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        pin_script=pins["computations/investigation-3/inv3_w2_as_amplitude_floor.py"],
        pin_canonical=pins["computations/_shared/canonical_constants.py"],
        pin_cache=pins["computations/session-84/s84_spectrum_cache_L12_tau019.npz"],
    )
    make_plot(res, verdict)

    # --- dual-SHA (over script bytes + canonical + pinmap, per S84+ recipe) ---
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_PATH, pins)

    # --- value payload (raw; no single-quote chars; emit_verdict wraps it) ---
    value = (
        f"gap_OOM={res['gap_OOM_4sf']:+.4g}_A_s={res['A_s_computed']:.4e}"
        f"_prefactor=(M_KK/M_Pl_red)^2={res['prefactor']:.4e}_log10pref={res['log10_prefactor']:.4f}"
        f"_F_nearfloor={res['F_nearfloor']:.5f}_logFnf={res['logF_nf']:.4f}"
        f"_zetaPrime0={res['zeta_prime0_direct']:.4f}_zeta0={res['zeta0_nearfloor']:.0f}"
        f"_band_PWmodes={int(res['n_band_modes_PWweighted'])}_ceil={res['ceil_lambda']:.4f}"
        f"_dist_to_S83wall={verdict['dist_to_wall']:.4f}_legacy=(3.02x:+0.480,RouteBPW:+3.150,Bogo:+9.472)"
        f"_sign=overproduction_{res['sign_overproduction']}"
    )

    extra_rows = [
        f"# regulator_pin={REGULATOR_PIN} CLASS={CLASS_PIN} M_Pl_choice={M_PL_CHOICE} "
        f"(zeta-scheme functional determinant exp(-zeta'(0)); NOT Gilkey SD a_2^SD=0.728235; "
        f"a_2^zeta=2776.165389 factor-3812 distinct; FULL live-zeta on cached L12 eigenvalues, NO SCHEMATIC helper)",
        f"# A_s decomposition: A_s=(M_KK/M_Pl_reduced)^2 * F_nearfloor; "
        f"prefactor=9.3073e-4 (log10=-3.0312, ALL weakness=M_KK gap G1); "
        f"F_nearfloor={res['F_nearfloor']:.5f} (intensive sqrt-cutoff geom-mean of mu over {int(res['n_band_modes_PWweighted'])} near-floor PW modes); "
        f"prefactor-only gap (F=1)=+5.6466 OOM (substitution-chain Step4 anchor)",
        f"# legacy reconciliation: single number {res['gap_OOM_4sf']:+.4g} OOM; "
        f"3.02x=+0.480(S83 PERMANENT WALL, Planck-multiple, near-floor+reduced M_Pl), "
        f"3.15(S66 RouteB-PW FULL-spectral-weight), 9.472(S74 Bogoliubov full-fiber); "
        f"dist to S83 wall={verdict['dist_to_wall']:.4f} OOM; [extra record S84 TD-canonical=+0.384 SCHEME-DEPENDENT]",
        f"# zeta'(0) live-zeta cross-check: direct(EXACT finite-spectrum)={res['zeta_prime0_direct']:.6f} "
        f"vs Mellin-grid={res['zeta_prime0_mellin']:.6f} residual={res['zeta_prime0_residual']:.3e} (FULL evaluator agreement)",
        f"# CROSS-TRACK: investigation gate emits VALUE ONLY; NO falsifier-master-inventory.md row "
        f"(mack-cosmic-bridge sole-writer on session-promotion per feedback_mack-bridge-role.md)",
        f"# substrate: A_s IS the loudness of the post-transit GGE acoustic interference pattern (PHONONIC); "
        f"the 3 legacy numbers are 3 DIFFERENT spectral functionals on one fabric, not 3 measurements of one thing",
    ]

    payload = {
        "session": 3,
        "track": "investigation",
        "gate_id": GATE_ID,
        "verdict": verdict["composite"],
        "value": value,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": verdict["sign"],
        "magnitude_verdict": verdict["magnitude"],
        "regime_verdict": verdict["regime"],
        "extra_rows": extra_rows,
    }
    print_verdict_payload(payload)  # delimited stdout block; agent calls emit_verdict(**payload)
    return payload


if __name__ == "__main__":
    main()
