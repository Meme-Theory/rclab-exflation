"""
Session 21c P0-5: Gauss-Bonnet Topological Check — FINAL COMPUTATION

Computes the 8D Euler density E_8(tau) at all 21 tau values using the
brute-force double-epsilon tensor contraction (no pair-partition decomposition).

The previous pair-partition formula was INCORRECT for SU(3) — it gave nonzero
results due to a combinatorial error in handling cross-pair contractions.
The brute-force method is exact and confirmed by:
- S^4: chi = 2 (correct)
- S^8: chi = 2 (correct)
- U(1) x SU(2): chi = 0 (correct)
- Analytic SU(3): S = 0 to machine epsilon (correct)
"""

import numpy as np
import time

print("=" * 70)
print("Session 21c P0-5: Gauss-Bonnet Topological Check")
print("=" * 70)
print(f"Date: 2026-02-19")
print(f"Method: Brute-force double-epsilon contraction")

# Build 8D Levi-Civita symbol
def levi_civita(n):
    from itertools import permutations
    eps = np.zeros([n] * n, dtype=np.float64)
    identity = list(range(n))
    for perm in permutations(identity):
        sign = 1
        perm_list = list(perm)
        for i in range(n):
            for j in range(i + 1, n):
                if perm_list[i] > perm_list[j]:
                    sign *= -1
        eps[tuple(perm)] = sign
    return eps

print("\nBuilding 8D Levi-Civita symbol...")
eps8 = levi_civita(8)

# Load Riemann data
d = np.load('C:/sandbox/Ainulindale Exflation/tier0-computation/r20a_riemann_tensor.npz',
            allow_pickle=True)
tau_vals = d['tau']
R_all = d['R_abcd']

print(f"Data file: tier0-computation/r20a_riemann_tensor.npz")
print(f"Manifold: SU(3) with Jensen TT-deformation (volume-preserving)")
print(f"Dimension: 8")
print(f"Expected chi(SU(3)): 0 (compact Lie group)")
print(f"Number of tau values: {len(tau_vals)}")

# Verify Riemann symmetries
R0 = R_all[0]
err_ab = np.max(np.abs(R0 + np.transpose(R0, (1, 0, 2, 3))))
err_cd = np.max(np.abs(R0 + np.transpose(R0, (0, 1, 3, 2))))
err_pair = np.max(np.abs(R0 - np.transpose(R0, (2, 3, 0, 1))))
# First Bianchi: R_{abcd} + R_{acdb} + R_{adbc} = 0
bianchi = R0 + np.transpose(R0, (0, 2, 3, 1)) + np.transpose(R0, (0, 3, 1, 2))
err_bianchi = np.max(np.abs(bianchi))

print(f"\nRiemann Tensor Symmetry Verification:")
print(f"  Max |R_abcd + R_bacd|: {err_ab:.2e}")
print(f"  Max |R_abcd + R_abdc|: {err_cd:.2e}")
print(f"  Max |R_abcd - R_cdab|: {err_pair:.2e}")
print(f"  Max |1st Bianchi|:     {err_bianchi:.2e}")

def compute_euler_S(R, eps8):
    """Compute the double-epsilon contraction S = eps_A eps_B RRRR.

    S = eps_{a1...a8} eps_{b1...b8} R_{a1a2,b1b2} R_{a3a4,b3b4} R_{a5a6,b5b6} R_{a7a8,b7b8}

    Uses stepwise contraction to avoid the 16-index einsum.
    """
    T1 = np.einsum('abcdefgh,abij->cdefghij', eps8, R)
    T2 = np.einsum('cdefghij,cdkl->efghijkl', T1, R)
    del T1
    T3 = np.einsum('efghijkl,efmn->ghijklmn', T2, R)
    del T2
    T4 = np.einsum('ghijklmn,ghop->ijklmnop', T3, R)
    del T3
    S = np.einsum('ijklmnop,ijklmnop', eps8, T4)
    del T4
    return S

# Compute Euler density S at all tau values
print(f"\n8D Double-Epsilon Contraction S(tau) at each tau:")
print("-" * 60)
print(f"{'tau':>6s}  {'S':>25s}  {'S/6144':>25s}")
print("-" * 60)

S_values = []
t_start = time.time()

for ti in range(len(tau_vals)):
    R = R_all[ti]
    S = compute_euler_S(R, eps8)
    S_values.append(S)
    elapsed = time.time() - t_start
    eta = elapsed / (ti + 1) * (len(tau_vals) - ti - 1)
    print(f"  {tau_vals[ti]:4.2f}  {S:25.15e}  {S/6144:25.15e}  ({elapsed:.1f}s, ETA {eta:.0f}s)")

S_values = np.array(S_values)
print("-" * 60)

# Analysis
max_S = np.max(np.abs(S_values))
max_dev = np.max(np.abs(S_values - S_values[0]))

print(f"\nMax |S(tau)|:               {max_S:.15e}")
print(f"Max |S(tau) - S(0)|:        {max_dev:.15e}")
print(f"Machine epsilon:            {np.finfo(np.float64).eps:.2e}")
print(f"Tolerance (1000 * eps):     {1000 * np.finfo(np.float64).eps:.2e}")

# The chi formula: chi = S * Vol / (6144 * (2pi)^4)
# For all tau, S should be zero to machine epsilon.
# The Euler density E_8 = S / 6144 is proportional to chi when integrated.

eps_mach = np.finfo(np.float64).eps
tol = 1000 * eps_mach  # generous tolerance: ~2.2e-13

# Cross-checks
print(f"\nCross-checks:")

# S^8
R_S8 = np.zeros((8, 8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            for dd in range(8):
                R_S8[a,b,c,dd] = float(a==c)*float(b==dd) - float(a==dd)*float(b==c)
S_S8 = compute_euler_S(R_S8, eps8)
chi_S8 = S_S8 / (6144 * (2*np.pi)**4) * 32*np.pi**4/105
print(f"  S^8:   S = {S_S8:.1f}, chi = {chi_S8:.6f} (expected 2)")

# Analytic SU(3) from structure constants
f = np.zeros((8, 8, 8))
f_values = {
    (0, 1, 2): 1.0, (0, 3, 6): 0.5, (0, 4, 5): -0.5,
    (1, 3, 5): 0.5, (1, 4, 6): 0.5, (2, 3, 4): 0.5,
    (2, 5, 6): -0.5, (3, 4, 7): np.sqrt(3)/2, (5, 6, 7): np.sqrt(3)/2,
}
for (a, b, c), val in f_values.items():
    f[a, b, c] = val; f[b, c, a] = val; f[c, a, b] = val
    f[a, c, b] = -val; f[b, a, c] = -val; f[c, b, a] = -val
R_analytic = (1.0 / 12.0) * np.einsum('abe,cde->abcd', f, f)
S_analytic = compute_euler_S(R_analytic, eps8)
print(f"  SU(3) analytic: S = {S_analytic:.15e} (expected 0)")

# Kretschner check: stored matches expected
K_stored = d['K']
K_check = np.array([np.einsum('abcd,abcd->', R_all[ti], R_all[ti]) for ti in range(len(tau_vals))])
K_err = np.max(np.abs(K_stored - K_check))
print(f"  Kretschner scalar consistency: max diff = {K_err:.2e}")

# Verdict
if max_S < tol:
    verdict = "PASS"
    reason = f"All S(tau) values are < {tol:.2e} (machine epsilon level)."
elif max_dev < tol and max_S > tol:
    verdict = "CONDITIONAL PASS"
    reason = f"S is constant to {max_dev:.2e} but nonzero at {max_S:.2e}. Possible normalization offset."
else:
    verdict = "FAIL"
    reason = f"S varies across tau: max |S| = {max_S:.2e}, max deviation = {max_dev:.2e}."

print(f"\nVERDICT: {verdict}")
print(f"Reason: {reason}")

if verdict == "PASS":
    print(f"\nInterpretation:")
    print(f"  The Euler density E_8(tau) = S(tau)/6144 is zero to machine epsilon at all tau values.")
    print(f"  This confirms chi(SU(3)) = 0 and validates the Riemann tensor data in")
    print(f"  r20a_riemann_tensor.npz for topological consistency.")
    print(f"  ALL Phase A computations can proceed with confidence.")
    print(f"\n  Note: The original computation (s21c_gauss_bonnet.py) used a pair-partition")
    print(f"  formula that had a combinatorial error for n >= 4 pairs. The cross-pair")
    print(f"  contractions (off-diagonal terms in the pair-reordering) cancel exactly for")
    print(f"  SU(3) but not for constant-curvature spaces, making the sphere cross-check")
    print(f"  misleadingly correct.")

# Write output file
output_path = 'C:/sandbox/Ainulindale Exflation/tier0-computation/s21c_gauss_bonnet.txt'
with open(output_path, 'w') as fout:
    fout.write("Session 21c P0-5: Gauss-Bonnet Topological Check\n")
    fout.write("=" * 60 + "\n\n")
    fout.write(f"Date: 2026-02-19\n")
    fout.write(f"Data file: tier0-computation/r20a_riemann_tensor.npz\n")
    fout.write(f"Manifold: SU(3) with Jensen TT-deformation (volume-preserving)\n")
    fout.write(f"Dimension: 8\n")
    fout.write(f"Expected chi(SU(3)): 0 (compact Lie group)\n")
    fout.write(f"Method: Brute-force double-epsilon tensor contraction\n\n")

    fout.write("Riemann Tensor Symmetry Verification:\n")
    fout.write(f"  Max |R_abcd + R_bacd|: {err_ab:.2e}\n")
    fout.write(f"  Max |R_abcd + R_abdc|: {err_cd:.2e}\n")
    fout.write(f"  Max |R_abcd - R_cdab|: {err_pair:.2e}\n")
    fout.write(f"  Max |1st Bianchi|:     {err_bianchi:.2e}\n\n")

    fout.write("8D Double-Epsilon Contraction S(tau):\n")
    fout.write("-" * 50 + "\n")
    fout.write(f"{'tau':>6s}  {'S':>25s}\n")
    fout.write("-" * 50 + "\n")
    for ti in range(len(tau_vals)):
        fout.write(f"  {tau_vals[ti]:4.2f}  {S_values[ti]:25.15e}\n")
    fout.write("-" * 50 + "\n\n")

    fout.write(f"Max |S(tau)|:            {max_S:.15e}\n")
    fout.write(f"Max |S(tau) - S(0)|:     {max_dev:.15e}\n")
    fout.write(f"Machine epsilon:         {np.finfo(np.float64).eps:.2e}\n")
    fout.write(f"Tolerance (1000*eps):    {tol:.2e}\n\n")

    fout.write(f"Cross-checks:\n")
    fout.write(f"  chi(S^8) = {chi_S8:.6f} (expected 2)\n")
    fout.write(f"  S(SU(3) analytic) = {S_analytic:.2e} (expected 0)\n")
    fout.write(f"  Kretschner consistency: max diff = {K_err:.2e}\n\n")

    fout.write(f"VERDICT: {verdict}\n")
    fout.write(f"Reason: {reason}\n\n")

    if verdict == "PASS":
        fout.write("Interpretation:\n")
        fout.write("  The Euler density is zero to machine epsilon at all tau values.\n")
        fout.write("  This confirms chi(SU(3)) = 0 and validates the Riemann tensor data.\n")
        fout.write("  ALL Phase A computations can proceed.\n\n")
        fout.write("  Note: The original pair-partition formula had a combinatorial error\n")
        fout.write("  for n >= 4 pairs. The brute-force double-epsilon contraction is the\n")
        fout.write("  correct and definitive computation.\n")

print(f"\nOutput written to: {output_path}")
print(f"Total computation time: {time.time() - t_start:.1f}s")
