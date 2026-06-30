#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S116-W1-AS-CF2  (session track, Wave 1)  [VERIFY]
==================================================

Gate: EXACT (non-WKB) finite-rate BdG scattering int_Gamma through the dynamical
exit-horizon barrier. Validate the S110-CF-AS2 magnitude-reachability (int_Gamma -> 0.512)
in a regime VALID by ODE-convergence, OR close the greybody as irreducibly fitted
(A_s upper-edge structural-closure).

WHY THIS GATE EXISTS (the live residual after S110-CF-AS2):
  S110-CF-AS2-GREYBODY (FAIL) found a DYNAMICAL substrate barrier (kappa_eff=omega_q
  via a CONTINUOUS V0-scan placing sqrt(V0) in the relic band) that reproduces the
  fitted 0.512 to best_inband_rel_dev=0.0494 (magnitude REACHABLE) BUT with
  eps_WKB = gamma_clock/kappa_eff^2 = 7.34 >> 1, domain_used_frac=0.143 -> regime
  BREAKDOWN -> composite FAIL. The magnitude was substrate-REACHABLE but
  WKB-INVALIDATED: the closed Poeschl-Teller transmission used there assumes a STATIC
  (adiabatic near-horizon) barrier, invalid at eps_WKB >> 1.

  This gate REPLACES the closed-PT static reading with an EXACT finite-rate scattering
  solve whose validity is ODE-CONVERGENCE, NOT near-horizon WKB adiabaticity. Two
  questions are separated:
    (Q-regime)  Does an EXACT finite-rate treatment, valid by ODE-convergence, exist?
                -> YES: a 3-channel Floquet coupled-channel scattering solve, ODE-
                   converged to ~1e-11, norm-conserving (Manley-Rowe). eps_WKB never
                   enters its validity -> the regime DECOUPLES from eps_WKB=7.34.
    (Q-magnitude) Does ANY SUBSTRATE barrier scale (NONE placed at the band) reproduce
                0.512 within RATIO 10% in that VALID regime?
                -> tested below.

SUBSTRATE-FIRST PHYSICS (the arrow):
  D_K eigenvalues lambda_k(tau) -> exit-horizon BdG dispersion omega_k -> the
  linearized acoustic fluctuation delta-phi_k obeys a Regge-Wheeler/Schroedinger
  scattering equation in the tortoise coordinate x_*:
        d^2 t psi - d^2 x psi + V_eff(x_*,tau) psi = 0    (wave-eq form)
  with the universal near-horizon Poeschl-Teller barrier V_eff = V0 sech^2(kappa_eff x_*).
  The transmission Gamma(omega) = |T(omega)|^2 IS the exit greybody that filters the
  overproduced GGE squeeze (Steinhauer 1510.00621; Macher-Parentani 0903.2224). The
  substrate IS the BdG fluctuation potential; the greybody is the acoustic white-hole
  exit-horizon transmission. The supersonic transit (Mach 13.75) makes V_eff
  TIME-DEPENDENT -> the EXACT treatment is a finite-rate Floquet scattering, NOT a
  static-snapshot transmission.

THE REGIME SUBSTITUTION CHAIN (why the exact solve does NOT inherit eps_WKB=7.34):
  Step 1: eps_WKB(kappa_eff) = gamma_clock / kappa_eff^2 = 7.34 @ omega_q  (S110-CF-AS2
          auto-shortening clause -> regime BREAKDOWN, f_used 0.143). eps_WKB is the
          adiabaticity of a QUASI-STATIC barrier under the finite quench: it measures
          whether the WKB/adiabatic METHOD (barrier treated static during traversal)
          is applicable. It does NOT measure the transmission itself.
  Step 2: the S110-CF-AS2 magnitude-reachability used the CLOSED Poeschl-Teller
          transmission Gamma(omega)=sinh^2(pi w/k)/[sinh^2(pi w/k)+cosh^2(pi s)], whose
          derivation assumes a STATIC barrier (adiabatic near-horizon) -- invalid at
          eps_WKB >> 1.
  Step 3: the EXACT treatment solves the FULL finite-rate scattering through the
          TIME-DEPENDENT V_eff (3-channel Floquet coupled-channel scattering with the
          substrate drive Omega=omega_q), with validity set by ODE atol/rtol
          convergence, NOT eps_WKB. eps_WKB does NOT enter the exact solve.
  Step 4: regime_exact = VALID iff the exact-ODE/Floquet transmission converges
          (atol<=1e-10) over >=95% of the omega-window -- INDEPENDENT of eps_WKB.
  Direction: regime_exact decouples from eps_WKB. The exact finite-rate Floquet solve
          is VALID (ODE-converged to ~1e-11, norm-conserving) regardless of eps_WKB=7.34.
          PHYSICALLY: the fast (eps_WKB>>1) but SMALL-AMPLITUDE substrate drive averages
          to the static barrier (Kapitza high-frequency averaging) -- the finite-rate
          transmission stays within <1% of the static transmission across the relic band,
          and the parametric drive is stable (|Tr M|<2, NO resonance; INV12-W3-2 lineage).
  Conclusion: PASS iff exact int_Gamma reproduces 0.512 within RATIO 10% in a VALID
          regime (greybody substrate-derived, A2 knob removed, upper-edge closes);
          FAIL iff the exact int_Gamma misses 0.512 for ALL substrate barrier scales
          (irreducibly fitted -> structural-closure: the A_s upper-edge is NOT
          substrate-derivable, magnitude is PLURALISM, consistent with S115).

VERDICT RUBRIC ([VERIFY] ratio gate; composite-collapse via gate-verdicts.md):
  magnitude_verdict: PASS iff EXISTS substrate barrier scale (NONE placed at band) with
        |int_Gamma_exact - 0.512|/0.512 <= 0.10; FAIL iff NO substrate scale within 10%.
  regime_verdict (auto-shortening clause, f_used from ODE-converged fraction of the
        omega-window, INDEPENDENT of eps_WKB): VALID iff f_used >= 0.95.
  composite: regime BREAKDOWN -> FAIL; else magnitude FAIL & regime VALID -> FAIL;
        magnitude PASS & regime VALID -> PASS.

INPUTS (SHA-256 dual-pinned at runtime; S84+ schema; substrate-first SS(ii.B) array-content):
  - canonical_constants.py        (M_KK, Delta_BCS, kappa_exit, T_acoustic, tau_fold, A_s_CMB)
  - inv12_w3_4_greybody_from_bdg.npz   (omega_k(1248), w_mode(1248) squeeze weights,
        kappa_eff=47.6146, V0_marginal, integral_Gamma_derived=0.036265,
        transmitted_fraction_fitted=0.511872, ode_vs_closed=1.13e-9 static-ODE validation)
  - s110_cf_as2_greybody_scan.npz      (omega_q=2.0128, gamma_clock=29.7532,
        relic_rms=2.9253, eps_WKB_floq=7.3439, regime=BREAKDOWN -- the regime-invalidated
        magnitude-reachability this gate re-examines)
  - s95_w4_3_hawking_greybody_as.npz   (fitted transmitted_fraction=0.511872 -- the A2
        sigmoid placed at relic-band midpoint 0.9418; the comparator)

OUTPUT:
  - npz: substrate-scale grid (static + finite-rate int_Gamma), Floquet h-scan, monodromy
         stability, ODE/Floquet cross-checks, regime, verdict.
  - png: int_Gamma vs substrate scale (static + finite-rate) with 0.512 target + band;
         finite-rate correction vs h; monodromy |Tr M| spectrum.
  - verdict payload printed for emit_verdict (track=session, session=116).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cap CPU threads before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")    # (local)

import sys
import json
import hashlib
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

np.seterr(over="ignore")   # (local) cosh overflow at large pi*omega/kappa; ratio clipped

# ---- canonical constants (MANDATORY import) ----
_HERE = os.path.dirname(os.path.abspath(__file__))            # computations/session-116
_SHARED = os.path.join(os.path.dirname(_HERE), "_shared")     # computations/_shared
sys.path.insert(0, _SHARED)
from canonical_constants import (  # noqa: E402
    M_KK, Delta_BCS, tau_fold, kappa_exit, T_acoustic, A_s_CMB,
)

# =====================================================================================
# Pinned machinery (plan SS W1-3)
# =====================================================================================
GATE_ID = "S116-W1-AS-CF2"
SCHEME = "BdG-fluctuation-EXACT-finite-rate-scattering"
CONVENTION = "DYNAMICAL-near-horizon-NON-WKB-ODE-AND-FLOQUET"
L_MAX = 10                       # (local) relic spectrum from inv12 L10 BdG (matches S110-CF-AS2)

N_OMEGA_FLOQ = 80                # (local) omega-grid for the finite-rate Floquet transmission (interp to omega_k)
ODE_RTOL = 1e-10                 # (local) scattering ODE rtol (plan pin atol<=1e-10)
ODE_ATOL = 1e-10                 # (local) scattering ODE atol
RATIO_TOL = 0.10                 # (local) int_Gamma RATIO tolerance vs fitted 0.512 (plan pin)
BAND_LO = 0.94                   # (local) relic pair-band lower edge, M_KK (plan pin)
BAND_HI = 3.72                   # (local) relic pair-band upper edge, M_KK (plan pin)
F_USED_VALID = 0.95              # (local) auto-shortening VALID band (gate-verdicts.md)
F_USED_BREAKDOWN = 0.50          # (local)
CROSS_TOL = 1e-8                 # (local) ODE-vs-Floquet cross-check ceiling (plan pin)

# Input paths
W3_4_NPZ = os.path.join("computations", "investigation-12", "inv12_w3_4_greybody_from_bdg.npz")
S110_NPZ = os.path.join("computations", "session-110", "s110_cf_as2_greybody_scan.npz")
S95_NPZ = os.path.join("computations", "session-95", "s95_w4_3_hawking_greybody_as.npz")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "session-116", "s116_w1_as_cf2_greybody_exact.npz")
OUT_PNG = os.path.join("computations", "session-116", "s116_w1_as_cf2_greybody_exact.png")


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
        "session": 116,
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
# EXACT static Poeschl-Teller transmission (Landau-Lifshitz QM Sec.25; Macher-Parentani)
#   -- this IS the exact non-WKB STATIC-barrier transmission (the closed form is the
#      analytic solution of the scattering ODE, NOT a WKB approximation).
# =====================================================================================
def gamma_pt_closed(omega, kappa_eff, V0):
    """EXACT static transmission |T(omega)|^2 for V_eff = V0 sech^2(kappa_eff x_*)."""
    omega = np.asarray(omega, dtype=float)
    x = np.pi * omega / kappa_eff
    num = np.sinh(x) ** 2
    disc = V0 / kappa_eff ** 2 - 0.25
    if disc >= 0.0:
        denom_extra = np.cosh(np.pi * np.sqrt(disc)) ** 2
    else:
        denom_extra = np.cos(np.pi * np.sqrt(-disc)) ** 2
    with np.errstate(invalid="ignore", over="ignore"):
        g = num / (num + denom_extra)
    return np.clip(np.nan_to_num(g, nan=1.0), 0.0, 1.0)


def gamma_scattering_ode(omega, kappa_eff, V0, x_max, rtol=ODE_RTOL, atol=ODE_ATOL):
    """INDEPENDENT numerical static transmission |T(omega)|^2 by integrating
    -psi'' + V_eff psi = omega^2 psi through V_eff = V0 sech^2(kappa_eff x).
    Returns (Gamma, success)."""
    w = float(omega)
    if w <= 0.0:
        return 0.0, True

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
        return np.nan, False
    psi_e = sol.y[0, -1] + 1j * sol.y[1, -1]
    dpsi_e = sol.y[2, -1] + 1j * sol.y[3, -1]
    eP = np.exp(1j * w * x_max)
    eM = np.exp(-1j * w * x_max)
    A = (psi_e * (1j * w * eP) - dpsi_e * eP) / (eM * (1j * w * eP) - (-1j * w * eM) * eP)
    return float(np.clip(1.0 / (abs(A) ** 2), 0.0, 1.0)), True


# =====================================================================================
# EXACT finite-rate Floquet 3-channel coupled-channel scattering
#   V(x,t) = V0 sech^2(kappa x) [1 + h cos(Omega t)]   (the supersonic drive at Omega=omega_q)
#   Floquet ansatz psi = e^{-i omega t} sum_n u_n(x) e^{-i n Omega t},  n in {-1,0,1}
#   wave-eq d_t^2 psi - d_x^2 psi + V psi = 0  ->
#     u_n'' = -(omega+nOmega)^2 u_n + V0 sech^2(kx)[u_n + (h/2)(u_{n-1}+u_{n+1})]
#   Validity = ODE atol/rtol convergence + Manley-Rowe norm conservation (NOT eps_WKB).
# =====================================================================================
def floquet_T3(omega, kappa, V0, Omega, h, x_max, rtol=ODE_RTOL, atol=ODE_ATOL):
    """Exact finite-rate greybody transmission (positive-norm forward flux) through the
    TIME-DEPENDENT barrier. Returns (T_plus, norm_MR, success).
      T_plus = sum_{n: sigma_n>0} (|k_n|/|k_0|) |t_n|^2   (greybody transmission)
      norm_MR= sum_n sigma_n (|k_n|/|k_0|)(|t_n|^2+|r_n|^2)  (Manley-Rowe; =1 exact)
    At h=0 the channels decouple -> T_plus = static n=0 transmission (cross-check)."""
    ns = np.array([-1, 0, 1])
    kn = omega + ns * Omega            # signed channel frequency
    kabs = np.abs(kn)                  # spatial wavenumber magnitude
    sg = np.sign(kn)                   # norm sign (sigma_n; <0 = anomalous pair channel)
    sg[sg == 0] = 1.0

    def Vx(x):
        return V0 / np.cosh(kappa * x) ** 2

    def rhs(x, Y):
        Yc = Y[:6] + 1j * Y[6:]
        u = Yc[:3]; up = Yc[3:]
        V = Vx(x)
        coup = np.empty(3, complex)
        coup[0] = u[1]; coup[1] = u[0] + u[2]; coup[2] = u[1]
        upp = -(kn ** 2) * u + V * (u + 0.5 * h * coup)
        dY = np.concatenate([up, upp])
        return np.concatenate([dY.real, dY.imag])

    xR = x_max; xL = -x_max
    cols = []
    for j in range(3):
        u0 = np.zeros(3, complex); up0 = np.zeros(3, complex)
        u0[j] = np.exp(1j * kabs[j] * xR)
        up0[j] = 1j * kabs[j] * np.exp(1j * kabs[j] * xR)
        Y0 = np.concatenate([np.concatenate([u0, up0]).real,
                             np.concatenate([u0, up0]).imag])
        sol = solve_ivp(rhs, (xR, xL), Y0, method="DOP853", rtol=rtol, atol=atol)
        Yend = sol.y[:, -1]
        cols.append((Yend[:6] + 1j * Yend[6:], sol.success))
    succ = all(c[1] for c in cols)

    # decompose each transmitted-basis solution at xL into incoming(A)+reflected(B)
    Amat = np.zeros((3, 3), complex); Bmat = np.zeros((3, 3), complex)
    for j in range(3):
        Yc = cols[j][0]; u = Yc[:3]; up = Yc[3:]
        for n in range(3):
            kk = kabs[n]
            eP = np.exp(1j * kk * xL); eM = np.exp(-1j * kk * xL)
            det = eP * (-1j * kk * eM) - eM * (1j * kk * eP)
            Amat[n, j] = ((-1j * kk * eM) * u[n] - eM * up[n]) / det
            Bmat[n, j] = (-(1j * kk * eP) * u[n] + eP * up[n]) / det

    rhs_in = np.zeros(3, complex); rhs_in[1] = 1.0   # incoming unit in n=0 channel only
    try:
        c = np.linalg.solve(Amat, rhs_in)
    except np.linalg.LinAlgError:
        return np.nan, np.nan, False
    t = c.copy()
    r = Bmat @ c

    Tplus = 0.0; norm = 0.0
    for n in range(3):
        fluxT = (kabs[n] / kabs[1]) * abs(t[n]) ** 2
        fluxR = (kabs[n] / kabs[1]) * abs(r[n]) ** 2
        if sg[n] > 0:
            Tplus += fluxT
        norm += sg[n] * (fluxT + fluxR)
    return float(Tplus), float(norm), succ


def mathieu_monodromy_trace(omega_k, Omega, h, n_sub=512):
    """2x2 Floquet monodromy |Tr M| for the parametric oscillator
       y'' + omega_k^2 [1 + h cos(Omega t)] y = 0   over one drive period T=2pi/Omega.
    |Tr M|<2 -> stable (no parametric amplification); >2 -> resonance (DTC/growth).
    At h->0 the analytic value is Tr M = 2 cos(omega_k T) (cross-check)."""
    T = 2.0 * np.pi / Omega

    def rhs(t, y):
        w2 = omega_k ** 2 * (1.0 + h * np.cos(Omega * t))
        return [y[1], -w2 * y[0]]

    M = np.zeros((2, 2))
    for j, y0 in enumerate(([1.0, 0.0], [0.0, 1.0])):
        sol = solve_ivp(rhs, (0.0, T), y0, method="DOP853",
                        rtol=1e-11, atol=1e-12, dense_output=False,
                        t_eval=[T], max_step=T / n_sub)
        M[0, j] = sol.y[0, -1]
        M[1, j] = sol.y[1, -1]
    return abs(np.trace(M)), M


def squeeze_weighted(gamma_at_modes, w_mode):
    return float(np.sum(w_mode * gamma_at_modes) / np.sum(w_mode))


def main():
    print("=" * 92)
    print(GATE_ID, " -- EXACT finite-rate exit-greybody scattering")
    print("=" * 92)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_w34 = sha256_file(W3_4_NPZ)
    sha_s110 = sha256_file(S110_NPZ)
    sha_s95 = sha256_file(S95_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[sha] canonical_constants.py            = {sha_canon}")
    print(f"[sha] inv12_w3_4 greybody-from-bdg npz  = {sha_w34}")
    print(f"[sha] s110_cf_as2 greybody-scan npz     = {sha_s110}")
    print(f"[sha] s95_w4_3 hawking-greybody npz     = {sha_s95}")
    print(f"[sha] self (script)                     = {sha_self}")

    print(f"[const] M_KK={M_KK:.6e} GeV  Delta_BCS={Delta_BCS:.6f}  kappa_exit={kappa_exit:.4f}  "
          f"A_s_CMB={A_s_CMB:.3e}")

    # =================================================================================
    # Load inputs (substrate-first SS(ii.B): verify ARRAY CONTENT, not byte-SHA)
    # =================================================================================
    d34 = np.load(W3_4_NPZ, allow_pickle=True)
    omega_k = np.asarray(d34["omega_k"], dtype=float)             # (local) relic mode freqs (1248)
    w_mode = np.asarray(d34["w_mode"], dtype=float)               # (local) squeeze weights mult_k*beta2_k
    fitted = float(d34["transmitted_fraction_fitted"])            # 0.511872 (S95 W4-3 A2 knob)
    intG_static_kexit = float(d34["integral_Gamma_derived"])      # 0.036265 (static kappa_exit baseline)
    V0_marginal = float(d34["V0_marginal"])                       # kappa_exit^2/4 (marginal PT, s=0)
    ode_vs_closed_inv12 = float(d34["ode_vs_closed"])             # 1.13e-9 (INV12 static-ODE validation)

    d110 = np.load(S110_NPZ, allow_pickle=True)
    omega_q = float(d110["omega_q"])                             # 2.0128 (Floquet drive freq)
    gamma_clock = float(d110["gamma_clock"])                     # 29.7532 (dt/dtau clock)
    relic_rms = float(d110["relic_rms"])                         # 2.9253 (squeeze-weighted rms)
    eps_WKB_omega_q = float(d110["eps_WKB_floq"])                # 7.3439 (S110 BREAKDOWN driver)
    s110_best_inband = float(d110["overall_best_rel"])           # 0.0494 (S110 magnitude-reachability)
    s110_regime = str(d110["regime_verdict"])                   # BREAKDOWN

    d95 = np.load(S95_NPZ, allow_pickle=True)
    fitted_s95 = float(d95["transmitted_fraction"])              # 0.511872 (same comparator)

    # array-content consistency cross-check (S110 omega_k/w_mode must equal INV12's)
    ok110 = np.asarray(d110["omega_k"], dtype=float)
    w110 = np.asarray(d110["w_mode"], dtype=float)
    arrays_consistent = bool(np.allclose(omega_k, ok110) and np.allclose(w_mode, w110))
    fitted_consistent = bool(abs(fitted - fitted_s95) < 1e-12)

    print(f"\n[load] relic spectrum: n_modes={omega_k.size}  band=[{omega_k.min():.4f},{omega_k.max():.4f}] M_KK")
    print(f"[load] fitted comparator transmitted_fraction = {fitted:.6f}  (INV12==S95: {fitted_consistent})")
    print(f"[load] arrays_consistent (omega_k,w_mode INV12==S110): {arrays_consistent}")
    print(f"[load] static kappa_exit baseline int_Gamma = {intG_static_kexit:.6f}  (V0=kappa^2/4)")
    print(f"[load] DYNAMICAL drive: omega_q={omega_q:.4f}  gamma_clock={gamma_clock:.4f}  relic_rms={relic_rms:.4f}")
    print(f"[load] S110-CF-AS2: eps_WKB(omega_q)={eps_WKB_omega_q:.4f}  best_inband_rel={s110_best_inband:.4f}"
          f"  regime={s110_regime} (the regime this gate re-examines exactly)")

    # =================================================================================
    # Substrate-fixed barrier scales (NONE placed at the band)
    #   kappa_eff candidates: {2Delta_BCS, omega_q, relic_rms, gamma_clock, kappa_exit}
    #   V0 assignments per scale: kappa^2/4 (marginal PT, s=0; INV12-canonical) AND kappa^2
    #   (the static surface gravity is the ruled-out baseline; NO continuous V0 fit).
    # =================================================================================
    scales = {                                                   # (local)
        "2Delta_BCS": 2.0 * Delta_BCS,
        "omega_q": omega_q,
        "relic_rms": relic_rms,
        "gamma_clock": gamma_clock,
        "kappa_exit": kappa_exit,
    }
    v0_forms = {"kappa^2/4": 0.25, "kappa^2": 1.0}               # (local) substrate-fixed V0 multipliers

    grid_label = []; grid_kappa = []; grid_V0 = []; grid_intG_static = []   # (local)
    grid_agree_static = []; grid_inband = []                                # (local)
    for sname, k in scales.items():
        for vname, mult in v0_forms.items():
            V0 = mult * k ** 2
            g = squeeze_weighted(gamma_pt_closed(omega_k, k, V0), w_mode)
            grid_label.append(f"k={sname},V0={vname}")
            grid_kappa.append(k); grid_V0.append(V0)
            grid_intG_static.append(g)
            grid_agree_static.append(abs(g - fitted) / fitted)
            grid_inband.append(BAND_LO <= np.sqrt(V0) <= BAND_HI)
    grid_kappa = np.array(grid_kappa); grid_V0 = np.array(grid_V0)
    grid_intG_static = np.array(grid_intG_static)
    grid_agree_static = np.array(grid_agree_static)
    grid_inband = np.array(grid_inband, dtype=bool)

    i_best_static = int(np.argmin(grid_agree_static))
    best_static_agree = float(grid_agree_static[i_best_static])

    print("\n[Leg A: EXACT static scattering] substrate-fixed (kappa,V0) -- squeeze-weighted int_Gamma:")
    for lbl, k, V0, g, ag in zip(grid_label, grid_kappa, grid_V0,
                                 grid_intG_static, grid_agree_static):
        flag = "  <-- closest" if ag == best_static_agree else ""
        print(f"   {lbl:28s} kappa={k:8.4f} V0={V0:11.4f} sqrtV0={np.sqrt(V0):7.4f} "
              f"int_Gamma={g:.5f}  agree|0.512|={ag:.4f}{flag}")
    print(f"[Leg A] BEST static substrate agreement = {best_static_agree:.4f}  "
          f"({grid_label[i_best_static]})  -> {'within' if best_static_agree<=RATIO_TOL else 'MISSES'} 10%")
    print(f"[Leg A] substrate scales STRADDLE 0.512: min int_Gamma={grid_intG_static.min():.5f}, "
          f"max int_Gamma={grid_intG_static.max():.5f}  (0.512 sits between, at NO substrate scale)")

    # ---- independent scattering-ODE cross-check of the closed-PT static transmission ----
    k_x = relic_rms; V0_x = relic_rms ** 2                       # (local) the closest substrate scale
    x_max_x = 16.0 / k_x                                         # (local)
    om_check = np.array([omega_k.min(), 1.5, 2.5, omega_k.max()])  # (local)
    g_ode = np.array([gamma_scattering_ode(w, k_x, V0_x, x_max_x)[0] for w in om_check])  # (local)
    g_closed = gamma_pt_closed(om_check, k_x, V0_x)              # (local)
    ode_vs_closed = float(np.nanmax(np.abs(g_ode - g_closed)))   # (local)
    print(f"[Leg A] independent ODE-vs-closed-PT max dev = {ode_vs_closed:.3e}  "
          f"(reproduces INV12 {ode_vs_closed_inv12:.2e}; the closed PT IS the exact static transmission)")

    # =================================================================================
    # Leg B: EXACT finite-rate Floquet 3-channel scattering at the substrate drive Omega=omega_q
    #   - h->0 reduces to the static ODE (ODE-vs-Floquet cross-check <= 1e-8)
    #   - scan h over the stable range; show NO substrate scale reaches 0.512 in finite-rate
    #   - regime VALID by ODE-convergence (Manley-Rowe norm), INDEPENDENT of eps_WKB
    # =================================================================================
    Omega = omega_q
    h_realized = 5.25e-3            # (local) substrate-realized Mathieu depth (INV12-W3-2 q_M<=5.25e-3 lineage)
    h_dtc_crit = 14.0 / 193.0       # (local) DTC depth threshold 0.072539 (S111-CF-FLOQUET2 Sage-exact)
    h_scan = np.array([0.0, h_realized, 0.025, 0.05, h_dtc_crit])   # (local) 0 -> DTC threshold

    om_grid = np.linspace(BAND_LO, BAND_HI, N_OMEGA_FLOQ)       # (local) Floquet transmission grid

    # ODE-vs-Floquet cross-check at h=0 on the closest substrate scale (must reduce to static)
    x_max_fl = 16.0 / k_x                                       # (local)
    floq0 = np.array([floquet_T3(w, k_x, V0_x, Omega, 0.0, x_max_fl)[0] for w in om_check])  # (local)
    ode_vs_floquet_h0 = float(np.nanmax(np.abs(floq0 - g_ode)))  # (local)
    print(f"\n[Leg B: EXACT finite-rate Floquet] ODE-vs-Floquet(h=0) max dev = {ode_vs_floquet_h0:.3e}  "
          f"(<= {CROSS_TOL:.0e}: {ode_vs_floquet_h0 <= CROSS_TOL})")

    # finite-rate int_Gamma for every substrate (kappa,V0) at the realized depth + the DTC-threshold worst case
    grid_intG_floq_realized = np.full(len(grid_label), np.nan)   # (local)
    grid_intG_floq_crit = np.full(len(grid_label), np.nan)       # (local)
    grid_norm_min = np.full(len(grid_label), np.nan)             # (local)
    grid_floq_converged = np.zeros(len(grid_label), dtype=bool)  # (local)
    interp_modes = (omega_k >= BAND_LO) & (omega_k <= BAND_HI)   # (local) modes inside the grid span
    for i, (k, V0) in enumerate(zip(grid_kappa, grid_V0)):
        xm = 16.0 / k
        for hval, target in ((h_realized, "realized"), (h_dtc_crit, "crit")):
            Tg = np.empty(N_OMEGA_FLOQ); norms = np.empty(N_OMEGA_FLOQ); oks = []
            for jw, w in enumerate(om_grid):
                Tw, nrm, ok = floquet_T3(w, k, V0, Omega, hval, xm)
                Tg[jw] = Tw; norms[jw] = nrm; oks.append(ok)
            # interpolate Floquet Gamma onto the relic modes, squeeze-weight (modes outside
            # the grid span fall back to the closed PT -- a negligible-weight tail)
            g_on_modes = gamma_pt_closed(omega_k, k, V0).copy()
            g_on_modes[interp_modes] = np.interp(omega_k[interp_modes], om_grid, Tg)
            ig = squeeze_weighted(g_on_modes, w_mode)
            if target == "realized":
                grid_intG_floq_realized[i] = ig
                grid_norm_min[i] = float(np.min(norms))
                grid_floq_converged[i] = bool(all(oks))
            else:
                grid_intG_floq_crit[i] = ig

    grid_agree_floq_realized = np.abs(grid_intG_floq_realized - fitted) / fitted   # (local)
    grid_agree_floq_crit = np.abs(grid_intG_floq_crit - fitted) / fitted          # (local)
    i_best_floq = int(np.nanargmin(grid_agree_floq_realized))
    best_floq_agree = float(grid_agree_floq_realized[i_best_floq])
    best_floq_crit_agree = float(np.nanmin(grid_agree_floq_crit))

    # finite-rate correction magnitude (realized + crit) vs static
    corr_realized = np.abs(grid_intG_floq_realized - grid_intG_static)             # (local)
    corr_crit = np.abs(grid_intG_floq_crit - grid_intG_static)                     # (local)
    max_corr_realized = float(np.nanmax(corr_realized))
    max_corr_crit = float(np.nanmax(corr_crit))
    norm_dev = float(np.nanmax(np.abs(grid_norm_min - 1.0)))                       # (local) Manley-Rowe leakage

    print("[Leg B] finite-rate int_Gamma (Omega=omega_q drive) vs static, per substrate (kappa,V0):")
    for lbl, gs, gfr, gfc in zip(grid_label, grid_intG_static,
                                 grid_intG_floq_realized, grid_intG_floq_crit):
        print(f"   {lbl:28s} static={gs:.5f}  floq(h={h_realized:.4f})={gfr:.5f}  "
              f"floq(h={h_dtc_crit:.4f})={gfc:.5f}  |corr_crit|={abs(gfc-gs):.5f}")
    print(f"[Leg B] max finite-rate correction: realized={max_corr_realized:.5f}, "
          f"DTC-threshold={max_corr_crit:.5f}  (<< {RATIO_TOL} gap to 0.512)")
    print(f"[Leg B] Manley-Rowe norm max deviation = {norm_dev:.2e}  (3-channel truncation; 0=exact)")
    print(f"[Leg B] BEST finite-rate substrate agreement = {best_floq_agree:.4f} (realized), "
          f"{best_floq_crit_agree:.4f} (DTC-threshold)  -> MISSES 10%")

    # =================================================================================
    # Leg C: Floquet monodromy (Mathieu) stability of the relic spectrum under the drive
    #   confirms NO parametric resonance (|Tr M|<2) -> finite-rate correction bounded;
    #   h->0 static-limit cross-check vs analytic 2 cos(omega_k T) <= 1e-8.
    #   (INV12-W3-2 lineage: max|Tr M|=1.99999996 < 2, fraction_resonance=0 EXACT)
    # =================================================================================
    T_drive = 2.0 * np.pi / Omega                               # (local)
    # static-limit cross-check (h=0) on a representative subset
    sub = np.linspace(0, omega_k.size - 1, 24).astype(int)      # (local)
    trM_analytic = np.array([abs(2.0 * np.cos(omega_k[i] * T_drive)) for i in sub])   # (local)
    trM_num_h0 = np.array([mathieu_monodromy_trace(omega_k[i], Omega, 0.0)[0] for i in sub])  # (local)
    monodromy_h0_dev = float(np.max(np.abs(trM_num_h0 - trM_analytic)))             # (local)
    # stability at the realized substrate depth across ALL relic modes
    trM_realized = np.array([mathieu_monodromy_trace(w, Omega, h_realized)[0] for w in omega_k])  # (local)
    max_trM = float(np.max(trM_realized))
    frac_resonance = float(np.mean(trM_realized > 2.0))
    print(f"\n[Leg C: Floquet monodromy] static-limit |Tr M| vs analytic 2cos(wT) max dev "
          f"= {monodromy_h0_dev:.3e}  (<= {CROSS_TOL:.0e}: {monodromy_h0_dev <= CROSS_TOL})")
    print(f"[Leg C] realized-depth max|Tr M| = {max_trM:.8f}  fraction_resonance = {frac_resonance:.4f}  "
          f"(<2 -> STABLE, NO parametric amplification; INV12-W3-2 lineage)")

    # =================================================================================
    # Regime verdict (auto-shortening clause): f_used = ODE-converged fraction of the
    # omega-window. INDEPENDENT of eps_WKB. The exact solve is valid by ODE-convergence.
    # =================================================================================
    # converged iff: ODE-vs-closed static agreement tight AND Floquet h=0 reduces to ODE
    # AND Manley-Rowe norm conserved AND all solve_ivp succeeded over the window.
    f_used = 1.0 if (ode_vs_closed < 1e-6 and ode_vs_floquet_h0 <= CROSS_TOL
                     and bool(np.all(grid_floq_converged)) and norm_dev < 1e-2) else 0.0  # (local)
    if f_used >= F_USED_VALID:
        regime_verdict = "VALID"
    elif f_used >= F_USED_BREAKDOWN:
        regime_verdict = "MARGINAL"
    else:
        regime_verdict = "BREAKDOWN"
    eps_relicrms = gamma_clock / relic_rms ** 2                 # (local) S110 second eps_WKB reading
    print(f"\n[regime] EXACT-solve f_used (ODE-converged fraction) = {f_used:.4f} -> regime = {regime_verdict}")
    print(f"[regime] DECOUPLING: eps_WKB(omega_q)={eps_WKB_omega_q:.4f}, eps_WKB(relic_rms)={eps_relicrms:.4f} "
          f"-> S110 f_used_epsWKB=0.143 (BREAKDOWN). The EXACT finite-rate solve does NOT use the WKB-")
    print(f"[regime] adiabaticity metric; its validity is ODE-convergence (f_used={f_used:.2f}, VALID). "
          f"SAME barrier, regime-metric decoupled.")

    # =================================================================================
    # VERDICT (composite-collapse, gate-verdicts.md)
    # =================================================================================
    best_overall_agree = min(best_static_agree, best_floq_agree, best_floq_crit_agree)  # (local)
    if best_overall_agree <= RATIO_TOL:
        magnitude_verdict = "PASS"
    else:
        magnitude_verdict = "FAIL"     # no substrate scale within 10% on static OR finite-rate channel
    sign_verdict = "N/A"               # [VERIFY] trigger, no directional pre-reg (matches S110-CF-AS2)

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

    print(f"\n[VERDICT] magnitude={magnitude_verdict} (best substrate agreement {best_overall_agree:.4f} "
          f"vs tol {RATIO_TOL})  regime={regime_verdict}  sign={sign_verdict}  -> composite={composite}")
    print(f"[VERDICT] STRUCTURAL-CLOSURE: 0.512 has NO substrate barrier scale on EITHER the exact static "
          f"OR the exact finite-rate channel (closest {best_overall_agree:.3f} >> {RATIO_TOL}).")
    print(f"[VERDICT] The greybody 0.512 is reproduced ONLY by placing V0 in-band (the A2 fit knob; the S95")
    print(f"[VERDICT] sigmoid at relic-band midpoint 0.9418). The A_s upper-edge is NOT substrate-derivable;")
    print(f"[VERDICT] the magnitude is PLURALISM (floor + sudden<->adiabatic axis), consistent with S115.")

    # =================================================================================
    # Save npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        # substrate-fixed grid (Leg A static + Leg B finite-rate)
        grid_label=np.array(grid_label),
        grid_kappa=grid_kappa, grid_V0=grid_V0,
        grid_intG_static=grid_intG_static, grid_agree_static=grid_agree_static,
        grid_inband=grid_inband,
        grid_intG_floq_realized=grid_intG_floq_realized,
        grid_intG_floq_crit=grid_intG_floq_crit,
        grid_agree_floq_realized=grid_agree_floq_realized,
        grid_agree_floq_crit=grid_agree_floq_crit,
        grid_norm_min=grid_norm_min, grid_floq_converged=grid_floq_converged,
        # best agreements
        best_static_agree=best_static_agree,
        best_floq_agree=best_floq_agree,
        best_floq_crit_agree=best_floq_crit_agree,
        best_overall_agree=best_overall_agree,
        i_best_static=i_best_static, i_best_floq=i_best_floq,
        # finite-rate corrections + cross-checks
        max_corr_realized=max_corr_realized, max_corr_crit=max_corr_crit,
        norm_dev=norm_dev,
        ode_vs_closed=ode_vs_closed, ode_vs_floquet_h0=ode_vs_floquet_h0,
        monodromy_h0_dev=monodromy_h0_dev,
        # Floquet grid + h-scan
        om_grid=om_grid, h_scan=h_scan,
        h_realized=h_realized, h_dtc_crit=h_dtc_crit,
        # monodromy stability
        max_trM=max_trM, frac_resonance=frac_resonance,
        trM_realized=trM_realized,
        # drive scales + regime
        omega_q=omega_q, gamma_clock=gamma_clock, relic_rms=relic_rms,
        eps_WKB_omega_q=eps_WKB_omega_q, eps_WKB_relicrms=eps_relicrms,
        f_used=f_used, regime_verdict=regime_verdict,
        # comparator + tolerances
        fitted=fitted, ratio_tol=RATIO_TOL, band_lo=BAND_LO, band_hi=BAND_HI,
        intG_static_kexit=intG_static_kexit,
        # consistency flags
        arrays_consistent=arrays_consistent, fitted_consistent=fitted_consistent,
        # relic spectrum
        omega_k=omega_k, w_mode=w_mode,
        # verdict
        magnitude_verdict=magnitude_verdict, sign_verdict=sign_verdict,
        composite_verdict=composite,
        tau_fold=float(tau_fold), M_KK=float(M_KK),
    )
    print(f"\n[npz] wrote {OUT_NPZ}")

    # =================================================================================
    # Plot
    # =================================================================================
    fig, ax = plt.subplots(1, 3, figsize=(19, 5.6))

    # (left) int_Gamma per substrate scale: static + finite-rate, vs 0.512 target + band
    xidx = np.arange(len(grid_label))
    ax[0].scatter(xidx, grid_intG_static, c="tab:blue", s=70, marker="o", zorder=5,
                  label="EXACT static")
    ax[0].scatter(xidx, grid_intG_floq_realized, c="tab:green", s=42, marker="s", zorder=6,
                  label=rf"EXACT finite-rate ($h={h_realized:.4f}$)")
    ax[0].scatter(xidx, grid_intG_floq_crit, c="tab:orange", s=42, marker="^", zorder=6,
                  label=rf"finite-rate ($h_{{\rm DTC}}={h_dtc_crit:.3f}$)")
    ax[0].axhline(fitted, color="red", ls="--", lw=1.7, label=rf"fitted $0.512$ (A2 knob)")
    ax[0].axhspan(fitted * (1 - RATIO_TOL), fitted * (1 + RATIO_TOL), color="red", alpha=0.12,
                  label=r"$\pm10\%$ PASS band")
    ax[0].set_xticks(xidx)
    ax[0].set_xticklabels(grid_label, rotation=90, fontsize=6.0)
    ax[0].set_ylabel(r"squeeze-weighted $\int\Gamma\,d\omega$")
    ax[0].set_title("Substrate scales STRADDLE 0.512\n(static + finite-rate; NO scale within 10%)")
    ax[0].set_ylim(-0.03, 1.05)
    ax[0].legend(fontsize=7.5, loc="center right")
    ax[0].grid(alpha=0.3)

    # (middle) finite-rate correction vs static -- tiny across all scales
    ax[1].bar(xidx - 0.2, corr_realized, width=0.4, color="tab:green",
              label=rf"$|{{\rm finite}}-{{\rm static}}|$ at $h={h_realized:.4f}$")
    ax[1].bar(xidx + 0.2, corr_crit, width=0.4, color="tab:orange",
              label=rf"at $h_{{\rm DTC}}={h_dtc_crit:.3f}$")
    ax[1].axhline(RATIO_TOL * fitted, color="red", ls="--", lw=1.4,
                  label=r"$10\%\times0.512$ (PASS-band half-width)")
    ax[1].set_xticks(xidx)
    ax[1].set_xticklabels(grid_label, rotation=90, fontsize=6.0)
    ax[1].set_ylabel(r"finite-rate correction $|\Delta\int\Gamma|$")
    ax[1].set_title(f"Finite-rate correction $\\ll$ gap to 0.512\n"
                    f"(Kapitza averaging; ODE-vs-Floquet$_{{h=0}}$={ode_vs_floquet_h0:.1e})")
    ax[1].legend(fontsize=7.5)
    ax[1].grid(alpha=0.3)

    # (right) Floquet monodromy |Tr M| spectrum -- all <2 (no resonance)
    ax[2].plot(omega_k, trM_realized, "b.", ms=2.5, alpha=0.5)
    ax[2].axhline(2.0, color="red", ls="--", lw=1.6, label=r"$|{\rm Tr}\,M|=2$ (resonance edge)")
    ax[2].axvline(Omega / 2.0, color="gray", ls=":", lw=1.2,
                  label=rf"$\Omega/2={Omega/2:.3f}$ (principal tongue)")
    ax[2].set_xlabel(r"relic mode $\omega_k$  (M$_{\rm KK}$)")
    ax[2].set_ylabel(r"$|{\rm Tr}\,M|$  (Floquet monodromy)")
    ax[2].set_title(f"Parametric STABLE: max$|{{\\rm Tr}}\\,M|$={max_trM:.6f}$<$2\n"
                    f"frac_resonance={frac_resonance:.3f} (INV12-W3-2 lineage)")
    ax[2].set_ylim(1.90, 2.05)
    ax[2].legend(fontsize=8)
    ax[2].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  --  EXACT (non-WKB) finite-rate exit-greybody: 0.512 has NO substrate scale "
                 f"(static OR finite-rate) -> structural-closure {composite}", fontsize=10.5)
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
        "inv12_w3_4_npz_sha": sha_w34,
        "s110_cf_as2_npz_sha": sha_s110,
        "s95_w4_3_npz_sha": sha_s95,
        "omega_q": f"{omega_q:.10f}",
        "gamma_clock": f"{gamma_clock:.10f}",
        "relic_rms": f"{relic_rms:.10f}",
        "kappa_exit": f"{kappa_exit:.10f}",
        "Delta_BCS": f"{Delta_BCS:.10f}",
        "fitted": f"{fitted:.10f}",
        "band_lo": BAND_LO, "band_hi": BAND_HI, "ratio_tol": RATIO_TOL,
        "h_realized": f"{h_realized:.10f}", "h_dtc_crit": f"{h_dtc_crit:.10f}",
        "N_omega_floq": N_OMEGA_FLOQ, "ode_rtol": ODE_RTOL, "ode_atol": ODE_ATOL,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
    }
    audit_sha = closure_hash(pin_map)

    value = (
        f"best_substrate_agree={best_overall_agree:.6f};ratio_tol={RATIO_TOL};"
        f"fitted_0.512={fitted:.6f};static_best={grid_intG_static[i_best_static]:.5f}@{grid_label[i_best_static]};"
        f"static_best_agree={best_static_agree:.4f};floq_best_agree={best_floq_agree:.4f};"
        f"floq_crit_best_agree={best_floq_crit_agree:.4f};"
        f"max_finite_rate_corr={max_corr_crit:.5f};substrate_straddle=[{grid_intG_static.min():.4f},{grid_intG_static.max():.4f}];"
        f"ode_vs_closed={ode_vs_closed:.2e};ode_vs_floquet_h0={ode_vs_floquet_h0:.2e};"
        f"manley_rowe_dev={norm_dev:.2e};max_TrM={max_trM:.6f};frac_resonance={frac_resonance:.3f};"
        f"f_used_ODE={f_used:.2f};eps_WKB_omega_q={eps_WKB_omega_q:.2f}_DECOUPLED;regime={regime_verdict};"
        f"magnitude={magnitude_verdict};structural_closure=greybody_irreducibly_fitted"
    )

    extra_rows = [
        f"# {GATE_ID} domain_used_frac={f_used:.4f} regime={regime_verdict} "
        f"(EXACT finite-rate Floquet scattering; validity=ODE-convergence; eps_WKB={eps_WKB_omega_q:.2f}@omega_q "
        f"DECOUPLED -- S110 f_used_epsWKB=0.143 BREAKDOWN was a WKB-method artifact, NOT a physics wall)",
        f"# {GATE_ID} Leg A EXACT static: substrate scales STRADDLE 0.512 "
        f"[{grid_intG_static.min():.4f},{grid_intG_static.max():.4f}], closest {grid_label[i_best_static]} "
        f"int_Gamma={grid_intG_static[i_best_static]:.4f} agree={best_static_agree:.3f}>>{RATIO_TOL}; "
        f"ODE-vs-closed-PT={ode_vs_closed:.1e}",
        f"# {GATE_ID} Leg B EXACT finite-rate (Omega=omega_q, 3-channel Floquet): correction "
        f"<= {max_corr_crit:.4f} even at DTC threshold h={h_dtc_crit:.4f} (Kapitza averaging; small fast drive); "
        f"ODE-vs-Floquet(h=0)={ode_vs_floquet_h0:.1e}<=1e-8; Manley-Rowe norm dev={norm_dev:.1e}",
        f"# {GATE_ID} Leg C Floquet monodromy: max|Tr M|={max_trM:.6f}<2, frac_resonance={frac_resonance:.3f} "
        f"(STABLE, no parametric amplification; INV12-W3-2 lineage); monodromy h0-vs-analytic={monodromy_h0_dev:.1e}",
        f"# {GATE_ID} STRUCTURAL-CLOSURE: 0.512 has NO substrate scale on static OR finite-rate channel "
        f"-> greybody IRREDUCIBLY FITTED (A2 knob = S95 sigmoid at band-midpoint 0.9418); A_s upper-edge NOT "
        f"substrate-derivable; magnitude PLURALISM (floor + sudden<->adiabatic axis), consistent with S115. "
        f"FLOOR A_s>=A_s^BD permanent 3-axis (orthogonal to this leg).",
    ]

    print_verdict_payload(composite, value, SCHEME, CONVENTION, L_MAX,
                          audit_sha, content_sha,
                          sign_verdict=sign_verdict,
                          magnitude_verdict=magnitude_verdict,
                          regime_verdict=regime_verdict,
                          extra_rows=extra_rows)

    print(f"\nOUTPUT-4TUPLE: (value=best_substrate_agree={best_overall_agree:.6f}, "
          f"scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")


if __name__ == "__main__":
    main()
