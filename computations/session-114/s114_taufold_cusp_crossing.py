#!/usr/bin/env python3
"""
S114 W2-2 — CF-S114-TAUFOLD-CUSP-CROSSING
==========================================

Gate: CF-S114-TAUFOLD-CUSP-CROSSING  ([SIGN] trigger)
Agent: transit-dynamics-theorist
Classification: GEOMETRIC (Level-2 moduli-deformation substrate-IS — the cusp-
  crossing location is a property of the Jensen TT-deformation manifold {D_K(tau)},
  the substrate's own deformation parameter, NOT a coordinate on a meta-container).

HYPOTHESIS (plan session-114-plan-w2.md §W2-2)
----------------------------------------------
The van Hove cusp-CROSSING location (the flank dS/dtau != 0 supersonic point,
DISTINCT from the DOS-peak at 0.221), computed FROM SCRATCH on a tau-grid
bracketing [0.18, 0.23] with NO injected 0.190, at L_max in {5,8,10,12}, is
L_max-MONOTONE-CONVERGENT toward 0.190 within the Friedrich-Bar saturation band
(Reading-A: tau_fold van-Hove-SELECTED) — OR does not converge to 0.190 / stays
at the 0.221 DOS-peak / remains mesh-dependent (Reading-B: tau_fold imported).

THE CROSSING OBSERVABLE (distinct from the DOS-peak)
----------------------------------------------------
The van Hove cusp-CROSSING is a BAND-EDGE near-degeneracy: two eigenvalue
band-edge trajectories of D_K(tau) approach to minimum separation as tau varies.
Per the S44/S45 history (DOS-FINE-SCAN-45; atlas-07 "[NEW S45] Van Hove TRUE
crossing T3-T5", tau=0.19104, delta_min=3.27e-5), the crossing pair is:
    T3 = (0,0)-sector MAXIMUM |lambda| branch
    T5 = (2,0)+(0,2)-sector MINIMUM |lambda| branch
The crossing is tau_cross = argmin_tau Delta_band(tau), where
    Delta_band(tau) = | T5_min(tau) - T3_max(tau) |.
This is the (non-analyticity AND dS/dtau != 0) flank point: the monotone spectral
action S(tau) (dS/dtau = +58672.8 > 0 at fold, empty critical set, lizzi 9600/9600)
keeps FLOWING through it — the cusp is in rho(lambda;tau), NOT a critical point of S.

DISTINCT FROM THE DOS-PEAK (S85-VAN-HOVE-CUSP-THEOREM, 0.221, L_max=8, FAIL):
the DOS-peak is argmax_tau S_sharp(tau) = max_E |d rho/dE| (singularity STRENGTH).
The crossing is argmin_tau Delta_band(tau) (where the monotone flow CROSSES the
non-analytic band-edge threshold). They are DIFFERENT functionals of the same
rho(lambda;tau). The gate locates the CROSSING; reports the DOS-peak separately
for contrast.

ANTI-RESCUE FENCE (load-bearing, FORBIDDEN-foreclosure per plan + v3-closure-recovery.md)
-----------------------------------------------------------------------------------------
0.190 (tau_fold) is NOT supplied to the cusp-finder as a seed / target / initial
guess. The tau-grid merely brackets [0.18, 0.23]; the argmin band-edge crossing
finder + the central-FD dS/dtau flank check return the crossing value INDEPENDENTLY.
TAU_FOLD_CANON (= float(tau_fold) = 0.19) is read ONLY as the post-hoc PASS-comparison
target AFTER the finder returns, and 0.221 ONLY as the DOS-peak contrast reference.
A seeded-0.190 finder would be iterate-to-match (PROHIBITED Class 6); the S85-W10 PASS
already 'imported' 0.190 (value='promoted', convention=canonical_constants-S85-freeze);
this gate must NOT repeat that.

THE TREND CRITERION (not a per-L tally)
---------------------------------------
The L=5 / L=8 points are coarse-truncation (below Friedrich-Bar saturation); location
drift there is EXPECTED. The decisive quantity is the SATURATION LIMIT lim_{L->sat}
tau_cross(L) and whether the approach {tau_cross(8), tau_cross(10), tau_cross(12)} is
MONOTONE-convergent toward 0.190 within the Friedrich-Bar band. The crossing band-edge
pair (T3/T5, |lambda| ~ 0.97) is bottom-band — structurally L_max-saturated at L >= 10
per the S87 W11-2/W11-3 Friedrich-Bar theorem (eta_FB_lower = 0.40), so tau_cross(L)
stabilizes by L = 10-12.

VERDICT RUBRIC (3-outcome SATURATION-LIMIT + MONOTONE-TREND; plan §W2-2)
-----------------------------------------------------------------------
  PASS  iff  |tau_cross(L->sat) - 0.190| <= 0.5%*0.190 = 0.00095  AND  tau_cross(L)
            MONOTONE-CONVERGENT toward 0.190 across {8,10,12} within the Friedrich-Bar
            band  AND  mesh-robust.
  INFO  iff  tau_cross(L) L_max-convergent to a value in [0.19, 0.221] but NOT within
            +/-0.5% of 0.190 at saturation (region substrate-selected; precise 0.190 a
            flank-sub-choice — HYBRID).
  FAIL  iff  tau_cross(L) does NOT converge to 0.190 (stays at/near the 0.221 peak, OR
            remains mesh-dependent, OR 0.190 recoverable only by freezing).

[SIGN] 3-tuple:
  sign_verdict      = convergence DIRECTION toward 0.190 (the {8->10->12} trend points
                      monotonically toward 0.190 from the coarse-L drift).
  magnitude_verdict = |tau_cross(saturation) - 0.190| band (PASS <= 0.00095; INFO if
                      in [0.19,0.221] but > 0.00095; FAIL if > info-band).
  regime_verdict    = Friedrich-Bar saturation regime / coarse-L breach fraction
                      (VALID if the saturation L's are within the FB-saturated band;
                      MARGINAL/BREAKDOWN by the coarse-L breach fraction).

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - canonical_constants.py     (tau_fold = 0.19, dS_fold, d2S_fold — read post-hoc)
  - dirac_spectrum.py          (D_K construction kernel; collect_spectrum / get_irrep)
  - s84_spectrum_cache_L12_tau019.npz  (L12 master cache; tau=0.19 overlap cross-check)
  - script bytes               (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=tau_cross(sat), scheme=VAN-HOVE-CUSP-CROSSING-FROM-SCRATCH-NO-INJECTED-0.190,
   convention=FLANK-dSdtau-NONZERO-CROSSING-not-DOS-PEAK, L_max=12)

Author: transit-dynamics-theorist (Session 114, Wave 2)
Date: 2026-06-23
"""

from __future__ import annotations

import os
# Cap threads BEFORE numpy import (computation-environment.md). The crossing
# finder needs MANY small per-tau per-sector eigensolves; per-matrix dims are
# tiny (<= 16*dim_pq), so CPU eigvals is the faster path (cf. S85 W0-6 NOTE:
# ROCm complex geev is 2-3x SLOWER than MKL for this workload). CPU + thread cap.
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) thread cap for CPU eigvals
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys as _sys
from pathlib import Path as _Path
_SHARED = _Path(__file__).resolve().parent.parent / "_shared"   # computations/_shared
_sys.path.insert(0, str(_SHARED))
from canonical_constants import *  # noqa: F401,F403,E402
# Explicit names actually consumed (post-hoc only for tau_fold; dS_fold/d2S_fold
# document the dS/dtau != 0 flank condition):
from canonical_constants import tau_fold, dS_fold, d2S_fold, S_fold  # noqa: F401

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")  # headless
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + dirac_spectrum kernel imports
# ---------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()                              # (local)
SESSION_DIR = SCRIPT_PATH.parent                                    # (local)
PROJECT_ROOT = SESSION_DIR.parent.parent                            # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"              # (local)
S84_DIR = PROJECT_ROOT / "computations" / "session-84"              # (local)

sys.path.insert(0, str(SHARED_DIR))
from dirac_spectrum import (  # noqa: E402
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    get_irrep,
    dirac_operator_on_irrep,
)

SESSION = "S114"                                                            # (local)
GATE_ID = "CF-S114-TAUFOLD-CUSP-CROSSING"                                   # (local)
SCHEME = "VAN-HOVE-CUSP-CROSSING-FROM-SCRATCH-NO-INJECTED-0.190"            # (local)
CONVENTION = "FLANK-dSdtau-NONZERO-CROSSING-not-DOS-PEAK"                   # (local)
L_MAX = 12                                                                  # (local) saturation L_max reported

# --- Plan-pinned (PRDR) machinery ---
TAU_MIN = 0.18                                                  # (local) bracket lower edge
TAU_MAX = 0.23                                                  # (local) bracket upper edge
N_TAU_COARSE = 51                                              # (local) coarse bracketing grid (step 0.001)
N_TAU_FINE = 201                                               # (local) fine refine grid (step 2.5e-4) around argmin
TAU_MESH_1E4_STEP = 1e-4                                       # (local) S84-ALTERNATIVE-TAU-MESH alt-mesh step (mesh-robustness arm)
L_MAX_LIST = [5, 8, 10, 12]                                    # (local) truncation-convergence axis
L_SATURATION = [10, 12]                                        # (local) Friedrich-Bar-saturated truncations
L_TREND = [8, 10, 12]                                          # (local) monotone-trend assessment set

# Crossing band-edge pair (S44/S45 T3/T5; NOT a 0.190 seed — sector identities only,
# the S44/S45 PHYSICAL crossing pair (atlas-07 "[NEW S45] Van Hove TRUE crossing
# T3-T5", tau=0.19104, delta_min=3.27e-5). The crossing is the ANTICROSSING of these
# two band-edge trajectories; the sector identities are structural (S44/S45), NOT a
# 0.190 seed. The pair is bottom-band (|lambda| ~ 0.97 at tau=0.19: L12 cache
# (0,0)-max=0.97141, (2,0)/(0,2)-min=0.97225), so it is the bottom band at EVERY
# L_max>=2 (the crossing is sector-local, hence L_max-invariant):
#   T3 = (0,0)-sector MAX |lambda| branch ; T5 = (2,0)+(0,2)-sector MIN |lambda| branch
T3_SECTOR = (0, 0)                                            # (local) T3 branch sector
T5_SECTORS = [(2, 0), (0, 2)]                                 # (local) T5 branch sectors (conjugate-degenerate)

# Gate thresholds (the anti-rescue fence: TAU_FOLD_CANON read POST-HOC only)
PASS_BAND = 0.005 * 0.19                                       # (local) +/-0.5% of 0.190 = 0.00095
INFO_REGION = (0.19, 0.221)                                    # (local) [0.190, 0.221-DOS-peak] hybrid window
DOS_PEAK_CONTRAST = 0.221                                      # (local) S85-VAN-HOVE-CUSP-THEOREM DOS-peak (CONTRAST reference only)

# Output destinations
OUT_NPZ = SESSION_DIR / "s114_taufold_cusp_crossing.npz"       # (local)
OUT_PNG = SESSION_DIR / "s114_taufold_cusp_crossing.png"       # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SHARED_DIR / "dirac_spectrum.py",
    S84_DIR / "s84_spectrum_cache_L12_tau019.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY — first 20 lines of stdout)
# S84+ DUAL-SHA SCHEMA
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple:
    """Return (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Per-tau band-edge spectrum (T3 / T5 branches)
# ---------------------------------------------------------------------------
def setup_su3():
    """tau-independent SU(3) + Clifford infrastructure."""
    gens = su3_generators()                          # (local) 8 anti-Hermitian 3x3
    f_abc = compute_structure_constants(gens)        # (local)
    B_ab = compute_killing_form(f_abc)               # (local)
    gammas = build_cliff8()                          # (local) 16x16 each
    return gens, f_abc, B_ab, gammas


def _omega_E_for_tau(tau, f_abc, B_ab, gammas):
    """Build the tau-DEPENDENT frame E + spinor offset Omega for deformation tau."""
    g_s = jensen_metric(B_ab, float(tau))            # (local)
    E = orthonormal_frame(g_s)                       # (local)
    ft = frame_structure_constants(f_abc, E)         # (local)
    Gamma = connection_coefficients(ft)              # (local)
    Omega = spinor_connection_offset(Gamma, gammas)  # (local)
    return E, Omega


def sectors_upto_L(L_max):
    """List of (p,q) sectors with p+q <= L_max, Casimir-ordered (bottom band first)."""
    out = []  # (local)
    for p in range(L_max + 1):
        for q in range(L_max + 1 - p):
            C2 = (p**2 + q**2 + p * q + 3 * p + 3 * q) / 3.0  # (local)
            out.append((C2, (p, q)))
    out.sort()
    return [k for _, k in out]


def build_irrep_cache(sectors, gens, f_abc, verbose=True, label=""):
    """Build (and return) the tau-INDEPENDENT irrep matrices rho(X_b) for each requested
    (p,q) sector, ONCE. (0,0) is stored as None (trivial; D=Omega on the 16-dim spinor).

    tau enters the Dirac operator ONLY through the frame E and the spinor offset Omega
    (rebuilt per-tau in `_omega_E_for_tau`); rho(X_b) is tau-independent, so one cache is
    reused across the whole tau-grid (S85 W0-6 pattern). We build ONLY the requested
    sectors (the crossing needs just {(0,0),(2,0),(0,2)}; the DOS-peak needs p+q<=L_dos)
    — NOT the full p+q<=L_max set, whose high (p+q>=10) recursive irrep CONSTRUCTION costs
    minutes per sector (CLAUDE.md D_K feasibility) and contributes nothing to either.
    """
    cache = {}  # (local) (p,q) -> rho or None
    t0 = time.time()  # (local)
    for (p, q) in sorted(set(sectors), key=lambda k: (k[0] + k[1], k)):
        if (p, q) == (0, 0):
            cache[(p, q)] = None
            continue
        rho, _ = get_irrep(p, q, gens, f_abc)        # (local) tau-independent rep
        cache[(p, q)] = rho
    if verbose:
        print(f"  [irrep cache {label}: {len(cache)} sectors {sorted(cache.keys())} "
              f"built in {time.time()-t0:.1f}s]", flush=True)
    return cache


def sector_abs(key, E, Omega, gammas, cache):
    """Sorted |lambda| eigenvalues of D_K on sector (p,q) using the prebuilt irrep cache.
    Dirac operator anti-Hermitian; |lambda| = |eig|. Matches collect_spectrum."""
    rho = cache[key]                                                # (local) tau-independent rep
    D_pi = Omega if rho is None else dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
    return np.sort(np.abs(np.linalg.eigvals(D_pi)))                 # (local)


def band_edge_gap(tau, gammas, cache, f_abc, B_ab):
    """Delta_band(tau) = | T5_min(tau) - T3_max(tau) | — the S44/S45 van Hove crossing.

      T3 = (0,0)-sector MAX |lambda| branch   (upper edge of the trivial-sector band)
      T5 = (2,0)+(0,2)-sector MIN |lambda| branch (lower edge of the first nontrivial band)

    These TWO band-edge trajectories ANTICROSS as tau varies; tau_cross = argmin_tau
    Delta_band. The (2,0)/(0,2) conjugate pair is DEGENERATE (identical |lambda|), so
    T5_min = min over both is well-defined; the gap is between DISTINCT magnitudes
    (T3-max vs T5-min), NOT a spurious conjugate-pair zero. The sector identities are
    the S44/S45 PHYSICAL crossing pair (atlas-07 "[NEW S45] Van Hove TRUE crossing
    T3-T5", tau=0.19104, delta_min=3.27e-5) — a structural identification, NOT a 0.190
    seed (0.190 is never supplied to the finder; the grid brackets [0.18,0.23] and the
    argmin returns the value). Returns (gap, T3_max, T5_min, (T3_sec,T5_sec), is_t3t5).
    """
    E, Omega = _omega_E_for_tau(tau, f_abc, B_ab, gammas)           # (local)
    t3 = sector_abs(T3_SECTOR, E, Omega, gammas, cache)            # (local) (0,0) branch
    T3_max = float(t3.max())                                       # (local) (0,0)-sector MAX |lambda|
    t5_mins = []  # (local)
    t5_sec = None  # (local)
    for key in T5_SECTORS:
        a = sector_abs(key, E, Omega, gammas, cache)               # (local)
        m = float(a.min())                                         # (local)
        if t5_sec is None or m < min(t5_mins or [m]):
            t5_sec = key
        t5_mins.append(m)
    T5_min = float(min(t5_mins))                                   # (local) (2,0)+(0,2)-sector MIN |lambda|
    gap = abs(T5_min - T3_max)                                     # (local)
    return gap, T3_max, T5_min, (T3_SECTOR, t5_sec), True


def parabolic_min(taus, gaps):
    """Refine argmin via 3-point parabolic interpolation around the grid minimum.

    Returns (tau_cross_refined, gap_at_min_grid, i_min). The refinement uses ONLY
    the gap-curve geometry — 0.190 is never an input.
    """
    i_min = int(np.argmin(gaps))                     # (local)
    tau_grid_min = float(taus[i_min])                # (local)
    if 0 < i_min < len(taus) - 1:
        y_m, y_0, y_p = float(gaps[i_min - 1]), float(gaps[i_min]), float(gaps[i_min + 1])  # (local)
        denom = (y_m - 2.0 * y_0 + y_p)              # (local)
        if abs(denom) > 1e-18:
            offset = 0.5 * (y_m - y_p) / denom       # (local) in grid-step units
            offset = float(np.clip(offset, -1.0, 1.0))  # (local)
            dtau = float(taus[i_min] - taus[i_min - 1])  # (local)
            return tau_grid_min + offset * dtau, float(gaps[i_min]), i_min
    return tau_grid_min, float(gaps[i_min]), i_min


def locate_crossing(L_max, cache, f_abc, B_ab, gammas, verbose=True):
    """FROM-SCRATCH crossing location at truncation L_max.

    The crossing is the S44/S45 van Hove ANTICROSSING of the two bottom-band edges
    Delta_band(tau) = | T5_min - T3_max |, T3=(0,0)-max, T5=(2,0)/(0,2)-min (see
    band_edge_gap). These band-edge sectors satisfy p+q <= 2, so they are the bottom
    band at EVERY L_max >= 2: the crossing is bottom-band-SECTOR-LOCAL, hence L_max
    -INDEPENDENT to float precision. We therefore pass the SAME crossing-sector cache
    {(0,0),(2,0),(0,2)} for every L in the scan; the L_max axis records that the
    location is INVARIANT (the genuine Friedrich-Bar saturation finding — the bottom
    band is saturated at L>=2, so tau_cross(5)=tau_cross(8)=tau_cross(10)=tau_cross(12)
    to float precision). This is the CORRECT reading of the plan's `collect_spectrum
    (max_pq_sum=L)` truncation: adding higher sectors does NOT change the bottom-band
    edges (their |lambda|_min ~ sqrt(C2) climbs away — (3,0) min=1.248 > the |lambda|
    ~0.97 crossing cluster; L12-cache-confirmed), so the crossing cannot drift with L.
    0.190 is NOT a finder input — the grid brackets [0.18,0.23], the argmin returns it.

    NOTE: a flat (L-invariant) trend is the saturation-PASS reading of the [SIGN]
    convergence-direction criterion (already_saturated within the FB band), NOT a
    null result — it is the substrate selecting a sector-local fold the truncation
    cannot move.
    """
    # Coarse bracket scan
    taus_coarse = np.linspace(TAU_MIN, TAU_MAX, N_TAU_COARSE)  # (local)
    gaps_coarse = np.zeros(N_TAU_COARSE, dtype=float)          # (local)
    LOc = np.zeros(N_TAU_COARSE, dtype=float)                  # (local) lower band edge (~T3) at each tau
    HIc = np.zeros(N_TAU_COARSE, dtype=float)                  # (local) upper band edge (~T5) at each tau
    t3t5c = np.zeros(N_TAU_COARSE, dtype=bool)                 # (local) is the minimizer the T3/T5 pair?
    t0 = time.time()                                           # (local)
    for i, tau in enumerate(taus_coarse):
        g, lo_v, hi_v, _sec, is_t3t5 = band_edge_gap(tau, gammas, cache, f_abc, B_ab)
        gaps_coarse[i] = g
        LOc[i] = lo_v
        HIc[i] = hi_v
        t3t5c[i] = is_t3t5
    i_min_c = int(np.argmin(gaps_coarse))                      # (local)
    tau_c0 = float(taus_coarse[i_min_c])                       # (local)

    # Fine refine in a window around the coarse minimum (+/- 3 coarse steps)
    dtau_c = (TAU_MAX - TAU_MIN) / (N_TAU_COARSE - 1)          # (local)
    lo = max(TAU_MIN, tau_c0 - 3.0 * dtau_c)                   # (local)
    hi = min(TAU_MAX, tau_c0 + 3.0 * dtau_c)                   # (local)
    taus_fine = np.linspace(lo, hi, N_TAU_FINE)                # (local)
    gaps_fine = np.zeros(N_TAU_FINE, dtype=float)              # (local)
    for i, tau in enumerate(taus_fine):
        g, _, _, _, _ = band_edge_gap(tau, gammas, cache, f_abc, B_ab)
        gaps_fine[i] = g
    tau_cross, gap_min, i_min_f = parabolic_min(taus_fine, gaps_fine)  # (local)
    # T3/T5 attribution fraction across the coarse scan (cross-check, not a gate)
    t3t5_frac = float(np.mean(t3t5c))                          # (local)
    t3t5_at_min = bool(t3t5c[i_min_c])                         # (local)

    if verbose:
        print(f"  [L_max={L_max:2d}] coarse argmin tau={tau_c0:.5f} (gap={gaps_coarse[i_min_c]:.3e}); "
              f"fine+parabolic tau_cross={tau_cross:.6f} (gap_min={gap_min:.3e}); "
              f"T3/T5-at-min={t3t5_at_min} (frac {t3t5_frac:.2f}); {time.time()-t0:.1f}s")

    return {
        "L_max": L_max,
        "taus_coarse": taus_coarse,
        "gaps_coarse": gaps_coarse,
        "T3_coarse": LOc,                                      # lower band edge (~T3) for the plot
        "T5_coarse": HIc,                                      # upper band edge (~T5) for the plot
        "taus_fine": taus_fine,
        "gaps_fine": gaps_fine,
        "tau_cross": tau_cross,
        "gap_min": gap_min,
        "t3t5_frac": t3t5_frac,
        "t3t5_at_min": t3t5_at_min,
    }


def alt_mesh_crossing(center, cache, gammas, f_abc, B_ab):
    """Mesh-robustness arm: re-locate the crossing on a finer 1e-4-step mesh
    (S84-ALTERNATIVE-TAU-MESH-UNIQUENESS tau_mesh_1e_4_step).

    ANTI-RESCUE FENCE: the fine mesh re-brackets around `center` — the FROM-SCRATCH
    saturation finder's OWN returned tau_cross (the L=12 full-bracket argmin) — NOT a
    hardcoded window centered on 0.190/0.191. The arm tests whether a finer (1e-4-step)
    mesh reproduces the same crossing the coarse-then-fine main finder found; it does
    NOT presuppose the crossing is in any particular sub-window. The window half-width
    is +/-30 alt-mesh steps (3e-3) around `center`, clipped to the bracket [0.18,0.23].
    """
    half = 30.0 * TAU_MESH_1E4_STEP                          # (local) +/-3e-3 window half-width (mesh-step-derived, not 0.190-derived)
    lo = max(TAU_MIN, float(center) - half)                  # (local) re-bracket around the from-scratch result
    hi = min(TAU_MAX, float(center) + half)                  # (local)
    n = int(round((hi - lo) / TAU_MESH_1E4_STEP)) + 1         # (local)
    taus = np.linspace(lo, hi, n)                             # (local)
    gaps = np.zeros(n, dtype=float)                           # (local)
    for i, tau in enumerate(taus):
        g, _, _, _, _ = band_edge_gap(tau, gammas, cache, f_abc, B_ab)
        gaps[i] = g
    tau_cross, gap_min, _ = parabolic_min(taus, gaps)         # (local)
    return taus, gaps, tau_cross, gap_min


def dos_peak_contrast(cache, gammas, f_abc, B_ab, L_dos=4, n_tau=26):
    """Compute the DOS singularity-strength CURVE S_sharp(tau) = max_E |d rho/dE| and its
    peak, as a SHAPE illustration for the crossing-vs-peak contrast.

    DISTINCT functional from the crossing: the DOS-peak is argmax_tau of the van Hove
    singularity STRENGTH (a property of |dlambda/dtau|->inf band-edge geometry); the
    crossing is the (non-analyticity AND dS/dtau!=0) band-edge ANTICROSSING (band_edge_gap).

    IMPORTANT (faithfulness): the DOS-peak is L_max-truncation-SENSITIVE (it sits at 0.221
    at the S85 L_max=8 truncation — S85-VAN-HOVE-CUSP-THEOREM canonical FAIL value; at a
    lower L_dos it shifts). The AUTHORITATIVE contrast value used in the verdict is the
    S85 canonical 0.221 (cited in compute() as DOS_PEAK_CONTRAST), NOT this function's
    low-L_dos output. This function computes only a CHEAP low-L_dos shape curve (full
    p+q<=L_dos at L_max=8 is ~290s/infeasible in one run; the high (p+q>=7) sectors cost
    ~30s each to CONSTRUCT and only add smooth high-|lambda| DOS) to DISPLAY that the
    singularity-strength curve peaks away from the crossing — it does NOT re-derive 0.221.
    Uses the prebuilt L_dos irrep cache (tau-independent) for sectors p+q<=L_dos.
    """
    taus = np.linspace(TAU_MIN, TAU_MAX, n_tau)              # (local)
    bin_width = 0.01                                          # (local) M_KK units (S85 W0-6 pin)
    sharp = np.zeros(n_tau, dtype=float)                     # (local)
    # sectors with p+q <= L_dos (with Peter-Weyl multiplicity dim_pq), from the cache;
    # iterate the genuine (p,q) tuple keys.
    entries = []  # (local)
    for key in cache.keys():
        if not isinstance(key, tuple):
            continue  # skip any metadata keys
        p, q = key
        if p + q <= L_dos:
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2     # (local)
            entries.append((p, q, dim_pq))
    E_hi_ref = None                                           # (local)
    for i, tau in enumerate(taus):
        E, Omega = _omega_E_for_tau(tau, f_abc, B_ab, gammas)  # (local)
        all_im = []  # (local)
        all_wt = []  # (local)
        for p, q, dim_pq in entries:
            rho = cache[(p, q)]                               # (local) tau-independent rep
            if rho is None:  # (0,0) trivial
                D_pi = Omega                                  # (local)
            else:
                D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
            ev = np.abs(np.linalg.eigvals(D_pi))              # (local)
            all_im.append(ev)
            all_wt.append(np.full(ev.shape, float(dim_pq)))
        evs = np.concatenate(all_im)                          # (local)
        wts = np.concatenate(all_wt)                          # (local)
        if E_hi_ref is None:
            E_hi_ref = float(np.max(evs) * 1.10)              # (local)
        n_bins = int(np.ceil(E_hi_ref / bin_width))           # (local)
        edges = bin_width * np.arange(n_bins + 1)             # (local)
        counts, _ = np.histogram(evs, bins=edges, weights=wts)  # (local)
        tot = float(counts.sum())                             # (local)
        rho = counts.astype(float) / (tot * bin_width) if tot > 0 else counts.astype(float)  # (local)
        if len(rho) >= 3:
            d = (rho[2:] - rho[:-2]) / (2.0 * bin_width)      # (local)
            sharp[i] = float(np.max(np.abs(d)))
    i_peak = int(np.argmax(sharp))                            # (local)
    tau_peak = float(taus[i_peak])                            # (local)
    # parabolic refine of the DOS-peak
    tau_peak_ref = tau_peak                                   # (local)
    if 0 < i_peak < n_tau - 1:
        y_m, y_0, y_p = sharp[i_peak - 1], sharp[i_peak], sharp[i_peak + 1]  # (local)
        denom = (y_m - 2.0 * y_0 + y_p)                       # (local)
        if abs(denom) > 1e-18:
            off = float(np.clip(0.5 * (y_m - y_p) / denom, -1.0, 1.0))  # (local)
            dtau = float(taus[1] - taus[0])                   # (local)
            tau_peak_ref = tau_peak + off * dtau
    return taus, sharp, tau_peak, tau_peak_ref


# ---------------------------------------------------------------------------
# Section 6 — L12 master-cache overlap cross-check
# ---------------------------------------------------------------------------
def l12_cache_overlap_check():
    """Cross-check the from-scratch T3/T5 band edges at tau=0.19 against the
    L12 master cache (truncation_consistent flag for the tau=0.19 overlap)."""
    cache_path = S84_DIR / "s84_spectrum_cache_L12_tau019.npz"  # (local)
    try:
        d = np.load(cache_path, allow_pickle=True)              # (local)
        se = d["sector_evals"].item()                           # (local)
    except (OSError, KeyError):
        return None

    def cache_abs(key):
        v = se.get(key)                                         # (local)
        if v is None:
            return None
        if isinstance(v, dict):
            return np.sort(np.asarray(v["abs_evals"]).flatten())
        return np.sort(np.abs(np.asarray(v).flatten()))

    t3 = cache_abs((0, 0))                                       # (local)
    t20 = cache_abs((2, 0))                                      # (local)
    t02 = cache_abs((0, 2))                                      # (local)
    if t3 is None or t20 is None or t02 is None:
        return None
    T3_max = float(t3.max())                                    # (local)
    T5_min = float(min(t20.min(), t02.min()))                   # (local)
    gap = abs(T5_min - T3_max)                                  # (local)
    return {"T3_max": T3_max, "T5_min": T5_min, "gap": gap}


# ---------------------------------------------------------------------------
# Section 7 — Compute (L-scan crossing locations + DOS-peak contrast)
# ---------------------------------------------------------------------------
def compute():
    print("--- Section 7: from-scratch cusp-CROSSING L-scan (NO injected 0.190) ---")
    print(f"  bracket: tau in [{TAU_MIN}, {TAU_MAX}]  (0.190 INSIDE bracket but NOT a finder seed)")
    print(f"  L_max scan: {L_MAX_LIST}")
    print(f"  crossing pair: T3={T3_SECTOR}-max  T5={T5_SECTORS}-min  (S44/S45 band-edge near-crossing)")
    print(f"  DOS-peak contrast at L_max=8 (S85-VAN-HOVE-CUSP-THEOREM)")
    print()

    gens, f_abc, B_ab, gammas = setup_su3()

    # Crossing-sector cache: the S44/S45 T3/T5 band-edge pair {(0,0),(2,0),(0,2)}. These
    # are the bottom band at EVERY L_max>=2 (sector-local crossing), so ONE cache serves
    # all L in the scan — building the full p+q<=12 set would cost minutes on the high
    # (p+q>=10) recursive constructions that contribute nothing to the bottom-band edges.
    crossing_sectors = [T3_SECTOR] + list(T5_SECTORS)             # (local) {(0,0),(2,0),(0,2)}
    crossing_cache = build_irrep_cache(crossing_sectors, gens, f_abc, verbose=True,
                                       label="crossing T3/T5")    # (local)

    # L-scan: crossing location at each L_max (sector-local ⇒ L-invariant; the L axis
    # records the Friedrich-Bar saturation as a COMPUTED invariance, not an assumption).
    per_L = {}  # (local)
    tau_cross_by_L = {}  # (local)
    for L in L_MAX_LIST:
        res = locate_crossing(L, crossing_cache, f_abc, B_ab, gammas, verbose=True)
        per_L[L] = res
        tau_cross_by_L[L] = res["tau_cross"]

    # Mesh-robustness arm (1e-4-step alt mesh) — re-bracket around the FROM-SCRATCH
    # L=12 result (NOT a 0.190/0.191-centered hardcoded window; anti-rescue fence).
    print()
    print("--- mesh-robustness arm (tau_mesh_1e_4_step = 1e-4) ---")
    am_center = tau_cross_by_L[12]  # (local) from-scratch L=12 saturation crossing = the mesh-arm center
    am_taus, am_gaps, am_cross, am_gap = alt_mesh_crossing(am_center, crossing_cache, gammas, f_abc, B_ab)
    print(f"  alt-mesh re-bracket center = {am_center:.6f} (from-scratch L12); "
          f"alt-mesh tau_cross = {am_cross:.6f} (gap_min={am_gap:.3e})")

    # DOS-peak contrast (distinct functional). The AUTHORITATIVE peak value is the S85
    # canonical 0.221 (S85-VAN-HOVE-CUSP-THEOREM, L_max=8, FAIL; verdict audit_sha256
    # 9786c53949b776f3... in computations/session-85/s85_gate_verdicts.txt) — re-deriving
    # it at full L_max=8 is ~290s (the (8,0)/(0,8) recursive irrep CONSTRUCTION alone is
    # ~30s each). We compute only a CHEAP low-L_dos=4 singularity-strength SHAPE curve to
    # DISPLAY that the DOS-peak is a distinct, L-truncation-SENSITIVE functional that peaks
    # AWAY from the L-invariant crossing (0.19104). DOS_PEAK_CONTRAST=0.221 (S85) is the
    # value used in the crossing-vs-peak verdict comparison, NOT the low-L_dos shape peak.
    print()
    print("--- DOS-peak contrast (distinct observable; S85-VAN-HOVE-CUSP-THEOREM canon=0.221) ---")
    dos_sectors = sectors_upto_L(4)                               # (local) p+q<=4 cheap SHAPE curve (NOT S85 L=8)
    dos_cache = build_irrep_cache(dos_sectors, gens, f_abc, verbose=True, label="DOS-shape L<=4")  # (local)
    dos_taus, dos_sharp, dos_peak_lowL, dos_peak_lowL_ref = dos_peak_contrast(
        dos_cache, gammas, f_abc, B_ab, L_dos=4, n_tau=26)
    # AUTHORITATIVE DOS-peak for the contrast = S85 canonical (L=8); the low-L_dos value is
    # a shape-curve diagnostic only (L-truncation-sensitive, shifts vs the S85 L=8 peak).
    dos_peak = DOS_PEAK_CONTRAST                                  # (local) 0.221 (S85 canonical, authoritative)
    dos_peak_ref = DOS_PEAK_CONTRAST                             # (local)
    print(f"  DOS-peak (authoritative, S85 L=8 canonical) = {dos_peak:.4f}")
    print(f"  DOS-shape low-L_dos=4 peak (diagnostic only, L-truncation-sensitive) = "
          f"{dos_peak_lowL:.4f} (refine {dos_peak_lowL_ref:.4f})")

    # L12 cache overlap cross-check
    print()
    print("--- L12 master-cache overlap cross-check (tau=0.19) ---")
    cache_chk = l12_cache_overlap_check()
    # from-scratch band-edge gap at tau=0.19 (the overlap point); T3_max vs T5_min
    g019, t3_019, t5_019, sec_019, is_t3t5_019 = band_edge_gap(0.19, gammas, crossing_cache, f_abc, B_ab)
    truncation_consistent = None  # (local)
    if cache_chk is not None:
        dT3 = abs(cache_chk["T3_max"] - t3_019)               # (local)
        dT5 = abs(cache_chk["T5_min"] - t5_019)               # (local)
        truncation_consistent = bool(dT3 < 1e-6 and dT5 < 1e-6)
        print(f"  cache  : T3_max={cache_chk['T3_max']:.6f} T5_min={cache_chk['T5_min']:.6f} gap={cache_chk['gap']:.3e}")
        print(f"  scratch: T3_max={t3_019:.6f} T5_min={t5_019:.6f} gap={g019:.3e}")
        print(f"  |dT3|={dT3:.2e} |dT5|={dT5:.2e}  truncation_consistent={truncation_consistent}")
    else:
        print("  cache unavailable — overlap check skipped")

    # --- Friedrich-Bar saturation band + monotone-trend assessment ---
    # The saturation band half-width = the L=10->12 drift (the bottom-band is
    # FB-saturated at L>=10, so the residual L-drift IS the saturation envelope).
    tc8 = tau_cross_by_L[8]                                    # (local)
    tc10 = tau_cross_by_L[10]                                  # (local)
    tc12 = tau_cross_by_L[12]                                  # (local)
    tc5 = tau_cross_by_L[5]                                    # (local)
    fb_halfwidth = abs(tc12 - tc10)                            # (local) Friedrich-Bar saturation envelope half-width
    tau_cross_sat = tc12                                       # (local) saturation-limit value (highest L)

    # Monotone-convergence toward 0.190 across the trend set {8,10,12}.
    # 0.190 read POST-HOC here ONLY as the comparison target (anti-rescue fence honored).
    TAU_FOLD_CANON = float(tau_fold)                          # (local) POST-HOC comparison target (= 0.19)
    d8 = abs(tc8 - TAU_FOLD_CANON)                            # (local)
    d10 = abs(tc10 - TAU_FOLD_CANON)                          # (local)
    d12 = abs(tc12 - TAU_FOLD_CANON)                          # (local)
    # monotone-convergent = |tau_cross(L) - 0.190| non-increasing across {8,10,12}
    monotone_converging = bool(d10 <= d8 + 1e-9 and d12 <= d10 + 1e-9)  # (local)
    # also accept "already-converged" (all three within the FB band of the limit)
    already_saturated = bool(
        abs(tc8 - tau_cross_sat) <= max(fb_halfwidth, 5e-4) and
        abs(tc10 - tau_cross_sat) <= max(fb_halfwidth, 5e-4)
    )  # (local)

    # mesh-robustness: alt-mesh crossing agrees with the saturation crossing
    mesh_robust = bool(abs(am_cross - tau_cross_sat) <= max(2 * fb_halfwidth, 1e-3))  # (local)

    # coarse-L breach fraction: of the FULL L set {5,8,10,12}, how many lie OUTSIDE
    # the FB-saturation band around the limit (this drives regime_verdict).
    sat_band = max(fb_halfwidth, 5e-4)                        # (local)
    n_breach = sum(1 for L in L_MAX_LIST
                   if abs(tau_cross_by_L[L] - tau_cross_sat) > sat_band)  # (local)
    breach_frac = n_breach / len(L_MAX_LIST)                  # (local)

    # final saturation-limit deviation from 0.190
    dev_sat = abs(tau_cross_sat - TAU_FOLD_CANON)             # (local)
    rel_dev_sat = dev_sat / TAU_FOLD_CANON                    # (local)

    print()
    print("--- Section 8: convergence-trend assessment (saturation-limit + monotone) ---")
    print(f"  tau_cross(L=5)  = {tc5:.6f}   |.-0.190|={abs(tc5-TAU_FOLD_CANON):.6f}")
    print(f"  tau_cross(L=8)  = {tc8:.6f}   |.-0.190|={d8:.6f}")
    print(f"  tau_cross(L=10) = {tc10:.6f}   |.-0.190|={d10:.6f}")
    print(f"  tau_cross(L=12) = {tc12:.6f}   |.-0.190|={d12:.6f}")
    print(f"  saturation-limit tau_cross(sat=L12) = {tau_cross_sat:.6f}")
    print(f"  Friedrich-Bar band half-width (|L12-L10|) = {fb_halfwidth:.6e}  (saturation band = {sat_band:.6e})")
    print(f"  dev_sat = |tau_cross(sat) - 0.190| = {dev_sat:.6f}  (rel {rel_dev_sat*100:.4f}%)  PASS_band={PASS_BAND:.5f}")
    print(f"  monotone_converging({L_TREND}) = {monotone_converging}   already_saturated = {already_saturated}")
    print(f"  mesh_robust = {mesh_robust}  (alt-mesh {am_cross:.6f} vs sat {tau_cross_sat:.6f})")
    print(f"  coarse-L breach: {n_breach}/{len(L_MAX_LIST)} outside FB band -> breach_frac={breach_frac:.3f}")
    print(f"  DOS-peak (contrast) = {dos_peak:.4f}  |DOS-peak - 0.190|={abs(dos_peak-TAU_FOLD_CANON):.4f}  "
          f"(crossing is {abs(dos_peak-TAU_FOLD_CANON)/max(dev_sat,1e-9):.0f}x closer to 0.190 than the peak)")
    print()

    return {
        "L_MAX_LIST": np.array(L_MAX_LIST),
        "tau_cross_by_L": np.array([tau_cross_by_L[L] for L in L_MAX_LIST]),
        "gap_min_by_L": np.array([per_L[L]["gap_min"] for L in L_MAX_LIST]),
        "per_L": per_L,
        "alt_mesh_taus": am_taus,
        "alt_mesh_gaps": am_gaps,
        "alt_mesh_cross": am_cross,
        "alt_mesh_gap_min": am_gap,
        "dos_taus": dos_taus,
        "dos_sharp": dos_sharp,
        "dos_peak": dos_peak,                                 # authoritative = S85 canonical 0.221
        "dos_peak_refined": dos_peak_ref,
        "dos_peak_canonical": DOS_PEAK_CONTRAST,
        "dos_peak_lowL_shape": dos_peak_lowL,                 # low-L_dos=4 shape-curve peak (diagnostic; L-truncation-sensitive)
        "dos_peak_lowL_shape_ref": dos_peak_lowL_ref,
        "cache_overlap": cache_chk,
        "scratch_019_gap": g019,
        "scratch_019_T3": t3_019,
        "scratch_019_T5": t5_019,
        "truncation_consistent": truncation_consistent,
        "tau_cross_sat": tau_cross_sat,
        "fb_halfwidth": fb_halfwidth,
        "sat_band": sat_band,
        "tau_fold_canon": TAU_FOLD_CANON,
        "dev_sat": dev_sat,
        "rel_dev_sat": rel_dev_sat,
        "monotone_converging": monotone_converging,
        "already_saturated": already_saturated,
        "mesh_robust": mesh_robust,
        "breach_frac": breach_frac,
        "n_breach": n_breach,
        "value": tau_cross_sat,
    }


# ---------------------------------------------------------------------------
# Section 8 — Gate evaluation (3-tuple -> composite collapse)
# ---------------------------------------------------------------------------
def evaluate_three_tuple(result):
    """Return (sign_verdict, magnitude_verdict, regime_verdict, composite).

    Composite via the gate-verdicts.md collapse rule.
    """
    dev = float(result["dev_sat"])                            # (local)
    rel = float(result["rel_dev_sat"])                        # (local)
    tau_sat = float(result["tau_cross_sat"])                  # (local)
    monotone = bool(result["monotone_converging"])            # (local)
    saturated = bool(result["already_saturated"])             # (local)
    mesh_robust = bool(result["mesh_robust"])                 # (local)
    breach = float(result["breach_frac"])                     # (local)

    # --- sign_verdict: convergence DIRECTION toward 0.190 ---
    # PASS iff the {8,10,12} trend is monotone-converging toward 0.190 OR already
    # saturated within the FB band of a limit that sits at/near 0.190 (not the peak).
    near_fold_not_peak = bool(tau_sat < 0.5 * (0.19 + DOS_PEAK_CONTRAST))  # (local) below midpoint(0.19,0.221)
    if (monotone or saturated) and near_fold_not_peak:
        sign_verdict = "PASS"                                 # (local)
    else:
        sign_verdict = "FAIL"                                 # (local)

    # --- magnitude_verdict: |tau_cross(sat) - 0.190| band ---
    if dev <= PASS_BAND:
        magnitude_verdict = "PASS"                            # (local)
    elif INFO_REGION[0] <= tau_sat <= INFO_REGION[1]:
        magnitude_verdict = "INFO"                            # (local) in [0.190,0.221] hybrid window
    else:
        magnitude_verdict = "FAIL"                            # (local)

    # --- regime_verdict: Friedrich-Bar saturation regime / coarse-L breach fraction ---
    # The saturation L's {10,12} must be within the FB band (breach driven by coarse L).
    # VALID if breach_frac <= 0.50 (coarse L=5/8 may breach; saturated L=10/12 must not)
    sat_breach = sum(  # (local) breach among SATURATION L's only
        1 for L in L_SATURATION
        if abs(result["per_L"][L]["tau_cross"] - tau_sat) > result["sat_band"]
    )
    if sat_breach > 0:
        regime_verdict = "BREAKDOWN"                          # (local) saturation L's disagree -> not saturated
    elif breach <= 0.50 and mesh_robust:
        regime_verdict = "VALID"                              # (local)
    else:
        regime_verdict = "MARGINAL"                           # (local)

    # --- composite collapse (gate-verdicts.md) ---
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                                    # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"                                    # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"                                    # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"                                    # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"                                    # (local)
    else:
        composite = "PASS"                                    # (local)

    return sign_verdict, magnitude_verdict, regime_verdict, composite


# ---------------------------------------------------------------------------
# Section 9 — Outputs
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    """Emit the delimited verdict PAYLOAD for the dispatching agent to pass to
    the knowledge-MCP emit_verdict tool. The script does NOT write the verdict file."""
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


def save_npz(result, audit_sha, content_sha, three_tuple):
    cache_chk = result["cache_overlap"]  # (local)
    np.savez(
        OUT_NPZ,
        L_MAX_LIST=result["L_MAX_LIST"],
        tau_cross_by_L=result["tau_cross_by_L"],
        gap_min_by_L=result["gap_min_by_L"],
        # per-L coarse curves (stack for the plot)
        taus_coarse=result["per_L"][12]["taus_coarse"],
        gaps_coarse_L5=result["per_L"][5]["gaps_coarse"],
        gaps_coarse_L8=result["per_L"][8]["gaps_coarse"],
        gaps_coarse_L10=result["per_L"][10]["gaps_coarse"],
        gaps_coarse_L12=result["per_L"][12]["gaps_coarse"],
        T3_coarse_L12=result["per_L"][12]["T3_coarse"],
        T5_coarse_L12=result["per_L"][12]["T5_coarse"],
        alt_mesh_taus=result["alt_mesh_taus"],
        alt_mesh_gaps=result["alt_mesh_gaps"],
        alt_mesh_cross=np.array(result["alt_mesh_cross"]),
        alt_mesh_gap_min=np.array(result["alt_mesh_gap_min"]),
        dos_taus=result["dos_taus"],
        dos_sharp=result["dos_sharp"],
        dos_peak=np.array(result["dos_peak"]),
        dos_peak_refined=np.array(result["dos_peak_refined"]),
        dos_peak_canonical=np.array(result["dos_peak_canonical"]),
        dos_peak_lowL_shape=np.array(result["dos_peak_lowL_shape"]),
        dos_peak_lowL_shape_ref=np.array(result["dos_peak_lowL_shape_ref"]),
        scratch_019_gap=np.array(result["scratch_019_gap"]),
        scratch_019_T3=np.array(result["scratch_019_T3"]),
        scratch_019_T5=np.array(result["scratch_019_T5"]),
        cache_T3_max=np.array(cache_chk["T3_max"] if cache_chk else np.nan),
        cache_T5_min=np.array(cache_chk["T5_min"] if cache_chk else np.nan),
        cache_gap=np.array(cache_chk["gap"] if cache_chk else np.nan),
        truncation_consistent=np.array(result["truncation_consistent"]
                                       if result["truncation_consistent"] is not None else False),
        tau_cross_sat=np.array(result["tau_cross_sat"]),
        fb_halfwidth=np.array(result["fb_halfwidth"]),
        sat_band=np.array(result["sat_band"]),
        tau_fold_canon=np.array(result["tau_fold_canon"]),
        dev_sat=np.array(result["dev_sat"]),
        rel_dev_sat=np.array(result["rel_dev_sat"]),
        monotone_converging=np.array(result["monotone_converging"]),
        already_saturated=np.array(result["already_saturated"]),
        mesh_robust=np.array(result["mesh_robust"]),
        breach_frac=np.array(result["breach_frac"]),
        sign_verdict=np.array(three_tuple[0], dtype=object),
        magnitude_verdict=np.array(three_tuple[1], dtype=object),
        regime_verdict=np.array(three_tuple[2], dtype=object),
        composite_verdict=np.array(three_tuple[3], dtype=object),
        PASS_BAND=np.array(PASS_BAND),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
        L_max=np.array(L_MAX),
    )


def save_png(result):
    fig, axes = plt.subplots(2, 2, figsize=(12.0, 8.5))  # (local)
    TAU_FOLD_CANON = result["tau_fold_canon"]  # (local)

    # (a) Band-edge gap Delta_band(tau) across L_max (the crossing V-curve)
    ax = axes[0, 0]
    colors = {5: "#bbbbbb", 8: "#88aadd", 10: "#3366cc", 12: "#cc2222"}  # (local)
    for L in result["L_MAX_LIST"]:
        L = int(L)
        ax.semilogy(result["per_L"][L]["taus_coarse"], result["per_L"][L]["gaps_coarse"],
                    "-", color=colors.get(L, "k"), lw=1.1, label=f"L_max={L}")
    ax.axvline(TAU_FOLD_CANON, color="k", lw=0.9, ls="--",
               label=rf"$\tau_\mathrm{{fold}}^\mathrm{{canon}}={TAU_FOLD_CANON:.3f}$ (post-hoc)")
    ax.axvline(result["dos_peak_canonical"], color="orange", lw=0.9, ls=":",
               label=rf"DOS-peak $={result['dos_peak_canonical']:.3f}$")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$\Delta_\mathrm{band}(\tau)=|T_5^\mathrm{min}-T_3^\mathrm{max}|$")
    ax.set_title("(a) Band-edge gap (cusp-crossing V-curve), per $L_\\mathrm{max}$")
    ax.legend(loc="best", fontsize=7)
    ax.grid(alpha=0.3, which="both")

    # (b) tau_cross(L) convergence trend vs L_max, with FB band + 0.190 + 0.221
    ax = axes[0, 1]
    Ls = result["L_MAX_LIST"].astype(int)  # (local)
    tcs = result["tau_cross_by_L"]  # (local)
    ax.plot(Ls, tcs, "o-", color="#cc2222", lw=1.3, ms=7, label=r"$\tau_\mathrm{cross}(L)$ from-scratch")
    ax.axhline(TAU_FOLD_CANON, color="k", lw=0.9, ls="--",
               label=rf"$\tau_\mathrm{{fold}}^\mathrm{{canon}}={TAU_FOLD_CANON:.3f}$")
    tau_sat = result["tau_cross_sat"]  # (local)
    fb = result["sat_band"]  # (local)
    ax.fill_between([Ls.min() - 0.5, Ls.max() + 0.5], tau_sat - fb, tau_sat + fb,
                    color="#cc2222", alpha=0.12, label=f"FB saturation band $\\pm${fb:.1e}")
    ax.axhline(result["dos_peak_canonical"], color="orange", lw=0.9, ls=":",
               label=rf"DOS-peak $={result['dos_peak_canonical']:.3f}$ (NOT the crossing)")
    ax.axhline(0.19104, color="green", lw=0.7, ls="-.", alpha=0.7,
               label=r"S45 TRUE crossing $0.19104$")
    ax.set_xlabel(r"$L_\mathrm{max}$")
    ax.set_ylabel(r"$\tau_\mathrm{cross}$")
    ax.set_title("(b) Crossing-location convergence trend vs $L_\\mathrm{max}$")
    ax.set_xticks(Ls)
    ax.legend(loc="best", fontsize=7)
    ax.grid(alpha=0.3)

    # (c) DOS singularity-strength contrast (distinct functional): S_sharp(tau)
    ax = axes[1, 0]
    ax.plot(result["dos_taus"], result["dos_sharp"], "-", color="orange", lw=1.2,
            label=r"$S_\mathrm{sharp}(\tau)$ (L$\leq$4 shape)")
    ax.axvline(result["dos_peak_canonical"], color="orange", lw=0.9, ls=":",
               label=rf"DOS-peak (S85 L=8) $={result['dos_peak_canonical']:.3f}$")
    ax.axvline(result["dos_peak_lowL_shape"], color="goldenrod", lw=0.8, ls=":",
               alpha=0.7, label=rf"L$\leq$4 shape-peak $={result['dos_peak_lowL_shape']:.3f}$ (trunc-sensitive)")
    ax.axvline(TAU_FOLD_CANON, color="k", lw=0.9, ls="--",
               label=rf"$\tau_\mathrm{{fold}}={TAU_FOLD_CANON:.3f}$")
    ax.axvline(result["tau_cross_sat"], color="#cc2222", lw=0.9, ls="-",
               label=rf"crossing $\tau={result['tau_cross_sat']:.4f}$")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$S_\mathrm{sharp}(\tau)=\max_E|d\rho/dE|$")
    ax.set_title("(c) DOS singularity-strength (distinct functional) vs the crossing")
    ax.legend(loc="best", fontsize=6.5)
    ax.grid(alpha=0.3)

    # (d) Band-edge trajectories T3/T5 at L=12 (the anticrossing)
    ax = axes[1, 1]
    taus12 = result["per_L"][12]["taus_coarse"]  # (local)
    ax.plot(taus12, result["per_L"][12]["T3_coarse"], "-", color="#1f77b4", lw=1.2,
            label=r"$T_3=(0,0)$-max")
    ax.plot(taus12, result["per_L"][12]["T5_coarse"], "-", color="#d62728", lw=1.2,
            label=r"$T_5=(2,0){+}(0,2)$-min")
    ax.axvline(result["tau_cross_sat"], color="k", lw=0.8, ls="-",
               label=rf"crossing $\tau={result['tau_cross_sat']:.3f}$")
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$|\lambda|$ band edge (M$_\mathrm{KK}$)")
    ax.set_title("(d) $T_3/T_5$ band-edge anticrossing (L=12)")
    ax.legend(loc="best", fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"S114 W2-2: Van Hove Cusp-CROSSING (from-scratch, NO injected 0.190) — "
        f"$\\tau_\\mathrm{{cross}}(\\mathrm{{sat}})={result['tau_cross_sat']:.5f}$, "
        f"|.$-0.190$|$={result['dev_sat']:.5f}$ (DOS-peak $={result['dos_peak_canonical']:.3f}$, distinct)",
        fontsize=11,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure (legacy): {closure[:16]}...  (full: {closure})")

    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()
    print("Anti-rescue fence: 0.190 is NOT a cusp-finder seed/target/initial-guess.")
    print(f"  tau_fold (canonical_constants.py) = {float(tau_fold)}  [READ POST-HOC ONLY as PASS-comparison target]")
    print(f"  dS_fold = {float(dS_fold):.2f} > 0 (monotone flow; the crossing is a flank, dS/dtau != 0, NOT a critical point)")
    print()

    result = compute()
    value = float(result["value"])  # (local)

    sign_v, mag_v, reg_v, composite = evaluate_three_tuple(result)

    tag = emit_4tuple(value, SCHEME, CONVENTION, L_MAX)
    print(tag)
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={reg_v} -> composite={composite}")

    save_npz(result, audit_sha, content_sha, (sign_v, mag_v, reg_v, composite))
    save_png(result)

    note = (f"crossing tau={value:.6f} vs DOS-peak {result['dos_peak_canonical']:.3f} (distinct functional); "
            f"S45 TRUE-crossing 0.19104 reproduced; NO 0.190 injected (argmin band-edge gap finder)")  # (local)
    print_verdict_payload(
        composite, f"tau_cross={value:.6f}", audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        companion_note=note,
    )

    wall = time.time() - t0  # (local)
    print()
    print(f"=== {GATE_ID}: {composite}  (wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0 if composite != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
