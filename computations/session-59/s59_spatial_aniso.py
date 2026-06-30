#!/usr/bin/env python3
"""
s59_spatial_aniso.py — SPATIAL-ANISO-59
Spatial anisotropy from Mach 421 supersonic quench.

Physics
-------
The BCS transit is supersonic: Mach ~ 421, meaning the modulus tau sweeps
through the condensate far faster than sound can propagate across the
fabric. The acoustic metric constructed in S58 yields a Ricci scalar
R_acoustic(tau) that diverges near the sonic point.

The back-reaction of this acoustic curvature on the physical 4D metric is:

    delta_g / g ~ (M_KK / M_Pl_eff)^2 * R_acoustic

where:
  - M_KK = Kaluza-Klein compactification scale (gravity route: 7.43e16 GeV)
  - M_Pl_eff = effective Planck mass from spectral action
  - R_acoustic = dimensionless acoustic Ricci scalar [in M_KK^2 units]

Two scenarios:
  A. Homogeneous Shattering: the transit is spatially uniform (all cells
     simultaneously). Then the perturbation is isotropic and modifies
     only the scale factor — no anisotropy generated.
  B. Causal front: the transit propagates as a causal front at speed
     c_fabric. Then the perturbation has a characteristic wavelength
     lambda ~ c_fabric * dt_transit, generating anisotropy at that scale.

The question: is delta_g above or below A_s = 2.1e-9 (CMB scalar amplitude)?

Gate: SPATIAL-ANISO-59
    PASS: delta_g < 10^{-5}
    FAIL: delta_g > 10^{-3} without matching spectrum
    INFO: observable range

Author: cosmic-web-theorist
Session: S59 W4F-3
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced,
    A_s_CMB, PI,
    dt_transit, omega_tau, c_fabric,
    N_cells, H_fold,
    c_light, hbar_c_GeV_m, Mpc_to_m,
)

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("SPATIAL-ANISO-59: Spatial Anisotropy from Mach 421 Quench")
print("=" * 72)

# =============================================================================
# 1. LOAD ACOUSTIC METRIC DATA (S58)
# =============================================================================
print("\n1. LOADING ACOUSTIC METRIC DATA")
print("-" * 40)

d_am = np.load(os.path.join(outdir, 's58_acoustic_metric.npz'), allow_pickle=True)
tau_values = d_am['tau_values']      # (50,) tau grid
c_BA = d_am['c_BA']                  # (50,) BA sound speed [M_KK]
H_tau = d_am['H_tau']                # (50,) H = (1/a)(da/dtau) [M_KK]
a_tau = d_am['a_tau']                # (50,) scale factor
R_acoustic = d_am['R_acoustic']      # (50,) acoustic Ricci scalar [M_KK^2]
Mach_cosmic = d_am['Mach_cosmic']    # (50,) Mach number
T_Parker = d_am['T_Parker']          # (50,) Parker temperature
fold_idx = int(d_am['fold_idx'])

print(f"  tau grid: {len(tau_values)} points, [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
print(f"  fold_idx = {fold_idx}, tau_fold = {tau_values[fold_idx]:.3f}")
print(f"  c_BA at fold = {c_BA[fold_idx]:.4f} M_KK")
print(f"  H_tau at fold = {H_tau[fold_idx]:.4f} M_KK")
print(f"  R_acoustic at fold = {R_acoustic[fold_idx]:.4f} M_KK^2")
print(f"  Mach at fold = {Mach_cosmic[fold_idx]:.1f}")

# =============================================================================
# 2. LOAD FRIEDMANN DERIVATION DATA (S58)
# =============================================================================
print("\n2. LOADING FRIEDMANN DERIVATION DATA")
print("-" * 40)

d_fr = np.load(os.path.join(outdir, 's58_friedmann_derivation.npz'), allow_pickle=True)
M_Pl_eff_GeV = float(d_fr['M_Pl_eff_GeV'])
M_Pl_ratio = float(d_fr['M_Pl_ratio'])
G_eff_fold_GeV2 = float(d_fr['G_eff_fold_GeV2'])
R_acoustic_fold = float(d_fr['R_acoustic_fold'])
Mach_fold = float(d_fr['Mach_fold'])
H_tau_fold = float(d_fr['H_tau_fold'])
c_BA_fold = float(d_fr['c_BA_fold'])

print(f"  M_Pl_eff = {M_Pl_eff_GeV:.4e} GeV")
print(f"  M_Pl_ratio = M_Pl_eff / M_Pl_reduced = {M_Pl_ratio:.4f}")
print(f"  G_eff at fold = {G_eff_fold_GeV2:.4e} GeV^{{-2}}")
print(f"  R_acoustic at fold (from friedmann) = {R_acoustic_fold:.4f} M_KK^2")
print(f"  Mach at fold (from friedmann) = {Mach_fold:.1f}")

# =============================================================================
# 3. COMPUTE delta_g / g — THE CORE CALCULATION
# =============================================================================
print("\n3. CORE CALCULATION: delta_g / g")
print("-" * 40)

# The metric perturbation from the acoustic Ricci scalar.
# R_acoustic is in units of M_KK^2 (dimensionless in M_KK natural units).
# The back-reaction on the 4D metric is suppressed by (M_KK / M_Pl)^2.
#
# Physical reasoning: the acoustic metric is the effective metric seen by
# phonons propagating on the internal space. Its curvature R_acoustic
# represents the distortion of the sound cone. This curvature backreacts
# on the 4D Einstein equations at the level of (l_KK / l_Pl)^2 = (M_KK / M_Pl)^2.
#
# Dimensionally:
#   R_acoustic ~ M_KK^2 [energy^2]
#   delta_g / g ~ R_acoustic * G_eff ~ R_acoustic * M_KK^{-2} * (M_KK/M_Pl)^2
#              = R_acoustic * (1/M_Pl^2) = (M_KK/M_Pl)^2 * (R_acoustic / M_KK^2) * M_KK^2 / M_Pl^2
#              ... simplifying: if R_acoustic is dimensionless (already in M_KK units):
#   delta_g / g = (M_KK / M_Pl_eff)^2 * R_acoustic_dimensionless

M_KK_GeV = M_KK_gravity  # 7.43e16 GeV (gravity route)

# Ratio (M_KK / M_Pl_eff)^2
ratio_MKK_MPl = M_KK_GeV / M_Pl_eff_GeV
ratio_sq = ratio_MKK_MPl**2

print(f"  M_KK (gravity) = {M_KK_GeV:.4e} GeV")
print(f"  M_Pl_eff = {M_Pl_eff_GeV:.4e} GeV")
print(f"  M_KK / M_Pl_eff = {ratio_MKK_MPl:.6e}")
print(f"  (M_KK / M_Pl_eff)^2 = {ratio_sq:.6e}")

# R_acoustic at the fold from S58
R_ac_fold = R_acoustic[fold_idx]
R_ac_max = np.max(np.abs(R_acoustic))
R_ac_friedmann = R_acoustic_fold

print(f"\n  R_acoustic (50-pt grid):")
print(f"    At fold (idx={fold_idx}): {R_ac_fold:.4f}")
print(f"    Max |R_acoustic|: {R_ac_max:.4f}")
print(f"    From friedmann npz: {R_ac_friedmann:.4f}")

# delta_g/g at the fold
delta_g_fold = ratio_sq * np.abs(R_ac_fold)
delta_g_max = ratio_sq * R_ac_max
delta_g_friedmann = ratio_sq * np.abs(R_ac_friedmann)

# Full tau-dependent delta_g
delta_g_tau = ratio_sq * np.abs(R_acoustic)

print(f"\n  delta_g / g:")
print(f"    At fold: {delta_g_fold:.6e}")
print(f"    Maximum: {delta_g_max:.6e}")
print(f"    From friedmann R: {delta_g_friedmann:.6e}")
print(f"    log10(delta_g_fold) = {np.log10(delta_g_fold) if delta_g_fold > 0 else -np.inf:.2f}")
print(f"    log10(delta_g_max) = {np.log10(delta_g_max) if delta_g_max > 0 else -np.inf:.2f}")

# =============================================================================
# 4. COMPARISON WITH CMB SCALAR AMPLITUDE
# =============================================================================
print("\n4. COMPARISON WITH CMB SCALAR AMPLITUDE")
print("-" * 40)

print(f"  A_s (CMB) = {A_s_CMB:.2e}")
print(f"  delta_g (fold) = {delta_g_fold:.6e}")
print(f"  delta_g / A_s = {delta_g_fold / A_s_CMB:.4e}")

if delta_g_fold > A_s_CMB:
    print(f"  delta_g EXCEEDS A_s by factor {delta_g_fold / A_s_CMB:.2e}")
    print(f"  => Would imprint on CMB/LSS if inhomogeneous")
elif delta_g_fold > 1e-15:
    print(f"  delta_g BELOW A_s by factor {A_s_CMB / delta_g_fold:.2e}")
    print(f"  => Invisible to CMB/LSS")
else:
    print(f"  delta_g negligibly small")

# =============================================================================
# 5. SCENARIO A: HOMOGENEOUS SHATTERING
# =============================================================================
print("\n5. SCENARIO A: HOMOGENEOUS SHATTERING")
print("-" * 40)
print("  If the transit is spatially uniform (all cells simultaneously),")
print("  the perturbation is isotropic and modifies only the scale factor.")
print("  No spatial anisotropy is generated.")
print(f"  delta_a / a = delta_g / g = {delta_g_fold:.6e}")
print(f"  This is a UNIFORM rescaling — pure conformal perturbation.")
print(f"  It shifts the effective scale factor at the transit epoch but")
print(f"  generates NO angular power spectrum contributions.")
print(f"  => GEOMETRIC contribution: isotropic, non-observable")

# =============================================================================
# 6. SCENARIO B: CAUSAL FRONT PROPAGATION
# =============================================================================
print("\n6. SCENARIO B: CAUSAL FRONT PROPAGATION")
print("-" * 40)

# If the transit propagates as a causal front at speed c_fabric,
# the perturbation has a characteristic wavelength:
#   lambda_front = c_fabric * dt_transit
# where both are in M_KK units.

lambda_front_MKK = c_fabric * dt_transit  # M_KK^{-1} units
print(f"  c_fabric = {c_fabric:.4f} M_KK")
print(f"  dt_transit = {dt_transit:.6e} M_KK^{{-1}}")
print(f"  lambda_front = c_fabric * dt_transit = {lambda_front_MKK:.4e} M_KK^{{-1}}")

# Convert to physical units
# lambda_phys = lambda_front / M_KK [in natural units where hbar=c=1]
# In meters: lambda_phys = lambda_front * hbar_c / M_KK
lambda_phys_m = lambda_front_MKK * hbar_c_GeV_m / M_KK_GeV
lambda_phys_Mpc = lambda_phys_m / Mpc_to_m

print(f"\n  Physical scale of causal front:")
print(f"    lambda = {lambda_phys_m:.4e} m")
print(f"    lambda = {lambda_phys_Mpc:.4e} Mpc")

# Compare to Hubble radius at transit
# H_transit in M_KK units, physical H = H_tau * M_KK * omega_tau
# Actually H_tau is the moduli-space Hubble rate.
# The physical Hubble time at transit is ~ 1/H_fold in M_KK^{-1} units
R_Hubble_MKK = 1.0 / H_fold  # M_KK^{-1}
R_Hubble_m = R_Hubble_MKK * hbar_c_GeV_m / M_KK_GeV

print(f"\n  Hubble radius at transit:")
print(f"    R_H = 1/H_fold = {R_Hubble_MKK:.6e} M_KK^{{-1}}")
print(f"    R_H = {R_Hubble_m:.4e} m")

ratio_front_Hubble = lambda_front_MKK / R_Hubble_MKK
print(f"    lambda_front / R_H = {ratio_front_Hubble:.4e}")

if lambda_front_MKK < R_Hubble_MKK:
    print(f"  Causal front SMALLER than Hubble radius")
    print(f"  => Sub-horizon perturbation (if it existed)")
else:
    print(f"  Causal front LARGER than Hubble radius")
    print(f"  => Super-horizon perturbation")

# The amplitude of the causal-front perturbation is still delta_g
print(f"\n  Causal front perturbation amplitude: delta_g = {delta_g_fold:.6e}")
print(f"  This perturbation has wavenumber k = 2*pi/lambda")
k_front_MKK = 2 * PI / lambda_front_MKK  # M_KK
k_front_Mpc = 2 * PI / lambda_phys_Mpc   # Mpc^{-1} (if lambda in Mpc)
print(f"  k_front = {k_front_MKK:.4e} M_KK")
print(f"  k_front = {k_front_Mpc:.4e} Mpc^{{-1}}")

# =============================================================================
# 7. MACH NUMBER AND SONIC HORIZON
# =============================================================================
print("\n7. MACH NUMBER AND SONIC HORIZON")
print("-" * 40)

Mach_fold_val = Mach_cosmic[fold_idx]
print(f"  Mach at fold = {Mach_fold_val:.1f}")

# Sonic horizon: the region within which sound can propagate during dt_transit
# R_sonic = c_BA * dt_transit
R_sonic_MKK = c_BA[fold_idx] * dt_transit
R_sonic_m = R_sonic_MKK * hbar_c_GeV_m / M_KK_GeV
print(f"  c_BA at fold = {c_BA[fold_idx]:.4f} M_KK")
print(f"  Sonic horizon during transit = c_BA * dt_transit = {R_sonic_MKK:.6e} M_KK^{{-1}}")
print(f"  Sonic horizon = {R_sonic_m:.4e} m")
print(f"  Compare: modulus covers tau_fold = {tau_fold} in dt = {dt_transit:.6e}")
print(f"  => Sound CANNOT communicate across the system during transit")
print(f"  => Mach 421 means the transit is 421x faster than sound")

# The transit sweeps distance L_transit = v_modulus * dt_transit = H * a * dt_transit
# But in the internal space, the relevant question is: can different cells
# of the 32-cell tessellation communicate?
# Cell crossing time ~ L_cell / c_BA
# System crossing time ~ N_cells^{1/3} * L_cell / c_BA
# If Mach >> 1, the answer is NO — each cell undergoes the transit independently.

print(f"\n  With {N_cells} cells and Mach = {Mach_fold_val:.0f}:")
print(f"  Each cell undergoes transit INDEPENDENTLY (no causal contact)")
print(f"  => Phase of condensate in each cell is RANDOM (Kibble-Zurek)")
print(f"  => But ALL cells experience the SAME tau evolution")
print(f"  => The quench is HOMOGENEOUS in tau, even though condensate phases are random")
print(f"  => Domain walls form (random phases) but delta_g is tau-dependent only")

# =============================================================================
# 8. THE KEY DISTINCTION: tau-homogeneity vs phase-randomness
# =============================================================================
print("\n8. KEY DISTINCTION: tau-HOMOGENEITY vs PHASE-RANDOMNESS")
print("-" * 40)

# The transit modifies tau uniformly across all cells (it's a global
# moduli evolution). What becomes random is the POST-transit condensate
# phase (U(1)_7 broken → random phase per cell = domain walls).
#
# The metric perturbation delta_g depends on |Delta(tau)|^2, not on the
# phase angle. Since the Shattering produces P_exc = 1.0 (complete
# pair-breaking) in ALL cells uniformly, delta_g is:
#   - Uniform in amplitude (same |Delta| = 0 post-transit in all cells)
#   - Therefore ISOTROPIC
#   - No CMB anisotropy from the transit itself
#
# The domain walls between cells have energy ~ J * delta_sigma^2 (from
# S58 off-Jensen domain wall calculation), which IS spatially varying.
# But this is a topological defect contribution, not the bulk metric.

E_DW_max = 5.28e-6  # max E_DW/E_J from S58 off_jensen_dw (delta_sigma=0.015)  # (local)
delta_g_DW = ratio_sq * E_DW_max  # Domain wall contribution to delta_g

print(f"  The Shattering is tau-HOMOGENEOUS:")
print(f"    ALL cells undergo tau=0 -> tau_fold simultaneously")
print(f"    P_exc = 1.0 in every cell (S38)")
print(f"    |Delta|^2 -> 0 in every cell (pair-breaking complete)")
print(f"    delta_g depends on |Delta(tau)|^2, not phase")
print(f"    => delta_g is ISOTROPIC (Scenario A)")
print(f"")
print(f"  Domain wall contribution (post-transit):")
print(f"    max E_DW / E_J ~ {E_DW_max:.2e} (S58 OFF-JENSEN-DW)")
print(f"    delta_g from DW ~ {delta_g_DW:.4e}")
print(f"    This is {delta_g_DW / A_s_CMB:.2e} x A_s")

# =============================================================================
# 9. QUANTITATIVE SUMMARY
# =============================================================================
print("\n9. QUANTITATIVE SUMMARY")
print("=" * 72)

print(f"\n  INPUTS:")
print(f"    M_KK = {M_KK_GeV:.4e} GeV (gravity route)")
print(f"    M_Pl_eff = {M_Pl_eff_GeV:.4e} GeV (spectral action)")
print(f"    (M_KK/M_Pl)^2 = {ratio_sq:.6e}")
print(f"    R_acoustic (fold) = {R_ac_fold:.4f} M_KK^2")
print(f"    Mach (fold) = {Mach_fold_val:.1f}")
print(f"    c_fabric = {c_fabric:.2f} M_KK")
print(f"    dt_transit = {dt_transit:.6e} M_KK^{{-1}}")

print(f"\n  RESULTS:")
print(f"    delta_g / g (fold) = {delta_g_fold:.6e}")
print(f"    delta_g / g (max)  = {delta_g_max:.6e}")
print(f"    log10(delta_g) = {np.log10(delta_g_fold) if delta_g_fold > 0 else -np.inf:.2f}")
print(f"    A_s (CMB) = {A_s_CMB:.2e}")
print(f"    delta_g / A_s = {delta_g_fold / A_s_CMB:.4e}")

# =============================================================================
# 10. GATE VERDICT: SPATIAL-ANISO-59
# =============================================================================
print("\n10. GATE VERDICT: SPATIAL-ANISO-59")
print("=" * 72)

if delta_g_fold < 1e-5:
    gate_verdict = "PASS"
    gate_detail = (
        f"delta_g/g = {delta_g_fold:.4e} < 10^{{-5}}. "
        f"Transit is Mach {Mach_fold_val:.0f} (supersonic). "
        f"(M_KK/M_Pl)^2 = {ratio_sq:.4e}. "
        f"R_acoustic = {R_ac_fold:.2f} M_KK^2. "
        f"Shattering is tau-homogeneous: all {N_cells} cells undergo "
        f"identical tau evolution => delta_g is ISOTROPIC. "
        f"No spatial anisotropy imprinted on 4D metric. "
        f"delta_g/A_s = {delta_g_fold / A_s_CMB:.2e} "
        f"({'BELOW' if delta_g_fold < A_s_CMB else 'ABOVE'} CMB amplitude)."
    )
elif delta_g_fold < 1e-3:
    gate_verdict = "INFO"
    gate_detail = (
        f"delta_g/g = {delta_g_fold:.4e} in observable range [10^{{-5}}, 10^{{-3}}]. "
        f"Mach = {Mach_fold_val:.0f}. R_acoustic = {R_ac_fold:.2f}. "
        f"(M_KK/M_Pl)^2 = {ratio_sq:.4e}. "
        f"delta_g/A_s = {delta_g_fold / A_s_CMB:.2e}."
    )
else:
    gate_verdict = "FAIL"
    gate_detail = (
        f"delta_g/g = {delta_g_fold:.4e} > 10^{{-3}}. "
        f"Metric perturbation too large without matching CMB spectrum."
    )

print(f"  Gate: SPATIAL-ANISO-59")
print(f"  Verdict: {gate_verdict}")
print(f"  {gate_detail}")

# =============================================================================
# 11. SAVE RESULTS
# =============================================================================
print("\n11. SAVING RESULTS")
print("-" * 40)

outpath = os.path.join(outdir, 's59_spatial_aniso.npz')
np.savez(outpath,
    # Inputs
    tau_values=tau_values,
    fold_idx=np.array(fold_idx),
    M_KK_GeV=np.array(M_KK_GeV),
    M_Pl_eff_GeV=np.array(M_Pl_eff_GeV),
    ratio_MKK_MPl=np.array(ratio_MKK_MPl),
    ratio_sq=np.array(ratio_sq),
    # Acoustic metric quantities
    R_acoustic=R_acoustic,
    R_acoustic_fold=np.array(R_ac_fold),
    Mach_cosmic=Mach_cosmic,
    c_BA=c_BA,
    # Core result
    delta_g_tau=delta_g_tau,
    delta_g_fold=np.array(delta_g_fold),
    delta_g_max=np.array(delta_g_max),
    delta_g_over_As=np.array(delta_g_fold / A_s_CMB),
    # Causal front
    lambda_front_MKK=np.array(lambda_front_MKK),
    lambda_front_m=np.array(lambda_phys_m),
    lambda_front_Mpc=np.array(lambda_phys_Mpc),
    R_sonic_MKK=np.array(R_sonic_MKK),
    # Domain wall contribution
    delta_g_DW=np.array(delta_g_DW),
    # Gate
    gate_name=np.array(['SPATIAL-ANISO-59']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"  Saved: {outpath}")

# =============================================================================
# 12. PLOT
# =============================================================================
print("\n12. GENERATING PLOT")
print("-" * 40)

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S59 SPATIAL-ANISO-59: Spatial Anisotropy from Mach 421 Quench',
             fontsize=14, fontweight='bold', y=0.98)

# (a) R_acoustic(tau)
ax = axes[0, 0]
ax.plot(tau_values, R_acoustic, 'b-', lw=2)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R_{\mathrm{acoustic}}$ [$M_{KK}^2$]')
ax.set_title(r'(a) Acoustic Ricci scalar $R_{\mathrm{ac}}(\tau)$')
ax.legend()
ax.grid(True, alpha=0.3)

# (b) delta_g(tau)
ax = axes[0, 1]
mask = delta_g_tau > 0
ax.semilogy(tau_values[mask], delta_g_tau[mask], 'r-', lw=2, label=r'$\delta g / g$')
ax.axhline(A_s_CMB, color='green', ls='--', lw=1.5, label=r'$A_s = 2.1\times10^{-9}$')
ax.axhline(1e-5, color='orange', ls=':', lw=1, label=r'PASS threshold $10^{-5}$')
ax.axhline(1e-3, color='red', ls=':', lw=1, label=r'FAIL threshold $10^{-3}$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\delta g / g$')
ax.set_title(r'(b) Metric perturbation $\delta g / g (\tau)$')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (c) Mach number
ax = axes[1, 0]
ax.plot(tau_values, Mach_cosmic, 'm-', lw=2)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.axhline(1.0, color='red', ls=':', lw=1, label='Mach = 1')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Mach number')
ax.set_title('(c) Mach number (transit vs sound speed)')
ax.set_yscale('log')
ax.legend()
ax.grid(True, alpha=0.3)

# (d) Summary bar chart
ax = axes[1, 1]
labels = [r'$\delta g$ (fold)', r'$\delta g$ (max)', r'$\delta g$ (DW)',
          r'$A_s$ (CMB)', r'PASS ($10^{-5}$)', r'FAIL ($10^{-3}$)']
values = [delta_g_fold, delta_g_max, delta_g_DW, A_s_CMB, 1e-5, 1e-3]
colors = ['steelblue', 'steelblue', 'teal', 'green', 'orange', 'red']
y_pos = np.arange(len(labels))
ax.barh(y_pos, [np.log10(v) if v > 0 else -30 for v in values], color=colors, alpha=0.7)
ax.set_yticks(y_pos)
ax.set_yticklabels(labels)
ax.set_xlabel(r'$\log_{10}(\delta g / g)$')
ax.set_title(f'(d) Summary: Gate {gate_verdict}')
ax.grid(True, alpha=0.3, axis='x')
# Add numeric labels
for i, v in enumerate(values):
    if v > 0:
        ax.text(np.log10(v) + 0.3, i, f'{v:.1e}', va='center', fontsize=8)

plt.tight_layout(rect=[0, 0, 1, 0.96])
plotpath = os.path.join(outdir, 's59_spatial_aniso.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print("\n" + "=" * 72)
print("COMPUTATION COMPLETE")
print("=" * 72)
