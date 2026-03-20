#!/usr/bin/env python3
"""
Session 36: Spectral Action Gauge Coupling on SU(3)

The spectral action Tr(f(D_K^2/Lambda^2)) on a compact Lie group K produces
gauge kinetic terms via the a_4 Seeley-DeWitt coefficient. The coefficient
of the gauge field strength F_a determines the inverse coupling g_a^{-2}.

For the Dirac operator D_K on (SU(3), g_Jensen(s)), the a_4 coefficient is:

  a_4 = (4*pi)^{-d/2} * integral_K [
    (1/12) Tr(Omega_{mu nu} Omega^{mu nu})  <-- gauge kinetic
    + (1/2) Tr(E)                           <-- endomorphism
    + ...scalar curvature terms...
  ] vol_K

where Omega_{mu nu} is the curvature of the spin connection, and the
trace is over the spinor bundle.

KEY QUESTION: Does the spectral action on K=SU(3) give a gauge coupling
ratio DIFFERENT from both the KK eigenvalue (sqrt(3)) and the NCG trace (sqrt(3/5))?

APPROACH: Compute the gauge kinetic coefficient from the spin connection
curvature on SU(3) with Jensen metric. The spin connection Omega_ab
depends on the metric, so the Jensen deformation modifies the gauge
kinetic normalization.

On a Lie group with left-invariant metric g, the spin connection is:
  omega^a_b(e_c) = (1/2)(C^a_{bc} + g^{ad}g_{ce}C^e_{db} - g^{ad}g_{be}C^e_{dc})
where C^a_{bc} are the structure constants.

The curvature 2-form:
  Omega^a_b = d(omega^a_b) + omega^a_c wedge omega^c_b

For left-invariant fields on a Lie group, this reduces to:
  Omega^a_b(e_c, e_d) = omega^a_b([e_c, e_d]) + R^a_{bcd}

The key: the spin connection curvature Tr(Omega^2) integrated over K
gives the gauge kinetic coefficient. Different blocks (u(1), su(2), C^2)
contribute differently because the Jensen metric treats them differently.

Author: main agent, Session 36
Date: 2026-03-07
"""

import numpy as np
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

# Try to import the tier1 infrastructure
try:
    from tier1_dirac_spectrum import (
        su3_generators, compute_structure_constants, compute_killing_form,
        jensen_metric, orthonormal_frame, U1_IDX, SU2_IDX, C2_IDX
    )
    HAS_TIER1 = True
except ImportError:
    HAS_TIER1 = False
    print("WARNING: tier1_dirac_spectrum not available. Using standalone computation.")

print("=" * 70)
print("SPECTRAL ACTION GAUGE COUPLING ON SU(3)")
print("=" * 70)

# ─────────────────────────────────────────────────────────────
# 1. Setup: structure constants and Jensen metric
# ─────────────────────────────────────────────────────────────

if HAS_TIER1:
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
else:
    # Standalone: compute Gell-Mann structure constants
    lam = np.zeros((8, 3, 3), dtype=complex)
    lam[0] = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]])
    lam[1] = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]])
    lam[2] = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]])
    lam[3] = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]])
    lam[4] = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]])
    lam[5] = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]])
    lam[6] = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]])
    lam[7] = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]]) / np.sqrt(3)

    # Anti-hermitian generators e_a = i*lam_a/2
    gens = 1j * lam / 2

    # Structure constants: [e_a, e_b] = f^c_ab e_c
    f_abc = np.zeros((8, 8, 8))
    for a in range(8):
        for b in range(8):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(8):
                # Project: f^c_ab = -2 * Tr(comm * e_c^dag) / Tr(e_c * e_c^dag)
                f_abc[c, a, b] = -2 * np.trace(comm @ gens[c].conj().T).real / \
                                  np.trace(gens[c] @ gens[c].conj().T).real

    # Killing form B_ab = f^c_ad f^d_bc
    B_ab = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            for c in range(8):
                for d in range(8):
                    B_ab[a, b] += f_abc[c, a, d] * f_abc[d, b, c]

    U1_IDX = [7]
    SU2_IDX = [0, 1, 2]
    C2_IDX = [3, 4, 5, 6]

print(f"\n  Killing form diagonal (should be -6 for all):")
for a in range(8):
    print(f"    B[{a},{a}] = {B_ab[a,a]:.4f}")

# ─────────────────────────────────────────────────────────────
# 2. Spin connection on (SU(3), g_Jensen(s))
# ─────────────────────────────────────────────────────────────

def compute_spin_connection(g_ab, f_abc):
    """
    Compute spin connection omega^a_{bc} on a Lie group with
    left-invariant metric g and structure constants f.

    omega^a_b(e_c) = (1/2)(f^a_{bc} + g^{ad}g_{ce}f^e_{db} - g^{ad}g_{be}f^e_{dc})

    This is the Levi-Civita connection in the left-invariant frame.
    """
    n = len(g_ab)
    g_inv = np.linalg.inv(g_ab)
    omega = np.zeros((n, n, n))

    for a in range(n):
        for b in range(n):
            for c in range(n):
                term1 = f_abc[a, b, c]
                term2 = sum(g_inv[a, d] * g_ab[c, e] * f_abc[e, d, b]
                           for d in range(n) for e in range(n))
                term3 = sum(g_inv[a, d] * g_ab[b, e] * f_abc[e, d, c]
                           for d in range(n) for e in range(n))
                omega[a, b, c] = 0.5 * (term1 + term2 - term3)

    return omega


def compute_riemann(omega, f_abc):
    """
    Compute Riemann tensor R^a_{bcd} from the spin connection.

    On a Lie group with left-invariant connection:
    R^a_{bcd} = omega^a_{b[c,d]} + omega^a_{ec} omega^e_{bd} - omega^a_{ed} omega^e_{bc}
              - omega^a_{be} f^e_{cd}

    Simplified for left-invariant:
    R^a_{bcd} = -omega^a_{be} f^e_{cd} + omega^a_{ec} omega^e_{bd} - omega^a_{ed} omega^e_{bc}
    """
    n = len(omega)
    R = np.zeros((n, n, n, n))

    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    # -omega^a_{be} f^e_{cd}
                    term1 = -sum(omega[a, b, e] * f_abc[e, c, d] for e in range(n))
                    # +omega^a_{ec} omega^e_{bd}
                    term2 = sum(omega[a, e, c] * omega[e, b, d] for e in range(n))
                    # -omega^a_{ed} omega^e_{bc}
                    term3 = -sum(omega[a, e, d] * omega[e, b, c] for e in range(n))
                    R[a, b, c, d] = term1 + term2 + term3

    return R


# ─────────────────────────────────────────────────────────────
# 3. Jensen metric and gauge kinetic coefficients
# ─────────────────────────────────────────────────────────────

print(f"\n{'─' * 70}")
print("GAUGE KINETIC COEFFICIENTS FROM SPIN CONNECTION CURVATURE")
print(f"{'─' * 70}")

s_values = [0.0, 0.10, 0.190, 0.30, 0.50]

for s in s_values:
    # Jensen metric: g_ab = |B_ab| * lambda_i(s) for generator in block i
    lam1 = np.exp(2 * s)   # u(1)
    lam2 = np.exp(-2 * s)  # su(2)
    lam3 = np.exp(s)       # C^2

    g_ab = np.zeros((8, 8))
    for a in range(8):
        for b in range(8):
            if a == b:
                if a in U1_IDX:
                    g_ab[a, a] = abs(B_ab[a, a]) * lam1
                elif a in SU2_IDX:
                    g_ab[a, a] = abs(B_ab[a, a]) * lam2
                elif a in C2_IDX:
                    g_ab[a, a] = abs(B_ab[a, a]) * lam3

    # Compute spin connection
    omega = compute_spin_connection(g_ab, f_abc)

    # Compute Riemann tensor
    R_abcd = compute_riemann(omega, f_abc)

    # Gauge kinetic coefficient for each block:
    # The coefficient of F_a^2 in the spectral action a_4 is proportional to
    # the integral of Tr(Omega^2) restricted to generators in block i.
    #
    # For gauge fields in the u(1) direction:
    #   c_{u(1)} propto sum_{c,d} R^a_{a,c,d} for a in u(1)
    # But more precisely: the gauge kinetic term comes from
    #   Tr(F_i^2) with coefficient determined by the metric normalization.
    #
    # The simplest approach: the gauge coupling g_i is determined by
    #   g_i^{-2} propto g_ab(e_i, e_i) * Vol(K)
    # This is Baptista's formula (Paper 15 eq 3.53 for left-invariant fields).
    #
    # For the spectral action, the coefficient is:
    #   g_i^{-2} propto Tr_S(T_i^2) * integral_K vol_K
    # where T_i is the generator in the spin representation.

    # The spin representation of su(3) on the 16-dim spinor space:
    # The spin rep is built from Cliff(8) acting on C^{16} = C^{2^4}.
    # But the gauge kinetic coefficient in the spectral action
    # traces over the spinor indices, giving an additional factor.

    # For a left-invariant metric on K:
    # 1/g_i^2 = c * g_K(e_i, e_i) * Vol(K)  (Baptista, geometric)
    # 1/g_i^2 = c' * Tr_S(rho(e_i)^2) * Vol(K)  (spectral, spin rep trace)
    #
    # The difference between Baptista and spectral: Tr_S(rho(e_i)^2) vs g_K(e_i, e_i).
    # In the spin representation, each generator e_a acts as
    #   rho(e_a) = (1/4) sum_{b,c} omega^a_{bc} gamma^b gamma^c
    # (Kosmann lift). The trace Tr_S(rho(e_a)^2) involves the spin connection.

    # For the bi-invariant metric (s=0): omega^a_{bc} = (1/2) f^a_{bc}
    # rho(e_a) = (1/8) sum_{b,c} f^a_{bc} gamma^b gamma^c = (1/8) [gamma_b, gamma_c] f^a_{bc}/2
    # = (1/4) sum_{b<c} f^a_{bc} gamma^b gamma^c

    # Trace: Tr_S(rho(e_a)^2) = (1/16) sum_{b,c,d,e} f^a_{bc} f^a_{de} Tr(gamma^b gamma^c gamma^d gamma^e)

    # For the spin rep on dim=8 (internal), spinor dim = 2^4 = 16.
    # Tr(gamma^b gamma^c gamma^d gamma^e) = 16 * (delta_{bc}delta_{de} - delta_{bd}delta_{ce} + delta_{be}delta_{cd})

    # So: Tr_S(rho(e_a)^2) = sum_{b,c,d,e} f^a_{bc} f^a_{de} (delta_{bc}delta_{de} - delta_{bd}delta_{ce} + delta_{be}delta_{cd})
    # = f^a_{bc} f^a_{bc} (sum over b,c using delta_{bc}delta_{de} gives 0 since f is antisymmetric)
    # Wait: f^a_{bc} is antisymmetric in b,c. delta_{bc} f^a_{bc} = 0.
    # Second term: -sum_{b,c} f^a_{bc} f^a_{cb} = +sum f^a_{bc} f^a_{bc} (using antisymmetry)
    # Third term: sum_{b,c} f^a_{bc} f^a_{cb} = -sum f^a_{bc}^2

    # Hmm, this is getting complicated. Let me just compute numerically.

    # Spin representation of e_a on 16-dim spinor:
    # rho(e_a) = (1/4) sum_{b<c} omega^a_{bc} * Gamma_{bc}
    # where Gamma_{bc} = (1/2)[gamma_b, gamma_c]

    # Build 8-dim Clifford algebra gamma matrices (real, 16x16)
    # Using tensor products of Pauli matrices
    I2 = np.eye(2)
    sx = np.array([[0, 1], [1, 0]])
    sy = np.array([[0, -1j], [1j, 0]])
    sz = np.array([[1, 0], [0, -1]])

    # 8 gamma matrices for Cliff(8), dimension 2^4 = 16
    # gamma_1 = sx x I x I x I, etc.
    def kron4(a, b, c, d):
        return np.kron(np.kron(np.kron(a, b), c), d)

    gamma = np.zeros((8, 16, 16), dtype=complex)
    gamma[0] = kron4(sx, I2, I2, I2)
    gamma[1] = kron4(sy, I2, I2, I2)
    gamma[2] = kron4(sz, sx, I2, I2)
    gamma[3] = kron4(sz, sy, I2, I2)
    gamma[4] = kron4(sz, sz, sx, I2)
    gamma[5] = kron4(sz, sz, sy, I2)
    gamma[6] = kron4(sz, sz, sz, sx)
    gamma[7] = kron4(sz, sz, sz, sy)

    # Verify: {gamma_a, gamma_b} = 2*delta_{ab}
    for a in range(8):
        for b in range(8):
            anticomm = gamma[a] @ gamma[b] + gamma[b] @ gamma[a]
            expected = 2 * (1 if a == b else 0) * np.eye(16)
            assert np.allclose(anticomm, expected), f"Clifford fail at ({a},{b})"

    # Gamma_{ab} = (1/2)[gamma_a, gamma_b]
    Gamma_ab = np.zeros((8, 8, 16, 16), dtype=complex)
    for a in range(8):
        for b in range(8):
            Gamma_ab[a, b] = 0.5 * (gamma[a] @ gamma[b] - gamma[b] @ gamma[a])

    # Spin representation of e_a:
    # rho(e_a) = (1/4) sum_{b,c} omega^a_{bc} Gamma_{bc}
    rho = np.zeros((8, 16, 16), dtype=complex)
    for a in range(8):
        for b in range(8):
            for c in range(8):
                rho[a] += 0.25 * omega[a, b, c] * Gamma_ab[b, c]

    # Trace of rho(e_a)^2 for each generator
    tr_rho2 = np.zeros(8)
    for a in range(8):
        tr_rho2[a] = np.trace(rho[a] @ rho[a]).real

    # Gauge kinetic coefficient per block
    c_u1 = sum(tr_rho2[a] for a in U1_IDX)
    c_su2 = sum(tr_rho2[a] for a in SU2_IDX) / 3  # per generator
    c_C2 = sum(tr_rho2[a] for a in C2_IDX) / 4   # per generator

    # Coupling ratio: g_i^2 proportional to 1/c_i (per generator)
    # g'^{-2} propto c_{u1} (1 generator)
    # g^{-2} propto c_{su2} (per generator, 3 generators)
    # Ratio: g'^2/g^2 = c_{su2}/c_{u1}

    ratio_spectral = c_su2 / c_u1 if c_u1 != 0 else float('inf')
    sin2_spectral = ratio_spectral / (1 + ratio_spectral) if ratio_spectral != float('inf') else 0

    # Also: Baptista geometric ratio
    ratio_baptista = 3 * np.exp(-4 * s)
    sin2_baptista = ratio_baptista / (1 + ratio_baptista)

    print(f"\n  s = {s:.3f}:")
    print(f"    Spin rep traces: Tr(rho^2) per block:")
    print(f"      u(1) [{U1_IDX}]:  {c_u1:.6f}")
    print(f"      su(2) [{SU2_IDX}]: {c_su2:.6f} (per gen)")
    print(f"      C^2 [{C2_IDX}]:   {c_C2:.6f} (per gen)")
    print(f"    Spectral ratio g'^2/g^2 = c_su2/c_u1 = {ratio_spectral:.6f}")
    print(f"    sin^2(spectral) = {sin2_spectral:.6f}")
    print(f"    Baptista ratio g'^2/g^2 = 3*e^{{-4s}} = {ratio_baptista:.6f}")
    print(f"    sin^2(Baptista) = {sin2_baptista:.6f}")
    if abs(ratio_spectral - 1.5) < 0.01:
        print(f"    >>> MATCH: ratio ≈ 3/2! <<<")
    if abs(ratio_spectral - 0.6) < 0.01:
        print(f"    >>> MATCH: ratio ≈ 3/5 (NCG)! <<<")

print(f"\n{'=' * 70}")
print("COMPARISON AT s=0")
print(f"{'=' * 70}")
print(f"  Baptista (eigenvalue):  g'^2/g^2 = 3.000,    sin^2 = 0.750")
print(f"  Connes (full trace):    g'^2/g^2 = 0.600,    sin^2 = 0.375")
print(f"  Target (sqrt(3/2)):     g'^2/g^2 = 1.500,    sin^2 = 0.600")
print(f"  Spectral action:        see above")
