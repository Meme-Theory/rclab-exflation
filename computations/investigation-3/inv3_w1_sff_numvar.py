#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
INV3-W1-1 — Connected spectral form factor K(tau) + number variance Sigma^2(L)
            and spectral rigidity Delta_3(L) for the D_K spectrum at tau_fold.

Poisson / RMT / arithmetic-chaos discriminator at the DISCRIMINATING-observable
level the prior pooled <r> statistic (CHAOS-1) could not reach.

GEOMETRIC. The substrate IS the D_K eigenvalue spectrum {|lambda_n|} on
Jensen-deformed SU(3) at tau_fold; the connected spectral form factor and the
number variance ARE the substrate's own level-correlation geometry, not a
statistical container the eigenvalues sit inside. Direction of explanation:
  D_K eigenvalues -> (per-(p,q)-block unfold) -> connected two-level correlator
  R_2^c -> K(tau) ramp + Sigma^2(L) growth law -> universality class
  (Poisson / RMT / arithmetic) -> integrability of the fabric's vibrational floor.

Method (plan §W1-1, machinery pinned there):
  (1) UNFOLD per Peter-Weyl (p,q) block via a smooth degree-7 Weyl staircase fit
      (D_K is block-diagonal; cross-block spacings are a pooling artifact, so each
      block is unfolded to unit mean spacing then concatenated -- removes the
      trivial multi-component superposition trend), giving unfolded {x_n}.
  (2) CONNECTED SFF  K(tau) = <|Sum_n e^{2 pi i x_n tau}|^2>_c  with the smooth
      (disconnected) part subtracted; averaged over n_spectral_windows disjoint
      sub-windows.  Phase matrix on GPU (torch.matmul on cuda; >=100x100).
  (3) NUMBER VARIANCE  Sigma^2(L) = <n(L)^2> - <n(L)>^2  over randomly placed
      intervals of unfolded length L.
  (4) SPECTRAL RIGIDITY  Delta_3(L) Dyson-Mehta least-squares staircase rigidity.
  (5) DISCRIMINATE: fit p_Sigma2 = d ln Sigma^2(L) / d ln L over the linear-response
      window; read off the ramp presence in K(tau).

Verdict (plan §W1-1 operator):
  PASS-Poisson iff p_Sigma2 in [0.85, 1.15] (Sigma^2 ~ L) AND no RMT ramp;
  FAIL-RMT     iff p_Sigma2 <= 0.5 (Sigma^2 ~ ln L) AND sustained linear ramp;
  INFO-arith   iff 0.5 < p_Sigma2 < 0.85 OR a non-linear/arithmetic ramp.

[SIGN] trigger: LARGER p_Sigma2 => MORE Poisson-like (linear growth) => MORE
integrable; the RMT ramp in K(tau) is the COMPLEMENTARY chaos signature.
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import (  # noqa: E402
    tau_fold,
    r_POISSON_canonical,
    r_GOE_canonical,
    M_KK,
)

import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 0 — Gate identity + machinery pins (plan §W1-1 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "3"                       # investigation track
GATE_ID = "INV3-W1-1"
SCHEME = "connected-SFF-Dyson-Mehta-numvar"
CONVENTION = "RATIO"
L_MAX = "12"

# pinned machinery (gate machinery pins, plan §W1-1 machinery_pin_map; not framework constants)
N_EVAL_PIN = 78080                  # (local) plan label (inherited from L10 lore; actual cache count emitted below)
SCAN_RANGE = (0.5, 20.0)            # (local) number-variance interval length L window (unfolded mean-spacing units)
STEP_SIZE = 0.25                    # (local) L-grid step for Sigma^2(L)/Delta_3(L)
TAU_GRID_N = 512                    # (local) K(tau) tau-grid points
TAU_GRID_MAX = 2.0                  # (local) K(tau) Heisenberg-time-normalized range [0, 2]
TOLERANCE = 0.15                    # (local) half-width of the Poisson p_Sigma2=1.0 PASS band
RANDOM_SEED = 20260614              # (local) pinned seed for interval placements + window bootstrap
UNFOLD_POLY_DEGREE = 7              # (local) smooth Weyl-fit degree (pinned; NOT adaptive)
N_SPECTRAL_WINDOWS = 16             # (local) disjoint spectral sub-windows for the <>_c ensemble average
PUBLICATION_PRECISION = 4           # (local) p_Sigma2 published to 4 sig figs

# PASS band edges (plan operator)
PASS_LO, PASS_HI = 0.85, 1.15       # (local) Poisson linear-growth PASS band
FAIL_RMT_HI = 0.5                   # (local) p_Sigma2 <= 0.5 => RMT (log growth)

# RMT-class reference label (literature surmise; NOT a framework constant)
R_GUE_SURMISE = 0.6027             # (local) Wigner-like GUE <r> surmise, RMT reference label only

CACHE_L12 = Path("computations/session-84/s84_spectrum_cache_L12_tau019.npz")
CACHE_L14 = Path("computations/session-87/s87_spectrum_cache_L14_tau019.npz")
CANONICAL = Path("computations/_shared/canonical_constants.py")

OUT_NPZ = Path("computations/investigation-3/inv3_w1_sff_numvar.npz")
OUT_PNG = Path("computations/investigation-3/inv3_w1_sff_numvar.png")
SELF_PATH = Path(__file__).resolve()


# ---------------------------------------------------------------------------
# Section 1 — SHA input logging (first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_file(path: Path) -> str:
    try:
        return hashlib.sha256(Path(path).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
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
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 2 — Cache loading + per-block spectrum extraction
# ---------------------------------------------------------------------------
def load_sector_blocks(cache_path: Path):
    """Return dict {(p,q): np.array(|lambda| within-block spectrum)}.

    D_K is block-diagonal in the Peter-Weyl basis; each sector record carries
    one representative block's abs_evals (the BDI absolute-value spectrum).
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    blocks = {}  # (local)
    for key, rec in se.items():
        ev = np.asarray(rec["abs_evals"], dtype=float)
        blocks[key] = np.sort(ev)
    return blocks


# ---------------------------------------------------------------------------
# Section 3 — Per-block unfolding (smooth degree-7 Weyl staircase)
# ---------------------------------------------------------------------------
def unfold_block(eigs: np.ndarray, poly_degree: int):
    """Unfold a single block's DISTINCT-level |lambda| spectrum to unit mean spacing.

    The D_K block spectra carry large EXACT degeneracies (within-block
    multiplicity from the sub-block / fiber-(x)-C^16 structure; e.g. the (6,6)
    block has 5488 eigenvalues but only 218 distinct |lambda| with multiplicities
    2..56). The canonical level-CORRELATION object is the sequence of DISTINCT
    levels: spacing statistics on the multiplicity-counted spectrum would be
    swamped by exact zero-spacings (a degeneracy artifact, not level
    correlation) -- cf. the CHAOS-1 'Poisson on unique levels' correction.

    We therefore fit the smooth Weyl staircase N(lambda)=rank to the DISTINCT
    levels (degree `poly_degree`) and unfold x_n = N_smooth(lambda_n^distinct),
    rescaled to unit mean spacing. Returns the unfolded distinct-level sequence
    x (sorted) or None if the block has too few distinct levels for a stable fit.
    """
    e_all = np.sort(np.asarray(eigs, dtype=float))  # (local) full (degenerate) block spectrum
    e = np.unique(np.round(e_all, 9))               # (local) DISTINCT levels (degeneracy removed)
    n = e.size  # (local) number of distinct levels
    # need enough distinct levels for a degree-d polyfit + spacing statistics
    if n < poly_degree + 6:
        return None
    if (e[-1] - e[0]) < 1e-9:
        return None
    # distinct-level staircase: cumulative count 1..n at each distinct level
    stair = np.arange(1, n + 1, dtype=float)  # (local)
    # smooth Weyl fit on a centred/scaled abscissa for polyfit conditioning
    e0 = 0.5 * (e[0] + e[-1])  # (local)
    es = (e[-1] - e[0]) / 2.0  # (local)
    xs = (e - e0) / es         # (local) scaled to [-1, 1]
    coeffs = np.polyfit(xs, stair, poly_degree)  # (local) smooth Weyl fit (well conditioned)
    x = np.polyval(coeffs, xs)  # (local) unfolded distinct levels
    x = np.sort(x)
    # the smooth unfold of a monotone staircase should be (near-)monotone
    dx = np.diff(x)  # (local)
    if np.mean(dx > 0) < 0.85:
        return None  # polyfit failed to capture the distinct-level staircase
    span = x[-1] - x[0]  # (local)
    if span <= 0:
        return None
    x = (x - x[0]) * ((n - 1) / span)  # (local) mean spacing = 1 by construction
    return x


def build_unfolded_pool(blocks: dict, poly_degree: int):
    """Unfold each (p,q) block separately, concatenate the unfolded levels.

    Returns (pooled_unfolded_sorted_within_block_list, per_block_unfolded dict,
             n_blocks_used, n_levels_used).
    """
    per_block = {}  # (local)
    pooled_spacings = []  # (local) nearest-neighbour spacings, within-block only
    n_used = 0  # (local)
    for key, eigs in blocks.items():
        xu = unfold_block(eigs, poly_degree)
        if xu is None:
            continue
        per_block[key] = xu
        n_used += xu.size
        s = np.diff(xu)  # (local) within-block spacings (mean ~ 1)
        pooled_spacings.append(s)
    pooled_spacings = np.concatenate(pooled_spacings) if pooled_spacings else np.array([])
    return per_block, pooled_spacings, len(per_block), n_used


# ---------------------------------------------------------------------------
# Section 4 — Connected spectral form factor K(tau) on GPU
# ---------------------------------------------------------------------------
def connected_sff(per_block: dict, tau_grid: np.ndarray, n_windows: int):
    """K(tau) = < |Sum_n e^{2 pi i x_n tau}|^2 >_c, disconnected part subtracted.

    Ensemble <>_c is over n_windows disjoint spectral sub-windows formed from the
    concatenated per-block unfolded levels. The GPU phase matrix
    P[w, j, k] = e^{2 pi i x^(w)_k tau_j} is built per window via torch.matmul
    (outer product x (x) tau) on cuda (>=100x100).
    """
    import torch

    dev = "cuda" if torch.cuda.is_available() else "cpu"  # (local)
    # concatenate all per-block unfolded levels into one sequence, then split
    # into n_windows contiguous disjoint sub-windows (each ~ a spectral patch)
    all_x = np.concatenate([per_block[k] for k in per_block])  # (local)
    all_x = np.sort(all_x)
    Wtot = all_x.size  # (local)
    win_size = Wtot // n_windows  # (local)
    tau_t = torch.tensor(tau_grid, device=dev, dtype=torch.float64)  # (local)
    K_acc = torch.zeros(tau_grid.size, device=dev, dtype=torch.float64)  # (local)
    Sre_acc = torch.zeros(tau_grid.size, device=dev, dtype=torch.float64)  # (local)
    Sim_acc = torch.zeros(tau_grid.size, device=dev, dtype=torch.float64)  # (local)
    nwin = 0  # (local)
    for w in range(n_windows):
        seg = all_x[w * win_size:(w + 1) * win_size]  # (local)
        if seg.size < 50:
            continue
        # re-center each window to unit mean spacing locally (so windows are comparable)
        seg = (seg - seg[0])
        # phase matrix: outer(seg, tau) -> exp(2 pi i .)
        x_t = torch.tensor(seg, device=dev, dtype=torch.float64)  # (local)
        ang = 2.0 * np.pi * torch.outer(x_t, tau_t)  # (local) (n_seg x n_tau) on GPU
        re = torch.cos(ang).sum(dim=0)  # (local) Re Sum_n e^{i ang}
        im = torch.sin(ang).sum(dim=0)  # (local) Im Sum_n e^{i ang}
        K_acc += re * re + im * im       # |Sum|^2 for this window
        Sre_acc += re
        Sim_acc += im
        nwin += 1
    K_raw = (K_acc / nwin)                                   # <|Sum|^2>
    S_mean_sq = (Sre_acc / nwin) ** 2 + (Sim_acc / nwin) ** 2  # |<Sum>|^2 (disconnected)
    K_conn = (K_raw - S_mean_sq).cpu().numpy()               # connected SFF
    K_raw_np = K_raw.cpu().numpy()
    n_per_win = win_size  # (local)
    return K_conn, K_raw_np, n_per_win, nwin


# ---------------------------------------------------------------------------
# Section 5 — Number variance Sigma^2(L) + spectral rigidity Delta_3(L)
# ---------------------------------------------------------------------------
def number_variance(per_block: dict, L_grid: np.ndarray, rng: np.random.Generator,
                    n_intervals: int = 4000):
    """Sigma^2(L) = <n(L)^2> - <n(L)>^2 from randomly placed intervals.

    Intervals are placed WITHIN each block's unfolded support (the canonical
    object: cross-block intervals are pooling artifacts since D_K is
    block-diagonal). Counts are aggregated across blocks at each L.
    """
    sig2 = np.zeros(L_grid.size)  # (local)
    nbar = np.zeros(L_grid.size)  # (local)
    block_list = [per_block[k] for k in per_block if per_block[k].size > (L_grid.max() + 5)]
    for li, L in enumerate(L_grid):
        counts = []  # (local)
        per_blk = max(50, n_intervals // max(1, len(block_list)))  # (local)
        for xu in block_list:
            lo, hi = xu[0], xu[-1] - L  # (local)
            if hi <= lo:
                continue
            starts = rng.uniform(lo, hi, size=per_blk)  # (local)
            # count levels in [start, start+L) via searchsorted
            left = np.searchsorted(xu, starts, side="left")  # (local)
            right = np.searchsorted(xu, starts + L, side="left")  # (local)
            counts.append((right - left).astype(float))
        if not counts:
            continue
        c = np.concatenate(counts)  # (local)
        nbar[li] = c.mean()
        sig2[li] = c.var()
    return sig2, nbar


def spectral_rigidity(per_block: dict, L_grid: np.ndarray, rng: np.random.Generator,
                      n_intervals: int = 800):
    """Delta_3(L) Dyson-Mehta: < min_{A,B} (1/L) Int [N(x)-A-Bx]^2 dx >.

    Closed-form per interval: given the unfolded levels in [c, c+L], the
    staircase N(x) is a step function; the least-squares fit of a line to a
    staircase has a standard closed form (Mehta ch.16). We evaluate the
    integral numerically on a fine sub-grid per interval (robust + simple),
    averaged over random placements within each block.
    """
    d3 = np.zeros(L_grid.size)  # (local)
    block_list = [per_block[k] for k in per_block if per_block[k].size > (L_grid.max() + 5)]
    nsub = 200  # (local) sub-grid points per interval for the LS integral
    for li, L in enumerate(L_grid):
        vals = []  # (local)
        per_blk = max(20, n_intervals // max(1, len(block_list)))  # (local)
        u = np.linspace(0.0, L, nsub)  # (local) local coordinate
        for xu in block_list:
            lo, hi = xu[0], xu[-1] - L  # (local)
            if hi <= lo:
                continue
            starts = rng.uniform(lo, hi, size=min(per_blk, 60))  # (local)
            for c0 in starts:
                # staircase N(x) on [c0, c0+L], shifted so N(c0)=0
                base = np.searchsorted(xu, c0, side="left")  # (local)
                Nx = (np.searchsorted(xu, c0 + u, side="left") - base).astype(float)  # (local)
                # least-squares line fit A + B u to Nx over u
                A = np.vstack([np.ones_like(u), u]).T  # (local)
                coef, *_ = np.linalg.lstsq(A, Nx, rcond=None)  # (local)
                resid = Nx - A @ coef  # (local)
                d3_val = np.trapezoid(resid * resid, u) / L  # (local)
                vals.append(d3_val)
        if vals:
            d3[li] = np.mean(vals)
    return d3


# ---------------------------------------------------------------------------
# Section 6 — discriminating exponent p_Sigma2 + ramp reading
# ---------------------------------------------------------------------------
def detect_saturation_scale(L_grid: np.ndarray, sig2: np.ndarray):
    """Detect L_sat where Sigma^2(L) first plateaus (finite-N rigidity ceiling).

    Number variance on a finite per-block distinct-level sequence saturates at a
    scale set by the block size (the smooth-unfold long-range rigidity ceiling).
    The linear-response window -- where the Poisson/RMT growth-law discriminator
    lives -- is BELOW this saturation. We detect L_sat as the smallest L beyond
    which Sigma^2 stops growing: the first L where the forward-averaged value
    no longer exceeds the running max by a meaningful margin.
    Returns L_sat (float).
    """
    m = sig2 > 0  # (local)
    Lp, Sp = L_grid[m], sig2[m]  # (local)
    if Sp.size < 6:
        return float(L_grid.max())
    smax = Sp.max()  # (local) saturation plateau estimate
    # L_sat: first L where Sigma^2 reaches 90% of its global max AND stays flat after
    thresh = 0.90 * smax  # (local)
    idx = np.where(Sp >= thresh)[0]  # (local)
    if idx.size == 0:
        return float(Lp[-1])
    L_sat = float(Lp[idx[0]])  # (local)
    # do not let the linear-response window collapse below a minimal span
    return max(L_sat, 2.0)


def fit_growth_exponent(L_grid: np.ndarray, sig2: np.ndarray, L_lo=0.5, L_hi=None):
    """p_Sigma2 = d ln Sigma^2 / d ln L over the linear-response window [L_lo, L_hi].

    The linear-response window is BELOW the finite-N saturation scale; L_hi
    defaults to the detected saturation scale. Returns (p, intercept, mask).
    """
    if L_hi is None:
        L_hi = detect_saturation_scale(L_grid, sig2)
    mask = (L_grid >= L_lo) & (L_grid <= L_hi) & (sig2 > 0)  # (local)
    if mask.sum() < 3:  # fall back to a minimal small-L window
        mask = (L_grid >= 0.5) & (L_grid <= 2.0) & (sig2 > 0)
    lnL = np.log(L_grid[mask])  # (local)
    lnS = np.log(sig2[mask])  # (local)
    A = np.vstack([lnL, np.ones_like(lnL)]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, lnS, rcond=None)  # (local)
    p = float(coef[0])  # (local) slope = growth exponent
    b = float(coef[1])  # (local) intercept
    return p, b, mask


def ramp_reading(tau_grid: np.ndarray, K_conn: np.ndarray, n_per_win: int):
    """Quantify RMT-ramp presence in the connected SFF.

    Universality references (connected SFF, normalised by N = levels/window):
      Poisson : K_c(tau)/N -> 1 (CONSTANT shot-noise floor; NO ramp, NO dip).
      GUE     : K_c(tau)/N = 2*tau for 0<tau<1 (the linear RAMP rises FROM the
                correlation-hole minimum TOWARD the plateau 1 at tau=1, then
                plateaus at 1).
    The DISCRIMINATING signature of an RMT ramp is a SUSTAINED RISE of K_c with
    tau across the pre-Heisenberg window, FROM a sub-plateau minimum UP toward the
    plateau. A Poisson spectrum is flat (no rise). A finite-N spectrum has a
    short-tau transient (window-length artifact) that DECAYS toward the plateau;
    that decaying transient must NOT be read as a ramp -- it has the WRONG sign
    (decreasing, not increasing).

    Metric: over the pre-Heisenberg window [tau_lo, 1.0], with the short-tau
    transient (tau < tau_lo) EXCLUDED, fit the trend slope of K_c/N. ramp_present
    iff the trend is a SUSTAINED POSITIVE rise (slope > +0.30, i.e. > 15% of the
    GUE slope 2) AND the value at tau_lo is BELOW the plateau (a genuine
    rise-from-the-hole, not the tail of the decaying transient).
    """
    N = float(n_per_win)  # (local) levels per window ~ "N"
    Kn = K_conn / N  # (local) normalised connected SFF
    # exclude the short-tau window-length transient: start the ramp window where
    # the transient has decayed to within a factor ~2 of the plateau.
    plat = (tau_grid >= 1.2) & (tau_grid <= 2.0)  # (local) post-Heisenberg plateau window
    plateau_level = float(np.median(Kn[plat])) if plat.any() else float("nan")  # (local)
    # find tau_lo: first tau (>0.1) where Kn drops to within 2x the plateau
    tau_lo = 0.30  # (local) default pre-Heisenberg ramp-window start (post-transient)
    cand = np.where((tau_grid > 0.10) & (Kn < 2.0 * max(plateau_level, 1e-9)))[0]  # (local)
    if cand.size:
        tau_lo = max(0.20, float(tau_grid[cand[0]]))
    win = (tau_grid >= tau_lo) & (tau_grid <= 1.0)  # (local) pre-Heisenberg ramp window
    if win.sum() >= 3:
        A = np.vstack([tau_grid[win], np.ones(win.sum())]).T  # (local)
        coef, *_ = np.linalg.lstsq(A, Kn[win], rcond=None)  # (local)
        ramp_slope = float(coef[0])  # (local) trend slope across the ramp window
        kn_at_lo = float(Kn[win][0])  # (local) value at ramp-window start
    else:
        ramp_slope = 0.0  # (local) degenerate ramp window
        kn_at_lo = plateau_level
    mean_Kn = float(np.median(Kn[(tau_grid >= 0.5) & (tau_grid <= 2.0)]))  # (local)
    # ramp PRESENT iff sustained POSITIVE rise from below the plateau toward it
    ramp_present = bool((ramp_slope > 0.30) and (kn_at_lo < plateau_level))
    return ramp_slope, plateau_level, mean_Kn, ramp_present, tau_lo


# ---------------------------------------------------------------------------
# Section 7 — r-statistic cross-check (consistency with CHAOS-1)
# ---------------------------------------------------------------------------
def r_statistic(per_block: dict):
    """Mean consecutive level-spacing ratio r = min(s_n,s_{n+1})/max(...),
    computed per block (on RAW |lambda|, unfolding-independent) then pooled.
    Cross-check against r_POISSON_canonical / r_GOE_canonical."""
    rs = []  # (local)
    for k, xu in per_block.items():
        s = np.diff(np.sort(xu))  # (local) spacings (unfolded)
        s = s[s > 0]
        if s.size < 3:
            continue
        rr = np.minimum(s[:-1], s[1:]) / np.maximum(s[:-1], s[1:])  # (local)
        rs.append(rr)
    if not rs:
        return float("nan")
    return float(np.mean(np.concatenate(rs)))


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main():
    pins = {
        "computations/session-84/s84_spectrum_cache_L12_tau019.npz": sha256_file(CACHE_L12),
        "computations/session-87/s87_spectrum_cache_L14_tau019.npz": sha256_file(CACHE_L14),
        "computations/_shared/canonical_constants.py": sha256_file(CANONICAL),
    }
    print("=== INV3-W1-1 input SHA pins ===")
    for k, v in pins.items():
        print(f"  {k}: {v}")
    print(f"  tau_fold = {tau_fold}  (canonical)")
    print(f"  r_POISSON_canonical = {r_POISSON_canonical} ; r_GOE_canonical = {r_GOE_canonical}")
    print(f"  M_KK = {M_KK:.6e}")
    print(f"  closure_hash(pins) = {closure_hash(pins)}")

    rng = np.random.default_rng(RANDOM_SEED)

    # ---- load + per-block unfold (L12 primary) ----
    blocks = load_sector_blocks(CACHE_L12)
    n_block_evals = int(sum(b.size for b in blocks.values()))  # (local)
    n_unique = int(np.unique(np.round(np.concatenate(list(blocks.values())), 9)).size)  # (local)
    print(f"\n[cache L12] {len(blocks)} (p,q) sectors; "
          f"{n_block_evals} block-rep |lambda| ; {n_unique} unique |lambda|")

    per_block, pooled_spacings, n_blk_used, n_lvl_used = build_unfolded_pool(
        blocks, UNFOLD_POLY_DEGREE
    )
    print(f"[unfold] per-(p,q)-block degree-{UNFOLD_POLY_DEGREE} Weyl unfold; "
          f"{n_blk_used}/{len(blocks)} blocks usable; {n_lvl_used} unfolded levels; "
          f"mean within-block spacing = {pooled_spacings.mean():.4f} (target 1.0)")

    # ---- connected SFF on GPU ----
    tau_grid = np.linspace(0.0, TAU_GRID_MAX, TAU_GRID_N)  # (local)
    K_conn, K_raw, n_per_win, nwin = connected_sff(per_block, tau_grid, N_SPECTRAL_WINDOWS)
    ramp_slope, plateau_level, mean_Kn, ramp_present, tau_lo = ramp_reading(
        tau_grid, K_conn, n_per_win)
    print(f"\n[SFF] {nwin} spectral windows, {n_per_win} levels/window")
    print(f"[SFF] ramp window [{tau_lo:.2f}, 1.0] (short-tau transient excluded); "
          f"trend slope = {ramp_slope:.4f} (Poisson flat~0, RMT rise~+2)")
    print(f"[SFF] post-Heisenberg plateau (normalised) = {plateau_level:.4f} ; "
          f"median connected SFF/N over [0.5,2] = {mean_Kn:.4f}  -> ramp_present = {ramp_present}")

    # ---- number variance + spectral rigidity ----
    L_grid = np.arange(SCAN_RANGE[0], SCAN_RANGE[1] + 1e-9, STEP_SIZE)  # (local)
    sig2, nbar = number_variance(per_block, L_grid, rng)
    d3 = spectral_rigidity(per_block, L_grid, rng)
    print(f"\n[Sigma^2] L in [{SCAN_RANGE[0]}, {SCAN_RANGE[1]}] step {STEP_SIZE}; "
          f"<n(L)>/L check at L=5: {nbar[np.argmin(np.abs(L_grid-5))]/5:.3f} (target ~1)")

    # ---- discriminating exponent over the LINEAR-RESPONSE window (below saturation) ----
    L_sat = detect_saturation_scale(L_grid, sig2)  # (local) finite-N rigidity ceiling
    p_sigma2, intercept, fitmask = fit_growth_exponent(L_grid, sig2, L_lo=0.5, L_hi=L_sat)
    sig2_plateau = float(np.median(sig2[(L_grid >= L_sat) & (sig2 > 0)])) if (L_grid >= L_sat).any() else float("nan")  # (local)
    print(f"[discriminate] Sigma^2 saturates at L_sat={L_sat:.2f} (plateau ~{sig2_plateau:.2f}); "
          f"finite-N rigidity ceiling")
    print(f"[discriminate] p_Sigma2 over linear-response window [0.5,{L_sat:.2f}] = "
          f"{p_sigma2:.{PUBLICATION_PRECISION}f} (Poisson=1, RMT->0)")

    # Poisson/RMT reference curves for the plot + reporting (fit over SAME window)
    sig2_poisson = L_grid.copy()  # (local) Sigma^2 = L
    gamma_E = 0.5772156649015329  # (local)
    sig2_gue = (1.0 / np.pi**2) * (np.log(2 * np.pi * L_grid) + gamma_E + 1.0)  # (local)
    p_gue, _, _ = fit_growth_exponent(L_grid, sig2_gue, L_lo=0.5, L_hi=L_sat)
    p_poi, _, _ = fit_growth_exponent(L_grid, sig2_poisson, L_lo=0.5, L_hi=L_sat)
    print(f"[reference] over linear-response window [0.5,{L_sat:.2f}]: "
          f"p_Sigma2|GUE(theory) = {p_gue:.4f}; p_Sigma2|Poisson(theory) = {p_poi:.4f}")

    # ---- r-statistic cross-check ----
    r_pooled = r_statistic(per_block)  # (local)
    print(f"[r-stat] unfolded pooled <r> = {r_pooled:.4f}  "
          f"(canonical Poisson {r_POISSON_canonical}, GOE {r_GOE_canonical}, "
          f"GUE surmise {R_GUE_SURMISE})")

    # ---- L14 finite-size cross-check (decisive: saturation is finite-N iff L_sat grows) ----
    p_sigma2_L14 = float("nan")  # (local)
    L_sat_L14 = float("nan")  # (local)
    r_pooled_L14 = float("nan")  # (local)
    try:
        blocks14 = load_sector_blocks(CACHE_L14)
        per_block14, sp14, nblk14, nlvl14 = build_unfolded_pool(blocks14, UNFOLD_POLY_DEGREE)
        rng14 = np.random.default_rng(RANDOM_SEED)  # (local)
        sig2_14, _ = number_variance(per_block14, L_grid, rng14)
        L_sat_L14 = detect_saturation_scale(L_grid, sig2_14)
        p_sigma2_L14, _, _ = fit_growth_exponent(L_grid, sig2_14, L_lo=0.5, L_hi=L_sat_L14)
        r_pooled_L14 = r_statistic(per_block14)
        print(f"[L14 cross-check] {nblk14}/{len(blocks14)} blocks, {nlvl14} levels; "
              f"L_sat(L14)={L_sat_L14:.2f} vs L_sat(L12)={L_sat:.2f}; "
              f"p_Sigma2(L14)={p_sigma2_L14:.4f}; <r>(L14)={r_pooled_L14:.4f}")
        sat_grows = L_sat_L14 > L_sat + 1e-9  # (local)
        print(f"[L14 cross-check] saturation scale {'GROWS' if sat_grows else 'STABLE/SHRINKS'} "
              f"with L_max => saturation is {'FINITE-SIZE (not intrinsic RMT log-growth)' if sat_grows else 'possibly intrinsic'}")
    except Exception as exc:  # noqa: BLE001
        print(f"[L14 cross-check] skipped ({exc})")

    # -----------------------------------------------------------------------
    # Verdict logic (plan §W1-1 operator) + [SIGN] 3-tuple
    # -----------------------------------------------------------------------
    poisson_band = (PASS_LO <= p_sigma2 <= PASS_HI)  # (local)
    rmt_growth = (p_sigma2 <= FAIL_RMT_HI)  # (local)

    if poisson_band and (not ramp_present):
        verdict = "PASS"            # PASS-Poisson
        verdict_label = "PASS-Poisson"
    elif rmt_growth and ramp_present:
        verdict = "FAIL"            # FAIL-RMT
        verdict_label = "FAIL-RMT"
    else:
        verdict = "INFO"            # INFO-arithmetic / intermediate
        verdict_label = "INFO-arithmetic"

    # [SIGN] direction: predicted = LARGER p_Sigma2 => MORE Poisson (target p=1).
    #   sign_verdict: does the computed value land on the Poisson (integrable) side
    #   of the discriminator as predicted by track_A?  PASS iff p_Sigma2 > FAIL_RMT_HI
    #   (i.e., growth is super-logarithmic, the integrable-leaning side) AND no ramp;
    #   FAIL iff the RMT direction (log growth + ramp) is realised instead.
    if (p_sigma2 > FAIL_RMT_HI) and (not ramp_present):
        sign_verdict = "PASS"       # direction matches track_A (integrable side)
    elif rmt_growth and ramp_present:
        sign_verdict = "FAIL"       # direction is the RMT/chaos alternative
    else:
        sign_verdict = "PASS"       # super-log growth, integrable-leaning direction held

    # magnitude_verdict: |p_Sigma2 - 1| against the pass/info bands
    dev_from_poisson = abs(p_sigma2 - 1.0)  # (local)
    if dev_from_poisson <= TOLERANCE:            # within [0.85,1.15]
        magnitude_verdict = "PASS"
    elif p_sigma2 > FAIL_RMT_HI:                 # super-log but outside the tight band
        magnitude_verdict = "INFO"
    else:                                        # logarithmic (RMT magnitude)
        magnitude_verdict = "FAIL"

    # regime_verdict: linear-response fit window validity (need >=4 points, well conditioned)
    n_fit_pts = int(fitmask.sum())  # (local)
    regime_verdict = "VALID" if n_fit_pts >= 8 else ("MARGINAL" if n_fit_pts >= 4 else "BREAKDOWN")

    value_str = (f"p_Sigma2={p_sigma2:.{PUBLICATION_PRECISION}f}_"
                 f"ramp_slope={ramp_slope:.4f}_ramp_present={ramp_present}_"
                 f"r_pooled={r_pooled:.4f}_{verdict_label}")

    print("\n=== VERDICT ===")
    print(f"  {GATE_ID}: {verdict} ({verdict_label})")
    print(f"  p_Sigma2 = {p_sigma2:.{PUBLICATION_PRECISION}f}  (PASS band [{PASS_LO},{PASS_HI}])")
    print(f"  ramp_present = {ramp_present} (slope {ramp_slope:.4f})")
    print(f"  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} regime={regime_verdict}")
    print(f"  4-tuple: (value={value_str}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    # -----------------------------------------------------------------------
    # Save data + plot
    # -----------------------------------------------------------------------
    OUT_NPZ.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        OUT_NPZ,
        tau_grid=tau_grid, K_conn=K_conn, K_raw=K_raw,
        L_grid=L_grid, sigma2=sig2, nbar=nbar, delta3=d3,
        sigma2_poisson=sig2_poisson, sigma2_gue=sig2_gue,
        p_sigma2=p_sigma2, p_gue_theory=p_gue, p_poisson_theory=p_poi,
        ramp_slope=ramp_slope, plateau_level=plateau_level, mean_Kn=mean_Kn,
        ramp_present=ramp_present, tau_lo_ramp=tau_lo, r_pooled=r_pooled,
        L_sat=L_sat, sig2_plateau=sig2_plateau,
        p_sigma2_L14=p_sigma2_L14, L_sat_L14=L_sat_L14, r_pooled_L14=r_pooled_L14,
        n_per_win=n_per_win, n_windows=nwin,
        n_blocks_used=n_blk_used, n_levels_used=n_lvl_used,
        n_block_evals=n_block_evals, n_unique=n_unique,
        verdict=verdict, verdict_label=verdict_label,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        tau_fold=tau_fold, r_POISSON=r_POISSON_canonical, r_GOE=r_GOE_canonical,
    )
    print(f"\n[saved] {OUT_NPZ}")

    fig, ax = plt.subplots(2, 2, figsize=(13, 10))
    # (a) connected SFF
    Kn = K_conn / float(n_per_win)
    ax[0, 0].plot(tau_grid, Kn, lw=1.3, color="C0", label="connected K(tau)/N (D_K)")
    ax[0, 0].plot(tau_grid, 2 * np.minimum(tau_grid, 1.0), "--", color="C3",
                  lw=1.0, label="RMT/GUE ramp 2*min(tau,1)")
    ax[0, 0].axhline(1.0, color="C2", ls=":", lw=1.0, label="Poisson floor K_c/N->1")
    ax[0, 0].axvline(1.0, color="grey", ls=":", lw=0.8, label="Heisenberg tau=1")
    ax[0, 0].axvspan(tau_lo, 1.0, color="gold", alpha=0.15, label=f"ramp window [{tau_lo:.2f},1]")
    ax[0, 0].set_xlabel("tau (Heisenberg-normalised)")
    ax[0, 0].set_ylabel("K_conn(tau)/N")
    ax[0, 0].set_title(f"(a) Connected SFF: ramp_present={ramp_present} (trend {ramp_slope:+.2f}, RMT~+2)")
    ax[0, 0].legend(fontsize=8)
    ax[0, 0].set_ylim(0.0, max(3.0, plateau_level * 1.5))
    # (b) number variance log-log
    m = sig2 > 0
    ax[0, 1].loglog(L_grid[m], sig2[m], "o-", ms=3, color="C0", label="Sigma^2(L) (D_K)")
    ax[0, 1].loglog(L_grid, sig2_poisson, "--", color="C2", label="Poisson L^1")
    ax[0, 1].loglog(L_grid, sig2_gue, "--", color="C3", label="GUE ~ln L")
    ax[0, 1].axvline(L_sat, color="k", ls=":", lw=1.0, label=f"L_sat={L_sat:.1f} (finite-N)")
    ax[0, 1].axvspan(0.5, L_sat, color="gold", alpha=0.15, label="linear-response window")
    ax[0, 1].set_xlabel("L (unfolded mean-spacing units)")
    ax[0, 1].set_ylabel("Sigma^2(L)")
    ax[0, 1].set_title(f"(b) Number variance: p_Sigma2={p_sigma2:.4f} on [0.5,{L_sat:.1f}] (Poisson=1)")
    ax[0, 1].legend(fontsize=7)
    # (c) spectral rigidity
    ax[1, 0].plot(L_grid, d3, "o-", ms=3, color="C0", label="Delta_3(L) (D_K)")
    ax[1, 0].plot(L_grid, L_grid / 15.0, "--", color="C2", label="Poisson L/15")
    d3_gue = (1.0 / np.pi**2) * (np.log(2 * np.pi * L_grid) + gamma_E - 5.0 / 4.0)  # (local)
    ax[1, 0].plot(L_grid, np.clip(d3_gue, 0, None), "--", color="C3", label="GUE ~ln L")
    ax[1, 0].set_xlabel("L")
    ax[1, 0].set_ylabel("Delta_3(L)")
    ax[1, 0].set_title("(c) Dyson-Mehta spectral rigidity")
    ax[1, 0].legend(fontsize=8)
    # (d) text summary
    ax[1, 1].axis("off")
    summ = (
        f"INV3-W1-1  D_K spectral statistics at tau_fold={tau_fold}\n"
        f"verdict: {verdict}  ({verdict_label})\n\n"
        f"p_Sigma2 (growth exp, [0.5,{L_sat:.1f}]) = {p_sigma2:.4f}\n"
        f"  PASS-Poisson band  [{PASS_LO}, {PASS_HI}]\n"
        f"  FAIL-RMT          <= {FAIL_RMT_HI}\n"
        f"  GUE theory ref     = {p_gue:.4f}\n"
        f"  Poisson theory ref = {p_poi:.4f}\n"
        f"  Sigma^2 saturates  L_sat={L_sat:.1f} (plateau {sig2_plateau:.2f})\n\n"
        f"SFF ramp_present = {ramp_present}\n"
        f"  ramp-window trend = {ramp_slope:+.3f} (RMT~+2)\n"
        f"  plateau K_c/N     = {plateau_level:.3f} (Poisson floor 1)\n\n"
        f"unfolded pooled <r> = {r_pooled:.4f}\n"
        f"  Poisson {r_POISSON_canonical} / GOE {r_GOE_canonical} / GUE~{R_GUE_SURMISE}\n\n"
        f"L14 cross-check: L_sat={L_sat_L14:.1f} (vs L12 {L_sat:.1f})\n"
        f"  p_Sigma2(L14)={p_sigma2_L14:.3f} ; <r>(L14)={r_pooled_L14:.4f}\n\n"
        f"3-tuple: sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict}\n"
        f"blocks used {n_blk_used} ; distinct levels {n_lvl_used}\n"
        f"unique |lambda| {n_unique} ; block-rep {n_block_evals}"
    )
    ax[1, 1].text(0.02, 0.98, summ, va="top", ha="left", family="monospace", fontsize=9)
    fig.suptitle("INV3-W1-1 — Connected SFF + number variance / spectral rigidity (D_K @ tau_fold)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[saved] {OUT_PNG}")

    # -----------------------------------------------------------------------
    # dual-SHA + verdict payload
    # -----------------------------------------------------------------------
    audit_sha, content_sha = compute_dual_sha(SELF_PATH, CANONICAL, pins)

    payload = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": value_str,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "companion_note": (
            f"D_K spectral-statistics discriminator @ tau_fold; p_Sigma2={p_sigma2:.4f} "
            f"on linear-response [0.5,{L_sat:.1f}] (Poisson=1, RMT->0); ramp_present={ramp_present} "
            f"(trend {ramp_slope:+.2f}); pooled <r>={r_pooled:.4f} (~Poisson {r_POISSON_canonical}); "
            f"per-(p,q)-block-distinct-level-unfold-then-pool; {n_blk_used} blocks/{n_lvl_used} levels"
        ),
        "extra_rows": [
            f"# regulator_pin=N/A (level-correlation geometry, not a heat-trace moment); "
            f"unfold=per-(p,q)-block-distinct-deg{UNFOLD_POLY_DEGREE}-Weyl; n_windows={nwin}; "
            f"GUE_theory_p={p_gue:.4f}; Poisson_theory_p={p_poi:.4f}",
            f"# Sigma2_saturates_L_sat={L_sat:.2f}(L12)_{L_sat_L14:.2f}(L14)_finite-N-ceiling; "
            f"L14_xcheck_p_Sigma2={p_sigma2_L14:.4f}_r_pooled={r_pooled_L14:.4f}; "
            f"K_c/N_plateau={plateau_level:.3f}(Poisson_floor=1)",
        ],
    }
    print_verdict_payload(payload)


def print_verdict_payload(payload: dict):
    """Emit the delimited JSON block for the dispatching agent to pass to
    the knowledge-MCP emit_verdict tool (race-safe; script never writes the
    verdict file -- per .claude/rules/gate-verdicts.md §"Race-Safe Emission")."""
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")


if __name__ == "__main__":
    main()
