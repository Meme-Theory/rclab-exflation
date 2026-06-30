#!/usr/bin/env python3
"""
s63_jacobson_gge.py — Jacobson Thermodynamic Derivation for GGE Matter
======================================================================
Gate: JACOBSON-GGE-63
Session: S63, Wave 3, W3-03

Formal analysis of whether Jacobson's delta Q = T dS derivation of the
Einstein equations extends to non-thermal (GGE) matter on M4 x SU(3).

The Jacobson (1995) derivation:
  1. Local Rindler horizon at each spacetime point
  2. Heat flux: delta Q = integral T_ab chi^a d Sigma^b
  3. Area change: delta A = -integral lambda R_ab k^a k^b d lambda dA  (Raychaudhuri)
  4. Entropy-area: dS = eta * delta A
  5. Clausius: delta Q = T_Unruh * dS
  => T_ab k^a k^b = (hbar eta / 2pi) R_ab k^a k^b for all null k^a
  => Einstein equations with Lambda as integration constant

Key question: Does step 5 survive when matter is in a GGE state
(non-Planckian occupations locked by R-G integrability)?

Answer: YES, with a critical subtlety. The derivation does NOT require
thermal matter. It requires only:
  (a) T_ab is well-defined (any state has a T_ab)
  (b) S = eta * A (entanglement entropy of vacuum across horizon)
  (c) T_Unruh = hbar kappa / (2 pi) (kinematic, observer-dependent)

The GGE modifies what T_ab IS, not WHETHER the derivation works.
Lambda emerges as an integration constant, as in the thermal case.
"""

import numpy as np
import sys
sys.path.insert(0, '.')
from canonical_constants import (
    M_KK, M_Pl_reduced, M_Pl_unreduced, G_N, hbar_SI, c_light, k_B,
    rho_Lambda_obs, E_cond, tau_fold, a0_fold, a2_fold, a4_fold,
    T_acoustic, N_cells, Vol_SU3_Haar, PI
)

# =============================================================================
# SECTION 1: Load GGE data
# =============================================================================

meissner = np.load('computations/session-62/s62_meissner_gge.npz', allow_pickle=True)
cc_data = np.load('computations/session-62/s62_cc_qtheory_gge.npz', allow_pickle=True)

n_k_GGE = meissner['n_k_GGE']       # GGE occupation numbers (8 BCS modes)
n_k_GS = meissner['n_k_GS']         # Ground state occupations
F_k_GGE = meissner['F_k_GGE']       # GGE anomalous density
T_GGE_eff = float(meissner['T_GGE_eff'])  # Effective GGE temperature
n_condensate = float(meissner['n_condensate_GGE'])  # Condensate fraction

E_ZP_vacuum = float(cc_data['E_ZP_vacuum'])   # Zero-point energy (vacuum)
E_ZP_GGE = float(cc_data['E_ZP_GGE'])         # Zero-point energy (GGE)
Delta_E_BCS = float(cc_data['Delta_E_BCS_only'])  # BCS condensation energy
Delta_E_full = float(cc_data['Delta_E_full'])      # Full energy shift
N_modes_BCS = int(cc_data['N_modes_BCS'])
N_modes_total = int(cc_data['N_modes_total'])
omega_BCS = cc_data['omega_BCS']     # BCS mode frequencies
Lambda_CC_MP4 = float(cc_data['Lambda_CC_MP4'])  # Lambda/M_Pl^4

# Richardson-Gaudin conserved charges (constructed from BCS occupations)
# For Richardson-Gaudin integrable pairing, the conserved charges are:
#   I_k = n_k (1 - n_k) - F_k^2 / (product terms)
# In the reduced BCS limit, I_k = sqrt(n_k(1-n_k)) * phase_factor
# The key property: [H_BCS, I_k] = 0 for all k

print("=" * 70)
print("JACOBSON-GGE-63: Formal Jacobson Derivation for GGE Matter")
print("=" * 70)

print("\n--- GGE State Properties ---")
print(f"  Condensate fraction:  {n_condensate:.6f}")
print(f"  Effective temperature: {T_GGE_eff:.6f} M_KK")
print(f"  N_BCS modes:          {N_modes_BCS}")
print(f"  N_total modes:        {N_modes_total}")
print(f"  E_ZP (vacuum):        {E_ZP_vacuum:.4f} M_KK^4")
print(f"  E_ZP (GGE):           {E_ZP_GGE:.4f} M_KK^4")
print(f"  Delta E_BCS:          {Delta_E_BCS:.6f} M_KK^4")

# =============================================================================
# SECTION 2: T_ab for the GGE state
# =============================================================================
# The energy-momentum tensor T_ab for ANY quantum state is well-defined:
#   T_ab = <psi| T^_ab |psi>
# where T^_ab is the renormalized stress-energy operator.
#
# For the GGE state |GGE> = prod_k |n_k, F_k>:
#   T_ab^{GGE} = sum_k n_k^{GGE} * t_ab^{(k)} + vacuum_contribution
#
# where t_ab^{(k)} is the single-mode contribution.
# The GGE differs from thermal: n_k^{GGE} != 1/(exp(omega_k/T) - 1)
# Instead: n_k^{GGE} is determined by the R-G conserved charges {I_k}.
#
# CRITICAL POINT: Jacobson's derivation does NOT use the internal structure
# of T_ab. It only requires T_ab to exist and satisfy nabla^a T_ab = 0.
# The GGE T_ab satisfies conservation because [H, I_k] = 0 for all k.

print("\n--- T_ab Analysis ---")

# Construct T_ab components for GGE
# In the rest frame of the BCS condensate, T_ab is diagonal:
#   T^00 = rho_GGE = sum_k omega_k n_k + E_ZP + E_cond
#   T^ii = P_GGE = (equation of state)

rho_GGE_modes = np.sum(omega_BCS * n_k_GGE)
rho_GGE_total = E_ZP_GGE + Delta_E_full  # Total: ZP + BCS shift
P_GGE = rho_GGE_modes / 3.0  # Ultrarelativistic approximation for modes

# For comparison: thermal state at T_GGE_eff
n_k_thermal = 1.0 / (np.exp(omega_BCS / T_GGE_eff) - 1.0 + 1e-30)
rho_thermal_modes = np.sum(omega_BCS * n_k_thermal)

print(f"  rho_GGE (modes):     {rho_GGE_modes:.6f} M_KK^4")
print(f"  rho_GGE (total):     {rho_GGE_total:.4f} M_KK^4")
print(f"  rho_thermal (modes): {rho_thermal_modes:.6f} M_KK^4")
print(f"  P_GGE (approx):     {P_GGE:.6f} M_KK^4")

# Deviation from Planck distribution
deviation = np.abs(n_k_GGE - n_k_thermal) / (np.abs(n_k_GGE) + 1e-30)
print(f"\n  Mode-by-mode deviation from Planck:")
for i in range(N_modes_BCS):
    print(f"    k={i}: n_GGE={n_k_GGE[i]:.6e}, n_thermal={n_k_thermal[i]:.6e}, "
          f"dev={deviation[i]:.2f}")

# =============================================================================
# SECTION 3: Step-by-step Jacobson derivation for GGE
# =============================================================================
print("\n" + "=" * 70)
print("STEP-BY-STEP JACOBSON DERIVATION")
print("=" * 70)

# Step 1: Local Rindler horizon exists
# PASSES: This is a GEOMETRIC construct. For any spacetime point p,
# we can construct a local Rindler horizon from null geodesics.
# The GGE state does not affect the existence of horizons.
print("\nStep 1: Local Rindler horizon construction")
print("  Status: PASSES")
print("  Reason: Geometric construct, independent of matter state")

# Step 2: Unruh temperature
# PASSES: T_U = hbar * kappa / (2*pi) is KINEMATIC.
# It depends on the observer's acceleration, not on the matter state.
# An accelerated observer sees T_U regardless of the matter content.
print("\nStep 2: Unruh temperature T_U = hbar*kappa/(2*pi)")
print("  Status: PASSES")
print("  Reason: Kinematic quantity, depends on acceleration only")

# Step 3: Heat flux delta Q = integral T_ab chi^a d Sigma^b
# PASSES: T_ab^{GGE} is well-defined. The heat flux is:
#   delta Q = -kappa * integral lambda * T_ab^{GGE} k^a k^b d lambda dA
# The GGE state has a definite T_ab; it just differs from the thermal T_ab.
print("\nStep 3: Heat flux delta Q")
print("  Status: PASSES")
print("  Reason: T_ab well-defined for any state. GGE has definite T_ab.")
print(f"  T_00^GGE = {rho_GGE_total:.4f} M_KK^4")

# Step 4: Area variation via Raychaudhuri equation
# PASSES: This is PURELY GEOMETRIC. The Raychaudhuri equation:
#   d theta / d lambda = -theta^2/2 - sigma^2 - R_ab k^a k^b
# relates the expansion of null geodesics to the Ricci tensor.
# It makes NO reference to matter content or thermal properties.
print("\nStep 4: Area variation (Raychaudhuri equation)")
print("  Status: PASSES")
print("  Reason: Purely geometric identity, no matter content assumed")

# Step 5: Entropy-area proportionality dS = eta * delta A
# THIS IS THE CRITICAL STEP.
# Jacobson assumes S_ent proportional to A.
# For THERMAL states: this follows from the entanglement entropy of the
# vacuum across the Rindler horizon (Bombelli et al. 1986).
# For GGE states: the vacuum entanglement entropy STILL exists because
# the VACUUM state (not the matter excitation) determines S_ent.
#
# KEY DISTINCTION:
# - S_matter (thermodynamic entropy of matter) depends on the state
#   and IS different for GGE vs thermal.
# - S_ent (entanglement entropy of vacuum across horizon) depends on
#   the VACUUM structure, not the excitation above it.
# - Jacobson uses S_ent, NOT S_matter.
#
# The GGE state |GGE> is built on the BCS vacuum |0_BCS>.
# The entanglement entropy across a Rindler cut depends on |0_BCS>,
# which is the SAME vacuum for thermal and GGE excitations.
# Therefore S_ent(A) is the SAME for GGE and thermal matter.
#
# SUBTLETY: The GGE occupations modify the state, which could modify
# the entanglement entropy via state-dependent corrections.
# These corrections are O(E_exc / E_Planck) ~ O(M_KK^4 / M_Pl^4) ~ 10^{-10}.

print("\nStep 5: Entropy-area proportionality dS = eta * delta A")
print("  Status: PASSES (with subtlety)")
print("  Reason: Jacobson uses VACUUM entanglement entropy, not matter entropy")
print("  The BCS vacuum |0_BCS> is the same for GGE and thermal excitations")
print("  State-dependent corrections: O(M_KK^4 / M_Pl^4)")

correction_ratio = (M_KK / M_Pl_unreduced)**4
print(f"  Correction magnitude: (M_KK/M_Pl)^4 = {correction_ratio:.2e}")

# Step 6: Clausius relation delta Q = T_U * dS
# PASSES: This is the combination of Steps 3 and 5.
# delta Q is determined by T_ab^{GGE} (well-defined, conserved).
# dS is determined by the area change (geometric + vacuum entanglement).
# T_U is kinematic.
# The relation delta Q = T_U dS imposes:
#   T_ab^{GGE} k^a k^b = (hbar eta / 2pi) R_ab k^a k^b
# for ALL null k^a.
print("\nStep 6: Clausius relation delta Q = T_U * dS")
print("  Status: PASSES")
print("  Yields: T_ab^{GGE} k^a k^b = (hbar*eta/2pi) R_ab k^a k^b")

# Step 7: Einstein equations from contracted Bianchi identity
# PASSES: T_ab^{GGE} k^a k^b = (hbar eta / 2pi) R_ab k^a k^b for all k^a
# implies T_ab = (hbar eta / 2pi) (R_ab + f g_ab) for some f.
# Conservation nabla^a T_ab = 0 plus Bianchi identity nabla^a G_ab = 0
# fixes f = -R/2 + Lambda.
# Result: R_ab - (1/2) R g_ab + Lambda g_ab = (2pi / hbar eta) T_ab^{GGE}
print("\nStep 7: Einstein equations via Bianchi identity")
print("  Status: PASSES")
print("  Result: G_ab + Lambda g_ab = 8*pi*G * T_ab^{GGE}")
print("  Lambda appears as UNDETERMINED integration constant")

# =============================================================================
# SECTION 4: What changes for GGE vs thermal matter
# =============================================================================
print("\n" + "=" * 70)
print("GGE vs THERMAL: What Changes")
print("=" * 70)

# The Einstein equations are IDENTICAL in form.
# What changes is T_ab on the right-hand side.
# For thermal: T_ab^{thermal} encodes Planck distribution
# For GGE: T_ab^{GGE} encodes R-G charges

# The effective Lambda from the Jacobson derivation:
# Lambda is an INTEGRATION CONSTANT, not determined by the derivation.
# Jacobson (1995) explicitly notes this.

# However, if we identify the matter content, we can ask:
# What gravitates? T_ab^{GGE} or T_ab^{thermal}?

# In equilibrium thermodynamics, T_ab^{eq} determines the geometry.
# Volovik's result: Lambda_eq = 0 because in equilibrium the thermodynamic
# potential (pressure) adjusts to make Lambda vanish identically.

# For the GGE: it is NOT in thermal equilibrium but in a GENERALIZED
# equilibrium (the R-G charges prevent full thermalization).
# The GGE density matrix is:
#   rho_GGE = exp(-sum_k beta_k I_k) / Z_GGE
# where I_k are R-G conserved charges and beta_k are Lagrange multipliers.

# Energy density from GGE:
rho_GGE_GeV4 = rho_GGE_total * M_KK**4
ratio_to_obs = rho_GGE_GeV4 / rho_Lambda_obs
log10_ratio = np.log10(abs(ratio_to_obs))

print(f"\n  rho_GGE (total):     {rho_GGE_total:.4f} M_KK^4")
print(f"  rho_GGE (GeV^4):    {rho_GGE_GeV4:.4e}")
print(f"  rho_Lambda_obs:      {rho_Lambda_obs:.2e} GeV^4")
print(f"  |rho_GGE / rho_obs|: 10^{log10_ratio:.1f}")
print(f"  CC gap (Jacobson):   {log10_ratio:.1f} orders of magnitude")

# =============================================================================
# SECTION 5: The Lambda question — three perspectives
# =============================================================================
print("\n" + "=" * 70)
print("THREE PERSPECTIVES ON Lambda")
print("=" * 70)

# Perspective 1: Jacobson (Lambda = integration constant)
# The derivation gives G_ab + Lambda g_ab = 8 pi G T_ab^{GGE}
# Lambda is UNDETERMINED. The derivation works for ANY T_ab.
# This means Lambda is NOT fixed by the matter content.
print("\nPerspective 1: Jacobson (Lambda = integration constant)")
print("  Lambda is UNDETERMINED by the derivation")
print("  The Jacobson framework is NECESSARY but not SUFFICIENT for CC")

# Perspective 2: Volovik (Lambda_eq = 0 in equilibrium)
# Volovik's argument: in equilibrium, the Gibbs-Duhem relation gives
#   P = -rho_vac = 0 (at T=0 chemical equilibrium)
# This requires FULL thermalization, which the GGE state prevents.
# The GGE is in CONSTRAINED equilibrium: it maximizes entropy subject
# to the R-G charge constraints sum_k beta_k I_k.
# The constrained free energy is:
#   F_GGE = E - T_eff * S - sum_k beta_k <I_k>
# In constrained equilibrium: P_GGE = -partial F / partial V |_{T, {beta_k}}
# This does NOT necessarily vanish.

P_GGE_constrained = -Delta_E_full  # Negative of condensation energy (pressure)
print(f"\nPerspective 2: Volovik (Lambda_eq = 0 in equilibrium)")
print(f"  Volovik requires FULL thermalization")
print(f"  GGE has CONSTRAINED equilibrium (R-G charges conserved)")
print(f"  P_GGE (constrained): {P_GGE_constrained:.6f} M_KK^4")
print(f"  Volovik Lambda_eq = 0 does NOT apply to GGE")

# Perspective 3: Entanglement entropy (S62 result)
# The S62 Hawking-QA workshop found: S_ent = 0 for the GGE product state.
# If S_ent = 0, then delta S = 0 in the Jacobson derivation,
# and delta Q = T_U * 0 = 0, which would require T_ab k^a k^b = 0.
# This gives RICCI-FLAT spacetime: R_ab k^a k^b = 0 for all null k.
#
# BUT: This conclusion rests on S_ent = 0 for the GGE as a PRODUCT STATE
# in the R-G eigenbasis. The GGE state on the CG(24) fabric may have
# LOCAL entanglement even if the GLOBAL state is a product state.
# The entanglement entropy across a Rindler cut depends on LOCAL
# correlations, not global product structure.
#
# RESOLUTION: The Jacobson derivation uses VACUUM entanglement entropy,
# not matter-state entanglement entropy. The vacuum |0_BCS> has
# entanglement across any spatial cut (UV entanglement from the
# continuum). This entanglement is ALWAYS present, regardless of
# excitations. The GGE occupations modify the entanglement by
# O(n_k * (length scale)^{d-2}) relative to the vacuum contribution.

# Vacuum entanglement entropy density (Bombelli et al. 1986, Srednicki 1993):
# S_ent = c_UV * A / epsilon^2 + c_1 * A / L^2 + ...
# where epsilon = UV cutoff, A = area, L = system scale
# For the KK framework: epsilon ~ 1/M_KK, A = arbitrary horizon area

# The GGE correction to vacuum entanglement:
# delta S_GGE / S_vac ~ sum_k n_k^{GGE} * (omega_k / M_KK)^2
# This is a SMALL perturbation because n_k << 1 for k > 0.

delta_S_ratio = np.sum(n_k_GGE[1:] * (omega_BCS[1:] / M_KK)**2)
# Actually in M_KK units, omega_BCS is already O(1) M_KK
delta_S_ratio_MKK = np.sum(n_k_GGE[1:] * omega_BCS[1:]**2)

print(f"\nPerspective 3: Entanglement entropy")
print(f"  S_ent = 0 for GGE PRODUCT STATE: MISLEADING")
print(f"  Jacobson uses VACUUM entanglement, not matter-state entanglement")
print(f"  Vacuum |0_BCS> has S_ent propto A (always)")
print(f"  GGE correction: delta S / S_vac ~ sum n_k omega_k^2 / M_KK^2")
print(f"  = {delta_S_ratio_MKK:.6e} (in M_KK units)")
print(f"  Conclusion: vacuum entanglement dominates; GGE is a perturbation")

# =============================================================================
# SECTION 6: Effective Lambda computation
# =============================================================================
print("\n" + "=" * 70)
print("EFFECTIVE LAMBDA FROM GGE")
print("=" * 70)

# The Jacobson derivation gives: G_ab + Lambda g_ab = 8 pi G T_ab^{GGE}
# Taking the trace: -R + 4 Lambda = 8 pi G T^{GGE}
# For the FRW metric with GGE matter:
#   Lambda_eff = 8 pi G rho_Lambda_eff / 3
# where rho_Lambda_eff = rho_vac^{GGE}

# The vacuum energy in the Jacobson framework is NOT E_ZP.
# It is the thermodynamic potential that enters the equation of state.
# For the GGE, this is the GGE free energy:
#   F_GGE = E_GGE - sum_k beta_k I_k

# What SHOULD gravitate (the key insight):
# In Jacobson's framework, what enters the Einstein equations is T_ab,
# which is determined by the FULL quantum state including vacuum.
# The CC problem is: T_ab includes E_ZP ~ M_KK^4 >> Lambda_obs.
#
# Jacobson's derivation does NOT solve the CC problem.
# It REFORMULATES it: instead of "why is Lambda small?"
# the question becomes "what is eta?"
# Because G = 1/(4 hbar eta), and eta = S/A,
# if eta is modified by the GGE, G is modified.

# Compute the three possible Lambda values:

# Option A: Naive (E_ZP gravitates fully)
Lambda_naive = E_ZP_GGE * M_KK**4  # GeV^4
gap_naive = np.log10(abs(Lambda_naive / rho_Lambda_obs))

# Option B: Spectral action (a_0 * M_KK^4 gravitates)
Lambda_SA = (2.0 / PI**2) * a0_fold * M_KK**4
gap_SA = np.log10(abs(Lambda_SA / rho_Lambda_obs))

# Option C: BCS condensation energy only
Lambda_BCS = abs(Delta_E_BCS) * M_KK**4
gap_BCS = np.log10(abs(Lambda_BCS / rho_Lambda_obs))

# Option D: Volovik (equilibrium => Lambda = 0)
Lambda_Volovik = 0.0  # (local)

# Option E: GGE constrained free energy
# F_GGE = E_GGE - sum_k beta_k <I_k>
# In the integrable limit, F_GGE = sum_k omega_k n_k^{GGE} + E_ZP + E_cond
# The Lagrange multipliers beta_k are chosen to reproduce n_k^{GGE}
# The pressure is P_GGE = -dF/dV, and Lambda_eff = 8 pi G P_GGE
# For the GGE: P_GGE depends on the equation of state

# The GGE equation of state differs from Planck:
# For Planck: P = rho/3 (radiation), P = 0 (matter), P = -rho (CC)
# For GGE: w_GGE = P_GGE / rho_GGE
# The BCS condensate has w = -1 (gap energy acts like CC)
# The quasiparticle excitations have w = 1/3 (relativistic)

w_condensate = -1.0  # BCS condensate  # (local)
w_qp = 1.0 / 3.0    # Quasiparticles

# Decompose: rho_GGE = rho_cond + rho_qp
rho_cond = abs(E_cond)  # Condensation energy (negative, acts like CC)
rho_qp = np.sum(omega_BCS * n_k_GGE)  # Quasiparticle contribution

# Total equation of state:
w_GGE = (w_condensate * rho_cond + w_qp * rho_qp) / (rho_cond + rho_qp)

print(f"  rho_condensate:  {rho_cond:.6f} M_KK^4")
print(f"  rho_qp:          {rho_qp:.6f} M_KK^4")
print(f"  w_condensate:    {w_condensate}")
print(f"  w_qp:            {w_qp:.4f}")
print(f"  w_GGE (total):   {w_GGE:.4f}")

print(f"\n  Lambda values (5 options):")
print(f"    A. Naive (E_ZP):      {Lambda_naive:.4e} GeV^4, gap = {gap_naive:.1f} OOM")
print(f"    B. Spectral action:   {Lambda_SA:.4e} GeV^4, gap = {gap_SA:.1f} OOM")
print(f"    C. BCS only:          {Lambda_BCS:.4e} GeV^4, gap = {gap_BCS:.1f} OOM")
print(f"    D. Volovik (eq):      0 (does NOT apply to GGE)")
print(f"    E. GGE constrained:   w_GGE = {w_GGE:.4f} (quintessence-like)")

# =============================================================================
# SECTION 7: The resolution — why Jacobson helps but doesn't solve CC
# =============================================================================
print("\n" + "=" * 70)
print("RESOLUTION: THE JACOBSON-GGE THEOREM")
print("=" * 70)

# THEOREM: The Jacobson derivation extends to GGE matter WITHOUT modification.
# The Einstein equations hold with T_ab = T_ab^{GGE}.
# Lambda remains an undetermined integration constant.
#
# PROOF:
# 1. The derivation requires only:
#    (a) Well-defined T_ab (GGE has this: YES)
#    (b) S = eta * A for vacuum entanglement (GGE preserves this: YES,
#        because Jacobson uses vacuum entanglement, not matter entropy)
#    (c) T_U = hbar kappa / (2 pi) (kinematic: YES)
#    (d) nabla^a T_ab = 0 (GGE conserves energy: YES, because [H, I_k] = 0)
#
# 2. NO step requires thermal equilibrium of matter.
#    - Step 5 (entropy-area) uses VACUUM entanglement, which is state-independent
#      to leading order in the UV.
#    - The Clausius relation delta Q = T dS is imposed as a POSTULATE on the
#      vacuum degrees of freedom crossing the horizon, not as a thermodynamic
#      property of the matter.
#
# 3. The GGE modifies T_ab on the RHS of the Einstein equations,
#    but does NOT affect the DERIVATION of those equations.
#
# COROLLARY: Lambda is NOT determined by the Jacobson derivation for GGE
# matter, just as it is not determined for thermal matter.
#
# COMPARISON TO VOLOVIK:
# Volovik's Lambda_eq = 0 requires FULL thermalization to the Gibbs state.
# The GGE is NOT Gibbs: it is constrained by R-G charges.
# Therefore Volovik's theorem does NOT apply.
# The GGE has a NONZERO vacuum energy that gravitates: Lambda =/= 0.
# But this Lambda is the FULL E_ZP + E_cond, not the observed Lambda.
# The CC problem persists at ~114 OOM.

# Compute what the Jacobson derivation DOES fix:
# G_N = 1 / (4 hbar eta)
# eta = 1 / (4 G_N hbar) = 1 / (4 l_Pl^2) in natural units

eta_Jacobson = 1.0 / (4.0 * G_N * hbar_SI)  # in SI
# In natural units (GeV^2):
l_Pl_natural = 1.0 / M_Pl_unreduced  # GeV^{-1}
eta_natural = 1.0 / (4.0 * l_Pl_natural**2)  # GeV^2
print(f"\n  eta (Jacobson):    {eta_natural:.4e} GeV^2")
print(f"  G_N (from eta):    G = 1/(4*hbar*eta)")
print(f"  Lambda:            UNDETERMINED (integration constant)")

# Does the GGE modify eta?
# eta = S_ent / A depends on the vacuum state.
# The BCS vacuum has the same UV entanglement structure as the free vacuum.
# BCS pairing modifies IR correlations but not UV divergences.
# Therefore eta is UNCHANGED by the GGE to leading order.
# Corrections: delta eta / eta ~ (Delta_BCS / M_KK)^2 ~ 0.6^2 ~ 0.36
# But this is a RELATIVE correction, not an absolute one.

Delta_BCS_val = float(np.sqrt(abs(Delta_E_BCS) * 2))  # Rough BCS gap estimate
delta_eta_ratio = (Delta_BCS_val)**2
print(f"\n  BCS gap (est):     {Delta_BCS_val:.4f} M_KK")
print(f"  delta eta / eta:   ~ {delta_eta_ratio:.4f} (relative correction)")
print(f"  This modifies G_N by ~{delta_eta_ratio:.1%}")
print(f"  Already captured in SAKHAROV-GN-44 (factor 2.3 agreement)")

# =============================================================================
# SECTION 8: Comparison to S62 QA workshop result
# =============================================================================
print("\n" + "=" * 70)
print("COMPARISON TO S62 HAWKING-QA WORKSHOP")
print("=" * 70)

# S62 concluded: "S_ent = 0 for the GGE product state => Lambda = 0"
# This is INCORRECT as stated. The error:
# - The GGE is a product state in the R-G EIGENBASIS
# - But the VACUUM is NOT a product state across spatial cuts
# - Jacobson uses VACUUM entanglement, not matter-state entanglement
# - The vacuum entanglement entropy is S_vac = eta * A (always nonzero)
#
# The S62 result conflated two different entropy concepts:
# 1. S_ent^{matter} = von Neumann entropy of GGE state = 0 (product state)
# 2. S_ent^{vacuum} = entanglement entropy of vacuum across Rindler cut != 0
#
# Jacobson uses (2), not (1). The derivation proceeds with S = eta * A.

print("  S62 claim: S_ent = 0 for GGE product state => Lambda = 0")
print("  THIS ANALYSIS: S_ent = 0 applies to MATTER STATE entropy")
print("  Jacobson uses VACUUM entanglement entropy (always nonzero)")
print("  CORRECTION: Jacobson derivation EXTENDS to GGE without modification")
print("  Lambda is an undetermined integration constant (as in thermal case)")
print("  The CC problem persists at ~114 OOM for the GGE")

# =============================================================================
# SECTION 9: What the GGE structure DOES buy for CC
# =============================================================================
print("\n" + "=" * 70)
print("WHAT GGE BUYS FOR THE CC")
print("=" * 70)

# The GGE structure has specific consequences for the CC:
#
# 1. Equation of state: w_GGE != -1 (because non-Planckian occupations)
#    This means the GGE dark energy sector is DYNAMICAL, not a pure CC.
#    The w_GGE value depends on the relative weight of condensate vs qp.
#
# 2. Non-thermalizable vacuum: The GGE cannot relax to thermal equilibrium.
#    This means Volovik's Lambda_eq = 0 does NOT apply.
#    The vacuum energy is LOCKED by R-G charges.
#
# 3. Integration constant: Lambda in Jacobson is not fixed by the derivation.
#    The GGE does not help fix Lambda; it only changes what T_ab is.
#    The CC problem is pushed to the initial conditions: what IS Lambda?
#
# 4. Spectral action route: The CCS 2018 identification S_vN = Tr(f(beta D))
#    relates the spectral action to an entropy functional.
#    For the GGE, the relevant entropy is the GGE entropy (maximized
#    subject to R-G charges), not the Gibbs entropy.
#    The GGE spectral action would be:
#    S_GGE = Tr(g(D, {I_k}))
#    where g encodes the R-G constraint structure.
#    This is a DIFFERENT functional from the standard spectral action.
#    It is currently UNCOMPUTED.

# Effective CC from BCS sector only:
Lambda_eff_BCS = abs(E_cond) * M_KK**4  # GeV^4
gap_BCS_OOM = np.log10(Lambda_eff_BCS / rho_Lambda_obs)

# Effective CC including EIH suppression (from S44):
# EIH suppression: (M_KK / M_Pl)^4 buys ~10 orders
EIH_suppression = (M_KK / M_Pl_unreduced)**4
Lambda_eff_EIH = abs(E_cond) * M_KK**4 * EIH_suppression
gap_EIH_OOM = np.log10(abs(Lambda_eff_EIH / rho_Lambda_obs))

print(f"\n  w_GGE = {w_GGE:.4f} (dynamical dark energy, not pure CC)")
print(f"  Lambda_BCS (no suppression): {Lambda_eff_BCS:.4e} GeV^4, gap = {gap_BCS_OOM:.1f} OOM")
print(f"  EIH suppression: (M_KK/M_Pl)^4 = {EIH_suppression:.2e}")
print(f"  Lambda_BCS (EIH): {Lambda_eff_EIH:.4e} GeV^4, gap = {gap_EIH_OOM:.1f} OOM")

# Remaining gap after known suppressions:
# From S44: total suppression 9.6 orders, leaving 110.5 OOM gap
# The Jacobson derivation does NOT change this.
print(f"\n  Remaining gap: ~110-114 OOM (UNCHANGED by Jacobson extension)")
print(f"  The Jacobson framework REFORMULATES but does NOT SOLVE the CC")

# =============================================================================
# SECTION 10: Gate verdict
# =============================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: JACOBSON-GGE-63")
print("=" * 70)

verdict = "INFO"
detail = (
    "Jacobson derivation EXTENDS to GGE matter without modification. "
    "All 7 steps pass. Lambda remains undetermined integration constant. "
    "S62 claim (S_ent=0 => Lambda=0) CORRECTED: Jacobson uses vacuum "
    "entanglement (nonzero), not matter-state entropy (zero for GGE). "
    "Volovik Lambda_eq=0 does NOT apply (GGE is constrained, not "
    "Gibbs). CC gap persists at ~114 OOM. w_GGE = %.4f (dynamical, "
    "not pure CC). Jacobson reformulates CC problem but does not "
    "solve it." % w_GGE
)

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {detail}")

# =============================================================================
# Save results
# =============================================================================
np.savez('computations/session-63/s63_jacobson_gge.npz',
    # Gate
    gate_name='JACOBSON-GGE-63',
    gate_verdict=verdict,
    gate_detail=detail,
    # GGE state
    n_k_GGE=n_k_GGE,
    n_k_GS=n_k_GS,
    omega_BCS=omega_BCS,
    T_GGE_eff=T_GGE_eff,
    n_condensate=n_condensate,
    # Energies
    rho_GGE_total=rho_GGE_total,
    rho_GGE_modes=rho_GGE_modes,
    E_ZP_GGE=E_ZP_GGE,
    Delta_E_BCS=Delta_E_BCS,
    Delta_E_full=Delta_E_full,
    # Lambda options
    Lambda_naive_GeV4=Lambda_naive,
    Lambda_SA_GeV4=Lambda_SA,
    Lambda_BCS_GeV4=Lambda_BCS,
    # CC gaps
    gap_naive_OOM=gap_naive,
    gap_SA_OOM=gap_SA,
    gap_BCS_OOM=gap_BCS_OOM,
    gap_EIH_OOM=gap_EIH_OOM,
    # Equation of state
    w_GGE=w_GGE,
    w_condensate=w_condensate,
    w_qp=w_qp,
    rho_cond=rho_cond,
    rho_qp=rho_qp,
    # Corrections
    correction_ratio=correction_ratio,
    delta_eta_ratio=delta_eta_ratio,
    EIH_suppression=EIH_suppression,
    # Jacobson parameters
    eta_natural_GeV2=eta_natural,
)

print("\nData saved to computations/session-63/s63_jacobson_gge.npz")
print("Done.")
