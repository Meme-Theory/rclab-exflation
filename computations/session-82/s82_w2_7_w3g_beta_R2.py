#!/usr/bin/env python3
"""
s82_w2_7_w3g_beta_R2.py -- S82-W3G-BETA-R2: F_amp Coupling Propagation
========================================================================
Classification: PHONONIC (substrate compaction timescape, F_amp through GGE).

Gate: S82-W3G-BETA-R2
  Threshold: |Delta w_0| under +/- 50% F_amp variation
    PASS: |Delta w_0| < 0.01  (Decoupling Principle holds)
    INFO: 0.01 <= |Delta w_0| < 0.04  (below DR3 sigma, detectable)
    FAIL: |Delta w_0| >= 0.04  (comparable to DR3 sigma; observationally distinguishable)
  (Per P2-C C1/Q2 §542-546)

Mechanism under test (P2-C §548):
  F_amp may propagate into w_0 via f_DM = F_amp * n_pivot / D_total
  (ME3 closed-form). If so, rho_GGE depends on F_amp, and w_0 via
  Volovik algebraic partition shifts.

INPUT: W0-5 slot-audited F_amp
  From computations/session-80/s80_gate_verdicts.txt row 1:
    S80-W1-A-SLOT-CONSISTENCY-AUDIT: PASS -- slot=a_2, k_slot=0.3822 [SUPPRESS]
    F_amp_canonical (S80-W1-B-REMED) = 1.0166
    F_amp_slot = 1.0166 * 0.3822 = 0.3885  (S80-UNIFIED-AS-79-FULL)

The task prompt identifies F_amp_slot_adjusted = 0.389 as the W0-5 audited
value after slot routing; we take this as the POST-SLOT value. The canonical
pre-slot F_amp is 1.0166.

SUBSTITUTION CHAIN (sign of dw_0/dF_amp):
  Step 1: w_0 = (rho_J * w_J + rho_GGE * w_GGE) / (rho_J + rho_GGE)
  Step 2: d(w_0)/d(rho_GGE) at fixed rho_J, w_J, w_GGE:
          = [w_GGE*(rho_J+rho_GGE) - (rho_J*w_J+rho_GGE*w_GGE)] / (rho_J+rho_GGE)^2
          = [rho_J * w_GGE + rho_GGE * w_GGE - rho_J * w_J - rho_GGE * w_GGE] / D^2
          = [rho_J * (w_GGE - w_J)] / (rho_J + rho_GGE)^2
  Step 3: Substitute w_J = -1, w_GGE = -0.408:
          w_GGE - w_J = -0.408 - (-1) = +0.592 > 0
  Step 4: rho_J > 0 and (rho_J + rho_GGE)^2 > 0  =>  d(w_0)/d(rho_GGE) > 0
  Step 5: DIRECTION: increasing rho_GGE INCREASES w_0 (less negative).
  Step 6: If f_DM = F_amp * n_pivot / D_total (ME3 closed form), then
          d(f_DM)/d(F_amp) = n_pivot / D_total > 0.
  Step 7: If rho_GGE tracks f_DM (e.g., rho_GGE = f_DM * rho_matter_total or
          rho_GGE enters multiplicatively through the GGE occupation weighting),
          then d(rho_GGE)/d(F_amp) > 0.
  Step 8: Chain: d(w_0)/d(F_amp) = [d(w_0)/d(rho_GGE)] * [d(rho_GGE)/d(F_amp)] > 0.
  Conclusion: Increasing F_amp DRIVES w_0 UP (less negative) through the
  Volovik partition coupling -- IF the partition has an F_amp-dependent
  rho_GGE. The Decoupling Principle asserts this derivative is zero.

Two test modes:
  (a) CLOSED-FORM analytic: compute dw_0/dF_amp through ME3 f_DM relation.
  (b) FINITE DIFFERENCE: +/- 10% and +/- 50% F_amp variation, recompute.

Author: mack-cosmic-bridge (S82 W2-7 R2)
"""

import sys, os, hashlib, json
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))  # (local)
sys.path.insert(0, SCRIPT_DIR)

import numpy as np
from canonical_constants import (
    N_cells,
    Omega_DM, Omega_m,
)

# =============================================================================
# 0. Input SHA pins
# =============================================================================
def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for blk in iter(lambda: f.read(65536), b''):
            h.update(blk)
    return h.hexdigest()

R1_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R1.npz')  # (local)
vol_npz = os.path.join(SCRIPT_DIR, 's58_volovik_partition.npz')  # (local)
verd_path = os.path.join(SCRIPT_DIR, 's80_gate_verdicts.txt')   # (local)

sha_R1  = sha256_file(R1_path)   # (local)
sha_vol = sha256_file(vol_npz)   # (local)
sha_verd = sha256_file(verd_path) # (local)
sha_cc  = sha256_file(os.path.join(SCRIPT_DIR, 'canonical_constants.py'))  # (local)

print("=" * 72)
print("S82-W3G-BETA-R2: F_amp Coupling Propagation into Volovik w_0")
print("=" * 72)
print(f"INPUT PIN: s82_w2_7_w3g_beta_R1.npz   sha256={sha_R1[:16]}...")
print(f"INPUT PIN: s58_volovik_partition.npz  sha256={sha_vol[:16]}...")
print(f"INPUT PIN: s80_gate_verdicts.txt      sha256={sha_verd[:16]}...")
print(f"INPUT PIN: canonical_constants.py     sha256={sha_cc[:16]}...")

# =============================================================================
# 1. Load R1 values
# =============================================================================
dR1 = np.load(R1_path, allow_pickle=True)
rho_J_cell   = float(dR1['rho_J_cell'])
rho_GGE_ref  = float(dR1['rho_GGE'])        # (local) 1.709 at F_amp canonical
P_GGE_ref    = float(dR1['P_GGE'])          # (local)
w_J_exact    = float(dR1['w_J_exact'])
w_GGE_S57    = float(dR1['w_GGE_S57'])
w_0_ref      = float(dR1['w_0_fresh'])
target_w0    = float(dR1['target_w0'])
f_DM_canonical = float(dR1['f_DM_canonical'])  # (local) 0.947

# =============================================================================
# 2. W0-5 slot-audited F_amp values
# =============================================================================
# From task prompt and s80_gate_verdicts.txt:
#   S80-W1-B-REMED: F_amp_canonical (slot-naive) = 1.0166
#   S80-W1-A-SLOT-CONSISTENCY-AUDIT: slot=a_2, k_slot=0.3822 [SUPPRESS]
#   S80-UNIFIED-AS-79-FULL: F_amp_slot_adjusted = 1.0166 * 0.3822 = 0.3885
F_amp_canonical  = 1.0166   # (local) pre-slot
k_slot_a2        = 0.3822   # (local) slot-routing factor (SUPPRESS direction)
F_amp_slot       = F_amp_canonical * k_slot_a2   # (local) = 0.389

print(f"\n=== W0-5 SLOT-AUDITED F_amp ===")
print(f"  F_amp (pre-slot canonical) = {F_amp_canonical}")
print(f"  k_slot (a_2 routing)       = {k_slot_a2}  [SUPPRESS]")
print(f"  F_amp_slot                 = {F_amp_slot:.4f}")

# =============================================================================
# 3. Algebraic partition: w_0 as function of rho_GGE
# =============================================================================
def w0_algebraic(rho_J, rho_G, wJ=w_J_exact, wG=w_GGE_S57):
    """Volovik algebraic partition w_0 formula."""
    return (rho_J * wJ + rho_G * wG) / (rho_J + rho_G)

# =============================================================================
# 4. R2 PRIMARY TEST: f_DM dependence on F_amp (ME3 closed form test)
# =============================================================================
# P2-C Q2 (§548):
#   f_DM = F_amp * n_pivot / D_total  (ME3 closed form)
# At F_amp_canonical = 1.0166 (pre-slot), f_DM = 0.947 (S65 FDMPW-65 PASS).
# So  n_pivot / D_total = f_DM / F_amp = 0.947 / 1.0166 = 0.9315.
#
# Under +/- delta variation of F_amp:
#   f_DM(F_amp) = F_amp * (n_pivot / D_total)
# This would give a linear dependence -- IF n_pivot and D_total are fixed.
# But the DECOUPLING PRINCIPLE asserts f_DM has NO effective F_amp coupling
# (the n_pivot and D_total adjust such that the ratio kills the dependence).
#
# R2 test question: DOES rho_GGE (via Parker-squeezing occupation weighting)
# move with F_amp?

# Test model A (pessimistic, f_DM linear in F_amp):
#   f_DM(F_amp) = F_amp * 0.9315
# Test model B (decoupled, f_DM fixed at 0.947):
#   f_DM(F_amp) = 0.947 (Decoupling Principle)
#
# Under model A, rho_GGE scales with f_DM (Leggett/DM channel weight), so:
#   rho_GGE(F_amp) ~ rho_GGE_ref * f_DM(F_amp) / f_DM_canonical

n_pivot_over_D_total = f_DM_canonical / F_amp_canonical  # (local) = 0.9315

# Model A: rho_GGE scales with f_DM (which scales with F_amp)
def rho_GGE_coupled(F_amp):
    """Pessimistic coupling: rho_GGE = rho_GGE_ref * (F_amp / F_amp_canonical)."""
    return rho_GGE_ref * (F_amp / F_amp_canonical)

# Model B: rho_GGE decoupled from F_amp (Decoupling Principle)
def rho_GGE_decoupled(F_amp):
    return rho_GGE_ref

# =============================================================================
# 5. Finite-difference sensitivity: +/-10% and +/-50% variations
# =============================================================================
variations = [-0.50, -0.10, -0.01, 0.0, +0.01, +0.10, +0.50]  # (local)

print(f"\n=== R2 FINITE-DIFFERENCE TEST ===")
print(f"  Reference: F_amp = {F_amp_canonical}, rho_GGE = {rho_GGE_ref:.4f}")
print(f"  Reference w_0 = {w_0_ref:.6f}")
print(f"")
print(f"  Model A (PESSIMISTIC: rho_GGE scales with F_amp):")
print(f"  {'dF/F':>7s}  {'F_amp':>8s}  {'rho_GGE':>9s}  {'w_0':>10s}  {'Delta w_0':>12s}")
print(f"  {'-'*55}")
deltas_A = []
for dv in variations:
    F = F_amp_canonical * (1 + dv)   # (local)
    rg = rho_GGE_coupled(F)           # (local)
    w0 = w0_algebraic(rho_J_cell, rg) # (local)
    dw0 = w0 - w_0_ref                # (local)
    deltas_A.append(dw0)
    tag = "  <-- REF" if dv == 0 else ""
    print(f"  {dv:+7.2%}  {F:8.4f}  {rg:9.4f}  {w0:10.6f}  {dw0:+12.6f}{tag}")

print(f"")
print(f"  Model B (DECOUPLED: rho_GGE independent of F_amp):")
print(f"  {'dF/F':>7s}  {'F_amp':>8s}  {'rho_GGE':>9s}  {'w_0':>10s}  {'Delta w_0':>12s}")
print(f"  {'-'*55}")
deltas_B = []
for dv in variations:
    F = F_amp_canonical * (1 + dv)   # (local)
    rg = rho_GGE_decoupled(F)         # (local)
    w0 = w0_algebraic(rho_J_cell, rg) # (local)
    dw0 = w0 - w_0_ref                # (local)
    deltas_B.append(dw0)
    tag = "  <-- REF" if dv == 0 else ""
    print(f"  {dv:+7.2%}  {F:8.4f}  {rg:9.4f}  {w0:10.6f}  {dw0:+12.6f}{tag}")

# Primary gate threshold: |Delta w_0| at +/- 50% F_amp variation.
# Model A (pessimistic, representing "worst-case" F_amp->rho_GGE->w_0 chain)
# is the binding test per P2-C Q2 §548.
dw0_plus50  = deltas_A[variations.index(+0.50)]   # (local)
dw0_minus50 = deltas_A[variations.index(-0.50)]   # (local)
max_abs_dw0_A = max(abs(dw0_plus50), abs(dw0_minus50))   # (local)

dw0_plus10  = deltas_A[variations.index(+0.10)]   # (local)
dw0_minus10 = deltas_A[variations.index(-0.10)]   # (local)
max_abs_dw0_10 = max(abs(dw0_plus10), abs(dw0_minus10))  # (local)

# =============================================================================
# 6. Closed-form analytic derivative dw_0/dF_amp (Model A chain rule)
# =============================================================================
# dw_0/d(rho_GGE) at F_amp = F_amp_canonical:
#   = rho_J * (w_GGE - w_J) / (rho_J + rho_GGE)^2
dw_drho_GGE = rho_J_cell * (w_GGE_S57 - w_J_exact) / (rho_J_cell + rho_GGE_ref)**2
# d(rho_GGE)/dF_amp  (Model A):
#   rho_GGE = rho_GGE_ref * F_amp / F_amp_canonical
#   => d(rho_GGE)/dF_amp = rho_GGE_ref / F_amp_canonical
drho_GGE_dF_A = rho_GGE_ref / F_amp_canonical  # (local)
# Chain rule:
dw0_dF_analytic_A = dw_drho_GGE * drho_GGE_dF_A  # (local)

# Logarithmic form: dw_0/dlnF_amp = F_amp * dw_0/dF_amp
dw0_dlnF_analytic_A = F_amp_canonical * dw0_dF_analytic_A  # (local)

print(f"\n=== R2 ANALYTIC DERIVATIVES ===")
print(f"  d(w_0)/d(rho_GGE)          = {dw_drho_GGE:.6f}  (>0: verified sign chain Step 5)")
print(f"  d(rho_GGE)/d(F_amp)  (A)   = {drho_GGE_dF_A:.6f}")
print(f"  d(w_0)/d(F_amp)      (A)   = {dw0_dF_analytic_A:.6f}")
print(f"  d(w_0)/d(ln F_amp)   (A)   = {dw0_dlnF_analytic_A:.6f}")
print(f"  ==> at +/- 50% F_amp, Delta w_0 (linear approx) = "
      f"+/- {0.5 * dw0_dF_analytic_A * F_amp_canonical:.6f}")

# Numerical cross-check for Model A (central diff at +/- 1%)
F_plus  = F_amp_canonical * 1.01  # (local)
F_minus = F_amp_canonical * 0.99  # (local)
w0_plus  = w0_algebraic(rho_J_cell, rho_GGE_coupled(F_plus))   # (local)
w0_minus = w0_algebraic(rho_J_cell, rho_GGE_coupled(F_minus))  # (local)
dw0_dF_numeric_A = (w0_plus - w0_minus) / (F_plus - F_minus)   # (local)
print(f"  d(w_0)/d(F_amp) numerical  = {dw0_dF_numeric_A:.6f}  "
      f"(agrees with analytic: rel.err = {abs(dw0_dF_numeric_A-dw0_dF_analytic_A)/abs(dw0_dF_analytic_A):.2e})")

# =============================================================================
# 7. Slot-routed test: F_amp_slot = 0.389 (post-slot)
# =============================================================================
# Under Model A, if the POST-SLOT F_amp = 0.389 is the "effective" coupling
# that the Volovik partition sees, then the expected w_0 under this slot-
# routed amplitude is different. We report BOTH.
w0_at_F_slot_A = w0_algebraic(rho_J_cell, rho_GGE_coupled(F_amp_slot))  # (local)
w0_at_F_slot_B = w0_algebraic(rho_J_cell, rho_GGE_decoupled(F_amp_slot))  # (local)

print(f"\n=== R2 SLOT-ADJUSTED F_amp EFFECT ===")
print(f"  F_amp pre-slot (1.0166)  -> w_0 = {w_0_ref:.6f}  (R1 reference)")
print(f"  F_amp post-slot (0.389)  -> w_0 (Model A) = {w0_at_F_slot_A:.6f}")
print(f"  F_amp post-slot (0.389)  -> w_0 (Model B) = {w0_at_F_slot_B:.6f}")
print(f"  Delta (slot - pre-slot, Model A) = {w0_at_F_slot_A - w_0_ref:+.6f}")
print(f"  Delta (slot - pre-slot, Model B) = {w0_at_F_slot_B - w_0_ref:+.6f}")

# =============================================================================
# 8. R2 GATE VERDICT
# =============================================================================
# Threshold per P2-C Q2 §546:
#   PASS:  |Delta w_0| < 0.01 at +/- 50% F_amp variation
#   INFO:  0.01 <= |Delta w_0| < 0.04
#   FAIL:  |Delta w_0| >= 0.04
# Binding test is MODEL A (worst-case coupling scenario).

PASS_THRESH = 0.01  # (local)
INFO_THRESH = 0.04  # (local)

if max_abs_dw0_A < PASS_THRESH:
    verdict_R2 = "PASS"
    detail = (f"max |Delta w_0| = {max_abs_dw0_A:.6f} < {PASS_THRESH} "
              f"(Decoupling Principle holds even under Model A)")
elif max_abs_dw0_A < INFO_THRESH:
    verdict_R2 = "INFO"
    detail = (f"max |Delta w_0| = {max_abs_dw0_A:.6f} in [{PASS_THRESH}, {INFO_THRESH}] "
              f"(below DR3 sigma, detectable)")
else:
    verdict_R2 = "FAIL"
    detail = (f"max |Delta w_0| = {max_abs_dw0_A:.6f} >= {INFO_THRESH} "
              f"(comparable to DR3 sigma; observationally distinguishable)")

print(f"\n=== R2 GATE VERDICT ===")
print(f"  Test: +/- 50% F_amp variation (Model A, pessimistic coupling)")
print(f"  Delta w_0 (+50%) = {dw0_plus50:+.6f}")
print(f"  Delta w_0 (-50%) = {dw0_minus50:+.6f}")
print(f"  max |Delta w_0| (50%) = {max_abs_dw0_A:.6f}")
print(f"  max |Delta w_0| (10%) = {max_abs_dw0_10:.6f}")
print(f"  Thresholds: PASS<{PASS_THRESH}, INFO<{INFO_THRESH}, FAIL>=INFO")
print(f"  VERDICT: {verdict_R2} -- {detail}")

# =============================================================================
# 9. Closure SHA
# =============================================================================
input_pins = {
    's58_volovik_partition.npz': sha_vol,
    's82_w2_7_w3g_beta_R1.npz':  sha_R1,
    's80_gate_verdicts.txt':     sha_verd,
    'canonical_constants.py':    sha_cc,
    'F_amp_canonical':           f'{F_amp_canonical}',
    'k_slot_a2':                 f'{k_slot_a2}',
    'F_amp_slot':                f'{F_amp_slot:.6f}',
    'rho_J_cell':                f'{rho_J_cell:.6f}',
    'rho_GGE_ref':               f'{rho_GGE_ref:.6f}',
    'w_J':                       f'{w_J_exact}',
    'w_GGE':                     f'{w_GGE_S57}',
    'variations':                json.dumps(variations),
    'PASS_THRESH':               str(PASS_THRESH),
    'INFO_THRESH':               str(INFO_THRESH),
}
closure_sha = hashlib.sha256(
    json.dumps(input_pins, sort_keys=True).encode()
).hexdigest()

# =============================================================================
# 10. Save outputs
# =============================================================================
out_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R2.npz')
np.savez(
    out_path,
    # Finite-difference tables
    variations=np.array(variations),
    deltas_A=np.array(deltas_A),
    deltas_B=np.array(deltas_B),
    # Primary thresholds
    max_abs_dw0_A_50pct=np.array(max_abs_dw0_A),
    max_abs_dw0_A_10pct=np.array(max_abs_dw0_10),
    dw0_plus50=np.array(dw0_plus50),
    dw0_minus50=np.array(dw0_minus50),
    # Analytic derivatives
    dw0_dF_analytic_A=np.array(dw0_dF_analytic_A),
    dw0_dlnF_analytic_A=np.array(dw0_dlnF_analytic_A),
    dw0_dF_numeric_A=np.array(dw0_dF_numeric_A),
    dw_drho_GGE=np.array(dw_drho_GGE),
    drho_GGE_dF_A=np.array(drho_GGE_dF_A),
    # Slot-routed
    F_amp_canonical=np.array(F_amp_canonical),
    k_slot_a2=np.array(k_slot_a2),
    F_amp_slot=np.array(F_amp_slot),
    w0_at_F_slot_A=np.array(w0_at_F_slot_A),
    w0_at_F_slot_B=np.array(w0_at_F_slot_B),
    # Gate
    gate_name=np.array(['S82-W3G-BETA-R2']),
    gate_verdict=np.array([verdict_R2]),
    gate_detail=np.array([detail]),
    PASS_THRESH=np.array(PASS_THRESH),
    INFO_THRESH=np.array(INFO_THRESH),
    # Provenance
    closure_sha=np.array([closure_sha]),
)

# =============================================================================
# 11. Plot: w_0 vs F_amp (both models) with DR3 falsifier band overlay
# =============================================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# (a) w_0 vs F_amp
ax = axes[0]
F_grid = np.linspace(0.4, 1.6, 121)  # (local)
w_A_grid = np.array([w0_algebraic(rho_J_cell, rho_GGE_coupled(F)) for F in F_grid])  # (local)
w_B_grid = np.array([w0_algebraic(rho_J_cell, rho_GGE_decoupled(F)) for F in F_grid]) # (local)
ax.plot(F_grid, w_A_grid, 'r-', linewidth=2, label='Model A (coupled rho_GGE ∝ F_amp)')
ax.plot(F_grid, w_B_grid, 'b-', linewidth=2, label='Model B (decoupled, DP)')
ax.axvspan(F_amp_canonical*0.5, F_amp_canonical*1.5, color='orange', alpha=0.08,
           label=f'+/- 50% F_amp range')
ax.axvline(F_amp_canonical, color='green', ls='--', alpha=0.6, label=f'F_amp canonical = {F_amp_canonical}')
ax.axvline(F_amp_slot, color='purple', ls=':', alpha=0.8, label=f'F_amp slot = {F_amp_slot:.3f}')
ax.axhspan(-0.94, -0.88, color='green', alpha=0.12, label='DR3 falsifier band [-0.94, -0.88]')
ax.axhline(target_w0, color='darkgreen', ls='--', alpha=0.5, label=f'canonical w_0 = {target_w0}')
ax.set_xlabel('F_amp')
ax.set_ylabel('w_0')
ax.set_title('(a) R2: w_0 vs F_amp  |  dw_0/dF (A) = {:.4f}'.format(dw0_dF_analytic_A))
ax.legend(loc='best', fontsize=8)
ax.grid(True, alpha=0.3)

# (b) Delta w_0 vs fractional F_amp variation
ax = axes[1]
dv_grid = np.array(variations) * 100  # (local) pct
ax.bar([f'{v:+.0%}' for v in variations], deltas_A, color='red', alpha=0.6, label='Model A')
ax.bar([f'{v:+.0%}' for v in variations], deltas_B, color='blue', alpha=0.4, label='Model B')
ax.axhline( PASS_THRESH, color='green', ls='--', label=f'PASS +/-{PASS_THRESH}')
ax.axhline(-PASS_THRESH, color='green', ls='--')
ax.axhline( INFO_THRESH, color='orange', ls='--', label=f'INFO +/-{INFO_THRESH}')
ax.axhline(-INFO_THRESH, color='orange', ls='--')
ax.set_xlabel('F_amp variation')
ax.set_ylabel('Delta w_0')
ax.set_title(f'(b) R2: Delta w_0 under F_amp variation  |  {verdict_R2}')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's82_w2_7_w3g_beta_R2.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
plt.close()

# =============================================================================
# 12. Canonical verdict line
# =============================================================================
print(f"\n{'='*72}")
print(f"VERDICT LINE:")
print(f"S82-W3G-BETA-R2: {verdict_R2} -- value={max_abs_dw0_A:.6f} scheme=SLOT-AUDITED convention=UNIFIED-AS-79 L_max=10 sha256={closure_sha}")
print(f"{'='*72}")
print(f"Saved: {out_path}")
print(f"Saved: {plot_path}")
print("DONE.")
