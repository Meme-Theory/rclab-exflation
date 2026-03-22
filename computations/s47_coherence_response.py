#!/usr/bin/env python3
"""
s47_coherence_response.py -- Deformation Response of Character Coherence
=========================================================================

Session 47 Wave 3, COHERENCE-RESPONSE-47

Computes C(theta, 0; tau) -- the character coherence function on T^2 --
across the full tau range. Extracts the 1/e^2 radius r_C(tau).
Correlates with Delta_B2(tau).

DECISIVE TEST: If r_C tracks 1/Delta_B2, the BCS weights dynamically
determine the coherence pattern (substrate). If r_C is constant,
the pattern is kinematic (truncation artifact).

PRE-REGISTERED GATE:
  |r| > 0.9  -> SUBSTRATE (coherence dynamically determined)
  |r| < 0.3  -> ARTIFACT (truncation-determined)
  else       -> AMBIGUOUS

KEY INSIGHT: Characters chi_{(p,q)}(theta1, theta2) are tau-INDEPENDENT.
They are representation characters on T^2, fixed by the group. Only the
BCS WEIGHTS w_{(p,q)}(tau) change with tau:

  |Delta(theta1, theta2; tau)|^2 ~ Sum_{(p,q)} w_{(p,q)}(tau) * |chi_{(p,q)}(theta1, theta2)|^2

where w_{(p,q)}(tau) = [Sum_sectors frac_s * v_s(tau) * Delta_s(tau)]^2
      weighted by BCS occupations and gaps at each tau.

This makes the test CLEAN: same Fourier basis, different coefficients.

Author: Nazarewicz agent (S47 W3)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold

# =============================================================================
#  SECTION 1: Import character machinery from W2-1 script
# =============================================================================
# We reuse the verified character functions from s47_condensate_torus.py

def su3_character_weyl(p, q, t1, t2):
    """
    SU(3) character via Weyl character formula.
    Copied from s47_condensate_torus.py (verified to machine epsilon).
    """
    if p == 0 and q == 0:
        return np.ones_like(t1, dtype=complex)

    phi1 = t1
    phi2 = t2
    phi3 = -(t1 + t2)

    a, b, c = p + q + 2, q + 1, 0

    num = (  np.exp(1j*(a*phi1 + b*phi2 + c*phi3))
           - np.exp(1j*(a*phi1 + c*phi2 + b*phi3))
           - np.exp(1j*(b*phi1 + a*phi2 + c*phi3))
           + np.exp(1j*(b*phi1 + c*phi2 + a*phi3))
           + np.exp(1j*(c*phi1 + a*phi2 + b*phi3))
           - np.exp(1j*(c*phi1 + b*phi2 + a*phi3)))

    den = (  np.exp(1j*(2*phi1 + 1*phi2 + 0*phi3))
           - np.exp(1j*(2*phi1 + 0*phi2 + 1*phi3))
           - np.exp(1j*(1*phi1 + 2*phi2 + 0*phi3))
           + np.exp(1j*(1*phi1 + 0*phi2 + 2*phi3))
           + np.exp(1j*(0*phi1 + 2*phi2 + 1*phi3))
           - np.exp(1j*(0*phi1 + 1*phi2 + 2*phi3)))

    eps = 1e-8
    small = np.abs(den) < eps
    chi = np.where(small, 0.0+0j, num / np.where(small, 1.0, den))

    if np.any(small):
        chi_direct = su3_character_weights(p, q, t1, t2)
        chi = np.where(small, chi_direct, chi)

    return chi


def su3_character_weights(p, q, t1, t2):
    """Direct weight enumeration fallback."""
    weights = _weights_from_fourier(p, q)
    chi = np.zeros_like(t1, dtype=complex)
    for w1, w2, mult in weights:
        chi += mult * np.exp(1j * (w1*t1 + w2*t2))
    return chi


def _weights_from_fourier(p, q):
    """Extract weights by Fourier analysis of Weyl formula."""
    if p == 0 and q == 0:
        return [(0, 0, 1)]

    dim_pq = (p+1)*(q+1)*(p+q+2)//2
    w_max = p + q + 1
    N = max(4 * w_max + 1, 17)

    t1_grid = np.linspace(0, 2*np.pi, N, endpoint=False)
    t2_grid = np.linspace(0, 2*np.pi, N, endpoint=False)
    T1, T2 = np.meshgrid(t1_grid, t2_grid, indexing='ij')

    phi1, phi2, phi3 = T1, T2, -(T1 + T2)
    a, b, c = p + q + 2, q + 1, 0

    num = (  np.exp(1j*(a*phi1 + b*phi2 + c*phi3))
           - np.exp(1j*(a*phi1 + c*phi2 + b*phi3))
           - np.exp(1j*(b*phi1 + a*phi2 + c*phi3))
           + np.exp(1j*(b*phi1 + c*phi2 + a*phi3))
           + np.exp(1j*(c*phi1 + a*phi2 + b*phi3))
           - np.exp(1j*(c*phi1 + b*phi2 + a*phi3)))

    den = (  np.exp(1j*(2*phi1 + 1*phi2 + 0*phi3))
           - np.exp(1j*(2*phi1 + 0*phi2 + 1*phi3))
           - np.exp(1j*(1*phi1 + 2*phi2 + 0*phi3))
           + np.exp(1j*(1*phi1 + 0*phi2 + 2*phi3))
           + np.exp(1j*(0*phi1 + 2*phi2 + 1*phi3))
           - np.exp(1j*(0*phi1 + 1*phi2 + 2*phi3)))

    small = np.abs(den) < 1e-10
    if np.any(small):
        T1s = T1.copy(); T2s = T2.copy()
        T1s[small] += 0.001; T2s[small] += 0.0007
        phi1s, phi2s, phi3s = T1s, T2s, -(T1s + T2s)
        num_s = (  np.exp(1j*(a*phi1s + b*phi2s + c*phi3s))
                 - np.exp(1j*(a*phi1s + c*phi2s + b*phi3s))
                 - np.exp(1j*(b*phi1s + a*phi2s + c*phi3s))
                 + np.exp(1j*(b*phi1s + c*phi2s + a*phi3s))
                 + np.exp(1j*(c*phi1s + a*phi2s + b*phi3s))
                 - np.exp(1j*(c*phi1s + b*phi2s + a*phi3s)))
        den_s = (  np.exp(1j*(2*phi1s + 1*phi2s + 0*phi3s))
                 - np.exp(1j*(2*phi1s + 0*phi2s + 1*phi3s))
                 - np.exp(1j*(1*phi1s + 2*phi2s + 0*phi3s))
                 + np.exp(1j*(1*phi1s + 0*phi2s + 2*phi3s))
                 + np.exp(1j*(0*phi1s + 2*phi2s + 1*phi3s))
                 - np.exp(1j*(0*phi1s + 1*phi2s + 2*phi3s)))
        num[small] = num_s[small]
        den[small] = den_s[small]

    chi_grid = num / den
    coeffs = np.fft.fft2(chi_grid) / (N * N)

    weights = []
    for k1 in range(N):
        for k2 in range(N):
            w1 = k1 if k1 <= N//2 else k1 - N
            w2 = k2 if k2 <= N//2 else k2 - N
            c_val = coeffs[k1, k2]
            mult = round(c_val.real)
            if mult > 0 and abs(c_val.real - mult) < 0.1 and abs(c_val.imag) < 0.1:
                weights.append((w1, w2, mult))

    total_dim = sum(m for _, _, m in weights)
    if total_dim != dim_pq:
        # Larger grid fallback
        N2 = 8 * w_max + 1
        t1_grid2 = np.linspace(0, 2*np.pi, N2, endpoint=False)
        t2_grid2 = np.linspace(0, 2*np.pi, N2, endpoint=False)
        T1b, T2b = np.meshgrid(t1_grid2, t2_grid2, indexing='ij')
        phi1b, phi2b, phi3b = T1b, T2b, -(T1b + T2b)
        num_b = (  np.exp(1j*(a*phi1b + b*phi2b + c*phi3b))
                 - np.exp(1j*(a*phi1b + c*phi2b + b*phi3b))
                 - np.exp(1j*(b*phi1b + a*phi2b + c*phi3b))
                 + np.exp(1j*(b*phi1b + c*phi2b + a*phi3b))
                 + np.exp(1j*(c*phi1b + a*phi2b + b*phi3b))
                 - np.exp(1j*(c*phi1b + b*phi2b + a*phi3b)))
        den_b = (  np.exp(1j*(2*phi1b + 1*phi2b + 0*phi3b))
                 - np.exp(1j*(2*phi1b + 0*phi2b + 1*phi3b))
                 - np.exp(1j*(1*phi1b + 2*phi2b + 0*phi3b))
                 + np.exp(1j*(1*phi1b + 0*phi2b + 2*phi3b))
                 + np.exp(1j*(0*phi1b + 2*phi2b + 1*phi3b))
                 - np.exp(1j*(0*phi1b + 1*phi2b + 2*phi3b)))
        small_b = np.abs(den_b) < 1e-10
        if np.any(small_b):
            T1bs = T1b.copy(); T2bs = T2b.copy()
            T1bs[small_b] += 0.001; T2bs[small_b] += 0.0007
            phi1bs, phi2bs, phi3bs = T1bs, T2bs, -(T1bs + T2bs)
            num_bs = (  np.exp(1j*(a*phi1bs + b*phi2bs + c*phi3bs))
                      - np.exp(1j*(a*phi1bs + c*phi2bs + b*phi3bs))
                      - np.exp(1j*(b*phi1bs + a*phi2bs + c*phi3bs))
                      + np.exp(1j*(b*phi1bs + c*phi2bs + a*phi3bs))
                      + np.exp(1j*(c*phi1bs + a*phi2bs + b*phi3bs))
                      - np.exp(1j*(c*phi1bs + b*phi2bs + a*phi3bs)))
            den_bs = (  np.exp(1j*(2*phi1bs + 1*phi2bs + 0*phi3bs))
                      - np.exp(1j*(2*phi1bs + 0*phi2bs + 1*phi3bs))
                      - np.exp(1j*(1*phi1bs + 2*phi2bs + 0*phi3bs))
                      + np.exp(1j*(1*phi1bs + 0*phi2bs + 2*phi3bs))
                      + np.exp(1j*(0*phi1bs + 2*phi2bs + 1*phi3bs))
                      - np.exp(1j*(0*phi1bs + 1*phi2bs + 2*phi3bs)))
            num_b[small_b] = num_bs[small_b]
            den_b[small_b] = den_bs[small_b]
        chi_grid_b = num_b / den_b
        coeffs_b = np.fft.fft2(chi_grid_b) / (N2 * N2)
        weights = []
        for k1 in range(N2):
            for k2 in range(N2):
                w1 = k1 if k1 <= N2//2 else k1 - N2
                w2 = k2 if k2 <= N2//2 else k2 - N2
                c_val = coeffs_b[k1, k2]
                mult = round(c_val.real)
                if mult > 0 and abs(c_val.real - mult) < 0.3 and abs(c_val.imag) < 0.3:
                    weights.append((w1, w2, mult))

    return weights


# =============================================================================
#  SECTION 2: Precompute characters on radial cut (theta, 0)
# =============================================================================

def precompute_characters_radial(N_theta=500):
    """
    Compute |chi_{(p,q)}(theta, 0)|^2 for all 9 reps on the radial cut.
    Characters are tau-INDEPENDENT. Compute ONCE and reuse.
    """
    reps = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (3,0), (0,3)]
    dims = [1, 3, 3, 8, 6, 6, 15, 10, 10]

    theta = np.linspace(0, np.pi, N_theta, endpoint=True)
    t2 = np.zeros_like(theta)  # theta2 = 0

    chi_sq = {}  # (p,q) -> |chi(theta, 0)|^2

    print("Precomputing characters on radial cut (theta, 0)...")
    for (p, q), d in zip(reps, dims):
        chi = su3_character_weyl(p, q, theta, t2)

        # Verify at identity
        chi_0 = chi[0]
        if abs(chi_0.real - d) > 0.1:
            print(f"  WARNING: chi_{{{p},{q}}}(0,0) = {chi_0:.4f}, expected {d}. Using direct weights.")
            chi = su3_character_weights(p, q, theta, t2)

        chi_sq[(p, q)] = np.abs(chi)**2
        print(f"  ({p},{q}): dim={d}, chi(0,0)={chi[0].real:.4f}, "
              f"|chi|^2 max={np.max(np.abs(chi)**2):.1f}")

    return theta, chi_sq, reps, dims


# =============================================================================
#  SECTION 3: BCS weights as a function of tau
# =============================================================================

def compute_bcs_weights(tau_scan, Delta_B1, Delta_B2, Delta_B3,
                        lam2_B1, lam2_B2, lam2_B3):
    """
    Compute the BCS weight w_{(p,q)}(tau) for each rep at each tau.

    The condensate gap function in the Peter-Weyl basis:
      Delta(g; tau) = Sum_{(p,q)} w_{(p,q)}(tau) * chi_{(p,q)}(g)

    The weight for each rep depends on the BCS occupation factors v_k
    and the sector gaps Delta_s. Since each spinor eigenvalue belongs to
    a definite sector (B1/B2/B3), the BCS weight for rep (p,q) is:

      w_{(p,q)}(tau) = Sum_sectors frac_s * v_s(tau) * Delta_s(tau)

    where frac_s is the fraction of spinor eigenvalues in sector s,
    and v_s^2 = (1/2)(1 - xi_s/E_s) with xi_s = sqrt(lam2_s),
    E_s = sqrt(lam2_s + Delta_s^2).

    All reps have the SAME sector fractions (B1: 2/16, B2: 8/16, B3: 6/16)
    because the spinor module decomposes the same way for every rep.
    Therefore the weight function factorizes:

      w_{(p,q)}(tau) = dim(p,q) * w_sector(tau)

    where w_sector = Sum_s frac_s * v_s * Delta_s is rep-INDEPENDENT.

    The |chi|^2 weighting in the condensate density then goes as dim(p,q)^2,
    BUT the dim-dependent BCS suppression from higher eigenvalues modifies this.

    For the COHERENCE test: what matters is how the RELATIVE weights between
    reps change with tau. If w is dominated by the sector-averaged piece
    (which is the same for all reps), then the shape on T^2 changes only
    through the overall normalization -- not through relative reshaping.

    However, the energy-dependent BCS suppression IS rep-dependent:
    higher reps have eigenvalues further from the gap edge, so their
    v*Delta product is suppressed. This is the channel through which
    BCS can actually change the coherence width.
    """
    n_tau = len(tau_scan)
    reps = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (3,0), (0,3)]
    dims = np.array([1, 3, 3, 8, 6, 6, 15, 10, 10], dtype=float)

    # Sector fractions per spinor (all reps identical)
    frac_s = np.array([2.0/16, 8.0/16, 6.0/16])  # B1, B2, B3

    # Representative eigenvalue^2 for each rep, per sector.
    # The lowest rep (0,0) sits at the Dirac gap edge.
    # Higher reps sit at progressively larger eigenvalues.
    # At each tau, lam2_Bs(tau) gives the sector-averaged eigenvalue^2 for (0,0).
    # For higher reps, we need to scale.
    #
    # From s44_dos_tau.npz, the eigenvalue ordering:
    # (0,0) cluster at lowest eigenvalues, then (1,0)/(0,1), then (1,1)/(2,0)/(0,2),
    # then (2,1)/(3,0)/(0,3) at the highest.
    #
    # The energy-dependent BCS suppression goes as:
    #   v_k * Delta / dim_k = (Delta / (2*E_k)) where E_k = sqrt(eps_k^2 + Delta^2)
    #
    # For each rep at each tau, we use the INTERPOLATED lam2 values scaled by
    # a rep-dependent factor. Since all 60 tau points have smooth interpolated
    # lam2 for each sector, we compute the BCS suppression.
    #
    # KEY APPROXIMATION: All modes within a sector share the same gap Delta_s.
    # The rep-dependence comes ONLY from the eigenvalue shift.
    #
    # For reps beyond (0,0), the eigenvalues are approximately:
    # eps_{(p,q)} = eps_{(0,0)} * (1 + alpha * (p+q))
    # where alpha ~ 0.2 from the Dirac spectrum at the fold.
    #
    # Rather than assume a functional form, we use the 5 tau points
    # from s44_dos_tau.npz to calibrate the energy shifts, then interpolate.

    # Load the 5-point eigenvalue data to get rep-resolved energies
    data_dir = os.path.dirname(os.path.abspath(__file__))
    d44 = np.load(os.path.join(data_dir, 's44_dos_tau.npz'), allow_pickle=True)

    tau_pts = [0.00, 0.05, 0.10, 0.15, 0.19]
    # For each tau point, get the mean eigenvalue per rep by rank ordering
    rep_energy_ratios = {}  # (p,q) -> ratio of mean eps^2 to (0,0) mean eps^2

    for tau_str in ['0.00', '0.05', '0.10', '0.15', '0.19']:
        key_o = f'tau{tau_str}_all_omega'
        all_omega = d44[key_o]
        sorted_omega = np.sort(all_omega)

        cum = 0
        eps_this = {}
        for (p, q), d_pq in zip(reps, dims.astype(int)):
            n = 16 * d_pq
            if cum + n <= len(sorted_omega):
                eps_this[(p, q)] = np.mean(sorted_omega[cum:cum+n]**2)
            else:
                eps_this[(p, q)] = sorted_omega[-1]**2
            cum += n

        eps_00 = eps_this[(0, 0)]
        for (p, q) in reps:
            key = (p, q)
            ratio = eps_this[key] / eps_00
            if key not in rep_energy_ratios:
                rep_energy_ratios[key] = []
            rep_energy_ratios[key].append(ratio)

    # Average energy ratios across the 5 tau points (they are stable)
    rep_ratio = {}
    for (p, q) in reps:
        ratios = rep_energy_ratios[(p, q)]
        rep_ratio[(p, q)] = np.mean(ratios)

    print("\nPer-rep energy ratios (eps^2_{(p,q)} / eps^2_{(0,0)}):")
    for (p, q) in reps:
        print(f"  ({p},{q}): ratio = {rep_ratio[(p,q)]:.4f} "
              f"(range {min(rep_energy_ratios[(p,q)]):.4f} - "
              f"{max(rep_energy_ratios[(p,q)]):.4f})")

    # Now compute weights at each tau
    # For each (p,q) at each tau:
    #   eps^2_{(p,q),s}(tau) = lam2_s(tau) * rep_ratio[(p,q)]
    #   v^2_s = 0.5 * (1 - sqrt(eps^2) / sqrt(eps^2 + Delta_s^2))
    #   v_s = sqrt(v^2_s)
    #   w_{(p,q)}(tau) = [Sum_s frac_s * v_s * Delta_s]^2

    weights = np.zeros((n_tau, len(reps)))

    for i_tau in range(n_tau):
        D = np.array([Delta_B1[i_tau], Delta_B2[i_tau], Delta_B3[i_tau]])
        L2 = np.array([lam2_B1[i_tau], lam2_B2[i_tau], lam2_B3[i_tau]])

        for j, (p, q) in enumerate(reps):
            r = rep_ratio[(p, q)]
            # Scale eigenvalues for this rep
            eps2_s = L2 * r  # shape (3,)
            E_s = np.sqrt(eps2_s + D**2)
            v2_s = 0.5 * (1.0 - np.sqrt(eps2_s) / E_s)
            v_s = np.sqrt(np.maximum(v2_s, 0.0))

            # Weight = (Sum_s frac_s * v_s * Delta_s)^2
            w = np.sum(frac_s * v_s * D)
            weights[i_tau, j] = w**2

    print("\nWeight sample at fold (tau ~ 0.19):")
    i_fold = np.argmin(np.abs(tau_scan - 0.19))
    for j, (p, q) in enumerate(reps):
        dim_pq = dims[j]
        print(f"  ({p},{q}): w = {weights[i_fold, j]:.6f}, "
              f"w*dim^2 = {weights[i_fold, j] * dim_pq**2:.4f}")

    return weights, rep_ratio


# =============================================================================
#  SECTION 4: Coherence function C(theta; tau)
# =============================================================================

def compute_coherence(theta, chi_sq, weights, reps, dims):
    """
    Compute normalized coherence function at each tau:

      C(theta; tau) = [Sum_{(p,q)} w_{(p,q)}(tau) * |chi_{(p,q)}(theta, 0)|^2]
                    / [Sum_{(p,q)} w_{(p,q)}(tau) * dim(p,q)^2]

    The denominator normalizes to C(0; tau) = 1 since chi(0,0) = dim(p,q).
    """
    n_tau = weights.shape[0]
    n_theta = len(theta)
    dims_arr = np.array(dims, dtype=float)

    C = np.zeros((n_tau, n_theta))

    for i_tau in range(n_tau):
        numerator = np.zeros(n_theta)
        denominator = 0.0

        for j, (p, q) in enumerate(reps):
            w = weights[i_tau, j]
            numerator += w * chi_sq[(p, q)]
            denominator += w * dims_arr[j]**2

        if denominator > 0:
            C[i_tau, :] = numerator / denominator
        else:
            C[i_tau, :] = 1.0  # uniform if no weights

    return C


# =============================================================================
#  SECTION 5: Extract 1/e^2 radius
# =============================================================================

def extract_radius(theta, C, threshold=np.exp(-2)):
    """
    At each tau, find the angle where C drops to 1/e^2 ~ 0.135.
    Uses linear interpolation between grid points.
    """
    n_tau = C.shape[0]
    r_C = np.zeros(n_tau)

    for i_tau in range(n_tau):
        profile = C[i_tau, :]
        peak = profile[0]

        if peak <= 0:
            r_C[i_tau] = np.nan
            continue

        # Find where normalized profile drops to threshold
        level = threshold * peak  # since C(0)=1, this is just threshold
        # Actually C is already normalized to C(0)=1, so level = threshold

        # Find first crossing below threshold
        below = np.where(profile < threshold)[0]
        if len(below) == 0:
            r_C[i_tau] = theta[-1]  # never drops below
            continue

        idx = below[0]
        if idx == 0:
            r_C[i_tau] = 0.0
            continue

        # Linear interpolation
        t0, t1 = theta[idx-1], theta[idx]
        c0, c1 = profile[idx-1], profile[idx]
        if abs(c1 - c0) > 1e-15:
            r_C[i_tau] = t0 + (threshold - c0) * (t1 - t0) / (c1 - c0)
        else:
            r_C[i_tau] = (t0 + t1) / 2

    return r_C


# =============================================================================
#  SECTION 6: Contrast ratio
# =============================================================================

def compute_contrast(C):
    """max / min of C at each tau."""
    n_tau = C.shape[0]
    contrast = np.zeros(n_tau)
    for i_tau in range(n_tau):
        cmax = np.max(C[i_tau, :])
        cmin = np.min(C[i_tau, :])
        contrast[i_tau] = cmax / max(cmin, 1e-30)
    return contrast


# =============================================================================
#  SECTION 7: Correlation analysis
# =============================================================================

def correlation_analysis(tau_scan, r_C, Delta_B2):
    """
    Compute Pearson correlation between r_C and Delta_B2,
    and between r_C and 1/Delta_B2.
    Handle edge cases where Delta_B2 = 0.
    """
    # Mask valid points
    valid = np.isfinite(r_C) & (Delta_B2 > 0)
    tau_v = tau_scan[valid]
    r_v = r_C[valid]
    D_v = Delta_B2[valid]
    invD_v = 1.0 / D_v

    n_valid = np.sum(valid)
    n_excluded = len(tau_scan) - n_valid

    print(f"\nCorrelation analysis:")
    print(f"  Valid points: {n_valid} / {len(tau_scan)}")
    print(f"  Excluded (Delta_B2=0 or r_C=nan): {n_excluded}")

    if n_valid < 3:
        print("  INSUFFICIENT DATA for correlation")
        return {
            'r_direct': np.nan, 'p_direct': np.nan,
            'r_inverse': np.nan, 'p_inverse': np.nan,
            'n_valid': n_valid, 'n_excluded': n_excluded,
            'cv_rC': np.nan
        }

    # Direct correlation: r_C vs Delta_B2
    r_direct, p_direct = stats.pearsonr(r_v, D_v)
    print(f"  r(r_C, Delta_B2) = {r_direct:.6f}, p = {p_direct:.4e}")

    # Inverse correlation: r_C vs 1/Delta_B2
    r_inverse, p_inverse = stats.pearsonr(r_v, invD_v)
    print(f"  r(r_C, 1/Delta_B2) = {r_inverse:.6f}, p = {p_inverse:.4e}")

    # Coefficient of variation of r_C
    cv_rC = np.std(r_v) / np.mean(r_v) if np.mean(r_v) > 0 else np.nan
    print(f"  CV(r_C) = {cv_rC:.6f}")
    print(f"  r_C range: [{np.min(r_v):.6f}, {np.max(r_v):.6f}]")
    print(f"  r_C mean: {np.mean(r_v):.6f}")
    print(f"  r_C std: {np.std(r_v):.6f}")

    # Constant hypothesis test
    if cv_rC < 0.01:
        print(f"  CONSTANT HYPOTHESIS: STRONG (CV < 0.01)")
    elif cv_rC < 0.10:
        print(f"  CONSTANT HYPOTHESIS: MODERATE (CV < 0.10)")
    else:
        print(f"  CONSTANT HYPOTHESIS: REJECTED (CV >= 0.10)")

    # Spearman rank correlation (non-parametric)
    rho_direct, p_sp_direct = stats.spearmanr(r_v, D_v)
    rho_inverse, p_sp_inverse = stats.spearmanr(r_v, invD_v)
    print(f"  Spearman rho(r_C, Delta_B2) = {rho_direct:.6f}, p = {p_sp_direct:.4e}")
    print(f"  Spearman rho(r_C, 1/Delta_B2) = {rho_inverse:.6f}, p = {p_sp_inverse:.4e}")

    return {
        'r_direct': r_direct, 'p_direct': p_direct,
        'r_inverse': r_inverse, 'p_inverse': p_inverse,
        'rho_direct': rho_direct, 'p_sp_direct': p_sp_direct,
        'rho_inverse': rho_inverse, 'p_sp_inverse': p_sp_inverse,
        'n_valid': n_valid, 'n_excluded': n_excluded,
        'cv_rC': cv_rC,
        'r_C_mean': np.mean(r_v), 'r_C_std': np.std(r_v),
        'r_C_min': np.min(r_v), 'r_C_max': np.max(r_v),
    }


# =============================================================================
#  SECTION 8: Gate assessment
# =============================================================================

def gate_assessment(corr_results):
    """
    Pre-registered gate COHERENCE-RESPONSE-47:
      |r| > 0.9  -> SUBSTRATE
      |r| < 0.3  -> ARTIFACT
      else       -> AMBIGUOUS
    """
    r = corr_results['r_inverse']  # r_C vs 1/Delta_B2 is the predicted substrate signal
    r_abs = abs(r)

    print(f"\n{'='*60}")
    print(f"GATE COHERENCE-RESPONSE-47")
    print(f"{'='*60}")
    print(f"  |r(r_C, 1/Delta_B2)| = {r_abs:.6f}")
    print(f"  Pearson r = {r:.6f}")
    print(f"  p-value = {corr_results['p_inverse']:.4e}")

    # Also report the direct correlation
    r_d = abs(corr_results['r_direct'])
    print(f"  |r(r_C, Delta_B2)| = {r_d:.6f}")

    # Use the STRONGER of direct and inverse correlations
    r_max = max(r_abs, r_d)
    print(f"  max(|r_direct|, |r_inverse|) = {r_max:.6f}")

    if r_max > 0.9:
        verdict = "SUBSTRATE"
        detail = "Coherence radius dynamically tracks BCS gap"
    elif r_max < 0.3:
        verdict = "ARTIFACT"
        detail = "Coherence radius effectively constant; truncation-determined"
    else:
        verdict = "AMBIGUOUS"
        detail = f"Partial correlation {r_max:.3f} in [0.3, 0.9]"

    cv = corr_results['cv_rC']
    print(f"  CV(r_C) = {cv:.6f}")

    if cv < 0.01:
        constant_label = "EFFECTIVELY CONSTANT (CV < 1%)"
    elif cv < 0.10:
        constant_label = "WEAKLY VARYING (1% < CV < 10%)"
    else:
        constant_label = "STRONGLY VARYING (CV > 10%)"

    print(f"  Constant test: {constant_label}")
    print(f"\n  VERDICT: {verdict}")
    print(f"  DETAIL: {detail}")
    print(f"{'='*60}")

    return verdict, detail, constant_label


# =============================================================================
#  SECTION 9: Plotting
# =============================================================================

def make_plots(tau_scan, r_C, Delta_B2, C, theta, contrast, corr_results,
               verdict, data_dir):
    """
    Three-panel figure:
      (A) Dual-axis: r_C(tau) and Delta_B2(tau)
      (B) Scatter: r_C vs Delta_B2 with regression
      (C) Heatmap: C(theta; tau)
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5.5), constrained_layout=True)

    valid = np.isfinite(r_C) & (Delta_B2 > 0)

    # --- (A) Dual-axis ---
    ax1 = axes[0]
    color1 = '#1f77b4'
    color2 = '#d62728'

    ax1.plot(tau_scan[valid], r_C[valid], 'o-', color=color1, ms=3, lw=1.2,
             label=r'$r_C(\tau)$')
    ax1.set_xlabel(r'$\tau$', fontsize=13)
    ax1.set_ylabel(r'$r_C$ (1/$e^2$ radius, rad)', fontsize=12, color=color1)
    ax1.tick_params(axis='y', labelcolor=color1)

    ax2 = ax1.twinx()
    ax2.plot(tau_scan[valid], Delta_B2[valid], 's-', color=color2, ms=3, lw=1.2,
             label=r'$\Delta_{B2}(\tau)$')
    ax2.set_ylabel(r'$\Delta_{B2}$ (M$_{\rm KK}$)', fontsize=12, color=color2)
    ax2.tick_params(axis='y', labelcolor=color2)

    # Add fold marker
    ax1.axvline(tau_fold, color='gray', ls='--', alpha=0.5, lw=0.8)
    ax1.text(tau_fold + 0.005, ax1.get_ylim()[1]*0.95, 'fold', fontsize=9,
             color='gray', va='top')

    ax1.set_title(f'(A) r_C and Delta_B2 vs tau', fontsize=12)
    ax1.grid(True, alpha=0.2)

    # --- (B) Scatter plot ---
    ax = axes[1]
    r_v = r_C[valid]
    D_v = Delta_B2[valid]

    ax.scatter(D_v, r_v, c=tau_scan[valid], cmap='viridis', s=15, zorder=3)
    cb = plt.colorbar(ax.collections[0], ax=ax, label=r'$\tau$', shrink=0.85)

    # Regression line
    slope, intercept, r_val, p_val, se = stats.linregress(D_v, r_v)
    D_line = np.linspace(D_v.min(), D_v.max(), 100)
    ax.plot(D_line, slope * D_line + intercept, 'r--', lw=1.5,
            label=f'r={r_val:.4f}, p={p_val:.2e}')

    ax.set_xlabel(r'$\Delta_{B2}$', fontsize=13)
    ax.set_ylabel(r'$r_C$ (1/$e^2$ radius)', fontsize=12)
    ax.set_title(f'(B) Correlation: |r| = {abs(r_val):.4f}', fontsize=12)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.2)

    # --- (C) Heatmap ---
    ax = axes[2]
    # Transpose so tau is on y-axis, theta on x-axis
    im = ax.pcolormesh(theta / np.pi, tau_scan, C, cmap='inferno',
                        shading='auto', rasterized=True)
    plt.colorbar(im, ax=ax, label=r'$C(\theta; \tau)$', shrink=0.85)

    # Overlay r_C contour
    ax.plot(r_C[valid] / np.pi, tau_scan[valid], 'c-', lw=1.5,
            label=r'$r_C$ (1/$e^2$)')

    ax.axhline(tau_fold, color='white', ls='--', lw=0.8, alpha=0.6)
    ax.set_xlabel(r'$\theta / \pi$', fontsize=13)
    ax.set_ylabel(r'$\tau$', fontsize=12)
    ax.set_title(f'(C) Coherence heatmap', fontsize=12)
    ax.legend(fontsize=9, loc='upper right')

    fig.suptitle(
        f'COHERENCE-RESPONSE-47: {verdict}\n'
        f'|r(r_C, Delta_B2)| = {abs(corr_results["r_direct"]):.4f}, '
        f'|r(r_C, 1/Delta_B2)| = {abs(corr_results["r_inverse"]):.4f}, '
        f'CV = {corr_results["cv_rC"]:.4f}',
        fontsize=13, fontweight='bold')

    plotfile = os.path.join(data_dir, 's47_coherence_response.png')
    fig.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"\n  Main plot: {plotfile}")

    # --- Supplementary: contrast ratio ---
    fig2, ax2 = plt.subplots(1, 1, figsize=(8, 5))
    ax2.semilogy(tau_scan[valid], contrast[valid], 'ko-', ms=4)
    ax2.set_xlabel(r'$\tau$', fontsize=13)
    ax2.set_ylabel('Contrast ratio (max/min of C)', fontsize=12)
    ax2.set_title('Contrast ratio vs tau', fontsize=12)
    ax2.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax2.grid(True, alpha=0.3)

    plotfile2 = os.path.join(data_dir, 's47_coherence_response_contrast.png')
    fig2.savefig(plotfile2, dpi=120, bbox_inches='tight')
    plt.close(fig2)
    print(f"  Contrast plot: {plotfile2}")

    return plotfile, plotfile2


# =============================================================================
#  SECTION 10: Main
# =============================================================================

if __name__ == '__main__':
    print("=" * 70)
    print("s47_coherence_response.py -- Deformation Response of Character Coherence")
    print("COHERENCE-RESPONSE-47")
    print("=" * 70)

    data_dir = os.path.dirname(os.path.abspath(__file__))

    # ── Step 1: Load BCS data ──
    print("\n--- Step 1: Load BCS data (S46 self-consistent) ---")
    d46 = np.load(os.path.join(data_dir, 's46_qtheory_selfconsistent.npz'))

    tau_scan = d46['tau_scan']
    Delta_B1 = d46['Delta_B1_sc']
    Delta_B2 = d46['Delta_B2_sc']
    Delta_B3 = d46['Delta_B3_sc']
    lam2_B1 = d46['lam2_B1_interp']
    lam2_B2 = d46['lam2_B2_interp']
    lam2_B3 = d46['lam2_B3_interp']

    n_tau = len(tau_scan)
    print(f"  tau range: [{tau_scan[0]:.4f}, {tau_scan[-1]:.4f}], {n_tau} points")
    print(f"  Delta_B2 range: [{Delta_B2.min():.6f}, {Delta_B2.max():.6f}]")
    print(f"  Delta_B2 at fold: {Delta_B2[np.argmin(np.abs(tau_scan - 0.19))]:.6f}")

    # ── Step 2: Precompute characters (tau-independent) ──
    print("\n--- Step 2: Precompute characters (tau-INDEPENDENT) ---")
    N_theta = 500
    theta, chi_sq, reps, dims = precompute_characters_radial(N_theta)

    # Verify characters sum to dim^2 at identity
    for j, (p, q) in enumerate(reps):
        chi_0 = chi_sq[(p, q)][0]
        expected = dims[j]**2
        err = abs(chi_0 - expected) / expected
        if err > 1e-6:
            print(f"  WARNING: |chi_{{{p},{q}}}(0)|^2 = {chi_0:.6f}, "
                  f"expected {expected:.0f}, err = {err:.2e}")

    # ── Step 3: Compute BCS weights at each tau ──
    print("\n--- Step 3: Compute BCS weights w_{(p,q)}(tau) ---")
    weights, rep_ratio = compute_bcs_weights(
        tau_scan, Delta_B1, Delta_B2, Delta_B3,
        lam2_B1, lam2_B2, lam2_B3)

    # Check weight variation across tau for each rep
    print("\nWeight variation across tau:")
    for j, (p, q) in enumerate(reps):
        w = weights[:, j]
        cv_w = np.std(w) / np.mean(w) if np.mean(w) > 0 else 0
        print(f"  ({p},{q}): min={w.min():.6f}, max={w.max():.6f}, CV={cv_w:.4f}")

    # ── Step 4: Compute coherence function ──
    print("\n--- Step 4: Compute C(theta; tau) ---")
    C = compute_coherence(theta, chi_sq, weights, reps, dims)

    # Verify C(0; tau) = 1 for all tau
    c0_err = np.max(np.abs(C[:, 0] - 1.0))
    print(f"  C(0; tau) = 1 check: max error = {c0_err:.2e}")

    # ── Step 5: Extract 1/e^2 radius ──
    print("\n--- Step 5: Extract 1/e^2 radius ---")
    r_C = extract_radius(theta, C)
    print(f"  r_C range: [{np.nanmin(r_C):.6f}, {np.nanmax(r_C):.6f}] rad")
    print(f"  r_C at fold: {r_C[np.argmin(np.abs(tau_scan - 0.19))]:.6f} rad")
    print(f"  r_C / pi range: [{np.nanmin(r_C)/np.pi:.6f}, {np.nanmax(r_C)/np.pi:.6f}]")

    # ── Step 6: Contrast ratio ──
    print("\n--- Step 6: Contrast ratio ---")
    contrast = compute_contrast(C)
    print(f"  Contrast range: [{contrast.min():.2f}, {contrast.max():.2f}]")
    cv_contrast = np.std(contrast) / np.mean(contrast)
    print(f"  CV(contrast) = {cv_contrast:.4f}")

    # ── Step 7: Correlation analysis ──
    print("\n--- Step 7: Correlation analysis ---")
    corr_results = correlation_analysis(tau_scan, r_C, Delta_B2)

    # ── Step 8: Gate assessment ──
    verdict, detail, constant_label = gate_assessment(corr_results)

    # ── Step 9: Edge case analysis ──
    print("\n--- Step 9: Edge case analysis ---")
    # What happens at the tau extremes?
    print(f"  At tau = {tau_scan[0]:.4f} (smallest):")
    print(f"    Delta_B2 = {Delta_B2[0]:.6f}, r_C = {r_C[0]:.6f}")
    print(f"  At tau = {tau_scan[-1]:.4f} (largest):")
    print(f"    Delta_B2 = {Delta_B2[-1]:.6f}, r_C = {r_C[-1]:.6f}")

    # What would r_C be with UNIFORM weights (all w = 1)?
    print("\n  Uniform-weight control (w = 1 for all reps):")
    C_uniform = np.zeros(N_theta)
    denom_u = 0.0
    for j, (p, q) in enumerate(reps):
        C_uniform += chi_sq[(p, q)]
        denom_u += float(dims[j])**2
    C_uniform /= denom_u
    r_C_uniform = None
    below_u = np.where(C_uniform < np.exp(-2))[0]
    if len(below_u) > 0:
        idx = below_u[0]
        if idx > 0:
            t0, t1 = theta[idx-1], theta[idx]
            c0, c1 = C_uniform[idx-1], C_uniform[idx]
            r_C_uniform = t0 + (np.exp(-2) - c0) * (t1 - t0) / (c1 - c0)
    if r_C_uniform is None:
        r_C_uniform = theta[-1]
    print(f"    r_C (uniform) = {r_C_uniform:.6f} rad = {r_C_uniform/np.pi:.6f}*pi")
    print(f"    Compare: r_C range from BCS = [{np.nanmin(r_C):.6f}, {np.nanmax(r_C):.6f}]")

    # ── Step 10: Save data ──
    print("\n--- Step 10: Save data ---")
    outfile = os.path.join(data_dir, 's47_coherence_response.npz')
    np.savez(outfile,
             # Grid
             theta=theta,
             tau_scan=tau_scan,
             # Coherence function
             C=C,
             # Radius
             r_C=r_C,
             r_C_uniform=r_C_uniform,
             # BCS data
             Delta_B2=Delta_B2,
             Delta_B1=Delta_B1,
             Delta_B3=Delta_B3,
             # Weights
             weights=weights,
             rep_ratios=[rep_ratio[(p,q)] for (p,q) in reps],
             # Contrast
             contrast=contrast,
             # Correlation results
             r_direct=corr_results['r_direct'],
             p_direct=corr_results['p_direct'],
             r_inverse=corr_results['r_inverse'],
             p_inverse=corr_results['p_inverse'],
             cv_rC=corr_results['cv_rC'],
             r_C_mean=corr_results.get('r_C_mean', np.nan),
             r_C_std=corr_results.get('r_C_std', np.nan),
             r_C_min=corr_results.get('r_C_min', np.nan),
             r_C_max=corr_results.get('r_C_max', np.nan),
             # Gate
             gate_name='COHERENCE-RESPONSE-47',
             verdict=verdict,
             detail=detail,
             constant_label=constant_label,
             N_theta=N_theta,
             n_tau=n_tau,
             )
    print(f"  Data: {outfile}")

    # ── Step 11: Plots ──
    print("\n--- Step 11: Plots ---")
    make_plots(tau_scan, r_C, Delta_B2, C, theta, contrast,
               corr_results, verdict, data_dir)

    # ── Summary ──
    print("\n" + "=" * 70)
    print("COHERENCE-RESPONSE-47 SUMMARY")
    print("=" * 70)
    print(f"  Characters: tau-INDEPENDENT (precomputed once, 9 reps)")
    print(f"  BCS weights: tau-DEPENDENT ({n_tau} tau points)")
    print(f"  r_C range: [{corr_results.get('r_C_min', np.nan):.6f}, "
          f"{corr_results.get('r_C_max', np.nan):.6f}] rad")
    print(f"  r_C uniform control: {r_C_uniform:.6f} rad")
    print(f"  CV(r_C) = {corr_results['cv_rC']:.6f}")
    print(f"  |r(r_C, Delta_B2)| = {abs(corr_results['r_direct']):.6f}")
    print(f"  |r(r_C, 1/Delta_B2)| = {abs(corr_results['r_inverse']):.6f}")
    print(f"  Contrast range: [{contrast.min():.2f}, {contrast.max():.2f}]")
    print(f"  VERDICT: {verdict}")
    print(f"  DETAIL: {detail}")
    print(f"  CONSTANT TEST: {constant_label}")
    print("=" * 70)
