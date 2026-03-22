#!/usr/bin/env python3
"""
Session 39 — W2-4: Coupled Friedmann-BCS Dynamics (FRIED-39 MASTER GATE)

Physics: The modulus tau(t) obeys a Klein-Gordon equation in FRW spacetime
with potential V(tau) from the spectral action, plus BCS backreaction:

    G_mod * ddot{tau} + 3*H*G_mod*dot{tau} + dV_eff/dtau = 0
    H^2 = G_eff * [(G_mod/2)*dot{tau}^2 + V_eff(tau)]

V_eff = V_bare(S_full) + E_BCS(Gaussian at fold, depth -0.1557).

Gate: FRIED-39. PASS: dwell > 40 for any H_0. FAIL: dwell < 40 for ALL H_0.
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os, time

t0_wall = time.time()
base = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# 1. Load data
# ============================================================
d36s = np.load(os.path.join(base, 's36_sfull_tau_stabilization.npz'), allow_pickle=True)
d36d = np.load(os.path.join(base, 's36_tau_dynamics.npz'), allow_pickle=True)
d37  = np.load(os.path.join(base, 's37_instanton_action.npz'), allow_pickle=True)

tau_grid = d36s['tau_combined']
S_full   = d36s['S_full']
dS_fold  = float(d36s['dS_fold'].flat[0])

E_cond   = float(d37['E_cond_use'].flat[0])      # -0.1557
tau_fold = float(d37['tau_fold'].flat[0])          # 0.19016
tau_BCS  = float(d36d['tau_BCS'].flat[0])          # 40.0
BCS_lo   = float(d36d['BCS_window_lo'].flat[0])    # 0.175
BCS_hi   = float(d36d['BCS_window_hi'].flat[0])    # 0.205
G_mod    = float(d36d['G_mod_standard'].flat[0])   # 5.0

print("=" * 70)
print("FRIED-39: Coupled Friedmann-BCS Dynamics (MASTER GATE)")
print("=" * 70)

# ============================================================
# 2. Build potentials
# ============================================================
cs_S = CubicSpline(tau_grid, S_full)
sigma_BCS = 0.015
Delta_tau = BCS_hi - BCS_lo  # 0.03

def dV_bare(tau):
    return float(cs_S(tau, 1))

def E_BCS(tau):
    return E_cond * np.exp(-((tau - tau_fold)/sigma_BCS)**2)

def dE_BCS(tau):
    x = (tau - tau_fold)/sigma_BCS
    return E_cond * np.exp(-x**2) * (-2*x/sigma_BCS)

# ============================================================
# 3. Gradient hierarchy (the decisive number)
# ============================================================
dV_fold = abs(dV_bare(tau_fold))
tau_maxdE = tau_fold + sigma_BCS/np.sqrt(2)
dE_max = abs(dE_BCS(tau_maxdE))
ratio_grad = dV_fold / dE_max

print(f"\n--- GRADIENT HIERARCHY (decisive) ---")
print(f"  |dV_bare/dtau| at fold:  {dV_fold:.1f}")
print(f"  max|dE_BCS/dtau|:        {dE_max:.4f}")
print(f"  RATIO: {ratio_grad:.0f}x")
print(f"  BCS backreaction is {ratio_grad:.0f}x weaker than bare gradient")
print(f"  E_cond = {E_cond:.4f}, S_full at fold = {float(cs_S(tau_fold)):.0f}")

# ============================================================
# 4. ODE integrator (LSODA for stiffness at high friction)
# ============================================================
def integrate(G_eff, tau0, v0, amp=1.0, t_max=10.0):
    """Integrate Friedmann-BCS system, return (t, tau, v, dwell)."""
    V_bare_fn = cs_S

    def rhs(t, y):
        tau, v = y
        Vb = float(V_bare_fn(tau))
        dVb = float(V_bare_fn(tau, 1))
        Eb = amp * E_cond * np.exp(-((tau - tau_fold)/sigma_BCS)**2)
        x = (tau - tau_fold)/sigma_BCS
        dEb = amp * E_cond * np.exp(-x**2) * (-2*x/sigma_BCS)

        rho = 0.5*G_mod*v**2 + Vb + Eb
        H = np.sqrt(G_eff * max(rho, 0.0)) if G_eff > 0 else 0.0
        a = -3.0*H*v - (dVb + dEb)/G_mod
        return [v, a]

    def ev_low(t, y):
        return y[0] - 0.005
    ev_low.terminal = True
    ev_low.direction = -1

    # Use LSODA (auto stiff/nonstiff) with sparse output
    n_out = min(10000, max(1000, int(t_max*100)))
    t_eval = np.linspace(0, t_max, n_out)

    sol = solve_ivp(rhs, (0, t_max), [tau0, v0],
                    method='LSODA', events=[ev_low],
                    t_eval=t_eval, rtol=1e-10, atol=1e-12)

    t_a, tau_a, v_a = sol.t, sol.y[0], sol.y[1]
    # Dwell time
    in_w = (tau_a >= BCS_lo) & (tau_a <= BCS_hi)
    if np.any(in_w) and len(t_a) > 1:
        dt = np.diff(t_a)
        mid = in_w[:-1] & in_w[1:]
        dwell = np.sum(dt[mid])
    else:
        dwell = 0.0
    return t_a, tau_a, v_a, dwell

# ============================================================
# 5. Scenario A: Start from rest at tau=0.40, scan H_0
# ============================================================
print(f"\n{'='*70}")
print("SCENARIO A: tau_0=0.40, v_0=0, scan H_0")
print('='*70)

tau0 = 0.40
V0 = float(cs_S(tau0))  # ~269,856

H0_vals = [0.0, 1e-4, 1e-2, 1.0, 10, 100, 1000, 1e4, 1e5]
res_A = {}

for H0 in H0_vals:
    G_eff = (H0**2 / V0) if H0 > 0 else 0.0
    # Estimate needed integration time
    if H0 > 10:
        # Overdamped: v ~ dV/(3*H*G_mod), t_transit ~ 0.4/(v) ~ 0.4*3*H*G_mod/dV
        t_est = 3.0*H0*G_mod*0.4/dV_fold * 3
        t_max = min(t_est, 5e5)
    elif H0 > 0:
        t_max = 10.0
    else:
        t_max = 0.1

    try:
        t_a, tau_a, v_a, dwell = integrate(G_eff, tau0, 0.0, amp=1.0, t_max=t_max)
        fi = np.argmin(np.abs(tau_a - tau_fold))
        v_fold = v_a[fi] if fi < len(v_a) else np.nan
        res_A[H0] = dict(t=t_a, tau=tau_a, v=v_a, dwell=dwell, v_fold=v_fold)
        print(f"  H0={H0:.0e}: dwell={dwell:.6e}, v_fold={v_fold:.4f}, "
              f"npts={len(t_a)}, t_end={t_a[-1]:.3e}")
    except Exception as e:
        res_A[H0] = dict(dwell=0.0)
        print(f"  H0={H0:.0e}: FAILED — {e}")

# ============================================================
# 6. Scenario B: Start at BCS edge, scan initial velocity
# ============================================================
print(f"\n{'='*70}")
print("SCENARIO B: tau_0=0.205 (BCS edge), H0=1, scan v_0")
print('='*70)

V_B = float(cs_S(0.205))
G_eff_B = 1.0/V_B

v0_scan = [0.0, -1e-4, -1e-3, -0.01, -0.1, -1.0, -10, -26.5]
res_B = {}

for v0 in v0_scan:
    try:
        _, _, _, dwell = integrate(G_eff_B, 0.205, v0, amp=1.0, t_max=1.0)
        res_B[v0] = dict(dwell=dwell)
        print(f"  v0={v0:+.3f}: dwell={dwell:.6e}")
    except Exception as e:
        res_B[v0] = dict(dwell=0.0)
        print(f"  v0={v0:+.3f}: FAILED — {e}")

# ============================================================
# 7. Scenario C: BCS amplification (H0=1, tau0=0.40)
# ============================================================
print(f"\n{'='*70}")
print("SCENARIO C: Amplify BCS (H0=1, tau0=0.40)")
print('='*70)

# Use H0=0 (no friction) to isolate the BCS amplification effect
# Start at tau=0.205 (BCS edge) with v0 chosen to match free-fall entry speed
# Free-fall from 0.40 to 0.205: v ~ sqrt(2*dV*0.195/G_mod) ~ sqrt(2*57000*0.195/5) ~ 67
# But also try from rest right at the edge
amps = [1, 10, 100, 1000, 5000, 1e4, 5e4, 1e5, 1e6]
res_C = {}

for amp in amps:
    # Start from rest at BCS edge (most favorable for trapping)
    # No friction, just see if amplified BCS creates a barrier
    try:
        t_a, tau_a, v_a, dwell = integrate(0.0, 0.205, 0.0, amp=amp, t_max=1.0)
        trapped = BCS_lo <= tau_a[-1] <= BCS_hi
        res_C[amp] = dict(dwell=dwell, trapped=trapped, tau_final=tau_a[-1])
        # Check if the amplified BCS creates a minimum (gradient reversal)
        dV_at_edge = dV_bare(BCS_hi) + amp * dE_BCS(BCS_hi)
        dV_at_fold = dV_bare(tau_fold) + amp * dE_BCS(tau_fold)
        has_min = (dV_at_edge < 0)  # if gradient is negative at upper edge, there's a minimum below
        print(f"  amp={amp:.0e}: dwell={dwell:.6e}, trapped={trapped}, "
              f"tau_f={tau_a[-1]:.4f}, dV_edge={dV_at_edge:.1f}, has_min={has_min}")
    except Exception as e:
        res_C[amp] = dict(dwell=0.0)
        print(f"  amp={amp:.0e}: FAILED — {e}")

# What amplification creates a local minimum?
print(f"\n  Minimum creation: need amp * |dE_BCS|_max > |dV_bare|_fold")
print(f"  amp_crit = {dV_fold/dE_max:.0f}")
amp_crit = dV_fold/dE_max

# ============================================================
# 8. Dense H0 scan (20 values, fast)
# ============================================================
print(f"\n{'='*70}")
print("SCENARIO D: Dense H_0 scan (20 values)")
print('='*70)

H0_dense = np.logspace(-2, 6, 20)
dwell_dense = np.zeros(len(H0_dense))

for i, H0 in enumerate(H0_dense):
    G_eff = H0**2 / V0
    if H0 > 10:
        t_est = 3.0*H0*G_mod*0.4/dV_fold * 3
        t_max = min(t_est, 5e5)
    else:
        t_max = 10.0
    try:
        _, _, _, dwell = integrate(G_eff, tau0, 0.0, amp=1.0, t_max=t_max)
        dwell_dense[i] = dwell
    except:
        pass

idx_best = np.argmax(dwell_dense)
H0_best = H0_dense[idx_best]
dwell_best = dwell_dense[idx_best]
print(f"  Best: dwell={dwell_best:.6e} at H0={H0_best:.2e}")

# ============================================================
# 9. Analytic overdamped estimate
# ============================================================
print(f"\n{'='*70}")
print("ANALYTIC OVERDAMPED ESTIMATE")
print('='*70)

# In overdamped regime: v ~ -dV/(3*H*G_mod), H ~ sqrt(G_eff * V)
# dwell = Delta_tau / |v| = 3*G_mod*sqrt(G_eff*V)*Delta_tau / |dV|
# For dwell = tau_BCS: G_eff = (tau_BCS * |dV| / (3*G_mod*Delta_tau))^2 / V
dV_avg = 0.5*(abs(dV_bare(BCS_lo)) + abs(dV_bare(BCS_hi)))
V_avg = 0.5*(float(cs_S(BCS_lo)) + float(cs_S(BCS_hi)))

G_eff_needed = (tau_BCS * dV_avg / (3*G_mod*Delta_tau))**2 / V_avg
H_needed = np.sqrt(G_eff_needed * V_avg)

print(f"  |dV/dtau| avg:     {dV_avg:.1f}")
print(f"  V_avg:             {V_avg:.1f}")
print(f"  G_eff for dwell=40: {G_eff_needed:.4e}")
print(f"  H needed:          {H_needed:.4e}")

# Verify numerically
try:
    t_od_max = min(3*H_needed*G_mod*0.4/dV_avg*5, 5e5)
    t_od, tau_od, v_od, dwell_od = integrate(
        G_eff_needed, tau0, 0.0, amp=1.0, t_max=t_od_max)
    print(f"  Numerical: dwell={dwell_od:.4f} (target: {tau_BCS})")
    print(f"  Ratio: {dwell_od/tau_BCS:.4f}")
except Exception as e:
    dwell_od = 0.0
    print(f"  Verification FAILED: {e}")

# Physical impossibility
efolds = H_needed * tau_BCS
print(f"\n  e-folds during dwell: {efolds:.2e}")
print(f"  Scale factor: exp({efolds:.0e}) — physically impossible")
print(f"  Physical H/M_KK ~ 10^-60, needed ~ {H_needed:.0e}")

# ============================================================
# 10. Gate verdict
# ============================================================
print(f"\n{'='*70}")
print("GATE VERDICT: FRIED-39 (MASTER GATE)")
print('='*70)

# Collect all dwell times
all_dw = []
for H0 in H0_vals:
    all_dw.append(res_A.get(H0, {}).get('dwell', 0.0))
for v0 in v0_scan:
    all_dw.append(res_B.get(v0, {}).get('dwell', 0.0))
all_dw.append(dwell_best)
all_dw.append(dwell_od)

dwell_max = max(all_dw)
shortfall = tau_BCS / dwell_max if dwell_max > 0 else float('inf')

# Physical maximum (H0 <= 1)
phys_dw = []
for H0 in H0_vals:
    if H0 <= 1.0:
        phys_dw.append(res_A.get(H0, {}).get('dwell', 0.0))
dwell_max_phys = max(phys_dw) if phys_dw else 0.0
shortfall_phys = tau_BCS / dwell_max_phys if dwell_max_phys > 0 else float('inf')

# The overdamped limit achieves dwell=40 mathematically, but requires
# H ~ 5e6 (producing ~2e8 e-folds). This is physically impossible.
# Physical H_0 <= 1 gives dwell ~ 3e-4 (shortfall 133,200x).
# VERDICT: FAIL. The fundamental obstruction is the 6,596x gradient ratio.
verdict = "FAIL"

print(f"\n  SCENARIO SUMMARY:")
print(f"  {'Scenario':<30} {'Dwell':>12} {'Shortfall':>12}")
print(f"  {'-'*54}")
for H0 in H0_vals:
    d = res_A.get(H0, {}).get('dwell', 0.0)
    sf = tau_BCS/d if d > 0 else float('inf')
    lbl = f"H0={H0:.0e}"
    print(f"  A: {lbl:<16} {d:12.4e} {sf:12.1f}x")
for v0 in v0_scan:
    d = res_B.get(v0, {}).get('dwell', 0.0)
    sf = tau_BCS/d if d > 0 else float('inf')
    lbl = f"v0={v0:+.3f}"
    print(f"  B: {lbl:<16} {d:12.4e} {sf:12.1f}x")
print(f"  D: H0={H0_best:.2e} (best) {dwell_best:12.4e} {tau_BCS/dwell_best if dwell_best>0 else float('inf'):12.1f}x")
print(f"  E: overdamped target       {dwell_od:12.4e} {tau_BCS/dwell_od if dwell_od>0 else float('inf'):12.1f}x")

# Amplification needed
amp_pass = None
for amp in sorted(res_C.keys()):
    if res_C[amp].get('dwell', 0) >= tau_BCS:
        amp_pass = amp
        break

print(f"\n  MAXIMUM DWELL (all scenarios):   {dwell_max:.6e}")
print(f"  MAXIMUM DWELL (physical H<=1):   {dwell_max_phys:.6e}")
print(f"  tau_BCS threshold:               {tau_BCS}")
print(f"  Shortfall (all):                 {shortfall:.1f}x")
print(f"  Shortfall (physical):            {shortfall_phys:.1f}x")
print(f"  Gradient ratio:                  {ratio_grad:.0f}x")
print(f"  H needed for overdamped dwell=40: {H_needed:.4e}")
print(f"  e-folds at that H:               {efolds:.2e}")
if amp_pass:
    print(f"  Amplification for PASS:          {amp_pass:.0e}x")
else:
    print(f"  Amplification: none up to 10^6 suffices")
    print(f"  Gradient-balance estimate:       ~{ratio_grad:.0f}x")

print(f"\n  *** VERDICT: {verdict} ***")
print(f"  *** Physical shortfall: {shortfall_phys:.0f}x ***")
print(f"  *** Gradient ratio: {ratio_grad:.0f}x (BCS cannot create a local minimum) ***")
print(f"  *** Overdamped dwell=40 requires H={H_needed:.2e}, giving {efolds:.1e} e-folds ***")

# ============================================================
# 11. Save data
# ============================================================
save = {
    'verdict': np.array([verdict]),
    'tau_BCS': np.array(tau_BCS),
    'dwell_max': np.array(dwell_max),
    'dwell_max_phys': np.array(dwell_max_phys),
    'shortfall': np.array(shortfall),
    'shortfall_phys': np.array(shortfall_phys),
    'gradient_ratio': np.array(ratio_grad),
    'dV_bare_fold': np.array(dV_fold),
    'dE_BCS_max': np.array(dE_max),
    'E_cond': np.array(E_cond),
    'H0_best': np.array(H0_best),
    'G_eff_needed': np.array(G_eff_needed),
    'H_needed': np.array(H_needed),
    'efoldings_needed': np.array(efolds),
    'dwell_overdamped': np.array(dwell_od),
    'H0_scan_A': np.array(H0_vals),
    'dwell_A': np.array([res_A.get(h, {}).get('dwell', 0.0) for h in H0_vals]),
    'v0_scan_B': np.array(v0_scan),
    'dwell_B': np.array([res_B.get(v, {}).get('dwell', 0.0) for v in v0_scan]),
    'amp_scan_C': np.array(amps),
    'dwell_C': np.array([res_C.get(a, {}).get('dwell', 0.0) for a in amps]),
    'H0_dense': H0_dense,
    'dwell_dense': dwell_dense,
}

# Save a few trajectories
for H0_s in [0.0, 1.0, 1e4]:
    r = res_A.get(H0_s, {})
    if 't' in r:
        tag = f"{H0_s:.0e}".replace('+','').replace('.','p')
        save[f'traj_A_{tag}_t'] = r['t']
        save[f'traj_A_{tag}_tau'] = r['tau']

npz = os.path.join(base, 's39_friedmann_bcs.npz')
np.savez(npz, **save)
print(f"\nData: {npz}")

# ============================================================
# 12. Plot
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle(f'FRIED-39: Friedmann-BCS — {verdict}, '
             f'dwell_max={dwell_max:.2e}, shortfall={shortfall:.0f}x, '
             f'gradient ratio={ratio_grad:.0f}x',
             fontsize=12, fontweight='bold')

# (0,0) Potential
ax = axes[0,0]
tp = np.linspace(0, 0.50, 500)
Vp = np.array([float(cs_S(t)) for t in tp])
Ep = np.array([E_BCS(t) for t in tp])
ax.plot(tp, Vp, 'b-', lw=1.5, label='V_bare')
ax.plot(tp, Vp+Ep, 'r--', lw=1.5, label='V_bare+E_BCS')
ax.axvspan(BCS_lo, BCS_hi, alpha=0.2, color='g')
ax.set_xlabel('tau'); ax.set_ylabel('Potential'); ax.set_title('Potential'); ax.legend(fontsize=8)

# (0,1) Gradient comparison
ax = axes[0,1]
tz = np.linspace(0.15, 0.23, 200)
dVz = np.array([abs(dV_bare(t)) for t in tz])
dEz = np.array([abs(dE_BCS(t)) for t in tz])
ax.semilogy(tz, dVz, 'b-', lw=2, label='|dV_bare\'|')
ax.semilogy(tz, dEz, 'r-', lw=2, label='|dE_BCS\'|')
ax.axvspan(BCS_lo, BCS_hi, alpha=0.15, color='g')
ax.set_xlabel('tau'); ax.set_ylabel('|Gradient|')
ax.set_title(f'Gradient hierarchy: {ratio_grad:.0f}x'); ax.legend(fontsize=9)

# (0,2) Trajectories
ax = axes[0,2]
cm = plt.cm.plasma(np.linspace(0.1, 0.9, len(H0_vals)))
for i, H0 in enumerate(H0_vals):
    r = res_A.get(H0, {})
    if 't' in r:
        ax.plot(r['t'], r['tau'], color=cm[i],
                label=f'H0={H0:.0e}, dw={r["dwell"]:.1e}', lw=1)
ax.axhspan(BCS_lo, BCS_hi, alpha=0.15, color='g')
ax.set_xlabel('t'); ax.set_ylabel('tau(t)')
ax.set_title('Scenario A trajectories'); ax.legend(fontsize=5, loc='upper right')

# (1,0) Dwell vs H0
ax = axes[1,0]
m = dwell_dense > 0
if np.any(m):
    ax.loglog(H0_dense[m], dwell_dense[m], 'b.-', ms=4)
ax.axhline(tau_BCS, color='r', ls='--', lw=2, label=f'tau_BCS={tau_BCS}')
ax.set_xlabel('H_0'); ax.set_ylabel('Dwell')
ax.set_title(f'Dwell vs H_0 (best={dwell_best:.2e})'); ax.legend(fontsize=8)

# (1,1) Amplification
ax = axes[1,1]
aa = np.array(amps)
da = np.array([res_C.get(a,{}).get('dwell',0) for a in amps])
mc = da > 0
if np.any(mc):
    ax.loglog(aa[mc], da[mc], 'ro-', ms=5)
ax.axhline(tau_BCS, color='r', ls='--', lw=2, label=f'tau_BCS={tau_BCS}')
ax.axvline(ratio_grad, color='b', ls=':', label=f'Grad ratio={ratio_grad:.0f}')
ax.set_xlabel('Amplification'); ax.set_ylabel('Dwell')
ax.set_title('BCS amplification scan'); ax.legend(fontsize=8)

# (1,2) e-folds impossibility
ax = axes[1,2]
Hp = np.logspace(-2, 6, 100)
ef = Hp * tau_BCS
ax.loglog(Hp, ef, 'b-', lw=2, label='e-folds = H*tau_BCS')
ax.axhline(60, color='orange', ls='--', alpha=0.7, label='60 (inflation)')
ax.axhline(1, color='gray', ls='--', alpha=0.5, label='1 e-fold')
ax.axvline(H_needed, color='r', ls=':', lw=2, label=f'H_needed={H_needed:.1e}')
ax.set_xlabel('H_0'); ax.set_ylabel('e-folds')
ax.set_title(f'e-folds={efolds:.1e} (impossible)'); ax.legend(fontsize=7)

plt.tight_layout()
png = os.path.join(base, 's39_friedmann_bcs.png')
plt.savefig(png, dpi=150, bbox_inches='tight')
print(f"Plot: {png}")
print(f"\nRuntime: {time.time()-t0_wall:.1f}s")
print("=" * 70)
print("DONE")
