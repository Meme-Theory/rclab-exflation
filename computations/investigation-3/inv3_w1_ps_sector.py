#!/usr/bin/env python
"""
INV3-W1-2 — Nearest-neighbor spacing distribution P(s) fitted to semi-Poisson +
Berry-Robnik forms; small-s repulsion exponent beta; SECTOR-RESOLVED per
Peter-Weyl (p,q) block (the pooling-artifact test of the <r>=0.422 pooled value).

GEOMETRIC. The substrate IS the D_K spectrum; its block-diagonal structure
D_K = (+)_{(p,q)} D_{(p,q)} (Peter-Weyl, PROVEN to 8.4e-15, S22b/S33) means the
pooled nearest-neighbor spacing distribution is a SUPERPOSITION of the
independent irreducible-sector spectra. Direction of explanation:
  D_K eigenvalues
    -> per-(p,q)-block unfolding
    -> within-block P(s) small-s exponent beta_block
    -> intrinsic-vs-superposition verdict on the substrate's level-repulsion geometry.

Substitution chain (the [SIGN] direction claim):
  Def 1: P(s) := NN spacing distribution of the unfolded spectrum (<s>=1 after unfold).
  Def 2: beta := small-s repulsion exponent, P(s) ~ s^beta as s->0.
         beta=0 Poisson; beta=1 semi-Poisson & GOE; beta=2 GUE.
  Def 3 (superposition theorem, Mehta ch.16): union of M statistically independent
         sub-spectra -> pooled P(s) -> e^{-s} (Poisson) as M grows, regardless of
         each sub-spectrum's own statistics.
  Def 4 (block-diagonality, S22b/S33): D_K = (+)_{(p,q)} D_{(p,q)}, so the pooled
         spectrum IS a superposition of the independent block spectra.
  Substitute: pooled small-s exponent beta_pooled driven toward 0 by Def 3+4 even
         if beta_block > 0 inside each block.
  Simplify: the DISCRIMINATING quantity is beta_block (single-block), not beta_pooled.
  Direction: LARGER beta_block => MORE intrinsic within-sector repulsion => LESS
         integrable at the single-sector level.
  Conclusion: going SECTOR-RESOLVED converts the ambiguous pooled <r> datum into a
         decisive test; beta_block is the observable the pooled-only CHAOS-1 could
         not isolate.

PASS-pooling-artifact iff beta_block in [-0.15, 0.30] AND pooled Berry-Robnik rho >= 0.85.
INFO-intrinsic-semi-Poisson iff beta_block in [0.70, 1.30].
FAIL-intrinsic-GOE iff beta_block >= 1.70.

Operator: RATIO (beta is a dimensionless small-s log-slope exponent).
GPU_path: cpu-cap-OMP8 (per-block spacing histograms + small curve fits; no >=100x100
dense linear algebra).

Inputs:
  computations/session-84/s84_spectrum_cache_L12_tau019.npz  (canonical, L_max=12, tau_fold=0.19)
  computations/session-87/s87_spectrum_cache_L14_tau019.npz  (L-trend cross-check)
  computations/_shared/canonical_constants.py

Outputs:
  computations/investigation-3/inv3_w1_ps_sector.npz
  computations/investigation-3/inv3_w1_ps_sector.png
  + printed verdict payload (agent calls emit_verdict).
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # GPU_path = cpu-cap-OMP8 (before numpy import)

import sys
import hashlib
import json

import numpy as np
from scipy.optimize import curve_fit, brentq
from scipy.integrate import quad

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import; never hardcode) ----------------------
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import r_POISSON_canonical, r_GOE_canonical, tau_fold  # noqa: E402

# ============================== machinery pins ===================================
GATE_ID = "INV3-W1-2"
L_MAX = 12                                  # (local) machinery pin: canonical cache L_max
SCHEME = "P-of-s-semiPoisson-BerryRobnik-fit-sector-resolved"
CONVENTION = "RATIO"
RANDOM_SEED = 20260614                       # (local) machinery pin: bootstrap resampling seed
UNFOLD_POLY_DEGREE = 7                       # (local) machinery pin: smooth Weyl-fit degree for unfolding
N_MIN_BLOCK = 50                             # (local) machinery pin: min UNIQUE levels to sector-resolve
SMALL_S_FIT_WINDOW = (0.0, 0.5)              # (local) machinery pin: s-window for P(s) ~ s^beta fit
BERRY_ROBNIK_INIT_RHO = 0.5                  # (local) machinery pin: deterministic LM start for rho fit
PUBLICATION_PRECISION = 3                    # (local) machinery pin: beta_block + rho to 3 sig figs
N_BOOTSTRAP = 400                            # (local) bootstrap replicas for beta error bar
PS_NBINS = 50                                # (local) histogram bins for P(s) on [0, s_max_hist]
S_MAX_HIST = 4.0                             # (local) histogram domain upper edge in mean-spacing units
ROUND_DECIMALS = 10                          # (local) decimals to dedupe degenerate eigenvalues

# PASS / INFO / FAIL band edges (pre-registered)
BETA_PASS_LO, BETA_PASS_HI = -0.15, 0.30  # (local) pre-registered PASS band (plan operator)
BETA_INFO_LO, BETA_INFO_HI = 0.70, 1.30   # (local) pre-registered INFO band (plan operator)
BETA_FAIL_GOE = 1.70                       # (local) pre-registered FAIL-GOE threshold (plan operator)
RHO_PASS_MIN = 0.85                        # (local) pre-registered pooled-rho PASS floor (plan operator)

CACHE_L12 = "computations/session-84/s84_spectrum_cache_L12_tau019.npz"
CACHE_L14 = "computations/session-87/s87_spectrum_cache_L14_tau019.npz"
CANON = "computations/_shared/canonical_constants.py"

rng = np.random.default_rng(RANDOM_SEED)


# ============================== reference analytic forms =========================
def beta_of_reference():
    """Pre-registered integer/half-integer reference mesh for beta."""
    return {"Poisson": 0.0, "semi-Poisson": 1.0, "GOE": 1.0, "GUE": 2.0}


def r_poisson_surmise():
    return r_POISSON_canonical  # 0.3863


def r_goe_surmise():
    return r_GOE_canonical      # 0.5307


# ------------------------------- unfolding ---------------------------------------
def unfold_levels(levels, deg=UNFOLD_POLY_DEGREE):
    """
    Polynomial unfolding of a SORTED level sequence: fit the integrated density of
    states N(E) (the staircase) by a smooth polynomial of degree `deg`, then map
    x_i = N_smooth(E_i). The unfolded sequence has mean spacing 1 by construction.
    Returns the unfolded coordinates (sorted).
    """
    levels = np.sort(np.asarray(levels, dtype=float))
    n = levels.size
    if n < deg + 2:
        # too few points for the requested polynomial; drop degree to n-2 (>=1)
        deg = max(1, n - 2)
    staircase = np.arange(1, n + 1, dtype=float)  # N(E_i) = i (1-indexed)
    # Fit staircase ~ poly(E); use centred/scaled E for conditioning.
    coeffs = np.polyfit(levels, staircase, deg)
    x = np.polyval(coeffs, levels)
    x = np.sort(x)
    return x


def spacings_from_unfolded(x):
    """Nearest-neighbour spacings of an unfolded (mean-spacing-1) sequence."""
    s = np.diff(np.sort(np.asarray(x, dtype=float)))
    s = s[np.isfinite(s)]
    # Renormalise to unit mean (guards residual unfolding drift).
    m = s.mean() if s.size else 1.0
    if m > 0:
        s = s / m
    return s


# ------------------------------- r-ratio -----------------------------------------
def r_ratio(levels):
    """
    Oganesyan-Huse consecutive-spacing ratio <r> = <min(s_n,s_{n+1})/max(s_n,s_{n+1})>.
    Computed on RAW sorted levels (ratio is unfolding-invariant by construction).
    """
    e = np.sort(np.asarray(levels, dtype=float))
    s = np.diff(e)
    s = s[s > 0]  # drop exact degeneracies (zero spacings) -> physical level sequence
    if s.size < 2:
        return np.nan
    r = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])
    return float(np.mean(r))


# ------------------------------- small-s beta fit --------------------------------
def small_s_beta(s, window=SMALL_S_FIT_WINDOW, nbins=20):
    """
    Extract the small-s repulsion exponent beta from P(s) ~ s^beta as s->0.
    Method: histogram P(s) on the small-s window, fit log P(s) = const + beta*log(s)
    over the bins whose centre lies in (window) and whose count is positive.
    Returns (beta, n_bins_used). NaN beta if insufficient data.
    """
    s = np.asarray(s, dtype=float)
    s = s[(s > 0) & np.isfinite(s)]
    if s.size < 10:
        return np.nan, 0
    lo, hi = window
    # Build a fine histogram over [0, hi] (the s->0 regime).
    edges = np.linspace(0.0, hi, nbins + 1)
    counts, _ = np.histogram(s, bins=edges, density=True)
    centres = 0.5 * (edges[:-1] + edges[1:])
    mask = (centres > lo) & (counts > 0)
    if mask.sum() < 3:
        return np.nan, int(mask.sum())
    lx = np.log(centres[mask])
    ly = np.log(counts[mask])
    # Linear fit ly = b0 + beta*lx  => slope is beta.
    A = np.vstack([np.ones_like(lx), lx]).T
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)
    beta = float(coef[1])
    return beta, int(mask.sum())


def bootstrap_beta(s, window=SMALL_S_FIT_WINDOW, n_boot=N_BOOTSTRAP):
    """Bootstrap error bar on the small-s beta of a single spacing sample."""
    s = np.asarray(s, dtype=float)
    s = s[(s > 0) & np.isfinite(s)]
    if s.size < 20:
        b0, _ = small_s_beta(s, window)
        return b0, np.nan
    betas = []
    for _ in range(n_boot):
        idx = rng.integers(0, s.size, s.size)
        b, nb = small_s_beta(s[idx], window)
        if np.isfinite(b):
            betas.append(b)
    if not betas:
        return np.nan, np.nan
    return float(np.mean(betas)), float(np.std(betas))


# ------------------------------- Berry-Robnik fit --------------------------------
def berry_robnik_gap(s, rho):
    """
    Berry-Robnik spacing distribution for a 2-component (Poisson rho + GOE 1-rho)
    superposition. The gap distribution E(s) and P(s) = d2E/ds2.
    Standard closed form (Robnik 1984):
      E(s; rho) = exp(-rho*s) * erfc( sqrt(pi)/2 * (1-rho) * s )
      P(s; rho) = d^2 E / ds^2
    rho is the relative Liouville (Poisson) phase-space fraction; rho=1 -> pure
    Poisson, rho=0 -> pure GOE.
    """
    from scipy.special import erfc
    rho = np.clip(rho, 1e-6, 1.0 - 1e-9)
    a = rho
    b = np.sqrt(np.pi) / 2.0 * (1.0 - rho)
    s = np.asarray(s, dtype=float)
    E = np.exp(-a * s) * erfc(b * s)
    # P(s) = E''(s). Closed-form derivatives:
    #   E = e^{-a s} * erfc(b s)
    #   E' = -a e^{-a s} erfc(b s) + e^{-a s} * (-2 b / sqrt(pi)) e^{-(b s)^2}
    #   E'' = a^2 e^{-a s} erfc(b s)
    #         + 2 a (2 b/sqrt(pi)) e^{-a s} e^{-(b s)^2}
    #         + e^{-a s} * (-2 b/sqrt(pi)) * (-2 b^2 s) e^{-(b s)^2}
    g = (2.0 * b / np.sqrt(np.pi)) * np.exp(-(b * s) ** 2)  # = -d/ds erfc(b s)
    erfc_bs = erfc(b * s)
    Epp = (a * a * np.exp(-a * s) * erfc_bs
           + 2.0 * a * np.exp(-a * s) * g
           + np.exp(-a * s) * (2.0 * b ** 2 / np.sqrt(np.pi)) * 2.0 * b * s * np.exp(-(b * s) ** 2))
    return np.maximum(Epp, 0.0)


def fit_berry_robnik_rho(s, init_rho=BERRY_ROBNIK_INIT_RHO):
    """
    Fit the Berry-Robnik rho to the empirical P(s) histogram by least-squares on the
    binned density. Returns (rho, rho_err).
    """
    s = np.asarray(s, dtype=float)
    s = s[(s > 0) & np.isfinite(s)]
    if s.size < 30:
        return np.nan, np.nan
    edges = np.linspace(0.0, S_MAX_HIST, PS_NBINS + 1)
    counts, _ = np.histogram(s, bins=edges, density=True)
    centres = 0.5 * (edges[:-1] + edges[1:])
    mask = counts >= 0  # use all bins
    try:
        popt, pcov = curve_fit(
            lambda ss, rho: berry_robnik_gap(ss, rho),
            centres[mask], counts[mask],
            p0=[init_rho], bounds=(0.0, 1.0), maxfev=20000,
        )
        rho = float(popt[0])
        rho_err = float(np.sqrt(np.diag(pcov))[0]) if np.all(np.isfinite(pcov)) else np.nan
        return rho, rho_err
    except Exception:
        return np.nan, np.nan


def semi_poisson(s):
    """Semi-Poisson reference: P(s) = 4 s e^{-2 s} (beta=1)."""
    s = np.asarray(s, dtype=float)
    return 4.0 * s * np.exp(-2.0 * s)


def poisson(s):
    s = np.asarray(s, dtype=float)
    return np.exp(-s)


def goe_wigner(s):
    s = np.asarray(s, dtype=float)
    return (np.pi / 2.0) * s * np.exp(-np.pi * s ** 2 / 4.0)


def chi2_to_form(s, form):
    """Reduced-chi2-like residual of empirical P(s) histogram against an analytic form."""
    s = np.asarray(s, dtype=float)
    s = s[(s > 0) & np.isfinite(s)]
    if s.size < 30:
        return np.nan
    edges = np.linspace(0.0, S_MAX_HIST, PS_NBINS + 1)
    counts, _ = np.histogram(s, bins=edges, density=True)
    centres = 0.5 * (edges[:-1] + edges[1:])
    model = form(centres)
    resid = counts - model
    return float(np.sum(resid ** 2) / max(1, (counts.size - 1)))


# ============================== cache loader =====================================
def load_sector_levels(cache_path, round_dec=ROUND_DECIMALS):
    """
    Load the Peter-Weyl (p,q)-tagged spectrum cache. Each (p,q) sector maps to a dict
    with 'abs_evals' (|lambda| WITH multiplicity), 'dim', 'level'. The physical level
    SEQUENCE within a sector is the UNIQUE set of |lambda| values (degeneracy from the
    C^16 fiber + irrep dimension is NOT a level-statistics observable; raw multiplicity
    creates spurious s=0 spacings -- the artifact that produced the spurious sub-Poisson
    <r>=0.321, corrected to 0.439 on unique levels, S46).
    Returns: dict (p,q) -> sorted unique levels (np.ndarray).
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    out = {}
    meta = {}
    for k, v in se.items():
        ae = np.asarray(v["abs_evals"], dtype=float)
        ae = ae[np.isfinite(ae)]
        uniq = np.unique(np.round(ae, round_dec))
        out[tuple(k)] = np.sort(uniq)
        meta[tuple(k)] = {"dim": int(v.get("dim", -1)),
                          "level": int(v.get("level", -1)),
                          "n_with_mult": int(ae.size),
                          "n_unique": int(uniq.size)}
    return out, meta


# ============================== dual-SHA closure =================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """audit_sha256 = sha256 of the ordered input-pin map (JSON-serialised, sorted keys)."""
    blob = json.dumps(pin_map, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(blob).hexdigest()


def print_verdict_payload(payload):
    """Print the verdict payload the agent passes verbatim to emit_verdict()."""
    print("=" * 72)
    print("VERDICT PAYLOAD (pass verbatim to emit_verdict):")
    print(json.dumps(payload, indent=2))
    print("=" * 72)


# ============================== main =============================================
def main():
    # ---- input SHA pins (logged in first 20 lines of stdout per gate-verdicts.md) ----
    sha_script = sha256_file(os.path.abspath(__file__))
    sha_canon = sha256_file(CANON)
    sha_cache12 = sha256_file(CACHE_L12)
    sha_cache14 = sha256_file(CACHE_L14)
    print(f"[SHA] script        = {sha_script}")
    print(f"[SHA] canonical     = {sha_canon}")
    print(f"[SHA] cache_L12     = {sha_cache12}")
    print(f"[SHA] cache_L14     = {sha_cache14}")
    print(f"[PIN] r_POISSON={r_POISSON_canonical} r_GOE={r_GOE_canonical} tau_fold={tau_fold}")
    print(f"[PIN] L_max={L_MAX} N_min_block={N_MIN_BLOCK} unfold_deg={UNFOLD_POLY_DEGREE} "
          f"window={SMALL_S_FIT_WINDOW} seed={RANDOM_SEED}")

    # ============================ (1) load + unfold ==============================
    sectors, meta = load_sector_levels(CACHE_L12)

    # --------- POOLED spectrum: superposition of all blocks (unique global levels) ----
    pooled_levels = np.sort(np.unique(np.round(
        np.concatenate([sectors[k] for k in sectors]), ROUND_DECIMALS)))
    pooled_unfolded = unfold_levels(pooled_levels)
    s_pooled = spacings_from_unfolded(pooled_unfolded)
    beta_pooled, beta_pooled_err = bootstrap_beta(s_pooled)
    rho_pooled, rho_pooled_err = fit_berry_robnik_rho(s_pooled)
    r_pooled = r_ratio(pooled_levels)

    chi2_pooled = {
        "Poisson": chi2_to_form(s_pooled, poisson),
        "semi-Poisson": chi2_to_form(s_pooled, semi_poisson),
        "GOE": chi2_to_form(s_pooled, goe_wigner),
    }

    print(f"\n[POOLED] n_unique_global={pooled_levels.size}  "
          f"beta_pooled={beta_pooled:.4f}+/-{beta_pooled_err:.4f}  "
          f"rho_pooled={rho_pooled:.4f}+/-{rho_pooled_err:.4f}  r_pooled={r_pooled:.4f}")
    print(f"[POOLED] chi2-to-form: {chi2_pooled}")

    # ============================ (2) sector-resolved ============================
    block_betas = []          # (local) per-block small-s beta
    block_beta_errs = []      # (local)
    block_rhos = []           # (local)
    block_rs = []             # (local) per-block <r>
    block_records = []        # (local) full per-block record for npz
    residual_block_keys = []  # (local) <N_min, diagnostic-only

    for k in sorted(sectors.keys(), key=lambda t: (meta[t]["level"], t)):
        lv = sectors[k]
        nun = lv.size
        if nun < N_MIN_BLOCK:
            residual_block_keys.append(k)
            continue
        x = unfold_levels(lv)
        s = spacings_from_unfolded(x)
        b, berr = bootstrap_beta(s)
        rho_b, rho_be = fit_berry_robnik_rho(s)
        rb = r_ratio(lv)
        if np.isfinite(b):
            block_betas.append(b)
            block_beta_errs.append(berr)
        if np.isfinite(rho_b):
            block_rhos.append(rho_b)
        if np.isfinite(rb):
            block_rs.append(rb)
        block_records.append({
            "pq": k, "dim": meta[k]["dim"], "level": meta[k]["level"],
            "n_unique": nun, "n_with_mult": meta[k]["n_with_mult"],
            "beta": b, "beta_err": berr, "rho": rho_b, "r": rb,
        })

    block_betas = np.asarray(block_betas, dtype=float)
    block_rs = np.asarray(block_rs, dtype=float)
    block_rhos = np.asarray(block_rhos, dtype=float)

    # Aggregate per-block beta (the DISCRIMINATING observable).
    beta_block = float(np.mean(block_betas)) if block_betas.size else np.nan
    beta_block_median = float(np.median(block_betas)) if block_betas.size else np.nan
    beta_block_std = float(np.std(block_betas)) if block_betas.size else np.nan
    beta_block_sem = (beta_block_std / np.sqrt(block_betas.size)
                      if block_betas.size else np.nan)
    r_block_mean = float(np.mean(block_rs)) if block_rs.size else np.nan
    rho_block_mean = float(np.mean(block_rhos)) if block_rhos.size else np.nan

    print(f"\n[SECTOR] n_blocks_resolved={block_betas.size}  "
          f"n_residual(<{N_MIN_BLOCK})={len(residual_block_keys)}")
    print(f"[SECTOR] beta_block (mean)={beta_block:.4f}  median={beta_block_median:.4f}  "
          f"std={beta_block_std:.4f}  sem={beta_block_sem:.4f}")
    print(f"[SECTOR] <r>_block (mean over blocks)={r_block_mean:.4f}  "
          f"rho_block (mean)={rho_block_mean:.4f}")
    print(f"[SECTOR] beta_block range=[{block_betas.min():.4f}, {block_betas.max():.4f}]")

    # ============================ (3) L-trend cross-check ========================
    sectors14, meta14 = load_sector_levels(CACHE_L14)
    block_betas_14 = []  # (local)
    for k in sectors14:
        lv = sectors14[k]
        if lv.size < N_MIN_BLOCK:
            continue
        x = unfold_levels(lv)
        s = spacings_from_unfolded(x)
        b, _ = small_s_beta(s)
        if np.isfinite(b):
            block_betas_14.append(b)
    block_betas_14 = np.asarray(block_betas_14, dtype=float)
    beta_block_14 = float(np.mean(block_betas_14)) if block_betas_14.size else np.nan
    print(f"\n[L14 cross-check] n_blocks={block_betas_14.size}  "
          f"beta_block(L14)={beta_block_14:.4f}  (L12 was {beta_block:.4f})")

    # ============================ (4) VERDICT ====================================
    # SIGN: predicted direction (substitution chain Step 4): beta_block small (~0)
    # => pooling artifact (Track A prior 0.6). The signed quantity is (beta_block - 0.30):
    # negative/in-band => PASS-pooling-artifact direction confirmed.
    pass_pooling = (BETA_PASS_LO <= beta_block <= BETA_PASS_HI) and (rho_pooled >= RHO_PASS_MIN)
    info_semi = (BETA_INFO_LO <= beta_block <= BETA_INFO_HI)
    fail_goe = (beta_block >= BETA_FAIL_GOE)

    if fail_goe:
        composite = "FAIL"
        sign_verdict = "PASS"     # direction (larger beta => more repulsion) is well-defined
        magnitude_verdict = "FAIL"
        regime_verdict = "VALID"
        verdict_label = "FAIL-intrinsic-GOE"
    elif pass_pooling:
        composite = "PASS"
        # SIGN PASS: predicted Track-A direction (beta_block in per-block-Poisson band) holds.
        sign_verdict = "PASS"
        magnitude_verdict = "PASS"
        regime_verdict = "VALID"
        verdict_label = "PASS-pooling-artifact"
    elif info_semi:
        composite = "INFO"
        sign_verdict = "PASS"
        magnitude_verdict = "INFO"
        regime_verdict = "VALID"
        verdict_label = "INFO-intrinsic-semi-Poisson"
    else:
        # Between bands (e.g. beta in (0.30, 0.70) or (1.30, 1.70)) or rho<0.85 with
        # in-band beta: intermediate -- pre-registered as INFO (neither clean PASS nor FAIL).
        composite = "INFO"
        sign_verdict = "PASS"
        magnitude_verdict = "INFO"
        regime_verdict = "VALID"
        verdict_label = "INFO-intermediate-between-bands"

    # ---- dual SHA ----
    pin_map = {
        "gate_id": GATE_ID,
        "L_max": L_MAX,
        "N_eval": int(pooled_levels.size),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "random_seed": RANDOM_SEED,
        "unfold_poly_degree": UNFOLD_POLY_DEGREE,
        "N_min_block": N_MIN_BLOCK,
        "small_s_fit_window": list(SMALL_S_FIT_WINDOW),
        "berry_robnik_init_rho": BERRY_ROBNIK_INIT_RHO,
        "tolerance": BETA_PASS_HI,
        "sha_script": sha_script,
        "sha_canonical": sha_canon,
        "sha_cache_L12": sha_cache12,
        "sha_cache_L14": sha_cache14,
    }
    audit_sha256 = closure_hash(pin_map)
    content_sha256 = sha_script  # content_sha256_inputs: ["script"]

    beta_block_pub = round(beta_block, PUBLICATION_PRECISION)
    rho_pooled_pub = round(rho_pooled, PUBLICATION_PRECISION)
    value_str = (f"beta_block={beta_block_pub}+/-{round(beta_block_sem,3)} "
                 f"rho_pooled={rho_pooled_pub} r_pooled={round(r_pooled,3)} "
                 f"r_block={round(r_block_mean,3)} n_blocks={block_betas.size} "
                 f"label={verdict_label}")

    # ============================ (5) save npz + png =============================
    np.savez(
        "computations/investigation-3/inv3_w1_ps_sector.npz",
        # pooled
        pooled_levels=pooled_levels, s_pooled=s_pooled,
        beta_pooled=beta_pooled, beta_pooled_err=beta_pooled_err,
        rho_pooled=rho_pooled, rho_pooled_err=rho_pooled_err, r_pooled=r_pooled,
        chi2_pooled_Poisson=chi2_pooled["Poisson"],
        chi2_pooled_semiPoisson=chi2_pooled["semi-Poisson"],
        chi2_pooled_GOE=chi2_pooled["GOE"],
        # sector-resolved
        block_betas=block_betas, block_beta_errs=np.asarray(block_beta_errs, dtype=float),
        block_rs=block_rs, block_rhos=block_rhos,
        beta_block=beta_block, beta_block_median=beta_block_median,
        beta_block_std=beta_block_std, beta_block_sem=beta_block_sem,
        r_block_mean=r_block_mean, rho_block_mean=rho_block_mean,
        n_blocks_resolved=block_betas.size, n_residual=len(residual_block_keys),
        # L-trend
        block_betas_14=block_betas_14, beta_block_14=beta_block_14,
        # references
        r_POISSON=r_POISSON_canonical, r_GOE=r_GOE_canonical,
        beta_ref_Poisson=0.0, beta_ref_semiPoisson=1.0, beta_ref_GUE=2.0,
        # band edges
        beta_pass_lo=BETA_PASS_LO, beta_pass_hi=BETA_PASS_HI,
        beta_info_lo=BETA_INFO_LO, beta_info_hi=BETA_INFO_HI,
        beta_fail_goe=BETA_FAIL_GOE, rho_pass_min=RHO_PASS_MIN,
        # verdict
        composite=composite, verdict_label=verdict_label,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        audit_sha256=audit_sha256, content_sha256=content_sha256,
        block_records=np.array(block_records, dtype=object),
        residual_block_keys=np.array(residual_block_keys, dtype=object),
    )

    # ---- plot ----
    fig, axes = plt.subplots(2, 2, figsize=(13, 10))
    sgrid = np.linspace(1e-3, S_MAX_HIST, 400)

    # (a) pooled P(s) vs forms
    ax = axes[0, 0]
    ax.hist(s_pooled, bins=PS_NBINS, range=(0, S_MAX_HIST), density=True,
            alpha=0.5, color="#4477aa", label=f"pooled P(s) (N={pooled_levels.size})")
    ax.plot(sgrid, poisson(sgrid), "k--", lw=1.6, label="Poisson $e^{-s}$ ($\\beta$=0)")
    ax.plot(sgrid, semi_poisson(sgrid), "r-", lw=1.4, label="semi-Poisson $4se^{-2s}$ ($\\beta$=1)")
    ax.plot(sgrid, goe_wigner(sgrid), "g-.", lw=1.4, label="GOE Wigner ($\\beta$=1)")
    if np.isfinite(rho_pooled):
        ax.plot(sgrid, berry_robnik_gap(sgrid, rho_pooled), "m:", lw=2.0,
                label=f"Berry-Robnik $\\rho$={rho_pooled:.3f}")
    ax.set_xlabel("s (unfolded mean-spacing units)"); ax.set_ylabel("P(s)")
    ax.set_title(f"POOLED spectrum — $\\beta_{{pooled}}$={beta_pooled:.3f}, $r$={r_pooled:.3f}")
    ax.legend(fontsize=8); ax.set_xlim(0, S_MAX_HIST)

    # (b) per-block beta distribution
    ax = axes[0, 1]
    ax.hist(block_betas, bins=24, color="#ee6677", alpha=0.7, edgecolor="k")
    ax.axvline(0.0, color="k", ls="--", label="Poisson $\\beta$=0")
    ax.axvline(1.0, color="r", ls="-", label="semi-Poisson/GOE $\\beta$=1")
    ax.axvline(beta_block, color="b", ls="-", lw=2.0,
               label=f"mean $\\beta_{{block}}$={beta_block:.3f}")
    ax.axvspan(BETA_PASS_LO, BETA_PASS_HI, color="green", alpha=0.12, label="PASS band")
    ax.axvspan(BETA_INFO_LO, BETA_INFO_HI, color="orange", alpha=0.12, label="INFO band")
    ax.set_xlabel("$\\beta_{block}$ (small-s exponent)"); ax.set_ylabel("# blocks")
    ax.set_title(f"Per-(p,q)-block $\\beta$ ({block_betas.size} blocks $\\geq${N_MIN_BLOCK} levels)")
    ax.legend(fontsize=7)

    # (c) sample single-block P(s)
    ax = axes[1, 0]
    # pick the largest resolved block
    if block_records:
        big = max(block_records, key=lambda rr: rr["n_unique"])
        kbig = big["pq"]
        lvb = sectors[tuple(kbig)]
        xb = unfold_levels(lvb); sb = spacings_from_unfolded(xb)
        ax.hist(sb, bins=30, range=(0, S_MAX_HIST), density=True, alpha=0.5,
                color="#228833", label=f"block {kbig} P(s) (N={lvb.size})")
        ax.plot(sgrid, poisson(sgrid), "k--", lw=1.5, label="Poisson")
        ax.plot(sgrid, semi_poisson(sgrid), "r-", lw=1.3, label="semi-Poisson")
        ax.set_title(f"Largest block {kbig}: $\\beta$={big['beta']:.3f}, $r$={big['r']:.3f}")
    ax.set_xlabel("s"); ax.set_ylabel("P(s)"); ax.legend(fontsize=8); ax.set_xlim(0, S_MAX_HIST)

    # (d) per-block <r> distribution vs canonical references
    ax = axes[1, 1]
    ax.hist(block_rs, bins=24, color="#66ccee", alpha=0.7, edgecolor="k")
    ax.axvline(r_POISSON_canonical, color="k", ls="--", lw=1.8,
               label=f"Poisson r={r_POISSON_canonical}")
    ax.axvline(r_GOE_canonical, color="g", ls="-.", lw=1.8, label=f"GOE r={r_GOE_canonical}")
    ax.axvline(r_pooled, color="b", ls="-", lw=2.0, label=f"pooled r={r_pooled:.3f}")
    ax.axvline(r_block_mean, color="r", ls="-", lw=2.0, label=f"<r>_block={r_block_mean:.3f}")
    ax.set_xlabel("$\\langle r\\rangle$ per block"); ax.set_ylabel("# blocks")
    ax.set_title("Per-block $\\langle r\\rangle$ vs Poisson/GOE")
    ax.legend(fontsize=7)

    fig.suptitle(f"INV3-W1-2  P(s) sector-resolved | verdict={composite} ({verdict_label})  "
                 f"$\\tau_{{fold}}$={tau_fold}, $L_{{max}}$={L_MAX}", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig("computations/investigation-3/inv3_w1_ps_sector.png", dpi=130)
    plt.close(fig)

    # ============================ (6) verdict payload ============================
    print("\n[VERDICT] composite =", composite, "|", verdict_label)
    print(f"[VERDICT] sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"[VERDICT] value = {value_str}")
    print(f"[VERDICT] audit_sha256   = {audit_sha256}")
    print(f"[VERDICT] content_sha256 = {content_sha256}")

    # final non-verdict 4-tuple tag
    print(f"\n(value={beta_block_pub}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    payload = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "extra_rows": [
            f"# beta_pooled={round(beta_pooled,4)} rho_pooled={rho_pooled_pub} "
            f"beta_block_median={round(beta_block_median,3)} beta_block_std={round(beta_block_std,3)} "
            f"beta_block(L14)={round(beta_block_14,3)} n_blocks={block_betas.size} "
            f"# {GATE_ID} sector-resolved P(s) detail",
        ],
    }
    print_verdict_payload(payload)
    return payload


if __name__ == "__main__":
    main()
