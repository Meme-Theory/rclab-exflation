#!/usr/bin/env python3
"""
s61_zeta_zeros.py — ZETA-ZEROS-61
Spectral Zeta Function Zeros of D_K on Jensen-deformed SU(3)

Mathematical Setup
------------------
The spectral zeta function of the fiber Dirac operator D_K(tau) on SU(3)
with Jensen deformation parameter tau is:

    zeta_{D_K}(s) = sum_{n: lambda_n != 0} |lambda_n|^{-s}

where {lambda_n} are the eigenvalues of D_K, counted with Peter-Weyl
multiplicity dim(p,q)^2.

For Re(s) > d = 8 (the dimension of SU(3)), this converges absolutely.
For Re(s) <= 8, we need analytic continuation via the Mellin transform:

    zeta(s) = (1/Gamma(s)) * int_0^infty t^{s-1} Theta(t) dt

where Theta(t) = sum_n exp(-lambda_n^2 * t) is the heat trace. For a finite
(PW-truncated) spectrum this is a sum of exponentials whose Mellin transform
is exact:

    zeta(s) = sum_n |lambda_n|^{-s}     [valid for all s by analytic continuation]

since for a FINITE sum of |lambda_n|^{-s} with lambda_n != 0, the function
is ENTIRE in s (no poles). The "dimension = 8" abscissa of convergence is a
property of the FULL infinite PW expansion; any finite truncation gives an
entire function.

Key consequence: For a truncated spectrum, zeta(s) = sum |lambda_n|^{-s}
is well-defined for ALL complex s as a finite sum of exponentials
|lambda_n|^{-s} = exp(-s * ln|lambda_n|). No regularization needed.

The "critical line" for a d-dimensional manifold is Re(s) = d/2 = 4.
If zeros cluster near Re(s) = 4, the spectral geometry exhibits a
Riemannian analog of the Riemann hypothesis.

Gate: ZETA-ZEROS-61
    PASS: >80% zeros within |Re(s)-4| < 0.5 AND fraction increases with truncation
    FAIL: zeros scatter uniformly
    INFO: cluster near sigma_0 != 4

Author: connes-ncg-theorist
Session: S61 W2-B1b
"""

import sys
import os
import time
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, str(_x2_shared_dir()))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.optimize import minimize_scalar
from scipy.special import gamma as gamma_func

from canonical_constants import tau_fold, PI

import dirac_spectrum as tds

outdir = os.path.dirname(os.path.abspath(__file__))

print("=" * 72)
print("ZETA-ZEROS-61: Spectral Zeta Zero Location on D_K(tau_fold)")
print("=" * 72)

# =============================================================================
# 1. COMPUTE DIRAC EIGENVALUES AT THE FOLD
# =============================================================================
print("\n" + "=" * 72)
print("1. DIRAC EIGENVALUE COMPUTATION AT tau = %.4f" % tau_fold)
print("=" * 72)

gens = tds.su3_generators()
f_abc = tds.compute_structure_constants(gens)
gammas = tds.build_cliff8()

cliff_err = tds.validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")

B_ab = tds.compute_killing_form(f_abc)
g_s = tds.jensen_metric(B_ab, tau_fold)
E = tds.orthonormal_frame(g_s)
ft = tds.frame_structure_constants(f_abc, E)
Gamma = tds.connection_coefficients(ft)

mc_err = tds.validate_connection(Gamma)
print(f"  Metric compatibility error: {mc_err:.2e}")

Omega = tds.spinor_connection_offset(Gamma, gammas)
is_h, is_ah, h_err, ah_err = tds.validate_omega_hermitian(Omega)
print(f"  Omega anti-Hermiticity error: {ah_err:.2e}")

# Collect eigenvalues at multiple truncation levels
# Level L includes all irreps (p,q) with p+q <= L
L_max = 7  # Maximum truncation level

all_eigenvalues = {}  # (p,q) -> array of |lambda_n|
all_degeneracies = {}  # (p,q) -> dim(p,q)^2

t_start = time.time()

for L in range(L_max + 1):
    for p in range(L + 1):
        q = L - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

        tds._irrep_cache.clear()

        try:
            rho, dim_check = tds.get_irrep(p, q, gens, f_abc)
            assert dim_check == dim_pq
        except Exception as e:
            print(f"  ({p},{q}): SKIPPED - {e}")
            continue

        D_pi = tds.dirac_operator_on_irrep(rho, E, gammas, Omega)
        evals = np.linalg.eigvals(D_pi)
        abs_evals = np.abs(evals)

        # Remove near-zero eigenvalues (if any)
        abs_evals = abs_evals[abs_evals > 1e-10]

        all_eigenvalues[(p, q)] = abs_evals
        all_degeneracies[(p, q)] = dim_pq ** 2

        print(f"  ({p},{q}): dim={dim_pq:3d}, deg={dim_pq**2:5d}, "
              f"n_evals={len(abs_evals):4d}, "
              f"|lam| in [{np.min(abs_evals):.4f}, {np.max(abs_evals):.4f}]")

t_evals = time.time() - t_start
print(f"\n  Total eigenvalue computation: {t_evals:.1f}s")

# =============================================================================
# 2. BUILD SPECTRAL ZETA AT MULTIPLE TRUNCATION LEVELS
# =============================================================================
print("\n" + "=" * 72)
print("2. SPECTRAL ZETA FUNCTION CONSTRUCTION")
print("=" * 72)

# Define truncation levels: L_cut = 3, 5, 7
truncation_levels = [3, 5, 7]

def build_weighted_spectrum(L_cut):
    """Build (eigenvalue, degeneracy) pairs for all irreps with p+q <= L_cut."""
    evals_list = []
    degs_list = []
    for (p, q), ev in all_eigenvalues.items():
        if p + q <= L_cut:
            evals_list.append(ev)
            degs_list.append(np.full(len(ev), all_degeneracies[(p, q)], dtype=float))
    if not evals_list:
        return np.array([]), np.array([])
    return np.concatenate(evals_list), np.concatenate(degs_list)


def spectral_zeta(s, lambdas, degs):
    """
    Compute zeta_{D_K}(s) = sum_n d_n |lambda_n|^{-s}

    For finite spectrum, this is an entire function of s (no poles).
    |lambda_n|^{-s} = exp(-s * ln|lambda_n|) is well-defined for all complex s.

    Args:
        s: complex number
        lambdas: array of |eigenvalues| (all > 0)
        degs: array of degeneracies (dim(p,q)^2 for each eigenvalue)

    Returns:
        complex value of zeta(s)
    """
    # |lambda|^{-s} = exp(-s * ln|lambda|)
    log_lam = np.log(lambdas)
    terms = degs * np.exp(-s * log_lam)
    return np.sum(terms)


def spectral_zeta_deriv(s, lambdas, degs):
    """
    Compute zeta'(s) = -sum_n d_n ln|lambda_n| * |lambda_n|^{-s}
    """
    log_lam = np.log(lambdas)
    terms = -degs * log_lam * np.exp(-s * log_lam)
    return np.sum(terms)


# Verify: at large Re(s), direct sum should give sensible values
for L_cut in truncation_levels:
    lam, deg = build_weighted_spectrum(L_cut)
    N_modes = int(np.sum(deg))
    z10 = spectral_zeta(10.0, lam, deg)
    print(f"  L_cut={L_cut}: {len(lam)} distinct evals, "
          f"N_weighted={N_modes}, zeta(10) = {z10:.6e}")

# =============================================================================
# 3. GRID SCAN FOR ZEROS
# =============================================================================
print("\n" + "=" * 72)
print("3. GRID SCAN FOR APPROXIMATE ZEROS")
print("=" * 72)

# Grid: Re(s) in [0.5, 7.5], Im(s) in [-50, 50]
# Note: zeta(s) is real on the real axis for real spectrum, so zeros
# come in conjugate pairs. We scan Im(s) >= 0 and reflect.
re_grid = np.arange(0.5, 7.51, 0.05)
im_grid = np.arange(0.0, 50.01, 0.05)

# For efficiency, precompute log(lambda) once per truncation level
results_by_truncation = {}

for L_cut in truncation_levels:
    print(f"\n  --- Truncation L_cut = {L_cut} ---")
    lam, deg = build_weighted_spectrum(L_cut)
    log_lam = np.log(lam)
    N_weighted = int(np.sum(deg))

    t0 = time.time()

    # Vectorized grid evaluation
    # zeta(sigma + i*t) = sum_n d_n exp(-(sigma+it)*ln|lam_n|)
    #                    = sum_n d_n |lam_n|^{-sigma} exp(-i*t*ln|lam_n|)

    # Pre-compute |lam|^{-sigma} for each sigma value
    # Shape: (n_re, n_evals)
    lam_pow = np.exp(-re_grid[:, None] * log_lam[None, :])  # (n_re, n_evals)

    # For each (sigma, t), zeta = sum_n d_n * lam_pow[sigma_idx, n] * exp(-i*t*log_lam[n])
    # We need |zeta|^2 = |sum ...|^2 on the grid

    abs_zeta_grid = np.zeros((len(re_grid), len(im_grid)))

    # Vectorize over im_grid using broadcasting
    # phases[t_idx, n] = exp(-i * im_grid[t_idx] * log_lam[n])
    # Do in chunks to manage memory
    chunk_size = 200
    for i_chunk in range(0, len(im_grid), chunk_size):
        t_slice = im_grid[i_chunk:i_chunk + chunk_size]
        phases = np.exp(-1j * t_slice[:, None] * log_lam[None, :])  # (chunk, n_evals)

        for i_re in range(len(re_grid)):
            weighted = deg * lam_pow[i_re, :]  # (n_evals,)
            z_vals = phases @ weighted  # (chunk,)
            abs_zeta_grid[i_re, i_chunk:i_chunk + len(t_slice)] = np.abs(z_vals)

    t_grid = time.time() - t0
    print(f"  Grid scan: {len(re_grid)}x{len(im_grid)} = {len(re_grid)*len(im_grid)} points in {t_grid:.1f}s")

    # Find local minima: points where |zeta| is less than all 8 neighbors
    # and |zeta| < threshold
    threshold = 1.0  # Initial threshold for candidate zeros (local)

    candidates = []
    for i_re in range(1, len(re_grid) - 1):
        for i_im in range(1, len(im_grid) - 1):
            val = abs_zeta_grid[i_re, i_im]
            if val < threshold:
                # Check if local minimum
                neighbors = [
                    abs_zeta_grid[i_re-1, i_im], abs_zeta_grid[i_re+1, i_im],
                    abs_zeta_grid[i_re, i_im-1], abs_zeta_grid[i_re, i_im+1],
                    abs_zeta_grid[i_re-1, i_im-1], abs_zeta_grid[i_re+1, i_im+1],
                    abs_zeta_grid[i_re-1, i_im+1], abs_zeta_grid[i_re+1, i_im-1],
                ]
                if val <= min(neighbors):
                    candidates.append((re_grid[i_re], im_grid[i_im], val))

    # Also check boundary at Im(s)=0 (real axis)
    for i_re in range(1, len(re_grid) - 1):
        val = abs_zeta_grid[i_re, 0]
        if val < threshold:
            if (val <= abs_zeta_grid[i_re-1, 0] and
                val <= abs_zeta_grid[i_re+1, 0] and
                val <= abs_zeta_grid[i_re, 1]):
                candidates.append((re_grid[i_re], 0.0, val))

    print(f"  Found {len(candidates)} candidate zeros (|zeta| < {threshold})")

    # Sort by |zeta| value
    candidates.sort(key=lambda x: x[2])
    for c in candidates[:20]:
        print(f"    s = {c[0]:.2f} + {c[1]:.2f}i, |zeta| = {c[2]:.4e}")

    results_by_truncation[L_cut] = {
        'lam': lam,
        'deg': deg,
        'log_lam': log_lam,
        'N_weighted': N_weighted,
        'abs_zeta_grid': abs_zeta_grid,
        'candidates': candidates,
    }

# =============================================================================
# 4. REFINE ZEROS VIA NEWTON-RAPHSON
# =============================================================================
print("\n" + "=" * 72)
print("4. ZERO REFINEMENT VIA NEWTON-RAPHSON")
print("=" * 72)

def refine_zero_newton(s0, lam, deg, log_lam, max_iter=200, tol=1e-12):
    """
    Refine a zero of zeta(s) using Newton-Raphson: s_{n+1} = s_n - zeta(s_n)/zeta'(s_n).

    Returns: (s_refined, |zeta(s_refined)|, converged)
    """
    s = complex(s0)
    for it in range(max_iter):
        exp_vals = np.exp(-s * log_lam)
        z = np.sum(deg * exp_vals)
        zp = np.sum(-deg * log_lam * exp_vals)

        if abs(zp) < 1e-30:
            return s, abs(z), False

        ds = z / zp
        s = s - ds

        if abs(ds) < tol:
            exp_vals_final = np.exp(-s * log_lam)
            z_final = np.sum(deg * exp_vals_final)
            return s, abs(z_final), True

    exp_vals_final = np.exp(-s * log_lam)
    z_final = np.sum(deg * exp_vals_final)
    return s, abs(z_final), False


refined_zeros_by_truncation = {}

for L_cut in truncation_levels:
    print(f"\n  --- Truncation L_cut = {L_cut} ---")
    data = results_by_truncation[L_cut]
    lam = data['lam']
    deg = data['deg']
    log_lam = data['log_lam']
    candidates = data['candidates']

    refined = []
    seen = set()  # Avoid duplicates (round to 3 decimal places)

    for sigma0, t0, val0 in candidates:
        # Try refining from both (sigma, t) and (sigma, -t) for conjugate pairs
        for sign in [1, -1]:
            if t0 == 0.0 and sign == -1:
                continue
            s0 = complex(sigma0, sign * t0)
            s_ref, abs_z, conv = refine_zero_newton(s0, lam, deg, log_lam)

            if conv and abs_z < 1e-6:
                # Check for duplicates
                key = (round(s_ref.real, 3), round(abs(s_ref.imag), 3))
                if key not in seen:
                    seen.add(key)
                    refined.append({
                        's': s_ref,
                        'abs_zeta': abs_z,
                        'sigma': s_ref.real,
                        'tau_imag': s_ref.imag,
                        'converged': conv,
                    })

    # Also try a denser search near Re(s) = 4 (the predicted critical line)
    print(f"  Dense search near Re(s) = 4...")
    for sigma_init in np.arange(3.0, 5.01, 0.1):
        for t_init in np.arange(0.5, 50.0, 0.5):
            s0 = complex(sigma_init, t_init)
            s_ref, abs_z, conv = refine_zero_newton(s0, lam, deg, log_lam)
            if conv and abs_z < 1e-6:
                key = (round(s_ref.real, 3), round(abs(s_ref.imag), 3))
                if key not in seen:
                    seen.add(key)
                    refined.append({
                        's': s_ref,
                        'abs_zeta': abs_z,
                        'sigma': s_ref.real,
                        'tau_imag': s_ref.imag,
                        'converged': conv,
                    })

    # Sort by imaginary part
    refined.sort(key=lambda x: abs(x['tau_imag']))

    print(f"  Refined zeros: {len(refined)}")
    for z in refined[:30]:
        marker = ""
        if abs(z['sigma'] - 4.0) < 0.5:
            marker = " <-- near critical line"
        print(f"    s = {z['sigma']:.6f} + {z['tau_imag']:.6f}i, "
              f"|zeta| = {z['abs_zeta']:.2e}{marker}")
    if len(refined) > 30:
        print(f"    ... ({len(refined) - 30} more)")

    refined_zeros_by_truncation[L_cut] = refined

# =============================================================================
# 5. CLASSIFICATION AND GATE EVALUATION
# =============================================================================
print("\n" + "=" * 72)
print("5. ZERO CLASSIFICATION AND GATE EVALUATION")
print("=" * 72)

gate_results = {}

for L_cut in truncation_levels:
    refined = refined_zeros_by_truncation[L_cut]
    n_total = len(refined)

    if n_total == 0:
        print(f"\n  L_cut={L_cut}: NO ZEROS FOUND")
        gate_results[L_cut] = {
            'n_total': 0,
            'n_near_4': 0,
            'fraction_near_4': 0.0,
            'mean_sigma': float('nan'),
            'std_sigma': float('nan'),
        }
        continue

    sigmas = np.array([z['sigma'] for z in refined])
    taus = np.array([z['tau_imag'] for z in refined])

    # Classify: near Re(s)=4
    near_4 = np.abs(sigmas - 4.0) < 0.5
    n_near_4 = np.sum(near_4)
    frac_near_4 = n_near_4 / n_total if n_total > 0 else 0.0

    # Statistics
    mean_sigma = np.mean(sigmas)
    std_sigma = np.std(sigmas)
    median_sigma = np.median(sigmas)

    # Distribution by Re(s) bands
    bands = [(0, 1), (1, 2), (2, 3), (3, 3.5), (3.5, 4.5), (4.5, 5), (5, 6), (6, 7), (7, 8)]

    print(f"\n  L_cut={L_cut}: {n_total} zeros")
    print(f"  Mean Re(s) = {mean_sigma:.4f}, Std = {std_sigma:.4f}, Median = {median_sigma:.4f}")
    print(f"  Near |Re(s)-4| < 0.5: {n_near_4}/{n_total} = {frac_near_4*100:.1f}%")
    print(f"  Distribution by Re(s) band:")
    for lo, hi in bands:
        count = np.sum((sigmas >= lo) & (sigmas < hi))
        pct = count / n_total * 100 if n_total > 0 else 0
        bar = "#" * int(pct / 2)
        print(f"    [{lo:.1f}, {hi:.1f}): {count:3d} ({pct:5.1f}%) {bar}")

    gate_results[L_cut] = {
        'n_total': n_total,
        'n_near_4': int(n_near_4),
        'fraction_near_4': float(frac_near_4),
        'mean_sigma': float(mean_sigma),
        'std_sigma': float(std_sigma),
        'median_sigma': float(median_sigma),
        'sigmas': sigmas,
        'taus': taus,
    }

# Gate evaluation
print("\n  --- GATE EVALUATION ---")
fracs = [gate_results[L]['fraction_near_4'] for L in truncation_levels if gate_results[L]['n_total'] > 0]
n_totals = [gate_results[L]['n_total'] for L in truncation_levels]
means = [gate_results[L]['mean_sigma'] for L in truncation_levels if gate_results[L]['n_total'] > 0]

if all(n == 0 for n in n_totals):
    verdict = "INFO"
    verdict_detail = "No nontrivial zeros found in 0 < Re(s) < 8, |Im(s)| < 50."
elif len(fracs) >= 2 and fracs[-1] > 0.80 and fracs[-1] >= fracs[0]:
    verdict = "PASS"
    verdict_detail = (f">{fracs[-1]*100:.0f}% near Re(s)=4, fraction increases with truncation. "
                     f"Fracs: {[f'{f*100:.1f}%' for f in fracs]}")
elif len(fracs) >= 1 and max(fracs) < 0.3:
    verdict = "FAIL"
    verdict_detail = f"Zeros scatter. Max fraction near Re(s)=4: {max(fracs)*100:.1f}%"
else:
    # Check if they cluster near some other sigma_0
    if len(means) > 0:
        mean_of_means = np.mean(means)
        if abs(mean_of_means - 4.0) > 0.5:
            verdict = "INFO"
            verdict_detail = f"Zeros cluster near Re(s)={mean_of_means:.2f} (not 4). "
        else:
            verdict = "INFO"
            verdict_detail = (f"Zeros near Re(s)=4 but fraction {fracs[-1]*100:.1f}% < 80% threshold. "
                            f"Fracs: {[f'{f*100:.1f}%' for f in fracs]}")
    else:
        verdict = "INFO"
        verdict_detail = "Insufficient data for classification."

print(f"\n  ZETA-ZEROS-61: {verdict}")
print(f"  Detail: {verdict_detail}")

# =============================================================================
# 6. ADDITIONAL ANALYSIS: REAL-AXIS STRUCTURE
# =============================================================================
print("\n" + "=" * 72)
print("6. REAL-AXIS STRUCTURE OF zeta(sigma)")
print("=" * 72)

# zeta(sigma) for real sigma is REAL and positive for the truncated spectrum
# (since all terms are positive for real sigma). So no zeros on the real axis.
# But we can study the growth rate and poles of the full theory.

L_cut = 7
lam, deg = build_weighted_spectrum(L_cut)
log_lam = np.log(lam)

sigma_range = np.linspace(-2, 12, 1000)
zeta_real = np.array([spectral_zeta(s, lam, deg).real for s in sigma_range])

# Find where zeta(sigma) has interesting structure
print(f"  zeta(0) = {spectral_zeta(0, lam, deg).real:.6f} (= N_weighted = sum d_n)")
print(f"  zeta(2) = {spectral_zeta(2, lam, deg).real:.6e}")
print(f"  zeta(4) = {spectral_zeta(4, lam, deg).real:.6e}")
print(f"  zeta(8) = {spectral_zeta(8, lam, deg).real:.6e}")
print(f"  Sum d_n = {np.sum(deg):.0f}")

# Verify: zeta(0) should equal the total weighted count
z0_check = spectral_zeta(0.0, lam, deg)
print(f"  zeta(0) check: {z0_check.real:.6f} vs sum(deg) = {np.sum(deg):.0f}")

# Heat kernel coefficients from the zeta function
# Res_{s=d/2-k} zeta(s) gives a_{2k}/(4pi)^{d/2}
# But for truncated spectrum, zeta is entire -- no residues.
# The heat kernel asymptotics emerge only in the full PW limit.

# =============================================================================
# 7. IMAGINARY-AXIS ZEROS (FUNCTIONAL EQUATION TEST)
# =============================================================================
print("\n" + "=" * 72)
print("7. FUNCTIONAL EQUATION STRUCTURE")
print("=" * 72)

# For a compact Riemannian manifold, the spectral zeta satisfies a
# functional equation relating zeta(s) and zeta(d-s) through the
# heat kernel coefficients. For the truncated spectrum this is approximate.

# Check: does zeta(s) approximately equal some transform of zeta(8-s)?
# The Minakshisundaram-Pleijel relation gives:
#   zeta(s) = (meromorphic continuation from Re(s) > d)
# with poles at s = d/2, d/2-1, d/2-2, ...

# For our finite spectrum: zeta(s) is entire, so no poles.
# But we can check the RATIO zeta(s)/zeta(8-s) for structure.

test_points = [1.0, 2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 7.0]
print(f"  Functional equation probe: zeta(s) vs zeta(8-s)")
print(f"  {'s':>6s}  {'zeta(s)':>20s}  {'zeta(8-s)':>20s}  {'ratio':>14s}")
for s_val in test_points:
    z_s = spectral_zeta(complex(s_val, 0), lam, deg)
    z_8ms = spectral_zeta(complex(8 - s_val, 0), lam, deg)
    ratio = z_s / z_8ms if abs(z_8ms) > 1e-30 else float('inf')
    print(f"  {s_val:6.1f}  {z_s.real:20.6e}  {z_8ms.real:20.6e}  {ratio.real:14.6e}")

# =============================================================================
# 8. SPECTRAL ZETA AT SPECIAL POINTS
# =============================================================================
print("\n" + "=" * 72)
print("8. SPECTRAL ZETA AT SPECIAL POINTS")
print("=" * 72)

# zeta(-n) for non-negative integers gives heat kernel coefficients
# For truncated spectrum: zeta(-n) = sum d_k |lam_k|^n
# These are moments of the spectral measure.
for n in range(5):
    z_neg_n = spectral_zeta(-n, lam, deg).real
    print(f"  zeta({-n:2d}) = {z_neg_n:.6e}  (= sum d_k |lam_k|^{n})")

# zeta'(0) gives log(det D) via zeta regularization
# For truncated spectrum: zeta'(0) = -sum d_k ln|lam_k|
zp0 = spectral_zeta_deriv(0.0, lam, deg).real
print(f"\n  zeta'(0) = {zp0:.6e}  (= -sum d_k ln|lam_k|)")
print(f"  log(det D) = -zeta'(0) = {-zp0:.6e}")

# =============================================================================
# 9. PLOT
# =============================================================================
print("\n" + "=" * 72)
print("9. GENERATING PLOTS")
print("=" * 72)

fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle(
    r"Spectral Zeta $\zeta_{D_K}(s)$ on Jensen SU(3) at $\tau=0.19$",
    fontsize=14, fontweight='bold'
)

# Panel 1: |zeta(s)| heat map for L_cut=7
ax = axes[0, 0]
data7 = results_by_truncation[7]
extent = [im_grid[0], im_grid[-1], re_grid[0], re_grid[-1]]
# Transpose so x=Im(s), y=Re(s)
log_abs_zeta = np.log10(data7['abs_zeta_grid'] + 1e-30)
im = ax.imshow(log_abs_zeta, aspect='auto', origin='lower', extent=extent,
               cmap='viridis', vmin=-6, vmax=10)
ax.axhline(y=4.0, color='red', linewidth=2, linestyle='--', label=r'Re$(s)=4$')
# Mark zeros
if len(refined_zeros_by_truncation[7]) > 0:
    z7 = refined_zeros_by_truncation[7]
    z_taus = [abs(z['tau_imag']) for z in z7]
    z_sigmas = [z['sigma'] for z in z7]
    ax.scatter(z_taus, z_sigmas, color='red', marker='x', s=40, zorder=5, label='Zeros')
ax.set_xlabel(r'Im$(s)$')
ax.set_ylabel(r'Re$(s)$')
ax.set_title(r'$\log_{10}|\zeta(s)|$, $L_{\max}=7$')
ax.legend(loc='upper right')
plt.colorbar(im, ax=ax, label=r'$\log_{10}|\zeta|$')

# Panel 2: Zero locations across truncations
ax = axes[0, 1]
colors = {3: 'blue', 5: 'green', 7: 'red'}
for L_cut in truncation_levels:
    refined = refined_zeros_by_truncation[L_cut]
    if refined:
        sigmas = [z['sigma'] for z in refined]
        taus = [abs(z['tau_imag']) for z in refined]
        n_near = gate_results[L_cut]['n_near_4']
        n_tot = gate_results[L_cut]['n_total']
        frac = gate_results[L_cut]['fraction_near_4']
        ax.scatter(taus, sigmas, color=colors[L_cut], s=20, alpha=0.7,
                  label=rf'$L={L_cut}$ ({n_near}/{n_tot}={frac*100:.0f}% near 4)')
ax.axhline(y=4.0, color='gray', linewidth=2, linestyle='--', alpha=0.5,
           label=r'Critical line Re$(s)=d/2=4$')
ax.axhline(y=3.5, color='gray', linewidth=0.5, linestyle=':')
ax.axhline(y=4.5, color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel(r'$|\mathrm{Im}(s)|$')
ax.set_ylabel(r'Re$(s)$')
ax.set_title('Zero locations by truncation level')
ax.legend(fontsize=8)
ax.set_ylim(0, 8)

# Panel 3: Histogram of Re(s) for zeros
ax = axes[1, 0]
for L_cut in truncation_levels:
    if gate_results[L_cut]['n_total'] > 0:
        sigmas = gate_results[L_cut]['sigmas']
        ax.hist(sigmas, bins=np.arange(0, 8.5, 0.5), alpha=0.4, color=colors[L_cut],
               label=rf'$L={L_cut}$ (n={len(sigmas)})', edgecolor='black', linewidth=0.5)
ax.axvline(x=4.0, color='red', linewidth=2, linestyle='--', label=r'$d/2=4$')
ax.set_xlabel(r'Re$(s)$')
ax.set_ylabel('Count')
ax.set_title(r'Distribution of Re$(s)$ at zeros')
ax.legend()

# Panel 4: zeta(sigma) on real axis
ax = axes[1, 1]
# Plot log|zeta(sigma)| vs sigma
zeta_real_positive = np.where(zeta_real > 0, zeta_real, np.nan)
zeta_real_negative = np.where(zeta_real < 0, -zeta_real, np.nan)
ax.semilogy(sigma_range, zeta_real_positive, 'b-', linewidth=1, label=r'$\zeta(\sigma)>0$')
ax.semilogy(sigma_range, zeta_real_negative, 'r--', linewidth=1, label=r'$\zeta(\sigma)<0$')
ax.axvline(x=4.0, color='gray', linewidth=1, linestyle='--', label=r'$d/2=4$')
ax.axvline(x=0.0, color='gray', linewidth=0.5, linestyle=':')
ax.set_xlabel(r'$\sigma$')
ax.set_ylabel(r'$|\zeta(\sigma)|$')
ax.set_title(r'$\zeta(\sigma)$ on real axis ($L=7$)')
ax.legend()
ax.set_xlim(-2, 12)

plt.tight_layout()
out_png = os.path.join(outdir, 's61_zeta_zeros.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"  Plot saved: {out_png}")
plt.close()

# =============================================================================
# 10. SAVE DATA
# =============================================================================
print("\n" + "=" * 72)
print("10. SAVING DATA")
print("=" * 72)

save_dict = {
    'tau_fold': tau_fold,
    'truncation_levels': np.array(truncation_levels),
    're_grid': re_grid,
    'im_grid': im_grid,
    'gate_name': np.array(['ZETA-ZEROS-61']),
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([verdict_detail]),
}

# Per-truncation data
for L_cut in truncation_levels:
    gr = gate_results[L_cut]
    prefix = f'L{L_cut}_'
    save_dict[prefix + 'n_total'] = np.array(gr['n_total'])
    save_dict[prefix + 'n_near_4'] = np.array(gr.get('n_near_4', 0))
    save_dict[prefix + 'fraction_near_4'] = np.array(gr.get('fraction_near_4', 0.0))
    save_dict[prefix + 'mean_sigma'] = np.array(gr.get('mean_sigma', np.nan))
    save_dict[prefix + 'std_sigma'] = np.array(gr.get('std_sigma', np.nan))
    if 'sigmas' in gr:
        save_dict[prefix + 'sigmas'] = gr['sigmas']
        save_dict[prefix + 'taus'] = gr['taus']

    # Save the abs_zeta grid for L=7
    if L_cut == 7:
        save_dict['abs_zeta_grid_L7'] = results_by_truncation[7]['abs_zeta_grid']

# Eigenvalue spectrum summary
save_dict['n_irreps'] = np.array(len(all_eigenvalues))
lam7, deg7 = build_weighted_spectrum(7)
save_dict['spectrum_L7_lam'] = lam7
save_dict['spectrum_L7_deg'] = deg7
save_dict['zeta_special'] = np.array([
    spectral_zeta(0, lam7, deg7).real,
    spectral_zeta(2, lam7, deg7).real,
    spectral_zeta(4, lam7, deg7).real,
    spectral_zeta(8, lam7, deg7).real,
])
save_dict['zeta_prime_0'] = np.array(zp0)

out_npz = os.path.join(outdir, 's61_zeta_zeros.npz')
np.savez(out_npz, **save_dict)
print(f"  Data saved: {out_npz}")

# =============================================================================
# 11. FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 72)
print("ZETA-ZEROS-61: FINAL SUMMARY")
print("=" * 72)

print(f"\n  Gate: ZETA-ZEROS-61")
print(f"  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")
print(f"\n  Truncation analysis:")
for L_cut in truncation_levels:
    gr = gate_results[L_cut]
    print(f"    L={L_cut}: {gr['n_total']} zeros, "
          f"{gr.get('n_near_4',0)} near Re(s)=4 ({gr.get('fraction_near_4',0)*100:.1f}%), "
          f"mean Re(s) = {gr.get('mean_sigma', float('nan')):.3f} +/- {gr.get('std_sigma', float('nan')):.3f}")

print(f"\n  Key numbers:")
print(f"    zeta(0) = {spectral_zeta(0, lam7, deg7).real:.0f} (total weighted mode count)")
print(f"    zeta'(0) = {zp0:.6e} (log det D_K)")
print(f"    Eigenvalue range: [{np.min(lam7):.4f}, {np.max(lam7):.4f}]")
print(f"    N_weighted(L=7) = {int(np.sum(deg7))}")

print("\n" + "=" * 72)
print("DONE")
print("=" * 72)
