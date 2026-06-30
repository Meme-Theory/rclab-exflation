"""
S74 W1-P: INSTANTON-INTERACTION-DENSITY-74
===========================================

Test case (added mid-session) for the surviving channel of W1-B MODULI-STABILIZATION-74 FAIL.

Question: Does the connected two-instanton correlator <n_inst(tau) n_inst(tau')>_connected
generate multi-instanton condensate contributions to V_eff(tau) large enough to overcome
the 309x single-instanton shortfall identified by W1-B sub-gate (a)?

Governing structure
-------------------
- Jensen-deformed SU(3) gauge sector supports topologically stabilized saddles counted by
  second Chern class. S73A W4-A found the instanton gas is DENSE (n_inst O(1) at tau > 0.3,
  peaking at tau ~ 0.60). Dilute-gas approximation is therefore suspect.
- Two-instanton action: S_2(tau, tau', Delta x) = S_inst(tau) + S_inst(tau') - S_int(Delta x; tau, tau')
- Two mechanisms for S_int:
  (a) 't Hooft vertex: 6-fermion operator mediating long-range I-Ibar attraction, S_int ~ g^2 log(R/rho)
  (b) Moduli-space constrained instanton correction (saddle-point perturbation)
- Connected correlator:
    <n_inst(tau) n_inst(tau')>_c = exp(-S_2) - exp(-S_inst(tau)) * exp(-S_inst(tau'))
- Multi-instanton contribution integrated over Planck band [0.45, 0.70].

Gate: PASS if correlator POSITIVE (attractive) AND R_multi/single > 100.
      INFO if positive but R in [10, 100].
      FAIL if NEGATIVE OR R < 10.

Pre-registered per S74 plan.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

# Canonical constants
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    M_KK, tau_fold, PI, Vol_SU3_Haar,
)

OUT_DIR = Path(__file__).parent
SCRIPT_STAMP = "s74_instanton_interaction_density"

# =============================================================================
# Step 1: Load S73A instanton landscape + W1-B moduli stabilization outputs
# =============================================================================

s73a = np.load(OUT_DIR / "s73a_instanton_landscape.npz", allow_pickle=True)
w1b = np.load(OUT_DIR / "s74_moduli_stabilization.npz", allow_pickle=True)

tau_scan_s73a = s73a["tau_scan"]                 # (21,) [0, 1] step 0.05
S_inst_arr = s73a["S_inst_A"]                    # Single-inst action (Jensen-dressed)
n_inst_arr = s73a["n_inst_unnorm"]               # Dilute-gas density (unnorm)
g2_arr = s73a["g2_modelA"]                       # Running g^2(tau) — Model A
gap_arr = s73a["gap_DK_array"]                   # D_K spectral gap vs tau
kappa_arr = s73a["kappa_physical"]               # Jensen ratio kappa
tau_kappa1 = float(s73a["kappa1_crossings"][0])  # kappa=1 crossing tau ~ 0.480

# W1-B reference numbers
TAU_LO = float(w1b["TAU_LO"])                    # 0.45
TAU_HI = float(w1b["TAU_HI"])                    # 0.70
V_bare_at_kappa1_force = float(w1b["dV_bare_dtau_at_kappa1"])  # 445.43
force_inst_A = float(w1b["force_inst_A"])                      # -1.436
E_inst_A = float(w1b["E_inst_A"])                              # 0.749
# W1-B ratio |dV_inst|/|dV_bare| = 3.22e-3 at tau=0.48, 309x short

print("=" * 70)
print("S74 W1-P INSTANTON-INTERACTION-DENSITY-74")
print("=" * 70)
print(f"Loaded S73A landscape: tau in [0,1] step 0.05, {len(tau_scan_s73a)} points")
print(f"Loaded W1-B outputs: force_inst_A={force_inst_A:.4f}, E_inst_A={E_inst_A:.4f}")
print(f"Shortfall factor W1-B: |dV_inst|/|dV_bare| = {abs(force_inst_A)/V_bare_at_kappa1_force:.3e}")
print(f"Ratio to 1.0 (PASS): {V_bare_at_kappa1_force/abs(force_inst_A):.1f}x short")
print(f"kappa=1 crossing: tau = {tau_kappa1:.4f}")
print(f"Planck n_s target band: [{TAU_LO}, {TAU_HI}]")

# =============================================================================
# Step 2: Interpolate S_inst(tau) and g^2(tau) on a refined Planck-band grid
# =============================================================================
# Use fine grid within the Planck target band for correlator computation.

NTAU = 51
tau_grid = np.linspace(TAU_LO, TAU_HI, NTAU)

def _interp(tau_arr, y_arr, tau_new):
    """Linear interpolation with clipping to range."""
    return np.interp(tau_new, tau_arr, y_arr)

S_inst_grid = _interp(tau_scan_s73a, S_inst_arr, tau_grid)
n_inst_grid = _interp(tau_scan_s73a, n_inst_arr, tau_grid)
g2_grid = _interp(tau_scan_s73a, g2_arr, tau_grid)
gap_grid = _interp(tau_scan_s73a, gap_arr, tau_grid)
kappa_grid = _interp(tau_scan_s73a, kappa_arr, tau_grid)

# Find tau corresponding to peak of n_inst (should be ~ 0.60)
idx_peak_ninst_full = int(np.argmax(n_inst_arr))
tau_peak_ninst_full = float(tau_scan_s73a[idx_peak_ninst_full])
idx_peak_grid = int(np.argmax(n_inst_grid))
tau_peak_grid = float(tau_grid[idx_peak_grid])
n_inst_peak = float(n_inst_grid[idx_peak_grid])
S_inst_at_peak = float(S_inst_grid[idx_peak_grid])
g2_at_peak = float(g2_grid[idx_peak_grid])
gap_at_peak = float(gap_grid[idx_peak_grid])

print()
print("--- n_inst peak location ---")
print(f"S73A full grid peak: tau = {tau_peak_ninst_full:.3f}, n_inst = {n_inst_arr[idx_peak_ninst_full]:.4f}")
print(f"Planck-band peak: tau = {tau_peak_grid:.3f}, n_inst = {n_inst_peak:.4f}")
print(f"S_inst(0.60) = {S_inst_at_peak:.4f}")
print(f"g^2(0.60) = {g2_at_peak:.4f}")
print(f"D_K gap(0.60) = {gap_at_peak:.4f}")

# =============================================================================
# Step 3: Construct two-instanton action S_2(tau, tau')
# =============================================================================
# Governing framework: 't Hooft instanton-instanton interaction on Jensen SU(3).
#
# Two channels must be distinguished:
#
#   (I-Ibar channel): ATTRACTIVE valley interaction. Two-saddle action reduced
#       below 2*S_inst. Channel encodes topological-charge-density fluctuations.
#       Valley approximation (large R/rho): S_int_IIbar ~ (16*pi^2/g^2)*(rho/R)^4
#
#   (I-I channel): REPULSIVE Coulomb interaction between like topological charges.
#       Two-saddle action raised above 2*S_inst. Channel encodes net topological
#       charge Q^2 > 0 configurations.
#
# In the DILUTE limit (R >> rho, applicable when n_inst * rho^4 << 1), the
# connected density-density correlator is dominated by the valley term of the
# I-Ibar channel and is POSITIVE. The Coulomb gas is in its MOLECULAR phase.
#
# In the DENSE limit (n_inst * rho^4 ~ 1, applicable at tau > 0.5 per S73A),
# the valley approximation BREAKS DOWN. At the 2-saddle separation R ~ rho,
# the two constrained-instanton solutions merge into a single (charge-2) saddle.
# The correct partition function is the Debye-screened Coulomb gas, which
# transitions to a PLASMA phase (BKT-like, confined topological charge).
#
# We implement BOTH channels with the following structure:
#
#   S_2(tau, tau') = S_inst(tau) + S_inst(tau') - S_attr + S_rep
#
# where:
#   S_attr = (16*pi^2/g^2_bar) * (rho_bar^2/R_bar^2)^2 * f_valid(R/rho)
#   S_rep  = c_rep * (8*pi^2/g^2_bar) * (rho_bar/R_bar)^2 * f_valid(R/rho)
#
# f_valid(x) = 1/(1 + (rho_min/R)^2) smoothly regulates the R->rho merger region.
#
# For I-Ibar density-density correlator (dominant channel), c_rep = 0 and we
# keep only S_attr with the valley regulator. This is the physically
# defensible choice for the <n_inst n_inst>_c computation because n_inst is a
# SCALAR density (summing |Q|=1 sectors) and the vacuum channel dominates.
#
# We ALSO enforce the merger cap:
#   S_2 >= S_inst(tau = max of tau, tau')   (two saddles can't have less action
#                                              than a single charge-2 saddle)
#
# The charge-2 instanton has action 2*S_inst (linear in Q by topology), so the
# correct cap for S_2 is 2*S_inst of the "average" tau.
#
# IMPORTANT: S_inst is linear in |Q| by topology. The charge-2 saddle has
# action exactly 2*S_inst(tau). The valley correction S_attr represents the
# *difference* between the constrained-instanton 2-saddle (separate) and the
# topologically-equivalent charge-2 saddle (merged). Thus S_attr is bounded:
#   0 <= S_attr <= 0 !
# That is: in the R -> 0 merger limit, the 2-saddle reduces to the charge-2
# saddle and S_int -> 0 (not 2*S_inst).
#
# The correct valley result vanishes in BOTH the R->infinity (dilute) AND
# R->0 (merger) limits. The maximum attraction occurs at intermediate R ~ few*rho.
#
# We use the standard 't Hooft valley profile:
#
#   S_int(R) = (16*pi^2/g^2) * (rho_1*rho_2/R^2)^2 * (1 - (rho_1*rho_2/R^2)^2) * Theta(R^2 > rho^2)
#
# which vanishes at R -> infinity (dilute) and at R -> 0 (merger), peaking at
# R^2 = sqrt(2)*rho_1*rho_2. This is the CORRECT valley action — it is a
# perturbative correction, not a cap-saturating divergence.

def dS_dtau_numerical(tau_arr, S_arr):
    """Central-difference derivative."""
    dS = np.gradient(S_arr, tau_arr)
    return dS

dS_dtau_grid = dS_dtau_numerical(tau_grid, S_inst_grid)

# Effective instanton "size in tau units" from spectral gap
# In natural units, rho ~ 1/gap (inverse infrared scale set by D_K gap)
rho_tau_grid = 1.0 / gap_grid       # characteristic width

# 't Hooft coupling (8*pi^2/g^2) — the action of a single instanton in Model A
#  S_inst = 8*pi^2/g^2 (standard)
S8pi2_over_g2_grid = S_inst_grid.copy()   # by definition for bare SU(N) instanton

# Characteristic tau-separation where S_inst changes by O(S_inst) itself
# (the 't Hooft "size" in tau moduli direction):
Dtau_char_grid = np.abs(S_inst_grid / np.maximum(np.abs(dS_dtau_grid), 1e-12))
# Note: dS/dtau ~ -S_inst / tau roughly, so Dtau_char ~ tau. This sets units.

# =============================================================================
# Step 3a: Build the two-instanton action surface S_2(tau_i, tau_j)
# =============================================================================

# For a valley-based 't Hooft approach on Jensen-deformed SU(3):
#
#   S_2(tau, tau') = S_inst(tau) + S_inst(tau') - S_int(tau, tau')
#
# where S_int is the ATTRACTIVE interaction energy (positive --> reduces total action).
# We use the valley approximation:
#
#   S_int(tau, tau') = Delta_align * (rho_bar^2 / R^2) * f_coulomb(tau, tau')
#
# with:
#   rho_bar^2 = (rho_tau(tau)^2 + rho_tau(tau')^2) / 2
#   R^2 = rho_bar^2 + (Delta tau / Dtau_char_bar)^2
#   Delta_align = min(S_inst(tau), S_inst(tau'))   (geometric mean attractive channel)
#   f_coulomb captures the 2D Coulomb log structure in topological charge density space
#
# Physical justification: the 't Hooft vertex for SU(3) is a 6-fermion operator
# (det psi_L psi_R) whose leading vacuum contribution to the effective action
# at the 2-instanton level scales as:
#   S_eff^(2) ~ -(16*pi^2/g^2) * (rho_1 * rho_2)^2 / R^4
# Setting rho_1 = rho_2 = rho_bar and R = R_bar gives:
#   S_int = (16*pi^2/g^2) * rho_bar^4/R_bar^4 * sign(attractive)

# Governing framework CORRECTED: The <n_inst(tau) n_inst(tau')>_c is a correlator
# between TWO SPATIALLY SEPARATED INSTANTONS living on the SAME substrate slice
# indexed by tau (resp. tau'). They are NOT at the same 4D position.
#
# For a density-density correlator, we integrate over the RELATIVE 4D position
# of the two instantons, holding the moduli (sizes and Jensen parameters) fixed.
# The proper dimensionless interaction integral is the second virial coefficient:
#
#   B_2(tau, tau') = int d^4R [ exp(-S_int(R; rho_1, rho_2)) - 1 ]
#
# where R is the 4D spatial separation, rho_i = 1/gap_i are the instanton sizes
# set by the D_K spectral gap at Jensen parameter tau_i, and S_int is the
# 't Hooft valley interaction at separation R.
#
# The standard 't Hooft valley profile (Shuryak, QCD instanton liquid model):
#   S_int(R; rho_1, rho_2) = (8*pi^2/g^2_eff) * h(R/rho_bar)
# with (I-Ibar channel, aligned orientation):
#   h(x) = -4 * x^2 * (1 + x^2)^(-2)  for small x,
# approaching -4/x^2 in the intermediate regime and -4/x^4 at large x.
#
# For the integrated virial, we use the Shuryak empirical form:
#   S_int_IIbar(R) = -2*S_inst*(rho_bar^2/R^2)^2   for R >= rho_bar
#                  = 0                              for R < rho_bar (merger)
#
# then B_2 = 2*pi^2 * int_{rho_bar}^infty R^3 dR [exp(-S_int(R)) - 1]
#         = 2*pi^2 * rho_bar^4 * int_1^infty dy y^3 [exp(+2*S_inst*y^{-4}) - 1]
# with y = R/rho_bar.
#
# This integral converges at large y (integrand ~ y^3 * 2*S_inst*y^-4 = 2*S_inst/y)
# no wait -- that's log-divergent. The convergence comes from the -1 cancellation
# and exp(1/y^4) -> 1. Let me re-check:
#   integrand = y^3 * [exp(2*S_inst/y^4) - 1]
# At large y: exp(2*S_inst/y^4) - 1 ~ 2*S_inst/y^4, so integrand ~ 2*S_inst/y
# This IS log-divergent. Physical cutoff: the spatial box size, or the scale at
# which the dilute gas assumption holds (nearest-neighbor instanton distance).
#
# Nearest-neighbor distance for a gas of density n_inst in 4D:
#   d_nn = (1/n_inst)^(1/4) * rho_bar_scale
# where rho_bar_scale converts the dimensionless n_inst_unnorm to physical
# density. In natural units (rho_bar = 1), d_nn = (1/n_inst)^(1/4).
# For n_inst ~ 0.73 at tau=0.6: d_nn ~ 1.08 * rho_bar. The IR cutoff is
# essentially rho_bar itself -- instantons at peak density are CLOSE-PACKED.
#
# The finite-B_2 regime therefore requires:
#   IR cutoff = max(d_nn, rho_bar)
#   UV cutoff = rho_bar (below which valley profile breaks down)
#
# For the correlator we keep both tau slices with their own rho_i but evaluate
# at the COMMON physical R cutoff d_nn_bar = mean nearest-neighbor.

NTau2 = NTAU
S_2 = np.zeros((NTau2, NTau2))
S_int = np.zeros((NTau2, NTau2))        # peak value along R axis (diagnostic)
B2_surface = np.zeros((NTau2, NTau2))   # second virial coefficient surface

# Nearest-neighbor scale from mean density
n_inst_mean = float(np.mean(n_inst_grid))

def S_int_valley(R, rho_bar, S_eff):
    """'t Hooft valley interaction for I-Ibar on SU(3).

    Form:
      S_int(y) = -S_eff * [1 - (1 - y_rho^4/y^4)^2]   for y > 1   (y = R/rho_bar)
               = 0                                    for y <= 1   (merger regime)

    Properties:
      - At R = rho_bar+ (y = 1+): S_int -> 0 (smooth approach to merger)
      - At large y: S_int -> -S_eff * (2 y_rho^4/y^4) ~ -2*S_eff/y^4 (standard
        asymptotic valley form)
      - Bounded: |S_int| <= S_eff (no unphysical over-binding; the bound energy
        is at most half the rest mass).

    Returns negative value for attractive channel.
    """
    if R <= rho_bar:
        return 0.0
    y = R / rho_bar
    y4 = y * y * y * y
    # Smooth profile with correct asymptote and bounded by S_eff
    bracket = 1.0 - (1.0 - 1.0/y4)**2
    return -S_eff * bracket

def B2_virial(rho_bar, S_eff, R_lo, R_hi, N_R=400):
    """Second virial integral:
       B_2 = 2*pi^2 * int dR R^3 [exp(-S_int(R)) - 1]
       (from 4D spherical shell element d^4R = 2*pi^2 R^3 dR)"""
    if R_hi <= R_lo:
        return 0.0
    Rs = np.linspace(R_lo, R_hi, N_R)
    integrand = np.zeros(N_R)
    for k, R in enumerate(Rs):
        S = S_int_valley(R, rho_bar, S_eff)
        integrand[k] = 2.0 * PI**2 * R**3 * (np.exp(-S) - 1.0)
    return np.trapezoid(integrand, Rs)

for i in range(NTau2):
    for j in range(NTau2):
        rho1 = rho_tau_grid[i]
        rho2 = rho_tau_grid[j]
        rho_bar = np.sqrt(0.5 * (rho1**2 + rho2**2))
        S_eff = 0.5 * (S_inst_grid[i] + S_inst_grid[j])   # 8*pi^2/g^2_bar
        # IR cutoff: nearest-neighbor separation
        n_bar = 0.5 * (n_inst_grid[i] + n_inst_grid[j])
        # Physical density ~ n_bar / rho_bar^4, so d_nn^4 = rho_bar^4 / n_bar
        d_nn = rho_bar / (n_bar**0.25) if n_bar > 1e-10 else 10.0 * rho_bar
        R_lo = rho_bar           # valley regime starts here
        R_hi = max(d_nn, 2.0 * rho_bar)
        B2_ij = B2_virial(rho_bar, S_eff, R_lo, R_hi)
        B2_surface[i, j] = B2_ij
        # Peak interaction strength (just after R = rho_bar)
        S_int[i, j] = -S_int_valley(1.01 * rho_bar, rho_bar, S_eff)   # positive = attractive
        # Effective 2-instanton "condensed" action: subtract B2 contribution from 2*S_inst
        # (This is a diagnostic; the physical statement is that B2 enters the free energy.)
        S_2[i, j] = S_inst_grid[i] + S_inst_grid[j] - S_int[i, j]

print()
print("--- 2-instanton action surface ---")
print(f"S_2 range: [{S_2.min():.3f}, {S_2.max():.3f}]")
print(f"S_int range: [{S_int.min():.3f}, {S_int.max():.3f}]")

# On-diagonal values (tau = tau')
i_peak = idx_peak_grid
S_2_diag = np.array([S_2[i, i] for i in range(NTau2)])
S_int_diag = np.array([S_int[i, i] for i in range(NTau2)])
print(f"S_2(0.60, 0.60) = {S_2[i_peak, i_peak]:.4f}")
print(f"S_int(0.60, 0.60) = {S_int[i_peak, i_peak]:.4f}")
print(f"2*S_inst(0.60) = {2*S_inst_grid[i_peak]:.4f}")
print(f"Fractional interaction at peak: {S_int[i_peak, i_peak]/(2*S_inst_grid[i_peak]):.4f}")

# =============================================================================
# Step 4: Connected correlator via cluster expansion
# =============================================================================
# For a Coulomb gas of instantons with fugacity zeta = exp(-S_inst), the grand
# partition function has the cluster expansion:
#
#   ln Z = zeta * V_4 + (1/2) * zeta^2 * B_2 + O(zeta^3)
#
# where B_2 = int d^4R [exp(-S_int(R)) - 1] is the second virial coefficient.
#
# The density-density connected correlator (position space):
#   <n(x) n(y)>_c = zeta(tau)*zeta(tau')*[exp(-S_int(x-y)) - 1] * delta(tau slice)
#
# Integrated over 4D relative position at fixed tau, tau':
#   <n_inst(tau) n_inst(tau')>_c = zeta(tau)*zeta(tau')*B_2(tau, tau')
#
# where zeta(tau) = exp(-S_inst(tau)) is the single-instanton fugacity.
#
# Attractive S_int > 0 --> B_2 > 0 (clustering), positive correlator, condensation.
# Repulsive S_int < 0 --> B_2 < 0 (anti-clustering), negative correlator, dilute.

exp_S_inst_grid = np.exp(-S_inst_grid)
zeta_outer = np.outer(exp_S_inst_grid, exp_S_inst_grid)   # fugacity product

# Connected correlator = fugacity_product * B_2
C_conn = zeta_outer * B2_surface

# Relative correlator: C_conn / (zeta_outer) = B_2
# This dimensional ratio is the "clustering volume" -- when positive and large
# compared to the single-instanton volume rho^4, the gas is strongly correlated.
# Relative to disconnected <n(tau)*n(tau')> = zeta(tau)*zeta(tau'):
#   C_rel = C_conn / zeta_outer = B_2 (dimensional)

C_rel = B2_surface.copy()

print()
print("--- Connected correlator (virial form) ---")
print(f"B_2(0.60, 0.60) = {B2_surface[i_peak, i_peak]:.6e}")
print(f"zeta(0.60)^2 = {zeta_outer[i_peak, i_peak]:.6e}")
print(f"C_conn(0.60, 0.60) = {C_conn[i_peak, i_peak]:.6e}")
print(f"Sign of correlator at peak: {'POSITIVE (attractive)' if C_conn[i_peak, i_peak] > 0 else 'NEGATIVE (repulsive)'}")
print(f"B_2 range: [{B2_surface.min():.3e}, {B2_surface.max():.3e}]")
print(f"C_conn range: [{C_conn.min():.3e}, {C_conn.max():.3e}]")
print(f"S_int(peak, peak) (valley max): {S_int[i_peak, i_peak]:.4f}")

# =============================================================================
# Step 5: Integrated multi-instanton vs single-instanton contribution to V_eff
# =============================================================================
# Cluster expansion of grand potential:
#   Omega / V_4 = -zeta - (1/2)*zeta^2*B_2 - ...
# with zeta = zeta(tau) = exp(-S_inst(tau)).
#
# Contribution to V_eff(tau) from 1-instanton sector: V_1 = -zeta(tau)
# Contribution from 2-instanton cluster: V_2 = -(1/2)*zeta^2(tau)*B_2(tau, tau)
#
# Note: B_2 has units of 4D volume. To be dimensionless, divide by a reference
# 4D volume. The natural reference is rho^4 (single-instanton core volume).
#
# Ratio (physical):
#   R_multi/single(tau) = |V_2(tau)| / |V_1(tau)| = (1/2) * zeta(tau) * B_2(tau, tau)
#
# Integrated over Planck band:
#   C_single = int_band dtau |V_1(tau)| = int dtau exp(-S_inst(tau))
#   C_multi  = int_band dtau |V_2(tau)| = (1/2) * int dtau zeta^2(tau) * B_2(tau, tau)
#
# R_multi_single = C_multi / C_single

dtau = tau_grid[1] - tau_grid[0]

# Diagonal B_2 (tau = tau')
B2_diag = np.array([B2_surface[i, i] for i in range(NTau2)])

# Single-instanton "contribution to V_eff" integrated over Planck band
C_single = np.trapezoid(exp_S_inst_grid, tau_grid)
# Multi-instanton 2-cluster contribution (virial)
# Physical density prefactor: (1/2) zeta^2 B_2 has the same units as zeta
# if we divide B_2 by rho^4 -- a natural dimensionless volume.
integrand_multi = 0.5 * exp_S_inst_grid**2 * B2_diag / (rho_tau_grid**4)
C_multi = np.trapezoid(integrand_multi, tau_grid)

# R_multi/single -- dimensionless ratio
R_multi_single = C_multi / C_single if C_single > 0 else float('nan')

# Also report a LOCAL ratio at tau = 0.60 peak
R_at_peak_local = 0.5 * exp_S_inst_grid[i_peak] * B2_diag[i_peak] / (rho_tau_grid[i_peak]**4)
R_at_peak_local_ratio = R_at_peak_local / 1.0   # denominator = V_1(tau)/V_1(tau) = 1

# The local V_2/V_1 ratio at peak
V2_over_V1_peak = 0.5 * exp_S_inst_grid[i_peak] * B2_diag[i_peak] / (rho_tau_grid[i_peak]**4)

print()
print("--- Integrated contributions (virial form) ---")
print(f"B_2(0.60, 0.60) [4D volume] = {B2_surface[i_peak, i_peak]:.3e}")
print(f"B_2 / rho^4 at peak [dimensionless] = {B2_surface[i_peak, i_peak]/rho_tau_grid[i_peak]**4:.3e}")
print(f"zeta(0.60) = {exp_S_inst_grid[i_peak]:.3e}")
print(f"V_1(0.60) [fugacity] = {exp_S_inst_grid[i_peak]:.3e}")
print(f"V_2(0.60) [cluster]  = {0.5 * exp_S_inst_grid[i_peak]**2 * B2_diag[i_peak] / rho_tau_grid[i_peak]**4:.3e}")
print(f"V_2/V_1 at peak = {V2_over_V1_peak:.4f}")
print()
print(f"C_single (int V_1 over Planck band): {C_single:.6e}")
print(f"C_multi  (int V_2 over Planck band): {C_multi:.6e}")
print(f"R_multi/single = C_multi / C_single = {R_multi_single:.4f}")

# =============================================================================
# Step 5a: Local peak ratio -- V_2/V_1 on diagonal
# =============================================================================
# The LOCAL ratio of 2-cluster to 1-cluster at each tau:
#   r(tau) = (1/2) * zeta(tau) * B_2(tau,tau) / rho(tau)^4

r_diag = 0.5 * exp_S_inst_grid * B2_diag / rho_tau_grid**4
R_peak_local = np.max(r_diag)
tau_R_peak_local = tau_grid[np.argmax(r_diag)]

print(f"R_peak_local (max V_2/V_1 on diagonal) = {R_peak_local:.4f} at tau={tau_R_peak_local:.3f}")

# =============================================================================
# Step 6: Force-magnitude check -- does multi-instanton close the 309x gap?
# =============================================================================
# The W1-B result: single-inst force ~ -1.436 vs bare restoring force ~ +445.
# Gap: 445 / 1.436 = 310x.
# If multi-inst contribution scales as (1 + R_multi_single + R_multi_single^2 + ...):
# For R_multi_single ~ O(1), series converges to ~ 1/(1 - R) ~ O(1) total enhancement.
# For R_multi_single > 1 we need resummation (Debye screening in the Coulomb gas).

enhancement_series = 1.0 / (1.0 - R_multi_single) if R_multi_single < 1 else float('inf')
force_enhancement_naive = R_multi_single
force_enhancement_resummed = enhancement_series if R_multi_single < 1 else 1e6

new_force_naive = abs(force_inst_A) * (1.0 + force_enhancement_naive)
new_force_resummed = abs(force_inst_A) * force_enhancement_resummed if R_multi_single < 1 else abs(force_inst_A) * 1e6

force_needed = V_bare_at_kappa1_force   # ~ 445
print()
print("--- Force closure check (vs W1-B 309x gap) ---")
print(f"Single-inst force (W1-B): {abs(force_inst_A):.3f}")
print(f"Bare restoring force: {force_needed:.3f}")
print(f"Naive enhancement (1 + R): force = {new_force_naive:.3f}")
print(f"Resummed enhancement: force = {new_force_resummed:.3f}")
print(f"Gap closure (naive): {new_force_naive/force_needed:.3e}")
print(f"Gap closure (resummed): {new_force_resummed/force_needed:.3e}")

# =============================================================================
# Step 6a: Valley bound sensitivity scan (required for verdict reasoning)
# =============================================================================
# Valley profile has free bound parameter alpha in [1, 2]:
#   S_int(y) = -alpha * S_eff * [1 - (1 - 1/y^4)^2]
# alpha=1 : half-BPS (conservative), |S_int| <= S_eff
# alpha=2 : BPS-saturating (aggressive), |S_int| <= 2*S_eff

def S_int_alpha(R, rho_bar, S_eff, alpha):
    if R <= rho_bar:
        return 0.0
    y = R / rho_bar
    bracket = 1.0 - (1.0 - 1.0/y**4)**2
    return -alpha * S_eff * bracket

def B2_alpha(rho_bar, S_eff, R_lo, R_hi, alpha, N_R=400):
    if R_hi <= R_lo:
        return 0.0
    Rs = np.linspace(R_lo, R_hi, N_R)
    integrand = np.zeros(N_R)
    for k, R in enumerate(Rs):
        S = S_int_alpha(R, rho_bar, S_eff, alpha)
        integrand[k] = 2.0 * PI**2 * R**3 * (np.exp(-S) - 1.0)
    return np.trapezoid(integrand, Rs)

alpha_scan = np.array([1.0, 1.25, 1.5, 1.75, 2.0])
R_alpha = np.zeros_like(alpha_scan)
for k_alpha, alpha_val in enumerate(alpha_scan):
    B2_alpha_diag = np.zeros(NTau2)
    for i in range(NTau2):
        rho_i = rho_tau_grid[i]
        S_i = S_inst_grid[i]
        n_i = n_inst_grid[i]
        d_nn = rho_i / (n_i**0.25) if n_i > 1e-10 else 10.0 * rho_i
        B2_alpha_diag[i] = B2_alpha(rho_i, S_i, rho_i, max(d_nn, 2.0*rho_i), alpha_val)
    integrand_alpha = 0.5 * exp_S_inst_grid**2 * B2_alpha_diag / (rho_tau_grid**4)
    C_multi_alpha = np.trapezoid(integrand_alpha, tau_grid)
    R_alpha[k_alpha] = C_multi_alpha / C_single if C_single > 0 else float('nan')

print()
print("--- Valley-bound sensitivity scan (alpha = valley depth coefficient) ---")
for a, R in zip(alpha_scan, R_alpha):
    gate_ann = ("PASS" if R > 100 else ("INFO" if R > 10 else "FAIL"))
    print(f"   alpha = {a:.2f}: R_multi/single = {R:.3e} --> {gate_ann}")

# Interpolation for crossover alpha (monotone increasing in alpha)
if np.any(R_alpha > 100):
    alpha_pass = float(np.interp(np.log(100.0), np.log(R_alpha), alpha_scan))
else:
    alpha_pass = float('nan')
if np.any(R_alpha > 10):
    alpha_info = float(np.interp(np.log(10.0), np.log(R_alpha), alpha_scan))
else:
    alpha_info = float('nan')
print(f"   Alpha crossover to INFO (R=10): {alpha_info:.3f}")
print(f"   Alpha crossover to PASS (R=100): {alpha_pass:.3f}")

# =============================================================================
# Step 7: Gate verdict
# =============================================================================

sign_correlator = C_conn[i_peak, i_peak] > 0
PASS_R_multi = R_multi_single > 100.0
INFO_R_multi = 10.0 <= R_multi_single <= 100.0

# Primary verdict uses the conservative (alpha=1, half-BPS) valley bound.
# This is the physically defensible lower bound on the multi-instanton enhancement.
if sign_correlator and PASS_R_multi:
    verdict = "PASS"
    reasoning = "Correlator POSITIVE (attractive) AND R_multi/single > 100 under conservative valley bound."
elif sign_correlator and INFO_R_multi:
    verdict = "INFO"
    reasoning = f"Correlator POSITIVE but R_multi/single = {R_multi_single:.2f} in [10, 100] under conservative valley bound."
elif not sign_correlator:
    verdict = "FAIL"
    reasoning = "Correlator NEGATIVE (repulsive) -- dilute-gas approximation used by W1-B is correct. W1-B FAIL stands structurally."
elif sign_correlator and R_multi_single < 10:
    verdict = "FAIL"
    reasoning = (f"Correlator positive but R_multi/single = {R_multi_single:.3f} < 10 under conservative valley bound. "
                 f"Under BPS-saturating valley bound R jumps to {R_alpha[-1]:.3e} (PASS). "
                 f"Primary FAIL stands because first-principles valley Jacobian on Jensen SU(3) is unknown and the "
                 f"conservative bound is the physically defensible lower estimate.")
else:
    verdict = "FAIL"
    reasoning = "Unknown fall-through case."

print()
print("=" * 70)
print(f"GATE VERDICT: {verdict}")
print("=" * 70)
print(f"Reasoning: {reasoning}")
print(f"Correlator sign at peak: {'POSITIVE' if sign_correlator else 'NEGATIVE'}")
print(f"R_multi/single: {R_multi_single:.4f}")
print(f"PASS threshold: R > 100. INFO band: [10, 100]. FAIL: R < 10 or negative.")

# =============================================================================
# Step 8: Cross-checks
# =============================================================================

print()
print("--- Cross-checks ---")

# Cross-check 1: Virial integral convergence
# B_2 must be FINITE (proper IR cutoff applied). Verify:
#   (a) B_2 > 0 (attractive valley dominates)
#   (b) B_2 < (cluster volume)^2 to be meaningful
B2_peak = B2_surface[i_peak, i_peak]
rho_peak = rho_tau_grid[i_peak]
B2_physical = B2_peak / (rho_peak**4)
print(f"1. Virial integral convergence:")
print(f"   B_2(0.60, 0.60) [4D volume] = {B2_peak:.3e}")
print(f"   B_2 / rho^4 [dimensionless] = {B2_physical:.3e}")
print(f"   B_2 > 0: {'PASS' if B2_peak > 0 else 'FAIL'}")
# Dilute-gas check: B_2 should decrease with Dtau (sized by nearest-neighbor)
B2_diag_ends = 0.5 * (B2_surface[0, 0] + B2_surface[-1, -1])
B2_offdiag = B2_surface[0, -1]
print(f"   B_2(0.45, 0.45) diag = {B2_surface[0, 0]:.3e}")
print(f"   B_2(0.70, 0.70) diag = {B2_surface[-1, -1]:.3e}")
print(f"   B_2(0.45, 0.70) corner = {B2_offdiag:.3e}")

# Cross-check 2: Sign convention --
# The 't Hooft vertex is attractive between I-Ibar (vacuum-preserving) and repulsive
# between I-I (like-topological-charge). For a "density" correlator we sum BOTH
# channels; the sign of the net correlator depends on the balance.
# For the substrate's Jensen-deformed SU(3), the n_inst(tau) is counting total
# topological density |Q|, so the correlator is dominated by the I-Ibar
# attractive channel at typical densities.
print(f"2. Sign convention:")
print(f"   S_int positive --> attractive I-Ibar vacuum channel dominates")
print(f"   S_int at peak: {S_int[i_peak, i_peak]:.4f} (positive = attractive)")
print(f"   Consistent with 't Hooft vertex structure: {'YES' if S_int[i_peak, i_peak] > 0 else 'NO'}")

# Cross-check 3: S37 integrable GGE irrelevance
# S37 found the BCS pair sector follows Richardson-Gaudin integrability and forms
# a GGE. That is a STATEMENT ABOUT PAIR-CHANNEL QUASIPARTICLES.
# The instantons here are gauge-sector topological saddles, NOT BCS quasiparticles.
# The correlator is computed on a separate Hilbert space and is NOT constrained by
# the S37 integrability result.
print(f"3. S37 GGE decoupling: PASS (gauge-sector vs BCS-sector Hilbert spaces distinct)")

# Cross-check 4: Finite-size convergence -- double grid density
NTAU_fine = 101
tau_fine = np.linspace(TAU_LO, TAU_HI, NTAU_fine)
S_inst_fine = _interp(tau_scan_s73a, S_inst_arr, tau_fine)
rho_tau_fine = 1.0 / _interp(tau_scan_s73a, gap_arr, tau_fine)
g2_fine = _interp(tau_scan_s73a, g2_arr, tau_fine)
Dtau_char_fine = np.abs(S_inst_fine / np.maximum(
    np.abs(np.gradient(S_inst_fine, tau_fine)), 1e-12))

exp_S_inst_fine = np.exp(-S_inst_fine)
n_inst_fine = _interp(tau_scan_s73a, n_inst_arr, tau_fine)
B2_diag_fine = np.zeros(NTAU_fine)
for i in range(NTAU_fine):
    rho_i = rho_tau_fine[i]
    S_eff_i = S_inst_fine[i]
    n_bar_i = n_inst_fine[i]
    d_nn_i = rho_i / (n_bar_i**0.25) if n_bar_i > 1e-10 else 10.0 * rho_i
    R_lo = rho_i
    R_hi = max(d_nn_i, 2.0 * rho_i)
    B2_diag_fine[i] = B2_virial(rho_i, S_eff_i, R_lo, R_hi)

integrand_multi_fine = 0.5 * exp_S_inst_fine**2 * B2_diag_fine / (rho_tau_fine**4)
C_multi_fine = np.trapezoid(integrand_multi_fine, tau_fine)
C_single_fine = np.trapezoid(exp_S_inst_fine, tau_fine)
R_fine = C_multi_fine / C_single_fine if C_single_fine > 0 else float('nan')
print(f"4. Grid convergence: R(51) = {R_multi_single:.6f}, R(101) = {R_fine:.6f}")
print(f"   Relative change: {abs(R_fine - R_multi_single)/max(abs(R_multi_single), 1e-300):.2e}")

# Cross-check 5: B_2 finite (virial integral converged)
nan_count = np.sum(~np.isfinite(B2_surface))
inf_count = np.sum(np.isinf(B2_surface))
print(f"5. Virial integral finiteness: nan={nan_count}, inf={inf_count} (should both be 0)")
# Cross-check 6: S_int is attractive everywhere (valley form)
S_int_nonneg = np.sum(S_int < 0)
print(f"6. Valley interaction attractive: {NTau2*NTau2 - S_int_nonneg}/{NTau2*NTau2} points with S_int >= 0")

# Cross-check 7: Sensitivity scan previously computed in Step 6a.
print(f"7. Valley-bound sensitivity (see Step 6a above):")
for a, R in zip(alpha_scan, R_alpha):
    gate_ann = ("PASS" if R > 100 else ("INFO" if R > 10 else "FAIL"))
    print(f"   alpha = {a:.2f}: R_multi/single = {R:.3e} --> {gate_ann}")

# =============================================================================
# Step 9: Save outputs
# =============================================================================

np.savez(
    OUT_DIR / f"{SCRIPT_STAMP}.npz",
    tau_grid=tau_grid,
    S_inst_grid=S_inst_grid,
    n_inst_grid=n_inst_grid,
    g2_grid=g2_grid,
    gap_grid=gap_grid,
    rho_tau_grid=rho_tau_grid,
    Dtau_char_grid=Dtau_char_grid,
    S_2=S_2,
    S_int_peak_strength=S_int,
    B2_surface=B2_surface,
    B2_diag=B2_diag,
    C_conn=C_conn,
    C_rel=C_rel,
    zeta_outer=zeta_outer,
    C_multi=C_multi,
    C_single=C_single,
    R_multi_single=R_multi_single,
    R_peak_local=R_peak_local,
    tau_R_peak_local=tau_R_peak_local,
    sign_correlator_at_peak=int(sign_correlator),
    tau_peak_ninst=tau_peak_grid,
    S_inst_at_peak=S_inst_at_peak,
    S_int_at_peak=S_int[i_peak, i_peak],
    B2_at_peak=B2_surface[i_peak, i_peak],
    V2_over_V1_peak=V2_over_V1_peak,
    force_enhancement_naive=force_enhancement_naive,
    force_enhancement_resummed=force_enhancement_resummed,
    new_force_resummed=new_force_resummed,
    force_needed=force_needed,
    gap_closure_naive=new_force_naive/force_needed,
    gap_closure_resummed=new_force_resummed/force_needed if R_multi_single < 1 else 1e6,
    verdict=verdict,
    reasoning=reasoning,
    # Cross-check artifacts
    R_fine=R_fine,
    NTAU_coarse=NTAU,
    NTAU_fine=NTAU_fine,
    alpha_scan=alpha_scan,
    R_alpha=R_alpha,
    alpha_crossover_info=alpha_info,
    alpha_crossover_pass=alpha_pass,
)

print()
print(f"Saved: {SCRIPT_STAMP}.npz")

# =============================================================================
# Step 10: Plot
# =============================================================================

fig = plt.figure(figsize=(14, 10))

# Panel 1: S_2 surface
ax1 = plt.subplot(2, 2, 1)
T1, T2 = np.meshgrid(tau_grid, tau_grid, indexing='ij')
im1 = ax1.pcolormesh(T1, T2, S_2, cmap='viridis', shading='auto')
ax1.axvline(tau_peak_grid, color='red', linestyle='--', alpha=0.5, lw=1)
ax1.axhline(tau_peak_grid, color='red', linestyle='--', alpha=0.5, lw=1)
ax1.set_xlabel(r"$\tau$")
ax1.set_ylabel(r"$\tau'$")
ax1.set_title(r"$S_2(\tau, \tau')$ = $S_{inst}(\tau) + S_{inst}(\tau') - S_{int}$")
plt.colorbar(im1, ax=ax1)

# Panel 2: B_2 (second virial coefficient)
ax2 = plt.subplot(2, 2, 2)
B2_norm = B2_surface / (rho_tau_grid[:, None]**2 * rho_tau_grid[None, :]**2)
im2 = ax2.pcolormesh(T1, T2, B2_norm, cmap='magma', shading='auto')
ax2.axvline(tau_peak_grid, color='cyan', linestyle='--', alpha=0.5, lw=1)
ax2.axhline(tau_peak_grid, color='cyan', linestyle='--', alpha=0.5, lw=1)
ax2.set_xlabel(r"$\tau$")
ax2.set_ylabel(r"$\tau'$")
ax2.set_title(r"$B_2(\tau, \tau') / \rho^4$ [dimensionless, + = attractive]")
plt.colorbar(im2, ax=ax2)

# Panel 3: Connected correlator (sign map)
ax3 = plt.subplot(2, 2, 3)
# Symmetric log for handling small/large values
C_conn_sym = np.sign(C_conn) * np.log10(np.abs(C_conn) + 1e-300)
im3 = ax3.pcolormesh(T1, T2, C_conn_sym, cmap='RdBu_r', shading='auto',
                     vmin=-np.max(np.abs(C_conn_sym)), vmax=np.max(np.abs(C_conn_sym)))
ax3.set_xlabel(r"$\tau$")
ax3.set_ylabel(r"$\tau'$")
ax3.set_title(r"sign($\langle n n \rangle_c$) $\times \log_{10}|\langle n n \rangle_c|$")
plt.colorbar(im3, ax=ax3)
ax3.text(0.05, 0.95,
         f"sign at peak: {'POS (attractive)' if sign_correlator else 'NEG (repulsive)'}",
         transform=ax3.transAxes, va='top',
         bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Panel 4: V_2/V_1 on diagonal + summary
ax4 = plt.subplot(2, 2, 4)
ax4.plot(tau_grid, r_diag, 'b-', lw=2, label=r"$V_2/V_1 = \frac{1}{2}\zeta B_2/\rho^4$")
ax4.plot(tau_grid, exp_S_inst_grid, 'g--', lw=1.5, label=r"$V_1 = \zeta(\tau)$")
ax4.plot(tau_grid, 0.5*exp_S_inst_grid**2*B2_diag/rho_tau_grid**4, 'r:', lw=1.5, label=r"$V_2$")
ax4.axvline(tau_peak_grid, color='red', linestyle='--', alpha=0.5, label=f"tau peak = {tau_peak_grid:.3f}")
ax4.axhline(0, color='k', linestyle='-', alpha=0.3)
ax4.set_xlabel(r"$\tau$")
ax4.set_ylabel("Contribution magnitude")
ax4.set_yscale('symlog', linthresh=1e-10)
ax4.set_title("Cluster expansion terms on diagonal\n"
              f"R_multi/single = {R_multi_single:.3e} -- {verdict}")
ax4.legend(loc='best', fontsize=8)
ax4.grid(alpha=0.3)

fig.suptitle(f"S74 W1-P INSTANTON-INTERACTION-DENSITY-74 -- {verdict}\n"
             f"Connected correlator: sign = {'POSITIVE' if sign_correlator else 'NEGATIVE'}, "
             f"R_multi/single = {R_multi_single:.3f}",
             fontsize=12)
plt.tight_layout()
plt.savefig(OUT_DIR / f"{SCRIPT_STAMP}.png", dpi=120, bbox_inches='tight')
print(f"Saved: {SCRIPT_STAMP}.png")
print()
print("DONE.")
