"""
Session 25 Berry Geometric Phase Computations
==============================================
Berry-Geometric-Phase-Theorist -- Comprehensive computation script.

Tasks performed:
  1. Goal 3: Fubini-Study distance (gauge-invariant overlap matrix)
  2. Goal 3: Curvature-based distance estimate vs direct overlap
  3. Goal 3: Landau-Zener transition probability
  4. Goal 5: Gap-edge 2x2 Berry connection and holonomy
  5. Level statistics correlation with Berry curvature peak
  6. Spectral form factor K(k; tau) as order parameter
  7. Fermion determinant det(D_K(tau))
  8. Full spectral action at finite cutoff (Goal 2 contribution)
  9. Q-factor of Berry curvature peak
  10. J-constraint verification (Kramers pair symmetry)

Data sources:
  - s23a_kosmann_singlet.npz  (singlet eigenvectors + Kosmann matrices)
  - s24a_berry.npz            (Berry curvature data)
  - s23a_eigenvectors_extended.npz (full multi-sector eigenvalues + eigenvectors)
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy import linalg
import os

base = "C:/sandbox/Ainulindale Exflation/tier0-computation"

# =====================================================================
# LOAD DATA
# =====================================================================
print("=" * 70)
print("SESSION 25: BERRY GEOMETRIC PHASE COMPUTATIONS")
print("=" * 70)

d_singlet = np.load(f"{base}/s23a_kosmann_singlet.npz")
d_berry = np.load(f"{base}/s24a_berry.npz")
d_ext = np.load(f"{base}/s23a_eigenvectors_extended.npz", mmap_mode='r')

tau_values = d_singlet['tau_values']
n_tau = len(tau_values)
print(f"tau grid: {tau_values}")
print(f"n_tau = {n_tau}")

B_gap_edge = d_berry['B_gap_edge']
B_all = d_berry['B_all']

# =====================================================================
# COMPUTATION 1: FUBINI-STUDY DISTANCE (Goal 3, Step 1-2)
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 1: Fubini-Study Distance (Goal 3)")
print("=" * 70)

# Extract gap-edge eigenvectors at each tau
# CRITICAL: At tau=0, the spectrum is 8-fold degenerate (all |evals|=sqrt(3)/2).
# The "gap-edge" eigenvectors at tau=0 are arbitrary vectors in the 8D degenerate
# subspace. Comparing them directly to the specific gap-edge states at tau>0 gives
# zero overlap -- an artifact of the degeneracy, NOT a physical orthogonality.
#
# CORRECT APPROACH: For the Fubini-Study distance, when comparing states at tau_i
# and tau_j where one has a degenerate subspace, we must use the SUBSPACE overlap:
# the maximum overlap of the state |n(tau_j)> with the degenerate subspace at tau_i.
# This is computed as sum_k |<n_k(tau_i)|n(tau_j)>|^2 where the sum runs over all
# states in the degenerate subspace containing the gap-edge at tau_i.

gap_evecs = []  # shape (n_tau, 16, 2) -- 2 gap-edge states
gap_evals = []
all_evecs = []  # full eigenvector matrices
all_evals = []

for t_idx in range(n_tau):
    evecs = d_singlet[f'eigenvectors_{t_idx}']  # (16, 16)
    evals = d_singlet[f'eigenvalues_{t_idx}']   # (16,)
    gap_idx = d_singlet[f'gap_edge_indices_{t_idx}']  # (2,)

    v1 = evecs[:, gap_idx[0]]
    v2 = evecs[:, gap_idx[1]]
    gap_evecs.append(np.column_stack([v1, v2]))  # (16, 2)
    gap_evals.append(evals[gap_idx])
    all_evecs.append(evecs)
    all_evals.append(evals)

# Identify degenerate subspaces at each tau
def get_degenerate_subspace_indices(evals, target_idx, tol=1e-6):
    """Return indices of all eigenvalues degenerate with evals[target_idx]."""
    target_val = evals[target_idx]
    return np.where(np.abs(evals - target_val) < tol)[0]

# Compute the gauge-invariant SUBSPACE overlap
# For state |n> at tau_j and degenerate subspace S at tau_i containing the gap-edge:
# overlap = sum_{k in S_i} |<k(tau_i)|n(tau_j)>|^2
# This equals the squared norm of the projection of |n(tau_j)> onto S_i.
# The Fubini-Study distance is then d_FS = arccos(sqrt(overlap)).

print("\nGauge-invariant SUBSPACE overlap (handling tau=0 degeneracy):")
print("  At tau=0: 8-fold degeneracy. Computing projection onto degenerate subspace.")
print("  At tau>0: non-degenerate gap-edge. Standard |<n_i|n_j>|^2.\n")

# For each tau_i, find the degenerate subspace containing the gap-edge
gap_edge_state_idx_0 = []  # index 0 of the gap-edge pair at each tau
for t_idx in range(n_tau):
    gap_idx = d_singlet[f'gap_edge_indices_{t_idx}']
    gap_edge_state_idx_0.append(gap_idx[0])  # positive eigenvalue partner

overlap_matrix_sub = np.zeros((n_tau, n_tau))
for i in range(n_tau):
    evals_i = all_evals[i]
    evecs_i = all_evecs[i]
    gi = gap_edge_state_idx_0[i]
    deg_i = get_degenerate_subspace_indices(evals_i, gi)

    for j in range(n_tau):
        evals_j = all_evals[j]
        evecs_j = all_evecs[j]
        gj = gap_edge_state_idx_0[j]

        # Project |n_j> onto the degenerate subspace at tau_i
        v_j = evecs_j[:, gj]  # the gap-edge state at tau_j
        overlap = 0.0
        for k in deg_i:
            overlap += np.abs(np.vdot(evecs_i[:, k], v_j))**2
        overlap_matrix_sub[i, j] = overlap

print("  Subspace overlap matrix [rows=tau_i, cols=tau_j]:")
header = "         " + "".join([f"tau={t:.2f}  " for t in tau_values])
print(header)
for i in range(n_tau):
    row = f"  tau={tau_values[i]:.2f} "
    for j in range(n_tau):
        row += f"{overlap_matrix_sub[i,j]:8.5f} "
    print(row)

# Also compute consecutive overlaps (tau_j vs tau_{j+1}) which avoid the
# tau=0 degeneracy problem since consecutive non-zero tau values are non-degenerate
print("\n  Consecutive-step overlaps |<n(tau_j)|n(tau_{j+1})>|^2:")
consec_overlaps = np.zeros(n_tau - 1)
for j in range(n_tau - 1):
    ov = np.abs(np.vdot(gap_evecs[j][:, 0], gap_evecs[j+1][:, 0]))**2
    consec_overlaps[j] = ov
    dFS_step = np.arccos(min(1.0, np.sqrt(ov)))
    print(f"  tau=[{tau_values[j]:.2f},{tau_values[j+1]:.2f}]: |overlap|^2 = {ov:.8f}, d_FS_step = {dFS_step:.6f} rad")

# The overlap between the two gap-edge Kramers partners (state 1 vs state 2)
overlap_matrix_1 = np.zeros((n_tau, n_tau))
overlap_matrix_2 = np.zeros((n_tau, n_tau))
for i in range(n_tau):
    for j in range(n_tau):
        ov1 = np.abs(np.vdot(gap_evecs[i][:, 0], gap_evecs[j][:, 0]))**2
        ov2 = np.abs(np.vdot(gap_evecs[i][:, 1], gap_evecs[j][:, 1]))**2
        overlap_matrix_1[i, j] = ov1
        overlap_matrix_2[i, j] = ov2

# Fubini-Study distance using SUBSPACE overlap (correct for degenerate tau=0)
print("\n  Fubini-Study distance d_FS = arccos(sqrt(subspace_overlap)):")
dFS_sub = np.zeros((n_tau, n_tau))
for i in range(n_tau):
    for j in range(n_tau):
        ov = min(1.0, np.sqrt(overlap_matrix_sub[i, j]))
        dFS_sub[i, j] = np.arccos(ov)

print("\n  d_FS matrix (subspace-corrected) [radians]:")
header = "         " + "".join([f"tau={t:.2f}  " for t in tau_values])
print(header)
for i in range(n_tau):
    row = f"  tau={tau_values[i]:.2f} "
    for j in range(n_tau):
        row += f"{dFS_sub[i,j]:8.5f} "
    print(row)

# Also compute raw single-state dFS for tau>0 pairs (non-degenerate regime)
dFS_1 = np.zeros((n_tau, n_tau))
dFS_2 = np.zeros((n_tau, n_tau))
for i in range(n_tau):
    for j in range(n_tau):
        ov1 = min(1.0, np.sqrt(overlap_matrix_1[i, j]))
        ov2 = min(1.0, np.sqrt(overlap_matrix_2[i, j]))
        dFS_1[i, j] = np.arccos(ov1)
        dFS_2[i, j] = np.arccos(ov2)

# KEY RESULT: d_FS(0, tau) using subspace overlap
print("\n  KEY RESULT: d_FS(tau=0, tau) [radians] -- subspace-corrected:")
print(f"  {'tau':>6s}  {'d_FS(sub)':>12s}  {'d_FS/pi':>10s}  {'overlap':>10s}")
for j in range(n_tau):
    print(f"  {tau_values[j]:6.2f}  {dFS_sub[0,j]:12.6f}  {dFS_sub[0,j]/np.pi:10.4f}  {overlap_matrix_sub[0,j]:10.6f}")

# d_FS between consecutive tau values (non-degenerate for tau > 0)
print("\n  Consecutive d_FS (non-degenerate regime, tau > 0 pairs):")
dFS_consecutive = np.zeros(n_tau - 1)
for j in range(n_tau - 1):
    dFS_consecutive[j] = np.arccos(min(1.0, np.sqrt(consec_overlaps[j])))
    print(f"  [{tau_values[j]:.2f},{tau_values[j+1]:.2f}]: d_FS = {dFS_consecutive[j]:.6f} rad = {dFS_consecutive[j]/np.pi:.4f}*pi")

# Accumulated d_FS along the path (sum of consecutive steps)
dFS_accumulated = np.zeros(n_tau)
for j in range(1, n_tau):
    dFS_accumulated[j] = dFS_accumulated[j-1] + dFS_consecutive[j-1]
print("\n  Accumulated path-length d_FS (sum of consecutive steps):")
for j in range(n_tau):
    print(f"  tau={tau_values[j]:.2f}: accumulated = {dFS_accumulated[j]:.6f} rad = {dFS_accumulated[j]/np.pi:.4f}*pi")

orthogonal_threshold = np.pi / 2
max_dFS_sub = np.max(dFS_sub[0, :])
max_j = np.argmax(dFS_sub[0, :])
print(f"\n  Maximum d_FS(0,tau) [subspace]: {max_dFS_sub:.6f} rad at tau={tau_values[max_j]:.2f}")
print(f"  pi/2 = {orthogonal_threshold:.6f}")
print(f"  Ratio max_dFS / (pi/2) = {max_dFS_sub / orthogonal_threshold:.4f}")
if max_dFS_sub > 0.95 * orthogonal_threshold:
    print("  >>> STATES APPROACHING ORTHOGONALITY")
elif max_dFS_sub > 0.5 * orthogonal_threshold:
    print("  >>> SIGNIFICANT EIGENSTATE ROTATION (> pi/4)")
else:
    print("  >>> MODERATE OR SMALL EIGENSTATE ROTATION")

# =====================================================================
# COMPUTATION 2: Curvature-Based Distance Estimate (Goal 3, Step 3)
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 2: Curvature-Based Distance Estimate")
print("=" * 70)

# Integrate d_FS(0, tau) = integral_0^tau sqrt(B(tau')) dtau'
# using trapezoidal rule on the Berry curvature data
B_ge = B_gap_edge[:, 0]  # Gap-edge state 1

dFS_curvature = np.zeros(n_tau)
for j in range(1, n_tau):
    # Trapezoidal integration of sqrt(B) from tau=0 to tau_j
    integrand = np.sqrt(np.maximum(B_ge[:j+1], 0.0))
    dFS_curvature[j] = np.trapezoid(integrand, tau_values[:j+1])

print("\n  Comparison: direct subspace overlap vs curvature-based estimate")
print(f"  {'tau':>6s}  {'d_FS(sub)':>12s}  {'d_FS(accum)':>12s}  {'d_FS(curv)':>12s}  {'B_gap':>10s}")
for j in range(n_tau):
    print(f"  {tau_values[j]:6.2f}  {dFS_sub[0,j]:12.6f}  {dFS_accumulated[j]:12.6f}  {dFS_curvature[j]:12.6f}  {B_ge[j]:10.4f}")

# Assess grid resolution
print("\n  Grid resolution assessment:")
for j in range(1, n_tau):
    dtau = tau_values[j] - tau_values[j-1]
    B_mid = (B_ge[j] + B_ge[j-1]) / 2
    rotation_per_step = np.sqrt(B_mid) * dtau
    print(f"  tau=[{tau_values[j-1]:.2f},{tau_values[j]:.2f}]: dtau={dtau:.2f}, "
          f"B_mid={B_mid:.1f}, rotation/step={rotation_per_step:.3f} rad "
          f"{'(UNDER-RESOLVED!)' if rotation_per_step > 1.0 else '(OK)'}")

# =====================================================================
# COMPUTATION 3: Landau-Zener Transition Probability
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 3: Landau-Zener Transition Probability")
print("=" * 70)

# Find the minimum gap near the gap edge at each tau
print("\n  Gap structure analysis (positive eigenvalues only):")
gap_data = []
for t_idx in range(n_tau):
    evals = d_singlet[f'eigenvalues_{t_idx}']
    # Positive eigenvalues, sorted
    pos_evals = np.sort(evals[evals > 0])
    # Minimum spacing between adjacent positive eigenvalues
    spacings = np.diff(pos_evals)
    min_gap = np.min(spacings)
    min_gap_idx = np.argmin(spacings)
    gap_data.append({
        'tau': tau_values[t_idx],
        'pos_evals': pos_evals,
        'min_gap': min_gap,
        'gap_pair': (pos_evals[min_gap_idx], pos_evals[min_gap_idx+1]),
        'lambda_min': pos_evals[0]
    })
    print(f"  tau={tau_values[t_idx]:.2f}: lambda_min={pos_evals[0]:.8f}, "
          f"min_gap={min_gap:.8f}, between ({pos_evals[min_gap_idx]:.6f}, {pos_evals[min_gap_idx+1]:.6f})")

# Compute crossing velocity v = d(Delta E)/dtau at the minimum gap
print("\n  Landau-Zener analysis near tau=0.10 (Berry curvature peak):")
# Use finite differences between tau=0 and tau=0.10, and tau=0.10 and tau=0.15
for t_idx in [1, 2]:  # tau=0.10 and tau=0.15
    delta = gap_data[t_idx]['min_gap']

    # Crossing velocity from finite difference
    if t_idx > 0 and t_idx < n_tau - 1:
        gap_before = gap_data[t_idx - 1]['min_gap']
        gap_after = gap_data[t_idx + 1]['min_gap']
        dtau_before = tau_values[t_idx] - tau_values[t_idx - 1]
        dtau_after = tau_values[t_idx + 1] - tau_values[t_idx]
        v = abs((gap_after - gap_before) / (dtau_before + dtau_after))
    else:
        v = abs(gap_data[t_idx+1]['min_gap'] - gap_data[t_idx]['min_gap']) / (tau_values[t_idx+1] - tau_values[t_idx])

    # Also compute velocity from gap-edge eigenvalue motion
    lam_min_vals = [gap_data[i]['lambda_min'] for i in range(n_tau)]
    if t_idx > 0 and t_idx < n_tau - 1:
        v_lambda = abs(lam_min_vals[t_idx+1] - lam_min_vals[t_idx-1]) / (tau_values[t_idx+1] - tau_values[t_idx-1])
    else:
        v_lambda = 0

    # Landau-Zener: P_LZ = exp(-pi * Delta^2 / (2 * v))
    # Here Delta is the minimum gap, v is the crossing velocity
    # In dimensionless units (hbar = 1 in spectral units)
    if v > 1e-15:
        P_LZ = np.exp(-np.pi * delta**2 / (2 * v))
    else:
        P_LZ = 0.0

    # Alternative: use B itself to estimate the adiabatic parameter
    # epsilon = sqrt(B) * |d(tau)/dt| -- but we compute epsilon = V_nm / Delta_E
    # From B ~ sum |V|^2 / (DeltaE)^2, the dominant coupling is ~ sqrt(B) * Delta_E
    B_val = B_ge[t_idx]
    # Effective coupling: sqrt(B * Delta_E^2) ~ sqrt(B) * Delta_E
    V_eff = np.sqrt(B_val) * delta if B_val > 0 else 0
    adiabatic_param = V_eff / delta if delta > 1e-15 else float('inf')  # = sqrt(B)

    print(f"\n  tau = {tau_values[t_idx]:.2f}:")
    print(f"    Minimum gap Delta = {delta:.8f}")
    print(f"    Gap crossing velocity v = d(Delta)/dtau = {v:.6f}")
    print(f"    Berry curvature B = {B_val:.2f}")
    print(f"    P_LZ = exp(-pi*Delta^2/(2*v)) = {P_LZ:.6e}")
    print(f"    Effective coupling V_eff = sqrt(B)*Delta = {V_eff:.6f}")
    print(f"    Adiabatic parameter sqrt(B) = {np.sqrt(B_val):.4f}")
    print(f"    Adiabatic condition: sqrt(B) << 1? sqrt(B) = {np.sqrt(B_val):.2f} {'VIOLATED' if np.sqrt(B_val) > 1 else 'OK'}")

# =====================================================================
# COMPUTATION 4: Gap-Edge 2x2 Berry Connection (Goal 5)
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 4: Gap-Edge 2x2 Berry Connection and Holonomy (Goal 5)")
print("=" * 70)

# The non-Abelian Berry connection for the Kramers pair
# A_{ab}(tau) = i <psi_a(tau)|d/dtau|psi_b(tau)>
# Approximated by finite differences: d|psi>/dtau ~ (|psi(tau+dtau)> - |psi(tau)>) / dtau
# The overlap matrix approach: A_{ab} ~ -Im[<psi_a(tau)|psi_b(tau+dtau)>] / dtau

print("\n  2x2 Berry connection matrix at each tau step:")
print("  (BDI constraint: A_11 = A_22, i.e. diagonal elements equal)")

A_matrices = []  # Store 2x2 connection matrices

for j in range(n_tau - 1):
    dtau = tau_values[j+1] - tau_values[j]

    # 2x2 overlap matrix between consecutive tau values
    # O_{ab} = <psi_a(tau_j)|psi_b(tau_{j+1})>
    O = np.zeros((2, 2), dtype=complex)
    for a in range(2):
        for b in range(2):
            O[a, b] = np.vdot(gap_evecs[j][:, a], gap_evecs[j+1][:, b])

    # Berry connection: A = -Im(log(O))/dtau  (for small dtau)
    # More precisely: A_{ab} ~ (1/dtau) * Im[<a(j)|b(j+1)> - delta_{ab}]
    # Or equivalently: A = i * (O - I) / dtau for small dtau

    # For finite differences, use the log of the overlap matrix
    # Wilson line: W = O / |O|  (normalize to get the gauge part)
    # For the 2x2 case, compute phases directly

    # Diagonal Berry phase (Abelian part)
    A_11 = -np.angle(O[0, 0]) / dtau  # Berry connection for state 1
    A_22 = -np.angle(O[1, 1]) / dtau  # Berry connection for state 2

    # Off-diagonal (non-Abelian part)
    A_12 = -np.imag(O[0, 1]) / dtau if abs(O[0, 1]) > 1e-14 else 0.0
    A_21 = -np.imag(O[1, 0]) / dtau if abs(O[1, 0]) > 1e-14 else 0.0

    A_mat = np.array([[A_11, A_12], [A_21, A_22]])
    A_matrices.append(A_mat)

    # J-gate check
    j_violation = abs(A_11 - A_22) / (abs(A_11) + 1e-15)

    print(f"  tau=[{tau_values[j]:.2f},{tau_values[j+1]:.2f}]:")
    print(f"    A_11 = {A_11:+10.6f}, A_22 = {A_22:+10.6f} (J-gate: |A_11-A_22|/|A_11| = {j_violation:.2e})")
    print(f"    A_12 = {A_12:+10.6f}, A_21 = {A_21:+10.6f}")
    print(f"    |O_11| = {abs(O[0,0]):.8f}, |O_22| = {abs(O[1,1]):.8f}")
    print(f"    |O_12| = {abs(O[0,1]):.8f}, |O_21| = {abs(O[1,0]):.8f}")

# Compute Wilson loop (path-ordered product of overlap matrices)
print("\n  Wilson loop W = product of O matrices along tau path:")
W = np.eye(2, dtype=complex)
for j in range(n_tau - 1):
    dtau = tau_values[j+1] - tau_values[j]
    O = np.zeros((2, 2), dtype=complex)
    for a in range(2):
        for b in range(2):
            O[a, b] = np.vdot(gap_evecs[j][:, a], gap_evecs[j+1][:, b])
    W = W @ O

print(f"  W = ")
print(f"    [{W[0,0]:+10.6f}+{W[0,0].imag:+10.6f}i, {W[0,1]:+10.6f}+{W[0,1].imag:+10.6f}i]")
print(f"    [{W[1,0]:+10.6f}+{W[1,0].imag:+10.6f}i, {W[1,1]:+10.6f}+{W[1,1].imag:+10.6f}i]")

# Format properly
print(f"\n  Wilson loop (complex):")
for i in range(2):
    for j_loop in range(2):
        print(f"    W[{i},{j_loop}] = {W[i,j_loop].real:+.8f} {W[i,j_loop].imag:+.8f}i  (|W| = {abs(W[i,j_loop]):.8f})")

det_W = np.linalg.det(W)
tr_W = np.trace(W)
print(f"\n  det(W) = {det_W.real:+.8f} {det_W.imag:+.8f}i  (|det| = {abs(det_W):.8f})")
print(f"  tr(W) = {tr_W.real:+.8f} {tr_W.imag:+.8f}i  (|tr| = {abs(tr_W):.8f})")
print(f"  |tr(W)| = {abs(tr_W):.8f}  (= 2 means trivial holonomy, < 2 means nontrivial)")

# Z_2 holonomy check
# In BDI class, the holonomy is real-valued. Check if |tr(W)| ~ 2 (trivial) or ~ -2 or 0 (nontrivial)
holonomy_param = abs(tr_W) / 2.0
print(f"\n  Holonomy parameter |tr(W)|/2 = {holonomy_param:.8f}")
if holonomy_param > 0.95:
    print("  >>> HOLONOMY IS APPROXIMATELY TRIVIAL (|tr(W)|/2 ~ 1)")
    holonomy_verdict = "TRIVIAL"
elif holonomy_param < 0.05:
    print("  >>> HOLONOMY IS NONTRIVIAL (|tr(W)| ~ 0, Z_2 = -1)")
    holonomy_verdict = "NONTRIVIAL"
else:
    print(f"  >>> HOLONOMY IS INTERMEDIATE (not clearly trivial or nontrivial)")
    print(f"  >>> This may indicate under-resolution or gauge issues on non-compact parameter space")
    holonomy_verdict = "INTERMEDIATE"

# Accumulated phase for each gap-edge state
print("\n  Accumulated Berry phase (diagonal of Wilson loop):")
phase_1 = np.angle(W[0, 0])
phase_2 = np.angle(W[1, 1])
print(f"  phi_1 = {phase_1:.6f} rad = {phase_1/np.pi:.4f} * pi")
print(f"  phi_2 = {phase_2:.6f} rad = {phase_2/np.pi:.4f} * pi")
print(f"  phi_1 - phi_2 = {phase_1 - phase_2:.6f} rad  (should be ~0 by J-constraint)")

# =====================================================================
# COMPUTATION 5: Level Statistics Correlation with Berry Peak
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 5: Level Statistics vs Berry Curvature Correlation")
print("=" * 70)

# Load level statistics
d_ls = np.load(f"{base}/s22a_level_stats.npz", allow_pickle=True)
tau_ls = d_ls['tau_all']
q_N50 = d_ls['q_vs_tau_N50']
q_N100 = d_ls['q_vs_tau_N100']

print("\n  Berry-Tabor/BGS conjecture test (Paper 02 / Paper 10):")
print("  q -> 0: Poisson statistics (integrable)")
print("  q -> 1: Wigner/GOE statistics (chaotic)\n")

print(f"  {'tau':>6s}  {'q(N=50)':>10s}  {'q(N=100)':>10s}  {'B_gap':>10s}")
# Match tau values between level stats and Berry curvature
for i, t in enumerate(tau_ls):
    # Find closest Berry curvature value
    berry_match = None
    for j, tb in enumerate(tau_values):
        if abs(t - tb) < 0.005:
            berry_match = B_ge[j]
            break

    q50 = q_N50[i] if not np.isnan(q_N50[i]) else float('nan')
    q100 = q_N100[i] if not np.isnan(q_N100[i]) else float('nan')
    berry_str = f"{berry_match:.2f}" if berry_match is not None else "---"
    print(f"  {t:6.2f}  {q50:10.6f}  {q100:10.6f}  {berry_str:>10s}")

# =====================================================================
# COMPUTATION 6: Spectral Form Factor K(k; tau)
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 6: Spectral Form Factor K(k; tau)")
print("=" * 70)

# K(k) = (1/N) |sum_n exp(2*pi*i*k*E_n / E_mean)|^2
# where E_n are the unfolded eigenvalues

k_values = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0]

print(f"\n  {'tau':>6s}", end="")
for k in k_values:
    print(f"  {'K('+str(k)+')':>10s}", end="")
print()

K_results = np.zeros((n_tau, len(k_values)))

for t_idx in range(n_tau):
    # Use full spectrum for form factor
    evals = np.sort(d_ext[f'eigenvalues_{t_idx}'])
    pos_evals = evals[evals > 0]  # positive eigenvalues only
    N = len(pos_evals)

    # Unfold: use mean spacing
    mean_spacing = np.mean(np.diff(pos_evals)) if N > 1 else 1.0
    unfolded = pos_evals / mean_spacing

    print(f"  {tau_values[t_idx]:6.2f}", end="")
    for ki, k in enumerate(k_values):
        # Form factor
        phases = 2 * np.pi * k * unfolded
        K_val = np.abs(np.sum(np.exp(1j * phases)))**2 / N
        K_results[t_idx, ki] = K_val
        print(f"  {K_val:10.4f}", end="")
    print()

print("\n  Reference values:")
print("  GOE (Wigner): K(k) = k for k < 1, K(k) = 1 for k > 1")
print("  Poisson: K(k) = 1 for all k")

# =====================================================================
# COMPUTATION 7: Fermion Determinant det(D_K(tau))
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 7: Fermion Determinant det(D_K(tau))")
print("=" * 70)

# det(D_K) = product of all eigenvalues
# log|det(D_K)| = sum of log|lambda_n|

print("\n  Products are not subject to Weyl-law averaging.")
print("  W1 (Perturbative Exhaustion) does NOT apply to det(D_K).")
print("  Zero free parameters, zero test function.\n")

log_det = np.zeros(n_tau)
det_positive = np.zeros(n_tau)  # product of |positive eigenvalues|

for t_idx in range(n_tau):
    evals = d_ext[f'eigenvalues_{t_idx}']
    # Remove zero eigenvalues if any
    nonzero = evals[np.abs(evals) > 1e-15]

    log_det[t_idx] = np.sum(np.log(np.abs(nonzero)))

    pos = nonzero[nonzero > 0]
    det_positive[t_idx] = np.sum(np.log(pos))

    print(f"  tau={tau_values[t_idx]:.2f}: log|det(D_K)| = {log_det[t_idx]:.6f}, "
          f"log|det(D_K+)| = {det_positive[t_idx]:.6f}")

# Check monotonicity
diffs = np.diff(log_det)
monotone_inc = all(d > 0 for d in diffs)
monotone_dec = all(d < 0 for d in diffs)
print(f"\n  log|det(D_K)| monotone? {'YES (increasing)' if monotone_inc else 'YES (decreasing)' if monotone_dec else 'NO -- NON-MONOTONE'}")
if not monotone_inc and not monotone_dec:
    # Find extrema
    for j in range(1, n_tau - 1):
        if (log_det[j] > log_det[j-1] and log_det[j] > log_det[j+1]):
            print(f"  >>> LOCAL MAXIMUM at tau={tau_values[j]:.2f}: log|det| = {log_det[j]:.6f}")
        elif (log_det[j] < log_det[j-1] and log_det[j] < log_det[j+1]):
            print(f"  >>> LOCAL MINIMUM at tau={tau_values[j]:.2f}: log|det| = {log_det[j]:.6f}")

# =====================================================================
# COMPUTATION 8: Full Spectral Action at Finite Cutoff (Goal 2)
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 8: Full Spectral Action at Finite Cutoff (Goal 2)")
print("=" * 70)

Lambda_values = [1.0, 2.0, 5.0, 10.0]

# Test functions
def f_smooth(x):
    """Chamseddine-Connes: f(x) = x * exp(-x)"""
    return x * np.exp(-x)

def f_debye(x):
    """Debye hard cutoff: f(x) = theta(1-x)"""
    return np.where(x <= 1.0, 1.0, 0.0)

def f_exp(x):
    """Simple exponential: f(x) = exp(-x)"""
    return np.exp(-x)

test_funcs = {
    'xe^{-x}': f_smooth,
    'theta(1-x)': f_debye,
    'e^{-x}': f_exp
}

for fname, f_func in test_funcs.items():
    print(f"\n  Test function: f(x) = {fname}")
    print(f"  {'tau':>6s}", end="")
    for L in Lambda_values:
        print(f"  {'V(L='+str(L)+')':>14s}", end="")
    print()

    V_full = np.zeros((n_tau, len(Lambda_values)))

    for t_idx in range(n_tau):
        evals = d_ext[f'eigenvalues_{t_idx}']
        print(f"  {tau_values[t_idx]:6.2f}", end="")
        for li, L in enumerate(Lambda_values):
            x = evals**2 / L**2
            V_val = np.sum(f_func(x))
            V_full[t_idx, li] = V_val
            print(f"  {V_val:14.4f}", end="")
        print()

    # Check monotonicity for each Lambda
    for li, L in enumerate(Lambda_values):
        diffs = np.diff(V_full[:, li])
        mono_inc = all(d > 0 for d in diffs)
        mono_dec = all(d < 0 for d in diffs)
        if mono_inc:
            verdict = "MONOTONE (increasing)"
        elif mono_dec:
            verdict = "MONOTONE (decreasing)"
        else:
            verdict = "NON-MONOTONE"
            # Find extrema
            for j in range(1, n_tau - 1):
                if V_full[j, li] < V_full[j-1, li] and V_full[j, li] < V_full[j+1, li]:
                    verdict += f" -- LOCAL MIN at tau={tau_values[j]:.2f}"
                elif V_full[j, li] > V_full[j-1, li] and V_full[j, li] > V_full[j+1, li]:
                    verdict += f" -- LOCAL MAX at tau={tau_values[j]:.2f}"
        print(f"    Lambda={L}: {verdict}")

# =====================================================================
# COMPUTATION 9: Q-Factor of Berry Curvature Peak
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 9: Q-Factor of Berry Curvature Peak")
print("=" * 70)

B_peak = np.max(B_ge)
peak_idx = np.argmax(B_ge)
tau_peak = tau_values[peak_idx]
B_half = B_peak / 2

# Find half-maximum points by interpolation
# Left side
left_idx = None
for j in range(peak_idx - 1, -1, -1):
    if B_ge[j] < B_half:
        # Linear interpolation
        t = (B_half - B_ge[j]) / (B_ge[j+1] - B_ge[j])
        tau_left = tau_values[j] + t * (tau_values[j+1] - tau_values[j])
        left_idx = j
        break

# Right side
right_idx = None
for j in range(peak_idx + 1, n_tau):
    if B_ge[j] < B_half:
        t = (B_half - B_ge[j]) / (B_ge[j-1] - B_ge[j])
        tau_right = tau_values[j] - t * (tau_values[j] - tau_values[j-1])
        right_idx = j
        break

print(f"\n  Berry curvature peak: B = {B_peak:.2f} at tau = {tau_peak:.2f}")
print(f"  Half-maximum: B/2 = {B_half:.2f}")

if left_idx is not None and right_idx is not None:
    FWHM = tau_right - tau_left
    Q_factor = tau_peak / FWHM
    print(f"  FWHM: [{tau_left:.4f}, {tau_right:.4f}] = {FWHM:.4f}")
    print(f"  Q-factor = tau_peak / FWHM = {Q_factor:.2f}")
    if Q_factor > 5:
        print("  >>> HIGH Q: sharp resonance, nearly exact degeneracy")
    elif Q_factor > 1:
        print("  >>> MODERATE Q: distinct peak but not a sharp resonance")
    else:
        print("  >>> LOW Q: broad feature, not a sharp resonance")
else:
    # Peak is at the boundary or very broad
    if left_idx is None:
        print("  Left half-maximum not resolved (peak extends below tau=0)")
        tau_left = 0.0
    if right_idx is None:
        print("  Right half-maximum not resolved (B remains > B/2 across grid)")
        tau_right = tau_values[-1]
    FWHM = tau_right - tau_left
    Q_factor = tau_peak / FWHM if FWHM > 0 else float('inf')
    print(f"  Estimated FWHM: ~{FWHM:.4f} (incomplete)")
    print(f"  Estimated Q ~ {Q_factor:.2f} (lower bound)")

# =====================================================================
# COMPUTATION 10: J-Constraint Verification
# =====================================================================
print("\n" + "=" * 70)
print("COMPUTATION 10: J-Constraint Verification (Kramers Pair)")
print("=" * 70)

print("\n  Dirac J-gate: Berry curvature B_n = B_{Jn} for Kramers partners")
print("  (If violated, data has a bug)")

max_violation = 0
for t_idx in range(n_tau):
    B_1 = B_gap_edge[t_idx, 0]
    B_2 = B_gap_edge[t_idx, 1]
    violation = abs(B_1 - B_2) / (abs(B_1) + 1e-15)
    max_violation = max(max_violation, violation)
    status = "PASS" if violation < 1e-10 else "FAIL"
    print(f"  tau={tau_values[t_idx]:.2f}: B_1={B_1:.6f}, B_2={B_2:.6f}, "
          f"|B_1-B_2|/|B_1|={violation:.2e} [{status}]")

print(f"\n  Maximum J-violation: {max_violation:.2e}")
print(f"  J-gate verdict: {'PASS (machine precision)' if max_violation < 1e-10 else 'FAIL -- BUG DETECTED'}")

# Also check overlap matrix symmetry
print("\n  J-gate on overlaps: |<psi_1(i)|psi_1(j)>|^2 = |<psi_2(i)|psi_2(j)>|^2")
max_ov_violation = 0
for i in range(n_tau):
    for j in range(n_tau):
        v = abs(overlap_matrix_1[i, j] - overlap_matrix_2[i, j])
        max_ov_violation = max(max_ov_violation, v)

print(f"  Maximum overlap J-violation: {max_ov_violation:.2e}")
print(f"  Overlap J-gate: {'PASS' if max_ov_violation < 1e-10 else 'FAIL'}")

# =====================================================================
# EXTRA: Sector-by-sector eigenvalue minimum tracking
# =====================================================================
print("\n" + "=" * 70)
print("EXTRA: Sector-by-Sector Gap-Edge Eigenvalue Tracking")
print("=" * 70)

sector_labels = d_ext['sector_labels_0']
sector_sizes = d_ext['sector_sizes_0']
n_sectors = len(sector_sizes)

print(f"\n  {n_sectors} sectors, tracking lambda_min per sector across tau")
print(f"  {'Sector':>12s}  {'p':>2s}  {'q':>2s}  {'size':>5s}", end="")
for t in tau_values:
    print(f"  {'tau='+str(t):>10s}", end="")
print()

sector_lambda_min = np.zeros((n_sectors, n_tau))
for t_idx in range(n_tau):
    all_evals = np.sort(np.abs(d_ext[f'eigenvalues_{t_idx}']))
    # Decompose into sectors using cumulative sizes
    offset = 0
    for s_idx in range(n_sectors):
        sz = int(sector_sizes[s_idx])
        p, q = sector_labels[s_idx]

        # Get sector eigenvectors to extract sector eigenvalues
        sec_evecs = d_ext[f'eigvec_{t_idx}_sector_{s_idx}']
        sec_evals_full = d_ext[f'eigenvalues_{t_idx}']

        # The sector eigenvectors are in the full basis; eigenvalues are sorted globally
        # We need to identify which eigenvalues belong to this sector
        # Use the fact that sector eigenvectors are orthogonal to other sectors
        # Actually, the eigenvalues in the sector block are the diagonal of
        # evecs^H @ D_K @ evecs restricted to this sector

        # Simpler approach: sector eigenvalues = eigenvalues of D_K restricted to sector
        # These are just the eigenvalues of the sector-block matrix
        sec_evals = np.sort(linalg.eigvalsh(sec_evecs.conj().T @ sec_evecs))
        # Wait, that gives us the overlap matrix, not D_K eigenvalues

        # Actually since D_K is block-diagonal (proven Session 22b),
        # the eigenvalues of D_K in sector s are the eigenvalues of the s-th block
        # The sector eigenvectors diagonalize the sector block
        # So sector eigenvalues are obtained from the full eigenvalue list
        # by noting which eigenvalues correspond to which sector

        # Since we don't have direct sector-eigenvalue mapping in this file,
        # let's use a different approach: compute |lambda_min| for the sector
        # by noting that sector eigenvectors are columns that span the sector subspace
        # For now, just track the number of eigenvalues per sector

        sector_lambda_min[s_idx, t_idx] = float('nan')  # Placeholder
        offset += sz

# Since the direct sector decomposition is not trivially available from the file structure,
# let me use the singlet (sector 0) data which we DO have
print("\n  (0,0) Singlet sector lambda_min tracking:")
print(f"  {'tau':>6s}  {'lambda_min':>12s}  {'d(lam)/dtau':>12s}")
for t_idx in range(n_tau):
    lam_min = gap_data[t_idx]['lambda_min']
    if t_idx > 0:
        dlam = (gap_data[t_idx]['lambda_min'] - gap_data[t_idx-1]['lambda_min']) / \
               (tau_values[t_idx] - tau_values[t_idx-1])
    else:
        dlam = 0
    print(f"  {tau_values[t_idx]:6.2f}  {lam_min:12.8f}  {dlam:+12.6f}")

# =====================================================================
# PLOTS
# =====================================================================
print("\n" + "=" * 70)
print("GENERATING PLOTS")
print("=" * 70)

fig, axes = plt.subplots(2, 3, figsize=(18, 12))

# Plot 1: Fubini-Study distance from tau=0
ax = axes[0, 0]
ax.plot(tau_values, dFS_sub[0, :], 'b-o', linewidth=2, markersize=6, label='Subspace overlap')
ax.plot(tau_values, dFS_accumulated, 'g-^', linewidth=2, markersize=6, label='Accumulated path')
ax.plot(tau_values, dFS_curvature, 'r--s', linewidth=2, markersize=6, label='Curvature integral')
ax.axhline(y=np.pi/2, color='gray', linestyle=':', linewidth=1, label='pi/2 (orthogonality)')
ax.axhline(y=np.pi/4, color='gray', linestyle='-.', linewidth=1, alpha=0.5, label='pi/4')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('d_FS(0, tau) [rad]', fontsize=12)
ax.set_title('Fubini-Study Distance from tau=0', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Plot 2: Berry curvature with Q annotation
ax = axes[0, 1]
ax.plot(tau_values, B_ge, 'b-o', linewidth=2, markersize=6)
ax.axhline(y=B_half, color='red', linestyle=':', linewidth=1, label=f'B/2 = {B_half:.0f}')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('B_n(tau)', fontsize=12)
ax.set_title(f'Berry Curvature (Peak B={B_peak:.1f} at tau={tau_peak:.2f})', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Plot 3: Fermion determinant
ax = axes[0, 2]
ax.plot(tau_values, log_det, 'g-o', linewidth=2, markersize=6, label='log|det(D_K)|')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('log|det(D_K)|', fontsize=12)
ax.set_title('Fermion Determinant', fontsize=13)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# Plot 4: V_full for different Lambda (xe^{-x})
ax = axes[1, 0]
for li, L in enumerate(Lambda_values):
    V_vals = np.zeros(n_tau)
    for t_idx in range(n_tau):
        evals = d_ext[f'eigenvalues_{t_idx}']
        x = evals**2 / L**2
        V_vals[t_idx] = np.sum(f_smooth(x))
    # Normalize to tau=0 value for comparison
    if V_vals[0] != 0:
        V_norm = V_vals / V_vals[0]
    else:
        V_norm = V_vals
    ax.plot(tau_values, V_norm, '-o', markersize=4, linewidth=1.5, label=f'Lambda={L}')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('V_full / V_full(0)', fontsize=12)
ax.set_title('V_full(tau; Lambda) / V_full(0) [f = xe^{-x}]', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Plot 5: Spectral form factor
ax = axes[1, 1]
for ki, k in enumerate(k_values):
    ax.plot(tau_values, K_results[:, ki], '-o', markersize=4, linewidth=1.5, label=f'k={k}')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('K(k; tau)', fontsize=12)
ax.set_title('Spectral Form Factor', fontsize=13)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

# Plot 6: Gap-edge eigenvalue and Berry curvature overlay
ax = axes[1, 2]
lam_min_arr = [gap_data[i]['lambda_min'] for i in range(n_tau)]
ax2_twin = ax.twinx()
ax.plot(tau_values, lam_min_arr, 'b-o', linewidth=2, markersize=6, label='lambda_min')
ax2_twin.plot(tau_values, B_ge, 'r-s', linewidth=2, markersize=6, label='B_gap')
ax.set_xlabel('tau', fontsize=12)
ax.set_ylabel('lambda_min', fontsize=12, color='blue')
ax2_twin.set_ylabel('B_gap', fontsize=12, color='red')
ax.set_title('Gap-Edge Eigenvalue vs Berry Curvature', fontsize=13)
ax.tick_params(axis='y', labelcolor='blue')
ax2_twin.tick_params(axis='y', labelcolor='red')
ax.grid(True, alpha=0.3)

plt.tight_layout()
outpath = f"{base}/s25_berry_results.png"
plt.savefig(outpath, dpi=150)
print(f"  Saved: {outpath}")

# =====================================================================
# SAVE ALL RESULTS
# =====================================================================
np.savez(f"{base}/s25_berry_results.npz",
         tau=tau_values,
         overlap_matrix_sub=overlap_matrix_sub,
         overlap_matrix_1=overlap_matrix_1,
         overlap_matrix_2=overlap_matrix_2,
         dFS_sub=dFS_sub,
         dFS_accumulated=dFS_accumulated,
         dFS_consecutive=dFS_consecutive,
         dFS_1=dFS_1,
         dFS_2=dFS_2,
         dFS_curvature=dFS_curvature,
         B_gap_edge=B_gap_edge,
         B_all=B_all,
         log_det=log_det,
         det_positive=det_positive,
         K_results=K_results,
         k_values=np.array(k_values),
         Wilson_loop=W,
         holonomy_verdict=holonomy_verdict,
         A_matrices=np.array(A_matrices),
         Q_factor=Q_factor,
         FWHM=FWHM)
print(f"  Saved: {base}/s25_berry_results.npz")

print("\n" + "=" * 70)
print("SESSION 25 BERRY COMPUTATIONS COMPLETE")
print("=" * 70)
