#!/usr/bin/env python3
"""
GEOD-39: Geodesic Mass Variation Cross-Check
=============================================
Independent cross-check on KK mass spectrum from W3-1
using classical geodesic mass variation from Paper 15.

Physics:
  The Jensen metric on SU(3) has scale factors (Paper 15, eq 3.68):
    lambda_1(tau) = exp(2*tau)   [u(1) direction, dim=1]
    lambda_2(tau) = exp(-2*tau)  [su(2) directions, dim=3]
    lambda_3(tau) = exp(tau)     [C^2 directions, dim=4]

  The Dirac operator eigenvalues E_k(tau) on (SU(3), g^tau) give the
  "classical" KK mass at each tau. The BdG mass from W3-1 includes
  pairing effects on top of this geometric contribution.

  This computation:
    1. Extracts E_k^{Dirac}(tau) from the (0,0) sector eigenvalues
    2. Computes dm^2/dtau along the transit geodesic
    3. Integrates mass variation from tau_init to tau_exit
    4. Compares classical m_k(tau) with BdG masses
    5. Estimates pair creation from classical mass variation rate

Input:
  - tier0-computation/s39_kk_mass.npz (W3-1 BdG masses)
  - tier0-computation/s27_multisector_bcs.npz (Dirac eigenvalues vs tau)
  - tier0-computation/s36_tau_dynamics.npz (terminal velocity)

Output:
  - tier0-computation/s39_geodesic_mass.npz

Gate: GEOD-39 (INFO cross-check, agreement within 50%)
"""

import numpy as np
from scipy.interpolate import CubicSpline

# ============================================================
# 1. Load input data
# ============================================================

d_mass = np.load('tier0-computation/s39_kk_mass.npz', allow_pickle=True)
d_spec = np.load('tier0-computation/s27_multisector_bcs.npz', allow_pickle=True)
d_dyn = np.load('tier0-computation/s36_tau_dynamics.npz', allow_pickle=True)

tau_grid = d_spec['tau_values']  # [0.0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]
tau_exit_values = d_mass['tau_exit_values']  # [0.205, 0.25, 0.50]
branch_labels = d_mass['branch_labels']
tau_fold = float(d_dyn['tau_fold'])
v_terminal = float(d_dyn['an_S_singlet_v_terminal'])
omega_att = 1.430  # From S38, fully geometric

print("=" * 70)
print("GEOD-39: Geodesic Mass Variation Cross-Check")
print("=" * 70)

# ============================================================
# 2. Extract 3 energy levels from (0,0) sector Dirac eigenvalues
# ============================================================

# The (0,0) sector has 16 eigenvalues that split into 3 levels:
#   B1: degeneracy 2  (u(1) direction)
#   B2: degeneracy 8  (C^2 directions)
#   B3: degeneracy 6  (su(2) directions)

E_B1 = np.zeros(len(tau_grid))
E_B2 = np.zeros(len(tau_grid))
E_B3 = np.zeros(len(tau_grid))

for i, tau in enumerate(tau_grid):
    evals = d_spec[f'evals_0_0_{i}']
    unique_abs = np.sort(np.unique(np.round(np.abs(evals), 8)))
    if len(unique_abs) == 1:
        # tau=0: all degenerate
        E_B1[i] = E_B2[i] = E_B3[i] = unique_abs[0]
    else:
        E_B1[i] = unique_abs[0]   # smallest (u(1), lambda_1 = e^{2tau})
        E_B2[i] = unique_abs[1]   # middle (C^2, lambda_3 = e^{tau})
        E_B3[i] = unique_abs[-1]  # largest (su(2), lambda_2 = e^{-2tau})

print("\n--- Dirac eigenvalues |E_k(tau)| in (0,0) sector ---")
print(f"{'tau':>6s}  {'E_B1':>10s}  {'E_B2':>10s}  {'E_B3':>10s}")
for i, tau in enumerate(tau_grid):
    print(f"{tau:6.3f}  {E_B1[i]:10.6f}  {E_B2[i]:10.6f}  {E_B3[i]:10.6f}")

# ============================================================
# 3. Cubic spline interpolation for continuous E_k(tau)
# ============================================================

cs_B1 = CubicSpline(tau_grid, E_B1)
cs_B2 = CubicSpline(tau_grid, E_B2)
cs_B3 = CubicSpline(tau_grid, E_B3)

# Derivatives: dE/dtau
dcs_B1 = cs_B1.derivative()
dcs_B2 = cs_B2.derivative()
dcs_B3 = cs_B3.derivative()

# ============================================================
# 4. Classical mass^2 and its variation along geodesic
# ============================================================

# Classical KK mass: m_k^{classical}(tau) = E_k^{Dirac}(tau)
# Classical mass^2: m_k^2(tau) = E_k^2(tau)
# Rate: d(m^2)/dtau = 2 * E_k * dE_k/dtau

print("\n--- d(m^2)/dtau at key tau values ---")
print(f"{'tau':>6s}  {'dm2_B1/dtau':>12s}  {'dm2_B2/dtau':>12s}  {'dm2_B3/dtau':>12s}")
for tau in [0.0, 0.10, 0.15, 0.19, 0.20, 0.205, 0.25, 0.30, 0.50]:
    dm2_B1 = 2 * cs_B1(tau) * dcs_B1(tau)
    dm2_B2 = 2 * cs_B2(tau) * dcs_B2(tau)
    dm2_B3 = 2 * cs_B3(tau) * dcs_B3(tau)
    print(f"{tau:6.3f}  {dm2_B1:12.6f}  {dm2_B2:12.6f}  {dm2_B3:12.6f}")

# ============================================================
# 5. Paper 15 eq (3.84): C^2 gauge boson mass^2
# ============================================================

def m2_C2_gauge(sigma):
    """
    Mass^2 of C^2 gauge bosons from Paper 15 eq (3.84).
    Returns f(sigma) proportional to m^2, up to overall constant.
    """
    return np.exp(sigma) * (
        (np.exp(sigma) - np.exp(-2*sigma))**2 +
        (1 - np.exp(-sigma))**2
    ) / 5.0

# Derivative: d(m^2)/dsigma analytically
def dm2_C2_gauge(sigma):
    """Derivative of m^2(sigma) for C^2 gauge bosons."""
    # Numerical derivative for reliability
    ds = 1e-8
    return (m2_C2_gauge(sigma + ds) - m2_C2_gauge(sigma - ds)) / (2 * ds)

print("\n--- Paper 15 C^2 gauge boson mass^2 (eq 3.84) ---")
print(f"{'tau':>6s}  {'m2_gauge':>12s}  {'dm2/dtau':>12s}")
for tau in [0.0, 0.10, 0.15, 0.20, 0.205, 0.25, 0.30, 0.50]:
    print(f"{tau:6.3f}  {m2_C2_gauge(tau):12.8f}  {dm2_C2_gauge(tau):12.8f}")

# ============================================================
# 6. Accumulated mass variation along transit geodesic
# ============================================================

# Transit direction: tau decreases from large values toward fold
# tau_init is the starting point (we use tau=0.50 as the "far field")
tau_init = 0.50

print("\n" + "=" * 70)
print("ACCUMULATED MASS VARIATION: tau_init = %.3f -> tau_exit" % tau_init)
print("=" * 70)

results = {}

for j, tau_exit in enumerate(tau_exit_values):
    print(f"\n--- tau_exit = {tau_exit:.3f} ---")

    # Integrate d(m^2)/dtau from tau_init to tau_exit
    # Note: transit goes from high tau to low tau, so integral is negative range
    tau_fine = np.linspace(tau_init, tau_exit, 10000)

    # Classical mass at tau_init and tau_exit
    E_B1_init = cs_B1(tau_init)
    E_B2_init = cs_B2(tau_init)
    E_B3_init = cs_B3(tau_init)

    E_B1_exit = cs_B1(tau_exit)
    E_B2_exit = cs_B2(tau_exit)
    E_B3_exit = cs_B3(tau_exit)

    # Classical mass^2 change
    Delta_m2_B1 = E_B1_exit**2 - E_B1_init**2
    Delta_m2_B2 = E_B2_exit**2 - E_B2_init**2
    Delta_m2_B3 = E_B3_exit**2 - E_B3_init**2

    # Also integrate directly to verify
    dm2_B1_integrand = 2 * cs_B1(tau_fine) * dcs_B1(tau_fine)
    dm2_B2_integrand = 2 * cs_B2(tau_fine) * dcs_B2(tau_fine)
    dm2_B3_integrand = 2 * cs_B3(tau_fine) * dcs_B3(tau_fine)

    Delta_m2_B1_int = np.trapezoid(dm2_B1_integrand, tau_fine)
    Delta_m2_B2_int = np.trapezoid(dm2_B2_integrand, tau_fine)
    Delta_m2_B3_int = np.trapezoid(dm2_B3_integrand, tau_fine)

    print(f"  Delta(m^2) [direct]:    B1={Delta_m2_B1:+.6f}  B2={Delta_m2_B2:+.6f}  B3={Delta_m2_B3:+.6f}")
    print(f"  Delta(m^2) [integral]:  B1={Delta_m2_B1_int:+.6f}  B2={Delta_m2_B2_int:+.6f}  B3={Delta_m2_B3_int:+.6f}")
    print(f"  Consistency check:      B1={abs(Delta_m2_B1 - Delta_m2_B1_int):.2e}  "
          f"B2={abs(Delta_m2_B2 - Delta_m2_B2_int):.2e}  "
          f"B3={abs(Delta_m2_B3 - Delta_m2_B3_int):.2e}")

    # Classical mass at exit
    m_B1_classical = E_B1_exit
    m_B2_classical = E_B2_exit
    m_B3_classical = E_B3_exit

    # BdG mass at exit (from W3-1)
    E_bdg = d_mass[f'tau{j}_E_bdg_mf']
    m_B2_bdg = E_bdg[0]   # B2[0]-B2[3] all same
    m_B1_bdg = E_bdg[4]   # B1
    m_B3_bdg = E_bdg[5]   # B3[0]-B3[2] all same

    # Ratios
    ratio_B1 = m_B1_bdg / m_B1_classical
    ratio_B2 = m_B2_bdg / m_B2_classical
    ratio_B3 = m_B3_bdg / m_B3_classical

    print(f"\n  Classical mass (Dirac): B1={m_B1_classical:.6f}  B2={m_B2_classical:.6f}  B3={m_B3_classical:.6f}")
    print(f"  BdG mass (W3-1):       B1={m_B1_bdg:.6f}  B2={m_B2_bdg:.6f}  B3={m_B3_bdg:.6f}")
    print(f"  Ratio BdG/classical:   B1={ratio_B1:.4f}  B2={ratio_B2:.4f}  B3={ratio_B3:.4f}")

    within_50 = (0.5 <= ratio_B1 <= 1.5) or (0.5 <= ratio_B2 <= 1.5) or (0.5 <= ratio_B3 <= 1.5)
    print(f"  Any branch within 50%: {within_50}")

    results[f'tau_exit_{j}'] = {
        'tau_exit': tau_exit,
        'E_classical': np.array([m_B2_classical]*4 + [m_B1_classical] + [m_B3_classical]*3),
        'E_bdg': E_bdg,
        'ratio': np.array([ratio_B2]*4 + [ratio_B1] + [ratio_B3]*3),
        'Delta_m2': np.array([Delta_m2_B2]*4 + [Delta_m2_B1] + [Delta_m2_B3]*3),
    }

# ============================================================
# 7. Paper 15 gauge boson mass vs Dirac eigenvalue comparison
# ============================================================

print("\n" + "=" * 70)
print("PAPER 15 GAUGE BOSON MASS vs DIRAC EIGENVALUE RATIOS")
print("=" * 70)

# The gauge boson mass formula (3.84) applies to C^2 modes (= B3 in our labeling?
# Actually: the gauge bosons associated to e_a^L with e_a in C^2 subspace get mass.
# In the Dirac spectrum, B3 has degeneracy 6 = 2*dim(su(2)), while C^2 has dim 4.
# Let me re-examine the identification.

# From the degeneracy pattern:
#   B1 (deg 2) = u(1) direction (dim 1, *2 for chirality)
#   B2 (deg 8) = C^2 directions (dim 4, *2 for chirality)
#   B3 (deg 6) = su(2) directions (dim 3, *2 for chirality)

# Paper 15 says:
#   - Bosons associated to u(2) subspace remain MASSLESS
#   - Bosons associated to C^2 subspace get mass from eq (3.84)

# u(2) = u(1) + su(2), dim = 1 + 3 = 4
# C^2 complement, dim = 4

# So the gauge boson mass from (3.84) applies to the C^2 directions = B2 in eigenvalue labeling!
# (B2 has degeneracy 8 = 2 * dim(C^2) = 2 * 4, checks out)

# The gauge boson mass grows from zero at tau=0.
# The Dirac eigenvalue for B2 starts at sqrt(3)/2 at tau=0 and ALSO varies.
# These are different objects: gauge boson mass vs Dirac eigenvalue.

# But we can check if the VARIATION of the Dirac eigenvalue^2 tracks the
# gauge boson mass^2 variation.

# For the C^2 modes: define
#   delta_E^2(tau) = E_B2^2(tau) - E_B2^2(0) = E_B2^2(tau) - 3/4
# and compare with
#   m^2_gauge(tau) from (3.84)

print("\nC^2 (B2) modes: Dirac eigenvalue^2 shift vs gauge boson mass^2")
print(f"{'tau':>6s}  {'E_B2^2':>10s}  {'delta_E^2':>10s}  {'m2_gauge':>10s}  {'ratio':>10s}")
E0_sq = 0.75  # (sqrt(3)/2)^2 = 3/4
for i, tau in enumerate(tau_grid):
    if tau == 0:
        print(f"{tau:6.3f}  {E_B2[i]**2:10.6f}  {0.0:10.6f}  {0.0:10.6f}  {'---':>10s}")
    else:
        delta = E_B2[i]**2 - E0_sq
        mg = m2_C2_gauge(tau)
        ratio = delta / mg if mg > 1e-10 else float('inf')
        print(f"{tau:6.3f}  {E_B2[i]**2:10.6f}  {delta:+10.6f}  {mg:10.6f}  {ratio:10.4f}")

# ============================================================
# 8. Pair creation lower bound from classical geodesic
# ============================================================

print("\n" + "=" * 70)
print("PAIR CREATION LOWER BOUND FROM CLASSICAL MASS VARIATION")
print("=" * 70)

# From Landau-Zener / Schwinger pair creation:
#   delta_n ~ |Delta(m^2)| / (2 * m * omega_att)
# where omega_att = 1.430 (attractive mode frequency from S38)
# and m is evaluated at the midpoint of the transit

# The quantum result from W3-1: n_Bog = 0.999 (Bogoliubov pair number)
# This is per mode pair, from sudden quench analysis

n_Bog_quantum = 0.999  # From S38 sudden quench

print(f"\nomega_att = {omega_att:.3f}")
print(f"n_Bog (quantum) = {n_Bog_quantum:.3f}")

for j, tau_exit in enumerate(tau_exit_values):
    print(f"\n--- tau_exit = {tau_exit:.3f} ---")

    # Use B2 modes (dominant pairing, 93% GGE weight)
    E_B2_init_val = cs_B2(tau_init)
    E_B2_exit_val = cs_B2(tau_exit)
    E_B2_mid = cs_B2((tau_init + tau_exit) / 2)

    Delta_m2 = abs(E_B2_exit_val**2 - E_B2_init_val**2)
    m_mid = E_B2_mid

    # Classical estimate
    delta_n_classical = Delta_m2 / (2 * m_mid * omega_att)

    # Also compute from velocity:
    # d(m^2)/dt = d(m^2)/dtau * dtau/dt = d(m^2)/dtau * v_terminal
    dm2_dtau_at_fold = 2 * cs_B2(tau_fold) * dcs_B2(tau_fold)
    dm2_dt_at_fold = dm2_dtau_at_fold * abs(v_terminal)

    # Adiabaticity parameter: gamma = omega^2 / |dm^2/dt|
    gamma_adiab = omega_att**2 / abs(dm2_dt_at_fold) if abs(dm2_dt_at_fold) > 1e-15 else float('inf')

    print(f"  Delta(m^2_B2) = {Delta_m2:.6f}")
    print(f"  m_mid(B2) = {m_mid:.6f}")
    print(f"  delta_n (classical LB) = {delta_n_classical:.4f}")
    print(f"  delta_n / n_Bog = {delta_n_classical / n_Bog_quantum:.4f}")
    print(f"  dm^2/dtau at fold = {dm2_dtau_at_fold:.6f}")
    print(f"  dm^2/dt at fold = {dm2_dt_at_fold:.6f}")
    print(f"  Adiabaticity gamma = {gamma_adiab:.4f}")

# ============================================================
# 9. Detailed 8-mode comparison table
# ============================================================

print("\n" + "=" * 70)
print("FULL 8-MODE COMPARISON TABLE")
print("=" * 70)

E_init_8 = np.array([cs_B2(tau_init)]*4 + [cs_B1(tau_init)] + [cs_B3(tau_init)]*3)

for j, tau_exit in enumerate(tau_exit_values):
    print(f"\n--- tau_exit = {tau_exit:.3f} ---")

    # Classical
    E_exit_classical = np.array(
        [cs_B2(tau_exit)]*4 + [cs_B1(tau_exit)] + [cs_B3(tau_exit)]*3
    )

    # BdG
    E_bdg = d_mass[f'tau{j}_E_bdg_mf']

    # 8-mode E_8 from W3-1
    E_8 = d_mass[f'tau{j}_E_8']

    print(f"  {'Mode':>6s}  {'E_Dirac':>10s}  {'E_8(W3-1)':>10s}  {'E_BdG':>10s}  {'BdG/Dirac':>10s}  {'within50':>8s}")
    for k in range(8):
        ratio = E_bdg[k] / E_exit_classical[k]
        w50 = "YES" if 0.5 <= ratio <= 1.5 else "NO"
        print(f"  {branch_labels[k]:>6s}  {E_exit_classical[k]:10.6f}  {E_8[k]:10.6f}  {E_bdg[k]:10.6f}  {ratio:10.4f}  {w50:>8s}")

    # Check: E_exit_classical should match E_8 (they're the same thing)
    max_dev = np.max(np.abs(E_exit_classical - E_8) / E_8)
    print(f"  Max deviation E_classical vs E_8: {max_dev:.2e}")

# ============================================================
# 10. Gate verdict
# ============================================================

print("\n" + "=" * 70)
print("GATE VERDICT: GEOD-39")
print("=" * 70)

# At tau_exit = 0.50: all ratios should be ~1 (no pairing effect)
E_bdg_05 = d_mass['tau2_E_bdg_mf']
E_class_05 = np.array([cs_B2(0.50)]*4 + [cs_B1(0.50)] + [cs_B3(0.50)]*3)
ratios_05 = E_bdg_05 / E_class_05
max_deviation_05 = np.max(np.abs(ratios_05 - 1))

# At tau_exit = 0.25: B3 should be close to 1, B2 enhanced
E_bdg_025 = d_mass['tau1_E_bdg_mf']
E_class_025 = np.array([cs_B2(0.25)]*4 + [cs_B1(0.25)] + [cs_B3(0.25)]*3)
ratios_025 = E_bdg_025 / E_class_025

# At tau_exit = 0.205: strong pairing enhancement
E_bdg_0205 = d_mass['tau0_E_bdg_mf']
E_class_0205 = np.array([cs_B2(0.205)]*4 + [cs_B1(0.205)] + [cs_B3(0.205)]*3)
ratios_0205 = E_bdg_0205 / E_class_0205

# Count modes within 50% at each tau_exit
n_within_50 = []
for ratios in [ratios_0205, ratios_025, ratios_05]:
    n = np.sum((ratios >= 0.5) & (ratios <= 1.5))
    n_within_50.append(n)

print(f"\ntau_exit = 0.205: {n_within_50[0]}/8 modes within 50% (B3 only expected)")
print(f"tau_exit = 0.250: {n_within_50[1]}/8 modes within 50% (B1+B3 expected)")
print(f"tau_exit = 0.500: {n_within_50[2]}/8 modes within 50% (all expected)")

# The cross-check passes if:
# 1. At large tau (0.50), BdG ~ Dirac (pairing negligible)
# 2. The deviation pattern is monotonic: closer to fold -> larger deviation
# 3. B2 (dominant pairing) shows largest enhancement, B3 (weakest) smallest

pattern_correct = (
    max_deviation_05 < 0.02 and  # <2% at tau=0.5
    np.mean(np.abs(ratios_025 - 1)) > np.mean(np.abs(ratios_05 - 1)) and  # larger at 0.25
    np.mean(np.abs(ratios_0205 - 1)) > np.mean(np.abs(ratios_025 - 1)) and  # largest at 0.205
    ratios_0205[0] > ratios_0205[4] > ratios_0205[5]  # B2 > B1 > B3 enhancement
)

verdict = "INFO: VALIDATES GEOMETRIC INTERPRETATION" if pattern_correct else "INFO: PATTERN ANOMALY"

print(f"\nMax deviation at tau=0.50: {max_deviation_05:.4f} (should be <0.02)")
print(f"Mean |ratio-1| at 0.205: {np.mean(np.abs(ratios_0205 - 1)):.4f}")
print(f"Mean |ratio-1| at 0.250: {np.mean(np.abs(ratios_025 - 1)):.4f}")
print(f"Mean |ratio-1| at 0.500: {np.mean(np.abs(ratios_05 - 1)):.4f}")
print(f"Enhancement ordering (B2>B1>B3): {ratios_0205[0]:.2f} > {ratios_0205[4]:.2f} > {ratios_0205[5]:.2f}: {ratios_0205[0] > ratios_0205[4] > ratios_0205[5]}")

print(f"\n*** VERDICT: {verdict} ***")

# ============================================================
# 11. Classical pair creation bound
# ============================================================

# Best estimate: use accumulated mass variation from tau=0.5 to tau=0.205
Delta_m2_B2_total = abs(cs_B2(0.205)**2 - cs_B2(0.50)**2)
m_B2_avg = (cs_B2(0.205) + cs_B2(0.50)) / 2
delta_n_classical_total = Delta_m2_B2_total / (2 * m_B2_avg * omega_att)

print(f"\n--- Classical pair creation bound (B2, tau: 0.50 -> 0.205) ---")
print(f"  |Delta(m^2_B2)| = {Delta_m2_B2_total:.6f}")
print(f"  <m_B2> = {m_B2_avg:.6f}")
print(f"  delta_n_classical = {delta_n_classical_total:.4f}")
print(f"  n_Bog (quantum) = {n_Bog_quantum:.3f}")
print(f"  Ratio classical/quantum = {delta_n_classical_total / n_Bog_quantum:.4f}")

bound_validates = delta_n_classical_total < n_Bog_quantum
print(f"  Classical < Quantum (bound respected): {bound_validates}")

# ============================================================
# 12. Save results
# ============================================================

# Build per-tau arrays for 8 modes
E_classical_all = np.zeros((3, 8))
E_bdg_all = np.zeros((3, 8))
ratio_all = np.zeros((3, 8))
Delta_m2_all = np.zeros((3, 8))

for j, tau_exit in enumerate(tau_exit_values):
    E_classical_all[j] = np.array(
        [cs_B2(tau_exit)]*4 + [cs_B1(tau_exit)] + [cs_B3(tau_exit)]*3
    )
    E_bdg_all[j] = d_mass[f'tau{j}_E_bdg_mf']
    ratio_all[j] = E_bdg_all[j] / E_classical_all[j]
    Delta_m2_all[j] = E_classical_all[j]**2 - E_init_8**2

# Pair creation estimates
delta_n_classical_arr = np.zeros(3)
for j in range(3):
    tau_exit = tau_exit_values[j]
    Delta_m2 = abs(cs_B2(tau_exit)**2 - cs_B2(tau_init)**2)
    m_mid = cs_B2((tau_init + tau_exit) / 2)
    delta_n_classical_arr[j] = Delta_m2 / (2 * m_mid * omega_att)

# Adiabaticity at fold
dm2_dtau_fold_B2 = 2 * cs_B2(tau_fold) * dcs_B2(tau_fold)
dm2_dt_fold_B2 = dm2_dtau_fold_B2 * abs(v_terminal)
gamma_fold = omega_att**2 / abs(dm2_dt_fold_B2) if abs(dm2_dt_fold_B2) > 1e-15 else float('inf')

np.savez('tier0-computation/s39_geodesic_mass.npz',
    # Grid
    tau_grid=tau_grid,
    tau_exit_values=tau_exit_values,
    tau_init=tau_init,
    branch_labels=branch_labels,
    # Dirac eigenvalues
    E_B1=E_B1,
    E_B2=E_B2,
    E_B3=E_B3,
    # Comparison tables
    E_classical=E_classical_all,
    E_bdg=E_bdg_all,
    ratio_bdg_classical=ratio_all,
    Delta_m2=Delta_m2_all,
    # Pair creation
    delta_n_classical=delta_n_classical_arr,
    n_Bog_quantum=n_Bog_quantum,
    omega_att=omega_att,
    # Adiabaticity
    dm2_dtau_fold_B2=dm2_dtau_fold_B2,
    dm2_dt_fold_B2=dm2_dt_fold_B2,
    gamma_adiabaticity=gamma_fold,
    # Paper 15 gauge boson mass
    m2_gauge_C2=np.array([m2_C2_gauge(tau) for tau in tau_grid]),
    # Verdict
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([
        f"BdG/Dirac at tau=0.50: max dev {max_deviation_05:.4f}. "
        f"At tau=0.205: B2={ratios_0205[0]:.2f}x, B1={ratios_0205[4]:.2f}x, B3={ratios_0205[5]:.2f}x. "
        f"Pattern B2>B1>B3: {ratios_0205[0] > ratios_0205[4] > ratios_0205[5]}. "
        f"Classical pair bound: {delta_n_classical_total:.4f} vs quantum {n_Bog_quantum:.3f}. "
        f"Adiabaticity gamma={gamma_fold:.4f}."
    ]),
    pattern_monotonic=pattern_correct,
    n_within_50_pct=np.array(n_within_50),
)

print("\nSaved: tier0-computation/s39_geodesic_mass.npz")
print("DONE.")
