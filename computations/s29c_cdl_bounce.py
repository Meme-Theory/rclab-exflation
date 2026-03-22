#!/usr/bin/env python3
"""
29c-3: Coleman-De Luccia Bounce Action for BCS First-Order Transition
=====================================================================

Physics:
    The L-9 gate established that modulus trapping requires a first-order
    transition (smooth V_eff is monotonically decreasing, no minimum).
    The BCS condensation provides a discontinuous free energy jump at the
    condensation point, creating an effective barrier.

    The Coleman-De Luccia (CDL) bounce computes the tunneling rate from
    the false vacuum (normal phase, high tau) to the true vacuum (BCS phase,
    tau ~ 0.35). The O(4)-symmetric bounce equation is:

        d^2 phi/dr^2 + (3/r) dphi/dr = dV/dphi

    where phi = tau (the modulus), r is the O(4) radial coordinate,
    and V(tau) is the effective potential including BCS condensation energy.

    The bounce action B determines the tunneling rate: Gamma ~ exp(-B).
    If B < 400 (roughly), tunneling completes within a Hubble time.
    If B > 400, the false vacuum is metastable.

Method:
    1. Construct V_eff(tau) from spectral action + BCS free energy:
       V_normal(tau) = S_spectral(tau)  [from s28a]
       V_BCS(tau) = S_spectral(tau) + F_BCS(tau)  [from s28b/s29b]
    2. The barrier is at the BCS onset: tau where F_BCS first becomes negative
    3. Solve the O(4) bounce equation using shooting method
    4. Compute B = S_E[bounce] - S_E[false vacuum]
    5. Compare B to 400 threshold

Inputs:
    tier0-computation/s28a_spectral_action_comparison.npz
    tier0-computation/s28b_self_consistent_tau_T.npz
    tier0-computation/s29b_free_energy_comparison.npz

Outputs:
    tier0-computation/s29c_cdl_bounce.npz
    tier0-computation/s29c_cdl_bounce.png
"""

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp, quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# ==============================================================================
# Load data
# ==============================================================================

data_dir = os.path.join(os.path.dirname(__file__))

spec = np.load(os.path.join(data_dir, 's28a_spectral_action_comparison.npz'), allow_pickle=True)
bcs_data = np.load(os.path.join(data_dir, 's29b_free_energy_comparison.npz'), allow_pickle=True)
sc_data = np.load(os.path.join(data_dir, 's28b_self_consistent_tau_T.npz'), allow_pickle=True)

# Spectral action: use the HEAT KERNEL cutoff at Lambda=1 (Levi-Civita),
# which is the physically relevant spectral action used in 29b.
# S_LC_total_sharp[3] (Lambda=10) is FLAT (all eigenvalues below cutoff at all tau)
# and must NOT be used as V_normal.
tau_spec = spec['tau_values']  # (21,) [0, 0.5]
# Use Levi-Civita total with heat kernel cutoff at Lambda=1
S_spectral = spec['S_LC_total_heat'][0]  # Lambda index 0 = Lambda=1, shape (21,)

# BCS free energy
tau_bcs = bcs_data['tau_bcs']  # (9,) [0, 0.5]
F_bcs_s1 = bcs_data['F_bcs_scenario1']  # mu = lambda_min
F_bcs_s2 = bcs_data['F_bcs_scenario2']  # mu = 1.2*lambda_min
F_normal = bcs_data['F_normal']          # = S_spectral at BCS tau values (same as S_LC_total_heat[0])

# Verify consistency: F_normal should match S_spectral at BCS tau points
S_at_bcs_tau = np.interp(tau_bcs, tau_spec, S_spectral)
max_mismatch = np.max(np.abs(S_at_bcs_tau - F_normal))
print(f"S_spectral vs F_normal mismatch: {max_mismatch:.4e}")
if max_mismatch > 1.0:
    print(f"WARNING: S_spectral and F_normal disagree by {max_mismatch:.2f}. Check Lambda choice.")

print("=" * 70)
print("29c-3: CDL BOUNCE ACTION FOR BCS FIRST-ORDER TRANSITION")
print("=" * 70)

# ==============================================================================
# Construct effective potential
# ==============================================================================

# The spectral action S(tau) is the "normal phase" potential.
# In the BCS phase, V_BCS(tau) = S(tau) + F_BCS(tau), where F_BCS < 0 in the
# condensed region.
#
# For the CDL bounce, we need V(tau) as a continuous function.
# The "false vacuum" is the normal phase at large tau (tau -> infinity, or tau = 0.5
# as our boundary), and the "true vacuum" is the BCS phase at tau_min.

# Interpolate the spectral action to a fine grid
S_interp = CubicSpline(tau_spec, S_spectral)

# Scenario 1: mu = lambda_min (physical)
# F_BCS is only nonzero where condensation occurs
# Need to interpolate F_BCS(tau) between the sparse tau_bcs points
F_bcs_s1_interp = CubicSpline(tau_bcs, F_bcs_s1, bc_type='natural')

# The effective potential: V_eff(tau) = S(tau) + F_BCS(tau) in BCS phase
# In normal phase: V_eff(tau) = S(tau)
# The BCS condensation turns on at some critical tau.

# From the data: F_BCS is most negative at tau=0.0 (-13.05) for scenario 1,
# and at tau=0.35 (-18.56) for scenario 2.
# The BCS phase has lower energy wherever F_BCS < 0.

# For the CDL bounce, the key potential is V_normal - V_BCS = -F_BCS > 0
# This is the energy difference between the two phases.

# Let's construct both potentials on a fine grid
tau_fine = np.linspace(0.0, 0.5, 2001)
dt = tau_fine[1] - tau_fine[0]

V_normal = S_interp(tau_fine)
F_bcs_fine_s1 = F_bcs_s1_interp(tau_fine)
F_bcs_fine_s2 = CubicSpline(tau_bcs, F_bcs_s2, bc_type='natural')(tau_fine)

# Clip: BCS free energy should be <= 0 (or 0 where no condensation)
# Actually, F_BCS can be 0 at some tau values (no condensation there)
# The spline might produce positive values in non-condensing regions
F_bcs_fine_s1 = np.minimum(F_bcs_fine_s1, 0.0)
F_bcs_fine_s2 = np.minimum(F_bcs_fine_s2, 0.0)

V_BCS_s1 = V_normal + F_bcs_fine_s1  # True vacuum potential (lower)
V_BCS_s2 = V_normal + F_bcs_fine_s2

print("\nPotential landscape (Scenario 1, mu=lambda_min):")
print(f"  V_normal(0.0) = {V_normal[0]:.2f}")
print(f"  V_normal(0.5) = {V_normal[-1]:.2f}")
print(f"  V_BCS(0.0)    = {V_BCS_s1[0]:.2f}")
print(f"  V_BCS(0.35)   = {V_BCS_s1[int(0.35/dt)]:.2f}")
print(f"  Delta V_max   = {-F_bcs_fine_s1.min():.4f}")

# ==============================================================================
# CDL Bounce: O(4) Symmetric Solution
# ==============================================================================
# The bounce equation: phi'' + (3/r)*phi' = dV/dphi
# with BCs: phi'(0) = 0, phi(r->inf) -> false vacuum
#
# In our case, the potential landscape is more complex because V_normal
# is not a simple double-well. Instead, the BCS condensation creates
# a discontinuous jump. For the thin-wall approximation:
#   B_thin_wall = 27*pi^2 * sigma^4 / (2 * epsilon^3)
# where sigma = surface tension and epsilon = energy difference.
#
# For the thick-wall case, we need to solve numerically.

# First: construct the CDL potential
# The modulus tau rolls in V_normal. The BCS condensation provides a
# "pocket" of lower energy. The bounce interpolates between the two.
#
# We model this as a 1D potential V(tau) where:
# V(tau) = V_normal(tau) for tau > tau_c (normal phase, false vacuum side)
# V(tau) = V_BCS(tau) for tau < tau_c (BCS phase, true vacuum side)
# The barrier is at tau_c where V_normal = V_BCS + barrier_height.

# Since V_normal is monotonically decreasing and V_BCS is also decreasing
# but with a deeper well, the "false vacuum" is at high tau and "true vacuum"
# at the BCS minimum.

# For CDL bounce in curved space (Euclidean de Sitter):
# B = B_flat - (gravitational corrections)
# But for our case, the potential is in field space (internal modulus),
# not in the inflaton. The gravitational correction goes as epsilon / M_Pl^4,
# which is tiny for internal-space energies.

# Strategy: Use the bounce action in flat space as the leading term.

# ==============================================================================
# Method 1: Thin-wall approximation
# ==============================================================================

# For the thin-wall limit:
# B = 27*pi^2 * sigma^4 / (2 * epsilon^3)
# where:
# epsilon = V_false - V_true  (energy difference between vacua)
# sigma = integral of sqrt(2*(V - V_true)) dtau across the barrier

# Use Scenario 1 (mu = lambda_min) as primary
# The kinetic term for tau: L_kin = (1/2) G_{tau tau} (dtau/dt)^2
# From s29b: G_tau_tau = 5.0
G_tau_tau = 5.0  # metric on moduli space

# The "false vacuum" is at the far side (large tau where BCS doesn't condense).
# For scenario 1: F_BCS is most negative at tau=0 and near tau=0.5.
# The BCS condensation occurs wherever |Delta| > 0.

# Let's identify the key features:
# - True vacuum: tau where V_BCS is minimum
# - False vacuum: tau where the modulus would sit without BCS
#   (Since V_normal is monotonic, there's no stable point. The "false vacuum"
#   is really the would-be trajectory endpoint at tau -> large.)

# For a more physical picture:
# The modulus starts at tau=0 and rolls. BCS condensation creates a potential
# well. The question is whether the modulus gets trapped.
# The CDL bounce describes tunneling INTO the well from outside.
# But actually, from the K-29c result, the modulus is ROLLING THROUGH.
# The question is: can the first-order BCS transition capture it?

# Revised picture: The modulus rolls through the potential. At tau_BCS,
# the BCS condensation suddenly turns on (first-order). The latent heat
# released must exceed the kinetic energy for trapping (L-9 condition).

# The CDL bounce is relevant if the modulus overshoots and we need
# quantum tunneling back into the BCS well. But the primary trapping
# mechanism is classical energy balance.

# Let's compute both:
# (a) Classical trapping condition: L > KE
# (b) CDL bounce action for quantum tunneling back if overshoots

print("\n" + "=" * 50)
print("Thin-wall approximation:")
print("=" * 50)

# For each scenario, compute B_thin_wall
for label, F_bcs_fine, F_bcs_raw in [
    ("mu=lambda_min", F_bcs_fine_s1, F_bcs_s1),
    ("mu=1.2*lambda_min", F_bcs_fine_s2, F_bcs_s2)
]:
    # Energy difference: epsilon = -F_BCS at minimum
    epsilon = -F_bcs_fine.min()

    if epsilon < 1e-10:
        print(f"\n  {label}: No BCS well (epsilon = {epsilon:.2e})")
        continue

    # True vacuum location
    idx_true = np.argmin(F_bcs_fine)
    tau_true = tau_fine[idx_true]

    # For the barrier profile, we need V(tau) - V_true
    # V_true = V_BCS at true vacuum
    V_true = V_normal[idx_true] + F_bcs_fine[idx_true]

    # The barrier is at the edge of the BCS region
    # Find where F_BCS transitions from 0 to negative
    bcs_onset_mask = F_bcs_fine < -1e-6
    if not bcs_onset_mask.any():
        print(f"\n  {label}: No clear BCS onset")
        continue

    # Surface tension: sigma = integral of sqrt(2 * G_tau_tau * (V - V_true)) dtau
    # through the barrier region
    V_barrier = V_normal - V_true  # potential above true vacuum, in normal phase
    V_barrier_bcs = (V_normal + F_bcs_fine) - V_true  # in BCS phase

    # The integrand for sigma: use the BCS potential profile
    integrand = np.sqrt(2.0 * G_tau_tau * np.maximum(V_barrier_bcs, 0.0))
    sigma = np.trapezoid(integrand, tau_fine)

    # Thin-wall bounce action
    if epsilon > 0:
        B_thin = 27.0 * np.pi**2 * sigma**4 / (2.0 * epsilon**3)
    else:
        B_thin = np.inf

    print(f"\n  {label}:")
    print(f"    True vacuum at tau = {tau_true:.3f}")
    print(f"    epsilon (energy diff) = {epsilon:.4f}")
    print(f"    sigma (surface tension) = {sigma:.4f}")
    print(f"    B_thin_wall = {B_thin:.2f}")
    print(f"    B < 400? {'YES' if B_thin < 400 else 'NO'}")
    print(f"    Gamma/H^4 ~ exp(-{B_thin:.0f})")

# ==============================================================================
# Method 2: Numerical bounce (shooting method)
# ==============================================================================

print("\n" + "=" * 50)
print("Numerical CDL bounce (O(4) shooting):")
print("=" * 50)

# Work with Scenario 1 primarily
# Construct the total potential for the bounce
# V(tau) = V_normal(tau) + F_BCS(tau), where F_BCS is 0 in normal phase

# The effective 1D potential for the bounce:
V_eff_fine = V_normal + F_bcs_fine_s1

# dV/dtau
dV_dtau = np.gradient(V_eff_fine, dt)
dV_interp = CubicSpline(tau_fine, dV_dtau)
V_eff_interp = CubicSpline(tau_fine, V_eff_fine)

# The "false vacuum" is at large tau. Since V is monotonically decreasing
# in the normal phase, we take tau_false = 0.50 as the starting point.
# The "true vacuum" is at the BCS minimum.

# Find true vacuum (minimum of V_eff)
idx_min = np.argmin(V_eff_fine)
tau_tv = tau_fine[idx_min]
V_tv = V_eff_fine[idx_min]

# False vacuum: local maximum between TV and tau=0.5
# (or the flat region at large tau)
# Since V_normal is monotonic, the "false vacuum" is where the BCS
# effect turns off, i.e., where F_BCS goes to zero coming from below.
# Look for the maximum of V_eff between tau_tv and 0.5

search_mask = (tau_fine > tau_tv)
if search_mask.any():
    idx_local_max = np.argmax(V_eff_fine[search_mask])
    tau_fv = tau_fine[search_mask][idx_local_max]
    V_fv = V_eff_fine[search_mask][idx_local_max]
    # Check if it's actually a local maximum
    if V_fv <= V_tv:
        # No barrier — V is everywhere below TV, or monotonic
        tau_fv = 0.5
        V_fv = V_eff_fine[-1]
else:
    tau_fv = 0.5
    V_fv = V_eff_fine[-1]

print(f"\n  True vacuum:  tau = {tau_tv:.4f}, V = {V_tv:.4f}")
print(f"  False vacuum: tau = {tau_fv:.4f}, V = {V_fv:.4f}")
print(f"  Barrier height (V_fv - V_tv) = {V_fv - V_tv:.4f}")

# O(4) bounce equation: phi'' + (3/r)*phi' = (1/G)*dV/dphi
# where phi = tau, and we include the moduli space metric G_tau_tau.
# In canonical normalization: phi_c = sqrt(G)*tau, V_c(phi_c) = V(phi_c/sqrt(G))
# Then bounce eq: phi_c'' + (3/r)*phi_c' = dV_c/dphi_c

# Shooting method: start at r=0 with phi(0) = phi_0 (near TV), phi'(0) = 0
# Shoot and adjust phi_0 until phi(r -> inf) -> phi_fv (FV).

sqrt_G = np.sqrt(G_tau_tau)
tau_to_phic = lambda tau: tau * sqrt_G
phic_to_tau = lambda phic: phic / sqrt_G

def dV_dphi_c(phic):
    """dV/dphi_c = (1/sqrt(G)) * dV/dtau"""
    tau = phic / sqrt_G
    tau = np.clip(tau, 0.0, 0.5)
    return dV_interp(tau) / sqrt_G

def V_c(phic):
    tau = phic / sqrt_G
    tau = np.clip(tau, 0.0, 0.5)
    return V_eff_interp(tau)

phic_tv = tau_to_phic(tau_tv)
phic_fv = tau_to_phic(tau_fv)

def bounce_ode(r, y):
    """O(4) bounce: y = [phi_c, dphi_c/dr]"""
    phi, dphi = y
    if r < 1e-10:
        # At r=0: phi'' = (1/4)*dV/dphi (from L'Hopital on 3/r term)
        ddphi = 0.25 * dV_dphi_c(phi)
    else:
        ddphi = dV_dphi_c(phi) - 3.0/r * dphi
    return [dphi, ddphi]

# Shooting: vary phi_0, look for solution that approaches FV
r_max = 50.0
r_span = (1e-6, r_max)
r_eval = np.linspace(1e-6, r_max, 5000)

# Binary search for the correct phi_0
phi_lo = phic_tv + 1e-6  # slightly above TV
phi_hi = phic_fv - 1e-6  # slightly below FV

B_numerical = np.nan
bounce_phi = None
bounce_r = None

n_shoot = 80
for iteration in range(n_shoot):
    phi_0 = 0.5 * (phi_lo + phi_hi)

    sol = solve_ivp(bounce_ode, r_span, [phi_0, 0.0],
                    t_eval=r_eval, method='RK45', rtol=1e-10, atol=1e-12,
                    max_step=0.1)

    if not sol.success:
        # If integration fails, the initial condition is too close to the barrier
        phi_hi = phi_0
        continue

    phi_end = sol.y[0, -1]
    dphi_end = sol.y[1, -1]

    # The correct bounce overshoots toward FV and settles
    # If phi_end > phic_fv: overshoot -> decrease phi_0
    # If phi_end < phic_fv: undershoot -> increase phi_0
    if phi_end > phic_fv:
        phi_hi = phi_0
    else:
        phi_lo = phi_0

    # Convergence check
    if abs(phi_hi - phi_lo) < 1e-12:
        break

# Final solution with best phi_0
phi_0_best = 0.5 * (phi_lo + phi_hi)
sol = solve_ivp(bounce_ode, r_span, [phi_0_best, 0.0],
                t_eval=r_eval, method='RK45', rtol=1e-10, atol=1e-12,
                max_step=0.1)

if sol.success:
    bounce_r = sol.t
    bounce_phi = sol.y[0]
    bounce_dphi = sol.y[1]
    bounce_tau = bounce_phi / sqrt_G

    # Compute bounce action:
    # B = 2*pi^2 * integral_0^inf r^3 * [(1/2)(dphi/dr)^2 + V(phi) - V_fv] dr
    integrand_B = bounce_r**3 * (0.5 * bounce_dphi**2 + V_c(bounce_phi) - V_fv)
    B_numerical = 2.0 * np.pi**2 * np.trapezoid(integrand_B, bounce_r)

    print(f"\n  Shooting converged after {iteration+1} iterations")
    print(f"  phi_0 (canonical) = {phi_0_best:.6f}")
    print(f"  tau_0 = {phi_0_best/sqrt_G:.6f}")
    print(f"  phi(r_max) = {bounce_phi[-1]:.6f} (target: {phic_fv:.6f})")
    print(f"  B_numerical = {B_numerical:.4f}")
    print(f"  B < 400? {'YES' if B_numerical < 400 else 'NO'}")
else:
    print("\n  Shooting did not converge!")

# ==============================================================================
# Method 3: Triangular barrier approximation
# ==============================================================================

# For a triangular barrier of height V_b and width Delta_tau:
# B_triangle ~ (2*pi^2/3) * G_tau_tau^2 * V_b * (Delta_tau)^4

print("\n" + "=" * 50)
print("Triangular barrier approximation:")
print("=" * 50)

# Barrier height: difference between FV and TV
V_b = V_fv - V_tv

# Barrier width: distance in tau between TV and FV
Delta_tau = abs(tau_fv - tau_tv)

B_triangle = (2.0 * np.pi**2 / 3.0) * G_tau_tau**2 * V_b * Delta_tau**4
print(f"  V_barrier = {V_b:.4f}")
print(f"  Delta_tau = {Delta_tau:.4f}")
print(f"  B_triangle = {B_triangle:.4f}")

# ==============================================================================
# Comparison with L-9 classical trapping
# ==============================================================================

# From s29b: KE at crossing for E_mult = 1.5 (lowest energy)
# trap_0_KE_at_cross = 3.16, latent_heat_mu1 = 5.63
# KE < L => classical trapping SUCCEEDS for E_mult = 1.5
# So the CDL bounce is relevant only for higher-energy trajectories
# that overshoot.

from_eom = np.load(os.path.join(data_dir, 's29b_modulus_eom.npz'), allow_pickle=True)
KE_cross = [float(from_eom[f'trap_{i}_KE_at_cross'].flat[0]) for i in range(3)]
L_mu1 = float(from_eom['latent_heat_mu1'].flat[0])
E_mults = [float(from_eom[f'trap_{i}_E_mult'].flat[0]) for i in range(3)]
trapped_mu1 = [bool(from_eom[f'trap_{i}_trapped_mu1'].flat[0]) for i in range(3)]

print("\n" + "=" * 50)
print("L-9 Classical trapping comparison:")
print("=" * 50)
for j in range(3):
    status = "TRAPPED" if trapped_mu1[j] else "OVERSHOOT"
    print(f"  E_mult={E_mults[j]}: KE={KE_cross[j]:.2f}, L={L_mu1:.2f} => {status}")

# ==============================================================================
# Gate verdict
# ==============================================================================

# The CDL bounce is a DIAGNOSTIC computation:
# - If B < 400: quantum tunneling efficient (good for trapping if classical fails)
# - If B > 400: tunneling too slow, need classical trapping
# PASS if B is computable and finite (provides information)
# The physical interpretation depends on whether we need quantum or classical trapping.

B_best = B_numerical if np.isfinite(B_numerical) else B_triangle
tunneling_efficient = B_best < 400

if np.isfinite(B_best):
    if tunneling_efficient:
        verdict = "PASS"
        verdict_detail = f"B = {B_best:.1f} < 400: quantum tunneling efficient"
    else:
        verdict = "DIAGNOSTIC"
        verdict_detail = f"B = {B_best:.1f} > 400: tunneling slow, classical trapping required"
else:
    verdict = "DIAGNOSTIC"
    verdict_detail = "Bounce action computation inconclusive (no clear barrier)"

print(f"\nB_best = {B_best:.4f}")
print(f"Verdict: {verdict}")
print(f"Detail: {verdict_detail}")

# ==============================================================================
# Save
# ==============================================================================

save_dict = dict(
    tau_fine=tau_fine,
    V_normal=V_normal,
    V_BCS_s1=V_BCS_s1,
    V_BCS_s2=V_BCS_s2,
    tau_tv=tau_tv,
    V_tv=V_tv,
    tau_fv=tau_fv,
    V_fv=V_fv,
    V_barrier=V_b,
    Delta_tau_barrier=Delta_tau,
    G_tau_tau=G_tau_tau,
    B_thin_wall_s1=27.0 * np.pi**2 * sigma**4 / (2.0 * epsilon**3) if epsilon > 0 else np.inf,
    B_numerical=B_numerical,
    B_triangle=B_triangle,
    B_best=B_best,
    tunneling_efficient=tunneling_efficient,
    verdict=verdict,
    verdict_detail=verdict_detail,
)

if bounce_r is not None:
    save_dict['bounce_r'] = bounce_r
    save_dict['bounce_tau'] = bounce_tau
    save_dict['bounce_dphi'] = bounce_dphi

np.savez(os.path.join(data_dir, 's29c_cdl_bounce.npz'), **save_dict)
print(f"\nSaved: s29c_cdl_bounce.npz")

# ==============================================================================
# Plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Effective potential
ax = axes[0, 0]
ax.plot(tau_fine, V_normal, 'b-', lw=2, label=r'$V_{normal}(\tau)$')
ax.plot(tau_fine, V_BCS_s1, 'r-', lw=2, label=r'$V_{BCS}(\tau)$ [$\mu=\lambda_{min}$]')
ax.plot(tau_fine, V_BCS_s2, 'g--', lw=1.5, label=r'$V_{BCS}(\tau)$ [$\mu=1.2\lambda_{min}$]')
ax.axvline(tau_tv, color='red', ls=':', alpha=0.5, label=f'TV ($\\tau$={tau_tv:.3f})')
ax.axvline(tau_fv, color='blue', ls=':', alpha=0.5, label=f'FV ($\\tau$={tau_fv:.3f})')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$V_{eff}$', fontsize=12)
ax.set_title('Effective Potential with BCS Condensation', fontsize=13)
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel 2: BCS contribution (F_BCS)
ax = axes[0, 1]
ax.plot(tau_fine, F_bcs_fine_s1, 'r-', lw=2, label=r'$F_{BCS}$ [$\mu=\lambda_{min}$]')
ax.plot(tau_fine, F_bcs_fine_s2, 'g--', lw=1.5, label=r'$F_{BCS}$ [$\mu=1.2\lambda_{min}$]')
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$F_{BCS}(\tau)$', fontsize=12)
ax.set_title('BCS Free Energy Contribution', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Panel 3: Bounce profile
ax = axes[1, 0]
if bounce_r is not None and bounce_tau is not None:
    ax.plot(bounce_r, bounce_tau, 'b-', lw=2)
    ax.axhline(tau_tv, color='red', ls=':', label=f'True vacuum ({tau_tv:.3f})')
    ax.axhline(tau_fv, color='blue', ls=':', label=f'False vacuum ({tau_fv:.3f})')
    ax.set_xlabel(r'$r$ (O(4) radius)', fontsize=12)
    ax.set_ylabel(r'$\tau(r)$', fontsize=12)
    ax.set_title(f'CDL Bounce Profile (B = {B_numerical:.1f})', fontsize=13)
    ax.legend(fontsize=10)
else:
    ax.text(0.5, 0.5, 'Bounce not converged', transform=ax.transAxes,
            ha='center', fontsize=14)
ax.grid(True, alpha=0.3)

# Panel 4: Summary / comparison
ax = axes[1, 1]
methods = ['Thin-wall', 'Numerical', 'Triangle']
B_values_plot = []
# Thin wall for scenario 1
if epsilon > 0:
    B_tw = 27.0 * np.pi**2 * sigma**4 / (2.0 * epsilon**3)
else:
    B_tw = 0
B_values_plot = [B_tw, B_numerical if np.isfinite(B_numerical) else 0, B_triangle]

colors = ['steelblue', 'firebrick', 'seagreen']
bars = ax.bar(methods, B_values_plot, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(400, color='red', ls='--', lw=2, label='B = 400 threshold')
ax.set_ylabel('Bounce Action B', fontsize=12)
ax.set_title('CDL Bounce Action Comparison', fontsize=13)
ax.legend(fontsize=10)

for bar, val in zip(bars, B_values_plot):
    if val > 0:
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + max(B_values_plot)*0.02,
                f'{val:.1f}', ha='center', fontsize=10)

ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig(os.path.join(data_dir, 's29c_cdl_bounce.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s29c_cdl_bounce.png")
print("\nDone.")
