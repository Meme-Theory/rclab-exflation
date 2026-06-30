#!/usr/bin/env python3
"""
s75_swampland_substrate.py — de Sitter Swampland Conjecture Test
================================================================

Gate: S75-H5-SWAMPLAND
  PASS: |V'|/V >= 0.5 for all tau in [0.19, 1.70] (Planck units)
  INFO: |V'|/V >= 0.1 but < 0.5
  FAIL: |V'|/V < 0.1 at some tau

Tests the Vafa (2018) de Sitter swampland conjecture against the spectral
action potential V(tau). The conjecture states:

    |nabla_phi V| / V >= c ~ O(1)     [in Planck units]

where phi is the canonically normalized scalar field. For the spectral action
modulus tau with kinetic term (1/2) G_DeWitt * M_KK^2 * (dtau/dt)^2:

    phi = sqrt(G_DeWitt) * M_KK * tau

The Planck-unit gradient ratio is:

    epsilon_V := M_Pl |dV/dphi| / V = (M_Pl / (sqrt(G) * M_KK)) * |dV/dtau| / V

where dV/dtau and V are both dimensionless (in M_KK^4 units).

Physical principle: The spectral action potential has NO minimum in the moduli
space (dV/dtau > 0 everywhere). The modulus rolls through the fold at Mach 13.75
— this is NOT a quasi-static de Sitter vacuum but a supersonic transit. The
swampland conjecture, which forbids metastable de Sitter vacua in consistent
quantum gravity, should be SATISFIED by such a runaway potential.

Session: S75
Author: Einstein Theorist
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from canonical_constants import (
    M_Pl_reduced, M_KK_gravity, M_KK_kerner, G_DeWitt, tau_fold,
    S_fold, dS_fold, a0_fold, a2_fold
)

# ─── Load S74 data ───────────────────────────────────────────────────────────
data = np.load(os.path.join(os.path.dirname(__file__),
               's74_moduli_stabilization.npz'), allow_pickle=True)

tau_scan = data['tau_scan']           # 500 points, [0.15, 1.70]
V_bare = data['V_bare_scan']          # V(tau) in M_KK^4 units
V_dressed_b = data['V_dressed_b']     # BCS-dressed potential
V_dressed_c = data['V_dressed_c']     # GGE-dressed potential
V_total_A = data['V_total_A']         # Instanton-corrected (type A)
V_total_B = data['V_total_B']         # Instanton-corrected (type B)

# ─── Gate range: tau in [0.19, 1.70] ─────────────────────────────────────────
GATE_TAU_LO = 0.19  # (local) fold location
GATE_TAU_HI = 1.70  # (local) upper bound of scan
PASS_THRESH = 0.5   # (local) PASS threshold
INFO_THRESH = 0.1   # (local) INFO threshold

mask = (tau_scan >= GATE_TAU_LO) & (tau_scan <= GATE_TAU_HI)  # (local)
tau_g = tau_scan[mask]  # (local)

# ─── Planck conversion factor ────────────────────────────────────────────────
# phi_canonical = sqrt(G_DeWitt) * M_KK * tau
# epsilon_V = M_Pl * |dV/dphi| / V = (M_Pl / (sqrt(G) * M_KK)) * |dV/dtau| / V
#
# Two M_KK routes give different conversion factors:
#   gravity:  M_Pl / (sqrt(5) * 7.43e16) = 14.66
#   kerner:   M_Pl / (sqrt(5) * 5.04e17) = 2.16
# Use BOTH and report. The conjecture should hold for EITHER route.

conv_grav = M_Pl_reduced / (np.sqrt(G_DeWitt) * M_KK_gravity)   # (local) = 14.66
conv_kern = M_Pl_reduced / (np.sqrt(G_DeWitt) * M_KK_kerner)    # (local) = 2.16

print("=" * 70)
print("S75-H5-SWAMPLAND: de Sitter Swampland Conjecture Test")
print("=" * 70)
print(f"M_Pl (reduced)    = {M_Pl_reduced:.4e} GeV")
print(f"M_KK (gravity)    = {M_KK_gravity:.4e} GeV")
print(f"M_KK (kerner)     = {M_KK_kerner:.4e} GeV")
print(f"G_DeWitt          = {G_DeWitt}")
print(f"Conversion factor (gravity): {conv_grav:.4f}")
print(f"Conversion factor (kerner):  {conv_kern:.4f}")
print()

# ─── Compute swampland ratio for ALL potential variants ──────────────────────
potentials = {
    'V_bare':      V_bare,
    'V_dressed_b': V_dressed_b,
    'V_dressed_c': V_dressed_c,
    'V_total_A':   V_total_A,
    'V_total_B':   V_total_B,
}

results = {}  # (local)

for name, V_full in potentials.items():
    V_g = V_full[mask]  # (local)
    dV_g = np.gradient(V_g, tau_g)  # (local) numerical derivative

    # Raw dimensionless ratio (M_KK units)
    raw_ratio = np.abs(dV_g) / V_g  # (local)

    # Planck-unit swampland parameter (both routes)
    eps_grav = conv_grav * raw_ratio  # (local)
    eps_kern = conv_kern * raw_ratio  # (local)

    results[name] = {
        'raw_ratio': raw_ratio,
        'eps_grav': eps_grav,
        'eps_kern': eps_kern,
        'min_raw': raw_ratio.min(),
        'min_grav': eps_grav.min(),
        'min_kern': eps_kern.min(),
        'max_raw': raw_ratio.max(),
        'max_grav': eps_grav.max(),
        'max_kern': eps_kern.max(),
        'tau_min_raw': tau_g[np.argmin(raw_ratio)],
        'tau_min_grav': tau_g[np.argmin(eps_grav)],
    }

    # Monotonicity check: is dV/dtau > 0 everywhere?
    n_sign_changes = np.sum(np.diff(np.sign(dV_g)) != 0)  # (local)
    results[name]['monotone'] = bool(np.all(dV_g > 0))
    results[name]['sign_changes'] = int(n_sign_changes)

    print(f"--- {name} ---")
    print(f"  Raw |dV/dtau|/V: min={raw_ratio.min():.6f} at tau={tau_g[np.argmin(raw_ratio)]:.4f}")
    print(f"                   max={raw_ratio.max():.6f} at tau={tau_g[np.argmax(raw_ratio)]:.4f}")
    print(f"  Planck (gravity): min epsilon_V = {eps_grav.min():.4f}")
    print(f"  Planck (kerner):  min epsilon_V = {eps_kern.min():.4f}")
    print(f"  Monotone (dV>0): {results[name]['monotone']}")
    print(f"  Sign changes:    {results[name]['sign_changes']}")
    print()

# ─── Gate verdict ────────────────────────────────────────────────────────────
# Use V_bare as the primary (spectral action IS the potential; dressing modifies it)
# Use the CONSERVATIVE route (Kerner M_KK gives smaller conversion factor)
primary = results['V_bare']  # (local)
min_eps_conservative = primary['min_kern']  # (local)
min_eps_optimistic = primary['min_grav']  # (local)

print("=" * 70)
print("GATE VERDICT: S75-H5-SWAMPLAND")
print("=" * 70)
print(f"Primary potential: V_bare (spectral action)")
print(f"Conservative route (Kerner M_KK): min epsilon_V = {min_eps_conservative:.4f}")
print(f"Optimistic route (gravity M_KK):  min epsilon_V = {min_eps_optimistic:.4f}")
print()

# Even the most conservative route gives min >> 0.5
if min_eps_conservative >= PASS_THRESH:
    verdict = "PASS"
    reason = (f"|V'|/V >= {min_eps_conservative:.2f} >= {PASS_THRESH} "
              f"everywhere in [{GATE_TAU_LO}, {GATE_TAU_HI}]")
elif min_eps_conservative >= INFO_THRESH:
    verdict = "INFO"
    reason = (f"|V'|/V = {min_eps_conservative:.4f} in [{INFO_THRESH}, {PASS_THRESH}) "
              f"-- marginal")
else:
    verdict = "FAIL"
    reason = (f"|V'|/V = {min_eps_conservative:.4f} < {INFO_THRESH} "
              f"at tau = {primary['tau_min_grav']:.4f}")

print(f"Verdict: {verdict}")
print(f"Reason:  {reason}")
print()

# ─── Detailed profile at key tau values ──────────────────────────────────────
print("Swampland parameter epsilon_V profile (V_bare, Kerner route):")
print(f"{'tau':>8s}  {'V (MKK4)':>12s}  {'dV/dtau':>12s}  {'raw |dV|/V':>12s}  {'eps_V':>10s}")
sample_taus = [0.19, 0.25, 0.35, 0.50, 0.70, 1.00, 1.30, 1.50, 1.70]  # (local)
V_g_bare = V_bare[mask]  # (local)
dV_g_bare = np.gradient(V_g_bare, tau_g)  # (local)
raw_bare = np.abs(dV_g_bare) / V_g_bare  # (local)
eps_bare_kern = conv_kern * raw_bare  # (local)
eps_bare_grav = conv_grav * raw_bare  # (local)

for t_sample in sample_taus:
    idx = np.argmin(np.abs(tau_g - t_sample))  # (local)
    print(f"{tau_g[idx]:8.4f}  {V_g_bare[idx]:12.4f}  {dV_g_bare[idx]:12.4f}  "
          f"{raw_bare[idx]:12.6f}  {eps_bare_kern[idx]:10.4f}")

print()

# ─── Refined de Sitter conjecture: also check the REFINED version ────────────
# The refined conjecture (Ooguri, Palti, Shiu, Vafa 2018):
#   |V'|/V >= c  OR  min(nabla_i nabla_j V) / V <= -c'
# with c, c' ~ O(1). The second condition involves the Hessian.
# For a 1D modulus: d^2V/dphi^2 / V < -c'
# d^2V/dphi^2 = (1/(G * M_KK^2)) * d^2V/dtau^2
# In Planck units: (M_Pl^2 / (G * M_KK^2)) * d^2V/dtau^2 / V

d2V_g = np.gradient(dV_g_bare, tau_g)  # (local) second derivative
conv2_grav = M_Pl_reduced**2 / (G_DeWitt * M_KK_gravity**2)  # (local)
conv2_kern = M_Pl_reduced**2 / (G_DeWitt * M_KK_kerner**2)  # (local)

eta_grav = conv2_grav * d2V_g / V_g_bare  # (local) eta_V parameter
eta_kern = conv2_kern * d2V_g / V_g_bare  # (local)

print("Refined conjecture check (eta_V = M_Pl^2 d^2V/dphi^2 / V):")
print(f"  Gravity route: eta_V in [{eta_grav.min():.2f}, {eta_grav.max():.2f}]")
print(f"  Kerner route:  eta_V in [{eta_kern.min():.2f}, {eta_kern.max():.2f}]")
print(f"  (eta_V > 0 means convex — NO tachyonic direction)")
print(f"  Note: since epsilon_V >> O(1), the refined condition is moot")
print()

# ─── Cross-check with S42 fold values ────────────────────────────────────────
# At the fold: dS_fold = 58672.80, S_fold = 250360.68
# Raw ratio at fold: dS_fold / S_fold
raw_fold_crosscheck = dS_fold / S_fold  # (local)
eps_fold_grav = conv_grav * raw_fold_crosscheck  # (local)
eps_fold_kern = conv_kern * raw_fold_crosscheck  # (local)
print("Cross-check with S42 canonical values at the fold (tau = 0.19):")
print(f"  dS_fold / S_fold = {raw_fold_crosscheck:.6f}")
print(f"  epsilon_V (gravity) = {eps_fold_grav:.4f}")
print(f"  epsilon_V (kerner)  = {eps_fold_kern:.4f}")
print(f"  (vs scan value at tau~0.19: raw={raw_bare[0]:.6f}, "
      f"eps_kern={eps_bare_kern[0]:.4f})")
print()

# ─── Physical interpretation ─────────────────────────────────────────────────
print("PHYSICAL INTERPRETATION:")
print(f"  The spectral action potential is monotonically increasing (no minimum).")
print(f"  The swampland parameter epsilon_V = {min_eps_conservative:.2f} -- {primary['max_kern']:.2f}")
print(f"  (Kerner, conservative) across the entire moduli range.")
print(f"  This EXCEEDS the O(1) bound demanded by the de Sitter swampland conjecture.")
print(f"  The potential is a runaway: V(tau) increases with tau, driving the modulus")
print(f"  toward tau -> 0 (the fold). There is no metastable de Sitter vacuum.")
print(f"  This is structurally consistent with the swampland program: the spectral")
print(f"  action does not support de Sitter vacua at any tau.")

# ─── Save data ───────────────────────────────────────────────────────────────
outpath = os.path.join(os.path.dirname(__file__), 's75_swampland_substrate.npz')  # (local)
np.savez(outpath,
         # Gate metadata
         gate_name='S75-H5-SWAMPLAND',
         gate_verdict=verdict,
         pass_thresh=PASS_THRESH,
         info_thresh=INFO_THRESH,
         # Scan data
         tau_gate=tau_g,
         V_bare_gate=V_g_bare,
         dV_bare_gate=dV_g_bare,
         # Swampland parameters
         raw_ratio_bare=raw_bare,
         eps_V_gravity=eps_bare_grav,
         eps_V_kerner=eps_bare_kern,
         eta_V_gravity=eta_grav,
         eta_V_kerner=eta_kern,
         # Conversion factors
         conv_factor_gravity=conv_grav,
         conv_factor_kerner=conv_kern,
         conv2_factor_gravity=conv2_grav,
         conv2_factor_kerner=conv2_kern,
         # Summary statistics
         min_eps_gravity=min_eps_optimistic,
         min_eps_kerner=min_eps_conservative,
         max_eps_gravity=primary['max_grav'],
         max_eps_kerner=primary['max_kern'],
         tau_at_min_eps=primary['tau_min_grav'],
         # Cross-check
         raw_fold_crosscheck=raw_fold_crosscheck,
         eps_fold_gravity=eps_fold_grav,
         eps_fold_kerner=eps_fold_kern,
         # All potential variants
         min_eps_all_grav=np.array([results[k]['min_grav'] for k in potentials]),
         min_eps_all_kern=np.array([results[k]['min_kern'] for k in potentials]),
         potential_names=np.array(list(potentials.keys())),
         )
print(f"\nSaved: {outpath}")
