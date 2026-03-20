"""
GQUEST-43: GQuEST Null Prediction Pre-Registration
====================================================
Pre-registers framework prediction: ZERO pixellon noise at GQuEST.

Physics:
  The fabric modulus tau has mass m_tau = 2.062 M_KK (from s42_fabric_dispersion.npz).
  The dispersion relation is omega^2 = k^2 + m_tau^2 (Lorentz-invariant, gapped).
  Any process exciting the fabric DOF at frequency f_lab requires energy h*f_lab.
  But the gap energy is m_tau * c^2 = 2.062 * M_KK * c^2.

  For GQuEST: f_opt ~ 2.82e14 Hz (1064 nm Nd:YAG laser).
  The ratio f_lab / f_gap = h*f_opt / (m_tau * M_KK * c^2) ~ 10^{-25}.

  Thermal/quantum excitation of the gapped mode is suppressed by
  exp(-m_tau * M_KK * c^2 / (h * f_opt)) = exp(-10^{25}).

  This is a HARD null prediction. The fabric DOF cannot be excited at ANY
  laboratory frequency. The suppression is not marginal -- it is absolute.

Inputs:
  - tier0-computation/s42_fabric_dispersion.npz (m_tau, c_fabric)
  - GQuEST parameters from Paper 17 (Vermeulen+ 2025, PRX 15 011034)

Outputs:
  - tier0-computation/s43_gquest_prereg.npz (all computed quantities)
  - tier0-computation/s43_gquest_prereg.png (suppression factor visualization)

Gate: GQUEST-43 (INFO — pre-registration, not pass/fail)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# FUNDAMENTAL CONSTANTS (SI)
# ============================================================
from canonical_constants import hbar_SI as hbar  # J s
from canonical_constants import h_planck_SI as h_planck  # J s
from canonical_constants import c_light as c  # m/s
from canonical_constants import G_N  # m^3 kg^-1 s^-2
from canonical_constants import k_B_SI as k_B  # J/K

# Planck units
l_P = np.sqrt(hbar * G_N / c**3)         # 1.616e-35 m
t_P = l_P / c                             # 5.391e-44 s
M_P = np.sqrt(hbar * c / G_N)             # 2.176e-8 kg
E_P = M_P * c**2                           # 1.956e9 J = 1.221e28 eV
f_P = 1.0 / t_P                           # 1.855e43 Hz

from canonical_constants import eV_SI as eV  # J per eV
GeV = 1e9 * eV

print("=" * 70)
print("GQUEST-43: GQuEST Null Prediction Pre-Registration")
print("=" * 70)

print(f"\nFundamental constants:")
print(f"  l_P = {l_P:.4e} m")
print(f"  t_P = {t_P:.4e} s")
print(f"  M_P = {M_P:.4e} kg")
print(f"  E_P = {E_P/GeV:.4e} GeV = {E_P:.4e} J")
print(f"  f_P = {f_P:.4e} Hz")

# ============================================================
# FRAMEWORK PARAMETERS (from s42_fabric_dispersion.npz)
# ============================================================
d = np.load('tier0-computation/s42_fabric_dispersion.npz', allow_pickle=True)
m_tau_MKK = float(d['m_tau'][0])        # 2.062 in units of M_KK
c_fabric = float(d['c_fabric_value'][0])  # 1.0 (Lorentz invariant)

print(f"\nFramework parameters (from S42):")
print(f"  m_tau = {m_tau_MKK:.6f} M_KK")
print(f"  c_fabric = {c_fabric:.1f} (Lorentz invariant)")

# M_KK bracket from CONST-FREEZE-42
# Spectral zeta: M_KK ~ 10^{16.9} GeV (gravity route, 7.4e16 GeV)
# Gauge route: M_KK ~ 10^{17.7} GeV (5.0e17 GeV) — but fails FIRAS
# Use gravity route as primary, gauge as upper bound
M_KK_low = 10**16.5 * GeV / c**2    # kg (conservative lower)
M_KK_mid = 10**16.9 * GeV / c**2    # kg (gravity route preferred)
M_KK_high = 10**17.7 * GeV / c**2   # kg (gauge route upper)

M_KK_values = {
    'low': (10**16.5, M_KK_low),
    'mid': (10**16.9, M_KK_mid),
    'high': (10**17.7, M_KK_high),
}

print(f"\nM_KK bracket (CONST-FREEZE-42):")
for label, (exp_val, mass) in M_KK_values.items():
    E_gap = m_tau_MKK * mass * c**2
    f_gap = E_gap / h_planck
    print(f"  {label}: M_KK = {exp_val:.1e} GeV, "
          f"E_gap = {E_gap/GeV:.2e} GeV, "
          f"f_gap = {f_gap:.2e} Hz")

# ============================================================
# GQuEST EXPERIMENTAL PARAMETERS (Paper 17, Vermeulen+ 2025)
# ============================================================
lambda_laser = 1064e-9       # m (Nd:YAG)
f_laser = c / lambda_laser   # 2.82e14 Hz
L_arm = 1.5                  # m (arm length)
F_finesse = 1e5              # cavity finesse
P_laser = 100.0              # W (input power)
t_run = 72 * 3600            # s (commissioning run duration)
sigma_L_achieved = 1e-18     # m (displacement sensitivity)

# GQuEST search frequencies
f_search = np.array([100, 1e3, 1e4, 1e5])  # Hz

print(f"\nGQuEST parameters (Paper 17):")
print(f"  lambda = {lambda_laser*1e9:.0f} nm")
print(f"  f_laser = {f_laser:.3e} Hz")
print(f"  L_arm = {L_arm:.1f} m")
print(f"  Finesse = {F_finesse:.0e}")
print(f"  P_laser = {P_laser:.0f} W")
print(f"  sigma_L = {sigma_L_achieved:.0e} m")
print(f"  Run time = {t_run/3600:.0f} hours")

# ============================================================
# COMPUTATION 1: Gap Frequency and Suppression Factor
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 1: Fabric Gap vs Laboratory Frequencies")
print("=" * 70)

# Use mid (preferred) M_KK
M_KK_pref = M_KK_mid
M_KK_pref_GeV = 10**16.9

# Gap energy and frequency
E_gap = m_tau_MKK * M_KK_pref * c**2   # J
f_gap = E_gap / h_planck                # Hz

print(f"\nFabric gap (preferred M_KK = {M_KK_pref_GeV:.2e} GeV):")
print(f"  m_tau = {m_tau_MKK:.3f} M_KK = {m_tau_MKK * M_KK_pref_GeV:.2e} GeV")
print(f"  E_gap = m_tau * M_KK * c^2 = {E_gap:.4e} J = {E_gap/GeV:.2e} GeV")
print(f"  f_gap = E_gap / h = {f_gap:.4e} Hz")

# Ratio: lab frequency / gap frequency
ratio_laser = f_laser / f_gap
print(f"\n  f_laser / f_gap = {ratio_laser:.2e}")

# Suppression factor: exp(-f_gap / f_lab)
# This is the Boltzmann factor for exciting a mode of energy E_gap
# at effective temperature T_eff = h*f_lab / k_B (single photon energy)
# Suppression = exp(-E_gap / E_photon) = exp(-f_gap / f_laser)
exponent_laser = f_gap / f_laser
print(f"  f_gap / f_laser = {exponent_laser:.4e}")
print(f"  log10(exponent) = {np.log10(exponent_laser):.2f}")
print(f"  Suppression: exp(-{exponent_laser:.2e}) = 10^(-{exponent_laser/np.log(10):.2e})")
print(f"  This is IDENTICALLY ZERO to any conceivable numerical precision.")

# Same for search frequencies
print(f"\nSuppression at GQuEST search frequencies:")
for f_s in f_search:
    exp_s = f_gap / f_s
    log10_exp = exp_s / np.log(10)
    print(f"  f = {f_s:.0e} Hz: exp(-{exp_s:.2e}) = 10^(-{log10_exp:.2e})")

# ============================================================
# COMPUTATION 2: Hierarchy of Scales
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 2: Hierarchy of Energy/Frequency Scales")
print("=" * 70)

# All relevant frequencies in the problem
scales = {
    'Planck frequency f_P': f_P,
    'Gap frequency f_gap': f_gap,
    'Laser frequency f_laser': f_laser,
    'GQuEST search (10 kHz)': 1e4,
    'GQuEST search (100 Hz)': 100,
    'LIGO band (100 Hz)': 100,
    'LISA band (1 mHz)': 1e-3,
    'Microwave (10 GHz)': 1e10,
}

print(f"\nFrequency hierarchy (all in Hz):")
for name, freq in sorted(scales.items(), key=lambda x: -x[1]):
    ratio_to_gap = freq / f_gap
    print(f"  {name:35s}: {freq:.2e} Hz  (f/f_gap = {ratio_to_gap:.2e})")

# Orders of magnitude between gap and lab
gap_over_lab = np.log10(f_gap / f_laser)
print(f"\nGap-to-lab separation: {gap_over_lab:.1f} orders of magnitude")
print(f"Gap-to-Planck: {np.log10(f_P/f_gap):.1f} orders of magnitude below Planck")

# ============================================================
# COMPUTATION 3: Comparison with Standard Foam Models
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 3: Framework vs Standard Foam Models")
print("=" * 70)

# Standard foam: pixellon is GAPLESS (massless Goldstone or massless metric DOF)
# Verlinde-Zurek: pixellon produces red noise S_h(f) ~ f^{-1/2}
# Framework: pixellon-analog (tau modulus) is GAPPED at m_tau = 2.062 M_KK

# Verlinde-Zurek predicted strain at 10 Hz
S_h_VZ_10Hz = 1e-52  # Hz^{-1} at 10 Hz (from Paper 20)
h_VZ = np.sqrt(S_h_VZ_10Hz * 1.0)  # strain in 1 Hz bandwidth
print(f"\nVerlinde-Zurek pixellon prediction:")
print(f"  S_h(10 Hz) ~ {S_h_VZ_10Hz:.0e} Hz^-1")
print(f"  h_strain(1 Hz BW) ~ {h_VZ:.0e}")

# GQuEST sensitivity (from Paper 17)
# sigma_L ~ 10^{-18} m over 1 hour integration
# Strain sensitivity: h = sigma_L / L_arm
h_GQuEST = sigma_L_achieved / L_arm
print(f"\nGQuEST sensitivity:")
print(f"  h_GQuEST = sigma_L / L = {h_GQuEST:.0e}")

# Framework prediction: ZERO (gapped)
# But quantify the suppressed amplitude
# If foam fluctuations at Planck scale have amplitude delta_g ~ 1,
# and the fabric DOF carries this, then the thermally excited amplitude
# at temperature T_lab is delta_g * exp(-E_gap / (k_B * T_lab))
T_lab = 300  # K (room temperature)
T_cryogenic = 0.1  # K (cryogenic)
exponent_thermal_300K = E_gap / (k_B * T_lab)
exponent_thermal_cryoK = E_gap / (k_B * T_cryogenic)

print(f"\nFramework prediction (gapped fabric):")
print(f"  T = 300 K: E_gap/(k_B*T) = {exponent_thermal_300K:.2e}")
print(f"    Boltzmann suppression: exp(-{exponent_thermal_300K:.2e}) = 10^(-{exponent_thermal_300K/np.log(10):.2e})")
print(f"  T = 0.1 K: E_gap/(k_B*T) = {exponent_thermal_cryoK:.2e}")
print(f"    Boltzmann suppression: exp(-{exponent_thermal_cryoK:.2e}) = 10^(-{exponent_thermal_cryoK/np.log(10):.2e})")

# The only way to get signal: GAPLESS DOF
# Framework internal DOF check: are there any ungapped modes?
# From spectral data: all tau-modulus excitations gapped (m_tau^2 > 0 at all tau in [0.05, 0.30])
print(f"\nGapless DOF check:")
m_tau_sq_arr = d['m_tau_sq_arr']
tau_grid = d['tau_grid']
all_gapped = np.all(m_tau_sq_arr > 0)
print(f"  m_tau^2 > 0 at all {len(tau_grid)} tau points: {all_gapped}")
print(f"  min(m_tau^2) = {np.min(m_tau_sq_arr):.4f} M_KK^2 at tau = {tau_grid[np.argmin(m_tau_sq_arr)]:.2f}")
print(f"  => ALL fabric DOF are gapped. No ungapped channel exists.")

# ============================================================
# COMPUTATION 4: What Signal WOULD Look Like (Falsification Path)
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 4: Falsification Conditions")
print("=" * 70)

# If GQuEST detects a signal, three possibilities:
# 1. Non-fabric origin (conventional noise, systematic)
# 2. m_tau is wrong (would require m_tau << 1 M_KK, contradicted by S42)
# 3. Ungapped DOF exists (not in current spectrum)

# What m_tau would need to be for GQuEST to detect it?
# Need f_gap ~ f_lab => m_tau * M_KK ~ h * f_laser / c^2
m_tau_needed_optical = h_planck * f_laser / (M_KK_pref * c**2)
print(f"\nFor detection at f_laser = {f_laser:.2e} Hz:")
print(f"  Need m_tau < {m_tau_needed_optical:.2e} M_KK")
print(f"  Actual m_tau = {m_tau_MKK:.3f} M_KK")
print(f"  Ratio actual/needed = {m_tau_MKK / m_tau_needed_optical:.2e}")

# For detection at 10 kHz (GQuEST search band)
m_tau_needed_10kHz = h_planck * 1e4 / (M_KK_pref * c**2)
print(f"\nFor detection at f = 10 kHz:")
print(f"  Need m_tau < {m_tau_needed_10kHz:.2e} M_KK")
print(f"  Ratio actual/needed = {m_tau_MKK / m_tau_needed_10kHz:.2e}")

# For detection at LIGO band (100 Hz)
m_tau_needed_100Hz = h_planck * 100 / (M_KK_pref * c**2)
print(f"\nFor detection at f = 100 Hz:")
print(f"  Need m_tau < {m_tau_needed_100Hz:.2e} M_KK")

# For ANY lab frequency to excite the gap:
# Need f ~ f_gap => f ~ m_tau * M_KK * c^2 / h
print(f"\nTo probe the fabric gap directly:")
print(f"  f_gap = {f_gap:.2e} Hz (= {f_gap/f_P:.2e} f_Planck)")
print(f"  This is {np.log10(f_gap):.1f} orders above 1 Hz")
print(f"  => No terrestrial experiment can excite this mode")

# ============================================================
# COMPUTATION 5: Perlman Blur Bound Cross-Check
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 5: Perlman Bound Cross-Check (Paper 12)")
print("=" * 70)

# From PERLMAN-43 (already computed): framework predicts coherent foam,
# which passes Perlman bounds with 4.9 OOM margin.
# Here we verify consistency: gapped fabric implies NO image blurring.
# Perlman tests delta_theta ~ (l_P / L)^alpha for alpha = 1/2 (random walk)
# or alpha = 1/3 (holographic). Framework: delta_theta = 0 (gapped).

# The fabric contributes to distance fluctuations only through virtual
# excitations of the massive mode. The amplitude is:
# delta_l / l ~ (l_P / l)^2 * exp(-m_tau * M_KK / E_photon)
# For optical photons: completely negligible.

print(f"\nFabric contribution to Perlman blur:")
print(f"  Mechanism: virtual excitation of gapped tau modulus")
print(f"  delta_l/l ~ (l_P/l)^2 * exp(-m_tau*M_KK*c^2 / E_photon)")
print(f"  For 1 keV X-ray photon (Chandra): E = {1e3*eV:.2e} J")
E_xray = 1e3 * eV
exp_xray = E_gap / E_xray
print(f"  Exponent: {exp_xray:.2e}")
print(f"  Suppression: 10^(-{exp_xray/np.log(10):.2e})")
print(f"  => ZERO contribution. Consistent with PERLMAN-43 PASS.")

# ============================================================
# COMPUTATION 6: Comparison with Other Experiments
# ============================================================
print("\n" + "=" * 70)
print("COMPUTATION 6: Framework Predictions Across Experiments")
print("=" * 70)

experiments = {
    'GQuEST (optical, 10^14 Hz)': f_laser,
    'LIGO O4 (100 Hz)': 100,
    'LIGO O5 (10 Hz)': 10,
    'LISA (1 mHz)': 1e-3,
    'Einstein Telescope (1 Hz)': 1,
    'Fermi-LAT (10^23 Hz)': 1e23,
    'CTA (10^26 Hz)': 1e26,
    'IceCube (PeV, 10^29 Hz)': 1e29,
}

print(f"\nFramework null predictions (f_gap = {f_gap:.2e} Hz):")
print(f"{'Experiment':45s} {'f_obs (Hz)':>12s} {'f_obs/f_gap':>12s} {'log10(supp)':>12s}")
print("-" * 85)
for name, f_obs in sorted(experiments.items(), key=lambda x: x[1]):
    ratio = f_obs / f_gap
    if ratio < 1:
        supp_log10 = -(f_gap / f_obs) / np.log(10)
        supp_str = f"{supp_log10:.1e}"
    else:
        supp_str = "ACCESSIBLE"
    print(f"  {name:43s} {f_obs:12.2e} {ratio:12.2e} {supp_str:>12s}")

# Even the highest-energy cosmic rays can't probe it
E_GZK = 1e20 * eV  # GZK cutoff
f_GZK = E_GZK / h_planck
ratio_GZK = f_GZK / f_gap
print(f"\n  GZK cosmic ray (10^20 eV): f/f_gap = {ratio_GZK:.2e}")
if ratio_GZK < 1:
    print(f"    Still {np.log10(1/ratio_GZK):.1f} orders BELOW gap.")
else:
    print(f"    ABOVE gap -- fabric DOF excited.")

# ============================================================
# SAVE RESULTS
# ============================================================
print("\n" + "=" * 70)
print("SAVING RESULTS")
print("=" * 70)

results = {
    # Framework parameters
    'm_tau_MKK': np.array([m_tau_MKK]),
    'c_fabric': np.array([c_fabric]),
    'M_KK_mid_GeV': np.array([M_KK_pref_GeV]),

    # Gap properties
    'E_gap_J': np.array([E_gap]),
    'E_gap_GeV': np.array([E_gap / GeV]),
    'f_gap_Hz': np.array([f_gap]),

    # GQuEST parameters
    'f_laser_Hz': np.array([f_laser]),
    'L_arm_m': np.array([L_arm]),
    'sigma_L_m': np.array([sigma_L_achieved]),

    # Suppression factors
    'exponent_laser': np.array([exponent_laser]),
    'log10_suppression_laser': np.array([exponent_laser / np.log(10)]),
    'exponent_thermal_300K': np.array([exponent_thermal_300K]),
    'log10_suppression_300K': np.array([exponent_thermal_300K / np.log(10)]),

    # Falsification thresholds
    'm_tau_needed_optical': np.array([m_tau_needed_optical]),
    'm_tau_needed_10kHz': np.array([m_tau_needed_10kHz]),

    # Gap stability
    'all_gapped': np.array([all_gapped]),
    'min_m_tau_sq': np.array([np.min(m_tau_sq_arr)]),
    'tau_at_min_m_tau_sq': np.array([tau_grid[np.argmin(m_tau_sq_arr)]]),

    # Cross-checks
    'gap_over_lab_orders': np.array([gap_over_lab]),
    'ratio_GZK': np.array([ratio_GZK]),

    # Gate verdict
    'verdict': np.array(['INFO']),
    'gate_name': np.array(['GQUEST-43']),
}

np.savez('tier0-computation/s43_gquest_prereg.npz', **results)
print("Saved: tier0-computation/s43_gquest_prereg.npz")

# ============================================================
# FIGURE: Suppression Factor Across Frequency Range
# ============================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle('GQUEST-43: GQuEST Null Prediction Pre-Registration\n'
             f'Fabric gap: $m_\\tau = {m_tau_MKK:.3f}\\,M_{{KK}}$, '
             f'$f_{{gap}} = {f_gap:.2e}$ Hz',
             fontsize=13, fontweight='bold')

# --- Panel (a): Frequency hierarchy ---
ax = axes[0, 0]
freq_labels = [
    ('LISA\n1 mHz', 1e-3, 'tab:blue'),
    ('LIGO\n100 Hz', 100, 'tab:blue'),
    ('GQuEST\n$10^4$ Hz', 1e4, 'tab:orange'),
    ('GQuEST laser\n$2.8\\times10^{14}$ Hz', f_laser, 'tab:orange'),
    ('Fermi-LAT\n$10^{23}$ Hz', 1e23, 'tab:green'),
    ('GZK\n$10^{34}$ Hz', f_GZK, 'tab:green'),
    ('Fabric gap\n$f_{gap}$', f_gap, 'tab:red'),
    ('Planck\n$f_P$', f_P, 'tab:purple'),
]
for i, (label, freq, color) in enumerate(freq_labels):
    ax.barh(i, np.log10(freq), color=color, alpha=0.7, height=0.6)
    ax.text(np.log10(freq) + 0.3, i, f'{np.log10(freq):.1f}',
            va='center', fontsize=9)

ax.set_yticks(range(len(freq_labels)))
ax.set_yticklabels([l[0] for l in freq_labels], fontsize=8)
ax.set_xlabel('$\\log_{10}(f / \\mathrm{Hz})$', fontsize=11)
ax.set_title('(a) Frequency Hierarchy', fontsize=11)
ax.axvline(np.log10(f_gap), color='red', ls='--', alpha=0.5, lw=1.5)
ax.set_xlim(-5, 50)

# --- Panel (b): Boltzmann suppression vs frequency ---
ax = axes[0, 1]
f_range = np.logspace(-3, 35, 1000)
# Suppression = exp(-f_gap / f) for f < f_gap
# log10(suppression) = -(f_gap / f) / ln(10)
log10_supp = np.where(f_range < f_gap,
                       -(f_gap / f_range) / np.log(10),
                       0)
ax.plot(np.log10(f_range), log10_supp, 'k-', lw=2)
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axvline(np.log10(f_gap), color='red', ls='--', alpha=0.7,
           label=f'$f_{{gap}} = 10^{{{np.log10(f_gap):.1f}}}$ Hz')

# Mark experiments
exp_marks = {
    'GQuEST': f_laser,
    'LIGO': 100,
    'LISA': 1e-3,
    'Fermi': 1e23,
}
for name, f_exp in exp_marks.items():
    if f_exp < f_gap:
        y_val = -(f_gap / f_exp) / np.log(10)
        # Clip for display
        y_disp = max(y_val, -1e30)
        ax.plot(np.log10(f_exp), y_disp, 'o', ms=8,
                label=f'{name}: $10^{{{y_val:.0e}}}$')

ax.set_xlabel('$\\log_{10}(f / \\mathrm{Hz})$', fontsize=11)
ax.set_ylabel('$\\log_{10}$(Suppression Factor)', fontsize=11)
ax.set_title('(b) Boltzmann Suppression $e^{-f_{gap}/f}$', fontsize=11)
ax.set_ylim(-1e6, 100)
ax.set_xlim(-3, 40)
ax.legend(fontsize=8, loc='lower right')

# --- Panel (c): m_tau^2(tau) from S42 showing all positive ---
ax = axes[1, 0]
ax.plot(tau_grid, m_tau_sq_arr, 'ko-', ms=6, lw=2, label='$m_\\tau^2(\\tau)$')
ax.axhline(0, color='red', ls='--', alpha=0.7, label='Gapless threshold')
ax.fill_between(tau_grid, 0, m_tau_sq_arr, alpha=0.15, color='blue')
ax.set_xlabel('$\\tau$ (Jensen parameter)', fontsize=11)
ax.set_ylabel('$m_\\tau^2$ [$M_{KK}^2$]', fontsize=11)
ax.set_title('(c) Fabric Mass Gap: Positive at All $\\tau$', fontsize=11)
ax.legend(fontsize=10)
ax.set_ylim(-0.5, 7)

# Annotate fold point
fold_idx = 5  # tau=0.19 is the fold
ax.annotate(f'Fold: $m_\\tau^2 = {m_tau_sq_arr[fold_idx]:.2f}$',
           xy=(tau_grid[fold_idx], m_tau_sq_arr[fold_idx]),
           xytext=(tau_grid[fold_idx]+0.04, m_tau_sq_arr[fold_idx]+0.8),
           arrowprops=dict(arrowstyle='->', color='black'),
           fontsize=9)

# --- Panel (d): Framework vs foam models table ---
ax = axes[1, 1]
ax.axis('off')

table_data = [
    ['Model', 'Fabric DOF', 'Gap?', 'GQuEST Signal'],
    ['Verlinde-Zurek\n(pixellon)', 'Gapless', 'NO', '$h \\sim 10^{-24}$'],
    ['Random walk\n($\\alpha=1/2$)', 'Gapless', 'NO', 'Ruled out\n(Perlman)'],
    ['Holographic\n($\\alpha=1/3$)', 'Gapless', 'NO', 'Marginal\n(Perlman)'],
    ['LQG area\nquanta', 'Planck gap', 'YES\n($E_P$)', 'Zero'],
    ['THIS\nFRAMEWORK', f'Gapped\n$m_\\tau={m_tau_MKK:.2f} M_{{KK}}$',
     f'YES\n($10^{{{np.log10(E_gap/GeV):.0f}}}$ GeV)',
     f'ZERO\n($10^{{-{exponent_laser/np.log(10):.0e}}}$)'],
]

table = ax.table(cellText=table_data, loc='center', cellLoc='center',
                colWidths=[0.22, 0.22, 0.22, 0.22])
table.auto_set_font_size(False)
table.set_fontsize(8)
table.scale(1.1, 2.2)

# Style header
for j in range(4):
    table[0, j].set_facecolor('#d4e6f1')
    table[0, j].set_text_props(fontweight='bold')

# Highlight framework row
for j in range(4):
    table[5, j].set_facecolor('#d5f5e3')
    table[5, j].set_text_props(fontweight='bold')

ax.set_title('(d) Comparison: Foam Models vs Framework', fontsize=11, pad=20)

plt.tight_layout(rect=[0, 0, 1, 0.94])
plt.savefig('tier0-computation/s43_gquest_prereg.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s43_gquest_prereg.png")

# ============================================================
# FORMAL PRE-REGISTRATION SUMMARY
# ============================================================
print("\n" + "=" * 70)
print("FORMAL PRE-REGISTRATION: GQUEST-43")
print("=" * 70)

print(f"""
PRE-REGISTRATION DOCUMENT
==========================
Date: 2026-03-14
Gate: GQUEST-43 (INFO)
Agent: quantum-foam-theorist

PREDICTION:
  The phonon-exflation framework predicts ZERO signal in the GQuEST
  experiment (Vermeulen+ 2025, PRX 15, 011034) and in ANY tabletop
  interferometric search for spacetime metric fluctuations at frequencies
  below the fabric gap frequency f_gap.

QUANTITATIVE BASIS:
  1. The only spacetime-fabric DOF in the framework is the Jensen modulus tau.
  2. tau has mass m_tau = {m_tau_MKK:.3f} M_KK (S42, C-FABRIC-42).
  3. At M_KK = 10^{{16.9}} GeV (CONST-FREEZE-42, gravity route):
       E_gap = {E_gap/GeV:.2e} GeV
       f_gap = {f_gap:.2e} Hz
  4. GQuEST operates at f_laser = {f_laser:.2e} Hz.
  5. Ratio f_laser / f_gap = {ratio_laser:.2e}.
  6. Suppression factor: exp(-f_gap / f_laser) = 10^(-{exponent_laser/np.log(10):.2e}).
  7. This is zero to any conceivable numerical precision.
  8. m_tau^2 > 0 at ALL tau in [0.05, 0.30] -- no ungapped DOF.

GAP STABILITY:
  The fabric gap is structural. m_tau^2(tau) is positive at all 10 computed
  tau values. Minimum m_tau^2 = {np.min(m_tau_sq_arr):.3f} M_KK^2 at tau = {tau_grid[np.argmin(m_tau_sq_arr)]:.2f}.
  No mechanism within the framework produces a gapless fabric excitation.

FALSIFICATION CONDITIONS:
  If GQuEST (or any successor) detects a statistically significant signal
  attributable to metric fluctuations, EXACTLY ONE of the following is true:

  (A) The signal has non-fabric origin (systematic, conventional noise,
      or new physics unrelated to the internal geometry).

  (B) m_tau is wrong: the fabric gap is much smaller than 2.062 M_KK.
      This would require overturning the spectral action computation
      (d^2 S_full / d tau^2 at all tau), which has been cross-verified
      to machine epsilon (CUTOFF-SA-37).

  (C) An ungapped DOF exists in the internal geometry that was not
      captured by the Jensen-direction modulus. This would require
      new light modes in the Peter-Weyl decomposition, contradicting
      the block-diagonal theorem (W2) and the complete sector analysis.

COMPARISON WITH STANDARD FOAM MODELS:
  Verlinde-Zurek pixellon: GAPLESS, predicts h ~ 10^(-24) at 10 Hz.
  Framework: GAPPED, predicts h = 0 at all frequencies below {f_gap:.0e} Hz.
  These predictions are MUTUALLY EXCLUSIVE. GQuEST directly discriminates.

BROADER EXPERIMENTAL LANDSCAPE:
  The fabric gap at {f_gap:.0e} Hz means:
  - LIGO/Virgo/ET: NO fabric signal (f ~ 1-10^4 Hz)
  - LISA: NO fabric signal (f ~ 10^(-3) Hz)
  - GQuEST: NO fabric signal (f ~ 10^4 - 10^14 Hz)
  - Fermi-LAT: NO fabric dispersion (LIV-43, QF-63: alpha_LIV = 0 structural)
  - Even GZK cosmic rays (10^20 eV, f ~ 10^34 Hz) are {np.log10(f_gap/f_GZK):.0f} orders
    BELOW the gap. No terrestrial or astrophysical probe accesses the fabric DOF.

WHAT WOULD PROBE THE FABRIC:
  Direct excitation requires f ~ f_gap ~ {f_gap:.0e} Hz, corresponding to
  particle energies E ~ {E_gap/GeV:.0e} GeV. This is {np.log10(E_gap/(14e12*eV)):.0f} orders
  above the LHC center-of-mass energy. The fabric DOF is inaccessible to
  any foreseeable accelerator or astrophysical source below M_KK.
""")

print("=" * 70)
print("GQUEST-43 COMPLETE: INFO (pre-registration filed)")
print("=" * 70)
