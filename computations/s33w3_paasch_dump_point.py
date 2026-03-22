"""
Session 33 Workshop 3: Paasch phi at dump point tau=0.190
=========================================================
Deliverables:
  1. Exact phi_paasch ratio m_{(3,0)}/m_{(0,0)} at tau=0.190
  2. Paasch tolerance assessment (P-30phi gate)
  3. Domain wall corollary analysis
  4. Transcendental equation test: lambda_B2^2 * ln(lambda_B2) at dump point
  5. B1+B2+B3 branch eigenvalues at dump point
"""

import numpy as np
from scipy.interpolate import CubicSpline

# =====================================================================
# PART 1: Inter-sector ratio m_{(3,0)}/m_{(0,0)} at tau=0.190
# =====================================================================

# Load s22a_paasch_curve.npz -- contains E_(0,0) and E_(3,0) at tau=0,0.1,...,2.0
pc = np.load('s22a_paasch_curve.npz', allow_pickle=True)
tau_pc = pc['tau_values']
E_00 = pc['E_00']
E_30 = pc['E_30']
ratio_pc = pc['ratio']  # E_30/E_00
phi_p = 1.5315844  # exact Paasch phi from x = e^{-x^2}

print("=" * 70)
print("PART 1: Inter-sector ratio E_{(3,0)}/E_{(0,0)} at tau = 0.190")
print("=" * 70)

# Build cubic spline interpolants for E_00 and E_30
cs_E00 = CubicSpline(tau_pc, E_00)
cs_E30 = CubicSpline(tau_pc, E_30)
cs_ratio = CubicSpline(tau_pc, ratio_pc)

# Evaluate at dump point tau=0.190
tau_dump = 0.190

E00_dump = cs_E00(tau_dump)
E30_dump = cs_E30(tau_dump)
ratio_dump = E30_dump / E00_dump
ratio_dump_direct = cs_ratio(tau_dump)

print(f"\nE_(0,0) at tau={tau_dump:.3f}: {E00_dump:.8f}")
print(f"E_(3,0) at tau={tau_dump:.3f}: {E30_dump:.8f}")
print(f"Ratio E_(3,0)/E_(0,0):        {ratio_dump:.8f}")
print(f"Ratio (direct spline):         {ratio_dump_direct:.8f}")
print(f"phi_paasch (exact):            {phi_p:.7f}")
print(f"Deviation from phi_paasch:     {(ratio_dump/phi_p - 1)*100:+.4f}%")
print(f"Deviation (direct spline):     {(ratio_dump_direct/phi_p - 1)*100:+.4f}%")

# Also compute at key neighboring points for context
print("\n--- Context table ---")
print(f"{'tau':>6s}  {'E_(0,0)':>10s}  {'E_(3,0)':>10s}  {'ratio':>10s}  {'dev(%)':>8s}")
for t in [0.10, 0.12, 0.14, 0.15, 0.16, 0.17, 0.18, 0.185, 0.190, 0.195, 0.20, 0.25]:
    e00 = cs_E00(t)
    e30 = cs_E30(t)
    r = e30 / e00
    dev = (r / phi_p - 1) * 100
    marker = " <-- dump" if abs(t - 0.190) < 0.001 else ""
    print(f"{t:6.3f}  {e00:10.6f}  {e30:10.6f}  {r:10.6f}  {dev:+8.4f}%{marker}")

# =====================================================================
# PART 2: Paasch tolerance assessment (P-30phi gate)
# =====================================================================

print("\n" + "=" * 70)
print("PART 2: P-30phi Gate Assessment")
print("=" * 70)

# Gate P-30phi: ratio at operating point must fall in [1.524, 1.539] (0.5% of phi_paasch)
gate_low = phi_p * (1 - 0.005)   # 1.52392
gate_high = phi_p * (1 + 0.005)  # 1.53924

print(f"\nPaasch tolerance window: [{gate_low:.5f}, {gate_high:.5f}]")
print(f"  (phi_paasch * [0.995, 1.005])")
print(f"Ratio at tau=0.190:     {ratio_dump:.6f}")
inside = gate_low <= ratio_dump <= gate_high
print(f"Inside tolerance:       {'YES' if inside else 'NO'}")
print(f"Distance from boundary: {min(ratio_dump - gate_low, gate_high - ratio_dump):.5f}")

# Also check the broader 0.4% tolerance from Paper 02 (dm/m = 4e-3)
gate_low_02 = phi_p * (1 - 0.004)
gate_high_02 = phi_p * (1 + 0.004)
inside_02 = gate_low_02 <= ratio_dump <= gate_high_02
print(f"\nPaper 02 tolerance (0.4%): [{gate_low_02:.5f}, {gate_high_02:.5f}]")
print(f"Inside Paper 02 window: {'YES' if inside_02 else 'NO'}")

# Find tau where ratio exactly equals phi_paasch (using fine grid)
tau_fine = np.linspace(0.0, 0.3, 10000)
ratio_fine = cs_ratio(tau_fine)
crossings = []
for i in range(len(ratio_fine)-1):
    if (ratio_fine[i] - phi_p) * (ratio_fine[i+1] - phi_p) < 0:
        # Linear interpolation for crossing
        t_cross = tau_fine[i] + (phi_p - ratio_fine[i]) / (ratio_fine[i+1] - ratio_fine[i]) * (tau_fine[i+1] - tau_fine[i])
        crossings.append(t_cross)

print(f"\nExact phi_paasch crossings: {crossings}")
if crossings:
    tau_phi = crossings[-1]  # The crossing near 0.15
    print(f"Relevant crossing at tau = {tau_phi:.6f}")
    print(f"Distance from dump point: Delta_tau = {abs(tau_dump - tau_phi):.4f}")

# =====================================================================
# PART 3: B1+B2+B3 branch eigenvalues at and near dump point
# =====================================================================

print("\n" + "=" * 70)
print("PART 3: Singlet B1+B2+B3 Branch Eigenvalues")
print("=" * 70)

# Load s24a data for intra-sector structure
er = np.load('s24a_eigenvalue_ratios.npz', allow_pickle=True)
tau_er = er['tau']
abs_eig = er['abs_eigenvalues']  # (9, 16)

# Identify branches at each tau (sorted eigenvalues)
# At tau>0: B1 = lowest 2, B2 = middle 8, B3 = highest 6
print(f"\n{'tau':>6s}  {'B1 (2x)':>10s}  {'B2 (8x)':>10s}  {'B3 (6x)':>10s}  {'B2_min?':>8s}")
for i, t in enumerate(tau_er):
    eigs = np.sort(abs_eig[i])
    if t == 0:
        print(f"{t:6.2f}  {eigs[0]:10.6f}  (all degenerate = {eigs[0]:.6f})")
        continue
    b1 = eigs[0]     # 2 copies
    b2 = eigs[2]     # 8 copies (indices 2-9)
    b3 = eigs[10]    # 6 copies (indices 10-15)
    # Check B2 minimum status
    is_near_min = abs(t - 0.19) < 0.03
    print(f"{t:6.2f}  {b1:10.6f}  {b2:10.6f}  {b3:10.6f}  {'<--' if is_near_min else ''}")

# Interpolate B2 eigenvalue at tau=0.190
# Extract B2 at each available tau
b2_vals = []
b1_vals = []
b3_vals = []
tau_nonzero = []
for i, t in enumerate(tau_er):
    if t == 0:
        continue
    eigs = np.sort(abs_eig[i])
    b1_vals.append(eigs[0])
    b2_vals.append(eigs[2])
    b3_vals.append(eigs[10])
    tau_nonzero.append(t)

tau_nz = np.array(tau_nonzero)
b1_arr = np.array(b1_vals)
b2_arr = np.array(b2_vals)
b3_arr = np.array(b3_vals)

cs_b1 = CubicSpline(tau_nz, b1_arr)
cs_b2 = CubicSpline(tau_nz, b2_arr)
cs_b3 = CubicSpline(tau_nz, b3_arr)

b1_dump = cs_b1(tau_dump)
b2_dump = cs_b2(tau_dump)
b3_dump = cs_b3(tau_dump)

print(f"\nInterpolated values at tau = {tau_dump}:")
print(f"  B1 = {b1_dump:.8f}")
print(f"  B2 = {b2_dump:.8f}")
print(f"  B3 = {b3_dump:.8f}")

# Find B2 minimum
tau_search = np.linspace(0.1, 0.35, 5000)
b2_search = cs_b2(tau_search)
i_min = np.argmin(b2_search)
tau_b2min = tau_search[i_min]
b2_min = b2_search[i_min]
print(f"\n  B2 minimum at tau = {tau_b2min:.4f}, lambda_B2 = {b2_min:.8f}")
print(f"  B2 at dump (0.190): {b2_dump:.8f}")
print(f"  B2 at phi crossing ({crossings[-1] if crossings else 'N/A'}): {cs_b2(crossings[-1]) if crossings else 'N/A'}")

# =====================================================================
# PART 4: Transcendental equation test
# =====================================================================

print("\n" + "=" * 70)
print("PART 4: Transcendental Equation Test")
print("=" * 70)

# Paasch's equation: x = e^{-x^2}, equivalently phi^2 * ln(phi) = 1
# where phi = 1/x
# Test: lambda_B2^2 * ln(lambda_B2) at dump point
lam = b2_dump
trans_val = lam**2 * np.log(lam)
print(f"\nlambda_B2 at dump = {lam:.8f}")
print(f"lambda_B2^2 * ln(lambda_B2) = {trans_val:.8f}")
print(f"  Compare to 1.0:  deviation = {(trans_val/1.0 - 1)*100:+.2f}%")
print(f"  Compare to 0.5:  deviation = {(trans_val/0.5 - 1)*100:+.2f}%")

# Also test the B1 and B3 eigenvalues
lam_b1 = b1_dump
lam_b3 = b3_dump
trans_b1 = lam_b1**2 * np.log(lam_b1)
trans_b3 = lam_b3**2 * np.log(lam_b3)
print(f"\nlambda_B1 at dump = {lam_b1:.8f}")
print(f"lambda_B1^2 * ln(lambda_B1) = {trans_b1:.8f}")
print(f"\nlambda_B3 at dump = {lam_b3:.8f}")
print(f"lambda_B3^2 * ln(lambda_B3) = {trans_b3:.8f}")

# Test on the inter-sector ratio itself
r = ratio_dump
trans_ratio = r**2 * np.log(r)
print(f"\nratio at dump = {r:.8f}")
print(f"ratio^2 * ln(ratio) = {trans_ratio:.8f}")
print(f"  Compare to 1.0:  deviation = {(trans_ratio/1.0 - 1)*100:+.2f}%")

# For reference: phi_paasch^2 * ln(phi_paasch)
phi_ref = phi_p
trans_phi = phi_ref**2 * np.log(phi_ref)
print(f"\nphi_paasch^2 * ln(phi_paasch) = {trans_phi:.8f} (should = 1.0 by construction)")

# Also try: x = e^{-x^2} directly on 1/lambda_B2
x_b2 = 1.0 / lam
check = np.exp(-x_b2**2)
print(f"\n1/lambda_B2 = {x_b2:.8f}")
print(f"e^{{-(1/lambda_B2)^2}} = {check:.8f}")
print(f"  x vs e^{{-x^2}} deviation: {(check/x_b2 - 1)*100:+.2f}%")

# =====================================================================
# PART 5: Domain wall phi_paasch analysis
# =====================================================================

print("\n" + "=" * 70)
print("PART 5: Domain Wall Corollary")
print("=" * 70)

# For walls spanning [tau_1, tau_2], phi_paasch is exact at one side
# if the wall crosses tau ~ 0.148 (phi crossing)
if crossings:
    tau_phi_crossing = crossings[-1]

    print(f"\nphi_paasch crossing:    tau = {tau_phi_crossing:.4f}")
    print(f"Dump point:             tau = {tau_dump:.3f}")
    print(f"Wall span needed:       Delta_tau = {tau_dump - tau_phi_crossing:.4f}")

    # Candidate wall configurations
    print("\nCandidate wall configurations (straddling dump point):")
    walls = [
        (0.10, 0.25),
        (0.10, 0.20),
        (0.15, 0.25),
        (0.14, 0.22),
        (0.13, 0.20),
    ]
    print(f"{'tau_1':>6s}  {'tau_2':>6s}  {'phi_cross?':>11s}  {'dump_straddle?':>15s}  {'ratio_geo_mean':>15s}")
    for t1, t2 in walls:
        has_phi = t1 <= tau_phi_crossing <= t2
        straddles = t1 <= tau_dump <= t2
        # Geometric mean of ratios at boundaries
        r1 = cs_ratio(t1)
        r2 = cs_ratio(t2)
        geo = np.sqrt(r1 * r2)
        dev_geo = (geo / phi_p - 1) * 100
        print(f"{t1:6.2f}  {t2:6.2f}  {'YES' if has_phi else 'NO':>11s}  {'YES' if straddles else 'NO':>15s}  {geo:.6f} ({dev_geo:+.3f}%)")

    # Paasch equilibrium mass test
    print("\n--- Paasch Equilibrium Mass Test ---")
    print("m_E = sqrt(m_1 * m_2): geometric mean of boundary eigenvalues")
    for t1, t2 in [(0.15, 0.25), (0.10, 0.25)]:
        e00_1 = cs_E00(t1)
        e00_2 = cs_E00(t2)
        e00_geo = np.sqrt(e00_1 * e00_2)
        e00_dump_val = cs_E00(tau_dump)
        print(f"\n  Wall ({t1:.2f}, {t2:.2f}):")
        print(f"    E_(0,0) at t1: {e00_1:.6f}, at t2: {e00_2:.6f}")
        print(f"    Geometric mean: {e00_geo:.6f}")
        print(f"    E_(0,0) at dump: {e00_dump_val:.6f}")
        print(f"    Deviation: {(e00_geo / e00_dump_val - 1)*100:+.3f}%")

# =====================================================================
# PART 6: Summary and gate verdict
# =====================================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print(f"""
DELIVERABLE 1 -- phi_paasch at dump point:
  E_(3,0)/E_(0,0) at tau=0.190 = {ratio_dump:.6f}
  phi_paasch = {phi_p:.7f}
  Deviation: {(ratio_dump/phi_p - 1)*100:+.4f}%

DELIVERABLE 2 -- P-30phi gate assessment:
  Tolerance window [0.5%]: [{gate_low:.5f}, {gate_high:.5f}]
  Ratio at dump: {ratio_dump:.6f}
  GATE STATUS: {'PASS' if inside else 'FAIL'}

  Paper 02 tolerance [0.4%]: [{gate_low_02:.5f}, {gate_high_02:.5f}]
  Paper 02 STATUS: {'PASS' if inside_02 else 'FAIL'}

DELIVERABLE 3 -- Domain wall corollary:
  phi_paasch crossing at tau = {crossings[-1] if crossings else 'N/A'}
  Dump point at tau = 0.190
  Wall span: Delta_tau = {tau_dump - crossings[-1]:.4f} (if crossing exists)
  The "wrong triple" thesis resolves the tension IF domain walls
  span from ~{crossings[-1]:.3f} to ~{tau_dump:.3f}.

DELIVERABLE 4 -- Transcendental equation test:
  lambda_B2^2 * ln(lambda_B2) at dump = {trans_val:.6f}
  phi_paasch^2 * ln(phi_paasch) = {trans_phi:.6f} (= 1 by construction)
  Connection: {'ALGEBRAIC' if abs(trans_val - 1) < 0.01 or abs(trans_val - 0.5) < 0.01 else 'NOT SIMPLE RATIONAL'}

B2 EIGENVALUE AT DUMP: {b2_dump:.8f}
B2 MINIMUM LOCATION:   tau = {tau_b2min:.4f} (lambda_B2 = {b2_min:.8f})
""")

# Save results
np.savez('s33w3_paasch_dump_point.npz',
         tau_dump=tau_dump,
         E00_dump=E00_dump,
         E30_dump=E30_dump,
         ratio_dump=ratio_dump,
         phi_paasch=phi_p,
         deviation_pct=(ratio_dump/phi_p - 1)*100,
         gate_P30phi_pass=inside,
         gate_low=gate_low,
         gate_high=gate_high,
         tau_phi_crossing=crossings[-1] if crossings else np.nan,
         b1_dump=b1_dump,
         b2_dump=b2_dump,
         b3_dump=b3_dump,
         tau_b2_min=tau_b2min,
         b2_min=b2_min,
         trans_b2=trans_val,
         trans_phi=trans_phi,
         )
print("Results saved to s33w3_paasch_dump_point.npz")
