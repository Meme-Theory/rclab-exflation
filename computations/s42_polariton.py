"""
S42 W5-4: Digamma-polariton — B2 Collective Mode / Gauge Boson Hybridization
=============================================================================

Computes whether the B2 collective mode (GPV at omega=0.792 M_KK) or the B2
single-particle gap-edge mode (0.845 M_KK) hybridizes with KK gauge bosons
to form a phonon-polariton. Tests the PI's proposal that the Higgs mass is
the polariton gap (anticrossing energy).

Physics: In solid-state, phonon-polaritons form when an optical phonon branch
crosses a photon dispersion. The hybridization opens a gap = 2g at the crossing
point, where g is the dipole coupling strength. The polariton has mixed
phonon-photon character throughout.

Here, the "phonon" = B2 Digamma-mode (internal-space vibrational mode of D_K)
and the "photon" = KK gauge boson (4D gauge field from dimensional reduction).
The coupling is the Kosmann connection matrix element V(B2, gauge).

Pre-registered gate POLARITON-42:
  PASS: Delta_pol < 0.01 x M_KK
  FAIL: Delta_pol > 0.1 x M_KK

Author: Quantum Acoustics Theorist
Date: 2026-03-13
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

# =============================================================================
# SECTION 1: LOAD DATA FROM PRIOR SESSIONS
# =============================================================================

base_dir = os.path.dirname(os.path.abspath(__file__))

# Load V matrix and eigenvalues from S36 (full 8-mode multisector ED)
s36_data = np.load(os.path.join(base_dir, 's36_multisector_ed.npz'), allow_pickle=True)
V_8x8 = s36_data['V_8x8_full']          # (8,8) Kosmann coupling matrix
E_8 = s36_data['E_8_full']              # (8,) single-particle energies in M_KK
branch_labels = s36_data['branch_labels'] # ['B2[0]','B2[1]','B2[2]','B2[3]','B1','B3[0]','B3[1]','B3[2]']

# Load QRPA data from S40 for collective mode frequencies
s40_data = np.load(os.path.join(base_dir, 's40_qrpa_modes.npz'), allow_pickle=True)
omegas_qrpa = s40_data['omegas_pos']     # (8,) QRPA mode frequencies
strengths = s40_data['strengths']        # (8,) transition strengths
omega_gpv = float(s40_data['omega_gpv'])  # GPV frequency = 0.792 M_KK
E_qp = s40_data['E_qp']                 # (8,) BdG quasiparticle energies
u_k = s40_data['u_k']                   # BdG coherence factors
v_k = s40_data['v_k']                   # BdG coherence factors
tau_fold = float(s40_data['tau_fold'])

print("=" * 72)
print("S42 W5-4: DIGAMMA-POLARITON HYBRIDIZATION COMPUTATION")
print("=" * 72)
print()

# =============================================================================
# SECTION 2: IDENTIFY THE MODES
# =============================================================================

print("--- SECTION 2: MODE IDENTIFICATION ---")
print()

# Branch structure at fold (tau = 0.190):
# B2: 4 modes at E = 0.845 M_KK (flat band, degenerate quartet)
# B1: 1 mode at E = 0.819 M_KK (acoustic gap edge)
# B3: 3 modes at E = 0.978 M_KK (dispersive optical triplet)

omega_B2_sp = E_8[0]     # B2 single-particle energy = 0.845 M_KK
omega_B1_sp = E_8[4]     # B1 single-particle energy = 0.819 M_KK
omega_B3_sp = E_8[5]     # B3 single-particle energy = 0.978 M_KK

print(f"Single-particle energies (M_KK units):")
print(f"  B2 (flat quartet): {omega_B2_sp:.6f}")
print(f"  B1 (acoustic):     {omega_B1_sp:.6f}")
print(f"  B3 (optical trip):  {omega_B3_sp:.6f}")
print()

# BdG quasiparticle energies (2-particle gap)
omega_B2_qp = np.mean(E_qp[0:4])
omega_B1_qp = E_qp[4]
omega_B3_qp = np.mean(E_qp[5:8])

print(f"BdG quasiparticle energies (M_KK units):")
print(f"  B2 (mean): {omega_B2_qp:.6f}")
print(f"  B1:        {omega_B1_qp:.6f}")
print(f"  B3 (mean): {omega_B3_qp:.6f}")
print()

# QRPA collective modes
idx_giant = np.argmax(strengths)
omega_giant = omegas_qrpa[idx_giant]
S_giant = strengths[idx_giant]

print(f"QRPA collective modes:")
print(f"  {'omega':>10s}  {'strength':>12s}  note")
for i, (w, s) in enumerate(zip(omegas_qrpa, strengths)):
    note = ""
    if i == idx_giant:
        note = " <-- GIANT RESONANCE (97.5% EWSR)"
    elif i == 0:
        note = " <-- lowest (B1-like)"
    print(f"  {w:10.6f}  {s:12.6e}{note}")
print(f"  GPV (pair vibration): {omega_gpv:.3f}")
print()

# KK gauge boson masses from the spectral action
# In the NCG framework, gauge boson masses arise from the spectral action a_4 term.
# The first KK gauge boson mass is of order M_KK (by definition — it IS the KK scale).
# More precisely, the KK gauge bosons form a tower starting at ~M_KK.
# The gap-edge modes (B1 at 0.819, B2 at 0.845, B3 at 0.978) are the LOWEST
# KK modes — they ARE the first KK excitations.
#
# The key question: which mode hybridizes with which?
# In condensed matter: phonon-polariton = optical phonon crossing photon dispersion.
# Here: Digamma-mode = internal vibrational mode
#        Gauge boson = propagating 4D field
#
# The crucial distinction: the B2 mode IS a KK mode. It is not a separate
# "phonon" that hybridizes with a separate "gauge boson." It is the same object
# viewed from two perspectives:
#   - From inside the crystal: it's a lattice vibration (Digamma-mode)
#   - From outside (4D observer): it's a massive KK gauge boson
#
# The polariton picture requires TWO DISTINCT modes crossing. Let us examine
# all possible pairings.

print("--- SECTION 3: POLARITON ANALYSIS ---")
print()

# =============================================================================
# SECTION 3: COUPLED OSCILLATOR HAMILTONIAN
# =============================================================================

# Case A: B2 gap-edge (omega = 0.845) hybridizing with B1 (omega = 0.819)
# These are the two closest-lying modes.
# Coupling: V(B2, B1) = 0.080 (from the Kosmann connection matrix)

g_B2_B1 = V_8x8[0, 4]  # = 0.0799 M_KK (uniform across all 4 B2 modes)
detuning_B2_B1 = omega_B2_sp - omega_B1_sp

print("Case A: B2 -- B1 hybridization (gap-edge pair)")
print(f"  omega_B2 = {omega_B2_sp:.6f} M_KK")
print(f"  omega_B1 = {omega_B1_sp:.6f} M_KK")
print(f"  detuning = {detuning_B2_B1:.6f} M_KK")
print(f"  coupling g = V(B2,B1) = {g_B2_B1:.6f} M_KK")
print()

H_A = np.array([[omega_B2_sp, g_B2_B1],
                 [g_B2_B1, omega_B1_sp]])
evals_A = eigvalsh(H_A)
Delta_pol_A = evals_A[1] - evals_A[0]

print(f"  2x2 Hamiltonian eigenvalues: {evals_A[0]:.6f}, {evals_A[1]:.6f}")
print(f"  Polariton gap: Delta_pol = {Delta_pol_A:.6f} M_KK")
print(f"  Analytic check: sqrt(delta^2 + 4g^2) = {np.sqrt(detuning_B2_B1**2 + 4*g_B2_B1**2):.6f}")
print(f"  Gap / M_KK = {Delta_pol_A:.4f}")
print()

# Mixing angle
theta_A = 0.5 * np.arctan2(2 * g_B2_B1, omega_B2_sp - omega_B1_sp)
print(f"  Mixing angle: theta = {np.degrees(theta_A):.2f} deg")
print(f"  B2 content of lower polariton: cos^2(theta) = {np.cos(theta_A)**2:.4f}")
print(f"  B1 content of lower polariton: sin^2(theta) = {np.sin(theta_A)**2:.4f}")
print()

# Case B: B2 gap-edge (0.845) hybridizing with B3 (0.978)
g_B2_B3_avg = np.mean(np.abs(V_8x8[0:4, 5:8]))
detuning_B2_B3 = omega_B3_sp - omega_B2_sp

print("Case B: B2 -- B3 hybridization")
print(f"  omega_B2 = {omega_B2_sp:.6f} M_KK")
print(f"  omega_B3 = {omega_B3_sp:.6f} M_KK")
print(f"  detuning = {detuning_B2_B3:.6f} M_KK")
print(f"  coupling g = <|V(B2,B3)|> = {g_B2_B3_avg:.6f} M_KK")
print()

H_B = np.array([[omega_B2_sp, g_B2_B3_avg],
                 [g_B2_B3_avg, omega_B3_sp]])
evals_B = eigvalsh(H_B)
Delta_pol_B = evals_B[1] - evals_B[0]

print(f"  2x2 eigenvalues: {evals_B[0]:.6f}, {evals_B[1]:.6f}")
print(f"  Polariton gap: Delta_pol = {Delta_pol_B:.6f} M_KK")
print(f"  Gap / M_KK = {Delta_pol_B:.4f}")
print()

theta_B = 0.5 * np.arctan2(2 * g_B2_B3_avg, omega_B3_sp - omega_B2_sp)
print(f"  Mixing angle: theta = {np.degrees(theta_B):.2f} deg")
print()

# Case C: Full 8x8 hybridization (ALL branches coupled)
print("Case C: Full 8-mode hybridization (all branches)")

H_full = np.diag(E_8) + V_8x8
evals_full = eigvalsh(H_full)

print(f"  Bare energies:     {E_8}")
print(f"  Dressed energies:  {evals_full}")
print(f"  Shifts (dressed - bare):")
for i, (l, e_bare, e_dressed) in enumerate(zip(branch_labels, np.sort(E_8), evals_full)):
    print(f"    mode {i}: {e_bare:.6f} -> {e_dressed:.6f}  (shift = {e_dressed - e_bare:+.6f})")
print()

# The polariton gap in the full problem
gaps_full = np.diff(evals_full)
print(f"  Level spacings: {gaps_full}")
print(f"  Min gap: {np.min(gaps_full):.6f} M_KK between modes {np.argmin(gaps_full)} and {np.argmin(gaps_full)+1}")
print()

# =============================================================================
# SECTION 4: THE PHYSICAL POLARITON PICTURE
# =============================================================================

print("--- SECTION 4: PHYSICAL POLARITON ANALYSIS ---")
print()

# The polariton picture requires distinguishing the "phonon" branch from the
# "photon" branch. In condensed matter:
#   - Photon: omega = c*k (linear dispersion, massless)
#   - Phonon: omega = omega_TO (flat, dispersionless for optical modes)
# The polariton = anticrossing of these two branches.
#
# In the SU(3) phononic crystal:
#   - The "photon" is the 4D gauge boson. In 4D, it has omega = c*|k|.
#     After KK reduction, the first KK mode has mass omega = M_KK * lambda_min
#     where lambda_min is the smallest positive D_K eigenvalue.
#     The KK gauge boson dispersion in 4D is:
#       omega^2 = k^2 + m_KK_gauge^2  (massive Klein-Gordon)
#     where m_KK_gauge = lambda_min * M_KK in physical units.
#
#   - The "phonon" is the B2 collective mode (GPV or QRPA giant resonance).
#     The GPV at omega = 0.792 M_KK is a pair vibration mode.
#     The QRPA giant resonance at omega = 3.245 M_KK carries 97.5% EWSR.
#
# Key distinction: The B2 single-particle mode at 0.845 M_KK IS a KK mode.
# It is NOT a separate entity from the gauge boson. It IS the gauge boson
# mass in the KK sense. You cannot form a polariton of something with itself.
#
# The COLLECTIVE modes (GPV at 0.792, QRPA giant at 3.245) ARE distinct from
# the single-particle KK modes. They are many-body excitations (coherent
# superpositions of particle-hole pairs) that can in principle hybridize with
# the single-particle KK gauge bosons.

print("Physical distinction:")
print("  Single-particle KK modes (B1=0.819, B2=0.845, B3=0.978) ARE gauge boson masses.")
print("  Collective modes (GPV=0.792, Giant=3.245) are many-body excitations.")
print("  Polariton = collective mode hybridizing with single-particle KK mode.")
print()

# Case D: GPV (omega=0.792) hybridizing with B2 gap-edge (omega=0.845)
# This is the PHYSICALLY CORRECT polariton picture:
# the pair vibration (collective phonon) crossing the KK gauge boson mass.
#
# What is the coupling? The GPV is a coherent superposition of particle-hole
# excitations: |GPV> = sum_k X_k a_k^dag b_k^dag |BCS>
# The coupling to the single-particle mode is through the residual interaction V_rem.
# From S40: V_rem has eigenvalues spanning [-1.06, +1.05], with var_rem = 0.119.
# The effective coupling is the matrix element <GPV|V|single-particle>.
#
# From QRPA theory, the GPV couples to the single-particle continuum through
# the B matrix: B_{kk'} = -Delta_k * V_{kk'} * Delta_{k'} / (4 * E_k * E_k').
# The GPV's coherence factor sqrt(strength/EWSR) gives the effective coupling.
#
# The relevant coupling for GPV-gauge hybridization is NOT the V matrix
# (which couples single-particle states). It is the matrix element of the
# gauge interaction between the collective GPV mode and the gauge boson.
#
# In the NCG framework, the gauge coupling is determined by the spectral action:
#   L_gauge = -(1/4) f_4 * F_mu_nu F^mu_nu
# where f_4 = a_4 / M_KK^4. The gauge boson mass comes from the Higgs mechanism
# (the finite spectral triple's D_F), not from KK.
#
# CRITICAL POINT: In Connes' NCG Standard Model, the Higgs is NOT a KK mode.
# It is a component of the generalized connection on the finite spectral triple.
# The Higgs mass is set by the quartic coupling and the vev, both determined
# by the spectral action coefficients a_0, a_2, a_4.
# See Chamseddine-Connes 2007: m_H^2 = (2*a_0*lambda) / (pi^2*f_0) at tree level.
#
# The polariton picture therefore requires:
#   1. A "phonon" = collective B2 mode (GPV or QRPA giant)
#   2. A "photon" = 4D gauge boson (massless before EWSB)
#   3. Their hybridization = the NCG Higgs mechanism
#
# Let's compute this properly.

# The coupling between the GPV and the gauge sector is through the spectral
# action. The relevant matrix element is:
#   g_pol = <GPV| D_K |gauge> = sum_k X_k * <k|D_K|gauge>
# where X_k are the QRPA amplitudes.
#
# From S40 QRPA: the dominant QRPA mode has X_k proportional to v_dom.
# The transition strength S = sum_k X_k^2 ~ 2.93 (97.5% EWSR).
# But X_k describes particle-hole excitations WITHIN the internal space.
# The coupling to the 4D gauge boson requires a vertex connecting the
# internal collective mode to the 4D photon propagator.
#
# In the phononic crystal language: this is the IR activity of the optical mode.
# A phonon couples to photons only if it carries a dipole moment (IR-active).
# The B2 mode's "IR activity" is its projection onto the gauge generators.
# From S34: [iK_7, D_K] = 0 — Jensen preserves U(1)_7.
# B2 modes carry K_7 charge. They couple to the U(1)_7 gauge boson.
#
# The coupling strength is set by the gauge coupling constant:
#   g_gauge = g_2 (SU(2) coupling) or g_1 (U(1) coupling)
# In M_KK units, these are O(1) numbers (from the spectral action):
#   g_2^2 = pi^2 / (2 * a_4)
# where a_4 = 2/5 * F/B * N_gen = 2/5 * 0.55 * 3 = 0.66 (from the F/B ratio)
#
# Actually, let me compute this more carefully using the established framework.

# From S33a: a_4(K) = 0 at the Einstein (bi-invariant) point.
# At Jensen deformation tau = 0.190: a_4(K) != 0.
# The gauge kinetic term EMERGES from the Jensen deformation.
# g^2 = 1 / a_4(K,tau), which varies with tau.
#
# For the polariton coupling, what matters is the vertex connecting the
# collective phonon to two gauge bosons (or one gauge boson in the case
# of a linear coupling). The relevant quantity is:
#
#   g_polariton = g_gauge * <B2_collective|Q|0>
#
# where Q is the charge operator (generator of the gauge group) and
# <B2_collective|Q|0> is the transition matrix element.

# From the QRPA, the transition matrix element for the giant resonance is:
#   B(GT) = sqrt(S / (2*omega)) where S is the strength and omega the frequency
# For B2 giant resonance: S = 2.929, omega = 3.245
B_transition = np.sqrt(S_giant / (2 * omega_giant))
print(f"B2 giant resonance transition amplitude: {B_transition:.6f}")

# For the GPV:
B_gpv = np.sqrt(0.136 / (2 * 0.792))  # strength 0.136 (from B1-like lowest mode)
# Actually, the GPV at 0.792 is the pair vibration mode from S37/S38.
# It carries pair-addition strength, not single-particle transition strength.
# Its coupling to gauge bosons requires pair creation/annihilation, which is
# a SECOND-ORDER process (two gauge bosons -> pair). The effective coupling is:
#   g_GPV_gauge ~ g_gauge^2 * <GPV|Q^2|0> / omega_GPV
# This is parametrically smaller than the single-particle coupling by g_gauge.

print()
print("--- SECTION 5: QUANTITATIVE POLARITON GAPS ---")
print()

# Let us now compute ALL polariton gaps systematically.
# The coupling g in the 2x2 Hamiltonian:
#   H = [[omega_1, g], [g, omega_2]]
# has eigenvalues omega_pm = (omega_1 + omega_2)/2 +/- sqrt((omega_1-omega_2)^2/4 + g^2)
# The polariton gap = omega_+ - omega_- = sqrt(delta^2 + 4*g^2)
# where delta = omega_1 - omega_2.

# At the exact crossing point (delta = 0), the gap = 2*g.
# This is the MINIMUM gap. For a polariton to exist, we need the two branches
# to actually cross when the coupling is turned off. If they don't cross,
# there is no avoided crossing — just perturbative level repulsion.

# Case 1: B2 sp (0.845) vs B1 sp (0.819)
# These don't cross (they're at fixed energies). But the coupling mixes them.
delta_1 = omega_B2_sp - omega_B1_sp
g_1 = g_B2_B1  # = 0.0799
gap_1 = np.sqrt(delta_1**2 + 4*g_1**2)
print(f"Case 1: B2_sp (0.845) -- B1_sp (0.819)")
print(f"  detuning delta = {delta_1:.6f}")
print(f"  coupling g = {g_1:.6f}")
print(f"  gap = sqrt(delta^2 + 4g^2) = {gap_1:.6f} M_KK")
print(f"  gap/M_KK = {gap_1:.4f}")
print(f"  2g (resonant gap) = {2*g_1:.6f}")
print()

# Case 2: B2 sp (0.845) vs B3 sp (0.978)
delta_2 = omega_B3_sp - omega_B2_sp
g_2 = g_B2_B3_avg
gap_2 = np.sqrt(delta_2**2 + 4*g_2**2)
print(f"Case 2: B2_sp (0.845) -- B3_sp (0.978)")
print(f"  detuning delta = {delta_2:.6f}")
print(f"  coupling g = {g_2:.6f}")
print(f"  gap = {gap_2:.6f} M_KK")
print(f"  gap/M_KK = {gap_2:.4f}")
print()

# Case 3: GPV (0.792) vs B2 sp (0.845) — collective-single hybridization
# The coupling for this case is NOT V(B2,B1). The GPV is a pair vibration
# (Delta N = +/-2). Its coupling to single-particle modes is through the
# anomalous density <a_k a_{-k}> which is the v_k*u_k coherence factor.
# The effective coupling:
#   g_GPV_sp ~ sum_k u_k v_k * V_{kk'} ~ Delta_BCS * <V> / (2*E_qp)
# where Delta_BCS is the BCS gap.
# From S36: E_cond = -0.137, which gives Delta_BCS ~ sqrt(2*|E_cond|/N_eff) ~ 0.23
# From the v_k values: max v_k for B2 is ~0.49, u_k ~ 0.87
# Product u*v ~ 0.43 for B2 modes

uv_B2 = np.mean(u_k[0:4] * v_k[0:4])
g_GPV_sp = uv_B2 * np.mean(np.abs(V_8x8[0:4, 0:4]))  # within-B2 coupling
delta_3 = omega_B2_sp - omega_gpv
gap_3 = np.sqrt(delta_3**2 + 4*g_GPV_sp**2)

print(f"Case 3: GPV (0.792) -- B2_sp (0.845)")
print(f"  detuning delta = {delta_3:.6f}")
print(f"  <u*v>_B2 = {uv_B2:.6f}")
print(f"  effective coupling g = <uv> * <|V_B2|> = {g_GPV_sp:.6f}")
print(f"  gap = {gap_3:.6f} M_KK")
print(f"  gap/M_KK = {gap_3:.4f}")
print()

# Case 4: GPV (0.792) vs B1 sp (0.819)
delta_4 = omega_B1_sp - omega_gpv
g_GPV_B1 = np.mean(u_k[0:4] * v_k[0:4]) * g_B2_B1  # GPV (B2-character) coupling to B1
gap_4 = np.sqrt(delta_4**2 + 4*g_GPV_B1**2)

print(f"Case 4: GPV (0.792) -- B1_sp (0.819)")
print(f"  detuning delta = {delta_4:.6f}")
print(f"  coupling g = {g_GPV_B1:.6f}")
print(f"  gap = {gap_4:.6f} M_KK")
print(f"  gap/M_KK = {gap_4:.4f}")
print()

# Case 5: QRPA giant (3.245) vs 2*B2 quasiparticle threshold (2*1.623 = 3.246)
# This is the near-resonance identified in S40: omega_B2_coll ~ 2*omega_B1
# The 3-phonon decay channel.
delta_5 = omega_giant - 2*omega_B1_qp  # B1 threshold
threshold_B2 = 2 * omega_B2_qp
delta_5b = omega_giant - threshold_B2

print(f"Case 5: Giant resonance (3.245) near thresholds")
print(f"  omega_giant = {omega_giant:.6f}")
print(f"  2*E_qp(B1) = {2*omega_B1_qp:.6f}  (detuning = {omega_giant - 2*omega_B1_qp:.6f})")
print(f"  2*E_qp(B2) = {2*omega_B2_qp:.6f}  (detuning = {omega_giant - 2*omega_B2_qp:.6f})")
print(f"  The giant resonance sits BETWEEN the B1 and B2 pair-breaking thresholds")
print()

# =============================================================================
# SECTION 6: DISPERSION RELATION omega_pm(k)
# =============================================================================

print("--- SECTION 6: POLARITON DISPERSION RELATION ---")
print()

# For a phonon-polariton, the dispersion is:
#   omega^2 = (omega_phonon^2 + c^2*k^2)/2 +/- sqrt((omega_phonon^2 - c^2*k^2)^2/4 + g_eff^2*c^2*k^2)
#
# But our system has massive modes (not photons with omega = c*k).
# The "photon" here is a massive KK gauge boson:
#   omega_gauge^2 = m_gauge^2 + k^2  (in M_KK units, c=1)
# where m_gauge is set by the D_K eigenvalue.
#
# The "phonon" is the B2 collective mode:
#   omega_B2 = const (dispersionless in the flat-band limit)
#
# For the flat-band B2 coupled to a massive KK gauge boson (B1 or B3):
#   H(k) = [[omega_B2, g], [g, sqrt(m_gauge^2 + k^2)]]
#
# This is a k-dependent 2x2 problem.
# At k=0: just the cases computed above.
# At large k: omega_gauge >> omega_B2, so no crossing. The upper branch
#   follows the gauge boson, the lower stays at omega_B2.
#
# The interesting regime is near k* where omega_gauge(k*) = omega_B2:
#   k* = sqrt(omega_B2^2 - m_gauge^2)
# For B2 (0.845) vs B1 (0.819): k* = sqrt(0.845^2 - 0.819^2) = sqrt(0.044) = 0.209
# For B2 (0.845) vs B3 (0.978): omega_B2 < m_B3, so they NEVER cross.

# B2 vs B1 crossing:
k_star_B1 = np.sqrt(max(0, omega_B2_sp**2 - omega_B1_sp**2))
print(f"B2-B1 crossing momentum: k* = {k_star_B1:.6f} M_KK")
print(f"  At k*, both modes have omega = {omega_B2_sp:.6f} M_KK")
print(f"  Anticrossing gap at k* = 2*g = {2*g_B2_B1:.6f} M_KK")
print()

# Compute the full dispersion
k_vals = np.linspace(0, 0.6, 500)

# B2 flat band: omega = omega_B2_sp (constant)
omega_B2_branch = omega_B2_sp * np.ones_like(k_vals)

# B1 massive gauge: omega = sqrt(m_B1^2 + k^2)
omega_B1_k = np.sqrt(omega_B1_sp**2 + k_vals**2)

# B3 massive gauge: omega = sqrt(m_B3^2 + k^2)
omega_B3_k = np.sqrt(omega_B3_sp**2 + k_vals**2)

# Polariton branches for B2-B1 coupling
omega_plus_B1 = np.zeros_like(k_vals)
omega_minus_B1 = np.zeros_like(k_vals)
mixing_angle_B1 = np.zeros_like(k_vals)

for i, k in enumerate(k_vals):
    H_k = np.array([[omega_B2_sp, g_B2_B1],
                     [g_B2_B1, np.sqrt(omega_B1_sp**2 + k**2)]])
    evals = eigvalsh(H_k)
    omega_minus_B1[i] = evals[0]
    omega_plus_B1[i] = evals[1]
    # Mixing angle
    delta_k = omega_B2_sp - np.sqrt(omega_B1_sp**2 + k**2)
    mixing_angle_B1[i] = 0.5 * np.arctan2(2*g_B2_B1, delta_k)

# Find minimum gap
min_gap_idx = np.argmin(omega_plus_B1 - omega_minus_B1)
min_gap = omega_plus_B1[min_gap_idx] - omega_minus_B1[min_gap_idx]
k_min_gap = k_vals[min_gap_idx]

print(f"Polariton dispersion (B2 flat band + B1 dispersive):")
print(f"  Minimum gap = {min_gap:.6f} M_KK at k = {k_min_gap:.4f}")
print(f"  2*g = {2*g_B2_B1:.6f} M_KK (expected at crossing)")
print(f"  Gap / M_KK = {min_gap:.4f}")
print()

# Polariton branches for B2-B3 coupling
omega_plus_B3 = np.zeros_like(k_vals)
omega_minus_B3 = np.zeros_like(k_vals)

for i, k in enumerate(k_vals):
    H_k = np.array([[omega_B2_sp, g_B2_B3_avg],
                     [g_B2_B3_avg, np.sqrt(omega_B3_sp**2 + k**2)]])
    evals = eigvalsh(H_k)
    omega_minus_B3[i] = evals[0]
    omega_plus_B3[i] = evals[1]

# B2-B3 never cross (omega_B2 < omega_B3 at all k), so the "gap" is just
# the level repulsion at k=0:
gap_B3_k0 = omega_plus_B3[0] - omega_minus_B3[0]
print(f"B2-B3 level spacing at k=0: {gap_B3_k0:.6f} M_KK (no crossing)")
print()

# =============================================================================
# SECTION 7: COMPARISON TO HIGGS MASS
# =============================================================================

print("--- SECTION 7: HIGGS MASS COMPARISON ---")
print()

m_Higgs = 125.1  # GeV
M_KK_gravity = 7.43e16  # GeV (from W4-2)
M_KK_gauge = 5.04e17    # GeV (from W4-2)

ratio_grav = m_Higgs / M_KK_gravity
ratio_gauge = m_Higgs / M_KK_gauge

print(f"m_Higgs = {m_Higgs} GeV")
print(f"M_KK (gravity route) = {M_KK_gravity:.2e} GeV")
print(f"M_KK (gauge route) = {M_KK_gauge:.2e} GeV")
print(f"m_Higgs / M_KK (gravity) = {ratio_grav:.2e}")
print(f"m_Higgs / M_KK (gauge)   = {ratio_gauge:.2e}")
print()

# Our computed polariton gaps:
print("Computed polariton gaps vs required Higgs ratio:")
print(f"  Case 1 (B2-B1 sp):    Delta_pol/M_KK = {gap_1:.4f}  (need {ratio_grav:.2e})")
print(f"  Case 2 (B2-B3 sp):    Delta_pol/M_KK = {gap_2:.4f}  (need {ratio_grav:.2e})")
print(f"  Case 3 (GPV-B2 sp):   Delta_pol/M_KK = {gap_3:.4f}  (need {ratio_grav:.2e})")
print(f"  Case 4 (GPV-B1 sp):   Delta_pol/M_KK = {gap_4:.4f}  (need {ratio_grav:.2e})")
print(f"  Case 5 (B2-B1 disp):  Delta_pol/M_KK = {min_gap:.4f} (need {ratio_grav:.2e})")
print()

# The gap ratios:
print("Hierarchy check (all gaps in M_KK units):")
for name, gap in [("B2-B1 sp", gap_1), ("B2-B3 sp", gap_2),
                   ("GPV-B2", gap_3), ("GPV-B1", gap_4),
                   ("B2-B1 disp", min_gap)]:
    excess = gap / ratio_grav
    print(f"  {name:15s}: {gap:.6f} = {excess:.2e} x (m_H/M_KK)")

print()

# =============================================================================
# SECTION 8: STRUCTURAL ANALYSIS — WHY THE GAP IS O(1)
# =============================================================================

print("--- SECTION 8: STRUCTURAL ANALYSIS ---")
print()

print("The polariton gap is O(0.1) M_KK in ALL cases.")
print("This is O(10^{14-15}) times larger than the required Higgs mass.")
print()
print("Structural reason: the coupling g = V(B2,B1) = 0.080 M_KK is an")
print("O(1) quantity in M_KK units. The detuning delta = 0.026 M_KK is also O(1).")
print("Therefore the polariton gap = sqrt(delta^2 + 4g^2) is necessarily O(1).")
print()
print("This is the PHONONIC HIERARCHY PROBLEM:")
print("  In a phononic crystal, ALL energy scales are O(M_KK).")
print("  The couplings, detunings, and gaps are all set by the Dirac spectrum")
print("  of D_K, which has eigenvalues O(1) in M_KK units.")
print("  There is no mechanism within the single-crystal internal space to")
print("  produce a hierarchically small energy scale.")
print()
print("The actual Higgs mass in the NCG Standard Model comes from a DIFFERENT")
print("mechanism: the spectral action's coefficients a_0, a_2, a_4 involve")
print("SUMS over the Dirac spectrum up to a cutoff Lambda. The Higgs quartic")
print("and mass-squared parameter emerge from the FULL spectral action, not")
print("from a simple 2x2 anticrossing.")
print()
print("The polariton picture is a QUALITATIVE ANALOGY, not a quantitative")
print("mechanism for the Higgs mass. The actual mechanism is the spectral")
print("action with its cutoff-dependent coefficients.")

# =============================================================================
# SECTION 9: GATE VERDICT
# =============================================================================

print()
print("=" * 72)
print("GATE VERDICT: POLARITON-42")
print("=" * 72)
print()

# Pre-registered criteria:
# PASS: Delta_pol < 0.01 M_KK
# FAIL: Delta_pol > 0.1 M_KK

# The minimum polariton gap across all cases:
all_gaps = {
    'B2-B1 single-particle': gap_1,
    'B2-B3 single-particle': gap_2,
    'GPV-B2 single-particle': gap_3,
    'GPV-B1 single-particle': gap_4,
    'B2-B1 dispersive (min)': min_gap,
}

min_gap_name = min(all_gaps, key=all_gaps.get)
min_gap_val = all_gaps[min_gap_name]

print(f"Minimum polariton gap: {min_gap_val:.6f} M_KK ({min_gap_name})")
print()

if min_gap_val < 0.01:
    verdict = "PASS"
    print("VERDICT: PASS — polariton gap is hierarchically small")
elif min_gap_val > 0.1:
    verdict = "FAIL"
    print(f"VERDICT: FAIL — polariton gap = {min_gap_val:.4f} M_KK > 0.1 M_KK")
    print("  All gaps are O(0.1) M_KK. No hierarchy from hybridization.")
    print("  The polariton mechanism does NOT produce the Higgs mass hierarchy.")
else:
    verdict = "INTERMEDIATE"
    print(f"VERDICT: INTERMEDIATE — 0.01 < {min_gap_val:.4f} < 0.1")

print()
print(f"  Smallest gap: {min_gap_val:.6f} M_KK = {min_gap_val * M_KK_gravity:.2e} GeV")
print(f"  Required: m_Higgs = 125.1 GeV = {ratio_grav:.2e} M_KK")
print(f"  Ratio: gap / m_Higgs = {min_gap_val / ratio_grav:.2e}")
print()
print("PHYSICAL INTERPRETATION:")
print("  The polariton gap is determined by the Kosmann coupling matrix V,")
print("  which has entries O(0.01-0.08) M_KK. These are O(1) numbers on the")
print("  natural KK scale. The gap cannot be hierarchically small because")
print("  ALL internal-space energy scales are O(M_KK).")
print()
print("  The Higgs mass in the NCG Standard Model arises from the spectral")
print("  action coefficients (Chamseddine-Connes), not from a polariton")
print("  anticrossing. The polariton analogy is useful for intuition about")
print("  mode hybridization but does not explain the hierarchy.")
print()
print("INFO: Polariton dispersion and mixing angle reported in plot and data files.")

# =============================================================================
# SECTION 10: SAVE DATA
# =============================================================================

np.savez(os.path.join(base_dir, 's42_polariton.npz'),
    # Gate verdict
    gate_verdict=verdict,

    # Mode energies
    omega_B2_sp=omega_B2_sp,
    omega_B1_sp=omega_B1_sp,
    omega_B3_sp=omega_B3_sp,
    omega_gpv=omega_gpv,
    omega_giant=omega_giant,
    omega_B2_qp=omega_B2_qp,
    omega_B1_qp=omega_B1_qp,
    omega_B3_qp=omega_B3_qp,

    # Couplings
    g_B2_B1=g_B2_B1,
    g_B2_B3_avg=g_B2_B3_avg,
    g_GPV_sp=g_GPV_sp,
    g_GPV_B1=g_GPV_B1,

    # Polariton gaps
    gap_B2_B1_sp=gap_1,
    gap_B2_B3_sp=gap_2,
    gap_GPV_B2=gap_3,
    gap_GPV_B1=gap_4,
    gap_B2_B1_disp=min_gap,
    min_gap=min_gap_val,
    min_gap_name=min_gap_name,

    # Mixing angles
    theta_B2_B1=theta_A,
    theta_B2_B3=theta_B,

    # Dispersion
    k_vals=k_vals,
    omega_B2_branch=omega_B2_branch,
    omega_B1_k=omega_B1_k,
    omega_B3_k=omega_B3_k,
    omega_plus_B1=omega_plus_B1,
    omega_minus_B1=omega_minus_B1,
    omega_plus_B3=omega_plus_B3,
    omega_minus_B3=omega_minus_B3,
    mixing_angle_B1=mixing_angle_B1,
    k_star_B1=k_star_B1,

    # Full 8x8
    H_full_evals=evals_full,
    E_8_bare=E_8,

    # Transition amplitude
    B_transition_giant=B_transition,

    # Reference masses
    m_Higgs_GeV=m_Higgs,
    M_KK_gravity=M_KK_gravity,
    M_KK_gauge=M_KK_gauge,
    ratio_Higgs_MKK_grav=ratio_grav,
    ratio_Higgs_MKK_gauge=ratio_gauge,
)

print()
print(f"Data saved to: tier0-computation/s42_polariton.npz")

# =============================================================================
# SECTION 11: PLOT
# =============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel A: Polariton dispersion (B2 flat band + B1 dispersive)
ax = axes[0, 0]
ax.plot(k_vals, omega_B2_branch, 'b--', alpha=0.5, label=r'$\omega_{B2}$ (bare, flat)')
ax.plot(k_vals, omega_B1_k, 'r--', alpha=0.5, label=r'$\omega_{B1}(k) = \sqrt{m_{B1}^2 + k^2}$ (bare)')
ax.plot(k_vals, omega_plus_B1, 'k-', lw=2, label=r'$\omega_+$ (upper polariton)')
ax.plot(k_vals, omega_minus_B1, 'k-', lw=2, label=r'$\omega_-$ (lower polariton)')
ax.axvline(k_star_B1, color='gray', ls=':', alpha=0.5)
ax.annotate(f'anticrossing\n$k^* = {k_star_B1:.3f}$\n$\\Delta = {min_gap:.4f}\\,M_{{KK}}$',
            xy=(k_star_B1, omega_B2_sp), xytext=(k_star_B1 + 0.1, omega_B2_sp + 0.05),
            arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
ax.set_xlabel(r'$k$ [$M_{KK}$]')
ax.set_ylabel(r'$\omega$ [$M_{KK}$]')
ax.set_title('A: B2-B1 Polariton Dispersion')
ax.legend(fontsize=8)
ax.set_xlim(0, 0.5)
ax.set_ylim(0.78, 0.95)

# Panel B: Mixing angle vs k
ax = axes[0, 1]
ax.plot(k_vals, np.degrees(mixing_angle_B1), 'b-', lw=2)
ax.axhline(45, color='gray', ls=':', alpha=0.5)
ax.axvline(k_star_B1, color='gray', ls=':', alpha=0.5)
ax.set_xlabel(r'$k$ [$M_{KK}$]')
ax.set_ylabel(r'Mixing angle $\theta$ [degrees]')
ax.set_title('B: B2-B1 Mixing Angle')
ax.annotate(f'equal mixing\nat $k^* = {k_star_B1:.3f}$',
            xy=(k_star_B1, 45), xytext=(k_star_B1 + 0.1, 30),
            arrowprops=dict(arrowstyle='->', color='gray'), fontsize=9)
ax.set_xlim(0, 0.5)

# Panel C: All polariton gaps (bar chart)
ax = axes[1, 0]
gap_names = ['B2-B1\n(sp)', 'B2-B3\n(sp)', 'GPV-B2\n(sp)', 'GPV-B1\n(sp)', 'B2-B1\n(disp)']
gap_values = [gap_1, gap_2, gap_3, gap_4, min_gap]
colors = ['#cc3333' if g > 0.1 else '#33cc33' if g < 0.01 else '#cccc33' for g in gap_values]
bars = ax.bar(gap_names, gap_values, color=colors, edgecolor='black', linewidth=0.8)
ax.axhline(0.1, color='red', ls='--', label='FAIL threshold (0.1)')
ax.axhline(0.01, color='green', ls='--', label='PASS threshold (0.01)')
ax.axhline(ratio_grav, color='blue', ls=':', label=f'$m_H/M_{{KK}}$ = {ratio_grav:.1e}')
ax.set_ylabel(r'$\Delta_{\rm pol}$ [$M_{KK}$]')
ax.set_title(f'C: Polariton Gaps (VERDICT: {verdict})')
ax.set_yscale('log')
ax.set_ylim(1e-16, 1)
ax.legend(fontsize=7, loc='lower right')

# Panel D: Full 8-mode level diagram
ax = axes[1, 1]
# Bare levels
for i, (l, e) in enumerate(zip(branch_labels, E_8)):
    color = 'blue' if 'B2' in l else ('red' if 'B1' in l else 'green')
    ax.plot([0.7, 1.3], [e, e], color=color, lw=2, alpha=0.7)
    if i == 0:
        ax.text(0.5, e, l, fontsize=7, ha='right', va='center', color=color)
    elif 'B1' in l:
        ax.text(0.5, e, l, fontsize=7, ha='right', va='center', color=color)
    elif i == 5:
        ax.text(0.5, e, l, fontsize=7, ha='right', va='center', color=color)

# Dressed levels
for i, e in enumerate(evals_full):
    ax.plot([1.7, 2.3], [e, e], color='black', lw=2)
    ax.text(2.5, e, f'{e:.4f}', fontsize=7, ha='left', va='center')

# Connect with lines
for i in range(8):
    ax.plot([1.3, 1.7], [np.sort(E_8)[i], evals_full[i]], 'gray', ls=':', alpha=0.5)

ax.set_xlim(0, 3)
ax.set_ylabel(r'$\omega$ [$M_{KK}$]')
ax.set_title('D: 8-Mode Level Diagram (Bare vs Dressed)')
ax.set_xticks([1.0, 2.0])
ax.set_xticklabels(['Bare', 'Dressed'])

plt.suptitle(r'S42 W5-4: $\digamma$-Polariton Hybridization — POLARITON-42: ' + verdict,
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig(os.path.join(base_dir, 's42_polariton.png'), dpi=150, bbox_inches='tight')
print(f"Plot saved to: tier0-computation/s42_polariton.png")
print()
print("COMPUTATION COMPLETE.")
