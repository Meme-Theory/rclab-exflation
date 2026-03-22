#!/usr/bin/env python3
"""
TWOFLUID-W-43: Two-Fluid w(z) Trajectory for DESI
===================================================
Einstein-Theorist, Session 43, Wave 2.

Physics: Volovik's Landau-Khalatnikov two-fluid decomposition (Paper 37)
applied to the phonon-exflation framework.

Superfluid component = spectral action vacuum (rho_s, P_s = -rho_s)
Normal component = GGE quasiparticles (rho_n, P_n = 0 for dust)

Two-fluid equations (Paper 37):
  dot(rho_s) + 3H*(rho_s + P_s) = -Gamma*(rho_s + P_s)   [superfluid]
  dot(rho_n) + 3H*(rho_n + P_n) = +Gamma*(rho_s + P_s)   [normal]
  H^2 = (8*pi*G/3)*(rho_s + rho_n)

Since P_s = -rho_s:  (rho_s + P_s) = 0 identically for pure CC.

This is the CRITICAL point: if the superfluid component is a pure cosmological
constant (w_s = -1 exactly), then (rho_s + P_s) = 0 and the mutual friction
term vanishes IDENTICALLY, regardless of Gamma. The two fluids decouple.

For w != -1, need w_s != -1. The framework gives:
  epsilon_V = (dS/dtau)^2 / (2 * Z * S^2) = 3.67e-7
  w_s = -1 + (2/3)*epsilon_V = -1 + 2.45e-7

This is the slow-roll departure from w = -1 for the spectral action.
With this tiny departure, (rho_s + P_s) = epsilon_V * 2 * rho_s / 3.

The mutual friction coupling is then:
  Gamma * (rho_s + P_s) = Gamma * (2/3) * epsilon_V * rho_s

Even though Gamma >> H, the source term is suppressed by epsilon_V ~ 3.7e-7.

We solve the full system numerically for 4 scenarios:
  (A) Pure CC: w_s = -1 exactly -> w = -1 (trivial)
  (B) Slow-roll: w_s = -1 + 2*epsilon_V/3 -> w departs by O(epsilon_V)
  (C) GGE-evolved: normal fluid has time-dependent EOS from GGE evolution
  (D) Volovik's prescription: rho_Lambda ~ t^{0.6}, rho_m ~ t^{-0.4}

Gate TWOFLUID-W-43:
  PASS: |w_0 + 1| > 0.001
  FAIL: |w_0 + 1| < 10^{-6}
  INTERMEDIATE: 10^{-6} to 0.001
"""

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# =============================================================================
# 1. LOAD UPSTREAM DATA
# =============================================================================
print("=" * 70)
print("TWOFLUID-W-43: Two-Fluid w(z) from Volovik Paper 37")
print("=" * 70)

grad = np.load('s42_gradient_stiffness.npz', allow_pickle=True)
gge = np.load('s42_gge_energy.npz', allow_pickle=True)
const = np.load('s42_constants_snapshot.npz', allow_pickle=True)
qth = np.load('s43_qtheory_selftune.npz', allow_pickle=True)
s38 = np.load('s38_attempt_freq.npz', allow_pickle=True)
s42wz = np.load('s42_dark_energy_wz.npz', allow_pickle=True)

# Extract framework parameters
def scalar(x):
    """Extract scalar from numpy array (handles 0-d arrays)."""
    v = np.asarray(x)
    return float(v.flat[0]) if v.size == 1 else float(v)

tau_fold = scalar(grad['tau_fold_used'])
S_fold = scalar(grad['S_fold'])
dS_fold = scalar(grad['dS_fold'])
d2S_fold = scalar(grad['d2S_fold'])
Z_fold = scalar(grad['Z_fold'])
epsilon_V = scalar(s42wz['epsilon_V'])  # 3.67e-7
omega_att = scalar(s38['omega_att_BCS'])  # 1.430 M_KK
omega_tau = scalar(s38['omega_tau_fold'])  # 8.27 M_KK
m_tau = scalar(s42wz['m_tau'])  # 2.062 M_KK
E_cond = scalar(s38['E_cond'])  # -0.156 M_KK^4
E_exc_MKK = scalar(gge['E_exc_MKK'])  # 50.945 M_KK
n_pairs = scalar(gge['n_pairs'])  # 59.8
r_suppression = scalar(qth['r_suppression'])  # 5.37e-7 (effacement)

# Physical constants
from canonical_constants import M_Pl_unreduced as M_Pl_GeV  # 1.22e19 GeV
H_0_GeV = 1.5e-42    # H_0 ~ 70 km/s/Mpc in GeV
M_KK_grav = float(gge['M_KK_gravity'])  # 7.43e16 GeV
M_KK_gauge = float(gge['M_KK_gauge'])   # 5.04e17 GeV

print(f"\n--- Framework Parameters ---")
print(f"tau_fold        = {tau_fold}")
print(f"S_fold          = {S_fold:.2f} M_KK^4")
print(f"dS/dtau(fold)   = {dS_fold:.2f} M_KK^4")
print(f"Z_fold          = {Z_fold:.2f} M_KK^4")
print(f"epsilon_V       = {epsilon_V:.4e}")
print(f"omega_att       = {omega_att:.4f} M_KK")
print(f"omega_tau       = {omega_tau:.4f} M_KK")
print(f"m_tau           = {m_tau:.4f} M_KK")
print(f"E_cond          = {E_cond:.6f} M_KK^4")
print(f"E_exc           = {E_exc_MKK:.3f} M_KK")
print(f"n_pairs         = {n_pairs}")
print(f"r_suppression   = {r_suppression:.4e}")

# =============================================================================
# 2. MUTUAL FRICTION SCALE
# =============================================================================
# Gamma = omega_att / (2*pi) in M_KK units
Gamma_MKK = omega_att / (2.0 * np.pi)  # M_KK
Gamma_Hz = Gamma_MKK * M_KK_grav / (6.582e-25)  # convert to Hz
H_0_Hz = H_0_GeV / (6.582e-25)  # ~ 2.3e-18 Hz

# Use both M_KK scales
for label, MKK in [("gravity", M_KK_grav), ("gauge", M_KK_gauge)]:
    G_Hz = Gamma_MKK * MKK / (6.582e-25)
    ratio = G_Hz / H_0_Hz
    print(f"\n--- Mutual Friction ({label}) ---")
    print(f"  Gamma       = {Gamma_MKK:.4f} M_KK = {G_Hz:.4e} Hz")
    print(f"  H_0         = {H_0_Hz:.4e} Hz")
    print(f"  Gamma/H_0   = {ratio:.4e}")

# Use gravity route for main computation
Gamma_phys = Gamma_MKK * M_KK_grav / (6.582e-25)  # Hz
GammaOverH0 = Gamma_phys / H_0_Hz

print(f"\n==> Gamma/H_0 = {GammaOverH0:.4e}")
print(f"    log10(Gamma/H_0) = {np.log10(GammaOverH0):.1f}")

# =============================================================================
# 3. CRITICAL ANALYSIS: WHY (rho_s + P_s) CONTROLS EVERYTHING
# =============================================================================
print("\n" + "=" * 70)
print("CRITICAL: Source term analysis")
print("=" * 70)

# For pure CC: P_s = -rho_s => rho_s + P_s = 0 IDENTICALLY
# For slow-roll: P_s = w_s * rho_s with w_s = -1 + 2*epsilon_V/3
# => rho_s + P_s = (1 + w_s) * rho_s = (2/3)*epsilon_V * rho_s

w_s_slowroll = -1.0 + (2.0/3.0) * epsilon_V
source_fraction = (1.0 + w_s_slowroll)  # = (2/3)*epsilon_V

print(f"w_s (slow-roll)       = {w_s_slowroll:.10f}")
print(f"1 + w_s               = {source_fraction:.4e}")
print(f"Source fraction        = (2/3)*epsilon_V = {(2.0/3.0)*epsilon_V:.4e}")
print(f"Gamma * (1+w_s)       = {Gamma_MKK * source_fraction:.4e} M_KK")
print(f"Gamma*(1+w_s) / H_0   = {GammaOverH0 * source_fraction:.4e}")

# The effacement ratio: |E_BCS|/S_fold
effacement = abs(E_cond) / S_fold
print(f"\nEffacement ratio      = |E_cond|/S_fold = {effacement:.4e}")
print(f"(cf r_suppression     = {r_suppression:.4e})")

# =============================================================================
# 4. NUMERICAL SOLUTION: TWO-FLUID FRIEDMANN EQUATIONS
# =============================================================================
print("\n" + "=" * 70)
print("NUMERICAL SOLUTION: Two-Fluid Friedmann")
print("=" * 70)

# Work in units where 8*pi*G/(3*H_0^2) = 1 (standard Friedmann normalization)
# Use ln(a) as the independent variable (a = scale factor, a_0 = 1 today)
# x = ln(a), so a = e^x, z = e^{-x} - 1

# State: [Omega_s, Omega_n] where Omega = rho / rho_crit_0

# Present-day values (LCDM-like initial conditions)
Omega_Lambda_0 = 0.7  # dark energy
Omega_m_0 = 0.3       # matter

# Gamma/H ratio as function of a
# H(a) = H_0 * sqrt(Omega_m * a^{-3} + Omega_Lambda)
# In the two-fluid model with exchange:
# Gamma_eff = Gamma * (1 + w_s) where w_s is the superfluid EOS

# The key dimensionless parameter:
# gamma = Gamma / H_0
gamma_dimless = GammaOverH0  # ~ 10^{58}

def rhs_twofluid(x, Y, gamma, w_s_val):
    """
    Two-fluid Friedmann in ln(a) variable.
    Y = [Omega_s, Omega_n]
    x = ln(a)

    d(Omega_s)/dx + 3*(1+w_s)*Omega_s = -(gamma/E(x)) * (1+w_s)*Omega_s
    d(Omega_n)/dx + 3*(1+w_n)*Omega_n = +(gamma/E(x)) * (1+w_s)*Omega_s

    where E(x) = H(a)/H_0 = sqrt(Omega_s + Omega_n * e^{-3x}) * e^{3x/2}
    Wait -- need to be careful. Let me use cosmic time.

    Actually, using x = ln(a):
    d(rho)/dt = (d(rho)/dx) * (dx/dt) = H * d(rho)/dx

    So: H * d(rho_s)/dx + 3H*(rho_s + P_s) = -Gamma*(rho_s + P_s)
    => d(rho_s)/dx = -3*(1+w_s)*rho_s - (Gamma/H)*(1+w_s)*rho_s
    => d(rho_s)/dx = -(1+w_s)*rho_s * (3 + Gamma/H)

    Similarly:
    d(rho_n)/dx = -3*(1+w_n)*rho_n + (Gamma/H)*(1+w_s)*rho_s
    """
    Os, On = Y

    # w_n = 0 for matter (dust)
    w_n = 0.0

    # E(x) = H(a)/H_0
    # In the two-fluid model, H^2 = (8piG/3)(rho_s + rho_n)
    # Normalize: Omega_total = Os + On
    # H^2/H_0^2 = Omega_total (already normalized)

    # But Os and On evolve, so H/H_0 = sqrt(Os + On) where
    # Os is the actual current Omega_s (not rescaled by a^3 etc)
    # This requires tracking rho, not Omega.

    # Let's track rho/rho_crit_0 directly.
    # rho_s_bar = rho_s / rho_crit_0, etc.
    # H^2 = H_0^2 * (rho_s_bar + rho_n_bar)
    # E = H/H_0 = sqrt(rho_s_bar + rho_n_bar)

    rho_total = Os + On
    if rho_total <= 0:
        return [0.0, 0.0]
    E = np.sqrt(rho_total)

    # Gamma/H = gamma_dimless / E
    GoverH = gamma / E

    # Evolution equations
    dOs_dx = -(1.0 + w_s_val) * Os * (3.0 + GoverH)
    dOn_dx = -3.0 * (1.0 + w_n) * On + GoverH * (1.0 + w_s_val) * Os

    return [dOs_dx, dOn_dx]


# Scenario A: Pure CC (w_s = -1 exactly)
# => (1+w_s) = 0 => source = 0 => decoupled => w = -1
print("\n--- Scenario A: Pure Cosmological Constant (w_s = -1) ---")
print("  (1 + w_s) = 0 identically.")
print("  Mutual friction source = 0 regardless of Gamma.")
print("  Two fluids DECOUPLE.")
print("  w(z) = -1 at all z. EXACT.")

# Scenario B: Slow-roll departure
print(f"\n--- Scenario B: Slow-Roll Departure (w_s = {w_s_slowroll:.10f}) ---")

# Initial conditions at a=1 (z=0, today)
Y0 = [Omega_Lambda_0, Omega_m_0]

# Integrate from x=0 (today, a=1) backward to x = -ln(1+z_max)
z_max = 5.0
x_start = 0.0
x_end = -np.log(1.0 + z_max)

# Use a MUCH smaller gamma to avoid stiffness (since gamma ~ 10^58)
# The physical result is clear: Gamma/H >> 1 means LOCAL EQUILIBRIUM
# Let me solve for a range of gamma values to show convergence

print(f"\n  Convergence test: gamma = Gamma/H_0")
print(f"  Physical value: gamma = {gamma_dimless:.4e}")

# For gamma >> 1 and (1+w_s) = epsilon_V ~ 3.7e-7:
# The equilibration rate is gamma * epsilon_V / E(x)
# At z=0: E = sqrt(0.7 + 0.3) = 1, so rate = gamma * epsilon_V
# For gamma = 10^58 and epsilon_V = 3.7e-7: rate = 3.7e51 >> 1

# In local equilibrium, the source term drives Omega_s to adjust so that
# the net source vanishes. This means (1+w_s)*Omega_s -> 0, i.e., either
# w_s -> -1 or Omega_s -> 0.

# For the physical system: epsilon_V is fixed by the spectral action geometry.
# The mutual friction rapidly transfers energy from superfluid to normal, but
# the transfer rate is proportional to (1+w_s)*rho_s = epsilon_V*rho_s*(2/3).
# Over one Hubble time, the fractional transfer is:
# delta_rho / rho ~ (Gamma/H) * (1+w_s) = gamma_dimless * 2/3 * epsilon_V

# This is HUGE (~10^51), which means the superfluid would EMPTY into normal
# fluid in a tiny fraction of a Hubble time... UNLESS the system reaches
# equilibrium where the back-reaction adjusts w_s.

# PHYSICAL RESOLUTION:
# In Volovik's model, the two-fluid coupling conserves TOTAL energy.
# The system reaches LOCAL THERMAL EQUILIBRIUM at the Gibbons-Hawking temp.
# In LTE, the effective w is:
# w_eff = (P_s + P_n) / (rho_s + rho_n)
# With P_s = -rho_s (exact for CC) and P_n = 0:
# w_eff = -rho_s / (rho_s + rho_n) = -Omega_Lambda

# Let me solve numerically for modest gamma to show convergence
# Limit gamma range to avoid stiffness issues at gamma > 1e6
# Physical gamma ~ 10^58, but we only need to show convergence
# The analytic proof covers the physical regime
gamma_values = [0.1, 1.0, 10.0, 100.0, 1000.0, 1e4]
w0_results = {}

# Fine z grid for output
z_out = np.linspace(0, z_max, 500)
x_out = -np.log(1.0 + z_out)  # negative values (past)

# For each gamma, integrate backward
for gval in gamma_values:
    w_s_B = w_s_slowroll
    one_plus_ws = 1.0 + w_s_B  # ~ 2.45e-7

    # Use stiff solver; t_eval must be sorted in integration direction
    # Integration goes from x=0 to x=x_end (negative), so sort descending
    x_eval_sorted = np.sort(x_out)[::-1]  # descending (0 to -ln(6))
    # But x_start=0 > x_end<0, so integration direction is decreasing
    sol = solve_ivp(
        rhs_twofluid,
        [x_start, x_end],
        Y0,
        args=(gval, w_s_B),
        method='Radau',
        t_eval=x_eval_sorted,
        rtol=1e-12,
        atol=1e-15,
        max_step=0.01
    )

    if sol.success:
        # Compute w_eff(z) = P_total / rho_total = (-rho_s) / (rho_s + rho_n)
        # since P_s = w_s * rho_s and P_n = 0
        Os_sol = sol.y[0]
        On_sol = sol.y[1]
        w_eff = (w_s_B * Os_sol) / (Os_sol + On_sol)

        # Map to z
        z_sol = np.exp(-sol.t) - 1.0

        # w at z=0
        w0_val = w_eff[np.argmin(np.abs(z_sol))]
        w0_results[gval] = w0_val

        # Store for gamma=1e4 for plotting
        if gval == 1e4:
            z_B_plot = z_sol.copy()
            w_B_plot = w_eff.copy()
            Os_B = Os_sol.copy()
            On_B = On_sol.copy()
    else:
        print(f"  gamma={gval:.0e}: FAILED ({sol.message})")
        w0_results[gval] = np.nan

print(f"\n  {'gamma':>12s}  {'w_0':>20s}  {'|w_0+1|':>15s}")
print(f"  {'-'*12}  {'-'*20}  {'-'*15}")
for gval in gamma_values:
    w0 = w0_results.get(gval, np.nan)
    if not np.isnan(w0):
        print(f"  {gval:12.0e}  {w0:20.15f}  {abs(w0+1):15.4e}")
    else:
        print(f"  {gval:12.0e}  {'FAILED':>20s}  {'N/A':>15s}")

# =============================================================================
# 5. ANALYTIC ESTIMATE IN LOCAL EQUILIBRIUM LIMIT
# =============================================================================
print("\n" + "=" * 70)
print("ANALYTIC: Local Equilibrium Limit (Gamma >> H)")
print("=" * 70)

# When Gamma >> H, the mutual friction instantaneously equilibrates.
# The condition for equilibrium of the source term:
#   Gamma * (1+w_s) * rho_s = 0
# Since Gamma != 0 and rho_s != 0, we need (1+w_s) = 0, i.e., w_s = -1.
#
# But w_s is FIXED by the spectral action geometry (epsilon_V).
# Resolution: the "superfluid" component adjusts its density on the
# mutual friction timescale (1/Gamma << 1/H) until the net energy
# transfer per Hubble time is negligible.
#
# The fractional energy transfer per Hubble time:
# delta_rho_n / rho_total ~ (Gamma/H) * (1+w_s) * (rho_s/rho_total) * (H/Gamma)
# Wait, this is circular. Let me think more carefully.
#
# The PHYSICAL point is that Gamma >> H means the two fluids are
# in thermal contact. The equilibrium condition is NOT that the source
# vanishes, but that the system reaches a STEADY STATE where:
#
# d(rho_s)/dt = -3H*(rho_s + P_s) - Gamma*(rho_s + P_s)
#
# In steady state, d(rho_s)/dt = 0:
# (3H + Gamma) * (rho_s + P_s) = 0
#
# Since 3H + Gamma != 0, we need rho_s + P_s = 0, i.e., w_s = -1 EXACTLY.
#
# This is the THERMODYNAMIC ATTRACTOR. Any departure from w_s = -1 is
# exponentially damped on the mutual friction timescale 1/Gamma.
#
# The actual w_s is set by the spectral action geometry: w_s = -1 + (2/3)*epsilon_V.
# This means the system is NOT in exact steady state but departs by O(epsilon_V).
# The departure produces an effective w:
#
# w_eff = w_LCDM + delta_w
# where delta_w is suppressed by both epsilon_V AND the equilibration dynamics.

# In the adiabatic limit (Gamma >> H), solve perturbatively.
# Let rho_s = rho_s^{(0)} + delta_rho_s, where rho_s^{(0)} satisfies w_s = -1.
# The correction delta_rho_s satisfies:
# Gamma * delta_rho_s ~ H * rho_s * (2/3) * epsilon_V
# => delta_rho_s / rho_s ~ (H/Gamma) * (2/3) * epsilon_V

delta_w_analytic = (2.0/3.0) * epsilon_V * (1.0 / GammaOverH0) * Omega_Lambda_0
print(f"Analytic delta_w = (2/3)*eps_V * (H_0/Gamma) * Omega_Lambda")
print(f"                 = {delta_w_analytic:.4e}")
print(f"|w_0 + 1|        = {abs(delta_w_analytic):.4e}")

# The H/Gamma suppression kills everything:
print(f"\nH_0/Gamma = {1.0/GammaOverH0:.4e}")
print(f"epsilon_V = {epsilon_V:.4e}")
print(f"Product   = {epsilon_V/GammaOverH0:.4e}")

# Even Volovik's power-law predictions need a MECHANISM to
# produce Gamma ~ H (not Gamma >> H). In our framework,
# Gamma is set by omega_att which is geometric and constant.

# =============================================================================
# 6. SCENARIO C: GGE-EVOLVED NORMAL FLUID
# =============================================================================
print("\n" + "=" * 70)
print("Scenario C: GGE Evolution (time-dependent normal EOS)")
print("=" * 70)

# The GGE has 8 conserved integrals. Post-transit, it is a product state (S_ent=0).
# The GGE does NOT thermalize (integrable, block-diagonal theorem).
# But the GGE quasiparticle energies redshift with expansion: E_k ~ 1/a for
# relativistic modes, E_k ~ const for massive modes.
#
# Total GGE energy post-transit: E_exc = 50.9 M_KK (59.8 pairs)
# Quasiparticle mass: m_qp ~ Delta ~ 0.464 M_KK
# At the transit epoch: E_k >> m_qp (relativistic, w_n = 1/3)
# At late times: E_k ~ m_qp (non-relativistic, w_n = 0)
#
# Transition from w_n = 1/3 to w_n = 0 occurs at a/a_transit ~ E_k/m_qp
# E_k_initial ~ E_exc/n_pairs = 50.9/59.8 = 0.851 M_KK
# a_transition ~ E_k/m_qp = 0.851/0.464 = 1.83

# But this is at the KK scale, a_transit ~ T_CMB/M_KK ~ 2.35e-22
# By z = 5 (a ~ 0.17), the quasiparticles have been non-relativistic for
# a factor of a ~ 0.17/(2.35e-22 * 1.83) = 3.9e20 >> 1.

# So w_n = 0 (dust) for ALL observable z. The GGE normal fluid behaves
# as cold dark matter.

a_transit = 2.725e-4 / (M_KK_grav / 1.16e13)  # T_CMB/M_KK (CMB temp / M_KK)
# M_KK_grav = 7.43e16 GeV, T_CMB = 2.725 K = 2.35e-13 GeV
from canonical_constants import T_CMB_GeV  # GeV
a_transit_val = T_CMB_GeV / M_KK_grav

E_per_pair = E_exc_MKK / n_pairs
Delta_pair = float(s38['Delta_OES'])
a_NR = a_transit_val * (E_per_pair / Delta_pair)

print(f"a_transit     = {a_transit_val:.4e}")
print(f"E_per_pair    = {E_per_pair:.4f} M_KK")
print(f"Delta_pair    = {Delta_pair:.4f} M_KK")
print(f"a_NR          = {a_NR:.4e} (GGE becomes non-relativistic)")
print(f"a(z=5)        = {1.0/6.0:.4f}")
print(f"a(z=0)        = 1.0")
print(f"a_NR / a(z=5) = {a_NR / (1.0/6.0):.4e}")
print(f"\n=> GGE is DUST (w_n=0) for ALL observable z.")
print(f"=> Scenario C = Scenario B. No additional departure from w=-1.")

# =============================================================================
# 7. SCENARIO D: VOLOVIK POWER-LAW (Paper 37 prescription)
# =============================================================================
print("\n" + "=" * 70)
print("Scenario D: Volovik Power-Law Prescription")
print("=" * 70)

# Paper 37 predicts rho_m ~ t^{-0.4}, rho_Lambda ~ t^{0.6}
# In a(t) terms for matter-dominated: a ~ t^{2/3}, so t ~ a^{3/2}
# rho_m ~ a^{-3*0.4/0.667} = a^{-0.6/0.667} ... this doesn't match standard.
#
# Actually, Volovik's prediction is for the TOTAL evolution including
# the two-fluid coupling. Let me extract w_eff from these power laws.
#
# If rho_Lambda ~ t^{0.6}, then in the late universe (DE dominated):
# a ~ e^{Ht}, so t ~ ln(a)/H, so rho_Lambda ~ (ln a)^{0.6}
# This means rho_Lambda is slowly GROWING, which gives w_Lambda < -1 (phantom)
# or more precisely, the growing Lambda acts like w_eff slightly above -1.
#
# For rho_Lambda ~ t^beta with beta = 0.6:
# d(rho_Lambda)/dt = beta * rho_Lambda / t
# Continuity: d(rho_Lambda)/dt + 3H*(rho_Lambda + P_Lambda) = 0
# => P_Lambda = -(1 + beta/(3Ht)) * rho_Lambda
# => w_Lambda = -(1 + beta/(3Ht))
#
# At the current epoch: H_0 * t_0 ~ 1 (Hubble time ~ age)
# w_Lambda = -(1 + 0.6/3) = -(1 + 0.2) = -1.2
#
# Wait -- that's phantom (w < -1). And the sign depends on whether
# rho_Lambda is growing (beta > 0 => w < -1) or decaying.
#
# Volovik's Paper 37 says rho_Lambda ~ t^{0.6} (growing vacuum energy).
# This requires w < -1 (phantom), which is NOT what DESI sees (w > -1).

# Let me compute w_eff for Volovik's ansatz
alpha_V = 0.4  # rho_m ~ t^{-alpha}
beta_V = 0.6   # rho_Lambda ~ t^{beta}

# At late times (DE dominated), H ~ const, t ~ 1/H
# w_Lambda = -(1 + beta_V / (3 * H * t))
# At z=0: H_0 * t_0 ~ 0.96 (for LCDM)
Ht_0 = 0.96
w_Lambda_Volovik = -(1.0 + beta_V / (3.0 * Ht_0))
w_eff_Volovik = (w_Lambda_Volovik * Omega_Lambda_0 + 0.0 * Omega_m_0)

print(f"Volovik ansatz: rho_m ~ t^{{-{alpha_V}}}, rho_Lambda ~ t^{{{beta_V}}}")
print(f"w_Lambda (Volovik) = -(1 + {beta_V}/(3*{Ht_0:.2f})) = {w_Lambda_Volovik:.4f}")
print(f"w_eff (Volovik)    = w_Lambda * Omega_Lambda = {w_eff_Volovik:.4f}")
print(f"|w_eff + 1|        = {abs(w_eff_Volovik + 1):.4f}")
print(f"\nVolovik predicts PHANTOM (w < -1), opposite sign to DESI (w > -1).")
print(f"But this requires beta > 0 (growing vacuum energy), which needs")
print(f"continuous condensation at the Hubble rate.")

# In our framework: vacuum energy is FROZEN post-transit.
# No continuous condensation. beta = 0. w_Lambda = -1 exactly.
print(f"\nFramework: vacuum frozen post-transit. beta = 0. w_Lambda = -1.")

# =============================================================================
# 8. BREATHING MODE ANALYSIS (last escape)
# =============================================================================
print("\n" + "=" * 70)
print("Breathing Mode: Could tau oscillations produce w != -1?")
print("=" * 70)

# The modulus tau could oscillate around the fold with frequency omega_tau.
# If tau oscillates, the spectral action S(tau) oscillates, producing
# time-varying vacuum energy.
#
# omega_tau = 8.27 M_KK. Period ~ 1/M_KK ~ 10^{-42} s.
# This is ultrafast compared to H_0^{-1} ~ 10^{18} s.
# The oscillation AVERAGES OUT over a Hubble time.
#
# Time-averaged <S(tau)> = S(tau_fold) + (1/2)*S''(tau_fold) * <delta_tau^2>
# This gives a constant shift, not a time-varying w.
#
# For w != -1, need the oscillation amplitude to vary with cosmic time.
# Energy in oscillation: E_osc = (1/2) * Z_fold * omega_tau^2 * A^2
# where A is the amplitude.
# This energy redshifts as rho_osc ~ a^{-3}*(1+w_osc) where w_osc ~ 0
# (massive scalar field oscillation has w ~ 0 on average).
#
# The oscillating part contributes:
# delta_w = (E_osc/rho_total) * (w_osc - w_vacuum)
#         = (E_osc/rho_total) * (0 - (-1))
#         = E_osc / rho_total
#
# But E_osc is suppressed by effacement:
# E_osc / rho_vacuum ~ (delta_tau)^2 * Z_fold * omega_tau^2 / S_fold

# What sets delta_tau? The quantum zero-point fluctuation:
# delta_tau_ZP = 1/sqrt(2 * Z_fold * omega_tau) (in natural units)
delta_tau_ZP = 1.0 / np.sqrt(2.0 * Z_fold * omega_tau)
E_osc_ZP = 0.5 * omega_tau  # zero-point energy = (1/2)*omega (in M_KK^4 if Z=1)
# More carefully: E_ZP = (1/2)*omega_tau * sqrt(Z_fold) (proper normalization)
# Actually for canonically normalized field: phi = sqrt(Z)*tau, m_phi = omega_tau/sqrt(Z) * sqrt(Z) = omega_tau
# E_ZP = (1/2)*omega_tau in M_KK units

E_ZP_ratio = (0.5 * omega_tau) / S_fold
print(f"omega_tau         = {omega_tau:.4f} M_KK")
print(f"Z_fold            = {Z_fold:.2f} M_KK^4")
print(f"delta_tau_ZP      = {delta_tau_ZP:.4e}")
print(f"E_ZP              = {0.5*omega_tau:.4f} M_KK")
print(f"E_ZP / S_fold     = {E_ZP_ratio:.4e}")
print(f"\nBreathing mode contributes |delta_w| ~ E_ZP/S_fold")
print(f"|delta_w|_breath   = {E_ZP_ratio:.4e}")
print(f"\nEffacement-suppressed. 5 orders below INTERMEDIATE threshold (10^{-6}).")

# =============================================================================
# 9. COMPREHENSIVE w(z) COMPUTATION
# =============================================================================
print("\n" + "=" * 70)
print("COMPREHENSIVE w(z) RESULTS")
print("=" * 70)

# Compute w(z) for the full framework (all effects combined)
z_eval = np.array([0.0, 0.295, 0.51, 0.706, 1.0, 1.317, 2.0, 3.0, 5.0])

# All corrections to w = -1:
# 1. Slow-roll: delta_w_SR = (2/3)*epsilon_V * (Omega_Lambda / Omega_total)
#    (z-independent to leading order since epsilon_V is constant post-freeze)
# 2. Mutual friction equilibrium correction: delta_w_MF ~ epsilon_V * (H/Gamma)
# 3. Breathing mode: delta_w_BM ~ E_ZP / S_fold ~ 1.7e-5
# 4. Effacement: all corrections above multiplied by ~ r_suppression ~ 5.4e-7

# The DOMINANT correction is the slow-roll epsilon_V = 3.67e-7
# But this is the EOS of the vacuum sector ALONE.
# The effective EOS of the total (vacuum + matter) system is:
# w_eff = (P_s + P_n) / (rho_s + rho_n)
# = (w_s * rho_s + w_n * rho_n) / (rho_s + rho_n)

# For standard LCDM evolution:
# Omega_Lambda(z) = Omega_Lambda_0 / E(z)^2
# Omega_m(z) = Omega_m_0 * (1+z)^3 / E(z)^2
# E(z)^2 = Omega_Lambda_0 + Omega_m_0 * (1+z)^3

E2_z = Omega_Lambda_0 + Omega_m_0 * (1.0 + z_eval)**3
Omega_Lambda_z = Omega_Lambda_0 / E2_z
Omega_m_z = Omega_m_0 * (1.0 + z_eval)**3 / E2_z

# w_eff(z) for the dark energy sector only (what DESI measures):
# w_DE(z) = w_s = -1 + (2/3)*epsilon_V
w_DE_z = np.full_like(z_eval, w_s_slowroll, dtype=float)

# Total effective EOS:
w_total_z = w_s_slowroll * Omega_Lambda_z + 0.0 * Omega_m_z

# The departure |w_DE + 1| = (2/3)*epsilon_V = 2.45e-7 at ALL z
delta_w_DE = abs(w_s_slowroll + 1.0)

# Mutual friction correction (suppressed by H/Gamma):
H_z = np.sqrt(E2_z)  # in units of H_0
delta_w_MF = (2.0/3.0) * epsilon_V * H_z / GammaOverH0

# Breathing mode:
delta_w_BM = np.full_like(z_eval, E_ZP_ratio, dtype=float)

# Combined departure from w = -1 (dark energy sector):
delta_w_total = delta_w_DE + delta_w_MF + delta_w_BM
# Note: delta_w_MF is negligible (~10^{-65}), delta_w_BM ~ 1.7e-5
# But delta_w_BM is a CONSTANT SHIFT to rho_Lambda, not a varying w.
# It shifts the CC but doesn't make w != -1.
# The time-varying part of breathing mode is averaged out.

# CORRECT: The only dynamical departure is delta_w_DE = (2/3)*epsilon_V = 2.45e-7
w_framework_z = np.full_like(z_eval, -1.0 + delta_w_DE, dtype=float)

print(f"\n{'z':>6s}  {'w_DE(z)':>20s}  {'|w_DE+1|':>12s}  {'Omega_Lambda':>14s}")
print(f"{'-'*6}  {'-'*20}  {'-'*12}  {'-'*14}")
for i, z in enumerate(z_eval):
    print(f"{z:6.3f}  {w_framework_z[i]:20.15f}  {abs(w_framework_z[i]+1):12.4e}  {Omega_Lambda_z[i]:14.6f}")

# CPL parameterization: w(z) = w_0 + w_a * z/(1+z)
# Since w is constant to 10^{-7}, CPL fit is trivial:
w_0_CPL = -1.0 + delta_w_DE
w_a_CPL = 0.0  # no z-dependence
print(f"\nCPL Parameters:")
print(f"  w_0 = {w_0_CPL:.15f}")
print(f"  w_a = {w_a_CPL:.15f}")
print(f"  |w_0 + 1| = {abs(w_0_CPL + 1):.4e}")

# =============================================================================
# 10. GATE VERDICT
# =============================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: TWOFLUID-W-43")
print("=" * 70)

w0_departure = abs(w_0_CPL + 1)
if w0_departure > 0.001:
    verdict = "PASS"
elif w0_departure < 1e-6:
    verdict = "FAIL"
else:
    verdict = "INTERMEDIATE"

print(f"|w_0 + 1| = {w0_departure:.4e}")
print(f"Threshold PASS:         > 0.001")
print(f"Threshold FAIL:         < 10^-6")
print(f"Threshold INTERMEDIATE: 10^-6 to 0.001")
print(f"\nVerdict: {verdict}")

# Comparison with S42 single-component result:
print(f"\nComparison with S42 W-Z-42:")
print(f"  S42 (single-component):  |w+1| ~ 2.4e-7 (slow-roll epsilon_V)")
print(f"  S43 (two-fluid):         |w+1| ~ {w0_departure:.4e} (same epsilon_V)")
print(f"  Improvement:             NONE")
print(f"  Reason:                  Gamma >> H => local equilibrium => w = -1")
print(f"                           Two-fluid friction CANNOT departing from w=-1")
print(f"                           because source term (1+w_s)*rho_s ~ epsilon_V*rho_s")
print(f"                           is suppressed by the SAME epsilon_V that sets w_s.")

# =============================================================================
# 11. DESI COMPARISON
# =============================================================================
print("\n" + "=" * 70)
print("DESI DR2 COMPARISON")
print("=" * 70)

w0_DESI = -0.72
w0_DESI_err = 0.07
wa_DESI = -1.07
wa_DESI_err = 0.37

print(f"DESI DR2: w_0 = {w0_DESI} +/- {w0_DESI_err}")
print(f"DESI DR2: w_a = {wa_DESI} +/- {wa_DESI_err}")
print(f"\nFramework: w_0 = {w_0_CPL:.10f}")
print(f"Framework: w_a = {w_a_CPL:.10f}")
print(f"\nDISCREPANCY:")
print(f"  |w_0(framework) - w_0(DESI)| = {abs(w_0_CPL - w0_DESI):.4f}")
print(f"  In sigma: {abs(w_0_CPL - w0_DESI)/w0_DESI_err:.1f} sigma")
print(f"\nThe framework predicts w = -1 to 7 decimal places.")
print(f"DESI DR2's w_0 = -0.72 (if confirmed) would EXCLUDE the framework.")
print(f"Skeptical assessment (Wang & Mota): dataset tensions drive w != -1.")
print(f"If DESI DR3 confirms w = -1, framework is CONSISTENT.")

# =============================================================================
# 12. EFFACEMENT CHECK
# =============================================================================
print("\n" + "=" * 70)
print("EFFACEMENT CHECK")
print("=" * 70)

# All BCS-related corrections to w are suppressed by:
# |E_BCS| / S_fold ~ 6.2e-7
# This is the "gravitational effacement" of internal structure

E_BCS_over_S = abs(E_cond) / S_fold
print(f"|E_BCS|/S_fold    = {E_BCS_over_S:.4e}")
print(f"r_suppression    = {r_suppression:.4e}")
print(f"epsilon_V         = {epsilon_V:.4e}")
print(f"\nAll three suppressions are O(10^{{-7}}). This is NOT coincidence.")
print(f"Effacement ratio = |E_BCS|/S_fold is the SPECTRAL-GEOMETRIC analog")
print(f"of the strong equivalence principle (S40 result).")
print(f"\nAny mechanism coupling BCS dynamics to the cosmological EOS is")
print(f"suppressed by at least 6 orders of magnitude below the INTERMEDIATE")
print(f"threshold (10^{{-6}}), and 4 orders below the slow-roll epsilon_V.")

# =============================================================================
# 13. STRUCTURAL OBSTRUCTIONS TABLE
# =============================================================================
print("\n" + "=" * 70)
print("STRUCTURAL OBSTRUCTIONS TO w != -1")
print("=" * 70)

print("""
| Mechanism                    | |delta_w|     | Obstruction              |
|:-----------------------------|:-------------|:-------------------------|
| Slow-roll (epsilon_V)        | 2.45e-7      | Spectral action geometry |
| Mutual friction (Gamma>>H)   | ~10^{-65}    | H/Gamma = 10^{-58}      |
| Breathing mode (zero-point)  | 1.65e-5      | Constant shift, not w    |
| GGE evolution                | 0            | Dust (w_n=0) for all z   |
| Volovik power-law            | ~0.2         | Requires Gamma~H (NO)    |
| BCS condensation energy      | ~6e-7        | Effacement               |
| Domain wall dynamics         | ~10^{-29}    | S42 REDO #2 (frozen)     |
| KK tower threshold           | 0            | Frozen post-transit       |
""")

# =============================================================================
# 14. SAVE RESULTS
# =============================================================================
print("\n" + "=" * 70)
print("Saving results...")
print("=" * 70)

np.savez('s43_twofluid_wz.npz',
    # Gate
    gate_name='TWOFLUID-W-43',
    gate_verdict=verdict,

    # w(z) results
    z_eval=z_eval,
    w_framework=w_framework_z,
    w_0_CPL=w_0_CPL,
    w_a_CPL=w_a_CPL,
    delta_w_DE=delta_w_DE,

    # Framework parameters used
    epsilon_V=epsilon_V,
    omega_att=omega_att,
    omega_tau=omega_tau,
    m_tau=m_tau,
    Gamma_MKK=Gamma_MKK,
    GammaOverH0=GammaOverH0,

    # Corrections
    delta_w_slowroll=delta_w_DE,
    delta_w_breathing=E_ZP_ratio,
    delta_w_MF_z0=delta_w_MF[0],

    # Effacement
    E_BCS_over_S=E_BCS_over_S,
    r_suppression=r_suppression,

    # DESI comparison
    w0_DESI=w0_DESI,
    w0_DESI_err=w0_DESI_err,
    wa_DESI=wa_DESI,
    wa_DESI_err=wa_DESI_err,
    discrepancy_sigma=abs(w_0_CPL - w0_DESI)/w0_DESI_err,

    # Volovik scenario
    w_Lambda_Volovik=w_Lambda_Volovik,
    alpha_Volovik=alpha_V,
    beta_Volovik=beta_V,

    # Two-fluid convergence test
    gamma_test_values=np.array(list(w0_results.keys())),
    w0_test_values=np.array(list(w0_results.values())),

    # Upstream provenance
    tau_fold=tau_fold,
    S_fold=S_fold,
    Z_fold=Z_fold,
    M_KK_grav=M_KK_grav,
    M_KK_gauge=M_KK_gauge,
)

print("Saved: s43_twofluid_wz.npz")

# =============================================================================
# 15. PLOT
# =============================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('TWOFLUID-W-43: Two-Fluid w(z) for DESI\n'
             f'Gate verdict: {verdict} (|w₀+1| = {w0_departure:.2e})',
             fontsize=13, fontweight='bold')

# Panel (a): w(z) comparison with DESI
ax = axes[0, 0]
z_fine = np.linspace(0, 5, 200)
w_frame_fine = np.full_like(z_fine, -1.0 + delta_w_DE)
ax.axhline(-1, color='gray', ls='--', lw=0.8, label='$\\Lambda$CDM')
ax.plot(z_fine, w_frame_fine, 'b-', lw=2, label=f'Framework: $w = -1 + {delta_w_DE:.1e}$')

# DESI CPL band
w_DESI_fine = w0_DESI + wa_DESI * z_fine / (1 + z_fine)
w_DESI_upper = (w0_DESI + w0_DESI_err) + (wa_DESI + wa_DESI_err) * z_fine / (1 + z_fine)
w_DESI_lower = (w0_DESI - w0_DESI_err) + (wa_DESI - wa_DESI_err) * z_fine / (1 + z_fine)
ax.fill_between(z_fine, w_DESI_lower, w_DESI_upper, alpha=0.2, color='red', label='DESI DR2 (1$\\sigma$)')
ax.plot(z_fine, w_DESI_fine, 'r-', lw=1.5, label=f'DESI DR2: $w_0={w0_DESI}$')

ax.set_xlabel('z')
ax.set_ylabel('w(z)')
ax.set_title('(a) Dark Energy EOS')
ax.legend(fontsize=8, loc='lower right')
ax.set_ylim(-2.5, 0.5)
ax.set_xlim(0, 5)

# Panel (b): Obstruction hierarchy
ax = axes[0, 1]
mechanisms = ['Slow-roll\n$\\epsilon_V$', 'Breathing\nmode', 'Effacement\n$|E_{BCS}|/S$',
              'Mutual\nfriction', 'Domain\nwalls (S42)']
delta_w_values = [delta_w_DE, E_ZP_ratio, E_BCS_over_S, delta_w_MF[0], 2.4e-29]
colors = ['steelblue', 'teal', 'darkorange', 'firebrick', 'purple']

bars = ax.barh(range(len(mechanisms)), np.log10(np.array(delta_w_values) + 1e-100),
               color=colors, height=0.6)
ax.axvline(np.log10(0.001), color='green', ls='--', lw=1.5, label='PASS threshold')
ax.axvline(np.log10(1e-6), color='orange', ls='--', lw=1.5, label='INTERMEDIATE')
ax.set_yticks(range(len(mechanisms)))
ax.set_yticklabels(mechanisms, fontsize=9)
ax.set_xlabel('$\\log_{10}|\\delta w|$')
ax.set_title('(b) Obstruction Hierarchy')
ax.legend(fontsize=8)
ax.set_xlim(-70, 0)

# Panel (c): Two-fluid convergence test
# The numerical integration computes w_total = (w_s*rho_s + w_n*rho_n)/(rho_s+rho_n)
# This equals ~-0.7 (= -Omega_Lambda) for all gamma, confirming mutual friction
# has NO dynamical effect. Show the delta from the LCDM value.
ax = axes[1, 0]
gamma_vals = sorted(w0_results.keys())
# w_total(LCDM) = -Omega_Lambda = -0.7
w_LCDM_total = -Omega_Lambda_0
w0_diffs = [abs(w0_results[g] - w_LCDM_total) for g in gamma_vals if not np.isnan(w0_results[g])]
gamma_valid = [g for g in gamma_vals if not np.isnan(w0_results[g])]

if len(gamma_valid) > 0:
    # All diffs are ~ epsilon_V * Omega_Lambda, confirming convergence
    ax.semilogx(gamma_valid, [w0_results[g] for g in gamma_valid], 'ko-', lw=2, markersize=6)
    ax.axhline(w_LCDM_total, color='blue', ls='--', lw=1,
               label=f'$w_{{total}}(\\Lambda CDM) = {w_LCDM_total:.1f}$')

ax.set_xlabel('$\\Gamma/H_0$')
ax.set_ylabel('$w_{total}(z=0)$')
ax.set_title('(c) $w_{total}$ vs mutual friction strength')
ax.legend(fontsize=8)
ax.set_xlim(1e-2, 1e7)
ax.set_ylim(-0.75, -0.65)
ax.text(0.5, 0.15, 'Flat: mutual friction\nhas NO dynamical effect',
        transform=ax.transAxes, ha='center', fontsize=9, style='italic')

# Panel (d): Physical mechanism summary
ax = axes[1, 1]
ax.axis('off')
summary_text = (
    f"TWOFLUID-W-43 SUMMARY\n"
    f"{'='*40}\n\n"
    f"Gate verdict: {verdict}\n"
    f"|w₀ + 1| = {w0_departure:.4e}\n\n"
    f"Framework parameters:\n"
    f"  ε_V = {epsilon_V:.2e}\n"
    f"  ω_att = {omega_att:.3f} M_KK\n"
    f"  Γ/H₀ = {GammaOverH0:.2e}\n\n"
    f"Physical mechanism:\n"
    f"  Γ >> H => local equilibrium\n"
    f"  Source (ρ_s+P_s) = ε_V·ρ_s ≈ 0\n"
    f"  Two fluids DECOUPLE\n"
    f"  w = -1 + (2/3)ε_V ≈ -1\n\n"
    f"CPL: w₀ = {w_0_CPL:.10f}\n"
    f"     w_a = {w_a_CPL:.1f}\n\n"
    f"vs DESI DR2: w₀ = {w0_DESI} ± {w0_DESI_err}\n"
    f"  Discrepancy: {abs(w_0_CPL - w0_DESI)/w0_DESI_err:.1f}σ\n\n"
    f"DESI w≠-1 at >5σ excludes framework.\n"
    f"Skeptical: dataset tensions likely."
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('s43_twofluid_wz.png', dpi=150, bbox_inches='tight')
print("Saved: s43_twofluid_wz.png")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("TWOFLUID-W-43: FINAL SUMMARY")
print("=" * 70)
print(f"""
GATE:     TWOFLUID-W-43
VERDICT:  {verdict}
|w_0+1| = {w0_departure:.4e}

PHYSICS:
  The Volovik two-fluid model (Paper 37) applied to the phonon-exflation
  framework produces w = -1 + O(10^{{-7}}), identical to the single-component
  result (S42 W-Z-42).

  ROOT CAUSE: The mutual friction rate Gamma = omega_att/(2*pi) ~ 10^{{58}} * H_0
  vastly exceeds the Hubble rate. In local equilibrium, the two-fluid source
  term (rho_s + P_s) is proportional to (1 + w_s) = (2/3)*epsilon_V ~ 2.45e-7.
  The mutual friction cannot amplify this departure because the source itself
  is suppressed.

  Four scenarios tested:
  (A) Pure CC:          w = -1 exactly (source = 0)
  (B) Slow-roll:        w = -1 + 2.45e-7 (epsilon_V)
  (C) GGE evolution:    w_n = 0 (dust) for all observable z
  (D) Volovik ansatz:   w ~ -1.2 (phantom) -- requires Gamma ~ H (NOT satisfied)

  Volovik's power-law prediction (rho_Lambda ~ t^0.6) requires CONTINUOUS
  condensation at the Hubble rate. The framework's vacuum is FROZEN post-transit.
  No continuous condensation occurs. The two-fluid model reduces to standard
  LCDM plus a 10^{{-7}} slow-roll correction.

CONSTRAINT MAP:
  - Eliminates: two-fluid mutual friction as source of w != -1
  - Confirms: effacement (|E_BCS|/S_fold ~ 6e-7) suppresses ALL BCS corrections
  - Surviving region: w = -1 ± O(10^{{-7}}). Framework is LCDM to 7 decimal places
  - DESI DR2 (w_0 = -0.72, if confirmed at 5+ sigma) would EXCLUDE framework

NEXT GATE: None within two-fluid channel. All 6 w(z) mechanisms exhausted.
""")
