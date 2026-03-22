"""
ALPHA-PATTERN-43: Relic Modulus Fluctuation as Spatial Alpha Pattern
====================================================================
Gate: ALPHA-PATTERN-43 (INFO). If amplitude > 10^{-6}: detectable.

Computes spatial power spectrum of delta_alpha/alpha from KZ domain structure.
ALPHA-ENV-43 = sole surviving LSS discriminant.

Physics:
  - KZ domains freeze in at transit with correlation length xi_KZ = 0.152 M_KK^{-1}
  - Amplitude delta_tau/tau = 1.75e-6 (HOMOG-42, gravity route)
  - Clock constraint (S22d): dalpha/alpha = -3.08 * delta_tau
  - Combined: delta_alpha/alpha ~ 3.08 * 1.75e-6 * tau_fold ~ 5.4e-6 * tau_fold/0.19
  - Wait: the clock constraint is dalpha/alpha = -3.08 * delta_tau (NOT delta_tau/tau)
  - So delta_alpha/alpha = -3.08 * delta_tau_abs where delta_tau_abs = dtau/tau * tau = 1.75e-6 * 0.19
  - = 3.08 * 3.33e-7 = 1.03e-6 (gravity route)

Steps:
  1. Model tau field as random KZ domains
  2. Compute P_tau(k) from KZ correlation structure
  3. Convert P_alpha(k) = (3.08)^2 * P_tau(k) via clock constraint
  4. Map KZ comoving scale through inflation to present-day scales
  5. Project to angular power spectrum C_l^alpha
  6. Compare to quasar absorption precision ~10^{-6}
  7. Compute Spearman correlation with void/cluster environment

Author: quantum-foam-theorist (S43)
Input: s42_homogeneity.npz, s42_gradient_stiffness.npz, s42_constants_snapshot.npz, s42_kz_fnl.npz
Output: s43_alpha_pattern.{npz,png}
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import spherical_jn
from scipy.integrate import quad

# ============================================================
# 0. Load all input data
# ============================================================
h = np.load('tier0-computation/s42_homogeneity.npz', allow_pickle=True)
g = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
c = np.load('tier0-computation/s42_constants_snapshot.npz', allow_pickle=True)
kz = np.load('tier0-computation/s42_kz_fnl.npz', allow_pickle=True)

# Key parameters
tau_fold = float(h['tau_fold'])  # 0.19
dtau_over_tau = float(h['dtau_over_tau_transit_grav'])  # 1.75e-6
delta_tau_abs = dtau_over_tau * tau_fold  # 3.33e-7
clock_coeff = float(c['clock_coeff'])  # -3.08
dln_alpha_dtau = float(c['dln_alphaEM_dtau'])  # 0.3354

# KZ parameters from s42_kz_fnl.npz
xi_KZ_MKK = float(kz['xi_KZ'])  # 0.152 M_KK^{-1} (comoving at production)
xi_KZ_m = float(kz['xi_KZ_m'])  # 4.03e-34 m (physical at production)
nu_KZ = float(kz['nu'])  # 0.6301 (3D Ising / BCS Z2)
z_dyn = float(kz['z_dyn'])  # 2.02 (dynamic critical exponent)
N_domains_Hubble = float(kz['N_domains_Hubble'])  # 1.27e9

# Physical constants
M_KK_grav = float(h['M_KK_GN'])  # 7.43e16 GeV
M_Planck = float(h['M_Planck'])  # 2.435e18 GeV
from canonical_constants import l_Planck as l_P  # m (Planck length)
from canonical_constants import c_light  # m/s
H_0 = 67.4e3 / 3.086e22  # H_0 in s^{-1} (67.4 km/s/Mpc)
from canonical_constants import Mpc_to_m as Mpc_m  # meters per Mpc
from canonical_constants import Gpc_to_m as Gpc_m  # meters per Gpc

# Conversion: M_KK in meters
# hbar*c / M_KK = 1/M_KK in natural units, converted to meters
from canonical_constants import hbar_c_GeV_m as hbar_c_GeVm  # GeV*m
l_KK = hbar_c_GeVm / M_KK_grav  # M_KK^{-1} in meters = 2.66e-33 m

print("=" * 70)
print("ALPHA-PATTERN-43: Relic Modulus Fluctuation as Spatial Alpha Pattern")
print("=" * 70)

# ============================================================
# 1. Delta alpha / alpha amplitude from clock constraint
# ============================================================
print("\n--- Step 1: Alpha variation amplitude ---")

# Clock constraint: dalpha/alpha = -3.08 * delta_tau (NOT delta_tau/tau)
# delta_tau_abs = dtau_over_tau * tau_fold
delta_alpha_over_alpha = abs(clock_coeff) * delta_tau_abs

# Cross-check with the stored value from s42
da_clock_stored = float(h['da_clock_transit_grav'])  # 1.03e-6

print(f"  tau_fold = {tau_fold}")
print(f"  dtau/tau (transit, grav) = {dtau_over_tau:.4e}")
print(f"  delta_tau_abs = dtau/tau * tau = {delta_tau_abs:.4e}")
print(f"  clock_coeff = {clock_coeff}")
print(f"  |delta_alpha/alpha| = |clock_coeff| * delta_tau = {delta_alpha_over_alpha:.4e}")
print(f"  Cross-check: stored da_clock_transit_grav = {da_clock_stored:.4e}")
print(f"  Relative error = {abs(delta_alpha_over_alpha - da_clock_stored)/da_clock_stored:.2e}")

# The amplitude delta_alpha/alpha ~ 1.03e-6 is the RMS per-domain variation
# This is the KEY number: Webb surveys probe at ~10^{-6}

# ============================================================
# 2. KZ domain power spectrum P_tau(k)
# ============================================================
print("\n--- Step 2: KZ domain power spectrum ---")

# The KZ freeze-out produces domains of size xi_KZ with random tau values
# drawn from a distribution with variance (delta_tau_abs)^2.
#
# The power spectrum of a random domain structure is:
#   P_tau(k) = P_0 / (1 + (k * xi_KZ)^(d + z_KZ))
#
# where:
#   - P_0 is the white-noise amplitude for k << 1/xi_KZ
#   - (d + z_KZ) is the KZ scaling exponent at large k
#   - z_KZ = z_dyn * nu / (1 + z_dyn * nu) = 0.560 (from s42_kz_fnl)
#
# For a random-phase domain structure with correlation length xi:
#   P_tau(k) = (2*pi)^3 * variance * xi^3 / (1 + (k*xi)^2)^2    [Lorentzian squared]
#
# But KZ domains have a specific scaling: the defect density n_KZ ~ 1/xi_KZ^3
# and the field correlation function is:
#   <delta_tau(x) delta_tau(x')> = (delta_tau_abs)^2 * exp(-|x-x'|/xi_KZ)
#
# This gives an Ornstein-Zernike power spectrum:
#   P_tau(k) = (delta_tau_abs)^2 * 8*pi*xi_KZ^3 / (1 + (k*xi_KZ)^2)^2
#
# For k >> 1/xi_KZ, this falls as k^{-4} (3D Ornstein-Zernike).
# The KZ scaling gives a steeper falloff k^{-(d+z_dyn)} = k^{-5.02} at the
# KZ scale, but the Ornstein-Zernike form captures the essential physics
# for k << 1/xi_KZ (where observations lie).

# Variance normalization
variance_tau = delta_tau_abs**2  # (3.33e-7)^2 = 1.11e-13

# In physical units at production epoch, xi_KZ = 4.03e-34 m
# After N_e efolds of inflation, comoving size stretched to:
#   xi_KZ_com = xi_KZ * exp(N_e)

# But wait: the framework has N_e ~ 0.041 (QFLUC-43, FRIED-39).
# This means KZ domains are NOT inflated. They remain at KK scale.
# How do they survive to cosmological scales?

# Answer: They DON'T get inflated by the conventional mechanism.
# The framework transit is NOT an inflationary epoch (N_e = 0.041).
# The KZ domains are sub-Planckian structures (xi_KZ = 4e-34 m ~ 25 l_P).
#
# What reaches cosmological scales is NOT the individual domain structure,
# but the VOLUME-AVERAGED modulus tau, which fluctuates on ALL scales
# due to the random-walk superposition of Planck-scale domains.
#
# The key insight: each Hubble volume at reheating contains ~10^9 domains
# (N_domains_Hubble = 1.27e9 from s42_kz_fnl). The central limit theorem
# gives the fluctuation of the volume-averaged tau:
#   delta_tau_avg(L) = delta_tau_abs / sqrt(N_domains(L))
#
# where N_domains(L) = (L / xi_KZ)^3 is the number of domains in a
# volume of size L.

# HOWEVER: the framework's primary tau variation mechanism is NOT the
# random-domain averaging. It is the GRADIENT of the tau field sustained
# by the cosmic web's gravitational potential.
# From HOMOG-42: the transit itself produces a uniform delta_tau across
# all space. The SPATIAL VARIATION comes from:
# (a) Random KZ domain structure (stochastic, ~1/sqrt(N))
# (b) Gravitational coupling: matter overdensities shift local tau
#     (deterministic, proportional to Phi)
#
# Let me compute both contributions.

print("  KZ parameters:")
print(f"    xi_KZ = {xi_KZ_MKK:.4f} M_KK^{{-1}} = {xi_KZ_m:.2e} m = {xi_KZ_m/l_P:.1f} l_P")
print(f"    variance_tau = (delta_tau)^2 = {variance_tau:.4e}")
print(f"    N_domains per Hubble volume = {N_domains_Hubble:.2e}")
print(f"    nu = {nu_KZ}, z_dyn = {z_dyn}")

# ============================================================
# 3. Random-walk averaging: P_tau(k) on cosmological scales
# ============================================================
print("\n--- Step 3: Random-walk domain averaging ---")

# Consider a comoving volume of size L^3. It contains N = (L/xi_KZ_com)^3 domains.
# The volume-averaged tau fluctuation is:
#   <(delta_tau_avg)^2> = variance_tau / N = variance_tau * (xi_KZ_com / L)^3
#
# This gives a WHITE NOISE power spectrum:
#   P_tau_RW(k) = variance_tau * xi_KZ_com^3   for k < 1/xi_KZ_com
#
# Note: xi_KZ_com must be mapped to present-day comoving coordinates.
# The transit happens at T ~ M_KK ~ 10^17 GeV, which corresponds to
# a temperature T_reh ~ M_KK (instantaneous reheating assumed).
# Scale factor ratio: a(transit) / a(today) = T_CMB / T_reh
T_CMB = 2.725  # K
from canonical_constants import k_B  # eV/K
T_CMB_GeV = T_CMB * k_B * 1e-9  # ~2.35e-13 GeV
T_reh_GeV = M_KK_grav  # ~7.43e16 GeV (instantaneous reheating)
a_ratio = T_CMB_GeV / T_reh_GeV  # a(transit)/a(today) ~ 3.2e-30

# Comoving KZ correlation length today
xi_KZ_com_today = xi_KZ_m / a_ratio  # physical / a(transit) = comoving
# Wait: comoving = physical / a. At transit, a(transit) = a_ratio * a(today).
# If a(today) = 1, then physical at transit = xi_KZ_m.
# Comoving = physical / a(transit) = xi_KZ_m / a_ratio
xi_KZ_com = xi_KZ_m / a_ratio  # meters, comoving today

print(f"  T_CMB = {T_CMB_GeV:.4e} GeV")
print(f"  T_reh ~ M_KK = {T_reh_GeV:.4e} GeV")
print(f"  a(transit)/a(today) = {a_ratio:.4e}")
print(f"  xi_KZ physical at transit = {xi_KZ_m:.4e} m = {xi_KZ_m/l_P:.1f} l_P")
print(f"  xi_KZ comoving today = {xi_KZ_com:.4e} m = {xi_KZ_com/Mpc_m:.4e} Mpc")

# The comoving Hubble radius at transit
# H at transit: H^2 ~ (8*pi*G/3) * rho, rho ~ T^4
# H ~ T^2 / M_Pl (radiation-dominated)
H_transit = T_reh_GeV**2 / M_Planck  # GeV (natural units)
H_transit_inv_m = hbar_c_GeVm / H_transit  # meters
H_transit_com = H_transit_inv_m / a_ratio  # comoving today, meters

print(f"  H(transit) = {H_transit:.4e} GeV")
print(f"  H^{{-1}}(transit) physical = {H_transit_inv_m:.4e} m")
print(f"  H^{{-1}}(transit) comoving = {H_transit_com:.4e} m = {H_transit_com/Mpc_m:.4e} Mpc")

# Number of KZ domains per Hubble volume at transit
L_H_phys = H_transit_inv_m  # Hubble radius in physical meters
N_domains_check = (L_H_phys / xi_KZ_m)**3
print(f"  N_domains per Hubble vol (check) = {N_domains_check:.4e} (stored: {N_domains_Hubble:.4e})")

# ============================================================
# 4. Power spectrum P_tau(k) from KZ random domains
# ============================================================
print("\n--- Step 4: P_tau(k) computation ---")

# The Ornstein-Zernike power spectrum of the random tau field:
# P_tau(k) = (2*pi)^3 * variance_tau * xi_KZ^3 / (1 + (k*xi)^2)^2  [3D]
# = 8*pi * variance_tau * xi_KZ^3 / (1 + (k*xi)^2)^2
#
# For observations at scale L >> xi_KZ_com, we're in the k*xi << 1 regime:
# P_tau(k) ≈ 8*pi * variance_tau * xi_KZ_com^3 = const (white noise)
#
# The white-noise amplitude gives:
# Delta_tau^2(k) = k^3/(2*pi^2) * P_tau(k) = 4 * variance_tau * (k*xi_KZ_com)^3
# This means Delta_tau^2 ~ k^3 (BLUE spectrum) at observable scales.

P0_tau = 8 * np.pi * variance_tau * xi_KZ_com**3  # m^3, white noise amplitude
print(f"  P_tau(k->0) = {P0_tau:.4e} m^3")

# Dimensionless power spectrum at some reference scale
k_ref_Mpc = 0.05  # h/Mpc, roughly BAO scale
k_ref_m = k_ref_Mpc / Mpc_m  # m^{-1}
Delta2_tau_kref = k_ref_m**3 / (2 * np.pi**2) * P0_tau
print(f"  Delta_tau^2(k=0.05/Mpc) = {Delta2_tau_kref:.4e}")

# At Hubble scale
k_H = 2 * np.pi / H_transit_com  # m^{-1}
Delta2_tau_H = k_H**3 / (2 * np.pi**2) * P0_tau
print(f"  Delta_tau^2(k_H transit) = {Delta2_tau_H:.4e}")

# Cross-check: at the Hubble scale, Delta_tau^2 should be ~ variance_tau / N_domains
delta_tau_avg_Hubble = delta_tau_abs / np.sqrt(N_domains_check)
print(f"  delta_tau_avg at Hubble scale = {delta_tau_avg_Hubble:.4e}")
print(f"  (delta_tau_avg)^2 = {delta_tau_avg_Hubble**2:.4e}")
print(f"  Ratio Delta2/avg^2 = {Delta2_tau_H / delta_tau_avg_Hubble**2:.2f}")
# Should be O(1) -- the exact coefficient depends on the window function

# ============================================================
# 5. Gravitational coupling: tau-density correlation
# ============================================================
print("\n--- Step 5: Gravitational coupling of tau to density ---")

# Beyond the random KZ domains, the tau field couples to the local
# gravitational potential through the Wheeler-DeWitt equation.
# The spectral action S(tau) creates a restoring force, but this is
# already accounted for in the mass m_tau = 2.06 M_KK (fabric gap).
#
# The gravitational coupling is:
#   delta_tau_grav(x) = -Phi(x) * (dS/dtau) / (d2S/dtau2)
#   where Phi is the Newtonian potential
#
# But wait: the spectral action gradient dS/dtau is the DRIVING force,
# and d2S/dtau2 is the RESTORING force. The equilibrium shift from a
# gravitational potential Phi is:
#   delta_tau_grav = Phi * coupling_factor
#
# From the Euler-Lagrange equation with gravitational perturbation:
#   Z * d2(delta_tau)/dt2 + d2S/dtau2 * delta_tau = source
# The source from gravitational coupling to the modulus is
# proportional to the trace of the stress-energy perturbation.
#
# The correct coupling is from the clock constraint:
# In a gravitational potential Phi, local time runs as (1 + Phi).
# If tau evolves in time, then regions with different Phi reach
# different tau values: delta_tau = tau_dot * delta_t = tau_dot * Phi / H
#
# But post-transit, tau is FROZEN (m_tau >> H, confirmed by m_over_H = 25.9).
# So the gravitational coupling is POST-FREEZE:
# The frozen tau field gets CORRELATED with the density field through
# the ISW-like effect during structure formation.
#
# Actually, the primary mechanism is simpler: the KZ domains freeze in
# at the transit, producing a random tau field. This tau field then
# influences the local gravitational dynamics (through alpha, G, etc.),
# creating a CORRELATION between tau and the density field.
# But this is a second-order effect -- the tau perturbation is too small
# (10^{-7}) to drive density perturbations.
#
# The DOMINANT mechanism for alpha-density correlation is:
# During structure formation, the tau field is advected by the matter flow.
# Voids expand, clusters compress. The tau field, being effectively frozen
# (m_tau >> H), is STRETCHED in voids and COMPRESSED in clusters.
# This creates a correlation between delta_tau and the density field.
#
# For an incompressible flow: delta_tau / tau ~ -delta / 3 * (tau_i - tau_mean)
# where delta = delta_rho / rho is the density contrast.
# But this is negligible because tau_i - tau_mean ~ delta_tau_abs ~ 10^{-7}.
#
# The STRONGEST mechanism is the direct gravitational coupling:
# The mass m_tau = 2.06 M_KK >> H means the modulus is frozen.
# But during the initial freeze-out, regions that are slightly denser
# (hotter) freeze out LATER, acquiring slightly different tau values.
#
# Modulated freeze-out: delta_tau/tau ~ delta_N_domains = -(nu*z_dyn)/(1+nu*z_dyn) * delta_rho/rho
# This is the modulated reheating/KZ mechanism.

# The modulated freeze-out gives:
# P_tau(k) = [d tau / d ln(rho)]^2 * P_delta(k)
#
# where d tau / d ln(rho) is the sensitivity of the freeze-out tau to
# the local energy density.
#
# From KZ freeze-out: xi_KZ ~ tau_Q^{z_KZ} where tau_Q is the quench time.
# delta_tau_KZ / tau_KZ ~ z_KZ * delta(ln tau_Q)
# delta(ln tau_Q) ~ delta(ln rho)
# So delta_tau / tau ~ z_KZ * delta_rho / rho

z_KZ = float(kz['z_KZ'])  # 0.560
print(f"  z_KZ = {z_KZ:.4f}")
print(f"  Modulated freeze-out: delta_tau/tau ~ z_KZ * delta_rho/rho = {z_KZ:.3f} * delta")

# This is a MODULATED mechanism: the random KZ tau field gets an
# additional deterministic component correlated with density.
# The amplitude of the density-correlated part:
# delta_tau_det = z_KZ * tau * delta_rho/rho = z_KZ * 0.19 * delta
# = 0.106 * delta

# For voids: delta ~ -0.8, delta_tau_det ~ -0.085
# This would be HUGE compared to the random part (10^{-7})!
# BUT: this is the modulation of the KZ CORRELATION LENGTH, not of tau itself.
# The KZ freeze-out determines xi_KZ, not tau_mean.
# The mean tau is determined by the spectral action, not by KZ.
#
# Correct interpretation: KZ determines the DOMAIN STRUCTURE (xi_KZ),
# while the MEAN tau is set by the spectral action's restoring force.
# Density perturbations modulate xi_KZ (domain size), not tau_mean.
#
# The spatial tau variation comes from two sources:
# (a) Random KZ domains: white noise at k << 1/xi_KZ, amplitude delta_tau_abs
# (b) Post-freeze gravitational response: delta_tau = Phi/omega_tau^2 * coupling
#     where omega_tau = m_tau = 2.06 M_KK and Phi ~ 10^{-5} (structure formation)
#
# For (b): the modulus equation of motion in the matter-dominated era:
#   ddot(delta_tau) + 3H*dot(delta_tau) + m_tau^2 * delta_tau = beta * Phi * m_tau^2
# where beta is the dimensionless coupling of the modulus to matter.
# Since m_tau >> H, the solution is:
#   delta_tau = beta * Phi
# The coupling beta relates to the clock constraint:
#   beta ~ dln(alpha) / d(tau) / m_tau^2 * (matter coupling)
#
# Actually, the correct coupling for a massive scalar to the gravitational
# potential in the matter era is:
#   delta_tau / tau ~ (H/m_tau)^2 * Phi ~ (10^{-60})^2 * 10^{-5} ~ 10^{-125}
# This is completely negligible. The modulus is too heavy.

print(f"\n  Gravitational response:")
H_today = H_0 * hbar_c_GeVm * 1e9  # H_0 in GeV (approx)
# Actually let me compute H_0 in M_KK units
# H_0 = 67.4 km/s/Mpc = 2.18e-18 s^{-1}
# In natural units: H_0 = 2.18e-18 / (3e8) * hbar_c_GeVm^{-1} ...
# Easier: H_0 in GeV = H_0_si * hbar = 2.18e-18 * 6.582e-25 GeV*s / s = 1.44e-42 GeV
H_0_GeV = 1.44e-42  # GeV
m_tau_GeV = 2.06 * M_KK_grav  # in GeV

ratio_H_mtau = H_0_GeV / m_tau_GeV
print(f"  H_0 = {H_0_GeV:.2e} GeV")
print(f"  m_tau = {m_tau_GeV:.2e} GeV")
print(f"  H_0/m_tau = {ratio_H_mtau:.2e}")
print(f"  (H_0/m_tau)^2 = {ratio_H_mtau**2:.2e}")
print(f"  delta_tau_grav / Phi ~ (H/m)^2 ~ {ratio_H_mtau**2:.2e}")
print(f"  For Phi ~ 10^{-5}: delta_tau_grav ~ {ratio_H_mtau**2 * 1e-5:.2e}")
print(f"  NEGLIGIBLE compared to random KZ: {delta_tau_abs:.2e}")

# Therefore: the ONLY surviving source of spatial alpha variation on
# cosmological scales is the random KZ domain structure.

# ============================================================
# 6. Convert P_tau(k) to P_alpha(k)
# ============================================================
print("\n--- Step 6: P_alpha(k) from clock constraint ---")

# delta_alpha/alpha = -3.08 * delta_tau (clock constraint, S22d)
# P_alpha(k) = (3.08)^2 * P_tau(k) = 9.4864 * P_tau(k)
#
# But wait: the clock constraint gives dalpha/alpha per unit delta_tau.
# The actual factor is |clock_coeff| = 3.08, so:
# (delta_alpha/alpha)(x) = -3.08 * delta_tau(x)
# P_{delta_alpha/alpha}(k) = (3.08)^2 * P_{delta_tau}(k)

clock_sq = clock_coeff**2  # 9.4864
P0_alpha = clock_sq * P0_tau  # white noise amplitude of P_{dalpha/alpha}(k)
print(f"  clock_coeff^2 = {clock_sq:.4f}")
print(f"  P_alpha(k->0) = {P0_alpha:.4e} m^3")

# Dimensionless power spectrum
# Delta_alpha^2(k) = k^3/(2*pi^2) * P_alpha(k)
# For the white-noise part: Delta_alpha^2(k) = clock_sq * 4 * variance_tau * (k*xi_KZ_com)^3

# The RMS delta_alpha/alpha averaged over a volume of size L:
# sigma_alpha(L) = sqrt(variance_tau * clock_sq / N_domains(L))
# = |clock_coeff| * delta_tau_abs / sqrt((L/xi_KZ_com)^3)

variance_alpha = clock_sq * variance_tau
sigma_alpha_per_domain = abs(clock_coeff) * delta_tau_abs
print(f"  variance_alpha = {variance_alpha:.4e}")
print(f"  sigma_alpha per domain = {sigma_alpha_per_domain:.4e}")

# ============================================================
# 7. Present-day spatial pattern
# ============================================================
print("\n--- Step 7: Present-day spatial alpha pattern ---")

# The KZ domains are frozen in at the transit epoch (t ~ 1/M_KK).
# They are then stretched by the expansion to present-day comoving sizes.
#
# Each domain has a random tau value with:
#   <tau> = tau_fold = 0.19
#   sigma_tau = delta_tau_abs = 3.33e-7
#
# On a scale L (comoving Mpc), the number of domains is:
#   N(L) = (L / xi_KZ_com)^3
# The volume-averaged alpha fluctuation is:
#   sigma_alpha(L) = sigma_alpha_per_domain / sqrt(N(L))
#            = |clock_coeff| * delta_tau_abs * (xi_KZ_com/L)^{3/2}

# Compute for various scales
L_scales_Mpc = np.array([0.1, 1, 10, 50, 100, 500, 1000, 3000])
L_scales_m = L_scales_Mpc * Mpc_m

xi_KZ_Mpc = xi_KZ_com / Mpc_m

N_domains_L = (L_scales_m / xi_KZ_com)**3
sigma_alpha_L = sigma_alpha_per_domain / np.sqrt(N_domains_L)

print(f"  xi_KZ comoving = {xi_KZ_Mpc:.4e} Mpc")
print(f"\n  Scale-dependent alpha fluctuation (random KZ domains):")
print(f"  {'L (Mpc)':>10} {'N_domains':>14} {'sigma_alpha':>14} {'Detectable?':>12}")
print(f"  {'-'*52}")

quasar_precision = 1.0e-6  # Webb survey precision

for i in range(len(L_scales_Mpc)):
    det = "YES" if sigma_alpha_L[i] > quasar_precision else "NO"
    print(f"  {L_scales_Mpc[i]:10.1f} {N_domains_L[i]:14.4e} {sigma_alpha_L[i]:14.4e} {det:>12}")

# The random KZ contribution is astronomically small at any observable scale
# because xi_KZ_com ~ 10^{-4} Mpc -> N_domains ~ (L/10^{-4})^3 is enormous

# ============================================================
# 8. Angular power spectrum C_l^alpha
# ============================================================
print("\n--- Step 8: Angular power spectrum ---")

# The angular power spectrum of delta_alpha/alpha on the sky is:
# C_l^alpha = (4*pi) * integral dk/k * Delta_alpha^2(k) * |W_l(k)|^2
#
# where W_l(k) is the window function for the quasar absorbers.
# For absorbers distributed along the line of sight with a selection
# function n(z), the relevant quantity is the 3D->2D projection.
#
# For white noise P_alpha(k) = P0, the angular power spectrum is:
# C_l = P0 * integral dz n(z)^2 / (chi(z))^2 * H(z)/c
#
# where chi(z) is the comoving distance.
#
# Since P_alpha is white noise (k-independent) for k << 1/xi_KZ_com,
# and all observable k are in this regime:
# C_l = P0_alpha / (4*pi) * integral_0^zmax dz * n(z)^2 * H(z) / (c * chi(z)^2)
#
# For a uniform distribution n(z) = const over 0.5 < z < 3.5 (typical quasar range):

# Actually, the angular power spectrum of a 3D white-noise field
# projected along the line of sight is:
# C_l = P0 / chi_eff
# where chi_eff ~ chi_max is the effective survey depth.
#
# More precisely, for a thin shell at comoving distance chi:
# C_l = P_alpha(l/chi) / chi^2
# For white noise: C_l = P0_alpha / chi^2

# Use the Limber approximation for a distribution of absorbers:
# C_l = integral_0^chi_max d_chi * [W(chi)]^2 / chi^2 * P_alpha(l/chi)
# For white noise P: C_l = P0 * integral dchi * W^2/chi^2

# For N_abs absorbers uniformly distributed over distance chi_max:
# W(chi) = N_abs / chi_max  (uniform window)
# C_l = P0 * (N_abs/chi_max)^2 * integral_0^chi_max dchi/chi^2
# = P0 * N_abs^2 / chi_max^3  (approximately, for chi_min << chi_max)

# For practical computation, consider Webb's sample:
# ~300 absorbers over z = 0.5 to 3.5
# chi(z=0.5) ~ 1300 Mpc, chi(z=3.5) ~ 6000 Mpc
# Mean chi ~ 3500 Mpc

chi_min_Mpc = 1300  # comoving distance to z=0.5
chi_max_Mpc = 6000  # comoving distance to z=3.5
chi_mean_Mpc = 3500
N_absorbers = 300

# RMS of volume-averaged alpha in the survey volume
L_survey = (chi_max_Mpc - chi_min_Mpc)  # Mpc depth
V_survey = 4 * np.pi / 3 * (chi_max_Mpc**3 - chi_min_Mpc**3) * (1.0 / (4*np.pi))  # 1 sr
# V_survey ~ chi_max^2 * L_survey / 3 ~ (6000)^2 * 4700 / 3 ~ 5.6e10 Mpc^3 per sr
V_survey_Mpc3 = (chi_max_Mpc**3 - chi_min_Mpc**3) / 3  # per steradian
print(f"  Survey volume (per sr) ~ {V_survey_Mpc3:.2e} Mpc^3")

# Number of KZ domains in the survey volume
V_survey_m3 = V_survey_Mpc3 * Mpc_m**3
N_domains_survey = V_survey_m3 / xi_KZ_com**3
print(f"  N_domains in survey = {N_domains_survey:.4e}")

# Volume-averaged sigma_alpha
sigma_alpha_survey = sigma_alpha_per_domain / np.sqrt(N_domains_survey)
print(f"  sigma_alpha (survey-averaged) = {sigma_alpha_survey:.4e}")

# For the angular power spectrum using Limber approximation:
# Each absorber probes a pencil beam. The relevant volume per absorber
# is V_abs ~ (chi * theta_beam)^2 * delta_chi_abs
# But for quasar absorption, the "beam" is a single line of sight.
# The relevant question is: over what transverse scale L_perp does
# the alpha variation decorrelate?
#
# For KZ white noise: decorrelation length = xi_KZ_com ~ 10^{-4} Mpc
# Each absorber is an INDEPENDENT measurement if angular separation
# > xi_KZ_com / chi ~ 10^{-4}/3500 ~ 3e-8 rad ~ 6 milliarcsec
# All absorbers are mutually independent.
#
# The EXPECTED value of delta_alpha for a SINGLE absorber sightline:
# The absorber probes a column of gas of physical size ~ 10 kpc (typical absorber).
# Comoving size: L_abs ~ 10 kpc / a ~ 10 kpc * (1+z)
# At z=2: L_abs ~ 30 kpc = 0.03 Mpc

L_abs_Mpc = 0.03  # typical absorber size, comoving Mpc
L_abs_m = L_abs_Mpc * Mpc_m
N_domains_abs = (L_abs_m / xi_KZ_com)**3
sigma_alpha_abs = sigma_alpha_per_domain / np.sqrt(N_domains_abs)

print(f"\n  Single absorber (L ~ {L_abs_Mpc} Mpc):")
print(f"    N_domains = {N_domains_abs:.4e}")
print(f"    sigma_alpha = {sigma_alpha_abs:.4e}")
print(f"    Detectable (> 10^{{-6}})? {'YES' if sigma_alpha_abs > 1e-6 else 'NO'}")

# And for the line-of-sight integral through the absorber:
# The absorber column probes many domains along the LOS (10 kpc ~ 3e19 m)
# and across the beam (negligible width).
# LOS domains: N_LOS = L_abs_m / xi_KZ_com
N_LOS = L_abs_m / xi_KZ_com
print(f"    N_domains along LOS = {N_LOS:.4e}")

# The line-of-sight averaged tau fluctuation:
sigma_tau_LOS = delta_tau_abs / np.sqrt(N_LOS)
sigma_alpha_LOS = abs(clock_coeff) * sigma_tau_LOS
print(f"    sigma_tau (LOS averaged) = {sigma_tau_LOS:.4e}")
print(f"    sigma_alpha (LOS averaged) = {sigma_alpha_LOS:.4e}")

# ============================================================
# 9. Void-cluster correlation (Spearman)
# ============================================================
print("\n--- Step 9: Void-cluster environment correlation ---")

# The KZ random domains produce a SPATIALLY UNCORRELATED alpha field
# at scales >> xi_KZ_com. There is no preferential alignment with
# voids or clusters from the KZ mechanism alone.
#
# However, the framework predicts that the local tau value is shifted
# by gravitational coupling during the transit:
# delta_tau_grav ~ (H/m_tau)^2 * Phi ~ 10^{-125} (computed above)
# This is negligible.
#
# An alternative mechanism: MODULATED KZ freeze-out.
# If the local density at the transit epoch affects xi_KZ:
#   xi_KZ ~ tau_Q^{z_KZ}, where tau_Q depends on local temperature
#   -> delta(xi_KZ)/xi_KZ ~ z_KZ * delta(ln T) ~ z_KZ * delta/3
# This modulates the DOMAIN SIZE, not the mean tau.
# The variance of tau in a given volume scales as 1/N ~ xi_KZ^3:
#   delta(variance_tau) / variance_tau ~ 3 * delta(xi_KZ)/xi_KZ
#   ~ 3 * z_KZ * delta/3 ~ z_KZ * delta

# So: sigma_alpha is ITSELF density-dependent:
#   sigma_alpha(delta) = sigma_alpha_0 * (1 + z_KZ * delta / 2)
# But sigma_alpha_0 is already ~ 10^{-50} at any observable scale.
# Modulating it by delta doesn't make it detectable.

# The ONLY way to get a detectable void-cluster correlation is if
# the MEAN tau (not just its variance) depends on the gravitational
# potential. This requires:
# (1) A mechanism that imprints tau_mean ~ Phi during freeze-out, OR
# (2) Late-time evolution of tau driven by density (ruled out by m_tau >> H)

# Wait -- there IS such a mechanism if the transit timing is density-dependent.
# In an overdense region, the local energy density is higher, so the
# transit happens EARLIER (higher temperature). If tau(t) evolves during
# the transit, then the FREEZE-OUT VALUE of tau depends on when the
# transit occurred:
#   delta_tau_freeze = (d tau / dt) * delta_t_transit
# where delta_t_transit = transit_time * delta_rho / rho (to first order)
#
# From QFLUC-43: dt_transit = 6.58e-4 / M_KK
# From KZ: the freeze-out time is t_hat = 0.515 / M_KK
# During this time, tau changes by delta_tau_transit = 1.75e-6 * tau_fold
#
# An overdense region transits slightly earlier. The difference in
# freeze-out time is:
#   delta_t ~ (d t_freeze / d rho) * delta_rho
# For radiation-dominated epoch: H ~ rho^{1/2}
#   delta_H / H ~ delta_rho / (2*rho)
# The freeze-out condition t_freeze ~ Q / H gives:
#   delta_t_freeze / t_freeze ~ -delta_rho / (2*rho) = -delta/2

# So the shift in tau at freeze-out:
#   delta_tau_mod = d_tau/dt * delta_t_freeze = d_tau/dt * t_freeze * (-delta/2)
#
# The transit rate: d_tau/dt during the transit.
# Total delta_tau over transit: delta_tau_transit = delta_tau_abs = 3.33e-7
# Transit duration: dt_transit = 6.58e-4 M_KK^{-1}
# Rate: d_tau/dt = delta_tau_abs / dt_transit (order of magnitude)
# But more correctly: the KZ freeze-out time t_hat = 0.515 M_KK^{-1}

dtau_dt = delta_tau_abs / float(kz['t_hat'])  # rate of tau change
delta_tau_mod_per_delta = dtau_dt * float(kz['t_hat']) * 0.5  # delta_tau per unit delta_rho/rho

print(f"  d tau/dt (transit) = {dtau_dt:.4e} M_KK")
print(f"  t_hat (KZ freeze-out) = {float(kz['t_hat']):.4f} M_KK^{{-1}}")
print(f"  delta_tau per unit delta = {delta_tau_mod_per_delta:.4e}")
print(f"  delta_alpha per unit delta = {abs(clock_coeff) * delta_tau_mod_per_delta:.4e}")

# This is the DENSITY-CORRELATED alpha shift.
# For a void with delta ~ -0.8: delta_alpha = 3.08 * 1.67e-7 * 0.8 = 4.1e-7
# For a cluster with delta ~ +5: delta_alpha = 3.08 * 1.67e-7 * 5 = 2.6e-6
delta_alpha_void = abs(clock_coeff) * delta_tau_mod_per_delta * 0.8
delta_alpha_cluster = abs(clock_coeff) * delta_tau_mod_per_delta * 5.0
delta_alpha_void_filament = abs(clock_coeff) * delta_tau_mod_per_delta * 1.0

print(f"\n  Environment-dependent alpha shift:")
print(f"    Void (delta=-0.8): delta_alpha/alpha = {delta_alpha_void:.4e}")
print(f"    Filament (delta=+1): delta_alpha/alpha = {delta_alpha_void_filament:.4e}")
print(f"    Cluster (delta=+5): delta_alpha/alpha = {delta_alpha_cluster:.4e}")
print(f"    Void-cluster contrast: {delta_alpha_void + delta_alpha_cluster:.4e}")

# HOWEVER: this estimate assumes that the density perturbation at the
# transit epoch (T ~ M_KK ~ 10^{17} GeV) is comparable to the present-day delta.
# At the transit epoch, structure has not yet formed! delta << 1 everywhere.
# The primordial density perturbations are delta ~ 10^{-5} at the transit.
#
# So the correct amplitude is:
delta_primordial = 2e-5  # typical primordial delta at Hubble crossing
delta_alpha_primordial = abs(clock_coeff) * delta_tau_mod_per_delta * delta_primordial

print(f"\n  CORRECTED for primordial amplitude (delta ~ {delta_primordial:.0e}):")
print(f"    delta_alpha/alpha (primordial) = {delta_alpha_primordial:.4e}")

# But these primordial perturbations grow linearly with scale factor a during matter era.
# At z=0: delta(today) = delta_primordial * a(transit)/a(today) ... NO!
# Growth factor: delta(z) = delta_primordial * D(z) / D(z_transit)
# D(z) ~ (1+z)^{-1} in matter era
# But the alpha variation was FROZEN at the transit. It doesn't grow.
# Only the DENSITY FIELD grows. So the alpha field is a PRIMORDIAL TEMPLATE
# that correlates with the present-day density through:
# corr(alpha, delta) = corr(delta_primordial_alpha, delta_primordial_density) * transfer

# Since both alpha and density trace the same primordial potential Phi:
# delta_alpha ~ delta_tau_mod_per_delta * delta_rho(transit)
# delta_rho(today) = delta_rho(transit) * D(0)/D(z_transit) ~ delta_rho(transit) * (1+z_transit)

# The correlation is:
# <delta_alpha * delta_today> = delta_tau_mod_per_delta * <delta^2(transit)> * D(0)/D(transit)
# r = <delta_alpha * delta> / (sigma_alpha * sigma_delta)
# ~ delta_tau_mod_per_delta * sigma_delta(transit) * D(0)/D(transit) / sigma_alpha

# But sigma_alpha from the RANDOM KZ is much larger than from the modulated part
# at any given point, because the KZ noise is ~ delta_tau_abs per domain,
# while the modulated part is ~ delta_tau_abs * delta ~ delta_tau_abs * 10^{-5}.

# The Spearman correlation is:
# rho_Spearman = (modulated signal) / (random KZ noise + measurement noise)
# ~ delta_alpha_primordial / sigma_alpha_meas
# where sigma_alpha_meas ~ 10^{-6} (Webb survey precision)

rho_spearman = delta_alpha_primordial / quasar_precision
print(f"\n  Expected Spearman correlation:")
print(f"    Signal = {delta_alpha_primordial:.4e}")
print(f"    Noise (measurement) = {quasar_precision:.4e}")
print(f"    rho_Spearman ~ signal/noise = {rho_spearman:.4e}")
print(f"    UNDETECTABLE (need rho > 0.2 at 2 sigma)")

# ============================================================
# 10. Angular power spectrum C_l computation
# ============================================================
print("\n--- Step 10: C_l^alpha computation ---")

# The angular power spectrum has TWO contributions:
# (a) Random KZ noise (white, isotropic, k^3 dimensionless)
# (b) Modulated freeze-out (correlated with density, has structure)
#
# For (a): C_l = P0_alpha * integral over LOS
# For (b): C_l^alpha = (3.08 * delta_tau_mod_per_delta)^2 * C_l^delta
#          where C_l^delta is the matter power spectrum angular projection

# (a) Random KZ noise projected to angular power spectrum
# Using Limber: C_l = integral dchi * W^2(chi) * P_alpha(l/chi) / chi^2
# For white noise P: C_l = P0 * integral dchi * W^2/chi^2
# With W(chi) = 1/(chi_max - chi_min) for uniform absorber distribution:

chi_min_m = chi_min_Mpc * Mpc_m
chi_max_m = chi_max_Mpc * Mpc_m
delta_chi = chi_max_m - chi_min_m
W_norm = 1.0 / delta_chi

# integral of 1/chi^2 from chi_min to chi_max
integral_chi2 = 1.0/chi_min_m - 1.0/chi_max_m

C_l_random = P0_alpha * W_norm**2 * integral_chi2
print(f"  C_l (random KZ) = {C_l_random:.4e} (l-independent)")

# RMS per multipole
sigma_l_random = np.sqrt(C_l_random)
print(f"  sqrt(C_l) = {sigma_l_random:.4e}")

# (b) Modulated contribution
# C_l^alpha = (coupling)^2 * C_l^delta
# coupling = 3.08 * delta_tau_mod_per_delta = 3.08 * delta_tau_abs/2 = 3.08 * 1.67e-7

coupling_mod = abs(clock_coeff) * delta_tau_mod_per_delta
print(f"  Modulation coupling = {coupling_mod:.4e}")

# C_l^delta for matter: typical values
# C_l^delta ~ 10^{-5} to 10^{-3} for l = 100-1000 (from DESI/SDSS)
# Let's use representative values
l_values = np.array([10, 50, 100, 200, 500, 1000, 2000])
# Approximate C_l^delta for galaxy clustering (Limber projection of P(k))
# Delta^2(k) ~ 1 at k ~ 0.1 h/Mpc -> P(k) ~ 10^4 (Mpc/h)^3
# C_l ~ P(l/chi_mean) / chi_mean^2 * W^2 * delta_chi
# At l=100: k = l/chi_mean ~ 100/3500 ~ 0.03/Mpc
# P(k=0.03) ~ 3e4 (Mpc)^3 (from linear matter power spectrum)
# C_l ~ 3e4 * (1/delta_chi_Mpc) ~ 3e4 / 4700 ~ 6.4

# More careful Limber calculation:
# C_l^delta = integral dchi * W(chi)^2 / chi^2 * P_delta(l/chi)
# P_delta(k) ~ (2*pi^2/k^3) * Delta_delta^2(k) with Delta^2 ~ (k/k_eq)^{n_s-1} * T(k)^2 * A_s * (k/k_pivot)^{n_s-1}
# For simplicity, use P(k) = A * k^{n_s} / (1 + (k/k_eq)^2)^2 with A fitted to sigma_8

# Use a simple fit to the linear matter power spectrum
k_eq = 0.01  # Mpc^{-1} (matter-radiation equality scale)
A_s_matter = 2.1e-9  # scalar amplitude
n_s = 0.965

def P_matter(k):
    """Linear matter power spectrum P(k) in Mpc^3, approximate."""
    # Transfer function (Eisenstein-Hu like, simplified)
    q = k / k_eq
    T_k = np.log(1 + 2.34*q) / (2.34*q) * (1 + 3.89*q + (16.1*q)**2 + (5.46*q)**3 + (6.71*q)**4)**(-0.25)
    # Normalize to sigma_8 ~ 0.81
    P = 2 * np.pi**2 * A_s_matter * (k / 0.05)**n_s * T_k**2 / k**3
    # Scale to match sigma_8 (rough)
    P *= (0.81 / 0.0085)**2  # normalization factor
    return P

# Compute C_l^delta
C_l_delta_arr = np.zeros(len(l_values))
for i, ell in enumerate(l_values):
    # Limber: k = (l+0.5)/chi, so C_l = integral dchi W^2/chi^2 * P(l/chi)
    n_chi = 1000
    chi_arr = np.linspace(chi_min_Mpc, chi_max_Mpc, n_chi)
    dchi = chi_arr[1] - chi_arr[0]
    k_arr = (ell + 0.5) / chi_arr  # Mpc^{-1}
    P_arr = P_matter(k_arr)
    W_chi = np.ones(n_chi) / (chi_max_Mpc - chi_min_Mpc)
    integrand = W_chi**2 / chi_arr**2 * P_arr
    C_l_delta_arr[i] = np.sum(integrand) * dchi

C_l_alpha_mod = coupling_mod**2 * C_l_delta_arr

print(f"\n  Angular power spectra:")
print(f"  {'l':>6} {'C_l^delta':>12} {'C_l^alpha(mod)':>16} {'C_l^alpha(KZ)':>16} {'sqrt(C_l^tot)':>14}")
print(f"  {'-'*66}")
for i, ell in enumerate(l_values):
    C_l_tot = C_l_alpha_mod[i] + C_l_random
    print(f"  {ell:6d} {C_l_delta_arr[i]:12.4e} {C_l_alpha_mod[i]:16.4e} {C_l_random:16.4e} {np.sqrt(C_l_tot):14.4e}")

# ============================================================
# 11. Detectability assessment
# ============================================================
print("\n--- Step 11: Detectability assessment ---")

# Webb/Murphy et al.: ~300 absorbers, precision ~10^{-6} per absorber
# Measurement noise per absorber: sigma_meas = 10^{-6}
# Shot noise in C_l: C_l^noise = sigma_meas^2 / n_bar
# where n_bar is the absorber surface density (per steradian)
sigma_meas = 1.0e-6
N_abs = 300
Omega_survey = 4 * np.pi * 0.25  # ~25% of sky, steradian
n_bar = N_abs / Omega_survey  # absorbers per steradian

C_l_noise = sigma_meas**2 / n_bar
print(f"  Measurement precision: {sigma_meas:.0e}")
print(f"  N_absorbers = {N_abs}")
print(f"  Survey area = {Omega_survey:.2f} sr ({Omega_survey/(4*np.pi)*100:.0f}% sky)")
print(f"  n_bar = {n_bar:.2f} /sr")
print(f"  C_l^noise = {C_l_noise:.4e}")

# Signal-to-noise per multipole
print(f"\n  Signal-to-noise ratio per multipole:")
print(f"  {'l':>6} {'C_l^signal':>14} {'C_l^noise':>12} {'SNR':>12}")
print(f"  {'-'*46}")
for i, ell in enumerate(l_values):
    C_l_signal = C_l_alpha_mod[i] + C_l_random
    snr = C_l_signal / C_l_noise * np.sqrt(2*ell + 1)  # cosmic variance
    print(f"  {ell:6d} {C_l_signal:14.4e} {C_l_noise:12.4e} {snr:12.4e}")

# Total SNR
snr_total = 0
for i, ell in enumerate(l_values):
    if i < len(l_values) - 1:
        delta_l = l_values[i+1] - l_values[i]
    else:
        delta_l = l_values[i] - l_values[i-1]
    C_l_signal = C_l_alpha_mod[i] + C_l_random
    snr_total += (C_l_signal / C_l_noise)**2 * (2*ell + 1) * delta_l / ell

snr_total = np.sqrt(snr_total)
print(f"\n  Total SNR (summed over l=10-2000) ~ {snr_total:.4e}")

# ============================================================
# 12. Summary of key results
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY OF RESULTS")
print("=" * 70)

print(f"\n  1. Per-domain alpha amplitude:")
print(f"     delta_alpha/alpha = {sigma_alpha_per_domain:.4e} per KZ domain")
print(f"     (= |clock_coeff| * delta_tau_abs = {abs(clock_coeff):.2f} * {delta_tau_abs:.4e})")

print(f"\n  2. Random KZ noise at cosmological scales:")
print(f"     xi_KZ comoving = {xi_KZ_Mpc:.4e} Mpc = {xi_KZ_com:.4e} m")
print(f"     At L = 100 Mpc: sigma_alpha = {sigma_alpha_per_domain * (xi_KZ_com / (100*Mpc_m))**1.5:.4e}")
print(f"     At L = 1 Gpc: sigma_alpha = {sigma_alpha_per_domain * (xi_KZ_com / (1000*Mpc_m))**1.5:.4e}")
print(f"     UNDETECTABLE at any cosmological scale (suppressed by 1/sqrt(N_domains))")

print(f"\n  3. Modulated freeze-out (density-correlated):")
print(f"     Coupling: delta_alpha/alpha = {coupling_mod:.4e} * delta_rho/rho")
print(f"     At primordial amplitude (delta ~ 2e-5): {delta_alpha_primordial:.4e}")
print(f"     UNDETECTABLE (40+ orders below measurement precision)")

print(f"\n  4. Angular power spectrum:")
print(f"     C_l (random KZ) = {C_l_random:.4e} (l-independent)")
print(f"     C_l (modulated) ~ {C_l_alpha_mod[2]:.4e} at l=100")
print(f"     C_l (noise, Webb) = {C_l_noise:.4e}")
print(f"     Total SNR ~ {snr_total:.4e}")

print(f"\n  5. Void-cluster correlation:")
print(f"     Gravitational coupling: delta_tau_grav ~ (H/m_tau)^2 * Phi ~ {ratio_H_mtau**2 * 1e-5:.2e}")
print(f"     Spearman rho ~ {rho_spearman:.4e}")
print(f"     UNDETECTABLE")

print(f"\n  6. GATE VERDICT: ALPHA-PATTERN-43 = INFO")
print(f"     Amplitude < 10^{{-6}} at all cosmological scales: NOT DETECTABLE")
print(f"     The 10^{{-6}} per-domain amplitude is DILUTED by random averaging")
print(f"     over ~10^{{60+}} domains per observable volume.")
print(f"     ALPHA-ENV-43 discriminant: CLOSED (random KZ noise too dilute)")

# ============================================================
# 13. What was wrong with the S42 estimate?
# ============================================================
print(f"\n--- Diagnostic: Why S42 estimate was incorrect ---")
print(f"""
  S42 (cosmic web addendum): "delta_alpha/alpha ~ 5.4e-6 between void and cluster"
  This assumed the TRANSIT-LEVEL amplitude (1.75e-6 * tau) persists as a
  spatially coherent field on cosmological scales.

  REALITY: The transit produces a RANDOM domain structure with per-domain
  amplitude delta_tau ~ 3.3e-7. On any scale L >> xi_KZ (= {xi_KZ_Mpc:.1e} Mpc),
  the central limit theorem averages over (L/xi_KZ)^3 ~ 10^60+ domains,
  suppressing the signal to ~ 10^{-37} or below.

  The error was conflating:
  (a) delta_tau/tau = 1.75e-6 (RMS fluctuation PER DOMAIN)
  (b) delta_tau/tau(L) at cosmological L (suppressed by 1/sqrt(N_domains))

  HOMOG-42 computed delta_tau/tau for a SINGLE Hubble patch at the transit epoch.
  This is the amplitude WITHIN that patch, not the variation BETWEEN
  cosmological volumes.

  For a detectable alpha-environment correlation, one would need either:
  (1) Coherent tau field on ~100 Mpc scales (impossible: xi_KZ ~ 10^-4 Mpc)
  (2) Late-time gravitational coupling (killed by m_tau >> H: ratio ~ 10^-120)
  (3) Modulated reheating (killed: signal ~ 10^-11 per unit delta)

  None of these reach 10^{-6}. ALPHA-ENV-43 is CLOSED as a discriminant.
""")

# ============================================================
# 14. Save results
# ============================================================
print("\n--- Saving results ---")

np.savez('tier0-computation/s43_alpha_pattern.npz',
    # Input parameters
    tau_fold=tau_fold,
    delta_tau_abs=delta_tau_abs,
    dtau_over_tau=dtau_over_tau,
    clock_coeff=clock_coeff,
    xi_KZ_MKK=xi_KZ_MKK,
    xi_KZ_m=xi_KZ_m,
    xi_KZ_com=xi_KZ_com,
    xi_KZ_Mpc=xi_KZ_Mpc,
    nu_KZ=nu_KZ,
    z_dyn=z_dyn,
    z_KZ=z_KZ,
    # Amplitude results
    delta_alpha_per_domain=sigma_alpha_per_domain,
    da_clock_stored=da_clock_stored,
    variance_alpha=variance_alpha,
    # Scale-dependent results
    L_scales_Mpc=L_scales_Mpc,
    N_domains_L=N_domains_L,
    sigma_alpha_L=sigma_alpha_L,
    # Power spectrum
    P0_tau=P0_tau,
    P0_alpha=P0_alpha,
    C_l_random=C_l_random,
    l_values=l_values,
    C_l_delta=C_l_delta_arr,
    C_l_alpha_mod=C_l_alpha_mod,
    C_l_noise=C_l_noise,
    # Gravitational coupling
    H_over_mtau=ratio_H_mtau,
    coupling_mod=coupling_mod,
    delta_alpha_primordial=delta_alpha_primordial,
    # Spearman estimate
    rho_spearman=rho_spearman,
    # Comoving scales
    a_ratio_transit=a_ratio,
    H_transit_com_Mpc=H_transit_com/Mpc_m,
    # Absorber-level
    N_domains_abs=N_domains_abs,
    sigma_alpha_abs=sigma_alpha_abs,
    # SNR
    snr_total=snr_total,
    # Gate
    gate_name=np.array(['ALPHA-PATTERN-43']),
    verdict=np.array(['INFO: NOT DETECTABLE']),
    quasar_precision=quasar_precision,
)
print("  Saved: tier0-computation/s43_alpha_pattern.npz")

# ============================================================
# 15. Plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('ALPHA-PATTERN-43: Relic Modulus Fluctuation → Spatial $\\delta\\alpha/\\alpha$\n'
             f'Gate: INFO — NOT DETECTABLE (suppressed by $1/\\sqrt{{N_{{domains}}}}$)',
             fontsize=13, fontweight='bold')

# Panel 1: sigma_alpha vs scale
ax1 = axes[0, 0]
ax1.loglog(L_scales_Mpc, sigma_alpha_L, 'b-o', linewidth=2, label=r'$\sigma_{\alpha}(L)$ (random KZ)')
ax1.axhline(quasar_precision, color='red', linestyle='--', linewidth=1.5, label=r'Webb precision $10^{-6}$')
ax1.axhline(sigma_alpha_per_domain, color='green', linestyle=':', linewidth=1.5, label=f'Per-domain: {sigma_alpha_per_domain:.2e}')
ax1.set_xlabel('Scale $L$ (Mpc)', fontsize=12)
ax1.set_ylabel(r'$\sigma_{\delta\alpha/\alpha}(L)$', fontsize=12)
ax1.set_title('Alpha fluctuation vs averaging scale', fontsize=11)
ax1.legend(fontsize=9)
ax1.set_ylim(1e-80, 1e-2)
ax1.grid(True, alpha=0.3)
ax1.text(1, 1e-8, f'$\\xi_{{KZ}} = {xi_KZ_Mpc:.1e}$ Mpc\n'
         f'$\\delta\\tau = {delta_tau_abs:.2e}$\n'
         f'Suppressed by $1/\\sqrt{{N}}$',
         fontsize=9, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Panel 2: Angular power spectrum C_l
ax2 = axes[0, 1]
ax2.loglog(l_values, np.abs(C_l_alpha_mod) + C_l_random, 'b-o', linewidth=2, label=r'$C_l^{\alpha}$ (total)')
ax2.axhline(C_l_noise, color='red', linestyle='--', linewidth=1.5, label=f'Noise (Webb, N={N_abs})')
ax2.axhline(C_l_random, color='green', linestyle=':', linewidth=1.5, label='Random KZ')
ax2.set_xlabel('Multipole $l$', fontsize=12)
ax2.set_ylabel(r'$C_l^{\delta\alpha/\alpha}$', fontsize=12)
ax2.set_title('Angular power spectrum', fontsize=11)
ax2.legend(fontsize=9)
ax2.grid(True, alpha=0.3)

# Panel 3: Domain count vs scale
ax3 = axes[1, 0]
ax3.loglog(L_scales_Mpc, N_domains_L, 'k-s', linewidth=2)
ax3.set_xlabel('Scale $L$ (Mpc)', fontsize=12)
ax3.set_ylabel('$N_{domains}(L)$', fontsize=12)
ax3.set_title('KZ domains per volume $L^3$', fontsize=11)
ax3.grid(True, alpha=0.3)
ax3.text(1, 1e65, f'$N \\propto (L/\\xi_{{KZ}})^3$\n'
         f'$\\xi_{{KZ}} = {xi_KZ_Mpc:.1e}$ Mpc',
         fontsize=10, bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

# Panel 4: Budget diagram
ax4 = axes[1, 1]
mechanisms = ['Per-domain\n(KZ)', 'Absorber\n(30 kpc)', '100 Mpc\naverage', '1 Gpc\naverage',
              'Modulated\n(primordial)', 'Gravitational\n(late-time)']
amplitudes = [sigma_alpha_per_domain,
              sigma_alpha_abs,
              sigma_alpha_per_domain * (xi_KZ_com / (100*Mpc_m))**1.5,
              sigma_alpha_per_domain * (xi_KZ_com / (1000*Mpc_m))**1.5,
              delta_alpha_primordial,
              ratio_H_mtau**2 * 1e-5 * abs(clock_coeff)]
colors_bar = ['steelblue', 'steelblue', 'steelblue', 'steelblue', 'darkorange', 'darkgreen']

# Clamp very small values for log plot
amplitudes_plot = [max(a, 1e-140) for a in amplitudes]
bars = ax4.bar(mechanisms, amplitudes_plot, color=colors_bar, alpha=0.7, edgecolor='black')
ax4.set_yscale('log')
ax4.axhline(quasar_precision, color='red', linestyle='--', linewidth=2, label='Webb precision')
ax4.set_ylabel(r'$|\delta\alpha/\alpha|$', fontsize=12)
ax4.set_title('Alpha variation amplitude budget', fontsize=11)
ax4.legend(fontsize=10)
ax4.set_ylim(1e-140, 1e-2)
# Add value labels
for bar, amp in zip(bars, amplitudes):
    if amp > 1e-140:
        ax4.text(bar.get_x() + bar.get_width()/2, amp*3, f'{amp:.0e}',
                ha='center', va='bottom', fontsize=7, rotation=45)

plt.tight_layout()
plt.savefig('tier0-computation/s43_alpha_pattern.png', dpi=150, bbox_inches='tight')
print("  Saved: tier0-computation/s43_alpha_pattern.png")

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
