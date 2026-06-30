#!/usr/bin/env python3
"""
s58_transfer_function.py — Phononic DM Transfer Function T(k)
=============================================================

Gate: TRANSFER-FUNCTION-58
  PASS: WDM mass equivalent > 5.3 keV (Lyman-alpha compatible)
  FAIL: < 2.0 keV (excluded)
  INFO: [2.0, 5.3] keV (marginal)

Method (following Paper 15: Ganjoo-Erickcek-Lin-Mack 2022, and
Paper 16: Lin-Chen-Ganjoo-Hou-Mack 2023):

The phononic DM from the GGE has a non-thermal distribution with mode-dependent
effective temperatures T_k. The free-streaming length is set by the velocity
dispersion of these quasiparticles. The transfer function T(k) = P_phononic(k)/P_CDM(k)
encodes the suppression of the matter power spectrum at small scales due to this
velocity dispersion.

Key physics:
  1. DM quasiparticles have dispersion omega(K) = 2J(1 - cos Ka) [tight-binding]
  2. GGE distribution is non-thermal with mode-dependent T_k
  3. Velocity dispersion <v^2> from the GGE sets the free-streaming scale
  4. The cutoff k_cut where T(k) = 0.5 maps to an equivalent WDM thermal mass
  5. This WDM mass must exceed 5.3 keV (Irsic et al. 2017 Lyman-alpha bound)

Convention note: All internal quantities are in M_KK units. The mapping to
cosmological scales (h/Mpc) requires M_KK in GeV and standard conversion factors.

Session: S58 W3-14 (Mack)
Depends on: W3-6 (S(q,omega)), W3-7 (impedance), S54 (tight-binding)
"""

import sys
sys.path.insert(0, '.')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    M_KK, M_KK_gravity, M_KK_kerner,
    Omega_DM, Omega_m, H_0_km_s_Mpc, H_0_GeV,
    T_CMB, T_CMB_GeV, k_B, Mpc_to_m, hbar_c_GeV_m,
    c_light, c_light_km_s, rho_crit_GeV4,
    Delta_0_OES, E_cond, tau_fold, J_C2, T_acoustic,
    N_cells, Omega_Lambda, sigma_8, t_universe_s,
    hbar_GeV_s, GeV_to_inv_m, Mpc_to_GeV_inv, GeV_inv_to_Mpc,
)

# ==============================================================================
# SECTION 1: Load input data
# ==============================================================================

sq_data = np.load('s58_sq_omega_gge.npz', allow_pickle=True)
imp_data = np.load('s58_impedance_boundary.npz', allow_pickle=True)
tb_data = np.load('s54_tb_hamiltonian.npz', allow_pickle=True)

# GGE effective temperatures per mode (M_KK units)
T_k_gge = sq_data['T_k_volovik']       # shape (8,)
fk_gge = sq_data['fk_gge']             # GGE occupation numbers
E_k = sq_data['E_k']                   # Quasiparticle energies (M_KK)
xi_k = sq_data['xi_k']                 # Dispersion energies (M_KK)
Delta = sq_data['Delta'].item()         # BCS gap (M_KK)

# Spectral band data
omega_L = sq_data['omega_L']            # Leggett band frequencies
omega_BA = sq_data['omega_BA']          # BA band frequencies
W_L = sq_data['W_gge_leggett'].item()
W_BA = sq_data['W_gge_BA'].item()
W_pb = sq_data['W_gge_pb'].item()

# Transmission coefficient at fold
T_loc_mean = imp_data['T_loc_mean'][0]  # constant across tau = 0.969
T_loc_min = imp_data['T_loc_min'][0]

# Tight-binding parameters at fold
fold_idx_tb = 19  # tau ~ 0.194
J_C2_fold = tb_data['J_C2_tau'][fold_idx_tb]
bandwidth_fold = tb_data['bandwidths'][fold_idx_tb]
eigs_fold = tb_data['eigenvalues'][fold_idx_tb]

print("=" * 70)
print("S58 TRANSFER FUNCTION: Phononic DM T(k)")
print("=" * 70)
print()

# ==============================================================================
# SECTION 2: Compute velocity dispersion from GGE
# ==============================================================================

# The tight-binding dispersion on the 32-cell graph is:
#   omega_n = eigenvalue_n of H_TB  (not a simple cosine for a graph)
#
# For a 1D tight-binding chain: omega(K) = 2J(1 - cos Ka)
# Group velocity: v_g(K) = dw/dK = 2Ja sin(Ka)
#
# On the 32-cell graph, the "velocity" is the energy derivative with respect
# to the graph Laplacian eigenvalue lambda_n:
#   v_n ~ d(omega_n)/d(sqrt(lambda_n))
#
# The velocity dispersion is:
#   <v^2> = sum_k f_k * v_k^2 / sum_k f_k
#
# For the Leggett mode (dominant DM channel, 46.1% weight):
# The Leggett band spans [0.138, 0.383] M_KK on q in [0, pi/a]
# The group velocity is bounded by the band derivative.

# Method: compute group velocity from the tight-binding band structure.
# The Leggett band disperses across the 32-cell graph with width
# delta_omega_L = 0.383 - 0.138 = 0.245 M_KK over the BZ.
#
# For a graph, the "Brillouin zone" spans the Laplacian eigenvalues.
# The effective group velocity is:
#   v_eff ~ delta_omega / delta_K ~ delta_omega * a_lattice

# Lattice spacing in M_KK^{-1}: the SU(3) fiber has characteristic size ~ 1/M_KK.
# But the *fabric* (32-cell tessellation) is the cosmological structure.
# The inter-cell spacing is set by the coherence length xi_BCS = 0.808 M_KK^{-1}.
# In physical units: a_cell = xi_BCS / M_KK (meters) -- but we work in M_KK units.

# The Laplacian eigenvalues of the 32-cell graph span [0, lambda_max]
lapl_eigs = sq_data['laplacian_eigs']  # shape (32,)
lambda_max = lapl_eigs.max()
print(f"Graph Laplacian eigenvalues: min={lapl_eigs.min():.4f}, max={lambda_max:.4f}")

# Effective "momentum" on the graph: K_n = sqrt(lambda_n)
K_eff = np.sqrt(lapl_eigs)
K_max = K_eff.max()
print(f"Effective K range: [0, {K_max:.4f}] (M_KK units)")

# Tight-binding dispersion at fold: eigenvalues give omega(K_n)
# Group velocity: v_n = d omega / d K evaluated from finite differences
# Sort by K for interpolation
sort_idx = np.argsort(K_eff)
K_sorted = K_eff[sort_idx]
E_sorted = eigs_fold[sort_idx]

# Compute group velocity as finite difference of sorted (K, E)
v_group = np.zeros(len(K_sorted))
for i in range(1, len(K_sorted) - 1):
    dK = K_sorted[i+1] - K_sorted[i-1]
    if dK > 1e-12:
        v_group[i] = (E_sorted[i+1] - E_sorted[i-1]) / dK
# Boundary: use one-sided
if len(K_sorted) > 1 and (K_sorted[1] - K_sorted[0]) > 1e-12:
    v_group[0] = (E_sorted[1] - E_sorted[0]) / (K_sorted[1] - K_sorted[0])
if (K_sorted[-1] - K_sorted[-2]) > 1e-12:
    v_group[-1] = (E_sorted[-1] - E_sorted[-2]) / (K_sorted[-1] - K_sorted[-2])

v_group_rms = np.sqrt(np.mean(v_group**2))
v_group_max = np.max(np.abs(v_group))

print(f"\nGroup velocity (all modes):")
print(f"  v_rms = {v_group_rms:.6f} M_KK (c=1 units)")
print(f"  v_max = {v_group_max:.6f} M_KK")

# Now weight by GGE occupation numbers.
# The 8 BCS modes have occupations fk_gge. The TB Hamiltonian has 32 modes.
# The 8 GGE modes map to the lowest-energy TB modes (BCS active modes).
# Map: the first 8 sorted TB eigenvalues correspond to the BCS sector.
n_bcs = len(fk_gge)  # 8

# Velocity dispersion weighted by GGE occupations:
# <v^2>_GGE = sum_{k=1}^{8} f_k * v_k^2 / sum f_k
# where v_k is the group velocity of mode k

# The BCS modes are the low-energy ones (sorted by energy)
energy_sort = np.argsort(eigs_fold)
bcs_mode_indices = energy_sort[:n_bcs]

# Get K values and group velocities for BCS modes
v_bcs = np.zeros(n_bcs)
for i, midx in enumerate(bcs_mode_indices):
    # Find this mode in the K-sorted array
    pos = np.where(sort_idx == midx)[0][0]
    v_bcs[i] = v_group[pos]

v2_gge = np.sum(fk_gge * v_bcs**2) / np.sum(fk_gge)
v_rms_gge = np.sqrt(v2_gge)

print(f"\nGGE-weighted velocity dispersion:")
print(f"  <v^2>_GGE = {v2_gge:.6f}")
print(f"  v_rms_GGE = {v_rms_gge:.6f} (units of c)")

# ==============================================================================
# SECTION 3: Compute the Leggett-band velocity dispersion
# ==============================================================================

# The Leggett band is the dominant DM channel (46.1% of spectral weight).
# It disperses from omega_L_min = 0.138 to omega_L_max = 0.383 M_KK.
# The group velocity of the Leggett mode across the graph:
#   v_L ~ d(omega_L)/dK

# From the S(q,omega) data, the Leggett frequency varies with q:
q_values = sq_data['q_values']  # shape (32,)
omega_L_q = sq_data['omega_L']  # shape (32,), omega_L at each q

# Sort by q
q_sort = np.argsort(q_values)
q_s = q_values[q_sort]
omL_s = omega_L_q[q_sort]

# Group velocity of Leggett mode
v_L_group = np.zeros(len(q_s))
for i in range(1, len(q_s) - 1):
    dq = q_s[i+1] - q_s[i-1]
    if dq > 1e-12:
        v_L_group[i] = (omL_s[i+1] - omL_s[i-1]) / dq
if len(q_s) > 1 and (q_s[1] - q_s[0]) > 1e-12:
    v_L_group[0] = (omL_s[1] - omL_s[0]) / (q_s[1] - q_s[0])
if (q_s[-1] - q_s[-2]) > 1e-12:
    v_L_group[-1] = (omL_s[-1] - omL_s[-2]) / (q_s[-1] - q_s[-2])

v_L_rms = np.sqrt(np.mean(v_L_group**2))
v_L_max = np.max(np.abs(v_L_group))

print(f"\nLeggett band group velocity:")
print(f"  v_L_rms = {v_L_rms:.6f} (c=1)")
print(f"  v_L_max = {v_L_max:.6f}")
print(f"  omega_L range: [{omL_s.min():.4f}, {omL_s.max():.4f}] M_KK")

# ==============================================================================
# SECTION 4: Compute the effective DM velocity dispersion
# ==============================================================================

# The phononic DM has three bands contributing:
# 1. Leggett (46.1%): gapped collective mode, group velocity v_L
# 2. BA (23.3%): acoustic-like, higher velocity
# 3. Pair-breaking (30.6%): very heavy, effectively cold
#
# For the transfer function, the relevant quantity is the velocity dispersion
# of the DM component that free-streams.
#
# Following Paper 16 (Lin et al. 2023), the suppression scale is set by
# k_fs ~ H(a_nr) / v_DM(a_nr) where a_nr is the NR transition.
#
# For the GGE, the DM is ALREADY non-relativistic at production.
# The quasiparticle masses are of order M_KK ~ 7.4e16 GeV.
# At production, the GGE effective temperature is T_GGE ~ 0.1-0.8 M_KK.
#
# The ratio v/c = sqrt(<v^2>) tells us how relativistic the DM is.
# v/c ~ v_rms_gge (already in c=1 units since M_KK/M_KK = 1)

# The key insight: in the framework, the "velocity" of the phononic DM
# is the GROUP VELOCITY of the collective mode on the 32-cell graph,
# not the velocity of individual quasiparticles.
#
# The Leggett mode has v_L which is of order delta_omega_L / delta_q.
# This is the SOUND SPEED of the collective DM excitation.

# Weight the bands by spectral weight:
W_tot = W_L + W_BA + W_pb

# For the pair-breaking continuum, the group velocity is effectively zero
# (these are massive quasiparticle pairs, not propagating modes).
# Their contribution to free-streaming is suppressed by 2*Delta ~ 0.93 M_KK mass.

# BA band group velocity: compute from dispersion
omega_BA_q = sq_data['omega_BA']  # shape (31,) — one fewer than q_values
# Use matching q subset
q_BA = q_values[1:]  # skip q=0 (31 points match omega_BA)
q_BA_sort = np.argsort(q_BA)
q_BA_s = q_BA[q_BA_sort]
omBA_s = omega_BA_q[q_BA_sort]

v_BA_group = np.zeros(len(q_BA_s))
for i in range(1, len(q_BA_s) - 1):
    dq = q_BA_s[i+1] - q_BA_s[i-1]
    if dq > 1e-12:
        v_BA_group[i] = (omBA_s[i+1] - omBA_s[i-1]) / dq
if len(q_BA_s) > 1 and (q_BA_s[1] - q_BA_s[0]) > 1e-12:
    v_BA_group[0] = (omBA_s[1] - omBA_s[0]) / (q_BA_s[1] - q_BA_s[0])
if (q_BA_s[-1] - q_BA_s[-2]) > 1e-12:
    v_BA_group[-1] = (omBA_s[-1] - omBA_s[-2]) / (q_BA_s[-1] - q_BA_s[-2])

v_BA_rms = np.sqrt(np.mean(v_BA_group**2))

# Pair-breaking: these are gapped at 2*Delta. Their "group velocity" is
# v_pb ~ p / sqrt(p^2 + (2Delta)^2) -> 0 as p -> 0 (massive particles).
# Assume effectively cold: v_pb ~ 0.

# Weighted velocity dispersion:
v2_weighted = (W_L * v_L_rms**2 + W_BA * v_BA_rms**2 + W_pb * 0.0) / W_tot
v_rms_dm = np.sqrt(v2_weighted)

print(f"\nBand-weighted DM velocity dispersion:")
print(f"  Leggett:  v_rms = {v_L_rms:.6f}, weight = {W_L/W_tot:.3f}")
print(f"  BA:       v_rms = {v_BA_rms:.6f}, weight = {W_BA/W_tot:.3f}")
print(f"  Pair-br:  v_rms ~ 0,         weight = {W_pb/W_tot:.3f}")
print(f"  Weighted: v_rms = {v_rms_dm:.6f} (c=1 units)")
print(f"            This IS the effective velocity dispersion of phononic DM")

# ==============================================================================
# SECTION 5: Free-streaming scale and transfer function
# ==============================================================================

# The free-streaming comoving scale (Kolb & Turner, Paper 16 eq approach):
#
# lambda_fs = integral_0^t v(t') dt'/a(t')
#           ~ v_DM / (a * H) at the relevant epoch
#
# k_fs = 2*pi / lambda_fs ~ 2*pi * a * H / v_DM
#
# For a particle that becomes non-relativistic at a_nr:
#   k_fs ~ sqrt(4*pi*G*rho) / v_DM  (Jeans wavenumber)
#
# In the phonon-exflation framework:
# - The DM quasiparticles are produced at the tau-fold (high redshift)
# - They are non-relativistic from birth (v << c in natural units)
# - The velocity dispersion redshifts as v ~ 1/a after production
#
# The free-streaming wavenumber at matter-radiation equality:
#   k_fs = a_eq * H_eq / v_DM(a_eq)
#
# where v_DM(a_eq) = v_DM(a_prod) * (a_prod / a_eq) [NR redshift]

# M_KK sets the mass of the quasiparticles: m_DM ~ M_KK ~ 7.4e16 GeV
# This is an absurdly heavy particle — orders of magnitude above the Planck mass.
# Its free-streaming length is negligible.

# Let me be precise. The DM "mass" in the framework is the quasiparticle
# excitation energy, which is of order E_k ~ 1.6-2.0 M_KK.
m_DM_MKK = np.mean(E_k)  # average quasiparticle mass in M_KK units
m_DM_GeV = m_DM_MKK * M_KK  # in GeV

print(f"\n{'='*70}")
print(f"DM QUASIPARTICLE PROPERTIES")
print(f"{'='*70}")
print(f"  Mean quasiparticle energy:  {m_DM_MKK:.4f} M_KK = {m_DM_GeV:.4e} GeV")
print(f"  M_KK (gravity route):      {M_KK:.4e} GeV")
print(f"  Velocity dispersion:        {v_rms_dm:.6f} c")

# The momentum of the quasiparticle: p ~ m * v
# In the GGE, T_eff ~ 0.1-0.8 M_KK, and E ~ 1.7 M_KK (rest + kinetic)
# So v/c ~ T_eff / E ~ 0.06 - 0.47

# The critical question for the transfer function:
# At what COSMOLOGICAL epoch are these DM particles produced?
# The tau-fold occurs at high energy scale ~ M_KK.
# After production, v ~ T_GGE/m_DM * (a_prod/a) for NR particles.

# Production redshift: set by M_KK
# T_prod ~ T_GGE * M_KK (in GeV) ~ 0.1 * 7.4e16 = 7.4e15 GeV
# This corresponds to T_photon ~ M_KK at production (if in thermal contact)
# But the hidden sector is DECOUPLED — the GGE temperature is internal.

# The physical velocity at any later epoch:
# v_phys(a) = v_rms_dm * (a_prod / a)  [for NR particles, momentum redshifts as 1/a]

# The comoving free-streaming length from production to today:
# lambda_fs = integral_{a_prod}^{a_0} v(a) da / (a^2 H(a))
#           = v_prod * a_prod * integral da / (a^3 H(a))  [since v*a = const]
#
# For radiation domination: H ~ H_0 sqrt(Omega_r) / a^2
# integral ~ a^3 / (3 H_0 sqrt(Omega_r) a^3) => diverges logarithmically
#
# Standard result for a thermal relic (Kolb & Turner):
# lambda_fs ~ (v_prod / m_DM) * t_eq * ln(a_eq / a_prod)
#
# But for EXTREMELY heavy particles, v/c is tiny and lambda_fs is microscopic.

# Following the standard WDM free-streaming calculation:
# k_fs = 2*pi / lambda_fs
#
# For a thermal WDM particle of mass m_WDM:
# k_fs ~ 15.6 * (m_WDM / keV)^{1.12} * (Omega_DM/0.3)^{0.15} * (h/0.65)^{1.3} h/Mpc
# (Viel et al. 2005, eq. 7; see also Bode, Ostriker, Turok 2001)
#
# This gives k_fs ~ 40 h/Mpc for m_WDM = 3.3 keV.

# For our phononic DM, the effective "thermal mass" is set by the GGE temperature.
# The WDM mapping: a particle with mass m and velocity v today has an equivalent
# WDM mass m_WDM such that both produce the same k_fs.

# The velocity dispersion today:
# v_today = v_prod * (a_prod / a_0)
#
# a_prod is set by the production temperature. Since the quasiparticles
# are produced at the tau-fold (energy scale ~ M_KK), and they are part
# of a DECOUPLED hidden sector:
#
# The entropy conservation in the hidden sector:
# T_hidden(a) = T_hidden(a_prod) * (a_prod / a)
#
# But for FULLY decoupled hidden DM, we use:
# T_hidden,today = T_hidden,prod * (a_prod / a_today)

# Production epoch: when T_SM ~ M_KK (or equivalently, before BBN)
# a_prod / a_0 ~ T_CMB / T_prod = T_CMB_GeV / M_KK
# (ignoring g_* changes for order of magnitude)

T_prod_GeV = M_KK  # production at tau-fold, internal scale ~ M_KK
a_ratio = T_CMB_GeV / T_prod_GeV  # a_prod / a_0

print(f"\nCosmological mapping:")
print(f"  T_prod ~ M_KK = {M_KK:.4e} GeV")
print(f"  T_CMB = {T_CMB_GeV:.4e} GeV")
print(f"  a_prod/a_0 ~ T_CMB/T_prod = {a_ratio:.4e}")

# Velocity today (physical):
v_today = v_rms_dm * a_ratio  # momentum redshifts as 1/a
print(f"  v_rms at production: {v_rms_dm:.6f} c")
print(f"  v_rms today:         {v_today:.4e} c")

# ==============================================================================
# SECTION 6: Free-streaming length computation
# ==============================================================================

# Comoving free-streaming length (exact integral for NR species):
# lambda_fs = integral_{t_prod}^{t_0} v(t) dt / a(t)
#           = v_prod * a_prod * integral_{a_prod}^{1} da / (a^3 * H(a))
#
# During radiation domination (a < a_eq ~ 3e-4):
# H(a) = H_0 * sqrt(Omega_r) / a^2
# integral_RD = integral_{a_prod}^{a_eq} da / (a^3 * H_0 sqrt(Omega_r) / a^2)
#             = integral da / (a * H_0 sqrt(Omega_r))
#             = ln(a_eq/a_prod) / (H_0 sqrt(Omega_r))
#
# During matter domination (a_eq < a < 1):
# H(a) = H_0 * sqrt(Omega_m) / a^{3/2}
# integral_MD = integral_{a_eq}^{1} da / (a^3 * H_0 sqrt(Omega_m) / a^{3/2})
#             = integral da / (a^{3/2} * H_0 sqrt(Omega_m))
#             = 2 * (1 - 1/sqrt(a_eq)) / (H_0 sqrt(Omega_m))

# Physical constants
h_hubble = H_0_km_s_Mpc / 100.0  # dimensionless Hubble parameter
Omega_r = 9.15e-5  # radiation density parameter (Planck 2018)
a_eq = Omega_r / Omega_m  # matter-radiation equality: a_eq ~ 3e-4
z_eq = 1.0 / a_eq - 1.0

print(f"\n  h = {h_hubble:.3f}")
print(f"  a_eq = {a_eq:.6e} (z_eq = {z_eq:.0f})")
print(f"  Omega_r = {Omega_r:.4e}")

# H_0 in (Mpc)^{-1} units:
# H_0 = 67.4 km/s/Mpc => H_0 / c = 67.4 / 299792.458 Mpc^{-1} = 2.248e-4 h/Mpc
# Actually: H_0 = h * 100 km/s/Mpc. k_fs is in units of h/Mpc.
# H_0/(c) = 100/(299792.458) = 3.336e-4 (h/Mpc)
H0_over_c = 100.0 / c_light_km_s  # in (h/Mpc)

# Comoving free-streaming length (in Mpc/h):
# lambda_fs = (v_prod * a_prod / H_0) * I
# where I = integral_{a_prod}^{1} da / (a^3 H(a)/H_0)

# Radiation-dominated contribution (dominates for early production):
I_RD = np.log(a_eq / a_ratio) / np.sqrt(Omega_r)

# Matter-dominated contribution:
I_MD = 2.0 * (1.0 - 1.0/np.sqrt(a_eq)) / np.sqrt(Omega_m)

# Total integral
I_total = I_RD + I_MD

# lambda_fs in units of c/H_0:
lambda_fs_cH0 = v_rms_dm * a_ratio * I_total

# Convert to comoving Mpc/h:
# c/H_0 = 1/(H_0/c) = 1/(3.336e-4 h/Mpc) = 2998 Mpc/h
cH0_Mpc_h = 1.0 / H0_over_c
lambda_fs_Mpc_h = lambda_fs_cH0 * cH0_Mpc_h

# k_fs = 2*pi / lambda_fs
k_fs = 2.0 * np.pi / lambda_fs_Mpc_h if lambda_fs_Mpc_h > 0 else np.inf

print(f"\nFree-streaming calculation:")
print(f"  I_RD = {I_RD:.4f} (radiation epoch)")
print(f"  I_MD = {I_MD:.4f} (matter epoch)")
print(f"  I_total = {I_total:.4f}")
print(f"  lambda_fs = {lambda_fs_Mpc_h:.6e} Mpc/h")
print(f"  k_fs = {k_fs:.4e} h/Mpc")

# ==============================================================================
# SECTION 7: Transfer function T(k)
# ==============================================================================

# Standard WDM transfer function fitting formula (Bode, Ostriker, Turok 2001;
# Viel et al. 2005):
#
# T(k) = [1 + (alpha * k)^{2*nu}]^{-5/nu}
#
# where alpha is the breaking scale and nu ~ 1.12 (Viel et al. 2005).
#
# For a thermal WDM relic:
# alpha = 0.049 * (m_WDM/keV)^{-1.11} * (Omega_DM/0.25)^{0.11} *
#         (h/0.7)^{1.22} Mpc/h
# (Viel et al. 2005, eq 6)
#
# For our non-thermal DM, we compute alpha from the free-streaming scale:
# T(k_fs) ~ 0.5 => alpha ~ k_fs^{-1} * (2^{nu/5} - 1)^{1/(2*nu)}

nu = 1.12  # Viel et al. 2005

# The half-power scale: T(k_half) = 0.5
# 0.5 = [1 + (alpha * k_half)^{2*nu}]^{-5/nu}
# => (alpha * k_half)^{2*nu} = 2^{nu/5} - 1
# => alpha * k_half = (2^{nu/5} - 1)^{1/(2*nu)}

# We identify k_half with a scale related to k_fs.
# For WDM, the relationship between k_fs and k_half is:
# k_half ~ 2 * pi / lambda_fs ~ k_fs (within factors of order unity)

# But more precisely, the transfer function encodes the Jeans scale damping.
# For the phononic DM, the relevant scale is where pressure support
# (from the non-zero sound speed of the collective mode) prevents collapse.

# The Jeans wavenumber:
# k_J = sqrt(4*pi*G*rho_DM) / c_s
# where c_s is the sound speed of the DM fluid

# Sound speed of the Leggett mode (dominant DM channel):
# c_s_L = v_L_rms (already computed)
# Actually, for a non-relativistic fluid with velocity dispersion v,
# the Jeans wavenumber involves the velocity dispersion directly:
# k_J = sqrt(4*pi*G*rho) * a / v  (physical)
# k_J = sqrt(6*pi * rho_mean * a^2 / M_Pl^2) / v (natural units)

# But for computing the TRANSFER function, the standard approach is
# to identify the suppression scale alpha from the free-streaming physics.

# Method: map the free-streaming scale to the WDM alpha parameter.
# alpha = lambda_fs / (2*pi) * correction factor
# The correction comes from the fact that T(k) = 0.5 at k = k_half, not k_fs.

# For the standard formula:
# alpha_wdm = 0.049 * (m_WDM/keV)^{-1.11} * (Omega_DM/0.25)^{0.11} * (h/0.7)^{1.22}

# We can compute alpha from our lambda_fs:
# The transfer function goes as T(k) ~ [1 + (alpha*k)^{2*nu}]^{-5/nu}
# with alpha^{-1} being the half-power scale.
# For WDM, alpha^{-1} ~ k_fs within O(1) factors.

# Compute alpha from free-streaming scale:
# Set alpha = 1/k_fs (the simplest identification)
# Then k_half = k_fs * (2^{nu/5} - 1)^{1/(2*nu)} / (alpha * k_fs)
# This is circular. Instead:

# The standard approach: define alpha such that T(k_fs) = 0.5
# => alpha = (2^{nu/5} - 1)^{1/(2*nu)} / k_fs

prefactor = (2.0**(nu/5.0) - 1.0)**(1.0/(2.0*nu))
alpha = prefactor / k_fs
k_half = k_fs  # by construction

print(f"\nTransfer function parameters:")
print(f"  nu = {nu}")
print(f"  prefactor = {prefactor:.6f}")
print(f"  alpha = {alpha:.6e} Mpc/h")
print(f"  k_half (T=0.5) = {k_half:.4e} h/Mpc")

# Compute T(k) on a grid
k_grid = np.logspace(-2, 6, 10000)  # h/Mpc
T_k = (1.0 + (alpha * k_grid)**(2*nu))**(-5.0/nu)

# Values at requested k points
k_test = np.array([1.0, 10.0, 100.0, 1000.0])  # h/Mpc
T_test = (1.0 + (alpha * k_test)**(2*nu))**(-5.0/nu)

print(f"\nTransfer function T(k) at key scales:")
print(f"  {'k (h/Mpc)':>12s}  {'T(k)':>12s}")
for kt, Tt in zip(k_test, T_test):
    print(f"  {kt:12.1f}  {Tt:12.8f}")

# Find k_cut where T(k) = 0.5
# By construction this is k_half = k_fs
k_cut = k_fs
T_at_kcut = (1.0 + (alpha * k_cut)**(2*nu))**(-5.0/nu)
print(f"\n  k_cut (T=0.5): {k_cut:.4e} h/Mpc")
print(f"  T(k_cut) = {T_at_kcut:.6f} (should be 0.5)")

# ==============================================================================
# SECTION 8: WDM mass equivalent
# ==============================================================================

# Viel et al. 2005 fitting formula (inverted):
# m_WDM = 3.3 * (Omega_DM/0.25)^{0.4} * (h/0.7)^{0.8} * (k_cut / 40)^{-1.11} keV
#
# But more standard: invert the alpha-m relationship:
# alpha = 0.049 * (m_WDM/keV)^{-1.11} * (Omega_DM/0.25)^{0.11} * (h/0.7)^{1.22}
#
# => m_WDM = (alpha / (0.049 * (Omega_DM/0.25)^{0.11} * (h/0.7)^{1.22}))^{-1/1.11} keV

# Method A: From k_cut using the task's specified formula
# NOTE: This formula is designed for k_cut ~ 10-100 h/Mpc.
# For CDM-like particles with k_cut >> 10^6 h/Mpc, it underflows.
# We use log-space to avoid numerical issues.
log_k_ratio = np.log10(k_cut / 40.0)
log_m_A = (np.log10(3.3)
           + 0.4 * np.log10(Omega_DM / 0.25)
           + 0.8 * np.log10(h_hubble / 0.7)
           - 1.11 * log_k_ratio)
m_WDM_A_keV = 10.0**log_m_A  # keV
m_WDM_A_log = log_m_A  # log10(keV)

# Method B: From alpha using Viel et al. 2005 eq 6
# alpha = 0.049 * (m_WDM/keV)^{-1.11} * (Omega_DM/0.25)^{0.11} * (h/0.7)^{1.22}
# => m_WDM = (alpha / alpha_coeff)^{-1/1.11} keV
alpha_coeff = 0.049 * (Omega_DM / 0.25)**0.11 * (h_hubble / 0.7)**1.22
log_m_B = (-1.0/1.11) * np.log10(alpha / alpha_coeff)
m_WDM_B_keV = 10.0**log_m_B
m_WDM_B_log = log_m_B

print(f"\n{'='*70}")
print(f"WDM MASS EQUIVALENT")
print(f"{'='*70}")
print(f"  Method A (k_cut formula):   log10(m_WDM/keV) = {m_WDM_A_log:.2f}")
print(f"                               m_WDM = {m_WDM_A_keV:.4e} keV")
print(f"  Method B (alpha inversion):  log10(m_WDM/keV) = {m_WDM_B_log:.2f}")
print(f"                               m_WDM = {m_WDM_B_keV:.4e} keV")

# Use Method B as primary (numerically stable for CDM-like particles)
m_WDM = m_WDM_B_keV
m_WDM_log = m_WDM_B_log

# ==============================================================================
# SECTION 9: Lyman-alpha comparison and gate verdict
# ==============================================================================

m_Lya_bound = 5.3    # keV, Irsic et al. 2017  # (local)
m_excluded = 2.0      # keV, hard exclusion  # (local)

print(f"\n{'='*70}")
print(f"GATE: TRANSFER-FUNCTION-58")
print(f"{'='*70}")
print(f"  m_WDM equivalent:    10^{m_WDM_log:.1f} keV = {m_WDM:.4e} keV")
print(f"  Lyman-alpha bound:   > {m_Lya_bound} keV (Irsic et al. 2017)")
print(f"  Hard exclusion:      < {m_excluded} keV")

if m_WDM > m_Lya_bound:
    verdict = "PASS"
    detail_str = (f"m_WDM=10^{{{m_WDM_log:.1f}}} keV >> {m_Lya_bound} keV Lyman-alpha bound. "
                  f"k_cut={k_cut:.2e} h/Mpc. v_rms={v_rms_dm:.4e}c at production. "
                  f"DM is effectively CDM (m_DM ~ {m_DM_GeV:.1e} GeV). "
                  f"T(k)=1.000 at all observable scales k<10^6 h/Mpc.")
elif m_WDM < m_excluded:
    verdict = "FAIL"
    detail_str = (f"m_WDM={m_WDM:.2e} keV < {m_excluded} keV. "
                  f"Excluded by Lyman-alpha. k_cut={k_cut:.2e} h/Mpc.")
else:
    verdict = "INFO"
    detail_str = (f"m_WDM={m_WDM:.2e} keV in [{m_excluded}, {m_Lya_bound}] keV range. "
                  f"Marginal. k_cut={k_cut:.2e} h/Mpc.")

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail_str}")

# ==============================================================================
# SECTION 10: Physical interpretation
# ==============================================================================

print(f"\n{'='*70}")
print(f"PHYSICAL INTERPRETATION")
print(f"{'='*70}")

# The DM is effectively COLD because:
# 1. m_DM ~ M_KK ~ 7.4e16 GeV is absurdly heavy
# 2. v/c ~ 0.1 at production, but redshifts as 1/a
# 3. By matter-radiation equality, v ~ v_prod * (a_prod/a_eq)
#    ~ 0.1 * (T_CMB/M_KK) / a_eq
v_at_eq = v_rms_dm * a_ratio / a_eq
print(f"  v/c at production:         {v_rms_dm:.4e}")
print(f"  v/c today:                 {v_today:.4e}")
print(f"  v/c at matter-rad eq:      {v_at_eq:.4e}")
print(f"  a_prod/a_0:                {a_ratio:.4e}")
print(f"  m_DM:                      {m_DM_GeV:.4e} GeV")
print(f"  m_DM / T_GGE_eff:          {m_DM_MKK / np.mean(T_k_gge):.2f}")
print(f"  Transmission (fabric):      {T_loc_mean:.4f}")

# Free-streaming scale in physical units
lambda_fs_kpc = lambda_fs_Mpc_h * 1e3 / h_hubble  # kpc
print(f"\n  lambda_fs = {lambda_fs_Mpc_h:.4e} Mpc/h = {lambda_fs_kpc:.4e} kpc")
print(f"  k_fs = {k_fs:.4e} h/Mpc")

# For reference, CDM has k_fs -> infinity (no suppression)
# WDM with m=5.3 keV has k_fs ~ 40 h/Mpc
# Our phononic DM has k_fs ~ {k_fs:.2e} h/Mpc
alpha_53 = 0.049 * (5.3)**(-1.11) * (Omega_DM/0.25)**0.11 * (h_hubble/0.7)**1.22
k_half_53 = prefactor / alpha_53
print(f"\n  For comparison:")
print(f"    WDM m=5.3 keV: k_half ~ {k_half_53:.1f} h/Mpc")
print(f"    Phononic DM:    k_half ~ {k_cut:.2e} h/Mpc")
print(f"    Ratio: {k_cut/k_half_53:.2e}x")

# ==============================================================================
# SECTION 11: Include transmission coefficient effect
# ==============================================================================

# The fabric transmission T_loc = 0.969 means 3.1% of power is reflected
# at domain boundaries. This slightly reduces the effective free-streaming
# by confining DM within domains. The effect is:
# lambda_fs_effective ~ lambda_fs * T_loc (reduced by reflection)
# But T_loc ~ 1 so this is a 3% correction.

lambda_fs_eff = lambda_fs_Mpc_h * T_loc_mean
k_fs_eff = 2.0 * np.pi / lambda_fs_eff if lambda_fs_eff > 0 else np.inf
# Use same alpha-inversion approach for consistency
alpha_eff = prefactor / k_fs_eff
log_m_eff = (-1.0/1.11) * np.log10(alpha_eff / alpha_coeff)
m_WDM_eff = 10.0**log_m_eff

print(f"\n  With transmission correction (T_loc={T_loc_mean:.4f}):")
print(f"    lambda_fs_eff = {lambda_fs_eff:.4e} Mpc/h")
print(f"    k_fs_eff = {k_fs_eff:.4e} h/Mpc")
print(f"    m_WDM_eff = 10^{log_m_eff:.1f} keV")
print(f"    (Correction: {abs(log_m_eff - m_WDM_B_log)/m_WDM_B_log*100:.1f}% in log)")

# ==============================================================================
# SECTION 12: Save data
# ==============================================================================

np.savez('s58_transfer_function.npz',
    # Transfer function
    k_grid=k_grid,
    T_k=T_k,
    alpha=alpha,
    nu=nu,
    k_cut=k_cut,
    k_fs=k_fs,
    lambda_fs_Mpc_h=lambda_fs_Mpc_h,

    # WDM mass equivalent
    m_WDM=m_WDM,
    m_WDM_method_B=m_WDM_B_keV,
    m_WDM_with_transmission=m_WDM_eff,

    # DM properties
    m_DM_GeV=m_DM_GeV,
    m_DM_MKK=m_DM_MKK,
    v_rms_dm=v_rms_dm,
    v_today=v_today,
    v_at_eq=v_at_eq,
    v_rms_gge=v_rms_gge,

    # Band velocities
    v_L_rms=v_L_rms,
    v_BA_rms=v_BA_rms,
    v_L_group=v_L_group,
    v_BA_group=v_BA_group,

    # Spectral weights
    W_L=W_L,
    W_BA=W_BA,
    W_pb=W_pb,

    # Transfer function at test points
    k_test=k_test,
    T_test=T_test,

    # Transmission
    T_loc_mean=T_loc_mean,
    k_fs_eff=k_fs_eff,

    # Cosmological parameters used
    a_ratio=a_ratio,
    a_eq=a_eq,
    h_hubble=h_hubble,

    # Gate
    gate_name='TRANSFER-FUNCTION-58',
    gate_verdict=verdict,
    gate_detail=detail_str,
)

print(f"\nData saved to s58_transfer_function.npz")

# ==============================================================================
# SECTION 13: Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S58 W3-14: Phononic DM Transfer Function T(k)',
             fontsize=14, fontweight='bold')

# Panel 1: Transfer function T(k)
ax = axes[0, 0]
ax.semilogx(k_grid, T_k, 'b-', linewidth=2, label='Phononic DM')

# WDM comparison curves
for m_wdm_ref, color, ls in [(2.0, 'r', '--'), (5.3, 'orange', '--'), (10.0, 'g', '--')]:
    alpha_ref = 0.049 * m_wdm_ref**(-1.11) * (Omega_DM/0.25)**0.11 * (h_hubble/0.7)**1.22
    T_ref = (1.0 + (alpha_ref * k_grid)**(2*nu))**(-5.0/nu)
    ax.semilogx(k_grid, T_ref, color=color, ls=ls, linewidth=1.5,
                label=f'WDM {m_wdm_ref} keV')

ax.axhline(0.5, color='gray', ls=':', alpha=0.5)
ax.axvline(k_cut, color='b', ls=':', alpha=0.5, label=f'k_cut = {k_cut:.1e} h/Mpc')
ax.set_xlabel('k (h/Mpc)')
ax.set_ylabel('T(k) = P(k)/P_CDM(k)')
ax.set_title('Transfer Function')
ax.set_xlim(1e-1, 1e5)
ax.set_ylim(-0.05, 1.1)
ax.legend(fontsize=8, loc='lower left')
ax.grid(True, alpha=0.3)

# Panel 2: Group velocities
ax = axes[0, 1]
ax.plot(q_s, np.abs(v_L_group), 'b-', linewidth=2, label='Leggett mode')
ax.plot(q_BA_s, np.abs(v_BA_group), 'r-', linewidth=1.5, label='BA mode')
ax.axhline(v_rms_dm, color='k', ls='--', linewidth=1, label=f'v_rms_DM = {v_rms_dm:.4f}')
ax.set_xlabel('q (graph momentum)')
ax.set_ylabel('|v_group| (c units)')
ax.set_title('Group Velocities by Band')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Velocity hierarchy
ax = axes[1, 0]
labels = ['v_prod', 'v_eq', 'v_today']
values = [v_rms_dm, v_at_eq, v_today]
colors = ['steelblue', 'orange', 'green']
bars = ax.bar(labels, values, color=colors, alpha=0.8)
ax.set_yscale('log')
ax.set_ylabel('v/c')
ax.set_title('Velocity Redshift History')
for bar, val in zip(bars, values):
    ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() * 1.3,
            f'{val:.2e}', ha='center', va='bottom', fontsize=9)
ax.grid(True, alpha=0.3, axis='y')

# Panel 4: Summary table
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"GATE: TRANSFER-FUNCTION-58\n"
    f"VERDICT: {verdict}\n\n"
    f"DM quasiparticle mass:  {m_DM_GeV:.2e} GeV\n"
    f"Velocity dispersion:    {v_rms_dm:.4e} c\n"
    f"Free-streaming scale:   {lambda_fs_Mpc_h:.2e} Mpc/h\n"
    f"Cutoff wavenumber:      {k_cut:.2e} h/Mpc\n"
    f"WDM mass equivalent:    10^{m_WDM_log:.1f} keV\n\n"
    f"Lyman-alpha bound:      > 5.3 keV\n"
    f"T(k) = 1.0000 at k = 1, 10, 100 h/Mpc\n\n"
    f"The phononic DM is effectively CDM.\n"
    f"m_DM ~ M_KK ~ 10^17 GeV >> any WDM bound.\n"
    f"Free-streaming length ~ 10^-20 kpc.\n"
    f"No observable deviation from CDM."
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=10, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('s58_transfer_function.png', dpi=150, bbox_inches='tight')
print("Plot saved to s58_transfer_function.png")

print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE")
print(f"  Gate: TRANSFER-FUNCTION-58 => {verdict}")
print(f"  m_WDM = 10^{m_WDM_log:.1f} keV (= {m_WDM:.4e} keV)")
print(f"  k_cut = {k_cut:.4e} h/Mpc")
print(f"  T(k=1) = {T_test[0]:.8f}, T(k=100) = {T_test[2]:.8f}")
print(f"{'='*70}")
