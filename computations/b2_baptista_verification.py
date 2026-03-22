"""
B-2: CROSS-VERIFICATION OF SP GEOMETRY AGAINST BAPTISTA PAPERS
===============================================================

Baptista-Spacetime-Analyst — Session 17b

Verifies SP-Geometer's 17a outputs against Baptista's equations:
  1. g_ab reproduces eq 3.68: g_s = e^{2s}g_0|_{u(1)} + e^{-2s}g_0|_{su(2)} + e^s g_0|_{C^2}
  2. R(s)/R(0) matches eq 3.70: [2e^{2s}-1+8e^{-s}-e^{-4s}]/8
  3. V_tree(s) matches eq 3.80: V(0,s) = 1 - (1/10)[2e^{2s}-1+8e^{-s}-e^{-4s}]
  4. Sign conventions: Baptista uses (+,...,+) on SU(3)
  5. Volume preservation: det(g_s)/det(g_0) = 1 (analytic proof + numerical)

DELIVERABLE: Equation-by-equation PASS/FAIL with numerical evidence.

Author: Baptista-Spacetime-Analyst (Session 17b)
Date: 2026-02-14
"""

import numpy as np
from numpy.linalg import det, eigvalsh, inv, cholesky
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, validate_connection,
    U1_IDX, SU2_IDX, C2_IDX
)
from tier1_spectral_action import (
    scalar_curvature_from_connection, scalar_curvature_analytical,
    baptista_V_potential
)


def sep(title):
    print(f"\n{'='*72}")
    print(f"  {title}")
    print(f"{'='*72}")


# =============================================================================
# INFRASTRUCTURE
# =============================================================================

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)

s_test = np.array([0.0, 0.15, 0.30, 0.50, 1.0, 1.14, 2.0])

PASS_COUNT = 0
FAIL_COUNT = 0

def check(name, condition, detail=""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    print(f"    [{status}] {name}")
    if detail:
        print(f"           {detail}")


# =============================================================================
# CHECK 0: KILLING FORM CONVENTIONS
# =============================================================================
sep("CHECK 0: KILLING FORM AND GENERATOR CONVENTIONS")

# Baptista uses anti-Hermitian generators e_a = -i lambda_a / 2
# with [e_a, e_b] = f_{abc} e_c and Tr(e_a e_b) = -1/2 delta_{ab}
# => Killing form B_{ab} = f_{acd}f_{bcd}

# Verify B_ab = +3 delta_{ab} (positive for anti-Hermitian generators)
B_diag = np.diag(B_ab)
B_offdiag = B_ab - np.diag(B_diag)
B_val = B_diag[0]

print(f"\n  Killing form B_ab = f_{{acd}} f_{{bcd}}:")
print(f"    B[0,0] = {B_val:.15f}")
print(f"    |B - {B_val:.1f}*I|_max = {np.max(np.abs(B_ab - B_val*np.eye(8))):.2e}")
print(f"    |off-diagonal|_max = {np.max(np.abs(B_offdiag)):.2e}")

check("Killing form B_ab = +3 I_8",
      abs(B_val - 3.0) < 1e-14 and np.max(np.abs(B_offdiag)) < 1e-14,
      f"B = {B_val:.15f} * I, off-diag max = {np.max(np.abs(B_offdiag)):.2e}")

# Sign convention: B > 0 means we are using the POSITIVE-DEFINITE convention
# Baptista uses g_0 = |B| which would be 3*I for B = -3I (standard math convention)
# but here B IS positive already. The code uses g_0 = |B| = abs(B) = 3*I regardless.
# The base metric is g_0 = 3*I (positive definite) in both conventions.
print(f"\n  Base metric g_0 = |B_ab| = {abs(B_val):.1f} * I_8 (positive definite)")
check("Base metric g_0 = 3 I_8 (positive definite)",
      abs(abs(B_val) - 3.0) < 1e-14)


# =============================================================================
# CHECK 1: CARTAN DECOMPOSITION su(3) = u(1) + su(2) + C^2
# =============================================================================
sep("CHECK 1: CARTAN DECOMPOSITION su(3) = u(1) + su(2) + C^2")

print(f"\n  Decomposition indices (Gell-Mann basis):")
print(f"    su(2) = {{lambda_1, lambda_2, lambda_3}} => indices {SU2_IDX}")
print(f"    C^2   = {{lambda_4, lambda_5, lambda_6, lambda_7}} => indices {C2_IDX}")
print(f"    u(1)  = {{lambda_8}} => indices {U1_IDX}")
print(f"    Dimensions: 3 + 4 + 1 = {len(SU2_IDX)+len(C2_IDX)+len(U1_IDX)} = dim(su(3))")

check("Dimension count: 3+4+1 = 8",
      len(SU2_IDX)+len(C2_IDX)+len(U1_IDX) == 8)

# Verify su(2) subalgebra: [su(2), su(2)] subset su(2)
# i.e., f_{abc} = 0 when a,b in SU2_IDX and c not in SU2_IDX
su2_closure_err = 0.0
for a in SU2_IDX:
    for b in SU2_IDX:
        for c in range(8):
            if c not in SU2_IDX:
                su2_closure_err = max(su2_closure_err, abs(f_abc[a, b, c]))

print(f"\n  su(2) subalgebra closure: max |f_{{abc}}| for a,b in su(2), c not in su(2):")
print(f"    = {su2_closure_err:.2e}")
check("su(2) is a subalgebra: [su(2),su(2)] subset su(2)",
      su2_closure_err < 1e-14)

# Verify u(1) is central in u(2) = su(2)+u(1): [u(1), su(2)] = 0
u1_su2_err = 0.0
for a in U1_IDX:
    for b in SU2_IDX:
        for c in range(8):
            u1_su2_err = max(u1_su2_err, abs(f_abc[a, b, c]))

print(f"\n  u(1) centrality in u(2): max |f_{{abc}}| for a in u(1), b in su(2):")
print(f"    = {u1_su2_err:.2e}")
check("[u(1), su(2)] = 0 (u(1) central in u(2))",
      u1_su2_err < 1e-14)

# Verify C^2 is an Ad(u(2))-module: [u(2), C^2] subset C^2
# i.e., f_{abc} = 0 when a in u(2), b in C^2, c not in C^2
c2_module_err = 0.0
u2_idx = SU2_IDX + U1_IDX
for a in u2_idx:
    for b in C2_IDX:
        for c in range(8):
            if c not in C2_IDX:
                c2_module_err = max(c2_module_err, abs(f_abc[a, b, c]))

print(f"\n  C^2 is Ad(u(2))-module: max |f_{{abc}}| for a in u(2), b in C^2, c not in C^2:")
print(f"    = {c2_module_err:.2e}")
check("[u(2), C^2] subset C^2 (Ad-module structure)",
      c2_module_err < 1e-14)


# =============================================================================
# CHECK 2: METRIC g_s = eq 3.68 (DIAGONAL IN GELL-MANN BASIS)
# =============================================================================
sep("CHECK 2: METRIC g_s MATCHES eq 3.68")

print(f"\n  Baptista eq 3.68:")
print(f"    g_s = e^{{2s}} g_0|_{{u(1)}} + e^{{-2s}} g_0|_{{su(2)}} + e^s g_0|_{{C^2}}")
print(f"  In Gell-Mann basis (g_0 = 3I):")
print(f"    g_s = 3 * diag(e^{{-2s}}, e^{{-2s}}, e^{{-2s}}, e^s, e^s, e^s, e^s, e^{{2s}})")

max_metric_rel_err = 0.0
max_metric_abs_err = 0.0
max_offdiag_err = 0.0

for s in s_test:
    g_code = jensen_metric(B_ab, s)

    # Build analytic metric
    scale = np.zeros(8)
    for a in SU2_IDX:
        scale[a] = np.exp(-2*s)
    for a in C2_IDX:
        scale[a] = np.exp(s)
    for a in U1_IDX:
        scale[a] = np.exp(2*s)
    g_analytic = 3.0 * np.diag(scale)

    err_abs = np.max(np.abs(g_code - g_analytic))
    err_rel = err_abs / np.max(np.abs(g_analytic)) if np.max(np.abs(g_analytic)) > 0 else 0
    err_offdiag = np.max(np.abs(g_code - np.diag(np.diag(g_code))))
    max_metric_abs_err = max(max_metric_abs_err, err_abs)
    max_metric_rel_err = max(max_metric_rel_err, err_rel)
    max_offdiag_err = max(max_offdiag_err, err_offdiag)

    print(f"    s={s:5.2f}: abs err = {err_abs:.2e}, rel err = {err_rel:.2e}, "
          f"off-diag max = {err_offdiag:.2e}")

check("g_s matches eq 3.68 at all test s values (rel err < 1e-14)",
      max_metric_rel_err < 1e-14,
      f"max relative error = {max_metric_rel_err:.2e}, max absolute error = {max_metric_abs_err:.2e}")

check("g_s is EXACTLY diagonal (off-diagonal = 0)",
      max_offdiag_err < 1e-15,
      f"max off-diagonal = {max_offdiag_err:.2e}")


# =============================================================================
# CHECK 3: VOLUME PRESERVATION det(g_s)/det(g_0) = 1 (ANALYTIC + NUMERICAL)
# =============================================================================
sep("CHECK 3: VOLUME PRESERVATION (ANALYTIC + NUMERICAL)")

print(f"\n  ANALYTIC PROOF:")
print(f"    det(g_s) = 3^8 * prod(scale_factors)")
print(f"    prod = (e^{{-2s}})^3 * (e^s)^4 * (e^{{2s}})^1")
print(f"         = e^{{-6s}} * e^{{4s}} * e^{{2s}}")
print(f"         = e^{{-6s + 4s + 2s}}")
print(f"         = e^0 = 1")
print(f"    Therefore det(g_s) = 3^8 * 1 = det(g_0). QED.")

max_vol_err = 0.0
g0 = jensen_metric(B_ab, 0.0)
det_g0 = det(g0)

print(f"\n  NUMERICAL VERIFICATION:")
print(f"    det(g_0) = {det_g0:.15f} = 3^8 = {3**8}")

for s in s_test:
    g = jensen_metric(B_ab, s)
    ratio = det(g) / det_g0
    err = abs(ratio - 1.0)
    max_vol_err = max(max_vol_err, err)
    print(f"    s={s:5.2f}: det(g_s)/det(g_0) = {ratio:.16e}, |1-ratio| = {err:.2e}")

check("Volume preservation: det(g_s)/det(g_0) = 1 (analytic QED + numerical)",
      max_vol_err < 1e-14,
      f"max |1 - det ratio| = {max_vol_err:.2e}")


# =============================================================================
# CHECK 4: SCALAR CURVATURE R(s) MATCHES eq 3.70
# =============================================================================
sep("CHECK 4: SCALAR CURVATURE R(s) vs BAPTISTA eq 3.70")

print(f"\n  Baptista eq 3.70:")
print(f"    f(s) = 2 e^{{2s}} - 1 + 8 e^{{-s}} - e^{{-4s}}")
print(f"    R(s)/R(0) = f(s)/f(0)")
print(f"    f(0) = 2-1+8-1 = 8")
print(f"    R(0) = 2.0 (our normalization)")

def f_baptista(s):
    return 2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s)

# Verify f(0) = 8
f0 = f_baptista(0.0)
print(f"\n    f(0) = {f0:.15f}")
check("f(0) = 8.000000000000000",
      abs(f0 - 8.0) < 1e-14)

# R(0) from Levi-Civita connection
R0_code, Ric0 = scalar_curvature_from_connection(0.0, f_abc)
print(f"    R(0) from Levi-Civita = {R0_code:.15f}")
check("R(0) = 2.000000000000000 (from Levi-Civita)",
      abs(R0_code - 2.0) < 1e-13,
      f"R(0) = {R0_code}")

# Einstein check at s=0: Ric = R/8 * I
R_over_8 = R0_code / 8.0
einstein_err = np.max(np.abs(Ric0 - R_over_8 * np.eye(8)))
print(f"    Einstein at s=0: |Ric - R/8 I| = {einstein_err:.2e}")
check("s=0 is Einstein: Ric = R/8 * I_8",
      einstein_err < 1e-13)

# Compare R(s) at all test points
print(f"\n  R(s) comparison at 7 s-values:")
print(f"    Required: agreement < 10^{{-14}}")
print()
print(f"    {'s':>6}  {'R(s) Levi-Civita':>18}  {'R(s) eq 3.70':>18}  {'rel error':>14}")
print(f"    {'-'*6}  {'-'*18}  {'-'*18}  {'-'*14}")

max_R_err = 0.0
for s in s_test:
    R_code, _ = scalar_curvature_from_connection(s, f_abc)
    R_analytic = 2.0 * f_baptista(s) / 8.0
    rel_err = abs(R_code - R_analytic) / abs(R_analytic) if abs(R_analytic) > 1e-15 else 0
    max_R_err = max(max_R_err, rel_err)
    print(f"    {s:6.3f}  {R_code:18.14f}  {R_analytic:18.14f}  {rel_err:14.2e}")

check(f"R(s) matches eq 3.70 at all 7 s-values (tol < 10^-14)",
      max_R_err < 1e-14,
      f"max relative error = {max_R_err:.2e}")

# Also verify against scalar_curvature_analytical() which returns R(s)/R(0)
print(f"\n  Cross-check: scalar_curvature_analytical(s) == f(s)/f(0):")
max_ratio_err = 0.0
for s in s_test:
    ratio_code = scalar_curvature_analytical(s)
    ratio_analytic = f_baptista(s) / 8.0
    err = abs(ratio_code - ratio_analytic)
    max_ratio_err = max(max_ratio_err, err)
    print(f"    s={s:5.2f}: code={ratio_code:.15f}, analytic={ratio_analytic:.15f}, err={err:.2e}")

check("scalar_curvature_analytical(s) == f(s)/8",
      max_ratio_err < 1e-15)


# =============================================================================
# CHECK 5: V_tree(s) MATCHES eq 3.80
# =============================================================================
sep("CHECK 5: V_tree(s) = V(sigma=0, s) MATCHES eq 3.80")

print(f"\n  Baptista eq 3.80 at sigma=0:")
print(f"    V(0, s) = 1 - (1/10) * [2 e^{{2s}} - 1 + 8 e^{{-s}} - e^{{-4s}}]")
print(f"            = 1 - f(s)/10")
print(f"    V(0, 0) = 1 - 8/10 = 0.2")

def V_tree_analytic(s):
    return 1.0 - f_baptista(s) / 10.0

# Verify V(0,0) = 0.2
V00 = V_tree_analytic(0.0)
V00_code = baptista_V_potential(0.0, 0.0)
print(f"\n    V(0,0) analytic = {V00:.15f}")
print(f"    V(0,0) code     = {V00_code:.15f}")
check("V(0,0) = 0.2",
      abs(V00 - 0.2) < 1e-15 and abs(V00_code - 0.2) < 1e-15)

# Compare at all test points
print(f"\n  V_tree comparison at 7 s-values:")
print(f"    {'s':>6}  {'V analytic':>18}  {'V code':>18}  {'abs error':>14}")
print(f"    {'-'*6}  {'-'*18}  {'-'*18}  {'-'*14}")

max_V_err = 0.0
for s in s_test:
    V_analytic = V_tree_analytic(s)
    V_code = baptista_V_potential(0.0, s)
    err = abs(V_analytic - V_code)
    max_V_err = max(max_V_err, err)
    print(f"    {s:6.3f}  {V_analytic:18.14f}  {V_code:18.14f}  {err:14.2e}")

check("V_tree(s) matches eq 3.80 at all 7 s-values",
      max_V_err < 1e-14,
      f"max absolute error = {max_V_err:.2e}")


# =============================================================================
# CHECK 6: CONNECTION COEFFICIENTS — KOSZUL FORMULA
# =============================================================================
sep("CHECK 6: CONNECTION COEFFICIENTS (KOSZUL FORMULA)")

print(f"\n  Koszul formula in ON frame:")
print(f"    2 Gamma_{{cab}} = ft_{{abc}} - ft_{{bca}} + ft_{{cab}}")
print(f"  Metric compatibility: Gamma^c_{{ab}} + Gamma^b_{{ac}} = 0")

max_mc_err = 0.0
for s in s_test:
    g = jensen_metric(B_ab, s)
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    mc_err = validate_connection(Gamma)
    max_mc_err = max(max_mc_err, mc_err)
    print(f"    s={s:5.2f}: metric compatibility violation = {mc_err:.2e}")

check("Metric compatibility at all s values",
      max_mc_err < 1e-14,
      f"max violation = {max_mc_err:.2e}")

# At s=0: Gamma^c_{ab} = (1/2) f^c_{ab} (bi-invariant metric)
print(f"\n  Bi-invariant check (s=0): Gamma^c_{{ab}} = (1/2) ft^c_{{ab}}")
g0 = jensen_metric(B_ab, 0.0)
E0 = orthonormal_frame(g0)
ft0 = frame_structure_constants(f_abc, E0)
Gamma0 = connection_coefficients(ft0)

# For bi-invariant metric, Gamma_{cab} = (1/2) ft_{abc}
# where ft_{abc} = ft[a,b,c]. So Gamma[c,a,b] = (1/2)*ft[a,b,c].
biinv_err = 0.0
for c in range(8):
    for a in range(8):
        for b in range(8):
            diff = abs(Gamma0[c, a, b] - 0.5 * ft0[a, b, c])
            biinv_err = max(biinv_err, diff)

print(f"    |Gamma_0 - (1/2)ft|_max = {biinv_err:.2e}")
check("s=0: Gamma = (1/2) ft (bi-invariant connection)",
      biinv_err < 1e-14)


# =============================================================================
# CHECK 7: SIGN CONVENTION VERIFICATION
# =============================================================================
sep("CHECK 7: SIGN CONVENTION — BAPTISTA USES (+,...,+) ON SU(3)")

print(f"\n  Baptista signs:")
print(f"    (1) g_0 is POSITIVE DEFINITE (all eigenvalues > 0)")
print(f"    (2) R(0) > 0 (positive curvature for compact group)")
print(f"    (3) e_a are ANTI-HERMITIAN (e_a^dag = -e_a)")
print(f"    (4) B_ab > 0 in our convention (f_{{acd}}f_{{bcd}} for anti-Hermitian gens)")

# Check (1)
g0_evals = eigvalsh(g0)
print(f"\n    g_0 eigenvalues: {[f'{e:.6f}' for e in g0_evals]}")
check("g_0 positive definite", all(g0_evals > 0))

# Check (2)
print(f"    R(0) = {R0_code:.10f}")
check("R(0) > 0 (positive curvature)", R0_code > 0)

# Check (3)
ah_err = 0.0
for a, e in enumerate(gens):
    ah_err = max(ah_err, np.max(np.abs(e + e.conj().T)))
print(f"    max |e_a + e_a^dag| = {ah_err:.2e}")
check("Generators anti-Hermitian: e_a^dag = -e_a", ah_err < 1e-15)

# Check (4)
print(f"    B_ab[0,0] = {B_ab[0,0]:.10f}")
check("B_ab > 0", B_ab[0,0] > 0)


# =============================================================================
# CHECK 8: SP-1 OUTPUT MATCHES EXPECTED FORM
# =============================================================================
sep("CHECK 8: SP-1 OUTPUT — g_s = 3 * diag(e^{-2s},...,e^s,...,e^{2s})")

print(f"\n  SP-1 claimed:")
print(f"    g_s = 3 * diag(e^{{-2s}}, e^{{-2s}}, e^{{-2s}}, e^s, e^s, e^s, e^s, e^{{2s}})")
print(f"  This IS eq 3.68 in Gell-Mann basis.")

# Explicit check at s=0.15
s_check = 0.15
g_check = jensen_metric(B_ab, s_check)
expected = 3.0 * np.diag([
    np.exp(-2*s_check), np.exp(-2*s_check), np.exp(-2*s_check),
    np.exp(s_check), np.exp(s_check), np.exp(s_check), np.exp(s_check),
    np.exp(2*s_check)
])
sp1_err = np.max(np.abs(g_check - expected))
sp1_rel = sp1_err / np.max(np.abs(expected))
print(f"\n    At s=0.15: |g_code - SP-1 claimed|_max = {sp1_err:.2e}")
print(f"    Relative error = {sp1_rel:.2e}")
check("SP-1 output matches eq 3.68 at s=0.15 (machine epsilon)",
      sp1_rel < 1e-14,
      f"abs err = {sp1_err:.2e}, rel err = {sp1_rel:.2e}")


# =============================================================================
# CHECK 9: SP-4 V(0,s) — BITWISE COMPARISON WITH tier1_spectral_action.py
# =============================================================================
sep("CHECK 9: SP-4 V(0,s) — BITWISE MATCH WITH tier1_spectral_action.py")

print(f"\n  SP-4 claimed V(0,s) = 1 - (1/10)[2e^{{2s}}-1+8e^{{-s}}-e^{{-4s}}]")
print(f"  baptista_V_potential(0,s) implements the same formula.")

max_bitwise_err = 0.0
for s in s_test:
    V_sp4 = 1.0 - (1.0/10.0)*(2*np.exp(2*s) - 1 + 8*np.exp(-s) - np.exp(-4*s))
    V_code = baptista_V_potential(0.0, s)
    err = abs(V_sp4 - V_code)
    max_bitwise_err = max(max_bitwise_err, err)
    print(f"    s={s:5.2f}: V_SP4={V_sp4:.16e}, V_code={V_code:.16e}, diff={err:.2e}")

check("SP-4 formula bitwise matches baptista_V_potential(0,s)",
      max_bitwise_err < 1e-15,
      f"max difference = {max_bitwise_err:.2e}")


# =============================================================================
# FINAL SUMMARY
# =============================================================================
sep("B-2 VERIFICATION SUMMARY")

print(f"\n  Total checks: {PASS_COUNT + FAIL_COUNT}")
print(f"  PASSED: {PASS_COUNT}")
print(f"  FAILED: {FAIL_COUNT}")
print()

if FAIL_COUNT == 0:
    print("  *** ALL CHECKS PASSED ***")
    print("  SP-Geometer's 17a outputs are VERIFIED against Baptista equations.")
    print("  SP-2 (curvature invariants) is CLEARED to proceed.")
else:
    print(f"  *** {FAIL_COUNT} CHECKS FAILED ***")
    print("  SP-2 is BLOCKED until failures are resolved.")

print()
print("  Equation-by-equation summary:")
print("    eq 3.68 (metric):           PASS" if max_metric_rel_err < 1e-14 else "    eq 3.68 (metric):           FAIL")
print("    eq 3.70 (scalar curvature): PASS" if max_R_err < 1e-14 else "    eq 3.70 (scalar curvature): FAIL")
print("    eq 3.80 (V_tree):           PASS" if max_V_err < 1e-14 else "    eq 3.80 (V_tree):           FAIL")
print("    Volume preservation:        PASS" if max_vol_err < 1e-14 else "    Volume preservation:        FAIL")
print("    Sign conventions:           PASS" if R0_code > 0 else "    Sign conventions:           FAIL")
print("    Koszul formula:             PASS" if max_mc_err < 1e-14 else "    Koszul formula:             FAIL")
print("    SP-1 explicit metric:       PASS" if sp1_rel < 1e-14 else "    SP-1 explicit metric:       FAIL")
print("    SP-4 V(0,s) bitwise:        PASS" if max_bitwise_err < 1e-15 else "    SP-4 V(0,s) bitwise:        FAIL")
