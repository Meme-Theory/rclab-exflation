"""
s44_jacobson_spec.py — JACOBSON-SPEC-44
Jacobson mapping for the GGE relic: gravitating energy density from
delta Q = sum_k T_k dS_k on local Rindler horizons.

Gate: JACOBSON-SPEC-44
  PASS: rho_Jacobson within 30 OOM of Lambda_obs
  FAIL: rho_Jacobson > 10^60 * Lambda_obs

Physics:
  Jacobson (1995) derived G_mu_nu = 8piG T_mu_nu from delta Q = T dS
  on every local Rindler horizon. For a GGE with 8 conserved charges,
  the first law generalizes to delta Q = sum_k T_k dS_k.

  The gravitating energy density = internal energy E_GGE per unit volume
  (this IS what Jacobson's T_{ab} k^a k^b gives for a stationary state).

  Key insight: the Jacobson approach replaces the spectral action functional
  (polynomial in eigenvalues) with the GGE thermodynamic energy (set by
  occupation numbers * quasiparticle energies). This is a DIFFERENT functional
  and can give a different CC contribution.

  Normalization: E_GGE = 2 * sum_k E_k n_k (pair energy, factor 2 for BCS).
  S_GGE = -sum_k n_k ln(n_k) (Shannon entropy of occupation distribution).
"""

import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

# ═══════════════════════════════════════════════════════════════
# 1. LOAD ALL INPUT DATA
# ═══════════════════════════════════════════════════════════════

data_dir = Path(__file__).parent

gge = np.load(data_dir / 's43_gge_temperatures.npz', allow_pickle=True)
gsl = np.load(data_dir / 's43_gsl_transit.npz', allow_pickle=True)
fl  = np.load(data_dir / 's43_first_law.npz', allow_pickle=True)
cs  = np.load(data_dir / 's42_constants_snapshot.npz', allow_pickle=True)
eih = np.load(data_dir / 's44_eih_grav.npz', allow_pickle=True)

# Load Sakharov audit for corrected G_N
try:
    sak_audit = np.load(data_dir / 's44_sakharov_gn_audit.npz', allow_pickle=True)
    inv_16piG_sakharov = float(sak_audit['inv_16piG_sakharov_full'])
    inv_16piG_obs = float(sak_audit['inv_16piG_obs'])
except:
    inv_16piG_sakharov = None
    inv_16piG_obs = 2.9646125e36

# Key constants
M_KK_GN   = float(cs['M_KK_from_GN'])       # 7.43e16 GeV (gravity route)
from canonical_constants import M_Pl_reduced as M_Pl  # reduced Planck mass [GeV]
from canonical_constants import G_N as G_N_obs  # SI [m^3 kg^-1 s^-2]
rho_Lambda_obs = 2.888e-47                    # GeV^4 (observed CC)

# GGE data (M_KK units, per cell)
branch_labels = gge['branch_labels']
E_k     = gge['E_8']          # quasiparticle energies per mode
n_k     = gge['nk_exact']     # exact occupation numbers
T_k     = gge['T_k']          # mode temperatures
beta_k  = gge['beta_k']       # inverse temperatures
rho_dos = gge['rho']          # DOS weight per mode
S_GGE   = float(gge['S_GGE'])   # Shannon entropy = -sum n_k ln n_k
E_GGE   = float(gge['E_GGE'])   # = 2 * sum(E_k * n_k) (pair energy)
N_total = float(gge['N_total_pairs'])

# Branch-level data
T_B2 = float(gge['T_B2']); T_B1 = float(gge['T_B1']); T_B3 = float(gge['T_B3'])
S_branch = gge['S_branch']    # [S_B2, S_B1, S_B3] (Shannon per branch)
E_branch = gge['E_branch']    # [E_B2, E_B1, E_B3] (pair energy per branch)
N_B2 = float(gge['N_B2']); N_B1 = float(gge['N_B1']); N_B3 = float(gge['N_B3'])

# GSL data
tau_fold = float(gsl['tau_fold'])
S_fold   = float(gsl['S_gen_timeline'][int(gsl['fold_idx'])])
N_cells  = int(gsl['N_cells'])
lambda_B2 = float(gsl['lambda_B2'])
lambda_B1 = float(gsl['lambda_B1'])
lambda_B3 = float(gsl['lambda_B3'])

# First law data
T_acoustic = float(fl['T_acoustic'])
X_tau      = float(fl['X_tau'])

# EIH singlet projection
f_singlet = float(eih['gate_ratio'])           # 5.684e-5
S_singlet = float(eih['S_singlet'])            # 14.23 spectral units
S_fold_SA = float(eih['S_fold'])               # 250,361

# Reference densities from prior computations
rho_SA         = float(eih['rho_SA_phys'])     # 8.43e73 GeV^4 (poly SA)
rho_TL         = float(eih['rho_TL_phys'])     # 2.60e71 GeV^4 (trace-log)
rho_singlet_SA = float(eih['rho_singlet_phys'])# 4.79e69 GeV^4 (EIH on SA)

print("=" * 72)
print("JACOBSON-SPEC-44: Jacobson Mapping for GGE Relic")
print("=" * 72)

# ═══════════════════════════════════════════════════════════════
# 2. VERIFY GGE THERMODYNAMIC QUANTITIES
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 2: GGE Thermodynamic Verification ---")

# Verify E_GGE = 2 * sum(E_k * n_k)
E_GGE_check = 2.0 * np.sum(E_k * n_k)
print(f"  E_GGE = 2 * sum(E_k * n_k) = {E_GGE_check:.6f} M_KK")
print(f"  E_GGE (file) = {E_GGE:.6f} M_KK")
print(f"  Consistency: {abs(E_GGE_check - E_GGE)/E_GGE:.2e}")

# Verify S_GGE = -sum(n_k * ln(n_k))
S_GGE_check = -np.sum(n_k[n_k > 0] * np.log(n_k[n_k > 0]))
print(f"\n  S_GGE = -sum(n_k ln n_k) = {S_GGE_check:.6f} nats")
print(f"  S_GGE (file) = {S_GGE:.6f} nats")
print(f"  S_max = ln(8) = {np.log(8):.6f} nats")
print(f"  S_GGE / S_max = {S_GGE / np.log(8):.4f}")

# Binary (thermodynamic) entropy per mode: h(n) = -n ln n - (1-n) ln(1-n)
h_k = np.zeros(8)
for i in range(8):
    ni = n_k[i]
    if 0 < ni < 1:
        h_k[i] = -(ni * np.log(ni) + (1 - ni) * np.log(1 - ni))
S_thermo = np.sum(h_k)
print(f"\n  Thermodynamic entropy (binary): S_thermo = {S_thermo:.6f} nats")
print(f"  Shannon entropy: S_Shannon = {S_GGE:.6f} nats")
print(f"  Difference: S_thermo - S_Shannon = {S_thermo - S_GGE:.6f}")

# ═══════════════════════════════════════════════════════════════
# 3. JACOBSON HEAT FLUX: delta Q = sum_k T_k dS_k
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 3: Jacobson Heat Flux ---")

# Jacobson's argument: on a local Rindler horizon, the Einstein equation
# follows from delta Q = T dS with T = Unruh temperature and S = A/4G.
#
# For a STATIONARY GGE (post-transit), the stress-energy tensor is:
#   T_{ab} = diag(rho, P, P, P)
# The Jacobson "heat" crossing the horizon per unit proper time is:
#   delta Q / (delta lambda * delta A) = T_{ab} k^a k^b = rho + P
#
# For a GGE, the gravitating density is the INTERNAL energy.
# The thermodynamic identity E = TS - PV + mu N gives (with mu=0, 0D: PV=0):
#   E_GGE = sum_k T_k S_k  (Euler relation for GGE)
#
# BUT: the T_k in the file are NOT from the simple Fermi-Dirac relation
# (beta_k E_k != -logit(n_k)). They are effective temperatures from a
# variational/fitting procedure. The PHYSICAL gravitating quantity is E_GGE.
#
# Three Jacobson prescriptions for the gravitating density:

# (A) INTERNAL ENERGY: rho = E_GGE (= 2 * sum E_k n_k)
#     This is the energy of the quasiparticle excitations.
#     = what the local Rindler observer measures as heat flux.
rho_A_MKK = E_GGE  # M_KK units

# (B) THERMODYNAMIC POTENTIAL: rho = sum T_k S_k
#     The Jacobson delta Q = T dS integrated gives the Euler relation.
#     For a multi-T system, this is sum_k T_k S_k.
#     Using the Shannon entropy (S_k = -n_k ln n_k) per mode:
S_k_shannon = np.zeros(8)
for i in range(8):
    if n_k[i] > 0:
        S_k_shannon[i] = -n_k[i] * np.log(n_k[i])

TS_sum_shannon = np.sum(T_k * S_k_shannon)
rho_B_MKK = TS_sum_shannon

# (C) ACOUSTIC TEMPERATURE: rho = T_acoustic * S_GGE
#     T_acoustic = 0.112 M_KK (from T-ACOUSTIC-40, the effective
#     temperature of the acoustic metric at the fold).
rho_C_MKK = T_acoustic * S_GGE

# (D) CONDENSATION ENERGY: rho = |E_cond| (energy released by BCS pairing)
E_cond = float(fl['E_cond'])  # 0.137 M_KK
rho_D_MKK = abs(E_cond)

# (E) PER-CELL PAIR ENERGY (N_total_pairs * <E_pair>)
E_pair_avg = E_GGE / N_total  # energy per pair
rho_E_MKK = E_GGE  # same as (A) but through pair counting

print(f"  Jacobson prescriptions (M_KK units, per cell):")
print(f"  (A) E_GGE = 2 sum E_k n_k = {rho_A_MKK:.6f}")
print(f"  (B) sum T_k S_k (Shannon) = {rho_B_MKK:.6f}")
print(f"  (C) T_acoustic * S_GGE    = {rho_C_MKK:.6f}")
print(f"  (D) |E_cond| (condensation)= {rho_D_MKK:.6f}")
print(f"  (E) N_pairs * <E_pair>    = {rho_E_MKK:.6f}")

# ═══════════════════════════════════════════════════════════════
# 4. GRAVITATING ENERGY DENSITY IN PHYSICAL UNITS
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 4: Gravitating Energy Density ---")

M_KK4 = M_KK_GN**4  # GeV^4

# Convert all prescriptions to GeV^4
prescriptions = {
    'SA_poly':       (rho_SA,                    'Spectral action (polynomial)'),
    'SA_tracelog':   (rho_TL,                    'Trace-log'),
    'SA_EIH':        (rho_singlet_SA,            'EIH singlet (SA poly)'),
    'Jac_E_GGE':     (rho_A_MKK * M_KK4,        'Jacobson: E_GGE (internal energy)'),
    'Jac_TS':        (rho_B_MKK * M_KK4,        'Jacobson: sum T_k S_k (Euler)'),
    'Jac_acoustic':  (rho_C_MKK * M_KK4,        'Jacobson: T_acoustic * S_GGE'),
    'Jac_Econd':     (rho_D_MKK * M_KK4,        'Jacobson: |E_cond| (condensation)'),
    'Jac_E_EIH':     (f_singlet * rho_A_MKK * M_KK4, 'Jacobson: E_GGE * f_singlet'),
    'Jac_TS_EIH':    (f_singlet * rho_B_MKK * M_KK4, 'Jacobson: sum T_k S_k * f_singlet'),
    'Jac_Econd_EIH': (f_singlet * rho_D_MKK * M_KK4, 'Jacobson: |E_cond| * f_singlet'),
}

print(f"\n  M_KK = {M_KK_GN:.4e} GeV")
print(f"  M_KK^4 = {M_KK4:.4e} GeV^4")
print(f"  rho_obs (Lambda) = {rho_Lambda_obs:.4e} GeV^4")
print(f"  f_singlet (EIH) = {f_singlet:.4e}")
print()
print(f"  {'Prescription':<40s} {'rho [GeV^4]':>14s} {'log10(rho/rho_obs)':>20s}")
print(f"  {'-'*76}")

log10_gaps = {}
for key, (rho_val, desc) in prescriptions.items():
    gap = np.log10(rho_val / rho_Lambda_obs)
    log10_gaps[key] = gap
    print(f"  {desc:<40s} {rho_val:14.3e} {gap:20.2f}")
print(f"  {'Observed Lambda':<40s} {rho_Lambda_obs:14.3e} {'0.00':>20s}")

# ═══════════════════════════════════════════════════════════════
# 5. JACOBSON-SPECIFIC: WHY GGE ENERGY << SPECTRAL ACTION
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 5: Why E_GGE << S_fold ---")

# The spectral action S_fold = 250,361 spectral units
# The GGE energy E_GGE = 1.688 M_KK
# The ratio E_GGE / S_fold = 6.7e-6
#
# The spectral action sums ALL eigenvalues: S_fold = Tr f(D_K^2/Lambda^2)
# The GGE energy sums only OCCUPIED modes near the gap: E_GGE = 2 sum E_k n_k
#
# This is the Jacobson insight applied to the framework:
# Gravity couples to the HEAT FLUX (thermodynamic energy), not to the
# total spectral weight. The spectral action is the analog of the total
# number of microstates; the gravitating density is the analog of the
# actual thermal energy.

ratio_EGGE_Sfold = E_GGE / S_fold_SA
print(f"  S_fold (spectral action) = {S_fold_SA:.2f}")
print(f"  E_GGE (pair energy)      = {E_GGE:.6f} M_KK")
print(f"  Ratio E_GGE / S_fold     = {ratio_EGGE_Sfold:.4e}")
print(f"  Suppression:             {-np.log10(ratio_EGGE_Sfold):.2f} orders")

# The suppression has TWO sources:
# 1. Only 8 modes (out of 992 KK eigenvalues) participate in BCS pairing
# 2. Occupation numbers n_k << 1 for most modes (B3 has n ~ 0.003)
n_active = 8
n_total_KK = 992
print(f"\n  Source 1: active modes: {n_active}/{n_total_KK} = {n_active/n_total_KK:.4e}")
print(f"  Source 2: mean occupation: <n_k> = {np.mean(n_k):.4f}")
print(f"  Combined: {n_active/n_total_KK * np.mean(n_k):.4e}")
print(f"  Actual ratio: {ratio_EGGE_Sfold:.4e}")
print(f"  Additional factor: {ratio_EGGE_Sfold / (n_active/n_total_KK * np.mean(n_k)):.2f}")

# ═══════════════════════════════════════════════════════════════
# 6. 8-FLUID EQUATION OF STATE
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 6: 8-Fluid Equation of State ---")

# For massive quasiparticles with mass m_k and kinetic energy T_k:
# In the non-relativistic limit (T << m): w = 0 (cold dark matter)
# In the relativistic limit (T >> m): w = 1/3 (radiation)
# General: w = <v^2>/3 where v = p/E (velocity)
#
# For BCS quasiparticles, E_k is the gap energy (rest mass equivalent).
# The T_k are effective GGE temperatures. The ratio T_k/E_k determines
# whether the quasiparticle is "hot" or "cold":
#
# w_k = T_k / (m_k + T_k)  (relativistic correction)
# For T_k << m_k: w_k ~ T_k/m_k (non-relativistic)
# For T_k >> m_k: w_k ~ 1 (stiff matter)

# But T_k and E_k are comparable for B2 modes (T_B2 ~ 0.7 E_B2).
# This means B2 quasiparticles are SEMI-RELATIVISTIC.

# More precisely, for a free particle in the non-relativistic limit:
# w = P/rho = nT / (nm + 3nT/2) ~ T/m for T << m
# But our "temperature" T_k is the GGE effective temperature, not kinetic T.
# The EOS is w_k = P_k/rho_k where:
#   rho_k = E_k * n_k * (pair factor 2)  (rest mass energy dominates)
#   P_k = n_k * T_k / V  (ideal gas)
# => w_k = T_k / (2 E_k)  (factor 2 from pair energy vs single-particle T)

# Actually for massive non-relativistic particles:
# rho = n * m_eff (energy density = number density * mass)
# P = n * T (pressure = number density * temperature, kinetic theory)
# w = P/rho = T/m_eff
# Here m_eff = 2 * E_k (pair mass), T = T_k
w_k = T_k / (2.0 * E_k)

print(f"  Mode-level EOS (w_k = T_k / 2E_k):")
print(f"  {'Mode':<10s} {'E_k':>8s} {'T_k':>8s} {'n_k':>8s} {'w_k':>10s} {'Class':>15s}")
print(f"  {'-'*55}")
for i in range(8):
    cls = 'CDM' if w_k[i] < 0.01 else 'warm' if w_k[i] < 0.1 else 'hot' if w_k[i] < 1/3 else 'radiation'
    print(f"  {branch_labels[i]:<10s} {E_k[i]:8.4f} {T_k[i]:8.4f} {n_k[i]:8.4f} {w_k[i]:10.4f} {cls:>15s}")

# Branch-level weighted EOS
E_B2_modes = E_k[:4]
T_B2_modes = T_k[:4]
n_B2_modes = n_k[:4]
w_B2_avg = np.sum(T_B2_modes * n_B2_modes) / np.sum(2 * E_B2_modes * n_B2_modes)
w_B1 = T_k[4] / (2 * E_k[4])
w_B3_avg = np.sum(T_k[5:8] * n_k[5:8]) / np.sum(2 * E_k[5:8] * n_k[5:8])

print(f"\n  Branch-level EOS (energy-weighted):")
print(f"  {'Branch':<10s} {'w':>10s} {'N_pairs':>10s} {'E_branch':>12s} {'S_branch':>12s}")
print(f"  {'-'*56}")
print(f"  {'B2':<10s} {w_B2_avg:10.4f} {N_B2:10.2f} {E_branch[0]:12.4f} {S_branch[0]:12.4f}")
print(f"  {'B1':<10s} {w_B1:10.4f} {N_B1:10.2f} {E_branch[1]:12.4f} {S_branch[1]:12.4f}")
print(f"  {'B3':<10s} {w_B3_avg:10.4f} {N_B3:10.2f} {E_branch[2]:12.4f} {S_branch[2]:12.4f}")

# Overall EOS
w_eff = np.sum(T_k * n_k) / np.sum(2 * E_k * n_k)
print(f"\n  Overall energy-weighted EOS: w_eff = {w_eff:.4f}")

# Cosmological interpretation
print(f"\n  Cosmological interpretation:")
print(f"  B2 (w = {w_B2_avg:.3f}): hot dark matter / ultra-relativistic relic")
print(f"  B1 (w = {w_B1:.3f}): warm/hot component")
print(f"  B3 (w = {w_B3_avg:.3f}): warm component (near CDM boundary)")
print(f"  Overall w = {w_eff:.4f} ({('CDM-like' if w_eff < 0.01 else 'warm DM' if w_eff < 0.1 else 'hot DM' if w_eff < 1/3 else 'radiation-like')})")
print(f"  Note: T_k/m_k ~ O(1) means these are NOT cold. The GGE relic")
print(f"  behaves as a multi-temperature HOT component, not CDM.")

# However — the key insight from S42 C-FABRIC-42 is that the
# DISPERSIVE quasiparticles (with E = sqrt(Delta^2 + p^2)) at late times
# become non-relativistic (p -> 0, E -> Delta = m_eff). The GGE
# temperatures describe the INITIAL occupation, not the late-time velocity.
# At late times, all modes are massive with v -> 0, so w -> 0 (CDM).
print(f"\n  Late-time behavior: as universe expands, p ~ 1/a -> 0")
print(f"  All modes become non-relativistic: w -> 0 (CDM-like)")
print(f"  The T_k are INITIAL occupation parameters, not kinetic temperatures")
print(f"  CDM classification (from S42 C-FABRIC-42) is CORRECT asymptotically")

# ═══════════════════════════════════════════════════════════════
# 7. COMPLETE CC SUPPRESSION CHAIN
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 7: Complete CC Suppression Chain ---")

# The chain of independent suppressions from spectral action to observed CC:
log_SA = np.log10(rho_SA / rho_Lambda_obs)
log_TL = np.log10(rho_TL / rho_Lambda_obs)
log_EIH_SA = np.log10(rho_singlet_SA / rho_Lambda_obs)

rho_Jac = rho_A_MKK * M_KK4
log_Jac = np.log10(rho_Jac / rho_Lambda_obs)

rho_Jac_EIH = f_singlet * rho_A_MKK * M_KK4
log_Jac_EIH = np.log10(rho_Jac_EIH / rho_Lambda_obs)

rho_Econd = rho_D_MKK * M_KK4
log_Econd = np.log10(rho_Econd / rho_Lambda_obs)

rho_Econd_EIH = f_singlet * rho_D_MKK * M_KK4
log_Econd_EIH = np.log10(rho_Econd_EIH / rho_Lambda_obs)

print(f"\n  {'Step':<40s} {'rho [GeV^4]':>14s} {'Gap [OOM]':>10s} {'Suppression':>12s}")
print(f"  {'-'*78}")
print(f"  {'(0) Spectral action S_fold (poly)':<40s} {rho_SA:14.3e} {log_SA:10.1f} {'---':>12s}")
print(f"  {'(1) Poly -> Trace-log':<40s} {rho_TL:14.3e} {log_TL:10.1f} {log_SA - log_TL:12.1f}")
print(f"  {'(2) EIH singlet (poly)':<40s} {rho_singlet_SA:14.3e} {log_EIH_SA:10.1f} {log_SA - log_EIH_SA:12.1f}")
print(f"  {'(3) SA -> GGE E_GGE (Jacobson)':<40s} {rho_Jac:14.3e} {log_Jac:10.1f} {log_SA - log_Jac:12.1f}")
print(f"  {'(4) GGE E_GGE + EIH singlet':<40s} {rho_Jac_EIH:14.3e} {log_Jac_EIH:10.1f} {log_SA - log_Jac_EIH:12.1f}")
print(f"  {'(5) E_cond (condensation only)':<40s} {rho_Econd:14.3e} {log_Econd:10.1f} {log_SA - log_Econd:12.1f}")
print(f"  {'(6) E_cond + EIH':<40s} {rho_Econd_EIH:14.3e} {log_Econd_EIH:10.1f} {log_SA - log_Econd_EIH:12.1f}")
print(f"  {'Observed Lambda':<40s} {rho_Lambda_obs:14.3e} {'0.0':>10s} {log_SA:12.1f}")

# Physical interpretation of the suppression:
#  Step 0->3: The spectral action counts ALL 992 KK eigenvalues. The Jacobson
#    internal energy counts only the 8 active BCS modes, weighted by
#    occupation n_k. This gives 6.2 orders of suppression.
#  Step 3->4: The EIH singlet projection removes non-singlet representations
#    (4.2 orders). This is the ADM mass effacement.
#  Step 3->5: Using E_cond instead of E_GGE — only the binding energy
#    gravitates, not the rest mass of quasiparticles. This gives an additional
#    1.1 orders.

# Identify the Jacobson-specific contribution:
Jacobson_suppression = log_SA - log_Jac
print(f"\n  JACOBSON-SPECIFIC suppression: {Jacobson_suppression:.2f} orders")
print(f"  (Spectral action -> GGE internal energy)")
print(f"  This is the replacement of Tr f(D^2/Lambda^2) by E_GGE = 2 sum E_k n_k")

# Combined Jacobson + EIH:
combined_suppression = log_SA - log_Jac_EIH
print(f"\n  COMBINED Jacobson + EIH: {combined_suppression:.2f} orders suppression")
print(f"  Remaining gap: {log_Jac_EIH:.1f} OOM above Lambda_obs")

# ═══════════════════════════════════════════════════════════════
# 8. MULTI-TEMPERATURE JACOBSON EQUATION
# ═══════════════════════════════════════════════════════════════
print("\n--- Step 8: Multi-Temperature Jacobson Equation ---")

# S43 CC workshop E3: "The correct first law is delta Q = sum_k T_k dS_k."
# For the GGE, each conserved charge Q_k = N_k (pair number in mode k).
# The first law per mode:
#   dE_k = T_k dS_k + mu_k dN_k
# with mu_k = 0 (PH symmetry, Session 34).
#
# The MULTI-TEMPERATURE Jacobson equation on a Rindler horizon:
#   R_{ab} k^a k^b = 8piG sum_k T_k^{ab} k^a k^b
# where each T_k^{ab} is the stress-energy of fluid k.
#
# This gives 8 coupled Friedmann-like equations — one per conserved charge.
# But since all fluids share the SAME metric (same G_{ab}), the 8 equations
# are consistent only if the gravitating density is the SUM:
#   rho_grav = sum_k rho_k = E_GGE

print(f"  Multi-T Jacobson equation: R_00 = 8piG * sum_k T_00^(k)")
print(f"  T_00^(k) = E_k * n_k * (pair factor 2)")
print()
print(f"  {'Mode k':>10s} {'T_00^(k) [M_KK]':>16s} {'Fraction':>10s}")
print(f"  {'-'*38}")
T00_k = 2.0 * E_k * n_k
T00_total = np.sum(T00_k)
for i in range(8):
    print(f"  {branch_labels[i]:>10s} {T00_k[i]:16.6f} {T00_k[i]/T00_total:10.4f}")
print(f"  {'Total':>10s} {T00_total:16.6f} {'1.0000':>10s}")
print(f"  Check: T00_total = E_GGE = {E_GGE:.6f} -> diff = {abs(T00_total - E_GGE):.2e}")

# B2 dominates because of high DOS (rho = 14.02) — but here we used the
# per-cell occupation n_k (which already folds in DOS through the BCS dynamics).
# The dominance of B2 (89% of gravitating energy) is a van Hove effect:
# the DOS singularity at B2 produces more pairs.
frac_B2 = np.sum(T00_k[:4]) / T00_total
frac_B1 = T00_k[4] / T00_total
frac_B3 = np.sum(T00_k[5:8]) / T00_total
print(f"\n  Branch fractions of gravitating energy:")
print(f"  B2: {frac_B2:.4f} ({frac_B2*100:.1f}%)")
print(f"  B1: {frac_B1:.4f} ({frac_B1*100:.1f}%)")
print(f"  B3: {frac_B3:.4f} ({frac_B3*100:.1f}%)")

# ═══════════════════════════════════════════════════════════════
# 9. GATE VERDICT
# ═══════════════════════════════════════════════════════════════
print("\n" + "=" * 72)
print("GATE VERDICT: JACOBSON-SPEC-44")
print("=" * 72)

# The Jacobson gravitating density: E_GGE * M_KK^4
# This is the DEFINITIVE Jacobson result — the internal energy of the GGE
# is what crosses the local Rindler horizon and sources the Einstein equation.
rho_gate = rho_Jac
gap_gate = log_Jac

# Gate thresholds
threshold_pass = 30.0
threshold_fail = 60.0

if gap_gate <= threshold_pass:
    verdict = "PASS"
elif gap_gate > threshold_fail:
    verdict = "FAIL"
else:
    verdict = "INFO"

print(f"\n  rho_Jacobson = E_GGE * M_KK^4 = {rho_gate:.4e} GeV^4")
print(f"  rho_observed = {rho_Lambda_obs:.4e} GeV^4")
print(f"  Gap: {gap_gate:.2f} OOM")
print(f"  Gate PASS threshold: <= {threshold_pass:.0f} OOM")
print(f"  Gate FAIL threshold: > {threshold_fail:.0f} OOM")
print(f"\n  >>> JACOBSON-SPEC-44 = {verdict} <<<")

# Assess what the Jacobson approach achieves:
print(f"\n  What Jacobson achieves:")
print(f"  - Replaces spectral action ({log_SA:.1f} OOM) with GGE energy ({log_Jac:.1f} OOM)")
print(f"  - Suppression: {Jacobson_suppression:.2f} orders (SA -> GGE)")
print(f"  - With EIH singlet: additional {log_Jac - log_Jac_EIH:.2f} orders -> {log_Jac_EIH:.1f} OOM")
print(f"  - Gap reduced from {log_SA:.0f} to {log_Jac_EIH:.0f} OOM: {combined_suppression:.0f} orders removed")
print(f"  - Still {log_Jac_EIH:.0f} OOM short: need {log_Jac_EIH:.0f} more orders from other mechanisms")

print(f"\n  What Jacobson does NOT achieve:")
print(f"  - Does not close the CC gap (110 OOM remains)")
print(f"  - The GGE energy E_GGE is O(M_KK), giving rho ~ M_KK^4")
print(f"  - Only ~10 orders can be attributed to Jacobson + EIH")
print(f"  - The 110-order residual gap requires physics beyond")
print(f"    thermodynamic reweighting (e.g., cancellation mechanisms)")

# ═══════════════════════════════════════════════════════════════
# 10. SAVE RESULTS
# ═══════════════════════════════════════════════════════════════

results = {
    # GGE mode-level data
    'branch_labels': branch_labels,
    'E_k': E_k,
    'T_k': T_k,
    'n_k': n_k,
    'rho_dos': rho_dos,
    'beta_k': beta_k,
    'h_k': h_k,
    'S_k_shannon': S_k_shannon,

    # EOS
    'w_k': w_k,
    'w_B2': w_B2_avg,
    'w_B1': w_B1,
    'w_B3': w_B3_avg,
    'w_eff': w_eff,

    # Branch-level
    'T_branches': np.array([T_B2, T_B1, T_B3]),
    'E_branches': E_branch,
    'S_branches': S_branch,
    'frac_B2': frac_B2,
    'frac_B1': frac_B1,
    'frac_B3': frac_B3,

    # Thermodynamic quantities
    'E_GGE': E_GGE,
    'S_GGE': S_GGE,
    'S_thermo': S_thermo,
    'TS_sum_shannon': TS_sum_shannon,
    'E_cond': E_cond,

    # Jacobson prescriptions (M_KK units)
    'rho_A_MKK': rho_A_MKK,
    'rho_B_MKK': rho_B_MKK,
    'rho_C_MKK': rho_C_MKK,
    'rho_D_MKK': rho_D_MKK,

    # Multi-T stress-energy
    'T00_k': T00_k,
    'T00_total': T00_total,

    # Gravitating densities (GeV^4)
    'rho_SA': rho_SA,
    'rho_TL': rho_TL,
    'rho_singlet_SA': rho_singlet_SA,
    'rho_Jacobson': rho_Jac,
    'rho_Jacobson_EIH': rho_Jac_EIH,
    'rho_Econd': rho_Econd,
    'rho_Econd_EIH': rho_Econd_EIH,
    'rho_obs': rho_Lambda_obs,

    # Log10 gaps (OOM above Lambda_obs)
    'log10_gap_SA': log_SA,
    'log10_gap_TL': log_TL,
    'log10_gap_EIH_SA': log_EIH_SA,
    'log10_gap_Jacobson': log_Jac,
    'log10_gap_Jacobson_EIH': log_Jac_EIH,
    'log10_gap_Econd': log_Econd,
    'log10_gap_Econd_EIH': log_Econd_EIH,

    # Suppression chain
    'suppression_SA_to_GGE': Jacobson_suppression,
    'suppression_SA_to_GGE_EIH': combined_suppression,
    'suppression_poly_to_log': log_SA - log_TL,
    'suppression_total_to_singlet': log_SA - log_EIH_SA,
    'suppression_GGE_to_EIH': log_Jac - log_Jac_EIH,

    # Ratio
    'ratio_EGGE_Sfold': ratio_EGGE_Sfold,
    'f_singlet': f_singlet,
    'S_fold': S_fold_SA,

    # Constants
    'M_KK_GN': M_KK_GN,
    'M_Pl': M_Pl,
    'tau_fold': tau_fold,
    'T_acoustic': T_acoustic,

    # Gate
    'gate_name': np.array(['JACOBSON-SPEC-44']),
    'gate_verdict': np.array([verdict]),
    'gate_gap_OOM': gap_gate,
    'gate_gap_EIH_OOM': log_Jac_EIH,
    'gate_threshold_pass': threshold_pass,
    'gate_threshold_fail': threshold_fail,
}

np.savez(data_dir / 's44_jacobson_spec.npz', **results)
print(f"\n  Data saved: s44_jacobson_spec.npz")

# ═══════════════════════════════════════════════════════════════
# 11. PLOT
# ═══════════════════════════════════════════════════════════════

fig, axes = plt.subplots(1, 3, figsize=(18, 6.5))

# --- Panel 1: CC Suppression Chain ---
ax1 = axes[0]
bar_labels = [
    'SA\n(poly)',
    'Tr ln\n(log)',
    'EIH\n(SA)',
    'GGE\nE$_{GGE}$',
    'GGE\n+EIH',
    'E$_{cond}$',
    'E$_{cond}$\n+EIH',
]
bar_gaps = [log_SA, log_TL, log_EIH_SA, log_Jac, log_Jac_EIH, log_Econd, log_Econd_EIH]
bar_colors = ['#d62728', '#ff7f0e', '#ff7f0e', '#2ca02c', '#2ca02c', '#1f77b4', '#1f77b4']

bars = ax1.bar(range(len(bar_labels)), bar_gaps, color=bar_colors, alpha=0.8,
               edgecolor='black', linewidth=0.5)
ax1.set_xticks(range(len(bar_labels)))
ax1.set_xticklabels(bar_labels, fontsize=7.5)
ax1.set_ylabel('log$_{10}$(rho / rho$_{obs}$)', fontsize=11)
ax1.set_title('CC Suppression Chain\n(Spectral Action -> Jacobson -> EIH)', fontsize=11, fontweight='bold')
ax1.axhline(y=30, color='green', linestyle='--', alpha=0.7, linewidth=1.5, label='PASS (30 OOM)')
ax1.axhline(y=60, color='red', linestyle='--', alpha=0.7, linewidth=1.5, label='FAIL (60 OOM)')
ax1.legend(fontsize=8, loc='upper right')
ax1.set_ylim(0, max(bar_gaps) * 1.12)
for i, (g, bar) in enumerate(zip(bar_gaps, bars)):
    ax1.text(i, g + 1.5, f'{g:.1f}', ha='center', va='bottom', fontsize=7.5, fontweight='bold')

# --- Panel 2: 8-Fluid EOS ---
ax2 = axes[1]
mode_names = [str(bl) for bl in branch_labels]
mode_colors = ['#1f77b4'] * 4 + ['#ff7f0e'] + ['#2ca02c'] * 3
ax2.bar(range(8), w_k, color=mode_colors, alpha=0.8, edgecolor='black', linewidth=0.5)
ax2.set_xticks(range(8))
ax2.set_xticklabels(mode_names, fontsize=7.5, rotation=45, ha='right')
ax2.set_ylabel('w$_k$ = T$_k$ / 2E$_k$', fontsize=11)
ax2.set_title('8-Fluid Equation of State', fontsize=11, fontweight='bold')
ax2.axhline(y=1/3, color='red', linestyle=':', alpha=0.7, label='Radiation (w=1/3)')
ax2.axhline(y=0, color='black', linestyle='-', alpha=0.3, label='CDM (w=0)')
ax2.axhline(y=w_eff, color='purple', linestyle='--', alpha=0.7, label=f'$\\langle w \\rangle$ = {w_eff:.3f}')
ax2.legend(fontsize=8, loc='upper right')
ax2.set_ylim(0, max(w_k) * 1.15)
for i in range(8):
    ax2.text(i, w_k[i] + 0.01, f'{w_k[i]:.3f}', ha='center', va='bottom', fontsize=7)

# --- Panel 3: Gravitating Energy Fractions ---
ax3 = axes[2]
# Stacked bar: energy fraction per mode
frac_k = T00_k / T00_total
# Group by branch
branch_fracs = [frac_B2, frac_B1, frac_B3]
branch_names = ['B2\n(4 modes)', 'B1\n(1 mode)', 'B3\n(3 modes)']
branch_cols = ['#1f77b4', '#ff7f0e', '#2ca02c']
bars3 = ax3.bar(range(3), branch_fracs, color=branch_cols, alpha=0.8,
                edgecolor='black', linewidth=0.5)
ax3.set_xticks(range(3))
ax3.set_xticklabels(branch_names, fontsize=10)
ax3.set_ylabel('Fraction of T$_{00}^{total}$', fontsize=11)
ax3.set_title('Gravitating Energy by Branch\n(Multi-T Jacobson)', fontsize=11, fontweight='bold')
for i, (f, bar) in enumerate(zip(branch_fracs, bars3)):
    ax3.text(i, f + 0.01, f'{f*100:.1f}%', ha='center', va='bottom', fontsize=10, fontweight='bold')

# Add text annotations
textstr = (f'E$_{{GGE}}$ = {E_GGE:.3f} M$_{{KK}}$\n'
           f'w$_{{eff}}$ = {w_eff:.4f}\n'
           f'Gap = {log_Jac:.1f} OOM\n'
           f'(+EIH: {log_Jac_EIH:.1f} OOM)')
ax3.text(0.95, 0.55, textstr, transform=ax3.transAxes, fontsize=9,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

plt.suptitle('JACOBSON-SPEC-44: Jacobson Mapping for GGE Relic — FAIL (114 OOM)',
             fontsize=13, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig(data_dir / 's44_jacobson_spec.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: s44_jacobson_spec.png")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
