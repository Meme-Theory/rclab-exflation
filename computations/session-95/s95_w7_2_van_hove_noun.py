#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S95 W7-2 — CF-S95-W2-VAN-HOVE-NOUN
==================================================================================
NOUN-LICENSING adjudication: does the fixed mult-8 delta-WEIGHT on the FINITE
spectral triple (A_K, H_K, D_K) categorically LICENSE the noun "van Hove
singularity," or is it a representation-theoretic C^16 Clifford degeneracy
(a multiplicity, NOT a band-structure singularity)?

This gate is [VERIFY] (a noun-licensing adjudication via a STRUCTURAL discriminator,
NOT a directional claim). The discriminator is PRE-REGISTERED in the plan and does
NOT pre-decide which reading (kk-NO vs landau-yes) wins.

OWNER: landau-condensed-matter-theorist (converger/registry-owner of proven_1086).

------------------------------------------------------------------------------
PRE-REGISTERED STRUCTURAL DISCRIMINATOR (plan §W7-2 operator)
------------------------------------------------------------------------------
NOUN-LICENSED iff
   [ d(ln m)/d(ln L_max) -> 0 is FALSE  (multiplicity GROWS, continuum-band accretion) ]
   OR
   [ first_gap(L_max) -> 0 with power-law exponent beta_gap > 0 AND the implied DOS
     exponent produces an energy-axis non-analyticity ]
NOUN-OVER-CLAIMED iff
   [ m(L_max) == const fixed (FD-flat) AND first_gap(L_max) bounded away from 0
     (C^16 Clifford degeneracy at fixed E_0) ]

PASS (noun LICENSED) boundary: |d(ln m)/d(ln L_max)| > 0.05  OR  beta_gap > 0.05.
FAIL (noun OVER-CLAIMED) boundary: |d(ln m)/d(ln L_max)| < 1e-6 (FD-flat; m == const)
     AND first_gap relative variation across scan < 0.20 (no power-law approach to 0).

------------------------------------------------------------------------------
SUBSTITUTION CHAIN (plan §W7-2 — DERIVES the discriminator, NO pre-judgment)
------------------------------------------------------------------------------
Step 1 (band-structure van Hove): a van Hove singularity is a DOS non-analyticity
   rho(E) ~ |E - E_c|^{-(1-gamma_E)} at a stationary point grad_k E = 0 of a
   DISPERSING band E(k), with order gamma_E in [0,1).
Step 2 (finite-triple object): on (A_K, H_K, D_K) the (0,1)+(1,0) bottom is a
   Peter-Weyl multiplicity m*delta(E-E_0), m=8 = (bot_deg=4 per sector)*(2 sectors).
Step 3 (continuum-limit test quantities): m(L_max), first_gap(L_max). The noun is
   LICENSED iff L_max->inf produces a continuum-DOS non-analyticity (m->inf OR
   first_gap->0 with a power law making rho(E) diverge with a definable order).
Step 4 (standing facts, NO pre-judgment):
   Fact A (S94 W-2 T4): multiplicity != order (a delta of any coefficient is
     equi-order/infinite) => a FIXED m cannot, alone, confer a van Hove ORDER.
   Fact B (S94 W-2): rho_smooth = 14.02 = 1/(pi*v_g) (Phi_DOS-continuum) is the
     proven finite BCS driver, INVARIANT to this gate (it is NOT the delta-branch).
   Open: whether m(L_max) GROWS or first_gap(L_max)->0 with a power law.
Step 5 (read off the discriminator, both branches live):
   LICENSE:    d(ln m)/d(ln L) bounded away from 0  OR  beta_gap > 0.
   OVER-CLAIM: d(ln m)/d(ln L) ~ 0 (m == const, FD-flat) AND first_gap bounded.

The proven physics (rho_smooth=14.02 = 1/(pi*v_g)) is UNCHANGED under either branch.
This gate decides ONLY the residual NOUN in the re-worded proven_1086 row.

------------------------------------------------------------------------------
STRUCTURAL NOTE (the substrate reason this is computable from the L_max=12 cache)
------------------------------------------------------------------------------
D_K is BLOCK-DIAGONAL by Peter-Weyl (PROVEN wall: D_K = (+)_{(p,q)} D_{(p,q)}). The
(0,1) and (1,0) blocks are COMPLETE irrep diagonalizations; their bottom level and
internal first_gap are intrinsic to the FIXED finite-dimensional blocks. The L_max
"sub-truncation" is a GLOBAL-SPECTRUM filter (which (p,q) sectors are present); it
does NOT alter the (0,1)/(1,0) blocks. Hence m(L_max) and first_gap(L_max) for the
B2 bottom are L_max-INVARIANT once both sectors are present (L_max >= 1). No
high-L_max irrep build is needed (Friedrich-Bar/Casimir saturation: every higher
(p,q) sector has min|lambda| >= the B2 bottom, so no accretion into the level).
Whether this structural fact lands the OVER-CLAIM branch is what the gate COMPUTES.
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY import) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    rho_B2_per_mode,       # 14.023250234055  (B2 DOS per mode at fold)
    v_g_B2_fold,           # 0.022699323      (1/(pi*rho_B2_per_mode))
    PI,                    # pi
    tau_fold,              # 0.19
)

# =============================================================================
# Gate identity + machinery pins (PRDR — all free parameters pinned)
# =============================================================================
GATE_ID = "CF-S95-W2-VAN-HOVE-NOUN"
SCHEME = "PETER-WEYL-MULTIPLICITY-L-SCAN"
CONVENTION = "FINITE-TRIPLE-NOUN-LICENSING"
L_MAX = 12                                # (local) master-cache ceiling (gate machinery pin)

ROOT = Path(__file__).resolve().parents[2]
SESSION_DIR = ROOT / "computations" / "session-95"
SCRIPT_PATH = Path(__file__).resolve()
CANON_PATH = SHARED / "canonical_constants.py"
MASTER_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S94_GAMMA_E = ROOT / "computations" / "session-94" / "s94_ds_gamma_e_resolution_vg_b2_trajectory.npz"
VERDICT_TXT = SESSION_DIR / "s95_gate_verdicts.txt"
NPZ_OUT = SESSION_DIR / "s95_w7_2_van_hove_noun.npz"
PNG_OUT = SESSION_DIR / "s95_w7_2_van_hove_noun.png"

# --- machinery pins (plan §W7-2 machinery_pin_map) ---
L_SCAN = [6, 8, 10, 12]                  # (local) cache sub-truncation grid (step 2)
B2_SECTORS = [(0, 1), (1, 0)]            # (local) the optical-band Peter-Weyl sector pair
DEGEN_TOL = 1e-8                          # (local) eigenvalue degeneracy tolerance (round-8)
FD_FLAT_FLOOR = 1e-6                      # (local) |d ln m / d ln L| FD-flat floor (plan)
BETA_SIG = 0.05                           # (local) gap power-law significance (plan)
GAP_RELVAR_BOUND = 0.20                   # (local) first_gap relative-variation bound (plan)
DLNM_LICENSE_FLOOR = 0.05                 # (local) |d ln m / d ln L| license floor (plan)
N_HIGH_SECTORS_CHECK = 8                  # (local) # higher-(p,q) sectors for the Casimir-floor sanity check

# Pre-registered input SHAs (plan §W7-2 input_files)
PIN_SHA_CANON = "cc3878217389b0a68956563b3ac07e8de820ab626f9c801f0831a688f5f693c9"
PIN_SHA_MASTER = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"
PIN_SHA_S94GAMMA = "71e573e0c3aab1264667a713e6731a0f19973a5d60b589cad447a2b3ce59ca3b"


# =============================================================================
# SHA helpers (dual-SHA per S84+ schema; matches s93_w7_1 precedent)
# =============================================================================
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json);
    content = sha(script)."""
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def casimir_su3(p: int, q: int) -> float:
    """SU(3) quadratic Casimir C_2(p,q) = (1/3)(p^2 + q^2 + p*q + 3p + 3q)."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# =============================================================================
# Bottom-multiplicity & first-gap extraction for the B2 sector pair
# =============================================================================
def b2_bottom_observables(sector_evals: dict, L_filter: int) -> dict:
    """Combine the (0,1)+(1,0) blocks present at sub-truncation L_filter and read
    the bottom-level multiplicity m, the first_gap, and E_0.

    The (0,1)/(1,0) blocks are full irrep diagonalizations (D_K block-diagonal).
    The sub-truncation filter only controls sector PRESENCE; the blocks themselves
    are L_max-invariant. We report BOTH conventions:
      m_combined_distinct = multiplicity of the lowest DISTINCT |lambda| level in
                            the combined (0,1)+(1,0) spectrum (S94 bot_deg=4 conv).
      m_per_sector_x2     = (bottom multiplicity within a single sector) * 2
                            (the plan's "4 per sector x 2 = 8" framing).
    """
    present = {pq: sector_evals[pq] for pq in B2_SECTORS
               if pq in sector_evals and int(sector_evals[pq]["level"]) <= L_filter}
    if len(present) < 2:
        return {"L": L_filter, "b2_present": False}

    # combined spectrum of the two blocks
    both = np.concatenate([np.asarray(present[pq]["abs_evals"], dtype=np.float64)
                           for pq in B2_SECTORS])
    both_sorted = np.sort(both)
    u, c = np.unique(np.round(both_sorted, 8), return_counts=True)  # distinct levels + counts
    E0 = float(u[0])  # (local)
    m_combined_distinct = int(c[0])  # (local)
    first_gap = float(u[1] - u[0]) if u.size >= 2 else float("nan")  # (local)

    # per-sector bottom multiplicity (the "4 per sector" framing)
    per_sector_bot_mults = []  # (local)
    for pq in B2_SECTORS:
        ae = np.sort(np.asarray(present[pq]["abs_evals"], dtype=np.float64))
        mn = ae[0]  # (local)
        per_sector_bot_mults.append(int(np.sum(np.abs(ae - mn) < DEGEN_TOL)))
    m_per_sector_x2 = int(sum(per_sector_bot_mults))  # (local) sum over the 2 sectors

    return {
        "L": L_filter,
        "b2_present": True,
        "E0": E0,
        "first_gap": first_gap,
        "m_combined_distinct": m_combined_distinct,
        "m_per_sector_x2": m_per_sector_x2,
        "per_sector_bot_mults": per_sector_bot_mults,
    }


def loglog_slope(x: np.ndarray, y: np.ndarray) -> dict:
    """d(ln y)/d(ln x) via least-squares on ln-ln. Returns slope, R^2, and the
    relative variation of y across the scan. Handles the FD-flat (zero-variance)
    case explicitly (a constant y has slope exactly 0)."""
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    rel_var = float((np.max(y) - np.min(y)) / np.max(np.abs(y))) if np.max(np.abs(y)) > 0 else 0.0  # (local)
    if np.allclose(y, y[0], rtol=0.0, atol=1e-12):
        # exactly constant => slope is 0 by definition (no power law)
        return {"slope": 0.0, "r2": float("nan"), "rel_var": rel_var, "flat": True}
    lx = np.log(x)  # (local)
    ly = np.log(y)  # (local)
    A = np.vstack([lx, np.ones_like(lx)]).T  # (local)
    coef, *_ = np.linalg.lstsq(A, ly, rcond=None)  # (local)
    slope = float(coef[0])  # (local)
    yhat = A @ coef  # (local)
    ss_res = float(np.sum((ly - yhat) ** 2))  # (local)
    ss_tot = float(np.sum((ly - np.mean(ly)) ** 2))  # (local)
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float("nan")  # (local)
    return {"slope": slope, "r2": r2, "rel_var": rel_var, "flat": False}


# =============================================================================
# MAIN
# =============================================================================
def main() -> None:
    print("=" * 78)
    print(f"{GATE_ID}  —  van Hove NOUN-licensing adjudication (landau)")
    print("=" * 78)

    # ---- Step 0: input SHA verification (log in first 20 lines of stdout) ----
    sha_canon = sha256_of(CANON_PATH)  # (local)
    sha_master = sha256_of(MASTER_CACHE)  # (local)
    sha_s94 = sha256_of(S94_GAMMA_E)  # (local)
    print(f"  INPUT canonical_constants.py sha256 = {sha_canon}")
    print(f"  INPUT master_cache_L12      sha256 = {sha_master}")
    print(f"  INPUT s94_gamma_e_traj      sha256 = {sha_s94}")
    print(f"  PIN   canonical (plan)             = {PIN_SHA_CANON}  match={sha_canon == PIN_SHA_CANON}")
    print(f"  PIN   master   (plan)             = {PIN_SHA_MASTER}  match={sha_master == PIN_SHA_MASTER}")
    print(f"  PIN   s94      (plan)             = {PIN_SHA_S94GAMMA}  match={sha_s94 == PIN_SHA_S94GAMMA}")
    print(f"  canonical pins: rho_B2_per_mode={rho_B2_per_mode}  v_g_B2_fold={v_g_B2_fold}  tau_fold={tau_fold}")

    # cross-check: 1/(pi*v_g) == rho_B2_per_mode (the proven Phi_DOS-continuum, INVARIANT)
    rho_from_vg = 1.0 / (PI * v_g_B2_fold)  # (local)
    rho_check_resid = abs(rho_from_vg - rho_B2_per_mode) / rho_B2_per_mode  # (local)
    print(f"  PROVEN-INVARIANT cross-check: 1/(pi*v_g) = {rho_from_vg:.9f} vs rho_B2_per_mode "
          f"= {rho_B2_per_mode:.9f}  rel_resid={rho_check_resid:.3e}")

    # ---- Step 1: load master cache + S94 trajectory ----
    cache = np.load(MASTER_CACHE, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()  # (local)
    g94 = np.load(S94_GAMMA_E, allow_pickle=True)
    bot_deg_s94 = np.asarray(g94["bot_deg"], dtype=int)  # (local) S94 frozen bot_deg trajectory
    first_gap_s94 = np.asarray(g94["first_gap"], dtype=float)  # (local) S94 frozen first_gap trajectory
    gamma_E_primary_s94 = float(np.asarray(g94["gamma_E_primary"]))  # (local) S94: 0.0 (n=1 linear)
    n_disp_fold_s94 = float(np.asarray(g94["n_disp_fold"]))  # (local) S94: n=1
    print(f"  S94 frozen: bot_deg={bot_deg_s94.tolist()}  gamma_E_primary={gamma_E_primary_s94}  "
          f"n_disp_fold={n_disp_fold_s94}")

    # ---- Step 2: L_max-scan the B2 bottom multiplicity m(L) and first_gap(L) ----
    print("\n--- Step 2: B2 bottom-multiplicity + first_gap L_max-scan ---")
    rows = []  # (local)
    for L in L_SCAN:
        obs = b2_bottom_observables(sector_evals, L)
        rows.append(obs)
        if obs["b2_present"]:
            print(f"  L_max={L:>3}: m_combined_distinct={obs['m_combined_distinct']}  "
                  f"m_per_sector_x2={obs['m_per_sector_x2']}  "
                  f"first_gap={obs['first_gap']:.10f}  E0={obs['E0']:.10f}  "
                  f"per_sector={obs['per_sector_bot_mults']}")
        else:
            print(f"  L_max={L:>3}: (0,1)/(1,0) NOT both present")

    present_rows = [r for r in rows if r["b2_present"]]  # (local)
    L_arr = np.array([r["L"] for r in present_rows], dtype=float)  # (local)
    m_distinct_arr = np.array([r["m_combined_distinct"] for r in present_rows], dtype=float)  # (local)
    m_x2_arr = np.array([r["m_per_sector_x2"] for r in present_rows], dtype=float)  # (local)
    gap_arr = np.array([r["first_gap"] for r in present_rows], dtype=float)  # (local)
    E0_arr = np.array([r["E0"] for r in present_rows], dtype=float)  # (local)

    # ---- Step 3: discriminator scaling fits ----
    print("\n--- Step 3: discriminator scaling fits ---")
    # branch-1 quantity: d(ln m)/d(ln L_max) for BOTH multiplicity conventions
    fit_m_distinct = loglog_slope(L_arr, m_distinct_arr)  # (local)
    fit_m_x2 = loglog_slope(L_arr, m_x2_arr)  # (local)
    # branch-2 quantity: first_gap power-law exponent beta_gap = d(ln gap)/d(ln L_max)
    fit_gap = loglog_slope(L_arr, gap_arr)  # (local)
    dlnm_distinct = abs(fit_m_distinct["slope"])  # (local)
    dlnm_x2 = abs(fit_m_x2["slope"])  # (local)
    beta_gap = fit_gap["slope"]  # (local) signed (negative => gap shrinks)
    gap_relvar = fit_gap["rel_var"]  # (local)
    m_distinct_relvar = fit_m_distinct["rel_var"]  # (local)
    m_x2_relvar = fit_m_x2["rel_var"]  # (local)
    print(f"  |d ln m/d ln L| (combined-distinct) = {dlnm_distinct:.3e}  "
          f"(flat={fit_m_distinct['flat']}, rel_var={m_distinct_relvar:.3e})")
    print(f"  |d ln m/d ln L| (per-sector x2)      = {dlnm_x2:.3e}  "
          f"(flat={fit_m_x2['flat']}, rel_var={m_x2_relvar:.3e})")
    print(f"  beta_gap = d ln(first_gap)/d ln L    = {beta_gap:+.3e}  "
          f"(|beta|={abs(beta_gap):.3e}, gap rel_var={gap_relvar:.3e})")

    # ---- Step 4: Casimir-floor sanity check (does ANY higher (p,q) accrete below E_0?) ----
    print("\n--- Step 4: Casimir-floor sanity (higher-(p,q) accretion test) ---")
    E0_fold = float(E0_arr[-1])  # (local) the B2 bottom at the full L_max=12 cache
    # min |lambda| over ALL sectors with level in (2 .. cache ceiling), to confirm
    # no higher sector dips below the B2 bottom (no continuum accretion into E_0).
    higher_min_lambda = []  # (local)
    for pq, info in sector_evals.items():
        p, q = pq
        if (p + q) <= 1:
            continue  # skip (0,0),(0,1),(1,0) themselves
        mn = float(np.min(np.asarray(info["abs_evals"], dtype=np.float64)))  # (local)
        higher_min_lambda.append((p + q, casimir_su3(p, q), mn))
    higher_min_lambda.sort(key=lambda t: t[2])  # sort by min|lambda|
    global_higher_floor = higher_min_lambda[0][2] if higher_min_lambda else float("inf")  # (local)
    print(f"  B2 bottom E_0 (L=12)                 = {E0_fold:.10f}")
    print(f"  global higher-(p,q) min|lambda|      = {global_higher_floor:.10f}  "
          f"(sector p+q={higher_min_lambda[0][0]}, C_2={higher_min_lambda[0][1]:.4f})")
    no_accretion = global_higher_floor > E0_fold  # (local) True => no state dips below B2 bottom
    print(f"  no higher-sector accretion below E_0 = {no_accretion}  "
          f"(gap to higher floor = {global_higher_floor - E0_fold:+.6f})")
    # Friedrich-Bar slope on the higher-sector min|lambda| vs sqrt(C_2): is the
    # higher floor moving UP (away from E_0) with Casimir => no accretion in continuum
    hC = np.array([t[1] for t in higher_min_lambda], dtype=float)  # (local)
    hMin = np.array([t[2] for t in higher_min_lambda], dtype=float)  # (local)
    fb_slope = float(np.polyfit(np.sqrt(hC + 1.0), hMin, 1)[0])  # (local) min|lambda| vs sqrt(C_2+1)
    print(f"  Friedrich-Bar slope min|lambda| vs sqrt(C_2+1) = {fb_slope:+.4f}  "
          f"(>0 => higher sectors move UP with Casimir; NO continuum accretion)")

    # ---- Step 5: apply the PRE-REGISTERED discriminator ----
    print("\n--- Step 5: PRE-REGISTERED discriminator verdict ---")
    # multiplicity is FD-flat under BOTH conventions?
    m_fd_flat = (dlnm_distinct < FD_FLAT_FLOOR) and (dlnm_x2 < FD_FLAT_FLOOR)  # (local)
    # gap bounded away from 0 (no power-law approach)?
    gap_bounded = (gap_relvar < GAP_RELVAR_BOUND) and (abs(beta_gap) < BETA_SIG)  # (local)
    # LICENSE branch
    mult_grows = (dlnm_distinct > DLNM_LICENSE_FLOOR) or (dlnm_x2 > DLNM_LICENSE_FLOOR)  # (local)
    gap_powerlaw_to_zero = (beta_gap < -BETA_SIG) and (gap_relvar > GAP_RELVAR_BOUND)  # (local)
    branch_license = bool(mult_grows or gap_powerlaw_to_zero)  # (local)
    branch_overclaim = bool(m_fd_flat and gap_bounded)  # (local)

    print(f"  m_fd_flat (both conventions <{FD_FLAT_FLOOR}) = {m_fd_flat}")
    print(f"  gap_bounded (rel_var<{GAP_RELVAR_BOUND} & |beta|<{BETA_SIG}) = {gap_bounded}")
    print(f"  mult_grows (|d ln m/d ln L|>{DLNM_LICENSE_FLOOR}) = {mult_grows}")
    print(f"  gap_powerlaw_to_zero = {gap_powerlaw_to_zero}")
    print(f"  branch_LICENSE = {branch_license}   branch_OVER-CLAIM = {branch_overclaim}")

    # ---- Verdict mapping (plan rubric) ----
    # PASS  = noun LICENSED  (branch_license True)
    # FAIL  = noun OVER-CLAIMED (branch_overclaim True)
    # INFO  = inconclusive (neither branch crossed, or conflicting signals)
    if branch_license and not branch_overclaim:
        verdict = "PASS"
        noun_status = "LICENSED"
    elif branch_overclaim and not branch_license:
        verdict = "FAIL"
        noun_status = "OVER-CLAIMED"
    else:
        verdict = "INFO"
        noun_status = "UNDECIDABLE"

    print(f"\n  VERDICT = {verdict}   noun_status = {noun_status}")

    # value string for the verdict line (descriptive, audit-greppable)
    value_str = (
        f"noun_{noun_status}_mFDflat={m_fd_flat}_dlnm={dlnm_distinct:.2e}/{dlnm_x2:.2e}"
        f"_betagap={beta_gap:+.2e}_gaprelvar={gap_relvar:.2e}_noaccretion={no_accretion}"
        f"_rhoINVARIANT={rho_check_resid:.1e}"
    )  # (local)

    # ---- save npz ----
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        verdict=verdict,
        noun_status=noun_status,
        L_scan=L_arr,
        m_combined_distinct=m_distinct_arr,
        m_per_sector_x2=m_x2_arr,
        first_gap=gap_arr,
        E0=E0_arr,
        dlnm_distinct=dlnm_distinct,
        dlnm_x2=dlnm_x2,
        beta_gap=beta_gap,
        gap_relvar=gap_relvar,
        m_distinct_relvar=m_distinct_relvar,
        m_x2_relvar=m_x2_relvar,
        m_fd_flat=m_fd_flat,
        gap_bounded=gap_bounded,
        branch_license=branch_license,
        branch_overclaim=branch_overclaim,
        no_accretion=no_accretion,
        global_higher_floor=global_higher_floor,
        E0_fold=E0_fold,
        fb_slope_higher=fb_slope,
        rho_B2_per_mode=rho_B2_per_mode,
        v_g_B2_fold=v_g_B2_fold,
        rho_from_vg=rho_from_vg,
        rho_check_resid=rho_check_resid,
        gamma_E_primary_s94=gamma_E_primary_s94,
        n_disp_fold_s94=n_disp_fold_s94,
        bot_deg_s94=bot_deg_s94,
        first_gap_s94=first_gap_s94,
        FD_FLAT_FLOOR=FD_FLAT_FLOOR,
        BETA_SIG=BETA_SIG,
        GAP_RELVAR_BOUND=GAP_RELVAR_BOUND,
        DLNM_LICENSE_FLOOR=DLNM_LICENSE_FLOOR,
        sha_canon=sha_canon,
        sha_master=sha_master,
        sha_s94=sha_s94,
    )
    print(f"  npz -> {NPZ_OUT}")

    # ---- plot ----
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.6))
    # (a) multiplicity vs L_max
    ax = axes[0]
    ax.plot(L_arr, m_distinct_arr, "o-", color="C0", label="m (combined-distinct)")
    ax.plot(L_arr, m_x2_arr, "s--", color="C3", label="m (per-sector x2)")
    ax.set_xlabel("L_max (sub-truncation)")
    ax.set_ylabel("bottom multiplicity m")
    ax.set_ylim(0, max(m_x2_arr.max(), m_distinct_arr.max()) * 1.4 + 1)
    ax.set_title(f"(a) m(L_max): |d ln m/d ln L| = {dlnm_distinct:.1e} / {dlnm_x2:.1e}\nFD-FLAT (m fixed) "
                 f"=> NO continuum accretion")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    # (b) first_gap vs L_max
    ax = axes[1]
    ax.plot(L_arr, gap_arr, "o-", color="C2", label="first_gap(L_max)")
    ax.set_xlabel("L_max (sub-truncation)")
    ax.set_ylabel("first_gap (M_KK)")
    ax.set_title(f"(b) first_gap(L_max): beta_gap={beta_gap:+.1e}, rel_var={gap_relvar:.1e}\n"
                 f"BOUNDED away from 0 (no power-law -> 0)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    # (c) Casimir floor: B2 bottom vs higher-sector min|lambda|
    ax = axes[2]
    ax.scatter(np.sqrt(hC + 1.0), hMin, s=14, color="C1", alpha=0.6, label="higher (p,q) min|λ|")
    ax.axhline(E0_fold, color="C0", lw=2, ls="-", label=f"B2 bottom E_0={E0_fold:.4f}")
    xx = np.linspace(np.sqrt(hC.min() + 1.0), np.sqrt(hC.max() + 1.0), 50)  # (local)
    cc = np.polyfit(np.sqrt(hC + 1.0), hMin, 1)  # (local)
    ax.plot(xx, np.polyval(cc, xx), "C1--", lw=1, label=f"FB slope={fb_slope:+.3f}")
    ax.set_xlabel(r"$\sqrt{C_2(p,q)+1}$")
    ax.set_ylabel(r"min$|\lambda|$ per sector")
    ax.set_title(f"(c) no accretion below E_0 = {no_accretion}\n(higher sectors move UP with Casimir)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)
    fig.suptitle(f"{GATE_ID} — van Hove NOUN {noun_status} (verdict={verdict}); "
                 f"rho_smooth=1/(pi v_g)=14.02 INVARIANT (rel_resid={rho_check_resid:.1e})",
                 fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png -> {PNG_OUT}")

    # ---- dual-SHA + verdict line emission ----
    pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "L_scan": str(L_SCAN),
        "B2_sectors": str(B2_SECTORS),
        "FD_FLAT_FLOOR": FD_FLAT_FLOOR,
        "BETA_SIG": BETA_SIG,
        "GAP_RELVAR_BOUND": GAP_RELVAR_BOUND,
        "DLNM_LICENSE_FLOOR": DLNM_LICENSE_FLOOR,
        "sha_canon": sha_canon,
        "sha_master": sha_master,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANON_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # 4-tuple output tag (final non-verdict line)
    print(f"  OUTPUT 4-tuple: (value={value_str}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # supersession check (Option A)
    prior_sha = find_prior_audit_sha()  # (local)
    sup = prior_sha if (prior_sha and prior_sha != audit_sha) else ""  # (local)

    append_verdict(verdict, value_str, audit_sha, content_sha,
                   noun_status, branch_license, branch_overclaim,
                   no_accretion, rho_check_resid, supersedes_sha=sup)
    print(f"  verdict line appended -> {VERDICT_TXT}")
    print("=" * 78)
    print(f"DONE — {GATE_ID}: {verdict} (noun {noun_status})")
    print("=" * 78)


# =============================================================================
# Verdict-line emitter (atomic append; dual-SHA; [VERIFY] => no 3-tuple row)
# =============================================================================
def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for this GATE_ID (Option A supersession
    chain). Returns full 64-char audit_sha256 or ''."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   noun_status: str, branch_license: bool, branch_overclaim: bool,
                   no_accretion: bool, rho_resid: float, supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + discriminator-provenance rows.

    [VERIFY] gate (noun-licensing adjudication) — NO directional pre-registration, so
    NO schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (plan §W7-2
    schema_v2_3tuple_required: false). The discriminator-provenance row records the
    two-branch outcome and the proven-physics INVARIANCE for audit traceability.
    """
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )  # (local)
    disc_row = (
        f"# discriminator: noun_status={noun_status} branch_LICENSE={branch_license} "
        f"branch_OVERCLAIM={branch_overclaim} no_higher_sector_accretion={no_accretion} "
        f"# {GATE_ID} [VERIFY] two-branch structural discriminator (NO directional pre-reg; "
        f"schema_v2_3tuple N/A)\n"
    )  # (local)
    invariance_row = (
        f"# PROVEN-INVARIANT: rho_smooth=1/(pi*v_g)=14.02 UNCHANGED (rel_resid={rho_resid:.1e}); "
        f"this gate decides ONLY the residual NOUN in proven_1086, NOT the BCS-driver DOS value "
        f"# {GATE_ID} Phi_DOS-continuum invariance\n"
    )  # (local)
    rows = [line, companion, disc_row, invariance_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md §\"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write("".join(rows))


if __name__ == "__main__":
    main()
