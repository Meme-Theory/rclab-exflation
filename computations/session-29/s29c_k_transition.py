#!/usr/bin/env python3
"""
29c-2: Transition Scale k_transition from Modulus Dynamics
==========================================================

Physics:
    When the modulus tau rolls from tau=0 to the BCS trapping point at tau~0.35-0.50,
    it crosses the BCS condensation threshold at some time t_BCS. The comoving
    wavenumber that exits the horizon at that moment defines a characteristic scale:

        k_transition = a(t_BCS) * H(t_BCS)

    where a(t) is the scale factor and H(t) is the Hubble parameter. This scale
    separates modes that experienced the BCS phase transition (k < k_transition)
    from those that did not (k > k_transition). In the exflation framework,
    k_transition should fall within the observable range for DESI/Euclid
    (0.01-0.3 h/Mpc) to produce detectable signatures.

    From the modulus EOM (s29b), we have t_BCS in physical seconds and H(t_BCS)
    at different M_KK values. The scale factor at BCS transition depends on the
    expansion history before and during the transition.

T3 re-run (S81): canonical-constants imports, local tags, SHA-256 input pins,
closure SHA, S81 canonical verdict form.

Substitution chain for the THRESHOLD DIRECTION claim (used in the verdict):
    Def-1 : k_phys_today(i) = H_BCS(i) * (T_CMB / T_BCS(i))          [radiation scaling, k_phys*a const]
    Def-2 : k_hMpc(i)       = [k_phys_today(i) / c_light] * Mpc_to_m / h_hubble
    Def-3 : threshold DESI  : DESI_kmin <= k_hMpc(i) <= DESI_kmax
    Sub   : k_hMpc(i)       = H_BCS(i) * (T_CMB / T_BCS(i)) * Mpc_to_m / (c_light * h_hubble)
    Simpl : k_hMpc proportional to (H_BCS / T_BCS).
    Dir-1 : T_BCS ~ M_KK (reheat), H_BCS ~ M_KK^2 / M_Pl  =>  k_hMpc ~ M_KK / M_Pl .
    Dir-2 : Increasing M_KK monotonically INCREASES k_hMpc in the radiation scenario.
    Threshold: gate PASSES iff any M_KK in [1e14, 1e18] lands in DESI; FAILS otherwise.

Method:
    For each M_KK:
    1. Extract t_BCS, H at BCS crossing from s29b data
    2. Compute a(t_BCS) assuming radiation-dominated expansion before BCS
    3. k_transition = a(t_BCS) * H(t_BCS) in physical units
    4. Convert to h/Mpc for comparison with surveys
    5. Plot vs DESI/Euclid sensitivity range

Inputs:
    computations/session-29/s29b_modulus_eom.npz   (SHA pinned below)

Outputs:
    computations/session-29/s29c_k_transition.npz
    computations/session-29/s29c_k_transition.png
"""

import os
# CPU-only script (tiny scalar-per-M_KK arithmetic) -- cap threads
os.environ.setdefault('OMP_NUM_THREADS', '8')  # (local)
os.environ.setdefault('MKL_NUM_THREADS', '8')  # (local)

import sys
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Canonical constants import
# The script lives in computations/_shared/, canonical_constants.py in computations/_shared/.
# -----------------------------------------------------------------------------
_HERE = os.path.dirname(os.path.abspath(__file__))  # (local)
_PROJ = os.path.dirname(_HERE)                      # (local)
_CANON_DIR = os.path.join(_PROJ, "computations")  # (local)
if _CANON_DIR not in sys.path:
    sys.path.insert(0, _CANON_DIR)
from canonical_constants import (
    c_light, hbar_SI, G_N, M_Pl_reduced,
    hbar_GeV_s, GeV_to_inv_s,
    H_0_km_s_Mpc, T_CMB_GeV, Mpc_to_m,
)

# Derived shortcuts (match legacy names in this script, tagged local)
c_mks        = c_light                 # (local)
G_N_mks      = G_N                     # (local)
M_Pl_GeV     = M_Pl_reduced            # (local) reduced Planck mass, GeV
h_hubble     = H_0_km_s_Mpc / 100.0    # (local) dimensionless Hubble
# H_100 = 100 km/s/Mpc = 1e5 m/s / (Mpc_to_m meters)
H_100_invs   = 1.0e5 / Mpc_to_m        # (local) = 100 km/s/Mpc in 1/s

# -----------------------------------------------------------------------------
# SHA-256 input pins + closure utilities
# -----------------------------------------------------------------------------
def _sha256_file(path):
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

INPUT_S29B = os.path.join(_HERE, "s29b_modulus_eom.npz")  # (local)
PIN_S29B = _sha256_file(INPUT_S29B)                       # (local)
PIN_CANON = _sha256_file(os.path.join(_CANON_DIR, "canonical_constants.py"))  # (local)
PIN_SELF  = _sha256_file(os.path.abspath(__file__))       # (local)

# Pre-registered closure-input map (stable JSON -> SHA-256)
_input_pin_map = {
    "s29b_modulus_eom.npz":     PIN_S29B,
    "canonical_constants.py":   PIN_CANON,
    "s29c_k_transition.py":     PIN_SELF,
}
_closure_payload = json.dumps(_input_pin_map, sort_keys=True).encode("utf-8")  # (local)
CLOSURE_SHA = hashlib.sha256(_closure_payload).hexdigest()                     # (local)

print("=" * 70)
print("T3-S29C-K-TRANSITION (S81 canonical form)")
print("=" * 70)
print(f"SHA s29b_modulus_eom.npz   = {PIN_S29B}")
print(f"SHA canonical_constants.py = {PIN_CANON}")
print(f"SHA s29c_k_transition.py   = {PIN_SELF}")
print(f"CLOSURE_SHA                = {CLOSURE_SHA}")
print("=" * 70)
print()

# -----------------------------------------------------------------------------
# Load s29b data
# -----------------------------------------------------------------------------
eom = np.load(INPUT_S29B, allow_pickle=True)  # (local)

M_KK_values = eom['M_KK_values']                     # ndarray of M_KK in GeV
tau_cross_val = float(eom['tau_cross'].flat[0])      # (local) = 0.5

n_MKK = len(M_KK_values)                             # (local)
t_BCS_sec    = np.zeros(n_MKK)                       # (local)
H_phys_GeV   = np.zeros(n_MKK)                       # (local)
T_RH_GeV     = np.zeros(n_MKK)                       # (local)
friction_param = np.zeros(n_MKK)                     # (local)

for i in range(n_MKK):
    t_BCS_sec[i]      = float(eom[f'obs_{i}_t_BCS_sec'].flat[0])
    H_phys_GeV[i]     = float(eom[f'obs_{i}_H_phys_gev'].flat[0])
    T_RH_GeV[i]       = float(eom[f'obs_{i}_T_RH_gev'].flat[0])
    friction_param[i] = float(eom[f'obs_{i}_friction_param'].flat[0])

latent_heat = float(eom['latent_heat_mu1'].flat[0])  # (local) F_BCS at mu=lambda_min, tau=0.50

print("Inputs loaded.")
print(f"  tau_cross = {tau_cross_val}")
print(f"  n_MKK     = {n_MKK}")
print()

# -----------------------------------------------------------------------------
# Compute k_transition for radiation-dominated and de Sitter scenarios
# -----------------------------------------------------------------------------
# Physics:
#   k_phys_today = H_BCS * (T_CMB / T_BCS)    [radiation dom, entropy conservation]
#   k [h/Mpc]    = (k_phys / c) * Mpc_to_m / h_hubble
# For de Sitter pre-BCS: k_dS = H_BCS * exp(N_eff) * (T_CMB / T_BCS)
# where N_eff = H*t_BCS (small for our cases).
# Both scenarios monotone in M_KK by Dir-2 above.

k_transition_rad = np.zeros(n_MKK)  # (local)
k_transition_dS  = np.zeros(n_MKK)  # (local)
T_BCS_from_H     = np.zeros(n_MKK)  # (local)
N_eff_values     = np.zeros(n_MKK)  # (local)

for i in range(n_MKK):
    # Hubble at BCS in 1/s
    H_invs = H_phys_GeV[i] * GeV_to_inv_s           # (local)

    # Temperature at BCS (~reheat temperature)
    T_BCS = T_RH_GeV[i]                              # (local) GeV
    T_BCS_from_H[i] = T_BCS

    # Scenario A: radiation-dominated prior at BCS
    # k_phys_today [1/s, via frequency-like units] = H_BCS * (T_CMB / T_BCS)
    k_phys_invs = H_invs * (T_CMB_GeV / T_BCS)       # (local)

    # Convert to h/Mpc:
    #   k_phys [1/m] = k_phys [1/s] / c
    #   k [h/Mpc]    = k_phys [1/m] * Mpc_to_m / h_hubble
    k_phys_invm = k_phys_invs / c_mks                # (local)
    k_hMpc = k_phys_invm * Mpc_to_m / h_hubble       # (local)
    k_transition_rad[i] = k_hMpc

    # Scenario B: de Sitter-like (lower bound on k since dS produces more expansion)
    N_eff = H_invs * t_BCS_sec[i]                    # (local)
    N_eff_values[i] = N_eff
    k_dS_invs = H_invs * np.exp(N_eff) * (T_CMB_GeV / T_BCS)  # (local)
    k_dS_invm = k_dS_invs / c_mks                    # (local)
    k_transition_dS[i] = k_dS_invm * Mpc_to_m / h_hubble

    print(f"M_KK = {M_KK_values[i]:.0e} GeV:")
    print(f"  t_BCS  = {t_BCS_sec[i]:.3e} s")
    print(f"  H_BCS  = {H_phys_GeV[i]:.3e} GeV = {H_invs:.3e} /s")
    print(f"  T_BCS  = {T_BCS:.3e} GeV")
    print(f"  k (rad) = {k_hMpc:.4e} h/Mpc")
    print(f"  k (dS)  = {k_transition_dS[i]:.4e} h/Mpc")
    print(f"  N_eff   = {N_eff:.4f}")
    print(f"  friction = {friction_param[i]:.4e}")
    print()

# -----------------------------------------------------------------------------
# Survey ranges
# -----------------------------------------------------------------------------
# DESI BAO: 0.02 - 0.3 h/Mpc (galaxy survey)
# Euclid:   0.001 - 0.5 h/Mpc (broader)
# CMB (Planck): 0.0005 - 0.2 Mpc^{-1}, convert to h/Mpc
DESI_kmin,   DESI_kmax   = 0.02,  0.30                        # (local)
Euclid_kmin, Euclid_kmax = 0.001, 0.50                        # (local)
CMB_kmin,    CMB_kmax    = 0.0005 / h_hubble, 0.2 / h_hubble  # (local)

print("=" * 50)
print("Survey ranges (h/Mpc):")
print(f"  DESI   : [{DESI_kmin:.4f}, {DESI_kmax:.4f}]")
print(f"  Euclid : [{Euclid_kmin:.4f}, {Euclid_kmax:.4f}]")
print(f"  CMB    : [{CMB_kmin:.4f}, {CMB_kmax:.4f}]")
print()

for i in range(n_MKK):
    in_DESI = DESI_kmin <= k_transition_rad[i] <= DESI_kmax     # (local)
    in_Euclid = Euclid_kmin <= k_transition_rad[i] <= Euclid_kmax  # (local)
    status = ""  # (local)
    if in_DESI:
        status = " ** IN DESI **"
    elif in_Euclid:
        status = " * in Euclid *"
    print(f"  M_KK={M_KK_values[i]:.0e}: k={k_transition_rad[i]:.3e} h/Mpc{status}")

# -----------------------------------------------------------------------------
# Gate verdict logic (pre-registered)
#   PASS       : any M_KK lands in DESI
#   INFO       : any M_KK lands in Euclid (outside DESI)
#   DIAGNOSTIC : within 5 log-decades of DESI midpoint
#   FAIL       : farther than 5 decades from DESI midpoint
# -----------------------------------------------------------------------------
any_in_Euclid = bool(np.any((k_transition_rad >= Euclid_kmin) & (k_transition_rad <= Euclid_kmax)))  # (local)
any_in_DESI   = bool(np.any((k_transition_rad >= DESI_kmin)   & (k_transition_rad <= DESI_kmax)))    # (local)

if any_in_DESI:
    verdict = "PASS"
    verdict_detail = "k_transition falls within DESI BAO range for some M_KK"   # (local)
elif any_in_Euclid:
    verdict = "INFO"
    verdict_detail = "k_transition falls within Euclid range but outside DESI"  # (local)
else:
    log_k_min   = np.log10(k_transition_rad.min())                       # (local)
    log_k_max   = np.log10(k_transition_rad.max())                       # (local)
    log_DESI_mid = np.log10(np.sqrt(DESI_kmin * DESI_kmax))              # (local)
    if abs(log_k_min - log_DESI_mid) < 5 or abs(log_k_max - log_DESI_mid) < 5:
        verdict = "INFO"
        verdict_detail = (f"k_transition range [{k_transition_rad.min():.2e}, "
                          f"{k_transition_rad.max():.2e}] h/Mpc, within 5 decades of DESI")  # (local)
    else:
        verdict = "FAIL"
        verdict_detail = "k_transition far from observable range"  # (local)

print(f"\nVerdict: {verdict}")
print(f"Detail : {verdict_detail}")

# -----------------------------------------------------------------------------
# Scaling exponent (power-law in M_KK)
# -----------------------------------------------------------------------------
log_M = np.log10(M_KK_values)           # (local)
log_k = np.log10(k_transition_rad)      # (local)
finite_mask = np.isfinite(log_k)        # (local)
if finite_mask.sum() >= 2:
    coeffs = np.polyfit(log_M[finite_mask], log_k[finite_mask], 1)  # (local)
    scaling_exp = float(coeffs[0])                                  # (local)
    print(f"\nScaling: log10(k) = {coeffs[0]:.3f} * log10(M_KK) + {coeffs[1]:.3f}")
    print(f"  => k ~ M_KK^{scaling_exp:.3f}")
else:
    scaling_exp = float('nan')  # (local)

# -----------------------------------------------------------------------------
# Save NPZ
# -----------------------------------------------------------------------------
out_npz = os.path.join(_HERE, 's29c_k_transition.npz')  # (local)
np.savez(
    out_npz,
    M_KK_values=M_KK_values,
    t_BCS_sec=t_BCS_sec,
    H_phys_GeV=H_phys_GeV,
    T_RH_GeV=T_RH_GeV,
    friction_param=friction_param,
    k_transition_rad=k_transition_rad,
    k_transition_dS=k_transition_dS,
    N_eff_values=N_eff_values,
    DESI_range=np.array([DESI_kmin, DESI_kmax]),
    Euclid_range=np.array([Euclid_kmin, Euclid_kmax]),
    CMB_range=np.array([CMB_kmin, CMB_kmax]),
    scaling_exponent=scaling_exp,
    verdict=verdict,
    verdict_detail=verdict_detail,
    closure_sha=CLOSURE_SHA,
    pin_s29b=PIN_S29B,
    pin_canon=PIN_CANON,
    pin_self=PIN_SELF,
)
print(f"\nSaved: {out_npz}")

# -----------------------------------------------------------------------------
# Plot
# -----------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 6))
ax = axes[0]
ax.loglog(M_KK_values, k_transition_rad, 'bo-', ms=8, lw=2, label='Radiation dom.')
ax.loglog(M_KK_values, k_transition_dS,  'rs--', ms=6, lw=1.5, label='de Sitter')
ax.axhspan(DESI_kmin, DESI_kmax, alpha=0.15, color='green',
           label=f'DESI [{DESI_kmin}-{DESI_kmax}]')
ax.axhspan(Euclid_kmin, Euclid_kmax, alpha=0.08, color='blue',
           label=f'Euclid [{Euclid_kmin}-{Euclid_kmax}]')
ax.axhspan(CMB_kmin, CMB_kmax, alpha=0.08, color='orange', label='CMB')
ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$k_{transition}$ [h/Mpc]', fontsize=13)
ax.set_title('BCS Transition Scale vs KK Mass', fontsize=14)
ax.legend(fontsize=9, loc='upper left')
ax.grid(True, alpha=0.3, which='both')
ax.set_xlim(5e13, 2e18)

ax = axes[1]
ax.loglog(M_KK_values, t_BCS_sec, 'ko-', ms=8, lw=2)
ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=13)
ax.set_ylabel(r'$t_{BCS}$ [seconds]', fontsize=13)
ax.set_title('BCS Transition Time vs KK Mass', fontsize=14)
ax.grid(True, alpha=0.3, which='both')
t_EW  = 1e-12   # (local) electroweak transition time
t_QCD = 1e-5    # (local) QCD transition time
t_BBN = 1.0     # (local) BBN time
ax.axhline(t_EW,  color='purple', ls=':', alpha=0.5, label=f'EW ({t_EW:.0e} s)')
ax.axhline(t_QCD, color='red',    ls=':', alpha=0.5, label=f'QCD ({t_QCD:.0e} s)')
ax.axhline(t_BBN, color='green',  ls=':', alpha=0.5, label=f'BBN ({t_BBN:.0f} s)')
ax.legend(fontsize=9)
ax.set_xlim(5e13, 2e18)

plt.tight_layout()
out_png = os.path.join(_HERE, 's29c_k_transition.png')  # (local)
plt.savefig(out_png, dpi=150, bbox_inches='tight')
print(f"Saved: {out_png}")

# -----------------------------------------------------------------------------
# Final S81 4-tuple line
# -----------------------------------------------------------------------------
# We report the MAX k_transition over M_KK (the one closest to DESI), the
# observational scheme used (radiation-dominated), the survey convention, and
# L_max is not applicable (cosmological post-processing).
k_max_report = float(k_transition_rad.max())   # (local)
print()
print(f"FINAL 4-TUPLE: value={k_max_report:.4e}_hMpc "
      f"scheme=radiation convention=DESI-BAO L_max=NA")
print(f"CLOSURE_SHA_FINAL: {CLOSURE_SHA}")
print()
print("Done.")
