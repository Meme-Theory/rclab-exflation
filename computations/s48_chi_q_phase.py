#!/usr/bin/env python3
"""
s48_chi_q_phase.py — q-theory susceptibility: phase vs amplitude decomposition
===============================================================================

Gate: CHI-Q-PHASE-48

Physics:
  The q-theory vacuum energy rho_vac(tau) = E_spectral(tau) + E_cond(tau).

  Amplitude susceptibility chi_tau = d^2 rho_vac / dtau^2
    Measures restoring force in the modulus (tau) direction.

  Phase susceptibility chi_phi = d^2 rho_vac / dphi^2 at phi=0
    Measures restoring force for the U(1)_7 Goldstone phase.

  For a SINGLE sector: chi_phi = 0 exactly (Goldstone theorem — spontaneous
  breaking of U(1)_7 means no preferred phase, E_cond is phi-independent).

  For MULTI-SECTOR: the Leggett degree of freedom (relative phase between
  B2 and B3 condensates) contributes:
    E_inter(delta_phi) = -V(B2,B3) * |Delta_B2| * |Delta_B3| * cos(delta_phi)
    chi_phi = V(B2,B3) * |Delta_B2| * |Delta_B3|  (from -d^2/dphi^2 cos at phi=0)

  Note the sign: cos(0)=1 is a MAXIMUM of -cos, so chi_phi > 0 means the
  inter-sector coupling provides a restoring force (Leggett mode is stable).

Data sources:
  - s46_qtheory_selfconsistent.npz: rho_vac(tau), E_cond(tau), Delta_Bi(tau)
  - s35_thouless_multiband.npz: V_branch_3x3 (inter-sector pairing matrix)
  - canonical_constants.py: framework constants

Gate criteria:
  PASS if chi_phi / |chi_tau| > 0.1
  INFO if measurable but < 0.1
  FAIL if chi_phi = 0 (singlet sector only)

Session: 48
"""

import sys
sys.path.insert(0, "tier0-computation")
import numpy as np
from scipy.interpolate import UnivariateSpline
from canonical_constants import (
    tau_fold, E_cond, Delta_0_GL, Delta_B3,
    E_cond_ED_8mode, M_max_thouless
)

# =============================================================================
# 1. LOAD DATA
# =============================================================================

d46 = np.load("tier0-computation/s46_qtheory_selfconsistent.npz", allow_pickle=True)
d35 = np.load("tier0-computation/s35_thouless_multiband.npz", allow_pickle=True)

# Dense tau grid (4000 points) for spectral rho_vac
tau_dense = d46['tau_dense_sc']          # shape (4000,)
rho_raw   = d46['rho_raw_sc']           # spectral-only vacuum energy
rho_gs    = d46['rho_gs_sc']            # total (spectral + BCS constant offset)

# Coarse grid (60 points) for self-consistent BCS
tau_scan    = d46['tau_scan']            # shape (60,)
E_cond_tau  = d46['E_cond_tau']         # E_cond(tau) from self-consistent BCS
Delta_B1_sc = d46['Delta_B1_sc']        # self-consistent gaps
Delta_B2_sc = d46['Delta_B2_sc']
Delta_B3_sc = d46['Delta_B3_sc']

# Inter-sector pairing coupling (from S35 Thouless matrix)
V_branch = d35['V_branch_3x3']          # shape (3,3), rows/cols = B1, B2, B3
V_B2B3_branch = V_branch[1, 2]          # = 0.0510 (branch-averaged)
V_B3B2_branch = V_branch[2, 1]          # = 0.0680

# Also load the 8x8 element-resolved value
V_B2B3_8x8 = float(d35['V_B2B3_max'])   # = 0.0265 (maximum off-diagonal in 8x8)

# S46 constrained coupling matrix
V_constrained = d46['V_mat_constrained']  # shape (3,3)
V_B2B3_s46 = V_constrained[1, 2]         # = 0.0294

# Self-consistent gap values at fold
Delta_B1_fold = float(d46['Delta_B1_fold'])
Delta_B2_fold = float(d46['Delta_B2_fold'])
Delta_B3_fold = float(d46['Delta_B3_fold'])

print("=" * 78)
print("CHI-Q-PHASE-48: q-theory susceptibility — phase vs amplitude")
print("=" * 78)

# =============================================================================
# 2. DATA AUDIT
# =============================================================================

print("\n--- Data Audit ---")
print(f"Dense grid: {len(tau_dense)} points, tau in [{tau_dense[0]:.4f}, {tau_dense[-1]:.4f}]")
print(f"Coarse grid: {len(tau_scan)} points, tau in [{tau_scan[0]:.4f}, {tau_scan[-1]:.4f}]")
print(f"E_cond range: [{E_cond_tau.min():.6f}, {E_cond_tau.max():.6f}]")
print(f"E_cond canonical (8-mode ED): {E_cond_ED_8mode:.6f}")
print(f"E_cond at fold (S46 SC): {E_cond_tau[np.argmin(np.abs(tau_scan - tau_fold))]:.6f}")
print()
print("Inter-sector V(B2,B3) — THREE sources:")
print(f"  V_branch_3x3[1,2]  (S35 branch):     {V_B2B3_branch:.6f}")
print(f"  V_branch_3x3[2,1]  (S35 branch):     {V_B3B2_branch:.6f}")
print(f"  V_B2B3_max          (S35 8x8):        {V_B2B3_8x8:.6f}")
print(f"  V_constrained[1,2]  (S46 SC):         {V_B2B3_s46:.6f}")
print()
print("Self-consistent gaps at fold:")
print(f"  Delta_B1 = {Delta_B1_fold:.6f}")
print(f"  Delta_B2 = {Delta_B2_fold:.6f}")
print(f"  Delta_B3 = {Delta_B3_fold:.6f}")

# =============================================================================
# 3. AMPLITUDE SUSCEPTIBILITY chi_tau = d^2 rho_vac / dtau^2
# =============================================================================

print("\n" + "=" * 78)
print("SECTION A: Amplitude susceptibility chi_tau = d^2 rho_vac / dtau^2")
print("=" * 78)

# Spectral part: use dense grid with centered finite differences
targets = [0.10, 0.15, 0.19, 0.25, 0.30]

chi_tau_spec = {}
for t in targets:
    idx = np.argmin(np.abs(tau_dense - t))
    h = tau_dense[idx + 1] - tau_dense[idx]
    d2 = (rho_raw[idx + 1] - 2 * rho_raw[idx] + rho_raw[idx - 1]) / h**2
    chi_tau_spec[t] = d2

# BCS part: spline on the 60-point self-consistent E_cond
spl_Ec = UnivariateSpline(tau_scan, E_cond_tau, s=0, k=4)

chi_tau_bcs = {}
for t in targets:
    chi_tau_bcs[t] = float(spl_Ec.derivative(2)(t))

# Total amplitude susceptibility
chi_tau_total = {}
for t in targets:
    chi_tau_total[t] = chi_tau_spec[t] + chi_tau_bcs[t]

print(f"\n{'tau':>6s}  {'chi_spec':>12s}  {'chi_BCS':>12s}  {'chi_tau':>12s}")
print("-" * 50)
for t in targets:
    print(f"{t:6.2f}  {chi_tau_spec[t]:12.4f}  {chi_tau_bcs[t]:12.4f}  {chi_tau_total[t]:12.4f}")

# =============================================================================
# 4. PHASE SUSCEPTIBILITY chi_phi
# =============================================================================

print("\n" + "=" * 78)
print("SECTION B: Phase susceptibility chi_phi = d^2 rho_vac / dphi^2 at phi=0")
print("=" * 78)

# --- 4a. SINGLET SECTOR: chi_phi = 0 exactly ---
print("\n--- Singlet sector (global U(1)_7 phase) ---")
print("Goldstone theorem: E_cond(phi) = E_cond for any global phase phi.")
print("A global U(1)_7 rotation exp(i*phi*K_7) rotates ALL Cooper pairs")
print("by the same phase. Since E_cond depends only on |Delta|^2, it is")
print("phi-independent. Therefore:")
print("  chi_phi_singlet = 0   (EXACT, by Goldstone theorem)")

# --- 4b. MULTI-SECTOR: Leggett mode ---
print("\n--- Multi-sector (Leggett mode: relative phase delta_phi = phi_B2 - phi_B3) ---")
print("The inter-sector Josephson coupling is:")
print("  E_inter = -V(B2,B3) * |Delta_B2| * |Delta_B3| * cos(delta_phi)")
print("  chi_phi = d^2 E_inter / d(delta_phi)^2 |_{delta_phi=0}")
print("         = V(B2,B3) * |Delta_B2| * |Delta_B3|")
print()

# Compute chi_phi at each tau using interpolated gaps
spl_D2 = UnivariateSpline(tau_scan, Delta_B2_sc, s=0, k=3)
spl_D3 = UnivariateSpline(tau_scan, Delta_B3_sc, s=0, k=3)

# Use ALL THREE V(B2,B3) sources as a bracket
V_sources = {
    "V_8x8 (S35)":       V_B2B3_8x8,     # 0.0265 — element-resolved
    "V_constrained (S46)": V_B2B3_s46,     # 0.0294 — self-consistent
    "V_branch (S35)":      V_B2B3_branch,  # 0.0510 — branch-averaged
}

# Also include B1-B2 relative phase (Leggett mode between B1 and B2)
V_B1B2_branch = V_branch[0, 1]   # = 0.3197
V_B1B2_s46 = V_constrained[0, 1]  # = 0.1301

# B1-B3 coupling is zero (K_7 selection rule)
V_B1B3 = float(V_branch[0, 2])   # ~ 1e-29

print(f"V(B2,B3) sources:")
for name, val in V_sources.items():
    print(f"  {name}: {val:.6f}")
print(f"\nV(B1,B2) sources:")
print(f"  V_branch (S35): {V_B1B2_branch:.6f}")
print(f"  V_constrained (S46): {V_B1B2_s46:.6f}")
print(f"\nV(B1,B3) = {V_B1B3:.2e}  (zero by K_7 selection rule)")

# Compute chi_phi for B2-B3 Leggett mode using the CONSERVATIVE (smallest) V
V_B2B3_conservative = V_B2B3_8x8  # most conservative

# Also compute for B1-B2 Leggett mode
V_B1B2_conservative = V_B1B2_s46

chi_phi_B2B3 = {}
chi_phi_B1B2 = {}
chi_phi_total = {}

spl_D1 = UnivariateSpline(tau_scan, Delta_B1_sc, s=0, k=3)

print(f"\n{'tau':>6s}  {'|D_B1|':>8s}  {'|D_B2|':>8s}  {'|D_B3|':>8s}  "
      f"{'chi_B2B3':>10s}  {'chi_B1B2':>10s}  {'chi_phi':>10s}")
print("-" * 72)

for t in targets:
    D1 = abs(float(spl_D1(t)))
    D2 = abs(float(spl_D2(t)))
    D3 = abs(float(spl_D3(t)))

    # B2-B3 Leggett
    chi_23 = V_B2B3_conservative * D2 * D3
    chi_phi_B2B3[t] = chi_23

    # B1-B2 Leggett
    chi_12 = V_B1B2_conservative * D1 * D2
    chi_phi_B1B2[t] = chi_12

    # Total phase susceptibility = sum of all Leggett channels
    # (B1-B3 is zero)
    chi_phi_total[t] = chi_23 + chi_12

    print(f"{t:6.2f}  {D1:8.4f}  {D2:8.4f}  {D3:8.4f}  "
          f"{chi_23:10.6f}  {chi_12:10.6f}  {chi_phi_total[t]:10.6f}")

# =============================================================================
# 5. RATIO chi_phi / |chi_tau|
# =============================================================================

print("\n" + "=" * 78)
print("SECTION C: Ratio chi_phi / |chi_tau|")
print("=" * 78)

print(f"\n{'tau':>6s}  {'chi_phi':>10s}  {'|chi_tau|':>10s}  {'ratio':>10s}  {'verdict':>8s}")
print("-" * 52)

ratios = {}
for t in targets:
    r = chi_phi_total[t] / abs(chi_tau_total[t])
    ratios[t] = r
    verdict = "PASS" if r > 0.1 else ("INFO" if r > 0.001 else "FAIL")
    print(f"{t:6.2f}  {chi_phi_total[t]:10.6f}  {abs(chi_tau_total[t]):10.4f}  {r:10.6f}  {verdict:>8s}")

# =============================================================================
# 6. BRACKET ANALYSIS (sensitivity to V choice)
# =============================================================================

print("\n" + "=" * 78)
print("SECTION D: Sensitivity to V(B2,B3) choice")
print("=" * 78)

t_fold = 0.19
D2_fold = abs(float(spl_D2(t_fold)))
D3_fold = abs(float(spl_D3(t_fold)))
D1_fold = abs(float(spl_D1(t_fold)))

print(f"\nAt fold (tau = {t_fold}):")
print(f"  |chi_tau| = {abs(chi_tau_total[t_fold]):.4f}")
print()

for v_name, v_val in V_sources.items():
    chi_23 = v_val * D2_fold * D3_fold
    chi_12 = V_B1B2_s46 * D1_fold * D2_fold  # keep B1-B2 fixed
    chi_tot = chi_23 + chi_12
    r = chi_tot / abs(chi_tau_total[t_fold])
    print(f"  {v_name}: chi_B2B3={chi_23:.6f}, chi_total={chi_tot:.6f}, ratio={r:.4f}")

# Also do pure B2-B3 (no B1-B2) with branch V
print("\n  Pure B2-B3 Leggett (no B1-B2 channel):")
for v_name, v_val in V_sources.items():
    chi_23 = v_val * D2_fold * D3_fold
    r = chi_23 / abs(chi_tau_total[t_fold])
    print(f"    {v_name}: chi_B2B3={chi_23:.6f}, ratio={r:.6f}")

# =============================================================================
# 7. LEGGETT MODE FREQUENCY
# =============================================================================

print("\n" + "=" * 78)
print("SECTION E: Leggett mode frequency")
print("=" * 78)

# Leggett mode frequency: omega_L^2 = chi_phi * (1/N_B2 + 1/N_B3)
# where N_i = rho_i * |Delta_i|^2 (superfluid density proxy)
# In BCS: omega_L^2 ~ 2*V(B2,B3) * sqrt(Delta_B2 * Delta_B3) * (1/Delta_B2 + 1/Delta_B3)
# Simplified: omega_L^2 ~ 2*V * (sqrt(D3/D2) + sqrt(D2/D3))

rho_B2 = float(d35['rho_B2'])  # DOS at Fermi level
rho_B3 = float(d35['rho_B3'])

print(f"\nDOS: rho_B2 = {rho_B2:.4f}, rho_B3 = {rho_B3:.4f}")
print(f"Gaps at fold: Delta_B2 = {D2_fold:.4f}, Delta_B3 = {D3_fold:.4f}")

# Standard Leggett formula:
# omega_L^2 = V_{23} * (Delta_B2/N_B2 + Delta_B3/N_B3) * 2
# where N_i = rho_i is just the DOS
# More precisely: omega_L^2 = 2*V_12 * (Delta_1 * rho_2 + Delta_2 * rho_1) / (rho_1 * rho_2)

omega_L_sq_B2B3 = 2 * V_B2B3_conservative * (D2_fold / rho_B3 + D3_fold / rho_B2)
omega_L_B2B3 = np.sqrt(abs(omega_L_sq_B2B3))

print(f"\nLeggett mode (B2-B3 channel):")
print(f"  omega_L^2 = 2*V*(D2/rho_3 + D3/rho_2)")
print(f"  omega_L^2 = {omega_L_sq_B2B3:.6f}")
print(f"  omega_L   = {omega_L_B2B3:.6f}  (M_KK units)")

# Compare to pair vibration frequency
from canonical_constants import omega_PV, omega_att
print(f"\n  omega_PV (pair vibration)  = {omega_PV:.4f}")
print(f"  omega_att (attractor)      = {omega_att:.4f}")
print(f"  omega_L / omega_PV         = {omega_L_B2B3 / omega_PV:.4f}")

# =============================================================================
# 8. GATE VERDICT
# =============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: CHI-Q-PHASE-48")
print("=" * 78)

# Use fold values for gate
ratio_fold = ratios[0.19]
chi_phi_fold = chi_phi_total[0.19]
chi_tau_fold = chi_tau_total[0.19]

print(f"\nAt fold (tau = {tau_fold}):")
print(f"  chi_tau  = {chi_tau_fold:.4f}  (amplitude, d^2 rho_vac / dtau^2)")
print(f"  chi_phi  = {chi_phi_fold:.6f}  (phase, Leggett mode)")
print(f"  ratio    = {ratio_fold:.6f}")
print()

# Singlet contribution
print(f"  chi_phi (singlet)    = 0  (EXACT, Goldstone theorem)")
print(f"  chi_phi (B2-B3)      = {chi_phi_B2B3[0.19]:.6f}")
print(f"  chi_phi (B1-B2)      = {chi_phi_B1B2[0.19]:.6f}")
print(f"  chi_phi (B1-B3)      = 0  (K_7 selection rule)")
print()

if ratio_fold > 0.1:
    verdict = "PASS"
    detail = f"ratio = {ratio_fold:.4f} > 0.1"
elif chi_phi_fold > 0:
    verdict = "INFO"
    detail = f"ratio = {ratio_fold:.4f} < 0.1 but chi_phi nonzero (Leggett mode)"
else:
    verdict = "FAIL"
    detail = "chi_phi = 0 (singlet only)"

print(f"VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print()

# Physical interpretation
print("PHYSICAL INTERPRETATION:")
print("-" * 40)
print("1. The SINGLET phase susceptibility is exactly zero (Goldstone theorem).")
print("   A global U(1)_7 rotation costs no energy — this is the Nambu-Goldstone mode.")
print()
print("2. The MULTI-SECTOR Leggett mode has nonzero chi_phi from inter-sector")
print("   Josephson coupling V(B2,B3). This is a MASSIVE mode (Leggett 1966).")
print(f"   omega_Leggett = {omega_L_B2B3:.4f} M_KK.")
print()
print("3. The ratio chi_phi/|chi_tau| measures relative stiffness of the phase vs")
print(f"   amplitude channels. At {ratio_fold:.4f}, the phase channel is softer than")
print("   the amplitude channel but NOT zero — the Leggett degree of freedom provides")
print("   a physical q-theory phase susceptibility.")
print()
print("4. Amplitude susceptibility chi_tau < 0 everywhere (spectral action is concave).")
print("   The BCS contribution chi_tau_BCS > 0 partially compensates but does not")
print("   change the sign. The modulus tau is at a local MAXIMUM of rho_vac at the fold.")

# =============================================================================
# 9. SAVE
# =============================================================================

np.savez(
    "tier0-computation/s48_chi_q_phase.npz",
    # Tau grid
    tau_targets=np.array(targets),
    tau_fold=tau_fold,

    # Amplitude susceptibility
    chi_tau_spec=np.array([chi_tau_spec[t] for t in targets]),
    chi_tau_bcs=np.array([chi_tau_bcs[t] for t in targets]),
    chi_tau_total=np.array([chi_tau_total[t] for t in targets]),

    # Phase susceptibility
    chi_phi_singlet=np.zeros(len(targets)),   # exactly zero
    chi_phi_B2B3=np.array([chi_phi_B2B3[t] for t in targets]),
    chi_phi_B1B2=np.array([chi_phi_B1B2[t] for t in targets]),
    chi_phi_total=np.array([chi_phi_total[t] for t in targets]),

    # Ratios
    ratio_phi_tau=np.array([ratios[t] for t in targets]),

    # Coupling matrix data
    V_B2B3_8x8=V_B2B3_8x8,
    V_B2B3_s46=V_B2B3_s46,
    V_B2B3_branch=V_B2B3_branch,
    V_B1B2_s46=V_B1B2_s46,

    # Gaps at fold
    Delta_B1_fold=Delta_B1_fold,
    Delta_B2_fold=Delta_B2_fold,
    Delta_B3_fold=Delta_B3_fold,

    # Leggett mode
    omega_Leggett_B2B3=omega_L_B2B3,

    # Gate
    gate_name=np.array(["CHI-Q-PHASE-48"]),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\nSaved: tier0-computation/s48_chi_q_phase.npz")
print("=" * 78)
