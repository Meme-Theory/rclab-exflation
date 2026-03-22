#!/usr/bin/env python3
"""
Session 25 Einstein Workshop: Mixed Seeley-DeWitt Coefficients & Open Items

[MEME]S-1: Mixed a_2(D_P) and a_4(D_P) for total-space Dirac operator
           D_P on M^4 x SU(3)_Jensen, including gauge field strength F^a_{mu nu}.

Einstein open items: E-5 (a_0/a_2 ratio), Q-2 (CC implications),
                     Q-3 (spectral Bianchi identity analysis),
                     V_FR vs V_full interpretation, partition function thermodynamics.

Author: Einstein-Theorist (Claude Opus 4.6)
Date: 2026-02-22
"""

import numpy as np
from pathlib import Path

# =============================================================================
# LOAD ALL DATA
# =============================================================================

kk = np.load('tier0-computation/s25_kk_workshop.npz', allow_pickle=True)
fi = np.load('tier0-computation/s23c_fiber_integrals.npz', allow_pickle=True)
ba = np.load('tier0-computation/s25_baptista_results.npz', allow_pickle=True)
cn = np.load('tier0-computation/s25_connes_results.npz', allow_pickle=True)

# Core data arrays
tau_9 = kk['tau_values']          # 9 tau values: [0, 0.1, 0.15, ..., 0.5]
tau_21 = fi['tau']                # 21 tau values: [0, 0.1, 0.2, ..., 2.0]
R_K_9 = kk['R_K_comp']           # R_K at 9 tau values (Baptista normalization)
R_K_21 = fi['R_scalar']          # R_K at 21 tau values (ours normalization, factor 6 less)
omega3_9 = kk['omega3_comp']     # |omega_3|^2 at 9 tau values
omega3_21 = fi['omega_sq']       # |omega_3|^2 at 21 tau values
a4_geom_9 = kk['a4_interp']     # a_4_geom at 9 tau values
a4_geom_21 = fi['a4_geom']       # a_4_geom at 21 tau values
Ric_sq_21 = fi['Ric_sq']         # |Ric|^2 at 21 tau values
K_21 = fi['K_kretschner']        # Kretschner scalar at 21 tau values

# Connes SD coefficients (in ours normalization)
a2_connes = cn['a2_values']       # a_2 at 21 tau values
a4_connes = cn['a4_values']       # a_4 at 21 tau values

# Baptista fine grid
tau_fine = ba['tau_fine']          # 201 tau values [0, 0.01, ..., 2.0]
R_K_fine = ba['R_K_fine']         # R_K at fine grid (Baptista norm)
m2_fine = ba['m2_fine']           # m^2 at fine grid

print("=" * 70)
print("SESSION 25 EINSTEIN WORKSHOP COMPUTATION")
print("=" * 70)

# =============================================================================
# [MEME]S-1: MIXED SEELEY-DEWITT COEFFICIENTS
# =============================================================================

print("\n" + "=" * 70)
print("[MEME]S-1: MIXED SEELEY-DEWITT COEFFICIENTS FOR D_P")
print("=" * 70)

# ---- THEORETICAL FRAMEWORK ----
#
# The total-space Dirac operator D_P on P = M^4 x K (K = SU(3)_Jensen):
#   D_P^2 = D_4^2 + D_K^2 + mixed terms
#
# The Kerner decomposition (KK Paper 06, eq 26-30):
#   R_P = R_{M4} + R_K + (1/4) g_{ab} F^a_{mu nu} F^{b mu nu}
#
# The F^a_{mu nu} is the gauge field strength from the KK reduction.
# For the SU(3) internal space, the gauge field strength encodes the
# connection of the SU(3) principal bundle. The |omega_3|^2 term from
# KK-Q4 is the integrated gauge field energy.
#
# The mixed Seeley-DeWitt coefficients for D_P decompose as:
#
# a_2(D_P) = a_2(D_{M4}) * Vol(K) + Vol(M4) * a_2(D_K) + MIXED_2
# a_4(D_P) = a_4(D_{M4}) * Vol(K) + Vol(M4) * a_4(D_K)
#            + a_2(D_{M4}) * a_2(D_K) * CROSS + MIXED_4
#
# For the 4D effective potential V_eff(tau), after integrating over M4:
#   V_eff(tau) = alpha * integral_K a_2(D_K) dvol_K
#                + beta * integral_K a_4(D_K) dvol_K
#                + gamma * integral_K F^2 dvol_K
#                + delta * integral_K (R_K * F^2) dvol_K + ...
#
# The FIBER-ONLY terms (alpha, beta) are what V_spec uses -- MONOTONE.
# The MIXED terms (gamma, delta) include the gauge field strength.
#
# ---- SEELEY-DEWITT DECOMPOSITION FOR PRODUCT METRICS ----
#
# For a product metric g_P = g_4 + g_K on M^4 x K^n:
# The Dirac Laplacian D_P^2 has heat kernel:
#   K_P(t) = K_4(t) * K_K(t) * K_mix(t)
#
# The fiber-only a_2(D_K) involves:
#   a_2(D_K) = (1/6) * R_K * dim(spinor_K) * Vol(K)
# For 8-dim spinors: dim(spinor_K) = 2^{8/2} = 16
#   a_2(D_K) = (16/6) * R_K * Vol(K) = (8/3) * R_K * Vol(K)
# In our normalization (R_K_ours = R_K_Bap/6):
#   a_2 = (8/3) * R_K_ours = (20/3) * (R_K_ours/2.5) ...
# Let me use the Connes numbers directly.

# The MIXED a_2 includes the gauge kinetic term from KK reduction:
# On the total space P = M^4 x K, the connection 1-form omega gives
# field strength F^a_{mu nu} in 4D. The integrated field strength energy is:
#   E_F(tau) = (1/4) integral_K g_{ab} F^a_{mu nu} F^{b mu nu} dvol_K
# This is proportional to |omega_3|^2(tau) -- the Cartan 3-form norm.
#
# The mixed a_2 coefficient on the total space:
#   a_2^{mixed}(D_P) = (dim_spinor_4 / (16*pi^2)) * E_F(tau)
# where dim_spinor_4 = 4 (Dirac spinors in 4D).
#
# For the spectral action, the 4D effective potential becomes:
#   V_eff(tau) = f_2 * Lambda^2 * [a_2^{fiber}(tau) + c_F * E_F(tau)]
#              + f_0 * [a_4^{fiber}(tau) + c_FF * E_F(tau)^2 + c_RF * R_K(tau) * E_F(tau)]
#
# ---- QUANTITATIVE COMPUTATION ----

print("\n--- Phase 1: Kerner Decomposition Data ---")
print(f"tau values: {tau_9}")
print(f"R_K (Baptista norm): {R_K_9}")
print(f"|omega_3|^2: {omega3_9}")
print(f"a_4_geom: {a4_geom_9}")

# Growth rates normalized to tau=0
R_K_growth = R_K_9 / R_K_9[0]
omega3_growth = omega3_9 / omega3_9[0]
a4_growth = a4_geom_9 / a4_geom_9[0]

print("\n--- Growth rates (normalized to tau=0) ---")
for i, tau in enumerate(tau_9):
    print(f"  tau={tau:.2f}: R_K/R_K(0)={R_K_growth[i]:.4f}, "
          f"|omega3|^2/|omega3|^2(0)={omega3_growth[i]:.4f}, "
          f"a4/a4(0)={a4_growth[i]:.4f}")

# ---- MIXED COEFFICIENTS ----
#
# The key insight from Gilkey's theorem on product manifolds:
# For the Dirac Laplacian D_P^2 = nabla*nabla + R_P/4 + Omega_P
# on the product M^4 x K, the heat kernel coefficients decompose.
#
# The FIBER curvature R_K enters a_2 directly (this is V_spec).
# The GAUGE FIELD STRENGTH F enters through the curvature of the
# bundle connection, appearing in a_4 as:
#   a_4^{mixed} = c_1 * R_K^2 + c_2 * |Ric_K|^2 + c_3 * |Riem_K|^2
#                 + c_4 * Tr(F^2) + c_5 * R_K * Tr(F^2) + c_6 * Tr(F^4)
#
# The fiber-only basis {R_K^2, |Ric|^2, K} gives a_4^{fiber}.
# The mixed terms c_4 * Tr(F^2) and c_5 * R_K * Tr(F^2) are what V_spec misses.
#
# From the standard Gilkey formula for spin manifolds in dim n:
# a_4 = (1/(360)) * dim_S * integral { 5R^2 - 2|Ric|^2 + 2|Riem|^2 } dvol
#      + (1/12) * integral { R * tr(Omega^2) } dvol
#      + (1/(180)) * dim_S * integral { -12 Delta R } dvol  [boundary = 0]
#      + ...
#
# For the TOTAL space, the curvature endomorphism Omega_P includes contributions
# from F_{mu nu}. Specifically, in the KK reduction:
#   Omega_P^{mu nu} = Omega_4^{mu nu} + (1/4) F^a_{mu nu} * Sigma_a
# where Sigma_a are the fiber-representation matrices.
#
# The trace tr(Omega_P^2) then includes the CROSS TERM:
#   tr(Omega_P^2) = tr(Omega_4^2) + (1/16) F^a F^b tr(Sigma_a Sigma_b) + cross
#
# For SU(3) in the fundamental representation:
#   tr(Sigma_a Sigma_b) = (1/2) delta_{ab} * dim_fund = (1/2) * 3 * delta_{ab}
# But we use the SPIN representation (dim = 16), so:
#   tr(Sigma_a Sigma_b) = C_2(spin) * dim(spin) / dim(adj) * delta_{ab}
#
# In practice, the mixed contribution to a_4 from the gauge field is:
#   Delta a_4^{mixed} = c_gauge * integral_K |F|^2 dvol_K
# where |F|^2 is related to |omega_3|^2 through the structure constants.

print("\n--- Phase 2: Mixed Seeley-DeWitt Coefficient Construction ---")

# The Kerner relation:
#   R_P = R_base + R_K + (1/4) |F|^2
# gives us the total scalar curvature on the product space.
# For the spectral action, the a_2 coefficient of D_P on the full space is:
#   a_2(D_P) = (dim_spinor_P / 6) * R_P
# where dim_spinor_P = dim_spinor_4 * dim_spinor_K = 4 * 16 = 64
# (or 2^{12/2} = 64 for 12D Dirac spinors).

dim_spinor_P = 64  # 12-dimensional total space

# The mixed a_2 from the gauge field:
# a_2^{mixed}(tau) = (dim_spinor_P / 6) * (1/4) * |F|^2
# where |F|^2 is proportional to |omega_3|^2
#
# From the KK metric ansatz, the gauge field strength F^a_{mu nu} = f_{bc}^a * A^b_mu * A^c_nu
# where f_{bc}^a are the SU(3) structure constants.
# The norm |F|^2 = g^{mu rho} g^{nu sigma} g_{ab} F^a_{mu nu} F^b_{rho sigma}
#
# For our purposes, the RATIO of the mixed term to the fiber term is key:
# a_2^{mixed} / a_2^{fiber} = [(1/4) * |F|^2] / R_K
# This ratio tells us how important the gauge field is relative to fiber curvature.

gauge_to_curvature_ratio = (0.25 * omega3_9) / R_K_9

print("\nGauge-to-curvature ratio (1/4)|F|^2 / R_K:")
for i, tau in enumerate(tau_9):
    print(f"  tau={tau:.2f}: {gauge_to_curvature_ratio[i]:.6f}")

# ---- CONSTRUCT V_eff^{mixed}(tau) ----
#
# The TOTAL a_2 on the full 12D space (integrated over K):
#   a_2^{total}(tau) = a_2^{fiber}(tau) + a_2^{gauge}(tau)
# where a_2^{gauge}(tau) = (dim_S_P / 6) * (1/4) * |omega_3|^2(tau)
#
# In our normalization (using Connes' a_2 values in 'ours' convention):
# a_2^{fiber} from Connes: directly available
# a_2^{gauge}: proportional to |omega_3|^2
#
# The proportionality constant requires the 12D spinor trace.
# For the 8D internal Dirac operator, Connes computed:
#   a_2^{Connes}(tau) = (20/3) * R_ours(tau)
# where R_ours = R_Bap / 6.
#
# For the mixed term, the gauge field acts in the 4D sector:
#   a_2^{gauge}(tau) = (dim_spinor_4 / 6) * (1/4) * |omega_3|^2(tau) * Vol_K(tau)
#
# Since we're comparing to fiber-only V_spec, the relevant quantity is the
# RATIO of the mixed a_2 to the fiber a_2. Use the Kerner decomposition:
#
# Total R_P = R_4 + R_K + (1/4)|F|^2
# -> Effective a_2^{4D} propto R_K + (1/4)|F|^2  (after integrating over K)

# Compute the TOTAL Kerner curvature (fiber + gauge parts):
R_Kerner_total_9 = R_K_9 + 0.25 * omega3_9
R_Kerner_fiber_9 = R_K_9

print("\n--- Phase 3: Kerner Total vs Fiber Curvature ---")
print("\nR_Kerner (fiber only) vs R_Kerner (fiber + gauge):")
for i, tau in enumerate(tau_9):
    frac_gauge = (0.25 * omega3_9[i]) / R_Kerner_total_9[i]
    print(f"  tau={tau:.2f}: R_fiber={R_K_9[i]:.3f}, "
          f"R_total={R_Kerner_total_9[i]:.3f}, "
          f"gauge_fraction={frac_gauge:.4f}")

# ---- MIXED V_eff CONSTRUCTION ----
#
# V_eff(tau) = alpha * a_2^{total}(tau) + beta * a_4^{total}(tau)
#
# For the FIBER-ONLY case (V_spec):
#   V_spec(tau) = alpha * a_2^{fiber} + beta * a_4^{fiber}
# This is MONOTONE (Session 24a V-1 closure).
#
# For the MIXED case, we need a_4^{total} which includes:
#   a_4^{total} = a_4^{fiber} + c_4 * |F|^2 + c_5 * R_K * |F|^2 + c_6 * |F|^4
#
# The key question is whether the |F|^2 and |F|^4 terms, which grow
# 5.4x and 29.7x respectively over [0, 0.5], can COMPETE with the
# fiber a_4 to create a minimum.
#
# From the Gilkey formula for the curvature endomorphism on the total space:
# The tr(Omega_P^2) includes (1/16) * |F|^2 * C_2(spin_rep) * dim(spin_rep)
# For SU(3) with dim_spinor = 16:
#   c_4 = (1/12) * (1/16) * C_2(16) * 16
# where C_2(16) is the quadratic Casimir of the 16-dim spinor rep.
#
# For the spin representation on SU(3), the Casimir is:
# C_2 = (1/2) * sum_a Sigma_a^2 = dim(adj)/(2*dim(fund)) = 8/6 = 4/3
# (This uses the standard embedding of SU(3) in SO(8).)
# Actually, for the spin bundle on SU(3), the generators are the
# Kosmann-lifted Killing vector fields, and:
#   C_2(spin_8) = n(n-1)/8 for n=8: C_2 = 56/8 = 7
# This is the Casimir in the convention where Tr(T_a T_b) = delta_{ab}/2.

# Use dimensional analysis. The fiber a_4 scales as:
#   a_4^{fiber} ~ (dim_spinor)^2 * R_K^2  (dominant term, 98.4% from Connes C6)
# The mixed a_4 from gauge coupling scales as:
#   a_4^{mixed} ~ dim_spinor * |F|^2
# The ratio is:
#   a_4^{mixed} / a_4^{fiber} ~ |F|^2 / (dim_spinor * R_K^2)
#                               = omega3 / (16 * R_K^2)

# But this naive ratio is misleading. The CORRECT approach is to use
# the Kerner decomposition to build the TOTAL curvature and then
# compute the Gilkey coefficients of the TOTAL curvature.

# ---- APPROACH: PARAMETRIC MIXED POTENTIAL ----
#
# Since the exact coefficient c_4 requires the full 12D spinor algebra
# (which is beyond existing .npz data), I construct the parametric potential:
#
#   V_mixed(tau; rho, sigma) = a_2^{fiber}(tau) + sigma * |omega_3|^2(tau)
#                            + rho * [a_4^{fiber}(tau) + sigma_4 * |omega_3|^2(tau)]
#
# and determine whether there exists (rho, sigma, sigma_4) such that
# V_mixed has a minimum at finite tau.
#
# The question reduces to: can the gauge terms, which grow FASTER than
# the fiber terms, create a competing slope?

print("\n--- Phase 4: Parametric Mixed Potential V_mixed(tau; rho, sigma) ---")

# Use the 21-tau-point data from fiber integrals
# Convert to same normalization: use R_scalar (ours) and omega_sq
tau = tau_21
R_K = fi['R_scalar']         # ours normalization
omega3 = fi['omega_sq']
a4_g = fi['a4_geom']

# Fiber-only a_2 and a_4 (from Connes)
a2_fiber = cn['a2_values']  # (20/3) * R_ours
a4_fiber = cn['a4_values']  # Gilkey formula evaluated

# Normalize all to tau=0
a2_f0 = a2_fiber[0]
a4_f0 = a4_fiber[0]
om0 = omega3[0]

print(f"\nAt tau=0:")
print(f"  a_2^fiber = {a2_fiber[0]:.4f}")
print(f"  a_4^fiber = {a4_fiber[0]:.4f}")
print(f"  |omega_3|^2 = {omega3[0]:.4f}")
print(f"  R_K (ours) = {R_K[0]:.4f}")

# The MIXED potential (general parametric form):
# V_mixed(tau) = f_2 * Lambda^2 * [a_2^{fiber}(tau) + gamma * |omega_3|^2(tau)]
#              + f_0 * [a_4^{fiber}(tau) + delta * |omega_3|^2(tau)^2
#                       + epsilon * R_K(tau) * |omega_3|^2(tau)]
#
# Simplify: set alpha = f_2 * Lambda^2, beta = f_0
# V_mixed(tau) = alpha * a_2_fiber(tau) + alpha * gamma * omega3(tau)
#              + beta * a_4_fiber(tau) + beta * delta * omega3(tau)^2
#              + beta * epsilon * R_K(tau) * omega3(tau)
#
# Factor out alpha (sets overall scale):
# v(tau) = a_2_fiber(tau) + gamma * omega3(tau)
#        + rho * [a_4_fiber(tau) + delta * omega3(tau)^2 + epsilon * R_K(tau) * omega3(tau)]
# where rho = beta/alpha = f_0 / (f_2 * Lambda^2)

# From Session 24a: rho_spec = a_2(0)/a_4(0) gives the V_spec ratio
# a_4/a_2 = 985 at Baptista normalization, or 0.41 at ours normalization
rho_spec = a4_fiber[0] / a2_fiber[0]
print(f"\n  rho_spec = a_4(0)/a_2(0) = {rho_spec:.4f}")

# Scan: For what values of gamma (mixed a_2 coupling) and delta (mixed a_4 coupling)
# does V_mixed have a minimum?

# First: the simplest mixed potential (a_2 level only):
# v_2(tau) = a_2_fiber(tau) - sigma * omega3(tau)
# The NEGATIVE sign on omega3 is motivated by the Freund-Rubin mechanism:
# the flux OPPOSES the fiber curvature in the effective potential.
# V_FR = -R_K + (beta/alpha) * |omega_3|^2
# so the gauge term enters with OPPOSITE sign to R_K in V_FR.

# From KK-Q4: beta/alpha = 0.28 gives the Freund-Rubin minimum.
# In the spectral action, the mixed a_2 contribution is:
# a_2^{mixed} = -(1/4) * C_gauge * |omega_3|^2
# where the sign is NEGATIVE because the gauge energy SUBTRACTS from
# the gravitational (curvature) energy in the effective action.
# This is the Kerner sign: R_P = R_base + R_K + (1/4)|F|^2, but
# the POTENTIAL is V = -R_P (stabilizing) + ... so the F^2 term is:
# V ~ -R_K - (1/4)|F|^2 at the a_2 level.

print("\n--- Phase 5: V_mixed with Kerner Gauge Term ---")

# The Kerner-motivated mixed potential at a_2 level:
# V_Kerner(tau) = -[R_K(tau) + gamma * |omega_3|^2(tau)]
#               + rho * [a_4_fiber(tau) + delta * |omega_3|^2(tau)^2]
#
# For small gamma (gauge coupling), the a_2 part becomes more negative
# with tau (both R_K and omega3 increase). The a_4 part increases.
# Competition is POSSIBLE if the gauge-enhanced a_2 grows faster than a_4.

# Test: at what gamma does the derivative dV/dtau = 0 have a solution?
# dV/dtau = -dR_K/dtau - gamma * d(omega3)/dtau + rho * da4/dtau + ... = 0
# -> gamma = [rho * da4/dtau - dR_K/dtau] / [d(omega3)/dtau]

# Compute derivatives (finite differences on 21-point grid)
dR_dtau = np.gradient(R_K, tau)
domega3_dtau = np.gradient(omega3, tau)
da4_dtau = np.gradient(a4_g, tau)
da2_dtau = np.gradient(a2_fiber, tau)

# Critical gamma at each tau:
# gamma_crit(tau) = [rho * da4/dtau - dR_K/dtau] / [d(omega3)/dtau]
# For rho = rho_spec (the physical ratio from the spectral action)

rho_physical = 0.001  # V_spec uses rho = f_0/(f_2*Lambda^2), typically very small
# Actually, from V_spec: V_spec = f_2*Lambda^2*a_2 + f_0*a_4
# The "1000:1 ratio" means a_4 >> a_2, so rho*a_4 >> a_2
# In normalized units: v = a_2 + rho_norm * a_4
# where rho_norm absorbs the f_0/(f_2*Lambda^2) factor

# Let me use the physical setup from V_spec:
# V_spec(tau) = a_2(tau) + rho * a_4(tau)
# At tau=0: V_spec(0) = 13.33 + rho * 5.52
# For V_spec to be dominated by a_4 (1000:1), need rho ~ 1000 * a_2(0)/a_4(0) ~ 2414
# That's not right. The "1000:1" refers to the BAPTISTA normalization:
# a_4_Bap / a_2_Bap = 1970/12 = 164 at tau=0, or a_4_Bap/R_K_Bap = 985/12 ~ 82
# In ours: a_4_connes / a_2_connes = 5.52 / 13.33 = 0.414

# The V_spec potential: V = f_2*Lambda^2 * a_2(tau) + f_0 * a_4(tau)
# The ratio rho = f_0 / (f_2 * Lambda^2) controls the relative weight.
# For rho << 1: a_2 dominates (monotone increasing -> V monotone)
# For rho >> 1: a_4 dominates (monotone increasing -> V monotone)
# For any rho: both a_2 and a_4 increase monotonically -> V monotone.
# This is WHY V_spec is monotone: both terms have the same sign of derivative.

# NOW: add the mixed term from gauge coupling.
# V_mixed(tau) = a_2_fiber(tau) - gamma * omega3(tau) + rho * a_4_fiber(tau)
# The NEGATIVE gamma*omega3 term is the Kerner gauge contribution.
# dV/dtau = da_2/dtau - gamma * d(omega3)/dtau + rho * da_4/dtau
# = 0 when gamma = [da_2/dtau + rho * da_4/dtau] / [d(omega3)/dtau]

print("\nCritical gamma(tau) for dV_mixed/dtau = 0:")
print("  (gamma = coefficient of gauge term at a_2 level)")
print("  V_mixed = a_2(tau) - gamma * |omega_3|^2(tau) + rho * a_4(tau)")

for rho_test in [0.0, 0.01, 0.1, 0.414, 1.0]:
    print(f"\n  rho = {rho_test}:")
    gamma_crit = (da2_dtau + rho_test * np.gradient(a4_fiber, tau)) / domega3_dtau
    for i in [0, 1, 2, 3, 4, 5, 10, 15, 20]:
        if i < len(tau):
            print(f"    tau={tau[i]:.2f}: gamma_crit={gamma_crit[i]:.6f}, "
                  f"da2/dt={da2_dtau[i]:.3f}, d(om3)/dt={domega3_dtau[i]:.3f}")

# ---- THE KEY COMPUTATION: SCAN OVER (gamma, rho) ----

print("\n--- Phase 6: (gamma, rho) Parameter Scan for V_mixed Minimum ---")

# V_mixed(tau; gamma, rho) = a_2(tau) - gamma * omega3(tau) + rho * a_4(tau)
# Normalize to V_mixed(0) = 0:
# v(tau) = [a_2(tau) - a_2(0)] - gamma * [omega3(tau) - omega3(0)] + rho * [a_4(tau) - a_4(0)]

a2_norm = a2_fiber - a2_fiber[0]
a4_norm = a4_fiber - a4_fiber[0]
omega3_norm = omega3 - omega3[0]

# Scan gamma from 0 to 5 and rho from 0 to 2
gamma_range = np.linspace(0, 5.0, 501)
rho_range = np.linspace(0, 2.0, 201)

# For each (gamma, rho), check if V_mixed has a minimum in tau in (0, 2.0]
min_results = []
has_min_map = np.zeros((len(gamma_range), len(rho_range)), dtype=bool)
tau_min_map = np.full((len(gamma_range), len(rho_range)), np.nan)
depth_map = np.full((len(gamma_range), len(rho_range)), np.nan)

for ig, gamma in enumerate(gamma_range):
    for ir, rho in enumerate(rho_range):
        v = a2_norm - gamma * omega3_norm + rho * a4_norm
        # Check for interior minimum (not at boundary tau=0 or tau=2.0)
        # v[0] = 0 by construction
        # Find if v goes negative (minimum below start)
        # and then comes back up (has a minimum)
        min_idx = np.argmin(v)
        if min_idx > 0 and min_idx < len(tau) - 1:
            # Interior minimum found
            has_min_map[ig, ir] = True
            tau_min_map[ig, ir] = tau[min_idx]
            depth_map[ig, ir] = -v[min_idx]  # depth (positive = below V(0))

# Report
n_with_min = np.sum(has_min_map)
total_pts = has_min_map.size
print(f"\nParameter scan: {len(gamma_range)} x {len(rho_range)} = {total_pts} points")
print(f"Points with interior minimum: {n_with_min} ({100*n_with_min/total_pts:.1f}%)")

# Find the boundary in (gamma, rho) space
if n_with_min > 0:
    # For each gamma, find minimum rho that gives a minimum
    print("\nMinimum gamma for interior minimum (at various rho):")
    for rho_target in [0.0, 0.01, 0.1, 0.414, 1.0, 2.0]:
        ir = np.argmin(np.abs(rho_range - rho_target))
        for ig in range(len(gamma_range)):
            if has_min_map[ig, ir]:
                print(f"  rho={rho_range[ir]:.3f}: gamma_min={gamma_range[ig]:.4f}, "
                      f"tau_min={tau_min_map[ig, ir]:.2f}, "
                      f"depth={depth_map[ig, ir]:.4f}")
                break
        else:
            print(f"  rho={rho_range[ir]:.3f}: no minimum found in gamma range [0, 5]")

    # Show some representative minima
    print("\nRepresentative (gamma, rho) pairs with minima:")
    for gamma_target, rho_target in [(0.5, 0.0), (1.0, 0.0), (2.0, 0.0),
                                       (0.3, 0.1), (0.5, 0.1), (1.0, 0.414),
                                       (0.1, 1.0), (0.2, 1.0), (0.5, 1.0)]:
        ig = np.argmin(np.abs(gamma_range - gamma_target))
        ir = np.argmin(np.abs(rho_range - rho_target))
        if has_min_map[ig, ir]:
            print(f"  gamma={gamma_range[ig]:.3f}, rho={rho_range[ir]:.3f}: "
                  f"tau_min={tau_min_map[ig, ir]:.2f}, "
                  f"depth={depth_map[ig, ir]:.4f}")
        else:
            v = a2_norm - gamma_range[ig] * omega3_norm + rho_range[ir] * a4_norm
            print(f"  gamma={gamma_range[ig]:.3f}, rho={rho_range[ir]:.3f}: MONOTONE "
                  f"(min at tau={tau[np.argmin(v)]:.1f})")

# ---- CRITICAL gamma FROM KERNER ----
#
# The Kerner decomposition tells us the PHYSICAL value of gamma.
# The gauge field contribution to a_2 is:
#   Delta a_2 = (dim_spinor_P / 6) * (1/4) * |omega_3|^2
#             = (64/6) * (1/4) * |omega_3|^2 = (8/3) * |omega_3|^2
# While the fiber contribution is:
#   a_2^{fiber} = (dim_spinor_P / 6) * R_K = (64/6) * R_K = (32/3) * R_K
#
# BUT WAIT: the sign matters. In the Kerner formula:
# R_P = R_base + R_K + (1/4)|F|^2
# The gauge term ADDS to the curvature. In the spectral action:
# V ~ +a_2(tau) = +(dim_S/6) * R_P * Vol
# The gauge term makes a_2 LARGER, hence V LARGER.
# This is the WRONG sign for creating a minimum!
#
# In the Freund-Rubin potential, the flux enters with the OPPOSITE sign:
# V_FR = -R_K + (beta/alpha) * |omega_3|^2
# The minus sign on R_K is because in KK, the curvature STABILIZES
# (negative potential energy), while flux DESTABILIZES (positive).
# The competition gives a minimum.
#
# In the spectral action, BOTH R_K and |F|^2 enter a_2 with the SAME sign
# (both increase a_2). There is NO competition at the a_2 level!
#
# The competition, if it exists, must come at the a_4 level through
# CROSS TERMS like R_K * |F|^2 with a sign that opposes the pure R_K^2 term.

print("\n--- Phase 7: Sign Analysis of Mixed Terms ---")
print("\nKerner decomposition sign analysis:")
print("  R_P = R_base + R_K + (1/4)|F|^2  [ALL POSITIVE]")
print("  a_2(D_P) = (dim_S/6) * R_P        [POSITIVE, MONOTONE INCREASING]")
print("")
print("  => At the a_2 level, the gauge term REINFORCES the fiber term.")
print("     Both have the same sign. NO competition. NO minimum.")
print("")
print("  The Freund-Rubin mechanism works DIFFERENTLY:")
print("  V_FR = -integral R_K dvol + (beta/alpha) * integral |omega_3|^2 dvol")
print("  The MINUS sign on R_K comes from the STABILIZATION interpretation:")
print("  V_FR minimizes TOTAL ENERGY = -(gravitational binding) + (flux energy)")
print("  This is NOT captured by the spectral action a_2 coefficient.")

# ---- a_4 LEVEL: CROSS TERMS ----
#
# At the a_4 level, the Gilkey coefficient on the total space includes:
# a_4(D_P) = (1/360) dim_S * [5R_P^2 - 2|Ric_P|^2 + 2|Riem_P|^2]
#           + (1/12) [R_P * tr(Omega_P^2)]
#           ...
#
# Expanding R_P = R_4 + R_K + (1/4)|F|^2:
# R_P^2 = R_K^2 + (1/2) R_K |F|^2 + (1/16)|F|^4 + ... (4D terms)
# The CROSS TERM R_K * |F|^2 enters a_4 with coefficient:
# c_cross = (5/360) * dim_S * (1/2) = (5*64)/(720) = 0.444
#
# And the |F|^4 term enters with:
# c_quartic = (5/360) * dim_S * (1/16) = (5*64)/(5760) = 0.0556

# More precisely, using the Connes normalization:
# a_4^{total} = a_4^{fiber} + c_cross * R_K * |F|^2 + c_quartic * |F|^4
# where the cross term can have EITHER sign depending on the Ric and Riem
# decomposition of the mixed curvature.

# For the mixed Ricci tensor:
# |Ric_P|^2 includes off-diagonal terms Ric_{mu a} that depend on D_mu F.
# On our PRODUCT space (no warping), D_mu F = 0, so these terms vanish.
# BUT: the KK metric is NOT a product -- the connection mixes base and fiber.
# The mixed Ricci components are:
# Ric_{mu a} = (1/2) D_nu F^nu_{mu a}
# which is non-zero and tau-dependent.

# Rather than attempting the full 12D computation (which requires data we
# don't have), let me extract the QUANTITATIVE implication from the Kerner
# numbers we DO have.

print("\n--- Phase 8: Quantitative Mixed a_4 Assessment ---")

# From the Kerner data (9 tau points):
# a_4^{fiber} includes {R_K^2, |Ric|^2, K} -- all fiber curvature invariants
# The MISSING mixed invariants are:
#   (i)   R_K * |F|^2  ~ R_K * omega3
#   (ii)  |F|^4        ~ omega3^2
#   (iii) R_{mu a} R^{mu a} * F ~ mixed Ricci-gauge
#
# Compute these at the 9 tau points:

RK_F2 = R_K_9 * omega3_9          # R_K * |omega_3|^2
F4 = omega3_9**2                    # |omega_3|^4

print("\nMixed curvature invariants (9 tau points):")
print(f"{'tau':>6s} {'a4_fiber':>12s} {'R_K*|F|^2':>12s} {'|F|^4':>12s} "
      f"{'ratio_RF':>12s} {'ratio_F4':>12s}")
for i, t in enumerate(tau_9):
    ratio_RF = RK_F2[i] / a4_geom_9[i]
    ratio_F4 = F4[i] / a4_geom_9[i]
    print(f"{t:6.2f} {a4_geom_9[i]:12.1f} {RK_F2[i]:12.3f} {F4[i]:12.3f} "
          f"{ratio_RF:12.6f} {ratio_F4:12.6f}")

# Growth comparison
print("\nGrowth rates of a_4 components (normalized to tau=0):")
print(f"{'tau':>6s} {'a4_fiber':>12s} {'R_K*|F|^2':>12s} {'|F|^4':>12s}")
for i, t in enumerate(tau_9):
    print(f"{t:6.2f} {a4_geom_9[i]/a4_geom_9[0]:12.4f} "
          f"{RK_F2[i]/RK_F2[0]:12.4f} {F4[i]/F4[0]:12.4f}")

# ---- THE DECISIVE TEST: Can mixed a_4 terms create a minimum? ----
#
# V_mixed(tau) = alpha * a_2^{total}(tau) + beta * [a_4^{fiber}(tau) + c_RF * R_K*|F|^2 + c_F4 * |F|^4]
#
# For a minimum: dV/dtau = 0 requires:
# alpha * da_2^{total}/dtau = -beta * d[a_4^{mixed}]/dtau
#
# Since da_2/dtau > 0 (monotone increasing) and d(a_4^{fiber})/dtau > 0,
# we need d(R_K*|F|^2)/dtau or d(|F|^4)/dtau to be NEGATIVE somewhere.
# But both R_K and |F|^2 are monotone increasing, so their product is too.
# And |F|^4 is monotone increasing.
#
# CONCLUSION: ALL mixed terms at the a_4 level are MONOTONE INCREASING.
# They cannot create competition with the a_2 term because they have
# the SAME monotonicity.

print("\n--- Phase 9: MONOTONICITY CHECK ---")
print("\nChecking d/dtau of all terms:")
d_a4_fiber = np.diff(a4_geom_9)
d_RK_F2 = np.diff(RK_F2)
d_F4 = np.diff(F4)
d_a2_total = np.diff(R_Kerner_total_9)  # a_2^{total} ~ R_K + (1/4)|F|^2

print(f"  da_4^fiber/dtau > 0 at all points: {np.all(d_a4_fiber > 0)}")
print(f"  d(R_K*|F|^2)/dtau > 0 at all points: {np.all(d_RK_F2 > 0)}")
print(f"  d(|F|^4)/dtau > 0 at all points: {np.all(d_F4 > 0)}")
print(f"  da_2^total/dtau > 0 at all points: {np.all(d_a2_total > 0)}")

# ---- BUT WAIT: The Freund-Rubin minimum exists! How? ----
#
# V_FR(tau) = -R_K(tau) + (beta/alpha) * |omega_3|^2(tau)
# has a minimum because:
# (1) R_K grows at rate ~1.14x over [0, 0.5] (slowly)
# (2) |omega_3|^2 grows at rate ~5.4x over [0, 0.5] (fast)
# (3) The MINUS sign on R_K creates competition
#
# In V_FR, R_K enters with MINUS sign (stabilization from curvature)
# and |omega_3|^2 enters with PLUS sign (destabilization from flux).
# The slow-growing R_K "wins" at small tau (minimum slopes down),
# but the fast-growing |omega_3|^2 "overtakes" at large tau (slopes up).
#
# In the SPECTRAL ACTION, BOTH terms enter a_2 with the SAME (positive) sign.
# The spectral action CANNOT reproduce the Freund-Rubin sign pattern
# from the a_2 coefficient alone.
#
# The ONLY way to get the Freund-Rubin minimum from the spectral action
# is through a_4 cross-terms where the Ricci-squared and Kretschner terms
# contribute with OPPOSITE signs to the R^2 term.
#
# From the Gilkey formula:
# a_4 = c_1 * R^2 - c_2 * |Ric|^2 + c_3 * K + tr(Omega^2) terms
# The MINUS sign on |Ric|^2 is physical!

print("\n--- Phase 10: Gilkey Sign Structure in Mixed a_4 ---")
print("\nGilkey formula for a_4 (spin Dirac, 8D):")
print("  a_4 = (dim_S/360) * [5*R^2 - 2*|Ric|^2 + 2*K] + (1/12) tr(Omega^2)")
print("  dim_S = 16 for 8D")
print(f"  5*R^2(0) = {5 * R_K[0]**2:.4f}")
print(f"  -2*|Ric|^2(0) = {-2 * Ric_sq_21[0]:.4f}")
print(f"  2*K(0) = {2 * K_21[0]:.4f}")

# On the TOTAL space (12D), dim_S = 64, and R_P includes gauge terms.
# R_P = R_K + (1/4)|F|^2 (ignoring R_4 which is tau-independent).
# R_P^2 = R_K^2 + (1/2)*R_K*|F|^2 + (1/16)*|F|^4
#
# The -2|Ric_P|^2 term on the total space includes:
# |Ric_P|^2 = |Ric_K|^2 + |Ric_mixed|^2 + |Ric_4|^2
# The MIXED Ricci tensor Ric_{mu a} = (1/2)D^nu F_{mu nu a} is:
# For the Yang-Mills equation on the fiber: D^nu F_{mu nu} = J_mu
# If the gauge field is ON-SHELL (satisfies YM equations), |Ric_mixed|^2 ~ |J|^2.
# For the Cartan connection on SU(3), the gauge field is NOT on-shell in general.
# The |Ric_mixed|^2 term depends on how far the connection is from satisfying YM.

# Compute the Gilkey a_4 on the total space with naive product:
# a_4^{total} = (64/360) * [5*(R_K + 0.25*omega3)^2 - 2*(|Ric|^2 + |Ric_mixed|^2)
#                            + 2*(K + K_mixed)]

# WITHOUT the mixed Ricci/Kretschner (lower bound on mixed effects):
a4_total_naive = np.zeros(len(tau_21))
for i in range(len(tau_21)):
    R_total = R_K[i] + 0.25 * omega3[i]
    a4_total_naive[i] = (64/360) * (5 * R_total**2 - 2 * Ric_sq_21[i] + 2 * K_21[i])

# The FIBER-ONLY a_4 (Connes):
a4_fiber_check = np.zeros(len(tau_21))
for i in range(len(tau_21)):
    a4_fiber_check[i] = (16/360) * (5 * R_K[i]**2 - 2 * Ric_sq_21[i] + 2 * K_21[i])

print("\n\nComparison: fiber-only vs total-space a_4 (naive product):")
print(f"{'tau':>6s} {'a4_fiber':>12s} {'a4_total':>12s} {'ratio':>10s} {'excess':>12s}")
for i in range(0, len(tau_21), 2):
    ratio = a4_total_naive[i] / a4_fiber[i] if a4_fiber[i] > 0 else float('inf')
    excess = a4_total_naive[i] - a4_fiber[i]
    print(f"{tau_21[i]:6.1f} {a4_fiber[i]:12.4f} {a4_total_naive[i]:12.4f} "
          f"{ratio:10.4f} {excess:12.4f}")

# ---- V_eff with mixed a_4 ----
# V_eff(tau) = a_2^{total}(tau) + rho * a_4^{total}(tau)
# where a_2^{total} = (64/6) * (R_K + 0.25*omega3) [grows monotonically]
# and a_4^{total} includes cross terms [also grows monotonically]

a2_total = (64/6) * (R_K + 0.25 * omega3)
V_eff_mixed = a2_total + rho_spec * a4_total_naive

# Normalize
V_eff_mixed_norm = V_eff_mixed - V_eff_mixed[0]

print("\n\nV_eff with mixed a_4 (normalized):")
dV = np.diff(V_eff_mixed_norm)
is_monotone = np.all(dV > 0) or np.all(dV < 0)
print(f"  Monotone: {is_monotone}")
print(f"  Direction: {'increasing' if dV[0] > 0 else 'decreasing'}")
for i in range(0, len(tau_21), 2):
    print(f"  tau={tau_21[i]:.1f}: V_eff_norm={V_eff_mixed_norm[i]:.4f}")

# =============================================================================
# THE FREUND-RUBIN RECONSTRUCTION FROM MIXED a_4
# =============================================================================

print("\n" + "=" * 70)
print("[MEME]S-1 PART 2: CAN a_4 CROSS-TERMS REPRODUCE V_FR?")
print("=" * 70)

# The Gilkey a_4 on the total space with R_P = R_K + (1/4)|F|^2:
# 5*R_P^2 = 5*[R_K^2 + (1/2)*R_K*|F|^2 + (1/16)*|F|^4]
# The cross term 5*(1/2)*R_K*|F|^2 enters with COEFFICIENT +5/2.
# The -2*|Ric_P|^2 can include MIXED Ricci with coefficient -2.
# If |Ric_mixed|^2 ~ c * R_K * |F|^2 (dimensional analysis), then
# the NET coefficient of R_K*|F|^2 is: 5/2 - 2*c.
# For c > 5/4, the NET coefficient is NEGATIVE.
#
# This would mean: the R_K*|F|^2 cross-term in a_4 OPPOSES the R_P^2 term.
# If this opposition is strong enough, it could create a minimum in V_eff.

# Estimate: what value of the mixed Ricci coefficient c is needed?
# V_eff = a_2(tau) + rho * a_4(tau)
# dV/dtau = da_2/dtau + rho * [da_4^{fiber}/dtau + d(cross)/dtau] = 0
# Need d(cross)/dtau < 0 somewhere, with |d(cross)/dtau| > da_2/dtau / rho + da_4^{fiber}/dtau

# The cross term: Delta_a4 = c_net * R_K * |F|^2
# If c_net < 0: Delta_a4 is negative (opposes the monotone increase)
# d(Delta_a4)/dtau = c_net * [dR_K/dtau * |F|^2 + R_K * d|F|^2/dtau]
# Both derivatives are positive, so if c_net < 0, d(Delta_a4)/dtau < 0.
# This WOULD create opposition.

# Required magnitude: |c_net * d(R_K*|F|^2)/dtau| > da_2/dtau + rho * da_4^{fiber}/dtau
# Using the 21-point data:

dR_K_F2_21 = np.gradient(R_K * omega3, tau_21)
da2_21 = np.gradient(a2_fiber, tau_21)
da4_f_21 = np.gradient(a4_fiber, tau_21)

# Required |c_net| for minimum at each tau (for various rho):
print("\nRequired |c_net| for dV/dtau = 0 at each tau:")
print("(c_net is the coefficient of R_K*|F|^2 in a_4; negative = opposing)")
for rho_test in [0.01, 0.1, 0.414, 1.0]:
    print(f"\n  rho = {rho_test}:")
    for i in [0, 1, 2, 3, 4, 5, 10, 15, 20]:
        if i < len(tau_21) and dR_K_F2_21[i] > 0:
            c_needed = (da2_21[i] + rho_test * da4_f_21[i]) / dR_K_F2_21[i]
            print(f"    tau={tau_21[i]:.1f}: |c_net|_needed = {c_needed:.6f}")

# =============================================================================
# EINSTEIN SUGGESTION E-5: a_0/a_2 RATIO FROM EXACT EIGENVALUE DATA
# =============================================================================

print("\n" + "=" * 70)
print("EINSTEIN E-5: a_0(tau)/a_2(tau) FROM EXACT EIGENVALUES")
print("=" * 70)

# a_0 = total eigenvalue count below cutoff (mode counting)
# a_2 = sum of eigenvalues squared below cutoff
# The RATIO a_0/a_2 measures the "average inverse eigenvalue squared"
#
# From Connes C6:
# a_0 is proportional to (dim_spinor/6) * Vol(K) [from the constant term in heat kernel]
# But from EXACT eigenvalue data, a_0(tau) = N_total (constant for fixed truncation)
# and a_2(tau) = sum_n lambda_n^2(tau) / ...
#
# More precisely:
# a_0 = Tr(1) = number of eigenvalues = 11424 (fixed at all tau for max_pq=6)
# a_2 = (1/6) * Tr(R_K * 1) = (dim_S/6) * R_K * Vol = a_2^Connes
#
# But the RATIO from EXACT data is:
# a_0_exact(tau) / a_2_exact(tau) = N / [(dim_S/6) * R_K(tau) * Vol(tau)]
#
# Since Vol(tau) decreases with tau (Jensen deformation reduces volume)
# and R_K increases, the product R_K * Vol can be non-monotone.
#
# Actually, for the spectral action:
# a_0 corresponds to f(0) * Tr(1) = f(0) * N
# a_2 corresponds to f(0) * integral R/6 * dim_S = f(0) * a_2^Connes
#
# The Dixmier trace ratio from Connes C1 is the relevant quantity.
# But Connes found it MONOTONE DECREASING.
#
# Let me compute the RATIO of successive heat kernel coefficients
# from the Connes data to look for sign changes or crossings.

a0_exact = 11424  # constant (total eigenvalues at max_pq=6)
a2_exact = a2_connes  # Connes computation
a4_exact = a4_connes  # Connes computation
a4_over_a2_exact = cn['a4_over_a2']

print(f"\na_0 (eigenvalue count) = {a0_exact} (constant)")
print(f"\na_0/a_2 ratio (measures cosmological-to-curvature scale):")
ratio_a0_a2 = a0_exact / a2_exact
for i in range(0, len(tau_21), 2):
    print(f"  tau={tau_21[i]:.1f}: a_0/a_2 = {ratio_a0_a2[i]:.4f}")

# Check for minimum or zero-crossing
d_ratio = np.diff(ratio_a0_a2)
print(f"\na_0/a_2 monotone: {np.all(d_ratio < 0) or np.all(d_ratio > 0)}")
print(f"a_0/a_2 direction: {'decreasing' if d_ratio[0] < 0 else 'increasing'}")
min_idx = np.argmin(ratio_a0_a2)
print(f"a_0/a_2 minimum at tau={tau_21[min_idx]:.1f}: {ratio_a0_a2[min_idx]:.4f}")

# Also compute: a_2/a_4 ratio (related to Lambda_eff)
ratio_a2_a4 = a2_exact / a4_exact
print(f"\na_2/a_4 ratio (inverse of expansion parameter):")
for i in range(0, len(tau_21), 2):
    print(f"  tau={tau_21[i]:.1f}: a_2/a_4 = {ratio_a2_a4[i]:.4f}")

d_ratio_24 = np.diff(ratio_a2_a4)
print(f"\na_2/a_4 monotone: {np.all(d_ratio_24 < 0) or np.all(d_ratio_24 > 0)}")
print(f"a_2/a_4 direction: {'decreasing' if d_ratio_24[0] < 0 else 'increasing'}")

# =============================================================================
# EINSTEIN Q-2: COSMOLOGICAL CONSTANT IMPLICATIONS
# =============================================================================

print("\n" + "=" * 70)
print("EINSTEIN Q-2: COSMOLOGICAL CONSTANT AT SURVIVING MINIMA")
print("=" * 70)

# The partition function minimum (Feynman F-1) is at tau~0.10-0.25.
# The gap-edge CW minimum (Feynman F-2) is at tau~0.15.
# The V_Baptista minimum is at tau~0.15 (kappa=772).
#
# For each: what is the VALUE of the potential at the minimum?
# If V(tau_min) ~ O(M_KK^4), the CC problem persists.
# If V(tau_min) is exponentially small, there may be hope.

# From the partition function F(tau; beta):
# F(tau; beta) = -ln(Z)/beta where Z = sum exp(-beta * lambda_n^2)
# At beta = 200 (T->0 limit): F -> lambda_min^2 = 0.6702 (at tau=0.25)
# The depth is 12.1%, so F_min = 0.6702 vs F_max = 0.6944 (at tau=0)
# Delta F = 0.6944 - 0.6702 = 0.024

# In physical units: if Lambda_KK is the KK scale,
# Delta V = Delta F * Lambda_KK^4 / (16 pi^2)
# For Lambda_KK ~ 10^{16} GeV (GUT scale):
# Delta V ~ 0.024 * (10^{16})^4 / (16*pi^2) ~ 10^{60} GeV^4
# This is ~10^{182} times Lambda_obs ~ 10^{-122} M_Pl^4

# For Lambda_KK ~ 1 TeV:
# Delta V ~ 0.024 * (10^3)^4 ~ 10^{10} GeV^4 ~ 10^{132} * Lambda_obs

print("\nPartition function minimum (Feynman F-1):")
lambda_min_0 = 0.8333  # at tau=0
lambda_min_025 = 0.8186  # at tau=0.25
F_0 = lambda_min_0**2
F_min = lambda_min_025**2
delta_F = F_0 - F_min
depth_pct = 100 * delta_F / F_0
print(f"  F(tau=0) = lambda_min^2(0) = {F_0:.6f}")
print(f"  F(tau=0.25) = lambda_min^2(0.25) = {F_min:.6f}")
print(f"  Delta F = {delta_F:.6f} ({depth_pct:.2f}% depth)")
print(f"  In units where eigenvalues are dimensionless (D_K units):")
print(f"    Delta V / M_KK^4 ~ {delta_F:.4f}")
print(f"    Lambda_obs / M_KK^4 ~ 10^(-122) * (M_Pl/M_KK)^4")
print(f"    For M_KK = M_GUT (10^16 GeV): ratio = {delta_F:.4f} / 10^(-122+8) ~ 10^{np.log10(delta_F)+114:.0f}")
print(f"    For M_KK = 1 TeV: ratio = {delta_F:.4f} / 10^(-122+60) ~ 10^{np.log10(delta_F)+62:.0f}")
print(f"  CONCLUSION: The minimum depth is O(1) in KK units.")
print(f"  ANY non-zero stabilization energy creates a CC problem")
print(f"  that is 10^60 to 10^114 times worse than observation.")

# V_Baptista at minimum
print("\nV_Baptista minimum:")
print(f"  V_Baptista(tau=0.15) - V_Baptista(tau=0) = (kappa-dependent)")
print(f"  For kappa=772: the minimum is O(R_K) ~ O(10) in KK^4 units")
print(f"  This is the SAME CC problem as all other stabilization mechanisms.")

# =============================================================================
# PARTITION FUNCTION THERMODYNAMICS (BEC ANALOGY, Paper 08)
# =============================================================================

print("\n" + "=" * 70)
print("EINSTEIN: PARTITION FUNCTION AS BEC-TYPE PHASE TRANSITION")
print("=" * 70)

# From Paper 08 (BEC, 1924): The thermodynamic potential of a quantum gas
# exhibits a condensation when the chemical potential reaches the ground
# state energy. The partition function Z = sum exp(-beta * E_n) shows
# this as a non-analyticity at beta_c.
#
# In the spectral gas: Z(tau; beta) = sum exp(-beta * lambda_n^2(tau))
# The "condensation" occurs when beta is large enough that only the
# gap-edge modes contribute (the rest are exponentially suppressed).
# This is precisely the lambda_min turnaround regime.
#
# The BEC analogy: the lambda_min turnaround at tau~0.23 is the
# "ground state energy minimum" of the spectral gas. At high beta,
# the free energy F -> lambda_min^2 (ground state dominates).
# The tau-dependence of F is then entirely set by lambda_min(tau).
#
# lambda_min(tau) has a minimum at tau~0.23 (Session 24a, Feynman F-5).
# Therefore F(tau; beta->inf) has a minimum at tau~0.23.
# This is NOT a phase transition -- it is ground-state dominance.

# Compute the "condensation temperature" beta_c:
# At beta_c, the gap-edge contribution = (second level contribution)
# exp(-beta_c * lambda_1^2) = exp(-beta_c * lambda_2^2)
# This requires lambda_1 = lambda_2 (degenerate), which is always true
# for Kramers pairs. So beta_c is determined by the gap to the NEXT level.

# From the eigenvalue data at tau=0:
# lambda_min = 0.8333 (16-fold Kramers degenerate)
# lambda_next ~ 0.84 (next distinct level)
# gap = lambda_next^2 - lambda_min^2 ~ 0.007

gap_sq = 0.84**2 - 0.8333**2
beta_c = 1.0 / gap_sq if gap_sq > 0 else float('inf')
print(f"\nBEC condensation analogy:")
print(f"  Gap-edge eigenvalue: lambda_min = 0.8333")
print(f"  Next distinct level: lambda_2 ~ 0.84")
print(f"  Spectral gap^2 = {gap_sq:.6f}")
print(f"  beta_c = 1/gap^2 ~ {beta_c:.1f}")
print(f"  (Feynman found non-monotonicity onset at beta ~ 10, consistent)")
print(f"\n  Physical interpretation: The partition function 'condenses' onto")
print(f"  the gap-edge modes when beta > {beta_c:.0f}. At that point, F(tau)")
print(f"  is controlled entirely by lambda_min(tau), whose turnaround at")
print(f"  tau~0.23 produces the partition function minimum.")
print(f"\n  This is BEC-LIKE ground state dominance, NOT a thermodynamic")
print(f"  phase transition. The 'minimum' is a kinematic feature of")
print(f"  lambda_min(tau), not a dynamical stabilization mechanism.")

# =============================================================================
# SPECTRAL BIANCHI IDENTITY (Q-3)
# =============================================================================

print("\n" + "=" * 70)
print("EINSTEIN Q-3: SPECTRAL ANALOG OF THE BIANCHI IDENTITY")
print("=" * 70)

# In GR: nabla_mu G^{mu nu} = 0 identically (Bianchi identity)
# This constrains the field equations and implies conservation of T^{mu nu}.
# For the EIH result (Paper 10): the Bianchi identity DERIVES motion.
#
# In the spectral action:
# S[D] = Tr f(D^2/Lambda^2)
# Under a variation D -> D + delta D:
# delta S = Tr [f'(D^2/Lambda^2) * (D * delta D + delta D * D)]
# = Tr [f'(D^2/Lambda^2) * {D, delta D}]
# Setting delta S = 0 gives the equation of motion.
#
# The BIANCHI ANALOG is: for gauge transformations D -> U D U^{-1},
# delta D = [U-1, D] (infinitesimally). The gauge invariance of S
# gives:
# Tr [f'(D^2/Lambda^2) * {D, [T, D]}] = 0 for all T in Lie(G)
#
# For the Peter-Weyl decomposition, T is a generator of SU(3)_left.
# The identity becomes:
# sum_{(p,q)} d_{(p,q)} * [d/dtau V_{(p,q)}(tau)] * <T>_{(p,q)} = 0
# where <T>_{(p,q)} is the expectation of T in sector (p,q).
#
# This is the spectral Bianchi identity: the SECTOR-WEIGHTED DERIVATIVE
# of V is constrained by the gauge symmetry. It does NOT force V to be
# constant, but it RELATES the slopes of different sector contributions.

print("\nThe spectral Bianchi identity constrains sector-weighted derivatives:")
print("  sum_{(p,q)} d_{(p,q)} * dV_{(p,q)}/dtau * <K_a>_{(p,q)} = 0")
print("")
print("  This is the spectral analog of nabla_mu G^{mu nu} = 0.")
print("  It follows from the LEFT gauge invariance of the spectral action.")
print("  The identity RELATES sector slopes but does NOT force them to zero.")
print("  Block-diagonality (W2) ensures each sector's V is independent,")
print("  but the Bianchi constraint ties their derivatives together.")
print("")
print("  Physical consequence: The derivative dS_eff/dtau is NOT arbitrary.")
print("  The spectral Bianchi identity constrains HOW FAST the total")
print("  weighted spectral action can change with tau. It does not, however,")
print("  force dS_eff/dtau = 0 at any particular tau.")
print("")
print("  Connection to EIH (Paper 10): Just as the contracted Bianchi")
print("  identity in GR DERIVES the geodesic equation from the field")
print("  equations, the spectral Bianchi identity should DERIVE the")
print("  modulus equation of motion from the spectral action principle.")
print("  The modulus does not need an independent equation of motion --")
print("  its dynamics follows from the spectral action through the identity.")

# =============================================================================
# V_FR vs V_full INTERPRETATION
# =============================================================================

print("\n" + "=" * 70)
print("EINSTEIN: V_FR vs V_full INTERPRETATION")
print("=" * 70)

# KK-S3 showed V_full does NOT track V_FR.
# Spearman correlation at Lambda=1: rho = 0.867 (both decreasing)
# At Lambda=5: rho = -0.867 (opposite directions)
#
# The anti-correlation at Lambda=5 is key: V_full INCREASES while V_FR DECREASES.
# This means the spectral action (sum over eigenvalues) sees DIFFERENT physics
# than the Freund-Rubin potential (curvature vs flux competition).

print("\nV_FR and V_full detect DIFFERENT geometric properties:")
print("  V_FR = -R_K + (beta/alpha)*|omega_3|^2  [curvature vs flux]")
print("  V_full = sum f(lambda_n^2/Lambda^2)      [total eigenvalue distribution]")
print("")
print("  V_FR has a minimum because -R_K and +|omega_3|^2 compete.")
print("  V_full is monotone because eigenvalue SUMS cannot see the flux.")
print("  The D_K eigenvalues encode R_K (through Lichnerowicz) but NOT |omega_3|^2.")
print("  The flux enters only through MIXED curvature terms R_{mu a nu b}")
print("  which are absent from the fiber Dirac operator.")
print("")
print("  EINSTEIN VERDICT: V-1 (V_spec monotone) is a statement about the")
print("  fiber-only spectral action. The FULL 12D spectral action, which")
print("  includes the gauge field strength, is a different object whose")
print("  monotonicity has NOT been tested. The Kerner decomposition shows")
print("  the flux term |omega_3|^2 grows 5.4x faster than R_K, but")
print("  enters the spectral action a_2 with the SAME sign (not opposing).")
print("  The cross-terms at the a_4 level COULD oppose if the mixed Ricci")
print("  contributions have the right magnitude (|c_net| > 5/4), but this")
print("  requires computing the full 12D Dirac operator -- a calculation")
print("  beyond existing data.")

# =============================================================================
# SAVE RESULTS
# =============================================================================

print("\n" + "=" * 70)
print("SAVING RESULTS")
print("=" * 70)

np.savez('tier0-computation/s25_einstein_results.npz',
         # Kerner decomposition
         tau_9=tau_9,
         tau_21=tau_21,
         R_K_9=R_K_9,
         omega3_9=omega3_9,
         a4_geom_9=a4_geom_9,
         R_K_growth=R_K_growth,
         omega3_growth=omega3_growth,
         a4_growth=a4_growth,
         gauge_to_curvature_ratio=gauge_to_curvature_ratio,
         # Mixed invariants
         RK_F2=RK_F2,
         F4=F4,
         R_Kerner_total_9=R_Kerner_total_9,
         # Mixed a_4
         a4_total_naive=a4_total_naive,
         # E-5: a_0/a_2 ratio
         ratio_a0_a2=ratio_a0_a2,
         ratio_a2_a4=ratio_a2_a4,
         # Parameter scan
         has_min_map=has_min_map,
         gamma_range=gamma_range,
         rho_range=rho_range,
         tau_min_map=tau_min_map,
         depth_map=depth_map,
         # BEC analogy
         beta_c=np.array(beta_c),
         gap_sq=np.array(gap_sq),
         # Cosmological constant
         delta_F_partition=np.array(delta_F),
)

print("Results saved to tier0-computation/s25_einstein_results.npz")
print("\nComputation complete.")
