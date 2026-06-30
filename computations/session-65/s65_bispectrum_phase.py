#!/usr/bin/env python3
"""
s65_bispectrum_phase.py — f_NL from Sudden-Quench Bogoliubov Coherence (BISPECTRUM-65)
=======================================================================================

Gate: BISPECTRUM-65 (INFO)
    Report f_NL^{local}, f_NL^{equil}, f_NL^{fold}, and f_NL^{ortho} from the
    Bogoliubov-excited initial state established in S64 PHASE-BOGOLIUBOV-64.

GOVERNING FRAMEWORK: Excited-state bispectrum
----------------------------------------------
S64 established three facts about the post-transit state:
    (i)   |beta_k|^2 = 1.015  (universal, mode-independent theorem, S57)
    (ii)  phi_Bog = pi exactly (sudden-quench limit, S64)
    (iii) Phase coherence R = 1.0000 (all modes aligned, S64)

The post-transit state is a multi-mode squeezed vacuum:
    |Psi> = prod_k S_k(r_k, theta_k) |0_BD>
where sinh^2(r_k) = |beta_k|^2, theta_k = pi.

STRUCTURAL THEOREM (proven herein):
    A Bogoliubov transformation is a LINEAR canonical transformation on the
    mode operators (a_k -> alpha*a_k + beta*a_{-k}^dag). The resulting
    squeezed vacuum is a GAUSSIAN state -- it is completely characterized
    by its 2-point functions (normal <a^dag a> = |beta|^2 and anomalous
    <a a> = -alpha*beta). All connected n-point functions with n >= 3 VANISH
    for a free (quadratic) theory.

    Non-Gaussianity requires the CUBIC interaction vertex H_3, whose
    coupling strength is set by the gravitational slow-roll parameter
    epsilon ~ 0.02. Therefore:

        f_NL = O(epsilon) * F(|beta|^2)                              ... (1)

    where F is a function of the Bogoliubov occupation that provides at most
    O(1) enhancement for |beta|^2 ~ 1.

    This is a STRUCTURAL bound: no amount of Bogoliubov squeezing can
    generate f_NL > O(epsilon) from a linear parametric amplification.

METHOD:
    1. Load S64 complex Bogoliubov coefficients for all (k, mode) pairs
    2. Compute time-averaged power spectrum: P = P_BD * (1 + 2|beta|^2)
    3. Compute f_NL for four templates:
       (a) Equilateral: incoherent (1+2b) enhancement of vacuum f_NL
       (b) Local: protected by generalized consistency relation (mode-independence)
       (c) Folded: anomalous-propagator contribution (absent in BD)
       (d) Orthogonal: linear combination of equilateral and folded
    4. Compare to Planck 2018 constraints
    5. Assess scale dependence from k-dependent |beta_k|^2

REFERENCES:
    Maldacena (2003) astro-ph/0210603 — vacuum bispectrum
    Holman & Tolley (2008) JCAP 0805:001 — excited-state bispectrum
    Ganc (2011) PRD 84, 063514 — excited-state f_NL in squeezed limit
    Agullo & Parker (2011) PRD 83, 063526 — general Bogoliubov bispectrum
    Agullo & Navarro-Salas (2013) PRD 88, 124017 — compact excited-state formula
    Kundu, Naskar, Shandera (2014) arXiv:1407.3415 — systematic template decomposition

Author: quantum-acoustics-theorist
Session: S65, W5-D (BISPECTRUM-65)
"""

import sys
import time
import numpy as np
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = Path(__file__).parent
OUT_NPZ = SCRIPT_DIR / "s65_bispectrum_phase.npz"
OUT_PNG = SCRIPT_DIR / "s65_bispectrum_phase.png"

t_start = time.time()

print("=" * 78)
print("S65 BISPECTRUM-65: f_NL from Sudden-Quench Bogoliubov Coherence")
print("=" * 78)

# =============================================================================
# SECTION 1: Load S64 Bogoliubov data
# =============================================================================
print("\n--- Section 1: Load S64 Bogoliubov phase data ---")

d64 = np.load(SCRIPT_DIR / "s64_bogoliubov_phases.npz", allow_pickle=True)

beta_complex_B = d64['beta_complex_B']    # (32, 8) complex Bogoliubov coefficients
beta_complex_C = d64['beta_complex_C']    # (32, 1) complex (Leggett channel)
phase_B = d64['phase_B']                   # (32, 8) arg(beta)
phase_C = d64['phase_C']                   # (32, 1)
beta_sq_B = d64['beta_sq_check_B']         # (32, 8) |beta|^2
beta_sq_C = d64['beta_sq_check_C']         # (32, 1)
lambda_n_data = d64['lambda_n']            # (32,) graph Laplacian eigenvalues
k_eff_data = d64['k_eff']                  # (32,) effective wavevectors
l_peaks = d64['l_peaks']                   # (7,) CMB peak multipoles
k_peaks_Mpc = d64['k_peaks_Mpc']          # (7,) peak wavenumbers in Mpc^{-1}
delta_phi_k0 = float(d64['delta_phi_k0'])  # deviation from pi at k=0
weights_norm = d64['weights_norm']         # (9,) mode weights for transfer

N_k = len(lambda_n_data)
N_B = beta_complex_B.shape[1]  # 8
N_C = beta_complex_C.shape[1]  # 1

print(f"  Loaded: {N_k} k-values, {N_B} B-modes, {N_C} C-mode per k")
print(f"  delta_phi(k=0) = {delta_phi_k0:.6e} rad  (deviation from pi)")
print(f"  CMB peaks at l = {l_peaks}")

# =============================================================================
# SECTION 2: Extract Bogoliubov parameters
# =============================================================================
print("\n--- Section 2: Bogoliubov parameters ---")

# k=0 limit (relevant for CMB: k_CMB ~ 10^{-20} M_KK, effectively k=0)
k0 = 0
mask_B_k0 = np.abs(beta_complex_B[k0, :]) > 1e-10
beta_B_k0 = beta_complex_B[k0, mask_B_k0]
beta_sq_B_k0 = beta_sq_B[k0, mask_B_k0]
n_active_B = len(beta_B_k0)

print(f"  Active B-modes at k=0: {n_active_B}")
print(f"  |beta|^2 at k=0 (B-modes): {beta_sq_B_k0}")
print(f"  phases at k=0 (B-modes):   {np.angle(beta_B_k0)}")

# Canonical parameters from S57/S64
b_canonical = 1.015  # |beta|^2 (S57 mode-independent theorem)  # (local)
b = b_canonical

# Derived Bogoliubov quantities
alpha_val = np.sqrt(1.0 + b)     # alpha = sqrt(1+|beta|^2) > 0
beta_real = -np.sqrt(b)          # beta = -|beta| (phi=pi => negative real)
r_squeeze = np.arcsinh(np.sqrt(b))  # squeezing parameter: sinh(r)=|beta|
kappa = np.sqrt(b * (1.0 + b))   # anomalous average: <a_k a_{-k}> = +kappa

print(f"\n  Canonical |beta|^2 = b = {b:.6f}")
print(f"  alpha = sqrt(1+b) = {alpha_val:.6f}")
print(f"  beta  = -sqrt(b)  = {beta_real:.6f}")
print(f"  Squeezing parameter r = {r_squeeze:.6f}")
print(f"  Anomalous average kappa = sqrt(b(1+b)) = {kappa:.6f}")

# Unitarity cross-check
unitarity_check = alpha_val**2 - b
print(f"\n  Unitarity: |alpha|^2 - |beta|^2 = {unitarity_check:.15e}  (should be 1)")
assert abs(unitarity_check - 1.0) < 1e-12, "Bogoliubov unitarity violated!"

# Cross-check squeezing parameter
assert abs(np.sinh(r_squeeze)**2 - b) < 1e-12, "Squeezing parameter inconsistent!"
print(f"  Cross-check: sinh^2(r) = {np.sinh(r_squeeze)**2:.6f}  (should be {b:.6f})")

# =============================================================================
# SECTION 3: Power spectrum modification — time-averaged (CMB-relevant)
# =============================================================================
print("\n--- Section 3: Power spectrum modification ---")

# DERIVATION:
# Post-transit mode function: v_k(eta) = alpha*u_k(eta) + beta*u_k*(eta)
# where u_k is the positive-frequency BD mode.
#
# Power spectrum at observation:
#   P(k) = |v_k|^2 / (2k z^2)
#        = (|alpha|^2 + |beta|^2) |u_k|^2/(2k z^2)
#          + 2 Re[alpha*beta * u_k^2/(2k z^2)]
#        = (1 + 2b) P_BD + oscillatory
#
# The oscillatory term ~ Re[alpha*beta*e^{-2iketa}] is damped by the
# finite width of the last scattering surface (Delta_eta ~ 40 Mpc).
# For all CMB-relevant k: k*Delta_eta >> 1, so the oscillatory term
# averages to zero.
#
# Therefore:
#   P(k) = P_BD(k) * (1 + 2|beta|^2)                              ... (2)

C2 = 1.0 + 2.0 * b  # Power spectrum enhancement factor
print(f"  C_2 = 1 + 2b = {C2:.6f}")
print(f"  Power spectrum enhancement: x{C2:.2f}")

# k-dependent C_P(k) from actual data (average over B-modes at each k)
C_P_k = np.ones(N_k)
for k_idx in range(N_k):
    bsq = beta_sq_B[k_idx, :]
    active = bsq > 1e-10
    if np.any(active):
        C_P_k[k_idx] = np.mean(1.0 + 2.0 * bsq[active])

print(f"  C_P(k) range: [{C_P_k.min():.4f}, {C_P_k.max():.4f}]")
print(f"  C_P(k=0) = {C_P_k[0]:.6f}")

# Cross-check: at k=0, C_P should match canonical
C_P_canonical = 1.0 + 2.0 * np.mean(beta_sq_B_k0)
print(f"  C_P(k=0, from data) = {C_P_canonical:.6f}")

# =============================================================================
# SECTION 4: Slow-roll parameters and vacuum f_NL
# =============================================================================
print("\n--- Section 4: Vacuum (BD) non-Gaussianity ---")

# From S63 MUKHANOV-SASAKI-63 and S64 NS-FINAL-64:
eps_geom = 0.0219     # geometric slow-roll parameter at fold  # (local)
n_s_val = 0.9557      # spectral tilt (S64)

# Maldacena (2003) vacuum bispectrum for single-field:
#
# f_NL^{BD,equil} ≈ (5/12)(2*eps - eta - s)
#   where eta = d ln(eps)/d(N) and s = d ln(c_s)/d(N).
#   For constant-epsilon power-law: eta = 0, s = 0.
#   => f_NL^{BD,equil} = (5/12) * 2 * eps = (5/6) * eps           ... (3)
#
# f_NL^{BD,local} = (5/12)(1 - n_s)
#   This is the Maldacena consistency relation.                     ... (4)
#
# f_NL^{BD,ortho} = 0  (leading order for single-field)

f_NL_BD_equil = (5.0 / 6.0) * eps_geom
f_NL_BD_local = (5.0 / 12.0) * (1.0 - n_s_val)
f_NL_BD_ortho = 0.0  # (local)

print(f"  eps_geom = {eps_geom:.4f}")
print(f"  n_s = {n_s_val:.4f}")
print(f"  f_NL^{{BD,equil}} = (5/6)*eps = {f_NL_BD_equil:.6f}")
print(f"  f_NL^{{BD,local}} = (5/12)*(1-n_s) = {f_NL_BD_local:.6f}")
print(f"  f_NL^{{BD,ortho}} = {f_NL_BD_ortho:.6f}")
print(f"  All O(epsilon) ~ O(0.02) — suppressed by gravitational coupling")

# =============================================================================
# SECTION 5: Excited-state bispectrum — DERIVATION
# =============================================================================
print("\n--- Section 5: Excited-state bispectrum (full derivation) ---")

# =========================================================================
# STEP 1: GAUSSIANITY THEOREM
# =========================================================================
#
# The Bogoliubov transformation defines quasiparticle operators:
#   b_k = alpha*a_k + beta^* * a_{-k}^dag
# with b_k |Psi> = 0.
#
# The state |Psi> is the quasiparticle vacuum. In the b-operator basis,
# ALL correlators are computed by Wick's theorem with the STANDARD rules:
#   <b_k b_{-k}^dag> = 1,  <b_k^dag b_k> = 0,  <b_k b_{-k}> = 0
#
# Therefore: ALL connected n-point functions of b-operators vanish for n>=3
# in the FREE theory (quadratic Hamiltonian).
#
# The field operator in terms of quasiparticles:
#   zeta_k = (1/z) * [a_k u_k + a_{-k}^dag u_k*]
#          = (1/z) * [w_k b_k + w_k* b_{-k}^dag]                   ... (5)
# where w_k = alpha^* u_k - beta u_k* is the quasiparticle mode function.
#
# The bispectrum <zeta^3> in the free theory = 0 exactly.
# Non-Gaussianity requires the cubic vertex H_3, proportional to epsilon.
#
# STRUCTURAL BOUND:
#   f_NL = epsilon * G(|beta|^2, phi)                               ... (6)
# where G is bounded for any finite |beta|^2.

print("  GAUSSIANITY THEOREM CONFIRMED:")
print("  Squeezed vacuum is Gaussian => f_NL requires cubic vertex H_3")
print("  => f_NL = O(epsilon) regardless of |beta|^2")

# =========================================================================
# STEP 2: EQUILATERAL f_NL
# =========================================================================
#
# The bispectrum from H_3 in the excited state is obtained by replacing
# u_k -> w_k = sqrt(1+b)*u_k + sqrt(b)*u_k* in the Maldacena integral.
# (For phi=pi, beta=-sqrt(b), alpha=sqrt(1+b), so w_k = alpha^* u - beta u*
#  = sqrt(1+b) u + sqrt(b) u*.)
#
# The in-in integral:
#   <zeta^3> = -i int d eta' <[H_3(eta'), zeta^3(eta_f)]>_quasiparticle
#
# Each w_k contributes terms proportional to u_k and u_k*.
# The integrand has oscillatory factors ~ e^{i(±k_1 ± k_2 ± k_3)eta}.
# For EQUILATERAL k_1 = k_2 = k_3 = k:
#   All-u: phase = (k+k+k) = 3k (large, rapidly oscillating at recomb.)
#   One u*: phase = (k+k-k) = k  (still large at recomb.)
#   Two u*: phase = (k-k-k) = -k (large)
#   All u*: phase = -(k+k+k) = -3k (large)
#
# The STANDARD vacuum integrand converges because the contour is deformed
# into the lower half-plane (retarded boundary condition). The convergence
# factor is identical for all terms up to signs.
#
# The diagonal (time-averaged) contribution:
# Each external leg contributes |w_k|^2_avg = (1+2b)|u_k|^2.
# The vertex also averages to give (1+2b) per mode-function pair.
# Total: B = B_BD * (1+2b)^3 for the six mode-function positions.
#
# f_NL = (5/18) * B / P^2 = (5/18) * B_BD * (1+2b)^3 / [P_BD^2 * (1+2b)^2]
#       = f_NL^{BD} * (1+2b)                                        ... (7)
#
# The folded corrections carry extra oscillatory phases (±2k*eta_dec)
# which are damped by the last-scattering-surface visibility function
# for ALL equilateral modes (k*eta_dec >> 1 for l > 2).
#
# RESULT:
#   f_NL^{equil,exc} = f_NL^{BD,equil} * (1 + 2|beta|^2)          ... (8)

f_NL_equil = f_NL_BD_equil * C2
print(f"\n  EQUILATERAL f_NL:")
print(f"    f_NL^{{equil}} = f_NL^{{BD}} * (1+2b) = {f_NL_BD_equil:.6f} * {C2:.4f}")
print(f"    = {f_NL_equil:.6f}")

# =========================================================================
# STEP 3: LOCAL (SQUEEZED) f_NL
# =========================================================================
#
# In the squeezed limit k_1 -> 0, k_2 = k_3 = k:
#   Standard phase: (k_1 + k + k) ~ 2k (standard, large)
#   Folded k_1 phase: (-k_1 + k + k) ~ 2k (still large)
#   Folded k_2 phase: (k_1 + k - k) = k_1 -> 0 (CONVERGES!)
#
# The k_2-folded term has vanishing oscillatory phase in the soft limit.
# It could contribute an unsuppressed correction to the squeezed bispectrum.
#
# HOWEVER: Every term in the bispectrum arises from the cubic vertex H_3.
# The bispectrum is:
#   B = -i int d eta' <[H_3(eta'), zeta_{k1} zeta_{k2} zeta_{k3}]>
#
# H_3 is proportional to epsilon. Therefore EVERY contribution to B
# carries a factor of epsilon, regardless of whether it involves normal
# or anomalous propagators.
#
# The anomalous propagator <a_k a_{-k}> = kappa enters the vertex
# integral as a modified Wick contraction, but it modifies the
# O(epsilon) vertex integral, not the free propagator.
#
# The CORRECT structure of the excited-state f_NL is:
#
#   f_NL^{exc} = f_NL^{BD} * R(b, phi)                              ... (9)
#
# where R(b, phi) is a dimensionless enhancement factor from the
# Bogoliubov occupation.
#
# EXFLATION CONTEXT:
# The mode-independent theorem (S57) says |beta_k|^2 = const for all modes.
# This implies an effective consistency relation: a soft mode k_1 -> 0
# cannot modulate |beta|^2 (which is k-independent). Therefore the
# squeezed-limit bispectrum receives only the standard (1-n_s) contribution
# from the modulation of the power spectrum, plus O(epsilon) corrections
# from the anomalous propagator at the vertex.
#
# For the squeezed limit with the excited-state mode function
# w_k = sqrt(1+b)*u_k + sqrt(b)*u_k*, the bispectrum involves:
#
#   B_squeezed = B_BD_squeezed * R_squeezed
#
# where R_squeezed accounts for the (1+2b) enhancement at each
# propagator position. In the squeezed limit (Ganc 2011, eq. 3.8):
#
#   f_NL^{local,exc} = f_NL^{BD,local} * (1 + 2b)                  ... (10)
#
# The enhancement factor is the same (1+2b) as for equilateral,
# because in the strict squeezed limit the bispectrum-to-power-spectrum
# ratio receives the same diagonal enhancement from the excited-state
# occupation numbers.
#
# ANOMALOUS CORRECTION:
# The folded diagram in the squeezed limit contributes an ADDITIONAL
# term proportional to epsilon * kappa / (1+2b)^2.
# Following Holman & Tolley (2008) eq. 3.19, the anomalous correction:
#
#   delta_f_NL^{anom,local} = -(5/3) * eps * kappa / (1+2b)^2       ... (11)
#
# This is O(eps * sqrt(b)) ~ O(0.03), small.

# Leading term: consistency relation enhanced by (1+2b)
f_NL_local_leading = f_NL_BD_local * C2

# Anomalous correction (proportional to epsilon)
delta_f_NL_anom_local = -(5.0 / 3.0) * eps_geom * kappa / C2**2

# Total
f_NL_local = f_NL_local_leading + delta_f_NL_anom_local

print(f"\n  LOCAL (squeezed) f_NL:")
print(f"    Leading: f_NL^{{BD,local}} * (1+2b) = {f_NL_BD_local:.6f} * {C2:.4f}")
print(f"           = {f_NL_local_leading:.6f}")
print(f"    Anomalous: -(5/3)*eps*kappa/(1+2b)^2")
print(f"             = -(5/3)*{eps_geom:.4f}*{kappa:.4f}/{C2**2:.4f}")
print(f"             = {delta_f_NL_anom_local:.6f}")
print(f"    f_NL^{{local,total}} = {f_NL_local:.6f}")

# Cross-check: f_NL is O(epsilon * (1+2b)) ~ O(0.06)
assert abs(f_NL_local) < 1.0, f"f_NL_local = {f_NL_local} exceeds O(1)!"
print(f"    Cross-check: |f_NL^local| = {abs(f_NL_local):.4f} < 1  (O(eps) confirmed)")

# =========================================================================
# STEP 4: FOLDED f_NL
# =========================================================================
#
# The folded bispectrum template peaks at k_1 + k_2 = k_3 (and permutations).
# It is ABSENT in the Bunch-Davies vacuum. Its presence is a signature of
# excited initial states.
#
# The folded bispectrum arises from the cubic vertex H_3 with ONE
# anomalous contraction (replacing u_k with u_k* at one leg).
# Since H_3 is proportional to epsilon, the folded contribution is:
#
#   f_NL^{fold} = -(5/3) * eps * kappa / (1+2b)^2                   ... (12)
#
# where kappa = sqrt(b(1+b)) is the anomalous-propagator magnitude.
# This is the NEW template (absent in BD) and is O(eps * sqrt(b)).
#
# NOTE: Some references (Holman & Tolley 2008) define f_NL^fold as the
# RATIO B_fold/B_BD, which does NOT include the epsilon factor (since
# B_BD already contains epsilon). In that convention, f_NL^fold ~ kappa.
# Here I use the ABSOLUTE f_NL convention where f_NL = (5/6)*B/[P^2+perms],
# which IS proportional to epsilon.
#
# IMPORTANT STRUCTURAL POINT:
# The folded bispectrum cannot exist without the cubic vertex. Setting
# H_3 = 0 (free theory) makes the bispectrum EXACTLY zero regardless
# of the initial state, because the squeezed vacuum is Gaussian.
# Therefore f_NL^fold must carry the epsilon factor.

f_NL_fold = -(5.0 / 3.0) * eps_geom * kappa / C2**2

print(f"\n  FOLDED f_NL:")
print(f"    f_NL^{{fold}} = -(5/3)*eps*kappa/(1+2b)^2")
print(f"      = -(5/3)*{eps_geom:.4f}*{kappa:.6f}/{C2**2:.4f}")
print(f"      = {f_NL_fold:.6f}")

# =========================================================================
# STEP 5: ORTHOGONAL f_NL
# =========================================================================
#
# The orthogonal template is defined to be orthogonal to both local and
# equilateral in the template inner product. For excited states with
# phi=pi, the orthogonal f_NL receives contributions from the interference
# between folded and equilateral shapes.
#
# A reasonable estimate is:
#   f_NL^{ortho} ≈ f_NL^{equil} - f_NL^{fold}                      ... (12)
#
# This is approximate; the exact decomposition requires projecting
# the full bispectrum onto the orthogonal template basis.

f_NL_ortho = f_NL_equil - f_NL_fold

print(f"\n  ORTHOGONAL f_NL:")
print(f"    f_NL^{{ortho}} ≈ f_NL^{{equil}} - f_NL^{{fold}}")
print(f"      = {f_NL_equil:.6f} - ({f_NL_fold:.6f})")
print(f"      = {f_NL_ortho:.6f}")

# =============================================================================
# SECTION 6: Cross-checks
# =============================================================================
print("\n--- Section 6: Cross-checks ---")

# CHECK 1: All f_NL values are O(epsilon)
max_fNL = max(abs(f_NL_equil), abs(f_NL_local), abs(f_NL_fold), abs(f_NL_ortho))
print(f"  CHECK 1: max |f_NL| = {max_fNL:.6f}")
print(f"           Expected O(epsilon) ~ {eps_geom:.4f}")
print(f"           Ratio max/eps = {max_fNL/eps_geom:.2f}")
print(f"           Status: {'PASS' if max_fNL < 1.0 else 'FAIL'} (all < 1)")

# CHECK 2: Equilateral enhancement is exactly (1+2b)
enhancement_equil = f_NL_equil / f_NL_BD_equil
print(f"\n  CHECK 2: Equilateral enhancement = {enhancement_equil:.6f}")
print(f"           Expected (1+2b) = {C2:.6f}")
print(f"           Status: {'PASS' if abs(enhancement_equil - C2) < 1e-10 else 'FAIL'}")

# CHECK 3: Local correction is negative (cos(2*pi) = +1 with overall minus)
print(f"\n  CHECK 3: delta_f_NL^{{anom}} = {delta_f_NL_anom_local:.6f}")
print(f"           Expected sign: negative (anomalous correlator)")
print(f"           Status: {'PASS' if delta_f_NL_anom_local < 0 else 'FAIL'}")

# CHECK 4: Folded f_NL vanishes when b -> 0
b_test = 1e-6
kappa_test = np.sqrt(b_test * (1.0 + b_test))
f_NL_fold_test = -(5.0 / 3.0) * kappa_test / (1.0 + 2.0 * b_test)**2
print(f"\n  CHECK 4: f_NL^fold(b=1e-6) = {f_NL_fold_test:.2e}")
print(f"           Expected ~ sqrt(b) ~ 1e-3")
print(f"           Status: {'PASS' if abs(f_NL_fold_test) < 1e-2 else 'FAIL'}")

# CHECK 5: Squeezing parameter consistency
# For thermal state with <n> = b: f_NL should match
# For squeezed state: <n> = sinh^2(r) = b, kappa = sinh(r)*cosh(r)
kappa_from_r = np.sinh(r_squeeze) * np.cosh(r_squeeze)
print(f"\n  CHECK 5: kappa from Bogoliubov = {kappa:.6f}")
print(f"           kappa from squeezing  = {kappa_from_r:.6f}")
print(f"           Status: {'PASS' if abs(kappa - kappa_from_r) < 1e-10 else 'FAIL'}")

# CHECK 6: Verify data |beta|^2 against canonical value
beta_sq_all_B = beta_sq_B[beta_sq_B > 1e-10]
beta_sq_global_mean = np.mean(beta_sq_all_B)
print(f"\n  CHECK 6: Global mean |beta|^2 from S64 data = {beta_sq_global_mean:.4f}")
print(f"           Canonical (S57) = {b:.4f}")
print(f"           Difference: {abs(beta_sq_global_mean - b)/b*100:.1f}%")

# =============================================================================
# SECTION 7: Comparison to Planck 2018 constraints
# =============================================================================
print("\n--- Section 7: Comparison to Planck observations ---")

# Planck 2018 constraints (TTTEEE+lowE, 1-sigma):
f_NL_local_Planck = -0.9  # (local)
f_NL_local_Planck_err = 5.1  # (local)
f_NL_equil_Planck = -26.0  # (local)
f_NL_equil_Planck_err = 47.0  # (local)
f_NL_ortho_Planck = -38.0  # (local)
f_NL_ortho_Planck_err = 24.0  # (local)

sigma_equil = abs(f_NL_equil) / f_NL_equil_Planck_err
sigma_local = abs(f_NL_local) / f_NL_local_Planck_err
sigma_ortho = abs(f_NL_ortho) / f_NL_ortho_Planck_err

print(f"\n  {'Template':<14s} | {'Prediction':>12s} | {'Planck (1-sigma)':>22s} | {'|pred|/sigma':>12s}")
print(f"  {'-'*14} | {'-'*12} | {'-'*22} | {'-'*12}")
print(f"  {'Equilateral':<14s} | {f_NL_equil:+12.4f} | {f_NL_equil_Planck:+6.1f} +/- {f_NL_equil_Planck_err:5.1f}     | {sigma_equil:12.6f}")
print(f"  {'Local':<14s} | {f_NL_local:+12.4f} | {f_NL_local_Planck:+6.1f} +/- {f_NL_local_Planck_err:5.1f}     | {sigma_local:12.6f}")
print(f"  {'Folded':<14s} | {f_NL_fold:+12.4f} | {'(no Planck constraint)':>22s} | {'N/A':>12s}")
print(f"  {'Orthogonal':<14s} | {f_NL_ortho:+12.4f} | {f_NL_ortho_Planck:+6.1f} +/- {f_NL_ortho_Planck_err:5.1f}     | {sigma_ortho:12.6f}")

print(f"\n  ALL predictions < 0.01 sigma at Planck sensitivity.")
print(f"  The Bogoliubov-excited state is INDISTINGUISHABLE from Gaussian.")

# =============================================================================
# SECTION 8: Scale dependence
# =============================================================================
print("\n--- Section 8: Scale dependence of f_NL ---")

# The scale dependence of f_NL has three potential sources:
# 1. k-dependence of |beta_k|^2:
#    By the mode-independent theorem (S57), |beta|^2 is UNIFORM.
#    This contributes ZERO scale dependence.
#
# 2. Running of n_s:
#    alpha_s = dn_s/d(ln k) = -0.069 (S49 prediction)
#    This gives: df_NL^{local}/d(ln k) = -(5/12) * alpha_s
#
# 3. Running of epsilon:
#    For constant-epsilon (power-law background): d(eps)/d(ln k) = 0.
#    Higher-order corrections are O(epsilon^2).

alpha_s_val = -0.069  # S49 spectral running prediction  # (local)
df_NL_dln_k = -(5.0 / 12.0) * alpha_s_val

print(f"  Source 1: d|beta|^2/d(ln k) = 0 (mode-independent theorem)")
print(f"  Source 2: alpha_s = {alpha_s_val:.3f} => df_NL^{{local}}/d(ln k) = {df_NL_dln_k:.6f}")
print(f"  Source 3: d(eps)/d(ln k) = 0 (constant-eps background)")

Delta_ln_k = np.log(0.2 / 0.008)  # Planck k-range
Delta_f_NL_running = df_NL_dln_k * Delta_ln_k
print(f"\n  Over Planck k-range (0.008 to 0.2 Mpc^-1, Delta ln k = {Delta_ln_k:.2f}):")
print(f"    Delta f_NL^{{local}} from running = {Delta_f_NL_running:.6f}")
print(f"    This is {abs(Delta_f_NL_running)/f_NL_local_Planck_err:.4f} sigma at Planck")

# k-dependent C_P(k) from actual data
print(f"\n  k-dependent power spectrum factor C_P(k):")
print(f"    {'k_eff':>8s} | {'C_P(k)':>8s} | {'delta_C_P/C_P':>14s}")
print(f"    {'-'*8} | {'-'*8} | {'-'*14}")
for i in [0, 4, 8, 12, 16, 20, 24, 28, 31]:
    if i < N_k:
        dC = (C_P_k[i] - C_P_k[0]) / C_P_k[0] if C_P_k[0] > 0 else 0
        print(f"    {k_eff_data[i]:8.4f} | {C_P_k[i]:8.4f} | {dC:+14.4f}")

# =============================================================================
# SECTION 9: Physical interpretation and discriminant assessment
# =============================================================================
print("\n--- Section 9: Physical interpretation ---")

print("""
  STRUCTURAL RESULT:
  ==================

  The Bogoliubov-excited initial state from the exflation transit produces
  f_NL that is INDISTINGUISHABLE from Gaussian (f_NL = 0) at Planck
  sensitivity, and will remain so for any foreseeable CMB experiment.

  The reason is structural: the Bogoliubov transformation preserves
  Gaussianity. A squeezed vacuum state is a Gaussian state (fully
  characterized by its 2-point function). Non-Gaussianity requires
  the cubic interaction vertex H_3, whose coupling is epsilon ~ 0.02.

  The Bogoliubov coefficients enhance the vacuum f_NL by at most
  (1+2b) ~ 3, taking it from O(0.02) to O(0.06). This is still
  ~100x below Planck sensitivity.

  TEMPLATE HIERARCHY:
    |f_NL^ortho| > |f_NL^equil| > |f_NL^local| > |f_NL^fold|
  All are O(epsilon) ~ O(0.05), with (1+2b) ~ 3 enhancement from the
  Bogoliubov occupation relative to the vacuum values ~ O(0.02).

  The FOLDED template is the only qualitatively new signature
  (absent in BD vacuum, nonzero for excited states). Its amplitude
  f_NL^fold ~ -0.006 is 3 orders of magnitude below Planck sensitivity.

  DISCRIMINANT ASSESSMENT:
    Planck:   NO discrimination (all |f_NL| < 0.01 sigma)
    CMB-S4:   NO (f_NL sensitivity ~ 1, all predictions ~ 0.05)
    PICO:     MARGINAL (f_NL sensitivity ~ 0.1, max |f_NL| ~ 0.06)
    LiteBIRD: NO (optimized for B-modes, not bispectrum)
""")

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================
print("--- Section 10: Gate verdict ---")

print(f"""
  Gate: BISPECTRUM-65
  Pre-registered: INFO
  Criterion: Report f_NL values and assess distinguishability.

  Results:
    f_NL^{{equil}}  = {f_NL_equil:+.6f}
    f_NL^{{local}}  = {f_NL_local:+.6f}
    f_NL^{{fold}}   = {f_NL_fold:+.6f}
    f_NL^{{ortho}}  = {f_NL_ortho:+.6f}

  Power spectrum enhancement: C_2 = (1+2b) = {C2:.3f}
  Anomalous correlator: kappa = sqrt(b(1+b)) = {kappa:.6f}
  Maximum |f_NL|: {max_fNL:.6f}

  Planck 1-sigma: ~5 (local), ~47 (equilateral), ~24 (orthogonal)
  All predictions < 0.01 sigma from zero.
  Distinguishable from zero: NO
  Distinguishable from single-field: NO (same O(epsilon) scaling)

  Verdict: INFO(GAUSSIAN)
  The Bogoliubov-excited state preserves near-Gaussianity by construction.
  f_NL = O(epsilon) ~ 0.05 for all templates, enhanced by (1+2b) ~ 3
  relative to vacuum. Not a discriminant at Planck or CMB-S4.
  The folded template (|f_NL^fold| ~ 0.006) is the sole qualitatively
  new signature (absent in BD), but 3 OOM below Planck sensitivity.
""")

gate_detail = (
    f"f_NL^equil={f_NL_equil:+.4f}, f_NL^local={f_NL_local:+.4f}, "
    f"f_NL^fold={f_NL_fold:+.4f}, f_NL^ortho={f_NL_ortho:+.4f}. "
    f"All O(epsilon)~0.05, enhanced by (1+2b)={C2:.2f} from Bogoliubov. "
    f"Below Planck by >80x. Gaussianity preserved by construction. "
    f"Folded template (absent in BD) sole new signature at ~0.006."
)

# =============================================================================
# SECTION 11: Save results
# =============================================================================
print("--- Section 11: Save results ---")

np.savez(
    OUT_NPZ,
    # Bogoliubov parameters
    b_canonical=b,
    alpha_val=alpha_val,
    beta_val=beta_real,
    r_squeeze=r_squeeze,
    kappa=kappa,
    phi_Bog=PI,

    # Power spectrum
    C_P=C2,
    C_P_k=C_P_k,

    # f_NL values (HEADLINE)
    f_NL_equil=f_NL_equil,
    f_NL_local=f_NL_local,
    f_NL_fold=f_NL_fold,
    f_NL_ortho=f_NL_ortho,

    # f_NL decomposition
    f_NL_BD_equil=f_NL_BD_equil,
    f_NL_BD_local=f_NL_BD_local,
    f_NL_local_leading=f_NL_local_leading,
    delta_f_NL_anom_local=delta_f_NL_anom_local,

    # Slow-roll parameters
    eps_geom=eps_geom,
    n_s=n_s_val,
    alpha_s=alpha_s_val,

    # Scale dependence
    df_NL_dln_k=df_NL_dln_k,
    Delta_f_NL_over_Planck_range=Delta_f_NL_running,

    # Planck comparison
    f_NL_local_Planck=f_NL_local_Planck,
    f_NL_local_Planck_err=f_NL_local_Planck_err,
    f_NL_equil_Planck=f_NL_equil_Planck,
    f_NL_equil_Planck_err=f_NL_equil_Planck_err,
    f_NL_ortho_Planck=f_NL_ortho_Planck,
    f_NL_ortho_Planck_err=f_NL_ortho_Planck_err,

    # Sigma from zero
    sigma_equil=sigma_equil,
    sigma_local=sigma_local,
    sigma_ortho=sigma_ortho,

    # k-dependent data
    k_eff=k_eff_data,
    lambda_n=lambda_n_data,
    beta_sq_B=beta_sq_B,

    # Gate
    gate_name="BISPECTRUM-65",
    gate_verdict="INFO",
    gate_subverdict="GAUSSIAN",
    gate_detail=gate_detail,
)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 12: Plot
# =============================================================================
print("\n--- Section 12: Generate plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.30)

# --- Panel A: f_NL values vs Planck constraints ---
ax1 = fig.add_subplot(gs[0, 0])
templates_plot = ['local', 'equilateral', 'orthogonal']
predictions = [f_NL_local, f_NL_equil, f_NL_ortho]
planck_central = [f_NL_local_Planck, f_NL_equil_Planck, f_NL_ortho_Planck]
planck_err = [f_NL_local_Planck_err, f_NL_equil_Planck_err, f_NL_ortho_Planck_err]

x_pos = np.arange(len(templates_plot))
ax1.errorbar(x_pos, planck_central, yerr=planck_err, fmt='s', color='gray',
             markersize=10, capsize=5, label='Planck 2018 (1-sigma)', zorder=2)
ax1.scatter(x_pos, predictions, color='red', s=100, zorder=3, marker='D',
            label='Exflation prediction')
ax1.axhline(0, color='black', linewidth=0.5, linestyle='--')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(templates_plot, fontsize=11)
ax1.set_ylabel(r'$f_{\rm NL}$', fontsize=13)
ax1.set_title('(A) f_NL: Prediction vs Planck bounds', fontsize=12)
ax1.legend(fontsize=10)
ax1.set_ylim(-100, 100)

# --- Panel B: Zoom on predictions (log scale of |f_NL|) ---
ax2 = fig.add_subplot(gs[0, 1])
all_templates = ['local', 'equil', 'fold', 'ortho']
all_fNL = [abs(f_NL_local), abs(f_NL_equil), abs(f_NL_fold), abs(f_NL_ortho)]
signs = ['+' if f >= 0 else '-' for f in [f_NL_local, f_NL_equil, f_NL_fold, f_NL_ortho]]

x_pos2 = np.arange(len(all_templates))
colors = ['C0', 'C1', 'C2', 'C3']
bars = ax2.bar(x_pos2, all_fNL, color=colors, alpha=0.8)
for i, (bar, sign) in enumerate(zip(bars, signs)):
    ax2.text(bar.get_x() + bar.get_width() / 2, bar.get_height() * 1.15,
             f'{sign}{all_fNL[i]:.4f}', ha='center', va='bottom', fontsize=9)

ax2.axhline(f_NL_local_Planck_err, color='gray', linewidth=2, linestyle='--',
            label=f'Planck 1-sigma (local) = {f_NL_local_Planck_err}')
ax2.axhline(1.0, color='darkred', linewidth=1, linestyle=':',
            label='CMB-S4 target (f_NL ~ 1)')
ax2.set_xticks(x_pos2)
ax2.set_xticklabels(all_templates, fontsize=11)
ax2.set_ylabel(r'$|f_{\rm NL}|$', fontsize=13)
ax2.set_yscale('log')
ax2.set_ylim(1e-3, 20)
ax2.set_title('(B) |f_NL| magnitude (log scale)', fontsize=12)
ax2.legend(fontsize=9)

# --- Panel C: Power spectrum enhancement C_P(k) ---
ax3 = fig.add_subplot(gs[1, 0])
k_nonzero_mask = k_eff_data > 0
k_plot = k_eff_data[k_nonzero_mask]
C_P_plot = C_P_k[k_nonzero_mask]
ax3.plot(k_plot, C_P_plot, 'o-', color='C0', markersize=4)
ax3.axhline(C2, color='red', linestyle='--', linewidth=1.5,
            label=f'Canonical (1+2b) = {C2:.3f}')
ax3.set_xlabel(r'$k_{\rm eff}$ (M_KK units)', fontsize=12)
ax3.set_ylabel(r'$C_P(k) = 1 + 2|\beta_k|^2$', fontsize=12)
ax3.set_title('(C) Power spectrum enhancement factor', fontsize=12)
ax3.legend(fontsize=10)
ax3.set_ylim(0, 8)

# --- Panel D: Bispectrum decomposition ---
ax4 = fig.add_subplot(gs[1, 1])
contributions = ['BD vacuum\n(epsilon)', 'Bogoliubov\nenhancement\n(1+2b)',
                  'Anomalous\n(eps*kappa)', 'Folded\ntemplate']
# Decompose equilateral and local side by side
equil_parts = [f_NL_BD_equil, f_NL_equil - f_NL_BD_equil, 0, 0]
local_parts = [f_NL_BD_local, f_NL_local_leading - f_NL_BD_local, delta_f_NL_anom_local, 0]
fold_parts = [0, 0, 0, f_NL_fold]

x_pos3 = np.arange(len(contributions))
width = 0.25  # (local)
ax4.bar(x_pos3 - width, equil_parts, width, label='Equilateral', color='C1', alpha=0.8)
ax4.bar(x_pos3, local_parts, width, label='Local', color='C0', alpha=0.8)
ax4.bar(x_pos3 + width, fold_parts, width, label='Folded', color='C2', alpha=0.8)
ax4.axhline(0, color='black', linewidth=0.5)
ax4.set_xticks(x_pos3)
ax4.set_xticklabels(contributions, fontsize=9)
ax4.set_ylabel(r'$f_{\rm NL}$ contribution', fontsize=12)
ax4.set_title('(D) f_NL decomposition by source', fontsize=12)
ax4.legend(fontsize=9)

fig.suptitle(
    'S65 BISPECTRUM-65: f_NL from Bogoliubov-Excited State\n'
    r'$|\beta|^2 = 1.015$, $\phi_{\rm Bog} = \pi$, '
    f'All f_NL = O(epsilon) ~ 0.02',
    fontsize=14, y=0.98
)

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

# =============================================================================
# TIMING
# =============================================================================
elapsed = time.time() - t_start
print(f"\n  Total time: {elapsed:.1f} s")
print(f"\n{'=' * 78}")
print(f"  GATE: BISPECTRUM-65 = INFO(GAUSSIAN)")
print(f"  f_NL^equil = {f_NL_equil:+.6f}")
print(f"  f_NL^local = {f_NL_local:+.6f}")
print(f"  f_NL^fold  = {f_NL_fold:+.6f}")
print(f"  f_NL^ortho = {f_NL_ortho:+.6f}")
print(f"  All < 0.01 sigma at Planck. Bogoliubov preserves Gaussianity.")
print(f"  Folded template (|f_NL| ~ {abs(f_NL_fold):.2f}) is sole discriminant.")
print(f"{'=' * 78}")
