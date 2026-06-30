#!/usr/bin/env python3
"""
CF-S118-AS-CS-SUBSTRATE-FIRST  (S118 Wave 1, item W1-1)
=======================================================

Substrate-first hydrodynamic-IR sound speed c_s of the post-fold GGE two-fluid,
read off the a_2^{zeta} curvature channel of the D_K^2 spectral action -- the
Q23 A_s-magnitude rate-limiter.

SUBSTRATE-FIRST FRAMING (direction of explanation, NOT a "speed in a container"):
    D_K eigenvalues (s84 L12 cache, tau_fold=0.190)
      -> a_2^{zeta} Seeley-DeWitt curvature density  (FULL physical heat kernel)
      -> first/second-sound two-fluid ratio at the GGE relic
      -> intrinsic hydrodynamic-IR dispersion slope  c_s = d(omega^2)/d(k^2)|_IR
      -> acoustic sound horizon  l_horizon = c_s/(aH)_exit
      -> scale separation  Delta_scale  vs the xi_KZ occupation length
      -> deg=+2 substrate->pivot transport carrier test
      -> CMB A_s amplitude.
The substrate IS the acoustic medium; Planck's 2.1e-9 is the laboratory-IN
reading the substrate PREDICTS, not a target the substrate is fitted to.

GATE (set-membership, [SIGN] trigger):
    c_s in [cs_req_lo, cs_req_hi] = [0.5163972, 0.6501056]   (PASS-band)
      <=>  |2*Delta_scale(c_s) - fork_OOM| <= 0.10,   Delta_scale = log10( c_s/((aH)_exit*xi_KZ) )
    SIGN axis (two-fluid bracket): c_BLV <= c_s <= c_Gold  (0.485 <= c_s <= 0.915).
    PASS  -> deg=+2 transport SOLE carrier of the 0.668-OOM fork
           -> A_s resolves to the acoustic-horizon (H~, +0.196) grid, A_s=3.2994e-9; Q23 closes zero-parameter.
    FAIL  -> route to CF-S118-AS-PREFACTOR-SOURCE (residual non-scale prefactor co-carries).

PHYSICS OF THE DECOMPOSITION (first-principles; the gate delegates this to the executor):
    The substrate phonon dispersion is omega^2 = lambda^2 (Dirac energy^2) at
    spatial momentum^2 k^2 = C_2(p,q) (the SU(3) quadratic Casimir = fiber
    Laplacian eigenvalue of the Peter-Weyl (p,q) sector).  The hydrodynamic-IR
    sound speed is BY DEFINITION the long-wavelength group velocity:
          c_s^2 = ( d omega^2 / d k^2 )|_{k->0}  =  d <lambda^2> / d C_2 |_IR
    = K_grad / K_inertia, with (a_2^{zeta}-density x GGE weighted, Lagrangian
    G_ij/G_tt convention):
          K_grad   = Cov_w(lambda^2, C_2)   (gradient-stiffness cross second moment:
                     how the temporal energy^2 co-varies with the spatial Casimir-
                     momentum^2 -- the G_ij coefficient coupling fiber momentum to
                     curvature energy; > 0, energy rises with momentum)
          K_inertia= Var_w(C_2)             (Casimir-momentum second moment; the
                     inertial G_tt normalization; > 0, PSD spectrum)
    Both > 0 on the block-diagonal PSD D_K^2 spectrum; c_s = +sqrt(K_grad/K_inertia).

    CAUSALITY ORIENTS THE RATIO (a [SIGN] point):  the literal "spatial-Casimir /
    temporal-energy" reading c_s^2 = <C_2>/<lambda^2> = 2.79 is ACAUSAL (c_s=1.67>1)
    because the bare Casimir C_2 over-runs the Jensen-deformed lambda^2 at high (p,q)
    (e.g. (12,0): C_2=60 vs lambda^2 in [13.5,29.4]).  The PROVEN causality wall
    c_s<=1 forces the group-velocity orientation c_s^2 = d lambda^2/d C_2, which is
    sub-luminal and gap-separated (the intercept = condensate rest energy; the slope
    = sound).

GGE OCCUPATION:  the post-fold relic is SATURATED Parker pair production
    (P_exc_kz = 1.000; the GGE never thermalizes, R_therm=5252, S_ent=0): for the
    L12 band (all |lambda| in [0.82, 5.42], all deep in the sudden regime
    lambda*dt_transit << 1) the Bogoliubov occupation |beta_k|^2 is saturated and
    band-uniform.  Primary GGE weight n_k = P_exc_kz (uniform).  A cold thermal
    Bose-Einstein at T_acoustic is reported as a (non-thermal-regime) robustness
    comparator only.

MACHINERY: cached L12 sector_evals (Peter-Weyl block-decomposed); scalar heat-kernel
    sums + spectral moments; NO dense diagonalization, NO sparse-Lanczos.  CPU OMP=8.

Author: transit-dynamics-theorist  |  Session 118, Wave 1
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) avoid 32-core contention w/ parallel W1-2
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import time
import hashlib
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

GATE_ID = "CF-S118-AS-CS-SUBSTRATE-FIRST"
SCRIPT_PATH = Path(__file__).resolve()
PROJECT_ROOT = SCRIPT_PATH.parents[2]
SHARED = PROJECT_ROOT / "computations" / "_shared"
sys.path.insert(0, str(SHARED))

# --- canonical constants (MANDATORY import) -------------------------------------
from canonical_constants import (
    c_Gold, c_BLV, xi_KZ_FW, T_acoustic, tau_fold, P_exc_kz,
    M_KK, dt_transit, a2_fold,
)
# FULL physical heat-kernel evaluator (Chamseddine-Connes; NOT the SCHEMATIC helper)
from spectral_action import compute_heat_kernel, dim_su3_irrep

t_start = time.time()

# --- input file pins ------------------------------------------------------------
CANON = SHARED / "canonical_constants.py"
L12_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
GS1_NPZ = PROJECT_ROOT / "computations" / "session-117" / "s117_gs1_grid_selection.npz"
SPECTRAL_ACTION = SHARED / "spectral_action.py"

EXPECTED_SHA = {  # plan Input-SHA Ledger (S118 plan W1 sec.W1-1 input_files)
    "computations/_shared/canonical_constants.py":
        "d884a2b51200139296369dc6ed6ef2818b70386aee24e36b6c95365b43d3d78c",
    "computations/session-84/s84_spectrum_cache_L12_tau019.npz":
        "9e6d9cf7fd6a6949d622441b26fb9c2fa568654a22dc802e99898c326ca0f8d9",
    "computations/session-117/s117_gs1_grid_selection.npz":
        "dbecfedd3019d2f9c5db3caab31969578dc953c844da2526e1bb057980ebb1d0",
    "computations/_shared/spectral_action.py":
        "2ca6d921612305e4741fa158cb2f22bd35eb1484a731e8a27d709c965df1a025",
}


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(path).read_bytes())
    return h.hexdigest()


def log_input_pins() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}
    sha_ok = True  # (local)
    for p in (SCRIPT_PATH, CANON, L12_CACHE, GS1_NPZ, SPECTRAL_ACTION):
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        sha = sha256_of(p)
        pins[rel] = sha
        exp = EXPECTED_SHA.get(rel)
        tag = ""  # (local)
        if exp is not None:
            match = (sha == exp)            # (local)
            sha_ok = sha_ok and match
            tag = "  OK" if match else f"  *** MISMATCH vs plan ({exp[:16]}...) ***"
        print(f"  {rel}: {sha[:16]}...{tag}")
    return pins, sha_ok


def casimir_su3(p, q):
    """SU(3) quadratic Casimir C_2(p,q) = (p^2+q^2+p*q+3p+3q)/3.
    Convention: adjoint (1,1) -> C_2=3 (= N for su(N)); verified vs Weyl-dim sectors."""
    return (p * p + q * q + p * q + 3 * p + 3 * q) / 3.0


# ================================================================================
#  SECTION 1 -- load cached L12 spectrum (Peter-Weyl block-decomposed)
# ================================================================================
def load_spectrum():
    d = np.load(L12_CACHE, allow_pickle=True)
    se = d["sector_evals"].item()
    eval_data = []    # (local) list of (p,q,|lambda| array) for spectral_action heat kernel
    dims = []; C2 = []; lam = []; pq = []
    for (p, q), info in se.items():
        eva = np.abs(np.asarray(info["abs_evals"]).flatten())
        eva = eva[eva > 1e-9]
        if eva.size == 0:
            continue
        d_pq = dim_su3_irrep(p, q)
        assert d_pq == info["dim"], f"dim mismatch sector ({p},{q})"
        eval_data.append((p, q, eva))
        dims.append(np.full(eva.size, float(d_pq)))
        C2.append(np.full(eva.size, casimir_su3(p, q)))
        lam.append(eva)
        pq.append(np.full(eva.size, p + q))
    dims = np.concatenate(dims)
    C2 = np.concatenate(C2)
    lam = np.concatenate(lam)
    pq = np.concatenate(pq)
    return eval_data, dims, C2, lam, pq, se


# ================================================================================
#  SECTION 2 -- weighted dispersion-slope estimator  c_s^2 = K_grad/K_inertia
# ================================================================================
def slope_estimator(C2, lam2, w, c2_hi=None):
    """Weighted LSQ slope of lambda^2 on C_2 (intercept=gap). Returns (gap, slope, K_grad, K_inertia, n).
    K_grad   = Cov_w(lambda^2, C_2)  (gradient-stiffness cross second moment)
    K_inertia= Var_w(C_2)            (Casimir-momentum second moment)
    slope = K_grad/K_inertia = group velocity^2 = c_s^2 (gap-separated)."""
    m = np.ones(C2.shape, bool) if c2_hi is None else (C2 <= c2_hi)
    cc = C2[m]; yy = lam2[m]; ww = w[m]
    Wsum = ww.sum()
    cbar = (ww * cc).sum() / Wsum                 # (local) weighted mean C_2
    ybar = (ww * yy).sum() / Wsum                 # (local) weighted mean lambda^2
    K_grad = (ww * (cc - cbar) * (yy - ybar)).sum()      # (local) Cov_w
    K_inertia = (ww * (cc - cbar) ** 2).sum()            # (local) Var_w
    slope = K_grad / K_inertia
    gap = ybar - slope * cbar                     # (local) intercept
    return gap, slope, K_grad, K_inertia, int(m.sum())


def global_ratio(C2, lam2, w, exclude_condensate=True):
    """Phase-velocity^2 = <lambda^2>_w / <C_2>_w over finite-momentum (C_2>0) modes."""
    m = (C2 > 1e-9) if exclude_condensate else np.ones(C2.shape, bool)
    ww = w[m]
    return (ww * lam2[m]).sum() / (ww * C2[m]).sum()


def main():
    pins, sha_ok = log_input_pins()
    if not sha_ok:
        # Honest PRE-REG-INC: a SHA pin is the commitment; do NOT proceed under drift.
        print("\n*** INPUT SHA MISMATCH -- closing PRE-REG-INC (no convention-shopping). ***")
        payload = dict(verdict="PRE-REG-INC", value="input_sha_mismatch_vs_plan_ledger",
                       sign="N/A", magnitude="FAIL", regime="BREAKDOWN")
        return payload, {}

    eval_data, dims, C2, lam, pq, se = load_spectrum()
    lam2 = lam ** 2
    n_modes = lam.size
    print(f"\n[cache] {len(eval_data)} Peter-Weyl sectors, {n_modes} nonzero modes, "
          f"|lambda| in [{lam.min():.4f},{lam.max():.4f}], C_2 in [0,{C2.max():.1f}]")

    # --- window / fork constants from GS-1 npz (plan: sourced from s117_gs1_grid_selection.npz)
    g = np.load(GS1_NPZ, allow_pickle=True)
    cs_req_lo = float(g["cs_req_lo"]); cs_req_hi = float(g["cs_req_hi"])
    cs_req_center = float(g["cs_req_center"])
    fork_OOM = float(g["fork_OOM"]); aH_exit = float(g["aH_exit"])
    xi_KZ = float(g["l_occ"])                       # (local) = xi_KZ_FW
    assert abs(xi_KZ - xi_KZ_FW) < 1e-12, "xi_KZ npz vs canonical mismatch"
    occ_scale = aH_exit * xi_KZ                      # (local) occupation-horizon scale 0.26847
    print(f"[gs1] window c_s in [{cs_req_lo:.6f},{cs_req_hi:.6f}] center {cs_req_center:.6f}; "
          f"fork_OOM={fork_OOM:.6f}; aH_exit={aH_exit:.6f}; xi_KZ={xi_KZ:.8f}; occ_scale={occ_scale:.6f}")

    # ============================================================================
    #  SECTION 3 -- FULL physical heat-kernel a_2 validation (spectral_action.py)
    # ============================================================================
    t_hk = np.logspace(-3, -1, 24)                  # (local) plan t-window for t^{-3} moment
    K_t, _ = compute_heat_kernel(eval_data, t_hk)
    # K(t) = a0 t^-4 + a2 t^-3 + ... ; fit t^4 K(t) = a0 + a2 t + a4 t^2 + ...
    F = t_hk ** 4 * K_t                              # (local)
    V = np.vander(t_hk, N=5, increasing=True)        # (local) [1,t,t^2,t^3,t^4]
    wfit = 1.0 / t_hk                                # (local) weight small t
    coef = np.linalg.solve((V * wfit[:, None]).T @ V, (V * wfit[:, None]).T @ F)  # (local)
    a0_hk, a2_hk = float(coef[0]), float(coef[1])    # (local) heat-kernel Seeley-DeWitt
    print(f"\n[heat-kernel a_2 validation] a0={a0_hk:.4e}, a2={a2_hk:.4e} "
          f"(FULL physical Tr e^-tD^2; finite & {'positive' if a2_hk>0 else 'NONPOS'})")
    # a_2^{zeta} per-mode density rho_j = dim_j * |lambda_j|^-2  (= 0.5*zeta_D(1) density)
    a2_zeta_density = dims * lam ** -2               # (local)
    a2_zeta_total = 0.5 * a2_zeta_density.sum()      # (local) 0.5*zeta_D(1), L12 full
    print(f"[a_2^zeta] 0.5*zeta_D(1) on L12 full cache = {a2_zeta_total:.4e} "
          f"(canonical a2_fold={a2_fold:.4f}; NORMALIZATION CANCELS in c_s ratio)")

    # ============================================================================
    #  SECTION 4 -- GGE occupation  n_k
    # ============================================================================
    # PRIMARY: saturated Parker relic (P_exc_kz = 1.000; band-uniform in the sudden regime).
    n_sat = np.full(n_modes, float(P_exc_kz))        # (local) uniform saturated
    # comparator: cold thermal Bose-Einstein at T_acoustic (NOT the GGE regime; robustness only)
    n_BE = 1.0 / np.expm1(lam / T_acoustic)          # (local)
    sudden = lam * dt_transit                         # (local) adiabaticity param; <<1 => sudden
    print(f"\n[GGE] saturated Parker P_exc_kz={P_exc_kz} (band-uniform); "
          f"max(lambda*dt_transit)={sudden.max():.3e} << 1 (all modes sudden => saturated).")

    # ============================================================================
    #  SECTION 5 -- PRIMARY estimator: a_2^{zeta} x saturated-GGE dispersion slope
    #               over the hydrodynamic-IR Casimir window [C2_min, C2_min*e]
    # ============================================================================
    C2min = C2[C2 > 1e-9].min()                       # (local) 4/3
    c2_hi_IR = C2min * np.e                            # (local) bottom-decade ceiling
    w_primary = a2_zeta_density * n_sat               # (local) a_2^zeta x saturated GGE

    gapP, csqP, KgP, KiP, nP = slope_estimator(C2, lam2, w_primary, c2_hi=c2_hi_IR)
    c_s = float(np.sqrt(csqP))                        # (local) PRIMARY hydrodynamic-IR sound speed
    print(f"\n=== PRIMARY  c_s^2 = K_grad/K_inertia (a_2^zeta x sat-GGE IR dispersion slope) ===")
    print(f"  IR window C_2 in [{C2min:.4f},{c2_hi_IR:.4f}] ({nP} modes)")
    print(f"  K_grad (Cov_w)  = {KgP:.6e}   K_inertia (Var_w) = {KiP:.6e}")
    print(f"  gap(intercept)  = {gapP:.6f}   c_s^2 = {csqP:.6f}   c_s = {c_s:.6f}")

    # ============================================================================
    #  SECTION 6 -- cross-checks / robustness (NOT the verdict; map the estimator landscape)
    # ============================================================================
    print("\n=== cross-checks (robustness) ===")
    cc = {}  # (local)
    # (a) uniform (saturated) full-spectrum slope -- window-INDEPENDENT linear-acoustic signal
    _, csq_u, _, _, _ = slope_estimator(C2, lam2, np.ones(n_modes))
    cc["slope_uniform_full"] = float(np.sqrt(csq_u))
    # (b) a2^zeta x sat-GGE FULL-spectrum slope
    _, csq_zf, _, _, _ = slope_estimator(C2, lam2, w_primary)
    cc["slope_a2zeta_full"] = float(np.sqrt(csq_zf))
    # (c) global phase-velocity ratios (gap-contaminated upper estimates)
    cc["ratio_a2zeta"] = float(np.sqrt(global_ratio(C2, lam2, a2_zeta_density)))
    cc["ratio_a2zeta_GGEsat"] = float(np.sqrt(global_ratio(C2, lam2, w_primary)))
    cc["ratio_uniform"] = float(np.sqrt(global_ratio(C2, lam2, np.ones(n_modes))))
    # (d) cold-BE comparator (non-GGE-regime; expected lower)
    _, csq_be, _, _, _ = slope_estimator(C2, lam2, a2_zeta_density * n_BE, c2_hi=c2_hi_IR)
    cc["slope_a2zeta_coldBE_IR"] = float(np.sqrt(max(csq_be, 0.0)))
    # (e) acoustic-MINIMUM branch -> should reproduce c_BLV (lower bracket); machinery validation
    rows = {}
    for (p, q), info in se.items():
        eva = np.abs(np.asarray(info["abs_evals"]).flatten()); eva = eva[eva > 1e-9]
        if eva.size:
            rows[(p, q)] = (casimir_su3(p, q), float(dim_su3_irrep(p, q)), eva ** 2)
    num = den = 0.0
    for c2v, dpq, l2 in rows.values():
        num += dpq * l2.min(); den += dpq * c2v
    cc["acoustic_min_branch"] = float(np.sqrt(num / den))    # ~ c_BLV
    # (f) the ACAUSAL literal <C_2>/<lambda^2> reading (rejected by the causality wall c_s<=1)
    cc["acausal_C2_over_lam2"] = float(np.sqrt(
        (a2_zeta_density * C2).sum() / (a2_zeta_density * lam2).sum()))
    for k, v in cc.items():
        inwin = "IN-WINDOW" if cs_req_lo <= v <= cs_req_hi else ("below" if v < cs_req_lo else "above")
        print(f"  {k:<28} c_s = {v:.5f}   [{inwin}]")
    print(f"  (acoustic_min_branch vs canonical c_BLV={c_BLV}: "
          f"reldev {abs(cc['acoustic_min_branch']-c_BLV)/c_BLV*100:.2f}%  -- machinery validation)")

    # ============================================================================
    #  SECTION 7 -- AXIS 1 [SIGN]: positivity + two-fluid bracket  c_BLV <= c_s <= c_Gold
    # ============================================================================
    positive = (csqP > 0.0) and np.isreal(c_s)
    bracketed = (c_BLV <= c_s <= c_Gold)
    sign_verdict = "PASS" if (positive and bracketed) else "FAIL"
    print(f"\n=== AXIS 1 [SIGN] ===  c_s^2={csqP:.6f}>0 : {positive};  "
          f"c_BLV({c_BLV}) <= c_s({c_s:.4f}) <= c_Gold({c_Gold}) : {bracketed}  -> sign={sign_verdict}")

    # ============================================================================
    #  SECTION 8 -- AXIS 2 [MAGNITUDE]: window membership / |2*Dscale - fork_OOM|
    # ============================================================================
    dscale = float(np.log10(c_s / occ_scale))        # (local)
    two_dscale = 2.0 * dscale                         # (local) deg=+2 carrier
    resid = abs(two_dscale - fork_OOM)                # (local)
    in_window = (cs_req_lo <= c_s <= cs_req_hi)
    PASS_BAND, INFO_BAND = 0.10, 0.25                 # (local) plan tolerance
    if resid <= PASS_BAND:
        magnitude_verdict = "PASS"
    elif resid <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    print(f"\n=== AXIS 2 [MAGNITUDE] ===")
    print(f"  Delta_scale = log10(c_s/occ_scale) = {dscale:.6f};  2*Delta_scale = {two_dscale:.6f}")
    print(f"  |2*Delta_scale - fork_OOM| = |{two_dscale:.6f} - {fork_OOM:.6f}| = {resid:.6f}")
    print(f"  c_s in window [{cs_req_lo:.4f},{cs_req_hi:.4f}]: {in_window}  -> magnitude={magnitude_verdict}")

    # ============================================================================
    #  SECTION 9 -- AXIS 3 [REGIME]: hydrodynamic-IR gradient-expansion validity
    #               (a_4 K^4 << a_2 K^2 in-window  <=>  dispersion linear in IR)
    # ============================================================================
    # fit lambda^2 = gap + b1*C_2 + b2*C_2^2 over the IR window; require |b2*C2max^2| << |b1*C2max|
    mIR = (C2 <= c2_hi_IR)
    cc_ir = C2[mIR]; yy_ir = lam2[mIR]; ww_ir = w_primary[mIR]
    Vq = np.vander(cc_ir, N=3, increasing=True)       # (local) [1,C2,C2^2]
    coefq = np.linalg.solve((Vq * ww_ir[:, None]).T @ Vq, (Vq * ww_ir[:, None]).T @ yy_ir)  # (local)
    b1, b2 = float(coefq[1]), float(coefq[2])         # (local) linear, quadratic dispersion coeffs
    lin_term = abs(b1 * c2_hi_IR)                      # (local) a_2 K^2 scale at window edge
    quad_term = abs(b2 * c2_hi_IR ** 2)               # (local) a_4 K^4 scale at window edge
    breach = quad_term / (lin_term + 1e-30)           # (local) fraction of window where quad dominates
    if breach <= 0.05:
        regime_verdict = "VALID"
    elif breach <= 0.50:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    print(f"\n=== AXIS 3 [REGIME] ===  IR dispersion lambda^2 = gap + b1*C_2 + b2*C_2^2")
    print(f"  b1(linear)={b1:.5f}  b2(quad)={b2:.5f};  |a4 K^4|/|a2 K^2| at edge = {breach:.4e}")
    print(f"  uniform-slope window-independence (linear-acoustic) cross-check: "
          f"slope_uniform_full={cc['slope_uniform_full']:.5f}  -> regime={regime_verdict}")

    # ============================================================================
    #  SECTION 10 -- COMPOSITE collapse (gate-verdicts.md deterministic rule)
    # ============================================================================
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"
    print(f"\n=== COMPOSITE === sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict} -> {composite}")

    results = dict(
        c_s=c_s, c_s_sq=csqP, K_grad=KgP, K_inertia=KiP, gap=gapP, n_modes_IR=nP,
        a0_hk=a0_hk, a2_hk=a2_hk, a2_zeta_total=a2_zeta_total,
        cs_req_lo=cs_req_lo, cs_req_hi=cs_req_hi, cs_req_center=cs_req_center,
        fork_OOM=fork_OOM, aH_exit=aH_exit, xi_KZ=xi_KZ, occ_scale=occ_scale,
        dscale=dscale, two_dscale=two_dscale, resid=resid, in_window=in_window,
        c_BLV=c_BLV, c_Gold=c_Gold, bracketed=bracketed, positive=positive,
        b1_lin=b1, b2_quad=b2, regime_breach=breach,
        C2min=C2min, c2_hi_IR=c2_hi_IR, n_modes=n_modes,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        **{f"xchk_{k}": v for k, v in cc.items()},
    )
    payload = dict(verdict=composite, value=c_s, sign=sign_verdict,
                   magnitude=magnitude_verdict, regime=regime_verdict)
    # ---- plot ----
    make_plot(C2, lam2, w_primary, results, rows)
    # ---- save npz ----
    np.savez(SCRIPT_PATH.with_suffix(".npz"), **results)
    return payload, dict(results=results, pins=pins)


# ================================================================================
#  PLOT
# ================================================================================
def make_plot(C2, lam2, w, R, rows):
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))
    # panel 1: dispersion lambda^2 vs C_2 with IR slope
    sc = ax[0].scatter(C2, lam2, s=3, alpha=0.15, c="steelblue", label="modes (lambda^2 vs C_2)")
    c2g = np.linspace(0, C2.max(), 100)
    ax[0].plot(c2g, R["gap"] + R["c_s_sq"] * c2g, "r-", lw=2,
               label=f"IR slope c_s^2={R['c_s_sq']:.3f} (c_s={R['c_s']:.3f})")
    # acoustic-min branch
    cm = sorted(rows.items())
    ax[0].plot([casimir for casimir, _, _ in [(v[0], 0, 0) for _, v in cm]],
               [l2.min() for _, (_, _, l2) in cm], "g.", ms=6, label="acoustic min (-> c_BLV)")
    ax[0].axvline(R["c2_hi_IR"], color="gray", ls=":", alpha=0.6, label="IR window edge")
    ax[0].set_xlabel("C_2 (SU(3) Casimir = fiber momentum^2 = k^2)")
    ax[0].set_ylabel("lambda^2 (Dirac energy^2 = omega^2)")
    ax[0].set_title(f"{GATE_ID}: substrate dispersion + hydrodynamic-IR sound speed")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
    # panel 2: c_s vs GS-1 window + two-fluid bracket
    ax[1].axhspan(R["cs_req_lo"], R["cs_req_hi"], color="green", alpha=0.15,
                  label=f"GS-1 window [{R['cs_req_lo']:.3f},{R['cs_req_hi']:.3f}]")
    ax[1].axhline(R["cs_req_center"], color="green", ls="--", alpha=0.6, label="window center (deg+2)")
    ax[1].axhline(R["c_BLV"], color="purple", ls="-", alpha=0.7, label=f"c_BLV={R['c_BLV']} (2nd sound floor)")
    ax[1].axhline(R["c_Gold"], color="orange", ls="-", alpha=0.7, label=f"c_Gold={R['c_Gold']} (1st sound)")
    keys = ["c_s", "xchk_slope_uniform_full", "xchk_slope_a2zeta_full", "xchk_ratio_a2zeta",
            "xchk_ratio_a2zeta_GGEsat", "xchk_acoustic_min_branch"]
    labs = ["PRIMARY", "slope-unif", "slope-a2z", "ratio-a2z", "ratio-GGE", "acou-min"]
    vals = [R[k] for k in keys]
    ax[1].bar(range(len(vals)), vals, color=["red"] + ["steelblue"] * 4 + ["green"], alpha=0.75)
    ax[1].set_xticks(range(len(vals))); ax[1].set_xticklabels(labs, rotation=30, fontsize=8)
    ax[1].set_ylabel("c_s (M_KK units)")
    ax[1].set_title(f"c_s estimators vs GS-1 window  (composite {R['composite']})")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3, axis="y")
    fig.tight_layout()
    fig.savefig(SCRIPT_PATH.with_suffix(".png"), dpi=140, bbox_inches="tight")
    plt.close(fig)


# ================================================================================
#  DUAL-SHA + verdict payload
# ================================================================================
def print_verdict_payload(payload, pins):
    """Print the canonical verdict payload (script computes SHAs; agent calls emit_verdict)."""
    script_bytes = SCRIPT_PATH.read_bytes()
    canon_bytes = CANON.read_bytes()
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")
    audit = hashlib.sha256(script_bytes + canon_bytes + pinmap_json).hexdigest()
    content = hashlib.sha256(script_bytes).hexdigest()
    out = dict(
        session=118, gate_id=GATE_ID, verdict=payload["verdict"],
        value=payload["value"],
        scheme="a2-curvature-channel-GGE-two-fluid",
        convention=("hydrodynamic-IR-first-second-sound-ratio;"
                    "Delta_scale=log10(c_s/((aH)_exit*xi_KZ));poleconv-A-double"),
        l_max="12",
        audit_sha256=audit, content_sha256=content,
        sign_verdict=payload["sign"], magnitude_verdict=payload["magnitude"],
        regime_verdict=payload["regime"], schema_version="S84+",
    )
    print("\n=== VERDICT PAYLOAD (for emit_verdict) ===")
    print(json.dumps(out, indent=2))
    print(f"\nVERDICT-LINE-PREVIEW: {GATE_ID}: {out['verdict']} -- value='{out['value']}' "
          f"scheme={out['scheme']} convention={out['convention']} L_max=12 "
          f"audit_sha256={audit} content_sha256={content} schema_version=S84+")
    print(f"3-TUPLE: sign_verdict={out['sign_verdict']} "
          f"magnitude_verdict={out['magnitude_verdict']} regime_verdict={out['regime_verdict']}")
    return out


if __name__ == "__main__":
    payload, extra = main()
    out = print_verdict_payload(payload, extra.get("pins", {}))
    print(f"\n[elapsed] {time.time()-t_start:.1f}s")
    print("DONE.")
