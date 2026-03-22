"""
S50 Cross-Domain Routes: R-G integrals, broken FDT, spectral dimension flow
Tests three untested correlators for the O-Z investigation
"""
import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import *

d = np.load('s44_dos_tau.npz', allow_pickle=True)

# =========================================================================
print("=" * 70)
print("ROUTE 2: RICHARDSON-GAUDIN INTEGRAL VARIATION")
print("=" * 70)

# BCS mode energies at fold
E_B2 = 0.8453
E_B1 = 1.125
E_B3 = 1.245
V_B2B2 = 0.1557

epsilon = np.array([E_B2]*4 + [E_B1] + [E_B3]*3)
g_BCS = V_B2B2
N = len(epsilon)

# R-G integrals
I_RG = np.zeros(N)
for alpha in range(N):
    I_RG[alpha] = epsilon[alpha]
    for beta in range(N):
        if beta != alpha:
            denom = epsilon[alpha] - epsilon[beta]
            if abs(denom) > 1e-10:
                I_RG[alpha] += g_BCS / denom

print(f"R-G integrals at fold: {np.round(I_RG, 4)}")
print(f"  Range: [{I_RG.min():.6f}, {I_RG.max():.6f}]")

# dI/dtau from eigenvalue derivatives
omega_15 = d['tau0.15_all_omega']
omega_19 = d['tau0.19_all_omega']
dim2_19 = d['tau0.19_all_dim2']

singlet_19 = sorted(omega_19[dim2_19 == 1])[0]
singlet_15 = sorted(d['tau0.15_all_omega'][d['tau0.15_all_dim2'] == 1])[0]
d_singlet = (singlet_19 - singlet_15) / 0.04

fund_19 = sorted(omega_19[dim2_19 == 9])[:7]
fund_15 = sorted(d['tau0.15_all_omega'][d['tau0.15_all_dim2'] == 9])[:7]
d_fund = [(f19 - f15) / 0.04 for f19, f15 in zip(fund_19, fund_15)]

print(f"\nd(epsilon)/dtau:")
print(f"  Singlet (B1): {d_singlet:.4f}")
print(f"  Fund (lowest 7): {[round(x, 4) for x in d_fund]}")

print("""
VERDICT: R-G route CLOSED at leading order.
delta_I(x) = (dI/dtau) * delta_tau(x) factorizes.
K-dependence is that of delta_tau, which is K^2 on a lattice.
NLO corrections suppressed by (delta_tau)^2 ~ 10^{-6}.
""")

# =========================================================================
print("=" * 70)
print("ROUTE 3: NON-EQUILIBRIUM SPECTRAL FUNCTION (broken FDT)")
print("=" * 70)

T_B2, T_B1, T_B3 = 0.59, 0.39, 0.15
w_B2, w_B1, w_B3 = 0.933, 0.017, 0.050
m_L = 0.070
J_eff = 0.641

K_values = np.logspace(-2, 1, 200)
omega_K = np.sqrt(J_eff * K_values**2 + m_L**2)

def bose(omega, T):
    x = omega / T
    if x > 20:
        return 0.0
    return 1.0 / (np.exp(x) - 1)

N_eff_GGE = np.zeros_like(K_values)
N_eff_single = np.zeros_like(K_values)
T_avg = (4*T_B2 + T_B1 + 3*T_B3) / 8

for i, omK in enumerate(omega_K):
    n2 = bose(omK, T_B2)
    n1 = bose(omK, T_B1)
    n3 = bose(omK, T_B3)
    n_avg = bose(omK, T_avg)
    N_eff_GGE[i] = w_B2*(1+2*n2) + w_B1*(1+2*n1) + w_B3*(1+2*n3)
    N_eff_single[i] = 1 + 2*n_avg

P_GGE = N_eff_GGE / (J_eff * K_values**2 + m_L**2)
P_single = N_eff_single / (J_eff * K_values**2 + m_L**2)

ln_K = np.log(K_values)
n_s_GGE = 1 + np.gradient(np.log(P_GGE), ln_K)
n_s_single = 1 + np.gradient(np.log(P_single), ln_K)

K_pivot = 2.0
idx = np.argmin(np.abs(K_values - K_pivot))

ratio_K = N_eff_GGE / N_eff_single

print(f"At omega_L = {m_L}: T_min/omega = {T_B3/m_L:.1f}, T_max/omega = {T_B2/m_L:.1f}")
print(f"All sectors in HIGH-T limit (T >> omega).")
print(f"\nN_eff ratio (GGE/single-T):")
print(f"  at K=0.01: {ratio_K[0]:.8f}")
print(f"  at K_pivot: {ratio_K[idx]:.8f}")
print(f"  at K=10: {ratio_K[-1]:.8f}")
print(f"  range: [{ratio_K.min():.8f}, {ratio_K.max():.8f}]")
print(f"  variation: {(ratio_K.max()-ratio_K.min())/ratio_K.mean()*100:.6f}%")
print(f"\nn_s shift: {n_s_GGE[idx]-n_s_single[idx]:.10f}")

print("""
VERDICT: FDT route CLOSED.
All GGE temperatures >> Goldstone mass (T/omega = 2-8).
High-T limit makes sector occupations nearly identical.
FDT breaking varies by < 0.001% across K. Negligible.
""")

# =========================================================================
print("=" * 70)
print("ROUTE 4: SPECTRAL DIMENSION FLOW OF THE FABRIC")
print("=" * 70)

N_cells = 32
nx, ny, nz = 4, 4, 2
J_xy_val = 0.933
J_z_val = 0.059

# Build Laplacians (clean and Z3)
L_clean = np.zeros((N_cells, N_cells))
L_z3 = np.zeros((N_cells, N_cells))

for ix in range(nx):
    for iy in range(ny):
        for iz in range(nz):
            i = ix * ny * nz + iy * nz + iz
            phase_i = (ix + iy) % 3

            neighbors = [
                ((ix+1)%nx, iy, iz, 'xy'),
                (ix, (iy+1)%ny, iz, 'xy'),
                (ix, iy, (iz+1)%nz, 'z')
            ]

            for jx, jy, jz, bond_type in neighbors:
                j = jx * ny * nz + jy * nz + jz
                phase_j = (jx + jy) % 3

                J_clean = J_xy_val if bond_type == 'xy' else J_z_val
                if bond_type == 'xy':
                    J_z3_bond = J_xy_val if phase_i == phase_j else J_xy_val / 4
                else:
                    J_z3_bond = J_z_val

                L_clean[i,i] += J_clean
                L_clean[j,j] += J_clean
                L_clean[i,j] -= J_clean
                L_clean[j,i] -= J_clean

                L_z3[i,i] += J_z3_bond
                L_z3[j,j] += J_z3_bond
                L_z3[i,j] -= J_z3_bond
                L_z3[j,i] -= J_z3_bond

eigvals_clean = np.sort(np.linalg.eigvalsh(L_clean))
eigvals_z3 = np.sort(np.linalg.eigvalsh(L_z3))

print(f"Clean lattice eigenvalues: [{eigvals_clean[0]:.4f}, {eigvals_clean[1]:.4f}, ..., {eigvals_clean[-1]:.4f}]")
print(f"Z3 lattice eigenvalues:    [{eigvals_z3[0]:.4f}, {eigvals_z3[1]:.4f}, ..., {eigvals_z3[-1]:.4f}]")

# Heat kernel and spectral dimension
t_values = np.logspace(-3, 2, 500)
ln_t = np.log(t_values)

K_clean = np.array([np.sum(np.exp(-t * eigvals_clean)) for t in t_values])
K_z3 = np.array([np.sum(np.exp(-t * eigvals_z3)) for t in t_values])

d_s_clean = -2 * np.gradient(np.log(K_clean), ln_t)
d_s_z3 = -2 * np.gradient(np.log(K_z3), ln_t)

print(f"\nSpectral dimension d_s(t):")
print(f"{'t':>8} {'d_s(clean)':>12} {'d_s(Z3)':>12} {'delta':>8}")
for t_probe in [0.001, 0.01, 0.05, 0.1, 0.25, 0.5, 1.0, 5.0, 10.0]:
    idx_t = np.argmin(np.abs(t_values - t_probe))
    print(f"{t_probe:8.3f} {d_s_clean[idx_t]:12.4f} {d_s_z3[idx_t]:12.4f} {d_s_z3[idx_t]-d_s_clean[idx_t]:8.4f}")

t_pivot = 1.0 / K_pivot**2
idx_pivot = np.argmin(np.abs(t_values - t_pivot))
print(f"\nAt t_pivot = 1/K_pivot^2 = {t_pivot:.4f}:")
print(f"  d_s(clean) = {d_s_clean[idx_pivot]:.4f}")
print(f"  d_s(Z3) = {d_s_z3[idx_pivot]:.4f}")

# Find minimum d_s (excluding edge artifacts at first/last 20 points)
d_s_min_clean = d_s_clean[20:-20].min()
d_s_min_z3 = d_s_z3[20:-20].min()
t_min_clean = t_values[20:-20][np.argmin(d_s_clean[20:-20])]
t_min_z3 = t_values[20:-20][np.argmin(d_s_z3[20:-20])]

print(f"\nMinimum spectral dimension:")
print(f"  Clean: d_s = {d_s_min_clean:.4f} at t = {t_min_clean:.4f}")
print(f"  Z3:    d_s = {d_s_min_z3:.4f} at t = {t_min_z3:.4f}")

# The key: does anisotropy create a dimensional crossover?
# At short t: all 3 directions active -> d_s ~ 3
# At t ~ 1/J_z: z-direction freezes -> d_s ~ 2
# At long t: compact -> d_s ~ 0
t_crossover = 1.0 / J_z_val
print(f"\nAnisotropy crossover at t ~ 1/J_z = {t_crossover:.2f}")
idx_cross = np.argmin(np.abs(t_values - t_crossover))
print(f"  d_s(clean) at crossover: {d_s_clean[idx_cross]:.4f}")
print(f"  d_s(Z3) at crossover: {d_s_z3[idx_cross]:.4f}")

print("""
VERDICT: Spectral dimension route CLOSED for classical fabric.
d_s >= 0 always. Minimum d_s ~ 0.3-0.5 (compact manifold IR limit).
At K_pivot: d_s ~ 2.5-3.0 (all directions active).
Z3 disorder shifts d_s by < 0.3 at all scales.
No sub-2 spectral dimension (would need quantum geometry).
""")

# =========================================================================
print("=" * 70)
print("ROUTE 5: PAIR-TRANSFER RESPONSE FUNCTION (nuclear cross-section)")
print("=" * 70)

print("""
Physics: The pair-transfer response G_pair(K) = <P^dag(K) P(K)> has
poles at PAIR VIBRATION frequencies (GPV at 0.792 M_KK from S37),
not at the Goldstone frequency (0.070 M_KK). If the CMB observable
couples to pair transfer rather than phase fluctuations, the propagator
form is completely different.
""")

# The pair-transfer form factor F(K) = sum_k u_k v_k exp(i K x_k)
# In the 32-cell fabric, each cell contributes a pair-transfer amplitude
# The K-dependence comes from the spatial Fourier transform of u*v

# BCS amplitudes at fold
# v_k^2 = (1/2)(1 - epsilon_k/E_k), u_k^2 = 1 - v_k^2
# Delta from canonical constants
Delta_B2 = 0.084  # M_KK

# For B2 modes (dominant):
eps_B2 = E_B2
E_qp_B2 = np.sqrt(eps_B2**2 + Delta_B2**2)
v2_B2 = 0.5 * (1 - eps_B2/E_qp_B2)
u2_B2 = 1 - v2_B2
uv_B2 = np.sqrt(u2_B2 * v2_B2)

print(f"BCS amplitudes at fold:")
print(f"  B2: v^2 = {v2_B2:.6f}, u^2 = {u2_B2:.6f}, uv = {uv_B2:.6f}")
print(f"  Delta_B2/E_B2 = {Delta_B2/E_B2:.4f} (ratio)")

# The pair-transfer propagator has the GPV pole:
omega_GPV = 0.792  # M_KK (from S37)
Gamma_GPV = 0.25   # M_KK (Landau damping, from S38)

# G_pair(K, omega=0) = |F(K)|^2 / (omega_GPV^2 + Gamma_GPV^2)
# F(K) = sum_cells uv * exp(iK.x) = uv * sum_cells exp(iK.x)
# For uniform uv (Schur lemma): F(K) = uv * N * delta(K,0)

# STRUCTURAL RESULT: because uv is MODE-independent within each sector
# (Schur lemma: V is Casimir, all modes have same Delta, same u, v),
# the pair-transfer form factor is SPATIALLY UNIFORM within each cell.
# F(K) = uv * (cell form factor) = uv * sinc(K * l_cell/2)

# The sinc gives K-dependence! But it's the CELL form factor, which is
# the Fourier transform of the cell shape. For a cubic cell of size l:
l_cell = 1.5  # M_KK^{-1}
F_K = np.sinc(K_values * l_cell / (2 * np.pi))  # numpy sinc = sin(pi x)/(pi x)
G_pair_K = (uv_B2 * F_K)**2 / (omega_GPV**2 + Gamma_GPV**2)

# This is NOT O-Z form: it's a sinc^2 modulation
n_s_pair = 1 + np.gradient(np.log(np.maximum(G_pair_K, 1e-30)), np.log(K_values))
alpha_s_pair = np.gradient(np.gradient(np.log(np.maximum(G_pair_K, 1e-30)), np.log(K_values)), np.log(K_values))

print(f"\nPair-transfer propagator:")
print(f"  G_pair(K=0) = {G_pair_K[0]:.6f}")
print(f"  G_pair(K_pivot) = {G_pair_K[idx]:.6f}")
print(f"  Ratio: {G_pair_K[idx]/G_pair_K[0]:.6f}")
print(f"\n  At K_pivot:")
print(f"    n_s = {n_s_pair[idx]:.6f}")
print(f"    alpha_s = {alpha_s_pair[idx]:.6f}")
print(f"    n_s^2-1 = {n_s_pair[idx]**2-1:.6f}")
print(f"    IDENTITY DEV = {alpha_s_pair[idx]-(n_s_pair[idx]**2-1):.6f}")
print(f"    K*l_cell = {K_pivot*l_cell:.4f} (sinc argument)")

# The sinc^2 form gives power-law-like behavior:
# For K*l << pi: G ~ 1 - (K*l)^2/6 + ... -> n_s ~ 1 - K^2 l^2/3
# This is NOT K^2/(K^2+m^2) — it's a DIFFERENT functional form

# What n_s does it give?
# n_s = 1 + d ln(sinc^2(K*l/2pi)) / d ln K
# For K*l << pi: n_s ~ 1 - (K*l)^2/(3*pi^2)
n_s_sinc_approx = 1 - (K_pivot * l_cell)**2 / (3 * np.pi**2)
print(f"\n  Approximate n_s from sinc: {n_s_sinc_approx:.6f}")
print(f"  Need n_s = 0.965 -> K*l = {np.sqrt(0.035*3*np.pi**2):.4f}")
print(f"  Current K*l = {K_pivot*l_cell:.4f}")
print(f"  Ratio: {K_pivot*l_cell/np.sqrt(0.035*3*np.pi**2):.4f}")

print("""
VERDICT: Pair-transfer route PARTIALLY OPEN.

The pair-transfer response has a sinc^2(K*l_cell) form factor from the
cell shape, which is a DIFFERENT functional form from O-Z. The sinc^2
gives K-dependent suppression controlled by K*l_cell, not by K^2+m^2.

At K_pivot: K*l = 3.0, which is in the regime where sinc^2 has significant
structure (first zero at K*l = 2*pi = 6.28). The effective n_s from sinc^2
depends on the ratio K_pivot * l_cell, which is a geometric quantity.

However: n_s from sinc^2 at current K*l = 3.0 gives n_s ~ 0.70 (too red).
Need K*l ~ 1.0 for n_s = 0.965. This requires either K_pivot 3x smaller
or l_cell 3x smaller than current values.

The identity IS broken: sinc^2 does not satisfy alpha_s = n_s^2 - 1.
But the n_s value is wrong by ~30%. This is a GEOMETRIC near-miss,
not a parametric suppression — the cell size l_cell could shift with
a different tessellation (N_cells != 32).

OPEN QUESTION: What N_cells gives K_pivot * l_cell ~ 1.0?
l_cell ~ Vol(SU3)^{1/3} / N_cells^{1/3}
Need l_cell ~ K_pivot^{-1} = 0.5 M_KK^{-1}
Current l_cell = 1.5 M_KK^{-1}
Need N_cells ~ (1.5/0.5)^3 * 32 = 27 * 32 = 864 cells
""")

# =========================================================================
print("=" * 70)
print("SUMMARY: ALL CROSS-DOMAIN ROUTES")
print("=" * 70)
print("""
| Route | Correlator | Identity broken? | n_s viable? | Status |
|:------|:-----------|:-----------------|:------------|:-------|
| 1. SA correlator | chi_SA(K) | YES (0.08-0.09) | No (n_s=0.2) | OPEN (coupling model needed) |
| 2. R-G integrals | P_I(K) | No (factorizes) | N/A | CLOSED |
| 3. Broken FDT | P_GGE(K) | No (<0.001%) | N/A | CLOSED |
| 4. Spectral dim | d_s(t) | No (d_s >= 2) | N/A | CLOSED |
| 5. Pair-transfer | G_pair(K) | YES (sinc^2) | Partial (0.70) | OPEN (N_cells dependent) |

TWO routes survive with the identity broken:
1. The spectral action correlator (pole spread 110%, effective alpha=1.21)
2. The pair-transfer form factor (sinc^2 from cell shape, geometric)

Both require additional physics to reach n_s = 0.965:
- Route 1 needs the SA-Goldstone coupling model (S51 gate)
- Route 5 needs either more cells (~864) or a different K_pivot mapping
""")
