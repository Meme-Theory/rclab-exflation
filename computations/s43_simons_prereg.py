"""
SIMONS-43: Simons Observatory CMB Lensing Pre-Registration
===========================================================

Compute Planck LCDM CMB lensing convergence power spectrum C_l^{kappa kappa}
at l = 100-2000 using the Limber approximation. This IS the phonon-exflation
framework prediction (framework degenerate with LCDM at all z < z_BCS ~ 10^28).

Cosmology: Planck 2018 (TT,TE,EE+lowE+lensing)
  Omega_m = 0.3153, Omega_b = 0.0493, h = 0.6736
  sigma_8 = 0.8111, n_s = 0.9649

Pre-registration criterion (from Mehta & Mukherjee 2025, Paper 30):
  If Simons Observatory measures C_l^{kappa kappa} enhanced by >3 sigma
  relative to LCDM at z > 2 weighted scales, framework is EXCLUDED.

Gate: SIMONS-43 (INFO — pre-registration, not pass/fail)

Author: Little-Red-Dots-JWST-Analyst
Session: 43
"""

import numpy as np
from scipy.integrate import quad, simpson
from scipy.interpolate import interp1d
from scipy.special import spherical_jn
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# Cosmological Parameters (Planck 2018)
# ============================================================
h = 0.6736
H0 = h * 100  # km/s/Mpc
Omega_m = 0.3153
Omega_b = 0.0493
Omega_cdm = Omega_m - Omega_b
Omega_Lambda = 1.0 - Omega_m
sigma_8 = 0.8111
n_s = 0.9649

# CMB last scattering
z_star = 1089.92
from canonical_constants import c_light_km_s as c_km_s  # km/s

print("=" * 70)
print("SIMONS-43: CMB Lensing Convergence Pre-Registration")
print("=" * 70)
print(f"Cosmology: Planck 2018")
print(f"  Omega_m = {Omega_m}, Omega_b = {Omega_b}, h = {h}")
print(f"  sigma_8 = {sigma_8}, n_s = {n_s}")
print()

# ============================================================
# Background cosmology: E(z), comoving distance chi(z)
# ============================================================
def E(z):
    """Dimensionless Hubble parameter E(z) = H(z)/H0 for flat LCDM."""
    return np.sqrt(Omega_m * (1 + z)**3 + Omega_Lambda)

def chi_integrand(z):
    """d chi / dz = c / H(z) in Mpc."""
    return c_km_s / (H0 * E(z))

# Tabulate chi(z) for interpolation
z_tab = np.linspace(0, z_star + 10, 5000)
chi_tab = np.zeros_like(z_tab)
for i in range(1, len(z_tab)):
    chi_tab[i], _ = quad(chi_integrand, 0, z_tab[i], limit=200)

chi_of_z = interp1d(z_tab, chi_tab, kind='cubic')
z_of_chi = interp1d(chi_tab, z_tab, kind='cubic')

chi_star = chi_of_z(z_star)
print(f"Comoving distance to last scattering: chi* = {chi_star:.1f} Mpc")
print(f"  (= {chi_star * h:.1f} Mpc/h)")

# ============================================================
# Linear matter power spectrum P(k) via Eisenstein-Hu (1998) no-wiggle
# ============================================================
def transfer_EH98_nowiggle(k_hMpc):
    """
    Eisenstein & Hu (1998) no-wiggle transfer function T(k).
    k in h/Mpc. Returns T(k). Eq. 29 of astro-ph/9710252.
    """
    Omega_m_h2 = Omega_m * h**2
    Omega_b_h2 = Omega_b * h**2
    f_b = Omega_b / Omega_m
    theta_27 = 2.7255 / 2.7

    # Sound horizon
    z_eq = 2.5e4 * Omega_m_h2 * theta_27**(-4)
    k_eq = 7.46e-2 * Omega_m_h2 * theta_27**(-2)  # h/Mpc

    b1 = 0.313 * Omega_m_h2**(-0.419) * (1 + 0.607 * Omega_m_h2**0.674)
    b2 = 0.238 * Omega_m_h2**0.223
    z_drag = 1291 * Omega_m_h2**0.251 / (1 + 0.659 * Omega_m_h2**0.828) * (1 + b1 * Omega_b_h2**b2)

    R_drag = 31.5 * Omega_b_h2 * theta_27**(-4) * (1000 / z_drag)
    R_eq = 31.5 * Omega_b_h2 * theta_27**(-4) * (1000 / z_eq)
    s = (2 / (3 * k_eq)) * np.sqrt(6 / R_eq) * np.log(
        (np.sqrt(1 + R_drag) + np.sqrt(R_drag + R_eq)) / (1 + np.sqrt(R_eq))
    )

    # No-wiggle transfer function (Eq. 29)
    Gamma = Omega_m * h
    alpha_Gamma = 1 - 0.328 * np.log(431 * Omega_m_h2) * f_b + 0.38 * np.log(22.3 * Omega_m_h2) * f_b**2
    Gamma_eff_k = Gamma * (alpha_Gamma + (1 - alpha_Gamma) / (1 + (0.43 * k_hMpc * s)**4))

    q = k_hMpc * theta_27**2 / Gamma_eff_k
    L = np.log(2 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1 + 62.5 * q)
    T0 = L / (L + C * q**2)
    return T0


def P_linear_unnorm(k_hMpc):
    """Unnormalized linear P(k) in (Mpc/h)^3. k in h/Mpc."""
    T = transfer_EH98_nowiggle(k_hMpc)
    return k_hMpc**n_s * T**2


# Normalize to sigma_8 at z=0
def sigma_R_integrand(lnk, R):
    """Integrand for sigma(R) in log-k space."""
    k = np.exp(lnk)
    x = k * R
    if x < 1e-6:
        W = 1.0
    else:
        W = 3.0 * (np.sin(x) - x * np.cos(x)) / x**3
    return k**3 * P_linear_unnorm(k) * W**2 / (2 * np.pi**2)

R8 = 8.0  # 8 Mpc/h
sigma8_sq_unnorm, _ = quad(sigma_R_integrand, np.log(1e-4), np.log(1e2),
                           args=(R8,), limit=500)
A_s_norm = sigma_8**2 / sigma8_sq_unnorm

print(f"Power spectrum normalization: A = {A_s_norm:.6e}")
print(f"  sigma_8 check: {np.sqrt(A_s_norm * sigma8_sq_unnorm):.4f} (target: {sigma_8})")

def P_k_z0(k_hMpc):
    """Normalized linear P(k) at z=0 in (Mpc/h)^3."""
    return A_s_norm * P_linear_unnorm(k_hMpc)


# ============================================================
# Growth factor D(z) via ODE integration
# ============================================================
# The linear growth factor satisfies:
#   D'' + (2 - q) H D' - (3/2) Omega_m H^2 (1+z)^3 D = 0
# where q = -a*a''/a'^2. For numerical stability, solve the ODE.
#
# Using the integral form (Heath 1977):
#   D(a) = (5/2) Omega_m H(a) int_0^a da' / (a' H(a'))^3
# normalized so D(a=1) = 1.

def growth_factor_exact(z):
    """
    Linear growth factor D(z) normalized to D(0)=1.
    Uses the Heath (1977) integral.
    """
    a = 1.0 / (1.0 + z)
    def integrand(a_prime):
        z_prime = 1.0 / a_prime - 1.0
        return 1.0 / (a_prime * E(z_prime))**3

    integral_a, _ = quad(integrand, 1e-8, a, limit=200)
    integral_1, _ = quad(integrand, 1e-8, 1.0, limit=200)

    D_a = E(z) * integral_a
    D_1 = E(0) * integral_1

    return D_a / D_1


# Test growth factor
print(f"\nGrowth factor D(z) [Heath integral, D(0)=1]:")
test_zs = [0, 0.5, 1, 2, 3, 5, 7, 10, 50, 100]
for zt in test_zs:
    Dz = growth_factor_exact(zt)
    print(f"  D({zt:>5}) = {Dz:.6f}   [a={1/(1+zt):.4f}]")

# Tabulate for fast interpolation
z_growth_tab = np.logspace(-3, 3.5, 2000)
z_growth_tab = np.insert(z_growth_tab, 0, 0.0)
D_growth_tab = np.array([growth_factor_exact(z) for z in z_growth_tab])
D_of_z = interp1d(z_growth_tab, D_growth_tab, kind='cubic', fill_value='extrapolate')

# ============================================================
# CMB Lensing Convergence Power Spectrum C_l^{kappa kappa}
# ============================================================
# Limber approximation:
#   C_l^{kk} = int_0^{chi*} dchi / chi^2 * [W_kappa(chi)]^2 * P(k=(l+0.5)/chi, z(chi))
#
# Lensing kernel:
#   W_kappa(chi) = (3/2) * Omega_m * (H_0/c)^2 * (1+z) * chi * (chi* - chi) / chi*
#
# P(k,z) = D(z)^2 * P(k, z=0)

H0_over_c = H0 / c_km_s  # Mpc^{-1}

def W_kappa(chi_val, z_val):
    """
    CMB lensing kernel. Returns Mpc^{-1}.
    W(chi) = (3/2) Omega_m (H0/c)^2 (1+z) chi (chi* - chi) / chi*
    """
    if chi_val <= 0 or chi_val >= chi_star:
        return 0.0
    return 1.5 * Omega_m * H0_over_c**2 * (1 + z_val) * chi_val * (chi_star - chi_val) / chi_star


def Cl_kk_at_ell(ell, chi_grid, z_grid, D_grid):
    """
    Compute C_l^{kk} for a single ell using pre-computed grids.
    Uses l -> l+0.5 (LoVerde & Afshordi 2008) for Limber accuracy.
    """
    integrand = np.zeros_like(chi_grid)
    for j in range(len(chi_grid)):
        chi_j = chi_grid[j]
        z_j = z_grid[j]

        if chi_j < 1.0 or chi_j > chi_star - 1.0:
            continue

        W = W_kappa(chi_j, z_j)

        k_Mpc_inv = (ell + 0.5) / chi_j  # Mpc^{-1}
        k_hMpc = k_Mpc_inv / h  # h/Mpc

        if k_hMpc < 1e-4 or k_hMpc > 100:
            continue

        # P(k,z) in Mpc^3 = D(z)^2 * P(k,0) [in (Mpc/h)^3] / h^3
        Pk_Mpc3 = D_grid[j]**2 * P_k_z0(k_hMpc) / h**3

        integrand[j] = W**2 / chi_j**2 * Pk_Mpc3

    return simpson(integrand, x=chi_grid)


# Set up integration grid
n_chi = 2000
chi_grid = np.linspace(5, chi_star - 5, n_chi)
z_grid = np.array([float(z_of_chi(c)) for c in chi_grid])
D_grid = np.array([float(D_of_z(z)) for z in z_grid])

# Multipoles
ell_values = np.unique(np.logspace(np.log10(30), np.log10(3000), 200).astype(int))
ell_values = ell_values[(ell_values >= 30) & (ell_values <= 3000)]

print(f"\nComputing C_l^{{kk}} for {len(ell_values)} multipoles...")
Cl_kk = np.zeros(len(ell_values))

for i, ell in enumerate(ell_values):
    Cl_kk[i] = Cl_kk_at_ell(ell, chi_grid, z_grid, D_grid)
    if (i + 1) % 50 == 0:
        print(f"  Completed {i+1}/{len(ell_values)} (l={ell})")

print("  Done.")

# Cross-check: at l=100, Planck published C_l^{phi phi} ~ 3e-7
# C_l^{kk} = [l(l+1)]^2 / 4 * C_l^{phi phi}
# So C_l^{kk}(100) ~ (100*101)^2/4 * 3e-7 ~ 7.7e-1 ... no, C_l^{phi phi} ~ 1e-7 at l=100
# Actually l(l+1)C_l^{kk}/(2pi) ~ 1e-7 at l=100 (standard normalization)
# So C_l^{kk}(100) ~ 2pi * 1e-7 / (100*101) ~ 6.2e-11
# Our result at l=100:
idx100 = np.argmin(np.abs(ell_values - 100))
print(f"\nCross-check: C_l^{{kk}}(l={ell_values[idx100]}) = {Cl_kk[idx100]:.4e}")
print(f"  l(l+1)C_l/(2pi) = {ell_values[idx100]*(ell_values[idx100]+1)*Cl_kk[idx100]/(2*np.pi):.4e}")
print(f"  Expected from Planck: l(l+1)C_l^kk/(2pi) ~ 1e-7 to 4e-8 at l=100")

# ============================================================
# Simons Observatory Lensing Noise Model
# ============================================================
# Based on SO Science Forecasts (Ade et al. 2019, JCAP 02:056)
# Table 1 and Figure 15.
#
# SO LAT baseline: f_sky = 0.4, 6 frequency bands
# MV lensing reconstruction noise N_L^{kk} from iterative delensing.
#
# Approximate published noise curve with analytic fit.
# SO minimum-variance N_L^{kk} ~ few x 10^{-8} at l ~ 200-1000
#
# Key reference values from SO forecasts (Ade+2019 Fig 15, Table 7):
#   N_L^{kk}(L=40) ~ 3e-7
#   N_L^{kk}(L=100) ~ 5e-8
#   N_L^{kk}(L=500) ~ 1e-8
#   N_L^{kk}(L=1000) ~ 3e-8
#   N_L^{kk}(L=2000) ~ 3e-7
#   N_L^{kk}(L=3000) ~ 5e-6
#
# These correspond to quadratic-estimator MV (TT+TE+EE+EB)

# Fit: parabola in log space with asymptotic rise
def N_l_SO(ell):
    """
    Approximate SO MV lensing noise N_L^{kk}.
    Fit to SO Science Book (Ade et al. 2019) Figure 15.
    Uses analytic form capturing U-shape in log-log.
    """
    # Parameterize as sum of power laws (low-l cosmic variance + high-l beam/noise)
    # plus a floor
    l0 = 400.0  # minimum noise multipole
    N_min = 8e-9  # noise floor near minimum

    # Low-l rise (geometric limit, fewer modes)
    low_l = (l0 / np.maximum(ell, 10.0))**3.0

    # High-l rise (beam + detector noise dominated)
    high_l = (np.maximum(ell, 10.0) / l0)**3.5

    return N_min * (1.0 + low_l + high_l)


# Verify against reference values
print(f"\nSO noise model verification:")
for l_check, N_ref in [(40, 3e-7), (100, 5e-8), (500, 1e-8), (1000, 3e-8), (2000, 3e-7)]:
    print(f"  N({l_check:>4d}) = {N_l_SO(l_check):.2e}  (ref ~ {N_ref:.0e})")

# ============================================================
# Signal-to-noise in bandpowers
# ============================================================
f_sky = 0.4  # SO LAT wide survey

# Interpolate C_l
Cl_interp = interp1d(ell_values, Cl_kk, kind='cubic', fill_value='extrapolate')

# Bandpowers: Delta_l = 50
delta_l = 50
l_band_edges = np.arange(100, 2050 + delta_l, delta_l)
l_band_centers = l_band_edges[:-1] + delta_l // 2
n_bands = len(l_band_centers)

Cl_bands = np.zeros(n_bands)
Nl_bands = np.zeros(n_bands)
sigma_Cl = np.zeros(n_bands)
snr_per_band = np.zeros(n_bands)

print(f"\nBandpower analysis (Delta_l = {delta_l}, f_sky = {f_sky}):")
print(f"{'l_center':>8} {'C_l^kk':>12} {'N_l^kk':>12} {'sigma(C_l)':>12} {'S/N':>8}")
print("-" * 56)

for i in range(n_bands):
    l_c = l_band_centers[i]
    Cl_bands[i] = float(Cl_interp(l_c))
    Nl_bands[i] = N_l_SO(l_c)

    # Number of independent modes in bandpower
    n_modes = (2 * l_c + 1) * f_sky * delta_l

    # Gaussian variance: Var(C_l) = 2 * (C_l + N_l)^2 / n_modes
    C_tot = np.abs(Cl_bands[i]) + Nl_bands[i]
    sigma_Cl[i] = np.sqrt(2.0 / n_modes) * C_tot

    snr_per_band[i] = np.abs(Cl_bands[i]) / sigma_Cl[i] if sigma_Cl[i] > 0 else 0

    if i % 4 == 0:
        print(f"{l_c:8.0f} {Cl_bands[i]:12.4e} {Nl_bands[i]:12.4e} {sigma_Cl[i]:12.4e} {snr_per_band[i]:8.1f}")

total_snr = np.sqrt(np.sum(snr_per_band**2))
print(f"\nTotal lensing detection S/N (l=100-2000): {total_snr:.1f} sigma")
print(f"  (Planck achieved ~40 sigma; SO baseline forecast ~70-100 sigma)")

# ============================================================
# Modified cosmology discrimination (Mehta 2025)
# ============================================================
# Paper 30 states:
#   - Modified cosmology enhances C_l^{kk} by ~30%
#   - SO discriminates at 10.4 sigma
#   - CMB-S4 at 29.8 sigma
#
# The 10.4 sigma is from their full Fisher analysis including:
#   - Scale-dependent enhancement (not flat 30%)
#   - Marginalization over astrophysical parameters
#   - Cross-correlations with galaxy surveys
#   - Foreground marginalization
#
# Our simplified estimate (flat 30% excess, no marginalization):

enhancement = 0.30
delta_Cl = enhancement * np.abs(Cl_bands)
chi2_naive = np.sum((delta_Cl / sigma_Cl)**2)
sigma_naive = np.sqrt(chi2_naive)

print(f"\n30% enhancement test (naive, no marginalization):")
print(f"  Naive significance: {sigma_naive:.1f} sigma")
print(f"  Paper 30 (full Fisher): 10.4 sigma")
print(f"  Ratio: {sigma_naive/10.4:.1f}x (expected >1 since we don't marginalize)")
print(f"  Degradation factor from marginalization: ~{sigma_naive/10.4:.0f}x")

# More realistic: only use z>2 contribution
# The key test is enhancement at high-z, not low-z where cosmic variance dominates
# From our kernel analysis below, the z>2 fraction will give us a realistic scaling

# ============================================================
# Lensing kernel decomposition by redshift
# ============================================================
print(f"\n{'='*70}")
print("Lensing kernel analysis at l = 500")
print(f"{'='*70}")

z_kernel = np.linspace(0.05, 8.0, 500)
chi_kernel = np.array([float(chi_of_z(z)) for z in z_kernel])
D_kernel = np.array([float(D_of_z(z)) for z in z_kernel])

ell_ref = 500
kernel_by_z = np.zeros_like(z_kernel)

for j in range(len(z_kernel)):
    chi_j = chi_kernel[j]
    z_j = z_kernel[j]
    if chi_j < 1 or chi_j > chi_star - 1:
        continue
    W = W_kappa(chi_j, z_j)
    k_hMpc = (ell_ref + 0.5) / chi_j / h
    if k_hMpc < 1e-4 or k_hMpc > 100:
        continue
    Pk = D_kernel[j]**2 * P_k_z0(k_hMpc) / h**3
    kernel_by_z[j] = W**2 / chi_j**2 * Pk * chi_integrand(z_j)

# Normalize
kernel_max = np.max(kernel_by_z)
if kernel_max > 0:
    kernel_norm = kernel_by_z / kernel_max
else:
    kernel_norm = kernel_by_z

# Statistics
z_peak = z_kernel[np.argmax(kernel_by_z)]
cumul = np.cumsum(kernel_by_z) * (z_kernel[1] - z_kernel[0])
if cumul[-1] > 0:
    cumul_norm = cumul / cumul[-1]
else:
    cumul_norm = cumul
z_median = z_kernel[np.argmin(np.abs(cumul_norm - 0.5))]
frac_z_gt_2 = 1.0 - cumul_norm[np.argmin(np.abs(z_kernel - 2.0))]

print(f"  Peak contribution at z = {z_peak:.2f}")
print(f"  Median contribution at z = {z_median:.2f}")
print(f"  Fraction from z > 2: {frac_z_gt_2:.1%}")
print(f"  Fraction from z > 4 (LRD range): {1.0 - cumul_norm[np.argmin(np.abs(z_kernel - 4.0))]:.1%}")

# ============================================================
# Pre-registration record
# ============================================================
print(f"\n{'='*70}")
print("PRE-REGISTRATION: SIMONS-43")
print(f"{'='*70}")

key_ells = [100, 200, 300, 500, 700, 1000, 1500, 2000]
print(f"\nFramework prediction: C_l^{{kk}} = Planck LCDM (EXACT)")
print(f"  Reason: w = -1 + O(10^{{-29}}), sigma/m ~ 10^{{-51}} cm^2/g")
print(f"  Matter power spectrum identical to LCDM at ALL observable k")
print(f"")
print(f"{'l':>6} {'l(l+1)C_l/2pi':>16} {'C_l^kk':>14} {'N_l^kk (SO)':>14} {'sigma(C_l)':>14}")
print("-" * 68)
for l_key in key_ells:
    cl = float(Cl_interp(l_key))
    nl = N_l_SO(l_key)
    idx = np.argmin(np.abs(l_band_centers - l_key))
    sig = sigma_Cl[idx]
    ll1 = l_key * (l_key + 1) * cl / (2 * np.pi)
    print(f"{l_key:6d} {ll1:16.6e} {cl:14.6e} {nl:14.6e} {sig:14.6e}")

print(f"\nFalsification criterion:")
print(f"  Observable: C_l^{{kk}} from SO MV lensing reconstruction")
print(f"  Multipole range: l = 100-2000")
print(f"  Bandpower width: Delta_l = {delta_l}")
print(f"  Sky fraction: f_sky = {f_sky}")
print(f"")
print(f"  Test statistic: chi^2 = sum_bands [(C_l^obs - C_l^LCDM) / sigma_l]^2")
print(f"  Falsification: sqrt(chi^2) > 3.0  =>  framework EXCLUDED")
print(f"  Survival:      sqrt(chi^2) < 3.0  =>  framework survives")
print(f"")
print(f"  Modified cosmology (Paper 30, +30% P(k)):")
print(f"    Naive significance: {sigma_naive:.0f} sigma (no marginalization)")
print(f"    Full Fisher (Mehta 2025): 10.4 sigma (with marginalization)")
print(f"    SO detection guaranteed if modified cosmology is real")
print(f"")
print(f"  Timeline: SO first light 2024, design sensitivity ~2027-2028")
print(f"  Expected resolution by ~2028")

# ============================================================
# Save data
# ============================================================
np.savez(
    "tier0-computation/s43_simons_prereg.npz",
    ell_values=ell_values,
    Cl_kk=Cl_kk,
    l_band_centers=l_band_centers,
    Cl_bands=Cl_bands,
    Nl_bands=Nl_bands,
    sigma_Cl=sigma_Cl,
    snr_per_band=snr_per_band,
    total_snr=total_snr,
    sigma_naive_30pct=sigma_naive,
    z_kernel=z_kernel,
    kernel_by_z=kernel_norm,
    z_peak=z_peak,
    z_median=z_median,
    frac_z_gt_2=frac_z_gt_2,
    Omega_m=Omega_m, Omega_b=Omega_b, h=h,
    sigma_8=sigma_8, n_s=n_s, f_sky=f_sky, chi_star=chi_star,
)
print(f"\nSaved: tier0-computation/s43_simons_prereg.npz")

# ============================================================
# Plot
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle("SIMONS-43: CMB Lensing Pre-Registration\n"
             r"Framework prediction = Planck $\Lambda$CDM (exact degeneracy)",
             fontsize=14, fontweight='bold')

# Panel (a): C_l^{kk} spectrum
ax1 = axes[0, 0]
mask_plot = (ell_values >= 30) & (ell_values <= 3000)
l_p = ell_values[mask_plot]
cl_p = Cl_kk[mask_plot]

ax1.loglog(l_p, l_p * (l_p + 1) * cl_p / (2 * np.pi), 'b-', lw=2,
           label=r'$\Lambda$CDM = Framework')

# SO bandpower errors
mask_bp = (l_band_centers >= 100) & (l_band_centers <= 2000)
l_bp = l_band_centers[mask_bp]
cl_bp = Cl_bands[mask_bp]
sig_bp = sigma_Cl[mask_bp]
y_bp = l_bp * (l_bp + 1) * cl_bp / (2 * np.pi)
y_err = l_bp * (l_bp + 1) * sig_bp / (2 * np.pi)
ax1.errorbar(l_bp, y_bp, yerr=y_err, fmt='none', ecolor='gray', alpha=0.5,
             label=r'SO $1\sigma$ errors')

# Modified cosmology
ax1.loglog(l_p, l_p * (l_p + 1) * cl_p * 1.3 / (2 * np.pi), 'r--', lw=1.5,
           label='Modified cosmology (+30%)')

# SO noise
l_noise = np.logspace(np.log10(30), np.log10(3000), 200)
N_noise = np.array([N_l_SO(l) for l in l_noise])
ax1.loglog(l_noise, l_noise * (l_noise + 1) * N_noise / (2 * np.pi),
           'k:', lw=1, alpha=0.5, label=r'SO $N_L^{\kappa\kappa}$')

ax1.set_xlabel(r'Multipole $\ell$', fontsize=12)
ax1.set_ylabel(r'$\ell(\ell+1) C_\ell^{\kappa\kappa} / 2\pi$', fontsize=12)
ax1.set_xlim(30, 3000)
ax1.legend(fontsize=9, loc='lower left')
ax1.set_title(r'(a) Convergence power spectrum')
ax1.grid(True, alpha=0.3)

# Panel (b): S/N per band
ax2 = axes[0, 1]
ax2.bar(l_bp, snr_per_band[mask_bp], width=delta_l * 0.8, color='steelblue', alpha=0.8)
ax2.axhline(3, color='red', ls='--', lw=1, label=r'$3\sigma$')
ax2.set_xlabel(r'Multipole $\ell$', fontsize=12)
ax2.set_ylabel('S/N per bandpower', fontsize=12)
ax2.set_title(f'(b) Detection S/N (total = {total_snr:.0f}$\\sigma$)')
ax2.legend(fontsize=10)
ax2.set_xlim(50, 2100)
ax2.grid(True, alpha=0.3)

# Panel (c): Lensing kernel
ax3 = axes[1, 0]
ax3.fill_between(z_kernel, 0, kernel_norm, alpha=0.3, color='blue')
ax3.plot(z_kernel, kernel_norm, 'b-', lw=2)
ax3.axvline(z_peak, color='red', ls='--', lw=1, label=f'Peak z = {z_peak:.1f}')
ax3.axvline(z_median, color='orange', ls='--', lw=1, label=f'Median z = {z_median:.1f}')
ax3.axvline(2.0, color='green', ls=':', lw=1.5,
            label=f'z=2 ({frac_z_gt_2:.0%} above)')
ax3.axvspan(4, 8, alpha=0.1, color='red', label='LRD range (z=4-8)')
ax3.set_xlabel('Redshift z', fontsize=12)
ax3.set_ylabel(r'Lensing weight $dC_\ell/dz$ (norm.)', fontsize=12)
ax3.set_title(r'(c) Lensing kernel at $\ell = 500$')
ax3.legend(fontsize=9)
ax3.set_xlim(0, 8)
ax3.grid(True, alpha=0.3)

# Panel (d): Summary
ax4 = axes[1, 1]
ax4.axis('off')
text = (
    "PRE-REGISTRATION: SIMONS-43\n"
    "------------------------------------\n\n"
    "Framework prediction:\n"
    "  C_l^{kk} = Planck LCDM (exact)\n"
    "  w = -1 + O(10^{-29})\n"
    "  sigma/m ~ 10^{-51} cm^2/g (CDM)\n\n"
    "Falsification criterion:\n"
    "  sqrt(chi^2) > 3.0 across l=100-2000\n"
    "  chi^2 = sum [(C_l^obs - C_l^LCDM)/sigma]^2\n\n"
    f"Discriminating power:\n"
    f"  Mod. cosmology (+30%): 10.4 sigma\n"
    f"  (Mehta 2025, full Fisher)\n\n"
    f"Lensing kernel at l=500:\n"
    f"  Peak z = {z_peak:.1f}, median z = {z_median:.1f}\n"
    f"  {frac_z_gt_2:.0%} from z > 2\n\n"
    f"Timeline: SO ~2027-2028\n\n"
    f"Gate: INFO (pre-registration)\n"
    f"Verdict awaits SO data"
)
ax4.text(0.05, 0.95, text, transform=ax4.transAxes, fontsize=10,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
ax4.set_title('(d) Pre-registration summary')

plt.tight_layout()
plt.savefig("tier0-computation/s43_simons_prereg.png", dpi=150, bbox_inches='tight')
print(f"Saved: tier0-computation/s43_simons_prereg.png")

# ============================================================
# Final summary
# ============================================================
print(f"\n{'='*70}")
print("SIMONS-43 COMPLETE")
print(f"{'='*70}")
print(f"Gate: SIMONS-43 (INFO -- pre-registration)")
print(f"Framework prediction: C_l^{{kk}} = Planck LCDM (exact)")
print(f"Total lensing S/N (SO, l=100-2000): {total_snr:.0f} sigma")
print(f"Mehta 2025 discrimination (mod. cosmo vs astro): 10.4 sigma")
print(f"Falsification: >3 sigma excess in C_l^{{kk}} => framework excluded")
print(f"Lensing kernel peak: z = {z_peak:.1f}, median z = {z_median:.1f}")
print(f"High-z fraction (z>2): {frac_z_gt_2:.1%}")
print(f"Timeline: ~2028 (SO design sensitivity)")
print(f"Files: s43_simons_prereg.{{py,npz,png}}")
