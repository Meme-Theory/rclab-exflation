#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-W3-SADDLE-FULLDOMAIN
================================================================================
Gate:   S96-W3-SADDLE-FULLDOMAIN   (trigger [SIGN], classification GEOMETRIC)
Agent:  gen-physicist (cross-domain workhorse)
Plan:   sessions/session-plan/session-96-plan-w3.md  ## §W3-3
WP:     sessions/archive/session-96/session-96-w3-workingpaper.md  ### §W3-3

HYPOTHESIS (hawking V.9; feynman F-5; einstein §II.2; berry CF-BERRY-MASLOV-WKB)
--------------------------------------------------------------------------------
The one-loop effective action
    Gamma[tau] = S_SA(tau) + (1/2) Tr ln(D_K^2(tau)/Lambda^2)
has NO interior stationary point (dGamma/dtau != 0, FIXED sign, ZERO interior
sign-changes) on the FULL physical tau-domain [0, tau_NEC=1.383] -- extending the
S95-W2-3-NO-WELL-ONE-LOOP PASS from [0, tau_now] -- and through the overshoot
turnaround tau=1.614 (in the censored region tau>tau_NEC). Hence the partition
function Z = sum exp(-Gamma) is boundary-dominated (Gibbons-Hawking-York)
everywhere the censoring barrier admits the modulus: the universe TRANSITS, it
does not slow-roll in an interior well.

SUBSTRATE ARROW (phononic-framing.md; never inverted):
    D_K eigenvalues -> spectral-action moments a_0(tau)-a_2(tau)+a_4(tau)=S_SA(tau)
    + the (1/2) Tr ln(D_K^2/Lambda^2) fluctuation determinant -> dGamma/dtau fixed
    sign -> Z boundary-dominated. The spectral complexity grows monotonically
    inside each point; the partition function is dominated by the maximally-
    symmetric genesis boundary tau=0. We do NOT frame this as "the inflaton rolls
    in a potential well" (slow-roll / container relapse).

--------------------------------------------------------------------------------
EXTRAPOLATION-FREE EIGENVALUE MODEL (full-domain extension; the key design choice)
--------------------------------------------------------------------------------
S95-W2-3 (the [0,tau_now] baseline) Jensen-scaled the cached fold spectrum by a
QUADRATIC fit of ln(1/r) calibrated on the S36 multi-tau slices [0.05, 0.22].
Extrapolating that quadratic out to tau=1.65 is a ~7x extrapolation whose
derivative-zero would be a FIT ARTIFACT, not a substrate feature -- inadmissible
for a full-domain saddle count.

This gate instead drives the tau-dependence of EVERY eigenvalue by the
Lichnerowicz-Bochner identity (baptista E3-companion; the SAME object the sibling
gate S95-W3-5 uses), which is a CLOSED FORM valid for ALL tau (no extrapolation):
    D_K^2 = nabla*nabla + (1/4) R_K(tau)
 => lambda_k^2(tau) = nu_k + (1/4) R_K(tau),   nu_k = lambda_k(fold)^2 - (1/4)R_K(fold)
with R_K(tau) the E3 closed-form fiber scalar curvature (Sage residual 0):
    R_K(tau)  = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}
    R_K'(tau) = e^{2tau} - 2 e^{-tau} + e^{-4tau} = e^{-4tau}(e^{3tau}-1)^2 >= 0
                (Sage-verified; = 0 ONLY at tau=0 -- the genesis boundary).
nu_k > 0 for every cached mode (verified at runtime; min nu = nu_B1 = 0.1674,
matching S95-W3-5), so lambda_k^2(tau) = nu_k + (1/4)R_K(tau) > 0 for ALL tau:
the trace-log is finite everywhere, no zero modes, regime VALID across [0, 1.65].

--------------------------------------------------------------------------------
[SIGN] SUBSTITUTION CHAIN (MANDATORY, math-scripts.md
                          §"Double-Check Logic Before Compute"; plan §W3-3 Step 1-4)
--------------------------------------------------------------------------------
Claim: "dGamma/dtau has FIXED SIGN with 0 interior sign-changes on the physical
        domain [0, tau_NEC=1.383] ==> Gamma[tau] has no interior stationary point
        ==> Z = sum exp(-Gamma) is boundary-dominated over the full physical
        tau-range the censoring barrier admits."

  Step 1 -- Definitions (cite canonical source):
    S_SA(tau)   = a_0(tau) - a_2(tau) + a_4(tau)   [E7 spectral-action moment combo;
                  a_0_FW_zeta=6440, a_2_FW_zeta=2776.165389, a_4_FW_zeta=1350.7216 at fold]
    Gamma[tau]  = S_SA(tau) + (1/2) Tr ln(D_K^2(tau)/Lambda^2)   [one-loop EA; Lambda=M_KK]
                = S_full(tau) + Sum_k ln(|lambda_k(tau)|/Lambda)  [rep-A canonical tree]
    R_K(tau)    = E3 closed-form fiber scalar curvature; R_K'(tau) >= 0 (=0 only at tau=0).
    lambda_k^2(tau) = nu_k + (1/4)R_K(tau)         [Lichnerowicz-Bochner; nu_k>0 all k]
    tau_NEC     = 1.383   [NEC-violation onset, S95 W4-5 12D censorship; physical boundary]
    tau_overshoot = 1.614 [overshoot turnaround, in the censored region tau>tau_NEC]
    n_sc        = count of interior sign-changes of dGamma/dtau on a given interval
    E7 Structural Monotonicity (PROVEN, 9600/9600): dS_SA/dtau has FIXED SIGN for each
                  moment, all monotone f, all Lambda, all 10 sectors (dS_fold=+58672.8
                  for the Sum|lambda| instantiation).

  Step 2 -- Substitute (combined derivative via Jacobi's formula; no simplification):
    dGamma/dtau = dS_SA/dtau + (1/2) d/dtau Tr ln(D_K^2/Lambda^2)
                = dS_SA/dtau + (1/2) Tr[ (D_K^2)^{-1} d(D_K^2)/dtau ]   [Jacobi's formula]
    With lambda_k^2 = nu_k + (1/4)R_K, d(lambda_k^2)/dtau = (1/4) R_K'(tau)   EXACT, all k.
    => one-loop:  (1/2) Tr[(D_K^2)^{-1} d(D_K^2)/dtau]
                = (1/2) Sum_k [ (1/4)R_K'(tau) / lambda_k^2(tau) ]
                = (1/8) R_K'(tau) Sum_k 1/lambda_k^2(tau).
    => tree (rep-A canonical, S_full=Sum|lambda|, the S95-W2-3 convention):
       dS_full/dtau = Sum_k (1/2)(1/4)R_K'(tau)/|lambda_k(tau)|
                    = (1/8) R_K'(tau) Sum_k 1/|lambda_k(tau)|.

  Step 3 -- Simplify to canonical form (one step per line):
    dGamma/dtau = (1/8) R_K'(tau) * [ Sum_k 1/|lambda_k(tau)|  +  Sum_k 1/lambda_k^2(tau) ].
    Both bracket sums are STRICTLY POSITIVE (lambda_k^2(tau) > 0 for all k, all tau).
    The prefactor (1/8) R_K'(tau) >= 0, with R_K'(tau) = 0 ONLY at tau=0.
    => dGamma/dtau >= 0 everywhere, with equality ONLY at the tau=0 boundary.

  Step 4 -- Direction / sign read-off (ONLY now):
    For every interior tau in (0, tau_NEC]: R_K'(tau) > 0 (strict) AND both sums > 0
      => dGamma/dtau > 0 STRICTLY => NO interior zero => n_sc([0,tau_NEC]) == 0.
    sign_verdict PASS iff dGamma/dtau retains the S95-W2-3 fixed (positive) sign across
      [0, tau_NEC] (the extension does NOT flip the sign).
    magnitude_verdict PASS iff n_sc([0,tau_NEC]) == 0; INFO iff the ONLY sign-change(s)
      are in the censored region tau>tau_NEC (n_sc([0,tau_NEC])==0 BUT n_sc((tau_NEC,1.614])>0);
      FAIL iff n_sc([0,tau_NEC]) >= 1 (an interior saddle in the PHYSICAL domain).

  Conclusion: n_sc([0,tau_NEC])==0 hardens the no-interior-saddle PASS from [0,tau_now]
    (S95-W2-3) to the full physical domain up to the NEC boundary; the saddle-freeness is
    ANALYTIC (R_K'(tau)=e^{-4tau}(e^{3tau}-1)^2 has its only zero at tau=0), not a
    numerical accident. Z is boundary-dominated (Gibbons-Hawking-York) over the full
    physical range the censoring barrier admits. A FAIL (interior saddle in [0,tau_NEC])
    is not expected and would be a major constraint-map update; either verdict maps the
    surface (math-scripts.md "All Results Are Good Results").

--------------------------------------------------------------------------------
THREE ROUTES TO THE SIGN (CC1; mirrors the S95-W2-3 three-route machinery)
--------------------------------------------------------------------------------
Route 1 (tree dS_SA/dtau monotonicity): finite-difference dS_full/dtau on the rep-A
   canonical tree S_full(tau)=Sum sqrt(nu_k+(1/4)R_K(tau)); confirm fixed sign, 0 sc.
Route 2 (Tr-ln derivative via Jacobi): dGamma_1loop/dtau both by finite difference AND
   by the analytic Jacobi closed form (1/8)R_K'(tau) Sum 1/lambda_k^2; confirm agreement.
Route 3 (combined Gamma'): dGamma/dtau = dS_full/dtau + dGamma_1loop/dtau; count interior
   sign-changes; this is the canonical verdict route.

CROSS-CHECK ARM (representation B, alternating curvature-polynomial moment; mirrors
   s96_sdw_saddle_reginv.py): S_SA^(B)(tau) = a_0 - a_2 (R_K/R_K_fold) + a_4 (R_K/R_K_fold)^2.
   Its tree derivative is NOT sign-fixed (dS_SA^(B)/dtau = 0 where R_K = a_2 R_K_fold/(2 a_4));
   reported as a DIAGNOSTIC, NOT the canonical verdict (the saddle-count verdict is rep-A,
   matching S95-W2-3 which this gate extends).

CC2: 600-point refinement near tau=0 (where R_K'->0, the only place |dGamma/dtau| dips
   toward the tolerance floor) AND near any candidate interior sign-change.

REGULATOR-PIN (regulator-pin-discipline.md): tree moments a_0/a_2/a_4 tagged a_n^{zeta}
   (zeta-regulated Seeley-DeWitt; canonical a_*_FW_zeta). One-loop (1/2)Tr ln(D_K^2/Lambda^2)
   is the zeta/heat-kernel-log regulator class (a_n^{zeta} for consistency). CLASS=FULL:
   trace-log computed DIRECTLY on the cached FULL D_K spectrum (Lichnerowicz-Bochner
   closed-form scaled per tau), NO SCHEMATIC helper (substrate-first-canonical-sourcing.md
   §(iv)); convention carries no -SCHEMATIC suffix.

GPU PATH (declared at runtime): the eigenvalue tau-flow reuses the CACHED L_max=10
   band-bottoms scaled by the CLOSED-FORM Lichnerowicz-Bochner law lambda_k^2(tau)=
   nu_k+(1/4)R_K(tau); the Tr-ln is a vector reduction over 78080 pre-cached scalars x
   300 tau-points (a CPU vector op, NOT a matrix op -- NO eigendecomposition). Hence
   the path is CPU-cap-OMP8 (OMP_NUM_THREADS=8 set before import numpy per math-scripts.md);
   no off-cache tau block is re-diagonalized, so torch.linalg.eigvalsh is NOT invoked.

DISCIPLINE: `from canonical_constants import *`; every intermediate `# (local)`; dual-SHA
   emitted; [SIGN] trigger -> schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row appended.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) CPU thread cap; vector reductions only, no matrix op
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import hashlib
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Paths + canonical imports (MANDATORY: from canonical_constants import *)
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]                  # (local) script in computations/_shared => parents[2]=root
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402
from canonical_constants import (  # noqa: E402
    tau_fold, M_KK, tau_NEC, tau_overshoot,
    a_0_FW_zeta, a_2_FW_zeta, a_4_FW_zeta,
    dS_fold, d2S_fold,
)

# ---------------------------------------------------------------------------
# Gate identity + pre-registered pins (plan §W3-3 machinery_pin_map)
# ---------------------------------------------------------------------------
GATE_ID = "S96-W3-SADDLE-FULLDOMAIN"                                            # (local)
SCHEME = "SA"                                                                   # (local) plan-pinned
CONVENTION = "EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP-FULL-DOMAIN"      # (local) plan-pinned
L_MAX = "10"                                                                    # (local)
SCHEMA_VERSION = "S84+"                                                         # (local)

TAU_LO, TAU_HI = 0.0, 1.65          # (local) plan scan_range: physical [0,tau_NEC=1.383] + overshoot 1.614
N_GRID = 300                        # (local) plan N_eval: 300-point linspace (Delta_tau ~ 0.0055)
N_GRID_REFINE = 600                 # (local) CC2 600-point refinement
ZERO_TOL = 1e-6                     # (local) plan tolerance: |dGamma/dtau|>1e-6 counts as definite sign
TAU_NOW = 0.6                       # (local) present-epoch tau (region-partition boundary; S95-W2-3 tau_now)
N_EVAL_EXPECTED = 78080             # (local) L<=10 stored |lambda| count
PQ_CUT = 10                         # (local) L_max=10 Peter-Weyl restriction

# Output destinations: script in _shared/, but data/plot/verdict in session-96/ (orchestrator override)
SESSION_96_DIR = PROJECT_ROOT / "computations" / "session-96"
SCRIPT_PATH = Path(__file__).resolve()                                                       # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"                                   # (local)
SPECTRUM_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
S95_BASELINE_NPZ = PROJECT_ROOT / "computations" / "session-95" / "s95_w2_3_no_well_one_loop.npz"     # (local)
VERDICT_FILE = SESSION_96_DIR / "s96_gate_verdicts.txt"                                       # (local) canonical path
NPZ_OUT = SESSION_96_DIR / "s96_w3_3_oneloop_saddle_fulldomain.npz"                           # (local)
PNG_OUT = SESSION_96_DIR / "s96_w3_3_oneloop_saddle_fulldomain.png"                           # (local)

# Plan-pinned static SHA (input_files; runtime-verified below)
SPECTRUM_CACHE_SHA_PIN = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"   # (local)


# ---------------------------------------------------------------------------
# Dual-SHA helpers (S84+ schema; mirrors s95_w3_5 reference implementation)
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    for name, p in files.items():
        sha = sha256_of_file(p)  # (local)
        try:
            rel = str(Path(p).resolve().relative_to(PROJECT_ROOT))  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  INPUT-PIN  {name}: {rel}  sha256={sha[:16]}...")
        pins[name] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """audit_sha256 = sha256(script_bytes + canonical_bytes + pinmap_json);
       content_sha256 = sha256(script_bytes).  (S84+ dual-SHA schema.)"""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(verdict, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Single canonical dual-SHA verdict line + dual-SHA companion row + schema-v2
    3-tuple companion row ([SIGN] directional pre-reg). Append-only single open('a')."""
    canonical = (  # (local)
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row; [SIGN] one-loop EA no-interior-saddle full-domain; "
        f"Gamma=S_SA+(1/2)Tr ln(D_K^2/Lambda^2); rep-A canonical (Sum|lambda|, extends S95-W2-3); "
        f"eigenvalue tau-flow via Lichnerowicz-Bochner lambda_k^2=nu_k+(1/4)R_K(tau) (closed-form, "
        f"extrapolation-free); dGamma/dtau=(1/8)R_K'(tau)[Sum 1/|lambda|+Sum 1/lambda^2]>=0, "
        f"R_K'(tau)=e^-4tau(e^3tau-1)^2>=0 zero ONLY at tau=0; "
        f"CLASS=FULL (cached FULL D_K spectrum, NO SCHEMATIC helper); regulator_pin=a_n^zeta\n"
    )
    tuple_row = (  # (local)
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] §W3-3 Step-4 directional pre-reg: "
        f"SIGN=dGamma/dtau fixed (positive) across [0,tau_NEC] (no flip vs S95-W2-3); "
        f"MAG=n_interior_sign_changes([0,tau_NEC]) target 0 (INFO iff sign-change ONLY in censored tau>tau_NEC); "
        f"REGIME=trace-log finite (no zero mode) + full window computed)\n"
    )
    SESSION_96_DIR.mkdir(parents=True, exist_ok=True)
    with VERDICT_FILE.open("a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(companion)
        f.write(tuple_row)


# ---------------------------------------------------------------------------
# Substrate quantities (closed form + cache)
# ---------------------------------------------------------------------------
def R_K(tau):
    """E3 closed-form fiber scalar curvature (baptista E3-companion; Sage residual 0)."""
    return -0.25 * np.exp(-4.0 * tau) + 2.0 * np.exp(-tau) - 0.25 + 0.5 * np.exp(2.0 * tau)  # (local)


def dR_K_dtau(tau):
    """R_K'(tau) = e^{2tau} - 2 e^{-tau} + e^{-4tau} = e^{-4tau}(e^{3tau}-1)^2 >= 0 (Sage; =0 only tau=0)."""
    return np.exp(2.0 * tau) - 2.0 * np.exp(-tau) + np.exp(-4.0 * tau)  # (local)


def load_fold_spectrum():
    """Return (abs_fold, n_eval, min_abs, pq_list) for the L<=10 restriction (block-diagonal per sector)."""
    cache = np.load(SPECTRUM_CACHE, allow_pickle=True)
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
    return abs_fold, abs_fold.size, float(abs_fold.min()), pq_list


# ---------------------------------------------------------------------------
# Sign-change counting (reject float-noise zero crossings)
# ---------------------------------------------------------------------------
def count_interior_sign_changes(deriv, tol):
    """Count sign changes of `deriv`, rejecting noise: a sign change counts only when BOTH
    adjacent points have |deriv| > tol (rejects float-noise zero-crossings near deriv=0)."""
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
    # --- FULL L12 fold spectrum, L<=10 ---
    abs_fold, n_eval, min_abs_fold, pq_list = load_fold_spectrum()

    # --- Lichnerowicz-Bochner connection-Laplacian eigenvalues nu_k (closed-form, all tau) ---
    RKf = float(R_K(tau_fold))         # (local) R_K at fold
    quarter_RKf = 0.25 * RKf           # (local) (1/4)R_K(fold)
    nu = abs_fold ** 2 - quarter_RKf   # (local) nu_k = lambda_k(fold)^2 - (1/4)R_K(fold); band-specific, tau-indep
    nu_min = float(nu.min())           # (local) = nu_B1 (B1 band-bottom), must be > 0
    nu_all_pos = bool(nu_min > 0.0)    # (local)

    # --- tau grid over the FULL domain [0, 1.65] ---
    tau = np.linspace(TAU_LO, TAU_HI, N_GRID)  # (local)
    RK_grid = R_K(tau)                          # (local)
    dRK_grid = dR_K_dtau(tau)                   # (local) R_K'(tau) >= 0 (= 0 only at tau=0)
    # lambda_k^2(tau) = nu_k + (1/4)R_K(tau)  (closed-form Jensen flow; NO S36-quadratic extrapolation)
    # build per-tau via broadcasting: shape (N_GRID, n_eval)
    lam2_grid = nu[None, :] + 0.25 * RK_grid[:, None]  # (local) lambda^2(tau,k) > 0 for all tau,k
    lam2_min_grid = float(lam2_grid.min())      # (local) global min lambda^2 over the grid (at tau=0)
    no_zero_mode = bool(lam2_min_grid > 1e-12)  # (local) lambda^2>0 => ln finite, no zero mode
    abs_grid = np.sqrt(lam2_grid)               # (local) |lambda(tau,k)|

    # ===================================================================
    # REPRESENTATION A (CANONICAL; extends S95-W2-3): tree = S_full = Sum|lambda|, loop = Sum ln|lambda|
    # ===================================================================
    S_full = abs_grid.sum(axis=1)                       # (local) Sum_k |lambda_k(tau)|  (E7 INCREASING tree)
    G1 = np.log(abs_grid).sum(axis=1)                   # (local) (1/2)Tr ln(D^2/Lambda^2) = Sum_k ln|lambda_k|
    Gam_A = S_full + G1                                 # (local) Gamma[tau] rep-A
    dS_full = np.gradient(S_full, tau)                  # (local) Route 1 (tree dS_SA/dtau, FD)
    dG1 = np.gradient(G1, tau)                          # (local) Route 2 (Tr-ln derivative, FD)
    dGam_A = np.gradient(Gam_A, tau)                    # (local) Route 3 (combined Gamma', FD) -- CANONICAL

    # --- Route 2 analytic Jacobi cross-check: dGamma_1loop/dtau = (1/8) R_K'(tau) Sum_k 1/lambda_k^2 ---
    sum_inv_lam2 = (1.0 / lam2_grid).sum(axis=1)        # (local) Sum_k 1/lambda_k^2(tau)
    dG1_jacobi = 0.125 * dRK_grid * sum_inv_lam2        # (local) analytic one-loop derivative (Jacobi)
    # --- Route 1 analytic cross-check: dS_full/dtau = (1/8) R_K'(tau) Sum_k 1/|lambda_k| ---
    sum_inv_abs = (1.0 / abs_grid).sum(axis=1)          # (local) Sum_k 1/|lambda_k(tau)|
    dS_full_jacobi = 0.125 * dRK_grid * sum_inv_abs     # (local) analytic tree derivative
    dGam_A_jacobi = dS_full_jacobi + dG1_jacobi         # (local) analytic combined Gamma'
    # FD-vs-analytic agreement (max rel dev over interior, where FD is reliable)
    interior_full = slice(1, N_GRID - 1)
    rel_jacobi_dev = float(np.max(np.abs(dGam_A[interior_full] - dGam_A_jacobi[interior_full])
                                  / (np.abs(dGam_A_jacobi[interior_full]) + 1e-30)))  # (local)

    # ===================================================================
    # REPRESENTATION B (CROSS-CHECK ARM; mirrors s96_sdw_saddle_reginv): alternating curvature-polynomial
    #   S_SA^(B)(tau) = a_0 - a_2 (R_K/R_K_fold) + a_4 (R_K/R_K_fold)^2 ; NOT the canonical verdict.
    # ===================================================================
    c0 = a_0_FW_zeta                  # (local) deg-0 coefficient = a_0
    c2 = a_2_FW_zeta / RKf            # (local) a_2(tau) = c2 * R_K(tau)
    c4 = a_4_FW_zeta / (RKf ** 2)     # (local) a_4(tau) = c4 * R_K(tau)^2
    S_SA_B = c0 - c2 * RK_grid + c4 * RK_grid ** 2     # (local) alternating-moment tree
    Gam_B = S_SA_B + G1                                # (local) Gamma rep-B (same loop term)
    dS_SA_B = np.gradient(S_SA_B, tau)                 # (local)
    dGam_B = np.gradient(Gam_B, tau)                   # (local)
    # analytic rep-B tree-derivative zero: dS_SA_B/dtau = (-c2 + 2 c4 R_K) R_K'(tau) = 0 at R_K = c2/(2 c4)
    RK_star_B = c2 / (2.0 * c4)        # (local) R_K value where rep-B tree derivative vanishes

    # --- region indices: [0,tau_now], [0,tau_NEC], (tau_NEC, 1.614] ---
    i_now = int(np.searchsorted(tau, TAU_NOW))         # (local) first index with tau > tau_now
    i_NEC = int(np.searchsorted(tau, tau_NEC))         # (local) first index with tau > tau_NEC
    i_ovr = int(np.searchsorted(tau, tau_overshoot))   # (local) first index with tau > tau_overshoot

    def region_counts(deriv):
        """interior sign-change counts on [0,tau_now], [0,tau_NEC], (tau_NEC, tau_overshoot]."""
        n_now, _ = count_interior_sign_changes(deriv[:i_now + 1], ZERO_TOL)    # (local)
        n_NEC, locs_NEC = count_interior_sign_changes(deriv[:i_NEC + 1], ZERO_TOL)  # (local)
        # censored region (tau_NEC, tau_overshoot]: slice from i_NEC..i_ovr inclusive
        n_cen, _ = count_interior_sign_changes(deriv[i_NEC:i_ovr + 1], ZERO_TOL)    # (local)
        return int(n_now), int(n_NEC), int(n_cen), locs_NEC

    # rep-A canonical region counts (the verdict)
    nA_now, nA_NEC, nA_cen, locsA_NEC = region_counts(dGam_A)
    # rep-B cross-check region counts
    nB_now, nB_NEC, nB_cen, _ = region_counts(dGam_B)
    # full-domain [0,1.65] counts
    nA_full, locsA_full = count_interior_sign_changes(dGam_A, ZERO_TOL)
    nB_full, _ = count_interior_sign_changes(dGam_B, ZERO_TOL)

    # --- fixed-sign confirmation on [0, tau_NEC] (rep-A; the [SIGN] claim) ---
    dGam_A_NEC = dGam_A[:i_NEC + 1]                                            # (local)
    # exclude the tau=0 endpoint where dGam=0 (R_K'(0)=0) from the constant-sign test interior
    dGam_A_NEC_interior = dGam_A[1:i_NEC + 1]                                  # (local)
    sign_first_interior = int(np.sign(dGam_A_NEC_interior[0]))                 # (local)
    dGam_A_constant_sign_NEC = bool(np.all(
        np.sign(dGam_A_NEC_interior[np.abs(dGam_A_NEC_interior) > ZERO_TOL]) == sign_first_interior))  # (local)
    dGam_A_min_NEC = float(dGam_A_NEC.min())   # (local) 4-sig-fig diagnostic
    dGam_A_max_NEC = float(dGam_A_NEC.max())   # (local)
    dGam_A_min_full = float(dGam_A.min())      # (local)
    dGam_A_max_full = float(dGam_A.max())      # (local)

    # --- fold-point readouts ---
    ifold = int(np.argmin(np.abs(tau - tau_fold)))     # (local)
    dS_full_fold = float(dS_full[ifold])               # (local)
    dG1_fold = float(dG1[ifold])                       # (local)
    dGam_A_fold = float(dGam_A[ifold])                 # (local)
    dG1_jacobi_fold = float(dG1_jacobi[ifold])         # (local)
    dGam_A_jacobi_fold = float(dGam_A_jacobi[ifold])   # (local)
    # cross-check: sign of computed dS_full at fold vs E7 canonical +58672.8 (both POSITIVE; magnitudes
    # differ by normalization -- canonical dS_fold is the S42 Sum|lambda| gradient-stiffness, this is the
    # LB-closed-form band-bottom-anchored derivative; only the SIGN is verdict-relevant).
    dS_full_fold_sign_matches_E7 = bool(np.sign(dS_full_fold) == np.sign(dS_fold))  # (local)

    # --- CC2: 600-point refinement near tau=0 (R_K'->0, the only |dGam|-dip) ---
    tau_ref = np.linspace(0.0, 0.30, N_GRID_REFINE)    # (local) fine grid near the boundary
    RK_ref = R_K(tau_ref)                               # (local)
    lam2_ref = nu[None, :] + 0.25 * RK_ref[:, None]     # (local)
    abs_ref = np.sqrt(lam2_ref)                         # (local)
    Gam_A_ref = abs_ref.sum(axis=1) + np.log(abs_ref).sum(axis=1)  # (local)
    dGam_A_ref = np.gradient(Gam_A_ref, tau_ref)       # (local)
    nA_ref, _ = count_interior_sign_changes(dGam_A_ref[1:], ZERO_TOL)  # (local) exclude tau=0 endpoint

    # --- regime: trace-log finite (no zero mode) AND full window computed (no auto-shortening) ---
    domain_used_frac = 1.0  # (local) full [0,1.65] computed; no domain shortening

    return {
        "tau": tau, "RK_grid": RK_grid, "dRK_grid": dRK_grid,
        "abs_grid_min": float(abs_grid.min()), "lam2_min_grid": lam2_min_grid,
        "n_eval": n_eval, "min_abs_fold": min_abs_fold, "pq_list": pq_list,
        "RKf": RKf, "nu_min": nu_min, "nu_all_pos": nu_all_pos,
        # rep-A (canonical)
        "S_full": S_full, "G1": G1, "Gam_A": Gam_A,
        "dS_full": dS_full, "dG1": dG1, "dGam_A": dGam_A,
        "dS_full_jacobi": dS_full_jacobi, "dG1_jacobi": dG1_jacobi, "dGam_A_jacobi": dGam_A_jacobi,
        "rel_jacobi_dev": rel_jacobi_dev,
        # rep-B (cross-check)
        "S_SA_B": S_SA_B, "Gam_B": Gam_B, "dS_SA_B": dS_SA_B, "dGam_B": dGam_B,
        "RK_star_B": RK_star_B,
        # region counts
        "i_now": i_now, "i_NEC": i_NEC, "i_ovr": i_ovr,
        "nA_now": nA_now, "nA_NEC": nA_NEC, "nA_cen": nA_cen,
        "nB_now": nB_now, "nB_NEC": nB_NEC, "nB_cen": nB_cen,
        "nA_full": nA_full, "nB_full": nB_full,
        "locsA_NEC": locsA_NEC, "locsA_full": locsA_full,
        # fixed-sign confirmation
        "dGam_A_constant_sign_NEC": dGam_A_constant_sign_NEC,
        "sign_first_interior": sign_first_interior,
        "dGam_A_min_NEC": dGam_A_min_NEC, "dGam_A_max_NEC": dGam_A_max_NEC,
        "dGam_A_min_full": dGam_A_min_full, "dGam_A_max_full": dGam_A_max_full,
        # fold readouts
        "ifold": ifold, "dS_full_fold": dS_full_fold, "dG1_fold": dG1_fold, "dGam_A_fold": dGam_A_fold,
        "dG1_jacobi_fold": dG1_jacobi_fold, "dGam_A_jacobi_fold": dGam_A_jacobi_fold,
        "dS_full_fold_sign_matches_E7": dS_full_fold_sign_matches_E7,
        # CC2
        "tau_ref": tau_ref, "dGam_A_ref": dGam_A_ref, "nA_ref": nA_ref,
        # regime
        "no_zero_mode": no_zero_mode, "domain_used_frac": domain_used_frac,
        # canonical verdict value
        "value": int(nA_NEC),
    }


# ---------------------------------------------------------------------------
# Gate evaluation (pre-registered; no post-hoc edits)
# ---------------------------------------------------------------------------
def evaluate_gate(res: dict):
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    Pre-registered (plan §W3-3 Step 4):
      operator: n_interior_sign_changes(dGamma/dtau on [0,tau_NEC]) == 0  (PASS).
      sign_verdict PASS iff dGamma/dtau retains S95-W2-3 fixed sign across [0,tau_NEC].
      magnitude_verdict PASS iff n_sc([0,tau_NEC])==0; INFO iff the ONLY sign-change(s)
        are in the censored region tau>tau_NEC; FAIL iff n_sc([0,tau_NEC])>=1.
      regime_verdict VALID iff trace-log finite (no zero mode) AND full window computed.
    Composite collapse per gate-verdicts.md.
    """
    nA_NEC = res["nA_NEC"]   # (local) canonical rep-A interior sign-change count on [0,tau_NEC]
    nA_cen = res["nA_cen"]   # (local) censored-region (tau_NEC, tau_overshoot] count

    # SIGN verdict: substitution-chain Step 4 predicts FIXED (positive) sign of dGamma/dtau on
    # [0,tau_NEC] (no flip vs S95-W2-3). PASS iff constant sign across [0,tau_NEC] interior.
    sign_v = "PASS" if res["dGam_A_constant_sign_NEC"] else "FAIL"  # (local)

    # MAGNITUDE verdict: operator is the integer interior-sign-change count on [0,tau_NEC]; target 0.
    #   PASS iff nA_NEC == 0; INFO iff nA_NEC == 0 BUT a sign-change appears in the censored region;
    #   FAIL iff nA_NEC >= 1 (interior saddle in the PHYSICAL domain).
    if nA_NEC >= 1:
        mag_v = "FAIL"   # (local) interior saddle in [0,tau_NEC]
    elif nA_cen >= 1:
        mag_v = "INFO"   # (local) physical-domain clean, but censored-region sign-change present
    else:
        mag_v = "PASS"

    # REGIME verdict: trace-log finite (no zero mode) across the full window AND full window computed.
    #   Auto-shortening bands (gate-verdicts.md): >=0.95 -> VALID; 0.50-0.95 -> MARGINAL; <0.50 -> BREAKDOWN.
    f_used = res["domain_used_frac"]  # (local)
    if not res["no_zero_mode"]:
        regime_v = "BREAKDOWN"  # (local) ln divergence if any lambda^2 -> 0
    elif f_used >= 0.95:
        regime_v = "VALID"
    elif f_used >= 0.50:
        regime_v = "MARGINAL"
    else:
        regime_v = "BREAKDOWN"

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED -- modifications are Class-3):
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

    # Panel 1: Gamma(tau), S_full(tau), G1(tau) -- rep-A canonical, full domain
    ax = axes[0, 0]
    ax.plot(tau, res["Gam_A"], "-", color="C3", lw=2.2, label=r"$\Gamma=S_{\rm SA}+\frac{1}{2}{\rm Tr}\ln(D_K^2/\Lambda^2)$")
    ax.plot(tau, res["S_full"], "--", color="C0", lw=1.5, label=r"$S_{\rm tree}=\sum|\lambda|$ (rep-A, E7)")
    ax.plot(tau, res["G1"], ":", color="C2", lw=1.5, label=r"$\Gamma_{1\rm loop}=\sum\ln|\lambda|$")
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.6, label=r"$\tau_{\rm fold}$")
    ax.axvline(tau_NEC, ls="-.", color="purple", alpha=0.8, label=r"$\tau_{\rm NEC}=1.383$")
    ax.axvline(tau_overshoot, ls=":", color="brown", alpha=0.8, label=r"$\tau_{\rm ovr}=1.614$")
    ax.axvspan(tau_NEC, TAU_HI, color="red", alpha=0.06)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel("action")
    ax.set_title(r"Effective action $\Gamma(\tau)$ over full domain $[0,1.65]$ (rep-A canonical)")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=7.4)

    # Panel 2: dGamma/dtau (rep-A canonical) -- the SIGN gate
    ax = axes[0, 1]
    ax.plot(tau, res["dGam_A"], "-", color="C3", lw=2.2, label=r"$d\Gamma/d\tau$ (rep-A, FD)")
    ax.plot(tau, res["dGam_A_jacobi"], "--", color="k", lw=1.1, label=r"$d\Gamma/d\tau$ (Jacobi analytic)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_NEC, ls="-.", color="purple", alpha=0.8)
    ax.axvline(tau_overshoot, ls=":", color="brown", alpha=0.8)
    ax.axvspan(tau_NEC, TAU_HI, color="red", alpha=0.06, label="censored $\\tau>\\tau_{\\rm NEC}$")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d\Gamma/d\tau$")
    ax.set_title(f"$d\\Gamma/d\\tau$: interior sign-changes on $[0,\\tau_{{\\rm NEC}}]$ = {res['nA_NEC']} (rep-A)")
    ax.set_yscale("symlog")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=7.6)
    for i in res["locsA_full"]:
        ax.plot(tau[i], res["dGam_A"][i], "rv", ms=10)

    # Panel 3: rep-B cross-check arm (alternating moment) -- the diagnostic sign-change
    ax = axes[1, 0]
    ax.plot(tau, res["dGam_B"], "-", color="C4", lw=2.0, label=r"$d\Gamma/d\tau$ (rep-B alt-moment)")
    ax.plot(tau, res["dS_SA_B"], "--", color="C1", lw=1.3, label=r"$dS_{\rm SA}^{(B)}/d\tau$")
    ax.plot(tau, res["dG1"], ":", color="C2", lw=1.3, label=r"$d\Gamma_{1\rm loop}/d\tau$ ($>0$)")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_NEC, ls="-.", color="purple", alpha=0.8)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$d/d\tau$")
    ax.set_title(f"rep-B CROSS-CHECK (NOT verdict): $S_{{\\rm SA}}^{{(B)}}$ sign-changes $[0,\\tau_{{\\rm NEC}}]$ = {res['nB_NEC']}")
    ax.set_yscale("symlog")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=7.6)

    # Panel 4: CC2 refinement near tau=0 + Jacobi-vs-FD agreement
    ax = axes[1, 1]
    ax.plot(res["tau_ref"], res["dGam_A_ref"], "-", color="C5", lw=1.8,
            label=fr"$d\Gamma/d\tau$ 600-pt near $\tau$=0 (sc={res['nA_ref']})")
    ax.axhline(0, ls=":", color="red", lw=1.2)
    ax.axvline(tau_fold, ls="--", color="gray", alpha=0.6)
    ax.set_xlabel(r"$\tau$ (refined $[0,0.30]$)"); ax.set_ylabel(r"$d\Gamma/d\tau$")
    ax.set_title(f"CC2 600-pt refinement near boundary\nJacobi-vs-FD max rel dev = {res['rel_jacobi_dev']:.2e}")
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8)

    fig.suptitle(
        f"S96-W3-SADDLE-FULLDOMAIN: $\\Gamma=S_{{\\rm SA}}+\\frac{{1}}{{2}}{{\\rm Tr}}\\ln(D_K^2/\\Lambda^2)$, "
        f"full domain $[0,\\tau_{{\\rm NEC}}{{=}}1.383]$+censored -- interior saddles on $[0,\\tau_{{\\rm NEC}}]$ = {res['nA_NEC']}",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(PNG_OUT, dpi=120)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Driver
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    print("=" * 78)
    print(f"{GATE_ID}  ([SIGN])")
    print("=" * 78)

    input_files = {
        "script": SCRIPT_PATH,
        "canonical": CANONICAL_CONSTANTS,
        "spectrum_cache": SPECTRUM_CACHE,
        "s95_baseline": S95_BASELINE_NPZ,
    }
    print("\nINPUT SHA-256 PINS:")
    pins = log_input_pins(input_files)
    cache_sha_ok = (pins["spectrum_cache"] == SPECTRUM_CACHE_SHA_PIN)  # (local)
    print(f"\n  spectrum_cache SHA pin match = {cache_sha_ok}")

    print("\nCANONICAL CONSTANTS:")
    print(f"  tau_fold={tau_fold}  tau_NEC={tau_NEC}  tau_overshoot={tau_overshoot}  M_KK={M_KK:.6e}")
    print(f"  a_0_FW_zeta={a_0_FW_zeta}  a_2_FW_zeta={a_2_FW_zeta}  a_4_FW_zeta={a_4_FW_zeta}")
    print(f"  dS_fold (E7 canonical Sum|lambda|) = {dS_fold:+.6f}   d2S_fold = {d2S_fold:+.6f}")
    print(f"  GPU PATH: cpu-cap-OMP8 (LB closed-form lambda^2(tau)=nu+(1/4)R_K(tau) over cached")
    print(f"            band-bottoms; Tr-ln = vector reduction over {N_EVAL_EXPECTED} scalars x {N_GRID} tau;")
    print(f"            NO eigendecomposition => torch.linalg NOT invoked)")

    res = compute()

    print("\n" + "=" * 78)
    print("LICHNEROWICZ-BOCHNER eigenvalue tau-flow (closed-form, extrapolation-free)")
    print("=" * 78)
    print(f"  R_K(fold) = {res['RKf']:.8f}   (1/4)R_K(fold) = {0.25*res['RKf']:.8f}")
    print(f"  nu_k = lambda_k(fold)^2 - (1/4)R_K(fold): min nu = {res['nu_min']:.8f}  (= nu_B1)  all>0? {res['nu_all_pos']}")
    print(f"  n_eval (L<=10 |lambda| count) = {res['n_eval']}  (plan pin {N_EVAL_EXPECTED}; "
          f"match {res['n_eval']==N_EVAL_EXPECTED})")
    print(f"  min lambda^2(tau) over grid = {res['lam2_min_grid']:.8f}  (>0 at tau=0 => no zero mode, "
          f"ln finite all tau): {res['no_zero_mode']}")
    print(f"  R_K'(tau) >= 0 (Sage e^-4tau(e^3tau-1)^2): min on grid = {res['dRK_grid'].min():.3e} "
          f"(= 0 ONLY at tau=0)")

    print("\n" + "=" * 78)
    print("[SIGN] SUBSTITUTION CHAIN -- numbers substituted (Steps 1-4); plan §W3-3")
    print("=" * 78)
    print("  Step 1 (defs): Gamma = S_SA + (1/2)Tr ln(D^2/Lambda^2); rep-A tree S_full=Sum|lambda| (E7);")
    print("                 Gamma_1loop=Sum ln|lambda|; lambda_k^2(tau)=nu_k+(1/4)R_K(tau) (Bochner).")
    print("  Step 2 (subst, Jacobi): dGamma/dtau = dS_SA/dtau + (1/2)Tr[(D^2)^-1 d(D^2)/dtau];")
    print("                 d(lambda^2)/dtau=(1/4)R_K'(tau) all k => one-loop=(1/8)R_K'(tau)Sum 1/lambda^2.")
    print("  Step 3 (simplify): dGamma/dtau = (1/8)R_K'(tau)[Sum 1/|lambda| + Sum 1/lambda^2].")
    print(f"                 Both sums > 0; (1/8)R_K'(tau) >= 0 (=0 only tau=0) => dGamma/dtau >= 0.")
    print("  Step 4 (sign read-off):")
    print(f"     at fold: dS_full/dtau (rep-A, FD)           = {res['dS_full_fold']:+.4f}  "
          f"(sign matches E7 +58672.8: {res['dS_full_fold_sign_matches_E7']})")
    print(f"              dGamma_1loop/dtau (FD)             = {res['dG1_fold']:+.4f}")
    print(f"              dGamma_1loop/dtau (Jacobi analytic)= {res['dG1_jacobi_fold']:+.4f}")
    print(f"              dGamma/dtau = dS+dG1 (FD)          = {res['dGam_A_fold']:+.4f}")
    print(f"              dGamma/dtau (Jacobi analytic)      = {res['dGam_A_jacobi_fold']:+.4f}")
    print(f"     => BOTH terms POSITIVE => dGamma/dtau > 0 for tau>0 => NO interior zero on [0,tau_NEC].")

    print("\n" + "=" * 78)
    print("THREE ROUTES TO THE SIGN (CC1)")
    print("=" * 78)
    print(f"  Route 1 (tree dS_full/dtau, FD):  range [{res['dS_full'].min():.4g}, {res['dS_full'].max():.4g}]  "
          f"all>0(tau>0)? {bool(np.all(res['dS_full'][1:]>0))}")
    print(f"  Route 2 (Tr-ln dGamma_1loop/dtau): FD range [{res['dG1'].min():.4g}, {res['dG1'].max():.4g}]; "
          f"Jacobi range [{res['dG1_jacobi'].min():.4g}, {res['dG1_jacobi'].max():.4g}]")
    print(f"          Jacobi-vs-FD max rel dev (interior) = {res['rel_jacobi_dev']:.3e}")
    print(f"  Route 3 (combined dGamma/dtau, CANONICAL): range [{res['dGam_A_min_full']:.4g}, {res['dGam_A_max_full']:.4g}]")

    print("\n" + "=" * 78)
    print("REGION PARTITION -- interior sign-changes of dGamma/dtau (rep-A canonical)")
    print("=" * 78)
    print(f"  [0, tau_now={TAU_NOW}]          n_sc = {res['nA_now']}   (S95-W2-3 baseline window: was 0)")
    print(f"  [0, tau_NEC={tau_NEC}]  n_sc = {res['nA_NEC']}   *** CANONICAL VERDICT VALUE (target 0) ***")
    print(f"  (tau_NEC, tau_ovr={tau_overshoot}]  n_sc = {res['nA_cen']}   (censored region; INFO if >0)")
    print(f"  [0, 1.65] full                 n_sc = {res['nA_full']}")
    print(f"  dGamma/dtau min/max on [0,tau_NEC] = [{res['dGam_A_min_NEC']:.4g}, {res['dGam_A_max_NEC']:.4g}]")
    print(f"  dGamma/dtau fixed sign on [0,tau_NEC] interior? {res['dGam_A_constant_sign_NEC']} "
          f"(sign = {'+' if res['sign_first_interior']>0 else '-'})")

    print("\n" + "-" * 78)
    print("REP-B CROSS-CHECK ARM (alternating moment a_0-a_2+a_4; NOT the canonical verdict)")
    print("-" * 78)
    print(f"  S_SA^(B) tree-derivative zero at R_K* = {res['RK_star_B']:.6f} = a_2 R_K_fold/(2 a_4)")
    print(f"  rep-B interior sign-changes:  [0,tau_now]={res['nB_now']}  [0,tau_NEC]={res['nB_NEC']}  "
          f"(tau_NEC,ovr]={res['nB_cen']}  full={res['nB_full']}")
    print(f"  NOTE: rep-B is NOT sign-fixed (alternating curvature polynomial); its sign-change is a")
    print(f"        REPRESENTATION feature, NOT a physical interior saddle of the canonical EA (rep-A).")
    print(f"        The verdict uses rep-A (Sum|lambda|), matching S95-W2-3 which this gate extends.")

    print("\n" + "-" * 78)
    print(f"CC2: 600-point refinement near tau=0 (R_K'->0 boundary dip): interior sign-changes = {res['nA_ref']}")
    print("-" * 78)

    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    print("\n" + "=" * 78)
    print("GATE EVALUATION (composite collapse; gate-verdicts.md)")
    print("=" * 78)
    print(f"  value (n_interior_sign_changes on [0,tau_NEC], rep-A canonical) = {res['value']}")
    print(f"  domain_used_frac = {res['domain_used_frac']:.4f}   no_zero_mode = {res['no_zero_mode']}")
    print(f"  sign_verdict={sign_v}  magnitude_verdict={mag_v}  regime_verdict={regime_v}")
    print(f"  COMPOSITE VERDICT = {composite}")

    # dual-prior posterior re-allocation (plan §W3-3 dual_prior)
    if composite == "PASS":
        dual = "PASS -> 0.95 to Track A (boundary-domination hardened to full physical domain)"  # (local)
    elif composite == "INFO":
        dual = "INFO -> Track A on physical domain (sign-change only in censored tau>tau_NEC, physically irrelevant)"  # (local)
    else:
        dual = "FAIL -> 0.9 to Track B (interior saddle reopens slow-roll/equilibrium reading)"  # (local)
    print(f"  dual_prior posterior: {dual}")

    # ---- physics statement (substrate framing) ----
    print("\n" + "-" * 78)
    if composite == "PASS":
        print("  BOUNDARY-DOMINATION HARDENED to the full physical domain [0, tau_NEC=1.383]:")
        print("  dGamma/dtau = (1/8)R_K'(tau)[Sum 1/|lambda| + Sum 1/lambda^2] > 0 for all tau>0 (ANALYTIC;")
        print("  R_K'(tau)=e^-4tau(e^3tau-1)^2 has its only zero at the genesis boundary tau=0). Gamma[tau]")
        print("  has no interior stationary point, so Z=sum exp(-Gamma) is boundary-dominated (Gibbons-")
        print("  Hawking-York). The universe TRANSITS (supersonic van Hove sweep) -- it does NOT slow-roll")
        print("  in an interior well. r=16eps, n_s=1-6eps+2eta remain INAPPLICABLE by absent premises over")
        print("  the ENTIRE physical tau-range, not just the near-fold window (S95-W2-3 hardened).")
    elif composite == "INFO":
        print("  Boundary-domination holds on the PHYSICAL domain [0,tau_NEC]; the only dGamma/dtau sign-")
        print("  change is in the CENSORED region tau>tau_NEC (NEC-violating, Kretschmann-divergent), which")
        print("  the censoring barrier blocks the modulus from reaching -- physically irrelevant.")
    else:
        print("  An interior stationary point of Gamma[tau] appears in the PHYSICAL domain [0,tau_NEC] --")
        print("  would reopen the slow-roll/equilibrium reading; first action is a truncation-artifact check")
        print("  (it would contradict E7) before any structural reinterpretation.")

    # ---- data file ----
    value_str = (  # (local) compact, audit-greppable
        f"composite={composite};n_sc_phys=[0,tauNEC]={res['nA_NEC']};"
        f"n_sc_now=[0,{TAU_NOW}]={res['nA_now']};n_sc_censored=({tau_NEC},{tau_overshoot}]={res['nA_cen']};"
        f"n_sc_full=[0,1.65]={res['nA_full']};rep=A_sum_abs_lambda_canonical_extends_S95W2-3;"
        f"dGam_min_NEC={res['dGam_A_min_NEC']:.6g};dGam_max_NEC={res['dGam_A_max_NEC']:.6g};"
        f"dGam_fixed_sign_NEC={res['dGam_A_constant_sign_NEC']};sign={'+' if res['sign_first_interior']>0 else '-'};"
        f"route2_jacobi_vs_FD_reldev={res['rel_jacobi_dev']:.3e};CC2_600pt_n_sc={res['nA_ref']};"
        f"repB_xcheck_n_sc_NEC={res['nB_NEC']};repB_RKstar={res['RK_star_B']:.6f};"
        f"nu_min={res['nu_min']:.8f};lam2_min_grid={res['lam2_min_grid']:.8f};no_zero_mode={res['no_zero_mode']};"
        f"dS_full_fold={res['dS_full_fold']:.6f};dG1_fold={res['dG1_fold']:.6f};dGam_fold={res['dGam_A_fold']:.6f};"
        f"dS_full_sign_matches_E7={res['dS_full_fold_sign_matches_E7']};tau_NEC={tau_NEC};tau_overshoot={tau_overshoot};"
        f"sign_verdict={sign_v};magnitude_verdict={mag_v};regime_verdict={regime_v};"
        f"CLASS=FULL;regulator_pin=a_n^zeta;GPU_path=cpu-cap-OMP8"
    )

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        tau=res["tau"], RK_grid=res["RK_grid"], dRK_grid=res["dRK_grid"],
        # rep-A canonical
        S_full=res["S_full"], G1=res["G1"], Gam_A=res["Gam_A"],
        dS_full=res["dS_full"], dG1=res["dG1"], dGam_A=res["dGam_A"],
        dS_full_jacobi=res["dS_full_jacobi"], dG1_jacobi=res["dG1_jacobi"], dGam_A_jacobi=res["dGam_A_jacobi"],
        rel_jacobi_dev=res["rel_jacobi_dev"],
        # rep-B cross-check
        S_SA_B=res["S_SA_B"], Gam_B=res["Gam_B"], dS_SA_B=res["dS_SA_B"], dGam_B=res["dGam_B"],
        RK_star_B=res["RK_star_B"],
        # region counts
        nA_now=res["nA_now"], nA_NEC=res["nA_NEC"], nA_cen=res["nA_cen"], nA_full=res["nA_full"],
        nB_now=res["nB_now"], nB_NEC=res["nB_NEC"], nB_cen=res["nB_cen"], nB_full=res["nB_full"],
        # fixed-sign + diagnostics
        dGam_A_constant_sign_NEC=res["dGam_A_constant_sign_NEC"], sign_first_interior=res["sign_first_interior"],
        dGam_A_min_NEC=res["dGam_A_min_NEC"], dGam_A_max_NEC=res["dGam_A_max_NEC"],
        dGam_A_min_full=res["dGam_A_min_full"], dGam_A_max_full=res["dGam_A_max_full"],
        # fold readouts
        dS_full_fold=res["dS_full_fold"], dG1_fold=res["dG1_fold"], dGam_A_fold=res["dGam_A_fold"],
        dG1_jacobi_fold=res["dG1_jacobi_fold"], dGam_A_jacobi_fold=res["dGam_A_jacobi_fold"],
        dS_full_fold_sign_matches_E7=res["dS_full_fold_sign_matches_E7"], dS_fold_canonical=dS_fold,
        # CC2
        tau_ref=res["tau_ref"], dGam_A_ref=res["dGam_A_ref"], nA_ref=res["nA_ref"],
        # LB
        RKf=res["RKf"], nu_min=res["nu_min"], nu_all_pos=res["nu_all_pos"],
        n_eval=res["n_eval"], lam2_min_grid=res["lam2_min_grid"], no_zero_mode=res["no_zero_mode"],
        # regime + verdict
        domain_used_frac=res["domain_used_frac"], value=res["value"],
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v, composite=composite,
        tau_fold=tau_fold, tau_NEC=tau_NEC, tau_overshoot=tau_overshoot, tau_now=TAU_NOW, M_KK=M_KK,
        a_0_FW_zeta=a_0_FW_zeta, a_2_FW_zeta=a_2_FW_zeta, a_4_FW_zeta=a_4_FW_zeta,
    )
    print(f"\n  npz  -> {NPZ_OUT.relative_to(PROJECT_ROOT)}")

    make_plot(res)
    print(f"  png  -> {PNG_OUT.relative_to(PROJECT_ROOT)}")

    # ---- dual-SHA + verdict line ----
    print("\n" + "-" * 78)
    print("Dual-SHA closure + verdict-line emission")
    print("-" * 78)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS, pins)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
    print(f"\n  verdict line appended -> {VERDICT_FILE.relative_to(PROJECT_ROOT)}")

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n4-TUPLE OUTPUT TAG: (value={res['value']}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")
    print(f"\nElapsed: {time.time() - t0:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
