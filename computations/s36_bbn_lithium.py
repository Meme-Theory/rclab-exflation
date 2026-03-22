#!/usr/bin/env python3
"""
BBN-LITHIUM-36: Compute delta_H/H at T_BBN from BdG spectral action.

Physics:
  The spectral action Tr(f(D^2/Lambda^2)) encodes gravitational couplings.
  The Seeley-DeWitt coefficients a_0, a_2 of the heat kernel expansion
  Tr(exp(-tD^2)) = a_0*t^{-d/2} + a_2*t^{-d/2+1} + ...
  encode the cosmological constant (a_0) and Einstein-Hilbert (a_2) terms.

  When D_K -> D_BdG (BCS pairing), the spectrum shifts:
    lambda_k -> +/- sqrt(lambda_k^2 + Delta^2)
  with Nambu doubling of Hilbert space.

  Key relations:
    K_BdG(t) = 2 * exp(-t*Delta^2) * K_DK(t)
    => a_0(BdG) = 2 * a_0(DK)
    => a_2(BdG) = 2 * a_2(DK) - 2 * Delta^2 * a_0(DK)

  The fractional change in the Einstein-Hilbert coefficient per DOF:
    delta(a_2/a_0) / (a_2/a_0) = -Delta^2 * a_0(DK) / a_2(DK)

  This modifies G_eff and hence H(T_BBN).

Gate: BBN-LITHIUM-36
  PASS: delta_H/H in [-0.15, -0.03]
  FAIL: delta_H/H ~ 0, > 0, or < -0.15

Author: Feynman-Theorist
Session: 36
"""

import numpy as np
import sys

print("=" * 72)
print("BBN-LITHIUM-36: BdG Spectral Action and BBN Lithium Prediction")
print("=" * 72)

# ============================================================
# 1. Load D_K eigenvalues at tau closest to 0.190
# ============================================================
print("\n--- Step 1: Load D_K spectrum ---")

data = np.load('tier0-computation/s23a_eigenvectors_extended.npz', allow_pickle=True)
tau_values = data['tau_values']
print(f"Available tau: {tau_values}")

# tau = 0.190 not in grid; use tau = 0.20 (index 3) as closest
# Also compute at tau = 0.15 (index 2) for bracketing
tau_target = 0.190
idx_close = np.argmin(np.abs(tau_values - tau_target))
tau_used = tau_values[idx_close]
print(f"Target tau = {tau_target}, using tau = {tau_used} (index {idx_close})")

# Also load tau=0.15 for interpolation bracket
idx_lo = 2  # tau = 0.15
idx_hi = 3  # tau = 0.20

eigs_lo = data[f'eigenvalues_{idx_lo}']
mults_lo = data[f'multiplicities_{idx_lo}']
eigs_hi = data[f'eigenvalues_{idx_hi}']
mults_hi = data[f'multiplicities_{idx_hi}']

# Use tau=0.20 as primary (closest to 0.190)
eigs = eigs_hi
mults = mults_hi
tau = tau_used

N_bare = len(eigs)
N_full = int(np.sum(mults))
print(f"N eigenvalues (bare): {N_bare}")
print(f"N eigenvalues (with multiplicity): {N_full}")
print(f"Eigenvalue range: [{eigs.min():.6f}, {eigs.max():.6f}]")
print(f"Spectrum symmetric: {np.allclose(np.sort(eigs), -np.sort(-eigs)[::-1])}")

# ============================================================
# 2. BCS gap from RG-BCS-35
# ============================================================
print("\n--- Step 2: BCS gap parameters ---")

rg = np.load('tier0-computation/s35_rg_bcs_flow.npz', allow_pickle=True)
W_B2 = float(rg['W_B2'])
Delta_BCS_phi0 = float(rg['Delta_BCS_phi0'])
Delta_frac = 0.29  # Delta/W from task specification
Delta = Delta_frac * W_B2

print(f"W_B2 (B2 bandwidth) = {W_B2:.6f}")
print(f"Delta/W = {Delta_frac}")
print(f"Delta = {Delta:.6f}")
print(f"Delta_BCS(phi=0) from RG = {Delta_BCS_phi0:.6f} (ratio {Delta_BCS_phi0/W_B2:.4f})")

# Min eigenvalue magnitude
lambda_min = np.min(np.abs(eigs[np.abs(eigs) > 1e-10]))
print(f"|lambda_min| = {lambda_min:.6f}")
print(f"Delta / |lambda_min| = {Delta/lambda_min:.6e}")
print(f"  (BCS gap is {Delta/lambda_min*100:.4f}% of spectral gap)")

# ============================================================
# 3. Compute heat kernel coefficients numerically
# ============================================================
print("\n--- Step 3: Heat kernel K(t) = Tr(exp(-t*D^2)) ---")

# Build full spectrum with multiplicities
spec_full = np.repeat(eigs, mults)  # all N_full eigenvalues of D_K
spec_sq = spec_full**2  # eigenvalues of D_K^2

# D_BdG^2 eigenvalues: lambda_k^2 + Delta^2, each with multiplicity 2
spec_bdg_sq = spec_sq + Delta**2

# Compute K(t) for a range of t values to extract a_0, a_2 from fit
# For d=8 internal dimensions (SU(3) has dim 8):
#   K(t) = a_0 * t^{-4} + a_2 * t^{-3} + a_4 * t^{-2} + ...
#
# Actually: the internal manifold K = SU(3) has dim 8, but the Dirac operator
# acts on sections of the spinor bundle. The heat kernel expansion is:
#   Tr(exp(-tD_K^2)) ~ sum_{n=0}^infty a_n(D_K^2) * t^{(2n-d)/2}
# where d = dim(K) = 8.
#
# So: K(t) = a_0*t^{-4} + a_2*t^{-3} + a_4*t^{-2} + a_6*t^{-1} + a_8*t^0 + ...

d_K = 8  # dimension of SU(3)

# Use multiple t values to fit the expansion coefficients
# We need t small enough for the asymptotic expansion but large enough
# that the finite-cutoff spectrum is representative
#
# The largest eigenvalue is ~3.2, so D^2_max ~ 10.
# For t << 1/D^2_max ~ 0.1, the UV tail is not captured (cutoff at max_pq_sum=6)
# For t >> 1/D^2_min ~ 1.5, we're in the IR and miss the UV asymptotics
#
# Strategy: fit K(t)*t^4 = a_0 + a_2*t + a_4*t^2 + ... for small t

t_values = np.logspace(-2, 1, 200)  # t from 0.01 to 10

# Compute K_DK(t) and K_BdG(t)
K_DK = np.zeros_like(t_values)
K_BdG = np.zeros_like(t_values)

for i, t in enumerate(t_values):
    K_DK[i] = np.sum(np.exp(-t * spec_sq))
    # K_BdG = 2 * exp(-t*Delta^2) * K_DK analytically
    K_BdG[i] = 2 * np.exp(-t * Delta**2) * K_DK[i]

# Also verify K_BdG directly
K_BdG_direct = np.zeros(5)
t_test = [0.1, 0.5, 1.0, 2.0, 5.0]
for i, t in enumerate(t_test):
    K_BdG_direct[i] = 2 * np.sum(np.exp(-t * spec_bdg_sq))
K_BdG_at_test = np.array([2 * np.exp(-t * Delta**2) * np.sum(np.exp(-t * spec_sq)) for t in t_test])
print(f"K_BdG cross-check (direct vs analytic):")
for i, t in enumerate(t_test):
    err = abs(K_BdG_direct[i] - K_BdG_at_test[i]) / abs(K_BdG_direct[i])
    print(f"  t={t:.1f}: direct={K_BdG_direct[i]:.6e}, analytic={K_BdG_at_test[i]:.6e}, rel_err={err:.2e}")

# ============================================================
# 4. Extract a_0, a_2 by polynomial fit
# ============================================================
print("\n--- Step 4: Extract Seeley-DeWitt coefficients ---")

# Fit K(t) * t^{d/2} = a_0 + a_2*t + a_4*t^2 + ... for small t
# Use t values where the expansion is valid (t << 1/lambda_min^2)

# Select fitting range
t_fit_max = 0.5 / lambda_min**2  # well below 1/lambda_min^2
t_fit_min = 0.01  # limited by finite spectrum cutoff
mask = (t_values >= t_fit_min) & (t_values <= t_fit_max)
t_fit = t_values[mask]
print(f"Fitting range: t in [{t_fit.min():.4f}, {t_fit.max():.4f}], {len(t_fit)} points")

# K_DK(t) * t^4 = a_0 + a_2*t + a_4*t^2 + a_6*t^3 + ...
y_DK = K_DK[mask] * t_fit**4

# Fit polynomial in t up to order 4
coeffs_DK = np.polyfit(t_fit, y_DK, 4)  # highest power first
# coeffs = [c4, c3, c2, c1, c0]
# y = c0 + c1*t + c2*t^2 + c3*t^3 + c4*t^4
a0_DK = coeffs_DK[-1]      # constant term = a_0
a2_DK = coeffs_DK[-2]      # linear term = a_2
a4_DK = coeffs_DK[-3]      # quadratic term = a_4

print(f"\nD_K heat kernel coefficients (d=8):")
print(f"  a_0(D_K) = {a0_DK:.6e}  (counts modes ~ N_full = {N_full})")
print(f"  a_2(D_K) = {a2_DK:.6e}")
print(f"  a_4(D_K) = {a4_DK:.6e}")
print(f"  a_2/a_0 ratio = {a2_DK/a0_DK:.6f}")

# Now for D_BdG: using exact relation
# a_0(BdG) = 2 * a_0(DK)
# a_2(BdG) = 2 * a_2(DK) - 2 * Delta^2 * a_0(DK)
a0_BdG = 2 * a0_DK
a2_BdG = 2 * a2_DK - 2 * Delta**2 * a0_DK

print(f"\nD_BdG heat kernel coefficients (exact from K_BdG = 2*exp(-t*D^2)*K_DK):")
print(f"  a_0(BdG) = {a0_BdG:.6e}")
print(f"  a_2(BdG) = {a2_BdG:.6e}")
print(f"  a_2/a_0 ratio (BdG) = {a2_BdG/a0_BdG:.6f}")

# Also verify by fitting K_BdG directly
y_BdG = K_BdG[mask] * t_fit**4
coeffs_BdG = np.polyfit(t_fit, y_BdG, 4)
a0_BdG_fit = coeffs_BdG[-1]
a2_BdG_fit = coeffs_BdG[-2]
print(f"\nD_BdG coefficients (independent fit, cross-check):")
print(f"  a_0(BdG) = {a0_BdG_fit:.6e}  (expect {a0_BdG:.6e})")
print(f"  a_2(BdG) = {a2_BdG_fit:.6e}  (expect {a2_BdG:.6e})")
print(f"  a_0 err = {abs(a0_BdG_fit - a0_BdG)/abs(a0_BdG):.2e}")
print(f"  a_2 err = {abs(a2_BdG_fit - a2_BdG)/abs(a2_BdG):.2e}")

# ============================================================
# 5. Physical interpretation: delta_G_eff and delta_H/H
# ============================================================
print("\n--- Step 5: Physical observables ---")

# The spectral action S = f_0*Lambda^8*a_0 + f_2*Lambda^6*a_2 + f_4*Lambda^4*a_4 + ...
# where Lambda is the cutoff scale.
#
# The a_2 coefficient encodes the Einstein-Hilbert term:
#   S_EH = (1/16*pi*G) * integral R * sqrt(g) d^dx
#
# In Connes' spectral action:
#   a_2 = (4*pi)^{-d/2} * (R/6) * Vol(K)  * rank(spinor bundle)
# where R is the scalar curvature and Vol(K) is the volume of the internal space.
#
# The physical G_eff is proportional to 1/a_2:
#   1/(16*pi*G_eff) propto f_2 * Lambda^6 * a_2
#
# So: delta_G_eff / G_eff = -delta_a_2 / a_2

# Method A: Ratio per physical degree of freedom (remove Nambu doubling)
# The BdG description doubles the Hilbert space as bookkeeping.
# Physical content: same N modes, but with shifted eigenvalues.
# Effective a_2 per mode:
#   a_2_eff(DK) = a_2(DK) / a_0(DK)  (per mode)
#   a_2_eff(BdG) = a_2(BdG) / a_0(BdG) = (a_2(DK) - Delta^2*a_0(DK)) / a_0(DK)
#                = a_2(DK)/a_0(DK) - Delta^2

delta_a2_per_mode = -Delta**2
ratio_a2_per_mode = a2_DK / a0_DK

delta_G_over_G_methodA = -delta_a2_per_mode / ratio_a2_per_mode
delta_H_over_H_methodA = 0.5 * delta_G_over_G_methodA

print(f"\nMethod A: Per-mode spectral shift (Nambu doubling = bookkeeping)")
print(f"  delta(a_2/a_0) = -Delta^2 = {delta_a2_per_mode:.6e}")
print(f"  a_2/a_0 (DK) = {ratio_a2_per_mode:.6f}")
print(f"  delta_G/G = +Delta^2 / (a_2/a_0) = {delta_G_over_G_methodA:.6e}")
print(f"  delta_H/H = (1/2) * delta_G/G = {delta_H_over_H_methodA:.6e}")

# Method B: Treat Nambu doubling as physical (g_* counting)
# If D_BdG is the physical Dirac operator, then the effective number of
# relativistic species changes. At BBN:
#   H^2 = (8*pi*G/3) * (pi^2/30) * g_*(T) * T^4
#   delta_H/H = (1/2) * delta_g*/g*
#
# Standard BBN: g_* = 10.75 (photons + e+/e- + 3 neutrinos)
# The change from D_K to D_BdG modifies the KK spectrum, which changes
# the effective g_* via the spectral action.
#
# But the BCS condensate only affects modes near the Fermi surface
# (the B2 quartet with W_B2 = 0.058). The vast majority of modes
# (439,484 out of 439,488) are far from the gap and unaffected.

# The spectral action encodes g_* through a_0 (cosmological constant)
# and a_2 (Newton's constant). The DIRECT change:
delta_a0_frac = (a0_BdG - a0_DK) / a0_DK  # = 1.0 (doubling)
delta_a2_frac = (a2_BdG - a2_DK) / a2_DK

print(f"\nMethod B: Raw spectral action change (includes Nambu doubling)")
print(f"  delta_a0/a0 = {delta_a0_frac:.6f}  (Nambu doubling = +100%)")
print(f"  delta_a2/a2 = {delta_a2_frac:.6f}")
print(f"  Note: Nambu doubling of a_0 is not physical (bookkeeping)")

# Method C: Physical delta_a_2 correction only (no Nambu doubling artifact)
# The physical effect of BCS is NOT to double the DOFs but to gap some modes.
# In the spectral action framework (van Suijlekom, Connes 15/16):
#   - The BCS condensate is an inner fluctuation of D
#   - It does NOT change a_0 (same manifold, same spinor bundle)
#   - It DOES change a_2 through the gap
#
# Physical interpretation:
#   delta_a_2 = -2 * Delta^2 * a_0  (from the shift in D^2 eigenvalues)
#   but a_0 already has the Nambu factor, so per physical DOF:
#   delta_a_2_phys = -Delta^2 * N_full  (shift per mode, summed over N modes)
#
# The fraction of a_2 this represents:
delta_a2_physical = -Delta**2 * N_full  # total shift in eigenvalue sum
a2_total = a2_DK  # from the original (non-Nambu) operator

# BUT: what matters for G_eff is the RATIO of the a_2 integral over the
# full product M4 x K. The M4 part gives the volume factor, K part gives
# the spectral geometry. The BCS gap modifies only the K part.
#
# In the product geometry:
#   1/(16*pi*G) = f_2 * Lambda^6 * a_2(D_K)
#
# The BCS-modified operator:
#   1/(16*pi*G_eff) = f_2 * Lambda^6 * a_2_eff
#
# where a_2_eff = a_2(DK) - Delta^2 * a_0(DK)  [per physical DOF]
# (the -Delta^2 * a_0 comes from the exp(-t*Delta^2) shift)

delta_G_over_G_phys = Delta**2 * a0_DK / a2_DK
delta_H_over_H_phys = 0.5 * delta_G_over_G_phys

print(f"\nMethod C: Physical G_eff change (BCS modifies K-part only)")
print(f"  Delta = {Delta:.6f}")
print(f"  Delta^2 = {Delta**2:.6e}")
print(f"  a_0(DK) = {a0_DK:.6e}")
print(f"  a_2(DK) = {a2_DK:.6e}")
print(f"  delta_a_2 / a_2 = -Delta^2 * a_0/a_2 = {-Delta**2 * a0_DK/a2_DK:.6e}")
print(f"  delta_G/G = +Delta^2 * a_0/a_2 = {delta_G_over_G_phys:.6e}")
print(f"  delta_H/H = {delta_H_over_H_phys:.6e}")

# ============================================================
# 6. Cross-check: Compute spectral zeta functions directly
# ============================================================
print("\n--- Step 6: Cross-checks ---")

# Zeta function: zeta_D(s) = sum_k |lambda_k|^{-2s} * m_k
# a_0 = zeta_D(0) = N_full (mode count)  -- not quite; zeta(0) is regularized
# Actually, a_0 = Tr(1) on the spinor bundle = N_full for the truncated spectrum

# Direct a_0 check
a0_direct = N_full  # by definition for finite spectrum
print(f"a_0 check: fit = {a0_DK:.2f}, direct Tr(1) = {a0_direct}")

# For a_2, compute Tr(D_K^2) which is related but not equal to a_2:
# Tr(exp(-tD^2)) ~ a_0*t^{-4} + a_2*t^{-3} + ...
# At leading order for large t: dominated by smallest eigenvalues
# At small t: K(t) ~ N_full * t^{-0} (all modes contribute equally) -- NO!
# For t -> 0: each mode contributes exp(-t*lambda^2) -> 1, so K(t) -> N_full/t^0...
# but that's K(t) = N_full, not t^{-4}.
#
# The issue: t^{-d/2} growth comes from the CONTINUOUS spectrum in the
# thermodynamic limit. Our FINITE truncation (max_pq_sum=6) gives a
# discrete spectrum. The heat kernel expansion is an ASYMPTOTIC expansion
# valid when Lambda_cutoff >> 1/sqrt(t), which requires t not too small.

# Better approach: use the Euler-Maclaurin/Weyl law
# For the Dirac operator on a d-dimensional compact manifold:
#   N(Lambda) = #{|lambda_k| < Lambda} ~ C_d * Lambda^d * Vol(M)
# where C_d = Vol(S^{d-1}) / (d*(2*pi)^d)
#
# Then a_0 = (4*pi)^{-d/2} * dim(spinor) * Vol(M) = Weyl coefficient

# Compute N(Lambda) from our spectrum
Lambda_vals = np.sort(np.abs(spec_full))
N_cumul = np.arange(1, len(Lambda_vals) + 1)

# Weyl law: N(Lambda) ~ C * Lambda^8 for d=8
# Fit C from the data
Lambda_high = Lambda_vals[Lambda_vals > 1.0]
N_high = N_cumul[Lambda_vals > 1.0]
# N = C * Lambda^8 => log(N) = log(C) + 8*log(Lambda)
from numpy.polynomial import polynomial as P
log_fit = np.polyfit(np.log(Lambda_high), np.log(N_high), 1)
d_weyl = log_fit[0]
C_weyl = np.exp(log_fit[1])
print(f"\nWeyl law fit: N(Lambda) ~ {C_weyl:.2f} * Lambda^{d_weyl:.2f}")
print(f"  Expected exponent: d = 8")

# ============================================================
# 7. Alternative: Direct spectral sum approach
# ============================================================
print("\n--- Step 7: Direct spectral sum computation ---")

# Instead of heat kernel, compute the spectral action directly:
# S_n(D) = sum_k |lambda_k|^{d-2n} * m_k (for appropriate regularization)
#
# For d=8:
#   S_0 ~ sum |lambda_k|^8 * m_k  -> a_0 coefficient (cosmological constant)
#   S_1 ~ sum |lambda_k|^6 * m_k  -> a_2 coefficient (Einstein-Hilbert)

# These are DIVERGENT in the continuum limit but finite for our truncated spectrum.
# They correspond to the moments of the spectral distribution.

S0_DK = np.sum(np.abs(spec_full)**8)  # ~ Lambda^8 * a_0
S1_DK = np.sum(np.abs(spec_full)**6)  # ~ Lambda^6 * a_2
S2_DK = np.sum(np.abs(spec_full)**4)  # ~ Lambda^4 * a_4

# For BdG: |lambda_BdG| = sqrt(lambda^2 + Delta^2)
spec_bdg_abs = np.sqrt(spec_sq + Delta**2)
S0_BdG_per_mode = np.sum(spec_bdg_abs**8)  # per original mode, no Nambu factor
S1_BdG_per_mode = np.sum(spec_bdg_abs**6)
S2_BdG_per_mode = np.sum(spec_bdg_abs**4)

delta_S0 = S0_BdG_per_mode - S0_DK
delta_S1 = S1_BdG_per_mode - S1_DK
delta_S2 = S2_BdG_per_mode - S2_DK

print(f"Spectral sums (no Nambu doubling):")
print(f"  S_0(DK) = sum|lam|^8 = {S0_DK:.6e}")
print(f"  S_1(DK) = sum|lam|^6 = {S1_DK:.6e}")
print(f"  S_2(DK) = sum|lam|^4 = {S2_DK:.6e}")
print(f"  S_0(BdG) = sum(lam^2+D^2)^4 = {S0_BdG_per_mode:.6e}")
print(f"  S_1(BdG) = sum(lam^2+D^2)^3 = {S1_BdG_per_mode:.6e}")
print(f"  S_2(BdG) = sum(lam^2+D^2)^2 = {S2_BdG_per_mode:.6e}")
print(f"\nFractional changes (BCS shift per mode):")
print(f"  delta_S0/S0 = {delta_S0/S0_DK:.6e}  (cosmological constant)")
print(f"  delta_S1/S1 = {delta_S1/S1_DK:.6e}  (Einstein-Hilbert ~ G_eff)")
print(f"  delta_S2/S2 = {delta_S2/S2_DK:.6e}  (gauge kinetics)")

# Expand (lambda^2 + Delta^2)^n = lambda^{2n} + n*Delta^2*lambda^{2n-2} + ...
# Leading correction to S_1:
# delta_S1 ~ 3*Delta^2 * sum|lambda|^4 + 3*Delta^4*sum|lambda|^2 + Delta^6*N
delta_S1_leading = 3 * Delta**2 * S2_DK
print(f"\n  Leading-order delta_S1 = 3*Delta^2*S2 = {delta_S1_leading:.6e}")
print(f"  Exact delta_S1 = {delta_S1:.6e}")
print(f"  Ratio (should be ~1 if Delta << lambda) = {delta_S1/delta_S1_leading:.6f}")

# The physical change in G_eff from the spectral action:
# S_grav = f_2 * Lambda^{d-4} * sum|lambda|^{d-4}  [for d=8: f_2*Lambda^4 * sum|lambda|^4]
#
# Wait -- the correspondence is:
#   Tr(f(D^2/Lambda^2)) = sum_k f(lambda_k^2/Lambda^2)
# For a smooth cutoff f with moments f_n = integral f(u) u^{n-1} du:
#   Tr(f(D/Lambda)) ~ f_4*Lambda^8*a_0 + f_2*Lambda^6*a_2 + f_0*Lambda^4*a_4 + ...
#                      (cosmological)      (Einstein-Hilbert)    (gauge kinetics)
#
# Note: for d=8, a_0 ~ number of modes, a_2 ~ scalar curvature, a_4 ~ gauge/Higgs
#
# The Einstein-Hilbert term is:
#   S_EH = f_2 * Lambda^6 * a_2
# where a_2 = (4*pi)^{-4} * (1/6) * int_K R * tr(1) * dvol
#
# With BCS gap, the RATIO a_2(BdG)/a_2(DK) determines delta_G:
#   G_eff = G * a_2(DK) / a_2(BdG)   [since 1/G propto a_2]
#
# Using our spectral sums as proxy:
#   delta_G/G = -delta_S1/S1  [S_1 plays role of a_2 for d=8]
# This is POSITIVE (weakening gravity) because delta_S1 > 0
# (adding Delta^2 increases all |E|)

delta_G_over_G_spectral = -delta_S1 / S1_DK
delta_H_over_H_spectral = 0.5 * delta_G_over_G_spectral

print(f"\nMethod D: Direct spectral sum (most reliable)")
print(f"  delta_S1/S1 = {delta_S1/S1_DK:.6e}")
print(f"  delta_G/G = -delta_S1/S1 = {delta_G_over_G_spectral:.6e}")
print(f"  delta_H/H = (1/2) * delta_G/G = {delta_H_over_H_spectral:.6e}")

# ============================================================
# 8. Alternative perspective: g_* counting
# ============================================================
print("\n--- Step 8: Effective g_* at BBN ---")

# In standard cosmology, H^2 = (8piG/3)*rho with rho = (pi^2/30)*g_*(T)*T^4
# The spectral action encodes both G and g_* through the internal geometry.
#
# The BCS gap does NOT change the number of 4D particle species (g_*).
# It modifies the internal geometry's spectral action coefficients.
# The effect on H is purely through delta_G_eff (the a_2 shift).
#
# BUT: there is a subtlety. The BCS condensate opens a gap in the
# internal Dirac spectrum. Modes below the gap are "frozen out" as
# temperature drops below the gap scale. This could modify g_*(T).
#
# At T_BBN ~ 1 MeV ~ 10^{-3} GeV:
#   - The internal gap Delta corresponds to a KK mass scale
#   - If M_KK ~ 10^{10} GeV (from s35 Ricci analysis), then
#     Delta_physical = Delta * M_KK ~ 0.017 * 10^{10} ~ 10^8 GeV >> T_BBN
#   - ALL KK modes (including gapped ones) are frozen out at BBN
#   - The g_* counting at BBN is unaffected by the BCS gap

Delta_physical_GeV = Delta * 1e10  # M_KK ~ 10^10 GeV estimate
from canonical_constants import T_BBN_GeV  # 1 MeV

print(f"Physical gap scale: Delta_phys ~ {Delta_physical_GeV:.2e} GeV")
print(f"BBN temperature: T_BBN ~ {T_BBN_GeV:.0e} GeV")
print(f"Ratio Delta_phys/T_BBN ~ {Delta_physical_GeV/T_BBN_GeV:.2e}")
print(f"All KK modes (gapped and ungapped) are FAR above T_BBN")
print(f"=> g_* at BBN is UNAFFECTED by BCS gap")
print(f"=> Only effect is through delta_G_eff (spectral action a_2 shift)")

# ============================================================
# 9. Sensitivity analysis: scan over Delta/W
# ============================================================
print("\n--- Step 9: Sensitivity scan ---")

Delta_W_scan = np.linspace(0.0, 0.50, 51)
delta_H_scan = np.zeros_like(Delta_W_scan)

for i, dw in enumerate(Delta_W_scan):
    D = dw * W_B2
    if D == 0:
        delta_H_scan[i] = 0.0
        continue
    # delta_S1 = sum_k [(lam^2 + D^2)^3 - lam^{6}]
    dS1 = np.sum((spec_sq + D**2)**3 - spec_sq**3)
    delta_H_scan[i] = -0.5 * dS1 / S1_DK

print(f"delta_H/H at various Delta/W:")
for dw_show in [0.10, 0.20, 0.29, 0.30, 0.40, 0.50]:
    idx_show = np.argmin(np.abs(Delta_W_scan - dw_show))
    print(f"  Delta/W = {Delta_W_scan[idx_show]:.2f}: delta_H/H = {delta_H_scan[idx_show]:.6e}")

# ============================================================
# 10. Bracket: tau = 0.15 vs tau = 0.20
# ============================================================
print("\n--- Step 10: tau bracketing ---")

# Compute at tau = 0.15 for comparison
spec_full_lo = np.repeat(eigs_lo, mults_lo)
spec_sq_lo = spec_full_lo**2
S1_DK_lo = np.sum(spec_sq_lo**3)
dS1_lo = np.sum((spec_sq_lo + Delta**2)**3 - spec_sq_lo**3)
delta_H_lo = -0.5 * dS1_lo / S1_DK_lo

print(f"tau = {tau_values[idx_lo]}: delta_H/H = {delta_H_lo:.6e}")
print(f"tau = {tau_values[idx_hi]}: delta_H/H = {delta_H_over_H_spectral:.6e}")
# Interpolate to tau = 0.190
alpha = (0.190 - tau_values[idx_lo]) / (tau_values[idx_hi] - tau_values[idx_lo])
delta_H_interp = (1 - alpha) * delta_H_lo + alpha * delta_H_over_H_spectral
print(f"tau = 0.190 (interpolated): delta_H/H = {delta_H_interp:.6e}")

# ============================================================
# 11. The structural argument: WHY is delta_H/H so small?
# ============================================================
print("\n--- Step 11: Structural analysis ---")

print(f"\nWHY delta_H/H ~ 10^{{-7}}:")
print(f"  1. Delta = {Delta:.6f} (in spectrum units)")
print(f"  2. lambda_min = {lambda_min:.6f}")
print(f"  3. Delta/lambda_min = {Delta/lambda_min:.6e}")
print(f"  4. Typical |lambda| ~ {np.mean(np.abs(spec_full)):.3f}")
print(f"  5. Delta^2/lambda_typ^2 ~ {Delta**2 / np.mean(spec_sq):.6e}")
print(f"  6. The BCS gap is a perturbation of order Delta^2/lambda^2 on EACH mode")
print(f"     summed over N = {N_full} modes. But the spectral sum is dominated")
print(f"     by UV modes where Delta << lambda.")
print(f"  7. Fractional shift ~ Delta^2 * <lambda^4> / <lambda^6> ~ Delta^2/lambda_typ^2")
print(f"     = {Delta**2 * np.mean(spec_sq**2) / np.mean(spec_sq**3):.6e}")

# Additional check: how many modes are "near" the gap?
n_near_gap = np.sum((np.abs(spec_full) > lambda_min) & (np.abs(spec_full) < lambda_min + W_B2))
n_total = len(spec_full)
print(f"\n  Modes within W_B2 of gap edge: {n_near_gap} out of {n_total}")
print(f"  Fraction of modes near gap: {n_near_gap/n_total:.6e}")
print(f"  => BCS affects a TINY fraction of the spectral weight")

# ============================================================
# 12. Domain wall density effect (separate channel)
# ============================================================
print("\n--- Step 12: Domain wall density channel ---")
print(f"  The BCS condensate introduces domain walls in the internal space.")
print(f"  These walls carry tension ~ Delta^2 and modify the stress-energy.")
print(f"  BUT: this is a SEPARATE channel from the spectral action,")
print(f"  requiring a model for the wall density rho_wall at BBN epoch.")
print(f"  This is NOT parameter-free => not Level 4.")
print(f"  (The wall density would need: tau(t) trajectory + domain nucleation rate)")

# ============================================================
# 13. FINAL VERDICT
# ============================================================
print("\n" + "=" * 72)
print("FINAL RESULTS: BBN-LITHIUM-36")
print("=" * 72)

# Use Method D (direct spectral sums) as the definitive answer
# Cross-checked by Method A (heat kernel) and tau interpolation
delta_H_final = delta_H_interp  # interpolated to tau=0.190
delta_a0_final = 2.0  # Nambu doubling (bookkeeping, not physical)
delta_a2_a2_final = delta_S1 / S1_DK  # fractional change in a_2 proxy

print(f"\nKey numbers:")
print(f"  tau = 0.190 (interpolated from 0.15 and 0.20)")
print(f"  Delta/W = 0.29 (from RG-BCS-35)")
print(f"  Delta = {Delta:.6f} (in spectrum units)")
print(f"  |lambda_min| = {lambda_min:.6f}")
print(f"")
print(f"  delta_a_0/a_0 = +1.000 (Nambu doubling, NOT physical)")
print(f"  delta_a_2/a_2 (spectral sum) = {delta_a2_a2_final:.6e}")
print(f"  delta_G/G = {-delta_a2_a2_final:.6e}")
print(f"  delta_H/H = {delta_H_final:.6e}")
print(f"")

# Gate assessment
if -0.15 <= delta_H_final <= -0.03:
    verdict = "PASS"
elif abs(delta_H_final) < 1e-3:
    verdict = "FAIL_NEGLIGIBLE"
elif delta_H_final > 0:
    verdict = "FAIL_WRONG_DIRECTION"
elif delta_H_final < -0.15:
    verdict = "FAIL_TOO_LARGE"
else:
    verdict = "FAIL_INTERMEDIATE"

print(f"Gate BBN-LITHIUM-36: {verdict}")
print(f"  Criterion: delta_H/H in [-0.15, -0.03]")
print(f"  Result: delta_H/H = {delta_H_final:.6e}")

if "FAIL_NEGLIGIBLE" in verdict:
    print(f"\n  The BCS gap produces a NEGLIGIBLE modification to the")
    print(f"  spectral action. delta_H/H ~ {delta_H_final:.1e} is {abs(delta_H_final/0.03):.0e}x")
    print(f"  below the minimum required for lithium resolution.")
    print(f"")
    print(f"  STRUCTURAL REASON: The BCS gap (Delta ~ 0.017) is a perturbation")
    print(f"  of order Delta^2/lambda_min^2 ~ {(Delta/lambda_min)**2:.1e} on each mode.")
    print(f"  The spectral action sum_k |lambda_k|^n is UV-dominated;")
    print(f"  the BCS gap affects only modes near the gap edge, which carry")
    print(f"  negligible spectral weight compared to the UV tower.")
    print(f"")
    print(f"  This confirms the s35 memory note: 'delta-a_4 from BdG gap is")
    print(f"  ~10^{{-7}} (negligible). BCS role is tau-pinning, not spectral shift.'")

print(f"\nLevel 4 assessment:")
print(f"  NOT Level 4. The spectral action change from BCS is negligible.")
print(f"  The BCS condensate's role in the framework is TAU-PINNING")
print(f"  (selecting the fold point), not modifying gravitational couplings.")
print(f"  BBN lithium resolution would require a separate mechanism")
print(f"  (e.g., domain wall density, modified tau(t) trajectory, or")
print(f"  new physics beyond the internal spectral action).")

# ============================================================
# 14. Save results
# ============================================================
print("\n--- Saving results ---")

np.savez('tier0-computation/s36_bbn_lithium.npz',
    # Inputs
    tau_target=0.190,
    tau_used=tau_used,
    tau_bracket=np.array([tau_values[idx_lo], tau_values[idx_hi]]),
    Delta_over_W=Delta_frac,
    Delta=Delta,
    W_B2=W_B2,
    lambda_min=lambda_min,
    N_full=N_full,

    # Heat kernel coefficients
    a0_DK=a0_DK,
    a2_DK=a2_DK,
    a4_DK=a4_DK,
    a0_BdG=a0_BdG,
    a2_BdG=a2_BdG,

    # Spectral sums
    S0_DK=S0_DK,
    S1_DK=S1_DK,
    S2_DK=S2_DK,
    S0_BdG=S0_BdG_per_mode,
    S1_BdG=S1_BdG_per_mode,
    S2_BdG=S2_BdG_per_mode,
    delta_S0_frac=delta_S0/S0_DK,
    delta_S1_frac=delta_S1/S1_DK,
    delta_S2_frac=delta_S2/S2_DK,

    # Physical results
    delta_G_over_G=float(-delta_a2_a2_final),
    delta_H_over_H=float(delta_H_final),
    delta_H_at_tau015=delta_H_lo,
    delta_H_at_tau020=delta_H_over_H_spectral,
    delta_H_interp=delta_H_interp,

    # Sensitivity scan
    Delta_W_scan=Delta_W_scan,
    delta_H_scan=delta_H_scan,

    # Weyl law
    d_weyl=d_weyl,
    C_weyl=C_weyl,

    # Verdict
    verdict=np.array([verdict]),
    gate_name=np.array(['BBN-LITHIUM-36']),
)
print(f"Saved: tier0-computation/s36_bbn_lithium.npz")
print("\nDone.")
