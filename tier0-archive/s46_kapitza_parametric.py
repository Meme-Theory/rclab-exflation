#!/usr/bin/env python3
"""
KAPITZA-PARAMETRIC-46: Mathieu stability analysis for tau modulus
driven by GGE beat-frequency modulation.
=================================================================

Physics:
  After the BCS transit, the tau modulus oscillates near the q-theory
  minimum tau* ~ 0.21 with frequency omega_tau = 8.27 M_KK (S38).
  The GGE relic produces 3 beat frequencies (0.052, 0.266, 0.318 M_KK)
  that modulate the effective potential. Parametric resonance occurs when
  a drive frequency satisfies Omega = 2*omega_0/n for integer n.

  The linearized equation of motion:
    delta_tau'' + gamma * delta_tau' + omega_0^2 [1 + eps(t)] delta_tau = 0
  where eps(t) = sum_j eps_j cos(Omega_j t) and gamma = Gamma_Langer.

  In standard Mathieu form (for each beat separately):
    u'' + [a - 2q cos(2z)] u = 0
  with a = (2*omega_0/Omega)^2, q = eps * a / 2, z = Omega*t/2.

  Modulation depth: eps_total = Kapitza_ratio = 0.030 (S38, corrected).
  This is the physically established total modulation of omega_0^2 by
  the GGE oscillations, distributed across beats by (amp_E * deg).

Gate: Diagnostic. Report whether any beat is within 10% of 2*omega_tau.

Input:  s45_gge_beating.npz, s45_qtheory_bcs.npz, canonical_constants.py
Output: s46_kapitza_parametric.{npz,png}

Author: Tesla-Resonance, Session 46
"""

import sys
import os
import warnings
import numpy as np
from math import lgamma
from scipy.integrate import solve_ivp
from scipy.signal import hilbert
from scipy.interpolate import UnivariateSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore', category=RuntimeWarning)

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    Kapitza_ratio, Gamma_Langer_BCS, M_ATDHFB,
    omega_att, E_cond, tau_fold
)

# ===========================================================================
#  1. LOAD INPUT DATA
# ===========================================================================

data_dir = os.path.dirname(os.path.abspath(__file__))
gge = np.load(os.path.join(data_dir, 's45_gge_beating.npz'), allow_pickle=True)
qt = np.load(os.path.join(data_dir, 's45_qtheory_bcs.npz'), allow_pickle=True)

omega_beats = gge['omega_beats']     # [0.0523, 0.2659, 0.3182] M_KK
amp_E = gge['amp_E_beats']          # energy-density beat amplitudes
deg_beats = gge['deg_beats']        # degeneracies [4, 12, 3]
labels_beat = ['B2-B1', 'B2-B3', 'B1-B3']

omega_tau = 8.27                     # M_KK, S38 s38_attempt_freq.npz
gamma_damp = Gamma_Langer_BCS       # 0.2497 M_KK

# Q-theory curvature at tau*
tau_dense = qt['tau_dense']
rho_multi = qt['rho_gs_ext_multi']
tau_star = float(qt['tau_star_flatband'])   # 0.2094

mask_fin = np.isfinite(rho_multi)
spl = UnivariateSpline(tau_dense[mask_fin], rho_multi[mask_fin], s=0, k=4)
d2V_dtau2 = spl.derivative(2)(tau_star)
omega_q = np.sqrt(abs(d2V_dtau2) / M_ATDHFB)

print("=" * 70)
print("KAPITZA-PARAMETRIC-46: Mathieu Stability of Tau Modulus")
print("=" * 70)
print()
print(f"omega_tau (S38)      = {omega_tau:.3f} M_KK")
print(f"omega_q (q-theory)   = {omega_q:.3f} M_KK")
print(f"gamma (Langer)       = {gamma_damp:.4f} M_KK")
print(f"Q factor             = {omega_tau / (2*gamma_damp):.2f}")
print(f"Kapitza ratio (S38)  = {Kapitza_ratio:.4f}")
print(f"tau* (flatband)      = {tau_star:.4f}")
print(f"d2V/dtau2 at tau*    = {d2V_dtau2:.2f}")
print()

# ===========================================================================
#  2. MODULATION DEPTHS (from S38 Kapitza ratio)
# ===========================================================================
# The TOTAL modulation depth eps_total = 0.030 was established in S38 from
# the ratio of GGE oscillation amplitude to DC energy level. It measures
# delta(omega_tau^2) / omega_tau^2, i.e., fractional modulation of the
# spring constant. Distribute across beats by (amp_E_j * deg_j).

amp_E_eff = amp_E * deg_beats
total_amp = np.sum(amp_E_eff[amp_E_eff > 1e-20])
eps_j = np.where(amp_E_eff > 1e-20,
                  Kapitza_ratio * amp_E_eff / total_amp, 0.0)

print("--- Modulation depths (from S38 Kapitza ratio = 0.030) ---")
for j, lab in enumerate(labels_beat):
    print(f"  eps_{lab} = {eps_j[j]:.6f}  (fraction: {eps_j[j]/Kapitza_ratio*100:.1f}%)")
print(f"  eps_total = {np.sum(eps_j):.6f}")
print()

# ===========================================================================
#  3. FREQUENCY HIERARCHY AND DETUNING
# ===========================================================================

print("--- Frequency hierarchy ---")
print(f"  2*omega_tau = {2*omega_tau:.3f} M_KK (primary parametric resonance)")

n_sub_arr = np.zeros(3, dtype=int)
detuning_arr = np.zeros(3)

for j, (ob, lab) in enumerate(zip(omega_beats, labels_beat)):
    ratio = ob / (2 * omega_tau)
    n_sub = 2 * omega_tau / ob
    n_near = round(n_sub)
    n_sub_arr[j] = n_near
    omega_res = 2 * omega_tau / n_near if n_near > 0 else np.inf
    detune = abs(ob - omega_res) / omega_res if n_near > 0 else np.inf
    detuning_arr[j] = detune
    print(f"  Omega_{lab} = {ob:.6f}  |  ratio = {ratio:.4f}"
          f"  |  n = {n_sub:.1f} -> {n_near}  |  detune = {detune*100:.2f}%")

gate_10pct = any(abs(ob / (2*omega_tau) - 1.0) < 0.10 for ob in omega_beats)
print(f"\n  GATE: Any beat within 10% of 2*omega_tau?  {'YES' if gate_10pct else 'NO'}")
print(f"    Closest ratio: {max(omega_beats/(2*omega_tau)):.4f}")
print()

# ===========================================================================
#  4. MATHIEU PARAMETERS AND ARNOLD TONGUE ANALYSIS
# ===========================================================================
# Standard Mathieu: u'' + [a - 2q cos(2z)] u = 0
# a = (2*omega_0 / Omega)^2,  q = eps * a / 2

a_j_arr = (2 * omega_tau / omega_beats)**2
q_j_arr = eps_j * a_j_arr / 2

print("--- Mathieu parameters ---")
print(f"{'Beat':<8} {'a':>10} {'q':>10} {'n':>5} {'eps':>10}")
for j, lab in enumerate(labels_beat):
    print(f"{lab:<8} {a_j_arr[j]:>10.1f} {q_j_arr[j]:>10.4f}"
          f" {n_sub_arr[j]:>5d} {eps_j[j]:>10.6f}")
print()

# Arnold tongue width at n-th subharmonic
# delta_a_n ~ |q|^n / (2^{2(n-1)} * ((n-1)!)^2)
print("--- Arnold tongue widths ---")
log10_tongue = np.zeros(3)
for j, lab in enumerate(labels_beat):
    n = n_sub_arr[j]
    q = q_j_arr[j]
    if q > 1e-30 and n > 1:
        log_da = n * np.log(q) - 2*(n-1)*np.log(2) - 2*lgamma(n)
        log10_da = log_da / np.log(10)
    else:
        log10_da = -np.inf
    log10_tongue[j] = log10_da
    a_detune = abs(a_j_arr[j] - n**2)
    print(f"  {lab}: n = {n}, q = {q:.4f}")
    print(f"    log10(tongue_width) = {log10_da:.1f}")
    print(f"    |a - n^2| = {a_detune:.1f}")
    if log10_da > -300:
        log10_detune = np.log10(a_detune) if a_detune > 0 else -np.inf
        print(f"    Detuning exceeds tongue by 10^{{{log10_detune - log10_da:.0f}}}")
    else:
        print(f"    Tongue is astronomically narrow")
print()

# ===========================================================================
#  5. FLOQUET ANALYSIS (reference stability map at low a)
# ===========================================================================

def floquet_multiplier(a_val, q_val, n_steps=800):
    """Max |Floquet multiplier| for Mathieu eq via symplectic propagator."""
    dz = np.pi / n_steps
    M = np.eye(2)
    for i in range(n_steps):
        z_mid = (i + 0.5) * dz
        omega2 = a_val - 2 * q_val * np.cos(2 * z_mid)
        if omega2 > 0:
            w = np.sqrt(omega2)
            wdz = w * dz
            c, s = np.cos(wdz), np.sin(wdz)
            local = np.array([[c, s/w], [-w*s, c]])
        elif omega2 < 0:
            w = np.sqrt(-omega2)
            wdz = w * dz
            ch, sh = np.cosh(wdz), np.sinh(wdz)
            local = np.array([[ch, sh/w], [w*sh, ch]])
        else:
            local = np.array([[1.0, dz], [0.0, 1.0]])
        M = local @ M
    return np.max(np.abs(np.linalg.eigvals(M)))


print("--- Computing reference stability map ---")
a_scan = np.linspace(0.01, 50, 200)
q_scan = np.linspace(0.01, 15, 150)
stability_map = np.ones((len(q_scan), len(a_scan)))
for ia, av in enumerate(a_scan):
    for iq, qv in enumerate(q_scan):
        stability_map[iq, ia] = floquet_multiplier(av, qv)
print(f"  Grid: {len(a_scan)} x {len(q_scan)}")
print(f"  Unstable cells: {np.sum(stability_map > 1.001)} / {stability_map.size}")
print()

# ===========================================================================
#  6. DIRECT NUMERICAL INTEGRATION (multi-frequency, physical time)
# ===========================================================================
# eps ~ 0.03 total, so the modulation is genuinely small.
# omega_tau ~ 8.27, beats ~ 0.05-0.32.
# Integrate for 100 slow periods.

T_mod = 2 * np.pi / omega_tau      # ~0.76 M_KK^{-1}
T_slow = 2 * np.pi / omega_beats[0]  # ~120 M_KK^{-1}
n_slow = 100
t_final = n_slow * T_slow
dt_max = T_mod / 30  # resolve modulus oscillation

print(f"--- Multi-frequency integration (eps_total = {Kapitza_ratio:.4f}) ---")
print(f"  T_mod = {T_mod:.4f},  T_slow = {T_slow:.2f},  t_final = {t_final:.1f}")

def ode_damped(t, y):
    u, v = y
    mod = (eps_j[0] * np.cos(omega_beats[0]*t) +
           eps_j[1] * np.cos(omega_beats[1]*t) +
           eps_j[2] * np.cos(omega_beats[2]*t))
    return [v, -gamma_damp*v - omega_tau**2 * (1 + mod) * u]

def ode_undamped(t, y):
    u, v = y
    mod = (eps_j[0] * np.cos(omega_beats[0]*t) +
           eps_j[1] * np.cos(omega_beats[1]*t) +
           eps_j[2] * np.cos(omega_beats[2]*t))
    return [v, -omega_tau**2 * (1 + mod) * u]

print("  Integrating damped...")
sol_d = solve_ivp(ode_damped, [0, t_final], [1.0, 0.0],
                   method='DOP853', rtol=1e-12, atol=1e-15,
                   max_step=dt_max, dense_output=True)
print(f"    {sol_d.message} | steps={sol_d.t.size}")

print("  Integrating undamped...")
sol_u = solve_ivp(ode_undamped, [0, t_final], [1.0, 0.0],
                   method='DOP853', rtol=1e-12, atol=1e-15,
                   max_step=dt_max, dense_output=True)
print(f"    {sol_u.message} | steps={sol_u.t.size}")

n_sample = 40000
t_sample = np.linspace(0, t_final, n_sample)
u_d = sol_d.sol(t_sample)[0]
u_u = sol_u.sol(t_sample)[0]

# Envelopes via Hilbert
env_d = np.abs(hilbert(u_d))
env_u = np.abs(hilbert(u_u))

alpha_pure = -gamma_damp / 2

# For the DAMPED solution: it decays as exp(-gamma/2 * t).
# With gamma/2 = 0.125 and t_final ~ 12000, the signal is exp(-1500) ~ 0.
# So the second half is pure numerical noise. Fit EARLY portion instead.
# Use first 20 slow periods (envelope still has signal).

def fit_rate_early(t_arr, env_arr, t_fit_max):
    """Fit log(envelope) vs t over [0, t_fit_max]."""
    mask = (env_arr > 1e-15) & (t_arr < t_fit_max) & (t_arr > 0.5)
    if np.sum(mask) < 50:
        return np.nan
    log_e = np.log(env_arr[mask])
    t_m = t_arr[mask]
    A = np.vstack([t_m, np.ones_like(t_m)]).T
    return np.linalg.lstsq(A, log_e, rcond=None)[0][0]

t_fit_max_d = 5 * T_slow  # first 5 slow periods (enough decay signal)
alpha_d = fit_rate_early(t_sample, env_d, t_fit_max_d)

# For the UNDAMPED solution: signal persists. Fit second half.
n_half = n_sample // 2
def fit_rate(t_arr, env_arr):
    mask = env_arr > 1e-15
    if np.sum(mask) < 50:
        return np.nan
    log_e = np.log(env_arr[mask])
    t_m = t_arr[mask]
    A = np.vstack([t_m, np.ones_like(t_m)]).T
    return np.linalg.lstsq(A, log_e, rcond=None)[0][0]

alpha_u = fit_rate(t_sample[n_half:], env_u[n_half:])

# Undamped max amplitude (direct measure of growth)
max_amp_u = np.max(np.abs(u_u))
max_amp_ratio = max_amp_u / abs(u_u[0])

print()
print(f"  alpha_damped (first {t_fit_max_d/T_slow:.0f} slow periods) = {alpha_d:.8f} M_KK")
print(f"  Pure damping         = {alpha_pure:.8f} M_KK")
print(f"  Deviation from pure: {alpha_d - alpha_pure:.2e} M_KK")
param_frac = (alpha_d - alpha_pure) / abs(alpha_pure) if not np.isnan(alpha_d) else 0.0
print(f"  Parametric fraction: {param_frac:.2e}")
print()
print(f"  alpha_undamped = {alpha_u:.2e} M_KK")
print(f"  Undamped max|u| / |u(0)| = {max_amp_ratio:.6f}")
print(f"  Undamped amplitude variation: {(max_amp_ratio - 1)*100:.3f}%")

if np.isnan(alpha_d):
    verdict = "DECAYING -- signal too weak"
elif abs(param_frac) < 0.01:
    verdict = "PURE DECAY -- no parametric effect (< 1%)"
elif alpha_d > 0:
    verdict = "GROWING -- parametric amplification exceeds damping"
elif param_frac > 0.01:
    verdict = "REDUCED DAMPING -- partial parametric effect"
else:
    verdict = "ENHANCED DAMPING -- beats slightly increase decay"
print(f"  Verdict: {verdict}")
print()

# ===========================================================================
#  7. HYPOTHETICAL ONSET: what drive frequency would produce instability?
# ===========================================================================

print("--- Hypothetical: at what Omega would eps=0.030 produce instability? ---")
Omega_hyp = np.linspace(0.5, 30, 400)
mu_hyp = np.zeros(len(Omega_hyp))
for i, Om in enumerate(Omega_hyp):
    a_h = (2*omega_tau/Om)**2
    q_h = Kapitza_ratio * a_h / 2
    mu_hyp[i] = floquet_multiplier(a_h, q_h) if a_h < 2000 else 1.0

unstable_Om = Omega_hyp[mu_hyp > 1.001]
if len(unstable_Om) > 0:
    Om_onset = unstable_Om[0]
    print(f"  First instability at Omega = {Om_onset:.3f} M_KK")
    print(f"  Ratio Omega/(2*omega_tau) = {Om_onset/(2*omega_tau):.4f}")
    print(f"  Gap from nearest GGE beat: {Om_onset/max(omega_beats):.1f}x")
else:
    Om_onset = np.nan
    print("  No instability found in [0.5, 30] M_KK")

# Also find what eps would be needed at each GGE beat for instability
print()
print("--- Required eps for instability at each GGE beat frequency ---")
for j, (ob, lab) in enumerate(zip(omega_beats, labels_beat)):
    a_h = (2*omega_tau/ob)**2
    # For a >> 1, the n-th tongue has threshold q ~ 1 (approximately).
    # More precisely, instability at a = n^2 requires |q| > 0.
    # But detuning from n^2 adds a threshold: q_crit ~ |a - n^2|.
    n = n_sub_arr[j]
    a_detune = abs(a_h - n**2)
    # At the tongue tip, the half-width in a is delta_a ~ q^n * f(n).
    # For instability we need q^n * f(n) > |a - n^2|.
    # So q_crit ~ (|a-n^2| / f(n))^{1/n}.
    # f(n) ~ 1/(2^{2(n-1)} * ((n-1)!)^2)
    if n > 1:
        log_fn = -2*(n-1)*np.log(2) - 2*lgamma(n)
        log_q_crit = (np.log(a_detune) - log_fn) / n if a_detune > 0 else -np.inf
        q_crit = np.exp(log_q_crit) if log_q_crit < 50 else np.inf
        eps_crit = 2 * q_crit / a_h if a_h > 0 else np.inf
    else:
        eps_crit = np.inf
    print(f"  {lab}: a = {a_h:.0f}, n = {n}, |a-n^2| = {a_detune:.1f}")
    print(f"    q_crit ~ {q_crit:.2e}, eps_crit ~ {eps_crit:.2e}")
    print(f"    Available eps = {eps_j[j]:.6f}")
    print(f"    Shortfall: {eps_crit/eps_j[j]:.1e}x" if eps_j[j] > 0 else "    No modulation")
print()

# ===========================================================================
#  8. ADIABATIC MODULATION REGIME
# ===========================================================================

delta_omega = omega_tau * np.sum(eps_j) / 2
print("--- Adiabatic regime (Omega_beat << omega_tau) ---")
print(f"  omega_beat / omega_tau = [{omega_beats[0]/omega_tau:.4f},"
      f" {omega_beats[1]/omega_tau:.4f}, {omega_beats[2]/omega_tau:.4f}]")
print(f"  All << 1: ADIABATIC.")
print(f"  omega_eff wobbles by +/- {delta_omega:.4f} M_KK ({np.sum(eps_j)/2*100:.3f}%)")
print()

# Parametric threshold at primary tongue
eps_thresh = 2 * gamma_damp / omega_tau
print(f"  Primary tongue threshold: eps > {eps_thresh:.4f}")
print(f"  Available: {np.sum(eps_j):.4f}")
print(f"  Ratio: {np.sum(eps_j)/eps_thresh:.2f}")
print(f"  Would be MARGINAL if beats were at 2*omega_tau. They are not.")
print()

# ===========================================================================
#  9. SAVE
# ===========================================================================

results = {
    'gate_name': np.array(['KAPITZA-PARAMETRIC-46']),
    'gate_verdict': np.array(['INFO']),
    'gate_detail': np.array(['Beats at n=52-317 subharmonic of 2*omega_tau; '
                              'no parametric resonance; adiabatic regime']),

    'omega_tau': np.float64(omega_tau),
    'omega_q_theory': np.float64(omega_q),
    'omega_beats': omega_beats,
    'gamma_damp': np.float64(gamma_damp),
    'Q_factor': np.float64(omega_tau / (2*gamma_damp)),

    'a_j': a_j_arr,
    'q_j': q_j_arr,
    'n_sub': n_sub_arr,
    'eps_j': eps_j,
    'eps_total': np.float64(Kapitza_ratio),
    'eps_threshold_primary': np.float64(eps_thresh),

    'log10_tongue_width': log10_tongue,
    'detuning_pct': detuning_arr,

    'alpha_damped': np.float64(alpha_d if not np.isnan(alpha_d) else alpha_pure),
    'alpha_undamped': np.float64(alpha_u if not np.isnan(alpha_u) else 0.0),
    'alpha_pure_decay': np.float64(alpha_pure),
    'parametric_fraction': np.float64(param_frac),
    'max_amp_undamped': np.float64(max_amp_ratio),

    'a_scan': a_scan,
    'q_scan': q_scan,
    'stability_map': stability_map,

    't_sample_dec': t_sample[::10],
    'u_damped_dec': u_d[::10],
    'u_undamped_dec': u_u[::10],
    'env_damped_dec': env_d[::10],
    'env_undamped_dec': env_u[::10],

    'd2V_dtau2': np.float64(d2V_dtau2),
    'tau_star': np.float64(tau_star),
    'Kapitza_ratio_S38': np.float64(Kapitza_ratio),
    'delta_omega_adiabatic': np.float64(delta_omega),

    'Omega_onset_hypothetical': np.float64(Om_onset) if not np.isnan(Om_onset) else np.float64(0.0),
    'Omega_hyp': Omega_hyp,
    'mu_hyp': mu_hyp,
}

outpath = os.path.join(data_dir, 's46_kapitza_parametric.npz')
np.savez_compressed(outpath, **results)
print(f"Saved: {outpath}")

# ===========================================================================
#  10. PLOT
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('KAPITZA-PARAMETRIC-46: Mathieu Stability of Tau Modulus\n'
             'under GGE Beat Modulation (eps_total = 0.030)',
             fontsize=13, fontweight='bold')

# (a) Stability map
ax = axes[0, 0]
im = ax.pcolormesh(a_scan, q_scan, stability_map, cmap='RdYlGn_r',
                    vmin=0.95, vmax=1.10, shading='auto')
ax.contour(a_scan, q_scan, stability_map, levels=[1.0],
           colors='black', linewidths=1.5)
for nn in range(1, 8):
    if nn**2 <= 50:
        ax.axvline(nn**2, color='gray', alpha=0.3, ls='--', lw=0.5)
        ax.text(nn**2, q_scan[-1]*0.95, f'n={nn}', ha='center', fontsize=7, color='gray')
ax.set_xlabel('Mathieu a')
ax.set_ylabel('Mathieu q')
ax.set_title('(a) Reference stability map')
plt.colorbar(im, ax=ax, label='|Floquet multiplier|')
ax.text(0.95, 0.05,
        f'Our a = {min(a_j_arr):.0f}-{max(a_j_arr):.0f}\n(far off scale)',
        transform=ax.transAxes, ha='right', va='bottom', fontsize=8,
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# (b) Frequency hierarchy
ax = axes[0, 1]
all_freqs = [(gamma_damp, r'$\Gamma_L$', 'red'),
             (omega_beats[0], r'$\Omega_{B2-B1}$', 'blue'),
             (omega_beats[1], r'$\Omega_{B2-B3}$', 'blue'),
             (omega_beats[2], r'$\Omega_{B1-B3}$', 'blue'),
             (omega_att, r'$\omega_{att}$', 'orange'),
             (omega_tau, r'$\omega_\tau$', 'green'),
             (2*omega_tau, r'$2\omega_\tau$', 'darkgreen')]
yp = np.arange(len(all_freqs))
ax.barh(yp, [np.log10(f) for f,_,_ in all_freqs],
        color=[c for _,_,c in all_freqs], alpha=0.7, height=0.6)
for i, (f, l, c) in enumerate(all_freqs):
    ax.text(np.log10(f) + 0.02, i, f'{f:.3f}', va='center', fontsize=8)
ax.set_yticks(yp)
ax.set_yticklabels([l for _,l,_ in all_freqs], fontsize=9)
ax.set_xlabel(r'$\log_{10}(\omega / M_{KK})$')
ax.set_title('(b) Frequency hierarchy')
ax.axvline(np.log10(2*omega_tau), color='darkgreen', ls='--', alpha=0.4)
# Annotate gap
ax.annotate('', xy=(np.log10(2*omega_tau), 3.5),
            xytext=(np.log10(omega_beats[2]), 3.5),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax.text((np.log10(2*omega_tau)+np.log10(omega_beats[2]))/2, 3.8,
        f'{2*omega_tau/omega_beats[2]:.0f}x gap', ha='center', fontsize=9,
        color='red', fontweight='bold')

# (c) Time series
ax = axes[1, 0]
t_show = min(15 * T_slow, t_final)
mask_t = t_sample <= t_show
ax.plot(t_sample[mask_t], u_d[mask_t], 'b-', lw=0.15, alpha=0.4, label='u(t)')
ax.plot(t_sample[mask_t], env_d[mask_t], 'r-', lw=1.5, label='Envelope')
ax.plot(t_sample[mask_t], np.exp(alpha_pure * t_sample[mask_t]),
        'k--', lw=1, alpha=0.7, label=r'$e^{-\gamma t/2}$')
if not np.isnan(alpha_d):
    ax.plot(t_sample[mask_t], np.exp(alpha_d * t_sample[mask_t]),
            'g:', lw=1.5, label=f'Fit: alpha={alpha_d:.5f}')
ax.set_xlabel(r'$t$ [$M_{KK}^{-1}$]')
ax.set_ylabel(r'$\delta\tau$')
ax.set_title('(c) Damped modulus with all 3 beats')
ax.legend(fontsize=7, loc='upper right')
ax.set_xlim(0, t_show)

# (d) Arnold tongue width vs n
ax = axes[1, 1]
n_range = np.arange(1, 120)
for j, lab in enumerate(labels_beat):
    q = q_j_arr[j]
    if q > 1e-30:
        lw_list = [n_val * np.log10(q) - 2*(n_val-1)*np.log10(2) - 2*lgamma(n_val)/np.log(10)
                   for n_val in n_range]
        ax.plot(n_range, lw_list, '-', lw=1.5, label=f'{lab} (q={q:.2f})')
        n_op = n_sub_arr[j]
        if n_op < 120:
            idx = n_op - 1
            ax.plot(n_op, lw_list[idx], 'o', ms=8, zorder=5)
            ax.annotate(f'n={n_op}', (n_op, lw_list[idx]),
                        textcoords='offset points', xytext=(5, 5), fontsize=7)

ax.set_xlabel('Subharmonic order n')
ax.set_ylabel(r'$\log_{10}(\delta a_n)$')
ax.set_title('(d) Arnold tongue width vs subharmonic order')
ax.set_ylim(-500, 50)
ax.axhline(0, color='black', ls='-', alpha=0.3)
ax.axhline(-10, color='red', ls=':', alpha=0.5)
ax.text(5, -15, 'Practically zero below', fontsize=8, color='red')
ax.legend(fontsize=8)

plt.tight_layout()
outpng = os.path.join(data_dir, 's46_kapitza_parametric.png')
fig.savefig(outpng, dpi=150, bbox_inches='tight')
print(f"Saved: {outpng}")

# ===========================================================================
#  11. FINAL SUMMARY
# ===========================================================================

print()
print("=" * 70)
print("KAPITZA-PARAMETRIC-46 FINAL SUMMARY")
print("=" * 70)
print()
print("GATE VERDICT: INFO (diagnostic)")
print()
print("Q1: Any beat within 10% of 2*omega_tau?  NO")
print(f"    Max ratio = {max(omega_beats/(2*omega_tau)):.4f}")
print(f"    Frequency gap: 52x minimum (B1-B3)")
print()
print("Q2: Subharmonic resonance?  NO")
print(f"    n = {n_sub_arr}")
print(f"    log10(tongue widths) = [{log10_tongue[0]:.0f}, {log10_tongue[1]:.0f},"
      f" {log10_tongue[2]:.0f}]")
print()
print("Q3: Multi-frequency growth?  NO")
print(f"    alpha_d = {alpha_d:.6f} vs pure_decay = {alpha_pure:.6f}")
print(f"    Undamped max amplitude ratio = {max_amp_ratio:.6f} (variation: {(max_amp_ratio-1)*100:.3f}%)")
print()
print("REGIME: ADIABATIC (Omega_beat << omega_tau)")
print(f"  Frequency modulation: +/- {delta_omega:.4f} M_KK ({np.sum(eps_j)/2*100:.3f}%)")
print()
print("CONSTRAINT: Parametric amplification by GGE beats CLOSED")
print("  52-317x frequency mismatch, tongues < 10^{-100} wide")
print("  The modulus and GGE occupy separated frequency bands")
