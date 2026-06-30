#!/usr/bin/env python3
"""
S63 GRAV-BACKREACT-63 v2: Gravitational Backreaction on Gaudin Charges
=======================================================================

Corrected computation using the XXX Gaudin conserved charges (proven to
mutually commute to machine epsilon) in the physical N_pair=4 sector.

Gate: GRAV-BACKREACT-63 | W6-02 | CC-PATH
  PASS if any charge shift > 1% (integrability broken)
  FAIL if all shifts < 0.1% (charges robust)

Key correction from v1: The R-G charges must include BOTH exchange terms
s_k^+ s_l^- AND s_l^+ s_k^- (the full Heisenberg exchange), with the
factor 1/(2*(eps_k - eps_l)) for each, giving the correct XXX Gaudin algebra.

Session: S63 W6-02
Author: Einstein Theorist
"""

import numpy as np
from scipy.linalg import eigh, eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
from itertools import combinations

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    E_cond, Delta_0_OES, N_dof_BCS,
    E_B1, E_B2_mean, E_B3_mean,
    G_N, hbar_GeV_s, t_universe_s, H_0_inv_s, H_0_GeV,
    a2_fold, a0_fold, a4_fold, S_fold,
    PI, g0_diag, Vol_SU3_Haar
)

# =============================================================================
# Section 1: Load upstream data
# =============================================================================
print("=" * 70)
print("GRAV-BACKREACT-63 v2: Gaudin Algebra Integrability Breaking")
print("=" * 70)

data_dir = os.path.dirname(os.path.abspath(__file__))

# S60 R-G integrals: energies and pairing
rg_data = np.load(os.path.join(data_dir, 's60_rg_integrals.npz'), allow_pickle=True)
eps_fold = rg_data['eps_fold']         # 8 single-particle energies at fold
g_eff = float(rg_data['g_eff'])        # rank-1 coupling
u_vec = rg_data['u_vec']              # 8-component pairing amplitude

# S52 HFB
hfb_data = np.load(os.path.join(data_dir, 's52_hfb_full.npz'), allow_pickle=True)
labels = hfb_data['labels']

# S62 GGE
gge_data = np.load(os.path.join(data_dir, 's62_meissner_gge.npz'), allow_pickle=True)
n_k_GGE = gge_data['n_k_GGE']

N_modes = len(eps_fold)
print(f"\nN_modes = {N_modes}")
print(f"eps_fold = {eps_fold}")
print(f"labels = {list(labels)}")
print(f"g_eff = {g_eff:.6f}")

# =============================================================================
# Section 2: Build Hilbert Space (N_pair = 4, half-filling)
# =============================================================================
N_pair = 4  # Physical: 4 pairs in 8 modes (local)
basis = list(combinations(range(N_modes), N_pair))
dim = len(basis)
basis_dict = {state: idx for idx, state in enumerate(basis)}
print(f"\nHilbert space: N_pair={N_pair}, dim={dim}")

# =============================================================================
# Section 3: Gaudin XXX Conserved Charges
# =============================================================================
print("\n" + "=" * 70)
print("Section 3: Gaudin XXX Conserved Charges")
print("=" * 70)


def build_gaudin_charges(eps, g_val, basis, basis_dict, dim, N):
    """
    Build XXX Gaudin conserved charges in the N_pair sector.

    R_k = s_k^z + g * sum_{l!=k} (s_k . s_l) / (eps_k - eps_l)

    where s_k . s_l = (1/2)(s_k^+ s_l^- + s_l^+ s_k^-) + s_k^z s_l^z

    These satisfy [R_k, R_l] = 0 for all k, l (Gaudin 1976).
    """
    charges = []

    for kc in range(N):
        R = np.zeros((dim, dim))

        for i, state in enumerate(basis):
            nk = 1 if kc in state else 0
            sz_k = nk - 0.5

            # s_k^z
            R[i, i] += sz_k

            for ll in range(N):
                if ll == kc:
                    continue
                d = eps[kc] - eps[ll]
                if abs(d) < 1e-15:
                    continue

                nl = 1 if ll in state else 0
                sz_l = nl - 0.5

                # s_k^z s_l^z / (eps_k - eps_l)
                R[i, i] += g_val * sz_k * sz_l / d

                # (1/2) * s_k^+ s_l^- / (eps_k - eps_l)
                # pair transfer: destroy pair at l, create at k
                if ll in state and kc not in state:
                    ns = list(state)
                    ns[ns.index(ll)] = kc
                    ns = tuple(sorted(ns))
                    if ns in basis_dict:
                        j = basis_dict[ns]
                        R[j, i] += g_val / (2.0 * d)

                # (1/2) * s_l^+ s_k^- / (eps_k - eps_l)
                # pair transfer: destroy pair at k, create at l
                if kc in state and ll not in state:
                    ns = list(state)
                    ns[ns.index(kc)] = ll
                    ns = tuple(sorted(ns))
                    if ns in basis_dict:
                        j = basis_dict[ns]
                        R[j, i] += g_val / (2.0 * d)

        charges.append(R)

    return charges


# Build charges with original energies
charges_0 = build_gaudin_charges(eps_fold, g_eff, basis, basis_dict, dim, N_modes)

# Verify mutual commutation
print("\nMutual commutation [R_k, R_l] (original):")
max_comm_0 = 0.0
for k in range(N_modes):
    for ll in range(k + 1, N_modes):
        comm = charges_0[k] @ charges_0[ll] - charges_0[ll] @ charges_0[k]
        n = np.linalg.norm(comm)
        max_comm_0 = max(max_comm_0, n)
print(f"  max ||[R_k, R_l]|| = {max_comm_0:.6e}")

# Build Gaudin Hamiltonian
H_G_0 = sum(eps_fold[k] * charges_0[k] for k in range(N_modes))

# Verify [H_G, R_k] = 0
print("\n[H_Gaudin, R_k]:")
for k in range(N_modes):
    comm = H_G_0 @ charges_0[k] - charges_0[k] @ H_G_0
    print(f"  k={k}: {np.linalg.norm(comm):.6e}")

# Charge eigenvalues
print("\nCharge eigenvalues:")
for k in range(N_modes):
    evals = np.sort(eigvalsh(charges_0[k]))
    print(f"  R_{k}: {evals}")

# =============================================================================
# Section 4: Gravitational Backreaction Corrections
# =============================================================================
print("\n" + "=" * 70)
print("Section 4: Gravitational Backreaction")
print("=" * 70)

alpha_G = (M_KK_gravity / M_Pl_reduced)**2
print(f"alpha_G = (M_KK/M_Pl)^2 = {alpha_G:.6e}")

# SU(3) Casimir for each mode
C2_modes = np.array([3.0, 3.0, 3.0, 3.0,  # B2: adjoint, C2=3
                     0.0,                     # B1: singlet, C2=0
                     4.0/3.0, 4.0/3.0, 4.0/3.0])  # B3: fundamental, C2=4/3

# O(G_N): EIH self-energy
f_grav = eps_fold**2 * (1.0 + C2_modes / 3.0)
delta_eps_1 = -0.5 * alpha_G * f_grav

# O(G_N^2): Virtual graviton exchange
# Labels for sector matching
label_str = [str(l) for l in labels]
V_grav = np.zeros((N_modes, N_modes))
for k in range(N_modes):
    for ll in range(N_modes):
        # Same-sector overlap stronger
        if label_str[k][:2] == label_str[ll][:2]:
            overlap = 1.0  # (local)
        else:
            overlap = 0.3  # (local)
        V_grav[k, ll] = -alpha_G * eps_fold[k] * eps_fold[ll] * overlap

delta_eps_2 = np.zeros(N_modes)
for k in range(N_modes):
    for ll in range(N_modes):
        if ll == k:
            continue
        d = eps_fold[k] - eps_fold[ll]
        if abs(d) < 1e-15:
            continue
        delta_eps_2[k] += V_grav[k, ll]**2 / d

delta_eps_total = delta_eps_1 + delta_eps_2
eps_corr = eps_fold + delta_eps_total

print("\nEnergy corrections:")
for k in range(N_modes):
    rel = delta_eps_total[k] / eps_fold[k] if abs(eps_fold[k]) > 1e-15 else 0.0
    print(f"  k={k} ({labels[k]:>5s}): delta_eps = {delta_eps_total[k]:.6e}, "
          f"rel = {rel:.6e}")

# =============================================================================
# Section 5: R-G Charge Shifts
# =============================================================================
print("\n" + "=" * 70)
print("Section 5: Gaudin Charge Shifts")
print("=" * 70)

# Build charges with corrected energies
charges_corr = build_gaudin_charges(eps_corr, g_eff, basis, basis_dict, dim, N_modes)

# Verify corrected charges still commute
max_comm_c = 0.0
for k in range(N_modes):
    for ll in range(k + 1, N_modes):
        comm = charges_corr[k] @ charges_corr[ll] - charges_corr[ll] @ charges_corr[k]
        n = np.linalg.norm(comm)
        max_comm_c = max(max_comm_c, n)
print(f"Corrected mutual commutation: max ||[R_k, R_l]|| = {max_comm_c:.6e}")

# Method 1: Matrix norm shift
print("\nMethod 1: Matrix norm ||R_k(corr) - R_k(orig)|| / ||R_k(orig)||")
charge_shifts_rel = []
charge_shifts_abs = []
for k in range(N_modes):
    diff = charges_corr[k] - charges_0[k]
    abs_shift = np.linalg.norm(diff, 'fro')
    norm_0 = np.linalg.norm(charges_0[k], 'fro')
    rel = abs_shift / norm_0 if norm_0 > 0 else 0.0
    charge_shifts_abs.append(abs_shift)
    charge_shifts_rel.append(rel)
    print(f"  R_{k}: ||dR||={abs_shift:.6e}, ||R0||={norm_0:.4f}, "
          f"rel={rel:.6e} ({rel*100:.4e}%)")

max_matrix_shift = max(charge_shifts_rel)
print(f"\n  Max relative shift: {max_matrix_shift:.6e} ({max_matrix_shift*100:.4e}%)")

# Method 2: Eigenvalue shifts
print("\nMethod 2: Eigenvalue shifts")
eval_shifts_all = []
for k in range(N_modes):
    e0 = np.sort(eigvalsh(charges_0[k]))
    ec = np.sort(eigvalsh(charges_corr[k]))
    de = ec - e0
    re = np.abs(de) / (np.abs(e0) + 1e-30)
    mx_re = np.max(re)
    eval_shifts_all.append(mx_re)
    print(f"  R_{k}: max |delta_lambda/lambda| = {mx_re:.6e}")

max_eval_shift = max(eval_shifts_all)
print(f"\n  Max eigenvalue shift: {max_eval_shift:.6e} ({max_eval_shift*100:.4e}%)")

# Method 3: Cross-commutator [H_G(corrected), R_k(original)]
print("\nMethod 3: Cross-commutator [H_G(corr), R_k(orig)]")
H_G_corr = sum(eps_corr[k] * charges_corr[k] for k in range(N_modes))
H_scale = np.linalg.norm(H_G_0, 'fro')
cross_comms = []
for k in range(N_modes):
    comm = H_G_corr @ charges_0[k] - charges_0[k] @ H_G_corr
    n = np.linalg.norm(comm)
    rel = n / H_scale
    cross_comms.append(rel)
    print(f"  k={k}: ||[H_corr, R_k]|| = {n:.6e}, relative = {rel:.6e}")

max_cross = max(cross_comms)
print(f"\n  Max relative cross-commutator: {max_cross:.6e}")

# Method 4: GGE expectation value shifts
print("\nMethod 4: GGE expectation value shifts")
# GGE in N_pair sector: product state P(state) ~ prod n_k (occupied) * (1-n_k) (empty)
P_state = np.zeros(dim)
for i, state in enumerate(basis):
    p = 1.0  # (local)
    for m in range(N_modes):
        if m in state:
            p *= n_k_GGE[m]
        else:
            p *= (1.0 - n_k_GGE[m])
    P_state[i] = p
P_state /= P_state.sum()

gge_shifts = []
for k in range(N_modes):
    r0_diag = np.diag(charges_0[k])
    rc_diag = np.diag(charges_corr[k])
    exp_0 = np.dot(P_state, r0_diag)
    exp_c = np.dot(P_state, rc_diag)
    de = exp_c - exp_0
    rel = abs(de) / (abs(exp_0) + 1e-30)
    gge_shifts.append(rel)
    print(f"  k={k}: <R_k>_0={exp_0:.6e}, <R_k>_c={exp_c:.6e}, "
          f"shift={de:.6e}, rel={rel:.6e}")

max_gge = max(gge_shifts)
print(f"\n  Max GGE shift: {max_gge:.6e} ({max_gge*100:.4e}%)")

# Method 5: Gaudin determinant
print("\nMethod 5: Gaudin determinant")


def gaudin_determinant(eps, g_val):
    N2 = len(eps)
    G = np.zeros((N2, N2))
    for k in range(N2):
        for ll in range(N2):
            if k != ll:
                d2 = (eps[k] - eps[ll])**2
                if d2 > 1e-30:
                    G[k, ll] = 2.0 * g_val / d2
                    G[k, k] -= 2.0 * g_val / d2
    return G, np.linalg.det(G)


G_mat_0, det_0 = gaudin_determinant(eps_fold, g_eff)
G_mat_c, det_c = gaudin_determinant(eps_corr, g_eff)
det_shift = abs(det_c - det_0) / (abs(det_0) + 1e-30)
print(f"  det(G)_orig = {det_0:.6e}")
print(f"  det(G)_corr = {det_c:.6e}")
print(f"  Relative shift: {det_shift:.6e} ({det_shift*100:.4e}%)")

G_evals_0 = np.sort(eigvalsh(G_mat_0))
G_evals_c = np.sort(eigvalsh(G_mat_c))
G_eval_shifts = np.abs(G_evals_c - G_evals_0) / (np.abs(G_evals_0) + 1e-30)
print(f"\n  Gaudin matrix eigenvalue shifts:")
for k in range(N_modes):
    print(f"    lambda_{k}: {G_evals_0[k]:.6e} -> {G_evals_c[k]:.6e}, "
          f"rel = {G_eval_shifts[k]:.6e}")

# =============================================================================
# Section 6: Timescale Analysis
# =============================================================================
print("\n" + "=" * 70)
print("Section 6: Integrability Breaking Timescale")
print("=" * 70)

# The cross-commutator ||[H(corr), R_k(orig)]|| / ||H|| gives the
# fractional rate of charge non-conservation per dynamical timescale.
# The dynamical timescale is 1/||H|| in natural units.
# Physical breaking rate: Gamma ~ ||[H,R]||

# In M_KK units, the breaking rate per H oscillation is max_cross
# Physical rate in s^{-1}:
H_G_norm = np.linalg.norm(H_G_0, 'fro')
Gamma_break_MKK = max(cross_comms) * H_G_norm  # Rate in M_KK
Gamma_break_GeV = Gamma_break_MKK * M_KK
Gamma_break_inv_s = Gamma_break_GeV / hbar_GeV_s if Gamma_break_GeV > 0 else 0.0

print(f"Breaking rate:")
print(f"  Gamma_break = {Gamma_break_MKK:.6e} M_KK")
print(f"  Gamma_break = {Gamma_break_GeV:.4e} GeV")
print(f"  Gamma_break = {Gamma_break_inv_s:.4e} s^{{-1}}")
print(f"  H_0 = {H_0_inv_s:.4e} s^{{-1}}")
if Gamma_break_inv_s > 0:
    print(f"  Gamma/H_0 = {Gamma_break_inv_s / H_0_inv_s:.4e}")
    t_break = 1.0 / Gamma_break_inv_s
    print(f"  t_break = {t_break:.4e} s = {t_break / t_universe_s:.4e} t_universe")

# Non-perturbative effects
print(f"\nNon-perturbative gravitational effects:")
print(f"  Instantons: exp(-M_Pl^2/M_KK^2) = exp(-{(M_Pl_reduced/M_KK)**2:.0f}) ~ 0")
print(f"  Cosmological: (H_0/M_KK)^2 = {(H_0_GeV/M_KK)**2:.6e}")

# =============================================================================
# Section 7: Gate Verdict
# =============================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: GRAV-BACKREACT-63")
print("=" * 70)

overall_max_pct = max(max_matrix_shift, max_eval_shift, det_shift, max_gge) * 100

print(f"\nMaximum shifts (%):")
print(f"  Matrix norm:        {max_matrix_shift*100:.4e}%")
print(f"  Eigenvalue:         {max_eval_shift*100:.4e}%")
print(f"  Gaudin determinant: {det_shift*100:.4e}%")
print(f"  GGE expectation:    {max_gge*100:.4e}%")
print(f"  Cross-commutator:   {max_cross*100:.4e}%")
print(f"  Overall max:        {overall_max_pct:.4e}%")
print(f"  alpha_G:            {alpha_G:.6e}")

if overall_max_pct > 1.0:
    verdict = "PASS"
    detail = (f"R-G charge shift {overall_max_pct:.4e}% > 1%. "
              f"Gravity breaks Gaudin integrability at O(alpha_G) = O({alpha_G:.1e}). "
              f"Controlled by (M_KK/M_Pl)^2.")
elif overall_max_pct < 0.1:
    verdict = "FAIL"
    detail = (f"All shifts < 0.1% (max = {overall_max_pct:.4e}%). "
              f"Gaudin charges robust to gravitational backreaction at O(G_N^2). "
              f"alpha_G = {alpha_G:.2e}.")
else:
    verdict = "INFO"
    detail = (f"Shifts between 0.1% and 1% (max = {overall_max_pct:.4e}%). "
              f"Gravitational breaking present but marginal. "
              f"alpha_G = {alpha_G:.2e}.")

print(f"\nVerdict: {verdict}")
print(f"Detail: {detail}")

# =============================================================================
# Section 8: Save Data
# =============================================================================
save_path = os.path.join(data_dir, 's63_grav_backreact.npz')
np.savez(save_path,
         # Gate
         gate_name='GRAV-BACKREACT-63',
         gate_verdict=verdict,
         gate_detail=detail,
         # Input
         eps_fold=eps_fold,
         eps_corrected=eps_corr,
         labels=labels,
         n_k_GGE=n_k_GGE,
         alpha_G=alpha_G,
         g_eff=g_eff,
         C2_modes=C2_modes,
         N_pair=N_pair,
         dim=dim,
         # Energy corrections
         delta_eps_1=delta_eps_1,
         delta_eps_2=delta_eps_2,
         delta_eps_total=delta_eps_total,
         # Charge shifts
         charge_shifts_rel=np.array(charge_shifts_rel),
         charge_shifts_abs=np.array(charge_shifts_abs),
         eval_shifts=np.array(eval_shifts_all),
         gge_shifts=np.array(gge_shifts),
         cross_comms=np.array(cross_comms),
         # Gaudin
         det_G_0=det_0,
         det_G_c=det_c,
         det_shift=det_shift,
         G_evals_0=G_evals_0,
         G_evals_c=G_evals_c,
         # Commutation
         max_mutual_0=max_comm_0,
         max_mutual_c=max_comm_c,
         # Timescales
         Gamma_break_MKK=Gamma_break_MKK,
         max_matrix_shift=max_matrix_shift,
         max_eval_shift=max_eval_shift,
         max_gge_shift=max_gge,
         max_cross_comm=max_cross,
         overall_max_pct=overall_max_pct,
         )

print(f"\nSaved: {save_path}")

# =============================================================================
# Section 9: Plot
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

x = np.arange(N_modes)

# Panel 1: Energy corrections by mode
ax = axes[0, 0]
width = 0.35  # (local)
mask1 = np.abs(delta_eps_1) > 0
mask2 = np.abs(delta_eps_2) > 0
ax.bar(x[mask1] - width/2, np.abs(delta_eps_1[mask1]), width,
       label=r'$O(G_N)$', color='steelblue')
ax.bar(x[mask2] + width/2, np.abs(delta_eps_2[mask2]), width,
       label=r'$O(G_N^2)$', color='coral')
ax.set_yscale('log')
ax.set_xlabel('Mode index k')
ax.set_ylabel(r'$|\delta\varepsilon_k|$ (M$_{KK}$)')
ax.set_title('Gravitational Energy Corrections')
ax.set_xticks(x)
ax.set_xticklabels([str(l) for l in labels], rotation=45, fontsize=8)
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Charge shifts (all methods)
ax = axes[0, 1]
methods = ['Matrix', 'Eigenval', 'GGE', 'Cross-comm']
values = [max_matrix_shift*100, max_eval_shift*100, max_gge*100, max_cross*100]
colors = ['darkgreen', 'steelblue', 'coral', 'purple']
ax.barh(methods, values, color=colors)
ax.axvline(x=1.0, color='red', linestyle='--', label='1% threshold')
ax.axvline(x=0.1, color='orange', linestyle='--', label='0.1% threshold')
ax.set_xlabel('Maximum shift (%)')
ax.set_title('R-G Charge Shift by Method')
ax.set_xscale('log')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='x')

# Panel 3: Per-charge shifts
ax = axes[1, 0]
ax.bar(x - 0.2, charge_shifts_rel, 0.4, label='Matrix norm', color='darkgreen')
ax.bar(x + 0.2, eval_shifts_all, 0.4, label='Eigenvalue', color='steelblue')
ax.axhline(y=0.01, color='red', linestyle='--', alpha=0.5, label='1%')
ax.axhline(y=0.001, color='orange', linestyle='--', alpha=0.5, label='0.1%')
ax.set_yscale('log')
ax.set_xlabel('Charge index k')
ax.set_ylabel('Relative shift')
ax.set_title('Per-Charge Shifts')
ax.set_xticks(x)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Gaudin matrix eigenvalues
ax = axes[1, 1]
ax.plot(x, G_evals_0, 'bo-', label='Original', markersize=6)
ax.plot(x, G_evals_c, 'rs--', label='Corrected', markersize=6)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Gaudin eigenvalue')
ax.set_title('Gaudin Matrix Spectrum')
ax.legend()
ax.grid(True, alpha=0.3)

plt.suptitle(f'GRAV-BACKREACT-63: Gravitational Integrability Breaking\n'
             f'Verdict: {verdict} | Max shift: {overall_max_pct:.2e}% | '
             fr'$\alpha_G = {alpha_G:.2e}$',
             fontsize=12)
plt.tight_layout()

plot_path = os.path.join(data_dir, 's63_grav_backreact.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved plot: {plot_path}")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
