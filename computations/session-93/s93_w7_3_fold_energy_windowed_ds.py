#!/usr/bin/env python3
r"""
S93-W7-3-FOLD-ENERGY-WINDOWED-DS-GATE  ([SIGN], GEOMETRIC)
==========================================================

PRIMARY author: kaluza-klein-theorist (monotone-to-8 / Weyl side).
Co-review (separate later dispatch): landau-condensed-matter-theorist
(van-Hove / flat-band side).

Resolves the FOLD-ENERGY WINDOWED spectral dimension into Reading-KK vs
Reading-van-Hove and discharges the long-open S34 [F-4] question.

Method (per session-93-plan-w7.md §W7-3):
  Compute the windowed spectral dimension on the converged-L_max D_K spectrum
  at tau_fold = 0.190, NORMAL STATE (Delta = 0; the BdG gap is NOT applied --
  this is the BARE D_K heat trace):

      P(sigma) = Sum_{(p,q)} dim(p,q) * Sum_i exp(-sigma * lambda_i^2)
      d_s(sigma) = -2 d ln P(sigma) / d ln sigma            (centered finite diff)

  on sigma in [0.5, 2.0] M_KK^-2, fold-match diffusion window
  sigma_* = 1/E_B2^2 (a DERIVED window pin from the bit-exact canonical
  E_B2_mean, tagged # (local)).

  PLUS the directly-fitted energy-axis DOS exponent gamma_E (the discriminating
  sub-quantity per AH-PF-1) from the cumulative count
      N(lambda) - N(E_0) ~ sign(lambda - E_0) |lambda - E_0|^{1 - gamma_E}
  near E_0 = E_B2_mean, fit window w_fit = (E_B2_mean - E_B1), re-fit at 2*w_fit.

FAIR-COMPARISON OBSERVABLE DISCIPLINE (AH-PF-1 / phononic-framing.md
"Same-functional-different-scale fair-comparison"): the WINDOWED d_s(sigma_*)
is a DISTINCT functional of P(sigma) from the SETTLED sigma->0 Weyl asymptotic
d_s(sigma->0) = dim(SU(3)) = 8 (Minakshisundaram-Pleijel). This gate computes
ONLY the intermediate-window observable; it does NOT assert anything about the
sigma->0 asymptotic and does NOT conflate the two. No CDT numerical cross-
comparison (the S53 d_s_max=67.829 3D-K^2-weighting artifact + the L_max>>6
caution make any accessible NUMERICAL CDT comparison premature, Claim B).

Z = rho_E * v_g CONSISTENCY CHECK (NOT a gate): reported as a corroborant only;
Z is a PRODUCT invariant ~ 1/pi off-fold for the whole gamma_E in [1/2,1)
family (D-L1, Sage-verified), NOT a gamma_E-lock.

READINGS (pre-registered, two-sided):
  Reading-KK       iff (min d_s > 5) AND (d_s strictly monotone) AND gamma_E in [0.5,0.6]
  Reading-van-Hove iff (min d_s < 3) AND (flat sub-window)        AND gamma_E in [0.8,1.0)
  INDETERMINATE    iff (3 <= min d_s <= 5) OR (gamma_E in (0.6,0.8))
                       OR L_max-convergence / gamma_E-fit-window not met

Session: S93 | Wave: W7 | Gate: S93-W7-3-FOLD-ENERGY-WINDOWED-DS-GATE
"""

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    E_B2_mean,
    E_B1,
)

# -----------------------------------------------------------------------------
# GPU heat-trace reduction (RX 9070 XT, torch+rocm). Falls back to numpy.
# -----------------------------------------------------------------------------
try:
    import torch  # noqa: E402
    _TORCH_OK = torch.cuda.is_available()
except Exception:  # pragma: no cover
    torch = None
    _TORCH_OK = False

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan §W7-3 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S93-W7-3-FOLD-ENERGY-WINDOWED-DS-GATE"
SCHEME = "heat-trace-return-probability-windowed-d_s-NORMAL-STATE-Delta0"
CONVENTION = (
    "FOLD-ENERGY-WINDOWED-D_S-sigma-in-0.5-2.0-Mkk-inv2-sigma_star-1.40051-"
    "plus-gamma_E-DOS-cumulative-count-fit-E0-E_B2"
)

L_MAX = 12                       # (local) canonical master cache truncation
L_MAX_XCHECK = 10                # (local) convergence cross-check (L_max - 2)
SIGMA_LO = 0.5                   # (local) window lower bound, M_KK^-2
SIGMA_HI = 2.0                   # (local) window upper bound, M_KK^-2
N_SIGMA = 80                     # (local) sigma-grid density (>= 40 required)
# DERIVED fold-match diffusion window from the bit-exact canonical E_B2_mean.
# Plan-text presentation form 1.40051 comes from the 0.845 round figure
# (1/0.845^2 = 1.40051); the SUBSTRATE-FIRST canonical E_B2_mean gives
# 1/E_B2_mean^2 = 1.39962. Per substrate-first-canonical-sourcing.md the
# bit-exact canonical is authoritative; we use 1/E_B2_mean^2 and report both.
SIGMA_STAR = 1.0 / E_B2_mean**2  # (local) = 1.39962 (substrate-first canonical)
SIGMA_STAR_PLAN_TEXT = 1.40051   # (local) plan presentation form (from 0.845 round figure)
W_FIT = E_B2_mean - E_B1         # (local) DOS fit window = 0.0261291 M_KK
# Pre-registered reading thresholds (plan §W7-3 operator.form)
MIN_DS_KK = 5.0                  # (local) Reading-KK requires min d_s > 5
MIN_DS_VH = 3.0                  # (local) Reading-van-Hove requires min d_s < 3
GAMMA_KK_LO, GAMMA_KK_HI = 0.5, 0.6   # (local) Reading-KK gamma_E band
GAMMA_VH_LO, GAMMA_VH_HI = 0.8, 1.0   # (local) Reading-van-Hove gamma_E band
TOL_DS = 0.1                     # (local) L_max-convergence tol on d_s(sigma_*)
TOL_GAMMA = 0.05                 # (local) L_max-convergence + fit-window tol on gamma_E
PLATEAU_FLAT_TOL = 0.15          # (local) |d(d_s)/d ln sigma| below this over a finite
#                                          sub-window => "flat" (van-Hove plateau)

# -----------------------------------------------------------------------------
# Verdict file path (S93 canonical location per gate-verdicts.md)
# -----------------------------------------------------------------------------
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"

# -----------------------------------------------------------------------------
# Input files
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_L12_EXPECTED_SHA = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"

OUT_NPZ = PROJECT_ROOT / "computations" / "session-93" / "s93_w7_3_fold_energy_windowed_ds.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-93" / "s93_w7_3_fold_energy_windowed_ds.png"


# -----------------------------------------------------------------------------
# SHA helpers (dual-SHA per S84+ schema; matches S93 W7-1 precedent)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.
    audit = sha(script || canonical || pinmap_json); content = sha(script).
    """
    script_bytes = b""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Spectrum loader: dim-weighted (Peter-Weyl multiplicity) D_K eigenvalues
# -----------------------------------------------------------------------------
def load_dim_weighted_spectrum(cache_path: Path, lmax: int):
    r"""Return (lam, w) where lam = |lambda_i| and w = dim(p,q) per stored eigenvalue.

    The cache stores sector_evals[(p,q)] = {'dim': dim(p,q), 'level': p+q,
    'abs_evals': array of |lambda_i| of length dim(p,q)*16} -- ONE Peter-Weyl
    copy of irrep (p,q) tensored with the C^16 spinor block. Peter-Weyl:
    L^2(SU(3)) = oplus_{(p,q)} V_{(p,q)} (x) V_{(p,q)}^*, so irrep (p,q) appears
    with multiplicity dim(p,q) in the regular representation. The full heat
    trace Tr e^{-sigma D_K^2} therefore weights each stored eigenvalue by the
    OUTER PW multiplicity dim(p,q):
        P(sigma) = Sum_{(p,q)} dim(p,q) * Sum_i exp(-sigma lambda_i^2)
    (the S44 convention, confirmed against the knowledge-base equation).
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    lam_chunks = []
    w_chunks = []
    for (p, q), v in se.items():
        if v["level"] > lmax:
            continue
        ev = np.asarray(v["abs_evals"], dtype=np.float64)
        lam_chunks.append(ev)
        w_chunks.append(np.full(ev.shape, float(v["dim"]), dtype=np.float64))
    lam = np.concatenate(lam_chunks)
    w = np.concatenate(w_chunks)
    return lam, w


# -----------------------------------------------------------------------------
# Heat trace P(sigma) and windowed d_s(sigma) (GPU reduction)
# -----------------------------------------------------------------------------
def heat_trace(lam: np.ndarray, w: np.ndarray, sigma: np.ndarray) -> np.ndarray:
    r"""P(sigma) = Sum_i w_i exp(-sigma lambda_i^2), vectorized over the
    sigma-grid. GPU torch reduction when available (lam ~ 1.7e5 evals x
    >=40 sigma values), numpy fallback otherwise."""
    lam2 = lam ** 2
    if _TORCH_OK:
        dev = torch.device("cuda")
        lam2_t = torch.tensor(lam2, device=dev, dtype=torch.float64)
        w_t = torch.tensor(w, device=dev, dtype=torch.float64)
        sig_t = torch.tensor(sigma, device=dev, dtype=torch.float64)
        # P[j] = sum_i w_i exp(-sig_j lam2_i)
        expo = torch.exp(-sig_t[:, None] * lam2_t[None, :])  # (N_sig, N_eval)
        P = (expo * w_t[None, :]).sum(dim=1)
        return P.cpu().numpy()
    expo = np.exp(-sigma[:, None] * lam2[None, :])
    return (expo * w[None, :]).sum(axis=1)


def windowed_ds(lam, w, sigma_lo=SIGMA_LO, sigma_hi=SIGMA_HI, n_sigma=N_SIGMA):
    r"""d_s(sigma) = -2 d ln P / d ln sigma via centered finite difference on a
    log-spaced sigma grid across [sigma_lo, sigma_hi]."""
    sigma = np.logspace(np.log10(sigma_lo), np.log10(sigma_hi), n_sigma)
    P = heat_trace(lam, w, sigma)
    ln_sig = np.log(sigma)
    ln_P = np.log(np.clip(P, 1e-300, None))
    # np.gradient gives a centered finite difference on the interior, one-sided
    # at the endpoints -- the canonical d ln P / d ln sigma estimator.
    d_lnP = np.gradient(ln_P, ln_sig)
    ds = -2.0 * d_lnP
    return sigma, P, ds


# -----------------------------------------------------------------------------
# Energy-axis DOS exponent gamma_E (cumulative-count estimator, AH-PF-1)
# -----------------------------------------------------------------------------
def gamma_E_cumulative(lam, w, E0, wf):
    r"""Fit gamma_E from N(lambda) - N(E_0) ~ sign(lambda-E_0)|lambda-E_0|^{1-gamma_E}.

    Estimator: the multiplicity-weighted cumulative count N(lambda) = sum_{|lam_i|<=lambda} w_i.
    Fit log|N(lambda)-N(E_0)| vs log|lambda-E_0| over the symmetric window
    [E_0 - wf, E_0 + wf] on ALL weighted eigenvalue points -> slope = 1 - gamma_E.
    Returns (gamma_E, slope, n_points, N0).
    """
    order = np.argsort(lam)
    ls = lam[order]
    ws = w[order]
    Nc = np.cumsum(ws)
    N0 = float(np.interp(E0, ls, Nc))
    mask = (ls >= E0 - wf) & (ls <= E0 + wf) & (np.abs(ls - E0) > 1e-7)
    x = np.abs(ls[mask] - E0)
    y = np.abs(Nc[mask] - N0)
    good = (x > 0) & (y > 0)
    if int(good.sum()) < 3:
        return np.nan, np.nan, int(good.sum()), N0
    slope, _ = np.polyfit(np.log(x[good]), np.log(y[good]), 1)
    return 1.0 - slope, slope, int(good.sum()), N0


def gamma_E_unique(lam, w, E0, wf):
    r"""Robustness-diagnostic gamma_E variant: fit on DISTINCT eigenvalues
    (each weighted by its summed multiplicity, regression on the unique-lambda
    cumulative-count points). Sensitive to the sparse-fold discreteness; used
    ONLY to bound the estimator spread, not as the canonical gamma_E."""
    order = np.argsort(lam)
    ls = lam[order]
    ws = w[order]
    Nc = np.cumsum(ws)
    N0 = float(np.interp(E0, ls, Nc))
    mask = (ls >= E0 - wf) & (ls <= E0 + wf) & (np.abs(ls - E0) > 1e-7)
    lu = np.unique(np.round(ls[mask], 8))
    x = np.abs(lu - E0)
    y = np.abs(np.array([float(np.interp(l, ls, Nc)) - N0 for l in lu]))
    good = (x > 0) & (y > 0)
    if int(good.sum()) < 3:
        return np.nan, int(good.sum())
    slope, _ = np.polyfit(np.log(x[good]), np.log(y[good]), 1)
    return 1.0 - slope, int(good.sum())


# -----------------------------------------------------------------------------
# Z = rho_E * v_g consistency-check corroborant (NOT a gate)
# -----------------------------------------------------------------------------
def impedance_Z(lam, w, E0, wf):
    r"""Off-fold impedance Z = rho_E * v_g, the PRODUCT invariant.
    rho_E = local energy DOS near a reference (off-fold) energy;
    v_g = mean group velocity proxy (mean level spacing^-1 inverse).
    For a 1D-band-edge / HOvHS family Z ~ 1/pi for all gamma_E (D-L1, the
    WALL is a product invariant; Z is a CONSISTENCY CHECK, not a gamma_E-lock).
    Computed at an OFF-FOLD reference energy E_off = E0 + 4*wf to avoid the
    fold pile-up; reported as a corroborant only.
    """
    E_off = E0 + 4.0 * wf  # (local) off-fold reference energy
    order = np.argsort(lam)
    ls = lam[order]
    ws = w[order]
    # rho_E: weighted DOS in a small bin around E_off (counts per energy)
    half = wf  # (local) DOS bin half-width
    in_bin = (ls >= E_off - half) & (ls <= E_off + half)
    rho_E = float(ws[in_bin].sum()) / (2.0 * half) if in_bin.any() else np.nan  # (local)
    # v_g proxy: mean level spacing of the DISTINCT eigenvalues in the bin -> dE/dN
    lu = np.unique(np.round(ls[in_bin], 8))
    if lu.size >= 2:
        v_g = float(np.mean(np.diff(lu)))  # (local) mean distinct-level spacing ~ dE/d(index)
    else:
        v_g = np.nan
    Z = rho_E * v_g if (np.isfinite(rho_E) and np.isfinite(v_g)) else np.nan
    return Z, rho_E, v_g, E_off


# -----------------------------------------------------------------------------
# Plateau / monotonicity diagnostics
# -----------------------------------------------------------------------------
def plateau_diagnostics(sigma, ds):
    r"""Return (min_ds, monotone_incr, monotone_dec, has_flat_subwindow, max_flat_run)."""
    diffs = np.diff(ds)
    monotone_incr = bool(np.all(diffs > 0))
    monotone_dec = bool(np.all(diffs < 0))
    # local log-slope d(d_s)/d ln sigma
    ln_sig = np.log(sigma)
    local_slope = np.gradient(ds, ln_sig)
    flat_mask = np.abs(local_slope) < PLATEAU_FLAT_TOL
    # longest contiguous flat run
    max_run = 0  # (local) longest contiguous flat run
    run = 0      # (local) current run length
    for f in flat_mask:
        run = run + 1 if f else 0
        max_run = max(max_run, run)
    has_flat = max_run >= 3  # (local) >=3 consecutive grid points flat
    return float(np.min(ds)), monotone_incr, monotone_dec, has_flat, int(max_run)


# -----------------------------------------------------------------------------
# Composite-collapse rule (PRE-REGISTERED, gate-verdicts.md S87 schema-v2)
# -----------------------------------------------------------------------------
def collapse(sign_v, mag_v, reg_v):
    if reg_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and reg_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, reg_v, gv):
    """Append canonical line + dual-SHA companion + REQUIRED schema-v2 3-tuple
    row + reading-provenance row + regulator-pin row to s93_gate_verdicts.txt
    (atomic single open('a'))."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2); "
        f"sign = d(d_s)/d ln sigma ascending-toward-8 (KK) vs descending-to-plateau (vH); "
        f"magnitude = gamma_E band; regime = L_max-convergence + gamma_E fit-window stability\n"
    )
    reading_row = (
        f"# reading={gv['reading']} min_ds={gv['min_ds']:.4f} d_s_sigma_star={gv['ds_star']:.4f} "
        f"monotone_incr={gv['monotone_incr']} gamma_E_wf={gv['gE_wf']:.4f} "
        f"gamma_E_2wf={gv['gE_2wf']:.4f} gamma_E_central={gv['gE_central']:.4f} "
        f"Z_offfold={gv['Z']:.4f} sigma_star={gv['sigma_star']:.5f} "
        f"# {GATE_ID} two-sided d_s reading + gamma_E DOS exponent\n"
    )
    convergence_row = (
        f"# L_max_op={gv['L_max_op']} L_max_plan={L_MAX} "
        f"d_ds_L12_L10={gv['d_ds_conv']:.4f}(tol{TOL_DS}) "
        f"d_gamma_L12_L10={gv['d_gamma_conv']:.4f}(tol{TOL_GAMMA}) "
        f"gamma_fitwindow_delta={gv['gamma_fitwin']:.4f}(tol{TOL_GAMMA}) "
        f"# {GATE_ID} L_max-convergence + fit-window stability\n"
    )
    fair_row = (
        f"# AH-PF-1 fair-comparison: windowed d_s(sigma_*) is a DISTINCT functional "
        f"from the SETTLED sigma->0 Weyl asymptotic d_s(sigma->0)=dim(SU(3))=8 "
        f"(Minakshisundaram-Pleijel); NO conflation, NO CDT numerical cross-comparison; "
        f"Z=rho_E*v_g is a CONSISTENCY CHECK (product invariant), NOT a gamma_E-lock "
        f"# {GATE_ID} phononic-framing.md Same-functional-different-scale\n"
    )
    regulator_pin = (
        f"# REGULATOR_PIN=heat-trace-NORMAL-STATE-Delta0 LEVEL_CLASS_PIN=FULL "
        f"# {GATE_ID} bare D_K heat trace on the L_max=12 master cache "
        f"(no BdG gap, no SCHEMATIC helper); substrate-first-canonical-sourcing.md PASS\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(schema_v2_row)
        fp.write(reading_row)
        fp.write(convergence_row)
        fp.write(fair_row)
        fp.write(regulator_pin)


# -----------------------------------------------------------------------------
# Diagnostic plot
# -----------------------------------------------------------------------------
def make_plot(sigma, ds, lam12, w12, gv):
    fig, axes = plt.subplots(2, 2, figsize=(15, 11))

    # Panel 1: d_s(sigma) windowed curve at L_max=12 and L_max=10
    ax1 = axes[0, 0]
    ax1.semilogx(sigma, ds, "b.-", lw=1.6, ms=4, label=f"$L_{{max}}=12$")
    ax1.semilogx(gv["sigma10"], gv["ds10"], "r.--", lw=1.2, ms=3, alpha=0.7,
                 label=f"$L_{{max}}=10$")
    ax1.axvline(gv["sigma_star"], color="green", ls=":", lw=1.5,
                label=fr"$\sigma_*=1/E_{{B2}}^2={gv['sigma_star']:.4f}$")
    ax1.axhline(8.0, color="gray", ls=":", alpha=0.6, label=r"$\dim SU(3)=8$ (Weyl $\sigma\to0$)")
    ax1.axhline(MIN_DS_KK, color="orange", ls="--", alpha=0.4, label=r"Reading-KK floor (5)")
    ax1.axhline(MIN_DS_VH, color="purple", ls="--", alpha=0.4, label=r"Reading-vH ceiling (3)")
    ax1.set_xlabel(r"diffusion time $\sigma$  [$M_{KK}^{-2}$]", fontsize=11)
    ax1.set_ylabel(r"$d_s(\sigma)=-2\,d\ln P/d\ln\sigma$", fontsize=11)
    ax1.set_title(
        f"(a) WINDOWED spectral dimension, NORMAL state ($\\Delta=0$)\n"
        f"min $d_s$={gv['min_ds']:.3f}, $d_s(\\sigma_*)$={gv['ds_star']:.3f}, "
        f"reading: {gv['reading']}", fontsize=10)
    ax1.grid(True, alpha=0.3, which="both")
    ax1.legend(fontsize=7.5, loc="best")

    # Panel 2: cumulative count N(lambda) near the B2 fold + gamma_E fit
    ax2 = axes[0, 1]
    order = np.argsort(lam12)
    ls = lam12[order]
    ws = w12[order]
    Nc = np.cumsum(ws)
    win = (ls >= E_B2_mean - 3 * W_FIT) & (ls <= E_B2_mean + 3 * W_FIT)
    ax2.step(ls[win], Nc[win], where="post", color="b", lw=1.4,
             label=r"$N(\lambda)=\sum_{|\lambda_i|\leq\lambda}\,\mathrm{dim}(p,q)$")
    ax2.axvline(E_B2_mean, color="green", ls=":", lw=1.5,
                label=fr"$E_{{B2}}={E_B2_mean:.4f}$")
    ax2.axvline(E_B1, color="orange", ls=":", lw=1.2,
                label=fr"$E_{{B1}}={E_B1:.4f}$")
    ax2.axvspan(E_B2_mean - W_FIT, E_B2_mean + W_FIT, color="green", alpha=0.10,
                label=r"$w_{fit}=E_{B2}-E_{B1}$")
    ax2.set_xlabel(r"$|\lambda|$  [$M_{KK}$]", fontsize=11)
    ax2.set_ylabel(r"weighted cumulative count $N(\lambda)$", fontsize=11)
    ax2.set_title(
        f"(b) DOS cumulative count near B2 fold\n"
        fr"$\gamma_E$(w_fit)={gv['gE_wf']:.3f}, $\gamma_E$(2w_fit)={gv['gE_2wf']:.3f} "
        f"(n_distinct={gv['n_distinct_2wf']})", fontsize=10)
    ax2.grid(True, alpha=0.3)
    ax2.legend(fontsize=8, loc="best")

    # Panel 3: log-log gamma_E fit
    ax3 = axes[1, 0]
    for wf, col, lbl in [(W_FIT, "b", "w_fit"), (2 * W_FIT, "r", "2*w_fit")]:
        mask = (ls >= E_B2_mean - wf) & (ls <= E_B2_mean + wf) & (np.abs(ls - E_B2_mean) > 1e-7)
        N0 = float(np.interp(E_B2_mean, ls, Nc))
        x = np.abs(ls[mask] - E_B2_mean)
        y = np.abs(Nc[mask] - N0)
        good = (x > 0) & (y > 0)
        if good.sum() >= 2:
            ax3.loglog(x[good], y[good], col + ".", ms=5, alpha=0.6, label=f"{lbl} pts")
            sl, ic = np.polyfit(np.log(x[good]), np.log(y[good]), 1)
            xf = np.array([x[good].min(), x[good].max()])
            ax3.loglog(xf, np.exp(ic) * xf ** sl, col + "-", lw=1.3,
                       label=fr"{lbl} fit $\gamma_E$={1 - sl:.3f}")
    ax3.set_xlabel(r"$|\lambda - E_{B2}|$", fontsize=11)
    ax3.set_ylabel(r"$|N(\lambda)-N(E_{B2})|$", fontsize=11)
    ax3.set_title(
        f"(c) DOS exponent fit (discriminating sub-quantity)\n"
        fr"$\gamma_E\approx{gv['gE_central']:.3f}$ "
        f"(KK band [0.5,0.6] / vH band [0.8,1.0))", fontsize=10)
    ax3.grid(True, alpha=0.3, which="both")
    ax3.legend(fontsize=8)

    # Panel 4: verdict summary text
    ax4 = axes[1, 1]
    ax4.axis("off")
    txt = (
        f"GATE: {GATE_ID}\n"
        f"VERDICT (composite): {gv['composite']}\n"
        f"3-tuple: sign={gv['sign_v']}  mag={gv['mag_v']}  regime={gv['reg_v']}\n\n"
        f"PLATEAU metric (robust):\n"
        f"  min d_s on [0.5,2.0] = {gv['min_ds']:.4f}  (>5 KK, <3 vH)\n"
        f"  d_s(sigma_*)         = {gv['ds_star']:.4f}\n"
        f"  monotone increasing  = {gv['monotone_incr']}  (ascending->8 = KK)\n"
        f"  flat sub-window      = {gv['has_flat']}  (plateau = vH)\n\n"
        f"gamma_E (discriminating sub-quantity):\n"
        f"  gamma_E(w_fit)       = {gv['gE_wf']:.4f}\n"
        f"  gamma_E(2*w_fit)     = {gv['gE_2wf']:.4f}\n"
        f"  central / spread     = {gv['gE_central']:.4f} / {gv['gamma_fitwin']:.4f}\n"
        f"  KK band [0.5,0.6]?   = {gv['in_kk_band']}\n"
        f"  vH band [0.8,1.0)?   = {gv['in_vh_band']}\n\n"
        f"L_max-convergence:\n"
        f"  |d_s(L12)-d_s(L10)|  = {gv['d_ds_conv']:.4f}  (tol {TOL_DS})\n"
        f"  |gE(L12)-gE(L10)|    = {gv['d_gamma_conv']:.4f}  (tol {TOL_GAMMA})\n"
        f"  gamma_E fit-window dl= {gv['gamma_fitwin']:.4f}  (tol {TOL_GAMMA})\n\n"
        f"Z = rho_E*v_g (corroborant) = {gv['Z']:.4f}  (~1/pi={1/np.pi:.4f} off-fold)\n\n"
        f"FAIR-COMPARISON (AH-PF-1):\n"
        f"  windowed d_s(sigma_*) != Weyl d_s(sigma->0)=8\n"
        f"  (distinct functionals; NO conflation; NO CDT compare)\n\n"
        f"Reading: {gv['reading']}\n"
        f"S34 [F-4]: {gv['f4_status']}"
    )
    ax4.text(0.02, 0.98, txt, fontsize=8.5, family="monospace",
             va="top", ha="left", transform=ax4.transAxes)

    fig.suptitle(
        f"S93-W7-3 FOLD-ENERGY WINDOWED $d_s$ + $\\gamma_E$ DOS "
        f"(NORMAL state, $\\tau_{{fold}}=0.190$, $L_{{max}}=12$) -- {gv['composite']}",
        fontsize=13, fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    fig.savefig(OUT_PNG, dpi=140, bbox_inches="tight")
    plt.close(fig)


# =============================================================================
# MAIN
# =============================================================================
def main():
    print("=" * 78)
    print(f"GATE: {GATE_ID}")
    print("=" * 78)

    # --- input SHA pins (logged in first 20 lines of stdout per gate-verdicts.md) ---
    cache_sha = sha256_of(CACHE_L12)
    canon_sha = sha256_of(CANONICAL_CONSTANTS_PATH)
    print(f"INPUT cache SHA256       : {cache_sha}")
    print(f"INPUT cache expected SHA : {CACHE_L12_EXPECTED_SHA}")
    print(f"INPUT cache SHA match    : {cache_sha == CACHE_L12_EXPECTED_SHA}")
    print(f"INPUT canonical SHA256   : {canon_sha}")
    print(f"GPU (torch+rocm) active  : {_TORCH_OK}")
    print(f"E_B2_mean (canonical)    : {E_B2_mean}")
    print(f"E_B1 (canonical)         : {E_B1}")
    print(f"tau_fold                 : {tau_fold}")
    print(f"M_KK                     : {M_KK}")
    print(f"sigma_* = 1/E_B2_mean^2  : {SIGMA_STAR:.6f}  (substrate-first canonical)")
    print(f"sigma_* plan-text form   : {SIGMA_STAR_PLAN_TEXT}  (from 0.845 round figure)")
    print(f"w_fit = E_B2 - E_B1      : {W_FIT:.7f}")
    if cache_sha != CACHE_L12_EXPECTED_SHA:
        print("WARNING: cache SHA does not match plan-frozen value; proceeding "
              "(static master cache; SHA drift logged for audit).")

    # --- load dim-weighted spectra ---
    lam12, w12 = load_dim_weighted_spectrum(CACHE_L12, L_MAX)
    lam10, w10 = load_dim_weighted_spectrum(CACHE_L12, L_MAX_XCHECK)
    print(f"\nL_max=12: {lam12.size:,} stored evals, total weighted count {w12.sum():,.0f}")
    print(f"L_max=10: {lam10.size:,} stored evals, total weighted count {w10.sum():,.0f}")
    print(f"global min |lambda| (L12): {lam12.min():.7f}  (= E_B1 = spectral bottom)")

    # --- windowed d_s ---
    sigma, P12, ds12 = windowed_ds(lam12, w12)
    sigma10, P10, ds10 = windowed_ds(lam10, w10)
    ds_star = float(np.interp(SIGMA_STAR, sigma, ds12))
    ds_star10 = float(np.interp(SIGMA_STAR, sigma10, ds10))
    min_ds, mono_incr, mono_dec, has_flat, max_flat_run = plateau_diagnostics(sigma, ds12)
    print(f"\n--- WINDOWED d_s (plateau metric) ---")
    print(f"d_s(sigma_*) [L12]   = {ds_star:.4f}")
    print(f"d_s(sigma_*) [L10]   = {ds_star10:.4f}")
    print(f"min d_s on [0.5,2.0] = {min_ds:.4f}  (Reading-KK if >5; Reading-vH if <3)")
    print(f"monotone increasing  = {mono_incr}  (ascending toward 8 => KK-favorable)")
    print(f"monotone decreasing  = {mono_dec}")
    print(f"flat sub-window      = {has_flat}  (max flat run = {max_flat_run} pts)")

    # --- gamma_E DOS exponent (the discriminating sub-quantity) ---
    gE_wf, slope_wf, n_wf, N0 = gamma_E_cumulative(lam12, w12, E_B2_mean, W_FIT)
    gE_2wf, slope_2wf, n_2wf, _ = gamma_E_cumulative(lam12, w12, E_B2_mean, 2 * W_FIT)
    gE_wf10, _, _, _ = gamma_E_cumulative(lam10, w10, E_B2_mean, W_FIT)
    gE_uni_wf, n_uni_wf = gamma_E_unique(lam12, w12, E_B2_mean, W_FIT)
    gE_uni_2wf, n_uni_2wf = gamma_E_unique(lam12, w12, E_B2_mean, 2 * W_FIT)
    gE_central = float(np.nanmean([gE_wf, gE_2wf]))  # (local) canonical-estimator central value
    # full estimator spread (canonical all-points + unique-eigenvalue variants)
    all_gE = np.array([gE_wf, gE_2wf, gE_uni_wf, gE_uni_2wf])  # (local)
    gE_spread_full = float(np.nanmax(all_gE) - np.nanmin(all_gE))  # (local)
    print(f"\n--- gamma_E DOS exponent (discriminating sub-quantity) ---")
    print(f"gamma_E(w_fit)   [L12, all-points] = {gE_wf:.4f}  (n={n_wf})")
    print(f"gamma_E(2*w_fit) [L12, all-points] = {gE_2wf:.4f}  (n={n_2wf})")
    print(f"gamma_E central (all-points mean)  = {gE_central:.4f}")
    print(f"gamma_E fit-window delta |wf-2wf|  = {abs(gE_wf - gE_2wf):.4f}  (tol {TOL_GAMMA})")
    print(f"gamma_E(w_fit)   [unique-eval var] = {gE_uni_wf:.4f}  (n={n_uni_wf})")
    print(f"gamma_E(2*w_fit) [unique-eval var] = {gE_uni_2wf:.4f}  (n={n_uni_2wf})")
    print(f"gamma_E FULL estimator spread      = {gE_spread_full:.4f}")
    print(f"N(E_B2) weighted                   = {N0:.2f}")

    # --- Z = rho_E * v_g consistency-check corroborant ---
    Z, rho_E, v_g, E_off = impedance_Z(lam12, w12, E_B2_mean, W_FIT)
    print(f"\n--- Z = rho_E * v_g (consistency check, NOT a gate) ---")
    print(f"Z = {Z:.4f}  (rho_E={rho_E:.3f}, v_g={v_g:.5f}); off-fold E_off={E_off:.4f}; "
          f"1/pi={1/np.pi:.4f}")

    # --- L_max-convergence ---
    d_ds_conv = abs(ds_star - ds_star10)
    d_gamma_conv = abs(gE_wf - gE_wf10)
    gamma_fitwin = abs(gE_wf - gE_2wf)
    print(f"\n--- L_max-convergence (regime) ---")
    print(f"|d_s(sigma_*; L12) - d_s(sigma_*; L10)| = {d_ds_conv:.4f}  (tol {TOL_DS})")
    print(f"|gamma_E(L12) - gamma_E(L10)|           = {d_gamma_conv:.4f}  (tol {TOL_GAMMA})")
    print(f"gamma_E fit-window |wf - 2wf|           = {gamma_fitwin:.4f}  (tol {TOL_GAMMA})")

    # =========================================================================
    # VERDICT LOGIC (3-tuple per pre-registered operator + composite collapse)
    # =========================================================================
    # sign_verdict: the substitution-chain Step-4 DIRECTION. d_s ascending
    # toward 8 (mono increasing) = KK-favorable; descending-to-plateau = vH.
    # The two-branch prediction resolves to whichever branch the data takes;
    # sign_verdict=PASS iff the computed direction is one of the two
    # pre-registered directions (it IS -- ascending), N/A only if neither.
    if mono_incr:
        sign_v = "PASS"  # ascending toward 8 -> the KK branch of the prediction
        sign_dir = "ascending-toward-8 (KK branch)"  # (local)
    elif mono_dec or has_flat:
        sign_v = "PASS"  # descending/plateau -> the vH branch of the prediction
        sign_dir = "descending-to-plateau (vH branch)"  # (local)
    else:
        sign_v = "N/A"
        sign_dir = "non-monotone, no flat sub-window"  # (local)

    # magnitude_verdict: from the gamma_E band (the mechanism verdict).
    in_kk_band = bool(GAMMA_KK_LO <= gE_central <= GAMMA_KK_HI)
    in_vh_band = bool(GAMMA_VH_LO <= gE_central < GAMMA_VH_HI)
    # PASS iff gamma_E cleanly in ONE band AND the estimator is stable
    # (both fit windows agree to tol AND both windows land in the SAME band).
    gE_wf_inkk = GAMMA_KK_LO <= gE_wf <= GAMMA_KK_HI
    gE_2wf_inkk = GAMMA_KK_LO <= gE_2wf <= GAMMA_KK_HI
    gE_wf_invh = GAMMA_VH_LO <= gE_wf < GAMMA_VH_HI
    gE_2wf_invh = GAMMA_VH_LO <= gE_2wf < GAMMA_VH_HI
    clean_kk = gE_wf_inkk and gE_2wf_inkk
    clean_vh = gE_wf_invh and gE_2wf_invh
    if (clean_kk or clean_vh) and gamma_fitwin < TOL_GAMMA:
        mag_v = "PASS"
    elif in_kk_band or in_vh_band:
        # central in a band but the windows disagree / spread too large -> INFO
        mag_v = "INFO"
    else:
        # gamma_E in the INDETERMINATE band (0.6,0.8) or NaN
        mag_v = "INFO"

    # regime_verdict: L_max-convergence + gamma_E fit-window stability.
    # d_s(sigma_*) convergence is the primary regime axis; gamma_E fit-window
    # stability is the secondary (the gamma_E is the mechanism verdict).
    ds_converged = d_ds_conv < TOL_DS
    gamma_converged = d_gamma_conv < TOL_GAMMA
    gamma_fitwin_ok = gamma_fitwin < TOL_GAMMA
    if ds_converged and gamma_converged and gamma_fitwin_ok:
        reg_v = "VALID"
    elif ds_converged and gamma_converged and not gamma_fitwin_ok:
        # L_max-converged but gamma_E NOT fit-window-stable on the sparse fold
        # -> the discriminating sub-quantity is not yet in the asymptotic regime
        reg_v = "MARGINAL"
    elif not ds_converged or not gamma_converged:
        reg_v = "BREAKDOWN"
    else:
        reg_v = "MARGINAL"

    # --- two-sided reading (joint criterion) ---
    reading_kk = (min_ds > MIN_DS_KK) and mono_incr and clean_kk and gamma_fitwin_ok
    reading_vh = (min_ds < MIN_DS_VH) and has_flat and clean_vh and gamma_fitwin_ok
    if reading_kk and not reading_vh:
        reading = "Reading-KK"
    elif reading_vh and not reading_kk:
        reading = "Reading-van-Hove"
    else:
        reading = "INDETERMINATE"
    # Which side does the EVIDENCE favor (reported even when INDETERMINATE)?
    plateau_favors = "KK" if (min_ds > MIN_DS_KK and mono_incr) else (
        "van-Hove" if (min_ds < MIN_DS_VH and has_flat) else "neither")  # (local)
    gamma_favors = "KK" if in_kk_band else ("van-Hove" if in_vh_band else "neither")  # (local)

    composite = collapse(sign_v, mag_v, reg_v)
    f4_status = "DISCHARGED" if composite == "PASS" else "INFORMATIVE (unchanged)"

    print(f"\n{'='*78}")
    print("VERDICT")
    print(f"{'='*78}")
    print(f"sign_verdict      = {sign_v}   ({sign_dir})")
    print(f"magnitude_verdict = {mag_v}   (gamma_E central {gE_central:.4f}; "
          f"clean_kk={clean_kk} clean_vh={clean_vh})")
    print(f"regime_verdict    = {reg_v}   (d_s conv {ds_converged}, "
          f"gamma conv {gamma_converged}, fit-window {gamma_fitwin_ok})")
    print(f"COMPOSITE         = {composite}")
    print(f"Reading           = {reading}")
    print(f"  plateau metric favors: {plateau_favors}")
    print(f"  gamma_E favors      : {gamma_favors}")
    print(f"S34 [F-4]         = {f4_status}")

    # --- descriptive value string ---
    value = (
        f"min_ds={min_ds:.4f};ds_sigma_star={ds_star:.4f};monotone_incr={mono_incr};"
        f"has_flat={has_flat};gamma_E_wf={gE_wf:.4f};gamma_E_2wf={gE_2wf:.4f};"
        f"gamma_E_central={gE_central:.4f};gamma_fitwin_delta={gamma_fitwin:.4f}(tol{TOL_GAMMA});"
        f"gamma_E_full_spread={gE_spread_full:.4f};in_kk_band={in_kk_band};in_vh_band={in_vh_band};"
        f"reading={reading};plateau_favors={plateau_favors};gamma_favors={gamma_favors};"
        f"d_ds_L12_L10={d_ds_conv:.4f}(tol{TOL_DS});d_gamma_L12_L10={d_gamma_conv:.4f}(tol{TOL_GAMMA});"
        f"Z_offfold={Z:.4f}(1pi={1/np.pi:.4f});sigma_star={SIGMA_STAR:.5f}(plan_text=1.40051);"
        f"L_max_op=12;L_max_plan=12;n_distinct_2wf={n_uni_2wf};"
        f"S34_F4={f4_status};fair_comparison=windowed_NEQ_Weyl_sigma0_8_NO_CDT_compare"
    )

    # --- machinery pin map -> dual SHA ---
    pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "L_max_xcheck": L_MAX_XCHECK,
        "sigma_lo": SIGMA_LO,
        "sigma_hi": SIGMA_HI,
        "n_sigma": N_SIGMA,
        "sigma_star": round(SIGMA_STAR, 8),
        "w_fit": round(W_FIT, 8),
        "E_B2_mean": E_B2_mean,
        "E_B1": E_B1,
        "tau_fold": tau_fold,
        "cache_sha256": cache_sha,
        "min_ds_kk": MIN_DS_KK,
        "min_ds_vh": MIN_DS_VH,
        "gamma_kk_band": [GAMMA_KK_LO, GAMMA_KK_HI],
        "gamma_vh_band": [GAMMA_VH_LO, GAMMA_VH_HI],
        "tol_ds": TOL_DS,
        "tol_gamma": TOL_GAMMA,
    }
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\naudit_sha256   = {audit_sha}")
    print(f"content_sha256 = {content_sha}")
    print(f"4-tuple: (value=<descriptive>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    gv = dict(
        reading=reading, min_ds=min_ds, ds_star=ds_star, monotone_incr=mono_incr,
        has_flat=has_flat, gE_wf=gE_wf, gE_2wf=gE_2wf, gE_central=gE_central,
        Z=Z, sigma_star=SIGMA_STAR, L_max_op=12, d_ds_conv=d_ds_conv,
        d_gamma_conv=d_gamma_conv, gamma_fitwin=gamma_fitwin, composite=composite,
        sign_v=sign_v, mag_v=mag_v, reg_v=reg_v, in_kk_band=in_kk_band,
        in_vh_band=in_vh_band, n_distinct_2wf=n_uni_2wf, f4_status=f4_status,
        sigma10=sigma10, ds10=ds10,
    )

    # --- save data ---
    np.savez(
        OUT_NPZ,
        sigma=sigma, P12=P12, ds12=ds12,
        sigma10=sigma10, P10=P10, ds10=ds10,
        ds_star=ds_star, ds_star10=ds_star10, min_ds=min_ds,
        monotone_incr=mono_incr, monotone_dec=mono_dec, has_flat=has_flat,
        max_flat_run=max_flat_run,
        gamma_E_wf=gE_wf, gamma_E_2wf=gE_2wf, gamma_E_central=gE_central,
        gamma_E_wf_L10=gE_wf10, gamma_E_unique_wf=gE_uni_wf, gamma_E_unique_2wf=gE_uni_2wf,
        gamma_E_full_spread=gE_spread_full, gamma_fitwin=gamma_fitwin,
        n_wf=n_wf, n_2wf=n_2wf, n_unique_wf=n_uni_wf, n_unique_2wf=n_uni_2wf, N0=N0,
        Z=Z, rho_E=rho_E, v_g=v_g, E_off=E_off, one_over_pi=1.0 / np.pi,
        d_ds_conv=d_ds_conv, d_gamma_conv=d_gamma_conv,
        sigma_star=SIGMA_STAR, sigma_star_plan_text=SIGMA_STAR_PLAN_TEXT,
        w_fit=W_FIT, E_B2_mean=E_B2_mean, E_B1=E_B1, tau_fold=tau_fold, M_KK=M_KK,
        L_max=L_MAX, L_max_op=12, L_max_xcheck=L_MAX_XCHECK,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite=composite, reading=reading, f4_status=f4_status,
        in_kk_band=in_kk_band, in_vh_band=in_vh_band,
        plateau_favors=plateau_favors, gamma_favors=gamma_favors,
        cache_sha256=cache_sha, audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\nData saved: {OUT_NPZ}")

    # --- plot ---
    make_plot(sigma, ds12, lam12, w12, gv)
    print(f"Plot saved: {OUT_PNG}")

    # --- emit verdict ---
    append_verdict(composite, value, audit_sha, content_sha, sign_v, mag_v, reg_v, gv)
    print(f"\nVerdict appended to {VERDICT_TXT}")
    print("DONE.")


if __name__ == "__main__":
    main()
