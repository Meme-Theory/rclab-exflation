#!/usr/bin/env python3
"""
Session 35 SPEC-35: Specificity Test -- SU(2)xSU(2) vs SU(3)

Compare spectral action curvature d^2 S/ds^2 on SU(2)xSU(2) with Berger-type
deformation against SU(3) with Jensen deformation (d^2 S = 20.43).

Mathematical background:
=========================

SU(3): dim = 8, spinor rank = 2^4 = 16.
    Jensen deformation: one-parameter squashing preserving volume.
    Singlet (0,0) sector has 16 eigenvalues (8 positive by PH pairing).
    d^2 S/dtau^2 = 20.43 at tau = 0.20 (bare, from RPA-32b / Strutinsky-33a).

SU(2)xSU(2): dim = 6, spinor rank = 2^3 = 8.
    NOT the same dimension as SU(3). We compare per-mode curvature.

Dirac spectrum on round S^3 = SU(2):
    lambda_{n,pm} = +/-(n + 3/2),  n = 0, 1, 2, ...
    multiplicity = (n+1)(n+2) for each sign

Berger sphere deformation on SU(2):
    Left-invariant metric g_s = diag(e^{-s/2}, e^{-s/2}, e^s) on the Lie algebra
    basis {E_1, E_2, E_3} with [E_a, E_b] = 2*eps_{abc} E_c.
    Volume-preserving: det(g)^{1/2} = h_1*h_2*h_3 = 1.

Method:
    Construct the Dirac operator matrix D_j in each Peter-Weyl j-sector using the
    representation theory of SU(2). The matrix is anti-hermitian (because the
    representation matrices rho(E_a) = -2i*J_a are anti-hermitian and Pauli matrices
    are hermitian). The physical Dirac eigenvalues are the imaginary parts of the
    matrix eigenvalues (which are purely imaginary by anti-hermiticity).

    Verified: round S^3 gives lambda = +/-(n+3/2), mult = (n+1)(n+2).

Product structure:
    For SU(2) x SU(2) (3+3 = 6, even total):
    D = D_1 tensor 1 tensor sigma_1 + 1 tensor D_2 tensor sigma_2
    Eigenvalues: +/-sqrt(mu_j^2 + nu_k^2) where mu_j, nu_k are the factor eigenvalues.

Author: spectral-geometer (corrected by dirac-antimatter-theorist)
Date: 2026-03-07
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

print("=" * 70)
print("SPEC-35: SPECIFICITY TEST -- SU(2)xSU(2) vs SU(3)")
print("=" * 70)

# ---------------------------------------------------------------
# Part 1: Dirac Operator on SU(2) with Berger Deformation
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 1: Dirac Spectrum on SU(2) = S^3 (round and Berger)")
print("=" * 70)


def su2_dirac_eigenvalues_berger(s_param, n_max=20):
    """
    Compute Dirac eigenvalues on Berger S^3 with volume-preserving deformation.

    Metric: g_{aa} = h_a^2 with h_1 = h_2 = e^{-s/4}, h_3 = e^{s/2}.
    Volume preserved: h_1*h_2*h_3 = 1.

    Structure constants in orthonormal frame:
        f^c_{ab} = 2*h_c/(h_a*h_b) * eps_{abc}

    Connection coefficients (Koszul formula, left-invariant metric):
        Gamma^c_{ab} = (1/2)(f^c_{ab} - f^b_{ac} - f^a_{bc})

    Spin connection: omega_spinor[a] = (1/2) sum_{b,c} Gamma^b_{ac} Sigma^{bc}
    where Sigma^{bc} = (1/4)[gamma^b, gamma^c].

    The Dirac operator matrix in the j-sector is ANTI-HERMITIAN.
    Physical eigenvalues = imaginary parts of the matrix eigenvalues.

    Returns: (evals, mults) where evals are physical eigenvalues and
    mults are Peter-Weyl multiplicities (2j+1) for each eigenvalue.
    """
    sigma = [np.array([[0, 1], [1, 0]], dtype=complex),
             np.array([[0, -1j], [1j, 0]], dtype=complex),
             np.array([[1, 0], [0, -1]], dtype=complex)]

    h = np.array([np.exp(-s_param / 4), np.exp(-s_param / 4), np.exp(s_param / 2)])

    # Levi-Civita tensor
    eps_t = np.zeros((3, 3, 3))
    eps_t[0, 1, 2] = eps_t[1, 2, 0] = eps_t[2, 0, 1] = 1.0
    eps_t[0, 2, 1] = eps_t[2, 1, 0] = eps_t[1, 0, 2] = -1.0

    # Structure constants in orthonormal frame
    fc = np.zeros((3, 3, 3))
    for a in range(3):
        for b in range(3):
            for c in range(3):
                fc[c, a, b] = 2.0 * h[c] / (h[a] * h[b]) * eps_t[a, b, c]

    # Connection coefficients: Gamma^c_{ab} = <nabla_{e_a} e_b, e_c>
    Gam = np.zeros((3, 3, 3))
    for c in range(3):
        for a in range(3):
            for b in range(3):
                Gam[c, a, b] = 0.5 * (fc[c, a, b] - fc[b, a, c] - fc[a, b, c])

    # Sigma^{bc} = (1/4)[gamma^b, gamma^c]
    Sig = np.zeros((3, 3, 2, 2), dtype=complex)
    for b in range(3):
        for c in range(3):
            Sig[b, c] = 0.25 * (sigma[b] @ sigma[c] - sigma[c] @ sigma[b])

    # Spinorial connection: omega_spinor[a] = (1/2) sum_{b,c} Gamma^b_{ac} Sigma^{bc}
    omega_spinor = np.zeros((3, 2, 2), dtype=complex)
    for a in range(3):
        for b in range(3):
            for c in range(3):
                omega_spinor[a] += 0.5 * Gam[b, a, c] * Sig[b, c]

    # Total spin connection contribution to D: sum_a gamma^a @ omega_spinor[a]
    sc_total = np.zeros((2, 2), dtype=complex)
    for a in range(3):
        sc_total += sigma[a] @ omega_spinor[a]

    all_evals = []
    all_mults = []

    for two_j in range(0, 2 * (n_max + 1)):
        j = two_j / 2.0
        dim_j = two_j + 1

        # Spin-j matrices
        m_vals = np.arange(-j, j + 0.5, 1.0)
        assert len(m_vals) == dim_j

        Jz = np.diag(m_vals).astype(complex)
        Jp = np.zeros((dim_j, dim_j), dtype=complex)
        Jm = np.zeros((dim_j, dim_j), dtype=complex)
        for i in range(dim_j):
            m = m_vals[i]
            if i + 1 < dim_j:
                Jp[i + 1, i] = np.sqrt(j * (j + 1) - m * (m + 1))
            if i - 1 >= 0:
                Jm[i - 1, i] = np.sqrt(j * (j + 1) - m * (m - 1))
        Jx = 0.5 * (Jp + Jm)
        Jy = -0.5j * (Jp - Jm)
        J_matrices = [Jx, Jy, Jz]

        # Representation: rho(E_a) = -2i * J_a
        # Satisfies [rho(E_1), rho(E_2)] = 2*rho(E_3) etc.
        rho_E = [(-2.0j) * J for J in J_matrices]

        # Dirac operator in j-sector (anti-hermitian matrix):
        # D_j = sum_a kron(rho_E[a]/h[a], sigma[a]) + kron(I, sc_total)
        D_j = np.zeros((dim_j * 2, dim_j * 2), dtype=complex)
        for a in range(3):
            D_j += np.kron(rho_E[a] / h[a], sigma[a])
        D_j += np.kron(np.eye(dim_j, dtype=complex), sc_total)

        # Verify anti-hermiticity
        ah_err = np.max(np.abs(D_j + D_j.conj().T))
        if ah_err > 1e-10:
            print(f"  WARNING: j={j}, anti-hermiticity error = {ah_err:.2e}")

        # Physical eigenvalues = imaginary parts (D_j is anti-hermitian)
        evals_complex = np.linalg.eigvals(D_j)
        re_err = np.max(np.abs(evals_complex.real))
        if re_err > 1e-10:
            print(f"  WARNING: j={j}, real part residual = {re_err:.2e}")

        evals_phys = evals_complex.imag

        all_evals.extend(evals_phys)
        all_mults.extend([dim_j] * len(evals_phys))

    return np.array(all_evals), np.array(all_mults)


# ---------------------------------------------------------------
# Verify: round S^3 spectrum
# ---------------------------------------------------------------

print("\nVerifying round S^3 (s=0) Dirac spectrum:")
evals_0, mults_0 = su2_dirac_eigenvalues_berger(0.0, n_max=8)

# Sort by absolute value
idx = np.argsort(np.abs(evals_0))
evals_sorted = evals_0[idx]
mults_sorted = mults_0[idx]

# Group positive eigenvalues with total Peter-Weyl multiplicities
pos_mask = evals_sorted > 0.01
pos_evals = evals_sorted[pos_mask]
pos_mults = mults_sorted[pos_mask]

unique_vals = []
unique_total_mults = []
tol = 0.01
for ev, mu in zip(pos_evals, pos_mults):
    found = False
    for i, uv in enumerate(unique_vals):
        if abs(ev - uv) < tol:
            unique_total_mults[i] += mu
            found = True
            break
    if not found:
        unique_vals.append(ev)
        unique_total_mults.append(mu)

print(f"  {'Eigenvalue':>12s}  {'Total mult':>10s}  {'Expected':>10s}  {'Exp mult':>10s}")
all_ok = True
for i, (v, m) in enumerate(zip(unique_vals[:8], unique_total_mults[:8])):
    n_exp = i
    ev_exp = n_exp + 1.5
    m_exp = (n_exp + 1) * (n_exp + 2)
    match = "OK" if abs(v - ev_exp) < 0.01 and abs(m - m_exp) < 0.5 else "MISMATCH"
    if match != "OK":
        all_ok = False
    print(f"  {v:12.6f}  {int(m):10d}  {ev_exp:10.1f}  {int(m_exp):10d}  {match}")

if all_ok:
    print("  VERIFICATION PASSED: Round S^3 spectrum correct.")
else:
    print("  VERIFICATION FAILED!")


# ---------------------------------------------------------------
# Part 2: Berger Deformation Sweep
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 2: Berger Deformation Sweep on Single SU(2)")
print("=" * 70)

s_values = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
n_max_su2 = 15

print("\nComputing SU(2) spectra across deformation parameter s...")
su2_spectra = {}
for s in s_values:
    evals, mults = su2_dirac_eigenvalues_berger(s, n_max=n_max_su2)
    su2_spectra[s] = (evals, mults)
    n_pos = np.sum(evals > 0.01)
    n_neg = np.sum(evals < -0.01)
    print(f"  s={s:.2f}: {len(evals)} eigenvalues ({n_pos} pos, {n_neg} neg), "
          f"min|lambda|={np.min(np.abs(evals)):.6f}, max|lambda|={np.max(np.abs(evals)):.6f}")


# ---------------------------------------------------------------
# Part 3: Product Spectrum SU(2)xSU(2) with Deformation
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 3: Product Spectrum SU(2)xSU(2)")
print("=" * 70)


def get_sorted_positive_spectrum(evals, mults):
    """Return sorted positive eigenvalues and their Peter-Weyl multiplicities."""
    mask = evals > 0.01
    pos_e = evals[mask]
    pos_m = mults[mask]
    idx = np.argsort(pos_e)
    return pos_e[idx], pos_m[idx]


N_match = 8  # match SU(3) singlet mode count (8 positive modes)

S_product = np.zeros(len(s_values))
S_product_matched = np.zeros(len(s_values))

for si, s in enumerate(s_values):
    e1, m1 = get_sorted_positive_spectrum(*su2_spectra[s])
    e2, m2 = get_sorted_positive_spectrum(*su2_spectra[0.0])

    # Product eigenvalues: sqrt(mu^2 + nu^2) with multiplicity m1*m2
    product_evals = []
    product_mults = []
    for i in range(len(e1)):
        for j in range(len(e2)):
            ev = np.sqrt(e1[i]**2 + e2[j]**2)
            mt = m1[i] * m2[j]
            product_evals.append(ev)
            product_mults.append(mt)

    product_evals = np.array(product_evals)
    product_mults = np.array(product_mults)

    idx = np.argsort(product_evals)
    product_evals = product_evals[idx]
    product_mults = product_mults[idx]

    # Method A: full sum with Peter-Weyl multiplicities
    S_product[si] = 2 * np.sum(product_evals * product_mults)

    # Method B: lowest N_match product modes (unit multiplicity, like SU(3) singlet)
    S_product_matched[si] = 2 * np.sum(product_evals[:N_match])

    if s in [0.0, 0.20, 0.40]:
        print(f"  s={s:.2f}: lowest {N_match} product evals = "
              f"{product_evals[:N_match].round(6)}")
        print(f"          S_matched = {S_product_matched[si]:.6f}, "
              f"S_full = {S_product[si]:.2f}")


# ---------------------------------------------------------------
# Part 4: Compute d^2 S/ds^2 via Cubic Spline
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 4: Spectral Action Curvature d^2 S/ds^2")
print("=" * 70)

cs_matched = CubicSpline(s_values, S_product_matched)
d2S_matched_020 = cs_matched(0.20, 2)
d2S_matched_015 = cs_matched(0.15, 2)
d2S_matched_025 = cs_matched(0.25, 2)

print(f"\n  Method B (lowest {N_match} product modes, unit mult):")
print(f"    S(s=0.00) = {S_product_matched[0]:.6f}")
print(f"    S(s=0.20) = {S_product_matched[3]:.6f}")
print(f"    S(s=0.40) = {S_product_matched[7]:.6f}")
print(f"    d^2S/ds^2 at s=0.15: {d2S_matched_015:.4f}")
print(f"    d^2S/ds^2 at s=0.20: {d2S_matched_020:.4f}")
print(f"    d^2S/ds^2 at s=0.25: {d2S_matched_025:.4f}")

cs_full = CubicSpline(s_values, S_product)
d2S_full_020 = cs_full(0.20, 2)

print(f"\n  Method A (full product sum with Peter-Weyl mults):")
print(f"    d^2S/ds^2 at s=0.20: {d2S_full_020:.4f}")

S_single = np.zeros(len(s_values))
for si, s in enumerate(s_values):
    e1, m1 = get_sorted_positive_spectrum(*su2_spectra[s])
    S_single[si] = 2 * np.sum(e1[:4])
cs_single = CubicSpline(s_values, S_single)
d2S_single_020 = cs_single(0.20, 2)

print(f"\n  Single SU(2) (lowest 4 modes, unit mult):")
print(f"    d^2S/ds^2 at s=0.20: {d2S_single_020:.4f}")


# ---------------------------------------------------------------
# Part 5: SU(3) Comparison
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 5: COMPARISON WITH SU(3)")
print("=" * 70)

# Load SU(3) reference -- total_d2 has shape (1,), use .item()
d_su3 = np.load('tier0-computation/s33a_strutinsky.npz', allow_pickle=True)
d2S_su3 = d_su3['total_d2'].item()
S_su3_singlet = d_su3['S_singlet']
tau_su3 = d_su3['tau_values']

su3_per_mode = d2S_su3 / 8  # 8 positive modes in singlet

su2xu2_per_mode_matched = d2S_matched_020 / N_match

print(f"\n  SU(3) (Jensen, singlet, 8 positive modes):")
print(f"    d^2S/dtau^2 = {d2S_su3:.4f}")
print(f"    Per-mode curvature = {su3_per_mode:.4f}")
print(f"    S(tau=0.20) = {S_su3_singlet[3]:.6f}")

print(f"\n  SU(2)xSU(2) (Berger x round, lowest {N_match} product modes):")
print(f"    d^2S/ds^2 = {d2S_matched_020:.4f}")
print(f"    Per-mode curvature = {su2xu2_per_mode_matched:.4f}")
print(f"    S(s=0.20) = {S_product_matched[3]:.6f}")

ratio = d2S_matched_020 / d2S_su3
per_mode_ratio = su2xu2_per_mode_matched / su3_per_mode
print(f"\n  RATIOS:")
print(f"    d^2S(SU2xSU2) / d^2S(SU3) = {ratio:.4f}")
print(f"    Per-mode: curvature(SU2xSU2) / curvature(SU3) = {per_mode_ratio:.4f}")


# ---------------------------------------------------------------
# Part 6: Branch Structure Analysis
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 6: Branch Structure (does SU(2)xSU(2) have a fold?)")
print("=" * 70)

# Track eigenvalues of single SU(2) Berger
tracks_su2 = np.zeros((len(s_values), 8))
for si, s in enumerate(s_values):
    e1, m1 = get_sorted_positive_spectrum(*su2_spectra[s])
    tracks_su2[si, :] = e1[:8]

print("\n  SU(2) Berger eigenvalue tracks (lowest 8 positive):")
print(f"  {'s':>6s}", end="")
for j in range(8):
    print(f"  {'ev_'+str(j):>10s}", end="")
print()
for si, s in enumerate(s_values):
    print(f"  {s:6.2f}", end="")
    for j in range(8):
        print(f"  {tracks_su2[si,j]:10.6f}", end="")
    print()

# Fold check on single SU(2)
print("\n  Fold check (minimum at intermediate s):")
for j in range(8):
    cs_j = CubicSpline(s_values, tracks_su2[:, j])
    s_fine = np.linspace(0.01, 0.49, 1000)
    vals = cs_j(s_fine)
    s_min_idx = np.argmin(vals)
    s_min = s_fine[s_min_idx]
    d2_at_min = cs_j(s_min, 2)
    if 0.02 < s_min < 0.48:
        print(f"    Mode {j}: FOLD at s={s_min:.4f}, lambda={vals[s_min_idx]:.6f}, "
              f"d^2lambda/ds^2={d2_at_min:.4f}")
    else:
        print(f"    Mode {j}: NO fold (monotonic or edge), min at s={s_min:.4f}")

# Track product eigenvalues
print("\n  Product SU(2)xSU(2) eigenvalue tracks (lowest 8):")
tracks_product = np.zeros((len(s_values), N_match))
for si, s in enumerate(s_values):
    e1, m1 = get_sorted_positive_spectrum(*su2_spectra[s])
    e2, m2 = get_sorted_positive_spectrum(*su2_spectra[0.0])
    product_evals = []
    for i in range(min(len(e1), 20)):
        for k in range(min(len(e2), 20)):
            product_evals.append(np.sqrt(e1[i]**2 + e2[k]**2))
    product_evals = np.sort(product_evals)
    tracks_product[si, :] = product_evals[:N_match]

print(f"  {'s':>6s}", end="")
for j in range(N_match):
    print(f"  {'ev_'+str(j):>10s}", end="")
print()
for si, s in enumerate(s_values):
    print(f"  {s:6.2f}", end="")
    for j in range(N_match):
        print(f"  {tracks_product[si,j]:10.6f}", end="")
    print()

# Product fold check
has_fold = False
print("\n  Product fold check:")
for j in range(N_match):
    cs_j = CubicSpline(s_values, tracks_product[:, j])
    s_fine = np.linspace(0.01, 0.49, 1000)
    vals = cs_j(s_fine)
    s_min_idx = np.argmin(vals)
    s_min = s_fine[s_min_idx]
    d2_at_min = cs_j(s_min, 2)
    if 0.02 < s_min < 0.48:
        has_fold = True
        print(f"    Mode {j}: FOLD at s={s_min:.4f}, lambda={vals[s_min_idx]:.6f}, "
              f"d^2lambda/ds^2={d2_at_min:.4f}")
    else:
        trend = "increasing" if tracks_product[-1, j] > tracks_product[0, j] else "decreasing"
        print(f"    Mode {j}: NO fold ({trend}), min at s={s_min:.4f}")


# ---------------------------------------------------------------
# Part 7: Mode-resolved d^2|lambda|/ds^2 (Strutinsky-style)
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 7: Mode-Resolved Curvature Decomposition")
print("=" * 70)

d2_modes_product = np.zeros(N_match)
for j in range(N_match):
    cs_j = CubicSpline(s_values, tracks_product[:, j])
    d2_modes_product[j] = cs_j(0.20, 2)

total_d2_product = 2 * np.sum(d2_modes_product)  # x2 for +/- pairing

print(f"\n  Product SU(2)xSU(2) mode-resolved d^2|lambda|/ds^2 at s=0.20:")
for j in range(N_match):
    print(f"    Mode {j}: d^2/ds^2 = {d2_modes_product[j]:.6f}")
print(f"  Total (x2 for +/-): {total_d2_product:.4f}")
print(f"  Per-mode (positive only): {total_d2_product/(2*N_match):.4f}")

# Compare with SU(3) mode-resolved
su3_mode_d2 = d_su3['mode_d2_contributions']
print(f"\n  SU(3) mode-resolved d^2|lambda|/dtau^2 at tau=0.20:")
branch_labels = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']
for j in range(8):
    print(f"    Mode {j} ({branch_labels[j]}): d^2/dtau^2 = {su3_mode_d2[j]:.6f}")
print(f"  Total (x2 for +/-): {d2S_su3:.4f}")
print(f"  Per-mode: {d2S_su3/16:.4f}")


# ---------------------------------------------------------------
# Part 8: Dimensional Analysis & Additional Checks
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 8: Dimensional Analysis & Additional Checks")
print("=" * 70)

print(f"\n  Dimensional comparison:")
print(f"    SU(3): dim=8, rank=2, spinor_rank=16, #low_modes_singlet=8")
print(f"    SU(2)xSU(2): dim=6, rank=2, spinor_rank=8, #low_modes=8 (matched)")
print(f"    Dimension ratio: 8/6 = {8/6:.3f}")
print(f"    Spinor ratio: 16/8 = 2")
print(f"")
print(f"  Curvature comparison (raw):")
print(f"    SU(3): d^2S = {d2S_su3:.4f}")
print(f"    SU(2)xSU(2): d^2S = {total_d2_product:.4f}")
print(f"    Ratio: {total_d2_product/d2S_su3:.4f}")
print(f"")
print(f"  Curvature comparison (per mode):")
print(f"    SU(3): d^2S/mode = {d2S_su3/16:.4f} (16 modes = 8 pos x 2)")
print(f"    SU(2)xSU(2): d^2S/mode = {total_d2_product/(2*N_match):.4f} ({2*N_match} modes)")
print(f"    Ratio: {(total_d2_product/(2*N_match))/(d2S_su3/16):.4f}")


# ---------------------------------------------------------------
# Part 9: Convergence Check
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 9: Convergence Check")
print("=" * 70)

for N_test in [4, 8, 12, 16, 24]:
    S_test = np.zeros(len(s_values))
    for si, s in enumerate(s_values):
        e1, m1 = get_sorted_positive_spectrum(*su2_spectra[s])
        e2, m2 = get_sorted_positive_spectrum(*su2_spectra[0.0])
        product_evals = []
        for i in range(min(len(e1), 30)):
            for k in range(min(len(e2), 30)):
                product_evals.append(np.sqrt(e1[i]**2 + e2[k]**2))
        product_evals = np.sort(product_evals)
        S_test[si] = 2 * np.sum(product_evals[:N_test])
    cs_test = CubicSpline(s_values, S_test)
    d2_test = cs_test(0.20, 2)
    per_mode_test = d2_test / (2 * N_test)
    print(f"  N_modes={N_test:3d}: d^2S={d2_test:10.4f}, per_mode={per_mode_test:8.4f}")


# ---------------------------------------------------------------
# Part 10: GATE ASSESSMENT
# ---------------------------------------------------------------

print("\n" + "=" * 70)
print("SPEC-35 GATE ASSESSMENT")
print("=" * 70)

d2S_su2xu2 = total_d2_product
print(f"\n  d^2S(SU(2)xSU(2)) at s=0.20 = {d2S_su2xu2:.4f}")
print(f"  d^2S(SU(3)) at tau=0.20 = {d2S_su3:.4f}")
print(f"  Ratio = {d2S_su2xu2/d2S_su3:.4f}")

if d2S_su2xu2 > 10:
    gate_status = "SU(3) NOT SPECIAL (d^2S > 10 threshold)"
    gate_flag = "FAIL_SPECIFICITY"
elif d2S_su2xu2 < 1:
    gate_status = "SU(3) ANOMALOUSLY CURVED (d^2S < 1 threshold)"
    gate_flag = "PASS_SPECIFICITY"
else:
    gate_status = f"INTERMEDIATE: d^2S = {d2S_su2xu2:.2f} (between 1 and 10)"
    gate_flag = "INTERMEDIATE"

print(f"\n  GATE STATUS: {gate_status}")
print(f"  FLAG: {gate_flag}")


# ---------------------------------------------------------------
# Part 11: Plot
# ---------------------------------------------------------------

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: Spectral action S(s) comparison
ax = axes[0, 0]
ax.plot(s_values, S_product_matched, 'bo-', markersize=5,
        label=f'SU(2)xSU(2) ({N_match} modes)')
ax.plot(tau_su3, S_su3_singlet, 'rs-', markersize=5,
        label='SU(3) singlet (8 modes)')
ax.axvline(x=0.20, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Deformation parameter s (or tau)')
ax.set_ylabel('S = sum |lambda_k|')
ax.set_title('Spectral Sum Comparison')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Eigenvalue tracks SU(2) single factor
ax = axes[0, 1]
for j in range(min(6, tracks_su2.shape[1])):
    ax.plot(s_values, tracks_su2[:, j], '-o', markersize=3, label=f'mode {j}')
ax.axvline(x=0.20, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Berger parameter s')
ax.set_ylabel('Eigenvalue lambda')
ax.set_title('SU(2) Berger: Eigenvalue Tracks')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 3: Product eigenvalue tracks
ax = axes[1, 0]
for j in range(min(8, tracks_product.shape[1])):
    ax.plot(s_values, tracks_product[:, j], '-o', markersize=3, label=f'mode {j}')
ax.axvline(x=0.20, color='gray', linestyle='--', alpha=0.5)
ax.set_xlabel('Berger parameter s')
ax.set_ylabel('Product eigenvalue')
ax.set_title('SU(2)xSU(2) Product: Eigenvalue Tracks')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 4: Mode-resolved d^2|lambda|/ds^2 comparison
ax = axes[1, 1]
x_su3 = np.arange(8)
ax.bar(x_su3 - 0.2, su3_mode_d2, width=0.35, color='red', alpha=0.7, label='SU(3)')
x_su2 = np.arange(N_match)
ax.bar(x_su2 + 0.2, d2_modes_product, width=0.35, color='blue', alpha=0.7,
       label='SU(2)xSU(2)')
ax.axhline(y=0, color='black', linewidth=0.5)
ax.set_xlabel('Mode index')
ax.set_ylabel("d^2|lambda|/ds^2")
ax.set_title('Mode-Resolved Curvature at s=0.20')
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

plt.suptitle(f'SPEC-35: Specificity Test SU(2)xSU(2) vs SU(3)\n'
             f'd^2S(SU2xSU2)={d2S_su2xu2:.2f} vs d^2S(SU3)={d2S_su3:.2f}, '
             f'ratio={d2S_su2xu2/d2S_su3:.3f}',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s35_specificity_su2su2.png', dpi=150, bbox_inches='tight')
print("\nPlot saved: tier0-computation/s35_specificity_su2su2.png")


# ---------------------------------------------------------------
# Part 12: Save Data
# ---------------------------------------------------------------

np.savez('tier0-computation/s35_specificity_su2su2.npz',
         s_values=s_values,
         S_product_matched=S_product_matched,
         S_product_full=S_product,
         tracks_product=tracks_product,
         d2_modes_product=d2_modes_product,
         d2S_product_total=np.array([total_d2_product]),
         d2S_product_matched_020=np.array([d2S_matched_020]),
         S_single_su2=S_single,
         tracks_su2=tracks_su2,
         d2S_single_su2_020=np.array([d2S_single_020]),
         d2S_su3=np.array([d2S_su3]),
         S_su3_singlet=S_su3_singlet,
         tau_su3=tau_su3,
         ratio_raw=np.array([d2S_su2xu2 / d2S_su3]),
         ratio_per_mode=np.array([per_mode_ratio]),
         gate_flag=np.array([gate_flag]),
         N_match=np.array([N_match]),
         )
print("Data saved: tier0-computation/s35_specificity_su2su2.npz")


# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------

print(f"\n{'=' * 70}")
print("SUMMARY: SPEC-35")
print(f"{'=' * 70}")
print(f"  d^2S(SU(3), Jensen, singlet) = {d2S_su3:.4f}")
print(f"  d^2S(SU(2)xSU(2), Berger x round, {N_match} modes) = {d2S_su2xu2:.4f}")
print(f"  Raw ratio = {d2S_su2xu2/d2S_su3:.4f}")
print(f"  Per-mode ratio = {per_mode_ratio:.4f}")
print(f"  Gate: {gate_status}")
print(f"  Flag: {gate_flag}")
print(f"")
print(f"  KEY STRUCTURAL FINDING:")
print(f"  SU(3) has the B2 FOLD (eigenvalue minimum at tau=0.190).")
fold_str = "HAS" if has_fold else "DOES NOT HAVE"
print(f"  SU(2)xSU(2) {fold_str} eigenvalue folds in the deformed product spectrum.")
print(f"  The fold drives the van Hove singularity that enhances the BCS DOS.")
print(f"  This is the spectral mechanism that makes SU(3) potentially special.")
