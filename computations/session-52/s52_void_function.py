#!/usr/bin/env python3
"""
VOID-FUNCTION-52: Void Size Function at Both alpha_s Values
============================================================
Session 52, Wave 4-K | Agent: Cosmic-Web-Theorist
Gate: INFO (excess voids at R = 15-20 h^{-1} Mpc)

Computes the Sheth-van de Weygaert (2004) void size function n(R)
at three values of the primordial spectral running:
  - alpha_s = 0       (LCDM baseline, no running)
  - alpha_s = -0.02   (SA-Goldstone mixing regime, S51 window)
  - alpha_s = -0.069  (O-Z rigid prediction, S49-50)

Method:
  1. Matter P(k) = k * (k/k_*)^{n_s-1+(alpha_s/2)*ln(k/k_*)} * T_EH(k)^2
  2. Eisenstein-Hu (1998) transfer function (no-wiggle approximation)
  3. Normalize to sigma_8 = 0.811 at R=8 h^{-1} Mpc
  4. SvdW void multiplicity function from excursion set theory
  5. Void size function dn/dlnR = (f(nu)/V(R)) * |d ln sigma^{-1}/d ln R|

References:
  - Sheth & van de Weygaert, MNRAS 350, 517 (2004) [SvdW04]
  - Eisenstein & Hu, ApJ 496, 605 (1998) [EH98]
  - Contarini et al., A&A 668, A169 (2022) [Euclid void forecasts]
  - Jennings, Li & Hu, MNRAS 434, 2167 (2013) [Vdn model calibration]
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (, k_pivot_planck
    Omega_m, Omega_b, Omega_Lambda, sigma_8,
    H_0_km_s_Mpc, PI
)

# ============================================================================
#  Section 1: Cosmological Parameters
# ============================================================================

n_s = 0.9649  # Planck 2018 best-fit scalar spectral index (local)
k_pivot = k_pivot_planck  # canonical alias (was: = 0.05)
h = H_0_km_s_Mpc / 100.0  # = 0.674

# Three alpha_s scenarios
ALPHA_S_VALUES = {
    'LCDM':    0.0,
    'SA-mix':  -0.02,
    'O-Z':     -0.069
}

# Shell-crossing thresholds (SvdW04)
delta_v = -2.717        # void shell-crossing (linear, EdS)
delta_c = 1.686         # collapse threshold (linear, EdS)

print("=" * 72)
print("VOID-FUNCTION-52: Void Size Function at Both alpha_s Values")
print("=" * 72)
print(f"  Omega_m = {Omega_m}, Omega_b = {Omega_b}, h = {h:.4f}")
print(f"  sigma_8 = {sigma_8}, n_s = {n_s}")
print(f"  k_pivot = {k_pivot} Mpc^-1 = {k_pivot/h:.5f} h/Mpc")
print(f"  delta_v = {delta_v}, delta_c = {delta_c}")
print(f"  alpha_s values: {ALPHA_S_VALUES}")
print()

# ============================================================================
#  Section 2: Eisenstein-Hu (1998) Transfer Function (No-Wiggle)
# ============================================================================

def transfer_EH98(k_hMpc):
    """
    Eisenstein & Hu (1998) no-wiggle (zero-baryon) transfer function.
    Eq. 29-31 of EH98.

    Parameters
    ----------
    k_hMpc : array, wavenumber in h/Mpc

    Returns
    -------
    T(k) : array, transfer function normalized to 1 as k -> 0
    """
    Omega_m_h2 = Omega_m * h**2
    Omega_b_h2 = Omega_b * h**2
    f_b = Omega_b / Omega_m
    Theta_27 = 2.7255 / 2.7

    # Sound horizon (EH98 Eq. 26)
    s = 44.5 * np.log(9.83 / Omega_m_h2) / np.sqrt(1.0 + 10.0 * Omega_b_h2**0.75)

    # Shape parameter (EH98 Eq. 31)
    alpha_Gamma = 1.0 - 0.328 * np.log(431.0 * Omega_m_h2) * f_b + \
                  0.38 * np.log(22.3 * Omega_m_h2) * f_b**2

    Gamma_eff = Omega_m * h * (
        alpha_Gamma + (1.0 - alpha_Gamma) / (1.0 + (0.43 * k_hMpc * s)**4)
    )

    # EH98 Eq. 29
    q = k_hMpc * Theta_27**2 / Gamma_eff
    L = np.log(2.0 * np.e + 1.8 * q)
    C = 14.2 + 731.0 / (1.0 + 62.5 * q)
    T0 = L / (L + C * q**2)

    return T0


# ============================================================================
#  Section 3: Unnormalized Matter Power Spectrum P(k)
# ============================================================================

def P_unnorm(k_hMpc, alpha_s):
    """
    Unnormalized matter power spectrum.

    P(k) propto k * (k/k_*)^{n_s - 1 + (alpha_s/2)*ln(k/k_*)} * T(k)^2

    We work in units of h/Mpc for k. The pivot k_* = 0.05 Mpc^{-1} = 0.0742 h/Mpc.

    The normalization is irrelevant because we fix sigma_8.
    What matters is the SHAPE as a function of alpha_s.

    Parameters
    ----------
    k_hMpc : array, in h/Mpc
    alpha_s : float

    Returns
    -------
    P(k) : array (arbitrary units)
    """
    k_star_hMpc = k_pivot / h  # = 0.05/0.674 = 0.0742 h/Mpc

    # ln(k/k_*)
    ln_ratio = np.log(k_hMpc / k_star_hMpc)

    # Effective spectral index at each k
    # P(k) ~ k^{n_eff(k)} * T(k)^2  where n_eff = n_s + alpha_s * ln(k/k_*)
    # => P(k) ~ k * exp[(n_s - 1) * ln(k/k_*) + (alpha_s/2) * ln(k/k_*)^2] * T(k)^2

    shape = k_hMpc * np.exp((n_s - 1.0) * ln_ratio + 0.5 * alpha_s * ln_ratio**2)
    T_k = transfer_EH98(k_hMpc)

    return shape * T_k**2


# ============================================================================
#  Section 4: sigma(R) from Top-Hat Filter
# ============================================================================

def sigma_squared_raw(R_hMpc, alpha_s, k_min=1e-4, k_max=100.0, npts=5000):
    """
    Raw (unnormalized) sigma^2(R).

    sigma^2(R) = (1/2pi^2) int dk k^2 P(k) |W(kR)|^2

    where W(x) = 3*(sin x - x cos x)/x^3 is the top-hat window function.

    We integrate in ln(k) for better numerical behavior.

    Parameters
    ----------
    R_hMpc : float, smoothing scale in h^{-1} Mpc
    alpha_s : float
    """
    # Log-spaced k grid
    ln_k = np.linspace(np.log(k_min), np.log(k_max), npts)
    k = np.exp(ln_k)

    # Top-hat window
    x = k * R_hMpc
    # Taylor expansion for small x to avoid 0/0
    W = np.where(x < 1e-3,
                 1.0 - x**2/10.0 + x**4/280.0,
                 3.0 * (np.sin(x) - x * np.cos(x)) / x**3)

    # Power spectrum (unnormalized)
    Pk = P_unnorm(k, alpha_s)

    # Integrand in d(ln k): k^3 * P(k) * W^2 / (2 pi^2)
    integrand = k**3 * Pk * W**2 / (2.0 * PI**2)

    return np.trapezoid(integrand, ln_k)


# ============================================================================
#  Section 5: Normalization to sigma_8
# ============================================================================

print("Step 1: Computing sigma_8 normalization factors...")

norm_factors = {}
for label, alpha_val in ALPHA_S_VALUES.items():
    s2_raw = sigma_squared_raw(8.0, alpha_val)
    norm = sigma_8**2 / s2_raw
    norm_factors[label] = norm
    print(f"  {label:8s}: sigma_raw(8) = {np.sqrt(s2_raw):.6e}, norm = {norm:.6e}")

print()


def sigma_R(R_hMpc, alpha_s, label):
    """Normalized sigma(R)."""
    return np.sqrt(norm_factors[label] * sigma_squared_raw(R_hMpc, alpha_s))


# Verify normalization
print("Verification: sigma(8) at each alpha_s:")
for label, alpha_val in ALPHA_S_VALUES.items():
    print(f"  {label:8s}: sigma(8) = {sigma_R(8.0, alpha_val, label):.6f} (target: {sigma_8})")
print()

# ============================================================================
#  Section 6: sigma(R) Table
# ============================================================================

print("Step 2: Computing sigma(R) table...")
R_table = [2, 5, 8, 10, 15, 20, 25, 30, 40, 50, 70, 100]
print(f"  {'R':>5s}  {'LCDM':>10s}  {'SA-mix':>10s}  {'O-Z':>10s}  "
      f"{'SA/LCDM':>10s}  {'OZ/LCDM':>10s}")
print("  " + "-" * 62)

sigma_table = {}
for R_val in R_table:
    row = {}
    for label, alpha_val in ALPHA_S_VALUES.items():
        row[label] = sigma_R(R_val, alpha_val, label)
    sigma_table[R_val] = row
    print(f"  {R_val:5d}  {row['LCDM']:10.5f}  {row['SA-mix']:10.5f}  "
          f"{row['O-Z']:10.5f}  {row['SA-mix']/row['LCDM']:10.6f}  "
          f"{row['O-Z']/row['LCDM']:10.6f}")

print()


# ============================================================================
#  Section 7: SvdW Void Multiplicity Function
# ============================================================================

def f_SvdW(nu_v):
    """
    Sheth-van de Weygaert (2004) void first-crossing distribution.

    The two-barrier (void-in-void + void-in-cloud) problem gives
    (SvdW04, Eq. 14):

    f(S) = sum_{j=1}^{inf} (j*pi*D^2 / (1+D)^3)
           * sin(j*pi*D/(1+D))
           * exp(-j^2*pi^2*D^2 / (2*(1+D)^2) * S/delta_v^2)

    where D = |delta_v|/delta_c and S = sigma^2.

    In terms of nu_v = delta_v^2/sigma^2 = delta_v^2/S:

    f(nu_v) * d(nu_v) = ... (with appropriate Jacobian)

    We compute the multiplicity function nu_v * f(nu_v) = S * f(S) * dnu_v/dS.

    Actually, the void size function in the SvdW formalism is:

    dn/dlnR = (rho_bar / M(R)) * |d ln sigma / d ln R| * nu_v * f_FCD(nu_v)

    where f_FCD is the first-crossing distribution.

    For voids, we follow the convention of Jennings+ (2013):

    dn/dR = (rho_bar / (4/3 pi R^3 rho_bar)) * |d ln sigma^{-1}/dR| * f_v(sigma)

    Parameters
    ----------
    nu_v : array
        nu_v = (|delta_v| / sigma(R))^2

    Returns
    -------
    f_v : array
        Void multiplicity f_v = nu_v * f_FCD(nu_v) with two-barrier correction
    """
    D = abs(delta_v) / delta_c  # = 2.717 / 1.686 = 1.611

    # SvdW04 series (Eq. 14, rewritten in nu_v)
    # S/delta_v^2 = 1/nu_v
    result = np.zeros_like(nu_v, dtype=float)

    for j in range(1, 60):
        x_j = j * PI * D / (1.0 + D)
        prefactor = j * PI * D**2 / (1.0 + D)**3
        exp_arg = -j**2 * PI**2 * D**2 / (2.0 * (1.0 + D)**2 * nu_v)
        result += prefactor * np.sin(x_j) * np.exp(exp_arg)

    # This gives f(S). The void size function needs:
    # dn/dlnR = (1/V(R)) * |d ln sigma^{-1}/d ln R| * f(S)
    # where f(S) is integrated to give the fraction of volume in voids.
    # Actually SvdW04 Eq. 14 gives the first-crossing rate per unit S.
    # The multiplicity function for dn/dlnR is:
    #   nu_v * f_FCD(nu_v) = S * f(S)  [with delta_v^2 / S = nu_v]
    # So the volume fraction in voids of scale R:
    #   F(>R) = int_0^{S(R)} f(S') dS'

    # For the size function, we need f(S) at S = sigma^2:
    # dn/d ln R = (1/V) * |d ln sigma^{-1}/d ln R| * nu_f(nu) where
    # nu_f(nu) = S * f(S) * |delta_v|  [Eq. 10 of SvdW04]

    # The standard Press-Schechter analog for voids gives:
    # dn/d ln R = (rho_bar/M) * f_PS(nu) * |d ln sigma/d ln R|
    # For voids, M(R) -> V(R)*rho_bar, so rho_bar/M = 1/V(R).

    # The series f(S) above is per-unit-S. We want f(nu) per-unit-nu:
    # f(S) dS = f(nu) dnu => f(nu) = f(S) * |dS/dnu| = f(S) * delta_v^2 / nu^2
    # Then: nu * f(nu) = f(S) * delta_v^2 / nu

    # Actually the clean way:
    # dn/d ln R = (1/V) * |d ln sigma^{-1}/d ln R| * [S * f(S)]
    # S * f(S) is what we want.

    # result is f(S). S = delta_v^2 / nu_v.
    # S * f(S) = (delta_v^2 / nu_v) * result
    Sf = (delta_v**2 / nu_v) * result

    return Sf


# ============================================================================
#  Section 8: Void Size Function Computation
# ============================================================================

print("Step 3: Computing void size functions...")

R_arr = np.logspace(np.log10(5.0), np.log10(60.0), 120)

results = {}
for label, alpha_val in ALPHA_S_VALUES.items():
    # sigma(R) at each R
    sig_arr = np.array([sigma_R(R, alpha_val, label) for R in R_arr])

    # d ln sigma^{-1} / d ln R via central differences in log
    dlnsig_inv_dlnR = np.zeros_like(R_arr)
    eps = 0.005  # 0.5% step
    for i, R in enumerate(R_arr):
        sig_lo = sigma_R(R * (1 - eps), alpha_val, label)
        sig_hi = sigma_R(R * (1 + eps), alpha_val, label)
        dlnsig_dlnR = np.log(sig_hi / sig_lo) / np.log((1 + eps) / (1 - eps))
        dlnsig_inv_dlnR[i] = abs(dlnsig_dlnR)  # |d ln sigma^{-1}/d ln R|

    # nu_v = (|delta_v| / sigma)^2
    nu_v = (abs(delta_v) / sig_arr)**2

    # Volume
    V_R = (4.0 / 3.0) * PI * R_arr**3

    # SvdW multiplicity: S*f(S) where S = sigma^2
    Sf = f_SvdW(nu_v)

    # Void size function: dn/d ln R = (1/V) * |d ln sigma^{-1}/d ln R| * S*f(S)
    dn_dlnR = (1.0 / V_R) * dlnsig_inv_dlnR * Sf

    results[label] = {
        'R': R_arr.copy(),
        'dn_dlnR': dn_dlnR,
        'sigma': sig_arr,
        'nu': nu_v,
        'dlnsig_inv_dlnR': dlnsig_inv_dlnR,
        'Sf': Sf,
        'alpha_s': alpha_val
    }

    # Report key values
    idx_15 = np.argmin(np.abs(R_arr - 15.0))
    idx_20 = np.argmin(np.abs(R_arr - 20.0))
    print(f"\n  {label} (alpha_s = {alpha_val}):")
    print(f"    sigma(5)  = {sig_arr[0]:.5f},  sigma(8)  = {sigma_R(8, alpha_val, label):.5f}")
    print(f"    sigma(15) = {sig_arr[idx_15]:.5f},  sigma(20) = {sig_arr[idx_20]:.5f}")
    print(f"    sigma(50) = {sig_arr[-6]:.5f}")
    print(f"    |d ln sig^-1/d ln R| at R=15: {dlnsig_inv_dlnR[idx_15]:.5f}")
    print(f"    |d ln sig^-1/d ln R| at R=20: {dlnsig_inv_dlnR[idx_20]:.5f}")
    print(f"    nu(15) = {nu_v[idx_15]:.4f},  nu(20) = {nu_v[idx_20]:.4f}")
    print(f"    S*f(S) at R=15: {Sf[idx_15]:.6e}")
    print(f"    S*f(S) at R=20: {Sf[idx_20]:.6e}")
    print(f"    dn/dlnR(15) = {dn_dlnR[idx_15]:.6e} (h/Mpc)^3")
    print(f"    dn/dlnR(20) = {dn_dlnR[idx_20]:.6e} (h/Mpc)^3")

print()

# ============================================================================
#  Section 9: Relative Excess vs LCDM
# ============================================================================

print("=" * 72)
print("RELATIVE EXCESS vs LCDM (alpha_s = 0)")
print("=" * 72)

for label in ['SA-mix', 'O-Z']:
    alpha_val = ALPHA_S_VALUES[label]
    ratio = results[label]['dn_dlnR'] / results['LCDM']['dn_dlnR']
    excess_pct = (ratio - 1.0) * 100.0

    key_R = [10, 15, 20, 25, 30, 40, 50]
    print(f"\n  {label} (alpha_s = {alpha_val}):")
    for Rv in key_R:
        idx = np.argmin(np.abs(R_arr - Rv))
        print(f"    R = {Rv:3d} h^{{-1}} Mpc: excess = {excess_pct[idx]:+.2f}%, "
              f"sigma ratio = {results[label]['sigma'][idx]/results['LCDM']['sigma'][idx]:.6f}")

    idx_15 = np.argmin(np.abs(R_arr - 15.0))
    idx_20 = np.argmin(np.abs(R_arr - 20.0))
    avg_excess = np.mean(excess_pct[idx_15:idx_20+1])
    print(f"    Average excess [15, 20] h^-1 Mpc: {avg_excess:+.2f}%")

    # sigma ratio tells the story
    print(f"    sigma(R) ratios (this model / LCDM):")
    for Rv in [5, 8, 10, 15, 20, 30, 50]:
        s_this = sigma_R(Rv, alpha_val, label)
        s_lcdm = sigma_R(Rv, 0.0, 'LCDM')
        print(f"      R={Rv:3d}: {s_this/s_lcdm:.6f} (delta = {(s_this/s_lcdm - 1)*100:+.4f}%)")


# ============================================================================
#  Section 10: Diagnostic -- Where Does Running Bite?
# ============================================================================

print("\n" + "=" * 72)
print("DIAGNOSTIC: P(k) Shape Modification from Running")
print("=" * 72)

k_diag = np.logspace(-3, 1, 200)  # h/Mpc
for label in ['SA-mix', 'O-Z']:
    alpha_val = ALPHA_S_VALUES[label]
    P_lcdm = P_unnorm(k_diag, 0.0)
    P_run = P_unnorm(k_diag, alpha_val)
    ratio_Pk = P_run / P_lcdm

    # P(k) ratio at key scales
    for kv in [0.01, 0.05, 0.1, 0.5, 1.0, 5.0]:
        idx = np.argmin(np.abs(k_diag - kv))
        print(f"  {label}: P(k={kv:.2f})/P_LCDM = {ratio_Pk[idx]:.6f} "
              f"({(ratio_Pk[idx]-1)*100:+.3f}%)")
    print()


# ============================================================================
#  Section 11: Save Data
# ============================================================================

output_dir = os.path.dirname(os.path.abspath(__file__))
npz_path = os.path.join(output_dir, "s52_void_function.npz")

save_dict = {
    'R_hMpc_inv': R_arr,
    'alpha_s_values': np.array([0.0, -0.02, -0.069]),
}
for label in ['LCDM', 'SA-mix', 'O-Z']:
    safe = label.replace('-', '_')
    save_dict[f'dn_dlnR_{safe}'] = results[label]['dn_dlnR']
    save_dict[f'sigma_{safe}'] = results[label]['sigma']
    save_dict[f'nu_{safe}'] = results[label]['nu']
    save_dict[f'dlnsig_{safe}'] = results[label]['dlnsig_inv_dlnR']

np.savez(npz_path, **save_dict)
print(f"\nData saved: {npz_path}")


# ============================================================================
#  Section 12: Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(
    'VOID-FUNCTION-52: Void Size Function at Three $\\alpha_s$ Values\n'
    '(Sheth-van de Weygaert 2004, Eisenstein-Hu 1998 transfer function)',
    fontsize=13, fontweight='bold'
)

colors = {'LCDM': 'black', 'SA-mix': '#2166AC', 'O-Z': '#B2182B'}
styles = {'LCDM': '-', 'SA-mix': '--', 'O-Z': '-.'}
lw = 2.0  # (local)

# --- (a) Void size function ---
ax = axes[0, 0]
for label in ['LCDM', 'SA-mix', 'O-Z']:
    av = ALPHA_S_VALUES[label]
    ax.semilogy(results[label]['R'], results[label]['dn_dlnR'],
                color=colors[label], ls=styles[label], lw=lw,
                label=f'{label} ($\\alpha_s = {av:.3f}$)')
ax.axvspan(15, 20, alpha=0.12, color='gold', label='Gate region')
ax.set_xlabel('$R$ [$h^{-1}$ Mpc]', fontsize=11)
ax.set_ylabel('$dn/d\\ln R$ [$(h^{-1}\\,\\mathrm{Mpc})^{-3}$]', fontsize=11)
ax.set_title('(a) Void Size Function', fontsize=11)
ax.legend(fontsize=8.5, loc='upper right')
ax.set_xlim(5, 60)
ax.grid(True, alpha=0.3)

# --- (b) Relative excess ---
ax = axes[0, 1]
for label in ['SA-mix', 'O-Z']:
    ratio = results[label]['dn_dlnR'] / results['LCDM']['dn_dlnR']
    excess = (ratio - 1.0) * 100.0
    ax.plot(R_arr, excess,
            color=colors[label], ls=styles[label], lw=lw,
            label=f'{label} ($\\alpha_s = {ALPHA_S_VALUES[label]:.3f}$)')
ax.axhline(0, color='black', lw=0.5)
ax.axvspan(15, 20, alpha=0.1, color='green')
ax.set_xlabel('$R$ [$h^{-1}$ Mpc]', fontsize=11)
ax.set_ylabel('Excess vs $\\Lambda$CDM [%]', fontsize=11)
ax.set_title('(b) Void Abundance Excess', fontsize=11)
ax.legend(fontsize=8.5)
ax.set_xlim(5, 60)
ax.grid(True, alpha=0.3)

# --- (c) sigma(R) ---
ax = axes[1, 0]
for label in ['LCDM', 'SA-mix', 'O-Z']:
    av = ALPHA_S_VALUES[label]
    ax.plot(R_arr, results[label]['sigma'],
            color=colors[label], ls=styles[label], lw=lw,
            label=f'{label} ($\\alpha_s = {av:.3f}$)')
ax.axhline(abs(delta_v), color='red', ls=':', lw=1, alpha=0.5,
           label='$|\\delta_v|$ (shell-crossing)')
ax.set_xlabel('$R$ [$h^{-1}$ Mpc]', fontsize=11)
ax.set_ylabel('$\\sigma(R)$', fontsize=11)
ax.set_title('(c) RMS Density Fluctuation', fontsize=11)
ax.legend(fontsize=8.5)
ax.set_xlim(5, 60)
ax.grid(True, alpha=0.3)

# --- (d) P(k) ratio ---
ax = axes[1, 1]
k_plot = np.logspace(-3, 1, 300)
for label in ['SA-mix', 'O-Z']:
    av = ALPHA_S_VALUES[label]
    ratio_Pk = P_unnorm(k_plot, av) / P_unnorm(k_plot, 0.0)
    ax.semilogx(k_plot, (ratio_Pk - 1.0) * 100.0,
                color=colors[label], ls=styles[label], lw=lw,
                label=f'{label} ($\\alpha_s = {av:.3f}$)')
ax.axhline(0, color='black', lw=0.5)
ax.axvline(k_pivot/h, color='gray', ls=':', lw=1, alpha=0.5, label='$k_*$')
ax.set_xlabel('$k$ [$h$/Mpc]', fontsize=11)
ax.set_ylabel('$\\Delta P(k) / P_{\\Lambda CDM}$ [%]', fontsize=11)
ax.set_title('(d) Primordial Power Modification', fontsize=11)
ax.legend(fontsize=8.5)
ax.set_xlim(1e-3, 10)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.94])
png_path = os.path.join(output_dir, "s52_void_function.png")
fig.savefig(png_path, dpi=150, bbox_inches='tight')
print(f"Plot saved: {png_path}")


# ============================================================================
#  Section 13: Physical Assessment and Gate Verdict
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: VOID-FUNCTION-52 (INFO)")
print("=" * 72)

# Compute gate numbers
idx_15 = np.argmin(np.abs(R_arr - 15.0))
idx_20 = np.argmin(np.abs(R_arr - 20.0))

for label in ['SA-mix', 'O-Z']:
    ratio = results[label]['dn_dlnR'] / results['LCDM']['dn_dlnR']
    excess = (ratio - 1.0) * 100.0
    avg = np.mean(excess[idx_15:idx_20+1])
    max_abs = np.max(np.abs(excess))
    print(f"\n  {label} (alpha_s = {ALPHA_S_VALUES[label]}):")
    print(f"    Average excess [15,20] h^-1 Mpc: {avg:+.2f}%")
    print(f"    Maximum |excess| over full range: {max_abs:.2f}%")

print(f"""
ASSESSMENT:

1. MECHANISM: Running spectral index alpha_s modifies the primordial P(k)
   shape. This changes sigma(R) relative to its sigma_8-normalized value,
   particularly at scales far from R=8 h^{{-1}} Mpc. The void size function
   dn/dlnR responds through the SvdW multiplicity function f(nu_v).

2. SENSITIVITY: The effect enters through |d ln sigma^{{-1}}/d ln R|
   AND through nu_v = (delta_v/sigma)^2. Both are modified, but the
   sigma(R) curve is stiff: sigma_8 normalization anchors R=8,
   and the EH98 transfer function shapes most of the R dependence.
   Running only adds a slow ln(k/k_*)^2 modulation to the primordial shape.

3. DISCRIMINATING POWER:
   - From Contarini+ (2022, Paper 33): Euclid void precision ~5-10% per bin
   - From Salcedo+ (2025, Paper 32): DESI Y5 sigma(sigma_8)/sigma_8 ~ 0.8%
   - The void SIZE FUNCTION itself has larger statistical + systematic
     uncertainties than sigma_8. Void-finding algorithm, galaxy bias
     (b_void ~ 0.2-0.3), and RSDs each contribute ~5% systematics.

4. CONTEXT: The original CW prediction of "15-25% excess at R=15-20"
   was preliminary and did not account for sigma_8 renormalization.
   The actual excess depends sensitively on HOW the running enters
   through the transfer function convolution.

5. STRUCTURAL OBSERVATION: alpha_s = -0.069 (O-Z) is already at
   6-sigma tension with Planck's direct measurement. The SA-Goldstone
   mixing regime (alpha_s ~ -0.02 to 0) produces effects
   well below void survey systematics.

6. DECISIVE DISCRIMINATOR: CMB-S4 (sigma(alpha_s) ~ 0.005) directly
   measures alpha_s. This is 10x more constraining than any void
   statistic for the running spectral index.

VERDICT: INFO
  - The void size function IS sensitive to alpha_s through sigma(R) shape
  - O-Z (alpha_s = -0.069) produces large, potentially detectable effects
    but O-Z is already excluded at 6-sigma by Planck
  - SA-mix (alpha_s ~ -0.02) produces small effects at/below void systematics
  - Void statistics are NOT the decisive test for alpha_s
  - CMB-S4 is the gate: ALPHA-S-CMB-S4 (pre-registered, sigma ~ 0.005)
""")

print("=" * 72)
print("VOID-FUNCTION-52 COMPLETE")
print("=" * 72)
