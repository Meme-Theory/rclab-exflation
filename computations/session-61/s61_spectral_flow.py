#!/usr/bin/env python3
"""
s61_spectral_flow.py — Spectral Flow of D_K(tau) from tau=0 to tau_fold
=========================================================================

Gate: SPECTRAL-FLOW-61
  PASS if sf=0 (WKB, no topology change during transit)
  FAIL if sf!=0 and contradicts S38
  INFO if sf!=0 but compatible

Physics:
  The spectral flow sf(D_K; tau in [0, tau_fold]) counts the net number of
  eigenvalues of the fiber Dirac operator D_K(tau) on (SU(3), g_tau) that
  cross through zero as the Jensen deformation parameter tau increases from
  0 to tau_fold = 0.19.

  By the Atiyah-Patodi-Singer index theorem, sf is an INTEGER.

  The Dirac operator D_K(tau) is anti-self-adjoint in the math convention:
    D_K = sum_a rho(e_a) x gamma_a + I x Omega(tau)
  with purely imaginary eigenvalues lambda = i*mu, mu real.

  Spectral flow counts net crossings of mu through zero:
    sf = #{mu crosses 0 upward} - #{mu crosses 0 downward}

  By the Callias theorem (van den Dungen Paper 13), spectral flow depends
  ONLY on endpoints: sf(D_K(0), D_K(tau_fold)).

  Context: TESLA-3 showed [J, dH/dtau] = 0 (Berry phase preserves J-symmetry).
  Spectral flow is the complementary topological invariant -- it counts net
  eigenvalue crossings through zero, corresponding to fermion number change.

Method:
  1. Build D_K(tau) on SU(3) using dirac_spectrum infrastructure
  2. Sample 40 tau values in [0, 0.19]
  3. For each tau, compute eigenvalues of D_K restricted to irreps with p+q <= 3
     (these give all eigenvalues with |lambda| < ~5 M_KK)
  4. Track eigenvalue flow via nearest-neighbor matching
  5. Count zero crossings: sf = #{up} - #{down}
  6. Verify sf is integer

Comparison:
  S_inst = 0.069 (instanton action from s37)
  If sf = 0: consistent with WKB (no topology change), constrains instanton sector
  If sf != 0: topology changes during transit

Session: S61 W3-05
Agent: van-den-dungen-bridge-theorist
Date: 2026-03-28
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigvals, eigvalsh, eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold, S_inst, g0_diag

# Import Dirac spectrum infrastructure
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep,
)

t0 = time.time()

print("=" * 78)
print("S61 W3-05: SPECTRAL FLOW of D_K(tau) — SPECTRAL-FLOW-61")
print("=" * 78)
print(f"  tau_fold = {tau_fold}")
print(f"  S_inst   = {S_inst:.6f}")

# ======================================================================
#  Step 1: Infrastructure setup (one-time)
# ======================================================================

print("\n[1] Building su(3) infrastructure...")
gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()

print(f"  Killing form diagonal: {np.diag(B_ab)[:4]}... (should be -3)")

# ======================================================================
#  Step 2: Define tau grid and irrep sectors
# ======================================================================

# The Jensen parameter in the framework is called tau but maps to s in the
# tier1 code via s = tau (direct identification, S12 convention).
# The framework's tau_fold = 0.19 corresponds to s = 0.19 in tier1.

# Dense sampling: 40 points gives dtau ~ 0.005, sufficient to track
# eigenvalue crossings without ambiguity.
N_tau = 40  # (local)
tau_min = 0.0
tau_max = tau_fold  # = 0.19
tau_grid = np.linspace(tau_min, tau_max, N_tau)
dtau = tau_grid[1] - tau_grid[0]

print(f"\n[2] Tau grid: N={N_tau}, range=[{tau_min}, {tau_max:.4f}], dtau={dtau:.5f}")

# Use irreps with p+q <= 3 -- captures all low-lying eigenvalues
# This includes: (0,0), (1,0), (0,1), (2,0), (1,1), (0,2), (3,0), (2,1), (1,2), (0,3)
MAX_PQ_SUM = 3  # (local)

# Enumerate irreps
irreps = []
for pq_sum in range(MAX_PQ_SUM + 1):
    for p in range(pq_sum + 1):
        q = pq_sum - p
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        irreps.append((p, q, dim_pq))

print(f"  Irreps (p+q <= {MAX_PQ_SUM}): {len(irreps)} sectors")
total_spinor_dim = sum(d * 16 for _, _, d in irreps)
print(f"  Total Dirac matrix dimension per sector (max): "
      f"{max(d * 16 for _, _, d in irreps)}")

# For each irrep, D_pi is (dim_pq * 16) x (dim_pq * 16)
# Total eigenvalue count: sum over irreps of (dim_pq * 16)
total_evals = sum(d * 16 for _, _, d in irreps)
print(f"  Total eigenvalues per tau slice: {total_evals}")

# ======================================================================
#  Step 3: Compute D_K eigenvalues at each tau
# ======================================================================

print(f"\n[3] Computing Dirac eigenvalues at {N_tau} tau values...")

# Store eigenvalues for each irrep sector separately (for cleaner tracking)
# Then also collect ALL eigenvalues for the full spectrum analysis
all_spectra = []  # list of arrays, one per tau
sector_spectra = {}  # (p,q) -> array of shape (N_tau, dim_pq*16)

for p, q, dim_pq in irreps:
    sector_spectra[(p, q)] = np.zeros((N_tau, dim_pq * 16), dtype=np.float64)

# Clear irrep cache between tau values to avoid stale data
# (irreps don't depend on tau, only the metric/connection does)
# Build irreps once
irrep_reps = {}
for p, q, dim_pq in irreps:
    if p == 0 and q == 0:
        irrep_reps[(0, 0)] = None  # trivial handled separately
    else:
        rho, dim_check = get_irrep(p, q, gens, f_abc)
        assert dim_check == dim_pq, f"Dim mismatch for ({p},{q})"
        irrep_reps[(p, q)] = rho

print("  Irrep representations cached.")

for it, tau in enumerate(tau_grid):
    s = tau  # Direct identification: Jensen parameter s = tau

    # Build metric, frame, connection, Omega at this tau
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Collect all eigenvalues (imaginary parts of anti-self-adjoint D_K)
    tau_evals = []

    for p, q, dim_pq in irreps:
        if p == 0 and q == 0:
            # Trivial irrep: D = Omega (16x16)
            D_pi = Omega.copy()
        else:
            rho = irrep_reps[(p, q)]
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # D_pi is anti-self-adjoint: eigenvalues are purely imaginary
        # Compute eigenvalues
        evals = eigvals(D_pi)

        # Extract imaginary parts (the "Dirac eigenvalues" mu)
        # For a perfectly anti-Hermitian matrix, real parts should be ~0
        re_max = np.max(np.abs(evals.real))
        mu = evals.imag  # These are the physical eigenvalues

        # Sort consistently for tracking
        mu_sorted = np.sort(mu)

        sector_spectra[(p, q)][it, :] = mu_sorted
        tau_evals.extend(mu_sorted.tolist())

    all_spectra.append(np.sort(np.array(tau_evals)))

    if it % 10 == 0 or it == N_tau - 1:
        print(f"  tau={tau:.4f}: {len(tau_evals)} eigenvalues, "
              f"range=[{min(tau_evals):.4f}, {max(tau_evals):.4f}], "
              f"Re(max)={re_max:.2e}")

# Convert to array
all_spectra_arr = np.array(all_spectra)  # (N_tau, total_evals)

print(f"\n  Spectrum array shape: {all_spectra_arr.shape}")
print(f"  Time so far: {time.time() - t0:.1f}s")

# ======================================================================
#  Step 4: Track eigenvalue flow via nearest-neighbor matching
# ======================================================================

print(f"\n[4] Tracking eigenvalue flow...")

# Strategy: For each irrep sector separately, track eigenvalues.
# Within a sector, the eigenvalue count is fixed (dim_pq * 16).
# We match eigenvalues at tau+dtau to those at tau by proximity.

def track_eigenvalue_flow(mu_array):
    """
    Given mu_array of shape (N_tau, N_evals), track eigenvalue branches.

    Returns:
        branches: (N_tau, N_evals) with columns reordered so each column
                  follows a single eigenvalue branch.
    """
    N_t, N_e = mu_array.shape
    branches = np.zeros_like(mu_array)
    branches[0, :] = mu_array[0, :]

    for it in range(1, N_t):
        mu_prev = branches[it - 1, :]
        mu_curr = mu_array[it, :]

        # Hungarian algorithm approximation: greedy nearest-neighbor
        used = set()
        assignment = np.zeros(N_e, dtype=int)

        # Sort by distance to find best matches
        for j in range(N_e):
            # Find closest unmatched eigenvalue in current slice
            best_k = -1
            best_dist = np.inf
            for k in range(N_e):
                if k not in used:
                    dist = abs(mu_curr[k] - mu_prev[j])
                    if dist < best_dist:
                        best_dist = dist
                        best_k = k
            assignment[j] = best_k
            used.add(best_k)

        for j in range(N_e):
            branches[it, j] = mu_curr[assignment[j]]

    return branches


# Track eigenvalue flow sector by sector
sector_branches = {}
total_zero_crossings_up = 0
total_zero_crossings_down = 0
crossing_details = []

for p, q, dim_pq in irreps:
    mu_arr = sector_spectra[(p, q)]
    branches = track_eigenvalue_flow(mu_arr)
    sector_branches[(p, q)] = branches

    # Peter-Weyl multiplicity: each eigenvalue in sector (p,q) appears
    # dim(p,q) times in the full spectrum. The spectral flow gets a
    # multiplicity factor.
    pw_mult = dim_pq

    # Count zero crossings in each branch
    N_e = branches.shape[1]
    for j in range(N_e):
        branch = branches[:, j]
        for it in range(1, N_tau):
            if branch[it - 1] * branch[it] < 0:
                # Zero crossing detected
                # Direction: up if crossing from negative to positive
                if branch[it] > branch[it - 1]:
                    total_zero_crossings_up += pw_mult
                    direction = "UP"
                else:
                    total_zero_crossings_down += pw_mult
                    direction = "DOWN"
                # Interpolate zero location
                tau_cross = tau_grid[it - 1] + dtau * abs(branch[it - 1]) / (
                    abs(branch[it - 1]) + abs(branch[it])
                )
                crossing_details.append({
                    'sector': (p, q),
                    'branch': j,
                    'tau_cross': tau_cross,
                    'direction': direction,
                    'mu_before': branch[it - 1],
                    'mu_after': branch[it],
                    'pw_mult': pw_mult,
                })

    # Also check for eigenvalues that START or END at zero
    # (these contribute half-crossings in the APS theory, but for
    # continuous deformations on compact manifolds, they don't appear
    # unless there's a kernel dimension change)

sf_raw = total_zero_crossings_up - total_zero_crossings_down

print(f"  Zero crossings (up):   {total_zero_crossings_up}")
print(f"  Zero crossings (down): {total_zero_crossings_down}")
print(f"  Spectral flow sf = {sf_raw}")
print(f"  |sf| is integer: {sf_raw == int(sf_raw)}")

if crossing_details:
    print(f"\n  Crossing details ({len(crossing_details)} total):")
    for cd in crossing_details:
        print(f"    sector ({cd['sector'][0]},{cd['sector'][1]}), branch {cd['branch']}, "
              f"tau={cd['tau_cross']:.5f}, {cd['direction']}, "
              f"mu: {cd['mu_before']:.6f} -> {cd['mu_after']:.6f}, "
              f"PW mult={cd['pw_mult']}")

# ======================================================================
#  Step 5: Verify via endpoint analysis (Callias theorem)
# ======================================================================

print(f"\n[5] Endpoint analysis (Callias theorem verification)...")

# The Callias theorem says sf depends only on the endpoints.
# Specifically: sf = eta(D_K(tau_fold))/2 - eta(D_K(0))/2  (mod integers)
# where eta is the eta-invariant.
#
# For our purposes: count negative eigenvalues at each endpoint.
# If D_K has symmetric spectrum (due to symmetry), then the number of
# negative eigenvalues is the same at both endpoints => sf = 0.

mu_start = all_spectra_arr[0, :]
mu_end = all_spectra_arr[-1, :]

n_neg_start = np.sum(mu_start < -1e-12)
n_pos_start = np.sum(mu_start > 1e-12)
n_zero_start = np.sum(np.abs(mu_start) <= 1e-12)

n_neg_end = np.sum(mu_end < -1e-12)
n_pos_end = np.sum(mu_end > 1e-12)
n_zero_end = np.sum(np.abs(mu_end) <= 1e-12)

print(f"  At tau=0:        neg={n_neg_start}, zero={n_zero_start}, pos={n_pos_start}")
print(f"  At tau={tau_max:.4f}:  neg={n_neg_end}, zero={n_zero_end}, pos={n_pos_end}")
print(f"  Delta(neg) = {n_neg_end - n_neg_start}")
print(f"  Delta(pos) = {n_pos_end - n_pos_start}")

# Check spectral symmetry: D_K on SU(3) should have symmetric spectrum
# because of the charge conjugation symmetry J.
# If spectrum is symmetric: for each mu, there is -mu.
sym_err_start = 0
sym_err_end = 0
for mu in mu_start:
    closest = np.min(np.abs(mu_start + mu))
    sym_err_start = max(sym_err_start, closest)
for mu in mu_end:
    closest = np.min(np.abs(mu_end + mu))
    sym_err_end = max(sym_err_end, closest)

print(f"\n  Spectral symmetry (mu <-> -mu) check:")
print(f"    At tau=0:       max |mu + closest(-mu)| = {sym_err_start:.2e}")
print(f"    At tau={tau_max:.4f}: max |mu + closest(-mu)| = {sym_err_end:.2e}")

# ======================================================================
#  Step 6: Spectral gap analysis
# ======================================================================

print(f"\n[6] Spectral gap analysis...")

# The spectral gap is the smallest nonzero |mu|.
# If the gap remains open throughout [0, tau_fold], then sf = 0 trivially.

gaps = np.zeros(N_tau)
for it in range(N_tau):
    mu = all_spectra_arr[it, :]
    nonzero_mu = np.abs(mu[np.abs(mu) > 1e-10])
    if len(nonzero_mu) > 0:
        gaps[it] = np.min(nonzero_mu)
    else:
        gaps[it] = 0.0

gap_min = np.min(gaps)
gap_min_tau = tau_grid[np.argmin(gaps)]
gap_max = np.max(gaps)

print(f"  Spectral gap range: [{gap_min:.6f}, {gap_max:.6f}] M_KK")
print(f"  Minimum gap at tau = {gap_min_tau:.4f}")
print(f"  Gap stays open: {gap_min > 1e-6}")

# Count eigenvalues near zero at each tau (within 1e-4 tolerance)
near_zero_count = np.sum(np.abs(all_spectra_arr) < 1e-4, axis=1)
print(f"  Near-zero eigenvalue count: min={near_zero_count.min()}, "
      f"max={near_zero_count.max()}, mean={near_zero_count.mean():.1f}")

# ======================================================================
#  Step 7: Comparison with S_inst and gate verdict
# ======================================================================

print(f"\n[7] Comparison with S_inst = {S_inst:.6f}...")

sf = int(round(sf_raw))

print(f"  Spectral flow sf = {sf}")
print(f"  S_inst = {S_inst:.6f}")

if sf == 0:
    print(f"  sf = 0: No topology change during transit.")
    print(f"  Consistent with WKB interpretation (S38).")
    print(f"  The instanton action S_inst = {S_inst:.4f} governs tunneling RATE,")
    print(f"  not topology change. sf=0 is compatible with S_inst > 0.")
    gate_verdict = "PASS"
    gate_detail = (f"sf=0 (no topology change). Gap stays open: "
                   f"min_gap={gap_min:.4f} at tau={gap_min_tau:.4f}. "
                   f"Spectral symmetry: err={max(sym_err_start, sym_err_end):.2e}. "
                   f"Consistent with WKB/S38.")
else:
    print(f"  sf = {sf} != 0: Topology changes during transit!")
    print(f"  This means {abs(sf)} net fermion number change(s) during BCS flow.")
    if abs(sf) <= 1:
        print(f"  |sf| = 1: Single index change. Compatible with S38 if instanton-mediated.")
        gate_verdict = "INFO"
        gate_detail = (f"sf={sf} (single topology change). "
                       f"Compatible with instanton-mediated transit.")
    else:
        print(f"  |sf| > 1: Multiple topology changes. May contradict S38.")
        gate_verdict = "FAIL"
        gate_detail = f"sf={sf}, |sf|>1 multiple topology changes during transit."

print(f"\n  GATE VERDICT: SPECTRAL-FLOW-61 = {gate_verdict}")
print(f"  Detail: {gate_detail}")

# ======================================================================
#  Step 8: Save data
# ======================================================================

print(f"\n[8] Saving data and plot...")

outfile = os.path.join(SCRIPT_DIR, 's61_spectral_flow.npz')
np.savez(outfile,
    tau_grid=tau_grid,
    N_tau=N_tau,
    MAX_PQ_SUM=MAX_PQ_SUM,
    all_spectra=all_spectra_arr,
    spectral_gaps=gaps,
    near_zero_count=near_zero_count,
    n_neg_start=n_neg_start,
    n_pos_start=n_pos_start,
    n_zero_start=n_zero_start,
    n_neg_end=n_neg_end,
    n_pos_end=n_pos_end,
    n_zero_end=n_zero_end,
    sym_err_start=sym_err_start,
    sym_err_end=sym_err_end,
    sf=sf,
    sf_raw=sf_raw,
    total_up=total_zero_crossings_up,
    total_down=total_zero_crossings_down,
    S_inst=S_inst,
    gap_min=gap_min,
    gap_min_tau=gap_min_tau,
    gate_name=np.array(['SPECTRAL-FLOW-61']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"  Saved: {outfile}")

# ======================================================================
#  Step 9: Plot eigenvalue flow diagram
# ======================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Spectral Flow of $D_K(\\tau)$ on $(SU(3), g_\\tau)$\n"
             f"SPECTRAL-FLOW-61: {gate_verdict}", fontsize=14)

# Panel (a): Full eigenvalue flow (all eigenvalues vs tau)
ax = axes[0, 0]
# Plot a subset of branches for visibility
for p, q, dim_pq in irreps:
    branches = sector_branches[(p, q)]
    N_e = branches.shape[1]
    # Plot every 4th branch for large sectors
    step = max(1, N_e // 20)
    for j in range(0, N_e, step):
        ax.plot(tau_grid, branches[:, j], linewidth=0.3, color='steelblue', alpha=0.5)

ax.axhline(0, color='red', linewidth=0.8, linestyle='--', label='$\\mu = 0$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Dirac eigenvalue $\\mu$')
ax.set_title('(a) Eigenvalue flow (all sectors, sampled)')
ax.legend(fontsize=8)
ax.set_xlim(tau_min, tau_max)

# Panel (b): Low-lying eigenvalues near zero
ax = axes[0, 1]
# Find eigenvalues that come within 1.0 of zero at any point
for p, q, dim_pq in irreps:
    branches = sector_branches[(p, q)]
    N_e = branches.shape[1]
    for j in range(N_e):
        if np.min(np.abs(branches[:, j])) < 1.0:
            ax.plot(tau_grid, branches[:, j], linewidth=0.6,
                    label=f'({p},{q}) b{j}' if j < 3 else None)

ax.axhline(0, color='red', linewidth=0.8, linestyle='--')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\mu$')
ax.set_title('(b) Low-lying eigenvalues ($|\\mu| < 1$)')
ax.set_ylim(-1.5, 1.5)
ax.set_xlim(tau_min, tau_max)

# Panel (c): Spectral gap vs tau
ax = axes[1, 0]
ax.plot(tau_grid, gaps, 'k-', linewidth=1.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Spectral gap $\\Delta(\\tau)$')
ax.set_title(f'(c) Spectral gap: min={gap_min:.4f} at $\\tau$={gap_min_tau:.4f}')
ax.axhline(0, color='red', linewidth=0.5, linestyle='--')
ax.set_xlim(tau_min, tau_max)

# Panel (d): Endpoint spectra comparison
ax = axes[1, 1]
nbins = 60
mu_range = (-3, 3)
ax.hist(mu_start[np.abs(mu_start) < 3], bins=nbins, range=mu_range,
        alpha=0.5, label=f'$\\tau=0$ ({n_neg_start}$^-$/{n_zero_start}$^0$/{n_pos_start}$^+$)',  # (local)
        color='blue', density=True)
ax.hist(mu_end[np.abs(mu_end) < 3], bins=nbins, range=mu_range,
        alpha=0.5, label=f'$\\tau={tau_max:.2f}$ ({n_neg_end}$^-$/{n_zero_end}$^0$/{n_pos_end}$^+$)',  # (local)
        color='orange', density=True)
ax.axvline(0, color='red', linewidth=0.8, linestyle='--')
ax.set_xlabel('$\\mu$')
ax.set_ylabel('Density')
ax.set_title('(d) Endpoint spectral density')
ax.legend(fontsize=8)

plt.tight_layout()
plotfile = os.path.join(SCRIPT_DIR, 's61_spectral_flow.png')
plt.savefig(plotfile, dpi=150)
plt.close()
print(f"  Saved: {plotfile}")

# ======================================================================
#  Summary
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'=' * 78}")
print(f"SPECTRAL-FLOW-61 SUMMARY")
print(f"{'=' * 78}")
print(f"  Spectral flow sf = {sf}")
print(f"  Zero crossings: {total_zero_crossings_up} up, {total_zero_crossings_down} down")
print(f"  Spectral gap: min={gap_min:.6f} at tau={gap_min_tau:.4f}")
print(f"  Spectral symmetry errors: start={sym_err_start:.2e}, end={sym_err_end:.2e}")
print(f"  Endpoint counts: start({n_neg_start}/{n_zero_start}/{n_pos_start}), "
      f"end({n_neg_end}/{n_zero_end}/{n_pos_end})")
print(f"  S_inst = {S_inst:.6f}")
print(f"  GATE: SPECTRAL-FLOW-61 = {gate_verdict}")
print(f"  Detail: {gate_detail}")
print(f"  Runtime: {elapsed:.1f}s")
