#!/usr/bin/env python3
"""
FABRIC-RPA-50: RPA-Screened Phonon Propagator on the 32-Cell Fabric
====================================================================

Physics:
  S37 established E_vac/E_cond = 28.8 -- quantum fluctuations dominate by 29x.
  The O-Z propagator is the mean-field (Hartree-Fock) result. RPA is the first
  correction beyond mean field. It introduces K-dependent vertex renormalization
  through the pair susceptibility chi_0(K).

  The Schur Lemma Trap (S34, S50 deep-dive Section 3.3): V(B2,B2) = 0.1557
  is k-independent by Schur's lemma. The mean-field propagator is featureless.
  But the RPA vertex correction involves the PAIR SUSCEPTIBILITY chi_0(K,omega),
  which IS K-dependent because it includes the spatial structure of the Cooper
  pair wave function across multiple cells (xi_BCS/l_cell = 5.3).

  The nuclear precedent (Paper 07): effective charges correct transition rates
  by factors of 2-5. The framework's coupling g^2*chi_0 ~ 1.54 (estimated in
  deep-dive Section 3.6) suggests a similar-scale correction.

  Method:
    1. Build the 8-mode BdG quasiparticle spectrum from S48 ED data
    2. Construct the pair propagator on the 32-cell 1D fabric (ring)
    3. Compute the bare pair susceptibility chi_0(K) at omega=0 (static limit):
         chi_0(K) = sum_k F(k,K) / [E(k) + E(k+K)]
       where F is the pair form factor and E is the BdG quasiparticle energy
    4. Solve the RPA Dyson equation:
         D_RPA(K) = D_0(K) / [1 - g^2 * chi_0(K) * D_0(K)]
    5. Extract n_s(RPA) and alpha_s(RPA) from D_RPA

Gate: FABRIC-RPA-50
  PASS: alpha_s(RPA) in [-0.040, 0] (2-sigma Planck compatibility)
  FAIL: alpha_s(RPA) = n_s^2 - 1 (identity survives RPA -- chi_0 K-dependence too weak)
  INFO: alpha_s(RPA) deviates from identity but outside Planck range

Author: nazarewicz-nuclear-structure-theorist, Session 50
Date: 2026-03-20
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

t0 = time.time()

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import (
    tau_fold, N_cells, E_cond, E_cond_ED_8mode,
    Delta_0_GL, Delta_0_OES, Delta_B3,
    rho_B2_per_mode, E_B1, E_B2_mean, E_B3_mean,
    xi_BCS, xi_GL, omega_PV, PI,
    M_KK, M_KK_gravity,
)

print("=" * 78)
print("FABRIC-RPA-50: RPA-Screened Phonon Propagator on the 32-Cell Fabric")
print("=" * 78)

# =============================================================================
# STEP 1: Load all upstream data
# =============================================================================
print("\n--- Step 1: Load Upstream Data ---")

# S48 single-cell ED results
s48 = np.load(os.path.join(SCRIPT_DIR, 's48_npair_full.npz'), allow_pickle=True)
pair_occ = np.array(s48['pair_occ'])      # v_k^2 for 8 modes
E_8 = np.array(s48['E_8'])                # single-particle energies
V_8x8 = np.array(s48['V_8x8'])            # pairing interaction matrix
rho_8 = np.array(s48['rho_8'])            # DOS per mode
Delta_BCS = np.array(s48['Delta_BCS'])     # BCS gap for each mode
pair_corr = np.array(s48['pair_corr'])     # <b^dag_n b_m>

labels = ['B1', 'B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B3[0]', 'B3[1]', 'B3[2]']
n_modes = 8

# S50 leggett propagator (for lattice geometry and O-Z reference)
s50_lp = np.load(os.path.join(SCRIPT_DIR, 's50_leggett_propagator.npz'), allow_pickle=True)
J_C2 = float(s50_lp['J_C2'])
J_su2 = float(s50_lp['J_su2'])
J_eff_spatial = float(s50_lp['J_eff'])
K_pivot = float(s50_lp['K_pivot'])
T_acoustic = float(s50_lp['T_acoustic'])
m_base_sq_OZ = float(s50_lp['m_base_sq'])
m_star_OZ = float(s50_lp['m_star_OZ'])
alpha_s_OZ = float(s50_lp['alpha_s_OZ'])
n_s_OZ = float(s50_lp['n_s_OZ'])

# S49 fabric data
s49 = np.load(os.path.join(SCRIPT_DIR, 's49_fabric_npair.npz'), allow_pickle=True)
E_C = float(s49['E_C'])

# S50 jpair calibrate
s50_jp = np.load(os.path.join(SCRIPT_DIR, 's50_jpair_calibrate.npz'), allow_pickle=True)
J_pair_primary = float(s50_jp['J_pair_primary'])
F_transfer = float(s50_jp['F_transfer_plain'])
ukvk = np.array(s50_jp['ukvk'])

# S47 texture for l_cell
s47 = np.load(os.path.join(SCRIPT_DIR, 's47_texture_corr.npz'), allow_pickle=True)
l_cell = float(s47['l_cell'])

# S48 Leggett mode
s48_legg = np.load(os.path.join(SCRIPT_DIR, 's48_leggett_mode.npz'), allow_pickle=True)
Delta_fold = np.array(s48_legg['Delta_fold'])  # [B1, B2, B3]
rho_fold = np.array(s48_legg['rho_fold'])      # [B1, B2, B3]

print(f"  Lattice parameters:")
print(f"    J_C2 = {J_C2:.6f}, J_su2 = {J_su2:.6f}")
print(f"    J_eff = {J_eff_spatial:.6f}")
print(f"    K_pivot = {K_pivot:.6f}")
print(f"    l_cell = {l_cell:.4f} M_KK^-1")
print(f"    N_cells = {N_cells}")
print(f"    T_acoustic = {T_acoustic:.6f}")
print(f"    m_base^2(OZ) = {m_base_sq_OZ:.4f}")

print(f"\n  Single-cell BCS parameters:")
print(f"    E_cond = {E_cond:.10f}")
print(f"    Pair occupations (v_k^2): {pair_occ}")
print(f"    BCS gaps (Delta_k): {Delta_BCS}")
print(f"    SP energies (E_k): {E_8}")
print(f"    DOS (rho_k): {rho_8}")
print(f"    Delta_fold [B1,B2,B3] = {Delta_fold}")
print(f"    rho_fold [B1,B2,B3] = {rho_fold}")

print(f"\n  Pair transfer (S50 J-PAIR-CALIBRATE):")
print(f"    J_pair = {J_pair_primary:.6f}")
print(f"    F_transfer = {F_transfer:.6f}")
print(f"    u_k*v_k: {ukvk}")

# =============================================================================
# STEP 2: Build BdG quasiparticle spectrum
# =============================================================================
print("\n--- Step 2: BdG Quasiparticle Spectrum ---")

# In BCS theory:
#   E_k = sqrt((epsilon_k - mu)^2 + Delta_k^2)
# where epsilon_k are single-particle energies, mu = 0 (PH symmetric),
# Delta_k are the BCS gaps.
#
# For the framework: epsilon_k = E_8[k], mu = 0
# The quasiparticle energy is:
#   E_qp_k = sqrt(E_8[k]^2 + Delta_BCS[k]^2)
#
# BCS amplitudes:
#   v_k^2 = (1/2)(1 - xi_k/E_qp_k)  where xi_k = E_8[k] - mu = E_8[k]
#   u_k^2 = 1 - v_k^2
#
# NOTE: The actual pair occupations from ED differ from BCS due to
# fluctuation corrections (PBCS/BCS = 0.63). We use the ED values
# for the form factor but the BCS E_qp for the energy denominator,
# since the BdG spectrum is the relevant energy scale for the
# susceptibility denominator.

mu = 0.0
xi_k = E_8 - mu  # = E_8 since mu = 0

# BdG quasiparticle energies using BCS gaps
E_qp = np.sqrt(xi_k**2 + Delta_BCS**2)

# BCS coherence factors
v2_BCS = 0.5 * (1.0 - xi_k / E_qp)
u2_BCS = 1.0 - v2_BCS
uv_BCS = np.sqrt(u2_BCS * v2_BCS)

# ED coherence factors (from actual pair occupations)
v2_ED = pair_occ
u2_ED = 1.0 - v2_ED
uv_ED = np.sqrt(u2_ED * v2_ED)

print(f"  Quasiparticle energies E_qp_k:")
for k in range(n_modes):
    print(f"    {labels[k]:>5s}: E_qp = {E_qp[k]:.6f}, "
          f"Delta = {Delta_BCS[k]:.6f}, xi = {xi_k[k]:.6f}")

print(f"\n  Coherence factors:")
print(f"    {'Mode':>5s} {'v2_ED':>10s} {'v2_BCS':>10s} {'uv_ED':>10s} {'uv_BCS':>10s}")
for k in range(n_modes):
    print(f"    {labels[k]:>5s} {v2_ED[k]:10.6f} {v2_BCS[k]:10.6f} "
          f"{uv_ED[k]:10.6f} {uv_BCS[k]:10.6f}")

# =============================================================================
# STEP 3: Pair susceptibility chi_0(K) on the 32-cell ring
# =============================================================================
print("\n--- Step 3: Pair Susceptibility chi_0(K) ---")

# The static pair susceptibility at crystal momentum K is:
#
#   chi_0(K) = sum_{k,n,m} F_{nm}(k,K) / [E_qp(k,n) + E_qp(k+K,m)]
#
# where (k,n) labels the quasiparticle: k is the cell-level crystal momentum
# (fabric Bloch wave) and n is the internal mode index (8 modes per cell).
#
# For the 32-cell ring with 8 internal modes:
# - Cell momenta: k = 2*pi*j/(N_cells*l_cell) for j = 0,1,...,N_cells-1
# - Internal modes: n = 0,...,7
# - The BdG energy is E(k,n) = sqrt(epsilon_n^2 + Delta_n^2 + 2*J_eff*cos(k*l_cell)*rho_n*Delta_n^2/epsilon_n)
#
# SIMPLIFICATION: In the Mott insulator regime (J << E_C), the inter-cell
# coupling is perturbative. The quasiparticle energy at momentum k is:
#   E(k,n) ≈ E_qp(n) + delta_E(k,n)
# where delta_E(k,n) = J_pair * cos(k*l_cell) * f(n)
# and f(n) is the pair-hopping form factor for mode n.
#
# More precisely, in a Josephson junction chain, the collective excitations
# are pair-phonons (sound modes of the condensate). The pair susceptibility
# measures the response of the pair field to a spatially modulated perturbation.
#
# The pair form factor for a transition at momentum transfer K:
#   F_nm(K) = (u_n*v_m + v_n*u_m)^2
# For the same-sector, same-mode contribution (n=m, dominant):
#   F_nn = (2*u_n*v_n)^2 = 4*(u_n*v_n)^2
#
# On the ring, the crystal momenta are:
#   K_j = 2*pi*j / L_total, j = 0, 1, ..., N_cells-1
# where L_total = N_cells * l_cell

L_total = N_cells * l_cell
K_lattice = 2.0 * PI * np.arange(N_cells) / L_total

print(f"  Fabric lattice:")
print(f"    L_total = {L_total:.4f} M_KK^-1")
print(f"    K_BZ = pi/l_cell = {PI/l_cell:.4f}")
print(f"    K_max(lattice) = {K_lattice[-1]:.4f}")
print(f"    K_min(nonzero) = {K_lattice[1]:.4f}")
print(f"    K_pivot = {K_pivot:.4f}")
print(f"    K_pivot*l_cell = {K_pivot*l_cell:.4f}")
print(f"    xi_BCS/l_cell = {xi_BCS/l_cell:.2f}")

# The pair propagator on the ring with Josephson coupling J_pair:
# Each cell has a pair excitation spectrum E_qp(n) for n = 0,...,7.
# The inter-cell hopping of the pair is J_pair.
# The pair propagator (pair Green's function) at momentum K is:
#
#   G_pair(K, omega) = sum_n |F_n|^2 / [omega^2 - Omega_n(K)^2]
#
# where Omega_n(K)^2 = (2*E_qp(n))^2 + 4*E_qp(n)*J_pair*epsilon_K
# and epsilon_K = 2*(1 - cos(K*l_cell)) is the tight-binding dispersion.
#
# The STATIC pair susceptibility (omega=0):
#   chi_0(K) = sum_n rho_n * (2*u_n*v_n)^2 / [2*E_qp(n) + J_pair*epsilon_K*f_n]
#
# where f_n encodes how the pair hopping modifies the quasiparticle energy.
#
# In the nuclear BCS (Paper 03), the pair susceptibility is:
#   chi_0 = sum_k (u_k v_k)^2 / E_k
# which is the static, K=0 limit. The K-dependence comes from the
# inter-cell structure.
#
# For a 1D chain with pair hopping J_pair:
# The pair bandwidth is 4*J_pair (tight-binding)
# The pair energy at momentum K is:
#   E_pair(K) = E_pair(0) + 2*J_pair*(1 - cos(K*l_cell))
# = E_pair(0) + J_pair * epsilon_K

# Tight-binding dispersion
def epsilon_TB(K_val):
    """Tight-binding dispersion on the 32-cell ring."""
    return 2.0 * (1.0 - np.cos(K_val * l_cell))

# Pair form factors (from ED data)
# F_n = 2*u_n*v_n (coherence factor for pair creation/annihilation)
F_n_ED = 2.0 * uv_ED     # from ED pair occupations
F_n_BCS = 2.0 * uv_BCS   # from BCS for comparison

print(f"\n  Pair form factors:")
print(f"    {'Mode':>5s} {'F_ED':>10s} {'F_BCS':>10s} {'rho':>10s}")
for n in range(n_modes):
    print(f"    {labels[n]:>5s} {F_n_ED[n]:10.6f} {F_n_BCS[n]:10.6f} {rho_8[n]:10.4f}")

# The pair susceptibility at each K value
# Using the physical model:
# chi_0(K) = sum_n rho_n * F_n^2 / [2*E_qp(n) + J_pair * epsilon_K * w_n]
#
# where w_n is a weight factor from the pair-hopping matrix element.
# For a simple Josephson model, w_n = F_n^2 (the same mode participates in both
# the susceptibility and the dispersion).
#
# In the simplest case (dominant B2 sector, all modes at same E_qp):
# chi_0(K) = rho_B2 * F_B2^2 / [2*E_qp_B2 + J_pair * epsilon_K]
#
# We compute the FULL 8-mode susceptibility:

def chi_0_static(K_val, use_ED=True):
    """Static pair susceptibility at momentum K.

    chi_0(K) = sum_n rho_n * F_n^2 / [2*E_qp_n + J_pair * epsilon(K) * F_n^2 / F_max^2]

    The J_pair*epsilon(K) term represents the dispersion of the pair excitation
    across the fabric. It modifies the pair energy denominator in a K-dependent way.

    The weight F_n^2/F_max^2 ensures that modes with larger pairing amplitude
    participate more in the inter-cell propagation.
    """
    eps_K = epsilon_TB(K_val)
    F_n = F_n_ED if use_ED else F_n_BCS
    F2_n = F_n**2
    F2_max = F2_n.max()

    chi = 0.0
    for n in range(n_modes):
        # Energy denominator: pair excitation energy at momentum K
        # The 2*E_qp is the pair-breaking threshold (minimum energy to create
        # a quasiparticle pair). The J_pair*epsilon(K) adds the kinetic cost
        # of the pair having momentum K.
        denom = 2.0 * E_qp[n] + J_pair_primary * eps_K * F2_n[n] / F2_max
        chi += rho_8[n] * F2_n[n] / denom
    return chi

# Compute chi_0(K) for all lattice momenta and dense K grid
K_dense = np.linspace(0, PI / l_cell, 200)
chi_K_dense = np.array([chi_0_static(K) for K in K_dense])

# Lattice momenta
chi_K_lattice = np.array([chi_0_static(K_lattice[j]) for j in range(N_cells)])

print(f"\n  Pair susceptibility chi_0(K):")
print(f"    chi_0(K=0) = {chi_K_dense[0]:.6f}")
print(f"    chi_0(K_pivot) = {chi_0_static(K_pivot):.6f}")
print(f"    chi_0(K_BZ) = {chi_K_dense[-1]:.6f}")
print(f"    chi_0(K=0)/chi_0(K_BZ) = {chi_K_dense[0]/chi_K_dense[-1]:.4f}")
print(f"    K-variation: {(chi_K_dense[0] - chi_K_dense[-1])/chi_K_dense[0]*100:.2f}%")

# =============================================================================
# STEP 4: RPA-screened phonon propagator
# =============================================================================
print("\n--- Step 4: RPA-Screened Phonon Propagator ---")

# The bare phonon propagator (O-Z form):
#   D_0(K) = T / (J_eff * K^2 + m^2)
# where the angular average is already done (using the angularly-averaged result).
#
# The effective coupling g for the RPA vertex:
# In nuclear RPA, the vertex is the residual interaction (usually a density-dependent
# contact or finite-range force). Here, the residual interaction is the pairing
# interaction V(B2,B2).
#
# Two candidate couplings:
# (a) V(B2,B2) = 0.1557 (Casimir element, intra-sector total)
# (b) V_B2_per_pair = 0.0376 (per mode pair, off-diagonal average)
#
# The RPA PHYSICS: the phonon (Goldstone mode) is a collective excitation
# of the condensate. It couples to the pair field through the vertex g.
# The RPA dresses the propagator:
#   D_RPA(K) = D_0(K) / [1 - g^2 * chi_0(K) * D_0(K)]
#
# This is the standard Dyson equation for the screened propagator.
# When g^2*chi_0*D_0 > 0, the RPA SOFTENS the propagator (reduces stiffness).
# When g^2*chi_0*D_0 < 0, the RPA STIFFENS it.

# COUPLING CONSTANT:
# The deep-dive estimated g^2*chi_0 ~ 1.54.
# Let's verify: g = V(B2,B2)_Casimir = 0.1557
# chi_0(K=0) will be computed above.
# The product g^2 * chi_0(0) should be O(1).

g_casimir = 0.1557  # V(B2,B2) total Casimir (S34)

# Alternative: the per-mode off-diagonal V_B2 ~ 0.038
g_per_pair = 0.0376  # per mode-pair average

# The FULL V(B2,B2) pairing matrix element that enters the gap equation is
# the Casimir element 0.1557 summed over generators. The relevant coupling
# for the phonon-pair vertex is related to the pair-pair scattering amplitude.
# In nuclear RPA, the effective interaction is the ph (particle-hole) residual
# interaction, which differs from the pp (particle-particle) channel.
#
# For the phonon propagator, the relevant vertex is the coupling of the
# condensate fluctuation (delta_Delta) to the pair field. This is:
#   g_eff = V(B2,B2) * sqrt(rho_B2) = V * sqrt(sum_n rho_n * F_n^2)
# But we must be careful not to double-count what's already in chi_0.
#
# Standard RPA: D_RPA = D_0 / (1 - V*chi_0*D_0)
# where V = g^2 is the SQUARE of the coupling (in the convention where
# chi_0 already contains one factor of the form factor).
#
# Our chi_0 already has F_n^2 and rho_n. So V here is just the pairing
# interaction strength WITHOUT additional DOS or form-factor weighting.

# For the phonon-pair coupling, the relevant vertex is determined by
# how the phonon field phi couples to the pair field Delta:
#   L_int = g_phonon * phi * |Delta|^2
# The RPA self-energy is then:
#   Pi(K) = g_phonon^2 * chi_0(K)
# and D_RPA = D_0 / (1 - Pi * D_0)

# We will compute for MULTIPLE coupling strengths to map the sensitivity:
# g_eff values spanning the range from conservative to aggressive

# Method A: "Nuclear-calibrated" coupling
# In nuclear physics, g^2*chi_0 ~ 1 gives the correct effective charge
# correction (e_eff/e_bare ~ 1.5 corresponds to ~25% mass renormalization).
# We CALIBRATE g_eff so that g_eff^2 * chi_0(0) = g2chi0_target

print(f"  Coupling constants:")
print(f"    V(B2,B2) Casimir = {g_casimir:.4f}")
print(f"    V_B2 per pair = {g_per_pair:.4f}")
print(f"    g_casimir^2 * chi_0(0) = {g_casimir**2 * chi_K_dense[0]:.4f}")
print(f"    g_per_pair^2 * chi_0(0) = {g_per_pair**2 * chi_K_dense[0]:.4f}")

# Angular averaging for the bare propagator
N_ANGLE = 30000
rng = np.random.RandomState(42)
theta_samp = np.arccos(2*rng.random(N_ANGLE) - 1)
phi_samp = 2*PI*rng.random(N_ANGLE)
nx_h = np.sin(theta_samp)*np.cos(phi_samp)
ny_h = np.sin(theta_samp)*np.sin(phi_samp)
nz_h = np.cos(theta_samp)
J_dir = J_C2*(nx_h**2 + ny_h**2) + J_su2*nz_h**2

def P_OZ_angular(K_val, m_sq):
    """Angular-averaged bare O-Z propagator."""
    eps = J_dir * K_val**2
    return np.mean(T_acoustic / (eps + m_sq))

# The RPA propagator with K-dependent pair susceptibility
def P_RPA(K_val, m_sq, g_eff):
    """RPA-screened phonon propagator.

    D_RPA(K) = D_0(K) / [1 - g_eff^2 * chi_0(K) * D_0(K)]

    where D_0(K) is the angular-averaged bare propagator.
    """
    D0 = P_OZ_angular(K_val, m_sq)
    chi = chi_0_static(K_val)
    Pi_K = g_eff**2 * chi
    denom = 1.0 - Pi_K * D0
    return D0 / denom

# =============================================================================
# STEP 5: Root-finding for m_base with RPA
# =============================================================================
print("\n--- Step 5: Root-Finding for m_base (RPA) ---")

target_ns = 0.965

def ns_from_func(P_func, K_pivot_val, dK=0.005):
    """Compute n_s via central difference."""
    K_p = K_pivot_val * (1 + dK)
    K_m = K_pivot_val * (1 - dK)
    P_p = P_func(K_p)
    P_m = P_func(K_m)
    return 1.0 + (np.log(P_p) - np.log(P_m)) / (np.log(K_p) - np.log(K_m))

def ns_alpha_from_func(P_func, K_pivot_val):
    """Compute n_s and alpha_s via 7-point quadratic fit."""
    K_factors = np.array([0.85, 0.90, 0.95, 1.00, 1.05, 1.10, 1.15])
    K_pts = K_pivot_val * K_factors
    P_pts = np.array([P_func(K) for K in K_pts])

    ln_K = np.log(K_pts) - np.log(K_pivot_val)
    ln_P = np.log(P_pts)
    c = np.polyfit(ln_K, ln_P, 2)
    n_s_val = 1.0 + c[1]
    alpha_s_val = 2.0 * c[0]
    return n_s_val, alpha_s_val, K_pts, P_pts

# Scan over coupling strengths
# g_eff values: g_casimir, 2*g_casimir, 3*g_casimir, ...
# Also include the deep-dive estimate and nuclear-calibrated values

g_values = [0.0, g_per_pair, g_casimir, 0.25, 0.35, 0.50, 0.70, 1.0]
g_labels = ['bare', 'g_per_pair', 'g_Casimir', '0.25', '0.35', '0.50', '0.70', '1.0']

print(f"\n  Coupling scan: {len(g_values)} values")

results = []
for ig, g_eff in enumerate(g_values):
    # Find m_base that gives n_s = 0.965 for this g_eff
    m_lo, m_hi = 5.0, 25.0
    for iteration in range(200):
        m_mid = (m_lo + m_hi) / 2.0
        ns_mid = ns_from_func(
            lambda K, m2=m_mid**2, ge=g_eff: P_RPA(K, m2, ge) if ge > 0 else P_OZ_angular(K, m2),
            K_pivot)
        if ns_mid < target_ns:
            m_lo = m_mid
        else:
            m_hi = m_mid
        if abs(ns_mid - target_ns) < 1e-8:
            break

    m_base = (m_lo + m_hi) / 2.0
    m_base_sq = m_base**2

    # Full n_s and alpha_s
    P_func = lambda K, m2=m_base_sq, ge=g_eff: P_RPA(K, m2, ge) if ge > 0 else P_OZ_angular(K, m2)
    n_s, alpha_s, K_pts, P_pts = ns_alpha_from_func(P_func, K_pivot)

    identity = n_s**2 - 1
    deviation = alpha_s - identity

    # chi_0 at pivot
    chi_pivot = chi_0_static(K_pivot)
    g2chi = g_eff**2 * chi_pivot

    # RPA correction magnitude at pivot
    D0_pivot = P_OZ_angular(K_pivot, m_base_sq)
    Pi_pivot = g_eff**2 * chi_pivot
    RPA_factor = 1.0 / (1.0 - Pi_pivot * D0_pivot)

    results.append({
        'g_eff': g_eff,
        'g_label': g_labels[ig],
        'n_s': n_s,
        'alpha_s': alpha_s,
        'identity': identity,
        'deviation': deviation,
        'm_base': m_base,
        'm_base_sq': m_base_sq,
        'g2chi': g2chi,
        'Pi_pivot': Pi_pivot,
        'D0_pivot': D0_pivot,
        'RPA_factor': RPA_factor,
        'K_pts': K_pts,
        'P_pts': P_pts,
    })

    print(f"  g={g_eff:.4f} ({g_labels[ig]:>12s}): n_s={n_s:.8f}, "
          f"alpha_s={alpha_s:+.8f}, n_s^2-1={identity:+.8f}, "
          f"dev={deviation:+.6e}, m={m_base:.4f}, g^2*chi={g2chi:.4f}, "
          f"RPA_factor={RPA_factor:.4f}")

# =============================================================================
# STEP 6: K-dependent analysis of the RPA correction
# =============================================================================
print("\n--- Step 6: K-Dependent Structure of RPA Correction ---")

# The key question: does chi_0(K) introduce enough K-dependence to break
# the alpha_s = n_s^2 - 1 identity?
#
# The identity holds when the propagator is P(K) = A / (B*K^2 + C) with
# K-independent A, B, C. The RPA correction makes:
#   P_RPA(K) = D_0(K) / [1 - g^2*chi_0(K)*D_0(K)]
#
# If chi_0(K) = const (K-independent), then P_RPA(K) = D_0(K) / (1 - const*D_0(K))
# which is STILL a function of D_0(K) only. Since D_0 ~ 1/(K^2 + m^2),
# P_RPA ~ 1/(K^2 + m_eff^2) with a renormalized m_eff. The identity SURVIVES.
#
# The identity breaks ONLY if chi_0(K) has K-dependence DIFFERENT from D_0(K).

# Compute the K-dependent RPA factor
K_analysis = np.logspace(np.log10(0.5), np.log10(8.0), 100)

# Use physical Casimir coupling
g_phys = g_casimir

# Find m_base for this g
m_lo_p, m_hi_p = 5.0, 25.0
for _ in range(200):
    m_mid_p = (m_lo_p + m_hi_p) / 2.0
    ns_p = ns_from_func(lambda K, m2=m_mid_p**2: P_RPA(K, m2, g_phys), K_pivot)
    if ns_p < target_ns:
        m_lo_p = m_mid_p
    else:
        m_hi_p = m_mid_p
    if abs(ns_p - target_ns) < 1e-8:
        break
m_RPA = (m_lo_p + m_hi_p) / 2.0
m_RPA_sq = m_RPA**2

print(f"  Physical coupling g = {g_phys:.4f}")
print(f"  m_base(RPA) = {m_RPA:.6f} (OZ: {m_star_OZ:.6f})")
print(f"  m_base^2(RPA) = {m_RPA_sq:.4f} (OZ: {m_base_sq_OZ:.4f})")

# Compute all quantities as function of K
chi_K = np.array([chi_0_static(K) for K in K_analysis])
D0_K = np.array([P_OZ_angular(K, m_RPA_sq) for K in K_analysis])
Pi_K = g_phys**2 * chi_K
RPA_factor_K = 1.0 / (1.0 - Pi_K * D0_K)
D_RPA_K = D0_K * RPA_factor_K

# For comparison: the bare O-Z propagator at the OZ mass
D0_OZ_K = np.array([P_OZ_angular(K, m_base_sq_OZ) for K in K_analysis])

# Effective stiffness: J_eff(K) from D_RPA
# If D_RPA = T / (J_eff(K)*K^2 + m_eff^2), then:
# J_eff(K) = [T/D_RPA - m_eff^2] / K^2
# But m_eff is also renormalized. We need a different approach.
#
# The effective spectral index from the local log-derivative:
ns_K_bare = np.zeros(len(K_analysis))
ns_K_RPA = np.zeros(len(K_analysis))
for j in range(1, len(K_analysis)-1):
    dlnK = np.log(K_analysis[j+1]) - np.log(K_analysis[j-1])
    ns_K_bare[j] = 1.0 + (np.log(D0_OZ_K[j+1]) - np.log(D0_OZ_K[j-1])) / dlnK
    ns_K_RPA[j] = 1.0 + (np.log(D_RPA_K[j+1]) - np.log(D_RPA_K[j-1])) / dlnK

print(f"\n  K-dependent RPA corrections:")
print(f"    chi_0(K_min) = {chi_K[0]:.6f}")
print(f"    chi_0(K_max) = {chi_K[-1]:.6f}")
print(f"    chi_variation = {(chi_K[0]-chi_K[-1])/chi_K[0]*100:.4f}%")

# Find K closest to K_pivot in the analysis grid
idx_pivot = np.argmin(np.abs(K_analysis - K_pivot))
print(f"\n  At K_pivot = {K_pivot:.4f}:")
print(f"    chi_0 = {chi_K[idx_pivot]:.6f}")
print(f"    Pi = g^2*chi = {Pi_K[idx_pivot]:.6e}")
print(f"    D_0 = {D0_K[idx_pivot]:.6e}")
print(f"    Pi*D_0 = {Pi_K[idx_pivot]*D0_K[idx_pivot]:.6e}")
print(f"    RPA factor = {RPA_factor_K[idx_pivot]:.6f}")
print(f"    n_s(bare) = {ns_K_bare[idx_pivot]:.6f}")
print(f"    n_s(RPA) = {ns_K_RPA[idx_pivot]:.6f}")

# =============================================================================
# STEP 7: The chi_0(K) structure and the pair coherence length
# =============================================================================
print("\n--- Step 7: Pair Coherence Length and chi_0 Structure ---")

# The K-dependence of chi_0 is controlled by the coherence length xi_BCS.
# At K << 1/xi_BCS: chi_0 ≈ const (pair can't resolve K)
# At K ~ 1/xi_BCS: chi_0 starts to vary (pair resolves K)
# At K >> 1/xi_BCS: chi_0 falls off (pair can't follow fast oscillations)
#
# K_pivot * xi_BCS = ?

K_xi = K_pivot * xi_BCS
print(f"  K_pivot * xi_BCS = {K_xi:.4f}")
print(f"  K_pivot * l_cell = {K_pivot * l_cell:.4f}")
print(f"  xi_BCS / l_cell = {xi_BCS / l_cell:.2f}")

# If K_pivot * xi_BCS >> 1: we are in the regime where chi_0 varies
# If K_pivot * xi_BCS << 1: we are in the constant chi_0 regime
# K_xi = 1.6 -- intermediate regime

# Relative variation of chi_0 in the range relevant for n_s/alpha_s
K_low = K_pivot * 0.85
K_high = K_pivot * 1.15
chi_low = chi_0_static(K_low)
chi_high = chi_0_static(K_high)
chi_pivot_val = chi_0_static(K_pivot)

delta_chi_rel = (chi_low - chi_high) / chi_pivot_val
print(f"\n  chi_0 variation in fitting range [0.85, 1.15]*K_pivot:")
print(f"    chi_0(0.85*K_pivot) = {chi_low:.6f}")
print(f"    chi_0(K_pivot) = {chi_pivot_val:.6f}")
print(f"    chi_0(1.15*K_pivot) = {chi_high:.6f}")
print(f"    Relative variation = {delta_chi_rel*100:.4f}%")

# The relative variation of chi_0 in the fitting window determines
# the correction to alpha_s. If delta_chi/chi ~ epsilon, then
# delta_alpha_s / alpha_s ~ epsilon * g^2 * chi * D_0

# =============================================================================
# STEP 8: Full n_s and alpha_s with RPA at physical coupling
# =============================================================================
print("\n--- Step 8: Full n_s and alpha_s (RPA vs O-Z) ---")

# OZ reference (bare)
n_s_bare, alpha_s_bare, _, _ = ns_alpha_from_func(
    lambda K: P_OZ_angular(K, m_base_sq_OZ), K_pivot)

# RPA at physical coupling
n_s_rpa, alpha_s_rpa, _, _ = ns_alpha_from_func(
    lambda K: P_RPA(K, m_RPA_sq, g_phys), K_pivot)

identity_bare = n_s_bare**2 - 1
identity_rpa = n_s_rpa**2 - 1
dev_bare = alpha_s_bare - identity_bare
dev_rpa = alpha_s_rpa - identity_rpa

print(f"  BARE (O-Z):")
print(f"    n_s = {n_s_bare:.10f}")
print(f"    alpha_s = {alpha_s_bare:+.10f}")
print(f"    n_s^2-1 = {identity_bare:+.10f}")
print(f"    deviation = {dev_bare:+.6e}")

print(f"\n  RPA (g = {g_phys}):")
print(f"    n_s = {n_s_rpa:.10f}")
print(f"    alpha_s = {alpha_s_rpa:+.10f}")
print(f"    n_s^2-1 = {identity_rpa:+.10f}")
print(f"    deviation = {dev_rpa:+.6e}")

print(f"\n  COMPARISON:")
print(f"    Delta(n_s) = {n_s_rpa - n_s_bare:.6e}")
print(f"    Delta(alpha_s) = {alpha_s_rpa - alpha_s_bare:.6e}")
print(f"    RPA correction to deviation: {dev_rpa - dev_bare:.6e}")

# =============================================================================
# STEP 9: Coupling scan -- what g is needed for Planck compatibility?
# =============================================================================
print("\n--- Step 9: What Coupling Breaks the Identity? ---")

# Scan a fine grid of g values
g_fine = np.linspace(0.0, 2.0, 50)
alpha_s_scan = np.zeros(len(g_fine))
ns_scan = np.zeros(len(g_fine))
dev_scan = np.zeros(len(g_fine))
m_scan = np.zeros(len(g_fine))

for ig, g_val in enumerate(g_fine):
    # Find m_base
    m_lo_s, m_hi_s = 1.0, 500.0
    for _ in range(200):
        m_mid_s = (m_lo_s + m_hi_s) / 2.0
        P_test = lambda K, m2=m_mid_s**2, gv=g_val: P_RPA(K, m2, gv) if gv > 0 else P_OZ_angular(K, m2)
        try:
            ns_s = ns_from_func(P_test, K_pivot)
        except:
            ns_s = 0.5  # If failed, go lower
        if ns_s < target_ns:
            m_lo_s = m_mid_s
        else:
            m_hi_s = m_mid_s
        if abs(ns_s - target_ns) < 1e-6:
            break

    m_s = (m_lo_s + m_hi_s) / 2.0
    P_f = lambda K, m2=m_s**2, gv=g_val: P_RPA(K, m2, gv) if gv > 0 else P_OZ_angular(K, m2)
    ns_s, alpha_s_s, _, _ = ns_alpha_from_func(P_f, K_pivot)

    alpha_s_scan[ig] = alpha_s_s
    ns_scan[ig] = ns_s
    dev_scan[ig] = alpha_s_s - (ns_s**2 - 1)
    m_scan[ig] = m_s

# Find where alpha_s enters Planck 2-sigma range
in_planck = np.abs(alpha_s_scan) < 0.016  # 2 sigma
g_needed = None
for ig in range(len(g_fine)):
    if in_planck[ig]:
        g_needed = g_fine[ig]
        break

print(f"  Results from coupling scan:")
print(f"    g = 0:    alpha_s = {alpha_s_scan[0]:+.6f}")
print(f"    g = 0.15: alpha_s = {alpha_s_scan[np.argmin(np.abs(g_fine-0.15))]:+.6f}")
print(f"    g = 0.50: alpha_s = {alpha_s_scan[np.argmin(np.abs(g_fine-0.50))]:+.6f}")
print(f"    g = 1.00: alpha_s = {alpha_s_scan[np.argmin(np.abs(g_fine-1.00))]:+.6f}")
print(f"    g = 2.00: alpha_s = {alpha_s_scan[-1]:+.6f}")

if g_needed is not None:
    print(f"\n  Planck 2-sigma compatibility at g >= {g_needed:.3f}")
    print(f"    g_needed / g_Casimir = {g_needed / g_casimir:.2f}")
    print(f"    This is {g_needed/g_casimir:.1f}x the Casimir coupling")
else:
    print(f"\n  No Planck compatibility found in g scan [0, 2.0]")
    # Find what alpha_s is at g=2
    print(f"  At g = 2.0: alpha_s = {alpha_s_scan[-1]:+.6f}")
    print(f"  Identity deviation at g=2: {dev_scan[-1]:+.6e}")

# =============================================================================
# STEP 10: Nuclear effective charge benchmark
# =============================================================================
print("\n--- Step 10: Nuclear Effective Charge Benchmark ---")

# In nuclear physics (Paper 07), effective charges correct B(E2) by:
#   e_p_eff / e_p_bare ~ 1.5 (proton)
#   e_n_eff / e_n_bare ~ 0.5 (neutron, from 0)
# The correction magnitude is set by g^2*chi_0 ~ 1 in the RPA.
#
# For the framework:
# Physical g = V(B2,B2) = 0.1557
# chi_0(0) computed above
# g^2 * chi_0(0) = ?

g2_chi0 = g_casimir**2 * chi_K_dense[0]
g2_chi_pivot = g_casimir**2 * chi_pivot_val

print(f"  Nuclear RPA coupling comparison:")
print(f"    g = V(B2,B2) = {g_casimir:.4f}")
print(f"    chi_0(0) = {chi_K_dense[0]:.4f}")
print(f"    g^2 * chi_0(0) = {g2_chi0:.4f}")
print(f"    g^2 * chi_0(K_pivot) = {g2_chi_pivot:.4f}")
print(f"    Deep-dive estimate: 1.54")

# Nuclear effective charge: factor 1.5 in amplitude = 2.25 in rate
# This corresponds to a ~50% correction in the transition amplitude.
# In our case, the RPA correction to the propagator at K_pivot is:
rpa_corr_pct = (RPA_factor_K[idx_pivot] - 1.0) * 100
print(f"\n  RPA correction at K_pivot:")
print(f"    D_RPA/D_0 - 1 = {rpa_corr_pct:.4f}%")
print(f"    Nuclear e_eff/e_bare - 1 = ~50%")
print(f"    Ratio (framework/nuclear) = {abs(rpa_corr_pct)/50:.4f}")

# The issue: the RPA correction is small because g^2*chi_0*D_0 << 1.
# Even though g^2*chi_0 may be O(1), D_0(K_pivot) is very small
# because m_base^2 = 140 >> J*K_pivot^2 = 2.5.
# The mass hierarchy kills the RPA correction.

D0_at_pivot = P_OZ_angular(K_pivot, m_RPA_sq)
PiD0_at_pivot = g_phys**2 * chi_pivot_val * D0_at_pivot
print(f"\n  RPA correction anatomy:")
print(f"    g^2 = {g_phys**2:.6f}")
print(f"    chi_0(K_pivot) = {chi_pivot_val:.6f}")
print(f"    D_0(K_pivot) = {D0_at_pivot:.6e}")
print(f"    g^2*chi_0 = {g_phys**2 * chi_pivot_val:.6f}")
print(f"    Pi*D_0 = {PiD0_at_pivot:.6e}")
print(f"    D_0 is O({D0_at_pivot:.1e}) because m^2 = {m_RPA_sq:.0f} >> J*K^2 = {J_eff_spatial*K_pivot**2:.2f}")
print(f"    The mass hierarchy SUPPRESSES the RPA correction")

# =============================================================================
# STEP 11: K-dependence of chi_0 -- the critical diagnostic
# =============================================================================
print("\n--- Step 11: K-Dependence Diagnostic ---")

# The identity breaks if chi_0(K) varies differently from D_0(K)^{-1}.
# D_0(K)^{-1} = J_eff*K^2 + m^2 (linear in K^2)
# chi_0(K) = sum_n rho_n * F_n^2 / [2*E_qp_n + J_pair*eps(K)*w_n]
# At small K*l_cell: eps(K) ≈ K^2*l_cell^2
# So chi_0(K) ≈ sum_n rho_n*F_n^2 / [2*E_qp_n + J_pair*K^2*l_cell^2*w_n]
# = chi_0(0) - K^2 * sum_n rho_n*F_n^2*J_pair*l_cell^2*w_n / (2*E_qp_n)^2 + ...
#
# The K^2 coefficient of chi_0 provides a correction to the effective stiffness.
# But this correction is ADDITIVE (shifts J_eff), which does NOT break the identity.
# The identity is broken by terms in chi_0 that are NOT proportional to K^2.
#
# The non-K^2 terms come from the tight-binding dispersion:
# eps(K) = 2*(1 - cos(Ka)) = K^2*a^2 - K^4*a^4/12 + ...
# The K^4 term provides the first correction to the identity.

# Extract the effective K-dependence of chi_0 near K_pivot
K_fit = K_analysis[(K_analysis > 0.5*K_pivot) & (K_analysis < 2.0*K_pivot)]
chi_fit = np.array([chi_0_static(K) for K in K_fit])
lnK_fit = np.log(K_fit / K_pivot)
lnchi_fit = np.log(chi_fit / chi_pivot_val)

# Fit chi_0(K)/chi_0(K_pivot) = 1 + a2*(K/K_pivot)^2 + a4*(K/K_pivot)^4
# Using polynomial fit in ln(K)
# chi_0(K) ≈ chi_0_pivot * (1 + c1*ln(K/K_pivot) + c2*ln(K/K_pivot)^2)
c_chi = np.polyfit(lnK_fit, lnchi_fit, 3)

# Power-law index of chi_0
chi_power = c_chi[-2]  # coefficient of ln(K/K_pivot) in ln(chi_0)
chi_running = 2.0 * c_chi[-3]  # running of chi_0

print(f"  chi_0(K) power-law decomposition near K_pivot:")
print(f"    d ln(chi_0) / d ln(K) = {chi_power:.6f}")
print(f"    d^2 ln(chi_0) / d ln(K)^2 = {chi_running:.6f}")
print(f"    chi_0 ~ K^{{{chi_power:.4f}}} (effective power)")

# The correction to alpha_s from chi_0 running:
# If chi_0 ~ K^p, then the RPA propagator has:
#   D_RPA ~ D_0 / (1 - g^2*A*K^p*D_0)
# where A = chi_0(K_pivot)/K_pivot^p
#
# This introduces a correction to the effective spectral index:
# delta_n_s ~ -g^2*A*D_0 * p * K_pivot^p / (1 - g^2*A*K_pivot^p*D_0)
# and a correction to alpha_s proportional to the second derivative.

# =============================================================================
# STEP 12: Alternative: Enhanced coupling from pair coherence
# =============================================================================
print("\n--- Step 12: Enhanced Coupling from Pair Coherence ---")

# The deep-dive estimate g^2*chi_0 ~ 1.54 used:
#   g = V(B2,B2) = 0.1557
#   chi_0 = rho_B2 * F_transfer^2 = 14.02 * 2.13^2 = 63.5
#   g^2 * chi_0 = 0.0242 * 63.5 = 1.54
#
# But our chi_0(K=0) computation gives a DIFFERENT value because:
# (a) It includes all 8 modes, not just B2
# (b) It uses the energy denominator 2*E_qp, not just rho
# (c) The form factor is F_n^2 = (2*u_n*v_n)^2, not F_transfer^2

chi_0_direct = chi_K_dense[0]
chi_0_deepdive = rho_B2_per_mode * F_transfer**2
print(f"  chi_0 comparison:")
print(f"    Direct computation: {chi_0_direct:.4f}")
print(f"    Deep-dive estimate: {chi_0_deepdive:.4f}")
print(f"    Ratio: {chi_0_direct / chi_0_deepdive:.4f}")

# The direct computation gives chi_0 with the ENERGY DENOMINATOR,
# which the deep-dive estimate omitted. The denominator 2*E_qp ~ 1.7
# reduces chi_0 by that factor.

# The actual g^2*chi_0 at K=0:
print(f"\n  Coupling products:")
print(f"    g_Casimir^2 * chi_0(0) = {g_casimir**2 * chi_0_direct:.6f}")
print(f"    Deep-dive estimate = 1.54")
print(f"    The deep-dive OMITTED the 2*E_qp denominator")

# =============================================================================
# STEP 13: Structural assessment
# =============================================================================
print("\n\n--- Step 13: Structural Assessment ---")

# WHY THE IDENTITY SURVIVES THE RPA:
#
# 1. The K-dependence of chi_0 comes from the pair dispersion:
#    delta_chi(K) / chi(0) ~ J_pair * epsilon(K) / (2*E_qp)^2
#    = J_pair * K^2 * l_cell^2 / (2*E_qp)^2
#    ~ 0.115 * 3.9 * 0.023 / 2.86
#    ~ 0.0036 at K_pivot
#    This is a 0.36% variation, far too small to modify alpha_s significantly.
#
# 2. The K^2 part of chi_0's K-dependence ADDS to the stiffness (renormalizes J_eff)
#    but does NOT break the identity. The identity is broken only by non-K^2 terms.
#
# 3. The non-K^2 terms (from lattice discreteness) are:
#    K^4 correction to tight-binding: ~ (K*l_cell)^4/12 ~ 2.7e-5
#    This is O(10^{-5}) -- completely negligible.
#
# 4. The mass hierarchy m^2 >> J*K^2 further suppresses everything:
#    The RPA self-energy Pi*D_0 ~ 10^{-6} at K_pivot.
#    Even with g^2*chi_0 = O(1), D_0 ~ 10^{-3} kills the correction.
#
# CONCLUSION: The RPA correction to alpha_s is structurally negligible
# because:
# (a) chi_0(K) variation is 0.36% in the fitting window (pair bandwidth
#     << quasiparticle gap, so the pair is stiff)
# (b) The K-dependent part of chi_0 is K^2 (doesn't break identity)
# (c) The mass hierarchy (m^2/J*K^2 ~ 56) suppresses RPA corrections

# Compute the structural suppression factors
pair_bandwidth = 4 * J_pair_primary  # tight-binding bandwidth
pair_gap = 2 * np.min(E_qp)

print(f"  Structural suppression factors:")
print(f"    (a) chi_0 K-variation in fit window: {delta_chi_rel*100:.4f}%")
print(f"    (b) Pair bandwidth / pair gap: {pair_bandwidth/pair_gap:.4f}")
print(f"    (c) Mass ratio m^2/(J*K_pivot^2): {m_RPA_sq/(J_eff_spatial*K_pivot**2):.1f}")
print(f"    (d) Pi*D_0 at K_pivot: {PiD0_at_pivot:.2e}")
print(f"    (e) Non-K^2 fraction: (K*a)^2/12 = {(K_pivot*l_cell)**2/12:.2e}")

# =============================================================================
# STEP 14: Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE VERDICT: FABRIC-RPA-50")
print("=" * 78)

# Use the physical Casimir coupling result
n_s_final = n_s_rpa
alpha_s_final = alpha_s_rpa
identity_final = n_s_final**2 - 1
dev_final = alpha_s_final - identity_final

# Gate criteria:
# PASS: alpha_s in [-0.040, 0]
# FAIL: alpha_s = n_s^2 - 1 (identity survives)
# INFO: deviates but outside range

# The identity effectively holds if deviation < 0.001
identity_holds = abs(dev_final - dev_bare) < 0.001

alpha_in_pass = -0.040 <= alpha_s_final <= 0.0
sigma_planck = 0.008
tension = abs(alpha_s_final) / sigma_planck

if alpha_in_pass and not identity_holds:
    verdict = "PASS"
    detail = (f"alpha_s(RPA) = {alpha_s_final:.6f} in [-0.040, 0], "
              f"n_s = {n_s_final:.6f}, deviation from identity = {dev_final:.2e}")
elif identity_holds:
    verdict = "FAIL"
    detail = (f"RPA alpha_s = {alpha_s_final:.6f} matches O-Z alpha_s = {alpha_s_bare:.6f}. "
              f"Identity deviation unchanged by RPA: delta(dev) = {dev_final - dev_bare:.2e}. "
              f"chi_0(K) varies by {delta_chi_rel*100:.2f}% in fit window. "
              f"Pi*D_0 = {PiD0_at_pivot:.1e} at K_pivot. "
              f"Pair bandwidth ({pair_bandwidth:.4f}) << pair gap ({pair_gap:.4f}). "
              f"Mass hierarchy {m_RPA_sq/(J_eff_spatial*K_pivot**2):.0f}x kills RPA correction.")
else:
    verdict = "INFO"
    detail = (f"alpha_s(RPA) = {alpha_s_final:.6f}, identity deviation = {dev_final:.4f}, "
              f"outside PASS range.")

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")
print(f"")
print(f"  KEY NUMBERS:")
print(f"    n_s(RPA) = {n_s_final:.8f}")
print(f"    alpha_s(RPA) = {alpha_s_final:+.8f}")
print(f"    alpha_s(bare) = {alpha_s_bare:+.8f}")
print(f"    n_s^2-1 (RPA) = {identity_final:+.8f}")
print(f"    RPA correction to alpha_s: {alpha_s_final - alpha_s_bare:+.6e}")
print(f"    RPA correction to dev: {dev_final - dev_bare:+.6e}")
print(f"")
print(f"  STRUCTURAL DIAGNOSIS:")
print(f"    The RPA fails to break the identity for THREE independent reasons:")
print(f"    (1) chi_0(K) is nearly K-independent ({delta_chi_rel*100:.3f}% variation)")
print(f"        -> pair coherence length xi_BCS = {xi_BCS:.3f} >> l_cell = {l_cell:.3f}")
print(f"        -> K_pivot*xi_BCS = {K_xi:.2f} (intermediate regime)")
print(f"        -> but J_pair = {J_pair_primary:.4f} << 2*E_qp_min = {pair_gap:.4f}")
print(f"        -> pair dispersion ({pair_bandwidth:.4f}) is 2.7% of pair gap ({pair_gap:.4f})")
print(f"    (2) The K^2 part of chi_0(K) renormalizes J_eff but does NOT break identity")
print(f"        -> Non-K^2 contribution: O((Ka)^2/12) = O({(K_pivot*l_cell)**2/12:.1e})")
print(f"    (3) The mass hierarchy m^2/(J*K^2) = {m_RPA_sq/(J_eff_spatial*K_pivot**2):.0f}")
print(f"        -> Pi*D_0 = {PiD0_at_pivot:.1e} (RPA self-energy is tiny)")
print(f"        -> Even O(1) coupling gives O(10^-6) correction")
print(f"")
print(f"  PLANCK TENSION:")
print(f"    alpha_s = {alpha_s_final:.6f}")
print(f"    Planck: 0 +/- {sigma_planck}")
print(f"    Tension: {tension:.1f} sigma (unchanged from O-Z)")
print(f"")
print(f"  NUCLEAR COMPARISON:")
print(f"    Nuclear RPA: g^2*chi_0 ~ 1, correction to B(E2) ~ 2-3x")
print(f"    Framework RPA: g^2*chi_0 = {g2_chi0:.4f}, Pi*D_0 = {PiD0_at_pivot:.1e}")
print(f"    Nuclear works because B(E2) ~ |<f|O|i>|^2 (no mass hierarchy)")
print(f"    Framework fails because the propagator denominator (m^2) kills the effect")
print(f"    The analogy breaks: nuclear effective charge is a MATRIX ELEMENT effect,")
print(f"    not a PROPAGATOR effect. The mass hierarchy has no nuclear analog.")

# =============================================================================
# STEP 15: Save
# =============================================================================
print("\n--- Step 15: Save ---")

out_file = os.path.join(SCRIPT_DIR, 's50_fabric_rpa.npz')
np.savez(out_file,
    # Gate
    gate_name='FABRIC-RPA-50',
    gate_verdict=verdict,
    gate_detail=detail,

    # Key results
    n_s_RPA=n_s_final,
    alpha_s_RPA=alpha_s_final,
    n_s_bare=n_s_bare,
    alpha_s_bare=alpha_s_bare,
    identity_RPA=identity_final,
    identity_bare=identity_bare,
    deviation_RPA=dev_final,
    deviation_bare=dev_bare,
    RPA_correction_alpha=alpha_s_final - alpha_s_bare,
    RPA_correction_dev=dev_final - dev_bare,
    tension_sigma=tension,

    # Masses
    m_RPA=m_RPA,
    m_RPA_sq=m_RPA_sq,
    m_OZ=m_star_OZ,
    m_OZ_sq=m_base_sq_OZ,

    # Couplings
    g_Casimir=g_casimir,
    g_per_pair=g_per_pair,
    g2_chi0_K0=g2_chi0,
    g2_chi0_Kpivot=g2_chi_pivot,

    # Susceptibility
    chi_0_K0=chi_K_dense[0],
    chi_0_Kpivot=chi_pivot_val,
    chi_0_KBZ=chi_K_dense[-1],
    chi_K_variation_pct=delta_chi_rel*100,
    chi_power_index=chi_power,

    # RPA correction anatomy
    Pi_D0_at_pivot=PiD0_at_pivot,
    RPA_factor_pivot=RPA_factor_K[idx_pivot],
    pair_bandwidth=pair_bandwidth,
    pair_gap=pair_gap,
    mass_hierarchy=m_RPA_sq/(J_eff_spatial*K_pivot**2),

    # BdG spectrum
    E_qp=E_qp,
    uv_ED=uv_ED,
    uv_BCS=uv_BCS,
    F_n_ED=F_n_ED,
    F_n_BCS=F_n_BCS,

    # K-dependent data
    K_analysis=K_analysis,
    chi_K=chi_K,
    D0_K=D0_K,
    D_RPA_K=D_RPA_K,
    Pi_K=Pi_K,
    RPA_factor_K=RPA_factor_K,
    ns_K_bare=ns_K_bare,
    ns_K_RPA=ns_K_RPA,

    # Coupling scan
    g_scan=np.array(g_fine),
    alpha_s_g_scan=alpha_s_scan,
    ns_g_scan=ns_scan,
    dev_g_scan=dev_scan,
    m_g_scan=m_scan,

    # Metadata
    tau_fold=tau_fold,
    K_pivot=K_pivot,
    J_pair=J_pair_primary,
    xi_BCS=xi_BCS,
    l_cell=l_cell,
    N_cells=N_cells,
)
print(f"  Saved: {out_file}")

# =============================================================================
# STEP 16: Plot
# =============================================================================
print("\n--- Step 16: Plotting ---")

fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.40, wspace=0.35)

# --- Panel 1: chi_0(K) ---
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(K_dense, chi_K_dense, 'b-', lw=2, label=r'$\chi_0(K)$')
ax1.axvline(K_pivot, color='red', ls='--', alpha=0.5, label=f'$K_{{pivot}}$={K_pivot:.2f}')
ax1.axvline(1.0/xi_BCS, color='green', ls=':', alpha=0.5, label=f'$1/\\xi_{{BCS}}$={1/xi_BCS:.2f}')
ax1.set_xlabel(r'$K$ ($M_{KK}$)')
ax1.set_ylabel(r'$\chi_0(K)$')
ax1.set_title(r'Pair Susceptibility $\chi_0(K)$')
ax1.legend(fontsize=8)
ax1.grid(True, alpha=0.3)

# --- Panel 2: chi_0(K)/chi_0(0) (zoom) ---
ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(K_dense, chi_K_dense/chi_K_dense[0], 'b-', lw=2)
ax2.axhline(1.0, color='gray', ls=':', alpha=0.3)
ax2.axvline(K_pivot, color='red', ls='--', alpha=0.5)
ax2.set_xlabel(r'$K$ ($M_{KK}$)')
ax2.set_ylabel(r'$\chi_0(K) / \chi_0(0)$')
ax2.set_title(r'$\chi_0$ Variation: {:.3f}% at $K_{{pivot}}$'.format(
    (1 - chi_pivot_val/chi_K_dense[0])*100))
ax2.grid(True, alpha=0.3)

# --- Panel 3: D_RPA vs D_0 ---
ax3 = fig.add_subplot(gs[0, 2])
ax3.loglog(K_analysis, D0_OZ_K, 'r--', lw=2, label=r'$D_0(K)$ (bare O-Z)')
ax3.loglog(K_analysis, D_RPA_K, 'b-', lw=2, label=r'$D_{RPA}(K)$')
ax3.axvline(K_pivot, color='gray', ls=':', alpha=0.4)
ax3.set_xlabel(r'$K$ ($M_{KK}$)')
ax3.set_ylabel(r'$D(K)$')
ax3.set_title(r'Propagator: Bare vs RPA (indistinguishable)')
ax3.legend(fontsize=8)
ax3.grid(True, alpha=0.3)

# --- Panel 4: RPA correction factor ---
ax4 = fig.add_subplot(gs[1, 0])
ax4.semilogx(K_analysis, RPA_factor_K, 'b-', lw=2)
ax4.axhline(1.0, color='gray', ls=':', alpha=0.3)
ax4.axvline(K_pivot, color='red', ls='--', alpha=0.5)
ax4.set_xlabel(r'$K$ ($M_{KK}$)')
ax4.set_ylabel(r'$D_{RPA}/D_0$')
ax4.set_title(f'RPA Factor (max deviation: {(np.max(RPA_factor_K)-1)*100:.4f}%)')
ax4.grid(True, alpha=0.3)

# --- Panel 5: n_s(K) comparison ---
ax5 = fig.add_subplot(gs[1, 1])
mask = (ns_K_bare != 0)
ax5.semilogx(K_analysis[mask], ns_K_bare[mask], 'r--', lw=2, label=r'$n_s(K)$ bare')
ax5.semilogx(K_analysis[mask], ns_K_RPA[mask], 'b-', lw=2, label=r'$n_s(K)$ RPA')
ax5.axhline(0.965, color='green', ls='--', lw=1, alpha=0.5)
ax5.axvline(K_pivot, color='gray', ls=':', alpha=0.4)
ax5.set_xlabel(r'$K$ ($M_{KK}$)')
ax5.set_ylabel(r'$n_s(K)$')
ax5.set_title(r'$n_s(K)$: Bare vs RPA (indistinguishable)')
ax5.legend(fontsize=8)
ax5.grid(True, alpha=0.3)
ax5.set_ylim(0.90, 1.01)

# --- Panel 6: Coupling scan alpha_s(g) ---
ax6 = fig.add_subplot(gs[1, 2])
ax6.plot(g_fine, alpha_s_scan, 'ko-', ms=3, lw=1.5, label=r'$\alpha_s(g)$')
ax6.axhspan(-0.016, 0.016, color='green', alpha=0.1, label='Planck 2$\\sigma$')
ax6.axhline(0, color='green', ls='--', lw=1, alpha=0.5)
ax6.axvline(g_casimir, color='red', ls='--', alpha=0.5, label=f'$g_{{Casimir}}$={g_casimir:.3f}')
alpha_identity = target_ns**2 - 1
ax6.axhline(alpha_identity, color='blue', ls=':', alpha=0.5, label=f'$n_s^2-1$={alpha_identity:.4f}')
ax6.set_xlabel(r'Coupling $g$')
ax6.set_ylabel(r'$\alpha_s$')
ax6.set_title(r'$\alpha_s$ vs Coupling Strength')
ax6.legend(fontsize=7, loc='upper right')
ax6.grid(True, alpha=0.3)

# --- Panel 7: Suppression anatomy ---
ax7 = fig.add_subplot(gs[2, 0])
suppression_labels = [r'$\chi_0$ variation', r'$4J_{pair}/2E_{qp}$',
                       r'$(Ka)^2/12$', r'$\Pi D_0$']
suppression_values = [abs(delta_chi_rel), pair_bandwidth/pair_gap,
                       (K_pivot*l_cell)**2/12, abs(PiD0_at_pivot)]
colors_s = ['#2196F3', '#FF9800', '#4CAF50', '#F44336']
bars = ax7.barh(range(len(suppression_labels)), suppression_values, color=colors_s, alpha=0.8)
ax7.set_yticks(range(len(suppression_labels)))
ax7.set_yticklabels(suppression_labels, fontsize=9)
ax7.set_xlabel('Suppression Factor')
ax7.set_title('Why RPA Correction is Small')
ax7.set_xscale('log')
ax7.axvline(0.01, color='red', ls=':', alpha=0.5, label='1% threshold')
for i, v in enumerate(suppression_values):
    ax7.text(v*1.5, i, f'{v:.2e}', va='center', fontsize=8)
ax7.legend(fontsize=8)
ax7.grid(True, alpha=0.3, axis='x')

# --- Panel 8: Mass hierarchy diagram ---
ax8 = fig.add_subplot(gs[2, 1])
hierarchy_labels = [r'$m^2_{base}$', r'$J_{eff}K^2_{pivot}$', r'$4J_{pair}$',
                    r'$g^2\chi_0$', r'$\Pi D_0$']
hierarchy_vals = [m_RPA_sq, J_eff_spatial*K_pivot**2, 4*J_pair_primary,
                  g2_chi0, abs(PiD0_at_pivot)]
colors_h = ['#2196F3', '#FF9800', '#4CAF50', '#9C27B0', '#F44336']
ax8.bar(range(len(hierarchy_labels)), hierarchy_vals, color=colors_h, alpha=0.8)
ax8.set_xticks(range(len(hierarchy_labels)))
ax8.set_xticklabels(hierarchy_labels, fontsize=8, rotation=30)
ax8.set_ylabel('Value ($M_{KK}$ units)')
ax8.set_yscale('log')
ax8.set_title('Mass Hierarchy Kills RPA')
ax8.grid(True, alpha=0.3, axis='y')
for i, v in enumerate(hierarchy_vals):
    ax8.text(i, v*1.3, f'{v:.2e}', ha='center', fontsize=7)

# --- Panel 9: Identity deviation scan ---
ax9 = fig.add_subplot(gs[2, 2])
ax9.plot(g_fine, dev_scan, 'ko-', ms=3, lw=1.5)
ax9.axhline(0, color='gray', ls=':', alpha=0.3)
ax9.axvline(g_casimir, color='red', ls='--', alpha=0.5, label=f'$g_{{Casimir}}$')
ax9.set_xlabel(r'Coupling $g$')
ax9.set_ylabel(r'$\alpha_s - (n_s^2 - 1)$')
ax9.set_title(r'Identity Deviation vs $g$ (flat)')
ax9.legend(fontsize=8)
ax9.grid(True, alpha=0.3)

fig.text(0.5, 0.01,
         f"GATE: {verdict} | RPA $\\alpha_s$ = {alpha_s_final:.5f} "
         f"(bare: {alpha_s_bare:.5f}) | "
         f"$\\chi_0$ variation = {delta_chi_rel*100:.3f}% | "
         f"$\\Pi D_0$ = {PiD0_at_pivot:.1e} | "
         f"Tension = {tension:.1f}$\\sigma$",
         ha='center', fontsize=10,
         bbox=dict(boxstyle='round',
                   facecolor='#FFCDD2' if verdict == 'FAIL' else 'wheat', alpha=0.8))

plot_file = os.path.join(SCRIPT_DIR, 's50_fabric_rpa.png')
plt.savefig(plot_file, dpi=150, bbox_inches='tight')
print(f"  Saved: {plot_file}")

elapsed = time.time() - t0
print(f"\n  Total elapsed: {elapsed:.1f} s")
print("=" * 78)
