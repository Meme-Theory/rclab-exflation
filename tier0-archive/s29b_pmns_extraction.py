"""
Session 29Ba: PMNS Mixing Angle Extraction from Tridiagonal Kosmann Kernel
==========================================================================

Extracts the full 3x3 PMNS mixing matrix from the (0,0) singlet sector
of the D_K Dirac operator on Jensen-deformed SU(3).

The singlet sector has 16 eigenvalues grouping into 3 distinct positive-energy
levels (plus their particle-hole partners):
  L1: multiplicity 1 (gap-edge singlet)
  L2: multiplicity 4 (quadruplet)
  L3: multiplicity 3 (triplet)

Selection rules (Session 23a):
  V(L1, L2) ~ 0.07-0.13 (nearest-neighbor)
  V(L1, L3) = 0 EXACTLY (selection rule)
  V(L2, L3) ~ 0.01-0.03 (nearest-neighbor)

Three analysis methods:
  Method A: Full 16x16 H_eff diagonalization, extract 3 smallest positive eigenvalues
  Method B: Degenerate perturbation theory -> 3x3 reduction
  Method C: Single-mode 3x3 (individual coupling, not Frobenius norm)

Gate B-29b: sin^2(theta_13) < 0.005 or > 0.10 -> tridiagonal PMNS fails
Gate P-29b: sin^2(theta_13) in [0.015, 0.030] -> PASS

Input: s23a_kosmann_singlet.npz
Output: s29b_pmns_extraction.npz
"""

import numpy as np
import sys

base = "C:/sandbox/Ainulindale Exflation/tier0-computation"

# =====================================================================
# LOAD DATA
# =====================================================================
try:
    d = np.load(f"{base}/s23a_kosmann_singlet.npz", allow_pickle=True)
except FileNotFoundError:
    print("ERROR: s23a_kosmann_singlet.npz not found")
    sys.exit(1)

tau_values = d['tau_values']
n_tau = len(tau_values)

# PDG reference values
PDG = {
    'sin2_theta13': 0.0220,
    'sin2_theta13_err': 0.0007,
    'theta12_deg': 33.44,
    'theta12_deg_err': 0.77,
    'theta23_deg': 49.1,
    'theta23_deg_err': 1.0,  # approximate
    'sin2_2theta13': 0.0851,
    'R_target': 32.6,  # Delta m^2_32 / Delta m^2_21
}

print("=" * 70)
print("SESSION 29Ba: PMNS MIXING ANGLE EXTRACTION")
print("=" * 70)
print(f"tau values: {tau_values}")
print(f"\nPDG reference:")
print(f"  sin^2(theta_13) = {PDG['sin2_theta13']} +/- {PDG['sin2_theta13_err']}")
print(f"  theta_12 = {PDG['theta12_deg']} +/- {PDG['theta12_deg_err']} deg")
print(f"  theta_23 = {PDG['theta23_deg']} +/- {PDG['theta23_deg_err']} deg")
print(f"  R = Delta m^2_32/Delta m^2_21 = {PDG['R_target']}")

# =====================================================================
# HELPER: Extract PMNS angles from 3x3 unitary matrix
# =====================================================================
def extract_pmns(U):
    """Extract mixing angles from 3x3 eigenvector matrix.

    Convention: U[alpha, i] with alpha = flavor (e,mu,tau), i = mass (1,2,3)
    Eigenvalues sorted ascending -> column 0 = lightest mass state.

    Returns dict with sin2_13, theta_12, theta_23, theta_13 (all in degrees),
    and Jarlskog invariant.
    """
    # sin^2(theta_13) = |U_e3|^2
    sin2_13 = abs(U[0, 2])**2

    # theta_13 in degrees
    theta_13 = np.degrees(np.arcsin(np.sqrt(sin2_13)))

    # tan^2(theta_12) = |U_e2|^2 / |U_e1|^2
    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1])**2 / abs(U[0, 0])**2
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))
    else:
        theta_12 = 90.0

    # tan^2(theta_23) = |U_mu3|^2 / |U_tau3|^2
    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2])**2 / abs(U[2, 2])**2
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))
    else:
        theta_23 = 90.0

    # Jarlskog invariant (for real matrices, J = 0; check anyway)
    J = np.imag(U[0,0] * U[1,1] * np.conj(U[0,1]) * np.conj(U[1,0]))

    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'J': J,
    }


# =====================================================================
# METHOD A: Full 16x16 H_eff diagonalization
# =====================================================================
print("\n" + "=" * 70)
print("METHOD A: Full 16x16 H_eff diagonalization")
print("=" * 70)

results_A = []
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    evals = d[f'eigenvalues_{t_idx}']
    V = d[f'V_pairing_{t_idx}']

    H_eff = np.diag(evals) + V
    H_evals, H_evecs = np.linalg.eigh(H_eff)

    # Sort by ascending eigenvalue, take 3 smallest positive
    pos_mask = H_evals > 0
    pos_evals = H_evals[pos_mask]
    pos_evecs = H_evecs[:, pos_mask]

    if len(pos_evals) < 3:
        print(f"  tau={tau:.2f}: < 3 positive eigenvalues, skip")
        results_A.append(None)
        continue

    # Sort positive eigenvalues ascending
    sort_idx = np.argsort(pos_evals)
    m = pos_evals[sort_idx[:3]]  # 3 lightest masses
    # The corresponding eigenvectors
    U_3 = pos_evecs[:, sort_idx[:3]]  # 16x3

    # R = (m3^2 - m2^2) / (m2^2 - m1^2)
    denom = m[1]**2 - m[0]**2
    R = (m[2]**2 - m[1]**2) / denom if abs(denom) > 1e-30 else float('inf')

    # For 16x16, we can't directly extract 3x3 PMNS.
    # But we CAN check how the 3 lightest eigenstates overlap with
    # the 3 original level subspaces.
    # L1 = index 8, L2 = indices 9-12, L3 = indices 13-15
    if tau > 0:
        overlap_L1 = np.abs(U_3[8, :])**2  # overlap of each mass state with L1
        overlap_L2 = np.sum(np.abs(U_3[9:13, :])**2, axis=0)  # with L2 subspace
        overlap_L3 = np.sum(np.abs(U_3[13:16, :])**2, axis=0)  # with L3 subspace
        overlap_neg = np.sum(np.abs(U_3[:8, :])**2, axis=0)  # with negative sector
    else:
        overlap_L1 = np.zeros(3)
        overlap_L2 = np.zeros(3)
        overlap_L3 = np.zeros(3)
        overlap_neg = np.zeros(3)

    print(f"\n  tau={tau:.2f}:")
    print(f"    m1={m[0]:.8f}, m2={m[1]:.8f}, m3={m[2]:.8f}")
    print(f"    R = {R:.4f}  (target: 32.6)")
    if tau > 0:
        print(f"    Overlap with L1: {overlap_L1}")
        print(f"    Overlap with L2: {overlap_L2}")
        print(f"    Overlap with L3: {overlap_L3}")
        print(f"    Overlap with neg: {overlap_neg}")
        print(f"    Sum per state: {overlap_L1 + overlap_L2 + overlap_L3 + overlap_neg}")

    results_A.append({
        'tau': tau, 'm': m, 'R': R,
        'H_evals': H_evals,
    })


# =====================================================================
# METHOD B: Degenerate Perturbation Theory -> 3x3
# =====================================================================
print("\n" + "=" * 70)
print("METHOD B: Degenerate Perturbation Theory (3x3)")
print("=" * 70)

results_B = []
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    if tau == 0:
        results_B.append(None)
        continue

    evals = d[f'eigenvalues_{t_idx}']
    V = d[f'V_pairing_{t_idx}']

    # Level energies (positive sector)
    E1 = evals[8]   # L1 (singlet)
    E2 = evals[9]   # L2 (quadruplet, all degenerate)
    E3 = evals[13]  # L3 (triplet, all degenerate)

    # Coupling L1 -> L2
    v_L1_L2 = V[8, 9:13]  # 4-vector
    norm_12 = np.linalg.norm(v_L1_L2)

    # Effective L2 state
    if norm_12 > 1e-15:
        L2_eff = v_L1_L2 / norm_12
    else:
        L2_eff = np.array([0.5, 0.5, 0.5, 0.5])

    # Coupling L2_eff -> L3
    V_L2_L3 = V[9:13, 13:16]  # 4x3 block
    v_eff_L3 = L2_eff @ V_L2_L3  # 3-vector
    norm_23 = np.linalg.norm(v_eff_L3)

    # Build 3x3 H_eff (tridiagonal!)
    H_3x3 = np.array([
        [E1,      norm_12, 0.0    ],
        [norm_12, E2,      norm_23],
        [0.0,     norm_23, E3     ]
    ])

    # Diagonalize
    m_evals, U = np.linalg.eigh(H_3x3)

    # Extract PMNS
    pmns = extract_pmns(U)

    # R
    denom = m_evals[1]**2 - m_evals[0]**2
    R = (m_evals[2]**2 - m_evals[1]**2) / denom if abs(denom) > 1e-30 else float('inf')

    # Gate check
    if 0.015 <= pmns['sin2_13'] <= 0.030:
        gate = "P-29b PASS"
    elif pmns['sin2_13'] < 0.005 or pmns['sin2_13'] > 0.10:
        gate = "B-29b CONSTRAINT"
    else:
        gate = "INTERMEDIATE"

    print(f"\n  tau={tau:.2f}:")
    print(f"    H_3x3 diagonal: [{E1:.6f}, {E2:.6f}, {E3:.6f}]")
    print(f"    V_12 = {norm_12:.6f}, V_23 = {norm_23:.6f}, V_13 = 0 (exact)")
    print(f"    Eigenvalues: [{m_evals[0]:.8f}, {m_evals[1]:.8f}, {m_evals[2]:.8f}]")
    print(f"    sin^2(theta_13) = {pmns['sin2_13']:.6f}  (PDG: 0.0220)")
    print(f"    theta_13 = {pmns['theta_13']:.2f} deg  (PDG: 8.54)")
    print(f"    theta_12 = {pmns['theta_12']:.2f} deg  (PDG: 33.4)")
    print(f"    theta_23 = {pmns['theta_23']:.2f} deg  (PDG: 49.1)")
    print(f"    R = {R:.4f}  (target: 32.6)")
    print(f"    Gate: {gate}")

    results_B.append({
        'tau': tau,
        'E1': E1, 'E2': E2, 'E3': E3,
        'V_12': norm_12, 'V_23': norm_23,
        'H_3x3': H_3x3,
        'eigenvalues': m_evals,
        'U': U,
        'sin2_13': pmns['sin2_13'],
        'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'],
        'theta_23': pmns['theta_23'],
        'R': R,
        'gate': gate,
    })


# =====================================================================
# METHOD C: Single-mode 3x3 (individual coupling, no Frobenius sum)
# =====================================================================
print("\n" + "=" * 70)
print("METHOD C: Single-mode 3x3 (V_12 = individual, V_23 = average)")
print("=" * 70)

results_C = []
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    if tau == 0:
        results_C.append(None)
        continue

    evals = d[f'eigenvalues_{t_idx}']
    V = d[f'V_pairing_{t_idx}']

    E1 = evals[8]
    E2 = evals[9]
    E3 = evals[13]

    # In this method, use the individual coupling (all L2 states couple equally)
    v12_individual = abs(V[8, 9])  # same for all 4

    # For L2->L3, use the average coupling
    V_L2_L3 = V[9:13, 13:16]
    v23_avg = np.mean(np.abs(V_L2_L3))

    H_3x3 = np.array([
        [E1,              v12_individual, 0.0    ],
        [v12_individual, E2,             v23_avg],
        [0.0,            v23_avg,        E3     ]
    ])

    m_evals, U = np.linalg.eigh(H_3x3)
    pmns = extract_pmns(U)

    denom = m_evals[1]**2 - m_evals[0]**2
    R = (m_evals[2]**2 - m_evals[1]**2) / denom if abs(denom) > 1e-30 else float('inf')

    if 0.015 <= pmns['sin2_13'] <= 0.030:
        gate = "P-29b PASS"
    elif pmns['sin2_13'] < 0.005 or pmns['sin2_13'] > 0.10:
        gate = "B-29b CONSTRAINT"
    else:
        gate = "INTERMEDIATE"

    print(f"\n  tau={tau:.2f}:")
    print(f"    V_12 = {v12_individual:.6f}, V_23 = {v23_avg:.6f}")
    print(f"    sin^2(theta_13) = {pmns['sin2_13']:.6f}  (PDG: 0.0220)")
    print(f"    theta_13 = {pmns['theta_13']:.2f} deg  (PDG: 8.54)")
    print(f"    theta_12 = {pmns['theta_12']:.2f} deg  (PDG: 33.4)")
    print(f"    theta_23 = {pmns['theta_23']:.2f} deg  (PDG: 49.1)")
    print(f"    R = {R:.4f}  (target: 32.6)")
    print(f"    Gate: {gate}")

    results_C.append({
        'tau': tau,
        'V_12': v12_individual, 'V_23': v23_avg,
        'sin2_13': pmns['sin2_13'],
        'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'],
        'theta_23': pmns['theta_23'],
        'R': R,
        'gate': gate,
    })


# =====================================================================
# SUMMARY TABLE
# =====================================================================
print("\n" + "=" * 70)
print("SUMMARY: sin^2(theta_13) across methods and tau values")
print("=" * 70)
print(f"{'tau':>5} | {'Method B':>10} | {'Method C':>10} | {'PDG':>10} | {'Gate B':>15} | {'Gate C':>15}")
print("-" * 70)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    if results_B[t_idx] is None:
        print(f"{tau:5.2f} | {'N/A':>10} | {'N/A':>10} | {PDG['sin2_theta13']:10.4f} | {'N/A':>15} | {'N/A':>15}")
        continue
    s13_B = results_B[t_idx]['sin2_13']
    s13_C = results_C[t_idx]['sin2_13']
    gB = results_B[t_idx]['gate']
    gC = results_C[t_idx]['gate']
    print(f"{tau:5.2f} | {s13_B:10.6f} | {s13_C:10.6f} | {PDG['sin2_theta13']:10.4f} | {gB:>15} | {gC:>15}")

print("\n" + "=" * 70)
print("SUMMARY: theta_12 (deg) across methods")
print("=" * 70)
print(f"{'tau':>5} | {'Method B':>10} | {'Method C':>10} | {'PDG':>10}")
print("-" * 50)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    if results_B[t_idx] is None:
        print(f"{tau:5.2f} | {'N/A':>10} | {'N/A':>10} | {PDG['theta12_deg']:10.2f}")
        continue
    t12_B = results_B[t_idx]['theta_12']
    t12_C = results_C[t_idx]['theta_12']
    print(f"{tau:5.2f} | {t12_B:10.2f} | {t12_C:10.2f} | {PDG['theta12_deg']:10.2f}")

print("\n" + "=" * 70)
print("SUMMARY: R = Dm32/Dm21 across methods")
print("=" * 70)
print(f"{'tau':>5} | {'Method B':>10} | {'Method C':>10} | {'target':>10}")
print("-" * 50)
for t_idx in range(n_tau):
    tau = tau_values[t_idx]
    if results_B[t_idx] is None:
        print(f"{tau:5.2f} | {'N/A':>10} | {'N/A':>10} | {PDG['R_target']:10.1f}")
        continue
    R_B = results_B[t_idx]['R']
    R_C = results_C[t_idx]['R']
    print(f"{tau:5.2f} | {R_B:10.4f} | {R_C:10.4f} | {PDG['R_target']:10.1f}")


# =====================================================================
# TRIDIAGONAL ANALYTIC CHECK
# =====================================================================
print("\n" + "=" * 70)
print("ANALYTIC CHECK: Tridiagonal Eigenvalue Perturbation Theory")
print("=" * 70)
print("For a tridiagonal matrix with diagonal (E1, E2, E3) and off-diagonal")
print("(V12, 0, V23), the PMNS angles are determined by the ratio V/DeltaE.")
print("sin^2(theta_13) ~ (V12*V23 / (DeltaE12*DeltaE23))^2 to leading order.")
print()

for t_idx in range(1, n_tau):
    rb = results_B[t_idx]
    if rb is None:
        continue
    tau = rb['tau']
    dE12 = rb['E2'] - rb['E1']
    dE23 = rb['E3'] - rb['E2']
    v12 = rb['V_12']
    v23 = rb['V_23']
    # sin(theta_13) ~ V12*V23 / ((E2-E1)*(E3-E2)) in 2nd-order perturbation theory
    sin_13_PT = v12 * v23 / (dE12 * dE23)
    sin2_13_PT = sin_13_PT**2
    print(f"  tau={tau:.2f}: dE12={dE12:.6f}, dE23={dE23:.6f}, "
          f"V12/dE12={v12/dE12:.4f}, V23/dE23={v23/dE23:.4f}, "
          f"sin^2(13)_PT={sin2_13_PT:.6f} vs exact={rb['sin2_13']:.6f}")


# =====================================================================
# GATE VERDICT
# =====================================================================
print("\n" + "=" * 70)
print("GATE VERDICT")
print("=" * 70)

# Use Method B (degenerate PT, the physically correct reduction)
# Check at the target tau values
target_taus = [0.15, 0.25, 0.35]
all_constraint = True
any_pass = False

for t_idx in range(n_tau):
    rb = results_B[t_idx]
    if rb is None:
        continue
    if 0.015 <= rb['sin2_13'] <= 0.030:
        any_pass = True
        all_constraint = False
    elif 0.005 <= rb['sin2_13'] <= 0.10:
        all_constraint = False

if any_pass:
    verdict = "P-29b: PASS -- sin^2(theta_13) in [0.015, 0.030] at some tau"
elif all_constraint:
    verdict = "B-29b: CONSTRAINT -- sin^2(theta_13) outside [0.005, 0.10] at ALL tau"
else:
    verdict = "INTERMEDIATE -- sin^2(theta_13) in (0.005, 0.10) but outside [0.015, 0.030]"

print(f"  Method B verdict: {verdict}")

# Same for Method C
all_constraint_C = True
any_pass_C = False
for t_idx in range(n_tau):
    rc = results_C[t_idx]
    if rc is None:
        continue
    if 0.015 <= rc['sin2_13'] <= 0.030:
        any_pass_C = True
        all_constraint_C = False
    elif 0.005 <= rc['sin2_13'] <= 0.10:
        all_constraint_C = False

if any_pass_C:
    verdict_C = "P-29b: PASS"
elif all_constraint_C:
    verdict_C = "B-29b: CONSTRAINT"
else:
    verdict_C = "INTERMEDIATE"
print(f"  Method C verdict: {verdict_C}")


# =====================================================================
# SAVE RESULTS
# =====================================================================
save_dict = {
    'tau_values': tau_values,
    'PDG_sin2_theta13': PDG['sin2_theta13'],
    'PDG_theta12_deg': PDG['theta12_deg'],
    'PDG_theta23_deg': PDG['theta23_deg'],
    'PDG_R': PDG['R_target'],
}

# Save Method B results
for t_idx in range(n_tau):
    rb = results_B[t_idx]
    if rb is None:
        continue
    prefix = f"B_t{t_idx}"
    save_dict[f'{prefix}_tau'] = rb['tau']
    save_dict[f'{prefix}_E1'] = rb['E1']
    save_dict[f'{prefix}_E2'] = rb['E2']
    save_dict[f'{prefix}_E3'] = rb['E3']
    save_dict[f'{prefix}_V12'] = rb['V_12']
    save_dict[f'{prefix}_V23'] = rb['V_23']
    save_dict[f'{prefix}_eigenvalues'] = rb['eigenvalues']
    save_dict[f'{prefix}_U'] = rb['U']
    save_dict[f'{prefix}_sin2_13'] = rb['sin2_13']
    save_dict[f'{prefix}_theta13'] = rb['theta_13']
    save_dict[f'{prefix}_theta12'] = rb['theta_12']
    save_dict[f'{prefix}_theta23'] = rb['theta_23']
    save_dict[f'{prefix}_R'] = rb['R']

# Save Method C results
for t_idx in range(n_tau):
    rc = results_C[t_idx]
    if rc is None:
        continue
    prefix = f"C_t{t_idx}"
    save_dict[f'{prefix}_sin2_13'] = rc['sin2_13']
    save_dict[f'{prefix}_theta12'] = rc['theta_12']
    save_dict[f'{prefix}_theta23'] = rc['theta_23']
    save_dict[f'{prefix}_R'] = rc['R']

np.savez(f"{base}/s29b_pmns_extraction.npz", **save_dict)
print(f"\nSaved: {base}/s29b_pmns_extraction.npz")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
