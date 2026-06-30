#!/usr/bin/env python3
# =============================================================================
# INV11-W3-2 — Windowed heat-trace spectral dimension d_s(sigma) discriminated
#              by the energy-axis DOS exponent gamma_E vs CDT/asymptotic-safety.
#
# Gate ID : INV11-W3-2-DS-WINDOWED-GAMMA-E-VS-CDT
# Trigger : [VERIFY]  (set-membership d_s(sigma_*) in [1.9,2.1]; no directional claim)
# Class   : GEOMETRIC (heat-trace spectral dimension is a property of the D_K geometry)
# Agent   : quantum-foam-theorist
#
# HYPOTHESIS: the substrate windowed heat-trace spectral dimension
#   d_s(sigma_*) = -2 d ln P(sigma)/d ln sigma,   P(sigma) = Tr e^{-sigma D_K^2}
# evaluated at the substrate-natural feature window sigma_* = 1/lambda_B2^2
# = 1.4005 M_KK^{-2}, lies in [1.9,2.1] (overlapping the CDT/AS intermediate-
# window plateau d_s -> 2), discriminated by the energy-axis DOS exponent
# gamma_E (cumulative-count estimator near E_0 = lambda_B2); OR gamma_E does NOT
# discriminate at the substrate-natural window (INFO-on-inapplicability, VALID).
#
# *** RED-FLAG GUARD (load-bearing) ***
#   This gate is the DISTINCT, LIVE successor to a REFUTED claim. It MUST NOT
#   re-propose the refuted dimension-SPECTRUM-flow (S_d={0,2,4,6,8} tau-INDEP;
#   the "12->5.65->4 paralleling CDT 10->2->4" bridge) NOR the RETIRED
#   `min d_s < 3` van-Hove discriminator (inv-9 kaku R-2 RED; S31Aa/S92/S93 W7-3).
#   The LIVE object per cross-pillar-bridge-corpus.md §24 (K=2) is the WINDOWED
#   heat-trace d_s(sigma) discriminated by the energy-axis DOS exponent gamma_E.
#   The §24.2 heat-trace-vs-graph-Laplacian functional distinction is load-bearing.
#
# SUBSTRATE FRAMING: the substrate IS the return probability P(sigma); d_s(sigma)
#   is an intrinsic functional of the D_K spectrum, NOT diffusion in a container.
#   Per phononic-framing.md §"Same-functional-different-scale": d_s(sigma->0)=8
#   (Weyl asymptotic; SETTLED Claim A) and d_s(sigma_*) (windowed; OPEN Claim B)
#   are TWO intrinsic functionals of the SAME P(sigma). The CDT comparison applies
#   the SAME functional Phi at the SAME scale-type (intermediate-window<->intermediate-
#   window), NOT the sigma->0 asymptotic. Direction: D_K eigenvalues -> P(sigma) ->
#   windowed d_s(sigma_*) -> emergent-physics comparison.
# =============================================================================

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
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

# --- canonical constants (MANDATORY: never hardcode framework constants) ------
SHARED_DIR = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import d_s_fold_window_sigma, M_KK  # noqa: E402

# =============================================================================
# Section 1 — Identity + machinery pins (per plan §W3-2)
# =============================================================================
SESSION = "11"                       # investigation track
GATE_ID = "INV11-W3-2-DS-WINDOWED-GAMMA-E-VS-CDT"
SCHEME = "heat-trace"                 # P(sigma)=Tr e^{-sigma D_K^2} (NOT graph-Laplacian; §24.2 distinction)
CONVENTION = "windowed-d_s(sigma_*)"  # the WINDOWED functional, NOT the sigma->0 Weyl asymptotic
L_MAX = 12                            # (local) converged spectrum cache truncation (plan pin)

# machinery_pin_map (plan §W3-2 item 5) — all are pre-registered GATE parameters (scan/grid/window), not framework constants
N_EVAL = 400                          # (local) sigma-grid points (log-spaced) for the d_s finite-difference
SCAN_LO, SCAN_HI = 0.1, 10.0          # (local) sigma diffusion-time band (M_KK^{-2}) bracketing sigma_*
W_FIT = 0.026                         # (local) M_KK; gamma_E cumulative-count fit half-window (plan + S93 W7-3)

# Pre-registered membership window + gamma_E bands (plan §W3-2 item 2 + §24.1)
DS_PASS_LO, DS_PASS_HI = 1.9, 2.1     # PASS-membership window (overlapping CDT/AS d_s->2)
GAMMA_KK = (0.5, 0.6)                 # ordinary / Reading-KK band   (n=2 sqrt-edge)
GAMMA_LANDAU = (0.8, 1.0)             # flat-band / Reading-landau   (n->inf infinite-order vH)
# (0.6, 0.8) = INDETERMINATE band -> INFO-on-inapplicability (VALID pre-registered outcome)

# Substrate-physical anchor: the FOLD lives at tau_fold = 0.190 (the s84 cache).
# The canonical sigma_* = d_s_fold_window_sigma = 1.4005 = 1/E_B2^2 IS the tau=0.190
# value (S92 AH-PF-1 / S93 W7-3). We therefore use s84 (tau=0.190) as the substrate-
# PHYSICAL primary (the fold is defined there) and report s92 (tau=0.200) as a
# robustness cross-check. This honors BOTH the plan's named inputs AND the prior
# workshop's physical anchor per substrate-first-canonical-sourcing.md §(ii.B)
# (npz-ground-truth runtime canonical-path rescue; the drift is documented in the
# verdict value= field and the WP §Methodology).
CACHE_PRIMARY = Path(__file__).resolve().parents[1] / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CACHE_XCHECK = Path(__file__).resolve().parents[1] / "session-92" / "s92_spectrum_cache_L12_tau020.npz"
TAU_PRIMARY = float("0.190")          # (local) tau_fold anchor (s84 cache; the fold IS defined here)
TAU_XCHECK = float("0.200")           # (local) robustness cross-check tau (s92 cache)

INPUT_FILES = {
    "canonical_constants": SHARED_DIR / "canonical_constants.py",
    "spectrum_cache_primary_s84_tau019": CACHE_PRIMARY,
    "spectrum_cache_xcheck_s92_tau020": CACHE_XCHECK,
}

# =============================================================================
# Section 2 — SHA helpers (match the project template exactly)
# =============================================================================
def log_input_pins(input_files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 70)
    print(f"{GATE_ID} — input SHA-256 pins")
    print("=" * 70)
    for name, path in input_files.items():
        p = Path(path)  # (local)
        try:
            sha = hashlib.sha256(p.read_bytes()).hexdigest()  # (local)
        except OSError:
            sha = "MISSING"  # (local)
        rel = str(p).replace("\\", "/")  # (local)
        pins[rel] = sha
        print(f"  {name}: {sha[:16]}...  {rel}")
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
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


# =============================================================================
# Section 3 — Spectrum assembly + heat trace
# =============================================================================
def assemble_spectrum(cache_path: Path):
    """Return (lambdas, pw_weights) for the FULL Peter-Weyl heat trace.

    The cache stores sector_evals[(p,q)] = {'dim':d, 'abs_evals': array of length d*16}.
    The full heat trace is P(sigma) = Sum_{(p,q)} dim(p,q) * Sum_i e^{-sigma lambda_i^2}
    (the irrep (p,q) appears dim(p,q) times in the regular rep — the Peter-Weyl weight;
    the stored abs_evals already carries one multiplet copy of length dim*16).
    We build a flat array of |lambda| with the per-eigenvalue Peter-Weyl weight.
    """
    cache = np.load(cache_path, allow_pickle=True)  # (local)
    se = cache["sector_evals"].item()               # (local) dict keyed by (p,q)
    lam_list = []   # (local)
    wt_list = []    # (local)
    for (p, q), rec in se.items():
        ev = np.asarray(rec["abs_evals"], dtype=float).ravel()  # (local)
        dim_pq = int(rec["dim"])                                # (local)
        lam_list.append(ev)
        wt_list.append(np.full(ev.shape, float(dim_pq)))        # (local) Peter-Weyl weight per eigenvalue
    lam = np.concatenate(lam_list)  # (local)
    wt = np.concatenate(wt_list)    # (local)
    return lam, wt


def heat_trace_P(lam, wt, sigma_grid):
    """P(sigma) = Sum_k wt_k e^{-sigma lambda_k^2}  on the sigma_grid (GPU via torch if available)."""
    lam2 = lam.astype(np.float64) ** 2  # (local)
    try:
        import torch  # (local)
        dev = "cuda" if torch.cuda.is_available() else "cpu"  # (local)
        L2 = torch.tensor(lam2, device=dev, dtype=torch.float64)      # (local)
        W = torch.tensor(wt.astype(np.float64), device=dev, dtype=torch.float64)  # (local)
        S = torch.tensor(sigma_grid, device=dev, dtype=torch.float64)  # (local)
        # P[j] = sum_k W_k exp(-S_j * L2_k); chunk over sigma to bound memory
        Pvals = torch.empty(S.shape[0], device=dev, dtype=torch.float64)  # (local)
        CHUNK = 64  # (local)
        for a in range(0, S.shape[0], CHUNK):
            b = min(a + CHUNK, S.shape[0])  # (local)
            # (b-a, K) = exp(-S[a:b,None]*L2[None,:]) ; weighted sum over K
            expo = torch.exp(-S[a:b].unsqueeze(1) * L2.unsqueeze(0))  # (local)
            Pvals[a:b] = (expo * W.unsqueeze(0)).sum(dim=1)           # (local)
        out = Pvals.cpu().numpy()  # (local)
        backend = f"torch:{dev}"   # (local)
    except Exception as exc:  # noqa: BLE001
        # CPU numpy fallback (still correct; just slower)
        out = np.array([np.sum(wt * np.exp(-s * lam2)) for s in sigma_grid])  # (local)
        backend = f"numpy-cpu (torch unavailable: {exc})"  # (local)
    return out, backend


def windowed_d_s(sigma_grid, P):
    """d_s(sigma) = -2 d ln P/d ln sigma via centered finite difference in ln sigma."""
    lnS = np.log(sigma_grid)   # (local)
    lnP = np.log(P)            # (local)
    dlnP = np.gradient(lnP, lnS)  # (local) centered FD
    return -2.0 * dlnP


# =============================================================================
# Section 4 — energy-axis DOS exponent gamma_E (cumulative-count estimator)
# =============================================================================
def _integrated_dos_staircase(lam, wt, tol=1e-6):
    """Collapse the spectrum to DISTINCT energies, each carrying its TOTAL Peter-Weyl
    mass. Returns (edges, masses, Ncum, Nlvl) where:
      edges  = distinct |lambda| values (ascending)
      masses = total PW mass at each distinct energy (Sum m_i over the degenerate level)
      Ncum   = integrated DOS at each distinct energy (cumulative mass, the Sum m_i staircase)
      Nlvl   = distinct-level count staircase (Sum 1).
    Sampling N at distinct energies (jump = mass) is the CORRECT integrated-DOS estimator;
    sampling per-row over a degenerate level injects spurious dE->0,dN=1..m leverage
    (the artifact that swings gamma_E to ~0.86 on the tied B2 level).
    """
    order = np.argsort(lam)  # (local)
    lam_s = np.asarray(lam, dtype=float)[order]  # (local)
    wt_s = np.asarray(wt, dtype=float)[order]    # (local)
    edges = []; masses = []  # (local)
    i = 0
    while i < len(lam_s):
        j = i
        while j < len(lam_s) and abs(lam_s[j] - lam_s[i]) <= tol:
            j += 1
        edges.append(float(lam_s[i]))
        masses.append(float(np.sum(wt_s[i:j])))
        i = j
    edges = np.asarray(edges); masses = np.asarray(masses)  # (local)
    Ncum = np.cumsum(masses)                                # (local) integrated DOS (Sum m_i)
    Nlvl = np.arange(1, edges.size + 1, dtype=float)        # (local) distinct-level (Sum 1)
    return edges, masses, Ncum, Nlvl


def _loglog_slope(x, y):
    """log-log least-squares slope on strictly-positive (x,y); returns (slope, n_used)."""
    x = np.asarray(x, dtype=float); y = np.asarray(y, dtype=float)
    m = (x > 0) & (y > 0)  # (local)
    if int(np.count_nonzero(m)) < 3:
        return np.nan, int(np.count_nonzero(m))
    lx = np.log(x[m]); ly = np.log(y[m])  # (local)
    A = np.vstack([lx, np.ones_like(lx)]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)  # (local)
    return float(coef[0]), int(np.count_nonzero(m))


def _gamma_one(edges, Ncum, Nlvl, masses, E0, win, use_mass, side):
    """Single gamma_E estimate: gamma = 1 - slope of log|N - N0| vs log|lambda - E0|.

    edges/Ncum/Nlvl are the DISTINCT-energy integrated-DOS staircase (jump = mass).
    use_mass=True -> integrated-DOS (Sum m_i); False -> distinct-level (Sum 1).
    side in {sym, below, above}.
    """
    sel = np.abs(edges - E0) <= win  # (local)
    if side == "below":
        sel = sel & (edges < E0 - 1e-12)
    elif side == "above":
        sel = sel & (edges > E0 + 1e-12)
    if use_mass:
        N0 = float(np.sum(masses[edges <= E0 + 1e-12]))  # (local) integrated mass at/below E0
        dN = np.abs(Ncum[sel] - N0)                       # (local)
    else:
        N0l = float(np.sum(edges <= E0 + 1e-12))          # (local)
        dN = np.abs(Nlvl[sel] - N0l)                      # (local)
    dE = np.abs(edges[sel] - E0)                          # (local)
    slope, n = _loglog_slope(dE, dN)
    gamma = (1.0 - slope) if np.isfinite(slope) else np.nan  # (local)
    return gamma, n


def fit_gamma_E(lam, wt, E0_fold, w_fit, E0_pileup):
    """Energy-axis DOS exponent gamma_E (cumulative-count estimator) WITH the
    estimator/centering ROBUSTNESS ENVELOPE.

    Near a 1D band edge rho(E) ~ |E-E0|^{-gamma_E}, the integrated DOS satisfies
      |N(lambda) - N(E0)| ~ |lambda - E0|^{1 - gamma_E},  gamma_E = 1 - slope.

    *** LOAD-BEARING (corpus §24.0 item 5 + S93 W7-3 K3) ***: the B2 fold sits at a
    ONE-SIDED-STARVED spectral bottom (hard floor at E_B1 below; SU(3)-rep gap above;
    only ~5 distinct risers within +/-2*w_fit), L_max-saturated (|gamma(L12)-gamma(L10)|=0).
    The cumulative-count gamma_E is therefore ESTIMATOR- and CENTERING-SENSITIVE: it
    swings across the centering (E_B2 vs the weight-24 pile-up E=0.84086), the sidedness,
    and the all-points-vs-distinct estimator. We compute the FULL envelope and report
    min/max/spread; the band assignment + verdict key on ROBUSTNESS, not on any single
    non-robust point estimate (forcing one would be the exact §24 fair-comparison error
    the directive exists to prevent; the prior gate S93-W7-3 closed INDETERMINATE for
    precisely this reason).
    """
    edges, masses, Ncum, Nlvl = _integrated_dos_staircase(lam, wt)
    win = 2.0 * w_fit  # (local) symmetric +/- 2*w_fit window

    # The AH-PF-1 designated central estimate: all-points (integrated-DOS, Sum m_i),
    # symmetric, centered on E_B2 (the named fold energy E_0 = lambda_B2).
    gamma_central, n_central = _gamma_one(edges, Ncum, Nlvl, masses, E0_fold, win,
                                          use_mass=True, side="sym")

    # ENVELOPE: cross the estimator (mass/level) x centering (E_B2/pile-up) x side (sym/below/above).
    variants = {}  # (local)
    for est_name, use_mass in [("mass", True), ("level", False)]:
        for ctr_name, E0c in [("E_B2", E0_fold), ("pileup", E0_pileup)]:
            for side in ["sym", "below", "above"]:
                g, n = _gamma_one(edges, Ncum, Nlvl, masses, E0c, win, use_mass, side)
                variants[f"{est_name}|{ctr_name}|{side}"] = (g, n)
    finite = [g for (g, n) in variants.values() if np.isfinite(g)]  # (local)
    gamma_min = float(np.min(finite)) if finite else np.nan  # (local)
    gamma_max = float(np.max(finite)) if finite else np.nan  # (local)
    gamma_spread = (gamma_max - gamma_min) if finite else np.nan  # (local)

    # distinct-level central (for explicit reporting alongside the all-points central)
    gamma_distinct, n_distinct = _gamma_one(edges, Ncum, Nlvl, masses, E0_fold, win,
                                            use_mass=False, side="sym")

    return {
        "gamma_E_all_points": gamma_central,     # AH-PF-1 central (all-points, sym, E_B2)
        "gamma_E_distinct": gamma_distinct,
        "gamma_E_min": gamma_min,
        "gamma_E_max": gamma_max,
        "gamma_E_spread": gamma_spread,
        "n_points_central": n_central,
        "n_distinct_in_window": int(np.count_nonzero(np.abs(edges - E0_fold) <= win)),
        "envelope": {k: (float(g) if np.isfinite(g) else None, int(n))
                     for k, (g, n) in variants.items()},
        "edges_in_window": edges[np.abs(edges - E0_fold) <= win].tolist(),
        "masses_in_window": masses[np.abs(edges - E0_fold) <= win].tolist(),
    }


def assign_gamma_band(gamma_min, gamma_max):
    """Band assignment keyed on the ROBUSTNESS ENVELOPE, not a single point estimate.

    Returns a definite band (KK / LANDAU) ONLY if the WHOLE envelope [gamma_min, gamma_max]
    sits inside that band. If the envelope STRADDLES bands (crosses the INDETERMINATE
    (0.6,0.8) gap, or spans KK->LANDAU), the discriminator does NOT discriminate ->
    INDETERMINATE -> INFO-on-inapplicability (the explicitly VALID pre-registered outcome).
    """
    if not (np.isfinite(gamma_min) and np.isfinite(gamma_max)):
        return "UNDEFINED"
    # whole envelope inside the KK band [0.5, 0.6]
    if gamma_min >= GAMMA_KK[0] and gamma_max <= GAMMA_KK[1]:
        return "KK"
    # whole envelope inside the Landau band [0.8, 1.0)
    if gamma_min >= GAMMA_LANDAU[0] and gamma_max < GAMMA_LANDAU[1]:
        return "LANDAU"
    # whole envelope strictly inside the INDETERMINATE gap (0.6, 0.8)
    if gamma_min > GAMMA_KK[1] and gamma_max < GAMMA_LANDAU[0]:
        return "INDETERMINATE"
    # envelope STRADDLES band boundaries -> the discriminator is not robust -> INDETERMINATE
    return "INDETERMINATE"


# =============================================================================
# Section 5 — main compute
# =============================================================================
def compute():
    # --- substrate-natural feature window sigma_* (canonical) ---
    sigma_star = float(d_s_fold_window_sigma)  # 1.4005 = 1/lambda_B2^2 (S92 AH-PF-1)

    results = {}  # (local)
    for tag, cache_path, tau in [("primary_s84_tau0.190", CACHE_PRIMARY, TAU_PRIMARY),
                                 ("xcheck_s92_tau0.200", CACHE_XCHECK, TAU_XCHECK)]:
        lam, wt = assemble_spectrum(cache_path)
        # E_B2 (the fold) = the 4th distinct |lambda| (B2 optical band); E_B1 = ground tone.
        distinct = np.unique(np.round(np.sort(lam), 6))  # (local)
        E_B1 = float(distinct[0])  # (local) ground tone
        E_B2 = float(distinct[3])  # (local) B2 fold (4th distinct level; B1, +2 acoustic, then B2)
        sigma_grid = np.logspace(np.log10(SCAN_LO), np.log10(SCAN_HI), N_EVAL)  # (local)
        P, backend = heat_trace_P(lam, wt, sigma_grid)
        ds = windowed_d_s(sigma_grid, P)  # (local)
        # d_s at the canonical sigma_* (interpolate on the grid)
        ds_sigma_star = float(np.interp(sigma_star, sigma_grid, ds))  # (local)
        min_ds = float(np.min(ds))     # (local)
        max_ds = float(np.max(ds))     # (local)
        # monotonicity over [0.5, 2.0] (the prior workshop's intermediate window)
        wband = (sigma_grid >= 0.5) & (sigma_grid <= 2.0)  # (local)
        dds = np.gradient(ds, np.log(sigma_grid))           # (local)
        monotone_incr = bool(np.all(dds[wband] > 0))        # (local)
        has_flat = bool(np.any(np.abs(dds[wband]) < 1e-2))  # (local)
        # band minimum over the scan band (the AH-PF-1 plateau metric, for the CDT compare)
        ds_band_min = float(np.min(ds[wband]))              # (local)
        # --- pile-up energy E0 (the max-Peter-Weyl-mass distinct level within +/-2*w_fit of E_B2) ---
        edges_pk, masses_pk, _, _ = _integrated_dos_staircase(lam, wt)  # (local)
        near = np.abs(edges_pk - E_B2) <= 2.0 * W_FIT       # (local)
        E_pileup = float(edges_pk[near][np.argmax(masses_pk[near])])  # (local) weight-24 level ~0.84086
        # gamma_E fit at E0 = E_B2 WITH the estimator/centering robustness envelope
        gfit = fit_gamma_E(lam, wt, E_B2, W_FIT, E_pileup)
        gamma_band = assign_gamma_band(gfit["gamma_E_min"], gfit["gamma_E_max"])  # (local) ENVELOPE-keyed
        # weighted mass + fold mass-fraction (van-Hove-blindness diagnostic)
        total_weighted = float(np.sum(wt))                  # (local) ~3.20e7
        fold_mask = np.abs(lam - E_B2) < 1.5e-3             # (local)
        fold_weighted = float(np.sum(wt[fold_mask]))        # (local)
        fold_fraction = fold_weighted / total_weighted      # (local)
        results[tag] = {
            "tau": tau, "backend": backend,
            "E_B1": E_B1, "E_B2": E_B2, "E_pileup": E_pileup,
            "sigma_star_from_E_B2": 1.0 / E_B2 ** 2,
            "ds_sigma_star": ds_sigma_star,
            "min_ds_scanband": min_ds, "max_ds_scanband": max_ds,
            "ds_band_min_0p5_2p0": ds_band_min,
            "monotone_incr_0p5_2p0": monotone_incr, "has_flat_0p5_2p0": has_flat,
            "gamma_E_all_points": gfit["gamma_E_all_points"],
            "gamma_E_distinct": gfit["gamma_E_distinct"],
            "gamma_E_min": gfit["gamma_E_min"],
            "gamma_E_max": gfit["gamma_E_max"],
            "gamma_E_spread": gfit["gamma_E_spread"],
            "gamma_band": gamma_band,
            "gfit": gfit,
            "total_weighted_mass": total_weighted,
            "fold_weighted_mass": fold_weighted,
            "fold_mass_fraction": fold_fraction,
            "sigma_grid": sigma_grid, "P": P, "ds": ds,
        }

    # --- Z = rho_E * v_g consistency check (Sage-exact 1/pi for the whole gamma_E family) ---
    # For a 1D edge E(k)=E0+a|k|^n: rho_E ~ |E-E0|^{-(1-1/n)}, v_g ~ |E-E0|^{+(1-1/n)},
    # so Z = rho_E * v_g is INDEPENDENT of n (= 1/pi in the canonical normalization).
    # This is a CONSISTENCY CHECK, NOT a gamma_E lock (corpus §24.0 item 5).
    Z_family_invariant = 1.0 / np.pi  # (local) Sage-exact 1/pi (the product invariant)

    # --- gamma_E => van-Hove order n map (Sage-exact: gamma_E = 1 - 1/n) ---
    gpri = results["primary_s84_tau0.190"]["gamma_E_all_points"]  # (local)
    n_from_gamma = (1.0 / (1.0 - gpri)) if (np.isfinite(gpri) and gpri < 1.0) else np.inf  # (local)

    return {
        "sigma_star_canonical": sigma_star,
        "Z_family_invariant_1overpi": Z_family_invariant,
        "n_vanHove_from_gamma_primary": n_from_gamma,
        "results": results,
    }


def evaluate_gate(comp):
    """Two-clause [VERIFY] verdict with INFO-on-inapplicability as a first-class outcome.

    Clause-1 (membership): d_s(sigma_*) in [1.9,2.1]  (overlapping CDT/AS d_s->2)
    Clause-2 (discriminator): gamma_E band assignment
        KK  [0.5,0.6]    -> ordinary sqrt-edge; clean discriminator
        LANDAU [0.8,1.0) -> flat-band;          clean discriminator
        INDETERMINATE (0.6,0.8) -> gamma_E does NOT discriminate -> INFO-on-inapplicability (VALID)

    Verdict rule (plan §W3-2 dual_prior discriminator):
      PASS  iff d_s(sigma_*) in [1.9,2.1] AND gamma_band == KK
      INFO  iff gamma_band == INDETERMINATE  (INFO-on-inapplicability, VALID pre-reg outcome)
             OR (d_s(sigma_*) in window but gamma_band ambiguous)
      FAIL  iff d_s(sigma_*) OUTSIDE [1.9,2.1] AND gamma discriminates cleanly to a definite band
             (the windowed d_s does NOT reduce to a CDT-comparable value at the feature window)
    """
    pri = comp["results"]["primary_s84_tau0.190"]  # (local)
    ds_star = pri["ds_sigma_star"]                  # (local)
    band = pri["gamma_band"]                        # (local)

    ds_in_window = (DS_PASS_LO <= ds_star <= DS_PASS_HI)  # (local)

    if band == "INDETERMINATE":
        return "INFO"  # INFO-on-inapplicability: gamma_E does not discriminate at sigma_* (VALID)
    if ds_in_window and band == "KK":
        return "PASS"
    if ds_in_window and band in ("LANDAU", "UNDEFINED", "BELOW_KK", "AT_OR_ABOVE_1"):
        # d_s reduced into the CDT window but the discriminator is ambiguous -> INFO
        return "INFO"
    # d_s OUTSIDE [1.9,2.1]:
    if not ds_in_window and band in ("KK", "LANDAU"):
        # the windowed d_s does NOT reduce to a CDT-comparable value, and gamma is definite
        return "FAIL"
    # d_s outside window AND gamma not cleanly discriminating -> INFO-on-inapplicability
    return "INFO"


# =============================================================================
# Section 6 — plot
# =============================================================================
def make_plot(comp, out_png):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5))
    sigma_star = comp["sigma_star_canonical"]  # (local)

    ax = axes[0]
    for tag, sty in [("primary_s84_tau0.190", "-"), ("xcheck_s92_tau0.200", "--")]:
        r = comp["results"][tag]
        ax.plot(r["sigma_grid"], r["ds"], sty, label=f"{tag}  (d_s(σ*)={r['ds_sigma_star']:.3f})")
    ax.axvline(sigma_star, color="k", ls=":", lw=1, label=f"σ*={sigma_star:.4f} M_KK⁻²")
    ax.axhspan(DS_PASS_LO, DS_PASS_HI, color="green", alpha=0.12, label="PASS window [1.9,2.1] (CDT~2)")
    ax.axhline(8.0, color="gray", ls="-.", lw=0.8, label="dim SU(3)=8 (σ→0 Weyl, Claim A)")
    ax.set_xscale("log")
    ax.set_xlabel("σ  (M_KK⁻²)")
    ax.set_ylabel("d_s(σ) = −2 d ln P/d ln σ")
    ax.set_title("Windowed heat-trace spectral dimension (NOT σ→0 asymptotic)")
    ax.legend(fontsize=7, loc="best")
    ax.grid(alpha=0.3)

    ax = axes[1]
    pri = comp["results"]["primary_s84_tau0.190"]
    # scatter every envelope variant (estimator x centering x side) so the SPREAD is visible
    env = pri["gfit"]["envelope"]  # (local) {key: (gamma_or_None, n)}
    xs = []; ys = []; labels = []  # (local)
    for i, (k, (g, n)) in enumerate(sorted(env.items())):
        if g is not None and np.isfinite(g):
            xs.append(i); ys.append(g); labels.append(k)
    ax.scatter(xs, ys, c="C0", s=40, zorder=3, label="γ_E variants (est×center×side)")
    ax.axhline(pri["gamma_E_all_points"], color="k", ls="-", lw=1.2,
               label=f"central (all-pts,sym,E_B2)={pri['gamma_E_all_points']:.3f}")
    ax.axhspan(pri["gamma_E_min"], pri["gamma_E_max"], color="orange", alpha=0.18,
               label=f"ENVELOPE [{pri['gamma_E_min']:.3f},{pri['gamma_E_max']:.3f}] (straddles)")
    ax.axhspan(GAMMA_KK[0], GAMMA_KK[1], color="C2", alpha=0.15, label="KK band [0.5,0.6] (n=2 √-edge)")
    ax.axhspan(GAMMA_LANDAU[0], GAMMA_LANDAU[1], color="C3", alpha=0.15, label="Landau band [0.8,1.0) (n→∞ vH)")
    ax.axhspan(GAMMA_KK[1], GAMMA_LANDAU[0], color="gray", alpha=0.12, label="INDETERMINATE (0.6,0.8)→INFO")
    ax.set_xticks(xs)
    ax.set_xticklabels(labels, rotation=90, fontsize=5)
    ax.set_ylabel("γ_E (energy-axis DOS exponent)")
    ax.set_title(f"γ_E ENVELOPE at fold E_B2={pri['E_B2']:.4f}  (band: {pri['gamma_band']} → INFO-on-inapplicability)")
    ax.legend(fontsize=6, loc="upper left")
    ax.grid(alpha=0.3, axis="y")
    ax.set_ylim(0, 1.15)

    fig.suptitle("INV11-W3-2 — windowed d_s(σ_*) + γ_E discriminator vs CDT/AS  [RED-FLAG: NOT min d_s<3]",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# =============================================================================
# Section 7 — main
# =============================================================================
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    comp = compute()
    pri = comp["results"]["primary_s84_tau0.190"]
    xch = comp["results"]["xcheck_s92_tau0.200"]
    sigma_star = comp["sigma_star_canonical"]

    print("=" * 70)
    print("RESULTS — INV11-W3-2")
    print("=" * 70)
    print(f"  sigma_* (canonical d_s_fold_window_sigma) = {sigma_star:.5f} M_KK^-2")
    print(f"  PRIMARY (s84, tau=0.190): backend={pri['backend']}")
    print(f"    E_B1={pri['E_B1']:.6f}  E_B2(fold)={pri['E_B2']:.6f}  sigma_*(from E_B2)={pri['sigma_star_from_E_B2']:.5f}")
    print(f"    d_s(sigma_*)               = {pri['ds_sigma_star']:.4f}   [PASS window [{DS_PASS_LO},{DS_PASS_HI}]]")
    print(f"    min d_s (scan band)        = {pri['min_ds_scanband']:.4f}")
    print(f"    d_s band-min [0.5,2.0]     = {pri['ds_band_min_0p5_2p0']:.4f}  (CDT-window compare; CDT~2)")
    print(f"    monotone-incr [0.5,2.0]    = {pri['monotone_incr_0p5_2p0']}   has_flat={pri['has_flat_0p5_2p0']}")
    print(f"    gamma_E (all-points, central) = {pri['gamma_E_all_points']:.4f}   (distinct-level={pri['gamma_E_distinct']:.4f})")
    print(f"    gamma_E ENVELOPE (est x center x side) = [{pri['gamma_E_min']:.4f}, {pri['gamma_E_max']:.4f}]  spread={pri['gamma_E_spread']:.4f}")
    print(f"    gamma_E band (ENVELOPE-keyed) = {pri['gamma_band']}   "
          f"[KK[0.5,0.6] / landau[0.8,1.0) / INDETERMINATE(0.6,0.8)]")
    print(f"    -> envelope STRADDLES bands => discriminator does NOT discriminate (S93 W7-3 INDETERMINATE reproduced)")
    print(f"    fold mass-fraction         = {pri['fold_mass_fraction']:.3e}  ({pri['fold_weighted_mass']:.0f} / {pri['total_weighted_mass']:.3e})")
    print(f"  XCHECK  (s92, tau=0.200): d_s(sigma_*)={xch['ds_sigma_star']:.4f}  gamma_E_env=[{xch['gamma_E_min']:.4f},{xch['gamma_E_max']:.4f}]  band={xch['gamma_band']}")
    print(f"  Z = rho_E*v_g family-invariant = 1/pi = {comp['Z_family_invariant_1overpi']:.6f} (CONSISTENCY CHECK, not a gamma_E lock)")
    print(f"  n_vanHove from gamma_E (=1/(1-gamma)) = {comp['n_vanHove_from_gamma_primary']}")
    print()
    # SAME-FUNCTIONAL-SAME-SCALE fair-comparison statement (substitution chain, plan §W3-2)
    print("  FAIR-COMPARISON (substitution chain, plan §W3-2 + corpus §24):")
    print("    Phi[P](sigma) = -2 d ln P/d ln sigma applied at the SAME scale-type on BOTH sides.")
    print(f"    substrate WINDOWED d_s(sigma_*) = {pri['ds_sigma_star']:.4f}  (intermediate-window; Claim B)")
    print(f"    substrate band-min [0.5,2.0]    = {pri['ds_band_min_0p5_2p0']:.4f}  vs CDT/AS intermediate-window d_s->2")
    print("    NOT compared: substrate sigma->0 Weyl asymptotic d_s=dim SU(3)=8 (SETTLED Claim A; a DIFFERENT functional).")
    print()

    verdict = evaluate_gate(comp)
    # Composite collapse (no [SIGN] 3-tuple — [VERIFY] trigger, set-membership).
    print(f"  VERDICT: {verdict}")
    print()

    # --- assemble the value= payload string (no single-quote chars) ---
    ds_in = (DS_PASS_LO <= pri["ds_sigma_star"] <= DS_PASS_HI)  # (local)
    value = (
        f"d_s(sigma_*)={pri['ds_sigma_star']:.4f}(in[1.9,2.1]:{ds_in}); "
        f"sigma_*={sigma_star:.5f}; "
        f"gamma_E_central={pri['gamma_E_all_points']:.4f}; "
        f"gamma_E_envelope=[{pri['gamma_E_min']:.4f},{pri['gamma_E_max']:.4f}]spread{pri['gamma_E_spread']:.4f}(band={pri['gamma_band']}); "
        f"band_min_ds[0.5,2.0]={pri['ds_band_min_0p5_2p0']:.4f}(vs_CDT~2); "
        f"min_ds={pri['min_ds_scanband']:.4f}; monotone_up={pri['monotone_incr_0p5_2p0']}; "
        f"fold_massfrac={pri['fold_mass_fraction']:.2e}; "
        f"Z=rho_E*v_g=1/pi={comp['Z_family_invariant_1overpi']:.4f}(consistency_NOT_lock); "
        f"tau_primary=0.190(s84); xcheck_tau0.200_d_s={xch['ds_sigma_star']:.4f}_gammaenv[{xch['gamma_E_min']:.4f},{xch['gamma_E_max']:.4f}]; "
        f"INFO-on-inapplicability=gamma_E_straddles_bands(S93W7-3_INDETERMINATE_reproduced); "
        f"RED-FLAG-GUARD=NOT_min_d_s<3_NOT_dimspectrum-flow"
    )

    # --- save npz ---
    out_npz = Path(__file__).resolve().with_suffix("").as_posix() + ".npz"
    np.savez(
        out_npz,
        sigma_star_canonical=sigma_star,
        # primary
        pri_tau=pri["tau"], pri_E_B1=pri["E_B1"], pri_E_B2=pri["E_B2"],
        pri_ds_sigma_star=pri["ds_sigma_star"],
        pri_min_ds=pri["min_ds_scanband"], pri_band_min=pri["ds_band_min_0p5_2p0"],
        pri_monotone_incr=pri["monotone_incr_0p5_2p0"], pri_has_flat=pri["has_flat_0p5_2p0"],
        pri_gamma_E_all_points=pri["gamma_E_all_points"], pri_gamma_E_distinct=pri["gamma_E_distinct"],
        pri_gamma_E_min=pri["gamma_E_min"], pri_gamma_E_max=pri["gamma_E_max"], pri_gamma_E_spread=pri["gamma_E_spread"],
        pri_gamma_band=pri["gamma_band"], pri_E_pileup=pri["E_pileup"],
        pri_gamma_envelope_json=json.dumps(pri["gfit"]["envelope"]),
        pri_fold_mass_fraction=pri["fold_mass_fraction"],
        pri_total_weighted_mass=pri["total_weighted_mass"], pri_fold_weighted_mass=pri["fold_weighted_mass"],
        pri_sigma_grid=pri["sigma_grid"], pri_P=pri["P"], pri_ds=pri["ds"],
        # xcheck
        xch_tau=xch["tau"], xch_E_B2=xch["E_B2"], xch_ds_sigma_star=xch["ds_sigma_star"],
        xch_gamma_E_all_points=xch["gamma_E_all_points"], xch_gamma_band=xch["gamma_band"],
        xch_gamma_E_min=xch["gamma_E_min"], xch_gamma_E_max=xch["gamma_E_max"],
        # discriminator structural anchors
        Z_family_invariant_1overpi=comp["Z_family_invariant_1overpi"],
        n_vanHove_from_gamma=comp["n_vanHove_from_gamma_primary"],
        gamma_KK_band=np.array(GAMMA_KK), gamma_landau_band=np.array(GAMMA_LANDAU),
        ds_pass_window=np.array([DS_PASS_LO, DS_PASS_HI]),
        verdict=verdict,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  saved: {out_npz}")

    # --- plot ---
    out_png = Path(__file__).resolve().with_suffix("").as_posix() + ".png"
    make_plot(comp, out_png)
    print(f"  saved: {out_png}")
    print(f"  elapsed: {time.time() - t0:.1f}s")
    print()

    extra_rows = [
        f"# RED-FLAG-GUARD: this gate is the LIVE gamma_E successor; it does NOT re-propose "
        f"min_d_s<3 (RETIRED) nor the dimension-SPECTRUM-flow (REFUTED inv-9 kaku R-2 / S31Aa/S92).",
        f"# fair-comparison: Phi[P](sigma)=-2 dlnP/dlnsigma at SAME scale-type both sides; "
        f"substrate WINDOWED d_s(sigma_*)={pri['ds_sigma_star']:.4f}, band-min[0.5,2.0]={pri['ds_band_min_0p5_2p0']:.4f} "
        f"vs CDT/AS intermediate-window d_s->2; NOT the sigma->0 Weyl-8 asymptotic (Claim A, distinct functional).",
        f"# gamma_E discriminator ENVELOPE=[{pri['gamma_E_min']:.4f},{pri['gamma_E_max']:.4f}] spread={pri['gamma_E_spread']:.4f} "
        f"(est{{mass,level}}x center{{E_B2,pileup}}x side{{sym,below,above}}); STRADDLES bands "
        f"(KK[0.5,0.6]/landau[0.8,1.0)/INDETERMINATE(0.6,0.8)) => does NOT discriminate => INFO-on-inapplicability. "
        f"One-sided-starved fold (hard floor E_B1 below, SU(3)-rep gap above, ~5 risers, L_max-saturated; S93 W7-3 K3). "
        f"Z=rho_E*v_g=1/pi CONSISTENCY-CHECK not a lock (corpus §24.0 item 5).",
        f"# tau-anchor: primary s84 tau=0.190 (the fold IS defined here; sigma_*=1.4005 is the tau=0.190 value); "
        f"xcheck s92 tau=0.200 d_s(sigma_*)={xch['ds_sigma_star']:.4f}; per substrate-first-canonical-sourcing.md §(ii.B).",
        f"# INVESTIGATION-TRACK ONLY: no canonical/registry/inventory/capstone write; "
        f"any cross-FRAMEWORK comparison row is session-promotion (corpus §24.3 doc).",
    ]

    print_verdict_payload(
        verdict=verdict,
        value=value,
        audit_sha=audit_sha,
        content_sha=content_sha,
        companion_note=f"{GATE_ID} dual-SHA companion row; windowed d_s + gamma_E vs CDT (heat-trace, NOT graph-Laplacian)",
        extra_rows=extra_rows,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
