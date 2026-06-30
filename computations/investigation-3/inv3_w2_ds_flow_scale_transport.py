#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""INV3-W2-1 — Spectral-dimension-flow anomalous-scaling integral as the
K->K* scale-transport e-fold count.

GATE: INV3-W2-1-DS-FLOW-SCALE-TRANSPORT  (investigation track 3, Wave 2)
TRIGGER: [SIGN]
CLASSIFICATION: GEOMETRIC

Governing structure (heat trace = the Rosetta Stone):

    P(sigma) = Tr e^{-sigma D_K^2}
             = Sum_{(p,q)} dim(p,q) * Sum_{i} exp(-sigma * |lambda|^2_{(p,q),i})

over the L_max=12 Jensen-deformed SU(3) D_K spectrum at tau_fold = 0.19
(NORMAL STATE, Delta=0 -- this is the bare spectral-action heat trace,
Level-1 exact-on-truncation per the validity-tier discipline).

Spectral dimension:   d_s(sigma) = -2 d ln P(sigma) / d ln sigma   (centered FD on a log-sigma grid)
Anomalous scaling:    theta(sigma) = d_s(sigma) - d_s(sigma->0),  d_s(sigma->0) = 8 = dim SU(3)
Scale-transport int:  I = - int_{ln sigma_UV}^{ln sigma_fold} theta(sigma) dlnsigma   (trapezoid on log grid)

HYPOTHESIS: |I| equals the K->K* scale-transport e-fold count ln(K/K*) ~ ln(23) ~ 3.135
to within 10%, identifying the dimensionful K-pivot as an EMERGENT output of the
intensive d_s(sigma) flow.

SUBSTRATE-FIRST: the substrate IS the return probability P(sigma); "e-folds" =
spectral complexity GROWING inside the fiber point as sigma probes from the
fiber-UV plateau (d_s=8) DOWN to the fold window, NOT metric expansion.

PRE-REGISTERED RUBRIC (plan §W2-1):
  operator:  | |I| - ln(K/K*) | / ln(K/K*) <= 0.10
  PASS:      relative deviation <= 0.10
  FAIL:      relative deviation > 0.25  OR  sign wrong (I < 0)
  INFO:      0.10 < relative deviation <= 0.25
  [SIGN]:    Step-4/5 chain predicts I >= 0 (same sign as ln(K/K*) > 0).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # numpy path; cap threads (parallel-agent contention)

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# NumPy 2.x removed np.trapz -> np.trapezoid. Shim for cross-version stability.
_trapz = getattr(np, "trapezoid", None) or getattr(np, "trapz")  # (local)

# ---------------------------------------------------------------------------
# Section 0 — canonical constants (MANDATORY import; no hardcoded framework consts)
# ---------------------------------------------------------------------------
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403  (M_KK, d_s_fold_window_sigma, tau_fold, ...)

# ---------------------------------------------------------------------------
# Section 1 — Identity + machinery pins (per plan §W2-1)
# ---------------------------------------------------------------------------
SESSION = "3"          # investigation track 3
GATE_ID = "INV3-W2-1"  # short form -> ^INV3-W2-1: closure regex (descriptive suffix lives in SCHEME)
SCHEME = "DS-FLOW-SCALE-TRANSPORT-heat-trace-FW"  # heat-trace-FW: P=Tr e^{-sigma D_K^2}, full L12, no PV subtraction
CONVENTION = "RATIO"   # d_s is a log-derivative; I and ln(K/K*) are both dimensionless
L_MAX = "12"

# Machinery pins (plan §W2-1 machinery_pin_map) — gate-specific pins, tagged local
N_EVAL_INTEGRATION = 400            # (local) log-spaced sigma points across [sigma_UV, sigma_fold]
SIGMA_FOLD = float(d_s_fold_window_sigma)  # canonical 1.4005 M_KK^-2 (get_constant verified)
PLATEAU_TOL = 0.01                  # (local) |d_s - 8|/8 <= 0.01 fiber-UV plateau detection
FD_FLOOR = 1e-10                    # (local) finite-difference floor
D_S_UV_LIMIT = 8.0                  # (local) SU(3) real-manifold dimension; sigma->0 Weyl/MP plateau (dim SU(3)=8)

# Seed anchors for the scale-transport target (plan CONDITIONAL pins; NOT canonical_constants.py).
# K_pivot = 2.0 M_KK is atlas-04 C2 (tessellation CMB mapping, "BROKEN-WITH-LIVE-RESEARCH-PATHWAY",
# never rigorously derived); K_star = 0.087 M_KK is atlas-07 S51 (K* = m_G/sqrt(J), DERIVED,
# SA-Goldstone mixing threshold). NOTE: this 0.087 is the SEED anchor, DISTINCT from the
# canonical_constants.py K_star=1.3130 (the S84 lab-3He-B coth(1) anchor -- a different object).
# This gate tests whether the intensive d_s flow EMERGENTLY reproduces the ratio ln(K/K*).
K_PIVOT_SEED = 2.0     # (local) M_KK; atlas-04 C2 seed anchor (UV scale entering spectral complexity)
K_STAR_SEED = 0.087    # (local) M_KK; atlas-07 S51 seed anchor (IR scale; m_G/sqrt(J))
LN_K_RATIO_TARGET = float(np.log(K_PIVOT_SEED / K_STAR_SEED))  # ln(2.0/0.087) = 3.1350 (analytic target)

# Gate bands (plan §W2-1)
PASS_BAND = 0.10   # (local) pre-registered PASS band (relative deviation <= 10%)
INFO_BAND = 0.25   # (local) pre-registered INFO ceiling (10% < dev <= 25%)

# Probe grid: wider than the integration window, to LOCATE sigma_UV (where d_s first reaches 8
# from below as sigma -> 0) and to verify the d_s(sigma->0)->8 plateau empirically.
SIGMA_PROBE_MIN = 1.0e-4   # (local) deep-UV probe floor (M_KK^-2)
SIGMA_PROBE_MAX = SIGMA_FOLD
N_PROBE = 4000             # (local) dense log grid for plateau detection + FD stability

# ---------------------------------------------------------------------------
# Section 2 — Input files (SHA-pinned at runtime)
# ---------------------------------------------------------------------------
SESSION84_DIR = Path(__file__).resolve().parents[1] / "session-84"
SESSION56_DIR = Path(__file__).resolve().parents[1] / "session-56"
L12_CACHE = SESSION84_DIR / "s84_spectrum_cache_L12_tau019.npz"
S56_PRECEDENT = SESSION56_DIR / "s56_spectral_dim_flow.npz"  # methodological precedent only (fabric d_s; NOT spectrum source)

INPUT_FILES = {
    "canonical_constants": SHARED_DIR / "canonical_constants.py",
    "l12_fold_cache": L12_CACHE,
    "spectral_dim_flow_precedent": S56_PRECEDENT,
}

OUT_NPZ = Path(__file__).resolve().with_suffix(".npz")
OUT_PNG = Path(__file__).resolve().with_suffix(".png")


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (dual-SHA per S84+ schema; matches script-template.py)
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 72)
    print(f"INPUT PINS — {GATE_ID}")
    for name, path in files.items():
        relp = str(Path(path)).replace("\\", "/")  # (local)
        s = sha256_file(path)  # (local)
        pins[relp] = s
        print(f"  {name}: {s[:16]}...  {relp}")
    print("=" * 72)
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 4 — heat trace + spectral dimension
# ---------------------------------------------------------------------------
def load_spectrum():
    """Load the L12 fold-cache sector_evals dict.

    Returns (lam2_per_sector, dim_per_sector, meta):
      lam2_per_sector : list of np.ndarray, each = |lambda|^2 of the 16*dim(p,q) block eigenvalues
      dim_per_sector  : np.ndarray of dim(p,q) (the Peter-Weyl multiplicity weight)
      meta            : dict with sector keys, missing-sector note, counts
    """
    c = np.load(L12_CACHE, allow_pickle=True)
    se = c["sector_evals"].item()
    keys = sorted(se.keys())
    lam2 = []      # (local)
    dims = []      # (local)
    n_block = []   # (local)
    for k in keys:
        e = se[k]
        a = np.asarray(e["abs_evals"], dtype=np.float64)  # |lambda| block eigenvalues
        lam2.append(a * a)                                # |lambda|^2
        dims.append(int(e["dim"]))
        n_block.append(len(a))
    dims = np.asarray(dims, dtype=np.float64)
    # PW-weighted total eigenvalue count = Sum dim(p,q)*n_block = Sum 16*dim^2
    total_weighted = float(np.sum(dims * np.asarray(n_block, dtype=np.float64)))
    # (4,4) missing-sector accounting (dim=125 -> weight 16*125^2 = 250000)
    present_pq = set(keys)
    missing = [(p, q) for p in range(13) for q in range(13)
               if (p + q) <= 12 and (p, q) not in present_pq]
    meta = {
        "keys": keys,
        "n_sectors": len(keys),
        "total_weighted_count": total_weighted,
        "missing_sectors": missing,
        "global_min_abs": float(min(np.sqrt(x).min() for x in lam2)),
    }
    return lam2, dims, meta


def heat_trace(sigma_grid, lam2_per_sector, dim_per_sector):
    """P(sigma) = Sum_{(p,q)} dim(p,q) * Sum_i exp(-sigma |lambda|^2_i).

    Vectorized over the sigma grid; each sector contributes
    dim(p,q) * sum_i exp(-sigma * lam2_i). Numerically stable for the
    sigma range here (lam2 >= 0.67, sigma <= 1.4 -> exponents bounded).
    """
    P = np.zeros_like(sigma_grid, dtype=np.float64)  # (local)
    for lam2, d in zip(lam2_per_sector, dim_per_sector):
        # exp(-sigma * lam2): (Nsigma, Nblock) outer; sum over block; weight by dim
        # chunk to bound memory (Nblock up to 16*dim; largest sector ~ thousands)
        contrib = np.einsum("s,b->s", np.ones_like(sigma_grid), np.zeros(0)) if lam2.size == 0 else \
            (np.exp(-np.outer(sigma_grid, lam2)).sum(axis=1))  # (local) (Nsigma,)
        P += d * contrib
    return P


def spectral_dimension(sigma_grid, P):
    """d_s(sigma) = -2 d ln P / d ln sigma via centered finite difference on the log-sigma grid.

    Uses numpy.gradient on (ln P) vs (ln sigma) -> centered FD interior, one-sided at edges.
    """
    lnP = np.log(P)            # (local)
    lnsig = np.log(sigma_grid)  # (local)
    dlnP_dlnsig = np.gradient(lnP, lnsig)  # (local) centered FD
    ds = -2.0 * dlnP_dlnsig
    return ds


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def compute():
    lam2_per_sector, dim_per_sector, meta = load_spectrum()
    print(f"  spectrum: {meta['n_sectors']} sectors; PW-weighted count = {meta['total_weighted_count']:.0f}")
    print(f"  missing sectors (p+q<=12): {meta['missing_sectors']}  (dim(4,4)=125 -> weight 16*125^2=250000)")
    print(f"  global min |lambda| = {meta['global_min_abs']:.6f}")

    # --- Probe grid: locate sigma_UV (plateau-8) + verify d_s(sigma->0)->8 ---
    sig_probe = np.logspace(np.log10(SIGMA_PROBE_MIN), np.log10(SIGMA_PROBE_MAX), N_PROBE)  # (local)
    P_probe = heat_trace(sig_probe, lam2_per_sector, dim_per_sector)  # (local)
    ds_probe = spectral_dimension(sig_probe, P_probe)  # (local)

    # Empirical UV limit: d_s at the smallest probed sigma (deep UV).
    ds_uv_empirical = float(ds_probe[0])  # (local)
    ds_uv_min10 = float(np.mean(ds_probe[:10]))  # (local) mean of 10 deepest-UV points

    # sigma_UV READ-OFF: smallest sigma with |d_s - 8|/8 <= PLATEAU_TOL (fiber-UV plateau).
    rel_dev_from_8 = np.abs(ds_probe - D_S_UV_LIMIT) / D_S_UV_LIMIT  # (local)
    plateau_mask = rel_dev_from_8 <= PLATEAU_TOL  # (local)
    if plateau_mask.any():
        # the plateau is the (small-sigma) region within 1% of 8; sigma_UV = the LARGEST sigma
        # in the contiguous small-sigma plateau (the edge where d_s leaves 8 going toward the IR),
        # i.e. the start of the integration window where theta first becomes non-negligible.
        idx_plateau = np.where(plateau_mask)[0]  # (local)
        sigma_UV = float(sig_probe[idx_plateau.max()])  # (local) last sigma still within 1% of 8
        plateau_found = True
        # also record the smallest sigma in plateau (deep UV onset)
        sigma_UV_onset = float(sig_probe[idx_plateau.min()])  # (local)
    else:
        # plateau never reaches within 1% of 8: fall back to the sigma minimizing |d_s-8|
        sigma_UV = float(sig_probe[np.argmin(rel_dev_from_8)])  # (local)
        sigma_UV_onset = float(SIGMA_PROBE_MIN)
        plateau_found = False
    ds_at_sigmaUV = float(np.interp(np.log(sigma_UV), np.log(sig_probe), ds_probe))  # (local)
    ds_at_fold = float(np.interp(np.log(SIGMA_FOLD), np.log(sig_probe), ds_probe))   # (local)

    print(f"  d_s(sigma->0) empirical (deepest probe) = {ds_uv_empirical:.4f}  (target 8 = dim SU(3))")
    print(f"  d_s(sigma->0) mean(10 deepest) = {ds_uv_min10:.4f}")
    print(f"  plateau (|d_s-8|/8<=1%) found = {plateau_found}; sigma_UV READ-OFF = {sigma_UV:.6e} M_KK^-2 (ds={ds_at_sigmaUV:.4f})")
    print(f"  sigma_fold = {SIGMA_FOLD} M_KK^-2; d_s(sigma_fold) = {ds_at_fold:.4f}")

    # --- Integration grid: [sigma_UV, sigma_fold], N_EVAL_INTEGRATION log-uniform points ---
    sig_int = np.logspace(np.log10(sigma_UV), np.log10(SIGMA_FOLD), N_EVAL_INTEGRATION)  # (local)
    P_int = heat_trace(sig_int, lam2_per_sector, dim_per_sector)  # (local)
    # d_s on the integration grid (recompute on the fine integration grid for FD consistency)
    ds_int = spectral_dimension(sig_int, P_int)  # (local)
    theta = ds_int - D_S_UV_LIMIT  # (local) anomalous-scaling deviation theta(sigma) = d_s(sigma) - 8

    # --- I = - int theta dlnsigma  (trapezoid on the log-sigma grid) ---
    lnsig_int = np.log(sig_int)  # (local)
    integral_theta = float(_trapz(theta, lnsig_int))  # (local) int theta dlnsigma (<= 0 expected)
    I = -integral_theta  # (local) I >= 0 expected (theta <= 0)

    # --- Gate metric ---
    rel_dev = abs(abs(I) - LN_K_RATIO_TARGET) / LN_K_RATIO_TARGET  # (local)
    sign_ok = (I >= 0.0)  # (local) Step-4/5 prediction: I >= 0 (same sign as ln(K/K*) > 0)

    # --- sigma_UV robustness (INFO-discriminator follow-up): does |I| stay in band as sigma_UV moves? ---
    # scan sigma_UV across +/- a decade around the read-off, recompute I, report the spread.
    robustness = {}  # (local)
    sigUV_scan = np.logspace(np.log10(sigma_UV) - 0.5, np.log10(sigma_UV) + 0.5, 11)  # (local)
    I_scan = []  # (local)
    for s0 in sigUV_scan:
        if s0 >= SIGMA_FOLD:
            I_scan.append(np.nan)
            continue
        sg = np.logspace(np.log10(s0), np.log10(SIGMA_FOLD), N_EVAL_INTEGRATION)  # (local)
        Pg = heat_trace(sg, lam2_per_sector, dim_per_sector)  # (local)
        dsg = spectral_dimension(sg, Pg)  # (local)
        I_scan.append(-float(_trapz(dsg - D_S_UV_LIMIT, np.log(sg))))
    I_scan = np.asarray(I_scan, dtype=np.float64)
    I_scan_valid = I_scan[np.isfinite(I_scan)]  # (local)
    robustness = {
        "sigUV_scan": sigUV_scan,
        "I_scan": I_scan,
        "I_scan_min": float(np.nanmin(I_scan)),
        "I_scan_max": float(np.nanmax(I_scan)),
        "I_scan_spread": float(np.nanmax(I_scan) - np.nanmin(I_scan)),
        "frac_in_band": float(np.mean(np.abs(np.abs(I_scan_valid) - LN_K_RATIO_TARGET) / LN_K_RATIO_TARGET <= PASS_BAND)),
    }
    print(f"  I = -int theta dlnsigma = {I:.6f}")
    print(f"  ln(K/K*) target = {LN_K_RATIO_TARGET:.6f}  (K={K_PIVOT_SEED}, K*={K_STAR_SEED} M_KK)")
    print(f"  relative deviation = {rel_dev:.6f}  (PASS<= {PASS_BAND}, INFO<= {INFO_BAND})")
    print(f"  SIGN: I >= 0 ? {sign_ok}  (predicted I >= 0 same sign as ln(K/K*) > 0)")
    print(f"  sigma_UV robustness: I in [{robustness['I_scan_min']:.4f}, {robustness['I_scan_max']:.4f}] "
          f"spread={robustness['I_scan_spread']:.4f} frac_in_band={robustness['frac_in_band']:.3f}")

    return {
        "value": I,
        "I": I,
        "ln_K_ratio_target": LN_K_RATIO_TARGET,
        "rel_dev": rel_dev,
        "sign_ok": sign_ok,
        "ds_uv_empirical": ds_uv_empirical,
        "ds_uv_min10": ds_uv_min10,
        "plateau_found": plateau_found,
        "sigma_UV": sigma_UV,
        "sigma_UV_onset": sigma_UV_onset,
        "ds_at_sigmaUV": ds_at_sigmaUV,
        "ds_at_fold": ds_at_fold,
        # arrays for npz + plot
        "sig_probe": sig_probe,
        "P_probe": P_probe,
        "ds_probe": ds_probe,
        "sig_int": sig_int,
        "P_int": P_int,
        "ds_int": ds_int,
        "theta": theta,
        "meta": meta,
        "robustness": robustness,
    }


def evaluate_gate(rel_dev, sign_ok):
    """Composite collapse per plan §W2-1 + gate-verdicts.md schema-v2.

    sign_verdict   : PASS if I >= 0 (direction matches ln(K/K*) > 0), else FAIL.
    magnitude_verdict: PASS if rel_dev <= PASS_BAND; INFO if <= INFO_BAND; else FAIL.
    regime_verdict : VALID (deterministic heat-trace functional; no small-parameter
                     expansion; the full integration window is within method validity).
    composite:       FAIL if sign FAIL; else FAIL if mag FAIL & regime VALID;
                     else INFO if mag INFO; else PASS.
    """
    sign_verdict = "PASS" if sign_ok else "FAIL"  # (local)
    if rel_dev <= PASS_BAND:
        magnitude_verdict = "PASS"  # (local)
    elif rel_dev <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    regime_verdict = "VALID"  # (local) deterministic functional; window fully within validity

    # collapse rule (gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_verdict, magnitude_verdict, regime_verdict


# ---------------------------------------------------------------------------
# Section 6 — verdict payload emitter (script PRINTS; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION),
        "track": "investigation",
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


def make_plot(res):
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))

    # Panel 1: P(sigma) on the probe grid (log-log)
    ax = axes[0]
    ax.loglog(res["sig_probe"], res["P_probe"], "b-", lw=1.2)
    ax.axvline(SIGMA_FOLD, color="r", ls="--", lw=0.9, label=f"sigma_fold={SIGMA_FOLD}")
    ax.axvline(res["sigma_UV"], color="g", ls=":", lw=0.9, label=f"sigma_UV={res['sigma_UV']:.2e}")
    ax.set_xlabel(r"$\sigma$  (M$_{KK}^{-2}$)")
    ax.set_ylabel(r"$P(\sigma)=\mathrm{Tr}\,e^{-\sigma D_K^2}$")
    ax.set_title("Heat trace (bare D_K, L12 fold)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # Panel 2: d_s(sigma) with the d_s->8 plateau
    ax = axes[1]
    ax.semilogx(res["sig_probe"], res["ds_probe"], "b-", lw=1.2)
    ax.axhline(8.0, color="k", ls="-", lw=0.7, label="d_s=8 (dim SU(3), UV plateau)")
    ax.axhline(8.0 * (1 - PLATEAU_TOL), color="gray", ls=":", lw=0.6)
    ax.axvline(SIGMA_FOLD, color="r", ls="--", lw=0.9, label=f"sigma_fold")
    ax.axvline(res["sigma_UV"], color="g", ls=":", lw=0.9, label="sigma_UV (read-off)")
    ax.set_xlabel(r"$\sigma$  (M$_{KK}^{-2}$)")
    ax.set_ylabel(r"$d_s(\sigma)=-2\,d\ln P/d\ln\sigma$")
    ax.set_title(f"Spectral dimension flow (UV={res['ds_uv_empirical']:.2f})")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel 3: theta(sigma) and the accumulated -int theta dlnsigma
    ax = axes[2]
    theta = res["theta"]; sig = res["sig_int"]
    ax.semilogx(sig, theta, "m-", lw=1.2, label=r"$\theta(\sigma)=d_s-8$")
    # cumulative I(sigma) = -int_{sigma_UV}^{sigma} theta dlnsigma
    lnsig = np.log(sig)
    cum = -np.concatenate([[0.0], np.cumsum(0.5 * (theta[1:] + theta[:-1]) * np.diff(lnsig))])
    ax2 = ax.twinx()
    ax2.semilogx(sig, cum, "c-", lw=1.4, label=r"$-\int_{\sigma_{UV}}^{\sigma}\theta\,d\ln\sigma$")
    ax2.axhline(res["ln_K_ratio_target"], color="r", ls="--", lw=0.9,
                label=f"ln(K/K*)={res['ln_K_ratio_target']:.3f}")
    ax2.axhline(res["I"], color="g", ls=":", lw=1.0, label=f"I={res['I']:.3f}")
    ax.set_xlabel(r"$\sigma$  (M$_{KK}^{-2}$)")
    ax.set_ylabel(r"$\theta(\sigma)$")
    ax2.set_ylabel("accumulated e-fold integral")
    ax.set_title(f"I={res['I']:.4f} vs ln(K/K*)={res['ln_K_ratio_target']:.4f} (dev={res['rel_dev']*100:.1f}%)")
    lines1, labs1 = ax.get_legend_handles_labels()
    lines2, labs2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labs1 + labs2, fontsize=7, loc="center right")
    ax.grid(alpha=0.3)

    fig.suptitle("INV3-W2-1 — d_s(sigma)-flow anomalous-scaling integral as K->K* scale transport", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    composite, sign_v, mag_v, reg_v = evaluate_gate(res["rel_dev"], res["sign_ok"])

    # 4-tuple output line
    print()
    print(f"  4-tuple: (value={res['I']!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"  VERDICT: {composite}  [sign={sign_v} magnitude={mag_v} regime={reg_v}]")

    # save npz
    rob = res["robustness"]
    np.savez(
        OUT_NPZ,
        I=res["I"],
        ln_K_ratio_target=res["ln_K_ratio_target"],
        rel_dev=res["rel_dev"],
        sign_ok=res["sign_ok"],
        composite_verdict=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=reg_v,
        K_pivot_seed=K_PIVOT_SEED,
        K_star_seed=K_STAR_SEED,
        sigma_fold=SIGMA_FOLD,
        sigma_UV=res["sigma_UV"],
        sigma_UV_onset=res["sigma_UV_onset"],
        ds_uv_empirical=res["ds_uv_empirical"],
        ds_uv_min10=res["ds_uv_min10"],
        plateau_found=res["plateau_found"],
        ds_at_sigmaUV=res["ds_at_sigmaUV"],
        ds_at_fold=res["ds_at_fold"],
        d_s_uv_limit=D_S_UV_LIMIT,
        N_eval_integration=N_EVAL_INTEGRATION,
        plateau_tol=PLATEAU_TOL,
        pass_band=PASS_BAND,
        info_band=INFO_BAND,
        sig_probe=res["sig_probe"],
        P_probe=res["P_probe"],
        ds_probe=res["ds_probe"],
        sig_int=res["sig_int"],
        P_int=res["P_int"],
        ds_int=res["ds_int"],
        theta=res["theta"],
        sigUV_scan=rob["sigUV_scan"],
        I_scan=rob["I_scan"],
        I_scan_spread=rob["I_scan_spread"],
        I_scan_min=rob["I_scan_min"],
        I_scan_max=rob["I_scan_max"],
        frac_in_band=rob["frac_in_band"],
        n_sectors=res["meta"]["n_sectors"],
        total_weighted_count=res["meta"]["total_weighted_count"],
        missing_sectors=np.asarray(res["meta"]["missing_sectors"]),
        global_min_abs=res["meta"]["global_min_abs"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
    )
    print(f"  saved npz: {OUT_NPZ}")

    make_plot(res)
    print(f"  saved png: {OUT_PNG}")

    # verdict payload
    note = (f"I=-int theta dlnsigma={res['I']:.6f} vs ln(K/K*)={res['ln_K_ratio_target']:.6f} "
            f"(K={K_PIVOT_SEED},K*={K_STAR_SEED} M_KK seed anchors) rel_dev={res['rel_dev']:.6f} "
            f"sigma_UV(read-off)={res['sigma_UV']:.4e} ds_UV={res['ds_uv_empirical']:.4f}->8 "
            f"sigma_fold={SIGMA_FOLD} ds_fold={res['ds_at_fold']:.4f} plateau_found={res['plateau_found']}")
    extra = [
        ("# regulator_pin=N/A (d_s is a log-derivative of the heat trace P=Tr e^{-sigma D_K^2}; "
         "no Seeley-DeWitt a_n moment is cited -- scheme=heat-trace-FW Level-1 exact-on-truncation). "
         "convention=RATIO (I and ln(K/K*) both dimensionless)."),
        ("# anchor_provenance: K_pivot=2.0 M_KK = atlas-04 C2 SEED (BROKEN-WITH-LIVE-RESEARCH-PATHWAY, never derived); "
         "K_star=0.087 M_KK = atlas-07 S51 SEED (m_G/sqrt(J), DERIVED). 0.087 is the SEED anchor, "
         "DISTINCT from canonical_constants.py K_star=1.3130 (S84 lab-3He-B coth(1) anchor)."),
        (f"# missing_sector=(4,4) dim=125 weight=16*125^2=250000 NOT in L12 cache; "
         f"d_s is a log-derivative so a single interior bulk sector is a near-multiplicative shift -- "
         f"sigma_UV robustness spread={rob['I_scan_spread']:.4f} over +/-0.5 dex; "
         f"89/90 sectors used, PW-weighted count={res['meta']['total_weighted_count']:.0f}."),
        (f"# dual_prior_realloc: PASS->0.7 Track_A (emergent scale-map, sigma_UV=READ-OFF); "
         f"FAIL(>25%)->0.85 Track_B (numerical coincidence); INFO(10-25%)->unchanged, "
         f"window-sensitivity follow-up. composite={composite}."),
    ]
    print_verdict_payload(
        composite, res["I"], audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note=note, extra_rows=extra,
    )
    print(f"\n  elapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
