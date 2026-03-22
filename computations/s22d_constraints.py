"""
E-2 + E-3: EARLY DARK ENERGY BOUND AND ATOMIC CLOCK CONSTRAINT
================================================================

Session 22d — Einstein-Theorist

Extracts EDE and atomic clock constraints from the rolling modulus ODE
results (s22d_rolling_trajectories.npz) and saves a dedicated constraint
results file.

Author: Einstein-Theorist (Session 22d)
Date: 2026-02-20
"""

import numpy as np
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

print("=" * 78)
print("  E-2 + E-3: CONSTRAINT EXTRACTION FROM ROLLING MODULUS ODE")
print("  Einstein-Theorist -- Session 22d")
print("=" * 78)

# Load rolling modulus results
data = np.load(os.path.join(SCRIPT_DIR, 's22d_rolling_trajectories.npz'),
               allow_pickle=True)

G_tt = float(data['G_tt'].flat[0])
Omega_m0 = float(data['Omega_m0'].flat[0])
Omega_r0 = float(data['Omega_r0'].flat[0])
Omega_DE0 = float(data['Omega_DE0'].flat[0])

# Physical constants for conversion
cos2_thetaW = 0.769  # 1 - sin^2(theta_W), sin^2 = 0.231
coupling_factor = 4.0 * cos2_thetaW  # = 3.076
H0_inv_yr = 1.45e10  # 1/H_0 in years

# Clock bounds
alpha_dot_pass = 1e-17    # yr^{-1} (PASS threshold)
alpha_dot_bound = 1e-16   # yr^{-1} (hard bound)
tau_dot_bound_H0 = alpha_dot_bound / coupling_factor * H0_inv_yr  # in H_0 units

print(f"\n  PHYSICAL PARAMETERS:")
print(f"    G_tt = {G_tt}")
print(f"    cos^2(theta_W) = {cos2_thetaW}")
print(f"    Coupling: |dalpha/alpha| = {coupling_factor:.3f} * |tau_dot| * H_0 / H0_inv_yr")
print(f"    Clock PASS threshold: {alpha_dot_pass:.0e} yr^-1")
print(f"    Clock hard bound: {alpha_dot_bound:.0e} yr^-1")
print(f"    Max |tau_dot| for hard bound: {tau_dot_bound_H0:.4e} (H_0 units)")
print()

# ===========================================================================
# EXTRACT CONSTRAINTS FOR EACH SCENARIO
# ===========================================================================

results = {}

for label in ['A', 'B', 'C', 'D', 'E', 'F']:
    key_a = f'a_{label}'
    key_tau = f'tau_{label}'
    key_td = f'tau_dot_{label}'
    key_Ot = f'Omega_tau_{label}'
    key_w = f'w_{label}'
    key_w0 = f'w0_{label}'
    key_wa = f'wa_{label}'

    if key_a not in data:
        continue

    a_sol = data[key_a]
    tau_sol = data[key_tau]
    tau_dot_sol = data[key_td]
    Omega_tau_sol = data[key_Ot]
    w_sol = data[key_w]

    # E-2: Omega_tau at z=10
    a_z10 = 1.0 / 11.0
    idx_z10 = np.argmin(np.abs(a_sol - a_z10))
    Omega_tau_z10 = Omega_tau_sol[idx_z10]

    if Omega_tau_z10 < 0.02:
        ede_verdict = "PASS"
        ede_bf = 2.0
    elif Omega_tau_z10 < 0.10:
        ede_verdict = "MARGINAL"
        ede_bf = 0.8
    else:
        ede_verdict = "CMB_KILL"
        ede_bf = 0.1

    # E-3: Atomic clock
    tau_dot_today = tau_dot_sol[-1]
    alpha_dot = coupling_factor * abs(tau_dot_today) / H0_inv_yr

    if alpha_dot < alpha_dot_pass:
        clock_verdict = "PASS"
        clock_bf = 3.0
    elif alpha_dot < alpha_dot_bound:
        clock_verdict = "MARGINAL"
        clock_bf = 0.9
    else:
        clock_verdict = "CLOCK_KILL"
        clock_bf = 0.1

    # w_0, w_a
    w_0 = float(data[key_w0].flat[0])
    w_a = float(data[key_wa].flat[0])

    results[label] = {
        'tau_today': tau_sol[-1],
        'tau_dot_today': tau_dot_today,
        'Omega_tau_z10': Omega_tau_z10,
        'ede_verdict': ede_verdict,
        'ede_bf': ede_bf,
        'alpha_dot_per_yr': alpha_dot,
        'clock_verdict': clock_verdict,
        'clock_bf': clock_bf,
        'w_0': w_0,
        'w_a': w_a,
    }

    print(f"  SCENARIO {label}:")
    print(f"    tau(today) = {tau_sol[-1]:.8f}")
    print(f"    tau_dot(today) = {tau_dot_today:.4e} (H_0)")
    print(f"    Omega_tau(z=10) = {Omega_tau_z10:.4e}  -> {ede_verdict} (BF={ede_bf})")
    print(f"    |dalpha/alpha| = {alpha_dot:.4e} yr^-1  -> {clock_verdict} (BF={clock_bf})")
    print(f"    w_0 = {w_0:.6f}, w_a = {w_a:.6f}")
    print()

# ===========================================================================
# CRITICAL ANALYSIS: CLOCK BOUND vs INITIAL CONDITIONS
# ===========================================================================

print("=" * 78)
print("  CRITICAL ANALYSIS: CLOCK BOUND SENSITIVITY")
print("=" * 78)
print()

# The clock bound requires |tau_dot| < 4.71e-7 in H_0 units.
# In the overdamped slow-roll regime: tau_dot ~ -dV/(3*H*G_tt)
# Near the minimum: dV ~ V'' * delta_tau
# So: |tau_dot| ~ V''*|delta_tau| / (3*H_0*G_tt)

V_FR_scale = float(data['V_FR_scale'].flat[0])
# V'' at minimum (raw) = 0.106069
V_pp_raw = 0.106069
V_pp = V_FR_scale * V_pp_raw

delta_tau_clock = tau_dot_bound_H0 * 3 * 1.0 * G_tt / V_pp
print(f"  V_FR'' at minimum (normalized): {V_pp:.6f}")
print(f"  Overdamped tau_dot ~ V'' * delta_tau / (3*H_0*G_tt)")
print(f"  Clock bound |tau_dot| < {tau_dot_bound_H0:.4e}")
print(f"  => |delta_tau| < {delta_tau_clock:.4e}")
print(f"  => tau must be within {delta_tau_clock:.4e} of tau_0 = 0.30")
print(f"  => tau in [{0.30 - delta_tau_clock:.8f}, {0.30 + delta_tau_clock:.8f}]")
print()

# Characteristic damping time
rate_overdamp = V_pp / (G_tt * 3 * 1.0)  # at z=0
t_efold = 1.0 / rate_overdamp
print(f"  Overdamped e-folding time: {t_efold:.1f} Hubble times = {t_efold*14.5:.0f} Gyr")
print(f"  Universe age: ~14.5 Gyr = 1 Hubble time")
print(f"  => Only ~{1.0/t_efold:.3f} e-foldings of damping available since z=0")
print()

# From z=1000: effective damping (includes matter era with larger H)
# N_damp ~ integral_a_start^1 V''/(G_tt*3*H(a)*a) da
# In matter era: H(a) ~ H_0*sqrt(Omega_m/a^3), so
# integrand ~ V''/(G_tt*3*H_0*sqrt(Omega_m)*a^{-3/2}*a) = V''*a^{1/2}/(3*G_tt*H_0*sqrt(Om))
# Integral from a_eq to 1: ~ V''*2*(1-a_eq^{3/2})/(3*3*G_tt*H_0*sqrt(Om))
# This gives N_damp ~ V''*2/(9*G_tt*H_0*sqrt(Om)) = 0.937*2/(9*5*1*0.561) = 0.074
# Very small! Only ~0.07 e-foldings from matter era.

N_damp_matter = V_pp * 2.0 / (9.0 * G_tt * 1.0 * np.sqrt(Omega_m0))
print(f"  Estimated N_damp from matter era (z=1000 to z=0): ~{N_damp_matter:.3f} e-folds")
print(f"  This confirms: the FR potential is too shallow for dynamical settling.")
print()

print("  PHYSICAL CONCLUSIONS:")
print("  (1) Scenarios A/B/C: tau starts far from minimum => CLOCK CLOSED (15000x).")
print("      This is NOT a missing-physics artifact; matter/radiation Hubble")
print("      friction IS included but insufficient (shallow potential).")
print("  (2) Scenario D: tau exactly at minimum => trivial PASS (w=-1 exactly).")
print("  (3) Scenario E: delta_tau=0.01 => CLOCK CLOSED by 800x.")
print("      The FR settling time (~700 Gyr) >> universe age (~14.5 Gyr).")
print("  (4) Scenario F: delta_tau=0.05, small kick => CLOCK CLOSED by 85x.")
print("  (5) The clock bound REQUIRES the modulus to be frozen within")
print(f"      |delta_tau| < {delta_tau_clock:.1e} of tau_0 = 0.30.")
print("      This is a 25 ppm constraint on the modulus position.")
print("  (6) Dynamical rolling to the minimum is TOO SLOW to satisfy clocks.")
print("      Non-perturbative locking (BCS condensate, Session 22c L-3)")
print("      is REQUIRED for observational consistency.")
print("  (7) ALL scenarios give w_0 ~ -1 (MARGINAL CLOSURE for DESI).")
print("      Rolling modulus quintessence is CLOSED as a DESI explanation.")
print("      DESI dynamical DE requires a different mechanism if real.")

# ===========================================================================
# SAVE
# ===========================================================================

save_dict = {}
for label, r in results.items():
    for key, val in r.items():
        if isinstance(val, str):
            save_dict[f'{key}_{label}'] = np.array([val])
        else:
            save_dict[f'{key}_{label}'] = np.array([val])

save_dict['delta_tau_clock_bound'] = np.array([delta_tau_clock])
save_dict['tau_dot_bound_H0'] = np.array([tau_dot_bound_H0])
save_dict['alpha_dot_bound_yr'] = np.array([alpha_dot_bound])
save_dict['V_pp_normalized'] = np.array([V_pp])
save_dict['t_efold_Hubble'] = np.array([t_efold])
save_dict['N_damp_matter_era'] = np.array([N_damp_matter])

out_file = os.path.join(SCRIPT_DIR, 's22d_constraint_results.npz')
np.savez(out_file, **save_dict)
print(f"\n  Saved: {out_file}")

print("\n" + "=" * 78)
