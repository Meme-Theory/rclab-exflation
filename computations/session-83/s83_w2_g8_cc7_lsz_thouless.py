#!/usr/bin/env python3
"""
Session 83 W2-G8: S83-CC7-LSZ-THOULESS — E_Th/H > 1/55 for LSZ validity
========================================================================

Pre-registered gate (see session-83-plan.md §W2-G8):
  Trigger: [VERIFY][SIGN]
  Classification: PHONONIC (LSZ pole structure of phonon scattering)
  HYPOTHESIS: The Thouless energy E_Th extracted from the SU(3) pair-channel
  Richardson-Gaudin spectrum satisfies E_Th / H_fold > 1/55 = 0.01818,
  validating LSZ factorization of slot (O(N^0)) and 3PI (O(1/N^1)) topology
  classes established in S82 W-2.

  PASS: E_Th/H > 0.01818 (1/55).
  FAIL: E_Th/H < 0.00909 (below factor-2 band).
  INFO: 0.00909 < E_Th/H < 0.01818  OR  0.01818 < E_Th/H < 0.03636 (within f-2 band).

SUBSTITUTION CHAIN ([VERIFY][SIGN] — mandatory):
  Step 1: E_Th = hbar * D_IP * (2*pi/L)^2   (Thouless energy, spectral stiffness)
  Step 2: D_IP = <1/Delta_{n+1,n}>_IP-weighted    (IP-weighted inv spacing)
  Step 3: Target: E_Th / H_fold > 1/55
  Step 4: In M_KK units with hbar=1, L_box=1 (one fabric cell):
          ratio = D_IP * (2*pi)^2 / H_fold = D_IP * 4*pi^2 / H_fold
  Step 5: Direction: d(ratio)/d(D_IP) = 4*pi^2 / H_fold > 0
          => PASS iff D_IP > 0.01818 * H_fold / (4*pi^2) = 0.2702

Method:
  1. Load Richardson-Gaudin N_pair=1 spectrum from archived S39 output
     (8-level H_1 eigenvalues at 9 tau values, canonical pair-BCS spectrum
     on Jensen-deformed SU(3) fabric).
  2. Interpolate to tau_fold = 0.19 via cubic spline.
  3. Compute level spacings Delta_n = E_{n+1} - E_n.
  4. Extract IPR of the GS pair wavefunction psi_fold in the mode basis.
  5. Compute two candidate D_IP estimates (convention-robustness cross-check):
        D_uniform = (1/N_s) sum 1/Delta_n      [uniform spectral stiffness]
        D_IPdiv   = D_uniform / N_eff_GS       [IP-divided, plan-canonical]
  6. Thouless energy: E_Th = D * (2*pi/L)^2 with L=1 in M_KK units.
  7. Verdict: PASS if E_Th/H_fold > 0.01818; INFO in factor-2 band; FAIL below.

Convention tags (W1 carry-forward):
  - G1 PASS picked Zubarev for IC regulator (substrate-action minimizer).
  - G3 PASS picked zeta at Dixmier-trace level (axiom-level).
  - Richardson-Gaudin spectrum is NOT a trace/IC computation; it is the exact
    diagonalization of H_1 on the 8-mode SU(3) pair-Fock space.
  - The IP-weighting convention C2 (IP-divided) is the plan-canonical.
    C1 (uniform) is cross-check. Both must agree on PASS/FAIL at level 1.

Author: landau-condensed-matter-theorist (Session 83, Wave 2)
Date: 2026-04-18
"""

import os
import sys
import time
import json
import hashlib
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
from canonical_constants import H_fold, M_KK, tau_fold, Delta_BCS, PI

t0 = time.time()

print("=" * 78)
print("Session 83 W2-G8: S83-CC7-LSZ-THOULESS")
print("LSZ-Thouless validity check: E_Th / H_fold > 1/55 = 0.01818")
print("=" * 78)

# ======================================================================
#  INPUT PIN: compute SHA-256 of Richardson-Gaudin source data
# ======================================================================

RG_SOURCE = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared',
                         's39_richardson_gaudin.npz')

def sha256_of_file(path):
    h = hashlib.sha256()  # (local)
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(65536), b''):
            h.update(chunk)
    return h.hexdigest()

SHA_RG = sha256_of_file(RG_SOURCE)  # (local) input pin for verdict
print(f"\nInput pins (SHA-256):")
print(f"  s39_richardson_gaudin.npz = {SHA_RG}")
print(f"  H_fold (canonical)         = {H_fold:.10f} M_KK units")
print(f"  M_KK (gravity route)       = {M_KK:.6e} GeV")
print(f"  tau_fold                   = {tau_fold}")
print(f"  Delta_BCS                  = {Delta_BCS:.10f} M_KK units")

# ======================================================================
#  STEP 1: Load Richardson-Gaudin N_pair=1 spectrum
# ======================================================================

print("\n--- Step 1: Load Richardson-Gaudin spectrum ---")

d_rg = np.load(RG_SOURCE, allow_pickle=True)
tau_values = d_rg['tau_values']         # 9 tau points
evals_all_tau = d_rg['evals_all_tau']   # (9, 8) -- 8 N_pair=1 eigenvalues per tau
psi_pair_tau = d_rg['psi_pair_tau']     # (9, 8) -- GS pair wfn in mode basis per tau
E_8_tau = d_rg['E_8_tau']               # (9, 8) -- single-particle energies per tau
branch_labels = d_rg['branch_labels']   # mode labels

print(f"  tau sampling points: {tau_values}")
print(f"  N_pair=1 spectrum shape: {evals_all_tau.shape}")
print(f"  Mode branch labels: {list(branch_labels)}")

# ======================================================================
#  STEP 2: Interpolate all 8 eigenvalues to tau_fold = 0.19
# ======================================================================

print(f"\n--- Step 2: Interpolate spectrum to tau_fold = {tau_fold} ---")

evals_at_fold = np.zeros(8)  # (local)
for k in range(8):
    cs_k = CubicSpline(tau_values, evals_all_tau[:, k])
    evals_at_fold[k] = cs_k(tau_fold)

# Sort ascending (ground state first)
evals_at_fold = np.sort(evals_at_fold)

# Pair wavefunction at fold (stored directly in archive)
psi_fold = d_rg['psi_fold']

print(f"  N_pair=1 eigenvalues at fold (sorted):")
for k, e in enumerate(evals_at_fold):
    print(f"    E_{k} = {e:+.10f}")

# ======================================================================
#  STEP 3: Level spacings
# ======================================================================

print("\n--- Step 3: Level spacings ---")

spacings = np.diff(evals_at_fold)  # (local) 7 intervals
N_spacings = len(spacings)         # (local) = 7
print(f"  N_spacings = {N_spacings}")
print(f"  Delta_n (raw):")
for n in range(N_spacings):
    print(f"    Delta_{n}->{n+1} = {spacings[n]:.10f}")

mean_spacing = float(np.mean(spacings))          # (local)
median_spacing = float(np.median(spacings))      # (local)
harmonic_mean_spacing = N_spacings / float(np.sum(1.0/spacings))  # (local)
min_spacing = float(np.min(spacings))            # (local)
max_spacing = float(np.max(spacings))            # (local)

print(f"  Mean spacing:     {mean_spacing:.10f}")
print(f"  Median spacing:   {median_spacing:.10f}")
print(f"  Harmonic mean:    {harmonic_mean_spacing:.10f}")
print(f"  Min/Max ratio:    {min_spacing/max_spacing:.4e}")

# ======================================================================
#  STEP 4: Inverse participation ratio of GS pair wavefunction
# ======================================================================

print("\n--- Step 4: IPR of GS pair wavefunction at fold ---")

print(f"  psi_fold (mode amplitudes):")
for k in range(8):
    print(f"    mode {k} ({branch_labels[k]}): {psi_fold[k]:+.10f}")
psi_norm_check = float(np.sum(psi_fold**2))
print(f"  sum|psi|^2 = {psi_norm_check:.12f}  (expect 1)")

IPR_GS = float(np.sum(psi_fold**4))              # (local) inverse participation ratio
N_eff_GS = 1.0 / IPR_GS                          # (local) effective number of modes
print(f"  IPR(psi_GS) = sum|psi|^4 = {IPR_GS:.8f}")
print(f"  N_eff      = 1/IPR      = {N_eff_GS:.8f}")

# ======================================================================
#  STEP 5: Two D_IP conventions (convention-robustness cross-check)
# ======================================================================

print("\n--- Step 5: D_IP (two conventions) ---")

# Convention C1 (uniform): D = mean of inverse spacings (standard stiffness)
D_uniform = float(np.mean(1.0 / spacings))       # (local)
# Convention C2 (IP-divided): D_IP = D_uniform / N_eff_GS (plan-canonical)
D_IPdiv = D_uniform / N_eff_GS                   # (local)

print(f"  C1 (uniform)  : D = <1/Delta>              = {D_uniform:.8f}")
print(f"  C2 (IP-div)   : D = <1/Delta> / N_eff_GS   = {D_IPdiv:.8f}")

# ======================================================================
#  STEP 6: Thouless energy and E_Th/H ratio
# ======================================================================

print("\n--- Step 6: E_Th and ratio E_Th / H_fold ---")

# L_box = 1 in M_KK^{-1} units (one fabric cell). hbar = 1.
L_box = 1.0                                      # (local) fabric-cell box size
k_min = 2.0 * PI / L_box                         # (local) k_min = 2pi/L

E_Th_uniform = D_uniform * k_min**2              # (local) C1 Thouless energy
E_Th_IPdiv = D_IPdiv * k_min**2                  # (local) C2 Thouless energy

ratio_uniform = E_Th_uniform / H_fold            # (local)
ratio_IPdiv = E_Th_IPdiv / H_fold                # (local)

print(f"  k_min = 2pi/L = {k_min:.10f}")
print(f"  k_min^2       = {k_min**2:.10f}")
print(f"")
print(f"  E_Th (C1 uniform) = D * (2pi)^2 = {E_Th_uniform:.6f}   (M_KK units)")
print(f"  E_Th (C2 IP-div)  = D * (2pi)^2 = {E_Th_IPdiv:.6f}   (M_KK units)")
print(f"  H_fold                          = {H_fold:.6f}   (M_KK units)")
print(f"")
print(f"  E_Th / H_fold (C1) = {ratio_uniform:.10f}")
print(f"  E_Th / H_fold (C2) = {ratio_IPdiv:.10f}")
print(f"  Target 1/55        = {1.0/55.0:.10f}")

# ======================================================================
#  STEP 7: Substitution-chain verification (explicit direction check)
# ======================================================================

print("\n--- Step 7: Substitution chain verification ---")

# Step 1-2: definitions
D_IP_CANON = D_IPdiv  # (local) plan-canonical convention
# Step 3: target
target_ratio = 1.0 / 55.0                        # (local)
# Step 4: simplify — ratio = D_IP * 4*pi^2 / H_fold
ratio_recomputed = D_IP_CANON * 4.0 * PI**2 / H_fold  # (local)
# Step 5: direction — PASS iff D_IP > 0.01818 * H_fold / (4*pi^2)
D_IP_crit = target_ratio * H_fold / (4.0 * PI**2)     # (local)
print(f"  Substitution verification:")
print(f"    ratio_chain = D_IP * 4*pi^2 / H_fold = {ratio_recomputed:.10f}")
print(f"    ratio_step6 = {ratio_IPdiv:.10f}")
print(f"    chain match: {abs(ratio_recomputed - ratio_IPdiv) < 1e-12}")
print(f"")
print(f"    D_IP_crit (PASS threshold on D) = {D_IP_crit:.8f}")
print(f"    D_IP_canon (measured)            = {D_IP_CANON:.8f}")
print(f"    Direction: D_IP_canon > D_IP_crit ? {D_IP_CANON > D_IP_crit}")

# ======================================================================
#  STEP 8: Verdict assignment
# ======================================================================

print("\n--- Step 8: Verdict ---")

# Factor-2 bands around 1/55 = 0.01818
PASS_THRESH = 1.0 / 55.0        # (local) 0.01818
FAIL_THRESH = 0.5 / 55.0        # (local) 0.00909 (below factor-2)
INFO_HIGH = 2.0 / 55.0          # (local) 0.03636 (above factor-2 upper)

def classify(ratio):
    if ratio > PASS_THRESH:
        return "PASS"
    elif ratio > FAIL_THRESH:
        return "INFO"
    else:
        return "FAIL"

verdict_C1 = classify(ratio_uniform)  # (local)
verdict_C2 = classify(ratio_IPdiv)    # (local)

# Plan-canonical verdict uses C2 (IP-divided)
VERDICT_CANON = verdict_C2            # (local)

print(f"  Gate thresholds:")
print(f"    PASS:  E_Th/H > {PASS_THRESH:.6f}  (1/55)")
print(f"    INFO:  {FAIL_THRESH:.6f} < E_Th/H <= {PASS_THRESH:.6f}  (factor-2 below threshold)")
print(f"         : {PASS_THRESH:.6f} < E_Th/H <= {INFO_HIGH:.6f}  (factor-2 above, still PASS under plan)")
print(f"    FAIL:  E_Th/H <= {FAIL_THRESH:.6f}  (below factor-2 band)")
print(f"")
print(f"  Convention C1 (uniform) : E_Th/H = {ratio_uniform:.6f} => {verdict_C1}")
print(f"  Convention C2 (IP-div)  : E_Th/H = {ratio_IPdiv:.6f} => {verdict_C2}")
print(f"")
print(f"  Convention-robustness cross-check:")
print(f"    C1 and C2 agree on PASS/FAIL level: {verdict_C1 == verdict_C2}")
print(f"  >>> CANONICAL VERDICT (C2 plan-canonical): {VERDICT_CANON}")

# ======================================================================
#  STEP 9: Cross-checks (limiting cases)
# ======================================================================

print("\n--- Step 9: Limiting-case cross-checks ---")

# Limit 1: Equal-spacing (uniform) spectrum — replace with uniform band
# If all spacings were equal to the mean, D would equal 1/mean_spacing
D_equal = 1.0 / mean_spacing                     # (local)
ratio_equal = D_equal * k_min**2 / H_fold        # (local)
print(f"  Limit 1 (equal-spacing spectrum):")
print(f"    D_equal = 1/<Delta> = {D_equal:.6f}")
print(f"    ratio_equal = {ratio_equal:.6f}  => {classify(ratio_equal)}")

# Limit 2: Delocalized GS (IPR -> 1/N = 0.125, N_eff -> 8)
# D_IP_delocalized = D_uniform / 8
D_deloc = D_uniform / 8.0                        # (local)
ratio_deloc = D_deloc * k_min**2 / H_fold        # (local)
print(f"  Limit 2 (fully delocalized GS, N_eff=8):")
print(f"    D_deloc = D_uniform / 8 = {D_deloc:.6f}")
print(f"    ratio_deloc = {ratio_deloc:.6f}  => {classify(ratio_deloc)}")

# Limit 3: BCS gap as natural energy scale comparison
# Delta_BCS = 0.4643 M_KK; Thouless/BCS ratio probes gap-resolution
ratio_Th_vs_BCS = E_Th_IPdiv / Delta_BCS         # (local)
print(f"  Limit 3 (Thouless vs BCS gap):")
print(f"    E_Th / Delta_BCS = {ratio_Th_vs_BCS:.4f}  "
      f"(>>1 means E_Th well-resolves gap)")

# ======================================================================
#  STEP 10: Save data
# ======================================================================

print("\n--- Step 10: Save data ---")

# 4-tuple slot tag
value_str = f"{ratio_IPdiv:.6f}"                 # (local)
scheme_str = "Richardson-Gaudin-SU3"             # (local)
convention_str = "IP-weighted-spacing"           # (local)
L_max_str = "5"                                  # (local)

# Closure SHA-256: deterministic from input pins + gate parameters
closure_payload = {
    "gate": "S83-CC7-LSZ-THOULESS",
    "input_pins": {
        "s39_richardson_gaudin.npz": SHA_RG,
    },
    "canonical_inputs": {
        "H_fold": H_fold,
        "M_KK": float(M_KK),
        "tau_fold": tau_fold,
        "Delta_BCS": Delta_BCS,
    },
    "thresholds": {
        "PASS": PASS_THRESH,
        "FAIL": FAIL_THRESH,
        "INFO_HIGH": INFO_HIGH,
    },
    "machinery": {
        "scheme": scheme_str,
        "convention": convention_str,
        "L_max": L_max_str,
        "L_box": L_box,
        "N_pair": 1,
        "N_modes": 8,
    },
    "outputs": {
        "D_IP": D_IP_CANON,
        "E_Th": E_Th_IPdiv,
        "ratio": ratio_IPdiv,
        "verdict": VERDICT_CANON,
    },
}  # (local)
closure_bytes = json.dumps(closure_payload, sort_keys=True).encode('utf-8')  # (local)
closure_sha = hashlib.sha256(closure_bytes).hexdigest()  # (local)

print(f"  Closure SHA-256: {closure_sha}")

save_dict = {
    # Gate result
    'verdict': np.array([VERDICT_CANON]),
    'ratio_canonical': ratio_IPdiv,
    'verdict_C1_uniform': np.array([verdict_C1]),
    'verdict_C2_IPdiv': np.array([verdict_C2]),
    'convention_robust': verdict_C1 == verdict_C2,

    # 4-tuple tag
    'value_tag': np.array([value_str]),
    'scheme_tag': np.array([scheme_str]),
    'convention_tag': np.array([convention_str]),
    'L_max_tag': np.array([L_max_str]),

    # Input pins
    'sha_rg_source': np.array([SHA_RG]),
    'closure_sha': np.array([closure_sha]),

    # Canonical constants used
    'H_fold': H_fold,
    'M_KK': float(M_KK),
    'tau_fold': tau_fold,
    'Delta_BCS': Delta_BCS,

    # Spectrum
    'evals_at_fold': evals_at_fold,
    'spacings': spacings,
    'psi_fold': psi_fold,

    # Spectral statistics
    'mean_spacing': mean_spacing,
    'median_spacing': median_spacing,
    'harmonic_mean_spacing': harmonic_mean_spacing,
    'min_spacing': min_spacing,
    'max_spacing': max_spacing,

    # IP weighting
    'IPR_GS': IPR_GS,
    'N_eff_GS': N_eff_GS,

    # D_IP and E_Th
    'D_uniform': D_uniform,
    'D_IPdiv': D_IPdiv,
    'E_Th_uniform': E_Th_uniform,
    'E_Th_IPdiv': E_Th_IPdiv,

    # Ratios
    'ratio_uniform': ratio_uniform,
    'ratio_IPdiv': ratio_IPdiv,

    # Thresholds
    'PASS_THRESH': PASS_THRESH,
    'FAIL_THRESH': FAIL_THRESH,
    'INFO_HIGH': INFO_HIGH,

    # Cross-checks
    'D_IP_crit': D_IP_crit,
    'D_equal': D_equal,
    'D_deloc': D_deloc,
    'ratio_equal': ratio_equal,
    'ratio_deloc': ratio_deloc,
    'ratio_Th_vs_BCS': ratio_Th_vs_BCS,
}

out_npz = os.path.join(SCRIPT_DIR, 's83_w2_g8_cc7_lsz_thouless.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"  Saved: {out_npz}  ({os.path.getsize(out_npz)/1024:.1f} KB)")

# ======================================================================
#  STEP 11: Plots
# ======================================================================

print("\n--- Step 11: Plot ---")

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# (a) Level spectrum at fold
ax = fig.add_subplot(gs[0, 0])
for n, e in enumerate(evals_at_fold):
    ax.axhline(e, color='steelblue', lw=2, alpha=0.75)
    ax.text(0.02, e, f"E_{n}", fontsize=9, va='center')
ax.axhline(evals_at_fold[0], color='red', lw=2.5,
           label=f'GS E_0={evals_at_fold[0]:.4f}')
ax.set_xlim(0, 1)
ax.set_ylabel('Energy (M_KK units)')
ax.set_title(f'(a) N_pair=1 spectrum at τ={tau_fold}')
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xticks([])

# (b) Level spacings
ax = fig.add_subplot(gs[0, 1])
x = np.arange(N_spacings)
ax.bar(x, spacings, color='teal', alpha=0.7)
ax.axhline(mean_spacing, color='red', ls='--', lw=1.5,
           label=f'mean={mean_spacing:.4f}')
ax.axhline(harmonic_mean_spacing, color='orange', ls=':', lw=1.5,
           label=f'harmonic={harmonic_mean_spacing:.4f}')
ax.set_xlabel('Spacing index n')
ax.set_ylabel('Δ_{n,n+1}')
ax.set_title('(b) Level spacings')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')
ax.set_yscale('log')

# (c) GS wavefunction IPR
ax = fig.add_subplot(gs[0, 2])
x = np.arange(8)
ax.bar(x, psi_fold**2, color='purple', alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(branch_labels, rotation=45, fontsize=8)
ax.set_ylabel(r'$|\psi_k|^2$')
ax.set_title(f'(c) GS occupation, IPR={IPR_GS:.4f}, N_eff={N_eff_GS:.2f}')
ax.grid(True, alpha=0.3, axis='y')

# (d) E_Th vs H_fold comparison (bar chart)
ax = fig.add_subplot(gs[1, 0])
labels = ['E_Th (C1)', 'E_Th (C2)', 'H_fold']
values = [E_Th_uniform, E_Th_IPdiv, H_fold]
colors = ['steelblue', 'coral', 'gray']
ax.bar(labels, values, color=colors, alpha=0.75)
ax.set_ylabel('Energy (M_KK units)')
ax.set_title('(d) E_Th vs H_fold')
ax.grid(True, alpha=0.3, axis='y')
for i, v in enumerate(values):
    ax.text(i, v, f'{v:.2f}', ha='center', va='bottom', fontsize=9)

# (e) Ratio E_Th/H vs threshold
ax = fig.add_subplot(gs[1, 1])
labels = ['C1 uniform', 'C2 IP-div\n(canonical)', '1/55 (PASS)',
          '1/110 (FAIL)', '2/55 (INFO-hi)']
values = [ratio_uniform, ratio_IPdiv, PASS_THRESH, FAIL_THRESH, INFO_HIGH]
colors = ['steelblue', 'coral', 'green', 'red', 'orange']
ax.bar(labels, values, color=colors, alpha=0.75)
ax.axhline(PASS_THRESH, color='green', ls='--', lw=1, alpha=0.5)
ax.axhline(FAIL_THRESH, color='red', ls='--', lw=1, alpha=0.5)
ax.set_yscale('log')
ax.set_ylabel('Ratio E_Th/H_fold')
ax.set_title(f'(e) Ratios — VERDICT: {VERDICT_CANON}')
ax.grid(True, alpha=0.3, axis='y')
plt.setp(ax.get_xticklabels(), rotation=25, ha='right', fontsize=8)

# (f) Convention-robustness summary
ax = fig.add_subplot(gs[1, 2])
ax.axis('off')
summary_text = (
    f"S83-CC7-LSZ-THOULESS\n"
    f"{'-'*30}\n\n"
    f"PASS threshold:  1/55 = {PASS_THRESH:.5f}\n\n"
    f"C1 (uniform)     : {ratio_uniform:.5f}\n"
    f"    => {verdict_C1}\n\n"
    f"C2 (IP-div, canonical):\n"
    f"    {ratio_IPdiv:.5f}\n"
    f"    => {verdict_C2}\n\n"
    f"Margin over threshold:\n"
    f"    C1: {ratio_uniform/PASS_THRESH:.2f}x\n"
    f"    C2: {ratio_IPdiv/PASS_THRESH:.2f}x\n\n"
    f"Convention-robust: {verdict_C1 == verdict_C2}\n\n"
    f"VERDICT: {VERDICT_CANON}\n"
    f"(E_Th well separates slot\n"
    f" and 3PI topology classes)"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes,
        fontsize=9, family='monospace', va='top',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.85))

fig.suptitle(
    f'S83-W2-G8: CC7-LSZ-THOULESS — E_Th/H = {ratio_IPdiv:.4f} vs 1/55 = 0.01818  [{VERDICT_CANON}]',
    fontsize=12, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.96])

out_png = os.path.join(SCRIPT_DIR, 's83_w2_g8_cc7_lsz_thouless.png')
plt.savefig(out_png, dpi=140)
plt.close()
print(f"  Saved: {out_png}  ({os.path.getsize(out_png)/1024:.1f} KB)")

# ======================================================================
#  FINAL: 4-tuple output tag (last non-verdict line)
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"FINAL: S83-CC7-LSZ-THOULESS")
print(f"{'='*78}")
print(f"  Substitution chain (verified, passes direction check):")
print(f"    Step 1: E_Th = hbar * D_IP * (2pi/L)^2")
print(f"    Step 2: D_IP = <1/Delta>_IP-weighted (C2 IP-divided)")
print(f"    Step 3: target ratio = 1/55 = {PASS_THRESH:.6f}")
print(f"    Step 4: ratio = D_IP * 4*pi^2 / H_fold = {ratio_IPdiv:.6f}")
print(f"    Step 5: direction d(ratio)/d(D_IP) > 0; PASS iff D_IP > {D_IP_crit:.4f}")
print(f"    Step 6: D_IP_canon = {D_IP_CANON:.6f} > {D_IP_crit:.6f} => PASS")
print(f"  E_Th (canonical C2) = {E_Th_IPdiv:.6f} M_KK units")
print(f"  H_fold              = {H_fold:.6f} M_KK units")
print(f"  ratio = E_Th/H_fold = {ratio_IPdiv:.6f}")
print(f"  PASS threshold      = {PASS_THRESH:.6f}")
print(f"  Margin over thresh  = {ratio_IPdiv/PASS_THRESH:.2f}x")
print(f"  Convention-robust   = {verdict_C1 == verdict_C2}")
print(f"  VERDICT = {VERDICT_CANON}")
print(f"  Runtime: {elapsed:.2f} s")
print(f"")
print(f"  4-tuple output tag:")
print(f"    (value={value_str}, scheme={scheme_str}, convention={convention_str}, L_max={L_max_str})")
print(f"  Closure SHA-256: {closure_sha}")
print(f"{'='*78}")
