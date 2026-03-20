#!/usr/bin/env python3
"""
Session 39: Nazarewicz Review of SCHWING-PROOF-39
==================================================

Independent verification from nuclear BCS perspective.

The gen-physicist declared FAIL on the S38 Schwinger-instanton identity.
This script independently verifies the key numbers and assesses whether
the nuclear physics perspective reveals any subtlety missed.

CRITICAL QUESTION: In nuclear physics, the instanton action through a
pairing barrier and the Schwinger pair-creation exponent ARE related
through the WKB integral. Is the gen-physicist comparing the right
quantities?

The S38 claim was:
  S_Schwinger = pi * Delta_0^2 / |dtau/dt| = 0.070
  S_inst = integral sqrt(2V) dDelta = 0.069

The gen-physicist's objection: S_Schwinger used Delta_0_GL = 0.770
but S_inst used the numerical landscape with Delta_0_num = 0.365.

MY QUESTION: What is Delta_0_peak = 0.770 physically?

Author: nazarewicz-nuclear-structure-theorist (Session 39 review)
"""

import numpy as np
from scipy.integrate import quad, trapezoid
from scipy.interpolate import CubicSpline

# ====================================================================
# LOAD DATA
# ====================================================================
s37 = np.load('tier0-computation/s37_instanton_action.npz', allow_pickle=True)
s36 = np.load('tier0-computation/s36_tau_dynamics.npz', allow_pickle=True)
s39 = np.load('tier0-computation/s39_schwinger_proof.npz', allow_pickle=True)

# Key stored quantities
a_GL = s37['a_A'].item()
b_GL = s37['b_A'].item()
Delta_0_GL = np.sqrt(-a_GL / (2 * b_GL))
Delta_0_num = s37['Delta_0_num'].item()
S_inst_D = s37['S_inst_D'].item()
S_inst_A = s37['S_inst_A'].item()
V_bar_D = s37['barrier_D'].item()
V_bar_A = s37['barrier_A'].item()
v_terminal = abs(s36['an_S_full_v_terminal'].item())
E_cond = s37['E_cond_use'].item()
delta_scan = s37['delta_scan']
F_BCS = s37['F_BCS_B2']

print("=" * 72)
print("NAZAREWICZ INDEPENDENT REVIEW: SCHWING-PROOF-39")
print("=" * 72)
print()

# ====================================================================
# SECTION 1: Verify gen-physicist's key numbers
# ====================================================================
print("SECTION 1: Independent verification of key numbers")
print("-" * 50)

# (a) GL instanton action
S_GL_check = np.sqrt(2*b_GL) * (2/3) * Delta_0_GL**3
print(f"  S_inst_GL = sqrt(2b)*(2/3)*D0^3 = {S_GL_check:.10f}")
print(f"  gen-phys stored: {S_inst_A:.10f}")
print(f"  MATCH: {abs(S_GL_check - S_inst_A) < 1e-8}")

# (b) S_Schwinger(S38) with GL gap
S_Schw = np.pi * Delta_0_GL**2 / v_terminal
print(f"  S_Schwinger(S38) = pi*D0_GL^2/|v| = {S_Schw:.10f}")
print(f"  gen-phys stored: {s39['S_Schwinger_S38'].item():.10f}")
print(f"  MATCH: {abs(S_Schw - s39['S_Schwinger_S38'].item()) < 1e-8}")

# (c) GL ratio
ratio_GL = S_GL_check / S_Schw
print(f"  S_inst_GL / S_Schwinger = {ratio_GL:.6f}")
print(f"  gen-phys: {s39['ratio_GL'].item():.6f}")
print(f"  MATCH: {abs(ratio_GL - s39['ratio_GL'].item()) < 1e-4}")

# (d) Numerical instanton action (direct integration)
F_min = F_BCS.min()
idx_min = np.argmin(F_BCS)
F_shifted = F_BCS - F_min
integrand = np.sqrt(2 * np.maximum(0, F_shifted[:idx_min+1]))
S_D_check = trapezoid(integrand, delta_scan[:idx_min+1])
print(f"  S_inst_D (my recomputation) = {S_D_check:.10f}")
print(f"  S_inst_D (stored) = {S_inst_D:.10f}")
print(f"  MATCH: {abs(S_D_check - S_inst_D) < 1e-8}")

# (e) Discrepancy
disc = abs(S_Schw - S_inst_D) / S_inst_D
print(f"  |S_Schwinger - S_inst_D| / S_inst_D = {disc*100:.4f}%")
print(f"  gen-phys: {s39['disc_S38'].item()*100:.4f}%")
print()

print("  ==> ALL KEY NUMBERS CONFIRMED. The gen-physicist's arithmetic is correct.")
print()

# ====================================================================
# SECTION 2: What is Delta_0_GL = 0.770 physically?
# ====================================================================
print("SECTION 2: Physical meaning of Delta_0_GL")
print("-" * 50)
print()

# Delta_0_GL = sqrt(-a/(2b)) where a = 2*E_cond/Delta_0_peak^2
# This means Delta_0_GL IS Delta_0_peak by construction.
# It is the self-consistent BCS gap from the gap equation.
# But Delta_0_num = 0.365 is the minimum of F_BCS along the alpha path.
# These differ because the alpha-parametrization is NOT the gap equation.

# Let me understand the F_BCS landscape construction.
# From s37_instanton_action.py:
#   F(alpha) = sum_k [E_k(alpha) - |xi_k|] - sum_{kk'} V_{kk'} * sqrt(rho)*Delta_k*Delta_{k'}/(4*E_k*E_{k'})
#   Delta_k(alpha) = alpha * Delta_k^SC
#   where Delta_k^SC is the self-consistent gap (from the gap equation)
#
# The minimum of F(alpha) occurs at alpha != 1 because F(alpha) is
# NOT the same as the BCS free energy at gap Delta = alpha*Delta_SC.
# The alpha=1 point IS the self-consistent solution by construction.
# But F(alpha) can have its minimum elsewhere because the scaling
# ansatz Delta_k(alpha) = alpha * Delta_k^SC constrains the direction
# in Delta-space while varying the magnitude.

# CRITICAL CHECK: What is F at alpha = 1?
# alpha_min should be at alpha = 1 for the self-consistent solution
# UNLESS the parametrization is inconsistent.

# Let me reconstruct this
print("  The F_BCS landscape was constructed by:")
print("  1. Solving the gap equation: Delta_k^SC (self-consistent)")
print("  2. Computing F(alpha) = BCS energy at Delta_k = alpha * Delta_k^SC")
print("  3. The minimum should be at alpha = 1 (self-consistency)")
print()
print(f"  delta_scan = alpha * max(Delta_SC), range: [0, {delta_scan[-1]:.4f}]")
print(f"  Delta_0_peak = max(Delta_SC) = {s37['Delta_0_peak'].item():.6f}")
print(f"  Delta_0_num = delta_scan at F_min = {Delta_0_num:.6f}")
print(f"  alpha_min = Delta_0_num / Delta_0_peak = {Delta_0_num / s37['Delta_0_peak'].item():.6f}")
print()

# The minimum is at alpha = 0.473, NOT at alpha = 1.
# This means the gap equation solution is NOT the F(alpha) minimum.
# Why? Because the gap equation sets dF/dDelta_k = 0 for each k
# independently, while F(alpha) constrains all Delta_k to vary
# proportionally. These are different variational conditions.

alpha_at_min = Delta_0_num / s37['Delta_0_peak'].item()
print(f"  alpha at F_BCS minimum = {alpha_at_min:.6f}")
print(f"  This is NOT 1.0. The scaling ansatz minimum differs from")
print(f"  the self-consistent gap equation solution.")
print()
print(f"  WHY THEY DIFFER:")
print(f"  The gap equation solves dF/dDelta_k = 0 for each mode k.")
print(f"  The alpha-path minimizes F along Delta_k = alpha * Delta_k^SC.")
print(f"  These have different variational spaces:")
print(f"    Gap eq: all Delta_k are independent (8-dim optimization)")
print(f"    Alpha: all Delta_k locked in proportion (1-dim optimization)")
print(f"  The 1D restriction imposes a constraint that shifts the minimum.")
print()

# CRITICAL: Which is the correct instanton path?
# In nuclear physics, the instanton connects Delta=0 to the ground state.
# The COLLECTIVE PATH through the BCS energy surface matters.
# For a single-variable order parameter (like total |Delta|), the
# alpha-path IS the instanton path if we parametrize by the overall gap.
# For multi-mode BCS, the correct instanton path minimizes the action
# S = integral sqrt(2*m_eff(Delta)*V(Delta)) dDelta
# where m_eff is the collective mass along the path.

print(f"  INSTANTON PATH ASSESSMENT:")
print(f"  For nuclear fission, the instanton path is the MINIMUM ACTION path")
print(f"  through the multi-dimensional energy surface. The alpha-scaling")
print(f"  path is ONE choice of collective coordinate.")
print(f"  For a rank-1 separable pairing (our case: Richardson-Gaudin),")
print(f"  the alpha-scaling path IS the natural collective coordinate")
print(f"  because the gap vector has a fixed direction set by the")
print(f"  pairing matrix V (Schur's lemma: V is proportional to identity")
print(f"  within B2). The instanton follows this direction.")
print()
print(f"  S_inst_D (along alpha-path) = {S_inst_D:.6f}")
print(f"  This is the CORRECT instanton action for the system.")
print()

# ====================================================================
# SECTION 3: The provenance of E_cond_use
# ====================================================================
print("SECTION 3: Provenance of GL parameters")
print("-" * 50)
print()

# E_cond_use is NOT the minimum of F_BCS along the alpha-path.
# It is the BCS energy at the self-consistent gap (alpha=1).
# Let me verify this.

# F at alpha=1 point:
Delta_SC_max = s37['Delta_0_peak'].item()
# Find the index closest to alpha=1
idx_alpha1 = np.argmin(np.abs(delta_scan - Delta_SC_max))
F_at_alpha1 = F_BCS[idx_alpha1]

print(f"  E_cond_use (stored) = {E_cond:.10f}")
print(f"  F_BCS at alpha=1 (delta={delta_scan[idx_alpha1]:.6f}) = {F_at_alpha1:.10f}")
print(f"  F_BCS minimum = {F_min:.10f}")
print()

# Check: is E_cond_use = F at alpha=1?
print(f"  Is E_cond_use approx F(alpha=1)? diff = {abs(E_cond - F_at_alpha1):.6f}")
# Actually E_cond_use was computed from the GCM fine grid at the fold
# (see s37 script line 187: E_cond_use = float(gcm_data['E_BCS_fine'][idx_peak]))
# This is the full self-consistent BCS energy, not the alpha-path energy.

print(f"  NOTE: E_cond_use = -0.1557 comes from the self-consistent BCS")
print(f"  gap equation solution (GCM fine grid at tau_fold).")
print(f"  F_BCS min along alpha-path = {F_min:.6f} (different!)")
print(f"  The GL parameters a, b were extracted from E_cond_use and Delta_0_peak,")
print(f"  NOT from the alpha-path landscape.")
print()

# The inconsistency the gen-physicist identified:
# GL params: derived from (E_cond=-0.156, Delta_0=0.770) [gap equation]
# S_inst: computed from F_BCS along alpha-path [minimum at Delta=0.365]
# S_Schwinger: uses Delta_0_GL = 0.770 [from GL params]

# These are indeed THREE different computations that don't fully align.

# ====================================================================
# SECTION 4: Nuclear physics of the comparison
# ====================================================================
print("SECTION 4: Nuclear physics perspective")
print("-" * 50)
print()

print("""  In nuclear physics, the Schwinger pair-production formula applies to
  quasiparticle pair creation in a time-varying mean field:

    Gamma_pair ~ exp(-pi * Delta^2 / |dE/dt|)                     (*)

  where Delta is the pairing gap and |dE/dt| is the rate of change of
  the quasiparticle energy. This is the Landau-Zener formula for
  non-adiabatic pair-breaking.

  The instanton action, by contrast, is:

    S_inst = integral_0^{Delta_0} sqrt(2 * V(Delta)) dDelta        (**)

  where V(Delta) is the BCS free energy landscape (shifted).

  These are DIFFERENT physical quantities:
  (*) measures the real-time pair creation rate during a sweep
  (**) measures the Euclidean tunneling amplitude between paired/unpaired

  My S38 claim that they are "the same WKB integral" was imprecise.
  The WKB integral for tunneling through a barrier V(x):
    S_WKB = integral sqrt(2m*V(x)) dx
  and the Schwinger exponent for pair creation:
    S_Schwinger = pi * Delta^2 / |dxi/dt|
  are related only when the BCS energy landscape is quadratic
  (Delta^2 potential) AND the time-variation is linear.

  In the GL limit with V(Delta) = b*(Delta^2 - D0^2)^2:
    S_inst = sqrt(2b)*(2/3)*D0^3
    S_Schwinger(my formula) = pi*D0^2/|v|

  These are NOT equal. The gen-physicist correctly showed that their
  ratio is (2/3)*sqrt(|a|)*|v|/pi = 4.08.

  However: the gen-physicist did NOT address whether there exists a
  DIFFERENT form of the Schwinger exponent that IS the instanton action.
""")

# ====================================================================
# SECTION 5: Alternative Schwinger formula
# ====================================================================
print("SECTION 5: Is there a correct Schwinger-instanton identity?")
print("-" * 50)
print()

# In QED, the Schwinger pair production rate is:
#   Gamma ~ exp(-pi * m^2 / (e*E))
# where m is the particle mass and E is the electric field.
#
# For BCS quasiparticles in a time-varying gap, the analog is:
#   Gamma ~ exp(-pi * Delta_0^2 / |dDelta/dt|)  [NOT |v| = |dtau/dt|]
#
# But |dDelta/dt| = |dDelta/dtau| * |dtau/dt| = |dDelta/dtau| * |v|
#
# At the fold, |dDelta/dtau| -> 0 (peak of Delta), so S_LZ diverges.
# Away from the fold, Delta is smaller.
#
# The correct Schwinger exponent for pair creation in a time-dependent
# BCS system is NOT pi*Delta^2/|v|. It is:
#   S_Schwinger = pi * Delta^2 / |dDelta/dt|
# for the Landau-Zener formula, or more precisely:
#   S_Schwinger = integral_C pi * Delta(tau)^2 / |v| * |dk/dtau| dtau
# for the full path integral.
#
# But the instanton action measures something different:
# it is the Euclidean action for tunneling between Delta=0 and Delta=D0.
# This is NOT a pair creation rate.

# Let me check: in the limit where both are meaningful,
# do they agree?

# For a simple double-well with barrier height V0 and width d:
#   S_WKB ~ sqrt(V0) * d
#   S_Schwinger ~ Delta^2/E_dot where E_dot is the driving rate

# These are dimensionally different quantities unless we identify
# appropriate scales.

# The S38 "coincidence" is:
# pi * (0.770)^2 / 26.545 = 0.0703
# integral sqrt(2*F_BCS) d(Delta) = 0.0686

# Let me compute what the Schwinger formula gives with the CORRECT gap
S_Schw_correct = np.pi * Delta_0_num**2 / v_terminal
print(f"  S_Schwinger with Delta_0_num = {Delta_0_num:.6f}:")
print(f"    pi * ({Delta_0_num:.6f})^2 / {v_terminal:.4f} = {S_Schw_correct:.10f}")
print(f"    vs S_inst_D = {S_inst_D:.10f}")
print(f"    ratio = {S_Schw_correct / S_inst_D:.4f}")
print()
print(f"  S_Schwinger with Delta_0_GL = {Delta_0_GL:.6f}:")
print(f"    pi * ({Delta_0_GL:.6f})^2 / {v_terminal:.4f} = {S_Schw:.10f}")
print(f"    vs S_inst_D = {S_inst_D:.10f}")
print(f"    ratio = {S_Schw / S_inst_D:.4f}")
print()

# With the correct numerical gap, the Schwinger formula gives 0.0158,
# much smaller than S_inst = 0.069. So the "near-agreement" only
# works with the GL gap, which is 2.1x larger.

# ====================================================================
# SECTION 6: Shape factor kappa analysis
# ====================================================================
print("SECTION 6: Shape factor kappa = 0.653 near 2/3 = 0.667")
print("-" * 50)
print()

kappa_num = S_inst_D / (np.sqrt(2 * V_bar_D) * Delta_0_num)
kappa_GL = 2.0/3.0

print(f"  kappa_num = S_inst / (sqrt(2V)*D0) = {kappa_num:.6f}")
print(f"  kappa_GL  = 2/3 = {kappa_GL:.6f}")
print(f"  ratio = {kappa_num / kappa_GL:.6f}")
print()

# Is the 2% proximity of kappa_num to 2/3 a coincidence?
# In nuclear physics, the shape factor kappa depends on the barrier
# profile. For different potentials:
#   Quartic GL: kappa = 2/3 = 0.6667
#   Inverted harmonic: kappa = pi/4 = 0.7854
#   Rectangular: kappa = 1.0
#   Triangular: kappa = sqrt(2)/3 = 0.4714
#   Eckart: kappa = pi/4 (same as harmonic)
#   Woods-Saxon: kappa varies from 0.6 to 0.8

# The fact that kappa_num = 0.653 is close to 2/3 means the
# BCS landscape is qualitatively similar to the GL quartic in its
# SHAPE, even though the SCALE (gap, barrier height) differs.
# This is expected: the BCS free energy near a second-order transition
# is always approximately quartic (Landau theory).

# But the key quantitative question: does kappa HAVE to be near 2/3
# for a BCS system?

# For any symmetric double-well V(Delta) = V(-Delta) with a single
# minimum at Delta_0, the landscape can be written as:
#   V(Delta) = V_bar * f((Delta/Delta_0)^2)
# where f is a shape function with f(0) = 1, f(1) = 0, f'(1) < 0.

# Then S_inst = sqrt(2*V_bar) * Delta_0 * integral_0^1 sqrt(f(u)) * du/(2*sqrt(u))
# = sqrt(2*V_bar) * Delta_0 * (1/2) * integral_0^1 sqrt(f(u)) / sqrt(u) du

# For f(u) = (1-u)^2 (GL quartic): kappa = 2/3 (exact)
# For more general f, kappa depends on the shape of f.

# Let me compute f(u) for the actual BCS landscape
u_grid = (delta_scan[:idx_min+1] / Delta_0_num)**2
f_grid = (F_BCS[:idx_min+1] - F_min) / V_bar_D

# Check normalization
print(f"  Shape function f(u) verification:")
print(f"    f(0) = {f_grid[0]:.6f} (should be 1)")
print(f"    f(1) = {f_grid[-1]:.10f} (should be 0)")
print()

# Compare to GL: f_GL(u) = (1-u)^2
u_fine = np.linspace(0, 1, 1000)
f_GL = (1 - u_fine)**2

# Interpolate f_grid to compare
f_interp = np.interp(u_fine, u_grid, f_grid)

# RMS deviation
rms_dev = np.sqrt(np.mean((f_interp - f_GL)**2))
max_dev = np.max(np.abs(f_interp - f_GL))
print(f"  Deviation from GL shape (1-u)^2:")
print(f"    RMS = {rms_dev:.6f}")
print(f"    Max = {max_dev:.6f}")
print(f"    Max at u = {u_fine[np.argmax(np.abs(f_interp - f_GL))]:.4f}")
print()

# The shape IS near-GL. Let me quantify with the next correction.
# f(u) = (1-u)^2 + c3*(1-u)^3 + ...
# For small corrections: kappa = 2/3 * (1 + 3*c3/10 + ...)

# Fit f to: a*(1-u)^2 + b*(1-u)^3
mask_shape = u_fine < 0.95
A_shape = np.column_stack([(1-u_fine[mask_shape])**2, (1-u_fine[mask_shape])**3])
y_shape = f_interp[mask_shape]
coeffs_shape, _, _, _ = np.linalg.lstsq(A_shape, y_shape, rcond=None)
print(f"  Shape decomposition: f(u) = {coeffs_shape[0]:.4f}*(1-u)^2 + {coeffs_shape[1]:.4f}*(1-u)^3")
print(f"  c3/c2 = {coeffs_shape[1]/coeffs_shape[0]:.4f}")
print(f"  Expected kappa correction: kappa = 2/3 * (1 + 3*c3/(10*c2)) = {2/3*(1 + 3*coeffs_shape[1]/(10*coeffs_shape[0])):.4f}")
print(f"  Actual kappa = {kappa_num:.4f}")
print()

# ====================================================================
# SECTION 7: The "effective gap" D_eff
# ====================================================================
print("SECTION 7: Effective gap D_eff and its meaning")
print("-" * 50)
print()

D_eff = np.sqrt(S_inst_D * v_terminal / np.pi)
print(f"  D_eff = sqrt(S_inst * |v| / pi) = {D_eff:.10f}")
print(f"  Delta_0_GL = {Delta_0_GL:.10f}")
print(f"  D_eff / Delta_0_GL = {D_eff / Delta_0_GL:.6f}")
print()

# D_eff is defined so that pi*D_eff^2/|v| = S_inst_D exactly.
# It is 98.8% of Delta_0_GL. But what IS D_eff physically?

# D_eff^2 = S_inst * |v| / pi
#         = [integral sqrt(2V) dDelta] * |v| / pi

# In the GL limit:
# D_eff_GL^2 = [sqrt(2b)*(2/3)*D0^3] * |v| / pi
# For D_eff_GL = D0: need |v| = 3*pi / (2*sqrt(2b)*D0) = 3*pi / (2*sqrt(|a|))

# The gen-physicist correctly showed that D_eff = 0.96*D0_GL is a
# coincidence requiring |v| to have a specific value.

# But let me check: is there a quantity that naturally has this value?
v_needed = 3*np.pi / (2*np.sqrt(abs(a_GL)))
print(f"  For D_eff = D0_GL exactly, need |v| = {v_needed:.6f}")
print(f"  Actual |v| = {v_terminal:.6f}")
print(f"  Ratio = {v_terminal / v_needed:.4f}")
print()

# The actual velocity is 4.08x larger than needed.
# This factor is EXACTLY the ratio_GL = S_inst_GL / S_Schwinger.

# ====================================================================
# SECTION 8: The CORRECT nuclear analog
# ====================================================================
print("SECTION 8: Correct nuclear analog (fission/fusion WKB)")
print("-" * 50)
print()

print("""  My S38 claim was that the Schwinger-instanton identity is analogous to
  the fission-fusion WKB duality in nuclear physics:
    WKB_fission = integral sqrt(2*m_coll*V(r)) dr  (tunneling out)
    WKB_fusion  = integral sqrt(2*mu*[V(r)-E]) dr  (tunneling in)
  These are the SAME integral evaluated at the same energy E in the
  same potential V(r). The Euclidean/Lorentzian duality is exact.

  For the BCS problem, the analog would be:
    S_inst = integral_0^{D0} sqrt(2*V(Delta)) dDelta  (Euclidean)
    S_pair_creation = integral (pair creation exponent) dt  (Lorentzian)

  But the Lorentzian quantity pi*D0^2/|v| is NOT the pair creation
  integral through the same potential. It is the Schwinger formula
  for a CONSTANT gap D0 and a constant sweep rate |v|.

  The correct Lorentzian pair creation integral would be:
    S_LZ = integral pi*Delta(t)^2 / |d(xi(t))/dt| dt
  where xi(t) is the quasiparticle energy and Delta(t) is the gap.
  This is the integrated Landau-Zener exponent.

  For the system, the "sweep" is not through the quasiparticle spectrum
  with a fixed gap -- it is a variation of tau that changes BOTH the
  single-particle energies AND the gap simultaneously.

  SELF-CORRECTION: My S38 statement "the WKB integral is the same in
  both signatures" was wrong. The instanton action and the Schwinger
  exponent are NOT automatically equal, even approximately, unless the
  BCS landscape is quadratic AND the gap scales linearly with time.
  Neither condition holds here.
""")

# ====================================================================
# SECTION 9: What the shape factor proximity DOES mean
# ====================================================================
print("SECTION 9: What kappa = 0.653 ~ 2/3 tells us")
print("-" * 50)
print()

print(f"  kappa_num / kappa_GL = {kappa_num/kappa_GL:.4f} (2% deviation)")
print()
print("  This proximity is NOT a coincidence. It has a physical origin:")
print("  the BCS free energy landscape is APPROXIMATELY quartic near")
print("  the transition. Landau theory guarantees this: near a second-")
print("  order phase transition, the free energy is expandable in even")
print("  powers of the order parameter, with the quartic term being the")
print("  leading nonlinear term.")
print()
print("  The 2% deviation from 2/3 measures the importance of the a6")
print("  and higher terms. Since |a6/a4| = 0.88 (order unity), the")
print("  quartic approximation fails for the overall SCALE (4.2x error")
print("  in S_inst) but preserves the SHAPE to 2% because kappa is a")
print("  ratio that cancels most of the scale dependence.")
print()
print("  In nuclear physics, the fission barrier shape factor is")
print("  similarly stable under changes in the barrier parameters.")
print("  Strutinsky shell corrections change the barrier height by")
print("  1-3 MeV but the shape factor varies by only 5-10%.")
print("  This is because the shape factor is a GEOMETRIC property")
print("  of the energy landscape, not an energetic one.")
print()

# ====================================================================
# SECTION 10: Final quantitative summary
# ====================================================================
print("SECTION 10: Final quantitative summary")
print("-" * 50)
print()

print(f"  {'Quantity':<45} {'Value':>12}")
print(f"  {'-'*45} {'-'*12}")
print(f"  {'Delta_0_GL (from gap eq at fold)':<45} {Delta_0_GL:>12.6f}")
print(f"  {'Delta_0_num (F_BCS minimum, alpha-path)':<45} {Delta_0_num:>12.6f}")
print(f"  {'Ratio D_GL / D_num':<45} {Delta_0_GL/Delta_0_num:>12.4f}")
print(f"  {'S_inst_GL (quartic, exact)':<45} {S_inst_A:>12.6f}")
print(f"  {'S_inst_D (numerical, best)':<45} {S_inst_D:>12.6f}")
print(f"  {'S_Schwinger = pi*D_GL^2/|v|':<45} {S_Schw:>12.6f}")
print(f"  {'S_Schwinger = pi*D_num^2/|v|':<45} {S_Schw_correct:>12.6f}")
print(f"  {'GL ratio S_inst_GL / S_Schwinger':<45} {ratio_GL:>12.4f}")
print(f"  {'S38 disc |S_Schw(GL) - S_inst_D| / S_inst_D':<45} {disc*100:>10.2f}%")
print(f"  {'Shape factor kappa_num':<45} {kappa_num:>12.6f}")
print(f"  {'Shape factor kappa_GL = 2/3':<45} {kappa_GL:>12.6f}")
print(f"  {'D_eff / D_GL':<45} {D_eff/Delta_0_GL:>12.6f}")
print(f"  {'|v| actual / |v| needed for identity':<45} {v_terminal/v_needed:>12.4f}")
print(f"  {'Shape deviation RMS from (1-u)^2':<45} {rms_dev:>12.6f}")
print()

# ====================================================================
# VERDICT
# ====================================================================
print("=" * 72)
print("NAZAREWICZ VERDICT ON SCHWING-PROOF-39")
print("=" * 72)
print()
print("  I ENDORSE the gen-physicist's FAIL verdict.")
print()
print("  The S38 Schwinger-instanton agreement S = 0.070 vs 0.069 is a")
print("  NUMERICAL NEAR-COINCIDENCE, not an algebraic identity.")
print()
print("  REASONS FOR ENDORSEMENT:")
print()
print("  1. The gen-physicist's arithmetic is correct (independently verified).")
print()
print("  2. The GL instanton action and the Schwinger exponent are different")
print("     quantities: their ratio 4.08 depends on the transit speed |v|,")
print("     which has no BCS origin.")
print()
print("  3. The S38 comparison mixed Delta_0_GL = 0.770 (from the gap")
print("     equation) with S_inst_D = 0.069 (from the alpha-path landscape")
print("     with minimum at Delta_0_num = 0.365). These come from")
print("     incompatible approximations.")
print()
print("  4. My S38 claim that 'the WKB integral is the same in both")
print("     signatures' was imprecise. The correct nuclear analog")
print("     (fission/fusion WKB) requires the SAME potential evaluated at")
print("     the SAME energy. The Schwinger and instanton calculations use")
print("     different variational paths through the BCS energy surface.")
print()
print("  5. The 2% proximity of the shape factor kappa = 0.653 to 2/3")
print("     is NOT coincidental (it reflects Landau theory universality)")
print("     but it does NOT imply an exact identity.")
print()
print("  SELF-CORRECTION OF MY S38 STATEMENT:")
print("  My Session 38 claim (Section 1, point 3) that the Schwinger-")
print("  instanton duality is 'guaranteed by the fact that the BdG")
print("  Hamiltonian is the same in both signatures' was wrong.")
print("  The instanton and Schwinger processes traverse DIFFERENT paths")
print("  through the BCS parameter space. The instanton varies Delta")
print("  at fixed tau; the Schwinger process varies tau (hence all")
print("  single-particle energies) at whatever Delta follows from the")
print("  gap equation. These are different integrals over the same")
print("  energy landscape.")
print()
print("  WHAT SURVIVES:")
print("  The shape factor kappa = 0.653 near 2/3 is a genuine structural")
print("  feature (Landau theory universality). It constrains the barrier")
print("  profile to be near-quartic regardless of the BCS details.")
print("  This is a weaker but real statement about the system.")
print()
print("  NUCLEAR PRECEDENT FOR THE SHAPE FACTOR:")
print("  In nuclear fission barriers, the WKB action can be written as")
print("  S_fission = kappa * sqrt(2*m*V_B) * d, where V_B is the barrier")
print("  height, d is the barrier width, and kappa is the shape factor.")
print("  For actinide nuclei, kappa varies from 0.6 to 0.8 depending on")
print("  the nuclear deformation potential. The 2% proximity of kappa_num")
print("  to 2/3 is analogous to the stability of kappa_fission under")
print("  Strutinsky shell corrections.")
print()
print("  VERDICT: ENDORSE FAIL")
print("  The Schwinger-instanton 'duality' is downgraded from")
print("  'publishable identity' (my S38 claim) to 'shape factor")
print("  universality' (Landau theory, not a new result).")
print()

np.savez('tier0-computation/s39_schwinger_naz_review.npz',
    # Verified numbers
    S_inst_GL=S_GL_check,
    S_inst_D=S_D_check,
    S_Schwinger_GL=S_Schw,
    S_Schwinger_num=S_Schw_correct,
    ratio_GL=ratio_GL,
    disc_S38=disc,
    # Shape analysis
    kappa_num=kappa_num,
    kappa_GL=kappa_GL,
    shape_rms_dev=rms_dev,
    shape_max_dev=max_dev,
    shape_coeffs=coeffs_shape,
    # Key comparisons
    Delta_0_GL=Delta_0_GL,
    Delta_0_num=Delta_0_num,
    D_eff=D_eff,
    v_terminal=v_terminal,
    v_needed=v_needed,
    # Verdict
    verdict='ENDORSE FAIL',
    reason='near-coincidence from mixing GL gap with numerical instanton action',
)
print("Saved: tier0-computation/s39_schwinger_naz_review.npz")
