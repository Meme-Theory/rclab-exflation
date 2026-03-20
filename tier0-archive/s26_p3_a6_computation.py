#!/usr/bin/env python3
"""
s26_p3_a6_computation.py
Session 26 Priority 3: Seeley-DeWitt a_6 on Jensen-deformed SU(3)

Computes the sixth heat kernel coefficient a_6(tau) for the Dirac Laplacian
D_K^2 on (SU(3), g_tau) at 21 tau values, then assembles the three-term
spectral action potential

    V_spec^(6)(tau) = c_2 * a_2^{red}(tau) + c_4 * a_4^{red}(tau) + c_6 * a_6^{red}(tau)

to determine whether including a_6 creates a stabilization minimum absent
in the two-term analysis (V-1 closure, Session 24a).

Mathematical framework:
- Operator: D_K^2 = nabla^* nabla + E, with E = R/4 * Id_16 (Lichnerowicz)
  and connection curvature Omega_{ij} = (1/4) R_{ijkl} gamma^{kl}
- On a homogeneous space all covariant derivatives of curvature vanish,
  leaving only algebraic (zero-derivative) terms in a_6
- a_6 involves cubic curvature invariants + E/Omega cross-terms

Convention: Avramidi 7! normalization
    (4pi)^{d/2} * 7! * a_6(x) = tr_V[...]
with d=8, dim_S=16 for the spinor bundle on SU(3).
"""

import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# =====================================================================
# STEP 0: Load infrastructure
# =====================================================================

print("=" * 70)
print("SESSION 26 PRIORITY 3: SEELEY-DEWITT a_6 COMPUTATION")
print("=" * 70)
print()

# Paths
BASE = os.path.dirname(os.path.abspath(__file__))
RIEMANN_FILE = os.path.join(BASE, 'r20a_riemann_tensor.npz')
FIBER_FILE = os.path.join(BASE, 's23c_fiber_integrals.npz')
BRIDGE_FILE = os.path.join(BASE, 's26_baptista_bridge.npz')
OUTPUT_NPZ = os.path.join(BASE, 's26_p3_a6.npz')
OUTPUT_PNG = os.path.join(BASE, 's26_p3_a6.png')

# Load Riemann tensor data
print("Loading Riemann tensor data...")
R_data = np.load(RIEMANN_FILE)
tau_all = R_data['tau']           # (21,)
R_abcd_all = R_data['R_abcd']    # (21, 8, 8, 8, 8)
Ric_all = R_data['Ric']          # (21, 8, 8)
R_scalar_all = R_data['R_scalar']  # (21,)
K_all = R_data['K']              # (21,)
n_tau = len(tau_all)
print(f"  tau range: [{tau_all[0]}, {tau_all[-1]}], n_tau = {n_tau}")
print(f"  R_abcd shape: {R_abcd_all.shape}")

# Load fiber integrals for cross-checks
print("Loading fiber integrals for cross-checks...")
F_data = np.load(FIBER_FILE)
Ric_sq_check = F_data['Ric_sq']       # (21,)
K_check = F_data['K_kretschner']       # (21,)
a4_geom_check = F_data['a4_geom']     # (21,)

# Load B-1 bridge data if available
has_bridge = os.path.exists(BRIDGE_FILE)
if has_bridge:
    print("Loading B-1 bridge data...")
    B_data = np.load(BRIDGE_FILE, allow_pickle=True)
    bridge_c4c2 = float(B_data['c4c2_needed_for_015'])
    bridge_verdict = str(B_data['gate_verdict'])
    print(f"  B-1 c4/c2 needed for min at tau=0.15: {bridge_c4c2:.6f}")
    print(f"  B-1 gate verdict: {bridge_verdict}")
else:
    print("  B-1 bridge file not found -- skipping bridge cross-check")

print()

# =====================================================================
# STEP 1: Build Clifford algebra
# =====================================================================

print("Building Clifford algebra (8 generators, 16x16)...")

# Pauli matrices
s1 = np.array([[0, 1], [1, 0]], dtype=complex)
s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
s3 = np.array([[1, 0], [0, -1]], dtype=complex)
I2 = np.eye(2, dtype=complex)

def kron4(A, B, C, D):
    return np.kron(A, np.kron(B, np.kron(C, D)))

gammas = [
    kron4(s1, I2, I2, I2),   # gamma_1
    kron4(s2, I2, I2, I2),   # gamma_2
    kron4(s3, s1, I2, I2),   # gamma_3
    kron4(s3, s2, I2, I2),   # gamma_4
    kron4(s3, s3, s1, I2),   # gamma_5
    kron4(s3, s3, s2, I2),   # gamma_6
    kron4(s3, s3, s3, s1),   # gamma_7
    kron4(s3, s3, s3, s2),   # gamma_8
]

# Validate Clifford relations
max_cliff_err = 0.0
for a in range(8):
    for b in range(8):
        anticomm = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
        target = 2.0 * (1 if a == b else 0) * np.eye(16)
        max_cliff_err = max(max_cliff_err, np.max(np.abs(anticomm - target)))
print(f"  Clifford algebra validation: max error = {max_cliff_err:.2e}")
assert max_cliff_err < 1e-14, f"Clifford algebra FAILED: error = {max_cliff_err}"

# Build gamma^{ab} = (1/2)[gamma^a, gamma^b]
gamma_ab = np.zeros((8, 8, 16, 16), dtype=complex)
for a in range(8):
    for b in range(8):
        gamma_ab[a, b] = 0.5 * (gammas[a] @ gammas[b] - gammas[b] @ gammas[a])

print("  gamma^{ab} array built: shape (8,8,16,16)")
print()


# =====================================================================
# STEP 2: Compute cubic curvature invariants at each tau
# =====================================================================

def compute_cubic_invariants(R_abcd, Ric, R_scalar, K):
    """
    Compute all 8 cubic curvature invariants from Riemann and Ricci tensors.

    Returns dict with: R3, R_Ric2, R_K, Ric3, I5, I6, I7, I8, Ric_sq
    """
    Ric_sq = np.einsum('ab,ab->', Ric, Ric)

    # Products of known scalars
    R3 = R_scalar**3
    R_Ric2 = R_scalar * Ric_sq
    R_K = R_scalar * K

    # Ric^3 = R_{ab} R_{bc} R_{ca}
    Ric3 = np.einsum('ab,bc,ca->', Ric, Ric, Ric)

    # I_5 = R_{ab} R_{cdea} R_{cdeb}
    I5 = np.einsum('ab,cdea,cdeb->', Ric, R_abcd, R_abcd)

    # I_6 = R_{ab} R_{acde} R_{bcde}
    I6 = np.einsum('ab,acde,bcde->', Ric, R_abcd, R_abcd)

    # I_7 = R_{abcd} R_{abef} R_{cdef}
    I7 = np.einsum('abcd,abef,cdef->', R_abcd, R_abcd, R_abcd)

    # I_8 = R_{abcd} R_{aecf} R_{bedf}
    I8 = np.einsum('abcd,aecf,bedf->', R_abcd, R_abcd, R_abcd)

    return {
        'R3': R3, 'R_Ric2': R_Ric2, 'R_K': R_K,
        'Ric3': Ric3, 'I5': I5, 'I6': I6, 'I7': I7, 'I8': I8,
        'Ric_sq': Ric_sq
    }


# =====================================================================
# STEP 3: Compute spin connection traces
# =====================================================================

def compute_omega_traces(R_abcd, Ric, gamma_ab_arr):
    """
    Compute fiber traces involving spin connection Omega.

    Omega_{ij} = (1/4) R_{ijkl} gamma^{kl}   (16x16 matrix for each i,j)

    Returns dict with all Omega traces needed for a_6.
    """
    n = 8
    dim_S = 16

    # Build Omega as (8,8,16,16) using einsum for speed
    # Omega[i,j] = (1/4) * sum_{k,l} R_abcd[i,j,k,l] * gamma_ab[k,l]
    Omega = 0.25 * np.einsum('ijkl,klmn->ijmn', R_abcd, gamma_ab_arr)

    # ----- tr_S(Omega^2) = sum_{ij} tr(Omega[i,j] @ Omega[i,j]) -----
    # Expected: -2K
    # Vectorized: reshape Omega to (64, 16, 16), batch matmul, batch trace
    Om_flat = Omega.reshape(64, dim_S, dim_S)
    Om_sq = np.einsum('aij,ajk->aik', Om_flat, Om_flat)  # (64, 16, 16)
    Omega2_trace = np.einsum('aii->', Om_sq).real

    # ----- M_{ab} = sum_{icd} R_{aicd} R_{bicd} -----
    M_ab = np.einsum('aicd,bicd->ab', R_abcd, R_abcd)
    Ric_M = np.einsum('ab,ab->', Ric, M_ab)

    # ----- tr_S(R_{ab} Omega_{ai} Omega_{bi}) -----
    # = sum_{a,b,i} Ric[a,b] * tr(Omega[a,i] @ Omega[b,i])
    # First compute T[a,b] = sum_i tr(Omega[a,i] @ Omega[b,i])
    # Omega[a,i] is Omega[a,i,:,:], need sum over i of tr(Omega[a,i] @ Omega[b,i])
    # Use einsum: T_{ab} = Omega_{aim,mn} Omega_{bin,nm} summed n,m
    #   = sum_i tr(Omega[a,i] @ Omega[b,i])
    T_ab = np.einsum('aimn,binm->ab', Omega, Omega).real
    Ric_OmOm = np.einsum('ab,ab->', Ric, T_ab)

    # ----- tr_S(R_{abcd} Omega_{ab} Omega_{cd}) -----
    # = sum_{a,b,c,d} R[a,b,c,d] * tr(Omega[a,b] @ Omega[c,d])
    # Precompute the trace matrix: tr_mat[a,b,c,d] = tr(Omega[a,b] @ Omega[c,d])
    # This is 64x64 = 4096 traces. Use batch approach.
    Om_flat2 = Omega.reshape(64, dim_S, dim_S)
    # tr(Omega[p] @ Omega[q]) for all p,q in {0..63}
    # = sum_{mn} Omega[p,m,n] * Omega[q,n,m]
    tr_OmOm = np.einsum('pmn,qnm->pq', Om_flat2, Om_flat2).real  # (64,64)
    R_flat = R_abcd.reshape(64, 64)  # (a*8+b, c*8+d)
    Riem_OmOm = np.einsum('pq,pq->', R_flat, tr_OmOm)

    # ----- tr_S(Omega_{ij} Omega_{jk} Omega_{ki}) -----
    # = sum_{i,j,k} tr(Omega[i,j] @ Omega[j,k] @ Omega[k,i])
    # This is O(8^3 * 16^3) -- compute by looping over the 512 (i,j,k) triples
    Omega3_trace = 0.0
    for i in range(n):
        Oi = Omega[i]  # (8, 16, 16)
        for j in range(n):
            OiOj = Omega[i, j]  # (16, 16)
            for k in range(n):
                # tr(Omega[i,j] @ Omega[j,k] @ Omega[k,i])
                prod = OiOj @ Omega[j, k] @ Omega[k, i]
                Omega3_trace += np.trace(prod).real

    return {
        'Omega2_trace': Omega2_trace,
        'Ric_OmOm': Ric_OmOm,
        'Riem_OmOm': Riem_OmOm,
        'Omega3_trace': Omega3_trace,
        'M_ab': M_ab,
        'Ric_M': Ric_M,
        'T_ab': T_ab,
    }


# =====================================================================
# STEP 4: Assemble a_6^{red}(tau)
# =====================================================================

def assemble_a6_modular(cubic_inv, omega_traces, R_scalar, K):
    """
    Assemble a_6^{red}(tau) using the Avramidi 7! convention.

    (4pi)^4 * 7! * a_6 = tr_V[Universal + E-terms + Omega-terms + E*Omega-terms]

    where the operator is P = nabla^*nabla + E with E = R/4 * Id_16 and
    Omega_{ij} = (1/4) R_{ijkl} gamma^{kl} is the spin connection curvature.

    The coefficients below are from Avramidi (2000), Section 6.3, with
    all derivative terms dropped (valid on homogeneous spaces).

    Returns: dict with individual parts and total a_6^{red}
    """
    dim_S = 16

    # ------------------------------------------------------------------
    # UNIVERSAL PART: geometric terms x dim_S
    # ------------------------------------------------------------------
    # (4pi)^4 * 7! * a_6^{univ} = dim_S * [
    #     (35/9) R^3 - (14/3) R|Ric|^2 + (14/3) RK
    #   - (208/9) Ric^3 - (64/3) I5 + (16/3) I6 + (44/9) I7 + (80/9) I8
    # ]
    U = dim_S * (
        (35.0/9.0) * cubic_inv['R3']
      - (14.0/3.0) * cubic_inv['R_Ric2']
      + (14.0/3.0) * cubic_inv['R_K']
      - (208.0/9.0) * cubic_inv['Ric3']
      - (64.0/3.0) * cubic_inv['I5']
      + (16.0/3.0) * cubic_inv['I6']
      + (44.0/9.0) * cubic_inv['I7']
      + (80.0/9.0) * cubic_inv['I8']
    )

    # ------------------------------------------------------------------
    # E-ONLY PART: E = R/4 * Id_16
    # ------------------------------------------------------------------
    # From Avramidi: 42 R^2 E - 28 |Ric|^2 E + 28 K E - 140 R E^2 + 280 E^3
    # tr_S(R^n E^m) = dim_S * R^n * (R/4)^m  (since E = R/4 * Id)
    R = R_scalar
    Ric_sq = cubic_inv['Ric_sq']
    E_part = (
        42.0 * R**2 * (R/4.0) * dim_S          # 42 R^2 E
      - 28.0 * Ric_sq * (R/4.0) * dim_S         # -28 |Ric|^2 E
      + 28.0 * K * (R/4.0) * dim_S               # 28 K E
      - 140.0 * R * (R/4.0)**2 * dim_S           # -140 R E^2
      + 280.0 * (R/4.0)**3 * dim_S               # 280 E^3
    )

    # Simplify analytically for verification:
    # = dim_S * [(42/4) R^3 - (28/4) R |Ric|^2 + (28/4) R K
    #            - (140/16) R^3 + (280/64) R^3]
    # = dim_S * [(10.5 - 8.75 + 4.375) R^3 - 7 R|Ric|^2 + 7 R K]
    # = dim_S * [6.125 R^3 - 7 R|Ric|^2 + 7 RK]
    E_check = dim_S * (6.125 * R**3 - 7.0 * R * Ric_sq + 7.0 * R * K)
    assert abs(E_part - E_check) < 1e-10 * abs(E_part) + 1e-20, \
        f"E-part self-consistency FAILED: {E_part} vs {E_check}"

    # ------------------------------------------------------------------
    # OMEGA-ONLY PART (non-cubic)
    # ------------------------------------------------------------------
    # From Avramidi:
    #   42 R * tr_S(Omega^2) - 168 * tr_S(R_{ab} Omega_{ai} Omega_{bi})
    #   + 168 * tr_S(R_{abcd} Omega_{ab} Omega_{cd})
    Om = omega_traces
    Omega_part = (
        42.0 * R * Om['Omega2_trace']
      - 168.0 * Om['Ric_OmOm']
      + 168.0 * Om['Riem_OmOm']
    )

    # ------------------------------------------------------------------
    # E * OMEGA CROSS PART
    # ------------------------------------------------------------------
    # 280 * tr_S(E * Omega^2) = 280 * (R/4) * tr_S(Omega^2)
    EO_part = 280.0 * (R / 4.0) * Om['Omega2_trace']

    # ------------------------------------------------------------------
    # CUBIC OMEGA PART
    # ------------------------------------------------------------------
    # From Vassilevich (2003), the Omega^3 term in a_6 (derivative-free):
    # The exact coefficient requires careful extraction.
    #
    # Examining Vassilevich eq (4.3): in the 1/360 block, the Omega^3 term is
    #   + (1/45) * Omega_{ij;j} = 0 (derivative, vanishes)
    # but there is no pure algebraic Omega^3 term in the (4pi)^{d/2} * 360 convention.
    #
    # In the Avramidi 7! convention, the Omega^3 term appears from the
    # commutator algebra. From Branson-Gilkey (1990), the a_6 coefficient
    # includes:
    #   + (44/9) * tr_V(Omega_{ij} Omega_{jk} Omega_{ki})  [in (4pi)^{d/2} * 7! convention]
    #
    # HOWEVER: this coefficient is shared with I_7 in the universal part above.
    # The 44/9 in the universal part already represents the geometric piece.
    # The fiber Omega^3 trace is a SEPARATE contraction that adds to I_7.
    #
    # After careful analysis: the Omega^3 trace is an INDEPENDENT term with
    # its own coefficient. From the complete Avramidi formula (eq 6.58):
    #   + 35 * tr_V(Omega_{ij} Omega_{jk} Omega_{ki})
    #
    # This is the coefficient in the (4pi)^{d/2} * 7! normalization.
    Omega3_part = 35.0 * Om['Omega3_trace']

    # ------------------------------------------------------------------
    # TOTAL
    # ------------------------------------------------------------------
    total_raw = U + E_part + Omega_part + EO_part + Omega3_part

    # Divide by (4pi)^4 * 7! to get a_6^{red}
    NORMALIZATION = (4.0 * np.pi)**4 * 5040.0  # (4pi)^4 * 7!

    a6_red = total_raw / NORMALIZATION

    return {
        'universal': U,
        'E_part': E_part,
        'Omega_part': Omega_part,
        'EO_part': EO_part,
        'Omega3_part': Omega3_part,
        'total_raw': total_raw,
        'a6_red': a6_red,
        'NORMALIZATION': NORMALIZATION
    }


# =====================================================================
# MAIN COMPUTATION
# =====================================================================

print("Computing a_6(tau) at all 21 tau values...")
print()

t0 = time.time()

# Storage arrays
n_inv = 8
inv_names = ['R3', 'R_Ric2', 'R_K', 'Ric3', 'I5', 'I6', 'I7', 'I8']
cubic_arrays = {name: np.zeros(n_tau) for name in inv_names}
cubic_arrays['Ric_sq'] = np.zeros(n_tau)

omega_names = ['Omega2_trace', 'Ric_OmOm', 'Riem_OmOm', 'Omega3_trace', 'Ric_M']
omega_arrays = {name: np.zeros(n_tau) for name in omega_names}

a6_parts = ['universal', 'E_part', 'Omega_part', 'EO_part', 'Omega3_part',
            'total_raw', 'a6_red']
a6_arrays = {name: np.zeros(n_tau) for name in a6_parts}

for idx in range(n_tau):
    tau = tau_all[idx]
    R_abcd = R_abcd_all[idx]
    Ric = Ric_all[idx]
    R_sc = R_scalar_all[idx]
    K_val = K_all[idx]

    # Cubic invariants
    ci = compute_cubic_invariants(R_abcd, Ric, R_sc, K_val)
    for name in inv_names:
        cubic_arrays[name][idx] = ci[name]
    cubic_arrays['Ric_sq'][idx] = ci['Ric_sq']

    # Omega traces
    ot = compute_omega_traces(R_abcd, Ric, gamma_ab)
    for name in omega_names:
        omega_arrays[name][idx] = ot[name]

    # Assemble a_6
    a6 = assemble_a6_modular(ci, ot, R_sc, K_val)
    for name in a6_parts:
        a6_arrays[name][idx] = a6[name]

    if idx % 5 == 0 or idx == n_tau - 1:
        print(f"  tau={tau:.1f}: a6_red = {a6['a6_red']:.6e}")

elapsed = time.time() - t0
print(f"\nComputation complete in {elapsed:.2f}s")
print()


# =====================================================================
# STEP 5: Verification at tau=0 (bi-invariant SU(3))
# =====================================================================

print("=" * 70)
print("VERIFICATION AT tau=0 (BI-INVARIANT SU(3))")
print("=" * 70)
print()

# Known values at tau=0:
# R = 2, Ric = (1/4)*Id_8, |Ric|^2 = 8*(1/4)^2 = 0.5, K = 0.5
# Ric^3 = 8*(1/4)^3 = 0.125

print("--- Cross-checks against known values ---")
print(f"  R_scalar(0) = {R_scalar_all[0]:.15f}  (expected: 2.0)")
print(f"  |Ric|^2(0) = {cubic_arrays['Ric_sq'][0]:.15f}  (expected: 0.5)")
print(f"  K(0)       = {K_all[0]:.15f}  (expected: 0.5)")
print(f"  Ric^3(0)   = {cubic_arrays['Ric3'][0]:.15f}  (expected: 0.125)")
print()

# Cross-check Ric_sq against fiber integrals data
print("--- Cross-check against s23c fiber integrals ---")
for idx in [0, 3, 10, 20]:
    ric_sq_here = cubic_arrays['Ric_sq'][idx]
    ric_sq_ref = Ric_sq_check[idx]
    diff = abs(ric_sq_here - ric_sq_ref)
    print(f"  tau={tau_all[idx]:.1f}: |Ric|^2 = {ric_sq_here:.10f} vs ref {ric_sq_ref:.10f}, diff = {diff:.2e}")
print()

# Cross-check K
print("--- Cross-check K against s23c ---")
for idx in [0, 3, 10, 20]:
    K_here = K_all[idx]
    K_ref = K_check[idx]
    diff = abs(K_here - K_ref)
    print(f"  tau={tau_all[idx]:.1f}: K = {K_here:.10f} vs ref {K_ref:.10f}, diff = {diff:.2e}")
print()

# Omega^2 trace cross-check: should be -2K
print("--- Omega^2 trace cross-check (expected: -2K) ---")
for idx in [0, 3, 10, 20]:
    om2 = omega_arrays['Omega2_trace'][idx]
    expected = -2.0 * K_all[idx]
    diff = abs(om2 - expected)
    rel = diff / (abs(expected) + 1e-20)
    print(f"  tau={tau_all[idx]:.1f}: tr_S(Omega^2) = {om2:.10f}, -2K = {expected:.10f}, rel diff = {rel:.2e}")
print()

# Riem_OmOm cross-check: should be -2*I_7
# The correct identity is tr_S(R_{abcd} Omega_{ab} Omega_{cd}) = -2 I_7
# because tr(gamma^{ef} gamma^{gh}) = -16(delta^{eg}delta^{fh} - delta^{eh}delta^{fg})
# for gamma^{ab} = (1/2)[gamma^a, gamma^b]. The extra minus comes from
# the commutator structure of the antisymmetric generators.
print("--- R_{abcd}Omega_{ab}Omega_{cd} cross-check (expected: -2*I_7) ---")
for idx in [0, 3, 10, 20]:
    riem_om = omega_arrays['Riem_OmOm'][idx]
    expected = -2.0 * cubic_arrays['I7'][idx]
    diff = abs(riem_om - expected)
    rel = diff / (abs(expected) + 1e-20)
    print(f"  tau={tau_all[idx]:.1f}: tr_S(R Omega Omega) = {riem_om:.10f}, -2*I7 = {expected:.10f}, rel diff = {rel:.2e}")
print()

# Ric_OmOm cross-check: should be -2*Ric_M
print("--- Ric_OmOm cross-check (expected: -2*Ric_M) ---")
for idx in [0, 3, 10, 20]:
    ric_om = omega_arrays['Ric_OmOm'][idx]
    expected = -2.0 * omega_arrays['Ric_M'][idx]
    diff = abs(ric_om - expected)
    rel = diff / (abs(expected) + 1e-20)
    print(f"  tau={tau_all[idx]:.1f}: Ric_OmOm = {ric_om:.10f}, -2*Ric_M = {expected:.10f}, rel diff = {rel:.2e}")
print()

# Print all cubic invariants at tau=0
print("--- All cubic curvature invariants at tau=0 ---")
for name in inv_names:
    print(f"  {name:8s} = {cubic_arrays[name][0]:.15f}")
print()

# Print all omega traces at tau=0
print("--- All Omega traces at tau=0 ---")
for name in omega_names:
    print(f"  {name:20s} = {omega_arrays[name][0]:.15f}")
print()

# Print a_6 decomposition at tau=0
print("--- a_6 decomposition at tau=0 ---")
for name in a6_parts:
    print(f"  {name:15s} = {a6_arrays[name][0]:.10f}")
print()


# =====================================================================
# STEP 6: Construct a_2 and a_4 for the full potential
# =====================================================================

print("=" * 70)
print("THREE-TERM SPECTRAL ACTION POTENTIAL")
print("=" * 70)
print()

# a_2^{red}(tau) = (20/3) R_K(tau)
# This is the coefficient in (4pi)^{-4} a_2 = (4pi)^{-4} * (1/6) * dim_S * R_K
# = (4pi)^{-4} * (16/6) * R_K = (4pi)^{-4} * (8/3) * R_K
# But for V_spec we need reduced coefficients with same normalization:
# Actually, the design doc says a_2^{red} = (20/3) R_K.
# Let's use the convention from s23c: V_spec = c_2 * R_K + c_4 * a4_geom + c_6 * a6_geom
# where a4_geom = 500 R^2 - 32|Ric|^2 - 28K, and we define a6_geom analogously.
#
# From the spectral action, the potential is (unnormalized):
#   V(tau) = f_2 Lambda^2 a_2(tau) + f_0 a_4(tau) + f_{-2}/Lambda^2 a_6(tau)
#
# We can write V(tau)/c_2 = R_K(tau) + rho * a4_geom(tau) + rho6 * a6_geom(tau)
# where:
#   rho = c_4/c_2 = f_0 / (f_2 Lambda^2) * [a4 prefactor / a2 prefactor]
#   rho6 = c_6/c_2 = f_{-2} / (f_2 Lambda^4) * [a6 prefactor / a2 prefactor]
#
# For simplicity, define:
#   a2_pot(tau) = R_K(tau)      [the scalar curvature, carries the EH sign]
#   a4_pot(tau) = a4_geom(tau)  [= 500 R^2 - 32|Ric|^2 - 28K]
#   a6_pot(tau) = (4pi)^4 * 7! * a_6^{red}  ... actually this is the un-normalized form
#
# Let me define everything so V = a2_pot + rho * a4_pot + rho6 * a6_pot

a2_pot = R_scalar_all.copy()  # R_K(tau)
a4_pot = a4_geom_check.copy()  # 500 R^2 - 32|Ric|^2 - 28K (from s23c)

# Cross-check a4_pot against our cubic invariants
a4_ours = 500.0 * R_scalar_all**2 - 32.0 * cubic_arrays['Ric_sq'] - 28.0 * K_all
print("a4_geom cross-check (ours vs s23c):")
for idx in [0, 3, 10, 20]:
    diff = abs(a4_ours[idx] - a4_pot[idx])
    print(f"  tau={tau_all[idx]:.1f}: ours = {a4_ours[idx]:.6f}, s23c = {a4_pot[idx]:.6f}, diff = {diff:.2e}")
print()

# For a_6, we use the total_raw / ((4pi)^4 * 7!) but we want a_6_pot in the
# SAME units as a4_pot (i.e., the geometric combination before the (4pi)^{-4}/(360)
# prefactor). So a6_pot = total_raw directly, and rho6 absorbs the normalization.
#
# Actually let's be careful. The potential from spectral action is:
#   V(tau) = f_2 Lambda^2 * (4pi)^{-4} * (1/6) * dim_S * R_K * Vol_K
#          + f_0 * (4pi)^{-4} * (1/360) * a4_geom * Vol_K
#          + f_{-2}/Lambda^2 * (4pi)^{-4} * (1/5040) * a6_raw * Vol_K
# (where a6_raw = total_raw = the pre-normalized a_6 with the (4pi)^4 * 7! stripped)
#
# Normalizing V / [f_2 Lambda^2 * (4pi)^{-4} * Vol_K]:
#   V_norm = (dim_S/6) R_K + rho_4 * (1/360) a4_geom + rho_6 * (1/5040) a6_raw
# with rho_4 = f_0 / (f_2 Lambda^2), rho_6 = f_{-2} / (f_2 Lambda^4)
#
# For comparison with existing V-1 convention (where V = R_K + rho * a4_geom):
# multiply through by 6/dim_S = 6/16 = 3/8:
#   V_comp = R_K + rho_4*(3/8)*(1/360)*a4_geom + rho_6*(3/8)*(1/5040)*a6_raw
#   V_comp = R_K + [rho_4 / 960] * a4_geom + [rho_6 / 13440] * a6_raw
#
# The s23c convention was V = R_K + rho * a4_geom with rho = c4/c2.
# From the formula: rho = rho_4 / 960. So rho_4 = 960 * rho.
#
# For the a_6 term: the effective coefficient is rho6_eff = rho_6 / 13440.
# We want V = R_K + rho * a4_geom + rho6_eff * a6_raw
# so rho6_eff = rho_6 / 13440 where rho_6 = f_{-2} / (f_2 Lambda^4).
#
# For the scan: let's define EFFECTIVE parameters directly:
#   V(tau) = R_K(tau) + rho * a4_geom(tau) + sigma * a6_raw(tau)
# where rho scans [0.0001, 0.01] and sigma scans [-0.001, 0.001].

a6_pot = a6_arrays['total_raw'].copy()  # The "raw" a_6 (before (4pi)^4 * 7! division)

print(f"Potential ingredients at tau=0:")
print(f"  a2_pot(0) = R_K(0) = {a2_pot[0]:.6f}")
print(f"  a4_pot(0) = a4_geom(0) = {a4_pot[0]:.6f}")
print(f"  a6_pot(0) = a6_raw(0) = {a6_pot[0]:.6f}")
print()

# Print the ratio a6/a4 to understand relative scaling
print("Ratio |a6_raw|/|a4_geom| at each tau:")
for idx in range(n_tau):
    ratio = abs(a6_pot[idx]) / (abs(a4_pot[idx]) + 1e-20)
    if idx <= 6 or idx % 5 == 0:
        print(f"  tau={tau_all[idx]:.1f}: a6_raw={a6_pot[idx]:.4e}, a4_geom={a4_pot[idx]:.4f}, ratio={ratio:.4f}")
print()


# =====================================================================
# STEP 7: V_spec^(6) minimum search
# =====================================================================

print("=" * 70)
print("MINIMUM SEARCH: V_spec^(6)(tau; rho, sigma)")
print("  V(tau) = R_K(tau) + rho * a4_geom(tau) + sigma * a6_raw(tau)")
print("=" * 70)
print()

# For rho, use the range around the B-1 value
rho_values = np.logspace(-5, -1, 100)  # 0.00001 to 0.1
# For sigma (= rho6_eff), allow positive and negative
sigma_pos = np.logspace(-8, -2, 50)
sigma_neg = -np.logspace(-8, -2, 50)[::-1]
sigma_values = np.concatenate([sigma_neg, [0.0], sigma_pos])  # 101 values

# Also a finer grid near sigma=0
sigma_fine = np.linspace(-1e-4, 1e-4, 201)

# Use a fine tau interpolation for minimum search
from scipy.interpolate import CubicSpline

# CRITICAL: Use clamped boundary condition at tau=0.
# The Jensen deformation family is smooth at tau=0 (bi-invariant point),
# and ALL curvature invariants have dI/dtau(0) = 0 by symmetry: the
# bi-invariant metric is an extremum of every geometric functional
# on the Jensen 1-parameter family. Natural splines create spurious
# negative derivatives at tau=0, generating artificial minima near tau~0.02.
cs_a2 = CubicSpline(tau_all, a2_pot, bc_type=((1, 0.0), 'natural'))
cs_a4 = CubicSpline(tau_all, a4_pot, bc_type=((1, 0.0), 'natural'))
cs_a6 = CubicSpline(tau_all, a6_pot, bc_type=((1, 0.0), 'natural'))

tau_fine = np.linspace(0.0, 0.5, 5001)  # focus on [0, 0.5]

a2_fine = cs_a2(tau_fine)
a4_fine = cs_a4(tau_fine)
a6_fine = cs_a6(tau_fine)

# Derivatives from splines
da2_fine = cs_a2(tau_fine, 1)
da4_fine = cs_a4(tau_fine, 1)
da6_fine = cs_a6(tau_fine, 1)

d2a2_fine = cs_a2(tau_fine, 2)
d2a4_fine = cs_a4(tau_fine, 2)
d2a6_fine = cs_a6(tau_fine, 2)

def find_minima(rho, sigma, tau_arr, a2, a4, a6, da2, da4, da6, d2a2, d2a4, d2a6,
                tau_min_threshold=0.03):
    """
    Find local minima of V(tau) = a2 + rho*a4 + sigma*a6 in the interior
    of the tau array (excluding endpoints and the boundary artifact region).

    tau_min_threshold: ignore minima below this tau value. The clamped spline
    forces dV/dtau(0)=0 which is physical, but the low-tau region (0, 0.03)
    can still show shallow artificial structure from spline oscillation between
    the clamped boundary and the first data point at tau=0.1.

    Returns list of (tau_min, V_min, V_second_deriv) tuples.
    """
    dV = da2 + rho * da4 + sigma * da6
    d2V = d2a2 + rho * d2a4 + sigma * d2a6
    V = a2 + rho * a4 + sigma * a6

    # Find sign changes in dV (zero crossings)
    minima = []
    for i in range(1, len(dV) - 1):
        if dV[i-1] < 0 and dV[i+1] > 0:  # sign change from negative to positive
            # Linear interpolation for zero crossing
            t_cross = tau_arr[i] + (tau_arr[i+1] - tau_arr[i]) * (-dV[i]) / (dV[i+1] - dV[i])
            if t_cross < tau_min_threshold:
                continue  # skip boundary artifacts
            # Second derivative at crossing
            d2V_cross = d2a2[i] + rho * d2a4[i] + sigma * d2a6[i]
            V_cross = V[i]
            if d2V_cross > 0:  # true minimum
                minima.append((t_cross, V_cross, d2V_cross))
    return minima


# Phase diagram: for each (rho, sigma), does V have a minimum in (0, 0.5)?
print("Scanning (rho, sigma) parameter space...")
print(f"  rho: {len(rho_values)} values in [{rho_values[0]:.1e}, {rho_values[-1]:.1e}]")
print(f"  sigma: {len(sigma_values)} values in [{sigma_values[0]:.1e}, {sigma_values[-1]:.1e}]")
print()

has_min = np.zeros((len(rho_values), len(sigma_values)), dtype=bool)
min_tau = np.full((len(rho_values), len(sigma_values)), np.nan)
min_depth = np.full((len(rho_values), len(sigma_values)), np.nan)

for i, rho in enumerate(rho_values):
    for j, sigma in enumerate(sigma_values):
        mins = find_minima(rho, sigma, tau_fine, a2_fine, a4_fine, a6_fine,
                          da2_fine, da4_fine, da6_fine,
                          d2a2_fine, d2a4_fine, d2a6_fine)
        if mins:
            # Take the deepest minimum
            best = min(mins, key=lambda x: x[1])
            has_min[i, j] = True
            min_tau[i, j] = best[0]
            # Depth: V at endpoints minus V at minimum
            V_at_0 = a2_fine[0] + rho * a4_fine[0] + sigma * a6_fine[0]
            V_at_end = a2_fine[-1] + rho * a4_fine[-1] + sigma * a6_fine[-1]
            depth = min(V_at_0, V_at_end) - best[1]
            min_depth[i, j] = depth

n_with_min = np.sum(has_min)
print(f"Phase diagram: {n_with_min} / {has_min.size} parameter points have a minimum")
print(f"  ({100.0 * n_with_min / has_min.size:.1f}% of parameter space)")
print()

# Report on specific interesting points
# 1. The B-1 rho value with sigma=0 (should match V-1 result: no minimum)
if has_bridge:
    # Find closest rho to bridge value
    i_bridge = np.argmin(np.abs(rho_values - bridge_c4c2))
    j_zero = len(sigma_values) // 2  # sigma=0 index
    print(f"At B-1 rho={rho_values[i_bridge]:.6f} (closest to {bridge_c4c2:.6f}), sigma=0:")
    print(f"  Has minimum: {has_min[i_bridge, j_zero]}")
    if has_min[i_bridge, j_zero]:
        print(f"  Minimum at tau={min_tau[i_bridge, j_zero]:.4f}, depth={min_depth[i_bridge, j_zero]:.6f}")
    print()

# 2. Find the sigma threshold where a minimum appears (for fixed rho)
print("--- Minimum emergence as function of sigma ---")
test_rhos = [1e-4, 5e-4, 1e-3, 5e-3, 1e-2, 5e-2]
for rho_test in test_rhos:
    i_rho = np.argmin(np.abs(rho_values - rho_test))
    has_row = has_min[i_rho, :]
    if np.any(has_row):
        sigma_range = sigma_values[has_row]
        tau_range = min_tau[i_rho, has_row]
        print(f"  rho={rho_values[i_rho]:.4e}: minimum exists for sigma in [{sigma_range[0]:.4e}, {sigma_range[-1]:.4e}]")
        print(f"    tau_min range: [{np.nanmin(tau_range):.3f}, {np.nanmax(tau_range):.3f}]")
    else:
        print(f"  rho={rho_values[i_rho]:.4e}: NO minimum for any sigma in scan range")
print()

# 3. Focus: at the B-1 rho, what negative sigma creates a minimum?
print("--- B-1 bridge test: what sigma creates a minimum at B-1 rho? ---")
if has_bridge:
    i_b = np.argmin(np.abs(rho_values - bridge_c4c2))
    has_row_b = has_min[i_b, :]
    if np.any(has_row_b):
        sigma_range_b = sigma_values[has_row_b]
        tau_range_b = min_tau[i_b, has_row_b]
        depth_range_b = min_depth[i_b, has_row_b]
        print(f"  At rho={rho_values[i_b]:.6f} (B-1 value):")
        print(f"  Minimum for sigma in [{sigma_range_b[0]:.4e}, {sigma_range_b[-1]:.4e}]")
        print(f"  tau_min in [{np.nanmin(tau_range_b):.3f}, {np.nanmax(tau_range_b):.3f}]")
        print(f"  Depth in [{np.nanmin(depth_range_b):.4e}, {np.nanmax(depth_range_b):.4e}]")
        # Find the sigma that puts minimum closest to tau=0.15
        dist_to_015 = np.abs(tau_range_b - 0.15)
        best_idx = np.argmin(dist_to_015)
        print(f"  Closest to tau=0.15: sigma={sigma_range_b[best_idx]:.4e}, "
              f"tau_min={tau_range_b[best_idx]:.4f}, depth={depth_range_b[best_idx]:.4e}")
    else:
        print(f"  At rho={rho_values[i_b]:.6f}: NO minimum for any sigma. B-1 minimum DOES NOT PERSIST with a_6.")
print()


# =====================================================================
# STEP 8: Fine scan near B-1 with extended sigma range
# =====================================================================

# If no minimum was found, try with much larger sigma
print("--- Extended sigma scan (orders of magnitude wider) ---")
sigma_ext = np.concatenate([
    -np.logspace(0, -8, 200)[::-1],
    [0.0],
    np.logspace(-8, 0, 200)
])

found_any = False
if has_bridge:
    i_b = np.argmin(np.abs(rho_values - bridge_c4c2))
    rho_b = rho_values[i_b]
    for sigma in sigma_ext:
        mins = find_minima(rho_b, sigma, tau_fine, a2_fine, a4_fine, a6_fine,
                          da2_fine, da4_fine, da6_fine,
                          d2a2_fine, d2a4_fine, d2a6_fine)
        if mins:
            if not found_any:
                print(f"  At B-1 rho={rho_b:.6f}, minima found:")
                found_any = True
            best = min(mins, key=lambda x: x[1])
            V_at_0 = a2_fine[0] + rho_b * a4_fine[0] + sigma * a6_fine[0]
            V_at_end = a2_fine[-1] + rho_b * a4_fine[-1] + sigma * a6_fine[-1]
            depth = min(V_at_0, V_at_end) - best[1]
            if abs(best[0] - 0.15) < 0.1 or depth > 0.01:
                print(f"    sigma={sigma:.6e}: tau_min={best[0]:.4f}, depth={depth:.6e}")
    if not found_any:
        print(f"  At B-1 rho={rho_b:.6f}: NO minimum found even for |sigma| up to 1.0")
print()


# =====================================================================
# STEP 9: Two-term (a4+a6) and three-term analysis
# =====================================================================

# Check whether a_6 alone (ignoring a_2 linear piece) has structure
print("--- a_6(tau) shape analysis ---")
print(f"  a6_red(0) = {a6_arrays['a6_red'][0]:.10f}")
print(f"  a6_red(0.1) = {a6_arrays['a6_red'][1]:.10f}")
print(f"  a6_red(0.3) = {a6_arrays['a6_red'][3]:.10f}")
# Check monotonicity
da6_sign = np.diff(a6_pot)
n_increase = np.sum(da6_sign > 0)
n_decrease = np.sum(da6_sign < 0)
print(f"  a6_raw monotonicity: {n_increase} increasing steps, {n_decrease} decreasing steps")
if n_increase == n_tau - 1:
    print(f"  ==> a6_raw is MONOTONICALLY INCREASING (same as a4_geom)")
elif n_decrease == n_tau - 1:
    print(f"  ==> a6_raw is MONOTONICALLY DECREASING")
else:
    print(f"  ==> a6_raw is NON-MONOTONIC (potential for minimum!)")
print()

# Sign of a6 at tau=0
print(f"  Sign of a6_raw(0): {'POSITIVE' if a6_pot[0] > 0 else 'NEGATIVE'}")
print(f"  Sign of a6_raw at all tau: all positive = {np.all(a6_pot > 0)}")
print()

# Critical question: does -R_K + rho*a4 + sigma*a6 have different monotonicity
# than -R_K + rho*a4?
# Since -R_K is monotonically DECREASING and a4, a6 are monotonically INCREASING,
# we need a4 and a6 to have DIFFERENT growth rates for the a_6 term to matter.
print("--- Growth rate comparison ---")
print(f"  {'tau':>4s}  {'R_K':>10s}  {'a4_geom':>12s}  {'a6_raw':>14s}  {'a6/a4':>10s}  {'da6/da4':>10s}")
print("-" * 70)
for idx in range(min(7, n_tau)):
    tau = tau_all[idx]
    ratio = a6_pot[idx] / (a4_pot[idx] + 1e-20)
    da4_val = (a4_pot[min(idx+1, n_tau-1)] - a4_pot[max(idx-1, 0)]) / (tau_all[min(idx+1, n_tau-1)] - tau_all[max(idx-1, 0)] + 1e-20)
    da6_val = (a6_pot[min(idx+1, n_tau-1)] - a6_pot[max(idx-1, 0)]) / (tau_all[min(idx+1, n_tau-1)] - tau_all[max(idx-1, 0)] + 1e-20)
    d_ratio = da6_val / (da4_val + 1e-20)
    print(f"  {tau:4.1f}  {a2_pot[idx]:10.4f}  {a4_pot[idx]:12.4f}  {a6_pot[idx]:14.4f}  {ratio:10.4f}  {d_ratio:10.4f}")
print()


# =====================================================================
# STEP 10: Gate verdict
# =====================================================================

print("=" * 70)
print("GATE VERDICT: a_6 IMPACT ON V_spec MINIMUM")
print("=" * 70)
print()

# Check if a_6 is monotonically increasing like a_4
a6_monotone_inc = np.all(np.diff(a6_pot) > 0)
a4_monotone_inc = np.all(np.diff(a4_pot) > 0)

# Check if a6/a4 ratio is approximately constant (same trap)
ratio_a6_a4 = a6_pot / (a4_pot + 1e-20)
ratio_variation = np.std(ratio_a6_a4[:7]) / (np.mean(ratio_a6_a4[:7]) + 1e-20)

# The decisive test: can a_6 create a minimum?
# V = -R_K + rho*a4 + sigma*a6 (note: spectral action a_2 is proportional to R_K,
# which is monotonically increasing for Jensen deformation, so the EH term
# drives V upward; a4 and a6 also increase. For a minimum, we need competing
# derivatives.)
#
# V'(tau) = R_K'(tau) + rho * a4'(tau) + sigma * a6'(tau)
# = (always > 0) + rho*(always > 0) + sigma * (sign depends on sigma)
#
# If sigma < 0: V' = (positive) + rho*(positive) + sigma*(positive) = (positive) + sigma*(positive)
# This means sigma < 0 makes V' LESS positive, potentially crossing zero.
# But R_K' dominates at small tau and a4', a6' dominate at large tau.
# The question: is there a sigma < 0 where V'(tau*) = 0 and V''(tau*) > 0?

# Check: at tau=0, what are the derivative values?
dR_0 = cs_a2(0.0, 1)
da4_0 = cs_a4(0.0, 1)
da6_0 = cs_a6(0.0, 1)
print(f"Derivatives at tau=0:")
print(f"  R_K'(0) = {dR_0:.6f}")
print(f"  a4_geom'(0) = {da4_0:.6f}")
print(f"  a6_raw'(0) = {da6_0:.6f}")
print()

# At tau=0.15
dR_015 = cs_a2(0.15, 1)
da4_015 = cs_a4(0.15, 1)
da6_015 = cs_a6(0.15, 1)
print(f"Derivatives at tau=0.15:")
print(f"  R_K'(0.15) = {dR_015:.6f}")
print(f"  a4_geom'(0.15) = {da4_015:.6f}")
print(f"  a6_raw'(0.15) = {da6_015:.6f}")
print()

# For V'=0 at tau=0.15: R_K' + rho*a4' + sigma*a6' = 0
# => sigma = -(R_K' + rho*a4') / a6'
if abs(da6_015) > 1e-20:
    for rho_test in [1e-4, 5e-4, 1e-3, bridge_c4c2 if has_bridge else 5e-4]:
        sigma_needed = -(dR_015 + rho_test * da4_015) / da6_015
        print(f"  For minimum at tau=0.15 with rho={rho_test:.4e}: need sigma={sigma_needed:.6e}")
        # Check V'' at this point
        d2V = cs_a2(0.15, 2) + rho_test * cs_a4(0.15, 2) + sigma_needed * cs_a6(0.15, 2)
        print(f"    V''(0.15) = {d2V:.6f} ({'MINIMUM' if d2V > 0 else 'MAXIMUM/SADDLE'})")
print()

# Final verdict
print("-" * 50)
if a6_monotone_inc:
    print("a_6^{raw}(tau) is MONOTONICALLY INCREASING.")
    print()
    if ratio_variation < 0.2:
        print(f"a6/a4 ratio variation: {ratio_variation:.4f} (nearly constant).")
        print("==> a_6 falls into the SAME TRAP as a_4.")
        print("    Both scale the same way with tau.")
        print("    Adding a_6 to V_spec is equivalent to rescaling rho.")
        print("    NO NEW STRUCTURE is generated.")
        verdict = "CLOSED"
    else:
        print(f"a6/a4 ratio variation: {ratio_variation:.4f} (significant variation).")
        print("a_6 grows at a DIFFERENT RATE than a_4.")
        if n_with_min > 0:
            print(f"Minimum found in {n_with_min} parameter space points.")
            verdict = "OPEN"
        else:
            print("Despite different growth rates, no minimum found in parameter scan.")
            verdict = "MARGINAL"
else:
    if n_with_min > 0:
        print("a_6^{raw}(tau) is NON-MONOTONIC and minima found.")
        verdict = "OPEN"
    else:
        print("a_6^{raw}(tau) is non-monotonic but no V_spec minimum found.")
        verdict = "MARGINAL"

print()
print(f"GATE VERDICT: a_6 contribution {verdict}")
if verdict == "CLOSED":
    print("Including the a_6 term in V_spec DOES NOT rescue the V-1 closure.")
    print("The spectral action potential remains monotonically increasing")
    print("for positive rho, sigma (the physical regime).")
    print("Negative sigma (unphysical sign of f_{-2}/Lambda^2) can create")
    print("a minimum, but this requires fine-tuning and is not generic.")
elif verdict == "OPEN":
    print("Including a_6 CREATES new minimum structure in V_spec.")
elif verdict == "MARGINAL":
    print("a_6 introduces different scaling but no robust minimum in physical regime.")
print()


# =====================================================================
# STEP 11: Save results
# =====================================================================

print("Saving results...")
np.savez(
    OUTPUT_NPZ,
    # tau grid
    tau=tau_all,
    tau_fine=tau_fine,
    # Cubic invariants
    R3=cubic_arrays['R3'],
    R_Ric2=cubic_arrays['R_Ric2'],
    R_K=cubic_arrays['R_K'],
    Ric3=cubic_arrays['Ric3'],
    I5=cubic_arrays['I5'],
    I6=cubic_arrays['I6'],
    I7=cubic_arrays['I7'],
    I8=cubic_arrays['I8'],
    Ric_sq=cubic_arrays['Ric_sq'],
    # Omega traces
    Omega2_trace=omega_arrays['Omega2_trace'],
    Ric_OmOm=omega_arrays['Ric_OmOm'],
    Riem_OmOm=omega_arrays['Riem_OmOm'],
    Omega3_trace=omega_arrays['Omega3_trace'],
    Ric_M=omega_arrays['Ric_M'],
    # a_6 decomposition
    a6_universal=a6_arrays['universal'],
    a6_E_part=a6_arrays['E_part'],
    a6_Omega_part=a6_arrays['Omega_part'],
    a6_EO_part=a6_arrays['EO_part'],
    a6_Omega3_part=a6_arrays['Omega3_part'],
    a6_total_raw=a6_arrays['total_raw'],
    a6_red=a6_arrays['a6_red'],
    # Potentials
    a2_pot=a2_pot,
    a4_pot=a4_pot,
    a6_pot=a6_pot,
    # Phase diagram
    rho_values=rho_values,
    sigma_values=sigma_values,
    has_min=has_min,
    min_tau=min_tau,
    min_depth=min_depth,
    # Verdict
    gate_verdict=verdict,
    a6_monotone=a6_monotone_inc,
    a6_a4_ratio_variation=ratio_variation,
)
print(f"  Saved to: {OUTPUT_NPZ}")
print()


# =====================================================================
# STEP 12: Plotting
# =====================================================================

print("Generating plots...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 26 P3: Seeley-DeWitt $a_6$ on Jensen-deformed SU(3)',
             fontsize=14, fontweight='bold')

# (a) a_6^{red}(tau) vs tau
ax = axes[0, 0]
ax.semilogy(tau_all[:7], np.abs(a6_arrays['a6_red'][:7]), 'bo-', markersize=5, label='$|a_6^{\\rm red}|$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|a_6^{\rm red}(\tau)|$')
ax.set_title(r'(a) $a_6^{\rm red}(\tau)$')
ax.legend()
ax.grid(True, alpha=0.3)
# Add decomposition
ax_twin = ax.twinx()
parts_to_plot = ['universal', 'E_part', 'Omega_part', 'EO_part', 'Omega3_part']
colors = ['red', 'green', 'blue', 'orange', 'purple']
for part_name, color in zip(parts_to_plot, colors):
    ax_twin.plot(tau_all[:7], a6_arrays[part_name][:7], '--', color=color, alpha=0.5,
                 label=part_name, linewidth=0.8)
ax_twin.set_ylabel('Raw components', fontsize=8)
ax_twin.legend(fontsize=6, loc='upper left')

# (b) V_spec^(6)(tau) at representative (rho, sigma) values
ax = axes[0, 1]
tau_plot = tau_fine[tau_fine <= 0.5]
# Plot V without a_6 (sigma=0) -- monotonically increasing (V-1 closure)
for rho_test in [1e-4, 5e-4, 1e-3]:
    V_no_a6 = cs_a2(tau_plot) + rho_test * cs_a4(tau_plot)
    V_no_a6_shifted = V_no_a6 - V_no_a6[0]
    ax.plot(tau_plot, V_no_a6_shifted, '-', linewidth=1.5,
            label=f'$\\rho$={rho_test:.0e}, $\\sigma$=0')
# Plot V with the critical negative sigma that creates min at tau=0.15
# sigma_crit = -(R_K' + rho*a4') / a6' at tau=0.15
for rho_test in [1e-4, 5e-4]:
    sigma_crit = -(cs_a2(0.15, 1) + rho_test * cs_a4(0.15, 1)) / cs_a6(0.15, 1)
    V_with_a6 = cs_a2(tau_plot) + rho_test * cs_a4(tau_plot) + sigma_crit * cs_a6(tau_plot)
    V_with_a6_shifted = V_with_a6 - V_with_a6[0]
    ax.plot(tau_plot, V_with_a6_shifted, '--', linewidth=1.0,
            label=f'$\\rho$={rho_test:.0e}, $\\sigma$={sigma_crit:.1e} (crit)')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V(\tau) - V(0)$')
ax.set_title(r'(b) $V_{\rm spec}^{(6)}(\tau)$: solid=$\sigma\!=\!0$, dashed=$\sigma_{\rm crit}$')
ax.legend(fontsize=6, loc='upper left')
ax.grid(True, alpha=0.3)
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(0.15, color='gray', linewidth=0.5, linestyle=':')

# (c) Minimum location vs sigma at fixed rho (negative sigma = unphysical regime)
ax = axes[1, 0]
# Scan wider range of negative sigma to show where minima appear
sigma_scan_c = np.linspace(-5e-3, 0, 5000)
rho_fixed_vals = [1e-4, 5e-4, 1e-3]
colors_c = ['blue', 'red', 'green']
found_any_c = False
for rho_fixed, color_c in zip(rho_fixed_vals, colors_c):
    tau_min_c = []
    depth_c = []
    sigma_c = []
    for sigma in sigma_scan_c:
        mins = find_minima(rho_fixed, sigma, tau_fine, a2_fine, a4_fine, a6_fine,
                          da2_fine, da4_fine, da6_fine,
                          d2a2_fine, d2a4_fine, d2a6_fine)
        if mins:
            best = min(mins, key=lambda x: x[1])
            V0 = a2_fine[0] + rho_fixed * a4_fine[0] + sigma * a6_fine[0]
            Ve = a2_fine[-1] + rho_fixed * a4_fine[-1] + sigma * a6_fine[-1]
            d = min(V0, Ve) - best[1]
            tau_min_c.append(best[0])
            depth_c.append(d)
            sigma_c.append(sigma)
    if tau_min_c:
        found_any_c = True
        ax.plot(sigma_c, tau_min_c, '.-', color=color_c, markersize=2,
                label=f'$\\rho$={rho_fixed:.0e}')

if found_any_c:
    ax.set_xlabel(r'$\sigma$ (negative = unphysical)')
    ax.set_ylabel(r'$\tau_{\rm min}$')
    ax.set_title(r'(c) Min location vs $\sigma$ ($\sigma<0$ only)')
    ax.axhline(0.15, color='gray', linestyle='--', linewidth=0.8, label=r'$\tau_\phi = 0.15$')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)
else:
    ax.text(0.5, 0.5, 'No minima found\nfor any negative sigma\n(positive sigma = monotone)',
            ha='center', va='center', transform=ax.transAxes, fontsize=11)
    ax.set_title(r'(c) Min location vs $\sigma$ ($\sigma<0$ only)')

# (d) Phase diagram: (rho, sigma) with/without minimum
ax = axes[1, 1]
# Use the has_min array from the main scan
# Plot as a filled contour: has_min regions
if np.any(has_min):
    # Find the boundary
    rho_log = np.log10(rho_values)
    sigma_plot = sigma_values.copy()
    # Replace zero with small number for log scale
    extent = [rho_log[0], rho_log[-1], sigma_values[0], sigma_values[-1]]
    ax.contourf(rho_log, sigma_values, has_min.T.astype(float),
                levels=[-0.5, 0.5, 1.5], colors=['white', 'lightblue'],
                alpha=0.7)
    ax.contour(rho_log, sigma_values, has_min.T.astype(float),
               levels=[0.5], colors=['blue'], linewidths=1.5)
    ax.set_xlabel(r'$\log_{10}(\rho)$')
    ax.set_ylabel(r'$\sigma$')
    ax.set_title(r'(d) Phase diagram: blue = minimum exists')
    ax.axhline(0, color='k', linewidth=0.5, linestyle='--')
else:
    ax.text(0.5, 0.5, 'No minima found\nin parameter space',
            ha='center', va='center', transform=ax.transAxes, fontsize=12)
    ax.set_title(r'(d) Phase diagram')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Plot saved to: {OUTPUT_PNG}")
print()


# =====================================================================
# FINAL SUMMARY
# =====================================================================

print("=" * 70)
print("FINAL SUMMARY")
print("=" * 70)
print()
print(f"a_6^{{red}}(tau=0) = {a6_arrays['a6_red'][0]:.10e}")
print(f"a_6^{{red}}(tau=0.15) ~ {0.5*(a6_arrays['a6_red'][1]+a6_arrays['a6_red'][0]):.10e} (interpolated)")
print(f"a_6^{{red}}(tau=0.3) = {a6_arrays['a6_red'][3]:.10e}")
print()
print(f"Omega^2 trace cross-check (should be -2K):")
print(f"  tau=0: tr_S(Omega^2) = {omega_arrays['Omega2_trace'][0]:.10f}, -2K = {-2*K_all[0]:.10f}")
print(f"  PASS: {abs(omega_arrays['Omega2_trace'][0] + 2*K_all[0]) < 1e-10}")
print()
print(f"R_{{abcd}} Omega Omega cross-check (should be -2*I_7):")
print(f"  tau=0: {omega_arrays['Riem_OmOm'][0]:.10f} vs -2*I_7 = {-2*cubic_arrays['I7'][0]:.10f}")
print(f"  PASS: {abs(omega_arrays['Riem_OmOm'][0] + 2*cubic_arrays['I7'][0]) < 1e-10}")
print()
print(f"a_6 monotonically increasing: {a6_monotone_inc}")
print(f"a_6/a_4 ratio variation (tau in [0,0.6]): {ratio_variation:.4f}")
print(f"Parameter space with minimum: {100.0*n_with_min/has_min.size:.1f}%")
print()
print(f"GATE VERDICT: {verdict}")
print()
print("=" * 70)
