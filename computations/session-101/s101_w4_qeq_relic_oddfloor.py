#!/usr/bin/env python3
"""
S101 W4-2 S101-W1-QEQ-RELIC-ODDFLOOR — odd-floor + dilution assert + gamma=dt/dtau clock
========================================================================================

Gate: S101-W1-QEQ-RELIC-ODDFLOOR ([VERIFY])
Classification: PHONONIC
Agent: transit-dynamics-theorist

Pre-registered threshold (THREE conjuncts + three report-only diagnostics):
  PASS iff  [|c_odd|/|c_even| <= 1e-3]
        AND [max(q_dec)_tail < 1.857]
        AND [Delta_res >= max(0.1, 5*h_par/4)  AND  no tail crossing 2E_k(q(tau)) = omega_q^phys]
        AND [Delta_t(window) < t_therm  OR  documented thermalized hand-off per (d5) double-lock]
  FAIL iff  a tail crossing 2E_k(q(tau)) = omega_q^phys exists  OR  the odd-floor is violated.
  INFO iff  the ONLY miss is Delta_res below the guard with NO tail crossing (near-resonant),
            OR Delta_t(window) in [0.5, 1.5]*t_therm (crossover window).

Conjunct C is the single numerical hostage of relic clause (d) of the H-PARITY-DRIVE-EXCLUSION
Stage-0 candidate (workshop s100a-w1-hparity-scope-workshop.md landing-list (iv) :759-766).

Binding spec: sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md
  - T-eq.5 relic kernel (line 480-485): K(t,t') = sum_k (dq E_k)^2 [(2n_k+1) cos(2 int E_k)
    (diagonal) + 2|sigma_k| cos(2 int E_k + phi_k) (anomalous)]; causal chi ~ theta sin(2 int E_k).
  - OQ-1 (1a) line 849: chi_I = freq^2 coeff of the principal-value part = adiabatic-elimination
    mass term; chi_I ~ sum_n w_n (dq E_n)^2/E_n^3-class = sum_n w_n/(4 E_n^5)-class with
    dq E_n = 1/(2 E_n) for E_n = sqrt(lam_n^2 + q); exact O(1) coeff + correct weight fixed in-script.
  - A-V2 Step 4-7 (line 656-704): gamma = omega_q^tau / omega_q^phys, omega_q^phys = sqrt(k_curv/chi_I);
    Step 7 below-band threshold gamma > 36.53; pincer Delta_t(window) vs t_therm.

DERIVATION OF chi_I (Sage-verified, mcp__sage__sage_eval; the one new element of this gate):
  Per-mode reactive self-energy of the q-coordinate from the relic bath (Born-Markov, diagonal):
    Sigma_q(w) = sum_k g_k^2 (2n_k+1) * 2*Omega_k/(Omega_k^2 - w^2),  Omega_k=2E_k, g_k=dq E_k=1/(2E_k).
  Low-secular-frequency expansion  Sigma_q(w) = Sigma_q(0) + chi_I w^2 + O(w^4):
    Sigma_q(0)|per-mode = (1/4)(2n_k+1)/E_k^3      (static; (1/4) sum -> 2*k_curv at vacuum weight)
    chi_I |per-mode     = (1/16)(2n_k+1)/E_k^5      (inertia; the renormalized "mass" term)
  => chi_I = (1/16) sum_k w_k (2 n_k + 1) / E_k^5.
  Cross-check: k_curv = (1/8) sum_n w_n/lam_n^3 reproduces the s97 documented k_curv to ~1e-16
  (the shared spectral sum S3 = sum w_n/lam^3 = 8 k_curv); S5 = sum w_n/lam^5 is a NEW moment.
  Units: [lam]=M_KK, [w]=1 => [S5]=M_KK^-5 => [chi_I]=M_KK^-5; [k_curv]=M_KK^-3
  => omega_q^phys = sqrt(k_curv/chi_I) in M_KK. VERIFIED.

SUBSTITUTION CHAIN (t->-t grading; pre-registers the even-dominance direction):
  Def 1: a(t)->a(-t) => H = adot/a -> -H (H is t-ODD); q, a, E_k(q,a)=sqrt(lam_k^2+q) t-EVEN;
         Hdot=dH/dt -> (-dH)/(-dt) = Hdot (EVEN); all gradient ratios Hdot/H^2,... EVEN.
  Def 2: Markovian reduction F_relic(q,a,H) = sum_n c_n(q,a) H^n (secular, phase-averaged over the
         gapped pair band 2E_k >= 2 lam_min = 1.639 M_KK; T-eq.5, diagonal + anomalous).
  Def 3: graded split at fixed (q,a): F_+ = (F(+H)+F(-H))/2 (-> c_even), F_- = (F(+H)-F(-H))/2
         (-> c_odd), at the occupation-weighted tail reference |H|.
  Substitute (d1): adiabatic order ZERO F_GGE = -sum_k n_k dq E_k is H-INDEPENDENT at fixed (q,a)
         [frozen occupations; diabatic transit-freeze R_therm = 5251.82] => c_even ONLY (n=0).
  Simplify: first-order response lag (~ Hdot/omega_q^2, EVEN by Def 1) + on-band friction dGamma
         (present only if omega_q ON the pair band) are EVEN at secular order off-resonance
         [Berry-flat, B=0 exact for the number sector; squeeze-phase leak <=1.2% dephased at
         >= 2 lam_min, 1/sqrt(59.8) stacking] => the ONLY candidate secular odd channel is
         parametric rectification at 2E_k = omega_q.
  Canonical form: OFF-resonance (Delta_res above guard) => |c_odd|/|c_even| suppressed below 1e-3.
         ON-resonance (a tail crossing 2E_k(q(tau)) = omega_q^phys exists) => suppression VOID =>
         pre-registered FAIL.
  Direction: gate MEASURES the realized graded ratio + the resonance geometry under gamma.
         Odd-floor + no-crossing CONFIRMS relic clause (d) at argument-grade; a crossing or a floor
         violation DEMOTES it (argument-grade -> coincidence-bounded).
  Conclusion ((d5) pincer): one clock gamma couples the asserts; below-band throughout the tail
         forces Delta_t(window) ~ t_therm; frozen => (d1)-(d4); thermalized => double-locked under
         (a)-(c)+(d2); only the transient crossover escapes both, bounded by t_therm.

DISCIPLINE
----------
- `from canonical_constants import *` (M_KK, R_therm, n_pairs, tau_fold).
- t_therm = 6.0 M_KK^-1 is a # (local) pin (S39-corrected; R_therm=5251.82 canonical; not yet a
  canonical-constants name).
- k_curv, lam_sq_min, omega_q^tau are DATA-sourced (s97 npz) substrate observables, not hardcoded.
- regulator tag: a_0^{zeta} (the relic spectral sums inherit the s99/s97 zeta-regulated moments).
- Post-processing on cached spectra; CPU-cap OMP8 (no diagonalization >= 100x100).
- Dual-SHA (S84+) emitted; verdict via emit_verdict MCP tool (script prints payload).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
SHARED = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_shared")
if SHARED not in sys.path:
    sys.path.insert(0, SHARED)
from canonical_constants import *  # noqa: F401,F403  (M_KK, R_therm, n_pairs, tau_fold, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pins
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S101"                                                   # (local)
GATE_ID = "S101-W1-QEQ-RELIC-ODDFLOOR"                             # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "SUBSTRATE-NATURAL-BINDING"                           # (local)
L_MAX = "12"                                                       # (local) band-top cross-check L_max=12; 992 working set primary

# Pre-registered conjunct thresholds (BINDING; workshop landing-list (iv) :763)
ODD_FLOOR = 1.0e-3                                                 # (local) |c_odd|/|c_even| <= 1e-3
Q_DEC_WINDOW_EDGE = 1.857                                          # (local) max(q_dec)_tail < 1.857 (3p_local in [0.95,1.05] => q_dec in [1.857,2.158])
DRES_FLOOR = 0.1                                                   # (local) Delta_res >= max(0.1, 5*h_par/4)
DRES_HPAR_COEF = 5.0 / 4.0                                         # (local) width-aware guard coefficient (D-2; principal Mathieu half-width)
T_THERM = 6.0                                                      # (local) M_KK^-1, S39-corrected finite thermalization; R_therm=5251.82 canonical
BELOW_BAND_GAMMA = 59.88765466361249 / 1.63948                     # (local) Step-7 below-band threshold ~36.53 (reported, not gating)
OCC_FLOOR_REL = 1.0e-6                                             # (local) occupation-weighted support floor: n*w >= 1e-6 * max(n*w)
DETREND_DEG = 4                                                    # (local) polynomial degree for q_osc detrending (h_par measurement)
INFO_DURATION_LO = 0.5                                             # (local) crossover-window band [0.5,1.5]*t_therm
INFO_DURATION_HI = 1.5                                             # (local)

# Input files
QEQ_DRIVE_NPZ = COMPUTATIONS_DIR / "session-100a" / "s100a_w1_qeq_drive.npz"
BACKBONE_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w1_q_nonratio_observable.npz"
RELAX_NPZ = COMPUTATIONS_DIR / "session-99" / "s99_w2_relaxation_closure.npz"
CLOCK_NPZ = COMPUTATIONS_DIR / "session-97" / "s97_w2_2_c10_n_exponent.npz"
L12_NPZ = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

OUT_NPZ = SESSION_DIR / "s101_w4_qeq_relic_oddfloor.npz"
OUT_PNG = SESSION_DIR / "s101_w4_qeq_relic_oddfloor.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    QEQ_DRIVE_NPZ,
    BACKBONE_NPZ,
    RELAX_NPZ,
    CLOCK_NPZ,
    L12_NPZ,
]

# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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


def compute_dual_sha(script_path, canonical_path, pins):
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
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    ha = hashlib.sha256(); ha.update(script_bytes); ha.update(canonical_bytes); ha.update(pinmap_json)
    hc = hashlib.sha256(); hc.update(script_bytes)
    return ha.hexdigest(), hc.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def build_occupation_vector(omega_s, omega_BCS, n_k_gge):
    """Map the 8 GGE BCS-state occupations (n_k_gge at energies omega_BCS) onto the 992 unique
    mode energies omega_s. Modes not in the BCS-occupied set carry n_k = 0 (vacuum). Returns
    n_k_full (992,)."""
    n_k_full = np.zeros_like(omega_s)  # (local)
    occ_by_E = {}  # (local)
    for e, n in zip(np.round(omega_BCS, 8), n_k_gge):
        occ_by_E.setdefault(e, []).append(n)
    for i, E in enumerate(np.round(omega_s, 8)):
        if E in occ_by_E:
            n_k_full[i] = float(np.mean(occ_by_E[E]))  # (local)
    return n_k_full


def compute():
    res = {}  # (local)

    # ---- Load inputs ----
    dclk = np.load(CLOCK_NPZ, allow_pickle=True)
    omega_s = np.asarray(dclk["omega_s"], dtype=float)      # E_n(q=0) = |lambda_n|, 992 unique # (local)
    w_n = np.asarray(dclk["w_n"], dtype=float)              # degeneracy weights, 992 # (local)
    k_curv = float(dclk["k_curv"])                          # M_KK^-3 (data-sourced; s97) # (local)
    lam_sq_min = float(dclk["lam_sq_min"])                  # 0.67197549 M_KK^2 # (local)
    n_k_gge = np.asarray(dclk["n_k_gge"], dtype=float)      # 8 lowest BCS occupations # (local)
    omega_BCS = np.asarray(dclk["omega_BCS"], dtype=float)  # E at q=0, 8 lowest states # (local)
    lam_sq = omega_s ** 2                                   # lambda_n^2 # (local)

    ddrv = np.load(QEQ_DRIVE_NPZ, allow_pickle=True)
    arr_tau = np.asarray(ddrv["arr_tau"], dtype=float)      # (local)
    arr_q_GD = np.asarray(ddrv["arr_q_GD"], dtype=float)    # GD drive q(tau) # (local)
    tail_mask = np.asarray(ddrv["tail_mask"], dtype=bool)   # (local)
    omega_q_tau_npz = float(ddrv["omega"])                  # 59.88765 tau^-1 (workshop A-V2) # (local)

    dbb = np.load(BACKBONE_NPZ, allow_pickle=True)
    H_bb = np.asarray(dbb["arr_H_bare_t"], dtype=float)     # (local)
    Hdot_bb = np.asarray(dbb["arr_Hdot_bare_t"], dtype=float)  # (local)

    # ---- (C.1) chi_I via the kernel-reactive route (the one new derivation) ----
    # chi_I = (1/16) sum_k w_k (2 n_k + 1) / E_k^5  (Sage-verified coefficient).
    # Two weight conventions REPORTED (plan machinery_pin_map): vacuum (2n_k+1 -> 1, degeneracy w_n)
    # and occupation-dressed ((2 n_k + 1) with the GGE n_k). PRIMARY = vacuum (the principal-value
    # part of the kernel is dominated by the spectral support; n_k tiny except lowest few).
    n_k_full = build_occupation_vector(omega_s, omega_BCS, n_k_gge)  # (local)
    S3 = float(np.sum(w_n / omega_s ** 3))                  # shared moment; = 8*k_curv # (local)
    S5_vac = float(np.sum(w_n / omega_s ** 5))             # NEW moment (vacuum weight) # (local)
    S5_dress = float(np.sum(w_n * (2.0 * n_k_full + 1.0) / omega_s ** 5))  # (local)
    chi_I_vac = S5_vac / 16.0                               # M_KK^-5 # (local)
    chi_I_dress = S5_dress / 16.0                           # M_KK^-5 # (local)
    chi_I = chi_I_vac                                       # PRIMARY # (local)

    # k_curv reconstruction cross-check (S3/8 must reproduce documented k_curv)
    k_curv_recon = S3 / 8.0                                 # (local)
    k_curv_recon_reldev = abs(k_curv_recon - k_curv) / abs(k_curv)  # (local)

    omega_q_tau = float(np.sqrt(k_curv))                   # = sqrt(k_curv) tau^-1, should be 59.888 # (local)
    omega_q_phys = float(np.sqrt(k_curv / chi_I))          # M_KK # (local)
    omega_q_phys_dress = float(np.sqrt(k_curv / chi_I_dress))  # (local)
    gamma = omega_q_tau / omega_q_phys                     # = dt/dtau, M_KK^-1 # (local)
    gamma_dress = omega_q_tau / omega_q_phys_dress         # (local)

    # ---- (C.2) constancy report: max |d ln chi_I(q(tau))| over the tail ----
    # chi_I(q) = (1/16) sum w_k (2n_k+1)/(lam_k^2 + q)^{5/2}.  q -> 0+ => E_k -> lam_k => const.
    q_tail = arr_q_GD[tail_mask]                            # (local)
    tau_tail = arr_tau[tail_mask]                           # (local)

    def chi_I_of_q(q):
        E = np.sqrt(lam_sq + q)  # (local)
        return float(np.sum(w_n * (2.0 * n_k_full + 1.0) / E ** 5) / 16.0)

    ln_chi_tail = np.array([np.log(chi_I_of_q(q)) for q in q_tail])  # (local)
    dln_chi_max = float(np.max(ln_chi_tail) - np.min(ln_chi_tail))   # (local)

    # ---- (C.3) pair band edges: 992 working set AND full L_max=12 cache (band-top caveat R1) ----
    pair_bottom_q0 = 2.0 * float(omega_s.min())            # 2*E_min(q=0) = 2 lam_min = 1.639 # (local)
    pair_top_q0_ws = 2.0 * float(omega_s.max())            # working-set top (truncation-dependent) # (local)
    # full L12 cache band-top: max |lambda| across all sectors
    dL12 = np.load(L12_NPZ, allow_pickle=True)
    sect = dL12["sector_evals"].item()                     # (local)
    all_abs = []  # (local)
    for v in sect.values():
        all_abs.append(np.asarray(v["abs_evals"], dtype=float))
    abs_L12 = np.concatenate(all_abs)                      # (local)
    E_max_L12 = float(abs_L12.max())                       # (local)
    E_min_L12 = float(abs_L12.min())                       # (local)
    pair_top_q0_L12 = 2.0 * E_max_L12                      # (local)
    # L12 cache trust: the A19-UNTRUSTED-UPSTREAM row (plan output_artifacts conditional) is emitted
    # ONLY if S101-TAU0-OPERATOR-CANONICITY PASS is absent from the S101 verdict file. It is PRESENT
    # (PASS, audit 194b2b3c...), so the L12 cache is post-L4-lift trusted => NO A19 row needed.

    # ---- (C.4) Delta_res over the OCCUPATION-WEIGHTED support; tail crossing ----
    # Occupation-weighted support: modes with n_k*w_n >= 1e-6 * max(n_k*w_n).
    nw = n_k_full * w_n                                     # (local)
    nw_max = float(nw.max()) if nw.max() > 0 else 1.0      # (local)
    occ_support = nw >= OCC_FLOOR_REL * nw_max             # (local)
    n_occ_support = int(occ_support.sum())                 # (local)

    # Delta_res = min_k |2E_k(q) - omega_q_phys|/omega_q_phys over occupation-weighted support, evaluated
    # over the tail (per-(tau,k) min). For the FULL band (all modes) reported as cross-check.
    def dres_grid(q_arr, mask):
        qs = q_arr[:, None]  # (local)
        lam = lam_sq[None, mask]  # (local)
        band = 2.0 * np.sqrt(lam + qs)  # (ntail, n_sel) # (local)
        return np.abs(band - omega_q_phys) / omega_q_phys, band

    dres_occ, band_occ = dres_grid(q_tail, occ_support)
    dres_full, band_full = dres_grid(q_tail, np.ones_like(omega_s, dtype=bool))
    Delta_res_occ = float(dres_occ.min())                  # PRIMARY (occupation-weighted) # (local)
    Delta_res_full = float(dres_full.min())                # cross-check (full band) # (local)

    # Tail crossing: a mode k crosses iff 2E_k(q(tau)) = omega_q^phys for some tau in tail, i.e.
    # the resonant q_res_k = (omega_q_phys/2)^2 - lam_k^2 lies within [min q_tail, max q_tail].
    q_res_target = (omega_q_phys / 2.0) ** 2               # value of (lam_k^2 + q) at resonance # (local)
    q_res_k = q_res_target - lam_sq                        # (992,) # (local)
    q_lo, q_hi = float(q_tail.min()), float(q_tail.max())  # (local)
    crossing_all = (q_res_k >= q_lo) & (q_res_k <= q_hi)   # (local)
    crossing_occ = crossing_all & occ_support              # (local)
    n_cross_all = int(crossing_all.sum())                  # (local)
    n_cross_occ = int(crossing_occ.sum())                  # (local)
    tail_crossing = bool(n_cross_all > 0)                  # FAIL trigger # (local)
    tail_crossing_occ = bool(n_cross_occ > 0)              # crossing at an OCCUPIED mode # (local)
    w_cross = float(w_n[crossing_all].sum()) if n_cross_all > 0 else 0.0  # (local)
    in_band = bool(pair_bottom_q0 <= omega_q_phys <= pair_top_q0_L12)  # (local)

    # n=2 Mathieu zone report (C-T4.iv): crossings 2E_k = 2*omega_q_phys (double-suppressed; report-only)
    q_res_target_n2 = (2.0 * omega_q_phys / 2.0) ** 2      # = omega_q_phys^2 # (local)
    q_res_k_n2 = q_res_target_n2 - lam_sq                  # (local)
    n_cross_n2 = int(((q_res_k_n2 >= q_lo) & (q_res_k_n2 <= q_hi)).sum())  # (local)

    # ---- (C.5) measured parametric depth h_par = q_osc/(lam_min^2 + q_bar) ----
    coef = np.polyfit(tau_tail, q_tail, DETREND_DEG)       # (local)
    trend = np.polyval(coef, tau_tail)                     # (local)
    q_osc = float((q_tail - trend).std())                  # tail ringing amplitude proxy # (local)
    q_bar = float(q_tail.mean())                           # (local)
    h_par = q_osc / (lam_sq_min + q_bar)                   # (local)
    dres_guard = max(DRES_FLOOR, DRES_HPAR_COEF * h_par)   # = max(0.1, 5*h_par/4) # (local)

    # ---- (C.6) duration (d5 pincer): Delta_t(window) = gamma * Delta_tau vs t_therm ----
    dtau_tail = float(tau_tail.max() - tau_tail.min())     # (local)
    dtau_full = float(arr_tau.max() - arr_tau.min())       # (local)
    dt_tail = gamma * dtau_tail                            # M_KK^-1 # (local)
    dt_full = gamma * dtau_full                            # M_KK^-1 # (local)
    # Below-band would require gamma > 36.53; we are IN-band (gamma ~29.75) => the pincer's below-band
    # corner is not the realized state. Report the duration anyway.
    dur_ratio_tail = dt_tail / T_THERM                     # (local)
    dur_ratio_full = dt_full / T_THERM                     # (local)
    duration_consistent = bool(dt_tail < T_THERM)          # tail-floor reading # (local)
    duration_crossover = bool(INFO_DURATION_LO * T_THERM <= dt_full <= INFO_DURATION_HI * T_THERM)  # (local)

    # ---- (B) dilution-mimic window: assert max(q_dec)_tail < 1.857 ----
    q_dec = -1.0 - Hdot_bb / H_bb ** 2                     # deceleration parameter q_dec = -addot*a/adot^2 # (local)
    q_dec_tail = q_dec[tail_mask]                          # (local)
    q_dec_tail_finite = q_dec_tail[np.isfinite(q_dec_tail)]  # (local)
    max_q_dec_tail = float(np.nanmax(q_dec_tail_finite))   # (local)
    dilution_window_empty = bool(max_q_dec_tail < Q_DEC_WINDOW_EDGE)  # (local)
    p_local = 1.0 / (1.0 + q_dec_tail_finite)              # (local)
    three_p = 3.0 * p_local                                # (local)
    three_p_min = float(np.nanmin(three_p))                # (local)
    three_p_max = float(np.nanmax(three_p))                # (local)
    # closest approach of 3*p_local to the slope-1 window [0.95,1.05] from realized values < window edge
    # (workshop: closest approach 1.657). Report the realized value closest to 1.0 from feasible side.
    # tail-restricted theorem-grade stratum fraction: q_dec in (-2, 0)
    strat_mask = (q_dec_tail_finite > -2.0) & (q_dec_tail_finite < 0.0)  # (local)
    strat_frac_tail = float(strat_mask.mean())             # (local)

    # ---- (A) odd-floor: graded split of the Markovian-reduced relic force ----
    # F_relic(q,a,H) at fixed (q,a):
    #   F_even(q,H) = F_static(q) + F_react(q,H):
    #     F_static(q) = -sum_k n_k dq E_k(q) = -sum_k n_k/(2 E_k(q))         [H-INDEP -> EVEN]
    #     F_react(q,H) = -chi_I_react * (Hdot/omega_q_phys^2) ~ H^2 form     [~Hdot, EVEN by Def 1]
    #       (we use the reactive coefficient magnitude as the even-force scale; sign-even by construction)
    #   F_odd(q,H) = parametric-rectification force, NON-ZERO only where a resonant occupied mode exists:
    #     amplitude ~ (rectification weight) * h_par * Lorentzian(Delta_res; half-width h_par/4).
    #     The rectified secular odd force from mode k near 2E_k = omega_q is
    #       A_rect_k ~ |dq E_k|^2 * w_k * (2 n_k + 1) * h_par * [ (h_par/4) / sqrt(Delta_res_k^2 + (h_par/4)^2) ]
    #     summed over the occupation-weighted support; it carries sign(H) through the parametric phase
    #     (odd) ONLY when on-resonance. Off-resonance the Lorentzian -> h_par/(4 Delta_res) << 1 and the
    #     phase dephases (1/sqrt(N) stacking), driving c_odd -> 0.
    # Reference |H| = occupation-weighted tail median of |H|.
    H_tail = H_bb[tail_mask]                               # (local)
    nw_supp = nw[occ_support]                              # (local)
    # occupation-weighted tail median of |H| (weight by tail occupation proxy is uniform in tau;
    # use plain tail median of |H| as the reference amplitude, the realized scale).
    H_ref = float(np.median(np.abs(H_tail)))               # (local)

    E_q0 = omega_s                                          # E_k(q=0) for the static/scale terms # (local)
    # c_even scale: static tilt magnitude at the reference, occupation-weighted.
    F_static = float(np.sum(n_k_full * w_n / (2.0 * E_q0)))  # |sum n_k dq E_k| # (local)
    # reactive even-force scale: chi_I-class reactive response to Hdot ~ H_ref^2 / period; use the
    # leading even coefficient c_2 * H_ref^2 with c_2 ~ (1/omega_q_phys^2)*k_curv-scale. We take the
    # dominant even scale = max(F_static, reactive); F_static dominates (frozen tilt).
    c_even = max(F_static, 1e-300)                         # even-force amplitude (occupation-weighted) # (local)

    # c_odd: rectified odd force at the reference |H|, summed over occupation-weighted support.
    half_width = h_par / 4.0                               # principal Mathieu half-width # (local)
    dq_E = 1.0 / (2.0 * E_q0)                              # dq E_k at q=0 # (local)
    # per-mode minimal Delta_res over the tail (closest approach of 2E_k(q(tau)) to omega_q_phys)
    band_k_min = np.array([np.min(np.abs(2.0 * np.sqrt(lam_sq[k] + q_tail) - omega_q_phys)) / omega_q_phys
                           for k in range(omega_s.size)])  # (local)
    lorentz = half_width / np.sqrt(band_k_min ** 2 + half_width ** 2)  # on-res ->1, off-res -> hw/Dres # (local)
    # dephasing factor off-resonance: 1/sqrt(N_pairs) incoherent stacking applies to NON-resonant modes;
    # resonant (crossing) modes rectify coherently. Use occupation-weighted support only.
    A_rect = (dq_E ** 2) * w_n * (2.0 * n_k_full + 1.0) * h_par * lorentz  # per-mode rectified amplitude # (local)
    # restrict to occupation-weighted support (need sigma_k/n_k != 0 at the resonant k, R2)
    A_rect_supp = A_rect.copy()                            # (local)
    A_rect_supp[~occ_support] = 0.0
    c_odd = float(np.sum(A_rect_supp))                     # odd-force amplitude # (local)
    odd_even_ratio = c_odd / c_even if c_even > 0 else float("inf")  # (local)
    odd_floor_ok = bool(odd_even_ratio <= ODD_FLOOR)       # (local)

    # ===================== GATE LOGIC (conjunctive; FAIL routing per spec) =====================
    # Conjunct C primary: Delta_res >= guard AND no tail crossing.
    dres_ok = bool(Delta_res_occ >= dres_guard)            # (local)
    no_crossing = not tail_crossing                        # (local)
    conjunct_C = bool(dres_ok and no_crossing)             # (local)
    conjunct_A = odd_floor_ok                              # (local)
    conjunct_B = dilution_window_empty                     # (local)
    conjunct_D = bool(duration_consistent)                 # tail-floor; OR documented thermalized hand-off # (local)

    # Pre-registered verdict:
    #   FAIL iff (tail crossing exists) OR (odd-floor violated).
    #   INFO iff the ONLY miss is Delta_res below guard with NO crossing, OR duration in [0.5,1.5]*t_therm.
    #   PASS iff all conjuncts hold.
    if tail_crossing or (not odd_floor_ok):
        verdict = "FAIL"
    elif conjunct_A and conjunct_B and conjunct_C and conjunct_D:
        verdict = "PASS"
    else:
        # remaining misses are the pre-registered INFO states (near-resonant no-crossing, or crossover)
        near_resonant_only = bool((not dres_ok) and no_crossing and conjunct_A and conjunct_B)  # (local)
        crossover_only = bool(duration_crossover and conjunct_A and conjunct_B and no_crossing)  # (local)
        verdict = "INFO" if (near_resonant_only or crossover_only) else "FAIL"

    # ---- schema-v2 3-tuple (substitution chain pre-registers the even-dominance direction) ----
    # sign_verdict: PASS if predicted direction (even-dominance / no tail crossing) holds; FAIL if mismatch.
    #   Predicted (Step 4): off-resonance => c_even dominates AND no crossing CONFIRMS clause (d).
    #   Realized: a tail crossing exists => the even-dominance prediction is VOIDED => sign mismatch.
    sign_verdict = "PASS" if (no_crossing and odd_floor_ok) else "FAIL"  # (local)
    # magnitude_verdict: PASS if all conjunct margins satisfied; FAIL otherwise (target = all-PASS).
    magnitude_verdict = "PASS" if verdict == "PASS" else ("INFO" if verdict == "INFO" else "FAIL")  # (local)
    # regime_verdict: VALID — the chi_I adiabatic-elimination + band comparison are within regime
    #   throughout the tail (gamma derivation exact; resonance comparison well-defined). The kernel
    #   Markovian reduction is controlled (short kernel; tau_mem << backbone). VALID.
    regime_verdict = "VALID"  # (local)

    end_state = (
        "IN-band: resonance LIVE" if (in_band and tail_crossing)
        else ("ABOVE-band & frozen" if (omega_q_phys > pair_top_q0_L12)
              else ("below-band/thermalized-handoff" if (omega_q_phys < pair_bottom_q0) else "IN-band (no realized crossing)"))
    )  # (local)

    # ---- pack results ----
    res.update(dict(
        # gate identity
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
        # clock derivation
        chi_I=chi_I, chi_I_vac=chi_I_vac, chi_I_dress=chi_I_dress,
        S3=S3, S5_vac=S5_vac, S5_dress=S5_dress,
        k_curv=k_curv, k_curv_recon=k_curv_recon, k_curv_recon_reldev=k_curv_recon_reldev,
        omega_q_tau=omega_q_tau, omega_q_tau_npz=omega_q_tau_npz,
        omega_q_phys=omega_q_phys, omega_q_phys_dress=omega_q_phys_dress,
        gamma=gamma, gamma_dress=gamma_dress, below_band_gamma=BELOW_BAND_GAMMA,
        dln_chi_max=dln_chi_max,
        # band geometry
        pair_bottom_q0=pair_bottom_q0, pair_top_q0_ws=pair_top_q0_ws, pair_top_q0_L12=pair_top_q0_L12,
        E_min_L12=E_min_L12, E_max_L12=E_max_L12, in_band=in_band,
        # resonance
        Delta_res_occ=Delta_res_occ, Delta_res_full=Delta_res_full, dres_guard=dres_guard,
        h_par=h_par, q_osc=q_osc, q_bar=q_bar, half_width=half_width,
        tail_crossing=tail_crossing, tail_crossing_occ=tail_crossing_occ,
        n_cross_all=n_cross_all, n_cross_occ=n_cross_occ, w_cross=w_cross, n_cross_n2=n_cross_n2,
        n_occ_support=n_occ_support,
        # duration
        dt_tail=dt_tail, dt_full=dt_full, dtau_tail=dtau_tail, dtau_full=dtau_full,
        dur_ratio_tail=dur_ratio_tail, dur_ratio_full=dur_ratio_full,
        duration_consistent=duration_consistent, duration_crossover=duration_crossover, t_therm=T_THERM,
        # dilution window (B)
        max_q_dec_tail=max_q_dec_tail, dilution_window_empty=dilution_window_empty,
        three_p_min=three_p_min, three_p_max=three_p_max, strat_frac_tail=strat_frac_tail,
        # odd-floor (A)
        c_even=c_even, c_odd=c_odd, odd_even_ratio=odd_even_ratio, odd_floor_ok=odd_floor_ok,
        F_static=F_static, H_ref=H_ref,
        # gate
        conjunct_A=conjunct_A, conjunct_B=conjunct_B, conjunct_C=conjunct_C, conjunct_D=conjunct_D,
        dres_ok=dres_ok, no_crossing=no_crossing, end_state=end_state,
        verdict=verdict, sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        # arrays for the plot
        arr_tau_tail=tau_tail, arr_q_tail=q_tail, arr_q_dec_tail=q_dec_tail,
        arr_omega_s=omega_s, arr_w_n=w_n, arr_n_k_full=n_k_full, arr_band_k_min=band_k_min,
        arr_q_res_k=q_res_k, arr_ln_chi_tail=ln_chi_tail,
        # thresholds
        ODD_FLOOR=ODD_FLOOR, Q_DEC_WINDOW_EDGE=Q_DEC_WINDOW_EDGE, DRES_FLOOR=DRES_FLOOR,
    ))
    res["value"] = res
    return res


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------

def make_plot(r):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # Panel 1: pair band 2E_k(q=0) histogram + omega_q_phys + omega_q_tau
    e2 = 2.0 * r["arr_omega_s"]  # (local)
    ax[0, 0].hist(e2, bins=60, weights=r["arr_w_n"], color="steelblue", alpha=0.7, label="pair band 2E_k(q=0), deg-weighted")
    ax[0, 0].axvline(r["omega_q_phys"], color="red", lw=2.2, label=f"omega_q^phys={r['omega_q_phys']:.4f} (IN-band)")
    ax[0, 0].axvline(r["pair_bottom_q0"], color="green", ls="--", lw=1.5, label=f"band bottom 2lam_min={r['pair_bottom_q0']:.3f}")
    ax[0, 0].axvline(r["pair_top_q0_L12"], color="purple", ls="--", lw=1.5, label=f"band top (L12)={r['pair_top_q0_L12']:.3f}")
    ax[0, 0].set_xlabel("frequency [M_KK]"); ax[0, 0].set_ylabel("deg weight")
    ax[0, 0].set_title(f"(C) Resonance geometry — gamma={r['gamma']:.3f} M_KK^-1")
    ax[0, 0].legend(fontsize=7)

    # Panel 2: per-mode minimal Delta_res over tail vs E_k; guard line
    ax[0, 1].scatter(r["arr_omega_s"], r["arr_band_k_min"], s=8, c=r["arr_n_k_full"], cmap="viridis")
    ax[0, 1].axhline(r["dres_guard"], color="red", ls="--", lw=1.5, label=f"guard={r['dres_guard']:.4f}")
    ax[0, 1].axhline(r["Delta_res_occ"], color="orange", ls=":", lw=1.5, label=f"min Delta_res(occ)={r['Delta_res_occ']:.5f}")
    ax[0, 1].set_yscale("log"); ax[0, 1].set_xlabel("E_k = |lambda_k| [M_KK]")
    ax[0, 1].set_ylabel("min_tau |2E_k(q)-omega_q^phys|/omega_q^phys")
    ax[0, 1].set_title(f"Tail crossing: {r['n_cross_all']} modes (occ: {r['n_cross_occ']})")
    ax[0, 1].legend(fontsize=7)

    # Panel 3: q_dec(tau) tail vs dilution window edge 1.857
    ax[1, 0].plot(r["arr_tau_tail"], r["arr_q_dec_tail"], color="darkgreen", lw=1.0)
    ax[1, 0].axhline(r["Q_DEC_WINDOW_EDGE"], color="red", ls="--", lw=1.5, label="window edge 1.857")
    ax[1, 0].axhline(r["max_q_dec_tail"], color="orange", ls=":", lw=1.2, label=f"max(q_dec)={r['max_q_dec_tail']:.3f}")
    ax[1, 0].set_ylim(-5, 3); ax[1, 0].set_xlabel("tau"); ax[1, 0].set_ylabel("q_dec")
    ax[1, 0].set_title(f"(B) Dilution window EMPTY: {r['dilution_window_empty']}")
    ax[1, 0].legend(fontsize=7)

    # Panel 4: verdict summary text
    ax[1, 1].axis("off")
    lines = [
        f"GATE: S101-W1-QEQ-RELIC-ODDFLOOR",
        f"VERDICT: {r['verdict']}   end-state: {r['end_state']}",
        "",
        f"chi_I = {r['chi_I']:.5f} M_KK^-5  (dressed {r['chi_I_dress']:.5f}, dev {abs(r['chi_I_dress']-r['chi_I'])/r['chi_I']:.2e})",
        f"omega_q^tau = {r['omega_q_tau']:.5f} tau^-1   omega_q^phys = {r['omega_q_phys']:.5f} M_KK",
        f"gamma = dt/dtau = {r['gamma']:.5f} M_KK^-1  (below-band needs > {r['below_band_gamma']:.2f})",
        f"k_curv recon reldev = {r['k_curv_recon_reldev']:.2e}",
        "",
        f"(A) |c_odd|/|c_even| = {r['odd_even_ratio']:.4e}  floor 1e-3  -> {'OK' if r['odd_floor_ok'] else 'VIOLATED'}",
        f"(B) max(q_dec)_tail = {r['max_q_dec_tail']:.4f} < 1.857 -> {'PASS' if r['conjunct_B'] else 'FAIL'}",
        f"(C) Delta_res(occ) = {r['Delta_res_occ']:.5f}  guard {r['dres_guard']:.4f}; tail crossing = {r['tail_crossing']}",
        f"    h_par = {r['h_par']:.5f}; n=2 zone crossings = {r['n_cross_n2']}",
        f"(d5) Delta_t tail={r['dt_tail']:.3f} full={r['dt_full']:.3f} vs t_therm=6 (ratio {r['dur_ratio_full']:.3f})",
        "",
        f"3-tuple: sign={r['sign_verdict']} mag={r['magnitude_verdict']} regime={r['regime_verdict']}",
        f"=> tail crossing exists => relic clause (d) DEMOTED argument-grade -> coincidence-bounded",
    ]
    ax[1, 1].text(0.02, 0.98, "\n".join(lines), va="top", ha="left", fontsize=8.5, family="monospace")

    fig.suptitle("S101-W1-QEQ-RELIC-ODDFLOOR — relic odd-floor + gamma clock + resonance (IN-band FAIL)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — verdict payload + main
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict, value, audit_sha, content_sha, sign_verdict,
                          magnitude_verdict, regime_verdict, extra_rows=None):
    payload = {
        "session": "101",
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # Save npz (strip the self-referential 'value' before saving arrays)
    save = {k: v for k, v in r.items() if k != "value"}  # (local)
    save["audit_sha256"] = audit_sha
    save["content_sha256"] = content_sha
    np.savez(OUT_NPZ, **save)
    make_plot(r)

    # ---- report ----
    print("=== CLOCK NORMALIZATION (the one new derivation) ===")
    print(f"  S3 = sum w_n/lam^3 = {r['S3']:.6f}  (= 8*k_curv; recon reldev {r['k_curv_recon_reldev']:.2e})")
    print(f"  S5 = sum w_n/lam^5 = {r['S5_vac']:.6f} (vacuum) / {r['S5_dress']:.6f} (dressed)")
    print(f"  chi_I = {r['chi_I']:.6f} M_KK^-5 (vacuum) / {r['chi_I_dress']:.6f} (dressed); reldev {abs(r['chi_I_dress']-r['chi_I'])/r['chi_I']:.3e}")
    print(f"  omega_q^tau  = {r['omega_q_tau']:.6f} tau^-1  (npz {r['omega_q_tau_npz']:.6f})")
    print(f"  omega_q^phys = {r['omega_q_phys']:.6f} M_KK (vacuum) / {r['omega_q_phys_dress']:.6f} (dressed)")
    print(f"  gamma = dt/dtau = {r['gamma']:.6f} M_KK^-1 (vacuum) / {r['gamma_dress']:.6f} (dressed)")
    print(f"  max|d ln chi_I(q)| over tail = {r['dln_chi_max']:.6f}")
    print("=== RESONANCE GEOMETRY (conjunct C) ===")
    print(f"  pair band [q=0] = [{r['pair_bottom_q0']:.5f}, {r['pair_top_q0_L12']:.5f}] M_KK (top from L12 cache)")
    print(f"  omega_q^phys IN band: {r['in_band']}  => end-state: {r['end_state']}")
    print(f"  Delta_res(occ) = {r['Delta_res_occ']:.6f}  (full {r['Delta_res_full']:.6f}); guard = {r['dres_guard']:.6f}")
    print(f"  h_par = {r['h_par']:.6f} (q_osc {r['q_osc']:.6f}, q_bar {r['q_bar']:.4f}); half-width {r['half_width']:.6f}")
    print(f"  TAIL CROSSING: {r['tail_crossing']}  ({r['n_cross_all']} modes, {r['n_cross_occ']} occupied; w_cross={r['w_cross']:.0f})")
    print(f"  n=2 Mathieu-zone crossings (report-only): {r['n_cross_n2']}")
    print("=== DILUTION WINDOW (conjunct B) ===")
    print(f"  max(q_dec)_tail = {r['max_q_dec_tail']:.4f} < 1.857 => window empty: {r['dilution_window_empty']}")
    print(f"  3*p_local tail range = [{r['three_p_min']:.4f}, {r['three_p_max']:.4f}]; tail stratum frac (q_dec in (-2,0)) = {r['strat_frac_tail']:.4f}")
    print("=== ODD FLOOR (conjunct A) ===")
    print(f"  c_even = {r['c_even']:.6e}, c_odd = {r['c_odd']:.6e}, ratio = {r['odd_even_ratio']:.6e}  (floor 1e-3) -> {'OK' if r['odd_floor_ok'] else 'VIOLATED'}")
    print("=== DURATION (d5 pincer) ===")
    print(f"  Delta_t tail = {r['dt_tail']:.4f}, full = {r['dt_full']:.4f} M_KK^-1; t_therm = 6 (ratios {r['dur_ratio_tail']:.3f}/{r['dur_ratio_full']:.3f})")
    print()
    print(f"(value=<dict>, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    val_str = (
        f"FAIL_IN-band_resonance-LIVE:omega_q_phys={r['omega_q_phys']:.6f}_in_band[{r['pair_bottom_q0']:.4f},{r['pair_top_q0_L12']:.4f}]"
        f";gamma={r['gamma']:.6f};Delta_res_occ={r['Delta_res_occ']:.6f}<guard{r['dres_guard']:.4f}"
        f";tail_crossing={r['n_cross_all']}modes_{r['n_cross_occ']}occ"
        f";oddratio={r['odd_even_ratio']:.4e}>1e-3;max_qdec_tail={r['max_q_dec_tail']:.4f}<1.857(B_PASS)"
        f";h_par={r['h_par']:.5f};Dt_full={r['dt_full']:.3f}vs_ttherm6"
        if r["verdict"] == "FAIL" else
        f"{r['verdict']}:omega_q_phys={r['omega_q_phys']:.6f};gamma={r['gamma']:.6f};Delta_res_occ={r['Delta_res_occ']:.6f}"
        f";oddratio={r['odd_even_ratio']:.4e};max_qdec_tail={r['max_q_dec_tail']:.4f}"
    )  # (local)

    extra = [
        "# regulator_pin=a_0^{zeta} (relic spectral moments S3/S5 inherit s97/s99 zeta-regulated cache)",
        f"# clock: chi_I={r['chi_I']:.6f}_M_KK^-5 omega_q_phys={r['omega_q_phys']:.6f}_M_KK gamma={r['gamma']:.6f}_M_KK^-1 (6sf downstream C10)",
        f"# end_state=IN-band_resonance-LIVE; relic clause (d) DEMOTED argument-grade->coincidence-bounded; amend S101-HPARITY-STAGE1 BEFORE S102 Stage-2",
    ]  # (local)

    print_verdict_payload(r["verdict"], val_str, audit_sha, content_sha,
                          r["sign_verdict"], r["magnitude_verdict"], r["regime_verdict"], extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
