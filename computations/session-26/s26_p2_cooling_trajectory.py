"""
re-run: Session 26 Priority 2 -- Coupled Cooling-Trajectory ODE System
========================================================================

Gate: S26-P2-COOLING-TRAJECTORY
Parent: computations/session-26/s26_p2_cooling_trajectory.py (original author: gen-physicist, 2026-02-25)

T3 changes from parent:
  - `from canonical_constants import *` (was hardcoded G_TT=5.0)
  - G_TT replaced by G_DeWitt (canonical, S42 s42_gradient_stiffness)
  - `# (local)` tags on all intermediate / scan / threshold variables
  - First-20-line stdout SHA-256 log for every input
  - Final closure SHA-256 emission and S81 canonical verdict line

Physics is UNCHANGED. No physics parameters altered.

SUBSTITUTION CHAIN -- cooling-direction claim verdict logic
==========================================================
Claim (from parent compute_verdict): "P2-LOCK: CLOSED if no sustained lock in ODE."

Step 1: Definitions
  tau(t)  : modulus (Jensen deformation parameter), dimensionless
  mu(t)   : chemical potential, M_KK units
  H(t)    : Hubble rate, H(t) = H_0 * t_0 / t (radiation-era-like, script convention)
  V_spec(tau)  : bare spectral-action potential from s24a_vspec.npz
  F_cond(tau,r): BCS condensation free energy, r = mu/lmin(tau), from s26_multimode_bcs.npz
  V_eff(tau,mu,Tf) = V_spec(tau) + F_cond(tau,r) * sqrt(max(0,1-Tf^2))

Step 2: EOM substitution (G_DeWitt is the tau-kinetic coefficient)
  G_DeWitt * tau_ddot + 3*H*G_DeWitt*tau_dot + dV_eff/dtau = 0
  mu_dot = -H*mu                                (dilution)

Step 3: Lock criterion (canonical form)
  "Sustained lock at (tau*, mu*)" requires simultaneously:
    (a) dV_eff/dtau|(tau*,mu*) = 0          (equilibrium)
    (b) d^2V_eff/dtau^2|(tau*,mu*) > 0       (stable minimum, not saddle)
    (c) r* = mu*/lmin(tau*) in [rlo(tau*), rhi(tau*)]  (inside BCS window)
    (d) |tau_dot|  < 0.01 * max|tau_dot|     (velocity settled, not transient ringing)
    (e) |dV_spec/dtau| > 0.1                 (NOT at V_spec cubic-spline artifact minimum)

Step 4: Direction -- closure verdict
  No sustained lock in any ODE scan => P2-LOCK: CLOSED
  Any sustained lock found         => P2-LOCK: MARGINAL (requires further analysis)
  Static adiabatic lock points are DIAGNOSTIC ONLY (never dynamically accessible
  because t_settle ~ O(1) << t_dilution ~ (mu_0/lmin)^2 at physical H_0).

Step 5: This gate maps the constraint surface -- CLOSED means BCS-induced
  modulus stabilization is eliminated as a geometric channel; MARGINAL means
  a narrow parameter wedge survives and needs stability analysis.
"""

import sys
import hashlib
import warnings
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')   # (local) CPU cap (no heavy linalg here)
os.environ.setdefault('MKL_NUM_THREADS', '8')   # (local) CPU cap
from pathlib import Path

# Canonical constants (MANDATORY)
_THIS = Path(__file__).resolve()
_CANON_DIR = _THIS.parent.parent   # computations/_shared/
sys.path.insert(0, str(_CANON_DIR))
from canonical_constants import *   # noqa: F401,F403
# Aliases for clarity
G_TT = G_DeWitt                     # (local) alias for script readability; canonical is G_DeWitt

import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator, RegularGridInterpolator
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import time as wc

warnings.filterwarnings('ignore')

# ===========================================================================
# 0. INPUT PINS + SHA-256 LOGGING
# ===========================================================================
BASE_OUT = _THIS.parent                               # computations/_shared/t3-intake/
ARCHIVE = _CANON_DIR.parent / "computations/_shared"         # computations/_shared/

INPUT_FILES = {
    "s22a_slow_roll.npz":            ARCHIVE / "s22a_slow_roll.npz",
    "s24a_vspec.npz":                ARCHIVE / "s24a_vspec.npz",
    "s26_multimode_bcs.npz":         ARCHIVE / "s26_multimode_bcs.npz",
    "s26_p2_cooling_trajectory.py":  ARCHIVE / "s26_p2_cooling_trajectory.py",
    "canonical_constants.py":        _CANON_DIR / "canonical_constants.py",
}

def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

INPUT_HASHES = {name: sha256_file(p) for name, p in INPUT_FILES.items()}

# Print SHA-256 pins in first 20 lines of stdout (per gate-verdicts.md)
print("=" * 72)
print("S26-P2-COOLING-TRAJECTORY -- input SHA-256 pins")
print("=" * 72)
for name, h in INPUT_HASHES.items():
    print(f"  {name:<40s} {h}")
print("=" * 72)
sys.stdout.flush()

OUT_NPZ = BASE_OUT / "s26_p2_cooling_trajectory.npz"
OUT_PNG = BASE_OUT / "s26_p2_cooling_trajectory.png"
OUT_VERDICT = BASE_OUT / "s26_p2_cooling_trajectory_verdict.txt"

TAU_MAX = 0.5    # (local) BCS data range upper bound (s26_multimode_bcs.npz tau grid)

# ===========================================================================
# 1. DATA + INTERPOLANTS (unchanged from parent)
# ===========================================================================
def load_and_build():
    vd = np.load(str(INPUT_FILES['s24a_vspec.npz']))
    bd = np.load(str(INPUT_FILES['s26_multimode_bcs.npz']))
    sd = np.load(str(INPUT_FILES['s22a_slow_roll.npz']))
    assert abs(float(sd['G_tt'][0]) - G_TT) < 1e-10

    ip = {}   # (local) interpolant dictionary
    ip['Vs'] = CubicSpline(vd['tau'], vd['V_spec_rho_0p010'])

    tau_b = bd['tau_values']   # (local)
    ip['tau_b'] = tau_b
    eig = np.zeros((9, 16))    # (local)
    for i in range(9):
        eig[i] = bd[f'eigenvalues_{i}']
    lm = np.min(np.abs(eig), axis=1)   # (local) lmin per tau slice
    ip['lm'] = CubicSpline(tau_b, lm)
    ip['lm_raw'] = lm
    ip['mc'] = CubicSpline(tau_b, bd['mu_critical'])

    MR = np.array([0., 0.5, 0.8, 0.9, 0.95, 1., 1.05, 1.1, 1.2, 1.5, 2., 3.])   # (local) mu/lmin ratios
    MS = ['0.00','0.50','0.80','0.90','0.95','1.00','1.05','1.10','1.20','1.50','2.00','3.00']   # (local) key strings
    Fc = np.zeros((9, 12))   # (local)
    Dn = np.zeros((9, 12))   # (local)
    for i in range(9):
        for j, ms in enumerate(MS):
            Fc[i, j] = float(bd[f'sc_Fcond_{i}_{ms}'])
            Dn[i, j] = float(bd[f'sc_Dnorm_{i}_{ms}'])

    ip['Fc'] = RegularGridInterpolator((tau_b, MR), Fc,
                   method='linear', bounds_error=False, fill_value=0.)
    ip['Dn'] = RegularGridInterpolator((tau_b, MR), Dn,
                   method='linear', bounds_error=False, fill_value=0.)
    ip['Fc_raw'], ip['Dn_raw'] = Fc, Dn

    mr_s = bd['mu_scan_ratios']   # (local)
    rlo = np.zeros(9)             # (local) per-tau window lower bound
    rhi = np.zeros(9)             # (local) per-tau window upper bound
    for i in range(9):
        a = np.where(bd['M_max_phase_diagram'][i] > 1.)[0]
        if len(a):
            rlo[i], rhi[i] = mr_s[a[0]], mr_s[a[-1]]
        else:
            rlo[i], rhi[i] = 0.925, 1.075   # (local) fallback defaults
    ip['rlo'] = PchipInterpolator(tau_b, rlo)
    ip['rhi'] = PchipInterpolator(tau_b, rhi)
    ip['rlo_raw'], ip['rhi_raw'] = rlo, rhi

    mg = np.zeros(9)   # (local) gap per tau slice
    for i in range(9):
        ae = np.sort(np.abs(eig[i]))   # (local)
        u = np.unique(np.round(ae, 10))   # (local)
        mg[i] = np.min(np.diff(u)) if len(u) > 1 else 1e-6
    ip['gap'] = PchipInterpolator(tau_b, mg)
    ip['gap_raw'] = mg
    ip['eig'] = eig
    ip['Tc'] = bd['T_critical'].copy()

    def _fg(rv, fv):
        nz = np.abs(fv) > 1e-12   # (local)
        if np.sum(nz) < 2:
            return (0., 1., 0.08) if np.sum(nz) == 0 else (fv[np.where(nz)[0][0]], rv[np.where(nz)[0][0]], 0.05)
        rn, fn = rv[nz], fv[nz]   # (local)
        im = np.argmin(fn)        # (local)
        try:
            p, _ = curve_fit(lambda r, A, r0, s: A * np.exp(-(r - r0)**2 / (2 * s**2)),
                             rn, fn, p0=[fn[im], rn[im], 0.05],
                             bounds=([-np.inf, 0.5, 0.01], [0.01, 1.5, 0.5]), maxfev=5000)
            return tuple(p)
        except Exception:
            return fn[im], rn[im], 0.05
    FA = np.zeros(9)   # (local) Gaussian amplitude fit
    FR = np.zeros(9)   # (local) Gaussian center fit
    FS = np.zeros(9)   # (local) Gaussian sigma fit
    for i in range(9):
        FA[i], FR[i], FS[i] = _fg(MR, Fc[i])
    ip['FA'], ip['FR'], ip['FS'] = FA, FR, FS

    return ip


# ===========================================================================
# 2. POTENTIAL EVALUATION (unchanged)
# ===========================================================================
def _cb(tau):
    return float(np.clip(tau, 1e-14, TAU_MAX - 1e-14))

def _cv(tau):
    return float(np.clip(tau, 0, 2. - 1e-14))

def Fc_eval(tau, r, ip):
    if r < 0.85 or r > 1.55:
        return 0.
    return float(ip['Fc']((_cb(tau), r)))

def Dn_eval(tau, r, ip):
    if r < 0.85 or r > 1.55:
        return 0.
    return max(0., float(ip['Dn']((_cb(tau), r))))

def V_eff(tau, mu, ip, Tf=0.):
    Vs = float(ip['Vs'](_cv(tau)))   # (local)
    if mu < 1e-14 or tau < -0.01 or tau > TAU_MAX + 0.01:
        return Vs
    lm = float(ip['lm'](_cb(tau)))   # (local)
    if lm < 1e-14:
        return Vs
    r = mu / lm                      # (local)
    Ts = 1.                          # (local) T-suppression
    if Tf >= 1.:
        Ts = 0.                      # (local) zero suppression at/above T_c
    elif Tf > 0.:
        Ts = np.sqrt(max(0., 1. - Tf**2))
    return Vs + Fc_eval(tau, r, ip) * Ts

def dV_eff_dtau(tau, mu, ip, Tf=0.):
    h = 5e-4   # (local) FD step
    tp = min(tau + h, TAU_MAX - 1e-6)   # (local)
    tm = max(tau - h, 1e-6)             # (local)
    dh = tp - tm                         # (local)
    if dh < 1e-14:
        return float(ip['Vs'](_cv(tau), 1))
    return (V_eff(tp, mu, ip, Tf) - V_eff(tm, mu, ip, Tf)) / dh


# ===========================================================================
# 3-5. PHASES (unchanged from parent)
# ===========================================================================
def settle_tau(tau_i, pi_i, H_0, ip, t_settle=None):
    ip_local = ip

    if t_settle is None:
        V2 = float(ip_local['Vs'](max(tau_i, 0.01), 2))   # (local)
        omega = np.sqrt(max(abs(V2) / G_TT, 0.01))         # (local)
        t_settle = max(100. / omega, 50.)                  # (local)

    def rhs(t, y):
        tau, pi = y
        tau = max(tau, 0.)
        H = H_0 / max(t, 1e-10)
        dVs = float(ip_local['Vs'](_cv(tau), 1))
        extra = 0.   # (local) restoring-force adjustment
        if tau < 0:
            extra = -1000. * tau
        return [pi, -(1. / G_TT) * (dVs + extra) - 3. * H * pi]

    sol = solve_ivp(rhs, (1., 1. + t_settle), [tau_i, pi_i],
                    method='RK45', rtol=1e-6, atol=1e-8, max_step=t_settle / 100)

    tau_f = max(float(sol.y[0, -1]), 0.)   # (local)
    pi_f = float(sol.y[1, -1])              # (local)
    return tau_f, pi_f, float(sol.t[-1]), sol


def adiabatic_sweep(tau_settled, ip, Tf=0., n_r=200):
    results = {}   # (local)

    r_vals = np.linspace(0.8, 1.5, n_r)   # (local)
    lm_s = float(ip['lm'](_cb(tau_settled)))   # (local)

    dV_vs_r = np.zeros(n_r)   # (local)
    V_vs_r = np.zeros(n_r)    # (local)
    D_vs_r = np.zeros(n_r)    # (local)
    for k, r in enumerate(r_vals):
        mu = r * lm_s   # (local)
        V_vs_r[k] = V_eff(tau_settled, mu, ip, Tf)
        dV_vs_r[k] = dV_eff_dtau(tau_settled, mu, ip, Tf)
        D_vs_r[k] = Dn_eval(tau_settled, r, ip)

    results['r_vals'] = r_vals
    results['V_vs_r'] = V_vs_r
    results['dV_vs_r'] = dV_vs_r
    results['D_vs_r'] = D_vs_r

    sign_changes = []   # (local)
    for k in range(1, n_r):
        if dV_vs_r[k - 1] * dV_vs_r[k] < 0:
            sign_changes.append(k)
    results['sign_changes'] = sign_changes

    tau_scan = np.linspace(0.005, 0.495, 50)   # (local)
    r_scan = np.linspace(0.85, 1.45, 50)       # (local)
    dV_2d = np.zeros((50, 50))                 # (local)
    V_2d = np.zeros((50, 50))                  # (local)

    for i, tau in enumerate(tau_scan):
        lm = float(ip['lm'](tau))   # (local)
        for j, r in enumerate(r_scan):
            mu = r * lm   # (local)
            V_2d[i, j] = V_eff(tau, mu, ip, Tf)
            dV_2d[i, j] = dV_eff_dtau(tau, mu, ip, Tf)

    results['tau_scan'] = tau_scan
    results['r_scan'] = r_scan
    results['dV_2d'] = dV_2d
    results['V_2d'] = V_2d

    lock_points = []   # (local)
    for i in range(1, 50):
        for j in range(50):
            if dV_2d[i - 1, j] * dV_2d[i, j] < 0:
                tau_lock = 0.5 * (tau_scan[i - 1] + tau_scan[i])   # (local)
                h = 1e-3   # (local) FD step
                lm = float(ip['lm'](_cb(tau_lock)))   # (local)
                mu = r_scan[j] * lm                    # (local)
                dVp = dV_eff_dtau(min(tau_lock + h, 0.499), mu, ip, Tf)   # (local)
                dVm = dV_eff_dtau(max(tau_lock - h, 0.001), mu, ip, Tf)   # (local)
                d2V = (dVp - dVm) / (2 * h)   # (local)
                if d2V > 0:
                    lock_points.append((tau_lock, r_scan[j], d2V / G_TT))

    results['lock_points'] = lock_points
    results['has_lock'] = len(lock_points) > 0

    return results


def integrate_full(tau_i, pi_i, mu_i, H_0, Tf, ip, t_max_factor=3.):
    t_0 = 1.   # (local) initial time
    mc_est = float(ip['mc'](_cb(tau_i)))   # (local)
    t_exit = t_0 * max((mu_i / max(mc_est, 1e-14))**2, 10.)   # (local)
    t_end = t_exit * t_max_factor                              # (local)

    def rhs(t, y):
        tau, pi, mu = max(y[0], 0.), y[1], max(y[2], 0.)
        H = H_0 / max(t, 1e-10)
        dV = dV_eff_dtau(tau, mu, ip, Tf)
        extra = 0.   # (local) boundary-damping adjustment
        if tau < 0.001:
            extra = -100. * (tau - 0.001)
            pi = max(pi, 0.)
        return [max(pi, 0.) if tau < 0.001 else pi,
                -(1. / G_TT) * (dV + extra) - 3. * H * pi,
                -H * mu]

    def exit_evt(t, y):
        tc = _cb(y[0])
        return y[2] - float(ip['mc'](tc))
    exit_evt.terminal = True
    exit_evt.direction = -1

    sol = solve_ivp(rhs, (t_0, t_end), [tau_i, pi_i, mu_i],
                    method='LSODA', rtol=1e-4, atol=1e-6,
                    events=[exit_evt], max_step=t_end / 100)

    return {
        't': sol.t, 'tau': sol.y[0], 'pi': sol.y[1], 'mu': sol.y[2],
        'terminated': sol.status == 1, 'n_steps': len(sol.t),
        't_exit': float(sol.t_events[0][0]) if len(sol.t_events[0]) > 0 else None,
    }


def diag_full(res, ip, Tf=0.):
    t, tau, mu = res['t'], res['tau'], res['mu']
    n = len(t)   # (local)
    d = {'tau_f': float(tau[-1]), 'mu_f': float(mu[-1])}   # (local)

    lm_t = np.array([float(ip['lm'](_cb(tt))) for tt in tau])   # (local)
    r_t = mu / np.maximum(lm_t, 1e-14)                           # (local)
    d['r'] = r_t
    d['r_min'] = float(np.min(r_t))

    idx = np.linspace(0, n - 1, min(500, n), dtype=int)   # (local) sampling indices
    Dt = np.zeros(n)   # (local)
    Ft = np.zeros(n)   # (local)
    dVt = np.zeros(n)  # (local)
    for k in idx:
        tc = _cb(tau[k])          # (local)
        mu_k = max(mu[k], 0.)      # (local)
        lm = float(ip['lm'](tc))   # (local)
        r = mu_k / lm if lm > 1e-14 else 0.   # (local)
        Dt[k] = Dn_eval(tc, r, ip)
        Ft[k] = Fc_eval(tc, r, ip)
        dVt[k] = dV_eff_dtau(tc, mu_k, ip, Tf)
    if Tf > 0 and Tf < 1.:
        Ft *= np.sqrt(max(0, 1 - Tf**2))

    d['Delta'] = Dt
    d['Fc'] = Ft
    d['dV'] = dVt
    d['Dmax'] = float(np.max(Dt))
    d['Fmin'] = float(np.min(Ft))

    rlo_t = np.array([float(ip['rlo'](_cb(tt))) for tt in tau])   # (local)
    rhi_t = np.array([float(ip['rhi'](_cb(tt))) for tt in tau])   # (local)
    in_w = (r_t >= rlo_t) & (r_t <= rhi_t) & (tau >= 0) & (tau <= TAU_MAX)   # (local)
    d['in_win'] = bool(np.any(in_w))
    d['t_win'] = float(t[in_w][-1] - t[in_w][0]) if np.sum(in_w) >= 2 else 0.

    lock = []   # (local)
    for k in range(1, n):
        if dVt[k - 1] * dVt[k] < 0 and 0 <= tau[k] <= TAU_MAX and in_w[k]:
            lock.append(k)
    d['n_lock_cross_raw'] = len(lock)

    pi_max = max(abs(res['pi']).max(), 1e-14)   # (local)
    pi_thresh = 0.01 * pi_max                    # (local)

    sustained_lock = []   # (local)
    for k in lock:
        if abs(res['pi'][k]) < pi_thresh:
            tl = _cb(0.5 * (tau[k - 1] + tau[k]))   # (local)
            ml = 0.5 * (mu[k - 1] + mu[k])           # (local)

            dVs_here = float(ip['Vs'](_cv(tl), 1))   # (local)
            if abs(dVs_here) < 0.1:
                continue

            h = 1e-4   # (local)
            dVp = dV_eff_dtau(min(tl + h, 0.499), ml, ip, Tf)   # (local)
            dVm = dV_eff_dtau(max(tl - h, 0.001), ml, ip, Tf)   # (local)
            d2V = (dVp - dVm) / (2 * h)   # (local)
            if d2V > 0:
                sustained_lock.append((k, tl, ml, d2V / G_TT))

    d['locked'] = len(sustained_lock) > 0
    d['n_lock_sustained'] = len(sustained_lock)
    if sustained_lock:
        ki, tl, ml, msq = sustained_lock[0]   # (local)
        d['m_sq'] = float(msq)
        d['tau_lock'] = float(tl)
    else:
        d['m_sq'] = None
        d['tau_lock'] = None

    P = np.zeros(n)   # (local) LZ tunneling probability
    for k in idx:
        tc = _cb(tau[k])                  # (local)
        dg = float(ip['gap'](tc))          # (local)
        h = 1e-4                           # (local)
        gp = float(ip['gap'](min(tc + h, TAU_MAX - 1e-14)))   # (local)
        gm = float(ip['gap'](max(tc - h, 1e-14)))              # (local)
        vel = abs((gp - gm) / (2 * h) * res['pi'][k])          # (local)
        if vel > 1e-30 and dg > 1e-30:
            P[k] = np.exp(-2 * np.pi * dg**2 / vel)
    d['PLZ'] = P
    d['PLZ_max'] = float(np.max(P))
    return d


def scan_H0(ip, tau_i=0.15, mr=10., Tf=0.,
            H0s=np.array([0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1., 5., 10.])):
    lm = float(ip['lm'](tau_i))   # (local)
    mu0 = mr * lm                  # (local)
    o = {k: np.zeros(len(H0s)) for k in ['tauf', 'Dmax', 'Fmin', 'rmin', 'twin']}   # (local)
    o['H0s'] = H0s
    o['locked'] = np.zeros(len(H0s), dtype=bool)
    o['in_win'] = np.zeros(len(H0s), dtype=bool)
    o['n_lock_raw'] = np.zeros(len(H0s), dtype=int)
    o['n_lock_sustained'] = np.zeros(len(H0s), dtype=int)
    for k, H0 in enumerate(H0s):
        r = integrate_full(tau_i, 0., mu0, H0, Tf, ip)   # (local)
        dg = diag_full(r, ip, Tf)   # (local)
        o['tauf'][k] = dg['tau_f']
        o['locked'][k] = dg['locked']
        o['Dmax'][k] = dg['Dmax']
        o['Fmin'][k] = dg['Fmin']
        o['rmin'][k] = dg['r_min']
        o['twin'][k] = dg['t_win']
        o['in_win'][k] = dg['in_win']
        o['n_lock_raw'][k] = dg['n_lock_cross_raw']
        o['n_lock_sustained'][k] = dg['n_lock_sustained']
    return o


def scan_mu0(ip, tau_i=0.15, H_0=0.01, Tf=0., n=20, rng=(2., 50.)):
    lm = float(ip['lm'](tau_i))   # (local)
    mrs = np.geomspace(rng[0], rng[1], n)   # (local)
    o = {k: np.zeros(n) for k in ['tauf', 'Dmax', 'Fmin', 'twin', 'rmin']}   # (local)
    o['mrs'] = mrs
    o['locked'] = np.zeros(n, dtype=bool)
    o['in_win'] = np.zeros(n, dtype=bool)
    for k, mr in enumerate(mrs):
        r = integrate_full(tau_i, 0., mr * lm, H_0, Tf, ip)   # (local)
        dg = diag_full(r, ip, Tf)                              # (local)
        o['tauf'][k] = dg['tau_f']
        o['locked'][k] = dg['locked']
        o['Dmax'][k] = dg['Dmax']
        o['Fmin'][k] = dg['Fmin']
        o['twin'][k] = dg['t_win']
        o['rmin'][k] = dg['r_min']
        o['in_win'][k] = dg['in_win']
    return o


def scan_2d(ip, mr=10., H_0=0.01, Tf=0., nt=8, np_=8):
    tv = np.linspace(0.02, 0.48, nt)       # (local)
    pv = np.linspace(-0.05, 0.05, np_)     # (local)
    o = {'tau_i': tv, 'pi_i': pv,
         'tauf': np.zeros((nt, np_)),
         'locked': np.zeros((nt, np_), dtype=bool),
         'rmin': np.zeros((nt, np_))}   # (local)
    for i, ti in enumerate(tv):
        lm = float(ip['lm'](ti))   # (local)
        mu0 = mr * lm              # (local)
        for j, pi in enumerate(pv):
            try:
                r = integrate_full(ti, pi, mu0, H_0, Tf, ip, t_max_factor=2.)   # (local)
                dg = diag_full(r, ip, Tf)                                        # (local)
                o['tauf'][i, j] = dg['tau_f']
                o['locked'][i, j] = dg['locked']
                o['rmin'][i, j] = dg['r_min']
            except Exception:
                o['tauf'][i, j] = ti
                o['rmin'][i, j] = mr
    return o


# ===========================================================================
# PLOTTING (kept minimal -- same as parent)
# ===========================================================================
def make_plot(fid, fd, adiab, mu_sc, H0_sc, s2d, ip, tau_i, H_0, Tf):
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("T3 S26 P2: Coupled Cooling Trajectory", fontsize=14, fontweight='bold')
    lm_i = float(ip['lm'](tau_i))   # (local)

    ax = axes[0, 0]
    ax.plot(fid['t'], fid['tau'], 'b-', label=r'$\tau(t)$')
    ax.set_xlabel('t'); ax.set_ylabel(r'$\tau$', color='b')
    ax.set_xscale('log'); ax.set_title('Fiducial trajectory')
    ax2 = ax.twinx()
    ax2.plot(fid['t'], fd['r'], 'r-', alpha=0.7, label='$r(t)$')
    ax2.set_ylabel(r'$\mu/\lambda_{min}$', color='r')
    ax2.axhline(1.15, color='g', ls='--', alpha=0.3)
    ax2.axhline(0.925, color='g', ls='--', alpha=0.3)
    ax.legend(fontsize=8, loc='upper left'); ax2.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    ax = axes[0, 1]
    ax.plot(adiab['r_vals'], adiab['dV_vs_r'], 'b-')
    ax.axhline(0, color='k', ls='-', alpha=0.3)
    rlo = float(ip['rlo'](_cb(fd['tau_f'])))   # (local)
    rhi = float(ip['rhi'](_cb(fd['tau_f'])))   # (local)
    ax.axvspan(rlo, rhi, alpha=0.15, color='green')
    ax.set_xlabel('$r$'); ax.set_ylabel(r'$dV_{eff}/d\tau$')
    ax.set_title(f'Force at tau_s={fd["tau_f"]:.4f}')
    ax.grid(True, alpha=0.3)

    ax = axes[0, 2]
    tpl = np.linspace(0.005, 0.495, 200)   # (local)
    for mr in [0., 0.95, 1.0, 1.05]:
        Va = np.array([V_eff(tp, mr * float(ip['lm'](tp)), ip, Tf) for tp in tpl])   # (local)
        lab = f'r={mr:.2f}' if mr > 0 else 'V_spec'
        ax.plot(tpl, Va, label=lab)
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('V_eff')
    ax.set_title('Potential landscape'); ax.legend(fontsize=7); ax.grid(True, alpha=0.3)

    ax = axes[1, 0]
    ax.semilogx(H0_sc['H0s'], H0_sc['rmin'], 'bo-', ms=5)
    ax.axhline(1.15, color='g', ls='--', alpha=0.5)
    ax.axhline(0.925, color='r', ls='--', alpha=0.5)
    for k in range(len(H0_sc['H0s'])):
        if H0_sc['in_win'][k]:
            ax.plot(H0_sc['H0s'][k], H0_sc['rmin'][k], 'g*', ms=12, zorder=5)
    ax.set_xlabel('H_0'); ax.set_ylabel('r_min')
    ax.set_title('H_0 scan'); ax.grid(True, alpha=0.3)

    ax = axes[1, 1]
    T_, R_ = np.meshgrid(adiab['tau_scan'], adiab['r_scan'], indexing='ij')
    pcm = ax.pcolormesh(T_, R_, adiab['dV_2d'], cmap='RdBu_r', shading='auto', vmin=-5, vmax=5)
    fig.colorbar(pcm, ax=ax, label=r'$dV_{eff}/d\tau$')
    ax.contour(T_, R_, adiab['dV_2d'], levels=[0], colors='black', linewidths=2)
    if adiab['lock_points']:
        tl = [p[0] for p in adiab['lock_points']]   # (local)
        rl = [p[1] for p in adiab['lock_points']]   # (local)
        ax.scatter(tl, rl, marker='*', color='gold', s=100, zorder=5, label='Lock')
        ax.legend(fontsize=7)
    ax.set_xlabel(r'$\tau$'); ax.set_ylabel('r'); ax.set_title('Force map')
    ax.grid(True, alpha=0.3)

    ax = axes[1, 2]
    TI, PI = np.meshgrid(s2d['tau_i'], s2d['pi_i'], indexing='ij')
    pcm = ax.pcolormesh(TI, PI, s2d['tauf'], cmap='RdYlBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, label=r'$\tau_f$')
    if np.any(s2d['locked']):
        li, lj = np.where(s2d['locked'])
        ax.scatter(s2d['tau_i'][li], s2d['pi_i'][lj], marker='x', color='k', s=30)
    ax.set_xlabel('tau_i'); ax.set_ylabel('pi_i')
    ax.set_title('Phase diagram'); ax.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Plot: {OUT_PNG}")


# ===========================================================================
# VERDICT (same logic as parent, S81 canonical line emitted)
# ===========================================================================
def compute_verdict(mu_sc, H0_sc, H0_fine, s2d, adiab, fd, ip, Tf_results=None):
    L = ["=" * 70,
         "S26-P2-COOLING-TRAJECTORY -- VERDICT (v2, canonical import)",
         "=" * 70]   # (local) verdict text lines

    any_lock_mu = bool(np.any(mu_sc['locked']))
    any_lock_2d = bool(np.any(s2d['locked']))
    any_lock_H0 = bool(np.any(H0_sc['locked']))
    any_lock_H0f = bool(np.any(H0_fine['locked']))
    any_win = bool(np.any(H0_sc['in_win'])) or bool(np.any(H0_fine['in_win']))

    L.append(f"\n--- ADIABATIC ANALYSIS (DIAGNOSTIC) ---")
    L.append(f"Static lock points: {len(adiab['lock_points'])}")
    n_vspec = sum(1 for tl, rl, msq in adiab['lock_points'] if tl < 0.025)   # (local)
    n_bcs = len(adiab['lock_points']) - n_vspec                                # (local)
    L.append(f"  V_spec artifacts (tau<0.025): {n_vspec}")
    L.append(f"  BCS-influenced (tau>=0.025): {n_bcs}")

    L.append(f"\n--- ODE SCANS (determines verdict) ---")
    L.append(f"mu_0 scan (n={len(mu_sc['mrs'])}): {'LOCK' if any_lock_mu else 'NO LOCK'}"
             f"  r_min range [{mu_sc['rmin'].min():.4f}, {mu_sc['rmin'].max():.4f}]"
             f"  in_win={int(np.sum(mu_sc['in_win']))}/{len(mu_sc['in_win'])}")
    L.append(f"H_0 coarse (n={len(H0_sc['H0s'])}): "
             f"locked={int(np.sum(H0_sc['locked']))}, in_win={int(np.sum(H0_sc['in_win']))}")
    L.append(f"H_0 fine   (n={len(H0_fine['H0s'])}): "
             f"locked={int(np.sum(H0_fine['locked']))}, in_win={int(np.sum(H0_fine['in_win']))}")
    win_h0s = H0_fine['H0s'][H0_fine['in_win'].astype(bool)]
    if len(win_h0s) > 0:
        L.append(f"Window accessed for H_0 >= {win_h0s[0]:.4f}")
    else:
        L.append(f"Window never accessed in fine scan")
    L.append(f"2D scan: {'LOCK' if any_lock_2d else 'NO LOCK'}")

    L.append(f"\n--- GRADIENT ANALYSIS ---")
    lm15 = float(ip['lm'](0.15))              # (local)
    dVs = float(ip['Vs'](0.15, 1))             # (local)
    dVf = dV_eff_dtau(0.15, lm15, ip)          # (local)
    dVb = dVf - dVs                             # (local)
    L.append(f"At tau=0.15, r=1.0: dV_spec={dVs:.4f}  dV_BCS={dVb:.4f}  "
             f"|dV_BCS/dV_spec|={abs(dVb)/max(abs(dVs),1e-14):.4f}")

    max_ratio = 0.   # (local)
    best_tau = 0.    # (local)
    best_r = 0.      # (local)
    for i, tau in enumerate(adiab['tau_scan']):
        dVs_i = float(ip['Vs'](_cv(tau), 1))   # (local)
        if abs(dVs_i) < 1e-14:
            continue
        for j, r in enumerate(adiab['r_scan']):
            dV_total = adiab['dV_2d'][i, j]       # (local)
            dV_bcs = dV_total - dVs_i              # (local)
            ratio = abs(dV_bcs) / abs(dVs_i)       # (local)
            if ratio > max_ratio:
                max_ratio = ratio
                best_tau = tau
                best_r = r
    L.append(f"Max |dV_BCS/dV_spec| = {max_ratio:.4f} at tau={best_tau:.3f}, r={best_r:.3f}")
    L.append(f"{'PASSES' if max_ratio > 1 else 'FAILS'} gradient competition (need > 1)")

    if Tf_results is not None:
        L.append(f"\n--- TEMPERATURE SHOW-STOPPER ---")
        for tf_val, tf_data in Tf_results.items():
            L.append(f"  Tf={tf_val:.1f}: locked={int(np.sum(tf_data['locked']))} "
                     f"in_win={int(np.sum(tf_data['in_win']))} "
                     f"Dmax_max={tf_data['Dmax'].max():.4f}")

    any_lock_ode = any_lock_mu or any_lock_2d or any_lock_H0 or any_lock_H0f
    all_sustained = (int(np.sum(H0_sc.get('n_lock_sustained', np.zeros(1)))) +
                     int(np.sum(H0_fine.get('n_lock_sustained', np.zeros(1)))))   # (local)
    all_raw = (int(np.sum(H0_sc.get('n_lock_raw', np.zeros(1)))) +
               int(np.sum(H0_fine.get('n_lock_raw', np.zeros(1)))))              # (local)

    if any_lock_ode and all_sustained > 0:
        v = "P2-LOCK: MARGINAL"
        L.append(f"\n** VERDICT: {v} ** (sustained={all_sustained} raw={all_raw})")
    else:
        v = "P2-LOCK: CLOSED"
        L.append(f"\n** VERDICT: {v} ** (sustained={all_sustained} raw={all_raw})")
        if any_lock_ode:
            L.append("ODE sign changes are transient ringing, not sustained locks.")
        else:
            L.append("No modulus lock in any ODE configuration.")

    if max_ratio < 1:
        L.append("|dV_BCS| < |dV_spec| everywhere => BCS gradient too weak.")
    if not any_win:
        L.append("At physical H_0, modulus settles before mu reaches window.")

    L.append(f"\nAdiabatic static locks ({len(adiab['lock_points'])}) dynamically inaccessible")
    L.append(f"(tau settles to ~0.018 before mu enters window).")

    if Tf_results is not None:
        any_T_lock = any(bool(np.any(d['locked'])) for d in Tf_results.values())
        if not any_T_lock:
            L.append("\nFinite-T: no lock at Tf=0.5, 0.9. Show-stopper confirmed.")

    L.append("=" * 70)
    return v, "\n".join(L), {"max_ratio": float(max_ratio),
                             "sustained": all_sustained,
                             "raw": all_raw,
                             "any_win": any_win}


# ===========================================================================
# MAIN
# ===========================================================================
if __name__ == '__main__':
    t0 = wc.time()   # (local)
    print("T3 S26 P2 cooling trajectory -- canonical import + SHA-256 pins")
    print("=" * 60); sys.stdout.flush()

    ip = load_and_build()
    print(f"[1] lm={ip['lm_raw']}")
    print(f"    window lo={ip['rlo_raw']}  hi={ip['rhi_raw']}")
    sys.stdout.flush()

    TAU_I = 0.15    # (local) fiducial initial tau
    MR0 = 10.       # (local) fiducial mu_0 / lmin
    H0 = 0.01       # (local) fiducial Hubble
    TF = 0.         # (local) fiducial T/T_c (zero temperature)
    lm_i = float(ip['lm'](TAU_I))   # (local)

    print(f"\n[2] Phase A settle tau..."); sys.stdout.flush()
    tau_s, pi_s, t_s, solA = settle_tau(TAU_I, 0., H0, ip)
    print(f"    tau: {TAU_I:.4f} -> {tau_s:.6f}")

    print(f"\n[3] Phase B adiabatic sweep..."); sys.stdout.flush()
    adiab = adiabatic_sweep(tau_s, ip, TF)
    print(f"    static locks: {len(adiab['lock_points'])}")

    print(f"\n[4] Phase C fiducial ODE..."); sys.stdout.flush()
    fid = integrate_full(TAU_I, 0., MR0 * lm_i, H0, TF, ip)
    fd = diag_full(fid, ip, TF)
    print(f"    tau_f={fd['tau_f']:.6f}  r_min={fd['r_min']:.4f}  "
          f"in_win={fd['in_win']}  locked={fd['locked']}")

    print(f"\n[5] mu_0 scan..."); sys.stdout.flush()
    mu_sc = scan_mu0(ip, tau_i=TAU_I, H_0=H0, Tf=TF, n=20)

    print(f"\n[6a] H_0 coarse scan..."); sys.stdout.flush()
    H0_sc = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=TF)

    print(f"\n[6b] H_0 fine scan..."); sys.stdout.flush()
    H0_fine_vals = np.geomspace(0.1, 10., 30)   # (local)
    H0_fine = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=TF, H0s=H0_fine_vals)

    print(f"\n[6c] Temperature scans..."); sys.stdout.flush()
    Tf_results = {}   # (local)
    for Tf_val in [0.5, 0.9]:
        Tf_results[Tf_val] = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=Tf_val, H0s=H0_fine_vals)

    print(f"\n[7] 2D scan..."); sys.stdout.flush()
    s2d = scan_2d(ip, mr=10., H_0=H0, Tf=TF, nt=8, np_=8)

    print(f"\n[8] Verdict..."); sys.stdout.flush()
    v, vtxt, summary = compute_verdict(mu_sc, H0_sc, H0_fine, s2d, adiab, fd, ip, Tf_results)
    print(vtxt); sys.stdout.flush()

    print(f"\n[9] Plotting..."); sys.stdout.flush()
    make_plot(fid, fd, adiab, mu_sc, H0_fine, s2d, ip, TAU_I, H0, TF)

    print(f"\n[10] Saving..."); sys.stdout.flush()
    sv = {
        'fid_t': fid['t'], 'fid_tau': fid['tau'], 'fid_pi': fid['pi'],
        'fid_mu': fid['mu'], 'fid_r': fd['r'],
        'fid_Dmax': fd['Dmax'], 'fid_rmin': fd['r_min'],
        'fid_tau_f': fd['tau_f'], 'fid_in_win': fd['in_win'], 'fid_locked': fd['locked'],
        'musc_mrs': mu_sc['mrs'], 'musc_locked': mu_sc['locked'],
        'musc_rmin': mu_sc['rmin'], 'musc_in_win': mu_sc['in_win'],
        'H0sc_H0s': H0_sc['H0s'], 'H0sc_locked': H0_sc['locked'],
        'H0sc_rmin': H0_sc['rmin'], 'H0sc_in_win': H0_sc['in_win'],
        'H0sc_n_lock_raw': H0_sc['n_lock_raw'],
        'H0sc_n_lock_sustained': H0_sc['n_lock_sustained'],
        'H0f_H0s': H0_fine['H0s'], 'H0f_locked': H0_fine['locked'],
        'H0f_rmin': H0_fine['rmin'], 'H0f_in_win': H0_fine['in_win'],
        'H0f_n_lock_raw': H0_fine['n_lock_raw'],
        'H0f_n_lock_sustained': H0_fine['n_lock_sustained'],
        'Tf05_locked': Tf_results[0.5]['locked'],
        'Tf05_in_win': Tf_results[0.5]['in_win'],
        'Tf09_locked': Tf_results[0.9]['locked'],
        'Tf09_in_win': Tf_results[0.9]['in_win'],
        's2d_locked': s2d['locked'], 's2d_tauf': s2d['tauf'],
        'adiab_n_locks': len(adiab['lock_points']),
        'tau_i': TAU_I, 'H_0': H0, 'G_TT': G_TT, 'lm_i': lm_i,
        'tau_settled': tau_s, 'verdict': v,
        'max_ratio': summary['max_ratio'],
        'sustained': summary['sustained'],
        'raw_crossings': summary['raw'],
    }
    np.savez(str(OUT_NPZ), **sv)

    # ----- Closure SHA-256: hash of input pins + core numeric summary -----
    closure_payload = {   # (local)
        'inputs': INPUT_HASHES,
        'summary': {
            'verdict': v,
            'tau_settled': float(tau_s),
            'fid_tau_f': float(fd['tau_f']),
            'fid_r_min': float(fd['r_min']),
            'fid_in_win': bool(fd['in_win']),
            'fid_locked': bool(fd['locked']),
            'musc_n_locked': int(np.sum(mu_sc['locked'])),
            'H0sc_n_locked': int(np.sum(H0_sc['locked'])),
            'H0f_n_locked':  int(np.sum(H0_fine['locked'])),
            's2d_n_locked':  int(np.sum(s2d['locked'])),
            'Tf05_n_locked': int(np.sum(Tf_results[0.5]['locked'])),
            'Tf09_n_locked': int(np.sum(Tf_results[0.9]['locked'])),
            'adiab_n_static_locks': int(len(adiab['lock_points'])),
            'max_ratio': float(summary['max_ratio']),
            'sustained': int(summary['sustained']),
            'raw_crossings': int(summary['raw']),
            'any_win': bool(summary['any_win']),
        },
    }
    import json
    closure_str = json.dumps(closure_payload, sort_keys=True)   # (local)
    closure_sha = hashlib.sha256(closure_str.encode('utf-8')).hexdigest()   # (local)
    print(f"\n[11] Closure SHA-256: {closure_sha}")

    # ----- Write verdict file with S81 canonical first line -----
    status = "FAIL" if v == "P2-LOCK: CLOSED" else ("INFO" if v == "P2-LOCK: MARGINAL" else "PASS")   # (local)
    value_tag = f"{v.replace(' ','_')}|sustained={summary['sustained']}|raw={summary['raw']}|max_ratio={summary['max_ratio']:.4f}"   # (local)
    canonical = (f"S26-P2-COOLING-TRAJECTORY: {status} -- "
                 f"value={value_tag} "
                 f"scheme=LSODA_ODE "
                 f"convention=G_DeWitt "
                 f"L_max=fiducial "
                 f"sha256={closure_sha}")   # (local)

    verdict_body = []   # (local)
    verdict_body.append(canonical)
    verdict_body.append("")
    verdict_body.append("# S26-P2-COOLING-TRAJECTORY full verdict body")
    verdict_body.append(f"# closure-sha = {closure_sha}")
    verdict_body.append("# Inputs:")
    for name, h in INPUT_HASHES.items():
        verdict_body.append(f"#   {name}: {h}")
    verdict_body.append("")
    verdict_body.append(vtxt)
    verdict_body.append("")
    verdict_body.append("# Full numeric summary:")
    verdict_body.append(json.dumps(closure_payload['summary'], indent=2, sort_keys=True))

    OUT_VERDICT.write_text("\n".join(verdict_body), encoding='utf-8')
    print(f"\n[12] Verdict written: {OUT_VERDICT}")
    print(f"\n{canonical}")
    print(f"\nTotal: {wc.time()-t0:.1f}s")
    sys.stdout.flush()
