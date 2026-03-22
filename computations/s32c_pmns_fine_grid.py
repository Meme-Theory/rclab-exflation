"""
Session 32c: PMNS Fine-Grid Extraction (Method B) at tau in [0.15, 0.22]
========================================================================

Runs the Method B (degenerate perturbation theory) PMNS extraction at a
fine tau grid: 0.15, 0.16, 0.17, 0.18, 0.19, 0.20, 0.21, 0.22.

The coarse grid (Session 29b) had tau = {0.10, 0.15, 0.20, 0.25, ...}.
The fine grid fills in the gap around the dump point tau ~ 0.190.

Method: Cubic spline interpolation of the 5 smooth quantities
  {E1(tau), E2(tau), E3(tau), norm_12(tau), norm_23(tau)}
from the 8 available coarse-grid points (tau = 0.10 ... 0.50).

Justification for interpolation:
  - L2_eff = [0.5, 0.5, 0.5, 0.5] EXACTLY at all tau (structural symmetry).
  - v_eff_L3 is uniform across the triplet at all tau.
  - All 5 quantities are smooth, monotonic functions of tau.
  - The interpolation interval [0.15, 0.22] is well inside the data range.
  - Cross-check: spline at tau=0.15 and tau=0.20 must reproduce coarse-grid results.

Input: tier0-computation/s23a_kosmann_singlet.npz
Output: tier0-computation/s32c_pmns_fine_grid.npz
        tier0-computation/s32c_pmns_fine_grid.png

PDG targets:
  sin^2(theta_13): [0.020, 0.024] (best fit 0.0218)
  theta_12: [31.3, 35.9] deg (best fit 33.4)
  theta_23: [40.1, 51.7] deg (best fit 42.2 or 49.2)
  R = Delta m^2_21 / Delta m^2_32: [0.028, 0.034] (best fit 0.030)
  NOTE: The framework computes R' = Delta m^2_32 / Delta m^2_21 = 1/R ~ 32.6
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
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

tau_coarse = d['tau_values']
n_coarse = len(tau_coarse)

print("=" * 75)
print("SESSION 32c: PMNS FINE-GRID EXTRACTION (Method B)")
print("=" * 75)
print(f"Coarse tau grid: {tau_coarse}")

# =====================================================================
# EXTRACT Method B quantities at coarse grid
# =====================================================================
# Only use tau > 0
mask = tau_coarse > 0
tau_data = tau_coarse[mask]
n_data = len(tau_data)

E1_data = np.zeros(n_data)
E2_data = np.zeros(n_data)
E3_data = np.zeros(n_data)
norm_12_data = np.zeros(n_data)
norm_23_data = np.zeros(n_data)

for j, i in enumerate(np.where(mask)[0]):
    evals = d[f'eigenvalues_{i}']
    V = d[f'V_pairing_{i}']

    E1_data[j] = evals[8]   # L1 singlet
    E2_data[j] = evals[9]   # L2 quadruplet (all 4 degenerate)
    E3_data[j] = evals[13]  # L3 triplet (all 3 degenerate)

    # Method B coupling norms
    v_L1_L2 = V[8, 9:13]  # 4-vector
    norm_12_data[j] = np.linalg.norm(v_L1_L2)

    # Effective L2 state (always [0.5, 0.5, 0.5, 0.5] by symmetry)
    L2_eff = v_L1_L2 / norm_12_data[j]
    V_L2_L3 = V[9:13, 13:16]  # 4x3 block
    v_eff_L3 = L2_eff @ V_L2_L3  # 3-vector
    norm_23_data[j] = np.linalg.norm(v_eff_L3)

print(f"\nCoarse-grid Method B quantities:")
print(f"{'tau':>5} | {'E1':>12} | {'E2':>12} | {'E3':>12} | {'norm_12':>12} | {'norm_23':>12}")
print("-" * 70)
for j in range(n_data):
    print(f"{tau_data[j]:5.2f} | {E1_data[j]:12.8f} | {E2_data[j]:12.8f} | "
          f"{E3_data[j]:12.8f} | {norm_12_data[j]:12.8f} | {norm_23_data[j]:12.8f}")

# =====================================================================
# BUILD CUBIC SPLINES
# =====================================================================
cs_E1 = CubicSpline(tau_data, E1_data)
cs_E2 = CubicSpline(tau_data, E2_data)
cs_E3 = CubicSpline(tau_data, E3_data)
cs_n12 = CubicSpline(tau_data, norm_12_data)
cs_n23 = CubicSpline(tau_data, norm_23_data)

# =====================================================================
# HELPER: Extract PMNS angles from 3x3 unitary matrix
# =====================================================================
def extract_pmns(U):
    """Extract mixing angles from 3x3 eigenvector matrix.

    Convention: U[alpha, i] with alpha = flavor (e,mu,tau), i = mass (1,2,3)
    Eigenvalues sorted ascending -> column 0 = lightest mass state.
    """
    # sin^2(theta_13) = |U_e3|^2
    sin2_13 = abs(U[0, 2])**2
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

    # Jarlskog (zero for real matrices)
    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))

    return {
        'sin2_13': sin2_13,
        'theta_13': theta_13,
        'theta_12': theta_12,
        'theta_23': theta_23,
        'J': J,
    }


# =====================================================================
# FINE GRID COMPUTATION
# =====================================================================
tau_fine = np.arange(0.15, 0.225, 0.01)  # [0.15, 0.16, ..., 0.22]
n_fine = len(tau_fine)

print(f"\nFine tau grid: {tau_fine}")
print(f"Number of fine-grid points: {n_fine}")

# Storage
results = []

print("\n" + "=" * 75)
print("FINE-GRID METHOD B RESULTS")
print("=" * 75)
print(f"{'tau':>5} | {'E1':>10} | {'E2':>10} | {'E3':>10} | "
      f"{'V12':>10} | {'V23':>10} | {'sin2_13':>10} | "
      f"{'th12':>8} | {'th23':>8} | {'R':>10}")
print("-" * 110)

for tau in tau_fine:
    # Interpolate the 5 quantities
    E1 = float(cs_E1(tau))
    E2 = float(cs_E2(tau))
    E3 = float(cs_E3(tau))
    n12 = float(cs_n12(tau))
    n23 = float(cs_n23(tau))

    # Build tridiagonal 3x3
    H_3x3 = np.array([
        [E1,  n12, 0.0],
        [n12, E2,  n23],
        [0.0, n23, E3 ]
    ])

    # Diagonalize
    m_evals, U = np.linalg.eigh(H_3x3)

    # PMNS angles
    pmns = extract_pmns(U)

    # R = (m3^2 - m2^2) / (m2^2 - m1^2)  [framework convention]
    denom = m_evals[1]**2 - m_evals[0]**2
    R = (m_evals[2]**2 - m_evals[1]**2) / denom if abs(denom) > 1e-30 else float('inf')

    # R_pdg = 1/R = Delta m^2_21 / Delta m^2_32
    R_pdg = 1.0 / R if abs(R) > 1e-30 else float('inf')

    result = {
        'tau': tau,
        'E1': E1, 'E2': E2, 'E3': E3,
        'V_12': n12, 'V_23': n23,
        'H_3x3': H_3x3,
        'eigenvalues': m_evals,
        'U': U,
        'sin2_13': pmns['sin2_13'],
        'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'],
        'theta_23': pmns['theta_23'],
        'R': R,
        'R_pdg': R_pdg,
        'J': pmns['J'],
    }
    results.append(result)

    print(f"{tau:5.2f} | {E1:10.6f} | {E2:10.6f} | {E3:10.6f} | "
          f"{n12:10.6f} | {n23:10.6f} | {pmns['sin2_13']:10.6f} | "
          f"{pmns['theta_12']:8.2f} | {pmns['theta_23']:8.2f} | {R:10.4f}")


# =====================================================================
# CROSS-CHECK against coarse grid at tau=0.15 and tau=0.20
# =====================================================================
print("\n" + "=" * 75)
print("CROSS-CHECK: Fine grid vs coarse grid at tau = 0.15 and 0.20")
print("=" * 75)

# Reference values from Session 29b output
ref = {
    0.15: {'sin2_13': 0.253715, 'theta_12': 35.06, 'theta_23': 48.76, 'R': 0.4781},
    0.20: {'sin2_13': 0.202569, 'theta_12': 36.55, 'theta_23': 41.97, 'R': 0.3810},
}

# User-provided reference (slightly different rounding)
ref_user = {
    0.15: {'sin2_13': 0.254, 'theta_12': 35.1, 'theta_23': 48.8, 'R': 0.48},
    0.20: {'sin2_13': 0.203, 'theta_12': 36.5, 'theta_23': 42.0, 'R': 0.38},
}

all_checks_pass = True
for tau_check in [0.15, 0.20]:
    # Find the fine-grid result at this tau
    for r in results:
        if abs(r['tau'] - tau_check) < 1e-10:
            fine = r
            break

    s29b = ref[tau_check]
    print(f"\n  tau = {tau_check:.2f}:")
    print(f"    {'Quantity':>15} | {'Fine grid':>12} | {'29b ref':>12} | {'Rel err (%)':>12} | {'Status':>8}")
    print(f"    {'-'*70}")

    for key, label in [('sin2_13', 'sin^2(th13)'),
                       ('theta_12', 'theta_12 (deg)'),
                       ('theta_23', 'theta_23 (deg)'),
                       ('R', 'R')]:
        val_fine = fine[key]
        val_ref = s29b[key]
        rel_err = abs(val_fine - val_ref) / abs(val_ref) * 100
        status = "PASS" if rel_err < 1.0 else "FAIL"
        if status == "FAIL":
            all_checks_pass = False
        print(f"    {label:>15} | {val_fine:12.6f} | {val_ref:12.6f} | {rel_err:12.4f} | {status:>8}")

print(f"\n  Overall cross-check: {'PASS' if all_checks_pass else 'FAIL'}")


# =====================================================================
# PDG WINDOW CROSSING ANALYSIS
# =====================================================================
print("\n" + "=" * 75)
print("PDG WINDOW CROSSING ANALYSIS")
print("=" * 75)

pdg_windows = {
    'sin2_13': (0.020, 0.024, 'sin^2(theta_13)'),
    'theta_12': (31.3, 35.9, 'theta_12 (deg)'),
    'theta_23': (40.1, 51.7, 'theta_23 (deg)'),
    'R_pdg': (0.028, 0.034, 'R_pdg = Dm21/Dm32'),
}

for key, (lo, hi, label) in pdg_windows.items():
    print(f"\n  {label}: PDG window [{lo}, {hi}]")
    values = [r[key] for r in results]
    taus = [r['tau'] for r in results]

    in_window = [(lo <= v <= hi) for v in values]
    any_in = any(in_window)
    crosses_lo = any((values[i] - lo) * (values[i+1] - lo) < 0 for i in range(len(values)-1))
    crosses_hi = any((values[i] - hi) * (values[i+1] - hi) < 0 for i in range(len(values)-1))

    for i, (tau, val, iw) in enumerate(zip(taus, values, in_window)):
        marker = " <-- IN WINDOW" if iw else ""
        print(f"    tau={tau:.2f}: {val:.6f}{marker}")

    if any_in:
        print(f"    --> INSIDE PDG window at some tau")
    elif crosses_lo:
        print(f"    --> CROSSES lower bound {lo}")
    elif crosses_hi:
        print(f"    --> CROSSES upper bound {hi}")
    else:
        if values[0] > hi:
            print(f"    --> ALL ABOVE PDG window (min = {min(values):.6f} > {hi})")
        elif values[0] < lo:
            print(f"    --> ALL BELOW PDG window (max = {max(values):.6f} < {lo})")
        else:
            print(f"    --> Does not cross PDG window boundaries")


# =====================================================================
# DERIVATIVE ANALYSIS: d/dtau of key quantities
# =====================================================================
print("\n" + "=" * 75)
print("DERIVATIVE ANALYSIS (finite differences)")
print("=" * 75)

print(f"{'tau':>5} | {'d(sin2_13)/dtau':>16} | {'d(th12)/dtau':>14} | {'d(th23)/dtau':>14} | {'dR/dtau':>12}")
print("-" * 70)
for i in range(1, len(results)):
    dt = results[i]['tau'] - results[i-1]['tau']
    ds13 = (results[i]['sin2_13'] - results[i-1]['sin2_13']) / dt
    dt12 = (results[i]['theta_12'] - results[i-1]['theta_12']) / dt
    dt23 = (results[i]['theta_23'] - results[i-1]['theta_23']) / dt
    dR = (results[i]['R'] - results[i-1]['R']) / dt
    tau_mid = (results[i]['tau'] + results[i-1]['tau']) / 2
    print(f"{tau_mid:5.3f} | {ds13:16.6f} | {dt12:14.4f} | {dt23:14.4f} | {dR:12.6f}")


# =====================================================================
# SUMMARY TABLE (formatted for user)
# =====================================================================
print("\n" + "=" * 75)
print("SUMMARY TABLE: Fine-Grid PMNS (Method B)")
print("=" * 75)
print(f"{'tau':>6} | {'sin^2(th13)':>12} | {'th12 (deg)':>11} | {'th23 (deg)':>11} | {'R':>10}")
print("-" * 60)
for r in results:
    print(f"{r['tau']:6.2f} | {r['sin2_13']:12.6f} | {r['theta_12']:11.2f} | "
          f"{r['theta_23']:11.2f} | {r['R']:10.4f}")

print(f"\nPDG targets:")
print(f"  sin^2(theta_13): [0.020, 0.024] (best fit 0.0218)")
print(f"  theta_12: [31.3, 35.9] deg (best fit 33.4)")
print(f"  theta_23: [40.1, 51.7] deg (best fit 42.2 or 49.2)")
print(f"  R = Dm21/Dm32: [0.028, 0.034] (best fit 0.030)")


# =====================================================================
# SAVE DATA
# =====================================================================
save_dict = {
    'tau_fine': tau_fine,
    'tau_coarse': tau_coarse,
    'method': 'B_degenerate_PT',
    'interpolation': 'cubic_spline',
}

# Arrays for easy plotting
sin2_13_arr = np.array([r['sin2_13'] for r in results])
theta_12_arr = np.array([r['theta_12'] for r in results])
theta_23_arr = np.array([r['theta_23'] for r in results])
R_arr = np.array([r['R'] for r in results])
R_pdg_arr = np.array([r['R_pdg'] for r in results])

save_dict['sin2_theta13'] = sin2_13_arr
save_dict['theta_12_deg'] = theta_12_arr
save_dict['theta_23_deg'] = theta_23_arr
save_dict['R_framework'] = R_arr
save_dict['R_pdg'] = R_pdg_arr

for i, r in enumerate(results):
    prefix = f"t{i}"
    save_dict[f'{prefix}_tau'] = r['tau']
    save_dict[f'{prefix}_E1'] = r['E1']
    save_dict[f'{prefix}_E2'] = r['E2']
    save_dict[f'{prefix}_E3'] = r['E3']
    save_dict[f'{prefix}_V12'] = r['V_12']
    save_dict[f'{prefix}_V23'] = r['V_23']
    save_dict[f'{prefix}_eigenvalues'] = r['eigenvalues']
    save_dict[f'{prefix}_U'] = r['U']
    save_dict[f'{prefix}_sin2_13'] = r['sin2_13']
    save_dict[f'{prefix}_theta12'] = r['theta_12']
    save_dict[f'{prefix}_theta23'] = r['theta_23']
    save_dict[f'{prefix}_R'] = r['R']

np.savez(f"{base}/s32c_pmns_fine_grid.npz", **save_dict)
print(f"\nSaved: {base}/s32c_pmns_fine_grid.npz")


# =====================================================================
# PLOT: 4-panel figure
# =====================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 32c: Fine-Grid PMNS Extraction (Method B)\n'
             r'$\tau \in [0.15, 0.22]$, cubic spline interpolation',
             fontsize=14, fontweight='bold')

# Also plot coarse-grid points for comparison
# Re-run Method B at coarse grid to get reference
coarse_results = []
for j, i in enumerate(np.where(mask)[0]):
    tau = tau_data[j]
    evals = d[f'eigenvalues_{i}']
    V_mat = d[f'V_pairing_{i}']
    E1 = evals[8]
    E2 = evals[9]
    E3 = evals[13]
    v_L1_L2 = V_mat[8, 9:13]
    n12 = np.linalg.norm(v_L1_L2)
    L2_eff = v_L1_L2 / n12
    V_L2_L3 = V_mat[9:13, 13:16]
    v_eff_L3 = L2_eff @ V_L2_L3
    n23 = np.linalg.norm(v_eff_L3)
    H = np.array([[E1, n12, 0.0], [n12, E2, n23], [0.0, n23, E3]])
    me, Ue = np.linalg.eigh(H)
    p = extract_pmns(Ue)
    dm = me[1]**2 - me[0]**2
    Rc = (me[2]**2 - me[1]**2) / dm if abs(dm) > 1e-30 else float('inf')
    coarse_results.append({
        'tau': tau, 'sin2_13': p['sin2_13'],
        'theta_12': p['theta_12'], 'theta_23': p['theta_23'], 'R': Rc
    })

tau_coarse_plot = np.array([cr['tau'] for cr in coarse_results])
sin2_13_coarse = np.array([cr['sin2_13'] for cr in coarse_results])
theta_12_coarse = np.array([cr['theta_12'] for cr in coarse_results])
theta_23_coarse = np.array([cr['theta_23'] for cr in coarse_results])
R_coarse = np.array([cr['R'] for cr in coarse_results])

# Panel 1: sin^2(theta_13)
ax = axes[0, 0]
ax.plot(tau_fine, sin2_13_arr, 'b-o', markersize=6, label='Fine grid (spline)')
ax.plot(tau_coarse_plot, sin2_13_coarse, 'rs', markersize=8, label='Coarse grid (exact)')
ax.axhspan(0.020, 0.024, alpha=0.2, color='green', label='PDG window')
ax.axhline(0.0218, color='green', linestyle='--', alpha=0.5, label='PDG best fit')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\sin^2(\theta_{13})$')
ax.set_title(r'$\sin^2(\theta_{13})$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.14, 0.23)

# Panel 2: theta_12
ax = axes[0, 1]
ax.plot(tau_fine, theta_12_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, theta_12_coarse, 'rs', markersize=8, label='Coarse grid')
ax.axhspan(31.3, 35.9, alpha=0.2, color='green', label='PDG window')
ax.axhline(33.4, color='green', linestyle='--', alpha=0.5, label='PDG best fit')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\theta_{12}$ (deg)')
ax.set_title(r'$\theta_{12}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.14, 0.23)

# Panel 3: theta_23
ax = axes[1, 0]
ax.plot(tau_fine, theta_23_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, theta_23_coarse, 'rs', markersize=8, label='Coarse grid')
ax.axhspan(40.1, 51.7, alpha=0.2, color='green', label='PDG window')
ax.axhline(42.2, color='green', linestyle='--', alpha=0.3, label='PDG 42.2')
ax.axhline(49.2, color='green', linestyle=':', alpha=0.3, label='PDG 49.2')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\theta_{23}$ (deg)')
ax.set_title(r'$\theta_{23}$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.14, 0.23)

# Panel 4: R (framework convention: Dm32/Dm21)
ax = axes[1, 1]
ax.plot(tau_fine, R_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, R_coarse, 'rs', markersize=8, label='Coarse grid')
# PDG R_framework = 1/R_pdg = 1/0.030 ~ 33.3; but our R ~ 0.3-0.5 (inverted hierarchy?)
# The framework R = Dm32/Dm21 ~ 0.3-0.5, while PDG R_framework ~ 33
# So mark PDG target in the R_pdg = Dm21/Dm32 convention
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R = \Delta m^2_{32}/\Delta m^2_{21}$')
ax.set_title(r'$R$ (mass ratio)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0.14, 0.23)

# Add text annotation about PDG R
ax.text(0.05, 0.95, f'PDG: R ~ 32.6\nModel: R ~ {R_arr.mean():.2f}\n(inverted)',
        transform=ax.transAxes, fontsize=8, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig(f"{base}/s32c_pmns_fine_grid.png", dpi=150, bbox_inches='tight')
print(f"Saved: {base}/s32c_pmns_fine_grid.png")

print("\n" + "=" * 75)
print("COMPUTATION COMPLETE")
print("=" * 75)
