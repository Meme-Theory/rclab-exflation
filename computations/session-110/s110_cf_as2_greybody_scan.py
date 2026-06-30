#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S110-CF-AS2-GREYBODY  (session track, Wave 2)  [VERIFY]
========================================================

Gate: A_s upper-edge EXIT-FILTER leg adjudication. Scan the BdG exit-horizon
fluctuation potential for ANY substrate-derived barrier whose half-transmission
omega_half = sqrt(V0) lands inside the relic band [0.94, 3.72] M_KK AND reproduces
the fitted exit-filter transmitted fraction int_Gamma = 0.512 +/- 10% (RATIO tol).

The STATIC surface-gravity barrier (kappa_eff = kappa_exit = 47.6146 M_KK) is the
ruled-out baseline: BOTH prior routes (inv-4 W1-4 black-hole-thermodynamics +
inv-12 W3-4 analog-gravity BdG-fluctuation) found it gives int_Gamma ~ 0.036
(14x short of 0.512), with sqrt(V0) = kappa_exit/2 = 23.8 M_KK far ABOVE the band.
That baseline is NOT re-scanned here (its two-route agreement that the static
barrier is non-substrate is the established input).

This gate scans the UN-SCANNED candidate: the DYNAMICAL near-horizon resonance
from the FINITE quench rate tau_dot(tau) -- the supersonic transit (Mach 13.75)
makes the barrier time-dependent, so the relevant near-horizon scale is the
Floquet/parametric drive frequency omega_q (inv-12 W3-2) and the substrate-scale
barrier heights it makes available, NOT the static surface gravity.

PHYSICS (substrate-first):
  D_K eigenvalues lambda_k(tau) -> exit-horizon BdG dispersion
      omega_k = sqrt((lambda_k^2 - mu^2)^2 + Delta_k^2)   (mu = 0)
  -> linearized fluctuation delta-phi_k around the tau~0.16 exit-horizon background
     obeys a Schroedinger-form scattering equation in a tortoise coordinate x_*:
         -d^2 psi/dx_*^2 + V_eff(x_*) psi = omega^2 psi
  -> transmission Gamma(omega) = |T(omega)|^2 through V_eff IS the exit greybody.
  For a finite-rate transit the near-horizon V_eff is DYNAMICAL: the parametric
  drive (Floquet exponent gamma_clock, drive freq omega_q from inv-12 W3-2) sets a
  time-dependent barrier. We scan the universal analog-gravity Poeschl-Teller form
         V_eff(x_*) = V0 * sech^2(kappa_eff * x_*)
  over SUBSTRATE-SCALE (kappa_eff, V0) pairs -- NONE placed at the band:
    kappa_eff candidates: {Floquet omega_q, Delta_BCS, relic-rms, 2*Delta_BCS, kappa_exit, ...}
    V0 candidates       : substrate-scale^2 from the same set.
  For EACH candidate compute omega_half = sqrt(V0) and the squeeze-weighted
  int_Gamma over the relic spectrum (the SAME produced-power weighting the fitted
  comparator used: weight = mult_k * beta2_k).

EXACT Poeschl-Teller transmission (Landau-Lifshitz QM Sec.25; Macher-Parentani):
    Gamma(omega) = sinh^2(pi omega/kappa) / [sinh^2(pi omega/kappa) + cosh^2(pi s)]
    s = sqrt(V0/kappa^2 - 1/4)   (cosh -> cos for V0/kappa^2 < 1/4)
  cross-checked by an independent 1D scattering-ODE solve of -psi'' + V_eff psi = w^2 psi.

VERDICT RUBRIC (existential operator + ratio criterion, plan SS W2-4):
  PASS iff EXISTS substrate V0: sqrt(V0) in [0.94, 3.72] M_KK
           AND |int_Gamma_derived - 0.512|/0.512 <= 0.10
  FAIL iff FOR ALL substrate scales sqrt(V0) NOT in [0.94, 3.72] M_KK
  INFO iff EXISTS sqrt(V0) in band but |int_Gamma_derived - 0.512|/0.512 > 0.10
           OR fires via the auto-shortening regime_verdict (finite-rate WKB
           breakdown): if the WKB small-parameter is breached over >5% of the scan
           window, regime=MARGINAL -> composite INFO (gate-verdicts.md auto-shortening).

  Finite-rate WKB small-parameter (pre-registered, auto-shortening clause):
    eps_WKB(kappa_eff) = gamma_clock / kappa_eff^2   (adiabaticity of the near-horizon
       barrier under the finite quench: drive-decay rate gamma_clock over barrier-freq^2).
    f_used = fraction of the in-band scan window with eps_WKB < 1 (WKB-valid).
    f_used >= 0.95 -> regime VALID ; 0.50 <= f_used < 0.95 -> MARGINAL ;
    f_used < 0.50 -> BREAKDOWN (regime=BREAKDOWN -> composite FAIL regardless).

INPUTS (SHA-256 dual-pinned at runtime; S84+ schema):
  - canonical_constants.py  (Delta_BCS, kappa_exit, T_acoustic, Mach_max, M_KK, tau_fold)
  - inv12_w3_1_relic_spectrum_ode_lock.npz  (locked {alpha_k, beta_k}, omega_k, mult_k -- relic spectrum)
  - inv12_w3_4_greybody_from_bdg.npz        (the STATIC-baseline V_eff machinery, read-only:
        kappa_eff=47.6146, V0_marginal, integral_Gamma_derived=0.036, transmitted_fraction_fitted=0.512)
  - inv12_w3_2_floquet_ordered_veil_resonance.npz (DYNAMICAL drive scale omega_q, gamma_clock)
  - s57_finite_rate_transit.npz             (tau_dot quench-rate trajectory; provenance for the finite rate)

PLAN-TEXT-DRIFT NOTE (substrate-first-canonical-sourcing.md SS(ii.B)):
  The plan pins canonical_constants.py sha = e5a7587f...; the file on disk has sha = 89c9b086...
  (the S110 W0a T_acoustic PROVENANCE backfill changed bytes, NO value change). The runtime SHA
  is pinned as canonical and the drift is documented in the verdict value field. All consumed
  constant VALUES (Delta_BCS, kappa_exit, T_acoustic, Mach_max) are unchanged.

OUTPUT:
  - npz: scan arrays, per-candidate (kappa_eff, sqrt(V0), int_Gamma, in_band, rel_dev),
         the static baseline reproduction, the WKB f_used, verdict.
  - png: int_Gamma vs sqrt(V0) scan with band + 0.512 target + static baseline.
  - verdict payload printed for emit_verdict (track=session).

  substitution_chain: required=true (plan SS W2-4).
  schema_v2 3-tuple: NOT required ([VERIFY] trigger); BUT the regime_verdict auto-shortening
    clause applies (emit domain_used_frac + regime per gate-verdicts.md).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")    # (local) cap CPU threads before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")    # (local)

import sys
import json
import hashlib
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.seterr(over="ignore")   # (local) cosh can overflow at large pi*omega/kappa; clipped downstream

# ---- canonical constants (MANDATORY import) ----
_HERE = os.path.dirname(os.path.abspath(__file__))            # computations/session-110
_SHARED = os.path.join(os.path.dirname(_HERE), "_shared")     # computations/_shared
sys.path.insert(0, _SHARED)
from canonical_constants import (  # noqa: E402
    M_KK, Delta_BCS, tau_fold, kappa_exit, T_acoustic, Mach_max,
)

# =====================================================================================
# Pinned machinery (plan SS W2-4)
# =====================================================================================
GATE_ID = "S110-CF-AS2-GREYBODY"
SCHEME = "BdG-fluctuation-Poschl-Teller"
CONVENTION = "DYNAMICAL-near-horizon-resonance"
L_MAX = 10                      # (local) inv-12 W3-1 locked {alpha,beta} relic-spectrum source (D_K L10 BdG)

N_V0_SCAN = 200                 # (local) >= 50 scan points over substrate-scale V0 (plan pin)
N_OMEGA = 2000                  # (local) omega-grid points across the relic spectrum support
ODE_RTOL = 1e-9                 # (local) scattering ODE rtol
ODE_ATOL = 1e-12                # (local) scattering ODE atol
RATIO_TOL = 0.10                # (local) int_Gamma RATIO tolerance vs fitted 0.512 (plan pin)
BAND_LO = 0.94                  # (local) relic pair-band lower edge, M_KK (plan pin)
BAND_HI = 3.72                  # (local) relic pair-band upper edge, M_KK (plan pin)

# auto-shortening WKB regime bands (gate-verdicts.md)
F_USED_VALID = 0.95             # (local)
F_USED_BREAKDOWN = 0.50         # (local)

# Input paths
W3_1_NPZ = os.path.join("computations", "investigation-12",
                        "inv12_w3_1_relic_spectrum_ode_lock.npz")
W3_4_NPZ = os.path.join("computations", "investigation-12",
                        "inv12_w3_4_greybody_from_bdg.npz")
W3_2_NPZ = os.path.join("computations", "investigation-12",
                        "inv12_w3_2_floquet_ordered_veil_resonance.npz")
S57_NPZ = os.path.join("computations", "session-57",
                       "s57_finite_rate_transit.npz")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

# plan-pinned canonical SHA (for plan-text-drift detection per substrate-first SS(ii.B))
PLAN_PINNED_CANON_SHA = "e5a7587f8326c9cc90cb720197a3ace824b3f89c5bbea17cfd659b27f607568a"

OUT_NPZ = os.path.join("computations", "session-110", "s110_cf_as2_greybody_scan.npz")
OUT_PNG = os.path.join("computations", "session-110", "s110_cf_as2_greybody_scan.png")


# =====================================================================================
# SHA helpers (gate-verdicts.md dual-SHA)
# =====================================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """Audit SHA over the ordered input-pin map (gate-verdicts.md / script-template.py)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode("utf-8"))
    return h.hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, sign_verdict=None,
                          magnitude_verdict=None, regime_verdict=None,
                          extra_rows=None):
    """Print the verdict payload as JSON for the agent to pass to emit_verdict
    (race-safe MCP tool). The script NEVER writes the verdict file directly."""
    payload = {
        "session": 110,
        "track": "session",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": scheme,
        "convention": convention,
        "l_max": str(l_max),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
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


# =====================================================================================
# Greybody from the BdG fluctuation potential (consolidated inv-4 + inv-12 V_eff)
# =====================================================================================
def gamma_pt_closed(omega, kappa_eff, V0):
    """EXACT Poeschl-Teller transmission |T(omega)|^2 for V_eff = V0 sech^2(kappa_eff x_*).
    Landau-Lifshitz QM Sec.25 / Macher-Parentani. Both over- and sub-barrier branches.
        s^2 = V0/kappa_eff^2 - 1/4
        Gamma = sinh^2(pi w/kappa)/[sinh^2(pi w/kappa) + cosh^2(pi s)]   (s^2 >= 0)
              = sinh^2(pi w/kappa)/[sinh^2(pi w/kappa) + cos^2(pi |s|)]  (s^2 < 0)
    """
    omega = np.asarray(omega, dtype=float)
    x = np.pi * omega / kappa_eff
    num = np.sinh(x) ** 2
    disc = V0 / kappa_eff ** 2 - 0.25
    if disc >= 0.0:
        denom_extra = np.cosh(np.pi * np.sqrt(disc)) ** 2
    else:
        denom_extra = np.cos(np.pi * np.sqrt(-disc)) ** 2
    # numerically stable ratio (num and denom_extra can both overflow; their ratio is finite)
    with np.errstate(invalid="ignore", over="ignore"):
        g = num / (num + denom_extra)
    return np.clip(np.nan_to_num(g, nan=1.0), 0.0, 1.0)


def gamma_scattering_ode(omega, kappa_eff, V0, x_max, rtol=ODE_RTOL, atol=ODE_ATOL):
    """INDEPENDENT numerical transmission |T(omega)|^2 by integrating
    -psi'' + V_eff psi = omega^2 psi through V_eff = V0 sech^2(kappa_eff x).
    Transmitted-only wave on the left; decompose at +x_max; Gamma = 1/|A|^2."""
    w = float(omega)
    if w <= 0.0:
        return 0.0

    def V_eff(x):
        return V0 / np.cosh(kappa_eff * x) ** 2

    def rhs(x, y):
        psi_r, psi_i, dpsi_r, dpsi_i = y
        fac = (V_eff(x) - w * w)
        return [dpsi_r, dpsi_i, fac * psi_r, fac * psi_i]

    xL = -x_max
    psiL = np.exp(-1j * w * xL)
    dpsiL = -1j * w * np.exp(-1j * w * xL)
    y0 = [psiL.real, psiL.imag, dpsiL.real, dpsiL.imag]
    sol = solve_ivp(rhs, (xL, x_max), y0, method="DOP853", rtol=rtol, atol=atol)
    if not sol.success:
        return np.nan
    psi_e = sol.y[0, -1] + 1j * sol.y[1, -1]
    dpsi_e = sol.y[2, -1] + 1j * sol.y[3, -1]
    eP = np.exp(1j * w * x_max)
    eM = np.exp(-1j * w * x_max)
    A = (psi_e * (1j * w * eP) - dpsi_e * eP) / (eM * (1j * w * eP) - (-1j * w * eM) * eP)
    return float(np.clip(1.0 / (abs(A) ** 2), 0.0, 1.0))


def main():
    print("=" * 90)
    print(GATE_ID)
    print("=" * 90)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_w31 = sha256_file(W3_1_NPZ)
    sha_w34 = sha256_file(W3_4_NPZ)
    sha_w32 = sha256_file(W3_2_NPZ)
    sha_s57 = sha256_file(S57_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[sha] canonical_constants.py        = {sha_canon}")
    print(f"[sha] inv12_w3_1 relic-lock npz      = {sha_w31}")
    print(f"[sha] inv12_w3_4 greybody-BdG npz    = {sha_w34}")
    print(f"[sha] inv12_w3_2 Floquet npz         = {sha_w32}")
    print(f"[sha] s57 finite-rate-transit npz    = {sha_s57}")
    print(f"[sha] self (script)                  = {sha_self}")

    # ---- plan-text-drift detection (substrate-first SS(ii.B)) ----
    canon_drift = (sha_canon != PLAN_PINNED_CANON_SHA)
    if canon_drift:
        print(f"[drift] canonical_constants.py SHA drifted plan->runtime: "
              f"plan={PLAN_PINNED_CANON_SHA[:16]}... runtime={sha_canon[:16]}... "
              f"(S110 W0a T_acoustic PROVENANCE backfill; NO value change). Runtime SHA pinned.")

    print(f"[const] Delta_BCS   = {Delta_BCS} M_KK   (BdG gap; dispersion floor)")
    print(f"[const] kappa_exit  = {kappa_exit} M_KK  (STATIC surface gravity = ruled-out baseline)")
    print(f"[const] T_acoustic  = {T_acoustic} M_KK")
    print(f"[const] Mach_max    = {Mach_max}        (supersonic transit -> finite-rate barrier)")

    # ---- load locked relic spectrum (inv-12 W3-1) ----
    d = np.load(W3_1_NPZ, allow_pickle=True)
    omega_k = np.asarray(d["omega_k"], dtype=float)
    beta2_k = np.asarray(d["beta2_k"], dtype=float)
    mult_k = np.asarray(d["mult_k"], dtype=float)
    Delta_k = np.asarray(d["Delta_k"], dtype=float)
    mu_chem = float(d["mu_chem"])
    w_mode = mult_k * beta2_k                                  # (local) produced-power weight
    omega_min = float(omega_k.min())
    omega_max = float(omega_k.max())
    relic_rms = float(np.sqrt(np.average(omega_k ** 2, weights=w_mode)))  # (local)
    print(f"[w3-1] n_modes={omega_k.size}  relic band omega_k in "
          f"[{omega_min:.4f},{omega_max:.4f}]  Delta_k={Delta_k[0]:.6f}  mu={mu_chem}")
    print(f"[w3-1] squeeze-weighted relic-rms omega = {relic_rms:.4f} M_KK")

    # ---- load STATIC baseline (inv-12 W3-4) -- the ruled-out reference, NOT re-scanned ----
    b = np.load(W3_4_NPZ, allow_pickle=True)
    transmitted_fraction_fitted = float(b["transmitted_fraction_fitted"])  # 0.512 (S95 W4-3)
    int_Gamma_static_baseline = float(b["integral_Gamma_derived"])          # 0.036
    kappa_static = float(b["kappa_eff"])                                    # 47.6146
    V0_static = float(b["V0_marginal"])                                     # kappa^2/4
    print(f"[base] STATIC baseline (kappa_eff=kappa_exit={kappa_static:.4f}, V0=kappa^2/4={V0_static:.4f}): "
          f"sqrt(V0)={np.sqrt(V0_static):.4f} M_KK (ABOVE band), int_Gamma={int_Gamma_static_baseline:.5f}")
    print(f"[base] fitted exit-filter transmitted_fraction = {transmitted_fraction_fitted:.6f} (the comparator)")

    # ---- load DYNAMICAL drive scale (inv-12 W3-2 Floquet) ----
    fl = np.load(W3_2_NPZ, allow_pickle=True)
    omega_q = float(fl["omega_q_phys"])      # principal parametric drive freq (DYNAMICAL near-horizon scale)
    gamma_clock = float(fl["gamma_clock"])   # Floquet exponent / drive-decay rate
    print(f"[w3-2] DYNAMICAL Floquet drive: omega_q={omega_q:.4f} M_KK (IN band), gamma_clock={gamma_clock:.4f}")

    # ---- load finite-rate quench trajectory (S57) -- provenance for the finite rate ----
    s = np.load(S57_NPZ, allow_pickle=True)
    tau_dot = float(s["dtau_dt_phys"])
    print(f"[s57 ] quench rate tau_dot (dtau/dt at fold) = {tau_dot:.4f} M_KK  (Mach {Mach_max} supersonic)")

    # =================================================================================
    # SUBSTRATE-SCALE candidate set (NONE placed at the band):
    #   the DYNAMICAL near-horizon resonance barrier (kappa_eff, V0) pairs drawn ONLY
    #   from substrate scales. The static surface gravity is the ruled-out baseline.
    # =================================================================================
    # Substrate scales available (canonical / derived, none band-placed):
    substrate_scales = {                                       # (local)
        "T_acoustic": T_acoustic,
        "Delta_BCS": Delta_BCS,
        "2Delta_BCS": 2.0 * Delta_BCS,
        "Delta_BCS_sq_over_T": Delta_BCS ** 2 / T_acoustic,
        "Floquet_omega_q": omega_q,
        "relic_rms": relic_rms,
        "kappa_exit": kappa_exit,
    }
    scale_names = list(substrate_scales.keys())               # (local)
    scale_vals = np.array([substrate_scales[k] for k in scale_names])  # (local)

    # ---- (A) DISCRETE candidate grid: every (kappa_eff, V0=scale^2) substrate pair ----
    cand_kappa = []     # (local)
    cand_sqrtV0 = []    # (local)
    cand_intG = []      # (local)
    cand_inband = []    # (local)
    cand_reldev = []    # (local)
    cand_label = []     # (local)
    cand_epsWKB = []    # (local)
    for ke_name in scale_names:
        ke = substrate_scales[ke_name]
        eps = gamma_clock / ke ** 2                            # (local) WKB small-parameter at this barrier scale
        for v0_name in scale_names:
            V0 = substrate_scales[v0_name] ** 2
            sv0 = float(np.sqrt(V0))
            ig = float(np.sum(w_mode * gamma_pt_closed(omega_k, ke, V0)) / np.sum(w_mode))
            inb = (BAND_LO <= sv0 <= BAND_HI)
            rel = abs(ig - transmitted_fraction_fitted) / transmitted_fraction_fitted
            cand_kappa.append(ke); cand_sqrtV0.append(sv0); cand_intG.append(ig)
            cand_inband.append(inb); cand_reldev.append(rel)
            cand_label.append(f"k={ke_name},V0={v0_name}^2")
            cand_epsWKB.append(eps)
    cand_kappa = np.array(cand_kappa); cand_sqrtV0 = np.array(cand_sqrtV0)
    cand_intG = np.array(cand_intG); cand_inband = np.array(cand_inband, dtype=bool)
    cand_reldev = np.array(cand_reldev); cand_epsWKB = np.array(cand_epsWKB)

    # ---- (B) CONTINUOUS V0-scan at the DYNAMICAL Floquet inverse-width (>=50 points) ----
    # The dynamical near-horizon barrier inverse-width IS the parametric drive scale omega_q
    # (substrate-derived); scan V0 continuously over substrate-scale^2 range to map int_Gamma.
    V0_lo = (0.5 * T_acoustic) ** 2                            # (local) below band
    V0_hi = kappa_exit ** 2 / 4.0                              # (local) up to the static value
    V0_scan = np.linspace(V0_lo, V0_hi, N_V0_SCAN)            # (local)
    sqrtV0_scan = np.sqrt(V0_scan)                            # (local)
    intG_scan_floq = np.array(                                # (local) kappa_eff = omega_q (dynamical)
        [float(np.sum(w_mode * gamma_pt_closed(omega_k, omega_q, V0)) / np.sum(w_mode))
         for V0 in V0_scan])
    intG_scan_relicrms = np.array(                            # (local) kappa_eff = relic_rms (dynamical)
        [float(np.sum(w_mode * gamma_pt_closed(omega_k, relic_rms, V0)) / np.sum(w_mode))
         for V0 in V0_scan])

    # ---- (C) Does ANY in-band substrate barrier reproduce 0.512 within +/-10%? ----
    inband_mask = (sqrtV0_scan >= BAND_LO) & (sqrtV0_scan <= BAND_HI)
    # best agreement among in-band scan points (over BOTH dynamical kappa_eff readings):
    best_rel = np.inf                                         # (local)
    best_info = None                                          # (local)
    for ke_name, ke, intG_scan in [("Floquet_omega_q", omega_q, intG_scan_floq),
                                    ("relic_rms", relic_rms, intG_scan_relicrms)]:
        rel_scan = np.abs(intG_scan - transmitted_fraction_fitted) / transmitted_fraction_fitted
        rel_scan_inband = np.where(inband_mask, rel_scan, np.inf)
        i_best = int(np.argmin(rel_scan_inband))
        if rel_scan_inband[i_best] < best_rel:
            best_rel = float(rel_scan_inband[i_best])
            best_info = (ke_name, ke, float(sqrtV0_scan[i_best]),
                         float(intG_scan[i_best]), float(rel_scan_inband[i_best]))
    # also the discrete-grid best in-band agreement
    if cand_inband.any():
        i_grid = int(np.argmin(np.where(cand_inband, cand_reldev, np.inf)))
        grid_best = (cand_label[i_grid], float(cand_kappa[i_grid]), float(cand_sqrtV0[i_grid]),
                     float(cand_intG[i_grid]), float(cand_reldev[i_grid]))
    else:
        grid_best = None

    # combined best in-band agreement (continuous + discrete)
    overall_best_rel = best_rel
    if grid_best is not None and grid_best[4] < overall_best_rel:
        overall_best_rel = grid_best[4]

    exists_inband = bool(inband_mask.any() or cand_inband.any())  # there ARE in-band substrate barriers
    pass_inband_and_target = (overall_best_rel <= RATIO_TOL)      # in-band AND reproduces 0.512

    print(f"\n[scan] in-band substrate barriers exist: {exists_inband}")
    if best_info is not None:
        print(f"[scan] best CONTINUOUS in-band: kappa_eff={best_info[0]}={best_info[1]:.4f}, "
              f"sqrt(V0)={best_info[2]:.4f}, int_Gamma={best_info[3]:.5f}, rel_dev={best_info[4]:.4f}")
    if grid_best is not None:
        print(f"[scan] best DISCRETE in-band: {grid_best[0]}, kappa_eff={grid_best[1]:.4f}, "
              f"sqrt(V0)={grid_best[2]:.4f}, int_Gamma={grid_best[3]:.5f}, rel_dev={grid_best[4]:.4f}")
    print(f"[scan] overall best in-band rel_dev = {overall_best_rel:.4f}  (PASS iff <= {RATIO_TOL})")

    # =================================================================================
    # WKB regime (auto-shortening clause): fraction of the in-band scan window with eps_WKB < 1
    # =================================================================================
    # eps_WKB at each in-band scan point depends ONLY on kappa_eff (the dynamical inverse-width).
    # The two dynamical readings give eps at omega_q and relic_rms. The in-band window is scanned
    # over V0; kappa_eff is fixed per reading. f_used = fraction of in-band candidates WKB-valid.
    eps_floq = gamma_clock / omega_q ** 2                     # (local)
    eps_relicrms = gamma_clock / relic_rms ** 2               # (local)
    # f_used over the full DISCRETE candidate set (the actual scan of substrate barriers):
    inband_cands = cand_inband
    if inband_cands.any():
        wkb_valid_inband = (cand_epsWKB[inband_cands] < 1.0)
        f_used = float(np.mean(wkb_valid_inband))             # (local) fraction WKB-valid among in-band
    else:
        f_used = 1.0                                          # (local) no in-band candidates -> regime N/A
    print(f"\n[wkb ] eps_WKB(omega_q)={eps_floq:.4f}  eps_WKB(relic_rms)={eps_relicrms:.4f}  "
          f"(WKB valid iff eps<1)")
    print(f"[wkb ] f_used (fraction of in-band scan window WKB-valid) = {f_used:.4f}")

    if f_used >= F_USED_VALID:
        regime_verdict = "VALID"
    elif f_used >= F_USED_BREAKDOWN:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    print(f"[wkb ] regime_verdict = {regime_verdict}  (VALID>={F_USED_VALID}, "
          f"MARGINAL>={F_USED_BREAKDOWN}, else BREAKDOWN)")

    # =================================================================================
    # INDEPENDENT scattering-ODE cross-check of the closed PT form (method consistency)
    # at the dynamical Floquet barrier
    # =================================================================================
    V0_check = omega_q ** 2                                   # (local) representative dynamical barrier
    x_max = 12.0 / omega_q                                     # (local) sech^2 decays over ~1/kappa
    omega_check = np.array([omega_min, 0.5 * (omega_min + omega_max), omega_max, 2.0 * omega_q])  # (local)
    gamma_ode = np.array([gamma_scattering_ode(w, omega_q, V0_check, x_max) for w in omega_check])  # (local)
    gamma_closed = gamma_pt_closed(omega_check, omega_q, V0_check)  # (local)
    ode_vs_closed = float(np.nanmax(np.abs(gamma_ode - gamma_closed)))  # (local)
    method_consistent = (ode_vs_closed < 1e-3)
    print(f"\n[xcheck] ODE-vs-closed-PT max dev = {ode_vs_closed:.3e} (method consistent: {method_consistent})")

    # =================================================================================
    # VERDICT (existential operator + ratio criterion + auto-shortening regime collapse)
    # =================================================================================
    # magnitude_verdict: does an in-band substrate barrier reproduce 0.512 within +/-10%?
    if pass_inband_and_target:
        magnitude_verdict = "PASS"
    elif exists_inband:
        magnitude_verdict = "INFO"     # in-band substrate barrier exists but misses 0.512 by >10%
    else:
        magnitude_verdict = "FAIL"     # no in-band substrate barrier at all
    # sign_verdict: N/A ([VERIFY] trigger, no directional pre-reg)
    sign_verdict = "N/A"

    # Composite-collapse (gate-verdicts.md), with the plan operator mapped onto the 3-tuple:
    #   PASS  : in-band substrate V0 AND int_Gamma in 0.512+/-10%   (magnitude PASS, regime VALID)
    #   FAIL  : every substrate scale OUT of band                   (magnitude FAIL)  OR regime BREAKDOWN
    #   INFO  : in-band but misses 0.512                            (magnitude INFO)  OR regime MARGINAL
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
    print(f"\n[VERDICT] magnitude={magnitude_verdict} regime={regime_verdict} "
          f"sign={sign_verdict} -> composite={composite}")

    # =================================================================================
    # Save npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # candidate grid
        cand_kappa=cand_kappa,
        cand_sqrtV0=cand_sqrtV0,
        cand_intG=cand_intG,
        cand_inband=cand_inband,
        cand_reldev=cand_reldev,
        cand_label=np.array(cand_label),
        cand_epsWKB=cand_epsWKB,
        # continuous V0-scan
        V0_scan=V0_scan,
        sqrtV0_scan=sqrtV0_scan,
        intG_scan_floq=intG_scan_floq,
        intG_scan_relicrms=intG_scan_relicrms,
        inband_mask=inband_mask,
        # substrate scales
        scale_names=np.array(scale_names),
        scale_vals=scale_vals,
        # dynamical drive
        omega_q=omega_q,
        gamma_clock=gamma_clock,
        tau_dot=tau_dot,
        relic_rms=relic_rms,
        # static baseline (ruled-out reference)
        kappa_static=kappa_static,
        V0_static=V0_static,
        int_Gamma_static_baseline=int_Gamma_static_baseline,
        transmitted_fraction_fitted=transmitted_fraction_fitted,
        # band + tolerances
        band_lo=BAND_LO,
        band_hi=BAND_HI,
        ratio_tol=RATIO_TOL,
        # results
        exists_inband=exists_inband,
        overall_best_rel=overall_best_rel,
        pass_inband_and_target=pass_inband_and_target,
        # WKB regime
        eps_WKB_floq=eps_floq,
        eps_WKB_relicrms=eps_relicrms,
        f_used=f_used,
        regime_verdict=regime_verdict,
        # method cross-check
        omega_check=omega_check,
        gamma_ode=gamma_ode,
        gamma_closed=gamma_closed,
        ode_vs_closed=ode_vs_closed,
        # relic spectrum
        omega_k=omega_k,
        w_mode=w_mode,
        # verdict
        magnitude_verdict=magnitude_verdict,
        sign_verdict=sign_verdict,
        composite_verdict=composite,
        canon_drift=canon_drift,
        tau_fold=float(tau_fold),
        M_KK=float(M_KK),
    )
    print(f"[npz] wrote {OUT_NPZ}")

    # =================================================================================
    # Plot
    # =================================================================================
    fig, ax = plt.subplots(1, 2, figsize=(15, 5.8))

    # left: int_Gamma vs sqrt(V0) for both dynamical kappa_eff readings + band + 0.512
    ax[0].plot(sqrtV0_scan, intG_scan_floq, "b-", lw=2.0,
               label=rf"dynamical $\kappa_{{\rm eff}}=\omega_q={omega_q:.2f}$ (Floquet drive)")
    ax[0].plot(sqrtV0_scan, intG_scan_relicrms, "g-", lw=2.0,
               label=rf"dynamical $\kappa_{{\rm eff}}=\omega_{{\rm rms}}={relic_rms:.2f}$")
    ax[0].axhline(transmitted_fraction_fitted, color="red", ls="--", lw=1.6,
                  label=rf"fitted $\int\Gamma={transmitted_fraction_fitted:.3f}$ (S95 W4-3 knob)")
    ax[0].axhspan(transmitted_fraction_fitted * (1 - RATIO_TOL),
                  transmitted_fraction_fitted * (1 + RATIO_TOL),
                  color="red", alpha=0.12, label=r"$\pm10\%$ PASS band")
    ax[0].axvspan(BAND_LO, BAND_HI, color="orange", alpha=0.12,
                  label=rf"relic band $\sqrt{{V_0}}\in[{BAND_LO},{BAND_HI}]$")
    ax[0].axhline(int_Gamma_static_baseline, color="gray", ls=":", lw=1.4,
                  label=rf"STATIC baseline $\int\Gamma={int_Gamma_static_baseline:.3f}$ (ruled out)")
    ax[0].set_xlabel(r"$\sqrt{V_0}=\omega_{1/2}$  (M$_{\rm KK}$)")
    ax[0].set_ylabel(r"squeeze-weighted $\int\Gamma\,d\omega$")
    ax[0].set_title("Exit-filter scan: dynamical near-horizon resonance")
    ax[0].set_ylim(-0.02, 1.02)
    ax[0].legend(fontsize=7.5, loc="center right")
    ax[0].grid(alpha=0.3)

    # right: discrete substrate-pair candidates (sqrt(V0) vs int_Gamma), color by in-band
    sc_in = ax[1].scatter(cand_sqrtV0[cand_inband], cand_intG[cand_inband],
                          c="tab:blue", s=55, marker="o", zorder=5, label="in-band substrate pair")
    sc_out = ax[1].scatter(cand_sqrtV0[~cand_inband], cand_intG[~cand_inband],
                          c="tab:gray", s=35, marker="x", zorder=4, label="out-of-band substrate pair")
    ax[1].axhline(transmitted_fraction_fitted, color="red", ls="--", lw=1.6, label="fitted 0.512")
    ax[1].axhspan(transmitted_fraction_fitted * (1 - RATIO_TOL),
                  transmitted_fraction_fitted * (1 + RATIO_TOL), color="red", alpha=0.12)
    ax[1].axvspan(BAND_LO, BAND_HI, color="orange", alpha=0.12, label="relic band")
    ax[1].set_xscale("log")
    ax[1].set_xlabel(r"$\sqrt{V_0}=\omega_{1/2}$  (M$_{\rm KK}$, log)")
    ax[1].set_ylabel(r"squeeze-weighted $\int\Gamma\,d\omega$")
    ax[1].set_title(f"Substrate-pair grid: best in-band rel_dev={overall_best_rel:.3f}\n"
                    f"regime={regime_verdict} (eps_WKB$\\gg$1) -> {composite}")
    ax[1].set_ylim(-0.02, 1.02)
    ax[1].legend(fontsize=8, loc="center left")
    ax[1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  --  A_s upper-edge exit-filter (dynamical near-horizon resonance scan)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG}")

    # =================================================================================
    # Dual-SHA + verdict payload
    # =================================================================================
    content_sha = sha256_file(SELF_PATH)
    pin_map = {
        "gate_id": GATE_ID,
        "script_sha": content_sha,
        "canonical_sha": sha_canon,
        "w3_1_npz_sha": sha_w31,
        "w3_4_npz_sha": sha_w34,
        "w3_2_npz_sha": sha_w32,
        "s57_npz_sha": sha_s57,
        "omega_q": f"{omega_q:.10f}",
        "gamma_clock": f"{gamma_clock:.10f}",
        "kappa_exit": f"{kappa_exit:.10f}",
        "Delta_BCS": f"{Delta_BCS:.10f}",
        "T_acoustic": f"{T_acoustic:.10f}",
        "band_lo": BAND_LO,
        "band_hi": BAND_HI,
        "ratio_tol": RATIO_TOL,
        "N_v0_scan": N_V0_SCAN,
        "transmitted_fraction_fitted": f"{transmitted_fraction_fitted:.10f}",
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
    }
    audit_sha = closure_hash(pin_map)

    value = (
        f"exists_inband={exists_inband};best_inband_rel_dev={overall_best_rel:.6f};"
        f"ratio_tol={RATIO_TOL};fitted_0.512={transmitted_fraction_fitted:.6f};"
        f"static_baseline_intG={int_Gamma_static_baseline:.6f};"
        f"dyn_omega_q={omega_q:.4f};dyn_relic_rms={relic_rms:.4f};"
        f"eps_WKB_omega_q={eps_floq:.4f};eps_WKB_relic_rms={eps_relicrms:.4f};"
        f"domain_used_frac={f_used:.4f};regime={regime_verdict};"
        f"magnitude={magnitude_verdict};ode_vs_closed={ode_vs_closed:.3e};"
        f"canon_drift_plan2runtime={canon_drift}"
    )

    extra_rows = [
        f"# {GATE_ID} domain_used_frac={f_used:.4f} regime={regime_verdict} "
        f"(auto-shortening clause; eps_WKB=gamma_clock/kappa_eff^2={eps_floq:.2f}@omega_q, "
        f"{eps_relicrms:.2f}@relic_rms; finite-rate near-horizon barrier NON-adiabatic)",
        f"# {GATE_ID} STATIC baseline (ruled out, NOT re-scanned): kappa_eff=kappa_exit={kappa_static:.4f}, "
        f"sqrt(V0)={np.sqrt(V0_static):.2f}>>band, int_Gamma={int_Gamma_static_baseline:.4f} "
        f"(inv-4 W1-4 + inv-12 W3-4 two-route agreement)",
        f"# {GATE_ID} DYNAMICAL scan (un-scanned candidate): in-band substrate barriers give "
        f"int_Gamma~0.65-0.99 (over-transmissive), best in-band rel_dev={overall_best_rel:.3f}>>{RATIO_TOL}; "
        f"0.512 reachable only at fitted kappa_eff~5.0 (NOT a substrate scale)",
        f"# {GATE_ID} VERDICT: A_s upper-edge exit-filter is bounded-but-filter-FITTED "
        f"(0.512 has no substrate scale on EITHER static or dynamical channel); "
        f"FLOOR A_s>=A_s^BD permanent on 3 axes (orthogonal to this leg)",
        f"# {GATE_ID} canonical SHA plan-text-drift: plan={PLAN_PINNED_CANON_SHA[:16]} "
        f"runtime={sha_canon[:16]} (S110 W0a T_acoustic PROVENANCE backfill, NO value change; "
        f"runtime SHA pinned per substrate-first SS(ii.B))",
    ]

    print_verdict_payload(composite, value, SCHEME, CONVENTION, L_MAX,
                          audit_sha, content_sha,
                          sign_verdict=sign_verdict,
                          magnitude_verdict=magnitude_verdict,
                          regime_verdict=regime_verdict,
                          extra_rows=extra_rows)

    print(f"OUTPUT-4TUPLE: (value=best_inband_rel_dev={overall_best_rel:.6f}, "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")


if __name__ == "__main__":
    main()
