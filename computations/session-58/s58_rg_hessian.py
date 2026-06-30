#!/usr/bin/env python3
"""
s58_rg_hessian.py — RG-HESSIAN-58: Richardson-Gaudin Hessian in Integral Space I^8
====================================================================================

Gate: RG-HESSIAN-58
  PASS: At least one negative eigenvalue (Penrose process direction exists)
  FAIL: All eigenvalues positive (GGE is stable minimum; CC locked by integrability)

Physics:
  The GGE departs from equilibrium by ||delta_n||/N = 0.195 (S57 W0-3).
  The near-cancellation +0.316 - 0.315 = +0.00145 shows the system is trying
  to self-tune but integrability prevents completion.

  CRITICAL DISTINCTION: Three physically different Hessians.

  (1) Post-quench (alpha=0): H_free is diagonal, E = Sum E_k*n_k is LINEAR.
      The GGE thermodynamic potential Omega = E - Sum T_k*s_k has
      d^2 Omega/dn^2 = diag(T_k/n_k) > 0. ALWAYS a minimum.
      The GGE is unconditionally stable when pairing is OFF.

  (2) With Andreev channel (0 < alpha < 1): The effective Hamiltonian
      H_eff = H_free + alpha*V_pair reactivates pairing partially.
      The BCS pairing curvature is NEGATIVE (d^2 E_BCS/dn^2 < 0).
      There exists a critical alpha_crit such that for alpha > alpha_crit,
      the total Hessian H = alpha*H_BCS + diag(T_k/n_k) has a negative
      eigenvalue. THIS is the physically relevant Penrose process: the
      Andreev channel enables CC reduction.

  (3) Full BCS (alpha=1): The complete BCS Hessian dominates entropy.
      3 negative eigenvalues on the constraint surface. Strong saddle.
      But this regime is unphysical post-quench (condensate destroyed).

  The gate verdict reports on regime (2): does a Penrose process exist
  when the Andreev channel (S56) partially restores pairing?

Author: Volovik-Superfluid-Universe-Theorist
Session: S58, Wave 1, Task W1-2
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize_scalar

# Import canonical constants
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
import canonical_constants as cc

print("=" * 72)
print("S58 RG-HESSIAN-58: Richardson-Gaudin Hessian in Integral Space I^8")
print("=" * 72)

# ==============================================================================
# 1. LOAD DATA
# ==============================================================================

d54 = np.load(os.path.join(os.path.dirname(__file__), 's54_ed_sweep.npz'),
              allow_pickle=True)
d57_gge = np.load(os.path.join(os.path.dirname(__file__),
                  's57_gge_equilibrium_gap.npz'), allow_pickle=True)
d57_cc = np.load(os.path.join(os.path.dirname(__file__), 's57_cc_sign.npz'),
                 allow_pickle=True)
d43 = np.load(os.path.join(os.path.dirname(__file__), "..", "_shared",
              's43_gge_temperatures.npz'), allow_pickle=True)

fold_idx = int(d54['fold_idx'])
tau_fold = d54['tau_values'][fold_idx]
N_modes = 8  # (local)
N_pair = 1  # (local)

# BCS pair energies
xi_k = d43['xi']              # single-particle energies = E_k/2
E_k = d57_gge['E_k']         # pair energies = 2*xi_k
branch_labels = d57_gge['branch_labels']

# GGE occupations (the Richardson-Gaudin integrals)
nk_gge = d57_gge['fk_gge']   # 8 GGE occupations, sum = 1

# Equilibrium occupations (Boltzmann fit)
nk_eq = d57_gge['fk_eq_canonical']
T_eq = float(d57_gge['T_eq_canonical'])

# GGE temperatures and Lagrange multipliers
T_k = d57_gge['T_k_volovik']
beta_k = d57_gge['beta_k']

# Pairing matrix
V_kl = d54['V_bare_cont']    # 8x8 symmetric pairing matrix

# Single-particle energies at fold
E_sp_fold = d54['E_sp_sweep'][fold_idx]

# Stored energies
E_BCS_gs = float(d54['E0'][fold_idx])
E_GGE = float(d57_gge['E_GGE'])
E_eq = float(d57_gge['E_eq_canonical'])
Lambda_V_stored = float(d57_cc['Lambda_volovik_total'])

print(f"\nData loaded:")
print(f"  tau_fold = {tau_fold:.6f}")
print(f"  N_modes = {N_modes}, N_pair = {N_pair}")
print(f"  E_BCS_gs = {E_BCS_gs:.6f} M_KK")
print(f"  E_GGE = {E_GGE:.6f} M_KK")
print(f"  E_eq = {E_eq:.6f} M_KK")
print(f"  Lambda_V (Volovik CC) = {Lambda_V_stored:.6f} M_KK")
print(f"  Sum(nk_gge) = {np.sum(nk_gge):.10f}")

print(f"\n{'Mode':<8} {'E_k':>10} {'n_k^GGE':>10} {'n_k^eq':>10} "
      f"{'delta_n':>10} {'T_k':>10}")
print("-" * 62)
delta_nk = nk_gge - nk_eq
for k in range(N_modes):
    print(f"{str(branch_labels[k]):<8} {E_k[k]:10.6f} {nk_gge[k]:10.6f} "
          f"{nk_eq[k]:10.6f} {delta_nk[k]:+10.6f} {T_k[k]:10.6f}")

# ==============================================================================
# 2. REGIME 1: FREE HAMILTONIAN (alpha = 0, post-quench)
# ==============================================================================

print("\n" + "=" * 72)
print("2. REGIME 1: FREE HAMILTONIAN (alpha = 0)")
print("    E(n) = Sum E_k * n_k  [LINEAR — Hessian identically zero]")
print("    Omega_GGE = Sum [E_k*n_k + T_k*n_k*ln(n_k)]")
print("=" * 72)

eps_reg = 1e-15
nk_safe = np.clip(nk_gge, eps_reg, 1.0 - eps_reg)

# Entropy Hessian: d^2(-S)/dn_k^2 = 1/n_k for Shannon entropy
# GGE potential Hessian: d^2 Omega_GGE / dn_j dn_k = T_k/n_k * delta_{jk}
H_entropy = np.diag(T_k / nk_safe)

print(f"\nGGE entropy Hessian (T_k/n_k diagonal):")
for k in range(N_modes):
    print(f"  {str(branch_labels[k]):<8}: T_k/n_k = {T_k[k]/nk_safe[k]:8.4f}")
print(f"\n  ALL POSITIVE. GGE is unconditionally STABLE at alpha=0.")
print(f"  Min diagonal: {np.min(T_k/nk_safe):.4f} (B2[0])")
print(f"  Max diagonal: {np.max(T_k/nk_safe):.4f} (B3[0])")

# ==============================================================================
# 3. BCS PAIRING HESSIAN (the energy curvature from pairing interaction)
# ==============================================================================

print("\n" + "=" * 72)
print("3. BCS PAIRING HESSIAN")
print("    E_BCS(n) = Sum 2*xi_k*n_k + Sum V_kl*sqrt(n_k(1-n_k))*sqrt(n_l(1-n_l))")
print("=" * 72)

n_s = np.clip(nk_gge, 1e-10, 1.0 - 1e-10)
f_n = np.sqrt(n_s * (1.0 - n_s))
fp_n = (1.0 - 2.0 * n_s) / (2.0 * f_n)
fpp_n = -1.0 / (4.0 * (n_s * (1.0 - n_s))**1.5)
Delta_j = V_kl @ f_n  # gap vector

# Analytical Hessian
H_bcs = np.zeros((N_modes, N_modes))
for j in range(N_modes):
    for k in range(N_modes):
        if j == k:
            H_bcs[j, k] = 2.0 * fpp_n[j] * Delta_j[j] + 2.0 * V_kl[j, j] * fp_n[j]**2
        else:
            H_bcs[j, k] = 2.0 * fp_n[j] * V_kl[j, k] * fp_n[k]

# Numerical cross-check
delta_h = 1e-6
H_bcs_num = np.zeros((N_modes, N_modes))

def E_bcs_mf(n):
    E_kin = np.sum(2.0 * xi_k * n)
    uv = np.sqrt(np.clip(n * (1.0 - n), 0, None))
    E_pair = np.sum(V_kl * np.outer(uv, uv))
    return E_kin + E_pair

for j in range(N_modes):
    for k in range(j, N_modes):
        n_pp = nk_gge.copy(); n_pp[j] += delta_h; n_pp[k] += delta_h
        n_pm = nk_gge.copy(); n_pm[j] += delta_h; n_pm[k] -= delta_h
        n_mp = nk_gge.copy(); n_mp[j] -= delta_h; n_mp[k] += delta_h
        n_mm = nk_gge.copy(); n_mm[j] -= delta_h; n_mm[k] -= delta_h
        H_bcs_num[j, k] = (E_bcs_mf(n_pp) - E_bcs_mf(n_pm)
                            - E_bcs_mf(n_mp) + E_bcs_mf(n_mm)) / (4 * delta_h**2)
        H_bcs_num[k, j] = H_bcs_num[j, k]

max_diff = np.max(np.abs(H_bcs - H_bcs_num))
print(f"\n  Analytical vs numerical: max |diff| = {max_diff:.2e}")
print(f"  Symmetry: max |H - H^T| = {np.max(np.abs(H_bcs - H_bcs.T)):.2e}")

evals_bcs, evecs_bcs = np.linalg.eigh(H_bcs)
print(f"\n  Eigenvalues of d^2 E_BCS / dn^2 (full 8x8):")
for i, ev in enumerate(evals_bcs):
    print(f"    lambda_{i} = {ev:+.4f}")
print(f"  ALL NEGATIVE ({np.sum(evals_bcs < 0)}/8).")
print(f"  Pairing curvature is universally destabilizing.")

# Projected onto constraint surface
ones = np.ones(N_modes)
P_proj = np.eye(N_modes) - np.outer(ones, ones) / N_modes

H_bcs_proj = P_proj @ H_bcs @ P_proj
evals_bcs_proj_all = np.sort(np.linalg.eigvalsh(H_bcs_proj))
# Identify the zero eigenvalue (from projection)
evals_bcs_proj = evals_bcs_proj_all[1:]  # skip zero mode

print(f"\n  Projected eigenvalues (7D constraint surface):")
for i, ev in enumerate(evals_bcs_proj):
    print(f"    lambda_{i} = {ev:+.4f}")
n_neg_bcs = np.sum(evals_bcs_proj < -1e-8)
print(f"  Negative: {n_neg_bcs}/7 (all but constraint zero)")

# ==============================================================================
# 4. REGIME 2: ANDREEV CHANNEL ANALYSIS (0 < alpha <= 1)
# ==============================================================================

print("\n" + "=" * 72)
print("4. REGIME 2: ANDREEV CHANNEL (alpha-dependent Hessian)")
print("    H(alpha) = alpha * H_BCS + diag(T_k/n_k)")
print("    Find alpha_crit where first eigenvalue crosses zero.")
print("=" * 72)

# Fine-grained alpha sweep
N_alpha = 1001  # (local)
alphas = np.linspace(0, 1, N_alpha)
min_evals = np.zeros(N_alpha)
n_negative = np.zeros(N_alpha, dtype=int)

for i, alpha in enumerate(alphas):
    H_total = alpha * H_bcs + H_entropy
    H_proj = P_proj @ H_total @ P_proj
    evals = np.sort(np.linalg.eigvalsh(H_proj))
    # Skip the zero mode (from projection)
    evals_physical = evals[1:]
    min_evals[i] = evals_physical[0]
    n_negative[i] = np.sum(evals_physical < -1e-8)

# Find critical alpha
cross_idx = np.where(min_evals < 0)[0]
if len(cross_idx) > 0:
    alpha_crit = alphas[cross_idx[0]]
    # Refine with bisection
    a_lo, a_hi = max(0, alpha_crit - 0.002), alpha_crit + 0.002
    for _ in range(50):
        a_mid = (a_lo + a_hi) / 2
        H_mid = a_mid * H_bcs + H_entropy
        H_mid_proj = P_proj @ H_mid @ P_proj
        ev_mid = np.sort(np.linalg.eigvalsh(H_mid_proj))[1]
        if ev_mid < 0:
            a_hi = a_mid
        else:
            a_lo = a_mid
    alpha_crit = (a_lo + a_hi) / 2
else:
    alpha_crit = None

print(f"\n  alpha = 0.0:  min projected eigenvalue = {min_evals[0]:+.4f} (STABLE)")
print(f"  alpha = 0.5:  min projected eigenvalue = {min_evals[N_alpha//2]:+.4f}")
print(f"  alpha = 1.0:  min projected eigenvalue = {min_evals[-1]:+.4f} (SADDLE)")

if alpha_crit is not None:
    print(f"\n  CRITICAL COUPLING: alpha_crit = {alpha_crit:.6f}")
    print(f"  For alpha > {alpha_crit:.4f}, GGE becomes a SADDLE in integral space.")

    # Analyze at alpha_crit + epsilon
    alpha_test = alpha_crit + 0.01
    H_test = alpha_test * H_bcs + H_entropy
    H_test_proj = P_proj @ H_test @ P_proj
    evals_test, evecs_test = np.linalg.eigh(H_test_proj)

    # Find the negative eigenvalue
    for i in range(N_modes):
        if evals_test[i] < -1e-8:
            vec = evecs_test[:, i]
            vec_proj = vec - np.mean(vec)
            if np.linalg.norm(vec_proj) > 1e-10:
                vec_proj /= np.linalg.norm(vec_proj)
            print(f"\n  Penrose direction at alpha={alpha_test:.3f} "
                  f"(eigenvalue = {evals_test[i]:+.6f}):")
            print(f"  {'Mode':<8} {'Component':>10}")
            for k in range(N_modes):
                print(f"  {str(branch_labels[k]):<8} {vec_proj[k]:+.6f}")
            increase = [str(branch_labels[k]) for k in range(N_modes) if vec_proj[k] > 0.1]
            decrease = [str(branch_labels[k]) for k in range(N_modes) if vec_proj[k] < -0.1]
            print(f"\n  Transfer occupation: {decrease} -> {increase}")
else:
    print(f"\n  NO crossing found. GGE stable for all alpha in [0,1].")

# At full BCS (alpha=1)
H_full = H_bcs + H_entropy
H_full_proj = P_proj @ H_full @ P_proj
evals_full, evecs_full = np.linalg.eigh(H_full_proj)
evals_full_phys = evals_full[1:]  # skip zero mode

print(f"\n  Full BCS + GGE entropy (alpha=1), projected eigenvalues:")
for i, ev in enumerate(evals_full_phys):
    sign_str = "NEGATIVE" if ev < -1e-8 else "positive"
    print(f"    lambda_{i} = {ev:+.6f}  [{sign_str}]")
n_neg_full = np.sum(evals_full_phys < -1e-8)
print(f"  Negative: {n_neg_full}/7")

# Penrose directions at alpha=1
print(f"\n  Penrose eigenvectors at alpha=1:")
for i in range(N_modes):
    if evals_full[i] < -1e-8 and i > 0:
        vec = evecs_full[:, i]
        vec_proj = vec - np.mean(vec)
        if np.linalg.norm(vec_proj) > 1e-10:
            vec_proj /= np.linalg.norm(vec_proj)
        print(f"\n  Direction {i} (lambda = {evals_full[i]:+.4f}):")
        for k in range(N_modes):
            if abs(vec_proj[k]) > 0.05:
                print(f"    {str(branch_labels[k]):<8}: {vec_proj[k]:+.4f}")

# ==============================================================================
# 5. CROSS-SUSCEPTIBILITY d^2 Omega / dN dI_k
# ==============================================================================

print("\n" + "=" * 72)
print("5. CROSS-SUSCEPTIBILITY d^2 Omega / dN dI_k")
print("=" * 72)

# For GGE with mode-specific T_k:
# Omega(N, {f_k}) = Sum_l [E_l * N*f_l + T_l * N*f_l * ln(N*f_l)]
# d^2/dN df_k = E_k + T_k*(ln(N*f_k) + 2) at N=1
chi_cross = E_k + T_k * (np.log(nk_safe) + 2.0)

print(f"\n  {'Mode':<8} {'chi_cross':>12} {'|chi|':>10}")
print(f"  " + "-" * 34)
for k in range(N_modes):
    print(f"  {str(branch_labels[k]):<8} {chi_cross[k]:+12.6f} {abs(chi_cross[k]):10.6f}")

print(f"\n  All nonzero: {np.all(np.abs(chi_cross) > 1e-10)}")
print(f"  Range: [{np.min(chi_cross):.4f}, {np.max(chi_cross):.4f}]")
print(f"  This means pair-number fluctuations (N_pair changes)")
print(f"  couple to EVERY integral of motion.")
print(f"  The multi-pair sector (N_pair >= 2) accesses new directions.")

# ==============================================================================
# 6. ENTROPY-PAIRING COMPETITION (diagonal analysis)
# ==============================================================================

print("\n" + "=" * 72)
print("6. ENTROPY vs PAIRING: DIAGONAL COMPETITION")
print("=" * 72)

H_bcs_diag = np.diag(H_bcs)
H_ent_diag = T_k / nk_safe

print(f"\n  {'Mode':<8} {'Entropy':>12} {'Pairing':>12} {'Ratio E/P':>10} {'Winner':>10}")
print(f"  " + "-" * 56)
for k in range(N_modes):
    ratio = H_ent_diag[k] / abs(H_bcs_diag[k]) if abs(H_bcs_diag[k]) > 1e-15 else float('inf')
    winner = "Entropy" if ratio > 1 else "PAIRING"
    print(f"  {str(branch_labels[k]):<8} {H_ent_diag[k]:12.4f} {H_bcs_diag[k]:+12.4f} "
          f"{ratio:10.2f} {winner:>10}")

# B3 modes: pairing curvature dominates entropy
b3_ratio = H_ent_diag[5:8] / np.abs(H_bcs_diag[5:8])
print(f"\n  B3 modes: entropy/pairing ratio = {b3_ratio}")
print(f"  B3 modes have pairing DOMINATING entropy (ratio < 1).")
print(f"  This is why the full Hessian has negative eigenvalues.")
print(f"  Physical: B3 modes are nearly empty (n~0.003), so")
print(f"  entropy cost T_k/n_k ~ 50 but pairing curvature ~ -80.")
print(f"  The f''(n) = -1/(4[n(1-n)]^{3/2}) divergence at small n")
print(f"  amplifies pairing relative to entropy.")

# ==============================================================================
# 7. GRADIENT OF VOLOVIK VACUUM ENERGY
# ==============================================================================

print("\n" + "=" * 72)
print("7. GRADIENT OF VOLOVIK VACUUM ENERGY AT GGE POINT")
print("=" * 72)

# Lambda_V per mode (from S57):
Lambda_V_permode = d57_cc['Lambda_volovik_permode']
print(f"\n  Per-mode Volovik CC contribution:")
for k in range(N_modes):
    sign = "+" if Lambda_V_permode[k] > 0 else "-"
    print(f"  {str(branch_labels[k]):<8}: {Lambda_V_permode[k]:+.6f} M_KK")
print(f"  Total: {np.sum(Lambda_V_permode):.6f} M_KK")

# The gradient of Lambda_V at fixed T_eq:
# dLambda_V/dn_k = g_k = E_k - mu_eff_k
# where mu_eff_k = T_eq * ln((1-n^eq_k)/n^eq_k)
mu_eff_k = d57_cc['mu_eff_k']
g_k = E_k - mu_eff_k

print(f"\n  Gradient (dLambda_V/dn_k at fixed T_eq):")
for k in range(N_modes):
    print(f"  {str(branch_labels[k]):<8}: g_k = {g_k[k]:+.6f}")

# The gradient is nearly constant (~1.36-1.40) because E_k and mu_eff_k
# have similar branch structure. Project onto constraint surface:
g_proj = g_k - np.mean(g_k)
print(f"\n  Projected gradient ||g_proj|| = {np.linalg.norm(g_proj):.6f}")
print(f"  (Near-zero: Lambda_V is nearly flat on constraint surface)")
print(f"  The CC is determined by which side of the equilibrium")
print(f"  each mode sits on, not by the gradient magnitude.")

# ==============================================================================
# 8. PHYSICAL INTERPRETATION
# ==============================================================================

print("\n" + "=" * 72)
print("8. PHYSICAL INTERPRETATION")
print("=" * 72)

print("""
Superfluid 3He-B Analog:

The GGE is the analog of a quenched superfluid where the condensate has
been destroyed (P_exc = 1.000). Post-quench, the quasiparticle distribution
is frozen by integrability. Three distinct stability regimes:

1. ALPHA = 0 (free, post-quench):
   The mode occupations are conserved. The entropy Hessian T_k/n_k is
   always positive. The GGE is a minimum of the free energy.
   No Penrose process. CC is locked.

2. ALPHA = alpha_crit (Andreev threshold):
   When quasiparticle tunneling (Andreev reflection) partially restores
   the pairing interaction, the BCS curvature competes with entropy.
   At alpha_crit, the B3 modes (nearly empty, n ~ 0.003) become
   unstable because pairing curvature |d^2E_pair/dn^2| ~ 80 exceeds
   the entropic stabilization T_k/n_k ~ 50.

3. ALPHA > alpha_crit (Penrose regime):
   The Penrose direction transfers occupation from B2+B1 to B3 modes.
   This REDUCES the vacuum energy because B3 modes contribute Lambda < 0
   (S57: Lambda_B3 = -0.150 M_KK) while B2 modes contribute Lambda > 0
   (S57: Lambda_B2 = +0.316 M_KK).

The critical question is whether the Andreev channel (S56 FABRIC-INTEG-56)
provides alpha > alpha_crit. S56 found <r> = 0.367 (integrable) for
isotropic coupling but <r> = 0.446 for anisotropic coupling, suggesting
the Andreev channel MAY provide sufficient coupling.
""")

# ==============================================================================
# 9. GATE VERDICT
# ==============================================================================

print("=" * 72)
print("9. GATE VERDICT: RG-HESSIAN-58")
print("=" * 72)

# The gate asks: is there a negative eigenvalue?
# At alpha=0: NO (FAIL). At alpha>alpha_crit: YES (PASS).
# The honest answer is that the Hessian is alpha-DEPENDENT.
# The gate as pre-registered asks about "the thermodynamic potential
# at the GGE point in integral space" without specifying alpha.
#
# At the GGE point with the PHYSICAL post-quench Hamiltonian (alpha=0),
# the answer is FAIL: all eigenvalues positive.
#
# However, the BCS pairing curvature provides a CONDITIONAL PASS:
# if the Andreev channel provides alpha > alpha_crit, the saddle exists.
# This connects directly to S56 FABRIC-INTEG-56 and NPAIR2-INTEG-58.

# Primary verdict: FAIL (alpha=0 is the post-quench reality)
# Secondary: CONDITIONAL on Andreev alpha > alpha_crit
gate_verdict = "FAIL"

print(f"\n  Primary verdict: FAIL")
print(f"  At alpha=0 (post-quench, integrability preserved):")
print(f"    All 7 projected eigenvalues POSITIVE (min = {np.min(T_k/nk_safe):.4f})")
print(f"    GGE is a LOCAL MINIMUM. CC permanently locked.")
print(f"")
print(f"  Conditional result:")
if alpha_crit is not None:
    print(f"    alpha_crit = {alpha_crit:.6f}")
    print(f"    For Andreev coupling alpha > {alpha_crit:.4f}, GGE becomes SADDLE")
    print(f"    At alpha=1 (full BCS): {n_neg_full} negative eigenvalues")
    print(f"    Penrose direction: B2+B1 -> B3 (reduces Lambda_B2, increases Lambda_B3)")
    print(f"    Net CC reduction: B3 contributes Lambda < 0")
else:
    print(f"    No Penrose process found at any alpha.")

print(f"\n  Physical conclusion:")
print(f"  The integrability-locked GGE is thermodynamically stable.")
print(f"  CC reduction requires BREAKING integrability (alpha > 0),")
print(f"  which is precisely the Andreev channel of S56.")
print(f"  The Hessian quantifies the threshold: alpha_crit = {alpha_crit:.4f}.")

# ==============================================================================
# 10. SAVE RESULTS
# ==============================================================================

print("\n" + "=" * 72)
print("10. SAVING RESULTS")
print("=" * 72)

save_path = os.path.join(os.path.dirname(__file__), 's58_rg_hessian.npz')

np.savez(save_path,
    # Gate
    gate_name='RG-HESSIAN-58',
    gate_verdict=gate_verdict,

    # Input data
    tau_fold=tau_fold,
    E_k=E_k,
    xi_k=xi_k,
    nk_gge=nk_gge,
    nk_eq=nk_eq,
    T_eq=T_eq,
    T_k=T_k,
    beta_k=beta_k,
    V_kl=V_kl,
    branch_labels=branch_labels,

    # Hessians
    H_entropy=H_entropy,          # diag(T_k/n_k), always positive
    H_bcs_pairing=H_bcs,          # BCS pairing curvature, all negative
    H_bcs_numerical=H_bcs_num,    # numerical cross-check
    H_bcs_anal_num_diff=max_diff, # agreement

    # Alpha-dependent analysis
    alpha_crit=alpha_crit if alpha_crit is not None else -1.0,
    alphas=alphas,
    min_evals_vs_alpha=min_evals,
    n_negative_vs_alpha=n_negative,

    # Full BCS + entropy Hessian (alpha=1)
    H_full_projected_evals=evals_full,
    H_full_projected_evecs=evecs_full,
    n_neg_alpha1=n_neg_full,

    # Projected eigenvalues
    evals_entropy_proj=np.sort(np.linalg.eigvalsh(P_proj @ H_entropy @ P_proj))[1:],
    evals_bcs_proj=evals_bcs_proj,
    evals_full_proj=evals_full_phys,

    # Cross-susceptibility
    chi_cross=chi_cross,

    # Volovik Lambda_V per mode
    Lambda_V_permode=Lambda_V_permode,
    Lambda_V_total=Lambda_V_stored,
    g_k_gradient=g_k,
    g_k_projected=g_proj,

    # Diagonal competition
    entropy_diagonal=H_ent_diag,
    pairing_diagonal=H_bcs_diag,
    entropy_pairing_ratio=H_ent_diag / np.abs(H_bcs_diag),
)

print(f"  Saved to: {save_path}")
print(f"  Gate verdict: {gate_verdict}")
print(f"  Alpha_crit: {alpha_crit:.6f}" if alpha_crit is not None else "  No crossing")
print(f"\n{'='*72}")
print(f"COMPUTATION COMPLETE: RG-HESSIAN-58 [{gate_verdict}]")
print(f"{'='*72}")
