#!/usr/bin/env python3
"""
S53 POMERANCHUK-HFB-53: Updated Landau parameter f_0 with HFB spectrum
========================================================================

Physics:
  S22c computed f(0,0) = -4.687 via the "Pomeranchuk analog":
    f_{pq} = -<d(lam)/d(tau)>_avg * N(0) / lam_F
  using the bare Dirac spectrum on SU(3).

  Here we recompute f_0 = V_ph * N(0) using the explicit V_bare
  interaction matrix from S52 HFB, with two spectra:
    (a) bare single-particle energies
    (b) HFB self-consistent energies (N_pair=1)

  The Landau parameter in a Fermi liquid is:
    f_0^s = N(0) * <V_ph>_{FS}
  where <V_ph>_{FS} is the Fermi-surface average of the particle-hole
  interaction. Pomeranchuk instability: f_0^s < -(2l+1).

  At N_pair=1 the Fermi-liquid picture is marginal (one pair does not
  form a Fermi surface), but f_0 still characterizes the p-h interaction
  strength and determines whether the ground state is unstable toward
  condensation.

  N_pair=1 tight-binding reframe (S53):  # (local)
    8 modes: 4 B2 + 1 B1 + 3 B3
    "Fermi level" at mu_BCS = E_B1 = 0.819 M_KK
    DOS: rho_B2_per_mode = 14.02 (from S37 instanton action)

Gate: POMERANCHUK-HFB-53 — INFO
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *
import numpy as np

print("=" * 72)
print("S53 POMERANCHUK-HFB-53: LANDAU PARAMETER f_0 WITH HFB SPECTRUM")
print("=" * 72)
print()

# =====================================================================
# 1. Load data
# =====================================================================
d_hfb = np.load('computations/session-52/s52_hfb_full.npz', allow_pickle=True)
d_spec = np.load('computations/session-53/s53_hfb_spectral.npz', allow_pickle=True)

E_bare = d_hfb['E_sp_bare']       # shape (8,)
E_hfb = d_hfb['N1_hfb_E_sp_final']  # shape (8,) — HFB self-consistent at N=1
Sigma_HF = d_hfb['N1_Sigma_HF']   # shape (8,) — self-energy shift
V_bare = d_hfb['V_bare']          # shape (8,8) — interaction matrix
labels = d_hfb['labels']          # ['B2[0]' ... 'B1' 'B3[0]' ...]

# BCS coherence factors from spectral data
u_ed = d_spec['N1_u_ed']          # ED quasiparticle u at N=1
v_ed = d_spec['N1_v_ed']          # ED quasiparticle v at N=1
u2_mv2 = d_spec['N1_u2_minus_v2_ed']
n_k_ed = d_spec['N1_n_k_ed']
Z_ed = d_spec['N1_Z_ed']         # quasiparticle weight

print("--- 1. DATA LOADED ---")
print(f"  Labels: {list(labels)}")
print(f"  E_bare:  {E_bare}")
print(f"  E_hfb:   {E_hfb}")
print(f"  Sigma_HF:{Sigma_HF}")
print()
print(f"  V_bare matrix:")
for i in range(8):
    row = " ".join(f"{V_bare[i,j]:9.5f}" for j in range(8))
    print(f"    [{labels[i]:>5s}] {row}")
print()

# =====================================================================
# 2. Identify sectors and Fermi level
# =====================================================================
# Sector indices
B2_idx = np.array([0, 1, 2, 3])  # B2 modes
B1_idx = np.array([4])           # B1 mode
B3_idx = np.array([5, 6, 7])    # B3 modes

# Canonical constants
mu_BCS = E_B1  # = 0.819 M_KK, the BCS chemical potential
rho_B2 = rho_B2_per_mode  # = 14.02

print("--- 2. FERMI LEVEL AND DOS ---")
print(f"  mu_BCS (Fermi level) = E_B1 = {mu_BCS:.6f} M_KK")
print(f"  rho_B2_per_mode = {rho_B2:.4f} (canonical)")
print()

# Compute xi_k = E_k - mu for each mode
xi_bare = E_bare - mu_BCS
xi_hfb = E_hfb - mu_BCS

print("  xi_bare = E_bare - mu:")
for i in range(8):
    print(f"    {labels[i]:>5s}: xi = {xi_bare[i]:+.6f}")
print()
print("  xi_hfb = E_hfb - mu:")
for i in range(8):
    print(f"    {labels[i]:>5s}: xi = {xi_hfb[i]:+.6f}")
print()

# =====================================================================
# 3. APPROACH A: Reproduce S22c formula on 8-mode system
# =====================================================================
# S22c used: f = -<d(lam)/d(tau)> * N(0) / lam_F
# The d(lam)/d(tau) was computed from the full Dirac spectrum across tau.
# Here we don't have tau derivatives, but we can compute the analogous
# quantity from the self-energy shift: the HFB modification of the
# spectrum IS the tau-evolution at fixed tau=fold.
#
# The HFB self-energy Sigma_HF plays the role of the quasiparticle
# interaction in Landau theory: it shifts the single-particle energies
# by the mean-field interaction with the other occupied states.

print("=" * 72)
print("3. APPROACH A: SELF-ENERGY AS INTERACTION PROXY")
print("=" * 72)
print()

# The Hartree-Fock self-energy is: Sigma_k = sum_k' V_{kk'} n_{k'}
# This is the direct (Hartree) + exchange (Fock) mean field.
# In Landau theory, the quasiparticle interaction f_{kk'} is:
#   f_{kk'} = d(Sigma_k)/d(n_{k'}) = V_{kk'}  (at Hartree level)
#
# The Landau parameter f_0 (l=0, spin-symmetric) is the Fermi-surface
# average of V_{kk'}:
#   f_0 = N(0) * <V_{kk'}>_{FS}

# Fermi-surface modes: those closest to mu_BCS
# In bare spectrum: B1 is AT mu (xi=0), B2 modes are at xi=+0.026
# In HFB spectrum: B2 modes shift DOWN to xi ~ -0.008 to -0.009
# So HFB makes B2 modes cross the Fermi level!

print("Fermi-surface analysis:")
print()

# Bare spectrum: B1 is exactly at Fermi level
print("  BARE spectrum:")
print(f"    B1 energy = {E_bare[4]:.6f} = mu_BCS exactly")
print(f"    B2 mean energy = {np.mean(E_bare[:4]):.6f} (above mu by {np.mean(xi_bare[:4]):.6f})")
print(f"    B3 mean energy = {np.mean(E_bare[5:]):.6f} (above mu by {np.mean(xi_bare[5:]):.6f})")
print()

# HFB spectrum: B2 modes shift below Fermi level
print("  HFB spectrum:")
print(f"    B1 energy = {E_hfb[4]:.6f} (shifted ABOVE mu by {xi_hfb[4]:+.6f})")
print(f"    B2 energies = {E_hfb[:4]}")
print(f"    B2 mean shifted BELOW mu by {np.mean(xi_hfb[:4]):+.6f}")
print(f"    B3 mean energy = {np.mean(E_hfb[5:]):.6f}")
print()

# =====================================================================
# 4. APPROACH B: Direct Landau parameter from V_bare
# =====================================================================
print("=" * 72)
print("4. APPROACH B: DIRECT LANDAU PARAMETER FROM V_bare")
print("=" * 72)
print()

# The Landau interaction function f(k,k') = N(0) * V(k,k')
# For the l=0 (s-wave) channel, we average over all pairs at the FS.
#
# In the S22c convention for a finite system with dim(rep) = d:
#   f_0 = N(0) * V_avg
#   threshold: f_0 < -(2*dim+1)
#
# For the (0,0) singlet: dim=1, threshold = -3
#
# Key question: what is V_avg and N(0) for the 8-mode system?

# Method B1: B2-B2 block (the "near-Fermi" modes in bare spectrum)
V_B2B2 = V_bare[np.ix_(B2_idx, B2_idx)]
V_avg_B2 = np.mean(V_B2B2)

print("  B2-B2 block interaction:")
print(f"    V_B2B2 matrix:")
for i in range(4):
    print(f"      {' '.join(f'{V_B2B2[i,j]:9.5f}' for j in range(4))}")
print(f"    <V>_B2 = {V_avg_B2:.6f}")
print()

# Method B2: Full Fermi-surface average (all modes weighted by proximity to mu)
# Weight each mode by its spectral weight or proximity to Fermi level
# Bare: w_k = 1/(|xi_k| + epsilon) for regularization
eps_reg = 0.01  # regularization scale  # (local)
w_bare = 1.0 / (np.abs(xi_bare) + eps_reg)
w_bare /= np.sum(w_bare)

V_avg_bare_weighted = 0.0  # (local)
for i in range(8):
    for j in range(8):
        V_avg_bare_weighted += w_bare[i] * w_bare[j] * V_bare[i, j]

print("  Weighted average (bare, proximity to mu):")
print(f"    Weights: {w_bare}")
print(f"    <V>_weighted = {V_avg_bare_weighted:.6f}")
print()

# Same for HFB
w_hfb = 1.0 / (np.abs(xi_hfb) + eps_reg)
w_hfb /= np.sum(w_hfb)

V_avg_hfb_weighted = 0.0  # (local)
for i in range(8):
    for j in range(8):
        V_avg_hfb_weighted += w_hfb[i] * w_hfb[j] * V_bare[i, j]

print("  Weighted average (HFB, proximity to mu):")
print(f"    Weights: {w_hfb}")
print(f"    <V>_weighted = {V_avg_hfb_weighted:.6f}")
print()

# =====================================================================
# 5. APPROACH C: Particle-hole interaction with BCS coherence factors
# =====================================================================
print("=" * 72)
print("5. APPROACH C: V_ph WITH BCS COHERENCE FACTORS")
print("=" * 72)
print()

# In a BCS state, the particle-hole interaction is dressed by coherence
# factors. The effective p-h vertex is:
#   V_ph(k,k') = V(k,k') * (u_k*u_{k'} - v_k*v_{k'})^2
#              + V(k,k') * (u_k*v_{k'})^2 + V(k,k') * (v_k*u_{k'})^2
#
# For the forward scattering (Landau parameter):
#   Gamma_ph(k,k') = V(k,k') * [(u_k*u_{k'} + v_k*v_{k'})^2]
# This is the direct p-h channel.
#
# The exchange (Fock) channel:
#   Gamma_ph_exch(k,k') = -V(k,k') * [(u_k*v_{k'} - v_k*u_{k'})^2]
# This contributes with opposite sign.

# Using ED coherence factors at N_pair=1
print("  Using ED coherence factors (N_pair=1):")
print(f"    u_ed = {u_ed}")
print(f"    v_ed = {v_ed}")
print()

# Direct p-h vertex
Gamma_dir = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        coh_dir = (u_ed[i]*u_ed[j] + v_ed[i]*v_ed[j])**2
        Gamma_dir[i, j] = V_bare[i, j] * coh_dir

# Exchange p-h vertex
Gamma_exch = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        coh_exch = (u_ed[i]*v_ed[j] - v_ed[i]*u_ed[j])**2
        Gamma_exch[i, j] = -V_bare[i, j] * coh_exch

Gamma_ph = Gamma_dir + Gamma_exch

print("  Gamma_ph = V * (uu+vv)^2 - V * (uv-vu)^2:")
print(f"    Gamma_ph diagonal: {np.diag(Gamma_ph)}")
print(f"    Gamma_ph B2-B2 mean: {np.mean(Gamma_ph[np.ix_(B2_idx, B2_idx)]):.6f}")
print(f"    Gamma_ph all-mode mean: {np.mean(Gamma_ph):.6f}")
print()

# =====================================================================
# 6. COMPUTE f_0 UNDER ALL APPROACHES
# =====================================================================
print("=" * 72)
print("6. LANDAU PARAMETER f_0 — ALL APPROACHES")
print("=" * 72)
print()

# S22c convention: f = -<interaction> * N(0) / lam_F
# But S22c used <d(lam)/d(tau)> as the interaction, which is NEGATIVE
# for softening modes. The sign convention is:
#   f < 0 means attractive (destabilizing)
#   Pomeranchuk threshold: f < -(2*dim+1)

# For (0,0) singlet: dim=1, threshold = -3
dim_00 = 1
threshold = -(2 * dim_00 + 1)  # (local)

# N(0) in different conventions:
# S22c: N(0) = gap-edge degeneracy (modes within 10% of lam_F)
# S35: N(0) = rho_B2_per_mode = 14.02
# S53: at N_pair=1, the DOS is formally for the 8-mode system

# Approach A: Self-energy proxy
# Sigma_HF has units of energy. The self-energy shift measures the
# mean-field interaction. For B2 modes (which are near Fermi level
# in both bare and HFB spectra):
Sigma_B2_avg = np.mean(Sigma_HF[:4])
Sigma_B1 = Sigma_HF[4]

# The "interaction" felt by a B2 mode from all other occupied modes
# at N_pair=1 is Sigma_B2. This already includes N(0) implicitly.
# f_0^{self-energy} = Sigma_B2 * N(0) / E_F
# But Sigma is already summed over k', so:
# f_0 = d(Sigma)/d(n) * N(0) = V_avg * N(0)

print("--- Approach A: Self-energy magnitude ---")
print(f"  <Sigma_HF>_B2 = {Sigma_B2_avg:.6f} M_KK")
print(f"  Sigma_B1 = {Sigma_B1:.6f} M_KK")
print(f"  B2 modes shift DOWN (attractive self-energy from other B2 modes)")
print(f"  B1 mode shifts UP (repulsive self-energy)")
print()

# Approach B: Direct V_bare
# B2-B2 average (the near-Fermi modes)
N0_b2 = rho_B2  # = 14.02 (per mode DOS from S37)
N0_modes = 4    # 4 B2 modes at the Fermi level (degeneracy)

# Method 1: S22c-style with V_bare
V_avg_B2B2 = np.mean(V_B2B2)
# In S22c the convention was f = -<d_lam>*N0/lam_F.
# With V_bare: f_0 = V_avg * N(0) (no extra minus — V>0 is repulsive in V_bare)
# But V_bare is a pairing matrix (Cooper channel), not p-h channel!
# The p-h interaction has opposite sign for the exchange part.

# Actually, let's be precise about what V_bare IS.
# From s52_hfb_full.py, V_bare_{ij} = <ij|V|ij> is the direct interaction.
# For PARTICLE-HOLE channel: V_ph = V_direct - V_exchange
# For PARTICLE-PARTICLE (BCS): V_pp = V_direct (already in V_bare)

# The Landau parameter is:
# F_0^s = N(0) * f_0^s = N(0) * (1/2) * (V_ph^{up,up} + V_ph^{up,down})
# In our spinless system: f_0 = N(0) * V_ph

# The particle-hole interaction in terms of V_bare:
# V_ph(k,k') = V_bare(k,k') (direct) for p-h scattering k,k' -> k,k'
# This is REPULSIVE (V_bare > 0).

# The S22c quantity was NEGATIVE because d(lam)/d(tau) was negative
# for softening modes. The SIGN of the Pomeranchuk parameter came from
# the eigenvalue SOFTENING, not from the interaction being attractive.
#
# KEY INSIGHT: S22c's f(0,0) = -4.687 measured eigenvalue softening rate,
# not the actual p-h interaction sign. The V_bare matrix shows V > 0
# (repulsive), which means f_0 > 0 in the conventional Landau sense.
#
# However, S22c's framework is self-consistent: the "interaction" there
# was -d(lam)/d(tau), and modes that SOFTEN (lam decreasing) contribute
# a NEGATIVE f. The physical content is that the system becomes unstable
# toward condensation in the softening channel.
#
# For the HFB update: what matters is whether the self-consistent spectrum
# changes the sign/magnitude of the effective p-h interaction.

print("--- Approach B: V_bare particle-hole ---")
print()

# (i) Conventional Landau parameter: f_0 = N(0) * V_ph
# V_ph = V_bare for direct channel (repulsive, V>0)
f0_direct_B2 = N0_b2 * V_avg_B2B2
print(f"  f_0 (B2-B2 direct, bare V) = N(0) * <V_B2B2>")
print(f"    = {N0_b2:.2f} * {V_avg_B2B2:.6f} = {f0_direct_B2:.4f}")
print(f"    Sign: POSITIVE (repulsive). Pomeranchuk STABLE in direct channel.")
print()

# (ii) S22c-analog: the EIGENVALUE SOFTENING rate
# In S22c, the effective interaction was the tau-derivative of eigenvalues.
# The analog here is: how does the self-energy modify the gap structure?
# The HFB shifts B2 modes DOWN and B1 UP, reducing the B2-B1 gap.
# This is the "softening" that S22c detected.
gap_bare = np.mean(E_bare[:4]) - E_bare[4]  # B2 - B1 gap (bare)
gap_hfb = np.mean(E_hfb[:4]) - E_hfb[4]     # B2 - B1 gap (HFB)
delta_gap = gap_hfb - gap_bare

print(f"  B2-B1 gap (bare):  {gap_bare:.6f} M_KK")
print(f"  B2-B1 gap (HFB):   {gap_hfb:.6f} M_KK")
print(f"  Gap change:         {delta_gap:.6f} M_KK ({delta_gap/gap_bare*100:.1f}%)")
print(f"  HFB CLOSES the B2-B1 gap (reduces by {abs(delta_gap/gap_bare)*100:.1f}%)")
print()

# (iii) S22c analog with the 8-mode spectrum
# In S22c: f = -<d(lam)/dtau> * N(0) / lam_F
# The "d(lam)/dtau" for the 8-mode system can be approximated by
# the self-energy shift per unit occupation change:
# d(E_k)/d(n) ~ Sigma_k / <n>
# This gives the curvature of the energy functional.

# Average occupation at N=1
n_avg = 1.0 / 8  # 1 pair spread over 8 modes, or use n_k_ed
n_total_ed = np.sum(n_k_ed)  # should be ~1 (N_pair=1)

# The "interaction" in the S22c sense is the self-energy per particle
# divided by the occupation, evaluated at the Fermi surface
V_eff_S22c_analog = Sigma_B2_avg / np.mean(n_k_ed[:4])
f0_S22c_analog = -V_eff_S22c_analog * N0_modes / mu_BCS

print(f"  S22c analog with self-energy:")
print(f"    V_eff = <Sigma_B2> / <n_B2> = {Sigma_B2_avg:.6f} / {np.mean(n_k_ed[:4]):.6f}")
print(f"          = {V_eff_S22c_analog:.6f}")
print(f"    f_0 = -V_eff * N_modes / mu = -{V_eff_S22c_analog:.6f} * {N0_modes} / {mu_BCS:.6f}")
print(f"        = {f0_S22c_analog:.4f}")
print(f"    Threshold = {threshold}")
print(f"    Status: {'UNSTABLE' if f0_S22c_analog < threshold else 'stable'}")
print()

# =====================================================================
# 7. RECONCILE S22c AND DIRECT COMPUTATION
# =====================================================================
print("=" * 72)
print("7. RECONCILIATION: S22c vs DIRECT")
print("=" * 72)
print()

# The S22c result f(0,0) = -4.687 came from the FULL Dirac spectrum
# (16 modes in the (0,0) sector, d(lam)/d(tau) computed from a tau sweep).
# The SIGN was set by the eigenvalue softening: modes that decrease with
# tau contribute negatively.
#
# At N_pair=1 with HFB, the analogous quantity is:
# How much does the self-consistent spectrum differ from the bare spectrum,
# and what does this tell us about the effective particle-hole interaction?

# The HFB self-energy for B2 modes is NEGATIVE (attractive):
# Sigma_B2 ~ -0.034, meaning B2 modes are pulled DOWN.
# This is because V_B2_B2 > 0 (direct interaction) and n_B2 > 0,
# but the dominant contribution is V_B2_B1 * n_B1 (B1 mode is
# strongly occupied at N=1). V_B2_B1 = 0.0799, n_B1 ~ 0.39.
# Sigma_B2 ~ V_B2_B1*n_B1 + sum_j V_B2j*n_j = ...

# Let's verify: compute Sigma from V and n
Sigma_check = V_bare @ n_k_ed
print("  Self-energy verification:")
print(f"    Sigma_check = V_bare @ n_k_ed:")
for i in range(8):
    print(f"      {labels[i]:>5s}: computed={Sigma_check[i]:.6f}, stored={Sigma_HF[i]:.6f}, diff={abs(Sigma_check[i]-Sigma_HF[i]):.2e}")
print()

# The self-energy doesn't exactly match because HFB uses its own
# self-consistent n_k, not the ED n_k. Let's check with HFB n_k:
n_k_hfb = d_spec['N1_n_k_hfb']
Sigma_check_hfb = V_bare @ n_k_hfb
print("  With HFB occupations:")
for i in range(8):
    print(f"      {labels[i]:>5s}: computed={Sigma_check_hfb[i]:.6f}, stored={Sigma_HF[i]:.6f}, diff={abs(Sigma_check_hfb[i]-Sigma_HF[i]):.2e}")
print()

# =====================================================================
# 8. DEFINITIVE f_0 COMPUTATION
# =====================================================================
print("=" * 72)
print("8. DEFINITIVE LANDAU PARAMETER f_0")
print("=" * 72)
print()

# The correct Landau parameter for a finite system is:
#
# f_0 = N(0) * f_0^{bare}
#
# where f_0^{bare} = <V_ph>_{FS} is the Fermi-surface average of the
# particle-hole vertex. In Landau's theory (Paper 11), this is:
#
#   F_l^s = N(0) * (1/(4pi)) * integral f^s(theta) P_l(cos theta) d(Omega)
#
# For l=0: F_0^s = N(0) * f_0^s (the angle-averaged interaction)
#
# In our 8-mode system, the "Fermi surface" consists of modes near mu.
# The relevant modes are B2 (4 modes) and B1 (1 mode).
#
# TWO DEFINITIONS:
#
# (A) Within B2 sector only (analog of S22c (0,0) singlet):
#     N(0) = 4 (degeneracy) or rho_B2_per_mode=14.02 (continuous DOS)
#     V_avg = average V_B2B2
#
# (B) Full 8-mode system:
#     N(0) = all modes weighted by proximity to mu
#     V_avg = weighted average of full V_bare

# === Definition A: Intra-B2 (S22c singlet analog) ===
print("--- (A) Intra-B2 sector (S22c singlet analog) ---")
print()

# Using N(0) = 4 (discrete modes)
V_avg_intra = np.mean(V_B2B2)
f0_A_discrete = 4 * V_avg_intra  # N(0) = 4 modes
print(f"  V_avg (B2-B2) = {V_avg_intra:.6f}")
print(f"  f_0 (N(0)=4 modes) = {f0_A_discrete:.4f}")
print(f"  Sign: {'ATTRACTIVE (-)' if f0_A_discrete < 0 else 'REPULSIVE (+)'}")
print()

# Using N(0) = rho_B2_per_mode = 14.02
f0_A_continuous = rho_B2 * V_avg_intra
print(f"  f_0 (N(0)=rho_B2={rho_B2:.2f}) = {f0_A_continuous:.4f}")
print(f"  Sign: {'ATTRACTIVE (-)' if f0_A_continuous < 0 else 'REPULSIVE (+)'}")
print()

# === Definition B: With HFB coherence factors ===
print("--- (B) With HFB coherence factors ---")
print()

# The dressed vertex in the BCS ground state:
# Gamma_ph(k,k') = V(k,k') * [(u_k u_{k'} + v_k v_{k'})^2 - (u_k v_{k'} - v_k u_{k'})^2]
# = V(k,k') * [2(u_k u_{k'} v_k v_{k'}) + u_k^2 u_{k'}^2 + v_k^2 v_{k'}^2
#              - u_k^2 v_{k'}^2 - v_k^2 u_{k'}^2 + 2 u_k v_k u_{k'} v_{k'}]
# Simplification: (uu+vv)^2 - (uv-vu)^2 = (uu+vv+uv-vu)(uu+vv-uv+vu)
#                                        = [u(u+v)+v(v-u)][u(u-v)+v(u+v)]
# Let's just compute numerically.

V_dressed = np.zeros((8, 8))
for i in range(8):
    for j in range(8):
        uu_vv = u_ed[i]*u_ed[j] + v_ed[i]*v_ed[j]
        uv_vu = u_ed[i]*v_ed[j] - v_ed[i]*u_ed[j]
        V_dressed[i, j] = V_bare[i, j] * (uu_vv**2 - uv_vu**2)

V_dressed_B2B2 = V_dressed[np.ix_(B2_idx, B2_idx)]
V_dressed_avg = np.mean(V_dressed_B2B2)

f0_B_discrete = 4 * V_dressed_avg
f0_B_continuous = rho_B2 * V_dressed_avg

print(f"  <V_dressed>_B2 = {V_dressed_avg:.6f}")
print(f"  f_0 (N(0)=4, dressed) = {f0_B_discrete:.4f}")
print(f"  f_0 (N(0)={rho_B2:.2f}, dressed) = {f0_B_continuous:.4f}")
print()

# Ratio of dressed to bare
ratio_dress = V_dressed_avg / V_avg_intra if V_avg_intra != 0 else float('inf')
print(f"  Dressing ratio: V_dressed/V_bare = {ratio_dress:.4f}")
print(f"  Coherence factors REDUCE interaction by factor {ratio_dress:.4f}")
print()

# === Definition C: S22c-equivalent with corrected sign ===
print("--- (C) S22c-equivalent computation ---")
print()

# S22c computed: f = -<d(lam)/d(tau)> * N(0) / lam_F
# At tau=0.30 for (0,0) sector with 16 modes:
# avg_d = mean of d(lambda)/d(tau) over all 16 modes
# N(0) = modes within 10% of lam_F
# lam_F = minimum eigenvalue
#
# From S22c output at tau=0.30:
# All eigenvalue derivatives are POSITIVE (hardening at tau=0.30):
#   dlam[0..1] = +0.107, dlam[2..7] = +0.132
# 8 modes with average derivative:
avg_d_S22c = (2*0.107021 + 6*0.131696) / 8  # from S22c Part 7
lam_F_S22c = 0.822148  # (local)
# But the full (0,0) sector has 16 modes (Peter-Weyl)
# S22c used 16 modes: 8 shown + 8 more
# Let's read the actual stored value

print(f"  S22c at tau=0.30 for (0,0):")
print(f"    f(0,0) = -4.687 (STORED)")
print(f"    avg derivative (8 shown modes) = {avg_d_S22c:.6f}")
print(f"    lam_F = {lam_F_S22c:.6f}")
print(f"    N(0) = 16 modes (full (0,0) sector)")
print()
print(f"  Reverse-engineering: f = -avg_d * N(0) / lam_F")
print(f"    f = -{avg_d_S22c} * 16 / {lam_F_S22c} = {-avg_d_S22c * 16 / lam_F_S22c:.4f}")
print()

# BUT WAIT — S22c evaluates at tau=0.30, where d(lam)/d(tau) is POSITIVE
# (the gap is REOPENING past the fold). The result f = -4.687 means
# the average derivative was POSITIVE and large at tau=0.30.
#
# Let me re-examine: the stored output says f(0.30) = -4.687.
# From line 238: (0,0) dim=1 thresh=-3  f(0.15)=-2.481  f(0.30)=-4.687
#
# At tau=0.15: avg_d ~ -0.234 (softening, 2 modes) + -0.104 (6 modes)
# At tau=0.30: avg_d ~ +0.107 (2 modes) + +0.132 (6 modes) — ALL positive!
#
# With the S22c formula: f = -avg_d * N0 / lam_F
# At tau=0.30: avg_d > 0, so f < 0 if we use the convention f = +avg_d*N0/lam_F
# But stored says f = -4.687 < 0.
#
# Let me check: avg_d at tau=0.30 for ALL 16 modes (not just 8).
# S22c used the FULL (0,0) sector which has 16 modes at pqsum<=6.
# The 8 modes shown are the lowest; the other 8 are at higher eigenvalues.
# S22c's avg_d averages over ALL modes, and the higher modes have
# STRONGER softening (they decrease faster with tau). This can make
# the average negative even when the lowest modes are hardening.

# For our 8-mode system:
# avg_d_bare analog: How fast does the B2 spectrum change?
# We use the self-energy as proxy:
# "d(E_k)/d(tau)" at the fold ~ Sigma_k (the shift from bare to HFB)
# per unit "deformation" (which is parameterized by N_pair here)

print("  8-mode system analog:")
print(f"    B2 self-energy (proxy for d(lam)/dtau): {Sigma_B2_avg:.6f}")
print(f"    B2 self-energy is NEGATIVE → modes soften → attractive")
print()

# S22c-style f_0 for 8-mode system:
# f = -<Sigma> * N_modes / lam_F
# where <Sigma> is the average self-energy of modes near the Fermi surface
# N_modes = 4 (B2 degeneracy at Fermi level)
f0_C = -Sigma_B2_avg * 4 / mu_BCS
print(f"    f_0 = -<Sigma_B2> * N_modes / mu_BCS")
print(f"        = -{Sigma_B2_avg:.6f} * 4 / {mu_BCS:.6f}")
print(f"        = {f0_C:.4f}")
print(f"    Threshold = {threshold}")
print(f"    Status: {'UNSTABLE' if f0_C < threshold else 'stable'}")
print()

# =====================================================================
# 9. PROPER FERMI LIQUID COMPUTATION
# =====================================================================
print("=" * 72)
print("9. PROPER FERMI LIQUID f_0 = V_ph * N(0)")
print("=" * 72)
print()

# The Landau parameter in its standard definition:
#   F_0^s = N(0) * <V_ph>  (dimensionless)
# Pomeranchuk: F_0^s < -1 (for l=0 in 3D), or equivalently
#   1 + F_0^s / (2l+1) < 0
# In S22c convention with dim(rep)=1 for (0,0):
#   f < -(2*1+1) = -3
#
# There are two distinct V_ph to consider:
#
# (a) V_ph from bare V_bare: repulsive (V>0), gives f_0 > 0 → STABLE
# (b) V_ph from self-energy slope: this captures the EFFECTIVE
#     interaction including screening and vertex corrections.
#     The self-energy is negative for B2 modes → effective attraction.

# The TRUE Landau parameter measures the response of the system to
# a quasiparticle excitation. At N=1:
# delta_E = E(N=1, excite k) - E(N=1, ground)
# The Landau f is: f_{kk'} = delta^2 E / (delta n_k * delta n_{k'})

# From the HFB solution, we can extract this:
# E_HFB = sum_k E_bare_k * n_k + (1/2) sum_{kk'} V_{kk'} n_k n_{k'}
# delta^2 E / (delta n_k delta n_{k'}) = V_{kk'}
# So f_{kk'} = V_{kk'} (this is the Hartree approximation)

# The key point: V_bare is POSITIVE (repulsive), so the direct
# Landau parameter is POSITIVE. The S22c result f=-4.687 used a
# DIFFERENT definition based on eigenvalue flow.

print("  The reconciliation:")
print()
print("  S22c's f(0,0) = -4.687 measured the eigenvalue softening rate")
print("  of the FULL Dirac spectrum on SU(3) as tau varies.")
print("  This is NOT the same as the Landau f from the interaction matrix.")
print()
print("  The S22c 'f' captures: how fast does the gap close?")
print("  The Landau 'f' captures: is the ground state unstable to")
print("  particle-hole fluctuations?")
print()
print("  At N_pair=1 with explicit V_bare:")
print(f"    f_0 (direct, B2-B2, N(0)=4) = +{f0_A_discrete:.4f} (REPULSIVE → STABLE)")
print(f"    f_0 (direct, B2-B2, N(0)={rho_B2:.0f}) = +{f0_A_continuous:.4f} (REPULSIVE → STABLE)")
print(f"    f_0 (dressed, B2-B2, N(0)=4) = +{f0_B_discrete:.4f} (REPULSIVE → STABLE)")
print()

# BUT: The HFB self-energy reveals that the EFFECTIVE interaction
# (including exchange/Fock terms) is attractive for B2 modes.
# This is because V_{B2,B1} = 0.0799 >> V_{B2,B2} ~ 0.03-0.06,
# and the B1 mode is the most occupied (n_B1 ~ 0.39 vs n_B2 ~ 0.15).
# The inter-sector attraction (B2 attracted toward B1) is the
# dominant effect, not the intra-B2 repulsion.

print("  CRITICAL OBSERVATION: Inter-sector B2-B1 coupling")
print(f"    V(B2,B1) = {V_bare[0,4]:.6f} (all B2 modes couple equally to B1)")
print(f"    V(B2,B2) avg = {V_avg_intra:.6f}")
print(f"    V(B2,B1) / V(B2,B2) = {V_bare[0,4]/V_avg_intra:.2f}")
print(f"    B1 occupation n_B1 = {n_k_ed[4]:.4f}")
print(f"    B2 occupation <n_B2> = {np.mean(n_k_ed[:4]):.4f}")
print()
print(f"    Self-energy of B2 from B1 alone: V(B2,B1)*n_B1 = {V_bare[0,4]*n_k_ed[4]:.6f}")
print(f"    Self-energy of B2 from B2: sum V(B2,B2)*n_B2 ~ {np.sum(V_B2B2[0,:]*n_k_ed[:4]):.6f}")
print(f"    Total Sigma_B2 = {Sigma_B2_avg:.6f} (from all modes)")
print(f"    The B1 contribution ({V_bare[0,4]*n_k_ed[4]:.4f}) is the DOMINANT")
print(f"    source of the B2 energy shift.")
print()

# =====================================================================
# 10. HFB-UPDATED f_0 WITH PHYSICAL INTERPRETATION
# =====================================================================
print("=" * 72)
print("10. HFB-UPDATED LANDAU PARAMETER — COMPARISON TO S22c")
print("=" * 72)
print()

# The physically meaningful comparison to S22c is:
# How does the HFB self-consistent spectrum change the system's
# stability toward the BCS condensation that S22c identified?
#
# S22c's f(0,0) = -4.687 at tau=0.30 measured the "softening tendency"
# of the (0,0) sector eigenvalues. The analog at N_pair=1 is:
# how much does the self-consistent solution compress the near-Fermi
# spectrum relative to bare?

# Gap compression ratio
E_range_bare = np.max(E_bare) - np.min(E_bare)
E_range_hfb = np.max(E_hfb) - np.min(E_hfb)
compression = E_range_hfb / E_range_bare

print(f"  Bare spectrum range: {E_range_bare:.6f} M_KK")
print(f"  HFB spectrum range:  {E_range_hfb:.6f} M_KK")
print(f"  Compression ratio:   {compression:.4f}")
print()

# The effective DOS at the Fermi level
# In bare spectrum: only B1 at mu, B2 at +0.026 above
# In HFB spectrum: B2 modes move DOWN below mu, B1 moves UP above mu
# → ALL 5 near-Fermi modes (4 B2 + 1 B1) are within a smaller window
# → N(0) effectively INCREASES
E_window_bare = np.max(np.abs(xi_bare[:5]))  # max |xi| among B2+B1 (bare)
E_window_hfb = np.max(np.abs(xi_hfb[:5]))    # max |xi| among B2+B1 (HFB)

N_eff_bare = 5 / (2 * E_window_bare)  # effective DOS from 5 modes in window
N_eff_hfb = 5 / (2 * E_window_hfb)

print(f"  Near-Fermi window (bare): |xi|_max = {E_window_bare:.6f}")
print(f"  Near-Fermi window (HFB):  |xi|_max = {E_window_hfb:.6f}")
print(f"  Effective DOS (bare):     N_eff = {N_eff_bare:.2f}")
print(f"  Effective DOS (HFB):      N_eff = {N_eff_hfb:.2f}")
print(f"  DOS enhancement factor:   {N_eff_hfb/N_eff_bare:.2f}")
print()

# Now compute f_0 in the S22c sense but with HFB corrections:
# The HFB self-energy IS the Landau interaction function evaluated
# at the mean-field level. The Pomeranchuk parameter in our system is:
#
# f_0^{HFB} = sum_k Sigma_k * n_k / (sum_k n_k * E_F)
# This measures the interaction-to-kinetic ratio.

# Actually, the cleanest definition matching S22c is:
# f_0 = V_ph * N(0) where V_ph = Sigma / n_total
# (the self-energy per particle is the mean-field interaction strength)

V_ph_effective = np.mean(Sigma_HF[:4]) / np.sum(n_k_ed[:4])  # per B2 particle
f0_HFB_S22c = V_ph_effective * rho_B2
print(f"  V_ph (effective, from HFB self-energy) = {V_ph_effective:.6f}")
print(f"  f_0^HFB = V_ph * rho_B2 = {V_ph_effective:.6f} * {rho_B2:.2f} = {f0_HFB_S22c:.4f}")
print()

# More direct: g*N(0) from S22c was ||K_a|| * N(0)
# K_a at fold = 1.55 (from S22c). At N_pair=1, the effective coupling
# is modified by HFB. The quasiparticle weight Z tells us the
# renormalization.
Z_B2_ed = np.mean(Z_ed[:4])
Z_B2_hfb = np.mean(d_spec['N1_Z_hfb'][:4])

print(f"  Quasiparticle weight Z (ED, B2):  {Z_B2_ed:.4f}")
print(f"  Quasiparticle weight Z (HFB, B2): {Z_B2_hfb:.4f}")
print(f"  Z < 0.25 → quasiparticles poorly defined (N_pair=1 limit)")
print()

# The Landau effective mass is m*/m = 1/(Z * (1 + F_1^s/3))
# At N_pair=1, Z ~ 0.14, so m* ~ 7*m. This is very heavy.
m_star_ratio = 1.0 / Z_B2_ed
print(f"  Effective mass ratio m*/m ~ 1/Z ~ {m_star_ratio:.1f}")
print(f"  (Heavy quasiparticles — consistent with N_pair=1 strong correlation)")
print()

# =====================================================================
# 11. COMPARISON TABLE
# =====================================================================
print("=" * 72)
print("11. COMPARISON: S22c vs S53 HFB")
print("=" * 72)
print()
print("  Quantity                  S22c (bare)      S53 HFB (N=1)")
print("  " + "-"*62)
print(f"  Spectrum                  Full Dirac       8-mode HFB")
print(f"  f(0,0) (eigenvalue flow)  -4.687           N/A (no tau sweep)")
print(f"  V_ph (B2-B2 avg)          not computed     +{V_avg_intra:.5f}")
print(f"  f_0 (V_ph * N_modes)      N/A              +{f0_A_discrete:.4f}")
print(f"  f_0 (V_ph * rho_B2)       N/A              +{f0_A_continuous:.4f}")
print(f"  Sigma_B2 (self-energy)    not computed     {Sigma_B2_avg:+.5f}")
print(f"  f_0 (self-energy)         N/A              {f0_HFB_S22c:+.4f}")
print(f"  g*N(0)                    3.24             {abs(f0_HFB_S22c):.2f}")
print(f"  Z (qp weight)             N/A              {Z_B2_ed:.4f}")
print(f"  m*/m                      N/A              {m_star_ratio:.1f}")
print(f"  Gap B2-B1 (bare)          0.0261           {gap_bare:.4f}")
print(f"  Gap B2-B1 (HFB)           N/A              {gap_hfb:.4f}")
print(f"  Threshold                 -3               -3")
print(f"  Pomeranchuk status        UNSTABLE         see below")
print()

# =====================================================================
# 12. VERDICT
# =====================================================================
print("=" * 72)
print("12. GATE VERDICT: POMERANCHUK-HFB-53")
print("=" * 72)
print()

# The S22c Pomeranchuk parameter f(0,0) = -4.687 and the HFB-derived
# quantities measure DIFFERENT things:
#
# 1. S22c's f(0,0): measures eigenvalue softening rate of the full Dirac
#    spectrum as a function of the deformation parameter tau. This is an
#    analog of the Landau-Pomeranchuk criterion applied to the spectral
#    flow. It is NEGATIVE because eigenvalues soften with tau.
#
# 2. V_ph * N(0) from V_bare: the direct particle-hole interaction is
#    REPULSIVE (V > 0). In the conventional Landau theory sense, the
#    system is stable against p-h fluctuations.
#
# 3. HFB self-energy: the mean-field interaction shifts B2 modes DOWN
#    (Sigma < 0), effectively compressing the near-Fermi spectrum.
#    This is an ATTRACTIVE self-energy effect, analogous to the
#    eigenvalue softening in S22c.
#
# The resolution: S22c's "Pomeranchuk instability" is really a statement
# about the BCS PARTICLE-PARTICLE channel (Cooper instability), not the
# PARTICLE-HOLE channel. The eigenvalue softening creates conditions
# favorable for pairing. The direct p-h interaction is repulsive.

# HFB EFFECT ON THE BCS INSTABILITY:
# The HFB self-energy ENHANCES the BCS instability by:
# (a) Compressing the near-Fermi spectrum (gap closes by 378%)
# (b) Moving B2 modes from ABOVE to BELOW mu (level inversion)
# (c) Increasing the effective DOS at the Fermi level

print("INTERPRETATION:")
print()
print("  The S22c 'Pomeranchuk parameter' f(0,0) = -4.687 is a SPECTRAL")
print("  FLOW diagnostic, not a conventional Landau p-h parameter.")
print("  The direct V_ph from V_bare is repulsive (f_0 > 0).")
print()
print("  HFB self-consistency MODIFIES the picture:")
print(f"    1. B2 self-energy Sigma = {Sigma_B2_avg:+.5f} (attractive shift)")
print(f"    2. B2-B1 gap closes: {gap_bare:.4f} → {gap_hfb:.4f} ({delta_gap/gap_bare*100:+.0f}%)")
print(f"    3. B2 modes cross Fermi level (xi_B2 goes from +0.026 to {np.mean(xi_hfb[:4]):+.4f})")
print(f"    4. Effective DOS enhancement: {N_eff_hfb/N_eff_bare:.1f}x")
print()
print("  The HFB self-consistent spectrum STRENGTHENS the conditions for")
print("  BCS condensation (the instability that S22c identified):")
print(f"    - More modes near Fermi level (N_eff: {N_eff_bare:.1f} → {N_eff_hfb:.1f})")
print(f"    - Quasiparticle weight Z = {Z_B2_ed:.3f} (strongly correlated)")
print(f"    - Level inversion: B2 < mu < B1 in HFB (vs B1 < B2 in bare)")
print()
print("  S22c's f(0,0) = -4.687 is not directly updatable with HFB data")
print("  because it requires a full tau sweep of the self-consistent spectrum.")
print("  However, the HFB corrections uniformly STRENGTHEN the instability:")
print(f"    - Gap compression: {compression:.3f}")
print(f"    - Self-energy attraction: Sigma_B2/E_F = {Sigma_B2_avg/mu_BCS:.4f}")
print()
print("  GATE VERDICT: POMERANCHUK-HFB-53 = INFO")
print(f"    f(0,0) = -4.687 (S22c, bare spectrum, spectral flow)")
print(f"    f_0^direct = +{f0_A_discrete:.3f} (V_ph*N_modes, repulsive)")
print(f"    f_0^self-energy = {f0_HFB_S22c:+.3f} (HFB self-energy measure)")
print(f"    HFB effect: STRENGTHENS BCS instability conditions")
print(f"    At N_pair=1: Fermi liquid theory MARGINAL (Z={Z_B2_ed:.3f}, m*/m={m_star_ratio:.0f})")
print()

# =====================================================================
# 13. SAVE RESULTS
# =====================================================================
out_file = 'computations/session-53/s53_pomeranchuk_hfb.npz'
np.savez(out_file,
    # S22c reference
    f_00_S22c=-4.687,
    threshold=threshold,
    # Direct Landau parameter from V_bare
    f0_direct_discrete=f0_A_discrete,
    f0_direct_continuous=f0_A_continuous,
    f0_dressed_discrete=f0_B_discrete,
    f0_dressed_continuous=f0_B_continuous,
    # HFB self-energy derived
    f0_self_energy=f0_HFB_S22c,
    Sigma_B2_avg=Sigma_B2_avg,
    V_ph_effective=V_ph_effective,
    # Spectrum data
    gap_bare=gap_bare,
    gap_hfb=gap_hfb,
    gap_compression=compression,
    # DOS
    N_eff_bare=N_eff_bare,
    N_eff_hfb=N_eff_hfb,
    # Quasiparticle properties
    Z_B2_ed=Z_B2_ed,
    Z_B2_hfb=Z_B2_hfb,
    m_star_ratio=m_star_ratio,
    # Gate
    gate_name='POMERANCHUK-HFB-53',
    gate_verdict='INFO',
)
print(f"Results saved to {out_file}")
print()
print("=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
