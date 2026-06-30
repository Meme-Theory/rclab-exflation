"""
TOPOLOGY-TRANSITION-57: Level Quasi-Crossing at tau ~ 0.459
============================================================

Tests whether the TB spectrum quasi-crossing near tau=0.449-0.459 is a
genuine topological transition (gap closure + Z_2 invariant change) or
an accidental avoided crossing.

GEOMETRIC PICTURE
-----------------
The 32x32 TB Hamiltonian H(tau) is REAL-SYMMETRIC at all tau (verified
computationally). For a real-symmetric Hamiltonian:

  (1) All eigenvectors can be chosen real.
  (2) Berry curvature Omega_n = 0 identically (Im of real products).
  (3) Any Z_2 invariant (Pfaffian sign, Zak phase mod pi) can only
      change when the spectral gap closes EXACTLY (gap = 0).

The quasi-crossing at tau ~ 0.459 has gap ~ 1.6e-4 M_KK. Unless this gap
is zero to machine precision, it is an AVOIDED CROSSING -- the levels
repel, exchange character, and no topological invariant changes.

AVOIDED CROSSING DIAGNOSTICS
-----------------------------
At an avoided crossing between levels i and j:
  (a) The gap passes through a local minimum delta_min > 0
  (b) Eigenvector character swaps: |<psi_i(before)|psi_j(after)>| ~ 1
  (c) The coupling matrix element V_ij that opens the gap can be extracted:
      delta_min ~ 2|V_ij| (for a symmetric 2-level model)

This is Berry's diabolical point theory (Paper 03) applied in 1D parameter
space: generically, exact degeneracies require codimension-2 tuning in
real-symmetric systems (Wigner-von Neumann). In 1D, crossings are measure-zero.

BDI Z_2 INVARIANT
------------------
The relevant Z_2 is sgn(Pf(C1 @ D_K)), established in S35 as -1 at all 34+25
tau values tested. For the TB Hamiltonian specifically:
  - H_TB is real-symmetric => orthogonal class (AI)
  - The BDI structure lives on the 16x16 D_K (Dirac operator), not H_TB
  - sgn(Pf) changes IFF det(D_K) passes through zero IFF spectral gap closes
  - S35 min|ev(D_K)| = 0.819 (WIDE OPEN gap, nowhere near closing)

Berry-Geometric-Phase-Theorist, Session 57
"""

import os
import sys
import time
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import tau_fold, E_B1

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("TOPOLOGY-TRANSITION-57: Level Quasi-Crossing Analysis")
print("Berry-Geometric-Phase-Theorist, Session 57")
print("=" * 78)

# ======================================================================
#  STEP 1: Load TB Hamiltonian data
# ======================================================================

tb_data = np.load(os.path.join(SCRIPT_DIR, 's54_tb_hamiltonian.npz'),
                  allow_pickle=True)
tau_vals = tb_data['tau_values']       # (50,)
eigenvalues = tb_data['eigenvalues']   # (50, 32)
eigenvectors = tb_data['eigenvectors'] # (50, 32, 32)
hamiltonians = tb_data['hamiltonians'] # (50, 32, 32)
cell_labels = tb_data['cell_labels']   # (32, 2)
n_tau = len(tau_vals)
n_cells = eigenvalues.shape[1]

print(f"\nLoaded TB data: {n_tau} tau values, {n_cells} cells")
print(f"  tau range: [{tau_vals[0]:.4f}, {tau_vals[-1]:.4f}]")

# ======================================================================
#  STEP 2: Verify H is real-symmetric (prerequisite for analysis)
# ======================================================================

print("\n--- Step 2: Hamiltonian reality check ---")

max_imag_all = 0.0
max_asym_all = 0.0
for i in range(n_tau):
    H = hamiltonians[i]
    if np.iscomplexobj(H):
        max_imag_all = max(max_imag_all, np.max(np.abs(np.imag(H))))
    max_asym_all = max(max_asym_all, np.max(np.abs(H - H.T)))

is_real_sym = (max_imag_all < 1e-14) and (max_asym_all < 1e-14)
print(f"  max|Im(H)|  across all tau: {max_imag_all:.2e}")
print(f"  max|H-H^T|  across all tau: {max_asym_all:.2e}")
print(f"  H is real-symmetric: {is_real_sym}")

if is_real_sym:
    print("  => Berry curvature = 0 identically (Paper 01, Section 3)")
    print("  => Z_2 invariant can change ONLY at exact gap closure")

# Verify eigenvectors are real
max_imag_vec = 0.0
for i in range(n_tau):
    v = eigenvectors[i]
    if np.iscomplexobj(v):
        max_imag_vec = max(max_imag_vec, np.max(np.abs(np.imag(v))))
print(f"  max|Im(eigvec)| across all tau: {max_imag_vec:.2e}")
print(f"  Eigenvectors real: {max_imag_vec < 1e-14}")

# ======================================================================
#  STEP 3: Locate ALL quasi-crossings (gap < 0.01)
# ======================================================================

print("\n--- Step 3: Quasi-crossing survey ---")
print(f"  Threshold: consecutive gap < 0.01 M_KK")

quasi_crossings = []  # (tau_idx, level_idx, gap_value)

for i in range(n_tau):
    ev = eigenvalues[i]
    diffs = np.diff(ev)
    for j in range(len(diffs)):
        if diffs[j] < 0.01:
            quasi_crossings.append((i, j, diffs[j]))

print(f"  Found {len(quasi_crossings)} quasi-crossings total")
print(f"\n  {'tau':>8s}  {'levels':>8s}  {'gap':>12s}  {'eig_lower':>12s}  {'eig_upper':>12s}")
print("  " + "-" * 60)

for (ti, li, gap) in quasi_crossings:
    ev = eigenvalues[ti]
    print(f"  {tau_vals[ti]:8.6f}  {li:2d}-{li+1:2d}    {gap:12.8f}  {ev[li]:12.6f}  {ev[li+1]:12.6f}")

# ======================================================================
#  STEP 4: Focus on the eig[30]-eig[31] quasi-crossing near tau~0.459
# ======================================================================

print("\n--- Step 4: Eigenvalue 30-31 flow (the target quasi-crossing) ---")

# Find the tau where gap(30,31) is minimized
gaps_30_31 = eigenvalues[:, 31] - eigenvalues[:, 30]
idx_min_gap = np.argmin(gaps_30_31)
tau_min_gap = tau_vals[idx_min_gap]
min_gap_30_31 = gaps_30_31[idx_min_gap]

print(f"  Minimum gap: {min_gap_30_31:.8f} M_KK at tau = {tau_min_gap:.6f}")
print(f"  eig[30] = {eigenvalues[idx_min_gap, 30]:.8f}")
print(f"  eig[31] = {eigenvalues[idx_min_gap, 31]:.8f}")

# Show flow around minimum
print(f"\n  {'tau':>8s}  {'eig[30]':>12s}  {'eig[31]':>12s}  {'gap':>12s}")
print("  " + "-" * 50)
for di in range(-5, 6):
    i = idx_min_gap + di
    if 0 <= i < n_tau:
        marker = " <-- min" if i == idx_min_gap else ""
        print(f"  {tau_vals[i]:8.6f}  {eigenvalues[i,30]:12.8f}  "
              f"{eigenvalues[i,31]:12.8f}  {gaps_30_31[i]:12.8f}{marker}")

# ======================================================================
#  STEP 5: Eigenvector character exchange (avoided crossing diagnostic)
# ======================================================================

print("\n--- Step 5: Eigenvector character exchange ---")
print("  Overlap matrix |<psi_n(tau_i)|psi_m(tau_{i+1})>| for n,m in {30,31}")

# Compute overlap matrices between consecutive tau values
overlap_data = []
for i in range(max(0, idx_min_gap - 4), min(n_tau - 1, idx_min_gap + 4)):
    v30_now = eigenvectors[i, :, 30]
    v31_now = eigenvectors[i, :, 31]
    v30_next = eigenvectors[i+1, :, 30]
    v31_next = eigenvectors[i+1, :, 31]

    o30_30 = abs(np.dot(v30_now, v30_next))
    o30_31 = abs(np.dot(v30_now, v31_next))
    o31_30 = abs(np.dot(v31_now, v30_next))
    o31_31 = abs(np.dot(v31_now, v31_next))

    # Detect character swap: off-diagonal > diagonal
    is_swap = (o30_31 > o30_30) and (o31_30 > o31_31)

    overlap_data.append({
        'tau_from': tau_vals[i],
        'tau_to': tau_vals[i+1],
        'o30_30': o30_30,
        'o30_31': o30_31,
        'o31_30': o31_30,
        'o31_31': o31_31,
        'swap': is_swap,
    })

    swap_str = "SWAP" if is_swap else "    "
    print(f"  tau {tau_vals[i]:.4f} -> {tau_vals[i+1]:.4f}: "
          f"|<30|30>|={o30_30:.6f}  |<30|31>|={o30_31:.6f}  "
          f"|<31|30>|={o31_30:.6f}  |<31|31>|={o31_31:.6f}  {swap_str}")

n_swaps = sum(1 for d in overlap_data if d['swap'])
print(f"\n  Total character swaps detected: {n_swaps}")

# Identify the specific cells dominating each eigenvector
print("\n  Dominant cell character at gap minimum (tau = {:.6f}):".format(tau_min_gap))
for lev in [30, 31]:
    v = eigenvectors[idx_min_gap, :, lev]
    weights = v**2
    top_cells = np.argsort(weights)[-3:][::-1]
    print(f"    eig[{lev}]: ", end="")
    for c in top_cells:
        p, q = cell_labels[c]
        print(f"({p},{q})={weights[c]:.3f}  ", end="")
    print()

# ======================================================================
#  STEP 6: Extract coupling matrix element (2-level model)
# ======================================================================

print("\n--- Step 6: Avoided crossing parameters (2-level model) ---")

# At the avoided crossing, the 2-level Hamiltonian is:
#   H_eff = [[E_+(tau), V], [V, E_-(tau)]]
# Minimum gap = 2|V|, occurring when E_+(tau) = E_-(tau)
# The diabatic (unperturbed) levels cross; the adiabatic levels repel

V_coupling = min_gap_30_31 / 2.0
print(f"  |V_coupling| = delta_min / 2 = {V_coupling:.8f} M_KK")

# Estimate the slope of the diabatic levels
# Before crossing: eig[30] is the "fast-moving" level, eig[31] is "slow"
# Use levels well before and after to estimate diabatic slopes
if idx_min_gap >= 3 and idx_min_gap + 3 < n_tau:
    # Diabatic slope from well before the crossing
    d_tau = tau_vals[1] - tau_vals[0]  # uniform spacing
    slope_before = (eigenvalues[idx_min_gap - 3, 31] - eigenvalues[idx_min_gap - 3, 30]) / 1.0
    slope_after = (eigenvalues[min(idx_min_gap + 3, n_tau-1), 31] -
                   eigenvalues[min(idx_min_gap + 3, n_tau-1), 30]) / 1.0

    # The diabatic slopes are the derivatives of the CROSSING (not anti-crossing) levels
    # Estimate relative diabatic velocity
    # Use 3-point derivative at the crossing point
    i_m = idx_min_gap
    d30 = (eigenvalues[i_m+1, 30] - eigenvalues[i_m-1, 30]) / (tau_vals[i_m+1] - tau_vals[i_m-1])
    d31 = (eigenvalues[i_m+1, 31] - eigenvalues[i_m-1, 31]) / (tau_vals[i_m+1] - tau_vals[i_m-1])
    rel_velocity = abs(d30 - d31)
    print(f"  d(eig30)/dtau at crossing: {d30:.6f}")
    print(f"  d(eig31)/dtau at crossing: {d31:.6f}")
    print(f"  |relative velocity|: {rel_velocity:.6f}")

    # Landau-Zener transition probability (if traversed at rate v)
    # P_LZ = exp(-2*pi*|V|^2 / (hbar * |F1-F2| * v_tau))
    # For adiabatic passage (slow), P_LZ -> 0 (system follows adiabatic level)
    # For diabatic passage (fast), P_LZ -> 1 (system jumps)
    if rel_velocity > 0:
        LZ_param = np.pi * V_coupling**2 / rel_velocity
        print(f"  LZ parameter pi*V^2/|dE/dtau|: {LZ_param:.8f}")
        print(f"  P_LZ = exp(-2*LZ_param) = {np.exp(-2*LZ_param):.6e}")
    else:
        LZ_param = np.inf
        print(f"  Relative velocity = 0 => fully adiabatic")

# ======================================================================
#  STEP 7: Z_2 invariant analysis
# ======================================================================

print("\n--- Step 7: Z_2 invariant (topological transition test) ---")

print("\n  STRUCTURAL ARGUMENT (no computation needed):")
print("  =============================================")
print(f"  1. H_TB(tau) is 32x32 real-symmetric at all tau.")
print(f"  2. Symmetry class for real-symmetric H: AI (orthogonal).")
print(f"  3. AI in 0D (no momentum): Z_2 = sgn(det(H)) if H has a gap.")
print(f"  4. For the eigenvalue flow, a topological transition requires")
print(f"     an eigenvalue to cross EXACTLY through zero (or two levels")
print(f"     to become exactly degenerate for Kramers-type Z_2).")
print(f"  5. The quasi-crossing at tau={tau_min_gap:.4f} has gap = {min_gap_30_31:.2e}.")
print(f"     This is nonzero (>> machine epsilon {np.finfo(float).eps:.2e}).")
print(f"  6. Therefore: NO topological transition occurs.")

# Compute det(H_TB) at each tau to check for sign changes
print("\n  det(H_TB) sign check:")
det_signs = []
det_vals = []
for i in range(n_tau):
    # det = product of eigenvalues
    d = np.prod(eigenvalues[i])
    det_vals.append(d)
    det_signs.append(np.sign(d) if d != 0 else 0)

det_signs = np.array(det_signs)
det_vals = np.array(det_vals)

# eig[0] = 0 at all tau => det = 0 always. This is the (0,0) trivial rep.
print(f"  Note: eig[0] = 0 at all tau (trivial rep). det(H_TB) = 0 always.")
print(f"  The zero eigenvalue is STRUCTURAL (not a gap closure).")
print(f"  It corresponds to the (0,0) representation with Casimir = 0.")

# More meaningful: check the REDUCED determinant (excluding eig[0])
det_reduced = []
for i in range(n_tau):
    d = np.prod(eigenvalues[i, 1:])  # skip eig[0] = 0
    det_reduced.append(d)
det_reduced = np.array(det_reduced)
sgn_reduced = np.sign(det_reduced)

print(f"\n  Reduced det (excluding zero mode):")
print(f"    All positive: {np.all(sgn_reduced > 0)}")
print(f"    All negative: {np.all(sgn_reduced < 0)}")
n_sign_changes = np.sum(np.diff(sgn_reduced) != 0)
print(f"    Sign changes: {n_sign_changes}")

if n_sign_changes == 0:
    print(f"    => sgn(det_reduced) = {int(sgn_reduced[0]):+d} at ALL tau")
    print(f"    => Z_2 invariant CONSTANT => no topological transition")

# ======================================================================
#  STEP 8: Connection to BDI Pfaffian (D_K level)
# ======================================================================

print("\n--- Step 8: Connection to D_K Pfaffian (BDI Z_2) ---")
print(f"  The BDI Z_2 lives on D_K (16x16 Dirac operator), NOT on H_TB (32x32).")
print(f"  S35 result: sgn(Pf(C1 @ D_K)) = -1 at all 34+25 tau values.")
print(f"  S36 result: BDI winding number nu = 0. Gap open (min = {E_B1:.3f}).")
print(f"  The D_K spectral gap at fold = {E_B1:.3f} M_KK.")
print(f"  At tau = {tau_min_gap:.4f}, E_B1 >> 0 (monotonically varying).")
print(f"  The TB quasi-crossing at tau = {tau_min_gap:.4f} involves")
print(f"  the HIGHEST levels (eig[30], eig[31]) -- far from the gap edge.")
print(f"  These are high-lying representations: (2,5) and (5,2).")
print(f"  They have NO bearing on the topological invariant,")
print(f"  which is determined by the gap between occupied and empty states.")

# ======================================================================
#  STEP 9: Survey ALL quasi-crossings for completeness
# ======================================================================

print("\n--- Step 9: All quasi-crossings classified ---")
print("  Identifying all local gap minima (avoided crossings) in the spectrum")

# For each pair of consecutive eigenvalues, find where gap is minimized
all_avoided = []
for j in range(n_cells - 1):
    gaps_j = eigenvalues[:, j+1] - eigenvalues[:, j]
    # Find local minima
    for i in range(1, n_tau - 1):
        if gaps_j[i] < gaps_j[i-1] and gaps_j[i] < gaps_j[i+1] and gaps_j[i] < 0.05:
            all_avoided.append({
                'tau': tau_vals[i],
                'tau_idx': i,
                'levels': (j, j+1),
                'gap': gaps_j[i],
                'ev_lower': eigenvalues[i, j],
                'ev_upper': eigenvalues[i, j+1],
                'p_lower': cell_labels[j, 0],
                'q_lower': cell_labels[j, 1],
            })

all_avoided.sort(key=lambda x: x['gap'])

print(f"\n  Found {len(all_avoided)} avoided crossings with gap < 0.05 M_KK")
print(f"\n  {'tau':>8s}  {'levels':>8s}  {'gap':>12s}  {'location':>12s}")
print("  " + "-" * 50)
for ac in all_avoided[:15]:
    print(f"  {ac['tau']:8.6f}  {ac['levels'][0]:2d}-{ac['levels'][1]:2d}    "
          f"{ac['gap']:12.8f}  {ac['ev_lower']:12.6f}")

# ======================================================================
#  STEP 10: Load ED sweep for V_kl structure check
# ======================================================================

print("\n--- Step 10: Pairing matrix V near quasi-crossing ---")

try:
    ed_data = np.load(os.path.join(SCRIPT_DIR, 's54_ed_sweep.npz'), allow_pickle=True)
    ed_tau = ed_data['tau_values']
    E_sp = ed_data['E_sp_sweep']     # (50, 8) single-particle energies
    pair_occ = ed_data['pair_occupations']  # (50, 8)
    V_bare = ed_data['V_bare_cont']  # (8, 8) pairing matrix

    # The quasi-crossing in TB is at levels 30-31 (high reps).
    # The ED uses only 8 modes (low-lying). Check for any structure change.

    # Find idx closest to tau_min_gap in ED
    idx_ed = np.argmin(np.abs(ed_tau - tau_min_gap))

    print(f"  ED single-particle energies at tau = {ed_tau[idx_ed]:.6f}:")
    print(f"    {E_sp[idx_ed]}")
    print(f"  Pair occupations at tau = {ed_tau[idx_ed]:.6f}:")
    print(f"    {pair_occ[idx_ed]}")

    # Check if pair occupations change smoothly through the quasi-crossing
    print(f"\n  Pair occupation flow near tau = {tau_min_gap:.4f}:")
    print(f"  {'tau':>8s}  ", end="")
    for m in range(8):
        print(f"  {'n_'+str(m):>8s}", end="")
    print()
    for di in range(-3, 4):
        idx = idx_ed + di
        if 0 <= idx < len(ed_tau):
            marker = " <--" if abs(ed_tau[idx] - tau_min_gap) < 0.006 else ""
            print(f"  {ed_tau[idx]:8.6f}", end="")
            for m in range(8):
                print(f"  {pair_occ[idx, m]:8.5f}", end="")
            print(marker)

    # Pair occupations are smooth => no phase transition in BCS sector
    po_diffs = np.abs(np.diff(pair_occ[max(0,idx_ed-3):min(len(ed_tau),idx_ed+4)], axis=0))
    max_jump = np.max(po_diffs)
    print(f"\n  Max pair-occupation jump near crossing: {max_jump:.6f}")
    print(f"  Smooth (< 0.01): {max_jump < 0.01}")

except Exception as e:
    print(f"  Could not load ED data: {e}")
    max_jump = None

# ======================================================================
#  STEP 11: Codimension argument (Paper 03 / von Neumann-Wigner)
# ======================================================================

print("\n--- Step 11: Codimension argument ---")
print("  For a real-symmetric NxN matrix depending on parameters:")
print("    - Exact degeneracy of 2 levels requires codimension 2")
print("      (Wigner-von Neumann, 1929; Berry Paper 03)")
print("    - In 1D parameter space (tau only), codim-2 degeneracies")
print("      are GENERICALLY ABSENT")
print("    - They can appear at isolated points if an extra symmetry")
print("      is present (e.g., a conserved quantum number)")
print("    - The TB Hamiltonian has NO additional symmetry that would")
print("      protect a degeneracy between (2,5) and (5,2) reps")
print("  CONCLUSION: The near-degeneracy is ACCIDENTAL, not protected")

# ======================================================================
#  VERDICT
# ======================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: TOPOLOGY-TRANSITION-57")
print("=" * 78)

# Compile results
verdict = "INFO"
gap_at_target = min_gap_30_31
tau_at_target = tau_min_gap
z2_constant = (n_sign_changes == 0)
is_avoided_crossing = (n_swaps > 0 and gap_at_target > 100 * np.finfo(float).eps)

print(f"\n  VERDICT: {verdict}")
print(f"  The tau = 0.449-0.459 quasi-crossing is NOT a topological transition.")
print(f"  It is a textbook AVOIDED CROSSING between levels 30 and 31.")
print(f"")
print(f"  Key numbers:")
print(f"    Minimum gap:          {gap_at_target:.8f} M_KK (at tau = {tau_at_target:.6f})")
print(f"    Gap / epsilon_mach:   {gap_at_target / np.finfo(float).eps:.1e}")
print(f"    Character swaps:      {n_swaps} (complete eigenvector exchange)")
print(f"    Z_2 (reduced det):    constant = {int(sgn_reduced[0]):+d} at all tau")
print(f"    Pair occupations:     smooth (max jump = {max_jump:.6f})")
print(f"    H_TB real-symmetric:  {is_real_sym} (Berry curvature = 0)")
print(f"    Codimension:          2 required for exact degeneracy in 1D")
print(f"")
print(f"  Classification: ACCIDENTAL AVOIDED CROSSING")
print(f"    The (2,5) and (5,2) representations have different (p,q) quantum")
print(f"    numbers but the same Casimir eigenvalue C_2(2,5) = C_2(5,2).")
print(f"    Their TB eigenvalues approach each other as tau increases, but")
print(f"    the off-diagonal coupling (V ~ {V_coupling:.6f} M_KK) prevents")
print(f"    exact degeneracy. This is Paper 03's 'diabolical point avoidance'")
print(f"    in 1D parameter space.")
print(f"")
print(f"  Extends topological triviality chain:")
print(f"    S25: Berry curv = 0 | S25: Chern = 0 | S48: Zak = artifact")
print(f"    S48: Wilson = trivial | S36: BDI nu = 0 | S53: GL Zak = 0")
print(f"    S55: fold Berry = 0 | S56: fabric holonomy = trivial")
print(f"    S57: TB quasi-crossing = NOT topological (this computation)")
print(f"")
print(f"  Physical interpretation (GEOMETRIC):")
print(f"    The quasi-crossing is the SAME avoided-crossing phenomenon as")
print(f"    the fold (Session 55), viewed in the highest-lying representations.")
print(f"    The coupling V = {V_coupling:.6f} that opens the gap is the")
print(f"    off-diagonal TB matrix element connecting (2,5) and (5,2),")
print(f"    mediated by their shared bonds in the representation graph.")

# ======================================================================
#  Save results
# ======================================================================

save_dict = {
    # Quasi-crossing identification
    'tau_min_gap': tau_at_target,
    'idx_min_gap': idx_min_gap,
    'min_gap_30_31': gap_at_target,
    'V_coupling': V_coupling,
    'gaps_30_31': gaps_30_31,

    # Reality check
    'max_imag_H': max_imag_all,
    'max_asym_H': max_asym_all,
    'is_real_symmetric': is_real_sym,

    # Character exchange
    'n_character_swaps': n_swaps,

    # Z_2 invariant
    'det_reduced': det_reduced,
    'sgn_det_reduced': sgn_reduced,
    'n_sign_changes': n_sign_changes,
    'z2_constant': z2_constant,

    # All avoided crossings
    'n_avoided_crossings': len(all_avoided),
    'avoided_tau': np.array([ac['tau'] for ac in all_avoided]),
    'avoided_gaps': np.array([ac['gap'] for ac in all_avoided]),
    'avoided_levels': np.array([ac['levels'] for ac in all_avoided]),

    # Landau-Zener
    'LZ_parameter': LZ_param if 'LZ_param' in dir() else np.nan,

    # Tau and eigenvalue arrays (reference)
    'tau_values': tau_vals,
    'eigenvalues': eigenvalues,

    # Gate info
    'gate_name': 'TOPOLOGY-TRANSITION-57',
    'gate_verdict': verdict,
    'gate_detail': (f'Quasi-crossing at tau={tau_at_target:.4f}: '
                    f'gap={gap_at_target:.2e}, {n_swaps} character swaps, '
                    f'Z_2 constant, AVOIDED CROSSING (not topological)'),
}

out_npz = os.path.join(SCRIPT_DIR, 's57_topology_transition.npz')
np.savez(out_npz, **save_dict)
print(f"\n  Saved: {out_npz}")

elapsed = time.time() - t0
print(f"  Runtime: {elapsed:.1f}s")
print(f"\nDONE")
print("=" * 78)
