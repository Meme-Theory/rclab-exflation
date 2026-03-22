"""
COLLECTIVE-NS-45 v2: Pair creation from CONDENSATE DESTRUCTION at the fold.

Physics: The system arrives at tau=0.19 (fold). BCS condensate forms (Delta=0.770).
The quench destroys the condensate (P_exc=1.000, S38). Pair creation from
the sudden removal of the BCS gap at FIXED tau=0.19.

Pre-quench:  E_k = sqrt(lambda_k^2 + Delta^2)  (BCS-dressed)
Post-quench: E_k = |lambda_k|                    (undressed, Delta->0)

The spectral distribution of created pairs depends on how much each mode's
energy changes when the gap is removed: modes near the gap edge (lambda ~ Delta)
change the most.
"""
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# Load data
occ = np.load('tier0-computation/s45_occ_spectral.npz', allow_pickle=True)
bcs = np.load('tier0-computation/s38_cc_instanton.npz', allow_pickle=True)
naz = np.load('tier0-computation/s45_occ_spectral_crosscheck.npz', allow_pickle=True)
hf = np.load('tier0-computation/s42_hauser_feshbach.npz', allow_pickle=True)

# Eigenvalues at fold (1232 matrix eigenvalues, positive branch)
lambda_k = occ['evals_tau0.190']  # |lambda_k| at fold
d_k = occ['weights_tau0.190']     # PW degeneracies dim(p,q)^2
Delta = float(bcs['Delta_0'])      # 0.770 M_KK

# Multi-component gaps from Nazarewicz (more physical than uniform)
Delta_mc = naz['Delta_mc_fold']  # [B2, B2, B2, B2, B1, B3, B3, B3] = 8 modes
# But we need gaps for all 1232 eigenvalues. Use sector-dependent gaps.
# Sector labels from HF
sector_labels = hf['sector_labels']  # (9, 2) array of (p,q) pairs

print("=" * 70)
print("COLLECTIVE-NS-45 v2: Condensate Destruction at Fixed tau=0.19")
print("=" * 70)
print(f"  Eigenvalues: {len(lambda_k)} (positive branch)")
print(f"  Delta (uniform): {Delta:.4f} M_KK")
print(f"  Delta (multi-comp): B2={Delta_mc[0]:.4f}, B1={Delta_mc[4]:.4f}, B3={Delta_mc[5]:.4f}")

# ============================================================
# 1. BCS-DRESSED vs UNDRESSED energies at fold
# ============================================================
# Pre-quench: E_dressed = sqrt(lambda^2 + Delta^2) with mu=0
# Post-quench: E_undressed = |lambda|

E_dressed = np.sqrt(lambda_k**2 + Delta**2)
E_undressed = lambda_k  # = |lambda_k| since all positive

# Bogoliubov coefficient for sudden gap removal
# |beta_k|^2 = ((E_dressed - E_undressed) / (2 * sqrt(E_dressed * E_undressed)))^2
beta2 = ((E_dressed - E_undressed) / (2 * np.sqrt(E_dressed * E_undressed)))**2

print(f"\n--- Bogoliubov Coefficients (condensate destruction) ---")
print(f"  |beta|^2 range: [{beta2.min():.6e}, {beta2.max():.6e}]")
print(f"  |beta|^2 mean:  {beta2.mean():.6e}")
print(f"  |beta|^2 at gap edge (lambda=0.820): {beta2[np.argmin(np.abs(lambda_k - 0.820))]:.6e}")
print(f"  |beta|^2 at mid-band (lambda=1.2):   {beta2[np.argmin(np.abs(lambda_k - 1.2))]:.6e}")
print(f"  |beta|^2 at band top (lambda=2.06):  {beta2[np.argmin(np.abs(lambda_k - 2.06))]:.6e}")

# CROSS-CHECK: beta=0 if Delta=0 (no condensate = no pairs)
beta2_check = ((np.sqrt(lambda_k**2 + 0**2) - lambda_k) / (2 * np.sqrt(np.sqrt(lambda_k**2) * lambda_k)))**2
print(f"  Cross-check (Delta=0): max |beta|^2 = {beta2_check.max():.2e} (should be 0)")

# ============================================================
# 2. PAIR CREATION depends on Delta/lambda ratio
# ============================================================
# |beta_k|^2 = ((sqrt(1 + (Delta/lambda)^2) - 1) / (2 * (1 + (Delta/lambda)^2)^(1/4)))^2
# For Delta/lambda >> 1: |beta|^2 -> 1/4 (maximal pair creation)
# For Delta/lambda << 1: |beta|^2 -> (Delta/(2*lambda))^4 (quartic suppression)

x = Delta / lambda_k  # the key ratio
print(f"\n--- Delta/lambda ratio ---")
print(f"  Range: [{x.min():.4f}, {x.max():.4f}]")
print(f"  Mean:  {x.mean():.4f}")
print(f"  At gap edge: Delta/lambda = {Delta/0.820:.4f}")
print(f"  At band top: Delta/lambda = {Delta/2.06:.4f}")

# Analytic form: beta^2 = ((sqrt(1+x^2) - 1)/(2*(1+x^2)^(1/4)))^2
# Simplified: for x << 1, beta^2 ~ x^4/16
# For x ~ 1, beta^2 ~ 0.04
# For x >> 1, beta^2 -> 0.25

# ============================================================
# 3. ASSIGN 4D WAVENUMBER from Casimir
# ============================================================
# Each eigenvalue comes from a (p,q) sector with Casimir C_2(p,q)
# We need to map the 1232 eigenvalues to their (p,q) labels
# The sectors are: (0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)+(1,2)
# With max_pq_sum = 3

# Reconstruct sector assignment from eigenvalue count per sector
# From the Dirac spectrum computation: each sector (p,q) contributes
# n_eigenvalues = 2 * (p+q+1) positive eigenvalues (from the matrix structure)
# PW multiplicity = dim(p,q)^2

# Actually, we can use the eigenvalue + weight to infer the Casimir
# C_2(p,q) = (p^2 + q^2 + pq + 3*(p+q)) / 3
sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)]
casimir = []
dim_sq = []
for p, q in sectors:
    c2 = (p**2 + q**2 + p*q + 3*(p+q)) / 3
    d = ((p+1)*(q+1)*(p+q+2)//2)**2
    casimir.append(c2)
    dim_sq.append(d)

casimir = np.array(casimir)
dim_sq = np.array(dim_sq)

print(f"\n--- Sector Casimir and Dimensions ---")
for i, (p,q) in enumerate(sectors):
    print(f"  ({p},{q}): C_2 = {casimir[i]:.4f}, dim^2 = {dim_sq[i]}")

# Map eigenvalues to wavenumber k = sqrt(C_2)
# Each eigenvalue has a weight d_k = dim(p,q)^2 which tells us the sector
# Build the mapping: for each of the 1232 eigenvalues, find its sector
k_4d = np.zeros(len(lambda_k))
sector_id = np.zeros(len(lambda_k), dtype=int)

idx = 0
for s_idx, (p, q) in enumerate(sectors):
    d = dim_sq[s_idx]
    c2 = casimir[s_idx]
    # Find eigenvalues with this weight
    mask = np.abs(d_k - d) < 0.5
    k_4d[mask] = np.sqrt(c2) if c2 > 0 else 0.0
    sector_id[mask] = s_idx

print(f"\n  k_4d assigned: {np.unique(k_4d)}")

# ============================================================
# 4. POWER SPECTRUM P(k) = sum d_k |beta_k|^2 at each k
# ============================================================
unique_k = np.unique(k_4d)
P_k = np.zeros(len(unique_k))
N_modes = np.zeros(len(unique_k))
beta2_mean_k = np.zeros(len(unique_k))

for i, kv in enumerate(unique_k):
    mask = np.abs(k_4d - kv) < 1e-6
    P_k[i] = np.sum(d_k[mask] * beta2[mask])
    N_modes[i] = np.sum(d_k[mask])
    beta2_mean_k[i] = np.mean(beta2[mask])

print(f"\n--- Power Spectrum P(k) = sum d_k |beta_k|^2 ---")
print(f"{'k':>8s} {'P(k)':>12s} {'N_modes':>10s} {'<|b|^2>':>12s}")
for i in range(len(unique_k)):
    print(f"{unique_k[i]:8.4f} {P_k[i]:12.4f} {N_modes[i]:10.0f} {beta2_mean_k[i]:12.6e}")

# ============================================================
# 5. EXTRACT n_s (skip k=0 singlet)
# ============================================================
k_nonzero = unique_k[unique_k > 0]
P_nonzero = P_k[unique_k > 0]

lnk = np.log(k_nonzero)
lnP = np.log(P_nonzero)

coeffs = np.polyfit(lnk, lnP, 1)
ns = coeffs[0] + 1

pred = np.polyval(coeffs, lnk)
ss_res = np.sum((lnP - pred)**2)
ss_tot = np.sum((lnP - np.mean(lnP))**2)
R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

print(f"\n--- SPECTRAL TILT ---")
print(f"  n_s - 1 = {coeffs[0]:.4f}")
print(f"  n_s     = {ns:.4f}")
print(f"  R^2     = {R2:.4f}")

# ============================================================
# 6. DECOMPOSE: why is the tilt what it is?
# ============================================================
# |beta_k|^2 depends on Delta/lambda_k — DECREASING with lambda (more pairs near gap edge)
# d_k depends on dim(p,q)^2 — INCREASING with Casimir (Weyl's law)
# P(k) = d_k * beta^2 — the competition determines the tilt

print(f"\n--- Decomposition ---")
print(f"  |beta|^2 scaling: modes near gap edge get more pairs")
print(f"  d_k scaling: higher representations have more modes (Weyl)")
print(f"  {'k':>8s} {'<|b|^2>':>12s} {'N_modes':>10s} {'product':>12s}")
for i in range(len(unique_k)):
    if unique_k[i] > 0:
        print(f"  {unique_k[i]:8.4f} {beta2_mean_k[i]:12.6e} {N_modes[i]:10.0f} {P_k[i]:12.4f}")

# Separate contributions
# beta^2 alone (no degeneracy weighting):
beta2_at_k = beta2_mean_k[unique_k > 0]
lnb = np.log(beta2_at_k)
cb = np.polyfit(lnk, lnb, 1)
print(f"\n  |beta|^2 power law: exponent = {cb[0]:.4f}")

# Degeneracy alone:
N_at_k = N_modes[unique_k > 0]
lnN = np.log(N_at_k)
cn = np.polyfit(lnk, lnN, 1)
print(f"  N_modes power law: exponent = {cn[0]:.4f}")
print(f"  Net: {cb[0]:.4f} + {cn[0]:.4f} = {cb[0]+cn[0]:.4f} (should be ~ n_s - 1 = {coeffs[0]:.4f})")

# ============================================================
# 7. SENSITIVITY: Delta variation
# ============================================================
print(f"\n--- Sensitivity to Delta ---")
for Delta_test in [0.385, 0.500, 0.770, 1.000, 1.500]:
    E_d = np.sqrt(lambda_k**2 + Delta_test**2)
    b2 = ((E_d - lambda_k) / (2 * np.sqrt(E_d * lambda_k)))**2
    P_test = np.zeros(len(unique_k))
    for i, kv in enumerate(unique_k):
        mask = np.abs(k_4d - kv) < 1e-6
        P_test[i] = np.sum(d_k[mask] * b2[mask])
    P_nz = P_test[unique_k > 0]
    if np.all(P_nz > 0):
        c_test = np.polyfit(np.log(k_nonzero), np.log(P_nz), 1)
        print(f"  Delta = {Delta_test:.3f}: n_s = {c_test[0]+1:.4f}")

# ============================================================
# 8. GATE VERDICT
# ============================================================
print(f"\n{'='*70}")
print(f"GATE VERDICT: COLLECTIVE-NS-45 v2")
print(f"{'='*70}")
print(f"  n_s = {ns:.4f} (R^2 = {R2:.4f})")
if 0.955 <= ns <= 0.975:
    verdict = "PASS"
elif 0.80 <= ns <= 1.10:
    verdict = "INFO (extended window)"
else:
    verdict = f"OUTSIDE extended window [0.80, 1.10]"
print(f"  Verdict: {verdict}")
print(f"\n  Physics: pair creation from condensate destruction at tau=0.19")
print(f"  Pre-quench: E_k = sqrt(lambda_k^2 + Delta^2), Delta={Delta:.3f}")
print(f"  Post-quench: E_k = |lambda_k| (Delta -> 0)")
print(f"  |beta_k|^2 scaling: {cb[0]:.2f} (decreasing with k, more pairs near gap)")
print(f"  Degeneracy scaling: {cn[0]:.2f} (increasing with k, Weyl law)")
print(f"  Net tilt: {cb[0]:.2f} + {cn[0]:.2f} = {coeffs[0]:.2f}")

# ============================================================
# 9. PLOT
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle('COLLECTIVE-NS-45 v2: Condensate Destruction at Fold', fontsize=14)

# Panel 1: beta^2 vs lambda
ax = axes[0, 0]
ax.semilogy(lambda_k, beta2, 'b.', ms=1, alpha=0.3)
# Analytic curve
lam_smooth = np.linspace(lambda_k.min(), lambda_k.max(), 200)
x_smooth = Delta / lam_smooth
b2_smooth = ((np.sqrt(1 + x_smooth**2) - 1) / (2 * (1 + x_smooth**2)**0.25))**2
ax.semilogy(lam_smooth, b2_smooth, 'r-', lw=2, label=r'Analytic')
ax.set_xlabel(r'$|\lambda_k|$ (M_KK)')
ax.set_ylabel(r'$|\beta_k|^2$')
ax.set_title('Pair creation vs eigenvalue')
ax.legend()

# Panel 2: Delta/lambda ratio
ax = axes[0, 1]
ax.hist(x, bins=50, weights=d_k, color='steelblue', edgecolor='k', lw=0.5)
ax.axvline(1.0, color='r', ls='--', label=r'$\Delta/\lambda = 1$')
ax.set_xlabel(r'$\Delta/|\lambda_k|$')
ax.set_ylabel('Weighted count')
ax.set_title(r'Gap/eigenvalue ratio distribution')
ax.legend()

# Panel 3: P(k) power spectrum
ax = axes[0, 2]
ax.loglog(k_nonzero, P_nonzero, 'ko-', ms=8, label='P(k)')
k_fit_line = np.linspace(k_nonzero.min(), k_nonzero.max(), 50)
ax.loglog(k_fit_line, np.exp(np.polyval(coeffs, np.log(k_fit_line))), 'r--',
          label=f'n_s = {ns:.3f}')
ax.set_xlabel('k (Casimir)')
ax.set_ylabel('P(k)')
ax.set_title(f'Power Spectrum (n_s = {ns:.3f}, R² = {R2:.3f})')
ax.legend()

# Panel 4: n_s fit
ax = axes[1, 0]
ax.plot(lnk, lnP, 'ko', ms=8)
ax.plot(lnk, np.polyval(coeffs, lnk), 'r--', lw=2)
ax.set_xlabel('ln k')
ax.set_ylabel('ln P(k)')
ax.set_title(f'Linear fit: slope = {coeffs[0]:.3f}')

# Panel 5: beta^2 and N_modes decomposition
ax = axes[1, 1]
ax2 = ax.twinx()
ax.semilogy(k_nonzero, beta2_at_k, 'bs-', ms=6, label=r'$\langle|\beta|^2\rangle$')
ax2.semilogy(k_nonzero, N_at_k, 'r^-', ms=6, label='N_modes')
ax.set_xlabel('k')
ax.set_ylabel(r'$\langle|\beta|^2\rangle$', color='b')
ax2.set_ylabel('N_modes', color='r')
ax.set_title('Decomposition: pairs vs modes')
ax.legend(loc='upper left')
ax2.legend(loc='upper right')

# Panel 6: Sensitivity to Delta
ax = axes[1, 2]
deltas = np.linspace(0.1, 2.0, 50)
ns_vals = []
for dt in deltas:
    E_d = np.sqrt(lambda_k**2 + dt**2)
    b2t = ((E_d - lambda_k) / (2 * np.sqrt(E_d * lambda_k)))**2
    P_t = np.zeros(len(unique_k))
    for i, kv in enumerate(unique_k):
        mask = np.abs(k_4d - kv) < 1e-6
        P_t[i] = np.sum(d_k[mask] * b2t[mask])
    P_nzt = P_t[unique_k > 0]
    if np.all(P_nzt > 0):
        ct = np.polyfit(np.log(k_nonzero), np.log(P_nzt), 1)
        ns_vals.append(ct[0] + 1)
    else:
        ns_vals.append(np.nan)
ax.plot(deltas, ns_vals, 'b-', lw=2)
ax.axhline(0.965, color='g', ls='--', alpha=0.7, label='Planck')
ax.axhline(1.0, color='gray', ls=':', alpha=0.5, label='Scale invariant')
ax.axvline(Delta, color='r', ls='--', alpha=0.7, label=f'Delta_0 = {Delta:.2f}')
ax.fill_between([0.1, 2.0], 0.955, 0.975, alpha=0.1, color='g')
ax.set_xlabel(r'$\Delta$ (M_KK)')
ax.set_ylabel('n_s')
ax.set_title('n_s sensitivity to BCS gap')
ax.legend(fontsize=7)
ax.set_ylim([0.5, 2.5])

plt.tight_layout()
plt.savefig('tier0-computation/s45_collective_ns_v2.png', dpi=150)
print("\nPlot saved to s45_collective_ns_v2.png")

# Save
np.savez('tier0-computation/s45_collective_ns_v2.npz',
    lambda_k=lambda_k, d_k=d_k, Delta=Delta,
    beta2=beta2, E_dressed=E_dressed, E_undressed=E_undressed,
    k_4d=k_4d, unique_k=unique_k, P_k=P_k,
    N_modes=N_modes, beta2_mean_k=beta2_mean_k,
    ns=ns, R2=R2, ns_minus_1=coeffs[0],
    beta2_exponent=cb[0], degeneracy_exponent=cn[0],
    delta_sensitivity_deltas=deltas, delta_sensitivity_ns=np.array(ns_vals),
    gate_verdict=verdict
)
print("Data saved to s45_collective_ns_v2.npz")
