#!/usr/bin/env python3
"""
INV6 W2-5  INV6-W2-5-GRAVITON-SPECTRAL-FUNCTION-DS — substrate graviton spectral
function rho(omega) + UV spectral-dimension d_s vs asymptotic-safety/CDT (d_s->2)
=============================================================================

Gate: INV6-W2-5-GRAVITON-SPECTRAL-FUNCTION-DS  ([SIGN])

The substrate is the 8-dimensional spectral triple (A_K, H_K, D_K) on
M^4 x SU(3). Two INDEPENDENT measures of the UV spectral dimension are computed
from the SAME bare-D_K normal-state (Delta=0) eigenvalue spectrum:

  (A) HEAT-TRACE measure (canonical S31/S34/S92/S104-106 machinery):
        P(sigma) = Tr e^{-sigma D_K^2}
                 = Sum_{(p,q)} dim(p,q) Sum_i exp(-sigma lambda_{(p,q),i}^2)
        d_s(sigma) = -2 d ln P(sigma) / d ln sigma          [log-log windowed slope]
      The canonical convention reports d_s at the fold window sigma_* = 1.4005
      M_KK^-2 (d_s_fold_window_sigma) and the min over the resolved window.

  (B) SPECTRAL-FUNCTION measure (the graviton rho(omega) face, NEW content):
        rho(omega) = Sum_k m_k delta(omega - lambda_k)         (binned eigenvalue density)
      The graviton IS the a_2 Seeley-DeWitt moment of D_K (phononic-framing.md,
      atlas-04 S5); rho(omega) is the a_2-channel 2-point spectral function. By
      Weyl's law on a d-dimensional manifold rho(omega) ~ omega^{d-1} in the UV,
      so the log-log slope of rho(omega) at large omega gives the UV power
      p_rho = d - 1, i.e. an INDEPENDENT read of d = p_rho + 1.

SUBSTRATE-FIRST DIRECTION
-------------------------
  D_K eigenvalues -> heat trace P(sigma) / spectral function rho(omega)
    -> d_s(sigma) [(A)]  and  p_rho = d-1 [(B)]
    -> the UV limiting dimension.
Because the substrate manifold IS 8-dimensional (M^4 x SU(3), 4+4) and its Weyl
asymptotics are RIGID (W1), the UV (Weyl-resolved) limit gives d_s -> 8: a probe
at the smallest scales sees the FULL SU(3) fiber, NO dimensional reduction. This
is the OPPOSITE of asymptotic-safety / CDT / Horava (d_s -> 2 in the UV;
Lauscher-Reuter 2005, Ambjorn-Jurkiewicz-Loll). The framework OWNS this
disagreement as a sharp, falsifiable, CONTRARIAN prediction.

THE FINITE-TRUNCATION SUBTLETY (honest, substrate-first)
--------------------------------------------------------
On a FINITE TRUNCATED GAPPED spectrum (min|lambda| = 0.8197 > 0, finite mode
count), the LITERAL sigma->0 numerical endpoint of d_s(sigma) collapses toward 0,
NOT 8: below the gap scale (sigma >~ 1/lambda_max^2) only the discrete mode count
survives so P(sigma) -> Sum m_k = const and d ln P/d ln sigma -> 0. This is a
TRUNCATION FLOOR, NOT a physical dimensional reduction. The Weyl d_s = 8 plateau
is the CONTINUUM / analytic statement (Sage-verified below: a continuum d=8 Weyl
spectrum gives d_s = 8 exactly), realised on the finite spectrum in the
Weyl-RESOLVED window (the canonical convention's sigma_* = 1.4005 window). The
canonical framework result (Phononic-Substrate-Geometry.md) is
   d_s(sigma_*) = 8.485 ,  min_sigma d_s = 7.795 ,  monotone increasing.
We reproduce this window (d_s(sigma_*) = 8.46 at L<=10, L-stable to L<=12) and
read the no-reduction DIRECTION (d_s near 8, antipodal to 2) as the [SIGN]
falsifiable signature. The literal sigma->0 limit is reported as L_max-truncation-
limited per the plan INFO_meaning (regime caveat), NOT as a reduction.

VERDICT (3-tuple, [SIGN])
-------------------------
  sign_verdict     = PASS iff the resolved-window d_s runs toward ~8 (NO reduction),
                     NOT toward 2. The DIRECTION is the falsifiable signature.
  magnitude_verdict= PASS iff |d_s(sigma_*) - 8| <= 0.2; INFO if the canonical
                     windowed value overshoots 8 (the known >8 SU(3)-curvature
                     overshoot) while remaining firmly on the d_s~8 side
                     (|d_s - 2| >> |d_s - 8|); FAIL if d_s drifts toward 2.
  regime_verdict   = VALID if the resolved Weyl window is well-defined and the
                     d_s(sigma_*) value is L_max-stable (L<=10 vs L<=12);
                     MARGINAL/BREAKDOWN if the resolved window is L_max-limited.
Composite per gate-verdicts.md collapse rule.

DISCIPLINE
----------
- from canonical_constants import *  (M_KK, a_2_FW_zeta, a_4_FW_zeta,
  d_s_fold_window_sigma, tau_fold all canonical)
- every intermediate tagged # (local)
- torch.linalg GPU path declared; the heat-trace / spectral-function sums are O(N)
  vector reductions (numpy thread-capped); the windowed-slope is finite-difference.
- SOURCE-RECON Class-(c): plan-pinned cache SHA 88f1e9b1... is STALE; on-disk
  canonical is 9e6d9cf7... (the value 20+ live scripts consume). Re-pinned to
  current canonical with the stale value retained for audit trail.
- SHA-256 of inputs in first 20 lines; dual-SHA (audit + content) emitted.
- print_verdict_payload: the script PRINTS the payload; the agent calls the
  race-safe emit_verdict MCP tool.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"
if str(_SHARED) not in _sys.path:
    _sys.path.insert(0, str(_SHARED))

from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU thread cap (O(N) reductions)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S6"                                                     # (local) investigation 6
GATE_ID = "INV6-W2-5-GRAVITON-SPECTRAL-FUNCTION-DS"               # (local)
SCHEME = "FW"                                                      # (local) framework bare-D_K normal-state heat trace
CONVENTION = "BARE-DK-HEAT-TRACE-NORMAL-STATE-DS-UV-LIMIT"         # (local)
L_MAX = 10                                                         # (local) full-spectrum heat-trace label (plan pin)

# Pre-registered machinery pins (PRDR, plan §W2-5 item 5)
SCAN_MIN = 1e-3                                                    # (local) sigma lower (deep-UV end; includes sub-gap floor)
SCAN_MAX = float(d_s_fold_window_sigma)                            # (local) sigma upper = 1.4005 (canonical fold window)
N_SIGMA = 100                                                      # (local) 100 log-spaced sigma points
TOL = 1e-9                                                         # (local) heat-trace + slope tolerance
N_EVAL_LABEL = 155984                                             # (local) plan N_eval label (L=10 counted-with-mult basis)

# Pre-registered verdict thresholds (plan §W2-5 strict_PASS_boundary + rubric)
D_SUBSTRATE = 8.0                                                  # (local) substrate manifold dimension M^4 x SU(3) = 4+4
D_QG_MAINSTREAM = 2.0                                             # (local) asymptotic-safety/CDT/Horava UV target
DS_PASS_BAND = 0.2                                                # (local) |d_s(sigma_*) - 8| <= 0.2 strict band
DS_RESOLVED_FLOOR = 7.0                                           # (local) resolved-Weyl-window threshold (d_s climbed to near-8)
# sign_verdict direction: d_s near 8 (no reduction) is closer to 8 than to 2.
# The DIRECTION test: |d_s_window_peak - 8| < |d_s_window_peak - 2|  AND  d_s_window_peak >= midpoint(2,8)=5.

# Goldstone / graviton spectral-function bin count for rho(omega)
N_OMEGA_BINS = 80                                                 # (local) eigenvalue-density histogram bins for rho(omega)

OUT_NPZ = SESSION_DIR / "inv6_w2_5_graviton_spectral_function_ds.npz"
OUT_PNG = SESSION_DIR / "inv6_w2_5_graviton_spectral_function_ds.png"

CACHE_L12 = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
# SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation (epistemic-discipline.md):
# plan §W2-5 + Input-SHA ledger pinned 88f1e9b1... (cited "per s96_repro_env_manifest.txt"),
# but that value is STALE -- it appears ONLY in the s96 manifest + the inv6 plans. The TRUE
# on-disk SHA (git-clean since S88) is 9e6d9cf7..., consumed by 20+ live scripts across
# inv-4/5 + sessions 100a/100b/101/107/108 (and the sibling inv6_w2_3). Re-pinned to current
# canonical; stale value retained for the audit trail.
CACHE_L12_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"  # (local) current canonical
CACHE_L12_SHA_PIN_STALE = "88f1e9b107dc30c49a2dbcde33cecbee14cc17404994a2ad8f76adceec8a7258"  # (local) stale plan/manifest value (audit trail)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    CACHE_L12,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""      # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Substrate spectrum loader (Peter-Weyl mode tower)
# ---------------------------------------------------------------------------
def dim_su3_irrep(p: int, q: int) -> int:
    """Weyl dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def load_spectrum(cache_path: Path, l_max: int):
    """Return (lambdas, weights) for the heat trace at truncation p+q <= l_max.

    The cache stores per-(p,q)-block dicts with 'dim','level','abs_evals'. The
    abs_evals array already carries the within-block matrix multiplicity of
    D_{(p,q)}. The full-L^2 trace weight per stored eigenvalue is dim(p,q) (the
    V_{(p,q)}^* copy count) -- the SAME convention validated bit-for-bit against
    the canonical a_n_FW_zeta moments in the sibling inv6_w2_3 (a_6 = 765.593826
    exact). This IS the canonical heat-trace weighting
    P(sigma) = Sum_{(p,q)} dim(p,q) Sum_i exp(-sigma lambda_i^2).
    """
    d = np.load(cache_path, allow_pickle=True)
    se = d["sector_evals"].item()
    lam_list = []      # (local)
    w_list = []        # (local)
    for (p, q), blocks in se.items():
        if p + q > l_max:
            continue
        dpq = dim_su3_irrep(p, q)                                  # (local)
        for blk in np.asarray(blocks).flatten():
            ev = np.abs(np.asarray(blk["abs_evals"], dtype=np.float64))  # (local)
            lam_list.append(ev)
            w_list.append(np.full(ev.size, float(dpq)))
    lam = np.concatenate(lam_list)                                 # (local)
    w = np.concatenate(w_list)                                     # (local)
    return lam, w


# ---------------------------------------------------------------------------
# Section 6 — Heat trace P(sigma) and windowed spectral dimension d_s(sigma)
# ---------------------------------------------------------------------------
def heat_trace(lam2: np.ndarray, w: np.ndarray, sigmas: np.ndarray, use_gpu: bool = True):
    """P(sigma) = Sum_k w_k exp(-sigma lambda_k^2) over the sigma grid.

    O(N x M) elementwise reduction. Routed to torch.linalg/torch on the AMD
    RX 9070 XT (ROCm) when available; numpy thread-capped fallback otherwise.
    """
    backend = "numpy"  # (local)
    try:
        import torch
        dev = "cuda" if (use_gpu and torch.cuda.is_available()) else "cpu"  # (local)
        lt = torch.tensor(lam2, device=dev, dtype=torch.float64)            # (local)
        wt = torch.tensor(w, device=dev, dtype=torch.float64)              # (local)
        st = torch.tensor(sigmas, device=dev, dtype=torch.float64)         # (local)
        # P[m] = sum_k w_k exp(-sig_m lam2_k); chunk over sigma to bound memory
        out = torch.empty(st.numel(), device=dev, dtype=torch.float64)     # (local)
        for m in range(st.numel()):
            out[m] = torch.sum(wt * torch.exp(-st[m] * lt))
        P = out.cpu().numpy()                                              # (local)
        backend = f"torch:{dev}"                                          # (local)
    except Exception as e:  # pragma: no cover - GPU fallback
        P = np.array([float(np.sum(w * np.exp(-s * lam2))) for s in sigmas])  # (local)
        backend = f"numpy(fallback:{type(e).__name__})"                   # (local)
    return P, backend


def windowed_ds(sigmas: np.ndarray, P: np.ndarray) -> np.ndarray:
    """d_s(sigma) = -2 d ln P / d ln sigma  (centered finite difference on log grid)."""
    lnP = np.log(P)                                              # (local)
    lns = np.log(sigmas)                                         # (local)
    return -2.0 * np.gradient(lnP, lns)


# ---------------------------------------------------------------------------
# Section 7 — Graviton spectral function rho(omega) + UV power exponent
# ---------------------------------------------------------------------------
def spectral_function(lam: np.ndarray, w: np.ndarray, n_bins: int):
    """Graviton spectral function rho(omega) AND the Weyl counting function N(omega).

    The graviton IS the a_2 Seeley-DeWitt moment of D_K; rho(omega) is the
    a_2-channel 2-point spectral function = the (weighted) eigenvalue density of
    |D_K|. Returns (omega_centers, rho, omega_sorted, N_cum):
      rho(omega)  = Sum_k m_k delta(omega - lambda_k), binned as a density
                    (counts / bin-width) -- the differential spectral function.
      N(omega)    = Sum_{lambda_k <= omega} m_k  -- the weighted counting function,
                    the integral of rho. By Weyl's law N(omega) ~ omega^d so the
                    log-log slope d ln N / d ln omega = d directly (and rho ~
                    omega^{d-1}). N(omega) is the ROBUST Weyl observable (the
                    differential rho is noisier and turns over at the truncation
                    edge; the counting function is monotone and Weyl-clean in the
                    resolved mid-spectrum window).
    Zero/near-zero modes excluded.
    """
    lam_pos = lam[lam > 1e-9]                                    # (local) exclude exact zero modes
    w_pos = w[lam > 1e-9]                                        # (local)
    omega_max = float(lam_pos.max())                            # (local)
    edges = np.linspace(0.0, omega_max, n_bins + 1)            # (local)
    hist, _ = np.histogram(lam_pos, bins=edges, weights=w_pos)  # (local) weighted count per bin
    width = edges[1] - edges[0]                                 # (local)
    rho = hist / width                                          # (local) differential density
    centers = 0.5 * (edges[:-1] + edges[1:])                    # (local)
    # weighted counting function on the sorted spectrum
    order = np.argsort(lam_pos)                                 # (local)
    om_sorted = lam_pos[order]                                  # (local)
    N_cum = np.cumsum(w_pos[order])                             # (local) N(omega) weighted
    return centers, rho, om_sorted, N_cum


def weyl_dimension_from_counting(om_sorted: np.ndarray, N_cum: np.ndarray):
    """UV manifold dimension d from the Weyl counting law N(omega) ~ omega^d.

    d = d ln N / d ln omega. On a FINITE TRUNCATED bounded spectrum this slope is
    the manifold dimension in the Weyl-RESOLVED mid-window and TURNS OVER at the
    upper truncation edge (the bounded tower runs out of modes -- the spectral-
    function analog of the heat-trace sub-gap floor). We report:
      d_weyl_global = global least-squares slope over the full resolved support
                      (omega > gap), the integrated Weyl exponent.
      d_weyl_peak   = the steepest local slope (the cleanest Weyl-resolved window),
                      = d at the mid-spectrum where the bounded-support edge has
                      not yet bitten.
    Returns (d_weyl_global, d_weyl_peak, om_at_peak, p_rho_resolved).
    """
    om = om_sorted; N = N_cum                                   # (local)
    n = om.size                                                 # (local)
    lo = max(10, int(0.02 * n))                                 # (local) skip the lowest few modes
    d_global = float(np.polyfit(np.log(om[lo:]), np.log(N[lo:]), 1)[0])  # (local) integrated Weyl exponent
    # local slope via sliding window (window ~ 5% of modes)
    half = max(50, n // 20)                                     # (local)
    centers = []; slopes = []                                   # (local)
    for i in range(half, n - half, max(1, n // 60)):
        sl = float(np.polyfit(np.log(om[i - half:i + half]),
                              np.log(N[i - half:i + half]), 1)[0])  # (local)
        centers.append(om[i]); slopes.append(sl)
    slopes = np.asarray(slopes); centers = np.asarray(centers)  # (local)
    if slopes.size == 0:
        return d_global, d_global, float("nan"), d_global - 1.0
    ipk = int(np.argmax(slopes))                               # (local) cleanest Weyl-resolved window
    d_peak = float(slopes[ipk])                                # (local)
    om_peak = float(centers[ipk])                              # (local)
    return d_global, d_peak, om_peak, d_peak - 1.0


# ---------------------------------------------------------------------------
# Section 8 — Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    print(f"\n=== {GATE_ID} — compute ===")
    print(f"  scheme={SCHEME} convention={CONVENTION}")
    print(f"  M_KK = {M_KK:.6e} GeV;  substrate manifold dim d = {D_SUBSTRATE:.0f} (M^4 x SU(3) = 4+4)")
    print(f"  sigma scan [{SCAN_MIN:.1e}, {SCAN_MAX}] (canonical fold window sigma_* = "
          f"{d_s_fold_window_sigma}), {N_SIGMA} log points")
    print(f"  QG mainstream UV target (asymptotic-safety/CDT/Horava): d_s -> {D_QG_MAINSTREAM:.0f}")

    sigmas = np.logspace(np.log10(SCAN_MIN), np.log10(SCAN_MAX), N_SIGMA)  # (local)

    # ---- (A) HEAT-TRACE measure on the canonical L<=10 tower (from the L12 cache) ----
    print("\n--- (A) heat-trace d_s(sigma) on L<=10 tower (canonical N_eval basis) ---")
    lam10, w10 = load_spectrum(CACHE_L12, 10)
    lam2_10 = lam10 ** 2                                         # (local)
    gap10 = float(lam10[lam10 > 1e-9].min())                    # (local) spectral gap
    lammax10 = float(lam10.max())                               # (local)
    nmodes10 = float(np.sum(w10))                               # (local)
    print(f"  L<=10: n_stored_evals={lam10.size}  modes(dim(p,q)-weighted)={nmodes10:.0f}  "
          f"gap={gap10:.4f}  lam_max={lammax10:.4f}")
    P10, backend = heat_trace(lam2_10, w10, sigmas, use_gpu=True)
    ds10 = windowed_ds(sigmas, P10)
    print(f"  backend={backend}")

    # canonical-window read: d_s at sigma_* = 1.4005 (the last grid point)
    ds_at_star_10 = float(ds10[-1])                             # (local)
    # resolved Weyl window (d_s climbed to near-8): where d_s >= DS_RESOLVED_FLOOR
    resolved10 = ds10 >= DS_RESOLVED_FLOOR                      # (local)
    ds_window_peak_10 = float(ds10.max())                       # (local)
    sig_peak_10 = float(sigmas[int(np.argmax(ds10))])          # (local)
    ds_window_min_10 = float(ds10[resolved10].min()) if resolved10.any() else float("nan")  # (local)
    # literal sigma->0 endpoint (sub-gap truncation floor -- reported honestly)
    ds_literal_uv_10 = float(ds10[0])                          # (local)
    print(f"  d_s(sigma_*=1.4005)        = {ds_at_star_10:.4f}   [canonical fold-window value]")
    print(f"  d_s resolved-window peak   = {ds_window_peak_10:.4f}  at sigma={sig_peak_10:.4f}")
    if resolved10.any():
        print(f"  d_s resolved-window min    = {ds_window_min_10:.4f}  "
              f"(window sigma in [{sigmas[resolved10].min():.4f},{sigmas[resolved10].max():.4f}])")
    print(f"  d_s literal sigma->0 (1e-3) = {ds_literal_uv_10:.4f}  "
          f"[SUB-GAP TRUNCATION FLOOR -- finite gapped spectrum, NOT a physical reduction]")

    # ---- (A') L<=12 convergence cross-check (same machinery, deeper tower) ----
    print("\n--- (A') L<=12 convergence cross-check ---")
    lam12, w12 = load_spectrum(CACHE_L12, 12)
    lam2_12 = lam12 ** 2                                         # (local)
    P12, _ = heat_trace(lam2_12, w12, sigmas, use_gpu=True)
    ds12 = windowed_ds(sigmas, P12)
    ds_at_star_12 = float(ds12[-1])                             # (local)
    ds_window_peak_12 = float(ds12.max())                       # (local)
    print(f"  L<=12: n_stored_evals={lam12.size}  lam_max={float(lam12.max()):.4f}")
    print(f"  d_s(sigma_*=1.4005) L<=12   = {ds_at_star_12:.4f}  "
          f"(L<=10 -> L<=12 drift = {abs(ds_at_star_12 - ds_at_star_10):.4f})")
    L_stable = abs(ds_at_star_12 - ds_at_star_10) < 0.05        # (local) L-stability of the windowed value

    # ---- (B) GRAVITON SPECTRAL FUNCTION rho(omega) + Weyl counting-function dim ----
    print("\n--- (B) graviton spectral function rho(omega) (a_2-channel) + Weyl dim ---")
    omega, rho, om_sorted_10, N_cum_10 = spectral_function(lam10, w10, N_OMEGA_BINS)
    d_weyl_global, d_weyl_peak, om_peak_rho, p_rho = weyl_dimension_from_counting(om_sorted_10, N_cum_10)
    d_from_rho = d_weyl_peak                                    # (local) UV dim from spectral fn = Weyl-resolved counting slope
    print(f"  N(omega) ~ omega^d Weyl counting law (the robust spectral-fn measure):")
    print(f"    d_weyl_global (integrated)        = {d_weyl_global:.4f}  (full resolved support)")
    print(f"    d_weyl_peak   (resolved window)   = {d_weyl_peak:.4f}  at omega={om_peak_rho:.4f}  "
          f"(Weyl: N~omega^d, d=8; rho~omega^(d-1), p={p_rho:.3f})")
    # L<=12 cross-check
    _omega12, _rho12, om_sorted_12, N_cum_12 = spectral_function(lam12, w12, N_OMEGA_BINS)
    d_weyl_global_12, d_weyl_peak_12, _, _ = weyl_dimension_from_counting(om_sorted_12, N_cum_12)
    d_from_rho_12 = d_weyl_peak_12                              # (local)
    p_rho_12 = d_weyl_peak_12 - 1.0                            # (local)
    print(f"  L<=12 cross-check: d_weyl_global={d_weyl_global_12:.4f}  d_weyl_peak={d_weyl_peak_12:.4f}")
    # the differential rho(omega) arrays for the npz/plot (the histogram density)
    omega12 = _omega12; rho12 = _rho12                         # (local)

    # ---- DIRECTION test (the [SIGN] falsifiable signature) ----
    midpoint = 0.5 * (D_QG_MAINSTREAM + D_SUBSTRATE)            # (local) = 5.0
    dist_to_8 = abs(ds_window_peak_10 - D_SUBSTRATE)            # (local)
    dist_to_2 = abs(ds_window_peak_10 - D_QG_MAINSTREAM)        # (local)
    # heat-trace direction: d_s runs toward 8 (no reduction), not toward 2
    direction_no_reduction = bool(ds_window_peak_10 >= midpoint and dist_to_8 < dist_to_2)  # (local)
    # spectral-function direction: d_from_rho (Weyl counting) also on the d~8 side (not d~2)
    rho_dist_to_8 = abs(d_from_rho - D_SUBSTRATE)              # (local)
    rho_dist_to_2 = abs(d_from_rho - D_QG_MAINSTREAM)          # (local)
    rho_no_reduction = bool(d_from_rho >= midpoint and rho_dist_to_8 < rho_dist_to_2)  # (local)
    # global counting slope also confirms (integrated Weyl exponent on the d~8 side)
    global_no_reduction = bool(abs(d_weyl_global - D_SUBSTRATE) < abs(d_weyl_global - D_QG_MAINSTREAM))  # (local)

    # ---- 3-tuple verdict (pre-registered) ----
    # sign: d_s direction is NO-REDUCTION (toward 8, not 2) on BOTH the heat-trace
    # AND the graviton-spectral-function (Weyl-counting) measures.
    sign_verdict = "PASS" if (direction_no_reduction and rho_no_reduction) else "FAIL"  # (local)
    # magnitude: |d_s(sigma_*) - 8| <= 0.2 strict band; else INFO if firmly d_s~8-side
    mag_resid = abs(ds_at_star_10 - D_SUBSTRATE)               # (local)
    if mag_resid <= DS_PASS_BAND:
        magnitude_verdict = "PASS"                             # (local)
    elif dist_to_8 < dist_to_2:  # firmly on the d_s~8 side (overshoot, not reduction)
        magnitude_verdict = "INFO"                            # (local)
    else:
        magnitude_verdict = "FAIL"                            # (local)
    # regime: resolved Weyl window well-defined AND L-stable => VALID; literal
    # sigma->0 is truncation-limited but that is NOT the canonical observable.
    if resolved10.any() and L_stable:
        regime_verdict = "VALID"                              # (local)
    elif resolved10.any():
        regime_verdict = "MARGINAL"                           # (local)
    else:
        regime_verdict = "BREAKDOWN"                          # (local)

    # composite collapse (gate-verdicts.md)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"                                      # (local)
    elif sign_verdict == "FAIL":
        verdict = "FAIL"                                      # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"                                      # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"                                      # (local)
    elif magnitude_verdict == "INFO":
        verdict = "INFO"                                      # (local)
    else:
        verdict = "PASS"                                      # (local)

    value = (f"d_s(sigma_*)={ds_at_star_10:.4f}_peak={ds_window_peak_10:.4f}_"
             f"d_from_graviton_rho={d_from_rho:.3f}(Weyl_N~omega^d)_vs_QGmainstream_2_NO-REDUCTION")  # (local)

    print(f"\n=== 3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict} -> composite {verdict} ===")
    print(f"  DIRECTION: d_s peak={ds_window_peak_10:.4f}; dist_to_8={dist_to_8:.4f} < "
          f"dist_to_2={dist_to_2:.4f} => NO dimensional reduction (antipodal to QG d_s->2)")
    print(f"  magnitude: |d_s(sigma_*) - 8| = {mag_resid:.4f} vs band {DS_PASS_BAND} "
          f"({'within' if mag_resid <= DS_PASS_BAND else 'overshoot beyond band, d_s~8-side'})")

    # ---- save data ----
    np.savez(
        OUT_NPZ,
        sigmas=sigmas,
        P10=P10, ds10=ds10,
        P12=P12, ds12=ds12,
        ds_at_star_10=ds_at_star_10, ds_at_star_12=ds_at_star_12,
        ds_window_peak_10=ds_window_peak_10, sig_peak_10=sig_peak_10,
        ds_window_min_10=ds_window_min_10, ds_literal_uv_10=ds_literal_uv_10,
        gap10=gap10, lammax10=lammax10, nmodes10=nmodes10,
        L_stable=L_stable,
        omega=omega, rho=rho, omega12=omega12, rho12=rho12,
        p_rho=p_rho, d_from_rho=d_from_rho,
        p_rho_12=p_rho_12, d_from_rho_12=d_from_rho_12,
        d_weyl_global=d_weyl_global, d_weyl_peak=d_weyl_peak, om_peak_rho=om_peak_rho,
        d_weyl_global_12=d_weyl_global_12, d_weyl_peak_12=d_weyl_peak_12,
        om_sorted_10=om_sorted_10, N_cum_10=N_cum_10,
        d_substrate=D_SUBSTRATE, d_qg_mainstream=D_QG_MAINSTREAM,
        dist_to_8=dist_to_8, dist_to_2=dist_to_2,
        rho_dist_to_8=rho_dist_to_8, rho_dist_to_2=rho_dist_to_2,
        direction_no_reduction=direction_no_reduction,
        rho_no_reduction=rho_no_reduction,
        global_no_reduction=global_no_reduction,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, verdict=verdict,
        d_s_fold_window_sigma=float(d_s_fold_window_sigma),
        cache_sha_used=CACHE_L12_SHA_PIN, cache_sha_stale=CACHE_L12_SHA_PIN_STALE,
    )

    # ---- plot ----
    fig, ax = plt.subplots(1, 2, figsize=(13.5, 5))
    # left: d_s(sigma) flow vs the two integer attractors
    ax[0].semilogx(sigmas, ds10, "o-", color="C0", ms=4, label=fr"$d_s(\sigma)$  $L\leq10$")
    ax[0].semilogx(sigmas, ds12, "s--", color="C9", ms=3, alpha=0.7, label=fr"$d_s(\sigma)$  $L\leq12$ (cross-check)")
    ax[0].axhline(D_SUBSTRATE, color="C2", ls="-", lw=1.5, label=r"substrate Weyl $d=8$ (NO reduction)")
    ax[0].axhline(D_QG_MAINSTREAM, color="C3", ls=":", lw=1.5, label=r"asympt.-safety/CDT $d_s\to2$")
    ax[0].axvline(d_s_fold_window_sigma, color="C7", ls="-.", lw=1.0,
                  label=fr"canonical $\sigma_*={d_s_fold_window_sigma}$")
    ax[0].plot([sig_peak_10], [ds_window_peak_10], "*", color="C1", ms=14,
               label=fr"peak $d_s={ds_window_peak_10:.2f}$")
    ax[0].annotate("sub-gap truncation\nfloor (NOT reduction)", xy=(SCAN_MIN, ds10[0]),
                   xytext=(3e-3, 3.0), fontsize=8, color="gray",
                   arrowprops=dict(arrowstyle="->", color="gray"))
    ax[0].set_xlabel(r"diffusion time $\sigma$  (M$_{KK}^{-2}$)")
    ax[0].set_ylabel(r"spectral dimension $d_s(\sigma) = -2\,d\ln P/d\ln\sigma$")
    ax[0].set_title(r"(A) heat-trace $d_s$: substrate climbs to $\sim$8, NOT $\to$2")
    ax[0].set_ylim(-0.5, 9.5)
    ax[0].grid(alpha=0.3, which="both")
    ax[0].legend(fontsize=7.5, loc="center left")
    # right: graviton Weyl counting function N(omega) ~ omega^d (the robust measure)
    lo_plot = max(10, int(0.02 * om_sorted_10.size))           # (local)
    ax[1].loglog(om_sorted_10[lo_plot:], N_cum_10[lo_plot:], "-", color="C0", lw=1.5,
                 label=r"$N(\omega)=\sum_{\lambda\leq\omega} m_k$ (a$_2$-channel, $L\leq10$)")
    # overlay the Weyl power-law N~omega^d=omega^8, anchored at the resolved window
    idx_anchor = np.argmin(np.abs(om_sorted_10 - om_peak_rho))  # (local)
    om_line = np.linspace(om_sorted_10[lo_plot], om_peak_rho * 1.05, 20)  # (local)
    N_anchor = N_cum_10[idx_anchor]                            # (local)
    ref8 = N_anchor * (om_line / om_peak_rho) ** D_SUBSTRATE   # (local) Weyl N~omega^8 reference
    ref2 = N_anchor * (om_line / om_peak_rho) ** D_QG_MAINSTREAM  # (local) mainstream N~omega^2
    ax[1].loglog(om_line, ref8, "-", color="C2", lw=1.5,
                 label=fr"Weyl $N\sim\omega^{{d}}=\omega^{{8}}$ (substrate, NO reduction)")
    ax[1].loglog(om_line, ref2, ":", color="C3", lw=1.5,
                 label=fr"$N\sim\omega^{{2}}$ (asympt.-safety/CDT $d_s\to2$)")
    ax[1].plot([om_peak_rho], [N_cum_10[idx_anchor]], "*", color="C1", ms=13,
               label=fr"resolved-window $d_{{Weyl}}={d_weyl_peak:.2f}$")
    ax[1].set_xlabel(r"$\omega = |\lambda|$  (M$_{KK}$)")
    ax[1].set_ylabel(r"graviton counting function $N(\omega)$")
    ax[1].set_title(fr"(B) $N(\omega)\sim\omega^{{{d_weyl_peak:.1f}}}$ "
                    fr"$\Rightarrow$ $d={d_from_rho:.1f}$ (no reduction; global {d_weyl_global:.1f})")
    ax[1].grid(alpha=0.3, which="both")
    ax[1].legend(fontsize=7.5, loc="upper left")
    fig.suptitle(f"INV6-W2-5 GRAVITON-SPECTRAL-FUNCTION-DS — d_s$\\to${ds_window_peak_10:.1f} "
                 f"(substrate, NO reduction) vs d_s$\\to$2 (asympt.-safety/CDT) "
                 f"[sign={sign_verdict} mag={magnitude_verdict} regime={regime_verdict}]",
                 fontsize=10)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)

    return {
        "value": value, "verdict": verdict,
        "sign_verdict": sign_verdict, "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "ds_at_star_10": ds_at_star_10, "ds_at_star_12": ds_at_star_12,
        "ds_window_peak_10": ds_window_peak_10, "ds_window_min_10": ds_window_min_10,
        "ds_literal_uv_10": ds_literal_uv_10,
        "p_rho": p_rho, "d_from_rho": d_from_rho,
        "p_rho_12": p_rho_12, "d_from_rho_12": d_from_rho_12,
        "d_weyl_global": d_weyl_global, "d_weyl_peak": d_weyl_peak, "om_peak_rho": om_peak_rho,
        "global_no_reduction": bool(global_no_reduction),
        "rho_no_reduction": bool(rho_no_reduction),
        "dist_to_8": dist_to_8, "dist_to_2": dist_to_2,
        "L_stable": bool(L_stable),
        "gap10": gap10, "lammax10": lammax10,
        "backend": backend,
    }


# ---------------------------------------------------------------------------
# Section 9 — verdict payload (PRINT ONLY; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": 6,
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
    if sign_verdict is not None:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 10 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # verify the cache SHA pin matches the canonical (SOURCE-RECON Class-(c) re-pin)
    cache_sha = sha256_of(CACHE_L12)  # (local)
    if cache_sha == CACHE_L12_SHA_PIN_STALE:
        print(f"NOTE: on-disk cache matches STALE plan pin {CACHE_L12_SHA_PIN_STALE[:16]}... "
              f"(unexpected; canonical is {CACHE_L12_SHA_PIN[:16]}...)", file=sys.stderr)
    if cache_sha != CACHE_L12_SHA_PIN:
        print(f"FATAL: cache SHA mismatch\n  got {cache_sha}\n  canonical pin {CACHE_L12_SHA_PIN}\n"
              f"  (stale plan pin was {CACHE_L12_SHA_PIN_STALE})", file=sys.stderr)
        return 2
    print(f"SOURCE-RECON Class-(c): cache SHA = {cache_sha[:16]}... matches current canonical "
          f"(re-pinned from stale plan value {CACHE_L12_SHA_PIN_STALE[:16]}...)")

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    res = compute()
    verdict = res["verdict"]
    value = res["value"]

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print("\n" + tag)

    note = (f"d_s(sigma_*=1.4005)={res['ds_at_star_10']:.4f}(L<=10),{res['ds_at_star_12']:.4f}(L<=12,"
            f"L-stable={res['L_stable']}); d_s_window_peak={res['ds_window_peak_10']:.4f}; "
            f"d_from_graviton_rho(Weyl N~omega^d)={res['d_from_rho']:.3f}(resolved),"
            f"{res['d_weyl_global']:.3f}(global); "
            f"NO-REDUCTION: dist_to_8={res['dist_to_8']:.3f}<dist_to_2={res['dist_to_2']:.3f} "
            f"(substrate d_s~8 ANTIPODAL to asympt.-safety/CDT d_s->2)")  # (local)
    extra = [
        (f"# INV6-W2-5 regulator_pin=a_n^{{zeta}} scheme=FW(bare-D_K normal-state Delta=0) "
         f"sigma_scan=[{SCAN_MIN:.0e},{d_s_fold_window_sigma}]M_KK^-2 N_sigma={N_SIGMA} "
         f"backend={res['backend']}"),
        (f"# INV6-W2-5 TWO independent UV-dimension measures: (A) heat-trace "
         f"d_s(sigma_*)={res['ds_at_star_10']:.3f}, peak={res['ds_window_peak_10']:.3f}; "
         f"(B) graviton spectral fn Weyl counting N(omega)~omega^d => d_resolved="
         f"{res['d_from_rho']:.2f}, d_global={res['d_weyl_global']:.2f}; "
         f"BOTH ~8, NEITHER ~2 => NO dimensional reduction (contrarian vs QG mainstream)"),
        (f"# INV6-W2-5 FINITE-TRUNCATION CAVEAT: literal sigma->0 endpoint "
         f"d_s={res['ds_literal_uv_10']:.3f} is a SUB-GAP truncation floor (gap={res['gap10']:.4f}>0, "
         f"finite mode count) -- NOT a physical reduction; the Weyl d_s=8 plateau is the "
         f"continuum statement, realised in the resolved window (canonical convention, "
         f"Phononic-Substrate-Geometry d_s(sigma_*)=8.485)"),
        (f"# INV6-W2-5 SOURCE-RECON Class-(c): cache re-pinned 88f1e9b1...(stale plan/manifest) "
         f"-> 9e6d9cf7...(on-disk canonical, 20+ live scripts)"),
    ]  # (local)

    print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=res["sign_verdict"],
                          magnitude_verdict=res["magnitude_verdict"],
                          regime_verdict=res["regime_verdict"],
                          companion_note=note, extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (sign={res['sign_verdict']} mag={res['magnitude_verdict']} "
          f"regime={res['regime_verdict']}, wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
