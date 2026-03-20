"""
Session 24a Step 3: Neutrino R Diagnostic
==========================================

H_eff = diag(E_1,...,E_16) + V_nm(tau)
R = (m3^2 - m2^2) / (m2^2 - m1^2)

where m_i are the 3 smallest |eigenvalues| of H_eff.

Mixing angle: tan(2*theta_12) = 2*|H_12| / |H_11 - H_22|

Gate: R in [17, 66] = PASS (experimental value ~ 32.6)

Data source: s23a_kosmann_singlet.npz
"""

import numpy as np

# =====================================================================
# LOAD DATA
# =====================================================================
base = "C:/sandbox/Ainulindale Exflation/tier0-computation"
d = np.load(f"{base}/s23a_kosmann_singlet.npz")

tau_values = d['tau_values']  # shape (9,)
n_tau = len(tau_values)

print("=" * 60)
print("STEP 3: Neutrino R Diagnostic")
print("=" * 60)
print(f"tau values: {tau_values}")

# Target tau values for this step
target_taus = [0.15, 0.20, 0.25, 0.30, 0.35]

# =====================================================================
# COMPUTE H_eff AND EXTRACT R
# =====================================================================

results = []

for tau_target in target_taus:
    # Find closest tau index
    t_idx = np.argmin(np.abs(tau_values - tau_target))
    tau_actual = tau_values[t_idx]

    evals = d[f'eigenvalues_{t_idx}']  # shape (16,)

    # Build V_nm: sum of Kosmann matrix elements over 8 generators
    # V_nm = V_pairing matrix (already computed in s23a)
    V_nm = d[f'V_pairing_{t_idx}']  # shape (16, 16)

    # H_eff = diag(E) + V_nm
    H_eff = np.diag(evals) + V_nm

    # Diagonalize H_eff
    H_evals = np.linalg.eigvalsh(H_eff)

    # Extract 3 smallest |eigenvalues|
    abs_evals = np.sort(np.abs(H_evals))
    # Remove near-zero values if any
    m1, m2, m3 = abs_evals[0], abs_evals[1], abs_evals[2]

    # R = (m3^2 - m2^2) / (m2^2 - m1^2)
    denom = m2**2 - m1**2
    if abs(denom) < 1e-30:
        R = float('inf')
    else:
        R = (m3**2 - m2**2) / denom

    # Mixing angle from 2x2 submatrix of H_eff
    # Use the two smallest-eigenvalue states
    tan_2theta = 0.0
    if abs(H_eff[0,0] - H_eff[1,1]) > 1e-30:
        tan_2theta = 2.0 * abs(H_eff[0,1]) / abs(H_eff[0,0] - H_eff[1,1])
    theta_12 = 0.5 * np.arctan(tan_2theta)

    gate = "PASS" if 17 <= R <= 66 else "FAIL"

    print(f"\n  tau={tau_actual:.2f} (target {tau_target:.2f}):")
    print(f"    3 smallest |evals(H_eff)|: m1={m1:.8f}, m2={m2:.8f}, m3={m3:.8f}")
    print(f"    m1^2={m1**2:.10f}, m2^2={m2**2:.10f}, m3^2={m3**2:.10f}")
    print(f"    R = (m3^2-m2^2)/(m2^2-m1^2) = {R:.4f}")
    print(f"    Gate [17, 66]: {gate}")
    print(f"    tan(2*theta_12) = {tan_2theta:.6f}, theta_12 = {np.degrees(theta_12):.2f} deg")
    print(f"    All H_eff eigenvalues: {np.sort(H_evals)}")

    results.append({
        'tau': tau_actual,
        'm1': m1, 'm2': m2, 'm3': m3,
        'R': R, 'gate': gate,
        'tan_2theta': tan_2theta, 'theta_12_deg': np.degrees(theta_12),
        'H_eff_evals': np.sort(H_evals)
    })

# =====================================================================
# ALTERNATIVE: Use K_a matrices directly for V_nm if V_pairing gives
# unexpected results. Cross-check with raw Kosmann matrices.
# =====================================================================
print("\n--- Cross-check: Build V_nm from K_a matrices at tau=0.30 ---")
t_idx_030 = np.argmin(np.abs(tau_values - 0.30))
evals_030 = d[f'eigenvalues_{t_idx_030}']
V_from_Ka = np.zeros((16, 16))
for a in range(8):
    K_a = d[f'K_a_matrix_{t_idx_030}_{a}']
    V_from_Ka += np.real(K_a)  # Real part of sum

V_pairing_030 = d[f'V_pairing_{t_idx_030}']
diff = np.max(np.abs(V_from_Ka - V_pairing_030))
print(f"  max|V_from_Ka - V_pairing| = {diff:.6e}")
if diff > 0.1:
    print("  WARNING: V_pairing and K_a-derived V differ significantly!")
    print("  Recomputing H_eff with K_a-derived V...")
    H_eff_alt = np.diag(evals_030) + V_from_Ka
    H_evals_alt = np.linalg.eigvalsh(H_eff_alt)
    abs_alt = np.sort(np.abs(H_evals_alt))
    m1a, m2a, m3a = abs_alt[0], abs_alt[1], abs_alt[2]
    Ra = (m3a**2 - m2a**2) / (m2a**2 - m1a**2) if abs(m2a**2 - m1a**2) > 1e-30 else float('inf')
    print(f"  Alt R at tau=0.30: {Ra:.4f}")

# =====================================================================
# SAVE RESULTS
# =====================================================================
with open(f"{base}/s24a_neutrino.txt", 'w') as f:
    f.write("Session 24a Step 3: Neutrino R Diagnostic\n")
    f.write("=" * 50 + "\n\n")
    f.write(f"Gate criterion: R in [17, 66] (experimental ~ 32.6)\n\n")
    for r in results:
        f.write(f"tau = {r['tau']:.2f}:\n")
        f.write(f"  m1 = {r['m1']:.8f}, m2 = {r['m2']:.8f}, m3 = {r['m3']:.8f}\n")
        f.write(f"  R = {r['R']:.4f}  [{r['gate']}]\n")
        f.write(f"  theta_12 = {r['theta_12_deg']:.2f} deg\n")
        f.write(f"  H_eff eigenvalues: {r['H_eff_evals']}\n\n")

print(f"\nSaved: {base}/s24a_neutrino.txt")

print("\n" + "=" * 60)
print("STEP 3 COMPLETE")
print("=" * 60)
