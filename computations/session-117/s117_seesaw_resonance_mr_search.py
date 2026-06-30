#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CF-S117-SEESAW-RESONANCE-MR-SEARCH  (Session 117, Wave 2, §W2-3)  -- [VERIFY] gate.

M_R RESONANCE SCAN, anchored on the S-3-closed fold-spectrum form diag(B1,B2,B3)
(fiber-spectrum eigenvalue-SELECTION). A_K-built degenerate diag(M0,M1,M1) forms are
OFF-FORM -> INFO not PASS (convention-shopping guard per CF-W2-2 / S-3 Result 4).

WHAT THIS GATE DOES (plan sessions/session-plan/session-117-plan-w2.md §W2-3)
----------------------------------------------------------------------------
  (i)  Resolve the (p,q)/triality label + C2(p,q) of each B-branch fold energy by
       nearest-|lambda| match against the L12 master cache sector_evals.
  (ii) Scan FIBER-SPECTRUM M_R candidates (S-3 form): a tau-scan of the B-branch
       fold energies (incl. the tau=0.107 B1-B2 crossing) x a sector-selection axis
       {three-globally-lowest, lowest-per-triality-class t in {0,1,2}}.  For each
       candidate M_R = diag(B1,B2,B3): test the single-RH-dominance resonance
       condition  M_D[2,2]/M_D[1,1] ~ sqrt(M_R[2]/M_R[1])  at the MASS-FIT Dirac seed
       (s116 texture), and recompute the seesaw -> U_PMNS -> mix_grp + R JOINTLY.
  (iii) Convention-shopping guard: A_K-built degenerate diag(M0,M1,M1) forms are
       FORBIDDEN as PASS (-> INFO).  Also test the full theta_nu envelope and a
       forced off-fold reshape as off-form references.

OPERATOR (plan §W2-3):  mix_grp(candidate) >= 3  on a fiber-spectrum (S-3-form) M_R,
  where mix_grp = #{ theta in {th12,th23,th13} : theta within NuFIT 5.2 NO 3sigma }.
  PASS iff a fiber-spectrum M_R fires mix_grp>=3;
  FAIL iff no fiber-spectrum sector-selection across the tau-moduli+sector axes reaches
       a large-enough sqrt(B2/B1) (the bowtie is structurally too flat);
  INFO iff resonance fires ONLY off-form (A_K-degenerate diag(M0,M1,M1) OR off-fold
       tau-rescaled M_R) -- NOT a substrate-natural PASS.

SUBSTRATE-FIRST (phononic-framing.md) -- GEOMETRIC:
  The scan ranges over D_K's OWN fold-eigenvalue spectrum. Each candidate M_R is a
  fiber-spectrum eigenvalue-SELECTION diag(B1,B2,B3) (S-3 OQ-4: M_R is fold-spectrum-
  split, NOT an A_K-built coupling). The resonance maps to a Casimir-gap condition on
  those eigenvalues. Direction: D_K fold spectrum -> M_R selection -> seesaw
  enhancement -> PMNS angles + R.  A_K-built degenerate diag(M0,M1,M1) is the un-used
  standard-NCG A_F coupling the framework does NOT use (D_K == D_F sources M_R from
  the spectrum) -> a resonance that fires only there is OFF-substrate -> INFO.

OPERATIONAL L_max DISCLOSURE (math-scripts.md Friedrich-Bar bottom-K saturation):
  The plan pins L_max=12 (L12 cache, for sector (p,q) resolution -- USED as pinned)
  and L_max=10 (dirac_spectrum, for the B-branch fold energies). The fiber-spectrum
  SELECTIONS (three-globally-lowest, lowest-per-triality-class) draw ONLY on the
  LOWEST |lambda| per sector, which are Friedrich-Bar bottom-K SATURATED at low
  max_pq_sum (higher sectors add only HIGHER |lambda| by Casimir scaling). The
  tau-scan therefore runs at operational max_pq_sum=4, VALIDATED at tau=0.19 against
  the L12 cache (truncation_consistent). convention tag carries the disclosure.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  computations/_shared/canonical_constants.py
  computations/session-99/s99_w3_seesaw_summnu.npz       (bare B-branch M_R triple, Y)
  computations/session-84/s84_spectrum_cache_L12_tau019.npz  (sector (p,q) resolution)
  computations/session-116/s116_lepton_pmns_texture.npz  (mass-fit M_D, U_eL, NuFIT bands)
  computations/_shared/dirac_spectrum.py                 (tau-scan of fold energies)
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; D_pi<=432x432 + 3x3 seesaw) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import itertools
import json
import sys
import time
from pathlib import Path

import numpy as np

# ---------------------------------------------------------------------------
# Section 1 -- Paths + canonical constants (MANDATORY import)
# ---------------------------------------------------------------------------
THIS = Path(__file__).resolve()
SESSION_DIR = THIS.parent                                  # computations/session-117
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import (  # noqa: E402
    M_KK, tau_fold,
    dm2_21_NuFit, dm2_31_NuFit,
)
import dirac_spectrum as ds                                # noqa: E402

import matplotlib                                          # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                            # noqa: E402

# ---------------------------------------------------------------------------
# Section 2 -- Identity + pinned machinery (plan §W2-3 machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "117"                                            # (local)
GATE_ID = "CF-S117-SEESAW-RESONANCE-MR-SEARCH"             # (local)
SCHEME = "fiber-spectrum-MR-resonance-scan"               # (local) S-3 fold-eigenvalue form ONLY
CONVENTION = ("RATIO-resonance-sqrt-MR2-MR1-Sminus3-fold-form-"
              "AK-degenerate-diagM0M1M1-INFO-not-PASS-CFW22-guard-"
              "opL4-FriedrichBar-bottomK-saturated-valid-vs-L12cache")  # (local)
L_MAX = 12                                                 # (local) plan pin: L12 cache for (p,q) resolution
OP_MAX_PQ = 4                                              # (local) operational max_pq_sum for tau-scan (FB-saturated)
TAU_FOLD = float(tau_fold)                                 # (local) 0.19 canonical

# resonance + scan machinery (plan §W2-3 pins)
EPS_RES = 0.05                                             # (local) resonance tol |MD-ratio - sqrt(MR-ratio)|
ZERO_LAM = 1e-9                                            # (local) zero-mode floor in |lambda|
PIPE_TOL = 0.018                                           # (local) distinct-pipeline cache match ~1.8% (INV11-W2-4)
TAU_LO, TAU_HI = 0.08, 0.21                                # (local) B-branch fold window (incl tau=0.107, tau_fold)

# --- NuFIT 5.2 NO 3sigma bands (# (local) class-(B) lab anchors; EXACTLY the s116 pins;
#     NOT canonical_constants -- get_constant('J_PMNS')->not-found; methodological-anchor
#     sourcing per substrate-first-canonical-sourcing.md §(i), same vintage as S115/S116) ---
S2T12_BF, S2T12_LO, S2T12_HI = 0.303,  0.270,  0.341       # (local) NuFIT 5.2 NO sin^2 th12 (3sig)
S2T23_BF, S2T23_LO, S2T23_HI = 0.572,  0.434,  0.610       # (local) NuFIT 5.2 NO sin^2 th23 (3sig, upper octant)
S2T13_BF, S2T13_LO, S2T13_HI = 0.02203, 0.02029, 0.02391   # (local) NuFIT 5.2 NO sin^2 th13 (3sig)

PUB_SIGFIGS = 6                                            # (local) Class-8.3

# ---------------------------------------------------------------------------
# Section 3 -- Tower / Casimir / PMNS helpers (REUSE s116 conventions verbatim)
# ---------------------------------------------------------------------------
def C2_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C2(p,q) = (p^2+q^2+pq+3p+3q)/3."""
    return (p * p + q * q + p * q + 3.0 * p + 3.0 * q) / 3.0


def triality(p: int, q: int) -> int:
    """SU(3) center character t(p,q) = (p-q) mod 3."""
    return (p - q) % 3


def yukawa_block_real(diag: np.ndarray, w12: float, w13: float, w23: float) -> np.ndarray:
    """Real-symmetric 3x3 Yukawa block (REAL: delta_CP in {0,pi}); s116 verbatim."""
    M = np.diag(diag).astype(float)
    M[0, 1] = M[1, 0] = w12
    M[0, 2] = M[2, 0] = w13
    M[1, 2] = M[2, 1] = w23
    return M


def diag_block(M: np.ndarray):
    """Real-symmetric eigendecomp, eigenvalues by ASCENDING |lambda| (=mass); s116 verbatim."""
    lam, U = np.linalg.eigh(M)
    order = np.argsort(np.abs(lam))
    return np.abs(lam)[order], U[:, order]


def pmns_observables(U: np.ndarray) -> dict:
    """Extract (sin^2 th13, sin^2 th12, sin^2 th23, J) from a 3x3 unitary U; s116 verbatim.
    Rows = charged-lepton flavor (e,mu,tau ascending); cols = nu mass eigenstate (1,2,3)."""
    Uabs2 = np.abs(U) ** 2                                 # (local)
    s13sq = float(Uabs2[0, 2])                             # (local) |U_e3|^2
    s13sq = min(max(s13sq, 0.0), 1.0)
    denom = 1.0 - s13sq                                    # (local) c13^2
    s12sq = float(Uabs2[0, 1] / denom) if denom > 1e-15 else 0.0  # (local)
    s23sq = float(Uabs2[1, 2] / denom) if denom > 1e-15 else 0.0  # (local)
    J = float(np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0])))  # (local)
    return {"sin2_th13": s13sq, "sin2_th12": s12sq, "sin2_th23": s23sq, "J": J}


def in_band(val: float, lo: float, hi: float) -> bool:
    return bool(lo <= val <= hi)


def mix_grp_3angle(obs: dict) -> int:
    """mix_grp = #{th12,th23,th13 within NuFIT 5.2 NO 3sigma}  (plan §W2-3 operator: 3 angles)."""
    return (int(in_band(obs["sin2_th12"], S2T12_LO, S2T12_HI))
            + int(in_band(obs["sin2_th23"], S2T23_LO, S2T23_HI))
            + int(in_band(obs["sin2_th13"], S2T13_LO, S2T13_HI)))


# ---------------------------------------------------------------------------
# Section 4 -- SHA-256 dual-SHA block (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs) -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 -- Paths/targets
# ---------------------------------------------------------------------------
OUT_NPZ = SESSION_DIR / "s117_seesaw_resonance_mr_search.npz"
OUT_PNG = SESSION_DIR / "s117_seesaw_resonance_mr_search.png"

CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"
S99_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w3_seesaw_summnu.npz"
S84_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S116_NPZ = COMPUTATIONS_DIR / "session-116" / "s116_lepton_pmns_texture.npz"
DIRAC_SPECTRUM = SHARED_DIR / "dirac_spectrum.py"

INPUT_FILES = [CANONICAL_PATH, S99_NPZ, S84_CACHE, S116_NPZ, DIRAC_SPECTRUM]


# ---------------------------------------------------------------------------
# Section 6 -- Seesaw pipeline (REUSE s116 mass-fit M_D + U_eL; vary ONLY M_R)
# ---------------------------------------------------------------------------
def seesaw_pmns(M_R_triple: np.ndarray, M_D: np.ndarray, U_eL: np.ndarray) -> dict:
    """type-I seesaw M_nu = M_D M_R^{-1} M_D^T at FIXED mass-fit M_D + U_eL; vary ONLY M_R.
    Returns the PMNS observables, mix_grp, R, and the seesaw spectrum."""
    M_R_triple = np.asarray(M_R_triple, float).ravel()
    MR_inv = np.diag(1.0 / M_R_triple)                    # (local)
    M_nu = M_D @ MR_inv @ M_D.T                           # (local) type-I seesaw
    M_nu = 0.5 * (M_nu + M_nu.T)                          # (local) symmetrize
    m_nu_vals, U_nuL = diag_block(M_nu)                   # (local) ascending |lambda|
    U_PMNS = U_eL.conj().T @ U_nuL                        # (local) rows e/mu/tau, cols 1/2/3
    obs = pmns_observables(U_PMNS)                        # (local)
    mg = mix_grp_3angle(obs)                              # (local)
    # R = Delta m^2_32 / Delta m^2_21 = (m3^2-m2^2)/(m2^2-m1^2); m1=0 => m3^2/m2^2 - 1
    m1, m2, m3 = m_nu_vals[0], m_nu_vals[1], m_nu_vals[2]  # (local)
    R = float((m3**2 - m2**2) / (m2**2 - m1**2)) if (m2**2 - m1**2) > 1e-300 else float("nan")  # (local)
    return {"obs": obs, "mix_grp": mg, "R": R, "m_nu_vals": m_nu_vals,
            "U_nuL": U_nuL, "U_PMNS": U_PMNS, "Ue1_sq": float(np.abs(U_PMNS[0, 0]) ** 2)}


def best_over_permutations(triple: np.ndarray, M_D: np.ndarray, U_eL: np.ndarray) -> dict:
    """Max mix_grp over all 6 generation-assignments of the fold triple to (M_R[0],M_R[1],M_R[2]).
    (The theta12 wall is permutation-INVARIANT; the max guards against assignment-incompleteness.)"""
    best = None                                           # (local)
    triple = np.asarray(triple, float).ravel()
    for perm in itertools.permutations(range(3)):
        cand = triple[list(perm)]
        r = seesaw_pmns(cand, M_D, U_eL)
        if best is None or r["mix_grp"] > best["mix_grp"]:
            best = r
            best["perm"] = perm
            best["M_R_perm"] = cand.copy()
    return best


def sqrt_ratios(triple: np.ndarray) -> dict:
    """All pairwise sqrt(Bj/Bi) of a sorted triple; the bowtie sharpness diagnostic."""
    t = np.sort(np.asarray(triple, float).ravel())
    return {"sqrt_21": float(np.sqrt(t[1] / t[0])),
            "sqrt_32": float(np.sqrt(t[2] / t[1])),
            "sqrt_31": float(np.sqrt(t[2] / t[0])),
            "sqrt_max": float(np.sqrt(t[2] / t[0]))}


# ---------------------------------------------------------------------------
# Section 7 -- Compute
# ---------------------------------------------------------------------------
def per_sector_min_abs(eval_data, zero=ZERO_LAM):
    """eval_data = [(p,q,evals_pi complex)] -> {(p,q): min|lambda| excluding zero modes}."""
    out = {}                                              # (local)
    for (p, q, ev) in eval_data:
        a = np.abs(np.asarray(ev).ravel())
        nz = a[a > zero]
        out[(p, q)] = float(np.min(nz)) if nz.size else float(np.min(a))
    return out


def select_globally_lowest3(secmin: dict):
    """Three globally-lowest DISTINCT |lambda| sector-minima (merge numeric degeneracies)."""
    vals = sorted(secmin.values())
    distinct = []                                         # (local)
    for v in vals:
        if not distinct or abs(v - distinct[-1]) > 1e-6:
            distinct.append(v)
        if len(distinct) == 3:
            break
    return np.array(distinct[:3], float)


def select_lowest_per_triality(secmin: dict):
    """Lowest |lambda| sector-minimum in each triality class t in {0,1,2}."""
    by_t = {0: [], 1: [], 2: []}                          # (local)
    for (p, q), v in secmin.items():
        by_t[triality(p, q)].append(v)
    return np.array([min(by_t[t]) for t in (0, 1, 2)], float)


def nearest_sector(secmin_pairs, lam):
    """Nearest (p,q) by |lambda| match (all eigenvalues, not just minima)."""
    best = min(secmin_pairs, key=lambda pr: abs(pr[1] - lam))
    return best[0], best[1], abs(best[1] - lam) / lam


def compute() -> dict:
    res: dict = {}
    np.set_printoptions(precision=6, suppress=False, linewidth=140)

    # ===== STEP 0: load mass-fit M_D + U_eL (s116) and bare triple (s99) =====
    d116 = np.load(S116_NPZ, allow_pickle=True)
    d99 = np.load(S99_NPZ, allow_pickle=True)
    U_eL = np.asarray(d116["U_eL"], float)                # (local) FIXED charged-lepton rotation
    Y_nu_diag = np.asarray(d116["Y_nu_diag"], float).ravel()  # (local) [0, 4.794, 11.928] rank-2
    w23_nu = float(d116["w23_nu"])                        # (local) shared eps_LX 2-3 neutrino texture
    M_D = yukawa_block_real(Y_nu_diag, 0.0, 0.0, w23_nu)  # (local) mass-fit M_D (m_1=0 rank def)
    M_R_bare = np.asarray(d99["M_R_MKK"], float).ravel()  # (local) [1.0044,1.0786,1.1700] bare B-branch
    s116_mixgrp = int(d116["mix_grp"])                    # (local) s116 baseline (4-slot incl J)
    Y_ratio = float(Y_nu_diag[2] / Y_nu_diag[1])          # (local) Dirac hierarchy M_D[2,2]/M_D[1,1]
    Ue1_sq_fixed = float(np.abs(U_eL[0, 0]) ** 2)         # (local) |U_e1|^2 = |U_eL[0,0]|^2 (M_R-INVARIANT)
    res["Y_ratio_MD"] = Y_ratio
    res["Ue1_sq_fixed"] = Ue1_sq_fixed
    res["M_R_bare"] = M_R_bare
    res["s116_mixgrp_4slot"] = s116_mixgrp
    print("=== STEP 0: mass-fit M_D + U_eL (s116), bare B-branch M_R (s99) ===")
    print(f"  M_D diag (Y_nu) = {Y_nu_diag}; w23_nu = {w23_nu:.5f}; Dirac ratio Y3/Y2 = {Y_ratio:.5f}")
    print(f"  bare M_R triple = {M_R_bare} (M_KK)")
    print(f"  |U_e1|^2 = |U_eL[0,0]|^2 = {Ue1_sq_fixed:.6f}  (M_R-INVARIANT: nu_1 decoupled, m_1=0)")

    # ===== STEP 1: STRUCTURAL WALL -- theta12 is M_R-invariant (rank-2 decoupling) =====
    # nu_1 is Dirac-decoupled (Y_1=0 => m_1=0) => U_nuL[0,:]=[1,0,0] for ALL M_R =>
    # U_PMNS[0,0]=conj(U_eL[0,0]) => |U_e1|^2 = |U_eL[0,0]|^2 INDEPENDENT of M_R.
    # NuFIT: |U_e1|^2 = cos^2 th12 cos^2 th13 ~ (1-0.303)(1-0.02203) = 0.6817.
    # => cos^2 th12 = |U_e1|^2 / cos^2 th13 <= |U_e1|^2 => sin^2 th12 >= 1 - |U_e1|^2.
    nufit_Ue1_sq = (1.0 - S2T12_BF) * (1.0 - S2T13_BF)    # (local) cos^2 th12 cos^2 th13 (NuFIT 5.2)
    sin2_th12_floor = 1.0 - Ue1_sq_fixed                  # (local) hard lower bound (cos^2 th13<=1)
    th12_ever_reachable = (sin2_th12_floor <= S2T12_HI)   # (local) can th12 EVER enter band?
    res["nufit_Ue1_sq"] = float(nufit_Ue1_sq)
    res["sin2_th12_floor"] = float(sin2_th12_floor)
    res["th12_ever_reachable"] = bool(th12_ever_reachable)
    res["Ue1_deficit_factor"] = float(nufit_Ue1_sq / Ue1_sq_fixed)
    print("\n=== STEP 1: structural wall (theta12 M_R-invariant from rank-2 decoupling) ===")
    print(f"  |U_e1|^2 framework = {Ue1_sq_fixed:.6f}  vs NuFIT cos^2th12 cos^2th13 = {nufit_Ue1_sq:.6f} "
          f"(deficit {nufit_Ue1_sq/Ue1_sq_fixed:.1f}x)")
    print(f"  => sin^2 th12 >= 1 - |U_e1|^2 = {sin2_th12_floor:.6f}  (band upper edge {S2T12_HI})")
    print(f"  => th12 EVER in band for ANY M_R? {th12_ever_reachable}  "
          f"=> mix_grp <= {'3' if th12_ever_reachable else '2'} (theta12 slot {'open' if th12_ever_reachable else 'WALLED'})")

    # ===== STEP 2: anchor -- bare triple reproduces the s116 baseline =====
    bare = seesaw_pmns(M_R_bare, M_D, U_eL)
    res["bare_obs"] = bare["obs"]
    res["bare_mixgrp_3angle"] = bare["mix_grp"]
    res["bare_R"] = bare["R"]
    res["bare_Ue1_sq"] = bare["Ue1_sq"]
    s116_th12 = float(d116["sin2_th12"]); s116_th23 = float(d116["sin2_th23"]); s116_th13 = float(d116["sin2_th13"])
    repro_ok = (abs(bare["obs"]["sin2_th12"] - s116_th12) < 1e-6
                and abs(bare["obs"]["sin2_th23"] - s116_th23) < 1e-6
                and abs(bare["obs"]["sin2_th13"] - s116_th13) < 1e-6)
    res["s116_reproduction_ok"] = bool(repro_ok)
    print("\n=== STEP 2: anchor (bare triple reproduces s116) ===")
    print(f"  bare: sin2_th12={bare['obs']['sin2_th12']:.5f} th23={bare['obs']['sin2_th23']:.5f} "
          f"th13={bare['obs']['sin2_th13']:.5f}  mix_grp(3ang)={bare['mix_grp']}  R={bare['R']:.3f}")
    print(f"  s116: sin2_th12={s116_th12:.5f} th23={s116_th23:.5f} th13={s116_th13:.5f}  "
          f"(reproduced={repro_ok})")
    # s99 aligned-basis R (diagonal M_D, oscillation-anchored)
    m_nu_s99 = np.asarray(d99["m_nu_eV"], float).ravel()  # (local) [0,0.00868,0.04953]
    R_s99 = float((m_nu_s99[2]**2 - m_nu_s99[1]**2) / (m_nu_s99[1]**2)) if m_nu_s99[1] > 0 else float("nan")
    R_osc = float(dm2_31_NuFit / dm2_21_NuFit)            # (local) NuFit-6.0 R ~ 33.5
    res["R_s99_aligned"] = R_s99
    res["R_osc_anchor"] = R_osc
    print(f"  R(aligned s99 diag M_D) = {R_s99:.3f}; R_osc(NuFit) = {R_osc:.3f}; R(textured bare) = {bare['R']:.3f}")

    # ===== STEP 3: L12-cache sector resolution of the bare B-branch triple =====
    cache = np.load(S84_CACHE, allow_pickle=True)
    se = cache["sector_evals"].item()                    # (local) {(p,q): {dim,level,abs_evals}}
    allpairs = []                                        # (local) (pq, |lambda|) over all sectors
    secmin_cache = {}                                    # (local) {(p,q): min|lambda|}
    for (p, q), val in se.items():
        a = np.abs(np.asarray(val["abs_evals"], float).ravel())
        for lam in a:
            allpairs.append(((p, q), lam))
        nz = a[a > ZERO_LAM]
        secmin_cache[(p, q)] = float(np.min(nz)) if nz.size else float(np.min(a))
    bbranch_resolution = []                              # (local)
    for mr in M_R_bare:
        pq, lam, rel = nearest_sector(allpairs, mr)
        bbranch_resolution.append((tuple(int(x) for x in pq), float(lam), float(rel),
                                   float(C2_su3(*pq)), int(triality(*pq))))
    res["bbranch_resolution"] = bbranch_resolution
    print("\n=== STEP 3: L12-cache (p,q)/C2/triality resolution of bare B-branch triple ===")
    for mr, (pq, lam, rel, c2, t) in zip(M_R_bare, bbranch_resolution):
        print(f"  M_R={mr:.5f} -> sector {pq} |lam|={lam:.5f} reldiff={rel:.4f} C2={c2:.4f} tri={t}")

    # ===== STEP 4: tau-scan x sector-selection (the FIBER-SPECTRUM / on-form search) =====
    # validate operational max_pq_sum=4 against the L12 cache at tau_fold first.
    print("\n=== STEP 4: tau-scan x sector-selection {globally-lowest-3, lowest-per-triality} ===")
    gens = ds.su3_generators()                            # (local)
    f_abc = ds.compute_structure_constants(gens)          # (local)
    gammas = ds.build_cliff8()                            # (local)

    # validate FB bottom-K saturation at tau=0.19 (op L4 vs L12 cache)
    _, eval_fold = ds.collect_spectrum(TAU_FOLD, gens, f_abc, gammas,
                                       max_pq_sum=OP_MAX_PQ, verbose=False)
    secmin_op = per_sector_min_abs(eval_fold)
    g3_op = select_globally_lowest3(secmin_op)
    g3_cache = select_globally_lowest3(secmin_cache)
    tri_op = select_lowest_per_triality(secmin_op)
    tri_cache = select_lowest_per_triality(secmin_cache)
    trunc_g3 = float(np.max(np.abs(g3_op - g3_cache) / g3_cache))   # (local)
    trunc_tri = float(np.max(np.abs(tri_op - tri_cache) / tri_cache))  # (local)
    truncation_consistent = bool(trunc_g3 < PIPE_TOL and trunc_tri < PIPE_TOL)
    res["truncation_consistent"] = truncation_consistent
    res["trunc_reldiff_g3"] = trunc_g3
    res["trunc_reldiff_tri"] = trunc_tri
    print(f"  op-L{OP_MAX_PQ} globally-lowest-3 @tau_fold = {g3_op}  (L12 cache {g3_cache}; reldiff {trunc_g3:.4f})")
    print(f"  op-L{OP_MAX_PQ} lowest-per-tri  @tau_fold = {tri_op}  (L12 cache {tri_cache}; reldiff {trunc_tri:.4f})")
    print(f"  Friedrich-Bar bottom-K saturation truncation_consistent = {truncation_consistent}")

    # tau grid: >=50 pts across [0.08,0.21] + refine near the tau=0.107 B1-B2 crossing
    tau_grid = np.unique(np.concatenate([
        np.linspace(TAU_LO, TAU_HI, 53),
        np.linspace(0.100, 0.115, 11),                   # (local) refine the tau=0.107 crossing
    ]))                                                  # (local) ~62 tau points
    selections = ("globally_lowest_3", "lowest_per_triality")

    scan_rows = []                                       # (local) one row per (tau, selection)
    onform_max_mixgrp = 0                                # (local)
    onform_max_sqrt32 = 0.0                              # (local) max bowtie sharpness on-form
    for tau in tau_grid:
        _, eval_data = ds.collect_spectrum(float(tau), gens, f_abc, gammas,
                                           max_pq_sum=OP_MAX_PQ, verbose=False)
        secmin = per_sector_min_abs(eval_data)
        for sel in selections:
            triple = (select_globally_lowest3(secmin) if sel == "globally_lowest_3"
                      else select_lowest_per_triality(secmin))
            sr = sqrt_ratios(triple)
            best = best_over_permutations(triple, M_D, U_eL)
            res_fire = bool(abs(Y_ratio - sr["sqrt_max"]) < EPS_RES)
            scan_rows.append({
                "tau": float(tau), "selection": sel, "triple": triple.tolist(),
                "sqrt_21": sr["sqrt_21"], "sqrt_32": sr["sqrt_32"], "sqrt_31": sr["sqrt_31"],
                "sqrt_max": sr["sqrt_max"], "resonance_fired": res_fire,
                "mix_grp": int(best["mix_grp"]), "R": float(best["R"]),
                "sin2_th12": float(best["obs"]["sin2_th12"]),
                "sin2_th23": float(best["obs"]["sin2_th23"]),
                "sin2_th13": float(best["obs"]["sin2_th13"]),
            })
            onform_max_mixgrp = max(onform_max_mixgrp, int(best["mix_grp"]))
            onform_max_sqrt32 = max(onform_max_sqrt32, sr["sqrt_max"])
    res["scan_rows"] = scan_rows
    res["onform_max_mixgrp"] = onform_max_mixgrp
    res["onform_max_sqrt_ratio"] = onform_max_sqrt32
    res["onform_resonance_ever_fired"] = bool(any(r["resonance_fired"] for r in scan_rows))
    n_pass = sum(1 for r in scan_rows if r["mix_grp"] >= 3)  # (local)
    res["onform_n_candidates"] = len(scan_rows)
    res["onform_n_pass"] = n_pass
    print(f"  scanned {len(scan_rows)} on-form candidates ({len(tau_grid)} tau x 2 selections)")
    print(f"  on-form max sqrt(B_max/B_min) = {onform_max_sqrt32:.5f}  (resonance needs ~ Y3/Y2 = {Y_ratio:.3f})")
    print(f"  on-form resonance EVER fired (|Y3/Y2 - sqrt-ratio|<{EPS_RES}) = {res['onform_resonance_ever_fired']}")
    print(f"  on-form max mix_grp = {onform_max_mixgrp}/3;  #candidates with mix_grp>=3 = {n_pass}")

    # ===== STEP 5: off-form references (convention-shopping guard) =====
    print("\n=== STEP 5: off-form references (CF-W2-2 convention-shopping guard) ===")
    # (a) full theta_nu envelope [0,pi/2] with FIXED U_eL -- the ABSOLUTE mix_grp ceiling
    th_grid = np.linspace(0.0, np.pi / 2.0, 721)          # (local)
    env_max = 0                                            # (local)
    for th in th_grid:
        c, s = np.cos(th), np.sin(th)
        U_nu = np.array([[1.0, 0.0, 0.0], [0.0, c, -s], [0.0, s, c]])  # (local) pure 2-3 rotation
        env_max = max(env_max, mix_grp_3angle(pmns_observables(U_eL.conj().T @ U_nu)))
    res["theta_nu_envelope_max_mixgrp"] = int(env_max)
    print(f"  (a) full theta_nu in [0,pi/2] envelope (fixed U_eL): max mix_grp = {env_max}/3")

    # (b) A_K-built degenerate diag(M0,M1,M1) -- OFF-FORM (un-used standard-NCG A_F coupling)
    ak_max = 0                                             # (local)
    ratio_grid = np.concatenate([np.linspace(1.0, 50.0, 60), np.array([Y_ratio**2])])  # (local) M1/M0
    for r0 in ratio_grid:
        for trip in ([1.0, r0, r0], [r0, 1.0, 1.0]):     # (local) diag(M0,M1,M1) both orderings
            ak_max = max(ak_max, best_over_permutations(np.array(trip), M_D, U_eL)["mix_grp"])
    res["ak_degenerate_max_mixgrp"] = int(ak_max)
    print(f"  (b) A_K-built degenerate diag(M0,M1,M1) [OFF-FORM]: max mix_grp = {ak_max}/3 "
          f"(-> INFO not PASS even if >=3, CF-W2-2 guard)")

    # (c) off-fold forced-reshape M_R: force sqrt(MR[2]/MR[1]) = Y3/Y2 EXACTLY (non-fold)
    reshape_max = 0                                       # (local)
    for r31 in np.linspace(1.0, (Y_ratio**2) * 4.0, 80):  # (local) span the needed gap and beyond
        trip = np.array([1.0, Y_ratio**2, r31 if r31 > Y_ratio**2 else (Y_ratio**2) * 1.5])
        reshape_max = max(reshape_max, best_over_permutations(trip, M_D, U_eL)["mix_grp"])
    res["offfold_reshape_max_mixgrp"] = int(reshape_max)
    print(f"  (c) off-fold forced-reshape (sqrt-ratio={Y_ratio:.2f}) [OFF-FORM]: max mix_grp = {reshape_max}/3")

    offform_fires = bool(max(ak_max, reshape_max, env_max) >= 3)
    res["offform_fires"] = offform_fires
    print(f"  off-form fires mix_grp>=3 anywhere = {offform_fires}")

    return res


# ---------------------------------------------------------------------------
# Section 8 -- Verdict (plan §W2-3 rubric: on-form PASS / off-form INFO / flat FAIL)
# ---------------------------------------------------------------------------
def verdict_from(res: dict) -> str:
    onform_pass = res["onform_max_mixgrp"] >= 3
    offform_fires = res["offform_fires"]
    if onform_pass:
        return "PASS"          # fiber-spectrum (S-3-form) M_R fires mix_grp>=3 ON-FORM
    if offform_fires:
        return "INFO"          # resonance fires ONLY off-form (A_K-degenerate / off-fold)
    return "FAIL"              # flat bowtie + theta12 wall: no substrate-natural mix_grp>=3


# ---------------------------------------------------------------------------
# Section 9 -- Plot
# ---------------------------------------------------------------------------
def make_plot(res: dict, verdict: str) -> None:
    rows = res["scan_rows"]
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.4))

    # Panel 1: bowtie sharpness sqrt(B_max/B_min) across tau, per selection, vs needed Y3/Y2
    ax = axes[0]
    for sel, col in (("globally_lowest_3", "tab:blue"), ("lowest_per_triality", "tab:orange")):
        rr = [r for r in rows if r["selection"] == sel]
        taus = [r["tau"] for r in rr]; sq = [r["sqrt_max"] for r in rr]
        ax.plot(taus, sq, ".-", color=col, ms=4, lw=1.0, label=sel)
    ax.axhline(res["Y_ratio_MD"], color="tab:red", ls="--", lw=1.8,
               label=f"resonance need Y3/Y2={res['Y_ratio_MD']:.2f}")
    ax.axvline(0.107, color="gray", ls=":", lw=1.2, label="tau=0.107 (B1-B2 crossing)")
    ax.axvline(TAU_FOLD, color="k", ls=":", lw=1.0, label=f"tau_fold={TAU_FOLD}")
    ax.set_xlabel("tau"); ax.set_ylabel("sqrt(B_max/B_min)")
    ax.set_title(f"Bowtie sharpness vs resonance need\non-form max = {res['onform_max_sqrt_ratio']:.3f} "
                 f"<< need {res['Y_ratio_MD']:.2f}")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # Panel 2: mix_grp across tau (on-form) + off-form references + envelope ceiling
    ax = axes[1]
    for sel, col in (("globally_lowest_3", "tab:blue"), ("lowest_per_triality", "tab:orange")):
        rr = [r for r in rows if r["selection"] == sel]
        ax.plot([r["tau"] for r in rr], [r["mix_grp"] for r in rr], ".-", color=col, ms=4, lw=1.0, label=sel)
    ax.axhline(3, color="tab:green", ls="--", lw=1.6, label="PASS boundary mix_grp>=3")
    ax.axhline(res["theta_nu_envelope_max_mixgrp"], color="purple", ls=":", lw=1.5,
               label=f"theta_nu envelope ceiling = {res['theta_nu_envelope_max_mixgrp']}")
    ax.set_ylim(-0.3, 3.4); ax.set_xlabel("tau"); ax.set_ylabel("mix_grp (3 angles)")
    ax.set_title(f"mix_grp across tau-moduli (on-form)\non-form max = {res['onform_max_mixgrp']}/3 => {verdict}")
    ax.legend(fontsize=7.5); ax.grid(alpha=0.3)

    # Panel 3: the structural theta12 wall + checklist
    ax = axes[2]; ax.axis("off")
    ax.text(0.0, 1.0, f"{GATE_ID}\nverdict => {verdict}", fontsize=11, weight="bold",
            transform=ax.transAxes, va="top")
    txt = (
        f"STRUCTURAL WALL (M_R-INVARIANT):\n"
        f"  nu_1 decoupled (Y_1=0 => m_1=0) => U_nuL[0,:]=[1,0,0]\n"
        f"  => |U_e1|^2 = |U_eL[0,0]|^2 = {res['Ue1_sq_fixed']:.5f}  (any M_R)\n"
        f"  NuFIT cos^2th12 cos^2th13 = {res['nufit_Ue1_sq']:.5f}  ({res['Ue1_deficit_factor']:.0f}x deficit)\n"
        f"  => sin^2 th12 >= {res['sin2_th12_floor']:.5f} > band hi {S2T12_HI}\n"
        f"  => theta12 slot WALLED for ALL M_R => mix_grp <= 2\n\n"
        f"FLAT-BOWTIE (fiber-spectrum):\n"
        f"  on-form max sqrt(B2/B1) = {res['onform_max_sqrt_ratio']:.4f}\n"
        f"  resonance need Y3/Y2 = {res['Y_ratio_MD']:.3f}  (NEVER fired)\n"
        f"  bare triple {np.round(res['M_R_bare'],4)}\n"
        f"  -> sectors {[r[0] for r in res['bbranch_resolution']]}\n"
        f"     C2 {[round(r[3],2) for r in res['bbranch_resolution']]}\n\n"
        f"on-form max mix_grp     = {res['onform_max_mixgrp']}/3 ({res['onform_n_pass']} pass)\n"
        f"theta_nu envelope max   = {res['theta_nu_envelope_max_mixgrp']}/3\n"
        f"A_K-degenerate max      = {res['ak_degenerate_max_mixgrp']}/3 (OFF-FORM)\n"
        f"off-fold reshape max    = {res['offfold_reshape_max_mixgrp']}/3 (OFF-FORM)\n"
        f"bare R(textured)={res['bare_R']:.2f}  R_osc={res['R_osc_anchor']:.2f}"
    )
    ax.text(0.0, 0.90, txt, fontsize=7.7, transform=ax.transAxes, va="top", family="monospace")

    fig.suptitle(f"{GATE_ID}: seesaw single-RH-dominance resonance scan over fiber-spectrum M_R "
                 f"(D_K fold energies); op-L{OP_MAX_PQ} (FB-saturated vs L12 cache)", fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 10 -- Verdict payload (race-safe MCP single-writer)
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None) -> dict:
    payload = {
        "session": int(SESSION),
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 11 -- Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                      # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL_PATH, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    res = compute()
    verdict = verdict_from(res)

    # persist arrays + scalars
    scan = res["scan_rows"]
    np.savez(
        OUT_NPZ,
        verdict=verdict,
        # structural wall
        Ue1_sq_fixed=res["Ue1_sq_fixed"], nufit_Ue1_sq=res["nufit_Ue1_sq"],
        sin2_th12_floor=res["sin2_th12_floor"], th12_ever_reachable=res["th12_ever_reachable"],
        Ue1_deficit_factor=res["Ue1_deficit_factor"],
        Y_ratio_MD=res["Y_ratio_MD"],
        # anchor
        M_R_bare=res["M_R_bare"], bare_mixgrp_3angle=res["bare_mixgrp_3angle"],
        bare_R=res["bare_R"], R_s99_aligned=res["R_s99_aligned"], R_osc_anchor=res["R_osc_anchor"],
        s116_reproduction_ok=res["s116_reproduction_ok"], s116_mixgrp_4slot=res["s116_mixgrp_4slot"],
        # sector resolution
        bbranch_pq=np.array([r[0] for r in res["bbranch_resolution"]]),
        bbranch_C2=np.array([r[3] for r in res["bbranch_resolution"]]),
        bbranch_tri=np.array([r[4] for r in res["bbranch_resolution"]]),
        bbranch_reldiff=np.array([r[2] for r in res["bbranch_resolution"]]),
        # FB saturation
        truncation_consistent=res["truncation_consistent"],
        trunc_reldiff_g3=res["trunc_reldiff_g3"], trunc_reldiff_tri=res["trunc_reldiff_tri"],
        # scan arrays
        scan_tau=np.array([r["tau"] for r in scan]),
        scan_selection=np.array([r["selection"] for r in scan]),
        scan_triple=np.array([r["triple"] for r in scan]),
        scan_sqrt_max=np.array([r["sqrt_max"] for r in scan]),
        scan_sqrt_21=np.array([r["sqrt_21"] for r in scan]),
        scan_sqrt_32=np.array([r["sqrt_32"] for r in scan]),
        scan_resonance_fired=np.array([r["resonance_fired"] for r in scan]),
        scan_mixgrp=np.array([r["mix_grp"] for r in scan]),
        scan_R=np.array([r["R"] for r in scan]),
        scan_sin2_th12=np.array([r["sin2_th12"] for r in scan]),
        scan_sin2_th23=np.array([r["sin2_th23"] for r in scan]),
        scan_sin2_th13=np.array([r["sin2_th13"] for r in scan]),
        # summary
        onform_max_mixgrp=res["onform_max_mixgrp"],
        onform_max_sqrt_ratio=res["onform_max_sqrt_ratio"],
        onform_resonance_ever_fired=res["onform_resonance_ever_fired"],
        onform_n_candidates=res["onform_n_candidates"], onform_n_pass=res["onform_n_pass"],
        theta_nu_envelope_max_mixgrp=res["theta_nu_envelope_max_mixgrp"],
        ak_degenerate_max_mixgrp=res["ak_degenerate_max_mixgrp"],
        offfold_reshape_max_mixgrp=res["offfold_reshape_max_mixgrp"],
        offform_fires=res["offform_fires"],
        EPS_RES=EPS_RES, OP_MAX_PQ=OP_MAX_PQ, L_MAX=L_MAX,
        audit_sha256=audit_sha, content_sha256=content_sha,
        scheme=SCHEME, convention=CONVENTION,
    )
    make_plot(res, verdict)

    value = (f"mix_grp_onform_max={res['onform_max_mixgrp']}/3(n_pass={res['onform_n_pass']}/"
             f"{res['onform_n_candidates']});sqrt(B2/B1)_onform_max={res['onform_max_sqrt_ratio']:.4f}"
             f"(need_Y3/Y2={res['Y_ratio_MD']:.3f},reson_fired={res['onform_resonance_ever_fired']});"
             f"theta12_WALLED(|Ue1|^2={res['Ue1_sq_fixed']:.5f}_vs_NuFIT{res['nufit_Ue1_sq']:.4f}_"
             f"{res['Ue1_deficit_factor']:.0f}x_deficit_MR-invariant=>sin2th12_floor={res['sin2_th12_floor']:.4f});"
             f"theta_nu_env_max={res['theta_nu_envelope_max_mixgrp']}/3;"
             f"AKdegen_max={res['ak_degenerate_max_mixgrp']}/3_OFFFORM;"
             f"reshape_max={res['offfold_reshape_max_mixgrp']}/3_OFFFORM;"
             f"FB-sat_vs_L12={res['truncation_consistent']};bare_R={res['bare_R']:.2f}")
    print()
    print(emit_4tuple(value, SCHEME, CONVENTION, L_MAX))
    note = ("flat-bowtie + theta12 rank-2-decoupling wall: no fiber-spectrum (S-3-form) M_R "
            "reaches mix_grp>=3; A_K-degenerate diag(M0,M1,M1) off-form also <3 => clean FAIL")
    print_verdict_payload(verdict, value, audit_sha, content_sha, companion_note=note)

    wall = time.time() - t0                               # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
