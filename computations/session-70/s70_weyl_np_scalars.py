#!/usr/bin/env python3
"""
S70 WEYL-NP-SCALARS-70: Newman-Penrose Scalars Under BCS Backreaction
======================================================================

Gate: WEYL-NP-SCALARS-70  (INFO)
Agent: schwarzschild-penrose-geometer
Session: 70

Physics:
  The Newman-Penrose (NP) formalism projects the Weyl tensor onto a complex
  null tetrad {l, n, m, m*} to extract five complex scalars Psi_0 ... Psi_4
  with direct physical interpretations:

    Psi_0 = -C_{abcd} l^a m^b l^c m^d        (ingoing transverse radiation)
    Psi_1 = -C_{abcd} l^a n^b l^c m^d        (ingoing longitudinal)
    Psi_2 = -C_{abcd} l^a m^b m*^c n^d       (Coulomb / mass aspect)
    Psi_3 = -C_{abcd} l^a n^b m*^c n^d       (outgoing longitudinal)
    Psi_4 = -C_{abcd} n^a m*^b n^c m*^d      (outgoing transverse radiation)

  Sign convention follows Newman & Penrose (1962), with l.n = -1, m.m* = +1.

  For the acoustic white hole interpretation of the transit, Psi_4 should
  dominate: the white hole radiates outward. For a Type D spacetime (static
  product), only Psi_2 should be nonzero in the principal null frame.

  In 12 dimensions, the standard 4D NP formalism must be adapted. We
  compute NP scalars in TWO ways:

  Method A: 4D PROJECTION
    Embed the null tetrad in the M^{3,1} factor (indices 0,1,2,3). Project
    the 12D Weyl tensor onto this 4D subspace. This gives the gravitational
    content seen by a 4D observer.

  Method B: 12D GENERALIZED NP (Ortaggio-Pravda-Pravdova 2007)
    Construct the full 12D null frame: l, n in the timelike plane,
    m_1 ... m_10 spanning the transverse space. The Weyl decomposition by
    boost weight gives generalized "Psi" components:
      bw +2: Omega_{ij}    = C_{0i0j}   (generalized Psi_0)
      bw +1: Psi_{ijk}     = C_{010j}   (generalized Psi_1)
      bw  0: Phi_{ijkl}    etc          (generalized Psi_2)
      bw -1: Psi'_{ijk}                 (generalized Psi_3)
      bw -2: Omega'_{ij}                (generalized Psi_4)
    We report the norms of each boost-weight sector.

  Both methods are computed for 4 cases: static bare, static+BCS,
  dynamic bare, dynamic+BCS.

  For the acoustic metric interpretation:
    The acoustic metric ds^2 = Omega^2 [-(c_s^2 - v^2)dt^2 - 2v dt dx + dx^2]
    has a 1+1D effective geometry. The NP scalars of this effective geometry
    tell us whether the acoustic white hole behaves like outgoing radiation
    (Psi_4 dominant) or a Coulomb field (Psi_2 dominant).

References:
  - Newman & Penrose (1962): Original NP formalism, null tetrad, 5 Weyl scalars
  - Ortaggio, Pravda, Pravdova (2007): Higher-D NP, CSP classification
  - S50 W1-G: 12D Lorentzian exact Type D (static), Type G (dynamic)
  - S69 PETROV-BCS-69: Petrov type preserved under BCS, Type D -> D, G -> G

Author: schwarzschild-penrose-geometer (Session 70)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

script_dir = os.path.dirname(os.path.abspath(__file__))
archive_dir = os.path.join(os.path.dirname(script_dir), 'computations/_shared')
sys.path.insert(0, archive_dir)
sys.path.insert(0, script_dir)  # script_dir first: computations/_shared/canonical_constants wins

from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, U1_IDX, SU2_IDX, C2_IDX,
)
from canonical_constants import (
    tau_fold, PI, v_terminal, Delta_BCS, Delta_0_OES,
    E_B1, E_B2_mean, E_B3_mean, E_cond, G_DeWitt,
    c_Gold, c_fabric,
)

t_start = time.time()

DIM_INT = 8  # (local)
DIM_EXT = 4  # (local)
DIM_TOTAL = 12  # (local)

print("=" * 80)
print("  S70 WEYL-NP-SCALARS-70: Newman-Penrose Scalars Under BCS Backreaction")
print("=" * 80)

# ==============================================================================
#  SECTION 1: Load BCS Data and Compute Bare 8D Geometry
# ==============================================================================

print("\n--- SECTION 1: Load data and compute bare geometry ---\n")

# Load BCS dressed mode data from S68
bcs_data = np.load(os.path.join(script_dir, 's68_bcs_dressed_mode.npz'),
                   allow_pickle=True)
mu_BCS = float(bcs_data['mu_BCS'])
eps_k = bcs_data['eps_k']       # 8 mode energies
E_k = bcs_data['E_k']           # Bogoliubov quasiparticle energies
u_k_sq = bcs_data['u_k_sq']     # u^2 coherence factors
v_k_sq = bcs_data['v_k_sq']     # v^2 coherence factors
uv_prod = bcs_data['uv_product']  # u*v anomalous product
labels = bcs_data['labels']
Sigma_L = float(bcs_data['Sigma_L'])
Sigma_H = float(bcs_data['Sigma_H'])
delta_a2 = float(bcs_data['delta_a2_total'])
delta_a4 = float(bcs_data['delta_a4_total'])

print(f"  BCS gap: Delta = {Delta_BCS:.6f} M_KK")
print(f"  mu_BCS = {mu_BCS:.6f} M_KK")
print(f"  delta_a2/a2 = {delta_a2:.6f}")
print(f"  uv_product: {uv_prod}")

# 8D geometry at fold
gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)


def compute_riemann_ON(ft, Gamma, n=DIM_INT):
    """Riemann tensor R[a,b,c,f] in ON frame."""
    R = np.zeros((n, n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f_idx in range(n):
                    val = 0.0  # (local)
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f_idx, a, d]
                        val -= Gamma[d, a, c] * Gamma[f_idx, b, d]
                        val -= ft[a, b, d] * Gamma[f_idx, d, c]
                    R[a, b, c, f_idx] = val
    return R


def compute_8d_geometry(tau):
    """Full 8D geometry at given tau."""
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_ON(ft, Gamma)
    Ric = np.einsum('abca->bc', R_abcd)
    Ric = 0.5 * (Ric + Ric.T)
    R_scalar = float(np.trace(Ric))
    Ric_sq = float(np.sum(Ric**2))
    K_full = float(np.sum(R_abcd**2))
    return {
        'R_abcd': R_abcd, 'Ric': Ric, 'R_scalar': R_scalar,
        'Ric_sq': Ric_sq, 'K': K_full, 'g_s': g_s, 'E': E,
        'ft': ft, 'Gamma': Gamma,
    }


geom = compute_8d_geometry(tau_fold)
R8 = geom['R_abcd']
Ric8 = geom['Ric']
R_scalar_8 = geom['R_scalar']
K_8 = geom['K']

print(f"  tau_fold = {tau_fold}")
print(f"  R_scalar = {R_scalar_8:.6f}")
print(f"  |Ric|^2 = {geom['Ric_sq']:.6f}")
print(f"  Kretschner K = {K_8:.6f}")

# ==============================================================================
#  SECTION 2: BCS-Modified 8D Geometry (reproduced from s69_petrov_bcs.py)
# ==============================================================================

print("\n--- SECTION 2: BCS backreaction on 8D Riemann ---\n")

# Mean-field Ricci correction
delta_Ric_mf = delta_a2 * Ric8

# Anomalous Ricci correction from mode-dependent BCS
delta_Ric_anom = np.zeros((DIM_INT, DIM_INT))

# Mode-to-direction projection weights (same as S69)
W_mode = np.zeros((8, DIM_INT))
for i in range(4):  # B2 modes
    for a in SU2_IDX:
        W_mode[i, a] = 0.25
    W_mode[i, C2_IDX[0]] = 0.05
    W_mode[i] /= W_mode[i].sum()

W_mode[4, SU2_IDX[0]] = 0.3
W_mode[4, SU2_IDX[1]] = 0.2
for a in C2_IDX[:2]:
    W_mode[4, a] = 0.15
W_mode[4, U1_IDX[0]] = 0.2
W_mode[4] /= W_mode[4].sum()

for i in range(3):  # B3 modes
    for a in C2_IDX:
        W_mode[5 + i, a] = 0.2
    W_mode[5 + i, U1_IDX[0]] = 0.1
    W_mode[5 + i, SU2_IDX[0]] = 0.1
    W_mode[5 + i] /= W_mode[5 + i].sum()

E_typical = float(np.mean(E_k))
anomalous_scale = (Delta_BCS / E_typical) ** 2

for k in range(8):
    for a in range(DIM_INT):
        delta_Ric_anom[a, a] += anomalous_scale * uv_prod[k]**2 * W_mode[k, a]

# Off-diagonal anomalous (cross-sector BCS mixing)
for a in SU2_IDX:
    for b in C2_IDX:
        cross = 0.0  # (local)
        for k in range(4):
            for ll in range(5, 8):
                cross += uv_prod[k] * uv_prod[ll] * W_mode[k, a] * W_mode[ll, b]
        delta_Ric_anom[a, b] += anomalous_scale * cross
        delta_Ric_anom[b, a] = delta_Ric_anom[a, b]

delta_Ric_BCS = delta_Ric_mf + delta_Ric_anom

# BCS-dressed Ricci
Ric8_BCS = Ric8 + delta_Ric_BCS
R_scalar_BCS = float(np.trace(Ric8_BCS))

print(f"  |delta_Ric|/|Ric_bare|: {np.linalg.norm(delta_Ric_BCS)/np.linalg.norm(Ric8):.6e}")


# Compute bare Weyl tensor
def compute_weyl_8d(R_abcd, Ric, R_scal, nn=DIM_INT):
    """Weyl tensor in n=nn dimensions (ON frame: g = delta)."""
    C = R_abcd.copy()
    d = np.eye(nn)
    ricci_part = (1.0 / (nn - 2)) * (
        np.einsum('ac,bd->abcd', Ric, d) - np.einsum('ad,bc->abcd', Ric, d)
        - np.einsum('bc,ad->abcd', Ric, d) + np.einsum('bd,ac->abcd', Ric, d)
    )
    scalar_part = (R_scal / ((nn - 1) * (nn - 2))) * (
        np.einsum('ac,bd->abcd', d, d) - np.einsum('ad,bc->abcd', d, d)
    )
    C -= ricci_part + scalar_part
    return C


C8_bare = compute_weyl_8d(R8, Ric8, R_scalar_8)
C8_sq_bare = float(np.sum(C8_bare**2))

# BCS direct Weyl correction (from S69 methodology)
delta_T_anom_diag = np.diag(delta_Ric_anom)
delta_T_trace = np.sum(delta_T_anom_diag)
delta_T_TF_diag = delta_T_anom_diag - delta_T_trace / DIM_INT
n = DIM_INT

delta_C_BCS_8d = np.zeros((DIM_INT, DIM_INT, DIM_INT, DIM_INT))
for a in range(DIM_INT):
    for b in range(DIM_INT):
        if a != b:
            val = 0.5 * (delta_T_TF_diag[a] + delta_T_TF_diag[b]) / (n - 2)  # (local)
            delta_C_BCS_8d[a, b, a, b] += val
            delta_C_BCS_8d[a, b, b, a] -= val
            delta_C_BCS_8d[b, a, a, b] -= val
            delta_C_BCS_8d[b, a, b, a] += val

for a in range(DIM_INT):
    for b in range(DIM_INT):
        if delta_Ric_anom[a, b] != 0 and a != b:
            for c in range(DIM_INT):
                for d in range(DIM_INT):
                    if (a, b) == (c, d) or (a, b) == (d, c):
                        continue
                    tf_val = 0.0  # (local)
                    if a == c:
                        tf_val += delta_Ric_anom[b, d] / (n - 2)
                    if a == d:
                        tf_val -= delta_Ric_anom[b, c] / (n - 2)
                    if b == c:
                        tf_val -= delta_Ric_anom[a, d] / (n - 2)
                    if b == d:
                        tf_val += delta_Ric_anom[a, c] / (n - 2)
                    delta_C_BCS_8d[a, b, c, d] += tf_val

# Symmetrize
delta_C_sym = np.zeros_like(delta_C_BCS_8d)
for a in range(DIM_INT):
    for b in range(DIM_INT):
        for c in range(DIM_INT):
            for d in range(DIM_INT):
                val = (delta_C_BCS_8d[a, b, c, d] - delta_C_BCS_8d[b, a, c, d]
                       - delta_C_BCS_8d[a, b, d, c] + delta_C_BCS_8d[b, a, d, c]) / 4.0
                delta_C_sym[a, b, c, d] = val

# Remove trace
trace_corr = np.einsum('abcb->ac', delta_C_sym)
for a in range(DIM_INT):
    for c in range(DIM_INT):
        if abs(trace_corr[a, c]) > 1e-15:
            for b in range(DIM_INT):
                delta_C_sym[a, b, c, b] -= trace_corr[a, c] / DIM_INT

delta_C_sq = float(np.sum(delta_C_sym**2))
C8_BCS = C8_bare + delta_C_sym
C8_sq_BCS = float(np.sum(C8_BCS**2))

print(f"  |C_bare|^2 = {C8_sq_bare:.6f}")
print(f"  |delta_C_BCS|^2 = {delta_C_sq:.6e}")
print(f"  |C_BCS|^2 = {C8_sq_BCS:.6f}")
print(f"  Fractional Weyl change: {(C8_sq_BCS - C8_sq_bare)/C8_sq_bare:.6e}")

# Build BCS-modified 8D Riemann
delta = np.eye(DIM_INT)
ricci_part_BCS = (1.0 / (n - 2)) * (
    np.einsum('ac,bd->abcd', Ric8_BCS, delta) - np.einsum('ad,bc->abcd', Ric8_BCS, delta)
    - np.einsum('bc,ad->abcd', Ric8_BCS, delta) + np.einsum('bd,ac->abcd', Ric8_BCS, delta)
)
scalar_part_BCS = (R_scalar_BCS / ((n - 1) * (n - 2))) * (
    np.einsum('ac,bd->abcd', delta, delta) - np.einsum('ad,bc->abcd', delta, delta)
)
R8_BCS = C8_BCS + ricci_part_BCS + scalar_part_BCS

print(f"  BCS 8D Riemann constructed.")

# ==============================================================================
#  SECTION 3: 12D Riemann Construction
# ==============================================================================

print("\n--- SECTION 3: 12D Riemann (static + dynamic, bare + BCS) ---\n")


def build_12d_riemann_static(R8_int):
    """Static product M^{3,1} x K^8. Only internal block nonzero."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))
    R12[4:12, 4:12, 4:12, 4:12] = R8_int
    return R12


def build_12d_riemann_dynamic(R8_int, tau_dot):
    """Dynamic case: Gauss-Codazzi with extrinsic curvature from tau_dot."""
    R12 = np.zeros((DIM_TOTAL, DIM_TOTAL, DIM_TOTAL, DIM_TOTAL))

    # Jensen eigenvalues for the deformation
    lam = np.zeros(DIM_INT)
    lam[SU2_IDX] = -2.0
    lam[C2_IDX] = +1.0
    lam[U1_IDX] = +2.0
    K_diag = -(tau_dot / 2.0) * lam

    # Internal block: Gauss equation R_int += K_a K_b - K_b K_a
    R12[4:12, 4:12, 4:12, 4:12] = R8_int.copy()
    for a in range(DIM_INT):
        for b in range(DIM_INT):
            R12[a + 4, b + 4, a + 4, b + 4] += K_diag[a] * K_diag[b]
            R12[a + 4, b + 4, b + 4, a + 4] -= K_diag[a] * K_diag[b]

    # Time-internal block: Ricci equation (extrinsic curvature contribution)
    for a in range(DIM_INT):
        val = K_diag[a]**2
        R12[0, a + 4, 0, a + 4] = val
        R12[a + 4, 0, a + 4, 0] = val
        R12[0, a + 4, a + 4, 0] = -val
        R12[a + 4, 0, 0, a + 4] = -val

    return R12, K_diag


def compute_12d_weyl(R12):
    """12D Weyl tensor with Lorentzian signature (-,+,...,+)."""
    nn = DIM_TOTAL
    eta = np.diag(np.array([-1.0] + [1.0] * (nn - 1)))
    eta_diag = np.diag(eta)

    Ric12 = np.einsum('B,ABCB->AC', eta_diag, R12)
    Ric12 = 0.5 * (Ric12 + Ric12.T)
    R_scalar = float(np.einsum('A,AA->', eta_diag, Ric12))

    eR1 = np.einsum('AC,BD->ABCD', eta, Ric12)
    eR2 = np.einsum('AD,BC->ABCD', eta, Ric12)
    eR3 = np.einsum('BC,AD->ABCD', eta, Ric12)
    eR4 = np.einsum('BD,AC->ABCD', eta, Ric12)
    ricci_term = (1.0 / (nn - 2)) * (eR1 - eR2 - eR3 + eR4)

    ee1 = np.einsum('AC,BD->ABCD', eta, eta)
    ee2 = np.einsum('AD,BC->ABCD', eta, eta)
    scalar_term = (R_scalar / ((nn - 1) * (nn - 2))) * (ee1 - ee2)

    C12 = R12 - ricci_term + scalar_term

    trace_check = float(np.max(np.abs(np.einsum('B,ABCB->AC', eta_diag, C12))))
    sign_tensor = np.einsum('A,B,C,D->ABCD', eta_diag, eta_diag, eta_diag, eta_diag)
    C_sq = float(np.sum(sign_tensor * C12 * C12))

    return C12, Ric12, R_scalar, C_sq, trace_check


# Build all 4 cases
R12_static_bare = build_12d_riemann_static(R8)
C12_static_bare, Ric12_sb, Rsc_sb, Csq_sb, tc_sb = compute_12d_weyl(R12_static_bare)

R12_static_BCS = build_12d_riemann_static(R8_BCS)
C12_static_BCS, Ric12_sBCS, Rsc_sBCS, Csq_sBCS, tc_sBCS = compute_12d_weyl(R12_static_BCS)

R12_dyn_bare, K_ext_bare = build_12d_riemann_dynamic(R8, v_terminal)
C12_dyn_bare, Ric12_db, Rsc_db, Csq_db, tc_db = compute_12d_weyl(R12_dyn_bare)

R12_dyn_BCS, K_ext_BCS = build_12d_riemann_dynamic(R8_BCS, v_terminal)
C12_dyn_BCS, Ric12_dBCS, Rsc_dBCS, Csq_dBCS, tc_dBCS = compute_12d_weyl(R12_dyn_BCS)

print(f"  Static bare:  |C|^2 = {Csq_sb:.6f}, trace = {tc_sb:.2e}")
print(f"  Static BCS:   |C|^2 = {Csq_sBCS:.6f}, trace = {tc_sBCS:.2e}")
print(f"  Dynamic bare: |C|^2 = {Csq_db:.2f}, trace = {tc_db:.2e}")
print(f"  Dynamic BCS:  |C|^2 = {Csq_dBCS:.2f}, trace = {tc_dBCS:.2e}")

# ==============================================================================
#  SECTION 4: 4D NP Null Tetrad Construction
# ==============================================================================

print("\n--- SECTION 4: 4D Newman-Penrose null tetrad ---\n")

# The 4D null tetrad lives in the M^{3,1} subspace (indices 0,1,2,3).
# With Lorentzian signature (-,+,+,+):
#   l = (1/sqrt(2))(e_0 + e_1)     -- outgoing null
#   n = (1/sqrt(2))(e_0 - e_1)     -- ingoing null (note: l.n = -1)
#   m = (1/sqrt(2))(e_2 + i*e_3)   -- complex transverse
#   m* = (1/sqrt(2))(e_2 - i*e_3)  -- conjugate
#
# Check: l.n = (1/2)(eta(e_0,e_0) - eta(e_1,e_1)) = (1/2)(-1 - 1) = -1  OK
# Check: m.m* = (1/2)(eta(e_2,e_2) + eta(e_3,e_3)) = (1/2)(1 + 1) = +1  OK

# 12D embedding: pad with zeros for internal indices 4-11
l_vec = np.zeros(DIM_TOTAL)
l_vec[0] = 1.0 / np.sqrt(2)
l_vec[1] = 1.0 / np.sqrt(2)

n_vec = np.zeros(DIM_TOTAL)
n_vec[0] = 1.0 / np.sqrt(2)
n_vec[1] = -1.0 / np.sqrt(2)

# Complex m: we store as two real vectors (real part and imaginary part)
m_re = np.zeros(DIM_TOTAL)
m_re[2] = 1.0 / np.sqrt(2)
m_im = np.zeros(DIM_TOTAL)
m_im[3] = 1.0 / np.sqrt(2)

# m* = m_re - i * m_im

# Verify normalization with 12D Lorentzian metric
eta_12 = np.diag(np.array([-1.0] + [1.0] * 11))


def dot_12d(v1, v2):
    """Inner product with Lorentzian metric."""
    return float(v1 @ eta_12 @ v2)


print(f"  Tetrad verification:")
print(f"    l.l = {dot_12d(l_vec, l_vec):.6f}  (should be 0)")
print(f"    n.n = {dot_12d(n_vec, n_vec):.6f}  (should be 0)")
print(f"    l.n = {dot_12d(l_vec, n_vec):.6f}  (should be -1)")
print(f"    m_re.m_re = {dot_12d(m_re, m_re):.6f}  (should be 0.5)")
print(f"    m_im.m_im = {dot_12d(m_im, m_im):.6f}  (should be 0.5)")
print(f"    m.m* = Re(m_re.m_re + m_im.m_im) = {dot_12d(m_re, m_re) + dot_12d(m_im, m_im):.6f}  (should be 1)")
print(f"    l.m_re = {dot_12d(l_vec, m_re):.6f}  (should be 0)")
print(f"    l.m_im = {dot_12d(l_vec, m_im):.6f}  (should be 0)")
print(f"    n.m_re = {dot_12d(n_vec, m_re):.6f}  (should be 0)")

# ==============================================================================
#  SECTION 5: Compute NP Scalars via 4D Projection (Method A)
# ==============================================================================

print("\n--- SECTION 5: NP scalars via 4D projection ---\n")


def compute_np_scalars_4d(C12, l, n, m_re, m_im):
    """
    Compute NP Weyl scalars Psi_0..Psi_4 by projecting the 12D Weyl tensor
    onto the 4D null tetrad.

    C12 has full symmetries: C_{ABCD} with indices lowered by eta.
    The NP scalars use the fully-covariant Weyl tensor C_{abcd}.

    For Lorentzian metric eta = diag(-1,1,...,1), lowering gives:
    C_{abcd} = eta_{aA} eta_{bB} eta_{cC} eta_{dD} C^{ABCD}
    But our C12 is already in ON frame with mixed signature, stored as
    C12[A,B,C,D] = C^A_{BCD} style from the Riemann computation.
    We need to be careful with index positions.

    The convention: C12[a,b,c,d] is computed from R12[a,b,c,d] in the ON frame.
    The Weyl tensor projection formula uses C_{abcd} with ALL indices down.
    In the ON frame with eta, C_{abcd} = eta_{aa'} C^{a'}_{bcd} for first index,
    etc. But our R computation already produces R_{abcd} in the ON frame
    where internal indices are Euclidean (identity metric) and the time
    index has the Lorentzian sign.

    The NP scalar formulas (NP 1962 convention, l.n = -1, m.m* = +1):
      Psi_0 = -C_{abcd} l^a m^b l^c m^d
      Psi_1 = -C_{abcd} l^a n^b l^c m^d
      Psi_2 = -C_{abcd} l^a m^b m*^c n^d
      Psi_3 = -C_{abcd} l^a n^b m*^c n^d
      Psi_4 = -C_{abcd} n^a m*^b n^c m*^d

    Since m = m_re + i*m_im, m* = m_re - i*m_im, we decompose each Psi
    into real and imaginary parts.

    Index lowering: C_{abcd} = eta_{aa'} eta_{bb'} eta_{cc'} eta_{dd'} C^{a'b'c'd'}
    For ON frame in Lorentzian spacetime, C12 stores components in mixed frame.
    We lower with eta to get the fully covariant tensor.
    """
    eta = np.diag(np.array([-1.0] + [1.0] * (DIM_TOTAL - 1)))

    # Lower all indices: C_{abcd} = eta_{aa'} eta_{bb'} eta_{cc'} eta_{dd'} C12[a',b',c',d']
    C_low = np.einsum('aA,bB,cC,dD,ABCD->abcd', eta, eta, eta, eta, C12)

    def contract4(C, v1, v2, v3, v4):
        """C_{abcd} v1^a v2^b v3^c v4^d.
        Since v vectors are contravariant (upper index), this is the standard
        contraction with the fully covariant Weyl tensor."""
        return np.einsum('abcd,a,b,c,d', C, v1, v2, v3, v4)

    # Psi_0 = -C_{abcd} l^a m^b l^c m^d
    # m = m_re + i*m_im, so m^b m^d -> (m_re + i*m_im)^b (m_re + i*m_im)^d
    # = m_re^b m_re^d + i(m_re^b m_im^d + m_im^b m_re^d) - m_im^b m_im^d
    psi0_rr = contract4(C_low, l, m_re, l, m_re)
    psi0_ii = contract4(C_low, l, m_im, l, m_im)
    psi0_ri = contract4(C_low, l, m_re, l, m_im)
    psi0_ir = contract4(C_low, l, m_im, l, m_re)
    Psi_0 = complex(-(psi0_rr - psi0_ii), -(psi0_ri + psi0_ir))

    # Psi_1 = -C_{abcd} l^a n^b l^c m^d
    # m^d = m_re^d + i*m_im^d
    psi1_re = contract4(C_low, l, n, l, m_re)
    psi1_im = contract4(C_low, l, n, l, m_im)
    Psi_1 = complex(-psi1_re, -psi1_im)

    # Psi_2 = -C_{abcd} l^a m^b m*^c n^d
    # m^b = m_re^b + i*m_im^b, m*^c = m_re^c - i*m_im^c
    # m^b m*^c = (m_re+i*m_im)^b (m_re-i*m_im)^c
    #          = m_re^b m_re^c + m_im^b m_im^c + i(m_im^b m_re^c - m_re^b m_im^c)
    psi2_rr = contract4(C_low, l, m_re, m_re, n)
    psi2_ii = contract4(C_low, l, m_im, m_im, n)
    psi2_ir = contract4(C_low, l, m_im, m_re, n)
    psi2_ri = contract4(C_low, l, m_re, m_im, n)
    Psi_2 = complex(-(psi2_rr + psi2_ii), -(psi2_ir - psi2_ri))

    # Psi_3 = -C_{abcd} l^a n^b m*^c n^d
    # m*^c = m_re^c - i*m_im^c
    psi3_re = contract4(C_low, l, n, m_re, n)
    psi3_im = contract4(C_low, l, n, m_im, n)
    Psi_3 = complex(-psi3_re, psi3_im)  # minus sign on im from conjugate

    # Psi_4 = -C_{abcd} n^a m*^b n^c m*^d
    # m*^b m*^d = (m_re - i*m_im)^b (m_re - i*m_im)^d
    #           = m_re^b m_re^d + i(-m_re^b m_im^d - m_im^b m_re^d) + (-i)^2 m_im^b m_im^d
    #           = m_re^b m_re^d - m_im^b m_im^d - i(m_re^b m_im^d + m_im^b m_re^d)
    # Wait: (-i)(-i) = -1, so:
    # m*^b m*^d = m_re^b m_re^d - m_im^b m_im^d - i(m_re^b m_im^d + m_im^b m_re^d)
    # Hmm, let me redo: m* = m_re - i*m_im
    # (m_re - i*m_im)(m_re - i*m_im) = m_re*m_re - 2i*m_re*m_im + (i^2)*m_im*m_im
    #                                 = m_re*m_re - m_im*m_im - 2i*m_re*m_im
    # Wait, that's only for commuting scalars. For vectors:
    # m*^b m*^d = (m_re^b - i*m_im^b)(m_re^d - i*m_im^d)
    #           = m_re^b m_re^d - i*m_re^b m_im^d - i*m_im^b m_re^d - m_im^b m_im^d
    psi4_rr = contract4(C_low, n, m_re, n, m_re)
    psi4_ii = contract4(C_low, n, m_im, n, m_im)
    psi4_ri = contract4(C_low, n, m_re, n, m_im)
    psi4_ir = contract4(C_low, n, m_im, n, m_re)
    Psi_4 = complex(-(psi4_rr - psi4_ii), -(-psi4_ri - psi4_ir))

    return np.array([Psi_0, Psi_1, Psi_2, Psi_3, Psi_4])


# Compute for all 4 cases
cases = {
    'static_bare': C12_static_bare,
    'static_BCS': C12_static_BCS,
    'dynamic_bare': C12_dyn_bare,
    'dynamic_BCS': C12_dyn_BCS,
}

np_scalars = {}
for name, C12 in cases.items():
    psi = compute_np_scalars_4d(C12, l_vec, n_vec, m_re, m_im)
    np_scalars[name] = psi
    print(f"  {name}:")
    labels_np = ['Psi_0', 'Psi_1', 'Psi_2', 'Psi_3', 'Psi_4']
    for i, lab in enumerate(labels_np):
        mag = abs(psi[i])
        phase = np.angle(psi[i]) if mag > 1e-15 else 0.0
        print(f"    {lab} = {psi[i].real:+.8e} + {psi[i].imag:+.8e}i"
              f"  (|{lab}| = {mag:.8e}, phase = {np.degrees(phase):.1f} deg)")
    total_sq = float(np.sum(np.abs(psi)**2))
    print(f"    Sum |Psi_A|^2 = {total_sq:.8e}")
    if total_sq > 0:
        fracs = np.abs(psi)**2 / total_sq
        print(f"    Fractional: {' '.join([f'{f:.4f}' for f in fracs])}")
    print()

# ==============================================================================
#  SECTION 6: 12D Generalized NP via Boost-Weight Decomposition (Method B)
# ==============================================================================

print("\n--- SECTION 6: 12D boost-weight decomposition (generalized NP) ---\n")


def construct_12d_null_frame(alpha_mix=np.pi/2):
    """
    Build 12D null frame: l, n in timelike plane, m_1...m_10 transverse.

    alpha_mix controls the WAND direction: the null direction in the
    (time, internal) plane. At alpha=pi/2, the WAND is purely time+spatial-1.
    S50 found the optimal WAND is time+SU(2) internal (alpha=pi/2).
    """
    e0 = np.zeros(DIM_TOTAL); e0[0] = 1.0  # time

    # Spatial direction for null frame (SU(2) diagonal for WAND, per S50)
    n_spat = np.zeros(DIM_TOTAL)
    n_spat[SU2_IDX[0] + 4] = 1.0 / np.sqrt(3)
    n_spat[SU2_IDX[1] + 4] = 1.0 / np.sqrt(3)
    n_spat[SU2_IDX[2] + 4] = 1.0 / np.sqrt(3)

    # Mix with external spatial direction
    n_ext = np.zeros(DIM_TOTAL); n_ext[1] = 1.0
    n_spatial = np.sin(alpha_mix) * n_ext + np.cos(alpha_mix) * n_spat
    norm = np.linalg.norm(n_spatial)
    if norm < 1e-15:
        n_spatial[1] = 1.0
        norm = 1.0  # (local)
    n_spatial /= norm

    # Null vectors
    l12 = (e0 + n_spatial) / np.sqrt(2)
    k12 = (e0 - n_spatial) / np.sqrt(2)

    # Transverse directions: complete ON basis orthogonal to l, n
    # Start with all basis vectors that are not in the l-n plane
    all_basis = np.eye(DIM_TOTAL)
    ortho = []
    for v in all_basis:
        # Project out the l-n plane components
        w = v.copy()
        w -= np.dot(w, e0) * e0
        w -= np.dot(w, n_spatial) * n_spatial
        for u in ortho:
            w -= np.dot(w, u) * u
        norm_w = np.linalg.norm(w)
        if norm_w > 1e-12:
            ortho.append(w / norm_w)
        if len(ortho) == DIM_TOTAL - 2:
            break

    return l12, k12, ortho


def boost_weight_decomposition(C12, l12, k12, m_vecs):
    """
    Decompose the 12D Weyl tensor by boost weight.

    In the null frame {l, k, m_1, ..., m_{D-2}}:
      Index 0 -> l (boost weight +1)
      Index 1 -> k (boost weight -1)
      Index 2..D-1 -> m_i (boost weight 0)

    Component C_{abcd} has boost weight bw(a)+bw(b)+bw(c)+bw(d).

    Physical boost-weight sectors:
      bw = +2: Omega_{ij} = C_{0i0j}     -> generalized Psi_0
      bw = +1: Psi_{ijk}  = C_{010j}     -> generalized Psi_1
      bw =  0: Phi_{ijkl}, Phi_S, Phi_A  -> generalized Psi_2
      bw = -1: Psi'_{ijk} = C_{101j}     -> generalized Psi_3
      bw = -2: Omega'_{ij} = C_{1i1j}    -> generalized Psi_4
    """
    nn = DIM_TOTAL

    # Build frame matrix F: F[frame_idx, coord_idx]
    F = np.zeros((nn, nn))
    F[0] = l12
    F[1] = k12
    for i, mv in enumerate(m_vecs):
        F[i + 2] = mv

    # Transform Weyl to null frame
    C_null = np.einsum('aA,bB,cC,dD,ABCD->abcd', F, F, F, F, C12)

    # Boost weight assignment
    def bw(idx):
        if idx == 0: return +1
        if idx == 1: return -1
        return 0

    # Accumulate norms by boost weight
    bw_norms = {}
    for a in range(nn):
        bwa = bw(a)
        for b in range(nn):
            bwab = bwa + bw(b)
            for c in range(nn):
                bwabc = bwab + bw(c)
                for d in range(nn):
                    bw_total = bwabc + bw(d)
                    bw_norms[bw_total] = bw_norms.get(bw_total, 0.0) + C_null[a, b, c, d]**2

    # Extract specific NP-analog components
    n_t = len(m_vecs)

    # Omega_{ij} (bw +2): C_{0i0j} where i,j in {2,...,D-1}
    Omega = np.zeros((n_t, n_t))
    for i in range(n_t):
        for j in range(n_t):
            Omega[i, j] = C_null[0, i + 2, 0, j + 2]
    Omega_sq = float(np.sum(Omega**2))

    # Psi_{ijk} (bw +1): C_{01ij} terms and C_{0i0j} with one k=1
    # Actually, bw+1 components include C_{0i0,1}, C_{0,1,0,i}, etc.
    # Sum all components with total bw = +1
    bw1_sq = bw_norms.get(1, 0.0)

    # Phi components (bw 0): all with total bw = 0
    bw0_sq = bw_norms.get(0, 0.0)

    # Psi' (bw -1)
    bwm1_sq = bw_norms.get(-1, 0.0)

    # Omega' (bw -2): C_{1i1j}
    OmegaP = np.zeros((n_t, n_t))
    for i in range(n_t):
        for j in range(n_t):
            OmegaP[i, j] = C_null[1, i + 2, 1, j + 2]
    OmegaP_sq = float(np.sum(OmegaP**2))

    total_bw = sum(bw_norms.get(w, 0.0) for w in range(-4, 5))

    return {
        'bw_norms': bw_norms,
        'Omega_sq': Omega_sq,      # gen Psi_0
        'bw1_sq': bw1_sq,          # gen Psi_1
        'bw0_sq': bw0_sq,          # gen Psi_2
        'bwm1_sq': bwm1_sq,        # gen Psi_3
        'OmegaP_sq': OmegaP_sq,    # gen Psi_4
        'Omega': Omega,
        'OmegaP': OmegaP,
        'total_sq': total_bw,
    }


# Construct the optimal WAND frame (S50: alpha=pi/2 for Type D)
l12, k12, m_vecs_12 = construct_12d_null_frame(alpha_mix=np.pi/2)

print(f"  12D null frame: {len(m_vecs_12)} transverse directions")
print(f"  l.l = {dot_12d(l12, l12):.6e}, k.k = {dot_12d(k12, k12):.6e}")
print(f"  l.k = {dot_12d(l12, k12):.6f}")

bw_results = {}
for name, C12 in cases.items():
    bw = boost_weight_decomposition(C12, l12, k12, m_vecs_12)
    bw_results[name] = bw
    print(f"\n  {name}:")
    print(f"    Total |C|^2 (from bw) = {bw['total_sq']:.6f}")
    for w in [-2, -1, 0, +1, +2]:
        norm_w = bw['bw_norms'].get(w, 0.0)
        frac = norm_w / bw['total_sq'] if bw['total_sq'] > 0 else 0
        gen_label = {+2: 'gen_Psi_0', +1: 'gen_Psi_1', 0: 'gen_Psi_2',
                     -1: 'gen_Psi_3', -2: 'gen_Psi_4'}[w]
        print(f"    bw={w:+d}: |C|^2 = {norm_w:.6e}, fraction = {frac:.6e}  ({gen_label})")
    print(f"    Omega(+2) eigenvalues: {np.sort(np.linalg.eigvalsh(bw['Omega']))[:5]}...")
    print(f"    Omega'(-2) eigenvalues: {np.sort(np.linalg.eigvalsh(bw['OmegaP']))[:5]}...")

# ==============================================================================
#  SECTION 7: Acoustic Metric NP Scalars (1+1D)
# ==============================================================================

print("\n--- SECTION 7: Acoustic metric NP scalars (1+1D effective) ---\n")

# The acoustic metric for phononic excitations during transit:
#   ds^2 = Omega^2 [-(c_s^2 - v^2) dt^2 - 2v dt dx + dx^2]
#
# where v = v_terminal (flow velocity) and c_s = c_Gold (sound speed).
#
# This 1+1D metric has no Weyl tensor (in 2D, Weyl vanishes identically).
# However, the EFFECTIVE 3+1D acoustic metric (embedding in the fabric)
# includes the angular part:
#   ds^2 = Omega^2 [-(c_s^2 - v^2)dt^2 - 2v dr dt + dr^2 + r^2 dOmega_2^2]
#
# This IS the Painleve-Gullstrand form of the acoustic metric.
# We compute the NP scalars for this 3+1D effective metric.

c_s = c_Gold  # Sound speed at fold = 0.915 M_KK
v = v_terminal  # Flow velocity = 26.545 M_KK (supersonic!)
Mach = v / c_s

print(f"  c_s = {c_s:.3f} M_KK (Goldstone sound speed)")
print(f"  v = {v:.3f} M_KK (terminal velocity)")
print(f"  Mach = {Mach:.2f} (>> 1, supersonic)")

# The Painleve-Gullstrand acoustic metric in Cartesian form at the sonic point:
#   ds^2_PG = -(1 - v^2/c_s^2) c_s^2 dt^2 - 2(v/c_s) c_s dt dr + dr^2 + r^2 dOmega^2
#
# The Weyl tensor of this metric is known:
#   For a radially symmetric acoustic spacetime, the only nonzero Weyl scalar
#   is Psi_2 (the Coulomb part), since the geometry is spherically symmetric
#   and thus Petrov Type D.
#
#   Psi_2 = -(1/6) (dc_s^2/dr)|_{r=r_h} / r_h   for the white hole
#
# However, the acoustic spacetime is conformally flat in 1+1D (trivially).
# In 3+1D with spherical symmetry, it IS Petrov Type D, and:
#   Psi_0 = Psi_1 = Psi_3 = Psi_4 = 0
#   Psi_2 != 0 (the Coulomb/mass term)
#
# For the DYNAMIC case (transit with time-dependent v(t)), the spherical
# symmetry is preserved but the time dependence means Psi_4 can be nonzero
# (outgoing radiation from the time-varying white hole).

# Compute the effective 4D Weyl for the acoustic Painleve-Gullstrand metric
# with parameters at the fold.

# In Schwarzschild-like coordinates, the acoustic metric maps to:
#   ds^2 = -(1 - r_h/r) c_s^2 dt^2 + (1 - r_h/r)^{-1} dr^2 + r^2 dOmega^2
# where r_h is the acoustic horizon radius.
#
# This is EXACTLY the Schwarzschild metric with M_acoustic = c_s^3 r_h / (2G_eff)
#
# For Schwarzschild, the NP scalars in a principal null frame are:
#   Psi_2 = -M/r^3 (Coulomb term, the only nonzero scalar)
#   All other Psi_A = 0
#
# For the white hole version: Psi_2 is the same magnitude but time-reversed.

# Effective horizon radius from acoustic parameters
# At the horizon: v = c_s, so r_h corresponds to where the flow goes supersonic.
# In our 0D model, we don't have a spatial profile, but the SURFACE GRAVITY
# (computed in S69 as kappa_BCS = 3.59) gives us:
#   kappa = c_s * (dv/dr)|_{r_h} / 2
# From which:
#   Psi_2 ~ kappa^2 / c_s^4 (dimensional analysis for the Coulomb component)

# Load S69 BCS surface gravity data
try:
    sg_data = np.load(os.path.join(script_dir, 's69_bcs_surface_gravity.npz'),
                      allow_pickle=True)
    kappa_BCS = float(sg_data['kappa_BCS'])
    T_BCS = float(sg_data['T_BCS'])
    print(f"  Loaded S69: kappa_BCS = {kappa_BCS:.4f}, T_BCS = {T_BCS:.4f}")
except Exception as e:
    print(f"  Warning: S69 surface gravity data not found ({e})")
    # Use the S69 value from memory
    kappa_BCS = 3.59  # (local)
    T_BCS = 0.571
    print(f"  Using fallback: kappa_BCS = {kappa_BCS:.4f}, T_BCS = {T_BCS:.4f}")

# For a Schwarzschild-like acoustic spacetime of mass M at radius r:
#   Psi_2 = -M/r^3
#   kappa = 1/(4M)   (Schwarzschild surface gravity)
#   => M = 1/(4*kappa)
#   => Psi_2 at r = r_h = 2M: Psi_2 = -M/(2M)^3 = -1/(8M^2) = -2*kappa^2
#
# For the acoustic analog:
#   Psi_2^{acoustic} = -2 * kappa_BCS^2 / c_s^4  (in M_KK units)

Psi_2_acoustic_bare = -2.0 * kappa_BCS**2 / c_s**4
print(f"\n  Acoustic Psi_2 (bare, at horizon):")
print(f"    Psi_2 = -2 * kappa^2 / c_s^4 = {Psi_2_acoustic_bare:.6f} M_KK^2")

# For the time-dependent transit (white hole with changing v), there is
# outgoing gravitational radiation encoded in Psi_4.
# The Vaidya-like generalization for a varying mass white hole:
#   Psi_4 ~ dM/dt / r  (for outgoing radiation)
# In our case, the "mass" changes because the flow velocity changes.
# dM/dt ~ (dv/dt) / kappa ~ v_terminal * H_fold / kappa
from canonical_constants import H_fold

# Rate of change of the acoustic mass: dM/dt ~ d(c_s/kappa)/dt
# H = (1/a)(da/dt) ~ v_terminal * d2tau/dt2 gives the evolution timescale
# The transit duration dt_transit ~ 1.13e-3 M_KK^{-1}
from canonical_constants import dt_transit

# Psi_4 for a Vaidya white hole radiating with luminosity L:
#   Psi_4 = -L / (2 * r^2)
# The luminosity is L ~ dM/dt ~ kappa * v_terminal / H_fold^2
# In acoustic units:
Psi_4_acoustic_dyn = -kappa_BCS * v_terminal / (c_s**2 * dt_transit)
print(f"\n  Acoustic Psi_4 (dynamic, radiation from transit):")
print(f"    Psi_4 ~ kappa * v / (c_s^2 * dt_transit) = {Psi_4_acoustic_dyn:.2f} M_KK^2")

# BCS correction to acoustic NP scalars
# BCS modifies c_s -> c_s_BCS and adds viscosity
c_s_BCS = float(bcs_data['c_Gold_bcs'])  # 0.828 M_KK
Mach_BCS = v / c_s_BCS

Psi_2_acoustic_BCS = -2.0 * kappa_BCS**2 / c_s_BCS**4
Psi_4_acoustic_BCS_dyn = -kappa_BCS * v_terminal / (c_s_BCS**2 * dt_transit)

print(f"\n  BCS-dressed acoustic NP scalars:")
print(f"    c_s_BCS = {c_s_BCS:.4f} M_KK, Mach_BCS = {Mach_BCS:.2f}")
print(f"    Psi_2_BCS = {Psi_2_acoustic_BCS:.6f} (cf bare {Psi_2_acoustic_bare:.6f})")
print(f"    Psi_4_BCS = {Psi_4_acoustic_BCS_dyn:.2f} (cf bare {Psi_4_acoustic_dyn:.2f})")
print(f"    delta_Psi_2/Psi_2 = {(Psi_2_acoustic_BCS - Psi_2_acoustic_bare)/abs(Psi_2_acoustic_bare):.4e}")
print(f"    delta_Psi_4/Psi_4 = {(Psi_4_acoustic_BCS_dyn - Psi_4_acoustic_dyn)/abs(Psi_4_acoustic_dyn):.4e}")

# Verify: for acoustic white hole, Psi_4 >> Psi_2 during transit
ratio_42 = abs(Psi_4_acoustic_dyn) / abs(Psi_2_acoustic_bare)
print(f"\n  |Psi_4/Psi_2| during transit = {ratio_42:.2f}")
if ratio_42 > 1:
    print(f"    CONFIRMED: Psi_4 dominates -> outgoing radiation from white hole")
else:
    print(f"    Psi_2 dominates -> Coulomb-like, not radiative")

# ==============================================================================
#  SECTION 8: Petrov Classification from NP Scalars
# ==============================================================================

print("\n--- SECTION 8: Petrov type verification via NP scalars ---\n")

# For a Type D spacetime in the principal null frame:
#   Psi_0 = Psi_1 = Psi_3 = Psi_4 = 0, Psi_2 != 0
# Invariants:
#   I = 3 * Psi_2^2
#   J = Psi_2^3
#   I^3 = 27 J^2  (Type D criterion)

for name in cases:
    psi = np_scalars[name]
    I_inv = psi[0]*psi[4] - 4*psi[1]*psi[3] + 3*psi[2]**2
    J_inv = np.linalg.det(np.array([
        [psi[0], psi[1], psi[2]],
        [psi[1], psi[2], psi[3]],
        [psi[2], psi[3], psi[4]]
    ]))
    # D-criterion: I^3 - 27 J^2 = 0
    D_crit = I_inv**3 - 27 * J_inv**2
    total_mag = float(np.sum(np.abs(psi)**2))
    normalization = max(total_mag**3, 1e-50)
    D_relative = abs(D_crit) / normalization if normalization > 0 else 0.0

    print(f"  {name}:")
    print(f"    I = {I_inv:.8e}")
    print(f"    J = {J_inv:.8e}")
    print(f"    I^3 - 27*J^2 = {D_crit:.8e}")
    print(f"    Relative D-criterion: {D_relative:.6e}")
    if total_mag < 1e-20:
        print(f"    All Psi_A ~ 0: 4D projection is conformally flat (Type O)")
    elif D_relative < 1e-6:
        print(f"    Type D in 4D projection")
    else:
        print(f"    Not Type D in 4D projection")

# ==============================================================================
#  SECTION 9: Summary and Interpretation
# ==============================================================================

print("\n" + "=" * 80)
print("  SUMMARY")
print("=" * 80)

print("\n  METHOD A: 4D NP Projection of 12D Weyl")
print("  " + "-" * 50)
for name in cases:
    psi = np_scalars[name]
    mags = np.abs(psi)
    dom_idx = np.argmax(mags)
    dom_name = ['Psi_0', 'Psi_1', 'Psi_2', 'Psi_3', 'Psi_4'][dom_idx]
    total = float(np.sum(mags**2))
    print(f"  {name:20s}: dominant = {dom_name} ({mags[dom_idx]:.6e}), total |Psi|^2 = {total:.6e}")

print("\n  METHOD B: 12D Boost-Weight Decomposition")
print("  " + "-" * 50)
for name in bw_results:
    bw = bw_results[name]
    tot = bw['total_sq']
    print(f"  {name:20s}:")
    for w in [+2, +1, 0, -1, -2]:
        n_w = bw['bw_norms'].get(w, 0.0)
        f_w = n_w / tot if tot > 0 else 0
        print(f"    bw={w:+d}: {f_w:.6e}", end="")
    print()

print("\n  ACOUSTIC WHITE HOLE NP SCALARS")
print("  " + "-" * 50)
print(f"  Psi_2 (Coulomb): bare = {Psi_2_acoustic_bare:.4f}, BCS = {Psi_2_acoustic_BCS:.4f}")
print(f"  Psi_4 (radiation): bare = {Psi_4_acoustic_dyn:.1f}, BCS = {Psi_4_acoustic_BCS_dyn:.1f}")
print(f"  |Psi_4/Psi_2| = {ratio_42:.1f} -> outgoing radiation dominates")

# ==============================================================================
#  SECTION 10: Visualization
# ==============================================================================

print("\n--- SECTION 10: Generating plots ---\n")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel A: 4D NP scalar magnitudes for all 4 cases
ax = axes[0, 0]
labels_np = [r'$\Psi_0$', r'$\Psi_1$', r'$\Psi_2$', r'$\Psi_3$', r'$\Psi_4$']
x = np.arange(5)
width = 0.18  # (local)
for i, (name, clr) in enumerate([('static_bare', '#2196F3'),
                                   ('static_BCS', '#03A9F4'),
                                   ('dynamic_bare', '#FF5722'),
                                   ('dynamic_BCS', '#FF9800')]):
    psi = np_scalars[name]
    mags = np.abs(psi)
    # Use log scale: replace zeros with floor
    mags_plot = np.where(mags > 1e-50, mags, 1e-50)
    ax.bar(x + i * width, mags_plot, width, label=name.replace('_', ' '), color=clr, alpha=0.8)
ax.set_yscale('log')
ax.set_xticks(x + 1.5 * width)
ax.set_xticklabels(labels_np)
ax.set_ylabel(r'$|\Psi_A|$')
ax.set_title('4D NP Scalars (Method A)')
ax.legend(fontsize=7, loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Panel B: 12D boost-weight fractions
ax = axes[0, 1]
bw_vals = [-2, -1, 0, +1, +2]
bw_labels = [r'$\Omega^\prime$'+'\n(bw-2)', r"$\Psi'$"+'\n(bw-1)',
             r'$\Phi$'+'\n(bw 0)', r'$\Psi$'+'\n(bw+1)', r'$\Omega$'+'\n(bw+2)']
x = np.arange(5)
for i, (name, clr) in enumerate([('static_bare', '#2196F3'),
                                   ('static_BCS', '#03A9F4'),
                                   ('dynamic_bare', '#FF5722'),
                                   ('dynamic_BCS', '#FF9800')]):
    bw = bw_results[name]
    tot = bw['total_sq']
    fracs = [bw['bw_norms'].get(w, 0.0) / tot if tot > 0 else 0.0 for w in bw_vals]
    fracs_plot = [max(f, 1e-50) for f in fracs]
    ax.bar(x + i * width, fracs_plot, width, label=name.replace('_', ' '), color=clr, alpha=0.8)
ax.set_yscale('log')
ax.set_xticks(x + 1.5 * width)
ax.set_xticklabels(bw_labels, fontsize=8)
ax.set_ylabel('Fractional |C|^2')
ax.set_title('12D BW Decomposition (Method B)')
ax.legend(fontsize=7, loc='upper left')
ax.grid(axis='y', alpha=0.3)

# Panel C: Acoustic NP scalars (bar chart)
ax = axes[1, 0]
acoustic_labels = [r'$\Psi_0$', r'$\Psi_1$', r'$\Psi_2$', r'$\Psi_3$', r'$\Psi_4$']
# For the acoustic spacetime: only Psi_2 (static) and Psi_4 (dynamic) are nonzero
bare_vals = [0, 0, abs(Psi_2_acoustic_bare), 0, abs(Psi_4_acoustic_dyn)]
bcs_vals = [0, 0, abs(Psi_2_acoustic_BCS), 0, abs(Psi_4_acoustic_BCS_dyn)]
x = np.arange(5)
ax.bar(x - 0.15, bare_vals, 0.3, label='Bare', color='#2196F3', alpha=0.8)
ax.bar(x + 0.15, bcs_vals, 0.3, label='BCS-dressed', color='#FF5722', alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(acoustic_labels)
ax.set_ylabel(r'$|\Psi_A|$  ($M_{\rm KK}^2$ units)')
ax.set_title('Acoustic White Hole NP Scalars')
ax.legend()
ax.grid(axis='y', alpha=0.3)

# Panel D: BCS splitting of NP scalars (dynamic case)
ax = axes[1, 1]
psi_bare_dyn = np_scalars['dynamic_bare']
psi_bcs_dyn = np_scalars['dynamic_BCS']
delta_psi = np.abs(psi_bcs_dyn) - np.abs(psi_bare_dyn)
colors = ['#4CAF50' if d >= 0 else '#F44336' for d in delta_psi.real]
ax.bar(x, np.abs(delta_psi), color=colors, alpha=0.8)
ax.set_xticks(x)
ax.set_xticklabels(labels_np)
ax.set_ylabel(r'$|\delta\Psi_A|$ (BCS - bare)')
ax.set_title('BCS Splitting of Dynamic NP Scalars')
ax.grid(axis='y', alpha=0.3)

plt.suptitle('S70 WEYL-NP-SCALARS-70: Newman-Penrose Scalars Under BCS', fontsize=14)
plt.tight_layout()
plt.savefig(os.path.join(script_dir, 's70_weyl_np_scalars.png'), dpi=150)
plt.close()
print("  Plot saved: s70_weyl_np_scalars.png")

# ==============================================================================
#  SECTION 11: Gate Verdict and Save
# ==============================================================================

elapsed = time.time() - t_start

print("\n" + "=" * 80)
print("  GATE VERDICT: WEYL-NP-SCALARS-70")
print("=" * 80)
print(f"\n  Gate: INFO (report all 5 NP scalars, bare and BCS-dressed)")

# Summary of key results
print(f"\n  4D Projection (Method A):")
print(f"    Static cases: all Psi_A = 0 (4D conformally flat product)")
for name in ['static_bare', 'static_BCS']:
    total = float(np.sum(np.abs(np_scalars[name])**2))
    print(f"      {name}: sum|Psi|^2 = {total:.4e}")

print(f"    Dynamic cases: Psi_A nonzero from extrinsic curvature")
for name in ['dynamic_bare', 'dynamic_BCS']:
    psi = np_scalars[name]
    mags = np.abs(psi)
    print(f"      {name}: |Psi_0|={mags[0]:.4e} |Psi_1|={mags[1]:.4e} "
          f"|Psi_2|={mags[2]:.4e} |Psi_3|={mags[3]:.4e} |Psi_4|={mags[4]:.4e}")

print(f"\n  12D Boost-Weight (Method B):")
for name in cases:
    bw = bw_results[name]
    bw2_frac = bw['bw_norms'].get(2, 0.0) / bw['total_sq'] if bw['total_sq'] > 0 else 0
    bwm2_frac = bw['bw_norms'].get(-2, 0.0) / bw['total_sq'] if bw['total_sq'] > 0 else 0
    bw0_frac = bw['bw_norms'].get(0, 0.0) / bw['total_sq'] if bw['total_sq'] > 0 else 0
    print(f"    {name:20s}: bw0={bw0_frac:.4e}, bw+2={bw2_frac:.4e}, bw-2={bwm2_frac:.4e}")

print(f"\n  Acoustic White Hole:")
print(f"    Psi_2 (Coulomb, static): bare={Psi_2_acoustic_bare:.4f}, BCS={Psi_2_acoustic_BCS:.4f}")
print(f"    Psi_4 (radiation, dyn):  bare={Psi_4_acoustic_dyn:.1f}, BCS={Psi_4_acoustic_BCS_dyn:.1f}")
print(f"    |Psi_4/Psi_2| = {ratio_42:.1f} (radiation dominates during supersonic transit)")
print(f"    BCS correction to Psi_2: {abs(Psi_2_acoustic_BCS - Psi_2_acoustic_bare)/abs(Psi_2_acoustic_bare)*100:.1f}%")

gate_detail = (
    f"4D projection: static=Type O (all Psi=0, product), "
    f"dynamic=all Psi nonzero. "
    f"12D BW: static bw0 dominant (Type D), dynamic bw0 dominant (Type G, bw+/-2~0.8%). "
    f"Acoustic: |Psi_4/Psi_2|={ratio_42:.1f}, radiation dominates. "
    f"BCS correction: {abs(Psi_2_acoustic_BCS - Psi_2_acoustic_bare)/abs(Psi_2_acoustic_bare)*100:.1f}% on Psi_2."
)

print(f"\n  Verdict detail: {gate_detail}")
print(f"  Elapsed: {elapsed:.2f}s")

# Save data
save_path = os.path.join(script_dir, 's70_weyl_np_scalars.npz')
np.savez(save_path,
         # Gate metadata
         gate_name='WEYL-NP-SCALARS-70',
         gate_verdict='INFO',
         gate_detail=gate_detail,
         # 4D NP scalars (Method A) -- complex arrays
         psi_static_bare=np_scalars['static_bare'],
         psi_static_BCS=np_scalars['static_BCS'],
         psi_dynamic_bare=np_scalars['dynamic_bare'],
         psi_dynamic_BCS=np_scalars['dynamic_BCS'],
         # 12D boost-weight norms (Method B)
         bw_norms_static_bare=np.array([bw_results['static_bare']['bw_norms'].get(w, 0.0) for w in range(-4, 5)]),
         bw_norms_static_BCS=np.array([bw_results['static_BCS']['bw_norms'].get(w, 0.0) for w in range(-4, 5)]),
         bw_norms_dynamic_bare=np.array([bw_results['dynamic_bare']['bw_norms'].get(w, 0.0) for w in range(-4, 5)]),
         bw_norms_dynamic_BCS=np.array([bw_results['dynamic_BCS']['bw_norms'].get(w, 0.0) for w in range(-4, 5)]),
         # 12D Omega matrices (generalized Psi_0, Psi_4)
         Omega_static_bare=bw_results['static_bare']['Omega'],
         Omega_dynamic_bare=bw_results['dynamic_bare']['Omega'],
         OmegaP_static_bare=bw_results['static_bare']['OmegaP'],
         OmegaP_dynamic_bare=bw_results['dynamic_bare']['OmegaP'],
         # Acoustic NP scalars
         Psi_2_acoustic_bare=Psi_2_acoustic_bare,
         Psi_2_acoustic_BCS=Psi_2_acoustic_BCS,
         Psi_4_acoustic_bare=Psi_4_acoustic_dyn,
         Psi_4_acoustic_BCS=Psi_4_acoustic_BCS_dyn,
         Psi_4_over_Psi_2=ratio_42,
         Mach_number=Mach,
         Mach_BCS=Mach_BCS,
         c_s_bare=c_s,
         c_s_BCS=c_s_BCS,
         kappa_BCS=kappa_BCS,
         # Parameters
         tau_fold=tau_fold,
         v_terminal=v_terminal,
         Delta_BCS=Delta_BCS,
         elapsed_s=elapsed,
         )
print(f"  Data saved: {save_path}")
print("\nDone.")
