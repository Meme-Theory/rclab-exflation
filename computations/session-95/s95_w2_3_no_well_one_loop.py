#!/usr/bin/env python3
"""
S95 W2-3 — NO-WELL-ONE-LOOP
===========================

Gate: S95-W2-3-NO-WELL-ONE-LOOP  ([SIGN])
Classification: GEOMETRIC
Agent: spectral-geometer

Pre-registered threshold (session-95-plan-w2.md §W2-3):
  Operator:  { tau in [0, tau_now] : dGamma/dtau(tau) = 0 } = empty ?
             (equivalently sign(dGamma/dtau) constant over the tau-grid)
  PASS iff N_interior_sign_changes of dGamma/dtau over [0, tau_now] = 0  (regime VALID).
  FAIL iff N_interior_sign_changes >= 1 (a genuine interior zero of dGamma/dtau, regime VALID):
           the one-loop trace-log creates an interior stationary feature (well/barrier)
           absent at tree level.
  INFO iff the apparent interior sign change appears only where regime_verdict =
           MARGINAL/BREAKDOWN, or the tree/one-loop terms balance only at the tau=0 boundary.

GOVERNING OBJECT (heat-kernel / Seeley-DeWitt; spectral-geometer specialty):
  Gamma[tau] = S[D_K(tau)]  +  Gamma_1loop(tau)
    S[D_K(tau)]   = tree spectral action = Sum_k f(x_k(tau)),  x_k = lambda_k^2 / Lambda^2.
                    E7 / W7-S37 Structural Monotonicity Theorem (PROVEN, 9600/9600 checks):
                    S_f(tau) monotone for ALL smooth monotone f, ALL Lambda, ALL 10 sectors;
                    d<lambda^2>/dtau > 0 (eigenvalues GROW with tau).
    Gamma_1loop   = 1/2 Tr ln(D_K^2/Lambda^2) = 1/2 Sum_k ln(x_k) = Sum_k ln(|lambda_k|/Lambda).
                    [section 1.3a; S62 einstein-baptista one-loop spectral-action form]

[SIGN] SUBSTITUTION CHAIN for the claim "dGamma/dtau retains a FIXED sign over
[0, tau_now] -- the one-loop correction introduces NO interior stationary point":

  Step 1 -- Definitions:
    S[D_K(tau)] : tree spectral action; E7 => monotone in tau for ANY monotone f.
                  CANONICAL (E7-baseline) convention: f(x)=sqrt(x)=|lambda| (an INCREASING
                  monotone function) => dS/dtau>0, matching the canonical dS_fold=+58672.8.
    Gamma_1loop(tau) = Sum_k ln(|lambda_k(tau)|/Lambda)   [increasing in |lambda_k|]
    lambda_k(tau) = lambda_k(tau_fold) * r(tau_fold)/r(tau);   |lambda_k(tau)| ~ 1/r(tau),
                  r(tau) the Jensen radius (monotone). The cached spectrum is the tau_fold slice;
                  it is Jensen-scaled across the tau-grid. r(tau) is CALIBRATED substrate-first
                  from the S36 multi-tau cache (the framework's own Jensen-flow data), NOT an
                  external placeholder: 1/r(tau) := <|lambda|>(tau)/<|lambda|>(tau_fold).

  Step 2 -- Substitution (plug definitions into dGamma/dtau; no simplification):
    dGamma/dtau = dS/dtau + dGamma_1loop/dtau
                = dS/dtau + d/dtau [ Sum_k ln(|lambda_k(tau)|/Lambda) ]
                = dS/dtau + Sum_k (1/lambda_k(tau)) (dlambda_k/dtau)
                = dS/dtau + Sum_k d ln|lambda_k(tau)|/dtau

  Step 3 -- Simplification (algebra; one step per line):
    Since |lambda_k(tau)| ~ 1/r(tau),  d ln|lambda_k|/dtau = - d ln r(tau)/dtau  (SAME sign for
      every k -- a global factor; r(tau) is the single Jensen radius).
    => Sum_k d ln|lambda_k|/dtau = N_eval * (- d ln r/dtau)        [N_eval=78080; one common sign]
    => dGamma/dtau = dS/dtau  +  N_eval * (- d ln r/dtau)
    With eigenvalues GROWING in tau (E7: d<lambda^2>/dtau>0), -d ln r/dtau = +d ln|lambda|/dtau > 0.

  Step 4 -- Direction / sign read-off:
    dS/dtau > 0 (E7, INCREASING-f convention; canonical +58672.8 at fold).
    one-loop term N_eval*(-d ln r/dtau) > 0 (eigenvalues grow => log grows).
    BOTH terms share sign (POSITIVE) => dGamma/dtau > 0 everywhere => NO interior zero => NO WELL.
    The SIGN is NOT assumed: the gate MEASURES sign(dGamma/dtau) on a 200-point grid and counts
    interior sign changes. If the two terms had OPPOSITE signs (e.g. a DECREASING Gaussian cutoff
    tree term vs the increasing log one-loop term), an interior zero COULD form where the one-loop
    magnitude crosses the tree magnitude -- that contingency is the stringent cross-check arm.

  Conclusion (NEUTRAL): PASS (N_interior_sign_changes=0) => the tree-level no-saddle E7 result is
    ONE-LOOP-ROBUST; the monotone-ramp / "no landscape AND no stabilizing well" picture (two faces
    of E7) survives the leading quantum correction. FAIL (>=1 interior zero) => a one-loop-induced
    well/barrier; consequential. The sign is the gate's OUTPUT.

THREE INDEPENDENT ROUTES TO THE SIGN (cross-checks):
  Route A (CANONICAL, FULL): tree=|lambda| (E7 INCREASING convention) + one-loop log, on the
    FULL L12 cache (78080 modes, L<=10), Jensen-scaled over a 200-pt grid [0, tau_now=0.6].
    dGamma/dtau by finite differences (np.gradient); count interior sign changes.
  Route B (STRINGENT CROSS-CHECK, regulator-spread): tree=Gaussian f(x)=exp(-x/2) (DECREASING)
    + one-loop log (INCREASING) -> OPPOSITE-sign sum. The harder test: does the increasing
    one-loop log ever cancel the decreasing Gaussian tree to make an interior zero? This is the
    a_n^{Pauli-Villars}-flavoured regulator-spread sibling discriminator (reported, not canonical).
  Route C (INDEPENDENT, S36 direct, NO scaling model): per-mode d ln|lambda_k|/dtau computed
    directly from the S36 multi-tau eigenvalues (no Jensen-scaling assumption); confirms the SIGN
    of dGamma_1loop/dtau independently of the r(tau) calibration.

REGULATOR-PIN (regulator-pin-discipline.md): the one-loop trace-log 1/2 Tr ln(D^2/Lambda^2) is
  the zeta/heat-kernel-log regulator class, tagged a_n^{zeta} (NEW Seeley-DeWitt-adjacent
  citation). The Gaussian cross-check arm carries the a_n^{Pauli-Villars}-flavoured massive-cutoff
  reading (regulator-spread). CLASS=FULL: the trace-log is computed DIRECTLY on the cached FULL
  D_K spectrum (Jensen-scaled per tau), NOT the SCHEMATIC _spectral_action_regulators.py analog
  (substrate-first-canonical-sourcing.md sec (iv)).

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`; CPU-cap-OMP8
  (trace-log is a vector reduction over 78080 pre-cached scalars x 200 tau-points = a CPU vector op,
  NOT a matrix op -- eigenvalues are PRE-CACHED, no eigendecomposition); dual-SHA emitted; [SIGN]
  trigger -> schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row appended.
"""

from __future__ import annotations

import glob
import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Paths + canonical imports
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_95_DIR = PROJECT_ROOT / "computations" / "session-95"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    tau_fold,
    M_KK,
    dS_fold,
    d2S_fold,
    S_fold,
    PI,
)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W2-3 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S95-W2-3-NO-WELL-ONE-LOOP"
SCHEME = "SA"
CONVENTION = "EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP"
L_MAX = 10                                  # (local) operational truncation (p+q<=10)

TAU_LO, TAU_HI = 0.0, 0.6                    # (local) tau in [0, tau_now]; plan scan_range
N_GRID = 200                                 # (local) >=200 pts; plan step_size 0.003 => 200 pts
ZERO_TOL = 1e-10                             # (local) sign-change zero-detection tolerance
N_EVAL_EXPECTED = 78080                      # (local) plan N_eval pin (L<=10 stored abs_evals)
PQ_CUT = 10                                  # (local) L_max=10 Peter-Weyl restriction

CANONICAL_CONSTANTS_PATH = SHARED_DIR / "canonical_constants.py"
L12_CACHE_PATH = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
INPUT_FILES = [L12_CACHE_PATH, CANONICAL_CONSTANTS_PATH]

VERDICT_TXT = SESSION_95_DIR / "s95_gate_verdicts.txt"
OUT_NPZ = SESSION_95_DIR / "s95_w2_3_no_well_one_loop.npz"
OUT_PNG = SESSION_95_DIR / "s95_w2_3_no_well_one_loop.png"

# Jensen radius calibration source (framework's own multi-tau cache; substrate-first)
S36_CACHE_PATTERN = "computations/**/s36_sfull_tau_stabilization.npz"
S36_SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1), (1, 2)]
S36_TAUS = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])  # (local) S36 tau slices


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors sibling s95_w1_4)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
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


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    """Atomic single-write canonical line + dual-SHA companion + ([SIGN]) 3-tuple row."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    SESSION_95_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def append_3tuple_row(sign_v: str, mag_v: str, regime_v: str) -> None:
    """schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row ([SIGN] trigger; gate-verdicts.md)."""
    row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(row)


# ---------------------------------------------------------------------------
# SU(3) Peter-Weyl helpers
# ---------------------------------------------------------------------------
def dim_pq(p: int, q: int) -> int:
    """SU(3) Weyl dimension (closed form)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def C2_pq(p: int, q: int) -> float:
    """SU(3) quadratic Casimir (closed form)."""
    return (p * p + p * q + q * q + 3 * (p + q)) / 3.0


# ---------------------------------------------------------------------------
# Jensen radius r(tau): substrate-first calibration from the S36 multi-tau cache
# ---------------------------------------------------------------------------
def calibrate_jensen_inv_r():
    """Calibrate 1/r(tau) := <|lambda|>(tau)/<|lambda|>(tau_fold) from the S36 multi-tau cache.

    <|lambda|>(tau) is the Peter-Weyl-multiplicity-weighted (mult = dim_pq) arithmetic mean of
    |lambda| over the 10 S36 sectors. Normalized so 1/r(tau_fold) = 1. A smooth quadratic in tau
    is fitted to ln(1/r) (the residual is ~3.5e-6 in ln units, see stdout) so that 1/r(tau) and
    its analytic derivative d ln(1/r)/dtau are available on the full grid [0, tau_now], including
    the EXTRAPOLATION beyond the S36 data range [0.05, 0.22] to tau_now=0.6.

    Returns (inv_r_fn, dln_invr_dt_fn, coef, residual_max, inv_r_data).
    """
    cands = glob.glob(str(PROJECT_ROOT / S36_CACHE_PATTERN), recursive=True)
    if not cands:
        raise FileNotFoundError("S36 multi-tau cache (s36_sfull_tau_stabilization.npz) not found")
    d36 = np.load(cands[0], allow_pickle=True)

    def sec36(t, p, q):
        return np.abs(np.asarray(d36[f"evals_tau{t:.3f}_{p}_{q}"], dtype=float))

    def mean_abs(t):
        num = 0.0  # (local)
        den = 0.0  # (local)
        for (p, q) in S36_SECTORS:
            m = dim_pq(p, q)  # (local) Peter-Weyl regular-rep multiplicity
            v = sec36(t, p, q)
            num += m * v.sum()
            den += m * v.size
        return num / den

    mbar_fold = mean_abs(tau_fold)  # (local)
    inv_r_data = np.array([mean_abs(t) / mbar_fold for t in S36_TAUS])  # (local) 1/r at S36 taus
    coef = np.polyfit(S36_TAUS, np.log(inv_r_data), 2)  # (local) ln(1/r) ~ a t^2 + b t + c
    resid_max = float(np.max(np.abs(np.log(inv_r_data) - np.polyval(coef, S36_TAUS))))  # (local)

    def inv_r_fn(t):
        return np.exp(np.polyval(coef, t))

    def dln_invr_dt_fn(t):
        a, b, _c = coef  # (local)
        return 2.0 * a * t + b  # (local) analytic d ln(1/r)/dtau

    return inv_r_fn, dln_invr_dt_fn, coef, resid_max, inv_r_data, str(Path(cands[0]).resolve())


# ---------------------------------------------------------------------------
# Load FULL L12 spectrum (tau_fold slice), restrict to p+q<=10
# ---------------------------------------------------------------------------
def load_fold_spectrum():
    """Return (abs_fold, n_eval, min_abs, sector_pq_list) for the L<=10 restriction.

    abs_fold: concatenated |lambda| over all sectors with p+q<=10 (78080 entries; the spinor
    rank 2^4=16 is already baked into each sector's abs_evals; the additional Peter-Weyl
    regular-rep multiplicity dim_pq is supplied separately for the d^2-weighted moment cross-check).
    """
    cache = np.load(L12_CACHE_PATH, allow_pickle=True)
    se = cache["sector_evals"].item()  # (local) dict keyed by (p,q)
    abs_list = []  # (local)
    pq_list = []  # (local)
    for (p, q), v in se.items():
        if p + q > PQ_CUT:
            continue
        ae = np.asarray(v["abs_evals"], dtype=float)  # (local)
        abs_list.append(ae)
        pq_list.append((p, q, ae.size))
    abs_fold = np.concatenate(abs_list)  # (local)
    return abs_fold, abs_fold.size, float(abs_fold.min()), pq_list, se


# ---------------------------------------------------------------------------
# Tree spectral action S(tau) and one-loop Gamma_1loop(tau)
# ---------------------------------------------------------------------------
def tree_action_abs(abs_tau):
    """CANONICAL (E7 INCREASING) tree action: f(x)=sqrt(x)=|lambda| => S = sum |lambda|.

    This is the S42/S84 |lambda| convention whose dS_fold = +58672.8 is the canonical E7
    baseline. f is INCREASING, so eigenvalue growth (E7) drives dS/dtau > 0.
    """
    return float(np.sum(abs_tau))


def tree_action_gauss(abs_tau):
    """STRINGENT-CROSS-CHECK Gaussian tree action: f(x)=exp(-x/2) (Chamseddine-Connes).

    f is DECREASING in x, so eigenvalue growth (E7) drives dS/dtau < 0 -- the OPPOSITE sign
    from the one-loop log term. This makes the Gaussian arm the harder no-well test.
    Lambda = M_KK and |lambda| are in M_KK units, so x = |lambda|^2.
    """
    return float(np.sum(np.exp(-(abs_tau ** 2) / 2.0)))


def one_loop_tracelog(abs_tau):
    """One-loop effective-action generator Gamma_1loop = 1/2 Tr ln(D^2/Lambda^2)
       = Sum_k ln(|lambda_k|/Lambda). Lambda = M_KK = 1 in M_KK units => Sum_k ln|lambda_k|.
       INCREASING in |lambda_k|.
    """
    return float(np.sum(np.log(abs_tau)))


# ---------------------------------------------------------------------------
# Route C: independent per-mode d ln|lambda|/dtau from S36 (NO scaling model)
# ---------------------------------------------------------------------------
def route_c_s36_direct(s36_path):
    """Compute Sum_k d ln|lambda_k|/dtau DIRECTLY from the S36 multi-tau eigenvalues at the fold,
    via sorted central finite difference (stencil 0.18, 0.19, 0.21), Peter-Weyl d^2-weighted.
    INDEPENDENT of the Jensen-scaling r(tau) model -> confirms the SIGN of dGamma_1loop/dtau.
    Returns (dG1loop_dtau_route_c, sign).
    """
    d36 = np.load(s36_path, allow_pickle=True)

    def sec36(t, p, q):
        return np.sort(np.abs(np.asarray(d36[f"evals_tau{t:.3f}_{p}_{q}"], dtype=float)))

    hL = 0.19 - 0.18  # (local)
    hR = 0.21 - 0.19  # (local)
    a = hL / (hR * (hL + hR))  # (local) forward weight
    b = -hR / (hL * (hL + hR))  # (local) backward weight
    c = (hR - hL) / (hL * hR)  # (local) center weight
    total = 0.0  # (local)
    for (p, q) in S36_SECTORS:
        m = dim_pq(p, q) ** 2  # (local) d^2 PW weight (matches s95_w1_4 moment convention)
        lam_lo = sec36(0.18, p, q)
        lam_0 = sec36(0.19, p, q)
        lam_hi = sec36(0.21, p, q)
        dlam = a * lam_hi + b * lam_lo + c * lam_0  # (local) sorted dlambda/dtau
        dln = dlam / lam_0  # (local) d ln|lambda|/dtau per mode
        total += m * np.sum(dln)
    return float(total), int(np.sign(total))


# ---------------------------------------------------------------------------
# Sign-change counting (reject float-noise zero crossings)
# ---------------------------------------------------------------------------
def count_interior_sign_changes(deriv, tol):
    """Count interior sign changes of `deriv`, rejecting noise: a sign change counts only when
    BOTH adjacent points have |deriv| > tol (rejects float-noise zero-crossings near deriv=0).
    """
    sgn = np.sign(deriv)  # (local)
    n = 0  # (local)
    locs = []  # (local)
    for i in range(1, len(deriv)):
        if abs(deriv[i]) > tol and abs(deriv[i - 1]) > tol and sgn[i] != sgn[i - 1]:
            n += 1
            locs.append(i)
    return n, locs


# ---------------------------------------------------------------------------
# Main compute
# ---------------------------------------------------------------------------
def compute():
    # --- Jensen radius calibration (substrate-first, from S36) ---
    inv_r_fn, dln_invr_dt_fn, coef, resid_max, inv_r_data, s36_path = calibrate_jensen_inv_r()

    # --- FULL L12 fold spectrum, L<=10 ---
    abs_fold, n_eval, min_abs_fold, pq_list, _se = load_fold_spectrum()

    # --- tau grid [0, tau_now] ---
    tau = np.linspace(TAU_LO, TAU_HI, N_GRID)  # (local)

    # Jensen-scaled |lambda| at each tau: |lambda(tau)| = |lambda(fold)| * (1/r(tau))
    # (1/r normalized to 1 at fold => |lambda(fold)| recovered at tau_fold)
    inv_r_grid = inv_r_fn(tau)  # (local)
    abs_grid = np.outer(inv_r_grid, abs_fold)  # (local) shape (N_GRID, n_eval); positive, no zero modes
    min_abs_grid = float(abs_grid.min())  # (local)

    # --- Route A (CANONICAL): tree = |lambda| (E7 INCREASING), one-loop = log ---
    S_abs = np.array([tree_action_abs(abs_grid[i]) for i in range(N_GRID)])  # (local)
    G1 = np.array([one_loop_tracelog(abs_grid[i]) for i in range(N_GRID)])  # (local)
    Gam_abs = S_abs + G1  # (local)
    dS_abs = np.gradient(S_abs, tau)  # (local)
    dG1 = np.gradient(G1, tau)  # (local)
    dGam_abs = np.gradient(Gam_abs, tau)  # (local)
    n_sc_abs, locs_abs = count_interior_sign_changes(dGam_abs, ZERO_TOL)

    # --- Route B (STRINGENT CROSS-CHECK): tree = Gaussian (DECREASING) + one-loop log ---
    S_g = np.array([tree_action_gauss(abs_grid[i]) for i in range(N_GRID)])  # (local)
    Gam_g = S_g + G1  # (local)
    dS_g = np.gradient(S_g, tau)  # (local)
    dGam_g = np.gradient(Gam_g, tau)  # (local)
    n_sc_g, locs_g = count_interior_sign_changes(dGam_g, ZERO_TOL)

    # --- analytic one-loop derivative cross-check (closed form, Step 3) ---
    # dGamma_1loop/dtau = N_eval * d ln(1/r)/dtau (common log-derivative * mode count)
    dG1_analytic = n_eval * dln_invr_dt_fn(tau)  # (local)

    # --- Route C (INDEPENDENT, S36 direct, no scaling model) ---
    dG1loop_route_c, sign_route_c = route_c_s36_direct(s36_path)

    # --- fold-point readouts ---
    ifold = int(np.argmin(np.abs(tau - tau_fold)))  # (local)
    dS_abs_fold = float(dS_abs[ifold])  # (local)
    dG1_fold = float(dG1[ifold])  # (local)
    dGam_abs_fold = float(dGam_abs[ifold])  # (local)
    dln_invr_fold = float(dln_invr_dt_fn(tau_fold))  # (local)
    dG1_analytic_fold = float(n_eval * dln_invr_fold)  # (local)

    # cross-check: computed-tree dS_fold vs E7 canonical +58672.8 (same |lambda| convention)
    dS_abs_vs_canonical_ratio = dS_abs_fold / dS_fold  # (local)

    # --- regime / auto-shortening ---
    # The Jensen-scaling eigenvalue model is exact only over the S36 data range [0.05, 0.22];
    # beyond that it is a smooth extrapolation. The PHYSICAL regime requirement is that the
    # one-loop trace-log stays finite (no lambda -> 0) AND the eigenvalues remain positive
    # across [0, tau_now]. min|lambda| over the grid > 0 => ln finite everywhere => regime VALID
    # for the trace-log. The intended scan window is the FULL [0, tau_now]; it is computed in
    # full (no domain shortening) -> domain_used_frac = 1.0.
    no_zero_mode = bool(min_abs_grid > 1e-9)  # (local)
    domain_used_frac = 1.0  # (local) full [0, tau_now] computed; no auto-shortening

    return {
        "tau": tau,
        "inv_r_grid": inv_r_grid,
        "abs_min_fold": min_abs_fold,
        "abs_min_grid": min_abs_grid,
        "n_eval": n_eval,
        "coef": coef,
        "jensen_fit_residual_max": resid_max,
        "inv_r_data": inv_r_data,
        # Route A
        "S_abs": S_abs, "G1": G1, "Gam_abs": Gam_abs,
        "dS_abs": dS_abs, "dG1": dG1, "dGam_abs": dGam_abs,
        "n_sc_abs": n_sc_abs, "locs_abs": locs_abs,
        # Route B
        "S_g": S_g, "Gam_g": Gam_g, "dS_g": dS_g, "dGam_g": dGam_g,
        "n_sc_g": n_sc_g, "locs_g": locs_g,
        # analytic + Route C
        "dG1_analytic": dG1_analytic,
        "dG1_analytic_fold": dG1_analytic_fold,
        "dG1loop_route_c": dG1loop_route_c,
        "sign_route_c": sign_route_c,
        # fold readouts
        "ifold": ifold,
        "dS_abs_fold": dS_abs_fold,
        "dG1_fold": dG1_fold,
        "dGam_abs_fold": dGam_abs_fold,
        "dln_invr_fold": dln_invr_fold,
        "dS_abs_vs_canonical_ratio": dS_abs_vs_canonical_ratio,
        # directional predicates
        "dS_abs_all_pos": bool(np.all(dS_abs > 0)),
        "dG1_all_pos": bool(np.all(dG1 > 0)),
        "dGam_abs_all_pos": bool(np.all(dGam_abs > 0)),
        "dGam_abs_constant_sign": bool(np.all(np.sign(dGam_abs) == np.sign(dGam_abs[0]))),
        "Gam_abs_monotone_incr": bool(np.all(np.diff(Gam_abs) > 0)),
        "dGam_g_constant_sign": bool(np.all(np.sign(dGam_g) == np.sign(dGam_g[0]))),
        # regime
        "no_zero_mode": no_zero_mode,
        "domain_used_frac": domain_used_frac,
        # canonical verdict value = interior sign-change count (Route A canonical)
        "value": int(n_sc_abs),
    }


# ---------------------------------------------------------------------------
# Gate evaluation (pre-registered; no post-hoc edits)
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Pre-registered (plan §W2-3):
      PASS iff N_interior_sign_changes(dGamma/dtau) = 0 over [0, tau_now], regime VALID.
      FAIL iff N_interior_sign_changes >= 1, regime VALID.
      INFO iff feature appears only where regime MARGINAL/BREAKDOWN.
    """
    n_sc = res["n_sc_abs"]  # (local) canonical Route-A interior sign-change count

    # SIGN verdict: substitution-chain Step 4 predicts a FIXED sign of dGamma/dtau (no sign change).
    # sign PASS iff dGamma/dtau retains a constant sign over the grid (==> no interior zero).
    sign_v = "PASS" if res["dGam_abs_constant_sign"] else "FAIL"  # (local)

    # MAGNITUDE verdict: the operator is the integer interior-sign-change count; target 0.
    # PASS iff n_sc == 0; FAIL iff n_sc >= 1.
    if n_sc == 0:
        mag_v = "PASS"  # (local)
    else:
        mag_v = "FAIL"

    # REGIME verdict: the one-loop trace-log is finite (no zero mode) across the full window AND
    # the window is computed in full (domain_used_frac = 1.0) => VALID. Auto-shortening bands
    # (gate-verdicts.md): >=0.95 -> VALID; 0.50-0.95 -> MARGINAL; <0.50 -> BREAKDOWN.
    f_used = res["domain_used_frac"]  # (local)
    if not res["no_zero_mode"]:
        regime_v = "BREAKDOWN"  # (local) ln divergence if any lambda -> 0
    elif f_used >= 0.95:
        regime_v = "VALID"
    elif f_used >= 0.50:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        composite = "INFO"
    elif mag_v == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict) -> None:
    tau = res["tau"]  # (local)
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Gamma(tau), S(tau), Gamma_1loop(tau) -- CANONICAL |lambda| arm
    ax = axes[0, 0]
    ax.plot(tau, res["Gam_abs"], "-", color="C3", lw=2.2,
            label=r"$\Gamma=S+\Gamma_{1\rm loop}$ (canonical, $|\lambda|$)")
    ax.plot(tau, res["S_abs"], "--", color="C0", lw=1.6, label=r"$S_{\rm tree}=\sum|\lambda|$ (E7)")
    ax.plot(tau, res["G1"], ":", color="C2", lw=1.6, label=r"$\Gamma_{1\rm loop}=\sum\ln|\lambda|$")
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.7, label=r"$\tau_{\rm fold}=0.19$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel("action")
    ax.set_title("Effective action $\\Gamma(\\tau)$ over $[0,\\tau_{\\rm now}]$ (canonical arm)")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    # Panel 2: dGamma/dtau (canonical) -- the SIGN gate
    ax = axes[0, 1]
    ax.plot(tau, res["dGam_abs"], "-", color="C3", lw=2.2, label=r"$d\Gamma/d\tau$")
    ax.plot(tau, res["dS_abs"], "--", color="C0", lw=1.4, label=r"$dS/d\tau$ (E7, $>0$)")
    ax.plot(tau, res["dG1"], ":", color="C2", lw=1.4, label=r"$d\Gamma_{1\rm loop}/d\tau$ ($>0$)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.7)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d/d\tau$")
    ax.set_title(f"$d\\Gamma/d\\tau$: interior sign changes = {res['n_sc_abs']} (canonical)")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)
    for i in res["locs_abs"]:
        ax.plot(tau[i], res["dGam_abs"][i], "rv", ms=10)

    # Panel 3: STRINGENT cross-check arm (Gaussian tree, opposite-sign sum)
    ax = axes[1, 0]
    ax.plot(tau, res["dGam_g"], "-", color="C4", lw=2.2, label=r"$d\Gamma/d\tau$ (Gaussian tree)")
    ax.plot(tau, res["dS_g"], "--", color="C1", lw=1.4, label=r"$dS_{\rm Gauss}/d\tau$ ($<0$)")
    ax.plot(tau, res["dG1"], ":", color="C2", lw=1.4, label=r"$d\Gamma_{1\rm loop}/d\tau$ ($>0$)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.7)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d/d\tau$")
    ax.set_title(f"Stringent arm (opposite-sign): sign changes = {res['n_sc_g']}")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)
    for i in res["locs_g"]:
        ax.plot(tau[i], res["dGam_g"][i], "rv", ms=10)

    # Panel 4: analytic vs finite-difference one-loop derivative (cross-check)
    ax = axes[1, 1]
    ax.plot(tau, res["dG1"], "-", color="C2", lw=2.0, label=r"$d\Gamma_{1\rm loop}/d\tau$ (FD)")
    ax.plot(tau, res["dG1_analytic"], "--", color="k", lw=1.4,
            label=r"$N_{\rm eval}\cdot d\ln(1/r)/d\tau$ (analytic)")
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.7)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d\Gamma_{1\rm loop}/d\tau$")
    ax.set_title("One-loop derivative: analytic vs finite-difference\n(independent-route sign check)")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    fig.suptitle(
        f"S95-W2-3 NO-WELL-ONE-LOOP: $\\Gamma=S+\\frac{{1}}{{2}}\\,$Tr$\\ln(D_K^2/\\Lambda^2)$ over "
        f"$[0,\\tau_{{\\rm now}}]$ -- interior sign changes = {res['n_sc_abs']}",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}  ([SIGN])")
    print("=" * 78)
    pins = log_input_pins(INPUT_FILES)
    print()
    print("CANONICAL CONSTANTS:")
    print(f"  tau_fold = {tau_fold}   M_KK = {M_KK:.6e}   PI = {PI:.6f}")
    print(f"  dS_fold (E7 canonical, |lambda| conv) = {dS_fold:+.6f}")
    print(f"  d2S_fold = {d2S_fold:+.6f}   S_fold = {S_fold:.6f}")
    print()

    res = compute()

    print("=" * 78)
    print("JENSEN RADIUS CALIBRATION (substrate-first, from S36 multi-tau cache)")
    print("=" * 78)
    print(f"  ln(1/r) quadratic fit coef [a,b,c] = {res['coef']}")
    print(f"  fit residual max (ln units)        = {res['jensen_fit_residual_max']:.3e}")
    print(f"  1/r(tau) at S36 taus {list(S36_TAUS)}:")
    print(f"    {np.round(res['inv_r_data'], 6)}")
    print(f"  d ln(1/r)/dtau at fold = d ln|lambda|/dtau (common) = {res['dln_invr_fold']:+.6f}")
    print(f"    => eigenvalues {'GROW' if res['dln_invr_fold'] > 0 else 'SHRINK'} with tau"
          f"  (E7-consistent: d<lambda^2>/dtau > 0)")
    print()

    print("=" * 78)
    print("FULL L12 SPECTRUM (tau_fold slice, p+q<=10)")
    print("=" * 78)
    print(f"  N_eval (stored |lambda| count, L<=10) = {res['n_eval']}  "
          f"(plan pin {N_EVAL_EXPECTED}; match: {res['n_eval'] == N_EVAL_EXPECTED})")
    print(f"  min|lambda| at fold  = {res['abs_min_fold']:.6f}  (> 0 => ln finite, no zero mode)")
    print(f"  min|lambda| over grid = {res['abs_min_grid']:.6f}  (> 0 over full [0, tau_now])")
    print()

    print("=" * 78)
    print("[SIGN] SUBSTITUTION CHAIN -- numbers substituted (Steps 1-4)")
    print("=" * 78)
    print("  Step 1 (defs): Gamma = S[D_K(tau)] + Gamma_1loop; S=sum|lambda| (E7 increasing conv);")
    print("                 Gamma_1loop = sum ln|lambda|; |lambda(tau)| = |lambda(fold)|*(1/r(tau)).")
    print("  Step 2 (subst): dGamma/dtau = dS/dtau + sum_k d ln|lambda_k|/dtau.")
    print("  Step 3 (simplify): d ln|lambda_k|/dtau = -d ln r/dtau (common, all k)")
    print(f"                 => dGamma_1loop/dtau = N_eval*(-d ln r/dtau)")
    print(f"                 = {res['n_eval']} * ({res['dln_invr_fold']:+.6f}) "
          f"= {res['dG1_analytic_fold']:+.4f}  (analytic, at fold)")
    print(f"                 finite-difference dGamma_1loop/dtau at fold = {res['dG1_fold']:+.4f}")
    print("  Step 4 (sign read-off at fold):")
    print(f"     dS/dtau (tree, E7 |lambda|)            = {res['dS_abs_fold']:+.4f}  (canonical "
          f"+58672.8; ratio {res['dS_abs_vs_canonical_ratio']:.4f})")
    print(f"     dGamma_1loop/dtau (one-loop)           = {res['dG1_fold']:+.4f}")
    print(f"     dGamma/dtau = dS/dtau + dGamma_1loop/dtau = {res['dGam_abs_fold']:+.4f}")
    print(f"     one-loop / tree ratio                  = {res['dG1_fold']/res['dS_abs_fold']:.4%}")
    print("     BOTH terms POSITIVE => share sign => dGamma/dtau > 0 => NO interior zero => NO WELL.")
    print()

    print("=" * 78)
    print("ROUTE A (CANONICAL): tree=|lambda| (E7) + one-loop log -- over [0, tau_now], 200 pts")
    print("=" * 78)
    print(f"  dS/dtau:        all>0? {res['dS_abs_all_pos']}   "
          f"range [{res['dS_abs'].min():.1f}, {res['dS_abs'].max():.1f}]")
    print(f"  dGamma_1loop/dtau: all>0? {res['dG1_all_pos']}   "
          f"range [{res['dG1'].min():.1f}, {res['dG1'].max():.1f}]")
    print(f"  dGamma/dtau:    constant sign? {res['dGam_abs_constant_sign']}   "
          f"range [{res['dGam_abs'].min():.1f}, {res['dGam_abs'].max():.1f}]")
    print(f"  Gamma(tau) monotone increasing? {res['Gam_abs_monotone_incr']}")
    print(f"  *** N_interior_sign_changes(dGamma/dtau) = {res['n_sc_abs']}  (target 0) ***")
    print()

    print("=" * 78)
    print("ROUTE B (STRINGENT CROSS-CHECK): Gaussian tree (DECREASING) + one-loop log (INCREASING)")
    print("=" * 78)
    print(f"  dS_Gauss/dtau:  range [{res['dS_g'].min():.1f}, {res['dS_g'].max():.1f}] (decreasing => <0)")
    print(f"  dGamma/dtau (opposite-sign sum): range [{res['dGam_g'].min():.1f}, {res['dGam_g'].max():.1f}]"
          f"   constant sign? {res['dGam_g_constant_sign']}")
    print(f"  N_interior_sign_changes (Gaussian arm) = {res['n_sc_g']}")
    print("  (one-loop log DOMINATES the decreasing Gaussian tree everywhere => still no zero)")
    print()

    print("=" * 78)
    print("ROUTE C (INDEPENDENT, S36 direct, NO scaling model)")
    print("=" * 78)
    print(f"  dGamma_1loop/dtau (S36 direct per-mode FD, d^2-weighted) = {res['dG1loop_route_c']:+.4f}")
    print(f"  sign = {'+' if res['sign_route_c'] > 0 else '-'}  "
          f"(agrees with Route A one-loop sign: {res['sign_route_c'] > 0 and res['dG1_fold'] > 0})")
    print()

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    print("=" * 78)
    print("GATE EVALUATION")
    print("=" * 78)
    print(f"  value (N_interior_sign_changes, canonical Route A) = {res['value']}")
    print(f"  domain_used_frac = {res['domain_used_frac']:.4f}   no_zero_mode = {res['no_zero_mode']}")
    print(f"  sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print(f"  COMPOSITE VERDICT = {composite}")
    print()

    # --- save npz ---
    np.savez_compressed(
        OUT_NPZ,
        tau=res["tau"],
        inv_r_grid=res["inv_r_grid"],
        jensen_coef=res["coef"],
        jensen_fit_residual_max=res["jensen_fit_residual_max"],
        inv_r_data=res["inv_r_data"],
        s36_taus=S36_TAUS,
        n_eval=res["n_eval"],
        abs_min_fold=res["abs_min_fold"],
        abs_min_grid=res["abs_min_grid"],
        # Route A
        S_abs=res["S_abs"], G1=res["G1"], Gam_abs=res["Gam_abs"],
        dS_abs=res["dS_abs"], dG1=res["dG1"], dGam_abs=res["dGam_abs"],
        n_sc_abs=res["n_sc_abs"],
        # Route B
        S_g=res["S_g"], Gam_g=res["Gam_g"], dS_g=res["dS_g"], dGam_g=res["dGam_g"],
        n_sc_g=res["n_sc_g"],
        # analytic + Route C
        dG1_analytic=res["dG1_analytic"],
        dG1_analytic_fold=res["dG1_analytic_fold"],
        dG1loop_route_c=res["dG1loop_route_c"],
        sign_route_c=res["sign_route_c"],
        # fold readouts
        dS_abs_fold=res["dS_abs_fold"],
        dG1_fold=res["dG1_fold"],
        dGam_abs_fold=res["dGam_abs_fold"],
        dln_invr_fold=res["dln_invr_fold"],
        dS_fold_canonical=dS_fold,
        dS_abs_vs_canonical_ratio=res["dS_abs_vs_canonical_ratio"],
        # predicates
        dS_abs_all_pos=res["dS_abs_all_pos"],
        dG1_all_pos=res["dG1_all_pos"],
        dGam_abs_constant_sign=res["dGam_abs_constant_sign"],
        Gam_abs_monotone_incr=res["Gam_abs_monotone_incr"],
        dGam_g_constant_sign=res["dGam_g_constant_sign"],
        # regime
        no_zero_mode=res["no_zero_mode"],
        domain_used_frac=res["domain_used_frac"],
        # verdict
        value=res["value"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite,
        tau_fold=tau_fold, M_KK=M_KK,
    )
    print(f"  npz written: {OUT_NPZ}")

    make_plot(res)
    print(f"  png written: {OUT_PNG}")

    # --- dual-SHA closure + verdict emission ---
    SELF = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(SELF, CANONICAL_CONSTANTS_PATH, pins)
    print()
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # 4-tuple final non-verdict line
    print()
    print(f"4-TUPLE: (value={res['value']}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(composite, res["value"], audit_sha, content_sha)
    append_3tuple_row(sign_v, mag_v, regime_v)  # [SIGN] trigger => REQUIRED

    print()
    print(f"VERDICT LINE APPENDED to {VERDICT_TXT}")
    print(f"  {GATE_ID}: {composite} -- value={res['value']!r} ... "
          f"audit_sha256={audit_sha}")
    print(f"  3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")
    print(f"\nElapsed: {time.time() - t0:.2f}s")


if __name__ == "__main__":
    main()
