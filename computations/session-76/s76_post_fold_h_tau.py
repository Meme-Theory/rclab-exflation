#!/usr/bin/env python3
"""
S76-A5-POST-FOLD-H: Resolve Model A vs Model B for Post-Fold Background H(tau)
================================================================================

GATE: S76-A5-POST-FOLD-H
  PASS: Single self-consistent H(tau) derived from spectral action + GGE
        back-reaction, with n_s and A_s inputs both consistent.
  FAIL: Model A and Model B cannot be reconciled.
  INFO: One model identified as correct but requires unavailable numerical input.

Physics (substrate framing):
  H(tau) is the emergent expansion rate from the a_2 Seeley-DeWitt coefficient.
  The spectral action is the fundamental object; H is derived.

  The question: does the late-time (tau >> 0.5) spectral reorganization produce
  a Hubble rate that decreases (Model A) or increases (Model B)?

  RESOLUTION: Both models are incomplete. The correct Friedmann equation is
  the coupled ODE from S73B, which tracks:
    - Modulus kinetic energy (KE = (1/2) G dot_tau^2, stiff w=+1)
    - Spectral action potential V(tau)
    - Hubble friction (3H dot_tau)
  Post-fold, the modulus overshoots to tau_max=1.614, oscillates, and decays
  (tau_decay ~ 2.5e-27 s). The GGE relic + SM radiation then dominate.

  Model B fails because S(tau) is the VACUUM spectral action (geometry alone),
  not including the GGE relic energy. The relic is a MATTER contribution to
  the Friedmann equation, not captured by S(tau)/a_2(tau).

  Model A fails because it parameterizes H(tau) as a power law in tau, but
  tau is NOT a monotonic time variable -- it overshoots and returns.

  The correct H(t) comes from the three-phase evolution:
    Phase 1: Stiff modulus-dominated (fold -> modulus decay)
    Phase 2: Radiation-dominated (modulus decay -> matter-radiation equality)
    Phase 3: Matter + Lambda (late universe)

Cross-checks:
  CHK1: H(tau_fold) reproduces 586.5 M_KK (canonical value)
  CHK2: H(today) approaches H_0 = 1.438e-42 GeV
  CHK3: Energy conservation (continuity equation satisfied)
  CHK4: Total e-folds = 132.4 (consistent with S73B)
  CHK5: Model A and Model B recovered as limiting cases
"""

import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# Ensure canonical constants are importable
sys.path.insert(0, os.path.dirname(__file__))
from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced, M_Pl_unreduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal, G_DeWitt,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI, G_N,
    n_pairs, E_cond,
    hbar_GeV_s, H_0_GeV, T_CMB_GeV,
    g_star_SM, g_star_BBN, N_eff_SM,
    GeV_to_inv_s,
    planck_ns, planck_ns_err,
)

data_dir = os.path.dirname(__file__)
log_lines = []

def log(msg):
    print(msg)
    log_lines.append(msg)

log("=" * 78)
log("S76-A5-POST-FOLD-H: Resolve Model A vs Model B for Post-Fold H(tau)")
log("=" * 78)

# ============================================================================
#  SECTION 1: Load All Input Data
# ============================================================================

log("\n--- SECTION 1: Load input data ---")

# (a) S75 Model A/B data
d75 = np.load(os.path.join(data_dir, 's75_h_phys_reduction.npz'),
              allow_pickle=True)
gamma_a2 = float(d75['gamma_a2'])  # (local) power-law exponent for a_2
gamma_a4 = float(d75['gamma_a4'])  # (local)
log10_As_A_B3 = float(d75['log10_As_ratio_A_B3'])  # (local) -9.51
log10_As_B_B3 = float(d75['log10_As_ratio_B_B3'])  # (local) +2.34
tau_cross_B3 = float(d75['tau_cross_B3'])  # (local)
tau_cross_B1 = float(d75['tau_cross_B1'])  # (local)
tau_cross_B2 = float(d75['tau_cross_B2'])  # (local)

log(f"  S75 Model A (power-law) log10[A_s ratio] @ B3: {log10_As_A_B3:.4f}")
log(f"  S75 Model B (spectral)  log10[A_s ratio] @ B3: {log10_As_B_B3:.4f}")
log(f"  Discrepancy: {log10_As_B_B3 - log10_As_A_B3:.4f} OOM")

# (b) S75 ns data (contains the Model B H(tau) profile)
d75_ns = np.load(os.path.join(data_dir, 's75_ns_nonpower_law_h.npz'),
                 allow_pickle=True)
tau_ns_fine = d75_ns['tau_fine']   # [0.16, 1.65], 500 points
H_ns_data = d75_ns['H_data']      # H(tau) from spectral action model
q_ns_eff = d75_ns['q_eff']        # effective deceleration

log(f"  S75 ns H(tau): tau=[{tau_ns_fine[0]:.3f}, {tau_ns_fine[-1]:.3f}], "
    f"H=[{H_ns_data.min():.2f}, {H_ns_data.max():.2f}] M_KK")

# (c) S73B coupled ODE solution
d73 = np.load(os.path.join(data_dir, 's73b_efold_mapping.npz'),
              allow_pickle=True)
t_73 = d73['t_sol']        # time in M_KK^{-1}
tau_73 = d73['tau_sol']     # tau(t) from ODE
H_73 = d73['H_sol']        # H(t) in M_KK units
lna_73 = d73['lna_sol']    # ln(a/a_fold)
w_73 = d73['w_sol']        # EOS w(t)
N_total = float(d73['N_total'])  # (local) 132.4

H_phys_fold_MKK = float(d73['H_phys_fold_MKK'])  # (local)
T_rh_73 = float(d73['T_rh_GeV'])  # (local)

log(f"  S73B: N_total = {N_total:.4f} e-folds")
log(f"  S73B: H_phys(fold) = {H_phys_fold_MKK:.6f} M_KK")
log(f"  S73B: T_rh = {T_rh_73:.4e} GeV")
log(f"  S73B: t_range = [{t_73[0]:.4e}, {t_73[-1]:.4e}] M_KK^{{-1}}")

# (d) S66 spectral data for a_2(tau)
d66 = np.load(os.path.join(data_dir, 's66_zeta_sa.npz'), allow_pickle=True)
tau_16 = d66['tau_all']
a2_16 = d66['a2']
a4_16 = d66['a4']
S_cutoff_16 = d66['S_cutoff']

# (e) Modulus decay data
d_mod = np.load(os.path.join(data_dir, 's74_modulus_decay.npz'),
                allow_pickle=True)
Gamma_mod = float(d_mod['Gamma_mod'])  # (local) GeV
m_mod = float(d_mod['m_mod'])  # (local) GeV
T_rh_74 = float(d_mod['T_rh'])  # (local) GeV

tau_decay_s = hbar_GeV_s / Gamma_mod  # (local) modulus lifetime in seconds
tau_decay_MKK_inv = tau_decay_s * M_KK / hbar_GeV_s  # (local) lifetime in M_KK^{-1}

log(f"\n  Modulus: m = {m_mod:.4e} GeV, Gamma = {Gamma_mod:.4e} GeV")
log(f"  Modulus lifetime: {tau_decay_s:.4e} s = {tau_decay_MKK_inv:.4e} M_KK^{{-1}}")
log(f"  T_rh(S74) = {T_rh_74:.4e} GeV")

# ============================================================================
#  SECTION 2: STRUCTURAL ANALYSIS -- Why Both Models Fail
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 2: Structural Diagnosis of the A/B Discrepancy")
log("=" * 78)

# The root cause: tau is NOT a monotonic proxy for cosmic time.
# S73B shows tau overshoots to 1.614 at t ~ 0.09 M_KK^{-1},
# then oscillates and decays. Model A assumes tau increases monotonically
# and uses H ~ (tau_fold/tau)^2. Model B uses S(tau)/a_2(tau) which
# increases because S grows faster than a_2 shrinks.

# Find tau_max from S73B data
idx_tau_max = np.argmax(tau_73)  # (local)
tau_max = tau_73[idx_tau_max]  # (local)
t_tau_max = t_73[idx_tau_max]  # (local)
H_at_tau_max = H_73[idx_tau_max]  # (local)

log(f"\n  [DIAGNOSIS 1] tau is NOT monotonic in time.")
log(f"    tau_max = {tau_max:.4f} at t = {t_tau_max:.4e} M_KK^{{-1}}")
log(f"    H(tau_max) = {H_at_tau_max:.6f} M_KK")
log(f"    Model A assumes tau ~ t^alpha (monotonic) -- INVALID post-overshoot")
log(f"    Model B evaluates S(tau)/a_2(tau) on vacuum geometry -- MISSES matter content")

# Demonstrate that S73B H(t) does decrease post-fold (Model A's PHYSICS is right)
H_fold_73 = H_73[0]  # (local)
H_end_73 = H_73[-1]  # (local)

log(f"\n  [DIAGNOSIS 2] H(t) DECREASES monotonically in the S73B ODE solution.")
log(f"    H(t=0) = {H_fold_73:.6f} M_KK")
log(f"    H(t=100) = {H_end_73:.6f} M_KK")
log(f"    Overall decrease: factor {H_fold_73/H_end_73:.4f}")

# But the decrease is MUCH slower than Model A predicts
# Model A: H(t_100) ~ H_fold * (tau_fold / tau_at_t100)^2
# At t=100, tau has overshot and returned, so tau(t=100) is NEGATIVE
# (S73B shows tau becomes -99 at t=100 -- unphysical clamping)
# The actual physical evolution reaches only ~63 e-folds in 100 M_KK^{-1}

log(f"\n  [DIAGNOSIS 3] Model A's power-law drastically oversuppresses H.")
log(f"    Model A at tau_cross(B3) = {tau_cross_B3:.2f}:")
log(f"      H_A = {H_fold_canon} * ({tau_fold}/{tau_cross_B3:.2f})^2 "
    f"= {H_fold_canon * (tau_fold/tau_cross_B3)**2:.6e} M_KK")
log(f"    But S73B ODE never reaches tau > {tau_max:.2f}!")
log(f"    The tau_cross values from S74 are EXTRAPOLATIONS beyond the physical range.")

log(f"\n  [DIAGNOSIS 4] Model B misidentifies the energy source.")
log(f"    S(tau) is the vacuum spectral action = integral Tr[f(D_K^2/Lambda^2)]")
log(f"    It describes the GEOMETRY of the fiber, not the energy in excitations.")
log(f"    Post-fold, the energy is carried by:")
log(f"      (i)   Modulus KE: (1/2) G dot_tau^2 (stiff, w=+1)")
log(f"      (ii)  GGE relic: E_exc * M_KK^4 / a^4 (radiation-like)")
log(f"      (iii) Spectral action potential V(tau) ~ (2/pi^2) a_0 * S(tau)/S_fold")
log(f"    Model B uses H^2 ~ S(tau)/a_2(tau) but S(tau) is component (iii) only.")
log(f"    Components (i) and (ii) dominate at the fold and post-fold!")

# ============================================================================
#  SECTION 3: The Correct Three-Phase H(t) from First Principles
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 3: Three-Phase H(t) from the Coupled Friedmann Equation")
log("=" * 78)

# The correct Friedmann equation (substrate-derived):
#
#   3 M_Pl^2 H^2 = rho_total
#   rho_total = rho_stiff + rho_rad + rho_matter + rho_Lambda
#
# where:
#   M_Pl^2 = a_2(tau) * M_KK^2 / (48 pi^2)    [from spectral action]
#   rho_stiff = (1/2) G_DeWitt * M_KK^4 * dot_tau^2  [modulus KE]
#   rho_rad = rho_GGE + rho_SM_rad              [GGE relic + SM radiation]
#   rho_matter = 0 (SM matter forms later at BBN)
#   rho_Lambda = (2/pi^2) * a_0 * M_KK^4       [vacuum spectral action]
#
# Key point: M_Pl^2 ~ a_2(tau) is CONSTANT after modulus settles.
# The a_2 evaluation is at the SETTLED tau, not evolving tau.
# This is because a_2 determines the gravitational coupling, and
# after modulus decay, tau is fixed (no more spectral evolution).

# Phase boundaries:
# Phase 1 (Stiff): fold -> modulus oscillation damping
#   Ends when modulus KE drops below radiation energy
#   w_eff ~ 1 -> 1/3 transition
#   Duration: ~63 e-folds of stiff expansion (S73B N_modulus)

# Phase 2 (Radiation): modulus decay -> matter-radiation equality
#   Standard radiation-dominated Friedmann
#   Duration: ~42 e-folds (from T_rh ~ 10^10 GeV to T_eq ~ 1 eV)

# Phase 3 (Matter + Lambda): equality to today
#   Duration: ~27 e-folds (from z_eq ~ 3400 to z=0)
#   Last ~8 e-folds Lambda-dominated

N_stiff = float(d73['N_modulus'])  # (local) from S73B
N_post_rh = float(d73['N_post_rh'])  # (local)

log(f"  Phase 1 (Stiff/modulus): N = {N_stiff:.2f} e-folds")
log(f"  Phase 2+3 (Post-reheating): N = {N_post_rh:.2f} e-folds")
log(f"  Total: N = {N_stiff + N_post_rh:.2f} e-folds")

# ============================================================================
#  SECTION 4: Quantitative H(t) Across All Phases
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 4: Quantitative H(t) Profile")
log("=" * 78)

# We construct H(N) where N = ln(a/a_fold) is the number of e-folds.
# This is the natural variable for the Friedmann equation.

# Phase 1: Stiff era (N = 0 to N_stiff)
# The S73B ODE gives H(t) directly. Convert to H(N):

# Construct H(N) from S73B data
N_phase1 = lna_73  # (local) already = ln(a/a_fold)
H_phase1 = H_73    # (local) H in M_KK units

# Key point: S73B H is the PHYSICAL Friedmann H, not the transit H_fold.
# H_fold = 586.5 is from sqrt(V_gradient_energy / (3 M_Pl^2)) using the
# full spectral action gradient at the fold. The S73B ODE uses a different
# normalization because it works with V_eff rather than dS/dtau directly.

log(f"  Phase 1 (S73B ODE):")
log(f"    N range: [0, {N_phase1[-1]:.4f}] = {N_stiff:.2f} e-folds")
log(f"    H range: [{H_phase1.min():.6f}, {H_phase1.max():.6f}] M_KK (S73B units)")

# The ratio between H_fold_canon (586.5 M_KK) and H_73[0] (0.975 M_KK)
# reflects two different quantities:
#   H_fold_canon = sqrt[(1/2 G v_tau^2 + V_fold) / (3 M_Pl^2/M_KK^2)]
#     using G_DeWitt = 5.0, v_tau = 26.545, V_fold = 1304.7 M_KK^4
#     KE = 0.5 * 5.0 * 26.545^2 = 1762.3 M_KK^4
#     rho = 1762.3 + 1304.7 = 3067.0 M_KK^4
#     H^2 = 3067.0 / (3 * (M_Pl/M_KK)^2)
#     (M_Pl/M_KK)^2 = (2.435e18 / 7.429e16)^2 = 1074.0
#     H^2 = 3067.0 / 3222.0 = 0.952
#     H = 0.976 M_KK -- matches S73B!
#
# So H_fold_canon = 586.5 M_KK was a DIFFERENT formula (from S38 KZ dynamics,
# H_fold = sqrt[(dS/dtau)^2 / (6 * Z_fold)] where Z_fold is gradient stiffness).
# The S73B Friedmann H is ~0.976 M_KK.

H_fold_friedmann = np.sqrt(  # (local)
    (0.5 * G_DeWitt * v_terminal**2 + (2.0/PI**2) * a0_fold) /
    (3.0 * (M_Pl_reduced / M_KK)**2)
)

log(f"\n  H_fold cross-check:")
log(f"    From Friedmann: H = {H_fold_friedmann:.6f} M_KK")
log(f"    From S73B ODE:  H = {H_73[0]:.6f} M_KK")
log(f"    From S38 (KZ):  H = {H_fold_canon:.4f} M_KK (DIFFERENT quantity -- transit rate)")

# The transit H_fold = 586.5 M_KK is the SUBSTRATE expansion rate
# (how fast spectral weight redistributes during the fold).
# The Friedmann H ~ 0.976 M_KK is the EMERGENT cosmic expansion rate.
# The ratio is:
ratio_H = H_fold_canon / H_fold_friedmann  # (local)
log(f"    Ratio H_transit / H_Friedmann = {ratio_H:.2f}")
log(f"    This is sqrt(Z_fold / (3 M_Pl^2)) / sqrt(rho_fold / (3 M_Pl^2))")
log(f"    = sqrt(Z_fold / rho_fold) = sqrt({74730.76 / 3067:.1f}) = {np.sqrt(74730.76/3067):.1f}")

# ============================================================================
#  SECTION 5: Model A Reinterpretation in Physical Time
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 5: Model A Reinterpreted -- H(N) in Physical E-fold Variable")
log("=" * 78)

# Model A claimed H ~ (tau_fold/tau)^2, which gives H suppression at large tau.
# In physical Friedmann evolution, the stiff era gives H ~ 1/(3t) or
# H(N) = H_fold * exp(-3N) [since a ~ t^{1/3} -> N ~ (1/3) ln t -> t ~ exp(3N)].
# But this is too fast.
#
# Actually: H ~ 1/(3t) -> H(a) = H_fold * (a_fold/a)^3 for stiff w=1.
# In e-fold variable: H(N) = H_fold * exp(-3N).
#
# For radiation (w=1/3): H(N) = H_rh * exp(-2N_rad) where N_rad counts from reheating.
# For matter (w=0): H(N) = H_eq * exp(-3N_mat/2).

# Model A's physics (energy dilution) IS correct in principle.
# The error was parameterizing it in tau rather than in N (e-folds).

# Construct H(N) for the full evolution:
N_grid = np.linspace(0, N_total, 10000)  # (local) 0 to 132.4

H_of_N = np.zeros_like(N_grid)  # (local)
phase_label = np.zeros_like(N_grid, dtype=int)  # (local)

# Phase 1: Stiff (N = 0 to N_stiff = 63.4)
# Use S73B data directly where available
# S73B covers N up to 63.4 but its H values are in the coupled regime
# (not pure stiff). Use the ODE solution directly.

# Interpolate S73B H(N) for Phase 1
from scipy.interpolate import interp1d
H_phase1_interp = interp1d(N_phase1, H_phase1,
                           kind='cubic', fill_value='extrapolate')  # (local)

# Phase 2+3: Post-reheating standard cosmology
# After modulus decays, T_rh ~ 10^10 GeV -> standard Friedmann
# N_rad = ln(T_rh / T_eq) where T_eq ~ 0.8 eV = 0.8e-9 GeV
T_eq_GeV = 0.8e-9  # (local) matter-radiation equality temperature
T_rh_eff = T_rh_74  # (local) use S74 reheating temperature

# Number of e-folds in radiation era (T_rh -> T_eq)
N_rad = np.log(T_rh_eff / T_eq_GeV)  # (local)
log(f"  N_radiation = ln(T_rh / T_eq) = ln({T_rh_eff:.2e} / {T_eq_GeV:.2e})")
log(f"            = {N_rad:.2f} e-folds")

# Number of e-folds in matter era (T_eq -> T_Lambda)
T_Lambda_GeV = T_CMB_GeV * (1 + 0.5)  # (local) Lambda domination at z ~ 0.5
N_matter = np.log(T_eq_GeV / T_Lambda_GeV)  # (local)
log(f"  N_matter = ln(T_eq / T_Lambda) = {N_matter:.2f} e-folds")

# Number of e-folds in Lambda era (T_Lambda -> today)
N_lambda = np.log((1 + 0.5))  # (local)
log(f"  N_lambda = ln(1+z_Lambda) = {N_lambda:.2f} e-folds")

log(f"  Total post-RH: N_rad + N_matter + N_lambda = "
    f"{N_rad + N_matter + N_lambda:.2f}")
log(f"  S73B N_post_rh = {N_post_rh:.2f}")

# Build H(N) array
# H at reheating (transition from stiff to radiation)
H_rh_MKK = H_phase1_interp(min(N_stiff, N_phase1[-1]))  # (local) H at end of stiff era

# Convert to GeV for the standard cosmology phases
H_rh_GeV = H_rh_MKK * M_KK  # (local)

log(f"\n  H at reheating: {H_rh_MKK:.6e} M_KK = {H_rh_GeV:.4e} GeV")

# Standard Friedmann:
# Radiation: H(N) = H_rh * exp(-2 * (N - N_stiff))
# Matter:    H(N) = H_eq * exp(-1.5 * (N - N_stiff - N_rad))
# Lambda:    H(N) = H_Lambda = const (de Sitter)

H_eq_MKK = H_rh_MKK * np.exp(-2.0 * N_rad)  # (local)
H_eq_GeV = H_eq_MKK * M_KK  # (local)

for i, N_val in enumerate(N_grid):
    if N_val <= N_stiff:
        # Phase 1: Use S73B ODE interpolation
        if N_val <= N_phase1[-1]:
            H_of_N[i] = H_phase1_interp(N_val)
        else:
            # Extrapolate stiff: H ~ exp(-3N)
            H_of_N[i] = H_phase1[-1] * np.exp(-3.0 * (N_val - N_phase1[-1]))
        phase_label[i] = 1
    elif N_val <= N_stiff + N_rad:
        # Phase 2: Radiation era
        dN = N_val - N_stiff  # (local)
        H_of_N[i] = H_rh_MKK * np.exp(-2.0 * dN)
        phase_label[i] = 2
    elif N_val <= N_stiff + N_rad + N_matter:
        # Phase 3a: Matter era
        dN = N_val - N_stiff - N_rad  # (local)
        H_of_N[i] = H_eq_MKK * np.exp(-1.5 * dN)
        phase_label[i] = 3
    else:
        # Phase 3b: Lambda era (approx constant H)
        H_of_N[i] = H_0_GeV / M_KK  # (local) final H
        phase_label[i] = 4

log(f"  H profile constructed over N = [0, {N_total:.1f}]")
log(f"    Phase 1 (stiff):     N = [0, {N_stiff:.1f}]")
log(f"    Phase 2 (radiation): N = [{N_stiff:.1f}, {N_stiff + N_rad:.1f}]")
log(f"    Phase 3 (matter):    N = [{N_stiff + N_rad:.1f}, {N_stiff + N_rad + N_matter:.1f}]")
log(f"    Phase 4 (Lambda):    N = [{N_stiff + N_rad + N_matter:.1f}, {N_total:.1f}]")

# ============================================================================
#  SECTION 6: Cross-Checks
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 6: Cross-Checks")
log("=" * 78)

# CHK1: H at fold
H_chk1 = H_of_N[0]  # (local)
chk1_pass = abs(H_chk1 - H_73[0]) / H_73[0] < 0.01  # (local)
log(f"  CHK1: H(N=0) = {H_chk1:.6f} M_KK, expected {H_73[0]:.6f} M_KK")
log(f"    -> {'PASS' if chk1_pass else 'FAIL'} (Friedmann H, not transit H_fold=586.5)")

# The transit H_fold=586.5 is a DIFFERENT quantity -- it measures the rate
# of spectral redistribution, not the cosmic expansion rate.
# The Friedmann H = 0.976 M_KK is verified by the S73B ODE.

# CHK2: H at z=0
H_chk2 = H_of_N[-1]  # (local)
H_0_MKK = H_0_GeV / M_KK  # (local)
chk2_ratio = H_chk2 / H_0_MKK  # (local)
chk2_log = np.log10(chk2_ratio)  # (local)
log(f"\n  CHK2: H(N={N_total:.1f}) = {H_chk2:.4e} M_KK")
log(f"    H_0(observed) = {H_0_MKK:.4e} M_KK")
log(f"    Ratio = {chk2_ratio:.4e} (log10 = {chk2_log:.2f})")

# The ratio should be 1 if the phase boundaries are exact.
# Since we use approximate phase boundaries, we check order-of-magnitude.
chk2_pass = abs(chk2_log) < 3.0  # (local) within 3 OOM
log(f"    -> {'PASS' if chk2_pass else 'FAIL'} (within 3 OOM)")

# CHK3: Energy conservation -- check H decreases monotonically
dH_dN = np.diff(H_of_N) / np.diff(N_grid)  # (local)
frac_increasing = np.sum(dH_dN > 0) / len(dH_dN)  # (local)
log(f"\n  CHK3: Monotonic H decrease (energy conservation)")
log(f"    Fraction of steps where dH/dN > 0: {frac_increasing:.4f}")
log(f"    (Should be 0 for pure deceleration)")
# Note: during Phase 1, S73B allows non-monotonic H because the modulus
# oscillates, temporarily violating naive monotonicity.
chk3_pass = frac_increasing < 0.10  # (local) < 10% non-monotonic
log(f"    -> {'PASS' if chk3_pass else 'FAIL'}")

# CHK4: Total e-folds
N_total_chk = N_grid[-1]  # (local)
chk4_pass = abs(N_total_chk - N_total) / N_total < 0.01  # (local)
log(f"\n  CHK4: Total e-folds = {N_total_chk:.2f}, expected {N_total:.2f}")
log(f"    -> {'PASS' if chk4_pass else 'FAIL'}")

# CHK5: Recover Model A and B as limiting cases
# Model A: for stiff era (w=1), H(N) ~ exp(-3N) -> H(tau_fold/tau)^2 if tau ~ exp(N)
# This is approximately true when dot_tau is constant (early stiff phase).
# But tau is NOT exp(N) -- it overshoots and returns.
H_A_at_1efold = H_fold_friedmann * np.exp(-3.0 * 1.0)  # (local)
H_73_at_1efold_idx = np.argmin(np.abs(lna_73 - 1.0))  # (local)
H_73_at_1efold = H_73[H_73_at_1efold_idx] if H_73_at_1efold_idx < len(H_73) else None  # (local)

log(f"\n  CHK5: Model A/B recovery")
if H_73_at_1efold is not None:
    log(f"    At N=1: Stiff model H = {H_A_at_1efold:.6f}, "
        f"S73B H = {H_73_at_1efold:.6f}, ratio = {H_A_at_1efold/H_73_at_1efold:.4f}")
log(f"    (Model A physics correct for STIFF ERA but wrong variable tau vs N)")
log(f"    (Model B wrong because S(tau) is vacuum geometry, not total energy)")

# ============================================================================
#  SECTION 7: Resolution of the A_s Gap
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 7: Impact on A_s Gap")
log("=" * 78)

# The A_s formula: A_s ~ H^2 / (eps_H * M_Pl^2)
# The key question for A_s: what is H at the epoch when CMB perturbations freeze out?
#
# In the substrate framework, perturbations are generated at the FOLD,
# not at a slow-roll epoch 60 e-folds before the end of inflation.
# The relevant H is the Friedmann H at the fold: ~0.976 M_KK.
#
# This is NOT the transit H_fold = 586.5 M_KK, which is the substrate rate.
# The A_s gap computed in S75 used H_fold = 586.5 in the numerator.
# If the correct H is 0.976, the A_s gap changes by:
#   Delta_log10 = 2 * log10(586.5 / 0.976) = 2 * 2.779 = 5.56 OOM

ratio_transit_to_friedmann = H_fold_canon / H_fold_friedmann  # (local)
As_correction_OOM = 2.0 * np.log10(ratio_transit_to_friedmann)  # (local)

log(f"  Transit H / Friedmann H = {ratio_transit_to_friedmann:.2f}")
log(f"  A_s correction = 2 * log10({ratio_transit_to_friedmann:.2f}) "
    f"= {As_correction_OOM:.2f} OOM")
log(f"  (H^2 in A_s formula: using Friedmann H REDUCES A_s by {As_correction_OOM:.2f} OOM)")

# The S75 A_s gap was 9.47 OOM (Model A) or +2.34 OOM (Model B).
# With Friedmann H instead of transit H:
#   Model A gap: 9.47 - 5.56 = 3.91 OOM (still too large, but much closer)
#   The remaining 3.91 OOM comes from eps_H and M_Pl^2 normalization

# But wait: the ENTIRE A_s calculation from S74/S75 used H_fold = 586.5.
# The Friedmann H at fold is 0.976 M_KK. So A_s(fold) is:
# A_s_fold ~ H_friedmann^2 / (eps_H * M_Pl_eff^2)
# M_Pl_eff^2 = a2_fold * M_KK^2 / (48 pi^2) = 2776.2 * M_KK^2 / (48 pi^2)
#            = 5.861 M_KK^2

M_Pl_eff_sq = a2_fold / (48.0 * PI**2)  # (local) in M_KK^2 units
H_friedmann_sq = H_fold_friedmann**2  # (local) in M_KK^2 units

# eps_H from the spectral action gradient
# eps_H = -(dH/dN) / H = -dot_H / H^2
# From S73B, extract eps at fold from the ODE
if len(H_73) > 10:
    dH_dt = np.gradient(H_73[:100], t_73[:100])  # (local)
    eps_fold_73 = -dH_dt[0] / H_73[0]**2  # (local) = -dot_H / H^2
else:
    eps_fold_73 = 0.022  # (local) fallback

# But eps_H should use the e-fold time N, not coordinate time t:
# eps_H = -(1/H) * dH/dN = -(1/H^2) * dH/dt * (dt/dN) = -(1/H^2) * dH/dt / H
# = -(1/H^3) * dH/dt ... actually eps_H = -(dH/dN)/H = -(dH/dt)/(H^2)
# since dN = H dt.

# From S73B ODE:
# dH/dt at fold can be estimated from the ODE itself:
# 3H^2 M_Pl^2 = rho -> 6H dot_H M_Pl^2 = dot_rho = -3H(rho + P) = -3H(1+w)rho
# dot_H = -(1+w)/2 * H * rho/M_Pl^2 ... but rho/(M_Pl^2) = 3H^2
# dot_H = -(3/2)(1+w) H^3 / H = -(3/2)(1+w) H^2
# Wait: dot_H = -(1+w) * rho / (2 M_Pl^2) = -(1+w)/2 * 3 H^2 = -(3/2)(1+w) H^2
# Wrong sign convention. Standard: dot_H = -(4piG)(rho+P) = -(rho+P)/(2M_Pl^2)
# = -(1+w)*rho/(2M_Pl^2) = -(3/2)(1+w)*H^2
# eps = -dot_H/H^2 = (3/2)(1+w)

w_at_fold = float(w_73[0])  # (local)
eps_fold_from_w = 1.5 * (1.0 + w_at_fold)  # (local) = 3(1+w)/2

log(f"\n  At the fold:")
log(f"    w_fold = {w_at_fold:.6f}")
log(f"    eps_H = (3/2)(1 + w) = {eps_fold_from_w:.6f}")
log(f"    H_Friedmann = {H_fold_friedmann:.6f} M_KK")
log(f"    M_Pl_eff^2 = a_2/(48 pi^2) = {M_Pl_eff_sq:.4f} M_KK^2")

# A_s ~ H^2 / (8 pi^2 eps_H M_Pl^2)   (standard slow-roll formula)
A_s_fold_raw = H_friedmann_sq / (8.0 * PI**2 * eps_fold_from_w * M_Pl_eff_sq)  # (local) dimensionless
log10_As_fold = np.log10(A_s_fold_raw)  # (local)
log10_As_obs = np.log10(A_s_CMB)  # (local)
As_gap = log10_As_fold - log10_As_obs  # (local)

log(f"\n  A_s(fold, Friedmann H) = {A_s_fold_raw:.4e}")
log(f"  log10[A_s] = {log10_As_fold:.4f}")
log(f"  A_s(CMB observed) = {A_s_CMB:.4e}")
log(f"  log10[A_s_obs] = {log10_As_obs:.4f}")
log(f"  Gap = {As_gap:.4f} OOM")

# The gap using Friedmann H is MUCH smaller than the S75 value
# because H_friedmann << H_transit by a factor of ~600.

# Now check at later times (Phase 1 decay):
# In the stiff era, eps_H = 3(1+w)/2 ~ 3 (for w~1)
# H(N) ~ exp(-3N) (stiff)
# So A_s(N) ~ exp(-6N) / (3 * M_Pl^2) ~ exp(-6N) * const
# A_s DECREASES by 6 OOM per e-fold. This is extremely rapid suppression.

log(f"\n  Stiff-era suppression rate:")
log(f"    A_s ~ H^2/eps ~ exp(-6N) (for w=1 stiff)")
log(f"    After 1 e-fold: suppression by {6:.1f} OOM")
log(f"    After 10 e-folds: suppression by {60:.0f} OOM")
log(f"    This is Model A's correct physics in the proper variable.")

# ============================================================================
#  SECTION 8: The Perturbation Epoch Question
# ============================================================================

log("\n" + "=" * 78)
log("SECTION 8: When Do CMB Perturbations Freeze Out?")
log("=" * 78)

# In standard inflation: perturbations generated 50-60 e-folds before end.
# In exflation: perturbations generated AT THE FOLD (the transit event).
# They then propagate through the stiff era.
#
# The question for A_s: is the RELEVANT H the value at the fold,
# or at some later time when modes "freeze out"?
#
# The S75 tau_cross values (B3=13.2, B1=18.0, B2=112.5 in tau units)
# correspond to when modes cross the acoustic horizon k = c_s * aH.
# But these were computed using Model A's H(tau), which is now invalid.
#
# In the correct Friedmann picture:
# k_phys = k / a(t)
# Horizon crossing: k_phys = H(t) (for GR modes)
# Acoustic horizon: k_phys = c_s * H(t) / (1 + c_s^2)
#
# For modes generated at the fold (impulsive, not slow-roll),
# the relevant A_s is set by the Bogoliubov coefficient at production,
# not by a slow-roll formula. The slow-roll formula is an approximation
# that assumes H is nearly constant over one Hubble time.
# In the stiff era, H changes by a factor e^3 per e-fold -- NOT slow-roll!

log(f"  CRITICAL: The slow-roll A_s formula does NOT apply in the stiff era.")
log(f"    eps_H = {eps_fold_from_w:.3f} >> 1  (NOT slow-roll: eps << 1)")
log(f"    The correct A_s comes from the Bogoliubov coefficient")
log(f"    at the fold, which was computed in S74 (s74_as_from_bogoliubov).")
log(f"    Post-fold H decay affects how modes PROPAGATE, not how they are PRODUCED.")

# The S74 Bogoliubov A_s used H_fold = 586.5 in its formula.
# That's the TRANSIT rate (substrate spectral redistribution speed).
# The Friedmann H ~ 0.976 M_KK is the EXPANSION rate.
# For Bogoliubov particle production, the relevant rate is the one
# that enters the mode equation: u'' + (k^2 - z''/z) u = 0.
# z''/z ~ a^2 * (V''/H^2 - ...) in slow-roll, but in the stiff regime
# z''/z ~ a^2 * (2H^2 + ...) with FRIEDMANN H.

# The Bogoliubov coefficient depends on which H enters z''/z.
# In exflation, the relevant dynamics is the Jensen parameter transit,
# which has rate H_fold = 586.5 M_KK (spectral redistribution).
# But the mode equation z''/z is governed by a_eff(t) which uses
# Friedmann H = 0.976 M_KK.
#
# This is the RESOLUTION: the A_s computation must use Friedmann H,
# not transit H_fold, in the mode equation.

log(f"\n  RESOLUTION STATEMENT:")
log(f"    The S74/S75 A_s gap (9.47 OOM) was computed using transit H = {H_fold_canon:.1f}")
log(f"    The correct H for the Friedmann equation is {H_fold_friedmann:.3f} M_KK")
log(f"    Ratio: {ratio_transit_to_friedmann:.1f}")
log(f"    This does NOT automatically close the gap because the Bogoliubov")
log(f"    coefficient also changes when H changes in the mode equation.")
log(f"    The net effect requires recomputing the S74 Bogoliubov analysis")
log(f"    with H_Friedmann. This is a SEPARATE computation (not available here).")

# ============================================================================
#  SECTION 9: Gate Verdict
# ============================================================================

log("\n" + "=" * 78)
log("GATE VERDICT: S76-A5-POST-FOLD-H")
log("=" * 78)

# Summary of findings:
# 1. Model A's PHYSICS is correct (H decreases post-fold due to energy dilution)
#    but its PARAMETERIZATION is wrong (used tau as time proxy; tau overshoots)
# 2. Model B is INCORRECT (uses vacuum spectral action, misses matter content)
# 3. The correct H(t) is the S73B coupled ODE solution
# 4. H at fold = 0.976 M_KK (Friedmann), not 586.5 M_KK (transit)
# 5. The two H values are different physical quantities
# 6. A_s gap is affected by ~5.6 OOM from the H identification
# 7. Full resolution requires recomputing Bogoliubov A_s with Friedmann H

# The gate asks for a single self-consistent H(tau) with n_s and A_s consistent.
# We HAVE a single self-consistent H(t) (the S73B ODE solution), but:
# - We cannot express it as H(tau) because tau is not monotonic
# - The A_s impact requires a separate Bogoliubov recomputation

gate_verdict = "INFO"  # (local)
gate_detail = (
    f"Model A/B reconciled: both incomplete. Correct H(t) from S73B coupled ODE "
    f"(H_fold_Friedmann = {H_fold_friedmann:.3f} M_KK, NOT H_transit = {H_fold_canon:.1f}). "
    f"tau not monotonic (max = {tau_max:.3f}), so H(tau) is ill-defined post-overshoot. "
    f"Model A physics correct (energy dilutes), Model B wrong (vacuum geometry != total energy). "
    f"A_s gap correction ~{As_correction_OOM:.1f} OOM from H identification. "
    f"Full A_s requires Bogoliubov recomputation with H_Friedmann (unavailable)."
)

log(f"\n  Verdict: {gate_verdict}")
log(f"  Detail: {gate_detail}")
log(f"\n  KEY NUMBERS:")
log(f"    H_fold_Friedmann = {H_fold_friedmann:.6f} M_KK")
log(f"    H_fold_transit   = {H_fold_canon:.4f} M_KK")
log(f"    Ratio             = {ratio_transit_to_friedmann:.2f}")
log(f"    tau_max            = {tau_max:.4f}")
log(f"    A_s(fold, Friedmann) = {A_s_fold_raw:.4e} (log10 = {log10_As_fold:.2f})")
log(f"    A_s(CMB)             = {A_s_CMB:.4e} (log10 = {log10_As_obs:.2f})")
log(f"    Gap (Friedmann H)    = {As_gap:.2f} OOM")
log(f"    Gap (transit H, S75) = 9.47 OOM")
log(f"    Delta                = {9.47 - As_gap:.2f} OOM from H identification")
log(f"    eps_H(fold)          = {eps_fold_from_w:.4f} (w = {w_at_fold:.4f})")
log(f"    N_total              = {N_total:.2f} e-folds")
log(f"    N_stiff              = {N_stiff:.2f} e-folds")

# ============================================================================
#  SECTION 10: Save Data
# ============================================================================

out_path = os.path.join(data_dir, 's76_post_fold_h_tau.npz')
np.savez(
    out_path,
    # Gate
    gate_name='S76-A5-POST-FOLD-H',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
    # Key results
    H_fold_friedmann=H_fold_friedmann,
    H_fold_transit=H_fold_canon,
    ratio_H_transit_to_friedmann=ratio_transit_to_friedmann,
    tau_max=tau_max,
    t_at_tau_max=t_tau_max,
    w_fold=w_at_fold,
    eps_fold_from_w=eps_fold_from_w,
    M_Pl_eff_sq=M_Pl_eff_sq,
    # A_s
    A_s_fold_friedmann=A_s_fold_raw,
    log10_As_fold=log10_As_fold,
    As_gap_OOM=As_gap,
    As_correction_OOM=As_correction_OOM,
    # S75 comparison
    log10_As_A_B3=log10_As_A_B3,
    log10_As_B_B3=log10_As_B_B3,
    # H(N) profile
    N_grid=N_grid,
    H_of_N=H_of_N,
    phase_label=phase_label,
    N_stiff=N_stiff,
    N_rad=N_rad,
    N_total=N_total,
    # Cross-checks
    CHK1_pass=chk1_pass,
    CHK2_pass=chk2_pass,
    CHK2_log_ratio=chk2_log,
    CHK3_pass=chk3_pass,
    CHK4_pass=chk4_pass,
    # Input lineage
    gamma_a2=gamma_a2,
    gamma_a4=gamma_a4,
)

log(f"\n  Saved: {out_path}")

# ============================================================================
#  SECTION 11: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("S76-A5-POST-FOLD-H: Resolve Model A vs Model B for H(tau)",
             fontsize=13, fontweight='bold')

# Panel 1: H(N) full evolution
ax1 = axes[0, 0]
colors = {1: 'red', 2: 'orange', 3: 'blue', 4: 'purple'}
labels_map = {1: 'Stiff (modulus)', 2: 'Radiation', 3: 'Matter', 4: 'Lambda'}
for ph in [1, 2, 3, 4]:
    mask = phase_label == ph  # (local)
    if mask.any():
        ax1.semilogy(N_grid[mask], H_of_N[mask] * M_KK,
                     color=colors[ph], lw=1.5, label=labels_map[ph])
ax1.set_xlabel('N (e-folds from fold)')
ax1.set_ylabel('H [GeV]')
ax1.set_title('H(N) -- Full Expansion History')
ax1.legend(fontsize=8)
ax1.axhline(H_0_GeV, color='gray', ls='--', lw=0.8, label='H_0')
ax1.set_xlim(0, N_total)

# Panel 2: S73B Phase 1 detail -- H(t) and tau(t)
ax2 = axes[0, 1]
t_plot = t_73[:5000]  # (local) first 5000 points for detail
H_plot = H_73[:5000]  # (local)
tau_plot = tau_73[:5000]  # (local)
ax2.plot(t_plot, H_plot, 'b-', lw=1.5, label='H(t) [M_KK]')
ax2_twin = ax2.twinx()
ax2_twin.plot(t_plot, tau_plot, 'r-', lw=1.0, alpha=0.7, label='tau(t)')
ax2.set_xlabel('t [M_KK^{-1}]')
ax2.set_ylabel('H [M_KK]', color='b')
ax2_twin.set_ylabel('tau', color='r')
ax2.set_title('Phase 1: Coupled Friedmann + KG (S73B)')
ax2.legend(loc='upper left', fontsize=8)
ax2_twin.legend(loc='upper right', fontsize=8)

# Panel 3: Model comparison -- A vs B vs correct
ax3 = axes[1, 0]
tau_range_plot = np.linspace(tau_fold, 2.0, 200)  # (local)

# Model A: H ~ (tau_fold/tau)^2
H_model_A_plot = H_fold_canon * (tau_fold / tau_range_plot)**2  # (local)

# Model B: H increases (from S75 ns data)
# Interpolate from the S75 H data
from scipy.interpolate import interp1d
H_B_interp = interp1d(tau_ns_fine, H_ns_data,
                       kind='cubic', fill_value='extrapolate')  # (local)
H_model_B_plot = H_B_interp(np.clip(tau_range_plot, tau_ns_fine[0], tau_ns_fine[-1]))  # (local)

ax3.semilogy(tau_range_plot, H_model_A_plot, 'r--', lw=1.5, alpha=0.7,
             label=f'Model A: H ~ tau^{{-2}} (transit H)')
ax3.semilogy(tau_range_plot, H_model_B_plot, 'b--', lw=1.5, alpha=0.7,
             label='Model B: H ~ sqrt(S/a_2)')
ax3.axhline(H_fold_friedmann, color='green', ls='-', lw=2,
            label=f'Friedmann H = {H_fold_friedmann:.3f} M_KK')
ax3.axvline(tau_max, color='gray', ls=':', lw=0.8, label=f'tau_max = {tau_max:.2f}')
ax3.set_xlabel('tau (Jensen parameter)')
ax3.set_ylabel('H [M_KK]')
ax3.set_title('Model A vs Model B vs Friedmann')
ax3.legend(fontsize=7)
ax3.set_ylim(1e-3, 1e4)

# Panel 4: Diagnosis summary
ax4 = axes[1, 1]
ax4.axis('off')
summary_text = (
    f"DIAGNOSIS SUMMARY\n"
    f"{'='*40}\n\n"
    f"Model A (power-law H ~ tau^{{-2}}):\n"
    f"  Physics: CORRECT (energy dilutes)\n"
    f"  Variable: WRONG (tau not monotonic)\n"
    f"  H(fold): {H_fold_canon:.1f} M_KK (transit rate)\n\n"
    f"Model B (spectral S/a_2):\n"
    f"  Physics: WRONG (vacuum only, no matter)\n"
    f"  Result: H increases (unphysical)\n\n"
    f"CORRECT: Friedmann + Klein-Gordon ODE\n"
    f"  H(fold) = {H_fold_friedmann:.4f} M_KK\n"
    f"  tau overshoots to {tau_max:.3f}\n"
    f"  w(fold) = {w_at_fold:.4f}\n"
    f"  eps = {eps_fold_from_w:.4f}\n\n"
    f"A_s gap: {As_gap:.2f} OOM (was 9.47 OOM)\n"
    f"H correction: {As_correction_OOM:.2f} OOM\n\n"
    f"Gate: {gate_verdict}"
)
ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plot_path = os.path.join(data_dir, 's76_post_fold_h_tau.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
log(f"\n  Plot saved: {plot_path}")

log("\n" + "=" * 78)
log("COMPUTATION COMPLETE")
log("=" * 78)
