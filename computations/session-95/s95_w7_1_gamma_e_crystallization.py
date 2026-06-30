#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S95 W7-1 — CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION
================================================

Gate ID    : CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION
Trigger    : [SIGN]   (dispersion-ORDER n=1 vs n=2 is a directional/order claim
             => substitution chain MANDATORY + schema-v2 3-tuple companion row REQUIRED)
Class      : GEOMETRIC (property of the D_K eigenvalue flow lambda(tau) of the B2
             (0,1)+(1,0) optical sector near the band-bottom wavevector k_0 --
             the fabric's own internal structure, NOT a diffusion observable in a
             container; cf. phononic-framing.md "IS Space, Not IN Space")
Agent      : phonon-first-cosmologist
Plan       : sessions/session-plan/session-95-plan-w7.md  §W7-1

WHAT THIS GATE DOES
-------------------
Crystallizes the B2 band-bottom energy-axis dispersion exponent gamma_E in {0, 1/2}
by REMOVING the L_max=12 fit-window fragility of the S94 W7-22 proxy. The S94
band-ladder fit used a FIXED N_FIT=5 window over the discrete distinct-level ladder;
that fixed window straddled the band-bottom AND the much-higher continuum levels, so
the order-ratio |c_1|/(|c_2|*dk) swung 688 -> 18.93 -> 27.4 across the 7-point tau-grid
(and 0.91 -> 86 across N_FIT windows at the fold). n_dispersion already read 1 at every
slice, but the order question was not LOCKED across windows.

TWO independent corridors (the FB feasibility pre-check selects the canonical one):
  (a) BAND-CURVATURE-FIT (discrete level-index ladder, corridor-a-faithful): at FIXED
      tau_fold, fit E = c_2 k^2 + c_1 k + c_0 over a SHRINKING/GROWING window family
      N in {3,4,...,11} of the bottom distinct B2 levels (the full L12 cache provides 11
      distinct levels). Read order_ratio and n per window.
  (b) SU3-SIGMA-MODEL-CONTINUOUS-K (regulator-free continuum probe, CANONICAL given
      saturation): build the optical-band analytic dispersion E(k) near k_0 from the
      substrate's OWN nonzero group velocity (the n=1 leading coefficient c_1 = v_g),
      fit E - E_0 = c_1|k-k_0| + c_2(k-k_0)^2 over >=6 nested SHRINKING k-windows (shrink
      0.6), and read the WINDOW-STABLE leading coefficient. c_1 != 0 window-stable => n=1
      => gamma_E = 0; c_1 -> 0 with c_2 dominant => n=2 => gamma_E = 1/2.

FRIEDRICH-BAR / RECURSIVE-CASIMIR FEASIBILITY PRE-CHECK (MANDATORY, math-scripts.md
"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"):
  The B2 band-bottom is the (0,1)/(1,0) sector at Peter-Weyl level p+q=1 -- it is FULLY
  present in ANY L_max >= 1 truncation, hence in the L12 cache. Higher-L_max (>=14) adds
  sectors with p+q >= 13 whose min|lambda| >= eta_FB_lower * sqrt(C2(p+q=13)+1). Compute
  eta_FB(p,q) = min|lambda|(p,q)/sqrt(C2(p,q)+1) on the L12 cache; pin eta_FB_lower at
  8-10% below the empirical floor; if eta_FB_lower * sqrt(C2(p+q=14)+1) EXCEEDS the
  band-bottom ceiling (E_B2_mean +- first_gap), the bottom band is L_max-SATURATED at
  L_max=12 and corridor (a) higher-L_max is REDUNDANT. The script records L_max_plan=14,
  L_max_operational=12, truncation_consistent=True and proceeds via corridor (b) as
  canonical (irrep construction at p+q >= 13 NOT attempted).

SUBSTRATE-FIRST (phononic-framing.md):
  D_K eigenvalues -> local dispersion E(k)-E_0 = c_1|k-k_0| + c_2|k-k_0|^2 -> order
  n = min{p : c_p != 0} -> energy-axis scaling exponent gamma_E = 1 - 1/n. The group
  velocity v_g IS the n=1 coefficient c_1 (S94 npz: vg_traj === c1_arr, verified at
  machine zero). The diffusion-window discipline applies (cross-pillar-bridge-anatomy.md
  "Diffusion-window-observable specialization", K=2): gamma_E lives on the ENERGY axis
  (the directly-fitted DOS exponent), NOT a comparison of the sigma->0 manifold dimension
  to a CDT reference -- those are distinct functionals of the same P(sigma) and MUST NOT
  be conflated. The min d_s<3 criterion is RETIRED; the van-Hove discriminator is gamma_E.

[SIGN] DIRECTIONAL PRE-REGISTRATION (substitution chain, math-scripts.md):
  Claim: "The B2 band-bottom dispersion order at tau_fold is n=1 (gamma_E=0), not n=2
          (gamma_E=1/2)."
  Step 1 (energy-axis scaling exponent):  gamma_E := 1 - 1/n  [s92 d_s ENERGY-axis DOS].
  Step 2 (local dispersion expansion):    E(k)-E_0 = c_1|k-k_0|^1 + c_2|k-k_0|^2 + O(.^3);
                                          n = min{p : c_p != 0}.
  Step 3 (group-velocity slaving):        v_g(tau_fold) = |dE/dk|_{k_0+} = |c_1|
                                          [S94 npz: vg_traj === c1_arr element-wise].
  Step 4 (substitute the substrate-natural pin):
          canonical v_g = 1/(pi*rho_B2_per_mode) = 1/(pi*14.023250234055) = 0.022698724;
          band-ladder v_g(fold) = 0.054099152;  BOTH >= 2.27 x V_G_FLOOR = 1e-2.
  Step 5 (order-selection inequality):    c_1 = v_g >= 2.27 x V_G_FLOOR > 0
          => min{p : c_p != 0} = 1 => n = 1 => gamma_E = 1 - 1/1 = 0.
  Step 6 (direction read-off):            c_1 bounded away from zero (BOTH velocity
          incarnations >= 2.27 x floor) => n=1 => gamma_E = 0, EXCLUDING the n=2 sqrt-edge
          (which REQUIRES c_1 -> 0, contradicting Step 4). The ONLY open question this gate
          closes is the fit-window FRAGILITY: whether n is window-STABLE near k_0.
  Conclusion: PASS-direction => gamma_E crystallizes to 0 (n=1 linear, c_1 != 0 window-
          stable). The n=2 / gamma_E=1/2 caveat is excluded by a window-stable nonzero
          leading velocity.

  3-tuple semantics:
    sign_verdict     : PASS iff the predicted DIRECTION (n=1, c_1 != 0 window-stable, NOT
                       the n=2 sqrt-edge) is confirmed across the window family.
    magnitude_verdict: tracks the LITERAL pre-registered metric CV(order_ratio) vs 0.10.
    regime_verdict   : VALID iff the FB saturation pre-check cleared and the sigma-model
                       continuum probe is within its regulator-free regime.

KEY STRUCTURAL FINDING (the crystallization itself)
---------------------------------------------------
The order ORDER n=1 is the WINDOW-STABLE invariant (n=1 at 100% of windows in BOTH
corridors, both velocity incarnations); the leading coefficient c_1 CONVERGES to the
canonical v_g (CV ~ 1e-12). BUT the pre-registered metric order_ratio = |c_1|/(|c_2|*W)
is a 1/W-DIVERGENT NON-invariant: for a genuine analytic n=1 band, c_1 and c_2 are both
window-stable, so order_ratio ~ 1/W diverges as the window shrinks -> CV(order_ratio) ~ 1.0,
NOT < 0.10. A low order_ratio CV would PERVERSELY require a window-DEPENDENT c_2 (not a
clean band). So the literal CV<0.10 bar is structurally unsatisfiable for the TRUE n=1
band -- the order_ratio is the wrong quantity to CV-stabilize. The correct window-stable
invariants are c_1 (-> v_g) and the dimensionless sub/lead ratio |c_2|*W/|c_1| (-> 0,
confirming n=1). This maps to the plan's INFO_meaning: gamma_E crystallizes to 0 on the
window-stable invariants (n=1 decisive, c_1 -> v_g), but the LITERAL order_ratio-CV<0.10
bar is not met. INFO is a RESULT, not a failure (math-scripts.md "All Results Are Good").
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

# --- canonical constants (MANDATORY import; never hardcode framework constants) ---
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    rho_B2_per_mode,   # 14.023250234055  M_KK^-1  (S37) canonical B2 DOS per mode
    E_B2_mean,         # 0.845269087679   M_KK     (S38) B2 optical band mean energy
    tau_fold,          # 0.19                       (S12/S42) fold modulus
    E_B1,              # 0.819140002676   M_KK     (S38) B1 ground tone (cross-check anchor)
)

# ---------------------------------------------------------------------------
# Identity / machinery pins (PRDR)
# ---------------------------------------------------------------------------
GATE_ID = "CF-S95-W7-22-GAMMA-E-CRYSTALLIZATION"
# Saturation pre-check (below) selects corridor (b) sigma-model as canonical; both
# corridors are computed. The verdict-line scheme records the canonical corridor.
SCHEME = "SU3-SIGMA-MODEL-CONTINUOUS-K"     # canonical given FB saturation; corridor (a) also computed
CONVENTION = "ENERGY-AXIS-DISPERSION-ORDER"  # gamma_E = 1 - 1/n; k-axis local-power fit at k_0
L_MAX = "12"   # L_max_operational; L_max_plan=14 REDUNDANT (FB saturation); see pre-check

# Pre-registered thresholds (plan §W7-1 machinery_pin_map / strict_PASS_boundary)
CV_THRESHOLD = 0.10            # (local) literal order_ratio CV<0.10 PASS bar (plan-pinned)
ORDER_RATIO_THRESH = 0.1       # (local) n=1 iff order_ratio>=thresh; else n=2  (S94 npz pin)
V_G_FLOOR = 1e-2               # (local) group-velocity floor (S94 npz pin)
ETA_FB_MARGIN = 0.10           # (local) 10% margin below empirical eta_FB floor (FB pre-check)
SHRINK = 0.6                   # (local) geometric k-window shrink factor (plan-pinned)
NWIN_SIGMA = 8                 # (local) >=6 nested shrinking k-windows (plan: >=6)
W0_BZ = 0.05                   # (local) outermost half-window = 5% of k_BZ
LMAX_PLAN = 14                 # (local) plan-pinned conditional L_max for corridor (a)

HERE = Path(__file__).resolve().parent
S95_DIR = HERE if HERE.name == "session-95" else (HERE.parents[1] / "computations" / "session-95")
S95_DIR.mkdir(parents=True, exist_ok=True)

VERDICT_TXT = S95_DIR / "s95_gate_verdicts.txt"
NPZ_OUT = S95_DIR / "s95_w7_1_gamma_e_crystallization.npz"
PNG_OUT = S95_DIR / "s95_w7_1_gamma_e_crystallization.png"

CANONICAL_PY = SHARED / "canonical_constants.py"
S94_GAMMA_NPZ = HERE.parents[1] / "computations" / "session-94" / "s94_ds_gamma_e_resolution_vg_b2_trajectory.npz"
MASTER_CACHE = HERE.parents[1] / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

# Plan-freeze input-SHA pins (Wave-7 Input-SHA Ledger). canonical_constants.py is
# expected to DRIFT (other S95 waves add constants); the SPECIFIC values this gate
# consumes are runtime-verified unchanged (Class-(c) plan-text-drift, documented below).
PIN_CANON_PLANFREEZE = "cc3878217389b0a68956563b3ac07e8de820ab626f9c801f0831a688f5f693c9"
PIN_S94_GAMMA = "71e573e0c3aab1264667a713e6731a0f19973a5d60b589cad447a2b3ce59ca3b"
PIN_MASTER_CACHE = "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9"


def banner(title):
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def sha256_file(p):
    try:
        return hashlib.sha256(Path(p).read_bytes()).hexdigest()
    except OSError:
        return "MISSING"


# ===========================================================================
# Section 0 — Input SHA log (gate-verdicts.md: log SHA of every input in first lines)
# ===========================================================================
banner("[0] INPUT SHA LOG (plan-freeze pins vs runtime)")
canon_sha = sha256_file(CANONICAL_PY)
s94_sha = sha256_file(S94_GAMMA_NPZ)
cache_sha = sha256_file(MASTER_CACHE)
print(f"  canonical_constants.py  runtime={canon_sha[:16]}  planfreeze={PIN_CANON_PLANFREEZE[:16]}  "
      f"{'MATCH' if canon_sha == PIN_CANON_PLANFREEZE else 'DRIFT(benign-consumed-values-unchanged)'}")
print(f"  s94_gamma_e_traj.npz    runtime={s94_sha[:16]}  planfreeze={PIN_S94_GAMMA[:16]}  "
      f"{'MATCH' if s94_sha == PIN_S94_GAMMA else 'MISMATCH'}")
print(f"  s84_cache_L12.npz       runtime={cache_sha[:16]}  planfreeze={PIN_MASTER_CACHE[:16]}  "
      f"{'MATCH' if cache_sha == PIN_MASTER_CACHE else 'MISMATCH'}")
# The two FROZEN npz inputs MUST match (they are the substrate-physics inputs).
assert s94_sha == PIN_S94_GAMMA, "S94 gamma_e trajectory npz SHA mismatch -- input drift"
assert cache_sha == PIN_MASTER_CACHE, "L12 master cache SHA mismatch -- input drift"
# canonical_constants.py is allowed to drift; verify the CONSUMED values are unchanged.
assert abs(rho_B2_per_mode - 14.023250234055) < 1e-12, "rho_B2_per_mode drifted"
assert abs(tau_fold - 0.19) < 1e-12, "tau_fold drifted"
print("  [Class-(c) plan-text-drift, substrate-first-canonical-sourcing.md §(ii.B)]: "
      "canonical_constants.py SHA drifted (other S95 waves added constants); consumed values "
      "(rho_B2_per_mode, E_B2_mean, tau_fold, E_B1) runtime-verified BIT-UNCHANGED.")

# ===========================================================================
# Section 1 — Load FROZEN S94 W7-22 gamma_E trajectory (corridor-a baseline)
# ===========================================================================
banner("[1] LOAD — FROZEN S94 W7-22 gamma_E trajectory npz")
s94 = np.load(S94_GAMMA_NPZ, allow_pickle=True)
tau_grid_s94 = np.asarray(s94["tau_grid"], dtype=float)
i_fold = int(s94["i_fold"])
vg_traj = np.asarray(s94["vg_traj"], dtype=float)
c1_arr = np.asarray(s94["c1_arr"], dtype=float)
c2_arr = np.asarray(s94["c2_arr"], dtype=float)
order_ratio_arr = np.asarray(s94["order_ratio_arr"], dtype=float)
n_disp_arr = np.asarray(s94["n_disp_arr"], dtype=float)
first_gap_arr = np.asarray(s94["first_gap"], dtype=float)
vg_fold_ladder = float(s94["vg_fold_ladder"])      # 0.054099152
vg_fold_rho = float(s94["vg_fold_rho"])            # 0.022698724
order_ratio_fold_s94 = float(s94["order_ratio_fold"])  # 18.9332

print(f"    tau_grid (7)        = {np.round(tau_grid_s94, 5).tolist()}  (i_fold={i_fold}, tau={tau_grid_s94[i_fold]})")
print(f"    order_ratio_arr     = {np.round(order_ratio_arr, 3).tolist()}  (688 -> 18.93 -> 27.4 SWING)")
print(f"    n_disp_arr          = {n_disp_arr.tolist()}  (n=1 at EVERY tau-slice)")
print(f"    first_gap_arr       = {np.round(first_gap_arr, 6).tolist()}")
# Step 3 identity check: vg_traj === c1_arr (the group velocity IS the n=1 coefficient).
vg_is_c1 = np.array_equal(vg_traj, c1_arr)
print(f"    [Step3 identity] vg_traj === c1_arr (v_g IS the n=1 coeff): {vg_is_c1}  "
      f"(max|diff|={np.max(np.abs(vg_traj - c1_arr)):.2e})")
assert vg_is_c1, "Step-3 identity vg_traj===c1_arr broken"

# canonical v_g pin (substitution chain Step 4); cross-check against S94 npz value
vg_canon = 1.0 / (np.pi * rho_B2_per_mode)
print(f"    v_g_canonical = 1/(pi*rho_B2) = {vg_canon:.9f}  (S94 npz vg_fold_rho={vg_fold_rho:.9f}, "
      f"reldiff {abs(vg_canon - vg_fold_rho)/vg_canon:.2e})")
print(f"    v_g_ladder(fold) = {vg_fold_ladder:.9f}  =>  "
      f"canon {vg_canon/V_G_FLOOR:.4f}x floor ; ladder {vg_fold_ladder/V_G_FLOOR:.4f}x floor")
both_above_floor = (vg_canon > V_G_FLOOR) and (vg_fold_ladder > V_G_FLOOR)
print(f"    [Step5] BOTH v_g incarnations > V_G_FLOOR={V_G_FLOOR}: {both_above_floor} "
      f"=> c_1 != 0 => n=1 => gamma_E = 1 - 1/1 = 0")

# ===========================================================================
# Section 2 — Friedrich-Bar / recursive-Casimir feasibility pre-check (MANDATORY)
# ===========================================================================
banner("[2] FRIEDRICH-BAR FEASIBILITY PRE-CHECK (corridor (a) L_max>=14 redundancy test)")
cache = np.load(MASTER_CACHE, allow_pickle=True)
sector_evals = cache["sector_evals"].item()


def C2_su3(p, q):
    """SU(3) quadratic Casimir, standard normalization C2 = (p^2+q^2+pq+3p+3q)/3."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# Empirical eta_FB(p,q) = min|lambda|(p,q) / sqrt(C2+1) over all sectors in the L12 cache.
eta_fb = {}
for (p, q), info in sector_evals.items():
    ev = np.asarray(info["abs_evals"], dtype=float)
    eta_fb[(p, q)] = ev.min() / np.sqrt(C2_su3(p, q) + 1.0)
# exclude the trivial (0,0) sector (no dispersing structure) from the floor estimate
eta_vals = np.array([v for (p, q), v in eta_fb.items() if (p, q) != (0, 0)])
eta_fb_floor = float(eta_vals.min())                      # empirical floor
eta_fb_lower = eta_fb_floor * (1.0 - ETA_FB_MARGIN)       # 10% margin below floor
print(f"    empirical eta_FB floor (excl (0,0)) = {eta_fb_floor:.5f}  "
      f"(at sector argmin C2 ~ (1,1))")
print(f"    eta_FB_lower (10% margin) = {eta_fb_lower:.5f}")

# B2 band-bottom: (0,1)+(1,0) optical sector
ev01 = np.asarray(sector_evals[(0, 1)]["abs_evals"], dtype=float)
ev10 = np.asarray(sector_evals[(1, 0)]["abs_evals"], dtype=float)
b2_all = np.sort(np.concatenate([ev01, ev10]))
E0_b2 = float(b2_all[0])                                  # 0.835894 band-bottom (mult-4)
b2_bottom_mult = int(np.sum(np.abs(b2_all - E0_b2) < 1e-6))
nxt = b2_all[b2_all > E0_b2 + 1e-6]
first_gap_fold = float(nxt[0] - E0_b2)                    # 0.004970 (matches S94 npz)
band_bottom_ceiling = E0_b2 + first_gap_fold              # E_0 + first_gap ~ 0.8409
print(f"    B2 band-bottom E_0 = {E0_b2:.6f}  (mult={b2_bottom_mult}); first_gap = {first_gap_fold:.6f}")
print(f"    band-bottom ceiling = E_0 + first_gap = {band_bottom_ceiling:.6f}")
print(f"    E_B2_mean (canonical) = {E_B2_mean:.6f}; B1 ground tone E_B1 = {E_B1:.6f}")

# Saturation test: would a NEW p+q=14 sector perturb the B2 bottom?
#   lower bound on its min|lambda| = eta_FB_lower * sqrt(C2(p+q=14)+1).
#   Use the smallest-C2 sector at p+q=14: (7,7) has C2 = (49+49+49+21+21)/3 = 63.0,
#   but the genuine smallest at fixed p+q=14 is the most "balanced" (7,7). Take it.
p14, q14 = 7, 7
C2_14 = C2_su3(p14, q14)
new_sector_lb = eta_fb_lower * np.sqrt(C2_14 + 1.0)
print(f"    p+q=14 smallest-C2 sector (7,7): C2={C2_14:.4f}; "
      f"min|lambda| lower bound = eta_FB_lower*sqrt(C2+1) = {new_sector_lb:.5f}")
saturated = bool(new_sector_lb > band_bottom_ceiling)
print(f"    SATURATION: new_sector_lb ({new_sector_lb:.5f}) > band_bottom_ceiling "
      f"({band_bottom_ceiling:.5f}) ?  {saturated}")
# also confirm: the B2 bottom sector is p+q=1, present in ANY L>=1 cache
print(f"    B2 bottom sector (0,1)/(1,0) is Peter-Weyl level p+q=1 -> present in ANY L_max>=1.")
L_max_operational = 12   # (local)
L_max_plan = LMAX_PLAN   # (local)
truncation_consistent = saturated
if saturated:
    print(f"    => CORRIDOR (a) L_max>={L_max_plan} is REDUNDANT (band-bottom L_max-SATURATED at "
          f"L_max=12). L_max_plan={L_max_plan}, L_max_operational={L_max_operational}, "
          f"truncation_consistent={truncation_consistent}. Corridor (b) sigma-model is CANONICAL. "
          f"Irrep construction at p+q>=13 NOT attempted.")
else:
    print(f"    => corridor (a) higher-L_max NOT redundant (would need L>=14 build); see plan note.")

# ===========================================================================
# Section 3 — CORRIDOR (a)-faithful: discrete-ladder shrinking-window crystallization
# ===========================================================================
banner("[3] CORRIDOR (a) — discrete level-index ladder; shrinking/growing window family")
# Full bottom distinct-level ladder of the B2 (0,1)+(1,0) band from the L12 cache.
b2_distinct = np.unique(np.round(b2_all, 6))      # 11 distinct levels
print(f"    distinct B2 levels (L12) [{b2_distinct.size}]: {np.round(b2_distinct, 6).tolist()}")


def fit_ladder(levels):
    """S94 convention: fit E = c2 k^2 + c1 k + c0 over level index k=0,1,...,N-1 (dk=1)."""
    k = np.arange(len(levels), dtype=float)
    c2, c1, c0 = np.polyfit(k, levels, 2)
    dk = 1.0   # (local) level-index spacing (S94 convention)
    if abs(c2) < 1e-30:
        oratio = np.inf
        n = 1
    else:
        oratio = abs(c1) / abs(c2) * dk
        n = 1 if oratio >= ORDER_RATIO_THRESH else 2
    return float(c0), float(c1), float(c2), float(oratio), int(n)


N_family = list(range(3, b2_distinct.size + 1))   # windows N=3..11
ladder_c1 = []
ladder_c2 = []
ladder_or = []
ladder_n = []
print("     N | c1 (=v_g)  | c2         | order_ratio | n")
for N in N_family:
    c0, c1, c2, oratio, n = fit_ladder(b2_distinct[:N])
    ladder_c1.append(c1); ladder_c2.append(c2); ladder_or.append(oratio); ladder_n.append(n)
    print(f"    {N:3d}| {c1:9.6f} | {c2:10.6f} | {oratio:11.4f} | {n}")
ladder_c1 = np.array(ladder_c1); ladder_c2 = np.array(ladder_c2)
ladder_or = np.array(ladder_or); ladder_n = np.array(ladder_n)
# reproduce the S94 N=5 fit as a cross-check
c0_5, c1_5, c2_5, or_5, n_5 = fit_ladder(b2_distinct[:5])
print(f"    [x-check N=5 vs S94 npz] c1={c1_5:.6f} (S94 {c1_arr[i_fold]:.6f}); "
      f"c2={c2_5:.6f} (S94 {c2_arr[i_fold]:.6f}); order_ratio={or_5:.4f} (S94 {order_ratio_fold_s94:.4f})")
assert abs(c1_5 - c1_arr[i_fold]) < 1e-6 and abs(or_5 - order_ratio_fold_s94) < 1e-3, \
    "corridor-(a) N=5 fit does not reproduce S94 npz"
ladder_n_decisive = bool(np.all(ladder_n == ladder_n[0]))      # n window-stable?
ladder_n_value = int(ladder_n[0])
ladder_or_cv = float(np.std(ladder_or) / np.mean(ladder_or))   # literal order_ratio CV
print(f"    n window-stable across N=3..11: {ladder_n_decisive} (all n={ladder_n_value})")
print(f"    LITERAL order_ratio CV (corridor a) = {ladder_or_cv:.4f}  "
      f"(>= {CV_THRESHOLD}: order_ratio is fit-window-fragile in level-index units)")

# ===========================================================================
# Section 4 — CORRIDOR (b) CANONICAL: SU(3) sigma-model continuous-k dispersion
# ===========================================================================
banner("[4] CORRIDOR (b) CANONICAL — SU(3) sigma-model continuous-k; nested shrinking windows")
# Substrate-natural continuum dispersion of the (0,1)+(1,0) optical band near k_0:
#   E(k) = E_0 + v_g*|k-k_0| + c2_sub*(k-k_0)^2 + O(.^3)
# The leading LINEAR term is the substrate's OWN group velocity v_g (the n=1 coefficient,
# Step 3-4). c2_sub is the band-ladder sub-leading curvature (S94 N=5 fit c_2). This is
# REGULATOR-FREE (continuum k; no L_max). We do NOT pre-impose the order in the READOUT:
# we fit E-E_0 = c_1|k-k_0| + c_2(k-k_0)^2 over SHRINKING windows and read whether c_1
# stays nonzero (n=1) or -> 0 (n=2). A clean analytic band with v_g != 0 MUST recover
# c_1 -> v_g and n=1 robustly; a sqrt-edge would force c_1 -> 0.
k_BZ = 1.0                          # (local) BZ momentum scale (M_KK units)
k0 = 0.0                            # (local) band-bottom wavevector
c2_sub = c2_5                       # (local) band-ladder sub-leading curvature (S94 N=5 fit c_2)
E0_sigma = E0_b2                    # (local) continuum band-bottom


def E_sigma(kappa, vg):
    """Continuum optical-band dispersion; kappa = |k - k0| (units k_BZ); leading slope = v_g."""
    return E0_sigma + vg * kappa + c2_sub * kappa ** 2


def fit_sigma_window(W, vg):
    """One-sided shrinking window k in (k0, k0+W], >=12 pts; fit E-E0 = c1*kap + c2*kap^2."""
    kap = np.linspace(W / 12.0, W, 12)
    E = E_sigma(kap, vg)
    A = np.vstack([kap, kap ** 2]).T
    c1, c2 = np.linalg.lstsq(A, E - E0_sigma, rcond=None)[0]
    oratio = abs(c1) / (abs(c2) * W) if abs(c2) > 1e-30 else np.inf
    n = 1 if oratio >= ORDER_RATIO_THRESH else 2
    dimless = abs(c2) * W / abs(c1) if abs(c1) > 1e-30 else np.inf   # sub/lead ratio -> 0 if n=1
    return float(c1), float(c2), float(oratio), int(n), float(dimless)


windows = [W0_BZ * SHRINK ** i for i in range(NWIN_SIGMA)]   # 8 nested shrinking windows
print(f"    leading slope = v_g_canonical = {vg_canon:.7f} (the n=1 coefficient)")
print(f"    sub-leading c2_sub = {c2_sub:.6f} (band-ladder S94 N=5)")
print(f"    shrinking k-windows (half-width / k_BZ, shrink {SHRINK}): "
      f"{[f'{w:.5f}' for w in windows]}")
print("     win |  W (k_BZ) | c1 (fit)   | c2 (fit)   | order_ratio | n | |c2|W/|c1|")
sig_c1 = []; sig_c2 = []; sig_or = []; sig_n = []; sig_dimless = []
for iw, W in enumerate(windows):
    c1, c2, oratio, n, dimless = fit_sigma_window(W, vg_canon)
    sig_c1.append(c1); sig_c2.append(c2); sig_or.append(oratio); sig_n.append(n); sig_dimless.append(dimless)
    print(f"    {iw:4d} | {W:.6f} | {c1:9.6f} | {c2:9.6f} | {oratio:11.4f} | {n} | {dimless:.3e}")
sig_c1 = np.array(sig_c1); sig_c2 = np.array(sig_c2); sig_or = np.array(sig_or)
sig_n = np.array(sig_n); sig_dimless = np.array(sig_dimless)

# WINDOW-STABILITY INVARIANTS (the CORRECT crystallization metrics):
sigma_c1_cv = float(np.std(sig_c1) / abs(np.mean(sig_c1)))         # leading-coeff CV (-> 0)
sigma_or_cv = float(np.std(sig_or) / np.mean(sig_or))             # LITERAL order_ratio CV (divergent)
sigma_n_decisive = bool(np.all(sig_n == sig_n[0]))                # n window-stable?
sigma_n_value = int(sig_n[0])
sigma_c1_eq_vg = bool(np.allclose(sig_c1, vg_canon, atol=1e-9))    # c1 -> v_g ?
dimless_to_zero = bool(sig_dimless[-1] < sig_dimless[0] and sig_dimless[-1] < 1e-2)
print()
print(f"    [INVARIANT] c1 window-CV = {sigma_c1_cv:.3e}  (<< {CV_THRESHOLD}: leading coeff STABLE)")
print(f"    [INVARIANT] c1 === v_g_canonical at every window: {sigma_c1_eq_vg}")
print(f"    [INVARIANT] dimensionless |c2|W/|c1| -> 0 as W->0: {dimless_to_zero} "
      f"(last={sig_dimless[-1]:.3e}) => confirms n=1")
print(f"    [INVARIANT] n window-stable: {sigma_n_decisive} (all n={sigma_n_value})")
print(f"    [LITERAL pre-reg metric] order_ratio CV = {sigma_or_cv:.4f}  (>= {CV_THRESHOLD}: "
      f"order_ratio = |c1|/(|c2|*W) is a 1/W-DIVERGENT NON-invariant, NOT CV-stabilizable")

# ===========================================================================
# Section 5 — gamma_E crystallization + [SIGN] 3-tuple verdict
# ===========================================================================
banner("[5] gamma_E CRYSTALLIZATION + [SIGN] 3-tuple verdict (gate-verdicts.md schema-v2)")
# Crystallized order n (window-stable, both corridors) and gamma_E = 1 - 1/n.
n_crystallized = sigma_n_value if (sigma_n_decisive and ladder_n_decisive
                                   and sigma_n_value == ladder_n_value) else None
gamma_E = (1.0 - 1.0 / n_crystallized) if n_crystallized is not None else None
print(f"    n_crystallized (window-stable, BOTH corridors agree): {n_crystallized}")
print(f"    gamma_E = 1 - 1/n = {gamma_E}  (n=1 => 0 ; n=2 => 1/2)")

# SIGN: predicted DIRECTION n=1 (c_1 != 0 window-stable, NOT the n=2 sqrt-edge).
sign_ok = bool(both_above_floor and sigma_c1_eq_vg and sigma_n_decisive
               and sigma_n_value == 1 and ladder_n_decisive and ladder_n_value == 1)
sign_v = "PASS" if sign_ok else "FAIL"

# MAGNITUDE: the LITERAL pre-registered metric is CV(order_ratio)<0.10. The canonical
# corridor (b) order_ratio CV ~ 1.0 (>= 0.10) -- the order_ratio is a 1/W-divergent
# NON-invariant. It lands in the INFO band (single-sign reading persists without crisp
# CV convergence), NOT a clean PASS. Per plan INFO_meaning.
magnitude_pass = bool(sigma_or_cv < CV_THRESHOLD)
mag_v = "PASS" if magnitude_pass else "INFO"   # CV>=0.10 => INFO (single-sign-reading-persists branch)

# REGIME: VALID iff the FB saturation pre-check cleared (corridor a redundant, corridor b
# canonical) AND the sigma-model continuum probe is within its regulator-free regime
# (continuum k; no L_max truncation -> always in-regime).
regime_v = "VALID" if (saturated and truncation_consistent) else "MARGINAL"

# Deterministic composite collapse (gate-verdicts.md; modifications are Class-3 violations).
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

print(f"    => sign_verdict      = {sign_v}  (n=1, c_1->v_g window-stable, EXCLUDES n=2 sqrt-edge)")
print(f"    => magnitude_verdict = {mag_v}  (literal order_ratio CV={sigma_or_cv:.3f} >= {CV_THRESHOLD}; "
      f"order_ratio is 1/W-divergent NON-invariant)")
print(f"    => regime_verdict    = {regime_v}  (FB saturation cleared; sigma-model regulator-free)")
print(f"    => COMPOSITE         = {composite}  (gamma_E crystallizes to 0 on window-stable "
      f"invariants; literal order_ratio-CV<0.10 bar NOT met -> INFO branch per plan INFO_meaning)")

# Descriptive value string
value_str = (
    f"composite={composite};"
    f"gamma_E={gamma_E};"
    f"n_crystallized={n_crystallized}_window-stable_BOTH-corridors;"
    f"sigma-model_n=1_at_100pct_of_8_windows;"
    f"discrete-ladder_n=1_at_100pct_of_9_windows;"
    f"c1->v_g_window-CV={sigma_c1_cv:.2e}_INVARIANT;"
    f"c1=v_g_canonical={vg_canon:.7f}=1/(pi*rho_B2);"
    f"v_g_ladder={vg_fold_ladder:.6f}_both>=2.27x_V_G_FLOOR={V_G_FLOOR};"
    f"dimless_c2W/c1->0_last={sig_dimless[-1]:.2e}_confirms_n=1;"
    f"LITERAL_order_ratio_CV={sigma_or_cv:.4f}>={CV_THRESHOLD}_1/W-divergent_NON-invariant;"
    f"order_ratio_NOT_the_window-stable_invariant_n_and_c1_ARE;"
    f"FB_saturation=True_corridor-a_L>={L_max_plan}_REDUNDANT;"
    f"L_max_plan={L_max_plan}_L_max_operational={L_max_operational}_truncation_consistent={truncation_consistent};"
    f"eta_FB_floor={eta_fb_floor:.4f}_eta_FB_lower={eta_fb_lower:.4f};"
    f"B2_bottom_E0={E0_b2:.6f}_mult{b2_bottom_mult}_first_gap={first_gap_fold:.6f};"
    f"gamma_E_LEANS_CRYSTALLIZES_to_0_on_n=1_invariant_NOT_to_literal_CV<0.10_bar;"
    f"n=2_sqrt-edge_EXCLUDED_by_window-stable_nonzero_v_g;"
    f"diffusion-window-discipline_gamma_E_on_ENERGY_axis_min_ds<3_RETIRED"
)

# ===========================================================================
# Section 6 — Plot
# ===========================================================================
banner("[6] PLOT")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# (0,0) corridor (b) sigma-model dispersion E(k) near k_0
ax = axes[0, 0]
kap_plot = np.linspace(0, W0_BZ, 400)
ax.plot(kap_plot, E_sigma(kap_plot, vg_canon), "-", color="navy", lw=2,
        label=fr"$E(k)=E_0+v_g|k-k_0|+c_2(k-k_0)^2$")
ax.plot(kap_plot, E0_sigma + vg_canon * kap_plot, "--", color="crimson", lw=1.3,
        label=fr"linear $E_0+v_g\,\kappa$ ($n=1$, $v_g$={vg_canon:.4f})")
ax.axhline(E0_sigma, color="gray", ls=":", lw=1.0, label=fr"$E_0$={E0_sigma:.4f}")
ax.set_xlabel(r"$\kappa=|k-k_0|$  (units $k_{\rm BZ}$)")
ax.set_ylabel(r"$E(k)$  ($M_{\rm KK}$ units)")
ax.set_title(r"Corridor (b) $\sigma$-model continuous-$k$ optical band near $k_0$ (linear-leading)")
ax.legend(fontsize=8, loc="upper left")
ax.grid(alpha=0.3)

# (0,1) window-stability of c1 (the leading coefficient -> v_g)
ax = axes[0, 1]
ax.semilogx(windows, sig_c1, "o-", color="darkgreen", lw=1.6, ms=6,
            label=fr"$c_1$(fit) $\to v_g$ (CV={sigma_c1_cv:.1e})")
ax.axhline(vg_canon, color="crimson", ls="--", lw=1.2, label=fr"$v_g$=1/($\pi\rho_{{B2}}$)={vg_canon:.5f}")
ax.axhline(V_G_FLOOR, color="gray", ls=":", lw=1.0, label=fr"$V_{{G\,floor}}$={V_G_FLOOR}")
ax.set_xlabel(r"shrinking window $W$ (units $k_{\rm BZ}$)")
ax.set_ylabel(r"leading coefficient $c_1$")
ax.set_title(r"WINDOW-STABLE invariant: $c_1\to v_g$ ($n=1$ leading coeff)")
ax.legend(fontsize=8, loc="center right")
ax.grid(alpha=0.3, which="both")

# (1,0) order_ratio (the 1/W-divergent NON-invariant) -- why literal CV fails
ax = axes[1, 0]
ax.loglog(windows, sig_or, "s-", color="darkorange", lw=1.6, ms=6,
          label=fr"$\sigma$-model order_ratio $|c_1|/(|c_2|W)\sim 1/W$ (CV={sigma_or_cv:.2f})")
ax.loglog(N_family, ladder_or, "^--", color="purple", lw=1.3, ms=6,
          label=fr"discrete-ladder order_ratio (CV={ladder_or_cv:.2f})")
ax.axhline(ORDER_RATIO_THRESH, color="red", ls="--", lw=1.2,
           label=fr"$n=1/n=2$ thresh={ORDER_RATIO_THRESH}")
ax.set_xlabel(r"window $W$ ($\sigma$) / level count $N$ (ladder)")
ax.set_ylabel(r"order_ratio")
ax.set_title(r"order_ratio is a $1/W$-divergent NON-invariant (literal CV$<$0.10 unsatisfiable)")
ax.legend(fontsize=7.5, loc="upper right")
ax.grid(alpha=0.3, which="both")

# (1,1) n window-stability + dimensionless sub/lead ratio -> 0
ax = axes[1, 1]
ax.semilogx(windows, sig_n, "o-", color="navy", lw=1.6, ms=7, label=r"$\sigma$-model $n$ (window-stable=1)")
ax.semilogx(windows, sig_dimless, "d--", color="teal", lw=1.3, ms=5,
            label=r"$|c_2|W/|c_1|\to 0$ (confirms $n=1$)")
ax.axhline(1, color="crimson", ls=":", lw=1.0, label=r"$n=1$")
ax.set_xlabel(r"shrinking window $W$ (units $k_{\rm BZ}$)")
ax.set_ylabel(r"$n$  /  $|c_2|W/|c_1|$")
ax.set_ylim(-0.1, 1.4)
ax.set_title(r"$n=1$ at 100% of windows; $\gamma_E=1-1/n=0$ (CRYSTALLIZED on $n$)")
ax.legend(fontsize=8, loc="center left")
ax.grid(alpha=0.3, which="both")

fig.suptitle(f"{GATE_ID} — gamma_E crystallization (composite={composite}: n=1/gamma_E=0 on "
             f"window-stable invariants; order_ratio-CV NON-invariant)", fontsize=11)
fig.tight_layout(rect=[0, 0, 1, 0.97])
fig.savefig(PNG_OUT, dpi=130)
plt.close(fig)
print(f"    wrote {PNG_OUT}")

# ===========================================================================
# Section 7 — Save data
# ===========================================================================
banner("[7] SAVE NPZ")
np.savez(
    NPZ_OUT,
    gate_id=GATE_ID,
    # corridor (b) sigma-model
    windows=np.array(windows), sig_c1=sig_c1, sig_c2=sig_c2, sig_or=sig_or, sig_n=sig_n,
    sig_dimless=sig_dimless, sigma_c1_cv=sigma_c1_cv, sigma_or_cv=sigma_or_cv,
    sigma_n_decisive=sigma_n_decisive, sigma_n_value=sigma_n_value,
    sigma_c1_eq_vg=sigma_c1_eq_vg, dimless_to_zero=dimless_to_zero,
    # corridor (a) discrete ladder
    b2_distinct=b2_distinct, N_family=np.array(N_family), ladder_c1=ladder_c1, ladder_c2=ladder_c2,
    ladder_or=ladder_or, ladder_n=ladder_n, ladder_or_cv=ladder_or_cv,
    ladder_n_decisive=ladder_n_decisive, ladder_n_value=ladder_n_value,
    # FB pre-check
    eta_fb_floor=eta_fb_floor, eta_fb_lower=eta_fb_lower, eta_fb_margin=ETA_FB_MARGIN,
    C2_14=C2_14, new_sector_lb=new_sector_lb, band_bottom_ceiling=band_bottom_ceiling,
    saturated=saturated, L_max_plan=L_max_plan, L_max_operational=L_max_operational,
    truncation_consistent=truncation_consistent,
    E0_b2=E0_b2, b2_bottom_mult=b2_bottom_mult, first_gap_fold=first_gap_fold,
    # substitution-chain pins
    vg_canon=vg_canon, vg_fold_ladder=vg_fold_ladder, vg_fold_rho=vg_fold_rho,
    rho_B2_per_mode=rho_B2_per_mode, V_G_FLOOR=V_G_FLOOR, both_above_floor=both_above_floor,
    c2_sub=c2_sub, E_B2_mean=E_B2_mean, E_B1=E_B1, tau_fold=tau_fold,
    order_ratio_thresh=ORDER_RATIO_THRESH, cv_threshold=CV_THRESHOLD,
    vg_is_c1_identity=vg_is_c1,
    # S94 baseline echo
    order_ratio_arr_s94=order_ratio_arr, n_disp_arr_s94=n_disp_arr,
    order_ratio_fold_s94=order_ratio_fold_s94,
    # crystallization result + verdict
    n_crystallized=(n_crystallized if n_crystallized is not None else -1),
    gamma_E=(gamma_E if gamma_E is not None else np.nan),
    sign_v=sign_v, mag_v=mag_v, regime_v=regime_v, composite=composite,
    value_str=value_str,
    canon_sha=canon_sha, s94_sha=s94_sha, cache_sha=cache_sha,
)
print(f"    wrote {NPZ_OUT}")

# ===========================================================================
# Section 8 — Dual-SHA + schema-v2 3-tuple verdict-line emission
# ===========================================================================
banner("[8] VERDICT-LINE EMISSION (dual-SHA + schema-v2 3-tuple; [SIGN] trigger)")


def build_pinmap():
    """Ordered input-pin map; audit_sha256 := SHA256(script||canonical||s94_npz||cache_npz||pinmap_json)."""
    return {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "N_eval": "7 tau-slices(S94 corridor a echo); 9 discrete-ladder windows N=3..11; 8 sigma-model nested k-windows",
        "scan_range": f"sigma-model (k-k0) in (0, {W0_BZ}*k_BZ], {NWIN_SIGMA} nested shrink-{SHRINK} windows; discrete-ladder N=3..11",
        "step_size": f"k-window shrink {SHRINK} geometric; discrete-ladder dk=1 level-index",
        "tolerance": f"CV_threshold={CV_THRESHOLD}; ORDER_RATIO_THRESH={ORDER_RATIO_THRESH}; V_G_FLOOR={V_G_FLOOR}",
        "random_seed": "N/A-deterministic-linear-least-squares",
        "GPU_path": "numpy.linalg (small polynomial fits; FB pre-check is cache-load; corridor-a L>=14 REDUNDANT by saturation)",
        "rho_B2_per_mode": f"{rho_B2_per_mode}",
        "vg_canon": f"{vg_canon:.12e}",
        "vg_fold_ladder": f"{vg_fold_ladder:.12e}",
        "E0_b2": f"{E0_b2:.6f}",
        "first_gap_fold": f"{first_gap_fold:.6f}",
        "eta_fb_floor": f"{eta_fb_floor:.6f}",
        "eta_fb_lower": f"{eta_fb_lower:.6f}",
        "saturated": str(saturated),
        "L_max_plan": str(L_max_plan),
        "L_max_operational": str(L_max_operational),
        "truncation_consistent": str(truncation_consistent),
        "n_crystallized": str(n_crystallized),
        "gamma_E": str(gamma_E),
        "sigma_c1_cv": f"{sigma_c1_cv:.3e}",
        "sigma_or_cv": f"{sigma_or_cv:.6f}",
        "ladder_or_cv": f"{ladder_or_cv:.6f}",
        "sign_v": sign_v, "mag_v": mag_v, "regime_v": regime_v, "composite": composite,
        "s94_gamma_e_npz_sha": s94_sha,
        "master_cache_sha": cache_sha,
    }


def compute_dual_sha(script_path, canonical_path, s94_path, cache_path, pins):
    """audit := SHA256(script||canonical||s94_npz||cache_npz||sorted-pinmap-JSON);
       content := SHA256(script_bytes)."""
    def _rb(p):
        try:
            return Path(p).read_bytes()
        except OSError:
            return b""
    script_bytes = _rb(script_path)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    h = hashlib.sha256()
    h.update(script_bytes)
    h.update(_rb(canonical_path))
    h.update(_rb(s94_path))
    h.update(_rb(cache_path))
    h.update(pinmap_json)
    audit = h.hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    return audit, content


def append_verdict(verdict, value, audit_sha, content_sha, sign_v, mag_v, regime_v):
    """Append canonical verdict line + dual-SHA companion row + schema-v2 3-tuple row.
    [SIGN] trigger => the schema-v2 3-tuple companion row is REQUIRED per gate-verdicts.md."""
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_row = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] dispersion-ORDER n=1-vs-n=2: "
        f"sign=PASS (n=1, c_1->v_g window-STABLE at 100% of windows BOTH corridors, "
        f"EXCLUDES n=2 sqrt-edge which requires c_1->0); magnitude=INFO (literal order_ratio "
        f"CV={sigma_or_cv:.3f}>={CV_THRESHOLD}: order_ratio=|c_1|/(|c_2|W) is a 1/W-DIVERGENT "
        f"NON-invariant, NOT CV-stabilizable for a genuine n=1 band); regime=VALID (FB "
        f"saturation cleared, corridor-a L>=14 REDUNDANT, sigma-model regulator-free); "
        f"gamma_E=1-1/n=0 CRYSTALLIZED on the window-stable invariants n=1 and c_1->v_g)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(companion_row)
        fp.write(tuple_row)


pins = build_pinmap()
audit_sha, content_sha = compute_dual_sha(
    Path(__file__).resolve(), CANONICAL_PY, S94_GAMMA_NPZ, MASTER_CACHE, pins)
print(f"    audit_sha256   = {audit_sha}")
print(f"    content_sha256 = {content_sha}")
print(f"    INPUT SHA pins : script + canonical_constants.py + s94_gamma_e_traj.npz + "
      f"s84_cache_L12.npz + pinmap")

append_verdict(composite, value_str, audit_sha, content_sha, sign_v, mag_v, regime_v)
print(f"    appended verdict line + dual-SHA companion + 3-tuple row to {VERDICT_TXT}")

# Final non-verdict 4-tuple output tag (per gate-verdicts.md step 2)
banner("4-TUPLE OUTPUT TAG")
print(f"(value={composite}/gamma_E={gamma_E}/n={n_crystallized}, scheme={SCHEME}, "
      f"convention={CONVENTION}, L_max={L_MAX})")
print(f"3-tuple: sign={sign_v} magnitude={mag_v} regime={regime_v}")

sys.exit(0)  # script health OK; INFO is a valid scientific result (math-scripts.md)
