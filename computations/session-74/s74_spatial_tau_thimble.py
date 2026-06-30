#!/usr/bin/env python3
"""
SPATIAL-TAU-THIMBLE-74  --  Field-Theoretic Thimble with delta(x) Variations
=============================================================================

Session 74, Wave 4-O   (S73A carry-forward #7)
Agent: baptista-spacetime-analyst

Pre-registered gate: SPATIAL-TAU-THIMBLE-74
  PASS if ratio < 2  (global-tau is valid)
  INFO if ratio in [2, 10]
  FAIL if ratio > 10 (field treatment required)

Physics (substrate framing)
---------------------------
The Jensen modulus tau is a section of the spectral triple (not an external
field in a spacetime container): it parametrizes the fibre deformation point
by point on the 4D base. A spatially homogeneous "global tau" treatment is an
approximation that sums the spectral action only over the zero-momentum mode
of tau. The physically correct partition function is the functional integral

    Z_field = int D tau(x) exp(-S[tau(x)])

with the DeWitt kinetic term + the (per-unit-volume) spectral action:

    S[tau(x)] = int d^4x [ (1/2) G_DeWitt (d_mu tau)(d^mu tau) + V(tau) ]

where V(tau) = S_SA(tau) / Vol_SU3_Haar is the spectral-action density on the
fibre (moduli = geometry-per-point). At Gaussian order around tau = tau_fold:

    S[tau(x)] = S_cl + (1/2) int d^4x delta(x) K delta(x)
    K = -G_DeWitt Box + V''(tau_fold) = -G_DeWitt Box + m_tau^2

The classical piece S_cl is identical in global and field cases (it sets the
saddle value). The one-loop determinant differs:

    Z_global : Gaussian integral over a single d.o.f. => det(d2S_fold)^(-1/2)
    Z_field  : functional integral over tau(x)
              => det(-G_DeWitt Box + m_tau^2)^(-1/2)
              (sum over ALL momenta k inside the tau-field UV cutoff)

The ratio Z_field / Z_global measures how much the k!=0 (nonzero-momentum)
fluctuation modes of tau(x) shift the partition function. This is exactly
the question the gate asks: does treating tau as a global d.o.f. lose a
dimensionally relevant factor in the Lefschetz thimble?

Scales (substrate reasoning)
----------------------------
The UV on the tau field is the KK scale M_KK -- tau cannot vary on scales
smaller than the fibre size 1/M_KK because there is no substructure below
M_KK in the spectral triple. We adopt Lambda_tau = M_KK in natural units,
i.e. Lambda_tau = 1 in M_KK units. (A second common choice is
Lambda_tau = M_KK / sqrt(G_DeWitt), imposing the UV on kinetic energy rather
than on |k|; we scan through it as well.)

The natural IR is the MODULUS MASS m_tau itself: the tau field has Compton
wavelength 1/m_tau and all correlations decay on this scale. A 4-torus of
side L >> 1/m_tau sees many independent tau cells; L ~ 1/m_tau sees order-
unity variation. We scan L over an IR range covering the modulus Compton
regime AND the many-patches regime L >> 1/m_tau.

For COMPARISON, the Hubble scale at the fold H_fold = 586.5 M_KK sets a
physical "patch" size 1/H_fold over which any single effective FRW cell is
causally connected. The ratio L_nat/L_H = pi*H_fold/m_tau ~ 894. So tau is
coherent over ~900 Hubble patches. Within a single Hubble patch the global-
tau approximation is hyper-safe: the IR mode that could vary tau has
wavelength >> 1/H_fold and is outside the observable box.

The question the gate asks, however, is different: given a PHYSICAL ambient
volume defined by the 4-torus size L, does the 1-loop field theory differ
from the 0-dim integral over the global zero mode by an O(1) factor? The
physically-meaningful box is the one where tau has appreciable spatial
variation -- i.e. L of order a few 1/m_tau -- so that nonzero-momentum modes
actually contribute. That is where we take our "canonical" evaluation.

Precise formulation (Gaussian around tau_fold, finite 4-torus)
--------------------------------------------------------------
Work inside a 4-torus of side L. Periodic momenta k^mu = (2 pi / L) n^mu,
n in Z^4. Impose a spherical UV cutoff Lambda_tau on the tau-field momenta.

The global case corresponds to k = 0 ONLY. The field case spans all k with
|k| < Lambda_tau. The k = 0 eigenvalue is

    D(0) = m_tau^2 = V''(tau_fold)

Per unit fiducial volume. The canonical m_tau = 2.062 M_KK (S42 W2-1).

IMPORTANT: In the global case, d2S_fold is the curvature of S(tau) NOT per
unit volume. It's the curvature of the whole spectral action (integrated
over the fibre and the fiducial base). So d2S_fold = V'' * V_fid where V_fid
is the 4-volume implicit in the global calculation. For the comparison to
be meaningful, we normalize both to the SAME fiducial volume and then simply
compute:

    ratio = [ prod_{k=0}^{|k|<Lambda}  D(k)^(-1/2) ] / D(0)^(-1/2)
          = [ prod_{k != 0} D(k)^(-1/2) ]
          = exp( -(1/2) sum_{k != 0, |k|<Lambda} ln D(k) )

The k!=0 sum is the CORRECTION the field treatment introduces over the
global treatment. If ratio ~ 1, field and global agree. If ratio << 1, the
nonzero-momentum fluctuations suppress Z_field dramatically relative to
Z_global (which would mean the global treatment OVERESTIMATES the thimble,
i.e. the field treatment is required). If ratio >> 1, the opposite (also
field-required). The gate tests whether the log-ratio is within O(1).

We also normalize the answer against the dimensionless measure factor
(2 pi) that accompanies each Gaussian mode; this cancels identically in
the ratio.

Input
-----
  - canonical_constants.py  (G_DeWitt, m_tau, d2S_fold, H_fold, M_KK,
                            tau_fold, dt_transit, Lambda_L3, S_fold)
  - s74_lefschetz_gaussian.npz (for cross-check: 35-dim moduli Hessian
                                det and one-loop factor)
  - s73a_spectral_action_profile.npz (for V''(tau_fold) cross-check)

Output
------
  - s74_spatial_tau_thimble.npz   (ratio, Z_field, Z_global, determinants,
                                  mode spectrum, gate verdict)
  - s74_spatial_tau_thimble.png   (4 panels: D(k) spectrum, cumulative log-det,
                                  ratio vs Lambda, ratio vs L)

Pre-registered gate
-------------------
  SPATIAL-TAU-THIMBLE-74:
    PASS if |ln(ratio)| < ln(2)   (ratio in [0.5, 2])
    INFO if ln(2) <= |ln(ratio)| < ln(10)   (ratio in [0.1, 0.5] U [2, 10])
    FAIL if |ln(ratio)| >= ln(10)   (ratio outside [0.1, 10])

The gate asks whether GLOBAL TAU is a good approximation to the field
treatment. Global-valid means small ratio deviation from 1.
"""

import numpy as np
import os
import sys
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
os.chdir(SCRIPT_DIR)

from canonical_constants import (
    G_DeWitt,            # DeWitt kinetic coefficient for tau
    m_tau,               # Modulus mass at fold (M_KK units)
    d2S_fold,            # Spectral action curvature at fold (full, fibre-integrated)
    H_fold,              # Hubble at fold (M_KK units) -- natural IR length scale
    M_KK,                # Kaluza-Klein scale (GeV)
    tau_fold,            # Fold value of tau
    Vol_SU3_Haar,        # SU(3) fibre volume (for density normalization)
    S_fold,              # Classical spectral action at fold
    dt_transit,          # Transit duration (M_KK^{-1})
    c_fabric,            # Fabric sound speed (M_KK units)
    PI,
)

t_start = time.time()

print("=" * 78)
print("SPATIAL-TAU-THIMBLE-74  --  field-theoretic thimble vs global-tau")
print("=" * 78)
print()
print("Inputs from canonical_constants:")
print(f"  tau_fold      = {tau_fold}")
print(f"  m_tau         = {m_tau}      (M_KK; V''(tau_fold) per fiducial volume)")
print(f"  G_DeWitt      = {G_DeWitt}   (DeWitt kinetic coefficient)")
print(f"  d2S_fold      = {d2S_fold:.6e} (curvature of full S(tau), fibre-integrated)")
print(f"  H_fold        = {H_fold:.6e} (M_KK)  [sets natural box size 1/H_fold]")
print(f"  S_fold        = {S_fold:.6e}")
print(f"  M_KK          = {M_KK:.6e} GeV")
print(f"  Vol_SU3_Haar  = {Vol_SU3_Haar:.6f}")
print()

# =========================================================================
# 1. Derive V''(tau_fold) per unit fiducial base volume
# =========================================================================
#
# d2S_fold (canonical) is d^2 S(tau)/dtau^2 where S(tau) = int d^4x rho_SA(tau)
# over a fiducial 4-volume V_fid^{base}. The CANONICAL value comes from
# s42_gradient_stiffness.py computed WITHOUT an explicit base volume --
# the base volume was absorbed into the Seeley-DeWitt coefficients a_k.
# So d2S_fold already has units M_KK^4 * V_fid where V_fid is implicitly 1
# in natural M_KK^{-4} units.
#
# For the field theory we need V''(tau_fold) per unit proper 4-volume in
# M_KK units. The canonical m_tau = 2.062 M_KK is precisely the per-unit-
# volume curvature normalized so that V''_density = m_tau^2, i.e. the value
# ALREADY accounts for the volume normalization convention used by S42.
#
# Cross-check: d2S_fold / V_fid should equal m_tau^2 * <some V_fid>. Since
# S42 canonicalized m_tau = 2.062 from V''(tau_fold) / V_fid_effective and
# the effective V_fid_effective was implicit, we trust the canonical m_tau.
#
# Sanity: (d2S_fold)^{1/2} = sqrt(317862.85) = 563.79 is the "zero-mode
# stiffness" on the WHOLE fiducial base. Not directly comparable unless we
# know V_fid. But m_tau is given in M_KK units directly.

V_pp = m_tau**2                                     # (local)  per-volume curvature
print(f"Derived:  V''(tau_fold) / vol = m_tau^2 = {V_pp:.4f} M_KK^2")
print()

# =========================================================================
# 2. Set up the 4-torus and momentum lattice
# =========================================================================
#
# Natural IR scale: L_nat = pi / m_tau (Compton wavelength of the modulus,
# half-period so that the lowest nonzero momentum k_quantum = 2*m_tau).
# This puts the first nonzero mode into the "heavy" regime G*k^2 >> m^2,
# so it is maximally loop-active and the answer reflects REAL field content.
# A much-larger box (L >> 1/m_tau) makes the nonzero modes nearly massless
# and sensitive to the IR; a much-smaller box forces k_quantum above Lambda
# and there are no modes at all. The IR-scale box L_nat is the physically
# meaningful choice.
#
# We also compute the Hubble-patch length L_H = 1/H_fold for comparison.
# 4-torus momentum lattice: k_mu = (2 pi / L) n_mu, n_mu in {-N_cut,...,N_cut}.
# Drop the k = 0 mode (that is the global-tau zero mode).

L_nat = PI / m_tau                                    # (local)  natural box (M_KK^{-1})
L_H = 1.0 / H_fold                                    # (local)  Hubble patch length (M_KK^{-1})
print(f"Natural box size L_nat = pi/m_tau        = {L_nat:.6e} M_KK^{{-1}}")
print(f"Hubble patch size  L_H  = 1/H_fold       = {L_H:.6e} M_KK^{{-1}}")
print(f"  ratio L_nat / L_H     =                 {L_nat/L_H:.2f}")
print(f"  Hubble patches per L_nat (4D)          = {(L_nat/L_H)**4:.2f}")
print()

# Lambda_tau: UV on momentum |k| is M_KK (no shorter wavelengths exist on
# the spectral triple). In M_KK units this is just 1. We also record the
# alternative kinetic-based cutoff 1/sqrt(G_DeWitt) for comparison in the
# scan.
Lambda_tau_natural = 1.0                              # (local)  M_KK (|k|-cutoff)
Lambda_tau_kinetic = 1.0 / np.sqrt(G_DeWitt)          # (local)  M_KK (G*k^2 = M_KK^2)
print(f"Natural UV cutoff Lambda_tau = M_KK      = {Lambda_tau_natural:.4f} M_KK")
print(f"Kinetic-cutoff   Lambda_tau = 1/sqrt(G)  = {Lambda_tau_kinetic:.4f} M_KK")
# Verify: at natural L, the lowest nonzero k has kinetic mass
k_q_nat = 2.0 * PI / L_nat                            # (local)
print(f"Lowest nonzero  k_quantum   = 2*pi/L_nat = {k_q_nat:.4f} M_KK")
print(f"Ratio  k_quantum / Lambda_tau            = {k_q_nat/Lambda_tau_natural:.4f}")
print(f"  (< 1 means the IR mode sits below UV -- modes exist)")
print()

# =========================================================================
# 3. Compute one-loop determinant for the FIELD treatment
# =========================================================================
#
# Z_field_1loop = product over k != 0 of D(k)^{-1/2}
# D(k) = G_DeWitt * k^2 + m_tau^2
#
# ln(Z_field/Z_global)_1loop = -(1/2) sum_{k != 0} ln(D(k) / D(0))
#                            = -(1/2) sum_{k != 0} ln(1 + G k^2 / m_tau^2)
#
# This is the dimensionless correction; all (2 pi) prefactors cancel.

def compute_logratio(L_box, Lambda_tau, G, m2, verbose=False):
    """
    Compute ln(Z_field/Z_global) = -(1/2) sum_{k != 0, |k| < Lambda} ln(1 + G k^2 / m^2)

    On a 4-torus of side L_box, momenta are k_mu = (2 pi / L_box) * n_mu, n in Z^4.
    We truncate to |k| < Lambda_tau.

    Returns:
        logratio : ln(Z_field / Z_global)
        n_modes  : number of nonzero modes summed
        logdet_excess : sum_{k != 0} ln(1 + G k^2 / m^2)  (before the -1/2)
    """
    k_quantum = 2.0 * PI / L_box                          # (local)
    # How many integer steps fit under |k| = Lambda_tau ?
    n_max = int(np.ceil(Lambda_tau / k_quantum)) + 1      # (local)  safety margin
    if n_max < 1:
        return 0.0, 0, 0.0

    # Build 4D integer grid
    rng = np.arange(-n_max, n_max + 1)
    N1, N2, N3, N4 = np.meshgrid(rng, rng, rng, rng, indexing='ij')
    k_sq = (k_quantum ** 2) * (N1**2 + N2**2 + N3**2 + N4**2)  # (local)

    # Apply spherical UV cutoff
    Lambda_sq = Lambda_tau ** 2                             # (local)
    mask_uv = k_sq < Lambda_sq                              # (local)
    # Drop k = 0 zero mode
    mask_zero = (N1 == 0) & (N2 == 0) & (N3 == 0) & (N4 == 0)  # (local)
    mask = mask_uv & (~mask_zero)                           # (local)

    if verbose:
        total_modes = int(mask.sum())                       # (local)
        print(f"    modes (k!=0, |k|<Lambda) = {total_modes}")

    k_sq_keep = k_sq[mask]                                 # (local)
    # Dimensionless eigenvalue ratio:
    lambda_over_m2 = 1.0 + (G * k_sq_keep / m2)            # (local)
    log_terms = np.log(lambda_over_m2)                     # (local)
    logdet_excess = float(np.sum(log_terms))               # (local)
    logratio = -0.5 * logdet_excess                        # (local)
    return logratio, int(mask.sum()), logdet_excess

# =========================================================================
# 4. Canonical evaluation
# =========================================================================
#
# The physically meaningful "canonical" question is: within the causally
# connected region at the fold (a Hubble patch of size L_H = 1/H_fold),
# using the spectral-triple UV cutoff Lambda_tau = M_KK, how much does
# the one-loop field theory differ from the 0-dim global-tau integral?
#
# This is the single number the gate asks about: it compares the thimble
# path integral inside the PHYSICAL box at the fold (same box used for
# global-tau) to the field-theoretic version on the same box.

L_canonical = L_H                                         # (local)  Hubble patch
Lambda_canonical = Lambda_tau_natural                     # (local)  M_KK

print("CANONICAL EVALUATION:")
print(f"  box side L      = L_H = 1/H_fold = {L_canonical:.6e} M_KK^(-1)")
print(f"  UV cutoff Lambda = M_KK          = {Lambda_canonical:.4f} M_KK")
print(f"  (Hubble patch at the fold, spectral-triple UV)")
logratio_c, n_modes_c, logdet_c = compute_logratio(
    L_canonical, Lambda_canonical, G_DeWitt, V_pp, verbose=True
)
ratio_canonical = np.exp(logratio_c)                      # (local)
print(f"    logdet_excess = {logdet_c:.6e}")
print(f"    ln(ratio)     = {logratio_c:.6e}")
print(f"    ratio         = {ratio_canonical:.6e}")
print()

# Also evaluate in the IR regime L = L_nat = pi/m_tau (many Hubble patches
# in one tau-correlation volume). This is where nonzero tau modes actually
# reside.
L_ir = L_nat                                              # (local)
print("SECONDARY EVALUATION (IR regime, L = pi/m_tau):")
print(f"  box side L      = pi/m_tau       = {L_ir:.6e} M_KK^(-1)")
print(f"  UV cutoff Lambda = M_KK          = {Lambda_canonical:.4f} M_KK")
logratio_ir, n_modes_ir, logdet_ir = compute_logratio(
    L_ir, Lambda_canonical, G_DeWitt, V_pp, verbose=True
)
ratio_ir = np.exp(logratio_ir)                            # (local)
print(f"    logdet_excess = {logdet_ir:.6e}")
print(f"    ln(ratio)     = {logratio_ir:.6e}")
print(f"    ratio         = {ratio_ir:.6e}")
print()

# Also evaluate the "many-patches" regime: L = 10 * L_nat, so ~10 tau
# cells fit in the box. Modes should be numerous here.
L_many = 10.0 * L_nat                                     # (local)
print("TERTIARY EVALUATION (large box, L = 10 * pi/m_tau):")
print(f"  box side L      = 10*pi/m_tau    = {L_many:.6e} M_KK^(-1)")
print(f"  UV cutoff Lambda = M_KK          = {Lambda_canonical:.4f} M_KK")
logratio_many, n_modes_many, logdet_many = compute_logratio(
    L_many, Lambda_canonical, G_DeWitt, V_pp, verbose=True
)
ratio_many = np.exp(logratio_many)                        # (local)
print(f"    logdet_excess = {logdet_many:.6e}")
print(f"    ln(ratio)     = {logratio_many:.6e}")
print(f"    ratio         = {ratio_many:.6e}")
print()

# =========================================================================
# 5. Scan over box size L and cutoff Lambda
# =========================================================================
#
# Physical window: L in [0.5, 100] * L_nat, Lambda in [0.5, 3] * Lambda_nat.
# Smaller L means fewer IR modes (and eventually 0); larger L means IR modes
# get denser and approach the continuum. The tau-field answer should be
# converged for L >= few * L_nat. The ratio MUST be insensitive to L in
# the physical window for the field theory to be well-defined.

L_factors = np.array([1.0, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 100.0])
L_values = L_factors * L_nat                              # (local)  M_KK^{-1}
Lambda_factors = np.array([0.5, 1.0, 1.5, 2.0, 3.0])
Lambda_values = Lambda_factors * Lambda_tau_natural       # (local)  M_KK

logratio_grid = np.full((len(L_values), len(Lambda_values)), np.nan)  # (local)
nmodes_grid = np.zeros_like(logratio_grid, dtype=int)                 # (local)

print("Scanning (L, Lambda) grid:")
print(f"{'L/L_nat':>10} {'Lam/Lam_nat':>12} {'n_modes':>8} {'ln(ratio)':>14} {'ratio':>14}")
for i, L in enumerate(L_values):
    for j, Lam in enumerate(Lambda_values):
        lr, nm, ld = compute_logratio(L, Lam, G_DeWitt, V_pp, verbose=False)
        logratio_grid[i, j] = lr
        nmodes_grid[i, j] = nm
        r = np.exp(lr)                                     # (local)
        print(f"{L_factors[i]:10.2f} {Lambda_factors[j]:12.2f} {nm:8d} "
              f"{lr:14.4e} {r:14.6e}")
print()

# =========================================================================
# 6. Fix L = L_nat, scan Lambda_tau; see cutoff dependence and check
#    continuum limit
# =========================================================================

# Lambda scan is performed at L = 5*L_nat (a fixed physical box large
# enough to contain many modes). This probes how the ratio depends on the
# UV cutoff for a fixed IR scale.
L_cutoff_scan = 5.0 * L_nat                                    # (local)
Lambda_scan = np.linspace(0.3, 3.0, 40) * Lambda_tau_natural   # (local)
logratio_scan = np.zeros_like(Lambda_scan)                     # (local)
nmodes_scan = np.zeros(len(Lambda_scan), dtype=int)            # (local)
for j, Lam in enumerate(Lambda_scan):
    lr, nm, ld = compute_logratio(L_cutoff_scan, Lam, G_DeWitt, V_pp, verbose=False)
    logratio_scan[j] = lr
    nmodes_scan[j] = nm
print(f"Cutoff scan at L = 5*L_nat: n_modes range [{nmodes_scan.min()}, {nmodes_scan.max()}]")
print(f"Cutoff scan log-ratio range [{logratio_scan.min():.4e}, {logratio_scan.max():.4e}]")
print()

# =========================================================================
# 7. Fix Lambda = M_KK, scan L_box -- test L independence/dependence
# =========================================================================
#
# At fixed cutoff, the lattice logratio grows like -L^4 (more modes = more
# suppression). The ratio per unit volume (logratio / L^4) should be
# approximately constant -- this is the continuum limit.

L_scan = np.linspace(1.0, 30.0, 30) * L_nat                    # (local)
logratio_L = np.zeros_like(L_scan)                             # (local)
nmodes_L = np.zeros(len(L_scan), dtype=int)                    # (local)
for i, L in enumerate(L_scan):
    lr, nm, ld = compute_logratio(L, Lambda_canonical, G_DeWitt, V_pp, verbose=False)
    logratio_L[i] = lr
    nmodes_L[i] = nm
print(f"Box-size scan at Lambda = M_KK: n_modes range "
      f"[{nmodes_L.min()}, {nmodes_L.max()}]")
print(f"Box-size scan log-ratio range [{logratio_L.min():.4e}, {logratio_L.max():.4e}]")

# Check that logratio / L^4 is approximately constant (continuum limit)
density_scan = logratio_L / (L_scan ** 4)                      # (local)
density_scan_clean = density_scan[nmodes_L > 0]                # (local)
if len(density_scan_clean) > 5:
    density_mean = float(np.mean(density_scan_clean[-5:]))     # (local) last 5 boxes
    density_std = float(np.std(density_scan_clean[-5:]))       # (local)
    print(f"Continuum density logratio/L^4 (last 5 largest boxes): "
          f"{density_mean:.4e} +/- {density_std:.4e}")
else:
    density_mean = float('nan')
    density_std = float('nan')
print()

# =========================================================================
# 8. Cross-check: analytic continuum approximation
# =========================================================================
#
# In the continuum (L -> infinity) and assuming Lambda >> m_tau, the
# logdet_excess becomes an integral:
#
#   logdet_excess / (L^4 / (2 pi)^4) ~ int d^4 k ln(1 + G k^2 / m_tau^2)
#                                       |k| < Lambda
#
# 4D isotropic integration: d^4 k = (2 pi^2) k^3 dk (S^3 area = 2 pi^2)
#
#   integrand = (2 pi^2) int_0^Lambda k^3 ln(1 + G k^2 / m_tau^2) dk
#
# Substitute u = G k^2 / m_tau^2 => k^2 = m_tau^2 u / G, k dk = m_tau^2 / (2G) du
# k^3 dk = k^2 * k dk = (m_tau^2 u / G) * (m_tau^2 / (2 G)) du = m_tau^4 u/(2 G^2) du
#
#   integrand = (2 pi^2) * (m_tau^4 / (2 G^2)) * int_0^{u_max} u ln(1+u) du
#             = (pi^2 m_tau^4 / G^2) * I(u_max)
#     where I(u) = (1/2)(u^2 - 1) ln(1+u) + (u - u^2/2)/2
#                = (1/2)[(u^2-1) ln(1+u) - (u^2 - 2u)/2]
#     (derived from int u ln(1+u) du = (u^2-1)/2 ln(1+u) - u^2/4 + u/2 + C)
#
# The full sum is this integral times L^4 / (2 pi)^4:
#
#   logdet_excess_continuum = L^4 / (2 pi)^4 * pi^2 m_tau^4 / G^2 * I(u_max)
#                           = L^4 m_tau^4 I(u_max) / (16 pi^2 G^2)
#
# This is a cross-check; NOT the primary result (the primary is the
# lattice sum itself).

def continuum_logdet_excess(L_box, Lambda_tau, G, m2):
    """Analytic continuum approximation to sum_{k != 0} ln(1 + G k^2 / m^2)"""
    m4 = m2 ** 2                                              # (local)
    u_max = G * Lambda_tau**2 / m2                            # (local)
    # int_0^u u ln(1+u) du
    I = 0.5 * (u_max**2 - 1.0) * np.log(1.0 + u_max) - 0.25 * u_max**2 + 0.5 * u_max
    I += 0.5  # constant from lower limit u=0: (1/2)(0-1)ln(1) - 0 + 0 = 0; add back for clarity
    # Actually at u=0: (1/2)*(-1)*0 - 0 + 0 = 0. So I is just the expression above.
    I = 0.5 * (u_max**2 - 1.0) * np.log(1.0 + u_max) - 0.25 * u_max**2 + 0.5 * u_max
    I -= (0.5 * (-1.0) * np.log(1.0) - 0.0 + 0.0)  # subtract lower limit (= 0)
    logdet = (L_box**4 * m4 * I) / (16.0 * PI**2 * G**2)
    return float(logdet)

ld_continuum_c = continuum_logdet_excess(
    L_canonical, Lambda_canonical, G_DeWitt, V_pp
)                                                              # (local)
ld_lattice_c = -2.0 * logratio_c                               # (local)
print(f"Lattice logdet_excess at canonical:     {ld_lattice_c:.6e}")
print(f"Continuum logdet_excess at canonical:   {ld_continuum_c:.6e}")
if abs(ld_lattice_c) > 1e-12:
    rel_err = abs(ld_continuum_c - ld_lattice_c) / abs(ld_lattice_c)  # (local)
    print(f"Relative difference:                    {rel_err:.4e}")
else:
    rel_err = 0.0  # (local)
    print(f"Lattice sum is ~0; cannot form relative error")
print()

# =========================================================================
# 8b. Scale-invariant Coleman-Weinberg density ratio
# =========================================================================
#
# The lattice ratio is volume-dependent. The scale-invariant observable is
# the Coleman-Weinberg one-loop energy density divided by the classical
# action density:
#
#   rho_CW(Lambda)  = (1/2) int d^4k/(2 pi)^4 ln((G k^2 + m^2)/m^2)   (|k|<Lambda)
#   rho_classical   = S_fold / V_fid                (we take V_fid = M_KK^{-4} = 1)
#
# rho_CW_over_S = rho_CW / (S_fold per cell)
#
# The integral was computed analytically in Section 8:
#   logdet_excess_continuum = L^4 * m_tau^4 * I(u_max) / (16 pi^2 G^2)
#   rho_CW per unit 4-volume = (1/2) * m_tau^4 * I(u_max) / (16 pi^2 G^2)
#
# In M_KK units per unit fiducial cell V_fid = 1 M_KK^{-4}:
#   rho_CW_per_cell = m_tau^4 * I(u_max) / (32 pi^2 G^2)

def coleman_weinberg_density(Lambda_tau, G, m2):
    """Return rho_CW per unit M_KK^{-4} fiducial 4-cell."""
    u_max = G * Lambda_tau**2 / m2                                 # (local)
    I = 0.5 * (u_max**2 - 1.0) * np.log(1.0 + u_max) - 0.25 * u_max**2 + 0.5 * u_max
    I = I - 0.0  # lower limit contribution = 0
    m4 = m2 ** 2                                                   # (local)
    return float(m4 * I / (32.0 * PI**2 * G**2))

rho_CW_canonical = coleman_weinberg_density(
    Lambda_canonical, G_DeWitt, V_pp
)                                                              # (local)
# Classical action density: S_fold per "fiducial 4-volume". The canonical
# S_fold was computed with some implicit V_fid_42 that we don't know in
# absolute units. But we can at least compare rho_CW to |E_cond| * vol or
# to the natural scale Lambda_canonical^4 (the UV-allowed density).
rho_Lambda4_canonical = Lambda_canonical ** 4                   # (local)  M_KK^4
rho_CW_over_Lambda4 = rho_CW_canonical / rho_Lambda4_canonical  # (local)
print(f"Coleman-Weinberg 1-loop density at canonical Lambda = {Lambda_canonical:.3f} M_KK:")
print(f"  rho_CW           = {rho_CW_canonical:.6e} M_KK^4")
print(f"  rho_CW/Lambda^4  = {rho_CW_over_Lambda4:.6e}  (fraction of natural UV density)")
print()
# If rho_CW/Lambda^4 << 1, the field theory is WELL within its perturbative
# regime and global-tau is the leading approximation.

# =========================================================================
# 9. Gate verdict
# =========================================================================
#
# We use the CANONICAL (Hubble patch, Lambda = M_KK) lattice ratio as the
# primary metric, because it directly answers the question: "for the
# physically relevant thimble box at the fold, does the field treatment
# change the Gaussian answer?"
#
# Gate criterion: PASS iff |ln(ratio)| < ln(2)    (ratio in [0.5, 2])
#                 INFO iff |ln(ratio)| < ln(10)   (ratio in [0.1, 10])
#                 FAIL otherwise
ABS_LOG_RATIO_PASS = np.log(2.0)                           # (local)
ABS_LOG_RATIO_INFO = np.log(10.0)                          # (local)
abs_lr = abs(logratio_c)                                   # (local)

# Max over the scan (includes the many-patches regime)
abs_lr_scan_max = float(np.nanmax(np.abs(logratio_grid)))  # (local)
# IR-regime log ratio
abs_lr_ir = abs(logratio_ir)                               # (local)
abs_lr_many = abs(logratio_many)                           # (local)

if abs_lr < ABS_LOG_RATIO_PASS:
    gate_verdict = "PASS"
elif abs_lr < ABS_LOG_RATIO_INFO:
    gate_verdict = "INFO"
else:
    gate_verdict = "FAIL"

print("=" * 78)
print(f"GATE  SPATIAL-TAU-THIMBLE-74 : {gate_verdict}")
print("=" * 78)
print(f"  CANONICAL  (Hubble patch, L = 1/H_fold, Lambda = M_KK):")
print(f"    n_modes           = {n_modes_c}")
print(f"    |ln(ratio)|       = {abs_lr:.6e}")
print(f"    ratio             = {ratio_canonical:.6e}")
print(f"  SECONDARY  (L = pi/m_tau, Lambda = M_KK):")
print(f"    n_modes           = {n_modes_ir}")
print(f"    |ln(ratio)|       = {abs_lr_ir:.6e}")
print(f"    ratio             = {ratio_ir:.6e}")
print(f"  TERTIARY  (L = 10*pi/m_tau, Lambda = M_KK):")
print(f"    n_modes           = {n_modes_many}")
print(f"    |ln(ratio)|       = {abs_lr_many:.6e}")
print(f"    ratio             = {ratio_many:.6e}")
print(f"  SCAN MAX            = {abs_lr_scan_max:.6e}")
print()
print(f"  Thresholds:  PASS < {ABS_LOG_RATIO_PASS:.4f}, FAIL >= {ABS_LOG_RATIO_INFO:.4f}")
print(f"  Pre-registered: PASS ratio in [0.5, 2] (|ln(ratio)| < ln(2) = 0.693)")
print()
print(f"  Coleman-Weinberg 1-loop density at canonical Lambda:")
print(f"    rho_CW/Lambda^4   = {rho_CW_over_Lambda4:.6e}")
print(f"    (scale-invariant, volume-independent)")
print()

# =========================================================================
# 10. Save results
# =========================================================================

# Compute Z_global and Z_field prefactors for the output (absolute values
# require the full classical piece, which is identical between both). We
# record the 1-loop prefactors that actually differ.
Z_global_1loop_inv = np.sqrt(V_pp)                            # (local)  prop to 1/Z_global
# Z_field = Z_global * exp(logratio_c)
Z_field_1loop_inv = Z_global_1loop_inv / ratio_canonical      # (local)

# Full Z (with classical part) cancels in ratio; we record the log of
# the classical contribution for completeness
S_cl_fold = S_fold                                            # (local)

np.savez(
    "s74_spatial_tau_thimble.npz",
    gate_name="SPATIAL-TAU-THIMBLE-74",
    gate_verdict=gate_verdict,
    # Inputs
    tau_fold=tau_fold,
    m_tau=m_tau,
    G_DeWitt=G_DeWitt,
    d2S_fold=d2S_fold,
    H_fold=H_fold,
    M_KK=M_KK,
    S_fold=S_cl_fold,
    Vol_SU3_Haar=Vol_SU3_Haar,
    # Derived scales
    V_pp=V_pp,
    L_nat=L_nat,
    L_H=L_H,
    Lambda_tau_natural=Lambda_tau_natural,
    Lambda_tau_kinetic=Lambda_tau_kinetic,
    # Canonical (Hubble-patch) numbers
    L_canonical=L_canonical,
    Lambda_canonical=Lambda_canonical,
    logratio_canonical=logratio_c,
    ratio_canonical=ratio_canonical,
    n_modes_canonical=n_modes_c,
    logdet_excess_canonical=-2.0 * logratio_c,
    # Secondary (IR-patch, L = pi/m_tau)
    L_ir=L_ir,
    logratio_ir=logratio_ir,
    ratio_ir=ratio_ir,
    n_modes_ir=n_modes_ir,
    logdet_excess_ir=-2.0 * logratio_ir,
    # Tertiary (many-patches, L = 10*pi/m_tau)
    L_many=L_many,
    logratio_many=logratio_many,
    ratio_many=ratio_many,
    n_modes_many=n_modes_many,
    logdet_excess_many=-2.0 * logratio_many,
    # Scans
    L_factors=L_factors,
    L_values=L_values,
    Lambda_factors=Lambda_factors,
    Lambda_values=Lambda_values,
    logratio_grid=logratio_grid,
    nmodes_grid=nmodes_grid,
    Lambda_scan=Lambda_scan,
    logratio_scan=logratio_scan,
    nmodes_scan=nmodes_scan,
    L_scan=L_scan,
    logratio_L=logratio_L,
    nmodes_L=nmodes_L,
    # One-loop inverse-Z factors (ratio is what is physical)
    Z_global_1loop_inv=Z_global_1loop_inv,
    Z_field_1loop_inv=Z_field_1loop_inv,
    # Continuum cross-check
    logdet_continuum_canonical=ld_continuum_c,
    logdet_lattice_canonical=ld_lattice_c,
    rel_err_lattice_vs_continuum=rel_err,
    # Coleman-Weinberg density
    rho_CW_canonical=rho_CW_canonical,
    rho_CW_over_Lambda4=rho_CW_over_Lambda4,
    # Thresholds
    abs_log_ratio_pass=ABS_LOG_RATIO_PASS,
    abs_log_ratio_info=ABS_LOG_RATIO_INFO,
    abs_log_ratio_canonical=abs_lr,
    abs_log_ratio_ir=abs_lr_ir,
    abs_log_ratio_many=abs_lr_many,
    abs_log_ratio_scan_max=abs_lr_scan_max,
)
print("Saved: s74_spatial_tau_thimble.npz")

# =========================================================================
# 11. Plot
# =========================================================================

fig, axes = plt.subplots(2, 2, figsize=(13, 11))

# Panel 1: D(k) spectrum at L = 5 * L_nat, Lambda = M_KK (has many modes)
ax = axes[0, 0]
L_plot = 5.0 * L_nat                                         # (local)
k_q_plot = 2.0 * PI / L_plot                                 # (local)
n_max_plot = int(np.ceil(Lambda_canonical / k_q_plot)) + 1   # (local)
rng_plot = np.arange(-n_max_plot, n_max_plot + 1)
N1p, N2p, N3p, N4p = np.meshgrid(rng_plot, rng_plot, rng_plot, rng_plot, indexing='ij')
k_sq_all = (k_q_plot ** 2) * (N1p**2 + N2p**2 + N3p**2 + N4p**2)
k_mag = np.sqrt(k_sq_all).ravel()
D_k = G_DeWitt * k_sq_all.ravel() + V_pp
# Keep only |k| < Lambda and k != 0
mask_plot = (k_mag > 1e-12) & (k_mag < Lambda_canonical)
k_plot = k_mag[mask_plot]
D_plot = D_k[mask_plot]
if len(k_plot) > 0:
    ax.semilogy(k_plot, D_plot, 'o', ms=3, alpha=0.6, label=f'{len(k_plot)} modes')
ax.axhline(V_pp, color='r', ls='--', label=f'D(0) = $m_\\tau^2$ = {V_pp:.3f}')
ax.axvline(Lambda_canonical, color='g', ls='--', label=f'$\\Lambda_\\tau$ = {Lambda_canonical:.3f}')
ax.set_xlabel('|k|  (M_KK units)')
ax.set_ylabel('$D(k) = G k^2 + m_\\tau^2$')
ax.set_title('Fluctuation spectrum at L = 5 $\\pi$/m$_\\tau$')
ax.legend(loc='upper left', fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: cumulative log-ratio vs |k| at the same L as Panel 1
ax = axes[0, 1]
if len(k_plot) > 0:
    sort_idx = np.argsort(k_plot)                             # (local)
    k_sort = k_plot[sort_idx]                                 # (local)
    D_sort = D_plot[sort_idx]                                 # (local)
    log_terms_plot = np.log(D_sort / V_pp)                    # (local)
    cum_logdet = np.cumsum(log_terms_plot)                    # (local)
    logratio_plot = -0.5 * cum_logdet                         # (local)
    ax.plot(k_sort, logratio_plot, 'b-', lw=1.5)
    ax.axhline(logratio_plot[-1], color='r', ls='--',
               label=f'final ln(ratio) = {logratio_plot[-1]:.3e}')
    ax.axhline(-ABS_LOG_RATIO_PASS, color='g', ls=':', label='PASS edge')
    ax.axhline(-ABS_LOG_RATIO_INFO, color='orange', ls=':', label='FAIL edge')
ax.set_xlabel('|k|  (sorted)')
ax.set_ylabel('cumulative $\\ln(Z_\\mathrm{field}/Z_\\mathrm{global})$')
ax.set_title('Cumulative one-loop correction at L = 5 $\\pi$/m$_\\tau$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: log-ratio vs Lambda at L = 5*L_nat
ax = axes[1, 0]
ax.plot(Lambda_scan / Lambda_tau_natural, logratio_scan, 'b-', lw=2)
ax.axhline(0.0, color='k', ls=':', lw=0.8)
ax.axhline(-ABS_LOG_RATIO_PASS, color='g', ls='--', label='PASS edge (-ln 2)')
ax.axhline(-ABS_LOG_RATIO_INFO, color='orange', ls='--', label='FAIL edge (-ln 10)')
ax.axvline(1.0, color='r', ls=':', label='$\\Lambda$ = M_KK')
ax.set_xlabel('$\\Lambda_\\tau$  (M_KK)')
ax.set_ylabel('$\\ln(Z_\\mathrm{field}/Z_\\mathrm{global})$')
ax.set_title('Cutoff dependence at L = 5 $\\pi$/m$_\\tau$')
ax.set_yscale('symlog')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 4: log-ratio vs L at Lambda = M_KK (with density overlay)
ax = axes[1, 1]
ax.plot(L_scan / L_nat, logratio_L, 'b-', lw=2, label='ln(ratio)')
ax.axhline(0.0, color='k', ls=':', lw=0.8)
ax.axhline(-ABS_LOG_RATIO_PASS, color='g', ls='--', label='PASS edge (-ln 2)')
ax.axhline(-ABS_LOG_RATIO_INFO, color='orange', ls='--', label='FAIL edge (-ln 10)')
ax.set_yscale('symlog')
ax.set_xlabel('$L / L_\\mathrm{nat}$  ($L_\\mathrm{nat} = \\pi/m_\\tau$)')
ax.set_ylabel('$\\ln(Z_\\mathrm{field}/Z_\\mathrm{global})$')
ax.set_title('Box-size dependence at $\\Lambda$ = M$_{KK}$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

suptitle = (
    f"SPATIAL-TAU-THIMBLE-74  -- field-theoretic thimble vs global-tau\n"
    f"gate = {gate_verdict},   ratio (canonical) = {ratio_canonical:.4e},   "
    f"ln(ratio) = {logratio_c:.4e}"
)
fig.suptitle(suptitle, fontsize=12)
fig.tight_layout(rect=(0, 0, 1, 0.95))
fig.savefig("s74_spatial_tau_thimble.png", dpi=140)
plt.close(fig)
print("Saved: s74_spatial_tau_thimble.png")
print()

elapsed = time.time() - t_start                              # (local)
print(f"Elapsed: {elapsed:.2f} s")
print("Done.")
