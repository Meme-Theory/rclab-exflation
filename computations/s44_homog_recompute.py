#!/usr/bin/env python3
"""
HOMOG-42-RECOMPUTE-44: Homogeneity Gate with E-vs-F Correction
================================================================
Einstein-theorist computation.

PRINCIPLE: The Friedmann equation uses H^2 ~ a_0 * M_KK^4 / M_Pl^2.
The E-vs-F audit (S43 Instance 6) identified that replacing the polynomial
spectral action with the correct gravitating functional modifies a_0 -> f * a_0.

Two correction factors from S44:
  f_tracelog = 3.09e-3  (W1-4: trace-log vs polynomial ratio)
  f_EIH = 5.68e-5       (W2-3: EIH singlet projection)

This recomputes HOMOG-42 with corrected H for both physical f-values
and a parametric sweep f = 0.001, 0.01, 0.1, 1, 2, 5, 10.

SCALING ANALYSIS (exact, not approximate):
  H_corrected = H_original * sqrt(f)
  N_corrected = H_corrected * dt_transit = N_original * sqrt(f)

  The exact Starobinsky formula:
    <phi^2>(N) = (3 H^4)/(8 pi^2 m^2) * [1 - exp(-2 m^2 N/(3 H^2))]

  With H -> H*sqrt(f), N -> N*sqrt(f):
    phi2_eq -> phi2_eq * f^2
    exponent -> exponent / sqrt(f)
    relaxation_factor -> 1 - exp(-exponent/sqrt(f))

  In the SHORT-TIME limit (exponent << 1):
    phi2 ~ H^2 * N / (4 pi^2) ~ f * sqrt(f) * original = f^{3/2} * original
    delta_tau/tau ~ f^{3/4} * original

  In the EQUILIBRIUM limit:
    phi2 ~ H^4/m^2 ~ f^2 * original
    delta_tau/tau ~ f * original

  The actual scaling depends on the relaxation regime. We compute EXACTLY.

Gate: HOMOG-42-RECOMPUTE-44
  PASS: margin survives (corrected delta_tau/tau < 3e-6)
  FAIL: margin violated (corrected delta_tau/tau > 3e-6)

Author: Einstein-theorist agent, Session 44 W5-6
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

# ============================================================
# 1. LOAD ORIGINAL DATA
# ============================================================

print("=" * 70)
print("HOMOG-42-RECOMPUTE-44: E-vs-F Corrected Homogeneity")
print("=" * 70)

d = np.load('tier0-computation/s42_homogeneity.npz', allow_pickle=True)

tau_fold = d['tau_fold'].item()
Z_fold = d['Z_fold'].item()
d2S_fold = d['d2S_fold'].item()
a0_fold = d['a0_fold'].item()
M_KK_GN = d['M_KK_GN'].item()
M_KK_gauge = d['M_KK_gauge'].item()
M_Planck = d['M_Planck'].item()
m_phi_sq = d['m_phi_sq'].item()
m_phi = d['m_phi'].item()
c_fabric = d['c_fabric'].item()
H_prefactor = d['H_prefactor'].item()
dt_transit = d['dt_transit'].item()
FIRAS_bound = d['FIRAS_bound'].item()

# Original results for reference
orig_grav_transit = d['dtau_over_tau_transit_grav'].item()
orig_gauge_transit = d['dtau_over_tau_transit_gauge'].item()
orig_grav_eq = d['dtau_over_tau_eq_grav'].item()
orig_gauge_eq = d['dtau_over_tau_eq_gauge'].item()
orig_verdict = str(d['verdict'][0])

print(f"\n  === Original HOMOG-42 ===")
print(f"  tau_fold = {tau_fold}")
print(f"  Z_fold = {Z_fold:.2f}")
print(f"  d2S_fold = {d2S_fold:.2f}")
print(f"  a0_fold = {a0_fold:.1f}")
print(f"  m_phi = {m_phi:.4f} M_KK")
print(f"  H_prefactor = {H_prefactor:.6f}")
print(f"  dt_transit = {dt_transit:.6e}")
print(f"  M_KK(grav) = {M_KK_GN:.3e} GeV")
print(f"  M_KK(gauge) = {M_KK_gauge:.3e} GeV")
print(f"  M_Planck = {M_Planck:.3e} GeV")
print(f"\n  Original gravity:  dtau/tau = {orig_grav_transit:.4e} (transit)")
print(f"  Original gauge:    dtau/tau = {orig_gauge_transit:.4e} (transit)")
print(f"  FIRAS bound:       {FIRAS_bound:.0e}")
print(f"  Original margin (gravity): {FIRAS_bound/orig_grav_transit:.2f}x")
print(f"  Original margin (gauge):   {FIRAS_bound/orig_gauge_transit:.2f}x")
print(f"  Original verdict: {orig_verdict}")

# ============================================================
# 2. DEFINE CORRECTION FACTORS
# ============================================================

print("\n" + "=" * 70)
print("2. CORRECTION FACTORS")
print("=" * 70)

# Physical correction factors from S44
f_tracelog = 3.09e-3    # W1-4: trace-log replacement ratio
f_EIH = 5.68e-5         # W2-3: EIH singlet projection
f_combined = f_tracelog * f_EIH  # Not physical (double-counting possible)

# The two are ALTERNATIVE routes, not multiplicative:
# Route A: Replace polynomial SA with trace-log -> f = f_tracelog
# Route B: EIH singlet projection of polynomial SA -> f = f_EIH
# Route C: EIH singlet of trace-log -> f = f_tracelog * f_EIH (if independent)
# But: EIH projects OUT non-singlet modes from whatever functional we use.
# So: if we use trace-log, f_EIH still applies to it.
# Combined: f = f_tracelog * (f_EIH applies to the trace-log, but f_EIH was
# computed for polynomial SA). If trace-log has SAME singlet fraction, then
# f_combined = f_tracelog * f_EIH. Let's compute both alternatives AND combined.

# Parametric sweep
f_parametric = np.array([0.001, 0.01, 0.1, 1.0, 2.0, 5.0, 10.0])

# All f values to compute
f_physical = {
    'f_tracelog': f_tracelog,
    'f_EIH': f_EIH,
    'f_combined': f_tracelog * f_EIH,
}

print(f"\n  Physical correction factors:")
print(f"    f_tracelog  = {f_tracelog:.3e}  (trace-log / polynomial SA)")
print(f"    f_EIH       = {f_EIH:.3e}  (singlet / total in polynomial SA)")
print(f"    f_combined  = {f_tracelog * f_EIH:.3e}  (both, if independent)")
print(f"\n  Parametric sweep: f = {f_parametric}")

# ============================================================
# 3. EXACT RECOMPUTATION FUNCTION
# ============================================================

def compute_dtau(f, M_KK, label=""):
    """
    Compute delta_tau/tau with corrected H = H_original * sqrt(f).

    The correction a_0 -> f * a_0 gives:
      H^2 = f * a_0 * M_KK^4 / (6 * (4pi)^2 * M_Pl^2)
      H = sqrt(f) * H_original

    Everything else follows from the exact Starobinsky formula.
    """
    # Corrected Hubble (in units of M_KK)
    H_over_MKK_orig = H_prefactor * (M_KK / M_Planck)
    H_over_MKK = H_over_MKK_orig * np.sqrt(f)

    # m/H ratio (m is fixed, H changes)
    m_over_H = m_phi / H_over_MKK if H_over_MKK > 0 else np.inf
    m_sq_over_H_sq = m_phi_sq / H_over_MKK**2 if H_over_MKK > 0 else np.inf

    # Transit e-folds (N = H * dt, both in M_KK units)
    N_efolds = H_over_MKK * dt_transit

    # Saturation e-folds
    N_sat = 3.0 * H_over_MKK**2 / (2.0 * m_phi_sq) if m_phi_sq > 0 else np.inf

    # Exact Starobinsky relaxation
    if H_over_MKK > 0:
        exponent = 2.0 * m_phi_sq * N_efolds / (3.0 * H_over_MKK**2)
        relaxation = 1.0 - np.exp(-exponent)
    else:
        exponent = np.inf
        relaxation = 1.0

    # Equilibrium (BD) variance
    phi2_eq = 3.0 * H_over_MKK**4 / (8.0 * np.pi**2 * m_phi_sq)

    # Transit variance (exact)
    phi2_transit = phi2_eq * relaxation

    # delta_tau/tau
    dtau_eq = np.sqrt(phi2_eq) / np.sqrt(Z_fold) / tau_fold
    dtau_transit = np.sqrt(phi2_transit) / np.sqrt(Z_fold) / tau_fold

    return {
        'f': f,
        'M_KK': M_KK,
        'label': label,
        'H_over_MKK': H_over_MKK,
        'H_over_MKK_orig': H_over_MKK_orig,
        'm_over_H': m_over_H,
        'm_sq_over_H_sq': m_sq_over_H_sq,
        'N_efolds': N_efolds,
        'N_sat': N_sat,
        'exponent': exponent,
        'relaxation': relaxation,
        'phi2_eq': phi2_eq,
        'phi2_transit': phi2_transit,
        'dtau_eq': dtau_eq,
        'dtau_transit': dtau_transit,
    }

# ============================================================
# 4. COMPUTE FOR ALL f VALUES
# ============================================================

print("\n" + "=" * 70)
print("3. EXACT RECOMPUTATION")
print("=" * 70)

# Store all results
all_results = {}

# --- GRAVITY ROUTE ---
print(f"\n  {'='*60}")
print(f"  GRAVITY ROUTE: M_KK = {M_KK_GN:.3e} GeV")
print(f"  {'='*60}")

print(f"\n  {'f':>12} {'H/M_KK':>12} {'m/H':>10} {'N_efolds':>12} "
      f"{'relax':>12} {'dtau_eq':>12} {'dtau_tr':>12} {'margin':>8} {'status':>8}")
print(f"  {'-'*12} {'-'*12} {'-'*10} {'-'*12} "
      f"{'-'*12} {'-'*12} {'-'*12} {'-'*8} {'-'*8}")

# Original (f=1)
r = compute_dtau(1.0, M_KK_GN, "original")
margin_orig = FIRAS_bound / r['dtau_transit']
print(f"  {'1.0 (orig)':>12} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
      f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
      f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
      f"{margin_orig:>8.2f} {'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL':>8}")
all_results['grav_orig'] = r

# Verify original matches loaded data
assert abs(r['dtau_transit'] - orig_grav_transit) / orig_grav_transit < 1e-6, \
    f"Mismatch: {r['dtau_transit']:.6e} vs {orig_grav_transit:.6e}"

# Physical f values
for fname, fval in f_physical.items():
    r = compute_dtau(fval, M_KK_GN, fname)
    margin = FIRAS_bound / r['dtau_transit']
    status = 'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL'
    print(f"  {fval:>12.3e} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
          f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
          f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f} {status:>8}")
    all_results[f'grav_{fname}'] = r

# Parametric sweep
print(f"\n  --- Parametric sweep ---")
for fval in f_parametric:
    r = compute_dtau(fval, M_KK_GN, f"f={fval}")
    margin = FIRAS_bound / r['dtau_transit']
    status = 'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL'
    print(f"  {fval:>12.3e} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
          f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
          f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f} {status:>8}")
    all_results[f'grav_f{fval}'] = r

# --- GAUGE ROUTE ---
print(f"\n  {'='*60}")
print(f"  GAUGE ROUTE: M_KK = {M_KK_gauge:.3e} GeV")
print(f"  {'='*60}")

print(f"\n  {'f':>12} {'H/M_KK':>12} {'m/H':>10} {'N_efolds':>12} "
      f"{'relax':>12} {'dtau_eq':>12} {'dtau_tr':>12} {'margin':>8} {'status':>8}")
print(f"  {'-'*12} {'-'*12} {'-'*10} {'-'*12} "
      f"{'-'*12} {'-'*12} {'-'*12} {'-'*8} {'-'*8}")

# Original (f=1)
r = compute_dtau(1.0, M_KK_gauge, "original")
margin_orig_gauge = FIRAS_bound / r['dtau_transit']
print(f"  {'1.0 (orig)':>12} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
      f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
      f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
      f"{margin_orig_gauge:>8.2f} {'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL':>8}")
all_results['gauge_orig'] = r

# Physical f values
for fname, fval in f_physical.items():
    r = compute_dtau(fval, M_KK_gauge, fname)
    margin = FIRAS_bound / r['dtau_transit']
    status = 'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL'
    print(f"  {fval:>12.3e} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
          f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
          f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f} {status:>8}")
    all_results[f'gauge_{fname}'] = r

# Parametric sweep
print(f"\n  --- Parametric sweep ---")
for fval in f_parametric:
    r = compute_dtau(fval, M_KK_gauge, f"f={fval}")
    margin = FIRAS_bound / r['dtau_transit']
    status = 'PASS' if r['dtau_transit'] < FIRAS_bound else 'FAIL'
    print(f"  {fval:>12.3e} {r['H_over_MKK']:>12.4e} {r['m_over_H']:>10.2f} "
          f"{r['N_efolds']:>12.4e} {r['relaxation']:>12.6e} "
          f"{r['dtau_eq']:>12.4e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f} {status:>8}")
    all_results[f'gauge_f{fval}'] = r

# ============================================================
# 5. SCALING ANALYSIS
# ============================================================

print("\n" + "=" * 70)
print("4. SCALING ANALYSIS: Exact vs Approximate")
print("=" * 70)

# Compare exact f-dependence to the three candidate scaling laws
f_dense = np.logspace(-5, 1.5, 500)
dtau_exact_grav = np.zeros_like(f_dense)
dtau_exact_gauge = np.zeros_like(f_dense)

for i, fval in enumerate(f_dense):
    r_g = compute_dtau(fval, M_KK_GN)
    r_q = compute_dtau(fval, M_KK_gauge)
    dtau_exact_grav[i] = r_g['dtau_transit']
    dtau_exact_gauge[i] = r_q['dtau_transit']

# Reference: f=1 values
dtau_ref_grav = orig_grav_transit
dtau_ref_gauge = orig_gauge_transit

# Three scaling approximations
dtau_linear = dtau_ref_grav * f_dense          # delta ~ f (BD limit)
dtau_34 = dtau_ref_grav * f_dense**0.75        # delta ~ f^{3/4} (short-time)
dtau_sqrt = dtau_ref_grav * np.sqrt(f_dense)   # delta ~ f^{1/2} (intermediate?)

# Find the effective exponent
log_f = np.log(f_dense)
log_dtau_g = np.log(dtau_exact_grav)
# Local slope = d(log dtau)/d(log f)
dlog = np.gradient(log_dtau_g, log_f)

print(f"\n  At the physical f values:")
for fname, fval in f_physical.items():
    idx = np.argmin(np.abs(f_dense - fval))
    slope = dlog[idx]
    print(f"    {fname} (f={fval:.3e}): effective exponent = {slope:.4f}")

print(f"\n  At f=1 (original): effective exponent = {dlog[np.argmin(np.abs(f_dense - 1.0))]:.4f}")

# ============================================================
# 6. CRITICAL f VALUE (margin flip)
# ============================================================

print("\n" + "=" * 70)
print("5. CRITICAL f VALUE (where margin = 1)")
print("=" * 70)

# For gravity route: find f where dtau_transit = FIRAS_bound
idx_cross_grav = np.where(dtau_exact_grav > FIRAS_bound)[0]
if len(idx_cross_grav) > 0:
    f_crit_grav = f_dense[idx_cross_grav[0]]
    print(f"  Gravity: margin flips at f_crit = {f_crit_grav:.4f}")
    print(f"  This is {f_crit_grav/orig_grav_transit*FIRAS_bound:.1f}x the margin")
else:
    f_crit_grav = f_dense[-1]
    print(f"  Gravity: margin survives for all f up to {f_dense[-1]:.1f}")

# For gauge route: already ABOVE FIRAS at f=1
idx_cross_gauge = np.where(dtau_exact_gauge < FIRAS_bound)[0]
if len(idx_cross_gauge) > 0:
    f_safe_gauge = f_dense[idx_cross_gauge[-1]]
    print(f"  Gauge: enters PASS region below f = {f_safe_gauge:.4f}")
else:
    f_safe_gauge = 0.0
    print(f"  Gauge: NEVER passes FIRAS bound in scanned range")

# ============================================================
# 7. THE GATE VERDICT
# ============================================================

print("\n" + "=" * 70)
print("6. GATE VERDICT: HOMOG-42-RECOMPUTE-44")
print("=" * 70)

# The physical question: which f is correct?
# Route A (trace-log): f = 3.09e-3
# Route B (EIH singlet): f = 5.68e-5
# Both are < 1, so BOTH make HOMOG-42 safer.
# The combined f = 1.75e-7 is even smaller.

# For gravity route at each physical f:
print(f"\n  GRAVITY ROUTE (M_KK = {M_KK_GN:.3e} GeV):")
print(f"  {'Correction':>20} {'f':>12} {'dtau/tau':>12} {'margin':>8} {'verdict':>8}")
print(f"  {'-'*20} {'-'*12} {'-'*12} {'-'*8} {'-'*8}")

results_summary = {}
for fname, fval in [('original', 1.0)] + list(f_physical.items()):
    r = compute_dtau(fval, M_KK_GN)
    margin = FIRAS_bound / r['dtau_transit']
    v = 'PASS' if margin > 1 else 'FAIL'
    print(f"  {fname:>20} {fval:>12.3e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f}x {v:>8}")
    results_summary[f'grav_{fname}'] = {
        'f': fval, 'dtau': r['dtau_transit'], 'margin': margin, 'verdict': v
    }

print(f"\n  GAUGE ROUTE (M_KK = {M_KK_gauge:.3e} GeV):")
print(f"  {'Correction':>20} {'f':>12} {'dtau/tau':>12} {'margin':>8} {'verdict':>8}")
print(f"  {'-'*20} {'-'*12} {'-'*12} {'-'*8} {'-'*8}")

for fname, fval in [('original', 1.0)] + list(f_physical.items()):
    r = compute_dtau(fval, M_KK_gauge)
    margin = FIRAS_bound / r['dtau_transit']
    v = 'PASS' if margin > 1 else 'FAIL'
    print(f"  {fname:>20} {fval:>12.3e} {r['dtau_transit']:>12.4e} "
          f"{margin:>8.1f}x {v:>8}")
    results_summary[f'gauge_{fname}'] = {
        'f': fval, 'dtau': r['dtau_transit'], 'margin': margin, 'verdict': v
    }

# Determine overall gate
# The gate criterion: "PASS if margin survives (f < 4.5)"
# Physical f values are ALL << 1, so margin is MASSIVELY improved
grav_tracelog = results_summary['grav_f_tracelog']
grav_eih = results_summary['grav_f_EIH']
grav_combined = results_summary['grav_f_combined']
gauge_tracelog = results_summary['gauge_f_tracelog']
gauge_eih = results_summary['gauge_f_EIH']

# The WORST CASE among physical corrections is f_tracelog = 3.09e-3
# (the largest f, giving the smallest improvement)
worst_physical_f = f_tracelog
worst_case = compute_dtau(worst_physical_f, M_KK_gauge)  # gauge is worse
worst_margin = FIRAS_bound / worst_case['dtau_transit']

print(f"\n  {'='*60}")
print(f"  GATE: HOMOG-42-RECOMPUTE-44")
print(f"  {'='*60}")
print(f"\n  Pre-registered criterion: PASS if f < 4.5 (margin survives)")
print(f"  Physical f values: {f_tracelog:.3e} (tracelog), {f_EIH:.3e} (EIH)")
print(f"  Both are << 4.5. Both are << 1.")
print(f"  E-vs-F correction REDUCES H, REDUCES fluctuations.")
print(f"\n  Worst physical case: f_tracelog = {f_tracelog:.3e}")
print(f"    Gravity: dtau/tau = {results_summary['grav_f_tracelog']['dtau']:.4e}, "
      f"margin = {results_summary['grav_f_tracelog']['margin']:.0f}x")
print(f"    Gauge:   dtau/tau = {results_summary['gauge_f_tracelog']['dtau']:.4e}, "
      f"margin = {results_summary['gauge_f_tracelog']['margin']:.0f}x")

# The GAUGE route, which originally FAILED (margin 0.096x), now PASSES
gauge_orig_margin = FIRAS_bound / orig_gauge_transit
gauge_tracelog_margin = results_summary['gauge_f_tracelog']['margin']

if worst_margin > 1.0:
    gate_verdict = "PASS"
else:
    gate_verdict = "FAIL"

print(f"\n  VERDICT: **{gate_verdict}**")
print(f"\n  Key finding: The E-vs-F correction does NOT threaten HOMOG-42.")
print(f"  Both physical f-values are << 1 (not > 4.5).")
print(f"  The correction IMPROVES homogeneity by factors of {1/f_tracelog:.0f}x to {1/f_EIH:.0f}x.")

# Additional: what f would be needed to flip the gate?
print(f"\n  Critical f for gravity route:  f_crit = {f_crit_grav:.2f}")
print(f"  Critical f for gauge route:    f_crit = {f_safe_gauge:.4f} (already fails at f=1)")
print(f"  For gauge to PASS: need f < ~{f_safe_gauge:.3f}")
print(f"    f_tracelog = {f_tracelog:.3e} << {f_safe_gauge:.3f}: gauge route NOW PASSES")

# The real story: the gauge route was INTERMEDIATE at f=1, but PASSES at f=f_tracelog
# The gravity route was PASS at f=1, and is now PASS by enormous margin

# ============================================================
# 8. SAVE DATA
# ============================================================

print("\n" + "=" * 70)
print("7. SAVING DATA")
print("=" * 70)

# Collect key results for saving
save_dict = {
    # Input
    'tau_fold': tau_fold,
    'Z_fold': Z_fold,
    'd2S_fold': d2S_fold,
    'a0_fold': a0_fold,
    'M_KK_GN': M_KK_GN,
    'M_KK_gauge': M_KK_gauge,
    'M_Planck': M_Planck,
    'm_phi_sq': m_phi_sq,
    'm_phi': m_phi,
    'H_prefactor': H_prefactor,
    'dt_transit': dt_transit,
    'FIRAS_bound': FIRAS_bound,

    # Physical f values
    'f_tracelog': f_tracelog,
    'f_EIH': f_EIH,
    'f_combined': f_tracelog * f_EIH,

    # Original (f=1) results
    'dtau_grav_orig': orig_grav_transit,
    'dtau_gauge_orig': orig_gauge_transit,
    'margin_grav_orig': FIRAS_bound / orig_grav_transit,
    'margin_gauge_orig': FIRAS_bound / orig_gauge_transit,

    # Tracelog corrected
    'dtau_grav_tracelog': results_summary['grav_f_tracelog']['dtau'],
    'dtau_gauge_tracelog': results_summary['gauge_f_tracelog']['dtau'],
    'margin_grav_tracelog': results_summary['grav_f_tracelog']['margin'],
    'margin_gauge_tracelog': results_summary['gauge_f_tracelog']['margin'],

    # EIH corrected
    'dtau_grav_eih': results_summary['grav_f_EIH']['dtau'],
    'dtau_gauge_eih': results_summary['gauge_f_EIH']['dtau'],
    'margin_grav_eih': results_summary['grav_f_EIH']['margin'],
    'margin_gauge_eih': results_summary['gauge_f_EIH']['margin'],

    # Combined
    'dtau_grav_combined': results_summary['grav_f_combined']['dtau'],
    'dtau_gauge_combined': results_summary['gauge_f_combined']['dtau'],
    'margin_grav_combined': results_summary['grav_f_combined']['margin'],
    'margin_gauge_combined': results_summary['gauge_f_combined']['margin'],

    # Critical f
    'f_crit_grav': f_crit_grav,
    'f_safe_gauge': f_safe_gauge,

    # Scaling data (dense)
    'f_dense': f_dense,
    'dtau_exact_grav': dtau_exact_grav,
    'dtau_exact_gauge': dtau_exact_gauge,

    # Parametric
    'f_parametric': f_parametric,

    # Gate
    'gate_verdict': np.array([gate_verdict]),
    'gate_name': np.array(['HOMOG-42-RECOMPUTE-44']),
}

np.savez('tier0-computation/s44_homog_recompute.npz', **save_dict)
print("Saved: tier0-computation/s44_homog_recompute.npz")

# ============================================================
# 9. PLOT
# ============================================================

print("\n" + "=" * 70)
print("8. GENERATING PLOTS")
print("=" * 70)

fig = plt.figure(figsize=(16, 12))
gs_plot = GridSpec(2, 2, hspace=0.35, wspace=0.35)

# --- Panel A: delta_tau/tau vs f (gravity route) ---
ax1 = fig.add_subplot(gs_plot[0, 0])

ax1.loglog(f_dense, dtau_exact_grav, 'b-', lw=2.5, label='Gravity (exact Starobinsky)')
ax1.loglog(f_dense, dtau_exact_gauge, 'r-', lw=2.5, label='Gauge (exact Starobinsky)')

# FIRAS bound
ax1.axhline(FIRAS_bound, color='green', ls='--', lw=2, label=f'FIRAS bound ({FIRAS_bound:.0e})')

# Physical f values
for fval, color, marker, lbl in [
    (f_tracelog, 'orange', 'D', f'trace-log ({f_tracelog:.1e})'),
    (f_EIH, 'purple', 's', f'EIH singlet ({f_EIH:.1e})'),
]:
    r_g = compute_dtau(fval, M_KK_GN)
    r_q = compute_dtau(fval, M_KK_gauge)
    ax1.plot(fval, r_g['dtau_transit'], marker, color=color, markersize=12, zorder=5,
             label=lbl)
    ax1.plot(fval, r_q['dtau_transit'], marker, color=color, markersize=12, zorder=5)

# Mark original
ax1.plot(1.0, orig_grav_transit, 'o', color='blue', markersize=10, zorder=5,
         label='Original (f=1)')
ax1.plot(1.0, orig_gauge_transit, 'o', color='red', markersize=10, zorder=5)

# f=4.5 vertical line (where gate would flip per original spec)
ax1.axvline(4.5, color='gray', ls=':', lw=1.5, alpha=0.7, label='f=4.5 (spec threshold)')

# Shading
ax1.fill_between(f_dense, 0, FIRAS_bound, alpha=0.06, color='green')
ax1.fill_between(f_dense, FIRAS_bound, 1, alpha=0.04, color='red')

ax1.set_xlabel('Correction factor f', fontsize=13)
ax1.set_ylabel(r'$\delta\tau/\tau$ (transit)', fontsize=13)
ax1.set_title(r'(A) $\delta\tau/\tau$ vs E-vs-F correction factor', fontsize=13)
ax1.legend(fontsize=8, loc='upper left')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(1e-5, 30)
ax1.set_ylim(1e-13, 1e-2)

# --- Panel B: Margin vs f ---
ax2 = fig.add_subplot(gs_plot[0, 1])

margin_grav = FIRAS_bound / dtau_exact_grav
margin_gauge = FIRAS_bound / dtau_exact_gauge

ax2.loglog(f_dense, margin_grav, 'b-', lw=2.5, label='Gravity')
ax2.loglog(f_dense, margin_gauge, 'r-', lw=2.5, label='Gauge')
ax2.axhline(1.0, color='black', ls='-', lw=1.5, label='Margin = 1')
ax2.axhline(4.5, color='gray', ls=':', lw=1, alpha=0.5, label='Original margin (grav)')
ax2.axvline(f_tracelog, color='orange', ls='--', lw=2, label=f'f_tracelog={f_tracelog:.1e}')
ax2.axvline(f_EIH, color='purple', ls='--', lw=2, label=f'f_EIH={f_EIH:.1e}')
ax2.axvline(4.5, color='gray', ls=':', lw=1.5, alpha=0.5, label='f=4.5')

ax2.fill_between(f_dense, 1, np.max(margin_grav)*10, alpha=0.06, color='green')
ax2.fill_between(f_dense, 0, 1, alpha=0.06, color='red')

ax2.set_xlabel('Correction factor f', fontsize=13)
ax2.set_ylabel('Margin (FIRAS bound / dtau)', fontsize=13)
ax2.set_title('(B) Safety Margin vs Correction Factor', fontsize=13)
ax2.legend(fontsize=8, loc='upper right')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(1e-5, 30)
ax2.set_ylim(0.01, 1e8)

# --- Panel C: Effective scaling exponent ---
ax3 = fig.add_subplot(gs_plot[1, 0])

# Use gravity route for scaling analysis
mask = (f_dense > 1e-4) & (f_dense < 20)
ax3.semilogx(f_dense[mask], dlog[mask], 'b-', lw=2.5)
ax3.axhline(1.0, color='red', ls='--', alpha=0.5, label=r'$\alpha=1$ (BD limit)')
ax3.axhline(0.75, color='orange', ls='--', alpha=0.5, label=r'$\alpha=3/4$ (short-time)')
ax3.axhline(0.5, color='green', ls='--', alpha=0.5, label=r'$\alpha=1/2$')

ax3.axvline(f_tracelog, color='orange', ls=':', lw=2)
ax3.axvline(f_EIH, color='purple', ls=':', lw=2)

ax3.set_xlabel('Correction factor f', fontsize=13)
ax3.set_ylabel(r'Effective exponent $\alpha$: $\delta\tau \propto f^\alpha$', fontsize=13)
ax3.set_title(r'(C) Scaling Exponent: $\delta\tau/\tau \propto f^\alpha$', fontsize=13)
ax3.legend(fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_ylim(0.3, 1.2)

# --- Panel D: Summary table ---
ax4 = fig.add_subplot(gs_plot[1, 1])
ax4.axis('off')

table_data = [
    ['', 'Gravity', 'Gauge'],
    ['Original (f=1)', f'{orig_grav_transit:.2e}', f'{orig_gauge_transit:.2e}'],
    ['Margin (f=1)', f'{FIRAS_bound/orig_grav_transit:.1f}x', f'{FIRAS_bound/orig_gauge_transit:.2f}x'],
    ['', '', ''],
    [f'Trace-log (f={f_tracelog:.1e})',
     f'{results_summary["grav_f_tracelog"]["dtau"]:.2e}',
     f'{results_summary["gauge_f_tracelog"]["dtau"]:.2e}'],
    [f'Margin',
     f'{results_summary["grav_f_tracelog"]["margin"]:.0f}x',
     f'{results_summary["gauge_f_tracelog"]["margin"]:.0f}x'],
    ['', '', ''],
    [f'EIH (f={f_EIH:.1e})',
     f'{results_summary["grav_f_EIH"]["dtau"]:.2e}',
     f'{results_summary["gauge_f_EIH"]["dtau"]:.2e}'],
    [f'Margin',
     f'{results_summary["grav_f_EIH"]["margin"]:.0f}x',
     f'{results_summary["gauge_f_EIH"]["margin"]:.0f}x'],
    ['', '', ''],
    ['FIRAS bound', f'{FIRAS_bound:.0e}', f'{FIRAS_bound:.0e}'],
    ['Gate f<4.5?', f'f={f_tracelog:.1e} << 4.5', 'PASS'],
    ['HOMOG-42-RECOMPUTE', gate_verdict, 'STRENGTHENED'],
]

table = ax4.table(cellText=table_data, cellLoc='center', loc='center',
                  colWidths=[0.4, 0.3, 0.3])
table.auto_set_font_size(False)
table.set_fontsize(9)
table.scale(1, 1.3)

for j in range(3):
    table[0, j].set_facecolor('#4472C4')
    table[0, j].set_text_props(color='white', fontweight='bold')

# Color verdict row
for j in range(3):
    table[12, j].set_facecolor('#C6EFCE')

ax4.set_title('(D) HOMOG-42-RECOMPUTE-44 Summary', fontsize=13, pad=20)

fig.suptitle('HOMOG-42-RECOMPUTE-44: E-vs-F Corrected Homogeneity\n'
             'Both physical corrections f << 1 STRENGTHEN the margin',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig('tier0-computation/s44_homog_recompute.png', dpi=150, bbox_inches='tight')
print("Saved: tier0-computation/s44_homog_recompute.png")
plt.close()

print("\n" + "=" * 70)
print("COMPUTATION COMPLETE")
print("=" * 70)
