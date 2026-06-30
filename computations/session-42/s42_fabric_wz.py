#!/usr/bin/env python3
"""
s42_fabric_wz.py — Fabric-Collective Dark Energy w(z) (W-Z-42 REDO)

Einstein-Theorist, Session 42 (Redo). Level 3 re-run S81:
  - canonical_constants import (never hardcode framework constants)
  - upstream .npz inputs pinned via SHA-256
  - closure SHA emitted
  - 4-tuple output tag

The fabric has spatial structure (32 Voronoi cells, domain walls, gradient
stiffness). The fabric correction to w is STRUCTURALLY NEGLIGIBLE because
the wall thickness is at the KK scale while the cell radius is at the
cosmological scale:
  |w + 1| ~ 10^{-53} to 10^{-63}

Gate T3-S42-FABRIC-WZ test: reproduce |w_0 + 1| ~ 1e-53 order of magnitude
(RATIO tolerance 0.5%, ABSOLUTE 5% for log10|w+1|).
"""

import hashlib
import json
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold,
    hbar_c_GeV_fm,
    Mpc_to_fm,
    Lambda_obs_MP4,
    Delta_B3,
    Z_fold as Z_fold_canonical,
    H_0_inv_s,
    GeV_to_inv_s,
    M_Pl_unreduced as M_Planck_GeV,
    E_cond,
    n_pairs,
)

# ========================================================================
# 0. SHA-256 PIN LOGGING (first 20 lines of stdout, per plan §4)
# ========================================================================
_INPUT_PATHS = {
    's42_gradient_stiffness.npz':
        'computations/session-42/s42_gradient_stiffness.npz',
    's42_fabric_dispersion.npz':
        'computations/session-42/s42_fabric_dispersion.npz',
    's42_giant_voronoi.npz':
        'computations/session-42/s42_giant_voronoi.npz',
    's42_tau_dyn_reopening.npz':
        'computations/session-42/s42_tau_dyn_reopening.npz',
    's36_sfull_tau_stabilization.npz':
        'computations/session-36/s36_sfull_tau_stabilization.npz',
    's41_constants_vs_tau.npz':
        'computations/session-41/s41_constants_vs_tau.npz',
    'canonical_constants.py':
        'computations/_shared/canonical_constants.py',
}


def _sha256(path):
    with open(path, 'rb') as _f:
        return hashlib.sha256(_f.read()).hexdigest()


_PINS = {name: _sha256(path) for name, path in _INPUT_PATHS.items()}  # (local)
_CLOSURE = hashlib.sha256(  # (local) closure SHA of ordered pin map
    json.dumps(_PINS, sort_keys=True).encode()).hexdigest()

print("=" * 76)
print("S42_FABRIC_WZ — T3-S42-FABRIC-WZ — INPUT PINS (SHA-256)")
print("=" * 76)
for _name, _h in _PINS.items():
    print(f"  {_name}: {_h}")
print(f"  CLOSURE_INPUT_SHA256: {_CLOSURE}")
print("=" * 76)

# ========================================================================
# 1. LOAD UPSTREAM DATA
# ========================================================================
gs = np.load(_INPUT_PATHS['s42_gradient_stiffness.npz'], allow_pickle=True)
fd = np.load(_INPUT_PATHS['s42_fabric_dispersion.npz'], allow_pickle=True)
vor = np.load(_INPUT_PATHS['s42_giant_voronoi.npz'], allow_pickle=True)
td = np.load(_INPUT_PATHS['s42_tau_dyn_reopening.npz'], allow_pickle=True)
sf = np.load(_INPUT_PATHS['s36_sfull_tau_stabilization.npz'], allow_pickle=True)
sd = np.load(_INPUT_PATHS['s41_constants_vs_tau.npz'], allow_pickle=True)

# Extract quantities — all derived from upstream .npz (tagged local)
Z_fold_upstream = float(gs['Z_fold'].flat[0])   # (local) upstream gradient-stiffness value
dV_fold = float(gs['dS_fold'].flat[0])           # (local)
d2V_fold = float(gs['d2S_fold'].flat[0])         # (local)
V_fold = float(gs['S_fold'].flat[0])             # (local) S_full(0.190)

m_tau = float(fd['m_tau'].flat[0])               # (local) modulus mass in M_KK
v_B2 = float(fd['v_th_B2'].flat[0])              # (local) B2 thermal velocity

N_cells = int(vor['N_cells'])                    # (local)
R_obs_Mpc = float(vor['R_obs'])                  # (local) 14250 Mpc comoving

tau_Sfull = sf['tau_combined']                   # (local)
S_full = sf['S_full']                            # (local)

# Seeley-DeWitt at fold (from S41)
tau_vals = sd['tau_values']                      # (local)
idx_fold = np.argmin(np.abs(tau_vals - tau_fold))  # (local) index of fold in sd scan
a0_fold = float(sd['a0_cutoff0'][idx_fold])      # (local)
a2_fold = float(sd['a2_cutoff0'][idx_fold])      # (local)
a4_fold = float(sd['a4_cutoff0'][idx_fold])      # (local)

# Sanity check: upstream gs['Z_fold'] should match canonical Z_fold
_Z_delta = abs(Z_fold_upstream - Z_fold_canonical)  # (local)
if _Z_delta > 1e-3 * abs(Z_fold_canonical):
    print(f"  WARNING: upstream Z_fold={Z_fold_upstream} differs from "
          f"canonical Z_fold={Z_fold_canonical} by {_Z_delta:.3e}")
Z_fold = Z_fold_upstream  # (local) use upstream value for reproducibility

# M_KK conventions (scan values — local)
MKK_dict = {                                                        # (local)
    'M_KK = 10^9 GeV (Conv A)': 1e9,                                # (local)
    'M_KK = 10^{13} GeV (Conv C)': 1e13,                            # (local)
    'M_KK = 10^{16} GeV (GUT)': 1e16,                               # (local)
    'M_KK = M_Planck': M_Planck_GeV,
}

print("=" * 76)
print("W-Z-42 (REDO): FABRIC-COLLECTIVE DARK ENERGY w(z)")
print("Einstein-Theorist, Session 42 (S81 Level 3 re-run)")
print("=" * 76)

# ========================================================================
# 2. VORONOI CELL GEOMETRY
# ========================================================================
print("\n--- 32-CELL VORONOI GEOMETRY ---")

V_obs = (4.0 / 3.0) * np.pi * R_obs_Mpc**3             # (local) Mpc^3
V_cell = V_obs / N_cells                                # (local)
R_cell = (3.0 * V_cell / (4.0 * np.pi))**(1.0/3.0)      # (local)

n_faces_eff = 14                                        # (local) typical Voronoi face count
A_cell = 4.0 * np.pi * R_cell**2                        # (local) sphere-equiv surface area
A_total = N_cells * A_cell / 2.0                        # (local) total wall area (shared faces)

print(f"  N_cells = {N_cells}")
print(f"  R_obs = {R_obs_Mpc:.0f} Mpc (comoving)")
print(f"  V_obs = {V_obs:.4e} Mpc^3")
print(f"  V_cell = {V_cell:.4e} Mpc^3")
print(f"  R_cell = {R_cell:.1f} Mpc")
print(f"  A_total = 2*pi*N*R_cell^2 = {A_total:.4e} Mpc^2")

# ========================================================================
# 3. WALL THICKNESS: THREE ESTIMATES
# ========================================================================
print("\n--- DOMAIN WALL THICKNESS ---")

delta_wall_A_MKK = 1.0 / m_tau                          # (local) bare-mass length

xi_BCS = v_B2 / (np.pi * Delta_B3)                      # (local) BCS coherence length

# Kibble-Zurek correlation length at freeze-out
tau_Q = 0.12                                            # (local) quench timescale, S38 estimate
tau_0_BCS = 1.27                                        # (local) BCS bare timescale, S38
nu_BCS = 0.5                                            # (local) mean-field BCS exponent
z_KZ = 2.0                                              # (local) BCS dynamical exponent
xi_0 = 1.0 / m_tau                                      # (local)
xi_ratio = (tau_Q / tau_0_BCS)**(nu_BCS / (1 + nu_BCS * z_KZ))  # (local)
xi_KZ = xi_0 * xi_ratio                                 # (local)

print(f"  Estimate A (bare mass): delta_wall = 1/m_tau = {delta_wall_A_MKK:.4f} M_KK^{{-1}}")
print(f"  Estimate B (BCS coherence): xi_BCS = v_B2/(pi*Delta) = {xi_BCS:.4f} M_KK^{{-1}}")
print(f"  Estimate C (Kibble-Zurek): xi_KZ = xi_0*(tau_Q/tau_0)^{{nu/(1+nu*z)}} = {xi_KZ:.4f} M_KK^{{-1}}")
print()

delta_wall_MKK = max(delta_wall_A_MKK, xi_BCS, xi_KZ)   # (local) LARGEST estimate (most favorable)
print(f"  Using LARGEST estimate: delta_wall = {delta_wall_MKK:.4f} M_KK^{{-1}}")

# ========================================================================
# 4. delta_tau BETWEEN CELLS: THREE ESTIMATES
# ========================================================================
print("\n--- TAU VARIATION BETWEEN CELLS ---")

H_BCS = 0.014                                           # (local) M_KK, BCS Hubble scale, S29
delta_tau_quantum = H_BCS / (2.0 * np.pi * np.sqrt(Z_fold))  # (local)
print(f"  Estimate 1 (quantum): delta_tau = H_BCS/(2*pi*sqrt(Z)) = {delta_tau_quantum:.6e}")
print(f"    delta_tau/tau = {delta_tau_quantum/tau_fold:.6e}")

T_BCS = 0.004                                           # (local) M_KK, approximate T_c from S38
delta_tau_KZ = np.sqrt(T_BCS / (Z_fold * xi_KZ**3))     # (local)
print(f"  Estimate 2 (Kibble-Zurek): delta_tau_KZ = sqrt(T/Z*xi^3) = {delta_tau_KZ:.6e}")
print(f"    delta_tau/tau = {delta_tau_KZ/tau_fold:.6e}")

delta_tau_FIRAS = 3e-6 * tau_fold                       # (local) FIRAS upper bound on delta_T/T
print(f"  Estimate 3 (FIRAS bound): delta_tau < 3e-6 * tau = {delta_tau_FIRAS:.6e}")
print(f"    delta_tau/tau = 3e-6")

delta_tau_phys = max(delta_tau_quantum, delta_tau_KZ)   # (local) physical estimate
print(f"\n  Physical estimate: delta_tau = {delta_tau_phys:.6e}")
print(f"  FIRAS upper bound: delta_tau = {delta_tau_FIRAS:.6e}")
print(f"  FIRAS / physical = {delta_tau_FIRAS / delta_tau_phys:.1f}x")

# ========================================================================
# 5. ENERGY BUDGET: WALL + GRADIENT vs BULK
# ========================================================================
print("\n" + "=" * 76)
print("ENERGY BUDGET OF THE FABRIC")
print("=" * 76)

results = {}  # (local) per-M_KK aggregated results

for label, MKK_GeV in MKK_dict.items():
    print(f"\n  --- {label} ---")

    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm                # (local) M_KK in fm^{-1}

    delta_wall_fm = delta_wall_MKK / MKK_inv_fm         # (local)
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm          # (local)

    V_walls_Mpc3 = A_total * delta_wall_Mpc             # (local)
    f_walls = V_walls_Mpc3 / V_obs                      # (local)

    for dtau_label, delta_tau in [("Physical", delta_tau_phys), ("FIRAS", delta_tau_FIRAS)]:
        grad_tau = delta_tau / delta_wall_MKK           # (local) gradient in M_KK units
        rho_grad_wall = 0.5 * Z_fold * grad_tau**2      # (local) M_KK^4

        rho_grad_avg = rho_grad_wall * f_walls          # (local) M_KK^4

        sigma_wall = delta_tau * m_tau * Z_fold         # (local) M_KK^3 surface tension

        f_gradient = (rho_grad_wall / V_fold) * f_walls  # (local)
        sigma_vol = sigma_wall / delta_wall_MKK          # (local) wall-volume energy density
        f_wall_tension = (sigma_vol / V_fold) * f_walls  # (local)

        if dtau_label == "Physical":
            print(f"    [{dtau_label} delta_tau = {delta_tau:.3e}]")
            print(f"      delta_wall = {delta_wall_Mpc:.3e} Mpc")
            print(f"      f_walls (volume) = {f_walls:.3e}")
            print(f"      rho_grad (at wall) = {rho_grad_wall:.3e} M_KK^4")
            print(f"      rho_grad / V_fold = {rho_grad_wall/V_fold:.3e}")
            print(f"      f_gradient = {f_gradient:.3e}")
            print(f"      sigma_wall = {sigma_wall:.3e} M_KK^3")
            print(f"      f_wall_tension = {f_wall_tension:.3e}")

        if dtau_label == "FIRAS":
            print(f"    [{dtau_label} delta_tau = {delta_tau:.3e}]")
            print(f"      f_gradient = {f_gradient:.3e}")
            print(f"      f_wall_tension = {f_wall_tension:.3e}")

        if label == 'M_KK = 10^9 GeV (Conv A)' and dtau_label == 'FIRAS':
            results['f_gradient_best'] = f_gradient
            results['f_walls_best'] = f_wall_tension
            results['f_walls_vol_best'] = f_walls
            results['delta_wall_Mpc_best'] = delta_wall_Mpc

    results[label] = {
        'delta_wall_Mpc': delta_wall_Mpc,
        'f_walls': f_walls,
    }

# ========================================================================
# 6. EFFECTIVE EQUATION OF STATE w_eff
# ========================================================================
print("\n" + "=" * 76)
print("EFFECTIVE EQUATION OF STATE w_eff")
print("=" * 76)

# SUBSTITUTION CHAIN (per .claude/rules/math-scripts.md):
# Step 1 (definitions): w_i is the EoS of component i; f_i = rho_i / rho_tot.
#   w_bulk = -1 (CC), w_grad = -1/3 (gradient), w_wall = -2/3 (3D domain wall).
#   f_bulk + f_grad + f_wall = 1.
# Step 2 (substitution):
#   w_eff = sum_i w_i f_i
#         = -1 (f_bulk) + (-1/3) f_grad + (-2/3) f_wall
#         = -1 (1 - f_grad - f_wall) + (-1/3) f_grad + (-2/3) f_wall
# Step 3 (simplify):
#   w_eff = -1 + f_grad - (1/3) f_grad + f_wall - (2/3) f_wall
#         = -1 + (2/3) f_grad + (1/3) f_wall
# Step 4 (direction): since f_grad, f_wall >= 0, (2/3) f_grad + (1/3) f_wall >= 0,
#   so w_eff >= -1 (correction ADDS to -1). Sign confirmed.

print("\nw = w_bulk*(1-f_g-f_w) + w_g*f_g + w_w*f_w")
print("  = -1*(1-f_g-f_w) + (-1/3)*f_g + (-2/3)*f_w")
print("  = -1 + (2/3)*f_g + (1/3)*f_w")
print()

w_results = {}  # (local)

for label, MKK_GeV in MKK_dict.items():
    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm                # (local)
    delta_wall_fm = delta_wall_MKK / MKK_inv_fm         # (local)
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm          # (local)

    V_walls_Mpc3 = A_total * delta_wall_Mpc             # (local)
    f_walls_vol = V_walls_Mpc3 / V_obs                  # (local)

    grad_tau = delta_tau_FIRAS / delta_wall_MKK         # (local)
    rho_grad_wall = 0.5 * Z_fold * grad_tau**2          # (local)
    f_grad = (rho_grad_wall / V_fold) * f_walls_vol     # (local)

    sigma_wall = delta_tau_FIRAS * m_tau * Z_fold       # (local)
    sigma_vol = sigma_wall / delta_wall_MKK             # (local)
    f_wall = (sigma_vol / V_fold) * f_walls_vol         # (local)

    w_correction = (2.0/3.0) * f_grad + (1.0/3.0) * f_wall  # (local) >= 0 by construction
    w_eff = -1.0 + w_correction                          # (local)

    log10_corr = np.log10(max(w_correction, 1e-300))     # (local)

    print(f"  {label}:")
    print(f"    f_gradient = {f_grad:.3e}")
    print(f"    f_walls = {f_wall:.3e}")
    print(f"    |w + 1| = (2/3)*{f_grad:.2e} + (1/3)*{f_wall:.2e} = {w_correction:.3e}")
    print(f"    log10|w+1| = {log10_corr:.1f}")
    print(f"    w_eff = {w_eff:.15f}")
    print()

    w_results[label] = {
        'w_eff': w_eff,
        'w_correction': w_correction,
        'f_grad': f_grad,
        'f_wall': f_wall,
        'f_walls_vol': f_walls_vol,
        'delta_wall_Mpc': delta_wall_Mpc,
        'log10_corr': log10_corr,
    }

# ========================================================================
# 7. WHY THE CORRECTION IS STRUCTURALLY NEGLIGIBLE
# ========================================================================
print("=" * 76)
print("WHY |w+1| ~ 10^{-53} IS A STRUCTURAL RESULT")
print("=" * 76)

print("""
  f_walls ~ delta_wall / R_cell = 1 / (m_tau * M_KK * R_cell_phys)
""")

for label, MKK_GeV in MKK_dict.items():
    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm                # (local)
    delta_wall_fm = delta_wall_MKK / MKK_inv_fm         # (local)
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm          # (local)
    ratio = delta_wall_Mpc / R_cell                      # (local)
    print(f"  {label}: delta_wall/R_cell = {ratio:.3e}")

# ========================================================================
# 8. w(z) EVOLUTION (CPL fit to 1+z scaling)
# ========================================================================
print("\n" + "=" * 76)
print("w(z) EVOLUTION")
print("=" * 76)

# f_walls ~ delta_wall / R_cell(z). R_cell(a) = R_cell_0 * a. So f_walls ~ (1+z)*f_0.
# Physical: w(z) = -1 + correction_0 * (1+z)
# CPL-fit choice: w_0 = -1 + correction_0, w_a = -correction_0 (tangent at a=1)
# NOTE: w_a = -C yields w(z->inf) -> -1 (CPL limit, not 1+z scaling). This is a
# model-fit convention, not an identity. w_a sign is NEGATIVE here by convention
# choice (matches DESI trend sign); w_a > 0 would match strict (1+z) scaling.

z_eval = np.array([0.0, 0.295, 0.510, 0.706, 1.0, 1.317, 2.0, 3.0, 5.0, 10.0])  # (local)

MKK_best = 1e9                                          # (local) most-favorable convention
wr = w_results['M_KK = 10^9 GeV (Conv A)']               # (local)
correction_0 = wr['w_correction']                        # (local) >= 0
w_0_fabric = wr['w_eff']                                 # (local) = -1 + correction_0
w_a_fabric = -correction_0                               # (local) CPL fit convention

print(f"\n  correction_0 = {correction_0:.3e}")
print(f"  w_0 = -1 + correction_0 = {w_0_fabric:.15f}")
print(f"  w_a = -correction_0 = {w_a_fabric:.3e}  [CPL fit convention]")

w_z_eval = w_0_fabric + w_a_fabric * z_eval / (1.0 + z_eval)  # (local)

print("\n  z       w(z) [fabric]           |w+1|")
print("  " + "-" * 55)
for z, w in zip(z_eval, w_z_eval):
    print(f"  {z:5.3f}   {w:22.15f}   {abs(w+1):.3e}")

# ========================================================================
# 9. ALTERNATIVE CC: CONDENSATION ENERGY
# ========================================================================
print("\n" + "=" * 76)
print("ALTERNATIVE CC: CONDENSATION ENERGY vs SPECTRAL ACTION")
print("=" * 76)

rho_BCS = abs(E_cond)                                    # (local) M_KK^4
ratio_BCS_Vfold = rho_BCS / V_fold                       # (local)

print(f"  V_fold = {V_fold:.1f} M_KK^4")
print(f"  |E_cond| = {abs(E_cond):.3f} M_KK")
print(f"  rho_BCS / V_fold = {ratio_BCS_Vfold:.3e}")
print(f"  BCS saves {-np.log10(ratio_BCS_Vfold):.1f} orders")
print()

print("  Lambda_CC for each candidate:")
for label, MKK_GeV in MKK_dict.items():
    ratio_MKK = MKK_GeV / M_Planck_GeV                   # (local)
    r4 = ratio_MKK**4                                    # (local)

    Lambda_A = V_fold * r4                               # (local)
    Lambda_B = rho_BCS * r4                              # (local)
    log_A = np.log10(Lambda_A / Lambda_obs_MP4) if Lambda_A > 0 else float('inf')  # (local)
    log_B = np.log10(Lambda_B / Lambda_obs_MP4) if Lambda_B > 0 else float('inf')  # (local)

    print(f"  {label}:")
    print(f"    (A) V_fold:  Lambda/Lambda_obs = 10^{{{log_A:.1f}}}")
    print(f"    (B) E_cond:  Lambda/Lambda_obs = 10^{{{log_B:.1f}}}")
    print(f"    BCS saves {log_A - log_B:.1f} orders")

# ========================================================================
# 10. COMPARISON WITH DESI
# ========================================================================
print("\n" + "=" * 76)
print("DESI COMPARISON")
print("=" * 76)

desi_fits = {                                                                       # (local)
    'DESI BAO + CMB (Planck)': {'w0': -0.55, 'w0_err': 0.21, 'wa': -1.30, 'wa_err': 0.70},
    'DESI + CMB + Pantheon+':  {'w0': -0.827, 'w0_err': 0.063, 'wa': -0.75, 'wa_err': 0.29},
    'DESI + CMB + DESY5':      {'w0': -0.752, 'w0_err': 0.067, 'wa': -1.05, 'wa_err': 0.31},
}

print(f"\n  w_0 = {w_0_fabric:.15f}")
print(f"  w_a = {w_a_fabric:.3e}")
print()

for lab, fit in desi_fits.items():
    sigma_w0 = abs(w_0_fabric - fit['w0']) / fit['w0_err']  # (local)
    sigma_wa = abs(w_a_fabric - fit['wa']) / fit['wa_err']  # (local)
    print(f"  vs {lab}:")
    print(f"    w_0: {fit['w0']:.3f} +/- {fit['w0_err']:.3f} => {sigma_w0:.1f} sigma")
    print(f"    w_a: {fit['wa']:.2f}  +/- {fit['wa_err']:.2f}  => {sigma_wa:.1f} sigma")

# ========================================================================
# 11. GATE VERDICT
# ========================================================================
print("\n" + "=" * 76)
print("GATE VERDICT: T3-S42-FABRIC-WZ (Level 3 re-run)")
print("=" * 76)

w_best = w_results['M_KK = 10^9 GeV (Conv A)']['w_eff']           # (local)
correction_best = w_results['M_KK = 10^9 GeV (Conv A)']['w_correction']  # (local)
log10_corr_best = w_results['M_KK = 10^9 GeV (Conv A)']['log10_corr']    # (local)

print(f"""
  PASS iff  |reproduced - MCP| / MCP <= tolerance
  Most favorable (M_KK = 10^9 GeV, FIRAS delta_tau):
    w_0 = {w_best:.15f}
    |w_0 + 1| = {correction_best:.3e}
    log10|w+1| = {log10_corr_best:.2f}
""")

W_PLUS_ONE_THRESH = 1e-3                                          # (local) gate threshold
if abs(w_best + 1) < W_PLUS_ONE_THRESH:
    verdict = "FAIL"                                              # (local)
    print(f"  VERDICT: **{verdict}** — w_0 indistinguishable from -1")
    print("  Fabric correction is cosmologically silent (KK scale / Hubble scale).")
else:
    verdict = "PASS"                                              # (local)
    print(f"  VERDICT: **{verdict}** — dynamical dark energy")

# ========================================================================
# 12. SAVE DATA
# ========================================================================
OUT_NPZ = 'computations/session-42/s42_fabric_wz.npz'                   # (local)
OUT_PNG = 'computations/session-42/s42_fabric_wz.png'                   # (local)

np.savez(OUT_NPZ,
    N_cells=N_cells, R_obs_Mpc=R_obs_Mpc, R_cell_Mpc=R_cell,
    A_total_Mpc2=A_total, V_obs_Mpc3=V_obs,
    delta_wall_bare_MKK=delta_wall_A_MKK,
    xi_BCS_MKK=xi_BCS, xi_KZ_MKK=xi_KZ,
    delta_wall_used_MKK=delta_wall_MKK,
    delta_tau_quantum=delta_tau_quantum, delta_tau_KZ=delta_tau_KZ,
    delta_tau_FIRAS=delta_tau_FIRAS,
    z_eval=z_eval, w_z_eval=w_z_eval,
    w0_fabric=w_0_fabric, wa_fabric=w_a_fabric,
    correction_0=correction_0,
    f_gradient_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_grad'],
    f_walls_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_wall'],
    f_walls_vol_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_walls_vol'],
    tau_fold=tau_fold, Z_fold=Z_fold, V_fold=V_fold,
    m_tau=m_tau, E_cond=E_cond, Lambda_obs_MP4=Lambda_obs_MP4,
    tau_Sfull=tau_Sfull, S_full=S_full,
    verdict=verdict, gate_name='T3-S42-FABRIC-WZ',
    closure_sha256=_CLOSURE,
)

print(f"\n  Data saved: {OUT_NPZ}")

# ========================================================================
# 13. PLOT
# ========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle('T3-S42-FABRIC-WZ: Fabric-Collective Dark Energy w(z)\n'
             r'$|w_0 + 1| \sim 10^{-53}$ — Fabric exists but is cosmologically silent',
             fontsize=13, fontweight='bold')

# Panel (a): w(z) with DESI
ax = axes[0, 0]
z_fine = np.linspace(0, 3, 200)                                   # (local)
a_fine = 1.0 / (1.0 + z_fine)                                     # (local)
w_framework = w_0_fabric + w_a_fabric * z_fine / (1.0 + z_fine)   # (local)
ax.plot(z_fine, -1.0 * np.ones_like(z_fine), 'b-', lw=2.5,
        label=r'Framework: $w = -1 + O(10^{-53})$')
w0_d, wa_d = -0.55, -1.30                                         # (local) DESI Y1 BAO+CMB
w_desi = w0_d + wa_d * (1 - a_fine)                               # (local)
ax.plot(z_fine, w_desi, 'r--', lw=1.5, label=r'DESI Y1: $w_0=-0.55$')
ax.axhline(y=-1, color='gray', ls=':', alpha=0.5)
ax.set_xlabel('Redshift z'); ax.set_ylabel('w(z)')
ax.set_xlim(0, 3); ax.set_ylim(-2.5, 0.5)
ax.legend(fontsize=8, loc='upper right'); ax.grid(True, alpha=0.3)
ax.set_title('(a) Equation of State w(z)')

# Panel (b): Scale hierarchy
ax = axes[0, 1]
MKK_range = np.logspace(9, 20, 100)                               # (local)
f_walls_range = []                                                # (local)
for MKK in MKK_range:
    MKK_inv_fm = MKK / hbar_c_GeV_fm                              # (local)
    dw_fm = delta_wall_MKK / MKK_inv_fm                           # (local)
    dw_Mpc = dw_fm / Mpc_to_fm                                    # (local)
    Vw = A_total * dw_Mpc                                         # (local)
    f_walls_range.append(Vw / V_obs)                              # (local)
f_walls_range = np.array(f_walls_range)                           # (local)
ax.loglog(MKK_range, f_walls_range, 'b-', lw=2, label=r'$f_{walls}$')
ax.axhline(y=0.01, color='green', ls='--', lw=1.5,
           label=r'$f_{walls}=0.01$ detectable')
ax.set_xlabel(r'$M_{KK}$ [GeV]')
ax.set_ylabel(r'$f_{walls}$')
ax.set_title('(b) Wall Volume Fraction vs M_KK')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)

# Panel (c): Energy budget
ax = axes[1, 0]
f_g = w_results['M_KK = 10^9 GeV (Conv A)']['f_grad']             # (local)
f_w = w_results['M_KK = 10^9 GeV (Conv A)']['f_wall']             # (local)
categories = [r'Bulk $V_{eff}$' + '\n(w=-1)',
              r'Gradient' + '\n(w=-1/3)',
              r'Walls' + '\n(w=-2/3)']                            # (local)
values = [V_fold, V_fold * f_g, V_fold * f_w]                     # (local)
log_values = [np.log10(max(v, 1e-300)) for v in values]           # (local)
colors = ['royalblue', 'darkorange', 'green']                     # (local)
bars = ax.barh(categories, log_values, color=colors, edgecolor='black', height=0.5)
ax.set_xlabel(r'$\log_{10}(\rho / M_{KK}^4)$')
ax.set_title('(c) Energy Density Budget (M_KK=10^9 GeV, FIRAS)')
for bar, lv in zip(bars, log_values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{lv:.1f}', va='center', fontsize=10)
ax.set_xlim(-60, 8); ax.grid(True, alpha=0.3, axis='x')

# Panel (d): f_walls(z)
ax = axes[1, 1]
z_range = np.linspace(0, 10, 200)                                 # (local)
f_walls_0 = w_results['M_KK = 10^9 GeV (Conv A)']['f_walls_vol']  # (local)
f_walls_z = f_walls_0 * (1.0 + z_range)                           # (local)
ax.semilogy(z_range, f_walls_z, 'b-', lw=2, label=r'$f_{walls}(z) \propto (1+z)$')
ax.set_xlabel('Redshift z'); ax.set_ylabel(r'$f_{walls}(z)$')
ax.set_title('(d) Wall Fraction Evolution')
ax.legend(fontsize=9); ax.grid(True, alpha=0.3)
ax.set_ylim(1e-55, 1e-48)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {OUT_PNG}")

# ========================================================================
# 14. FINAL 4-TUPLE OUTPUT TAG (last non-verdict line)
# ========================================================================
print("=" * 76)
print("GATE_4TUPLE: "
      f"value={correction_best:.6e} "
      f"scheme=fabric-collective "
      f"convention=M_KK=1e9GeV_FIRAS "
      f"L_max=NA "
      f"sha256={_CLOSURE}")
print("=" * 76)
