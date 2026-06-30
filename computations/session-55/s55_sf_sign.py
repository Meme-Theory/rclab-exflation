#!/usr/bin/env python3
"""
SF-SIGN-55: Sign of dS_fermionic/dtau on the 992-mode continuum
================================================================

Computes S_f(tau) = sum_k n_k(tau) * |lambda_k(tau)| where:
  - |lambda_k(tau)| are the 992 Dirac eigenvalue magnitudes
  - n_k(tau) are BCS occupation numbers with Delta = 0.4643 M_KK

Pre-registered gate: SF-SIGN-55
  PASS (OPEN): dS_f/dtau > 0 anywhere in [0.10, 0.30]
  FAIL (CLOSED): dS_f/dtau < 0 everywhere in [0.10, 0.30]

Data sources:
  - computations/session-44/s44_dos_tau.npz: 992-mode spectra at tau = [0.00, 0.05, 0.10, 0.15, 0.19]
  - computations/session-27/s27_multisector_bcs.npz: per-sector eigenvalues at tau = [0.00, 0.10, 0.15, 0.20, ..., 0.50]
  - computations/session-54/s54_sa_latt_occ.npz: Delta_primary = 0.4643

Author: Spectral-Geometer (S55)
"""

import sys
import os
sys.path.insert(0, 'computations')
from canonical_constants import *

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
#  1. Load data
# ============================================================================

d44 = np.load('computations/session-44/s44_dos_tau.npz', allow_pickle=True)
d27 = np.load('computations/session-27/s27_multisector_bcs.npz', allow_pickle=True)
d54 = np.load('computations/session-54/s54_sa_latt_occ.npz', allow_pickle=True)

Delta = float(d54['Delta_primary'])  # 0.4643
print(f"BCS gap Delta = {Delta:.6f}")

sectors = d27['sectors']
s27_tau_values = d27['tau_values']
s44_tau_values = d44['tau_values']

print(f"s44 tau: {s44_tau_values}")
print(f"s27 tau: {s27_tau_values}")

# ============================================================================
#  2. Build unified spectrum at all available tau
# ============================================================================
# Combined tau values from both sources (sorted, unique):
# s44: [0.00, 0.05, 0.10, 0.15, 0.19]
# s27: [0.00, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]
# Union: [0.00, 0.05, 0.10, 0.15, 0.19, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]

# Build spectra dict: tau -> 992-element array of |eigenvalues|
spectra = {}

# From s44 (already provides 992-element |eigenvalue| arrays)
for tau_val in s44_tau_values:
    tau_str = f"tau{tau_val:.2f}"
    key = f"{tau_str}_all_omega"
    spectra[round(tau_val, 3)] = d44[key].copy()

# From s27 (provides signed eigenvalues per sector; take abs, concatenate)
for i_tau, tau_val in enumerate(s27_tau_values):
    tau_key = round(tau_val, 3)
    if tau_key in spectra:
        continue  # Already from s44 (prefer s44 for overlapping tau)
    evals_list = []
    for row in sectors:
        p, q = int(row[0]), int(row[1])
        key = f"evals_{p}_{q}_{i_tau}"
        evals_list.append(np.abs(d27[key]))
    spectra[tau_key] = np.concatenate(evals_list)

# Also get dim2 weights (Peter-Weyl multiplicity) — same at all tau
dim2_arr = d44['tau0.00_all_dim2']  # (992,)

# Map s27 sectors to dim2 for s27-only tau values
# For s27: each sector (p,q) has 16*dim(p,q) eigenvalues, each with PW weight dim(p,q)^2
dim2_from_s27 = []
for row in sectors:
    p, q = int(row[0]), int(row[1])
    dim_pq = (p+1)*(q+1)*(p+q+2)//2
    n_evals = 16 * dim_pq
    dim2_from_s27.extend([dim_pq**2] * n_evals)
dim2_from_s27 = np.array(dim2_from_s27, dtype=float)

# Verify consistency
assert np.allclose(dim2_arr, dim2_from_s27), "dim2 mismatch between s44 and s27 reconstruction"

# Sort by tau
tau_all = sorted(spectra.keys())
print(f"\nAll tau values ({len(tau_all)}): {tau_all}")

for tau in tau_all:
    sp = spectra[tau]
    print(f"  tau={tau:.3f}: n_modes={len(sp)}, min|lambda|={sp.min():.6f}, max|lambda|={sp.max():.6f}, mean={sp.mean():.6f}")

# ============================================================================
#  3. BCS occupation numbers at each tau
# ============================================================================
# n_k = (1/2)(1 - (eps_k - mu) / sqrt((eps_k - mu)^2 + Delta^2))
# where eps_k = |lambda_k| (Dirac eigenvalue magnitude)
# mu at half-filling: mu = median of {|lambda_k|}
#
# IMPORTANT: The fermionic spectral action uses the PHYSICAL spectrum including
# Peter-Weyl multiplicity. The occupation sum S_f should weight by dim2.
# However, for the SIGN of dS_f/dtau, both weighted and unweighted give the
# same directional information since dim2 is tau-independent.
# We compute both for completeness.

def bcs_occupations(eigenvalues, Delta, mu):
    """Compute BCS occupation numbers.

    n_k = (1/2)(1 - (eps_k - mu)/sqrt((eps_k - mu)^2 + Delta^2))
    """
    xi_k = eigenvalues - mu  # xi_k = eps_k - mu
    E_k = np.sqrt(xi_k**2 + Delta**2)
    n_k = 0.5 * (1.0 - xi_k / E_k)
    return n_k

# Store results
results = {}
for tau in tau_all:
    lam = spectra[tau]  # |lambda_k|, shape (992,)
    mu = np.median(lam)
    n_k = bcs_occupations(lam, Delta, mu)

    # Unweighted S_f (over 992 modes)
    S_f_unw = np.sum(n_k * lam)

    # Weighted S_f (physical, with PW multiplicity dim2)
    S_f_w = np.sum(dim2_arr * n_k * lam)

    results[tau] = {
        'lambda': lam,
        'mu': mu,
        'n_k': n_k,
        'S_f_unweighted': S_f_unw,
        'S_f_weighted': S_f_w,
        'sum_nk': np.sum(n_k),
        'sum_nk_w': np.sum(dim2_arr * n_k),
    }

    print(f"\ntau={tau:.3f}: mu={mu:.6f}, sum(n_k)={np.sum(n_k):.2f}, "
          f"S_f(unw)={S_f_unw:.6f}, S_f(w)={S_f_w:.4f}")

# ============================================================================
#  4. Compute dS_f/dtau via finite differences
# ============================================================================

tau_arr = np.array(tau_all)
S_f_unw_arr = np.array([results[t]['S_f_unweighted'] for t in tau_all])
S_f_w_arr = np.array([results[t]['S_f_weighted'] for t in tau_all])

# Finite difference derivatives (forward, backward, central where possible)
def finite_diff(tau, S):
    """Compute dS/dtau via finite differences. Returns (tau_mid, dSdtau)."""
    n = len(tau)
    tau_mid = []
    dSdtau = []
    for i in range(n - 1):
        dt = tau[i+1] - tau[i]
        dS = S[i+1] - S[i]
        tau_mid.append(0.5 * (tau[i] + tau[i+1]))
        dSdtau.append(dS / dt)
    return np.array(tau_mid), np.array(dSdtau)

tau_mid, dSf_unw = finite_diff(tau_arr, S_f_unw_arr)
_, dSf_w = finite_diff(tau_arr, S_f_w_arr)

print("\n" + "="*70)
print("DERIVATIVE dS_f/dtau (forward differences)")
print("="*70)
print(f"{'tau_mid':>8s}  {'dS_f/dtau(unw)':>16s}  {'dS_f/dtau(w)':>16s}  {'sign(unw)':>10s}  {'sign(w)':>10s}")
for i in range(len(tau_mid)):
    s_unw = "+" if dSf_unw[i] > 0 else "-"
    s_w = "+" if dSf_w[i] > 0 else "-"
    print(f"{tau_mid[i]:8.3f}  {dSf_unw[i]:16.6f}  {dSf_w[i]:16.4f}  {s_unw:>10s}  {s_w:>10s}")

# ============================================================================
#  5. Decompose: drift term + occupation response term
# ============================================================================
# dS_f/dtau = sum_k n_k * (dlambda_k/dtau) + sum_k (dn_k/dtau) * lambda_k
# Term 1 (spectral drift): uses n_k at the midpoint tau, finite-diff on lambda_k
# Term 2 (occupation response): uses lambda_k at the midpoint tau, finite-diff on n_k

print("\n" + "="*70)
print("DECOMPOSITION: drift + occupation response")
print("="*70)

decomp_results = []
for i in range(len(tau_all) - 1):
    t0, t1 = tau_all[i], tau_all[i+1]
    dt = t1 - t0

    lam0 = results[t0]['lambda']
    lam1 = results[t1]['lambda']
    n0 = results[t0]['n_k']
    n1 = results[t1]['n_k']

    # Sort eigenvalues consistently (they're already sector-ordered, so concatenation
    # order matches between tau values as long as no level crossings reorder sectors).
    # The s44/s27 data maintains sector-order consistency.

    dlam_dt = (lam1 - lam0) / dt
    dn_dt = (n1 - n0) / dt

    n_mid = 0.5 * (n0 + n1)
    lam_mid = 0.5 * (lam0 + lam1)

    # Term 1: spectral drift (eigenvalue change with fixed occupation)
    drift_unw = np.sum(n_mid * dlam_dt)
    drift_w = np.sum(dim2_arr * n_mid * dlam_dt)

    # Term 2: occupation response (occupation change with fixed eigenvalue)
    occ_resp_unw = np.sum(dn_dt * lam_mid)
    occ_resp_w = np.sum(dim2_arr * dn_dt * lam_mid)

    total_unw = drift_unw + occ_resp_unw
    total_w = drift_w + occ_resp_w

    decomp_results.append({
        'tau_mid': 0.5 * (t0 + t1),
        'drift_unw': drift_unw,
        'occ_resp_unw': occ_resp_unw,
        'total_unw': total_unw,
        'drift_w': drift_w,
        'occ_resp_w': occ_resp_w,
        'total_w': total_w,
    })

    print(f"\ntau: [{t0:.3f}, {t1:.3f}]  (mid={0.5*(t0+t1):.3f})")
    print(f"  Unweighted: drift={drift_unw:+.6f}, occ_resp={occ_resp_unw:+.6f}, total={total_unw:+.6f}")
    print(f"  Weighted:   drift={drift_w:+.4f}, occ_resp={occ_resp_w:+.4f}, total={total_w:+.4f}")

# ============================================================================
#  6. Gate verdict
# ============================================================================

print("\n" + "="*70)
print("GATE: SF-SIGN-55")
print("="*70)

# Check sign of dS_f/dtau in [0.10, 0.30]
# The gate interval is [0.10, 0.30]. We check both unweighted and weighted.
gate_interval = (0.10, 0.30)
positive_anywhere_unw = False
positive_anywhere_w = False

for d in decomp_results:
    tm = d['tau_mid']
    if gate_interval[0] <= tm <= gate_interval[1]:
        if d['total_unw'] > 0:
            positive_anywhere_unw = True
        if d['total_w'] > 0:
            positive_anywhere_w = True

# Also check the direct finite difference
for i in range(len(tau_mid)):
    if gate_interval[0] <= tau_mid[i] <= gate_interval[1]:
        if dSf_unw[i] > 0:
            positive_anywhere_unw = True
        if dSf_w[i] > 0:
            positive_anywhere_w = True

if positive_anywhere_w:
    verdict = "PASS"
    detail = "dS_f/dtau > 0 found in [0.10, 0.30] (PW-weighted). S_b + S_f OPEN on continuum."
elif positive_anywhere_unw:
    verdict = "PASS"
    detail = "dS_f/dtau > 0 found in [0.10, 0.30] (unweighted). S_b + S_f OPEN on continuum."
else:
    verdict = "FAIL"
    detail = "dS_f/dtau < 0 everywhere in [0.10, 0.30]. S_b + S_f CLOSED on continuum."

print(f"Verdict: {verdict}")
print(f"Detail: {detail}")

# ============================================================================
#  7. Per-branch decomposition (B1, B2, B3)
# ============================================================================

print("\n" + "="*70)
print("PER-BRANCH ANALYSIS")
print("="*70)

# Branch classification from memory:
# B1 (trivial, 1-fold): (0,0) sector, dim=1, 16 eigenvalues
# B2 (U(2) fund, 4-fold): (1,0)+(0,1), dim=3 each, 48 eigenvalues each => 96 total
# B3 (SU(2) adj, 3-fold): (1,1)+(2,0)+(0,2)+(3,0)+(0,3)+(2,1), remaining
# More precisely, B1/B2/B3 refers to spectral branches, not exact sector decomposition.
# The Dirac eigenvalues form 3 branches (from S34 MEMORY):
#   B1: smallest eigenvalue branch (1 mode per spinor = 8 positive eigenvalues out of 16 in (0,0))
#   B2: near-degenerate cluster of 4 (= B2 degeneracy from (0,0) + (1,0)/(0,1) crossings)
#   B3: upper branch

# For a clean decomposition, identify branches by eigenvalue magnitude at each tau.
# The (0,0) sector has 16 eigenvalues: 8 positive, 8 negative.
# At tau>0: 3 distinct magnitudes in (0,0): smallest (B1, 1-fold), middle (B2, 4-fold), largest (B3, 3-fold)
# From s27 at tau=0.10 (idx=1):
# evals_0_0_1 = [-0.916, -0.916, -0.916, -0.850, -0.850, -0.850, -0.850, -0.833,
#                 0.833, 0.850, 0.850, 0.850, 0.850, 0.916, 0.916, 0.916]
# Positive |magnitudes|: 0.833(x1=B1), 0.850(x4=B2), 0.916(x3=B3)

# For the full 992-mode spectrum, the branch assignment is less clean.
# Let's instead do sector-level decomposition.

# Sector grouping (matches Peter-Weyl blocks):
sector_groups = {
    'singlet (0,0)': [(0, 0)],
    'fundamental (1,0)+(0,1)': [(1, 0), (0, 1)],
    'adjoint+higher': [(1, 1), (2, 0), (0, 2), (3, 0), (0, 3), (2, 1)],
}

# Build sector masks for the 992-mode spectrum
# Order: (0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1)
sector_ranges = {}
offset = 0  # (local)
for row in sectors:
    p, q = int(row[0]), int(row[1])
    dim_pq = (p+1)*(q+1)*(p+q+2)//2
    n = 16 * dim_pq
    sector_ranges[(p, q)] = (offset, offset + n)
    offset += n

for group_name, sector_list in sector_groups.items():
    print(f"\n--- {group_name} ---")
    for i in range(len(tau_all) - 1):
        t0, t1 = tau_all[i], tau_all[i+1]
        dt = t1 - t0

        lam0 = results[t0]['lambda']
        lam1 = results[t1]['lambda']
        n0 = results[t0]['n_k']
        n1 = results[t1]['n_k']

        dlam = (lam1 - lam0) / dt
        dn = (n1 - n0) / dt
        n_mid = 0.5 * (n0 + n1)
        lam_mid = 0.5 * (lam0 + lam1)

        drift_grp = 0.0  # (local)
        occ_grp = 0.0  # (local)
        for (p, q) in sector_list:
            s, e = sector_ranges[(p, q)]
            w = dim2_arr[s:e]
            drift_grp += np.sum(w * n_mid[s:e] * dlam[s:e])
            occ_grp += np.sum(w * dn[s:e] * lam_mid[s:e])

        print(f"  tau=[{t0:.2f},{t1:.2f}]: drift={drift_grp:+.4f}, occ_resp={occ_grp:+.4f}, total={drift_grp+occ_grp:+.4f}")

# ============================================================================
#  8. Bosonic spectral action for comparison (S_b = sum |lambda_k|^2)
# ============================================================================

print("\n" + "="*70)
print("BOSONIC S_b = sum dim2 * |lambda_k|^2  (for reference)")
print("="*70)

S_b_arr = np.array([np.sum(dim2_arr * spectra[t]**2) for t in tau_all])
_, dSb = finite_diff(tau_arr, S_b_arr)

print(f"{'tau':>8s}  {'S_b':>14s}")
for tau in tau_all:
    sb = np.sum(dim2_arr * spectra[tau]**2)
    print(f"{tau:8.3f}  {sb:14.4f}")

print(f"\n{'tau_mid':>8s}  {'dS_b/dtau':>14s}  {'sign':>6s}")
for i in range(len(tau_mid)):
    s = "+" if dSb[i] > 0 else "-"
    print(f"{tau_mid[i]:8.3f}  {dSb[i]:14.4f}  {s:>6s}")

# Combined
print(f"\n{'tau_mid':>8s}  {'dS_b/dtau':>14s}  {'dS_f/dtau(w)':>14s}  {'d(S_b+S_f)/dtau':>16s}  {'sign':>6s}")
for i in range(len(tau_mid)):
    total = dSb[i] + dSf_w[i]
    s = "+" if total > 0 else "-"
    print(f"{tau_mid[i]:8.3f}  {dSb[i]:14.4f}  {dSf_w[i]:14.4f}  {total:16.4f}  {s:>6s}")

# ============================================================================
#  9. Save results
# ============================================================================

np.savez('computations/session-55/s55_sf_sign.npz',
    # Tau arrays
    tau_all=tau_arr,
    tau_mid=tau_mid,

    # Spectral action values
    S_f_unweighted=S_f_unw_arr,
    S_f_weighted=S_f_w_arr,
    S_b=S_b_arr,

    # Derivatives
    dSf_dtau_unweighted=dSf_unw,
    dSf_dtau_weighted=dSf_w,
    dSb_dtau=dSb,

    # Decomposition
    decomp_drift_unw=np.array([d['drift_unw'] for d in decomp_results]),
    decomp_occ_resp_unw=np.array([d['occ_resp_unw'] for d in decomp_results]),
    decomp_drift_w=np.array([d['drift_w'] for d in decomp_results]),
    decomp_occ_resp_w=np.array([d['occ_resp_w'] for d in decomp_results]),

    # Parameters
    Delta=Delta,

    # Gate
    gate_name=np.array(['SF-SIGN-55']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)
print(f"\nSaved: computations/session-55/s55_sf_sign.npz")

# ============================================================================
#  10. Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'SF-SIGN-55: Fermionic Spectral Action Sign Analysis\n'
             f'$\\Delta = {Delta:.4f}$, 992 modes, Gate: {verdict}',
             fontsize=13, fontweight='bold')

# Panel (a): S_f(tau) unweighted and weighted
ax = axes[0, 0]
ax.plot(tau_arr, S_f_unw_arr, 'bo-', label='$S_f$ (unweighted)', markersize=5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$S_f(\tau)$ (unweighted)')
ax.set_title('(a) $S_f(\\tau)$ — unweighted (992 modes)')
ax.legend()
ax.grid(True, alpha=0.3)
# Secondary axis for weighted
ax2 = ax.twinx()
ax2.plot(tau_arr, S_f_w_arr, 'rs-', label='$S_f$ (PW-weighted)', markersize=5)
ax2.set_ylabel(r'$S_f(\tau)$ (PW-weighted)', color='red')
ax2.tick_params(axis='y', labelcolor='red')
ax2.legend(loc='lower right')

# Panel (b): dS_f/dtau
ax = axes[0, 1]
ax.bar(tau_mid - 0.005, dSf_unw, width=0.008, color='blue', alpha=0.6, label='unweighted')
ax.bar(tau_mid + 0.005, dSf_w / np.abs(dSf_w).max() * np.abs(dSf_unw).max(),
       width=0.008, color='red', alpha=0.6, label='weighted (rescaled)')  # (local)
ax.axhline(0, color='k', linewidth=0.8)
ax.axvspan(0.10, 0.30, alpha=0.1, color='green', label='gate interval')
ax.set_xlabel(r'$\tau_{\rm mid}$')
ax.set_ylabel(r'$dS_f/d\tau$')
ax.set_title(f'(b) $dS_f/d\\tau$ — Gate: {verdict}')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): Decomposition (weighted)
ax = axes[1, 0]
drift_w_arr = np.array([d['drift_w'] for d in decomp_results])
occ_w_arr = np.array([d['occ_resp_w'] for d in decomp_results])
total_w_arr = drift_w_arr + occ_w_arr
ax.plot(tau_mid, drift_w_arr, 'g^-', label='Drift: $\\sum n_k \\cdot d\\lambda_k/d\\tau$', markersize=6)
ax.plot(tau_mid, occ_w_arr, 'mv-', label='Occ resp: $\\sum (dn_k/d\\tau) \\cdot \\lambda_k$', markersize=6)
ax.plot(tau_mid, total_w_arr, 'ko-', label='Total', markersize=5, linewidth=2)
ax.axhline(0, color='k', linewidth=0.8)
ax.axvspan(0.10, 0.30, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau_{\rm mid}$')
ax.set_ylabel(r'$dS_f/d\tau$ (PW-weighted)')
ax.set_title('(c) Decomposition: drift vs occupation response')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Combined S_b + S_f
ax = axes[1, 1]
S_total = S_b_arr + S_f_w_arr
_, dStot = finite_diff(tau_arr, S_total)
ax.plot(tau_mid, dSb, 'b^-', label=r'$dS_b/d\tau$', markersize=6)
ax.plot(tau_mid, dSf_w, 'rv-', label=r'$dS_f/d\tau$ (weighted)', markersize=6)
ax.plot(tau_mid, dStot, 'ko-', label=r'$d(S_b + S_f)/d\tau$', markersize=5, linewidth=2)
ax.axhline(0, color='k', linewidth=0.8)
ax.axvspan(0.10, 0.30, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau_{\rm mid}$')
ax.set_ylabel(r'$dS/d\tau$')
ax.set_title('(d) Combined: bosonic + fermionic')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-55/s55_sf_sign.png', dpi=150, bbox_inches='tight')
print(f"Saved: computations/session-55/s55_sf_sign.png")

# ============================================================================
#  11. Summary table
# ============================================================================

print("\n" + "="*70)
print("SUMMARY TABLE: S_f values at each tau")
print("="*70)
print(f"{'tau':>8s}  {'S_f(unw)':>12s}  {'S_f(w)':>14s}  {'mu':>10s}  {'sum(n_k)':>10s}")
for tau in tau_all:
    r = results[tau]
    print(f"{tau:8.3f}  {r['S_f_unweighted']:12.6f}  {r['S_f_weighted']:14.4f}  {r['mu']:10.6f}  {r['sum_nk']:10.2f}")

print(f"\n{'tau_mid':>8s}  {'dS_f/dtau(unw)':>16s}  {'dS_f/dtau(w)':>16s}  {'dS_b/dtau':>12s}  {'d(Sb+Sf)/dtau':>16s}")
for i in range(len(tau_mid)):
    total = dSb[i] + dSf_w[i]
    print(f"{tau_mid[i]:8.3f}  {dSf_unw[i]:16.6f}  {dSf_w[i]:16.4f}  {dSb[i]:12.4f}  {total:16.4f}")

print(f"\nGate SF-SIGN-55: {verdict}")
print(f"Detail: {detail}")
print("DONE")
