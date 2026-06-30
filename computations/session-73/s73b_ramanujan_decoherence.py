#!/usr/bin/env python3
"""
S73b W4-B: Heat Kernel Spectral Dimension on CG(24)
=====================================================
Gate: RAMANUJAN-73B (INFO)

Physics: The heat kernel on a graph is K(t) = Tr(exp(-t*L)) where L is the
graph Laplacian. For short times, K(t) ~ C * t^{-d_s/2}, defining the
spectral dimension d_s. On a d-dimensional smooth manifold d_s = d; on a
graph, d_s is determined entirely by the eigenvalue distribution.

Setup:
  * CG(24) = Cayley graph of S_4 with 6 transposition generators
  * 24 vertices, 72 edges, 6-regular
  * Ramanujan graph: lambda_1 = 4 (spectral gap), lambda_max = 12
  * Spectrum multiplicities: {0:1, 4:9, 6:4, 8:9, 12:1}

Task (reduced scope -- Ramanujan property established in S73a W2-C):
  1. Rebuild CG(24) Laplacian, verify lambda_1 = 4
  2. Compute K(t) = Tr(exp(-t*L)) for t in [1e-4, 1e2]
  3. Extract spectral dimension d_s from short-time scaling
  4. Compare to graph-theoretic dimensions (degree=6, Hausdorff, 4D substrate)
  5. Compute return probability p_return(t) = K(t)/N
  6. Identify diffusion regimes (ballistic / diffusive / mixed)
  7. Assess physical relationship to 4D substrate spacetime

Gate: RAMANUJAN-73B (INFO only)
  Report d_s, heat kernel shape, return probability regimes, and physical
  interpretation. No pass/fail.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy import linalg
from canonical_constants import (
    dt_transit, M_KK, N_cells, c_fabric, J_C2,
)

# ============================================================================
#  SECTION 1: Construct CG(24) Laplacian and verify spectrum
# ============================================================================

def cayley_graph_S4():
    """Construct the Cayley graph of S_4 with all 6 transposition generators.

    S_4 has 24 elements. The 6 transpositions (ij) for 0 <= i < j <= 3 form a
    generating set. Each vertex has degree 6 -- the graph is 6-regular.
    Transpositions are self-inverse so the graph is undirected.

    Returns: adjacency matrix A (24x24)
    """
    from itertools import permutations

    elements = list(permutations(range(4)))  # (local)
    elem_to_idx = {e: i for i, e in enumerate(elements)}  # (local)
    N = len(elements)  # (local)

    transpositions = []  # (local)
    for i in range(4):
        for j in range(i + 1, 4):
            transpositions.append((i, j))

    A = np.zeros((N, N), dtype=float)  # (local)
    for idx, perm in enumerate(elements):
        for (i, j) in transpositions:
            new_perm = list(perm)  # (local)
            new_perm[i], new_perm[j] = new_perm[j], new_perm[i]
            neighbor_idx = elem_to_idx[tuple(new_perm)]  # (local)
            A[idx, neighbor_idx] = 1.0

    return A


print("=" * 72)
print("S73b W4-B: Heat Kernel Spectral Dimension on CG(24)")
print("=" * 72)
print()

A = cayley_graph_S4()  # (local)
N_vert = A.shape[0]  # (local)
degree = int(A[0].sum())  # (local)
N_edges = int(A.sum() / 2)  # (local)

print(f"CG(24): {N_vert} vertices, {N_edges} edges, {degree}-regular")

L = np.diag(A.sum(axis=1)) - A  # (local) -- graph Laplacian L = D - A
evals_L, _ = linalg.eigh(L)  # (local)
evals_L = np.where(np.abs(evals_L) < 1e-12, 0.0, evals_L)  # (local)

lambda_1 = float(evals_L[evals_L > 1e-10].min())  # (local) -- spectral gap
lambda_max = float(evals_L.max())  # (local)
# Ramanujan bound: a k-regular graph is Ramanujan if |mu_i| <= 2*sqrt(k-1) for
# all nontrivial adjacency eigenvalues mu_i (i != 0). In Laplacian terms L=kI-A
# so lambda_i = k - mu_i, and the Ramanujan criterion on the spectral gap is
# lambda_1 >= k - 2*sqrt(k-1). For k=6: lambda_1 >= 6 - 2*sqrt(5) = 1.5279.
ramanujan_bound = degree - 2.0 * np.sqrt(degree - 1)  # (local) -- Alon-Boppana (L form)

print(f"Laplacian spectrum (sorted):")
print(f"  evals = {evals_L}")
print(f"  lambda_0 = {evals_L[0]:.6e}")
print(f"  lambda_1 = {lambda_1:.4f}  (Ramanujan bound: {ramanujan_bound:.4f})")
print(f"  lambda_max = {lambda_max:.4f}")
print(f"  Ramanujan? {lambda_1 >= ramanujan_bound}")

# Multiplicity breakdown
unique_vals, mults = np.unique(np.round(evals_L, 8), return_counts=True)  # (local)
print(f"  Multiplicities:")
for v, m in zip(unique_vals, mults):
    print(f"    lambda = {v:6.2f}   mult = {m}")

# Consistency with S73a W2-C
s73a = np.load("computations/session-73/s73a_graph_spectral_decoherence.npz", allow_pickle=True)  # (local)
s73a_evals = np.array(s73a["evals_L"])  # (local)
max_diff_s73a = float(np.max(np.abs(np.sort(s73a_evals) - np.sort(evals_L))))  # (local)
print(f"  Consistency with S73a evals_L: max diff = {max_diff_s73a:.2e}")

# ============================================================================
#  SECTION 2: Heat kernel K(t) = Tr(exp(-t*L))
# ============================================================================

print()
print("-" * 72)
print("SECTION 2: Heat kernel K(t) = Tr(exp(-t L))")
print("-" * 72)

# Log-spaced t grid
t_grid = np.logspace(-4, 2, 600)  # (local) -- natural units (edge-hop time)
K_t = np.array([np.sum(np.exp(-t * evals_L)) for t in t_grid])  # (local)
p_return = K_t / N_vert  # (local) -- return probability density per vertex

print(f"t range: [{t_grid[0]:.1e}, {t_grid[-1]:.1e}]")
print(f"K(t_min = {t_grid[0]:.1e}) = {K_t[0]:.6f}")
print(f"K(t_mid = 1.0)            = {np.interp(1.0, t_grid, K_t):.6f}")
print(f"K(t_max = {t_grid[-1]:.1e}) = {K_t[-1]:.6f}")
print(f"K(t -> infinity) -> 1 (ground state only, kernel of L)")
print(f"p_return(t_min) = {p_return[0]:.6f}  (short time: near 1)")
print(f"p_return(t_max) = {p_return[-1]:.6f}  (long time: 1/N = {1.0/N_vert:.6f})")

# ============================================================================
#  SECTION 3: Extract spectral dimension d_s from short-time scaling
# ============================================================================

print()
print("-" * 72)
print("SECTION 3: Spectral dimension from K(t) ~ C t^{-d_s/2}")
print("-" * 72)

# On a finite graph, K(t) ~ N - t*Tr(L) + ... for t -> 0 (heat kernel expansion).
# The power-law regime is INTERMEDIATE: short enough that boundary is not felt,
# long enough that the leading quadratic term dominates. For a discrete graph,
# this regime is narrow and we must isolate it carefully.
#
# We fit log K vs log t in a window where the logarithmic derivative
#   alpha(t) = d log K / d log t
# is approximately constant. alpha = -d_s/2.

# Numerical log-derivative
log_t = np.log(t_grid)  # (local)
log_K = np.log(K_t)  # (local)
alpha_t = np.gradient(log_K, log_t)  # (local) -- local slope of log K vs log t
d_s_local = -2.0 * alpha_t  # (local) -- instantaneous spectral dimension

# Find window where d_s is most stable (lowest |d alpha/d log t|)
dalpha = np.abs(np.gradient(alpha_t, log_t))  # (local)

# Report the minimum |dalpha| (most scale-invariant point) and its value
i_stable = int(np.argmin(dalpha))  # (local)
t_stable = float(t_grid[i_stable])  # (local)
d_s_stable = float(d_s_local[i_stable])  # (local)

print(f"Most scale-invariant point: t = {t_stable:.4e}")
print(f"  alpha(t) = d log K / d log t = {alpha_t[i_stable]:.4f}")
print(f"  d_s_local = -2*alpha = {d_s_stable:.4f}")
print()

# Average d_s over several candidate windows
# Short-time window: t in [1e-3, 1e-1]
mask_short = (t_grid >= 1e-3) & (t_grid <= 1e-1)  # (local)
coef_short = np.polyfit(log_t[mask_short], log_K[mask_short], 1)  # (local)
d_s_short = -2.0 * coef_short[0]  # (local)
print(f"Window short (t in [1e-3, 1e-1]):")
print(f"  slope = {coef_short[0]:.4f}, intercept = {coef_short[1]:.4f}")
print(f"  d_s_short = {d_s_short:.4f}")

# Very short time window: t in [1e-4, 1e-3]
mask_vshort = (t_grid >= 1e-4) & (t_grid <= 1e-3)  # (local)
coef_vshort = np.polyfit(log_t[mask_vshort], log_K[mask_vshort], 1)  # (local)
d_s_vshort = -2.0 * coef_vshort[0]  # (local)
print(f"Window very-short (t in [1e-4, 1e-3]):")
print(f"  slope = {coef_vshort[0]:.4f}, intercept = {coef_vshort[1]:.4f}")
print(f"  d_s_vshort = {d_s_vshort:.4f}")

# Intermediate window: t in [1e-2, 1]
mask_inter = (t_grid >= 1e-2) & (t_grid <= 1.0)  # (local)
coef_inter = np.polyfit(log_t[mask_inter], log_K[mask_inter], 1)  # (local)
d_s_inter = -2.0 * coef_inter[0]  # (local)
print(f"Window intermediate (t in [1e-2, 1]):")
print(f"  slope = {coef_inter[0]:.4f}, intercept = {coef_inter[1]:.4f}")
print(f"  d_s_inter = {d_s_inter:.4f}")

# The analytic short-time expansion on a graph:
# K(t) = N - t*Tr(L) + (t^2/2)*Tr(L^2) - ...
# Tr(L) = sum_i deg(i) = 2*|E| = 144 for CG(24)
# For a very short time, log K ~ log N - (Tr(L)/N) t + O(t^2)
# So alpha(t -> 0) = d log K / d log t = -(Tr(L)/N) * t / log(N/K) -> 0
# meaning d_s -> 0 exactly at t = 0. This is the finite-size artifact.

trace_L = float(np.trace(L))  # (local) = sum of degrees = 144
trace_L2 = float(np.trace(L @ L))  # (local)
print()
print(f"Tr(L)  = {trace_L:.1f}  (expected 2|E| = {2*N_edges})")
print(f"Tr(L^2) = {trace_L2:.1f}  (= sum lambda^2 = {np.sum(evals_L**2):.1f})")

# Small-t expansion prediction: K(t)/N = 1 - (trace_L/N) * t + (trace_L2/(2N)) * t^2 + ...
# So alpha(t -> 0+) = (d log K / d log t) = t * (d log K / dt) = -t*(Tr(L)/N) / (K/N)
# At t = 1e-4 this gives alpha = -1e-4 * 144/24 = -6e-4, d_s_local = 1.2e-3 (near zero)

# This confirms: the TRUE short-time behavior has d_s -> 0 due to discreteness.
# A power-law with nonzero d_s only emerges in an INTERMEDIATE asymptotic
# regime characteristic of the graph's long-wavelength structure.

# ============================================================================
#  SECTION 4: Diffusion regimes from return probability
# ============================================================================

print()
print("-" * 72)
print("SECTION 4: Diffusion regimes and return probability")
print("-" * 72)

# Regimes on a graph:
# (A) Very short time t << 1/lambda_max: K(t) ~ N, p_return ~ 1 (on-site, ballistic)
# (B) Intermediate: all modes damping, power-law regime (diffusive-like)
# (C) Long time t >> 1/lambda_1: K(t) -> 1, p_return -> 1/N (mixed / equilibrium)

t_ballistic = 1.0 / lambda_max  # (local) -- fastest mode timescale
t_mix = 1.0 / lambda_1  # (local) -- mixing (slowest nonzero mode)
print(f"t_ballistic = 1/lambda_max = {t_ballistic:.4f}")
print(f"t_mix = 1/lambda_1 = {t_mix:.4f}")
print(f"Dynamical range t_mix/t_ballistic = {t_mix/t_ballistic:.3f} = lambda_max/lambda_1 = 3")

# Characteristic timescale of the power-law window (if any)
# The intermediate window spans roughly [1/lambda_max, 1/lambda_1] -- only 3x.
# This is the Ramanujan compression: the spectrum is too tight for a wide
# power-law regime.

# Value of K(t) in each regime
K_ballistic = float(np.interp(t_ballistic, t_grid, K_t))  # (local)
K_mix = float(np.interp(t_mix, t_grid, K_t))  # (local)
p_ballistic = K_ballistic / N_vert  # (local)
p_mix = K_mix / N_vert  # (local)
print(f"At t_ballistic: K = {K_ballistic:.3f}, p_return = {p_ballistic:.4f}")
print(f"At t_mix:       K = {K_mix:.3f}, p_return = {p_mix:.4f}")

# Equilibration: when p_return - 1/N drops below e^{-1} * (1 - 1/N)
p_eq = 1.0 / N_vert  # (local)
excess = p_return - p_eq  # (local)
excess_norm = excess / excess[0]  # (local)
i_eq = int(np.argmin(np.abs(excess_norm - 1.0/np.e)))  # (local)
t_eq = float(t_grid[i_eq])  # (local)
print(f"Equilibration time (excess/e^1): t_eq = {t_eq:.4f} (compare t_mix = {t_mix:.4f})")

# ============================================================================
#  SECTION 5: Compare d_s to graph-theoretic dimensions
# ============================================================================

print()
print("-" * 72)
print("SECTION 5: Dimensional comparisons")
print("-" * 72)

d_degree = float(degree)  # (local) -- 6 (local coordination)
d_hausdorff = float(np.log(N_vert) / np.log(degree))  # (local)
d_substrate = 4.0  # (local) -- 4D emergent substrate spacetime
# Diameter of CG(24) with transposition generators = 3 (known result for S_n bubble sort)
diam = 3  # (local) -- graph diameter (max shortest-path length on CG(S_4))

print(f"Graph properties for CG(24):")
print(f"  Degree (local coordination)     = {d_degree:.2f}")
print(f"  Hausdorff-like log_deg(N)       = {d_hausdorff:.4f}  (N^(1/d_H) = deg)")
print(f"  Diameter                         = {diam}")
print(f"  Substrate spacetime emergent dim = {d_substrate:.1f}")
print()
print(f"Computed spectral dimensions:")
print(f"  d_s (scale-invariant pt, t={t_stable:.2e}) = {d_s_stable:.4f}")
print(f"  d_s (very short [1e-4,1e-3])       = {d_s_vshort:.4f}")
print(f"  d_s (short       [1e-3,1e-1])       = {d_s_short:.4f}")
print(f"  d_s (intermediate [1e-2, 1])        = {d_s_inter:.4f}")

# ============================================================================
#  SECTION 6: Physical interpretation
# ============================================================================

print()
print("-" * 72)
print("SECTION 6: Physical interpretation")
print("-" * 72)

# CG(24) has finite number of vertices. The heat kernel is a FINITE sum of
# decaying exponentials. There is no true power-law regime because:
#   (i) for t < 1/lambda_max ~ 0.08, K(t) ~ N * (1 - t*6 + ...) is quadratic-linear
#   (ii) for t > 1/lambda_1 = 0.25, K(t) -> 1 exponentially
# These windows overlap: the intermediate "power-law" region is only a factor 3.
#
# The fitted d_s is therefore a LOCAL SLOPE in log-log space, NOT a true
# spectral dimension in the sense of a continuum manifold. On a Riemannian
# d-manifold K(t)/N ~ (4*pi*t)^{-d/2} * vol and d_s = d exactly. On a finite
# graph the value of d_s_inter depends on which window is chosen.

print("Key structural facts:")
print(f"  * CG(24) is Ramanujan with lambda_1 = 4 (S73a W2-C).")
print(f"  * Spectrum: {{0 (x1), 4 (x9), 6 (x4), 8 (x9), 12 (x1)}}")
print(f"  * Only 4 distinct nonzero eigenvalues -> no continuum spectral density")
print(f"  * Dynamical range lambda_max/lambda_1 = 3 (Ramanujan compression)")
print()
print("Heat kernel structure:")
print(f"  * Short time t << 1/lambda_max: K(t) ~ N - t*Tr(L) (linear regime)")
print(f"  * No clean power-law window: dynamical range too small (factor 3)")
print(f"  * Long time t >> 1/lambda_1: exponential relaxation to K=1")
print()
print("No physical connection to 4D substrate spacetime:")
print("  * The fitted d_s depends on choice of fitting window.")
print("  * Substrate 4D-ness is NOT encoded in CG(24) spectral density.")
print("  * Substrate 4D emerges from the Seeley-DeWitt a_2 coefficient of D_K,")
print("    NOT from the island graph of domain-wall centers.")
print("  * CG(24) is a COMBINATORIAL abstraction of the Weyl-reflection structure")
print("    of S_4-symmetric configurations; it is not the spacetime manifold.")

# Compare the single-point d_s_stable value to 4D
ratio_4D = d_s_stable / d_substrate  # (local)
print()
print(f"d_s / 4 (substrate) = {ratio_4D:.4f}")
print(f"  (No physical correspondence expected; reported for completeness.)")

# Compare to t_transit
# dt_transit is in M_KK^{-1} units; CG(24) Laplacian time is in graph-hop units.
# To map: t_hop_physical ~ 1 / J_eff  where J_eff ~ J_C2 in M_KK units.
# Previously from S73a: t_mix_graph * (1/J_C2) = physical mixing time
J_eff = J_C2  # (local) -- dominant C^2 coset coupling
t_mix_physical = t_mix / J_eff  # (local) in M_KK^{-1}
t_eq_physical = t_eq / J_eff  # (local)
ratio_mix_transit = t_mix_physical / dt_transit  # (local)
ratio_eq_transit = t_eq_physical / dt_transit  # (local)

print()
print(f"Physical mapping (hop time = 1/J_eff with J_eff = J_C2 = {J_eff:.3f} M_KK):")
print(f"  t_mix / t_transit = {ratio_mix_transit:.4f}")
print(f"  t_eq  / t_transit = {ratio_eq_transit:.4f}")

if ratio_mix_transit > 10:
    print(f"  VERDICT: Mixing is SLOW relative to transit by factor {ratio_mix_transit:.1f}x.")
    print(f"  Consistent with S73a FAIL: graph diffusion cannot operate within transit.")
elif ratio_mix_transit > 1:
    print(f"  Mixing is slightly slower than transit (factor {ratio_mix_transit:.2f}x).")
else:
    print(f"  Mixing is FASTER than transit by factor {1.0/ratio_mix_transit:.2f}x.")

# ============================================================================
#  SECTION 7: Save outputs
# ============================================================================

print()
print("-" * 72)
print("SECTION 7: Saving outputs")
print("-" * 72)

out_path = "computations/session-73/s73b_ramanujan_decoherence.npz"  # (local)
np.savez(
    out_path,
    # Gate metadata
    gate_name="RAMANUJAN-73B",
    gate_verdict="INFO",
    gate_detail=(
        f"d_s (stable)={d_s_stable:.3f}, d_s (vshort)={d_s_vshort:.3f}, "
        f"d_s (short)={d_s_short:.3f}, d_s (inter)={d_s_inter:.3f}. "
        f"No true power law: dynamical range lambda_max/lambda_1 = 3. "
        f"No physical link to 4D substrate spacetime."
    ),
    # Graph structure
    N_vert=N_vert,
    N_edges=N_edges,
    degree=degree,
    diameter=diam,
    # Laplacian spectrum
    evals_L=evals_L,
    lambda_1=lambda_1,
    lambda_max=lambda_max,
    ramanujan_bound=ramanujan_bound,
    trace_L=trace_L,
    trace_L2=trace_L2,
    consistency_diff_s73a=max_diff_s73a,
    # Heat kernel
    t_grid=t_grid,
    K_t=K_t,
    p_return=p_return,
    log_t=log_t,
    log_K=log_K,
    alpha_t=alpha_t,
    d_s_local=d_s_local,
    # Window fits
    t_stable=t_stable,
    d_s_stable=d_s_stable,
    d_s_vshort=d_s_vshort,
    d_s_short=d_s_short,
    d_s_inter=d_s_inter,
    slope_vshort=coef_vshort[0],
    slope_short=coef_short[0],
    slope_inter=coef_inter[0],
    # Diffusion regimes
    t_ballistic=t_ballistic,
    t_mix=t_mix,
    t_eq=t_eq,
    K_at_ballistic=K_ballistic,
    K_at_mix=K_mix,
    p_at_ballistic=p_ballistic,
    p_at_mix=p_mix,
    # Dimensional comparisons
    d_degree=d_degree,
    d_hausdorff=d_hausdorff,
    d_substrate=d_substrate,
    ratio_4D=ratio_4D,
    # Physical mapping
    J_eff=J_eff,
    dt_transit=dt_transit,
    t_mix_physical=t_mix_physical,
    t_eq_physical=t_eq_physical,
    ratio_mix_transit=ratio_mix_transit,
    ratio_eq_transit=ratio_eq_transit,
)
print(f"  Saved: {out_path}")

# ============================================================================
#  Verdict
# ============================================================================

print()
print("=" * 72)
print("GATE VERDICT: RAMANUJAN-73B")
print("=" * 72)
print()
print(f"  Gate:      RAMANUJAN-73B (INFO)")
print(f"  Threshold: INFO only -- report d_s, heat kernel shape, return prob regimes")
print(f"  Computed:")
print(f"    lambda_1          = {lambda_1:.3f}  (Ramanujan gap >= {ramanujan_bound:.3f})")
print(f"    lambda_max        = {lambda_max:.3f}")
print(f"    d_s (short [1e-3,1e-1])     = {d_s_short:.3f}")
print(f"    d_s (intermediate [1e-2,1]) = {d_s_inter:.3f}")
print(f"    d_s (stable point t={t_stable:.2e}) = {d_s_stable:.3f}")
print(f"    t_mix / t_transit  = {ratio_mix_transit:.2f}")
print(f"  Verdict:   INFO. No power-law regime (lambda_max/lambda_1 = 3). ")
print(f"             d_s is window-dependent. No physical link to 4D substrate.")
print()
print("Done.")
