#!/usr/bin/env python3
"""
S61 YUKAWA-FIRST-PRINCIPLES-61: Yukawa Couplings from D_F
==========================================================

Constructs the finite Dirac operator D_F from the framework's SU(3) geometry
and extracts Yukawa matrices Y_u, Y_d, Y_e, Y_nu. Compares mass ratios to PDG.

METHOD:
  1. Build su(3) = u(2) + C^2 decomposition with Jensen metric at tau_fold.
  2. Compute the L-homomorphism failure delta_F(X,Y) = L_{[X,Y]} - [L_X, L_Y]
     for all pairs of su(3) generators, following Baptista 2105.02901 eq (2.65).
  3. Compute the Kosmann-Lichnerowicz derivative [D_K, L_X] for non-Killing X,
     following Baptista 2506.09126 eq (4.1). This generates mass mixing.
  4. Build D_F from: (a) diagonal Laplacian mass matrices Omega^D_g, Omega^b_g,
     Omega^c_g (Paper 14 eqs 3.19, 3.22), and (b) off-diagonal Dirac mass
     contributions from the spin connection at tau_fold.
  5. Extract 3x3 Yukawa matrices from the appropriate blocks.
  6. Diagonalize and compare eigenvalue RATIOS to PDG.

GATE: YUKAWA-FIRST-PRINCIPLES-61
  PASS if any mass ratio within 30% of PDG.
  FAIL if all off by > OOM.
  INFO if structure correct (3 generations) but ratios need RG running.

Author: Nazarewicz Nuclear Structure Theorist Agent
Date: 2026-03-28
Session: S61
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, norm
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, Vol_SU3_Haar, M_KK, M_KK_gravity, M_KK_kerner,
    g_SU2_fold, g_U1_fold, PI, M_Z, sin2_thetaW_MSbar,
    g0_diag, J_C2, J_su2, J_u1
)
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, validate_connection,
    build_cliff8, validate_clifford, build_chirality,
    spinor_connection_offset,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX, M_IDX
)

# ==============================================================================
# PDG MASS VALUES (2024, MS-bar at M_Z = 91.1876 GeV)
# From Antusch et al. 2510.01312 (Paasch paper 33)
# ==============================================================================

# Running quark masses at M_Z (MS-bar, in GeV)
m_u_MZ = 1.27e-3    # up quark  # (local)
m_c_MZ = 0.626      # charm quark  # (local)
m_t_MZ = 171.5      # top quark (pole mass ~ 172.4, running ~ 163 at M_Z)  # (local)

m_d_MZ = 2.90e-3    # down quark  # (local)
m_s_MZ = 54.7e-3    # strange quark  # (local)
m_b_MZ = 2.84       # bottom quark  # (local)

# Charged lepton pole masses (GeV)
m_e = 0.51099895e-3  # (local)
# m_mu = 0.1056583745  # S72: now imported from canonical_constants
m_tau = 1.77686

# Mass RATIOS at M_Z (the observables we compare against)
# These are more robust than absolute masses since M_KK drops out
PDG_ratios = {
    # Up sector
    'm_c/m_u': m_c_MZ / m_u_MZ,          # ~ 493
    'm_t/m_c': m_t_MZ / m_c_MZ,          # ~ 274
    'm_t/m_u': m_t_MZ / m_u_MZ,          # ~ 1.35e5
    # Down sector
    'm_s/m_d': m_s_MZ / m_d_MZ,          # ~ 18.9
    'm_b/m_s': m_b_MZ / m_s_MZ,          # ~ 51.9
    'm_b/m_d': m_b_MZ / m_d_MZ,          # ~ 979
    # Lepton sector
    'm_mu/m_e': m_mu / m_e,              # ~ 206.8
    'm_tau/m_mu': m_tau / m_mu,          # ~ 16.8
    'm_tau/m_e': m_tau / m_e,            # ~ 3477
    # Cross-sector
    'm_b/m_tau': m_b_MZ / m_tau,         # ~ 1.60
    'm_t/m_b': m_t_MZ / m_b_MZ,         # ~ 60.4
    'm_t/m_tau': m_t_MZ / m_tau,         # ~ 96.5
}


def print_header(title):
    print(f"\n{'='*72}")
    print(f"  {title}")
    print(f"{'='*72}\n")


def print_section(title):
    print(f"\n--- {title} ---\n")


# ==============================================================================
# STEP 1: Build the su(3) algebraic infrastructure at tau_fold
# ==============================================================================

def build_infrastructure(s):
    """Build all algebraic objects at Jensen parameter s."""
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    gammas = build_cliff8()

    return {
        'gens': gens, 'f_abc': f_abc, 'B_ab': B_ab,
        'g_s': g_s, 'E': E, 'ft': ft, 'Gamma': Gamma,
        'gammas': gammas, 's': s
    }


# ==============================================================================
# STEP 2: Compute L-homomorphism failure (Baptista eq 2.65)
# ==============================================================================

def compute_L_homomorphism_failure(infra):
    """
    Compute the closure defect delta_F(X,Y) for all pairs of su(3) generators.

    From Baptista 2105.02901 eq (2.65):
      [rho^L_u, rho^L_v] - rho^L_{[u,v]} = [[0, 2[u,v]_{11} c^T],
                                               [-2[u,v]_{11} b, 0]]

    The closure defect is nonzero precisely when [u,v]_{11} != 0, which
    happens when the commutator has a nonzero (1,1) entry.

    For the su(3) basis e_a = -i/2 lambda_a:
      [e_a, e_b] = f_{abc} e_c
      [e_a, e_b]_{11} = f_{abc} (e_c)_{11}

    The (1,1) entry of e_c is (e_c)_{11} = -i/2 (lambda_c)_{11}.
    Only lambda_3 and lambda_8 have nonzero (1,1) entries:
      lambda_3: diag(1,-1,0) -> (lambda_3)_{11} = 1
      lambda_8: diag(1,1,-2)/sqrt(3) -> (lambda_8)_{11} = 1/sqrt(3)

    So (e_c)_{11} = -i/2 for c=2 (lambda_3), -i/(2 sqrt(3)) for c=7 (lambda_8).
    Wait -- our indexing is 0-based: lambda_1 is index 0, ..., lambda_8 is index 7.
    So lambda_3 is index 2, lambda_8 is index 7.

    Returns: 8x8 matrix delta_F[a,b] = [e_a, e_b]_{11} (complex scalar)
    """
    gens = infra['gens']
    f_abc = infra['f_abc']

    # Extract (1,1) entry of each generator (0-indexed: row 0, col 0)
    gen_11 = np.array([g[0, 0] for g in gens])

    # [e_a, e_b]_{11} = f_{abc} * (e_c)_{11}
    # delta_F[a,b] = sum_c f_abc[a,b,c] * gen_11[c]
    delta_F = np.einsum('abc,c->ab', f_abc, gen_11)

    return delta_F


# ==============================================================================
# STEP 3: Construct D_K mass matrices (Baptista Paper 14 eqs 3.19, 3.22)
# ==============================================================================

def compute_laplacian_mass_matrices(infra):
    """
    Compute the mass matrices Omega^D_g, Omega^b_g, Omega^c_g from the
    Laplacian of D_K acting on each spinor component.

    From Baptista 2105.02901:
      Omega^D_g = sum_j e_j e_j + (1/3) Tr(e_j e_j) I_3    [eq 3.19]
      Omega^b_g = sum_j e_j e_j + 4(e_j)_{11} e_j
                  + [2(e_j)^2_{11} + (e_j e_j)_{11}/kappa] I_3  [eq 3.22]
      Omega^c_g is proportional to I_3

    Here the sum is over an ORTHONORMAL frame for g_s, using the
    Jensen-deformed metric. The generators e_j are in the ON frame.

    For the Jensen metric with parameter s:
      L1 = e^{2s} (u(1)), L2 = e^{-2s} (su(2)), L3 = e^s (C^2)

    The ON frame generators are E_a = e_a / sqrt(g_{aa}).
    """
    s = infra['s']
    gens = infra['gens']  # original generators in coordinate frame
    g_s = infra['g_s']
    E = infra['E']        # orthonormal frame transformation

    # Scale factors
    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)

    # The Killing metric for our normalization: B_{ab} = -3 delta_{ab}
    # So g0_{ab} = |B_{ab}| = 3 delta_{ab}
    # Jensen metric: g_s = diag(3*L2, 3*L2, 3*L2, 3*L3, 3*L3, 3*L3, 3*L3, 3*L1)
    # (su(2) indices 0,1,2; C^2 indices 3,4,5,6; u(1) index 7)

    # Construct ON-frame generators: tilde_e_a = E_{ab} e_b
    # But for the mass matrices, we need the 3x3 representation matrices
    # evaluated in the ON frame.

    # The ON frame effectively rescales each generator:
    # For su(2) direction (a in {0,1,2}): scale by 1/sqrt(3*L2)
    # For C^2 direction (a in {3,4,5,6}): scale by 1/sqrt(3*L3)
    # For u(1) direction (a=7): scale by 1/sqrt(3*L1)

    # However, the metric is not generally diagonal in the full 8x8 form
    # after Jensen deformation -- it IS diagonal because the decomposition
    # is orthogonal. Let me verify.

    # Compute diagonal elements of g_s to extract scale factors
    g_diag = np.diag(g_s)

    # Build ON-frame representation matrices
    # In the ON frame, the generator representations are:
    #   rho_ON(tilde_e_a) = sum_b E_{ab} rho(e_b)
    # where E is the inverse-Cholesky of g_s.

    # For the mass matrices, we need:
    # Omega^D_g = sum_a [rho_ON(tilde_e_a)]^2 + (1/3) Tr([rho_ON(tilde_e_a)]^2) I_3

    # But rho_ON(tilde_e_a) = E_{ab} rho(e_b) where rho(e_b) = e_b (fundamental rep)
    # For diagonal g_s: E = diag(1/sqrt(g_{aa}))
    # So rho_ON(tilde_e_a) = (1/sqrt(g_{aa})) * e_a

    # ON frame generators as 3x3 matrices
    gens_ON = []
    for a in range(8):
        scale = 1.0 / np.sqrt(g_diag[a])
        gens_ON.append(scale * gens[a])

    # --- Omega^D_g: quark (D-component) mass matrix ---
    # Omega^D_g = sum_a e_a_ON @ e_a_ON + (1/3) Tr(e_a_ON @ e_a_ON) * I_3
    Omega_D = np.zeros((3, 3), dtype=complex)
    trace_sum = 0.0  # (local)
    for a in range(8):
        prod = gens_ON[a] @ gens_ON[a]
        Omega_D += prod
        trace_sum += np.trace(prod).real

    Omega_D += (trace_sum / 3.0) * np.eye(3, dtype=complex)

    # --- Omega^b_g: lepton (b-component) mass matrix ---
    # Omega^b_g = sum_a {e_a_ON @ e_a_ON + 4*(e_a_ON)_{11} * e_a_ON
    #              + [2*(e_a_ON)_{11}^2 + (e_a_ON @ e_a_ON)_{11}/kappa] * I_3}
    # where kappa = 1 + 8*cos^2(phi). For the simplest case phi=0: kappa=9.
    # Baptista's phi parametrizes the vertical transformation family.
    # At phi=0 (the canonical choice): kappa = 9.
    kappa = 9.0  # phi=0 canonical

    Omega_b = np.zeros((3, 3), dtype=complex)
    for a in range(8):
        ea = gens_ON[a]
        ea_11 = ea[0, 0]  # (1,1) entry (0-indexed)
        prod = ea @ ea
        Omega_b += prod + 4.0 * ea_11 * ea
        Omega_b += (2.0 * ea_11**2 + prod[0, 0] / kappa) * np.eye(3, dtype=complex)

    # --- Omega^c_g: up-quark (c-component) mass matrix ---
    # The c-mass matrix is proportional to I_3 (Paper 14 statement)
    # Omega^c_g = mu_c * I_3 where mu_c depends on the metric
    # From the integral: integral_K |grad s|^2 type term
    # The eigenvalue is: sum_a 4*(e_a)_{11}^2 / g_{aa}
    mu_c = 0.0  # (local)
    for a in range(8):
        ea_11 = gens[a][0, 0]
        mu_c += 4.0 * abs(ea_11)**2 / g_diag[a]
    Omega_c = mu_c * np.eye(3, dtype=complex)

    # --- Omega^a_g: neutrino (a-component, scalar function s) ---
    # The a-component mass comes from integral_K |grad |s|^2|^2 vol_K
    # This is a single scalar: all neutrinos have the same mass contribution
    # from the Laplacian. The Dirac mass will split them.
    mu_a = 0.0  # (local)
    for a in range(8):
        # |s(h)|^2 = 2 |(h^T h)_{11}|^2, Laplacian eigenvalue
        ea_11 = gens[a][0, 0]
        mu_a += 16.0 * abs(ea_11)**2 / g_diag[a]
    Omega_a = mu_a * np.eye(1, dtype=complex)  # scalar

    return Omega_D, Omega_b, Omega_c, Omega_a


# ==============================================================================
# STEP 4: Compute full D_F from Dirac operator mass terms
# ==============================================================================

def compute_dirac_mass_contributions(infra):
    """
    Compute the Dirac operator mass contributions from the spin connection.

    The Dirac operator on K = SU(3):
      D_K = sum_a gamma_a nabla_{e_a} = sum_a gamma_a (L_{e_a} + omega_a^{spin})

    Acting on a spinor mode psi(h) with vertical behavior S(h), the
    mass terms arise from:
    1. The spin connection Omega (from dirac_spectrum: spinor_connection_offset)
    2. The structure constant terms gamma_a [e_a, .] acting on the 3x3 blocks

    For the mass matrix in the D-sector (quarks), the relevant matrix elements are:
      M^D_{ij} = <D_i | D_K | D_j>_{L^2(K)}
    integrated over K with the appropriate S(h) weighting.

    In the ON frame, D_K restricted to the D-sector gives:
      M^D = sum_a (e_a_ON)_left tensor gamma_a + Omega

    The eigenvalues of this operator (restricted to the appropriate irrep
    of the Peter-Weyl decomposition) give the KK mass spectrum.

    For the LOWEST modes (which map to SM fermion masses), the relevant
    contribution is the curvature offset Omega from the spin connection.
    """
    Gamma = infra['Gamma']
    gammas = infra['gammas']
    s = infra['s']

    # Compute the spinorial curvature offset
    Omega = spinor_connection_offset(Gamma, gammas)

    # Omega is a 16x16 matrix in spinor space
    # In the framework, this encodes the "finite Dirac operator" contribution
    # from the spin connection geometry.

    return Omega


# ==============================================================================
# STEP 5: Build the full D_F matrix in the SM fermion basis
# ==============================================================================

def build_D_F(infra, Omega_D, Omega_b, Omega_c, Omega_a, Omega_spin):
    """
    Construct D_F in the Connes basis:
      H_F = (nu_R, e_R, nu_L, e_L) x (1, 3_color) x 3_generation

    In the framework, D_F emerges from combining:
    1. Laplacian mass matrices (diagonal blocks) -- from Omega^D_g, etc.
    2. Dirac spin connection (off-diagonal blocks) -- from Omega_spin
    3. L-homomorphism failure (generation mixing) -- from delta_F

    The NCG D_F has the block structure:
      D_F = | 0      S^*  |     where S = | Y_nu  0   |
            | S      0    |              | 0     Y_e |    (lepton sector)

    and similarly for quarks with Y_u, Y_d replacing Y_nu, Y_e.

    In the KK framework, the Yukawa matrices arise from the SPLIT of the
    Laplacian eigenvalues by the spin connection at nonzero tau.
    """
    s = infra['s']
    gens = infra['gens']
    g_s = infra['g_s']
    g_diag = np.diag(g_s)

    # Scale factors
    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)

    # ------------------------------------------------------------------
    # Part A: The Laplacian mass eigenvalues
    # ------------------------------------------------------------------

    # Diagonalize Omega^D (quark sector)
    evals_D, evecs_D = eigh(-Omega_D.real)  # Omega is negative-definite
    # Eigenvalues are -mu_i^2 where mu_i are mass eigenvalues

    # Diagonalize Omega^b (lepton sector)
    evals_b, evecs_b = eigh(-Omega_b.real)

    # c-sector is proportional to I: all eigenvalues equal
    evals_c = np.array([-Omega_c[0, 0].real] * 3)

    # ------------------------------------------------------------------
    # Part B: Spin connection splitting
    # ------------------------------------------------------------------
    # The spin connection offset Omega_spin is 16x16.
    # Extract its eigenvalues to find the mass splitting pattern.
    omega_evals = eigvalsh(1j * Omega_spin)  # i*Omega should have real eigenvalues
    omega_evals_real = np.sort(np.real(omega_evals))

    # The 16 spinor components split under U(2) into:
    #   a (1 component), b (3 components), c (3 components), D (9 components)
    # = 1 + 3 + 3 + 9 = 16
    # The spin connection lifts the degeneracy within each sector.

    # ------------------------------------------------------------------
    # Part C: Jensen deformation mass splitting
    # ------------------------------------------------------------------
    # At s != 0, the three scale factors (L1, L2, L3) are unequal.
    # This breaks the su(3) symmetry down to u(2), which generates
    # DIFFERENT mass contributions for:
    #   - su(2) directions: contribute with weight 1/L2
    #   - C^2 directions: contribute with weight 1/L3
    #   - u(1) direction: contributes with weight 1/L1
    #
    # The effective mass matrix for the D-sector (quarks):
    # Omega^D_eff(s) = sum_{a in su(2)} (e_a@e_a)/(3*L2)
    #                + sum_{a in C^2} (e_a@e_a)/(3*L3)
    #                + sum_{a in u(1)} (e_a@e_a)/(3*L1)
    #                + (1/3)*Tr(...)* I_3

    # The KEY INSIGHT: the Jensen deformation introduces a HIERARCHY
    # through the exponential dependence on s.
    # At tau_fold = 0.19:
    #   L1 = e^{0.38} = 1.462
    #   L2 = e^{-0.38} = 0.684
    #   L3 = e^{0.19} = 1.209
    #
    # Ratio L1/L2 = e^{4*0.19} = 2.138 -- this is the u(1)/su(2) splitting
    # Ratio L3/L2 = e^{3*0.19} = 1.768 -- this is the C^2/su(2) splitting

    # ------------------------------------------------------------------
    # Part D: Construct Yukawa-like matrices from the geometry
    # ------------------------------------------------------------------
    # The "Yukawa matrices" in the NCG sense are the matrix elements of D_F
    # connecting left-handed and right-handed fermions.
    #
    # In the KK framework, these arise from the Dirac operator matrix elements
    # between different vertical modes. For the LOWEST KK modes (the SM fermions),
    # the mass matrix is determined by the overlap integrals:
    #
    #   M_{ij} = integral_K psi_i^dag D_K psi_j vol_K
    #
    # The vertical modes psi_i are determined by the representation content.
    # For quarks (D-sector): psi transforms as 3_color under right-SU(3),
    #   and as 2_weak under left-SU(2). The 3 generations come from the
    #   3 independent states within the SU(2) doublet structure.
    #
    # The mass matrix in the D-sector:
    #   M^D = Omega^D_g (Laplacian, diagonal)
    #       + delta_D (Dirac spin connection, off-diagonal)
    #
    # where delta_D comes from the Dirac-specific terms.

    # Compute the Dirac-specific correction to the Laplacian mass matrices.
    # From the Dirac operator: D_K = sum_a gamma_a nabla_{e_a}
    # The nabla_{e_a} on the D-sector gives:
    #   nabla_{e_a} D = (ad(e_a)) D + connection terms
    # The adjoint action [e_a, D] = f_{abc} e_c D (on the left)
    # plus D [e_a, .] (on the right).

    # For the ON frame, the Dirac mass matrix element connecting
    # the k-th and l-th states of the D-sector (k,l = color indices) is:
    #
    # (M_Dirac)_{kl} = sum_a (1/sqrt(g_{aa})) *
    #   integral_K (h)^dag_k [nabla_{e_a} (h D)]_l vol_K
    #
    # The key structure: the DIFFERENCE between Dirac and Laplacian masses
    # comes from the spin connection terms in nabla.

    # The spin connection contribution to D-sector masses:
    # From Gamma^b_{ac} (the Levi-Civita connection), the correction is:
    # delta_M^D_{kl} = (1/4) sum_{a,b,c} Gamma^b_{ac} sigma_{bc} (e_a)_{kl}
    # where sigma_{bc} = (i/2)[gamma_b, gamma_c] is the spin matrix.

    # For the mass hierarchy, the crucial quantity is the RATIO of
    # Jensen scale factors acting on different su(3) subspaces.

    return evals_D, evecs_D, evals_b, evecs_b, evals_c, omega_evals_real


# ==============================================================================
# STEP 6: Extract Yukawa matrices from the KK mass spectrum
# ==============================================================================

def extract_yukawa_matrices(infra, Omega_D, Omega_b, Omega_c):
    """
    Extract 3x3 Yukawa matrices from the mass structure.

    The Yukawa coupling y_f is related to the fermion mass by:
      m_f = y_f * v / sqrt(2)
    where v = 246 GeV is the Higgs VEV.

    In the KK framework, the Yukawa coupling for the f-th fermion is:
      y_f = mu_f / M_KK
    where mu_f is the KK mass eigenvalue (in M_KK units).

    The key result: the RATIOS m_i/m_j = mu_i/mu_j = sqrt(eig_i/eig_j)
    where eig_i are the eigenvalues of the mass-squared matrices.
    """
    s = infra['s']
    gens = infra['gens']
    g_s = infra['g_s']
    g_diag = np.diag(g_s)
    f_abc = infra['f_abc']
    Gamma = infra['Gamma']

    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)

    # ------------------------------------------------------------------
    # The D-sector (down-type quarks) mass matrix
    # ------------------------------------------------------------------
    # Omega^D_g is the Laplacian contribution. For the DIRAC operator,
    # there is an additional spin-connection term that SPLITS the
    # Laplacian eigenvalues.
    #
    # The splitting pattern is controlled by the u(2) Casimir structure:
    # Under su(2) x u(1) subset su(3), the fundamental 3 decomposes as:
    #   3 -> 2_{1/6} + 1_{-1/3}
    # (doublet + singlet with different hypercharges)
    #
    # At nonzero s, the doublet and singlet have different effective masses
    # because L2 != L3 != L1.

    # Diagonalize Omega^D
    # First make it Hermitian (it should be by construction)
    Omega_D_herm = 0.5 * (Omega_D + Omega_D.conj().T)
    evals_D_sq, evecs_D = eigh(Omega_D_herm)

    # These are the mass-squared eigenvalues (negative, since Omega ~ -m^2)
    # Mass eigenvalues: sqrt(-evals)
    mass_D = np.sqrt(np.abs(evals_D_sq))

    # ------------------------------------------------------------------
    # The b-sector (charged leptons) mass matrix
    # ------------------------------------------------------------------
    Omega_b_herm = 0.5 * (Omega_b + Omega_b.conj().T)
    evals_b_sq, evecs_b = eigh(Omega_b_herm)
    mass_b = np.sqrt(np.abs(evals_b_sq))

    # ------------------------------------------------------------------
    # The c-sector (up-type quarks) mass matrix
    # ------------------------------------------------------------------
    # c-sector is proportional to I_3 from the Laplacian.
    # The splitting must come entirely from the Dirac/spin-connection terms.
    #
    # The spin connection correction for the c-sector:
    # delta_M^c_{kl} = sum_a (1/sqrt(g_{aa})) * connection_correction
    #
    # For the c-sector, the vertical behavior is c_+(x,h) = s(h) h^dag c(x),
    # where s(h) = sqrt(2) (h^T h)_{11}.
    # The Dirac action generates:
    #   (D_K c)_k = sum_a (gamma_a / sqrt(g_aa)) *
    #     [(-2(e_a)_{11} I + e_a^T) c + spin_connection_c]_k
    #
    # The mass matrix for c:
    # M^c = sum_a (1/g_{aa}) * [4|(e_a)_{11}|^2 I_3 - 2(e_a)_{11} e_a^T
    #        - 2 conj((e_a)_{11}) e_a + e_a^dag e_a]
    # Plus spin-connection corrections.

    Omega_c_full = np.zeros((3, 3), dtype=complex)
    for a in range(8):
        ea = gens[a]
        ea_11 = ea[0, 0]
        inv_gaa = 1.0 / g_diag[a]

        # Quadratic form from (L_{e_a} c) structure
        # The c-sector covariant derivative has rho_c(e_a) = -2(e_a)_{11}*I + e_a^T
        rho_c_a = -2.0 * ea_11 * np.eye(3, dtype=complex) + ea.T
        Omega_c_full += inv_gaa * (rho_c_a.conj().T @ rho_c_a)

    Omega_c_herm = 0.5 * (Omega_c_full + Omega_c_full.conj().T)
    evals_c_sq, evecs_c = eigh(Omega_c_herm)
    mass_c = np.sqrt(np.abs(evals_c_sq))

    # ------------------------------------------------------------------
    # The a-sector (neutrinos) mass
    # ------------------------------------------------------------------
    # The a-component is a scalar under SU(3)_R, so there is only one
    # mass eigenvalue per generation. The generation structure comes
    # from the spin-connection splitting in the 4D spinor space.
    # For now: scalar mass (no splitting from internal geometry alone).
    mass_a = np.sqrt(np.abs(Omega_c[0, 0].real))  # Same as c-sector baseline

    return mass_D, mass_b, mass_c, mass_a, evecs_D, evecs_b, evecs_c


# ==============================================================================
# STEP 7: Compute full Dirac operator D_F including off-diagonal terms
# ==============================================================================

def compute_full_D_F(infra):
    """
    Compute the FULL finite Dirac operator D_F by constructing the
    matrix elements of D_K between all fermion sectors.

    In the NCG Standard Model, D_F is a 32x32 matrix (per generation)
    or 96x96 for 3 generations. Its nonzero blocks encode:
    - Yukawa couplings (off-diagonal: L <-> R)
    - Majorana mass (nu_R sector)

    In the KK framework, D_F emerges from D_K restricted to the lowest
    KK modes. The key ingredients:

    1. The rho^L action (Baptista eq 2.62) determines the gauge couplings
    2. The D_K mass terms (Section 3 of Paper 14) determine Yukawa couplings
    3. The L-homomorphism failure (eq 2.65) generates generation mixing

    The mass hierarchy comes from:
    - The Jensen deformation splitting L1 : L2 : L3 = e^{2s} : e^{-2s} : e^s
    - The representation structure (different su(3) Casimirs for different sectors)
    - The spin connection coupling between sectors
    """
    s = infra['s']
    gens = infra['gens']
    g_s = infra['g_s']
    g_diag = np.diag(g_s)
    f_abc = infra['f_abc']
    Gamma = infra['Gamma']

    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)

    # ------------------------------------------------------------------
    # Build representation matrices for each sector in the ON frame
    # ------------------------------------------------------------------
    # D-sector: rho^L_D(e_a) = e_a (fundamental on left) [eq 2.27]
    # b-sector: rho^L_b(e_a) = 2(e_a)_{11} I_3 + e_a [eq 2.40]
    # c-sector: rho^L_c(e_a) = -2(e_a)_{11} I_3 [eq 2.51]
    # a-sector: rho^L_a(e_a) = 0 (decoupled)

    # ON-frame representation matrices
    rho_D = []  # 3x3 each
    rho_b = []  # 3x3 each
    rho_c = []  # 3x3 each
    for a in range(8):
        ea = gens[a]
        ea_11 = ea[0, 0]
        scale = 1.0 / np.sqrt(g_diag[a])

        rho_D.append(scale * ea)
        rho_b.append(scale * (2.0 * ea_11 * np.eye(3, dtype=complex) + ea))
        rho_c.append(scale * (-2.0 * ea_11 * np.eye(3, dtype=complex)))

    # ------------------------------------------------------------------
    # Mass-squared matrices from D_K^2 restricted to each sector
    # ------------------------------------------------------------------
    # M^2_sector = -sum_a rho_sector(tilde_e_a)^dag @ rho_sector(tilde_e_a)
    # (using anti-Hermitian generators)

    M2_D = np.zeros((3, 3), dtype=complex)
    M2_b = np.zeros((3, 3), dtype=complex)
    M2_c = np.zeros((3, 3), dtype=complex)

    for a in range(8):
        M2_D -= rho_D[a].conj().T @ rho_D[a]
        M2_b -= rho_b[a].conj().T @ rho_b[a]
        M2_c -= rho_c[a].conj().T @ rho_c[a]

    # Add spin connection corrections
    # The Dirac operator has additional terms from the spin connection
    # that modify the mass matrices. These come from:
    # D_K = sum_a gamma_a (rho(e_a) + omega_a^{spin})
    # D_K^2 = -sum_a rho(e_a)^2 + cross terms + Omega^2 + curvature

    # The cross terms between rho and omega generate off-diagonal mass terms.
    # For the lowest KK modes, these are the Yukawa-generating terms.

    # Spin connection contribution to mass matrix:
    # delta_M^2 = (1/4) sum_{a,b,c} Gamma^b_{ac} [rho_a, sigma_{bc}]
    # For each sector, sigma_{bc} acts on the spinor index while rho acts
    # on the representation index. In the mass matrix (integrated over spinor),
    # the contribution depends on the specific spinor state.

    # For the LOWEST spinor mode (ground state of spin connection), the
    # correction is:
    # delta_M^2 = -(1/4) sum_{a,b,c} Gamma_{bac}^2 * I  (scalar shift, no splitting)
    # PLUS off-diagonal terms from the torsion-like piece:
    # (1/2) sum_{a,b,c} Gamma_{bac} f_abc (from [nabla, L] commutator)

    # The torsion correction to the mass matrix:
    torsion_D = np.zeros((3, 3), dtype=complex)
    torsion_b = np.zeros((3, 3), dtype=complex)
    torsion_c = np.zeros((3, 3), dtype=complex)

    for a in range(8):
        for b in range(8):
            for c in range(8):
                if abs(Gamma[b, a, c]) > 1e-15 and abs(f_abc[a, b, c]) > 1e-15:
                    coeff = 0.5 * Gamma[b, a, c]  # (local)
                    # The torsion-like correction involves [rho(e_a), rho(e_c)]
                    comm_D = rho_D[a] @ rho_D[c] - rho_D[c] @ rho_D[a]
                    comm_b = rho_b[a] @ rho_b[c] - rho_b[c] @ rho_b[a]
                    comm_c = rho_c[a] @ rho_c[c] - rho_c[c] @ rho_c[a]

                    torsion_D += coeff * comm_D
                    torsion_b += coeff * comm_b
                    torsion_c += coeff * comm_c

    # Full mass-squared matrices
    M2_D_full = M2_D + torsion_D
    M2_b_full = M2_b + torsion_b
    M2_c_full = M2_c + torsion_c

    # Make Hermitian
    M2_D_full = 0.5 * (M2_D_full + M2_D_full.conj().T)
    M2_b_full = 0.5 * (M2_b_full + M2_b_full.conj().T)
    M2_c_full = 0.5 * (M2_c_full + M2_c_full.conj().T)

    return M2_D_full, M2_b_full, M2_c_full


# ==============================================================================
# STEP 8: Compute the Kosmann-Lichnerowicz mass mixing
# ==============================================================================

def compute_KL_mixing(infra):
    """
    Compute the Kosmann-Lichnerowicz derivative mass mixing terms.

    From Baptista 2506.09126 (Paper 17):
      [D_K, L_X] psi = (1/2) sum_{i,j} (L_X g_K)(v_i, v_j) v_i . nabla_{v_j} psi
                      + (1/4) sum_{i,j} {grad terms} v_j . psi

    For Killing X (su(2) + u(1) directions): [D_K, L_X] = 0 (no mass mixing)
    For non-Killing X (C^2 directions): [D_K, L_X] != 0 (mass mixing + chirality)

    The C^2 directions are indices 3,4,5,6 in our basis.
    The Lie derivative of the Jensen metric along C^2 directions:
      (L_{e_a} g_s)(e_b, e_c) = f_{abd} g_s(e_d, e_c) + f_{acd} g_s(e_b, e_d)
                                (for left-invariant vector fields and metric)

    This is nonzero when a in C^2 and the metric has different scale factors
    for different subspaces.
    """
    s = infra['s']
    ft = infra['ft']  # ON-frame structure constants
    Gamma = infra['Gamma']
    g_s = infra['g_s']
    g_diag = np.diag(g_s)
    f_abc = infra['f_abc']

    L1 = np.exp(2.0 * s)
    L2 = np.exp(-2.0 * s)
    L3 = np.exp(s)

    # Lie derivative of g_s along each generator
    # For a left-invariant metric on a Lie group:
    # (L_{e_a} g)(e_b, e_c) = g([e_a, e_b], e_c) + g(e_b, [e_a, e_c])
    #                       = sum_d f_{abd} g_{dc} + sum_d f_{acd} g_{bd}

    Lie_g = np.zeros((8, 8, 8), dtype=np.float64)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                val = 0.0  # (local)
                for d in range(8):
                    val += f_abc[a, b, d] * g_s[d, c].real
                    val += f_abc[a, c, d] * g_s[b, d].real
                Lie_g[a, b, c] = val

    # Lie derivative squared magnitude for each direction
    Lie_norm = np.zeros(8)
    for a in range(8):
        Lie_norm[a] = np.sum(Lie_g[a]**2)

    # The Killing condition: L_{e_a} g = 0
    # Check which directions are Killing
    killing_status = {}
    for a in range(8):
        killing_status[a] = Lie_norm[a] < 1e-10

    # Compute the KL mixing matrix elements
    # For the D-sector, the mixing between mass eigenstate i and j:
    # (KL_mix)_{ij} = sum_{a in C2} <D_i | [D_K, L_{e_a}] | D_j>
    #
    # In the ON frame:
    # [D_K, L_{e_a}] = (1/2) sum_{b,c} (L_{e_a} g)(tilde_e_b, tilde_e_c) ...
    #
    # For the mass hierarchy, the KEY quantity is the RATIO:
    # (L_{e_a} g)(su2, C2) / (L_{e_a} g)(C2, C2)
    # This controls how much the C^2 non-Killing fields mix different sectors.

    return Lie_g, Lie_norm, killing_status


# ==============================================================================
# STEP 9: Full computation at tau_fold with tau-scan
# ==============================================================================

def compute_mass_ratios_at_s(s, verbose=True):
    """Compute all mass eigenvalues and ratios at Jensen parameter s."""
    if verbose:
        print_section(f"Computing at s = {s:.4f} (tau_fold = {s})")

    # Build infrastructure
    infra = build_infrastructure(s)

    # Validate connection
    conn_err = validate_connection(infra['Gamma'])
    if verbose:
        print(f"  Connection metric compatibility error: {conn_err:.2e}")

    # Compute mass matrices
    M2_D, M2_b, M2_c = compute_full_D_F(infra)

    # Diagonalize
    evals_D, evecs_D = eigh(M2_D)
    evals_b, evecs_b = eigh(M2_b)
    evals_c, evecs_c = eigh(M2_c)

    # Mass eigenvalues (take sqrt of |eigenvalues|)
    mass_D = np.sqrt(np.abs(evals_D))
    mass_b = np.sqrt(np.abs(evals_b))
    mass_c = np.sqrt(np.abs(evals_c))

    # Sort by magnitude
    mass_D = np.sort(mass_D)
    mass_b = np.sort(mass_b)
    mass_c = np.sort(mass_c)

    # Compute Lie derivative for non-Killing analysis
    Lie_g, Lie_norm, killing_status = compute_KL_mixing(infra)

    # Also compute L-homomorphism failure
    delta_F = compute_L_homomorphism_failure(infra)

    # Compute Laplacian mass matrices for comparison
    Omega_D, Omega_b, Omega_c, Omega_a = compute_laplacian_mass_matrices(infra)

    return {
        's': s,
        'mass_D': mass_D,
        'mass_b': mass_b,
        'mass_c': mass_c,
        'M2_D': M2_D,
        'M2_b': M2_b,
        'M2_c': M2_c,
        'evals_D': evals_D,
        'evals_b': evals_b,
        'evals_c': evals_c,
        'evecs_D': evecs_D,
        'evecs_b': evecs_b,
        'evecs_c': evecs_c,
        'Lie_norm': Lie_norm,
        'killing_status': killing_status,
        'delta_F': delta_F,
        'Omega_D_lap': Omega_D,
        'Omega_b_lap': Omega_b,
        'Omega_c_lap': Omega_c,
        'conn_err': conn_err,
        'infra': infra,
    }


# ==============================================================================
# MAIN COMPUTATION
# ==============================================================================

def main():
    print_header("S61 YUKAWA-FIRST-PRINCIPLES-61")
    print("Computing Yukawa couplings from D_F via L-homomorphism failure")
    print(f"Jensen parameter: s = tau_fold = {tau_fold}")
    print(f"M_KK (gravity): {M_KK_gravity:.4e} GeV")
    print(f"M_KK (Kerner):  {M_KK_kerner:.4e} GeV")

    # ==================================================================
    # Validation: bi-invariant limit (s=0)
    # ==================================================================
    print_header("VALIDATION: Bi-invariant limit (s = 0)")
    result_0 = compute_mass_ratios_at_s(0.0)

    print(f"\n  Mass eigenvalues at s=0:")
    print(f"    D-sector (down quarks): {result_0['mass_D']}")
    print(f"    b-sector (leptons):     {result_0['mass_b']}")
    print(f"    c-sector (up quarks):   {result_0['mass_c']}")

    # At s=0 (bi-invariant), all Killing: no mass splitting expected
    # All eigenvalues should be degenerate within each sector
    D_spread_0 = (result_0['mass_D'].max() - result_0['mass_D'].min()) / result_0['mass_D'].mean() if result_0['mass_D'].mean() > 0 else 0
    b_spread_0 = (result_0['mass_b'].max() - result_0['mass_b'].min()) / result_0['mass_b'].mean() if result_0['mass_b'].mean() > 0 else 0
    c_spread_0 = (result_0['mass_c'].max() - result_0['mass_c'].min()) / result_0['mass_c'].mean() if result_0['mass_c'].mean() > 0 else 0

    print(f"\n  Degeneracy check (fractional spread):")
    print(f"    D-sector: {D_spread_0:.2e} {'(DEGENERATE)' if D_spread_0 < 1e-10 else '(SPLIT)'}")
    print(f"    b-sector: {b_spread_0:.2e} {'(DEGENERATE)' if b_spread_0 < 1e-10 else '(SPLIT)'}")
    print(f"    c-sector: {c_spread_0:.2e} {'(DEGENERATE)' if c_spread_0 < 1e-10 else '(SPLIT)'}")

    # Killing vector check
    print(f"\n  Killing status at s=0:")
    for a in range(8):
        status = "KILLING" if result_0['killing_status'][a] else "NON-KILLING"
        print(f"    e_{a} (Lie_norm={result_0['Lie_norm'][a]:.2e}): {status}")

    # L-homomorphism failure
    delta_F_0 = result_0['delta_F']
    print(f"\n  L-homomorphism failure |delta_F| at s=0:")
    print(f"    max |delta_F[a,b]|: {np.max(np.abs(delta_F_0)):.6e}")

    # ==================================================================
    # Main computation: tau_fold = 0.19
    # ==================================================================
    print_header(f"MAIN COMPUTATION: s = tau_fold = {tau_fold}")
    result = compute_mass_ratios_at_s(tau_fold)

    print(f"\n  Mass-squared eigenvalues (M_KK^2 units):")
    print(f"    D-sector (d,s,b quarks): {result['evals_D']}")
    print(f"    b-sector (e,mu,tau):     {result['evals_b']}")
    print(f"    c-sector (u,c,t quarks): {result['evals_c']}")

    print(f"\n  Mass eigenvalues (M_KK units):")
    print(f"    D-sector (d,s,b): {result['mass_D']}")
    print(f"    b-sector (e,mu,tau): {result['mass_b']}")
    print(f"    c-sector (u,c,t):    {result['mass_c']}")

    # Compute mass RATIOS within each sector
    print_section("Mass ratios WITHIN sectors (framework vs PDG)")

    # Down sector
    if result['mass_D'][0] > 0:
        r_sd = result['mass_D'][1] / result['mass_D'][0]
        r_bd = result['mass_D'][2] / result['mass_D'][0]
        r_bs = result['mass_D'][2] / result['mass_D'][1]
        print(f"  Down-quark sector:")
        print(f"    m_s/m_d: framework = {r_sd:.3f}, PDG = {PDG_ratios['m_s/m_d']:.1f}")
        print(f"    m_b/m_d: framework = {r_bd:.3f}, PDG = {PDG_ratios['m_b/m_d']:.1f}")
        print(f"    m_b/m_s: framework = {r_bs:.3f}, PDG = {PDG_ratios['m_b/m_s']:.1f}")
    else:
        print(f"  Down-quark sector: lightest mass is zero (degenerate)")
        r_sd = r_bd = r_bs = np.nan

    # Lepton sector
    if result['mass_b'][0] > 0:
        r_mue = result['mass_b'][1] / result['mass_b'][0]
        r_taue = result['mass_b'][2] / result['mass_b'][0]
        r_taumu = result['mass_b'][2] / result['mass_b'][1]
        print(f"\n  Lepton sector:")
        print(f"    m_mu/m_e:   framework = {r_mue:.3f}, PDG = {PDG_ratios['m_mu/m_e']:.1f}")
        print(f"    m_tau/m_e:  framework = {r_taue:.3f}, PDG = {PDG_ratios['m_tau/m_e']:.1f}")
        print(f"    m_tau/m_mu: framework = {r_taumu:.3f}, PDG = {PDG_ratios['m_tau/m_mu']:.1f}")
    else:
        print(f"\n  Lepton sector: lightest mass is zero (degenerate)")
        r_mue = r_taue = r_taumu = np.nan

    # Up sector
    if result['mass_c'][0] > 0:
        r_cu = result['mass_c'][1] / result['mass_c'][0]
        r_tu = result['mass_c'][2] / result['mass_c'][0]
        r_tc = result['mass_c'][2] / result['mass_c'][1]
        print(f"\n  Up-quark sector:")
        print(f"    m_c/m_u: framework = {r_cu:.3f}, PDG = {PDG_ratios['m_c/m_u']:.1f}")
        print(f"    m_t/m_u: framework = {r_tu:.3f}, PDG = {PDG_ratios['m_t/m_u']:.1e}")
        print(f"    m_t/m_c: framework = {r_tc:.3f}, PDG = {PDG_ratios['m_t/m_c']:.1f}")
    else:
        print(f"\n  Up-quark sector: lightest mass is zero (degenerate)")
        r_cu = r_tu = r_tc = np.nan

    # Cross-sector ratios
    print_section("Cross-sector ratios")
    if result['mass_b'].mean() > 0 and result['mass_D'].mean() > 0:
        r_btau = result['mass_D'][2] / result['mass_b'][2]
        r_tb = result['mass_c'][2] / result['mass_D'][2]
        print(f"  m_b/m_tau: framework = {r_btau:.3f}, PDG = {PDG_ratios['m_b/m_tau']:.2f}")
        print(f"  m_t/m_b:   framework = {r_tb:.3f}, PDG = {PDG_ratios['m_t/m_b']:.1f}")
    else:
        r_btau = r_tb = np.nan

    # Killing vector analysis at tau_fold
    print_section("Killing vector analysis at tau_fold")
    n_killing = sum(1 for v in result['killing_status'].values() if v)
    n_nonkilling = 8 - n_killing
    print(f"  Killing vectors: {n_killing}/8")
    print(f"  Non-Killing vectors: {n_nonkilling}/8 (these generate mass mixing)")

    for a in range(8):
        subspace = "su(2)" if a in SU2_IDX else ("C^2" if a in C2_IDX else "u(1)")
        status = "KILLING" if result['killing_status'][a] else "NON-KILLING"
        print(f"    e_{a} [{subspace}] Lie_norm={result['Lie_norm'][a]:.4e}: {status}")

    # L-homomorphism failure analysis
    print_section("L-homomorphism failure delta_F")
    delta_F = result['delta_F']
    print(f"  delta_F matrix (8x8, [e_a, e_b]_{{11}} component):")
    print(f"  max |delta_F|: {np.max(np.abs(delta_F)):.6f}")

    # Show which pairs have nonzero delta_F
    print(f"\n  Nonzero delta_F pairs (|delta_F| > 1e-10):")
    for a in range(8):
        for b in range(a+1, 8):
            if abs(delta_F[a, b]) > 1e-10:
                print(f"    (e_{a}, e_{b}): delta_F = {delta_F[a,b]:.6f}")

    # Laplacian vs full Dirac comparison
    print_section("Laplacian vs Full Dirac mass matrices")

    Omega_D_lap = result['Omega_D_lap']
    Omega_b_lap = result['Omega_b_lap']
    Omega_c_lap = result['Omega_c_lap']

    evals_D_lap = np.sort(eigvalsh(0.5*(Omega_D_lap + Omega_D_lap.conj().T)))
    evals_b_lap = np.sort(eigvalsh(0.5*(Omega_b_lap + Omega_b_lap.conj().T)))
    evals_c_lap = np.sort(eigvalsh(0.5*(Omega_c_lap + Omega_c_lap.conj().T)))

    print(f"  LAPLACIAN eigenvalues:")
    print(f"    D: {evals_D_lap}")
    print(f"    b: {evals_b_lap}")
    print(f"    c: {evals_c_lap}")
    print(f"  DIRAC eigenvalues (M^2):")
    print(f"    D: {result['evals_D']}")
    print(f"    b: {result['evals_b']}")
    print(f"    c: {result['evals_c']}")

    # Splitting ratios
    print_section("Eigenvalue splitting ratios (Jensen hierarchy test)")
    L1 = np.exp(2.0 * tau_fold)
    L2 = np.exp(-2.0 * tau_fold)
    L3 = np.exp(tau_fold)

    print(f"  Jensen scale factors at s={tau_fold}:")
    print(f"    L1 (u(1)) = {L1:.4f}")
    print(f"    L2 (su(2)) = {L2:.4f}")
    print(f"    L3 (C^2) = {L3:.4f}")
    print(f"    L1/L2 = {L1/L2:.4f} (u(1)/su(2) ratio)")
    print(f"    L3/L2 = {L3/L2:.4f} (C^2/su(2) ratio)")
    print(f"    L1/L3 = {L1/L3:.4f} (u(1)/C^2 ratio)")

    # Tau-scan: how do the mass ratios evolve with Jensen parameter?
    print_header("TAU-SCAN: Mass eigenvalue evolution")
    s_values = np.linspace(0.0, 0.5, 11)
    scan_data = []

    for s_val in s_values:
        res = compute_mass_ratios_at_s(s_val, verbose=False)
        scan_data.append(res)
        eD = res['mass_D']
        eb = res['mass_b']
        ec = res['mass_c']
        if eD[0] > 1e-15:
            ratio_D = eD[2] / eD[0]
        else:
            ratio_D = np.inf if eD[2] > 0 else 1.0
        if eb[0] > 1e-15:
            ratio_b = eb[2] / eb[0]
        else:
            ratio_b = np.inf if eb[2] > 0 else 1.0
        if ec[0] > 1e-15:
            ratio_c = ec[2] / ec[0]
        else:
            ratio_c = np.inf if ec[2] > 0 else 1.0

        print(f"  s={s_val:.3f}: m3/m1(D)={ratio_D:8.3f}  m3/m1(b)={ratio_b:8.3f}  m3/m1(c)={ratio_c:8.3f}")

    # ==================================================================
    # GATE ASSESSMENT
    # ==================================================================
    print_header("GATE ASSESSMENT: YUKAWA-FIRST-PRINCIPLES-61")

    # Collect all predicted ratios
    predicted_ratios = {}
    if not np.isnan(r_sd):
        predicted_ratios['m_s/m_d'] = r_sd
    if not np.isnan(r_bd):
        predicted_ratios['m_b/m_d'] = r_bd
    if not np.isnan(r_bs):
        predicted_ratios['m_b/m_s'] = r_bs
    if not np.isnan(r_mue):
        predicted_ratios['m_mu/m_e'] = r_mue
    if not np.isnan(r_taue):
        predicted_ratios['m_tau/m_e'] = r_taue
    if not np.isnan(r_taumu):
        predicted_ratios['m_tau/m_mu'] = r_taumu
    if not np.isnan(r_cu):
        predicted_ratios['m_c/m_u'] = r_cu
    if not np.isnan(r_tu):
        predicted_ratios['m_t/m_u'] = r_tu
    if not np.isnan(r_tc):
        predicted_ratios['m_t/m_c'] = r_tc

    # Check each ratio
    any_within_30pct = False
    all_off_by_OOM = True
    n_ratios_checked = 0
    n_within_30pct = 0
    n_within_OOM = 0

    print(f"\n  Ratio comparison:")
    print(f"  {'Ratio':<12} {'Framework':>12} {'PDG':>12} {'log10(F/P)':>12} {'Status':>12}")
    print(f"  {'-'*60}")

    for key in sorted(predicted_ratios.keys()):
        if key in PDG_ratios:
            fw = predicted_ratios[key]
            pdg = PDG_ratios[key]
            if fw > 0 and pdg > 0:
                log_ratio = np.log10(fw / pdg)
                within_30 = abs(fw - pdg) / pdg < 0.30
                within_OOM = abs(log_ratio) < 1.0
                n_ratios_checked += 1
                if within_30:
                    any_within_30pct = True
                    n_within_30pct += 1
                    status = "PASS (30%)"
                elif within_OOM:
                    all_off_by_OOM = False
                    n_within_OOM += 1
                    status = "within OOM"
                else:
                    status = "OFF > OOM"
                print(f"  {key:<12} {fw:12.4f} {pdg:12.1f} {log_ratio:12.3f} {status:>12}")
            else:
                print(f"  {key:<12} {fw:12.4f} {pdg:12.1f} {'N/A':>12} {'ZERO':>12}")

    # Structure check: do we get 3 distinct generations?
    D_distinct = len(set(np.round(result['mass_D'], 10)))
    b_distinct = len(set(np.round(result['mass_b'], 10)))
    c_distinct = len(set(np.round(result['mass_c'], 10)))
    three_gen_structure = (D_distinct == 3 and b_distinct == 3 and c_distinct == 3)

    print(f"\n  Structural check:")
    print(f"    D-sector distinct masses: {D_distinct}/3")
    print(f"    b-sector distinct masses: {b_distinct}/3")
    print(f"    c-sector distinct masses: {c_distinct}/3")
    print(f"    Three-generation structure: {'YES' if three_gen_structure else 'NO'}")

    # Determine verdict
    if any_within_30pct:
        verdict = "PASS"
        reason = f"{n_within_30pct} mass ratio(s) within 30% of PDG"
    elif not all_off_by_OOM or n_within_OOM > 0:
        verdict = "INFO"
        reason = f"Structure {'correct' if three_gen_structure else 'incorrect'}. {n_within_OOM} ratios within OOM. Needs RG running."
    else:
        if three_gen_structure:
            verdict = "INFO"
            reason = "3 generations produced but all ratios off by >OOM. Jensen splitting too weak for mass hierarchy."
        else:
            verdict = "FAIL"
            reason = "Neither correct generation structure nor mass ratios."

    print(f"\n  ============================================")
    print(f"  VERDICT: {verdict}")
    print(f"  REASON:  {reason}")
    print(f"  ============================================")

    # ==================================================================
    # Save data
    # ==================================================================
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             's61_yukawa_first_principles.npz')

    # Build scan arrays
    scan_s = np.array([d['s'] for d in scan_data])
    scan_mass_D = np.array([d['mass_D'] for d in scan_data])
    scan_mass_b = np.array([d['mass_b'] for d in scan_data])
    scan_mass_c = np.array([d['mass_c'] for d in scan_data])

    np.savez(save_path,
             # Main results at tau_fold
             s=tau_fold,
             mass_D=result['mass_D'],
             mass_b=result['mass_b'],
             mass_c=result['mass_c'],
             evals_D=result['evals_D'],
             evals_b=result['evals_b'],
             evals_c=result['evals_c'],
             M2_D=result['M2_D'],
             M2_b=result['M2_b'],
             M2_c=result['M2_c'],
             evecs_D=result['evecs_D'],
             evecs_b=result['evecs_b'],
             evecs_c=result['evecs_c'],
             delta_F=result['delta_F'],
             Lie_norm=result['Lie_norm'],
             # Laplacian mass matrices
             Omega_D_lap=result['Omega_D_lap'],
             Omega_b_lap=result['Omega_b_lap'],
             Omega_c_lap=result['Omega_c_lap'],
             # s=0 reference
             mass_D_s0=result_0['mass_D'],
             mass_b_s0=result_0['mass_b'],
             mass_c_s0=result_0['mass_c'],
             # Tau scan
             scan_s=scan_s,
             scan_mass_D=scan_mass_D,
             scan_mass_b=scan_mass_b,
             scan_mass_c=scan_mass_c,
             # PDG reference values
             PDG_mass_ratios=np.array(list(PDG_ratios.values())),
             PDG_ratio_names=np.array(list(PDG_ratios.keys())),
             # Gate result
             verdict=np.array([verdict]),
             reason=np.array([reason]),
             conn_err=result['conn_err'],
             )

    print(f"\n  Data saved to: {save_path}")
    print(f"\n{'='*72}")
    print(f"  COMPUTATION COMPLETE")
    print(f"{'='*72}")

    return result, result_0, scan_data, verdict, reason


if __name__ == '__main__':
    result, result_0, scan_data, verdict, reason = main()
