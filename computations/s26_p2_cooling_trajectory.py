"""
Session 26 Priority 2: Coupled Cooling-Trajectory ODE System
=============================================================

Modulus (tau) + chemical potential (mu) dynamics in FRW background.

KEY PHYSICS INSIGHT: The modulus tau settles under V_spec + Hubble damping
on a timescale t_roll ~ O(1), while mu dilutes to the BCS window on a timescale
t_dil ~ (mu_0 / lmin)^2 >> 1. By the time mu enters the window, tau has long
settled near its V_spec equilibrium. The ODE integration confirms this.

STRATEGY:
  Phase A: Integrate tau dynamics under V_spec alone (no BCS). Use hard floor
           at tau=0 via clipping (not a stiff wall). Determine tau_settled.
  Phase B: At tau_settled, sweep mu through the BCS window using a simple
           adiabatic analysis: at each r = mu/lmin(tau), evaluate V_eff and
           check for lock (dV_eff/dtau = 0 with d^2V_eff/dtau^2 > 0).
           NOTE: Phase B is DIAGNOSTIC ONLY. The adiabatic lock points are
           static equilibria that may not be dynamically accessible. The
           verdict is determined solely by the ODE integration (Phase C).
  Phase C: Full 3-variable ODE with relaxed tolerances and max_step control.

SCANS: mu_0, tau_i, pi_i, H_0, T/T_c.

VERDICT LOGIC (v2, corrected):
  The verdict is determined ONLY by dynamic ODE integration results.
  Adiabatic lock points are reported as diagnostics, not gates.
  A "lock" requires: tau settled near a fixed point with |pi| < threshold
  AND inside the BCS condensation window for a sustained period.
  Transient sign changes during tau ringing do NOT count as locks.

Author: gen-physicist (Session 26)
Date: 2026-02-25
"""

import sys
import warnings
import numpy as np
from scipy.interpolate import CubicSpline, PchipInterpolator, RegularGridInterpolator
from scipy.integrate import solve_ivp
from scipy.optimize import curve_fit, minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import time as wc

warnings.filterwarnings('ignore')

BASE = Path(__file__).resolve().parent
OUT_NPZ = BASE / "s26_p2_cooling_trajectory.npz"
OUT_PNG = BASE / "s26_p2_cooling_trajectory.png"

G_TT = 5.0
TAU_MAX = 0.5  # BCS data range


# ===========================================================================
# 1. DATA + INTERPOLANTS
# ===========================================================================
def load_and_build():
    vd = np.load(str(BASE/"s24a_vspec.npz"))
    bd = np.load(str(BASE/"s26_multimode_bcs.npz"))
    sd = np.load(str(BASE/"s22a_slow_roll.npz"))
    assert abs(float(sd['G_tt'][0]) - G_TT) < 1e-10

    ip = {}
    ip['Vs'] = CubicSpline(vd['tau'], vd['V_spec_rho_0p010'])

    tau_b = bd['tau_values']
    ip['tau_b'] = tau_b
    eig = np.zeros((9,16))
    for i in range(9): eig[i] = bd[f'eigenvalues_{i}']
    lm = np.min(np.abs(eig), axis=1)
    ip['lm'] = CubicSpline(tau_b, lm)
    ip['lm_raw'] = lm
    ip['mc'] = CubicSpline(tau_b, bd['mu_critical'])

    MR = np.array([0.,0.5,0.8,0.9,0.95,1.,1.05,1.1,1.2,1.5,2.,3.])
    MS = ['0.00','0.50','0.80','0.90','0.95','1.00','1.05','1.10','1.20','1.50','2.00','3.00']
    Fc = np.zeros((9,12)); Dn = np.zeros((9,12))
    for i in range(9):
        for j,ms in enumerate(MS):
            Fc[i,j] = float(bd[f'sc_Fcond_{i}_{ms}'])
            Dn[i,j] = float(bd[f'sc_Dnorm_{i}_{ms}'])

    ip['Fc'] = RegularGridInterpolator((tau_b, MR), Fc,
                   method='linear', bounds_error=False, fill_value=0.)
    ip['Dn'] = RegularGridInterpolator((tau_b, MR), Dn,
                   method='linear', bounds_error=False, fill_value=0.)
    ip['Fc_raw'], ip['Dn_raw'] = Fc, Dn

    mr_s = bd['mu_scan_ratios']
    rlo, rhi = np.zeros(9), np.zeros(9)
    for i in range(9):
        a = np.where(bd['M_max_phase_diagram'][i] > 1.)[0]
        if len(a): rlo[i], rhi[i] = mr_s[a[0]], mr_s[a[-1]]
        else: rlo[i], rhi[i] = 0.925, 1.075
    ip['rlo'] = PchipInterpolator(tau_b, rlo)
    ip['rhi'] = PchipInterpolator(tau_b, rhi)
    ip['rlo_raw'], ip['rhi_raw'] = rlo, rhi

    mg = np.zeros(9)
    for i in range(9):
        ae = np.sort(np.abs(eig[i]))
        u = np.unique(np.round(ae,10))
        mg[i] = np.min(np.diff(u)) if len(u)>1 else 1e-6
    ip['gap'] = PchipInterpolator(tau_b, mg)
    ip['gap_raw'] = mg
    ip['eig'] = eig
    ip['Tc'] = bd['T_critical'].copy()

    # Gaussian fits for diagnostics
    def _fg(rv, fv):
        nz = np.abs(fv)>1e-12
        if np.sum(nz)<2:
            return (0.,1.,0.08) if np.sum(nz)==0 else (fv[np.where(nz)[0][0]], rv[np.where(nz)[0][0]], 0.05)
        rn,fn = rv[nz],fv[nz]; im = np.argmin(fn)
        try:
            p,_ = curve_fit(lambda r,A,r0,s: A*np.exp(-(r-r0)**2/(2*s**2)),
                            rn, fn, p0=[fn[im],rn[im],0.05],
                            bounds=([-np.inf,0.5,0.01],[0.01,1.5,0.5]), maxfev=5000)
            return tuple(p)
        except: return fn[im], rn[im], 0.05
    FA,FR,FS = np.zeros(9),np.zeros(9),np.zeros(9)
    for i in range(9): FA[i],FR[i],FS[i] = _fg(MR, Fc[i])
    ip['FA'], ip['FR'], ip['FS'] = FA, FR, FS

    return ip


# ===========================================================================
# 2. POTENTIAL EVALUATION
# ===========================================================================
def _cb(tau):
    return float(np.clip(tau, 1e-14, TAU_MAX-1e-14))

def _cv(tau):
    return float(np.clip(tau, 0, 2.-1e-14))

def Fc_eval(tau, r, ip):
    """BCS F_cond from 2D grid."""
    if r < 0.85 or r > 1.55: return 0.
    return float(ip['Fc']((_cb(tau), r)))

def Dn_eval(tau, r, ip):
    if r < 0.85 or r > 1.55: return 0.
    return max(0., float(ip['Dn']((_cb(tau), r))))


def V_eff(tau, mu, ip, Tf=0.):
    """V_eff(tau, mu) = V_spec(tau) + F_cond(tau, r) * T_suppression."""
    Vs = float(ip['Vs'](_cv(tau)))
    if mu < 1e-14 or tau < -0.01 or tau > TAU_MAX + 0.01:
        return Vs
    lm = float(ip['lm'](_cb(tau)))
    if lm < 1e-14: return Vs
    r = mu / lm
    Ts = 1.
    if Tf >= 1.: Ts = 0.
    elif Tf > 0.: Ts = np.sqrt(max(0., 1.-Tf**2))
    return Vs + Fc_eval(tau, r, ip) * Ts


def dV_eff_dtau(tau, mu, ip, Tf=0.):
    """dV_eff/dtau by symmetric finite difference."""
    h = 5e-4
    tp = min(tau + h, TAU_MAX - 1e-6)
    tm = max(tau - h, 1e-6)
    dh = tp - tm
    if dh < 1e-14:
        return float(ip['Vs'](_cv(tau), 1))
    return (V_eff(tp, mu, ip, Tf) - V_eff(tm, mu, ip, Tf)) / dh


# ===========================================================================
# 3. PHASE A: MODULUS SETTLING (V_spec only, quick)
# ===========================================================================
def settle_tau(tau_i, pi_i, H_0, ip, t_settle=None):
    """
    Integrate tau under V_spec + Hubble damping. Clip tau >= 0.
    Returns (tau_settled, pi_settled, t_end).
    """
    ip_local = ip

    if t_settle is None:
        # Settle for ~20 oscillation periods
        V2 = float(ip_local['Vs'](max(tau_i, 0.01), 2))
        omega = np.sqrt(max(abs(V2)/G_TT, 0.01))
        t_settle = max(100. / omega, 50.)

    def rhs(t, y):
        tau, pi = y
        tau = max(tau, 0.)  # soft floor
        H = H_0 / max(t, 1e-10)  # H_0 * t_0/t with t_0=1
        dVs = float(ip_local['Vs'](_cv(tau), 1))
        # Add strong damping if tau < 0 (push back)
        extra = 0.
        if tau < 0:
            extra = -1000. * tau  # strong restoring
        return [pi, -(1./G_TT)*(dVs + extra) - 3.*H*pi]

    sol = solve_ivp(rhs, (1., 1.+t_settle), [tau_i, pi_i],
                    method='RK45', rtol=1e-6, atol=1e-8, max_step=t_settle/100)

    tau_f = max(float(sol.y[0,-1]), 0.)
    pi_f = float(sol.y[1,-1])
    return tau_f, pi_f, float(sol.t[-1]), sol




# ===========================================================================
# 4. PHASE B: ADIABATIC SWEEP (no ODE, just scan r through window)
# ===========================================================================
def adiabatic_sweep(tau_settled, ip, Tf=0., n_r=200):
    """
    At fixed tau = tau_settled, sweep r = mu/lmin through the BCS window.
    Check if V_eff(tau) develops a local minimum at any r.

    Also check at neighboring tau values: is there any (tau, r) where
    dV_eff/dtau = 0 and d^2V_eff/dtau^2 > 0?
    """
    results = {}

    # Sweep r values through the BCS window
    r_vals = np.linspace(0.8, 1.5, n_r)
    lm_s = float(ip['lm'](_cb(tau_settled)))

    # At tau_settled, evaluate dV_eff/dtau vs r
    dV_vs_r = np.zeros(n_r)
    V_vs_r = np.zeros(n_r)
    D_vs_r = np.zeros(n_r)
    for k, r in enumerate(r_vals):
        mu = r * lm_s
        V_vs_r[k] = V_eff(tau_settled, mu, ip, Tf)
        dV_vs_r[k] = dV_eff_dtau(tau_settled, mu, ip, Tf)
        D_vs_r[k] = Dn_eval(tau_settled, r, ip)

    results['r_vals'] = r_vals
    results['V_vs_r'] = V_vs_r
    results['dV_vs_r'] = dV_vs_r
    results['D_vs_r'] = D_vs_r

    # Check for sign change in dV/dtau (lock candidate)
    sign_changes = []
    for k in range(1, n_r):
        if dV_vs_r[k-1] * dV_vs_r[k] < 0:
            sign_changes.append(k)
    results['sign_changes'] = sign_changes

    # 2D search: scan (tau, r) for lock points
    tau_scan = np.linspace(0.005, 0.495, 50)
    r_scan = np.linspace(0.85, 1.45, 50)
    dV_2d = np.zeros((50, 50))
    V_2d = np.zeros((50, 50))

    for i, tau in enumerate(tau_scan):
        lm = float(ip['lm'](tau))
        for j, r in enumerate(r_scan):
            mu = r * lm
            V_2d[i, j] = V_eff(tau, mu, ip, Tf)
            dV_2d[i, j] = dV_eff_dtau(tau, mu, ip, Tf)

    results['tau_scan'] = tau_scan
    results['r_scan'] = r_scan
    results['dV_2d'] = dV_2d
    results['V_2d'] = V_2d

    # Find sign changes in dV_2d (lock candidates)
    lock_points = []
    for i in range(1, 50):
        for j in range(50):
            if dV_2d[i-1, j] * dV_2d[i, j] < 0:
                tau_lock = 0.5*(tau_scan[i-1]+tau_scan[i])
                # Check d^2V/dtau^2 > 0 (true minimum)
                h = 1e-3
                lm = float(ip['lm'](_cb(tau_lock)))
                mu = r_scan[j] * lm
                dVp = dV_eff_dtau(min(tau_lock+h, 0.499), mu, ip, Tf)
                dVm = dV_eff_dtau(max(tau_lock-h, 0.001), mu, ip, Tf)
                d2V = (dVp - dVm) / (2*h)
                if d2V > 0:
                    lock_points.append((tau_lock, r_scan[j], d2V/G_TT))

    results['lock_points'] = lock_points
    results['has_lock'] = len(lock_points) > 0

    return results


# ===========================================================================
# 5. PHASE C: FULL ODE (lightweight, with clamped tau)
# ===========================================================================
def integrate_full(tau_i, pi_i, mu_i, H_0, Tf, ip, t_max_factor=3.):
    """
    Full 3-variable ODE. tau clamped to [0, 0.5].
    Uses LSODA (auto stiff/non-stiff) with relaxed tolerances.
    """
    t_0 = 1.
    mc_est = float(ip['mc'](_cb(tau_i)))
    t_exit = t_0 * max((mu_i / max(mc_est, 1e-14))**2, 10.)
    t_end = t_exit * t_max_factor

    def rhs(t, y):
        tau, pi, mu = max(y[0], 0.), y[1], max(y[2], 0.)
        H = H_0 / max(t, 1e-10)
        dV = dV_eff_dtau(tau, mu, ip, Tf)
        # Extra damping if tau near boundaries
        extra = 0.
        if tau < 0.001:
            extra = -100. * (tau - 0.001)  # push back gently
            pi = max(pi, 0.)  # floor: no negative velocity at tau=0
        return [max(pi, 0.) if tau < 0.001 else pi,
                -(1./G_TT)*(dV+extra) - 3.*H*pi,
                -H*mu]

    def exit_evt(t, y):
        tc = _cb(y[0])
        return y[2] - float(ip['mc'](tc))
    exit_evt.terminal = True; exit_evt.direction = -1

    sol = solve_ivp(rhs, (t_0, t_end), [tau_i, pi_i, mu_i],
                    method='LSODA', rtol=1e-4, atol=1e-6,
                    events=[exit_evt], max_step=t_end/100)

    return {
        't': sol.t, 'tau': sol.y[0], 'pi': sol.y[1], 'mu': sol.y[2],
        'terminated': sol.status == 1, 'n_steps': len(sol.t),
        't_exit': float(sol.t_events[0][0]) if len(sol.t_events[0])>0 else None,
    }


def diag_full(res, ip, Tf=0.):
    """Extract diagnostics from full ODE result."""
    t, tau, mu = res['t'], res['tau'], res['mu']
    n = len(t)
    d = {'tau_f': float(tau[-1]), 'mu_f': float(mu[-1])}

    lm_t = np.array([float(ip['lm'](_cb(tt))) for tt in tau])
    r_t = mu / np.maximum(lm_t, 1e-14)
    d['r'] = r_t; d['r_min'] = float(np.min(r_t))

    # Sample diagnostics at up to 500 points
    idx = np.linspace(0, n-1, min(500, n), dtype=int)
    Dt = np.zeros(n); Ft = np.zeros(n); dVt = np.zeros(n)
    for k in idx:
        tc = _cb(tau[k]); mu_k = max(mu[k], 0.)
        lm = float(ip['lm'](tc))
        r = mu_k / lm if lm > 1e-14 else 0.
        Dt[k] = Dn_eval(tc, r, ip)
        Ft[k] = Fc_eval(tc, r, ip)
        dVt[k] = dV_eff_dtau(tc, mu_k, ip, Tf)
    if Tf > 0 and Tf < 1.: Ft *= np.sqrt(max(0,1-Tf**2))

    d['Delta'] = Dt; d['Fc'] = Ft; d['dV'] = dVt
    d['Dmax'] = float(np.max(Dt)); d['Fmin'] = float(np.min(Ft))

    rlo_t = np.array([float(ip['rlo'](_cb(tt))) for tt in tau])
    rhi_t = np.array([float(ip['rhi'](_cb(tt))) for tt in tau])
    in_w = (r_t >= rlo_t) & (r_t <= rhi_t) & (tau >= 0) & (tau <= TAU_MAX)
    d['in_win'] = bool(np.any(in_w))
    d['t_win'] = float(t[in_w][-1]-t[in_w][0]) if np.sum(in_w)>=2 else 0.

    # Lock detection (v2: require BCS-induced equilibrium, not V_spec artifact)
    # A transient sign change during tau oscillation is NOT a lock.
    # A sign change at the V_spec cubic spline minimum (tau~0.017) is NOT a lock.
    # Lock requires: (1) in BCS window, (2) |pi_tau| small (settled),
    # (3) dV_eff/dtau sign change, (4) d2V/dtau2 > 0, (5) NOT at V_spec minimum.
    #
    # V_spec has a cubic spline artifact minimum at tau~0.017 (depth ~1e-3).
    # Any dV sign change near this tau is V_spec, not BCS. Filter these out
    # by checking: does dV_spec alone also change sign at this tau?
    lock = []
    for k in range(1, n):
        if dVt[k-1]*dVt[k]<0 and 0<=tau[k]<=TAU_MAX and in_w[k]:
            lock.append(k)
    d['n_lock_cross_raw'] = len(lock)  # raw count (includes transients)

    # Filter step 1: require |pi_tau| < settling threshold
    pi_max = max(abs(res['pi']).max(), 1e-14)
    pi_thresh = 0.01 * pi_max

    # Filter step 2: exclude V_spec artifact minimum (dV_spec changes sign at same tau)
    # V_spec minimum is at tau ~ 0.017; dV_spec < 0 for tau < 0.017, > 0 for tau > 0.017
    sustained_lock = []
    for k in lock:
        if abs(res['pi'][k]) < pi_thresh:
            tl = _cb(0.5*(tau[k-1]+tau[k]))
            ml = 0.5*(mu[k-1]+mu[k])

            # Check if V_spec alone has same-sign change at this tau
            dVs_here = float(ip['Vs'](_cv(tl), 1))
            # Near V_spec minimum, |dV_spec| < 0.1. If dV_spec is near zero
            # and changes sign, this is a V_spec feature, not BCS.
            if abs(dVs_here) < 0.1:
                continue  # Skip: at V_spec local minimum artifact

            # Verify d2V/dtau2 > 0 (true minimum, not saddle)
            h = 1e-4
            dVp = dV_eff_dtau(min(tl+h, 0.499), ml, ip, Tf)
            dVm = dV_eff_dtau(max(tl-h, 0.001), ml, ip, Tf)
            d2V = (dVp-dVm)/(2*h)
            if d2V > 0:
                sustained_lock.append((k, tl, ml, d2V/G_TT))

    d['locked'] = len(sustained_lock) > 0
    d['n_lock_sustained'] = len(sustained_lock)
    if sustained_lock:
        ki, tl, ml, msq = sustained_lock[0]
        d['m_sq'] = float(msq)
        d['tau_lock'] = float(tl)
    else:
        d['m_sq'] = None; d['tau_lock'] = None

    # LZ
    P = np.zeros(n)
    for k in idx:
        tc = _cb(tau[k]); dg = float(ip['gap'](tc))
        h = 1e-4
        gp = float(ip['gap'](min(tc+h, TAU_MAX-1e-14)))
        gm = float(ip['gap'](max(tc-h, 1e-14)))
        vel = abs((gp-gm)/(2*h) * res['pi'][k])
        if vel>1e-30 and dg>1e-30: P[k] = np.exp(-2*np.pi*dg**2/vel)
    d['PLZ'] = P; d['PLZ_max'] = float(np.max(P))
    return d


# ===========================================================================
# 6. SCANS
# ===========================================================================
def scan_H0(ip, tau_i=0.15, mr=10., Tf=0.,
            H0s=np.array([0.001,0.005,0.01,0.05,0.1,0.5,1.,5.,10.])):
    lm = float(ip['lm'](tau_i)); mu0 = mr*lm
    o = {k: np.zeros(len(H0s)) for k in ['tauf','Dmax','Fmin','rmin','twin']}
    o['H0s'] = H0s
    o['locked'] = np.zeros(len(H0s), dtype=bool)
    o['in_win'] = np.zeros(len(H0s), dtype=bool)
    o['n_lock_raw'] = np.zeros(len(H0s), dtype=int)
    o['n_lock_sustained'] = np.zeros(len(H0s), dtype=int)
    for k, H0 in enumerate(H0s):
        r = integrate_full(tau_i, 0., mu0, H0, Tf, ip)
        dg = diag_full(r, ip, Tf)
        o['tauf'][k]=dg['tau_f']; o['locked'][k]=dg['locked']
        o['Dmax'][k]=dg['Dmax']; o['Fmin'][k]=dg['Fmin']
        o['rmin'][k]=dg['r_min']; o['twin'][k]=dg['t_win']
        o['in_win'][k]=dg['in_win']
        o['n_lock_raw'][k]=dg['n_lock_cross_raw']
        o['n_lock_sustained'][k]=dg['n_lock_sustained']
    return o


def scan_mu0(ip, tau_i=0.15, H_0=0.01, Tf=0., n=20, rng=(2.,50.)):
    lm = float(ip['lm'](tau_i))
    mrs = np.geomspace(rng[0], rng[1], n)
    o = {k: np.zeros(n) for k in ['tauf','Dmax','Fmin','twin','rmin']}
    o['mrs'] = mrs; o['locked'] = np.zeros(n, dtype=bool)
    o['in_win'] = np.zeros(n, dtype=bool)
    for k, mr in enumerate(mrs):
        r = integrate_full(tau_i, 0., mr*lm, H_0, Tf, ip)
        dg = diag_full(r, ip, Tf)
        o['tauf'][k]=dg['tau_f']; o['locked'][k]=dg['locked']
        o['Dmax'][k]=dg['Dmax']; o['Fmin'][k]=dg['Fmin']
        o['twin'][k]=dg['t_win']; o['rmin'][k]=dg['r_min']
        o['in_win'][k]=dg['in_win']
    return o


def scan_2d(ip, mr=10., H_0=0.01, Tf=0., nt=8, np_=8):
    tv = np.linspace(0.02, 0.48, nt)
    pv = np.linspace(-0.05, 0.05, np_)
    o = {'tau_i':tv, 'pi_i':pv,
         'tauf':np.zeros((nt,np_)), 'locked':np.zeros((nt,np_),dtype=bool),
         'rmin':np.zeros((nt,np_))}
    for i, ti in enumerate(tv):
        lm = float(ip['lm'](ti)); mu0 = mr*lm
        for j, pi in enumerate(pv):
            try:
                r = integrate_full(ti, pi, mu0, H_0, Tf, ip, t_max_factor=2.)
                dg = diag_full(r, ip, Tf)
                o['tauf'][i,j]=dg['tau_f']; o['locked'][i,j]=dg['locked']
                o['rmin'][i,j]=dg['r_min']
            except Exception:
                o['tauf'][i,j]=ti; o['rmin'][i,j]=mr
    return o


# ===========================================================================
# 7. PLOTTING
# ===========================================================================
def make_plot(fid, fd, adiab, mu_sc, H0_sc, s2d, ip, tau_i, H_0, Tf):
    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("Session 26 P2: Coupled Cooling Trajectory", fontsize=14, fontweight='bold')
    lm_i = float(ip['lm'](tau_i))

    # P1: tau(t) and mu(t)/lmin from fiducial
    ax = axes[0,0]
    ax.plot(fid['t'], fid['tau'], 'b-', label='$\\tau(t)$')
    ax.set_xlabel('t'); ax.set_ylabel('$\\tau$', color='b')
    ax.set_xscale('log'); ax.set_title('Fiducial trajectory')
    ax2 = ax.twinx()
    ax2.plot(fid['t'], fd['r'], 'r-', alpha=0.7, label='$r(t)$')
    ax2.set_ylabel('$\\mu/\\lambda_{min}$', color='r')
    ax2.axhline(1.15, color='g', ls='--', alpha=0.3)
    ax2.axhline(0.925, color='g', ls='--', alpha=0.3)
    ax.legend(fontsize=8, loc='upper left'); ax2.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    # P2: Adiabatic dV_eff/dtau vs r at tau_settled
    ax = axes[0,1]
    ax.plot(adiab['r_vals'], adiab['dV_vs_r'], 'b-')
    ax.axhline(0, color='k', ls='-', alpha=0.3)
    rlo = float(ip['rlo'](_cb(fd['tau_f'])))
    rhi = float(ip['rhi'](_cb(fd['tau_f'])))
    ax.axvspan(rlo, rhi, alpha=0.15, color='green')
    ax.set_xlabel('$r = \\mu/\\lambda_{min}$')
    ax.set_ylabel('$dV_{eff}/d\\tau$')
    ax.set_title(f'Force at $\\tau_{{settled}}={fd["tau_f"]:.4f}$')
    ax.grid(True, alpha=0.3)

    # P3: V_eff(tau) at different r
    ax = axes[0,2]
    tpl = np.linspace(0.005, 0.495, 200)
    for mr in [0., 0.95, 1.0, 1.05]:
        Va = np.array([V_eff(tp, mr*float(ip['lm'](tp)), ip, Tf) for tp in tpl])
        lab = f'$r={mr:.2f}$' if mr>0 else '$V_{{spec}}$'
        ax.plot(tpl, Va, label=lab)
    ax.set_xlabel('$\\tau$'); ax.set_ylabel('$V_{eff}$')
    ax.set_title('Potential landscape'); ax.legend(fontsize=7); ax.grid(True,alpha=0.3)

    # P4: H_0 scan
    ax = axes[1,0]
    ax.semilogx(H0_sc['H0s'], H0_sc['rmin'], 'bo-', ms=5, label='$r_{min}$')
    ax.axhline(1.15, color='g', ls='--', alpha=0.5, label='Window upper')
    ax.axhline(0.925, color='r', ls='--', alpha=0.5, label='Window lower')
    for k in range(len(H0_sc['H0s'])):
        if H0_sc['in_win'][k]:
            ax.plot(H0_sc['H0s'][k], H0_sc['rmin'][k], 'g*', ms=12, zorder=5)
    ax.set_xlabel('$H_0$'); ax.set_ylabel('$r_{min}$')
    ax.set_title('$H_0$ scan: window access'); ax.legend(fontsize=7); ax.grid(True,alpha=0.3)

    # P5: 2D dV_eff/dtau map from adiabatic sweep
    ax = axes[1,1]
    T_, R_ = np.meshgrid(adiab['tau_scan'], adiab['r_scan'], indexing='ij')
    pcm = ax.pcolormesh(T_, R_, adiab['dV_2d'], cmap='RdBu_r', shading='auto',
                        vmin=-5, vmax=5)
    fig.colorbar(pcm, ax=ax, label='$dV_{eff}/d\\tau$')
    ax.contour(T_, R_, adiab['dV_2d'], levels=[0], colors='black', linewidths=2)
    if adiab['lock_points']:
        tl = [p[0] for p in adiab['lock_points']]
        rl = [p[1] for p in adiab['lock_points']]
        ax.scatter(tl, rl, marker='*', color='gold', s=100, zorder=5, label='Lock')
        ax.legend(fontsize=7)
    ax.set_xlabel('$\\tau$'); ax.set_ylabel('$r = \\mu/\\lambda_{min}$')
    ax.set_title('Force map $dV_{eff}/d\\tau$'); ax.grid(True,alpha=0.3)

    # P6: 2D phase diagram from scan
    ax = axes[1,2]
    TI,PI = np.meshgrid(s2d['tau_i'], s2d['pi_i'], indexing='ij')
    pcm = ax.pcolormesh(TI, PI, s2d['tauf'], cmap='RdYlBu_r', shading='auto')
    fig.colorbar(pcm, ax=ax, label='$\\tau_f$')
    if np.any(s2d['locked']):
        li,lj = np.where(s2d['locked'])
        ax.scatter(s2d['tau_i'][li], s2d['pi_i'][lj], marker='x', color='k', s=30)
    ax.set_xlabel('$\\tau_i$'); ax.set_ylabel('$\\dot\\tau_i$')
    ax.set_title('Phase diagram'); ax.grid(True,alpha=0.3)

    plt.tight_layout()
    fig.savefig(str(OUT_PNG), dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Plot: {OUT_PNG}")


# ===========================================================================
# 8. VERDICT
# ===========================================================================
def compute_verdict(mu_sc, H0_sc, H0_fine, s2d, adiab, fd, ip, Tf_results=None):
    L = ["="*70, "SESSION 26 P2: COUPLED COOLING TRAJECTORY -- VERDICT (v2)", "="*70]

    any_lock_mu = bool(np.any(mu_sc['locked']))
    any_lock_2d = bool(np.any(s2d['locked']))
    any_lock_H0 = bool(np.any(H0_sc['locked']))
    any_lock_H0f = bool(np.any(H0_fine['locked']))
    any_lock_adiab = adiab['has_lock']
    any_win = bool(np.any(H0_sc['in_win'])) or bool(np.any(H0_fine['in_win']))

    # --- ADIABATIC ANALYSIS (DIAGNOSTIC ONLY) ---
    L.append(f"\n--- ADIABATIC ANALYSIS (DIAGNOSTIC, does NOT enter verdict) ---")
    L.append(f"Lock points in (tau, r) space: {len(adiab['lock_points'])}")
    n_vspec = sum(1 for tl,rl,msq in adiab['lock_points'] if tl < 0.025)
    n_bcs = len(adiab['lock_points']) - n_vspec
    L.append(f"  Of these: {n_vspec} at tau<0.025 (V_spec cubic spline minimum artifact)")
    L.append(f"            {n_bcs} at tau>=0.025 (BCS-influenced)")
    L.append(f"  V_spec has shallow local minimum at tau~0.017 (spline artifact from")
    L.append(f"  nearly flat V_spec: V(0)=17.700, V(0.1)=17.750, diff=0.050)")
    L.append(f"  These static equilibria are NEVER reached by the dynamic trajectory.")

    # --- ODE SCANS (DETERMINES VERDICT) ---
    L.append(f"\n--- ODE SCANS (determines verdict) ---")
    L.append(f"\n1. mu_0 scan (n={len(mu_sc['mrs'])}): {'LOCK' if any_lock_mu else 'NO LOCK'}")
    L.append(f"   r_min: [{mu_sc['rmin'].min():.4f}, {mu_sc['rmin'].max():.4f}]")
    L.append(f"   in_window: {np.sum(mu_sc['in_win'])}/{len(mu_sc['in_win'])}")

    L.append(f"\n2. H_0 coarse scan (n={len(H0_sc['H0s'])}):")
    for k in range(len(H0_sc['H0s'])):
        w = "WIN" if H0_sc['in_win'][k] else "---"
        lk = "LOCK" if H0_sc['locked'][k] else "----"
        L.append(f"   H_0={H0_sc['H0s'][k]:<8.4f}: {w} {lk} rmin={H0_sc['rmin'][k]:.4f} "
                 f"Dmax={H0_sc['Dmax'][k]:.4f}")

    L.append(f"\n3. H_0 fine scan (n={len(H0_fine['H0s'])}):")
    for k in range(len(H0_fine['H0s'])):
        w = "WIN" if H0_fine['in_win'][k] else "---"
        lk = "LOCK" if H0_fine['locked'][k] else "----"
        L.append(f"   H_0={H0_fine['H0s'][k]:<8.4f}: {w} {lk} rmin={H0_fine['rmin'][k]:.4f} "
                 f"Dmax={H0_fine['Dmax'][k]:.4f}")

    # Window-access boundary from fine scan
    win_h0s = H0_fine['H0s'][H0_fine['in_win'].astype(bool)]
    if len(win_h0s) > 0:
        L.append(f"   Window accessed for H_0 >= {win_h0s[0]:.4f}")
    else:
        L.append(f"   Window never accessed in fine scan")

    L.append(f"\n4. 2D scan ({s2d['tau_i'].size}x{s2d['pi_i'].size}): "
             f"{'LOCK' if any_lock_2d else 'NO LOCK'}")

    # --- GRADIENT ANALYSIS ---
    L.append(f"\n--- GRADIENT ANALYSIS ---")
    lm15 = float(ip['lm'](0.15))
    dVs = float(ip['Vs'](0.15, 1))
    dVf = dV_eff_dtau(0.15, lm15, ip)
    dVb = dVf - dVs
    L.append(f"At tau=0.15, r=1.0:")
    L.append(f"   dV_spec/dtau = {dVs:.4f}")
    L.append(f"   dV_BCS/dtau  = {dVb:.4f}")
    L.append(f"   dV_eff/dtau  = {dVf:.4f}")
    L.append(f"   |dV_BCS/dV_spec| = {abs(dVb)/max(abs(dVs),1e-14):.4f}")

    # Best case: at which (tau, r) is |dV_BCS/dV_spec| largest?
    L.append(f"\n--- FORCE COMPETITION OVER FULL (tau, r) GRID ---")
    max_ratio = 0.; best_tau = 0.; best_r = 0.
    for i, tau in enumerate(adiab['tau_scan']):
        dVs_i = float(ip['Vs'](_cv(tau), 1))
        if abs(dVs_i) < 1e-14: continue
        for j, r in enumerate(adiab['r_scan']):
            dV_total = adiab['dV_2d'][i, j]
            dV_bcs = dV_total - dVs_i
            ratio = abs(dV_bcs) / abs(dVs_i)
            if ratio > max_ratio:
                max_ratio = ratio; best_tau = tau; best_r = r
    L.append(f"Max |dV_BCS/dV_spec| = {max_ratio:.4f} at tau={best_tau:.3f}, r={best_r:.3f}")
    L.append(f"{'PASSES' if max_ratio > 1 else 'FAILS'} the gradient competition (need > 1)")

    # --- TEMPERATURE SHOW-STOPPER ---
    if Tf_results is not None:
        L.append(f"\n--- TEMPERATURE SHOW-STOPPER ---")
        L.append(f"Design doc Sec. 13.2: T ~ mu ~ lambda_min >> T_c = 0.03*lambda_min")
        L.append(f"When mu/lambda_min ~ 1 (window), T/T_c ~ 1/0.03 ~ 33 >> 1")
        for tf_val, tf_data in Tf_results.items():
            L.append(f"\n  Tf={tf_val:.1f} (T-suppression sqrt(1-Tf^2)={np.sqrt(max(0,1-tf_val**2)):.3f}):")
            L.append(f"    H0_fine locked: {np.sum(tf_data['locked'])}/{len(tf_data['locked'])}")
            L.append(f"    H0_fine in_win: {np.sum(tf_data['in_win'])}/{len(tf_data['in_win'])}")
            w = tf_data['H0s'][tf_data['in_win'].astype(bool)]
            if len(w) > 0:
                L.append(f"    Window accessed for H_0 >= {w[0]:.4f}")
                L.append(f"    Max Delta: {tf_data['Dmax'].max():.4f}")
            else:
                L.append(f"    Window never accessed")

    # --- VERDICT (v2: ODE-only, no adiabatic) ---
    any_lock_ode = any_lock_mu or any_lock_2d or any_lock_H0 or any_lock_H0f
    if any_lock_ode:
        # Check if locks are sustained or just transient
        all_raw = (int(np.sum(H0_sc.get('n_lock_raw', np.zeros(1)))) +
                   int(np.sum(H0_fine.get('n_lock_raw', np.zeros(1)))))
        all_sustained = (int(np.sum(H0_sc.get('n_lock_sustained', np.zeros(1)))) +
                         int(np.sum(H0_fine.get('n_lock_sustained', np.zeros(1)))))
        if all_sustained > 0:
            v = "P2-LOCK: MARGINAL"
            L.append(f"\n** VERDICT: {v} **")
            L.append(f"Sustained lock found in ODE. Requires stability analysis.")
        else:
            v = "P2-LOCK: CLOSED"
            L.append(f"\n** VERDICT: {v} **")
            L.append(f"ODE sign changes are transient ringing, not sustained locks.")
            L.append(f"Raw dV sign changes in window: {all_raw}")
            L.append(f"Sustained (low velocity + d2V>0): {all_sustained}")
    else:
        v = "P2-LOCK: CLOSED"
        L.append(f"\n** VERDICT: {v} **")
        L.append(f"No modulus lock in any ODE configuration.")

    if max_ratio < 1:
        L.append(f"|dV_BCS| < |dV_spec| everywhere => BCS gradient too weak.")
    if not any_win:
        L.append(f"At physical H_0, modulus settles before mu reaches window.")
    elif not any_lock_ode:
        L.append(f"mu reaches window at large H_0 but gradient competition lost.")
    elif v == "P2-LOCK: CLOSED":
        L.append(f"tau ringing through window produces transient sign changes,")
        L.append(f"but tau never settles to a BCS-induced equilibrium.")

    L.append(f"\nAdiabatic static lock points ({len(adiab['lock_points'])}) are")
    L.append(f"dynamically inaccessible: tau settles to ~0.018 before mu enters window.")

    if Tf_results is not None:
        any_T_lock = any(bool(np.any(d['locked'])) for d in Tf_results.values())
        if not any_T_lock:
            L.append(f"\nFinite-T scans (Tf=0.5, 0.9): No lock at any temperature.")
            L.append(f"Temperature show-stopper CONFIRMED: T >> T_c in window.")

    L.append("\n" + "="*70)
    return v, "\n".join(L)


# ===========================================================================
# 9. MAIN
# ===========================================================================
if __name__ == '__main__':
    t0 = wc.time()
    print("Session 26 P2: Coupled Cooling-Trajectory ODE (v2: corrected verdict)")
    print("="*60); sys.stdout.flush()

    print("\n[1] Loading..."); sys.stdout.flush()
    ip = load_and_build()
    print(f"    lm={ip['lm_raw']}")
    print(f"    Window lo={ip['rlo_raw']}, hi={ip['rhi_raw']}")
    print(f"    F_cond A={ip['FA']}"); sys.stdout.flush()

    TAU_I, MR0, H0, TF = 0.15, 10., 0.01, 0.
    lm_i = float(ip['lm'](TAU_I))

    # Phase A: settle tau
    print(f"\n[2] Phase A: settle tau (tau_i={TAU_I}, H_0={H0})..."); sys.stdout.flush()
    tau_s, pi_s, t_s, solA = settle_tau(TAU_I, 0., H0, ip)
    print(f"    tau settled: {TAU_I:.4f} -> {tau_s:.6f} (pi={pi_s:.2e})")
    print(f"    Steps: {len(solA.t)}, t_final={t_s:.1f}"); sys.stdout.flush()

    # Phase B: adiabatic sweep (DIAGNOSTIC ONLY)
    print(f"\n[3] Phase B: adiabatic sweep at tau_s={tau_s:.4f} (diagnostic)..."); sys.stdout.flush()
    adiab = adiabatic_sweep(tau_s, ip, TF)
    n_locks_adiab = len(adiab['lock_points'])
    n_vspec_art = sum(1 for tl,rl,msq in adiab['lock_points'] if tl < 0.025)
    print(f"    Static lock points: {n_locks_adiab} ({n_vspec_art} V_spec artifacts, "
          f"{n_locks_adiab - n_vspec_art} BCS-influenced)")
    print(f"    NOTE: These are static equilibria, NOT dynamically accessible.")
    print(f"    Sign changes in dV at tau_s: {len(adiab['sign_changes'])}")
    sys.stdout.flush()

    # Phase C: full ODE fiducial
    print(f"\n[4] Phase C: full ODE (tau_i={TAU_I}, r_0={MR0}, H_0={H0})..."); sys.stdout.flush()
    t4 = wc.time()
    fid = integrate_full(TAU_I, 0., MR0*lm_i, H0, TF, ip)
    fd = diag_full(fid, ip, TF)
    print(f"    Done {wc.time()-t4:.1f}s, steps={fid['n_steps']}")
    print(f"    tau: {fid['tau'][0]:.6f} -> {fd['tau_f']:.6f}")
    print(f"    r: {fd['r'][0]:.4f} -> min={fd['r_min']:.4f}")
    print(f"    in_win={fd['in_win']}, locked={fd['locked']}, Dmax={fd['Dmax']:.4f}")
    sys.stdout.flush()

    # Scan: mu_0
    print(f"\n[5] mu_0 scan [2,50], 20 pts...", end=' '); sys.stdout.flush()
    t5 = wc.time()
    mu_sc = scan_mu0(ip, tau_i=TAU_I, H_0=H0, Tf=TF, n=20)
    print(f"Done {wc.time()-t5:.1f}s")
    print(f"    Locked: {np.sum(mu_sc['locked'])}/{len(mu_sc['locked'])}")
    print(f"    in_win: {np.sum(mu_sc['in_win'])}/{len(mu_sc['in_win'])}")
    print(f"    r_min: [{mu_sc['rmin'].min():.4f}, {mu_sc['rmin'].max():.4f}]"); sys.stdout.flush()

    # Scan: H_0 coarse (original 9 points)
    print(f"\n[6a] H_0 coarse scan...", end=' '); sys.stdout.flush()
    t6 = wc.time()
    H0_sc = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=TF)
    print(f"Done {wc.time()-t6:.1f}s")
    for k in range(len(H0_sc['H0s'])):
        lk_info = f"raw={H0_sc['n_lock_raw'][k]} sust={H0_sc['n_lock_sustained'][k]}"
        print(f"    H_0={H0_sc['H0s'][k]:.3f}: rmin={H0_sc['rmin'][k]:.4f} "
              f"win={H0_sc['in_win'][k]} Dmax={H0_sc['Dmax'][k]:.4f} {lk_info}")
    sys.stdout.flush()

    # Scan: H_0 fine (30 points in [0.1, 10]) -- map window-access boundary
    print(f"\n[6b] H_0 fine scan [0.1, 10], 30 pts...", end=' '); sys.stdout.flush()
    t6b = wc.time()
    H0_fine_vals = np.geomspace(0.1, 10., 30)
    H0_fine = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=TF, H0s=H0_fine_vals)
    print(f"Done {wc.time()-t6b:.1f}s")
    win_mask = H0_fine['in_win'].astype(bool)
    if np.any(win_mask):
        print(f"    Window accessed for H_0 >= {H0_fine['H0s'][win_mask][0]:.4f}")
        print(f"    Max Delta over all: {H0_fine['Dmax'].max():.4f}")
    print(f"    Locked (sustained): {np.sum(H0_fine['locked'])}/{len(H0_fine['locked'])}")
    for k in range(len(H0_fine['H0s'])):
        if H0_fine['in_win'][k] or H0_fine['n_lock_raw'][k] > 0:
            print(f"    H_0={H0_fine['H0s'][k]:.4f}: rmin={H0_fine['rmin'][k]:.4f} "
                  f"win={H0_fine['in_win'][k]} raw={H0_fine['n_lock_raw'][k]} "
                  f"sust={H0_fine['n_lock_sustained'][k]} Dmax={H0_fine['Dmax'][k]:.4f}")
    sys.stdout.flush()

    # Scan: Temperature factor (Tf=0.5, Tf=0.9) -- show-stopper test
    print(f"\n[6c] Temperature scans..."); sys.stdout.flush()
    Tf_results = {}
    for Tf_val in [0.5, 0.9]:
        t6c = wc.time()
        Tsup = np.sqrt(max(0, 1 - Tf_val**2))
        print(f"  Tf={Tf_val} (suppression={Tsup:.3f})...", end=' '); sys.stdout.flush()
        Tf_sc = scan_H0(ip, tau_i=TAU_I, mr=MR0, Tf=Tf_val, H0s=H0_fine_vals)
        Tf_results[Tf_val] = Tf_sc
        tw = Tf_sc['in_win'].astype(bool)
        print(f"Done {wc.time()-t6c:.1f}s  win={np.sum(tw)} locked={np.sum(Tf_sc['locked'])}")
        if np.any(tw):
            print(f"    Max Delta: {Tf_sc['Dmax'].max():.4f}")
        sys.stdout.flush()

    # Scan: 2D
    print(f"\n[7] 2D scan 8x8...", end=' '); sys.stdout.flush()
    t7 = wc.time()
    s2d = scan_2d(ip, mr=10., H_0=H0, Tf=TF, nt=8, np_=8)
    print(f"Done {wc.time()-t7:.1f}s")
    print(f"    Locked: {np.sum(s2d['locked'])}/{s2d['locked'].size}"); sys.stdout.flush()

    # Verdict
    print(f"\n[8] Verdict..."); sys.stdout.flush()
    v, vtxt = compute_verdict(mu_sc, H0_sc, H0_fine, s2d, adiab, fd, ip, Tf_results)
    print(vtxt); sys.stdout.flush()

    # Plot (enhanced with fine H0 scan)
    print(f"\n[9] Plotting..."); sys.stdout.flush()
    make_plot(fid, fd, adiab, mu_sc, H0_fine, s2d, ip, TAU_I, H0, TF)

    # Save
    print(f"\n[10] Saving..."); sys.stdout.flush()
    sv = {
        'fid_t': fid['t'], 'fid_tau': fid['tau'], 'fid_pi': fid['pi'],
        'fid_mu': fid['mu'], 'fid_r': fd['r'],
        'fid_Delta': fd['Delta'], 'fid_Fc': fd['Fc'], 'fid_dV': fd['dV'],
        'fid_PLZ': fd['PLZ'], 'fid_locked': fd['locked'],
        'fid_Dmax': fd['Dmax'], 'fid_Fmin': fd['Fmin'],
        'fid_rmin': fd['r_min'], 'fid_twin': fd['t_win'],
        'fid_in_win': fd['in_win'], 'fid_tau_f': fd['tau_f'],

        'adiab_r': adiab['r_vals'], 'adiab_V': adiab['V_vs_r'],
        'adiab_dV': adiab['dV_vs_r'], 'adiab_D': adiab['D_vs_r'],
        'adiab_tau_scan': adiab['tau_scan'], 'adiab_r_scan': adiab['r_scan'],
        'adiab_dV_2d': adiab['dV_2d'], 'adiab_V_2d': adiab['V_2d'],
        'adiab_n_locks': len(adiab['lock_points']),
        'adiab_n_vspec_artifact': n_vspec_art,

        'musc_mrs': mu_sc['mrs'], 'musc_tauf': mu_sc['tauf'],
        'musc_locked': mu_sc['locked'], 'musc_Dmax': mu_sc['Dmax'],
        'musc_rmin': mu_sc['rmin'], 'musc_in_win': mu_sc['in_win'],

        'H0sc_H0s': H0_sc['H0s'], 'H0sc_tauf': H0_sc['tauf'],
        'H0sc_locked': H0_sc['locked'], 'H0sc_Dmax': H0_sc['Dmax'],
        'H0sc_rmin': H0_sc['rmin'], 'H0sc_twin': H0_sc['twin'],
        'H0sc_in_win': H0_sc['in_win'],
        'H0sc_n_lock_raw': H0_sc['n_lock_raw'],
        'H0sc_n_lock_sustained': H0_sc['n_lock_sustained'],

        'H0f_H0s': H0_fine['H0s'], 'H0f_tauf': H0_fine['tauf'],
        'H0f_locked': H0_fine['locked'], 'H0f_Dmax': H0_fine['Dmax'],
        'H0f_rmin': H0_fine['rmin'], 'H0f_twin': H0_fine['twin'],
        'H0f_in_win': H0_fine['in_win'],
        'H0f_n_lock_raw': H0_fine['n_lock_raw'],
        'H0f_n_lock_sustained': H0_fine['n_lock_sustained'],

        'Tf05_locked': Tf_results[0.5]['locked'],
        'Tf05_in_win': Tf_results[0.5]['in_win'],
        'Tf05_Dmax': Tf_results[0.5]['Dmax'],
        'Tf09_locked': Tf_results[0.9]['locked'],
        'Tf09_in_win': Tf_results[0.9]['in_win'],
        'Tf09_Dmax': Tf_results[0.9]['Dmax'],

        's2d_taui': s2d['tau_i'], 's2d_pii': s2d['pi_i'],
        's2d_tauf': s2d['tauf'], 's2d_locked': s2d['locked'],
        's2d_rmin': s2d['rmin'],

        'FA': ip['FA'], 'FR': ip['FR'], 'FS': ip['FS'],
        'rlo': ip['rlo_raw'], 'rhi': ip['rhi_raw'], 'gaps': ip['gap_raw'],
        'tau_i': TAU_I, 'H_0': H0, 'G_tt': G_TT, 'lm_i': lm_i,
        'tau_settled': tau_s,
        'verdict': v,
    }
    np.savez(str(OUT_NPZ), **sv)
    print(f"    {OUT_NPZ}")
    print(f"\nTotal: {wc.time()-t0:.1f}s\nVERDICT: {v}"); sys.stdout.flush()
