"""
S80 W1-2: UNIFIED-AS-79-FULL — A_s^framework five-factor decomposition.

DUAL-BRANCH dispatch (W1-1 dual-owner DIVERGED > 20%):
  - Branch LI: H_tilde = 2.46411e-05 (SDW / epoch-resolved-a_2 / L_max=5)
  - Branch TD-framework: H_tilde = 5.90760e-03 (zeta / substrate-native / L_max=3, at N_pivot=55)
  - Additional reference: H_tilde_TD_pathB = 1.941e-02 (zeta / substrate-native / L_max=3, at fold)

Formula (P2-A closer, session-79/workshops/p2-a-as-ledger-dissonance.md:1140-1234):
  A_s = (H_tilde^2 / (8*pi^2)) * (1/eps_H) * F_amp * c_sub^{-1} * f_conv

Gate: S80-UNIFIED-AS-79-FULL
  PASS-F2: |A_s - 2.1e-9| / 2.1e-9 < 1.0 (factor of 2) under EITHER branch
  INFO-F15: ratio in [1.0, 15.0]
  FAIL-GT15: > 15 under BOTH branches

Sub-gate: S80-H-TILDE-DIVERGENCE-CHASE
  Identifies which scheme (zeta vs SDW-epoch-resolved-a_2) is physically correct,
  or flags as unresolved based on the A_s verdicts.

Classification: GEOMETRIC. A_s is a spectral-moment quantity (H_tilde^2 ~ rho_substrate
via Friedmann), NOT a CMB observable property. Matching to Planck is an emergence check
of the substrate's acoustic GGE spectral signature.
"""
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Required by project standards (though this script is scalar arithmetic)
from canonical_constants import (
    M_KK_gravity, M_Pl_reduced, a0_fold, A_s_CMB,
)

# =============================================================================
# BRANCH INPUTS (from W1-1 dual-owner workshop)
# =============================================================================

# Branch LI (SDW / epoch-resolved-a_2 / L_max=5): horizon-exit epoch canonical
H_tilde_LI = 2.46411e-05            # (local) W1-1 LI verdict line
scheme_LI = 'SDW'                   # (local)
convention_LI = 'epoch-resolved-a2' # (local)
L_max_LI = 5                        # (local)

# Branch TD-framework (zeta / substrate-native / L_max=3, at N_pivot=55)
H_tilde_TD_framework = 5.90760e-03  # (local) W1-1 TD verdict line (framework-internal dS evolution from fold)
scheme_TD = 'zeta'                  # (local)
convention_TD = 'substrate-native'  # (local)
L_max_TD = 3                        # (local)

# Reference only (NOT a verdict branch; used for diagnostic 267-e-folds test):
H_tilde_TD_pathB = 1.941e-02        # (local) W1-1 TD Path B fold-epoch
H_tilde_LI_obs = 5.989e-05          # (local) obs-inverse calibration (tautological)

# =============================================================================
# COMMON FACTOR VALUES (per plan W1-2)
# =============================================================================

eps_H = 0.02163                      # (local) one-loop slow-roll, per plan line 895
c_sub = 2.238                        # (local) central of S78 W2-E three-scheme range {2.232, 2.244, 3.647}
f_conv = 9.30e-4                     # (local) (M_KK/M_Pl_red)^2 single KK hierarchy, per plan line 909
k_a2 = 0.3822                        # (local) W0-5 slot factor [SUPPRESS], per plan line 908
F_amp_canonical = 1.0166             # (local) S80 W1-B-REMED PASS, Method B pinned value
F_amp_slot_adjusted = F_amp_canonical * k_a2   # (local) reading B: W1-B times k_a2

A_s_Planck = A_s_CMB                 # 2.1e-9 from canonical_constants

print('=' * 70)
print('S80 W1-2: UNIFIED-AS-79-FULL — DUAL-BRANCH dispatch')
print('=' * 70)

# =============================================================================
# SUBSTITUTION CHAIN — per factor, per branch
# =============================================================================

def unified_as_79(H_tilde, label):
    """Compute A_s^framework under UNIFIED-AS-79 with full substitution chain printed."""
    print(f"\n--- BRANCH {label} ---")
    print(f"Factor 1: H_tilde = {H_tilde:.6e}  (from W1-1 4-tuple)")
    print(f"Factor 2: eps_H   = {eps_H:.5f}")
    print(f"Factor 3: F_amp   = {F_amp_slot_adjusted:.6f} = {F_amp_canonical:.4f} (W1-B) * {k_a2:.4f} (k_a2)")
    print(f"Factor 4: c_sub   = {c_sub:.4f}  (central of S78 W2-E range)")
    print(f"Factor 5: f_conv  = {f_conv:.4e}  (single KK hierarchy)")
    # Canonical form:
    # A_s = (H_tilde^2 / (8*pi^2)) * (1/eps_H) * F_amp * (1/c_sub) * f_conv
    term_1 = H_tilde**2 / (8 * np.pi**2)                           # (local) prefactor from H_tilde^2
    term_2 = 1.0 / eps_H                                            # (local) inverse slow-roll
    term_3 = F_amp_slot_adjusted                                    # (local) amplification (SUPPRESS at a_2)
    term_4 = 1.0 / c_sub                                            # (local) subhorizon damping
    term_5 = f_conv                                                 # (local) physical-unit conversion
    A_s = term_1 * term_2 * term_3 * term_4 * term_5                # (local)
    ratio = A_s / A_s_Planck                                        # (local)
    delta_OOM = np.log10(abs(ratio))                                # (local)
    print(f"  Step-a: H_tilde^2/(8 pi^2)       = {term_1:.6e}")
    print(f"  Step-b: * 1/eps_H               -> {term_1*term_2:.6e}")
    print(f"  Step-c: * F_amp (slot-adjusted) -> {term_1*term_2*term_3:.6e}")
    print(f"  Step-d: * 1/c_sub               -> {term_1*term_2*term_3*term_4:.6e}")
    print(f"  Step-e: * f_conv                -> {A_s:.6e}")
    print(f"  A_s^framework / A_s_Planck = {ratio:.6e} (delta_OOM = {delta_OOM:+.4f})")
    # Factor-2 band = |delta_OOM| < log10(2) = 0.30103
    if abs(delta_OOM) < np.log10(2.0):
        verdict = 'PASS-F2'
    elif abs(delta_OOM) < np.log10(15.0):
        verdict = 'INFO-F15'
    else:
        verdict = 'FAIL-GT15'
    print(f"  Verdict: {verdict}")
    return dict(
        label=label,
        H_tilde=H_tilde, A_s=A_s, ratio=ratio, delta_OOM=delta_OOM,
        verdict=verdict,
        factors=dict(
            f1_Htilde_sq_over_8pi2=term_1,
            f2_inv_eps=term_2,
            f3_F_amp=term_3,
            f4_inv_csub=term_4,
            f5_f_conv=term_5,
        ),
    )

# Compute for both primary branches
result_LI = unified_as_79(H_tilde_LI, 'LI (SDW / epoch-resolved-a_2 / L_max=5)')
result_TD = unified_as_79(H_tilde_TD_framework, 'TD-framework (zeta / substrate-native / L_max=3)')

# Reference-only computations (diagnostic)
result_TD_pathB = unified_as_79(H_tilde_TD_pathB, 'TD-Path-B (REFERENCE — fold-epoch, zeta)')
result_LI_obsinv = unified_as_79(H_tilde_LI_obs, 'LI-obs-inverse (REFERENCE — tautological)')

# =============================================================================
# W1-6 SANITY CHECK: d(ln A_s)/d(ln c_sub) = -1 (machine precision)
# =============================================================================

print("\n--- W1-6 sanity check: d(ln A_s)/d(ln c_sub) identity ---")
c_sub_pert = c_sub * 1.01                                           # (local)
A_s_base_LI = result_LI['A_s']                                      # (local)
A_s_pert_LI = (H_tilde_LI**2 / (8*np.pi**2)) * (1.0/eps_H) * \
               F_amp_slot_adjusted / c_sub_pert * f_conv            # (local)
d_ln_As = np.log(A_s_pert_LI / A_s_base_LI)                         # (local)
d_ln_csub = np.log(c_sub_pert / c_sub)                              # (local)
logdiff = d_ln_As / d_ln_csub                                       # (local)
print(f"  c_sub -> c_sub * 1.01 = {c_sub_pert:.6f}")
print(f"  d(ln A_s) / d(ln c_sub) = {logdiff:.10f}  (expected: -1.0)")
W1_6_match = abs(logdiff + 1.0) < 1e-10                             # (local)
print(f"  W1-6 identity satisfied at machine precision: {W1_6_match}")

# =============================================================================
# 267-E-FOLDS DIAGNOSTIC (framework-internal eps_H evolution)
# =============================================================================

print("\n--- 267-e-folds diagnostic (framework eps_H epoch-independence test) ---")
# If H(N) = H_fold * exp(-eps_H * N), then reaching H_obs from H_fold requires:
# N_required = ln(H_fold / H_obs) / eps_H
H_fold_TD = H_tilde_TD_pathB                                        # (local) zeta-scheme Path B
H_target = H_tilde_LI_obs                                           # (local) obs-inverse target
N_required = np.log(H_fold_TD / H_target) / eps_H                   # (local)
print(f"  From H_fold={H_fold_TD:.3e} to H_obs={H_target:.3e} at eps_H={eps_H} requires N = {N_required:.1f}")
print(f"  Canonical N_pivot = 55; excess factor = {N_required/55:.2f}x")
flag_267 = N_required > 200                                          # (local)
print(f"  267-e-folds flag (epoch-dependent eps_H or fold != dS entry): {flag_267}")

# =============================================================================
# H-TILDE-DIVERGENCE-CHASE sub-gate
# =============================================================================

print("\n--- S80-H-TILDE-DIVERGENCE-CHASE sub-gate ---")
# Compare verdict outcomes under both branches
v_LI = result_LI['verdict']                                         # (local)
v_TD = result_TD['verdict']                                         # (local)
if 'PASS' in v_LI and 'FAIL' in v_TD:
    divergence_chase_verdict = 'LI-PHYSICAL'
    dc_interpretation = 'SDW/epoch-resolved-a2 produces Planck-compatible A_s; zeta/substrate-native over-predicts'
elif 'PASS' in v_TD and 'FAIL' in v_LI:
    divergence_chase_verdict = 'TD-PHYSICAL'
    dc_interpretation = 'zeta/substrate-native produces Planck-compatible A_s; SDW under-predicts'
elif 'PASS' in v_LI and 'PASS' in v_TD:
    divergence_chase_verdict = 'BOTH-COMPATIBLE'
    dc_interpretation = 'Both schemes Planck-compatible; scheme-degeneracy in A_s prediction'
elif 'FAIL' in v_LI and 'FAIL' in v_TD:
    divergence_chase_verdict = 'NEITHER-PHYSICAL'
    dc_interpretation = 'Both schemes FAIL; UNIFIED-AS-79 framework amendment required beyond scheme fix'
else:
    divergence_chase_verdict = 'UNRESOLVED-INFO'
    dc_interpretation = 'Both schemes in INFO band; scheme split does not resolve to PASS'
print(f"  Verdict: {divergence_chase_verdict}")
print(f"  Interpretation: {dc_interpretation}")

# =============================================================================
# SAVE RESULTS
# =============================================================================

np.savez(
    'computations/session-80/s80_unified_as_79_full.npz',
    H_tilde_LI=H_tilde_LI,
    H_tilde_TD_framework=H_tilde_TD_framework,
    H_tilde_TD_pathB=H_tilde_TD_pathB,
    H_tilde_LI_obs=H_tilde_LI_obs,
    eps_H=eps_H,
    c_sub=c_sub,
    f_conv=f_conv,
    k_a2=k_a2,
    F_amp_canonical=F_amp_canonical,
    F_amp_slot_adjusted=F_amp_slot_adjusted,
    A_s_Planck=A_s_Planck,
    A_s_LI=result_LI['A_s'],
    A_s_TD_framework=result_TD['A_s'],
    A_s_TD_pathB=result_TD_pathB['A_s'],
    A_s_LI_obs=result_LI_obsinv['A_s'],
    delta_OOM_LI=result_LI['delta_OOM'],
    delta_OOM_TD_framework=result_TD['delta_OOM'],
    verdict_LI=result_LI['verdict'],
    verdict_TD=result_TD['verdict'],
    N_required_267=N_required,
    flag_267=flag_267,
    W1_6_logdiff=logdiff,
    divergence_chase_verdict=divergence_chase_verdict,
)

# =============================================================================
# PLOT: A_s by factor + dual-branch bars + Planck band overlay
# =============================================================================

fig, axes = plt.subplots(1, 2, figsize=(13, 6))

# Left panel: A_s cumulative contributions (LI branch)
ax = axes[0]
labels_step = ['H_tilde^2/(8pi^2)', '* 1/eps_H', '* F_amp_slot', '* 1/c_sub', '* f_conv']
values_LI = []
acc = 1.0                                                           # (local)
acc *= result_LI['factors']['f1_Htilde_sq_over_8pi2']; values_LI.append(acc)
acc *= result_LI['factors']['f2_inv_eps'];             values_LI.append(acc)
acc *= result_LI['factors']['f3_F_amp'];                values_LI.append(acc)
acc *= result_LI['factors']['f4_inv_csub'];             values_LI.append(acc)
acc *= result_LI['factors']['f5_f_conv'];               values_LI.append(acc)
values_TD = []
acc = 1.0                                                           # (local)
acc *= result_TD['factors']['f1_Htilde_sq_over_8pi2']; values_TD.append(acc)
acc *= result_TD['factors']['f2_inv_eps'];             values_TD.append(acc)
acc *= result_TD['factors']['f3_F_amp'];                values_TD.append(acc)
acc *= result_TD['factors']['f4_inv_csub'];             values_TD.append(acc)
acc *= result_TD['factors']['f5_f_conv'];               values_TD.append(acc)
x = np.arange(len(labels_step))
ax.semilogy(x, np.abs(values_LI), 'o-', color='C0', label='Branch LI (SDW)', linewidth=2)
ax.semilogy(x, np.abs(values_TD), 's-', color='C3', label='Branch TD-framework (zeta)', linewidth=2)
ax.axhline(A_s_Planck, color='k', linestyle='--', alpha=0.6, label=f'Planck A_s = {A_s_Planck:.2e}')
ax.axhspan(A_s_Planck/2, A_s_Planck*2, color='g', alpha=0.15, label='PASS-F2 band')
ax.axhspan(A_s_Planck/15, A_s_Planck*15, color='y', alpha=0.10, label='INFO-F15 band')
ax.set_xticks(x); ax.set_xticklabels(labels_step, rotation=30, ha='right')
ax.set_ylabel('Cumulative product (log scale)')
ax.set_title('UNIFIED-AS-79 factor-by-factor accumulation')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# Right panel: A_s by branch (bar chart, log scale)
ax = axes[1]
branch_labels = ['LI\n(SDW)', 'TD-fw\n(zeta,N=55)', 'TD-Path-B\n(zeta,fold)', 'LI obs-inv\n(tautology)']
A_s_values = [result_LI['A_s'], result_TD['A_s'], result_TD_pathB['A_s'], result_LI_obsinv['A_s']]
colors = ['C0', 'C3', 'C1', 'gray']
bars = ax.bar(branch_labels, A_s_values, color=colors, alpha=0.7)
ax.set_yscale('log')
ax.axhline(A_s_Planck, color='k', linestyle='--', alpha=0.6, label=f'Planck A_s = {A_s_Planck:.2e}')
ax.axhspan(A_s_Planck/2, A_s_Planck*2, color='g', alpha=0.15, label='PASS-F2')
ax.axhspan(A_s_Planck/15, A_s_Planck*15, color='y', alpha=0.10, label='INFO-F15')
for bar, val, res in zip(bars, A_s_values, [result_LI, result_TD, result_TD_pathB, result_LI_obsinv]):
    h = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, h*2, f'{val:.2e}\nΔ={res["delta_OOM"]:+.2f}',
            ha='center', va='bottom', fontsize=8)
ax.set_ylabel('A_s^framework')
ax.set_title(f'UNIFIED-AS-79 A_s by branch (DIVERGENCE-CHASE: {divergence_chase_verdict})')
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plt.savefig('computations/session-80/s80_unified_as_79_full.png', dpi=140)
plt.close()

# =============================================================================
# VERDICT LINES for s80_gate_verdicts.txt
# =============================================================================

print("\n" + "=" * 70)
print("Verdict lines (to append to s80_gate_verdicts.txt):")
print("=" * 70)

verdict_main = (
    f"S80-UNIFIED-AS-79-FULL: BRANCH-LI={result_LI['verdict']} (A_s={result_LI['A_s']:.4e}, delta_OOM={result_LI['delta_OOM']:+.4f}), "
    f"BRANCH-TD={result_TD['verdict']} (A_s={result_TD['A_s']:.4e}, delta_OOM={result_TD['delta_OOM']:+.4f}), "
    f"4-tuple-LI=(A_s={result_LI['A_s']:.4e},scheme=SDW,convention=UNIFIED-AS-79-branch-LI,L_max=5), "
    f"4-tuple-TD=(A_s={result_TD['A_s']:.4e},scheme=zeta,convention=UNIFIED-AS-79-branch-TD,L_max=3), "
    f"F_amp_slot_adjusted={F_amp_slot_adjusted:.4f} (={F_amp_canonical:.4f}*{k_a2:.4f}), "
    f"W1-6_identity_match={W1_6_match}, flag_267_e_folds={flag_267} (N_required={N_required:.1f})"
)
print(verdict_main)

verdict_divergence = (
    f"S80-H-TILDE-DIVERGENCE-CHASE: {divergence_chase_verdict} -- "
    f"H_tilde_LI={H_tilde_LI:.4e}, H_tilde_TD={H_tilde_TD_framework:.4e}, OOM_gap={np.log10(H_tilde_TD_framework/H_tilde_LI):+.2f}, "
    f"verdict_LI={result_LI['verdict']}, verdict_TD={result_TD['verdict']}, interpretation='{dc_interpretation}'"
)
print(verdict_divergence)

with open('computations/session-80/s80_gate_verdicts.txt', 'a') as fh:
    fh.write('\n' + verdict_main + '\n')
    fh.write(verdict_divergence + '\n')

print("\nScript complete. Files produced:")
print("  computations/session-80/s80_unified_as_79_full.py")
print("  computations/session-80/s80_unified_as_79_full.npz")
print("  computations/session-80/s80_unified_as_79_full.png")
print("  computations/session-80/s80_gate_verdicts.txt (appended)")
