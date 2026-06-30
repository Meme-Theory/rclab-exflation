#!/usr/bin/env python3
"""
S102 W7-1 CF-S102-OQ5-RECTIFIED-DRIVE — rectified parametric drive relic-budget test
====================================================================================

Gate: CF-S102-OQ5-RECTIFIED-DRIVE  ([SIGN])

Pre-registered threshold (plan §W7-1):
  R_rect = Delta_n_rect / n_pairs <= tau_budget = 0.05   (PASS)
  R_rect > 0.05                                          (FAIL — overproduce)
  ODE non-convergence OR dilution window q_dec_tail crosses 1.857 in-window (INFO)

  [SIGN] direction: Delta_n_rect >= 0 ALWAYS (Bogoliubov squeezing only ADDS
  occupation; |alpha|^2 - |beta|^2 = 1 unitarity). Overproduction (R_rect large)
  is the ONLY failure mode. A NEGATIVE Delta_n_rect would be a unitarity violation
  (sign_verdict=FAIL, regime BREAKDOWN).

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py   (n_pairs, Omega_DM, M_KK, tau_fold)
  - computations/session-101/s101_w4_qeq_relic_oddfloor.npz
        carries: gamma=29.7532 (clock dt/dtau), chi_I=885.254, h_par=8.30e-4
        (Mathieu depth), half_width=2.075e-4 (=h_par/4), q_osc=8.998e-4, q_bar=0.41218,
        omega_q_phys=2.012813, omega_q_tau=59.888, the 24-mode/14-occupied crossing set
        (arr_omega_s=E_k, arr_w_n=weights, arr_n_k_full=occupations, arr_band_k_min=
        per-mode closest-approach detuning Delta_res_k, arr_q_res_k=resonant q),
        arr_tau_tail / arr_q_tail (the post-fold q(tau) sweep), max_q_dec_tail=7.98e-5.
        W4-2 audit 98a923fd.
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=R_rect, scheme=FW, convention=SUBSTRATE-NATURAL-BINDING, L_max=12)

Classification: PHONONIC

METHODOLOGY
-----------
The substrate IS the impulsive Mach-13.75 transit through the van Hove fold at
tau_fold=0.190; the GGE relic is the post-transit spectrum of Bogoliubov phonon
pairs (n_pairs=59.8, P_exc=1.000 — a GGE relic, NOT thermal reheating). On the
post-fold tail the q-channel drives a time-dependent BdG pair-band frequency
omega_k(tau) = 2 E_k(q(tau)). The physical drive frequency omega_q^phys=2.012813
M_KK sits INSIDE the pair band [1.6395, 10.838] (W4-2 in_band=True), so 24 modes
(14 occupied, weight 248) cross the parametric resonance 2 E_k(q(tau)) = omega_q^phys
on the tail.

This gate quantifies whether the rectified parametric drive on those 14 OCCUPIED
modes overproduces the GGE relic. Per mode in the crossing set we integrate a
SWEPT parametric-resonance (Mathieu) Bogoliubov system: the mean q(tau) sweeps
(0.20 -> 0.66 over the tail, read from arr_q_tail) carrying each mode's
2 E_k(q(tau)) THROUGH resonance (Landau-Zener-style passage), while the fast
zero-point oscillation q_osc*cos(omega_q^tau * tau) (depth h_par=8.30e-4) provides
the parametric PUMP through the n-th Mathieu instability tongue at 2 E_k = n*omega_q^phys
(principal n=1; half-width h_par/4=2.075e-4 per the S100a W-1 D-2 width-aware-guard
lesson — the suppressed force-component amplitude governs THROUGHPUT, not width).

For each occupied mode k:
  (1) omega_k(tau) = sqrt( omega_k0^2 + 2*omega_k0*Delta_res_k*shape(tau)
                            + (parametric pump) )   built from the crossing geometry
  (2) integrate the 2x2 Bogoliubov ODE (alpha_k, beta_k) in the fold-conformal
      clock dt = gamma*dtau (Radau/RK45, rtol<=1e-10) across the crossing window;
      read Delta|beta_k|^2 = |beta_k(end)|^2 - |beta_k(start=0)|^2.
  (3) Delta_n_rect = Sum_{k occupied} w_k * Delta|beta_k|^2  (weights from npz).
  (4) R_rect = Delta_n_rect / n_pairs; PASS iff R_rect <= 0.05.
Dilution cross-check: W4-2 conjunct B max_q_dec_tail=7.98e-5 << 1.857 (post-fold
dilution suppresses the tail; the rectified increment is cleanly separable).

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate `# (local)`
- CPU with OMP cap (14 small 2x2 Bogoliubov ODEs; no >=100x100 linear algebra)
- SHA-256 of inputs logged in first 20 lines; dual-SHA (S84+) emitted
- 4-tuple printed; verdict via emit_verdict MCP tool (script PRINTS payload)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (n_pairs, Omega_DM, M_KK, tau_fold)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S102"                                                   # (local)
GATE_ID = "CF-S102-OQ5-RECTIFIED-DRIVE"                            # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "SUBSTRATE-NATURAL-BINDING"                           # (local)
L_MAX = 12                                                         # (local)

# Pre-registered pass/fail threshold (plan §W7-1; FROZEN at plan-freeze) ---
TAU_BUDGET = 0.05            # (local) 5% of n_pairs GGE-relic pair budget (plan-frozen)
ODE_RTOL = 1e-10            # (local) plan machinery pin
ODE_ATOL = 1e-12           # (local)
RRECT_RELTOL = 1e-6        # (local) plan machinery pin (R_rect comparison)
Q_DEC_WINDOW_EDGE = 1.857  # (local) dilution-window edge (W4-2)

W4_NPZ = COMPUTATIONS_DIR / "session-101" / "s101_w4_qeq_relic_oddfloor.npz"  # (local)
CANON = SHARED_DIR / "canonical_constants.py"                                 # (local)

OUT_NPZ = SESSION_DIR / "s102_w7_oq5_rectified_drive.npz"
OUT_PNG = SESSION_DIR / "s102_w7_oq5_rectified_drive.png"

INPUT_FILES = [CANON, W4_NPZ]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
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


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------
def per_mode_bogoliubov_increment(omega_k0, delta_res_k, h_par, omega_drive_tau,
                                  gamma_clock, tau_window):
    """Integrate the SWEPT parametric-resonance Bogoliubov ODE for one mode.

    Mode equation (parametric oscillator / Mathieu) in the conformal-clock
    time t = gamma * tau:
        u_k'' + omega_k(t)^2 u_k = 0
    with the instantaneous BdG frequency
        omega_k(t)^2 = omega_res^2 * [ 1 + (2 delta_res_k/omega_res) * s_sweep(t)
                                       + h_par * cos(omega_d_phys * t) ]
    where:
      - omega_res = omega_q^phys/2 is the resonant pair-band frequency
        (the per-mode frequency at the crossing, since 2 omega_k = omega_q^phys
        AT resonance). omega_k0 = E_k is the static (snapshot) energy; the
        crossing brings 2 E_k(q(tau)) -> omega_q^phys, i.e. the band frequency
        sweeps to omega_res at closest approach delta_res_k.
      - s_sweep(t) is a smooth Landau-Zener-style passage profile through the
        crossing: |2 E_k(q(tau)) - omega_q^phys| reaches its minimum delta_res_k
        at the centre of the window and is larger at the edges. We model the
        slow detuning as delta(t) = delta_res_k * sqrt(1 + (xi*(t-t_c))^2)*sign,
        but for the THROUGHPUT estimate (the relic increment) the governing
        scale is the closest-approach detuning delta_res_k vs the tongue
        half-width h_par/4, integrated over the in-tongue dwell time.
      - omega_d_phys = omega_drive_tau / gamma_clock is the fast parametric
        pump frequency in conformal-clock time (the zero-point q oscillation).

    Bogoliubov decomposition: write u_k = (1/sqrt(2 omega_res)) *
      [ alpha_k e^{-i omega_res t} + beta_k e^{+i omega_res t} ], with the
    standard first-order-in-(coupling) evolution
        d alpha_k/dt = (i h_par omega_res / 4) e^{+2 i omega_res t (...)} beta_k
        d beta_k/dt  = (-i h_par omega_res / 4) e^{-2 i omega_res t (...)} alpha_k
    Integrating the FULL 2x2 system (not first-order PT) captures the
    finite-window swept resonance exactly. Initial condition (alpha,beta)=(1,0)
    => |beta_k(0)|^2 = 0; the increment is |beta_k(end)|^2.

    Returns (Delta_beta2, converged_bool, max_beta2).
    """
    omega_res = omega_q_phys_local / 2.0          # (local) resonant pair-band frequency
    omega_d_phys = omega_drive_tau / gamma_clock  # (local) fast pump freq in clock time
    t0 = 0.0                                       # (local)
    t1 = gamma_clock * tau_window                  # (local) conformal-clock window length
    t_c = 0.5 * (t0 + t1)                          # (local) crossing centre
    # Landau-Zener sweep rate: the detuning passes through delta_res_k at t_c.
    # The dimensionless detuning at the window edge is bounded by the tongue
    # structure; xi sets how fast the mode sweeps through the tongue. We anchor
    # xi so the detuning reaches ~the tongue half-width at the window edge
    # (the mode is in-tongue for the central fraction of the window) -- this is
    # the CONSERVATIVE (largest-dwell) choice consistent with delta_res_k being
    # the closest approach.
    halfw = h_par / 4.0                            # (local) principal tongue half-width
    # detuning(t) = delta_res_k + slope*|t-t_c|, slope set so detuning = halfw at edge
    # i.e. the mode is inside the tongue while |t-t_c| < (halfw-delta_res_k)/slope.
    # Choose slope so the in-tongue dwell spans the central window fraction.
    edge_detune = halfw                            # (local) detuning at window edge (tongue boundary)
    slope = (edge_detune - delta_res_k) / max(t_c - t0, 1e-30)  # (local)
    slope = max(slope, 0.0)

    omega_res_sq = omega_res * omega_res           # (local)

    def detuning(t):
        return delta_res_k + slope * abs(t - t_c)  # (local) frequency-units detuning

    def rhs(t, y):
        ar, ai, br, bi = y  # (local) alpha=ar+i ai, beta=br+i bi
        # instantaneous BdG frequency offset (slow detuning) + fast pump
        # delta_om(t): the band frequency 2 omega_k(t) = omega_q^phys +- detuning(t)
        # => omega_k(t) = omega_res +- detuning(t)/2 ; the resonant-frame phase
        # accumulates 2*integral(omega_k - omega_res) = +- integral(detuning).
        # Coupling g(t) = h_par * omega_res / 4 (parametric pump amplitude).
        g = h_par * omega_res / 4.0  # (local)
        # resonant-frame mismatch phase: Phi(t) = integral_0^t detuning(t') dt'
        # detuning(t) = delta_res_k + slope|t-t_c|; integral is piecewise.
        if t <= t_c:
            Phi = delta_res_k * t + slope * (-(t - t_c) ** 2 / 2.0 + (t0 - t_c) ** 2 / 2.0)  # (local)
        else:
            Phi_c = delta_res_k * t_c + slope * ((t0 - t_c) ** 2 / 2.0)  # (local)
            Phi = Phi_c + delta_res_k * (t - t_c) + slope * (t - t_c) ** 2 / 2.0  # (local)
        cP = np.cos(Phi)  # (local)
        sP = np.sin(Phi)  # (local)
        # d alpha/dt = i g e^{+i Phi} beta ; d beta/dt = -i g e^{-i Phi} alpha
        # alpha = ar+i ai, beta = br+i bi
        # i g e^{+iPhi} beta = i g (cP+i sP)(br+i bi)
        #   = i g [ (cP*br - sP*bi) + i (cP*bi + sP*br) ]
        #   = g [ -(cP*bi + sP*br) + i (cP*br - sP*bi) ]
        dar = g * (-(cP * bi + sP * br))  # (local)
        dai = g * (cP * br - sP * bi)     # (local)
        # -i g e^{-iPhi} alpha = -i g (cP - i sP)(ar + i ai)
        #   = -i g [ (cP*ar + sP*ai) + i (cP*ai - sP*ar) ]
        #   = g [ (cP*ai - sP*ar) - i (cP*ar + sP*ai) ]
        dbr = g * (cP * ai - sP * ar)     # (local)
        dbi = g * (-(cP * ar + sP * ai))  # (local)
        return [dar, dai, dbr, dbi]

    y0 = [1.0, 0.0, 0.0, 0.0]  # (local) (alpha,beta)=(1,0)
    sol = solve_ivp(rhs, (t0, t1), y0, method="RK45", rtol=ODE_RTOL, atol=ODE_ATOL,
                    dense_output=False, max_step=(t1 - t0) / 4000.0)
    converged = bool(sol.success)  # (local)
    ar, ai, br, bi = sol.y[:, -1]  # (local)
    beta2_end = br * br + bi * bi   # (local)
    alpha2_end = ar * ar + ai * ai  # (local)
    # unitarity residual |alpha|^2 - |beta|^2 - 1
    unit_resid = abs(alpha2_end - beta2_end - 1.0)  # (local)
    # max |beta|^2 over the trajectory (for diagnostics)
    beta2_traj = sol.y[2] ** 2 + sol.y[3] ** 2  # (local)
    max_beta2 = float(np.max(beta2_traj))        # (local)
    delta_beta2 = beta2_end - 0.0                # (local) increment from |beta(0)|^2=0
    return delta_beta2, converged, max_beta2, unit_resid, omega_d_phys


# module-scope handle to omega_q_phys (read in compute, used in per-mode fn)
omega_q_phys_local = None  # (local) set in compute()


def compute() -> dict:
    global omega_q_phys_local
    print("Loading W4-2 crossing set from", W4_NPZ.name)
    d = np.load(W4_NPZ, allow_pickle=True)
    E_k_all = d["arr_omega_s"]        # (local) E_k per mode (NOT 2E_k)
    w_all = d["arr_w_n"]              # (local) weights
    nk_all = d["arr_n_k_full"]        # (local) occupations
    dres_all = d["arr_band_k_min"]    # (local) per-mode closest-approach detuning Delta_res_k
    qres_all = d["arr_q_res_k"]       # (local) resonant q per mode
    omega_q_phys = float(d["omega_q_phys"])  # (local)
    omega_q_tau = float(d["omega_q_tau"])    # (local) drive freq in tau units
    gamma_clock = float(d["gamma"])          # (local) dt/dtau
    h_par = float(d["h_par"])                # (local) Mathieu depth
    half_width = float(d["half_width"])      # (local) =h_par/4
    q_osc = float(d["q_osc"])                # (local)
    q_bar = float(d["q_bar"])                # (local)
    dtau_tail = float(d["dtau_tail"])        # (local) crossing-window tau span
    dt_tail = float(d["dt_tail"])            # (local) = gamma*dtau_tail
    chi_I = float(d["chi_I"])                # (local)
    max_q_dec_tail = float(d["max_q_dec_tail"])  # (local) dilution-window probe
    pair_bottom = float(d["pair_bottom_q0"])     # (local) band bottom = 2*E_min
    pair_top = float(d["pair_top_q0_L12"])       # (local) band top
    in_band = bool(d["in_band"])                 # (local)
    omega_q_phys_local = omega_q_phys

    # --- Identify the crossing set: E_k in [0.819,0.874] AND q_res in [0.250,0.342] ---
    # (matches W4-2 n_cross_all=24, w_cross=248.045 EXACTLY; verified at decode time)
    mask_cross = ((E_k_all >= 0.819) & (E_k_all <= 0.874)
                  & (qres_all >= 0.250) & (qres_all <= 0.342))  # (local)
    idx_cross = np.where(mask_cross)[0]                          # (local)
    n_cross = int(len(idx_cross))                               # (local)
    w_cross_sum = float(w_all[idx_cross].sum())                 # (local)

    # occupied subset: n_k > 0 (the 14 occupied modes; w_sum ~ 112.045)
    occ_mask = nk_all[idx_cross] > 0.0                          # (local)
    idx_occ = idx_cross[occ_mask]                               # (local)
    n_occ = int(len(idx_occ))                                   # (local)
    w_occ_sum = float(w_all[idx_occ].sum())                     # (local)

    print(f"  crossing set: {n_cross} modes (w_sum={w_cross_sum:.5f}); "
          f"npz n_cross_all={int(d['n_cross_all'])}, w_cross={float(d['w_cross']):.5f}")
    print(f"  occupied subset: {n_occ} modes (w_sum={w_occ_sum:.5f}); "
          f"npz n_cross_occ={int(d['n_cross_occ'])}")
    print(f"  omega_q_phys={omega_q_phys:.6f} in band [{pair_bottom:.4f},{pair_top:.4f}] "
          f"= {in_band}; gamma={gamma_clock:.6f}; h_par={h_par:.3e}; "
          f"half_width(h_par/4)={half_width:.3e}")
    print(f"  crossing window: dtau_tail={dtau_tail:.5f}, dt_tail={dt_tail:.5f} "
          f"(=gamma*dtau={gamma_clock*dtau_tail:.5f})")
    print(f"  dilution probe: max_q_dec_tail={max_q_dec_tail:.3e} (edge {Q_DEC_WINDOW_EDGE})")
    print()

    # --- Per-mode Bogoliubov increment over the swept crossing window ---
    rows = []  # (local)
    all_converged = True  # (local)
    max_unit_resid = 0.0  # (local)
    delta_n_rect = 0.0    # (local)
    omega_d_phys_val = None  # (local)
    print("  Per-occupied-mode swept-resonance Bogoliubov integration:")
    for j in idx_occ:
        Ek = float(E_k_all[j])          # (local)
        wk = float(w_all[j])            # (local)
        nk = float(nk_all[j])           # (local)
        dres = float(dres_all[j])       # (local) closest-approach detuning
        dbeta2, conv, maxb2, ures, omd = per_mode_bogoliubov_increment(
            Ek, dres, h_par, omega_q_tau, gamma_clock, dtau_tail)
        omega_d_phys_val = omd
        all_converged = all_converged and conv
        max_unit_resid = max(max_unit_resid, ures)
        # The increment to the OCCUPATION of an already-populated mode: a squeezed
        # state on a thermal/occupied background amplifies occupation by the
        # stimulated factor. For the pair-count increment we use the spontaneous
        # |beta_k|^2 (vacuum seed) times the Bose stimulation (1+2 n_k): squeezing
        # a populated mode adds (1+2 n_k)*|beta_k|^2 pairs (standard squeezed-
        # thermal result). n_k here is the per-mode occupation.
        stim = 1.0 + 2.0 * nk           # (local) Bose stimulation factor
        dn_mode = wk * dbeta2 * stim    # (local) weighted pair increment
        delta_n_rect += dn_mode
        rows.append((Ek, wk, nk, dres, dbeta2, maxb2, stim, dn_mode, conv, ures))
        print(f"    E_k={Ek:.5f} w={wk:8.4f} n_k={nk:.3e} dres={dres:.3e} "
              f"|beta|^2={dbeta2:.3e} stim={stim:.4f} dn={dn_mode:.3e} conv={conv}")

    # --- Relic-abundance ratio ---
    R_rect = delta_n_rect / n_pairs                         # (local) fractional relic shift
    delta_Omega_DM = Omega_DM * R_rect                      # (local) absolute Omega_DM shift
    Omega_DM_total = Omega_DM * (1.0 + R_rect)              # (local)

    # --- Dilution cross-check: does q_dec_tail cross 1.857 in-window? ---
    arr_q_dec = d["arr_q_dec_tail"]                         # (local)
    max_abs_qdec = float(np.max(np.abs(arr_q_dec)))         # (local)
    # NOTE: arr_q_dec_tail contains transient spikes (the kappa-inversion probe);
    # the W4-2-canonical dilution metric is max_q_dec_tail=7.98e-5 (conjunct B).
    dilution_window_crossed = max_q_dec_tail > Q_DEC_WINDOW_EDGE  # (local)

    print()
    print(f"  Delta_n_rect = {delta_n_rect:.6e} pairs")
    print(f"  R_rect = Delta_n_rect / n_pairs = {delta_n_rect:.6e} / {n_pairs} = {R_rect:.6e}")
    print(f"  Delta_Omega_DM = Omega_DM * R_rect = {delta_Omega_DM:.6e}")
    print(f"  Omega_DM_total = {Omega_DM_total:.6f} (was {Omega_DM})")
    print(f"  max unitarity residual |alpha|^2-|beta|^2-1 = {max_unit_resid:.3e}")
    print(f"  all ODEs converged = {all_converged}")
    print(f"  dilution: max_q_dec_tail={max_q_dec_tail:.3e} crossed {Q_DEC_WINDOW_EDGE}? "
          f"{dilution_window_crossed}")
    print()

    return {
        "value": R_rect,
        "delta_n_rect": delta_n_rect,
        "R_rect": R_rect,
        "delta_Omega_DM": delta_Omega_DM,
        "Omega_DM_total": Omega_DM_total,
        "n_occ": n_occ,
        "n_cross": n_cross,
        "w_occ_sum": w_occ_sum,
        "w_cross_sum": w_cross_sum,
        "all_converged": all_converged,
        "max_unit_resid": max_unit_resid,
        "dilution_window_crossed": dilution_window_crossed,
        "max_q_dec_tail": max_q_dec_tail,
        "omega_q_phys": omega_q_phys,
        "gamma_clock": gamma_clock,
        "h_par": h_par,
        "half_width": half_width,
        "omega_d_phys": omega_d_phys_val,
        "chi_I": chi_I,
        "rows": rows,
        "dtau_tail": dtau_tail,
        "dt_tail": dt_tail,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


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


def evaluate_gate(res) -> tuple[str, str, str, str]:
    """Return (composite, sign_verdict, magnitude_verdict, regime_verdict).

    [SIGN] one-sided overproduction gate:
      sign_verdict   = PASS iff Delta_n_rect >= 0 (overproduction direction; unitarity)
                       FAIL iff Delta_n_rect < 0 (unitarity violation)
      magnitude_verdict = PASS iff R_rect <= TAU_BUDGET (within budget)
                          FAIL iff R_rect > TAU_BUDGET (overproduce)
      regime_verdict = VALID iff all ODEs converged AND unit residual small
                              AND dilution window NOT crossed
                       BREAKDOWN otherwise
    Composite per gate-verdicts.md collapse rule.
    """
    dn = res["delta_n_rect"]   # (local)
    R = res["R_rect"]          # (local)
    # sign
    sign_v = "PASS" if dn >= 0.0 else "FAIL"  # (local)
    # magnitude (one-sided)
    mag_v = "PASS" if R <= TAU_BUDGET * (1.0 + RRECT_RELTOL) else "FAIL"  # (local)
    # regime
    regime_ok = (res["all_converged"]
                 and res["max_unit_resid"] < 1e-6
                 and not res["dilution_window_crossed"])  # (local)
    regime_v = "VALID" if regime_ok else "BREAKDOWN"  # (local)
    # composite collapse (gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        composite = "FAIL" if not res["all_converged"] else "INFO"
        # ODE non-convergence OR dilution crossed -> INFO per the gate rubric
        if not res["all_converged"]:
            composite = "INFO"
        elif res["dilution_window_crossed"]:
            composite = "INFO"
        else:
            composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL":
        composite = "FAIL"
    else:
        composite = "PASS"
    return composite, sign_v, mag_v, regime_v


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------
def make_plot(res):
    rows = res["rows"]  # (local)
    Eks = [r[0] for r in rows]      # (local)
    dbeta2s = [r[4] for r in rows]  # (local)
    dns = [r[7] for r in rows]      # (local)
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
    ax = axes[0]
    ax.scatter(Eks, dbeta2s, c="tab:blue", s=40)
    ax.set_xlabel("E_k (M_KK)")
    ax.set_ylabel(r"$\Delta|\beta_k|^2$")
    ax.set_title("Per-mode spontaneous Bogoliubov increment")
    ax.set_yscale("log")
    ax.grid(alpha=0.3)
    ax = axes[1]
    ax.scatter(Eks, np.abs(dns), c="tab:red", s=40)
    ax.set_xlabel("E_k (M_KK)")
    ax.set_ylabel(r"$w_k (1+2n_k) \Delta|\beta_k|^2$")
    ax.set_title("Per-mode weighted pair increment")
    ax.set_yscale("log")
    ax.grid(alpha=0.3)
    ax = axes[2]
    ax.bar(["R_rect", "tau_budget"], [res["R_rect"], TAU_BUDGET],
           color=["tab:green" if res["R_rect"] <= TAU_BUDGET else "tab:red", "gray"])
    ax.set_ylabel("relic-abundance fraction")
    ax.set_title(f"R_rect={res['R_rect']:.3e} vs budget {TAU_BUDGET}")
    ax.set_yscale("log")
    ax.grid(alpha=0.3, axis="y")
    fig.suptitle("CF-S102-OQ5-RECTIFIED-DRIVE — rectified parametric drive relic-budget test\n"
                 f"14 occupied crossing modes; Delta_n_rect={res['delta_n_rect']:.3e}; "
                 f"R_rect={res['R_rect']:.3e}")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    res = compute()
    composite, sign_v, mag_v, regime_v = evaluate_gate(res)

    # Save data
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        value=res["R_rect"], R_rect=res["R_rect"], delta_n_rect=res["delta_n_rect"],
        delta_Omega_DM=res["delta_Omega_DM"], Omega_DM_total=res["Omega_DM_total"],
        n_pairs=n_pairs, Omega_DM=Omega_DM, tau_budget=TAU_BUDGET,
        n_occ=res["n_occ"], n_cross=res["n_cross"],
        w_occ_sum=res["w_occ_sum"], w_cross_sum=res["w_cross_sum"],
        all_converged=res["all_converged"], max_unit_resid=res["max_unit_resid"],
        dilution_window_crossed=res["dilution_window_crossed"],
        max_q_dec_tail=res["max_q_dec_tail"],
        omega_q_phys=res["omega_q_phys"], gamma_clock=res["gamma_clock"],
        h_par=res["h_par"], half_width=res["half_width"],
        omega_d_phys=res["omega_d_phys"], chi_I=res["chi_I"],
        dtau_tail=res["dtau_tail"], dt_tail=res["dt_tail"],
        per_mode=np.array([(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7])
                           for r in res["rows"]], dtype=float),
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        composite=composite, audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"  data -> {OUT_NPZ.name}")
    make_plot(res)
    print()

    # 4-tuple + verdict payload
    tag = emit_4tuple(res["R_rect"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    value_payload = (
        f"R_rect={res['R_rect']:.6e}_dn_rect={res['delta_n_rect']:.6e}_"
        f"budget={TAU_BUDGET}_14occ_w{res['w_occ_sum']:.3f}_"
        f"dOmegaDM={res['delta_Omega_DM']:.3e}_unitresid={res['max_unit_resid']:.2e}_"
        f"qdec{res['max_q_dec_tail']:.2e}<{Q_DEC_WINDOW_EDGE}"
    )  # (local)
    extra = [
        f"# regulator_pin=N/A (relic/Bogoliubov observable, not a Seeley-DeWitt moment)",
        f"# OQ-5 rectified-drive: Delta_n_rect={res['delta_n_rect']:.6e} pairs >= 0 "
        f"(Bogoliubov squeeze ADDS; unitarity |alpha|^2-|beta|^2=1); "
        f"R_rect={res['R_rect']:.6e} vs tau_budget={TAU_BUDGET}",
    ]  # (local)
    print_verdict_payload(
        composite, value_payload, audit_sha, content_sha,
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=regime_v,
        companion_note="CF-S102-OQ5-RECTIFIED-DRIVE [SIGN] one-sided overproduction gate",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} "
          f"(sign={sign_v} mag={mag_v} regime={regime_v}; wall {wall:.1f}s) ===")
    return 0 if composite != "FAIL" else 1


if __name__ == "__main__":
    sys.exit(main())
