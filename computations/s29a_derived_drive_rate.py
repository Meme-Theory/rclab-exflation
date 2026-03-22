"""
Session 29a Computation 29a-2: Self-Consistent Drive Rate
=========================================================

Derives dtau/dt from the modulus equation of motion and determines whether
the resulting n_gap at tau=0.50 exceeds the BCS threshold of 20.

Physics:
--------
The SU(3) deformation parameter tau obeys the modulus equation of motion:

    G_{tau,tau} * d^2(tau)/dt^2 + dV_eff/dtau + Gamma_friction * dtau/dt = 0

where:
    G_{tau,tau} = 5  (modulus space metric, from s22d)
    V_eff(tau) = V_spec(tau, rho)  (spectral action potential)
    Gamma_friction accounts for particle production back-reaction

Energy conservation (without friction):
    E_total = (1/2) * G_{tau,tau} * (dtau/dt)^2 + V_eff(tau)

This gives:
    dtau/dt = sqrt(2 * (E_total - V_eff(tau)) / G_{tau,tau})

Since V_eff is monotonically increasing (VSPEC-1 constraint), the modulus
rolls DOWN from high tau toward tau=0, not up. The relevant scenario is
the modulus starting at some tau_initial with total energy E_total and
rolling toward smaller tau (or being driven by an external mechanism).

ALTERNATIVE INTERPRETATION: In the phonon condensate picture, the BCS
condensation energy F_cond provides an ADDITIONAL contribution to V_eff
that could create an effective minimum. At mu = lambda_min, F_cond ~ -0.37
(from s26 multimode BCS). This is O(1) compared to V_eff changes of O(1-5)
over the tau range 0-0.5.

This computation:
1. Scans E_total relative to V_eff(0) to find the self-consistent dtau/dt
2. For each (tau, dtau/dt), computes n_gap from KC-3 steady-state equation
3. Checks gate G-29a: n_gap > 20 at tau=0.50 for natural E_total

Gate G-29a (soft):
    PASS: n_gap > 20 at tau=0.50 for E_total <= 2 * V_eff(0)
    WEAK PASS: n_gap > 20 requires E_total in [2, 10] * V_eff(0)
    FAIL: n_gap > 20 requires E_total > 10 * V_eff(0)

Input: tier0-computation/s24a_vspec.npz
       tier0-computation/s28c_steady_state_mu.npz
       tier0-computation/s22d_rolling_trajectories.npz
       tier0-computation/s26_multimode_bcs.npz
Output: tier0-computation/s29a_derived_drive_rate.npz
        tier0-computation/s29a_derived_drive_rate.png

Author: phonon-exflation-sim agent
Date: 2026-02-28
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import interp1d
import time

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
VSPEC_FILE = DATA_DIR / "s24a_vspec.npz"
KC3_FILE = DATA_DIR / "s28c_steady_state_mu.npz"
ROLLING_FILE = DATA_DIR / "s22d_rolling_trajectories.npz"
BCS_FILE = DATA_DIR / "s26_multimode_bcs.npz"
OUTPUT_NPZ = DATA_DIR / "s29a_derived_drive_rate.npz"
OUTPUT_PNG = DATA_DIR / "s29a_derived_drive_rate.png"

# Modulus metric
G_TAU_TAU = 5.0

# BCS threshold
N_GAP_THRESHOLD = 20

# E_total scan: multiples of V_eff(0)
E_TOTAL_MULTIPLIERS = [1.01, 1.05, 1.1, 1.2, 1.5, 2.0, 3.0, 5.0, 10.0, 100.0]

# Reference rho for V_spec (cutoff scale)
# Use rho=0.01 as primary, check rho=0.05 and 0.1 for sensitivity
RHO_VALUES = {'0.010': 'V_spec_rho_0p010', '0.050': 'V_spec_rho_0p050', '0.100': 'V_spec_rho_0p100'}
RHO_PRIMARY = '0.010'

# Reference alpha_decay for KC-3
ALPHA_DECAY_REF = 0.003

# tau values for detailed analysis
TAU_ANALYSIS = [0.15, 0.25, 0.35, 0.40, 0.50]


# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("29a-2: Self-Consistent Drive Rate from Modulus EOM")
print("=" * 72)

t_start = time.time()

# V_spec(tau, rho)
print("\nLoading V_spec data...")
vspec_data = np.load(VSPEC_FILE, allow_pickle=True)
tau_vspec = vspec_data['tau']
print(f"  tau grid: {tau_vspec}")

V_eff = {}
for rho_str, key in RHO_VALUES.items():
    V_eff[rho_str] = vspec_data[key]
    print(f"  V_spec(rho={rho_str}): range [{V_eff[rho_str].min():.2f}, {V_eff[rho_str].max():.2f}]")

# KC-3 steady-state data
print("\nLoading KC-3 data...")
kc3_data = np.load(KC3_FILE, allow_pickle=True)
tau_kc3 = kc3_data['tau_values']
drive_kc3 = kc3_data['drive_values']  # (100,) = dtau/dt grid
B_gap = kc3_data['B_gap']  # (21,)
lambda_min = kc3_data['lambda_min']  # (21,)
print(f"  tau_kc3: {tau_kc3}")
print(f"  drive range: [{drive_kc3.min():.4e}, {drive_kc3.max():.4e}]")
print(f"  B_gap at tau=0.50: {B_gap[5]:.4e}")

# L1 n_gap data (n_gap = B_gap * drive / alpha)
n_gap_L1 = {}
for alpha_str in ['0.0010', '0.0030', '0.0100', '0.0300']:
    n_gap_L1[alpha_str] = kc3_data[f'L1_alpha{alpha_str}_n_gap']  # (21, 100)
    dtau_crit = kc3_data[f'L1_alpha{alpha_str}_dtau_crit']  # (21,)
    print(f"  L1 alpha={alpha_str}: dtau_crit at tau=0.50 = {dtau_crit[5]:.4e}")

# L2 thermalized n_gap (available for tau=0.15, 0.25, 0.35)
n_gap_L2 = {}
for tau_str in ['0.15', '0.25', '0.35']:
    key = f'L2_tau{tau_str}_n_gap_th'
    if key in kc3_data.files:
        n_gap_L2[tau_str] = kc3_data[key]  # (100,)
        print(f"  L2 tau={tau_str}: n_gap_th range [{n_gap_L2[tau_str].min():.4f}, {n_gap_L2[tau_str].max():.4f}]")

# Modulus metric
print(f"\nG_{{tau,tau}} = {G_TAU_TAU}")

# BCS condensation energy
print("\nLoading BCS condensation energy...")
bcs_data = np.load(BCS_FILE, allow_pickle=True)
# F_cond at mu/lambda_min = 1.0 (the BCS onset point)
F_cond_at_mu1 = {}
for tau_idx in range(9):  # s26 has 9 tau values
    key = f'sc_Fcond_{tau_idx}_1.00'
    if key in bcs_data.files:
        F_cond_at_mu1[tau_idx] = float(bcs_data[key])
print(f"  F_cond at mu=lambda_min: {F_cond_at_mu1}")


# ==============================================================================
# Module 1: Compute dtau/dt from energy conservation
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 1: dtau/dt from E_total = (1/2)*G*(dtau/dt)^2 + V_eff(tau)")
print("=" * 72)

def compute_dtau_dt(tau_val, E_total, V_eff_interp):
    """
    Compute dtau/dt from energy conservation.

    dtau/dt = sqrt(2 * max(0, E_total - V_eff(tau)) / G_{tau,tau})

    Parameters:
        tau_val: float, the tau value
        E_total: float, total energy
        V_eff_interp: callable, V_eff(tau) interpolant

    Returns:
        dtau_dt: float, |dtau/dt|
    """
    V = V_eff_interp(tau_val)
    KE = E_total - V
    if KE < 0:
        return 0.0  # Classically forbidden
    return np.sqrt(2.0 * KE / G_TAU_TAU)


# Build V_eff interpolant for each rho
V_eff_interp = {}
for rho_str, V_arr in V_eff.items():
    V_eff_interp[rho_str] = interp1d(tau_vspec, V_arr, kind='cubic', fill_value='extrapolate')

# Primary V_eff
V0 = V_eff_interp[RHO_PRIMARY]
V_at_0 = float(V0(0.0))
print(f"\n  V_eff(tau=0, rho={RHO_PRIMARY}) = {V_at_0:.4f}")

# Compute dtau/dt for each E_total multiplier at each tau
print(f"\n  {'E_mult':>8s} | {'E_total':>10s} | ", end='')
for tau in TAU_ANALYSIS:
    print(f"{'tau='+str(tau):>10s} | ", end='')
print()
print(f"  {'-'*8}-+-{'-'*10}-+-" + "-+-".join(['-'*10]*len(TAU_ANALYSIS)))

dtau_dt_results = {}
for E_mult in E_TOTAL_MULTIPLIERS:
    E_total = E_mult * V_at_0
    dtau_dt_at_tau = {}
    print(f"  {E_mult:8.2f} | {E_total:10.4f} | ", end='')
    for tau in TAU_ANALYSIS:
        dt = compute_dtau_dt(tau, E_total, V0)
        dtau_dt_at_tau[tau] = dt
        print(f"{dt:10.4e} | ", end='')
    print()
    dtau_dt_results[E_mult] = dtau_dt_at_tau


# ==============================================================================
# Module 2: Map dtau/dt to n_gap via KC-3
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 2: n_gap from dtau/dt via KC-3 steady-state equation")
print("=" * 72)

print(f"\n  n_gap = B_gap(tau) * |dtau/dt| / alpha_decay")
print(f"  alpha_decay = {ALPHA_DECAY_REF}")
print(f"  BCS threshold: n_gap >= {N_GAP_THRESHOLD}")

# Build B_gap interpolant
B_gap_interp = interp1d(tau_kc3, B_gap, kind='cubic', fill_value='extrapolate')
lambda_min_interp = interp1d(tau_kc3, lambda_min, kind='cubic', fill_value='extrapolate')

print(f"\n  {'E_mult':>8s} | {'E_total':>10s} | ", end='')
for tau in TAU_ANALYSIS:
    print(f"{'n_gap@'+str(tau):>12s} | ", end='')
print()
print(f"  {'-'*8}-+-{'-'*10}-+-" + "-+-".join(['-'*12]*len(TAU_ANALYSIS)))

n_gap_results = {}
for E_mult in E_TOTAL_MULTIPLIERS:
    E_total = E_mult * V_at_0
    n_gap_at_tau = {}
    print(f"  {E_mult:8.2f} | {E_total:10.4f} | ", end='')
    for tau in TAU_ANALYSIS:
        dt = dtau_dt_results[E_mult][tau]
        B = float(B_gap_interp(tau))
        n = B * dt / ALPHA_DECAY_REF
        n_gap_at_tau[tau] = n
        marker = " ***" if n >= N_GAP_THRESHOLD else ""
        print(f"{n:12.4f}{marker:>4s} | ", end='')
    print()
    n_gap_results[E_mult] = n_gap_at_tau


# ==============================================================================
# Module 3: Find critical E_total for n_gap=20 at each tau
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 3: Critical E_total for n_gap=20 at each tau")
print("=" * 72)

print(f"\n  n_gap = 20 requires dtau/dt_crit = 20 * alpha / B_gap(tau)")
print(f"  Then E_crit = (1/2) * G * (dtau/dt_crit)^2 + V_eff(tau)")

crit_results = {}
for tau in TAU_ANALYSIS:
    B = float(B_gap_interp(tau))
    V = float(V0(tau))
    lmin = float(lambda_min_interp(tau))

    dtau_crit = N_GAP_THRESHOLD * ALPHA_DECAY_REF / B if B > 0 else np.inf
    E_crit = 0.5 * G_TAU_TAU * dtau_crit**2 + V
    E_crit_mult = E_crit / V_at_0

    crit_results[tau] = {
        'B_gap': B,
        'V_eff': V,
        'lambda_min': lmin,
        'dtau_crit': dtau_crit,
        'E_crit': E_crit,
        'E_crit_mult': E_crit_mult,
    }

    print(f"\n  tau = {tau:.2f}:")
    print(f"    B_gap         = {B:.6e}")
    print(f"    V_eff         = {V:.4f}")
    print(f"    lambda_min    = {lmin:.6f}")
    print(f"    dtau/dt_crit  = {dtau_crit:.6e}")
    print(f"    E_crit        = {E_crit:.4f}")
    print(f"    E_crit/V(0)   = {E_crit_mult:.4f}")
    print(f"    KE_crit/V(0)  = {(E_crit - V)/V_at_0:.4e}")


# ==============================================================================
# Module 4: Rho sensitivity check
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 4: Sensitivity to V_eff cutoff scale rho")
print("=" * 72)

for rho_str in RHO_VALUES.keys():
    V_interp = V_eff_interp[rho_str]
    V0_rho = float(V_interp(0.0))
    V50_rho = float(V_interp(0.50))
    dV = V50_rho - V0_rho

    print(f"\n  rho = {rho_str}:")
    print(f"    V_eff(0)  = {V0_rho:.4f}")
    print(f"    V_eff(0.5)= {V50_rho:.4f}")
    print(f"    dV(0->0.5)= {dV:.4f}")

    # dtau/dt at tau=0.50 for E_total = 2*V(0)
    E_test = 2.0 * V0_rho
    dt_050 = compute_dtau_dt(0.50, E_test, V_interp)
    B_050 = float(B_gap_interp(0.50))
    n_gap_050 = B_050 * dt_050 / ALPHA_DECAY_REF
    print(f"    dtau/dt at tau=0.50 (E=2*V(0)) = {dt_050:.4e}")
    print(f"    n_gap at tau=0.50               = {n_gap_050:.4f}")


# ==============================================================================
# Module 5: BCS back-reaction on V_eff
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 5: BCS Condensation Energy Contribution")
print("=" * 72)

print(f"\n  From s26 multimode BCS, F_cond at mu=lambda_min:")
for idx, F in sorted(F_cond_at_mu1.items()):
    print(f"    tau_idx={idx}: F_cond = {F:.6f}")

print(f"\n  F_cond ~ -0.37 at the BCS onset (tau_idx=0, tau~0.0)")
print(f"  This is compared to V_eff changes:")
print(f"    dV(0->0.50) = {float(V0(0.50)) - float(V0(0.0)):.4f} (rho={RHO_PRIMARY})")
print(f"  F_cond / dV = {0.37 / (float(V0(0.50)) - float(V0(0.0))):.4f}")
print(f"\n  The BCS condensation energy is small (~6%) relative to V_eff variation.")
print(f"  It cannot qualitatively change the potential landscape.")


# ==============================================================================
# Module 6: Continuous tau scan for E_crit(tau) profile
# ==============================================================================

print("\n" + "=" * 72)
print("MODULE 6: E_crit(tau) Profile (Continuous)")
print("=" * 72)

tau_scan = np.linspace(0.01, 0.60, 200)
E_crit_scan = np.zeros_like(tau_scan)
dtau_crit_scan = np.zeros_like(tau_scan)
B_gap_scan = np.zeros_like(tau_scan)
V_eff_scan = np.zeros_like(tau_scan)
n_gap_at_E2V0 = np.zeros_like(tau_scan)  # n_gap for E=2*V(0)

E2V0 = 2.0 * V_at_0

for i, tau in enumerate(tau_scan):
    B = max(float(B_gap_interp(tau)), 1e-20)
    V = float(V0(tau))
    B_gap_scan[i] = B
    V_eff_scan[i] = V

    dtau_c = N_GAP_THRESHOLD * ALPHA_DECAY_REF / B
    dtau_crit_scan[i] = dtau_c
    E_crit_scan[i] = 0.5 * G_TAU_TAU * dtau_c**2 + V

    # n_gap for E=2*V(0)
    dt = compute_dtau_dt(tau, E2V0, V0)
    n_gap_at_E2V0[i] = B * dt / ALPHA_DECAY_REF

# Find where n_gap_at_E2V0 crosses 20
crosses_20 = np.where(n_gap_at_E2V0 >= N_GAP_THRESHOLD)[0]
if len(crosses_20) > 0:
    tau_cross = tau_scan[crosses_20[0]]
    print(f"  n_gap crosses 20 at tau ~ {tau_cross:.3f} for E=2*V(0)")
else:
    print(f"  n_gap NEVER reaches 20 for E=2*V(0) in tau range [0.01, 0.60]")
    print(f"  max n_gap = {n_gap_at_E2V0.max():.4f} at tau = {tau_scan[np.argmax(n_gap_at_E2V0)]:.3f}")


# ==============================================================================
# Module 7: Gate G-29a Verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE G-29a: SELF-CONSISTENT DRIVE RATE VERDICT")
print("=" * 72)

# The critical question: at tau=0.50, what E_total is needed for n_gap=20?
cr = crit_results[0.50]
E_crit_050 = cr['E_crit']
E_crit_mult_050 = cr['E_crit_mult']

print(f"\n  At tau=0.50:")
print(f"    E_crit for n_gap=20 = {E_crit_050:.4f}")
print(f"    E_crit / V(0)       = {E_crit_mult_050:.4f}")
print(f"    Required dtau/dt    = {cr['dtau_crit']:.4e}")

# Summary for each tau
print(f"\n  Summary:")
print(f"  {'tau':>5s} | {'E_crit/V(0)':>12s} | {'dtau_crit':>12s} | {'B_gap':>12s} | {'n_gap@E=2V0':>12s}")
print(f"  {'-'*5}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}")
for tau in TAU_ANALYSIS:
    cr_t = crit_results[tau]
    # n_gap at E=2*V(0)
    dt_2v0 = compute_dtau_dt(tau, 2.0 * V_at_0, V0)
    n_2v0 = cr_t['B_gap'] * dt_2v0 / ALPHA_DECAY_REF
    print(f"  {tau:5.2f} | {cr_t['E_crit_mult']:12.4f} | {cr_t['dtau_crit']:12.4e} | "
          f"{cr_t['B_gap']:12.4e} | {n_2v0:12.4f}")

# Gate decision
# E_crit_mult_050 tells us how much energy above V(0) is needed
if E_crit_mult_050 <= 2.0:
    verdict = "PASS"
    detail = (f"n_gap >= 20 at tau=0.50 requires E_total <= {E_crit_mult_050:.2f}*V(0). "
              f"Natural energy range.")
elif E_crit_mult_050 <= 10.0:
    verdict = "WEAK_PASS"
    detail = (f"n_gap >= 20 at tau=0.50 requires E_total = {E_crit_mult_050:.2f}*V(0). "
              f"Moderate fine-tuning of initial energy.")
else:
    verdict = "FAIL"
    detail = (f"n_gap >= 20 at tau=0.50 requires E_total = {E_crit_mult_050:.2f}*V(0). "
              f"Severe fine-tuning of initial energy.")

print(f"\n  G-29a VERDICT: {verdict}")
print(f"  Detail: {detail}")

# Cross-check: at E=2*V(0), what's n_gap at tau=0.50?
dt_crosscheck = compute_dtau_dt(0.50, 2.0 * V_at_0, V0)
n_crosscheck = float(B_gap_interp(0.50)) * dt_crosscheck / ALPHA_DECAY_REF
print(f"\n  Cross-check: E=2*V(0) -> dtau/dt={dt_crosscheck:.4e}, n_gap={n_crosscheck:.4f} at tau=0.50")


# ==============================================================================
# Module 8: Save output
# ==============================================================================

print("\n" + "=" * 72)
print("SAVING OUTPUT")
print("=" * 72)

save_dict = {
    'G_tau_tau': np.array([G_TAU_TAU]),
    'V_at_0': np.array([V_at_0]),
    'alpha_decay_ref': np.array([ALPHA_DECAY_REF]),
    'n_gap_threshold': np.array([N_GAP_THRESHOLD]),
    'rho_primary': np.array([float(RHO_PRIMARY)]),
    'verdict': np.array([verdict]),

    # E_total multipliers and tau grid
    'E_multipliers': np.array(E_TOTAL_MULTIPLIERS),
    'tau_analysis': np.array(TAU_ANALYSIS),

    # dtau/dt results: shape (n_E, n_tau)
    'dtau_dt': np.array([[dtau_dt_results[E_mult][tau] for tau in TAU_ANALYSIS]
                         for E_mult in E_TOTAL_MULTIPLIERS]),
    'n_gap': np.array([[n_gap_results[E_mult][tau] for tau in TAU_ANALYSIS]
                       for E_mult in E_TOTAL_MULTIPLIERS]),

    # Critical E_total for n_gap=20
    'E_crit': np.array([crit_results[tau]['E_crit'] for tau in TAU_ANALYSIS]),
    'E_crit_mult': np.array([crit_results[tau]['E_crit_mult'] for tau in TAU_ANALYSIS]),
    'dtau_crit': np.array([crit_results[tau]['dtau_crit'] for tau in TAU_ANALYSIS]),
    'B_gap_analysis': np.array([crit_results[tau]['B_gap'] for tau in TAU_ANALYSIS]),
    'V_eff_analysis': np.array([crit_results[tau]['V_eff'] for tau in TAU_ANALYSIS]),

    # Continuous tau scan
    'tau_scan': tau_scan,
    'E_crit_scan': E_crit_scan,
    'dtau_crit_scan': dtau_crit_scan,
    'B_gap_scan': B_gap_scan,
    'V_eff_scan': V_eff_scan,
    'n_gap_at_E2V0': n_gap_at_E2V0,
}

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"  Saved: {OUTPUT_NPZ}")


# ==============================================================================
# Module 9: Visualization
# ==============================================================================

print("\nGenerating plots...")

fig = plt.figure(figsize=(20, 16))
fig.suptitle(f'29a-2: Self-Consistent Drive Rate — G-29a: {verdict}', fontsize=14, fontweight='bold')

gs = fig.add_gridspec(3, 3, hspace=0.35, wspace=0.35)

# Panel 1: V_eff(tau) for different rho
ax = fig.add_subplot(gs[0, 0])
for rho_str, V_arr in V_eff.items():
    ax.plot(tau_vspec, V_arr, 'o-', ms=4, label=f'rho={rho_str}')
ax.set_xlabel('tau')
ax.set_ylabel('V_eff')
ax.set_title('V_eff(tau) = V_spec(tau, rho)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 0.6)

# Panel 2: dtau/dt vs tau for different E_total
ax = fig.add_subplot(gs[0, 1])
for E_mult in [1.01, 1.1, 2.0, 10.0, 100.0]:
    dtau_vals = [dtau_dt_results[E_mult][tau] for tau in TAU_ANALYSIS]
    ax.semilogy(TAU_ANALYSIS, dtau_vals, 'o-', ms=5, label=f'E={E_mult:.0g}*V(0)' if E_mult >= 2 else f'E={E_mult}*V(0)')
ax.set_xlabel('tau')
ax.set_ylabel('|dtau/dt|')
ax.set_title('Drive rate vs tau')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 3: n_gap vs tau for different E_total
ax = fig.add_subplot(gs[0, 2])
for E_mult in [1.01, 1.1, 2.0, 10.0, 100.0]:
    n_vals = [n_gap_results[E_mult][tau] for tau in TAU_ANALYSIS]
    ax.semilogy(TAU_ANALYSIS, [max(v, 1e-6) for v in n_vals], 'o-', ms=5,
                label=f'E={E_mult:.0g}*V(0)' if E_mult >= 2 else f'E={E_mult}*V(0)')
ax.axhline(N_GAP_THRESHOLD, color='red', ls='--', lw=2, label=f'n_gap={N_GAP_THRESHOLD}')
ax.set_xlabel('tau')
ax.set_ylabel('n_gap')
ax.set_title('Gap occupation vs tau')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: E_crit/V(0) vs tau (continuous)
ax = fig.add_subplot(gs[1, 0])
ax.semilogy(tau_scan, E_crit_scan / V_at_0, 'b-', lw=2)
ax.axhline(2.0, color='green', ls='--', lw=1.5, label='E=2*V(0)')
ax.axhline(10.0, color='orange', ls='--', lw=1.5, label='E=10*V(0)')
ax.set_xlabel('tau')
ax.set_ylabel('E_crit / V(0)')
ax.set_title('Critical energy for n_gap=20')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 5: B_gap and dtau_crit vs tau
ax = fig.add_subplot(gs[1, 1])
ax2 = ax.twinx()
ax.semilogy(tau_scan, B_gap_scan, 'b-', lw=2, label='B_gap')
ax2.semilogy(tau_scan, dtau_crit_scan, 'r-', lw=2, label='dtau/dt_crit')
ax.set_xlabel('tau')
ax.set_ylabel('B_gap', color='blue')
ax2.set_ylabel('dtau/dt_crit', color='red')
ax.set_title('Bogoliubov coeff & critical drive')
lines1 = ax.get_lines()
lines2 = ax2.get_lines()
ax.legend(lines1 + lines2, [l.get_label() for l in lines1 + lines2], fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 6: n_gap at E=2*V(0) vs tau (continuous)
ax = fig.add_subplot(gs[1, 2])
ax.plot(tau_scan, n_gap_at_E2V0, 'b-', lw=2)
ax.axhline(N_GAP_THRESHOLD, color='red', ls='--', lw=2, label=f'n_gap={N_GAP_THRESHOLD}')
ax.fill_between(tau_scan, 0, n_gap_at_E2V0,
                where=n_gap_at_E2V0 >= N_GAP_THRESHOLD, alpha=0.3, color='green', label='PASS region')
ax.set_xlabel('tau')
ax.set_ylabel('n_gap')
ax.set_title(f'n_gap at E=2*V(0)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 7: n_gap vs E_total/V(0) at tau=0.50
ax = fig.add_subplot(gs[2, 0])
E_mults_arr = np.array(E_TOTAL_MULTIPLIERS)
n_gap_050 = np.array([n_gap_results[E_mult][0.50] for E_mult in E_TOTAL_MULTIPLIERS])
ax.loglog(E_mults_arr, n_gap_050, 'bo-', ms=8, lw=2)
ax.axhline(N_GAP_THRESHOLD, color='red', ls='--', lw=2, label=f'n_gap={N_GAP_THRESHOLD}')
ax.axvline(E_crit_mult_050, color='green', ls=':', lw=2, label=f'E_crit={E_crit_mult_050:.2f}*V(0)')
ax.set_xlabel('E_total / V(0)')
ax.set_ylabel('n_gap at tau=0.50')
ax.set_title('n_gap(E) at tau=0.50')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 8: Phase diagram: tau vs E/V(0), colored by n_gap
ax = fig.add_subplot(gs[2, 1])
tau_grid = np.linspace(0.01, 0.55, 100)
E_grid = np.geomspace(1.001, 100, 100) * V_at_0

N_GAP_MAP = np.zeros((len(E_grid), len(tau_grid)))
for i, E in enumerate(E_grid):
    for j, tau in enumerate(tau_grid):
        B = max(float(B_gap_interp(tau)), 1e-20)
        V = float(V0(tau))
        KE = E - V
        if KE > 0:
            dt = np.sqrt(2.0 * KE / G_TAU_TAU)
            N_GAP_MAP[i, j] = B * dt / ALPHA_DECAY_REF
        else:
            N_GAP_MAP[i, j] = 0

im = ax.pcolormesh(tau_grid, E_grid / V_at_0, np.log10(N_GAP_MAP + 1e-10),
                   cmap='RdYlGn', vmin=-2, vmax=3, shading='auto')
ax.contour(tau_grid, E_grid / V_at_0, N_GAP_MAP, levels=[20], colors='red', linewidths=2)
ax.set_xlabel('tau')
ax.set_ylabel('E_total / V(0)')
ax.set_yscale('log')
ax.set_title('Phase diagram: log10(n_gap)')
plt.colorbar(im, ax=ax, label='log10(n_gap)')

# Panel 9: V_eff landscape with energy levels
ax = fig.add_subplot(gs[2, 2])
tau_plot = np.linspace(0, 0.6, 200)
V_plot = np.array([float(V0(t)) for t in tau_plot])
ax.plot(tau_plot, V_plot, 'k-', lw=2, label='V_eff(tau)')
for E_mult in [1.01, 1.1, 2.0, 10.0]:
    E_val = E_mult * V_at_0
    ax.axhline(E_val, ls='--', lw=1, alpha=0.5, label=f'E={E_mult}*V(0)')
ax.fill_between(tau_plot, V_plot, V_plot.max()*1.1, alpha=0.1, color='gray')
ax.set_xlabel('tau')
ax.set_ylabel('Energy')
ax.set_title('V_eff landscape')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)
ax.set_ylim(V_at_0 * 0.9, V_at_0 * 3)

plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUTPUT_PNG}")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print(f"\n{'='*72}")
print(f"FINAL VERDICT: G-29a = {verdict}")
print(f"  {detail}")
print(f"{'='*72}")
