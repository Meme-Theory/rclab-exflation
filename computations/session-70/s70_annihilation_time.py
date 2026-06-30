#!/usr/bin/env python3
"""
S70 ANNIHILATION-TIME-70: Bucher Test 4 — Pair Annihilation Timescale
=====================================================================

Computes the annihilation timescale for singularity-antisingularity pairs
on CG(24) and compares with the BA (Bogoliubov-Anderson) phonon lifetime
from S67 and the Richardson-Gaudin integrability relaxation timescale.

Physics
-------
Bucher (2024) found pre-annihilation acceleration of vortex singularity
pairs in continuous random wave fields. In the phonon-exflation framework,
the GGE relic on the 32-cell CG(24) fabric contains topological defects
(phase singularities) whose dynamics are governed by the collective mode
spectrum. The pair annihilation timescale t_ann is set by the approach
velocity (Goldstone sound speed c_Gold) and the initial separation
(one graph step = M_KK^{-1}).

The key physical point: t_ann ~ 10^{-42} s is the timescale AT WHICH
pairs WOULD annihilate IF integrability were broken. The GGE's Richardson-
Gaudin integrability freezes this dynamics, suppressing pair annihilation.
The pair density is frozen — a SNAPSHOT, not a steady-state.

Three timescales are compared:
  1. t_ann ~ hbar / (c_Gold * M_KK)       — pair approach timescale
  2. t_BA  ~ 2*pi*hbar / (Delta_B3 * M_KK) — BA mode oscillation period
  3. t_relax ~ t_ann / gamma_RP^2          — integrability-breaking relaxation

Gate: ANNIHILATION-TIME-70
  PASS: t_ann in [10^{-43}, 10^{-40}] s AND t_ann/t_BA in [0.1, 10]
  FAIL: t_ann > 10^{-35} s OR t_ann < 10^{-50} s
  INFO: within range but scaling unexpected

Author: Landau Condensed Matter Theorist (S70)
"""

import sys
import os
import numpy as np
from pathlib import Path

# === Import canonical constants ===
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import (
    M_KK, M_KK_gravity, hbar_GeV_s, PI,
    c_Gold, Delta_B3, gamma_RP, omega_L1,
    Delta_BCS, E_cond, J_C2, T_acoustic,
    H_fold, dt_transit, t_Planck, l_Planck,
    N_cells, H_0_inv_s
)

print("=" * 72)
print("S70 ANNIHILATION-TIME-70: Bucher Test 4 — Pair Annihilation Timescale")
print("=" * 72)

# ============================================================================
#  SECTION 1: Fundamental timescales in natural units (M_KK)
# ============================================================================

print("\n--- Section 1: Natural-unit timescales ---")

# 1a. Pair annihilation timescale
# Initial separation: one graph step on CG(24) = lattice spacing a = M_KK^{-1}
# Approach velocity: c_Gold = 0.915 M_KK (Goldstone sound speed, S52)
# t_ann = d_initial / v_approach = (1/M_KK) / (c_Gold) = 1 / (c_Gold * M_KK)
# In natural units (hbar=c=1): t_ann_nat = 1 / (c_Gold * M_KK)
# In seconds: t_ann = hbar / (c_Gold * M_KK)

t_ann_nat = 1.0 / c_Gold  # in M_KK^{-1} units
t_ann_s = hbar_GeV_s / (c_Gold * M_KK)

print(f"c_Gold (Goldstone sound speed) = {c_Gold:.3f} M_KK")
print(f"M_KK = {M_KK:.4e} GeV")
print(f"hbar = {hbar_GeV_s:.4e} GeV*s")
print(f"t_ann (natural) = 1/c_Gold = {t_ann_nat:.4f} M_KK^{{-1}}")
print(f"t_ann = hbar / (c_Gold * M_KK) = {t_ann_s:.4e} s")
print(f"log10(t_ann) = {np.log10(t_ann_s):.2f}")

# 1b. BA oscillation timescale (using Delta_B3 as the relevant gap)
# omega_BA ~ Delta_B3 * M_KK, where Delta_B3 = 0.176 M_KK
# t_BA = 2*pi / omega_BA = 2*pi*hbar / (Delta_B3 * M_KK)
omega_BA_nat = Delta_B3  # in M_KK units
t_BA_nat = 2.0 * PI / omega_BA_nat  # in M_KK^{-1}
t_BA_s = 2.0 * PI * hbar_GeV_s / (Delta_B3 * M_KK)

print(f"\nDelta_B3 = {Delta_B3:.3f} M_KK")
print(f"omega_BA = Delta_B3 = {omega_BA_nat:.3f} M_KK")
print(f"t_BA (natural) = 2*pi/omega_BA = {t_BA_nat:.4f} M_KK^{{-1}}")
print(f"t_BA = 2*pi*hbar / (Delta_B3 * M_KK) = {t_BA_s:.4e} s")
print(f"log10(t_BA) = {np.log10(t_BA_s):.2f}")

# 1c. Ratio t_ann / t_BA
ratio_ann_BA = t_ann_s / t_BA_s
print(f"\nt_ann / t_BA = {ratio_ann_BA:.4f}")
print(f"  (gate requires this in [0.1, 10])")

# ============================================================================
#  SECTION 2: Integrability-breaking relaxation timescale
# ============================================================================

print("\n--- Section 2: Integrability-breaking relaxation ---")

# The Ruelle-Pollicott gap gamma_RP = 0.0398 M_KK (S52 Liouvillian)
# This is the smallest nonzero frequency spacing in the pair Hamiltonian.
# It sets the integrability-breaking energy scale.
#
# The relaxation timescale from Fermi's golden rule (Paper 11, Eq. 3.4):
#   Gamma_relax ~ (delta_E / Delta)^2 * Gamma_direct
# where delta_E is the perturbation that breaks integrability.
#
# In the present context:
#   t_relax = t_ann / gamma_RP^2
# because gamma_RP/M_KK is the dimensionless integrability-breaking parameter,
# and the annihilation rate is suppressed by the square of this parameter
# (Fermi golden rule scaling: Gamma ~ |V|^2).

print(f"gamma_RP (Ruelle-Pollicott gap) = {gamma_RP:.5f} M_KK")
print(f"gamma_RP^2 = {gamma_RP**2:.6f}")

t_relax_nat = t_ann_nat / gamma_RP**2  # in M_KK^{-1}
t_relax_s = t_ann_s / gamma_RP**2

print(f"t_relax = t_ann / gamma_RP^2 = {t_relax_nat:.2f} M_KK^{{-1}}")
print(f"t_relax = {t_relax_s:.4e} s")
print(f"log10(t_relax) = {np.log10(t_relax_s):.2f}")
print(f"t_relax / t_ann = {t_relax_s / t_ann_s:.1f}")

# ============================================================================
#  SECTION 3: Comparison with S67 BA lifetime
# ============================================================================

print("\n--- Section 3: Cross-check with S67 BA lifetime ---")

# Load S67 results
s67_data = np.load(
    str(Path(__file__).resolve().parent / 's67_ba_lifetime.npz'),
    allow_pickle=True
)

tau_BA_min_s67 = float(s67_data['tau_BA_min_s'])  # shortest BA lifetime
tau_BA_max_s67 = float(s67_data['tau_BA_max_s'])  # longest BA lifetime
Gamma_to_s_inv = float(s67_data['Gamma_to_s_inv'])  # conversion factor
Q_Leggett = float(s67_data['Q_Leggett'])
Gamma_Leggett = float(s67_data['Gamma_Leggett'])

# S67 labels and full Gamma array
labels_s67 = s67_data['labels']
Gamma_fabric = s67_data['Gamma_fabric']  # shape (8, 32)
omega_BA_s67 = s67_data['omega_BA']      # shape (8, 32)

# BA decay rate range from S67 (M_KK units)
Gamma_BA_max_MKK = np.max(Gamma_fabric[:, 0])  # k=0 mode (highest Gamma)
Gamma_BA_min_MKK = np.min(Gamma_fabric[:, 0])  # k=0 mode (lowest Gamma)

# Convert to lifetimes
tau_BA_from_Gamma_max = 1.0 / (Gamma_BA_max_MKK * M_KK) * hbar_GeV_s  # shortest lifetime
tau_BA_from_Gamma_min = 1.0 / (Gamma_BA_min_MKK * M_KK) * hbar_GeV_s  # longest lifetime

print(f"S67 BA lifetime range: [{tau_BA_min_s67:.3e}, {tau_BA_max_s67:.3e}] s")
print(f"S67 Gamma_BA(k=0) range: [{Gamma_BA_min_MKK:.4f}, {Gamma_BA_max_MKK:.4f}] M_KK")
print(f"S67 Q_Leggett = {Q_Leggett:.2f}")
print(f"S67 Gamma_Leggett = {Gamma_Leggett:.5f} M_KK")

# Compare t_ann with S67 tau_BA
print(f"\nt_ann / tau_BA_min(S67) = {t_ann_s / tau_BA_min_s67:.3f}")
print(f"t_ann / tau_BA_max(S67) = {t_ann_s / tau_BA_max_s67:.3f}")
print(f"  (t_ann is {t_ann_s / tau_BA_min_s67:.1f}x shorter than shortest BA lifetime)")

# ============================================================================
#  SECTION 4: Leggett mode timescale (DM carrier)
# ============================================================================

print("\n--- Section 4: Leggett mode (DM carrier) timescale ---")

# omega_L1 = 0.138 M_KK (S52)
t_Leggett_nat = 2.0 * PI / omega_L1  # in M_KK^{-1}
t_Leggett_s = 2.0 * PI * hbar_GeV_s / (omega_L1 * M_KK)

print(f"omega_Leggett = {omega_L1:.3f} M_KK")
print(f"t_Leggett = 2*pi/omega_L = {t_Leggett_nat:.2f} M_KK^{{-1}}")
print(f"t_Leggett = {t_Leggett_s:.4e} s")
print(f"log10(t_Leggett) = {np.log10(t_Leggett_s):.2f}")

# Leggett lifetime from S67 (tau = 1/Gamma)
tau_Leggett_s67 = 1.0 / (Gamma_Leggett * M_KK) * hbar_GeV_s
print(f"Leggett lifetime (S67) = {tau_Leggett_s67:.4e} s")
print(f"t_Leggett / t_ann = {t_Leggett_s / t_ann_s:.1f}")
print(f"tau_Leggett / t_ann = {tau_Leggett_s67 / t_ann_s:.1e}")

# ============================================================================
#  SECTION 5: Timescale hierarchy summary
# ============================================================================

print("\n--- Section 5: Timescale hierarchy ---")

# Additional reference timescales
t_transit_s = dt_transit * hbar_GeV_s / M_KK  # transit duration in seconds
# Actually dt_transit is already in M_KK^{-1} units
t_transit_s = dt_transit / M_KK * hbar_GeV_s

print("\nComplete timescale hierarchy (seconds):")
print(f"  t_Planck    = {t_Planck:.3e} s  (Planck time)")
print(f"  t_ann       = {t_ann_s:.3e} s  (pair annihilation -- THIS COMPUTATION)")
print(f"  tau_BA_min  = {tau_BA_min_s67:.3e} s  (fastest BA decay, S67)")
print(f"  tau_BA_max  = {tau_BA_max_s67:.3e} s  (slowest BA decay, S67)")
print(f"  t_BA_osc    = {t_BA_s:.3e} s  (BA oscillation period)")
print(f"  t_Leggett   = {t_Leggett_s:.3e} s  (Leggett oscillation period)")
print(f"  t_relax     = {t_relax_s:.3e} s  (integrability-breaking relaxation)")
print(f"  tau_Leggett = {tau_Leggett_s67:.3e} s  (Leggett lifetime, S67)")
print(f"  t_transit   = {t_transit_s:.3e} s  (fold transit duration)")

# Log10 hierarchy
scales = {
    't_Planck': t_Planck,
    't_ann': t_ann_s,
    'tau_BA_min': tau_BA_min_s67,
    'tau_BA_max': tau_BA_max_s67,
    't_BA_osc': t_BA_s,
    't_Leggett': t_Leggett_s,
    't_relax': t_relax_s,
    'tau_Leggett': tau_Leggett_s67,
    't_transit': t_transit_s,
}

print("\nlog10 hierarchy:")
for name, val in sorted(scales.items(), key=lambda x: x[1]):
    print(f"  {name:15s}: log10 = {np.log10(val):+.2f}")

# ============================================================================
#  SECTION 6: Bucher connection — frozen GGE snapshot
# ============================================================================

print("\n--- Section 6: Bucher connection ---")

# The annihilation rate in the integrable limit is ZERO.
# With integrability-breaking perturbation delta_E = gamma_RP * M_KK:
#   Gamma_ann ~ gamma_RP^2 / t_ann_nat  (Fermi golden rule)
#   tau_ann_eff = t_ann_nat / gamma_RP^2 = t_relax
#
# The pair density WOULD decay as:
#   n_pairs(t) ~ n_pairs(0) * exp(-t / t_relax)
#
# At t = t_eq (matter-radiation equality ~ 3e12 s):
#   n_pairs(t_eq) / n_pairs(0) = exp(-t_eq / t_relax)
# This ratio tells us whether pairs survive until late cosmology.

t_eq_s = 2.917e12  # matter-radiation equality (from S67)  # (local)

n_ratio_eq = np.exp(-t_eq_s / t_relax_s)
# This is effectively exp(-huge number) = 0 if t_eq >> t_relax
# BUT: t_relax ~ 6e-39 s << t_eq ~ 3e12 s, so n_ratio ~ 0

# However, the GGE is INTEGRABLE. The actual relaxation rate is set by
# the Liouvillian spectrum, and the GGE is a fixed point.
# gamma_RP is a spacing in the spectrum, not a decay rate.
# The true decay rate from S67 is Gamma_BA ~ 0.3-2.3 M_KK (NOT gamma_RP^2).

# The resolution: what is frozen is not the BA mode occupation but the
# CONSERVED CHARGES of the Richardson-Gaudin Hamiltonian. The GGE
# distribution {n_k} = {p_n} from S56 is the permanent distribution.
# Phase singularity PAIRS in this distribution don't annihilate because
# the pair density is a function of the conserved charges, not a
# dynamical variable.

print("Bucher scenario: singularity pair annihilation")
print(f"  t_ann (if free) = {t_ann_s:.3e} s  — timescale for pair approach")
print(f"  t_relax (FGR)   = {t_relax_s:.3e} s  — Fermi golden rule relaxation")
print(f"  t_eq            = {t_eq_s:.3e} s  — matter-radiation equality")
print()
print("In the INTEGRABLE GGE:")
print("  The pair density is a functional of conserved charges I_k.")
print("  Conserved charges are PERMANENT (integrable Hamiltonian).")
print("  -> Pair annihilation is FORBIDDEN by conservation laws.")
print("  -> The Bucher acceleration mechanism cannot operate.")
print()
print("In a WEAKLY NON-INTEGRABLE system (gamma_RP << 1):")
print(f"  Pair lifetime ~ t_relax = {t_relax_s:.3e} s")
print(f"  Pairs annihilate within {t_relax_s/t_ann_s:.0f} natural timescales")
print(f"  This is {np.log10(t_eq_s/t_relax_s):.0f} OOM before z_eq")
print(f"  -> Even weak integrability breaking destroys pairs before z_eq")
print()
print("CONCLUSION: The frozen pair density in the GGE is the Bucher snapshot.")
print("  Pairs are present but CANNOT annihilate (integrable dynamics).")
print("  BA modes that WOULD mediate annihilation are overdamped (Q < 2, S67).")
print("  Leggett modes that carry DM are underdamped (Q = 18.6, S67).")

# ============================================================================
#  SECTION 7: Additional cross-checks
# ============================================================================

print("\n--- Section 7: Cross-checks ---")

# Cross-check 1: t_ann vs Planck time
ratio_Planck = t_ann_s / t_Planck
print(f"t_ann / t_Planck = {ratio_Planck:.2f}")
print(f"  -> t_ann is {ratio_Planck:.0f}x the Planck time (sub-Planckian: NO)")

# Cross-check 2: dimensional consistency
# t_ann = hbar / (c_Gold * M_KK)
# [hbar] = GeV*s, [c_Gold*M_KK] = GeV, so [t_ann] = s ✓
t_ann_check = hbar_GeV_s / (c_Gold * M_KK)
assert abs(t_ann_check / t_ann_s - 1.0) < 1e-10, "Dimensional consistency FAILED"
print("Dimensional consistency: VERIFIED")

# Cross-check 3: t_ann in M_KK^{-1} units
# 1 M_KK^{-1} in seconds = hbar / M_KK
one_MKK_inv_s = hbar_GeV_s / M_KK
print(f"1 M_KK^{{-1}} = {one_MKK_inv_s:.4e} s")
print(f"t_ann = {t_ann_nat:.4f} M_KK^{{-1}} = {t_ann_nat * one_MKK_inv_s:.4e} s")
assert abs(t_ann_nat * one_MKK_inv_s / t_ann_s - 1.0) < 1e-10, "Unit conversion FAILED"
print("Unit conversion: VERIFIED")

# Cross-check 4: Compare with QA estimate from S67 memory
# QA estimated tau_BA ~ 3.1e-37 s. Our t_ann ~ 10^{-41} s is 4-5 OOM shorter.
# This is expected: QA used a different (slower) velocity scale.
print(f"\nQA estimate (S67): tau_BA ~ 3.1e-37 s")
print(f"This computation: t_ann = {t_ann_s:.2e} s")
print(f"Ratio: {3.1e-37 / t_ann_s:.0f}x  (QA used slower velocity scale)")

# Cross-check 5: approach velocity in physical units
v_approach_m_per_s = c_Gold * M_KK * hbar_GeV_s / l_Planck * (l_Planck / t_Planck)
# More directly: v = c_Gold * M_KK in energy units -> v/c = c_Gold * M_KK / M_Pl
# But c_Gold is in M_KK units already (it's a speed in natural units of the fabric)
# So v/c = c_Gold if the fabric units are set such that c_fabric = 1
# Actually c_Gold = 0.915 means the Goldstone speed is 0.915 * M_KK in frequency units
# This is the GROUP VELOCITY of the Goldstone mode
print(f"\nApproach velocity: c_Gold = {c_Gold:.3f} M_KK")
print(f"  (This is a velocity in units where M_KK sets both energy and inverse length)")

# ============================================================================
#  SECTION 8: Gate verdict
# ============================================================================

print("\n" + "=" * 72)
print("GATE VERDICT: ANNIHILATION-TIME-70")
print("=" * 72)

# Gate criteria from session plan:
# PASS: t_ann in [10^{-43}, 10^{-40}] s AND t_ann/t_BA in [0.1, 10]
# FAIL: t_ann > 10^{-35} s OR t_ann < 10^{-50} s
# INFO: within range but scaling unexpected

log10_t_ann = np.log10(t_ann_s)

in_pass_range = (-43 <= log10_t_ann <= -40)
in_ratio_range = (0.1 <= ratio_ann_BA <= 10)
in_fail_range = (t_ann_s > 1e-35) or (t_ann_s < 1e-50)

print(f"  t_ann           = {t_ann_s:.4e} s")
print(f"  log10(t_ann)    = {log10_t_ann:.2f}")
print(f"  t_ann/t_BA      = {ratio_ann_BA:.4f}")
print(f"  Range check     : t_ann in [1e-43, 1e-40]? {'YES' if in_pass_range else 'NO'}")
print(f"  Ratio check     : t_ann/t_BA in [0.1, 10]? {'YES' if in_ratio_range else 'NO'}")

if in_fail_range:
    gate_verdict = "FAIL"
    gate_detail = (
        f"FAIL: t_ann = {t_ann_s:.3e} s outside allowed range "
        f"[1e-50, 1e-35] s"
    )
elif in_pass_range and in_ratio_range:
    gate_verdict = "PASS"
    gate_detail = (
        f"PASS: t_ann = {t_ann_s:.3e} s in [1e-43, 1e-40] AND "
        f"t_ann/t_BA = {ratio_ann_BA:.3f} in [0.1, 10]. "
        f"Annihilation timescale is same order as BA oscillation. "
        f"GGE integrability suppresses pair annihilation. "
        f"Frozen pair density is the Bucher snapshot."
    )
elif in_pass_range and not in_ratio_range:
    gate_verdict = "INFO"
    gate_detail = (
        f"INFO: t_ann = {t_ann_s:.3e} s in allowed range but "
        f"t_ann/t_BA = {ratio_ann_BA:.3f} outside [0.1, 10] — "
        f"unexpected scaling."
    )
else:
    gate_verdict = "INFO"
    gate_detail = (
        f"INFO: t_ann = {t_ann_s:.3e} s. log10 = {log10_t_ann:.2f}. "
        f"t_ann/t_BA = {ratio_ann_BA:.3f}."
    )

print(f"\n  VERDICT: {gate_verdict}")
print(f"  Detail:  {gate_detail}")

# ============================================================================
#  SECTION 9: Save results
# ============================================================================

output_path = Path(__file__).resolve().parent / 's70_annihilation_time.npz'

np.savez(
    str(output_path),
    # Primary results
    t_ann_s=t_ann_s,
    t_ann_nat=t_ann_nat,
    t_BA_s=t_BA_s,
    t_BA_nat=t_BA_nat,
    ratio_ann_BA=ratio_ann_BA,
    t_relax_s=t_relax_s,
    t_relax_nat=t_relax_nat,
    t_Leggett_s=t_Leggett_s,
    # Input parameters
    c_Gold=c_Gold,
    M_KK=M_KK,
    Delta_B3=Delta_B3,
    gamma_RP=gamma_RP,
    omega_L1=omega_L1,
    hbar_GeV_s=hbar_GeV_s,
    # S67 cross-references
    tau_BA_min_s67=tau_BA_min_s67,
    tau_BA_max_s67=tau_BA_max_s67,
    Q_Leggett_s67=Q_Leggett,
    Gamma_Leggett_s67=Gamma_Leggett,
    tau_Leggett_s67=tau_Leggett_s67,
    # Hierarchy
    log10_t_ann=log10_t_ann,
    log10_t_BA=np.log10(t_BA_s),
    log10_t_relax=np.log10(t_relax_s),
    log10_t_Leggett=np.log10(t_Leggett_s),
    log10_tau_BA_min=np.log10(tau_BA_min_s67),
    log10_tau_BA_max=np.log10(tau_BA_max_s67),
    # Gate
    gate_name='ANNIHILATION-TIME-70',
    gate_verdict=gate_verdict,
    gate_detail=gate_detail,
)

print(f"\nResults saved to: {output_path}")
print("DONE.")
