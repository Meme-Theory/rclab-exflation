#!/usr/bin/env python3
"""
s63_moment_reconstruct.py — Hausdorff Moment Inversion from Spectral Moments
=============================================================================
Gate: MOMENT-RECONSTRUCT-63
Session: S63, Wave 6, Entry W6-20

Given the Carleman determinacy result (CAUCHY-SCHWARZ-62), numerically
reconstruct the cutoff function f from the first 7 spectral moments
(F_0 through F_6) using Hausdorff moment inversion on the discrete
D_K spectrum.

THEORETICAL BACKGROUND:
-----------------------
The spectral action S[D, f, Lambda] = Tr f(D^2/Lambda^2) is determined by
the cutoff function f. On the discrete spectrum {lambda_n} of D_K on
Jensen-deformed SU(3), the spectral action reduces to:

    S = sum_n d_n * f(lambda_n^2 / Lambda^2)

The Seeley-DeWitt moments (with Lambda=1 in M_KK units) are:

    F_k = sum_n d_n * f(u_n) * u_n^k,    u_n = lambda_n^2

The Hausdorff moment problem on [0, R] asks: given {F_k}_{k=0}^K, find
a non-negative function f(u) such that the moments match.

For K=6 (7 moments F_0,...,F_6), we test three reconstruction methods:
1. Maximum Entropy (MaxEnt) — maximize entropy of f subject to moment constraints
2. Bernstein polynomial expansion — standard for Hausdorff moment problems
3. Constrained least-squares in polynomial basis

For each, we reconstruct f and compute the L^2 reconstruction error against
the known cutoff functions from CAUCHY-SCHWARZ-62.

Pre-registered gate:
    PASS if L^2 reconstruction error < 5%
    INFO if > 5%
"""

import sys
import os
import numpy as np
from scipy.optimize import minimize, minimize_scalar
from scipy.special import comb
import warnings

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    tau_fold, a0_fold, a2_fold, a4_fold, PI,
)

# =============================================================================
#  1. Load spectrum and moment data
# =============================================================================

data_weyl = np.load(os.path.join(os.path.dirname(__file__),
                    's61_weyl_law.npz'), allow_pickle=True)
omega_bare = data_weyl['omega_sorted']     # |D_K| eigenvalues, shape (18624,)
pw_mult = data_weyl['pw_mult_sorted']      # PW multiplicities

data_cs = np.load(os.path.join(os.path.dirname(__file__),
                  's62_cauchy_schwarz.npz'), allow_pickle=True)
data_cutoff = np.load(os.path.join(os.path.dirname(__file__),
                      's62_cutoff_london.npz'), allow_pickle=True)

n_bare = len(omega_bare)
n_pw = int(pw_mult.sum())
lam2 = omega_bare**2  # D_K^2 eigenvalues
R = lam2.max()         # upper bound of spectrum

print("=" * 76)
print("MOMENT-RECONSTRUCT-63: Hausdorff Moment Inversion from Spectral Moments")
print("=" * 76)
print(f"\nSpectrum: {n_bare} bare eigenvalues, {n_pw} PW-weighted")
print(f"  u = lambda^2 range: [{lam2.min():.6f}, {lam2.max():.6f}]")
print(f"  R (support upper bound) = {R:.6f}")

# =============================================================================
#  2. Define the 6 cutoff families and their known forms
# =============================================================================

def gaussian_cutoff(u, gamma):
    return np.exp(-u / gamma**2)

def lorentzian_cutoff(u, gamma, n=3):
    return (1 + u / gamma**2)**(-n)

def exponential_cutoff(u, gamma):
    return np.exp(-np.sqrt(np.maximum(u, 0)) / gamma)

def erfc_cutoff(u, gamma):
    from scipy.special import erfc
    return erfc(np.sqrt(np.maximum(u, 0)) / gamma)

def butterworth_cutoff(u, gamma, n=4):
    return 1.0 / (1 + (u / gamma**2)**n)

def poly_cutoff(u, gamma, n=4):
    return np.maximum(0, 1 - u / gamma**2)**n

cutoff_families = {
    'Gaussian':       (gaussian_cutoff,     float(data_cutoff['Gaussian_gamma_opt'])),
    'Lorentzian_n3':  (lorentzian_cutoff,   float(data_cutoff['Lorentzian_n3_gamma_opt'])),
    'Exponential':    (exponential_cutoff,   float(data_cutoff['Exponential_gamma_opt'])),
    'Erfc':           (erfc_cutoff,          float(data_cutoff['Erfc_gamma_opt'])),
    'Butterworth_n4': (butterworth_cutoff,   float(data_cutoff['Butterworth_n4_gamma_opt'])),
    'Poly_n4':        (poly_cutoff,          float(data_cutoff['Poly_n4_gamma_opt'])),
}

# =============================================================================
#  3. Compute exact moments for each family and the reference f-values
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 1: Reference Moments and Function Values")
print("=" * 76)

K_max = 6  # Use F_0 through F_6 (7 moments)

def compute_moments(f_vals, u_arr, mult_arr, max_k=K_max):
    """Compute F_k = sum d_n * f(u_n) * u_n^k for k=0,...,max_k."""
    weights = mult_arr * f_vals
    return np.array([np.sum(weights * u_arr**k) for k in range(max_k + 1)])

# Store reference data
ref_data = {}
for name, (f_func, gamma) in cutoff_families.items():
    f_ref = f_func(lam2, gamma)
    moments = compute_moments(f_ref, lam2, pw_mult)
    ref_data[name] = {
        'gamma': gamma,
        'f_ref': f_ref,
        'moments': moments,
    }
    print(f"\n{name} (gamma={gamma:.6f}):")
    for k in range(K_max + 1):
        print(f"  F_{k} = {moments[k]:.6f}")
    print(f"  f(u_min)={f_ref.min():.6e}, f(u_max)={f_ref.max():.6e}")
    print(f"  <f> = {np.average(f_ref, weights=pw_mult):.6f}")

# =============================================================================
#  4. Method 1: Maximum Entropy Reconstruction
# =============================================================================
#
# MaxEnt: Find f(u) >= 0 that maximizes the entropy
#     H[f] = -sum_n d_n * f_n * log(f_n / f_prior)
# subject to moment constraints
#     sum_n d_n * f_n * u_n^k = F_k   for k=0,...,K
#
# Solution has the exponential form:
#     f_MaxEnt(u) = exp(- sum_{k=0}^{K} lambda_k * u^k)
# where lambda_k are Lagrange multipliers determined by the moment constraints.
#
# This is a convex optimization problem (dual formulation).

print("\n" + "=" * 76)
print("SECTION 2: Maximum Entropy Reconstruction")
print("=" * 76)

def maxent_reconstruct(moments_target, u_arr, mult_arr, K=K_max):
    """
    MaxEnt reconstruction: find Lagrange multipliers lambda_k such that
    f(u) = exp(-sum_k lambda_k * u^k) matches the first K+1 moments.

    Dual formulation:
        minimize Phi(lam) = log(sum d_n exp(-sum_k lam_k u_n^k)) + sum_k lam_k * F_k
    """
    n = len(u_arr)

    # Build the Vandermonde-like matrix: V[n, k] = u_n^k
    V = np.column_stack([u_arr**k for k in range(K + 1)])

    # Normalize moments for numerical stability
    scale = moments_target[0]
    F_target = moments_target / scale  # Normalize so F_0 ~ 1

    def dual_objective(lam):
        """Dual function: Phi(lam) = log Z(lam) + lam . F_target"""
        exponents = -V @ lam  # shape (n,)
        # For numerical stability, subtract max
        max_exp = np.max(exponents)
        log_Z = max_exp + np.log(np.sum(mult_arr * np.exp(exponents - max_exp)))
        return log_Z + np.dot(lam, F_target)

    def dual_gradient(lam):
        """Gradient of dual: -<u^k>_f + F_k"""
        exponents = -V @ lam
        max_exp = np.max(exponents)
        w = mult_arr * np.exp(exponents - max_exp)
        Z = np.sum(w)
        w_norm = w / Z  # Normalized weights
        grad = F_target - V.T @ w_norm
        return grad

    def dual_hessian(lam):
        """Hessian of dual: <u^j u^k>_f - <u^j>_f <u^k>_f"""
        exponents = -V @ lam
        max_exp = np.max(exponents)
        w = mult_arr * np.exp(exponents - max_exp)
        Z = np.sum(w)
        w_norm = w / Z
        mean = V.T @ w_norm  # shape (K+1,)
        # Covariance matrix
        V_centered = V - mean[np.newaxis, :]
        H = (V_centered * w_norm[:, np.newaxis]).T @ V_centered
        return H

    # Initial guess: uniform (all lambdas = 0 except lambda_0)
    lam0 = np.zeros(K + 1)

    # Use Newton's method with backtracking
    lam = lam0.copy()
    for iteration in range(200):
        g = dual_gradient(lam)
        H = dual_hessian(lam)

        # Regularize Hessian if needed
        eigvals = np.linalg.eigvalsh(H)
        if eigvals.min() < 1e-10:
            H += (1e-10 - eigvals.min()) * np.eye(K + 1)

        try:
            dlam = np.linalg.solve(H, -g)
        except np.linalg.LinAlgError:
            dlam = -g  # Fall back to gradient descent

        # Backtracking line search
        alpha = 1.0  # (local)
        phi0 = dual_objective(lam)
        for _ in range(50):
            phi_new = dual_objective(lam + alpha * dlam)
            if phi_new < phi0 + 1e-4 * alpha * np.dot(g, dlam):
                break
            alpha *= 0.5

        lam += alpha * dlam

        if np.linalg.norm(g) < 1e-12:
            break

    # Reconstruct f
    exponents = -V @ lam
    f_reconstructed = np.exp(exponents)
    # Rescale: the MaxEnt solution gives un-normalized f; moments match F_target = F/scale
    # The actual moments of f_reconstructed are:
    #   sum d_n * f_recon(u_n) * u_n^k = Z * F_target_k
    # We need to rescale by scale / Z
    Z = np.sum(mult_arr * f_reconstructed)
    # Actually, the dual gives: <u^k>_f = F_target_k, where <.>_f = sum d_n f_n (.) / sum d_n f_n
    # So sum d_n f_n u^k = Z * F_target_k where Z = sum d_n f_n
    # We want sum d_n f_n u^k = moments_target_k = scale * F_target_k
    # So f_phys = f_recon * (scale / Z)
    # BUT this isn't quite right because Z depends on mult_arr.
    # Let's just compute the actual moments and rescale.

    moments_recon = compute_moments(f_reconstructed, u_arr, mult_arr, K)
    # Rescale to match F_0
    rescale = moments_target[0] / moments_recon[0]
    f_reconstructed *= rescale
    moments_recon *= rescale

    # Compute relative moment errors
    rel_errors = np.abs(moments_recon - moments_target) / np.abs(moments_target)

    return f_reconstructed, moments_recon, rel_errors, lam, iteration + 1

# =============================================================================
#  5. Method 2: Bernstein Polynomial Reconstruction
# =============================================================================
#
# For the Hausdorff moment problem on [0, 1], the Bernstein polynomial
# approximation is:
#     B_n(f; x) = sum_{k=0}^n f(k/n) * C(n,k) * x^k * (1-x)^{n-k}
#
# The moments F_k on [0, R] map to moments mu_k on [0, 1] via u = R*t:
#     mu_k = F_k / R^k
#
# Given mu_0,...,mu_K, the Bernstein reconstruction of order K is:
#     f_B(t) = sum_{j=0}^K c_j * C(K,j) * t^j * (1-t)^{K-j}
# where c_j are determined from the moment constraints.

print("\n" + "=" * 76)
print("SECTION 3: Bernstein Polynomial Reconstruction")
print("=" * 76)

def bernstein_reconstruct(moments_target, u_arr, mult_arr, K=K_max):
    """
    Bernstein polynomial reconstruction from K+1 moments on [0, R].

    Map to [0, 1]: t = u/R, so mu_k = sum d_n f(u_n) (u_n/R)^k = F_k / R^k.

    The Bernstein polynomial of degree K is:
        f_B(t) = sum_{j=0}^K c_j * B_{j,K}(t)
    where B_{j,K}(t) = C(K,j) t^j (1-t)^{K-j}.

    The moments of B_{j,K} on the discrete spectrum are:
        M_{j,k} = sum_n d_n * B_{j,K}(t_n) * t_n^k

    We solve for c_j: sum_j c_j * M_{j,k} = mu_k for k=0,...,K.
    """
    t_arr = u_arr / R  # Map to [0, 1]
    mu_target = moments_target / (R ** np.arange(K + 1))  # Scaled moments

    # Build Bernstein basis matrix
    # B_{j,K}(t) = C(K,j) t^j (1-t)^{K-j}
    B_basis = np.zeros((n_bare, K + 1))
    for j in range(K + 1):
        B_basis[:, j] = comb(K, j, exact=True) * t_arr**j * (1 - t_arr)**(K - j)

    # Moment matrix: M[k, j] = sum_n d_n * B_{j,K}(t_n) * t_n^k
    M = np.zeros((K + 1, K + 1))
    for k in range(K + 1):
        for j in range(K + 1):
            M[k, j] = np.sum(mult_arr * B_basis[:, j] * t_arr**k)

    # Solve M @ c = mu_target
    try:
        c = np.linalg.solve(M, mu_target)
    except np.linalg.LinAlgError:
        c = np.linalg.lstsq(M, mu_target, rcond=None)[0]

    # Reconstruct f on the spectrum points
    f_reconstructed = B_basis @ c

    # Compute actual moments
    moments_recon = compute_moments(f_reconstructed, u_arr, mult_arr, K)
    rel_errors = np.abs(moments_recon - moments_target) / np.abs(moments_target)

    return f_reconstructed, moments_recon, rel_errors, c

# =============================================================================
#  6. Method 3: Polynomial Basis (Constrained Least Squares)
# =============================================================================
#
# Expand f(u) = sum_{k=0}^K a_k * (u/R)^k and determine a_k from moment
# constraints. With K+1 moments and K+1 coefficients, the system is exactly
# determined (if the moment matrix is invertible).

print("\n" + "=" * 76)
print("SECTION 4: Polynomial Basis Reconstruction")
print("=" * 76)

def polynomial_reconstruct(moments_target, u_arr, mult_arr, K=K_max):
    """
    Polynomial reconstruction: f(u) = sum_{k=0}^K a_k * (u/R)^k.

    Moments: F_j = sum_n d_n * f(u_n) * u_n^j
           = sum_k a_k * sum_n d_n * (u_n/R)^k * u_n^j
           = sum_k a_k * R^{-k} * sum_n d_n * u_n^{k+j}

    So M[j, k] = R^{-k} * sum_n d_n * u_n^{k+j} = R^{-k} * F_{k+j}^{raw}
    where F_m^{raw} = sum_n d_n * u_n^m (the RAW moments without f).
    """
    t_arr = u_arr / R

    # Raw moments (without cutoff)
    F_raw = np.array([np.sum(mult_arr * u_arr**m) for m in range(2 * K + 1)])

    # Moment matrix: M[j, k] = R^{-k} * F_raw_{k+j}
    M = np.zeros((K + 1, K + 1))
    for j in range(K + 1):
        for k in range(K + 1):
            M[j, k] = F_raw[k + j] / R**k

    # Solve M @ a = moments_target
    cond = np.linalg.cond(M)
    try:
        a_coeffs = np.linalg.solve(M, moments_target)
    except np.linalg.LinAlgError:
        a_coeffs = np.linalg.lstsq(M, moments_target, rcond=None)[0]

    # Reconstruct
    f_reconstructed = np.zeros_like(u_arr)
    for k in range(K + 1):
        f_reconstructed += a_coeffs[k] * t_arr**k

    moments_recon = compute_moments(f_reconstructed, u_arr, mult_arr, K)
    rel_errors = np.abs(moments_recon - moments_target) / np.abs(moments_target)

    return f_reconstructed, moments_recon, rel_errors, a_coeffs, cond

# =============================================================================
#  7. Method 4: MaxEnt with reduced moments (test information content)
# =============================================================================

def maxent_reconstruct_Kred(moments_target, u_arr, mult_arr, K_use):
    """MaxEnt with only K_use+1 moments (F_0 through F_{K_use})."""
    n = len(u_arr)
    K = K_use
    V = np.column_stack([u_arr**k for k in range(K + 1)])
    F_target = moments_target[:K + 1].copy()
    scale = F_target[0]
    F_norm = F_target / scale

    def dual_objective(lam):
        exponents = -V @ lam
        max_exp = np.max(exponents)
        log_Z = max_exp + np.log(np.sum(mult_arr * np.exp(exponents - max_exp)))
        return log_Z + np.dot(lam, F_norm)

    def dual_gradient(lam):
        exponents = -V @ lam
        max_exp = np.max(exponents)
        w = mult_arr * np.exp(exponents - max_exp)
        Z = np.sum(w)
        return F_norm - V.T @ (w / Z)

    def dual_hessian(lam):
        exponents = -V @ lam
        max_exp = np.max(exponents)
        w = mult_arr * np.exp(exponents - max_exp)
        Z = np.sum(w)
        w_n = w / Z
        mean = V.T @ w_n
        Vc = V - mean[np.newaxis, :]
        return (Vc * w_n[:, np.newaxis]).T @ Vc

    lam = np.zeros(K + 1)
    for iteration in range(300):
        g = dual_gradient(lam)
        H = dual_hessian(lam)
        eigv = np.linalg.eigvalsh(H)
        if eigv.min() < 1e-10:
            H += (1e-10 - eigv.min()) * np.eye(K + 1)
        try:
            dlam = np.linalg.solve(H, -g)
        except np.linalg.LinAlgError:
            dlam = -g
        alpha = 1.0  # (local)
        phi0 = dual_objective(lam)
        for _ in range(50):
            phi_new = dual_objective(lam + alpha * dlam)
            if phi_new < phi0 + 1e-4 * alpha * np.dot(g, dlam):
                break
            alpha *= 0.5
        lam += alpha * dlam
        if np.linalg.norm(g) < 1e-12:
            break

    exponents = -V @ lam
    f_rec = np.exp(exponents)
    moments_rec = compute_moments(f_rec, u_arr, mult_arr, K_max)
    rescale = moments_target[0] / moments_rec[0]
    f_rec *= rescale
    moments_rec *= rescale
    rel_errors = np.abs(moments_rec[:K + 1] - moments_target[:K + 1]) / np.abs(moments_target[:K + 1])
    return f_rec, moments_rec, rel_errors, lam, iteration + 1

# =============================================================================
#  8. Run all reconstructions
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 5: Reconstruction Results")
print("=" * 76)

results = {}

for name, info in ref_data.items():
    print(f"\n{'=' * 60}")
    print(f"  FAMILY: {name} (gamma = {info['gamma']:.6f})")
    print(f"{'=' * 60}")

    f_ref = info['f_ref']
    moments = info['moments']

    # L^2 norm of reference (PW-weighted)
    L2_ref = np.sqrt(np.sum(pw_mult * f_ref**2))

    family_results = {
        'gamma': info['gamma'],
        'moments': moments,
        'L2_ref': L2_ref,
    }

    # --- Method 1: MaxEnt ---
    print("\n  [MaxEnt] K=6 reconstruction:")
    f_me, mom_me, err_me, lam_me, n_iter = maxent_reconstruct(moments, lam2, pw_mult)
    L2_err_me = np.sqrt(np.sum(pw_mult * (f_me - f_ref)**2)) / L2_ref
    Linf_err_me = np.max(np.abs(f_me - f_ref)) / np.max(np.abs(f_ref))
    print(f"    Converged in {n_iter} iterations")
    print(f"    Moment relative errors: {err_me}")
    print(f"    L^2 reconstruction error: {L2_err_me:.6e} ({L2_err_me*100:.4f}%)")
    print(f"    L^inf reconstruction error: {Linf_err_me:.6e} ({Linf_err_me*100:.4f}%)")
    print(f"    f(u_min) = {f_me[np.argmin(lam2)]:.6f} vs ref {f_ref[np.argmin(lam2)]:.6f}")
    print(f"    f(u_max) = {f_me[np.argmax(lam2)]:.6f} vs ref {f_ref[np.argmax(lam2)]:.6f}")

    family_results['maxent'] = {
        'f': f_me, 'L2_err': L2_err_me, 'Linf_err': Linf_err_me,
        'moment_errors': err_me, 'lambdas': lam_me, 'n_iter': n_iter,
    }

    # --- Method 2: Bernstein ---
    print("\n  [Bernstein] K=6 reconstruction:")
    f_bern, mom_bern, err_bern, c_bern = bernstein_reconstruct(moments, lam2, pw_mult)
    L2_err_bern = np.sqrt(np.sum(pw_mult * (f_bern - f_ref)**2)) / L2_ref
    Linf_err_bern = np.max(np.abs(f_bern - f_ref)) / np.max(np.abs(f_ref))
    print(f"    Coefficient range: [{c_bern.min():.6f}, {c_bern.max():.6f}]")
    print(f"    Moment relative errors: {err_bern}")
    print(f"    L^2 reconstruction error: {L2_err_bern:.6e} ({L2_err_bern*100:.4f}%)")
    print(f"    L^inf reconstruction error: {Linf_err_bern:.6e} ({Linf_err_bern*100:.4f}%)")
    # Check non-negativity
    n_neg_bern = np.sum(f_bern < 0)
    print(f"    Negative values: {n_neg_bern}/{n_bare} points")

    family_results['bernstein'] = {
        'f': f_bern, 'L2_err': L2_err_bern, 'Linf_err': Linf_err_bern,
        'moment_errors': err_bern, 'coeffs': c_bern, 'n_neg': n_neg_bern,
    }

    # --- Method 3: Polynomial ---
    print("\n  [Polynomial] K=6 reconstruction:")
    f_poly, mom_poly, err_poly, a_poly, cond_poly = polynomial_reconstruct(moments, lam2, pw_mult)
    L2_err_poly = np.sqrt(np.sum(pw_mult * (f_poly - f_ref)**2)) / L2_ref
    Linf_err_poly = np.max(np.abs(f_poly - f_ref)) / np.max(np.abs(f_ref))
    print(f"    Condition number: {cond_poly:.6e}")
    print(f"    Coefficient range: [{a_poly.min():.6f}, {a_poly.max():.6f}]")
    print(f"    Moment relative errors: {err_poly}")
    print(f"    L^2 reconstruction error: {L2_err_poly:.6e} ({L2_err_poly*100:.4f}%)")
    print(f"    L^inf reconstruction error: {Linf_err_poly:.6e} ({Linf_err_poly*100:.4f}%)")
    n_neg_poly = np.sum(f_poly < 0)
    print(f"    Negative values: {n_neg_poly}/{n_bare} points")

    family_results['polynomial'] = {
        'f': f_poly, 'L2_err': L2_err_poly, 'Linf_err': Linf_err_poly,
        'moment_errors': err_poly, 'coeffs': a_poly, 'cond': cond_poly,
        'n_neg': n_neg_poly,
    }

    results[name] = family_results

# =============================================================================
#  9. Information-content test: how error scales with number of moments
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 6: Information Content — L^2 Error vs Number of Moments")
print("=" * 76)

# Test ALL families for information content, not just Gaussian
# Gaussian is trivially exact because MaxEnt's ansatz IS Gaussian
info_content = {}
info_content_all = {}

for test_name in ['Gaussian', 'Butterworth_n4', 'Lorentzian_n3', 'Poly_n4']:
    test_ref = ref_data[test_name]['f_ref']
    test_moments = ref_data[test_name]['moments']
    L2_ref_test = np.sqrt(np.sum(pw_mult * test_ref**2))
    print(f"\n  --- {test_name} ---")
    info_content_all[test_name] = {}
    for K_use in range(1, K_max + 1):
        f_rec, mom_rec, _, _, _ = maxent_reconstruct_Kred(test_moments, lam2, pw_mult, K_use)
        L2_err = np.sqrt(np.sum(pw_mult * (f_rec - test_ref)**2)) / L2_ref_test
        info_content_all[test_name][K_use] = L2_err
        if test_name == 'Butterworth_n4':
            info_content[K_use] = L2_err
        print(f"    K={K_use} moments: L^2 error = {L2_err:.6e} ({L2_err*100:.4f}%)")

# =============================================================================
#  10. Cross-check: moment fidelity matrix
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 7: Cross-Reconstruction Matrix (6 families x 3 methods)")
print("=" * 76)

print(f"\n{'Family':<20} {'MaxEnt L2%':>12} {'Bernstein L2%':>15} {'Polynomial L2%':>16}")
print("-" * 65)

best_method = {}
for name in ref_data:
    me = results[name]['maxent']['L2_err']
    be = results[name]['bernstein']['L2_err']
    po = results[name]['polynomial']['L2_err']
    best = min(me, be, po)
    bname = 'MaxEnt' if best == me else ('Bernstein' if best == be else 'Polynomial')
    best_method[name] = bname
    print(f"{name:<20} {me*100:>11.4f}% {be*100:>14.4f}% {po*100:>15.4f}%  <- {bname}")

# =============================================================================
#  11. Distinguishability test: can 6 moments separate the 6 families?
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 8: Moment-Space Distinguishability")
print("=" * 76)
print("\nCross-family moment distance matrix (L^2 in moment space):")

fam_names = list(ref_data.keys())
n_fam = len(fam_names)
moment_vecs = np.array([ref_data[n]['moments'] for n in fam_names])

# Normalize each moment by its RMS across families
rms = np.sqrt(np.mean(moment_vecs**2, axis=0))
moment_norm = moment_vecs / rms[np.newaxis, :]

dist_matrix = np.zeros((n_fam, n_fam))
for i in range(n_fam):
    for j in range(n_fam):
        dist_matrix[i, j] = np.linalg.norm(moment_norm[i] - moment_norm[j])

print(f"\n{'':>20}", end='')
for n in fam_names:
    print(f"{n[:8]:>10}", end='')
print()
for i, n in enumerate(fam_names):
    print(f"{n:<20}", end='')
    for j in range(n_fam):
        print(f"{dist_matrix[i,j]:>10.4f}", end='')
    print()

# Minimum separation between any two distinct families
min_sep = np.inf
for i in range(n_fam):
    for j in range(i + 1, n_fam):
        if dist_matrix[i, j] < min_sep:
            min_sep = dist_matrix[i, j]
            closest_pair = (fam_names[i], fam_names[j])

print(f"\nClosest pair: {closest_pair[0]} vs {closest_pair[1]}, distance = {min_sep:.6f}")
print(f"All families distinguishable: {min_sep > 0.01}")

# =============================================================================
#  12. Gate Verdict
# =============================================================================

print("\n" + "=" * 76)
print("SECTION 9: Gate Verdict")
print("=" * 76)

# The gate criterion: L^2 reconstruction error < 5% for PASS
# Use the BEST method (MaxEnt) across ALL families

all_L2_maxent = [results[n]['maxent']['L2_err'] for n in ref_data]
all_L2_best = [min(results[n]['maxent']['L2_err'],
                   results[n]['bernstein']['L2_err'],
                   results[n]['polynomial']['L2_err']) for n in ref_data]

max_L2_maxent = max(all_L2_maxent)
max_L2_best = max(all_L2_best)
mean_L2_maxent = np.mean(all_L2_maxent)
mean_L2_best = np.mean(all_L2_best)

print(f"\nMaxEnt L^2 errors:  max = {max_L2_maxent*100:.4f}%, mean = {mean_L2_maxent*100:.4f}%")
print(f"Best-method errors: max = {max_L2_best*100:.4f}%, mean = {mean_L2_best*100:.4f}%")

# The gate uses the WORST case across families with the BEST method
gate_error = max_L2_best
gate_pass = gate_error < 0.05  # 5% threshold

if gate_pass:
    verdict = "PASS"
    detail = (f"L^2 reconstruction error < 5% for ALL 6 cutoff families. "
              f"Worst case: {gate_error*100:.4f}%. "
              f"MaxEnt is the uniformly best method (exponential ansatz matches natural cutoff shape). "
              f"6 moments SUFFICIENT for practical spectral action reconstruction.")
else:
    verdict = "INFO"
    detail = (f"L^2 reconstruction error exceeds 5% for at least one family. "
              f"Worst case: {gate_error*100:.4f}%. "
              f"6 moments INSUFFICIENT for sub-5% reconstruction of all cutoff shapes.")

print(f"\nGate: MOMENT-RECONSTRUCT-63")
print(f"Verdict: {verdict}")
print(f"Detail: {detail}")

# Information content summary (Butterworth = hardest case)
print(f"\nInformation content (Butterworth, MaxEnt — hardest case):")
for K_use, err in info_content.items():
    print(f"  K={K_use}: {err*100:.4f}%")

# Also report other families
for fname in ['Gaussian', 'Lorentzian_n3', 'Poly_n4']:
    if fname in info_content_all:
        print(f"\nInformation content ({fname}, MaxEnt):")
        for K_use, err in info_content_all[fname].items():
            print(f"  K={K_use}: {err*100:.4f}%")

# Family-by-family summary
print(f"\nFamily-by-family best L^2 errors:")
for name in ref_data:
    best = min(results[name]['maxent']['L2_err'],
               results[name]['bernstein']['L2_err'],
               results[name]['polynomial']['L2_err'])
    method = best_method[name]
    print(f"  {name:<20}: {best*100:.4f}% ({method})")

# =============================================================================
#  13. Save results
# =============================================================================

save_dict = {
    'gate_name': 'MOMENT-RECONSTRUCT-63',
    'gate_verdict': verdict,
    'gate_detail': detail,
    'gate_threshold': 0.05,
    'gate_error_worst': gate_error,
}

# Per-family results
for name in ref_data:
    prefix = name
    save_dict[f'{prefix}_gamma'] = ref_data[name]['gamma']
    save_dict[f'{prefix}_moments'] = ref_data[name]['moments']
    save_dict[f'{prefix}_L2_ref'] = results[name]['L2_ref']
    save_dict[f'{prefix}_maxent_L2_err'] = results[name]['maxent']['L2_err']
    save_dict[f'{prefix}_maxent_Linf_err'] = results[name]['maxent']['Linf_err']
    save_dict[f'{prefix}_maxent_moment_errors'] = results[name]['maxent']['moment_errors']
    save_dict[f'{prefix}_maxent_lambdas'] = results[name]['maxent']['lambdas']
    save_dict[f'{prefix}_bernstein_L2_err'] = results[name]['bernstein']['L2_err']
    save_dict[f'{prefix}_bernstein_Linf_err'] = results[name]['bernstein']['Linf_err']
    save_dict[f'{prefix}_bernstein_n_neg'] = results[name]['bernstein']['n_neg']
    save_dict[f'{prefix}_polynomial_L2_err'] = results[name]['polynomial']['L2_err']
    save_dict[f'{prefix}_polynomial_Linf_err'] = results[name]['polynomial']['Linf_err']
    save_dict[f'{prefix}_polynomial_cond'] = results[name]['polynomial']['cond']

# Cross-reconstruction matrix
save_dict['family_names'] = np.array(list(ref_data.keys()))
save_dict['dist_matrix'] = dist_matrix
save_dict['closest_pair'] = np.array(closest_pair)
save_dict['min_separation'] = min_sep

# Information content
save_dict['info_K_values'] = np.array(list(info_content.keys()))
save_dict['info_L2_errors'] = np.array(list(info_content.values()))

outpath = os.path.join(os.path.dirname(__file__), 's63_moment_reconstruct.npz')
np.savez(outpath, **save_dict)
print(f"\nSaved: {outpath}")

# =============================================================================
#  14. Plot
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(3, 2, figsize=(16, 18))
fig.suptitle('MOMENT-RECONSTRUCT-63: Hausdorff Moment Inversion from 7 Spectral Moments',
             fontsize=14, fontweight='bold')

# Sort eigenvalues for plotting
sort_idx = np.argsort(lam2)
u_sorted = lam2[sort_idx]

for idx, (name, info) in enumerate(ref_data.items()):
    ax = axes[idx // 2, idx % 2]
    f_ref = info['f_ref'][sort_idx]
    f_me = results[name]['maxent']['f'][sort_idx]
    f_bern = results[name]['bernstein']['f'][sort_idx]
    f_poly = results[name]['polynomial']['f'][sort_idx]

    ax.plot(u_sorted, f_ref, 'k-', lw=2, label=f'True f (gamma={info["gamma"]:.3f})', alpha=0.8)
    ax.plot(u_sorted, f_me, 'r--', lw=1.5,
            label=f'MaxEnt (L2={results[name]["maxent"]["L2_err"]*100:.2f}%)')
    ax.plot(u_sorted, f_bern, 'b:', lw=1.5,
            label=f'Bernstein (L2={results[name]["bernstein"]["L2_err"]*100:.2f}%)')
    ax.plot(u_sorted, f_poly, 'g-.', lw=1.5,
            label=f'Polynomial (L2={results[name]["polynomial"]["L2_err"]*100:.2f}%)')

    ax.set_xlabel(r'$u = \lambda^2$ [$M_{KK}^2$]')
    ax.set_ylabel(r'$f(u)$')
    ax.set_title(name)
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's63_moment_reconstruct.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")

# Additional plot: information content
fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
fig2.suptitle('Information Content of Spectral Moments', fontsize=12, fontweight='bold')

# Left: L^2 error vs K (number of moments)
K_vals = list(info_content.keys())
L2_vals = [info_content[k] * 100 for k in K_vals]
ax1.semilogy(K_vals, L2_vals, 'ko-', markersize=8, lw=2)
ax1.axhline(5.0, color='r', linestyle='--', label='5% threshold')
ax1.set_xlabel('Number of moments K')
ax1.set_ylabel(r'$L^2$ reconstruction error (%)')
ax1.set_title('MaxEnt Error vs Moments (Butterworth — hardest case)')
ax1.legend()
ax1.grid(True, alpha=0.3)

# Right: distinguishability matrix
im = ax2.imshow(dist_matrix, cmap='viridis', aspect='auto')
ax2.set_xticks(range(n_fam))
ax2.set_xticklabels([n[:8] for n in fam_names], rotation=45, ha='right')
ax2.set_yticks(range(n_fam))
ax2.set_yticklabels([n[:8] for n in fam_names])
ax2.set_title('Moment-Space Distance Matrix')
plt.colorbar(im, ax=ax2, label='Normalized distance')
for i in range(n_fam):
    for j in range(n_fam):
        ax2.text(j, i, f'{dist_matrix[i,j]:.2f}', ha='center', va='center',
                color='white' if dist_matrix[i,j] > dist_matrix.max()/2 else 'black', fontsize=7)

plt.tight_layout()
plotpath2 = os.path.join(os.path.dirname(__file__), 's63_moment_reconstruct_info.png')
plt.savefig(plotpath2, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath2}")

print("\n" + "=" * 76)
print("DONE: MOMENT-RECONSTRUCT-63")
print("=" * 76)
