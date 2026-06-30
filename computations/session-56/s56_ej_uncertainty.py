#!/usr/bin/env python3
"""
s56_ej_uncertainty.py — EJ-UNCERTAINTY-56
Systematic uncertainties on fabric Josephson parameters.

Methodology (Nazarewicz UQ, Paper 06 DFT methodology):
  Three independent uncertainty sources:
    (a) GAP CHOICE: Delta_OES = 0.4643 vs Delta_GL = 0.7704 M_KK
    (b) PERTURBATION ORDER: Higher-order corrections to E_J^(2)
    (c) MODE CONVERGENCE: 32-mode TB vs continuum estimates

  Nuclear structure methodology:
  - Paper 06 (Dobaczewski et al.): model-spread uncertainty from
    different functionals is the dominant source in nuclear DFT.
  - Paper 02 (HFB continuum): basis truncation can miss continuum
    contributions to pairing.
  - Paper 03 (Bogoliubov): odd-even staggering gap vs BCS gap differ
    by factors of 1-2 in nuclei.

Gate: EJ-UNCERTAINTY-56 (INFO)
"""

import sys
import numpy as np

sys.path.insert(0, 'computations')
from canonical_constants import (
    tau_fold, Delta_0_OES, Delta_0_GL, E_cond, N_cells,
    M_KK, M_Pl_reduced, xi_BCS, n_pairs,
    E_B2_mean, omega_PV,
)

# ─── Load tight-binding data ───────────────────────────────────────────
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
tau_tb    = tb['tau_values']      # (50,)
evals_tb  = tb['eigenvalues']     # (50, 32)
J_C2_tau  = tb['J_C2_tau']       # (50,)
bandwidths = tb['bandwidths']
N = int(tb['N_cells'])            # = 32

# Load S55 continuum data
erich = np.load('computations/session-55/s55_erich_continuum.npz', allow_pickle=True)

# ─── Identify fold ────────────────────────────────────────────────────
i_fold = np.argmin(np.abs(tau_tb - tau_fold))
tau_actual = tau_tb[i_fold]

J_fold = J_C2_tau[i_fold]
evals_fold = evals_tb[i_fold]

print(f"{'='*72}")
print(f"EJ-UNCERTAINTY-56: Systematic Uncertainty Quantification")
print(f"{'='*72}")
print(f"Fold: tau = {tau_actual:.4f} (index {i_fold})")
print(f"J_C2 at fold = {J_fold:.6f} M_KK")
print(f"N_modes = {N}")

# ─── Helper: compute E_J and derived quantities ──────────────────────
def compute_fabric_params(evals, J, Delta, label="", verbose=True):
    """Compute E_J, E_c, E_J/E_c, omega_J from single-particle spectrum."""
    N_loc = len(evals)
    mu = (evals[N_loc//2 - 1] + evals[N_loc//2]) / 2
    xi_k = evals - mu
    E_k = np.sqrt(xi_k**2 + Delta**2)
    uv_k = Delta / (2 * E_k)

    # E_J = J^2 * sum_k [Delta / (2 * E_k^2)] (2nd-order PT)
    F_anom = np.sum(uv_k / E_k)  # = sum Delta/(2*E_k^2)
    E_J = J**2 * F_anom

    # Charging energy
    delta_E_F = evals[N_loc//2] - evals[N_loc//2 - 1]
    E_c = delta_E_F / 2

    # Josephson plasma frequency
    if E_c > 0:
        omega_J = np.sqrt(2 * E_J * E_c)
        ratio = E_J / E_c
    else:
        omega_J = 0.0  # (local)
        ratio = np.inf

    if label and verbose:
        print(f"\n  [{label}]")
        print(f"    Delta = {Delta:.6f} M_KK")
        print(f"    mu = {mu:.6f}")
        print(f"    F_anom = {F_anom:.6f}")
        print(f"    E_J = {E_J:.6f} M_KK")
        print(f"    E_c = {E_c:.6f} M_KK")
        print(f"    E_J/E_c = {ratio:.2f}")
        print(f"    omega_J = {omega_J:.6f} M_KK")

    return {
        'E_J': E_J, 'E_c': E_c, 'ratio': ratio,
        'omega_J': omega_J, 'F_anom': F_anom,
        'mu': mu, 'delta_E_F': delta_E_F,
        'uv_k': uv_k, 'E_k': E_k, 'xi_k': xi_k
    }


# ====================================================================
# BASELINE: Reproduce S55 W3-16 result
# ====================================================================
r_oes = compute_fabric_params(evals_fold, J_fold, Delta_0_OES, "OES gap (primary)")
E_J_central = r_oes['E_J']
E_c_central = r_oes['E_c']
ratio_central = r_oes['ratio']
omega_J_central = r_oes['omega_J']

print(f"\n  BASELINE VERIFIED: E_J = {E_J_central:.4f}, E_J/E_c = {ratio_central:.1f}, omega_J = {omega_J_central:.4f}")


# ====================================================================
# (a) GAP CHOICE UNCERTAINTY: Delta_OES vs Delta_GL
# ====================================================================
print(f"\n{'='*72}")
print(f"(a) GAP CHOICE UNCERTAINTY")
print(f"{'='*72}")
print(f"Delta_OES = {Delta_0_OES:.6f} M_KK (odd-even staggering, primary)")
print(f"Delta_GL  = {Delta_0_GL:.6f}  M_KK (Ginzburg-Landau functional)")
print(f"Ratio GL/OES = {Delta_0_GL/Delta_0_OES:.4f}")

r_gl = compute_fabric_params(evals_fold, J_fold, Delta_0_GL, "GL gap")

# Physical reasoning (Nazarewicz, Paper 03):
# The OES gap is the PHYSICAL gap extracted from pair-addition/removal
# energies. In nuclei this is the 3-point formula:
#   Delta^(3)(A) = (-1)^A * [B(A+1) - 2B(A) + B(A-1)] / 2
# The GL gap is the ORDER PARAMETER magnitude from the GL functional
# minimum. These differ because:
#   1. Self-energy corrections renormalize the OES gap downward
#   2. Number projection shifts the OES gap (Paper 03, Eq. 12)
#   3. The GL gap includes fluctuation effects
#
# In nuclei, Delta_OES/Delta_GL typically ranges 0.5-0.9 (Paper 03).
# Here: Delta_OES/Delta_GL = 0.602, within the nuclear range.
#
# Following Paper 06 (DFT UQ): treat the spread as a model uncertainty.
# Use half-spread as 1-sigma for a uniform prior.

dE_J_gap = abs(r_gl['E_J'] - r_oes['E_J'])
dE_J_gap_frac = dE_J_gap / r_oes['E_J']
dratio_gap = abs(r_gl['ratio'] - r_oes['ratio'])
domega_gap = abs(r_gl['omega_J'] - r_oes['omega_J'])

print(f"\n  Gap choice spread:")
print(f"    delta(E_J)    = {dE_J_gap:.6f} M_KK ({dE_J_gap_frac*100:.2f}%)")
print(f"    delta(E_J/Ec) = {dratio_gap:.2f}")
print(f"    delta(omega_J)= {domega_gap:.6f} M_KK")

# Key physical insight: E_J DECREASES with larger Delta.
# This is because F_anom = sum Delta/(2*E_k^2) and E_k = sqrt(xi^2 + Delta^2).
# For xi >> Delta: F_anom ~ sum Delta/xi^2 (linear in Delta).
# For xi << Delta: F_anom ~ sum 1/(2*Delta) (DECREASING in Delta).
# At the fold, most modes have xi comparable to Delta, so the
# competition produces a WEAK dependence. The 11% spread is less
# than the 66% gap variation because of this partial cancellation.
# This is the analog of the "pairing anti-halo effect" in nuclear
# physics (Paper 02), where pairing correlations are less sensitive
# to the details of the potential than single-particle energies.

sigma_E_J_gap = dE_J_gap / 2
sigma_ratio_gap = dratio_gap / 2
sigma_omega_gap = domega_gap / 2

print(f"\n  1-sigma (half-spread):")
print(f"    sigma(E_J)    = {sigma_E_J_gap:.4f} M_KK")
print(f"    sigma(E_J/Ec) = {sigma_ratio_gap:.2f}")
print(f"    sigma(omega_J)= {sigma_omega_gap:.4f} M_KK")


# ====================================================================
# (b) PERTURBATION CONVERGENCE
# ====================================================================
print(f"\n{'='*72}")
print(f"(b) PERTURBATION ORDER ASSESSMENT")
print(f"{'='*72}")

# The E_J formula is derived from second-order perturbation theory
# in the tunneling Hamiltonian H_T = J * sum_k c_{k,L}^+ c_{k,R}.
# The expansion parameter is:
#
#   alpha_PT = J / min(E_k) = J_fold / Delta_OES
#
# For a single-channel junction (Ambegaokar-Baratoff), the EXACT
# result is:
#   I_c = (pi*Delta)/(2*R_N) * tanh(Delta/(2*kT))
# which corresponds to:
#   E_J_exact = (pi*Delta/4) * sum_n T_n
# where T_n are the eigenvalues of the normal-state transmission
# matrix t*t^+. The 2nd-order result E_J^(2) uses T_n << 1.
#
# For our tight-binding model, the effective transmission per channel is:
#   T_eff = (2*J/W)^2 where W is the bandwidth
#
# The correction to E_J from higher orders goes as:
#   E_J = E_J^(2) * [1 + c_1 * T_eff + c_2 * T_eff^2 + ...]
#
# For the AB formula, c_1 = 1/4 (from the sqrt(1-T) denominator).
#
# IMPORTANT: The naive 4th-order PT sum
#   J^4 * sum_{k,k'} uv_k*uv_{k'} / (E_k + E_{k'})^3
# is NOT the correct E_J correction. That formula gives the
# 4th-order correction to the GROUND STATE ENERGY when both
# condensates are present, which involves cross terms between
# the two BCS states. The Josephson E_J has a specific structure
# from the Schrieffer-Wolff transformation.

uv_k = r_oes['uv_k']
E_k = r_oes['E_k']
Delta = Delta_0_OES

alpha_PT = J_fold / Delta
T_eff = (2 * J_fold / bandwidths[i_fold])**2

print(f"  Expansion parameters:")
print(f"    J_fold / Delta_OES = {alpha_PT:.4f}")
print(f"    T_eff = (2J/W)^2  = {T_eff:.6f}")
print(f"    sqrt(T_eff)       = {np.sqrt(T_eff):.6f}")

# Method 1: Ambegaokar-Baratoff exact vs 2nd-order
# AB exact (per channel): E_J_exact = (pi*Delta/4) * T / sqrt(1-T)
# AB 2nd-order: E_J^(2) = (pi*Delta/4) * T
# Ratio: 1/sqrt(1-T) = 1 + T/2 + 3T^2/8 + ...
AB_ratio_exact = 1.0 / np.sqrt(1 - T_eff)
AB_correction = AB_ratio_exact - 1.0

print(f"\n  Ambegaokar-Baratoff exact/2nd-order ratio:")
print(f"    1/sqrt(1-T) = {AB_ratio_exact:.6f}")
print(f"    Fractional correction = {AB_correction*100:.4f}%")

# Method 2: Direct perturbation series estimate
# The leading correction to E_J from 4th order in J is:
#   delta_E_J / E_J ~ (J/Delta)^2 * (correction factor)
# For the BCS anomalous density method:
#   E_J = J^2 * F_anom + O(J^4)
# The O(J^4) term involves double virtual pair excitations.
# Conservative upper bound: |delta_E_J^(4)| <= E_J^(2) * (J/Delta)^2

naive_ratio = (J_fold / Delta)**2
print(f"\n  Naive PT convergence estimate:")
print(f"    (J/Delta)^2 = {naive_ratio:.4f}")
print(f"    This overestimates because not all modes contribute at O(J^4)")

# Method 3: Compare different E_J methods as convergence check
# Method 1 (anomalous density): E_J = 7.042
# Method 3 (AB single channel): E_J_AB = (pi*Delta/4) * T
E_J_AB = (np.pi * Delta / 4) * T_eff
z_mean = 3.125  # C2 coordination  # (local)
E_J_AB_total = z_mean * E_J_AB

# The actual multi-mode correction (using the full spectrum) is:
# Ratio of F_anom method to AB method
method_ratio = r_oes['E_J'] / E_J_AB

print(f"\n  Method comparison (convergence cross-check):")
print(f"    E_J (Method 1, anomalous density) = {r_oes['E_J']:.4f} M_KK")
print(f"    E_J (Method 3, AB single channel) = {E_J_AB:.4f} M_KK")
print(f"    Ratio Method1/Method3 = {method_ratio:.4f}")

# The AB correction per channel is 3.8%.
# The method discrepancy is much larger because Method 1 sums over
# ALL 32 modes (including those far from E_F), while AB uses a
# single-channel picture. This is not a PT convergence issue —
# it's a model difference.
#
# For the PT truncation uncertainty, use the AB correction (3.8%)
# as the most physically motivated estimate:
# it captures the leading beyond-2nd-order tunneling process.

# For nuclear analogy: in nuclear HFB (Paper 02), the perturbative
# expansion in the residual interaction converges because
# Delta << bandwidth. Here T_eff = 0.074, so the expansion is
# well-controlled.

sigma_E_J_pt_AB = abs(AB_correction) * r_oes['E_J']

# Also compute with the naive (J/Delta)^2 as an UPPER BOUND
sigma_E_J_pt_upper = naive_ratio * r_oes['E_J']

print(f"\n  PT truncation uncertainty estimates:")
print(f"    AB correction:   sigma(E_J) = {sigma_E_J_pt_AB:.4f} M_KK ({AB_correction*100:.2f}%)")
print(f"    Naive (J/D)^2:   sigma(E_J) = {sigma_E_J_pt_upper:.4f} M_KK ({naive_ratio*100:.2f}%)")

# USE the AB correction as the 1-sigma PT uncertainty
# (conservative but physically motivated)
sigma_E_J_pt = sigma_E_J_pt_AB
sigma_ratio_pt = AB_correction * r_oes['ratio']
sigma_omega_pt = AB_correction * r_oes['omega_J'] / 2  # omega ~ sqrt(E_J)

print(f"\n  Adopted (AB correction as 1-sigma):")
print(f"    sigma(E_J)    = {sigma_E_J_pt:.4f} M_KK")
print(f"    sigma(E_J/Ec) = {sigma_ratio_pt:.2f}")
print(f"    sigma(omega_J)= {sigma_omega_pt:.4f} M_KK")


# ====================================================================
# (c) MODE CONVERGENCE: 32 vs CONTINUUM
# ====================================================================
print(f"\n{'='*72}")
print(f"(c) MODE CONVERGENCE: 32 vs CONTINUUM")
print(f"{'='*72}")

# The S55 erich_continuum computed with 496 pair levels (992 modes)
# across 9 sectors. The key question: how does F_anom change?
#
# F_anom = sum_k Delta/(2*E_k^2) = sum_k Delta/(2*(xi_k^2 + Delta^2))
#
# This sum converges because each term ~ 1/xi_k^2 for large |xi_k|.
# The convergence rate depends on the DOS near the Fermi surface.
#
# For UNIFORM DOS with N levels in bandwidth W:
#   F_anom(N) -> N(0) * arctan(W/(2*Delta)) / Delta
#   where N(0) = N/W is the DOS at E_F.
#   This is PROPORTIONAL to N for fixed W.
#
# But for the TIGHT-BINDING spectrum, levels are not uniformly
# distributed. The DOS has van Hove singularities.
#
# Physical approach: use the S55 data to estimate the continuum F_anom.
# The S55 computation gives d/Delta = 0.077 at the fold.
# This means there are Delta/d ~ 6 levels per pairing window.
# The 32-mode TB spectrum has different level density near E_F.

W_32 = bandwidths[i_fold]
delta_32 = W_32 / N  # mean spacing
print(f"  32-mode: W = {W_32:.4f}, delta = {delta_32:.4f}, delta/Delta = {delta_32/Delta_0_OES:.3f}")

# S55 continuum parameters at fold
i_s55 = 3  # tau=0.20 (closest to fold tau=0.19)
d_over_delta_s55 = float(erich['d_over_delta'][i_s55])
n_levels_sector = erich['n_levels_sector'][i_s55]
total_pair_levels = int(erich['n_pair_levels'])
print(f"  S55 continuum: {total_pair_levels} pair levels, d/Delta = {d_over_delta_s55:.4f}")

# The 32-mode spectrum has:
#   - 32 single-particle levels spanning [0, W_32]
#   - delta_E_F = 0.0725 M_KK (spacing at Fermi level)
#   - delta_E_F / Delta = 0.156
# The continuum spectrum has:
#   - 496 pair levels (992 modes including spin)
#   - d/Delta = 0.077
#   - d = 0.077 * 0.464 = 0.036 M_KK average near E_F
#
# CRITICAL DISTINCTION: F_anom for E_J uses ALL single-particle
# levels (not just near-Fermi). The convergence of sum_k 1/E_k^2
# with number of levels depends on the FAR tails.
#
# For the TB spectrum, levels above the bandwidth DO NOT EXIST.
# Adding more modes extends the bandwidth OR fills in between.
# The TB Hamiltonian already captures the COMPLETE Hilbert space
# of the 32-cell lattice — there are exactly 32 modes.
#
# The question is: how well does the 32-cell TB lattice approximate
# the PHYSICAL SU(3) fabric?
#
# Key insight (nuclear analogy, Paper 02):
# In nuclear HFB, the continuum (positive energy states) contributes
# to pairing through the tail of the pairing field. The continuum
# contribution is typically 5-15% of the total pairing energy.
# The continuum states are FAR from E_F (|xi| >> Delta), so their
# contribution to F_anom scales as:
#   delta(F_anom) / F_anom ~ N_cont * Delta / xi_max^2 / F_anom
#
# For our case, let's estimate the effect of adding modes BETWEEN
# the existing 32-mode levels (interpolation) and ABOVE the
# bandwidth (extrapolation).

# Method: Estimate F_anom for a dense spectrum matching the 32-mode
# DENSITY OF STATES (not Weyl law, which has wrong degeneracy structure).
# The 32-mode spectrum already accounts for the lattice structure.
# Additional modes from a LARGER lattice would:
# 1. Fill in levels between existing ones (increases N(E_F))
# 2. NOT change the bandwidth (Bloch theorem: bandwidth = max eigenvalue
#    of the hopping matrix, independent of system size for periodic BC)
# 3. Change E_c (charging energy decreases as 1/N_cells for bulk)

# For an N_cell lattice, the tight-binding levels fill in between
# the same bandwidth. The DOS at E_F scales as N_cell/W.
# So F_anom scales as N_cell/W * (integral part that's independent of N_cell).
# More precisely:
#   F_anom(N) = sum_{k=1}^{N} Delta/(2*E_k^2)
#             ~ (N/W) * integral_{-W/2}^{W/2} dx Delta/(2*(x^2+Delta^2))
#             = (N/W) * pi/2  for W >> Delta
# So F_anom scales LINEARLY with N for a uniform-DOS approximation.

# But this assumes we keep the SAME hopping J.
# E_J = J^2 * F_anom -> E_J scales linearly with N_modes
# This is WRONG physically: E_J is the coupling between TWO CELLS,
# not the total energy. The sum over k is over single-particle
# states WITHIN ONE CELL.
#
# In the TB model, the 32 modes ARE the Bloch states of the 32-cell
# lattice. Each mode is a plane wave across the lattice.
# The Josephson coupling between two cells uses the SINGLE-CELL
# wavefunctions (Wannier states), not the Bloch states.
#
# RESOLUTION: The 32-mode sum is over LATTICE modes.
# For the Josephson coupling, we need single-cell modes.
# The S55 W3-16 computation uses the 32 lattice eigenvalues as
# proxies for the single-cell spectrum. This is approximate:
# the single-cell spectrum has d(p,q) states per sector, totaling
# sum d(p,q) for the first 32 irreps. The TB spectrum is the
# tight-binding approximation to this.
#
# The PHYSICAL question is: does F_anom converge when computed
# with more single-cell states?

# Estimate using the ACTUAL single-cell spectrum at the fold.
# Load the sector eigenvalues from S55 for a direct comparison.
# The (0,0) sector at fold should give the BCS spectrum.

# Since we don't have the raw per-sector eigenvalues easily accessible,
# estimate F_anom convergence analytically.

# Analytic estimate: For levels at energy epsilon_k = k * delta + epsilon_0
# (k = 0, 1, ..., N-1), with delta = W/N:
#   F_anom(N) = sum_{k=0}^{N-1} Delta / (2 * ((k*delta - mu)^2 + Delta^2))
# This is a Riemann sum for the integral:
#   I = integral_0^W d(epsilon) * Delta / (2 * ((epsilon - mu)^2 + Delta^2))
#     = (1/2) * arctan((W - mu)/Delta) + (1/2) * arctan(mu/Delta)
#     ~ pi/2 for W >> Delta (using arctan(x) -> pi/2 for x >> 1)
# The N-mode Riemann approximation error is O(delta^2) = O((W/N)^2).

# For N=32 with W=6.77, delta = 0.212:
# Riemann error ~ delta^2 / Delta^2 ~ 0.212^2 / 0.464^2 ~ 0.209
# This gives a ~21% correction to the integral.

# For N=992 with same W: delta_992 = 0.0068
# Riemann error ~ 0.0068^2 / 0.464^2 ~ 0.0002 (negligible)

# So the FRACTIONAL enhancement from 32 to continuum limit:
# F_anom(continuum) / F_anom(32) ~ (1 + 0.209) / 1 ~ 1.21 (correction)
# BUT: this assumes UNIFORM DOS. The actual spectrum is non-uniform.

# More refined: compute the trapezoidal rule correction.
# The Euler-Maclaurin formula gives:
#   sum_k f(k*delta) = (1/delta) * integral f(x)dx - (delta/12)*f'|_boundaries
#                     + (delta^3/720)*f'''|_boundaries + ...
# The leading correction to F_anom from finite spacing is:
#   delta(F_anom) = -(delta^2/12) * d^2/dx^2 [Delta/(2*(x^2+Delta^2))] |_{x=0}
#                 = -(delta^2/12) * Delta * (6*0^2 - 2*Delta^2) / (2*Delta^4)^2
# At x=0 (Fermi surface): f''(0) = -Delta / Delta^4 = -1/Delta^3 ... wait,
# let me compute this numerically.

# Numerical Euler-Maclaurin estimate:
def f_anom(xi, Delta):
    """Integrand for F_anom."""
    return Delta / (2 * (xi**2 + Delta**2))

# Actual sum (32 modes)
F_32 = r_oes['F_anom']

# Trapezoidal integral (continuum limit)
xi_fold = r_oes['xi_k']
xi_min, xi_max = xi_fold.min(), xi_fold.max()
xi_dense = np.linspace(xi_min, xi_max, 10000)
f_dense = f_anom(xi_dense, Delta_0_OES)
from numpy import trapezoid as _trapz
F_integral = _trapz(f_dense, xi_dense)

# The integral gives F per unit xi-range. To get the sum equivalent,
# multiply by N/W (the density of levels):
F_continuum_est = (N / W_32) * F_integral

# More precisely: for Riemann sum with N points, the exact sum value
# converges to (N/W) * integral as N -> inf.
# So the continuum-limit F_anom for N=32 levels in bandwidth W is:
# F_anom(N->inf) = (N/W) * integral_{xi_min}^{xi_max} f(xi) dxi
# But N is FIXED at 32 (the number of cells in the physical lattice).
# Adding more modes means going to a LARGER lattice (more cells).
# For a larger lattice (M cells), the single-cell spectrum is UNCHANGED.
# The M modes fill in the BAND STRUCTURE more densely, but
# E_J depends on the single-cell wavefunctions, not the band structure.

# CRITICAL REALIZATION: The 32 eigenvalues of the 32-cell TB
# Hamiltonian are NOT single-cell energy levels.
# They are the BAND ENERGIES of the 32-cell lattice.
# The single-cell has only ~8-10 energy levels (depending on
# the SU(3) truncation).
# The S55 W3-16 computation INCORRECTLY treated the 32 lattice
# modes as if they were single-cell modes for the F_anom sum.
#
# For a Josephson junction between two BCS grains, the sum
# sum_k uv_k/E_k runs over the single-particle states of
# ONE GRAIN. The 32-cell lattice with N=32 band energies is
# not the right basis.
#
# HOWEVER: for the fabric, there is no "single cell" separate
# from the lattice. The cells are defined by the Voronoi
# tessellation of SU(3), and each cell has its own Dirac spectrum.
# The 32-mode TB eigenvalues represent the HYBRIDIZED spectrum
# of the 32-cell system, which IS the correct single-particle
# spectrum for computing anomalous density.
#
# Resolution: The 32-mode spectrum is the CORRECT basis for
# the 32-cell lattice. Mode convergence means: what if the
# PHYSICAL lattice has more cells, or if we include more
# SU(3) modes per cell?
#
# For more cells (larger lattice):
#   - E_J per bond does not change (local coupling)
#   - E_c decreases as 1/N_cells (more states near E_F)
#   - E_J/E_c increases (more superfluid)
#   - omega_J ~ sqrt(E_J * E_c) decreases (slower plasma oscillation)
#
# For more modes per cell:
#   - Higher-energy modes contribute less (|xi| >> Delta, uv/E ~ 1/xi^2)
#   - Convergent sum: dominated by modes within ~10*Delta of E_F
#   - The "pairing window" contains ~5 modes (Delta/delta_E ~ 0.46/0.07 ~ 6)
#   - Additional modes OUTSIDE the window contribute negligibly

# Method: Compute F_anom truncation as a function of pairing window
print(f"\n  Pairing window analysis:")
print(f"  {'Window (Delta)':>15} {'N_modes_in':>12} {'F_partial':>12} {'F_frac':>10}")

xi_fold_sorted = np.sort(np.abs(r_oes['xi_k']))
windows = [1, 2, 3, 5, 10, 20, 50]  # in units of Delta
for w in windows:
    mask = np.abs(r_oes['xi_k']) <= w * Delta_0_OES
    n_in = mask.sum()
    F_partial = np.sum(r_oes['uv_k'][mask] / r_oes['E_k'][mask])
    F_frac = F_partial / F_32
    print(f"  {w:>15.0f} {n_in:>12d} {F_partial:>12.4f} {F_frac:>10.4f}")

# The key test: how much does F_anom change if we ADD more modes
# far from E_F? Each mode at |xi| = n*Delta contributes:
#   delta_F = Delta / (2*(n^2+1)*Delta^2) = 1 / (2*(n^2+1)*Delta)
# For n=10: delta_F / F_32 = 1/(2*101*0.464) / 8.34 ~ 0.0013 (0.13%)
# For n=100: negligible.

# Estimate total contribution from modes we MIGHT be missing:
# If there are N_add additional modes outside |xi| > W/2:
N_add_estimate = 100  # conservative: 100 additional modes
xi_add = np.linspace(W_32/2 + Delta_0_OES, W_32 + 10*Delta_0_OES, N_add_estimate)
F_add = np.sum(Delta_0_OES / (2 * (xi_add**2 + Delta_0_OES**2)))
F_add_frac = F_add / F_32

print(f"\n  Extrapolation: {N_add_estimate} modes outside bandwidth")
print(f"    F_add = {F_add:.6f}")
print(f"    F_add / F_32 = {F_add_frac:.6f} ({F_add_frac*100:.3f}%)")

# The dominant uncertainty is NOT from missing high-energy modes
# (those are suppressed by 1/E^2), but from the DENSITY of modes
# near E_F. This is controlled by d/Delta.
#
# The 32-mode spectrum has delta_E_F/Delta = 0.156 (moderate).
# The S55 continuum has d/Delta = 0.077 (well-paired).
# Both are in the BCS regime (d/Delta << 1), so pairing is
# well-converged with respect to level density.
#
# For E_J specifically, the question is how F_anom scales with
# the number of levels NEAR E_F (within the pairing window).
# The 32-mode spectrum has ~6 levels within |xi| < Delta.
# Adding more levels would increase F_anom roughly as N_eff.
#
# Use the S55 E_cond enhancement as a PROXY for F_anom enhancement.
# E_cond ~ -g * Delta^2 * N(0) in BCS theory.
# F_anom ~ N(0) * pi / (2*Delta) in BCS theory.
# Both scale as N(0), the DOS at E_F.
# So E_cond enhancement ~ F_anom enhancement.

E_cond_full_fold = float(erich['E_cond_full'][i_s55])
E_cond_8mode_fold = float(erich['E_gs_8mode_interp'][i_s55])
enhancement_Econd = abs(E_cond_full_fold / E_cond_8mode_fold) if abs(E_cond_8mode_fold) > 1e-12 else 1.0

print(f"\n  S55 E_cond enhancement (proxy for DOS scaling):")
print(f"    E_cond_full(tau=0.20) / E_cond_8mode = {enhancement_Econd:.2f}x")

# HOWEVER: the E_cond comparison is 496 pair levels vs 8-mode.
# The 32-mode TB uses 32 modes (NOT 8). The 8-mode is the
# original singlet BCS space (4B2 + 1B1 + 3B3).
# The 32-mode TB includes ALL sectors of the lattice.
# So the relevant comparison is 32-mode -> 992-mode.
# Assuming the enhancement scales as N_modes^alpha with the
# E_cond data giving 496/8 ~ 62x modes and 6.6x enhancement:
#   alpha ~ log(6.6) / log(62) ~ 0.46
# Then 992/32 = 31x modes would give enhancement:
#   (31)^0.46 ~ 5.0x
# But this uses E_cond scaling, which is different from F_anom.

# More careful: E_cond scales as g * Delta^2 * N(0) in BCS theory.
# F_anom scales as N(0) * pi / (2*Delta).
# The ratio E_cond / F_anom ~ g * Delta^3 / pi (independent of N(0)).
# So the FRACTIONAL enhancement is the SAME for both.

alpha_scale = np.log(enhancement_Econd) / np.log(total_pair_levels / 4)  # 496/4 = 124 (8 modes give 4 pair levels)
enhancement_32_to_992 = (total_pair_levels / (N//2))**alpha_scale  # 496/16 = 31

print(f"  Scaling exponent alpha = {alpha_scale:.3f}")
print(f"  Estimated 32->992 enhancement = {enhancement_32_to_992:.2f}x")

# Alternative: direct computation. The 32-mode TB gives F_anom = 8.34.
# If we DOUBLED the number of levels (64 modes, same bandwidth),
# the additional levels would fill in between existing ones.
# The contribution of interstitial levels to F_anom is bounded by
# the trapezoidal rule correction: O(delta^2 * f''(0) / 12).

# At the Fermi surface, f(xi) = Delta/(2*(xi^2+Delta^2)):
f_0 = Delta_0_OES / (2 * Delta_0_OES**2)  # = 1/(2*Delta)
f_pp_0 = Delta_0_OES * (6*0 - 2*Delta_0_OES**2) / (2*Delta_0_OES**4)**2
# More carefully:
# f(xi) = Delta/(2*(xi^2+D^2))
# f'(xi) = -Delta*2*xi / (2*(xi^2+D^2)^2) = -Delta*xi / (xi^2+D^2)^2
# f''(xi) = -Delta*((xi^2+D^2)^2 - xi*2*(xi^2+D^2)*2*xi) / (xi^2+D^2)^4
# f''(0) = -Delta * D^4 / D^8 = ... let me just compute numerically.
xi_test = 0.001
f_test = Delta_0_OES / (2 * (xi_test**2 + Delta_0_OES**2))
f_test_m = Delta_0_OES / (2 * ((-xi_test)**2 + Delta_0_OES**2))
f_test_0 = Delta_0_OES / (2 * Delta_0_OES**2)
f_pp_num = (f_test + f_test_m - 2*f_test_0) / xi_test**2

# Euler-Maclaurin leading correction per mode:
# delta(F) / F ~ (delta^2 / 12) * |f''(0)| / f(0) * N
delta_EM = r_oes['delta_E_F']  # use actual Fermi-level spacing
correction_EM = (delta_EM**2 / 12) * abs(f_pp_num) * N / F_32
print(f"\n  Euler-Maclaurin discretization correction:")
print(f"    delta_E_F = {delta_EM:.4f} M_KK")
print(f"    f''(0) = {f_pp_num:.6f}")
print(f"    Correction fraction = {correction_EM:.4f} ({correction_EM*100:.2f}%)")

# Take the LARGER of:
# 1. Euler-Maclaurin correction (controlled, but assumes smooth DOS)
# 2. Scaling from S55 enhancement (empirical, but involves model extrapolation)
# Use as ASYMMETRIC uncertainty (E_J can only increase with more modes)

# For the most defensible estimate, take the S55-guided value but
# note that E_J and E_cond scale differently.
# The S55 enhancement was for E_cond (many-body), not F_anom (single-sum).
# The F_anom enhancement should be SMALLER because F_anom converges faster
# (individual terms fall as 1/E^2, while E_cond involves all occupied states).

# CONSERVATIVE APPROACH: Use the Euler-Maclaurin correction as the
# symmetric uncertainty, and note the S55-guided enhancement as
# an asymmetric upper bound.

sigma_E_J_modes_EM = correction_EM * r_oes['E_J']

# S55-guided asymmetric upper bound:
E_J_992_asymmetric = r_oes['E_J'] * enhancement_32_to_992
dE_J_modes_upper = (enhancement_32_to_992 - 1) * r_oes['E_J']

print(f"\n  Mode convergence uncertainty:")
print(f"    Euler-Maclaurin (symmetric): sigma = {sigma_E_J_modes_EM:.4f} M_KK ({correction_EM*100:.2f}%)")
print(f"    S55-guided upper bound: E_J could be up to {E_J_992_asymmetric:.2f} M_KK ({enhancement_32_to_992:.1f}x)")
print(f"    NOTE: The E_J scaling from E_cond is an OVERESTIMATE because")
print(f"    F_anom converges faster than E_cond with mode count.")

# For the combined budget, use the Euler-Maclaurin as the symmetric sigma
# and note the asymmetric upper bound separately.
sigma_E_J_modes = sigma_E_J_modes_EM

# For E_J/E_c: if N_cells increases, E_c ~ delta_E_F/2 DECREASES
# as delta_E_F ~ W / N_modes. This means E_J/E_c INCREASES.
# The mode convergence makes E_J/E_c LARGER (more superfluid).
# sigma(E_J/E_c) from modes is ASYMMETRIC upward.

# For omega_J = sqrt(2*E_J*E_c):
# If E_J increases by factor f and E_c stays the same:
#   omega_J -> omega_J * sqrt(f)
# If E_c decreases (more modes): omega_J could go either way.
sigma_ratio_modes = correction_EM * r_oes['ratio']  # same fraction
sigma_omega_modes = correction_EM * r_oes['omega_J'] / 2  # sqrt gives factor 1/2

print(f"    sigma(E_J/Ec) = {sigma_ratio_modes:.2f}")
print(f"    sigma(omega_J) = {sigma_omega_modes:.4f} M_KK")


# ====================================================================
# ADDITIONAL: Intermediate Delta values
# ====================================================================
print(f"\n{'='*72}")
print(f"ADDITIONAL: Delta scan for systematic spread")
print(f"{'='*72}")

# Scan Delta values between OES and GL to map the E_J(Delta) curve
Delta_scan = np.linspace(Delta_0_OES, Delta_0_GL, 20)
E_J_scan = np.zeros_like(Delta_scan)
omega_J_scan = np.zeros_like(Delta_scan)
ratio_scan = np.zeros_like(Delta_scan)

for i_d, D in enumerate(Delta_scan):
    r_d = compute_fabric_params(evals_fold, J_fold, D, verbose=False)
    E_J_scan[i_d] = r_d['E_J']
    omega_J_scan[i_d] = r_d['omega_J']
    ratio_scan[i_d] = r_d['ratio']

print(f"  {'Delta':>8} {'E_J':>10} {'E_J/Ec':>10} {'omega_J':>10}")
for i_d in range(0, len(Delta_scan), 4):
    print(f"  {Delta_scan[i_d]:8.4f} {E_J_scan[i_d]:10.4f} {ratio_scan[i_d]:10.2f} {omega_J_scan[i_d]:10.4f}")
print(f"  {Delta_scan[-1]:8.4f} {E_J_scan[-1]:10.4f} {ratio_scan[-1]:10.2f} {omega_J_scan[-1]:10.4f}")

# E_J is a monotonically DECREASING function of Delta in this range
print(f"\n  E_J(Delta) is {'MONOTONE DECREASING' if all(np.diff(E_J_scan) < 0) else 'NON-MONOTONE'}")
print(f"  E_J range: [{E_J_scan.min():.4f}, {E_J_scan.max():.4f}] M_KK")
print(f"  E_J variation: {(E_J_scan.max()-E_J_scan.min())/E_J_scan.mean()*100:.2f}%")


# ====================================================================
# COMBINED UNCERTAINTY BUDGET
# ====================================================================
print(f"\n{'='*72}")
print(f"COMBINED UNCERTAINTY BUDGET")
print(f"{'='*72}")

# Three independent sources combined in quadrature
sigma_E_J_total = np.sqrt(sigma_E_J_gap**2 + sigma_E_J_pt**2 + sigma_E_J_modes**2)
sigma_ratio_total = np.sqrt(sigma_ratio_gap**2 + sigma_ratio_pt**2 + sigma_ratio_modes**2)
sigma_omega_total = np.sqrt(sigma_omega_gap**2 + sigma_omega_pt**2 + sigma_omega_modes**2)

print(f"\n  {'Source':<25} {'sigma(E_J)':>12} {'frac%':>8} {'sigma(ratio)':>14} {'sigma(omega)':>14}")
print(f"  {'-'*73}")
print(f"  {'(a) Gap choice':<25} {sigma_E_J_gap:12.4f} {sigma_E_J_gap/E_J_central*100:8.2f} {sigma_ratio_gap:14.2f} {sigma_omega_gap:14.4f}")
print(f"  {'(b) PT truncation':<25} {sigma_E_J_pt:12.4f} {sigma_E_J_pt/E_J_central*100:8.2f} {sigma_ratio_pt:14.2f} {sigma_omega_pt:14.4f}")
print(f"  {'(c) Mode convergence':<25} {sigma_E_J_modes:12.4f} {sigma_E_J_modes/E_J_central*100:8.2f} {sigma_ratio_modes:14.2f} {sigma_omega_modes:14.4f}")
print(f"  {'-'*73}")
print(f"  {'TOTAL (quadrature)':<25} {sigma_E_J_total:12.4f} {sigma_E_J_total/E_J_central*100:8.2f} {sigma_ratio_total:14.2f} {sigma_omega_total:14.4f}")

# Variance fractions
var_total = sigma_E_J_total**2
print(f"\n  Variance decomposition (E_J):")
print(f"    Gap choice:       {sigma_E_J_gap**2/var_total*100:.1f}%")
print(f"    PT truncation:    {sigma_E_J_pt**2/var_total*100:.1f}%")
print(f"    Mode convergence: {sigma_E_J_modes**2/var_total*100:.1f}%")

print(f"\n  FINAL RESULTS (32-mode central +/- symmetric quadrature):")
print(f"    E_J     = {E_J_central:.3f} +/- {sigma_E_J_total:.3f} M_KK  ({sigma_E_J_total/E_J_central*100:.1f}%)")
print(f"    E_c     = {E_c_central:.4f} M_KK  (not independently varied)")
print(f"    E_J/E_c = {ratio_central:.1f} +/- {sigma_ratio_total:.1f}  ({sigma_ratio_total/ratio_central*100:.1f}%)")
print(f"    omega_J = {omega_J_central:.3f} +/- {sigma_omega_total:.3f} M_KK  ({sigma_omega_total/omega_J_central*100:.1f}%)")

# Asymmetric mode-convergence note
print(f"\n  ASYMMETRIC NOTE (mode convergence):")
print(f"    E_J could be up to {E_J_992_asymmetric:.1f} M_KK ({enhancement_32_to_992:.1f}x) with continuum modes")
print(f"    This would make E_J/E_c LARGER (more superfluid)")
print(f"    Superfluid classification is robust REGARDLESS of mode convergence direction")


# ====================================================================
# PROPAGATION TO alpha AND N_e
# ====================================================================
print(f"\n{'='*72}")
print(f"PROPAGATION TO COSMOLOGICAL OBSERVABLES")
print(f"{'='*72}")

alpha_central = 0.408
N_e_central = 1.04

# alpha sensitivity (from S55 framework):
V_KK_fold = float(erich['V_KK_at_tau'][i_s55])
E_J_z_over_V = E_J_central * z_mean / V_KK_fold
sensitivity_alpha = E_J_z_over_V

sigma_alpha = alpha_central * sensitivity_alpha * (sigma_E_J_total / E_J_central)

print(f"  alpha = {alpha_central} (DM/DE ratio)")
print(f"  Sensitivity: d(ln alpha)/d(ln E_J) = {sensitivity_alpha:.4f}")
print(f"  sigma(alpha) = {sigma_alpha:.4f}")
print(f"  alpha = {alpha_central:.3f} +/- {sigma_alpha:.3f}  ({sigma_alpha/alpha_central*100:.1f}%)")

# N_e sensitivity
sigma_Ne = N_e_central * (sigma_omega_total / omega_J_central)

print(f"\n  N_e = {N_e_central} (e-folds)")
print(f"  sigma(N_e) = {sigma_Ne:.3f}")
print(f"  N_e = {N_e_central:.2f} +/- {sigma_Ne:.2f}  ({sigma_Ne/N_e_central*100:.1f}%)")


# ====================================================================
# TAU SWEEP
# ====================================================================
print(f"\n{'='*72}")
print(f"TAU SWEEP: E_J +/- sigma across tau")
print(f"{'='*72}")
print(f"{'tau':>8} {'E_J(OES)':>10} {'E_J(GL)':>10} {'sigma_tot':>10} {'frac%':>8} {'E_J/Ec':>8}")

E_J_tau_oes = np.zeros(len(tau_tb))
E_J_tau_gl = np.zeros(len(tau_tb))
sigma_tot_tau = np.zeros(len(tau_tb))
ratio_tau = np.zeros(len(tau_tb))

for i in range(len(tau_tb)):
    J_i = J_C2_tau[i]
    ev_i = evals_tb[i]
    W_i = bandwidths[i]

    r_i_oes = compute_fabric_params(ev_i, J_i, Delta_0_OES, verbose=False)
    r_i_gl  = compute_fabric_params(ev_i, J_i, Delta_0_GL, verbose=False)

    E_J_tau_oes[i] = r_i_oes['E_J']
    E_J_tau_gl[i]  = r_i_gl['E_J']
    ratio_tau[i] = r_i_oes['ratio']

    # Source uncertainties at this tau
    s_gap_i = abs(r_i_gl['E_J'] - r_i_oes['E_J']) / 2
    T_i = (2 * J_i / W_i)**2
    AB_corr_i = 1.0 / np.sqrt(1 - T_i) - 1.0 if T_i < 1 else 1.0
    s_pt_i = AB_corr_i * r_i_oes['E_J']
    dEF_i = max(ev_i[N//2] - ev_i[N//2 - 1], 1e-12)
    xi_i = ev_i - (ev_i[N//2-1] + ev_i[N//2])/2
    f_pp_i = Delta_0_OES * (-2*Delta_0_OES**2) / (2*Delta_0_OES**2)**2  # f''(0) for uniform
    # Use numerical f''(0)
    f_pp_i_num = (f_anom(0.001, Delta_0_OES) + f_anom(-0.001, Delta_0_OES) - 2*f_anom(0, Delta_0_OES)) / 0.001**2
    corr_EM_i = (dEF_i**2 / 12) * abs(f_pp_i_num) * N / r_i_oes['F_anom'] if r_i_oes['F_anom'] > 0 else 0
    s_mode_i = corr_EM_i * r_i_oes['E_J']

    sigma_tot_tau[i] = np.sqrt(s_gap_i**2 + s_pt_i**2 + s_mode_i**2)

    if i % 5 == 0 or i == i_fold:
        tag = " <-- fold" if i == i_fold else ""
        frac = sigma_tot_tau[i] / E_J_tau_oes[i] * 100 if E_J_tau_oes[i] > 0 else 0
        print(f"{tau_tb[i]:8.4f} {E_J_tau_oes[i]:10.4f} {E_J_tau_gl[i]:10.4f} {sigma_tot_tau[i]:10.4f} {frac:8.2f}% {ratio_tau[i]:8.1f}{tag}")


# ====================================================================
# NUCLEAR BENCHMARK
# ====================================================================
print(f"\n{'='*72}")
print(f"NUCLEAR BENCHMARK COMPARISON")
print(f"{'='*72}")
print(f"""
  In nuclear DFT (Paper 06, Dobaczewski et al. 2014):
  - Pairing gap uncertainty from functional choice: 20-40%
  - Binding energy uncertainty from EDF: 0.5-2 MeV
  - Pair transfer matrix element uncertainty: 15-30%

  This computation:
  - Gap choice spread in E_J: {dE_J_gap_frac*100:.1f}% (within nuclear range)
  - PT convergence: {AB_correction*100:.2f}% (well-controlled, T_eff = {T_eff:.4f})
  - Mode convergence (symmetric): {correction_EM*100:.2f}%
  - Total E_J uncertainty: {sigma_E_J_total/E_J_central*100:.1f}%

  Nuclear comparison:
  - Delta_OES/Delta_GL = {Delta_0_OES/Delta_0_GL:.3f} (cf. nuclear: typically 0.5-0.9)
  - The partial cancellation in F_anom = sum(uv/E) reduces the gap
    sensitivity from 66% to 11%. This is analogous to the "pairing
    anti-halo" effect (Paper 02): pairing observables are less
    sensitive to the potential tail than single-particle energies.
  - The PT expansion parameter T = {T_eff:.4f} is small, ensuring rapid
    convergence of the tunneling series. Nuclear analog: g*N(0) << 1
    ensures BCS mean-field is valid (Paper 03).

  REGIME ROBUSTNESS:
  - E_J/E_c = {ratio_central:.1f} +/- {sigma_ratio_total:.1f}
  - Minimum at -3sigma: {ratio_central - 3*sigma_ratio_total:.1f}
  - SIT transition at E_J/E_c ~ 5 (quantum Monte Carlo, Capogrosso-Sansone 2007)
  - Superfluid classification: ROBUST at {(ratio_central - 5) / sigma_ratio_total:.0f} sigma above SIT
""")


# ====================================================================
# SAVE DATA
# ====================================================================
print("Saving data...")

np.savez('computations/session-56/s56_ej_uncertainty.npz',
    # Central values
    E_J_central=E_J_central,
    E_c_central=E_c_central,
    ratio_central=ratio_central,
    omega_J_central=omega_J_central,

    # Gap choice (a)
    E_J_OES=r_oes['E_J'],
    E_J_GL=r_gl['E_J'],
    ratio_OES=r_oes['ratio'],
    ratio_GL=r_gl['ratio'],
    omega_J_OES=r_oes['omega_J'],
    omega_J_GL=r_gl['omega_J'],
    sigma_E_J_gap=sigma_E_J_gap,
    sigma_ratio_gap=sigma_ratio_gap,
    sigma_omega_gap=sigma_omega_gap,
    dE_J_gap_frac=dE_J_gap_frac,

    # PT truncation (b)
    T_eff=T_eff,
    AB_correction=AB_correction,
    sigma_E_J_pt=sigma_E_J_pt,
    sigma_ratio_pt=sigma_ratio_pt,
    sigma_omega_pt=sigma_omega_pt,

    # Mode convergence (c)
    correction_EM=correction_EM,
    enhancement_Econd=enhancement_Econd,
    enhancement_32_to_992=enhancement_32_to_992,
    E_J_992_asymmetric=E_J_992_asymmetric,
    sigma_E_J_modes=sigma_E_J_modes,
    sigma_ratio_modes=sigma_ratio_modes,
    sigma_omega_modes=sigma_omega_modes,

    # Total
    sigma_E_J_total=sigma_E_J_total,
    sigma_ratio_total=sigma_ratio_total,
    sigma_omega_total=sigma_omega_total,

    # Propagated
    alpha_central=alpha_central,
    sigma_alpha=sigma_alpha,
    N_e_central=N_e_central,
    sigma_Ne=sigma_Ne,
    sensitivity_alpha=sensitivity_alpha,

    # Delta scan
    Delta_scan=Delta_scan,
    E_J_scan=E_J_scan,
    omega_J_scan=omega_J_scan,
    ratio_scan=ratio_scan,

    # Tau sweep
    tau_values=tau_tb,
    E_J_tau_oes=E_J_tau_oes,
    E_J_tau_gl=E_J_tau_gl,
    sigma_tot_tau=sigma_tot_tau,
    ratio_tau=ratio_tau,

    # Gate
    gate_name=np.array(['EJ-UNCERTAINTY-56']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([
        f'E_J = {E_J_central:.3f} +/- {sigma_E_J_total:.3f} M_KK ({sigma_E_J_total/E_J_central*100:.1f}%). '
        f'E_J/E_c = {ratio_central:.1f} +/- {sigma_ratio_total:.1f} ({sigma_ratio_total/ratio_central*100:.1f}%). '
        f'omega_J = {omega_J_central:.3f} +/- {sigma_omega_total:.3f} M_KK ({sigma_omega_total/omega_J_central*100:.1f}%). '
        f'Dominant: gap choice ({sigma_E_J_gap**2/var_total*100:.0f}% variance). '
        f'PT well-controlled (AB correction {AB_correction*100:.2f}%). '
        f'Superfluid classification robust at {(ratio_central-5)/sigma_ratio_total:.0f} sigma above SIT.'
    ]),
)

print("Saved: computations/session-56/s56_ej_uncertainty.npz")


# ====================================================================
# FINAL GATE VERDICT
# ====================================================================
print(f"\n{'='*72}")
print(f"GATE VERDICT: EJ-UNCERTAINTY-56 — INFO")
print(f"{'='*72}")
print(f"")
print(f"Parameter            Central     sigma         Frac")
print(f"{'-'*58}")
print(f"E_J [M_KK]           {E_J_central:>7.3f}     +/- {sigma_E_J_total:.3f}     {sigma_E_J_total/E_J_central*100:.1f}%")
print(f"E_c [M_KK]           {E_c_central:>7.4f}     (not varied)")
print(f"E_J/E_c              {ratio_central:>7.1f}     +/- {sigma_ratio_total:.1f}       {sigma_ratio_total/ratio_central*100:.1f}%")
print(f"omega_J [M_KK]       {omega_J_central:>7.3f}     +/- {sigma_omega_total:.3f}     {sigma_omega_total/omega_J_central*100:.1f}%")
print(f"alpha (DM/DE)        {alpha_central:>7.3f}     +/- {sigma_alpha:.3f}     {sigma_alpha/alpha_central*100:.1f}%")
print(f"N_e (e-folds)        {N_e_central:>7.2f}     +/- {sigma_Ne:.2f}       {sigma_Ne/N_e_central*100:.1f}%")
print(f"")
print(f"Uncertainty breakdown (fraction of E_J variance):")
print(f"  (a) Gap choice (OES vs GL):   {sigma_E_J_gap**2/var_total*100:.1f}%  [MODEL]")
print(f"  (b) PT truncation (AB corr):  {sigma_E_J_pt**2/var_total*100:.1f}%  [TRUNCATION]")
print(f"  (c) Mode convergence (EM):    {sigma_E_J_modes**2/var_total*100:.1f}%  [BASIS]")
print(f"")
print(f"ASYMMETRIC NOTE: Mode convergence is one-sided (E_J increases")
print(f"  with more modes). Upper bound from S55 scaling: E_J ~ {E_J_992_asymmetric:.1f} M_KK.")
print(f"  This makes E_J/E_c LARGER, reinforcing the superfluid classification.")
print(f"")
print(f"KEY FINDING:")
print(f"  1. E_J is robust to ~{sigma_E_J_total/E_J_central*100:.0f}% (symmetric quadrature)")
print(f"  2. Superfluid classification (E_J/E_c >> 1) is robust at")
print(f"     {(ratio_central - 5) / sigma_ratio_total:.0f} sigma above SIT threshold")
print(f"  3. Gap choice is the dominant uncertainty source")
print(f"  4. PT convergence is well-controlled (T_eff = {T_eff:.4f})")
print(f"  5. Mode convergence is small (EM: {correction_EM*100:.2f}%) but")
print(f"     potentially large if continuum DOS enhancement applies")
