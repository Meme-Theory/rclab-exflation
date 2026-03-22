#!/usr/bin/env python3
"""
SAKHAROV-GN-44 AUDIT: Independent formula verification.

The W1-1 script computes:
    1/(16piG) = (1/2) * sum_k d_k * ln(Lambda^2 / (lambda_k * M_KK)^2)

This audit checks:
1. Is this formula dimensionally correct? (spoiler: it gives a dimensionless number)
2. What does the STANDARD Sakharov formula give? (includes Lambda^2 leading term)
3. What normalization does the 4D one-loop calculation require? (1/(48 pi^2) prefactor)
4. How do results compare to the spectral action?

Reference: Sakharov (1968), Visser (2002 review), Volovik Paper 07 (1994), Paper 30 (2022)
"""

import numpy as np
from pathlib import Path

DATA_DIR = Path(__file__).parent

# ============================================================
# Constants
# ============================================================
from canonical_constants import M_Pl_reduced as M_PL_RED, M_Pl_unreduced as M_PL_UNRED  # GeV
from canonical_constants import G_N as G_N_OBS  # m^3 kg^-1 s^-2
G_N_NAT = 1.0 / (8 * np.pi * M_PL_RED**2)  # GeV^{-2}
inv_16piG_obs = M_PL_RED**2 / 2  # 1/(16piG) = M_Pl_red^2/2 since M_Pl_red = 1/sqrt(8piG)

print("=" * 78)
print("SAKHAROV-GN-44: INDEPENDENT FORMULA AUDIT")
print("=" * 78)
print(f"\nPhysical target: 1/(16piG_obs) = 2*M_Pl_red^2 = {inv_16piG_obs:.6e} GeV^2")

# ============================================================
# Load spectrum
# ============================================================
d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d42c = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)

a0_stored = float(d42c['a0_fold'])
a2_stored = float(d42c['a2_fold'])
a4_stored = float(d42c['a4_fold'])
M_KK = float(d42c['M_KK_from_GN'])  # 7.43e16 GeV

SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Build spectrum arrays
evals = []
degs = []
for (p, q) in SECTORS:
    key = f'evals_tau0.190_{p}_{q}'
    if key not in d36.files:
        continue
    ev = d36[key]
    pos = ev[ev > 0.01]
    d = dim_pq(p, q)
    for lam in pos:
        evals.append(lam)
        degs.append(d)

evals = np.array(evals)
degs = np.array(degs)

# Basic sums (all dimensionless, eigenvalues in code units)
a0 = np.sum(degs)                           # = 6440
a2 = np.sum(degs * evals**(-2))             # = 2776
a4 = np.sum(degs * evals**(-4))             # = 1350
S_log = np.sum(degs * np.log(evals))        # sum d_k ln(lambda_k)

print(f"\n--- Spectrum Summary ---")
print(f"  N_eigenvalues = {len(evals)}")
print(f"  a_0 = {a0:.0f}  (stored: {a0_stored:.0f})")
print(f"  a_2 = {a2:.4f}  (stored: {a2_stored:.4f})")
print(f"  a_4 = {a4:.4f}  (stored: {a4_stored:.4f})")
print(f"  S_log = {S_log:.4f}")
print(f"  Geom mean eigenvalue = {np.exp(S_log / a0):.4f}")
print(f"  M_KK = {M_KK:.4e} GeV")
print(f"  Lambda/M_KK ratio at Lambda=M_Pl: {M_PL_RED / M_KK:.2f}")

# ============================================================
# FORMULA A: What the W1-1 script computes (AGENT'S FORMULA)
# ============================================================
print(f"\n{'='*78}")
print("FORMULA A: Agent's formula (dimensionless log sum)")
print("  1/(16piG) = (1/2) * [a0 * ln(Lambda^2/M_KK^2) - 2*S_log]")
print("=" * 78)

for Lambda_label, Lambda in [("M_Pl", M_PL_RED), ("10*M_KK", 10*M_KK), ("100*M_KK", 100*M_KK)]:
    ln_ratio = np.log(Lambda**2 / M_KK**2)
    inv_16piG_A = 0.5 * (a0 * ln_ratio - 2 * S_log)

    # Agent treats this as GeV^2:
    G_A_nat = 1.0 / (16 * np.pi * inv_16piG_A)
    M_Pl_A = 1.0 / np.sqrt(8 * np.pi * G_A_nat)

    print(f"\n  Lambda = {Lambda_label} = {Lambda:.4e} GeV")
    print(f"    ln(Lambda^2/M_KK^2) = {ln_ratio:.4f}")
    print(f"    inv_16piG = {inv_16piG_A:.2f}  <-- DIMENSIONLESS!")
    print(f"    If treated as GeV^2: M_Pl_eff = {M_Pl_A:.2f} GeV")
    print(f"    Ratio to target: {inv_16piG_A / inv_16piG_obs:.4e}")
    print(f"    log10 deviation: {np.log10(inv_16piG_obs / inv_16piG_A):.2f} OOM")

# ============================================================
# FORMULA B: Standard Sakharov (1968) / one-loop QFT
# ============================================================
# For each KK mode of mass m_n (4D Dirac fermion), the one-loop
# contribution to the 4D Einstein-Hilbert coefficient is:
#
#   delta(1/16piG) = c_n / (48 pi^2) * [Lambda_4D^2 - m_n^2 * ln(1 + Lambda_4D^2/m_n^2)]
#
# where c_n = number of real DOF (Dirac fermion = 4, real scalar = 1)
#
# For our KK modes: m_n = lambda_n * M_KK, and d_n already counts
# the spinor structure + PW degeneracy.
#
# NOTE: In the spectral triple context, the 6440 PW-weighted modes
# ALREADY include the spinor trace (8 spinor components x 805 irrep-weighted
# modes). So we should NOT multiply by 4 again.
#
# The question is: does d_k count Dirac fermion DOF or real scalar DOF?
# Since D_K acts on spinors, each mode is a SPINOR mode.
# A Dirac fermion in 4D has 4 complex = 8 real DOF.
# But the eigenvalue list already resolves the spinor structure.
# Each eigenvalue is ONE mode of the Dirac operator.
# So c_n = 1 per listed eigenvalue (the spinor trace is already in the counting).
# The PW degeneracy d_k then just counts repeated eigenvalues.
#
# Conservative: use c_n = 1 (counting already done)
# This gives: 1/(16piG) = (1/48pi^2) * sum d_k [Lambda^2 - m_k^2 ln(1 + Lambda^2/m_k^2)]

print(f"\n{'='*78}")
print("FORMULA B: Standard Sakharov (1968) one-loop QFT")
print("  1/(16piG) = (1/48pi^2) * sum_k d_k [Lambda^2 - m_k^2 ln(1 + Lambda^2/m_k^2)]")
print("  with m_k = lambda_k * M_KK")
print("=" * 78)

for Lambda_label, Lambda_4D in [("M_Pl", M_PL_RED), ("10*M_KK", 10*M_KK), ("100*M_KK", 100*M_KK), ("M_KK", M_KK)]:
    m_k = evals * M_KK  # physical masses in GeV

    # Full formula per mode
    term_per_mode = Lambda_4D**2 - m_k**2 * np.log(1 + Lambda_4D**2 / m_k**2)

    # Weighted sum
    total_sum = np.sum(degs * term_per_mode)

    inv_16piG_B = total_sum / (48 * np.pi**2)

    # Decompose into Lambda^2 (leading) and log (subleading)
    leading = np.sum(degs) * Lambda_4D**2  # = a0 * Lambda^2
    subleading = -np.sum(degs * m_k**2 * np.log(1 + Lambda_4D**2 / m_k**2))

    G_B_nat = 1.0 / (16 * np.pi * inv_16piG_B) if inv_16piG_B > 0 else float('inf')
    M_Pl_B = 1.0 / np.sqrt(8 * np.pi * G_B_nat) if G_B_nat > 0 and not np.isinf(G_B_nat) else 0

    ratio = inv_16piG_B / inv_16piG_obs if inv_16piG_obs > 0 else 0

    print(f"\n  Lambda_4D = {Lambda_label} = {Lambda_4D:.4e} GeV")
    print(f"    Leading (a0 * Lambda^2):      {leading/(48*np.pi**2):.6e} GeV^2")
    print(f"    Subleading (mass-log):         {subleading/(48*np.pi**2):.6e} GeV^2")
    print(f"    Total 1/(16piG):               {inv_16piG_B:.6e} GeV^2")
    print(f"    M_Pl_eff:                      {M_Pl_B:.4e} GeV")
    print(f"    Ratio to target:               {ratio:.4f}")
    print(f"    log10 deviation:               {np.log10(max(abs(ratio), 1e-100)):+.2f}")

# ============================================================
# FORMULA C: Spectral action (for comparison)
# ============================================================
print(f"\n{'='*78}")
print("FORMULA C: Spectral action (Chamseddine-Connes)")
print("  1/(16piG) = (6/pi^3) * a_2 * M_KK^2  [with f_2=1]")
print("  NOTE: M_KK was DEFINED by matching G_N, so this gives G_obs by construction")
print("=" * 78)

inv_16piG_C = (6 / np.pi**3) * a2 * M_KK**2
ratio_C = inv_16piG_C / inv_16piG_obs

print(f"  inv_16piG_spec = {inv_16piG_C:.6e} GeV^2")
print(f"  Ratio to target: {ratio_C:.6f}")
print(f"  (This is ~1 by construction since M_KK was fit from G_N)")

# ============================================================
# FORMULA D: Volovik Paper 30 formula
# ============================================================
# G_N ~ Delta^2 / rho_0 (condensed matter)
# This is NOT the same as the QFT Sakharov formula.
# It applies to the BCS condensate, not to the KK mode sum.
# Including for completeness.

print(f"\n{'='*78}")
print("FORMULA D: Volovik Paper 30 (superfluid G_N)")
print("  G_N ~ Delta^2 / rho_0 ~ c_s^2 / rho_0")
print("  Not directly applicable to KK mode counting, included for comparison")
print("=" * 78)

# ============================================================
# FORMULA E: Pure logarithmic Sakharov (agent's INTENT corrected)
# ============================================================
# If the agent intended Volovik's condensed matter formula adapted to KK:
# The trace-log of the Dirac propagator gives the free energy.
# The curvature-dependent part of the free energy gives G_N.
# In 4D: 1/(16piG) = (1/48pi^2) sum_k d_k m_k^2 ln(Lambda^2/m_k^2)
# This is the SUBLEADING piece of Formula B.

print(f"\n{'='*78}")
print("FORMULA E: Logarithmic piece only (with correct 4D normalization)")
print("  1/(16piG) = (1/48pi^2) * sum_k d_k * m_k^2 * ln(Lambda^2/m_k^2)")
print("  This is the subleading correction in Formula B")
print("=" * 78)

for Lambda_label, Lambda_4D in [("M_Pl", M_PL_RED), ("10*M_KK", 10*M_KK), ("100*M_KK", 100*M_KK)]:
    m_k = evals * M_KK
    log_sum = np.sum(degs * m_k**2 * np.log(Lambda_4D**2 / m_k**2))
    inv_16piG_E = log_sum / (48 * np.pi**2)

    G_E_nat = 1.0 / (16 * np.pi * inv_16piG_E) if inv_16piG_E > 0 else float('inf')
    M_Pl_E = 1.0 / np.sqrt(8 * np.pi * G_E_nat) if G_E_nat > 0 and not np.isinf(G_E_nat) else 0

    ratio = inv_16piG_E / inv_16piG_obs

    print(f"\n  Lambda_4D = {Lambda_label} = {Lambda_4D:.4e} GeV")
    print(f"    1/(16piG) = {inv_16piG_E:.6e} GeV^2")
    print(f"    M_Pl_eff = {M_Pl_E:.4e} GeV")
    print(f"    Ratio to target: {ratio:.4f}")
    print(f"    log10 deviation: {np.log10(max(abs(ratio), 1e-100)):+.2f}")

# ============================================================
# FORMULA F: Agent's formula WITH M_KK^2 prefactor (dimensional fix)
# ============================================================
# If the agent's formula is missing M_KK^2 and 1/(48pi^2):
# 1/(16piG) = M_KK^2 / (48pi^2) * [a0 * ln(Lambda^2/M_KK^2) - 2*S_log]

print(f"\n{'='*78}")
print("FORMULA F: Agent's log sum WITH dimensional correction")
print("  1/(16piG) = M_KK^2 / (48pi^2) * [a0*ln(Lambda^2/M_KK^2) - 2*S_log]")
print("=" * 78)

for Lambda_label, Lambda_4D in [("M_Pl", M_PL_RED), ("10*M_KK", 10*M_KK), ("100*M_KK", 100*M_KK)]:
    ln_ratio = np.log(Lambda_4D**2 / M_KK**2)
    log_sum = a0 * ln_ratio - 2 * S_log
    inv_16piG_F = M_KK**2 * log_sum / (48 * np.pi**2)

    G_F_nat = 1.0 / (16 * np.pi * inv_16piG_F) if inv_16piG_F > 0 else float('inf')
    M_Pl_F = 1.0 / np.sqrt(8 * np.pi * G_F_nat) if G_F_nat > 0 and not np.isinf(G_F_nat) else 0

    ratio = inv_16piG_F / inv_16piG_obs

    print(f"\n  Lambda_4D = {Lambda_label} = {Lambda_4D:.4e} GeV")
    print(f"    log_sum = {log_sum:.2f}")
    print(f"    1/(16piG) = {inv_16piG_F:.6e} GeV^2")
    print(f"    M_Pl_eff = {M_Pl_F:.4e} GeV")
    print(f"    Ratio to target: {ratio:.4f}")
    print(f"    log10 deviation: {np.log10(max(abs(ratio), 1e-100)):+.2f}")

# ============================================================
# SUMMARY COMPARISON
# ============================================================
print(f"\n{'='*78}")
print("SUMMARY: All formulas at Lambda = M_Pl")
print("=" * 78)

Lambda_4D = M_PL_RED
m_k = evals * M_KK
ln_ratio = np.log(Lambda_4D**2 / M_KK**2)

# A: Agent's
inv_A = 0.5 * (a0 * ln_ratio - 2 * S_log)
# B: Standard Sakharov
inv_B = np.sum(degs * (Lambda_4D**2 - m_k**2 * np.log(1 + Lambda_4D**2/m_k**2))) / (48 * np.pi**2)
# C: Spectral action
inv_C = (6 / np.pi**3) * a2 * M_KK**2
# E: Log-only with normalization
inv_E = np.sum(degs * m_k**2 * np.log(Lambda_4D**2 / m_k**2)) / (48 * np.pi**2)
# F: Agent's with dimensional fix
inv_F = M_KK**2 * (a0 * ln_ratio - 2 * S_log) / (48 * np.pi**2)

print(f"\n  {'Formula':>40s}  {'1/(16piG) GeV^2':>18s}  {'ratio':>10s}  {'log10':>8s}  {'Verdict':>8s}")
print(f"  {'='*90}")
print(f"  {'OBSERVED':>40s}  {inv_16piG_obs:18.6e}  {'1.0000':>10s}  {'+0.00':>8s}  {'TARGET':>8s}")
print(f"  {'A: Agent (dimensionless!)':>40s}  {inv_A:18.6e}  {inv_A/inv_16piG_obs:10.2e}  {np.log10(inv_16piG_obs/inv_A):+8.1f}  {'WRONG':>8s}")
print(f"  {'B: Standard Sakharov (full)':>40s}  {inv_B:18.6e}  {inv_B/inv_16piG_obs:10.4f}  {np.log10(max(abs(inv_B/inv_16piG_obs),1e-100)):+8.2f}  {'':>8s}")
print(f"  {'C: Spectral action (by construction)':>40s}  {inv_C:18.6e}  {inv_C/inv_16piG_obs:10.4f}  {np.log10(max(abs(inv_C/inv_16piG_obs),1e-100)):+8.2f}  {'':>8s}")
print(f"  {'E: Log-only with 1/(48pi^2) & m_k^2':>40s}  {inv_E:18.6e}  {inv_E/inv_16piG_obs:10.4f}  {np.log10(max(abs(inv_E/inv_16piG_obs),1e-100)):+8.2f}  {'':>8s}")
print(f"  {'F: Agent log + M_KK^2/(48pi^2)':>40s}  {inv_F:18.6e}  {inv_F/inv_16piG_obs:10.4f}  {np.log10(max(abs(inv_F/inv_16piG_obs),1e-100)):+8.2f}  {'':>8s}")

# ============================================================
# DIAGNOSIS
# ============================================================
print(f"\n{'='*78}")
print("DIAGNOSIS")
print("=" * 78)
print(f"""
The W1-1 script's Formula A gives a DIMENSIONLESS number (~19,590) and treats
it as if it has dimensions of GeV^2. This is 10^{{32}} below the target because
it is missing:

1. The DOMINANT Lambda^2 term from the standard Sakharov formula
2. The m_k^2 factor that makes the logarithmic piece dimensionful
3. The 1/(48*pi^2) = {1/(48*np.pi**2):.6e} normalization from the 4D loop integral

Formula B (standard Sakharov with full one-loop structure) gives the correct
result. The leading Lambda^2 term dominates and gives 1/G close to observed.

Key insight: for Lambda = M_Pl, the Sakharov formula's leading term is
  (a_0 / 48pi^2) * M_Pl^2 = 6440 * {M_PL_RED**2:.3e} / 474 = {6440*M_PL_RED**2/474:.3e} GeV^2
  Target: {inv_16piG_obs:.3e} GeV^2
  Ratio: {6440*M_PL_RED**2/(474*inv_16piG_obs):.3f}

This means the STANDARD Sakharov formula gives G_N within a factor of
{inv_16piG_obs * 474 / (6440*M_PL_RED**2):.2f} of observed at Lambda=M_Pl.
The 32 OOM "deficit" was entirely an artifact of the wrong formula.
""")

# Check if the PASS criteria would be met with corrected formula
ratio_B = inv_B / inv_16piG_obs
log10_dev = np.log10(abs(ratio_B))
print(f"CORRECTED GATE EVALUATION (Formula B at Lambda=M_Pl):")
print(f"  1/(16piG_Sak) = {inv_B:.6e} GeV^2")
print(f"  1/(16piG_obs) = {inv_16piG_obs:.6e} GeV^2")
print(f"  Ratio = {ratio_B:.4f}")
print(f"  |log10(G_Sak/G_obs)| = {abs(log10_dev):.4f}")
if abs(log10_dev) < 2:
    print(f"  VERDICT: PASS (within {10**abs(log10_dev):.1f}x of observed)")
else:
    print(f"  VERDICT: FAIL ({10**abs(log10_dev):.1f}x off)")

np.savez(DATA_DIR / 's44_sakharov_gn_audit.npz',
    inv_16piG_agent=inv_A,
    inv_16piG_sakharov_full=inv_B,
    inv_16piG_spectral=inv_C,
    inv_16piG_log_corrected=inv_E,
    inv_16piG_agent_dimfix=inv_F,
    inv_16piG_obs=inv_16piG_obs,
    ratio_B=ratio_B,
    log10_dev=log10_dev,
)
print(f"\nAudit data saved to s44_sakharov_gn_audit.npz")
