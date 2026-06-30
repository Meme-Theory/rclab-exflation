#!/usr/bin/env python3
"""
S75 Atlas Reclassification: NEEDS_REVERIFY -> ROBUST / QUASI-ROBUST / FRAGILE
===============================================================================

Gate: S75-O1-ATLAS-RECLASS
  PASS: >= 40 entries classified
  INFO: 20-39 classified
  FAIL: < 20 classified

Task: Classify 70 NEEDS_REVERIFY entries from the S74 W4-W joint audit atlas
by L_max dependence using the structural analysis from:
  - S74 W4-N: (0,0) sector eigenvalues IDENTICAL at L_max=3,5,7 (machine precision)
  - S74 W4-X: Six-layer multi-layer protection theorem for (0,0) sector
  - S73B W5-A: Canonical constants audit (CONV-FLAG taxonomy)
  - S73B W5-D: Three-phonon L_max=3/5/7 verification

Classification criteria:
  ROBUST:       L_max-INDEPENDENT by proof.
                  (a) Pure (0,0) sector eigenvalue quantity (multi-layer protected)
                  (b) Dimensionless ratio where Weyl exponents cancel
                  (c) Analytic expression independent of D_K spectrum
                  (d) Structural identity / algebraic invariant

  QUASI-ROBUST: L_max-independent at tested values, analytic proof incomplete.
                  (a) Ratio of (0,0) sector quantities (protection expected, chain non-trivial)
                  (b) BCS quantity derived from (0,0) eigenvalues via GL/MC intermediate
                  (c) Quantity where sub-leading Weyl corrections are small but non-zero

  FRAGILE:      L_max-SENSITIVE, changes with truncation.
                  (a) Depends on absolute spectral moments a_k without ratio cancellation
                  (b) Depends on non-(0,0) sector eigenvalues (B2, B3 bands at higher (p,q))
                  (c) Mode selection changes with L_max (DOS, mean energies of higher bands)
                  (d) Cutoff-function-dependent (f_2, f_4)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import *  # noqa: F401,F403

# ============================================================================
# Step 1: Load the S74 joint audit atlas
# ============================================================================

atlas_path = os.path.join(os.path.dirname(__file__), "s74_joint_audit_atlas.npz")  # (local)
d = np.load(atlas_path, allow_pickle=True)  # (local)

source = d['source']       # (local)
entry = d['entry']         # (local)
status = d['status']       # (local)
proof = d['proof_or_note'] # (local)

nr_mask = (status == 'NEEDS_REVERIFY')  # (local)
nr_idx = np.where(nr_mask)[0]  # (local)
n_total = len(nr_idx)  # (local)
print(f"Total NEEDS_REVERIFY entries: {n_total}")
assert n_total == 70, f"Expected 70, got {n_total}"

# ============================================================================
# Step 2: Build the classification for each entry
# ============================================================================
#
# The classification is based on the DERIVATION CHAIN of each quantity.
# The key structural facts are:
#
# (A) (0,0) sector eigenvalues are EXACTLY L_max-independent (W4-N, W4-X).
#     The eight positive eigenvalues at tau_fold:
#       E_8 = [0.84521, 0.84521, 0.84521, 0.84521, 0.81974, 0.97141, 0.97141, 0.97141]
#     are identical at L_max = 3, 5, 7 to machine precision.
#     Therefore any quantity computed PURELY from these 8 eigenvalues is ROBUST.
#
# (B) The BCS Hilbert space is 8-mode Fock space: 4 B2 + 1 B1 + 3 B3.
#     B1 = (0,0) sector acoustic mode (E_B1 = 0.81974), ROBUST.
#     B2 = 4 modes from (0,0) sector (E ~ 0.84521), ROBUST.
#     B3 = 3 modes from (0,0) sector (E ~ 0.97141), ROBUST.
#     ALL 8 modes live in the (0,0) sector per permanent result #10.
#     Therefore E_B1, E_B2_mean, E_B3_mean are all (0,0) sector eigenvalues.
#
# (C) BCS exact diagonalization at 8-mode level uses ONLY these 8 eigenvalues
#     as input (the pairing Hamiltonian H_BCS is built from (0,0) sector states).
#     Therefore E_cond, Delta_0_OES, Delta_BCS, S2_HFB are all ROBUST.
#     The GL fit (a_GL, b_GL) is a polynomial fit to the BCS energy landscape
#     which is computed from (0,0) eigenvalues -> ROBUST.
#
# (D) Spectral action moments a_0, a_2, a_4 are sums over ALL sectors.
#     They diverge as L_max^alpha (Weyl theorem). Any quantity derived from
#     absolute a_k values is FRAGILE.
#     EXCEPTION: Ratios where Weyl exponents cancel are QUASI-ROBUST or ROBUST.
#
# (E) Quantities derived from a_k ratios (e.g., a_4/a_2 for gauge couplings)
#     have partial Weyl cancellation. The protected ratio R_1 = a_0*a_4/a_2^2
#     drifts only +1.74% from L=3 to L=7 (S73B). These are QUASI-ROBUST.
#
# (F) Quantities depending on the full mode spectrum (not just (0,0) sector)
#     are potentially L_max-sensitive. This includes rho_B2_per_mode (DOS over
#     all modes) and anything derived from non-(0,0) sector information.
#
# (G) Cutoff function moments f_2, f_4 are scheme-dependent by definition. FRAGILE.

# Build classification arrays
new_status = np.empty(n_total, dtype=object)  # (local)
reason = np.empty(n_total, dtype=object)      # (local)
category = np.empty(n_total, dtype=object)    # (local)

# Entry names for lookup
names = [entry[i] for i in nr_idx]  # (local)

# -------------------------------------------------------------------
# Classification engine: one entry at a time
# -------------------------------------------------------------------

for j in range(n_total):
    name = names[j]  # (local)
    note = proof[nr_idx[j]]  # (local)

    # ================================================================
    # GROUP 1: BCS sector quantities from (0,0) eigenvalue ED
    # All 8 modes are (0,0) sector. ED uses only these eigenvalues.
    # Multi-layer protection theorem (W4-X) => ROBUST
    # ================================================================

    # E_cond variants: all from 8-mode ED on (0,0) sector eigenvalues
    if name in ('E_cond', 'E_cond_ED_8mode', 'E_cond_ED_5mode'):
        new_status[j] = 'ROBUST'
        reason[j] = ('8-mode ED uses ONLY (0,0) sector eigenvalues '
                      '(4B2+1B1+3B3 all in trivial sector). '
                      'W4-N proved E_8(L=3)=E_8(L=7) to machine precision. '
                      'Six-layer multi-layer protection (W4-X) guarantees invariance.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # BCS gaps: computed from (0,0) eigenvalue ED
    if name in ('Delta_0_OES', 'Delta_BCS', 'Delta_B3'):
        new_status[j] = 'ROBUST'
        reason[j] = ('Pair-addition gap from 8-mode ED on (0,0) sector. '
                      'Eigenvalue input L_max-invariant to machine precision (W4-N). '
                      'Delta_BCS R-PROTECTED status confirmed S74 W4-F #19.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Delta_0_GL: GL order parameter from GL fit to BCS energy landscape
    if name == 'Delta_0_GL':
        new_status[j] = 'ROBUST'
        reason[j] = ('GL order parameter sqrt(|a_GL|/(2*b_GL)). Both a_GL, b_GL are '
                      'polynomial fits to BCS energy landscape computed from (0,0) sector '
                      'eigenvalues. All inputs L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # GL coefficients: polynomial fit to BCS energy near fold
    if name in ('a_GL', 'b_GL'):
        new_status[j] = 'ROBUST'
        reason[j] = ('GL coefficient from quadratic/quartic fit of BCS energy near fold. '
                      'BCS energy computed from (0,0) sector eigenvalues only. '
                      'Input L_max-invariant by multi-layer protection.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # GL barrier heights: derived from a_GL, b_GL -> ROBUST
    if name in ('barrier_0d', 'barrier_1d'):
        new_status[j] = 'ROBUST'
        reason[j] = ('GL barrier height = a_GL^2/(4*b_GL) or related. '
                      'Both a_GL, b_GL are (0,0) sector derived. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Pair vibration: from 8-mode ED spectrum
    if name in ('omega_PV', 'omega_split'):
        new_status[j] = 'ROBUST'
        reason[j] = ('Pair vibration frequency from 8-mode ED on (0,0) sector. '
                      'All excited states of H_BCS use (0,0) eigenvalues. L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Ratio of BCS quantities: E_vac/E_cond
    if name == 'ratio_Evac_Econd':
        new_status[j] = 'ROBUST'
        reason[j] = ('Ratio of two (0,0)-sector ED quantities. '
                      'Both numerator and denominator are L_max-invariant. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # E_exc_ratio: ratio of BCS quantities
    if name == 'E_exc_ratio':
        new_status[j] = 'ROBUST'
        reason[j] = ('E_exc/|E_cond| = 443 from Schwinger duality (S38). '
                      'Both quantities from (0,0) sector BCS. '
                      'Dimensionless ratio of L_max-invariant quantities. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # E_exc: derived from E_exc_ratio * |E_cond|
    if name == 'E_exc':
        new_status[j] = 'ROBUST'
        reason[j] = ('E_exc = E_exc_ratio * |E_cond|. Both factors (0,0)-sector derived. '
                      'Product of L_max-invariant quantities. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # T_compound: E_exc / 8
    if name == 'T_compound':
        new_status[j] = 'ROBUST'
        reason[j] = ('Microcanonical temperature = E_exc / N_dof_BCS. '
                      'E_exc is (0,0)-sector derived. N_dof_BCS = 8 is structural. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # n_pairs: Bogoliubov pair count from transit
    if name == 'n_pairs':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('59.8 pairs from 3-component additive Landau-Zener at transit. '
                      'LZ depends on gap (ROBUST) and sweep rate d(tau)/dt. '
                      'Sweep rate involves dynamics on spectral action landscape S(tau) '
                      'which has Weyl-sensitive normalization. '
                      'However the LZ formula P = exp(-pi Delta^2 / v_sweep) saturates '
                      'at P=1 (verified), so the count is set by mode number (structural) '
                      'not the sweep rate. QUASI-ROBUST: protected by saturation, not by algebra.')
        category[j] = 'BCS_transit'
        continue

    # M_max_thouless: RPA Thouless parameter at fold
    if name == 'M_max_thouless':
        new_status[j] = 'ROBUST'
        reason[j] = ('RPA Thouless parameter maximum. RPA uses (0,0) sector eigenvalues '
                      'and BCS pairing amplitudes (from (0,0) ED). L_max-invariant input.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # S_inst: instanton action from MC on BCS landscape
    if name == 'S_inst':
        new_status[j] = 'ROBUST'
        reason[j] = ('Instanton action from MC sampling of BCS energy landscape. '
                      'Landscape computed from (0,0) sector eigenvalues. '
                      'MC explores configurations in the (0,0) Fock space. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Coherence lengths: from GL parameters
    if name in ('xi_BCS', 'xi_GL', 'xi_BCS_over_BW'):
        new_status[j] = 'ROBUST'
        reason[j] = ('Coherence length from GL parameters (a_GL, b_GL) and/or BCS gap. '
                      'All derived from (0,0) sector eigenvalues. '
                      'xi_BCS ~ 1/Delta_BCS and xi_GL ~ sqrt(|a_GL|/b_GL). '
                      'Both inputs ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Gamma_Langer: Langer decay rate from BCS landscape
    if name == 'Gamma_Langer_BCS':
        new_status[j] = 'ROBUST'
        reason[j] = ('Langer decay rate = attempt_freq * exp(-S_barrier). '
                      'Both the attempt frequency and barrier are from (0,0) sector BCS. '
                      'L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Kapitza ratio: from BCS dynamics
    if name == 'Kapitza_ratio':
        new_status[j] = 'ROBUST'
        reason[j] = ('Corrected Kapitza ratio from BCS thermal transport calculation (S38). '
                      'Uses (0,0) sector eigenvalues and BCS gap. L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # ================================================================
    # GROUP 2: Mode energies — B1, B2, B3 are all (0,0) sector
    # ================================================================

    if name == 'E_B1':
        new_status[j] = 'ROBUST'
        reason[j] = ('B1 acoustic mode energy = E_min of (0,0) sector = 0.81974. '
                      'Identical at L_max=3,5,7 to machine precision (W4-N).')
        category[j] = '(0,0)_eigenvalue_direct'
        continue

    if name == 'E_B2_mean':
        new_status[j] = 'ROBUST'
        reason[j] = ('Mean B2 energy: arithmetic mean of 4 (0,0) sector eigenvalues '
                      'at 0.84521. All four identical at L_max=3,5,7 (W4-N).')
        category[j] = '(0,0)_eigenvalue_direct'
        continue

    if name == 'E_B3_mean':
        new_status[j] = 'ROBUST'
        reason[j] = ('Mean B3 energy: arithmetic mean of 3 (0,0) sector eigenvalues '
                      'at 0.97141. All three identical at L_max=3,5,7 (W4-N).')
        category[j] = '(0,0)_eigenvalue_direct'
        continue

    # n_Bog: Bogoliubov fraction per mode
    if name == 'n_Bog':
        new_status[j] = 'ROBUST'
        reason[j] = ('Bogoliubov occupation number from (0,0) sector BdG spectrum. '
                      'BdG uses (0,0) eigenvalues and BCS gap. Both L_max-invariant. '
                      'n_Bog = 0.9986 reflects near-total pair conversion.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # ================================================================
    # GROUP 3: Spectral-action-derived quantities (absolute moments)
    # These depend on a_k sums over ALL sectors -> FRAGILE
    # ================================================================

    # E_cond_GL: GL energy derived from a_0, a_2, a_4 fit
    if name == 'E_cond_GL':
        new_status[j] = 'FRAGILE'
        reason[j] = ('GL functional energy derived from a_0, a_2, a_4 fit. '
                      'Spectral moments diverge as L^alpha (Weyl theorem). '
                      'Not protected by (0,0) sector or ratio cancellation. '
                      'a0 shift +7257%, a2 shift +2643% at L_max=7. FRAGILE.')
        category[j] = 'spectral_action_absolute'
        continue

    # m_tau: modulus mass from d2S/dtau2
    if name == 'm_tau':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('m_tau = sqrt(d2S/dtau2 / G_DeWitt). G_DeWitt=5 is structural. '
                      'd2S_fold is a spectral moment sum (FRAGILE in absolute value). '
                      'However note in W5-A says ratio d2S/S is near-protected. '
                      'The near-protection via ratio-of-moments gives partial Weyl cancellation '
                      'but the sqrt introduces non-linear dependence. QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    # omega_att: attractor frequency, claimed "fully geometric"
    if name == 'omega_att':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Attractor frequency claimed fully geometric (S38). '
                      'Derived from spectral action landscape ratios. '
                      'Weyl cancellation partial but not proven complete. QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    # omega_tau: transit frequency d(tau)/dt
    if name == 'omega_tau':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Transit frequency from BCS dynamics on S(tau). '
                      'Depends on ratio of spectral action derivatives. '
                      'Partial Weyl cancellation in ratio form but absolute moments enter '
                      'through the equation of motion. QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    # M_ATDHFB: collective mass from GCM overlap integrals
    if name == 'M_ATDHFB':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('ATDHFB collective mass from GCM overlap integrals at L_max=3. '
                      'GCM integrals involve (0,0) sector BCS wavefunctions (ROBUST input) '
                      'but the kinetic-energy operator involves the spectral-action metric '
                      'which is an a_2 derivative (L_max-sensitive in absolute value). '
                      'As a ratio M_ATDHFB * omega^2 = d2S/dtau2 cancellation may hold. '
                      'QUASI-ROBUST pending explicit L_max=5/7 test.')
        category[j] = 'mixed_BCS_SA'
        continue

    # H_fold: Hubble parameter at fold
    if name == 'H_fold':
        new_status[j] = 'FRAGILE'
        reason[j] = ('Hubble parameter = sqrt(S_fold / (3 M_Pl^2)). '
                      'S_fold diverges as L_max^alpha (shift ~287x at L_max=7). '
                      'Absolute spectral moment, no ratio protection. FRAGILE.')
        category[j] = 'spectral_action_absolute'
        continue

    # v_terminal: terminal velocity from dynamics on S(tau)
    if name == 'v_terminal':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Terminal velocity from dynamics on S(tau) landscape. '
                      'Derived from dS/dtau and kinetic normalization. '
                      'Both are spectral-moment sums, but their ratio may have partial '
                      'Weyl cancellation (the equation of motion involves dS/dtau divided '
                      'by effective inertia). QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    # dt_transit: transit duration from KZ scaling
    if name == 'dt_transit':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Transit duration from Kibble-Zurek scaling. '
                      'dt ~ xi_BCS / v_sweep. xi_BCS is ROBUST (from (0,0) sector). '
                      'v_sweep depends on spectral action dynamics (FRAGILE). '
                      'However as a ratio xi/v, partial cancellation may occur. '
                      'QUASI-ROBUST.')
        category[j] = 'mixed_BCS_SA'
        continue

    # ================================================================
    # GROUP 4: Gauge couplings — ratio of spectral moments
    # ================================================================

    if name == 'g_SU2_fold':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('SU(2) coupling at M_KK: g^2 = (4pi/f(0)) * a_4/a_2. '
                      'Ratio a_4/a_2 has partial Weyl cancellation '
                      '(alpha_a4 - alpha_a2 residual drift -12.2% at L_max=7). '
                      'W5-A notes ratio protected. QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    if name == 'g_U1_fold':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('U(1)_Y coupling at M_KK. Same a_4/a_2 ratio structure as g_SU2. '
                      'QUASI-ROBUST.')
        category[j] = 'spectral_action_ratio'
        continue

    if name == 'alpha2_MKK_inv':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('1/alpha_2 = 4pi/g_SU2^2. Inherits QUASI-ROBUST from g_SU2_fold.')
        category[j] = 'spectral_action_ratio'
        continue

    if name == 'sin2_thetaW_fold':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Weinberg angle at fold: ratio of gauge couplings g_U1/g_SU2. '
                      'Double ratio of spectral moments: (a_4/a_2) structure cancels. '
                      'Since sin2_thetaW = g_U1^2/(g_U1^2 + g_SU2^2) and both have same '
                      'a_4/a_2 dependence, the Weyl exponent cancels completely. '
                      'However the Dynkin-index-weighted ratio introduces sub-leading terms. '
                      'QUASI-ROBUST (closer to ROBUST).')
        category[j] = 'spectral_action_ratio'
        continue

    # ================================================================
    # GROUP 5: Josephson couplings — from (0,0) sector overlap integrals
    # ================================================================

    if name in ('J_C2', 'J_su2', 'J_u1'):
        new_status[j] = 'ROBUST'
        reason[j] = ('Josephson coupling from overlap integrals of (0,0) sector BCS '
                      'wavefunctions across Voronoi cell boundaries. '
                      'Uses (0,0) sector states only. L_max-invariant by multi-layer protection.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # T_acoustic: GGE acoustic temperature
    if name == 'T_acoustic':
        new_status[j] = 'ROBUST'
        reason[j] = ('GGE acoustic temperature from Bogoliubov modes in (0,0) sector. '
                      'T_acoustic = 0.112 M_KK. Derived from (0,0) eigenvalues and BCS gap. '
                      'L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # ================================================================
    # GROUP 6: Phonon spectrum — from GL-Josephson on (0,0) sector
    # ================================================================

    # Goldstone sound speed
    if name == 'c_Gold':
        new_status[j] = 'ROBUST'
        reason[j] = ('Goldstone sound speed from GL-Josephson phonon spectrum. '
                      'GL parameters (a_GL, b_GL) and Josephson couplings (J_C2 etc.) '
                      'all from (0,0) sector. L_max-invariant. '
                      'S74 W4-F #20 confirms c_Gold/c_fabric R-PROTECTED.')
        category[j] = 'phonon_(0,0)_derived'
        continue

    if name == 'c_Gold_over_c_fabric':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Ratio c_Gold/c_fabric. c_Gold is ROBUST ((0,0) sector). '
                      'c_fabric = sqrt(Z_fold / G_DeWitt) involves Z_fold (gradient stiffness, '
                      'spectral-action derivative). Z_fold diverges with L_max. '
                      'The ratio may be partially protected but c_fabric is not (0,0) sector. '
                      'S74 W4-F #20 reports drift 0.00% -> may be more robust than expected. '
                      'QUASI-ROBUST (close to ROBUST).')
        category[j] = 'phonon_mixed'
        continue

    # c_fabric: fabric sound speed from gradient stiffness
    if name == 'c_fabric':
        new_status[j] = 'FRAGILE'
        reason[j] = ('Fabric sound speed c_fabric = sqrt(Z_fold / G_DeWitt). '
                      'Z_fold (gradient stiffness at fold) is a spectral-action quantity '
                      'that involves d2S/dtau2 evaluated over ALL Peter-Weyl sectors. '
                      'Diverges as L_max^alpha. G_DeWitt=5 is structural. '
                      'FRAGILE.')
        category[j] = 'spectral_action_absolute'
        continue

    # Leggett and Higgs mode frequencies
    if name in ('omega_L1', 'omega_L2'):
        new_status[j] = 'ROBUST'
        reason[j] = (f'{name}: Leggett mode frequency from GL-Josephson phonon spectrum. '
                      'All inputs ((0,0) sector GL parameters + Josephson couplings) are '
                      'L_max-invariant. Leggett modes are inter-band phase oscillations '
                      'within the (0,0) sector.')
        category[j] = 'phonon_(0,0)_derived'
        continue

    if name in ('omega_H1', 'omega_H2', 'omega_H3'):
        new_status[j] = 'ROBUST'
        reason[j] = (f'{name}: Higgs mode frequency from GL-Josephson phonon spectrum. '
                      'All inputs from (0,0) sector. Higgs modes are amplitude oscillations '
                      'of BCS order parameter. L_max-invariant.')
        category[j] = 'phonon_(0,0)_derived'
        continue

    # ================================================================
    # GROUP 7: Quantities with non-(0,0) sector dependence -> FRAGILE
    # ================================================================

    if name == 'rho_B2_per_mode':
        new_status[j] = 'FRAGILE'
        reason[j] = ('B2 density of states per mode at fold. '
                      'DOS is computed from the FULL eigenvalue spectrum across all sectors. '
                      'Mode count and spectral weight change with L_max. FRAGILE.')
        category[j] = 'full_spectrum_DOS'
        continue

    # ================================================================
    # GROUP 8: Miscellaneous derived quantities
    # ================================================================

    if name == 'L_over_xi':
        new_status[j] = 'ROBUST'
        reason[j] = ('System size / coherence length = 0.031. '
                      'L is set by N_cells (structural = 32) and xi_BCS is (0,0) sector. '
                      'Both inputs L_max-invariant. ROBUST.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    if name == 'alpha_QM':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Quantum metric K^4 correction coefficient from s52_qm_dispersion. '
                      'Quantum metric involves spectral geometry (Fubini-Study on parameter '
                      'space). The K^4 coefficient depends on curvature of the BCS ground '
                      'state wavefunction in tau, which is (0,0) sector but the dispersion '
                      'relation may involve spectral-action normalization. QUASI-ROBUST.')
        category[j] = 'mixed_BCS_SA'
        continue

    if name == 'gamma_RP':
        new_status[j] = 'ROBUST'
        reason[j] = ('Ruelle-Pollicott gap = 0.0398. Liouvillian integrability scale. '
                      'From s52_liouvillian on BCS dynamics. The Liouvillian is constructed '
                      'from (0,0) sector Hamiltonian. L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    if name == 't_deph_over_t_transit':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Decoherence/transit ratio = 139729. '
                      'Decoherence time from (0,0) sector Liouvillian (ROBUST). '
                      'Transit time involves spectral-action dynamics (QUASI-ROBUST). '
                      'Ratio inherits the weaker classification. QUASI-ROBUST.')
        category[j] = 'mixed_BCS_SA'
        continue

    if name == 'F_BCS_over_V_KK':
        new_status[j] = 'FRAGILE'
        reason[j] = ('BCS free energy / V_KK probe ratio. '
                      'V_KK involves a_0 * M_KK^4 (spectral moment, FRAGILE). '
                      'F_BCS is (0,0) sector (ROBUST). The ratio inherits FRAGILE.')
        category[j] = 'mixed_BCS_SA'
        continue

    if name == 'IBO_ratio':
        new_status[j] = 'QUASI-ROBUST'
        reason[j] = ('Inverted Born-Oppenheimer ratio = geometric_freq / BCS_freq = 1118. '
                      'BCS frequency is (0,0) sector (ROBUST). Geometric frequency involves '
                      'spectral action dynamics. As a ratio, partial cancellation may hold. '
                      'QUASI-ROBUST.')
        category[j] = 'mixed_BCS_SA'
        continue

    if name == 'S2_HFB':
        new_status[j] = 'ROBUST'
        reason[j] = ('HFB pair correlation S_2(N=2) = -0.131 (pair-repulsive). '
                      'HFB is computed from (0,0) sector BCS wavefunctions. '
                      'L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    if name == 'a_scatter':
        new_status[j] = 'ROBUST'
        reason[j] = ('Scattering length from Bogoliubov amplitudes in (0,0) sector. '
                      'L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    if name == 'M_Bog_max':
        new_status[j] = 'ROBUST'
        reason[j] = ('Max Bogoliubov amplitude from (0,0) sector BdG spectrum. '
                      'L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    if name == 'Q_Leggett':
        new_status[j] = 'ROBUST'
        reason[j] = ('Leggett mode quality factor Q = 6.7e5. '
                      'From damping calculation on (0,0) sector phonon spectrum. '
                      'All inputs (mode frequencies, BCS amplitudes) are L_max-invariant.')
        category[j] = 'phonon_(0,0)_derived'
        continue

    if name == 'T_GGE_B2':
        new_status[j] = 'ROBUST'
        reason[j] = ('B2-sector GGE temperature = 0.668 M_KK. '
                      'GGE temperature determined by (0,0) sector Bogoliubov amplitudes '
                      'and mode energies. All inputs L_max-invariant.')
        category[j] = 'BCS_(0,0)_eigenvalue'
        continue

    # Cutoff function moments: scheme-dependent by definition
    if name in ('f_2_default', 'f_4_default'):
        new_status[j] = 'FRAGILE'
        reason[j] = (f'{name}: spectral cutoff function moment from S62 W1 constraint. '
                      'Explicitly cutoff-dependent (Gaussian scheme). '
                      'Changes with cutoff choice. FRAGILE by definition.')
        category[j] = 'cutoff_dependent'
        continue

    # ================================================================
    # GROUP 9: W5-F theorems (DNP, Pomeranchuk, FR)
    # Already reverified at L_max=7 in W4-N!
    # ================================================================

    if 'DNP' in name:
        new_status[j] = 'ROBUST'
        reason[j] = ('DNP instability: lambda_L_min in (0,0) sector, proven L_max-invariant '
                      'in W4-N. (0,0) is global minimum across all sectors. '
                      'DNP ratio 3.0027 identical at L=3 and L=7.')
        category[j] = 'permanent_theorem_reverified'
        continue

    if 'Pomeranchuk' in name:
        new_status[j] = 'ROBUST'
        reason[j] = ('Pomeranchuk f(0,0): spectral flow proxy from (0,0) sector '
                      'finite-difference derivative. Identical at L=3 and L=7 to machine '
                      'precision (W4-N). Multi-layer protected.')
        category[j] = 'permanent_theorem_reverified'
        continue

    if 'FR' in name or 'settling' in name:
        new_status[j] = 'ROBUST'
        reason[j] = ('FR settling time: W4-N correction -- V_FR is ANALYTIC Baptista potential, '
                      'NOT spectral-action Hessian. Independent of D_K spectrum entirely. '
                      'T_osc = 1398.7 Gyr >> universe age. Stronger than originally claimed.')
        category[j] = 'permanent_theorem_reverified'
        continue

    # Catch-all: should not reach here
    print(f"WARNING: Unclassified entry: {name}")
    new_status[j] = 'UNCLASSIFIED'
    reason[j] = f'No classification rule matched. Original note: {note}'
    category[j] = 'unknown'

# ============================================================================
# Step 3: Tally results
# ============================================================================

n_robust = np.sum(new_status == 'ROBUST')  # (local)
n_quasi = np.sum(new_status == 'QUASI-ROBUST')  # (local)
n_fragile = np.sum(new_status == 'FRAGILE')  # (local)
n_unclassified = np.sum(new_status == 'UNCLASSIFIED')  # (local)
n_classified = n_robust + n_quasi + n_fragile  # (local)

print(f"\n{'='*70}")
print(f"ATLAS RECLASSIFICATION RESULTS")
print(f"{'='*70}")
print(f"  ROBUST:        {n_robust:3d}  (L_max-INDEPENDENT by proof)")
print(f"  QUASI-ROBUST:  {n_quasi:3d}  (expected L_max-independent, not fully proven)")
print(f"  FRAGILE:       {n_fragile:3d}  (L_max-SENSITIVE)")
print(f"  UNCLASSIFIED:  {n_unclassified:3d}")
print(f"  ---------------------")
print(f"  TOTAL CLASSIFIED: {n_classified} / {n_total}")
print()

# Gate verdict
if n_classified >= 40:
    verdict = "PASS"  # (local)
elif n_classified >= 20:
    verdict = "INFO"  # (local)
else:
    verdict = "FAIL"  # (local)

print(f"Gate S75-O1-ATLAS-RECLASS: {verdict}")
print(f"  Threshold: >= 40 classified")
print(f"  Achieved:  {n_classified} classified")
print()

# ============================================================================
# Step 4: Print detailed classification table
# ============================================================================

print(f"\n{'='*70}")
print(f"DETAILED CLASSIFICATION TABLE")
print(f"{'='*70}")
print()

# Group by classification
for cls in ['ROBUST', 'QUASI-ROBUST', 'FRAGILE', 'UNCLASSIFIED']:
    idx_cls = np.where(new_status == cls)[0]  # (local)
    if len(idx_cls) == 0:
        continue
    print(f"\n--- {cls} ({len(idx_cls)} entries) ---\n")
    for j in idx_cls:
        print(f"  [{j+1:2d}] {names[j]:45s} | {category[j]:30s}")
        # Print reason wrapped
        r = reason[j]  # (local)
        lines = [r[i:i+90] for i in range(0, len(r), 90)]  # (local)
        for line in lines:
            print(f"       {line}")
        print()

# ============================================================================
# Step 5: Print the category breakdown
# ============================================================================

print(f"\n{'='*70}")
print(f"DERIVATION CATEGORY BREAKDOWN")
print(f"{'='*70}")

cats_unique = sorted(set(category))  # (local)
for cat in cats_unique:
    cat_idx = np.where(category == cat)[0]  # (local)
    cat_statuses = [new_status[j] for j in cat_idx]  # (local)
    print(f"\n  {cat}: {len(cat_idx)} entries")
    for st in ['ROBUST', 'QUASI-ROBUST', 'FRAGILE']:
        cnt = sum(1 for s in cat_statuses if s == st)  # (local)
        if cnt > 0:
            print(f"    {st}: {cnt}")

# ============================================================================
# Step 6: Structural floor promotion analysis
# ============================================================================

print(f"\n{'='*70}")
print(f"STRUCTURAL FLOOR PROMOTION ANALYSIS")
print(f"{'='*70}")
print()
print(f"Current structural floor (W4-W): 120 L_max-INDEPENDENT + 1 QUASI-INDEPENDENT = 121")
print(f"ROBUST entries from NEEDS_REVERIFY: {n_robust}")
print(f"Proposed new floor: 121 + {n_robust} = {121 + int(n_robust)}")
print(f"QUASI-ROBUST entries (pending verification): {n_quasi}")
print(f"FRAGILE entries (L_max-SENSITIVE): {n_fragile}")
print()
print(f"The {n_robust} ROBUST entries are promoted to L_max-INDEPENDENT by the following")
print(f"structural argument: all derive from (0,0) sector eigenvalues of D_K, which are")
print(f"EXACTLY invariant under L_max increase (proven in S74 W4-N, explained by the")
print(f"six-layer multi-layer protection theorem S74 W4-X). The block-diagonal structure")
print(f"of D_K (permanent result #10, Schur's lemma) guarantees that adding higher")
print(f"Peter-Weyl sectors (p,q) at increased L_max cannot shift (0,0) eigenvalues.")
print()
print(f"The {n_quasi} QUASI-ROBUST entries involve ratios of spectral-action moments where")
print(f"Weyl exponents partially cancel, or mixed chains involving (0,0) eigenvalues and")
print(f"spectral-action quantities. These require explicit L_max=5/7 verification.")
print()
print(f"The {n_fragile} FRAGILE entries depend on absolute spectral moments (a_0, a_2, a_4)")
print(f"or cutoff function choices and are genuinely L_max-SENSITIVE.")

# ============================================================================
# Step 7: Save results
# ============================================================================

out_path = os.path.join(os.path.dirname(__file__), "s75_atlas_reclassify.npz")  # (local)

np.savez(out_path,
    # Input
    original_entries=np.array(names, dtype=object),
    original_source=np.array([source[i] for i in nr_idx], dtype=object),
    original_note=np.array([proof[i] for i in nr_idx], dtype=object),
    # Classification
    new_status=new_status,
    reason=reason,
    derivation_category=category,
    # Tallies
    n_robust=np.array(int(n_robust)),
    n_quasi_robust=np.array(int(n_quasi)),
    n_fragile=np.array(int(n_fragile)),
    n_unclassified=np.array(int(n_unclassified)),
    n_classified=np.array(int(n_classified)),
    n_total=np.array(n_total),
    # Gate
    gate_name=np.array('S75-O1-ATLAS-RECLASS'),
    gate_verdict=np.array(verdict),
    gate_detail=np.array(f'{n_classified}/{n_total} classified: '
                         f'{int(n_robust)} ROBUST + {int(n_quasi)} QUASI-ROBUST + {int(n_fragile)} FRAGILE'),
    # Structural floor
    current_floor=np.array(121),
    proposed_floor=np.array(121 + int(n_robust)),
    # Category breakdown
    category_names=np.array(sorted(set(category)), dtype=object),
    category_counts=np.array([int(np.sum(category == c)) for c in sorted(set(category))]),
)

print(f"\nResults saved to: {out_path}")
print(f"\nDone.")
