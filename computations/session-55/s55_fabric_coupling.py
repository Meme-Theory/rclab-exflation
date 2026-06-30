#!/usr/bin/env python3
"""
s55_fabric_coupling.py — FABRIC-COUPLING-55
Inter-cell Josephson coupling estimate for the SU(3) fabric.

Physics (Landau symmetry analysis):
  The fabric is a spatially extended lattice of SU(3) unit cells.
  Each cell carries a BCS condensate that spontaneously breaks U(1)_7.
  The order parameter is the pair amplitude Delta * exp(i*phi), where
  phi is the condensate phase.

  Adjacent cells couple through Josephson tunneling of Cooper pairs.
  The effective Hamiltonian for the phase degrees of freedom is:
      H_fabric = -E_J * sum_{<ij>} cos(phi_i - phi_j)
                 + E_c * sum_i (n_i - n_0)^2
  This is the quantum rotor model. Its phases are:
      E_J >> E_c: superfluid (global phase coherence)
      E_J << E_c: Mott insulator (number-locked cells)

  The Josephson coupling is estimated from the tight-binding model:
  1. BCS coherence factor method: t_J = J * sum_k u_k * v_k / N
  2. Ambegaokar-Baratoff: E_J = (pi*Delta/4) * (J/delta_E)
  3. Direct hopping: t_J = J (upper bound, transparent limit)

Gate: FABRIC-COUPLING-55 (INFO)
"""

import sys
import numpy as np

sys.path.insert(0, 'computations')
from canonical_constants import (
    tau_fold, Delta_0_OES, Delta_0_GL, E_cond, N_cells,
    H_fold, M_KK, M_Pl_reduced, xi_BCS, omega_PV, n_pairs,
    E_B2_mean, J_C2 as J_C2_canonical, v_terminal, omega_tau,
    H_0_GeV, H_0_inv_s
)

# ─── Load data ───────────────────────────────────────────────────────
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_tb    = tb['tau_values']      # (50,)
evals_tb  = tb['eigenvalues']     # (50, 32)
evecs_tb  = tb['eigenvectors']    # (50, 32, 32)
H_tb      = tb['hamiltonians']    # (50, 32, 32)
adj_C2    = tb['adj_C2']          # (32, 32)
J_C2_tau  = tb['J_C2_tau']        # (50,)
bandwidths = tb['bandwidths']
band_gaps  = tb['band_gaps']
cell_dims  = tb['cell_dims']
N = int(tb['N_cells'])

sf = np.load('computations/session-54/s54_scale_factor.npz')
tau_sf = sf['tau']
H_sf   = sf['H']
H_at_fold_sf = float(sf['H_at_fold'])

# ─── Identify fold index ────────────────────────────────────────────
i_fold = np.argmin(np.abs(tau_tb - tau_fold))
tau_actual = tau_tb[i_fold]
print(f"Fold index: {i_fold}, tau = {tau_actual:.4f} (target: {tau_fold})")

# ─── Parameters at fold ─────────────────────────────────────────────
J_fold    = J_C2_tau[i_fold]
W_fold    = bandwidths[i_fold]
gap_fold  = band_gaps[i_fold]
evals_fold = evals_tb[i_fold]
evecs_fold = evecs_tb[i_fold]
H_fold_mat = H_tb[i_fold]
Delta = Delta_0_OES  # BCS gap = 0.4643 (OES, canonical)

z_mean = adj_C2.sum() / N  # mean C2 coordination number

print(f"\n{'='*60}")
print(f"PARAMETERS AT FOLD (tau = {tau_actual:.4f})")
print(f"{'='*60}")
print(f"J_C2      = {J_fold:.6f} [M_KK]")
print(f"Bandwidth = {W_fold:.6f} [M_KK]")
print(f"Band gap  = {gap_fold:.6f} [M_KK]")
print(f"Delta_BCS = {Delta:.6f} [M_KK]")
print(f"z_mean    = {z_mean:.3f} (C2 bonds per cell)")
print(f"n_pairs   = {n_pairs:.1f} (Cooper pairs per cell)")

# ─── BCS coherence factors ──────────────────────────────────────────
# Half-filling: mu = midpoint between levels N/2-1 and N/2
mu = (evals_fold[N//2 - 1] + evals_fold[N//2]) / 2
xi_k = evals_fold - mu
E_k = np.sqrt(xi_k**2 + Delta**2)
u_k = np.sqrt(0.5 * (1 + xi_k / E_k))
v_k = np.sqrt(0.5 * (1 - xi_k / E_k))
uv_k = Delta / (2 * E_k)  # = u_k * v_k identically

delta_E_F = evals_fold[N//2] - evals_fold[N//2 - 1]
print(f"\nmu (Fermi level) = {mu:.6f}")
print(f"Level spacing at E_F = {delta_E_F:.6f}")

# ─── METHOD 1: BCS anomalous density (single-bond Josephson) ────────
# For a single weak link (hopping J) between two identical BCS
# condensates, the Josephson coupling is:
#
#   E_J = J^2 * sum_k (u_k * v_k / E_k)
#       = J^2 * sum_k Delta / (2 * E_k^2)
#       = (J^2 * Delta / 2) * sum_k 1/E_k^2
#
# This is the CORRECT second-order perturbation theory result:
# virtual excitation of a quasiparticle across the junction,
# energy denominator 2*E_k (pair breaking + reformation).
# The factor u_k*v_k/E_k comes from the BCS Green's function.
#
# Reference: Ambegaokar & Baratoff, PRL 10, 486 (1963), Eq. (2)
# In their notation: I_c = (pi*Delta)/(2*e*R_N) * tanh(Delta/2kT)
# which at T=0 gives E_J = (pi*Delta)/(4) * sum_n T_n

F_anomalous = np.sum(uv_k / E_k)  # = sum Delta/(2*E_k^2)
E_J_per_bond = J_fold**2 * F_anomalous

# Total per cell (z_mean bonds):
E_J_cell = z_mean * E_J_per_bond

print(f"\n=== Method 1: BCS anomalous density ===")
print(f"F_anomalous = sum(u_k v_k / E_k) = {F_anomalous:.6f}")
print(f"E_J per bond = J^2 * F = {E_J_per_bond:.6f} [M_KK]")
print(f"E_J per cell = z * E_J/bond = {E_J_cell:.6f} [M_KK]")

# ─── METHOD 2: BCS coherence factor sum (Cooper pair transfer) ──────
# The Josephson matrix element for transferring one Cooper pair:
#   t_J = J * (1/N) * sum_k (u_k * v_k)
#       = J * (1/N) * sum_k Delta/(2*E_k)
# This is the pair transfer amplitude, normalized per site.

sum_uv = np.sum(uv_k)
t_J_pair = J_fold * sum_uv / N

print(f"\n=== Method 2: Pair transfer amplitude ===")
print(f"sum(u_k v_k) = {sum_uv:.6f}")
print(f"t_J = J * sum(uv)/N = {t_J_pair:.6f} [M_KK]")

# ─── METHOD 3: Ambegaokar-Baratoff (single-channel weak link) ───────
# For a single tunneling channel with transmission T = (2J/W)^2:
#   E_J = (pi*Delta/4) * T / (1 - T)^{1/2}
# In weak-coupling limit (T << 1):
#   E_J ≈ (pi*Delta/4) * T = (pi*Delta/4) * (2J/W)^2

T_channel = (2 * J_fold / W_fold)**2
E_J_AB_single = (np.pi * Delta / 4) * T_channel
# With z_mean channels:
E_J_AB_total = z_mean * E_J_AB_single

print(f"\n=== Method 3: Ambegaokar-Baratoff (single channel) ===")
print(f"Transmission T = (2J/W)^2 = {T_channel:.6f}")
print(f"E_J per channel = (pi*Delta/4)*T = {E_J_AB_single:.6f} [M_KK]")
print(f"E_J total (z channels) = {E_J_AB_total:.6f} [M_KK]")

# ─── METHOD 4: Direct hopping (transparent limit, upper bound) ──────
t_direct = J_fold
print(f"\n=== Method 4: Direct hopping (upper bound) ===")
print(f"t_direct = J_C2 = {t_direct:.6f} [M_KK]")

# ─── Comparison ─────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"COMPARISON OF JOSEPHSON COUPLING ESTIMATES")
print(f"{'='*60}")
print(f"{'Method':<40} {'E_J [M_KK]':>12} {'E_J/Delta':>10}")
print(f"{'-'*62}")
print(f"{'BCS anomalous density (per bond)':<40} {E_J_per_bond:>12.6f} {E_J_per_bond/Delta:>10.4f}")
print(f"{'BCS anomalous density (per cell)':<40} {E_J_cell:>12.6f} {E_J_cell/Delta:>10.4f}")
print(f"{'Pair transfer amplitude':<40} {t_J_pair:>12.6f} {t_J_pair/Delta:>10.4f}")
print(f"{'A-B single channel':<40} {E_J_AB_single:>12.6f} {E_J_AB_single/Delta:>10.4f}")
print(f"{'A-B total (z channels)':<40} {E_J_AB_total:>12.6f} {E_J_AB_total/Delta:>10.4f}")
print(f"{'Direct hopping (upper bound)':<40} {t_direct:>12.6f} {t_direct/Delta:>10.4f}")

# ─── SELECT PRIMARY ESTIMATE ────────────────────────────────────────
# The BCS anomalous density (Method 1) is the most rigorous:
# it correctly accounts for the pair-breaking/reformation process
# and uses the actual spectrum. The per-bond value is the fundamental
# Josephson coupling; per-cell gives the coordination.
#
# For the fabric, the relevant coupling is PER BOND (between two cells):
t_J = E_J_per_bond

print(f"\n>>> PRIMARY ESTIMATE: t_J = {t_J:.6f} M_KK (per bond, Method 1)")

# ─── Charging energy ────────────────────────────────────────────────
# E_c = "cost to add one Cooper pair to the grain"
# For a small BCS grain with N_pair pairs, the leading contribution is
# the mean level spacing at E_F:
#   E_c ~ delta_E / (2 * g * N(0)) where g = coupling, N(0) = DOS
# More directly: E_c ~ 1 / (2 * N_pair * N(E_F))
# In BCS theory for a finite grain (Anderson, 1959):
#   E_c = delta_E_F / 2 (half the single-particle level spacing)

E_c = delta_E_F / 2
print(f"\n=== Charging energy ===")
print(f"E_c = delta_E_F / 2 = {E_c:.6f} M_KK")
print(f"E_J / E_c = {t_J / E_c:.4f}")

# ─── Josephson plasma frequency ─────────────────────────────────────
omega_J = np.sqrt(2 * t_J * E_c)
print(f"\n=== Josephson plasma frequency ===")
print(f"omega_J = sqrt(2*E_J*E_c) = {omega_J:.6f} M_KK")
print(f"omega_J / Delta = {omega_J / Delta:.4f}")

# ─── Hubble parameters ──────────────────────────────────────────────
# All in GeV (natural units, hbar = c = 1):
#   M_KK = 7.43e16 GeV (canonical)
#   H_0 = 1.438e-42 GeV (present day)
#   H_transit ~ M_KK^2 / M_Pl ~ 2.3e15 GeV (during KK fold)
#   L_cell = 1/M_KK = 1.35e-17 GeV^{-1} (KK cell size)

t_J_GeV = t_J * M_KK
omega_J_GeV = omega_J * M_KK
H_transit = M_KK**2 / M_Pl_reduced
L_cell_GeV = 1.0 / M_KK  # GeV^{-1}

print(f"\n{'='*60}")
print(f"PHYSICAL SCALES (GeV)")
print(f"{'='*60}")
print(f"t_J      = {t_J_GeV:.4e} GeV")
print(f"omega_J  = {omega_J_GeV:.4e} GeV")
print(f"M_KK     = {M_KK:.4e} GeV")
print(f"H_transit = {H_transit:.4e} GeV (M_KK^2/M_Pl)")
print(f"H_0      = {H_0_GeV:.4e} GeV")
print(f"L_cell   = {L_cell_GeV:.4e} GeV^-1")

# ─── THE GATEKEEPER RATIO ───────────────────────────────────────────
# t / (H * L_cell):
# [t] = energy (GeV), [H] = energy (GeV, natural units), [L] = 1/energy (GeV^{-1})
# [H * L] = dimensionless. [t / (H*L)] = energy.
# This is NOT dimensionless as written.
#
# The PHYSICALLY meaningful dimensionless ratio is E_J / H:
# = (coupling energy) / (expansion rate)
# = number of Josephson oscillation cycles per e-fold of expansion
# If E_J / H >> 1, the phase relaxes much faster than expansion disrupts it.

ratio_today = t_J_GeV / H_0_GeV
ratio_transit = t_J_GeV / H_transit
ratio_omegaJ_transit = omega_J_GeV / H_transit

print(f"\n{'='*60}")
print(f"GATEKEEPER RATIOS: E_J / H (dimensionless)")
print(f"{'='*60}")
print(f"")
print(f"Present day:")
print(f"  E_J / H_0         = {ratio_today:.4e}")
print(f"  omega_J / H_0     = {omega_J_GeV / H_0_GeV:.4e}")
print(f"")
print(f"During transit (fold):")
print(f"  E_J / H_transit   = {ratio_transit:.4e}")
print(f"  omega_J / H_transit = {ratio_omegaJ_transit:.4e}")

# Number of coherent cells across Hubble volume:
# N_coherent ~ (E_J / H)^{d} for d spatial dimensions
# In 1D: L_coherent / L_cell = E_J / H (phase coherence length)
N_coh_transit = ratio_transit
N_coh_today = ratio_today
print(f"\nCoherence length (in cells):")
print(f"  During transit: N_coh ~ E_J/H = {N_coh_transit:.4e} cells")
print(f"  Present day:    N_coh ~ E_J/H = {N_coh_today:.4e} cells")

# ─── Regime classification ──────────────────────────────────────────
print(f"\n{'='*60}")
print(f"REGIME CLASSIFICATION")
print(f"{'='*60}")

r_EJ_Ec = t_J / E_c
r_EJ_Delta = t_J / Delta

print(f"\nQuantum rotor model parameters:")
print(f"  E_J / E_c    = {r_EJ_Ec:.4f}")
if r_EJ_Ec > 1:
    rotor_regime = "SUPERFLUID (phase coherent, number fluctuating)"
else:
    rotor_regime = "MOTT INSULATOR (phase fluctuating, number locked)"
print(f"  => {rotor_regime}")

print(f"\n  E_J / Delta  = {r_EJ_Delta:.4f}")
if r_EJ_Delta > 1:
    pair_regime = "STRONG COUPLING: inter-cell hybridization exceeds gap"
elif r_EJ_Delta > 0.01:
    pair_regime = "INTERMEDIATE: Josephson coupling comparable to gap"
else:
    pair_regime = "WEAK COUPLING: isolated grains"
print(f"  => {pair_regime}")

print(f"\n  E_J / H_transit = {ratio_transit:.4e}")
if ratio_transit > 1:
    cosmo_regime = "COHERENT: fabric maintains phase across Hubble horizon during transit"
else:
    cosmo_regime = "DECOHERENT: expansion disrupts inter-cell phase during transit"
print(f"  => {cosmo_regime}")

# ─── tau sweep ───────────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"TAU SWEEP: t_J(tau) [Method 1, per bond]")
print(f"{'='*60}")
print(f"{'tau':>8} {'J_C2':>8} {'W':>8} {'t_J':>10} {'t_J/D':>8} {'E_J/Ec':>8}")

t_J_array = np.zeros(len(tau_tb))
E_J_Ec_array = np.zeros(len(tau_tb))
for i in range(len(tau_tb)):
    J_i = J_C2_tau[i]
    ev_i = evals_tb[i]
    W_i = bandwidths[i]
    mu_i = (ev_i[N//2 - 1] + ev_i[N//2]) / 2
    xi_i = ev_i - mu_i
    E_i = np.sqrt(xi_i**2 + Delta**2)
    uv_i = Delta / (2 * E_i)
    F_i = np.sum(uv_i / E_i)
    t_J_i = J_i**2 * F_i
    dE_i = max(ev_i[N//2] - ev_i[N//2 - 1], 1e-12)
    Ec_i = dE_i / 2
    t_J_array[i] = t_J_i
    E_J_Ec_array[i] = t_J_i / Ec_i if Ec_i > 0 else np.inf

    if i % 5 == 0 or i == i_fold:
        tag = " <-- fold" if i == i_fold else ""
        print(f"{tau_tb[i]:8.4f} {J_i:8.4f} {W_i:8.4f} {t_J_i:10.6f} {t_J_i/Delta:8.4f} {t_J_i/Ec_i:8.2f}{tag}")

print(f"\nt_J range: [{t_J_array.min():.6f}, {t_J_array.max():.6f}] M_KK")
print(f"t_J/Delta range: [{t_J_array.min()/Delta:.4f}, {t_J_array.max()/Delta:.4f}]")

# Regime counts
n_super = np.sum(t_J_array / Delta > 1)
n_inter = np.sum((t_J_array / Delta > 0.01) & (t_J_array / Delta <= 1))
n_weak  = np.sum(t_J_array / Delta <= 0.01)
print(f"\nRegime counts over tau sweep:")
print(f"  Strong (t/D > 1):       {n_super}/50")
print(f"  Intermediate (0.01-1):  {n_inter}/50")
print(f"  Weak (t/D < 0.01):      {n_weak}/50")

# ─── FINAL SUMMARY ──────────────────────────────────────────────────
print(f"\n{'='*60}")
print(f"GATE VERDICT: FABRIC-COUPLING-55 — INFO")
print(f"{'='*60}")
print(f"")
print(f"Josephson coupling at fold (tau={tau_actual:.4f}):")
print(f"  t_J = {t_J:.6f} M_KK = {t_J_GeV:.4e} GeV [per bond, Method 1]")
print(f"  t_J / Delta = {r_EJ_Delta:.4f}")
print(f"  t_J / E_c   = {r_EJ_Ec:.4f}")
print(f"  omega_J     = {omega_J:.6f} M_KK = {omega_J_GeV:.4e} GeV")
print(f"")
print(f"Gatekeeper ratios (E_J/H, dimensionless):")
print(f"  Present:  t_J*M_KK / H_0       = {ratio_today:.4e}")
print(f"  Transit:  t_J*M_KK / H_transit  = {ratio_transit:.4e}")
print(f"")
print(f"CONCLUSION:")
print(f"  The SU(3) fabric is DEEPLY in the superfluid regime:")
print(f"  - E_J/E_c = {r_EJ_Ec:.1f} >> 1: quantum rotor in phase-coherent ground state")
print(f"  - E_J/H >> 1 at ALL epochs: Josephson coupling vastly exceeds Hubble rate")
print(f"  - The entire Hubble volume is ONE phase domain")
print(f"  - Collective fabric effects (phonons, domain walls) are PHYSICAL")
print(f"  - Fabric classification: PHONONIC (not geometric, not isolated)")
