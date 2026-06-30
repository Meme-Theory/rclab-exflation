#!/usr/bin/env python3
"""
S83 Wave 3 Gate G40 -- TAU-GGE-AT-K
====================================

Gate: S83-TAU-GGE-AT-K  [VERIFY]
Classification: PHONONIC
Owner: landau-condensed-matter-theorist

Purpose:
  Test whether the GGE relaxation timescale tau_GGE(K) undergoes a
  regime change between the framework primary K=2.035 (short-relaxation
  end of corridor) and the W1-E reconciliation point K=1.6e5 (long-
  relaxation, near the IC corridor ceiling S_IC^cap = 3.556e5).

  Pre-registered: PASS if tau_GGE(K=1.6e5) / tau_GGE(K=2.035) >= 100.
                  INFO if ratio in [10, 100). FAIL if ratio < 10.

Phononic framing:
  tau_GGE is the relaxation time to the generalized Gibbs ensemble --
  the timescale over which the substrate's non-equilibrium quasiparticle
  distribution approaches its K-dependent attractor. Short tau_GGE
  means the substrate equilibrates its occupation on a timescale faster
  than transit (dt_transit ~ 1.13e-3 / M_KK); long tau_GGE means the
  GGE relic is FROZEN IN during transit (the 3He-B-analog inheritance
  condition). The K factor sets the squeezing amplitude, which feeds
  directly into the Anderson-Morel quenched-BCS relaxation formula.

Substitution chain [VERIFY]:
  Step 1 (def):
    tau_GGE(K) = pi * hbar / [4 * Delta_BCS * tanh(Delta/(2T))]
                                  (Anderson-Morel; Volovik paper 25 sec V;
                                   S77 GGE-relaxation framework)
    K = coth(Delta / (2 T_eff))   (squeezing factor, II.A inversion)
    => tanh(Delta / (2T_eff)) = 1/K

  Step 2 (subst):
    tau_GGE(K) = pi * hbar * K / (4 * Delta_BCS)
    In hbar=1, Delta in M_KK units:
    tau_GGE(K) = (pi / 4) * K / Delta_BCS     [units: 1 / M_KK]

  Step 3 (simpl):
    ratio(K2, K1) = tau_GGE(K2) / tau_GGE(K1)
                  = [(pi/4) * K2 / Delta_BCS] / [(pi/4) * K1 / Delta_BCS]
                  = K2 / K1
    Both (pi/4) and Delta_BCS CANCEL in the ratio. This is the
    single-scale (single-Delta) closed-form prediction; the per-band-
    weighted refinement (V.3) multiplies by an O(1) amplification
    factor tau_full / tau_simple = 1.299 that cancels identically in
    any ratio at the same K-pair.

  Step 4 (direction):
    K2 = 1.6e5, K1 = 2.035 => ratio = 1.6e5 / 2.035 = 78,624
    PASS threshold: ratio >= 100. Since 78,624 >> 100, the
    regime-change claim is PASS.

Gate pre-registration (from session-83-plan.md L2426-L2466):
  PASS: tau_GGE(K=1.6e5) / tau_GGE(K=2.035) >= 100
  INFO: ratio >= 10 but < 100
  FAIL: ratio < 10

Output 4-tuple: (tau_ratio=?, scheme=GGE-relaxation-timescale,
                 convention=K=2.035-vs-K=1.6e5, L_max=N/A)
"""

from __future__ import annotations

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Canonical constants import (MANDATORY; S34+) ---
sys.path.insert(0, str(Path(__file__).resolve().parent))
from canonical_constants import Delta_BCS, M_KK, dt_transit, hbar_GeV_s, t_Planck

# ----------------------------------------------------------------------------
# Local pins (machinery, [VERIFY])
# ----------------------------------------------------------------------------
K1          = 2.035                      # (local) framework primary K (S43 R3)
K2          = 1.6e5                      # (local) W1-E Friedmann-BCS reconciliation K
PASS_THRESH = 100.0                      # (local) gate PASS threshold
INFO_THRESH = 10.0                       # (local) gate INFO threshold
OUTPUT_STEM = Path(__file__).with_suffix('')  # (local) npz/png basename

print(f"=== S83 Wave 3 Gate G40 -- TAU-GGE-AT-K ===")
print(f"K1 (primary)            = {K1}")
print(f"K2 (W1-E reconcile)     = {K2:.4e}")
print(f"PASS_THRESH             = {PASS_THRESH}")
print(f"INFO_THRESH             = {INFO_THRESH}")
print(f"Canonical Delta_BCS     = {Delta_BCS:.10f}  [M_KK units]")
print(f"Canonical M_KK          = {M_KK:.6e} GeV")
print(f"Canonical dt_transit    = {dt_transit:.6e} / M_KK")
print(f"Canonical hbar_GeV_s    = {hbar_GeV_s:.6e} GeV * s")
print(f"Canonical t_Planck      = {t_Planck:.6e} s")
print()

# ----------------------------------------------------------------------------
# Input-pin SHA-256 chain (S81+ standard)
# ----------------------------------------------------------------------------
# Static analytic gate -- pin the machinery vector + canonical values.
input_pins = {                                                      # (local)
    "K1":              f"{K1:.10e}",
    "K2":              f"{K2:.10e}",
    "PASS_THRESH":     f"{PASS_THRESH:.10e}",
    "INFO_THRESH":     f"{INFO_THRESH:.10e}",
    "Delta_BCS":       f"{Delta_BCS:.14e}",
    "M_KK_GeV":        f"{M_KK:.14e}",
    "dt_transit":      f"{dt_transit:.14e}",
    "hbar_GeV_s":      f"{hbar_GeV_s:.14e}",
    "t_Planck_s":      f"{t_Planck:.14e}",
    "formula":         "tau_GGE(K)=pi*K/(4*Delta_BCS); ratio=K2/K1 (Delta cancels)",
    "scheme":          "GGE-relaxation-timescale",
    "convention":      "K=2.035-vs-K=1.6e5",
    "L_max":           "N/A",
}
pin_blob = "\n".join(f"{k}={v}" for k, v in sorted(input_pins.items()))   # (local)
closure_sha = hashlib.sha256(pin_blob.encode('utf-8')).hexdigest()        # (local)
print("Input pin map (sorted):")
for k, v in sorted(input_pins.items()):
    print(f"  {k}: {v}")
print(f"Closure SHA-256: {closure_sha}")
print()


# ----------------------------------------------------------------------------
# Core computation: single-scale Anderson-Morel formula
# ----------------------------------------------------------------------------
def compute_tau_GGE(K: float, Delta: float = Delta_BCS) -> float:
    """Compute single-scale quenched-BCS GGE relaxation time.

    Formula: tau_GGE(K) = pi * K / (4 * Delta)
    Units: 1 / M_KK (natural units, hbar=1, Delta in M_KK).

    Derivation (Landau synthesis S82 sec II.C):
      tau_GGE = pi / [4 * Delta * tanh(Delta/(2T))]
      K = coth(Delta/(2T)) => tanh = 1/K
      => tau_GGE(K) = pi * K / (4 * Delta)
    """
    if K < 1.0:
        raise ValueError(f"K={K} violates positivity floor (K >= 1).")
    if Delta <= 0:
        raise ValueError(f"Delta={Delta} must be positive.")
    return np.pi * K / (4.0 * Delta)


# Evaluate at K1 and K2
t1 = compute_tau_GGE(K=K1)                                          # (local)
t2 = compute_tau_GGE(K=K2)                                          # (local)
ratio = t2 / t1                                                     # (local)

print(f"--- Single-scale closed-form evaluation ---")
print(f"tau_GGE({K1})       = {t1:.6e} / M_KK")
print(f"tau_GGE({K2:.2e})   = {t2:.6e} / M_KK")
print(f"Ratio               = {ratio:.6e}")
print()

# ----------------------------------------------------------------------------
# Cross-check 1: direct K-ratio (Delta_BCS cancels identically)
# ----------------------------------------------------------------------------
direct_K_ratio = K2 / K1                                            # (local)
ratio_error    = abs(ratio - direct_K_ratio)                        # (local)
rel_error      = ratio_error / direct_K_ratio                       # (local)

print(f"--- Cross-check 1: direct K-ratio (Delta-cancellation identity) ---")
print(f"K2 / K1             = {direct_K_ratio:.6e}")
print(f"|ratio - K2/K1|     = {ratio_error:.3e}")
print(f"rel error           = {rel_error:.3e}")
assert rel_error < 1e-14, "Delta-cancellation identity violated."
print(f"PASS: identity holds to machine precision.")
print()

# ----------------------------------------------------------------------------
# Cross-check 2: monotonicity of tau_GGE(K) across corridor
# ----------------------------------------------------------------------------
K_scan = np.logspace(0.0, 5.55, 100)                                # (local)
tau_scan = np.array([compute_tau_GGE(K=K) for K in K_scan])         # (local)
d_tau = np.diff(tau_scan)                                           # (local)
is_monotone = bool(np.all(d_tau > 0))                               # (local)

print(f"--- Cross-check 2: monotonicity of tau_GGE(K) ---")
print(f"K scan range: [{K_scan[0]:.3f}, {K_scan[-1]:.3e}]")
print(f"n points: {len(K_scan)}")
print(f"min(d tau / d K) > 0: {is_monotone}")
assert is_monotone, "tau_GGE(K) not monotone increasing (contradicts II.C claim)."
print(f"PASS: tau_GGE is monotone increasing across corridor.")
print()

# ----------------------------------------------------------------------------
# Cross-check 3: unit conversion to SI seconds (V.5 consistency)
# ----------------------------------------------------------------------------
# 1 / M_KK in GeV^-1 units: tau [1/M_KK] = tau / (M_KK [GeV]) * hbar_GeV_s
# equivalent: time scale of 1/M_KK in seconds
tau_unit_seconds = hbar_GeV_s / M_KK                                # (local) 1/M_KK in s
t1_seconds = t1 * tau_unit_seconds                                  # (local)
t2_seconds = t2 * tau_unit_seconds                                  # (local)
t1_dt      = t1 / dt_transit                                        # (local)
t2_dt      = t2 / dt_transit                                        # (local)

print(f"--- Cross-check 3: SI-second conversion (V.5 detector-window context) ---")
print(f"1/M_KK in s         = {tau_unit_seconds:.4e}")
print(f"tau_GGE(K={K1})     = {t1_seconds:.4e} s  ({t1_dt:.3e} * dt_transit)")
print(f"tau_GGE(K={K2:.2e}) = {t2_seconds:.4e} s  ({t2_dt:.3e} * dt_transit)")
print(f"ratio (seconds)     = {t2_seconds / t1_seconds:.4e}  (should equal {ratio:.4e})")
assert abs((t2_seconds / t1_seconds) - ratio) / ratio < 1e-14, "SI-unit ratio mismatch."
print()

# V.5 sanity: at K=1.6e5, tau_GGE should be ~2.4e-36 s (from Landau synthesis V.5)
# (V.5 used K=1.6e5 specifically; expected ~2.71e5 / M_KK * 8.86e-42 s = 2.40e-36 s)
v5_expected_s_order = 2.40e-36                                      # (local) from V.5 pre-reg
v5_rel = abs(t2_seconds - v5_expected_s_order) / v5_expected_s_order  # (local)
print(f"V.5 anchor check at K=1.6e5: expected ~{v5_expected_s_order:.2e} s, got {t2_seconds:.4e} s")
print(f"  relative distance   = {v5_rel:.3e}")
# allow ~5% tolerance (V.5 prefactor uses M_KK gravity, different digit precision)
assert v5_rel < 0.05, f"V.5 anchor failed (rel={v5_rel:.3e})."
print(f"  PASS: V.5 anchor preserved within 5% tolerance.")
print()

# ----------------------------------------------------------------------------
# Cross-check 4: II.C table anchor values (K=1 and K=2.035)
# ----------------------------------------------------------------------------
# From Landau synthesis II.C table:
#   K=1.0: tau_GGE = 1.692 /M_KK
#   K=2.035: tau_GGE = 3.442 /M_KK
tau_K1_synth      = 1.692                                           # (local)
tau_K2035_synth   = 3.442                                           # (local)

tau_K1_computed    = compute_tau_GGE(K=1.0)                         # (local)
tau_K2035_computed = compute_tau_GGE(K=2.035)                       # (local)

err_K1     = abs(tau_K1_computed - tau_K1_synth) / tau_K1_synth     # (local)
err_K2035  = abs(tau_K2035_computed - tau_K2035_synth) / tau_K2035_synth  # (local)

print(f"--- Cross-check 4: II.C table anchor reproduction ---")
print(f"K=1.0:    synthesis=1.692     computed={tau_K1_computed:.4f}    rel err={err_K1:.3e}")
print(f"K=2.035:  synthesis=3.442     computed={tau_K2035_computed:.4f}    rel err={err_K2035:.3e}")
# synthesis table uses 4-sig-fig rounding => tolerate 1e-3
assert err_K1 < 1e-3 and err_K2035 < 1e-3, "II.C anchor table not reproduced."
print(f"PASS: II.C table values reproduced within 1e-3 tolerance.")
print()

# ----------------------------------------------------------------------------
# Verdict
# ----------------------------------------------------------------------------
if ratio >= PASS_THRESH:
    verdict = "PASS"                                                # (local)
elif ratio >= INFO_THRESH:
    verdict = "INFO"                                                # (local)
else:
    verdict = "FAIL"                                                # (local)

print(f"=== Verdict Summary ===")
print(f"tau_GGE(K=2.035)   = {t1:.4e} / M_KK  = {t1_seconds:.4e} s")
print(f"tau_GGE(K=1.6e5)   = {t2:.4e} / M_KK  = {t2_seconds:.4e} s")
print(f"Ratio              = {ratio:.4e}")
print(f"Gate threshold     = {PASS_THRESH} (PASS), {INFO_THRESH} (INFO)")
print(f"\nVerdict: {verdict}")
print(f"4-tuple: (tau_ratio={ratio:.4e}, scheme=GGE-relaxation-timescale, "
      f"convention=K=2.035-vs-K=1.6e5, L_max=N/A)")
print(f"sha256={closure_sha}")

# ----------------------------------------------------------------------------
# Persist: npz + png
# ----------------------------------------------------------------------------
npz_path = OUTPUT_STEM.with_suffix('.npz')                          # (local)
png_path = OUTPUT_STEM.with_suffix('.png')                          # (local)

np.savez(
    npz_path,
    K1=K1,
    K2=K2,
    Delta_BCS=Delta_BCS,
    t1=t1,
    t2=t2,
    ratio=ratio,
    direct_K_ratio=direct_K_ratio,
    rel_error=rel_error,
    t1_seconds=t1_seconds,
    t2_seconds=t2_seconds,
    t1_dt=t1_dt,
    t2_dt=t2_dt,
    K_scan=K_scan,
    tau_scan=tau_scan,
    is_monotone=is_monotone,
    v5_expected_s_order=v5_expected_s_order,
    v5_rel=v5_rel,
    tau_K1_synth=tau_K1_synth,
    tau_K2035_synth=tau_K2035_synth,
    tau_K1_computed=tau_K1_computed,
    tau_K2035_computed=tau_K2035_computed,
    err_K1=err_K1,
    err_K2035=err_K2035,
    PASS_THRESH=PASS_THRESH,
    INFO_THRESH=INFO_THRESH,
    verdict=verdict,
    closure_sha=closure_sha,
)

# Plot: tau_GGE(K) across corridor with K1, K2, and gate thresholds
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.0, 4.5))

# Left: tau_GGE(K) on log-log
ax1.loglog(K_scan, tau_scan, color='tab:blue', linewidth=2.0,
           label=r'$\tau_{\rm GGE}(K) = \pi K / (4 \Delta_{\rm BCS})$')
ax1.axvline(K1, linestyle='--', color='tab:green', alpha=0.7,
            label=fr'$K_1 = {K1}$ (primary)')
ax1.axvline(K2, linestyle='--', color='tab:red', alpha=0.7,
            label=fr'$K_2 = {K2:.1e}$ (W1-E)')
ax1.scatter([K1], [t1], color='tab:green', s=80, zorder=5)
ax1.scatter([K2], [t2], color='tab:red', s=80, zorder=5)
ax1.set_xlabel(r'$K$ (squeezing factor)')
ax1.set_ylabel(r'$\tau_{\rm GGE}$  [$1/M_{\rm KK}$]')
ax1.set_title(r'S83 G40: $\tau_{\rm GGE}(K)$ across corridor')
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, which='both', alpha=0.3)

# Right: ratio vs gate thresholds
ratios_scan = tau_scan / t1                                         # (local)
ax2.loglog(K_scan, ratios_scan, color='tab:purple', linewidth=2.0,
           label=r'$\tau_{\rm GGE}(K) / \tau_{\rm GGE}(K_1)$')
ax2.axhline(PASS_THRESH, linestyle='--', color='tab:green', alpha=0.8,
            label=f'PASS threshold = {PASS_THRESH:.0f}')
ax2.axhline(INFO_THRESH, linestyle='--', color='tab:orange', alpha=0.8,
            label=f'INFO threshold = {INFO_THRESH:.0f}')
ax2.axvline(K2, linestyle=':', color='tab:red', alpha=0.7)
ax2.scatter([K2], [ratio], color='tab:red', s=100, zorder=5,
            label=f'ratio at $K_2$ = {ratio:.2e}')
ax2.set_xlabel(r'$K$')
ax2.set_ylabel(r'$\tau_{\rm GGE}(K) / \tau_{\rm GGE}(K_1)$')
ax2.set_title(f'Ratio vs gate thresholds ({verdict})')
ax2.legend(loc='lower right', fontsize=9)
ax2.grid(True, which='both', alpha=0.3)

fig.tight_layout()
fig.savefig(png_path, dpi=120)
plt.close(fig)

print(f"\nSaved: {npz_path}")
print(f"Saved: {png_path}")

# ----------------------------------------------------------------------------
# Verdict line emission (caller appends to s83_gate_verdicts.txt)
# ----------------------------------------------------------------------------
verdict_line = (
    f"S83-TAU-GGE-AT-K: {verdict} -- "
    f"value=tau_ratio={ratio:.4e} "
    f"scheme=GGE-relaxation-timescale "
    f"convention=K=2.035-vs-K=1.6e5 "
    f"L_max=N/A "
    f"sha256={closure_sha}"
)
print(f"\n{verdict_line}")
