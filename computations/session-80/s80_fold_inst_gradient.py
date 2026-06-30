#!/usr/bin/env python3
"""
S80 W1-3: FOLD-INST-GRADIENT (CF-5)
====================================

GATE [VERIFY]: S80-FOLD-INST-GRADIENT
HYPOTHESIS: dS_inst/dtau (instanton-action gradient) concentrates at
  tau_fold = 0.190, providing a 4th independent functional for Fold
  Transit Event Sec VII.I promotion.

PRE-REG: Compute dS_inst/dtau at tau in {0.15, 0.17, 0.19, 0.21, 0.25}.
PASS: max |dS_inst/dtau| at tau in [0.17, 0.21]     (|Delta tau| <= 0.02)
INFO: max |dS_inst/dtau| in [0.15, 0.17) U (0.21, 0.25]  (0.02-0.05)
FAIL: max displaced > 0.05 OR flat profile

Agent: kaku-speculative-theorist (instanton expert)
Classification: GEOMETRIC (instanton action derivative under Jensen tau-var)
Substrate framing: The instanton is a topological configuration of the
  internal fiber geometry, NOT a solution embedded in spacetime. dS_inst/dtau
  measures how the topological-sector weight of the fiber's eigenvalue
  spectrum reorganizes with Jensen deformation.

Method (per session-80-plan.md L983-1008):
  Step 1: S_inst(tau) = (8*pi^2 / g_eff^2(tau)) * kappa(tau)
          where kappa(tau) is the Jensen instanton-density correction,
          taken as the ratio of internal curvature invariants K(tau)/K(0)
          (spin-connection instanton density, Baptista eq 3.70).

  Step 2: g_eff^2(tau) = g_base^2 * exp(-2*tau)
          canonical identity g_1/g_2 = e^{-2*tau} (S22a, S42 Kerner route);
          g_base^2 inferred by back-extrapolation of g_SU2_fold to tau=0
          gives g_base^2 = 3.0 (matches g0_diag = 3.0 at round SU(3),
          Killing-metric normalization).

  Step 3: dS_inst/dtau via central differences on the 5-point scan,
          interior points only (per prompt pseudo-code). Fine-grid check
          validates monotonicity.

  Step 4: Read direction from canonical form; state verdict after Python print.

S22c s22c_instanton_action.py precedent: the SAME channels enter (R, K, Weyl^2).
That script showed the gravitational channel prefers large tau (decompactification)
and the YM channel prefers small tau. THIS script computes the SINGLE-instanton
combination using the spin-connection/Kretschmann density (which is the canonical
internal-space analog of the CC96 (1/g^2) instanton weight).

NOTE: The analytic structure predicts monotonically increasing |dS_inst/dtau|
on [0, 0.30] because:
  - exp(+2*tau) is monotone increasing (weakening coupling)
  - K(tau) is monotone increasing on [0, 2] (Baptista eq 3.70)
Their product has no interior minimum. The peak of |dS_inst/dtau| should
therefore be at the RIGHT boundary of the scan window, NOT at tau_fold.

This computation SHOULD FAIL if endpoints are included in the argmax.
Interior-only argmax (per prompt pseudo-code) restricts to {0.17, 0.19, 0.21}
and yields a boundary PASS at tau=0.21 that is an ARTIFACT of the
central-difference restriction, not a physical concentration signal.

The finding is structural: dS_inst/dtau is MONOTONE, not fold-concentrated.
It is NOT a qualifying 4th independent functional for Sec VII.I promotion.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
import sys
import hashlib
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import (
    tau_fold,
    dS_fold,
    d2S_fold,
    g_SU2_fold,
    g0_diag,
    PI,
)

# -----------------------------------------------------------------------
# Exact Jensen-SU(3) curvature invariants (Baptista eq 3.70, s22c_instanton_action)
# -----------------------------------------------------------------------
def K_exact(s):
    """Kretschmann invariant K(s) on Jensen SU(3). s is the Jensen parameter tau."""
    return (
        (23.0 / 96) * np.exp(-8 * s)
        - 1.0 * np.exp(-5 * s)
        + (5.0 / 16) * np.exp(-4 * s)
        + (11.0 / 6) * np.exp(-2 * s)
        - (3.0 / 2) * np.exp(-s)
        + 17.0 / 32
        + (1.0 / 12) * np.exp(4 * s)
    )

def R_exact(s):
    """Scalar curvature R(s) -- exact (Baptista eq 3.70)."""
    return (2 * np.exp(2 * s) - 1 + 8 * np.exp(-s) - np.exp(-4 * s)) / 4.0

# -----------------------------------------------------------------------
# Canonical coupling: g_base^2 inferred from g_SU2_fold via g_1/g_2 = e^{-2*tau}
# canonical identity. If g^2(tau) = g_base^2 * exp(-2*tau), then
# g_base^2 = g_SU2_fold * exp(+2 * tau_fold)
# -----------------------------------------------------------------------
g_base_sq = g_SU2_fold * np.exp(2.0 * tau_fold)  # (local) inferred g^2 at tau=0
# Sanity: should equal g0_diag = 3.0 (round SU(3) Killing normalization)
assert abs(g_base_sq - g0_diag) < 1e-6, (
    f"g_base_sq={g_base_sq} disagrees with g0_diag={g0_diag} (canonical Killing norm)"
)
print(f"[sanity] g_base^2 (from canonical) = {g_base_sq:.6f}, g0_diag = {g0_diag}")
print(f"[sanity] 8*pi^2 / g_base^2 = {8 * PI**2 / g_base_sq:.6f}")

# -----------------------------------------------------------------------
# Spectral-action single-instanton form
#    S_inst(tau) = (8*pi^2 / g_eff^2(tau)) * kappa(tau)
#                = (8*pi^2 / g_base^2) * exp(+2*tau) * K(tau)/K(0)
# Dimensional-analysis check: dimensionless in M_KK units (both factors
# are dimensionless; K is a curvature-squared per length^{-4}, normalized by K(0)).
# -----------------------------------------------------------------------
K0 = K_exact(0.0)  # (local)

def S_inst(tau):
    """Single-instanton action on Jensen SU(3), spectral-action form."""
    return (8.0 * PI**2 / g_base_sq) * np.exp(2.0 * tau) * K_exact(tau) / K0

# -----------------------------------------------------------------------
# Pre-registered 5-point tau scan
# -----------------------------------------------------------------------
tau_vals = np.array([0.15, 0.17, 0.19, 0.21, 0.25])  # (local) pre-reg scan
S_vals = np.array([S_inst(t) for t in tau_vals])  # (local)

print()
print("=" * 64)
print("S80 W1-3: FOLD-INST-GRADIENT -- pre-registered 5-point scan")
print("=" * 64)
print(f"{'tau':>6s} {'S_inst(tau)':>14s}")
for t, s in zip(tau_vals, S_vals):
    print(f"{t:6.2f} {s:14.8f}")
print()

# -----------------------------------------------------------------------
# Central differences at interior points (matches prompt pseudo-code)
# Step h_i = tau[i+1] - tau[i-1]; dS/dtau[i] ~ (S[i+1] - S[i-1]) / h_i
# -----------------------------------------------------------------------
dS_dtau = np.zeros_like(tau_vals)  # (local)
dS_dtau[1:-1] = (S_vals[2:] - S_vals[:-2]) / (tau_vals[2:] - tau_vals[:-2])
# Forward/backward differences at endpoints (diagnostic only; NOT used for argmax)
dS_dtau[0] = (S_vals[1] - S_vals[0]) / (tau_vals[1] - tau_vals[0])
dS_dtau[-1] = (S_vals[-1] - S_vals[-2]) / (tau_vals[-1] - tau_vals[-2])

print("Central differences (interior) and one-sided (endpoints):")
print(f"{'tau':>6s} {'dS/dtau':>14s}")
for t, d in zip(tau_vals, dS_dtau):
    print(f"{t:6.2f} {d:14.6f}")
print()

# -----------------------------------------------------------------------
# Peak location -- per prompt pseudo-code: interior-only argmax
# -----------------------------------------------------------------------
idx_peak_interior = np.argmax(np.abs(dS_dtau[1:-1])) + 1  # (local)
tau_peak_interior = tau_vals[idx_peak_interior]  # (local)
dS_peak_interior = dS_dtau[idx_peak_interior]  # (local)

# Full argmax (diagnostic, includes endpoints)
idx_peak_all = np.argmax(np.abs(dS_dtau))  # (local)
tau_peak_all = tau_vals[idx_peak_all]  # (local)
dS_peak_all = dS_dtau[idx_peak_all]  # (local)

delta_tau_interior = abs(tau_peak_interior - tau_fold)  # (local)
delta_tau_all = abs(tau_peak_all - tau_fold)  # (local)

print(f"Interior-argmax tau_peak = {tau_peak_interior}, |Delta tau| = {delta_tau_interior:.4f}")
print(f"All-points argmax tau_peak = {tau_peak_all}, |Delta tau| = {delta_tau_all:.4f}")
print()

# -----------------------------------------------------------------------
# Fine-grid diagnostic: is |dS/dtau| monotone on the window?
# -----------------------------------------------------------------------
tau_fine = np.linspace(0.01, 0.35, 341)  # (local)
S_fine = S_inst(tau_fine)  # (local)
dS_fine = np.gradient(S_fine, tau_fine)  # (local)
d2S_fine = np.gradient(dS_fine, tau_fine)  # (local)
is_monotone_increasing = np.all(np.diff(dS_fine) > 0)  # (local)
inflection_sign_changes = np.where(np.diff(np.sign(d2S_fine)))[0]  # (local)

print(f"[diagnostic] dS/dtau monotone increasing on [0.01, 0.35]? {is_monotone_increasing}")
if len(inflection_sign_changes) > 0:
    inflections = [tau_fine[i] for i in inflection_sign_changes]  # (local)
    print(f"[diagnostic] d^2 S/dtau^2 inflection points at tau = {inflections}")
else:
    print(f"[diagnostic] No d^2 S/dtau^2 sign changes on [0.01, 0.35] -- dS/dtau is strictly monotone.")

# FWHM of |dS/dtau| peak (if any)
peak_val = np.max(dS_fine)  # (local)
peak_tau = tau_fine[np.argmax(dS_fine)]  # (local)
half_max = 0.5 * peak_val  # (local)
above_half = dS_fine > half_max  # (local)
if np.any(above_half):
    idx_above = np.where(above_half)[0]  # (local)
    fwhm = tau_fine[idx_above[-1]] - tau_fine[idx_above[0]]  # (local)
    print(f"[diagnostic] Fine-grid peak: tau = {peak_tau:.4f}, dS/dtau = {peak_val:.4f}")
    print(f"[diagnostic] FWHM of |dS/dtau| (half-max width) = {fwhm:.4f}")
else:
    fwhm = float('nan')  # (local)
    print(f"[diagnostic] No half-max region found.")

# -----------------------------------------------------------------------
# Cross-check variants -- does choice of kappa(tau) change the verdict?
# V1: K/K0   (Kretschmann, canonical spin-connection density)
# V2: R/R0   (scalar curvature, gravitational-instanton density)
# V3: 1      (naive CC96 4D-gauge, no Jensen correction)
# -----------------------------------------------------------------------
print()
print("Cross-check of kappa(tau) variants (interior-argmax tau_peak):")

def gradient_variant(kappa_func):
    """Return (tau_peak_interior, tau_peak_all, monotone_increasing)."""
    S_v = np.array([(8.0 * PI**2 / g_base_sq) * np.exp(2 * t) * kappa_func(t) for t in tau_vals])  # (local)
    dS_v = np.zeros_like(tau_vals)  # (local)
    dS_v[1:-1] = (S_v[2:] - S_v[:-2]) / (tau_vals[2:] - tau_vals[:-2])
    dS_v[0] = (S_v[1] - S_v[0]) / (tau_vals[1] - tau_vals[0])
    dS_v[-1] = (S_v[-1] - S_v[-2]) / (tau_vals[-1] - tau_vals[-2])
    idx_int = np.argmax(np.abs(dS_v[1:-1])) + 1  # (local)
    idx_all = np.argmax(np.abs(dS_v))  # (local)
    # fine grid monotonicity
    S_fn = np.array([(8.0 * PI**2 / g_base_sq) * np.exp(2 * t) * kappa_func(t) for t in tau_fine])  # (local)
    dS_fn = np.gradient(S_fn, tau_fine)  # (local)
    return tau_vals[idx_int], tau_vals[idx_all], bool(np.all(np.diff(dS_fn) > 0))

eps_r0 = 1e-3  # (local) avoid R(0)=0 singularity
variants = [
    ("V1 K(tau)/K(0) Kretschmann", lambda t: K_exact(t) / K0),
    ("V2 R(tau)/R(eps) scalar", lambda t: R_exact(t) / R_exact(eps_r0)),
    ("V3 unit (no Jensen corr)", lambda t: 1.0),
]
variant_results = {}  # (local)
for name, func in variants:
    ti, ta, mono = gradient_variant(func)
    variant_results[name] = (ti, ta, mono)
    print(f"  {name:32s} interior={ti} all-pts={ta} monotone={mono}")
print()

# -----------------------------------------------------------------------
# Verdict selection -- per prompt pseudo-code (interior-argmax)
# -----------------------------------------------------------------------
if delta_tau_interior <= 0.02:
    verdict_interior = "PASS"  # (local)
elif delta_tau_interior <= 0.05:
    verdict_interior = "INFO"  # (local)
else:
    verdict_interior = "FAIL"  # (local)

# Diagnostic: verdict if endpoints are included
if delta_tau_all <= 0.02:
    verdict_all = "PASS"  # (local)
elif delta_tau_all <= 0.05:
    verdict_all = "INFO"  # (local)
else:
    verdict_all = "FAIL"  # (local)

# Structural verdict: monotone profile means NO concentration at fold.
# The interior-argmax PASS is a boundary artifact of restricting
# central differences to {0.17, 0.19, 0.21}.
if is_monotone_increasing and verdict_all == "FAIL":
    structural_verdict = "FAIL"  # (local) underlying profile is monotone, not fold-concentrated
elif is_monotone_increasing:
    structural_verdict = verdict_interior + "-ARTIFACT"  # (local)
else:
    structural_verdict = verdict_interior  # (local)

print("=" * 64)
print("VERDICT SUMMARY")
print("=" * 64)
print(f"  Interior-argmax (per prompt pseudo-code): tau_peak = {tau_peak_interior}, "
      f"|Delta tau| = {delta_tau_interior:.4f}, verdict = {verdict_interior}")
print(f"  All-points argmax (diagnostic): tau_peak = {tau_peak_all}, "
      f"|Delta tau| = {delta_tau_all:.4f}, verdict = {verdict_all}")
print(f"  Fine-grid monotonicity: dS/dtau is "
      f"{'MONOTONE INCREASING (no peak, runaway to right boundary)' if is_monotone_increasing else 'non-monotone'}")
print(f"  Structural verdict: {structural_verdict}")
print()

# Interpretation for session-80-results-workingpaper.md
interpretation = (
    "The naive single-instanton spectral-action form yields a MONOTONE "
    "|dS_inst/dtau| on [0, 0.35] -- the weakening-coupling factor exp(+2*tau) "
    "dominates any internal-curvature modulation from K(tau) or R(tau). "
    "The pre-registered interior-argmax reports PASS at tau=0.21, but this "
    "is an ARTIFACT of restricting central differences to {0.17, 0.19, 0.21}: "
    "the true |dS_inst/dtau| peak is at the RIGHT boundary tau=0.25 "
    "(structural FAIL with |Delta tau|=0.06). "
    "dS_inst/dtau is therefore NOT a qualifying 4th independent functional "
    "for the Fold Transit Event Sec VII.I promotion -- it belongs to a "
    "different functional class (monotone curvature-driven action) than "
    "the three ρ(ε,τ)-integral functionals (chi_a, |beta|^2, slow-mode IPR) "
    "which ARE concentrated at the DoS singularity at tau_fold."
)  # (local)
print("INTERPRETATION (for working paper):")
print(interpretation)
print()

# -----------------------------------------------------------------------
# Plot: dS_inst/dtau vs tau with fold location marked
# -----------------------------------------------------------------------
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

ax = axs[0]
ax.plot(tau_fine, S_fine, 'b-', linewidth=1.5, label='S_inst(tau) fine grid')
ax.plot(tau_vals, S_vals, 'ko', markersize=8, label='5-point pre-reg scan')
ax.axvline(tau_fold, color='r', linestyle='--', alpha=0.6, label=f'tau_fold={tau_fold}')
ax.set_xlabel('tau (Jensen deformation)')
ax.set_ylabel('S_inst(tau)')
ax.set_title('Substrate instanton action S_inst(tau)')
ax.legend(loc='best')
ax.grid(True, alpha=0.3)

ax = axs[1]
ax.plot(tau_fine, dS_fine, 'b-', linewidth=1.5, label='dS_inst/dtau fine grid')
ax.plot(tau_vals, dS_dtau, 'ko', markersize=8, label='5-point central diff')
ax.axvline(tau_fold, color='r', linestyle='--', alpha=0.6, label=f'tau_fold={tau_fold}')
ax.axvline(tau_peak_interior, color='g', linestyle=':', alpha=0.6,
           label=f'interior peak tau={tau_peak_interior}')
ax.axvline(tau_peak_all, color='orange', linestyle=':', alpha=0.6,
           label=f'all-pts peak tau={tau_peak_all}')
ax.set_xlabel('tau (Jensen deformation)')
ax.set_ylabel('dS_inst/dtau')
ax.set_title(f'Gradient dS_inst/dtau: MONOTONE, peak at boundary tau={tau_peak_all}')
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's80_fold_inst_gradient.png')
plt.savefig(plot_path, dpi=140)
print(f"Plot saved: {plot_path}")
plt.close()

# -----------------------------------------------------------------------
# Save NPZ
# -----------------------------------------------------------------------
npz_path = os.path.join(SCRIPT_DIR, 's80_fold_inst_gradient.npz')  # (local)
np.savez(
    npz_path,
    tau_vals=tau_vals,
    S_vals=S_vals,
    dS_dtau=dS_dtau,
    tau_peak_interior=tau_peak_interior,
    dS_peak_interior=dS_peak_interior,
    delta_tau_interior=delta_tau_interior,
    tau_peak_all=tau_peak_all,
    dS_peak_all=dS_peak_all,
    delta_tau_all=delta_tau_all,
    verdict_interior=verdict_interior,
    verdict_all=verdict_all,
    structural_verdict=structural_verdict,
    is_monotone_increasing=is_monotone_increasing,
    fwhm=fwhm,
    tau_fine=tau_fine,
    S_fine=S_fine,
    dS_fine=dS_fine,
    g_base_sq=g_base_sq,
    tau_fold=tau_fold,
    kappa_scheme='K(tau)/K(0) Kretschmann spin-connection density',
    scheme='single-instanton',
    convention='Jensen-deformation',
    L_max=5,  # (local)
)
print(f"Data saved: {npz_path}")

# -----------------------------------------------------------------------
# sha256 closure fingerprint (for audit) -- NPZ byte hash of core arrays
# -----------------------------------------------------------------------
core_payload = np.concatenate([  # (local)
    tau_vals.flatten(), S_vals.flatten(), dS_dtau.flatten(),
    np.array([tau_peak_interior, tau_peak_all,
              delta_tau_interior, delta_tau_all,
              dS_peak_interior, dS_peak_all,
              g_base_sq, float(is_monotone_increasing)])
])
sha_closure = hashlib.sha256(core_payload.tobytes()).hexdigest()[:16]  # (local)
print(f"sha256 closure: {sha_closure}")

# -----------------------------------------------------------------------
# Gate verdict line for s80_gate_verdicts.txt
# -----------------------------------------------------------------------
timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())  # (local)
verdict_line = (
    f"[{timestamp}] S80-FOLD-INST-GRADIENT | {structural_verdict} | "
    f"tau_peak_interior={tau_peak_interior} | delta_interior={delta_tau_interior:.4f} | "
    f"tau_peak_all={tau_peak_all} | delta_all={delta_tau_all:.4f} | "
    f"dS_peak_interior={dS_peak_interior:.4f} | dS_peak_all={dS_peak_all:.4f} | "
    f"monotone_increasing={is_monotone_increasing} | "
    f"verdict_interior_artifact={verdict_interior} | verdict_all_points={verdict_all} | "
    f"4-tuple=(dS_inst_dtau_peak={dS_peak_all:.4f},scheme=single-instanton,"
    f"convention=Jensen-deformation,L_max=5) | "
    f"classification=GEOMETRIC | "
    f"interpretation=monotone-profile-not-fold-concentrated-interior-PASS-is-boundary-artifact | "
    f"sha256={sha_closure} | agent=kaku-speculative-theorist | "
    f"script=s80_fold_inst_gradient.py\n"
)
verdicts_path = os.path.join(SCRIPT_DIR, 's80_gate_verdicts.txt')
with open(verdicts_path, 'a') as f:
    f.write(verdict_line)
print(f"Verdict appended to: {verdicts_path}")

print()
print("=" * 64)
print(f"S80 W1-3 FOLD-INST-GRADIENT complete: {structural_verdict}")
print("=" * 64)
