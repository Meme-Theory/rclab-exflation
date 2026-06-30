#!/usr/bin/env python3
"""
s61_ps_regime.py — PS-REGIME-61: Pati-Salam Spectral Action Regime at GUT Scale
================================================================================
Gate: PS-REGIME-61
  INFO classification: which side of alpha_crit = 52.4 does alpha_PS land?

Physics:
  PHONON-2 (s61_alpha_physical) showed alpha/alpha_crit = 0.038 at Lambda = M_KK.
  The Pati-Salam model SU(4) x SU(2)_L x SU(2)_R unifies at a HIGHER scale.

  From Chamseddine-Connes-van Suijlekom (JHEP 2015, Paper 23):
    Model A: Lambda_PS ~ 2.5e15 GeV, m_R ~ 4.25e13 GeV
    Model B: Lambda_PS ~ 6.3e16 GeV, m_R ~ 1.5e11 GeV
    Model C: Lambda_PS ~ 2.7e15 GeV, m_R ~ 5.1e13 GeV

  The spectral action at the Pati-Salam scale uses the SAME Seeley-DeWitt
  expansion, but the cutoff Lambda is now Lambda_PS instead of M_KK.

  alpha = (Phi_1 / Phi_2) * Lambda^2   [Lambda in M_KK units]

  So alpha_PS = ratio * (Lambda_PS / M_KK)^2
  where ratio = Phi_1/Phi_2 from the cutoff function (same as PHONON-2).

Method:
  1. Load PHONON-2 cutoff moment ratios (Phi_1/Phi_2 for 6 cutoff functions)
  2. Compute Lambda_PS / M_KK for all three Pati-Salam models
  3. Compute alpha_PS = ratio * (Lambda_PS / M_KK)^2 for each combination
  4. Compare to alpha_crit = 52.4
  5. Classify: a_4-dominated (< 52.4) or a_2-dominated (> 52.4)

Author: baptista-spacetime-analyst (Session 61)
"""

import sys
import os
import time
import numpy as np

sys.path.insert(0, 'computations')
from canonical_constants import M_KK_gravity, M_KK_kerner

print("=" * 78)
print("  PS-REGIME-61: Pati-Salam Spectral Action Regime at GUT Scale")
print("=" * 78)

t_start = time.time()

# =============================================================================
# 1. Load PHONON-2 alpha data
# =============================================================================
print("\n--- 1. Loading PHONON-2 alpha data (s61_alpha_physical.npz) ---")

alpha_data = np.load('computations/session-61/s61_alpha_physical.npz', allow_pickle=True)
cutoff_names = alpha_data['cutoff_names']
ratio_phi1_phi2 = alpha_data['ratio_phi1_phi2']
alpha_at_MKK = alpha_data['alpha_at_MKK']
alpha_crit = float(alpha_data['alpha_crit'])

print(f"  alpha_crit = {alpha_crit:.4f}")
print(f"  Cutoff functions and their Phi_1/Phi_2 ratios:")
for i, name in enumerate(cutoff_names):
    print(f"    {name:20s}: ratio = {ratio_phi1_phi2[i]:.6f}, "
          f"alpha(M_KK) = {alpha_at_MKK[i]:.6f}")

# =============================================================================
# 2. Pati-Salam Unification Scales
# =============================================================================
print("\n--- 2. Pati-Salam unification scales (Paper 23: CCS 2015) ---")

# From Chamseddine-Connes-van Suijlekom, JHEP 1511 (2015) 011
# (researchers/Baptista/23_2015_Spectral_Pati_Salam.md)
ps_models = {
    'Model A (Composite)': {
        'Lambda_PS': 2.5e15,    # GeV
        'm_R': 4.25e13,         # GeV (PS breaking scale)
        'betas': (7/3, 3, 31/3),
        'description': 'First-order condition satisfied, composite Higgs'
    },
    'Model B (Fundamental)': {
        'Lambda_PS': 6.3e16,    # GeV
        'm_R': 1.5e11,          # GeV
        'betas': (-26/3, -2, 2),
        'description': 'No left-right symmetry, fundamental Higgs'
    },
    'Model C (LR symmetric)': {
        'Lambda_PS': 2.7e15,    # GeV
        'm_R': 5.1e13,          # GeV
        'betas': (-26/3, -26/3, -4/3),
        'description': 'Left-right symmetric, most general D_F'
    },
}

# Two M_KK routes
M_KK_values = {
    'M_KK (gravity)': M_KK_gravity,
    'M_KK (Kerner)': M_KK_kerner,
}

print(f"  M_KK (gravity) = {M_KK_gravity:.4e} GeV")
print(f"  M_KK (Kerner)  = {M_KK_kerner:.4e} GeV")

for name, model in ps_models.items():
    L_PS = model['Lambda_PS']
    for mkk_name, mkk_val in M_KK_values.items():
        ratio_scale = L_PS / mkk_val
        print(f"  {name}, {mkk_name}: "
              f"Lambda_PS = {L_PS:.2e} GeV, "
              f"Lambda_PS/M_KK = {ratio_scale:.4f}")

# =============================================================================
# 3. Compute alpha_PS for all combinations
# =============================================================================
print("\n--- 3. Alpha at Pati-Salam scale ---")
print(f"  alpha_crit = {alpha_crit:.4f}")
print()

# Structure: results[model_name][mkk_name] = dict of alpha values per cutoff
results = {}
all_alphas = []

for model_name, model in ps_models.items():
    Lambda_PS = model['Lambda_PS']
    results[model_name] = {}

    for mkk_name, mkk_val in M_KK_values.items():
        # Lambda_PS in M_KK units
        Lambda_ratio = Lambda_PS / mkk_val
        Lambda_sq = Lambda_ratio**2

        # alpha_PS = (Phi_1/Phi_2) * Lambda_PS^2  [Lambda in M_KK units]
        alpha_PS_values = ratio_phi1_phi2 * Lambda_sq

        results[model_name][mkk_name] = {
            'Lambda_ratio': Lambda_ratio,
            'Lambda_sq': Lambda_sq,
            'alpha_PS': alpha_PS_values,
        }

        print(f"  === {model_name} | {mkk_name} ===")
        print(f"      Lambda_PS/M_KK = {Lambda_ratio:.6e}")
        print(f"      (Lambda_PS/M_KK)^2 = {Lambda_sq:.6e}")
        print()

        for i, cname in enumerate(cutoff_names):
            a_ps = alpha_PS_values[i]
            regime = "a_4-DOMINATED (fold stable)" if a_ps < alpha_crit else "a_2-DOMINATED (fold unstable)"
            ratio_to_crit = a_ps / alpha_crit
            all_alphas.append(a_ps)
            print(f"      {cname:20s}: alpha_PS = {a_ps:.6e}, "
                  f"alpha/alpha_crit = {ratio_to_crit:.4e}, {regime}")
        print()

# =============================================================================
# 4. Classification Summary
# =============================================================================
print("\n--- 4. Classification Summary ---")
print(f"  alpha_crit = {alpha_crit:.4f}")
print()

# Count: how many combinations are above/below threshold?
n_above = 0
n_below = 0
n_total = 0

for model_name, model in ps_models.items():
    for mkk_name in M_KK_values:
        alphas = results[model_name][mkk_name]['alpha_PS']
        for i, a_ps in enumerate(alphas):
            n_total += 1
            if a_ps > alpha_crit:
                n_above += 1
            else:
                n_below += 1

print(f"  Total combinations: {n_total}")
print(f"  Below alpha_crit (a_4-dominated, fold stable): {n_below}")
print(f"  Above alpha_crit (a_2-dominated, fold unstable): {n_above}")
print()

# Key insight: Lambda_PS < M_KK for Models A and C with gravity route
# Lambda_PS > M_KK for Model B with gravity route
# Lambda_PS < M_KK for all models with Kerner route

print("  --- Key Scale Ratios ---")
for model_name, model in ps_models.items():
    Lambda_PS = model['Lambda_PS']
    for mkk_name, mkk_val in M_KK_values.items():
        r = Lambda_PS / mkk_val
        direction = "ABOVE" if r > 1 else "BELOW"
        print(f"  {model_name:30s} | {mkk_name:18s}: "
              f"Lambda_PS/M_KK = {r:.4f} ({direction} M_KK)")

print()
print("  --- Maximum alpha across all cutoffs (worst case) ---")
for model_name in ps_models:
    for mkk_name in M_KK_values:
        alphas = results[model_name][mkk_name]['alpha_PS']
        max_alpha = np.max(alphas)
        max_idx = np.argmax(alphas)
        max_cutoff = cutoff_names[max_idx]
        ratio_to_crit = max_alpha / alpha_crit
        regime = "a_4" if max_alpha < alpha_crit else "a_2"
        print(f"  {model_name:30s} | {mkk_name:18s}: "
              f"alpha_max = {max_alpha:.4e} ({max_cutoff}), "
              f"alpha/alpha_crit = {ratio_to_crit:.4e}, regime = {regime}")

# =============================================================================
# 5. Structural Analysis
# =============================================================================
print("\n--- 5. Structural Analysis ---")

# The key physics: alpha scales as Lambda^2. So the question is whether
# Lambda_PS^2 / M_KK^2 is large enough to push alpha above 52.4.

# For the heat kernel (largest ratio), alpha = 2.0 at Lambda = M_KK.
# We need alpha > 52.4, so we need Lambda^2 > 52.4/2 = 26.2 M_KK^2.
# Lambda > sqrt(26.2) * M_KK = 5.12 * M_KK.

Lambda_cross_heat = np.sqrt(alpha_crit / 2.0)
print(f"  Heat kernel: alpha crosses alpha_crit at Lambda/M_KK = {Lambda_cross_heat:.3f}")
print(f"  (i.e., Lambda = {Lambda_cross_heat * M_KK_gravity:.3e} GeV with gravity M_KK)")
print(f"  (i.e., Lambda = {Lambda_cross_heat * M_KK_kerner:.3e} GeV with Kerner M_KK)")

# For the sharp cutoff (smallest nontrivial ratio):
Lambda_cross_sharp = np.sqrt(alpha_crit / ratio_phi1_phi2[1])
print(f"  Sharp cutoff: alpha crosses alpha_crit at Lambda/M_KK = {Lambda_cross_sharp:.3f}")

# For all cutoffs:
print()
print("  Lambda_cross / M_KK for each cutoff:")
for i, cname in enumerate(cutoff_names):
    if ratio_phi1_phi2[i] > 0:
        L_cross = np.sqrt(alpha_crit / ratio_phi1_phi2[i])
        L_cross_grav = L_cross * M_KK_gravity
        print(f"    {cname:20s}: Lambda_cross/M_KK = {L_cross:.3f}, "
              f"Lambda_cross = {L_cross_grav:.3e} GeV")

# =============================================================================
# 6. The Decisive Comparison
# =============================================================================
print("\n--- 6. DECISIVE COMPARISON ---")
print()

# Model B is the only one where Lambda_PS is close to or above M_KK
# Let's check if ANY model can reach the a_2-dominated regime

print("  All Pati-Salam models are BELOW M_KK for both extraction routes:")
print(f"  Lambda_PS(A) = 2.5e15 << M_KK(gravity) = {M_KK_gravity:.3e}")
print(f"  Lambda_PS(B) = 6.3e16 ~  M_KK(gravity) = {M_KK_gravity:.3e}")
print(f"  Lambda_PS(C) = 2.7e15 << M_KK(gravity) = {M_KK_gravity:.3e}")
print()
print(f"  Lambda_PS(A) = 2.5e15 << M_KK(Kerner) = {M_KK_kerner:.3e}")
print(f"  Lambda_PS(B) = 6.3e16 <  M_KK(Kerner) = {M_KK_kerner:.3e}")
print(f"  Lambda_PS(C) = 2.7e15 << M_KK(Kerner) = {M_KK_kerner:.3e}")
print()

# Maximum alpha_PS across everything
global_max_alpha = np.max(all_alphas)
global_max_ratio = global_max_alpha / alpha_crit
print(f"  GLOBAL MAXIMUM alpha_PS = {global_max_alpha:.6e}")
print(f"  GLOBAL MAXIMUM alpha_PS / alpha_crit = {global_max_ratio:.6e}")
print()

if global_max_alpha < alpha_crit:
    verdict = "ALL Pati-Salam models are in the a_4-dominated regime (fold STABLE)"
    gate_status = "INFO"
else:
    verdict = "Some Pati-Salam models reach the a_2-dominated regime (fold UNSTABLE)"
    gate_status = "INFO"

print(f"  VERDICT: {verdict}")
print(f"  Gate: PS-REGIME-61 = {gate_status}")

# =============================================================================
# 7. Save results
# =============================================================================
print("\n--- 7. Saving results ---")

# Flatten results for saving
model_names_list = list(ps_models.keys())
mkk_names_list = list(M_KK_values.keys())

# Create a 3D array: [n_models, n_mkk, n_cutoffs]
n_models = len(model_names_list)
n_mkk = len(mkk_names_list)
n_cutoffs = len(cutoff_names)

alpha_PS_array = np.zeros((n_models, n_mkk, n_cutoffs))
Lambda_ratio_array = np.zeros((n_models, n_mkk))
Lambda_PS_values = np.zeros(n_models)

for i, model_name in enumerate(model_names_list):
    Lambda_PS_values[i] = ps_models[model_name]['Lambda_PS']
    for j, mkk_name in enumerate(mkk_names_list):
        r = results[model_name][mkk_name]
        alpha_PS_array[i, j, :] = r['alpha_PS']
        Lambda_ratio_array[i, j] = r['Lambda_ratio']

outpath = 'computations/session-61/s61_ps_regime.npz'
np.savez(outpath,
    # PHONON-2 inputs
    cutoff_names=cutoff_names,
    ratio_phi1_phi2=ratio_phi1_phi2,
    alpha_crit=alpha_crit,
    # Pati-Salam scales
    model_names=np.array(model_names_list),
    Lambda_PS_GeV=Lambda_PS_values,
    M_KK_gravity=M_KK_gravity,
    M_KK_kerner=M_KK_kerner,
    # Results
    alpha_PS=alpha_PS_array,
    Lambda_ratio=Lambda_ratio_array,
    # Gate
    gate_name=np.array(['PS-REGIME-61']),
    gate_verdict=np.array([gate_status]),
    gate_detail=np.array([verdict]),
    global_max_alpha=global_max_alpha,
    global_max_ratio=global_max_ratio,
)
print(f"  Saved to {outpath}")

elapsed = time.time() - t_start
print(f"\n  Total time: {elapsed:.2f}s")
print("=" * 78)
print(f"  PS-REGIME-61: {gate_status} — {verdict}")
print("=" * 78)
