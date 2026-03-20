"""
Session 35 W3-B: Poschl-Teller Bound States at B2 Fold
=======================================================
Paasch Mass Quantization Analyst

Gate: PT-RATIO-35
Criterion: PASS if |E_2/E_1 - 1.53158| / 1.53158 < 0.10

Method:
1. Extract B2 eigenvalue curve lambda_B2(tau) from kosmann data (9 tau points).
2. Fit quadratic near the fold minimum to get a_2 (curvature).
3. Extract wall profile parameters (width, shape) from modulus equation data.
4. Construct the effective 1D Schrodinger equation for wall-localized modes:
   - tau(x) = tau_false + (tau_true - tau_false) * (1 + tanh(x/w))/2
   - The effective potential for B2 fluctuations on the wall is:
     V_eff(x) = a_2 * (tau(x) - tau_fold)^2
   - For a tanh wall centered at the fold, this gives:
     V_eff(x) = a_2 * (Delta_tau/2)^2 * tanh^2(x/w)
            = V_0 * (1 - 1/cosh^2(x/w))  + const
   - The bound-state part is the Poschl-Teller potential:
     V_PT(x) = -V_0 / cosh^2(x/w)
5. Solve analytically for bound states.
6. Also solve numerically (1D Schrodinger) as cross-check.
7. Compare E_2/E_1 with phi_paasch = 1.53158.

Physics:
- The B2 eigenvalue has a fold (quadratic minimum) at tau_fold ~ 0.190.
- A Z_3 domain wall interpolates tau from one vacuum to another, passing
  through tau_fold.
- Modes localized on the wall see the B2 eigenvalue as a potential well.
- The well shape is determined by the B2 curvature (a_2) and wall width (w).
- Poschl-Teller potentials have exactly solvable spectra.

Inputs:
- tier0-computation/s23a_kosmann_singlet.npz  (eigenvalue curves)
- tier0-computation/s33w3_modulus_equation.npz (wall profile parameters)
- tier0-computation/s33w3_paasch_dump_point.npz (dump point data)
"""

import numpy as np
from scipy.optimize import curve_fit
from scipy.linalg import eigh_tridiagonal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("POSCHL-TELLER BOUND STATES AT B2 FOLD")
print("=" * 70)

# ===========================================================================
# 1. EXTRACT B2 EIGENVALUE CURVE
# ===========================================================================

print("\n--- 1. B2 Eigenvalue Curve ---")

d_kosmann = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/s23a_kosmann_singlet.npz',
                     allow_pickle=True)
d_wall = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/s33w3_modulus_equation.npz',
                  allow_pickle=True)
d_dump = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/s33w3_paasch_dump_point.npz',
                  allow_pickle=True)

tau_values = d_kosmann['tau_values']
# tau_values = [0.0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.5]

# Extract B2 branch (4-fold degenerate, middle eigenvalue at each tau)
B2_values = []
B1_values = []
B3_values = []

for i, tau in enumerate(tau_values):
    evals = d_kosmann[f'eigenvalues_{i}']
    pos_evals = np.sort(evals[evals > 0])
    # Structure: B1 (1x, lowest), B2 (4x, middle), B3 (3x, highest)
    # At tau=0, all degenerate at 0.8660254
    if tau == 0.0:
        B1_values.append(pos_evals[0])
        B2_values.append(pos_evals[0])
        B3_values.append(pos_evals[0])
    else:
        # Identify by degeneracy: singlet, quartet, triplet
        B1_values.append(pos_evals[0])       # singlet (lowest)
        B2_values.append(pos_evals[1])       # quartet (middle, indices 1-4)
        B3_values.append(pos_evals[5])       # triplet (highest, indices 5-7)

B2_values = np.array(B2_values)
B1_values = np.array(B1_values)
B3_values = np.array(B3_values)

print(f"{'tau':>6} {'B1':>12} {'B2':>12} {'B3':>12}")
for i, tau in enumerate(tau_values):
    print(f"{tau:6.2f} {B1_values[i]:12.6f} {B2_values[i]:12.6f} {B3_values[i]:12.6f}")

# ===========================================================================
# 2. FIT QUADRATIC CURVATURE AT B2 FOLD
# ===========================================================================

print("\n--- 2. Quadratic Fit at B2 Fold ---")

# The B2 minimum is near tau = 0.190 (from dump point data)
tau_fold_known = float(d_dump['tau_b2_min'])  # 0.19017
b2_min_known = float(d_dump['b2_min'])        # 0.84521

print(f"Known dump point: tau_fold = {tau_fold_known:.5f}, B2_min = {b2_min_known:.5f}")

# Fit quadratic lambda_B2(tau) = lambda_fold + a_2 * (tau - tau_fold)^2
# Use points near the fold: tau = 0.10, 0.15, 0.20, 0.25, 0.30
# (exclude tau=0 which is degenerate and tau>0.30 which may be far from quadratic)

def quadratic(tau, lam_fold, a2, tau0):
    return lam_fold + a2 * (tau - tau0)**2

# Fit using all non-degenerate points
mask = tau_values > 0.05
popt, pcov = curve_fit(quadratic, tau_values[mask], B2_values[mask],
                        p0=[0.845, 0.5, 0.19])

lam_fold_fit, a2_fit, tau_fold_fit = popt
print(f"\nQuadratic fit (all tau > 0.05):")
print(f"  lambda_fold = {lam_fold_fit:.6f}")
print(f"  a_2 = {a2_fit:.6f}")
print(f"  tau_fold = {tau_fold_fit:.5f}")

# Also fit using just the 5 nearest points to the minimum
mask_near = (tau_values >= 0.10) & (tau_values <= 0.30)
popt_near, pcov_near = curve_fit(quadratic, tau_values[mask_near], B2_values[mask_near],
                                  p0=[0.845, 0.5, 0.19])

lam_fold_near, a2_near, tau_fold_near = popt_near
print(f"\nQuadratic fit (tau in [0.10, 0.30]):")
print(f"  lambda_fold = {lam_fold_near:.6f}")
print(f"  a_2 = {a2_near:.6f}")
print(f"  tau_fold = {tau_fold_near:.5f}")

# Also try the Berry-classification value a_2 = 0.588 with tau_fold and lam_fold from dump point
print(f"\nBerry classification value: a_2 = 0.588")

# Residuals for each fit
print(f"\nFit residuals:")
for i, tau in enumerate(tau_values):
    if tau > 0.05:
        res_all = B2_values[i] - quadratic(tau, *popt)
        res_near = B2_values[i] - quadratic(tau, *popt_near)
        res_berry = B2_values[i] - (b2_min_known + 0.588 * (tau - tau_fold_known)**2)
        print(f"  tau={tau:.2f}: fit_all={res_all:+.6f}, fit_near={res_near:+.6f}, Berry={res_berry:+.6f}")

# Use the near-fold fit as primary (most relevant for the bound state problem)
# But also compute with Berry value for comparison
a2_primary = a2_near
tau_fold_primary = tau_fold_near
lam_fold_primary = lam_fold_near

print(f"\n==> PRIMARY: a_2 = {a2_primary:.6f}, tau_fold = {tau_fold_primary:.5f}")

# ===========================================================================
# 3. WALL PROFILE PARAMETERS
# ===========================================================================

print("\n--- 3. Wall Profile Parameters ---")

# From modulus equation: wall_params array has columns [r_ba, eta, tau_min, tau_bar, delta_V]
wall_params = d_wall['wall_params']
G_tau_tau = float(d_wall['G_tau_tau'])  # 5.0
chi_0_spec = float(d_wall['chi_0'])     # 18.0
chi_1_spec = float(d_wall['chi_1'])     # 12.15
r_ba_primary = float(d_wall['r_ba_primary'])  # 0.28

print(f"G_tau_tau = {G_tau_tau}")
print(f"chi_0 = {chi_0_spec}, chi_1 = {chi_1_spec}")
print(f"r_ba = {r_ba_primary}")

# The wall interpolates between tau=0 (round metric) and tau=tau_min
# (true vacuum). For r_ba = 0.28, the wall parameters are:
print(f"\nWall parameter scan (beta/alpha = 0.28):")
print(f"{'r_ba':>6} {'eta':>6} {'tau_min':>10} {'tau_bar':>10} {'delta_V':>10}")
for row in wall_params:
    if abs(row[0] - 0.28) < 0.01:
        print(f"{row[0]:6.2f} {row[1]:6.2f} {row[2]:10.4f} {row[3]:10.4f} {row[4]:10.4f}")

# For the Poschl-Teller analysis, we need:
# 1. The tau range traversed by the wall: Delta_tau = tau_true - tau_false
# 2. The wall width w in the x-coordinate
#
# The wall profile is approximately: tau(x) = tau_c + (Delta_tau/2) * tanh(x/w)
# where tau_c is the center of the wall, Delta_tau = tau_true - tau_false
#
# For r_ba=0.28, eta=0.0: tau_min=0.4412, tau_bar=0.1517
# The wall goes from tau=0 (false vacuum) through tau_bar=0.15 to tau_min=0.44
#
# For r_ba=0.28, eta=0.05: tau_min=0.4057, tau_bar=0.1940
# IMPORTANT: tau_bar = 0.194 is very close to tau_fold = 0.190!
#
# For r_ba=0.28, eta=0.10: wall disappears (tau_min = 0)

# Primary case: r_ba=0.28, eta=0.05 (barrier near dump point)
# Secondary: r_ba=0.28, eta=0.00 (pure FR)
# Also compute for r_ba=0.20, 0.25 where walls exist at more eta values

# Extract wall width from the barrier height and shape
# Thin-wall approximation: w = Delta_tau * sqrt(G_tt / (2 * Delta_V))
# But we need more careful treatment for the Poschl-Teller mapping.

# For each case, compute the effective PT parameters
print("\n--- Computing Poschl-Teller parameters for each wall configuration ---")

# ===========================================================================
# 4. POSCHL-TELLER MAPPING
# ===========================================================================
#
# The domain wall has profile tau(x) = tau_c + (Delta_tau/2) * tanh(x/w)
# where w is the wall half-width.
#
# The B2 eigenvalue near the fold:
#   lambda_B2(tau) = lambda_fold + a_2 * (tau - tau_fold)^2
#
# On the wall, the effective potential for a mode with wavenumber k along the wall
# and localized transversally is:
#
#   V_eff(x) = a_2 * (tau(x) - tau_fold)^2
#
# If the wall center coincides with the fold (tau_c = tau_fold):
#   tau(x) - tau_fold = (Delta_tau/2) * tanh(x/w)
#   V_eff(x) = a_2 * (Delta_tau/2)^2 * tanh^2(x/w)
#            = V_0 * [1 - sech^2(x/w)]
#
# where V_0 = a_2 * (Delta_tau/2)^2.
#
# This gives the INVERTED Poschl-Teller problem:
#   -d^2 psi/dx^2 + V_0 * [1 - sech^2(x/w)] * psi = E * psi
#
# Rearranging:
#   -d^2 psi/dx^2 - V_0 * sech^2(x/w) * psi = (E - V_0) * psi
#
# Define epsilon = E - V_0, so epsilon < 0 for bound states below V_0.
# This is the standard Poschl-Teller equation:
#   -d^2 psi/dx^2 - V_0 / cosh^2(x/w) * psi = epsilon * psi
#
# The dimensionless strength parameter is:
#   s(s+1) = V_0 * w^2   (in units where hbar^2/(2m) = 1)
#
# For our problem, the kinetic term comes from the wall-localized Schrodinger eq:
#   -(1/(2*G_tau_tau)) * d^2 psi/dx^2 + a_2*(tau(x)-tau_fold)^2 * psi = E * psi
#
# So the effective mass is m_eff = G_tau_tau and the PT depth parameter is:
#   s(s+1) = 2 * G_tau_tau * V_0 * w^2 = 2 * G_tau_tau * a_2 * (Delta_tau/2)^2 * w^2
#
# HOWEVER: we need to be careful about the relationship between
# the wall width w and the potential depth V_0. They are NOT independent --
# both come from the same wall solution.
#
# From the wall ODE: G_tt * (dtau/dx)^2 / 2 = V_eff(tau) - V_eff(tau_min)
# For a tanh wall: dtau/dx = (Delta_tau/2w) * sech^2(x/w)
# Peak kinetic energy: G_tt * (Delta_tau/(2w))^2 / 2 = Delta_V (barrier height)
# => w = (Delta_tau/2) * sqrt(G_tt / (2 * Delta_V))
#
# So V_0 = a_2 * (Delta_tau/2)^2 and w = (Delta_tau/2) * sqrt(G_tt/(2*Delta_V))
# => V_0 * w^2 = a_2 * (Delta_tau/2)^4 * G_tt / (2 * Delta_V)
# => s(s+1) = 2 * G_tt * a_2 * (Delta_tau/2)^4 * G_tt / (2 * Delta_V)
#           = G_tt^2 * a_2 * (Delta_tau/2)^4 / Delta_V

print("\n" + "=" * 70)
print("4. POSCHL-TELLER ANALYSIS")
print("=" * 70)

phi_paasch = 1.5315844

# Reconstruct V_FR potential functions for wall width estimation
def R_K(tau):
    return 1.5 * (2*np.exp(2*tau) - 1 + 8*np.exp(-tau) - np.exp(-4*tau))

def dR_K_dtau(tau):
    return 1.5 * (4*np.exp(2*tau) - 8*np.exp(-tau) + 4*np.exp(-4*tau))

def omega_sq(tau):
    return 0.5*np.exp(-4*tau) + 0.5 + (1.0/3.0)*np.exp(6*tau)

def d_omega_sq_dtau(tau):
    return -2*np.exp(-4*tau) + 2*np.exp(6*tau)

def V_FR(tau, r_ba):
    return -R_K(tau) + r_ba * omega_sq(tau)

def dV_FR_dtau(tau, r_ba):
    return -dR_K_dtau(tau) + r_ba * d_omega_sq_dtau(tau)

def V_spec(tau, eta=1.0):
    return eta * (0.5 * chi_0_spec * tau**2 + (1.0/6.0) * chi_1_spec * tau**3)

def dV_spec_dtau(tau, eta=1.0):
    return eta * (chi_0_spec * tau + 0.5 * chi_1_spec * tau**2)

def V_eff_total(tau, r_ba, eta):
    return V_FR(tau, r_ba) + V_spec(tau, eta)

def dV_eff_total_dtau(tau, r_ba, eta):
    return dV_FR_dtau(tau, r_ba) + dV_spec_dtau(tau, eta)


# Compute for multiple wall configurations
# We scan: (r_ba, eta) pairs where walls exist and pass through or near the fold
configs = []

# For each row in wall_params: [r_ba, eta, tau_min, tau_bar, delta_V]
for row in wall_params:
    r_ba, eta, tau_min, tau_bar, delta_V = row
    if tau_min < 0.01:
        continue  # wall doesn't exist
    if delta_V < 1e-6:
        continue  # no barrier

    # Wall interpolates from tau=0 (or a local min near 0) to tau_min
    # The barrier is at tau_bar
    # For the tanh approximation: tau_c ~ tau_bar, Delta_tau ~ 2*tau_bar
    # (the wall goes from 0 to ~2*tau_bar approximately)

    # More precisely: the wall goes from tau_false=0 to tau_true=tau_min
    tau_false = 0.0
    tau_true = tau_min
    Delta_tau = tau_true - tau_false
    tau_center = (tau_true + tau_false) / 2.0  # center of the wall

    # Wall width from thin-wall: w = Delta_tau * sqrt(G_tt / (2 * Delta_V)) / 2
    # Actually: w = (Delta_tau / (2 * sqrt(2 * Delta_V / G_tt)))
    # The tanh profile is tau(x) = tau_c + (Delta_tau/2)*tanh(x/w)
    # with dtau/dx|_max = Delta_tau/(2w) at x=0
    # From energy conservation: (G_tt/2)*(dtau/dx)^2 = V(tau) - V(tau_true)
    # At x=0 (tau=tau_bar): (G_tt/2)*(Delta_tau/(2w))^2 ~ delta_V
    # => w = (Delta_tau/2) * sqrt(G_tt / (2*delta_V))

    w_wall = (Delta_tau / 2.0) * np.sqrt(G_tau_tau / (2.0 * delta_V))

    # Distance from wall center to fold
    dist_fold = abs(tau_center - tau_fold_primary)

    # Is the fold within the wall?
    fold_in_wall = (tau_false < tau_fold_primary < tau_true)

    # Effective PT potential depth
    # V_PT(x) arises from a_2 * (tau(x) - tau_fold)^2
    # If fold is at the center: V_0 = a_2 * (Delta_tau/2)^2
    # If fold is off-center at tau_fold: we need modified formula

    # For the general case, tau(x) = tau_c + (Delta_tau/2)*tanh(x/w)
    # tau(x) - tau_fold = (tau_c - tau_fold) + (Delta_tau/2)*tanh(x/w)
    # Let d = tau_c - tau_fold, A = Delta_tau/2
    # V(x) = a_2 * [d + A*tanh(x/w)]^2 = a_2*[d^2 + 2dA*tanh + A^2*tanh^2]
    # = a_2*A^2*(1 - sech^2) + 2*a_2*d*A*tanh + a_2*d^2
    # This is NOT a pure Poschl-Teller unless d=0 (fold at wall center).

    # Effective depth of the sech^2 well:
    V_0_PT = a2_primary * (Delta_tau / 2.0)**2

    # PT strength parameter (dimensionless)
    # s(s+1) = 2 * m_eff * V_0 * w^2 / hbar^2
    # In our natural units (hbar=1), m_eff = G_tau_tau for the kinetic term
    # The Schrodinger eq is: -(1/(2*G_tt)) * d^2psi/dx^2 + V(x)*psi = E*psi
    # => -d^2psi/dx^2 + 2*G_tt*V(x)*psi = 2*G_tt*E*psi
    # So the effective PT depth for the standard form is 2*G_tt*V_0

    lambda_PT = 2.0 * G_tau_tau * V_0_PT * w_wall**2

    # Solve s(s+1) = lambda_PT for s
    # s = (-1 + sqrt(1 + 4*lambda_PT)) / 2
    s_PT = (-1.0 + np.sqrt(1.0 + 4.0 * lambda_PT)) / 2.0

    # Number of bound states: n = 0, 1, ..., floor(s - 1/2) for s > 1/2
    # Or equivalently: N_bound = floor(s + 1/2) for s > 0
    N_bound = int(np.floor(s_PT + 0.5)) if s_PT > 0 else 0

    configs.append({
        'r_ba': r_ba, 'eta': eta,
        'tau_min': tau_min, 'tau_bar': tau_bar, 'delta_V': delta_V,
        'Delta_tau': Delta_tau, 'w_wall': w_wall,
        'tau_center': tau_center, 'dist_fold': dist_fold,
        'fold_in_wall': fold_in_wall,
        'V_0_PT': V_0_PT, 'lambda_PT': lambda_PT, 's_PT': s_PT,
        'N_bound': N_bound
    })

print(f"\n{'r_ba':>6} {'eta':>6} {'Delta_tau':>10} {'w_wall':>10} {'V_0':>10} "
      f"{'lambda':>10} {'s':>8} {'N_bound':>8} {'fold_in?':>10}")
for c in configs:
    print(f"{c['r_ba']:6.2f} {c['eta']:6.2f} {c['Delta_tau']:10.4f} {c['w_wall']:10.4f} "
          f"{c['V_0_PT']:10.6f} {c['lambda_PT']:10.4f} {c['s_PT']:8.4f} "
          f"{c['N_bound']:8d} {'YES' if c['fold_in_wall'] else 'NO':>10}")


# ===========================================================================
# 5. BOUND STATE ENERGIES AND RATIOS
# ===========================================================================

print("\n" + "=" * 70)
print("5. POSCHL-TELLER BOUND STATE ENERGIES")
print("=" * 70)

# For the Poschl-Teller potential V(x) = -V_0 / cosh^2(x/w):
# Bound state energies (measured from the top of the well, i.e., from 0):
#   epsilon_n = -V_0 * (s - n)^2 / s^2   for n = 0, 1, ..., floor(s - 1/2)
#
# Wait — the standard PT spectrum is:
#   E_n = -(hbar^2 / (2m w^2)) * (s - n)^2
#
# In our natural units with 2*m*V_0*w^2 = s(s+1):
#   E_n = -(V_0 / s(s+1)) * (s - n)^2 = -(1/(2*G_tt*w^2)) * (s-n)^2
#
# The BINDING energies (positive, measured from threshold) are:
#   |E_n| = (1/(2*G_tt*w^2)) * (s-n)^2
#
# For comparison with Paasch, we want the ABSOLUTE energies of wall modes,
# not their binding energies. The wall-localized modes have total energy:
#   E_n^{total} = V_0 + E_n = V_0 - (V_0/(s(s+1))) * (s-n)^2
#   = V_0 * [1 - (s-n)^2 / (s(s+1))]
#   = V_0 * [s(s+1) - (s-n)^2] / (s(s+1))
#   = V_0 * [2sn - n^2 + s] / (s(s+1))   -- after expanding
#
# Actually let me be more careful. The standard PT potential is:
#   V(x) = -U_0 / cosh^2(x/a)
# with bound state energies:
#   E_n = -U_0 * [(sqrt(1 + 4*U_0*a^2) - 1)/2 - n]^2 / (a^2 * ... )
#
# Let me use the standard textbook form.
# Define lambda_hat = (sqrt(1/4 + 2*m*U_0*a^2/hbar^2) - 1/2)
# Then E_n = -(hbar^2/(2*m*a^2)) * (lambda_hat - n)^2
# for n = 0, 1, ..., floor(lambda_hat)
#
# In our notation: lambda_hat = s (where s(s+1) = 2*m*V_0*w^2)
# and a = w, m = G_tau_tau
#
# E_n = -(1/(2*G_tt*w^2)) * (s - n)^2
#
# These are BINDING energies (negative, measured from continuum threshold at 0).
# The physical energy of the mode relative to the well bottom is:
#   E_n^{phys} = V_0 + E_n = V_0 - (1/(2*G_tt*w^2)) * (s-n)^2
#
# Using V_0 = s(s+1) / (2*G_tt*w^2):
#   E_n^{phys} = (1/(2*G_tt*w^2)) * [s(s+1) - (s-n)^2]
#   = (1/(2*G_tt*w^2)) * [2sn - n^2 + s]
#   = (1/(2*G_tt*w^2)) * (s-n) * [2n + 1 + ... ]  -- hmm let me just compute
#
# Actually: s(s+1) - (s-n)^2 = s^2 + s - s^2 + 2sn - n^2 = s + 2sn - n^2
#                              = s(1 + 2n) - n^2 = n(2s - n) + s
#
# So E_n^{phys} = [n(2s - n) + s] / (2*G_tt*w^2)
#
# For the RATIO of excitation energies above the ground state:
# Delta_E_n = E_n^{phys} - E_0^{phys}
# E_0^{phys} = s / (2*G_tt*w^2)  (n=0: s(1+0) - 0 = s)
# E_n^{phys} = [n(2s-n) + s] / (2*G_tt*w^2)
# Delta_E_n = n(2s-n) / (2*G_tt*w^2)
#
# Ratios: Delta_E_2 / Delta_E_1 = 2(2s-2) / (2s-1) = 2(2s-2)/(2s-1)
#
# For E_2/E_1 = Delta_E_2/Delta_E_1:
#   R_{21} = 2(2s-2) / (2s-1)
#
# Setting this equal to phi_paasch = 1.53158:
#   1.53158 = 2(2s-2)/(2s-1) = (4s-4)/(2s-1)
#   1.53158*(2s-1) = 4s - 4
#   3.06316s - 1.53158 = 4s - 4
#   4 - 1.53158 = 4s - 3.06316s
#   2.46842 = 0.93684s
#   s = 2.46842 / 0.93684 = 2.6347
#
# So s ~ 2.63 gives the phi_paasch ratio. Does any wall configuration produce this?

# Also: for BINDING energy ratios (not excitation energies):
# |E_n| = (s-n)^2 / (2*G_tt*w^2)
# |E_1|/|E_0| = (s-1)^2 / s^2
# This is always < 1 (deeper binding for ground state), so not the right comparison.
#
# The PHYSICAL comparison is between the EXCITATION LEVELS of wall-localized modes,
# measured from the well bottom. These are the "particle masses" in the wall picture.

print("\n--- Excitation energy formula ---")
print("E_n^{phys} = [n(2s-n) + s] / (2*G_tt*w^2)")
print("Delta_E_n = E_n^{phys} - E_0^{phys} = n(2s-n) / (2*G_tt*w^2)")
print("R_{n,1} = Delta_E_n / Delta_E_1 = n(2s-n) / (2s-1)")
print()

# The ratios are:
# R_{2,1} = 2(2s-2)/(2s-1)
# R_{3,1} = 3(2s-3)/(2s-1)
# R_{4,1} = 4(2s-4)/(2s-1)
# etc.

# For R_{2,1} = phi_paasch:
s_target = 2.46842 / 0.93684
print(f"s for R_21 = phi_paasch: s = {s_target:.6f}")
print(f"Check: 2*(2*{s_target:.4f}-2)/(2*{s_target:.4f}-1) = "
      f"{2*(2*s_target-2)/(2*s_target-1):.6f} (target: {phi_paasch:.6f})")

# Now compute for each wall configuration
print(f"\n{'r_ba':>6} {'eta':>6} {'s':>8} {'N_bound':>8} {'R_21':>10} {'R_31':>10} "
      f"{'|R21-phi|/phi':>14}")

results_table = []
for c in configs:
    s = c['s_PT']
    N = c['N_bound']
    w = c['w_wall']

    if N < 1:
        continue

    # Excitation energy ratios
    ratios = {}
    for n in range(1, N+1):
        ratios[n] = n * (2*s - n) / (2*s - 1)

    R21 = ratios.get(2, float('nan'))
    R31 = ratios.get(3, float('nan'))

    dev_phi = abs(R21 - phi_paasch) / phi_paasch if not np.isnan(R21) else float('nan')

    print(f"{c['r_ba']:6.2f} {c['eta']:6.2f} {s:8.4f} {N:8d} "
          f"{R21:10.6f} {R31:10.6f} {dev_phi:14.6f}")

    c['R21'] = R21
    c['R31'] = R31
    c['dev_phi'] = dev_phi
    c['ratios'] = ratios
    results_table.append(c)


# ===========================================================================
# 6. WHAT VALUE OF s GIVES phi_paasch?
# ===========================================================================

print("\n" + "=" * 70)
print("6. REQUIRED s FOR phi_paasch RATIO")
print("=" * 70)

# R_{2,1} = 2(2s-2)/(2s-1) = phi_paasch
# => s = (4 - phi) / (4 - 2*phi) = (4 - 1.53158) / (4 - 2*1.53158)
s_phi = (4 - phi_paasch) / (4 - 2*phi_paasch)
print(f"s_required = {s_phi:.6f}")
print(f"s(s+1) = {s_phi*(s_phi+1):.6f}")

# What lambda_PT = s(s+1) is needed?
lambda_needed = s_phi * (s_phi + 1)
print(f"lambda_PT needed = {lambda_needed:.6f}")

# What does this require in terms of physical parameters?
# lambda_PT = 2 * G_tt * V_0 * w^2
# = 2 * G_tt * a_2 * (Delta_tau/2)^2 * w^2
# = G_tt^2 * a_2 * (Delta_tau/2)^4 / delta_V  (using w = (Delta_tau/2)*sqrt(G_tt/(2*delta_V)))
#
# Actually let me substitute:
# V_0 = a_2 * (Delta_tau/2)^2
# w = (Delta_tau/2) * sqrt(G_tt / (2*delta_V))
# lambda_PT = 2*G_tt * a_2*(Delta_tau/2)^2 * (Delta_tau/2)^2 * G_tt/(2*delta_V)
#           = G_tt^2 * a_2 * (Delta_tau/2)^4 / delta_V

print(f"\nlambda_PT = G_tt^2 * a_2 * (Delta_tau/2)^4 / delta_V")
print(f"         = {G_tau_tau}^2 * {a2_primary:.4f} * (Delta_tau/2)^4 / delta_V")
print(f"         = {G_tau_tau**2 * a2_primary:.4f} * (Delta_tau/2)^4 / delta_V")

# For each config, show the actual lambda_PT
print(f"\n{'r_ba':>6} {'eta':>6} {'lambda_PT':>10} {'needed':>10} {'ratio':>8}")
for c in configs:
    ratio = c['lambda_PT'] / lambda_needed
    print(f"{c['r_ba']:6.2f} {c['eta']:6.2f} {c['lambda_PT']:10.4f} {lambda_needed:10.4f} {ratio:8.4f}")


# ===========================================================================
# 7. ALTERNATIVE: DIRECT POSCHL-TELLER WITH BERRY a_2
# ===========================================================================

print("\n" + "=" * 70)
print("7. ANALYSIS WITH BERRY CLASSIFICATION a_2 = 0.588")
print("=" * 70)

a2_berry = 0.588

print(f"\nUsing a_2 = {a2_berry} (Berry fold classification)")
print(f"Comparison: fitted a_2 = {a2_primary:.4f} (quadratic fit)")
print(f"Relative difference: {abs(a2_berry - a2_primary)/a2_primary:.4f}")

# Recompute PT parameters with Berry a_2
print(f"\n{'r_ba':>6} {'eta':>6} {'s(Berry)':>10} {'N_bound':>8} {'R21':>10} {'dev_phi':>12}")
for c in configs:
    V_0_berry = a2_berry * (c['Delta_tau'] / 2.0)**2
    lambda_berry = 2.0 * G_tau_tau * V_0_berry * c['w_wall']**2
    s_berry = (-1.0 + np.sqrt(1.0 + 4.0 * lambda_berry)) / 2.0
    N_berry = int(np.floor(s_berry + 0.5)) if s_berry > 0 else 0

    if N_berry >= 2:
        R21_berry = 2*(2*s_berry - 2) / (2*s_berry - 1)
        dev = abs(R21_berry - phi_paasch) / phi_paasch
    else:
        R21_berry = float('nan')
        dev = float('nan')

    c['s_berry'] = s_berry
    c['N_bound_berry'] = N_berry
    c['R21_berry'] = R21_berry
    c['dev_phi_berry'] = dev

    print(f"{c['r_ba']:6.2f} {c['eta']:6.2f} {s_berry:10.4f} {N_berry:8d} "
          f"{R21_berry:10.6f} {dev:12.6f}")


# ===========================================================================
# 8. NUMERICAL CROSS-CHECK: 1D FINITE-DIFFERENCE SCHRODINGER
# ===========================================================================

print("\n" + "=" * 70)
print("8. NUMERICAL CROSS-CHECK: 1D SCHRODINGER EQUATION")
print("=" * 70)

def solve_pt_numerical(V_0, w, G_tt, N_grid=2000, x_max=20.0):
    """Solve 1D Schrodinger numerically for PT potential.

    -1/(2*G_tt) * d^2psi/dx^2 - V_0/cosh^2(x/w) * psi = E * psi

    Returns bound state energies (negative, measured from continuum).
    """
    dx = 2 * x_max / (N_grid - 1)
    x = np.linspace(-x_max, x_max, N_grid)

    # Potential on grid
    V = -V_0 / np.cosh(x / w)**2

    # Kinetic coefficient
    T_coeff = 1.0 / (2.0 * G_tt * dx**2)

    # Tridiagonal Hamiltonian
    diag = 2.0 * T_coeff + V
    off_diag = -T_coeff * np.ones(N_grid - 1)

    # Solve for lowest eigenvalues
    eigenvalues, eigenvectors = eigh_tridiagonal(diag, off_diag,
                                                  select='i', select_range=[0, min(20, N_grid-1)])

    # Bound states have E < 0
    bound = eigenvalues[eigenvalues < -1e-10]
    return bound, x, V

# Test with the best wall configuration
# Find config closest to phi_paasch
best_config = None
best_dev = 1.0
for c in configs:
    if c['N_bound'] >= 2 and not np.isnan(c.get('dev_phi', 1.0)):
        if c['dev_phi'] < best_dev:
            best_dev = c['dev_phi']
            best_config = c

if best_config is not None:
    print(f"\nBest configuration: r_ba={best_config['r_ba']}, eta={best_config['eta']}")
    print(f"  s = {best_config['s_PT']:.4f}, N_bound = {best_config['N_bound']}")
    print(f"  R21 = {best_config['R21']:.6f}, dev = {best_config['dev_phi']:.6f}")

    # Numerical solution
    E_bound, x_grid, V_grid = solve_pt_numerical(
        best_config['V_0_PT'], best_config['w_wall'], G_tau_tau,
        N_grid=4000, x_max=30.0
    )

    print(f"\n  Numerical bound state energies (from continuum):")
    for i, E in enumerate(E_bound):
        print(f"    n={i}: E = {E:.8f}")

    if len(E_bound) >= 2:
        # Physical energies from well bottom
        E_phys = best_config['V_0_PT'] + E_bound
        print(f"\n  Physical energies (from well bottom):")
        for i, E in enumerate(E_phys):
            print(f"    n={i}: E_phys = {E:.8f}")

        # Excitation energies
        dE = E_phys - E_phys[0]
        print(f"\n  Excitation energies:")
        for i in range(1, len(dE)):
            print(f"    Delta_E_{i} = {dE[i]:.8f}")

        if len(dE) >= 3:
            R21_num = dE[2] / dE[1]
            print(f"\n  R_21 (numerical) = {R21_num:.6f}")
            print(f"  R_21 (analytic)  = {best_config['R21']:.6f}")
            print(f"  Agreement: {abs(R21_num - best_config['R21'])/best_config['R21']*100:.4f}%")

    # Compare analytic and numerical
    s = best_config['s_PT']
    print(f"\n  Analytic energies: E_n = -(s-n)^2 / (2*G_tt*w^2)")
    coeff = 1.0 / (2.0 * G_tau_tau * best_config['w_wall']**2)
    for n in range(best_config['N_bound']):
        E_an = -coeff * (s - n)**2
        E_num = E_bound[n] if n < len(E_bound) else float('nan')
        print(f"    n={n}: analytic = {E_an:.8f}, numerical = {E_num:.8f}, "
              f"diff = {abs(E_an - E_num):.2e}" if not np.isnan(E_num) else
              f"    n={n}: analytic = {E_an:.8f}, numerical = N/A")


# ===========================================================================
# 9. COMPREHENSIVE s-SCAN FOR phi_paasch
# ===========================================================================

print("\n" + "=" * 70)
print("9. COMPREHENSIVE EXCITATION RATIO SCAN")
print("=" * 70)

# Show R_{2,1} as a function of s
s_scan = np.linspace(1.5, 10.0, 1000)
R21_scan = 2.0 * (2.0 * s_scan - 2.0) / (2.0 * s_scan - 1.0)

# Find where R21 = phi_paasch
from scipy.optimize import brentq as brentq_opt
s_cross = brentq_opt(lambda s: 2*(2*s-2)/(2*s-1) - phi_paasch, 1.5, 10.0)
print(f"R_21 = phi_paasch = {phi_paasch} at s = {s_cross:.6f}")
print(f"This requires s(s+1) = {s_cross*(s_cross+1):.6f}")
print(f"Number of bound states at this s: {int(np.floor(s_cross + 0.5))}")

# Also check R_{3,1}/R_{2,1} = phi_paasch (higher ratios)
# R_{n+1}/R_n = (n+1)(2s-n-1) / [n(2s-n)]
# For phi pattern: R_{n+1}/R_n could also match phi

print(f"\n--- Ratios at s = s_cross = {s_cross:.4f} ---")
for n in range(1, int(np.floor(s_cross + 0.5)) + 1):
    R_n1 = n * (2*s_cross - n) / (2*s_cross - 1)
    print(f"  R_{{{n},1}} = {R_n1:.6f}")

# Consecutive ratios
print(f"\n--- Consecutive ratios R_{{n+1,1}}/R_{{n,1}} at s = {s_cross:.4f} ---")
for n in range(1, int(np.floor(s_cross + 0.5))):
    R_n = n * (2*s_cross - n) / (2*s_cross - 1)
    R_n1 = (n+1) * (2*s_cross - n - 1) / (2*s_cross - 1)
    print(f"  R_{{{n+1},1}}/R_{{{n},1}} = {R_n1/R_n:.6f}")

# What about R_{2,1}/R_{1,1}? That's just R_{2,1} = phi (already checked).

# Show the actual wall s values vs the required s
print(f"\n--- Wall s values vs required s = {s_cross:.4f} ---")
for c in configs:
    ratio_s = c['s_PT'] / s_cross
    print(f"  r_ba={c['r_ba']:.2f}, eta={c['eta']:.2f}: s = {c['s_PT']:.4f} "
          f"(ratio to target: {ratio_s:.4f})")


# ===========================================================================
# 10. ALSO CHECK: WALL MODES AS RELATIVE ENERGIES TO lambda_fold
# ===========================================================================

print("\n" + "=" * 70)
print("10. ALTERNATIVE RATIO: MODE ENERGIES RELATIVE TO lambda_fold")
print("=" * 70)

# Another physical interpretation: the "masses" are lambda_fold + delta_E_n
# where delta_E_n are the PT excitation energies.
# Then the ratio would be (lambda_fold + delta_E_2) / (lambda_fold + delta_E_1)

if best_config is not None:
    s = best_config['s_PT']
    w = best_config['w_wall']
    coeff = 1.0 / (2.0 * G_tau_tau * w**2)

    print(f"\nFor best config (r_ba={best_config['r_ba']}, eta={best_config['eta']}):")
    print(f"  lambda_fold = {lam_fold_primary:.6f}")
    print(f"  PT excitation coeff = {coeff:.6f}")

    for n in range(best_config['N_bound']):
        delta_E = n * (2*s - n) * coeff
        total_E = lam_fold_primary + delta_E
        print(f"  n={n}: delta_E = {delta_E:.6f}, total = {total_E:.6f}")

    if best_config['N_bound'] >= 3:
        dE1 = 1 * (2*s - 1) * coeff
        dE2 = 2 * (2*s - 2) * coeff
        total1 = lam_fold_primary + dE1
        total2 = lam_fold_primary + dE2
        ratio_total = total2 / total1
        print(f"\n  total_2 / total_1 = {ratio_total:.6f}")
        print(f"  phi_paasch = {phi_paasch:.6f}")
        print(f"  deviation = {abs(ratio_total - phi_paasch)/phi_paasch:.6f}")


# ===========================================================================
# 11. GATE EVALUATION
# ===========================================================================

print("\n" + "=" * 70)
print("11. GATE PT-RATIO-35 EVALUATION")
print("=" * 70)

# Gate criterion: |E_2/E_1 - 1.53158| / 1.53158 < 0.10
# where E_2/E_1 is the excitation energy ratio Delta_E_2/Delta_E_1

# Collect all R21 values
R21_values = []
for c in configs:
    if c['N_bound'] >= 2:
        R21_values.append((c['r_ba'], c['eta'], c['R21'], c['dev_phi'], c['s_PT']))

print(f"\nAll configurations with >= 2 bound states:")
print(f"{'r_ba':>6} {'eta':>6} {'R_21':>10} {'|dev|':>10} {'s':>8} {'GATE':>8}")

any_pass = False
for r, e, R, dev, s in R21_values:
    status = "PASS" if dev < 0.10 else "FAIL"
    if dev < 0.10:
        any_pass = True
    print(f"{r:6.2f} {e:6.2f} {R:10.6f} {dev:10.6f} {s:8.4f} {status:>8}")

# Also with Berry a_2
print(f"\nWith Berry a_2 = 0.588:")
R21_berry_values = []
for c in configs:
    if c.get('N_bound_berry', 0) >= 2:
        R21_berry_values.append((c['r_ba'], c['eta'], c['R21_berry'],
                                  c['dev_phi_berry'], c['s_berry']))

for r, e, R, dev, s in R21_berry_values:
    status = "PASS" if dev < 0.10 else "FAIL"
    if dev < 0.10:
        any_pass = True
    print(f"{r:6.2f} {e:6.2f} {R:10.6f} {dev:10.6f} {s:8.4f} {status:>8}")

print(f"\n*** GATE PT-RATIO-35: {'PASS' if any_pass else 'FAIL'} ***")
if any_pass:
    # Find best
    best = min(R21_values + R21_berry_values, key=lambda x: x[3])
    print(f"  Best: r_ba={best[0]}, eta={best[1]}, R_21={best[2]:.6f}, "
          f"deviation={best[3]*100:.2f}%, s={best[4]:.4f}")
else:
    # Show closest
    all_results = R21_values + R21_berry_values
    if all_results:
        best = min(all_results, key=lambda x: x[3])
        print(f"  Closest: r_ba={best[0]}, eta={best[1]}, R_21={best[2]:.6f}, "
              f"deviation={best[3]*100:.2f}%, s={best[4]:.4f}")
    print(f"  Required s = {s_cross:.4f}, actual s range: "
          f"[{min(c['s_PT'] for c in configs):.4f}, {max(c['s_PT'] for c in configs):.4f}]")


# ===========================================================================
# 12. WHAT WOULD MAKE IT PASS?
# ===========================================================================

print("\n" + "=" * 70)
print("12. CONDITIONS FOR GATE PASSAGE")
print("=" * 70)

# s_target = 2.6347 gives exact phi. What wall parameters produce this?
# s(s+1) = lambda_PT = 2*G_tt*V_0*w^2
# = 2*G_tt * a_2*(Delta_tau/2)^2 * (Delta_tau/2)^2 * G_tt/(2*delta_V)
# = G_tt^2 * a_2 * (Delta_tau/2)^4 / delta_V

lambda_target = s_cross * (s_cross + 1)
print(f"Required: s = {s_cross:.4f}, lambda_PT = {lambda_target:.4f}")

# For a_2 = 0.588 (Berry) and G_tt = 5.0:
# lambda_target = 25 * 0.588 * (Delta_tau/2)^4 / delta_V
# = 14.7 * (Delta_tau/2)^4 / delta_V

print(f"\nlambda_target = {G_tau_tau**2 * a2_berry:.2f} * (Delta_tau/2)^4 / delta_V")
print(f"             = {G_tau_tau**2 * a2_primary:.2f} * (Delta_tau/2)^4 / delta_V  (fitted a_2)")

# Show required Delta_V for various Delta_tau
print(f"\n{'Delta_tau':>10} {'delta_V_needed':>14} {'delta_V/Delta_tau^4':>20}")
for dt in [0.2, 0.3, 0.4, 0.5, 0.6, 0.8, 1.0]:
    dv_needed = G_tau_tau**2 * a2_primary * (dt/2)**4 / lambda_target
    print(f"{dt:10.2f} {dv_needed:14.6f} {dv_needed/dt**4:20.6f}")

# Compare with actual wall parameters
print(f"\nActual wall parameters:")
for c in configs:
    dv_needed = G_tau_tau**2 * a2_primary * (c['Delta_tau']/2)**4 / lambda_target
    print(f"  r_ba={c['r_ba']:.2f}, eta={c['eta']:.2f}: "
          f"Delta_tau={c['Delta_tau']:.4f}, delta_V={c['delta_V']:.4f}, "
          f"needed delta_V={dv_needed:.4f}, ratio={c['delta_V']/dv_needed:.4f}")


# ===========================================================================
# 13. FIGURE
# ===========================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: B2 eigenvalue with quadratic fit
ax = axes[0, 0]
tau_fine = np.linspace(0.05, 0.50, 500)
B2_fit = quadratic(tau_fine, *popt_near)
B2_berry = b2_min_known + a2_berry * (tau_fine - tau_fold_known)**2

ax.plot(tau_values[1:], B2_values[1:], 'ko', ms=8, label='B2 eigenvalues')
ax.plot(tau_fine, B2_fit, 'b-', lw=2, label=f'Quadratic fit (a_2={a2_primary:.3f})')
ax.plot(tau_fine, B2_berry, 'r--', lw=2, label=f'Berry (a_2={a2_berry:.3f})')
ax.axvline(tau_fold_primary, color='gray', ls=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('lambda_B2')
ax.set_title('B2 Eigenvalue Near Fold')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel B: R_{2,1} vs s
ax = axes[0, 1]
s_plot = np.linspace(1.5, 8.0, 500)
R21_plot = 2.0 * (2.0 * s_plot - 2.0) / (2.0 * s_plot - 1.0)

ax.plot(s_plot, R21_plot, 'b-', lw=2, label='R_{2,1}(s)')
ax.axhline(phi_paasch, color='red', ls='--', lw=2, label=f'phi_paasch = {phi_paasch:.4f}')
ax.axhline(phi_paasch * 1.10, color='red', ls=':', alpha=0.3, label='+/- 10%')
ax.axhline(phi_paasch * 0.90, color='red', ls=':', alpha=0.3)
ax.axvline(s_cross, color='green', ls='--', alpha=0.5, label=f's = {s_cross:.3f}')

# Mark actual wall s values
for c in configs:
    if c['N_bound'] >= 2:
        ax.plot(c['s_PT'], c['R21'], 'ro', ms=10, zorder=5)
        ax.annotate(f"({c['r_ba']},{c['eta']})", (c['s_PT'], c['R21']),
                   textcoords="offset points", xytext=(5, 5), fontsize=7)

ax.set_xlabel('Poschl-Teller parameter s')
ax.set_ylabel('R_{2,1} = Delta_E_2 / Delta_E_1')
ax.set_title('Excitation Energy Ratio vs PT Depth')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_ylim(1.0, 2.2)

# Panel C: PT potential and bound states for best config
ax = axes[1, 0]
if best_config is not None:
    x_pt = np.linspace(-15, 15, 1000)
    V_pt = -best_config['V_0_PT'] / np.cosh(x_pt / best_config['w_wall'])**2
    ax.plot(x_pt, V_pt, 'b-', lw=2, label='PT potential')

    # Mark bound state energies
    s = best_config['s_PT']
    w = best_config['w_wall']
    coeff = 1.0 / (2.0 * G_tau_tau * w**2)
    colors_bs = ['red', 'orange', 'green', 'purple', 'brown']
    for n in range(min(best_config['N_bound'], 5)):
        E_n = -coeff * (s - n)**2
        ax.axhline(E_n, color=colors_bs[n % len(colors_bs)], ls='--', alpha=0.7,
                   label=f'n={n}: E={E_n:.4f}')

    ax.axhline(0, color='black', ls='-', alpha=0.3)
    ax.set_xlabel('x (M_KK^{-1})')
    ax.set_ylabel('V(x)')
    ax.set_title(f'PT Potential (r_ba={best_config["r_ba"]}, eta={best_config["eta"]})')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

# Panel D: Summary table as text
ax = axes[1, 1]
ax.axis('off')
summary_text = "GATE PT-RATIO-35 SUMMARY\n" + "="*40 + "\n\n"
summary_text += f"Pre-registered criterion:\n"
summary_text += f"|R_21 - {phi_paasch}| / {phi_paasch} < 0.10\n\n"
summary_text += f"Required s = {s_cross:.4f}\n"
summary_text += f"Fitted a_2 = {a2_primary:.4f}\n"
summary_text += f"Berry a_2 = {a2_berry}\n\n"

summary_text += f"{'Config':>12} {'s':>6} {'R_21':>8} {'dev%':>8} {'Gate':>6}\n"
summary_text += "-" * 45 + "\n"
for c in configs:
    if c['N_bound'] >= 2:
        status = "PASS" if c['dev_phi'] < 0.10 else "FAIL"
        summary_text += (f"({c['r_ba']:.2f},{c['eta']:.2f}) {c['s_PT']:6.3f} "
                        f"{c['R21']:8.4f} {c['dev_phi']*100:8.2f} {status:>6}\n")

summary_text += f"\nVERDICT: {'PASS' if any_pass else 'FAIL'}\n"
if any_pass and R21_values:
    best = min(R21_values, key=lambda x: x[3])
    summary_text += f"Best: R_21={best[2]:.4f} ({best[3]*100:.1f}%)"

ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', fontfamily='monospace')
ax.set_title('Gate Evaluation')

plt.tight_layout()
plt.savefig('C:/sandbox/Ainulindale Exflation/tier0-computation/s35_poschl_teller.png', dpi=150)
print("\nFigure saved to tier0-computation/s35_poschl_teller.png")


# ===========================================================================
# 14. SAVE RESULTS
# ===========================================================================

# Prepare data for saving
config_array = np.array([(c['r_ba'], c['eta'], c['Delta_tau'], c['w_wall'],
                           c['V_0_PT'], c['lambda_PT'], c['s_PT'], c['N_bound'],
                           c.get('R21', np.nan), c.get('dev_phi', np.nan))
                          for c in configs])

np.savez('C:/sandbox/Ainulindale Exflation/tier0-computation/s35_poschl_teller.npz',
         # B2 eigenvalue data
         tau_values=tau_values,
         B1_values=B1_values,
         B2_values=B2_values,
         B3_values=B3_values,
         # Quadratic fit
         a2_fitted=a2_primary,
         a2_berry=a2_berry,
         tau_fold_fitted=tau_fold_primary,
         lam_fold_fitted=lam_fold_primary,
         tau_fold_dump=tau_fold_known,
         lam_fold_dump=b2_min_known,
         # PT analysis
         phi_paasch=phi_paasch,
         s_required_for_phi=s_cross,
         lambda_required_for_phi=lambda_target,
         G_tau_tau=G_tau_tau,
         # Wall configurations
         config_array=config_array,
         config_columns=np.array(['r_ba', 'eta', 'Delta_tau', 'w_wall',
                                   'V_0_PT', 'lambda_PT', 's_PT', 'N_bound',
                                   'R21', 'dev_phi']),
         # Gate
         gate_pass=any_pass,
         gate_criterion_threshold=0.10
)

print("\nResults saved to tier0-computation/s35_poschl_teller.npz")
print("\nDONE.")
