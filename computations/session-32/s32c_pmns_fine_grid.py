"""
Session 32c: PMNS Fine-Grid Extraction (Method B) at tau in [0.15, 0.22]
re-run wave (S81) — canonical-imports + local tags + SHA-256 pins.

PDG window literals remain inline (tagged # (local)) with PDG 2024 citation —
they are allow-listed names in canonical_constants.py's registry but have no
numeric definition there; per orchestrator instruction, do NOT modify
canonical_constants.py for this re-run.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')                # (local) CPU thread cap
os.environ.setdefault('MKL_NUM_THREADS', '8')                # (local) CPU thread cap

import hashlib
import sys
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403 (canonical discipline)

# =====================================================================
# SHA-256 INPUT PINS (log first, as required by S81+ discipline)
# =====================================================================
BASE = "C:/sandbox/Ainulindale Exflation/computations"                                                   # (local)
ARCHIVE = "C:/sandbox/Ainulindale Exflation/computations/_shared"                                                    # (local)
INPUT_NPZ = f"{ARCHIVE}/s23a_kosmann_singlet.npz"                                                             # (local)
SOURCE_PY = f"{ARCHIVE}/s32c_pmns_fine_grid.py"                                                               # (local) original source for SHA


def _sha256(path: str) -> str:
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


INPUT_SHA = _sha256(INPUT_NPZ)                                                                                # (local)
SOURCE_SHA = _sha256(SOURCE_PY)                                                                               # (local)

print("=" * 75)
print("T3 INPUT PINS")
print("=" * 75)
print(f"  source_py          : {SOURCE_PY}")
print(f"  source_py SHA-256  : {SOURCE_SHA}")
print(f"  input_npz          : {INPUT_NPZ}")
print(f"  input_npz SHA-256  : {INPUT_SHA}")

# =====================================================================
# LOAD DATA
# =====================================================================
try:
    d = np.load(INPUT_NPZ, allow_pickle=True)
except FileNotFoundError:
    print("ERROR: s23a_kosmann_singlet.npz not found")
    sys.exit(1)

tau_coarse = d['tau_values']
n_coarse = len(tau_coarse)                                                                                    # (local)

print("=" * 75)
print("SESSION 32c: PMNS FINE-GRID EXTRACTION (Method B) — re-run")
print("=" * 75)
print(f"Coarse tau grid: {tau_coarse}")

# =====================================================================
# EXTRACT Method B quantities at coarse grid
# =====================================================================
mask = tau_coarse > 0                                                                                         # (local) positive-tau mask
tau_data = tau_coarse[mask]                                                                                   # (local)
n_data = len(tau_data)                                                                                        # (local)

E1_data = np.zeros(n_data)                                                                                    # (local) L1 singlet energies
E2_data = np.zeros(n_data)                                                                                    # (local) L2 quadruplet energies
E3_data = np.zeros(n_data)                                                                                    # (local) L3 triplet energies
norm_12_data = np.zeros(n_data)                                                                               # (local) Method B couplings
norm_23_data = np.zeros(n_data)                                                                               # (local) Method B couplings

for j, i in enumerate(np.where(mask)[0]):
    evals = d[f'eigenvalues_{i}']
    V = d[f'V_pairing_{i}']

    E1_data[j] = evals[8]                                                                                     # (local) L1 singlet index
    E2_data[j] = evals[9]                                                                                     # (local) L2 quadruplet first index
    E3_data[j] = evals[13]                                                                                    # (local) L3 triplet first index

    v_L1_L2 = V[8, 9:13]                                                                                      # (local) 4-vector coupling
    norm_12_data[j] = np.linalg.norm(v_L1_L2)

    L2_eff = v_L1_L2 / norm_12_data[j]                                                                        # (local) effective L2 state
    V_L2_L3 = V[9:13, 13:16]                                                                                  # (local) 4x3 off-diagonal
    v_eff_L3 = L2_eff @ V_L2_L3                                                                               # (local) effective 3-vector
    norm_23_data[j] = np.linalg.norm(v_eff_L3)

print("\nCoarse-grid Method B quantities:")
print(f"{'tau':>5} | {'E1':>12} | {'E2':>12} | {'E3':>12} | {'norm_12':>12} | {'norm_23':>12}")
print("-" * 70)
for j in range(n_data):
    print(f"{tau_data[j]:5.2f} | {E1_data[j]:12.8f} | {E2_data[j]:12.8f} | "
          f"{E3_data[j]:12.8f} | {norm_12_data[j]:12.8f} | {norm_23_data[j]:12.8f}")

# =====================================================================
# BUILD CUBIC SPLINES
# =====================================================================
cs_E1 = CubicSpline(tau_data, E1_data)                                                                        # (local)
cs_E2 = CubicSpline(tau_data, E2_data)                                                                        # (local)
cs_E3 = CubicSpline(tau_data, E3_data)                                                                        # (local)
cs_n12 = CubicSpline(tau_data, norm_12_data)                                                                  # (local)
cs_n23 = CubicSpline(tau_data, norm_23_data)                                                                  # (local)

# =====================================================================
# HELPER: Extract PMNS angles from 3x3 unitary matrix
# =====================================================================
def extract_pmns(U):
    sin2_13 = abs(U[0, 2]) ** 2                                                                               # (local) |U_e3|^2
    theta_13 = np.degrees(np.arcsin(np.sqrt(sin2_13)))                                                        # (local)

    if abs(U[0, 0]) > 1e-15:
        tan2_12 = abs(U[0, 1]) ** 2 / abs(U[0, 0]) ** 2                                                       # (local)
        theta_12 = np.degrees(np.arctan(np.sqrt(tan2_12)))                                                    # (local)
    else:
        theta_12 = 90.0                                                                                       # (local) fallback
    if abs(U[2, 2]) > 1e-15:
        tan2_23 = abs(U[1, 2]) ** 2 / abs(U[2, 2]) ** 2                                                       # (local)
        theta_23 = np.degrees(np.arctan(np.sqrt(tan2_23)))                                                    # (local)
    else:
        theta_23 = 90.0                                                                                       # (local) fallback

    J = np.imag(U[0, 0] * U[1, 1] * np.conj(U[0, 1]) * np.conj(U[1, 0]))                                      # (local) Jarlskog (real=>0)
    return {'sin2_13': sin2_13, 'theta_13': theta_13, 'theta_12': theta_12,
            'theta_23': theta_23, 'J': J}


# =====================================================================
# FINE GRID COMPUTATION
# =====================================================================
tau_fine = np.arange(0.15, 0.225, 0.01)                                                                       # (local) fine tau scan
n_fine = len(tau_fine)                                                                                        # (local)
print(f"\nFine tau grid: {tau_fine}")
print(f"Number of fine-grid points: {n_fine}")

results = []                                                                                                  # (local)

print("\n" + "=" * 75)
print("FINE-GRID METHOD B RESULTS")
print("=" * 75)
print(f"{'tau':>5} | {'E1':>10} | {'E2':>10} | {'E3':>10} | "
      f"{'V12':>10} | {'V23':>10} | {'sin2_13':>10} | "
      f"{'th12':>8} | {'th23':>8} | {'R':>10}")
print("-" * 110)

for tau in tau_fine:
    E1 = float(cs_E1(tau))                                                                                    # (local)
    E2 = float(cs_E2(tau))                                                                                    # (local)
    E3 = float(cs_E3(tau))                                                                                    # (local)
    n12 = float(cs_n12(tau))                                                                                  # (local)
    n23 = float(cs_n23(tau))                                                                                  # (local)

    H_3x3 = np.array([                                                                                        # (local) tridiagonal Method-B Hamiltonian
        [E1, n12, 0.0],
        [n12, E2, n23],
        [0.0, n23, E3],
    ])
    m_evals, U = np.linalg.eigh(H_3x3)
    pmns = extract_pmns(U)                                                                                    # (local)

    denom = m_evals[1] ** 2 - m_evals[0] ** 2                                                                 # (local)
    R = (m_evals[2] ** 2 - m_evals[1] ** 2) / denom if abs(denom) > 1e-30 else float('inf')                    # (local)
    R_pdg = 1.0 / R if abs(R) > 1e-30 else float('inf')                                                       # (local)

    result = {
        'tau': tau, 'E1': E1, 'E2': E2, 'E3': E3, 'V_12': n12, 'V_23': n23,
        'H_3x3': H_3x3, 'eigenvalues': m_evals, 'U': U,
        'sin2_13': pmns['sin2_13'], 'theta_13': pmns['theta_13'],
        'theta_12': pmns['theta_12'], 'theta_23': pmns['theta_23'],
        'R': R, 'R_pdg': R_pdg, 'J': pmns['J'],
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

ref = {                                                                                                       # (local) S29b reference values
    0.15: {'sin2_13': 0.253715, 'theta_12': 35.06, 'theta_23': 48.76, 'R': 0.4781},
    0.20: {'sin2_13': 0.202569, 'theta_12': 36.55, 'theta_23': 41.97, 'R': 0.3810},
}

all_checks_pass = True                                                                                        # (local)
for tau_check in [0.15, 0.20]:
    for r in results:
        if abs(r['tau'] - tau_check) < 1e-10:
            fine = r
            break
    s29b = ref[tau_check]
    print(f"\n  tau = {tau_check:.2f}:")
    print(f"    {'Quantity':>15} | {'Fine grid':>12} | {'29b ref':>12} | {'Rel err (%)':>12} | {'Status':>8}")
    print(f"    {'-' * 70}")
    for key, label in [('sin2_13', 'sin^2(th13)'),
                       ('theta_12', 'theta_12 (deg)'),
                       ('theta_23', 'theta_23 (deg)'),
                       ('R', 'R')]:
        val_fine = fine[key]                                                                                  # (local)
        val_ref = s29b[key]                                                                                   # (local)
        rel_err = abs(val_fine - val_ref) / abs(val_ref) * 100                                                # (local)
        status = "PASS" if rel_err < 1.0 else "FAIL"                                                          # (local)
        if status == "FAIL":
            all_checks_pass = False
        print(f"    {label:>15} | {val_fine:12.6f} | {val_ref:12.6f} | {rel_err:12.4f} | {status:>8}")
print(f"\n  Overall cross-check: {'PASS' if all_checks_pass else 'FAIL'}")

# =====================================================================
# PDG WINDOW CROSSING ANALYSIS — PDG 2024 literals kept local per orchestrator
# =====================================================================
print("\n" + "=" * 75)
print("PDG WINDOW CROSSING ANALYSIS (PDG 2024 3-sigma)")
print("=" * 75)

pdg_windows = {                                                                                               # (local) PDG 2024 3-sigma windows
    'sin2_13': (0.020, 0.024, 'sin^2(theta_13)'),                                                             # PDG 2024
    'theta_12': (31.3, 35.9, 'theta_12 (deg)'),                                                               # PDG 2024
    'theta_23': (40.1, 51.7, 'theta_23 (deg)'),                                                               # PDG 2024
    'R_pdg': (0.028, 0.034, 'R_pdg = Dm21/Dm32'),                                                             # PDG 2024
}

pdg_best = {                                                                                                  # (local) PDG 2024 best-fit centers
    'sin2_13': 0.0218,
    'theta_12': 33.4,
    'theta_23': 42.2,
    'theta_23_alt': 49.2,
    'R_pdg': 0.030,
}

for key, (lo, hi, label) in pdg_windows.items():
    print(f"\n  {label}: PDG window [{lo}, {hi}]")
    values = [r[key] for r in results]                                                                        # (local)
    taus = [r['tau'] for r in results]                                                                        # (local)
    in_window = [(lo <= v <= hi) for v in values]                                                             # (local)
    any_in = any(in_window)                                                                                   # (local)
    crosses_lo = any((values[i] - lo) * (values[i + 1] - lo) < 0 for i in range(len(values) - 1))             # (local)
    crosses_hi = any((values[i] - hi) * (values[i + 1] - hi) < 0 for i in range(len(values) - 1))             # (local)
    for i, (tau, val, iw) in enumerate(zip(taus, values, in_window)):
        marker = " <-- IN WINDOW" if iw else ""                                                               # (local)
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
# DERIVATIVE ANALYSIS
# =====================================================================
print("\n" + "=" * 75)
print("DERIVATIVE ANALYSIS (finite differences)")
print("=" * 75)
print(f"{'tau':>5} | {'d(sin2_13)/dtau':>16} | {'d(th12)/dtau':>14} | {'d(th23)/dtau':>14} | {'dR/dtau':>12}")
print("-" * 70)
for i in range(1, len(results)):
    dt = results[i]['tau'] - results[i - 1]['tau']                                                            # (local)
    ds13 = (results[i]['sin2_13'] - results[i - 1]['sin2_13']) / dt                                           # (local)
    dt12 = (results[i]['theta_12'] - results[i - 1]['theta_12']) / dt                                         # (local)
    dt23 = (results[i]['theta_23'] - results[i - 1]['theta_23']) / dt                                         # (local)
    dR = (results[i]['R'] - results[i - 1]['R']) / dt                                                         # (local)
    tau_mid = (results[i]['tau'] + results[i - 1]['tau']) / 2                                                 # (local)
    print(f"{tau_mid:5.3f} | {ds13:16.6f} | {dt12:14.4f} | {dt23:14.4f} | {dR:12.6f}")

# =====================================================================
# SUMMARY TABLE
# =====================================================================
print("\n" + "=" * 75)
print("SUMMARY TABLE: Fine-Grid PMNS (Method B)")
print("=" * 75)
print(f"{'tau':>6} | {'sin^2(th13)':>12} | {'th12 (deg)':>11} | {'th23 (deg)':>11} | {'R':>10}")
print("-" * 60)
for r in results:
    print(f"{r['tau']:6.2f} | {r['sin2_13']:12.6f} | {r['theta_12']:11.2f} | "
          f"{r['theta_23']:11.2f} | {r['R']:10.4f}")

# =====================================================================
# SAVE DATA (T3 output, does not overwrite historical .npz)
# =====================================================================
save_dict = {'tau_fine': tau_fine, 'tau_coarse': tau_coarse,
             'method': 'B_degenerate_PT', 'interpolation': 'cubic_spline'}                                    # (local)

sin2_13_arr = np.array([r['sin2_13'] for r in results])                                                       # (local)
theta_12_arr = np.array([r['theta_12'] for r in results])                                                     # (local)
theta_23_arr = np.array([r['theta_23'] for r in results])                                                     # (local)
R_arr = np.array([r['R'] for r in results])                                                                   # (local)
R_pdg_arr = np.array([r['R_pdg'] for r in results])                                                           # (local)

save_dict['sin2_theta13'] = sin2_13_arr
save_dict['theta_12_deg'] = theta_12_arr
save_dict['theta_23_deg'] = theta_23_arr
save_dict['R_framework'] = R_arr
save_dict['R_pdg'] = R_pdg_arr

for i, r in enumerate(results):
    prefix = f"t{i}"                                                                                          # (local)
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

out_npz = f"{BASE}/s32c_pmns_fine_grid.npz"                                                                # (local) T3 output path
out_png = f"{BASE}/s32c_pmns_fine_grid.png"                                                                # (local) T3 output path
np.savez(out_npz, **save_dict)
print(f"\nSaved: {out_npz}")

# =====================================================================
# 4-panel plot with coarse overlay
# =====================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 32c (re-run): Fine-Grid PMNS Extraction (Method B)\n'
             r'$\tau \in [0.15, 0.22]$, cubic spline interpolation',
             fontsize=14, fontweight='bold')

coarse_results = []                                                                                           # (local)
for j, i in enumerate(np.where(mask)[0]):
    tau_c = tau_data[j]                                                                                       # (local)
    evals = d[f'eigenvalues_{i}']
    V_mat = d[f'V_pairing_{i}']
    E1c = evals[8]                                                                                            # (local)
    E2c = evals[9]                                                                                            # (local)
    E3c = evals[13]                                                                                           # (local)
    v_L1_L2 = V_mat[8, 9:13]                                                                                  # (local)
    n12c = np.linalg.norm(v_L1_L2)                                                                            # (local)
    L2_eff = v_L1_L2 / n12c                                                                                   # (local)
    V_L2_L3 = V_mat[9:13, 13:16]                                                                              # (local)
    v_eff_L3 = L2_eff @ V_L2_L3                                                                               # (local)
    n23c = np.linalg.norm(v_eff_L3)                                                                           # (local)
    H = np.array([[E1c, n12c, 0.0], [n12c, E2c, n23c], [0.0, n23c, E3c]])                                     # (local)
    me, Ue = np.linalg.eigh(H)
    p = extract_pmns(Ue)                                                                                      # (local)
    dm = me[1] ** 2 - me[0] ** 2                                                                              # (local)
    Rc = (me[2] ** 2 - me[1] ** 2) / dm if abs(dm) > 1e-30 else float('inf')                                  # (local)
    coarse_results.append({'tau': tau_c, 'sin2_13': p['sin2_13'],
                           'theta_12': p['theta_12'], 'theta_23': p['theta_23'], 'R': Rc})

tau_coarse_plot = np.array([cr['tau'] for cr in coarse_results])                                              # (local)
sin2_13_coarse = np.array([cr['sin2_13'] for cr in coarse_results])                                           # (local)
theta_12_coarse = np.array([cr['theta_12'] for cr in coarse_results])                                         # (local)
theta_23_coarse = np.array([cr['theta_23'] for cr in coarse_results])                                         # (local)
R_coarse = np.array([cr['R'] for cr in coarse_results])                                                       # (local)

ax = axes[0, 0]
ax.plot(tau_fine, sin2_13_arr, 'b-o', markersize=6, label='Fine grid (spline)')
ax.plot(tau_coarse_plot, sin2_13_coarse, 'rs', markersize=8, label='Coarse grid (exact)')
ax.axhspan(0.020, 0.024, alpha=0.2, color='green', label='PDG window')
ax.axhline(0.0218, color='green', linestyle='--', alpha=0.5, label='PDG best fit')
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$\sin^2(\theta_{13})$')
ax.set_title(r'$\sin^2(\theta_{13})$'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3); ax.set_xlim(0.14, 0.23)

ax = axes[0, 1]
ax.plot(tau_fine, theta_12_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, theta_12_coarse, 'rs', markersize=8, label='Coarse grid')
ax.axhspan(31.3, 35.9, alpha=0.2, color='green', label='PDG window')
ax.axhline(33.4, color='green', linestyle='--', alpha=0.5, label='PDG best fit')
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$\theta_{12}$ (deg)')
ax.set_title(r'$\theta_{12}$'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3); ax.set_xlim(0.14, 0.23)

ax = axes[1, 0]
ax.plot(tau_fine, theta_23_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, theta_23_coarse, 'rs', markersize=8, label='Coarse grid')
ax.axhspan(40.1, 51.7, alpha=0.2, color='green', label='PDG window')
ax.axhline(42.2, color='green', linestyle='--', alpha=0.3, label='PDG 42.2')
ax.axhline(49.2, color='green', linestyle=':', alpha=0.3, label='PDG 49.2')
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$\theta_{23}$ (deg)')
ax.set_title(r'$\theta_{23}$'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3); ax.set_xlim(0.14, 0.23)

ax = axes[1, 1]
ax.plot(tau_fine, R_arr, 'b-o', markersize=6, label='Fine grid')
ax.plot(tau_coarse_plot, R_coarse, 'rs', markersize=8, label='Coarse grid')
ax.set_xlabel(r'$\tau$'); ax.set_ylabel(r'$R = \Delta m^2_{32}/\Delta m^2_{21}$')
ax.set_title(r'$R$ (mass ratio)'); ax.legend(fontsize=8); ax.grid(True, alpha=0.3); ax.set_xlim(0.14, 0.23)
ax.text(0.05, 0.95, f'PDG: R ~ 32.6\nModel: R ~ {R_arr.mean():.2f}\n(inverted)',
        transform=ax.transAxes, fontsize=8, verticalalignment='top',
        bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"Saved: {out_png}")

# =====================================================================
# CLOSURE HASH (ordered input-pin map)
# =====================================================================
pin_map = (
    f"source_py={SOURCE_SHA};"
    f"input_npz={INPUT_SHA};"
    f"tau_fine_lo=0.15;tau_fine_hi=0.22;tau_fine_step=0.01;"
    f"method=B_degenerate_PT;interpolation=cubic_spline;"
    f"n_fine={n_fine};n_coarse={n_data};"
)                                                                                                             # (local) ordered input-pin map
CLOSURE_SHA = hashlib.sha256(pin_map.encode('utf-8')).hexdigest()                                             # (local)

# =====================================================================
# 4-TUPLE OUTPUT TAG (pre-verdict, final non-verdict line)
# =====================================================================
# Primary observable reported: sin^2(theta_13) at the physical fold tau ~ 0.190
# Secondary: theta_12, theta_23, R all at fold
idx_fold = int(np.argmin(np.abs(tau_fine - 0.19)))                                                            # (local)
sin2_13_fold = float(sin2_13_arr[idx_fold])                                                                   # (local)
theta_12_fold = float(theta_12_arr[idx_fold])                                                                 # (local)
theta_23_fold = float(theta_23_arr[idx_fold])                                                                 # (local)
R_fold = float(R_arr[idx_fold])                                                                               # (local)

print("\n" + "=" * 75)
print("T3 OUTPUT 4-TUPLE")
print("=" * 75)
print(f"  value=sin2_13_fold={sin2_13_fold:.6f},theta12_fold={theta_12_fold:.3f}deg,"
      f"theta23_fold={theta_23_fold:.3f}deg,R_fold={R_fold:.4f}")
print(f"  scheme=MethodB_degenerate_PT_cubic_spline")
print(f"  convention=U[alpha,i]_ascending_mass_flavor_basis")
print(f"  L_max=singlet_L1L2L3_subspace_(0..15)_from_L_max>=1_D_K")
print(f"  cross_check_vs_s29b_tau015_tau020={'PASS' if all_checks_pass else 'FAIL'}")
print(f"  sha256_closure={CLOSURE_SHA}")

print("\n" + "=" * 75)
print("COMPUTATION COMPLETE — T3 RE-RUN")
print("=" * 75)
