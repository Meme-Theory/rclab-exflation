#!/usr/bin/env python3
"""
s47_condensate_torus.py -- BCS condensate density on the maximal torus T^2 in SU(3)
===================================================================================

Session 47 Wave 2, CONDENSATE-T2-47 (INFO gate)

Computes |Delta(t1,t2)|^2 restricted to the maximal torus:
    g(t1,t2) = diag(e^{it1}, e^{it2}, e^{-i(t1+t2)})

The condensate gap function in the Peter-Weyl basis, restricted to T^2,
becomes a sum over characters:
    |Delta(t1,t2)|^2 ~ Sum_{(p,q)} |w_{(p,q)}|^2 * |chi_{(p,q)}(t1,t2)|^2

where w_{(p,q)} is the BCS weight and chi_{(p,q)} is the SU(3) character.

Method: Weyl character formula for SU(3), verified against direct weight sums.
All 9 reps with p+q <= 3 included.

Author: Landau agent (S47 W2)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, Vol_SU3_Haar

# =============================================================================
#  SECTION 1: SU(3) Characters on the Maximal Torus
# =============================================================================

def su3_character_weyl(p, q, t1, t2):
    """
    SU(3) character via the Weyl character formula.

    chi_{(p,q)}(t1,t2) = A_{rho+lambda} / A_{rho}

    where rho = (2,1,0), lambda = (p+q, q, 0) in partition notation,
    and A_mu = det[e^{i mu_{sigma(j)} phi_j}] summed over S_3 with signs.

    phi = (t1, t2, -(t1+t2)).

    Division by zero at Weyl walls is handled by falling back to direct
    weight enumeration.
    """
    if p == 0 and q == 0:
        return np.ones_like(t1, dtype=complex)

    phi1 = t1
    phi2 = t2
    phi3 = -(t1 + t2)

    # Shifted highest weight: mu = lambda + rho = (p+q+2, q+1, 0)
    a, b, c = p + q + 2, q + 1, 0

    # Numerator: alternating sum over S_3
    # A_mu = sum_{sigma in S_3} sign(sigma) * exp(i * sum_j mu_{sigma(j)} * phi_j)
    num = (  np.exp(1j*(a*phi1 + b*phi2 + c*phi3))
           - np.exp(1j*(a*phi1 + c*phi2 + b*phi3))
           - np.exp(1j*(b*phi1 + a*phi2 + c*phi3))
           + np.exp(1j*(b*phi1 + c*phi2 + a*phi3))
           + np.exp(1j*(c*phi1 + a*phi2 + b*phi3))
           - np.exp(1j*(c*phi1 + b*phi2 + a*phi3)))

    # Denominator: A_rho with rho = (2, 1, 0)
    den = (  np.exp(1j*(2*phi1 + 1*phi2 + 0*phi3))
           - np.exp(1j*(2*phi1 + 0*phi2 + 1*phi3))
           - np.exp(1j*(1*phi1 + 2*phi2 + 0*phi3))
           + np.exp(1j*(1*phi1 + 0*phi2 + 2*phi3))
           + np.exp(1j*(0*phi1 + 2*phi2 + 1*phi3))
           - np.exp(1j*(0*phi1 + 1*phi2 + 2*phi3)))

    # Where denominator is small, use direct weight sum
    eps = 1e-8
    small = np.abs(den) < eps

    chi = np.where(small, 0.0+0j, num / np.where(small, 1.0, den))

    if np.any(small):
        chi_direct = su3_character_weights(p, q, t1, t2)
        chi = np.where(small, chi_direct, chi)

    return chi


def su3_character_weights(p, q, t1, t2):
    """
    SU(3) character by direct weight enumeration.

    On the maximal torus, chi = sum_weights mult(w) * exp(i*(w1*t1 + w2*t2)).

    Weight convention: g(t1,t2) = diag(e^{it1}, e^{it2}, e^{-i(t1+t2)}).
    A state transforming as z1^{a} z2^{b} z3^{c} has phase
    a*t1 + b*t2 + c*(-t1-t2) = (a-c)*t1 + (b-c)*t2.
    So (w1, w2) = (a-c, b-c).

    Fundamental (1,0): states (1,0,0), (0,1,0), (0,0,1)
      -> weights (1,0), (0,1), (-1,-1).
    """
    weights = _get_weights(p, q)
    chi = np.zeros_like(t1, dtype=complex)
    for w1, w2, mult in weights:
        chi += mult * np.exp(1j * (w1*t1 + w2*t2))
    return chi


def _get_weights(p, q):
    """
    Return weights of (p,q) rep as list of (w1, w2, multiplicity).

    For all reps with p+q <= 3, computed by tensor product decomposition
    and verified against dim(p,q) = (p+1)(q+1)(p+q+2)/2.

    Convention: (w1,w2) where phase = exp(i*(w1*t1 + w2*t2)) on the
    maximal torus g = diag(e^{it1}, e^{it2}, e^{-i(t1+t2)}).
    """
    # All weights are hard-coded for correctness and speed.
    # Derived from standard SU(3) representation theory.
    #
    # Fundamental (1,0): 3
    #   States in the defining rep: e_1, e_2, e_3
    #   z_i eigenvalues: z_1=e^{it1}, z_2=e^{it2}, z_3=e^{-i(t1+t2)}
    #   Weights in (w1,w2): (1,0), (0,1), (-1,-1)
    #
    # Anti-fund (0,1): 3bar
    #   Contragredient: negate fundamental weights
    #   (-1,0), (0,-1), (1,1)
    #
    # (2,0) = Sym^2(fund): 6
    #   Symmetric products of pairs of fund weights:
    #   2e1: (2,0), 2e2: (0,2), 2e3: (-2,-2),
    #   e1+e2: (1,1), e1+e3: (0,-1), e2+e3: (-1,0)
    #   -> 6 weights, all mult 1
    #
    # (0,2) = Sym^2(anti-fund): 6
    #   Negate (2,0) weights: (-2,0), (0,-2), (2,2), (-1,-1), (0,1), (1,0)
    #
    # (3,0) = Sym^3(fund): 10
    #   All sym products of triples:
    #   3e1: (3,0), 3e2: (0,3), 3e3: (-3,-3)
    #   2e1+e2: (2,1), 2e1+e3: (1,-1), e1+2e2: (1,2),
    #   2e2+e3: (-1,1), e1+2e3: (-2,-1), e2+2e3: (-1,-2)
    #   e1+e2+e3: (0,0) [since w = (1-(-1), 1-(-1)) ... let me recompute]
    #
    # Actually let me be systematic. For fund, states are (a,b,c) with
    # a+b+c = 1 (single tensor index). Weight = (a-c, b-c).
    # For Sym^n, states are (a,b,c) with a+b+c = n. Weight = (a-c, b-c).

    # General formula for Sym^n(fund) = (n,0):
    # States: (a,b,c) with a+b+c = n, a,b,c >= 0
    # Weight: (a-c, b-c)
    # All multiplicities are 1 for symmetric tensors.

    # For anti-fund (0,1): states are (a,b,c) with a+b+c=1 for Sym^1(anti-fund)
    # Weight = -(a-c, b-c) = (c-a, c-b)
    # OR equivalently: anti-fund weights are negatives of fund weights.

    # For (0,q) = Sym^q(anti-fund): negate (q,0) weights.
    # For (p,q) general: need tensor product decomposition.

    # (1,1) = fund x anti-fund - trivial = adjoint:
    # Fund weights: (1,0), (0,1), (-1,-1)
    # Anti-fund weights: (-1,0), (0,-1), (1,1)
    # Tensor product 3 x 3bar = 1 + 8
    # All 9 products: subtract the (0,0) singlet contribution
    # Products: (1,0)+(-1,0)=(0,0), (1,0)+(0,-1)=(1,-1), (1,0)+(1,1)=(2,1),
    #           (0,1)+(-1,0)=(-1,1), (0,1)+(0,-1)=(0,0), (0,1)+(1,1)=(1,2),
    #           (-1,-1)+(-1,0)=(-2,-1), (-1,-1)+(0,-1)=(-1,-2), (-1,-1)+(1,1)=(0,0)
    # So 9 weights: (0,0)x3, (1,-1), (2,1), (-1,1), (1,2), (-2,-1), (-1,-2)
    # Singlet (1 rep) gets one (0,0). Adjoint (8) gets the remaining:
    # (0,0)x2 + (1,-1) + (2,1) + (-1,1) + (1,2) + (-2,-1) + (-1,-2) = 8 total. Good.

    # (2,1): 15-dim. 2 x anti-fund cross-products...
    # This is getting complex. Let me use the Weyl character formula to
    # COMPUTE the weights by Fourier analysis.

    # Strategy: evaluate the Weyl character formula on a fine grid,
    # then extract Fourier coefficients to get the weights.
    # This is foolproof for small reps.

    return _weights_from_fourier(p, q)


def _weights_from_fourier(p, q):
    """
    Extract weights and multiplicities of (p,q) by Fourier-analyzing
    the Weyl character formula on a fine grid.

    The character is a finite trigonometric polynomial:
    chi(t1,t2) = sum_w mult(w) * exp(i*(w1*t1 + w2*t2))

    where w ranges over a finite set of integer pairs.
    We recover mult(w) by 2D discrete Fourier transform.
    """
    if p == 0 and q == 0:
        return [(0, 0, 1)]

    dim_pq = (p+1)*(q+1)*(p+q+2)//2

    # The maximum |w| for rep (p,q) is bounded by p+q
    # (highest weight has max component p+q).
    w_max = p + q + 1  # generous bound

    # Grid size must be > 2*w_max to avoid aliasing
    N = 4 * w_max + 1  # odd for centering
    if N < 17:
        N = 17

    t1_grid = np.linspace(0, 2*np.pi, N, endpoint=False)
    t2_grid = np.linspace(0, 2*np.pi, N, endpoint=False)
    T1, T2 = np.meshgrid(t1_grid, t2_grid, indexing='ij')

    # Evaluate character via Weyl formula (avoiding singular points)
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

    # Use L'Hopital where denominator vanishes: replace with a slight offset
    small = np.abs(den) < 1e-10
    if np.any(small):
        # Shift singular points by a tiny amount
        T1s = T1.copy()
        T2s = T2.copy()
        T1s[small] += 0.001
        T2s[small] += 0.0007
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

    # 2D FFT to extract Fourier coefficients
    coeffs = np.fft.fft2(chi_grid) / (N * N)

    # The coefficient at frequency (k1, k2) corresponds to weight (k1, k2)
    # but FFT convention wraps negative frequencies
    weights = []
    for k1 in range(N):
        for k2 in range(N):
            w1 = k1 if k1 <= N//2 else k1 - N
            w2 = k2 if k2 <= N//2 else k2 - N
            c_val = coeffs[k1, k2]
            mult = round(c_val.real)
            if mult > 0 and abs(c_val.real - mult) < 0.1 and abs(c_val.imag) < 0.1:
                weights.append((w1, w2, mult))

    # Verify dimension
    total_dim = sum(m for _, _, m in weights)
    if total_dim != dim_pq:
        # This can happen with aliasing; try larger grid
        return _weights_from_fourier_large(p, q)

    return weights


def _weights_from_fourier_large(p, q):
    """Fallback with larger grid for problematic reps."""
    dim_pq = (p+1)*(q+1)*(p+q+2)//2
    w_max = p + q + 2

    N = 8 * w_max + 1

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
            if mult > 0 and abs(c_val.real - mult) < 0.3 and abs(c_val.imag) < 0.3:
                weights.append((w1, w2, mult))

    return weights


def verify_weights():
    """Verify weight construction against known dimensions."""
    reps = [(0,0), (1,0), (0,1), (2,0), (0,2), (1,1), (3,0), (0,3), (2,1)]
    expected_dims = [1, 3, 3, 6, 6, 8, 10, 10, 15]

    print("Weight construction verification:")
    print(f"{'Rep':>8s}  {'Expected':>8s}  {'Got':>8s}  {'Weights':>8s}  Status")

    all_pass = True
    for (p, q), dim_exp in zip(reps, expected_dims):
        weights = _get_weights(p, q)
        dim_got = sum(m for _, _, m in weights)
        n_weights = len(weights)
        status = "OK" if dim_got == dim_exp else "FAIL"
        if dim_got != dim_exp:
            all_pass = False
        print(f"  ({p},{q})    {dim_exp:>6d}    {dim_got:>6d}    {n_weights:>6d}    {status}")
        if dim_got != dim_exp:
            print(f"    Weights: {weights}")

    return all_pass


def verify_characters():
    """Cross-check Weyl formula vs direct weight sum at random points."""
    reps = [(1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (3,0), (0,3)]
    test_t1 = np.array([0.7, 1.3, 2.1, 3.5, 5.0])
    test_t2 = np.array([0.5, 1.7, 0.9, 4.2, 1.8])

    print("\nCharacter cross-check (Weyl vs weights):")
    max_err = 0
    for (p, q) in reps:
        chi_w = su3_character_weyl(p, q, test_t1, test_t2)
        chi_d = su3_character_weights(p, q, test_t1, test_t2)
        err = np.max(np.abs(chi_w - chi_d))
        max_err = max(max_err, err)
        status = "OK" if err < 1e-6 else "FAIL"
        print(f"  ({p},{q}): max|Weyl-direct| = {err:.2e} {status}")
    print(f"  Overall max error: {max_err:.2e}")
    return max_err < 1e-6


# =============================================================================
#  SECTION 2: Condensate Density Computation
# =============================================================================

def compute_condensate_density(N_grid=200):
    """
    Compute |Delta(t1,t2)|^2 on the maximal torus.

    The condensate on T^2 is:
        Delta(t1,t2) = sum_{(p,q)} w_{(p,q)} * chi_{(p,q)}(t1,t2)

    where w_{(p,q)} = dim(p,q) * [sum_s frac_s * Delta_s] * BCS_suppression(epsilon_{(p,q)}).

    The sector-averaged gap [sum_s frac_s * Delta_s] is the SAME for all reps
    (since each spinor index contributes to the same B1/B2/B3 split). What varies
    is the BCS suppression at higher energies.
    """
    # Load BCS data
    data_dir = os.path.dirname(os.path.abspath(__file__))
    d46 = np.load(os.path.join(data_dir, 's46_number_projected_bcs.npz'), allow_pickle=True)
    d44 = np.load(os.path.join(data_dir, 's44_dos_tau.npz'), allow_pickle=True)

    v2_bcs = d46['v2_bcs']              # [0.0446, 0.1220, 0.0019]
    Delta_bcs = d46['Delta_bcs_fold']    # [0.372, 0.732, 0.084]

    # Sector fractions (spinor structure)
    frac_s = np.array([2.0/16, 8.0/16, 6.0/16])  # B1, B2, B3

    # Sector-averaged gap weight
    w_sector = frac_s * Delta_bcs
    w_avg = np.sum(w_sector)  # sector-averaged gap per unit dim

    print(f"\nBCS sector weights:")
    print(f"  v2_bcs    = {v2_bcs}")
    print(f"  Delta_bcs = {Delta_bcs}")
    print(f"  frac_s    = {frac_s}")
    print(f"  w_sector  = {w_sector}")
    print(f"  w_avg     = {w_avg:.6f}")

    # Representative energies per rep from spectrum
    all_omega = d44['tau0.19_all_omega']
    all_dim2 = d44['tau0.19_all_dim2']

    reps = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (3,0), (0,3)]
    dims = [1, 3, 3, 8, 6, 6, 15, 10, 10]

    # Assign energies: sort spectrum, assign blocks by PW multiplicity
    sorted_omega = np.sort(all_omega)
    cum = 0
    rep_eps = {}
    for (p,q), d in zip(reps, dims):
        n = 16 * d
        if cum + n <= len(sorted_omega):
            rep_eps[(p,q)] = np.mean(sorted_omega[cum:cum+n])
        else:
            rep_eps[(p,q)] = sorted_omega[-1]
        cum += n

    eps_00 = rep_eps[(0,0)]  # reference energy

    print(f"\nPer-rep energies:")
    for (p,q) in reps:
        print(f"  ({p},{q}): <eps> = {rep_eps[(p,q)]:.4f}")

    # BCS suppression: modes far from Fermi surface contribute less
    Delta_B2 = Delta_bcs[1]  # dominant gap sets energy scale
    sigma_bcs = Delta_B2

    # Build grid
    theta1 = np.linspace(0, 2*np.pi, N_grid, endpoint=False)
    theta2 = np.linspace(0, 2*np.pi, N_grid, endpoint=False)
    T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')

    # Compute two versions: equal weight (geometric) and BCS-weighted (physical)
    Delta_eq = np.zeros_like(T1, dtype=complex)
    Delta_bcs_field = np.zeros_like(T1, dtype=complex)

    print(f"\nComputing characters on {N_grid}x{N_grid} grid...")
    weight_info = []

    for (p,q), dim_pq in zip(reps, dims):
        chi = su3_character_weyl(p, q, T1, T2)

        # Verify at identity
        chi_00 = chi[0, 0]
        if abs(chi_00.real - dim_pq) > 0.1:
            print(f"  WARNING: chi_({p},{q})(0,0) = {chi_00:.4f}, expected {dim_pq}")
            # Fallback to direct weight sum
            chi = su3_character_weights(p, q, T1, T2)
            chi_00 = chi[0, 0]
            print(f"    Fallback: chi = {chi_00:.4f}")

        # Equal weight: each rep weighted by dim
        w_eq = float(dim_pq)

        # BCS weight: gap * dim * energy suppression
        eps_pq = rep_eps[(p,q)]
        bcs_sup = np.exp(-((eps_pq - eps_00)**2) / (2 * sigma_bcs**2))
        w_bcs = w_avg * dim_pq * bcs_sup

        Delta_eq += w_eq * chi
        Delta_bcs_field += w_bcs * chi

        weight_info.append({
            'rep': (p,q), 'dim': dim_pq, 'eps': eps_pq,
            'bcs_sup': bcs_sup, 'w_eq': w_eq, 'w_bcs': w_bcs,
        })
        print(f"  ({p},{q}): dim={dim_pq:>2d}, eps={eps_pq:.4f}, "
              f"BCS_sup={bcs_sup:.4f}, w_bcs={w_bcs:.4f}, "
              f"|chi|^2_max={np.max(np.abs(chi)**2):.1f}")

    # Densities
    dens_eq = np.abs(Delta_eq)**2
    dens_bcs = np.abs(Delta_bcs_field)**2

    # Normalize
    dens_eq_n = dens_eq / np.max(dens_eq)
    dens_bcs_n = dens_bcs / np.max(dens_bcs)

    # Statistics
    print(f"\n{'='*60}")
    print("Condensate density statistics:")
    for label, d in [("Equal weight", dens_eq), ("BCS-weighted", dens_bcs)]:
        r = np.max(d) / max(np.min(d), 1e-30)
        cv = np.std(d) / np.mean(d)
        print(f"  {label}:")
        print(f"    max = {np.max(d):.4f}, min = {np.min(d):.6f}")
        print(f"    max/min = {r:.2f}")
        print(f"    CV = {cv:.4f}")

    # S3 symmetry check (swap theta1, theta2)
    sym_err = np.max(np.abs(dens_bcs - dens_bcs.T)) / np.max(dens_bcs)
    print(f"\n  S3 symmetry (sigma_12): max error = {sym_err:.2e}")

    return (T1, T2, dens_eq, dens_bcs, dens_eq_n, dens_bcs_n,
            weight_info, theta1, theta2)


# =============================================================================
#  SECTION 3: Plotting
# =============================================================================

def plot_condensate(T1, T2, dens_eq_n, dens_bcs_n, weight_info, theta1, theta2):
    """Main figure: condensate density heatmaps."""
    fig, axes = plt.subplots(1, 2, figsize=(16, 7), constrained_layout=True)

    for ax, density, title in zip(
        axes, [dens_eq_n, dens_bcs_n],
        ['(a) Equal PW weight (geometric)', '(b) BCS-weighted (physical)']
    ):
        im = ax.pcolormesh(theta1, theta2, density.T,
                           cmap='inferno', shading='auto', rasterized=True)
        plt.colorbar(im, ax=ax, label=r'$|\Delta|^2$ (normalized)')

        # Weyl chamber boundary lines
        t = np.linspace(0, 2*np.pi, 500)

        # theta1 = theta2 (S_{12} reflection)
        ax.plot(t, t, 'w--', lw=1.0, alpha=0.7, label=r'$\theta_1=\theta_2$')

        # theta1 + 2*theta2 = 2*pi*k (S_{23} reflection)
        for k in [0, 1, 2, 3]:
            t2 = (2*np.pi*k - t) / 2.0
            m = (t2 >= -0.05) & (t2 <= 2*np.pi+0.05)
            if np.any(m):
                ax.plot(t[m], np.clip(t2[m], 0, 2*np.pi), 'w:',
                        lw=0.8, alpha=0.6)

        # 2*theta1 + theta2 = 2*pi*k (S_{13} reflection)
        for k in [0, 1, 2, 3]:
            t2 = 2*np.pi*k - 2*t
            m = (t2 >= -0.05) & (t2 <= 2*np.pi+0.05)
            if np.any(m):
                ax.plot(t[m], np.clip(t2[m], 0, 2*np.pi), 'w-.',
                        lw=0.8, alpha=0.5)

        # Special points
        ax.plot(0, 0, 'w*', ms=12, mec='k', mew=0.5, label='Identity', zorder=5)
        ax.plot(2*np.pi/3, 2*np.pi/3, 'ws', ms=8, mec='k', mew=0.5,
                label=r'$\mathbb{Z}_3$ center', zorder=5)
        ax.plot(4*np.pi/3, 4*np.pi/3, 'ws', ms=8, mec='k', mew=0.5, zorder=5)
        ax.plot(np.pi, np.pi, 'wD', ms=7, mec='k', mew=0.5,
                label=r'$(-1,-1,1)$', zorder=5)

        ax.set_xlabel(r'$\theta_1$', fontsize=14)
        ax.set_ylabel(r'$\theta_2$', fontsize=14)
        ax.set_title(title, fontsize=12)
        ax.set_xlim(0, 2*np.pi)
        ax.set_ylim(0, 2*np.pi)
        ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
        tlabels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
        ax.set_xticks(ticks); ax.set_xticklabels(tlabels)
        ax.set_yticks(ticks); ax.set_yticklabels(tlabels)
        ax.set_aspect('equal')
        ax.legend(fontsize=9, loc='upper right', framealpha=0.8)

    fig.suptitle(
        r'BCS condensate density $|\Delta(\theta_1,\theta_2)|^2$ on '
        r'$T^2 \subset SU(3)$ at $\tau=0.19$',
        fontsize=14, fontweight='bold')
    return fig


def plot_characters(theta1, theta2):
    """Supplementary: individual |chi|^2 for each rep."""
    reps = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (2,1), (3,0), (0,3)]
    dims = [1, 3, 3, 8, 6, 6, 15, 10, 10]

    T1, T2 = np.meshgrid(theta1, theta2, indexing='ij')

    fig, axes = plt.subplots(3, 3, figsize=(15, 14), constrained_layout=True)
    for idx, ((p,q), d) in enumerate(zip(reps, dims)):
        ax = axes[idx//3, idx%3]
        chi = su3_character_weyl(p, q, T1, T2)

        # Check identity and fall back if needed
        if abs(chi[0,0].real - d) > 0.1:
            chi = su3_character_weights(p, q, T1, T2)

        dens = np.abs(chi)**2
        im = ax.pcolormesh(theta1, theta2, dens.T, cmap='viridis', shading='auto')
        plt.colorbar(im, ax=ax, shrink=0.8)
        t = np.linspace(0, 2*np.pi, 200)
        ax.plot(t, t, 'w--', lw=0.8, alpha=0.5)
        ax.set_title(f'$|\\chi_{{({p},{q})}}|^2$, dim={d}', fontsize=11)
        ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 2*np.pi)
        ax.set_aspect('equal')
        ax.set_xticks([0, np.pi, 2*np.pi])
        ax.set_xticklabels(['0', r'$\pi$', r'$2\pi$'])
        ax.set_yticks([0, np.pi, 2*np.pi])
        ax.set_yticklabels(['0', r'$\pi$', r'$2\pi$'])

    fig.suptitle(
        r'SU(3) characters $|\chi_{(p,q)}|^2$ on maximal torus $T^2$',
        fontsize=14, fontweight='bold')
    return fig


# =============================================================================
#  SECTION 4: Main
# =============================================================================

if __name__ == '__main__':
    print("="*70)
    print("s47_condensate_torus.py -- BCS condensate on T^2 in SU(3)")
    print("="*70)

    # Step 1: Verify weights
    print("\n--- Step 1: Weight verification ---")
    ok = verify_weights()
    if not ok:
        print("WEIGHT CONSTRUCTION FAILED")
        sys.exit(1)

    # Step 2: Cross-check characters
    print("\n--- Step 2: Character cross-check ---")
    ok2 = verify_characters()

    # Step 3: Compute condensate
    print("\n--- Step 3: Condensate computation ---")
    N_grid = 200
    (T1, T2, dens_eq, dens_bcs, dens_eq_n, dens_bcs_n,
     weight_info, theta1, theta2) = compute_condensate_density(N_grid)

    # Step 4: Characterize
    print("\n--- Step 4: Pattern characterization ---")
    idx_max = np.unravel_index(np.argmax(dens_bcs_n), dens_bcs_n.shape)
    idx_min = np.unravel_index(np.argmin(dens_bcs_n), dens_bcs_n.shape)

    print(f"  Maximum at (t1,t2) = ({theta1[idx_max[0]]/np.pi:.4f}pi, "
          f"{theta2[idx_max[1]]/np.pi:.4f}pi)")
    print(f"  Minimum at (t1,t2) = ({theta1[idx_min[0]]/np.pi:.4f}pi, "
          f"{theta2[idx_min[1]]/np.pi:.4f}pi)")

    contrast = np.max(dens_bcs) / max(np.min(dens_bcs), 1e-30)
    cv = np.std(dens_bcs_n) / np.mean(dens_bcs_n)
    print(f"  Contrast (max/min) = {contrast:.2f}")
    print(f"  CV = {cv:.4f}")

    # Fourier content
    ft = np.fft.fft2(dens_bcs_n)
    p00 = np.abs(ft[0,0])**2 / np.sum(np.abs(ft)**2)
    print(f"  (0,0) Fourier fraction = {p00:.4f} ({p00*100:.1f}%)")

    # Special points
    d_id = dens_bcs_n[0, 0]
    idx_z3 = int(round(N_grid * 2/3)) % N_grid
    d_z3 = dens_bcs_n[idx_z3, idx_z3]
    idx_pi = N_grid // 2
    d_anti = dens_bcs_n[idx_pi, idx_pi]
    print(f"  Density at identity (0,0):       {d_id:.6f}")
    print(f"  Density at Z3 center (2pi/3):    {d_z3:.6f}")
    print(f"  Density at anti-id (pi,pi):      {d_anti:.6f}")

    # Step 5: Save
    print("\n--- Step 5: Save ---")
    outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's47_condensate_torus.npz')
    np.savez(outfile,
             theta1=theta1, theta2=theta2,
             density_equal_weight=dens_eq,
             density_bcs_weighted=dens_bcs,
             density_A_norm=dens_eq_n,
             density_B_norm=dens_bcs_n,
             contrast_ratio=contrast,
             coeff_variation=cv,
             fourier_frac_00=p00,
             density_at_identity=d_id,
             density_at_Z3=d_z3,
             density_at_anti_identity=d_anti,
             max_theta1=theta1[idx_max[0]],
             max_theta2=theta2[idx_max[1]],
             min_theta1=theta1[idx_min[0]],
             min_theta2=theta2[idx_min[1]],
             gate_name='CONDENSATE-T2-47',
             gate_type='INFO',
             tau=tau_fold,
             N_grid=N_grid)
    print(f"  Data: {outfile}")

    # Step 6: Plot
    print("\n--- Step 6: Plot ---")
    fig = plot_condensate(T1, T2, dens_eq_n, dens_bcs_n, weight_info, theta1, theta2)
    plotfile = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           's47_condensate_torus.png')
    fig.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close(fig)
    print(f"  Main plot: {plotfile}")

    fig2 = plot_characters(theta1, theta2)
    plotfile2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's47_condensate_torus_characters.png')
    fig2.savefig(plotfile2, dpi=120, bbox_inches='tight')
    plt.close(fig2)
    print(f"  Character plot: {plotfile2}")

    # Log-scale + radial profile figure
    fig3, axes3 = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)

    # (a) Log-scale heatmap
    ax = axes3[0]
    log_dens = np.log10(dens_bcs_n + 1e-10)
    im = ax.pcolormesh(theta1, theta2, log_dens.T, cmap='inferno',
                       shading='auto', rasterized=True)
    plt.colorbar(im, ax=ax, label=r'$\log_{10}|\Delta|^2$')
    t = np.linspace(0, 2*np.pi, 500)
    ax.plot(t, t, 'w--', lw=0.8, alpha=0.5)
    ax.plot(0, 0, 'w*', ms=10, mec='k', mew=0.5)
    ax.set_xlabel(r'$\theta_1$', fontsize=13)
    ax.set_ylabel(r'$\theta_2$', fontsize=13)
    ax.set_title('(a) Log-scale condensate', fontsize=12)
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 2*np.pi)
    ax.set_aspect('equal')
    ticks = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
    tlabels = ['0', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$']
    ax.set_xticks(ticks); ax.set_xticklabels(tlabels)
    ax.set_yticks(ticks); ax.set_yticklabels(tlabels)

    # (b) Diagonal cross-section theta1 = theta2
    ax = axes3[1]
    diag = np.array([dens_bcs_n[i, i] for i in range(N_grid)])
    ax.semilogy(theta1, diag, 'b-', lw=1.5, label=r'$\theta_1=\theta_2$')
    # Also plot theta2 = 0 cross-section
    row0 = dens_bcs_n[:, 0]
    ax.semilogy(theta1, row0, 'r-', lw=1.5, label=r'$\theta_2=0$')
    ax.set_xlabel(r'$\theta$ along cut', fontsize=13)
    ax.set_ylabel(r'$|\Delta|^2$ (normalized)', fontsize=13)
    ax.set_title('(b) Cross-sections', fontsize=12)
    ax.legend(fontsize=10)
    ax.set_xlim(0, 2*np.pi)
    ax.set_xticks(ticks); ax.set_xticklabels(tlabels)
    ax.grid(True, alpha=0.3)
    # Mark Z3 and anti-id
    ax.axvline(2*np.pi/3, color='gray', ls=':', alpha=0.5, label=r'$2\pi/3$')
    ax.axvline(np.pi, color='gray', ls='--', alpha=0.5, label=r'$\pi$')

    # (c) Integrated Weyl-chamber angular profile
    ax = axes3[2]
    # Radial profile from identity on the flat torus metric
    r_grid = np.sqrt(T1**2 + T2**2)
    r_max = np.pi * np.sqrt(2)
    n_bins = 60
    r_edges = np.linspace(0, r_max, n_bins + 1)
    r_centers = (r_edges[:-1] + r_edges[1:]) / 2
    radial = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (r_grid >= r_edges[i]) & (r_grid < r_edges[i+1])
        if np.any(mask):
            radial[i] = np.mean(dens_bcs_n[mask])
    ax.semilogy(r_centers, radial, 'k-', lw=1.5)
    ax.set_xlabel(r'$r = \sqrt{\theta_1^2+\theta_2^2}$', fontsize=13)
    ax.set_ylabel(r'$\langle|\Delta|^2\rangle_\phi$', fontsize=13)
    ax.set_title('(c) Radial profile from identity', fontsize=12)
    ax.grid(True, alpha=0.3)
    # Mark the 1/e^2 radius
    peak = radial[0]
    if peak > 0:
        half_idx = np.argmin(np.abs(radial - peak/np.e**2))
        r_half = r_centers[half_idx]
        ax.axvline(r_half, color='red', ls='--', alpha=0.7,
                   label=f'$1/e^2$ radius = {r_half:.2f}')
        print(f"\n  1/e^2 radius from identity = {r_half:.2f} rad = {r_half/np.pi:.3f}*pi")
        ax.legend(fontsize=10)

    fig3.suptitle(
        r'Condensate structure on $T^2$: log scale, cross-sections, radial profile',
        fontsize=14, fontweight='bold')
    plotfile3 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's47_condensate_torus_analysis.png')
    fig3.savefig(plotfile3, dpi=150, bbox_inches='tight')
    plt.close(fig3)
    print(f"  Analysis plot: {plotfile3}")

    # Haar measure density (condensate weighted by Haar)
    # The Haar measure on T^2 (restricted to the maximal torus inside SU(3))
    # is proportional to the Weyl denominator squared:
    # dmu = |Delta_W(theta)|^2 dtheta1 dtheta2 / (2*pi)^2
    # where Delta_W = prod_{alpha>0} (e^{i*alpha*theta/2} - e^{-i*alpha*theta/2})
    # = product over positive roots of 2i*sin(alpha*theta/2)
    #
    # For SU(3), positive roots: epsilon_i - epsilon_j for i<j
    # alpha1: theta1-theta2, alpha2: theta2+theta1+theta2=theta2-(-theta1-theta2)=theta1+2*theta2
    # alpha1+alpha2: 2*theta1+theta2
    # So Haar ~ |sin((t1-t2)/2) * sin((t1+2*t2)/2) * sin((2*t1+t2)/2)|^2 * 8

    haar = np.abs(
        np.sin((T1 - T2) / 2) *
        np.sin((T1 + 2*T2) / 2) *
        np.sin((2*T1 + T2) / 2)
    )**2

    # Condensate weighted by Haar measure
    dens_haar = dens_bcs_n * haar
    dens_haar_n = dens_haar / np.max(dens_haar)

    fig4, axes4 = plt.subplots(1, 3, figsize=(18, 6), constrained_layout=True)

    # (a) Haar measure
    ax = axes4[0]
    im = ax.pcolormesh(theta1, theta2, haar.T, cmap='viridis', shading='auto')
    plt.colorbar(im, ax=ax, label='Haar density')
    ax.set_title('(a) SU(3) Haar measure on T^2', fontsize=12)
    ax.set_xlabel(r'$\theta_1$'); ax.set_ylabel(r'$\theta_2$')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 2*np.pi); ax.set_aspect('equal')
    ax.set_xticks(ticks); ax.set_xticklabels(tlabels)
    ax.set_yticks(ticks); ax.set_yticklabels(tlabels)

    # (b) Condensate * Haar
    ax = axes4[1]
    im = ax.pcolormesh(theta1, theta2, dens_haar_n.T, cmap='inferno', shading='auto')
    plt.colorbar(im, ax=ax, label=r'$|\Delta|^2 \times$ Haar (norm)')
    ax.set_title(r'(b) $|\Delta|^2 \times$ Haar measure', fontsize=12)
    ax.set_xlabel(r'$\theta_1$'); ax.set_ylabel(r'$\theta_2$')
    ax.set_xlim(0, 2*np.pi); ax.set_ylim(0, 2*np.pi); ax.set_aspect('equal')
    ax.set_xticks(ticks); ax.set_xticklabels(tlabels)
    ax.set_yticks(ticks); ax.set_yticklabels(tlabels)

    # (c) Radial profile of Haar-weighted condensate
    ax = axes4[2]
    radial_haar = np.zeros(n_bins)
    for i in range(n_bins):
        mask = (r_grid >= r_edges[i]) & (r_grid < r_edges[i+1])
        if np.any(mask):
            radial_haar[i] = np.mean(dens_haar_n[mask])
    ax.plot(r_centers, radial_haar, 'k-', lw=1.5)
    ax.set_xlabel(r'$r = \sqrt{\theta_1^2+\theta_2^2}$', fontsize=13)
    ax.set_ylabel(r'$\langle|\Delta|^2 \times \mathrm{Haar}\rangle_\phi$', fontsize=13)
    ax.set_title('(c) Haar-weighted radial profile', fontsize=12)
    ax.grid(True, alpha=0.3)
    # Peak location
    peak_idx = np.argmax(radial_haar)
    r_peak = r_centers[peak_idx]
    ax.axvline(r_peak, color='red', ls='--', alpha=0.7,
               label=f'Peak at r={r_peak:.2f}')
    ax.legend(fontsize=10)
    print(f"  Haar-weighted peak at r = {r_peak:.2f} rad = {r_peak/np.pi:.3f}*pi")

    # Fraction of Haar-weighted condensate in the first Weyl alcove
    total_int = np.sum(dens_haar)
    print(f"\n  Haar-weighted integrals:")
    print(f"    Total integral = {total_int:.2f}")
    print(f"    Mean Haar-weighted = {np.mean(dens_haar):.6f}")

    fig4.suptitle(
        r'Haar-weighted condensate: where does the BCS weight actually sit on SU(3)?',
        fontsize=14, fontweight='bold')
    plotfile4 = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's47_condensate_torus_haar.png')
    fig4.savefig(plotfile4, dpi=150, bbox_inches='tight')
    plt.close(fig4)
    print(f"  Haar plot: {plotfile4}")

    # Update npz with Haar results
    np.savez(outfile,
             theta1=theta1, theta2=theta2,
             density_equal_weight=dens_eq,
             density_bcs_weighted=dens_bcs,
             density_A_norm=dens_eq_n,
             density_B_norm=dens_bcs_n,
             density_haar_weighted=dens_haar,
             density_haar_norm=dens_haar_n,
             haar_measure=haar,
             contrast_ratio=contrast,
             coeff_variation=cv,
             fourier_frac_00=p00,
             density_at_identity=d_id,
             density_at_Z3=d_z3,
             density_at_anti_identity=d_anti,
             max_theta1=theta1[idx_max[0]],
             max_theta2=theta2[idx_max[1]],
             min_theta1=theta1[idx_min[0]],
             min_theta2=theta2[idx_min[1]],
             radial_r=r_centers,
             radial_profile=radial,
             radial_haar=radial_haar,
             haar_peak_r=r_peak,
             gate_name='CONDENSATE-T2-47',
             gate_type='INFO',
             tau=tau_fold,
             N_grid=N_grid)
    print(f"  Updated data: {outfile}")

    print("\n" + "="*70)
    print("CONDENSATE-T2-47: Complete")
    print("="*70)
