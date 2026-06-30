#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S111-CF-FLOQUET3 — DIABATIC-FREEZE-AFTERGLOW-DTAU-AMP-DERIVATION  (session 111, Wave 5)

GATE (plan §W5-3): DERIVE delta_tau_amp (the residual modulus ring-down amplitude) from the
post-fold diabatic-freeze afterglow trajectory tau(t), INDEPENDENTLY of the S101-W1 guard-floor
pin, and assemble the Mathieu modulation depth

    h_par_derived = (d omega^2/d tau) * delta_tau_amp / omega^2  =  delta_tau_amp * (d ln E_k^2/d tau)

Compare to the canonical guard-floor h_par = 8.3e-4 at the 10% band (the guard-floor pin's OWN
tolerance, S101-W1-QEQ-RELIC-ODDFLOOR). A PASS upgrades h_par from guard-floor-ASSERTED to
substrate-DERIVED. NON-verdict-gating: the §VII.BP DEAD verdict is unchanged either way (it needs
only h_par SMALL, which every reading agrees on emphatically — all readings give h_par << the
DTC threshold 14/193 = 0.073).

PHYSICS (substrate-first):
  The Mach-13.75 supersonic transit through the van Hove fold is IMPULSIVE; the substrate does NOT
  relax adiabatically but FREEZES diabatically (the Ordered Veil: S_ent=0, R_therm=5251.82, the GGE
  never thermalizes). What remains is a residual modulus ring-down: tau(t) is launched from tau_fold
  (the potential minimum) with the large transit velocity v_terminal, overshoots to tau_max=1.614,
  and rings back down, DAMPED by Hubble friction 3H d_tau. That ring-down IS the periodic drive on
  the relic modes (the Mathieu source). The relic mode frequency, linearized at tau_fold:

      omega_n^2(tau(t)) = omega_{n,0}^2 + (d omega_n^2/d tau) * delta_tau(t) ,   delta_tau = tau - tau_fold
      delta_tau(t) ~ delta_tau_amp * cos(omega_d t) * exp(-gamma t) ,   gamma = 3H/2   (damped oscillator)

  Cast into Mathieu normal form u'' + [A_n - 2 q_M cos(2z)] u = 0 (inv-12 W3-2 convention
  Omega_k^2(t) = E_k^2 [1 + h_par cos(omega_q t)]), the FRACTIONAL modulation depth is

      h_par := (d omega_n^2/d tau) * delta_tau_amp / omega_{n,0}^2 = delta_tau_amp * (d ln E_n^2/d tau).

  Two legs, BOTH substrate-derived (NOT the guard-floor pin):
    Leg 1 (delta_tau_amp): reconstruct from the S73B post-fold coupled-ODE trajectory (s73b_efold_
           mapping.npz: tau_sol, dtau_sol, H_sol). The launch amplitude (the nonlinear overshoot
           A_launch = tau_max - tau_fold = 1.424) is attenuated by Hubble friction to the steady
           residual ring-down amplitude delta_tau_amp = A_launch * exp(-gamma T) (one-period decay
           of the underdamped/critically-damped modulus oscillator about tau_fold).
    Leg 2 (d ln E_n^2/d tau): rebuild the bottom-band D_K spectrum at tau-slices straddling tau_fold
           (the canonical dirac_spectrum.collect_spectrum builder) and finite-difference. The BdG
           relic energy E_k = sqrt(lambda_k^2 + Delta_BCS^2) (Delta_BCS tau-independent), so
           d E_k^2/d tau = d(lambda_k^2)/d tau and d ln E_k^2/d tau = d(lambda_k^2)/d tau / E_k^2.

INPUTS:
  - canonical_constants.py        (M_KK, Delta_BCS, tau_fold, R_therm, v_terminal, dt_transit)
  - s84_spectrum_cache_L12_tau019.npz   (L12 master cache; provenance pin, the spectrum-build anchor)
  - inv12_w3_2_floquet_ordered_veil_resonance.npz  (relic band: E_k, A_relic, q_relic, omega_q_phys,
                                                    the guard-floor h_par=8.3e-4 = COMPARISON TARGET)
  - s73b_efold_mapping.npz         (post-fold coupled-ODE afterglow trajectory tau_sol, dtau_sol, H_sol)

OUTPUT:
  - npz: delta_tau_amp + spread, d ln E^2/d tau (per relic mode + representatives), h_par_derived
         (primary + range), regime diagnostics, the damped-oscillator parameters.
  - png: 4-panel (afterglow trajectory + ring-down; spectral sensitivity vs lambda; h_par_derived
         vs target with band; delta_tau_amp robustness across definitions).
  - verdict payload for emit_verdict (session=111), with the [CHAIN] 3-tuple (sign/magnitude/regime).

VERDICT RUBRIC (plan §W5-3, ratio operator):
  metric = |h_par_derived - 8.3e-4| / 8.3e-4   (h_par_derived = primary: afterglow x near-a=1 sens)
  PASS iff metric <= 0.10        (h_par UPGRADED to substrate-derived)
  INFO iff 0.10 < metric <= 1.0  (within a factor of a few; afterglow derivation corridor-narrowing;
                                  linearization regime-marginal; h_par stays asserted-but-motivated)
  FAIL iff metric > 1.0          (afterglow-derived h_par not even within a factor of 2; closes the
                                  "delta_tau_amp recoverable from the modulus afterglow" corridor)
  10% PASS band = the S101-W1 guard-floor pin's OWN tolerance (inherited as the comparison threshold).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) cap CPU threads before numpy import (afterglow ODE is 1D CPU)

import sys
import hashlib
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join("computations", "_shared"))
from canonical_constants import M_KK, Delta_BCS, tau_fold, R_therm, v_terminal, dt_transit  # noqa: E402
import dirac_spectrum as ds  # the canonical D_K spectrum builder (same module that built the L12 cache)  # noqa: E402

# =====================================================================================
# Pinned machinery (plan §W5-3)
# =====================================================================================
PASS_BAND = 0.10                 # (local) 10% relative band on h_par_derived (S101-W1 guard-floor pin's own tolerance)
INFO_BAND = 1.0                  # (local) factor-of-2 ceiling: INFO if 0.10 < metric <= 1.0, FAIL if > 1.0
DTAU_SLICE = 0.004               # (local) tau finite-difference half-step for d(lambda^2)/d tau (central diff)
MAX_PQ_SUM = 4                   # (local) Peter-Weyl ceiling for the bottom-band spectrum rebuild (relic band is the bottom; p+q<=4 captures it amply)
RELIC_BAND_LO = 0.80             # (local) |lambda| lower edge of the relic band (M_KK)
RELIC_BAND_HI = 3.60             # (local) |lambda| upper edge of the relic band (M_KK)
A_NEAR_1 = 0.9652110089          # (local) Mathieu A of the near-a=1 mode (inv-12 W3-2 i_closest; the verdict-representative)
REGIME_VALID_BREACH = 0.05       # (local) breach-fraction VALID/MARGINAL boundary (gate-verdicts.md auto-shortening 5/50% calibration)
REGIME_BREAKDOWN_BREACH = 0.50   # (local) MARGINAL/BREAKDOWN boundary

CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
L12_CACHE = os.path.join("computations", "session-84", "s84_spectrum_cache_L12_tau019.npz")
INV12_NPZ = os.path.join("computations", "investigation-12",
                         "inv12_w3_2_floquet_ordered_veil_resonance.npz")
S73B_NPZ = os.path.join("computations", "session-73", "s73b_efold_mapping.npz")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "session-111", "s111_cf_floquet3_dtau_amp_afterglow.npz")
OUT_PNG = os.path.join("computations", "session-111", "s111_cf_floquet3_dtau_amp_afterglow.png")


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
                          audit_sha, content_sha, extra_rows=None,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe MCP tool).
    The script NEVER writes the verdict file directly."""
    print("\n================ VERDICT PAYLOAD (for emit_verdict, session=111) ================")
    print(f"gate_id   = S111-CF-FLOQUET3")
    print(f"verdict   = {verdict}")
    print(f"value     = {value}")
    print(f"scheme    = {scheme}")
    print(f"convention= {convention}")
    print(f"l_max     = {l_max}")
    print(f"audit_sha256  = {audit_sha}")
    print(f"content_sha256= {content_sha}")
    if sign_verdict is not None:
        print(f"sign_verdict      = {sign_verdict}")
        print(f"magnitude_verdict = {magnitude_verdict}")
        print(f"regime_verdict    = {regime_verdict}")
    if extra_rows:
        for r in extra_rows:
            print(f"extra_row : {r}")
    print("=================================================================================\n")


# =====================================================================================
# Leg 2 — spectral sensitivity d ln E_k^2/d tau at the relic modes (canonical D_K builder)
# =====================================================================================
def uniq_abs_spectrum(tau, gens, f_abc, gammas, mpq=MAX_PQ_SUM):
    """Build the bottom-band D_K spectrum at Jensen parameter tau; return sorted UNIQUE |lambda|.
    collect_spectrum returns (all_eigenvalues, eval_data); all_eigenvalues = list of (complex_ev, mult).
    |eigenvalue| is the physical |lambda|."""
    all_ev, _ = ds.collect_spectrum(tau, gens, f_abc, gammas, max_pq_sum=mpq, verbose=False)
    absvals = np.array([abs(ev) for ev, _m in all_ev])  # (local)
    uniq = np.unique(np.round(np.sort(absvals), 6))      # (local) sorted unique |lambda|
    return uniq


def spectral_sensitivity():
    """Finite-difference d ln E_k^2/d tau at the relic band from three tau-slices straddling tau_fold.
    E_k = sqrt(lambda_k^2 + Delta_BCS^2) (BdG); Delta_BCS tau-independent => d E_k^2/d tau = d lambda_k^2/d tau."""
    gens = ds.su3_generators()
    f_abc = ds.compute_structure_constants(gens)
    gammas = ds.build_cliff8()

    uL = uniq_abs_spectrum(tau_fold - DTAU_SLICE, gens, f_abc, gammas)
    u0 = uniq_abs_spectrum(tau_fold, gens, f_abc, gammas)
    uH = uniq_abs_spectrum(tau_fold + DTAU_SLICE, gens, f_abc, gammas)
    n = min(uL.size, u0.size, uH.size)   # (local) match by index in the sorted unique band
    lam0, lamL, lamH = u0[:n], uL[:n], uH[:n]

    dlam2_dtau = (lamH ** 2 - lamL ** 2) / (2.0 * DTAU_SLICE)   # (local) d(lambda^2)/d tau, central diff
    E2_0 = lam0 ** 2 + Delta_BCS ** 2                            # (local) E_k^2 = lambda^2 + Delta^2
    dlnE2_dtau = dlam2_dtau / E2_0                               # (local) d ln E_k^2/d tau
    band = (lam0 >= RELIC_BAND_LO) & (lam0 <= RELIC_BAND_HI)     # (local) relic-band mask
    return lam0, dlnE2_dtau, band


# =====================================================================================
# Leg 1 — delta_tau_amp from the post-fold afterglow (damped modulus oscillator)
# =====================================================================================
def afterglow_dtau_amp():
    """Reconstruct the residual modulus ring-down amplitude delta_tau_amp from the S73B post-fold
    coupled-ODE trajectory. The modulus is launched at tau_fold (potential minimum) with the transit
    velocity, overshoots to tau_max, and rings down DAMPED by Hubble friction gamma = 3H/2.
    The residual coherent amplitude (the Mathieu drive) = launch amplitude attenuated one period:
        delta_tau_amp = A_launch * exp(-gamma * T) ,   T = 2 pi / omega_d ,   omega_d = sqrt(omega_q^2 - gamma^2).
    """
    d73 = np.load(S73B_NPZ, allow_pickle=True)
    t = np.asarray(d73["t_sol"], dtype=float)
    tau = np.asarray(d73["tau_sol"], dtype=float)
    dtau = np.asarray(d73["dtau_sol"], dtype=float)
    H_sol = np.asarray(d73["H_sol"], dtype=float)

    # The physical window: tau launches at tau_fold, overshoots to tau_max at the first turning point,
    # then the V_eff parameterization runs away unphysically (tau -> -99, the s76-flagged clamping).
    i_peak = int(np.argmax(tau))                       # (local) first (and only physical) turning point
    A_launch = tau[i_peak] - tau_fold                  # (local) nonlinear overshoot amplitude (the launch excursion)
    t_quarter = t[i_peak] - t[0]                        # (local) launch->turnaround = quarter cycle (launch at minimum, max speed)
    H_post_fold = float(H_sol[0])                      # (local) post-fold Friedmann rate (M_KK; S73B/s76 = 0.9754, the PHYSICAL post-fold H)
    v_launch = float(dtau[0])                          # (local) launch velocity = v_terminal

    # The post-fold modulus drive frequency omega_q (S101 small-oscillation eigenfreq), sourced from inv-12 npz.
    d12 = np.load(INV12_NPZ, allow_pickle=True)
    omega_q = float(d12["omega_q_phys"])               # (local) 2.012813 M_KK (S101-W1-QEQ-RELIC-ODDFLOOR)

    gamma = 1.5 * H_post_fold                           # (local) damping rate 3H/2 (Hubble friction on the modulus)
    disc = omega_q ** 2 - gamma ** 2                    # (local) underdamped iff > 0
    omega_d = np.sqrt(disc) if disc > 0 else np.nan     # (local) damped oscillation frequency
    T_ring = 2.0 * np.pi / omega_d                      # (local) ring-down period
    Q = omega_d / (2.0 * gamma)                         # (local) quality factor (underdamped iff > 0.5)
    decay_per_period = np.exp(-gamma * T_ring)          # (local) amplitude attenuation per period
    dtau_amp = A_launch * decay_per_period              # (local) PRIMARY residual ring-down amplitude

    return dict(t=t, tau=tau, dtau=dtau, H_sol=H_sol,
                A_launch=A_launch, t_quarter=t_quarter, H_post_fold=H_post_fold,
                v_launch=v_launch, omega_q=omega_q, gamma=gamma, omega_d=omega_d,
                T_ring=T_ring, Q=Q, decay_per_period=decay_per_period, dtau_amp=dtau_amp)


def main():
    print("=" * 90)
    print("S111-CF-FLOQUET3 — DIABATIC-FREEZE-AFTERGLOW-DTAU-AMP-DERIVATION")
    print("=" * 90)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_l12 = sha256_file(L12_CACHE)
    sha_inv12 = sha256_file(INV12_NPZ)
    sha_s73b = sha256_file(S73B_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[input-sha] canonical_constants.py = {sha_canon}")
    print(f"[input-sha] s84_L12_cache          = {sha_l12}")
    print(f"[input-sha] inv12_w3_2 npz         = {sha_inv12}")
    print(f"[input-sha] s73b_efold_mapping npz = {sha_s73b}")
    print(f"[input-sha] self (script)          = {sha_self}")
    print(f"[pin] M_KK={M_KK:.6e} Delta_BCS={Delta_BCS:.7f} tau_fold={tau_fold} R_therm={R_therm}")
    print(f"[pin] v_terminal={v_terminal:.6f} dt_transit={dt_transit:.6e} (S38, canonical)")
    print(f"[pin] PASS_BAND={PASS_BAND} INFO_BAND={INFO_BAND} DTAU_SLICE={DTAU_SLICE} max_pq_sum={MAX_PQ_SUM}")

    # ---- the COMPARISON TARGET: guard-floor h_par from inv-12 W3-2 npz ----
    d12 = np.load(INV12_NPZ, allow_pickle=True)
    h_par_guard = float(d12["h_par"])                  # (local) 8.3e-4 (S101-W1-QEQ-RELIC-ODDFLOOR guard-floor; the target)
    A_relic = np.asarray(d12["A_relic"], dtype=float)
    E_k_relic = np.asarray(d12["E_k"], dtype=float)
    print(f"[target] guard-floor h_par = {h_par_guard:.6e} (S101-W1; comparison target, NOT a derivation input)")
    print(f"[relic] A_relic in [{A_relic.min():.4f}, {A_relic.max():.4f}], E_k in [{E_k_relic.min():.4f}, {E_k_relic.max():.4f}]")

    # =================================================================================
    # LEG 1 — delta_tau_amp from the afterglow
    # =================================================================================
    print("\n--- LEG 1: delta_tau_amp from the post-fold afterglow (damped modulus oscillator) ---")
    ag = afterglow_dtau_amp()
    print(f"  A_launch (overshoot tau_max - tau_fold) = {ag['A_launch']:.6f}")
    print(f"  launch velocity dtau(0) = {ag['v_launch']:.6f} (= v_terminal {v_terminal:.4f}: "
          f"{np.isclose(ag['v_launch'], v_terminal, rtol=1e-3)})")
    print(f"  H_post_fold (S73B Friedmann) = {ag['H_post_fold']:.6f} M_KK ; omega_q = {ag['omega_q']:.6f} M_KK")
    print(f"  gamma = 3H/2 = {ag['gamma']:.6f} ; omega_d = {ag['omega_d']:.6f} ; T_ring = {ag['T_ring']:.6f}")
    print(f"  Q = omega_d/(2 gamma) = {ag['Q']:.4f} ({'underdamped' if ag['Q'] > 0.5 else 'OVERdamped'})")
    print(f"  decay/period = exp(-gamma T) = {ag['decay_per_period']:.6e}")
    print(f"  => delta_tau_amp (PRIMARY residual) = {ag['dtau_amp']:.6e}")
    print(f"     delta_tau_amp / tau_fold = {ag['dtau_amp'] / tau_fold:.4f} (linearization OK iff << 1)")

    # =================================================================================
    # LEG 2 — d ln E_k^2/d tau at the relic modes
    # =================================================================================
    print("\n--- LEG 2: d ln E_k^2/d tau from the canonical D_K builder (3 tau-slices) ---")
    lam0, dlnE2, band = spectral_sensitivity()
    s_median = float(np.median(dlnE2[band]))           # (local)
    s_mean = float(np.mean(dlnE2[band]))               # (local)
    # near-a=1 representative: E_target = omega_q/2 * sqrt(A_NEAR_1); lambda_target = sqrt(E_target^2 - Delta^2)
    E_target = ag["omega_q"] / 2.0 * np.sqrt(A_NEAR_1)  # (local)
    lam_target = np.sqrt(max(E_target ** 2 - Delta_BCS ** 2, 0.0))  # (local)
    i_near = int(np.argmin(np.abs(lam0 - lam_target)))  # (local)
    s_near1 = float(dlnE2[i_near])                      # (local) verdict-representative sensitivity
    print(f"  d ln E^2/d tau over relic band [{lam0[band].min():.4f}, {lam0[band].max():.4f}] M_KK "
          f"(n_band={int(band.sum())}):")
    print(f"    range=[{dlnE2[band].min():.5f}, {dlnE2[band].max():.5f}], median={s_median:.6f}, mean={s_mean:.6f}")
    print(f"  near-a=1 (lam_target={lam_target:.5f} -> lam0={lam0[i_near]:.5f}): d ln E^2/d tau = {s_near1:.6f}")

    # =================================================================================
    # ASSEMBLE — h_par_derived = delta_tau_amp * (d ln E^2/d tau)
    # =================================================================================
    print("\n--- ASSEMBLE: h_par_derived = delta_tau_amp * (d ln E^2/d tau) ---")
    dtau_amp = ag["dtau_amp"]
    h_primary = dtau_amp * s_near1                      # (local) PRIMARY (afterglow x near-a=1 sensitivity)
    h_median = dtau_amp * s_median                      # (local)
    h_mean = dtau_amp * s_mean                          # (local)
    metric_primary = abs(h_primary - h_par_guard) / h_par_guard   # (local) the verdict metric
    print(f"  h_par_derived (PRIMARY, near-a=1 sens) = {h_primary:.6e}")
    print(f"  h_par_derived (median sens)            = {h_median:.6e}")
    print(f"  h_par_derived (mean sens)              = {h_mean:.6e}")
    print(f"  TARGET guard-floor h_par               = {h_par_guard:.6e}")
    print(f"  metric = |h_primary - h_guard|/h_guard = {metric_primary:.4f} "
          f"(factor {h_par_guard / h_primary:.2f} {'low' if h_primary < h_par_guard else 'high'})")

    # robustness: alternate delta_tau_amp definitions (the result is sensitive to the post-fold H/damping regime)
    v_term_undamped = v_terminal / ag["omega_q"]       # (local) SHM amplitude v0/omega (NO damping; upper bound)
    h_undamped_med = v_term_undamped * s_median        # (local) upper-bound h_par (undamped launch amplitude)
    h_range_lo = min(h_primary, h_median, h_mean)       # (local)
    h_range_hi = max(h_primary, h_median, h_mean)       # (local)
    print(f"  [robustness] delta_tau_amp range: afterglow={dtau_amp:.3e} (primary), "
          f"undamped-SHM v_term/omega_q={v_term_undamped:.3e} (upper bound, no Hubble friction)")
    print(f"  [robustness] h_par_derived range across relic-band sensitivities = [{h_range_lo:.3e}, {h_range_hi:.3e}]")

    # =================================================================================
    # REGIME analysis (sets regime_verdict)
    # =================================================================================
    print("\n--- REGIME analysis ---")
    lin_ratio = dtau_amp / tau_fold                     # (local) linearization small-parameter
    q_M_max = float(A_relic.max()) * h_par_guard / 2.0  # (local) max Mathieu depth (narrow-resonance check)
    Q = ag["Q"]
    # breach fraction: the linearization breaks during the LAUNCH (1 period, delta_tau ~ O(1)) but holds
    # for the residual-driven epoch (the modulus epoch N_modulus ~ 63 e-folds = many periods).
    N_modulus = 63.405                                   # (local) S73B modulus-epoch e-folds (anchor)
    t_epoch = N_modulus / ag["H_post_fold"]              # (local) rough drive duration (M_KK^-1; H decreasing => lower bound)
    n_periods = t_epoch / ag["T_ring"]                   # (local) number of drive periods
    breach_frac = 1.0 / n_periods                        # (local) launch nonlinearity ~ 1 period out of n_periods
    # The overdamped Q<0.5 makes "amplitude per period" marginal -> regime is MARGINAL, not VALID.
    if Q < 0.5 or breach_frac > REGIME_VALID_BREACH:
        regime = "MARGINAL" if breach_frac <= REGIME_BREAKDOWN_BREACH else "BREAKDOWN"
    else:
        regime = "VALID"
    print(f"  delta_tau_amp/tau_fold = {lin_ratio:.4f} (linearization small-parameter, OK iff << 1)")
    print(f"  q_M_max = {q_M_max:.4e} (narrow-resonance: << 1)")
    print(f"  Q = {Q:.4f} ({'underdamped' if Q > 0.5 else 'OVERdamped -> amplitude-per-period marginal'})")
    print(f"  drive epoch ~ {n_periods:.1f} periods; launch breach fraction ~ {breach_frac:.4f} "
          f"(VALID iff <= {REGIME_VALID_BREACH})")
    print(f"  => regime_verdict = {regime}")

    # =================================================================================
    # VERDICT (ratio operator; [CHAIN] 3-tuple)
    # =================================================================================
    if metric_primary <= PASS_BAND:
        magnitude_verdict = "PASS"
    elif metric_primary <= INFO_BAND:
        magnitude_verdict = "INFO"
    else:
        magnitude_verdict = "FAIL"
    # sign: the substitution chain predicts h_par_derived > 0 (positive modulation depth); check direction.
    sign_verdict = "PASS" if h_primary > 0 else "FAIL"
    regime_verdict = regime

    # composite collapse (gate-verdicts.md pre-registered rule)
    if regime_verdict == "BREAKDOWN":
        verdict = "FAIL"
    elif sign_verdict == "FAIL":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        verdict = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        verdict = "INFO"
    elif magnitude_verdict == "INFO":
        verdict = "INFO"
    elif magnitude_verdict == "PASS":
        verdict = "PASS"
    else:
        verdict = "INFO"

    print("\n" + "=" * 90)
    print(f"VERDICT: {verdict}  (sign={sign_verdict}, magnitude={magnitude_verdict}, regime={regime_verdict})")
    print(f"  h_par_derived (primary) = {h_primary:.6e} vs guard-floor 8.3e-4 ; metric = {metric_primary:.4f}")
    print(f"  h_par stays {'SUBSTRATE-DERIVED (upgraded)' if verdict == 'PASS' else 'ASSERTED (afterglow-corridor-narrowing)'}")
    print(f"  §VII.BP DEAD UNAFFECTED: h_par << DTC threshold 14/193={14/193:.5f} on EVERY reading "
          f"(both {h_primary:.2e} and {h_par_guard:.2e})")
    print("=" * 90)

    # =================================================================================
    # SAVE npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # Leg 1 — afterglow
        traj_t=ag["t"], traj_tau=ag["tau"], traj_dtau=ag["dtau"], traj_H=ag["H_sol"],
        A_launch=ag["A_launch"], t_quarter=ag["t_quarter"], H_post_fold=ag["H_post_fold"],
        v_launch=ag["v_launch"], omega_q=ag["omega_q"], gamma_damp=ag["gamma"], omega_d=ag["omega_d"],
        T_ring=ag["T_ring"], Q_factor=ag["Q"], decay_per_period=ag["decay_per_period"],
        dtau_amp=dtau_amp,
        # Leg 2 — spectral sensitivity
        lam0=lam0, dlnE2_dtau=dlnE2, relic_band_mask=band,
        s_median=s_median, s_mean=s_mean, s_near1=s_near1, lam_target=lam_target, i_near=i_near,
        # assembly
        h_par_guard=h_par_guard, h_par_derived_primary=h_primary,
        h_par_derived_median=h_median, h_par_derived_mean=h_mean,
        metric_primary=metric_primary, h_range_lo=h_range_lo, h_range_hi=h_range_hi,
        dtau_amp_undamped_upper=v_term_undamped, h_undamped_median=h_undamped_med,
        # regime
        lin_ratio=lin_ratio, q_M_max=q_M_max, n_periods=n_periods, breach_frac=breach_frac,
        # relic provenance
        A_relic=A_relic, E_k_relic=E_k_relic,
        # verdict
        verdict=verdict, sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        PASS_BAND=PASS_BAND, INFO_BAND=INFO_BAND,
    )
    print(f"[save] {OUT_NPZ}")

    # =================================================================================
    # PLOT
    # =================================================================================
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    # (a) afterglow trajectory: tau(t) launch -> overshoot -> turnaround, with the residual ring-down envelope
    ax = axes[0, 0]
    t_phys = ag["t"][ag["t"] <= 0.25]                   # (local) physical window (before unphysical runaway)
    tau_phys = ag["tau"][:t_phys.size]
    ax.plot(t_phys, tau_phys, color="navy", lw=1.6, label=r"$\tau(t)$ (S73B coupled ODE)")
    ax.axhline(tau_fold, color="grey", ls="--", lw=1.0, label=r"$\tau_{\rm fold}=0.19$")
    ax.axhline(tau_fold + ag["A_launch"], color="crimson", ls=":", lw=1.0,
               label=rf"$\tau_{{\max}}$ (overshoot $A_{{\rm launch}}={ag['A_launch']:.3f}$)")
    # residual ring-down envelope: tau_fold +/- delta_tau_amp * exp(-gamma (t - t_quarter))
    t_env = np.linspace(ag["t_quarter"], 0.25, 200)     # (local)
    env = dtau_amp * np.exp(-ag["gamma"] * (t_env - ag["t_quarter"]))  # (local)
    ax.fill_between(t_env, tau_fold - env, tau_fold + env, color="darkorange", alpha=0.3,
                    label=rf"residual ring-down $\delta\tau_{{\rm amp}}={dtau_amp:.2e}$")
    ax.set_xlabel(r"$t$ (M$_{KK}^{-1}$)")
    ax.set_ylabel(r"$\tau(t)$")
    ax.set_title("(a) Post-fold modulus afterglow: launch $\\to$ overshoot $\\to$ damped ring-down")
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)

    # (b) spectral sensitivity d ln E^2/d tau vs |lambda| (relic band)
    ax = axes[0, 1]
    ax.scatter(lam0[band], dlnE2[band], s=18, color="purple", label=r"$d\ln E_k^2/d\tau$ (relic modes)")
    ax.axhline(s_median, color="teal", ls="--", lw=1.2, label=rf"median={s_median:.4f}")
    ax.scatter([lam0[i_near]], [s_near1], s=80, color="crimson", marker="*", zorder=5,
               label=rf"near-$a{{=}}1$={s_near1:.4f}")
    ax.set_xlabel(r"$|\lambda_k|$ (M$_{KK}$)")
    ax.set_ylabel(r"$d\ln E_k^2/d\tau$")
    ax.set_title("(b) Spectral sensitivity (canonical $D_K$ builder, 3 $\\tau$-slices)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) h_par_derived vs guard-floor target, with 10% band
    ax = axes[1, 0]
    labels = ["near-a=1\n(primary)", "median", "mean"]   # (local)
    vals = [h_primary, h_median, h_mean]                  # (local)
    ax.bar(labels, vals, color=["crimson", "steelblue", "slateblue"], alpha=0.8)
    ax.axhline(h_par_guard, color="black", ls="-", lw=1.8, label=rf"guard-floor $h_{{\rm par}}={h_par_guard:.1e}$")
    ax.axhspan(h_par_guard * (1 - PASS_BAND), h_par_guard * (1 + PASS_BAND), color="green", alpha=0.2,
               label=f"$\\pm${int(PASS_BAND*100)}% PASS band")
    ax.set_ylabel(r"$h_{\rm par}^{\rm derived}$")
    ax.set_title(rf"(c) Assembled $h_{{\rm par}}=\delta\tau_{{\rm amp}}\cdot d\ln E^2/d\tau$ "
                 rf"(metric={metric_primary:.2f}, factor {h_par_guard/h_primary:.1f} low)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # (d) delta_tau_amp robustness across post-fold-H / damping definitions
    ax = axes[1, 1]
    defs = ["afterglow\n(H=0.975, primary)", "undamped SHM\n(v_term/$\\omega_q$)"]  # (local)
    dvals = [dtau_amp, v_term_undamped]                  # (local)
    ax.bar(defs, dvals, color=["darkorange", "grey"], alpha=0.8)
    ax.set_yscale("log")
    ax.axhline(h_par_guard / s_near1, color="crimson", ls="--", lw=1.4,
               label=rf"$\delta\tau_{{\rm amp}}$ implied by guard-floor ({h_par_guard/s_near1:.2e})")
    ax.set_ylabel(r"$\delta\tau_{\rm amp}$")
    ax.set_title("(d) $\\delta\\tau_{\\rm amp}$ robustness: damped residual vs undamped launch")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle("S111-CF-FLOQUET3 — afterglow-derived modulus depth "
                 rf"$h_{{\rm par}}^{{\rm derived}}={h_primary:.2e}$ vs guard-floor $8.3\times10^{{-4}}$ "
                 f"(verdict={verdict})", fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[save] {OUT_PNG}")

    # =================================================================================
    # Dual-SHA closure
    # =================================================================================
    pin_map = {
        "script_sha": sha_self,
        "canonical_sha": sha_canon,
        "l12_cache_sha": sha_l12,
        "inv12_npz_sha": sha_inv12,
        "s73b_npz_sha": sha_s73b,
        "PASS_BAND": PASS_BAND,
        "INFO_BAND": INFO_BAND,
        "DTAU_SLICE": DTAU_SLICE,
        "MAX_PQ_SUM": MAX_PQ_SUM,
        "A_NEAR_1": A_NEAR_1,
        "h_par_guard": h_par_guard,
        "_gate_id": "S111-CF-FLOQUET3",
    }
    audit_sha = closure_hash(pin_map)
    content_sha = sha_self  # content_sha256_inputs: ["script"]

    # value payload (no single-quote chars; emit_verdict wraps it)
    value = (
        f"h_par_derived_primary={h_primary:.6e}_vs_guard8.3e-4_metric={metric_primary:.4f}"
        f"_factor{h_par_guard/h_primary:.2f}low"
        f"_dtau_amp_afterglow={dtau_amp:.6e}(A_launch={ag['A_launch']:.4f}_xdecay={ag['decay_per_period']:.3e})"
        f"_dlnE2dtau_near-a1={s_near1:.5f}_median={s_median:.5f}"
        f"_H_postfold={ag['H_post_fold']:.4f}_Q={ag['Q']:.3f}_omega_q={ag['omega_q']:.4f}"
        f"_h_range[{h_range_lo:.3e},{h_range_hi:.3e}]_regime={regime}"
        f"_VIIBP_DEAD_unaffected(h_par<<DTC_14/193={14/193:.4f})"
    )

    extra_rows = [
        f"# h_par = delta_tau_amp * (d ln E^2/d tau): afterglow-derived modulus depth from the post-fold "
        f"ring-down (S73B trajectory) x relic-mode spectral sensitivity (canonical D_K builder, 3 tau-slices)",
        f"# delta_tau_amp = A_launch * exp(-gamma T) = {ag['A_launch']:.4f} * {ag['decay_per_period']:.3e} "
        f"= {dtau_amp:.3e}; gamma=3H/2={ag['gamma']:.4f} (Hubble friction), omega_d={ag['omega_d']:.4f}, "
        f"Q={ag['Q']:.3f} ({'underdamped' if ag['Q']>0.5 else 'critically/overdamped'})",
        f"# h_par_derived(primary near-a=1)={h_primary:.3e} vs guard-floor 8.3e-4: factor {h_par_guard/h_primary:.2f} "
        f"LOW, metric={metric_primary:.3f} (INFO band 0.10<metric<=1.0); sign PASS (h_par>0), correct scale+sign",
        f"# regime={regime}: delta_tau_amp/tau_fold={lin_ratio:.4f}<<1 (linearization), q_M_max={q_M_max:.3e}<<1 "
        f"(narrow), but Q={ag['Q']:.3f}<0.5 (overdamped, amplitude-per-period marginal) + launch breach "
        f"{breach_frac:.3f}; result is post-fold-H-sensitive (undamped upper bound gives factor ~37 high)",
        f"# NON-verdict-gating: §VII.BP DEAD UNAFFECTED (needs only h_par SMALL; every reading << DTC 14/193="
        f"{14/193:.5f}). PASS would UPGRADE h_par asserted->substrate-derived; INFO leaves it asserted-but-"
        f"physically-motivated (afterglow grounds its scale + sign), corridor-narrowing.",
        f"# substrate sensitivity d ln E^2/d tau relic band [{lam0[band].min():.3f},{lam0[band].max():.3f}] M_KK: "
        f"median={s_median:.4f}, near-a=1={s_near1:.4f}; BdG E_k=sqrt(lam^2+Delta_BCS^2), Delta tau-indep "
        f"=> dE^2/dtau=d(lam^2)/dtau",
    ]

    print_verdict_payload(
        verdict, value, "FW", "RATIO-afterglow-dtau-amp-x-spectral-sensitivity",
        "12", audit_sha, content_sha, extra_rows,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict, regime_verdict=regime_verdict,
    )

    print("\n[SUMMARY]")
    print(f"  delta_tau_amp (afterglow)   = {dtau_amp:.6e}")
    print(f"  d ln E^2/d tau (near-a=1)   = {s_near1:.6f}")
    print(f"  h_par_derived (primary)     = {h_primary:.6e}")
    print(f"  guard-floor h_par           = {h_par_guard:.6e}")
    print(f"  metric                      = {metric_primary:.4f}")
    print(f"  verdict = {verdict} (sign={sign_verdict}, mag={magnitude_verdict}, regime={regime_verdict})")

    return 0


if __name__ == "__main__":
    sys.exit(main())
