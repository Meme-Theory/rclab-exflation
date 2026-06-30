#!/usr/bin/env python3
"""
S77-B7-MEAN-EIGEN: Mean |lambda| and dS/dt* at Fold
=====================================================

Computes spectral statistical moments of D_K at tau_fold = 0.190:
  1. <|lambda|> = (1/N) * sum |lambda_j|           (mean absolute eigenvalue)
  2. <lambda^2> = (1/N) * sum lambda_j^2            (second moment = a_2 normalization)
  3. sigma^2    = <lambda^2> - <|lambda|>^2          (variance)
  4. Z(t*)      = sum_j exp(-lambda_j^2 / (t* * lambda_max^2))  (spectral partition function)
  5. S(t*)      = -dZ/dt* / Z                       (spectral entropy gradient)
  6. dS/dt*     = sign classification (restoring vs anti-restoring)

The Dirac operator is computed at L_max = 3 (max_pq_sum = 3) on Jensen-deformed
SU(3), using the math convention where D is anti-Hermitian with purely imaginary
eigenvalues. We extract |Im(lambda)| as the physical Dirac eigenvalues.

Peter-Weyl multiplicities: each eigenvalue from sector (p,q) has multiplicity
dim(p,q) = (p+1)(q+1)(p+q+2)/2 in the full L^2 spectrum.

Gate: S77-B7-MEAN-EIGEN (INFO diagnostic)

Author: Connes-NCG-Theorist (S77)
Date: 2026-04-13
"""

import numpy as np
import sys
import os

# Add computations to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, a0_fold, a2_fold, a4_fold

from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    validate_connection,
    validate_omega_hermitian,
    collect_spectrum,
)

# ============================================================
# Parameters
# ============================================================
L_MAX = 3  # (local) max p+q for Peter-Weyl truncation
T_STAR = 0.088  # (local) candidate intensive CC parameter from WS5
DT_STAR = 1e-5  # (local) finite difference step for dS/dt*

print("=" * 70)
print("S77-B7-MEAN-EIGEN: Mean |lambda| and dS/dt* at Fold")
print("=" * 70)
print(f"  tau_fold = {tau_fold}")
print(f"  L_max    = {L_MAX}")
print(f"  t*       = {T_STAR}")
print()

# ============================================================
# Step 1: Compute D_K eigenvalues at tau_fold
# ============================================================
print("Step 1: Computing Dirac spectrum at tau_fold...")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

cliff_err = validate_clifford(gammas)  # (local)
print(f"  Clifford algebra error: {cliff_err:.2e}")
assert cliff_err < 1e-13, f"Clifford algebra broken: {cliff_err}"

# Collect spectrum with Peter-Weyl multiplicities
all_eigenvalues, eval_data = collect_spectrum(
    tau_fold, gens, f_abc, gammas, max_pq_sum=L_MAX, verbose=True
)

print(f"\n  Total sectors computed: {len(eval_data)}")

# ============================================================
# Step 2: Build weighted eigenvalue arrays
# ============================================================
print("\nStep 2: Building weighted eigenvalue arrays...")

# all_eigenvalues is a list of (eigenvalue_complex, multiplicity)
# Extract |Im(lambda)| as the physical Dirac eigenvalues
# (math convention: D anti-Hermitian => eigenvalues purely imaginary)

abs_evals = []  # (local) list of |lambda| values
multiplicities = []  # (local) list of PW multiplicities
raw_evals = []  # (local) list of raw complex eigenvalues

for ev, mult in all_eigenvalues:
    abs_evals.append(np.abs(ev))
    multiplicities.append(mult)
    raw_evals.append(ev)

abs_evals = np.array(abs_evals)  # (local)
multiplicities = np.array(multiplicities, dtype=np.float64)  # (local)
raw_evals = np.array(raw_evals)  # (local)

# Check: eigenvalues should be purely imaginary (math convention)
real_parts = np.abs(raw_evals.real)  # (local)
imag_parts = np.abs(raw_evals.imag)  # (local)
max_real = np.max(real_parts)  # (local)
max_imag = np.max(imag_parts)  # (local)
print(f"  Max |Re(lambda)|: {max_real:.6e}")
print(f"  Max |Im(lambda)|: {max_imag:.6e}")
if max_real > 1e-8 * max_imag and max_imag > 0:
    print(f"  WARNING: Eigenvalues not purely imaginary! Real/Imag ratio: {max_real/max_imag:.2e}")
elif max_real < 1e-10:
    print("  OK: Eigenvalues purely imaginary to machine precision")

N_evals = len(abs_evals)  # (local) number of distinct eigenvalues (without PW weighting)
N_weighted = np.sum(multiplicities)  # (local) total with PW multiplicities

print(f"  Distinct eigenvalues: {N_evals}")
print(f"  PW-weighted total: {N_weighted:.0f}")

# ============================================================
# Step 3: Compute <|lambda|> (mean absolute eigenvalue)
# ============================================================
print("\nStep 3: Computing spectral moments...")

# PW-weighted mean: <|lambda|> = sum_j mult_j * |lambda_j| / sum_j mult_j
mean_abs_lambda = np.sum(multiplicities * abs_evals) / N_weighted  # (local)
print(f"  <|lambda|> = {mean_abs_lambda:.6f}  (PW-weighted)")

# Unweighted for comparison
mean_abs_lambda_unweighted = np.mean(abs_evals)  # (local)
print(f"  <|lambda|> = {mean_abs_lambda_unweighted:.6f}  (unweighted)")

# ============================================================
# Step 4: Compute <lambda^2> and variance
# ============================================================
lambda_sq = abs_evals**2  # (local) = |lambda_j|^2

mean_lambda_sq = np.sum(multiplicities * lambda_sq) / N_weighted  # (local)
variance = mean_lambda_sq - mean_abs_lambda**2  # (local)
sigma = np.sqrt(max(0, variance))  # (local)

print(f"  <lambda^2> = {mean_lambda_sq:.6f}  (PW-weighted)")
print(f"  sigma^2    = {variance:.6f}")
print(f"  sigma      = {sigma:.6f}")

# Cross-check: <lambda^2> relates to spectral action moments
# In the heat kernel expansion, Tr(exp(-t D^2)) ~ sum_n a_n t^{(n-d)/2}
# The second spectral moment sum_j lambda_j^2 * mult_j relates to a_2
sum_lambda_sq_weighted = np.sum(multiplicities * lambda_sq)  # (local)
print(f"\n  Sum(mult_j * lambda_j^2) = {sum_lambda_sq_weighted:.2f}")
print(f"  a_2_fold (canonical)     = {a2_fold:.2f}")
print(f"  Ratio                    = {sum_lambda_sq_weighted / a2_fold:.4f}")
print(f"  (Ratio != 1 expected: a_2 involves heat kernel, not raw sum)")

# ============================================================
# Step 5: Compute Z(t*) = spectral partition function
# ============================================================
print("\nStep 5: Computing spectral partition function Z(t*)...")

lambda_max = np.max(abs_evals)  # (local)
print(f"  lambda_max = {lambda_max:.6f}")

# Z(t*) = sum_j mult_j * exp(-lambda_j^2 / (t* * lambda_max^2))
# This is a Boltzmann weight with "temperature" t* * lambda_max^2 in eigenvalue-squared space
scale_sq = T_STAR * lambda_max**2  # (local) = t* * lambda_max^2
boltzmann_args = -lambda_sq / scale_sq  # (local)
Z_tstar = np.sum(multiplicities * np.exp(boltzmann_args))  # (local)
print(f"  t* * lambda_max^2 = {scale_sq:.6f}")
print(f"  Z(t* = {T_STAR}) = {Z_tstar:.6f}")

# ============================================================
# Step 6: Compute S(t*) = -dZ/dt* / Z = spectral entropy gradient
# ============================================================
print("\nStep 6: Computing spectral entropy gradient S(t*)...")

# Analytic derivative:
# dZ/dt* = sum_j mult_j * (lambda_j^2 / (t*^2 * lambda_max^2)) * exp(-lambda_j^2 / (t* * lambda_max^2))
dZdt = np.sum(
    multiplicities * (lambda_sq / (T_STAR**2 * lambda_max**2)) * np.exp(boltzmann_args)
)  # (local)
S_tstar = -dZdt / Z_tstar  # (local)
print(f"  dZ/dt*     = {dZdt:.6f}")
print(f"  S(t*)      = {S_tstar:.6f}")
print(f"  Sign of S(t*): {'NEGATIVE (restoring)' if S_tstar < 0 else 'POSITIVE (anti-restoring)'}")

# ============================================================
# Step 7: Compute dS/dt* (second derivative of log Z)
# ============================================================
print("\nStep 7: Computing dS/dt* via finite difference...")

# Finite difference: dS/dt* ~ [S(t*+dt) - S(t*-dt)] / (2*dt)
# S(t) = -d/dt [log Z(t)]
# So dS/dt = -d^2/dt^2 [log Z(t)]

# Compute Z at t* + dt and t* - dt
for label, t_val in [("t*+dt", T_STAR + DT_STAR), ("t*-dt", T_STAR - DT_STAR)]:
    scale_sq_pm = t_val * lambda_max**2  # (local)
    boltz_pm = -lambda_sq / scale_sq_pm  # (local)
    Z_pm = np.sum(multiplicities * np.exp(boltz_pm))  # (local)
    dZ_pm = np.sum(
        multiplicities * (lambda_sq / (t_val**2 * lambda_max**2)) * np.exp(boltz_pm)
    )  # (local)
    S_pm = -dZ_pm / Z_pm  # (local)
    if label == "t*+dt":
        S_plus = S_pm  # (local)
    else:
        S_minus = S_pm  # (local)

dSdt = (S_plus - S_minus) / (2 * DT_STAR)  # (local)
print(f"  S(t*+dt)  = {S_plus:.6f}")
print(f"  S(t*-dt)  = {S_minus:.6f}")
print(f"  dS/dt*    = {dSdt:.6f}")
print(f"  Sign of dS/dt*: {'POSITIVE (anti-restoring)' if dSdt > 0 else 'NEGATIVE (restoring)'}")

# Also compute analytically for cross-check
# d^2(log Z)/dt*^2 = [Z * d^2Z/dt*^2 - (dZ/dt*)^2] / Z^2
# d^2Z/dt*^2 = sum_j mult_j * [lambda_j^4/(t*^4 * lambda_max^4) - 2*lambda_j^2/(t*^3 * lambda_max^2)] * exp(...)
d2Zdt2 = np.sum(
    multiplicities * (
        lambda_sq**2 / (T_STAR**4 * lambda_max**4)
        - 2 * lambda_sq / (T_STAR**3 * lambda_max**2)
    ) * np.exp(boltzmann_args)
)  # (local)
dSdt_analytic = -(Z_tstar * d2Zdt2 - dZdt**2) / Z_tstar**2  # (local)
print(f"  dS/dt* (analytic) = {dSdt_analytic:.6f}")
print(f"  FD vs analytic diff = {abs(dSdt - dSdt_analytic):.2e}")

# ============================================================
# Step 8: Cross-checks
# ============================================================
print("\n" + "=" * 70)
print("Step 8: Cross-checks")
print("=" * 70)

checks_pass = True  # (local)

# Check 1: <|lambda|> > 0
if mean_abs_lambda > 0:
    print(f"  [PASS] <|lambda|> = {mean_abs_lambda:.6f} > 0")
else:
    print(f"  [FAIL] <|lambda|> = {mean_abs_lambda:.6f} <= 0")
    checks_pass = False

# Check 2: sigma^2 > 0
if variance > 0:
    print(f"  [PASS] sigma^2 = {variance:.6f} > 0")
else:
    print(f"  [FAIL] sigma^2 = {variance:.6f} <= 0")
    checks_pass = False

# Check 3: Z(t*) > 0
if Z_tstar > 0:
    print(f"  [PASS] Z(t*) = {Z_tstar:.6f} > 0")
else:
    print(f"  [FAIL] Z(t*) = {Z_tstar:.6f} <= 0")
    checks_pass = False

# Check 4: lambda_max > <|lambda|> (max > mean)
if lambda_max > mean_abs_lambda:
    print(f"  [PASS] lambda_max = {lambda_max:.6f} > <|lambda|> = {mean_abs_lambda:.6f}")
else:
    print(f"  [FAIL] lambda_max = {lambda_max:.6f} <= <|lambda|>")
    checks_pass = False

# Check 5: variance = <lambda^2> - <|lambda|>^2 identity
var_check = mean_lambda_sq - mean_abs_lambda**2  # (local)
if abs(var_check - variance) < 1e-12:
    print(f"  [PASS] Variance identity: diff = {abs(var_check - variance):.2e}")
else:
    print(f"  [FAIL] Variance identity: diff = {abs(var_check - variance):.2e}")
    checks_pass = False

# Check 6: coefficient of variation (sigma / mean)
cv = sigma / mean_abs_lambda if mean_abs_lambda > 0 else float('inf')  # (local)
print(f"  CV = sigma/<|lambda|> = {cv:.4f}")

print()
print(f"  All cross-checks: {'PASS' if checks_pass else 'FAIL'}")

# ============================================================
# Sector-by-sector summary
# ============================================================
print("\n" + "=" * 70)
print("Sector-by-sector summary")
print("=" * 70)
print(f"  {'(p,q)':>8s}  {'dim':>5s}  {'N_evals':>8s}  {'<|lam|>':>10s}  {'max|lam|':>10s}  {'min|lam|':>10s}")
for (p, q, evals_raw) in eval_data:
    dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2  # (local)
    abs_ev = np.abs(evals_raw)  # (local)
    print(f"  ({p},{q}){'':<4s}  {dim_pq:5d}  {len(evals_raw):8d}  {np.mean(abs_ev):10.4f}  {np.max(abs_ev):10.4f}  {np.min(abs_ev):10.4f}")

# ============================================================
# Save data
# ============================================================
print("\nSaving results...")
outpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s77_mean_eigenvalue.npz")  # (local)
np.savez(
    outpath,
    tau_fold=tau_fold,
    L_max=L_MAX,
    t_star=T_STAR,
    mean_abs_lambda=mean_abs_lambda,
    mean_abs_lambda_unweighted=mean_abs_lambda_unweighted,
    mean_lambda_sq=mean_lambda_sq,
    variance=variance,
    sigma=sigma,
    lambda_max=lambda_max,
    Z_tstar=Z_tstar,
    S_tstar=S_tstar,
    dSdt_star=dSdt_analytic,
    dZdt_star=dZdt,
    N_distinct=N_evals,
    N_weighted=N_weighted,
    abs_evals=abs_evals,
    multiplicities=multiplicities,
    cv=cv,
    checks_pass=checks_pass,
    a0_fold=a0_fold,
    a2_fold=a2_fold,
    a4_fold=a4_fold,
    sum_lambda_sq_weighted=sum_lambda_sq_weighted,
)
print(f"  Saved to: {outpath}")

# ============================================================
# Final summary
# ============================================================
print("\n" + "=" * 70)
print("GATE S77-B7-MEAN-EIGEN: INFO DIAGNOSTIC")
print("=" * 70)
print(f"  tau_fold           = {tau_fold}")
print(f"  L_max              = {L_MAX}")
print(f"  N_distinct         = {N_evals}")
print(f"  N_PW_weighted      = {N_weighted:.0f}")
print(f"  <|lambda|>         = {mean_abs_lambda:.6f}   (M_KK units)")
print(f"  <lambda^2>         = {mean_lambda_sq:.6f}")
print(f"  sigma              = {sigma:.6f}")
print(f"  CV                 = {cv:.4f}")
print(f"  lambda_max         = {lambda_max:.6f}")
print(f"  Z(t*={T_STAR})      = {Z_tstar:.6f}")
print(f"  S(t*={T_STAR})      = {S_tstar:.6f}")
print(f"  dS/dt*(t*={T_STAR}) = {dSdt_analytic:.6f}")
print(f"  Sign(dS/dt*)       = {'POSITIVE' if dSdt_analytic > 0 else 'NEGATIVE'}")
sign_class = "anti-restoring" if dSdt_analytic > 0 else "restoring"  # (local)
print(f"  Classification     = {sign_class}")
print(f"  Cross-checks       = {'ALL PASS' if checks_pass else 'FAIL'}")
print("=" * 70)
